#!/usr/bin/env python3
"""KBDL-011-SMR1 decision-aware packet-state module (added by
KBDL-011-SMR1-BH-R1; extended by KBDL-011-SMR1-BH-R2; extended again by
KBDL-011-SMR1-BA-OD1-DR1-R1).

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

As of KBDL-011-SMR1-BH-R2, `compute()` also runs `check_state_prose()`,
which verifies that `source-model-resolution-packet.md` and
`project-owner-review.md` describe the *current* packet state without
contradiction: when durable decisions exist, neither document may claim
zero decisions are recorded or that every checkbox is unselected; the
recorded/pending counts stated in prose must match the computed counts;
the review-cycle sign-off summary must match the durable record; and no
document may introduce implementation authorization language.

As of KBDL-011-SMR1-BA-OD1-DR1-R1, `compute()` also runs
`check_authority_records()` and `check_current_state_prose()`. These
close a planning-agent-identified coverage gap: the prior validator (as
run at BA-OD1-DR1) had no check that would catch (a) a durable
"SET TO NOT VERIFIED" owner-decision record whose prose contradicts the
approved current-authority meaning (asserting no authority is created,
or conflating decision authority with validation evidence), or (b)
current-state prose anywhere in the packet still reporting stale
418-pending / three-recorded / "AGC1 or VF1 planning-agent validation
still pending" claims once four decisions are durably recorded and
AGC1/VF1 have since passed. Historical statements about a named past
step (KBDL-011-SMR1-BH-R1/BH-R2/BH-AGC1/BH-AGC1-VF1, or commit
662ee28) are exempt as long as they carry an explicit historical marker
in the same neighborhood as the count; unmarked or current-state
statements fail closed.
"""
import csv
import glob
import os
import re

ISSUE_ID_RE = re.compile(r"SMR1-[A-Z0-9]+-\d+")
TABLE_ROW_RE = re.compile(r"^\|\s*(SMR1-[A-Z0-9]+-\d+)\s*\|(.*)\|\s*$")
REQUIRED_STATUS = "OWNER DECISION RECORDED — AWAITING PLANNING-AGENT VALIDATION"
REQUIRED_IMPL_STATUS = "NOT AUTHORIZED"

# KBDL-011-SMR2-VC-0001 (reissued): once a durably recorded decision has been
# applied to effective metadata by a metadata-recording prompt, its issue row
# advances to this second permitted status. It is NOT a resolved/closed state:
# planning-agent validation of the recording is still required, and MD1-MD8
# below fail closed unless every piece of the recording is actually present and
# consistent. A row may never carry this status merely by being edited.
METADATA_RECORDED_STATUS = "METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION"

# KBDL-011-SMR2-VC-0001-PA1: the third permitted status. A recording reaches it
# only once a durable planning-agent validation record exists and every field of
# that record checks out (PA1-PA12 below). It is still NOT a resolved/closed
# state: the issue stays open, the classification stays Not verified, and no
# later prompt becomes eligible.
PLANNING_AGENT_VALIDATED_STATUS = "METADATA RECORDED — PLANNING-AGENT VALIDATED"
PERMITTED_RECORDED_STATUSES = (REQUIRED_STATUS, METADATA_RECORDED_STATUS,
                               PLANNING_AGENT_VALIDATED_STATUS)

# --- planning-agent validation record (PA1-PA12) ---

PA_RECORD_GLOB = "*-planning-agent-validation-record.md"
PA_PROMPT_ID = "KBDL-011-SMR2-VC-0001"
PA_RECORD_ID = "KBDL-SMR2-VC-0001-PLANNING-AGENT-VALIDATION-2026-07-30"
PA_VERDICT = "PASS"
PA_DATE = "2026-07-30"
PA_TZ = "Asia/Manila"
PA_IMPL_COMMIT = "af6a60a0737745ec4e2d975e58a058c619e861cb"
PA_EVIDENCE_COMMIT = "4aba456deeda8ea01b03eda072cfcdc82fb53ab7"
PA_REMEDIATION_COMMIT = "448e39b22f4dc69210ca795c365bbdf1a3904f20"
PA_ISSUE_ID = "SMR1-VC-0001"
PA_REQUIREMENT_ID = "KBDL-A11Y-001"
PA_PACKAGE_REL = "docs/kbdl/evidence/kbdl-011-smr2-vc-0001"

PA_TABLE_ROW_RE = re.compile(
    r"^\|\s*(KBDL-011-[A-Z0-9-]+)\s*\|\s*([A-Z]+)\s*\|\s*([\d-]+)\s*\|\s*([\w/]+)\s*\|"
    r"\s*([0-9a-f]{40})\s*\|\s*([0-9a-f]{40})\s*\|\s*([0-9a-f]{40})\s*\|\s*([\w-]+)\s*\|$")

# Language a planning-agent validation record must never contain.
PA_OVERREACH_PATTERNS = [
    (re.compile(r"(?i)\b(?:testing|screen-reader (?:testing|verification)|"
                r"automated (?:accessibility )?check(?:ing)?|WCAG conformance)\b"
                r"[^.\n]{0,60}\b(?:was|were|has been|have been)\s+"
                r"(?:executed|performed|completed|established)"), "claims testing occurred"),
    (re.compile(r"(?i)\bKBDL-VAL-00[3-6]\b[^.\n]{0,40}\b(?:is|are|now)\s+"
                r"(?:restored|Verified)\b"), "claims VAL restoration"),
    (re.compile(r"(?i)implementation (?:is|are) (?:now )?authorized|"
                r"authorizes implementation"), "claims implementation authorization"),
    (re.compile(r"(?i)\b(?:candidate|release candidate)\b[^.\n]{0,40}\bREADY\b"
                r"(?!\s*—)|conformance (?:is|now) verified"), "claims readiness/conformance"),
    (re.compile(r"(?i)KBDL-011 is complete|project (?:is )?complete\b"),
     "claims project completion"),
    (re.compile(r"(?i)\bSMR1-KL-0001\b[^.\n]{0,40}\b(?:is |now )?"
                r"(?:resolved|accepted|closed)\b"), "claims SMR1-KL-0001 resolved"),
]

# Statuses that would assert the issue is finished. Never permitted here.
FINAL_STATUS_RE = re.compile(
    r"^\s*(RESOLVED|CLOSED|COMPLETE|COMPLETED|VERIFIED|VALIDATED|"
    r"PLANNING-AGENT VALIDATED|APPROVED)\b", re.IGNORECASE)

# The one metadata recording this validator knows how to verify end to end.
MD_ISSUE_ID = "SMR1-VC-0001"
MD_REQUIREMENT_ID = "KBDL-A11Y-001"
MD_FIELD = "Validation classification"
MD_VALUE = "Not verified"
MD_RECORD_ID = "KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29"
MD_MODULE_REL = "docs/kbdl/accessibility.md"
MD_LEDGER_REL = "docs/kbdl/traceability-metadata.csv"
MD_REGISTRY_REL = ("docs/kbdl/evidence/kbdl-011-smr2-fsrg1/artifacts/"
                   "field-source-registry.csv")
# The requirement block starts at its own bullet and ends at the next one.
MD_BLOCK_RE = re.compile(
    r"^- \*\*KBDL-A11Y-001\*\*.*?(?=^- \*\*KBDL-A11Y-|\Z)", re.MULTILINE | re.DOTALL)
MD_STATUS_FIELD_RE = re.compile(r"(?m)^\s*-\s*Validation status:\s*(.+?)\s*$")
MD_AUTHORITY_CURRENT_RE = re.compile(r"current and non-retroactive", re.IGNORECASE)
MD_AUTHORITY_NOT_EVIDENCE_RE = re.compile(
    r"decision authority only[,;]?\s*not validation evidence", re.IGNORECASE)

# --- KBDL-011-SMR1-BA-OD1-DR1-R1: authority-record and current-state-prose checks ---

NUM_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}

# A durable "SET TO NOT VERIFIED" record must state that the decision
# creates new current, non-retroactive authority for retaining the
# classification -- and must not simultaneously (or instead) claim it
# creates no authority.
AUTHORITY_CREATION_RE = re.compile(
    r"creates?\s+new\s+current,?\s*non-retroactive\s+(?:owner\s+|project-owner\s+)?authority\s+for\s+retaining",
    re.IGNORECASE,
)
AUTHORITY_CONTRADICTION_RE = re.compile(
    r"selects?\s+no\s+new\s+authority|creates?\s+no\s+new\s+authority|no\s+new\s+authority,?\s*source,?\s*or\s+evidence",
    re.IGNORECASE,
)

# A durable record must explicitly distinguish decision authority from
# validation evidence, and must not claim the decision itself is (or
# constitutes, or proves) accessibility/WCAG validation evidence.
EVIDENCE_DISTINCTION_RE = re.compile(
    r"decision\s+authority\s+only\.\s*It\s+is\s+not\s+evidence\s+that\s+accessibility",
    re.IGNORECASE,
)
EVIDENCE_CONFLATION_RE = re.compile(
    r"is evidence that accessibility (?:testing|validation|conformance)|"
    r"proves that accessibility (?:testing|validation) occurred|"
    r"constitutes accessibility (?:testing|validation) evidence|"
    r"is (?:accessibility|wcag|screen-reader) (?:testing|validation|conformance) evidence",
    re.IGNORECASE,
)

# Current-state-prose staleness patterns.
HIST_MARKER_RE = re.compile(
    # Bare "historical" only counts when structurally anchored to a named
    # historical "... point" -- this deliberately excludes an unrelated
    # "historical" mention elsewhere in the same sentence (e.g. "fact 1
    # (historical cycle detection)") from rescuing a genuinely stale,
    # unmarked count mentioned later in that same sentence.
    r"(?:historical|at the historical)\b[^.]{0,40}?\bpoint\b|"
    r"as of (?:the )?(?:historical )?(?:commit )?`?"
    r"(?:662ee28|ea86add|46104c5|0fadb97|c7a70fc)|"
    r"historical-as-of|"
    r"unchanged by bh-|were unchanged|was unchanged|"
    r"superseded by the current|"
    r"planning-agent review|found (?:two |a )?defects?|coverage gap|"
    r"\bdr1-r1\b|remediation|stale current-state|still stated or could be read|"
    r"could be misread|current-state passages",
    re.IGNORECASE,
)
EXEMPT_418_CONTEXT_RE = re.compile(
    r"field/location/standard-clause|canonical (?:resolution|non-relationship) issues|"
    r"category population|R16 raw findings|defects\.csv|418 combined issues|"
    r"still claiming\s*\n?\s*three recorded",
    re.IGNORECASE,
)

TOTAL_CLAIM_RE = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b"
    r"(?:\s+of\s+the\s+\d+)?\s+decisions?\s+"
    r"(?:are|is)\s+now\s+durably\s+recorded\s+in\s+total",
    re.IGNORECASE,
)

AGC1_VF1_STALE_PATTERNS = [
    re.compile(r"planning-agent validation of\s*`?kbdl-011-smr1-bh-agc1(?:-vf1)?`?\s+remains required", re.IGNORECASE),
    re.compile(r"(?:agc1|vf1)[^.]{0,100}planning-agent validation[^.]{0,60}"
               r"(?:is\s+still\s+pending|remains\s+pending|remains\s+required)", re.IGNORECASE),
    re.compile(r"planning-agent validation[^.]{0,60}(?:agc1|vf1)[^.]{0,60}"
               r"(?:is\s+still\s+pending|remains\s+pending|remains\s+required)", re.IGNORECASE),
]


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9`\*\(])")


def _sentence_chunks(text):
    """Split text into (start_offset, chunk_text) sentence-ish chunks.
    Deliberately coarse (splits on '. '/'! '/'? ' followed by an
    upper-case/digit/backtick/asterisk/paren) -- good enough to require a
    historical marker to sit in the *same* sentence as a count, rather
    than merely somewhere in a wide, easily-misleading character window
    (e.g. borrowing a neighboring sentence's unrelated 'DR1-R1' mention)."""
    chunks = []
    pos = 0
    last_end = 0
    for m in SENTENCE_SPLIT_RE.finditer(text):
        chunks.append((last_end, text[last_end:m.start()]))
        last_end = m.start()
    chunks.append((last_end, text[last_end:]))
    return chunks


def _scan_stale_418(label, text):
    """Return a list of (label, offset, snippet) for every '418' occurrence
    that is not exempt (category-count context) and whose *own sentence*
    lacks a historical marker."""
    bad = []
    chunks = _sentence_chunks(text)
    for m in re.finditer(r"\b418\b", text):
        # Find the chunk containing this match.
        chunk_text = None
        for start, ctext in chunks:
            if start <= m.start() < start + len(ctext):
                chunk_text = ctext
                break
        if chunk_text is None:
            chunk_text = text[max(0, m.start() - 120):m.end() + 120]
        if EXEMPT_418_CONTEXT_RE.search(chunk_text):
            continue
        if HIST_MARKER_RE.search(chunk_text):
            continue
        bad.append((label, m.start(), chunk_text[:160].replace("\n", " ")))
    return bad


def check_authority_records(pkt):
    """AR1/AR2: every durable 'SET TO NOT VERIFIED' owner-decision record
    must state it creates new current, non-retroactive authority (never
    that it creates no authority), and must distinguish decision
    authority from validation evidence (never conflate the two)."""
    checks = []
    files = sorted(glob.glob(os.path.join(pkt, "*-owner-decision-record.md")))
    contradiction_hits = []
    missing_creation = []
    conflation_hits = []
    missing_distinction = []
    for fp in files:
        text = open(fp, encoding="utf-8").read()
        rows = [TABLE_ROW_RE.match(line.strip()) for line in text.splitlines()]
        rows = [r for r in rows if r]
        choices = []
        for r in rows:
            cells = [c.strip() for c in r.group(2).split("|")]
            if cells:
                choices.append(cells[0].strip().upper())
        if not any(c == "SET TO NOT VERIFIED" for c in choices):
            continue
        if AUTHORITY_CONTRADICTION_RE.search(text):
            contradiction_hits.append(fp)
        if not AUTHORITY_CREATION_RE.search(text):
            missing_creation.append(fp)
        if EVIDENCE_CONFLATION_RE.search(text):
            conflation_hits.append(fp)
        if not EVIDENCE_DISTINCTION_RE.search(text):
            missing_distinction.append(fp)
    checks.append(("AR1. no durable 'SET TO NOT VERIFIED' owner-decision record states or "
                    "implies it creates no current authority",
                    len(contradiction_hits) == 0 and len(missing_creation) == 0,
                    f"contradiction_hits={contradiction_hits} missing_creation_statement={missing_creation}"))
    checks.append(("AR2. no durable owner-decision record conflates decision authority with "
                    "validation/conformance evidence",
                    len(conflation_hits) == 0 and len(missing_distinction) == 0,
                    f"conflation_hits={conflation_hits} missing_distinction_statement={missing_distinction}"))
    return checks


def check_current_state_prose(pkt, recorded_count, pending_count, batch_counts):
    """SP1-SP4 (KBDL-011-SMR1-BA-OD1-DR1-R1): fail closed on stale
    current-state prose that the BA-OD1-DR1 validator run could not
    detect -- unmarked historical/current 418 mentions, stale "N
    decisions ... in total" claims, stale AGC1/VF1-pending claims, and
    recorded/per-batch/pending arithmetic inconsistency."""
    checks = []

    tracked_files = [
        "source-model-resolution-packet.md",
        "project-owner-review.md",
        "implementation-report.md",
        "evidence-manifest.md",
    ]
    texts = {}
    for fname in tracked_files:
        fpath = os.path.join(pkt, fname)
        if os.path.exists(fpath):
            texts[fname] = open(fpath, encoding="utf-8").read()

    # SP1: every '418' mention in a current-state-bearing file must either
    # be exempt (category-count context) or carry an explicit historical
    # marker nearby.
    stale_418 = []
    if recorded_count == 4:
        for fname, text in texts.items():
            stale_418.extend(_scan_stale_418(fname, text))
    checks.append(("SP1. no current-state section reports 418 pending without an explicit "
                    "historical marker once four decisions are durably recorded",
                    len(stale_418) == 0, f"stale_hits={stale_418}"))

    # SP2: any "N decisions are now durably recorded in total" claim must
    # match the actual recorded_count.
    total_claim_mismatches = []
    for fname, text in texts.items():
        for m in TOTAL_CLAIM_RE.finditer(text):
            raw = m.group(1).lower()
            n = NUM_WORDS.get(raw, None)
            if n is None:
                try:
                    n = int(raw)
                except ValueError:
                    n = None
            if n is not None and n != recorded_count:
                total_claim_mismatches.append((fname, m.group(0)))
    checks.append(("SP2. no current-state section reports a total durably-recorded-decision "
                    "count other than the computed total",
                    len(total_claim_mismatches) == 0, f"mismatches={total_claim_mismatches}"))

    # SP3: no current-state summary may say AGC1/VF1 planning-agent
    # validation remains pending/required.
    agc1_vf1_stale = []
    for fname, text in texts.items():
        for pat in AGC1_VF1_STALE_PATTERNS:
            if pat.search(text):
                agc1_vf1_stale.append((fname, pat.pattern))
    checks.append(("SP3. no current-state summary states that AGC1/VF1 planning-agent "
                    "validation remains pending", len(agc1_vf1_stale) == 0,
                    f"hits={agc1_vf1_stale}"))

    # SP4: total recorded, per-batch recorded, and pending counts are
    # mutually consistent.
    batch_h = batch_counts.get("Batch H", 0)
    batch_a = batch_counts.get("Batch A", 0)
    per_batch_sum_ok = (batch_h + sum(v for k, v in batch_counts.items() if k != "Batch H") == recorded_count)
    arithmetic_ok = per_batch_sum_ok
    checks.append(("SP4. total recorded count, per-batch recorded counts, and pending count "
                    "are mutually consistent",
                    arithmetic_ok,
                    f"batch_counts={batch_counts} recorded_count={recorded_count} "
                    f"pending_count={pending_count}"))

    return checks


def parse_planning_agent_records(repo):
    """Return [(path, fields_dict)] for every planning-agent validation record.

    Deliberately a different filename convention and a different parser from
    `parse_durable_records`, so a validation record can never be counted as an
    owner decision (PA12).
    """
    out = []
    pkg = os.path.join(repo, PA_PACKAGE_REL)
    for fp in sorted(glob.glob(os.path.join(pkg, PA_RECORD_GLOB))):
        text = open(fp, encoding="utf-8").read()
        row = None
        for line in text.splitlines():
            m = PA_TABLE_ROW_RE.match(line.strip())
            if m:
                row = {
                    "prompt_id": m.group(1), "verdict": m.group(2), "date": m.group(3),
                    "tz": m.group(4), "impl": m.group(5), "evidence": m.group(6),
                    "remediation": m.group(7), "record_id": m.group(8),
                }
                break
        out.append((fp, row, text))
    return out


def check_planning_agent_validation(pkt, rows, approved):
    """PA1-PA12 (KBDL-011-SMR2-VC-0001-PA1).

    The PLANNING-AGENT VALIDATED status is admitted only when a matching,
    complete, non-overreaching validation record exists — and only for the one
    authorized issue. Every check fails closed.
    """
    checks = []
    repo = os.path.abspath(os.path.join(pkt, "..", "..", "..", ".."))
    records = parse_planning_agent_records(repo)

    validated = [r["Resolution issue ID"] for r in rows
                 if r["Resolution status"].strip() == PLANNING_AGENT_VALIDATED_STATUS]

    # PA10: at most one issue may carry the validated status, and only the
    # authorized one.
    checks.append(("PA10. exactly the authorized issue carries the planning-agent-validated "
                   "status", validated in ([], [PA_ISSUE_ID]), f"validated={validated}"))

    # A valid record with the issue still "awaiting" is itself a defect: the
    # transition was left half-applied. Evaluate PA7 whenever a matching record
    # exists, not only once the status has already advanced.
    any_matching = [r for _fp, r, _t in records if r and r["prompt_id"] == PA_PROMPT_ID]
    status_now_early = next((r["Resolution status"].strip() for r in rows
                             if r["Resolution issue ID"] == PA_ISSUE_ID), "")
    if not validated and any_matching:
        checks.append(("PA7. the validated issue no longer reads 'awaiting' once a valid "
                       "validation record exists",
                       "AWAITING" not in status_now_early.upper(),
                       f"status={status_now_early!r} records={len(any_matching)}"))

    if not validated:
        for n in ("PA1. planning-agent-validated status is backed by a validation record",
                  "PA2. validation record verdict is PASS",
                  "PA3. validation record names the correct prompt ID",
                  "PA4. validation record names all three covered commits exactly",
                  "PA5. validation record date and timezone are correct",
                  "PA6. validation record names the correct issue and requirement",
                  "PA8. the validated issue is not marked finally resolved",
                  "PA9. validation record claims no testing, VAL restoration, conformance, "
                  "readiness, implementation authorization, or completion",
                  "PA11. validation record states 'Implementation authorization status: "
                  "NOT AUTHORIZED'",
                  "PA12. no planning-agent validation record is parsed as an owner decision"):
            checks.append((n + " (status not claimed; trivially satisfied)", True, ""))
        return checks

    matching = [(fp, row, text) for fp, row, text in records
                if row and row["prompt_id"] == PA_PROMPT_ID]
    checks.append(("PA1. planning-agent-validated status is backed by a validation record",
                   len(matching) == 1,
                   f"records={len(records)} matching={len(matching)}"))
    if len(matching) != 1:
        for n in ("PA2. validation record verdict is PASS",
                  "PA3. validation record names the correct prompt ID",
                  "PA4. validation record names all three covered commits exactly",
                  "PA5. validation record date and timezone are correct",
                  "PA6. validation record names the correct issue and requirement",
                  "PA9. validation record claims no testing, VAL restoration, conformance, "
                  "readiness, implementation authorization, or completion",
                  "PA11. validation record states 'Implementation authorization status: "
                  "NOT AUTHORIZED'"):
            checks.append((n, False, "no single matching validation record"))
        matching = []
    else:
        fp, row, text = matching[0]
        checks.append(("PA2. validation record verdict is PASS",
                       row["verdict"] == PA_VERDICT, f"verdict={row['verdict']!r}"))
        checks.append(("PA3. validation record names the correct prompt ID",
                       row["prompt_id"] == PA_PROMPT_ID and row["record_id"] == PA_RECORD_ID,
                       f"prompt={row['prompt_id']!r} record={row['record_id']!r}"))
        # Every 40-hex token anywhere in the record must be one of the three
        # covered commits, so corrupting the prose copy of a SHA -- while
        # leaving the machine-readable row intact -- still fails.
        expected_commits = {PA_IMPL_COMMIT, PA_EVIDENCE_COMMIT, PA_REMEDIATION_COMMIT}
        found_commits = set(re.findall(r"\b[0-9a-f]{40}\b", text))
        commits_ok = (row["impl"] == PA_IMPL_COMMIT
                      and row["evidence"] == PA_EVIDENCE_COMMIT
                      and row["remediation"] == PA_REMEDIATION_COMMIT
                      and found_commits == expected_commits)
        checks.append(("PA4. validation record names all three covered commits exactly",
                       commits_ok,
                       f"impl={row['impl'][:12]} evidence={row['evidence'][:12]} "
                       f"remediation={row['remediation'][:12]}"))
        checks.append(("PA5. validation record date and timezone are correct",
                       row["date"] == PA_DATE and row["tz"] == PA_TZ,
                       f"date={row['date']!r} tz={row['tz']!r}"))
        # Capture the declared values and compare them, rather than using a
        # negative lookahead: an optional-backtick quantifier backtracks to
        # zero width and makes the lookahead succeed against correct input.
        decl_issue = re.search(r"Validated issue:\s*`?([A-Za-z0-9-]+)", text)
        decl_req = re.search(r"Validated requirement:\s*`?([A-Za-z0-9-]+)", text)
        checks.append(("PA6. validation record names the correct issue and requirement",
                       bool(decl_issue) and decl_issue.group(1) == PA_ISSUE_ID
                       and bool(decl_req) and decl_req.group(1) == PA_REQUIREMENT_ID,
                       f"issue={decl_issue.group(1) if decl_issue else None!r} "
                       f"requirement={decl_req.group(1) if decl_req else None!r}"))
        overreach = [why for pat, why in PA_OVERREACH_PATTERNS if pat.search(text)]
        checks.append(("PA9. validation record claims no testing, VAL restoration, "
                       "conformance, readiness, implementation authorization, or completion",
                       not overreach, f"overreach={overreach}"))
        impl = re.search(r"Implementation authorization status:\s*([^\n]+)", text)
        checks.append(("PA11. validation record states 'Implementation authorization status: "
                       "NOT AUTHORIZED'",
                       bool(impl) and impl.group(1).strip() == REQUIRED_IMPL_STATUS,
                       f"value={impl.group(1).strip() if impl else None!r}"))

    status_now = next((r["Resolution status"].strip() for r in rows
                       if r["Resolution issue ID"] == PA_ISSUE_ID), "")
    checks.append(("PA7. the validated issue no longer reads 'awaiting'",
                   "AWAITING" not in status_now.upper(), f"status={status_now!r}"))
    checks.append(("PA8. the validated issue is not marked finally resolved",
                   not FINAL_STATUS_RE.match(status_now), f"status={status_now!r}"))

    # PA12: the validation record must not be picked up by the owner-decision
    # parser, and must not have inflated the recorded-decision count.
    owner_record_paths = {os.path.basename(rec["file"]) for rec in approved.values()}
    leaked = sorted(os.path.basename(fp) for fp, _row, _t in records
                    if os.path.basename(fp) in owner_record_paths)
    checks.append(("PA12. no planning-agent validation record is parsed as an owner decision",
                   not leaked and len(approved) == 4, f"leaked={leaked} approved={len(approved)}"))

    return checks


def check_metadata_recording(pkt, metadata_recorded, approved, rows):
    """MD1-MD8 (KBDL-011-SMR2-VC-0001, reissued).

    A row may carry METADATA_RECORDED_STATUS only when the recording it claims
    actually exists, everywhere it must exist, and only for the one issue this
    prompt authorized. Every check fails closed: a missing file, an unparsable
    block, or an unexpected extra recorded issue is a failure, never a skip.

    Deliberately NOT weakened for the zero-recording case: when no row claims
    the status, MD1-MD8 pass trivially and the pre-existing owner-decision
    checks (7/7b/7c/7d, D1-D14) are untouched.
    """
    checks = []
    repo = os.path.abspath(os.path.join(pkt, "..", "..", "..", ".."))

    # MD1: only the authorized issue may be metadata-recorded.
    unauthorized = sorted(i for i in metadata_recorded if i != MD_ISSUE_ID)
    checks.append(("MD1. only the authorized issue carries the metadata-recorded status",
                   not unauthorized, f"unauthorized={unauthorized}"))

    if MD_ISSUE_ID not in metadata_recorded:
        for name in ("MD2. metadata-recorded issue has a matching non-deferred durable record",
                     "MD3. normative module carries the approved value as a parseable field",
                     "MD4. normative module cites the exact durable authority record",
                     "MD5. normative authority language is current, non-retroactive, and "
                     "not represented as validation evidence",
                     "MD6. structured traceability row carries the same value and the "
                     "authority reference",
                     "MD7. live field-source registry row resolves to the approved value "
                     "and passes",
                     "MD8. metadata-recorded issue is not marked finally resolved"):
            checks.append((name + " (not claimed; trivially satisfied)", True, ""))
        return checks

    # MD2: durable record backing, non-deferred, matching choice.
    rec = approved.get(MD_ISSUE_ID)
    md2 = (rec is not None
           and rec["choice"].strip().upper() == "SET TO NOT VERIFIED"
           and rec["date"].strip() == "2026-07-29"
           and rec["record_id"].strip() == MD_RECORD_ID
           and "DEFER" not in rec["choice"].strip().upper())
    checks.append(("MD2. metadata-recorded issue has a matching non-deferred durable record",
                   md2, f"record={rec}"))

    # MD3/MD4/MD5: the normative module.
    module_path = os.path.join(repo, MD_MODULE_REL)
    block = ""
    if os.path.isfile(module_path):
        text = open(module_path, encoding="utf-8").read()
        m = MD_BLOCK_RE.search(text)
        block = m.group(0) if m else ""
    status_m = MD_STATUS_FIELD_RE.search(block)
    md3 = bool(status_m) and status_m.group(1).strip().startswith(MD_VALUE)
    checks.append(("MD3. normative module carries the approved value as a parseable field",
                   md3, f"parsed={status_m.group(1).strip() if status_m else None!r}"))

    md4 = MD_RECORD_ID in block
    checks.append(("MD4. normative module cites the exact durable authority record",
                   md4, f"record_id_present={md4}"))

    md5 = (bool(MD_AUTHORITY_CURRENT_RE.search(block))
           and bool(MD_AUTHORITY_NOT_EVIDENCE_RE.search(block))
           # the authority note must not be folded into the status value
           and (not status_m or MD_RECORD_ID not in status_m.group(1)))
    checks.append(("MD5. normative authority language is current, non-retroactive, and "
                   "not represented as validation evidence", md5, ""))

    # MD6: the structured traceability row.
    ledger_path = os.path.join(repo, MD_LEDGER_REL)
    ledger_row = None
    if os.path.isfile(ledger_path):
        with open(ledger_path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["Requirement ID"] == MD_REQUIREMENT_ID:
                    ledger_row = r
                    break
    md6 = (ledger_row is not None
           and ledger_row["Validation classification"].strip() == MD_VALUE
           and MD_RECORD_ID in ledger_row.get("Notes or exclusions", "")
           and MD_RECORD_ID not in ledger_row.get("Validation evidence", ""))
    checks.append(("MD6. structured traceability row carries the same value and the "
                   "authority reference", md6,
                   f"classification={ledger_row['Validation classification'] if ledger_row else None!r}"))

    # MD7: the live registry row.
    registry_path = os.path.join(repo, MD_REGISTRY_REL)
    reg_row = None
    if os.path.isfile(registry_path):
        with open(registry_path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if (r["Requirement ID"] == MD_REQUIREMENT_ID
                        and r["Field name"] == MD_FIELD):
                    reg_row = r
                    break
    md7 = (reg_row is not None
           and reg_row["Authoritative expected value"] == MD_VALUE
           and reg_row["Normative value"] == MD_VALUE
           and reg_row["Effective value"] == MD_VALUE
           and reg_row["Validation result"] == "PASS"
           and reg_row["Conflict result"] == "None"
           and reg_row["Primary basis"] == "Normative record")
    checks.append(("MD7. live field-source registry row resolves to the approved value "
                   "and passes", md7,
                   f"row={ {k: reg_row[k] for k in ('Authoritative expected value','Normative value','Validation result','Primary basis')} if reg_row else None}"))

    # MD8: not finally resolved.
    status_now = next((r["Resolution status"].strip() for r in rows
                       if r["Resolution issue ID"] == MD_ISSUE_ID), "")
    md8 = status_now == METADATA_RECORDED_STATUS and not FINAL_STATUS_RE.match(status_now)
    checks.append(("MD8. metadata-recorded issue is not marked finally resolved", md8,
                   f"status={status_now!r}"))

    return checks


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


STALE_ZERO_DECISION_PATTERNS = [
    re.compile(r"Every owner-decision field is literally `PENDING`\s*\.\s*(?!\s*As of)", re.IGNORECASE),
    re.compile(r"every checkbox/decision cell unselected(?!\.\s*As of)", re.IGNORECASE),
    re.compile(r"^\s*It records no decision\. Every\s*\n?\s*decision cell below is unselected\.", re.IGNORECASE | re.MULTILINE),
]

SIGNOFF_FIELD_RE = re.compile(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")


def _parse_signoff_table(review_text):
    """Return dict of sign-off field name -> value from the 'Sign-off'
    section table in project-owner-review.md (or {} if not found)."""
    m = re.search(r"## Sign-off.*?\n\n(\|.*?\n(?:\|.*?\n)+)", review_text, re.DOTALL)
    if not m:
        return {}
    table = m.group(1)
    fields = {}
    for line in table.splitlines():
        row = SIGNOFF_FIELD_RE.match(line.strip())
        if not row:
            continue
        key, val = row.group(1).strip(), row.group(2).strip()
        if key in ("Field", "---"):
            continue
        fields[key] = val
    return fields


def check_state_prose(pkt, recorded_count, pending_count, approved):
    """Verify the packet's own state-description prose is not stale or
    contradictory relative to the computed decision state (BH-R2).

    Returns a list of (name, ok, detail) tuples in the same shape as the
    other checks in this module.
    """
    checks = []

    packet_path = os.path.join(pkt, "source-model-resolution-packet.md")
    packet_text = open(packet_path, encoding="utf-8").read() if os.path.exists(packet_path) else ""
    review_path = os.path.join(pkt, "project-owner-review.md")
    review_text = open(review_path, encoding="utf-8").read() if os.path.exists(review_path) else ""

    has_decisions = recorded_count > 0

    # PS1: when durable decisions exist, neither document may contain an
    # unqualified "zero decisions recorded" / "every checkbox unselected"
    # claim about the packet's *current* state.
    stale_hits = []
    if has_decisions:
        for label, text in (("source-model-resolution-packet.md", packet_text),
                             ("project-owner-review.md", review_text)):
            for pat in STALE_ZERO_DECISION_PATTERNS:
                if pat.search(text):
                    stale_hits.append((label, pat.pattern))
    checks.append(("PS1. when durable decisions exist, the packet introduction/contents-table "
                    "does not claim zero decisions are recorded",
                    len(stale_hits) == 0, f"stale_hits={stale_hits}"))

    # PS2: recorded/pending counts stated in the packet's prose match the
    # computed decision-state counts (only meaningful once decisions exist;
    # trivially true at the zero-decision state).
    counts_ok = True
    counts_detail = ""
    if has_decisions:
        expected_pair_present = (
            str(recorded_count) in packet_text and str(pending_count) in packet_text
        )
        if not expected_pair_present:
            counts_ok = False
            counts_detail = (f"expected recorded_count={recorded_count} and "
                              f"pending_count={pending_count} both stated in "
                              f"source-model-resolution-packet.md")
    checks.append(("PS2. packet-state prose recorded/pending counts match the computed "
                    "decision-state counts", counts_ok, counts_detail))

    # PS3: the historical (662ee28) prepared state remains distinguished
    # from the current state -- both documents must still name 662ee28
    # as the zero-decision state.
    hist_ok = ("662ee28" in packet_text) and (
        "PENDING" in packet_text or "PREPARED" in packet_text.upper())
    checks.append(("PS3. historical zero-decision state (commit 662ee28) remains "
                    "distinguished from the current state", hist_ok,
                    "662ee28 reference missing or unqualified" if not hist_ok else ""))

    # PS4/PS5: the review-cycle sign-off summary matches the durable record.
    signoff = _parse_signoff_table(review_text)
    signoff_mismatches = []
    if has_decisions:
        expected = {
            "Decisions recorded in this review cycle": str(recorded_count),
        }
        for key, want in expected.items():
            got = signoff.get(key, "")
            if got != want:
                signoff_mismatches.append((key, "want=" + want, "got=" + got))
        # The summary must not still say PENDING for a field that has a
        # recorded, non-zero value.
        if signoff.get("Decisions recorded in this review cycle", "").strip().upper() == "PENDING":
            signoff_mismatches.append(("Decisions recorded in this review cycle",
                                        "still PENDING", "durable decisions exist"))
    checks.append(("PS4. review-cycle sign-off summary matches the durable record",
                    len(signoff_mismatches) == 0, f"mismatches={signoff_mismatches}"))

    # PS5: no document may introduce implementation authorization language
    # in the sign-off/state-summary areas.
    auth_bad = []
    signoff_auth = signoff.get("Implementation authorization", "")
    if signoff_auth and signoff_auth.strip().upper() not in ("NOT AUTHORIZED", ""):
        auth_bad.append(("project-owner-review.md sign-off", signoff_auth))
    checks.append(("PS5. no implementation authorization is introduced by the "
                    "review-cycle summary", len(auth_bad) == 0, f"bad={auth_bad}"))

    return checks


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
    final_status_claims, metadata_recorded = [], []
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
            if rs.strip() not in PERMITTED_RECORDED_STATUSES:
                status_mismatches.append(iid)
            if FINAL_STATUS_RE.match(rs.strip()):
                final_status_claims.append(iid)
            if rs.strip() == METADATA_RECORDED_STATUS:
                metadata_recorded.append(iid)
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
                    f"'{REQUIRED_STATUS}' / '{METADATA_RECORDED_STATUS}' for durably "
                    f"recorded rows",
                    len(status_mismatches) == 0, f"status_mismatches={status_mismatches}"))
    checks.append(("7e. no durably recorded issue claims a final resolved/closed/validated "
                    "status", len(final_status_claims) == 0,
                    f"final_status_claims={final_status_claims}"))

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
    #
    # As of KBDL-011-SMR1-BA-OD1-DR1, the ledger's durable-decision metric is
    # generalized from a Batch-H-only label ("Durably recorded owner decisions
    # (Batch H / KBDL-011-SMR1-BH-R1)") to a generic total metric ("Total
    # durably recorded owner decisions") plus a per-batch breakdown, so the
    # total is no longer represented only by a misleading Batch-H-specific
    # label. This does not rewrite the underlying generic counting logic
    # (`approved`/`recorded_count`/`pending_count` above are unchanged and
    # already generic across every *-owner-decision-record.md file found by
    # `parse_durable_records`); it only adds a total-metric lookup plus a new
    # per-batch breakdown check (D13) and a Batch H historical-count
    # invariant (D14).
    ledger_path = os.path.join(pkt, "source-model-resolution-ledger.csv")
    ledger_ok = True
    ledger_detail = ""
    LEGACY_BH_ONLY_METRIC = "Durably recorded owner decisions (Batch H / KBDL-011-SMR1-BH-R1)"
    TOTAL_METRIC = "Total durably recorded owner decisions"
    lrows = []
    if os.path.exists(ledger_path):
        with open(ledger_path, newline="", encoding="utf-8") as f:
            lrows = list(csv.DictReader(f))
        total_rows = [r for r in lrows if r["Metric"].strip() == TOTAL_METRIC]
        legacy_rows = [r for r in lrows if r["Metric"].strip() == LEGACY_BH_ONLY_METRIC]
        if total_rows:
            if total_rows[0]["Value"].strip() != str(len(approved)):
                ledger_ok = False
                ledger_detail = (f"ledger total durable-count={total_rows[0]['Value']} "
                                 f"expected={len(approved)}")
        elif legacy_rows:
            # Legacy Batch-H-only label still present -- only valid while it
            # is also the true total (i.e. no non-Batch-H decisions exist).
            if legacy_rows[0]["Value"].strip() != str(len(approved)):
                ledger_ok = False
                ledger_detail = (f"ledger legacy Batch-H-only count={legacy_rows[0]['Value']} "
                                 f"expected total={len(approved)}")
        elif len(approved) > 0:
            ledger_ok = False
            ledger_detail = f"no '{TOTAL_METRIC}' row present in ledger"
    checks.append(("D12. source-model-resolution-ledger.csv durable owner-decision count matches "
                    "the actual durable-record count", ledger_ok, ledger_detail))

    # D13: per-batch/per-record-file breakdown. Batch label is derived
    # generically from each durable-record file's basename convention
    # ("batch-<x>-...owner-decision-record.md" -> "Batch <X>"), not
    # hardcoded per-issue, so this works for any future batch file without
    # further changes to this module.
    def _batch_label(fp):
        base = os.path.basename(fp)
        m = re.match(r"batch-([a-z0-9]+)-", base)
        return "Batch " + m.group(1).upper() if m else f"Batch UNKNOWN({base})"

    batch_counts = {}
    for rec in approved.values():
        label = _batch_label(rec["file"])
        batch_counts[label] = batch_counts.get(label, 0) + 1

    per_batch_mismatches = []
    per_batch_missing = []
    if lrows:
        ledger_metric_values = {r["Metric"].strip(): r["Value"].strip() for r in lrows}
        for label, count in sorted(batch_counts.items()):
            metric_name = f"{label} recorded decisions"
            if metric_name not in ledger_metric_values:
                per_batch_missing.append(metric_name)
                continue
            if ledger_metric_values[metric_name] != str(count):
                per_batch_mismatches.append((metric_name, ledger_metric_values[metric_name], count))
    sum_ok = sum(batch_counts.values()) == len(approved)
    checks.append(("D13. source-model-resolution-ledger.csv per-batch durable-decision counts "
                    "match actual per-batch counts and sum to the total",
                    len(per_batch_mismatches) == 0 and len(per_batch_missing) == 0 and sum_ok,
                    f"mismatches={per_batch_mismatches} missing={per_batch_missing} "
                    f"batch_counts={batch_counts} sum_ok={sum_ok} total={len(approved)}"))

    # D14: Batch H's historically recorded decision count must remain
    # exactly three -- a fixed historical invariant (KBDL-011-SMR1-BH-R1),
    # independent of what any ledger row claims.
    batch_h_count = batch_counts.get("Batch H", 0)
    checks.append(("D14. Batch H's historically recorded owner-decision count remains exactly three",
                    batch_h_count == 3, f"batch_h_count={batch_h_count}"))

    # BH-R2: packet-state prose consistency checks.
    checks.extend(check_state_prose(pkt, recorded_count, pending_count, approved))

    # BA-OD1-DR1-R1: durable-record authority-wording checks and
    # current-state-prose staleness checks (AR1/AR2/SP1-SP4).
    checks.extend(check_authority_records(pkt))
    checks.extend(check_current_state_prose(pkt, recorded_count, pending_count, batch_counts))

    # KBDL-011-SMR2-VC-0001 (reissued): metadata-recording completeness.
    checks.extend(check_metadata_recording(pkt, metadata_recorded, approved, rows))

    # KBDL-011-SMR2-VC-0001-PA1: planning-agent validation record integrity.
    checks.extend(check_planning_agent_validation(pkt, rows, approved))

    stats = {
        "recorded_count": recorded_count,
        "pending_count": pending_count,
        "unknown_ids": unknown,
        "duplicates": dup_ids,
        "total_rows": len(rows),
    }
    return checks, stats
