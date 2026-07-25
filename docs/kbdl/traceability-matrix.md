# KBDL Traceability Matrix

Lifecycle status of this framework: `Approved`. Rows below reflect only
KBDL-001, KBDL-002, KBDL-003, and KBDL-004 scope.

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
- **Validation method:** Direct count of every role in the inventory against the actual light and dark mapping tables (re-run under KBDL-004-R1, not a re-assertion of the prior report).
- **Validation evidence:** Parity matrix in [themes/semantic-roles.md § Parity Matrix](themes/semantic-roles.md#parity-matrix-corrected-under-kbdl-004-r1) — 72 unique roles, 72 light mappings, 72 dark mappings, 2 role-level aliases, 0 unresolved; recorded in the KBDL-004-R1 commit. The re-run found and fixed one real defect: an inserted paragraph had broken the Status Families table in `light-theme.md §5`, orphaning its "Neutral status" row outside the table structure.
- **Known limitation:** None identified.
- **Related decision:** Not applicable
- **Notes:** The category-label wording error ("×5 sub-roles ×5 families") in the original parity matrix — which contradicted its own correct 4×6=24 total — is corrected under KBDL-004-R1; the total of 72 was independently re-verified, not merely preserved.

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
- **Approval status:** Recommended
- **Validation status:** Not verified
- **Validation method:** Manual review of the full precedence flow once implemented; project-owner review (not yet performed).
- **Validation evidence:** Not verified.
- **Known limitation:** Cannot be validated until an implementation exists, and requires project-owner approval first.
- **Related decision:** Not applicable
- **Notes:** Split out of the original `KBDL-THM-003` during KBDL-004-R1 because only two of the six levels are directly pre-approved.

### Persistence baseline (KBDL-THM-004, reclassified under KBDL-004-R1)

- **Blueprint section:** Theme preference persistence baseline
- **Roadmap prompt:** KBDL-004 (reclassified KBDL-004-R1)
- **Requirement ID:** KBDL-THM-004
- **Specification location:** [themes/README.md §7](themes/README.md#7-persistence-guidance)
- **Approval status:** Recommended — no prior approved KBDL decision specifically addresses theme-preference persistence; aligning with general accessibility/privacy principles does not by itself make this new baseline `Approved`
- **Validation status:** Not verified
- **Validation method:** Manual review of persistence design once implemented; project-owner review (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Cannot be validated until an implementation exists, and requires project-owner approval first.
- **Related decision:** Not applicable
- **Notes:** Previously mislabeled `Approved`; corrected under KBDL-004-R1.

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
- **Approval status:** Recommended
- **Validation status:** Not verified
- **Validation method:** Manual review of the override list once a project theme exists; project-owner review (not yet performed).
- **Validation evidence:** Not verified.
- **Known limitation:** Cannot be validated until a project theme exists, and requires project-owner approval first.
- **Related decision:** Not applicable
- **Notes:** Split out of the original `KBDL-THM-005` during KBDL-004-R1; this is new KBDL-004 policy, not a restatement of a prior decision.

### Local contrast contexts (KBDL-THM-015, new under KBDL-004-R1)

- **Blueprint section:** Named local-contrast-context set and nesting rules
- **Roadmap prompt:** KBDL-004-R1
- **Requirement ID:** KBDL-THM-015
- **Specification location:** [themes/adaptation.md §2](themes/adaptation.md#2-local-contrast-contexts)
- **Approval status:** Recommended
- **Validation status:** Not verified
- **Validation method:** Manual review of context usage against the defined set and rules once implemented; project-owner review (not yet performed).
- **Validation evidence:** Not verified.
- **Known limitation:** Cannot be validated until an implementation exists, and requires project-owner approval first.
- **Related decision:** Not applicable
- **Notes:** No prior KBDL decision defines local contrast contexts; this is new KBDL-004 architecture.

### Recommended light and dark theme mappings (KBDL-THM-007, KBDL-THM-008)

- **Blueprint section:** Light and dark theme semantic mappings
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-007, KBDL-THM-008
- **Specification location:** [themes/light-theme.md](themes/light-theme.md), [themes/dark-theme.md](themes/dark-theme.md)
- **Approval status:** Recommended (not `Approved` — requires project-owner approval, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status))
- **Validation status:** Verified for every contrast pair listed in [themes/validation.md § Consolidated Contrast Evidence](themes/validation.md#3-consolidated-contrast-evidence); Not verified for suitability beyond the tested pairs, and for the four translucent-role opacity values (Not verified pending an approved exact opacity)
- **Validation method:** WCAG relative-luminance contrast calculation via a local dependency-free script (completed); project-owner review (not yet performed).
- **Validation evidence:** [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence) — 52 pairs tested (updated count under KBDL-004-R1, including the gradient caption-band substitute), all passing their applicable threshold except 4 explicitly decorative-exempt borders/gridlines. The two Informational failures identified in the original KBDL-004 report (3.78:1, 4.21:1) are resolved by a revised hue (`#164499`), not carried forward as restrictions — see [adaptation.md §5.2](themes/adaptation.md#52-informational-correction-kbdl-004-r1).
- **Known limitation:** These are recommendations awaiting project-owner approval; must not be treated as `Approved` or implemented until that approval is recorded. The dark theme was independently designed, not inverted from light — see [dark-theme.md § Design Strategy](themes/dark-theme.md#design-strategy--why-some-roles-use-a-different-step-than-light-mode) for the `neutral-60`/`neutral-50` asymmetry this produced.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner reviews the theme decision packet.
- **Notes:** Uses only already-`Approved` KBDL-003 foundation colors (`neutral-*`, `accent-30`/`accent-50`); no new primitive hues were introduced for the light/dark base mapping.

### Status-family theme values, gradient strategy, and color-value expression (KBDL-THM-009, KBDL-THM-010, KBDL-THM-011)

- **Blueprint section:** Status-family theme colors; gradient strategy; color-value expression convention
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-009, KBDL-THM-010, KBDL-THM-011
- **Specification location:** [themes/adaptation.md §5, §4, §6](themes/adaptation.md#5-status-family-theme-behavior)
- **Approval status:** Recommended (extends the still-pending [color.md §3.3–§3.5](foundations/color.md#33-supporting-status-families) recommendations)
- **Validation status:** Verified for the status-family contrast pairs (see [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence)); Not verified for the gradient worked example and the color-value-expression convention (a documentation convention, not a testable claim)
- **Validation method:** WCAG contrast calculation (completed for status pairs); manual review (gradient, color-expression — not yet performed by the project owner).
- **Validation evidence:** [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence) for the recalculated pairs and [themes/adaptation.md §5.2](themes/adaptation.md#52-informational-correction-kbdl-004-r1) for the Informational correction record.
- **Known limitation:** New dark-mode status hues (`#7CC4FF`, `#6FD19A`, `#E0A840`, `#FF8A80`) were introduced here since the light-mode-only values from KBDL-003 fail contrast against a dark canvas; these dark hues are additionally new and unapproved, on top of the already-pending light-mode values. The light-mode Informational value was additionally revised to `#164499` under KBDL-004-R1 and now also awaits approval as part of this same pending item.
- **Related decision:** Not applicable
- **Notes:** Corrected under KBDL-004-R1: Informational no longer carries a large-text/icon restriction — the revised hue passes 4.5:1 in every context this family is used, in both modes.

### Theme-transition guidance (KBDL-THM-012, KBDL-THM-012a)

- **Blueprint section:** Theme-transition guidance (conceptual, no timing/easing); reduced-motion requirement
- **Roadmap prompt:** KBDL-004
- **Requirement ID:** KBDL-THM-012, KBDL-THM-012a
- **Specification location:** [themes/adaptation.md §7](themes/adaptation.md#7-theme-transition-guidance)
- **Approval status:** `KBDL-THM-012` Recommended; `KBDL-THM-012a` (reduced-motion) Approved — split under KBDL-004-R1 to resolve a contradiction where the document header previously claimed §7's "requirements" were `Approved` while §7's own status line said `Recommended`
- **Validation status:** Not verified
- **Validation method:** Manual review confirming no timing/easing values were introduced (performed); manual review confirming reduced-motion behavior once implemented.
- **Validation evidence:** Manual scope-compliance review recorded in the KBDL-004 commit — confirmed zero millisecond/easing values anywhere in `docs/kbdl/themes/`.
- **Known limitation:** Exact timing/easing depends entirely on KBDL-005, not yet reached.
- **Related decision:** KBDL-DEC-010 (for `KBDL-THM-012a`'s reduced-motion basis)
- **Notes:** Explicitly defers all durations and easing curves to Motion (KBDL-005). The lifecycle contradiction identified in KBDL-004 validation is resolved by this split.

## Notes on Scope

No requirement in this matrix outside `GOV`, `PRN`, and `FND` has been implemented,
designed, or validated. Rows for later roadmap modules exist only to show
where their future requirements will be traced once their roadmap step is
reached. Approval status and validation status are recorded independently
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
are split more narrowly than `FND`, following KBDL-004-R1: `Approved`
only where a requirement's exact wording is directly and explicitly
supported by a prior approved KBDL decision —
`KBDL-THM-001`, `KBDL-THM-002`, `KBDL-THM-003` (narrowed to its
precedence core), `KBDL-THM-005` (narrowed to its accessibility core),
`KBDL-THM-006`, and `KBDL-THM-012a` (the pre-existing reduced-motion
rule). Every other `THM` requirement is `Recommended` pending a future
project-owner decision — `KBDL-THM-004` (persistence baseline),
`KBDL-THM-007`–`012` (light/dark mappings, status-family colors,
gradient strategy, color-value-expression convention, and transition
guidance beyond reduced-motion), and the KBDL-004-R1-added
`KBDL-THM-013`–`015` (detailed precedence ordering, detailed project-
override list, and local-contrast-context set). Aligning with a general
KBDL principle does not by itself make a new policy `Approved`; see
[themes/README.md § Theme Decision Packet](themes/README.md#10-theme-decision-packet-restructured-under-kbdl-004-r1).
