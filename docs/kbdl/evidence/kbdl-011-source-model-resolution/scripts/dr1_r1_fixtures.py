#!/usr/bin/env python3
"""KBDL-011-SMR1-BA-OD1-DR1-R1 negative + positive-control fixtures.

Deterministically proves that decision_state.compute()'s new AR1/AR2/
SP1-SP4 checks (added by KBDL-011-SMR1-BA-OD1-DR1-R1) fail closed for
the authority-contradiction, evidence-conflation, and stale
current-state-prose defects that KBDL-011-SMR1-BA-OD1-DR1's original
74/74 validator run could not detect, and that they do NOT reject the
corrected repository's genuinely historical statements or its current
four-recorded/417-pending state.

Ten scenarios, as required by the KBDL-011-SMR1-BA-OD1-DR1-R1 task
specification:

  1. durable record says "selects no new authority"            -> AR1 rejects
  2. durable record claims validation evidence exists           -> AR2 rejects
  3. packet Batch H section says 418 pending as current state   -> SP1 rejects
  4. packet VF1 section says 418 pending as current state       -> SP1 rejects
  5. project-owner-review Batch H paragraph says 418 pending
     as current state                                           -> SP1 rejects
  6. current prose says only three decisions are recorded       -> SP2 rejects
  7. current prose says AGC1 planning validation is pending     -> SP3 rejects
  8. historical 418 statement lacks a historical marker         -> SP1 rejects
  9. correct historical 418 statement is preserved and accepted -> PASS (positive control)
  10. current four-recorded/417-pending state passes            -> PASS (positive control)

Every fixture operates on a temporary copy of the packet directory
(shutil.copytree into tempfile.mkdtemp()) and mutates only that copy --
the real repository is never written to. After every fixture, this
script re-reads the real packet files' hashes to confirm they are
unchanged, and deletes the temporary directory.

Exit code: 0 if every fixture produces its expected pass/rejection
result; 1 if any fixture produces an unexpected result (a validator
weakness) or errors.
"""
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


def _replace(path, old, new, count=1):
    text = open(path, encoding="utf-8").read()
    if old not in text:
        raise AssertionError(f"fixture setup error: text not found in {path}:\n{old!r}")
    text = text.replace(old, new, count)
    open(path, "w", encoding="utf-8").write(text)


def _append(path, extra):
    with open(path, "a", encoding="utf-8") as f:
        f.write(extra)


def run_rejection_fixture(name, mutate_fn, expect_fail_categories):
    """mutate_fn(tmp_pkt) mutates files under tmp_pkt. expect_fail_categories
    is the set of decision_state check names that MUST be present and
    failing (ok == False) after the mutation."""
    tmp_root = tempfile.mkdtemp(prefix="kbdl_smr1_dr1r1_fixture_")
    tmp_pkt = os.path.join(tmp_root, "pkt")
    shutil.copytree(PKT, tmp_pkt)
    try:
        mutate_fn(tmp_pkt)
        checks, stats = decision_state.compute(tmp_pkt)
        failing = {n for n, ok, d in checks if not ok}
        triggered = expect_fail_categories & failing
        ok_result = bool(triggered)
        detail = {n: d for n, ok, d in checks if not ok}
        return {
            "fixture": name,
            "mode": "rejection",
            "expected_defect_categories": sorted(expect_fail_categories),
            "actual_failing_checks": sorted(failing),
            "triggered_as_expected": sorted(triggered),
            "actual_result": "REJECTED (as expected)" if ok_result else "UNEXPECTEDLY ACCEPTED (validator weakness)",
            "meta_ok": ok_result,
            "detail": {k: v for k, v in detail.items() if k in triggered},
        }
    except Exception as e:  # fail closed on any error, never silently pass
        return {
            "fixture": name, "mode": "rejection",
            "expected_defect_categories": sorted(expect_fail_categories),
            "actual_failing_checks": [], "triggered_as_expected": [],
            "actual_result": f"ERROR: {e}", "meta_ok": False, "detail": {},
        }
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)


def run_positive_fixture(name, mutate_fn, must_pass_categories):
    """mutate_fn(tmp_pkt) applies a benign (or no-op) change under tmp_pkt.
    must_pass_categories is the set of decision_state check names that
    MUST be present and passing (ok == True) afterward."""
    tmp_root = tempfile.mkdtemp(prefix="kbdl_smr1_dr1r1_fixture_")
    tmp_pkt = os.path.join(tmp_root, "pkt")
    shutil.copytree(PKT, tmp_pkt)
    try:
        mutate_fn(tmp_pkt)
        checks, stats = decision_state.compute(tmp_pkt)
        by_name = {n: ok for n, ok, d in checks}
        missing = sorted(c for c in must_pass_categories if c not in by_name)
        failing = sorted(c for c in must_pass_categories if c in by_name and not by_name[c])
        ok_result = (not missing) and (not failing)
        detail = {n: d for n, ok, d in checks if n in must_pass_categories}
        return {
            "fixture": name, "mode": "positive",
            "expected_defect_categories": sorted(must_pass_categories),
            "actual_failing_checks": failing,
            "triggered_as_expected": sorted(must_pass_categories) if ok_result else [],
            "actual_result": "PASSED (as expected)" if ok_result else f"UNEXPECTEDLY FAILED/MISSING (missing={missing} failing={failing})",
            "meta_ok": ok_result,
            "detail": detail,
        }
    except Exception as e:
        return {
            "fixture": name, "mode": "positive",
            "expected_defect_categories": sorted(must_pass_categories),
            "actual_failing_checks": [], "triggered_as_expected": [],
            "actual_result": f"ERROR: {e}", "meta_ok": False, "detail": {},
        }
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)


# --- (1) durable record says "selects no new authority" ---

def fixture_authority_no_new(tmp_pkt):
    path = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-owner-decision-record.md")
    _replace(
        path,
        "**This durable project-owner decision creates new current,\n"
        "  non-retroactive authority for retaining `KBDL-A11Y-001`'s validation\n"
        "  classification as `Not verified`. This authority is decision authority\n"
        "  only. It is not evidence that accessibility testing, screen-reader\n"
        "  testing, automated checking, or WCAG conformance assessment occurred.**",
        "It selects no new authority, source, or evidence for the current "
        "candidate value.",
    )


# --- (2) durable record claims validation evidence exists ---

def fixture_evidence_conflation(tmp_pkt):
    path = os.path.join(tmp_pkt, "batch-a-smr1-vc-0001-owner-decision-record.md")
    _replace(
        path,
        "This authority is decision authority\n  only. It is not evidence that "
        "accessibility testing, screen-reader\n  testing, automated checking, "
        "or WCAG conformance assessment occurred.**",
        "This authority is decision authority only, and it is evidence that "
        "accessibility testing occurred.**",
    )


# --- (3) packet Batch H section says 418 pending as current state ---

def fixture_packet_batchh_418(tmp_pkt):
    path = os.path.join(tmp_pkt, "source-model-resolution-packet.md")
    _replace(
        path,
        "4. **Remaining unresolved KBDL-011 work.** At the historical\n"
        "   KBDL-011-SMR1-BH-AGC1 point (3 durably recorded, 418 other SMR1\n"
        "   issues pending), applying this one correction did not resolve any of\n"
        "   the other pending SMR1 issues. As of the current\n"
        "   KBDL-011-SMR1-BA-OD1-DR1-R1 point, four decisions are durably\n"
        "   recorded in total (3 Batch H + 1 Batch A) and 417 issues remain\n"
        "   PENDING. This correction does not restore any `VAL-###` status, does\n"
        "   not change candidate/implementation-conformance/completion status,\n"
        "   and does not authorize source-model implementation. KBDL-011 remains\n"
        "   open.",
        "4. **Remaining unresolved KBDL-011 work.** Applying this one correction "
        "does not resolve any of the other 418 SMR1 issues, does not restore "
        "any `VAL-###` status, does not change candidate/implementation-"
        "conformance/completion status, and does not authorize source-model "
        "implementation. KBDL-011 remains open.",
    )


# --- (4) packet VF1 section says 418 pending as current state ---

def fixture_packet_vf1_418(tmp_pkt):
    path = os.path.join(tmp_pkt, "source-model-resolution-packet.md")
    _replace(
        path,
        "This is a validator-tooling-only correction. It does not change fact 2\n"
        "above (the applied Batch H correction) and does not reopen fact 1\n"
        "(historical cycle detection). At the historical KBDL-011-SMR1-BH-AGC1-VF1\n"
        "point, fact 3 (planning-agent validation) was still pending and fact 4\n"
        "(KBDL-011 remains open, the other 418 issues pending) was unchanged; as\n"
        "of the current KBDL-011-SMR1-BA-OD1-DR1-R1 point, KBDL-011-SMR1-BH-AGC1\n"
        "and KBDL-011-SMR1-BH-AGC1-VF1 have both since passed planning-agent\n"
        "validation, four decisions are durably recorded in total (3 Batch H + 1\n"
        "Batch A), 417 issues remain PENDING, and KBDL-011 remains incomplete.",
        "This is a validator-tooling-only correction. It does not change fact 2 "
        "above (the applied Batch H correction), does not reopen fact 1 "
        "(historical cycle detection), does not resolve fact 3 (planning-agent "
        "validation is still pending), and does not change fact 4 (KBDL-011 "
        "remains open, the other 418 issues remain PENDING).",
    )


# --- (5) project-owner-review Batch H paragraph says 418 pending as current state ---

def fixture_review_batchh_418(tmp_pkt):
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    _replace(
        path,
        "validation) before it takes effect. No other batch's decisions are\n"
        "affected or preselected by this entry. At the historical Batch H point\n"
        "(`KBDL-011-SMR1-BH-R1`), all other 418 canonical issues remained\n"
        "literally `PENDING`. As of the current `KBDL-011-SMR1-BA-OD1-DR1-R1`\n"
        "point (following the additional Batch A / `SMR1-VC-0001` decision), 417\n"
        "canonical issues remain literally `PENDING`.",
        "validation) before it takes effect. No other batch's decisions are "
        "affected or preselected by this entry; all other 418 canonical issues "
        "remain literally `PENDING`.",
    )


# --- (6) current prose says only three decisions are recorded ---

def fixture_three_total(tmp_pkt):
    path = os.path.join(tmp_pkt, "project-owner-review.md")
    _replace(
        path,
        "Four decisions are\nnow durably recorded in total",
        "Three decisions are\nnow durably recorded in total",
    )


# --- (7) current prose says AGC1 planning validation is pending ---

def fixture_agc1_pending(tmp_pkt):
    path = os.path.join(tmp_pkt, "source-model-resolution-packet.md")
    _append(
        path,
        "\n\nPlanning-agent validation of KBDL-011-SMR1-BH-AGC1 remains "
        "required.\n",
    )


# --- (8) historical 418 statement lacks a historical marker ---

def fixture_418_missing_marker(tmp_pkt):
    path = os.path.join(tmp_pkt, "evidence-manifest.md")
    _replace(
        path,
        "non-reproducible \"70/70\" validator claim is superseded. At the\n"
        "historical VF1 point, the three Batch H decisions and the other 418\n"
        "PENDING SMR1 issues were unchanged (superseded by the current\n"
        "4-recorded/417-pending state as of `KBDL-011-SMR1-BA-OD1-DR1-R1`, which\n"
        "also records that `KBDL-011-SMR1-BH-AGC1` and\n"
        "`KBDL-011-SMR1-BH-AGC1-VF1` have since passed planning-agent\n"
        "validation); no VAL status, lifecycle, provenance, or\n"
        "implementation-authorization status changed; no implementation action is\n"
        "authorized.",
        "non-reproducible \"70/70\" validator claim is superseded. The three "
        "Batch H decisions and the other 418 PENDING SMR1 issues are unchanged; "
        "no VAL status, lifecycle, provenance, or implementation-authorization "
        "status changed; no implementation action is authorized.",
    )


# --- (9) positive control: correct historical 418 statement preserved and accepted ---

def fixture_historical_418_preserved(tmp_pkt):
    # No mutation: proves the real, corrected repository's genuinely
    # historical 418 mentions (all carrying an explicit historical marker)
    # are accepted by SP1, not over-rejected.
    pass


# --- (10) positive control: current four-recorded/417-pending state passes ---

def fixture_current_state_passes(tmp_pkt):
    # No mutation: proves the current 4-recorded/417-pending state, the
    # corrected authority wording, and the AGC1/VF1-passed prose all pass
    # every AR/SP check simultaneously.
    pass


REJECTION_FIXTURES = [
    ("authority_no_new", fixture_authority_no_new,
     {"AR1. no durable 'SET TO NOT VERIFIED' owner-decision record states or implies it creates no current authority"}),
    ("evidence_conflation", fixture_evidence_conflation,
     {"AR2. no durable owner-decision record conflates decision authority with validation/conformance evidence"}),
    ("packet_batchh_418", fixture_packet_batchh_418,
     {"SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded"}),
    ("packet_vf1_418", fixture_packet_vf1_418,
     {"SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded"}),
    ("review_batchh_418", fixture_review_batchh_418,
     {"SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded"}),
    ("three_total", fixture_three_total,
     {"SP2. no current-state section reports a total durably-recorded-decision count other than the computed total"}),
    ("agc1_pending", fixture_agc1_pending,
     {"SP3. no current-state summary states that AGC1/VF1 planning-agent validation remains pending"}),
    ("418_missing_marker", fixture_418_missing_marker,
     {"SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded"}),
]

POSITIVE_FIXTURES = [
    ("historical_418_preserved", fixture_historical_418_preserved,
     {"SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded"}),
    ("current_state_passes", fixture_current_state_passes,
     {"AR1. no durable 'SET TO NOT VERIFIED' owner-decision record states or implies it creates no current authority",
      "AR2. no durable owner-decision record conflates decision authority with validation/conformance evidence",
      "SP1. no current-state section reports 418 pending without an explicit historical marker once four decisions are durably recorded",
      "SP2. no current-state section reports a total durably-recorded-decision count other than the computed total",
      "SP3. no current-state summary states that AGC1/VF1 planning-agent validation remains pending",
      "SP4. total recorded count, per-batch recorded counts, and pending count are mutually consistent",
      "D7. exactly the durably-recorded issues are non-PENDING; every other issue remains PENDING",
      "D14. Batch H's historically recorded owner-decision count remains exactly three"}),
]


def main():
    real_files = [
        os.path.join(PKT, "issue-register.csv"),
        os.path.join(PKT, "project-owner-review.md"),
        os.path.join(PKT, "batch-a-smr1-vc-0001-owner-decision-record.md"),
        os.path.join(PKT, "batch-h-owner-decision-record.md"),
        os.path.join(PKT, "source-model-resolution-ledger.csv"),
        os.path.join(PKT, "source-model-resolution-packet.md"),
        os.path.join(PKT, "implementation-report.md"),
        os.path.join(PKT, "evidence-manifest.md"),
        os.path.join(PKT, "scripts", "decision_state.py"),
    ]
    before = _snapshot(real_files)

    results = []
    overall_ok = True
    for name, mutate_fn, expect in REJECTION_FIXTURES:
        r = run_rejection_fixture(name, mutate_fn, expect)
        results.append(r)
        if not r["meta_ok"]:
            overall_ok = False
    for name, mutate_fn, expect in POSITIVE_FIXTURES:
        r = run_positive_fixture(name, mutate_fn, expect)
        results.append(r)
        if not r["meta_ok"]:
            overall_ok = False

    after = _snapshot(real_files)
    unchanged = (before == after)
    if not unchanged:
        overall_ok = False

    print("=" * 70)
    for r in results:
        print(f"[{r['actual_result']}] fixture={r['fixture']} ({r['mode']})")
        print(f"    expected_categories: {r['expected_defect_categories']}")
        print(f"    triggered_as_expected: {r['triggered_as_expected']}")
    print("=" * 70)
    print(f"Real repository files unchanged after all fixtures: {unchanged}")
    print(f"All {len(results)} DR1-R1 fixtures produced the expected result: {overall_ok and unchanged}")
    print("=" * 70)
    sys.exit(0 if (overall_ok and unchanged) else 1)


if __name__ == "__main__":
    main()
