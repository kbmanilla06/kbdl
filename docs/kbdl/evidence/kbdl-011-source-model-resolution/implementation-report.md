# KBDL-011-SMR1 Implementation Report

Implementation-step status: PASS. This packet prepares a non-normative
source-model resolution decision set. It resolves nothing.

R16 raw findings mapped: 693
Canonical resolution issues: 421
Distinct affected requirements: 289
Cross-category overlaps: 274
Unmapped findings: 0
Duplicate canonical issues: 0

Validation-classification decisions: 59
Authority-source decisions: 21
Validation-evidence decisions: 14
Validation-method decisions: 12
Limitation decisions: 229
Location decisions: 63
Standard-clause decisions: 20
MOT edge decisions: 2
MOT cycle decisions: 1

Preselected owner decisions: 0
Total durably recorded owner decisions: 4
Durably recorded owner decisions (Batch H, KBDL-011-SMR1-BH-R1): 3
Durably recorded owner decisions (Batch A, KBDL-011-SMR1-BA-OD1-DR1): 1
Other owner decisions remaining PENDING: 417
Protected-field changes: 0
VAL-status changes: 0
Accepted limitations: 0
Readiness approvals: 0
Implementation authorizations: 0
Completion approvals: 0

Implementation conformance: NOT VERIFIED
Project completion: PENDING

## Basis for these numbers

Every figure above is computed directly from
`docs/kbdl/evidence/kbdl-011-r16/artifacts/` by
`scripts/reconciliation_compute.py` and cross-checked by
`scripts/generate_issue_register.py` (which independently produces
`issue-register.csv`, whose row count is the canonical-resolution-issues
figure) and `scripts/validate_packet.py` (which re-derives the
unmapped/duplicate/PENDING figures programmatically). See
`source-model-resolution-ledger.csv` for the full arithmetic, including
why 693 raw findings collapse to 421 canonical issues (274 findings are
documented as sharing an already-counted canonical issue rather than
creating a new one — see the ledger's per-row "Computation basis"
column).

The 289 distinct affected requirements figure reproduces the R16A
"Failed effective records: 289" figure exactly, confirming this packet's
population matches the validated R16A baseline rather than a
re-derivation that happens to differ.

## What was not done

No finding was resolved, suppressed, or converted into a PASS. No
protected field, VAL status, candidate status, implementation
conformance, or completion status changed. VAL-004's eleven clause
methods were not executed. No implementation package, application code,
dependency, schema, CI configuration, database, or deployment file was
added.

As of KBDL-011-SMR1-BH-R1, exactly 3 of the 421 canonical issues (Batch
H: `SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001`) carry a
durably recorded owner decision — see
`batch-h-owner-decision-record.md` — and their corresponding checkboxes
in `project-owner-review.md` are selected to match. As of
KBDL-011-SMR1-BA-OD1-DR1, one more canonical issue (`SMR1-VC-0001`,
Batch A) carries a durably recorded owner decision — see
`batch-a-smr1-vc-0001-owner-decision-record.md` — and its checkbox in
`project-owner-review.md` is selected to match. The other 417 rows
still hold the literal string `PENDING` in every Owner decision / Owner
decision date / Owner evidence cell, and no other checkbox in
`project-owner-review.md` is selected. `scripts/decision_state.py`
(invoked by `scripts/validate_packet.py`) fails validation closed if any
selected cell or checkbox lacks an exactly matching durable record, or if
any other cell/checkbox deviates from `PENDING`/unselected.

## KBDL-011-SMR1-BH-R2 correction

`KBDL-011-SMR1-BH-R1` durably recorded the three Batch H decisions but
left `source-model-resolution-packet.md`'s opening/contents-table
language and `project-owner-review.md`'s sign-off table describing the
pre-BH-R1, zero-decision state (commit `662ee28`). BH-R2 is a narrow,
documentation-only follow-up, published as one child commit of
`ea86add`, that: (1) corrects both documents so the historical
(`662ee28`: PREPARED — NO OWNER DECISIONS RECORDED) and current (OWNER
REVIEW IN PROGRESS — 3 DURABLY RECORDED BATCH H DECISIONS; 418 OTHER
ISSUES PENDING) states are stated without contradiction; (2) completes
`project-owner-review.md`'s review-cycle sign-off summary (3 decisions
recorded / Project owner / 2026-07-29 / Batch H / Implementation
authorization NOT AUTHORIZED / planning-agent validation PENDING); (3)
extends `scripts/decision_state.py` with five new state-prose checks
(PS1–PS5, invoked by `scripts/validate_packet.py`) that fail closed on
stale zero-decision claims, mismatched recorded/pending counts, a
missing historical/current distinction, a stale sign-off summary, or an
introduced implementation-authorization claim; (4) adds two new
regression fixtures (`stale_packet_overview`, `stale_review_summary`) to
`scripts/negative_fixtures.py`, bringing the total to 8/8 deterministic
negative fixtures, all still operating on temporary copies only; (5)
adds `batch-h-r2-validation-transcript.txt`, a durable command/output
transcript for this correction and its publication; and (6) regenerates
`checksums.sha256` and `evidence-inventory.csv`. BH-R2 selects no new
owner decision, changes no protected file, and authorizes no
implementation action; the exact three Batch H decisions and the other
418 PENDING issues are unchanged.

Stale packet-state statements after BH-R2: 0. Review-summary mismatches
after BH-R2: 0.

## KBDL-011-SMR1-BH-AGC1 authority-graph correction

`KBDL-011-SMR1-BH-AGC1` applies (not reopens or reinterprets) the three
already-durably-recorded Batch H decisions to the current authoritative
source model. It: (1) corrects `docs/kbdl/motion/README.md`'s and
`docs/kbdl/traceability-metadata.csv`'s Lifecycle-status/Authority text
for `KBDL-MOT-007` and `KBDL-MOT-008` so each independently cites
`KBDL-DEC-014`, decision packet item 2 — removing the
"together with `KBDL-MOT-00{7,8}`, as one timing system" clause that
R16 flagged as a circular authority edge; (2) adds an explicit
"Related requirement" bullet/note in both places, in both directions,
stating the relationship is related-requirement only and explicitly
disclaiming authority semantics; (3) adds
`scripts/authority_graph.py` (parses the current authority graph and
checks independent authority, related-requirement-only classification,
absence of the two-node cycle, and stability of lifecycle/provenance/
validation-status fields) and `scripts/authority_graph_fixtures.py` (8
deterministic negative fixtures covering both edges, both directions,
authority removal, misclassification, validation-status drift, and the
Batch H recorded/pending count, all in-memory/temp-copy only); (4) adds
12 new `AG.*` checks plus 3 `AG.narrow_authorized_diff.*` scope checks
to `scripts/validate_packet.py`, and narrows check 12's protected-file
list and check 22's allowlist to recognize these two specifically
authorized files without weakening protection of the other four
(`validation.md`, `decision-register.md`, `traceability-matrix.md`,
`motion/timing-easing.md`), all of which remain byte-identical; (5)
adds a §8 to `source-model-resolution-packet.md` distinguishing
historical cycle detection, the applied correction, pending
planning-agent validation, and remaining unresolved KBDL-011 work; (6)
adds `authority-graph-agc1-validation-transcript.txt`; and (7)
regenerates `checksums.sha256`/`evidence-inventory.csv`. No new
decision-register entry was created (see the transcript's
decision-register determination) — `KBDL-DEC-014`'s scope and meaning
are unchanged. The exact three Batch H decisions, the 418 other PENDING
issues, all four fully-protected files, requirement lifecycle/
provenance/validation-status, and every unrelated MOT requirement are
unchanged. No VAL status, candidate status, implementation conformance,
or completion status changed; no implementation action is authorized.

Authority-cycle status after BH-AGC1: removed (0 directional authority
edges between KBDL-MOT-007 and KBDL-MOT-008; historical R16 evidence of
the original cycle preserved unchanged).

## KBDL-011-SMR1-BH-AGC1-VF1 validator-reproducibility correction

`KBDL-011-SMR1-BH-AGC1-VF1` is a validator-tooling-only correction. It
does not reopen, reinterpret, or change the BH-AGC1 authority-graph
correction itself: `KBDL-MOT-007` and `KBDL-MOT-008` remain independently
authorized by `KBDL-DEC-014`, decision packet item 2; their relationship
remains related-requirement only, in both directions; the three Batch H
decisions and the other 418 PENDING SMR1 issues are unchanged; no VAL
status, lifecycle, provenance, or implementation-authorization status
changed.

A clean, post-publication run of `scripts/validate_packet.py` against
commit `0fadb9713299fb861830e419e06da8d82175ea1a` (parent
`46104c57f86a924b197f6ed380a5b1127eddbf7d`) reproducibly exited 1 with
69/70 checks passing, failing only
`AG.narrow_authorized_diff.csv_row_count_unchanged` (`added=0
removed=0`). Root cause: the three `AG.narrow_authorized_diff.*` checks
compared the working tree against symbolic `HEAD` (`git diff -U0 HEAD
-- <file>`), which was meaningful only pre-commit; once the AGC1
correction was committed and the tree became clean, that diff is empty
against the new HEAD, so the row-count check failed on `added=0
removed=0`, and the other two "only touches MOT-007/008" checks passed
*vacuously* on the same empty diff (an empty diff trivially contains no
disallowed content). The BH-AGC1 commit's own reported "70/70" claim
was therefore not reproducible from a clean post-publication checkout,
even though the underlying source-model correction was, and remains,
sound.

VF1 corrects this by adding `scripts/agc1_narrow_diff.py`, which
evaluates all three checks against the fixed, immutable historical
commit range `46104c57f86a924b197f6ed380a5b1127eddbf7d
..0fadb9713299fb861830e419e06da8d82175ea1a` — never symbolic `HEAD`,
`HEAD^`, the working tree, or the index — so the same correct result is
produced regardless of how many later commits (including this VF1
commit) exist on top. Every check fails closed: an unresolvable base or
target commit, a target whose direct parent is not the expected base, a
failed `git diff` invocation, or an empty diff, all FAIL; none can pass
vacuously. `scripts/validate_packet.py` now delegates its three
`AG.narrow_authorized_diff.*` checks to this module. A new regression
suite, `scripts/agc1_narrow_diff_fixtures.py`, exercises the mechanism
against ten required scenarios (valid change, empty diff, uncommitted-
only change, one-row-only change, unrelated-row change, added row,
deleted row, unrelated README change, wrong-parent commit, missing
commit) plus the mandatory HEAD-independence case (the historical range
still passes after HEAD advances to a later child commit) — entirely
inside temporary, disposable Git repositories it creates and destroys
itself, never touching the real repository.

This correction is additive evidence: it does not amend or rewrite the
`0fadb97` commit or its message, and does not retroactively claim
post-publication 70/70 evidence existed at BH-AGC1 commit time. The
original BH-AGC1 correction remains applied and its substance is
unaffected; VF1 only supersedes the non-reproducible validator claim.
Planning-agent validation of KBDL-011-SMR1-BH-AGC1 remains required;
KBDL-011 remains incomplete; the other 418 SMR1 issues remain PENDING;
no implementation action is authorized by this correction.

Changed files (validator-tooling and additive evidence only):
`scripts/validate_packet.py` (delegates the three narrow-diff checks to
the new module), `scripts/agc1_narrow_diff.py` (new), `scripts/
agc1_narrow_diff_fixtures.py` (new), `authority-graph-agc1-vf1-
validation-transcript.txt` (new), this report, `evidence-manifest.md`,
`source-model-resolution-packet.md`, `evidence-inventory.csv`, and
`checksums.sha256`. `docs/kbdl/motion/README.md`,
`docs/kbdl/traceability-metadata.csv`, `docs/kbdl/motion/
timing-easing.md`, `docs/kbdl/validation.md`,
`docs/kbdl/decision-register.md`, and `docs/kbdl/traceability-matrix.md`
remain byte-identical to `0fadb97`.

## KBDL-011-SMR1-BA-OD1-DR1 Batch A / SMR1-VC-0001 decision recording

`KBDL-011-SMR1-BA-OD1-DR1` durably records exactly one new project-owner
decision — `SMR1-VC-0001` (`KBDL-A11Y-001` validation classification) =
SET TO NOT VERIFIED, decided 2026-07-29, Asia/Manila — using the same
generic durable-record architecture already established by
`scripts/decision_state.py` for Batch H; no parallel Batch-A-specific
engine was built. It: (1) adds
`batch-a-smr1-vc-0001-owner-decision-record.md`, durable current-owner
evidence for this one decision (record
`KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29`); (2) updates only the
Owner decision / Owner decision date / Owner evidence / Resolution
status cells of `issue-register.csv`'s `SMR1-VC-0001` row to match,
leaving every other cell of that row, `SMR1-KL-0001`, and all other 417
issue rows unchanged; (3) adds a dedicated issue-level review block for
`SMR1-VC-0001` in `project-owner-review.md`'s Batch A section, selecting
exactly SET TO NOT VERIFIED, leaving the other 58 Batch A issues
unselected; (4) corrects `source-model-resolution-packet.md`'s and
`project-owner-review.md`'s current-state prose and sign-off summary to
state four total durably recorded decisions (3 Batch H + 1 Batch A) and
417 pending issues; (5) generalizes
`source-model-resolution-ledger.csv`'s durable-decision metric from a
Batch-H-only label to a total metric plus explicit per-batch rows
(`Total durably recorded owner decisions: 4`; `Batch H recorded
decisions: 3`; `Batch A recorded decisions: 1`), preserving the
historical fact that Batch H recorded exactly three; (6) extends
`scripts/decision_state.py` with a generic per-batch/per-record-file
breakdown check (D13) and a Batch H historical-count invariant (D14),
without rewriting the existing generic D1-D3/D6-D12/PS1-PS5 checks; (7)
extends `scripts/negative_fixtures.py` with 12 new fixtures (20 total)
covering an unbacked SMR1-VC-0001 change, a recorded-but-still-pending
row, a choice mismatch, a date mismatch, a wrong evidence reference, a
review-form mismatch, multiple review-form selections, an unauthorized
second Batch A issue, a duplicate durable record, an
implementation-authorizing record, stale packet prose, and stale
ledger counts — all on temporary copies only; and (8) adds
`batch-a-od1-dr1-validation-transcript.txt` and regenerates
`evidence-manifest.md`, `evidence-inventory.csv`, and
`checksums.sha256`.

This step does not apply the SET TO NOT VERIFIED classification to
effective normative or traceability metadata (`docs/kbdl/accessibility.md`
and `docs/kbdl/traceability-metadata.csv` remain byte-identical), does
not change lifecycle or provenance, does not resolve `SMR1-KL-0001`,
does not restore `VAL-003` or `VAL-006`, does not authorize
implementation, does not begin KBDL-011-SMR2, and does not approve or
record any other Batch A issue. Planning-agent validation of
KBDL-011-SMR1-BA-OD1-DR1 remains required.

Decision counts after BA-OD1-DR1: 4 durably recorded (3 Batch H, 1 Batch
A); 417 pending.

## Recommended next action

Planning-agent validation of KBDL-011-SMR1-BA-OD1-DR1 (the Batch A /
SMR1-VC-0001 owner-decision recording). This is the only recommended
next action; beginning KBDL-011-SMR2, another SMR1 batch, restoring any
VAL status, implementation work, or any readiness/completion approval
is explicitly out of scope for this prompt.

## Rollback

`git revert <KBDL-011-SMR1-BH-AGC1-commit-sha>` (0fadb9713299fb861830e419e06da8d82175ea1a).

`git revert <KBDL-011-SMR1-BH-AGC1-VF1-commit-sha>` reverts only the
validator/additive-evidence correction (restoring the pre-VF1 validator
design and evidence text) without reverting the BH-AGC1 authority
correction itself.

`git revert <KBDL-011-SMR1-BA-OD1-DR1-commit-sha>` reverts only the
Batch A / SMR1-VC-0001 owner-decision-recording and validator/evidence
changes (restoring `SMR1-VC-0001` to PENDING and the ledger/decision-state
checks to their pre-DR1 form) without affecting AGC1 or VF1.
