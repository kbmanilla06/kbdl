# Durable Project-Owner Decision Record — Batch A / SMR1-VC-0001 (KBDL-011-SMR1)

Record title: Batch A, `SMR1-VC-0001` (`KBDL-A11Y-001` validation
classification) owner-decision record.
Record identifier: `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29`.
Decision date: 2026-07-29.
Timezone: Asia/Manila.
Project-owner authority: the current project owner, recording a decision
against `docs/kbdl/evidence/kbdl-011-source-model-resolution/project-owner-review.md`,
Batch A ("Validation-classification authority"), issue `SMR1-VC-0001`
only.

This record exists because a packet-review decision, once selected, must
have durable evidence independent of the packet itself — the packet
cannot prove its own authority, and `project-owner-review.md`'s
checkbox selection alone is not evidence that this exact choice was
selected on 2026-07-29 for this exact issue (only this record is).

## Decision recorded (exactly one, verbatim, not broadened)

- `SMR1-VC-0001` — Requirement `KBDL-A11Y-001`, Field "Validation
  classification": **SET TO NOT VERIFIED**. The requirement's validation
  classification is retained as `Not verified`. This is the most
  conservative of the five available options; it selects no new
  authority, source, or evidence for the current candidate value.

This record covers only `SMR1-VC-0001`. It does not select, approve, or
preselect any decision for any of the other 58 Batch A issues
(`SMR1-VC-0002` … `SMR1-VC-0059`), for `SMR1-KL-0001` (the separate
Known-limitation issue for the same requirement `KBDL-A11Y-001`), or for
any of the other 417 canonical issues in `issue-register.csv`, all of
which remain literally `PENDING` in every Owner decision / Owner
decision date / Owner evidence field.

## Machine-readable decision block

The row below is the authoritative, parseable record consumed by
`scripts/decision_state.py`. Every cell must match `issue-register.csv`
and `project-owner-review.md` exactly for this issue ID.

| Issue ID | Selected choice | Decision date | Timezone | Evidence record ID |
| --- | --- | --- | --- | --- |
| SMR1-VC-0001 | SET TO NOT VERIFIED | 2026-07-29 | Asia/Manila | KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29 |

## Distinction between decision authority and validation evidence

**This record proves that the project owner selected `SET TO NOT
VERIFIED` for `SMR1-VC-0001` on 2026-07-29. It does not prove that any
accessibility validation, testing, or WCAG conformance assessment was
ever performed for `KBDL-A11Y-001`.** Retaining the `Not verified`
classification is a decision-authority act (choosing not to assert an
unsupported classification); it is not, and cannot substitute for,
validation evidence. `docs/kbdl/accessibility.md`'s existing text about
`KBDL-A11Y-001` is unaffected by this record and is not read as, or
converted into, validation evidence by this decision.

## Boundaries and limitations (all apply; none is waived)

- **Current and non-retroactive effect.** This record documents a
  current project-owner decision made on 2026-07-29. It does not
  reconstruct or assert any earlier historical approval of this
  classification, and it does not assert that the `Not verified`
  classification was ever anything other than what it already was.
- **Validation limitation.** This record does not perform, claim, or
  imply that accessibility testing, screen-reader verification, or any
  other validation method was executed for `KBDL-A11Y-001`. `VAL-003`
  and `VAL-006` remain Not verified.
- **Lifecycle and provenance limitation.** This record does not change
  `KBDL-A11Y-001`'s lifecycle status, provenance, or any other normative
  field. `docs/kbdl/accessibility.md` and
  `docs/kbdl/traceability-metadata.csv` remain byte-identical to the
  verified baseline.
- **Related-issue limitation.** This record does not resolve, decide,
  or preselect `SMR1-KL-0001` (the Known-limitation issue for the same
  requirement). `SMR1-KL-0001` remains literally `PENDING`.
- **VAL-status limitation.** This record does not restore `KBDL-VAL-003`
  or `KBDL-VAL-006`, and does not restore or reference any prior VAL-003
  or VAL-006 evidence.
- **Implementation limitation.** This record does not authorize any
  source-model, accessibility, or other implementation action, and does
  not authorize any edit to `docs/kbdl/accessibility.md` or any other
  protected file.
- **Readiness/completion limitation.** This record does not approve
  candidate readiness, implementation conformance, or project
  completion. Candidate status remains NOT READY — SOURCE-INDEPENDENCE
  AND CLAUSE-EVIDENCE REMEDIATION REQUIRED; implementation conformance
  remains NOT VERIFIED; project completion remains PENDING.
- **Scope limitation.** This record does not approve, decide, or begin
  KBDL-011-SMR2, another roadmap item, or any other Batch A issue. It
  covers `SMR1-VC-0001` alone.
- **Required later metadata-recording and planning-validation gate.** A
  later, separate metadata-recording prompt for `KBDL-A11Y-001`'s
  validation-classification field, and a separate planning-agent
  validation of that prompt, are required before this decision takes any
  effect in normative or traceability metadata. This record alone does
  not change any effective authority, validation, or traceability
  metadata.

## Implementation authorization status

Implementation authorization status: NOT AUTHORIZED

This record does not authorize, approve, unlock, or ready any
implementation, limitation-acceptance, readiness, conformance, or
completion action. `scripts/decision_state.py` fails validation closed
if this field is ever anything other than the literal string
`NOT AUTHORIZED`.

## Scope

This record covers only `SMR1-VC-0001`. It does not select, approve, or
preselect any decision for any of the other 58 Batch A issues, for
`SMR1-KL-0001`, or for any of the other 417 canonical issues in
`issue-register.csv`, all of which remain literally `PENDING` in every
Owner decision / Owner decision date / Owner evidence field. Combined
with the three already-recorded Batch H decisions
(`batch-h-owner-decision-record.md`), this brings the total number of
durably recorded owner decisions in the packet to four; 417 canonical
issues remain PENDING.

---

Rollback: this record is part of the single Batch A / SMR1-VC-0001
owner-decision-recording commit (KBDL-011-SMR1-BA-OD1-DR1); rollback
uses `git revert <DR1-COMMIT-SHA>` of that whole commit, not a separate
reversion of this file alone.
