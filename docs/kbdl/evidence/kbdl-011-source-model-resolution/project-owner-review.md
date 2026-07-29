# Project-Owner Review Form — KBDL-011-SMR1

This is a non-normative review form. It records no decision. Every
decision cell below is unselected. Blanket or bulk approval across any
category is unsafe and is not supported by this form's structure — each
row must be reviewed and decided individually, because categories overlap
(see `source-model-resolution-ledger.csv`) and a single requirement may
depend on more than one category's outcome (91 requirements do; see
`impact-assessment.md`).

Each decision the owner accepts here still requires a **separate, later
recording and validation prompt** before it has any normative effect.
Nothing recorded in this form is self-executing.

Full per-issue detail (current candidate value/source, permitted
authoritative source, risk, alternatives, trade-offs) is in
`issue-register.csv`, keyed by **Resolution issue ID**. This form groups
those 421 issues into eight reviewable batches and shows, for each, the
affected requirements and validation gates and the exact scope of the
possible decision — it does not restate every column.

Recommended review order: read `source-model-resolution-packet.md` §3–4
first, then work batch by batch below. Do not approve a batch without
opening the corresponding rows in `issue-register.csv`.

---

## Batch A — Validation-classification authority (59 issues)

Resolution issue IDs: `SMR1-VC-0001` … `SMR1-VC-0059`.
Affected validation gates: VAL-003, VAL-006.
Affected requirements: 59 distinct IDs spanning KBDL-A11Y, KBDL-CMP,
KBDL-GOV, KBDL-MOT, KBDL-PRN, KBDL-RSP (full list in
`docs/kbdl/evidence/kbdl-011-r16/artifacts/owner-decisions-required.md`
§ "Validation-classification authority").

Scope of possible decision, per requirement, independently:
- [ ] PROVIDE ORIGINAL OR APPROVED SOURCE
- [ ] CONFIRM CURRENT CLASSIFICATION AS NEW CURRENT AUTHORITY
- [ ] REVISE CLASSIFICATION
- [ ] SET TO NOT VERIFIED
- [ ] DEFER DECISION

Non-retroactive boundary (applies to every "confirm current" choice in
this batch): confirming would be current and non-retroactive; would not
reconstruct historical approval; would not prove execution evidence;
would not change lifecycle; would require a later recording and
validation prompt.

Risk: reviewing this batch in bulk could legitimize an unsupported
classification for a requirement that, individually, should instead be
set to Not verified.

## Batch B — Authority-field sources (21 issues)

Resolution issue IDs: `SMR1-AU-0001` … `SMR1-AU-0021`.
Affected validation gate: VAL-003.
Affected requirements: 21 distinct IDs (full list in
`owner-decisions-required.md` § "Authority-field sources"), including
`KBDL-MOT-007`, whose authority field is reviewed here independently of
the MOT cycle-level record in Batch H.

Candidate authority types identified per row in `issue-register.csv`:
AR2 prompt confirmation / Approved decision / Prior Approved requirement /
Adopted standard / Mixed authority / New current project-owner authority /
No valid authority identified.

Scope of possible decision, per requirement, independently:
- [ ] PROVIDE ORIGINAL OR APPROVED AUTHORITY
- [ ] CONFIRM CURRENT NON-RETROACTIVE AUTHORITY
- [ ] REVISE AUTHORITY EXPRESSION
- [ ] REJECT AUTHORITY
- [ ] DEFER DECISION

Risk: lifecycle, ledger presence, and implementation history are never
treated as authority in this batch; bulk approval could inadvertently
create a new authority cycle.

## Batch C — Validation-evidence mappings (14 issues)

Resolution issue IDs: `SMR1-VE-0001` … `SMR1-VE-0014`.
Affected validation gate: VAL-004.
Affected requirements: 14 distinct IDs (full list in
`owner-decisions-required.md` § "Validation-evidence mappings"). 11 of
these 14 additionally carry an R16 `EVIDENCE_SCOPE_RELATIONSHIP` finding
(the resolved evidence artifact does not name the requirement or an
approved shared scope) — see the `Notes` column in `issue-register.csv`.

Scope of possible decision, per requirement, independently:
- [ ] PROVIDE ORIGINAL EVIDENCE MANIFEST
- [ ] CONFIRM SCOPE MAPPING
- [ ] REVISE EVIDENCE CITATION
- [ ] SET TO NOT VERIFIED
- [ ] DEFER DECISION

Owner choices here may authorize later evidence work; this packet does
not execute any evidence-gathering or re-scoring itself.

## Batch D — Validation-method sources (12 issues)

Resolution issue IDs: `SMR1-VM-0001` … `SMR1-VM-0012`.
Affected validation gate: VAL-004.
Affected requirements: all 12 `KBDL-VAL-*` requirements (VAL-001 through
VAL-012).

Scope of possible decision, per requirement, independently:
- [ ] PROVIDE ORIGINAL METHOD SOURCE
- [ ] CONFIRM METHOD AS CURRENT NON-RETROACTIVE
- [ ] REVISE METHOD
- [ ] SET TO NOT VERIFIED
- [ ] DEFER DECISION

Some methods in this batch are implementation-dependent or belong to
VAL-004's locked scope; no method in this batch is executed by SMR1
regardless of which option the owner eventually selects.

## Batch E — Limitation mappings (229 issues)

Resolution issue IDs: `SMR1-KL-0001` … `SMR1-KL-0229`.
Affected validation gates: VAL-006, VAL-005.
Affected requirements: 229 distinct IDs — the largest single batch (full
list in `owner-decisions-required.md` § "Limitation mappings").

Scope of possible decision, per requirement, independently:
- [ ] PROVIDE APPROVED LIMITATION SOURCE
- [ ] CONFIRM CURRENT LIMITATION AS CURRENT NON-RETROACTIVE GOVERNANCE
- [ ] REVISE LIMITATION
- [ ] REMOVE UNSUPPORTED LIMITATION
- [ ] DEFER DECISION

No limitation is accepted through preparation of this form. Given the
size of this batch, review in controlled sub-batches (e.g. by requirement
prefix — KBDL-A11Y, KBDL-CMP, KBDL-CUS, KBDL-FND, KBDL-MOT, KBDL-PRN,
KBDL-PRO, KBDL-RSP, KBDL-THM, KBDL-VAL — as already grouped in
`issue-register.csv`) rather than as one action.

## Batch F — Exact locations (63 issues)

Resolution issue IDs: `SMR1-LOC-0001` … `SMR1-LOC-0063`.
Affected validation gates: VAL-006, VAL-007.
Affected requirements: 63 distinct IDs (full list in
`owner-decisions-required.md` § "Exact locations").

Scope of possible decision, per requirement, independently:
- [ ] CONFIRM DERIVED LOCATION
- [ ] CONFIRM EXISTING LOCATION WITH SOURCE
- [ ] REVISE LOCATION
- [ ] PROVIDE ORIGINAL EVIDENCE
- [ ] DEFER DECISION

Multiple legitimate locations may coexist (a containing section and an
exact subsection); review each row's `Current risk` column in
`issue-register.csv` before selecting.

## Batch G — Standard-clause mappings (20 issues)

Resolution issue IDs: `SMR1-SC-0001` … `SMR1-SC-0020`.
Affected validation gate: VAL-003.
Affected requirements: 20 distinct IDs (full list in
`owner-decisions-required.md` § "Standard-clause mappings"). Each row
folds R16's `MISSING_STANDARD_BASIS` and `STANDARD_CLAUSE_MISMATCH`
defect rows (same 20 requirements) into one canonical issue.

Scope of possible decision, per requirement, independently:
- [ ] CONFIRM DIRECT STANDARD AUTHORITY
- [ ] CLASSIFY AS SUPPORTING GUIDANCE
- [ ] CLASSIFY AS ANALOGY
- [ ] REVISE STANDARD REFERENCE
- [ ] REMOVE UNSUPPORTED REFERENCE
- [ ] PROVIDE SOURCE EVIDENCE
- [ ] DEFER DECISION

Risk: the current reference is generic only (no exact governing clause
independently resolved); confirming direct authority without evidence
risks overclaiming standard authority.

## Batch H — MOT-007 / MOT-008 authority cycle (3 issues — reviewed together, decided independently)

Resolution issue IDs: `SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`,
`SMR1-MOTCYCLE-0001`.
Affected validation gate: VAL-003.
Affected requirements: `KBDL-MOT-007`, `KBDL-MOT-008`.

Exact source: both requirements are `Approved` per `KBDL-DEC-014`,
decision packet item 2 (`docs/kbdl/motion/README.md` §10, table row 2),
which adopts the timing classes (`timing-easing.md` §1, KBDL-MOT-007) and
the duration recommendations (`timing-easing.md` §2, KBDL-MOT-008)
"together, as one timing system." Each requirement's authority text cites
the *other* requirement together with `KBDL-DEC-014`
(`docs/kbdl/evidence/kbdl-011-r16/artifacts/authority-cycle-audit.csv`),
producing the two-node cycle `KBDL-MOT-007 → KBDL-MOT-008 → KBDL-MOT-007`.

**Edge 1 — `SMR1-MOTEDGE-0001` (KBDL-MOT-007 → KBDL-MOT-008):**
- [ ] AUTHORITY EDGE
- [ ] SUPPORTING AUTHORITY
- [ ] CONTEXT-ONLY
- [ ] RELATED REQUIREMENT
- [ ] REMOVE OR REVISE RELATIONSHIP
- [ ] PROVIDE ORIGINAL EVIDENCE
- [ ] DEFER DECISION

**Edge 2 — `SMR1-MOTEDGE-0002` (KBDL-MOT-008 → KBDL-MOT-007):**
- [ ] AUTHORITY EDGE
- [ ] SUPPORTING AUTHORITY
- [ ] CONTEXT-ONLY
- [ ] RELATED REQUIREMENT
- [ ] REMOVE OR REVISE RELATIONSHIP
- [ ] PROVIDE ORIGINAL EVIDENCE
- [ ] DEFER DECISION

**Cycle-level disposition — `SMR1-MOTCYCLE-0001` (decide only after both
edges above are reviewed):**
- [ ] Break cycle via MOT-007 edge revision
- [ ] Break cycle via MOT-008 edge revision
- [ ] Replace both edges with shared independent authority
- [ ] Preserve the cycle and keep VAL-003 Not verified
- [ ] Provide original governance evidence

No cycle-level resolution is recommended or preselected here. Do not
select an edge or the cycle disposition in bulk; review both normative
requirement blocks (`docs/kbdl/motion/README.md` lines 396–421) together
before deciding.

---

## Sign-off (not completed by this packet)

| Field | Value |
| --- | --- |
| Decisions recorded in this review cycle | PENDING |
| Reviewer | PENDING |
| Review date | PENDING |
| Batches approved this cycle | PENDING |
| Follow-on recording prompt(s) requested | PENDING |

This form's completion does not itself change any protected field, VAL
status, candidate status, implementation conformance, or completion
status.
