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
by `scripts/validate_packet.py`, checks 7/7b/7c/7d/8/D1–D3/D6–D7/D9–D12)
asserts programmatically that: every non-`PENDING` cell exactly matches a
durable owner-decision record (issue ID, choice, date, evidence
reference, resolution status); every other cell remains literally
`PENDING`; every `project-owner-review.md` checkbox selection is backed
by, and exactly matches, that same durable record; no durable record is
duplicated, references an unknown issue ID, or claims implementation
authorization; and it fails closed if any of these conditions is
violated.

`KBDL-011-SMR1-BH-R1` durably recorded the three Batch H decisions but
left `source-model-resolution-packet.md` and `project-owner-review.md`'s
own descriptive prose (opening statement, contents-table cells, and
sign-off table) describing the pre-BH-R1, zero-decision state.
`KBDL-011-SMR1-BH-R2` is the narrow follow-up that corrects that stale
prose, completes the sign-off summary, and extends
`scripts/decision_state.py` with five new checks (PS1–PS5) that verify
the packet's own state description is not stale or contradictory: when
durable decisions exist, neither document may claim zero decisions are
recorded or every checkbox unselected; the stated recorded/pending
counts must match the computed counts; the historical (`662ee28`) and
current states must remain distinguished; the review-cycle sign-off
summary must match the durable record; and no document may introduce
implementation-authorization language. `scripts/negative_fixtures.py` now
proves 8/8 deterministic negative fixtures fail validation as expected —
the original six (BH-R1) plus two new stale-prose regressions
(`stale_packet_overview`, `stale_review_summary`) added by BH-R2 — all
operating on temporary copies only, with the real packet files verified
byte-unchanged after every fixture run. `batch-h-r2-validation-
transcript.txt` durably captures the BH-R2 command/output evidence
(positive validator run, all 8 negative fixtures, protected-field audit,
checksum verification, commit, and push).

`KBDL-011-SMR1-BH-AGC1` applies the three recorded Batch H decisions to
the current authoritative source model in `docs/kbdl/motion/README.md`
and `docs/kbdl/traceability-metadata.csv`: `KBDL-MOT-007` and
`KBDL-MOT-008` now each independently cite `KBDL-DEC-014`, decision
packet item 2, as authority, and their relationship is represented only
as related-requirement, in both directions — removing the two-node
authority edge R16 originally detected (that historical finding remains
unchanged in `docs/kbdl/evidence/kbdl-011-r16/`). `scripts/
authority_graph.py` parses this current state and asserts independent
authority, related-requirement-only classification, cycle absence, and
lifecycle/provenance/validation-status stability;
`scripts/authority_graph_fixtures.py` proves 8 deterministic negative
fixtures (both edges, both directions, authority removal ×2,
misclassification, validation-status drift, and the recorded/pending
count) fail as expected, on in-memory or temp-copy state only.
`scripts/validate_packet.py` gained 12 `AG.*` checks plus 3
`AG.narrow_authorized_diff.*` scope checks, and its protected-file
check (12) and unrelated-change check (22) now recognize these two
specifically authorized files without weakening protection of
`validation.md`, `decision-register.md`, `traceability-matrix.md`, or
`motion/timing-easing.md`, all of which remain byte-identical.
`authority-graph-agc1-validation-transcript.txt` durably captures the
before/after authority-graph text, the positive and negative validation
output, the protected-file/scope audit, and the decision-register
determination (no new entry created; `KBDL-DEC-014` unchanged).
