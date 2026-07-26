# KBDL Traceability Matrix

Lifecycle status of this framework: `Approved`. Rows below reflect only
KBDL-001, KBDL-002, KBDL-003, KBDL-004, and KBDL-005 scope.

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

Every row records:

- **Blueprint section** — The approved KBDL blueprint concept this row traces to.
- **Roadmap prompt** — The roadmap step (e.g. KBDL-001) that owns this row.
- **Requirement ID** — The requirement ID, if one has been assigned yet.
- **Specification location** — The file (and heading, where applicable) this concept lives in.
- **Approval status** — The lifecycle/approval label from [conventions.md §1.1](conventions.md#11-lifecycle--approval-status). Only `Approved` authorizes implementation.
- **Validation status** — The validation label from [conventions.md §1.3](conventions.md#13-validation-status): `Verified` or `Not verified`. Independent of approval status; `Verified` never implies `Approved`, and `Approved` never implies `Verified`.
- **Validation method** — How this requirement is or will be checked (for example manual review, link check, Markdown lint).
- **Validation evidence** — A concrete pointer to the evidence (a commit SHA, a named review, a tool's output), or `Not verified` if no validation has actually been performed yet. Evidence must never be the traceability matrix pointing at itself.
- **Known limitation** — Any known gap or caveat, or `None identified`.
- **Related decision** — Decision ID from the [decision register](decision-register.md), if applicable.
- **Notes** — Free text.

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
- **Specification location:** [governance.md](governance.md)
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
- **Requirement ID:** Not applicable
- **Specification location:** [decision-register.md § KBDL-DEC-004](decision-register.md#kbdl-dec-004--customization-is-manual-and-documented)
- **Approval status:** Approved
- **Validation status:** Not verified
- **Validation method:** Not applicable — no `CUS` requirements exist yet.
- **Validation evidence:** Not verified.
- **Known limitation:** Will require `CUS` requirements in a later step before it can be validated.
- **Related decision:** KBDL-DEC-004
- **Notes:** Out of scope for KBDL-001.

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
- **Requirement ID:** KBDL-GOV-001 (revised), KBDL-GOV-003 (revised)
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
- **Validation status:** Verified
- **Validation method:** Manual review confirming all nine principles include every required field (normative statement, purpose, required/prohibited behavior, profile interpretation, accessibility/responsive/motion implications, review questions) and that the nine required concepts (clarity before spectacle, precision, comprehension, hierarchy, controlled expression, consistency, adaptability, accessibility by default, performance) are all present.
- **Validation evidence:** Manual field-completeness review recorded in the KBDL-002 commit.
- **Known limitation:** None identified.
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
- **Validation status:** Verified
- **Validation method:** Manual review confirming all three categories (locked, controlled, open) address every element listed in this prompt's scope, and that no final ranges or values were introduced.
- **Validation evidence:** Manual scope-compliance review recorded in the KBDL-002 commit (see the scope-search evidence in the KBDL-002 final report).
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
- **Validation status:** Verified
- **Validation method:** Manual count and coverage review confirming at least six conforming examples spanning all three profiles, both themes, an expressive moment, a repeated workflow, and a mobile context; and at least eight non-conforming patterns each with reason, broken principle, risk, and correction.
- **Validation evidence:** Manual coverage review recorded in the KBDL-002 commit — six conforming examples and sixteen non-conforming patterns were produced, exceeding the required minimums.
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
- **Validation status:** Verified
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
- **Validation status:** Verified for the color-contrast calculations in [foundations/color.md §4](foundations/color.md#4-contrast-evidence-illustrative-not-a-theme-mapping) only; Not verified for all other aspects (typeface licensing of the eventual specific family, brand suitability beyond the tested pairs, final spacing/corner/elevation numeric values)
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
- **Specification location:** [themes/semantic-roles.md](themes/semantic-roles.md)
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
- **Specification location:** [themes/light-theme.md](themes/light-theme.md), [themes/dark-theme.md](themes/dark-theme.md)
- **Approval status:** Approved for the **opaque semantic mappings only** — per [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved); Accent-surface, Scrim, and Selection-background opacity remain `Recommended` and are explicitly excluded from this approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status)
- **Validation status:** Verified for every **opaque** contrast pair listed in [themes/validation.md § Consolidated Contrast Evidence](themes/validation.md#3-consolidated-contrast-evidence), each with an exact foreground, exact background, threshold, and result, no alpha compositing involved; Not verified for suitability beyond the tested pairs, and for the translucent-role opacity values (Accent-surface, Scrim, Selection-background — genuinely `Not verified`, no alpha-composite calculation performed) — these opacity values are explicitly excluded from the approval, per [themes/README.md §10.2](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1) items 1–2
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
- **Validation status:** Verified for the status-family contrast pairs (see [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence)) and for the **opaque** gradient caption-band substitute (`neutral-10` on fully opaque `neutral-100`, 17.17:1, directly correct — not a translucent/composited claim); Not verified for any translucent variant of the caption band, and for the color-value-expression convention (a documentation convention, not a testable claim)
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
- **Approval status:** `KBDL-MOT-004` Approved (structural completeness requirement); `KBDL-MOT-005` and `KBDL-MOT-006` Recommended (new KBDL-005 hierarchy and intensity-model architecture)
- **Validation status:** Not verified
- **Validation method:** Manual completeness review per category (performed); project-owner review of the hierarchy/intensity model (not yet performed).
- **Validation evidence:** Manual review recorded in [motion/validation.md §1](motion/validation.md#1-motion-validation-specification).
- **Known limitation:** Exceptional-level (Level 4) usage requires project-owner review each time; not yet exercised, since no implementation exists.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the motion decision packet. `KBDL-MOT-005` maps to [motion decision packet](motion/README.md#10-motion-decision-packet) item 1; `KBDL-MOT-006` maps to item 14 (added under KBDL-005-R2, which corrected the packet's initial omission of this requirement).
- **Notes:** The requirement that categories be documented completely is itself already supported by KBDL-002's visual-consistency principle; the specific five-level names and intensity factors are new.

### Timing, duration, and easing architecture (KBDL-MOT-007, KBDL-MOT-008, KBDL-MOT-009)

- **Blueprint section:** Semantic timing classes; duration recommendations; easing categories and exact curves
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-007, KBDL-MOT-008, KBDL-MOT-009
- **Specification location:** [motion/timing-easing.md §1, §2, §3](motion/timing-easing.md#1-timing-architecture)
- **Approval status:** Recommended (not `Approved` — requires project-owner approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status))
- **Validation status:** Not applicable — numerical and curve recommendations, not yet a testable implementation claim
- **Validation method:** Manual internal-consistency review (performed, see [motion/validation.md §2](motion/validation.md#2-numerical-consistency-review-performed)); project-owner review (not yet performed); implementation-level review once an implementation exists.
- **Validation evidence:** [motion/validation.md §2](motion/validation.md#2-numerical-consistency-review-performed) — every value has a stated purpose, exit durations are equal to or shorter than paired entrances, and no value is marked `Approved` or `Verified`.
- **Known limitation:** These are recommendations awaiting project-owner approval; must not be treated as `Approved` or implemented until that approval is recorded.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the motion decision packet. `KBDL-MOT-007` and `KBDL-MOT-008` together map to [motion decision packet](motion/README.md#10-motion-decision-packet) item 2 (one timing system); `KBDL-MOT-009` maps to item 3.
- **Notes:** Resolves the exact timing/easing KBDL-004 explicitly deferred (`KBDL-THM-012`); no CSS, JSON, or animation-library format is introduced.

### Spatial movement and choreography (KBDL-MOT-010, KBDL-MOT-011, KBDL-MOT-012)

- **Blueprint section:** Spatial-movement constraints; choreography and sequencing; entrance/exit behavior
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-010, KBDL-MOT-011, KBDL-MOT-012
- **Specification location:** [motion/foundations.md §6, §5, §7](motion/foundations.md#6-spatial-movement)
- **Approval status:** `KBDL-MOT-010` and `KBDL-MOT-011` Recommended (new consolidated architecture); `KBDL-MOT-012` Approved (directly restates safety/correctness priority already in `KBDL-PRN-002`)
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner review of the Recommended items (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Exact pixel/percentage movement and scale values are deferred to the Components module.
- **Related decision:** Not applicable
- **Notes:** The individual safety-relevant constraints (e.g., destructive actions must not rely on exit animation as confirmation) restate existing approved priorities; the consolidated spatial/choreography architecture is new.

### Interaction-category motion rules (KBDL-MOT-013 through KBDL-MOT-019)

- **Blueprint section:** Navigation continuity; loading/progress; direct manipulation; attention motion; ambient/continuous motion; scroll-linked motion; media motion
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-013, KBDL-MOT-014, KBDL-MOT-015, KBDL-MOT-016, KBDL-MOT-017, KBDL-MOT-018, KBDL-MOT-019
- **Specification location:** [motion/patterns.md §1–§7](motion/patterns.md#1-navigation-and-spatial-continuity)
- **Approval status:** `KBDL-MOT-013` Recommended (new navigation-motion architecture); `KBDL-MOT-014`, `KBDL-MOT-015`, `KBDL-MOT-016`, `KBDL-MOT-017`, `KBDL-MOT-018`, `KBDL-MOT-019` Approved — each directly restates an already-approved Technical Utility quality, accessibility requirement, locked component-state-clarity rule, or `KBDL-DEC-010` (WCAG 2.2 AA baseline)
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner review of `KBDL-MOT-013` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Exact repetition limits (attention motion) and scroll thresholds remain qualitative pending implementation-level review.
- **Related decision:** `KBDL-DEC-010` (for the media-motion autoplay prohibition and WCAG 2.2 AA baseline)
- **Notes:** The bounded-repetition limit for attention motion (2–3 repetitions) is a new `Recommended` numeric default within `KBDL-MOT-016`'s otherwise-Approved requirement; see [motion/README.md §10.2](motion/README.md#102-recommended-decisions--ready-for-approval) item 7. `KBDL-MOT-013` maps to [motion decision packet](motion/README.md#10-motion-decision-packet) item 15 (added under KBDL-005-R2, which corrected the packet's initial omission of this requirement).

### Theme-transition motion (KBDL-MOT-020)

- **Blueprint section:** Concrete duration/easing for the KBDL-004 theme-transition rules
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-020
- **Specification location:** [motion/patterns.md §8](motion/patterns.md#8-theme-transition-motion)
- **Approval status:** Recommended (the exact 150–250ms/Standard-easing values are new; the underlying non-blocking, readable, focus-preserving requirements are already `Approved` under `KBDL-THM-012`/`KBDL-THM-012a` and unaffected)
- **Validation status:** Not applicable — conceptual recommendation, not yet a testable implementation claim
- **Validation method:** Manual review of the worked example (performed); project-owner review (not yet performed).
- **Validation evidence:** [motion/patterns.md §8](motion/patterns.md#8-theme-transition-motion) — conceptually verified against the already-`Verified` opaque contrast pair (17.17:1, unrelated example) and the KBDL-004 non-blocking/readability requirements; no live implementation has been rendered or measured.
- **Known limitation:** No intermediate-frame contrast measurement has actually been performed against a live implementation.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the motion decision packet.
- **Notes:** This is the exact item KBDL-004's `KBDL-THM-012a` note deferred to KBDL-005; it does not reopen any approved KBDL-004 theme mapping.

### Interruption, recovery, and accessibility/performance requirements (KBDL-MOT-021 through KBDL-MOT-027)

- **Blueprint section:** Interruption/reversal/recovery; reduced-motion and no-motion parity; motion safety; performance requirements; mobile/input-method considerations; profile consistency; approval-gate governance
- **Roadmap prompt:** KBDL-005
- **Requirement ID:** KBDL-MOT-021, KBDL-MOT-022, KBDL-MOT-023, KBDL-MOT-024, KBDL-MOT-025, KBDL-MOT-026, KBDL-MOT-027
- **Specification location:** [motion/patterns.md §9](motion/patterns.md#9-interruption-reversal-and-recovery), [motion/accessibility-performance.md §1–§4](motion/accessibility-performance.md#1-reduced-motion-and-no-motion-parity), [motion/README.md §10](motion/README.md#10-motion-decision-packet)
- **Approval status:** Approved for all seven — each directly restates an already-approved safety/correctness priority, `KBDL-THM-012a` (reduced motion), `KBDL-DEC-010` (motion-safety baseline), Performance-Aware Enhancement (`KBDL-PRN-003`), Accessibility by Default, `KBDL-PRN-007` (profile consistency), or [conventions.md §1.1](conventions.md#11-lifecycle--approval-status) itself
- **Validation status:** Not verified (implementation-level); Not applicable for `KBDL-MOT-027` (a governance rule, not a testable claim)
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
- **Approval status:** Recommended for all seven — each is new KBDL-005 detail distinct from its already-`Approved` parent core (`KBDL-MOT-012`, `KBDL-MOT-016`, `KBDL-MOT-017`, `KBDL-MOT-018`, `KBDL-MOT-022`, and `KBDL-MOT-026` respectively; `KBDL-MOT-033` has no prior parent, since no earlier decision defines motion tokens)
- **Validation status:** Not verified (`KBDL-MOT-030`, `KBDL-MOT-031`, `KBDL-MOT-034`); Not applicable (`KBDL-MOT-028`, `KBDL-MOT-029`, `KBDL-MOT-032`, `KBDL-MOT-033` — numerical/documentation/naming recommendations, not yet testable implementation claims)
- **Validation method:** Manual review once implemented; project-owner review via the [motion decision packet](motion/README.md#10-motion-decision-packet) (not yet performed, items 6–9 and 11–13).
- **Validation evidence:** Not verified — no implementation exists yet; conceptual manual review recorded in [motion/validation.md](motion/validation.md) where applicable.
- **Known limitation:** These requirements exist specifically because KBDL-005's initial commit (`ea32ce3`) stated each parent core's exact detail (e.g., the 2–3 repetition default, the entrance/exit duration rule) inside an `Approved` section without its own `Recommended` lifecycle record — a mixed-scope defect corrected by KBDL-005-R1.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the motion decision packet.
- **Notes:** Splitting these out does not change any duration value, curve, movement range, hierarchy level, safety behavior, reduced-motion behavior, or profile recommendation — only the lifecycle bookkeeping.

## Notes on Scope

`GOV`, `PRN`, `FND`, `THM`, and `MOT` are documented (architecture and,
where noted per row, approved default values); none of their requirements
have been *implemented* in code, regardless of lifecycle status — this
matrix tracks specification-level approval and validation, not
implementation. Rows for `RSP`, `A11Y`, `CMP`, `PRO`, `CUS`, and `VAL`
exist only to show where their future requirements will be traced once
their roadmap step is reached; `RSP` (KBDL-006) specifically remains
locked until KBDL-005 passes validation and its proposed motion
decisions are approved. Approval status and validation status are recorded independently
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
`MOT` requirements follow the same pattern as `THM`: `Approved` only
where a requirement directly restates an already-approved KBDL-002
principle, KBDL-004 theme rule, or `KBDL-DEC-010` motion-safety baseline
(`KBDL-MOT-001`–`003`, `004`, `012`, `014`–`019`, `021`–`027`);
`Recommended` where new KBDL-005 policy is introduced — the motion
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
adjustments (`KBDL-MOT-034`). These sixteen `Recommended` requirements
each map to exactly one of the fifteen decisions in the
[motion decision packet](motion/README.md#10-motion-decision-packet)
(see [motion/README.md §10.2.1](motion/README.md#1021-recommended-requirement-coverage)
for the full mapping — `KBDL-MOT-007` and `KBDL-MOT-008` share one
decision, as one timing system). `KBDL-MOT-006` and `KBDL-MOT-013` were
initially documented without a decision-packet row; KBDL-005-R2 added
packet items 14 and 15 to correct this coverage gap. None of these
`Recommended` items are implemented or treated as `Approved` until the
project owner reviews the packet; no decision-register entry has been
created for KBDL-005, since no such review has yet occurred. KBDL-006
(Responsive and Accessibility) is locked until KBDL-005 passes
validation and its proposed motion decisions are approved, and has not
been started.
