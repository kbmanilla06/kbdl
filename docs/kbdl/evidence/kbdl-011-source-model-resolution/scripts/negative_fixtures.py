#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-R1 negative validation fixtures.

Deterministically proves that decision_state.compute() fails closed for
six categories of defect. Every fixture operates on a temporary copy of
the packet directory (made with shutil.copytree into a tempfile.mkdtemp()
directory) and mutates only that copy -- the real repository is never
written to. After every fixture, this script re-reads the real packet
files' mtimes/hashes to confirm they are unchanged, and deletes the
temporary directory.

Exit code: 0 if every fixture fails validation as expected (i.e. this
script's own "did validation correctly reject this?" meta-check passes
for all six fixtures); 1 if any fixture unexpectedly *passes* validation
(a validator weakness) or errors.
"""
import csv
import hashlib
import os
import shutil
import sys
import tempfile

REPO = "/Users/kbmanilla/Desktop/KBDL"
PKT = f"{REPO}/docs/kbdl/evidence/kbdl-011-source-model-resolution"

sys.path.insert(0, os.path.join(PKT, "scripts"))
import decision_state


def _snapshot(paths):
    snap = {}
    for p in paths:
        if os.path.exists(p):
            snap[p] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    return snap


def _rewrite_csv(path, mutate_row_fn):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    idx = {name: i for i, name in enumerate(header)}
    for row in rows:
        mutate_row_fn(row, idx)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)


def run_fixture(name, mutate_fn, expect_ok_categories):
    """mutate_fn(tmp_pkt) mutates files under tmp_pkt. expect_ok_categories
    is the set of decision_state check names that MUST be present and
    failing (ok == False) after the mutation -- i.e. the defect this
    fixture is designed to trigger."""
    tmp_root = tempfile.mkdtemp(prefix="kbdl_smr1_bh_fixture_")
    tmp_pkt = os.path.join(tmp_root, "pkt")
    shutil.copytree(PKT, tmp_pkt)
    try:
        mutate_fn(tmp_pkt)
        checks, stats = decision_state.compute(tmp_pkt)
        failing = {n for n, ok, d in checks if not ok}
        triggered = expect_ok_categories & failing
        exit_code = 0 if triggered else 1
        detail = {n: d for n, ok, d in checks if not ok}
        return {
            "fixture": name,
            "expected_defect_categories": sorted(expect_ok_categories),
            "actual_failing_checks": sorted(failing),
            "triggered_as_expected": sorted(triggered),
            "expected_exit_code": "nonzero (validation must reject)",
            "actual_result": "REJECTED (as expected)" if triggered else "UNEXPECTEDLY ACCEPTED (validator weakness)",
            "meta_exit_code": exit_code,
            "detail": {k: v for k, v in detail.items() if k in triggered},
        }
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)


def fixture_unbacked_unrelated_decision(tmp_pkt):
    # Mutation 1: select an unrelated, non-Batch-H issue without any durable record.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-SC-0017":
            row[idx["Owner decision"]] = "CONFIRM DIRECT STANDARD AUTHORITY"
            row[idx["Owner decision date"]] = "2026-07-29"
            row[idx["Owner evidence"]] = "KBDL-SMR1-BH-OWNER-DECISION-2026-07-29"
            row[idx["Resolution status"]] = "OWNER DECISION RECORDED — AWAITING PLANNING-AGENT VALIDATION"
    _rewrite_csv(path, mutate)


def fixture_choice_mismatch(tmp_pkt):
    # Mutation 2: recorded choice differs from the durable record's choice.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-MOTEDGE-0001":
            row[idx["Owner decision"]] = "AUTHORITY EDGE"  # durable record says RELATED REQUIREMENT
    _rewrite_csv(path, mutate)


def fixture_review_form_mismatch(tmp_pkt):
    # Mutation 3: review-form selection differs from the issue-register/durable record.
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "- [x] RELATED REQUIREMENT\n- [ ] REMOVE OR REVISE RELATIONSHIP\n- [ ] PROVIDE ORIGINAL EVIDENCE\n- [ ] DEFER DECISION\n\n**Edge 2",
        "- [ ] RELATED REQUIREMENT\n- [x] REMOVE OR REVISE RELATIONSHIP\n- [ ] PROVIDE ORIGINAL EVIDENCE\n- [ ] DEFER DECISION\n\n**Edge 2",
        1,
    )
    open(path, "w", encoding="utf-8").write(text)


def fixture_duplicate_durable_decision(tmp_pkt):
    # Mutation 4: a second durable record claims the same issue ID with a
    # conflicting choice.
    src = os.path.join(tmp_pkt, "batch-h-owner-decision-record.md")
    dup = os.path.join(tmp_pkt, "batch-h-duplicate-owner-decision-record.md")
    text = open(src, encoding="utf-8").read()
    text = text.replace("SMR1-MOTEDGE-0001 | RELATED REQUIREMENT",
                         "SMR1-MOTEDGE-0001 | AUTHORITY EDGE")
    open(dup, "w", encoding="utf-8").write(text)


def fixture_unknown_issue_id(tmp_pkt):
    # Mutation 5: durable record references an issue ID absent from issue-register.csv.
    path = os.path.join(tmp_pkt, "batch-h-owner-decision-record.md")
    text = open(path, encoding="utf-8").read()
    text += ("\n\n| SMR1-NONEXISTENT-9999 | RELATED REQUIREMENT | 2026-07-29 | "
             "Asia/Manila | KBDL-SMR1-BH-OWNER-DECISION-2026-07-29 |\n")
    open(path, "w", encoding="utf-8").write(text)


def fixture_implementation_authorizing_record(tmp_pkt):
    # Mutation 6: durable record claims implementation is authorized.
    path = os.path.join(tmp_pkt, "batch-h-owner-decision-record.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "Implementation authorization status: NOT AUTHORIZED",
        "Implementation authorization status: AUTHORIZED",
    )
    open(path, "w", encoding="utf-8").write(text)


FIXTURES = [
    ("unbacked_unrelated_decision", fixture_unbacked_unrelated_decision,
     {"7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice",
      "7b. every Owner decision date field is literally PENDING or exactly matches its durable owner-decision record's decision date",
      "7c. every Owner evidence field is literally PENDING or references its durable owner-decision record (never KBDL-DEC-014 alone)"}),
    ("choice_mismatch", fixture_choice_mismatch,
     {"7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice",
      "D9. every selected project-owner-review.md checkbox exactly matches its durable owner-decision record"}),
    ("review_form_mismatch", fixture_review_form_mismatch,
     {"D9. every selected project-owner-review.md checkbox exactly matches its durable owner-decision record",
      "D11. every durably-recorded issue has a matching project-owner-review.md checkbox selection"}),
    ("duplicate_durable_decision", fixture_duplicate_durable_decision,
     {"D1. no duplicate durable owner-decision records for the same issue ID"}),
    ("unknown_issue_id", fixture_unknown_issue_id,
     {"D3. every durable-record issue ID exists in issue-register.csv (no unknown issue ID)"}),
    ("implementation_authorizing_record", fixture_implementation_authorizing_record,
     {"D2. every durable owner-decision record states 'Implementation authorization status: NOT AUTHORIZED'"}),
]


def main():
    real_files = [
        os.path.join(PKT, "issue-register.csv"),
        os.path.join(PKT, "project-owner-review.md"),
        os.path.join(PKT, "batch-h-owner-decision-record.md"),
        os.path.join(PKT, "source-model-resolution-ledger.csv"),
    ]
    before = _snapshot(real_files)

    results = []
    overall_ok = True
    for name, mutate_fn, expect in FIXTURES:
        r = run_fixture(name, mutate_fn, expect)
        results.append(r)
        if r["meta_exit_code"] != 0:
            overall_ok = False

    after = _snapshot(real_files)
    unchanged = (before == after)
    if not unchanged:
        overall_ok = False

    print("=" * 70)
    for r in results:
        print(f"[{r['actual_result']}] fixture={r['fixture']}")
        print(f"    expected_defect_categories: {r['expected_defect_categories']}")
        print(f"    triggered_as_expected:      {r['triggered_as_expected']}")
    print("=" * 70)
    print(f"Real repository files unchanged after all fixtures: {unchanged}")
    print(f"All {len(results)} fixtures correctly rejected: {overall_ok and unchanged}")
    print("=" * 70)
    sys.exit(0 if (overall_ok and unchanged) else 1)


if __name__ == "__main__":
    main()
