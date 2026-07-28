# KBDL-011-R14 Evidence Manifest

The production entry point is `scripts/production_validator.py`; the real mutation entry point is `scripts/run_mutation_controls.py`. Both operate from repository sources, and every mutation invokes the production validator inside an isolated copied fixture.

Artifacts include the complete readable-group parse, 5,389-row field-source registry, 317-row effective records, authority population and graph, per-ID location/packet/dependency/evidence/limitation audits, group/ledger and precedence comparisons, counter provenance, VAL results, normative preservation, candidate status, and production summary. Each of sixteen mutation outputs is retained in `negative-tests`.

R12's eleven unresolved clause-evidence methods remain preserved and unexecuted. VAL-004 remains Not verified.

