# KBDL-011-R6 Evidence Manifest

R6 resolves every grouped value into an exact per-ID record. The resolver and independent validator do not import or call one another.

- `scripts/resolve_per_id_ledger.py` — authoritative per-ID location and packet resolver.
- `scripts/validate_per_id_records.py` — independent all-field, location, authority-chain, packet, dependency, evidence, and limitation validator.
- `scripts/capture_precommit.py` — exact command evidence capture.
- `artifacts/effective-record-audit.csv` — complete 317-row audit.
- `artifacts/exact-location-audit.csv` — exact per-ID anchor audit.
- `artifacts/authority-chain-audit.csv` — 266 Approved authority chains.
- `artifacts/packet-dependency-audit.csv` — 51 non-Approved mappings.
- `artifacts/evidence-limitation-audit.csv` — complete evidence review.
- `artifacts/validation-output.txt` — computed results.
- `precommit-transcript.txt` — commands, stdout, stderr, exit codes, results.
- `checksums.sha256` — byte sizes and full SHA-256 values.
- `implementation-report.md` — complete final evidence contract.

Implementation conformance: `NOT VERIFIED`. Project completion: `PENDING PLANNING-AGENT VALIDATION AND PROJECT-OWNER APPROVAL`. Accepted limitations: None.
