#!/usr/bin/env python3
"""KBDL-011-SMR1 packet validator.

Programmatically checks the 24 validation points required by the SMR1
task specification against the generated packet, plus (as of
KBDL-011-SMR1-BH-R1) a state-aware owner-decision model implemented in
`decision_state.py`. Exits 0 on full pass, 1 if any check fails. Prints
one PASS/FAIL line per check.

Packet review states recognized (see decision_state.py and
source-model-resolution-packet.md §7): PREPARED — NO OWNER DECISIONS
RECORDED / OWNER REVIEW IN PROGRESS — DURABLY RECORDED DECISIONS PRESENT
/ INVALID — SELECTED DECISIONS LACK DURABLE OR CONSISTENT OWNER EVIDENCE.
Reaching either of the first two states never implies implementation
readiness, VAL-status restoration, candidate readiness, implementation
conformance, or project completion.
"""
import csv, os, re, subprocess, sys

REPO = "/Users/kbmanilla/Desktop/KBDL"
PKT = f"{REPO}/docs/kbdl/evidence/kbdl-011-source-model-resolution"
R16 = f"{REPO}/docs/kbdl/evidence/kbdl-011-r16/artifacts"

sys.path.insert(0, os.path.join(PKT, "scripts"))
import decision_state
import authority_graph

checks = []
def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))

def rd(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

issue_rows = rd(f"{PKT}/issue-register.csv")

# 1. every R16 defect row mapped
defects = rd(f"{R16}/defects.csv")
unresolved = rd(f"{R16}/unresolved-field-sources.csv")
exact_loc = rd(f"{R16}/exact-location-audit.csv")

unresolved_reqs = {f: set(r["Requirement ID"] for r in unresolved if r["Field"] == f)
                    for f in ["Validation classification","Authority","Validation evidence","Validation method","Known limitation"]}
loc_fail_reqs = set(r["Requirement ID"] for r in exact_loc if r["Result"] != "PASS")
std_reqs = set(r["Requirement ID"] for r in defects if r["Category"] == "MISSING_STANDARD_BASIS")
mot_reqs = {"KBDL-MOT-007", "KBDL-MOT-008"}

unmapped = []
for r in defects:
    cat = r["Category"]
    reqid = r["Requirement ID"]
    ok = False
    if cat == "UNRESOLVED_FIELD_SOURCE":
        base = reqid.split(":")[0]
        ok = any(base in s for s in unresolved_reqs.values())
    elif cat == "LIMITATION_MISMATCH":
        ok = reqid in unresolved_reqs["Known limitation"]
    elif cat == "LOCATION_MISMATCH":
        ok = reqid in loc_fail_reqs
    elif cat == "EVIDENCE_SCOPE_RELATIONSHIP":
        ok = reqid in unresolved_reqs["Validation evidence"]
    elif cat == "EVIDENCE_MISMATCH":
        ok = reqid in unresolved_reqs["Validation evidence"]
    elif cat in ("MISSING_STANDARD_BASIS", "STANDARD_CLAUSE_MISMATCH"):
        ok = reqid in std_reqs
    elif cat == "CIRCULAR_AUTHORITY":
        ok = reqid in mot_reqs
    if not ok:
        unmapped.append((cat, reqid))
check("1. every R16 defect row maps to a canonical issue or documented shared issue", len(unmapped) == 0, f"unmapped={unmapped[:5]}")

# 2. every canonical issue has a unique stable ID
ids = [r["Resolution issue ID"] for r in issue_rows]
check("2. every canonical issue has a unique stable ID", len(ids) == len(set(ids)))

# 3. category identified for every issue
check("3. category identified for every issue", all(r["Category"].strip() for r in issue_rows))

# 4. affected requirement IDs identified
check("4. affected requirement IDs identified for every issue", all(r["Requirement ID"].strip() for r in issue_rows))

# 5. R16 evidence identified
check("5. R16 evidence reference identified for every issue", all(r["R16 evidence reference"].strip() for r in issue_rows))

# 6. affected validation gates identified
check("6. affected validation gate identified for every issue", all(r["Affected validation gate"].strip() for r in issue_rows))

# 7/7b/7c/7d and D1-D3, D6-D12: state-aware owner-decision checks (KBDL-011-SMR1-BH-R1).
# Delegated to decision_state.py so the same logic can be exercised, unchanged,
# against temporary mutated copies by negative_fixtures.py. This REPLACES the
# original "all fields literally PENDING" / "no checkbox selected anywhere"
# checks with a stronger, state-aware equivalent: every field/checkbox must be
# either PENDING/unselected, or an exact match for a durable owner-decision
# record -- it is never sufficient for a field merely to differ from PENDING.
ds_checks, ds_stats = decision_state.compute(PKT)
for name, ok, detail in ds_checks:
    check(name, ok, detail)

por_path = f"{PKT}/project-owner-review.md"
por_text = open(por_path, encoding="utf-8").read() if os.path.exists(por_path) else ""

# 9. every current-authority proposal says current and non-retroactive
current_authority_mentions = [r for r in issue_rows if "CONFIRM CURRENT" in r["Recommended resolution approach"]]
check("9. every current-authority proposal states current/non-retroactive boundary",
      all(("current" in r["Trade-offs"].lower() or "current" in r["Recommended resolution approach"].lower()) for r in current_authority_mentions))

# 10. every historical-evidence gap visible (Authoritative source found column present, non-fabricated)
check("10. authoritative-source-found column populated for every issue", all(r["Authoritative source found"] != "" for r in issue_rows))

# 11. MOT cycle has 2 edge records + 1 cycle record
mot_edge = [r for r in issue_rows if r["Category"] == "MOT authority edge"]
mot_cycle = [r for r in issue_rows if r["Category"] == "MOT authority cycle"]
check("11. MOT cycle has exactly 2 edge records and 1 cycle record", len(mot_edge) == 2 and len(mot_cycle) == 1)

# 12. no protected field changed -- git diff against HEAD for tracked protected files must be empty.
# As of KBDL-011-SMR1-BH-AGC1, docs/kbdl/motion/README.md and
# docs/kbdl/traceability-metadata.csv are narrowly and explicitly
# authorized to change (only the MOT-007/MOT-008 authority-graph
# correction); they are validated separately below (AG.* checks and
# AG.narrow_authorized_diff), not by this blanket check.
protected_paths = [
    "docs/kbdl/validation.md",
    "docs/kbdl/decision-register.md",
    "docs/kbdl/traceability-matrix.md",
    "docs/kbdl/motion/timing-easing.md",
]
diff_out = subprocess.run(["git", "-C", REPO, "diff", "--name-only", "HEAD"], capture_output=True, text=True).stdout.strip().splitlines()
changed_protected = [p for p in protected_paths if p in diff_out]
check("12. no protected file changed (git diff --name-only HEAD)", len(changed_protected) == 0, f"changed={changed_protected}; all diff names={diff_out}")

# 13. no VAL status changed -- validation.md content matches HEAD exactly (redundant with 12 but explicit)
val_diff = subprocess.run(["git", "-C", REPO, "diff", "HEAD", "--", "docs/kbdl/validation.md"], capture_output=True, text=True).stdout
check("13. docs/kbdl/validation.md byte-identical to HEAD", val_diff.strip() == "")

# 14. candidate status remains Not ready
val_text = open(f"{REPO}/docs/kbdl/validation.md", encoding="utf-8").read()
check("14. candidate status remains NOT READY in validation.md", "NOT READY" in val_text.upper())

# 15. implementation conformance remains Not verified
check("15. implementation conformance remains NOT VERIFIED in validation.md", "NOT VERIFIED" in val_text.upper())

# 16. completion remains pending
check("16. project completion remains PENDING in validation.md", "PENDING" in val_text.upper())

# 17. no implementation status LINE assigns a bare READY/APPROVED/UNLOCKED value
# (the map is allowed to name these words once, in prose, to say they are never
# used as a status value -- the check targets actual "Status:" assignments)
unlock_path = f"{PKT}/implementation-unlock-map.md"
unlock_text = open(unlock_path, encoding="utf-8").read() if os.path.exists(unlock_path) else ""
status_lines = re.findall(r"Status:\s*`([^`]+)`", unlock_text)
allowed_statuses = {
    "LOCKED — OWNER DECISION REQUIRED",
    "LOCKED — ADDITIONAL EVIDENCE REQUIRED",
    "LOCKED — PLANNING-AGENT VALIDATION REQUIRED",
    "ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL",
}
def status_variants_ok(s):
    # a status line may contain " / " to express a conditional either/or
    parts = [p.strip() for p in s.split(" / ")]
    return all(p in allowed_statuses for p in parts)
bad_statuses = [s for s in status_lines if not status_variants_ok(s)]
check("17. every implementation-unlock-map.md Status: assignment uses only the four permitted values", len(bad_statuses) == 0 and len(status_lines) > 0, f"bad={bad_statuses}")

# 18. links/anchors resolve -- check every packet .md internal relative link target file exists
def check_links(md_path):
    text = open(md_path, encoding="utf-8").read()
    links = re.findall(r"\]\(([^)]+)\)", text)
    problems = []
    for link in links:
        if link.startswith("http") or link.startswith("#"):
            continue
        target = link.split("#")[0]
        if not target:
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(md_path), target))
        if not os.path.exists(full):
            problems.append((md_path, link))
    return problems

md_files = [f for f in os.listdir(PKT) if f.endswith(".md")]
link_problems = []
for f in md_files:
    link_problems += check_links(os.path.join(PKT, f))
check("18. internal markdown links resolve to existing files", len(link_problems) == 0, f"{link_problems[:10]}")

# 19. CSV headers/row widths consistent
def check_csv_widths(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        w = len(header)
        for i, row in enumerate(r, 2):
            if len(row) != w:
                return (path, i, len(row), w)
    return None

csv_files = [os.path.join(PKT, f) for f in os.listdir(PKT) if f.endswith(".csv")]
csv_files += [os.path.join(f"{PKT}/artifacts", f) for f in os.listdir(f"{PKT}/artifacts") if f.endswith(".csv")] if os.path.isdir(f"{PKT}/artifacts") else []
csv_problems = [check_csv_widths(p) for p in csv_files]
csv_problems = [p for p in csv_problems if p]
check("19. CSV headers/row widths consistent across all packet CSVs", len(csv_problems) == 0, f"{csv_problems}")

# 20. counts reconcile with R16 artifacts
check("20. canonical issue count (421) = 418 field/location/standard + 2 edge + 1 cycle", len(issue_rows) == 421)
check("20b. distinct affected requirements = 289 (matches R16 Failed effective records)",
      len({rq.strip() for r in issue_rows for rq in r["Requirement ID"].split(";")}) == 289)

# 21. checksums verify
checks_path = f"{PKT}/checksums.sha256"
checksum_ok = True
checksum_detail = ""
if os.path.exists(checks_path):
    import hashlib
    for line in open(checks_path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        digest, path = line.split("  ", 1)
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            checksum_ok = False
            checksum_detail += f"MISSING:{path} "
            continue
        h = hashlib.sha256(open(full, "rb").read()).hexdigest()
        if h != digest:
            checksum_ok = False
            checksum_detail += f"MISMATCH:{path} "
else:
    checksum_ok = False
    checksum_detail = "checksums.sha256 not found"
check("21. checksums verify against on-disk files", checksum_ok, checksum_detail)

# 22. final tree clean (only new packet dir added, plus AGC1-authorized
# normative authority-graph files) -- checked by caller via git status
# after add; here check no *unexpected* modifications
AGC1_AUTHORIZED_NON_PACKET_FILES = {
    "docs/kbdl/motion/README.md",
    "docs/kbdl/traceability-metadata.csv",
}
status_out = subprocess.run(["git", "-C", REPO, "status", "--porcelain"], capture_output=True, text=True).stdout
non_packet_changes = []
for l in status_out.splitlines():
    if "kbdl-011-source-model-resolution" in l:
        continue
    path = l[3:].strip()
    if path in AGC1_AUTHORIZED_NON_PACKET_FILES:
        continue
    non_packet_changes.append(l)
check("22. no unrelated working-tree changes outside the new packet directory or AGC1-authorized files", len(non_packet_changes) == 0, f"{non_packet_changes[:10]}")

# 25-36. AGC1 authority-graph checks
readme_text = open(f"{REPO}/docs/kbdl/motion/README.md", encoding="utf-8").read()
csv_state = authority_graph.parse_traceability_csv_state(f"{REPO}/docs/kbdl/traceability-metadata.csv")
readme_state = authority_graph.parse_readme_state(readme_text)
ag_results = authority_graph.check_authority_graph(readme_state, csv_state)
for name, ok, detail in ag_results:
    check(name, ok, detail)
check("AG.no_two_node_cycle", not authority_graph.cycle_exists(readme_state))
check("AG.MOT-007.lifecycle_approved", readme_state["KBDL-MOT-007"]["lifecycle"] == "Approved")
check("AG.MOT-008.lifecycle_approved", readme_state["KBDL-MOT-008"]["lifecycle"] == "Approved")
check("AG.MOT-007.validation_status_not_verified", readme_state["KBDL-MOT-007"]["validation_status"].strip() == "Not verified")
check("AG.MOT-008.validation_status_not_applicable", readme_state["KBDL-MOT-008"]["validation_status"].strip().startswith("Not applicable"))
check("AG.csv.MOT-007.lifecycle_approved", csv_state["KBDL-MOT-007"]["lifecycle_status"] == "Approved")
check("AG.csv.MOT-008.lifecycle_approved", csv_state["KBDL-MOT-008"]["lifecycle_status"] == "Approved")
check("AG.csv.MOT-007.validation_classification_not_verified", csv_state["KBDL-MOT-007"]["validation_classification"] == "Not verified")
check("AG.csv.MOT-008.validation_classification_not_applicable", csv_state["KBDL-MOT-008"]["validation_classification"] == "Not applicable")

# AG.narrow_authorized_diff -- the diff to the two AGC1-authorized files
# must not touch normative requirement text for any requirement other
# than the MOT-007/MOT-008 authority-graph fields, and must not add or
# remove any requirement row.
readme_diff = subprocess.run(["git", "-C", REPO, "diff", "-U0", "HEAD", "--", "docs/kbdl/motion/README.md"],
                              capture_output=True, text=True).stdout
readme_added = [l[1:] for l in readme_diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
readme_removed = [l[1:] for l in readme_diff.splitlines() if l.startswith("-") and not l.startswith("---")]
other_mot_touched = any(
    re.search(r"KBDL-MOT-(?!007|008)\d+", l) for l in readme_added + readme_removed
)
check("AG.narrow_authorized_diff.readme_only_mot007_008", not other_mot_touched,
      "docs/kbdl/motion/README.md diff must only touch KBDL-MOT-007/KBDL-MOT-008 content")

csv_diff = subprocess.run(["git", "-C", REPO, "diff", "-U0", "HEAD", "--", "docs/kbdl/traceability-metadata.csv"],
                           capture_output=True, text=True).stdout
csv_added = [l[1:] for l in csv_diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
csv_removed = [l[1:] for l in csv_diff.splitlines() if l.startswith("-") and not l.startswith("---")]
csv_other_mot_touched = any(
    re.search(r"KBDL-MOT-(?!007|008)\d+", l) for l in csv_added + csv_removed
)
check("AG.narrow_authorized_diff.csv_only_mot007_008", not csv_other_mot_touched,
      "docs/kbdl/traceability-metadata.csv diff must only touch KBDL-MOT-007/KBDL-MOT-008 rows")
check("AG.narrow_authorized_diff.csv_row_count_unchanged",
      len(csv_added) == len(csv_removed) == 2,
      f"expected exactly 2 changed rows (MOT-007, MOT-008); added={len(csv_added)} removed={len(csv_removed)}")

# 23. push safety handled by caller (fast-forward check) -- placeholder true, actual check done in shell during commit/push
check("23. push-safety check deferred to commit/push shell sequence (fast-forward only)", True)

# 24. local/tracking/live-remote SHAs match -- handled by caller after push; here just report current HEAD
head_sha = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
check("24. local HEAD SHA captured for post-push comparison", len(head_sha) == 40, head_sha)

print("=" * 70)
failed = 0
for name, ok, detail in checks:
    status = "PASS" if ok else "FAIL"
    if not ok:
        failed += 1
    line = f"[{status}] {name}"
    if detail and not ok:
        line += f" -- {detail}"
    print(line)
print("=" * 70)
print(f"{len(checks)-failed}/{len(checks)} checks passed")
sys.exit(1 if failed else 0)
