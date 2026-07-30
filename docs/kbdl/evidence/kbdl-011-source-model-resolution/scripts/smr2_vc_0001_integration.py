#!/usr/bin/env python3
"""SMR1 packet integration for the KBDL-011-SMR2-VC-0001 metadata recording.

Narrow, read-only integration helper, kept out of `validate_packet.py` so no
existing check in that file is disturbed and so the same logic can be exercised
against temporary copies.

From the SMR1 packet's point of view it asserts that:

  VC1.package_present            the SMR2-VC-0001 package and required files exist
  VC1.validator_passes           validate_smr2_vc_0001.py exits 0 with no failed check
  VC1.package_checksums_verify   the package's own checksums verify
  VC1.issue_status_metadata_recorded  SMR1-VC-0001 carries the metadata-recorded status
  VC1.issue_not_finally_resolved      and is not marked resolved/closed/validated
  VC1.classification_unchanged   the effective classification is still Not verified
  VC1.kl_0001_still_pending      SMR1-KL-0001 is untouched
  VC1.other_batch_a_pending      the other 58 Batch A VC issues remain PENDING
  VC1.decision_counts_unchanged  4 durably recorded / 417 pending

It never regenerates the live registry and never writes to the repository.
"""
import csv
import hashlib
import os
import re
import subprocess
import sys

VC1_REL = "docs/kbdl/evidence/kbdl-011-smr2-vc-0001"
SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
LEDGER_REL = "docs/kbdl/traceability-metadata.csv"

ISSUE_ID = "SMR1-VC-0001"
REQUIREMENT_ID = "KBDL-A11Y-001"
VALUE = "Not verified"
RECORD_ID = "KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29"
METADATA_RECORDED = "METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION"
# Advanced by KBDL-011-SMR2-VC-0001-PA1; both are permitted post-recording states.
METADATA_VALIDATED = "METADATA RECORDED — PLANNING-AGENT VALIDATED"
PERMITTED_RECORDED_STATUSES = (METADATA_RECORDED, METADATA_VALIDATED)
FINAL_WORDS = ("RESOLVED", "CLOSED", "COMPLETE", "COMPLETED", "VERIFIED", "VALIDATED")

REQUIRED_FILES = [
    "README.md",
    "implementation-report.md",
    "evidence-manifest.md",
    "evidence-inventory.csv",
    "checksums.sha256",
    "smr2-vc-0001-validation-transcript.txt",
    "scripts/validate_smr2_vc_0001.py",
    "scripts/smr2_vc_0001_fixtures.py",
]

EXPECTED_RECORDED = 4
EXPECTED_PENDING = 417


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def compute(repo):
    """Return a list of (name, ok, detail) checks in validate_packet's shape."""
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))
        return bool(ok)

    pkg = os.path.join(repo, VC1_REL)
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(pkg, f))]
    present = check("VC1.package_present — SMR2-VC-0001 package and required files exist",
                    os.path.isdir(pkg) and not missing, f"missing={missing}")

    if present:
        result = subprocess.run(
            [sys.executable, os.path.join(pkg, "scripts", "validate_smr2_vc_0001.py"),
             "--repo-root", repo], capture_output=True, text=True)
        fails = [ln for ln in result.stdout.splitlines() if ln.startswith("[FAIL]")]
        tail = (result.stdout.strip().splitlines() or ["<no output>"])[-1]
        check("VC1.validator_passes — validate_smr2_vc_0001.py exits 0 with no failed check",
              result.returncode == 0 and not fails,
              f"rc={result.returncode} last={tail} failed={fails[:3]}")
    else:
        check("VC1.validator_passes — validate_smr2_vc_0001.py exits 0 with no failed check",
              False, "package incomplete; validator not run")

    sums = os.path.join(pkg, "checksums.sha256")
    if os.path.isfile(sums):
        bad = []
        with open(sums, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                digest, _, rel = line.rstrip("\n").partition("  ")
                target = os.path.join(repo, rel)
                if not os.path.isfile(target):
                    bad.append(f"MISSING:{rel}")
                elif _sha256(target) != digest:
                    bad.append(f"MISMATCH:{rel}")
        check("VC1.package_checksums_verify — SMR2-VC-0001 checksums verify on disk",
              not bad, f"{bad[:5]}")
    else:
        check("VC1.package_checksums_verify — SMR2-VC-0001 checksums verify on disk",
              False, "checksums.sha256 absent")

    issues_path = os.path.join(repo, SMR1_REL, "issue-register.csv")
    rows = []
    if os.path.isfile(issues_path):
        with open(issues_path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    target = next((r for r in rows if r["Resolution issue ID"] == ISSUE_ID), None)
    check("VC1.issue_status_metadata_recorded — SMR1-VC-0001 is in a permitted "
          "post-recording state (awaiting or planning-agent validated)",
          target is not None
          and target["Resolution status"].strip() in PERMITTED_RECORDED_STATUSES
          and RECORD_ID in target["Authoritative source found"],
          f"status={target['Resolution status'] if target else None!r}")
    status = target["Resolution status"].strip().upper() if target else ""
    check("VC1.issue_not_finally_resolved — no resolved/closed/verified/validated claim",
          bool(target) and not any(status.startswith(w) for w in FINAL_WORDS),
          f"status={status!r}")

    ledger_row = None
    ledger_path = os.path.join(repo, LEDGER_REL)
    if os.path.isfile(ledger_path):
        with open(ledger_path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["Requirement ID"] == REQUIREMENT_ID:
                    ledger_row = r
                    break
    check("VC1.classification_unchanged — KBDL-A11Y-001 remains Not verified",
          ledger_row is not None
          and ledger_row["Validation classification"].strip() == VALUE,
          f"value={ledger_row['Validation classification'] if ledger_row else None!r}")

    kl = next((r for r in rows if r["Resolution issue ID"] == "SMR1-KL-0001"), None)
    check("VC1.kl_0001_still_pending — SMR1-KL-0001 remains PENDING",
          kl is not None and kl["Owner decision"] == "PENDING"
          and kl["Owner decision date"] == "PENDING" and kl["Owner evidence"] == "PENDING",
          f"kl={kl['Owner decision'] if kl else None!r}")

    others = [r for r in rows
              if r["Category"] == "Validation classification"
              and r["Resolution issue ID"] != ISSUE_ID]
    non_pending = [r["Resolution issue ID"] for r in others if r["Owner decision"] != "PENDING"]
    check("VC1.other_batch_a_pending — the other 58 validation-classification issues "
          "remain PENDING",
          len(others) == 58 and not non_pending,
          f"count={len(others)} non_pending={non_pending}")

    # Recording one issue must never advance the batch itself. The four-value
    # map vocabulary permits ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL, so
    # check 17 alone cannot catch Batch A being promoted; this asserts it
    # explicitly.
    unlock_path = os.path.join(repo, SMR1_REL, "implementation-unlock-map.md")
    batch_a = ""
    if os.path.isfile(unlock_path):
        text = open(unlock_path, encoding="utf-8").read()
        for chunk in text.split("\n## "):
            if chunk.split("\n", 1)[0].startswith("Batch A"):
                batch_a = chunk
                break
    statuses = re.findall(r"Status:\s*`([^`]+)`", batch_a)
    check("VC1.batch_a_still_locked — Batch A as a whole remains LOCKED",
          bool(statuses) and all(s.startswith("LOCKED") for s in statuses),
          f"statuses={statuses}")

    sys.path.insert(0, os.path.join(repo, SMR1_REL, "scripts"))
    try:
        import decision_state
        _c, stats = decision_state.compute(os.path.join(repo, SMR1_REL))
        check("VC1.decision_counts_unchanged — 4 durably recorded / 417 pending",
              stats["recorded_count"] == EXPECTED_RECORDED
              and stats["pending_count"] == EXPECTED_PENDING,
              f"recorded={stats['recorded_count']} pending={stats['pending_count']}")
    except Exception as exc:  # fail closed
        check("VC1.decision_counts_unchanged — 4 durably recorded / 417 pending",
              False, f"{type(exc).__name__}: {exc}")

    checks.extend(check_next_review_queue(repo, rows))

    return checks


# --- KBDL-011-SMR2-VC-0001-PA1: next-review queue integrity (QUEUE1-QUEUE12) ---

NEXT_TARGET = "SMR1-VC-0002"
NEXT_REQUIREMENT = "KBDL-A11Y-004"
BRIEF_REL = f"{SMR1_REL}/smr1-vc-0002-owner-decision-brief.md"
REVIEW_REL = f"{SMR1_REL}/project-owner-review.md"

# A *current* queue designation. Historical or illustrative mentions are
# excluded by requiring the "next ... review target" phrasing rather than any
# bare mention of an issue ID, and by skipping paragraphs marked historical.
QUEUE_CLAIM_RE = re.compile(
    # "next [Batch A] [owner-]review target ... SMR1-XX-NNNN", where the short
    # qualifier allows the ledger metric name ("Next Batch A owner-review
    # target") as well as prose.
    r"next[^.\n]{0,20}?(?:owner-)?review target[^.\n]{0,90}?(SMR1-[A-Z]+-\d+)|"
    r"(SMR1-[A-Z]+-\d+)[^.\n]{0,60}?is the (?:sole |current |only )?next",
    re.IGNORECASE)
HISTORICAL_QUEUE_RE = re.compile(
    r"historical|previously|formerly|at the .{0,40}point", re.IGNORECASE)
ELIGIBILITY_CLAIM_RE = re.compile(
    r"(?:metadata[- ]recording prompt|recording prompt)[^.\n]{0,80}?"
    r"(?:SMR1-VC-0002|KBDL-A11Y-004)[^.\n]{0,40}?"
    r"\b(?:is|are)\s+(?:now\s+)?(?:ready|eligible|approved|released|unlocked)\b",
    re.IGNORECASE)

ADMIN_FILES = (
    f"{SMR1_REL}/implementation-unlock-map.md",
    REVIEW_REL,
    f"{SMR1_REL}/source-model-resolution-packet.md",
    f"{SMR1_REL}/source-model-resolution-ledger.csv",
    f"{SMR1_REL}/implementation-report.md",
    f"{SMR1_REL}/evidence-manifest.md",
)


def check_next_review_queue(repo, rows):
    """QUEUE1-QUEUE12: exactly one next-review target, and it stays untouched."""
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))
        return bool(ok)

    target = next((r for r in rows if r["Resolution issue ID"] == NEXT_TARGET), None)
    check("QUEUE3. the next-review target exists in issue-register.csv", target is not None)
    check("QUEUE4. the next-review target belongs to Batch A (Validation classification)",
          target is not None and target["Category"] == "Validation classification"
          and target["Requirement ID"] == NEXT_REQUIREMENT,
          f"category={target['Category'] if target else None!r}")
    check("QUEUE5. the next-review target is entirely pending",
          target is not None
          and target["Owner decision"] == "PENDING"
          and target["Owner decision date"] == "PENDING"
          and target["Owner evidence"] == "PENDING"
          and target["Resolution status"].strip() == "SOURCE EVIDENCE REQUIRED",
          f"decision={target['Owner decision'] if target else None!r} "
          f"status={target['Resolution status'] if target else None!r}")

    sys.path.insert(0, os.path.join(repo, SMR1_REL, "scripts"))
    try:
        import decision_state
        records, _files, _impl = decision_state.parse_durable_records(
            os.path.join(repo, SMR1_REL))
        check("QUEUE6. the next-review target has no durable owner-decision record",
              NEXT_TARGET not in records, f"records={sorted(records)}")
    except Exception as exc:  # fail closed
        check("QUEUE6. the next-review target has no durable owner-decision record",
              False, f"{type(exc).__name__}: {exc}")

    review = ""
    rp = os.path.join(repo, REVIEW_REL)
    if os.path.isfile(rp):
        review = open(rp, encoding="utf-8").read()
    block = ""
    marker = "### Next issue-level review — SMR1-VC-0002"
    if marker in review:
        block = re.split(r"\n## |\n### ", review.split(marker, 1)[1])[0]
    selected = re.findall(r"(?m)^- \[[xX]\]", block)
    unselected = re.findall(r"(?m)^- \[ \]", block)
    check("QUEUE7. every next-review checkbox is unselected",
          bool(block.strip()) and not selected and len(unselected) == 5,
          f"selected={len(selected)} unselected={len(unselected)}")

    check("QUEUE8. the next-review target carries no metadata-recording status",
          target is not None
          and "METADATA RECORDED" not in target["Resolution status"].upper(),
          f"status={target['Resolution status'] if target else None!r}")

    named = {}
    for rel in ADMIN_FILES:
        fp = os.path.join(repo, rel)
        if not os.path.isfile(fp):
            continue
        text = open(fp, encoding="utf-8").read()
        for m in QUEUE_CLAIM_RE.finditer(text):
            start = text.rfind("\n\n", 0, m.start())
            start = 0 if start == -1 else start
            end = text.find("\n\n", m.end())
            para = text[start:end if end != -1 else len(text)]
            if HISTORICAL_QUEUE_RE.search(para):
                continue
            named.setdefault(m.group(1) or m.group(2), set()).add(rel)
    check("QUEUE1. exactly one current next-review target is named across the "
          "administrative files", len(named) == 1,
          f"named={ {k: sorted(v) for k, v in named.items()} }")
    check("QUEUE2. the named next-review target is exactly SMR1-VC-0002",
          set(named) == {NEXT_TARGET}, f"named={sorted(named)}")
    check("QUEUE9. no other issue is named as the next/current/active review target",
          not (set(named) - {NEXT_TARGET}), f"others={sorted(set(named) - {NEXT_TARGET})}")

    eligibility = []
    for rel in (f"{SMR1_REL}/implementation-unlock-map.md", REVIEW_REL, BRIEF_REL,
                f"{SMR1_REL}/source-model-resolution-packet.md"):
        fp = os.path.join(repo, rel)
        if os.path.isfile(fp) and ELIGIBILITY_CLAIM_RE.search(
                open(fp, encoding="utf-8").read()):
            eligibility.append(rel)
    check("QUEUE10. no metadata-recording prompt for the next-review target is ready, "
          "eligible, approved, released, or unlocked", not eligibility,
          f"claims_in={eligibility}")

    unlock_path = os.path.join(repo, SMR1_REL, "implementation-unlock-map.md")
    batch_a = ""
    if os.path.isfile(unlock_path):
        for chunk in open(unlock_path, encoding="utf-8").read().split("\n## "):
            if chunk.split("\n", 1)[0].startswith("Batch A"):
                batch_a = chunk
                break
    statuses = re.findall(r"Status:\s*`([^`]+)`", batch_a)
    check("QUEUE11. Batch A remains LOCKED while a next-review target is queued",
          bool(statuses) and all(s.startswith("LOCKED") for s in statuses),
          f"statuses={statuses}")

    brief = ""
    bp = os.path.join(repo, BRIEF_REL)
    if os.path.isfile(bp):
        brief = open(bp, encoding="utf-8").read()
    check("QUEUE12. the owner-decision brief exists and disclaims being a decision",
          bool(brief) and NEXT_TARGET in brief and NEXT_REQUIREMENT in brief
          and "records no decision, selects no option" in brief
          and "Implementation authorization status: NOT AUTHORIZED" in brief,
          "brief missing or lacks its non-decision disclaimer")

    return checks
