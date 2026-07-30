#!/usr/bin/env python3
"""KBDL-011-SMR2-VC-0001 (reissued) — deterministic fixtures.

24 negative fixtures and 6 positive controls proving that
`validate_smr2_vc_0001.py` (and, where relevant, `decision_state.py`'s MD1-MD8)
fail closed on every way the metadata recording could be wrong or over-broad.

ISOLATION
---------
One temporary copy of the repository is made (including .git, which the FSRG1
generator and the baseline-diff checks need). Every fixture mutates only that
copy and restores what it touched. The real repository is hashed before and
after the whole suite and must be byte-identical; `git status --short` is also
compared. The temporary tree is removed afterwards and a cleanup failure fails
the suite.

Exit 0 only when every fixture behaved as specified, the real repository is
unchanged, and cleanup succeeded.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import validate_smr2_vc_0001 as V  # noqa: E402

MODULE_REL = V.MODULE_REL
LEDGER_REL = V.LEDGER_REL
REGISTRY_REL = V.REGISTRY_REL
ISSUES_REL = V.ISSUES_REL
RECORD_ID = V.RECORD_ID
SMR1_REL = V.SMR1_REL
VAL_REL = "docs/kbdl/validation.md"
UNLOCK_REL = f"{SMR1_REL}/implementation-unlock-map.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> dict:
    state = {}
    for p in root.rglob("*"):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(root).as_posix()
        if rel.startswith(".git/") or "__pycache__" in rel:
            continue
        state[rel] = sha256_file(p)
    return state


class Sandbox:
    def __init__(self, root: Path, tmp: Path):
        self.origin = root
        self.path = tmp / "repo"
        shutil.copytree(root, self.path, symlinks=True,
                        ignore=shutil.ignore_patterns("__pycache__"))
        self._dirty = set()

    def mark(self, rel):
        self._dirty.add(rel)

    def restore(self):
        for rel in sorted(self._dirty):
            src, dst = self.origin / rel, self.path / rel
            if dst.exists() or dst.is_symlink():
                dst.unlink()
            if src.is_file():
                shutil.copy2(src, dst)
        self._dirty.clear()

    def read(self, rel):
        return (self.path / rel).read_text(encoding="utf-8")

    def write(self, rel, text):
        self.mark(rel)
        with (self.path / rel).open("w", encoding="utf-8", newline="") as f:
            f.write(text)

    def sub(self, rel, old, new, count=1):
        t = self.read(rel)
        if old not in t:
            raise AssertionError(f"fixture setup: {old[:60]!r} not in {rel}")
        self.write(rel, t.replace(old, new, count))

    def edit_csv_cell(self, rel, key_col, key, col, value, crlf=False):
        """Byte-surgical single-line CSV cell edit preserving line endings."""
        self.mark(rel)
        p = self.path / rel
        raw = p.read_bytes()
        sep = b"\r\n" if crlf else b"\n"
        lines = raw.split(sep)
        header = next(csv.reader(io.StringIO(lines[0].decode("utf-8"))))
        idx = None
        for i, ln in enumerate(lines[1:], 1):
            if not ln.strip():
                continue
            row = next(csv.reader(io.StringIO(ln.decode("utf-8"))))
            if len(row) == len(header) and dict(zip(header, row))[key_col] == key:
                idx = i
                d = dict(zip(header, row))
                break
        assert idx is not None, f"fixture setup: {key} not found in {rel}"
        d[col] = value
        buf = io.StringIO()
        csv.writer(buf, lineterminator="").writerow([d[h] for h in header])
        lines[idx] = buf.getvalue().encode("utf-8")
        p.write_bytes(sep.join(lines))


def failing_checks(sb: Sandbox) -> set:
    """Run the issue validator against the sandbox and return failing numbers."""
    result = subprocess.run(
        [sys.executable, str(sb.path / V.VC1_REL / "scripts" / "validate_smr2_vc_0001.py"),
         "--repo-root", str(sb.path)],
        capture_output=True, text=True)
    return {ln.split(".")[0].replace("[FAIL] ", "")
            for ln in result.stdout.splitlines() if ln.startswith("[FAIL]")}


def regenerate(sb: Sandbox):
    return subprocess.run(
        [sys.executable, str(sb.path / V.FSRG1_REL / "scripts" / "field_source_registry.py"),
         "--repo-root", str(sb.path)], capture_output=True, text=True)


# --------------------------------------------------------------------------
# Negative fixtures
# --------------------------------------------------------------------------

def fx_status_verified(sb):
    sb.sub(MODULE_REL, "- Validation status: Not verified.",
           "- Validation status: Verified.")
    regenerate(sb)
    return failing_checks(sb), {"09", "20"}


def fx_status_not_applicable(sb):
    sb.sub(MODULE_REL, "- Validation status: Not verified.",
           "- Validation status: Not applicable.")
    regenerate(sb)
    return failing_checks(sb), {"09", "20"}


def fx_status_unparsable(sb):
    sb.sub(MODULE_REL, "  - Validation status: Not verified.\n",
           "  - Validation\n    status: Not verified.\n")
    regenerate(sb)
    return failing_checks(sb), {"09", "20"}


def fx_authority_reference_omitted(sb):
    t = sb.read(MODULE_REL)
    line = [l for l in t.splitlines() if "Validation-classification authority record" in l][0]
    sb.write(MODULE_REL, t.replace(line + "\n", ""))
    return failing_checks(sb), {"10", "11", "12"}


def fx_wrong_record_id(sb):
    sb.sub(MODULE_REL, RECORD_ID, "KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2099-01-01")
    return failing_checks(sb), {"10"}


def fx_authority_as_evidence(sb):
    sb.sub(MODULE_REL,
           "decision authority only, not validation evidence",
           "and constitutes validation evidence that accessibility testing occurred")
    return failing_checks(sb), {"12"}


def fx_lifecycle_changed(sb):
    sb.sub(MODULE_REL, "- Lifecycle status: Approved (directly restates",
           "- Lifecycle status: Deferred (directly restates")
    return failing_checks(sb), {"07"}


def fx_provenance_changed(sb):
    sb.sub(MODULE_REL, "Provenance: Confirmed.", "Provenance: Assumed.")
    return failing_checks(sb), {"08"}


def fx_method_changed(sb):
    sb.sub(MODULE_REL,
           "  - Validation method: Manual + automated static accessibility check\n",
           "  - Validation method: Automated static accessibility check\n")
    return failing_checks(sb), {"13"}


def fx_evidence_claims_execution(sb):
    sb.edit_csv_cell(LEDGER_REL, "Requirement ID", V.REQUIREMENT_ID,
                     "Validation evidence",
                     "Manual and automated accessibility testing was executed; PASS.")
    return failing_checks(sb), {"16"}


def fx_limitation_changed(sb):
    sb.edit_csv_cell(LEDGER_REL, "Requirement ID", V.REQUIREMENT_ID,
                     "Known limitation", "None — full WCAG conformance is claimed.")
    return failing_checks(sb), {"17"}


def fx_kl_marked_resolved(sb):
    sb.edit_csv_cell(ISSUES_REL, "Resolution issue ID", "SMR1-KL-0001",
                     "Owner decision", "ACCEPT LIMITATION", crlf=True)
    return failing_checks(sb), {"18", "24"}


def fx_other_batch_a_changed(sb):
    sb.edit_csv_cell(ISSUES_REL, "Resolution issue ID", "SMR1-VC-0002",
                     "Owner decision", "SET TO NOT VERIFIED", crlf=True)
    return failing_checks(sb), {"19", "24"}


def fx_other_traceability_row_changed(sb):
    sb.edit_csv_cell(LEDGER_REL, "Requirement ID", "KBDL-A11Y-002",
                     "Validation classification", "Verified")
    regenerate(sb)
    return failing_checks(sb), {"21"}


def fx_registry_hand_edited(sb):
    sb.mark(REGISTRY_REL)
    p = sb.path / REGISTRY_REL
    text = p.read_text(encoding="utf-8")
    p.write_text(text.replace("KBDL-A11Y-002,Known limitation,",
                              "KBDL-A11Y-002,Known limitation ,", 1), encoding="utf-8")
    # a hand edit must be caught by the FSRG1 drift gate
    r = subprocess.run(
        [sys.executable, str(sb.path / V.FSRG1_REL / "scripts" / "field_source_registry.py"),
         "--repo-root", str(sb.path), "--check"], capture_output=True, text=True)
    return ({"DRIFT"} if r.returncode != 0 else set()), {"DRIFT"}


def fx_target_row_unresolved(sb):
    """Revert the normative field only; the registry must stop resolving."""
    sb.sub(MODULE_REL, "  - Validation status: Not verified.\n", "")
    regenerate(sb)
    return failing_checks(sb), {"09", "20"}


def fx_ledger_as_authority(sb):
    """Force the registry to claim the ledger as the field's primary basis."""
    sb.mark(REGISTRY_REL)
    p = sb.path / REGISTRY_REL
    rows = list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"))))
    for r in rows:
        if r["Requirement ID"] == V.REQUIREMENT_ID and r["Field name"] == V.FIELD:
            r["Primary basis"] = "traceability-metadata.csv (candidate only)"
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()), lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    p.write_text(buf.getvalue(), encoding="utf-8")
    return failing_checks(sb), {"20"}


def fx_other_registry_row_result_changed(sb):
    sb.mark(REGISTRY_REL)
    p = sb.path / REGISTRY_REL
    rows = list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"))))
    for r in rows:
        if r["Requirement ID"] == "KBDL-A11Y-003" and r["Field name"] == "Known limitation":
            r["Validation result"] = "PASS"
            r["Authoritative expected value"] = "forced"
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()), lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    p.write_text(buf.getvalue(), encoding="utf-8")
    return failing_checks(sb), {"21"}


def fx_registry_row_count_changed(sb):
    sb.mark(REGISTRY_REL)
    p = sb.path / REGISTRY_REL
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    p.write_text("".join(lines[:-1]), encoding="utf-8")
    return failing_checks(sb), {"22"}


def fx_issue_marked_resolved(sb):
    sb.edit_csv_cell(ISSUES_REL, "Resolution issue ID", V.ISSUE_ID,
                     "Resolution status", "RESOLVED", crlf=True)
    return failing_checks(sb), {"23", "24"}


def fx_val_003_restored(sb):
    sb.sub(VAL_REL,
           "`KBDL-VAL-003`, `KBDL-VAL-004`,\n`KBDL-VAL-005`, and `KBDL-VAL-006` are `Not verified`",
           "`KBDL-VAL-003` is `Verified`; `KBDL-VAL-004`,\n`KBDL-VAL-005`, and `KBDL-VAL-006` are `Not verified`")
    return failing_checks(sb), {"25"}


def fx_val_006_restored(sb):
    sb.sub(VAL_REL,
           "`KBDL-VAL-003`, `KBDL-VAL-004`,\n`KBDL-VAL-005`, and `KBDL-VAL-006` are `Not verified`",
           "`KBDL-VAL-003`, `KBDL-VAL-004`,\nand `KBDL-VAL-005` are `Not verified`; `KBDL-VAL-006` is `Verified`")
    return failing_checks(sb), {"25"}


def fx_batch_a_globally_unlocked(sb):
    """Batch A must never be promoted by recording one issue.

    Exercised through `smr2_vc_0001_integration.compute()`, which takes the
    repository root as an argument. `validate_packet.py` cannot be used here:
    it hard-codes the real repository path, so invoking it against a sandbox
    would silently inspect the real tree and report a pass no matter what this
    fixture mutated.
    """
    sb.sub(UNLOCK_REL,
           "- Status: `LOCKED — OWNER DECISION REQUIRED`.\n\n## Prerequisite prompt",
           "- Status: `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL`.\n\n## Prerequisite prompt")
    sys.path.insert(0, str(sb.path / SMR1_REL / "scripts"))
    import importlib
    import smr2_vc_0001_integration as integ
    importlib.reload(integ)
    failing = {n.split(".")[1].split(" ")[0]
               for n, ok, _ in integ.compute(str(sb.path)) if not ok}
    return failing, {"batch_a_still_locked"}


def fx_implementation_authorized(sb):
    sb.sub(f"{V.VC1_REL}/README.md",
           "Implementation authorization status: NOT AUTHORIZED",
           "Implementation authorization status: AUTHORIZED — implementation is now authorized")
    return failing_checks(sb), {"29"}


# --------------------------------------------------------------------------
# Positive controls
# --------------------------------------------------------------------------

def pc_valid_recording(sb):
    return failing_checks(sb), set()


def pc_deterministic_regeneration(sb):
    r = subprocess.run(
        [sys.executable, str(sb.path / V.FSRG1_REL / "scripts" / "field_source_registry.py"),
         "--repo-root", str(sb.path), "--check"], capture_output=True, text=True)
    return (set() if r.returncode == 0 else {"DRIFT"}), set()


def pc_exact_one_row_transition(sb):
    fails = failing_checks(sb)
    return (fails & {"20", "21", "22"}), set()


def pc_limitation_preserved(sb):
    return (failing_checks(sb) & {"17", "18"}), set()


def pc_decision_state_preserved(sb):
    return (failing_checks(sb) & {"24"}), set()


def pc_fixture_isolation(sb):
    probe = sb.path / ".fixture-probe"
    probe.write_text("x", encoding="utf-8")
    probe.unlink()
    return (set() if not probe.exists() else {"ISO"}), set()


NEGATIVE = [
    ("01_status_changed_to_verified", "normative status -> Verified", fx_status_verified),
    ("02_status_changed_to_not_applicable", "normative status -> Not applicable",
     fx_status_not_applicable),
    ("03_status_label_unparsable", "re-wrap the label across lines", fx_status_unparsable),
    ("04_authority_reference_omitted", "delete the authority bullet",
     fx_authority_reference_omitted),
    ("05_wrong_owner_record_id", "cite a different record ID", fx_wrong_record_id),
    ("06_authority_represented_as_evidence", "call the decision validation evidence",
     fx_authority_as_evidence),
    ("07_lifecycle_changed", "lifecycle -> Deferred", fx_lifecycle_changed),
    ("08_provenance_changed", "provenance -> Assumed", fx_provenance_changed),
    ("09_validation_method_changed", "drop 'Manual +' from the method", fx_method_changed),
    ("10_evidence_claims_execution", "ledger evidence claims a PASS",
     fx_evidence_claims_execution),
    ("11_known_limitation_changed", "limitation -> claims conformance", fx_limitation_changed),
    ("12_kl_0001_marked_resolved", "SMR1-KL-0001 given a decision", fx_kl_marked_resolved),
    ("13_other_batch_a_issue_changed", "SMR1-VC-0002 given a decision",
     fx_other_batch_a_changed),
    ("14_other_traceability_row_changed", "KBDL-A11Y-002 classification -> Verified",
     fx_other_traceability_row_changed),
    ("15_registry_hand_edited", "hand-edit the live registry", fx_registry_hand_edited),
    ("16_target_row_left_unresolved", "remove the normative status field",
     fx_target_row_unresolved),
    ("17_ledger_used_as_authority", "primary basis -> ledger candidate", fx_ledger_as_authority),
    ("18_other_registry_row_result_changed", "force another row to PASS",
     fx_other_registry_row_result_changed),
    ("19_registry_row_count_changed", "truncate one registry row",
     fx_registry_row_count_changed),
    ("20_issue_marked_finally_resolved", "issue status -> RESOLVED", fx_issue_marked_resolved),
    ("21_val_003_restored", "validation.md promotes VAL-003", fx_val_003_restored),
    ("22_val_006_restored", "validation.md promotes VAL-006", fx_val_006_restored),
    ("23_batch_a_globally_unlocked", "Batch A -> ELIGIBLE FOR FUTURE PROMPT",
     fx_batch_a_globally_unlocked),
    ("24_implementation_authorization_introduced", "README claims authorization",
     fx_implementation_authorized),
]

POSITIVE = [
    ("P1_valid_metadata_recording", "unmutated repository", pc_valid_recording),
    ("P2_deterministic_regeneration", "generator --check reproduces the artifact",
     pc_deterministic_regeneration),
    ("P3_exact_one_row_transition", "only the target row changed result",
     pc_exact_one_row_transition),
    ("P4_known_limitation_preserved", "limitation and SMR1-KL-0001 untouched",
     pc_limitation_preserved),
    ("P5_decision_state_preserved", "4 recorded / 417 pending", pc_decision_state_preserved),
    ("P6_fixture_isolation", "sandbox writes are removable", pc_fixture_isolation),
]


def run_all(root: Path):
    results = []
    with tempfile.TemporaryDirectory(prefix="smr2vc1-fixtures-") as tmp:
        sb = Sandbox(root, Path(tmp))
        real_before = snapshot(root)

        for name, mutation, fn in NEGATIVE:
            try:
                triggered, expected = fn(sb)
                hit = sorted(triggered & expected)
                ok = bool(hit)
                actual = ("REJECTED (as expected)" if ok
                          else f"UNEXPECTEDLY ACCEPTED (triggered={sorted(triggered)})")
            except Exception as exc:
                hit, ok = [], False
                actual = f"ERROR: {type(exc).__name__}: {exc}"
            finally:
                sb.restore()
                regenerate(sb)
                sb.restore()
            results.append({
                "fixture": name, "mode": "negative", "mutation": mutation,
                "expected_result": "rejection", "actual_result": actual,
                "triggered_checks": hit,
                "real_repository_preserved": snapshot(root) == real_before,
                "meta_ok": ok})

        for name, mutation, fn in POSITIVE:
            try:
                failures, _ = fn(sb)
                ok = not failures
                actual = ("PASSED (as expected)" if ok
                          else f"UNEXPECTEDLY FAILED ({sorted(failures)})")
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
                "meta_ok": ok})

        sandbox_path = sb.path
    return results, real_before, snapshot(root), not sandbox_path.exists()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run the SMR2-VC-0001 fixture suite.")
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
    neg = [r for r in results if r["mode"] == "negative"]
    pos = [r for r in results if r["mode"] == "positive-control"]
    neg_ok = sum(1 for r in neg if r["meta_ok"])
    pos_ok = sum(1 for r in pos if r["meta_ok"])

    print(f"negative fixtures rejected as expected: {neg_ok}/{len(neg)}")
    print(f"positive controls passed as expected:   {pos_ok}/{len(pos)}")
    print(f"real repository files byte-unchanged:   {isolation_ok}")
    if not isolation_ok:
        print(f"  changed: {changed[:10]}")
    print(f"git status --short unchanged:           {status_before == status_after}")
    print(f"temporary fixture tree removed:         {cleanup_ok}")
    total = neg_ok + pos_ok
    print(f"{total}/{len(results)} fixtures produced their expected result")
    ok = (total == len(results) and isolation_ok and cleanup_ok
          and status_before == status_after)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
