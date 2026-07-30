#!/usr/bin/env python3
"""KBDL-011-SMR2-FSRG1 validator.

Enforces every declared FSRG1 gate fail-closed and prints one [PASS]/[FAIL]
line per check plus a final total. Exits nonzero when any check fails. No
mandatory check is ever downgraded to a warning, and no check writes to the
repository — validation is read-only, and in particular this validator never
regenerates the committed artifact in place.

Gate groups reported:

    SCHEMA      declared column contract, domains, key, coverage
    DETERM      byte-identical output across independent processes/CWDs
    DRIFT       committed artifact reproduces from current sources
    HIST        R13-R16 registries match their own recorded digests
    PATH        only the one declared output path is writable
    ISO         fixture isolation is real-repository-preserving
    COVER       every current requirement and field is represented
    LABEL       non-authoritative labelling is present and consistent
    PROT        protected/normative files unchanged vs the approved baseline
    DECISION    SMR1 decision state unchanged (4 recorded / 417 pending)
    STATE       VAL / readiness / conformance / completion unchanged
    PKG         package inventory and checksums verify
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import field_source_registry as fsr  # noqa: E402

PACKAGE_REL = fsr.PACKAGE_REL
ARTIFACT_REL = fsr.ARTIFACT_REL
GENERATOR_REL = f"{PACKAGE_REL}/scripts/field_source_registry.py"
SCHEMA_REL = f"{PACKAGE_REL}/field-source-registry-schema.md"

SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
HISTORICAL_ROUNDS = ["r13", "r14", "r15", "r16"]
REGISTRY_REL = "docs/kbdl/evidence/kbdl-011-{r}/artifacts/field-source-registry.csv"
INVENTORY_REL = "docs/kbdl/evidence/kbdl-011-{r}/evidence-inventory.csv"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

BASELINE_COMMIT = "448e39b22f4dc69210ca795c365bbdf1a3904f20"

# Paths a later, separately authorized metadata-recording prompt is permitted to
# change. Advanced by KBDL-011-SMR2-VC-0001 (reissued), which narrowly
# authorizes recording one approved owner decision into effective metadata.
#
# This does NOT weaken the PROT gate: every other protected path below is still
# compared byte-for-byte against the baseline, and each exempted path is instead
# validated field-by-field by
# `docs/kbdl/evidence/kbdl-011-smr2-vc-0001/scripts/validate_smr2_vc_0001.py`
# (checks 06-17 for the two source files, 21-22 for registry scope, 18-19 for
# sibling-issue preservation), plus `decision_state.py`'s MD1-MD8. Without this
# exemption the gate would forbid every future authorized recording, because it
# hard-codes the commit at which those files last stood unchanged.
AUTHORIZED_RECORDING_PATHS = {
    "docs/kbdl/accessibility.md",
    "docs/kbdl/traceability-metadata.csv",
    f"{SMR1_REL}/issue-register.csv",
    # KBDL-011-SMR2-VC-0001-PA1 additionally authorizes the review form, which
    # gains the unselected next-review block. Its checkbox state is asserted
    # field-by-field instead, by smr2_vc_0001_integration.py QUEUE7 and by
    # decision_state.py's D9-D11 review-form cross-checks.
    f"{SMR1_REL}/project-owner-review.md",
}

PROTECTED_RELS = [
    "docs/kbdl/traceability-metadata.csv",
    "docs/kbdl/traceability-matrix.md",
    "docs/kbdl/validation.md",
    "docs/kbdl/decision-register.md",
    "docs/kbdl/motion/timing-easing.md",
    "docs/kbdl/motion/README.md",
    "docs/kbdl/accessibility.md",
    "docs/kbdl/governance.md",
    "docs/kbdl/principles.md",
    "docs/kbdl/foundations/README.md",
    "docs/kbdl/themes/README.md",
    "docs/kbdl/responsive.md",
    "docs/kbdl/components-core.md",
    "docs/kbdl/components-system.md",
    "docs/kbdl/profiles.md",
    "docs/kbdl/customization.md",
    f"{SMR1_REL}/issue-register.csv",
    f"{SMR1_REL}/project-owner-review.md",
    f"{SMR1_REL}/batch-h-owner-decision-record.md",
    f"{SMR1_REL}/batch-a-smr1-vc-0001-owner-decision-record.md",
]

EXPECTED_RECORDED = 4
EXPECTED_PENDING = 417

NON_AUTHORITATIVE_SENTENCE = (
    "The live field-source registry is a derived, non-authoritative description "
    "of the current source model. It is not itself authority, a normative "
    "source, validation evidence, an owner-decision record, or implementation "
    "authorization."
)


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, name, ok, detail=""):
        self.rows.append((name, bool(ok), detail))
        return bool(ok)

    def report(self):
        failed = 0
        for name, ok, detail in self.rows:
            status = "PASS" if ok else "FAIL"
            if not ok:
                failed += 1
            line = f"[{status}] {name}"
            if detail and not ok:
                line += f" -- {detail}"
            print(line)
        print("=" * 70)
        print(f"{len(self.rows) - failed}/{len(self.rows)} FSRG1 checks passed")
        return failed


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(root: Path, *args, check=False):
    result = subprocess.run(["git", "-C", str(root), *args],
                            capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


# --------------------------------------------------------------------------
# SCHEMA
# --------------------------------------------------------------------------

def check_schema(c: Checks, root: Path):
    path = root / ARTIFACT_REL
    if not c.add("SCHEMA.artifact_exists", path.is_file(), f"missing {ARTIFACT_REL}"):
        return None
    raw = path.read_bytes()

    c.add("SCHEMA.encoding_utf8", _decodes_utf8(raw), "artifact is not valid UTF-8")
    c.add("SCHEMA.no_bom", not raw.startswith(b"\xef\xbb\xbf"), "byte-order mark present")
    c.add("SCHEMA.line_endings_lf", b"\r" not in raw, "CR byte present (expected LF only)")
    c.add("SCHEMA.final_newline", raw.endswith(b"\n"), "missing final newline")
    c.add("SCHEMA.nonempty", len(raw.splitlines()) > 1, "artifact has no data rows")

    try:
        text = raw.decode("utf-8")
        reader = csv.reader(io.StringIO(text))
        parsed = list(reader)
    except (UnicodeDecodeError, csv.Error) as exc:
        c.add("SCHEMA.parses", False, f"CSV parse error: {exc}")
        return None
    c.add("SCHEMA.parses", True)

    header = parsed[0] if parsed else []
    c.add("SCHEMA.header_exact", header == fsr.COLUMNS,
          f"header={header}")
    if header != fsr.COLUMNS:
        return None

    body = parsed[1:]
    widths = {len(r) for r in body}
    c.add("SCHEMA.row_widths_uniform", widths == {len(fsr.COLUMNS)},
          f"widths={sorted(widths)}")

    rows = [dict(zip(fsr.COLUMNS, r)) for r in body if len(r) == len(fsr.COLUMNS)]

    keys = [(r["Requirement ID"], r["Field name"]) for r in rows]
    dupes = sorted({k for k in keys if keys.count(k) > 1}) if len(keys) != len(set(keys)) else []
    c.add("SCHEMA.row_key_unique", not dupes, f"duplicate keys={dupes[:5]}")

    bad_field = sorted({r["Field name"] for r in rows if r["Field name"] not in fsr.FIELD_ORDER})
    c.add("SCHEMA.field_name_domain", not bad_field, f"unknown field names={bad_field}")

    bad_own = [(r["Requirement ID"], r["Field name"]) for r in rows
               if r["Field name"] in fsr.OWNERSHIP
               and r["Ownership class"] != fsr.OWNERSHIP[r["Field name"]]]
    c.add("SCHEMA.ownership_class_matches_field", not bad_own, f"mismatches={bad_own[:5]}")

    bad_rule = [(r["Requirement ID"], r["Field name"]) for r in rows
                if r["Field name"] in fsr.DERIVATION
                and r["Derivation rule"] != fsr.DERIVATION[r["Field name"]]]
    c.add("SCHEMA.derivation_rule_matches_field", not bad_rule, f"mismatches={bad_rule[:5]}")

    domains = {
        "Ownership class": set(fsr.OWNERSHIP.values()),
        "Governance resolution": {"PASS", "FAIL"},
        "Precedence result": {"PASS", "FAIL"},
        "Validation result": {"PASS", "FAIL"},
        "Readable-group classification": {
            "Exact per-ID mapping", "Uniform default", "Non-overriding summary",
            "Unresolved", "Missing"},
    }
    bad_domain = []
    for col, allowed in domains.items():
        for r in rows:
            if r[col] not in allowed:
                bad_domain.append((col, r["Requirement ID"], r[col]))
    c.add("SCHEMA.controlled_domains", not bad_domain, f"violations={bad_domain[:5]}")

    expected_order = sorted(
        rows, key=lambda r: (r["Requirement ID"], fsr.FIELD_ORDER.get(r["Field name"], 999)))
    c.add("SCHEMA.deterministic_sort_order",
          [(r["Requirement ID"], r["Field name"]) for r in rows]
          == [(r["Requirement ID"], r["Field name"]) for r in expected_order],
          "rows are not in the declared sort order")

    bad_pair = [(r["Requirement ID"], r["Field name"]) for r in rows
                if r["Effective value"] != r["Authoritative expected value"]]
    c.add("SCHEMA.effective_equals_expected", not bad_pair, f"mismatches={bad_pair[:5]}")

    bad_prec = [(r["Requirement ID"], r["Field name"]) for r in rows
                if (r["Conflict result"] == "None") != (r["Precedence result"] == "PASS")]
    c.add("SCHEMA.precedence_matches_conflict", not bad_prec, f"mismatches={bad_prec[:5]}")

    bad_val = [(r["Requirement ID"], r["Field name"]) for r in rows
               if (r["Validation result"] == "PASS")
               != (r["Authoritative expected value"] != "UNRESOLVED"
                   and r["Conflict result"] == "None")]
    c.add("SCHEMA.validation_result_policy", not bad_val, f"mismatches={bad_val[:5]}")

    no_abs = [r["Requirement ID"] for r in rows
              if any(str(root) in v for v in r.values())]
    c.add("SCHEMA.no_absolute_paths", not no_abs, f"rows leaking absolute paths={no_abs[:3]}")

    ts = re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}T\d{2}:\d{2}|\b\d{10,}\b")
    leaked = [(r["Requirement ID"], r["Field name"]) for r in rows
              if ts.search(r["Primary basis"])]
    c.add("SCHEMA.no_environment_values", not leaked, f"suspect cells={leaked[:3]}")

    return rows


def _decodes_utf8(raw: bytes) -> bool:
    try:
        raw.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


# --------------------------------------------------------------------------
# COVER
# --------------------------------------------------------------------------

def check_coverage(c: Checks, root: Path, rows):
    if rows is None:
        c.add("COVER.registry_available", False, "schema gate did not yield rows")
        return
    model_ids = set(fsr.SourceModel(root).blocks)
    registry_ids = {r["Requirement ID"] for r in rows}
    c.add("COVER.every_current_requirement_present",
          model_ids <= registry_ids, f"missing={sorted(model_ids - registry_ids)[:5]}")
    c.add("COVER.no_unknown_requirement",
          registry_ids <= model_ids, f"unknown={sorted(registry_ids - model_ids)[:5]}")
    missing_fields = []
    by_req = {}
    for r in rows:
        by_req.setdefault(r["Requirement ID"], set()).add(r["Field name"])
    for rid, fields in sorted(by_req.items()):
        if fields != set(fsr.FIELD_NAMES):
            missing_fields.append((rid, sorted(set(fsr.FIELD_NAMES) - fields)))
    c.add("COVER.every_required_field_per_requirement", not missing_fields,
          f"incomplete={missing_fields[:3]}")
    c.add("COVER.row_count_is_requirements_times_fields",
          len(rows) == len(registry_ids) * len(fsr.FIELD_NAMES),
          f"rows={len(rows)} expected={len(registry_ids) * len(fsr.FIELD_NAMES)}")


# --------------------------------------------------------------------------
# DETERM
# --------------------------------------------------------------------------

def check_determinism(c: Checks, root: Path, tmp_parent: Path):
    """Two independent generator processes, two repository copies, two CWDs."""
    outputs = []
    try:
        for i in (1, 2):
            copy_root = tmp_parent / f"determinism-{i}" / "repo"
            copy_root.parent.mkdir(parents=True, exist_ok=True)
            _copy_repo(root, copy_root)
            cwd = tmp_parent / f"determinism-{i}" / ("cwd-a" if i == 1 else "cwd-b" / Path("nested"))
            cwd = Path(str(cwd))
            cwd.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(
                [sys.executable,
                 str(copy_root / GENERATOR_REL),
                 "--repo-root", str(copy_root)],
                capture_output=True, text=True, cwd=str(cwd))
            if result.returncode != 0:
                c.add("DETERM.generator_runs", False,
                      f"run {i} rc={result.returncode} stderr={result.stderr.strip()[:200]}")
                return
            produced = copy_root / ARTIFACT_REL
            if not produced.is_file():
                c.add("DETERM.generator_runs", False, f"run {i} produced no artifact")
                return
            outputs.append(produced.read_bytes())
        c.add("DETERM.generator_runs", True)
        c.add("DETERM.byte_identical", outputs[0] == outputs[1],
              f"len0={len(outputs[0])} len1={len(outputs[1])}")
        c.add("DETERM.sha256_identical", sha256_bytes(outputs[0]) == sha256_bytes(outputs[1]),
              f"{sha256_bytes(outputs[0])[:16]} vs {sha256_bytes(outputs[1])[:16]}")
        c.add("DETERM.nonempty_output", len(outputs[0]) > 0 and outputs[0].count(b"\n") > 1,
              "generated output was empty")
        h0 = outputs[0].split(b"\n", 1)[0]
        h1 = outputs[1].split(b"\n", 1)[0]
        c.add("DETERM.header_identical", h0 == h1)
        c.add("DETERM.row_count_identical",
              outputs[0].count(b"\n") == outputs[1].count(b"\n"))
        c.add("DETERM.final_newline_identical",
              outputs[0].endswith(b"\n") and outputs[1].endswith(b"\n"))
        c.add("DETERM.line_endings_lf_only",
              b"\r" not in outputs[0] and b"\r" not in outputs[1])
    except (OSError, RuntimeError) as exc:
        c.add("DETERM.generator_runs", False, f"error: {exc}")


def _copy_repo(root: Path, dest: Path):
    """Copy the repository, including .git, excluding the FSRG1 artifact.

    .git is included because evidence values cite commit SHAs and the
    generator fails closed without an object database.
    """
    shutil.copytree(root, dest, symlinks=True,
                    ignore=shutil.ignore_patterns("__pycache__"))
    artifact = dest / ARTIFACT_REL
    if artifact.exists():
        artifact.unlink()


# --------------------------------------------------------------------------
# DRIFT + HIST
# --------------------------------------------------------------------------

def check_drift(c: Checks, root: Path):
    """The committed artifact must reproduce from current sources.

    Runs the generator's own --check mode as a separate process so a silent
    import-time failure cannot make this pass vacuously.
    """
    result = subprocess.run(
        [sys.executable, str(root / GENERATOR_REL), "--repo-root", str(root), "--check"],
        capture_output=True, text=True)
    ran = result.returncode in (0, 1)
    c.add("DRIFT.check_mode_executed", ran,
          f"rc={result.returncode} stderr={result.stderr.strip()[:200]}")
    c.add("DRIFT.committed_matches_regeneration", result.returncode == 0,
          f"rc={result.returncode} stdout={result.stdout.strip()[:200]} "
          f"stderr={result.stderr.strip()[:200]}")

    # Independent in-process regeneration, so the gate cannot pass on an
    # empty or skipped comparison.
    try:
        regenerated = fsr.generate(root)
    except fsr.GeneratorError as exc:
        c.add("DRIFT.independent_regeneration", False, f"generator error: {exc}")
        return
    committed = (root / ARTIFACT_REL).read_bytes() if (root / ARTIFACT_REL).is_file() else b""
    c.add("DRIFT.independent_regeneration", len(regenerated) > 0,
          "independent regeneration produced no bytes")
    c.add("DRIFT.independent_regeneration_matches", regenerated == committed,
          f"regenerated={sha256_bytes(regenerated)[:16]} committed={sha256_bytes(committed)[:16]}")


def recorded_registry_digest(root: Path, round_name: str):
    """Read the expected digest from that round's own committed inventory."""
    inv = root / INVENTORY_REL.format(r=round_name)
    rel = REGISTRY_REL.format(r=round_name)
    if not inv.is_file():
        return None
    with inv.open(newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or rel not in row[0]:
                continue
            digests = [x.strip() for x in row if SHA256_RE.match(x.strip())]
            return digests[0] if len(digests) == 1 else None
    return None


def check_historical(c: Checks, root: Path):
    for r in HISTORICAL_ROUNDS:
        path = root / REGISTRY_REL.format(r=r)
        recorded = recorded_registry_digest(root, r)
        if not c.add(f"HIST.{r}.recorded_digest_present", recorded is not None,
                     "no digest recorded in that round's evidence inventory"):
            continue
        if not c.add(f"HIST.{r}.registry_present", path.is_file(), f"missing {path}"):
            continue
        actual = sha256_file(path)
        c.add(f"HIST.{r}.byte_identical", actual == recorded,
              f"recorded={recorded[:16]} actual={actual[:16]}")


# --------------------------------------------------------------------------
# PATH
# --------------------------------------------------------------------------

def check_path_safety(c: Checks, root: Path, tmp_parent: Path):
    """Attempted-violation checks, not code inspection."""
    sandbox = tmp_parent / "path-safety" / "repo"
    sandbox.parent.mkdir(parents=True, exist_ok=True)
    _copy_repo(root, sandbox)

    out = fsr.resolve_output_path(sandbox)
    c.add("PATH.declared_target_resolves_inside_package",
          out.resolve(strict=False) == (sandbox / ARTIFACT_REL).resolve(strict=False),
          f"resolved={out}")

    # A symlinked artifact target must be refused outright.
    outside = tmp_parent / "path-safety" / "outside.csv"
    outside.parent.mkdir(parents=True, exist_ok=True)
    outside.write_text("x\n", encoding="utf-8")
    target = sandbox / ARTIFACT_REL
    if target.exists():
        target.unlink()
    target.symlink_to(outside)
    refused = False
    try:
        fsr.resolve_output_path(sandbox)
    except fsr.GeneratorError:
        refused = True
    c.add("PATH.symlinked_output_refused", refused,
          "a symlinked artifact path was accepted")
    target.unlink()
    c.add("PATH.symlink_escape_left_target_untouched", outside.read_text(encoding="utf-8") == "x\n",
          "the symlink target was written through")

    # Package escape: a package that is not inside the root must be refused.
    escaped = tmp_parent / "path-safety" / "not-a-repo"
    escaped.mkdir(parents=True, exist_ok=True)
    refused = False
    try:
        fsr.resolve_output_path(escaped)
    except (fsr.GeneratorError, FileNotFoundError, OSError):
        refused = True
    c.add("PATH.missing_package_refused", refused,
          "a root without the FSRG1 package was accepted")

    # The generator must write exactly one file into the repository.
    for p in (sandbox / ARTIFACT_REL, ):
        if p.exists():
            p.unlink()
    before = _tree_state(sandbox)
    result = subprocess.run(
        [sys.executable, str(sandbox / GENERATOR_REL), "--repo-root", str(sandbox)],
        capture_output=True, text=True)
    c.add("PATH.generator_succeeds_in_sandbox", result.returncode == 0,
          f"rc={result.returncode} stderr={result.stderr.strip()[:200]}")
    after = _tree_state(sandbox)
    created = sorted(set(after) - set(before))
    modified = sorted(p for p in set(after) & set(before) if after[p] != before[p])
    c.add("PATH.single_declared_write_target", created == [ARTIFACT_REL] and not modified,
          f"created={created[:5]} modified={modified[:5]}")

    # --check must never write.
    before = _tree_state(sandbox)
    subprocess.run(
        [sys.executable, str(sandbox / GENERATOR_REL), "--repo-root", str(sandbox), "--check"],
        capture_output=True, text=True)
    after = _tree_state(sandbox)
    c.add("PATH.check_mode_is_read_only", before == after,
          "--check modified the repository")

    # Historical and protected paths must be untouched by a generator run.
    hist_ok = all(
        (sandbox / REGISTRY_REL.format(r=r)).is_file()
        and sha256_file(sandbox / REGISTRY_REL.format(r=r))
        == sha256_file(root / REGISTRY_REL.format(r=r))
        for r in HISTORICAL_ROUNDS)
    c.add("PATH.historical_artifacts_never_written", hist_ok,
          "a historical registry changed during a sandbox generator run")


def _tree_state(root: Path):
    state = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/") or "__pycache__" in rel:
            continue
        state[rel] = sha256_file(path)
    return state


# --------------------------------------------------------------------------
# ISO
# --------------------------------------------------------------------------

def check_fixture_isolation(c: Checks, root: Path):
    """Run the fixture suite and confirm it preserved the real repository."""
    fixtures = root / PACKAGE_REL / "scripts" / "fsrg1_fixtures.py"
    if not c.add("ISO.fixture_suite_present", fixtures.is_file(), f"missing {fixtures}"):
        return
    before = _tracked_state(root)
    result = subprocess.run(
        [sys.executable, str(fixtures), "--repo-root", str(root)],
        capture_output=True, text=True)
    after = _tracked_state(root)
    c.add("ISO.fixture_suite_passes", result.returncode == 0,
          f"rc={result.returncode} tail={result.stdout.strip()[-300:]}")
    changed = sorted(set(before) ^ set(after)) + sorted(
        p for p in set(before) & set(after) if before[p] != after[p])
    c.add("ISO.real_repository_byte_unchanged", not changed, f"changed={changed[:5]}")
    status = git(root, "status", "--short")
    # Worktree paths a separately authorized recording prompt may touch: its own
    # evidence package plus the enumerated recording paths. Everything else must
    # still be inside the FSRG1 or SMR1 packages.
    allowed_worktree = (PACKAGE_REL, SMR1_REL,
                        "docs/kbdl/evidence/kbdl-011-smr2-vc-0001")
    unexpected = [ln for ln in status.stdout.splitlines()
                  if not any(a in ln for a in allowed_worktree)
                  and ln[3:].strip() not in AUTHORIZED_RECORDING_PATHS]
    c.add("ISO.no_unexpected_worktree_changes", not unexpected, f"{unexpected[:5]}")


def _tracked_state(root: Path):
    state = {}
    for rel in PROTECTED_RELS + [ARTIFACT_REL, GENERATOR_REL, SCHEMA_REL] + [
            REGISTRY_REL.format(r=r) for r in HISTORICAL_ROUNDS]:
        p = root / rel
        if p.is_file():
            state[rel] = sha256_file(p)
    return state


# --------------------------------------------------------------------------
# LABEL / PROT / DECISION / STATE / PKG
# --------------------------------------------------------------------------

def check_labelling(c: Checks, root: Path):
    readme = root / PACKAGE_REL / "README.md"
    if not c.add("LABEL.readme_present", readme.is_file(), f"missing {readme}"):
        return
    text = readme.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    c.add("LABEL.non_authoritative_sentence_present",
          " ".join(NON_AUTHORITATIVE_SENTENCE.split()) in normalized,
          "required non-authoritative sentence absent from README.md")
    schema = (root / SCHEMA_REL)
    schema_text = schema.read_text(encoding="utf-8") if schema.is_file() else ""
    c.add("LABEL.schema_states_non_authoritative",
          "non-authoritative" in schema_text.lower(),
          "schema does not state the non-authoritative boundary")
    claims = re.compile(
        r"(?i)\bthis registry is authoritative\b|\bis validation evidence\b"
        r"|authorizes implementation|resolves the (?:remaining )?SMR1 issues")
    hits = []
    for rel in [f"{PACKAGE_REL}/README.md", SCHEMA_REL, ARTIFACT_REL]:
        p = root / rel
        if p.is_file() and claims.search(p.read_text(encoding="utf-8", errors="ignore")):
            hits.append(rel)
    c.add("LABEL.no_authority_or_evidence_claim", not hits, f"claims found in {hits}")


def check_protected(c: Checks, root: Path):
    result = git(root, "diff", "--name-only", BASELINE_COMMIT, "--", *PROTECTED_RELS)
    if result.returncode != 0:
        c.add("PROT.baseline_diff_available", False, result.stderr.strip()[:200])
        return
    c.add("PROT.baseline_diff_available", True)
    changed = [x for x in result.stdout.splitlines() if x.strip()]
    unauthorized = [x for x in changed if x not in AUTHORIZED_RECORDING_PATHS]
    c.add("PROT.protected_files_unchanged_vs_baseline", not unauthorized,
          f"changed={unauthorized}")
    # The exempted paths are still reported, so an authorized change is visible
    # rather than silent, and is never mistaken for "nothing changed".
    c.add("PROT.authorized_recording_changes_declared",
          set(changed) <= AUTHORIZED_RECORDING_PATHS,
          f"undeclared={sorted(set(changed) - AUTHORIZED_RECORDING_PATHS)}")
    hist = git(root, "diff", "--name-only", BASELINE_COMMIT, "--",
               *[f"docs/kbdl/evidence/kbdl-011-{r}" for r in HISTORICAL_ROUNDS])
    changed_hist = [x for x in hist.stdout.splitlines() if x.strip()]
    c.add("PROT.historical_packages_unchanged_vs_baseline", not changed_hist,
          f"changed={changed_hist}")


def check_decision_state(c: Checks, root: Path):
    smr1_scripts = root / SMR1_REL / "scripts"
    sys.path.insert(0, str(smr1_scripts))
    try:
        import decision_state
    except ImportError as exc:
        c.add("DECISION.state_module_available", False, str(exc))
        return
    c.add("DECISION.state_module_available", True)
    try:
        _checks, stats = decision_state.compute(str(root / SMR1_REL))
    except Exception as exc:  # fail closed
        c.add("DECISION.state_computed", False, f"{type(exc).__name__}: {exc}")
        return
    c.add("DECISION.state_computed", True)
    c.add("DECISION.recorded_count_unchanged", stats["recorded_count"] == EXPECTED_RECORDED,
          f"recorded={stats['recorded_count']} expected={EXPECTED_RECORDED}")
    c.add("DECISION.pending_count_unchanged", stats["pending_count"] == EXPECTED_PENDING,
          f"pending={stats['pending_count']} expected={EXPECTED_PENDING}")
    c.add("DECISION.no_unknown_or_duplicate_records",
          not stats["unknown_ids"] and not stats["duplicates"],
          f"unknown={stats['unknown_ids']} duplicates={stats['duplicates']}")


def check_state_preservation(c: Checks, root: Path):
    val = root / "docs/kbdl/validation.md"
    if not c.add("STATE.validation_md_present", val.is_file(), "validation.md missing"):
        return
    text = val.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    c.add("STATE.candidate_not_ready",
          "Specification release candidate recommendation: NOT READY" in flat)
    c.add("STATE.conformance_not_verified",
          "Implementation conformance status: NOT VERIFIED" in flat)
    c.add("STATE.completion_pending",
          "Project completion status: PENDING" in flat)
    # validation.md declares VAL-003..006 collectively in one sentence; assert
    # that exact declaration rather than a per-gate line that does not exist.
    c.add("STATE.val_003_006_not_verified",
          "`KBDL-VAL-003`, `KBDL-VAL-004`, `KBDL-VAL-005`, and `KBDL-VAL-006` "
          "are `Not verified`" in flat,
          "the collective VAL-003..006 Not-verified declaration is absent or reworded")
    c.add("STATE.val_007_documentation_only",
          "`KBDL-VAL-007` remains `Verified` for its executed documentation method" in flat,
          "the VAL-007 documentation-only declaration changed")
    unlock = (root / SMR1_REL / "implementation-unlock-map.md")
    unlock_text = unlock.read_text(encoding="utf-8") if unlock.is_file() else ""
    section = ""
    for chunk in unlock_text.split("\n## "):
        if "KBDL-011-SMR2-VC-0001" in chunk.split("\n", 1)[0]:
            section = chunk
    statuses = re.findall(r"Status:\s*`([^`]+)`", section)
    # Generalized by KBDL-011-SMR2-VC-0001-PA1: the downstream entry may leave
    # LOCKED once, and only once, the map records that it passed planning-agent
    # validation. An unvalidated entry that is unlocked still fails.
    validated = bool(re.search(r"PASSED\s*[—-]\s*PLANNING-AGENT VALIDATED", section))
    c.add("STATE.smr2_vc_0001_locked_unless_validated",
          bool(statuses) and all(s.startswith("LOCKED") or validated for s in statuses),
          f"statuses={statuses} validated={validated}")
    c.add("STATE.smr2_vc_0001_reissue_required",
          bool(re.search(r"(?i)reissued", section)),
          "downstream entry no longer states the reissue requirement")


def check_package_integrity(c: Checks, root: Path):
    pkg = root / PACKAGE_REL
    required = ["README.md", "field-source-registry-schema.md",
                "artifacts/field-source-registry.csv",
                "scripts/field_source_registry.py", "scripts/validate_fsrg1.py",
                "scripts/fsrg1_fixtures.py", "implementation-report.md",
                "evidence-manifest.md", "evidence-inventory.csv", "checksums.sha256"]
    missing = [r for r in required if not (pkg / r).is_file()]
    c.add("PKG.required_files_present", not missing, f"missing={missing}")

    sums = pkg / "checksums.sha256"
    if sums.is_file():
        bad = []
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, _, rel = line.partition("  ")
            target = root / rel
            if not target.is_file():
                bad.append(f"MISSING:{rel}")
            elif sha256_file(target) != digest:
                bad.append(f"MISMATCH:{rel}")
        c.add("PKG.checksums_verify", not bad, f"{bad[:5]}")
    else:
        c.add("PKG.checksums_verify", False, "checksums.sha256 absent")

    inv = pkg / "evidence-inventory.csv"
    if inv.is_file():
        rows = list(csv.DictReader(inv.open(newline="", encoding="utf-8")))
        listed = {r["Path"] for r in rows}
        on_disk = {p.relative_to(root).as_posix() for p in pkg.rglob("*")
                   if p.is_file() and "__pycache__" not in p.as_posix()}
        self_ref = {f"{PACKAGE_REL}/evidence-inventory.csv",
                    f"{PACKAGE_REL}/checksums.sha256"}
        missing_rows = sorted(on_disk - listed - self_ref)
        stale_rows = sorted(listed - on_disk)
        c.add("PKG.inventory_complete", not missing_rows and not stale_rows,
              f"missing={missing_rows[:5]} stale={stale_rows[:5]}")
        bad_digest = [r["Path"] for r in rows
                      if (root / r["Path"]).is_file()
                      and sha256_file(root / r["Path"]) != r["SHA-256"]]
        c.add("PKG.inventory_digests_match", not bad_digest, f"{bad_digest[:5]}")
    else:
        c.add("PKG.inventory_complete", False, "evidence-inventory.csv absent")
        c.add("PKG.inventory_digests_match", False, "evidence-inventory.csv absent")


# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validate the FSRG1 package.")
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    ap.add_argument("--skip-fixtures", action="store_true",
                    help="skip the ISO gate (used only when invoked from the "
                         "fixture suite itself, to avoid unbounded recursion)")
    args = ap.parse_args(argv)
    root = args.repo_root.resolve(strict=True)

    c = Checks()
    print("=" * 70)
    rows = check_schema(c, root)
    check_coverage(c, root, rows)
    with tempfile.TemporaryDirectory(prefix="fsrg1-validate-") as tmp:
        tmp_parent = Path(tmp)
        check_determinism(c, root, tmp_parent)
        check_path_safety(c, root, tmp_parent)
    check_drift(c, root)
    check_historical(c, root)
    if not args.skip_fixtures:
        check_fixture_isolation(c, root)
    check_labelling(c, root)
    check_protected(c, root)
    check_decision_state(c, root)
    check_state_preservation(c, root)
    check_package_integrity(c, root)
    failed = c.report()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
