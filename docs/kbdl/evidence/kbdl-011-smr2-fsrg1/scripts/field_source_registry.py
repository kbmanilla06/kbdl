#!/usr/bin/env python3
"""KBDL-011-SMR2-FSRG1 — live current-state field-source registry generator.

Derives the current field source model from current repository sources and
writes exactly one artifact:

    docs/kbdl/evidence/kbdl-011-smr2-fsrg1/artifacts/field-source-registry.csv

Authorized by the implementation prompt KBDL-011-SMR2-FSRG1, whose approved
roadmap specification is `smr2-fsrg1-prompt.md` in the SMR1 packet.

WHAT THIS IS NOT
----------------
The generated registry is a *derived, non-authoritative description* of the
current source model. It is not authority, not a normative source, not
validation evidence, not an owner-decision record, and not implementation
authorization. It never feeds back into itself: no value is read from a
previously generated live registry, and the historical R13-R16 registries are
never read as authoritative input for current values.

SOURCES (all read-only)
-----------------------
  * normative module files under docs/kbdl/
  * docs/kbdl/traceability-metadata.csv          (candidate values only)
  * docs/kbdl/traceability-matrix.md             (readable traceability groups)
  * docs/kbdl/decision-register.md               (decision status)
  * docs/kbdl/evidence/kbdl-011-authority-recovery/  (AR2 confirmations)
  * git object existence, for evidence values citing a commit SHA

DETERMINISM
-----------
Output bytes are a pure function of repository content. Row order is fixed by
an explicit sort key (Requirement ID, then declared field order); column order
is the declared schema order. No timestamp, hostname, username, absolute path,
process ID, random value, or locale-dependent formatting is emitted. The file
is written UTF-8 with '\\n' line endings via Python's csv module, atomically.

The schema contract is declared in `field-source-registry-schema.md`
(schema version 1) and mirrored by SCHEMA_VERSION/COLUMNS/FIELD_SPEC below.

USAGE
-----
    python3 .../field_source_registry.py --repo-root .
    python3 .../field_source_registry.py --repo-root . --check

`--check` regenerates into isolated temporary storage and compares the bytes
with the committed artifact. It never writes to the repository.
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

SCHEMA_VERSION = 1

PACKAGE_REL = "docs/kbdl/evidence/kbdl-011-smr2-fsrg1"
ARTIFACT_REL = f"{PACKAGE_REL}/artifacts/field-source-registry.csv"

COLUMNS = [
    "Requirement ID",
    "Field name",
    "Ownership class",
    "Primary basis",
    "Derivation rule",
    "Authoritative expected value",
    "Normative value",
    "Governance resolution",
    "Ledger value",
    "Readable-group value",
    "Readable-group classification",
    "Effective value",
    "Precedence result",
    "Conflict result",
    "Validation result",
]

# The declared field-name domain and its per-field ownership/derivation
# contract. Declared here and in field-source-registry-schema.md; deliberately
# NOT read from the historical R16 `source-rules.csv`, so that the live schema
# is independently versioned rather than inheriting a point-in-time artifact.
FIELD_SPEC = [
    ("Requirement ID", "A — Normative-owned", "Normative requirement record",
     "Parse the ID from the normative record"),
    ("Blueprint section", "C — Traceability-owned administrative", "Readable traceability group",
     "Parse exact group heading or explicit per-ID mapping"),
    ("Roadmap prompt", "C — Traceability-owned administrative", "Approved roadmap and module ownership",
     "Derive base prompt from module/file and validate any remediation annotation"),
    ("Specification location", "A — Normative-owned", "Containing normative Markdown section",
     "Derive file and containing heading anchor around the requirement record"),
    ("Lifecycle status", "A — Normative-owned", "Normative requirement record",
     "Parse explicit lifecycle and compare every lower source"),
    ("Provenance", "A — Normative-owned", "Normative requirement record",
     "Parse explicit provenance and compare every lower source"),
    ("Validation classification", "A — Normative-owned", "Normative requirement record",
     "Parse explicit validation status and compare every lower source"),
    ("Verified scope", "D — Evidence-owned", "Executed evidence and stated scope",
     "Require evidence-compatible scope"),
    ("Not-verified scope", "D — Evidence-owned", "Unexecuted or excluded scope",
     "Require honest unexecuted scope"),
    ("Authority", "B — Governance-owned",
     "AR2 confirmation approved decision standard or Approved requirement",
     "Resolve every component and graph edge"),
    ("Validation method", "D — Evidence-owned",
     "Normative method or independently approved evidence-method registry",
     "Compare method to evidence classification without ledger self-proof"),
    ("Validation evidence", "D — Evidence-owned",
     "Existing evidence source or honest Not verified record",
     "Resolve paths and prevent unsupported execution claims"),
    ("Known limitation", "D — Evidence-owned", "Actual excluded or unverified scope",
     "Require consistency with validation scope"),
    ("Packet or tracking destination", "C — Traceability-owned administrative",
     "Exact packet or tracking section",
     "Resolve file section item owner and readiness class"),
    ("Pending dependencies", "C — Traceability-owned administrative",
     "Normative record packet or deferred tracking",
     "Resolve and classify dependency source"),
    ("Related decision", "B — Governance-owned", "Approved decision register",
     "Resolve every cited decision and status"),
    ("Notes or exclusions", "C — Traceability-owned administrative",
     "Higher-priority exclusion or bounded administrative note",
     "Reject unsupported promotion or completion claims"),
]

FIELD_NAMES = [name for name, _, _, _ in FIELD_SPEC]
FIELD_ORDER = {name: i for i, name in enumerate(FIELD_NAMES)}
OWNERSHIP = {name: cls for name, cls, _, _ in FIELD_SPEC}
DERIVATION = {name: rule for name, _, _, rule in FIELD_SPEC}

MODULES = "GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL"
RID_RX = rf"KBDL-(?:{MODULES})-\d{{3}}[a-z]?"

MODULE_FILES = [
    "governance.md", "principles.md", "foundations/README.md", "themes/README.md",
    "motion/README.md", "responsive.md", "accessibility.md", "components-core.md",
    "components-system.md", "profiles.md", "customization.md", "validation.md",
]

GROUP_LABELS = {
    "Blueprint section": "Blueprint section",
    "Roadmap prompt": "Roadmap prompt",
    "Specification location": "Specification location",
    "Lifecycle status": "Lifecycle status",
    "Provenance": "Provenance",
    "Validation classification": r"Validation status(?: \(per-ID\))?",
    "Authority": "Authority",
    "Validation method": r"Validation method(?: / evidence)?",
    "Validation evidence": "Validation evidence",
    "Known limitation": "Known limitation",
    "Packet or tracking destination": r"Packet destination(?: \(per-ID\))?",
    "Pending dependencies": r"Pending dependencies(?: \(per-ID\))?",
    "Related decision": "Related decision",
    "Notes or exclusions": "Notes",
}

ROADMAP_BY_MODULE = {
    "GOV": "KBDL-001", "PRN": "KBDL-002", "FND": "KBDL-003", "THM": "KBDL-004",
    "MOT": "KBDL-005", "RSP": "KBDL-006", "A11Y": "KBDL-006", "PRO": "KBDL-009",
    "CUS": "KBDL-010", "VAL": "KBDL-011",
}

AUTHORITY_DEFECTS = {
    "AR2_SCOPE", "HISTORICAL_RECOVERY", "MISSING_AUTHORITY_TARGET",
    "NONAPPROVED_AUTHORITY_TARGET", "SELF_AUTHORITY", "MISSING_STANDARD_BASIS",
    "STANDARD_CLAUSE_MISMATCH", "UNCLASSIFIED_AUTHORITY_REFERENCE",
    "LIFECYCLE_ONLY_AUTHORITY", "UNSUPPORTED_GENERIC_AUTHORITY",
    "CIRCULAR_AUTHORITY",
}

NORMATIVE_KIND = {
    "Lifecycle status": "life",
    "Provenance": "prov",
    "Validation classification": "val",
}


class GeneratorError(Exception):
    """Fail-closed generator error. Never downgraded to a warning."""


# --------------------------------------------------------------------------
# Markdown parsing helpers
# --------------------------------------------------------------------------

def slug(text: str) -> str:
    return re.sub(r"[^\w\- ]", "", text.replace("`", "").lower()).replace(" ", "-")


def headings(text: str):
    """Return [(start, end, level, anchor, title)] for every ATX heading.

    Duplicate slugs get the GitHub '-1', '-2', ... suffix, matching the anchor
    scheme the repository's cross-references already rely on.
    """
    out = []
    counts = Counter()
    for m in re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*#*$", text):
        base = slug(m.group(2))
        n = counts[base]
        counts[base] += 1
        out.append((m.start(), m.end(), len(m.group(1)),
                    base if not n else f"{base}-{n}", m.group(2)))
    return out


def section_text(path: Path, anchor: str) -> str:
    """Return the body of the section whose anchor matches, or ''."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""
    hs = headings(text)
    hit = next((h for h in hs if h[3] == unquote(anchor)), None)
    if not hit:
        return ""
    end = next((h[0] for h in hs if h[0] > hit[0] and h[2] <= hit[2]), len(text))
    return text[hit[0]:end]


LABEL_STOP = (
    r"(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status|\s+method"
    r"|\s+evidence)?|Authority|Known\s+limitation|Packet(?:\s+or\s+tracking)?\s+"
    r"destination|Pending\s+dependenc(?:y|ies)|Related\s+decision|Notes(?:\s+or\s+"
    r"exclusions)?)\s*:|\n\s*- |\Z)"
)


def label(block: str, pattern: str) -> str:
    """Extract one labelled field value from a normative requirement block."""
    m = re.search(r"(?is)\b" + pattern + r"\s*:\s*(.*?)" + LABEL_STOP, block)
    return " ".join(m.group(1).split()) if m else ""


def normalize(value: str, kind: str) -> str:
    """Normalize a lifecycle / provenance / validation value to its domain."""
    q = value.lower().strip()
    if kind == "life":
        m = re.match(r"(approved|recommended|deferred|blocked|unresolved)\b", q)
        return m.group(1).title() if m else ""
    if kind == "prov":
        if q.startswith("user-provided and confirmed"):
            return "User-provided and Confirmed"
        m = re.match(r"(user-provided|confirmed|assumed)\b", q)
        if not m:
            return ""
        return {"user-provided": "User-provided", "confirmed": "Confirmed",
                "assumed": "Assumed"}.get(m.group(1), "")
    # kind == "val"
    if q.startswith("mixed") and "verified" in q and "not verified" in q:
        return "Mixed — Verified / Not verified"
    if q.startswith("not verified"):
        return "Not verified"
    if q.startswith("not applicable"):
        return "Not applicable"
    if q.startswith("verified") and "not verified" in q:
        return "Mixed — Verified / Not verified"
    if q.startswith("verified"):
        return "Verified"
    return ""


def path_refs(value: str):
    return re.findall(r"(?<![\w/])([\w./-]+\.(?:md|csv|txt)(?:#[\w%.-]+)?)", value)


def collapse(value: str) -> str:
    return re.sub(r"[`.,\s]+", " ", value).strip().lower()


# --------------------------------------------------------------------------
# Source model
# --------------------------------------------------------------------------

class SourceModel:
    """Everything derived from current repository sources, computed once."""

    def __init__(self, repo_root: Path):
        self.root = repo_root
        self.docs = repo_root / "docs/kbdl"
        self.defects = defaultdict(set)   # category -> {requirement id}
        self._git_ok = None
        self._sha_cache = {}
        self._load()

    def add_defect(self, category: str, rid: str) -> None:
        self.defects[category].add(rid)

    def has_defect(self, rid: str, categories) -> bool:
        return any(rid in self.defects[c] for c in categories)

    def _read(self, rel: str) -> str:
        p = self.docs / rel
        if not p.is_file():
            raise GeneratorError(f"required source missing: docs/kbdl/{rel}")
        return p.read_text(encoding="utf-8")

    # -- loading ---------------------------------------------------------

    def _load(self):
        self._load_blocks()
        self._load_ledger()
        self._load_groups()
        self._load_decisions()
        self._load_authority_inputs()
        self._load_lifecycle()
        self._build_authority_graph()
        self._build_packet_index()

    def _load_blocks(self):
        """Normative requirement blocks and their containing section anchors."""
        self.blocks = {}
        self.locations = {}
        for rel in MODULE_FILES:
            text = self._read(rel)
            hs = headings(text)
            if rel == "governance.md":
                matches = list(re.finditer(r"(?m)^## (KBDL-GOV-\d{3})\b", text))
            else:
                matches = list(re.finditer(rf"(?m)^- \*\*`?({RID_RX})`?", text))
            for i, m in enumerate(matches):
                stop = matches[i + 1].start() if i + 1 < len(matches) else len(text)
                nxt = next((h[0] for h in hs if h[0] > m.start() and h[2] <= 2), stop)
                stop = min(stop, nxt)
                rid = m.group(1)
                if rid in self.blocks:
                    continue
                self.blocks[rid] = (rel, text[m.start():stop])
                owner = max((h for h in hs if h[0] < m.start()),
                            key=lambda x: x[0], default=None)
                self.locations[rid] = f"{rel}#{owner[3]}" if owner else rel
        if not self.blocks:
            raise GeneratorError("no normative requirement records parsed")

    def _load_ledger(self):
        text = self._read("traceability-metadata.csv")
        rows = list(csv.DictReader(io.StringIO(text)))
        if not rows:
            raise GeneratorError("traceability-metadata.csv contains no rows")
        self.ledger = rows
        self.by_id = {r["Requirement ID"]: r for r in rows}
        missing = sorted(set(self.blocks) - set(self.by_id))
        if missing:
            raise GeneratorError(
                "normative records absent from traceability-metadata.csv: "
                + ", ".join(missing))

    def _group_member_ids(self, spec: str) -> list:
        """Expand a readable-group 'Requirement ID' specification into IDs."""
        core = spec.split(" (")[0]
        ids = list(dict.fromkeys(re.findall(RID_RX, core)))

        def in_range(rid, module, lo, hi):
            if not rid.startswith(f"KBDL-{module}-"):
                return False
            m = re.search(r"\d{3}", rid.rsplit("-", 1)[1])
            return bool(m) and lo <= int(m.group()) <= hi

        for rm in re.finditer(
                rf"(KBDL-({MODULES})-(\d{{3}})[a-z]?)\s*(?:–|—|through|to)\s*"
                rf"`?(?:KBDL-\2-)?(\d{{3}})[a-z]?`?", core):
            module, lo, hi = rm.group(2), int(rm.group(3)), int(rm.group(4))
            ids.extend(r["Requirement ID"] for r in self.ledger
                       if in_range(r["Requirement ID"], module, lo, hi))
        if ids:
            module = ids[0].split("-")[1]
            for rm in re.finditer(r"(?<![\d-])(\d{3})\s*(?:–|—|through|to)\s*(\d{3})", core):
                lo, hi = map(int, rm.groups())
                ids.extend(r["Requirement ID"] for r in self.ledger
                           if in_range(r["Requirement ID"], module, lo, hi))
        if ids:
            module = ids[0].split("-")[1]
            for short in re.findall(r"`(\d{3}[a-z]?)`", spec):
                cand = f"KBDL-{module}-{short}"
                if cand in self.by_id:
                    ids.append(cand)
        return list(dict.fromkeys(ids))

    def _load_groups(self):
        """Parse readable traceability groups into per-(ID, field) values."""
        trace = self._read("traceability-matrix.md")
        starts = list(re.finditer(r"(?m)^###\s+(.+)$", trace))
        self.group_values = {}
        self.blueprint_values = set()

        for i, m in enumerate(starts):
            end = starts[i + 1].start() if i + 1 < len(starts) else len(trace)
            g = trace[m.start():end]
            idline = re.search(r"(?im)^- \*\*Requirement ID[^:]*:\*\*\s*(.+)$", g)
            ids = self._group_member_ids(idline.group(1)) if idline else []
            if not ids:
                continue
            for field, pat in GROUP_LABELS.items():
                lm = re.search(r"(?im)^- \*\*" + pat + r":\*\*\s*(.+(?:\n(?![-#])\s{2,}.+)*)", g)
                raw = " ".join(lm.group(1).split()) if lm else ""
                combined = "/" in (lm.group(0).split(":", 1)[0] if lm else "")
                for rid in ids:
                    value, cls, grammar, override = self._resolve_group_value(
                        rid, field, raw)
                    if field in {"Validation method", "Validation evidence"} and combined:
                        cls, grammar, override = ("Non-overriding summary",
                                                  "Combined method/evidence summary", "No")
                    self.group_values[(rid, field)] = (value, cls, grammar, override)
                    if field == "Blueprint section" and value:
                        self.blueprint_values.add(value)

    def _resolve_group_value(self, rid: str, field: str, raw: str):
        """Resolve one group member's value for one field from the group text."""
        short = rid.rsplit("-", 1)[1]

        arrow = re.search(
            rf"(?:`?{re.escape(rid)}`?|`?{re.escape(short)}`?)\s*(→|:)[ ]*(.*?)"
            rf"(?=;\s*(?:`?{RID_RX}`?|`?\d{{3}}[a-z]?`?)\s*(?:→|:)|$)", raw)

        clause = next(((cl.split(":", 1)[1].strip(), cl) for cl in raw.split(";")
                       if ":" in cl and (rid in cl.split(":", 1)[0]
                                         or short in re.findall(r"\b\d{3}[a-z]?\b",
                                                                cl.split(":", 1)[0]))), None)

        status_rx = (r"Mixed\s*[—-]\s*Verified\s*/\s*Not verified|Verified|Not verified"
                     r"|Not applicable|Approved|Recommended|Deferred|Blocked|Unresolved")
        buckets = list(re.finditer(
            rf"(?i)(?:^|;)\s*({status_rx})\s*:\s*(.*?)(?=;\s*(?:{status_rx})\s*:|$)", raw))
        bucket_hit = next((b for b in buckets
                           if rid in re.findall(RID_RX, b.group(2))
                           or short in re.findall(r"\b\d{3}[a-z]?\b", b.group(2))), None)

        short_num = int(re.match(r"\d{3}", short).group())
        range_hit = next((rm for rm in re.finditer(
            r"`?(\d{3}[a-z]?)`?\s*(?:–|—|through|to)\s*`?(\d{3}[a-z]?)`?\s*:\s*(.*?)(?=;|$)", raw)
            if int(re.match(r"\d{3}", rm.group(1)).group()) <= short_num
            <= int(re.match(r"\d{3}", rm.group(2)).group())), None)

        def status_value(text):
            fixed = re.sub(r"(?i)^mixed\s*[—-]\s*verified\s*/\s*not verified$",
                           "Mixed — Verified / Not verified", text)
            return fixed.capitalize().replace("Mixed — verified / not verified",
                                              "Mixed — Verified / Not verified")

        if field == "Validation classification" and bucket_hit:
            return status_value(bucket_hit.group(1)), "Exact per-ID mapping", "Status bucket", "Yes"
        if clause:
            summary = (field in {"Authority", "Known limitation", "Notes or exclusions"}
                       and re.search(r"(?i)see each|exact split|implementation-dependent"
                                     r"|readable group|group values", clause[0]))
            cls = "Non-overriding summary" if summary else "Exact per-ID mapping"
            return clause[0], cls, "Per-ID clause mapping", "No" if summary else "Yes"
        if arrow:
            grammar = "Arrow mapping" if arrow.group(1) == "→" else "Colon mapping"
            return arrow.group(2).strip(), "Exact per-ID mapping", grammar, "Yes"
        if range_hit:
            summary = (field in {"Authority", "Known limitation"}
                       or re.search(r"(?i)see each|exact sources|implementation-dependent",
                                    range_hit.group(3)))
            cls = "Non-overriding summary" if summary else "Exact per-ID mapping"
            return range_hit.group(3).strip(), cls, "Range mapping", "No" if summary else "Yes"
        if bucket_hit:
            return status_value(bucket_hit.group(1)), "Exact per-ID mapping", "Status bucket", "Yes"
        if buckets:
            return "", "Unresolved", "Status bucket", "Yes"
        if raw and field in NORMATIVE_KIND:
            candidate = normalize(re.sub(r"(?i)^all\s+", "", raw).rstrip("."),
                                  NORMATIVE_KIND[field])
            if candidate:
                return candidate, "Uniform default", "Uniform status default", "Yes"
        if raw:
            if field in {"Blueprint section", "Roadmap prompt"}:
                return raw, "Uniform default", "Uniform default", "Yes"
            return raw, "Non-overriding summary", "Broad descriptive summary", "No"
        return "", "Missing", "Missing", "No"

    def _load_decisions(self):
        text = self._read("decision-register.md")
        self.decisions = {}
        marks = list(re.finditer(r"(?m)^### (KBDL-DEC-\d{3})", text))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            body = text[m.start():end]
            sm = re.search(r"(?im)^- \*\*Status:\*\*\s*(.+)", body)
            self.decisions[m.group(1)] = sm.group(1).strip() if sm else "MISSING"

    def _load_authority_inputs(self):
        mapping_rel = ("evidence/kbdl-011-authority-recovery/artifacts/"
                       "requirement-authority-mapping.csv")
        ledger_rel = "evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv"
        self.auth_map = {r["Requirement ID"]: r
                         for r in csv.DictReader(io.StringIO(self._read(mapping_rel)))}
        self.recovery = {r["Prompt ID"]: r
                         for r in csv.DictReader(io.StringIO(self._read(ledger_rel)))}

    def _load_lifecycle(self):
        self.lifecycle = {}
        for rid, (_rel, block) in self.blocks.items():
            value = normalize(label(block, r"Lifecycle(?: status)?"), "life")
            if not value and rid.startswith("KBDL-GOV-"):
                # Historical GOV format carries no per-record lifecycle field;
                # the document status plus the approved KBDL-001 prompt govern.
                value = "Approved"
            self.lifecycle[rid] = value
        self.approved = {r for r, v in self.lifecycle.items() if v == "Approved"}
        self.approved_prompt = self.approved & set(self.auth_map)

    # -- authority graph --------------------------------------------------

    def _build_authority_graph(self):
        self.graph = defaultdict(set)
        for rid in sorted(self.approved):
            rel, block = self.blocks[rid]
            expr = self.by_id[rid]["Authority"]
            targets = set(re.findall(rf"KBDL-DEC-\d{{3}}|{RID_RX}", expr))
            prompt = rid in self.approved_prompt

            if prompt:
                confirmation = self.recovery.get(self.auth_map[rid]["Prompt ID"])
                relied = (confirmation["Requirements relying on the prompt"].split("; ")
                          if confirmation else [])
                if (not confirmation
                        or confirmation["Project-owner decision"] != "CONFIRM CURRENT AUTHORITY"
                        or rid not in relied):
                    self.add_defect("AR2_SCOPE", rid)
                if confirmation and confirmation["Approval command recovered"] != "NO":
                    self.add_defect("HISTORICAL_RECOVERY", rid)

            for target in sorted(targets):
                if target.startswith("KBDL-DEC-"):
                    if self.decisions.get(target) != "Approved":
                        self.add_defect("MISSING_AUTHORITY_TARGET", rid)
                    continue
                pos = expr.find(target)
                context = expr[max(0, pos - 120):pos + len(target) + 120].lower()
                if re.search(r"unapproved context|context only|does not approve|excluded"
                             r"|specific applications", context):
                    refclass = "Context-only reference"
                elif "together with" in context:
                    refclass = "Supporting authority"
                elif (re.search(r"analogy|consistent with", context)
                      and not re.search(r"restates|extends|authority|established|inherits",
                                        context)):
                    refclass = "Non-authoritative analogy"
                elif re.search(r"related requirement", context):
                    refclass = "Related requirement"
                else:
                    refclass = "Authority edge"
                if refclass in {"Authority edge", "Supporting authority"}:
                    self.graph[rid].add(target)
                    if self.lifecycle.get(target) != "Approved":
                        self.add_defect("NONAPPROVED_AUTHORITY_TARGET", rid)
                if target == rid:
                    self.add_defect("SELF_AUTHORITY", rid)

            self._check_standard_basis(rid, block, expr, prompt, targets)

            if not prompt and not targets and not re.search(r"\b(?:WCAG|WAI-ARIA|ARIA)\b",
                                                            expr, re.I):
                if re.search(r"approved lifecycle|lifecycle status", expr, re.I):
                    self.add_defect("LIFECYCLE_ONLY_AUTHORITY", rid)
                elif not re.match(r"^(?:Approved|Recommended|Deferred|Blocked|Unresolved)\b",
                                  expr, re.I):
                    self.add_defect("UNSUPPORTED_GENERIC_AUTHORITY", rid)

        self._detect_cycles()

    def _check_standard_basis(self, rid, block, expr, prompt, targets):
        if not re.search(r"\b(?:WCAG|WAI-ARIA|ARIA)\b", expr, re.I):
            return
        clause_rx = r"(?i)\b(?:SC\s*)?\d\.\d\.(?:\d|x)\b|\b(?:aria-[a-z-]+)"
        cited = set(re.findall(clause_rx, expr))
        governing = set(re.findall(clause_rx, block)) if cited else set()

        def canon(x):
            return re.sub(r"\s+", " ", x).strip().lower()

        match = bool(cited) and all(
            any(canon(c).replace(".x", ".") in canon(g) for g in governing) for c in cited)
        if cited and not match:
            self.add_defect("STANDARD_CLAUSE_MISMATCH", rid)
        if not cited and not governing and not (prompt or targets):
            self.add_defect("MISSING_STANDARD_BASIS", rid)
            self.add_defect("STANDARD_CLAUSE_MISMATCH", rid)
        if re.fullmatch(r"WCAG\s+2\.2", expr.strip(), re.I):
            self.add_defect("MISSING_STANDARD_BASIS", rid)

    def _detect_cycles(self):
        seen = set()

        def walk(start, node, path):
            for nxt in sorted(self.graph.get(node, set())):
                if nxt in path:
                    cycle = tuple(path[path.index(nxt):] + [nxt])
                    key = tuple(sorted(set(cycle)))
                    if len(key) > 1 and key not in seen:
                        seen.add(key)
                        self.add_defect("CIRCULAR_AUTHORITY", start)
                else:
                    walk(start, nxt, path + [nxt])

        for rid in sorted(self.graph):
            walk(rid, rid, [rid])

    # -- packet index -----------------------------------------------------

    def _build_packet_index(self):
        self.packet_index = defaultdict(list)
        for path in sorted(self.docs.rglob("*.md"), key=lambda p: p.as_posix()):
            if "evidence/" in path.relative_to(self.docs).as_posix():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            hs = headings(text)
            recognized = []
            for i, h in enumerate(hs):
                if re.search(r"(?i)packet|tracking|recommended decisions|unresolved"
                             r"|approval-ready|deferred|contingent|pending", h[4]):
                    end = hs[i + 1][0] if i + 1 < len(hs) else len(text)
                    recognized.append((h[0], end, h[3], h[4]))
            if not recognized:
                continue
            lines = text.splitlines()
            pos = 0
            rel = path.relative_to(self.docs).as_posix()
            for lineno, line in enumerate(lines, 1):
                start = pos
                pos += len(line) + 1
                owner = next((x for x in recognized if x[0] <= start < x[1]), None)
                if not owner:
                    continue
                found = re.findall(RID_RX, line)
                if not found:
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                nums = []
                if cells and re.fullmatch(r"\d+", cells[0]):
                    nums.append(int(cells[0]))
                nums += [int(x) for x in re.findall(r"(?i)\bitem\s+(\d+)\b", line)]
                for rid in found:
                    self.packet_index[rid].append(
                        {"Document": rel, "Line": lineno, "Item numbers": sorted(set(nums))})

    # -- git-backed evidence verification ---------------------------------

    def commit_exists(self, sha: str) -> bool:
        """True when `sha` resolves to a commit in this repository.

        Fails closed: if git is unavailable or the repository has no object
        database, the generator raises rather than silently producing a
        different registry than it would in a git-backed checkout.
        """
        if sha in self._sha_cache:
            return self._sha_cache[sha]
        if self._git_ok is None:
            probe = subprocess.run(
                ["git", "-C", str(self.root), "rev-parse", "--git-dir"],
                capture_output=True, text=True)
            self._git_ok = probe.returncode == 0
        if not self._git_ok:
            raise GeneratorError(
                "evidence values cite commit SHAs but this repository root has no "
                "git object database; refusing to emit a registry whose evidence "
                "resolution would differ from a git-backed checkout")
        result = subprocess.run(
            ["git", "-C", str(self.root), "cat-file", "-e", sha + "^{commit}"],
            capture_output=True)
        if result.returncode not in (0, 1, 128):
            raise GeneratorError(
                f"git cat-file failed unexpectedly for {sha}: rc={result.returncode}")
        ok = result.returncode == 0
        self._sha_cache[sha] = ok
        return ok


# --------------------------------------------------------------------------
# Per-requirement derivation
# --------------------------------------------------------------------------

class RequirementDerivation:
    """Derived per-requirement facts needed by the per-field rows."""

    def __init__(self, model: SourceModel, rid: str):
        self.m = model
        self.rid = rid
        self.rel, self.block = model.blocks[rid]
        self.ledger_row = model.by_id[rid]
        self.normative = {
            "Requirement ID": rid,
            "Lifecycle status": normalize(label(self.block, r"Lifecycle(?: status)?"), "life"),
            "Provenance": normalize(label(self.block, "Provenance"), "prov"),
            "Validation classification": normalize(
                label(self.block, r"Validation(?: status)?"), "val"),
            "Authority": label(self.block, "Authority"),
            "Validation method": label(self.block, "Validation method"),
            "Known limitation": label(self.block, "Known limitation"),
            "Pending dependencies": label(self.block, r"Pending dependenc(?:y|ies)"),
            "Related decision": label(self.block, "Related decision"),
        }
        self.roadmap = self._roadmap()
        self.location = self._location()
        self.packet_ok, self.packet_basis = self._packet()
        self.dependency_ok, self.dependency_basis = self._dependency()
        self.evidence_ok = self._evidence()
        self.limitation_ok = self._limitation()

    def _roadmap(self) -> str:
        module = self.rid.split("-")[1]
        if module == "CMP":
            return "KBDL-007" if self.rel == "components-core.md" else "KBDL-008"
        return ROADMAP_BY_MODULE[module]

    def _location(self) -> str:
        explicit = re.search(
            r"(?is)(?:Specification location|Related foundation section)\s*:\s*"
            r"\[[^\]]+\]\(([^)]+)\)", self.block)
        if not explicit:
            return self.m.locations[self.rid]
        target = explicit.group(1)
        pth, sep, anchor = target.partition("#")
        resolved = (Path(self.rel).parent / pth).as_posix() if pth else self.rel
        resolved = str(Path(resolved))
        return resolved + ("#" + anchor if sep else "")

    def _valid_location(self, value: str) -> bool:
        pth, sep, anchor = value.partition("#")
        return bool(sep and (self.m.docs / pth).is_file()
                    and section_text(self.m.docs / pth, anchor))

    def location_ok(self) -> bool:
        listed = [x.strip() for x in self.ledger_row["Specification location"].split(";")]
        return (bool(listed) and all(self._valid_location(x) for x in listed)
                and set(listed) == {self.location})

    def _packet(self):
        packet = self.ledger_row["Packet or tracking destination"]
        if not packet:
            return False, "missing"
        if packet.lower().startswith("none"):
            ok = self.m.lifecycle[self.rid] == "Approved"
            return ok, "Explicit None permitted only for Approved"
        rows = self.m.packet_index.get(self.rid, [])
        docm = re.search(r"([\w/-]+\.md)", packet)
        itemm = re.search(r"(?i)\bitem\s+(\d+)\b", packet)
        doc = docm.group(1) if docm else self.rel
        item = int(itemm.group(1)) if itemm else None
        matches = [x for x in rows
                   if (not doc or x["Document"] == doc)
                   and (item is None or item in x["Item numbers"])]
        basis = "; ".join(f"{x['Document']}:{x['Line']} item={x['Item numbers']}"
                          for x in matches) or "no exact packet row/item"
        return bool(matches), basis

    def _dependency(self):
        dep = self.ledger_row["Pending dependencies"]
        packet = self.ledger_row["Packet or tracking destination"]
        normative_dep = self.normative["Pending dependencies"]
        basis = normative_dep or ("Packet/tracking record"
                                  if packet and not packet.lower().startswith("none")
                                  else "Explicit None")
        ok = bool(dep) and (not normative_dep or collapse(dep) == collapse(normative_dep))
        return ok, basis

    def _evidence(self) -> bool:
        evidence = self.ledger_row["Validation evidence"]
        resolved, bad = [], []
        for ref in path_refs(evidence):
            base, sep, anchor = ref.partition("#")
            p = (self.m.root / base) if base.startswith("docs/") else (self.m.docs / base)
            if not p.exists() and not base.startswith("docs/"):
                p = self.m.docs / Path(self.ledger_row.get("Source file", "")).parent / base
            if p.exists() and (not sep or (p.suffix == ".md" and section_text(p, anchor))):
                resolved.append(p.relative_to(self.m.root).as_posix()
                                + (("#" + anchor) if sep else ""))
            else:
                bad.append(ref)

        shas = re.findall(r"(?<![0-9a-f])([0-9a-f]{7,40})(?![0-9a-f])", evidence)
        valid_shas = [s for s in shas if self.m.commit_exists(s)]

        classification = self.ledger_row["Validation classification"]
        verified = "Verified" in classification
        associated = True
        if verified and resolved:
            associated = any(
                self._names_requirement(x) for x in resolved) or any(
                self.rid.lower().replace("kbdl-", "") in Path(x.partition("#")[0]).stem.lower()
                for x in resolved)
        generic = evidence.startswith("Executed evidence") and not (resolved or valid_shas)
        return (bool(evidence) and not bad and not generic
                and (not verified or bool(resolved or valid_shas))
                and associated
                and not ("Not verified" in classification
                         and re.search(r"\bPASS\b", evidence)
                         and "no PASS" not in evidence))

    def _names_requirement(self, ref: str) -> bool:
        p = self.m.root / ref.partition("#")[0]
        if not p.is_file():
            return False
        try:
            return self.rid in p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return False

    def _limitation(self) -> bool:
        limitation = self.ledger_row["Known limitation"]
        unverified = (self.ledger_row["Not-verified scope"] + " "
                      + self.ledger_row["Validation classification"]).lower()
        ok = (bool(limitation)
              and (unverified.strip() or "none" in limitation.lower())
              and not re.search(r"production ready|completion approved", limitation, re.I))
        scope_terms = (set(re.findall(r"[a-z]{5,}", unverified))
                       - {"verified", "validation", "classification"})
        lim_terms = set(re.findall(r"[a-z]{5,}", limitation.lower()))
        if (normalize(self.ledger_row["Validation classification"], "val") == "Not verified"
                and not (scope_terms & lim_terms)):
            ok = False
        return bool(ok)


def semantically_equal(field: str, a: str, b: str) -> bool:
    kind = NORMATIVE_KIND.get(field)
    if kind:
        return normalize(a, kind) == normalize(b, kind)
    if field in {"Packet or tracking destination", "Pending dependencies"}:
        ai = set(re.findall(r"(?i)\bitem\s+(\d+)", a))
        bi = set(re.findall(r"(?i)\bitem\s+(\d+)", b))
        at = set(re.findall(RID_RX, a))
        bt = set(re.findall(RID_RX, b))

        def klass(x):
            x = x.lower()
            if "implement" in x:
                return "implementation"
            if "adopting" in x:
                return "project"
            if "review" in x or "planning" in x:
                return "review"
            if "block" in x:
                return "blocking"
            return ""

        return ((a.lower().startswith("none") and b.lower().startswith("none"))
                or (bool(ai) and ai == bi)
                or (bool(at) and at == bt
                    and ("block" in a.lower()) == ("block" in b.lower()))
                or (bool(klass(a)) and klass(a) == klass(b)))
    if field == "Related decision":
        return (set(re.findall(r"KBDL-DEC-\d{3}", a))
                == set(re.findall(r"KBDL-DEC-\d{3}", b)))
    if field == "Authority":
        rx = rf"KBDL-DEC-\d{{3}}|{RID_RX}"
        return set(re.findall(rx, a)) == set(re.findall(rx, b))
    return collapse(a) == collapse(b)


def build_rows(model: SourceModel):
    """Return every registry row, sorted by the declared sort key."""
    rows = []
    for rid in sorted(model.blocks):
        d = RequirementDerivation(model, rid)
        lr = d.ledger_row
        for field in FIELD_NAMES:
            gv, gcls, _grammar, goverride = model.group_values.get(
                (rid, field), ("", "Missing", "Missing", "No"))
            ledger_value = rid if field == "Requirement ID" else lr.get(field, "")
            normative_value = d.normative.get(field, "")
            expected, basis = resolve_expected(model, d, field, ledger_value,
                                               normative_value, gv, gcls)

            conflict = "None"
            if normative_value and field in NORMATIVE_KIND:
                if normalize(ledger_value, NORMATIVE_KIND[field]) != normative_value:
                    conflict = f"normative={normative_value}; ledger={ledger_value}"
            if goverride == "Yes" and gv and not semantically_equal(field, ledger_value, gv):
                conflict = "group/ledger mismatch"
            if field == "Roadmap prompt" and not (
                    ledger_value == expected
                    or ledger_value.startswith(expected + " ")
                    or ledger_value.startswith(expected + "-")):
                conflict = "roadmap mismatch"

            governance_ok = field not in {"Authority", "Related decision"} or bool(expected)
            rows.append({
                "Requirement ID": rid,
                "Field name": field,
                "Ownership class": OWNERSHIP[field],
                "Primary basis": basis,
                "Derivation rule": DERIVATION[field],
                "Authoritative expected value": expected or "UNRESOLVED",
                "Normative value": normative_value or "ABSENT",
                "Governance resolution": "PASS" if governance_ok else "FAIL",
                "Ledger value": ledger_value,
                "Readable-group value": gv or "MISSING",
                "Readable-group classification": gcls,
                "Effective value": expected or "UNRESOLVED",
                "Precedence result": "PASS" if conflict == "None" else "FAIL",
                "Conflict result": conflict,
                "Validation result": "PASS" if expected and conflict == "None" else "FAIL",
            })
    rows.sort(key=lambda r: (r["Requirement ID"], FIELD_ORDER[r["Field name"]]))
    return rows


def resolve_expected(model, d, field, ledger_value, normative_value, gv, gcls):
    """Return (authoritative expected value, primary basis) for one cell."""
    rid = d.rid
    if field == "Requirement ID":
        return rid, "Normative record"
    if field == "Blueprint section":
        if gcls in {"Exact per-ID mapping", "Uniform default"}:
            expected = gv
        elif ledger_value in model.blueprint_values:
            expected = ledger_value
        else:
            expected = ""
        return expected, "Exact readable-group value"
    if field == "Roadmap prompt":
        return d.roadmap, "Approved roadmap/module derivation"
    if field == "Specification location":
        return d.location, "Containing normative section"
    if field in NORMATIVE_KIND:
        if normative_value:
            return normative_value, "Normative record"
        if rid.startswith("KBDL-GOV-"):
            if field == "Lifecycle status":
                return ("Approved",
                        "Historical governance source: document status and approved "
                        "KBDL-001 prompt")
            if field == "Provenance":
                return ("Historical KBDL-001 prompt and approved decision record",
                        "Historical governance source: approved KBDL-001 prompt and decisions")
        return "", "Normative record"
    if field == "Validation method":
        if normative_value:
            return normative_value, "Normative record"
        if gv:
            return gv, "Readable-group evidence method"
        return "", "UNRESOLVED"
    if field == "Authority":
        resolved = (rid not in model.approved
                    or not model.has_defect(rid, AUTHORITY_DEFECTS))
        return ("RESOLVED" if resolved else ""), "Authority graph"
    if field == "Related decision":
        cited = re.findall(r"KBDL-DEC-\d{3}", ledger_value)
        ok = all(model.decisions.get(x) == "Approved" for x in cited)
        return ("RESOLVED" if ok else ""), "Decision register"
    if field == "Packet or tracking destination":
        return (ledger_value if d.packet_ok else ""), d.packet_basis
    if field == "Pending dependencies":
        return (ledger_value if d.dependency_ok else ""), d.dependency_basis
    if field == "Validation evidence":
        return (ledger_value if d.evidence_ok else ""), \
            "Resolved evidence/classification relationship"
    if field == "Known limitation":
        return (ledger_value if d.limitation_ok else ""), \
            "Not-verified/excluded scope relationship"
    if field in {"Verified scope", "Not-verified scope"}:
        return ledger_value, "Evidence scope registry"
    return ledger_value, "Owned administrative value bounded by prohibited-claim scan"


# --------------------------------------------------------------------------
# Serialization, path safety, CLI
# --------------------------------------------------------------------------

def serialize(rows) -> bytes:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue().encode("utf-8")


def resolve_output_path(repo_root: Path) -> Path:
    """Resolve and contain the single permitted output path.

    Every containment check is performed on fully resolved paths, so a symlink
    anywhere in the chain cannot redirect the write outside the package.
    """
    root = repo_root.resolve(strict=True)
    package_declared = root / PACKAGE_REL
    if not package_declared.is_dir():
        raise GeneratorError(
            f"FSRG1 package directory not present under this root: {PACKAGE_REL}")
    package = package_declared.resolve(strict=True)
    if package != root and root not in package.parents:
        raise GeneratorError("FSRG1 package does not resolve inside the repository root")
    declared = root / ARTIFACT_REL
    parent = declared.parent.resolve(strict=False)
    if package != parent and package not in parent.parents:
        raise GeneratorError("output parent does not resolve inside the FSRG1 package")
    if declared.is_symlink():
        raise GeneratorError("output target is a symlink; refusing to write")
    for ancestor in list(parent.parents) + [parent]:
        if ancestor.is_symlink() and root not in ancestor.resolve().parents \
                and ancestor.resolve() != root:
            raise GeneratorError(f"symlink escapes the repository: {ancestor}")
    final = parent / declared.name
    if final.resolve(strict=False) != (root / ARTIFACT_REL).resolve(strict=False):
        raise GeneratorError("resolved output does not equal the declared artifact path")
    return final


def write_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".fsrg1-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def generate(repo_root: Path) -> bytes:
    model = SourceModel(repo_root.resolve(strict=True))
    rows = build_rows(model)
    if not rows:
        raise GeneratorError("generated registry is empty")
    return serialize(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Generate the live current-state field-source registry.")
    ap.add_argument("--repo-root", type=Path, default=Path("."),
                    help="repository root (default: current directory)")
    ap.add_argument("--check", action="store_true",
                    help="regenerate into temporary storage and compare with the "
                         "committed artifact; never writes to the repository")
    args = ap.parse_args(argv)

    try:
        root = args.repo_root.resolve(strict=True)
        data = generate(root)
        if args.check:
            committed = root / ARTIFACT_REL
            if not committed.is_file():
                print(f"FAIL: committed artifact missing: {ARTIFACT_REL}", file=sys.stderr)
                return 1
            with tempfile.TemporaryDirectory(prefix="fsrg1-check-") as tmpdir:
                scratch = Path(tmpdir) / "field-source-registry.csv"
                write_atomic(scratch, data)
                regenerated = scratch.read_bytes()
            current = committed.read_bytes()
            if regenerated != current:
                print("FAIL: regenerated registry differs from the committed artifact",
                      file=sys.stderr)
                print(f"  regenerated bytes={len(regenerated)} committed bytes={len(current)}",
                      file=sys.stderr)
                return 1
            print(f"OK: {ARTIFACT_REL} matches regeneration ({len(current)} bytes)")
            return 0
        out = resolve_output_path(root)
        write_atomic(out, data)
        print(f"OK: wrote {ARTIFACT_REL} ({len(data)} bytes)")
        return 0
    except GeneratorError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
