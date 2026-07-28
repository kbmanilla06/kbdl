# IMPLEMENTATION PROMPT KBDL-011

## Role

Act as a senior:

* Design-language validation architect
* Requirements and lifecycle auditor
* Release-readiness reviewer
* Accessibility conformance reviewer
* Responsive-design reviewer
* Theme and color-validation reviewer
* Motion-safety reviewer
* Component-system reviewer
* Project Profile reviewer
* Manual-customization governance reviewer
* Security, privacy, correctness, and data-integrity reviewer
* Traceability and decision-register auditor
* Documentation QA engineer
* Evidence-integrity reviewer
* Git configuration-control reviewer
* Technical writer

You are performing KBDL’s final specification validation and preparing an evidence-based completion audit.

You are not implementing KBDL in a product, approving pending recommendations, accepting limitations for the project owner, or declaring the project complete.

## Current Project Context

KBDL is a reusable, framework-neutral web design-language specification.

The following roadmap steps have passed planning-agent validation:

* KBDL-001 — Specification architecture and governance
* KBDL-002 — Identity, principles, and visual consistency
* KBDL-003 — Core visual foundations
* KBDL-004 — Adaptive theme system
* KBDL-005 — Expressive motion language
* KBDL-006 — Responsive behavior and accessibility
* KBDL-007 — Core action, form, and navigation components
* KBDL-008 — Surface, overlay, feedback, system-state, and complex-presentation components
* KBDL-009 — Project Profiles
* KBDL-010 — Manual Customization

KBDL-011 is the final unlocked roadmap implementation step:

> Final Validation

Its planned document location is:

```text
docs/kbdl/validation.md
```

Its requirement module code is:

```text
VAL
```

KBDL-011 must validate the KBDL specification repository as a documentation and governance deliverable.

It must separately report that no coded KBDL project implementation has been supplied for implementation-level conformance testing.

KBDL-011 must not conflate:

* Documentation completion
* Requirement approval
* Requirement verification
* Project implementation
* Project-level KBDL conformance
* Deployment
* Production readiness
* Project completion

## Current Repository State

Expected baseline, subject to inspection:

* Repository: `kbmanilla06/kbdl`
* Branch: `main`
* Last validated commit: `55b6ba6d90a5e0c6f5dd9affbcc0ce302462de95`
* Working tree: clean
* Remote branch: synchronized
* `docs/kbdl/validation.md`: absent
* Existing `KBDL-VAL-###` requirements: none known
* KBDL-001 through KBDL-010 documents: present
* Application implementation: none known
* Deployment: not applicable
* Database: not applicable
* Completion declaration: not authorized

Inspect rather than assume this state.

If commits exist after `55b6ba6`:

1. Fetch current remote references.
2. Inspect every newer commit.
3. Preserve authorized collaborator work.
4. Do not reset to `55b6ba6`.
5. Stop and report conflicting KBDL-011 work.
6. Stop and report premature completion, implementation-package, or production-readiness work.
7. Do not overwrite, broadly reformat, discard, or rewrite newer work.

## Objective

Create and execute KBDL’s final validation specification and produce an approval-ready Final Completion Audit.

The completed step must:

1. Create `docs/kbdl/validation.md`.
2. Define KBDL’s final validation methodology.
3. Audit every KBDL requirement and decision.
4. Reconcile lifecycle, provenance, and validation status across every source.
5. Verify every Approved requirement has valid authority.
6. Verify every `Verified` claim has an executed method and recorded evidence.
7. Preserve every legitimate `Not verified` status.
8. Identify every missing-evidence defect.
9. Audit all pending recommendations, unresolved items, deferred items, and blockers.
10. Audit all decision-packet mappings and exclusions.
11. Audit traceability coverage and field completeness.
12. Re-run every repository-level validation possible without a coded product implementation.
13. Re-run calculation-based evidence where source inputs are available.
14. Audit semantic, accessibility, responsive, theme, motion, component, Profile, and customization consistency.
15. Create a complete implementation-dependent validation ledger.
16. Create a complete specification-completion matrix.
17. Create a candidate release-readiness verdict.
18. Update stale roadmap and validation-status wording.
19. Add stable `KBDL-VAL-###` requirements.
20. Add complete VAL traceability.
21. Preserve every pending recommendation status.
22. Preserve all locked requirements and shared architecture.
23. Keep implementation conformance explicitly unverified.
24. Keep completion subject to independent planning-agent review and explicit project-owner approval.
25. Return complete, reproducible evidence.

## Authorization Gate

This released prompt is not authorization to begin implementation.

Implementation may begin only after the project owner responds:

```text
APPROVE PROMPT
```

Approval authorizes only the mandatory KBDL-011 scope.

It does not approve:

* Any pending requirement
* Any decision-packet recommendation
* Any Deferred item
* Any failed-requirement deferral
* Any implementation technology
* Any project implementation
* Any accessibility exception
* Any security exception
* Any production-readiness limitation
* Any completion declaration

## Preconditions

Before editing:

1. Run `git fetch origin`.
2. Inspect configured remotes.
3. Confirm the active repository.
4. Confirm the active branch.
5. Confirm the working tree and index are clean.
6. Record local HEAD.
7. Record `origin/main`.
8. Confirm whether local HEAD equals `origin/main`.
9. Inspect the latest fifteen commits.
10. Inspect every commit after `55b6ba6`, if any.
11. Confirm `docs/kbdl/validation.md` does not contain authorized work.
12. Search the complete repository for `KBDL-VAL-###`.
13. Confirm the next unused VAL ID.
14. Confirm no completion decision has been recorded.
15. Confirm no implementation package exists.
16. Confirm no application, deployment, or database evidence has been introduced.
17. Stop and report unexpected, uncommitted, conflicting, or collaborator-owned changes.

Do not:

* Reset
* Rebase
* Amend
* Force-push
* Discard changes
* Overwrite teammate work
* Stash another contributor’s work
* Restore the repository to an earlier commit
* Rewrite any validated commit

## Source-of-Truth Hierarchy

Use:

1. Explicit project-owner approvals
2. Approved KBDL blueprint and roadmap
3. Planning-agent validation and progression decisions
4. Current repository and Git history
5. KBDL decision register
6. Per-requirement authoritative records
7. KBDL governance and conventions
8. Traceability matrix
9. Existing validation documents and evidence
10. Conformance checklist
11. Existing repository conventions
12. Applicable adopted standards

When sources conflict:

1. Stop work on the affected result.
2. Record the exact conflicting sources.
3. Identify affected requirement IDs, decisions, and files.
4. Do not silently select one status or value.
5. Do not promote or demote a requirement.
6. Do not fabricate evidence.
7. Do not mark a claim `Verified`.
8. Return the conflict for planning-agent and project-owner resolution.

## Status and Authority Model

Maintain KBDL’s three independent dimensions:

* Lifecycle status
* Provenance
* Validation status

Only lifecycle `Approved` authorizes implementation.

Only validation `Verified` means the stated validation method was executed and evidence was recorded.

A requirement may be:

* Approved and Verified
* Approved and Not verified
* Recommended and Verified
* Recommended and Not verified
* Deferred and Not verified

Validation never grants approval.

Approval never proves validation.

A requirement ID never grants authority.

A planning-agent pass for a documentation step does not make implementation-dependent behavior Verified.

## Final Validation Classification Model

Classify every validation claim as one primary evidence class.

### Class A — Repository and documentation integrity

Examples:

* Git state
* File presence
* Links
* Anchors
* headings
* tables
* ID uniqueness
* ID continuity
* status counts
* cross-references
* traceability coverage

These may become `Verified` when the checks run successfully.

### Class B — Governance and authority

Examples:

* Lifecycle authority
* approval records
* decision mappings
* exclusions
* pending-item preservation
* exception records

These may become `Verified` through exhaustive documentary comparison.

### Class C — Static specification consistency

Examples:

* Shared semantic architecture
* Profile invariants
* theme-role parity
* component contract consistency
* customization boundaries

These may become `Verified` only for the specific static consistency method executed.

### Class D — Calculation-based evidence

Examples:

* Color contrast
* numerical consistency
* sequence counts
* mapping parity

These may become `Verified` only when source inputs, formula, command, and output are recorded.

### Class E — Implementation-dependent behavior

Examples:

* Keyboard behavior
* screen-reader behavior
* focus management
* responsive reflow
* device behavior
* runtime motion
* performance
* authentication
* authorization
* system-state correctness
* production rollback

These remain `Not verified` because no implementation exists.

### Class F — Project-specific adoption

Examples:

* Profile declaration
* customization record
* project theme
* project media
* implementation evidence
* deployment

These remain `Not verified` or `Not applicable` until a project adopts KBDL.

## Required Inspection

Read every Markdown file under:

```text
docs/kbdl/
```

Also inspect:

* Root repository documentation
* Git history relevant to KBDL-001 through KBDL-010
* Every existing validation document
* Every decision-register entry
* Every requirement record
* Every packet and coverage audit
* Every conformance-checklist section
* Every traceability group
* Every planned-but-absent module reference

At minimum inspect:

* `docs/kbdl/README.md`
* `docs/kbdl/principles.md`
* `docs/kbdl/conventions.md`
* `docs/kbdl/governance.md`
* `docs/kbdl/contributing.md`
* `docs/kbdl/glossary.md`
* `docs/kbdl/decision-register.md`
* `docs/kbdl/traceability-matrix.md`
* `docs/kbdl/conformance-checklist.md`
* Every file under `docs/kbdl/foundations/`
* Every file under `docs/kbdl/themes/`
* Every file under `docs/kbdl/motion/`
* `docs/kbdl/responsive.md`
* `docs/kbdl/accessibility.md`
* `docs/kbdl/components-core.md`
* `docs/kbdl/components-system.md`
* `docs/kbdl/profiles.md`
* `docs/kbdl/customization.md`

Inspect every occurrence of:

* `Approved`
* `Recommended`
* `Unresolved`
* `Deferred`
* `Blocked`
* `Deprecated`
* `Superseded`
* `Verified`
* `Not verified`
* `Not applicable`
* `passed`
* `under validation`
* `locked`
* `unlocked`
* `complete`
* `production`
* `conformance`
* `KBDL-011`
* `validation.md`
* `final validation`
* `ten-step`
* `one roadmap step remains`
* `no implementation exists`
* `implementation-level`
* `decision packet`
* `approval-ready`
* `contingent`
* `known limitation`
* `validation evidence`

## Known Pending Boundaries

Preserve the following known sets exactly unless a later explicit project-owner decision exists in the repository.

### KBDL-006

Nine pending requirements:

```text
KBDL-RSP-002
KBDL-RSP-003
KBDL-RSP-004
KBDL-RSP-005
KBDL-RSP-008
KBDL-RSP-011
KBDL-A11Y-011
KBDL-A11Y-021
KBDL-A11Y-035
```

### KBDL-007

Ten pending requirements:

```text
KBDL-CMP-015
KBDL-CMP-017
KBDL-CMP-020
KBDL-CMP-025
KBDL-CMP-029
KBDL-CMP-036
KBDL-CMP-041
KBDL-CMP-044
KBDL-CMP-046
KBDL-CMP-048
```

### KBDL-008

Seventeen pending requirements:

```text
KBDL-CMP-067
KBDL-CMP-069
KBDL-CMP-073
KBDL-CMP-074
KBDL-CMP-076
KBDL-CMP-080
KBDL-CMP-083
KBDL-CMP-085
KBDL-CMP-089
KBDL-CMP-091
KBDL-CMP-099
KBDL-CMP-102
KBDL-CMP-105
KBDL-CMP-106
KBDL-CMP-108
KBDL-CMP-110
KBDL-CMP-111
```

### KBDL-009

Seven pending requirements:

```text
KBDL-PRO-009
KBDL-PRO-016
KBDL-PRO-017
KBDL-PRO-018
KBDL-PRO-027
KBDL-PRO-028
KBDL-PRO-029
```

Their existing state remains:

* Five independently approval-ready
* Two contingent
* None Approved

### KBDL-010

Seven Recommended requirements:

```text
KBDL-CUS-023
KBDL-CUS-024
KBDL-CUS-025
KBDL-CUS-026
KBDL-CUS-027
KBDL-CUS-028
KBDL-CUS-029
```

One Deferred requirement:

```text
KBDL-CUS-030
```

Their existing state remains:

* Seven independently approval-ready
* Zero contingent
* One Deferred tracking item
* None Approved

### Other pending items

Inventory and preserve every pending or excluded item in:

* Foundations
* Themes
* Motion
* Governance
* Accessibility
* Responsive behavior
* Components
* Profiles
* Customization

At minimum audit:

* Theme opacity values
* Translucent theme variants
* Project-specific media composites
* Account-level theme synchronization
* Forced-colors/high-contrast policy
* Data-visualization palettes
* Component-specific motion values
* Device-performance detection
* Animation technology
* Implementation token formats
* Browser-support policy
* Quantitative motion-hazard thresholds
* Machine-readable customization format
* Automated customization tooling

## Exact Scope

## 1. Create the final validation document

Create:

```text
docs/kbdl/validation.md
```

If it already exists:

1. Inspect it.
2. Identify whether it contains authorized work.
3. Preserve valid collaborator content.
4. Stop and report conflicting implementations.

Do not replace the planned file with a directory.

## 2. Required document structure

The document must contain at least:

1. Purpose and scope
2. Lifecycle and validation status
3. Final-validation principles
4. Evidence classification
5. Validation terminology
6. Repository baseline
7. Validation methodology
8. Requirement inventory
9. Lifecycle-status audit
10. Provenance audit
11. Validation-status audit
12. Approved-authority audit
13. Decision-register audit
14. Pending and deferred inventory
15. Traceability audit
16. Cross-reference and documentation-integrity audit
17. Governance and conventions audit
18. Principles audit
19. Foundations audit
20. Theme audit
21. Motion audit
22. Responsive audit
23. Accessibility audit
24. Core-component audit
25. System-component audit
26. Project Profile audit
27. Manual Customization audit
28. Security, privacy, correctness, and data-integrity audit
29. Implementation-dependent validation ledger
30. Project-specific validation ledger
31. Conformance-checklist audit
32. Scope-completion matrix
33. Defect and limitation register
34. Deferred backlog
35. Specification release-readiness assessment
36. Implementation-conformance assessment
37. Candidate Final Completion Audit
38. Normative `KBDL-VAL-###` requirements
39. VAL Requirement Coverage Matrix
40. VAL traceability
41. Completion and approval boundary

Additional sections may be added when necessary.

## 3. Validation terminology

Define at minimum:

* Final validation
* Validation method
* Validation evidence
* Evidence sufficiency
* Validation scope
* Validation class
* Documentation validation
* Static consistency validation
* Calculation-based validation
* Implementation-dependent validation
* Project-specific validation
* Verified
* Not verified
* Not applicable
* Validation defect
* Known limitation
* Accepted limitation
* Candidate final status
* Specification release readiness
* Implementation conformance
* Production readiness
* Completion approval

Do not define a limitation as accepted unless the project owner explicitly accepts it.

## 4. Complete requirement inventory

Build an exhaustive inventory of every requirement using module codes:

* GOV
* PRN
* FND
* THM
* MOT
* RSP
* A11Y
* CMP
* PRO
* CUS
* VAL

For each module record:

* First ID
* Last ID
* Total IDs
* Missing sequence numbers
* Duplicate IDs
* Approved count
* Recommended count
* Unresolved count
* Deferred count
* Blocked count
* Deprecated count
* Superseded count
* Verified count
* Not verified count
* Not applicable count
* Missing validation status
* Missing authoritative record
* Missing traceability
* Orphan traceability entry

Do not hardcode totals before inspection.

## 5. Lifecycle-status audit

For every requirement:

1. Read the authoritative record.
2. Read traceability.
3. Read any decision-register reference.
4. Read packet mapping.
5. Confirm the lifecycle status agrees everywhere.
6. Confirm any promotion has explicit project-owner authority.
7. Confirm every non-Approved requirement remains non-authoritative.
8. Confirm no validation result changed lifecycle status.
9. Confirm no prompt approval implicitly approved a packet.
10. Record every mismatch as a defect.

Do not change lifecycle status in KBDL-011.

## 6. Provenance audit

For every requirement:

* Confirm provenance is present where required.
* Confirm `Confirmed` is supported by evidence.
* Confirm `User-provided` refers to actual user-provided content.
* Confirm `Assumed` remains visible and non-authoritative.
* Confirm provenance is not represented as approval.

Correct only factual documentation mismatches.

Do not rewrite historical provenance without evidence.

## 7. Validation-status audit

For every requirement:

* Confirm a validation method exists.
* Confirm `Verified` has actual evidence.
* Confirm evidence matches the stated method.
* Confirm evidence covers the complete claim.
* Confirm `Not verified` is retained where testing was not performed.
* Confirm `Not applicable` is used only where no meaningful validation applies.
* Identify partial verification at clause level.
* Identify stale or unsupported Verified labels.
* Identify methods that cannot run without implementation.

Do not mark a requirement Verified merely because:

* Its document exists
* Its lifecycle is Approved
* A planning-agent prompt passed
* A reviewer read it
* It has a requirement ID
* Similar requirements passed
* An implementation is theoretically possible

## 8. Approved-authority audit

For every Approved requirement identify exact authority:

* Prior Approved requirement
* Adopted external standard
* Explicit project-owner decision
* Project-owner-approved prompt mandate
* Documented combination

Required result:

```text
Approved requirements lacking valid authority: 0
```

Where authority cannot be confirmed:

1. Do not invent it.
2. Do not silently demote the requirement.
3. Record a blocking lifecycle-authority defect.
4. Return `BLOCKED` or `PARTIAL PASS` as appropriate.

## 9. Decision-register audit

Audit every decision ID.

Confirm:

* Sequential uniqueness
* Exact title
* Status
* Owner
* Date
* Scope
* Requirement mapping
* Exclusions
* Evidence basis
* No duplicate decision
* No orphan decision
* No requirement claiming a nonexistent decision
* No packet represented as approved without a decision
* No decision represented more broadly than its recorded scope

Do not create a completion decision.

Completion approval belongs to the project owner after planning-agent validation.

## 10. Pending and deferred inventory

Create one exhaustive non-Approved ledger.

For every pending item record:

* Requirement ID
* Module
* Lifecycle
* Provenance
* Validation status
* Packet or tracking destination
* Dependencies
* Approval readiness
* Whether contingent
* Explicit exclusion
* Effect on specification readiness
* Effect on implementation conformance
* Recommended disposition

Do not recommend silent approval.

A pending optional policy does not automatically block documentation release.

A missing mandatory requirement or unsupported Approved authority does block release.

## 11. Traceability audit

For every requirement confirm:

* Appears exactly once
* Correct module
* Exact per-ID specification location
* Lifecycle
* Provenance
* Validation status
* Authority
* Validation method
* Validation evidence
* Known limitation
* Related decision
* Packet destination
* Pending dependencies
* Profile impact where applicable
* Future validation dependency
* Notes

Grouped entries are allowed only when every ID remains individually auditable.

Required result:

```text
Missing requirement traceability: 0
Duplicate requirement traceability: 0
Orphan traceability entries: 0
```

## 12. Documentation-integrity audit

Validate every Markdown file for:

* Relative links
* Heading anchors
* Visible section labels
* Heading hierarchy
* Duplicate headings
* Empty sections
* Placeholder text
* Conflict markers
* Malformed tables
* Missing table cells
* Duplicate IDs
* Invalid IDs
* Broken decision links
* Broken requirement links
* Broken packet references
* Planned-file links presented as existing links
* Stale lock wording
* Stale roadmap-step counts
* Contradictory completion claims

Audit the existing “ten-step roadmap” wording and reconcile it with the approved KBDL-011 roadmap only after confirming the approved roadmap source.

## 13. Governance and conventions audit

Verify:

* Status dimensions remain independent.
* Only Approved authorizes implementation.
* Verified requires evidence.
* Unverified work is not labeled complete.
* Failed mandatory requirements are not silently deferred.
* Locked-rule exceptions require Approved decisions.
* Requirement IDs remain stable.
* Cross-reference conventions are followed.
* Restoration and rollback guidance is present.
* Roadmap progression remains gated.

## 14. Principles and shared-architecture audit

Verify repository-wide preservation of:

* KBDL identity
* Digital Luxury
* Technical Utility
* Clarity before spectacle
* Consumer comprehension
* Accessibility by default
* Adaptability without fragmentation
* Performance-aware enhancement
* Safety and data integrity priority
* Shared semantic architecture
* Shared accessibility architecture

Identify any module that contradicts a higher-priority principle.

## 15. Foundations audit

Audit:

* Color role inventory
* Typography architecture
* Spacing and layout architecture
* Shape and corner architecture
* Elevation and depth
* Iconography
* Imagery and media
* Approved values
* Pending values
* Cross-module consumption
* Profile consistency
* Customization boundaries

Confirm no later module silently introduced a new foundation primitive as Approved.

## 16. Theme audit

Re-run and reconcile:

* Semantic-role inventory count
* Light-mode mapping completeness
* Dark-mode mapping completeness
* Alias model
* Theme parity
* Approved opaque contrast pairs
* Focus contrast
* Status-family contrast
* Gradient caption-band evidence
* Decorative exemptions
* Unverified opacity and translucency
* User-preference precedence
* Profile consistency
* Customization boundaries

Use a dependency-free script for calculations.

Record:

* Exact source values
* Formula
* Pair
* Ratio
* Threshold
* Result
* Restriction or exemption
* Script checksum

Do not infer translucent contrast without approved opacity and background inputs.

## 17. Motion audit

Re-run documentation-level checks for:

* Purpose completeness
* Category completeness
* Hierarchy
* Timing-class consistency
* Exit-versus-entrance relationships
* Easing-category consistency
* Spatial ranges
* Choreography
* Reduced-motion matrix
* No-motion parity
* Motion-safety language
* Profile consistency
* Theme transition consistency
* Pending implementation values
* Deferred technology decisions

Do not mark runtime motion, performance, interruption, or safety behavior Verified without implementation evidence.

## 18. Responsive audit

Audit:

* Content-driven adaptation
* Source-order preservation
* Focus-order preservation
* Reflow requirements
* Text resizing
* Orientation
* safe areas
* virtual keyboard behavior
* input parity
* component transformation references
* Profile emphasis
* pending exact breakpoints
* pending grid values
* pending gutter and container values
* pending dense-data transformation

Do not mark real-device behavior Verified.

## 19. Accessibility audit

Audit the complete WCAG 2.2 Level AA mapping.

Confirm:

* No AAA criterion is mislabeled AA.
* Every adopted criterion maps to KBDL requirements.
* Contrast evidence is scoped correctly.
* Keyboard behavior remains Not verified without implementation.
* Screen-reader behavior remains Not verified.
* Focus-management behavior remains Not verified.
* Zoom and reflow implementation remain Not verified.
* Forced-colors behavior remains pending where applicable.
* Target-size requirements and pending enhancement remain distinct.
* Motion safety remains preserved.
* Error, status, authentication, and recovery requirements remain present.

Do not claim complete WCAG conformance.

## 20. Component audits

Audit all `KBDL-CMP-###` requirements.

Confirm:

* Complete sequence and uniqueness
* Core/system module boundary
* Shared semantic contracts
* Shared accessibility contracts
* Anatomy consistency
* State consistency
* Focus and keyboard requirements
* Overlay and modality rules
* Feedback and live-region rules
* System-state honesty
* Data-presentation semantics
* Profile mappings
* Customization boundaries
* Pending component policies remain non-authoritative

Do not claim runtime component conformance.

## 21. Project Profile audit

Verify:

* Showcase, Precision, and Flow share one architecture.
* Profile is distinct from theme, viewport, role, and preference.
* Locked rules remain shared.
* Profile-specific semantics do not exist.
* Profile-specific accessibility exceptions do not exist.
* Profile mappings are complete.
* Five approval-ready and two contingent recommendations remain correctly separated.
* No profile implementation is claimed.

## 22. Manual Customization audit

Verify:

* Customization is manual and documented.
* Records do not create authority.
* Six customization classes remain distinct.
* Locked requirements cannot be bypassed.
* Approved controlled options remain bounded.
* Open expression remains subordinate.
* Project-local and reusable customization remain distinct.
* Seven packet items remain independently approval-ready.
* `KBDL-CUS-030` remains Deferred.
* No customization implementation or exception exists.
* No final-validation policy was silently approved by KBDL-010.

## 23. Security, privacy, correctness, and data-integrity audit

Audit documentation requirements for:

* Authentication
* Authorization
* Data ownership
* Sensitive-data handling
* Input validation
* Safe errors
* State accuracy
* Consequential actions
* Permission privacy
* Not-found privacy
* Auditability
* Recovery
* Rollback

Report these as specification requirements.

Do not mark implementation security Verified.

## 24. Implementation-dependent validation ledger

Create a complete ledger of requirements that cannot be validated without implementation.

Classify each as:

* Keyboard
* Screen reader
* Focus management
* Pointer/touch
* Zoom/reflow
* Forced colors
* Motion runtime
* Performance
* Browser compatibility
* Device compatibility
* Authentication
* Authorization
* Data integrity
* Offline behavior
* System-state correctness
* Deployment
* Rollback execution
* Project-specific content
* Project-specific customization
* Other

For each record:

* Requirement ID
* Validation method
* Required implementation evidence
* Current status
* Reason not run
* Blocking effect on documentation release
* Blocking effect on implementation conformance
* Future owner

Do not hide this ledger in a summary count.

## 25. Conformance-checklist audit

Preserve every existing checklist row.

Add a KBDL-011 Final Validation section covering at least:

1. Every requirement is inventoried.
2. Every requirement has one authoritative record.
3. Every requirement is traced exactly once.
4. Every lifecycle status agrees across sources.
5. Every Approved requirement has authority.
6. Every Verified claim has evidence.
7. Every Not verified claim is explicit.
8. Every pending item has a tracking destination.
9. Every decision maps to its exact scope.
10. Every link and anchor resolves.
11. Every table is valid.
12. Every requirement ID is unique.
13. Shared architecture is preserved.
14. Accessibility mappings are accurate.
15. Theme calculations are reproducible.
16. Motion runtime claims remain appropriately unverified.
17. Responsive/device claims remain appropriately unverified.
18. Component runtime claims remain appropriately unverified.
19. Profile invariants are preserved.
20. Customization boundaries are preserved.
21. Security implementation is not claimed.
22. Specification release readiness is assessed separately.
23. Implementation conformance is assessed separately.
24. Known limitations are complete.
25. Deferred work is complete and traceable.
26. No completion claim appears before approval.

Do not pre-mark repository checklist rows Passed.

## 26. Scope-completion matrix

Create a matrix for KBDL-001 through KBDL-011 containing:

* Prompt ID
* Module
* Deliverables
* Validated commit
* Planning-agent status
* Requirement range
* Lifecycle summary
* Validation summary
* Open defects
* Pending recommendations
* Deferred items
* Implementation-dependent limitations
* Completion status

Do not invent validated commits.

Use repository history and supplied planning-agent state.

Where a historical commit cannot be confirmed, mark it unresolved rather than guessing.

## 27. Specification release-readiness assessment

Assess the documentation specification independently from implementation.

Review:

* Scope completeness
* Internal consistency
* Governance completeness
* Traceability
* Decision integrity
* Validation evidence
* Accessibility specification
* Responsive specification
* Security requirements
* Documentation quality
* Rollback
* Deferred backlog
* Known risks

Use one candidate status:

* `PRODUCTION READY`
* `READY WITH ACCEPTED LIMITATIONS`
* `PARTIAL PASS`
* `BLOCKED`
* `NOT READY`

Interpretation rules:

### PRODUCTION READY

May refer only to the KBDL specification repository as a documentation deliverable.

It must never imply that a project implementation is production ready.

Use only when:

* Every mandatory documentation criterion passes.
* No blocking defect remains.
* All limitations are non-blocking.
* No limitation requires unrecorded acceptance.

### READY WITH ACCEPTED LIMITATIONS

May become final only after the project owner explicitly accepts the listed limitations.

Before that approval, report:

```text
Candidate status: READY WITH ACCEPTED LIMITATIONS
Limitation acceptance: Pending project-owner approval
```

### PARTIAL PASS

Use when substantial scope passes but one or more nontrivial mandatory areas remain incomplete or unverified for reasons beyond intentional implementation absence.

### BLOCKED

Use when validation cannot continue due to missing authority, conflicting sources, inaccessible required evidence, repository conflict, or security/data-integrity uncertainty.

### NOT READY

Use when mandatory specification criteria fail materially.

Do not preselect a favorable result.

## 28. Implementation-conformance assessment

Report separately:

```text
Implementation conformance status: NOT VERIFIED
```

unless a complete implementation and the required evidence are actually supplied.

The absence of implementation is expected and does not by itself invalidate the documentation specification.

It does prohibit claims about:

* Runtime accessibility
* Browser compatibility
* Device compatibility
* Performance
* Security implementation
* Production behavior
* Deployment
* Project-level KBDL conformance

## 29. Defects, limitations, and deferred work

Classify every finding:

* P0 Critical
* P1 High
* P2 Medium
* P3 Low
* Known limitation
* Deferred backlog
* Pending recommendation
* Not applicable

Do not call a pending recommendation a defect unless an Approved requirement depends on it.

Do not call implementation absence a documentation defect when implementation is explicitly out of scope.

Do classify unsupported `Verified` labels, invalid Approved authority, broken traceability, or contradictory status claims as defects.

## 30. KBDL-011 requirement architecture

Create requirements using:

```text
KBDL-VAL-###
```

Before assigning IDs:

1. Search the complete repository.
2. Begin at the next unused sequential number.
3. Use zero-padded three-digit numbering.
4. Never reuse an ID.
5. Assign one primary ID per independently testable final-validation rule.
6. Give each requirement one authoritative normative location.
7. Add complete metadata.

Each VAL record must include:

* Requirement ID and rule
* Lifecycle status
* Provenance
* Validation status
* Authority
* Evidence class
* Related requirements
* Applicable modules
* Specification location
* Pending dependencies
* Validation method
* Validation evidence
* Known limitation

The project-owner-approved KBDL-011 prompt may authorize its mandatory final-validation methodology.

Do not use VAL requirements to approve or alter another module’s policy.

Do not target an arbitrary requirement count.

## 31. KBDL-011 policy boundary

Do not create a KBDL-011 decision packet.

This prompt supplies the required final-validation methodology.

If a genuinely new discretionary validation policy is required but not authorized here:

1. Stop.
2. Record the policy gap.
3. Return `BLOCKED`.
4. Do not invent a Recommended policy.
5. Do not expand the final step silently.

## 32. VAL Requirement Coverage Matrix

Create a matrix containing every VAL requirement exactly once.

Include:

* ID
* Title
* Evidence class
* Lifecycle
* Provenance
* Validation status
* Authority
* Related modules
* Specification location
* Pending dependency
* Validation method
* Evidence
* Known limitation

## 33. VAL traceability

Add complete traceability for every VAL requirement.

Each entry must include:

* Blueprint section
* Roadmap prompt
* Requirement ID
* Per-ID specification location
* Lifecycle
* Provenance
* Validation status
* Authority
* Evidence class
* Validation method
* Validation evidence
* Known limitation
* Related requirements
* Pending dependencies
* Notes

Every VAL ID must appear exactly once.

## 34. Cross-module updates

Update only where necessary:

* `docs/kbdl/README.md`
* `docs/kbdl/traceability-matrix.md`
* `docs/kbdl/conformance-checklist.md`
* `docs/kbdl/glossary.md`
* Documents containing stale KBDL-010/KBDL-011 progression wording
* Documents containing inaccurate validation-status references

### README requirements

Update the index to state:

* KBDL-010 passed planning-agent validation.
* KBDL-011 deliverables are present.
* `validation.md` resolves.
* Final validation has been performed at documentation level.
* The specification’s candidate release-readiness status.
* Implementation conformance remains Not verified.
* No pending recommendation is approved.
* No project implementation is claimed.
* Completion remains pending planning-agent validation and project-owner approval.
* The project is not yet declared complete.

Correct stale roadmap-step counts only after confirming the approved roadmap.

### Traceability requirements

Update validation status only where the final method actually ran and evidence exists.

Do not broadly replace `Not verified` with `Verified`.

### Decision register

Do not add a completion decision.

Do not add a limitation-acceptance decision.

Do not alter decision scope.

## 35. Completion and approval boundary

KBDL-011 implementation must not declare the project complete.

It must produce a candidate Final Completion Audit for independent review.

After implementation:

1. The planning agent validates KBDL-011.
2. Any defects enter remediation.
3. If KBDL-011 passes, state moves to `RELEASE_READINESS`.
4. The project owner reviews the Final Completion Audit.
5. The project owner explicitly accepts or rejects limitations.
6. The project owner explicitly approves or rejects completion.
7. Only then may state move to `COMPLETED`.

## Out of Scope

Do not:

* Create an application implementation
* Create HTML, CSS, JavaScript, TypeScript, JSON, YAML, JSX, TSX, Vue, Svelte, or Angular files
* Create package files
* Add dependencies
* Create framework configuration
* Create token packages
* Create automated validation infrastructure
* Create CI workflows
* Create a deployment
* Create a database
* Create design assets
* Create implementation examples presented as tested
* Approve any recommendation
* Approve any packet
* Approve any Deferred item
* Accept any limitation
* Create any exception
* Create a completion decision
* Declare the project complete
* Claim project-level KBDL conformance
* Claim full WCAG conformance
* Claim browser support
* Claim production security
* Claim production readiness for an implementation
* Modify lifecycle statuses
* Change Approved values
* Change component semantics
* Change Profile architecture
* Change customization policy
* Begin implementation-package work
* Modify unrelated files
* Amend or rewrite validated history
* Reset, rebase, or force-push

## Security Requirements

The final validation must:

* Inspect the repository for exposed secrets.
* Inspect documentation examples for credentials or personal data.
* Verify security requirements exist where relevant.
* Verify authorization is not represented as visual hiding.
* Verify error examples avoid sensitive diagnostics.
* Verify state-completion claims require confirmed outcomes.
* Verify project customization cannot bypass security controls.
* Verify no security implementation is claimed without evidence.
* Record security implementation as Not verified.

Do not perform intrusive security testing against external systems.

## UI and UX Requirements

No application UI is being implemented.

Validate that the specification requires:

* Responsive behavior
* WCAG 2.2 Level AA
* Keyboard support
* Focus visibility and management
* Pointer and touch parity
* Loading states
* Empty states
* Error states
* Success states
* Disabled states
* Offline states
* Permission states
* Reduced-motion behavior
* No-motion parity
* Light and dark parity
* Shared component semantics
* Project Profile invariants
* Manual customization boundaries

Mark runtime behavior Not verified.

## Implementation Requirements

Perform work in this order:

1. Inspect repository and remote state.
2. Inspect recent commits.
3. Confirm KBDL-011 has not started.
4. Read every KBDL Markdown file.
5. Inventory every requirement.
6. Inventory every decision.
7. Inventory every packet.
8. Inventory every pending and deferred item.
9. Inventory every existing validation claim.
10. Define final-validation terminology and evidence classes.
11. Create `validation.md`.
12. Assign VAL IDs.
13. Audit lifecycle status.
14. Audit provenance.
15. Audit validation status.
16. Audit Approved authority.
17. Audit decisions.
18. Audit pending-item coverage.
19. Audit traceability.
20. Audit links, anchors, headings, tables, and IDs.
21. Audit governance and conventions.
22. Audit principles and shared architecture.
23. Audit foundations.
24. Re-run theme calculations.
25. Audit motion documentation.
26. Audit responsive requirements.
27. Audit accessibility mappings.
28. Audit all components.
29. Audit Profiles.
30. Audit Manual Customization.
31. Audit security/privacy/correctness requirements.
32. Create the implementation-dependent validation ledger.
33. Update conformance checklist.
34. Create the scope-completion matrix.
35. Create the defect and limitation register.
36. Create the candidate release-readiness assessment.
37. Create the candidate Final Completion Audit.
38. Add VAL traceability.
39. Update README and stale validation references.
40. Run complete repository validation.
41. Inspect the complete diff.
42. Confirm no lifecycle status changed.
43. Confirm no pending recommendation was promoted.
44. Confirm no implementation claim was created.
45. Confirm no completion decision was created.
46. Commit KBDL-011 separately.
47. Push only by normal fast-forward.
48. Return the complete implementation and audit evidence.
49. Do not declare completion.

## Acceptance Criteria

### KBDL-011-AC-001 — Repository safety

Work begins from a clean, synchronized repository and preserves collaborator work.

### KBDL-011-AC-002 — Baseline preservation

Commit `55b6ba6` remains unchanged.

### KBDL-011-AC-003 — Validation document

`docs/kbdl/validation.md` exists with substantive final-validation content.

### KBDL-011-AC-004 — Module continuity

The planned path and `VAL` module code are used.

### KBDL-011-AC-005 — Complete scope distinction

Documentation readiness, validation, implementation conformance, deployment, production readiness, and completion remain distinct.

### KBDL-011-AC-006 — Evidence classification

Every validation claim has a correct evidence class.

### KBDL-011-AC-007 — Requirement inventory

Every KBDL requirement is inventoried exactly once.

### KBDL-011-AC-008 — Module inventory

Every module has accurate ID ranges, counts, lifecycle totals, and validation totals.

### KBDL-011-AC-009 — ID integrity

All requirement IDs are unique, valid, and stable.

### KBDL-011-AC-010 — Lifecycle consistency

Every requirement has one consistent lifecycle status across all sources.

### KBDL-011-AC-011 — Provenance consistency

Every requirement’s provenance is accurate and non-authoritative by itself.

### KBDL-011-AC-012 — Validation-status consistency

Every requirement has an accurate validation status.

### KBDL-011-AC-013 — Verified-evidence integrity

Every Verified claim has an executed method and evidence covering the complete claim.

### KBDL-011-AC-014 — Not-verified integrity

Every implementation-dependent or untested claim remains Not verified.

### KBDL-011-AC-015 — Approved-authority integrity

Every Approved requirement has valid documented authority.

### KBDL-011-AC-016 — No lifecycle mutation

KBDL-011 changes no lifecycle status.

### KBDL-011-AC-017 — Decision integrity

Every decision is unique, scoped correctly, and mapped accurately.

### KBDL-011-AC-018 — No fabricated approval

No packet, recommendation, deferred item, exception, limitation, or completion status is represented as approved.

### KBDL-011-AC-019 — Pending-item inventory

Every non-Approved requirement has one auditable tracking destination.

### KBDL-011-AC-020 — KBDL-006 boundary

All nine KBDL-006 recommendations remain non-authoritative.

### KBDL-011-AC-021 — KBDL-007 boundary

All ten KBDL-007 recommendations remain non-authoritative.

### KBDL-011-AC-022 — KBDL-008 boundary

All seventeen KBDL-008 recommendations remain non-authoritative.

### KBDL-011-AC-023 — KBDL-009 boundary

All seven KBDL-009 recommendations retain their five-ready/two-contingent state.

### KBDL-011-AC-024 — KBDL-010 boundary

Seven KBDL-010 recommendations remain approval-ready and `KBDL-CUS-030` remains Deferred.

### KBDL-011-AC-025 — Other pending boundaries

No pending foundation, theme, motion, accessibility, or implementation item is promoted.

### KBDL-011-AC-026 — Traceability coverage

Every requirement appears exactly once in traceability.

### KBDL-011-AC-027 — Traceability completeness

Every traceability record contains all required fields.

### KBDL-011-AC-028 — Per-ID traceability

Every grouped traceability entry remains individually auditable.

### KBDL-011-AC-029 — Link integrity

All relative links and anchors resolve.

### KBDL-011-AC-030 — Heading integrity

All headings and visible section labels are valid and consistent.

### KBDL-011-AC-031 — Table integrity

All Markdown tables parse consistently.

### KBDL-011-AC-032 — Placeholder integrity

No unfinished placeholder or conflict marker remains.

### KBDL-011-AC-033 — Roadmap accuracy

Roadmap-step counts, statuses, and progression wording are accurate.

### KBDL-011-AC-034 — Governance integrity

Approval, verification, exception, scope-change, and completion rules remain consistent.

### KBDL-011-AC-035 — Shared-architecture integrity

One semantic and accessibility architecture is preserved.

### KBDL-011-AC-036 — Principles consistency

No module contradicts an Approved higher-priority principle.

### KBDL-011-AC-037 — Foundation integrity

No later module silently introduces or approves an unauthorized foundation value.

### KBDL-011-AC-038 — Theme completeness

The semantic-role inventory, mode mappings, parity model, and approved opaque evidence reconcile.

### KBDL-011-AC-039 — Theme calculation reproducibility

Every calculation-based theme result is reproducible from recorded source values and formulas.

### KBDL-011-AC-040 — Theme limitation integrity

Opacity, translucency, project media, forced colors, and pending palettes remain appropriately unverified or pending.

### KBDL-011-AC-041 — Motion consistency

Motion hierarchy, values, ranges, substitutions, and safety guidance reconcile across sources.

### KBDL-011-AC-042 — Motion validation honesty

Runtime motion and performance remain Not verified.

### KBDL-011-AC-043 — Responsive consistency

Responsive requirements and pending exact values remain distinct.

### KBDL-011-AC-044 — Responsive validation honesty

Real-device, zoom, reflow, orientation, safe-area, and virtual-keyboard behavior remain Not verified.

### KBDL-011-AC-045 — Accessibility mapping

The WCAG 2.2 Level AA mapping is accurate and complete within its documented scope.

### KBDL-011-AC-046 — Accessibility validation honesty

No complete WCAG, screen-reader, keyboard, or browser-conformance claim is made.

### KBDL-011-AC-047 — Component ID integrity

The complete CMP sequence is unique and correctly partitioned.

### KBDL-011-AC-048 — Component-contract consistency

Core and system component semantics, anatomy, states, and accessibility contracts reconcile.

### KBDL-011-AC-049 — Component validation honesty

Runtime component behavior remains Not verified.

### KBDL-011-AC-050 — Profile invariants

Showcase, Precision, and Flow retain one shared architecture.

### KBDL-011-AC-051 — Profile decision integrity

Profile recommendations and contingencies remain correctly separated.

### KBDL-011-AC-052 — Customization integrity

Manual customization cannot create authority or bypass locked rules.

### KBDL-011-AC-053 — Customization decision integrity

Seven KBDL-010 packet items remain independently approval-ready and CUS-030 remains Deferred.

### KBDL-011-AC-054 — Security specification completeness

Security, privacy, correctness, and data-integrity requirements are present and consistent.

### KBDL-011-AC-055 — Security validation honesty

No security implementation is represented as verified.

### KBDL-011-AC-056 — Implementation-dependent ledger

Every implementation-dependent validation gap is explicitly recorded.

### KBDL-011-AC-057 — Project-specific ledger

Every project-specific validation dependency is explicitly recorded.

### KBDL-011-AC-058 — Checklist completeness

The KBDL-011 checklist section covers all required final-validation controls.

### KBDL-011-AC-059 — Checklist preservation

All earlier checklist rows remain intact and unmarked.

### KBDL-011-AC-060 — Scope-completion matrix

Every KBDL-001 through KBDL-011 step has a complete, evidence-based entry.

### KBDL-011-AC-061 — Defect classification

Every finding is classified by severity or limitation type.

### KBDL-011-AC-062 — Deferred backlog

Every Deferred item remains visible and traceable.

### KBDL-011-AC-063 — Specification-readiness assessment

The candidate specification status follows the defined evidence rules.

### KBDL-011-AC-064 — Implementation-conformance assessment

Implementation conformance is reported separately and honestly.

### KBDL-011-AC-065 — Limitation-acceptance boundary

No limitation is called accepted without project-owner approval.

### KBDL-011-AC-066 — VAL IDs

All VAL IDs are unique, sequential, stable, and correctly referenced.

### KBDL-011-AC-067 — VAL metadata

Every VAL record contains complete metadata.

### KBDL-011-AC-068 — VAL authority

Every Approved VAL requirement is fully supported by prior authority or the approved prompt.

### KBDL-011-AC-069 — VAL traceability

Every VAL requirement has complete, per-ID traceability.

### KBDL-011-AC-070 — No VAL policy expansion

No unapproved discretionary validation policy is introduced.

### KBDL-011-AC-071 — Index accuracy

README accurately records KBDL-010 as passed and KBDL-011 as present under final review.

### KBDL-011-AC-072 — Existing-work protection

No Approved KBDL-001 through KBDL-010 rule, value, decision, or packet mapping is unintentionally changed.

### KBDL-011-AC-073 — Scope control

No implementation package, tool, schema, deployment, exception, approval, or later work is introduced.

### KBDL-011-AC-074 — Evidence completeness

All required commands, scripts, outputs, checksums, and criteria results are supplied.

### KBDL-011-AC-075 — Safe commit

KBDL-011 is committed separately without rewriting history.

### KBDL-011-AC-076 — Safe push

The KBDL-011 commit is pushed by normal fast-forward.

### KBDL-011-AC-077 — Completion gate

The project is not declared complete before planning-agent validation and project-owner approval.

## Required Validation

Run every existing applicable repository validator.

Record exact command, complete stdout, complete stderr, exit code, and result for:

```bash
git fetch origin
git remote -v
git branch --show-current
git status --short
git rev-parse HEAD
git rev-parse origin/main
git log --oneline --decorate -15
git show --no-patch --format=fuller 55b6ba6
git diff --check
```

Run complete dependency-free validation for:

1. Repository file inventory
2. Markdown link resolution
3. Heading-anchor resolution
4. Visible section-label resolution
5. Heading hierarchy
6. Duplicate headings
7. Empty sections
8. Placeholder text
9. Conflict markers
10. Markdown-table structure
11. Requirement-ID format
12. Requirement-ID uniqueness
13. Requirement-ID sequence
14. Per-module requirement totals
15. Lifecycle totals
16. Provenance totals
17. Validation-status totals
18. Missing status fields
19. Approved-authority coverage
20. Verified-evidence coverage
21. Non-Approved tracking coverage
22. Decision-ID sequence
23. Decision uniqueness
24. Decision-to-requirement mappings
25. Packet-item uniqueness
26. Packet coverage
27. Contingent mappings
28. Deferred-item tracking
29. Traceability coverage
30. Traceability duplicates
31. Traceability field completeness
32. Per-ID traceability locations
33. Orphan source requirements
34. Orphan traceability entries
35. Orphan decisions
36. Broken decision references
37. Broken packet references
38. Stale roadmap references
39. Stale validation-status references
40. Theme-role inventory
41. Light/dark parity
42. Theme aliases
43. Contrast calculations
44. Decorative-exemption restrictions
45. Motion value consistency
46. Motion entrance/exit relationships
47. Reduced-motion matrix completeness
48. Responsive/WCAG mapping
49. Accessibility criterion-level mapping
50. Complete CMP sequence
51. Component cross-module coverage
52. Profile requirement coverage
53. Profile packet coverage
54. CUS requirement coverage
55. CUS packet coverage
56. Shared-architecture invariants
57. Earlier-module promotion scans
58. Scope exclusions
59. Secret-pattern scan
60. Implementation-artifact exclusion
61. Deployment-artifact exclusion
62. Completion-claim exclusion
63. Conformance-checklist preservation
64. KBDL-011 checklist coverage
65. VAL requirement coverage
66. VAL traceability
67. Final working-tree cleanliness
68. Safe-fast-forward eligibility

### Required summary output

```text
Total requirements: <exact>
Approved: <exact>
Recommended: <exact>
Unresolved: <exact>
Deferred: <exact>
Blocked: <exact>
Deprecated: <exact>
Superseded: <exact>
Verified: <exact>
Not verified: <exact>
Not applicable: <exact>

Approved requirements lacking authority: 0
Verified claims lacking evidence: 0
Missing requirement traceability: 0
Duplicate requirement traceability: 0
Orphan traceability entries: 0
Orphan decisions: 0
Pending requirements lacking tracking: 0
Broken links or anchors: 0
Malformed tables: 0
Requirement-ID duplicates: 0
Decision-ID duplicates: 0
Earlier-module promotions: 0
Unauthorized lifecycle changes: 0
Implementation-level claims without evidence: 0
Completion decisions created: 0
```

### Required boundary output

```text
KBDL-006 pending: 9
KBDL-007 pending: 10
KBDL-008 pending: 17
KBDL-009 Recommended: 7
KBDL-009 approval-ready: 5
KBDL-009 contingent: 2
KBDL-010 Recommended: 7
KBDL-010 approval-ready: 7
KBDL-010 contingent: 0
KBDL-CUS-030 Deferred: 1
```

### Required readiness output

```text
Specification release candidate status: <status>
Limitation acceptance: <Not required | Pending project-owner approval>
Implementation conformance status: NOT VERIFIED
Project completion status: PENDING PLANNING-AGENT VALIDATION AND PROJECT-OWNER APPROVAL
```

## Required Evidence

Return:

* Initial repository state
* Initial HEAD
* Initial remote-main SHA
* Recent commits inspected
* Complete file inventory
* Files inspected
* Existing validation-document inventory
* Existing VAL-ID search
* Complete requirement inventory
* Per-module ID ranges and totals
* Lifecycle totals
* Provenance totals
* Validation-status totals
* Complete Approved-authority audit
* Complete Verified-evidence audit
* Complete decision-register audit
* Complete pending/deferred ledger
* Complete traceability audit
* Link and anchor results
* Heading and section-label results
* Table results
* Theme calculation results
* Theme script
* Motion consistency results
* Responsive and accessibility mapping results
* CMP coverage results
* Profile audit
* Customization audit
* Security specification audit
* Implementation-dependent ledger
* Project-specific ledger
* Scope-completion matrix
* Defect and limitation register
* Candidate Final Completion Audit
* Files created
* Files changed
* Exact validation commands
* Complete custom-script source
* Exact script invocations
* Complete stdout
* Complete stderr
* Exit codes
* Evidence-file paths
* Evidence-file byte sizes
* Complete SHA-256 checksums
* Evidence availability
* Diff statistics
* Commit SHA
* Branch
* Push output
* Final remote-main SHA
* Final working-tree status
* Failed or skipped validation
* Remaining defects
* Remaining risks
* Items not verified
* Rollback command

## Evidence Integrity Requirements

1. Use one complete record per command.
2. Include exact command, purpose, exit code, stdout, stderr, and result.
3. Provide complete source for every custom script.
4. Provide exact invocation for every script.
5. Provide complete 64-character SHA-256 values.
6. Do not truncate acceptance criteria.
7. Do not group criteria without individual evidence.
8. Do not omit failed or skipped checks.
9. Do not duplicate report sections.
10. Do not use malformed evidence tables.
11. Attach evidence files where supported.
12. Include critical evidence directly in the report.
13. A local path alone is insufficient.
14. Clearly mark unavailable evidence.
15. Never claim a check ran when it did not.

## Rollback Considerations

Keep all KBDL-011 changes in one separate commit.

Do not amend `55b6ba6`.

Record the initial SHA before editing.

Expected rollback:

```bash
git revert <KBDL-011-commit-sha>
```

The rollback must remove or reverse:

* `validation.md`
* VAL requirements
* VAL traceability
* README final-validation updates
* Glossary additions
* Checklist additions
* Validation-status corrections
* Stale roadmap-reference corrections
* KBDL-011 cross-module links

Do not use reset, rebase, amend, or force-push.

## Required Final Report

Return exactly:

# Implementation Result

## Status

Choose exactly one:

* PASS
* PARTIAL PASS
* FAIL
* BLOCKED

## Summary

## Root Cause

Use:

```text
Not applicable — final validation implementation, not defect remediation.
```

## Repository Inspection

## Commits Inspected

## Files Inspected

## Changes Made

## Final Validation Methodology

## Evidence Classification

## Requirement Inventory

## Lifecycle Audit

## Provenance Audit

## Validation-Status Audit

## Approved-Authority Audit

## Verified-Evidence Audit

## Decision-Register Audit

## Pending and Deferred Inventory

## Traceability Audit

## Documentation-Integrity Audit

## Governance and Conventions Audit

## Principles and Shared-Architecture Audit

## Foundations Audit

## Theme Audit

## Motion Audit

## Responsive Audit

## Accessibility Audit

## Core-Component Audit

## System-Component Audit

## Project Profile Audit

## Manual Customization Audit

## Security, Privacy, Correctness, and Data-Integrity Audit

## Implementation-Dependent Validation Ledger

## Project-Specific Validation Ledger

## Conformance-Checklist Audit

## Scope-Completion Matrix

## VAL Requirements Added

Include:

* Starting VAL ID
* Ending VAL ID
* Total
* Lifecycle breakdown
* Provenance breakdown
* Validation-status breakdown
* Authority breakdown
* Evidence-class breakdown

## Files Changed

## Validation Scripts

Provide complete source and exact invocation for every custom script.

## Validation Performed

For every command provide:

### [Command name]

**Command:**

```text
[exact command]
```

**Purpose:**
[Purpose]

**Exit code:**
[Exact exit code]

**Stdout:**

```text
[complete stdout]
```

**Stderr:**

```text
[complete stderr or "(empty)"]
```

**Result:**
Pass or Fail

## Acceptance Criteria Results

List `KBDL-011-AC-001` through `KBDL-011-AC-077` individually.

For each provide:

* Exact criterion
* Result: Passed, Failed, Not verified, or Not applicable
* Evidence
* Remaining uncertainty

## Evidence Files

For every evidence file provide:

* Path
* Purpose
* Size
* Full SHA-256
* Availability

## Failed or Skipped Validation

## Defects Found

Classify every defect:

* P0 Critical
* P1 High
* P2 Medium
* P3 Low

## Known Limitations

## Deferred Backlog

## Remaining Risks

## Items Not Verified

## Scope Compliance

## Repository Changes Outside Scope

## Rollback Plan

## Commit and Branch

## Push Status

## Deployment Status

Use:

```text
Not applicable
```

# Candidate Final Completion Audit

## Final Status

Choose one candidate:

* PRODUCTION READY
* READY WITH ACCEPTED LIMITATIONS
* PARTIAL PASS
* BLOCKED
* NOT READY

## Status Interpretation

State explicitly that this status concerns the KBDL specification repository.

## Scope Completion Matrix

## Validation Evidence

## Production Verification

Use:

```text
Not applicable to a coded implementation; implementation conformance remains Not verified.
```

## Unverified Areas

## Known Defects

## Accepted Limitations

Use one:

```text
None required
```

or:

```text
Pending explicit project-owner acceptance
```

Do not call a limitation accepted without approval.

## Deferred Backlog

## Security Status

## Deployment Status

Use:

```text
Not applicable
```

## Documentation Status

## Recommended Next Release

## Completion Approval Gate

State:

> This is a candidate Final Completion Audit. The implementation agent must not declare KBDL complete. The planning agent must independently validate KBDL-011. If it passes, the project owner must explicitly accept any limitations and approve completion before the state may become COMPLETED.

## Recommended Next Action

## Progression Gate

> Do not begin implementation packages, automated validation infrastructure, production-readiness work for a coded implementation, or any later scope. Complete only KBDL-011 and return the complete evidence package so the planning agent can determine whether release readiness is allowed.
