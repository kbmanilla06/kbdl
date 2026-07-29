# KBDL-011-R16A Evidence Manifest

This package preserves the blocked source-independent R16 audit. A nonzero production-validator exit is the expected semantic conclusion, not an execution failure.

`scripts/production_validator.py` generates the complete field registry, effective records, unresolved-field detail, exact-location findings, packet/dependency findings, evidence and limitation scope findings, independent standard findings, authority classification/graph/cycle findings, status audit, counter provenance, and production summary. `scripts/documentation_validator.py` performs the complete VAL-007 documentation method. The retained mutation harness is supporting R16 work but is not used to claim a semantic PASS.

Path equivalents: `evidence-field-audit.csv` and `evidence-scope-audit.csv` preserve evidence detail; `limitation-field-audit.csv` and `limitation-scope-audit.csv` preserve limitation detail; `adopted-standard-clause-audit.csv` and `standard-clause-audit.csv` preserve independent standard detail.

The prior reported counts were 332 unresolved sources, 12 evidence mappings, and 228 limitation mappings. Final regeneration with status-only corrections produces 335 unresolved sources, 11 evidence-scope mapping defects, 14 unresolved validation-evidence fields, and 229 limitation defects. The status-only downgrades preserve prior executed-evidence and limitation candidate text rather than rewriting it, exposing additional honest field inconsistencies; VAL-005 is no longer a Verified evidence-scope candidate, reducing that separate scope count by one.
