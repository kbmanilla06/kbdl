#!/usr/bin/env python3
"""Generate the SMR1 canonical issue-register.csv rows and reconciliation
ledger from the real R16/R16A evidence artifacts. Read-only w.r.t. R16
inputs; writes only to the new packet directory.
"""
import csv, json
from collections import defaultdict

R16 = "/Users/kbmanilla/Desktop/KBDL/docs/kbdl/evidence/kbdl-011-r16/artifacts"
OUT = "/Users/kbmanilla/Desktop/KBDL/docs/kbdl/evidence/kbdl-011-source-model-resolution"

def rd(name):
    with open(f"{R16}/{name}", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

unresolved = rd("unresolved-field-sources.csv")
exact_loc = rd("exact-location-audit.csv")
std_clause = rd("standard-clause-audit.csv")
defects = rd("defects.csv")
auth_cycle = rd("authority-cycle-audit.csv")
auth_class = rd("authority-reference-classification.csv")

HEADER = ["Resolution issue ID","Category","Requirement ID","Field or relationship",
"Current candidate value","Current candidate source","Permitted authoritative source",
"Authoritative source found","R16 defect category","R16 evidence reference",
"Affected validation gate","Affected effective record","Related requirements",
"Related decisions","Related packet item","Related standard","Current risk",
"Recommended resolution approach","Alternative approaches","Trade-offs",
"Required owner decision","Implementation action potentially unlocked",
"Additional approval required","Owner decision","Owner decision date",
"Owner evidence","Resolution status","Notes"]

GATE_MAP = {
    "Validation classification": "VAL-003; VAL-006",
    "Authority": "VAL-003",
    "Validation evidence": "VAL-004",
    "Validation method": "VAL-004",
    "Known limitation": "VAL-006; VAL-005",
    "Exact location": "VAL-006; VAL-007",
    "Standard clause": "VAL-003",
    "MOT authority edge": "VAL-003",
    "MOT authority cycle": "VAL-003",
}

APPROACH_MAP = {
    "Validation classification": ("PROVIDE ORIGINAL OR APPROVED SOURCE / CONFIRM CURRENT CLASSIFICATION AS NEW CURRENT AUTHORITY / REVISE CLASSIFICATION / SET TO NOT VERIFIED / DEFER DECISION",
        "Confirming current classification as new current authority would be current and non-retroactive; would not reconstruct historical approval; would not prove execution evidence; would not change lifecycle; would require a later recording and validation prompt.",
        "Setting to Not verified is the most conservative alternative and requires no new authority."),
    "Authority": ("PROVIDE ORIGINAL OR APPROVED AUTHORITY / CONFIRM CURRENT NON-RETROACTIVE AUTHORITY / REVISE AUTHORITY EXPRESSION / REJECT AUTHORITY / DEFER DECISION",
        "Lifecycle status, ledger presence, and implementation history are not treated as authority under this packet's source-of-truth hierarchy.",
        "Rejecting the authority expression would require reclassifying dependent requirement text."),
    "Validation evidence": ("PROVIDE ORIGINAL EVIDENCE MANIFEST / CONFIRM SCOPE MAPPING / REVISE EVIDENCE CITATION / SET TO NOT VERIFIED / DEFER DECISION",
        "Owner choices may authorize later evidence work; this packet does not execute it.",
        "Setting to Not verified avoids relying on unscoped shared evidence text."),
    "Validation method": ("PROVIDE ORIGINAL METHOD SOURCE / CONFIRM METHOD AS CURRENT NON-RETROACTIVE / REVISE METHOD / SET TO NOT VERIFIED / DEFER DECISION",
        "Some methods are implementation-dependent or belong to VAL-004's locked scope; execution is out of SMR1 scope regardless of the owner's choice.",
        "Deferring keeps the method unresolved without foreclosing later evidence work."),
    "Known limitation": ("PROVIDE APPROVED LIMITATION SOURCE / CONFIRM CURRENT LIMITATION AS CURRENT NON-RETROACTIVE GOVERNANCE / REVISE LIMITATION / REMOVE UNSUPPORTED LIMITATION / DEFER DECISION",
        "No limitation is accepted through packet preparation; confirming current text as governance would be current and non-retroactive only.",
        "Removing the limitation text without a supporting source risks silently narrowing disclosed scope."),
    "Exact location": ("CONFIRM DERIVED LOCATION / CONFIRM EXISTING LOCATION WITH SOURCE / REVISE LOCATION / PROVIDE ORIGINAL EVIDENCE / DEFER DECISION",
        "Multiple locations may be legitimate (containing section vs. exact subsection); changing either source carries anchor-breakage risk.",
        "Confirming the ledger location over the derived location (or vice versa) both remain live options pending owner review."),
    "Standard clause": ("CONFIRM DIRECT STANDARD AUTHORITY / CLASSIFY AS SUPPORTING GUIDANCE / CLASSIFY AS ANALOGY / REVISE STANDARD REFERENCE / REMOVE UNSUPPORTED REFERENCE / PROVIDE SOURCE EVIDENCE / DEFER DECISION",
        "The current reference is generic only, with no exact governing clause resolved independently; confirming direct authority without evidence risks overclaiming.",
        "Classifying as supporting guidance or analogy preserves some standard linkage without asserting direct authority."),
}

rows = []
seq = defaultdict(int)

def new_id(prefix):
    seq[prefix]+=1
    return f"SMR1-{prefix}-{seq[prefix]:04d}"

# --- 1. unresolved-field-sources.csv driven issues (335) ---
FIELD_PREFIX = {
    "Validation classification":"VC",
    "Authority":"AU",
    "Validation evidence":"VE",
    "Validation method":"VM",
    "Known limitation":"KL",
}
# index limitation-scope-audit and evidence-scope-audit detail for cross reference notes
lim_scope = rd("limitation-scope-audit.csv")
lim_scope_idx = {r["Requirement ID"]: r for r in lim_scope}
evid_scope = rd("evidence-scope-audit.csv")
evid_scope_idx = {r["Requirement ID"]: r for r in evid_scope}
evid_scope_rel_reqs = set(r["Requirement ID"] for r in defects if r["Category"]=="EVIDENCE_SCOPE_RELATIONSHIP")
limitation_mismatch_reqs = set(r["Requirement ID"] for r in defects if r["Category"]=="LIMITATION_MISMATCH")

for r in unresolved:
    field = r["Field"]
    prefix = FIELD_PREFIX[field]
    reqid = r["Requirement ID"]
    approach, tradeoffs_extra, alt = APPROACH_MAP[field]
    notes = ""
    if field == "Validation evidence" and reqid in evid_scope_rel_reqs:
        notes = "Shared with R16 EVIDENCE_SCOPE_RELATIONSHIP finding: resolved artifact does not name this requirement or an approved shared validation scope (evidence-scope-audit.csv)."
    if field == "Known limitation" and reqid in limitation_mismatch_reqs:
        ls = lim_scope_idx.get(reqid, {})
        notes = (notes + " " if notes else "") + f"Shared with R16 LIMITATION_MISMATCH finding: derived Not-verified/excluded scope = '{ls.get('Derived Not-verified/excluded scope','')}'; exact normalized scope overlap = '{ls.get('Exact normalized scope overlap','')}' (limitation-scope-audit.csv)."
    rows.append({
        "Resolution issue ID": new_id(prefix),
        "Category": field,
        "Requirement ID": reqid,
        "Field or relationship": field,
        "Current candidate value": r["Current candidate value"],
        "Current candidate source": r["Candidate source"],
        "Permitted authoritative source": r["Permitted authoritative source type"],
        "Authoritative source found": r["Authoritative source found"],
        "R16 defect category": r["Defect category"],
        "R16 evidence reference": "unresolved-field-sources.csv" + (" ; evidence-scope-audit.csv" if field=="Validation evidence" and reqid in evid_scope_rel_reqs else "") + (" ; limitation-scope-audit.csv" if field=="Known limitation" and reqid in limitation_mismatch_reqs else ""),
        "Affected validation gate": GATE_MAP[field],
        "Affected effective record": reqid,
        "Related requirements": "",
        "Related decisions": "",
        "Related packet item": "",
        "Related standard": "",
        "Current risk": r["Reason unresolved"],
        "Recommended resolution approach": "No approach recommended; options only: " + approach,
        "Alternative approaches": alt,
        "Trade-offs": tradeoffs_extra + " Prohibited automatic correction: " + r["Prohibited automatic correction"] + ".",
        "Required owner decision": r["Owner decision required"],
        "Implementation action potentially unlocked": f"A future recording/validation prompt for {reqid}'s {field.lower()} field, only after an explicit owner decision and separate validation.",
        "Additional approval required": "Planning-agent validation of the recorded decision before any implementation action.",
        "Owner decision": "PENDING",
        "Owner decision date": "PENDING",
        "Owner evidence": "PENDING",
        "Resolution status": "SOURCE EVIDENCE REQUIRED" if r["Authoritative source found"]=="None" else "CURRENT AUTHORITY DECISION REQUIRED",
        "Notes": notes,
    })

# --- 2. exact-location mismatches (63) ---
for r in exact_loc:
    if r["Result"] == "PASS":
        continue
    reqid = r["Requirement ID"]
    approach, tradeoffs_extra, alt = APPROACH_MAP["Exact location"]
    rows.append({
        "Resolution issue ID": new_id("LOC"),
        "Category": "Exact location",
        "Requirement ID": reqid,
        "Field or relationship": "Specification location",
        "Current candidate value": r["Ledger location"],
        "Current candidate source": "field-source-registry.csv ledger value",
        "Permitted authoritative source": "Normative requirement location / approved multi-location rule",
        "Authoritative source found": "None" if r["Exact comparison"] != "True" else "Partial",
        "R16 defect category": "LOCATION_MISMATCH",
        "R16 evidence reference": "exact-location-audit.csv",
        "Affected validation gate": GATE_MAP["Exact location"],
        "Affected effective record": reqid,
        "Related requirements": "",
        "Related decisions": "",
        "Related packet item": "",
        "Related standard": "",
        "Current risk": (f"Containing normative location = '{r['Containing normative location']}'; explicit normative location = '{r['Explicit normative location']}'; "
                          f"readable-group supported locations = '{r['Readable-group supported locations']}'; exact expected locations = '{r['Exact expected locations']}'; "
                          f"all anchors resolve = {r['All anchors resolve']}; exact comparison = {r['Exact comparison']}."),
        "Recommended resolution approach": "No approach recommended; options only: " + approach,
        "Alternative approaches": alt,
        "Trade-offs": tradeoffs_extra,
        "Required owner decision": "Confirm which location is authoritative for this requirement, or supply original evidence.",
        "Implementation action potentially unlocked": f"A future exact-location correction prompt for {reqid}, only after an explicit owner decision and separate validation.",
        "Additional approval required": "Planning-agent validation of the recorded decision before any implementation action.",
        "Owner decision": "PENDING",
        "Owner decision date": "PENDING",
        "Owner evidence": "PENDING",
        "Resolution status": "VALUE REVISION DECISION REQUIRED",
        "Notes": "",
    })

# --- 3. standard-clause mismatches (20, from defects.csv MISSING_STANDARD_BASIS reqs) ---
std_defect_reqs = [r["Requirement ID"] for r in defects if r["Category"]=="MISSING_STANDARD_BASIS"]
std_idx = {r["Requirement ID"]: r for r in std_clause}
for reqid in std_defect_reqs:
    r = std_idx[reqid]
    approach, tradeoffs_extra, alt = APPROACH_MAP["Standard clause"]
    rows.append({
        "Resolution issue ID": new_id("SC"),
        "Category": "Standard clause",
        "Requirement ID": reqid,
        "Field or relationship": "Standard-clause authority",
        "Current candidate value": r["Candidate standard citations"],
        "Current candidate source": "field-source-registry.csv / requirement text",
        "Permitted authoritative source": "Adopted standard (exact clause) / Approved decision",
        "Authoritative source found": r["Normative governing citations"],
        "R16 defect category": "MISSING_STANDARD_BASIS; STANDARD_CLAUSE_MISMATCH",
        "R16 evidence reference": "standard-clause-audit.csv ; adopted-standard-clause-audit.csv",
        "Affected validation gate": GATE_MAP["Standard clause"],
        "Affected effective record": reqid,
        "Related requirements": "",
        "Related decisions": "",
        "Related packet item": "",
        "Related standard": r["Candidate standard citations"],
        "Current risk": f"Direct-or-supporting classification currently recorded as '{r['Direct or supporting']}' with no independently resolved exact clause (Result={r['Result']}).",
        "Recommended resolution approach": "No approach recommended; options only: " + approach,
        "Alternative approaches": alt,
        "Trade-offs": tradeoffs_extra,
        "Required owner decision": "Confirm, revise, or remove this generic standard reference.",
        "Implementation action potentially unlocked": f"A future exact-clause citation correction prompt for {reqid}, only after an explicit owner decision and separate validation.",
        "Additional approval required": "Planning-agent validation of the recorded decision before any implementation action.",
        "Owner decision": "PENDING",
        "Owner decision date": "PENDING",
        "Owner evidence": "PENDING",
        "Resolution status": "SOURCE EVIDENCE REQUIRED",
        "Notes": "R16 recorded this as two defect rows (MISSING_STANDARD_BASIS and STANDARD_CLAUSE_MISMATCH) for the same requirement; this is one canonical issue documented as a shared finding.",
    })

# --- 4. MOT cycle: 2 edge issues + 1 cycle issue ---
mot_edge_text = {
    ("KBDL-MOT-007","KBDL-MOT-008"): auth_cycle[0],
    ("KBDL-MOT-008","KBDL-MOT-007"): auth_cycle[1],
}
for (src,tgt), r in mot_edge_text.items():
    rows.append({
        "Resolution issue ID": new_id("MOTEDGE"),
        "Category": "MOT authority edge",
        "Requirement ID": src,
        "Field or relationship": f"Authority edge {src} -> {tgt}",
        "Current candidate value": r["Exact authority text"],
        "Current candidate source": r["Source path and section"],
        "Permitted authoritative source": "Approved decision (KBDL-DEC-014) / independent shared authority",
        "Authoritative source found": "KBDL-DEC-014 (decision packet item 2) — cites the paired requirement together with the decision, producing a two-node cycle when both directions are read as full authority",
        "R16 defect category": "CIRCULAR_AUTHORITY",
        "R16 evidence reference": "authority-cycle-audit.csv ; authority-graph-audit.csv ; motion/README.md #10-motion-decision-packet",
        "Affected validation gate": GATE_MAP["MOT authority edge"],
        "Affected effective record": src,
        "Related requirements": tgt,
        "Related decisions": "KBDL-DEC-014",
        "Related packet item": "motion/README.md #10-motion-decision-packet, item 2",
        "Related standard": "",
        "Current risk": f"Edge classification currently recorded as '{r['Edge classification']}'; classification basis: '{r['Classification basis']}'; target lifecycle: '{r['Target lifecycle']}'. Status: {r['Status']}.",
        "Recommended resolution approach": "No approach recommended; independent per-edge options only: AUTHORITY EDGE / SUPPORTING AUTHORITY / CONTEXT-ONLY / RELATED REQUIREMENT / REMOVE OR REVISE RELATIONSHIP / PROVIDE ORIGINAL EVIDENCE / DEFER DECISION",
        "Alternative approaches": "Classifying this edge independently of the other edge (e.g. as Related requirement or Context-only) may break the cycle without requiring new authority evidence.",
        "Trade-offs": "Reclassifying downward (e.g. to Context-only) could remove this edge's contribution to KBDL-MOT-007/008's approved authority, requiring a separate authority-sufficiency review for the affected requirement.",
        "Required owner decision": f"Classify the {src} -> {tgt} authority edge independently of the {tgt} -> {src} edge.",
        "Implementation action potentially unlocked": "A future MOT-007/MOT-008 authority-graph correction prompt, only after both edges and the cycle-level decision are recorded and validated.",
        "Additional approval required": "Planning-agent validation of the recorded decision before any implementation action.",
        "Owner decision": "PENDING",
        "Owner decision date": "PENDING",
        "Owner evidence": "PENDING",
        "Resolution status": "RELATIONSHIP CLASSIFICATION REQUIRED",
        "Notes": "Reviewed together with the paired edge and the cycle-level record; not a bulk decision.",
    })

rows.append({
    "Resolution issue ID": new_id("MOTCYCLE"),
    "Category": "MOT authority cycle",
    "Requirement ID": "KBDL-MOT-007; KBDL-MOT-008",
    "Field or relationship": "Authority cycle KBDL-MOT-007 -> KBDL-MOT-008 -> KBDL-MOT-007",
    "Current candidate value": "Both requirements are Approved per KBDL-DEC-014, decision packet item 2, treating timing architecture (MOT-007) and duration recommendations (MOT-008) as one timing system; each requirement's authority expression names the other requirement together with the decision.",
    "Current candidate source": "motion/README.md #396-421 (KBDL-MOT-007, KBDL-MOT-008 requirement blocks); motion/timing-easing.md #1-timing-architecture, #2-duration-recommendations",
    "Permitted authoritative source": "Approved decision / AR2 current-authority confirmation / new current project-owner authority",
    "Authoritative source found": "KBDL-DEC-014 exists and is Approved, but the two-requirement mutual citation forms a two-node authority cycle when each edge is read as complete, independent authority",
    "R16 defect category": "CIRCULAR_AUTHORITY",
    "R16 evidence reference": "authority-cycle-audit.csv (both rows) ; authority-graph-audit.csv ; decision-register.md #kbdl-dec-014--kbdl-005-motion-decisions-approved",
    "Affected validation gate": GATE_MAP["MOT authority cycle"],
    "Affected effective record": "KBDL-MOT-007; KBDL-MOT-008",
    "Related requirements": "KBDL-MOT-009; KBDL-MOT-033 (share the same decision packet item context)",
    "Related decisions": "KBDL-DEC-014",
    "Related packet item": "motion/README.md #10-motion-decision-packet, item 2",
    "Related standard": "",
    "Current risk": "VAL-003 (lifecycle/authority integrity) requires every Approved requirement to have valid, non-circular authority; an unresolved cycle keeps VAL-003 Not verified for the whole project, not only for these two requirements.",
    "Recommended resolution approach": ("No cycle-level resolution is recommended or preselected. Independent cycle-level options only: "
        "break cycle via MOT-007 edge revision / break cycle via MOT-008 edge revision / replace both edges with shared independent authority "
        "(e.g. treat KBDL-DEC-014 alone, without the paired-requirement citation, as sufficient authority for each) / preserve the cycle and keep VAL-003 Not verified / "
        "provide original governance evidence that resolves the cycle without reclassification."),
    "Alternative approaches": "Preserving the cycle and keeping VAL-003 Not verified requires no new decision and keeps the current, disclosed BLOCKED status.",
    "Trade-offs": "Any edge revision changes graph-derived authority classification for KBDL-MOT-007 and/or KBDL-MOT-008 and must be independently re-validated; it does not, by itself, change either requirement's Approved lifecycle status.",
    "Required owner decision": "Select one cycle-level disposition after reviewing both edge decisions above; do not select an edge or the cycle disposition in bulk.",
    "Implementation action potentially unlocked": "A future KBDL-011 prompt to correct the authority-graph representation for KBDL-MOT-007/MOT-008 and re-run the source-independent audit, only after this decision is recorded and separately validated.",
    "Additional approval required": "Planning-agent validation of the recorded decision before any implementation action; the work remains additionally blocked by VAL-004's locked scope for any clause-level evidence implications.",
    "Owner decision": "PENDING",
    "Owner decision date": "PENDING",
    "Owner evidence": "PENDING",
    "Resolution status": "CONFLICTING SOURCES",
    "Notes": "This is the single, prominent cycle-level review record required by SMR1 section 10; it is separate from, and must be reviewed together with, the two edge-level records above.",
})

with open(f"{OUT}/artifacts/issue-register-generated.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HEADER)
    w.writeheader()
    for row in rows:
        w.writerow(row)

print("total rows:", len(rows))
cat_counts = defaultdict(int)
for r in rows:
    cat_counts[r["Category"]] += 1
print(json.dumps(cat_counts, indent=2))

# sanity: every owner decision literally PENDING
assert all(r["Owner decision"]=="PENDING" for r in rows)
assert all(r["Owner decision date"]=="PENDING" for r in rows)
assert all(r["Owner evidence"]=="PENDING" for r in rows)
# unique IDs
ids = [r["Resolution issue ID"] for r in rows]
assert len(ids)==len(set(ids))
print("All owner-decision fields literally PENDING:", True)
print("All resolution IDs unique:", True)
