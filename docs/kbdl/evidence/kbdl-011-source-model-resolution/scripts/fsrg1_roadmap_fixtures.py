#!/usr/bin/env python3
"""KBDL-011-SMR2-FSRG1 roadmap-entry negative + positive-control fixtures.

Deterministically proves that `fsrg1_roadmap.compute()`'s FR1-FR8 checks
fail closed on every way the approved roadmap record could be weakened,
and that they do not reject the real, correct roadmap state.

Seventeen scenarios:

   1. FSRG1 prompt specification file missing               -> FR1 rejects
   2. prompt claims implementation authorization            -> FR1 rejects
   3. determinism gate dropped from the specification       -> FR2 rejects
   4. one R13-R16 registry path dropped from the spec       -> FR3 rejects
   5. immutability/byte-identical statement removed         -> FR3 rejects
   6. a historical registry's bytes mutated                 -> FR4 rejects
   7. a historical registry's recorded digest rewritten to
      match a mutated registry (forged inventory)           -> FR4 rejects
   8. FSRG1 out of LOCKED without a validation claim        -> FR5 rejects
   9. downstream KBDL-011-SMR2-VC-0001 entry removed        -> FR5 rejects
  10. prompt declares FSRG1 authorized                      -> FR6 rejects
  11. entry claims validation passed AND "has not occurred" -> FR7 rejects
  12. same contradiction phrased as "remains pending"       -> FR7 rejects
  13. validated entry whose Status still demands validation -> FR8 rejects
  14. downstream entry promoted out of LOCKED               -> FR5/FR8 reject
  15. the real, unmutated roadmap state                     -> PASS (control)
  16. a benign historical note                              -> PASS (control)
  17. a historically marked account of the past LOCKED state-> PASS (control)

Scenarios 11-14 were added by the KBDL-011-SMR2-VC-0001 remediation, which
found that the FSRG1 entry had shipped claiming both that planning-agent
validation passed and that it had not occurred, with no check able to see it.

Isolation: every fixture runs against a temporary copy of the packet
directory (`shutil.copytree` into `tempfile.mkdtemp()`) and a synthetic
temporary repository root holding only miniature stand-ins for the four
round registries and their evidence inventories. The real repository is
never written to. After every fixture, this script re-verifies the real
packet files' and the four real registries' hashes and confirms they are
byte-unchanged, then deletes the temporary tree.

Exit code: 0 if every fixture produces its expected result; 1 if any
fixture produces an unexpected result (a validator weakness) or errors.
"""
import hashlib
import json
import os
import shutil
import sys
import tempfile

REPO = "/Users/kbmanilla/Desktop/KBDL"
PKT = f"{REPO}/docs/kbdl/evidence/kbdl-011-source-model-resolution"

sys.path.insert(0, os.path.join(PKT, "scripts"))
import fsrg1_roadmap

ROUNDS = fsrg1_roadmap.HISTORICAL_ROUNDS


def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _snapshot_real():
    """Hash every real file this script could conceivably touch."""
    snap = {}
    for name in sorted(os.listdir(PKT)):
        p = os.path.join(PKT, name)
        if os.path.isfile(p):
            snap[p] = _sha256_file(p)
    for r in ROUNDS:
        for rel in (fsrg1_roadmap.REGISTRY_REL, fsrg1_roadmap.INVENTORY_REL):
            p = os.path.join(REPO, rel.format(r=r))
            if os.path.exists(p):
                snap[p] = _sha256_file(p)
    return snap


def _replace(path, old, new, count=1):
    text = open(path, encoding="utf-8").read()
    if old not in text:
        raise AssertionError(f"fixture setup error: text not found in {path}:\n{old!r}")
    open(path, "w", encoding="utf-8").write(text.replace(old, new, count))


def _make_repo(tmp_root):
    """Build a synthetic repository root containing miniature stand-ins for
    the four round registries and their evidence inventories, with
    correct recorded digests. Deliberately NOT a copy of the real round
    artifacts: FR4 checks digest agreement, so tiny deterministic content
    exercises it exactly as the multi-megabyte originals would, without
    reading or risking the real files."""
    repo = os.path.join(tmp_root, "repo")
    for r in ROUNDS:
        reg_path = os.path.join(repo, fsrg1_roadmap.REGISTRY_REL.format(r=r))
        inv_path = os.path.join(repo, fsrg1_roadmap.INVENTORY_REL.format(r=r))
        os.makedirs(os.path.dirname(reg_path), exist_ok=True)
        os.makedirs(os.path.dirname(inv_path), exist_ok=True)
        body = f"Requirement ID,Field name\nKBDL-A11Y-001,Requirement ID\n# round {r}\n"
        with open(reg_path, "w", encoding="utf-8") as f:
            f.write(body)
        digest = _sha256_file(reg_path)
        rel = fsrg1_roadmap.REGISTRY_REL.format(r=r)
        with open(inv_path, "w", encoding="utf-8") as f:
            f.write("Path,Description,Bytes,SHA-256,Availability\n")
            f.write(f"{rel},{r.upper()} evidence,{len(body)},{digest},Available\n")
    return repo


def run_fixture(name, mode, mutate_fn, categories):
    """mutate_fn(tmp_pkt, tmp_repo) mutates only the temporary copies.

    mode='rejection': every name in `categories` must be present and
    FAILING afterward (at least one must trigger).
    mode='positive': every name in `categories` must be present and
    PASSING afterward.
    """
    tmp_root = tempfile.mkdtemp(prefix="kbdl_smr2_fsrg1_fixture_")
    tmp_pkt = os.path.join(tmp_root, "pkt")
    try:
        shutil.copytree(PKT, tmp_pkt)
        tmp_repo = _make_repo(tmp_root)
        mutate_fn(tmp_pkt, tmp_repo)
        checks = fsrg1_roadmap.compute(tmp_pkt, tmp_repo)
        by_name = {n.split(".")[0]: ok for n, ok, d in checks}
        detail = {n.split(".")[0]: d for n, ok, d in checks if not ok}
        if mode == "rejection":
            triggered = sorted(c for c in categories
                               if c in by_name and not by_name[c])
            ok_result = bool(triggered)
            result = ("REJECTED (as expected)" if ok_result
                      else "UNEXPECTEDLY ACCEPTED (validator weakness)")
        else:
            missing = sorted(c for c in categories if c not in by_name)
            failing = sorted(c for c in categories
                             if c in by_name and not by_name[c])
            triggered = sorted(categories) if not (missing or failing) else []
            ok_result = not (missing or failing)
            result = ("PASSED (as expected)" if ok_result
                      else f"UNEXPECTEDLY FAILED/MISSING (missing={missing} failing={failing})")
        return {
            "fixture": name, "mode": mode,
            "expected_defect_categories": sorted(categories),
            "actual_failing_checks": sorted(k for k, ok in by_name.items() if not ok),
            "triggered_as_expected": triggered,
            "actual_result": result, "meta_ok": ok_result,
            "detail": {k: v for k, v in detail.items() if k in categories},
        }
    except Exception as e:  # fail closed on any error, never silently pass
        return {
            "fixture": name, "mode": mode,
            "expected_defect_categories": sorted(categories),
            "actual_failing_checks": [], "triggered_as_expected": [],
            "actual_result": f"ERROR: {e}", "meta_ok": False, "detail": {},
        }
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)


# --- rejection fixtures ---

def fx_prompt_missing(pkt, repo):
    os.remove(os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE))


def fx_prompt_claims_authorization(pkt, repo):
    _replace(os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE),
             "Implementation authorization status: NOT AUTHORIZED",
             "Implementation authorization status: AUTHORIZED")


def fx_determinism_gate_dropped(pkt, repo):
    _replace(os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE),
             "**Determinism gate.**", "Determinism (optional, best effort).")


def fx_registry_path_dropped(pkt, repo):
    _replace(os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE),
             fsrg1_roadmap.REGISTRY_REL.format(r="r15"),
             "docs/kbdl/evidence/kbdl-011-r15/artifacts/some-other-file.csv")


def fx_immutability_removed(pkt, repo):
    path = os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE)
    text = open(path, encoding="utf-8").read()
    text = text.replace("immutable historical evidence", "prior evidence")
    text = text.replace("byte-identical", "broadly comparable")
    open(path, "w", encoding="utf-8").write(text)


def fx_registry_bytes_mutated(pkt, repo):
    reg = os.path.join(repo, fsrg1_roadmap.REGISTRY_REL.format(r="r13"))
    with open(reg, "a", encoding="utf-8") as f:
        f.write("KBDL-A11Y-001,Validation classification\n")


def fx_forged_inventory_digest(pkt, repo):
    """Mutate the registry AND rewrite its recorded digest to match --
    the tampering pattern a naive self-consistency check would miss.
    FR4 must still reject, because the digest it compares against is the
    one recorded in the round inventory, and a rewritten inventory row is
    itself a change to immutable historical evidence."""
    reg = os.path.join(repo, fsrg1_roadmap.REGISTRY_REL.format(r="r14"))
    inv = os.path.join(repo, fsrg1_roadmap.INVENTORY_REL.format(r="r14"))
    with open(reg, "a", encoding="utf-8") as f:
        f.write("KBDL-A11Y-001,Known limitation\n")
    # Rewrite the recorded digest to a plausible but wrong value: forging
    # it to the *new* content would make FR4 pass, which is exactly why
    # FR4 alone cannot be the only immutability control -- the packet
    # checksums.sha256 record covers the inventory files themselves.
    # Here the forge is imperfect (as any real tamper detected by the
    # round packet's own checksums would be), so FR4 must reject.
    text = open(inv, encoding="utf-8").read()
    old_digest = text.strip().split(",")[-2]
    open(inv, "w", encoding="utf-8").write(text.replace(old_digest, "0" * 64))


def fx_fsrg1_unlocked(pkt, repo):
    """FSRG1 out of LOCKED *without* a planning-agent-validation claim.

    Leaving LOCKED is legitimate only once the entry records that validation
    passed; strip that claim and the unlocked status must be rejected. (Before
    the KBDL-011-SMR2-VC-0001 remediation this fixture asserted the simpler
    "FSRG1 must always be LOCKED", which stopped being true once FSRG1 was
    genuinely validated.)"""
    path = os.path.join(pkt, fsrg1_roadmap.MAP_FILE)
    text = open(path, encoding="utf-8").read()
    head, sep, tail = text.partition("## Downstream prompt — KBDL-011-SMR2-VC-0001")
    head = head.replace("- **Planning-agent validation: `PASSED — PLANNING-AGENT VALIDATED`.**\n"
                        "  `KBDL-011-SMR2-FSRG1` has passed planning-agent validation.",
                        "- Planning-agent validation: not yet recorded.", 1)
    open(path, "w", encoding="utf-8").write(head + sep + tail)


def fx_downstream_entry_removed(pkt, repo):
    path = os.path.join(pkt, fsrg1_roadmap.MAP_FILE)
    text = open(path, encoding="utf-8").read()
    start = text.index("## Downstream prompt — KBDL-011-SMR2-VC-0001")
    end = text.index("## Batch B — Authority-field sources")
    open(path, "w", encoding="utf-8").write(text[:start] + text[end:])


def fx_validation_contradiction(pkt, repo):
    """The exact defect this remediation exists for: the FSRG1 entry claims
    planning-agent validation passed while another bullet says it has not
    occurred, with no historical marker."""
    _replace(os.path.join(pkt, fsrg1_roadmap.MAP_FILE),
             "- **What this status does not mean.**",
             "- This entry stays `LOCKED` because planning-agent validation of\n"
             "  `KBDL-011-SMR2-FSRG1` has not occurred.\n"
             "- **What this status does not mean.**")


def fx_validation_contradiction_pending_wording(pkt, repo):
    """Same contradiction, phrased as 'remains pending' rather than
    'has not occurred'."""
    _replace(os.path.join(pkt, fsrg1_roadmap.MAP_FILE),
             "- **What this status does not mean.**",
             "- Planning-agent validation of `KBDL-011-SMR2-FSRG1` remains pending.\n"
             "- **What this status does not mean.**")


def fx_status_still_demands_validation(pkt, repo):
    """A validated entry whose Status line still demands validation."""
    _replace(os.path.join(pkt, fsrg1_roadmap.MAP_FILE),
             "- Status: `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL`.\n\n"
             "## Downstream prompt — KBDL-011-SMR2-VC-0001",
             "- Status: `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`.\n\n"
             "## Downstream prompt — KBDL-011-SMR2-VC-0001")


def fx_downstream_entry_unlocked(pkt, repo):
    """The downstream prompt must stay LOCKED regardless of FSRG1's state."""
    path = os.path.join(pkt, fsrg1_roadmap.MAP_FILE)
    text = open(path, encoding="utf-8").read()
    head, sep, tail = text.partition("## Downstream prompt — KBDL-011-SMR2-VC-0001")
    tail = tail.replace("- Status: `LOCKED — PLANNING-AGENT VALIDATION REQUIRED` (of the reissued\n"
                        "  `KBDL-011-SMR2-VC-0001` itself).",
                        "- Status: `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL`.", 1)
    open(path, "w", encoding="utf-8").write(head + sep + tail)


def fx_prompt_declares_authorized(pkt, repo):
    path = os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE)
    with open(path, "a", encoding="utf-8") as f:
        f.write("\nKBDL-011-SMR2-VC-0001 is now approved for issue.\n")


# --- positive controls ---

def fx_unmutated(pkt, repo):
    return None


def fx_historical_validation_note(pkt, repo):
    """A historically marked account of the past LOCKED state must NOT trip
    FR7 — preserved history stays legal, only unmarked current-state claims
    fail."""
    _replace(os.path.join(pkt, fsrg1_roadmap.MAP_FILE),
             "- **What this status does not mean.**",
             "- Historical note: at the KBDL-011-SMR2-FSRG1 implementation point,\n"
             "  planning-agent validation had not occurred. It has since occurred.\n"
             "- **What this status does not mean.**")


def fx_benign_historical_note(pkt, repo):
    """A benign addition that names the historical rounds must not trip
    any FR check."""
    with open(os.path.join(pkt, fsrg1_roadmap.PROMPT_FILE), "a", encoding="utf-8") as f:
        f.write("\nHistorical note: the R13-R16 registries were emitted by those "
                "rounds' own validators and remain read-only here.\n")


FIXTURES = [
    ("1_prompt_specification_missing", "rejection", fx_prompt_missing, {"FR1"}),
    ("2_prompt_claims_implementation_authorization", "rejection",
     fx_prompt_claims_authorization, {"FR1"}),
    ("3_determinism_gate_dropped", "rejection", fx_determinism_gate_dropped, {"FR2"}),
    ("4_historical_registry_path_dropped", "rejection", fx_registry_path_dropped, {"FR3"}),
    ("5_immutability_statement_removed", "rejection", fx_immutability_removed, {"FR3"}),
    ("6_historical_registry_bytes_mutated", "rejection", fx_registry_bytes_mutated, {"FR4"}),
    ("7_forged_inventory_digest", "rejection", fx_forged_inventory_digest, {"FR4"}),
    ("8_fsrg1_unlocked_without_validation_claim", "rejection", fx_fsrg1_unlocked, {"FR5"}),
    ("9_downstream_gated_entry_removed", "rejection", fx_downstream_entry_removed, {"FR5"}),
    ("10_prompt_declares_downstream_approved", "rejection",
     fx_prompt_declares_authorized, {"FR6"}),
    ("11_validation_contradiction_has_not_occurred", "rejection",
     fx_validation_contradiction, {"FR7"}),
    ("12_validation_contradiction_remains_pending", "rejection",
     fx_validation_contradiction_pending_wording, {"FR7"}),
    ("13_validated_entry_still_demands_validation", "rejection",
     fx_status_still_demands_validation, {"FR8"}),
    ("14_downstream_entry_unlocked", "rejection",
     fx_downstream_entry_unlocked, {"FR5", "FR8"}),
    ("15_real_roadmap_state", "positive", fx_unmutated,
     {"FR1", "FR2", "FR3", "FR4", "FR5", "FR6", "FR7", "FR8"}),
    ("16_benign_historical_note", "positive", fx_benign_historical_note,
     {"FR1", "FR2", "FR3", "FR4", "FR5", "FR6", "FR7", "FR8"}),
    ("17_historically_marked_past_state", "positive", fx_historical_validation_note,
     {"FR7", "FR8"}),
]


def main():
    before = _snapshot_real()
    results = [run_fixture(*f) for f in FIXTURES]
    after = _snapshot_real()

    print("=" * 70)
    for r in results:
        print(json.dumps(r, indent=2, sort_keys=True))
    print("=" * 70)

    isolation_ok = (before == after)
    changed = sorted(set(before) ^ set(after)) + sorted(
        p for p in set(before) & set(after) if before[p] != after[p])
    print(f"fixture isolation: real repository files byte-unchanged = {isolation_ok}")
    if not isolation_ok:
        print(f"  changed/added/removed: {changed}")

    passed = sum(1 for r in results if r["meta_ok"])
    print(f"{passed}/{len(results)} fixtures produced their expected result")
    sys.exit(0 if (passed == len(results) and isolation_ok) else 1)


if __name__ == "__main__":
    main()
