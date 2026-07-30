#!/usr/bin/env python3
"""KBDL-011-SMR2-VC-0001-PA1 fixtures.

25 negative fixtures and 8 positive controls proving that the planning-agent
validation checks (`decision_state.py` PA1-PA12) and the next-review queue
checks (`smr2_vc_0001_integration.py` QUEUE1-QUEUE12) fail closed on every way
the administrative transition could be wrong or over-broad.

ISOLATION
---------
One temporary copy of the repository is made; every fixture mutates only that
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
import importlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path("/Users/kbmanilla/Desktop/KBDL")
SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
VC1_REL = "docs/kbdl/evidence/kbdl-011-smr2-vc-0001"
PA_RECORD_REL = f"{VC1_REL}/smr2-vc-0001-planning-agent-validation-record.md"
ISSUES_REL = f"{SMR1_REL}/issue-register.csv"
REVIEW_REL = f"{SMR1_REL}/project-owner-review.md"
UNLOCK_REL = f"{SMR1_REL}/implementation-unlock-map.md"
BRIEF_REL = f"{SMR1_REL}/smr1-vc-0002-owner-decision-brief.md"
LEDGER_REL = "docs/kbdl/traceability-metadata.csv"
REGISTRY_REL = "docs/kbdl/evidence/kbdl-011-smr2-fsrg1/artifacts/field-source-registry.csv"

VALIDATED_STATUS = "METADATA RECORDED — PLANNING-AGENT VALIDATED"
AWAITING_STATUS = "METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION"


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
            raise AssertionError(f"fixture setup: {old[:70]!r} not in {rel}")
        self.write(rel, t.replace(old, new, count))

    def remove(self, rel):
        self.mark(rel)
        p = self.path / rel
        if p.exists():
            p.unlink()

    def edit_issue_cell(self, issue_id, col, value):
        """Byte-surgical CRLF-preserving single-cell edit of issue-register.csv."""
        self.mark(ISSUES_REL)
        p = self.path / ISSUES_REL
        raw = p.read_bytes()
        lines = raw.split(b"\r\n")
        header = next(csv.reader(io.StringIO(lines[0].decode("utf-8"))))
        idx = None
        for i, ln in enumerate(lines[1:], 1):
            if ln.startswith(issue_id.encode() + b","):
                idx = i
                d = dict(zip(header, next(csv.reader(io.StringIO(ln.decode("utf-8"))))))
                break
        assert idx is not None, f"fixture setup: {issue_id} not found"
        d[col] = value
        buf = io.StringIO()
        csv.writer(buf, lineterminator="").writerow([d[h] for h in header])
        lines[idx] = buf.getvalue().encode("utf-8")
        p.write_bytes(b"\r\n".join(lines))


def failing(sb: Sandbox) -> set:
    """Run decision_state + integration against the sandbox; return failing prefixes."""
    scripts = str(sb.path / SMR1_REL / "scripts")
    sys.path.insert(0, scripts)
    out = set()
    try:
        import decision_state
        import smr2_vc_0001_integration as integ
        importlib.reload(decision_state)
        importlib.reload(integ)
        checks, _stats = decision_state.compute(str(sb.path / SMR1_REL))
        out |= {n.split(".")[0] for n, ok, _ in checks if not ok}
        out |= {n.split(".")[1].split(" ")[0] if n.startswith("VC1.") else n.split(".")[0]
                for n, ok, _ in integ.compute(str(sb.path)) if not ok}
    except Exception as exc:  # fail closed
        out.add(f"ERROR:{type(exc).__name__}")
    finally:
        if scripts in sys.path:
            sys.path.remove(scripts)
    return out


# --- negative fixtures -----------------------------------------------------

def fx_validated_without_record(sb):
    sb.remove(PA_RECORD_REL)
    return failing(sb), {"PA1"}


def fx_verdict_not_pass(sb):
    sb.sub(PA_RECORD_REL, "| KBDL-011-SMR2-VC-0001 | PASS |",
           "| KBDL-011-SMR2-VC-0001 | FAIL |")
    return failing(sb), {"PA2"}


def fx_wrong_impl_commit(sb):
    sb.sub(PA_RECORD_REL, "af6a60a0737745ec4e2d975e58a058c619e861cb",
           "0000000000000000000000000000000000000001")
    return failing(sb), {"PA4"}


def fx_wrong_evidence_commit(sb):
    sb.sub(PA_RECORD_REL, "4aba456deeda8ea01b03eda072cfcdc82fb53ab7",
           "0000000000000000000000000000000000000002")
    return failing(sb), {"PA4"}


def fx_wrong_remediation_commit(sb):
    sb.sub(PA_RECORD_REL, "448e39b22f4dc69210ca795c365bbdf1a3904f20",
           "0000000000000000000000000000000000000003")
    return failing(sb), {"PA4"}


def fx_wrong_date(sb):
    sb.sub(PA_RECORD_REL, "| PASS | 2026-07-30 |", "| PASS | 2026-08-01 |")
    return failing(sb), {"PA5"}


def fx_wrong_timezone(sb):
    sb.sub(PA_RECORD_REL, "| 2026-07-30 | Asia/Manila |", "| 2026-07-30 | UTC |")
    return failing(sb), {"PA5"}


def fx_missing_not_authorized(sb):
    sb.sub(PA_RECORD_REL, "Implementation authorization status: NOT AUTHORIZED",
           "Implementation authorization status: AUTHORIZED")
    return failing(sb), {"PA11"}


def fx_claims_testing(sb):
    sb.sub(PA_RECORD_REL, "## Boundaries (all apply; none is waived)",
           "Accessibility testing was executed for this requirement.\n\n"
           "## Boundaries (all apply; none is waived)")
    return failing(sb), {"PA9"}


def fx_claims_val_restoration(sb):
    sb.sub(PA_RECORD_REL, "## Boundaries (all apply; none is waived)",
           "KBDL-VAL-003 is now restored.\n\n"
           "## Boundaries (all apply; none is waived)")
    return failing(sb), {"PA9"}


def fx_claims_implementation_authorized(sb):
    sb.sub(PA_RECORD_REL, "## Boundaries (all apply; none is waived)",
           "This record authorizes implementation.\n\n"
           "## Boundaries (all apply; none is waived)")
    return failing(sb), {"PA9"}


def fx_issue_still_awaiting(sb):
    """A valid record with the issue left at AWAITING is a half-applied
    transition; PA7 evaluates whenever a matching record exists."""
    sb.edit_issue_cell("SMR1-VC-0001", "Resolution status", AWAITING_STATUS)
    return failing(sb), {"PA7"}


def fx_issue_marked_resolved(sb):
    sb.edit_issue_cell("SMR1-VC-0001", "Resolution status", "RESOLVED")
    return failing(sb), {"7d", "7e"}


def fx_record_counted_as_owner_decision(sb):
    """Rename the validation record so the owner-decision parser would pick it
    up; the durable-record and count checks must reject it."""
    sb.mark(PA_RECORD_REL)
    src = sb.path / PA_RECORD_REL
    dst = sb.path / f"{SMR1_REL}/pa-owner-decision-record.md"
    text = src.read_text(encoding="utf-8")
    dst.write_text(text.replace("| KBDL-011-SMR2-VC-0001 |", "| SMR1-VC-0002 |"),
                   encoding="utf-8")
    try:
        return failing(sb), {"D3", "D2", "D7", "7", "QUEUE6"}
    finally:
        dst.unlink()


def fx_two_next_targets(sb):
    sb.sub(REVIEW_REL,
           "**The sole next owner-review target is `SMR1-VC-0002` (`KBDL-A11Y-004`). No",
           "The next owner-review target is `SMR1-VC-0007` as well.\n\n"
           "**The sole next owner-review target is `SMR1-VC-0002` (`KBDL-A11Y-004`). No")
    return failing(sb), {"QUEUE1", "QUEUE2", "QUEUE9"}


def fx_wrong_next_target(sb):
    sb.sub(REVIEW_REL, "sole next owner-review target is `SMR1-VC-0002`",
           "sole next owner-review target is `SMR1-VC-0009`")
    return failing(sb), {"QUEUE1", "QUEUE2", "QUEUE9"}


def fx_next_target_has_owner_decision(sb):
    sb.edit_issue_cell("SMR1-VC-0002", "Owner decision", "SET TO NOT VERIFIED")
    return failing(sb), {"QUEUE5"}


def fx_next_target_checkbox_selected(sb):
    block = sb.read(REVIEW_REL)
    marker = "### Next issue-level review — SMR1-VC-0002"
    head, sep, tail = block.partition(marker)
    tail = tail.replace("- [ ] SET TO NOT VERIFIED", "- [x] SET TO NOT VERIFIED", 1)
    sb.write(REVIEW_REL, head + sep + tail)
    return failing(sb), {"QUEUE7", "D10"}


def fx_another_batch_a_checkbox_selected(sb):
    block = sb.read(REVIEW_REL)
    marker = "## Batch B — Authority-field sources"
    head, sep, tail = block.partition(marker)
    head = head.replace("- [ ] DEFER DECISION", "- [x] DEFER DECISION", 1)
    sb.write(REVIEW_REL, head + sep + tail)
    return failing(sb), {"8", "D10", "QUEUE7"}


def fx_next_target_fields_changed(sb):
    sb.edit_issue_cell("SMR1-VC-0002", "Owner decision date", "2026-07-30")
    return failing(sb), {"QUEUE5", "7"}


def fx_durable_record_for_next_target(sb):
    sb.mark(f"{SMR1_REL}/batch-a-smr1-vc-0002-owner-decision-record.md")
    (sb.path / SMR1_REL / "batch-a-smr1-vc-0002-owner-decision-record.md").write_text(
        "# Durable record\n\nImplementation authorization status: NOT AUTHORIZED\n\n"
        "| Issue ID | Selected choice | Decision date | Timezone | Evidence record ID |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| SMR1-VC-0002 | SET TO NOT VERIFIED | 2026-07-30 | Asia/Manila | X |\n",
        encoding="utf-8")
    try:
        return failing(sb), {"QUEUE6", "D6", "7", "D11"}
    finally:
        (sb.path / SMR1_REL / "batch-a-smr1-vc-0002-owner-decision-record.md").unlink()


def fx_metadata_prompt_marked_eligible(sb):
    sb.sub(UNLOCK_REL, "## Batch B — Authority-field sources",
           "A metadata-recording prompt for SMR1-VC-0002 is now eligible.\n\n"
           "## Batch B — Authority-field sources")
    return failing(sb), {"QUEUE10"}


def fx_batch_a_unlocked(sb):
    sb.sub(UNLOCK_REL,
           "- Status: `LOCKED — OWNER DECISION REQUIRED`.\n\n## Prerequisite prompt",
           "- Status: `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL`.\n\n## Prerequisite prompt")
    return failing(sb), {"QUEUE11", "batch_a_still_locked"}


def fx_decision_counts_changed(sb):
    sb.edit_issue_cell("SMR1-VC-0003", "Owner decision", "SET TO NOT VERIFIED")
    return failing(sb), {"7", "D7", "decision_counts_unchanged"}


def fx_effective_metadata_changed(sb):
    sb.mark(LEDGER_REL)
    p = sb.path / LEDGER_REL
    p.write_text(p.read_text(encoding="utf-8").replace(
        "KBDL-A11Y-001,Text alternatives", "KBDL-A11Y-001X,Text alternatives", 1),
        encoding="utf-8")
    return failing(sb), {"classification_unchanged", "validator_passes", "MD6"}


# --- positive controls -----------------------------------------------------

def pc_unmutated(sb):
    return failing(sb), set()


def pc_validated_status(sb):
    rows = list(csv.DictReader(io.StringIO(sb.read(ISSUES_REL))))
    r = next(x for x in rows if x["Resolution issue ID"] == "SMR1-VC-0001")
    return (set() if r["Resolution status"].strip() == VALIDATED_STATUS
            else {"status"}), set()


def pc_one_next_target(sb):
    return (failing(sb) & {"QUEUE1", "QUEUE2", "QUEUE9"}), set()


def pc_all_choices_unselected(sb):
    return (failing(sb) & {"QUEUE7"}), set()


def pc_decision_state_preserved(sb):
    scripts = str(sb.path / SMR1_REL / "scripts")
    sys.path.insert(0, scripts)
    try:
        import decision_state
        importlib.reload(decision_state)
        _c, stats = decision_state.compute(str(sb.path / SMR1_REL))
        ok = stats["recorded_count"] == 4 and stats["pending_count"] == 417
        return (set() if ok else {"counts"}), set()
    finally:
        if scripts in sys.path:
            sys.path.remove(scripts)


def pc_batch_a_locked(sb):
    return (failing(sb) & {"QUEUE11"}), set()


def pc_effective_unchanged(sb):
    for rel in (LEDGER_REL, REGISTRY_REL, "docs/kbdl/accessibility.md"):
        if sha256_file(sb.path / rel) != sha256_file(REPO / rel):
            return {"changed:" + rel}, set()
    return set(), set()


def pc_fixture_cleanup(sb):
    probe = sb.path / ".pa1-probe"
    probe.write_text("x", encoding="utf-8")
    probe.unlink()
    return (set() if not probe.exists() else {"cleanup"}), set()


NEGATIVE = [
    ("01_validated_status_without_record", "delete the validation record",
     fx_validated_without_record),
    ("02_verdict_not_pass", "verdict -> FAIL", fx_verdict_not_pass),
    ("03_wrong_implementation_commit", "corrupt af6a60a", fx_wrong_impl_commit),
    ("04_wrong_evidence_commit", "corrupt 4aba456", fx_wrong_evidence_commit),
    ("05_wrong_remediation_commit", "corrupt 448e39b", fx_wrong_remediation_commit),
    ("06_wrong_date", "date -> 2026-08-01", fx_wrong_date),
    ("07_wrong_timezone", "timezone -> UTC", fx_wrong_timezone),
    ("08_missing_not_authorized", "authorization -> AUTHORIZED",
     fx_missing_not_authorized),
    ("09_record_claims_testing", "record claims testing was executed", fx_claims_testing),
    ("10_record_claims_val_restoration", "record claims VAL-003 restored",
     fx_claims_val_restoration),
    ("11_record_claims_implementation_authorization", "record authorizes implementation",
     fx_claims_implementation_authorized),
    ("12_issue_still_awaiting", "issue left at AWAITING despite a valid record",
     fx_issue_still_awaiting),
    ("13_issue_marked_resolved", "issue status -> RESOLVED", fx_issue_marked_resolved),
    ("14_record_counted_as_owner_decision", "validation record renamed to an "
     "owner-decision record", fx_record_counted_as_owner_decision),
    ("15_two_next_review_targets", "a second next target is named", fx_two_next_targets),
    ("16_wrong_next_review_target", "next target -> SMR1-VC-0009", fx_wrong_next_target),
    ("17_next_target_has_owner_decision", "SMR1-VC-0002 given a decision",
     fx_next_target_has_owner_decision),
    ("18_next_target_checkbox_selected", "select a SMR1-VC-0002 choice",
     fx_next_target_checkbox_selected),
    ("19_another_batch_a_checkbox_selected", "select an unrelated Batch A choice",
     fx_another_batch_a_checkbox_selected),
    ("20_next_target_owner_fields_changed", "SMR1-VC-0002 decision date set",
     fx_next_target_fields_changed),
    ("21_durable_record_for_next_target", "create a durable record for SMR1-VC-0002",
     fx_durable_record_for_next_target),
    ("22_metadata_prompt_marked_eligible", "declare its recording prompt eligible",
     fx_metadata_prompt_marked_eligible),
    ("23_batch_a_globally_unlocked", "Batch A -> ELIGIBLE", fx_batch_a_unlocked),
    ("24_decision_counts_changed", "give SMR1-VC-0003 a decision",
     fx_decision_counts_changed),
    ("25_effective_metadata_changed", "corrupt the KBDL-A11Y-001 traceability row",
     fx_effective_metadata_changed),
]

POSITIVE = [
    ("P1_valid_planning_agent_record", "unmutated repository", pc_unmutated),
    ("P2_correct_validated_issue_status", "SMR1-VC-0001 is PLANNING-AGENT VALIDATED",
     pc_validated_status),
    ("P3_exactly_one_next_target", "only SMR1-VC-0002 is named", pc_one_next_target),
    ("P4_all_next_choices_unselected", "five unselected checkboxes",
     pc_all_choices_unselected),
    ("P5_decision_state_4_417", "4 recorded / 417 pending", pc_decision_state_preserved),
    ("P6_batch_a_locked", "Batch A remains LOCKED", pc_batch_a_locked),
    ("P7_effective_state_unchanged", "ledger, registry, module byte-identical",
     pc_effective_unchanged),
    ("P8_fixture_isolation_and_cleanup", "sandbox writes are removable",
     pc_fixture_cleanup),
]


def run_all(root: Path):
    results = []
    with tempfile.TemporaryDirectory(prefix="pa1-fixtures-") as tmp:
        sb = Sandbox(root, Path(tmp))
        before = snapshot(root)
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
            results.append({"fixture": name, "mode": "negative", "mutation": mutation,
                            "expected_result": "rejection", "actual_result": actual,
                            "triggered_checks": hit,
                            "real_repository_preserved": snapshot(root) == before,
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
            results.append({"fixture": name, "mode": "positive-control",
                            "mutation": mutation, "expected_result": "pass",
                            "actual_result": actual, "triggered_checks": [],
                            "real_repository_preserved": snapshot(root) == before,
                            "meta_ok": ok})
        sandbox_path = sb.path
    return results, before, snapshot(root), not sandbox_path.exists()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run the PA1 fixture suite.")
    ap.add_argument("--repo-root", type=Path, default=REPO)
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
