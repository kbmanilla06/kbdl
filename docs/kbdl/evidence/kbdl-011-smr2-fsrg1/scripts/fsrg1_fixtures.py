#!/usr/bin/env python3
"""KBDL-011-SMR2-FSRG1 deterministic fixtures.

Twenty-four negative fixtures and eight positive controls, proving that every
FSRG1 gate fails closed on the defect it targets and accepts the correct state.

ISOLATION
---------
The suite makes exactly one temporary copy of the repository (including .git,
which the generator needs to resolve commit-SHA evidence) and mutates only that
copy. Each fixture restores the files it touched before the next one runs. The
real repository is hashed before and after the whole suite and must be
byte-identical; `git status --short` is also compared. Temporary trees are
removed afterwards, and a cleanup failure fails the suite.

Exit code: 0 only when every fixture produced its expected result, the real
repository is byte-unchanged, and cleanup succeeded.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import field_source_registry as fsr  # noqa: E402
import validate_fsrg1 as vf  # noqa: E402

ARTIFACT_REL = fsr.ARTIFACT_REL
GENERATOR_REL = vf.GENERATOR_REL
HISTORICAL_ROUNDS = vf.HISTORICAL_ROUNDS
REGISTRY_REL = vf.REGISTRY_REL


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> dict:
    """Hash every real repository file the suite could plausibly disturb."""
    state = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/") or "__pycache__" in rel:
            continue
        state[rel] = sha256_file(path)
    return state


class Sandbox:
    """One temporary repository copy, with per-fixture restore."""

    def __init__(self, root: Path, tmp: Path):
        self.origin = root
        self.path = tmp / "repo"
        shutil.copytree(root, self.path, symlinks=True,
                        ignore=shutil.ignore_patterns("__pycache__"))
        self.scratch = tmp / "scratch"
        self.scratch.mkdir(parents=True, exist_ok=True)
        self._dirty = set()

    def restore(self):
        for rel in sorted(self._dirty):
            src = self.origin / rel
            dst = self.path / rel
            if dst.is_symlink() or dst.exists():
                if dst.is_dir() and not dst.is_symlink():
                    shutil.rmtree(dst)
                else:
                    dst.unlink()
            if src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        self._dirty.clear()

    def mark(self, rel: str):
        self._dirty.add(rel)

    def read(self, rel: str) -> str:
        return (self.path / rel).read_text(encoding="utf-8")

    def write(self, rel: str, text: str):
        self.mark(rel)
        p = self.path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        # newline="" keeps the written bytes exactly as given (Python 3.9's
        # Path.write_text has no newline parameter).
        with p.open("w", encoding="utf-8", newline="") as fh:
            fh.write(text)

    def write_bytes(self, rel: str, data: bytes):
        self.mark(rel)
        (self.path / rel).write_bytes(data)

    def remove(self, rel: str):
        self.mark(rel)
        p = self.path / rel
        if p.exists():
            p.unlink()


# --------------------------------------------------------------------------
# Gate runners — each returns the set of failing check names
# --------------------------------------------------------------------------

def failing(fn, *args) -> set:
    c = vf.Checks()
    fn(c, *args)
    return {name for name, ok, _ in c.rows if not ok}


def schema_failures(sb: Sandbox) -> set:
    return failing(vf.check_schema, sb.path)


def coverage_failures(sb: Sandbox) -> set:
    c = vf.Checks()
    rows = vf.check_schema(c, sb.path)
    vf.check_coverage(c, sb.path, rows)
    return {name for name, ok, _ in c.rows if not ok}


def historical_failures(sb: Sandbox) -> set:
    return failing(vf.check_historical, sb.path)


def drift_failures(sb: Sandbox) -> set:
    return failing(vf.check_drift, sb.path)


def two_run_bytes(sb: Sandbox):
    """Run the sandbox generator twice, in different CWDs, separate processes."""
    outputs = []
    for i, cwd in enumerate((sb.scratch, sb.path)):
        artifact = sb.path / ARTIFACT_REL
        if artifact.exists():
            artifact.unlink()
        sb.mark(ARTIFACT_REL)
        result = subprocess.run(
            [sys.executable, str(sb.path / GENERATOR_REL), "--repo-root", str(sb.path)],
            capture_output=True, text=True, cwd=str(cwd))
        if result.returncode != 0 or not artifact.is_file():
            return None, result
        outputs.append(artifact.read_bytes())
    return outputs, None


# --------------------------------------------------------------------------
# Registry mutation helpers
# --------------------------------------------------------------------------

def load_rows(sb: Sandbox):
    text = sb.read(ARTIFACT_REL)
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    return rows[0], rows[1:]


def store_rows(sb: Sandbox, header, body):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(body)
    sb.write_bytes(ARTIFACT_REL, buf.getvalue().encode("utf-8"))


# --------------------------------------------------------------------------
# Negative fixtures
# --------------------------------------------------------------------------

def fx_missing_column(sb):
    header, body = load_rows(sb)
    i = header.index("Ledger value")
    store_rows(sb, [h for j, h in enumerate(header) if j != i],
               [[c for j, c in enumerate(r) if j != i] for r in body])
    return schema_failures(sb), {"SCHEMA.header_exact"}


def fx_extra_column(sb):
    header, body = load_rows(sb)
    store_rows(sb, header + ["Extra"], [r + ["x"] for r in body])
    return schema_failures(sb), {"SCHEMA.header_exact"}


def fx_reordered_columns(sb):
    header, body = load_rows(sb)
    order = list(range(len(header)))
    order[1], order[2] = order[2], order[1]
    store_rows(sb, [header[i] for i in order], [[r[i] for i in order] for r in body])
    return schema_failures(sb), {"SCHEMA.header_exact"}


def fx_inconsistent_row_width(sb):
    header, body = load_rows(sb)
    body[5] = body[5][:-2]
    store_rows(sb, header, body)
    return schema_failures(sb), {"SCHEMA.row_widths_uniform"}


def fx_invalid_domain_value(sb):
    header, body = load_rows(sb)
    body[3][header.index("Ownership class")] = "Z — Invented-owned"
    store_rows(sb, header, body)
    return schema_failures(sb), {"SCHEMA.controlled_domains",
                                 "SCHEMA.ownership_class_matches_field"}


def fx_duplicate_row_key(sb):
    header, body = load_rows(sb)
    body.append(list(body[0]))
    store_rows(sb, header, body)
    return schema_failures(sb), {"SCHEMA.row_key_unique"}


def fx_missing_requirement(sb):
    header, body = load_rows(sb)
    victim = body[0][0]
    store_rows(sb, header, [r for r in body if r[0] != victim])
    return coverage_failures(sb), {"COVER.every_current_requirement_present"}


def fx_missing_field_row(sb):
    header, body = load_rows(sb)
    victim = body[0][0]
    dropped = False
    kept = []
    for r in body:
        if not dropped and r[0] == victim and r[1] == "Known limitation":
            dropped = True
            continue
        kept.append(r)
    store_rows(sb, header, kept)
    return coverage_failures(sb), {"COVER.every_required_field_per_requirement",
                                   "COVER.row_count_is_requirements_times_fields"}


def fx_nondeterministic_row_order(sb):
    """Generator sorts by a random key instead of the declared sort key."""
    src = sb.read(GENERATOR_REL)
    patched = src.replace(
        '    rows.sort(key=lambda r: (r["Requirement ID"], FIELD_ORDER[r["Field name"]]))',
        "    import random\n    random.shuffle(rows)")
    assert patched != src, "fixture setup: sort line not found"
    sb.write(GENERATOR_REL, patched)
    outputs, err = two_run_bytes(sb)
    if outputs is None:
        return {"DETERM.generator_runs"}, {"DETERM.generator_runs"}
    return ({"DETERM.byte_identical"} if outputs[0] != outputs[1] else set()), \
        {"DETERM.byte_identical"}


def fx_environment_dependent_output(sb):
    """Generator injects a timestamp/absolute path into a cell."""
    src = sb.read(GENERATOR_REL)
    patched = src.replace(
        '        "Primary basis": basis,',
        '        "Primary basis": basis + " " + str(__import__("time").time()),')
    assert patched != src, "fixture setup: Primary basis emission not found"
    sb.write(GENERATOR_REL, patched)
    outputs, err = two_run_bytes(sb)
    if outputs is None:
        return {"DETERM.generator_runs"}, {"DETERM.generator_runs"}
    return ({"DETERM.byte_identical"} if outputs[0] != outputs[1] else set()), \
        {"DETERM.byte_identical"}


def fx_hand_edited_registry(sb):
    header, body = load_rows(sb)
    body[10][header.index("Ledger value")] = "HAND EDITED"
    store_rows(sb, header, body)
    return drift_failures(sb), {"DRIFT.committed_matches_regeneration",
                                "DRIFT.independent_regeneration_matches"}


def _mutate_historical(sb, round_name):
    rel = REGISTRY_REL.format(r=round_name)
    sb.mark(rel)
    with (sb.path / rel).open("a", encoding="utf-8") as f:
        f.write("KBDL-A11Y-001,Injected row\n")
    return historical_failures(sb), {f"HIST.{round_name}.byte_identical"}


def fx_mutated_r13(sb):
    return _mutate_historical(sb, "r13")


def fx_mutated_r14(sb):
    return _mutate_historical(sb, "r14")


def fx_mutated_r15(sb):
    return _mutate_historical(sb, "r15")


def fx_mutated_r16(sb):
    return _mutate_historical(sb, "r16")


def _path_attempt(sb, rel_target):
    """Point the declared artifact path at `rel_target` and demand refusal."""
    src = sb.read(GENERATOR_REL)
    patched = src.replace(f'ARTIFACT_REL = f"{{PACKAGE_REL}}/artifacts/field-source-registry.csv"',
                          f'ARTIFACT_REL = {rel_target!r}')
    assert patched != src, "fixture setup: ARTIFACT_REL not found"
    sb.write(GENERATOR_REL, patched)
    result = subprocess.run(
        [sys.executable, str(sb.path / GENERATOR_REL), "--repo-root", str(sb.path)],
        capture_output=True, text=True)
    return result


def fx_absolute_output_path(sb):
    outside = sb.scratch / "absolute-escape.csv"
    result = _path_attempt(sb, str(outside))
    refused = result.returncode != 0 and not outside.exists()
    return ({"PATH.rejected"} if refused else set()), {"PATH.rejected"}


def fx_dotdot_traversal(sb):
    target = "docs/kbdl/evidence/kbdl-011-smr2-fsrg1/artifacts/../../../../escaped.csv"
    result = _path_attempt(sb, target)
    escaped = sb.path / "escaped.csv"
    refused = result.returncode != 0 and not escaped.exists()
    return ({"PATH.rejected"} if refused else set()), {"PATH.rejected"}


def fx_symlink_escape(sb):
    outside = sb.scratch / "symlink-target.csv"
    outside.write_text("sentinel\n", encoding="utf-8")
    artifact = sb.path / ARTIFACT_REL
    sb.mark(ARTIFACT_REL)
    if artifact.exists():
        artifact.unlink()
    artifact.symlink_to(outside)
    result = subprocess.run(
        [sys.executable, str(sb.path / GENERATOR_REL), "--repo-root", str(sb.path)],
        capture_output=True, text=True)
    untouched = outside.read_text(encoding="utf-8") == "sentinel\n"
    if artifact.is_symlink():
        artifact.unlink()
    refused = result.returncode != 0 and untouched
    return ({"PATH.rejected"} if refused else set()), {"PATH.rejected"}


def fx_historical_output_target(sb):
    target = REGISTRY_REL.format(r="r16")
    before = sha256_file(sb.path / target)
    result = _path_attempt(sb, target)
    after = sha256_file(sb.path / target)
    refused = result.returncode != 0 and before == after
    return ({"PATH.rejected"} if refused else set()), {"PATH.rejected"}


def fx_protected_output_target(sb):
    target = "docs/kbdl/traceability-metadata.csv"
    before = sha256_file(sb.path / target)
    result = _path_attempt(sb, target)
    after = sha256_file(sb.path / target)
    refused = result.returncode != 0 and before == after
    return ({"PATH.rejected"} if refused else set()), {"PATH.rejected"}


def fx_fixture_mutating_real_repo(sb):
    """Prove the isolation detector notices a real-repository mutation.

    Simulated against a disposable stand-in 'real' tree so the detector is
    exercised without ever touching the actual repository.
    """
    stand_in = sb.scratch / "standin"
    if stand_in.exists():
        shutil.rmtree(stand_in)
    stand_in.mkdir(parents=True)
    (stand_in / "file.txt").write_text("original\n", encoding="utf-8")
    before = snapshot(stand_in)
    (stand_in / "file.txt").write_text("mutated\n", encoding="utf-8")
    after = snapshot(stand_in)
    detected = before != after
    return ({"ISO.detector"} if detected else set()), {"ISO.detector"}


def fx_empty_generated_output(sb):
    """A generator that yields no rows must fail rather than emit an empty file."""
    src = sb.read(GENERATOR_REL)
    patched = src.replace("    rows = build_rows(model)",
                          "    rows = build_rows(model)\n    rows = []")
    assert patched != src, "fixture setup: build_rows call not found"
    sb.write(GENERATOR_REL, patched)
    result = subprocess.run(
        [sys.executable, str(sb.path / GENERATOR_REL), "--repo-root", str(sb.path)],
        capture_output=True, text=True)
    refused = result.returncode != 0 and "empty" in (result.stderr + result.stdout).lower()
    return ({"GEN.empty_rejected"} if refused else set()), {"GEN.empty_rejected"}


def fx_generator_subprocess_failure(sb):
    """A source the generator cannot parse must fail closed, not emit a registry."""
    sb.remove("docs/kbdl/traceability-metadata.csv")
    before = sha256_file(sb.path / ARTIFACT_REL)
    result = subprocess.run(
        [sys.executable, str(sb.path / GENERATOR_REL), "--repo-root", str(sb.path)],
        capture_output=True, text=True)
    after = sha256_file(sb.path / ARTIFACT_REL)
    failed_closed = result.returncode != 0 and before == after
    drift = drift_failures(sb)
    return (({"GEN.fails_closed"} if failed_closed else set())
            | ({"DRIFT.check_mode_executed"} if "DRIFT.check_mode_executed" in drift
               or "DRIFT.independent_regeneration" in drift else set())), \
        {"GEN.fails_closed"}


def fx_drift_passing_without_generation(sb):
    """With the generator absent, the drift gate must FAIL, never pass vacuously."""
    sb.remove(GENERATOR_REL)
    fails = drift_failures(sb)
    return fails, {"DRIFT.check_mode_executed", "DRIFT.committed_matches_regeneration"}


# --------------------------------------------------------------------------
# Positive controls
# --------------------------------------------------------------------------

def pc_valid_schema(sb):
    return schema_failures(sb), set()


def pc_deterministic_two_runs(sb):
    outputs, err = two_run_bytes(sb)
    if outputs is None:
        return {"DETERM.generator_runs"}, set()
    return (set() if outputs[0] == outputs[1] else {"DETERM.byte_identical"}), set()


def pc_clean_regeneration(sb):
    return drift_failures(sb), set()


def pc_historical_hashes_match(sb):
    return historical_failures(sb), set()


def pc_safe_declared_output(sb):
    out = fsr.resolve_output_path(sb.path)
    expected = (sb.path / ARTIFACT_REL).resolve(strict=False)
    return (set() if out.resolve(strict=False) == expected else {"PATH.declared"}), set()


def pc_fixture_cleanup(sb):
    probe = sb.scratch / "cleanup-probe"
    probe.mkdir(parents=True, exist_ok=True)
    (probe / "x").write_text("x", encoding="utf-8")
    shutil.rmtree(probe)
    return (set() if not probe.exists() else {"ISO.cleanup"}), set()


def pc_decision_state_unchanged(sb):
    return failing(vf.check_decision_state, sb.path), set()


def pc_val_readiness_unchanged(sb):
    return failing(vf.check_state_preservation, sb.path), set()


NEGATIVE = [
    ("01_missing_schema_column", "drop the Ledger value column", fx_missing_column),
    ("02_extra_schema_column", "append an undeclared column", fx_extra_column),
    ("03_reordered_columns", "swap two declared columns", fx_reordered_columns),
    ("04_inconsistent_row_width", "truncate one row", fx_inconsistent_row_width),
    ("05_invalid_domain_value", "set an out-of-domain Ownership class", fx_invalid_domain_value),
    ("06_duplicate_row_key", "duplicate a (Requirement ID, Field name) row", fx_duplicate_row_key),
    ("07_missing_required_requirement", "delete every row of one requirement",
     fx_missing_requirement),
    ("08_missing_required_field_row", "delete one required field row", fx_missing_field_row),
    ("09_nondeterministic_row_order", "generator shuffles rows randomly",
     fx_nondeterministic_row_order),
    ("10_environment_dependent_output", "generator injects a wall-clock value",
     fx_environment_dependent_output),
    ("11_hand_edited_live_registry", "hand-edit one committed cell", fx_hand_edited_registry),
    ("12_mutated_r13_registry", "append a row to the R13 registry", fx_mutated_r13),
    ("13_mutated_r14_registry", "append a row to the R14 registry", fx_mutated_r14),
    ("14_mutated_r15_registry", "append a row to the R15 registry", fx_mutated_r15),
    ("15_mutated_r16_registry", "append a row to the R16 registry", fx_mutated_r16),
    ("16_absolute_output_path", "declare an absolute output path", fx_absolute_output_path),
    ("17_dotdot_traversal", "declare a '..' traversal output path", fx_dotdot_traversal),
    ("18_symlink_escape", "point the artifact at a symlink outside the package",
     fx_symlink_escape),
    ("19_historical_artifact_output_target", "aim output at the R16 registry",
     fx_historical_output_target),
    ("20_protected_file_output_target", "aim output at traceability-metadata.csv",
     fx_protected_output_target),
    ("21_fixture_mutation_of_real_repository", "mutate a stand-in tree and require detection",
     fx_fixture_mutating_real_repo),
    ("22_empty_generated_output", "generator produces zero rows", fx_empty_generated_output),
    ("23_generator_source_failure", "remove a required source file",
     fx_generator_subprocess_failure),
    ("24_drift_pass_without_generation", "remove the generator and re-run the drift gate",
     fx_drift_passing_without_generation),
]

POSITIVE = [
    ("P1_valid_schema", "unmutated committed registry", pc_valid_schema),
    ("P2_two_deterministic_runs", "two runs, two CWDs, two processes",
     pc_deterministic_two_runs),
    ("P3_clean_live_regeneration", "committed artifact reproduces exactly",
     pc_clean_regeneration),
    ("P4_historical_hashes_match", "all four R13-R16 digests verify",
     pc_historical_hashes_match),
    ("P5_safe_declared_output", "declared path resolves inside the package",
     pc_safe_declared_output),
    ("P6_fixture_cleanup", "temporary tree removal succeeds", pc_fixture_cleanup),
    ("P7_decision_state_unchanged", "4 recorded / 417 pending", pc_decision_state_unchanged),
    ("P8_val_readiness_unchanged", "VAL/readiness/conformance/completion unchanged",
     pc_val_readiness_unchanged),
]


def run_all(root: Path):
    results = []
    with tempfile.TemporaryDirectory(prefix="fsrg1-fixtures-") as tmp:
        tmp_path = Path(tmp)
        sb = Sandbox(root, tmp_path)
        real_before = snapshot(root)

        for name, mutation, fn in NEGATIVE:
            try:
                triggered, expected = fn(sb)
                hit = sorted(triggered & expected) if expected else sorted(triggered)
                ok = bool(hit)
                actual = "REJECTED (as expected)" if ok else \
                    "UNEXPECTEDLY ACCEPTED (validator weakness)"
            except Exception as exc:  # fail closed
                hit, ok = [], False
                actual = f"ERROR: {type(exc).__name__}: {exc}"
            finally:
                sb.restore()
            results.append({
                "fixture": name, "mode": "negative", "mutation": mutation,
                "expected_result": "rejection", "actual_result": actual,
                "triggered_checks": hit,
                "real_repository_preserved": snapshot(root) == real_before,
                "meta_ok": ok,
            })

        for name, mutation, fn in POSITIVE:
            try:
                failures, _ = fn(sb)
                ok = not failures
                actual = "PASSED (as expected)" if ok else \
                    f"UNEXPECTEDLY FAILED ({sorted(failures)})"
            except Exception as exc:
                ok = False
                actual = f"ERROR: {type(exc).__name__}: {exc}"
            finally:
                sb.restore()
            results.append({
                "fixture": name, "mode": "positive-control", "mutation": mutation,
                "expected_result": "pass", "actual_result": actual,
                "triggered_checks": [],
                "real_repository_preserved": snapshot(root) == real_before,
                "meta_ok": ok,
            })

        sandbox_path = sb.path
    cleanup_ok = not sandbox_path.exists()
    real_after = snapshot(root)
    return results, real_before, real_after, cleanup_ok


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run the FSRG1 fixture suite.")
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    args = ap.parse_args(argv)
    root = args.repo_root.resolve(strict=True)

    status_before = subprocess.run(["git", "-C", str(root), "status", "--short"],
                                   capture_output=True, text=True).stdout
    results, before, after, cleanup_ok = run_all(root)
    status_after = subprocess.run(["git", "-C", str(root), "status", "--short"],
                                  capture_output=True, text=True).stdout

    print("=" * 70)
    for r in results:
        print(json.dumps(r, indent=2, sort_keys=True))
    print("=" * 70)

    isolation_ok = before == after
    changed = sorted(set(before) ^ set(after)) + sorted(
        p for p in set(before) & set(after) if before[p] != after[p])
    negatives = [r for r in results if r["mode"] == "negative"]
    positives = [r for r in results if r["mode"] == "positive-control"]
    neg_ok = sum(1 for r in negatives if r["meta_ok"])
    pos_ok = sum(1 for r in positives if r["meta_ok"])

    print(f"negative fixtures rejected as expected: {neg_ok}/{len(negatives)}")
    print(f"positive controls passed as expected:   {pos_ok}/{len(positives)}")
    print(f"real repository files byte-unchanged:   {isolation_ok}")
    if not isolation_ok:
        print(f"  changed: {changed[:10]}")
    print(f"git status --short unchanged:           {status_before == status_after}")
    print(f"temporary fixture tree removed:         {cleanup_ok}")
    total_ok = neg_ok + pos_ok
    print(f"{total_ok}/{len(results)} fixtures produced their expected result")

    ok = (total_ok == len(results) and isolation_ok and cleanup_ok
          and status_before == status_after)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
