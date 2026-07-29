# Prerequisite Roadmap Prompt — KBDL-011-SMR2-FSRG1 (Field-Source Registry Generator)

Prompt identifier: `KBDL-011-SMR2-FSRG1`.
Roadmap position: prerequisite to `KBDL-011-SMR2-VC-0001`.
Status: `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`.
Added: 2026-07-29 (Asia/Manila), by project-owner review disposition
**APPROVE WITH CHANGES** on the proposed `KBDL-011-SMR2-VC-0001`
metadata-recording prompt.

**This document is a roadmap prompt specification. It is not an
implementation authorization, not an owner-decision record for any
`issue-register.csv` row, and not evidence that any registry, generator,
or validation described below exists yet.** Nothing here changes the
state of any SMR1 canonical issue; `SMR1-VC-0001` remains exactly as
recorded in `batch-a-smr1-vc-0001-owner-decision-record.md`, and every
other canonical issue remains literally `PENDING`.

Implementation authorization status: NOT AUTHORIZED

## 1. Why this prerequisite exists

`implementation-unlock-map.md`, Batch A, lists `field-source-registry.csv`
among the files potentially affected by a later validation-classification
recording prompt, with the explicit qualifier **"(regenerated, not
hand-edited)"**. That qualifier cannot currently be satisfied:

- Four field-source registries exist in the repository —
  `docs/kbdl/evidence/kbdl-011-r13/artifacts/field-source-registry.csv`,
  `docs/kbdl/evidence/kbdl-011-r14/artifacts/field-source-registry.csv`,
  `docs/kbdl/evidence/kbdl-011-r15/artifacts/field-source-registry.csv`,
  and `docs/kbdl/evidence/kbdl-011-r16/artifacts/field-source-registry.csv`.
- Every one of them is a **point-in-time audit artifact** emitted by that
  round's own validator (`kbdl-011-r13/scripts/field_model_audit.py`, and
  `production_validator.py` for R14/R15/R16). Each describes the field
  source model as it stood at that round, not as it stands now.
- There is therefore **no live, current-state field-source registry** and
  **no standalone, re-runnable generator** that a later prompt could
  invoke to regenerate one.

Issuing `KBDL-011-SMR2-VC-0001` without this prerequisite would force one
of two unacceptable outcomes: hand-editing a registry (violating the
unlock map's own qualifier and creating an unreproducible artifact), or
mutating an R13–R16 round artifact (destroying immutable historical audit
evidence). `KBDL-011-SMR2-FSRG1` exists to remove that fork before any
metadata-recording prompt is issued.

## 2. Scope — what KBDL-011-SMR2-FSRG1 is authorized to prepare

FSRG1 is a **tooling-and-evidence prompt only**. When issued, it prepares:

1. **A deterministic generator.** A single standalone script
   (`scripts/field_source_registry.py` in the FSRG1 evidence package)
   that derives the field-source registry from current repository
   sources — the normative module files, `docs/kbdl/traceability-metadata.csv`,
   and the readable traceability groups — and writes it to a declared
   output path. Read-only with respect to every input.
2. **A live, current-state registry artifact.** The generator's output,
   committed as the FSRG1 package's `artifacts/field-source-registry.csv`,
   representing the field source model **as of the FSRG1 commit**, with
   the commit SHA recorded in the package's evidence records.
3. **A declared schema.** An explicit, versioned column contract for the
   live registry (column names, order, permitted value domains per
   column, and the key that makes a row unique), written down rather than
   implied by whatever the script happens to emit.
4. **A validator plus deterministic fixtures** implementing every gate in
   §4, in the established packet style: fail-closed checks, negative
   fixtures proving each check rejects the defect it targets, and
   positive-control fixtures proving the correct state still passes.
5. **A durable validation transcript** capturing the pre-commit,
   post-commit, and post-publication runs.

## 3. Preservation and non-change constraints (all mandatory)

- **R13–R16 registries are immutable historical evidence.** All four
  files named in §1 must remain **byte-identical** across FSRG1. They are
  never regenerated, re-derived, migrated, reformatted, relocated,
  deleted, superseded in place, or adopted as the generator's output
  path. The live registry is a **new, separate artifact** in the FSRG1
  package; it does not replace them and does not claim to correct them.
  Their round evidence-inventory rows and recorded SHA-256 digests remain
  unchanged and continue to verify.
- **No normative content changes.** No requirement text, lifecycle
  status, provenance, authority expression, validation classification,
  known limitation, specification location, or standard-clause citation
  changes in any module file.
- **No effective metadata changes.** `docs/kbdl/traceability-metadata.csv`
  is read only. The live registry is a **derived, non-authoritative
  description** of the current field source model; it is not itself an
  authority, a source, or validation evidence, and it does not sit
  anywhere in the source-of-truth hierarchy in
  `source-model-resolution-packet.md` §3.
- **Protected files unchanged.** `docs/kbdl/validation.md`,
  `docs/kbdl/decision-register.md`, `docs/kbdl/traceability-matrix.md`,
  and `docs/kbdl/motion/timing-easing.md` remain byte-identical.
- **No VAL-status, readiness, conformance, or completion movement.**
  `KBDL-VAL-003`–`KBDL-VAL-006` remain Not verified; candidate status
  remains NOT READY; implementation conformance remains NOT VERIFIED;
  project completion remains PENDING.
- **No decision movement.** FSRG1 records, reopens, and reinterprets no
  owner decision. The recorded/pending decision counts are identical
  before and after it.

## 4. Required validation gates (all six mandatory; each fails closed)

FSRG1 does not pass planning-agent validation unless all six are
implemented, exercised by fixtures, and shown passing in the transcript.

1. **Schema gate.** The emitted registry conforms to the declared schema:
   exact column set and order, no extra or missing columns, uniform row
   width, every cell in its column's permitted value domain, and a unique
   row key with no duplicates. A registry that drifts from the declared
   schema — in either direction — fails.
2. **Determinism gate.** Two consecutive generator runs over the same
   repository state, in different working directories and in a different
   process, produce **byte-identical** output. Row and column order are
   fully determined by an explicit sort key, never by dictionary,
   filesystem, or glob iteration order. No timestamp, hostname, absolute
   path, PID, random value, or locale-dependent formatting may appear in
   the output.
3. **Drift gate.** Re-running the generator against the committed
   repository state reproduces the committed live registry byte-for-byte;
   any divergence fails. The same gate independently verifies the four
   R13–R16 registries against their recorded SHA-256 digests, so silent
   mutation of historical evidence fails closed. A hand-edit to the live
   registry is detectable by, and fails, this gate.
4. **Path-safety gate.** The generator writes to exactly one declared
   output path inside the FSRG1 package and nowhere else. Writes outside
   that path, writes to any R13–R16 artifacts directory, writes to any
   protected file, absolute-path or `..` traversal in any output target,
   and symlink-mediated escape are each rejected. The gate must prove
   this by attempted-violation fixtures, not by inspection of the code.
5. **Fixture-isolation gate.** Every negative and positive-control
   fixture operates only on temporary copies or in-memory state, never on
   the real repository. After the full fixture run, every real repository
   file is verified byte-unchanged. A fixture that mutates real state
   fails the gate even if its own assertion passed.
6. **Clean post-publication validation gate.** The complete validation
   suite is re-run after commit and after push, from a clean working
   tree, and passes with no check passing vacuously. Any check whose
   result depends on uncommitted working-tree state, on symbolic `HEAD`,
   or on an empty diff must be reformulated against a fixed commit range
   — the defect class already recorded for
   `KBDL-011-SMR1-BH-AGC1-VF1`, which this gate exists to prevent
   recurring.

## 5. Acceptance criteria

FSRG1 is complete when, and only when: the generator, live registry,
declared schema, validator, fixtures, and transcript all exist in the
FSRG1 evidence package; all six §4 gates pass on a clean tree
post-publication; every §3 constraint is demonstrated, not merely
asserted; and the SMR1 packet validator continues to pass with no check
weakened or removed.

## 6. Gating relationship to KBDL-011-SMR2-VC-0001

- `KBDL-011-SMR2-VC-0001` — the metadata-recording prompt that would give
  the recorded `SMR1-VC-0001` = SET TO NOT VERIFIED decision effect in
  `KBDL-A11Y-001`'s validation-classification field — **remains
  `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`** and must not be issued.
- The lock is released only after FSRG1 has been prepared **and has
  passed planning-agent validation**. Preparing FSRG1, or FSRG1's own
  validators passing, is not sufficient on its own.
- On release, `KBDL-011-SMR2-VC-0001` is **reissued**, not resumed: the
  reissued prompt must invoke the FSRG1-approved generator to regenerate
  the live registry, and must not hand-edit it. The previously proposed
  form of the prompt is superseded.
- Until then, `SMR1-VC-0001`'s recorded decision continues to have **no
  effect** on normative or traceability metadata, exactly as
  `batch-a-smr1-vc-0001-owner-decision-record.md` already states.

## 7. What this prompt specification does not do

It does not authorize implementation; does not create, run, or approve
any generator; does not create a live registry; does not modify any
R13–R16 artifact; does not change normative content, effective metadata,
or any protected file; does not restore any VAL status; does not record,
reopen, or preselect any owner decision; does not begin any other SMR2
batch or roadmap item; and does not approve candidate readiness,
implementation conformance, or project completion.
