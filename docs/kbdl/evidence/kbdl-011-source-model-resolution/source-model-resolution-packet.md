# KBDL-011-SMR1 — Non-Normative R16 Source-Model Resolution Packet

Prompt ID: KBDL-011-SMR1. Original prompt context: KBDL-011-R16 / KBDL-011-R16A.

This packet was originally prepared, at commit `662ee28`, to present
project-owner decisions for review without making, recording, or
implementing any of them, and without preselecting any choice: at that
commit every one of its 421 owner-decision fields was literally `PENDING`
and every `project-owner-review.md` checkbox was unselected — **PREPARED
— NO OWNER DECISIONS RECORDED**.

As of KBDL-011-SMR1-BH-R1 (durably recorded 2026-07-29, corrected and
republished as KBDL-011-SMR1-BH-R2), the project owner has reviewed and
recorded exactly three of those 421 decisions (Batch H:
`SMR1-MOTEDGE-0001`, `SMR1-MOTEDGE-0002`, `SMR1-MOTCYCLE-0001`); the other
418 remain literally `PENDING`. The packet's current state is **OWNER
REVIEW IN PROGRESS — 3 DURABLY RECORDED BATCH H DECISIONS; 418 OTHER
ISSUES PENDING** (see §7 for the full state model). This is a
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
| `issue-register.csv` | One canonical row per distinct unresolved decision (421 rows). At commit `662ee28`, every owner-decision field was literally `PENDING`. As of KBDL-011-SMR1-BH-R1, 3 rows (Batch H) carry a durably recorded Owner decision / Owner decision date / Owner evidence, each backed by `batch-h-owner-decision-record.md`; the other 418 rows remain literally `PENDING`. |
| `source-model-resolution-ledger.csv` | The reconciliation arithmetic: raw findings, canonical issues, overlaps, cross-category dependencies, all computed from the R16 artifacts, not invented. |
| `project-owner-review.md` | The reviewable decision form, grouped by category. At commit `662ee28`, every checkbox/decision cell was unselected. As of KBDL-011-SMR1-BH-R1, the three Batch H checkboxes are selected to exactly match the durable record; every other checkbox, across all other batches, remains unselected. |
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
DECISIONS RECORDED. At the current commit: OWNER REVIEW IN PROGRESS — 3
DURABLY RECORDED BATCH H DECISIONS; 418 OTHER ISSUES PENDING.**

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
  implementation-readiness state. This is the current state, after
  KBDL-011-SMR1-BH-R1, for Batch H's three issues (418 issues remain
  `PENDING`).
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
3. **Pending planning-agent validation.** The correction above has not
   yet been validated by a planning agent. Until that validation
   occurs, the corrected graph is applied-but-unvalidated current state,
   not a confirmed final state.
4. **Remaining unresolved KBDL-011 work.** Applying this one correction
   does not resolve any of the other 418 SMR1 issues, does not restore
   any `VAL-###` status, does not change candidate/implementation-
   conformance/completion status, and does not authorize source-model
   implementation. KBDL-011 remains open.

`scripts/authority_graph.py` and `scripts/authority_graph_fixtures.py`
implement fail-closed regression checks and negative fixtures for this
correction (see `scripts/validate_packet.py`'s `AG.*` checks).

## 9. Validator-reproducibility correction (added by KBDL-011-SMR1-BH-AGC1-VF1)

This is a validator-tooling-only correction. It does not change fact 2
above (the applied Batch H correction), does not reopen fact 1
(historical cycle detection), does not resolve fact 3 (planning-agent
validation is still pending), and does not change fact 4 (KBDL-011
remains open, the other 418 issues remain PENDING).

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
underlying source-model correction was ever unsound. Planning-agent
validation of KBDL-011-SMR1-BH-AGC1 remains required.

## 8. Progression gate

This packet completes only KBDL-011-SMR1. The recommended next action is
planning-agent validation of this packet. No decision recording, metadata
correction, validation restoration, or implementation action begins here.
