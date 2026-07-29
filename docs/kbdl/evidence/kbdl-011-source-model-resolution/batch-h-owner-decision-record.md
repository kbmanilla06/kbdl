# Durable Project-Owner Decision Record — Batch H (KBDL-011-SMR1)

Record title: Batch H (MOT-007/MOT-008 authority cycle) owner-decision record.
Record identifier: `KBDL-SMR1-BH-OWNER-DECISION-2026-07-29`.
Decision date: 2026-07-29.
Timezone: Asia/Manila.
Project-owner authority: the current project owner, recording a decision
against `docs/kbdl/evidence/kbdl-011-source-model-resolution/project-owner-review.md`,
Batch H ("MOT-007 / MOT-008 authority cycle").

This record exists because a packet-review decision, once selected, must
have durable evidence independent of the packet itself — the packet
cannot prove its own authority, and `KBDL-DEC-014` alone is not evidence
that these three packet choices were selected on 2026-07-29 (only this
record is).

## Decisions recorded (exactly three, verbatim, not broadened)

- `SMR1-MOTEDGE-0001` — edge `KBDL-MOT-007 → KBDL-MOT-008`: **RELATED
  REQUIREMENT**. This edge is classified as a related-requirement
  relationship, not an authority edge.
- `SMR1-MOTEDGE-0002` — edge `KBDL-MOT-008 → KBDL-MOT-007`: **RELATED
  REQUIREMENT**. This edge is classified as a related-requirement
  relationship, not an authority edge.
- `SMR1-MOTCYCLE-0001` — cycle `KBDL-MOT-007 → KBDL-MOT-008 → KBDL-MOT-007`:
  **REPLACE BOTH EDGES WITH SHARED INDEPENDENT AUTHORITY**. Both
  requirements are intended to rely on shared independent authority from
  `KBDL-DEC-014`, decision-packet item 2, rather than on each other's
  authority text.

## Machine-readable decision block

The table below is the authoritative, parseable record consumed by
`scripts/decision_state.py`. Every cell must match `issue-register.csv`
and `project-owner-review.md` exactly for these three issue IDs.

| Issue ID | Selected choice | Decision date | Timezone | Evidence record ID |
| --- | --- | --- | --- | --- |
| SMR1-MOTEDGE-0001 | RELATED REQUIREMENT | 2026-07-29 | Asia/Manila | KBDL-SMR1-BH-OWNER-DECISION-2026-07-29 |
| SMR1-MOTEDGE-0002 | RELATED REQUIREMENT | 2026-07-29 | Asia/Manila | KBDL-SMR1-BH-OWNER-DECISION-2026-07-29 |
| SMR1-MOTCYCLE-0001 | REPLACE BOTH EDGES WITH SHARED INDEPENDENT AUTHORITY | 2026-07-29 | Asia/Manila | KBDL-SMR1-BH-OWNER-DECISION-2026-07-29 |

## Selected substantive authority (distinct from this record)

The selected shared independent authority for the cycle-level decision is
`KBDL-DEC-014`, decision-packet item 2
(`docs/kbdl/motion/README.md` §10, table row 2; see
`docs/kbdl/decision-register.md` §"KBDL-DEC-014 — KBDL-005 motion
decisions approved"). **This record proves that the project owner
selected the three Batch H packet choices on 2026-07-29. It does not
prove that the selected relationship classifications or authority
expressions were historically approved before that date.** `KBDL-DEC-014`
is the separately-existing, previously-approved substantive authority
cited by the cycle-level choice — it is not, by itself, evidence of the
current selection recorded here, and the current selection is not, by
itself, evidence that `KBDL-DEC-014` was historically understood to cover
this exact classification.

## Boundaries and limitations (all apply; none is waived)

- **Current and non-retroactive effect.** This record documents a
  current project-owner decision made on 2026-07-29. It does not
  reconstruct or assert any earlier historical approval of this specific
  relationship classification.
- **Historical-approval limitation.** This record proves selection on
  2026-07-29 only, per the paragraph above.
- **Effective-metadata limitation.** The selected choices do not take
  effect in normative or governance metadata through this record alone.
  A separate metadata-recording prompt and planning-agent validation are
  required. **This record does not itself change any effective authority
  metadata.**
- **Validation limitation.** This record does not restore `KBDL-VAL-003`
  or any other validation gate. `KBDL-VAL-003` remains Not verified.
- **Implementation limitation.** This record does not authorize
  source-model implementation and does not authorize any edit to
  `docs/kbdl/motion/README.md`, `docs/kbdl/motion/timing-easing.md`, or
  any other protected file.
- **Readiness/completion limitation.** This record does not approve
  candidate readiness, implementation conformance, or project completion.
  Candidate status remains NOT READY — SOURCE-INDEPENDENCE AND
  CLAUSE-EVIDENCE REMEDIATION REQUIRED; implementation conformance
  remains NOT VERIFIED; project completion remains PENDING.
- **Required next approval gate.** A later metadata-recording prompt
  (e.g. the future "KBDL-011-SMR9: MOT-007/MOT-008 authority-graph
  correction" prompt named in `implementation-unlock-map.md` Batch H)
  requires separate planning-agent authorization after this remediation,
  KBDL-011-SMR1-BH-R1, passes validation.

## Implementation authorization status

Implementation authorization status: NOT AUTHORIZED

This record does not authorize, approve, unlock, or ready any
implementation, limitation-acceptance, readiness, conformance, or
completion action. `scripts/decision_state.py` fails validation closed if
this field is ever anything other than the literal string
`NOT AUTHORIZED`.

## Scope

This record covers only the three Batch H issue IDs listed above. It
does not select, approve, or preselect any decision for any of the other
418 canonical issues in `issue-register.csv`, all of which remain
literally `PENDING` in every Owner decision / Owner decision date / Owner
evidence field.

---

Rollback: this record is part of the single Batch H owner-decision-
recording commit; rollback uses `git revert <FINAL-BATCH-H-COMMIT-SHA>`
of that whole commit, not a separate reversion of this file alone.
