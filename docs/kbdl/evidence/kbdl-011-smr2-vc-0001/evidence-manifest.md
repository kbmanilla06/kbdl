# KBDL-011-SMR2-VC-0001 (reissued) Evidence Manifest

This package records the effect of one approved project-owner decision
(`SMR1-VC-0001`) on one field (`Validation classification`) of one requirement
(`KBDL-A11Y-001`). It is read-only with respect to every other requirement,
every other issue, every R13–R16 evidence package, `traceability-matrix.md`,
`validation.md`, `decision-register.md`, every owner-decision record, and
`project-owner-review.md`.

Implementation authorization status: NOT AUTHORIZED

## The value did not change

`KBDL-A11Y-001`'s validation classification was `Not verified` before and is
`Not verified` after. This step created no validation outcome. It made the value
resolvable **from its permitted source class** by giving the normative record an
explicitly parseable `Validation status:` field and naming the durable owner
decision as its current, non-retroactive authority.

Previously the label was split across a line wrap (`Validation` / `status:`), so
no independent parse found the normative field at all; the live registry
reported `Normative value: ABSENT` and `Authoritative expected value:
UNRESOLVED`. The ledger and readable group both already showed `Not verified`,
but neither may prove a normative-owned field — that is the source self-proof
the SMR1 audit exists to prevent.

## Authority is not evidence

The owner decision is decision authority only. It is not evidence that
accessibility testing, screen-reader verification, automated checking, or WCAG
conformance assessment occurred. The validation method
(`Manual + automated static accessibility check once implemented`) remains
unexecuted; the validation evidence continues to say so; the known limitation is
unchanged; and the durable record's reference is deliberately placed in
`Notes or exclusions`, never in `Validation evidence`.

## The live registry is derived

The live field-source registry is a derived, non-authoritative description of
the current source model — not authority, not a normative source, not validation
evidence, not an owner-decision record, not implementation authorization. It was
regenerated **only** through the approved FSRG1 generator and never hand-edited;
`--check` verifies byte-for-byte reproduction. Exactly two rows changed
(`Validation classification` and `Notes or exclusions`, both for
`KBDL-A11Y-001`), and exactly one row changed validation result, `FAIL` → `PASS`.
Row, requirement, field, and duplicate-key counts are unchanged at
5,389 / 317 / 17 / 0.

## Validation architecture

`scripts/validate_smr2_vc_0001.py` runs 30 fail-closed checks covering the
durable record, the normative block, the structured traceability row, the
related and sibling issues, the live registry row and its scope, the issue
state, decision counts, gate preservation, and the changed-file allowlist. A
missing file or an impossible comparison is a `FAIL`, never a skip. It never
regenerates the registry and never writes to the repository.

`scripts/smr2_vc_0001_fixtures.py` proves 24 negative fixtures are rejected and
6 positive controls pass, on one temporary repository copy restored between
fixtures. The real repository is hashed before and after and `git status
--short` compared; a cleanup failure fails the suite.

`decision_state.py` gains the second permitted status,
`METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION`, admitted **only** when
MD1–MD8 all hold: authorized issue only, matching non-deferred durable record,
parseable normative value, exact authority-record citation, current and
non-retroactive language that is not evidence, matching traceability row with
the reference outside `Validation evidence`, a resolving and passing registry
row, and no final-resolution claim. New check `7e` rejects any
resolved/closed/verified/validated status. No existing owner-decision check was
weakened.

`smr2_vc_0001_integration.py` adds nine read-only `VC1.*` checks to the SMR1
packet validator.

## Boundaries

Decision counts are unchanged at 4 durably recorded (3 Batch H, 1 Batch A) and
417 pending — metadata recording does not create a fifth decision.
`SMR1-KL-0001` remains `PENDING`. The other 58 Batch A validation-classification
issues remain `PENDING`. `KBDL-VAL-003` and `KBDL-VAL-006` remain `Not verified`
and are not restored. Candidate readiness remains NOT READY, implementation
conformance NOT VERIFIED, project completion PENDING. Batch A as a whole remains
locked, and no later prompt is unlocked by this implementation.

Metadata is recorded; **planning-agent validation of this recording remains
required.**
