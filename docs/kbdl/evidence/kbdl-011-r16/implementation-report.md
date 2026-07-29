# KBDL-011-R16A Durable Failed-Audit Report

Implementation-step status: PASS. R16 audit conclusion: BLOCKED.

R16 rejects ledger and readable-group self-proof. It preserves 335 unresolved field sources, 63 exact-location mismatches, 11 evidence-scope mapping defects, 229 limitation-scope mismatches, 20 standard-clause mismatches, and the MOT-007/MOT-008 authority cycle. The difference from the initially reported 332 unresolved, 12 evidence-scope, and 228 limitation findings results from applying only the three authorized validation-classification downgrades while preserving their prior candidate evidence, method, scope, and limitation fields. This exposes additional field inconsistencies; VAL-005 is no longer a Verified evidence-scope candidate, reducing that separate scope count by one.

VAL-003, VAL-004, VAL-005, and VAL-006 are Not verified. VAL-007 remains Verified only for the complete documentation-integrity method. Candidate readiness remains Not ready; implementation conformance is Not verified; project completion is pending.

No finding was resolved, suppressed, or converted into a PASS. No normative or governance source changed. Planning-agent validation of this durable failed-audit commit is the only recommended next action.

Rollback: `git revert <KBDL-011-R16A-commit-sha>`.
