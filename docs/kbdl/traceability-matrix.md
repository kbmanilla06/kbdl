# KBDL Traceability Matrix

Lifecycle status of this framework: `Approved`. Rows below reflect only
KBDL-001, KBDL-002, and KBDL-003 scope.

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

### Later modules (themes, motion, responsive, accessibility, components, profiles, customization, validation)

- **Blueprint section:** Later roadmap modules
- **Roadmap prompt:** KBDL-004 through KBDL-010
- **Requirement ID:** Not assigned
- **Specification location:** Planned locations only, see [README.md § Document Hierarchy](README.md#document-hierarchy)
- **Approval status:** Deferred
- **Validation status:** Not verified
- **Validation method:** Not applicable
- **Validation evidence:** Not applicable
- **Known limitation:** Not designed; intentionally out of scope for KBDL-003 and earlier steps. Principles and Visual foundations (formerly in this group) are now delivered — see the KBDL-002 and KBDL-003 rows.
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

### Recommended color, typography, spacing, and shape/elevation defaults (KBDL-FND-009 through KBDL-FND-012)

- **Blueprint section:** Foundation decision packet — recommended default values
- **Roadmap prompt:** KBDL-003
- **Requirement ID:** KBDL-FND-009, KBDL-FND-010, KBDL-FND-011, KBDL-FND-012
- **Specification location:** [foundations/README.md §6](foundations/README.md#6-foundation-decision-packet)
- **Approval status:** Recommended (not `Approved` — requires project-owner approval before authorizing implementation, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status))
- **Validation status:** Verified for the color-contrast calculations in [foundations/color.md §4](foundations/color.md#4-contrast-evidence-illustrative-not-a-theme-mapping) only; Not verified for all other aspects (typeface licensing, brand suitability, final spacing/corner/elevation values)
- **Validation method:** WCAG relative-luminance contrast calculation (completed for the color pairs listed); typeface-licensing verification and project-owner review (not yet performed).
- **Validation evidence:** Contrast-ratio table in [foundations/color.md §4](foundations/color.md#4-contrast-evidence-illustrative-not-a-theme-mapping), computed via a local dependency-free script (see the KBDL-003 validation evidence for the script and full output). Updated under KBDL-003-R1: `neutral-50` (3.25:1) was found to fail the 4.5:1 normal-text threshold and is now restricted to large-text/non-text-UI/decorative use only; a new `neutral-60` (5.59:1) was added and verified as the safe value for normal-sized secondary/tertiary text.
- **Known limitation:** These are recommendations awaiting project-owner approval; they must not be treated as `Approved` or implemented until that approval is recorded. The geometric character ("softened-structured") was corrected under KBDL-003-R1 from an incorrectly stated `Approved` label to `Recommended`.
- **Related decision:** Not applicable — pending a future decision-register entry once the project owner approves or amends the packet.
- **Notes:** This is the only KBDL-003 row whose approval status is `Recommended` rather than `Approved`; all other KBDL-003 rows restate `Approved` architecture from KBDL-001/002. See KBDL-003-R1 for the accessibility and lifecycle corrections applied to this row's underlying content.

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
requirements are approved as foundation *architecture* only; the specific
recommended default values in the
[foundation decision packet](foundations/README.md#6-foundation-decision-packet)
carry `Recommended` approval status, not `Approved`, until the project
owner reviews them.
