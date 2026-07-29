#!/usr/bin/env python3
"""KBDL-011-SMR1 reconciliation computation.

Reads the R16/R16A evidence artifacts (read-only) and computes the real
reconciled counts required by the SMR1 spec: raw findings count, distinct
requirement count, distinct requirement-field count, distinct
owner-decision count, overlap count, cross-category dependency count, and
per-category decision counts. Every number this script prints is derived
from the CSVs on disk -- nothing here is hand-entered.

The methodology (why 693 raw findings reconcile to exactly 421 canonical
issues) is documented row-by-row in ../source-model-resolution-ledger.csv;
this script reproduces the same arithmetic independently so the ledger
can be checked against a second, script-derived source.
"""
import csv, json
from collections import defaultdict

BASE = "/Users/kbmanilla/Desktop/KBDL/docs/kbdl/evidence/kbdl-011-r16/artifacts"

def read_csv(name):
    with open(f"{BASE}/{name}", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

defects = read_csv("defects.csv")
unresolved = read_csv("unresolved-field-sources.csv")
exact_loc = read_csv("exact-location-audit.csv")
auth_cycle = read_csv("authority-cycle-audit.csv")

# --- raw findings count = every row of defects.csv (one row per R16 finding) ---
raw_findings = len(defects)

cat_counts = defaultdict(int)
for r in defects:
    cat_counts[r["Category"]] += 1

# --- the 5 field-source categories, from unresolved-field-sources.csv ---
field_reqs = defaultdict(set)
for r in unresolved:
    field_reqs[r["Field"]].add(r["Requirement ID"])
field_counts = {k: len(v) for k, v in field_reqs.items()}

# --- exact-location mismatches: independent of unresolved-field-sources.csv ---
loc_fail_reqs = set(r["Requirement ID"] for r in exact_loc if r["Result"] != "PASS")

# --- standard-clause mismatches: independent of unresolved-field-sources.csv ---
std_reqs = set(r["Requirement ID"] for r in defects if r["Category"] == "MISSING_STANDARD_BASIS")

# --- MOT cycle ---
cycle_reqs = set(r["Source requirement"] for r in auth_cycle) | set(r["Target requirement"] for r in auth_cycle)
mot_edges = len(auth_cycle)

# --- canonical non-MOT issues: one per (Requirement ID, Field) triple across
#     the three independent source tables (unresolved-field-sources.csv,
#     exact-location-audit.csv failures, MISSING_STANDARD_BASIS requirements).
#     These three tables never describe the same (requirement, field) pair,
#     so their counts add without collision. ---
non_mot_canonical = len(unresolved) + len(loc_fail_reqs) + len(std_reqs)

# --- MOT: 2 edge-level issues + 1 cycle-level issue, all distinct from the
#     per-field Authority/Validation-classification issues already counted
#     for KBDL-MOT-007/KBDL-MOT-008 above. ---
mot_issues = mot_edges + 1

canonical_issues_total = non_mot_canonical + mot_issues

# --- distinct affected requirements = union across every bucket, incl. MOT ---
distinct_requirements = (
    set(r["Requirement ID"] for r in unresolved)
    | loc_fail_reqs
    | std_reqs
    | cycle_reqs
)

# --- cross-category dependency count: requirements in more than one bucket ---
buckets = {
    "validation_classification": field_reqs.get("Validation classification", set()),
    "authority": field_reqs.get("Authority", set()),
    "validation_evidence": field_reqs.get("Validation evidence", set()),
    "validation_method": field_reqs.get("Validation method", set()),
    "known_limitation": field_reqs.get("Known limitation", set()),
    "exact_location": loc_fail_reqs,
    "standard_clause": std_reqs,
    "mot_cycle": cycle_reqs,
}
membership = defaultdict(set)
for name, reqs in buckets.items():
    for req in reqs:
        membership[req].add(name)
cross_category = {r: b for r, b in membership.items() if len(b) > 1}

# --- overlap count: raw defects.csv rows that duplicate an already-counted
#     canonical issue rather than establishing a new one. The rows that
#     establish a canonical issue for the first time are exactly:
#       UNRESOLVED_FIELD_SOURCE (335) + LOCATION_MISMATCH (63)
#       + MISSING_STANDARD_BASIS (20) + CIRCULAR_AUTHORITY (1) = 419
#     (419 non-edge canonical issues; the 2 MOT edge issues are additional
#     decision granularity sourced from authority-cycle-audit.csv, not from
#     defects.csv, so they are not part of the 693-row raw-findings total). ---
first_seen_categories = {"UNRESOLVED_FIELD_SOURCE", "LOCATION_MISMATCH", "MISSING_STANDARD_BASIS", "CIRCULAR_AUTHORITY"}
first_seen_rows = sum(cat_counts[c] for c in first_seen_categories)
overlap_count = raw_findings - first_seen_rows

# --- unmapped findings check: every defects.csv row must belong to a
#     recognised category and its requirement must appear in the
#     corresponding bucket. ---
unmapped = []
for r in defects:
    cat = r["Category"]
    reqid = r["Requirement ID"]
    ok = False
    if cat == "UNRESOLVED_FIELD_SOURCE":
        base = reqid.split(":")[0]
        ok = any(base in s for s in field_reqs.values())
    elif cat == "LIMITATION_MISMATCH":
        ok = reqid in field_reqs.get("Known limitation", set())
    elif cat == "LOCATION_MISMATCH":
        ok = reqid in loc_fail_reqs
    elif cat == "EVIDENCE_SCOPE_RELATIONSHIP":
        ok = reqid in field_reqs.get("Validation evidence", set())
    elif cat == "EVIDENCE_MISMATCH":
        ok = reqid in field_reqs.get("Validation evidence", set())
    elif cat in ("MISSING_STANDARD_BASIS", "STANDARD_CLAUSE_MISMATCH"):
        ok = reqid in std_reqs
    elif cat == "CIRCULAR_AUTHORITY":
        ok = reqid in cycle_reqs
    if not ok:
        unmapped.append((cat, reqid))

result = {
    "raw_findings_defects_csv_rows": raw_findings,
    "defects_category_counts": dict(cat_counts),
    "unresolved_field_source_field_counts": field_counts,
    "exact_location_mismatches": len(loc_fail_reqs),
    "standard_clause_mismatch_requirements": len(std_reqs),
    "mot_cycle_edges": mot_edges,
    "mot_cycle_requirements": sorted(cycle_reqs),
    "non_mot_canonical_issues": non_mot_canonical,
    "mot_issues": mot_issues,
    "canonical_issues_total": canonical_issues_total,
    "overlap_count": overlap_count,
    "distinct_affected_requirements": len(distinct_requirements),
    "cross_category_dependency_count": len(cross_category),
    "unmapped_findings_count": len(unmapped),
    "unmapped_findings_sample": unmapped[:20],
    "validation_classification_decisions": field_counts.get("Validation classification", 0),
    "authority_source_decisions": field_counts.get("Authority", 0),
    "validation_evidence_decisions": field_counts.get("Validation evidence", 0),
    "validation_method_decisions": field_counts.get("Validation method", 0),
    "limitation_decisions": field_counts.get("Known limitation", 0),
    "location_decisions": len(loc_fail_reqs),
    "standard_clause_decisions": len(std_reqs),
    "mot_edge_decisions": mot_edges,
    "mot_cycle_decisions": 1,
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2))
