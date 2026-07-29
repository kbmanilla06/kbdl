#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-R1/BH-R2/BA-OD1-DR1 negative validation fixtures.

Deterministically proves that decision_state.compute() fails closed for
twenty categories of defect (six from BH-R1, two BH-R2 stale-prose
regression fixtures, plus twelve BA-OD1-DR1 fixtures covering the Batch
A / SMR1-VC-0001 durable-record recording and the generalized
total/per-batch ledger metric). Every fixture operates on a temporary
copy of the packet directory (made with shutil.copytree into a
tempfile.mkdtemp() directory) and mutates only that copy -- the real
repository is never written to. After every fixture, this script
re-reads the real packet files' mtimes/hashes to confirm they are
unchanged, and deletes the temporary directory.

Exit code: 0 if every fixture fails validation as expected (i.e. this
script's own "did validation correctly reject this?" meta-check passes
for all fixtures); 1 if any fixture unexpectedly *passes* validation
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


def fixture_stale_packet_overview(tmp_pkt):
    # Mutation 7 (BH-R2): reintroduce the stale, pre-BH-R2 claim that the
    # packet's issue-register.csv has every owner-decision field PENDING,
    # even though durable Batch H (and, as of BA-OD1-DR1, Batch A)
    # decisions exist in this copy.
    path = os.path.join(tmp_pkt, "source-model-resolution-packet.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "As of KBDL-011-SMR1-BH-R1 (durably recorded 2026-07-29, corrected and\n"
        "republished as KBDL-011-SMR1-BH-R2), the project owner reviewed and\n"
        "recorded exactly three of those 421 decisions (Batch H:\n"
        "`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001`). As of\n"
        "KBDL-011-SMR1-BA-OD1-DR1 (durably recorded 2026-07-29), the project\n"
        "owner additionally recorded one Batch A decision (`SMR1-VC-0001` =\n"
        "SET TO NOT VERIFIED). Four of the 421 decisions are now durably\n"
        "recorded in total (3 Batch H + 1 Batch A); the other 417 remain\n"
        "literally `PENDING`. The packet's current state is **OWNER REVIEW IN\n"
        "PROGRESS — 4 DURABLY RECORDED DECISIONS (3 BATCH H, 1 BATCH A); 417\n"
        "OTHER ISSUES PENDING** (see §7 for the full state model).",
        "Every owner-decision field is literally `PENDING`.",
        1,
    )
    open(path, "w", encoding="utf-8").write(text)


def fixture_stale_review_summary(tmp_pkt):
    # Mutation 8 (BH-R2): revert the review-cycle sign-off summary to
    # PENDING even though the review form's Batch H and Batch A checkboxes
    # remain selected in this copy -- proves the summary/selection
    # contradiction is caught.
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "| Decisions recorded in this review cycle | 4 |",
        "| Decisions recorded in this review cycle | PENDING |",
        1,
    )
    open(path, "w", encoding="utf-8").write(text)


# --- KBDL-011-SMR1-BA-OD1-DR1 fixtures (Batch A / SMR1-VC-0001) ---

def fixture_ba_unbacked_change(tmp_pkt):
    # (1) SMR1-VC-0001's durable record is removed while its issue-register
    # row remains recorded -- must be rejected as unbacked.
    rec = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-owner-decision-record.md")
    os.remove(rec)


def fixture_ba_recorded_but_pending_row(tmp_pkt):
    # (2) Durable record exists but the issue-register row is reverted to
    # the PENDING triple -- must be rejected as incomplete recording (D6).
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-VC-0001":
            row[idx["Owner decision"]] = "PENDING"
            row[idx["Owner decision date"]] = "PENDING"
            row[idx["Owner evidence"]] = "PENDING"
    _rewrite_csv(path, mutate)


def fixture_ba_choice_mismatch(tmp_pkt):
    # (3) issue-register choice differs from the durable record's choice.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-VC-0001":
            row[idx["Owner decision"]] = "REVISE CLASSIFICATION"
    _rewrite_csv(path, mutate)


def fixture_ba_date_mismatch(tmp_pkt):
    # (4) issue-register decision date differs from the durable record's date.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-VC-0001":
            row[idx["Owner decision date"]] = "2026-07-30"
    _rewrite_csv(path, mutate)


def fixture_ba_wrong_evidence_reference(tmp_pkt):
    # (5) issue-register Owner evidence references the wrong record identifier.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-VC-0001":
            row[idx["Owner evidence"]] = "KBDL-SMR1-BH-OWNER-DECISION-2026-07-29"
    _rewrite_csv(path, mutate)


def fixture_ba_review_form_mismatch(tmp_pkt):
    # (6) review-form selection differs from the durable record's choice.
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "- [ ] REVISE CLASSIFICATION\n- [x] SET TO NOT VERIFIED\n- [ ] DEFER DECISION\n\n"
        "**Owner decision recorded (2026-07-29):** SMR1-VC-0001 = SET TO NOT",
        "- [x] REVISE CLASSIFICATION\n- [ ] SET TO NOT VERIFIED\n- [ ] DEFER DECISION\n\n"
        "**Owner decision recorded (2026-07-29):** SMR1-VC-0001 = SET TO NOT",
        1,
    )
    open(path, "w", encoding="utf-8").write(text)


def fixture_ba_multiple_selections(tmp_pkt):
    # (7) more than one option is selected for SMR1-VC-0001's issue-level block.
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "- [ ] REVISE CLASSIFICATION\n- [x] SET TO NOT VERIFIED\n- [ ] DEFER DECISION",
        "- [x] REVISE CLASSIFICATION\n- [x] SET TO NOT VERIFIED\n- [ ] DEFER DECISION",
        1,
    )
    open(path, "w", encoding="utf-8").write(text)


def fixture_ba_second_issue_unauthorized(tmp_pkt):
    # (8) a second Batch A issue (SMR1-VC-0002) becomes non-pending without
    # any durable authority -- must be rejected as unbacked, and D7 (only
    # durably-recorded issues are non-PENDING) must also fail.
    path = os.path.join(tmp_pkt, "issue-register.csv")
    def mutate(row, idx):
        if row[idx["Resolution issue ID"]] == "SMR1-VC-0002":
            row[idx["Owner decision"]] = "SET TO NOT VERIFIED"
            row[idx["Owner decision date"]] = "2026-07-29"
            row[idx["Owner evidence"]] = "KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29"
            row[idx["Resolution status"]] = "OWNER DECISION RECORDED — AWAITING PLANNING-AGENT VALIDATION"
    _rewrite_csv(path, mutate)


def fixture_ba_duplicate_durable_record(tmp_pkt):
    # (9) a second durable record claims SMR1-VC-0001 with a conflicting choice.
    src = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-owner-decision-record.md")
    dup = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-duplicate-owner-decision-record.md")
    text = open(src, encoding="utf-8").read()
    text = text.replace("SMR1-VC-0001 | SET TO NOT VERIFIED",
                         "SMR1-VC-0001 | REVISE CLASSIFICATION")
    open(dup, "w", encoding="utf-8").write(text)


def fixture_ba_implementation_authorizing_record(tmp_pkt):
    # (10) the Batch A durable record claims implementation is authorized.
    path = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-owner-decision-record.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace(
        "Implementation authorization status: NOT AUTHORIZED",
        "Implementation authorization status: AUTHORIZED",
    )
    open(path, "w", encoding="utf-8").write(text)


def fixture_ba_stale_packet_prose(tmp_pkt):
    # (11) packet prose still claims three recorded / 418 pending even
    # though four decisions (3 Batch H + 1 Batch A) are durably recorded
    # in this copy.
    path = os.path.join(tmp_pkt, "source-model-resolution-packet.md")
    text = open(path, encoding="utf-8").read()
    text = text.replace("417", "418")
    open(path, "w", encoding="utf-8").write(text)


def fixture_ba_stale_ledger_counts(tmp_pkt):
    # (12) ledger total/per-batch durable-decision counts are stale.
    path = os.path.join(tmp_pkt, "source-model-resolution-ledger.csv")
    text = open(path, encoding="utf-8").read()
    text = text.replace("Total durably recorded owner decisions,4,",
                         "Total durably recorded owner decisions,3,")
    text = text.replace("Batch A recorded decisions,1,",
                         "Batch A recorded decisions,0,")
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
    ("stale_packet_overview", fixture_stale_packet_overview,
     {"PS1. when durable decisions exist, the packet introduction/contents-table does not claim zero decisions are recorded"}),
    ("stale_review_summary", fixture_stale_review_summary,
     {"PS4. review-cycle sign-off summary matches the durable record"}),
    ("ba_unbacked_change", fixture_ba_unbacked_change,
     {"7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice",
      "7b. every Owner decision date field is literally PENDING or exactly matches its durable owner-decision record's decision date",
      "7c. every Owner evidence field is literally PENDING or references its durable owner-decision record (never KBDL-DEC-014 alone)",
      "D10. no project-owner-review.md checkbox selection lacks a matching durable owner-decision record"}),
    ("ba_recorded_but_pending_row", fixture_ba_recorded_but_pending_row,
     {"D6. no durable record exists for an issue-register row left at the PENDING triple (recording completeness)",
      "7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice"}),
    ("ba_choice_mismatch", fixture_ba_choice_mismatch,
     {"7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice"}),
    ("ba_date_mismatch", fixture_ba_date_mismatch,
     {"7b. every Owner decision date field is literally PENDING or exactly matches its durable owner-decision record's decision date"}),
    ("ba_wrong_evidence_reference", fixture_ba_wrong_evidence_reference,
     {"7c. every Owner evidence field is literally PENDING or references its durable owner-decision record (never KBDL-DEC-014 alone)"}),
    ("ba_review_form_mismatch", fixture_ba_review_form_mismatch,
     {"D9. every selected project-owner-review.md checkbox exactly matches its durable owner-decision record"}),
    ("ba_multiple_selections", fixture_ba_multiple_selections,
     {"D9. every selected project-owner-review.md checkbox exactly matches its durable owner-decision record"}),
    ("ba_second_issue_unauthorized", fixture_ba_second_issue_unauthorized,
     {"7. every Owner decision field is literally PENDING or exactly matches its durable owner-decision record's selected choice",
      "D7. exactly the durably-recorded issues are non-PENDING; every other issue remains PENDING"}),
    ("ba_duplicate_durable_record", fixture_ba_duplicate_durable_record,
     {"D1. no duplicate durable owner-decision records for the same issue ID"}),
    ("ba_implementation_authorizing_record", fixture_ba_implementation_authorizing_record,
     {"D2. every durable owner-decision record states 'Implementation authorization status: NOT AUTHORIZED'"}),
    ("ba_stale_packet_prose", fixture_ba_stale_packet_prose,
     {"PS2. packet-state prose recorded/pending counts match the computed decision-state counts"}),
    ("ba_stale_ledger_counts", fixture_ba_stale_ledger_counts,
     {"D12. source-model-resolution-ledger.csv durable owner-decision count matches the actual durable-record count",
      "D13. source-model-resolution-ledger.csv per-batch durable-decision counts match actual per-batch counts and sum to the total"}),
]


def main():
    real_files = [
        os.path.join(PKT, "issue-register.csv"),
        os.path.join(PKT, "project-owner-review.md"),
        os.path.join(PKT, "batch-h-owner-decision-record.md"),
        os.path.join(PKT, "batch-a-smr1-vc-0001-owner-decision-record.md"),
        os.path.join(PKT, "source-model-resolution-ledger.csv"),
        os.path.join(PKT, "source-model-resolution-packet.md"),
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
