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

`KBDL-011-SMR1-BH-AGC1-VF1` is a validator-tooling-only correction found
necessary by a clean post-publication evidence run: the three
`AG.narrow_authorized_diff.*` checks compared the working tree against
symbolic `HEAD`, which is empty once the AGC1 correction is committed
and the tree is clean — the row-count check then failed on `added=0
removed=0`, and the other two checks passed vacuously on that same
empty diff. `scripts/agc1_narrow_diff.py` replaces that design: it
evaluates all three checks against the fixed, immutable historical
range `46104c57f86a924b197f6ed380a5b1127eddbf7d
..0fadb9713299fb861830e419e06da8d82175ea1a`, never symbolic `HEAD`, and
fails closed on a missing commit, a wrong-parent target, a failed `git`
invocation, or an empty diff — none of these can pass vacuously.
`scripts/agc1_narrow_diff_fixtures.py` proves this against ten required
scenarios plus the mandatory HEAD-independence case (the historical
range still passes after HEAD advances past the target commit),
entirely inside temporary, disposable Git repositories, never touching
the real repository. `authority-graph-agc1-vf1-validation-
transcript.txt` durably captures the pre-fix 69/70 run, the root-cause
analysis, the fixture results, and the post-fix clean pre-commit/
post-commit/post-push validation runs. This correction is additive: the
`0fadb97` commit and message are unchanged; the BH-AGC1 authority
correction's substance is unaffected; only the previously
non-reproducible "70/70" validator claim is superseded. At the
historical VF1 point, the three Batch H decisions and the other 418
PENDING SMR1 issues were unchanged (superseded by the current
4-recorded/417-pending state as of `KBDL-011-SMR1-BA-OD1-DR1-R1`, which
also records that `KBDL-011-SMR1-BH-AGC1` and
`KBDL-011-SMR1-BH-AGC1-VF1` have since passed planning-agent
validation); no VAL status, lifecycle, provenance, or
implementation-authorization status changed; no implementation action is
authorized.

`KBDL-011-SMR1-BA-OD1-DR1` durably records exactly one Batch A decision
— `SMR1-VC-0001` (`KBDL-A11Y-001` validation classification) = SET TO
NOT VERIFIED — reusing the same generic durable-record architecture
`decision_state.py` already used for Batch H; no parallel
Batch-A-specific engine was introduced. `batch-a-smr1-vc-0001-owner-
decision-record.md` is the durable current-owner evidence for this
decision (record `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29`);
`issue-register.csv`'s `SMR1-VC-0001` row and `project-owner-review.md`'s
new dedicated issue-level block for `SMR1-VC-0001` are updated to match
it exactly, while `SMR1-KL-0001` and every other Batch A issue and other
417 canonical issues remain literally `PENDING`.
`source-model-resolution-ledger.csv`'s durable-decision metric is
generalized from a Batch-H-only label to a total metric (`Total durably
recorded owner decisions: 4`) plus explicit per-batch rows (`Batch H
recorded decisions: 3`; `Batch A recorded decisions: 1`), and
`scripts/decision_state.py` gains a generic per-batch/per-record-file
breakdown check (D13) plus a Batch H historical-count invariant (D14).
`scripts/negative_fixtures.py` now proves 20/20 deterministic negative
fixtures fail validation as expected — the original 8 (BH-R1/BH-R2) plus
12 new Batch A fixtures covering an unbacked change, a
recorded-but-pending row, a choice mismatch, a date mismatch, a wrong
evidence reference, a review-form mismatch, multiple selections, an
unauthorized second Batch A issue, a duplicate durable record, an
implementation-authorizing record, stale packet prose, and stale ledger
counts — all operating on temporary copies only, with the real packet
files verified byte-unchanged after every fixture run.
`batch-a-od1-dr1-validation-transcript.txt` durably captures the
BA-OD1-DR1 command/output evidence. This step does not apply the SET TO
NOT VERIFIED classification to effective normative or traceability
metadata, does not change lifecycle or provenance, does not resolve
`SMR1-KL-0001`, does not restore `VAL-003` or `VAL-006`, and does not
authorize implementation.

`KBDL-011-SMR1-BA-OD1-DR1-R1` is a prose-and-validator-only remediation
found necessary by planning-agent review of `KBDL-011-SMR1-BA-OD1-DR1`:
(1) `batch-a-smr1-vc-0001-owner-decision-record.md` contained language
saying the `SET TO NOT VERIFIED` selection "selects no new authority,
source, or evidence," contradicting the approved meaning that the
decision creates new current, non-retroactive authority for retaining
the `Not verified` classification; (2) several current-state passages
across `source-model-resolution-packet.md`, `project-owner-review.md`,
`implementation-report.md`, and this manifest still read (or could be
misread) as reporting 418 pending issues or pending AGC1/VF1
planning-agent validation as current state, when the current state is
417 pending and AGC1/VF1 have both passed; (3) `scripts/decision_state.py`
had no check that would catch either defect. DR1-R1: (a) corrects the
durable record's authority wording (adding the required "creates new
current, non-retroactive authority" / "decision authority only, not
[testing] evidence" sentences) without changing the selected choice,
issue ID, requirement ID, decision date, timezone, evidence identifier,
or Implementation authorization status; (b) adds explicit historical
markers to every preserved historical 418/three-recorded mention and
corrects every current-state mention to 417/four-recorded, and to state
that AGC1/VF1 have passed planning-agent validation while DR1-R1 was, at
that point, the then-current open gate (DR1-R1 has since itself passed —
see the RM1 paragraph below); (c) extends `scripts/decision_state.py` with
new fail-closed checks (`AR1`, `AR2`, `SP1`–`SP4`) covering the authority
contradiction, the evidence-conflation risk, stale current-state 418/
three-recorded prose lacking a historical marker, stale "AGC1/VF1
pending" prose, and count-arithmetic consistency; (d) adds
`scripts/dr1_r1_fixtures.py`, ten new deterministic fixtures (eight
rejection fixtures plus two positive-control fixtures) proving the new
checks fail closed and that the corrected repository state still
passes, all on temporary copies only; (e) adds
`batch-a-od1-dr1-r1-validation-transcript.txt`; and (f) regenerates
`evidence-inventory.csv` and `checksums.sha256`. DR1-R1 does not reopen,
reinterpret, or change the `SMR1-VC-0001` = SET TO NOT VERIFIED decision
itself, does not change any protected file, does not resolve
`SMR1-KL-0001`, does not restore `VAL-003`/`VAL-006`, and does not
authorize implementation.

`KBDL-011-SMR1-RM1` records the project owner's 2026-07-29 **APPROVE
WITH CHANGES** disposition on the proposed `KBDL-011-SMR2-VC-0001`
metadata-recording prompt, which directed that a prerequisite roadmap
prompt be added first. `smr2-fsrg1-prompt.md` specifies that prerequisite,
`KBDL-011-SMR2-FSRG1`: a live, current-state field-source-registry
artifact and a deterministic generator, with a declared schema, a
validator, fixtures, and a transcript. It exists because
`implementation-unlock-map.md`'s Batch A entry requires
`field-source-registry.csv` to be *regenerated, not hand-edited*, while
the repository's only four registries — under `kbdl-011-r13`,
`kbdl-011-r14`, `kbdl-011-r15`, and `kbdl-011-r16` — are point-in-time
round audit artifacts emitted by those rounds' own validators, leaving no
live registry and no standalone generator for a recording prompt to
invoke. All four are preserved as immutable historical evidence: RM1
leaves them byte-identical, never regenerates or relocates them, and
never adopts one as a generator output path. `implementation-unlock-map.md`
gains a prerequisite `KBDL-011-SMR2-FSRG1` entry and a downstream
`KBDL-011-SMR2-VC-0001` entry, both at
`LOCKED — PLANNING-AGENT VALIDATION REQUIRED`; the downstream prompt is
released only after FSRG1 passes planning-agent validation, and is then
reissued against the approved generator rather than resumed.
`scripts/fsrg1_roadmap.py` adds six fail-closed checks (FR1–FR6) over
that roadmap record — specification present and disclaiming
authorization, all six mandatory gates stated (schema, determinism,
drift, path-safety, fixture-isolation, clean post-publication), all four
historical registries named and declared immutable, those registries
verified against the SHA-256 digests recorded in their own round evidence
inventories, both roadmap entries LOCKED with the gate and reissue
requirement stated, and no language promoting either prompt out of that
state. `scripts/fsrg1_roadmap_fixtures.py` proves 12/12 deterministic
fixtures behave as specified (ten rejection, two positive-control), on
temporary copies and a synthetic temporary repository root only, with
every real repository file verified byte-unchanged after the run.

`KBDL-011-SMR2-FSRG1` then implements that prerequisite as the package
`docs/kbdl/evidence/kbdl-011-smr2-fsrg1/`: a deterministic standalone
generator, the live current-state field-source registry (5,389 rows =
317 requirements × 17 fields), a declared schema contract at version 1, the
FSRG1 validator reporting twelve gate groups, 24 negative and 8
positive-control fixtures, and a durable transcript. All six required gates —
schema, determinism, drift, path-safety, fixture-isolation, and clean
post-publication validation — are implemented fail-closed and pass. The live
registry is derived and non-authoritative; it is never hand-edited, and the
generator never reads a field-source registry, including its own output. The
four R13–R16 registries remain byte-identical immutable historical evidence,
verified on every run against the digests recorded in their own round
inventories. Inside this packet, FSRG1 adds `scripts/fsrg1_integration.py` and
eleven read-only `FSRG1.*` checks to `scripts/validate_packet.py`, weakening or
removing no existing check. Implementation is not validation:
`KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`, and
`KBDL-011-SMR2-VC-0001` was not begun, resumed, or reissued.

RM1 also records, on the same 2026-07-29 owner disposition, that
`KBDL-011-SMR1-BA-OD1-DR1-R1` is **PASSED — PLANNING-AGENT VALIDATED**
and is not an open gate; planning-agent validation of `KBDL-011-SMR1-RM1`
itself is now the only open gate. And RM1's regeneration of
`evidence-inventory.csv` and `checksums.sha256` closes a pre-existing
omission: `batch-a-od1-dr1-validation-transcript.txt`, the durable
transcript added by `KBDL-011-SMR1-BA-OD1-DR1`, existed in the packet but
was never listed in `evidence-inventory.csv`. **Only the inventory record
is corrected — the transcript file itself is byte-identical to the copy
published by `KBDL-011-SMR1-BA-OD1-DR1` and is neither rewritten,
re-run, re-dated, nor otherwise touched by RM1.** The inventory now
covers every packet file except `evidence-inventory.csv` and
`checksums.sha256` themselves, which by the packet's existing convention
are not listed inside themselves. RM1
prepares, authorizes, and runs no generator; creates no live registry;
issues no prompt; changes no normative content, no effective metadata,
and no protected file; restores no VAL status; and records, reopens, or
preselects no owner decision.

The reissued `KBDL-011-SMR2-VC-0001` records the approved `SMR1-VC-0001`
decision into effective metadata for one requirement and one field.
`KBDL-A11Y-001`'s validation classification is **unchanged** (`Not verified`);
what changed is that its normative record now states the value as an explicitly
parseable `Validation status:` field and cites
`KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29` as current, non-retroactive
decision authority — decision authority only, never validation evidence. The
previous `UNRESOLVED`/`FAIL` state was caused solely by the normative label
being split across a line wrap, so no independent parse found it; neither the
ledger nor the readable group may prove a normative-owned field. The structured
traceability row carries the same reference in `Notes or exclusions`, never in
`Validation evidence`. The live registry was regenerated through the approved
FSRG1 generator and never hand-edited: exactly two rows changed, exactly one
moved `FAIL` → `PASS`, and counts hold at 5,389 rows / 317 requirements / 17
fields / 0 duplicates. `scripts/decision_state.py` admits the new
`METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION` status only when
MD1-MD8 all hold, and new check `7e` rejects any final-resolution claim;
`scripts/smr2_vc_0001_integration.py` adds nine read-only `VC1.*` checks. No
lifecycle, provenance, method, evidence, or limitation changed; `SMR1-KL-0001`
and the other 58 Batch A issues remain PENDING; VAL-003/VAL-006, readiness,
conformance, and completion are unmoved; decision counts remain 4 recorded /
417 pending. Planning-agent validation of this recording remains required.

`KBDL-011-SMR2-VC-0001-PA1` records the planning-agent `PASS` for the reissued
`KBDL-011-SMR2-VC-0001` in the durable record
`KBDL-SMR2-VC-0001-PLANNING-AGENT-VALIDATION-2026-07-30`, covering commits
`af6a60a`, `4aba456`, and `448e39b`, and advances `SMR1-VC-0001` to
`METADATA RECORDED — PLANNING-AGENT VALIDATED`. That record is deliberately not
an owner-decision record — it uses a different filename convention and a
different parser — so it can never be counted as a fifth decision;
`scripts/decision_state.py` PA1–PA12 enforce this and every field of the record,
and PA12 asserts the separation directly. The sole next owner-review target is
`SMR1-VC-0002` (`KBDL-A11Y-004`), a queue designation only: its owner fields
remain `PENDING`, no durable record exists, every checkbox in its review block
is unselected, no metadata-recording prompt for it is eligible, and Batch A
remains `LOCKED — OWNER DECISION REQUIRED`.
`scripts/smr2_vc_0001_integration.py` QUEUE1–QUEUE12 enforce exactly one named
current target, its untouched pending state, and the absence of any eligibility
claim. Classification, effective metadata, the live registry, VAL states,
readiness, conformance, completion, and the decision counts (4 recorded / 417
pending) are all unchanged.
