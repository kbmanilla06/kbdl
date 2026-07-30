# KBDL-011-SMR2-FSRG1 — Live Field-Source Registry and Deterministic Generator

This package implements the prerequisite prompt `KBDL-011-SMR2-FSRG1`, whose
approved roadmap specification is
`docs/kbdl/evidence/kbdl-011-source-model-resolution/smr2-fsrg1-prompt.md`
(recorded by `KBDL-011-SMR1-RM1`, commit `dc16473a`).

The live field-source registry is a derived, non-authoritative description of the current source model. It is not itself authority, a normative source, validation evidence, an owner-decision record, or implementation authorization.

Implementation authorization status: NOT AUTHORIZED

## Why this package exists

`implementation-unlock-map.md`'s Batch A entry requires
`field-source-registry.csv` to be **regenerated, not hand-edited**. Before this
package, the repository contained only four field-source registries —
`kbdl-011-r13`, `kbdl-011-r14`, `kbdl-011-r15`, and `kbdl-011-r16`, each under
`artifacts/` — and every one of them is a *point-in-time round audit artifact*
emitted by that round's own validator, describing the source model as it stood
at that round. There was no live registry and no standalone generator, so any
metadata-recording prompt could only have hand-edited a registry or mutated
historical evidence. This package removes that fork.

All four historical registries remain **immutable historical evidence**. They
are never regenerated, relocated, reformatted, or used as this generator's
output path, and `validate_fsrg1.py`'s `HIST` gate verifies each one against the
SHA-256 digest recorded in its *own* round evidence inventory on every run.

## Contents

| Path | Purpose |
| --- | --- |
| `field-source-registry-schema.md` | The declared schema contract, version 1: columns, domains, row key, sort key, null spellings, and the schema-version policy. |
| `artifacts/field-source-registry.csv` | The live registry for the current repository state. Generated only by the generator below; never hand-edited. |
| `scripts/field_source_registry.py` | The deterministic standalone generator (`--repo-root`, `--check`). |
| `scripts/validate_fsrg1.py` | The FSRG1 validator: schema, determinism, drift, historical integrity, path safety, isolation, coverage, labelling, protection, decision state, VAL/readiness, package integrity. |
| `scripts/fsrg1_fixtures.py` | 24 negative fixtures and 8 positive controls proving every gate fails closed. |
| `fsrg1-validation-transcript.txt` | Durable command/output evidence. |
| `implementation-report.md` | What this step changed, and what it deliberately did not. |
| `evidence-manifest.md`, `evidence-inventory.csv`, `checksums.sha256` | Package evidence-integrity records. |

No file outside this package is created by the generator.

## Usage

Generate the live registry:

```bash
python3 docs/kbdl/evidence/kbdl-011-smr2-fsrg1/scripts/field_source_registry.py \
  --repo-root .
```

Verify the committed artifact reproduces byte-for-byte, writing nothing:

```bash
python3 docs/kbdl/evidence/kbdl-011-smr2-fsrg1/scripts/field_source_registry.py \
  --repo-root . --check
```

Validate the package, and run the fixtures:

```bash
python3 docs/kbdl/evidence/kbdl-011-smr2-fsrg1/scripts/validate_fsrg1.py --repo-root .
python3 docs/kbdl/evidence/kbdl-011-smr2-fsrg1/scripts/fsrg1_fixtures.py --repo-root .
```

The generator writes exactly one path,
`docs/kbdl/evidence/kbdl-011-smr2-fsrg1/artifacts/field-source-registry.csv`,
and refuses absolute paths, `..` traversal, symlink escape, historical-artifact
targets, protected-file targets, and any target outside this package. `--check`
and the validator never write to the repository.

## Sources

Read-only inputs: the normative module files under `docs/kbdl/`,
`docs/kbdl/traceability-metadata.csv` (candidate values only),
`docs/kbdl/traceability-matrix.md` (readable traceability groups),
`docs/kbdl/decision-register.md`, the AR2 authority-recovery records, and git
object existence for evidence values citing a commit SHA. The historical R13–R16
registries are never read as authoritative input for current values, and the
live registry is never an input to its own generation.

## Correctness reference

Run against the current tree, the generator reproduces all 5,389 rows of the
R16 registry except four cells across `KBDL-MOT-007` and `KBDL-MOT-008` — which
are exactly the cells the `KBDL-011-SMR1-BH-AGC1` authority-graph correction
(commit `0fadb97`) changed. That agreement with an independently written round
validator, and the isolated divergence being precisely the known current-state
change, is the package's primary correctness evidence.

## Boundaries

This package does not change any normative requirement, effective metadata
value, lifecycle, provenance, authority, validation classification, method,
evidence, limitation, or specification location; does not give `SMR1-VC-0001`
effect in effective metadata; does not change any VAL status, candidate
readiness, implementation conformance, or completion status; does not move any
owner-decision state (4 recorded / 417 pending, unchanged); and does not begin,
resume, or authorize `KBDL-011-SMR2-VC-0001`, which remains
`LOCKED — PLANNING-AGENT VALIDATION REQUIRED` and must be **reissued, not
resumed**, only after `KBDL-011-SMR2-FSRG1` passes planning-agent validation.
