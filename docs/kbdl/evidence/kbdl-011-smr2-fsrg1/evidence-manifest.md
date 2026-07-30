# KBDL-011-SMR2-FSRG1 Evidence Manifest

This package implements the prerequisite prompt `KBDL-011-SMR2-FSRG1`. It is
read-only with respect to every normative module file, `traceability-metadata.csv`,
`traceability-matrix.md`, every protected file, every owner-decision record, and
every R13–R16 evidence package — none of which it modifies.

**The live field-source registry is a derived, non-authoritative description of
the current source model.** It is not authority, a normative source, validation
evidence, an owner-decision record, or implementation authorization, and it does
not appear anywhere in the KBDL source-of-truth hierarchy.

Implementation authorization status: NOT AUTHORIZED

## Reproducibility

`scripts/field_source_registry.py` is the sole producer of
`artifacts/field-source-registry.csv`. The artifact is never hand-edited, and
the generator never reads a field-source registry — including its own output —
so the registry cannot become a source of truth for itself. Output bytes are a
pure function of repository content: UTF-8, LF-only, `csv`-module quoting,
column order fixed by the declared schema, row order fixed by an explicit
`(Requirement ID, declared field order)` sort key, written atomically, with no
timestamp, hostname, username, absolute path, process ID, random value, or
locale-dependent formatting. The source-model commit SHA is recorded in this
package's evidence records rather than in the artifact, so regenerating the same
tree always yields identical bytes.

`--check` regenerates into isolated temporary storage and compares bytes with
the committed artifact without writing to the repository.

## Independent correctness reference

Against the current tree the generator reproduces all 5,389 rows of
`docs/kbdl/evidence/kbdl-011-r16/artifacts/field-source-registry.csv` exactly,
except four cells across `KBDL-MOT-007` and `KBDL-MOT-008` — precisely the cells
changed by the `KBDL-011-SMR1-BH-AGC1` authority correction (commit `0fadb97`),
including MOT-007's authority now resolving because that correction removed the
two-node cycle. The generator was written independently of R16's
`production_validator.py`; the agreement is a cross-implementation check, not a
copy.

## Historical evidence preservation

`docs/kbdl/evidence/kbdl-011-r13/artifacts/field-source-registry.csv`,
`kbdl-011-r14`, `kbdl-011-r15`, and `kbdl-011-r16` remain **immutable historical
evidence**: byte-identical, never regenerated, relocated, reformatted, or used
as this generator's output path, and never read as authoritative input for
current values. Their round inventories, checksum records, validators,
transcripts, and reports are equally unchanged. `validate_fsrg1.py`'s `HIST`
gate reads each expected digest from that round's *own* committed evidence
inventory and compares the file against it — never recomputing the expected
value from the file under test — and the fixture suite proves the gate rejects a
mutation of each of the four registries independently.

## Validation architecture

`scripts/validate_fsrg1.py` reports twelve gate groups separately — SCHEMA,
DETERM, DRIFT, HIST, PATH, ISO, COVER, LABEL, PROT, DECISION, STATE, PKG —
with explicit `[PASS]`/`[FAIL]` lines, a final total, and a nonzero exit code on
any failure. No mandatory check is downgraded to a warning, and validation is
read-only: it never regenerates the committed artifact in place.

Two gates are specifically constructed so they cannot pass vacuously. DRIFT runs
the generator's `--check` in a separate process **and** performs an independent
in-process regeneration compared byte-for-byte, so a comparison that never
executed fails rather than passes; fixture 24 proves this by removing the
generator and requiring DRIFT to fail. PATH proves containment by attempting
prohibited writes — absolute path, `..` traversal, symlink escape, historical
artifact target, protected-file target — and requiring refusal with the target
byte-unchanged, rather than by inspecting the source.

`scripts/fsrg1_fixtures.py` runs 24 negative fixtures and 8 positive controls
against a single temporary repository copy, restoring each mutated file between
fixtures. The real repository is hashed before and after the whole suite and
`git status --short` compared; a temporary-tree cleanup failure fails the suite.
Every fixture reports its name, mutation, expected result, actual result,
triggered checks, and real-repository preservation result.

## Boundaries

This package changes no normative content and no effective metadata; gives
`SMR1-VC-0001` no effect in effective metadata; restores no VAL status; moves no
owner-decision state (4 durably recorded, 417 pending, unchanged); adds no
dependency; and creates no application code, API, database, migration, UI, or
deployment configuration. `KBDL-011-SMR2-VC-0001` is not begun, resumed, or
reissued and remains `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`; it may be
**reissued, not resumed**, only after `KBDL-011-SMR2-FSRG1` passes
planning-agent validation.

FSRG1 implementation is complete and **awaiting planning-agent validation**.
