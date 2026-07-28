# KBDL-011-R7 Evidence Manifest

This package records the independent effective-traceability remediation. The validator parses normative sources, 60 readable requirement groups, and the 317-row companion ledger without importing or calling either prior resolver.

## Files

- `implementation-report.md` — scope, criteria, results, risks, and rollback.
- `precommit-transcript.txt` — exact commands with complete stdout, stderr, and exit codes.
- `scripts/validate_effective_traceability.py` — independent source/group/ledger validator.
- `scripts/reconcile_evidence.py` — narrow A11Y evidence-attribution correction.
- `scripts/capture_precommit.py` — deterministic transcript capture.
- `artifacts/readable-group-parse.csv` — 317 expanded group memberships from 60 groups.
- `artifacts/effective-record-audit.csv` — all 317 effective records.
- `artifacts/exact-location-audit.csv` — independently derived locations and anchors.
- `artifacts/authority-chain-audit.csv` — all 266 Approved authority chains.
- `artifacts/packet-dependency-audit.csv` — all 51 non-Approved destinations and dependencies.
- `artifacts/evidence-attribution-audit.csv` — method/evidence ownership for 317 IDs.
- `artifacts/limitation-audit.csv` — limitation review for 317 IDs.
- `artifacts/stale-status-audit.csv` — README/validation stale-claim scan.
- `artifacts/validation-output.txt` — computed summary.
- `evidence-inventory.csv` — evidence paths, byte sizes, and full SHA-256 values.
- `checksums.sha256` — full SHA-256 digest set for evidence files.

Byte sizes and full digests are authoritative in `evidence-inventory.csv` and `checksums.sha256`. Git commit, push, remote SHA, and final clean-tree evidence are reported after the remediation commit because they cannot exist truthfully inside that same commit.
