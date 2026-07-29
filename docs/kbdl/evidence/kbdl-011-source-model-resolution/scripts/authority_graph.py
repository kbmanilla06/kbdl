#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-AGC1 authority-graph consistency module.

Parses the *current* authoritative source model for KBDL-MOT-007 and
KBDL-MOT-008 out of `docs/kbdl/motion/README.md` and
`docs/kbdl/traceability-metadata.csv`, and verifies the Batch H
authority-graph correction: each requirement's authority is
independently `KBDL-DEC-014, decision packet item 2`; the relationship
between the two requirements is `RELATED REQUIREMENT` only, in both
directions; and no directional authority edge (and therefore no
two-node authority cycle) exists between them.

This module is read-only with respect to the real repository: callers
pass it file contents (or file paths to read), and it never writes
anything. `authority_graph_fixtures.py` uses it against temporary,
deliberately-mutated copies of the two source files.
"""
import csv
import re

MOT007_BLOCK_RE = re.compile(
    r"- \*\*KBDL-MOT-007\*\*.*?(?=\n- \*\*KBDL-MOT-008\*\*)", re.DOTALL)
MOT008_BLOCK_RE = re.compile(
    r"- \*\*KBDL-MOT-008\*\*.*?(?=\n- \*\*KBDL-MOT-009\*\*|\n### )", re.DOTALL)

AUTHORITY_LINE_RE = re.compile(r"Lifecycle status:\s*(.*?)(?=\n\s*- )", re.DOTALL)
RELATED_REQ_LINE_RE = re.compile(r"Related requirement:\s*`(KBDL-MOT-\d+)`\s*—\s*(.*?)(?=\n\s*- )", re.DOTALL)
VALIDATION_STATUS_RE = re.compile(r"Validation\s+status:\s*(.*?)(?=\n\s*- |\.\s|\Z)", re.DOTALL)


def _extract_block(text, req_id):
    if req_id == "KBDL-MOT-007":
        m = MOT007_BLOCK_RE.search(text)
    elif req_id == "KBDL-MOT-008":
        m = MOT008_BLOCK_RE.search(text)
    else:
        raise ValueError(req_id)
    return m.group(0) if m else ""


def parse_readme_state(readme_text):
    """Returns dict: req_id -> {authority_text, related_req_id,
    related_req_text, lifecycle, validation_status}."""
    out = {}
    for req_id in ("KBDL-MOT-007", "KBDL-MOT-008"):
        block = _extract_block(readme_text, req_id)
        auth_m = AUTHORITY_LINE_RE.search(block)
        authority_text = " ".join(auth_m.group(1).split()) if auth_m else ""
        rel_m = RELATED_REQ_LINE_RE.search(block)
        related_req_id = rel_m.group(1) if rel_m else None
        related_req_text = " ".join(rel_m.group(2).split()) if rel_m else ""
        lifecycle = "Approved" if authority_text.startswith("Approved") else authority_text.split(".")[0]
        vs_m = VALIDATION_STATUS_RE.search(block)
        validation_status = vs_m.group(1).strip() if vs_m else ""
        out[req_id] = {
            "authority_text": authority_text,
            "related_req_id": related_req_id,
            "related_req_text": related_req_text,
            "lifecycle": lifecycle,
            "validation_status": validation_status,
            "block": block,
        }
    return out


def parse_traceability_csv_state(csv_path_or_rows):
    if isinstance(csv_path_or_rows, str):
        with open(csv_path_or_rows, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    else:
        rows = csv_path_or_rows
    out = {}
    for row in rows:
        rid = row.get("Requirement ID")
        if rid in ("KBDL-MOT-007", "KBDL-MOT-008"):
            out[rid] = {
                "authority": row.get("Authority", ""),
                "authority_targets": row.get("Authority targets", ""),
                "lifecycle_status": row.get("Lifecycle status", ""),
                "validation_classification": row.get("Validation classification", ""),
                "notes": row.get("Notes or exclusions", ""),
            }
    return out


def _authority_is_independent(authority_text):
    """True if the authority expression cites KBDL-DEC-014 item 2 and
    does NOT embed the other MOT requirement inside the authority claim
    itself (e.g. 'together with KBDL-MOT-008')."""
    if "KBDL-DEC-014" not in authority_text:
        return False, "does not cite KBDL-DEC-014"
    if "decision packet item 2" not in authority_text and "decision-packet item 2" not in authority_text:
        return False, "does not cite decision packet item 2"
    if "KBDL-MOT-007" in authority_text or "KBDL-MOT-008" in authority_text:
        return False, "authority expression embeds the other MOT requirement (authority edge)"
    return True, ""


def check_authority_graph(readme_state, csv_state):
    """Returns list of (check_name, passed, detail) tuples covering the
    13 AGC1 regression classes plus the core AC-003..AC-007 assertions."""
    results = []

    def add(name, cond, detail=""):
        results.append((name, bool(cond), detail))

    for rid in ("KBDL-MOT-007", "KBDL-MOT-008"):
        other = "KBDL-MOT-008" if rid == "KBDL-MOT-007" else "KBDL-MOT-007"
        r = readme_state.get(rid, {})
        c = csv_state.get(rid, {})

        ok, why = _authority_is_independent(r.get("authority_text", ""))
        add(f"AG.{rid}.readme_independent_authority", ok, why)

        csv_authority = c.get("authority", "")
        ok, why = _authority_is_independent(csv_authority)
        add(f"AG.{rid}.csv_independent_authority", ok, why)

        # relationship must be RELATED REQUIREMENT only, both directions
        add(f"AG.{rid}.related_requirement_present",
            r.get("related_req_id") == other,
            f"expected related requirement {other}, found {r.get('related_req_id')}")
        rel_text = (r.get("related_req_text") or "").lower()
        add(f"AG.{rid}.related_requirement_not_authority",
            "authority" not in rel_text.split("not authority")[0].replace("not authority", "")
            and "not authority" in rel_text,
            "related-requirement note must explicitly disclaim authority semantics")

        # no authority edge in either direction (readme prose form)
        add(f"AG.{rid}.no_authority_edge_to_{other}",
            f"authority of {other}" not in r.get("block", "").lower()
            and "grants" not in r.get("block", "").lower()
            and "supplies" not in r.get("block", "").lower(),
            "no wording implying the related requirement grants/supplies authority")

    # cross-check readme and csv agree
    for rid in ("KBDL-MOT-007", "KBDL-MOT-008"):
        add(f"AG.{rid}.readme_csv_agree",
            _authority_is_independent(readme_state.get(rid, {}).get("authority_text", ""))[0]
            == _authority_is_independent(csv_state.get(rid, {}).get("authority", ""))[0],
            "README and traceability-metadata.csv authority representations must agree")

    # validation status must not change (regression class #8)
    v7 = readme_state.get("KBDL-MOT-007", {}).get("validation_status", "").strip()
    add("AG.KBDL-MOT-007.validation_status_unchanged", v7 == "Not verified",
        f"expected 'Not verified', found {v7!r}")
    v8 = readme_state.get("KBDL-MOT-008", {}).get("validation_status", "").strip()
    add("AG.KBDL-MOT-008.validation_status_unchanged", v8.startswith("Not applicable"),
        f"expected to start with 'Not applicable', found {v8!r}")
    c7 = csv_state.get("KBDL-MOT-007", {}).get("validation_classification", "")
    add("AG.csv.KBDL-MOT-007.validation_classification_unchanged", c7 == "Not verified",
        f"expected 'Not verified', found {c7!r}")
    c8 = csv_state.get("KBDL-MOT-008", {}).get("validation_classification", "")
    add("AG.csv.KBDL-MOT-008.validation_classification_unchanged", c8 == "Not applicable",
        f"expected 'Not applicable', found {c8!r}")

    return results


def cycle_exists(readme_state):
    """A two-node authority cycle exists iff both directions are
    independent-authority-failing in a way that shows the other
    requirement embedded as authority (i.e. the pre-correction defect)."""
    a = readme_state.get("KBDL-MOT-007", {})
    b = readme_state.get("KBDL-MOT-008", {})
    a_embeds_b = "KBDL-MOT-008" in a.get("authority_text", "")
    b_embeds_a = "KBDL-MOT-007" in b.get("authority_text", "")
    return a_embeds_b and b_embeds_a
