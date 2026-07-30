# KBDL-011-SMR2-VC-0001 (reissued) — Validation-Classification Metadata Recording

This package records the effect of one approved project-owner decision, for one
requirement, in one field.

| | |
| --- | --- |
| Resolution issue | `SMR1-VC-0001` |
| Requirement | `KBDL-A11Y-001` |
| Field | Validation classification |
| Value | `Not verified` — **unchanged** |
| Owner choice | `SET TO NOT VERIFIED` |
| Durable authority record | `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29` |

Implementation authorization status: NOT AUTHORIZED

## Scope

**One issue and one field.** No other Batch A issue, no other requirement, and
no other traceability row is processed. `SMR1-KL-0001` — the Known-limitation
issue for this same requirement — remains `PENDING` and untouched.

## The classification did not change

`KBDL-A11Y-001`'s validation classification was `Not verified` before this step
and is `Not verified` after it. This step did not produce a new validation
outcome. What it changed is that the value is now **stated in its own
authoritative source** — the normative requirement record — with the durable
owner decision named as its authority.

Before, the normative record's label was split across a line wrap
(`Validation` / `status:`), so no independent parse of the normative source
found the field at all. The live registry therefore reported the field as
`Normative value: ABSENT`, `Authoritative expected value: UNRESOLVED`,
`Validation result: FAIL` — while the ledger and the readable traceability
group both already showed `Not verified`. Neither of those may prove itself:
a traceability candidate cannot be its own authority. Making the normative
field contiguous and citing the owner decision resolves the field from its
permitted source class (`A — Normative-owned`).

## Authority is not evidence

The owner decision is **current, non-retroactive decision authority** for
retaining the classification. It is not, and is never represented as:

* proof that accessibility testing occurred;
* proof of screen-reader compatibility;
* proof that an automated accessibility check ran;
* WCAG conformance;
* a validation result.

The requirement's validation method — `Manual + automated static accessibility
check once implemented` — remains unexecuted, its validation evidence continues
to say so, and its known limitation is unchanged.

## The live registry is derived

The live field-source registry is a derived, non-authoritative description of
the current source model. It is not authority, a normative source, validation
evidence, an owner-decision record, or implementation authorization. It was
**regenerated through the approved FSRG1 generator** and never hand-edited.

## Contents

| Path | Purpose |
| --- | --- |
| `scripts/validate_smr2_vc_0001.py` | 30 fail-closed checks over the whole recording. |
| `scripts/smr2_vc_0001_fixtures.py` | 24 negative fixtures and 6 positive controls. |
| `smr2-vc-0001-validation-transcript.txt` | Durable command/output evidence. |
| `implementation-report.md` | What changed, what did not, and the regression results. |
| `evidence-manifest.md`, `evidence-inventory.csv`, `checksums.sha256` | Evidence-integrity records. |

## Verify

```bash
python3 docs/kbdl/evidence/kbdl-011-smr2-vc-0001/scripts/validate_smr2_vc_0001.py --repo-root .
python3 docs/kbdl/evidence/kbdl-011-smr2-vc-0001/scripts/smr2_vc_0001_fixtures.py --repo-root .
```

## Status

Metadata is recorded. **Planning-agent validation of this recording is still
required.** `SMR1-VC-0001` is marked
`METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION` — not resolved, not
closed, not verified, not validated.

No VAL status moved: `KBDL-VAL-003` and `KBDL-VAL-006` remain `Not verified`.
Candidate readiness remains NOT READY, implementation conformance remains NOT
VERIFIED, project completion remains PENDING. Decision counts are unchanged at
4 durably recorded / 417 pending — metadata recording does not create a fifth
decision. No implementation is authorized.
