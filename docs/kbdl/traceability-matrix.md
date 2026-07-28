# KBDL Traceability Matrix

Lifecycle status of this framework: `Approved`. Rows below reflect
KBDL-001 through KBDL-011 scope. KBDL-010 passed planning-agent validation.
KBDL-011 remains in remediation and has not passed planning-agent validation.
Implementation conformance remains `Not verified`; project completion remains
pending explicit project-owner approval.

Return to the [specification index](README.md). Status labels are defined in
[conventions.md](conventions.md#1-status-labels).

## Purpose

This matrix connects each approved blueprint concept or KBDL requirement to
its roadmap origin, its requirement ID (where assigned), its location in
the specification, its approval and validation status, and how it was or
will be validated. It is updated whenever a requirement is created, changes
status, or is validated.

Each row is presented as a list of fields rather than a single wide table
row, so it remains readable without horizontal scrolling.

## Fields

Every requirement row consists of its readable group below plus the same ID's
row in the [per-ID metadata ledger](traceability-metadata.csv). Group fields
and ledger fields are inherited together; an explicit group value overrides
only an identical ledger field. This preserves grouping while making mixed
values individually auditable. Every combined record contains:

- **Blueprint section** — The approved KBDL blueprint concept this row traces to.
- **Roadmap prompt** — The roadmap step (e.g. KBDL-001) that owns this row.
- **Requirement ID** — The requirement ID, if one has been assigned yet.
- **Specification location** — The authoritative file and section for this ID.
- **Lifecycle status** — The lifecycle/approval label from [conventions.md §1.1](conventions.md#11-lifecycle--approval-status). Only `Approved` authorizes implementation.
- **Provenance** — The authoritative origin classification; historical GOV rows use documented KBDL-001 prompt/decision evidence.
- **Validation status** — The validation label from [conventions.md §1.3](conventions.md#13-validation-status): `Verified` or `Not verified`. Independent of approval status; `Verified` never implies `Approved`, and `Approved` never implies `Verified`.
- **Authority** — The authoritative rule, adopted standard, prompt, or decision supporting lifecycle authority.
- **Validation method** — How this requirement is or will be checked (for example manual review, link check, Markdown lint).
- **Validation evidence** — A concrete pointer to the evidence (a commit SHA, a named review, a tool's output), or `Not verified` if no validation has actually been performed yet. Evidence must never be the traceability matrix pointing at itself.
- **Known limitation** — Any known gap or caveat, or `None identified`.
- **Packet or tracking destination** — `None — Approved` or the exact owning packet/tracking destination.
- **Pending dependencies** — The explicit dependency or `None`.
- **Related decision** — Decision ID from the [decision register](decision-register.md), if applicable.
- **Notes or exclusions** — Per-ID clarification, exclusion, or ledger-inheritance note.

## KBDL-001 Rows

The rows below trace KBDL-001's documentation-architecture and governance
scope.

### Project naming

- **Blueprint section:** Project naming
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-001](decision-register.md#kbdl-dec-001--project-name-is-kbdl)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review (naming decision is user-provided context, not a checkable technical claim)
- **Validation evidence:** Not verified — a naming decision has no defined validation method beyond the project owner's statement recorded in the decision register.
- **Known limitation:** None identified.
- **Related decision:** KBDL-DEC-001
- **Notes:** Naming decision, not a technical requirement.

### Specification architecture

- **Blueprint section:** Specification architecture and governance foundation
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** KBDL-GOV-001
- **Specification location:** [governance.md § KBDL-GOV-001](governance.md#kbdl-gov-001--specification-architecture-is-established)
- **Approval status:** Approved
- **Validation status:** Verified
- **Validation method:** Manual review — heading hierarchy, relative-link resolution, and heading-anchor correctness checked across all KBDL-001 files.
- **Validation evidence:** Manual review recorded in commit `2d356b4` (KBDL-001 initial commit); re-checked for this remediation in commit-to-follow (see [decision-register.md § KBDL-DEC-011](decision-register.md#kbdl-dec-011--status-model-correction-approval-vs-provenance-vs-validation)).
- **Known limitation:** No automated Markdown linter or link checker was available in this environment; verification is manual, not tool-based.
- **Related decision:** Not applicable
- **Notes:** Demonstrates the requirement-ID convention.

### Accessibility baseline protection

- **Blueprint section:** WCAG 2.2 AA baseline with enhanced motion safety (locked-rule protection)
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** KBDL-GOV-002
- **Specification location:** [governance.md § KBDL-GOV-002](governance.md#kbdl-gov-002--accessibility-requirements-are-protected)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review; no automated check is applicable yet.
- **Validation evidence:** Not verified — no `A11Y` requirement exists yet for this rule to be checked against.
- **Known limitation:** Cannot be validated against a real accessibility requirement, since none exist yet.
- **Related decision:** KBDL-DEC-010
- **Notes:** Rule takes effect once `A11Y` requirements exist in a later module.

### Documentation governance process

- **Blueprint section:** Governance and change control
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** KBDL-GOV-003
- **Specification location:** [governance.md § KBDL-GOV-003](governance.md#kbdl-gov-003--documentation-governance-process)
- **Approval status:** Approved
- **Validation status:** Verified
- **Validation method:** Manual review against this prompt's required governance topics (ownership, proposal, review, approval, scope-change, exception, deprecation, versioning, documentation-update, accessibility/motion/responsive review, conformance-review, conflict-resolution, restoration, evidence).
- **Validation evidence:** Manual review recorded in commit `2d356b4`, corrected in the remediation commit for this status-model fix.
- **Known limitation:** None identified.
- **Related decision:** Not applicable
- **Notes:** Establishes change control before design content exists.

### Visual consistency strategy

- **Blueprint section:** Visual consistency as the cross-project strategy
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-003](decision-register.md#kbdl-dec-003--visual-consistency-is-the-cross-project-strategy)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `FND`, `THM`, or `PRO` requirements exist yet to validate against.
- **Validation evidence:** Not verified.
- **Known limitation:** Will require `FND`, `THM`, `PRO` requirements in later steps before it can be validated.
- **Related decision:** KBDL-DEC-003
- **Notes:** No visual foundation requirements exist yet; out of scope for KBDL-001.

### Manual customization strategy

- **Blueprint section:** Manual, documented customization
- **Roadmap prompt:** KBDL-001
- **Related future requirement ID:** `KBDL-CUS-001` (authoritative KBDL-010 traceability appears below)
- **Specification location:** [decision-register.md § KBDL-DEC-004](decision-register.md#kbdl-dec-004--customization-is-manual-and-documented), [customization.md §1](customization.md#1-purpose-and-scope)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual record and implementation audit once a project customization exists.
- **Validation evidence:** Not verified.
- **Known limitation:** KBDL-010 requirements exist, but no project customization exists to test.
- **Related decision:** KBDL-DEC-004
- **Notes:** KBDL-010 operationalizes the KBDL-001 decision without creating a customization or approving its decision packet.

### Progressive delivery / roadmap gating

- **Blueprint section:** Progressive-system delivery
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [governance.md](governance.md)
- **Approval status:** Approved
- **Validation status:** Verified
- **Validation method:** Manual review confirming no KBDL-002+ content was introduced in this prompt or its remediation.
- **Validation evidence:** Manual scope-compliance review recorded in commit `2d356b4` and re-confirmed in the remediation commit.
- **Known limitation:** None identified.
- **Related decision:** KBDL-DEC-005
- **Notes:** Enforced by the progression gate in this prompt and in governance.md.

### Project profiles (Showcase, Precision, Flow)

- **Blueprint section:** Initial project profiles
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [README.md § Document Hierarchy](README.md#document-hierarchy)
- **Approval status:** Approved (naming only — profile design content is not approved yet)
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `PRO` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** No `PRO` requirements exist yet.
- **Related decision:** KBDL-DEC-006
- **Notes:** Only the profile names and future module location are recorded.

### Responsive web platform context

- **Blueprint section:** Responsive web as the platform context
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-007](decision-register.md#kbdl-dec-007--responsive-web-is-the-platform-context)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `RSP` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** No `RSP` requirements exist yet.
- **Related decision:** KBDL-DEC-007
- **Notes:** Out of scope for KBDL-001.

### Adaptive theme behavior

- **Blueprint section:** Adaptive light and dark theme behavior
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-008](decision-register.md#kbdl-dec-008--adaptive-light-and-dark-theme-behavior)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `THM` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** No `THM` requirements exist yet.
- **Related decision:** KBDL-DEC-008
- **Notes:** Out of scope for KBDL-001.

### Controlled expressive motion

- **Blueprint section:** Expressive but controlled motion
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-009](decision-register.md#kbdl-dec-009--expressive-but-controlled-motion)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `MOT` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** No `MOT` requirements exist yet.
- **Related decision:** KBDL-DEC-009
- **Notes:** Out of scope for KBDL-001.

### WCAG 2.2 AA baseline with enhanced motion safety

- **Blueprint section:** Accessibility and motion-safety baseline
- **Roadmap prompt:** KBDL-001
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `A11Y` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** No `A11Y` requirements exist yet.
- **Related decision:** KBDL-DEC-010
- **Notes:** Protected as a locked-rule category by KBDL-GOV-002.

### Status-model correction (this remediation)

- **Blueprint section:** Governance and change control (status semantics)
- **Roadmap prompt:** KBDL-001-R1
- **Amended requirement IDs:** KBDL-GOV-001, KBDL-GOV-003 (their authoritative occurrences remain in the KBDL-001 rows above)
- **Specification location:** [conventions.md §1](conventions.md#1-status-labels), [governance.md](governance.md), [README.md § Status Labels](README.md#status-labels)
- **Approval status:** Approved
- **Validation status:** Verified
- **Validation method:** Repository-wide grep for contradictory authority language, plus manual review of every affected file and link/anchor check.
- **Validation evidence:** Grep results before and after the correction (see the KBDL-001-R1 final report), reviewed in the remediation commit.
- **Known limitation:** None identified.
- **Related decision:** KBDL-DEC-011
- **Notes:** Corrects prior wording that treated `Confirmed`, `User-provided`, and `Verified` as implementation authority.

### Later modules (motion, responsive, accessibility, components, profiles, customization, validation)

- **Blueprint section:** Later roadmap modules
- **Roadmap prompt:** KBDL-005 through KBDL-010
- **Requirement ID:** Not assigned
- **Specification location:** Planned locations only, see [README.md § Document Hierarchy](README.md#document-hierarchy)
- **Approval status:** Deferred
- **Validation status:** Not verified
- **Validation method:** Not applicable
- **Validation evidence:** Not applicable
- **Known limitation:** Not designed; intentionally out of scope for KBDL-004 and earlier steps. Principles, Visual foundations, and Adaptive themes (formerly in this group) are now delivered — see the KBDL-002, KBDL-003, and KBDL-004 rows.
- **Related decision:** Not applicable
- **Notes:** Do not treat as implemented, approved for design content, or verified.

## KBDL-002 Rows

The rows below trace KBDL-002's identity, principles, and visual-
consistency scope, defined in [principles.md](principles.md).

### KBDL identity statement and exclusions

- **Blueprint section:** KBDL identity, personality, and explicit exclusions
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-001
- **Specification location:** [principles.md § 1](principles.md#1-identity-statement)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual design review against Section 1 at each later module's approval gate.
- **Validation evidence:** Not verified — validation method has not yet been run against a later module, since none exist yet.
- **Known limitation:** Cannot be checked against real foundation, theme, or component content until those modules exist.
- **Related decision:** Not applicable
- **Notes:** Establishes what KBDL is and explicitly is not.

### Luxury/utility conflict resolution

- **Blueprint section:** Relationship between Digital Luxury and Technical Utility
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-002
- **Specification location:** [principles.md § 4](principles.md#4-relationship-between-luxury-and-utility)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review of design decisions against the priority order.
- **Validation evidence:** Not verified.
- **Known limitation:** No real design decisions exist yet to test the priority order against.
- **Related decision:** Not applicable
- **Notes:** Includes five worked conflict examples.

### Core principles

- **Blueprint section:** Core enforceable design principles
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-003
- **Specification location:** [principles.md § 6](principles.md#6-core-principles)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review confirming all nine principles include every required field (normative statement, purpose, required/prohibited behavior, profile interpretation, accessibility/responsive/motion implications, review questions) and that the nine required concepts (clarity before spectacle, precision, comprehension, hierarchy, controlled expression, consistency, adaptability, accessibility by default, performance) are all present.
- **Validation evidence:** Not verified — the requirement's later-module approval-gate method has not been executed completely.
- **Known limitation:** Complete evidence across every later module is unavailable.
- **Related decision:** Not applicable
- **Notes:** Nine principles defined (blueprint required six to nine).

### Visual-consistency relationships

- **Blueprint section:** Cross-project visual consistency
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-004
- **Specification location:** [principles.md § 7](principles.md#7-visual-consistency)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual cross-reference review once foundation, theme, and responsive modules are approved.
- **Validation evidence:** Not verified — dependent modules do not exist yet.
- **Known limitation:** Cannot be fully validated until `FND`, `THM`, and `RSP` requirements exist.
- **Related decision:** KBDL-DEC-003
- **Notes:** Defines relationships only; no final values.

### Locked, controlled, and open identity model

- **Blueprint section:** Stable and variable identity elements
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-005
- **Specification location:** [principles.md § 5](principles.md#5-stable-and-variable-identity-elements)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review confirming all three categories (locked, controlled, open) address every element listed in this prompt's scope, and that no final ranges or values were introduced.
- **Validation evidence:** Not verified — the requirement's full later-module and implementation review has not been executed.
- **Known limitation:** Controlled-variable ranges are intentionally undefined pending later modules.
- **Related decision:** Not applicable
- **Notes:** Ties directly to [governance.md § Exception process](governance.md#exception-process).

### Design-decision hierarchy

- **Blueprint section:** Design-decision hierarchy and conflict handling
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-006
- **Specification location:** [principles.md § 8](principles.md#8-design-decision-hierarchy)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review of decision records against the hierarchy; conflicts escalated per governance's conflict-resolution process.
- **Validation evidence:** Not verified — no real design decision has been escalated through this hierarchy yet.
- **Known limitation:** None identified.
- **Related decision:** Not applicable
- **Notes:** Aligns with [governance.md § Conflict-resolution process](governance.md#conflict-resolution-process).

### Profile-level interpretation (Showcase, Precision, Flow)

- **Blueprint section:** Profile-level interpretation of shared principles
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-007
- **Specification location:** [principles.md § 9](principles.md#9-profile-level-interpretation)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual cross-profile consistency review once the project-profiles module is approved.
- **Validation evidence:** Not verified — the project-profiles module (`PRO`) does not exist yet.
- **Known limitation:** Cannot be fully validated until `PRO` requirements exist.
- **Related decision:** KBDL-DEC-006
- **Notes:** Confirms Showcase, Precision, and Flow share all locked rules and principles.

### Conforming and non-conforming design directions

- **Blueprint section:** Conceptual examples distinguishing conformance from non-conformance
- **Roadmap prompt:** KBDL-002
- **Requirement ID:** KBDL-PRN-008
- **Specification location:** [principles.md § 10](principles.md#10-conforming-design-directions), [principles.md § 11](principles.md#11-non-conforming-design-directions)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual count and coverage review confirming at least six conforming examples spanning all three profiles, both themes, an expressive moment, a repeated workflow, and a mobile context; and at least eight non-conforming patterns each with reason, broken principle, risk, and correction.
- **Validation evidence:** Not verified — example-count evidence does not execute the requirement's later-module conformance-review method.
- **Known limitation:** Examples are conceptual; no mockups or token values exist to check them against yet.
- **Related decision:** Not applicable
- **Notes:** Sixteen non-conforming patterns exceed the required minimum of eight.

## KBDL-003 Rows

The rows below trace KBDL-003's visual-foundation scope, defined in
[foundations/README.md](foundations/README.md) and its linked documents.
Each `KBDL-FND-###` requirement's full lifecycle/provenance/validation
detail lives in [foundations/README.md § Normative Requirements](foundations/README.md#7-normative-requirements);
this matrix records only its blueprint origin, approval status, validation
status, and evidence, per this file's field definitions.

### Color role architecture (KBDL-FND-001, KBDL-FND-002)

- **Blueprint section:** Color architecture — semantic roles and color-
  only-meaning prohibition
- **Roadmap prompt:** KBDL-003
- **Requirement ID:** KBDL-FND-001, KBDL-FND-002
- **Specification location:** [foundations/color.md §1–§2](foundations/color.md#1-architectural-principles-approved)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review of role names and color-only-meaning usage at each later module's approval gate.
- **Validation evidence:** Not verified — no theme or component content exists yet to check role usage against.
- **Known limitation:** Cannot be fully validated until `THM` and `CMP` requirements exist.
- **Related decision:** Not applicable
- **Notes:** Architecture only; recommended hue values are tracked separately below (KBDL-FND-009).

### Spacing rhythm and responsive content priority (KBDL-FND-003, KBDL-FND-004)

- **Blueprint section:** Spacing rhythm and content-driven breakpoints
- **Roadmap prompt:** KBDL-003
- **Requirement ID:** KBDL-FND-003, KBDL-FND-004
- **Specification location:** [foundations/spacing-layout.md §1, §3](foundations/spacing-layout.md#1-spacing-and-sizing-logic)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review of spacing usage and breakpoint justification once `RSP` requirements exist.
- **Validation evidence:** Not verified — no responsive-behavior module exists yet.
- **Known limitation:** Cannot be fully validated until `RSP` requirements exist.
- **Related decision:** KBDL-DEC-003, KBDL-DEC-007
- **Notes:** Restates locked rules from [principles.md §5.1](principles.md#51-locked-identity-rules) at foundation-level specificity.

### Elevation and icon/media accessibility anticipation (KBDL-FND-005, KBDL-FND-006, KBDL-FND-007)

- **Blueprint section:** Depth semantics; icon and media accessibility anticipation
- **Roadmap prompt:** KBDL-003
- **Requirement ID:** KBDL-FND-005, KBDL-FND-006, KBDL-FND-007
- **Specification location:** [foundations/shape-depth.md §3](foundations/shape-depth.md#3-elevation-and-depth), [foundations/iconography-media.md §1.1, §2.1](foundations/iconography-media.md#1-iconography)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review confirming each elevation level states a simplified fallback, and that icon/media required principles explicitly state the state-clarity and reduced-motion anticipation rules.
- **Validation evidence:** Manual completeness review recorded in the KBDL-003 commit — confirmed all five elevation levels list a non-shadow-dependent fallback, and both icon and media sections state their respective anticipation requirements.
- **Known limitation:** None identified.
- **Related decision:** Not applicable
- **Notes:** "Anticipation" language is intentional — full reduced-motion and accessibility markup rules belong to KBDL-005/006.

### Shared foundation architecture across profiles (KBDL-FND-008)

- **Blueprint section:** Profile-level foundation adjustments
- **Roadmap prompt:** KBDL-003
- **Requirement ID:** KBDL-FND-008
- **Specification location:** [foundations/README.md §4](foundations/README.md#4-project-profile-adjustments--foundation-summary)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual cross-profile consistency review once the project-profiles module (`PRO`) is approved.
- **Validation evidence:** Not verified — `PRO` requirements do not exist yet.
- **Known limitation:** Cannot be fully validated until `PRO` requirements exist.
- **Related decision:** KBDL-DEC-006
- **Notes:** Restates [principles.md §9.4](principles.md#94-shared-constraints-across-profiles) at foundation-level specificity.

### Approved color, typography, spacing, and shape/elevation defaults (KBDL-FND-009 through KBDL-FND-012)

- **Blueprint section:** Foundation decision packet — default values
- **Roadmap prompt:** KBDL-003 (approved via project-owner review following KBDL-003-R1)
- **Requirement ID:** KBDL-FND-009, KBDL-FND-010, KBDL-FND-011, KBDL-FND-012
- **Specification location:** [foundations/README.md §6](foundations/README.md#6-foundation-decision-packet)
- **Approval status:** Approved — the project owner approved all eleven recommended defaults in full, with no changes, per [KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved)
- **Validation status:** Mixed — Verified / Not verified: KBDL-FND-009; Not verified: KBDL-FND-010, KBDL-FND-011, KBDL-FND-012
- **Validation method:** WCAG relative-luminance contrast calculation (completed for the color pairs listed); project-owner review (completed — see KBDL-DEC-012); typeface-licensing verification (not yet performed, applies to a future specific font-family decision).
- **Validation evidence:** Contrast-ratio table in [foundations/color.md §4](foundations/color.md#4-contrast-evidence-illustrative-not-a-theme-mapping), computed via a local dependency-free script (see the KBDL-003 validation evidence for the script and full output). Updated under KBDL-003-R1: `neutral-50` (3.25:1) was found to fail the 4.5:1 normal-text threshold and is now restricted to large-text/non-text-UI/decorative use only; a new `neutral-60` (5.59:1) was added and verified as the safe value for normal-sized secondary/tertiary text.
- **Known limitation:** Approval authorizes these defaults for implementation; it does not itself constitute rendering, brand-suitability, or licensing validation — those remain `Not verified` as noted above.
- **Related decision:** KBDL-DEC-012
- **Notes:** This row's approval status changed from `Recommended` to `Approved` following the project owner's decision recorded in KBDL-DEC-012. See KBDL-003-R1 for the accessibility and lifecycle corrections applied to this row's underlying content before approval.

## KBDL-004 Rows

The rows below trace KBDL-004's adaptive-theme scope, defined in
[themes/README.md](themes/README.md) and its linked documents.

### Theme architecture, terminology, and semantic-role inventory (KBDL-THM-001)

- **Blueprint section:** Theme architecture and semantic-role inventory
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-001
- **Specification location:** [themes/semantic-roles.md §1](themes/semantic-roles.md#1-semantic-role-inventory)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Manual review of role usage against the inventory at each later module's approval gate.
- **Validation evidence:** Not verified — no component module exists yet to check role usage against.
- **Known limitation:** Cannot be fully validated until component modules (`CMP`) exist.
- **Related decision:** Not applicable
- **Notes:** Restates the color-role architecture from `KBDL-FND-001`/`002` at theme-level specificity; 72 distinct semantic roles across 6 categories.

### Semantic parity (KBDL-THM-002)

- **Blueprint section:** Light/dark theme parity
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-002
- **Specification location:** [themes/semantic-roles.md §2](themes/semantic-roles.md#2-semantic-parity)
- **Approval status:** Approved
- **Validation status:** Verified
- **Validation method:** Direct count of every role in the inventory against the actual light and dark mapping tables (re-run under KBDL-004-R1 and again under KBDL-004-R3, not a re-assertion of the prior report each time).
- **Validation evidence:** Parity matrix in [themes/semantic-roles.md § Parity Matrix](themes/semantic-roles.md#parity-matrix-corrected-under-kbdl-004-r1) — 72 unique roles, 72 light mappings, 72 dark mappings, **1** role-level alias (corrected under KBDL-004-R3, previously miscounted as 2), 0 unresolved; recorded in the KBDL-004-R3 commit. The KBDL-004-R1 re-run found and fixed a real table-formatting defect (an inserted paragraph had broken the Status Families table in `light-theme.md §5`, orphaning its "Neutral status" row).
- **Known limitation:** None identified.
- **Related decision:** Not applicable
- **Notes:** The category-label wording error ("×5 sub-roles ×5 families") in the original parity matrix — which contradicted its own correct 4×6=24 total — is corrected under KBDL-004-R1; the total of 72 was independently re-verified, not merely preserved. Under KBDL-004-R2, the alias *definition* was reconciled to one model across all documents: an alias is a role with no separate definition of its own; a role whose *value* merely reuses (or, for Keyboard focus, is required to equal) another role's color is not an alias. However, the KBDL-004-R2 pass still classified **Keyboard focus** as an alias while simultaneously counting it among the Actions category's 10 distinct roles — an internal contradiction, since an aliased role contributes 0 to a distinct-role count, not 1. **KBDL-004-R3 resolves this**: Keyboard focus is now consistently classified as a distinct role (value/behavior equivalence with Focus indicator, not aliasing), leaving **Neutral status as the only true alias**. The unique-role, light-mapping, and dark-mapping totals are unchanged (72/72/72); only the alias total changes, from the previously irreproducible "2" to the correct **1**.

### Theme selection precedence — approved core (KBDL-THM-003, narrowed under KBDL-004-R1)

- **Blueprint section:** Theme-selection precedence — explicit-choice-over-system-preference core
- **Roadmap prompt:** KBDL-004 (narrowed KBDL-004-R1)
- **Requirement ID:** KBDL-THM-003
- **Specification location:** [themes/README.md §5](themes/README.md#5-theme-selection-precedence)
- **Approval status:** Approved — directly and explicitly stated in the KBDL-004 preconditions (explicit user choice outranks system preference; system preference used only absent an explicit choice)
- **Validation status:** Not verified
- **Validation method:** Manual review of precedence logic once implemented.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Cannot be validated until an implementation exists.
- **Related decision:** Not applicable
- **Notes:** Narrowed under KBDL-004-R1; the full six-level ordering was found to exceed what any prior decision explicitly supports and moved to `KBDL-THM-013` (Recommended, see below).

### Detailed selection-precedence ordering (KBDL-THM-013, new under KBDL-004-R1)

- **Blueprint section:** Full six-level theme-selection precedence ordering
- **Roadmap prompt:** KBDL-004-R1
- **Requirement ID:** KBDL-THM-013
- **Specification location:** [themes/README.md §5](themes/README.md#5-theme-selection-precedence)
- **Approval status:** Approved — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
- **Validation status:** Not verified
- **Validation method:** Manual review of the full precedence flow once implemented; project-owner review (performed for approval scope, not for implementation).
- **Validation evidence:** Not verified — approval is a lifecycle decision, not validation evidence.
- **Known limitation:** Cannot be validated until an implementation exists.
- **Related decision:** KBDL-DEC-013
- **Notes:** Split out of the original `KBDL-THM-003` during KBDL-004-R1 because only two of the six levels are directly pre-approved; the full six-level ordering was approved under KBDL-004-A1.

### Persistence baseline (KBDL-THM-004, reclassified under KBDL-004-R1)

- **Blueprint section:** Theme preference persistence baseline
- **Roadmap prompt:** KBDL-004 (reclassified KBDL-004-R1)
- **Requirement ID:** KBDL-THM-004
- **Specification location:** [themes/README.md §7](themes/README.md#7-persistence-guidance)
- **Approval status:** Approved — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
- **Validation status:** Not verified
- **Validation method:** Manual review of persistence design once implemented; project-owner review (performed for approval scope).
- **Validation evidence:** Not verified — no implementation exists yet; approval is a lifecycle decision, not validation evidence.
- **Known limitation:** Cannot be validated until an implementation exists.
- **Related decision:** KBDL-DEC-013
- **Notes:** Previously mislabeled `Approved`, then corrected to `Recommended` under KBDL-004-R1; approved for real under KBDL-004-A1.

### Accessibility-preserving override core (KBDL-THM-005, narrowed) and profile sharing (KBDL-THM-006)

- **Blueprint section:** Accessibility cannot be weakened by a project theme override; shared theme architecture across profiles
- **Roadmap prompt:** KBDL-004 (narrowed KBDL-004-R1)
- **Requirement ID:** KBDL-THM-005, KBDL-THM-006
- **Specification location:** [themes/adaptation.md §1.2](themes/adaptation.md#12-projects-must-not), [themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation)
- **Approval status:** Approved — `KBDL-THM-005` narrowed to only the accessibility-non-weakening core, directly derived from the locked `KBDL-GOV-002` rule; `KBDL-THM-006` unchanged
- **Validation status:** Not verified
- **Validation method:** Manual review of any project theme against the documented boundaries; manual cross-profile review once the project-profiles module is approved.
- **Validation evidence:** Not verified — no project theme or `PRO` module exists yet.
- **Known limitation:** Cannot be fully validated until `PRO` requirements exist.
- **Related decision:** KBDL-DEC-006
- **Notes:** `KBDL-THM-005`'s detailed permitted-override list moved to `KBDL-THM-014` (Recommended, see below); `KBDL-THM-006` restates `KBDL-FND-008` at theme-level specificity, unchanged.

### Detailed project-override list (KBDL-THM-014, new under KBDL-004-R1)

- **Blueprint section:** Detailed permitted project-override list and documentation requirement
- **Roadmap prompt:** KBDL-004-R1
- **Requirement ID:** KBDL-THM-014
- **Specification location:** [themes/adaptation.md §1.1, §1.3](themes/adaptation.md#1-project-controlled-adaptation)
- **Approval status:** Approved — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
- **Validation status:** Not verified
- **Validation method:** Manual review of the override list once a project theme exists; project-owner review (performed for approval scope).
- **Validation evidence:** Not verified — approval is a lifecycle decision, not validation evidence.
- **Known limitation:** Cannot be validated until a project theme exists.
- **Related decision:** KBDL-DEC-013
- **Notes:** Split out of the original `KBDL-THM-005` during KBDL-004-R1; approved under KBDL-004-A1.

### Local contrast contexts (KBDL-THM-015, new under KBDL-004-R1)

- **Blueprint section:** Named local-contrast-context set and nesting rules
- **Roadmap prompt:** KBDL-004-R1
- **Requirement ID:** KBDL-THM-015
- **Specification location:** [themes/adaptation.md §2](themes/adaptation.md#2-local-contrast-contexts)
- **Approval status:** Approved — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
- **Validation status:** Not verified
- **Validation method:** Manual review of context usage against the defined set and rules once implemented; project-owner review (performed for approval scope).
- **Validation evidence:** Not verified — approval is a lifecycle decision, not validation evidence.
- **Known limitation:** Cannot be validated until an implementation exists.
- **Related decision:** KBDL-DEC-013
- **Notes:** No prior KBDL decision defines local contrast contexts; this new KBDL-004-R1 architecture was approved under KBDL-004-A1.

### Recommended light and dark theme mappings (KBDL-THM-007, KBDL-THM-008)

- **Blueprint section:** Light and dark theme semantic mappings
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-007, KBDL-THM-008
- **Specification location:** [themes/light-theme.md §1–§7](themes/light-theme.md#1-canvas-and-surfaces), [themes/dark-theme.md §1–§8](themes/dark-theme.md#1-elevation-strategy)
- **Approval status:** Approved for the **opaque semantic mappings only** — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved); Accent-surface, Scrim, and Selection-background opacity remain `Recommended` and are explicitly excluded from this approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status)
- **Validation status:** Mixed — Verified / Not verified
- **Validation method:** WCAG relative-luminance contrast calculation via a local dependency-free script (completed for opaque pairs); project-owner review (performed for approval scope, per KBDL-DEC-013).
- **Validation evidence:** [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence) — 52 pairs tested, all opaque, all passing their applicable threshold except 4 explicitly decorative-exempt borders/gridlines. The two Informational failures identified in the original KBDL-004 report (3.78:1, 4.21:1) are resolved by a revised hue (`#164499`) for the Text/Icon/Border/Strong-surface roles, with `neutral-10` correctly retained for On-strong-surface content (role assignment corrected under KBDL-004-R2) — see [adaptation.md §5.2](themes/adaptation.md#52-informational-correction-kbdl-004-r1). The Media caption row was corrected under KBDL-004-R2 to describe a fully opaque `neutral-100` band (17.17:1 is directly correct for this pair, not inherited or assumed).
- **Known limitation:** Approval covers the opaque mappings only; opacity values must not be treated as `Approved` or implemented until a future decision addresses them. The dark theme was independently designed, not inverted from light — see [dark-theme.md § Design Strategy](themes/dark-theme.md#design-strategy--why-some-roles-use-a-different-step-than-light-mode) for the `neutral-60`/`neutral-50` asymmetry this produced. Translucent opacity values remain entirely out of scope for this row.
- **Related decision:** KBDL-DEC-013 (opaque mappings only)
- **Notes:** Uses only already-`Approved` KBDL-003 foundation colors (`neutral-*`, `accent-30`/`accent-50`); no new primitive hues were introduced for the light/dark base mapping.

### Status-family theme values, gradient strategy, and color-value expression (KBDL-THM-009, KBDL-THM-010, KBDL-THM-011)

- **Blueprint section:** Status-family theme colors; gradient strategy; color-value expression convention
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-009, KBDL-THM-010, KBDL-THM-011
- **Specification location:** [themes/adaptation.md §5, §4, §6](themes/adaptation.md#5-status-family-theme-behavior)
- **Approval status:** Approved — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved); `KBDL-THM-010`'s approval is scoped to the **opaque** gradient caption-band strategy only, any translucent variant remains `Recommended`/`Not verified` (extends the still-pending [color.md §3.3–§3.5](foundations/color.md#33-supporting-status-families) recommendations)
- **Validation status:** Mixed — Verified / Not verified: KBDL-THM-009, KBDL-THM-010; Not applicable: KBDL-THM-011
- **Validation method:** WCAG contrast calculation (completed for status pairs and the opaque gradient caption substitute); manual review (color-expression, performed for approval scope).
- **Validation evidence:** [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence) for the recalculated pairs and [themes/adaptation.md §5.2](themes/adaptation.md#52-informational-correction-kbdl-004-r1) for the Informational correction record. [themes/adaptation.md §4.3](themes/adaptation.md#43-worked-example--worst-case-contrast-corrected-kbdl-004-r1) documents both gradient endpoints tested against both candidate text colors and the corrected, fully-opaque caption-band resolution (KBDL-004-R2).
- **Known limitation:** New dark-mode status hues (`#7CC4FF`, `#6FD19A`, `#E0A840`, `#FF8A80`) were introduced here since the light-mode-only values from KBDL-003 fail contrast against a dark canvas; these dark hues, along with the light-mode Informational value revised to `#164499` under KBDL-004-R1, are now `Approved` as part of the theme layer under KBDL-004-A1 (its correct role assignment — `#164499` for Text/Icon/Border/Strong-surface, `neutral-10` for On-strong-surface content — was clarified under KBDL-004-R2). Any translucent caption-band variant remains outside this row's approved scope.
- **Related decision:** KBDL-DEC-013
- **Notes:** Corrected under KBDL-004-R1: Informational no longer carries a large-text/icon restriction — the revised hue passes 4.5:1 in every context this family is used, in both modes. Corrected under KBDL-004-R2: the gradient caption-band example is now explicitly opaque, and Informational's role assignment is stated precisely.

### Theme-transition guidance (KBDL-THM-012, KBDL-THM-012a)

- **Blueprint section:** Theme-transition guidance (conceptual, no timing/easing); reduced-motion requirement
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-012, KBDL-THM-012a
- **Specification location:** [themes/adaptation.md §7](themes/adaptation.md#7-theme-transition-guidance)
- **Approval status:** `KBDL-THM-012` Approved for its **conceptual** guidance only, per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved); `KBDL-THM-012a` (reduced-motion) Approved — split under KBDL-004-R1 to resolve a contradiction where the document header previously claimed §7's "requirements" were `Approved` while §7's own status line said `Recommended`
- **Validation status:** Not verified
- **Validation method:** Manual review confirming no timing/easing values were introduced (performed); manual review confirming reduced-motion behavior once implemented.
- **Validation evidence:** Manual scope-compliance review recorded in the KBDL-004 commit — confirmed zero millisecond/easing values anywhere in `docs/kbdl/themes/`.
- **Known limitation:** Exact timing/easing depends entirely on KBDL-005, which is eligible for its own future prompt and has not been started by this approval.
- **Related decision:** KBDL-DEC-013 (for `KBDL-THM-012`'s conceptual approval); KBDL-DEC-010 (for `KBDL-THM-012a`'s reduced-motion basis)
- **Notes:** Explicitly defers all durations and easing curves to Motion (KBDL-005). The lifecycle contradiction identified in KBDL-004 validation is resolved by this split.

## KBDL-005 — Motion

### Motion purpose, terminology, and conflict resolution (KBDL-MOT-001, KBDL-MOT-002, KBDL-MOT-003)

- **Blueprint section:** Motion purpose requirement; motion terminology; expressive-versus-usability conflict resolution
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-001, KBDL-MOT-002, KBDL-MOT-003
- **Specification location:** [motion/README.md §2, §3.3](motion/README.md#2-motion-terminology), [motion/foundations.md §1](motion/foundations.md#1-motion-purposes)
- **Approval status:** Approved — directly restates the locked Motion Purpose rule and `KBDL-PRN-002`/`KBDL-PRN-003`
- **Validation status:** Not verified
- **Validation method:** Manual review confirming every documented pattern cites an approved purpose; manual terminology-consistency review (performed).
- **Validation evidence:** Manual review recorded in [motion/validation.md §6](motion/validation.md#6-manual-documentation-reviews-performed).
- **Known limitation:** Per-component purpose assignment depends on the Components module (`CMP`), not yet reached.
- **Related decision:** Not applicable
- **Notes:** These three requirements restate already-`Approved` KBDL-002 principles at motion-specific granularity; no new policy is introduced.

### Motion category and hierarchy structure (KBDL-MOT-004, KBDL-MOT-005, KBDL-MOT-006)

- **Blueprint section:** Ten motion categories; five-level motion hierarchy; multi-factor intensity model
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-004, KBDL-MOT-005, KBDL-MOT-006
- **Specification location:** [motion/foundations.md §2, §3, §4](motion/foundations.md#2-motion-categories)
- **Approval status:** All three Approved — `KBDL-MOT-004` as a structural completeness requirement (unaffected by this decision); `KBDL-MOT-005` and `KBDL-MOT-006` per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (decision packet items 1 and 14)
- **Validation status:** Not verified
- **Validation method:** Manual completeness review per category (performed); project-owner review of the hierarchy/intensity model (performed, see KBDL-DEC-014).
- **Validation evidence:** Manual review recorded in [motion/validation.md §1](motion/validation.md#1-motion-validation-specification).
- **Known limitation:** Exceptional-level (Level 4) usage requires project-owner review each time; not yet exercised, since no implementation exists.
- **Related decision:** [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved). `KBDL-MOT-005` maps to [motion decision packet](motion/README.md#10-motion-decision-packet) item 1; `KBDL-MOT-006` maps to item 14 (added under KBDL-005-R2, which corrected the packet's initial omission of this requirement; approved under KBDL-005-A1).
- **Notes:** The requirement that categories be documented completely is itself already supported by KBDL-002's visual-consistency principle; the specific five-level names and intensity factors are new.

### Timing, duration, and easing architecture (KBDL-MOT-007, KBDL-MOT-008, KBDL-MOT-009)

- **Blueprint section:** Semantic timing classes; duration recommendations; easing categories and exact curves
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-007, KBDL-MOT-008, KBDL-MOT-009
- **Specification location:** [motion/timing-easing.md §1, §2, §3](motion/timing-easing.md#1-timing-architecture)
- **Approval status:** Approved — per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved), per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status)
- **Validation status:** Not verified: KBDL-MOT-007; Not applicable: KBDL-MOT-008, KBDL-MOT-009
- **Validation method:** Manual internal-consistency review (performed, see [motion/validation.md §2](motion/validation.md#2-numerical-consistency-review-performed)); project-owner review (performed, see KBDL-DEC-014); implementation-level review once an implementation exists.
- **Validation evidence:** [motion/validation.md §2](motion/validation.md#2-numerical-consistency-review-performed) — every value has a stated purpose, exit durations are equal to or shorter than paired entrances, and no value is marked `Verified` without implementation evidence.
- **Known limitation:** Approval is a lifecycle decision, not implementation validation; these values must not be treated as `Verified` until an implementation exists and is measured.
- **Related decision:** [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved). `KBDL-MOT-007` and `KBDL-MOT-008` together map to [motion decision packet](motion/README.md#10-motion-decision-packet) item 2 (one timing system); `KBDL-MOT-009` maps to item 3.
- **Notes:** Resolves the exact timing/easing KBDL-004 explicitly deferred (`KBDL-THM-012`); no CSS, JSON, or animation-library format is introduced.

### Spatial movement and choreography (KBDL-MOT-010, KBDL-MOT-011, KBDL-MOT-012)

- **Blueprint section:** Spatial-movement constraints; choreography and sequencing; entrance/exit behavior
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-010, KBDL-MOT-011, KBDL-MOT-012
- **Specification location:** [motion/foundations.md §6, §5, §7](motion/foundations.md#6-spatial-movement)
- **Approval status:** All three Approved — `KBDL-MOT-010` and `KBDL-MOT-011` per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (decision packet items 4 and 5); `KBDL-MOT-012` directly restates the safety/correctness priority already in `KBDL-PRN-002`, unaffected by this decision
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner review of `KBDL-MOT-010`/`011` (performed, see KBDL-DEC-014).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Exact pixel/percentage movement and scale values are deferred to the Components module.
- **Related decision:** [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (for `KBDL-MOT-010`/`011`)
- **Notes:** The individual safety-relevant constraints (e.g., destructive actions must not rely on exit animation as confirmation) restate existing approved priorities; the consolidated spatial/choreography architecture is new.

### Interaction-category motion rules (KBDL-MOT-013 through KBDL-MOT-019)

- **Blueprint section:** Navigation continuity; loading/progress; direct manipulation; attention motion; ambient/continuous motion; scroll-linked motion; media motion
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-013, KBDL-MOT-014, KBDL-MOT-015, KBDL-MOT-016, KBDL-MOT-017, KBDL-MOT-018, KBDL-MOT-019
- **Specification location:** [motion/patterns.md §1–§7](motion/patterns.md#1-navigation-and-spatial-continuity)
- **Approval status:** All seven Approved — `KBDL-MOT-013` per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (decision packet item 15); `KBDL-MOT-014`, `KBDL-MOT-015`, `KBDL-MOT-016`, `KBDL-MOT-017`, `KBDL-MOT-018`, `KBDL-MOT-019` each directly restate an already-approved Technical Utility quality, accessibility requirement, locked component-state-clarity rule, or `KBDL-DEC-010` (WCAG 2.2 AA baseline), unaffected by this decision
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner review of `KBDL-MOT-013` (performed, see KBDL-DEC-014).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Exact repetition limits (attention motion) and scroll thresholds remain qualitative pending implementation-level review.
- **Related decision:** `KBDL-DEC-010` (for the media-motion autoplay prohibition and WCAG 2.2 AA baseline); [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (for `KBDL-MOT-013`)
- **Notes:** The bounded-repetition limit for attention motion (2–3 repetitions, `KBDL-MOT-029`) is Approved per KBDL-DEC-014, decision packet item 7. `KBDL-MOT-013` maps to [motion decision packet](motion/README.md#10-motion-decision-packet) item 15 (added under KBDL-005-R2, which corrected the packet's initial omission of this requirement; approved under KBDL-005-A1).

### Theme-transition motion (KBDL-MOT-020)

- **Blueprint section:** Concrete duration/easing for the KBDL-004 theme-transition rules
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-020
- **Specification location:** [motion/patterns.md §8](motion/patterns.md#8-theme-transition-motion)
- **Approval status:** Approved — per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (decision packet item 10); the underlying non-blocking, readable, focus-preserving requirements were already `Approved` under `KBDL-THM-012`/`KBDL-THM-012a` and are unaffected either way
- **Validation status:** Not verified
- **Validation method:** Manual review of the worked example (performed); project-owner review (performed, see KBDL-DEC-014).
- **Validation evidence:** [motion/patterns.md §8](motion/patterns.md#8-theme-transition-motion) — conceptually verified against the already-`Verified` opaque contrast pair (17.17:1, unrelated example) and the KBDL-004 non-blocking/readability requirements; no live implementation has been rendered or measured.
- **Known limitation:** No intermediate-frame contrast measurement has actually been performed against a live implementation.
- **Related decision:** [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).
- **Notes:** This is the exact item KBDL-004's `KBDL-THM-012a` note deferred to KBDL-005; it does not reopen any approved KBDL-004 theme mapping.

### Interruption, recovery, and accessibility/performance requirements (KBDL-MOT-021 through KBDL-MOT-027)

- **Blueprint section:** Interruption/reversal/recovery; reduced-motion and no-motion parity; motion safety; performance requirements; mobile/input-method considerations; profile consistency; approval-gate governance
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-021, KBDL-MOT-022, KBDL-MOT-023, KBDL-MOT-024, KBDL-MOT-025, KBDL-MOT-026, KBDL-MOT-027
- **Specification location:** [motion/patterns.md §9](motion/patterns.md#9-interruption-reversal-and-recovery), [motion/accessibility-performance.md §1–§4](motion/accessibility-performance.md#1-reduced-motion-and-no-motion-parity), [motion/README.md §10](motion/README.md#10-motion-decision-packet)
- **Approval status:** Approved for all seven — each directly restates an already-approved safety/correctness priority, `KBDL-THM-012a` (reduced motion), `KBDL-DEC-010` (motion-safety baseline), Performance-Aware Enhancement (`KBDL-PRN-003`), Accessibility by Default, `KBDL-PRN-007` (profile consistency), or [conventions.md §1.1](conventions.md#11-lifecycle--approval-status) itself
- **Validation status:** Not verified: KBDL-MOT-021, KBDL-MOT-022, KBDL-MOT-023, KBDL-MOT-024, KBDL-MOT-025, KBDL-MOT-026; Not applicable: KBDL-MOT-027
- **Validation method:** Manual parity/safety/performance review performed conceptually (see [motion/validation.md §3, §4](motion/validation.md#3-reduced-motion-matrix-review-performed)); implementation-level measurement not yet performed.
- **Validation evidence:** [motion/validation.md §3](motion/validation.md#3-reduced-motion-matrix-review-performed) (reduced-motion parity, passed) and [motion/validation.md §4](motion/validation.md#4-pattern-coverage-review-performed) (pattern coverage, passed).
- **Known limitation:** No implementation exists to measure actual frame rate, input latency, or cross-input-method behavior.
- **Related decision:** `KBDL-THM-012a`, `KBDL-DEC-010`
- **Notes:** These seven requirements collectively ensure no motion default introduced by this module bypasses KBDL's existing accessibility, safety, performance, or approval-governance baseline.

### Detailed motion defaults separated from their approved cores (KBDL-MOT-028 through KBDL-MOT-034)

- **Blueprint section:** Entrance-versus-exit duration relationship; attention repetition default; detailed ambient-motion boundaries; detailed scroll-linked-motion boundaries; reduced-motion substitution matrix; conceptual motion-token naming architecture; profile-level motion-intensity adjustments
- **Roadmap prompt:** KBDL-005-R1 (added during remediation to separate new KBDL-005 policy that was previously bundled inside an Approved core requirement's section without its own lifecycle record)
- **Requirement ID:** KBDL-MOT-028, KBDL-MOT-029, KBDL-MOT-030, KBDL-MOT-031, KBDL-MOT-032, KBDL-MOT-033, KBDL-MOT-034
- **Specification location:** [motion/foundations.md §7](motion/foundations.md#7-entrance-and-exit-behavior), [motion/patterns.md §4, §5, §6, §10](motion/patterns.md#4-attention-motion), [motion/accessibility-performance.md §1.4](motion/accessibility-performance.md#14-per-category-parity-matrix), [motion/timing-easing.md §4](motion/timing-easing.md#4-conceptual-motion-tokens)
- **Approval status:** All seven Approved — per [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved) (decision packet items 6, 7, 8, 9, 11, 12, and 13 respectively); each remains distinct from its already-`Approved` parent core (`KBDL-MOT-012`, `KBDL-MOT-016`, `KBDL-MOT-017`, `KBDL-MOT-018`, `KBDL-MOT-022`, and `KBDL-MOT-026` respectively; `KBDL-MOT-033` has no prior parent, since no earlier decision defines motion tokens)
- **Validation status:** Not applicable: KBDL-MOT-028, KBDL-MOT-029, KBDL-MOT-032, KBDL-MOT-033; Not verified: KBDL-MOT-030, KBDL-MOT-031, KBDL-MOT-034
- **Validation method:** Manual review once implemented; project-owner review via the [motion decision packet](motion/README.md#10-motion-decision-packet) (performed, see KBDL-DEC-014, items 6–9 and 11–13).
- **Validation evidence:** Not verified — no implementation exists yet; conceptual manual review recorded in [motion/validation.md](motion/validation.md) where applicable.
- **Known limitation:** Approval is a lifecycle decision, not implementation validation; these values must not be treated as `Verified` until an implementation exists and is measured.
- **Related decision:** [KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).
- **Notes:** Splitting these out does not change any duration value, curve, movement range, hierarchy level, safety behavior, reduced-motion behavior, or profile recommendation — only the lifecycle bookkeeping.

## KBDL-006 — Responsive and Accessibility

### Responsive-content priority, source/reading order, and reflow core (KBDL-RSP-001, KBDL-RSP-006, KBDL-RSP-007, KBDL-RSP-015, KBDL-RSP-016, KBDL-RSP-020)

- **Blueprint section:** Responsive-content priority; layout reflow; source/reading order; orientation; zoom and enlarged text; responsive focus management
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-RSP-001, KBDL-RSP-006, KBDL-RSP-007, KBDL-RSP-015, KBDL-RSP-016, KBDL-RSP-020
- **Specification location:** [responsive.md §4, §11, §12, §20, §21, §25](responsive.md#4-responsive-content-priority)
- **Approval status:** Approved — each directly restates the locked responsive-content-priority rule (`principles.md §5.1`) or a WCAG 2.2 Level A/AA criterion (SC 1.4.10, SC 1.3.2, SC 2.4.3, SC 1.3.4, SC 1.4.4) already adopted under `KBDL-DEC-010`
- **Validation status:** Not verified
- **Validation method:** Manual reflow/zoom/orientation/order testing once an implementation exists.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent; cannot be tested until a real layout exists.
- **Related decision:** `KBDL-DEC-010` (WCAG 2.2 AA baseline).
- **Notes:** These six requirements restate already-approved principles or WCAG criteria at responsive-specific granularity; no new policy is introduced.

### Breakpoint, grid, container, and gutter defaults (KBDL-RSP-002, KBDL-RSP-003, KBDL-RSP-004, KBDL-RSP-005)

- **Blueprint section:** Exact breakpoint thresholds; grid column counts; container widths and reading measures; gutters and responsive spacing
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-RSP-002, KBDL-RSP-003, KBDL-RSP-004, KBDL-RSP-005
- **Specification location:** [responsive.md §7, §8, §9, §10](responsive.md#7-proposed-exact-breakpoint-thresholds)
- **Approval status:** Recommended (not `Approved` — requires project-owner approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status); the four named breakpoint roles themselves remain `Approved` under `KBDL-DEC-012`, unaffected)
- **Validation status:** Not applicable
- **Validation method:** Project-owner review (not yet performed); implementation-level review once an implementation exists.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** These are recommendations awaiting project-owner approval; must not be treated as `Approved` or implemented until that approval is recorded.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the responsive decision packet.
- **Notes:** Exact pixel values, grid columns, container widths, and gutters were explicitly deferred to KBDL-006 by `foundations/spacing-layout.md`; these four requirements resolve that deferral as `Recommended` proposals, mapped to [responsive decision packet](responsive.md#35-responsive-decision-packet) items 1–4.

### Navigation, density, media, and data-dense adaptation (KBDL-RSP-008, KBDL-RSP-009, KBDL-RSP-010, KBDL-RSP-011, KBDL-RSP-012)

- **Blueprint section:** Navigation adaptation; content-density adaptation; media and image adaptation; data-dense/tabular content; full-bleed and asymmetric layouts
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-RSP-008, KBDL-RSP-009, KBDL-RSP-010, KBDL-RSP-011, KBDL-RSP-012
- **Specification location:** [responsive.md §13–§17](responsive.md#13-navigation-adaptation)
- **Approval status:** `KBDL-RSP-009`, `KBDL-RSP-010`, `KBDL-RSP-012` Approved (each directly restates an already-approved KBDL principle or foundation rule); `KBDL-RSP-008`, `KBDL-RSP-011` Recommended (exact navigation collapse thresholds and the data-dense strategy are new KBDL-006 policy)
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner review of `KBDL-RSP-008`/`011` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Exact collapse thresholds and per-project column-priority rules remain qualitative pending implementation-level review.
- **Related decision:** Not applicable — pending a future decision-register entry.
- **Notes:** `KBDL-RSP-008` and `KBDL-RSP-011` map to [responsive decision packet](responsive.md#35-responsive-decision-packet) items 5 and 6.

### Sticky regions, safe areas, virtual keyboard, and input parity (KBDL-RSP-013, KBDL-RSP-014, KBDL-RSP-017, KBDL-RSP-018, KBDL-RSP-019)

- **Blueprint section:** Sticky/fixed regions; safe areas; virtual-keyboard behavior; touch/pointer/keyboard/hybrid input; hover-independent discoverability
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-RSP-013, KBDL-RSP-014, KBDL-RSP-017, KBDL-RSP-018, KBDL-RSP-019
- **Specification location:** [responsive.md §18, §19, §22, §23, §24](responsive.md#18-sticky-and-fixed-regions)
- **Approval status:** Approved — each directly restates WCAG 2.2 SC 2.4.11, SC 2.5.1/2.5.2, SC 1.4.13 (Levels A/AA), or an already-approved motion/accessibility-performance requirement
- **Validation status:** Not verified
- **Validation method:** Manual keyboard-focus, device, and cross-input testing once implemented.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation- and device-dependent.
- **Related decision:** `KBDL-DEC-010`.
- **Notes:** No new policy; these resolve the "detailed responsive breakpoint and layout rules" that `motion/accessibility-performance.md §4` explicitly deferred to KBDL-006.

### Responsive motion and performance (KBDL-RSP-021, KBDL-RSP-022)

- **Blueprint section:** Responsive motion behavior; performance and low-capability contexts
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-RSP-021, KBDL-RSP-022
- **Specification location:** [responsive.md §26, §27](responsive.md#26-responsive-motion-behavior)
- **Approval status:** Approved — restates already-approved `KBDL-MOT-006` and `KBDL-PRN-003` (Performance-Aware Enhancement)
- **Validation status:** Not verified
- **Validation method:** Manual review; implementation-level performance measurement once an implementation exists.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Performance claims cannot be `Verified` without a real implementation to measure.
- **Related decision:** `KBDL-MOT-006` (motion intensity model, already `Approved` under `KBDL-DEC-014`).
- **Notes:** Does not reopen or restate any KBDL-005 timing/easing/reduced-motion value.

### WCAG 2.2 Level A/AA baseline requirements (KBDL-A11Y-001 through KBDL-A11Y-010, KBDL-A11Y-012 through KBDL-A11Y-020, KBDL-A11Y-022 through KBDL-A11Y-034, KBDL-A11Y-036 through KBDL-A11Y-040)

- **Blueprint section:** Text alternatives; captions; semantic structure; landmarks; reading/focus order; color independence; text/non-text contrast; focus visibility/obscuration; text spacing; keyboard operability/traps/bypass; pointer cancellation; dragging/gesture alternatives; motion actuation; reduced-motion cross-reference; flashing; timing/automatic movement; forms/labels/autocomplete; error identification/prevention; status messages; authentication; plain language; consistent navigation/help; media controls cross-reference; data presentation; mobile/virtual-keyboard cross-reference; profile consistency
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-A11Y-001–010, 012–020, 022–034, 036–040 (37 requirements; excludes `KBDL-A11Y-011`, `021`, `035`, which are new KBDL enhancements listed separately below)
- **Specification location:** [accessibility.md §6–§45](accessibility.md#3-wcag-22-level-aa-mapping)
- **Approval status:** Approved for all 37 — each directly restates a WCAG 2.2 Level A or AA success criterion already adopted under `KBDL-DEC-010`, or an already-approved KBDL principle/foundation/theme/motion requirement, per the full mapping in [accessibility.md §3](accessibility.md#3-wcag-22-level-aa-mapping)
- **Validation status:** Not verified: KBDL-A11Y-001, KBDL-A11Y-002, KBDL-A11Y-003, KBDL-A11Y-004, KBDL-A11Y-005, KBDL-A11Y-006, KBDL-A11Y-010, KBDL-A11Y-012, KBDL-A11Y-013, KBDL-A11Y-014, KBDL-A11Y-015, KBDL-A11Y-016, KBDL-A11Y-017, KBDL-A11Y-018, KBDL-A11Y-020, KBDL-A11Y-022, KBDL-A11Y-023, KBDL-A11Y-024, KBDL-A11Y-025, KBDL-A11Y-026, KBDL-A11Y-027, KBDL-A11Y-028, KBDL-A11Y-029, KBDL-A11Y-030, KBDL-A11Y-031, KBDL-A11Y-032, KBDL-A11Y-033, KBDL-A11Y-034, KBDL-A11Y-037, KBDL-A11Y-040; Verified: KBDL-A11Y-007, KBDL-A11Y-008, KBDL-A11Y-009; Not applicable: KBDL-A11Y-019, KBDL-A11Y-036, KBDL-A11Y-038, KBDL-A11Y-039
- **Validation method:** WCAG relative-luminance contrast calculation (completed for contrast/focus rows); manual + automated static accessibility review, keyboard testing, screen-reader testing, and flash analysis (all pending an implementation).
- **Validation evidence:** [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence) for the three Verified rows; not verified for the rest.
- **Known limitation:** This document does not claim full WCAG conformance, screen-reader compatibility, or real-device support — those require an implementation and recorded test evidence.
- **Related decision:** `KBDL-DEC-010`.
- **Notes:** No AAA-level criterion is described as AA anywhere in this set; see [accessibility.md §3](accessibility.md#3-wcag-22-level-aa-mapping) for the exact criterion-to-section mapping.

### New KBDL-specific accessibility enhancements (KBDL-A11Y-011, KBDL-A11Y-021, KBDL-A11Y-035)

- **Blueprint section:** Forced-colors/high-contrast policy; preferred enhanced target size; preferred accessibility testing matrix
- **Roadmap prompt:** KBDL-006
- **Requirement ID:** KBDL-A11Y-011, KBDL-A11Y-021, KBDL-A11Y-035
- **Specification location:** [accessibility.md §16, §25, §39](accessibility.md#16-light-dark-forced-colors-and-high-contrast-behavior)
- **Approval status:** Recommended (not `Approved` — requires project-owner approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status))
- **Validation status:** Not verified: KBDL-A11Y-011; Not applicable: KBDL-A11Y-021, KBDL-A11Y-035
- **Validation method:** Project-owner review (not yet performed); implementation-level review once an implementation exists.
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Forced-colors/high-contrast mode is currently unaddressed elsewhere in the specification and was explicitly excluded from the KBDL-004 theme approval (`KBDL-DEC-013`); these three requirements must not be treated as `Approved` until reviewed.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the accessibility decision packet.
- **Notes:** Map to [accessibility decision packet](accessibility.md#49-accessibility-decision-packet) items 1–3 respectively.

## KBDL-007 — Core Action, Form, and Navigation Components

### Shared component contract and cross-cutting rules (KBDL-CMP-001 through KBDL-CMP-013, KBDL-CMP-050, KBDL-CMP-051)

- **Blueprint section:** Shared component contract; native-semantics-first rule; accessible naming; component state model; KBDL-008 scope boundary; focus/keyboard/pointer behavior; responsive/target-size/theme/foundation/motion mapping; cross-component composition; profile compatibility
- **Roadmap prompt:** KBDL-007
- **Requirement ID:** KBDL-CMP-001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 050, 051
- **Specification location:** [components-core.md §5–§19, §25, §26](components-core.md#6-shared-component-contract)
- **Approval status:** Approved for all fifteen — each directly restates an already-approved WCAG 2.2 Level A/AA criterion, WAI-ARIA rule, or prior approved KBDL principle/foundation/theme/motion/responsive/accessibility requirement
- **Provenance:** Confirmed for all fifteen.
- **Validation status:** Not verified: KBDL-CMP-001, KBDL-CMP-002, KBDL-CMP-003, KBDL-CMP-004, KBDL-CMP-006, KBDL-CMP-007, KBDL-CMP-008, KBDL-CMP-009, KBDL-CMP-010, KBDL-CMP-011, KBDL-CMP-012, KBDL-CMP-013, KBDL-CMP-051; Not applicable: KBDL-CMP-005, KBDL-CMP-050
- **Validation method:** Manual completeness/mapping review per component once implemented; manual scope-compliance review (performed, see implementation report).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent; cannot be tested until real components exist.
- **Related decision:** `KBDL-DEC-010` (WCAG 2.2 AA baseline).
- **Notes:** These fifteen requirements establish the contract every component below must follow; no new policy is introduced at this level.

### Action components (KBDL-CMP-014 through KBDL-CMP-021)

- **Blueprint section:** Button, Icon Button, Toggle Button, Link, Button Group, Disclosure/Menu Trigger
- **Roadmap prompt:** KBDL-007
- **Requirement ID:** KBDL-CMP-014, 015, 016, 017, 018, 019, 020, 021
- **Specification location:** [components-core.md §20](components-core.md#20-action-components)
- **Approval status:** `KBDL-CMP-014`, `016`, `018`, `019`, `021` Approved (restate native-semantics-first, WCAG, and WAI-ARIA rules); `KBDL-CMP-015` (button hierarchy taxonomy), `017` (icon-only visible-label threshold), `020` (button-group composition guidance) Recommended (new component-level taxonomy/guidance)
- **Provenance:** Confirmed for `KBDL-CMP-014`, `016`, `018`, `019`, `021`; Assumed for `KBDL-CMP-015`, `017`, `020`.
- **Validation status:** Not verified: KBDL-CMP-014, KBDL-CMP-016, KBDL-CMP-018, KBDL-CMP-019, KBDL-CMP-021; Not applicable: KBDL-CMP-015, KBDL-CMP-017, KBDL-CMP-020
- **Validation method:** Manual + automated static accessibility review, manual keyboard/ARIA review once implemented; project-owner review of `KBDL-CMP-015`/`017`/`020` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-007 decision packet.
- **Notes:** `KBDL-CMP-015`, `017`, `020` map to [KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet) items 1, 3, and 9 respectively.

### Form architecture and components (KBDL-CMP-022 through KBDL-CMP-037)

- **Blueprint section:** Shared field model; Text Input, Password Input, Search Field, Textarea, Select, Combobox, Checkbox, Radio Group, Switch, File Input, Field Group, Form Action Row; form validation and recovery
- **Roadmap prompt:** KBDL-007
- **Requirement ID:** KBDL-CMP-022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037
- **Specification location:** [components-core.md §21–§23](components-core.md#21-form-architecture)
- **Approval status:** `KBDL-CMP-022`, `023`, `024`, `026`, `027`, `028`, `030`, `031`, `032`, `033`, `034`, `035`, `037` Approved (restate WCAG 2.2 and WAI-ARIA form/error requirements); `KBDL-CMP-025` (search-field model), `029` (combobox-justification threshold), `036` (form-action-row reflow order) Recommended (new component-level guidance)
- **Provenance:** Confirmed for `KBDL-CMP-022`, `023`, `024`, `026`, `027`, `028`, `030`, `031`, `032`, `033`, `034`, `035`, `037`; Assumed for `KBDL-CMP-025`, `029`, `036`.
- **Validation status:** Not verified: KBDL-CMP-022, KBDL-CMP-023, KBDL-CMP-024, KBDL-CMP-026, KBDL-CMP-027, KBDL-CMP-028, KBDL-CMP-030, KBDL-CMP-031, KBDL-CMP-032, KBDL-CMP-033, KBDL-CMP-034, KBDL-CMP-035, KBDL-CMP-037; Not applicable: KBDL-CMP-025, KBDL-CMP-029, KBDL-CMP-036
- **Validation method:** Manual + automated static accessibility review once implemented; project-owner review of `KBDL-CMP-025`/`029`/`036` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-007 decision packet.
- **Notes:** `KBDL-CMP-025`, `029`, `036` map to [KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet) items 4, 5, and 6 respectively.

### Navigation components (KBDL-CMP-038 through KBDL-CMP-049)

- **Blueprint section:** Skip Link, Navigation Link/List, Primary/Global Navigation, Local/Section Navigation, Breadcrumb, Tabs, Pagination, Back Link
- **Roadmap prompt:** KBDL-007
- **Requirement ID:** KBDL-CMP-038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049
- **Specification location:** [components-core.md §24](components-core.md#24-navigation-components)
- **Approval status:** `KBDL-CMP-038`, `039`, `040`, `042`, `043`, `045`, `047`, `049` Approved (restate WCAG 2.2, WAI-ARIA tabs pattern, and already-approved responsive/navigation rules); `KBDL-CMP-041` (navigation collapse threshold), `044` (breadcrumb truncation model), `046` (tabs activation model), `048` (pagination truncation model) Recommended (new component-level guidance, some contingent on unapproved `KBDL-RSP-002`/`008`)
- **Provenance:** Confirmed for `KBDL-CMP-038`, `039`, `040`, `042`, `043`, `045`, `047`, `049`; Assumed for `KBDL-CMP-041`, `044`, `046`, `048`.
- **Validation status:** Not verified: KBDL-CMP-038, KBDL-CMP-039, KBDL-CMP-040, KBDL-CMP-042, KBDL-CMP-043, KBDL-CMP-045, KBDL-CMP-047, KBDL-CMP-049; Not applicable: KBDL-CMP-041, KBDL-CMP-044, KBDL-CMP-046, KBDL-CMP-048
- **Validation method:** Manual keyboard/ARIA review once implemented; project-owner review of `KBDL-CMP-041`/`044`/`046`/`048` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-CMP-041` additionally depends on the unapproved `KBDL-RSP-002`/`008` and cannot be approved independently of them.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-007 decision packet.
- **Notes:** `KBDL-CMP-044`, `046`, `048` map to approval-ready [KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet) items 7, 2, and 8 respectively. `KBDL-CMP-041` maps to a contingent, not-approval-ready item in [§35.3](components-core.md#353-unresolved-or-not-approval-ready) — it remains `Recommended`, but cannot be approved through the KBDL-007 packet until its `KBDL-RSP-002`/`008` dependencies are approved or replaced.

## KBDL-008 — Surface, Overlay, Feedback, and System-State Components

The rows below trace KBDL-008's scope, defined in
[components-system.md](components-system.md). Full per-requirement
detail (rationale, validation method, decision-packet mapping) lives in
that document; these rows summarize status for cross-module lookup.

### Surface components and module-wide baselines (KBDL-CMP-052, 053, 054, 055, 062, 065, 067, 068, 069, 070)

- **Blueprint section:** KBDL-007 ownership boundary; extended system-component contract; surface architecture; Container Surface, Panel, Card, Accordion, Static Data Table
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-052, 053, 054, 055, 062, 065, 067, 068, 069, 070
- **Specification location:** [components-system.md §5, §7, §8, §9](components-system.md#5-kbdl-007-ownership-boundary)
- **Approval status:** `KBDL-CMP-052`, `053`, `054`, `055`, `062`, `065`, `068`, `070` Approved (restate KBDL-007's scope-control and accessible-naming rules, native-semantics-first rule, WCAG 1.3.1/1.4.1, and the adopted ARIA disclosure/region definitions); `KBDL-CMP-067` (card-variant taxonomy), `069` (accordion open model) Recommended (new component-level taxonomy)
- **Provenance:** Confirmed for `KBDL-CMP-052`, `053`, `054`, `055`, `062`, `065`, `068`, `070`; Assumed for `KBDL-CMP-067`, `069`.
- **Validation status:** Not applicable: KBDL-CMP-052, KBDL-CMP-067, KBDL-CMP-069; Not verified: KBDL-CMP-053, KBDL-CMP-054, KBDL-CMP-055, KBDL-CMP-062, KBDL-CMP-065, KBDL-CMP-068, KBDL-CMP-070
- **Validation method:** Manual semantic-structure and DOM-relationship review once implemented; project-owner review of `KBDL-CMP-067`/`069` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-008 decision packet.
- **Notes:** `KBDL-CMP-067`, `069` map to [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet) items 1 and 2 respectively.

### Overlay components (KBDL-CMP-056 through KBDL-CMP-060, 071 through 085)

- **Blueprint section:** Overlay architecture; Tooltip, Popover, Menu surface, Listbox popup, Dialog, Modal Dialog, Alert Dialog, Drawer/Sheet; overlay layering and nesting
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-056, 057, 058, 059, 060, 071, 072, 073, 074, 075, 076, 077, 078, 079, 080, 081, 082, 083, 084, 085
- **Specification location:** [components-system.md §10–§12](components-system.md#10-overlay-architecture)
- **Approval status:** `KBDL-CMP-056`, `057`, `058`, `059`, `060`, `075`, `077`, `078`, `079`, `081`, `082`, `084` Approved (restate WCAG 2.1.1/2.1.2/2.2.1/2.4.3/2.4.11/4.1.2, the already-Approved motion-parity rule, adopted ARIA menu/listbox/dialog/alertdialog role definitions, and the KBDL-007 scope-control rule); `KBDL-CMP-071` Approved with mixed authority (background-inertness-for-screen-readers is authorized by the adopted WAI-ARIA `aria-modal` property definition, supported by WCAG 2.4.3/2.4.11; treating this as one complete rule is additionally authorized by the approved KBDL-008 prompt's explicit "Background inertness" requirement); `KBDL-CMP-072` Approved with mixed authority (dismissible/hoverable/persistent restates WCAG 1.4.13; accessible-name independence restates WCAG 4.1.2/`KBDL-CMP-003`; non-interactive-content and focus-remains-on-trigger are authorized only by the approved KBDL-008 prompt's explicit Tooltip requirements, not by WCAG 1.4.13 or the ARIA tooltip role alone); `KBDL-CMP-073` (tooltip timing), `074` (popover taxonomy), `076` (menu interaction model), `080` (modal sizing/nesting), `083` (drawer/sheet taxonomy), `085` (overlay nesting policy) Recommended (new, discretionary component-level timing, taxonomy, or nesting policy not mandated by the approved prompt)
- **Provenance:** Confirmed for `KBDL-CMP-056`, `057`, `058`, `059`, `060`, `071`, `072`, `075`, `077`, `078`, `079`, `081`, `082`, `084`; Assumed for `KBDL-CMP-073`, `074`, `076`, `080`, `083`, `085`.
- **Validation status:** Not applicable: KBDL-CMP-056, KBDL-CMP-073, KBDL-CMP-074, KBDL-CMP-076, KBDL-CMP-080, KBDL-CMP-082, KBDL-CMP-083, KBDL-CMP-085; Not verified: KBDL-CMP-057, KBDL-CMP-058, KBDL-CMP-059, KBDL-CMP-060, KBDL-CMP-071, KBDL-CMP-072, KBDL-CMP-075, KBDL-CMP-077, KBDL-CMP-078, KBDL-CMP-079, KBDL-CMP-081, KBDL-CMP-084
- **Validation method:** Manual focus-containment, keyboard, and ARIA-relationship review once implemented; project-owner review of the Recommended subset (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-CMP-083` additionally notes that navigation-drawer use remains bound by the unapproved `KBDL-CMP-041` (KBDL-007) regardless of this item's own approval.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-008 decision packet.
- **Notes:** `KBDL-CMP-073`, `074`, `076`, `080`, `083`, `085` map to [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet) items 3, 4, 5, 6, 7, and 8 respectively.

### Feedback components (KBDL-CMP-061, 086 through KBDL-CMP-098)

- **Blueprint section:** Feedback architecture; Inline Feedback, Alert, Banner, Toast/Snackbar, Status Region/Log, Badge, Progress Indicator, Meter, Skeleton
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-061, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 098
- **Specification location:** [components-system.md §13–§14](components-system.md#13-feedback-architecture)
- **Approval status:** `KBDL-CMP-061`, `086`, `087`, `092`, `093`, `094`, `095`, `098` Approved (restate the locked component-state-clarity rule, `KBDL-A11Y-031`, adopted WAI-ARIA live-region/progressbar/meter role definitions, WCAG 1.1.1/1.4.1, and the existing KBDL-007 submit-loading contract); `KBDL-CMP-088` Approved with mixed authority (urgency/no-focus-theft restates the adopted ARIA `alert` role definition; "must not be used for routine or successful updates" is authorized only by the approved KBDL-008 prompt's explicit Alert constraint, not by the ARIA role definition alone); `KBDL-CMP-090` Approved with mixed authority (no sensitive-information exposure restates the existing KBDL security principle, `components-core.md §37`; the persistent-path and no-default-focus-move requirements are authorized by the approved KBDL-008 prompt's explicit Toast/Snackbar constraints, with WCAG 2.2.1 as supporting rationale only); `KBDL-CMP-096` Approved with mixed authority (decorative/hidden treatment restates the adopted ARIA `aria-hidden` semantics and `KBDL-A11Y-031`; "must not expose meaningless placeholder shapes as content" is authorized only by the approved KBDL-008 prompt's explicit Skeleton requirements); `KBDL-CMP-089` (banner taxonomy), `091` (toast lifecycle model) Recommended (new, discretionary component-level taxonomy/timing not mandated by the approved prompt)
- **Provenance:** Confirmed for `KBDL-CMP-061`, `086`, `087`, `088`, `090`, `092`, `093`, `094`, `095`, `096`, `098`; Assumed for `KBDL-CMP-089`, `091`.
- **Validation status:** Not verified: KBDL-CMP-061, KBDL-CMP-086, KBDL-CMP-087, KBDL-CMP-088, KBDL-CMP-090, KBDL-CMP-092, KBDL-CMP-093, KBDL-CMP-094, KBDL-CMP-095, KBDL-CMP-096, KBDL-CMP-098; Not applicable: KBDL-CMP-089, KBDL-CMP-091
- **Validation method:** Manual live-region, role, and content-classification review once implemented; project-owner review of `KBDL-CMP-089`/`091` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-008 decision packet.
- **Notes:** `KBDL-CMP-089`, `091` map to [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet) items 9 and 10 respectively.

### System-state, complex-presentation, and profile/security baselines (KBDL-CMP-063, 064, 066, 097, 099–111)

- **Blueprint section:** System-state architecture; Loading, Empty, No-Results, Error, Offline/Reconnecting, Permission Denied, Not Found, Maintenance/Degraded, System Status; complex-presentation architecture; Interactive Grid, Tree/Treegrid, Carousel, Data Visualization; responsive transformation policy; security/privacy and profile-compatibility baselines
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-063, 064, 066, 097, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111
- **Specification location:** [components-system.md §15–§19, §23, §24](components-system.md#15-system-state-architecture)
- **Approval status:** `KBDL-CMP-063`, `064`, `066`, `097`, `103`, `104`, `107`, `109` Approved (restate `KBDL-A11Y-031`, the locked component-state-clarity rule, WCAG 2.2.2/1.4.1/1.3.1/2.1.1, the existing KBDL correctness/safety and security principles, the existing Data-display theme roles, and the already-Approved `KBDL-CMP-051` profile-consistency rule); `KBDL-CMP-100` Approved with mixed authority (preserving entered query/filter criteria is authorized by the approved KBDL-008 prompt's explicit No-Results State requirement, with WCAG 3.3.7 cited only as supporting analogy, not a direct restatement); `KBDL-CMP-101` Approved with mixed authority (error identification restates WCAG 3.3.1; the recoverable/blocking classification and retry/alternative-action requirement are authorized by the approved KBDL-008 prompt's explicit Error State requirements and the already-Approved Technical Utility recovery-support principle; the no-diagnostic-exposure clause restates `KBDL-CMP-064`); `KBDL-CMP-099` (empty-state taxonomy), `102` (error/system-state severity taxonomy), `105` (grid-versus-table threshold), `106` (treegrid justification threshold), `108` (carousel auto-rotation policy), `110` (data-visualization interaction model), `111` (responsive transformation policy) Recommended (new, discretionary component-level taxonomy, threshold, or policy not mandated by the approved prompt)
- **Provenance:** Confirmed for `KBDL-CMP-063`, `064`, `066`, `097`, `100`, `101`, `103`, `104`, `107`, `109`; Assumed for `KBDL-CMP-099`, `102`, `105`, `106`, `108`, `110`, `111`.
- **Validation status:** Not verified: KBDL-CMP-063, KBDL-CMP-064, KBDL-CMP-066, KBDL-CMP-097, KBDL-CMP-100, KBDL-CMP-101, KBDL-CMP-103, KBDL-CMP-104, KBDL-CMP-107, KBDL-CMP-109; Not applicable: KBDL-CMP-099, KBDL-CMP-102, KBDL-CMP-105, KBDL-CMP-106, KBDL-CMP-108, KBDL-CMP-110, KBDL-CMP-111
- **Validation method:** Manual review once implemented; project-owner review of the Recommended subset (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-CMP-105` additionally cites the unapproved `KBDL-RSP-011` as related context; `KBDL-CMP-111` additionally depends on the eventual `KBDL-RSP-002` value for its exact trigger point.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-008 decision packet.
- **Notes:** `KBDL-CMP-099`, `102`, `105`, `106`, `108`, `110`, `111` map to [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet) items 11, 12, 13, 14, 15, 16, and 17 respectively.

## KBDL-009 — Project Profiles

The rows below trace KBDL-009's scope, defined in
[profiles.md](profiles.md). Full per-requirement detail (rationale,
validation method, decision-packet mapping) lives in that document;
these rows summarize status for cross-module lookup.

### Shared architecture, terminology, and governance (KBDL-PRO-001 through KBDL-PRO-009)

- **Blueprint section:** Profile architecture; terminology; locked/controlled/open classification; profile selection and declaration
- **Roadmap prompt:** KBDL-009
- **Requirement ID:** KBDL-PRO-001, 002, 003, 004, 005, 006, 007, 008, 009
- **Specification location (per-ID map):** `KBDL-PRO-001` → [profiles.md §5](profiles.md#5-profile-architecture); `002` → [§4](profiles.md#4-project-profile-terminology) (terminology distinction, not §5 — verified directly against the requirement's own record); `003` → [§7](profiles.md#7-locked-controlled-and-open-profile-decisions); `004` → [§7](profiles.md#7-locked-controlled-and-open-profile-decisions); `005` → [§7](profiles.md#7-locked-controlled-and-open-profile-decisions); `006` → [§7](profiles.md#7-locked-controlled-and-open-profile-decisions); `007` → [§8](profiles.md#8-profile-selection-and-declaration); `008` → [§8](profiles.md#8-profile-selection-and-declaration); `009` → [§8](profiles.md#8-profile-selection-and-declaration).
- **Approval status:** `KBDL-PRO-001`–`008` Approved (restate the already-Approved `KBDL-PRN-007`, `KBDL-FND-008`, `KBDL-THM-006`, `KBDL-MOT-026`, `KBDL-A11Y-040`, `KBDL-CMP-051`, `KBDL-CMP-066`, and explicit mandatory clauses of the approved KBDL-009 prompt); `KBDL-PRO-009` (primary/secondary/hybrid policy) Recommended (new governance policy)
- **Provenance:** Confirmed for `KBDL-PRO-001`–`008`; Assumed for `KBDL-PRO-009`.
- **Validation status:** Not verified: KBDL-PRO-001, KBDL-PRO-002, KBDL-PRO-003, KBDL-PRO-004, KBDL-PRO-005; Not applicable: KBDL-PRO-006, KBDL-PRO-007, KBDL-PRO-008, KBDL-PRO-009
- **Authority:** `KBDL-PRO-001`–`008`: prior-Approved KBDL requirements and/or explicit mandatory clauses of the approved KBDL-009 prompt (see each ID's own record for the exact split). `KBDL-PRO-009`: not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
- **Validation method:** Manual cross-module architecture review once implemented; project-owner review of `KBDL-PRO-009` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-PRO-001`–`008`: implementation-dependent, not yet verified. `KBDL-PRO-009`: Recommended, grants no implementation authority pending project-owner review.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-009 decision packet.
- **Related prior requirements:** `KBDL-PRN-007`, `KBDL-FND-008`, `KBDL-THM-006`, `KBDL-MOT-026`, `KBDL-A11Y-040`, `KBDL-CMP-051`, `KBDL-CMP-066`.
- **Pending dependencies (per-ID):** `KBDL-PRO-001`–`008`: none. `KBDL-PRO-009`: no blocking dependency (independently approval-ready).
- **Packet destination (per-ID):** `KBDL-PRO-001`–`008`: None — Approved requirement; not awaiting packet approval. `KBDL-PRO-009`: Approval-ready item 1.
- **Future customization dependency:** None.
- **Future validation dependency:** Implementation-level profile validation (`VAL`, locked).
- **Notes:** `KBDL-PRO-009` maps to [KBDL-009 decision packet](profiles.md#33-kbdl-009-decision-packet) item 1.

### Showcase, Precision, and Flow profile definitions (KBDL-PRO-010 through KBDL-PRO-018)

- **Blueprint section:** Showcase Profile; Precision Profile; Flow Profile; component interpretation per profile
- **Roadmap prompt:** KBDL-009
- **Requirement ID:** KBDL-PRO-010, 011, 012, 013, 014, 015, 016, 017, 018
- **Specification location (per-ID map):** `KBDL-PRO-010` → [profiles.md §10.1](profiles.md#101-purpose); `011` → [§11.1](profiles.md#111-purpose); `012` → [§12.1](profiles.md#121-purpose); `013` → [§10.2](profiles.md#102-component-interpretation); `014` → [§11.2](profiles.md#112-component-interpretation); `015` → [§12.2](profiles.md#122-component-interpretation); `016` → [§10.2](profiles.md#102-component-interpretation); `017` → [§11.2](profiles.md#112-component-interpretation); `018` → [§12.2](profiles.md#122-component-interpretation).
- **Approval status:** `KBDL-PRO-010`–`015` Approved (consolidate the already-Approved per-profile interpretation in principles.md, foundations/README.md, themes/README.md, motion/patterns.md, responsive.md, and the already-Approved `KBDL-CMP-051`/`066`/`010`/`055`/`070`/`072`/`090`/`107` component boundaries); `KBDL-PRO-016` (Showcase composition defaults), `017` (Precision density defaults), `018` (Flow action defaults) Recommended (new discretionary profile-specific defaults)
- **Provenance:** Confirmed for `KBDL-PRO-010`–`015`; Assumed for `KBDL-PRO-016`, `017`, `018`.
- **Validation status:** Not verified: KBDL-PRO-010, KBDL-PRO-011, KBDL-PRO-012, KBDL-PRO-013, KBDL-PRO-014, KBDL-PRO-015; Not applicable: KBDL-PRO-016, KBDL-PRO-017, KBDL-PRO-018
- **Authority:** `KBDL-PRO-010`–`015`: prior-Approved KBDL requirements (see each ID's own record for the exact sources). `KBDL-PRO-016`, `017`, `018`: not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
- **Validation method:** Manual cross-module consistency review once implemented; project-owner review of `KBDL-PRO-016`/`017`/`018` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-PRO-016` additionally depends on the unapproved KBDL-008 `KBDL-CMP-067`; `KBDL-PRO-018` additionally depends on the unapproved KBDL-007 `KBDL-CMP-015`/`036`.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-009 decision packet.
- **Related prior requirements:** `KBDL-CMP-010`, `015`, `036`, `051`, `055`, `066`, `067`, `070`, `072`, `090`, `107`.
- **Pending dependencies (per-ID):** `KBDL-PRO-010`–`015`: none. `KBDL-PRO-016`: blocked by `KBDL-CMP-067` (KBDL-008). `KBDL-PRO-017`: no blocking dependency; `KBDL-RSP-002` and `003` are cited as unapproved context only, not required for this item's own approval. `KBDL-PRO-018`: blocked by `KBDL-CMP-015` and `036` (KBDL-007).
- **Packet destination (per-ID):** `KBDL-PRO-010`–`015`: None — Approved requirement; not awaiting packet approval. `KBDL-PRO-016`: Contingent — [§33.3](profiles.md#333-unresolved-or-not-approval-ready); not independently approval-ready. `KBDL-PRO-017`: Approval-ready item 2. `KBDL-PRO-018`: Contingent — [§33.3](profiles.md#333-unresolved-or-not-approval-ready); not independently approval-ready.
- **Future customization dependency:** None.
- **Future validation dependency:** Implementation-level profile validation (`VAL`, locked).
- **Notes:** `KBDL-PRO-017` maps to [KBDL-009 decision packet](profiles.md#33-kbdl-009-decision-packet) item 2 (independently approval-ready). `KBDL-PRO-016` and `018` map to the contingent items in [profiles.md §33.3](profiles.md#333-unresolved-or-not-approval-ready), not to any approval-ready item.

### Mapping, content, security, conflict, and adoption requirements (KBDL-PRO-019 through KBDL-PRO-029)

- **Blueprint section:** Principles/core-component/system-component mapping; content and communication; security, privacy, and correctness; profile conflicts; profile adoption and change management
- **Roadmap prompt:** KBDL-009
- **Requirement ID:** KBDL-PRO-019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029
- **Specification location (per-ID map):** `KBDL-PRO-019` → [profiles.md §14](profiles.md#14-principles-mapping); `020` → [§20](profiles.md#20-core-component-mapping); `021` → [§21](profiles.md#21-system-component-mapping); `022` → [§22](profiles.md#22-content-and-communication-considerations); `023` → [§23](profiles.md#23-security-privacy-and-correctness); `024`, `025` → [§24](profiles.md#24-profile-conflicts-and-exception-handling); `026`, `027`, `029` → [§25](profiles.md#25-profile-adoption-and-change-management); `028` → [§8](profiles.md#8-profile-selection-and-declaration) (grouped thematically with adoption/selection governance here, but normatively located at its own authoritative record in §8, not §25).
- **Approval status:** `KBDL-PRO-019`–`026` Approved (restate the already-Approved `KBDL-PRN-003`, `KBDL-CMP-051`, `066`, `101`, `103`, `KBDL-CMP-063`/`064`/`098`/`104`, `principles.md §8`, and `governance.md`'s exception process, plus explicit mandatory clauses of the approved KBDL-009 prompt); `KBDL-PRO-027` (change/migration governance), `028` (selection rubric), `029` (review cadence) Recommended (new discretionary governance policy)
- **Provenance:** Confirmed for `KBDL-PRO-019`–`026`; Assumed for `KBDL-PRO-027`, `028`, `029`.
- **Validation status:** Not verified: KBDL-PRO-019, KBDL-PRO-020, KBDL-PRO-021, KBDL-PRO-022, KBDL-PRO-023, KBDL-PRO-024; Not applicable: KBDL-PRO-025, KBDL-PRO-026, KBDL-PRO-027, KBDL-PRO-028, KBDL-PRO-029
- **Authority:** `KBDL-PRO-019`–`026`: prior-Approved KBDL requirements and/or explicit mandatory clauses of the approved KBDL-009 prompt (see each ID's own record for the exact split). `KBDL-PRO-027`, `028`, `029`: not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
- **Validation method:** Manual review once implemented; project-owner review of `KBDL-PRO-027`/`028`/`029` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-PRO-019`–`026`: implementation-dependent, not yet verified. `KBDL-PRO-027`, `029`: Recommended, grants no implementation authority pending project-owner review. `KBDL-PRO-028`: Recommended, grants no implementation authority pending project-owner review.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the KBDL-009 decision packet.
- **Related prior requirements:** `KBDL-PRN-003`, `KBDL-PRN-006`, `KBDL-GOV-002`, `KBDL-GOV-003`, `KBDL-CMP-051`, `063`, `064`, `066`, `098`, `101`, `103`, `104`.
- **Pending dependencies (per-ID):** `KBDL-PRO-027`: no pending dependency (independently approval-ready). `KBDL-PRO-028`: no pending dependency (independently approval-ready). `KBDL-PRO-029`: no pending dependency (independently approval-ready). `KBDL-PRO-019`–`026`: none.
- **Packet destination (per-ID):** `KBDL-PRO-019`–`026`: None — Approved requirement; not awaiting packet approval. `KBDL-PRO-027`: Approval-ready item 3. `KBDL-PRO-028`: Approval-ready item 4. `KBDL-PRO-029`: Approval-ready item 5.
- **Future customization dependency:** Governed by [customization.md](customization.md); no customization is approved by this traceability row.
- **Future validation dependency:** Implementation-level profile validation (`VAL`, locked).
- **Notes:** `KBDL-PRO-027`, `028`, `029` map to [KBDL-009 decision packet](profiles.md#33-kbdl-009-decision-packet) approval-ready items 3, 4, and 5 respectively (not contingent; see [profiles.md §38](profiles.md#38-decision-packet-coverage-audit) for the full, corrected coverage audit).

## KBDL-010 — Manual Customization

The entries below trace every KBDL-010 requirement to
[customization.md](customization.md). Each ID appears exactly once.

### Authority, classification, workflow, and records (KBDL-CUS-001 through KBDL-CUS-012)

- **Blueprint section:** Manual/documented customization; authority; classification; workflow; intake; records; impact/evidence; review/rollback
- **Roadmap prompt:** KBDL-010
- **Requirement ID:** `KBDL-CUS-001`, `KBDL-CUS-002`, `KBDL-CUS-003`, `KBDL-CUS-004`, `KBDL-CUS-005`, `KBDL-CUS-006`, `KBDL-CUS-007`, `KBDL-CUS-008`, `KBDL-CUS-009`, `KBDL-CUS-010`, `KBDL-CUS-011`, `KBDL-CUS-012`
- **Specification location (per-ID):** `001` → [§1](customization.md#1-purpose-and-scope); `002` → [§5](customization.md#5-customization-authority-model); `003` → [§6](customization.md#6-locked-controlled-open-proposed-and-exception-classifications); `004` → [§12](customization.md#12-approval-and-escalation-paths); `005` → [§24](customization.md#24-content-and-open-brand-expression); `006` → [§26](customization.md#26-reusable-versus-project-local-customization); `007` → [§27](customization.md#27-conflict-handling-and-exceptions); `008` → [§7](customization.md#7-manual-customization-workflow); `009` → [§8](customization.md#8-customization-request-intake); `010` → [§11](customization.md#11-customization-record); `011` → [§10](customization.md#10-impact-assessment) and [§14](customization.md#14-validation-and-evidence-planning); `012` → [§15](customization.md#15-review-expiry-change-and-rollback).
- **Lifecycle status:** All Approved.
- **Provenance:** All Confirmed.
- **Validation status:** Not verified
- **Authority:** Per-ID prior Approved governance/principle/profile sources and/or explicit mandatory KBDL-010 prompt clauses; exact source appears in each normative record.
- **Customization class:** `001`–`003`, `008`–`011`: A–F; `004`: A; `005`: B; `006`: C/D; `007`: E/F; `012`: A–E.
- **Validation method / evidence:** Per-ID record, authority, classification, workflow, field, impact, proposal, exception, history, or rollback audit; evidence Not verified because no project customization exists.
- **Known limitation:** Exact local operational policies remain Recommended; implementation behavior is absent.
- **Related decision:** `KBDL-DEC-004` for manual documentation; no KBDL-010 packet decision exists.
- **Related prior requirements:** `KBDL-PRN-005`, `KBDL-GOV-002`, `003`, `KBDL-PRO-004`, `005`, plus per-record references.
- **Packet destination (per-ID):** `001`–`012`: None — Approved requirements do not await packet approval.
- **Pending dependencies (per-ID):** `001`–`012`: None.
- **Profile impact:** Shared across Showcase, Precision, and Flow; no Profile architecture change.
- **Future validation dependency:** Project implementation evidence and later `VAL` policy.
- **Notes:** A record documents authority and never creates it.

### Cross-module preservation and handoff (KBDL-CUS-013 through KBDL-CUS-022)

- **Blueprint section:** Foundations; themes; motion; responsive; accessibility; core/system components; Profiles; security/correctness; handoff
- **Roadmap prompt:** KBDL-010
- **Requirement ID:** `KBDL-CUS-013`, `KBDL-CUS-014`, `KBDL-CUS-015`, `KBDL-CUS-016`, `KBDL-CUS-017`, `KBDL-CUS-018`, `KBDL-CUS-019`, `KBDL-CUS-020`, `KBDL-CUS-021`, `KBDL-CUS-022`
- **Specification location (per-ID):** `013` → [§16](customization.md#16-foundations-customization); `014` → [§17](customization.md#17-theme-customization); `015` → [§18](customization.md#18-motion-customization); `016` → [§19](customization.md#19-responsive-customization); `017` → [§20](customization.md#20-accessibility-customization-boundary); `018` → [§21](customization.md#21-core-component-customization); `019` → [§22](customization.md#22-system-component-customization); `020` → [§23](customization.md#23-project-profile-customization); `021` → [§25](customization.md#25-security-privacy-correctness-and-data-integrity); `022` → [§13](customization.md#13-implementation-handoff-boundary).
- **Lifecycle status:** All Approved.
- **Provenance:** All Confirmed.
- **Validation status:** Not verified
- **Authority:** Approved owning-module requirements plus explicit mandatory KBDL-010 preservation clauses; exact source appears per normative record.
- **Customization class:** All A–F.
- **Validation method / evidence:** Owning-module value, parity, safety, outcome, WCAG, component-contract, invariant, security, or handoff audit; evidence Not verified.
- **Known limitation:** No project implementation exists; every listed earlier recommendation remains excluded.
- **Related decision:** None new; existing owning-module decisions remain authoritative.
- **Related prior requirements:** `KBDL-FND-001`–`012`, Approved `THM`, `MOT`, `RSP`, `A11Y`, `CMP`, and `PRO` requirements, especially `KBDL-GOV-002`, `KBDL-PRO-023`, `KBDL-CMP-103`, `104`.
- **Packet destination (per-ID):** `013`–`022`: None — Approved.
- **Pending dependencies (per-ID):** `013`–`022`: None; pending earlier items are exclusions, not normative dependencies.
- **Profile impact:** One shared semantic/accessibility architecture and all invariants preserved.
- **Future validation dependency:** Real implementation evidence and later `VAL` policy.
- **Notes:** No exact value, technology, component semantic variant, Profile, or exception is introduced.

### Discretionary KBDL-010 policy (KBDL-CUS-023 through KBDL-CUS-029)

- **Blueprint section:** Identifier; local roles; risk/evidence and material-classification review triggers; review/expiry; precedence; reuse; archive/licensing/rollback evidence
- **Roadmap prompt:** KBDL-010
- **Requirement ID:** `KBDL-CUS-023`, `KBDL-CUS-024`, `KBDL-CUS-025`, `KBDL-CUS-026`, `KBDL-CUS-027`, `KBDL-CUS-028`, `KBDL-CUS-029`
- **Specification location (per-ID):** `023` → [§11](customization.md#11-customization-record); `024` → [§12](customization.md#12-approval-and-escalation-paths); `025` → [§14](customization.md#14-validation-and-evidence-planning); `026`, `027` → [§15](customization.md#15-review-expiry-change-and-rollback); `028` → [§26](customization.md#26-reusable-versus-project-local-customization); `029` → [§15](customization.md#15-review-expiry-change-and-rollback) and [§24](customization.md#24-content-and-open-brand-expression).
- **Lifecycle status:** All Recommended.
- **Provenance:** All Assumed.
- **Validation status:** Not applicable
- **Authority:** Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
- **Customization class:** `023`, `026`, `027`, `029`: A–E; `024`, `025`: A–F; `028`: C/D.
- **Validation method / evidence:** Project-owner review; not yet performed.
- **Known limitation:** Exact policies are not authorized.
- **Related decision:** None — no packet item has been approved.
- **Related prior requirements:** `KBDL-CUS-005`, `006`, `010`, `011`, `012` as specified per record.
- **Packet destination (per-ID):** `023` → item 1; `024` → item 2; `025` → item 3; `026` → item 4; `027` → item 5; `028` → item 6; `029` → item 7, all independently approval-ready.
- **Pending dependencies (per-ID):** None.
- **Profile impact:** Shared policy only; no Profile change.
- **Future validation dependency:** Implementation evidence; item 3 excludes final-validation policy.
- **Notes:** Approval scope and exclusions appear in [the packet](customization.md#37-kbdl-010-decision-packet). Item 2's accessibility/security independent-review rule has no material-threshold dependency; item 3 exclusively owns risk tiers, minor/material thresholds, and any material-classification reviewer trigger.

### Deferred machine-readable format (KBDL-CUS-030)

- **Blueprint section:** Deferred tooling and formats
- **Roadmap prompt:** KBDL-010
- **Requirement ID:** `KBDL-CUS-030`
- **Specification location:** [customization.md §41](customization.md#41-deferred-and-unresolved-items)
- **Lifecycle status:** Deferred.
- **Provenance:** Assumed.
- **Validation status:** Not applicable
- **Authority:** Not applicable — deliberately deferred; assignment of a CUS ID does not grant implementation authority.
- **Customization class:** A–E.
- **Validation method / evidence:** Not applicable until resumed; no evidence.
- **Known limitation:** No machine-readable format or tooling is authorized.
- **Related decision:** None.
- **Related prior requirements:** `KBDL-CUS-010`, `022`.
- **Packet destination:** Deferred tracking.
- **Pending dependency:** Later implementation/tooling authorization.
- **Profile impact:** None.
- **Future validation dependency:** Later authorized tooling and `VAL` scope.
- **Notes:** Not an orphan packet item and not approval-ready.

## KBDL-011 — Final Validation

The entries below trace every KBDL-011 methodology requirement to
[validation.md](validation.md). Each ID appears exactly once in the grouped
records and has its own specification location and evidence boundary.

### Evidence, inventory, lifecycle, and validation integrity (KBDL-VAL-001 through KBDL-VAL-004)

- **Blueprint section:** Final validation methodology; evidence classification; complete inventory; authority and status integrity
- **Roadmap prompt:** KBDL-011
- **Requirement ID:** `KBDL-VAL-001`, `KBDL-VAL-002`, `KBDL-VAL-003`, `KBDL-VAL-004`
- **Specification location (per-ID):** `001` → [§4](validation.md#4-evidence-classification); `002` → [§8](validation.md#8-requirement-inventory); `003` → [§9](validation.md#9-lifecycle-status-audit) and [§12](validation.md#12-approved-authority-audit); `004` → [§11](validation.md#11-validation-status-audit).
- **Lifecycle status:** All Approved.
- **Provenance:** All Confirmed.
- **Validation status (per-ID):** `001`, `002`, `003`, `004`: Verified.
- **Authority:** Explicit mandatory KBDL-011 prompt clauses approved by the project owner.
- **Validation class (per-ID):** `001`: A; `002`: A; `003`: B; `004`: B.
- **Validation method / evidence (per-ID):** `001`: class-assignment audit; `002`: repository inventory parser; `003`: lifecycle/authority comparison; `004`: validation-label/evidence comparison. Executed results are recorded in [§4](validation.md#4-evidence-classification), [§8](validation.md#8-requirement-inventory), [§9](validation.md#9-lifecycle-status-audit), and [§11](validation.md#11-validation-status-audit).
- **Known limitation:** These methods validate repository evidence only; they do not execute an implementation.
- **Related decision:** None; methodology approval does not alter earlier decisions.
- **Related prior requirements:** `KBDL-GOV-001`–`003` and all inventoried KBDL requirements.
- **Packet destination (per-ID):** `001`–`004`: None — Approved.
- **Pending dependencies (per-ID):** `001`–`004`: None for the documented checks.
- **Profile impact:** None; all Profiles remain under one shared architecture.
- **Future validation dependency:** Runtime and project claims remain Classes E/F.
- **Notes:** Verification is scoped to the executed validation method.

### Decisions, traceability, documentation, and architecture (KBDL-VAL-005 through KBDL-VAL-008)

- **Blueprint section:** Decision and pending integrity; traceability; documentation integrity; static cross-module consistency
- **Roadmap prompt:** KBDL-011
- **Requirement ID:** `KBDL-VAL-005`, `KBDL-VAL-006`, `KBDL-VAL-007`, `KBDL-VAL-008`
- **Specification location (per-ID):** `005` → [§13](validation.md#13-decision-register-audit) and [§14](validation.md#14-pending-and-deferred-inventory); `006` → [§15](validation.md#15-traceability-audit); `007` → [§16](validation.md#16-cross-reference-and-documentation-integrity-audit); `008` → [§17](validation.md#17-governance-and-conventions-audit) through [§28](validation.md#28-security-privacy-correctness-and-data-integrity-audit).
- **Lifecycle status:** All Approved.
- **Provenance:** All Confirmed.
- **Validation status (per-ID):** `005`, `006`, `007`: Verified; `008`: Not verified.
- **Authority:** Explicit mandatory KBDL-011 prompt clauses approved by the project owner.
- **Validation class (per-ID):** `005`: B; `006`: A; `007`: A; `008`: C.
- **Validation method / evidence (per-ID):** `005`: decision/pending ledger audit; `006`: per-ID traceability audit; `007`: link, anchor, heading, table, ID, roadmap, and claim checks; `008`: static invariant comparison. Executed evidence is recorded in the linked sections.
- **Known limitation:** Static agreement does not establish runtime, assistive-technology, device, security, or production conformance.
- **Related decision:** Existing `KBDL-DEC-001`–`015`; no new decision is created.
- **Related prior requirements:** All module requirements, with owning-module references listed in [validation.md §17–§28](validation.md#17-governance-and-conventions-audit).
- **Packet destination (per-ID):** `005`–`008`: None — Approved.
- **Pending dependencies (per-ID):** `005`–`008`: None for static repository validation; recorded recommendations and deferrals remain pending.
- **Profile impact:** Shared semantics, accessibility, components, and invariants are preserved.
- **Future validation dependency:** Implementation/project evidence for all runtime conclusions.
- **Notes:** Grouping is presentation only; each listed ID has a distinct evidence record.

### Calculations, evidence ledgers, and completion gate (KBDL-VAL-009 through KBDL-VAL-012)

- **Blueprint section:** Reproducible theme calculations; implementation and project ledgers; completion governance
- **Roadmap prompt:** KBDL-011
- **Requirement ID:** `KBDL-VAL-009`, `KBDL-VAL-010`, `KBDL-VAL-011`, `KBDL-VAL-012`
- **Specification location (per-ID):** `009` → [§20](validation.md#20-theme-audit); `010` → [§29](validation.md#29-implementation-dependent-validation-ledger); `011` → [§30](validation.md#30-project-specific-validation-ledger); `012` → [§41](validation.md#41-completion-and-approval-boundary).
- **Lifecycle status:** All Approved.
- **Provenance:** All Confirmed.
- **Validation status (per-ID):** `009`: Verified; `010`, `011`: Not verified; `012`: Verified.
- **Authority:** Explicit mandatory KBDL-011 prompt clauses approved by the project owner.
- **Validation class (per-ID):** `009`: D; `010`: E; `011`: F; `012`: B.
- **Validation method / evidence (per-ID):** `009`: independently executed WCAG opaque-color contrast calculation; `010`: implementation-evidence ledger audit; `011`: project-evidence/exclusion ledger audit; `012`: completion-claim and approval-gate audit. Results are retained in the linked sections and validator artifacts named there.
- **Known limitation:** `009` excludes unknown alpha/media contexts; `010` and `011` verify ledger honesty, not implementation or project conformance; `012` records a pending gate.
- **Related decision:** No completion decision exists; earlier decision scopes remain unchanged.
- **Related prior requirements:** Theme and accessibility contrast requirements for `009`; all implementation-dependent requirements for `010`; `PRO`/`CUS` and project adoption rules for `011`; `KBDL-GOV-003` for `012`.
- **Packet destination (per-ID):** `009`–`012`: None — Approved methodology requirements.
- **Pending dependencies (per-ID):** `009`: none for opaque checks; `010`: implementation evidence; `011`: adopting-project evidence; `012`: planning-agent validation and explicit project-owner approval.
- **Profile impact:** No Profile-specific system is introduced; project evidence remains absent.
- **Future validation dependency:** Exactly the Class E/F evidence and completion approvals stated above.
- **Notes:** Candidate documentation readiness is not project completion.

## Notes on Scope

`GOV`, `PRN`, `FND`, `THM`, `MOT`, `RSP`, `A11Y`, and `CMP` are
documented (architecture and, where noted per row, approved default
values or approved WCAG/ARIA-derived requirements); none of their
requirements have been *implemented* in code, regardless of lifecycle
status — this matrix tracks specification-level approval and
validation, not implementation. `RSP` and `A11Y` (KBDL-006) **passed**
planning-agent validation before KBDL-007 began: `responsive.md` and
`accessibility.md` are present; every requirement directly restating an
already-adopted WCAG 2.2 criterion or prior approved KBDL rule remains
`Approved`; the nine KBDL-specific recommendations
(`KBDL-RSP-002`–`005`, `008`, `011`; `KBDL-A11Y-011`, `021`, `035`)
remain `Recommended` and unapproved — KBDL-006 passing validation does
**not** promote them. Implementation-dependent validation for both
modules remains `Not verified`, since no implementation exists.
[KBDL-DEC-015](decision-register.md#kbdl-dec-015--kbdl-006-remediation-and-id-governance-amendment)
exists and records exactly two things: acceptance of the KBDL-006
remediation baseline (commit `14ef110`), and the requirement-ID
governance amendment permitting stable IDs before approval. **It does
not approve any of the nine KBDL-006 recommendation values** — no
decision-register entry currently approves the responsive or
accessibility decision packets, and none of the nine recommendations is
`Approved`. `CMP` (KBDL-007) **passed** planning-agent validation before
KBDL-008 began: `docs/kbdl/components-core.md` exists with 51
documented requirements (see the
[KBDL-007 — Core Action, Form, and Navigation Components](#kbdl-007--core-action-form-and-navigation-components)
section above); its standards-derived and inherited Approved
requirements remain `Approved`; its ten KBDL-specific recommendations
(`KBDL-CMP-015`, `017`, `020`, `025`, `029`, `036`, `041`, `044`, `046`,
`048`) remain `Recommended` and unapproved — KBDL-007 passing
validation does not promote them. `CMP` (KBDL-008) **passed**
planning-agent validation before KBDL-009 began:
`docs/kbdl/components-system.md` exists with 60 additional documented
requirements (`KBDL-CMP-052`–`111`, see the
[KBDL-008 — Surface, Overlay, Feedback, and System-State Components](#kbdl-008--surface-overlay-feedback-and-system-state-components)
section above); its standards-derived and inherited Approved
requirements remain `Approved`; its seventeen KBDL-specific
recommendations
(`KBDL-CMP-067`, `069`, `073`, `074`, `076`, `080`, `083`, `085`, `089`,
`091`, `099`, `102`, `105`, `106`, `108`, `110`, `111`) remain
`Recommended` and unapproved — KBDL-008 passing validation does not
promote them. `PRO` (KBDL-009) is no longer a future or locked module:
`docs/kbdl/profiles.md` exists with 29 documented requirements
(`KBDL-PRO-001`–`029`, see the
[KBDL-009 — Project Profiles](#kbdl-009--project-profiles) section
above); KBDL-009 passed planning-agent validation before KBDL-010 began.
`CUS` (KBDL-010) is present with the requirements traced above and passed
planning-agent validation before KBDL-011 began. `VAL` (KBDL-011) is present
as the Final Validation and completion gate; its baseline and candidate status
remain pending independent planning-agent review and project-owner action.
Approval status and validation status are recorded independently
for every row; a row being `Approved` never implies it is `Verified`, and a
row being `Verified` never implies or grants `Approved` status. `PRN`
requirements are approved as principles-level guidance; they do not
themselves introduce or approve any final visual, motion, or component
value — those remain `Deferred` until their own modules are reached. `FND`
requirements cover both foundation *architecture* (`KBDL-FND-001`–`008`)
and the specific default values in the
[foundation decision packet](foundations/README.md#6-foundation-decision-packet)
(`KBDL-FND-009`–`012`); all twelve are `Approved` following the project
owner's review recorded in
[KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Approval does not itself constitute validation — see each row's
Validation status for what has actually been checked. `THM` requirements
were originally split more narrowly than `FND`, following KBDL-004-R1:
`Approved` only where a requirement's exact wording was directly and
explicitly supported by a prior approved KBDL decision —
`KBDL-THM-001`, `KBDL-THM-002`, `KBDL-THM-003` (narrowed to its
precedence core), `KBDL-THM-005` (narrowed to its accessibility core),
`KBDL-THM-006`, and `KBDL-THM-012a` (the pre-existing reduced-motion
rule). Under KBDL-004-A1, the project owner approved the ten-item theme
decision packet, promoting `KBDL-THM-004` (persistence baseline),
`KBDL-THM-007`/`008` (opaque light/dark mappings only — the Accent-
surface, Scrim, and Selection-background opacity values remain
`Recommended`/`Not verified` and are excluded), `KBDL-THM-009`
(status-family colors), `KBDL-THM-010` (opaque gradient caption-band
strategy only — translucent variants remain excluded), `KBDL-THM-011`
(color-value-expression convention), `KBDL-THM-012` (conceptual
transition guidance only, no timing/easing), `KBDL-THM-013` (detailed
precedence ordering), `KBDL-THM-014` (detailed project-override list),
and `KBDL-THM-015` (local-contrast-context set) to `Approved`, per
[KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).
This approval does not extend to opacity values, translucent variants,
account-level sync, high-contrast/forced-colors mode, data-visualization
palettes, any implementation-layer format (CSS custom properties, JSON
tokens, component-level theme tokens, framework APIs), or any motion
timing/easing value — all of which remain `Recommended`/`Not verified`
or out of scope, per
[themes/README.md § Theme Decision Packet](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1).
`MOT` requirements followed the same pattern as `THM` prior to KBDL-005-A1:
`Approved` only where a requirement directly restated an already-approved
KBDL-002 principle, KBDL-004 theme rule, or `KBDL-DEC-010` motion-safety
baseline (`KBDL-MOT-001`–`003`, `004`, `012`, `014`–`019`, `021`–`027`);
`Recommended` where new KBDL-005 policy was introduced — the motion
hierarchy and intensity model (`KBDL-MOT-005`, `006`), the timing/
duration/easing architecture (`KBDL-MOT-007`–`009`), spatial-movement and
choreography ranges (`KBDL-MOT-010`, `011`), navigation-motion
architecture (`KBDL-MOT-013`), the theme-transition duration/easing
values that resolve what KBDL-004 deferred (`KBDL-MOT-020`), and the
detailed defaults separated from their Approved parent cores under
KBDL-005-R1 — the entrance-versus-exit duration relationship
(`KBDL-MOT-028`), the attention repetition default (`KBDL-MOT-029`),
detailed ambient-motion boundaries (`KBDL-MOT-030`), detailed
scroll-linked-motion boundaries (`KBDL-MOT-031`), the reduced-motion
substitution matrix (`KBDL-MOT-032`), the conceptual motion-token
naming architecture (`KBDL-MOT-033`), and profile-level motion-intensity
adjustments (`KBDL-MOT-034`). `KBDL-MOT-006` and `KBDL-MOT-013` were
initially documented without a decision-packet row; KBDL-005-R2 added
packet items 14 and 15 to correct this coverage gap, completing a
fifteen-item packet mapping all sixteen `Recommended` requirements (see
[motion/README.md §10.2.1](motion/README.md#1021-approved-requirement-coverage) —
`KBDL-MOT-007` and `KBDL-MOT-008` share one decision, as one timing
system). Under **KBDL-005-A1**, the project owner approved exactly the
fifteen-item packet, recorded as
[KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),
promoting all sixteen requirements above from `Recommended` to
`Approved`. This approval does not extend to any item in
[motion/README.md §10.3](motion/README.md#103-unresolved-or-not-approval-ready)
(exact component-specific values, device-performance detection,
animation-library/rendering-technology selection, CSS/JSON/JavaScript
token formats, browser-support policy, exact scroll thresholds, exact
quantitative motion-hazard thresholds), any unresolved KBDL-004 theme
value, or any KBDL-006-or-later content — all of which remain
`Recommended`/`Not verified`/`Deferred` or out of scope. Approval does
not itself constitute validation — every promoted requirement's
Validation status above is unchanged. `RSP` and `A11Y` requirements
follow the same pattern established by `THM`/`MOT`: `Approved` only
where a requirement directly restates an already-adopted WCAG 2.2 Level
A/AA criterion (`KBDL-DEC-010`) or a prior approved KBDL principle,
foundation, theme, or motion rule; `Recommended` where new KBDL-006
policy is introduced — exact breakpoint thresholds, grid columns,
container widths, and gutters (`KBDL-RSP-002`–`005`), navigation
collapse thresholds and the data-dense strategy (`KBDL-RSP-008`,
`011`), the forced-colors/high-contrast policy (`KBDL-A11Y-011`), the
preferred enhanced target size (`KBDL-A11Y-021`), and the preferred
accessibility testing matrix (`KBDL-A11Y-035`). None of these
`Recommended` items are implemented or treated as `Approved` until the
project owner reviews the
[responsive decision packet](responsive.md#35-responsive-decision-packet)
and [accessibility decision packet](accessibility.md#49-accessibility-decision-packet);
`KBDL-DEC-015` exists, but it records only the acceptance of the
KBDL-006 remediation baseline and the requirement-ID governance
amendment — it does not approve either decision packet, and no
decision-register entry currently approves any of the nine KBDL-006
recommendation values, since no such review has yet occurred. This document does not claim full WCAG
conformance, screen-reader compatibility, or real-device support — see
[accessibility.md §48](accessibility.md#48-accessibility-validation-matrix)
for exactly what has and has not been verified. `CMP` requirements
follow the same pattern established by `RSP`/`A11Y`: `Approved` only
where a requirement directly restates an already-adopted WCAG 2.2 Level
A/AA criterion, WAI-ARIA role/state/property, or a prior approved KBDL
principle, foundation, theme, motion, responsive, or accessibility
rule; `Recommended` where new KBDL-007 component-level policy is
introduced — the button hierarchy taxonomy, icon-only visible-label
threshold, button-group guidance (`KBDL-CMP-015`, `017`, `020`), the
search-field model, combobox-justification threshold, form-action-row
reflow order (`KBDL-CMP-025`, `029`, `036`), and the navigation collapse
threshold, breadcrumb/pagination truncation models, and tabs activation
model (`KBDL-CMP-041`, `044`, `046`, `048`). None of these `Recommended`
items are implemented or treated as `Approved` until the project owner
reviews the
[KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet);
no decision-register entry has been created for KBDL-007, since no such
review has yet occurred. This document does not claim full WCAG
conformance, ARIA-pattern compliance, screen-reader compatibility, or
real-device support for any component — see
[components-core.md §32–§34](components-core.md#32-accessibility-validation-matrix)
for exactly what has and has not been verified. `CMP` requirements
introduced by KBDL-008 extend this pattern with one additional
authority: `Approved` where a requirement is authorized by an
already-adopted WCAG 2.2 criterion, an adopted WAI-ARIA role/state/
property definition, a prior approved KBDL or KBDL-007 rule, an
explicit mandatory requirement in the project-owner-approved KBDL-008
implementation prompt, or a documented combination of these (see each
requirement's own record in
[components-system.md §27](components-system.md#27-normative-requirements)
for which authority applies, split by clause where mixed); prompt
approval authorizes only the prompt's own mandatory scope — it does
not approve the KBDL-008 decision packet, promote any KBDL-006 or
KBDL-007 recommendation, or grant implementation-level validation.
`Recommended` where new, discretionary KBDL-008 component-level policy
not mandated by the approved prompt is introduced — a card-variant
taxonomy, an accordion open model, a
tooltip timing policy, a popover taxonomy, a menu interaction model, a
modal sizing/nesting policy, a drawer/sheet taxonomy, an overlay
nesting policy, a banner severity taxonomy, a toast lifecycle model, an
empty-state taxonomy, an error/system-state severity taxonomy, a
grid-versus-table threshold, a treegrid justification threshold, a
carousel auto-rotation policy, a data-visualization interaction model,
and a responsive transformation policy (`KBDL-CMP-067`, `069`, `073`,
`074`, `076`, `080`, `083`, `085`, `089`, `091`, `099`, `102`, `105`,
`106`, `108`, `110`, `111`). None of these `Recommended` items are
implemented or treated as `Approved` until the project owner reviews
the
[KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet);
no decision-register entry has been created for KBDL-008, since no such
review has yet occurred. This document does not claim full WCAG
conformance, ARIA-pattern compliance, screen-reader compatibility, or
real-device support for any component — see
[components-system.md §29–§32](components-system.md#29-accessibility-validation-matrix)
for exactly what has and has not been verified. `PRO` requirements
introduced by KBDL-009 follow the same pattern: `Approved` where a
requirement is authorized by a prior approved KBDL requirement, an
explicit mandatory requirement in the project-owner-approved KBDL-009
implementation prompt, or a documented combination of these (see each
requirement's own record in
[profiles.md §28](profiles.md#28-normative-requirements) for which
authority applies); prompt approval authorizes only the prompt's own
mandatory scope — it does not approve the KBDL-009 decision packet,
promote any KBDL-006, KBDL-007, or KBDL-008 recommendation, or grant
implementation-level validation. `Recommended` where new, discretionary
profile-governance policy not mandated by the approved prompt is
introduced — a primary/secondary/hybrid profile policy, exact Precision
density defaults, profile change/migration governance, a profile-
selection rubric, and a profile review cadence (`KBDL-PRO-009`, `016`,
`017`, `018`, `027`, `028`, `029`). None of these `Recommended` items
are implemented or treated as `Approved` until the project owner
reviews the
[KBDL-009 decision packet](profiles.md#33-kbdl-009-decision-packet);
no decision-register entry has been created for KBDL-009, since no such
review has yet occurred. This document does not claim implementation-
level profile validation or production conformance — see
[profiles.md §31–§32](profiles.md#31-profile-invariant-validation-matrix)
for exactly what has and has not been verified. KBDL-009 passed the
planning agent's validation review and KBDL-010 (Manual Customization) is
present with 30 `CUS` requirements. Its seven discretionary policy items
remain Recommended, its format/tooling item remains Deferred, and no
implementation-level customization behavior is verified. KBDL-010 passed
planning-agent review and KBDL-011 is present with twelve Approved, Verified
validation-methodology requirements. R5 returns `VAL-006` to Verified after
the effective readable-group-plus-ledger audit and independent validator pass;
`VAL-008`, `010`, and `011` remain Not verified. The documentation-only candidate is `PRODUCTION
READY` subject to independent planning-agent review.
Implementation conformance is
`NOT VERIFIED`, and completion awaits independent review and explicit
project-owner approval.
