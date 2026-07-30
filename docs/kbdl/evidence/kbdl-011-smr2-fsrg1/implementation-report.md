# KBDL-011-SMR2-FSRG1 — Implementation Report

Prompt: `KBDL-011-SMR2-FSRG1` (Establish the Live Current-State Field-Source
Registry and Deterministic Generator).
Approved roadmap specification:
`docs/kbdl/evidence/kbdl-011-source-model-resolution/smr2-fsrg1-prompt.md`.
Baseline commit: `dc16473a63e446bd685640e18d64417d120b702e`
(parent `733c28e92672a4191b94045c800734c595bb014d`).

Implementation authorization status: NOT AUTHORIZED

## Root cause — why the historical registries could not serve as the live registry

Four field-source registries already existed, under `kbdl-011-r13`,
`kbdl-011-r14`, `kbdl-011-r15`, and `kbdl-011-r16`. None of them could be
maintained as *the* current-state registry, for four independent reasons:

1. **They are point-in-time audit evidence, not live state.** Each was emitted
   by that round's own validator (`field_model_audit.py` for R13,
   `production_validator.py` for R14–R16) as one output among many, describing
   the source model at that round. Regenerating one in place would destroy the
   audit record the round exists to preserve — and `KBDL-011-SMR1-RM1` already
   recorded all four as immutable historical evidence, verified by digest.
2. **They are already stale.** Against the current tree, four cells across
   `KBDL-MOT-007` and `KBDL-MOT-008` differ from the R16 artifact, because the
   `KBDL-011-SMR1-BH-AGC1` authority correction (commit `0fadb97`) changed the
   authority expressions and the MOT-007 cycle finding after R16 was published.
   A registry that cannot move with the sources is not a current-state registry.
3. **There was no standalone generator.** The registry was a side effect of a
   whole-round validator that also emits ten other artifacts and writes into its
   own round's `artifacts/` directory. Nothing could regenerate *only* the
   registry, into a maintained location, on demand.
4. **The round schemas are not a declared live contract.** R13's column set
   differs from R14–R16's; none is versioned, and none declares value domains,
   a row key, a sort key, or null spellings. `implementation-unlock-map.md`
   requires the registry be *regenerated, not hand-edited*, which requires a
   contract a validator can enforce.

A separate generator plus a separately versioned schema, writing to a new
artifact in its own package, was therefore the only option that satisfies the
unlock map without mutating historical evidence.

## What was created

A new package, `docs/kbdl/evidence/kbdl-011-smr2-fsrg1/`:

* `scripts/field_source_registry.py` — the deterministic standalone generator.
  It derives the current field source model from the normative module files,
  `traceability-metadata.csv` (candidate values only), the readable traceability
  groups in `traceability-matrix.md`, `decision-register.md`, and the AR2
  authority-recovery records; it never reads a field-source registry, including
  its own output. Standard library only. UTF-8, LF, `csv` module, explicit sort
  key, atomic write via `os.replace`, path containment on fully resolved paths,
  fail-closed on parse ambiguity and on a missing required source, no timestamp
  or environment value in the output, no network access.
* `field-source-registry-schema.md` — schema version 1: the fifteen columns in
  order, the closed seventeen-value `Field name` domain with its per-field
  ownership class and derivation rule, controlled domains, the
  `(Requirement ID, Field name)` row key, the sort key, the duplicate/conflict/
  validation-result policies, the five distinct null spellings, and the
  schema-version policy.
* `artifacts/field-source-registry.csv` — the live registry: 5,389 rows =
  317 requirements × 17 fields, 1,917,334 bytes, SHA-256
  `d94e8c43db6948638de3d61627dac6d42029db9b491834e9fc06cb6335e694d9`.
  5,055 rows `PASS`; 334 rows `FAIL`, every one of them an honest
  `UNRESOLVED` source-model report inherited from the state KBDL-011-SMR1
  catalogued — none suppressed, downgraded, or auto-repaired.
* `scripts/validate_fsrg1.py` — the FSRG1 validator, reporting each gate group
  separately with explicit `[PASS]`/`[FAIL]` lines, a final total, and a
  nonzero exit on any failure.
* `scripts/fsrg1_fixtures.py` — 24 negative fixtures and 8 positive controls.

## Correctness evidence

The generator was written independently of `production_validator.py` and then
compared against the R16 artifact row by row. It reproduces **all 5,389 rows
exactly**, except four cells across `KBDL-MOT-007` and `KBDL-MOT-008`:

| Row | Cell | R16 | Live |
| --- | --- | --- | --- |
| MOT-007 / Authority | Ledger value | `... together with KBDL-MOT-008, as one timing system` | `Approved (per KBDL-DEC-014, decision packet item 2)` |
| MOT-007 / Authority | Expected, Effective | `UNRESOLVED` | `RESOLVED` |
| MOT-007 / Authority | Governance resolution, Validation result | `FAIL` | `PASS` |
| MOT-008 / Authority | Ledger value | `... together with KBDL-MOT-007, as one timing system` | `Approved (per KBDL-DEC-014, decision packet item 2)` |
| MOT-007, MOT-008 / Notes or exclusions | Ledger, Expected, Effective | (no related-requirement sentence) | related-requirement sentence present |

Those are exactly the cells changed by `KBDL-011-SMR1-BH-AGC1`, and MOT-007's
authority now resolving is exactly that correction removing the two-node
authority cycle. Agreement with an independent implementation everywhere else,
with divergence confined to a known, separately validated current-state change,
is the primary correctness evidence for this package.

## Gates implemented

| Gate | Enforcement |
| --- | --- |
| Schema | Header, order, widths, controlled domains, row key uniqueness, field/ownership/rule agreement, declared sort order, effective-equals-expected, precedence-matches-conflict, validation-result policy, UTF-8/no-BOM/LF/final newline, non-empty, no absolute path or environment value. A CSV parse error fails; it is never a warning. |
| Determinism | Two generator runs, in two separate repository copies, in two separate processes, from two different working directories; compared by bytes, SHA-256, header, row count, final newline, and line endings. |
| Drift | The generator's `--check` mode run as a separate process, **plus** an independent in-process regeneration compared to the committed bytes — so the gate cannot pass on a comparison that never ran. |
| Historical | Each R13–R16 registry compared to the digest recorded in *its own* round evidence inventory. The expected digest is read from the committed inventory, never recomputed from the file being checked. |
| Path safety | Attempted-violation checks, not code inspection: symlinked target refused, package-escape refused, missing-package refused, exactly one created path per run, `--check` writes nothing, historical artifacts untouched. |
| Fixture isolation | The whole fixture suite runs, then every real file is re-hashed and `git status --short` re-compared; a temporary-tree cleanup failure fails the suite. |
| Coverage | Every current requirement present, no unknown requirement, all 17 fields per requirement, row count equals requirements × fields. |
| Labelling | The required non-authoritative sentence present verbatim; no authority/evidence/authorization claim anywhere in the package. |
| Protection | `git diff` against the baseline commit for every protected and normative path and for all four historical packages. |
| Decision state | The SMR1 packet's own `decision_state.compute()` must report 4 recorded / 417 pending with no unknown or duplicate record. |
| VAL / readiness | The exact declarations in `validation.md` for candidate readiness, conformance, completion, VAL-003–006, and VAL-007. |
| Package | Required files present, `checksums.sha256` verifies, inventory complete and digest-matching. |

## What this step did not do

No normative requirement, effective metadata value, lifecycle, provenance,
authority, validation classification, method, evidence, limitation, or
specification location changed. `SMR1-VC-0001` was not applied to effective
metadata; `KBDL-A11Y-001` and `traceability-metadata.csv` are byte-identical to
the baseline. No VAL status was restored; candidate readiness, implementation
conformance, and completion are unchanged. No owner-decision state moved: 4
durably recorded (3 Batch H, 1 Batch A), 417 pending, unchanged. No R13–R16
artifact, inventory, checksum, validator, transcript, or report changed. No
dependency was added; no application code, API, database, migration, UI, or
deployment configuration exists in this package.

`KBDL-011-SMR2-VC-0001` was not begun, resumed, or reissued. It remains
`LOCKED — PLANNING-AGENT VALIDATION REQUIRED`, and must be **reissued, not
resumed**, only after `KBDL-011-SMR2-FSRG1` passes planning-agent validation.

## Publication

Two linear commits, both fast-forward pushes, neither amended:

| Commit | SHA | Contents |
| --- | --- | --- |
| A — implementation | `ad729c8cee17cac70f6e867d0afdca8901098b71` (parent `dc16473a`) | Generator, live registry, schema, validator, fixtures, package documentation, stage-1 transcript, SMR1 packet integration, evidence records. |
| B — evidence closure | this commit (parent `ad729c8c`) | Actual post-publication Commit A outputs appended to the transcript, the finalized transcript, regenerated FSRG1 and SMR1 inventories and checksums, and this status text. |

Commit B changes no generator behavior, no registry content, no schema, no
fixture, no normative content, no effective metadata, and no historical
evidence.

The transcript records a self-reference limitation honestly: a transcript
cannot verify its own final bytes, so the `PKG.checksums_verify` and
`PKG.inventory_digests_match` checks fail *inside* the transcript, naming the
transcript file and nothing else. The evidence records are regenerated against
the transcript's final bytes in Commit B, and the authoritative clean runs are
executed afterwards against the published tree.

## Rollback

Reverse order, no reset/amend/rebase/squash/force-push:

```bash
git revert <Commit-B-SHA>
git revert ad729c8cee17cac70f6e867d0afdca8901098b71
```

That removes this package, its SMR1 packet integration, and its administrative
evidence records. It does not alter the historical registries, any recorded
owner decision, AGC1, VF1, DR1, DR1-R1, or RM1.

## Status

FSRG1 implementation is complete and **awaiting planning-agent validation**.
It is not validated, not approved, and authorizes nothing.
`KBDL-011-SMR2-FSRG1` remains `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`, as
does `KBDL-011-SMR2-VC-0001`, which must be **reissued, not resumed**, and only
after FSRG1 passes planning-agent validation.
