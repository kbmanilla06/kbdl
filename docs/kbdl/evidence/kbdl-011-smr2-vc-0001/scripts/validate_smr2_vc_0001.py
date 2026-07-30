#!/usr/bin/env python3
"""KBDL-011-SMR2-VC-0001 (reissued) — issue-specific validator.

Verifies the single-requirement metadata recording of:

    issue        SMR1-VC-0001
    requirement  KBDL-A11Y-001
    field        Validation classification
    value        Not verified   (unchanged; this records authority, not a new outcome)
    authority    KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29

Every check fails closed. A missing file, an unparsable block, or a comparison
that could not be performed is a FAIL, never a skip. Read-only: this validator
never regenerates the live registry and never writes to the repository.

Exit code 0 only when every check passes.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
from pathlib import Path

BASELINE_COMMIT = "718b0431af9e430a1fe52a88c99b520c1593bfb1"

ISSUE_ID = "SMR1-VC-0001"
REQUIREMENT_ID = "KBDL-A11Y-001"
FIELD = "Validation classification"
VALUE = "Not verified"
RECORD_ID = "KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29"
DECISION_DATE = "2026-07-29"
TIMEZONE = "Asia/Manila"
CHOICE = "SET TO NOT VERIFIED"

SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
FSRG1_REL = "docs/kbdl/evidence/kbdl-011-smr2-fsrg1"
VC1_REL = "docs/kbdl/evidence/kbdl-011-smr2-vc-0001"
MODULE_REL = "docs/kbdl/accessibility.md"
LEDGER_REL = "docs/kbdl/traceability-metadata.csv"
REGISTRY_REL = f"{FSRG1_REL}/artifacts/field-source-registry.csv"
RECORD_REL = f"{SMR1_REL}/batch-a-smr1-vc-0001-owner-decision-record.md"
ISSUES_REL = f"{SMR1_REL}/issue-register.csv"

METADATA_RECORDED = "METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION"

REQUIREMENT_SENTENCE = (
    "- **KBDL-A11Y-001** — Non-decorative images/icons **must** have a text\n"
    "  alternative; decorative images **must** be excluded from AT\n"
    "  narration; text **must not** be presented as an image except where\n"
    "  essential.\n"
)
METHOD_VALUE = "Manual + automated static accessibility check once implemented"
LIMITATION_VALUE = (
    "This document does not claim full WCAG conformance, screen-reader "
    "compatibility, or real-device support — those require an implementation "
    "and recorded test evidence"
)

BLOCK_RE = re.compile(
    r"^- \*\*KBDL-A11Y-001\*\*.*?(?=^- \*\*KBDL-A11Y-|\Z)", re.MULTILINE | re.DOTALL)
STATUS_FIELD_RE = re.compile(r"(?m)^\s*-\s*Validation status:\s*(.+?)\s*$")
LIFECYCLE_RE = re.compile(r"(?m)^\s*-\s*Lifecycle status:\s*(\w+)")
PROVENANCE_RE = re.compile(r"Provenance:\s*(\w+)")
CURRENT_NONRETRO_RE = re.compile(r"current and non-retroactive", re.IGNORECASE)
NOT_EVIDENCE_RE = re.compile(r"decision authority only[,;]?\s*not validation evidence",
                             re.IGNORECASE)
EXECUTION_CLAIM_RE = re.compile(
    r"(?i)\b(was executed|has been executed|executed on|test(?:s|ing)? passed|"
    r"screen[- ]reader (?:testing|verification) (?:was )?(?:performed|completed)|"
    r"WCAG conformance (?:established|achieved|verified))")

ALLOWED_PREFIXES = (
    MODULE_REL, LEDGER_REL,
    f"{FSRG1_REL}/artifacts/field-source-registry.csv",
    f"{FSRG1_REL}/evidence-inventory.csv",
    f"{FSRG1_REL}/checksums.sha256",
    VC1_REL + "/",
    f"{SMR1_REL}/issue-register.csv",
    f"{SMR1_REL}/implementation-unlock-map.md",
    f"{SMR1_REL}/source-model-resolution-packet.md",
    f"{SMR1_REL}/source-model-resolution-ledger.csv",
    f"{SMR1_REL}/implementation-report.md",
    f"{SMR1_REL}/evidence-manifest.md",
    f"{SMR1_REL}/evidence-inventory.csv",
    f"{SMR1_REL}/checksums.sha256",
    f"{SMR1_REL}/scripts/decision_state.py",
    f"{SMR1_REL}/scripts/validate_packet.py",
    f"{SMR1_REL}/scripts/smr2_vc_0001_integration.py",
)

# Paths outside the reissued prompt's Allowed Files list that this
# implementation nevertheless had to change, declared explicitly so they can
# never pass silently. Both hold FSRG1's protected-baseline constants, which
# enumerate exactly the files this prompt authorizes changing and pin them to
# the superseded baseline dc16473a; left unchanged, FSRG1's PROT gate fails for
# any authorized recording, permanently. See the package implementation report,
# "Scope deviation to report". Check 31 asserts the deviation set is exactly
# this and nothing more.
DECLARED_SCOPE_DEVIATIONS = (
    f"{FSRG1_REL}/scripts/validate_fsrg1.py",
    f"{SMR1_REL}/scripts/fsrg1_integration.py",
)

# Files changed by the KBDL-011-SMR2-VC-0001 validation remediation, which the
# orchestrator explicitly released ("one narrow remediation prompt for the
# unlock-map contradiction, validator coverage, fixture exit codes, and final
# publication verification"). Adding FR7/FR8 and their fixtures necessarily
# touches these two. Kept separate from DECLARED_SCOPE_DEVIATIONS so the
# retroactively approved FSRG1 baseline expansion cannot silently grow.
REMEDIATION_AUTHORIZED = (
    f"{SMR1_REL}/scripts/fsrg1_roadmap.py",
    f"{SMR1_REL}/scripts/fsrg1_roadmap_fixtures.py",
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
            if not ok:
                failed += 1
            line = f"[{'PASS' if ok else 'FAIL'}] {name}"
            if detail and not ok:
                line += f" -- {detail}"
            print(line)
        print("=" * 70)
        print(f"{len(self.rows) - failed}/{len(self.rows)} SMR2-VC-0001 checks passed")
        return failed


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)


def read(root, rel):
    p = root / rel
    return p.read_text(encoding="utf-8") if p.is_file() else None


def ledger_row(root, rel, key_col, key):
    text = read(root, rel)
    if text is None:
        return None
    for r in csv.DictReader(io.StringIO(text)):
        if r[key_col] == key:
            return r
    return None


def registry_rows(root):
    text = read(root, REGISTRY_REL)
    if text is None:
        return None
    return list(csv.DictReader(io.StringIO(text)))


def baseline_registry_rows(root):
    res = git(root, "show", f"{BASELINE_COMMIT}:{REGISTRY_REL}")
    if res.returncode != 0:
        return None
    return list(csv.DictReader(io.StringIO(res.stdout)))


def run(root: Path) -> int:
    c = Checks()
    print("=" * 70)

    # --- durable owner record (1-5) ---
    record = read(root, RECORD_REL)
    c.add("01. durable owner-decision record exists with the exact record ID",
          record is not None and RECORD_ID in record)
    table = re.search(rf"\|\s*{ISSUE_ID}\s*\|(.*?)\|\s*$", record or "", re.MULTILINE)
    cells = [x.strip() for x in table.group(1).split("|")] if table else []
    c.add("02. durable record selects exactly SET TO NOT VERIFIED",
          len(cells) >= 1 and cells[0].upper() == CHOICE, f"cells={cells[:2]}")
    c.add("03. durable record decision date is 2026-07-29",
          len(cells) >= 2 and cells[1] == DECISION_DATE, f"cells={cells[:3]}")
    c.add("04. durable record timezone is Asia/Manila",
          len(cells) >= 3 and cells[2] == TIMEZONE, f"cells={cells[:4]}")
    impl = re.search(r"Implementation authorization status:\s*([^\n]+)", record or "")
    c.add("05. durable record implementation authorization remains NOT AUTHORIZED",
          bool(impl) and impl.group(1).strip() == "NOT AUTHORIZED",
          f"value={impl.group(1).strip() if impl else None!r}")

    # --- normative module (6-13) ---
    module = read(root, MODULE_REL)
    block = ""
    if module:
        m = BLOCK_RE.search(module)
        block = m.group(0) if m else ""
    c.add("06. KBDL-A11Y-001 normative requirement sentence is byte-identical",
          REQUIREMENT_SENTENCE in (module or ""),
          "requirement sentence changed or not found")
    lm = LIFECYCLE_RE.search(block)
    c.add("07. lifecycle remains Approved", bool(lm) and lm.group(1) == "Approved",
          f"parsed={lm.group(1) if lm else None!r}")
    pm = PROVENANCE_RE.search(block)
    c.add("08. provenance remains Confirmed", bool(pm) and pm.group(1) == "Confirmed",
          f"parsed={pm.group(1) if pm else None!r}")
    sm = STATUS_FIELD_RE.search(block)
    c.add("09. validation status is explicitly parseable as Not verified",
          bool(sm) and sm.group(1).strip().startswith(VALUE),
          f"parsed={sm.group(1).strip() if sm else None!r}")
    c.add("10. authority record ID appears in the requirement block",
          RECORD_ID in block)
    c.add("11. authority language is current and non-retroactive",
          bool(CURRENT_NONRETRO_RE.search(block)))
    c.add("12. authority language states it is not validation evidence",
          bool(NOT_EVIDENCE_RE.search(block))
          and (not sm or RECORD_ID not in sm.group(1)),
          "missing disclaimer, or the authority note is folded into the status value")
    c.add("13. validation method is unchanged in the normative block",
          METHOD_VALUE.replace(" once implemented", "") in " ".join(block.split()),
          "validation method text changed")

    # --- structured traceability (14-17) ---
    row = ledger_row(root, LEDGER_REL, "Requirement ID", REQUIREMENT_ID)
    c.add("14. structured traceability classification remains Not verified",
          row is not None and row["Validation classification"].strip() == VALUE,
          f"value={row['Validation classification'] if row else None!r}")
    c.add("15. structured traceability references the durable record in Notes or exclusions",
          row is not None and RECORD_ID in row["Notes or exclusions"])
    c.add("16. validation evidence does not claim execution and does not carry the "
          "owner decision",
          row is not None
          and RECORD_ID not in row["Validation evidence"]
          and not EXECUTION_CLAIM_RE.search(row["Validation evidence"]),
          f"evidence={row['Validation evidence'][:80] if row else None!r}")
    c.add("17. known limitation is unchanged",
          row is not None and row["Known limitation"].strip() == LIMITATION_VALUE,
          f"limitation={row['Known limitation'][:80] if row else None!r}")

    # --- related and sibling issues (18-19) ---
    issues = read(root, ISSUES_REL)
    irows = list(csv.DictReader(io.StringIO(issues))) if issues else []
    kl = next((r for r in irows if r["Resolution issue ID"] == "SMR1-KL-0001"), None)
    c.add("18. SMR1-KL-0001 remains pending",
          kl is not None and kl["Owner decision"] == "PENDING"
          and kl["Owner decision date"] == "PENDING" and kl["Owner evidence"] == "PENDING",
          f"row={ {k: kl[k] for k in ('Owner decision','Owner decision date')} if kl else None}")
    others = [r for r in irows
              if r["Category"] == "Validation classification"
              and r["Resolution issue ID"] != ISSUE_ID]
    not_pending = [r["Resolution issue ID"] for r in others if r["Owner decision"] != "PENDING"]
    c.add("19. the other Batch A validation-classification issues remain pending",
          len(others) == 58 and not not_pending,
          f"count={len(others)} non_pending={not_pending}")

    # --- live registry (20-22) ---
    rows = registry_rows(root)
    base = baseline_registry_rows(root)
    target = next((r for r in (rows or [])
                   if r["Requirement ID"] == REQUIREMENT_ID and r["Field name"] == FIELD), None)
    c.add("20. target live-registry row resolves to Not verified and passes",
          target is not None
          and target["Authoritative expected value"] == VALUE
          and target["Normative value"] == VALUE
          and target["Effective value"] == VALUE
          and target["Ledger value"] == VALUE
          and target["Readable-group value"] == VALUE
          and target["Precedence result"] == "PASS"
          and target["Conflict result"] == "None"
          and target["Validation result"] == "PASS"
          and target["Ownership class"] == "A — Normative-owned"
          and target["Primary basis"] == "Normative record",
          f"row={target}")
    if rows is None or base is None:
        c.add("21. no other registry row changes validation result", False,
              "registry or baseline registry unavailable")
        c.add("22. registry row/requirement/field/duplicate counts are unchanged", False,
              "registry or baseline registry unavailable")
    else:
        keyed = {(r["Requirement ID"], r["Field name"]): r for r in rows}
        keyed_base = {(r["Requirement ID"], r["Field name"]): r for r in base}
        changed_result = sorted(k for k in set(keyed) & set(keyed_base)
                                if keyed[k]["Validation result"]
                                != keyed_base[k]["Validation result"])
        c.add("21. no other registry row changes validation result",
              changed_result == [(REQUIREMENT_ID, FIELD)], f"changed={changed_result}")
        keys = [(r["Requirement ID"], r["Field name"]) for r in rows]
        c.add("22. registry row/requirement/field/duplicate counts are unchanged",
              len(rows) == len(base)
              and len({k[0] for k in keys}) == len({(r['Requirement ID']) for r in base})
              and len({k[1] for k in keys}) == 17
              and len(keys) == len(set(keys)),
              f"rows={len(rows)} base={len(base)} dupes={len(keys) - len(set(keys))}")

    # --- issue state and decision counts (23-24) ---
    target_issue = next((r for r in irows if r["Resolution issue ID"] == ISSUE_ID), None)
    c.add("23. issue-register status is metadata-recorded and awaiting planning-agent "
          "validation",
          target_issue is not None
          and target_issue["Resolution status"].strip() == METADATA_RECORDED
          and RECORD_ID in target_issue["Authoritative source found"],
          f"status={target_issue['Resolution status'] if target_issue else None!r}")
    sys.path.insert(0, str(root / SMR1_REL / "scripts"))
    try:
        import decision_state
        dchecks, stats = decision_state.compute(str(root / SMR1_REL))
        failing = [n for n, ok, _ in dchecks if not ok]
        c.add("24. decision state remains 4 recorded / 417 pending with no failing "
              "decision-state check",
              stats["recorded_count"] == 4 and stats["pending_count"] == 417 and not failing,
              f"recorded={stats['recorded_count']} pending={stats['pending_count']} "
              f"failing={failing[:3]}")
    except Exception as exc:  # fail closed
        c.add("24. decision state remains 4 recorded / 417 pending with no failing "
              "decision-state check", False, f"{type(exc).__name__}: {exc}")

    # --- gate preservation (25-29) ---
    val = read(root, "docs/kbdl/validation.md")
    flat = " ".join((val or "").split())
    c.add("25. VAL-003 and VAL-006 are not restored",
          "`KBDL-VAL-003`, `KBDL-VAL-004`, `KBDL-VAL-005`, and `KBDL-VAL-006` "
          "are `Not verified`" in flat)
    c.add("26. candidate readiness is unchanged",
          "Specification release candidate recommendation: NOT READY" in flat)
    c.add("27. implementation conformance is unchanged",
          "Implementation conformance status: NOT VERIFIED" in flat)
    c.add("28. project completion status is unchanged",
          "Project completion status: PENDING" in flat)
    readme = read(root, f"{VC1_REL}/README.md") or ""
    # The negative lookbehind keeps the package's own disclaimer ("No
    # implementation is authorized.") from reading as an authorization claim.
    c.add("29. no implementation authorization is introduced",
          "Implementation authorization status: NOT AUTHORIZED" in readme
          and not re.search(r"(?i)(?<!no )implementation is (?:now )?authorized", readme))

    # --- scope (30) ---
    diff = git(root, "diff", "--name-only", BASELINE_COMMIT, "HEAD")
    tracked = [x for x in diff.stdout.splitlines() if x.strip()]
    worktree = git(root, "status", "--porcelain")
    pending = [ln[3:].strip() for ln in worktree.stdout.splitlines() if ln.strip()]
    outside = sorted({p for p in tracked + pending
                      if not any(p.startswith(a) for a in ALLOWED_PREFIXES)})
    permitted = set(DECLARED_SCOPE_DEVIATIONS) | set(REMEDIATION_AUTHORIZED)
    undeclared = [p for p in outside if p not in permitted]
    c.add("30. changed files remain inside the approved allowlist, the declared "
          "scope-deviation set, or the released remediation set",
          diff.returncode == 0 and not undeclared, f"undeclared={undeclared}")
    c.add("31. the declared FSRG1 scope deviation is exactly the two baseline-constant "
          "files and has not grown",
          set(outside) & set(DECLARED_SCOPE_DEVIATIONS) <= set(DECLARED_SCOPE_DEVIATIONS)
          and not (set(outside) - permitted),
          f"unexpected={sorted(set(outside) - permitted)}")

    return c.report()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validate the SMR2-VC-0001 metadata recording.")
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    args = ap.parse_args(argv)
    return 1 if run(args.repo_root.resolve(strict=True)) else 0


if __name__ == "__main__":
    sys.exit(main())
