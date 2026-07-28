#!/usr/bin/env python3
"""Build the non-normative AR1 packet from current records without granting authority."""
from pathlib import Path
import csv
import hashlib
import re
import subprocess

ROOT = Path(__file__).resolve().parents[5]
DOC = ROOT / "docs/kbdl"
PKG = DOC / "evidence/kbdl-011-authority-recovery"
ART = PKG / "artifacts"
SRC = PKG / "sources"
ART.mkdir(parents=True, exist_ok=True)
SRC.mkdir(parents=True, exist_ok=True)

PROMPT_FILES = {
    "KBDL-010": Path("/Users/kbmanilla/.codex/attachments/4e68c74e-b69d-4b8b-9286-92890f002aac/pasted-text.txt"),
    "KBDL-011": Path("/Users/kbmanilla/.codex/attachments/27e1a02d-6043-4000-9766-8fe31b53e0b7/pasted-text.txt"),
}
for prompt, source in PROMPT_FILES.items():
    (SRC / f"{prompt.lower()}-released-prompt.md").write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

titles = {
    "KBDL-001":"Specification architecture and governance foundation",
    "KBDL-002":"Identity, principles, and visual consistency",
    "KBDL-003":"Core visual foundations",
    "KBDL-004":"Adaptive theme system",
    "KBDL-005":"Expressive motion language",
    "KBDL-006":"Responsive behavior and accessibility",
    "KBDL-007":"Core action, form, and navigation components",
    "KBDL-008":"Surface, overlay, feedback, and system-state components",
    "KBDL-009":"Project profiles",
    "KBDL-010":"Manual customization",
    "KBDL-011":"Final validation",
}
positions = {
    "KBDL-001":"13", "KBDL-002":"2", "KBDL-003":"3", "KBDL-004":"4",
    "KBDL-005":"5", "KBDL-006":"6–7", "KBDL-007":"8", "KBDL-008":"9",
    "KBDL-009":"10", "KBDL-010":"11", "KBDL-011":"12",
}
impl = {
    "KBDL-001":"2d356b4", "KBDL-002":"867306c", "KBDL-003":"bd9f520",
    "KBDL-004":"74d1d8f", "KBDL-005":"ea32ce3", "KBDL-006":"14ef110",
    "KBDL-007":"332ae95", "KBDL-008":"393a980", "KBDL-009":"254b935",
    "KBDL-010":"12080da", "KBDL-011":"b5bb0a3",
}
remediation = {
    "KBDL-001":"caa6d5d (R1)", "KBDL-002":"c0d3b46 (R1)",
    "KBDL-003":"4ecd814 (R1); f3fbb98/6d6d1ec decision record",
    "KBDL-004":"978aedd/b3e26b1/568ff92/743532a (R1–R4); cad8307 decision record",
    "KBDL-005":"5aba999/a90b544 (R1–R2); e6916ac decision record",
    "KBDL-006":"0c5789e (R1)",
    "KBDL-007":"513dd7e/f45fd47/ee46f5a (R1–R3)",
    "KBDL-008":"c7d3da5/5cf9060 (R1–R2)",
    "KBDL-009":"8dc232c/3503d95/907708c (R1–R3)",
    "KBDL-010":"55b6ba6 (R1)",
    "KBDL-011":"eab3b41 through 3340225 (R1–R10)",
}

rows = list(csv.DictReader((DOC / "traceability-metadata.csv").open(encoding="utf-8")))
mapping = []
by_prompt = {p: [] for p in titles}
for row in rows:
    if not re.search(r"prompt", row["Authority"], re.I):
        continue
    match = re.match(r"KBDL-\d{3}", row["Roadmap prompt"])
    if not match:
        continue
    prompt = match.group(0)
    if prompt not in by_prompt:
        continue
    authority = row["Authority"]
    mixed = bool(re.search(r"KBDL-(?:DEC|GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}|WCAG|governance|conventions|prior|existing", authority, re.I))
    references = sorted(set(re.findall(r"KBDL-(?:DEC|GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}", authority)))
    concepts = [term for term in ["WCAG", "governance", "conventions", "prior/existing Approved requirements"] if (term.split('/')[0].lower() in authority.lower() or (term.startswith("prior/") and re.search(r"prior|existing", authority, re.I)))]
    additional = "; ".join(references + concepts) or "Mixed sources are stated in the exact authority clause"
    rec = {
        "Prompt ID": prompt, "Requirement ID": row["Requirement ID"],
        "Exact authority clause": authority,
        "Authority dependency": "MIXED" if mixed else "SOLE PROMPT",
        "Additional authority source": additional if mixed else "None recorded",
        "Lifecycle": row["Lifecycle status"],
        "Validation status": row["Validation classification"],
        "Source file": row["Source file"],
    }
    mapping.append(rec); by_prompt[prompt].append(rec)

with (ART / "requirement-authority-mapping.csv").open("w", newline="", encoding="utf-8") as h:
    w = csv.DictWriter(h, fieldnames=list(mapping[0]), lineterminator="\n"); w.writeheader(); w.writerows(mapping)

def exact_section(prompt, heading):
    if prompt not in PROMPT_FILES:
        return "UNAVAILABLE — exact released prompt text was not present in the repository or available attachment set."
    text = PROMPT_FILES[prompt].read_text(encoding="utf-8")
    m = re.search(rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return f"UNAVAILABLE — `{heading}` heading not recovered."
    target = f"sources/{prompt.lower()}-released-prompt.md#{heading.lower().replace(' ', '-')}"
    return f"Exact text retained at `{target}`."

ledger_fields = ["Prompt ID","Prompt title","Roadmap position","Exact objective","Mandatory scope","Explicit exclusions","Preconditions","Approval command recovered","Approval command source","Approval timing recovered","Approval timing source","Existing authority basis","Requirements relying on the prompt","Existing implementation commit","Existing validation status","Conflicts found","Missing evidence","Recovery status","Proposed current confirmation","Confirmation effect","Confirmation exclusions","Project-owner decision","Decision date","Decision evidence","Notes"]
ledger = []
for prompt in titles:
    reqs = "; ".join(r["Requirement ID"] for r in by_prompt[prompt])
    prompt_source = f"sources/{prompt.lower()}-released-prompt.md" if prompt in PROMPT_FILES else "Not recovered"
    confirmation = (f"AI-DRAFT FOR SEPARATE PROJECT-OWNER REVIEW — Confirm current, non-retroactive authority for {prompt}. "
        f"The exact mandatory scope being confirmed is limited to the normative text, as it exists at baseline "
        f"33402250e3fdb27bd8e1cba53c722b7b765daf8a, of these relying requirements: {reqs}. "
        "No unavailable historical prompt wording is incorporated or reconstructed. "
        "Effective date: date of explicit project-owner decision (pending). Prior implementation history is not rewritten; "
        "this does not prove historical approval wording; authority would arise only from the current approval forward. "
        "No pending decision-packet item, Recommended or Deferred requirement, implementation conformance, limitation, "
        "PRODUCTION READY status, or project completion is approved.")
    existing = "Current requirement Authority fields; roadmap/blueprint decisions; later implementation/validation history (secondary only)"
    if prompt == "KBDL-005": existing += "; KBDL-DEC-014 directly approves the later fifteen-item motion packet only"
    ledger.append({
        "Prompt ID":prompt, "Prompt title":titles[prompt], "Roadmap position":positions[prompt],
        "Exact objective":exact_section(prompt,"Objective"), "Mandatory scope":exact_section(prompt,"Exact Scope"),
        "Explicit exclusions":exact_section(prompt,"Out of Scope"), "Preconditions":exact_section(prompt,"Preconditions"),
        "Approval command recovered":"NO", "Approval command source":"None containing the original implementation-prompt approval command",
        "Approval timing recovered":"NO", "Approval timing source":"Sequence context only; not approval proof",
        "Existing authority basis":existing, "Requirements relying on the prompt":reqs,
        "Existing implementation commit":impl[prompt], "Existing validation status":"See per-requirement mapping; unchanged by AR1",
        "Conflicts found":"KBDL-005 later direct decision approval is distinct" if prompt == "KBDL-005" else "Later approval assertions/implementation commits do not contain original command",
        "Missing evidence":"Exact original approval command, date/sequence point, approved mandatory scope, and exclusions",
        "Recovery status":"UNRECOVERED", "Proposed current confirmation":confirmation,
        "Confirmation effect":"If separately approved: current authority from that decision forward; non-retroactive",
        "Confirmation exclusions":"No historical-wording proof; no packet/recommendation/implementation/limitation/readiness/completion approval",
        "Project-owner decision":"PENDING", "Decision date":"PENDING", "Decision evidence":"PENDING",
        "Notes":f"Released prompt source: {prompt_source}. Implementation {impl[prompt]}; remediation {remediation[prompt]}.",
    })

with (PKG / "authority-recovery-ledger.csv").open("w", newline="", encoding="utf-8") as h:
    w=csv.DictWriter(h, fieldnames=ledger_fields, lineterminator="\n"); w.writeheader(); w.writerows(ledger)

boundary = "> This packet is non-normative and preparation-only. It does not approve, confirm, restore, infer, or backdate any implementation-prompt authority. Authority changes require a later explicit project-owner decision on each prompt record."
packet = ["# KBDL Prompt-Authority Recovery Packet", "", boundary, "", "## Status", "", "Preparation was authorized by KBDL-011-AR1. Every project-owner decision remains `PENDING`. KBDL-011 remains blocked; candidate readiness is Not ready; implementation conformance is Not verified; project completion is pending.", "", "## Method and sources", "", "The hierarchy in KBDL-011-AR1 was applied. Exact released prompt text is retained only for KBDL-010 and KBDL-011. For KBDL-001 through KBDL-009, missing prompt text is not reconstructed from implementation. Sequence is recorded as context, never proof. See `artifacts/source-inventory.csv`, `artifacts/requirement-authority-mapping.csv`, and `authority-gaps.csv`."]
for item in ledger:
    p=item["Prompt ID"]
    prev="None (first implementation prompt)" if p=="KBDL-001" else f"KBDL-{int(p[-3:])-1:03d} passed/released next step according to repository sequence"
    nxt="No later implementation prompt; final-validation remediation follows" if p=="KBDL-011" else f"KBDL-{int(p[-3:])+1:03d} release followed validation/remediation sequence"
    packet += ["", f"## {p} — {item['Prompt title']}", "", f"- **Roadmap position:** {item['Roadmap position']}", f"- **Previous passed prompt:** {prev}", f"- **Prompt release point:** exact release event not independently recovered; Git sequence precedes `{impl[p]}`.", "- **Original approval point:** UNRECOVERED.", f"- **Implementation commit:** `{impl[p]}`.", f"- **Remediation sequence:** {remediation[p]}.", "- **Final validated commit:** not independently established as an original approval record.", f"- **Next prompt release point:** {nxt}.", f"- **Exact objective:** {item['Exact objective']}", f"- **Mandatory scope:** {item['Mandatory scope']}", f"- **Explicit exclusions:** {item['Explicit exclusions']}", f"- **Preconditions:** {item['Preconditions']}", f"- **Relying requirements ({len(by_prompt[p])}):** {item['Requirements relying on the prompt'] or 'None mapped'}", f"- **Original evidence status:** `{item['Recovery status']}`.", f"- **Available evidence:** {item['Existing authority basis']}.", f"- **Missing/conflicting evidence:** {item['Missing evidence']}; {item['Conflicts found']}."]
    if p=="KBDL-005":
        packet += ["- **Separate direct evidence:** [KBDL-DEC-014](../../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) records the direct later selection `Yes, approve motion decisions` for exactly fifteen motion decisions. It is not evidence of the original KBDL-005 implementation-prompt approval."]
    packet += ["", "### Proposed current confirmation — not effective", "", item["Proposed current confirmation"], "", "**Project-owner decision: PENDING**"]
packet += ["", "## Preparation boundary", "", boundary]
(PKG / "authority-recovery-packet.md").write_text("\n".join(packet)+"\n", encoding="utf-8")

review=["# Project-Owner Authority Review Form","",boundary,"","No option is preselected. Review each proposed record independently."]
choices=["CONFIRM CURRENT AUTHORITY","REVISE CONFIRMATION","REJECT AUTHORITY","PROVIDE ORIGINAL EVIDENCE","DEFER DECISION"]
for p in titles:
    review += ["",f"## {p}","",f"Review the proposed confirmation in [the {p} record](authority-recovery-packet.md#{p.lower()}--{titles[p].lower().replace(' ', '-').replace(',', '')}).",""]+[f"- [ ] {c}" for c in choices]+["","Decision date: ____________________","","Decision evidence/reference: ____________________"]
(PKG/"project-owner-review.md").write_text("\n".join(review)+"\n",encoding="utf-8")

gaps=[]
for i,p in enumerate(titles,1):
    gaps.append({"Prompt ID":p,"Gap ID":f"KBDL-AR-GAP-{i:03d}","Severity":"BLOCKING","Missing or conflicting item":"Original approval command, timing, mandatory scope, and exclusions are not durably recovered","Evidence inspected":"Released prompt when available; roadmap; decisions; requirements; traceability; validation; R8–R10 evidence; Git history","Why the gap matters":"Prompt-derived authority cannot be independently established","Affected requirements":"; ".join(r["Requirement ID"] for r in by_prompt[p]),"Required project-owner action":"Review this prompt's independent proposed current confirmation or provide original evidence","Blocking status":"BLOCKED"})
    if p=="KBDL-005": gaps.append({"Prompt ID":p,"Gap ID":"KBDL-AR-GAP-012","Severity":"HIGH","Missing or conflicting item":"Direct later motion-packet approval can be conflated with original implementation-prompt approval","Evidence inspected":"decision-register.md KBDL-DEC-014; motion/README.md","Why the gap matters":"The two approval scopes and times differ","Affected requirements":"KBDL-MOT-005–011; 013; 020; 028–034","Required project-owner action":"Keep DEC-014 separate; decide KBDL-005 prompt confirmation independently","Blocking status":"BLOCKED"})
with (PKG/"authority-gaps.csv").open("w",newline="",encoding="utf-8") as h:
    w=csv.DictWriter(h,fieldnames=list(gaps[0]),lineterminator="\n");w.writeheader();w.writerows(gaps)

sources=[
    ("docs/kbdl/README.md","Approved roadmap/status index","Durable repository source"),
    ("docs/kbdl/decision-register.md","Approved decisions including distinct KBDL-005 packet decision","Durable repository source"),
    ("docs/kbdl/traceability-matrix.md","Readable requirement traceability","Durable repository source"),
    ("docs/kbdl/traceability-metadata.csv","Per-ID authority/lifecycle/validation records","Durable repository source"),
    ("docs/kbdl/validation.md","Sequence and current status","Durable repository source"),
    ("docs/kbdl/evidence/kbdl-011-r8","Prior generated authority/evidence claims","Secondary generated evidence"),
    ("docs/kbdl/evidence/kbdl-011-r9","Prior approval registry and validators","Secondary generated evidence"),
    ("docs/kbdl/evidence/kbdl-011-r10","Blocked authority audit and recovery request","Durable remediation evidence"),
    ("sources/kbdl-010-released-prompt.md","Exact uploaded KBDL-010 prompt copy","Exact prompt text; no approval exchange"),
    ("sources/kbdl-011-released-prompt.md","Exact uploaded KBDL-011 prompt copy","Exact prompt text; no approval exchange"),
    ("git log --all","Implementation/remediation sequence","Sequence only; not approval proof"),
]
with (ART/"source-inventory.csv").open("w",newline="",encoding="utf-8") as h:
    w=csv.writer(h,lineterminator="\n");w.writerow(["Source","Purpose","Classification"]);w.writerows(sources)

missing=["Original prompt approvals recovered: 0","Partial original approvals recovered: 0","Unrecovered original approvals: 11","Exact released prompt texts recovered: 2 (KBDL-010 and KBDL-011)","Exact released prompt texts unavailable: 9 (KBDL-001 through KBDL-009)","KBDL-005 direct later packet selection: recovered separately in KBDL-DEC-014; not an original prompt approval","No approval command was inferred from sequence, lifecycle, implementation commits, or generated registries."]
(ART/"missing-evidence-report.txt").write_text("\n".join(missing)+"\n",encoding="utf-8")
print(f"Prompt records: {len(ledger)}; authority mappings: {len(mapping)}; gaps: {len(gaps)}")
