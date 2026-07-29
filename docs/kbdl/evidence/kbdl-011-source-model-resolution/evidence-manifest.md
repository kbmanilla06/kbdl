# KBDL-011-SMR1 Evidence Manifest

This package prepares the non-normative R16 source-model resolution
packet. It is read-only with respect to every R16/R16A artifact —
`docs/kbdl/evidence/kbdl-011-r16/` is never modified by this packet; it is
only read by `scripts/reconciliation_compute.py` and
`scripts/generate_issue_register.py`.

`scripts/reconciliation_compute.py` reproduces the raw-findings and
per-category computation directly from
`docs/kbdl/evidence/kbdl-011-r16/artifacts/*.csv`. `scripts/generate_issue_register.py`
independently reproduces the full `issue-register.csv` (421 rows) from the
same source CSVs — every current-candidate value, candidate source,
permitted-authoritative-source type, and defect-category cell in
`issue-register.csv` is copied verbatim from the R16 artifacts, not
authored by hand. `scripts/validate_packet.py` re-derives the reconciled
counts and checks all 24 required validation points programmatically.

Path equivalents mirrored from the R16A package's conventions:
`source-model-resolution-ledger.csv` plays the role R16A's
`production-summary.txt` played — a computed reconciliation record — but
in CSV form with one row per metric and its computation basis, so every
number in `implementation-report.md` is traceable to a specific
computation rather than restated without a source.

`issue-register.csv` is the canonical, single register: every one of
R16's 693 raw `defects.csv` rows maps either to exactly one of the 421
canonical issues or is documented, in that issue's `Notes` column, as
sharing an already-counted issue with another raw finding (274 such
shared findings — see `source-model-resolution-ledger.csv`).

The MOT-007/MOT-008 authority cycle is represented by three separate,
independently decidable rows (`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`,
`SMR1-MOTCYCLE-0001`) rather than folded into the general Authority-field
or Validation-classification batches, per the SMR1 specification's
requirement for a separate, prominent cycle review record.

Every `Owner decision`, `Owner decision date`, and `Owner evidence` cell
across all 421 rows of `issue-register.csv` was the literal string
`PENDING` as prepared by KBDL-011-SMR1 (commit 662ee28).

As of KBDL-011-SMR1-BH-R1, three of those 421 rows (Batch H:
`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001`) carry a
recorded owner decision, backed by the durable record
`batch-h-owner-decision-record.md`. `scripts/decision_state.py` (invoked
by `scripts/validate_packet.py`, checks 7/7b/7c/7d/8/25–31) asserts
programmatically that: every non-`PENDING` cell exactly matches a durable
owner-decision record (issue ID, choice, date, evidence reference,
resolution status); every other cell remains literally `PENDING`; every
`project-owner-review.md` checkbox selection is backed by, and exactly
matches, that same durable record; no durable record is duplicated,
references an unknown issue ID, or claims implementation authorization;
and it fails closed if any of these conditions is violated.
