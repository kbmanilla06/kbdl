#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-AGC1 negative validation fixtures for the
authority-graph correction.

Proves that `authority_graph.check_authority_graph()` /
`cycle_exists()` fail closed for eight regression classes. Each fixture
mutates an in-memory copy of the real README/CSV text (or, for the
pending-count fixture, a temporary copy of issue-register.csv) -- it
never writes to the real repository files. After every fixture this
script confirms the real repository files are byte-unchanged.
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
import authority_graph as ag
import decision_state

REAL_README = f"{REPO}/docs/kbdl/motion/README.md"
REAL_CSV = f"{REPO}/docs/kbdl/traceability-metadata.csv"
REAL_ISSUE_REGISTER = f"{PKT}/issue-register.csv"


def _hash(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def _real_snapshot():
    return {p: _hash(p) for p in (REAL_README, REAL_CSV, REAL_ISSUE_REGISTER)}


def _mutated_graph_ok(readme_text, csv_rows):
    """Returns True iff, for this mutated (in-memory) state, the
    authority-graph checks all pass and no cycle is detected -- i.e.
    True means validation would (wrongly) accept this mutation."""
    rstate = ag.parse_readme_state(readme_text)
    cstate = ag.parse_traceability_csv_state(csv_rows)
    results = ag.check_authority_graph(rstate, cstate)
    all_ok = all(ok for _, ok, _ in results)
    no_cycle = not ag.cycle_exists(rstate)
    return all_ok and no_cycle


def _csv_rows_for(readme_text_unused=None):
    with open(REAL_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


BASE_README = open(REAL_README, encoding="utf-8").read()
BASE_CSV_ROWS = _csv_rows_for()


def fixture_reintroduce_007_to_008():
    mutated = BASE_README.replace(
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2). Provenance: User-provided. Validation status: Not verified.",
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2, together with `KBDL-MOT-008`, as one timing\n    system). Provenance: User-provided. Validation status: Not verified.",
        1,
    )
    assert mutated != BASE_README, "fixture did not mutate MOT-007 block"
    return mutated, BASE_CSV_ROWS, "reintroduced MOT-007 -> MOT-008 authority edge"


def fixture_reintroduce_008_to_007():
    mutated = BASE_README.replace(
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2). Provenance: User-provided. Validation\n    status: Not applicable",
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2, together with `KBDL-MOT-007`, as one timing\n    system). Provenance: User-provided. Validation\n    status: Not applicable",
        1,
    )
    assert mutated != BASE_README, "fixture did not mutate MOT-008 block"
    return mutated, BASE_CSV_ROWS, "reintroduced MOT-008 -> MOT-007 authority edge"


def fixture_reintroduce_both_edges():
    m1, _, _ = fixture_reintroduce_007_to_008()
    mutated = m1.replace(
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2). Provenance: User-provided. Validation\n    status: Not applicable",
        "Approved (per\n    [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),\n    decision packet item 2, together with `KBDL-MOT-007`, as one timing\n    system). Provenance: User-provided. Validation\n    status: Not applicable",
        1,
    )
    assert mutated != m1, "fixture did not mutate both blocks"
    return mutated, BASE_CSV_ROWS, "reintroduced both authority edges (full cycle)"


def fixture_remove_authority_mot007():
    mutated_rows = []
    for row in BASE_CSV_ROWS:
        row = dict(row)
        if row["Requirement ID"] == "KBDL-MOT-007":
            row["Authority"] = "Approved"  # KBDL-DEC-014 removed
        mutated_rows.append(row)
    return BASE_README, mutated_rows, "removed KBDL-DEC-014 item 2 from MOT-007 authority"


def fixture_remove_authority_mot008():
    mutated_rows = []
    for row in BASE_CSV_ROWS:
        row = dict(row)
        if row["Requirement ID"] == "KBDL-MOT-008":
            row["Authority"] = "Approved"
        mutated_rows.append(row)
    return BASE_README, mutated_rows, "removed KBDL-DEC-014 item 2 from MOT-008 authority"


def fixture_misclassify_supporting_authority():
    mutated = BASE_README.replace(
        "Related requirement: `KBDL-MOT-008` — related requirement only (shares\n    decision packet item 2, the same timing system); not authority for,\n    and not derived from, this requirement.",
        "Related requirement: `KBDL-MOT-008` — supporting authority for this\n    requirement.",
        1,
    )
    assert mutated != BASE_README, "fixture did not mutate related-requirement note"
    return mutated, BASE_CSV_ROWS, "misclassified MOT-007's related requirement as supporting authority"


def fixture_change_validation_status():
    mutated = BASE_README.replace(
        "decision packet item 2). Provenance: User-provided. Validation status: Not verified.",
        "decision packet item 2). Provenance: User-provided. Validation status: Verified.",
        1,
    )
    assert mutated != BASE_README, "fixture did not mutate validation status"
    return mutated, BASE_CSV_ROWS, "changed KBDL-MOT-007 validation status from Not verified to Verified"


def fixture_change_pending_state():
    """Reuses decision_state on a temporary copy of the packet dir with
    an extra issue flipped away from PENDING without a durable record --
    proves the 3-recorded/418-pending invariant still fails closed after
    the AGC1 correction. Uses a temp copy; never touches the real repo."""
    tmp = tempfile.mkdtemp(prefix="agc1_fixture_")
    try:
        shutil.copytree(PKT, os.path.join(tmp, "pkt"))
        tmp_pkt = os.path.join(tmp, "pkt")
        issue_path = os.path.join(tmp_pkt, "issue-register.csv")
        with open(issue_path, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        header = rows[0]
        idx = header.index("Owner decision")
        for row in rows[1:]:
            if row[0] == "SMR1-VC-0001":
                row[idx] = "SET TO NOT VERIFIED"
                break
        with open(issue_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(rows)
        checks, stats = decision_state.compute(tmp_pkt)
        return (checks, stats), "flipped an unrelated issue (SMR1-VC-0001) away from PENDING without a durable record"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


TEXT_CSV_FIXTURES = [
    ("reintroduce_007_to_008_edge", fixture_reintroduce_007_to_008),
    ("reintroduce_008_to_007_edge", fixture_reintroduce_008_to_007),
    ("reintroduce_both_edges", fixture_reintroduce_both_edges),
    ("remove_authority_mot007", fixture_remove_authority_mot007),
    ("remove_authority_mot008", fixture_remove_authority_mot008),
    ("misclassify_supporting_authority", fixture_misclassify_supporting_authority),
    ("change_validation_status", fixture_change_validation_status),
]


def run():
    before = _real_snapshot()
    results = []
    all_rejected = True

    for name, fn in TEXT_CSV_FIXTURES:
        readme_text, csv_rows, mutation_desc = fn()
        would_pass = _mutated_graph_ok(readme_text, csv_rows)
        rejected = not would_pass
        results.append((name, mutation_desc, rejected))
        if not rejected:
            all_rejected = False

    # 8th fixture: pending-state change (temp-copy decision_state check)
    (ds_checks, ds_stats), mutation_desc = fixture_change_pending_state()
    ds_ok = (ds_stats["pending_count"] == 418 and all(ok for _, ok, _ in ds_checks))
    rejected = not ds_ok
    results.append(("change_pending_state", mutation_desc, rejected))
    if not rejected:
        all_rejected = False

    after = _real_snapshot()
    unchanged = before == after

    print("=" * 70)
    for name, mutation_desc, rejected in results:
        status = "REJECTED (as expected)" if rejected else "UNEXPECTEDLY ACCEPTED (validator weakness)"
        print(f"[{status}] fixture={name}")
        print(f"    mutation: {mutation_desc}")
    print("=" * 70)
    print(f"Real repository files unchanged after all fixtures: {unchanged}")
    print(f"All {len(results)} AGC1 fixtures correctly rejected: {all_rejected}")
    print("=" * 70)
    return 0 if (all_rejected and unchanged) else 1


if __name__ == "__main__":
    sys.exit(run())
