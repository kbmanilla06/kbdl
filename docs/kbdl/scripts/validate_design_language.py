#!/usr/bin/env python3
"""KBDL Design Language v1 validator.

Small, practical checks over the active design-language documentation and
tokens. Prints one [PASS]/[FAIL] line per check and exits nonzero if any fail.

Deliberately lightweight: no mutation suites, no fixtures, no checksummed
transcripts, no evidence packages. If this file grows past roughly twenty
checks, that is a signal the governance weight is creeping back.

Usage:
    python3 docs/kbdl/scripts/validate_design_language.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]
REPO = DOCS.parents[1]

REQUIRED_DOCS = [
    "README.md", "STATUS.md", "principles.md", "accessibility.md",
    "responsive.md", "profiles.md", "patterns.md", "adoption.md",
    "governance.md", "conformance-checklist.md",
    "foundations/README.md", "themes/README.md", "motion/README.md",
    "components/README.md", "tokens/README.md", "tokens/kbdl.tokens.json",
]

# Active design-language docs. Historical governance records are excluded by
# name and are classified as historical in STATUS.md and README.md.
HISTORICAL_DOCS = {
    "validation.md", "traceability-matrix.md", "decision-register.md",
    "conventions.md", "contributing.md", "glossary.md",
    "components-core.md", "components-system.md", "customization.md",
}

REQUIRED_TOKEN_GROUPS = [
    "color", "typography", "space", "size", "breakpoint", "container",
    "radius", "border", "shadow", "opacity", "motion", "layer", "focus",
]

COMPONENTS = [
    "Button", "Text link", "Icon button", "Text input", "Textarea", "Select",
    "Checkbox", "Radio group", "Switch", "Form field and validation message",
    "Card", "Badge / tag", "Alert", "Toast / notification", "Dialog",
    "Tooltip", "Tabs", "Primary navigation", "Breadcrumb",
    "Table / structured list", "Pagination", "Loading indicator", "Skeleton",
    "Empty state",
]

COMPONENT_SECTIONS = [
    "Purpose", "Anatomy", "Variants", "States", "Interaction", "Responsive",
    "Keyboard", "Focus", "Accessibility", "Content", "Tokens",
]

PROFILES = ["Showcase", "Precision", "Flow"]

A11Y_DISCLAIMER = ("Conformance must be verified in each product "
                   "implementation")
ARCHIVE_NOTICE = ("preserved under\n> `docs/kbdl/evidence/`",
                  "preserved under `docs/kbdl/evidence/`")

# Legacy programme terms that must not be presented as active v1 blockers.
LEGACY_TERMS = re.compile(
    r"PA1-R4|417 pending|owner-decision queue|field-source registry|"
    r"source-model resolution", re.IGNORECASE)
HISTORICAL_MARKER = re.compile(
    r"historical|retire[sd]?|preserved|earlier|previously|no longer|archive|"
    r"not active|do not gate|out of scope", re.IGNORECASE)

TOKEN_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    results.append((name, bool(ok), detail))
    return bool(ok)


def read(rel: str) -> str:
    p = DOCS / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def flat(text: str) -> str:
    """Collapse whitespace and drop Markdown markup so substring checks are not
    defeated by line wrapping, blockquote prefixes, or emphasis."""
    stripped = re.sub(r"[`*_>]", "", text)
    return re.sub(r"\s+", " ", stripped)


def active_markdown() -> list[Path]:
    """Active design-language Markdown: excludes evidence/ and historical docs."""
    out = []
    for p in sorted(DOCS.rglob("*.md")):
        rel = p.relative_to(DOCS).as_posix()
        if rel.startswith("evidence/") or rel in HISTORICAL_DOCS:
            continue
        out.append(p)
    return out


def flatten(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from flatten(v, f"{prefix}.{k}" if prefix else k)
    else:
        yield prefix, obj


def main() -> int:
    # 1. required documents exist
    missing = [d for d in REQUIRED_DOCS if not (DOCS / d).is_file()]
    check("1. required active documents exist", not missing, f"missing={missing}")

    # 2. token JSON parses
    raw = read("tokens/kbdl.tokens.json")
    tokens, parse_err = None, ""
    try:
        tokens = json.loads(raw) if raw else None
    except json.JSONDecodeError as exc:
        parse_err = str(exc)
    check("2. token JSON parses", tokens is not None, parse_err or "file missing")
    if tokens is None:
        return report()

    # 3. token paths are unique
    paths = [p for p, _ in flatten(tokens)]
    dupes = sorted({p for p in paths if paths.count(p) > 1})
    check("3. token paths are unique", not dupes, f"duplicates={dupes[:5]}")

    # 4. token names follow the convention
    bad = sorted({seg for p in paths for seg in p.split(".")
                  if not TOKEN_NAME.match(seg) and not seg.startswith("$")})
    check("4. token name segments are lowercase, hyphenated, hierarchical",
          not bad, f"invalid={bad[:8]}")

    # 5. required token groups exist
    absent = [g for g in REQUIRED_TOKEN_GROUPS if g not in tokens]
    check("5. required token groups exist", not absent, f"absent={absent}")

    # 6. internal markdown links resolve
    broken = []
    for p in active_markdown():
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path_part = target.split("#")[0]
            if not path_part:
                continue
            if not (p.parent / path_part).exists():
                broken.append(f"{p.relative_to(DOCS)} -> {target}")
    check("6. internal markdown links resolve", not broken, f"broken={broken[:5]}")

    # 7. every core component has a heading
    comp = read("components/README.md")
    headings = re.findall(r"(?m)^## \d+\.\s+(.+)$", comp)
    missing_c = [c for c in COMPONENTS if c not in headings]
    check(f"7. all {len(COMPONENTS)} core component headings exist",
          not missing_c, f"missing={missing_c}")

    # 8. every component carries the required specification sections
    blocks = re.split(r"(?m)^## \d+\.\s+", comp)[1:]
    incomplete = []
    for block in blocks:
        title = block.split("\n", 1)[0].strip()
        for section in COMPONENT_SECTIONS:
            if f"**{section}**" not in block:
                incomplete.append(f"{title}:{section}")
    check("8. every component has the required specification sections",
          not incomplete, f"missing={incomplete[:6]}")

    # 9. all three profiles are documented
    profiles_doc = read("profiles.md") + read("README.md")
    absent_p = [p for p in PROFILES if p not in profiles_doc]
    check("9. Showcase, Precision, and Flow are documented", not absent_p,
          f"absent={absent_p}")

    # 10. accessibility conformance disclaimer present
    a11y_ok = any(A11Y_DISCLAIMER in flat(read(d))
                  for d in ("README.md", "accessibility.md", "adoption.md",
                            "STATUS.md"))
    check("10. accessibility conformance disclaimer present", a11y_ok,
          "no document states conformance must be verified per implementation")

    # 11. historical archive notice present
    archive_ok = any("docs/kbdl/evidence/" in flat(read(d)) and
                     "not active completion gates" in flat(read(d))
                     for d in ("README.md", "governance.md", "STATUS.md"))
    check("11. historical archive notice present", archive_ok,
          "no active document labels docs/kbdl/evidence/ as historical")

    # 12. active docs do not present legacy programme items as v1 blockers
    unlabelled = []
    for p in active_markdown():
        text = p.read_text(encoding="utf-8")
        for m in LEGACY_TERMS.finditer(text):
            start = max(text.rfind("\n\n", 0, m.start()), 0)
            end = text.find("\n\n", m.end())
            para = flat(text[start:end if end != -1 else len(text)])
            if not HISTORICAL_MARKER.search(para):
                unlabelled.append(f"{p.relative_to(DOCS)}: {m.group(0)}")
    check("12. active documentation presents no legacy item as a v1 blocker",
          not unlabelled, f"unlabelled={unlabelled[:5]}")

    # 13. historical evidence directory still present
    ev = DOCS / "evidence"
    ev_files = list(ev.rglob("*")) if ev.is_dir() else []
    check("13. historical evidence directory is present",
          ev.is_dir() and len(ev_files) > 100, f"files={len(ev_files)}")

    # 14. STATUS declares the design-language scope
    status = read("STATUS.md")
    check("14. STATUS declares KBDL Design Language v1 scope",
          "KBDL Design Language" in status and "1.0" in status
          and "design language" in status.lower(), "STATUS.md incomplete")

    # 15. tokens documented values match the token file
    tok_doc = read("tokens/README.md")
    space_ok = all(v in tok_doc for v in ("4px", "8px", "16px", "64px"))
    bp_ok = all(v in tok_doc for v in ("600px", "905px", "1280px"))
    check("15. token documentation matches the token file",
          space_ok and bp_ok, "documented scales disagree with kbdl.tokens.json")

    # 16. patterns document covers the required pattern set
    pat = read("patterns.md")
    required_patterns = ["Page structure", "Form layout", "Validation",
                         "Loading", "Empty states", "Destructive confirmation",
                         "Search and filtering", "Theme selection",
                         "Progressive disclosure", "Reduced-motion"]
    absent_pat = [x for x in required_patterns if x not in pat]
    check("16. common experience patterns are documented", not absent_pat,
          f"absent={absent_pat}")

    # 17. adoption guide has both checklists
    ado = read("adoption.md")
    check("17. adoption guide includes designer and developer checklists",
          "Designer checklist" in ado and "Developer checklist" in ado)

    # 18. governance is lean
    gov = read("governance.md")
    gov_flat = flat(gov).lower()
    lean_ok = ("do not require" in gov_flat
               and "evidence package" in gov_flat
               and "stronger review" in gov_flat)
    check("18. governance documents a lightweight change process", lean_ok,
          "governance.md does not describe the lean process")

    # 19. no implementation code was added under docs/kbdl
    code = [p.relative_to(DOCS).as_posix() for ext in ("*.js", "*.ts", "*.tsx",
                                                       "*.jsx", "*.vue", "*.css")
            for p in DOCS.rglob(ext)
            if not p.relative_to(DOCS).as_posix().startswith("evidence/")]
    check("19. no framework or application code added to the design language",
          not code, f"found={code[:5]}")

    # 20. theme guidance covers light and dark selection behaviour
    themes = read("themes/README.md")
    check("20. theme guidance covers light, dark, and selection behaviour",
          all(k in themes.lower() for k in ("light", "dark")),
          "themes/README.md missing light/dark guidance")

    return report()


def report() -> int:
    failed = 0
    for name, ok, detail in results:
        line = f"[{'PASS' if ok else 'FAIL'}] {name}"
        if detail and not ok:
            line += f" -- {detail}"
        print(line)
        failed += 0 if ok else 1
    print("=" * 70)
    print(f"{len(results) - failed}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
