# Project-Owner Review Form — KBDL-011-SMR1

This is a non-normative review form. At commit `662ee28` it recorded no
decision and every decision cell below was unselected. As of
KBDL-011-SMR1-BH-R1, three checkboxes are selected — Batch H:
`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001` — each
backed by an exactly matching durable owner-decision record
(`batch-h-owner-decision-record.md`). As of KBDL-011-SMR1-BA-OD1-DR1, a
fourth checkbox is selected — Batch A: `SMR1-VC-0001` only — backed by
an exactly matching durable owner-decision record
(`batch-a-smr1-vc-0001-owner-decision-record.md`). Four decisions are
now durably recorded in total (three Batch H, one Batch A); every other
decision cell, across all other batches and the other 58 Batch A
issues, remains unselected — 417 issues remain PENDING. Blanket or bulk
approval across any category is unsafe and is not supported by this
form's structure — each row must be reviewed and decided individually,
because categories overlap (see `source-model-resolution-ledger.csv`)
and a single requirement may depend on more than one category's outcome
(91 requirements do; see `impact-assessment.md`).

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

### Issue-level decision — SMR1-VC-0001 (KBDL-A11Y-001)

This is the one issue-level decision recorded within Batch A this
review cycle. It applies only to this issue and to no other Batch A
issue; the shared option list above is a menu of per-issue
possibilities, not a group selection. The other 58 Batch A issues
remain unselected and PENDING.

**Issue-level selection — `SMR1-VC-0001`:**
- [ ] PROVIDE ORIGINAL OR APPROVED SOURCE
- [ ] CONFIRM CURRENT CLASSIFICATION AS NEW CURRENT AUTHORITY
- [ ] REVISE CLASSIFICATION
- [x] SET TO NOT VERIFIED
- [ ] DEFER DECISION

**Owner decision recorded (2026-07-29):** SMR1-VC-0001 = SET TO NOT
VERIFIED. The durable evidence of this selection is
`docs/kbdl/evidence/kbdl-011-source-model-resolution/batch-a-smr1-vc-0001-owner-decision-record.md`
(record `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29`) — not this
form alone. Mirrored in `issue-register.csv` (Owner decision / Owner
decision date / Owner evidence / Resolution status columns for this
row; that status has since advanced to `METADATA RECORDED —
PLANNING-AGENT VALIDATED`). This selection is current and non-retroactive; does not
prove accessibility testing occurred; does not establish WCAG
conformance; does not change lifecycle or provenance; does not resolve
`SMR1-KL-0001`; does not restore `VAL-003` or `VAL-006`; does not
authorize implementation; does not begin KBDL-011-SMR2; does not
approve any other Batch A issue. No other Batch A issue is affected or
preselected by this entry; the other 58 Batch A issues and all other
417 issues in the packet remain literally `PENDING`.

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
- [x] RELATED REQUIREMENT
- [ ] REMOVE OR REVISE RELATIONSHIP
- [ ] PROVIDE ORIGINAL EVIDENCE
- [ ] DEFER DECISION

**Edge 2 — `SMR1-MOTEDGE-0002` (KBDL-MOT-008 → KBDL-MOT-007):**
- [ ] AUTHORITY EDGE
- [ ] SUPPORTING AUTHORITY
- [ ] CONTEXT-ONLY
- [x] RELATED REQUIREMENT
- [ ] REMOVE OR REVISE RELATIONSHIP
- [ ] PROVIDE ORIGINAL EVIDENCE
- [ ] DEFER DECISION

**Cycle-level disposition — `SMR1-MOTCYCLE-0001` (decide only after both
edges above are reviewed):**
- [ ] Break cycle via MOT-007 edge revision
- [ ] Break cycle via MOT-008 edge revision
- [x] Replace both edges with shared independent authority
- [ ] Preserve the cycle and keep VAL-003 Not verified
- [ ] Provide original governance evidence

**Owner decisions recorded (2026-07-29):** SMR1-MOTEDGE-0001 = RELATED
REQUIREMENT; SMR1-MOTEDGE-0002 = RELATED REQUIREMENT; SMR1-MOTCYCLE-0001 =
REPLACE BOTH EDGES WITH SHARED INDEPENDENT AUTHORITY. The durable evidence
of this selection is
`docs/kbdl/evidence/kbdl-011-source-model-resolution/batch-h-owner-decision-record.md`
(record `KBDL-SMR1-BH-OWNER-DECISION-2026-07-29`) — not `KBDL-DEC-014`
alone. The cycle-level choice separately cites `KBDL-DEC-014`, decision
packet item 2, as the *selected shared independent authority* for both
KBDL-MOT-007 and KBDL-MOT-008; that citation is the substantive authority
being selected, while the durable record above is the evidence that this
selection happened on 2026-07-29. Mirrored in `issue-register.csv` (Owner
decision / Owner decision date / Owner evidence / Resolution status
columns for these three rows, status `OWNER DECISION RECORDED — AWAITING
PLANNING-AGENT VALIDATION`). This selection alone does not reclassify the
requirements' authority graph, change VAL-003 from Not verified, or alter
any protected field — per this packet's design, it still requires a
separate durable recording and validation prompt (an authority-graph
correction prompt for KBDL-MOT-007/MOT-008, followed by planning-agent
validation) before it takes effect. No other batch's decisions are
affected or preselected by this entry. At the historical Batch H point
(`KBDL-011-SMR1-BH-R1`), all other 418 canonical issues remained
literally `PENDING`. As of the current `KBDL-011-SMR1-BA-OD1-DR1-R1`
point (following the additional Batch A / `SMR1-VC-0001` decision), 417
canonical issues remain literally `PENDING`.

---

### Next issue-level review — SMR1-VC-0002 (KBDL-A11Y-004)

**The sole next owner-review target is `SMR1-VC-0002` (`KBDL-A11Y-004`). No
owner decision has been made.** Every checkbox below is unselected, and that is the current, accurate
state — not an oversight.

**Issue-level selection — `SMR1-VC-0002`:**
- [ ] PROVIDE ORIGINAL OR APPROVED SOURCE
- [ ] CONFIRM CURRENT CLASSIFICATION AS NEW CURRENT AUTHORITY
- [ ] REVISE CLASSIFICATION
- [ ] SET TO NOT VERIFIED
- [ ] DEFER DECISION

State of this issue:

- `SMR1-VC-0002` (`KBDL-A11Y-004`, Validation classification) is the
  lowest-numbered still-pending Batch A issue. It was selected by that rule
  alone; the selection is a queue designation, not a decision.
- Its `issue-register.csv` Owner decision, Owner decision date, and Owner
  evidence fields all remain literally `PENDING`, and its resolution status
  remains `SOURCE EVIDENCE REQUIRED`.
- **No durable owner-decision record exists for it**, and none is created by
  naming it here.
- `smr1-vc-0002-owner-decision-brief.md` sets out the confirmed facts, the five
  options with their trade-offs, and a recommended starting answer. **The brief
  is informational**; its recommendation is unapproved and unselected.
- No metadata-recording prompt for this issue is released, approved, ready, or
  eligible. Batch A remains `LOCKED — OWNER DECISION REQUIRED`.
- The other 57 pending Batch A validation-classification issues are **not**
  queued, preselected, or under review. Counting `SMR1-VC-0002` itself, and
  excluding the already-recorded `SMR1-VC-0001`, Batch A still has 58 issues
  without an owner decision.
- `SMR1-KL-0004`, the Known-limitation issue for the same requirement, is a
  separate issue and remains `PENDING`.


## Sign-off (cumulative across all review cycles to date: Batch H and Batch A/SMR1-VC-0001)

| Field | Value |
| --- | --- |
| Decisions recorded in this review cycle | 4 |
| Reviewer | Project owner |
| Review date | 2026-07-29 |
| Batch with decisions recorded | Batch H (3, prior cycle); Batch A (1: SMR1-VC-0001, this cycle) |
| Implementation authorization | NOT AUTHORIZED |
| Planning-agent validation | KBDL-011-SMR1-BH-AGC1 and KBDL-011-SMR1-BH-AGC1-VF1: PASSED. KBDL-011-SMR1-BA-OD1-DR1: superseded by KBDL-011-SMR1-BA-OD1-DR1-R1, which is itself PASSED — PLANNING-AGENT VALIDATED. KBDL-011-SMR2-FSRG1: PASSED — PLANNING-AGENT VALIDATED. The reissued KBDL-011-SMR2-VC-0001: PASSED — PLANNING-AGENT VALIDATED on 2026-07-30 (record KBDL-SMR2-VC-0001-PLANNING-AGENT-VALIDATION-2026-07-30, covering commits af6a60a/4aba456/448e39b). KBDL-011-SMR1-RM1 is not an open gate: the prompts it staged have since been implemented and validated. The current open gate is planning-agent validation of KBDL-011-SMR2-VC-0001-PA1-R2 |
| Other batches this cycle | None newly recorded this cycle beyond SMR1-VC-0001 — all other 417 issues remain `PENDING` |
| Follow-on recording prompt(s) requested | The metadata-recording prompt for KBDL-A11Y-001's validation-classification field was proposed as KBDL-011-SMR2-VC-0001 and returned APPROVE WITH CHANGES on 2026-07-29: a prerequisite roadmap prompt, KBDL-011-SMR2-FSRG1 (live field-source-registry artifact and deterministic generator), is added first (see `smr2-fsrg1-prompt.md`), and KBDL-011-SMR2-VC-0001 was then **reissued, not resumed**, after FSRG1 passed planning-agent validation. Both prompts have since been implemented and have passed planning-agent validation, and both now read `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL` in `implementation-unlock-map.md`. The recorded SMR1-VC-0001 choice is now reflected in `KBDL-A11Y-001`'s normative record and traceability row, with the classification unchanged at `Not verified`. Neither prompt authorizes implementation, unlocks Batch A, or makes any further recording prompt eligible. A separate authority-graph correction prompt for KBDL-MOT-007/MOT-008 would still be required before the Batch H cycle-level choice takes effect |

Recording 4 decisions in total (3 Batch H, 1 Batch A) is not, and does
not imply, implementation approval: it is a durably recorded
review-cycle choice only. This form's completion does not itself change
any protected field, VAL status, candidate status, implementation
conformance, or completion status. KBDL-011 remains incomplete.
