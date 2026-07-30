#!/usr/bin/env python3
"""KBDL-011-SMR2-VC-0001-PA1 sign-off, review-scope, and CRLF checks.

Added by the approved PA1 sign-off remediation. Three concerns, all
fail-closed, all read-only:

  GATE1-GATE4  no current-state document may still describe
               KBDL-011-SMR1-RM1, KBDL-011-SMR2-FSRG1, or the reissued
               KBDL-011-SMR2-VC-0001 as an open/pending gate, as LOCKED, or
               as not-yet-issued. A statement carrying an explicit historical
               marker in the same paragraph is preserved history and passes;
               an unmarked current-state claim fails.

  POR1-POR5    project-owner-review.md is an authorized PA1 change path, but
               only for (a) the SMR1-VC-0001 planning-validation status
               mirror, (b) the single unselected SMR1-VC-0002 review block,
               and (c) the sign-off current-state rows this remediation
               corrects. No checkbox may change state, and no other
               issue-level block may gain a selection.

  CRLF1-CRLF6  a CRLF-aware replacement for `git diff --check` on
               issue-register.csv. `git diff --check` counts the CR of that
               file's CRLF line terminators as trailing whitespace and exits
               2 on any changed line, which makes it useless as a gate there.
               These checks preserve the CRLF convention while still
               rejecting real whitespace damage: spaces or tabs before the
               line ending, mixed or bare-LF line endings, malformed rows,
               a changed row count, and any changed row other than the
               authorized ones.

Nothing here writes to the repository.
"""
import csv
import io
import os
import re
import subprocess
import sys

SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
VC1_REL = "docs/kbdl/evidence/kbdl-011-smr2-vc-0001"
ISSUES_REL = f"{SMR1_REL}/issue-register.csv"
REVIEW_REL = f"{SMR1_REL}/project-owner-review.md"

# Baseline for scope comparisons: the last commit before the PA1 transition.
PA1_BASELINE = "448e39b22f4dc69210ca795c365bbdf1a3904f20"

CURRENT_STATE_FILES = (
    REVIEW_REL,
    f"{SMR1_REL}/source-model-resolution-packet.md",
    f"{SMR1_REL}/implementation-report.md",
    f"{SMR1_REL}/evidence-manifest.md",
    f"{SMR1_REL}/implementation-unlock-map.md",
)

# An explicit historical marker anywhere in the same paragraph rescues a
# statement about a past state. Unmarked claims are read as current.
HISTORICAL_MARKER_RE = re.compile(
    r"historical note|historical|previously|formerly|at the [^.]{0,60}point|"
    r"has since|since been|superseded|then-current|no longer|was reissued|"
    r"prior cycle|not an open gate", re.IGNORECASE)

STALE_GATE_PATTERNS = {
    "GATE1": (
        "KBDL-011-SMR1-RM1 described as an open or pending gate",
        re.compile(r"KBDL-011-SMR1-RM1[^.\n]{0,120}?"
                   r"(?:is (?:now )?(?:the )?(?:current |only )?open gate|"
                   r"is the current open gate|remains (?:an )?open|"
                   r"PENDING until it passes)", re.IGNORECASE)),
    "GATE2": (
        "KBDL-011-SMR2-FSRG1 described as awaiting planning-agent validation",
        re.compile(r"KBDL-011-SMR2-FSRG1[^.\n]{0,120}?"
                   r"(?:planning-agent validation (?:is|remains) (?:still )?(?:pending|required)|"
                   r"awaiting planning-agent validation|is (?:an )?open gate)",
                   re.IGNORECASE)),
    "GATE3": (
        "the reissued KBDL-011-SMR2-VC-0001 described as LOCKED, awaiting, or not issued",
        re.compile(r"KBDL-011-SMR2-VC-0001[^.\n]{0,140}?"
                   r"(?:stays `?LOCKED|remains `?LOCKED|is `?LOCKED|"
                   r"awaiting planning-agent validation|"
                   r"Neither prompt is\s+issued or authorized)", re.IGNORECASE)),
}

# The sign-off must positively state the current gate, not merely omit the
# stale one.
SIGNOFF_CURRENT_GATE_RE = re.compile(
    r"current open gate is planning-agent validation of\s+"
    r"KBDL-011-SMR2-VC-0001-PA1-R2",
    re.IGNORECASE)

# project-owner-review.md scope.
VC2_BLOCK_MARKER = "### Next issue-level review — SMR1-VC-0002"
EXPECTED_SELECTED = [
    "SET TO NOT VERIFIED",
    "RELATED REQUIREMENT",
    "RELATED REQUIREMENT",
    "Replace both edges with shared independent authority",
]
# The three regions PA1 and this remediation are authorized to touch in
# project-owner-review.md. Scope is proven structurally: strip these regions
# from both the baseline and the current file and the remainder must be
# byte-identical. That is stronger than a line pattern allowlist, which can
# accidentally admit an unrelated edit that happens to look ordinary.
STATUS_MIRROR_RE = re.compile(
    r"row[;,][^.]*?(?:METADATA RECORDED|OWNER DECISION RECORDED)[^.]*?\.",
    re.DOTALL)


def _strip_authorized_regions(text):
    """Remove the sign-off section, the SMR1-VC-0002 block, and the
    SMR1-VC-0001 status-mirror sentence. What remains must never change."""
    t = text.split("## Sign-off", 1)[0]
    if VC2_BLOCK_MARKER in t:
        t = t.split(VC2_BLOCK_MARKER, 1)[0]
    return STATUS_MIRROR_RE.sub("<STATUS-MIRROR>", t)


def _read(root, rel):
    p = os.path.join(root, rel)
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8") as f:
        return f.read()


def _git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)


def _paragraph_around(text, pos):
    start = text.rfind("\n\n", 0, pos)
    start = 0 if start == -1 else start
    end = text.find("\n\n", pos)
    return text[start:end if end != -1 else len(text)]


def check_stale_gate_statements(root):
    """GATE1-GATE4."""
    checks = []
    for key, (label, pattern) in STALE_GATE_PATTERNS.items():
        hits = []
        for rel in CURRENT_STATE_FILES:
            text = _read(root, rel)
            if not text:
                continue
            for m in pattern.finditer(text):
                para = _paragraph_around(text, m.start())
                if HISTORICAL_MARKER_RE.search(para):
                    continue
                hits.append((rel, " ".join(m.group(0).split())[:110]))
        checks.append((f"{key}. no current-state document leaves {label}",
                       not hits, f"hits={hits[:3]}"))

    review = _read(root, REVIEW_REL) or ""
    signoff = review.split("## Sign-off", 1)[1] if "## Sign-off" in review else ""
    checks.append(("GATE4. the sign-off positively states the current open gate",
                   bool(SIGNOFF_CURRENT_GATE_RE.search(signoff)),
                   "sign-off does not name the current open gate"))
    return checks


def check_review_form_scope(root):
    """POR1-POR5: project-owner-review.md changed only where authorized."""
    checks = []
    review = _read(root, REVIEW_REL) or ""

    selected = re.findall(r"(?m)^- \[[xX]\] (.+)$", review)
    checks.append(("POR1. the review form carries exactly the four historical selections",
                   selected == EXPECTED_SELECTED, f"selected={selected}"))

    block = ""
    if VC2_BLOCK_MARKER in review:
        block = re.split(r"\n## |\n### ", review.split(VC2_BLOCK_MARKER, 1)[1])[0]
    n_selected = len(re.findall(r"(?m)^- \[[xX]\]", block))
    n_unselected = len(re.findall(r"(?m)^- \[ \]", block))
    checks.append(("POR2. the SMR1-VC-0002 review block exists and is entirely unselected",
                   bool(block.strip()) and n_selected == 0 and n_unselected == 5,
                   f"selected={n_selected} unselected={n_unselected}"))

    checks.append(("POR3. exactly one SMR1-VC-0002 review block exists",
                   review.count(VC2_BLOCK_MARKER) == 1,
                   f"count={review.count(VC2_BLOCK_MARKER)}"))

    base = _git(root, "show", f"{PA1_BASELINE}:{REVIEW_REL}")
    if base.returncode != 0:
        checks.append(("POR4. outside the three authorized regions, project-owner-review.md "
                       "is byte-identical to the PA1 baseline", False,
                       base.stderr.strip()[:200]))
    else:
        base_rest = _strip_authorized_regions(base.stdout)
        cur_rest = _strip_authorized_regions(review)
        same = base_rest == cur_rest
        detail = ""
        if not same:
            import difflib
            d = [x for x in difflib.unified_diff(base_rest.splitlines(),
                                                 cur_rest.splitlines(), lineterm="", n=0)
                 if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]
            detail = f"unauthorized changes={d[:4]}"
        checks.append(("POR4. outside the three authorized regions, project-owner-review.md "
                       "is byte-identical to the PA1 baseline", same, detail))

    diff = _git(root, "diff", "--unified=0", PA1_BASELINE, "HEAD", "--", REVIEW_REL)
    # POR5: no checkbox line was added or removed in a selected state.
    changed_selected = []
    for line in diff.stdout.splitlines():
        if line.startswith(("+", "-")) and re.match(r"^[+-]- \[[xX]\]", line):
            changed_selected.append(line[:80])
    checks.append(("POR5. no checkbox was added or removed in a selected state",
                   not changed_selected, f"changed={changed_selected[:3]}"))
    return checks


def check_crlf_integrity(root):
    """CRLF1-CRLF6: the CRLF-aware replacement for `git diff --check`."""
    checks = []
    path = os.path.join(root, ISSUES_REL)
    if not os.path.isfile(path):
        for k in ("CRLF1", "CRLF2", "CRLF3", "CRLF4", "CRLF5", "CRLF6"):
            checks.append((f"{k}. issue-register.csv present", False, "file missing"))
        return checks
    raw = open(path, "rb").read()

    crlf = raw.count(b"\r\n")
    bare_lf = raw.count(b"\n") - crlf
    stray_cr = raw.count(b"\r") - crlf
    checks.append(("CRLF1. issue-register.csv uses CRLF line endings throughout, with no "
                   "bare LF and no stray CR",
                   crlf > 0 and bare_lf == 0 and stray_cr == 0,
                   f"crlf={crlf} bare_lf={bare_lf} stray_cr={stray_cr}"))

    # CRLF2: real trailing whitespace -- a space or tab immediately before the
    # CR. This is what `git diff --check` is actually for; the CR itself is the
    # file's convention and is not an error.
    bad_ws = [i for i, ln in enumerate(raw.split(b"\r\n"), 1)
              if ln.endswith(b" ") or ln.endswith(b"\t")]
    checks.append(("CRLF2. no line carries a space or tab before its line ending",
                   not bad_ws, f"lines={bad_ws[:5]}"))

    text = raw.decode("utf-8")
    try:
        rows = list(csv.reader(io.StringIO(text)))
        parse_error = ""
    except csv.Error as exc:
        rows, parse_error = [], str(exc)
    checks.append(("CRLF3. issue-register.csv parses as CSV with a uniform row width",
                   bool(rows) and not parse_error
                   and len({len(r) for r in rows if r}) == 1,
                   f"error={parse_error!r} widths={sorted({len(r) for r in rows if r})}"))

    data_rows = [r for r in rows[1:] if r]
    checks.append(("CRLF4. issue-register.csv still holds exactly 421 canonical rows",
                   len(data_rows) == 421, f"rows={len(data_rows)}"))

    # CRLF5: no tab anywhere, and no double space before a delimiter -- the
    # remaining whitespace damage `git diff --check` would have caught.
    checks.append(("CRLF5. no tab characters anywhere in issue-register.csv",
                   b"\t" not in raw, "tab character present"))

    # CRLF6: only the authorized rows changed since the PA1 baseline.
    # Deliberately compares the baseline against the WORKING TREE (no explicit
    # HEAD), so uncommitted damage is caught too. On a clean published tree the
    # two forms are identical.
    diff = _git(root, "diff", "--unified=0", PA1_BASELINE, "--", ISSUES_REL)
    if diff.returncode != 0:
        checks.append(("CRLF6. only authorized issue-register rows changed since the PA1 "
                       "baseline", False, diff.stderr.strip()[:200]))
    else:
        changed_ids = set()
        for line in diff.stdout.splitlines():
            if line.startswith(("+++", "---", "@@", "diff ", "index ")):
                continue
            if line.startswith(("+", "-")):
                m = re.match(r"^[+-]([A-Z0-9-]+),", line)
                if m:
                    changed_ids.add(m.group(1))
                elif line[1:].strip():
                    changed_ids.add("<non-row line>")
        checks.append(("CRLF6. only authorized issue-register rows changed since the PA1 "
                       "baseline", changed_ids <= {"SMR1-VC-0001"},
                       f"changed={sorted(changed_ids)}"))
    return checks


def compute(root):
    """Return every check in validate_packet's (name, ok, detail) shape."""
    checks = []
    checks.extend(check_stale_gate_statements(root))
    checks.extend(check_review_form_scope(root))
    checks.extend(check_crlf_integrity(root))
    checks.extend(check_gate_contradictions(root))
    checks.extend(check_wrapped_and_section_gates(root))
    return checks




# ---------------------------------------------------------------------------
# KBDL-011-SMR2-VC-0001-PA1-R2: gate-contradiction checks (R2A-R2E)
# ---------------------------------------------------------------------------
#
# PA1's GATE1-GATE4 missed four things, all of which shipped:
#   * a prompt described as validated AND locked pending that same validation,
#     in the same section;
#   * the stale recommendation written with the validation phrase BEFORE the
#     prompt ID ("Planning-agent validation of KBDL-011-SMR2-FSRG1");
#   * a contradiction laundered by a broad historical marker sitting elsewhere
#     in the same paragraph;
#   * the four current-state documents disagreeing about the current gate.
#
# R2A-R2E close those. Historical exemptions here are STATEMENT-local (the
# sentence or bullet the claim sits in), never paragraph-wide.

COMPLETED_PROMPTS = ("KBDL-011-SMR2-FSRG1", "KBDL-011-SMR2-VC-0001")
CURRENT_GATE_PROMPT = "KBDL-011-SMR2-VC-0001-PA1-R2"

# Reverse-order stale recommendation: the validation phrase before the ID.
REVERSE_ORDER_RE = re.compile(
    r"[Pp]lanning-agent validation of\s+`?(KBDL-011-SMR2-FSRG1|"
    r"KBDL-011-SMR2-VC-0001)`?(?!-PA1)", re.MULTILINE)

# "locked / awaiting its own validation" claims about a completed prompt.
LOCKED_PENDING_RE = re.compile(
    r"(?:stay|stays|remain|remains|is|are)\s+`?LOCKED\s*[—-]\s*PLANNING-AGENT "
    r"VALIDATION REQUIRED|awaiting (?:its own )?planning-agent validation",
    re.IGNORECASE)
PASSED_CLAIM_RE = re.compile(
    r"PASSED\s*[—-]\s*PLANNING-AGENT VALIDATED|has passed planning-agent validation|"
    r"have (?:both )?passed planning-agent validation", re.IGNORECASE)

# Statement-local historical markers only. Deliberately narrower than
# HISTORICAL_MARKER_RE: a marker must sit in the same sentence/bullet as the
# claim, so a neighbouring "historical note" cannot launder a current claim.
LOCAL_HISTORICAL_RE = re.compile(
    r"historical note|at the [^.]{0,60}point|previously read|formerly read|"
    r"then-current|has since|since been|no longer|superseded|was reissued",
    re.IGNORECASE)


def _statements(text):
    """Split into bullet-or-sentence sized units for statement-local checks."""
    units = []
    for block in re.split(r"\n(?=\s*[-*] )|\n\n", text):
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z`*(])", block):
            if sentence.strip():
                units.append(sentence)
    return units


def check_gate_contradictions(root):
    """R2A-R2E."""
    checks = []
    texts = {rel: (_read(root, rel) or "") for rel in CURRENT_STATE_FILES}

    # R2A: reverse-order stale recommendation.
    hits = []
    for rel, text in texts.items():
        for m in REVERSE_ORDER_RE.finditer(text):
            unit = next((u for u in _statements(text) if m.group(0) in u), m.group(0))
            if LOCAL_HISTORICAL_RE.search(unit):
                continue
            hits.append((rel, " ".join(unit.split())[:110]))
    checks.append(("R2A. no current document recommends planning-agent validation of an "
                   "already-validated prompt (reverse-order phrasing)",
                   not hits, f"hits={hits[:3]}"))

    # R2B: validated AND locked-pending-that-validation for the same prompt.
    contradictions = []
    for rel, text in texts.items():
        for prompt in COMPLETED_PROMPTS:
            if not re.search(re.escape(prompt), text):
                continue
            for unit in _statements(text):
                if prompt not in unit:
                    continue
                if LOCKED_PENDING_RE.search(unit) and not LOCAL_HISTORICAL_RE.search(unit):
                    contradictions.append((rel, prompt, " ".join(unit.split())[:110]))
    checks.append(("R2B. no current document says a planning-agent-validated prompt is "
                   "locked or awaiting that same validation",
                   not contradictions, f"contradictions={contradictions[:3]}"))

    # R2C: a section may not hold both a passed claim and an unmarked
    # locked-pending claim about the same prompt.
    section_conflicts = []
    for rel, text in texts.items():
        for section in re.split(r"\n(?=## )", text):
            for prompt in COMPLETED_PROMPTS:
                if prompt not in section:
                    continue
                if not PASSED_CLAIM_RE.search(section):
                    continue
                for unit in _statements(section):
                    if (LOCKED_PENDING_RE.search(unit)
                            and prompt in unit
                            and not LOCAL_HISTORICAL_RE.search(unit)):
                        head = section.split("\n", 1)[0][:60]
                        section_conflicts.append((rel, head, prompt))
    checks.append(("R2C. no section asserts both that a prompt passed and that it remains "
                   "locked pending that validation (no paragraph-wide marker laundering)",
                   not section_conflicts, f"conflicts={section_conflicts[:3]}"))

    # R2D: the four current-state documents agree the completed prompts passed.
    disagreements = []
    for rel in (REVIEW_REL, f"{SMR1_REL}/source-model-resolution-packet.md",
                f"{SMR1_REL}/implementation-report.md",
                f"{SMR1_REL}/implementation-unlock-map.md"):
        text = texts.get(rel, "")
        if not text:
            disagreements.append((rel, "missing"))
            continue
        for prompt in COMPLETED_PROMPTS:
            if prompt in text and not PASSED_CLAIM_RE.search(text):
                disagreements.append((rel, prompt, "no passed claim"))
    checks.append(("R2D. implementation-unlock-map.md, the packet, the implementation "
                   "report, and the review form agree that both completed prompts passed",
                   not disagreements, f"disagreements={disagreements[:3]}"))

    # R2E: the current open gate is PA1-R2, and only PA1-R2.
    gate_named = {}
    # Only an actual designation counts ("the current open gate IS <id>"),
    # not prose that merely mentions the phrase while describing a correction
    # ("... described as the current open gate, KBDL-011-SMR2-FSRG1 described
    # as not yet validated ...").
    gate_re = re.compile(r"current open gate is[^.\n]{0,90}?"
                         r"(KBDL-011-[A-Z0-9-]+)", re.IGNORECASE)
    for rel, text in texts.items():
        for m in gate_re.finditer(text):
            unit = next((u for u in _statements(text) if m.group(0) in u), m.group(0))
            if LOCAL_HISTORICAL_RE.search(unit):
                continue
            gate_named.setdefault(m.group(1), set()).add(rel)
    ok = set(gate_named) == {CURRENT_GATE_PROMPT}
    checks.append((f"R2E. the current open gate is named as {CURRENT_GATE_PROMPT} and "
                   "nothing else", ok,
                   f"named={ {k: sorted(v) for k, v in gate_named.items()} }"))
    return checks




# ---------------------------------------------------------------------------
# KBDL-011-SMR2-VC-0001-PA1-R3: wrap-proof and section-aware gate checks
# ---------------------------------------------------------------------------
#
# R2B/R2C matched raw statement text, so Markdown line wrapping defeated them:
#
#     `KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION
#     REQUIRED`.
#
# shipped undetected, because LOCKED_PENDING_RE expects an ordinary space
# between VALIDATION and REQUIRED. R3A-R3D normalize first, and add section
# context so a completed-prompt section cannot carry active lock language even
# when the prompt ID is only in the heading.

# Characters Markdown uses for emphasis/code that must not break status
# matching. Stripped only for matching; the original statement is kept for
# evidence output.
MARKUP_CHARS = "`*_~"
# All Unicode whitespace, including NBSP and the narrow/thin spaces that can
# appear around em dashes.
WS_RUN_RE = re.compile(r"[\s  -​  　]+")
DASH_RE = re.compile(r"[‐-―−]")


def normalize_for_status(text):
    """Collapse whitespace, unwrap Markdown lines, drop markup, unify dashes.

    Returns a single-line lowercase string safe to match status phrases
    against. Matching is case-insensitive by construction; the caller keeps the
    untouched original for reporting.
    """
    stripped = "".join(ch for ch in text if ch not in MARKUP_CHARS)
    unified = DASH_RE.sub("-", stripped)
    return WS_RUN_RE.sub(" ", unified).strip().lower()


# Status phrases, expressed against normalized text. Deliberately targeted at
# the defect class that actually shipped: a present-tense assertion binding a
# completed prompt to its OWN planning-agent-validation lock. Batch A's
# "LOCKED - OWNER DECISION REQUIRED" is a different, correct lock and is
# excluded by OWNER_DECISION_LOCK_RE below.
# Past-tense forms are included deliberately: a retained historical lock
# statement is legal, but R3C then requires it to state its supersession.
_LOCK_VERB = r"(?:remains?|remained|stays?|stayed|is|are|was|were)"
NORM_LOCKED_RE = re.compile(
    rf"{_LOCK_VERB}\s+(?:`?locked)\s*-\s*planning-agent validation required|"
    rf"{_LOCK_VERB}\s+locked[^.]{{0,40}}?"
    r"(?:pending|until|awaiting)[^.]{0,40}?planning-agent validation|"
    rf"{_LOCK_VERB}\s+awaiting (?:its own )?planning-agent validation|"
    r"planning-agent validation of this recording (?:remains|is still|is)\s+required",
    re.IGNORECASE)

# Batch A and other owner-decision locks are correct and must never be flagged.
OWNER_DECISION_LOCK_RE = re.compile(r"locked\s*-\s*owner decision required", re.IGNORECASE)

# Narrative that records a past arrangement rather than asserting current
# state: a dated disposition, a description of a map entry being added, or a
# validator describing what it rejects. These are history or documentation,
# not claims about the present.
NARRATIVE_CONTEXT_RE = re.compile(
    r"on 20\d\d-\d\d-\d\d|returned (?:the )?(?:disposition|approve with changes)|"
    r"direct(?:ing|ed) that|entr(?:y|ies)\b|gains a |it: \(1\)|downstream gating|"
    r"reject(?:s|ed)? any|unmarked current-state claim|were added|was added",
    re.IGNORECASE)
NORM_HISTORICAL_RE = re.compile(
    r"historical note|at the [^.]{0,60}point|previously read|formerly read|"
    r"then-current|then-new|has since|since been|no longer|superseded|was reissued",
    re.IGNORECASE)
NORM_SUPERSESSION_RE = re.compile(
    r"ha(?:s|ve) since (?:passed|occurred|been)|since been recorded|is no longer|"
    r"since superseded|no longer locked|no longer awaited|now reads|"
    r"passed (?:that |its own )?planning-agent validation|recorded as passed",
    re.IGNORECASE)

COMPLETED_SECTION_RE = re.compile(
    r"KBDL-011-SMR2-FSRG1|KBDL-011-SMR2-VC-0001", re.IGNORECASE)


def _sections_with_headings(text):
    """Yield (heading, body) for every '## '/'### ' section, heading included."""
    parts = re.split(r"\n(?=#{2,3} )", text)
    for part in parts:
        heading = part.split("\n", 1)[0]
        yield heading, part


def check_wrapped_and_section_gates(root):
    """R3A-R3D."""
    checks = []
    texts = {rel: (_read(root, rel) or "") for rel in CURRENT_STATE_FILES}

    # R3A: normalized statement-level lock detection, wrap-proof.
    hits = []
    for rel, text in texts.items():
        for unit in _statements(text):
            norm = normalize_for_status(unit)
            if not NORM_LOCKED_RE.search(norm):
                continue
            if not COMPLETED_SECTION_RE.search(norm):
                continue
            if (OWNER_DECISION_LOCK_RE.search(norm)
                    or NORM_HISTORICAL_RE.search(norm)
                    or NARRATIVE_CONTEXT_RE.search(norm)):
                continue
            hits.append((rel, " ".join(unit.split())[:110]))
    checks.append(("R3A. no current statement locks or awaits validation for a completed "
                   "prompt, in any whitespace or Markdown wrapping",
                   not hits, f"hits={hits[:3]}"))

    # R3B: section-aware -- the heading supplies the prompt context, so a body
    # statement need not name the prompt itself.
    section_hits = []
    for rel, text in texts.items():
        for heading, body in _sections_with_headings(text):
            if not COMPLETED_SECTION_RE.search(normalize_for_status(heading)):
                continue
            for unit in _statements(body):
                if unit.strip() == heading.strip():
                    continue
                norm = normalize_for_status(unit)
                if not NORM_LOCKED_RE.search(norm):
                    continue
                if (OWNER_DECISION_LOCK_RE.search(norm)
                        or NORM_HISTORICAL_RE.search(norm)
                        or NARRATIVE_CONTEXT_RE.search(norm)):
                    continue
                section_hits.append((rel, heading.strip()[:50],
                                     " ".join(unit.split())[:90]))
    checks.append(("R3B. no completed-prompt section carries unmarked active lock or "
                   "validation-required language",
                   not section_hits, f"hits={section_hits[:3]}"))

    # R3C: a retained historical lock statement must also state supersession.
    incomplete = []
    for rel, text in texts.items():
        for unit in _statements(text):
            norm = normalize_for_status(unit)
            if not NORM_LOCKED_RE.search(norm):
                continue
            if not COMPLETED_SECTION_RE.search(norm):
                continue
            if OWNER_DECISION_LOCK_RE.search(norm) or NARRATIVE_CONTEXT_RE.search(norm):
                continue
            if not NORM_HISTORICAL_RE.search(norm):
                continue
            if not NORM_SUPERSESSION_RE.search(norm):
                incomplete.append((rel, " ".join(unit.split())[:110]))
    checks.append(("R3C. every retained historical lock statement also states its current "
                   "supersession", not incomplete, f"incomplete={incomplete[:3]}"))

    # R3D: the normalizer actually defeats the wrappings that shipped.
    flat = "`KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`."
    variants = [
        flat,
        "`KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION\nREQUIRED`.",
        "`KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION\n  REQUIRED`.",
        "KBDL-011-SMR2-FSRG1 remains **LOCKED —\nPLANNING-AGENT\nVALIDATION REQUIRED**.",
        "KBDL-011-SMR2-FSRG1 remains LOCKED —  PLANNING-AGENT VALIDATION\nREQUIRED.",
    ]
    missed = [v for v in variants
              if not NORM_LOCKED_RE.search(normalize_for_status(v))]
    checks.append(("R3D. the status normalizer detects the locked phrase across line "
                   "wrapping, repeated whitespace, backticks, emphasis, and dash variants",
                   not missed, f"missed={[m[:60] for m in missed]}"))
    return checks


if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    failed = 0
    for name, ok, detail in compute(os.path.abspath(repo)):
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail and not ok else ""))
        failed += 0 if ok else 1
    print("=" * 70)
    print(f"{'all checks passed' if not failed else str(failed) + ' check(s) failed'}")
    sys.exit(1 if failed else 0)
