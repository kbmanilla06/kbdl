#!/usr/bin/env python3
"""KBDL-011-SMR2-FSRG1 roadmap-entry consistency module.

Added by the 2026-07-29 project-owner disposition APPROVE WITH CHANGES on
the proposed `KBDL-011-SMR2-VC-0001` metadata-recording prompt, which
directed that a prerequisite roadmap prompt (`KBDL-011-SMR2-FSRG1`) be
added first and that `KBDL-011-SMR2-VC-0001` stay locked until FSRG1
passes planning-agent validation.

This module validates the *roadmap record* only. It does not validate a
generator, a live registry, or a schema -- none of those exist yet, and
FSRG1 is not authorized by this packet. What it enforces is that the
roadmap entry cannot silently rot into something weaker than what was
approved:

  FR1  the FSRG1 prompt specification exists, is identified, and
       disclaims implementation authorization;
  FR2  it states all six mandatory validation gates;
  FR3  it names all four R13-R16 registries and declares them immutable
       historical evidence;
  FR4  those four registries still verify byte-for-byte against the
       SHA-256 digests recorded in their own round evidence inventories;
  FR5  implementation-unlock-map.md carries the FSRG1 entry and the
       gated KBDL-011-SMR2-VC-0001 entry, both at a permitted LOCKED
       status, with the gate stated;
  FR6  neither document claims FSRG1 or KBDL-011-SMR2-VC-0001 is
       authorized, unlocked, ready, or approved for issue.

`compute()` takes explicit `pkt` and `repo` roots so `fsrg1_roadmap_
fixtures.py` can exercise every check against temporary, deliberately
mutated copies. Nothing in this module ever writes to the repository.
"""
import csv
import hashlib
import os
import re

PROMPT_FILE = "smr2-fsrg1-prompt.md"
MAP_FILE = "implementation-unlock-map.md"
PROMPT_ID = "KBDL-011-SMR2-FSRG1"
DOWNSTREAM_ID = "KBDL-011-SMR2-VC-0001"
REQUIRED_IMPL_STATUS = "NOT AUTHORIZED"

HISTORICAL_ROUNDS = ["r13", "r14", "r15", "r16"]
REGISTRY_REL = "docs/kbdl/evidence/kbdl-011-{r}/artifacts/field-source-registry.csv"
INVENTORY_REL = "docs/kbdl/evidence/kbdl-011-{r}/evidence-inventory.csv"

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

# The six mandatory gates, each with the pattern that proves the
# specification actually states it (not merely names it in a list).
GATE_PATTERNS = {
    "schema": re.compile(r"\*\*Schema gate\.\*\*", re.IGNORECASE),
    "determinism": re.compile(r"\*\*Determinism gate\.\*\*", re.IGNORECASE),
    "drift": re.compile(r"\*\*Drift gate\.\*\*", re.IGNORECASE),
    "path-safety": re.compile(r"\*\*Path-safety gate\.\*\*", re.IGNORECASE),
    "fixture-isolation": re.compile(r"\*\*Fixture-isolation gate\.\*\*", re.IGNORECASE),
    "clean post-publication": re.compile(
        r"\*\*Clean post-publication validation gate\.\*\*", re.IGNORECASE),
}

IMMUTABILITY_RE = re.compile(
    r"immutable historical evidence.*?byte-identical|"
    r"byte-identical.*?never (?:regenerated|re-derived)",
    re.IGNORECASE | re.DOTALL,
)

NO_NORMATIVE_CHANGE_RE = re.compile(r"no normative content changes", re.IGNORECASE)
NO_EFFECTIVE_CHANGE_RE = re.compile(r"no effective metadata changes", re.IGNORECASE)

# The downstream prompt must be stated as gated on FSRG1 *planning-agent*
# validation, and as reissued rather than resumed.
GATE_STATEMENT_RE = re.compile(
    r"passed?\s+planning-agent\s+validation", re.IGNORECASE)
REISSUE_RE = re.compile(r"reissued?\b", re.IGNORECASE)

ALLOWED_STATUSES = {
    "LOCKED — OWNER DECISION REQUIRED",
    "LOCKED — ADDITIONAL EVIDENCE REQUIRED",
    "LOCKED — PLANNING-AGENT VALIDATION REQUIRED",
    "ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL",
}

# FR7 (added by the KBDL-011-SMR2-VC-0001 remediation): a roadmap entry must
# never simultaneously assert that a prompt passed planning-agent validation
# and that the same validation has not occurred / is still required. That exact
# contradiction shipped in the FSRG1 entry — one bullet said
# "PASSED — PLANNING-AGENT VALIDATED" while another said validation "has not
# occurred", with a `Status:` line still demanding it — and no check caught it.
PASSED_VALIDATION_RE = re.compile(
    r"PASSED\s*[—-]\s*PLANNING-AGENT VALIDATED|"
    r"has passed planning-agent validation", re.IGNORECASE)
# "not occurred" style claims. A historical marker rescues the sentence, so a
# preserved account of a past state stays legal; an unmarked current-state
# claim does not.
NOT_VALIDATED_RE = re.compile(
    r"planning-agent validation[^.]{0,80}?(?:has not occurred|has not happened|"
    r"is still pending|remains pending|has not yet occurred)|"
    r"(?:has not|not yet) been planning-agent validated", re.IGNORECASE)
HISTORICAL_MARKER_RE = re.compile(
    r"historical note|at the [^.]{0,60}implementation point|"
    r"it has since occurred|previously read|formerly read", re.IGNORECASE)

# Language that would mean the roadmap entry has been quietly promoted
# out of its LOCKED state without the required planning-agent validation.
#
# These are deliberately narrow. The specification legitimately describes
# what FSRG1 "is authorized to prepare" once issued (§2) -- scoping
# language, not a promotion -- so a bare "authorized" is only a hit when
# it is not immediately qualified by "to prepare". The value of the
# "Implementation authorization status:" field is checked by FR1, which
# compares it exactly, rather than by a lookahead here (a `\s*`-prefixed
# negative lookahead backtracks to zero width and fires on the correct
# value, which is how an earlier draft of this check false-positived).
PREMATURE_AUTHORIZATION_PATTERNS = [
    re.compile(r"(?:FSRG1|KBDL-011-SMR2-VC-0001)[^.\n]{0,80}"
               r"(?:is|are)\s+(?:now\s+)?"
               r"(?:unlocked|approved for issue|ready to issue|"
               r"authorized to issue|authorized for issue)",
               re.IGNORECASE),
    re.compile(r"(?:FSRG1|KBDL-011-SMR2-VC-0001)\s+(?:is|are)\s+(?:now\s+)?"
               r"authorized(?!\s+to\s+prepare)", re.IGNORECASE),
    re.compile(r"may (?:now )?be issued without", re.IGNORECASE),
]


def _read(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def _section(text, heading_substr):
    """Return the text of the first '## ...heading_substr...' section."""
    if not text:
        return ""
    lines = text.splitlines()
    out = []
    capturing = False
    for line in lines:
        if line.startswith("## "):
            if capturing:
                break
            capturing = heading_substr.lower() in line.lower()
            if capturing:
                out.append(line)
            continue
        if capturing:
            out.append(line)
    return "\n".join(out)


def recorded_registry_digest(repo, round_name):
    """Return the SHA-256 digest recorded for this round's field-source
    registry in that round's own evidence-inventory.csv, or None.

    Round inventories do not share a column layout (R13 omits the
    description column the later rounds carry), so the digest is located
    positionally: the row naming the registry path, and within it the one
    cell that is a 64-character lowercase hex digest.
    """
    inv_path = os.path.join(repo, INVENTORY_REL.format(r=round_name))
    rel = REGISTRY_REL.format(r=round_name)
    if not os.path.exists(inv_path):
        return None
    with open(inv_path, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or rel not in row[0]:
                continue
            digests = [c.strip() for c in row if SHA256_RE.match(c.strip())]
            if len(digests) == 1:
                return digests[0]
            return None
    return None


def actual_registry_digest(repo, round_name):
    path = os.path.join(repo, REGISTRY_REL.format(r=round_name))
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def compute(pkt, repo):
    """Run every FSRG1 roadmap check. Returns a list of (name, ok, detail)
    tuples in the same shape used by validate_packet.py's check()."""
    checks = []
    prompt_text = _read(os.path.join(pkt, PROMPT_FILE))
    map_text = _read(os.path.join(pkt, MAP_FILE))

    # FR1: the specification exists, identifies itself, and disclaims
    # implementation authorization.
    fr1_problems = []
    if prompt_text is None:
        fr1_problems.append(f"{PROMPT_FILE} missing")
    else:
        if PROMPT_ID not in prompt_text:
            fr1_problems.append("prompt ID absent")
        m = re.search(r"Implementation authorization status:\s*([^\n]+)", prompt_text)
        if m is None:
            fr1_problems.append("no implementation-authorization line")
        elif m.group(1).strip() != REQUIRED_IMPL_STATUS:
            fr1_problems.append(f"impl status={m.group(1).strip()!r}")
    checks.append((f"FR1. {PROMPT_FILE} exists, identifies {PROMPT_ID}, and states "
                   f"'Implementation authorization status: {REQUIRED_IMPL_STATUS}'",
                   len(fr1_problems) == 0, f"problems={fr1_problems}"))

    # FR2: all six mandatory validation gates are stated.
    missing_gates = [name for name, pat in GATE_PATTERNS.items()
                     if not (prompt_text and pat.search(prompt_text))]
    checks.append(("FR2. the FSRG1 specification states all six mandatory validation gates "
                   "(schema, determinism, drift, path-safety, fixture-isolation, "
                   "clean post-publication)",
                   len(missing_gates) == 0, f"missing={missing_gates}"))

    # FR3: all four historical registries named, declared immutable, and
    # the no-normative/no-effective-change constraints stated.
    fr3_problems = []
    for r in HISTORICAL_ROUNDS:
        if not prompt_text or REGISTRY_REL.format(r=r) not in prompt_text:
            fr3_problems.append(f"{r} registry path not named")
    if not (prompt_text and IMMUTABILITY_RE.search(prompt_text)):
        fr3_problems.append("no immutable/byte-identical preservation statement")
    if not (prompt_text and NO_NORMATIVE_CHANGE_RE.search(prompt_text)):
        fr3_problems.append("no 'no normative content changes' constraint")
    if not (prompt_text and NO_EFFECTIVE_CHANGE_RE.search(prompt_text)):
        fr3_problems.append("no 'no effective metadata changes' constraint")
    checks.append(("FR3. the FSRG1 specification names all four R13-R16 registries and "
                   "declares them immutable historical evidence, with the normative/"
                   "effective-metadata non-change constraints stated",
                   len(fr3_problems) == 0, f"problems={fr3_problems}"))

    # FR4: those four registries still verify against their recorded digests.
    digest_problems = []
    for r in HISTORICAL_ROUNDS:
        recorded = recorded_registry_digest(repo, r)
        actual = actual_registry_digest(repo, r)
        if recorded is None:
            digest_problems.append((r, "no recorded digest"))
        elif actual is None:
            digest_problems.append((r, "registry missing"))
        elif recorded != actual:
            digest_problems.append((r, f"recorded={recorded[:12]} actual={actual[:12]}"))
    checks.append(("FR4. all four R13-R16 field-source registries verify byte-for-byte "
                   "against the SHA-256 digests recorded in their round evidence inventories",
                   len(digest_problems) == 0, f"problems={digest_problems}"))

    # FR5: the unlock map carries both entries, both LOCKED, with the gate
    # and the reissue requirement stated.
    fsrg1_section = _section(map_text, PROMPT_ID)
    downstream_section = _section(map_text, DOWNSTREAM_ID)
    fr5_problems = []
    # An entry may leave LOCKED only once the map records that it passed
    # planning-agent validation — FR7 enforces the consistency of that claim.
    # Extended by KBDL-011-SMR2-VC-0001-PA1: the downstream entry has now
    # itself been validated, so the same rule governs it rather than a blanket
    # "always LOCKED". An unvalidated entry that is unlocked still fails.
    fsrg1_passed = bool(PASSED_VALIDATION_RE.search(fsrg1_section))
    downstream_passed = bool(PASSED_VALIDATION_RE.search(downstream_section))
    passed_by_label = {"FSRG1": fsrg1_passed, "SMR2-VC-0001": downstream_passed}
    for label, section in (("FSRG1", fsrg1_section), ("SMR2-VC-0001", downstream_section)):
        if not section.strip():
            fr5_problems.append(f"{label} section missing from {MAP_FILE}")
            continue
        statuses = re.findall(r"Status:\s*`([^`]+)`", section)
        if not statuses:
            fr5_problems.append(f"{label} section states no Status")
            continue
        must_be_locked = not passed_by_label[label]
        for s in statuses:
            for part in (p.strip() for p in s.split(" / ")):
                if part not in ALLOWED_STATUSES:
                    fr5_problems.append((label, "disallowed status", part))
                elif must_be_locked and not part.startswith("LOCKED"):
                    fr5_problems.append((label, "not LOCKED", part))
    if downstream_section.strip():
        if not GATE_STATEMENT_RE.search(downstream_section):
            fr5_problems.append("SMR2-VC-0001 entry does not state the planning-agent gate")
        if not REISSUE_RE.search(downstream_section):
            fr5_problems.append("SMR2-VC-0001 entry does not state it must be reissued")
    checks.append((f"FR5. {MAP_FILE} carries LOCKED {PROMPT_ID} and {DOWNSTREAM_ID} entries, "
                   "with the planning-agent gate and the reissue requirement stated",
                   len(fr5_problems) == 0, f"problems={fr5_problems}"))

    # FR6: neither document promotes either prompt out of its LOCKED state.
    premature = []
    for label, text in ((PROMPT_FILE, prompt_text), (MAP_FILE, map_text)):
        if not text:
            continue
        for pat in PREMATURE_AUTHORIZATION_PATTERNS:
            m = pat.search(text)
            if m:
                premature.append((label, m.group(0)[:80].replace("\n", " ")))
    checks.append((f"FR6. neither {PROMPT_FILE} nor {MAP_FILE} claims {PROMPT_ID} or "
                   f"{DOWNSTREAM_ID} is authorized, unlocked, ready, or approved for issue",
                   len(premature) == 0, f"hits={premature}"))

    # FR7: no roadmap entry may simultaneously claim a prompt passed
    # planning-agent validation and that the same validation has not occurred.
    contradictions = []
    for label, section in (("FSRG1", fsrg1_section), ("SMR2-VC-0001", downstream_section)):
        if not section.strip():
            continue
        if not PASSED_VALIDATION_RE.search(section):
            continue
        for m in NOT_VALIDATED_RE.finditer(section):
            sentence = _sentence_around(section, m.start())
            if HISTORICAL_MARKER_RE.search(sentence):
                continue
            contradictions.append((label, " ".join(sentence.split())[:120]))
    checks.append(("FR7. no roadmap entry both claims planning-agent validation passed and "
                   "states that the same validation has not occurred",
                   len(contradictions) == 0, f"contradictions={contradictions}"))

    # FR8: a status line must agree with the entry's own validation claim.
    status_conflicts = []
    for label, section in (("FSRG1", fsrg1_section), ("SMR2-VC-0001", downstream_section)):
        for s in re.findall(r"Status:\s*`([^`]+)`", section):
            if passed_by_label[label] and "PLANNING-AGENT VALIDATION REQUIRED" in s:
                status_conflicts.append((label, "validated but still demands validation", s))
            if not passed_by_label[label] and not s.strip().startswith("LOCKED"):
                status_conflicts.append((label, "unlocked without a validation claim", s))
    checks.append(("FR8. a validated entry does not still demand planning-agent validation, "
                   "and an unvalidated entry is not unlocked",
                   len(status_conflicts) == 0, f"conflicts={status_conflicts}"))

    return checks


def _sentence_around(text, pos):
    """Return the sentence-ish chunk containing `pos`.

    Bounded by blank lines and list-item boundaries so a historical marker in a
    neighbouring bullet cannot rescue a contradiction in this one.
    """
    start = max(text.rfind("\n- ", 0, pos), text.rfind("\n\n", 0, pos), 0)
    nxt = [x for x in (text.find("\n- ", pos), text.find("\n\n", pos)) if x != -1]
    end = min(nxt) if nxt else len(text)
    return text[start:end]
