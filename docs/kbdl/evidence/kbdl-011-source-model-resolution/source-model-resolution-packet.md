# KBDL-011-SMR1 — Non-Normative R16 Source-Model Resolution Packet

Prompt ID: KBDL-011-SMR1. Original prompt context: KBDL-011-R16 / KBDL-011-R16A.

This packet was originally prepared, at commit `662ee28`, to present
project-owner decisions for review without making, recording, or
implementing any of them, and without preselecting any choice: at that
commit every one of its 421 owner-decision fields was literally `PENDING`
and every `project-owner-review.md` checkbox was unselected — **PREPARED
— NO OWNER DECISIONS RECORDED**.

As of KBDL-011-SMR1-BH-R1 (durably recorded 2026-07-29, corrected and
republished as KBDL-011-SMR1-BH-R2), the project owner reviewed and
recorded exactly three of those 421 decisions (Batch H:
`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001`). As of
KBDL-011-SMR1-BA-OD1-DR1 (durably recorded 2026-07-29), the project
owner additionally recorded one Batch A decision (`SMR1-VC-0001` =
SET TO NOT VERIFIED). Four of the 421 decisions are now durably
recorded in total (3 Batch H + 1 Batch A); the other 417 remain
literally `PENDING`. The packet's current state is **OWNER REVIEW IN
PROGRESS — 4 DURABLY RECORDED DECISIONS (3 BATCH H, 1 BATCH A); 417
OTHER ISSUES PENDING** (see §7 for the full state model). This is a
packet-review state only. Neither the original prepared state nor the
current owner-review state makes, implements, or self-executes any
decision; neither changes any protected project field; and the project
remains exactly as blocked, for implementation purposes, as it was before
this packet existed.

## 1. Why this packet exists

KBDL-011-R16A produced a durable, source-independent audit of every KBDL
requirement's field provenance. That audit concluded BLOCKED and remains
committed on `main` at `873577a536e74c906cc14321423057b255216a99` and later.
Its findings (all reproduced from `docs/kbdl/evidence/kbdl-011-r16/artifacts/`,
not re-derived or altered here):

- Requirements audited: 317; Effective records: 317; Failed effective
  records: 289.
- Unresolved field sources: 335 (`unresolved-field-sources.csv`).
- Known-limitation source defects: 229; Validation-classification source
  defects: 59; Authority-source defects: 21; Validation-evidence source
  defects: 14; Validation-method source defects: 12.
- Exact-location mismatches: 63; Evidence-scope mapping defects: 11;
  Limitation-scope mismatches: 229; Standard-clause mismatches: 20.
- Circular authority chains: 1 (`KBDL-MOT-007 → KBDL-MOT-008 → KBDL-MOT-007`).

The project owner authorized preparation — not resolution — of a packet
that turns these findings into independently reviewable decisions. The
intended downstream outcome (enabling later, individually approved and
validated implementation actions) is explicitly **not** current
implementation authorization.

## 2. What this packet contains

| File | Purpose |
| --- | --- |
| `issue-register.csv` | One canonical row per distinct unresolved decision (421 rows). At commit `662ee28`, every owner-decision field was literally `PENDING`. As of KBDL-011-SMR1-BH-R1, 3 rows (Batch H) carry a durably recorded Owner decision / Owner decision date / Owner evidence, each backed by `batch-h-owner-decision-record.md`. As of KBDL-011-SMR1-BA-OD1-DR1, one more row (`SMR1-VC-0001`, Batch A) carries a durably recorded Owner decision / Owner decision date / Owner evidence, backed by `batch-a-smr1-vc-0001-owner-decision-record.md`; the other 417 rows remain literally `PENDING`. |
| `source-model-resolution-ledger.csv` | The reconciliation arithmetic: raw findings, canonical issues, overlaps, cross-category dependencies, all computed from the R16 artifacts, not invented. |
| `project-owner-review.md` | The reviewable decision form, grouped by category. At commit `662ee28`, every checkbox/decision cell was unselected. As of KBDL-011-SMR1-BH-R1, the three Batch H checkboxes are selected to exactly match the durable record. As of KBDL-011-SMR1-BA-OD1-DR1, one Batch A checkbox (`SMR1-VC-0001` only) is selected to exactly match its durable record; every other checkbox, across all other batches and the other 58 Batch A issues, remains unselected. |
| `impact-assessment.md` | Change-impact analysis per decision group (requirements, modules, validation, traceability, documentation, regression risk, rollback complexity). |
| `implementation-unlock-map.md` | What each decision could unlock later — never phrased as current authorization. |
| `evidence-manifest.md`, `evidence-inventory.csv`, `checksums.sha256` | Evidence integrity records for this packet, mirroring the R16A conventions. |
| `implementation-report.md` | The required summary block with computed reconciliation numbers. |
| `precommit-transcript.txt`, `initial-repository-state.txt` | Exact commands, outputs, and interpretations for repository-safety validation. |
| `batch-h-r2-validation-transcript.txt` | (Added by KBDL-011-SMR1-BH-R2.) Durable command/output transcript for the BH-R2 packet-state correction and republication, including current positive/negative validation runs and post-push SHA equality. |
| `scripts/reconciliation_compute.py` | Reproduces the raw-findings/category computation directly from the R16 CSVs. |
| `scripts/generate_issue_register.py` | Reproduces `issue-register.csv` directly from the R16 CSVs (no hand-entered rows). |
| `scripts/validate_packet.py` | Programmatic check of the 24 required validation points, plus (as of KBDL-011-SMR1-BH-R1) state-aware owner-decision checks. |
| `scripts/decision_state.py` | (Added by KBDL-011-SMR1-BH-R1; extended by KBDL-011-SMR1-BH-R2.) Loads durable `*-owner-decision-record.md` files, cross-checks them against `issue-register.csv` and `project-owner-review.md`, and (as of BH-R2) verifies the packet's own state-description prose and review-cycle summary are not stale or contradictory. |
| `scripts/negative_fixtures.py` | (Added by KBDL-011-SMR1-BH-R1; extended by KBDL-011-SMR1-BH-R2.) Deterministic negative-validation fixtures proving `decision_state.py` fails closed on unbacked/mismatched/duplicate/unknown/implementation-authorizing decisions and stale packet-state prose; operates on temporary copies only. |
| `batch-h-owner-decision-record.md` | (Added by KBDL-011-SMR1-BH-R1.) Durable current-owner evidence for the three Batch H decisions. |
| `batch-a-smr1-vc-0001-owner-decision-record.md` | (Added by KBDL-011-SMR1-BA-OD1-DR1.) Durable current-owner evidence for the one Batch A decision (`SMR1-VC-0001` = SET TO NOT VERIFIED). |
| `batch-a-od1-dr1-validation-transcript.txt` | (Added by KBDL-011-SMR1-BA-OD1-DR1.) Durable command/output transcript for this recording step. |
| `smr2-fsrg1-prompt.md` | (Added by KBDL-011-SMR1-RM1.) Specification of the prerequisite roadmap prompt `KBDL-011-SMR2-FSRG1` (live field-source registry artifact and deterministic generator), including its preservation constraints and six mandatory validation gates. A roadmap record only — it authorizes nothing. |
| `scripts/fsrg1_roadmap.py` | (Added by KBDL-011-SMR1-RM1.) Fail-closed checks (FR1–FR6) that the FSRG1 roadmap record stays intact: the specification exists and disclaims authorization, states all six gates, names and protects the four R13–R16 registries (verified against their recorded SHA-256 digests), and keeps both `KBDL-011-SMR2-FSRG1` and `KBDL-011-SMR2-VC-0001` at a LOCKED status with the planning-agent gate stated. |
| `smr2-fsrg1-roadmap-validation-transcript.txt` | (Added by KBDL-011-SMR1-RM1.) Durable command/output transcript for the roadmap addition: positive validator run, FR1–FR6 fixtures, the pre-existing fixture suites, R13–R16 registry immutability verification, and the protected-file/working-tree scope audit. |
| `scripts/fsrg1_roadmap_fixtures.py` | (Added by KBDL-011-SMR1-RM1.) Twelve deterministic fixtures (ten rejection, two positive-control) proving FR1–FR6 fail closed; operates on temporary copies and a synthetic temporary repository root only. |

## 3. Source-of-truth hierarchy applied

This packet applies the same hierarchy R16 used, unchanged:

1. Current project-owner packet-preparation authorization.
2. The validated R16A durable audit.
3. Current normative requirement records.
4. Approved decisions.
5. AR2 current-authority confirmations.
6. Exact historical governance evidence.
7. Approved blueprint and roadmap.
8. Current traceability records as candidate values only.
9. Readable traceability groups as candidate values only.
10. Git history.

Consequences applied throughout every issue record: the ledger cannot
prove itself; readable groups cannot create authority; existing status
cannot serve as authority for that same status; historical implementation
commits cannot prove owner approval; missing sources remain missing;
recommendations are never presented as approved decisions; all
current-authority language is explicitly non-retroactive unless original
evidence is supplied.

## 4. Category population (computed, not asserted)

See `source-model-resolution-ledger.csv` for full computation detail and
`scripts/reconciliation_compute.py` to reproduce it. Summary:

- Raw R16 findings (`defects.csv` rows): **693**.
- Canonical resolution issues: **421** (418 field/location/standard-clause
  issues + 2 MOT authority-edge issues + 1 MOT authority-cycle issue).
- Distinct affected requirements: **289** (exactly the R16-reported Failed
  effective records count).
- Cross-category dependency count (requirements touched by more than one
  category): **91**.
- Overlap count (raw findings that duplicate an already-counted canonical
  issue rather than creating a new one): **274**.
- Unmapped findings: **0**. Duplicate canonical issues: **0**.

Per-category canonical issue counts: Validation classification 59,
Authority 21, Validation evidence 14, Validation method 12, Known
limitation 229, Exact location 63, Standard clause 20, MOT authority edge
2, MOT authority cycle 1.

## 5. What this packet does not do

It does not resolve any issue, preselect any decision, apply bulk
approval, add authority, change lifecycle or provenance, restore any VAL
status, execute VAL-004 methods, accept limitations, approve readiness,
claim implementation conformance, approve completion, or begin any
implementation package. `docs/kbdl/validation.md` and every other
protected file remain byte-identical to the pre-packet `HEAD`.

## 6. Current status (unchanged, referenced only)

```
KBDL-VAL-003: Not verified
KBDL-VAL-004: Not verified
KBDL-VAL-005: Not verified
KBDL-VAL-006: Not verified
KBDL-VAL-007: Verified — documentation method only
Candidate: NOT READY — SOURCE-INDEPENDENCE AND CLAUSE-EVIDENCE REMEDIATION REQUIRED
Implementation conformance: NOT VERIFIED
Project completion: PENDING
```

## 7. Packet review-state model (added by KBDL-011-SMR1-BH-R1; kept
consistent by KBDL-011-SMR1-BH-R2)

Stated without contradiction: **at commit `662ee28`: PREPARED — NO OWNER
DECISIONS RECORDED. At the current commit: OWNER REVIEW IN PROGRESS — 4
DURABLY RECORDED DECISIONS (3 BATCH H, 1 BATCH A); 417 OTHER ISSUES
PENDING.**

This packet's `scripts/validate_packet.py` / `scripts/decision_state.py`
recognize exactly three packet states:

- **PREPARED — NO OWNER DECISIONS RECORDED.** Every Owner decision /
  Owner decision date / Owner evidence cell in `issue-register.csv` is
  literally `PENDING`; no `project-owner-review.md` checkbox is selected.
  This was the state of commit `662ee28`.
- **OWNER REVIEW IN PROGRESS — DURABLY RECORDED DECISIONS PRESENT.** One
  or more issues have a non-`PENDING` decision, and every such issue is
  backed by an exactly matching durable owner-decision record (a
  `*-owner-decision-record.md` file); every other issue remains
  `PENDING`; every selected review-form checkbox exactly matches its
  durable record. This is a packet-review state only, **not** an
  implementation-readiness state. This is the current state: 3 issues
  from KBDL-011-SMR1-BH-R1 (Batch H) plus 1 issue from
  KBDL-011-SMR1-BA-OD1-DR1 (Batch A, `SMR1-VC-0001`) — 4 issues total
  (417 issues remain `PENDING`).
- **INVALID — SELECTED DECISIONS LACK DURABLE OR CONSISTENT OWNER
  EVIDENCE.** Validation fails when: a selected issue has no durable
  owner-decision record; a durable record references an unknown issue;
  a selected option differs from its durable record; a review-form
  selection differs from the issue register; duplicate or conflicting
  decisions exist; a decision record authorizes implementation,
  readiness, limitations, conformance, or completion; or integrity
  artifacts (checksums, ledger counts) are stale or inconsistent.

No state above is, or implies, implementation readiness, VAL-status
restoration, candidate readiness, implementation conformance, or project
completion.

## 8. Batch H authority-graph correction (added by KBDL-011-SMR1-BH-AGC1)

Four distinct facts must not be conflated:

1. **Historical cycle detection.** R16 originally detected a two-node
   authority cycle `KBDL-MOT-007 → KBDL-MOT-008 → KBDL-MOT-007` (see
   `docs/kbdl/evidence/kbdl-011-r16/artifacts/authority-cycle-audit.csv`).
   That historical finding is preserved unchanged and is not rewritten
   to pretend the defect was never found.
2. **Applied Batch H correction.** As of this commit, the current
   authoritative source model (`docs/kbdl/motion/README.md` and
   `docs/kbdl/traceability-metadata.csv`) has been corrected so that
   `KBDL-MOT-007` and `KBDL-MOT-008` each independently cite
   `KBDL-DEC-014`, decision packet item 2, as authority, and their
   mutual relationship is represented only as `RELATED REQUIREMENT` in
   both directions. Neither directional authority edge exists any
   longer; there is no live two-node authority cycle. This applies the
   three Batch H decisions already durably recorded in
   `batch-h-owner-decision-record.md` — it does not reopen, reinterpret,
   or broaden them, and it fabricates no new project-owner decision
   (`KBDL-DEC-014` itself is unchanged in scope and meaning).
3. **Planning-agent validation status.** At the historical KBDL-011-SMR1-BH-AGC1
   point, this correction had not yet been validated by a planning agent
   and was applied-but-unvalidated current state. As of the current
   KBDL-011-SMR1-BA-OD1-DR1-R1 point, **KBDL-011-SMR1-BH-AGC1 has passed
   planning-agent validation**; that specific gate is closed. As of
   KBDL-011-SMR1-RM1, `KBDL-011-SMR1-BA-OD1-DR1-R1` has also passed
   planning-agent validation, so it is no longer an open gate either;
   the current open gate is KBDL-011-SMR1-RM1 itself. See §11.
4. **Remaining unresolved KBDL-011 work.** At the historical
   KBDL-011-SMR1-BH-AGC1 point (3 durably recorded, 418 other SMR1
   issues pending), applying this one correction did not resolve any of
   the other pending SMR1 issues. As of the current
   KBDL-011-SMR1-BA-OD1-DR1-R1 point, four decisions are durably
   recorded in total (3 Batch H + 1 Batch A) and 417 issues remain
   PENDING. This correction does not restore any `VAL-###` status, does
   not change candidate/implementation-conformance/completion status,
   and does not authorize source-model implementation. KBDL-011 remains
   open.

`scripts/authority_graph.py` and `scripts/authority_graph_fixtures.py`
implement fail-closed regression checks and negative fixtures for this
correction (see `scripts/validate_packet.py`'s `AG.*` checks).

## 9. Validator-reproducibility correction (added by KBDL-011-SMR1-BH-AGC1-VF1)

This is a validator-tooling-only correction. It does not change fact 2
above (the applied Batch H correction) and does not reopen fact 1
(historical cycle detection). At the historical KBDL-011-SMR1-BH-AGC1-VF1
point, fact 3 (planning-agent validation) was still pending and fact 4
(KBDL-011 remains open, the other 418 issues pending) was unchanged; as
of the current KBDL-011-SMR1-BA-OD1-DR1-R1 point, KBDL-011-SMR1-BH-AGC1
and KBDL-011-SMR1-BH-AGC1-VF1 have both since passed planning-agent
validation, four decisions are durably recorded in total (3 Batch H + 1
Batch A), 417 issues remain PENDING, and KBDL-011 remains incomplete.

A clean post-publication run of `scripts/validate_packet.py` against
the published Batch H correction commit (`0fadb9713299fb861830e419e06da8d82175ea1a`,
parent `46104c57f86a924b197f6ed380a5b1127eddbf7d`) reproducibly exited 1
at 69/70: the three `AG.narrow_authorized_diff.*` checks compared the
working tree against symbolic `HEAD`, which is empty once that commit
is published and the tree is clean, so the row-count check failed
(`added=0 removed=0`) and the other two checks passed only vacuously on
that same empty diff. `scripts/agc1_narrow_diff.py` replaces this
design: all three checks now evaluate the fixed, immutable range
`46104c57f86a924b197f6ed380a5b1127eddbf7d
..0fadb9713299fb861830e419e06da8d82175ea1a` directly, independent of
current `HEAD`, and fail closed (never vacuously pass) on a missing
commit, a wrong-parent target, a failed `git` invocation, or an empty
diff. `scripts/agc1_narrow_diff_fixtures.py` proves this in ten
required scenarios plus the mandatory HEAD-independence case, entirely
in temporary, disposable Git repositories.

The originally reported "70/70" claim for the Batch H correction commit
was therefore not reproducible from a clean post-publication checkout;
this correction supersedes that specific validator claim without
amending or rewriting the original commit, and without implying the
underlying source-model correction was ever unsound. **As of the
current KBDL-011-SMR1-BA-OD1-DR1-R1 point, planning-agent validation of
KBDL-011-SMR1-BH-AGC1 has passed; it is no longer an open gate.**

## 10. Batch A / SMR1-VC-0001 decision recording (added by KBDL-011-SMR1-BA-OD1-DR1)

`KBDL-011-SMR1-BA-OD1-DR1` durably records exactly one Batch A decision
— `SMR1-VC-0001` (`KBDL-A11Y-001` validation classification) = SET TO
NOT VERIFIED — using the same generic durable-record architecture
`decision_state.py` already used for the three Batch H decisions; no
parallel Batch-A-specific engine was introduced. It: (1) adds
`batch-a-smr1-vc-0001-owner-decision-record.md`, a durable owner-decision
record for `SMR1-VC-0001` alone (record
`KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29`); (2) updates
`issue-register.csv`'s `SMR1-VC-0001` row's Owner decision / Owner
decision date / Owner evidence / Resolution status cells to exactly
match that record, leaving every other cell of that row, and every other
issue row (including `SMR1-KL-0001`), unchanged; (3) adds a dedicated
issue-level review block for `SMR1-VC-0001` in
`project-owner-review.md`'s Batch A section, selecting exactly SET TO
NOT VERIFIED, leaving the other 58 Batch A issues unselected; (4) updates
this packet's and `project-owner-review.md`'s current-state prose and
sign-off summary to state four total durably recorded decisions (3 Batch
H + 1 Batch A) and 417 pending issues; (5) generalizes
`source-model-resolution-ledger.csv`'s durable-decision metric from a
Batch-H-only label to a total metric (`Total durably recorded owner
decisions: 4`) plus explicit per-batch rows (`Batch H recorded
decisions: 3`; `Batch A recorded decisions: 1`; preserving the historical
fact that Batch H recorded exactly three), and extends
`scripts/decision_state.py` with a generic per-batch/per-record-file
breakdown check (D13) plus an explicit Batch H historical-count
invariant (D14), without rewriting the existing generic counting logic
(D6/D7 and the total durable-record count remain exactly as before,
now simply summing to 4 instead of 3); (6) extends
`scripts/negative_fixtures.py` with twelve new fixtures covering an
unbacked `SMR1-VC-0001` change, a recorded-but-still-pending row, a
choice mismatch, a date mismatch, a wrong evidence reference, a
review-form mismatch, multiple review-form selections, an unauthorized
second Batch A issue, a duplicate durable record, an
implementation-authorizing record, stale packet prose still claiming
three recorded/418 pending, and a stale ledger total/per-batch count —
all rejected for the intended reason, on temporary copies only; and (7)
adds `batch-a-od1-dr1-validation-transcript.txt` and regenerates
`evidence-manifest.md`, `evidence-inventory.csv`, and
`checksums.sha256`.

This step does not apply the SET TO NOT VERIFIED classification to any
effective normative or traceability metadata (`docs/kbdl/accessibility.md`
and `docs/kbdl/traceability-metadata.csv` remain byte-identical), does
not change lifecycle or provenance, does not resolve `SMR1-KL-0001`,
does not restore `VAL-003` or `VAL-006`, does not authorize
implementation, does not begin KBDL-011-SMR2, and does not approve or
record any other Batch A issue. A later, separate metadata-recording
prompt and planning-agent validation are required before this decision
has any normative effect. Planning-agent review of
KBDL-011-SMR1-BA-OD1-DR1 identified an internal authority contradiction
in the durable record and stale current-state prose (see §11);
`KBDL-011-SMR1-BA-OD1-DR1-R1` corrects those defects additively, without
reopening or reinterpreting the underlying `SET TO NOT VERIFIED`
decision itself.

## 11. Current planning-agent validation status (as of KBDL-011-SMR1-RM1)

This section states the current planning-agent-validation gate status
without rewriting any prior commit or historical transcript:

- `KBDL-011-SMR1-BH-R1` / `KBDL-011-SMR1-BH-R2`: passed planning-agent
  validation.
- `KBDL-011-SMR1-BH-AGC1`: **passed planning-agent validation.**
- `KBDL-011-SMR1-BH-AGC1-VF1`: **passed planning-agent validation.**
- `KBDL-011-SMR1-BA-OD1-DR1`: planning-agent review found two defects —
  (1) the durable record's authority wording contradicted the approved
  current-authority meaning; (2) stale current-state prose (418
  pending / AGC1 pending) survived in several sections. DR1's decision
  recording itself (`SMR1-VC-0001` = SET TO NOT VERIFIED, 2026-07-29)
  is not reopened, reinterpreted, or changed by this correction.
- `KBDL-011-SMR1-BA-OD1-DR1-R1`: **PASSED — PLANNING-AGENT VALIDATED**
  (recorded by KBDL-011-SMR1-RM1, on the project owner's 2026-07-29
  disposition). It is **not** an open gate. Its authority-wording and
  stale-prose corrections, and the `AR1`/`AR2`/`SP1`–`SP4` checks it
  added, stand as validated; `KBDL-011-SMR1-BA-OD1-DR1`'s superseded
  validation claims remain superseded.
- `KBDL-011-SMR1-RM1` (the `KBDL-011-SMR2-FSRG1` roadmap addition, §12):
  **planning-agent validation of this step is the current open gate.**

`KBDL-011` remains incomplete. Closing these gates does not approve
candidate readiness, implementation conformance, or project completion,
and does not unlock `KBDL-011-SMR2-FSRG1` or `KBDL-011-SMR2-VC-0001`,
both of which remain `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`.

Current decision-state counts (unchanged by this step): 4 decisions
durably recorded in total (3 Batch H, 1 Batch A); 417 issues remain
PENDING.

## 12. Prerequisite roadmap prompt KBDL-011-SMR2-FSRG1 (added by KBDL-011-SMR1-RM1)

On 2026-07-29 the project owner returned the disposition **APPROVE WITH
CHANGES** on the proposed `KBDL-011-SMR2-VC-0001` metadata-recording
prompt: a prerequisite roadmap prompt, `KBDL-011-SMR2-FSRG1`, is to be
added first, establishing a live, current-state field-source-registry
artifact and a deterministic generator; and `KBDL-011-SMR2-VC-0001` is to
stay locked until `KBDL-011-SMR2-FSRG1` passes planning-agent validation,
after which the metadata-recording prompt is reissued against the
approved generator.

`KBDL-011-SMR1-RM1` records that disposition in the roadmap. It: (1) adds
`smr2-fsrg1-prompt.md`, the FSRG1 prompt specification — its rationale,
scope, preservation constraints, the six mandatory validation gates
(schema, determinism, drift, path-safety, fixture-isolation, and clean
post-publication validation), its acceptance criteria, and its gating
relationship to `KBDL-011-SMR2-VC-0001`; (2) adds two entries to
`implementation-unlock-map.md` — the prerequisite `KBDL-011-SMR2-FSRG1`
and the downstream `KBDL-011-SMR2-VC-0001` — both at
`LOCKED — PLANNING-AGENT VALIDATION REQUIRED`, and updates Batch A's
later-prompt and precondition lines to name the gate; (3) adds
`scripts/fsrg1_roadmap.py`, six fail-closed checks (FR1–FR6) that the
roadmap record cannot silently weaken; (4) adds
`scripts/fsrg1_roadmap_fixtures.py`, twelve deterministic fixtures (ten
rejection, two positive-control) proving those checks fail closed, run
against temporary copies and a synthetic temporary repository root only,
with the real repository verified byte-unchanged afterward; (5) adds
`smr2-fsrg1-roadmap-validation-transcript.txt`; (6) records
`KBDL-011-SMR1-BA-OD1-DR1-R1` as PASSED — PLANNING-AGENT VALIDATED (§11),
closing that gate; and (7) regenerates `evidence-inventory.csv` and
`checksums.sha256`, which also closes a pre-existing omission:
`batch-a-od1-dr1-validation-transcript.txt` is a pre-existing durable
transcript, published by `KBDL-011-SMR1-BA-OD1-DR1`, that was never
listed in `evidence-inventory.csv`. **Only the inventory record is
corrected; the transcript file itself remains byte-identical** to the
published copy and is not rewritten, re-run, or re-dated here.

The rationale the disposition responds to is that Batch A requires
`field-source-registry.csv` to be *regenerated, not hand-edited*, while
the only four registries in the repository —
`kbdl-011-r13`/`r14`/`r15`/`r16` `artifacts/field-source-registry.csv` —
are point-in-time round audit artifacts emitted by those rounds' own
validators. There is no live registry and no standalone generator, so a
recording prompt issued today could only hand-edit a registry or mutate
historical round evidence. All four remain **immutable historical
evidence**: `KBDL-011-SMR1-RM1` leaves them byte-identical, and FR4
verifies them against the SHA-256 digests recorded in their own round
evidence inventories on every validator run.

This step is a roadmap and tooling record only. It does not prepare,
authorize, run, or approve the FSRG1 generator; does not create a live
registry; does not issue `KBDL-011-SMR2-VC-0001`; does not begin
KBDL-011-SMR2 or any other roadmap item; changes no normative content, no
effective metadata, and no protected file; restores no VAL status; and
records, reopens, or preselects no owner decision. The decision-state
counts are unchanged: 4 durably recorded (3 Batch H, 1 Batch A); 417
PENDING. `KBDL-011-SMR1-BA-OD1-DR1-R1` has passed planning-agent
validation and is not an open gate (§11); planning-agent validation of
`KBDL-011-SMR1-RM1` itself is now the open gate.

## 8. Progression gate

This packet completes only KBDL-011-SMR1. The recommended next action is
planning-agent validation of this packet. No decision recording, metadata
correction, validation restoration, or implementation action begins here.
