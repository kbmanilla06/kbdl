# Implementation-Unlock Map — KBDL-011-SMR1

**This map does not authorize implementation.** It records, for each
decision group, what a later remediation prompt *could* be prepared to
do — only after the owner decision is recorded and separately validated.
Every status below is one of exactly four values. `READY`, `APPROVED`,
and `UNLOCKED` are never used for implementation work in this document.

Status vocabulary:
- `LOCKED — OWNER DECISION REQUIRED`
- `LOCKED — ADDITIONAL EVIDENCE REQUIRED`
- `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`
- `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL`

## Batch A — Validation-classification authority

- Decision required: one of PROVIDE SOURCE / CONFIRM CURRENT / REVISE /
  SET NOT VERIFIED / DEFER, per requirement (59 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR2:
  Validation-classification recording," scoped to only the requirements
  with a recorded, non-deferred decision.
- Preconditions: owner decision recorded per requirement; no bulk
  decision accepted.
- Files/metadata potentially affected: `traceability-metadata.csv`,
  the requirement's own module file, `field-source-registry.csv`
  (regenerated, not hand-edited).
- Validation gates affected: VAL-003, VAL-006.
- Required regression tests: full VAL-003/VAL-006 re-run project-wide,
  not only for changed IDs (both gates score every requirement).
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: No (this batch does not touch
  clause-level evidence).
- Could affect candidate readiness: **Yes, indirectly** — VAL-003/VAL-006
  are two of the four Not-verified gates blocking candidate readiness.
- Status: `LOCKED — OWNER DECISION REQUIRED`.

## Batch B — Authority-field sources

- Decision required: one of PROVIDE AUTHORITY / CONFIRM CURRENT / REVISE
  / REJECT / DEFER, per requirement (21 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR3:
  Authority-expression recording and authority-graph regeneration."
- Preconditions: owner decision recorded; authority-graph regeneration
  script re-run and reviewed for newly introduced cycles before commit.
- Files/metadata potentially affected: the requirement's authority text,
  `authority-graph-audit.csv`, `authority-reference-classification.csv`,
  `approved-authority-population.csv`.
- Validation gates affected: VAL-003.
- Required regression tests: full authority-cycle detection re-run
  (not just the 21 changed IDs — a revision anywhere can create a new
  cycle elsewhere).
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: No.
- Could affect candidate readiness: **Yes, indirectly.**
- Status: `LOCKED — OWNER DECISION REQUIRED`.

## Batch C — Validation-evidence mappings

- Decision required: one of PROVIDE EVIDENCE MANIFEST / CONFIRM SCOPE /
  REVISE CITATION / SET NOT VERIFIED / DEFER, per requirement (14 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR4:
  Validation-evidence scope recording" — and, only if the owner
  separately authorizes it, a distinct future evidence-gathering
  engagement (out of scope for any KBDL-011 documentation prompt).
- Preconditions: owner decision recorded; if new evidence is to be
  gathered, that is its own, later-authorized body of work, not a
  documentation recording prompt.
- Files/metadata potentially affected: evidence citation text in the
  affected module files; `evidence-scope-audit.csv` (regenerated).
- Validation gates affected: VAL-004.
- Required regression tests: VAL-004 clause-method re-scoring for the
  14 changed IDs at minimum.
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: **Yes, for any option requiring new
  evidence** — VAL-004's eleven clause methods remain intentionally
  unexecuted; this map does not change that.
- Could affect candidate readiness: **Yes.**
- Status: `LOCKED — ADDITIONAL EVIDENCE REQUIRED` (for evidence-gathering
  options) / `LOCKED — OWNER DECISION REQUIRED` (for SET NOT VERIFIED or
  DEFER options).

## Batch D — Validation-method sources

- Decision required: one of PROVIDE METHOD SOURCE / CONFIRM CURRENT /
  REVISE / SET NOT VERIFIED / DEFER, per requirement (12 total, all
  `KBDL-VAL-*`).
- Later remediation prompt that could be prepared: "KBDL-011-SMR5:
  Validation-method-source recording."
- Preconditions: owner decision recorded per method; any method judged
  implementation-dependent remains unexecuted regardless of the
  recording outcome.
- Files/metadata potentially affected: `docs/kbdl/validation.md` method
  descriptions (via a later, separate edit — not this packet).
- Validation gates affected: VAL-004 directly; indirectly every gate
  whose method this batch reviews.
- Required regression tests: VAL-004 full re-run.
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: **Yes, for the eleven clause
  methods specifically.**
- Could affect candidate readiness: **Yes.**
- Status: `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`.

## Batch E — Limitation mappings

- Decision required: one of PROVIDE LIMITATION SOURCE / CONFIRM CURRENT /
  REVISE / REMOVE / DEFER, per requirement (229 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR6:
  Limitation-scope recording," likely split into per-module sub-prompts
  given the batch size.
- Preconditions: owner decisions recorded per requirement (or per
  identical shared-text group, with the grouping itself owner-approved
  first); no limitation accepted through recording alone.
- Files/metadata potentially affected: "Known limitation" fields across
  up to 229 module-file locations; `limitation-scope-audit.csv`
  (regenerated).
- Validation gates affected: VAL-005, VAL-006.
- Required regression tests: full VAL-005/VAL-006 re-run.
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: No.
- Could affect candidate readiness: **Yes — this is the single largest
  blocker by requirement count.**
- Status: `LOCKED — OWNER DECISION REQUIRED`.

## Batch F — Exact locations

- Decision required: one of CONFIRM DERIVED / CONFIRM EXISTING / REVISE /
  PROVIDE EVIDENCE / DEFER, per requirement (63 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR7:
  Specification-location correction."
- Preconditions: owner decision recorded; every cross-reference to a
  revised anchor identified before any anchor is changed.
- Files/metadata potentially affected: "Specification location" fields;
  anchors in the target module files; `exact-location-audit.csv`
  (regenerated).
- Validation gates affected: VAL-006, VAL-007.
- Required regression tests: full VAL-007 link/anchor-integrity re-run
  project-wide (anchor changes are not locally scoped).
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: No.
- Could affect candidate readiness: **Yes, indirectly.**
- Status: `LOCKED — OWNER DECISION REQUIRED`.

## Batch G — Standard-clause mappings

- Decision required: one of CONFIRM DIRECT / SUPPORTING / ANALOGY /
  REVISE / REMOVE / PROVIDE EVIDENCE / DEFER, per requirement (20 total).
- Later remediation prompt that could be prepared: "KBDL-011-SMR8:
  Standard-clause citation correction."
- Preconditions: owner decision recorded; exact clause identified before
  any CONFIRM DIRECT outcome is recorded.
- Files/metadata potentially affected: standard-citation text in the
  requirement's module file; `standard-clause-audit.csv`,
  `adopted-standard-clause-audit.csv` (regenerated).
- Validation gates affected: VAL-003.
- Required regression tests: VAL-003 re-run for changed IDs.
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: No.
- Could affect candidate readiness: **Yes, indirectly.**
- Status: `LOCKED — ADDITIONAL EVIDENCE REQUIRED`.

## Batch H — MOT-007/MOT-008 authority cycle

- Decision required: two independent edge classifications plus one
  cycle-level disposition (3 total, see `project-owner-review.md` Batch
  H). **Recorded, per KBDL-011-SMR1-BH-R1:** all three are now durably
  recorded — see `batch-h-owner-decision-record.md` — pending
  planning-agent validation. Recording alone does not advance this batch
  past `LOCKED`.
- Later remediation prompt that could be prepared: "KBDL-011-SMR9:
  MOT-007/MOT-008 authority-graph correction," scoped strictly to the
  graph representation, not to the requirements' Approved lifecycle
  status (which this map does not propose changing).
- Preconditions: both edges reviewed together; cycle-level disposition
  selected only after both edge decisions are recorded; no automatic
  edge removal.
- Files/metadata potentially affected: `authority-graph-audit.csv`,
  `authority-cycle-audit.csv`, `authority-reference-classification.csv`
  (all regenerated); potentially the authority-text sentences in
  `docs/kbdl/motion/README.md` lines 400–402 and 416–418, only if the
  owner selects an edge-revision option.
- Validation gates affected: VAL-003 (this is the sole remaining
  `CIRCULAR_AUTHORITY` finding).
- Required regression tests: full authority-graph cycle-detection re-run
  project-wide after any edge change, to confirm no new cycle was
  introduced.
- Owner approval alone sufficient: **No.**
- Planning-agent validation also required: **Yes.**
- Blocked by VAL-004's locked scope: **Partially** — any clause-level
  implication for KBDL-MOT-008's numerical recommendations would remain
  additionally gated by VAL-004.
- Could affect candidate readiness: **Yes** — VAL-003 cannot verify while
  this cycle is unresolved.
- Status: `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`.

## Summary

All nine batches (A–H, with H counted as one decision group of three
issues) are currently `LOCKED`. As of KBDL-011-SMR1-BH-R1, Batch H's three
issues have a durably recorded, non-deferred owner decision (see
`batch-h-owner-decision-record.md`), which is why Batch H's status moved
from `LOCKED — OWNER DECISION REQUIRED` to
`LOCKED — PLANNING-AGENT VALIDATION REQUIRED`. Batches A–G remain
`LOCKED — OWNER DECISION REQUIRED` (or, for Batch C/G,
`LOCKED — ADDITIONAL EVIDENCE REQUIRED`) because no owner decision has yet
been recorded for any of their 418 combined issues. No batch is
`ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL` — recording a decision alone
never reaches that status; a batch moves to
`ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL` only after (a) the owner
records a non-deferred decision for every issue in that batch (done for
Batch H; not yet done for A–G) and (b) a planning agent validates that
recording (not yet done for any batch, including Batch H).
