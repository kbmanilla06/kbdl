# KBDL-011-R15 Evidence Manifest

The production validator emits complete readable-group, group/ledger, location, packet, dependency, evidence, limitation, standard-clause, authority-graph, authority-reference, source-precedence, effective-record, defect, counter-provenance, and VAL audit artifacts under `artifacts/`. `artifacts/determinism-proof.txt` records two byte-identical generation runs and their identical authority-reference SHA-256 values.

The real mutation harness retains all sixteen earlier controls and ten R15 semantic controls under `negative-tests/`. Each artifact records the mutation, validator path, intended category, exit code, detected categories, fixture destruction, stdout, and stderr. `mutation-summary.txt` is the aggregate result.

`source-rules.csv` defines field ownership. `scripts/production_validator.py` is the production validator; `scripts/run_mutation_controls.py` runs the isolated repository mutations; `scripts/documentation_validator.py` executes the complete VAL-007 documentation method.

`initial-clean-state.txt`, `precommit-transcript.txt`, `implementation-report.md`, `evidence-inventory.csv`, and `checksums.sha256` provide configuration-control and evidence-contract records.
