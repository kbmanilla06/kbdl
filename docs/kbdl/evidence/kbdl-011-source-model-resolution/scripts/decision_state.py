#!/usr/bin/env python3
"""KBDL-011-SMR1 decision-aware packet-state module (added by
KBDL-011-SMR1-BH-R1).

Narrowly extends the SMR1 packet validator to distinguish three packet
review states:

  PREPARED — NO OWNER DECISIONS RECORDED
  OWNER REVIEW IN PROGRESS — DURABLY RECORDED DECISIONS PRESENT
  INVALID — SELECTED DECISIONS LACK DURABLE OR CONSISTENT OWNER EVIDENCE

It loads every durable `*-owner-decision-record.md` file in the packet
directory, extracts its machine-readable decision table, and cross-checks
it against `issue-register.csv` and `project-owner-review.md`. This
module is imported by `validate_packet.py` (for the real packet) and by
`negative_fixtures.py` (for temporary, deliberately-mutated copies used
only to prove validation fails correctly). Neither this module nor
`negative_fixtures.py` ever writes to the real repository.
"""
import csv
import glob
import os
import re

ISSUE_ID_RE = re.compile(r"SMR1-[A-Z0-9]+-\d+")
TABLE_ROW_RE = re.compile(r"^\|\s*(SMR1-[A-Z0-9]+-\d+)\s*\|(.*)\|\s*$")
REQUIRED_STATUS = "OWNER DECISION RECORDED — AWAITING PLANNING-AGENT VALIDATION"
REQUIRED_IMPL_STATUS = "NOT AUTHORIZED"


def parse_durable_records(pkt):
    """Return (records, files, impl_status).

    records: dict issue_id -> list of {choice, date, tz, record_id, file}
             (list length > 1 means a duplicate/conflicting record).
    files: sorted list of durable-record file paths found.
    impl_status: dict file -> "Implementation authorization status:" value
                 (or None if the field is absent).
    """
    records = {}
    impl_status = {}
    files = sorted(glob.glob(os.path.join(pkt, "*-owner-decision-record.md")))
    for fp in files:
        text = open(fp, encoding="utf-8").read()
        m = re.search(r"Implementation authorization status:\s*([^\n]+)", text)
        impl_status[fp] = m.group(1).strip() if m else None
        for line in text.splitlines():
            row = TABLE_ROW_RE.match(line.strip())
            if not row:
                continue
            issue_id = row.group(1)
            cells = [c.strip() for c in row.group(2).split("|")]
            if len(cells) < 4:
                continue
            choice, date, tz, record_id = cells[0], cells[1], cells[2], cells[3]
            records.setdefault(issue_id, []).append(
                {"choice": choice, "date": date, "tz": tz, "record_id": record_id, "file": fp}
            )
    return records, files, impl_status


def _paragraphs(text):
    return re.split(r"\n\s*\n", text)


def parse_review_form_selections(review_text):
    """Return (form_selections, orphan_selected).

    form_selections: dict issue_id -> list of selected checkbox labels
                      (uppercased), gathered from the same paragraph as
                      the issue ID's backtick mention.
    orphan_selected: list of selected checkbox labels found in a
                      paragraph with no recognizable issue ID (a stray
                      selection outside the batch-H review structure).
    """
    form_selections = {}
    orphan_selected = []
    for para in _paragraphs(review_text):
        ids_in_para = set(ISSUE_ID_RE.findall(para))
        cb_lines = re.findall(r"^- \[( |x|X)\] (.+)$", para, re.MULTILINE)
        selected_labels = [lbl.strip().upper() for mark, lbl in cb_lines if mark.lower() == "x"]
        if not ids_in_para:
            orphan_selected.extend(selected_labels)
            continue
        for iid in ids_in_para:
            form_selections.setdefault(iid, []).extend(selected_labels)
    return form_selections, orphan_selected


def compute(pkt):
    """Run every decision-state check against the packet at `pkt`.

    Returns (checks, stats) where checks is a list of (name, ok, detail)
    tuples in the same shape used by validate_packet.py's check().
    """
    checks = []
    records, files, impl_status = parse_durable_records(pkt)

    # Duplicate / conflicting durable decisions for the same issue ID,
    # whether within one file or across multiple files.
    dup_ids = [iid for iid, lst in records.items() if len(lst) > 1]
    checks.append(("D1. no duplicate durable owner-decision records for the same issue ID",
                    len(dup_ids) == 0, f"duplicates={dup_ids}"))

    # Every durable record must explicitly disclaim implementation authorization.
    bad_impl = [f for f, s in impl_status.items() if s != REQUIRED_IMPL_STATUS]
    checks.append(("D2. every durable owner-decision record states "
                    f"'Implementation authorization status: {REQUIRED_IMPL_STATUS}'",
                    len(bad_impl) == 0, f"bad={bad_impl}"))

    issue_path = os.path.join(pkt, "issue-register.csv")
    with open(issue_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ids_set = {r["Resolution issue ID"] for r in rows}

    unknown = sorted(iid for iid in records if iid not in ids_set)
    checks.append(("D3. every durable-record issue ID exists in issue-register.csv (no unknown issue ID)",
                    len(unknown) == 0, f"unknown={unknown}"))

    # Only unambiguous (non-duplicated) durable records are used for
    # exact-match checks below; duplicated ones already failed D1.
    approved = {iid: lst[0] for iid, lst in records.items() if len(lst) == 1}

    choice_mismatches, date_mismatches, evidence_mismatches, status_mismatches = [], [], [], []
    unbacked = []
    missing_recording = []
    pending_count = 0
    recorded_count = 0

    for r in rows:
        iid = r["Resolution issue ID"]
        od, odd, oe, rs = (r["Owner decision"], r["Owner decision date"],
                           r["Owner evidence"], r["Resolution status"])
        is_pending_triple = (od == "PENDING" and odd == "PENDING" and oe == "PENDING")

        if iid in approved:
            rec = approved[iid]
            recorded_count += 1
            if is_pending_triple:
                missing_recording.append(iid)
                continue
            if od.strip().upper() != rec["choice"].strip().upper():
                choice_mismatches.append(iid)
            if odd.strip() != rec["date"].strip():
                date_mismatches.append(iid)
            if rec["record_id"].strip() not in oe:
                evidence_mismatches.append(iid)
            if rs.strip() != REQUIRED_STATUS:
                status_mismatches.append(iid)
        else:
            if is_pending_triple:
                pending_count += 1
            else:
                unbacked.append(iid)

    checks.append(("7. every Owner decision field is literally PENDING or exactly matches "
                    "its durable owner-decision record's selected choice",
                    len(choice_mismatches) == 0 and len(unbacked) == 0 and len(missing_recording) == 0,
                    f"choice_mismatches={choice_mismatches} unbacked={unbacked} missing_recording={missing_recording}"))
    checks.append(("7b. every Owner decision date field is literally PENDING or exactly matches "
                    "its durable owner-decision record's decision date",
                    len(date_mismatches) == 0 and len(unbacked) == 0 and len(missing_recording) == 0,
                    f"date_mismatches={date_mismatches} unbacked={unbacked} missing_recording={missing_recording}"))
    checks.append(("7c. every Owner evidence field is literally PENDING or references its "
                    "durable owner-decision record (never KBDL-DEC-014 alone)",
                    len(evidence_mismatches) == 0 and len(unbacked) == 0 and len(missing_recording) == 0,
                    f"evidence_mismatches={evidence_mismatches} unbacked={unbacked} missing_recording={missing_recording}"))
    checks.append((f"7d. every Resolution status field is PENDING-consistent or exactly "
                    f"'{REQUIRED_STATUS}' for durably recorded rows",
                    len(status_mismatches) == 0, f"status_mismatches={status_mismatches}"))

    checks.append(("D6. no durable record exists for an issue-register row left at the PENDING triple "
                    "(recording completeness)", len(missing_recording) == 0, f"missing={missing_recording}"))
    all_others_pending = (pending_count == len(rows) - recorded_count)
    checks.append(("D7. exactly the durably-recorded issues are non-PENDING; every other issue remains PENDING",
                    all_others_pending and recorded_count == len(approved),
                    f"pending_count={pending_count} recorded_count={recorded_count} "
                    f"non_pending_rows={len(rows) - pending_count} approved={len(approved)}"))

    # Review-form cross-check.
    review_path = os.path.join(pkt, "project-owner-review.md")
    review_text = open(review_path, encoding="utf-8").read()
    form_selections, orphan_selected = parse_review_form_selections(review_text)

    checks.append(("8. no project-owner-review.md checkbox is selected outside a recognized "
                    "issue-ID review block", len(orphan_selected) == 0, f"orphan={orphan_selected}"))

    review_mismatch = []
    review_unbacked = []
    for iid, labels in form_selections.items():
        if not labels:
            continue
        if len(labels) > 1:
            review_mismatch.append((iid, "multiple-selections", labels))
            continue
        if iid not in approved:
            review_unbacked.append(iid)
            continue
        if labels[0] != approved[iid]["choice"].strip().upper():
            review_mismatch.append((iid, "choice-mismatch", labels))

    missing_form_selection = sorted(iid for iid in approved
                                     if len(form_selections.get(iid, [])) == 0)

    checks.append(("D9. every selected project-owner-review.md checkbox exactly matches its "
                    "durable owner-decision record", len(review_mismatch) == 0, f"{review_mismatch}"))
    checks.append(("D10. no project-owner-review.md checkbox selection lacks a matching durable "
                    "owner-decision record", len(review_unbacked) == 0, f"unbacked={review_unbacked}"))
    checks.append(("D11. every durably-recorded issue has a matching project-owner-review.md "
                    "checkbox selection", len(missing_form_selection) == 0,
                    f"missing={missing_form_selection}"))

    # Ledger cross-check (only if the ledger carries an owner-decision count row).
    ledger_path = os.path.join(pkt, "source-model-resolution-ledger.csv")
    ledger_ok = True
    ledger_detail = ""
    if os.path.exists(ledger_path):
        with open(ledger_path, newline="", encoding="utf-8") as f:
            lrows = list(csv.DictReader(f))
        durable_rows = [r for r in lrows
                         if r["Metric"].strip() == "Durably recorded owner decisions (Batch H / KBDL-011-SMR1-BH-R1)"]
        if durable_rows:
            if durable_rows[0]["Value"].strip() != str(len(approved)):
                ledger_ok = False
                ledger_detail = (f"ledger durable-count={durable_rows[0]['Value']} "
                                 f"expected={len(approved)}")
        # else: no such row present is only a problem once decisions exist.
        elif len(approved) > 0:
            ledger_ok = False
            ledger_detail = "no 'Durably recorded owner decisions' row present in ledger"
    checks.append(("D12. source-model-resolution-ledger.csv durable owner-decision count matches "
                    "the actual durable-record count", ledger_ok, ledger_detail))

    stats = {
        "recorded_count": recorded_count,
        "pending_count": pending_count,
        "unknown_ids": unknown,
        "duplicates": dup_ids,
        "total_rows": len(rows),
    }
    return checks, stats
