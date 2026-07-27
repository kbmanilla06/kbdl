# KBDL Project Profiles

Lifecycle status: mixed. `Approved` for the requirements below whose
normative rule is authorized by a prior approved KBDL principle,
foundation, theme, motion, responsive, accessibility, KBDL-007, or
KBDL-008 requirement; an explicit mandatory clause in the project-owner-
approved KBDL-009 implementation prompt; or a documented combination of
these — see [§28](#28-normative-requirements) for the exact authority
cited per requirement. `Recommended` for genuinely new, discretionary
profile-governance policy not mandated by the approved prompt — pending
project-owner approval via [§33](#33-kbdl-009-decision-packet). No
`Recommended` value in this document authorizes implementation on its
own — see [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
Assigning a `KBDL-PRO-###` ID does not grant approval or implementation
authority, per the amended convention
([conventions.md §2](conventions.md#2-requirement-identification),
[KBDL-DEC-015](decision-register.md#kbdl-dec-015--kbdl-006-remediation-and-id-governance-amendment)).

This document does not claim implementation-level profile validation,
production conformance, or automated profile-selection tooling. No
coded profile variant exists yet. Documentation review does not make
any requirement's implementation behavior `Verified`.

Return to the [specification index](README.md).

## 1. Purpose and Scope

This document defines KBDL's framework-neutral Project Profile
specification: the shared architecture every profile inherits, the
locked/controlled/open classification of profile decisions, the
Showcase, Precision, and Flow profiles in operational detail, and how a
project selects, declares, and reviews its profile. It does not define
application code, coded theme variants, page templates, product
mockups, manual-customization rules, or final validation. It turns the
profile-level guidance already scattered across
[principles.md §9](principles.md#9-profile-level-interpretation),
[foundations/README.md §4](foundations/README.md#4-project-profile-adjustments--foundation-summary),
[themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation),
[motion/patterns.md §10](motion/patterns.md#10-profile-level-motion-interpretation),
[responsive.md §28–§30](responsive.md#28-showcase-profile-interpretation),
[accessibility.md §44](accessibility.md#44-profile-interpretation),
[components-core.md §30](components-core.md#30-normative-requirements)
(`KBDL-CMP-051`), and
[components-system.md §24](components-system.md#24-cross-component-composition-and-profile-compatibility)
(`KBDL-CMP-066`) into one coherent, cross-referenced specification.

## 2. Lifecycle and Validation Status

Uses KBDL's standard three-dimension model
([conventions.md §1](conventions.md#1-status-labels)). A requirement
may be `Approved` when its normative rule is authorized by a prior
approved KBDL requirement, an explicit mandatory clause in the
project-owner-approved KBDL-009 implementation prompt, or a documented
combination of these. Prompt approval authorizes only the prompt's own
mandatory scope; it does not approve the
[KBDL-009 decision packet](#33-kbdl-009-decision-packet). A genuinely
new, discretionary profile-selection, scoring, migration, or
profile-specific-defaults policy remains `Recommended`, `Unresolved`,
`Deferred`, or `Blocked` until the project owner reviews that packet.
Documentation review never justifies `Verified` validation status.

## 3. Relationship to Prior KBDL Modules

This module consolidates and operationalizes, without reopening:
KBDL-002's design-decision hierarchy, locked identity rules, and
profile-level interpretation (`KBDL-PRN-007`); KBDL-003's foundation
profile-adjustment summary (`KBDL-FND-008`); KBDL-004's theme
profile-consistency rule (`KBDL-THM-006`); KBDL-005's motion
profile-architecture and emphasis rules (`KBDL-MOT-026`,
`KBDL-MOT-034`); KBDL-006's responsive profile interpretation and
accessibility profile floor (`KBDL-A11Y-040`); KBDL-007's component
profile-consistency rule (`KBDL-CMP-051`); and KBDL-008's
cross-component-composition and profile-compatibility rule
(`KBDL-CMP-066`). Every value already `Approved` in an earlier module
remains `Approved` here without change; every value still `Recommended`
remains `Recommended` here (see
[§35](#35-kbdl-006-approval-boundary-audit)–[§37](#37-kbdl-008-approval-boundary-audit)).

## 4. Project Profile Terminology

- **Project Profile** — a documented KBDL configuration that adjusts
  emphasis, not foundations, for a category of project. KBDL's initial
  profiles are Showcase, Precision, and Flow. Tracked under module code
  `PRO`.
- **Profile emphasis** — the permitted variation in frequency,
  intensity, or composition of an already-approved controlled variable,
  used to express a profile's purpose without changing shared
  architecture or meaning.
- **Profile invariant** — a rule, value, or meaning that must hold
  identically across every profile (see [§9](#9-cross-profile-invariants)).
- **Profile declaration** — a project's documented record of its
  selected profile, selection rationale, and applicable requirements
  (see [§8](#8-profile-selection-and-declaration)).
- **Primary profile** — the profile a project treats as its dominant
  configuration. Whether every project must select exactly one is
  `Recommended`, not yet approved (see [§33](#33-kbdl-009-decision-packet)
  item 1).
- **Secondary profile** — a profile applied to a bounded portion of a
  project alongside its primary profile. Whether KBDL permits secondary
  profiles at all is `Recommended`, not yet approved.
- **Hybrid profile** — a project configuration blending emphasis from
  more than one profile without a documented single primary. Whether
  KBDL permits hybrid profiles, and any required precedence rule, is
  `Recommended`, not yet approved.
- **Profile fit** — the qualitative match between a project's
  documented characteristics (§8) and a profile's purpose; not a
  numeric score unless a future approval defines one.
- **Profile conflict** — a case where profile emphasis would require
  overriding a higher-priority concern in the design-decision hierarchy
  ([principles.md §8](principles.md#8-design-decision-hierarchy)); see
  [§24](#24-profile-conflicts-and-exception-handling).
- **Controlled variable** — an aspect of KBDL's design that a project
  profile may adjust only within explicitly documented bounds, as
  already defined in
  [principles.md §5.2](principles.md#52-controlled-visual-variables).
- **Locked rule** — a KBDL rule that cannot be modified by a project
  profile without an approved exception, as already defined in
  [principles.md §5.1](principles.md#51-locked-identity-rules).
- **Open brand expression** — an aspect of KBDL explicitly left open for
  a project to express its own brand identity, as already defined in
  [principles.md §5.3](principles.md#53-open-brand-expression).
- **Profile conformance** — the condition of a project's use of KBDL
  meeting every locked rule and every requirement applicable to its
  declared profile, assessed the same way as general KBDL conformance
  ([glossary.md](glossary.md), "Conformance").
- **Profile exception** — an approved, documented deviation from a
  locked or Approved rule for a specific project, following
  [governance.md § Exception process](governance.md#exception-process);
  none is created or approved by this document.

A Project Profile is explicitly **not**: a light/dark theme mode; a
brand identity; a user role, persona, or audience segment; an
accessibility preference (reduced motion, forced colors, and similar
remain independently user-controlled per
[accessibility.md](accessibility.md), never selected via profile); a
viewport class or device category; a feature flag; a product tier; a
manual customization; a component variant; or a runtime UI state. A
profile describes project-level emphasis and must not be treated as a
user-selectable accessibility or presentation preference unless
separately approved.

## 5. Profile Architecture

- **`KBDL-PRO-001`** — Showcase, Precision, and Flow **must** share one
  identity, principles, foundation, theme, motion, responsive,
  accessibility, and component architecture; a profile **must not**
  define a separate architecture in any of these areas.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates and consolidates the already-Approved `KBDL-PRN-007`, `KBDL-FND-008`, `KBDL-THM-006`, `KBDL-MOT-026`, `KBDL-A11Y-040`, `KBDL-CMP-051`, and `KBDL-CMP-066`, each of which independently requires shared architecture in its own module
  - Related requirement: `KBDL-PRN-007`, `KBDL-FND-008`, `KBDL-THM-006`, `KBDL-MOT-026`, `KBDL-A11Y-040`, `KBDL-CMP-051`, `KBDL-CMP-066`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-profile-architecture), [§9](#9-cross-profile-invariants).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-profile architecture review (performed for this document's own consistency, see implementation report).
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

- **`KBDL-PRO-002`** — A Project Profile **must** be treated as
  project-level emphasis, distinct from theme mode, brand identity,
  user role or persona, audience segment, accessibility preference,
  viewport class, device category, feature flag, product tier,
  component variant, and runtime UI state; a profile **must not** be
  presented as a user-selectable accessibility or presentation
  preference unless separately approved.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: the accessibility-preference distinction restates the already-Approved independence of reduced-motion and forced-colors preferences from any presentational grouping, [accessibility.md §44](accessibility.md#44-profile-interpretation); the complete terminology distinction is an explicit mandatory clause of the approved KBDL-009 prompt's Terminology section
  - Related requirement: `KBDL-A11Y-040`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§4](#4-project-profile-terminology).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual terminology-consistency review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 6. Shared Semantic and Accessibility Architecture

Every profile shares, without exception: KBDL identity
([principles.md §1](principles.md#1-identity-statement)); the nine core
principles ([principles.md §6](principles.md#6-core-principles)); the
design-decision hierarchy
([principles.md §8](principles.md#8-design-decision-hierarchy));
foundation role architecture and Approved default values
([foundations/README.md](foundations/README.md)); the theme
semantic-role inventory and Approved light/dark mappings
([themes/semantic-roles.md](themes/semantic-roles.md)); theme-selection
precedence ([themes/README.md](themes/README.md)); the motion hierarchy
and Approved timing/easing architecture
([motion/foundations.md](motion/foundations.md),
[motion/timing-easing.md](motion/timing-easing.md)); reduced-motion and
no-motion behavior
([motion/accessibility-performance.md](motion/accessibility-performance.md));
responsive content-priority logic
([responsive.md §4](responsive.md#4-responsive-content-priority)); the
WCAG 2.2 Level AA baseline
([KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety));
accessible semantics, keyboard behavior, focus behavior, and input
parity ([accessibility.md](accessibility.md),
[responsive.md §23](responsive.md#23-touch-pointer-keyboard-and-hybrid-input));
core component semantics and anatomy
([components-core.md](components-core.md)); surface, overlay, feedback,
and system-state meaning
([components-system.md](components-system.md)); and the security and
correctness requirements already established across those modules (see
[§23](#23-security-privacy-and-correctness)).

## 7. Locked, Controlled, and Open Profile Decisions

| Category | Examples | Rule |
| --- | --- | --- |
| Locked | Accessibility baseline; semantic roles; component meaning; focus behavior; input parity; reduced-motion parity; safety and data-integrity rules; Approved foundations; Approved theme architecture; Approved motion architecture; Approved responsive outcomes | Cannot be overridden by profile emphasis without an approved exception ([governance.md § Exception process](governance.md#exception-process)) |
| Controlled | Relative compositional scale; density emphasis; media prominence; motion-category frequency; surface hierarchy emphasis; information density; action prominence; feedback tone; use of approved local contrast contexts; frequency of expressive moments | May vary only within bounds already documented in the owning module ([principles.md §5.2](principles.md#52-controlled-visual-variables) and each module's own profile-interpretation section) |
| Open | Project brand name; project-specific imagery; illustration subject matter; editorial voice; domain-specific content; approved project accent selection; content-specific media | Project-owned, but must still satisfy every locked and Approved rule ([principles.md §5.3](principles.md#53-open-brand-expression)) |

- **`KBDL-PRO-003`** — Locked profile decisions **must not** be
  overridden by profile emphasis without an approved exception; a
  profile **must not** replace KBDL foundations, remove accessibility
  rules, change core interaction meaning, introduce inconsistent
  component anatomy, ignore reduced-motion behavior, or create an
  unrelated visual identity.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates [principles.md §9.4](principles.md#94-shared-constraints-across-profiles) and the design-decision hierarchy, [principles.md §8](principles.md#8-design-decision-hierarchy)
  - Related requirement: `KBDL-PRN-006`, `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-locked-controlled-and-open-profile-decisions).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review once a project profile is implemented.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

- **`KBDL-PRO-004`** — Profile-controlled variables **must** vary only
  within bounds already documented in their owning module; this
  document **must not** introduce a new controlled-variable bound not
  already approved elsewhere.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates [principles.md §5.2](principles.md#52-controlled-visual-variables) and the already-Approved per-module profile-interpretation sections cited in [§3](#3-relationship-to-prior-kbdl-modules)
  - Related requirement: `KBDL-PRN-005`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-locked-controlled-and-open-profile-decisions).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review once a project profile is implemented.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

- **`KBDL-PRO-005`** — Open brand expression **must** remain
  project-owned but subordinate to every locked and Approved rule.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates [principles.md §5.3](principles.md#53-open-brand-expression)
  - Related requirement: `KBDL-PRN-005`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-locked-controlled-and-open-profile-decisions).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review once a project profile is implemented.
  - Known limitation: Not applicable — restates an existing scope/governance rule, not independently testable against an implementation.

- **`KBDL-PRO-006`** — This document **must not** convert an unapproved
  earlier-module recommendation into an Approved, controlled profile
  variable.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not
    applicable.
  - Authority: scope-control requirement, explicit mandatory clause of the approved KBDL-009 prompt's Locked/Controlled/ Open section
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-locked-controlled-and-open-profile-decisions), [§35](#35-kbdl-006-approval-boundary-audit)–[§37](#37-kbdl-008-approval-boundary-audit).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual scope-compliance review (performed, see implementation report).
  - Known limitation: Not applicable — scope-control requirement, not independently testable against an implementation.

## 8. Profile Selection and Declaration

- **`KBDL-PRO-007`** — A project adopting KBDL **should** document a
  profile declaration recording: project name; product or experience
  category; dominant user tasks; dominant content type; expected task
  frequency; information density; workflow structure; primary device
  contexts; media importance; error and recovery criticality; selected
  profile; selection rationale; applicable profile requirements;
  approved exceptions; pending dependencies; validation status; and the
  date and owner of the declaration.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not applicable.
  - Authority: the required field list is an explicit mandatory clause of the approved KBDL-009 prompt's Profile Selection and Declaration section
  - Related requirement: `KBDL-PRO-001`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-profile-selection-and-declaration).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review of a project's declaration once one exists.
  - Known limitation: No project profile declaration exists yet to review against this requirement's field list.

- **`KBDL-PRO-008`** — A profile **must not** be selected solely because
  its name sounds desirable, its visual style appears more attractive,
  a team wants weaker density or accessibility constraints, a viewport
  is small or large, a user prefers light or dark mode, or a product
  uses one particular component.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not applicable.
  - Authority: explicit mandatory clause of the approved KBDL-009 prompt's Profile Selection and Declaration section; also extends the already-Approved Accessibility by Default principle, [principles.md §6.8](principles.md#68-accessibility-by-default)
  - Related requirement: `KBDL-PRO-002`, `KBDL-PRN-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-profile-selection-and-declaration).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review of a project's stated selection rationale.
  - Known limitation: No project profile declaration exists yet to review against this requirement.

Whether a project must select exactly one primary profile, may select a
secondary profile, or may use a hybrid model is new governance policy:

- **`KBDL-PRO-009`** — Adopt a policy on primary-profile exclusivity,
  secondary-profile permission, and any hybrid-profile precedence
  model.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-profile-selection-and-declaration), [§33](#33-kbdl-009-decision-packet) item 1.
  - Decision-packet destination: Approval-ready item 1
  - Pending dependencies: None.
  - Validation method: Project-owner review (not yet performed).
  - Known limitation: Recommended — grants no implementation authority pending project-owner review; see the decision packet.

- **`KBDL-PRO-028`** — Adopt a qualitative profile-selection rubric
  (project characteristics to profile fit) that does not rely on a
  numeric score.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-007`, `KBDL-PRO-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-profile-selection-and-declaration), [§33](#33-kbdl-009-decision-packet) item 4.
  - Decision-packet destination: Approval-ready item 4
  - Pending dependencies: None.
  - Validation method: Project-owner review (not yet performed).
  - Known limitation: Recommended — grants no implementation authority pending project-owner review; see the decision packet.

## 9. Cross-Profile Invariants

Every profile preserves, without exception: identity, principles, and
the design-decision hierarchy (`KBDL-PRO-001`, `003`); foundation role
architecture and Approved values (`KBDL-FND-008`); the theme
semantic-role inventory and parity rules (`KBDL-THM-006`); the motion
hierarchy, timing/easing architecture, and reduced/no-motion parity
(`KBDL-MOT-026`); responsive content-priority logic and Approved
outcomes; the complete WCAG 2.2 AA baseline (`KBDL-A11Y-040`); core
component semantics and anatomy (`KBDL-CMP-051`); and system-component
semantics, focus models, modality, status meaning, and recovery
behavior (`KBDL-CMP-066`). No profile may weaken any of these; profile
differences are limited to the permitted emphasis documented per module
and consolidated in [§10](#10-showcase-profile)–[§12](#12-flow-profile).

## 10. Showcase Profile

### 10.1 Purpose

For portfolios, creative showcases, editorial storytelling, campaign-
like moments, and media-led presentation.

- **`KBDL-PRO-010`** — Showcase **must** emphasize editorial content
  hierarchy, media as structural content, large compositional gestures,
  deliberate typographic contrast, generous spatial rhythm, and
  controlled expressive moments, while preserving reading and viewing
  comfort, a clear primary message and action, motion that settles
  during consumption, stable navigation, accessible media treatment,
  and responsive content order.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: consolidates the already-Approved Showcase interpretation already established in [principles.md §9.1](principles.md#91-showcase-profile), [foundations/README.md §4.1](foundations/README.md#41-showcase), [themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation) Showcase, [motion/patterns.md §10.1](motion/patterns.md#101-showcase), and [responsive.md §28](responsive.md#28-showcase-profile-interpretation)
  - Related requirement: `KBDL-PRO-001`, `KBDL-MOT-034`.
  - Applicable profiles: Showcase.
  - Specification location: [§10.1](#101-purpose).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-module consistency review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

### 10.2 Component Interpretation

- **`KBDL-PRO-013`** — Showcase **may** emphasize media-forward Cards
  and Panels, editorial navigation composition, and project or gallery
  presentation using only existing Approved component semantics;
  Showcase **must not** create separate component anatomy, use a Card
  variant whose lifecycle is not Approved, depend on hover-only
  actions, allow media surfaces to replace semantic headings or
  navigation, treat tooltips as accessible names, or use carousels
  without their full Approved accessibility behavior.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not
    verified.
  - Authority: restates the already-Approved `KBDL-CMP-051`, `KBDL-CMP-066`, `KBDL-CMP-055` hover-independent- discoverability prohibition, `KBDL-CMP-072` tooltip-naming- independence rule, and `KBDL-CMP-107` carousel pause/stop/hide requirement
  - Related requirement: `KBDL-CMP-051`, `KBDL-CMP-055`, `KBDL-CMP-066`, `KBDL-CMP-072`, `KBDL-CMP-107`.
  - Applicable profiles: Showcase.
  - Specification location: [§10.2](#102-component-interpretation).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual component-composition review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

Any exact Showcase card-variant or composition default remains new
policy:

- **`KBDL-PRO-016`** — Adopt exact Showcase composition and
  component-emphasis defaults (which Card variant, media relationship,
  and navigation composition Showcase uses by default).
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-013`, `KBDL-CMP-067`.
  - Applicable profiles: Showcase.
  - Specification location: [§10.2](#102-component-interpretation), [§34](#34-approval-ready-versus-contingent-decisions) (contingent).
  - Decision-packet destination: Contingent — [§33.3](#333-unresolved-or-not-approval-ready); not independently approval-ready
  - Pending dependencies: `KBDL-CMP-067` (KBDL-008) — blocking.
  - Validation method: Project-owner review (not yet performed); not independently approvable until `KBDL-CMP-067` is approved.
  - Known limitation: Contingent on the unapproved KBDL-008 `KBDL-CMP-067`; cannot be approved independently through the KBDL-009 packet until `KBDL-CMP-067` is approved or replaced.

## 11. Precision Profile

### 11.1 Purpose

For SaaS dashboards, administration tools, operational interfaces,
repeated workflows, data review, and information-dense applications.

- **`KBDL-PRO-011`** — Precision **must** emphasize fast scanning,
  information and state hierarchy, repeated-workflow efficiency,
  predictable navigation, clear state presentation, readable density,
  alignment and structural precision, low visual noise, performance,
  error visibility, and data stability.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: consolidates the already-Approved Precision interpretation in [principles.md §9.2](principles.md#92-precision-profile), [foundations/README.md §4.2](foundations/README.md#42-precision), [themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation) Precision, [motion/patterns.md §10.2](motion/patterns.md#102-precision), and [responsive.md §29](responsive.md#29-precision-profile-interpretation)
  - Related requirement: `KBDL-PRO-001`, `KBDL-MOT-034`.
  - Applicable profiles: Precision.
  - Specification location: [§11.1](#111-purpose).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-module consistency review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

### 11.2 Component Interpretation

- **`KBDL-PRO-014`** — Precision **may** emphasize Static Data Tables,
  Interactive Grids where genuinely justified, compact action
  composition, persistent system state, and accessible data
  visualizations using only existing Approved component semantics;
  Precision **must not** reduce target sizes below the Approved
  minimum, replace native tables with grids for styling alone, hide
  critical actions behind hover, or weaken focus, status, or error
  communication.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates the already-Approved `KBDL-CMP-051`, `KBDL-CMP-066`, `KBDL-CMP-010` WCAG 24×24 target- size minimum, `KBDL-CMP-070` native-table/grid-misuse prohibition, and `KBDL-CMP-055` hover-independent-discoverability prohibition
  - Related requirement: `KBDL-CMP-010`, `KBDL-CMP-051`, `KBDL-CMP-055`, `KBDL-CMP-066`, `KBDL-CMP-070`.
  - Applicable profiles: Precision.
  - Specification location: [§11.2](#112-component-interpretation).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None blocking; `KBDL-CMP-105`, `KBDL-RSP-011` cited as unapproved context only, not adopted as authority.
  - Validation method: Manual component-composition review. This requirement does not adopt the pending grid-versus-table threshold (`KBDL-CMP-105`) or data-dense transformation strategy (`KBDL-RSP-011`) as authority — both remain cited only as unapproved context (see [§37](#37-kbdl-008-approval-boundary-audit)).
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

Any exact Precision density or component-variant default remains new
policy:

- **`KBDL-PRO-017`** — Adopt exact Precision density and
  component-emphasis defaults (compact spacing intensity, default table
  presentation, and action-composition density Precision uses by
  default).
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-014`.
  - Applicable profiles: Precision.
  - Specification location: [§11.2](#112-component-interpretation), [§33](#33-kbdl-009-decision-packet) item 2.
  - Decision-packet destination: Approval-ready item 2
  - Pending dependencies: None blocking; `KBDL-RSP-002`, `KBDL-RSP-003` cited as unapproved context only for the eventual exact grid-interaction point, not required for this item's own approval.
  - Validation method: Project-owner review (not yet performed).
  - Known limitation: Recommended — grants no implementation authority pending project-owner review; see the decision packet.

## 12. Flow Profile

### 12.1 Purpose

For consumer-facing web applications, checkout-style experiences,
onboarding, account setup, guided transactions, and progressive
workflows.

- **`KBDL-PRO-012`** — Flow **must** emphasize approachability, consumer
  comprehension, one clear next step, guided progression, reassuring
  feedback, recovery visibility, responsive simplicity, trust, plain
  language, immediate action acknowledgment, and balanced expression.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: consolidates the already-Approved Flow interpretation in [principles.md §9.3](principles.md#93-flow-profile), [foundations/README.md §4.3](foundations/README.md#43-flow), [themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation) Flow, [motion/patterns.md §10.3](motion/patterns.md#103-flow), and [responsive.md §30](responsive.md#30-flow-profile-interpretation)
  - Related requirement: `KBDL-PRO-001`, `KBDL-MOT-034`.
  - Applicable profiles: Flow.
  - Specification location: [§12.1](#121-purpose).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-module consistency review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

### 12.2 Component Interpretation

- **`KBDL-PRO-015`** — Flow **may** emphasize clear action sequences,
  field guidance, progress indicators, error summaries, reassuring
  feedback, empty and no-results recovery, and mobile-friendly surfaces
  using only existing Approved component semantics; Flow **must not**
  change field, action, or navigation semantics, or present critical
  information only in a transient Toast.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates the already-Approved `KBDL-CMP-051`, `KBDL-CMP-066`, and `KBDL-CMP-090` toast critical-information-persistence requirement
  - Related requirement: `KBDL-CMP-051`, `KBDL-CMP-066`, `KBDL-CMP-090`.
  - Applicable profiles: Flow.
  - Specification location: [§12.2](#122-component-interpretation).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None blocking; `KBDL-CMP-015`, `KBDL-CMP-036` cited as unapproved context only, not adopted as authority.
  - Validation method: Manual component-composition review. This requirement does not adopt the pending button-hierarchy (`KBDL-CMP-015`) or form-action-row-ordering (`KBDL-CMP-036`) recommendations as authority for Flow's action sequences — both remain cited only as unapproved context (see [§36](#36-kbdl-007-approval-boundary-audit)).
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

Any exact Flow action-hierarchy or workflow-component default remains
new policy:

- **`KBDL-PRO-018`** — Adopt exact Flow action-progression and
  workflow-component defaults (default action-sequence composition and
  progress-indicator treatment Flow uses by default).
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-015`, `KBDL-CMP-015`, `KBDL-CMP-036`.
  - Applicable profiles: Flow.
  - Specification location: [§12.2](#122-component-interpretation), [§34](#34-approval-ready-versus-contingent-decisions) (contingent).
  - Decision-packet destination: Contingent — [§33.3](#333-unresolved-or-not-approval-ready); not independently approval-ready
  - Pending dependencies: `KBDL-CMP-015`, `KBDL-CMP-036` (KBDL-007) — blocking.
  - Validation method: Project-owner review (not yet performed); not independently approvable until `KBDL-CMP-015`/`036` are approved.
  - Known limitation: Contingent on the unapproved KBDL-007 `KBDL-CMP-015`/`036`; cannot be approved independently through the KBDL-009 packet until those are approved or replaced.

## 13. Cross-Profile Comparison Matrix

| Dimension | Showcase | Precision | Flow |
| --- | --- | --- | --- |
| Intended project category | Portfolios, creative showcases | SaaS dashboards, operational tools | Consumer applications, guided workflows |
| Dominant user goal | Consumption, impression | Task completion, monitoring | Transaction completion |
| Dominant content type | Editorial, media | Data, state | Guided steps, forms |
| Task frequency | Low-to-moderate, browsing | High, repeated | Moderate, occasional |
| Information density | Low-to-moderate | High | Low-to-moderate |
| Media prominence | High | Low | Low-to-moderate |
| Composition | Large, editorial gestures | Compact, aligned | Simplified, linear |
| Navigation emphasis | Stable, exploratory | Persistent, predictable | Linear, progressive |
| Action emphasis | Singular, clear primary | Efficient, repeated | Single next step |
| Feedback emphasis | Editorial confirmation | Immediate, precise | Reassuring, explicit |
| Error/recovery emphasis | Standard recovery | High visibility, fast | Guided, reassuring recovery |
| Foundation emphasis | Display type, richer media | Compact spacing, tabular figures | Comfortable spacing, friendly type |
| Theme emphasis | Richer accents, inverse contexts | Restrained accents, strong hierarchy | Approachable, reassuring |
| Motion emphasis | Expressive reveals | Immediate, compact | Approachable, gentle continuity |
| Responsive emphasis | Media hierarchy, full-bleed | Density, persistent nav | Simplification, single action |
| Component emphasis | Media-forward Cards | Tables/Grids, compact actions | Action sequences, progress |
| Content tone | Editorial | Scannable, precise | Reassuring, plain |
| Performance sensitivity | Bounded high-impact cost | Low cost, always | Low cost for guided actions |
| Shared locked constraints | Identical across all three (§9) | Identical across all three (§9) | Identical across all three (§9) |
| Pending decisions | `KBDL-PRO-016` | `KBDL-PRO-017` | `KBDL-PRO-018` |
| Validation method | Manual cross-module review | Manual cross-module review | Manual cross-module review |

This matrix shows differences in emphasis only; no row implies a
separate architecture, and no numeric score is assigned unless
explicitly marked `Recommended` above.

## 14. Principles Mapping

| Principle | Shared requirement | Showcase emphasis | Precision emphasis | Flow emphasis | Prohibited interpretation |
| --- | --- | --- | --- | --- | --- |
| Clarity Before Spectacle | No addition may reduce comprehension | Stronger gestures, message stays unmistakable | Spectacle rare; clarity dominates | Spectacle sparing, reinforces success | Any profile treating spectacle as the primary goal |
| Precision and Intentionality | Every relationship traceable to a rule | Governs large compositions as strictly as small | Especially visible in dense layouts | Supports trustworthiness in guided flows | "Eyeballing" layout in any profile |
| Consumer Comprehension | Plain language, familiar patterns | Governs creative framing, not just controls | Complex data explained in consumer terms | Guided flows assume no prior knowledge | Developer jargon in any profile |
| Consistent System Behavior | Same interaction meaning everywhere | Interaction meaning constant despite expression | Critical for efficient repeated use | Builds trust for guided conversion | Same control behaving differently by profile |
| Visual Hierarchy | One unambiguous primary element | Foregrounds creative/editorial content | Foregrounds relevant data/action | Foregrounds the single next action | Multiple equal focal points in any profile |
| Controlled Expression | Expression stays within controlled variables | Uses upper documented range | Uses lower documented range | Uses balanced middle range | Bespoke, ungoverned effects in any profile |
| Adaptability Without Fragmentation | Same principles/rules across profiles | Adapts via compositional/editorial emphasis | Adapts via density/hierarchy emphasis | Adapts via approachability/progression emphasis | Profile-specific component anatomy or accessibility exception |
| Accessibility by Default | Applies to every decision, every profile | Editorial layouts remain fully accessible | Dense data remains fully accessible | Guided flows remain fully accessible | Treating accessibility as optional in any profile |
| Performance-Aware Enhancement | Cost weighed before adoption | Higher cost accepted only for bounded moments | Cost stays low, used intensively | Cost stays low for guided actions | Unbounded expensive effects in any profile |

- **`KBDL-PRO-019`** — Every profile **must** map to, and **must not**
  reinterpret into its opposite, each of the nine core KBDL principles
  in [principles.md §6](principles.md#6-core-principles).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates the already-Approved `KBDL-PRN-003`, extended explicitly to per-profile mapping
  - Related requirement: `KBDL-PRN-003`, `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14](#14-principles-mapping).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual principle-by-principle review using each principle's review questions ([principles.md §6](principles.md#6-core-principles)).
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 15. Foundation Mapping

| Area | Shared architecture | Approved values (unchanged) | Permitted emphasis | Prohibited fragmentation |
| --- | --- | --- | --- | --- |
| Color roles | One semantic role set | Neutral/accent/status families | Frequency of accent/status use | New profile-only colors |
| Typography roles | One type-role set and scale | Type scale, tabular-figure strategy | Display-role prominence (Showcase), tabular emphasis (Precision) | New profile-only type scale |
| Spacing and layout | One spacing scale and grid principle | 8-step modular scale | Density/generosity within the scale | New profile-only spacing values |
| Shape and corner | One corner-classification system | 5-step named corner system | Corner-character frequency | New profile-only radii |
| Elevation and depth | One elevation scale | 5-level semantic elevation scale | Surface-drama intensity (§3.5 of shape-depth.md) | New profile-only elevation values |
| Iconography | One icon strategy | Stroke-based, consistent optical size | Icon-use frequency | New profile-only icon sizes |
| Imagery and media | One media-treatment logic | Named aspect-treatment set | Media prominence and richness | New profile-only aspect ratios |

No area above introduces a new color, type scale, spacing value, radius,
elevation value, icon size, or media aspect ratio; see `KBDL-FND-008`
and [foundations/README.md §4](foundations/README.md#4-project-profile-adjustments--foundation-summary)
for the existing per-area detail this table consolidates.

## 16. Theme Mapping

- A profile is independent of light, dark, or automatic mode; a
  project has exactly one profile under any supported theme mode.
- Every profile consumes the same semantic-role inventory
  ([themes/semantic-roles.md](themes/semantic-roles.md)).
- Theme parity ([themes/semantic-roles.md §2](themes/semantic-roles.md#2-semantic-parity))
  applies equally across profiles.
- Profile emphasis may change use *frequency* of a role, never its
  *meaning*.
- User theme preference remains independent of profile selection.
- A profile must not alter theme-selection precedence
  ([themes/README.md](themes/README.md)).
- Project-controlled theme variation remains governed by the existing
  theme module and any later customization module.
- This document does not define profile-only themes and does not
  approve pending opacity, translucent-variant, forced-colors, or
  data-visualization-palette guidance.

This section restates the already-Approved `KBDL-THM-006` and the
Showcase/Precision/Flow theme-interpretation text in
[themes/README.md §8](themes/README.md#8-project-profile-theme-interpretation)
without change.

## 17. Motion Mapping

Per profile, using the already-Approved motion hierarchy and shared
timing/easing architecture: Showcase emphasizes expressive reveals,
editorial sequencing, richer media motion, selective shared-element
continuity, controlled ambient moments, and stronger branded
choreography, while preserving reading stability, user control,
reduced-motion parity, fast navigation access, bounded continuous
motion, and stable focus. Precision emphasizes immediate feedback,
short state transitions, efficient data updates, predictable
navigation, minimal ambient motion, and compact choreography, while
preserving scanning speed, workflow efficiency, data stability, state
clarity, low visual noise, and performance. Flow emphasizes
approachable transitions, reassuring feedback, clear progress, gentle
spatial continuity, and balanced expressive moments, while preserving
predictable progression, trust, error recovery, mobile clarity,
immediate action acknowledgment, and motion safety. No profile defines
a separate timing scale, easing curve, exact duration, exact distance,
exact scale range, exact stagger, or motion-frequency quota — these
already-Approved constraints restate `KBDL-MOT-026` and `KBDL-MOT-034`
([motion/patterns.md §10](motion/patterns.md#10-profile-level-motion-interpretation))
without change. Any new exact profile motion-frequency policy belongs
in the decision packet (see [§39](#39-deferred-and-unresolved-items)).

## 18. Responsive Mapping

All profiles preserve content-driven adaptation, source and reading
order, focus order, reflow, text resizing, orientation flexibility,
safe areas, virtual-keyboard visibility, input parity, semantic
continuity, and error/recovery access
([responsive.md](responsive.md)). Showcase may prioritize media
hierarchy, editorial sequence, and full-bleed or asymmetric composition
where Approved outcomes remain satisfied
([responsive.md §28](responsive.md#28-showcase-profile-interpretation)).
Precision may prioritize data scanning, action access, state
visibility, and task-context preservation
([responsive.md §29](responsive.md#29-precision-profile-interpretation)).
Flow may prioritize step progression, primary-action visibility, error
recovery, and mobile simplicity
([responsive.md §30](responsive.md#30-flow-profile-interpretation)).
This document does not prescribe the still-pending exact breakpoints,
grid columns, gutters, containers, navigation-collapse threshold, or
data-dense transformation strategy (`KBDL-RSP-002`–`005`, `008`, `011`)
— see [§35](#35-kbdl-006-approval-boundary-audit).

## 19. Accessibility Mapping

The complete accessibility specification
([accessibility.md](accessibility.md)) applies equally to every
profile without exception, per the already-Approved `KBDL-A11Y-040`
([accessibility.md §44](accessibility.md#44-profile-interpretation)).
No profile may change the WCAG 2.2 AA baseline, semantic structure,
accessible naming, keyboard support, focus behavior, the target-size
minimum, pointer cancellation, gesture alternatives, reflow, text
resizing, contrast, status communication, authentication accessibility,
error identification, error prevention, reduced-motion requirements, or
media alternatives. Profile emphasis may improve an accessibility
outcome but may never lower it. This document does not present the
still-pending 44×44 enhanced-target-size preference
(`KBDL-A11Y-021`), forced-colors policy (`KBDL-A11Y-011`), or preferred
testing matrix (`KBDL-A11Y-035`) as Approved.

## 20. Core-Component Mapping

Every KBDL-007 component family (Buttons, Icon Buttons, Toggle Buttons,
Links, Button Groups, Disclosure/Menu triggers, Text Inputs, Password
Inputs, Search Fields, Textareas, Selects, Comboboxes, Checkboxes,
Radio Groups, Switches, File Inputs, Field Groups, Form Action Rows,
Skip Links, Global/Local Navigation, Breadcrumbs, Tabs, Pagination, and
Back Links) shares its semantic contract, accessibility contract, and
anatomy across all three profiles unchanged, per the already-Approved
`KBDL-CMP-051`. Profiles may adjust visual emphasis, density, and
composition frequency for these components (see
[§10.2](#102-component-interpretation)–[§12.2](#122-component-interpretation))
but never their semantics or anatomy. This document does not define a
profile-specific component variant as Approved unless a future
project-owner approval makes it a mandatory clause independent of a
pending earlier requirement — see [§36](#36-kbdl-007-approval-boundary-audit)
for the ten pending KBDL-007 recommendations this document does not
adopt.

- **`KBDL-PRO-020`** — KBDL-007 core-component semantics and anatomy
  **must** remain unchanged and identical across Showcase, Precision,
  and Flow.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates and extends the already- Approved `KBDL-CMP-051` explicitly to this module's own mapping
  - Related requirement: `KBDL-CMP-051`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20](#20-core-component-mapping).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-profile component-semantics review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 21. System-Component Mapping

Every KBDL-008 component family (Container Surface, Panel, Card,
Accordion, Data Table, Tooltip, Popover, Menu, Listbox, Dialog, Modal
Dialog, Alert Dialog, Drawer and Sheet, Inline Feedback, Alert, Banner,
Toast/Snackbar, Status/Log, Badge, Progress Indicator, Meter, Skeleton,
Loading/Empty/No-Results/Error/Offline/Permission-Denied/Not-Found/
Maintenance-and-Degraded states, System Status, Interactive Grid, Tree
and Treegrid, Carousel, and Data Visualization) shares its architecture,
focus model, modality, status meaning, and recovery behavior across all
three profiles unchanged, per the already-Approved `KBDL-CMP-066`.
Profiles may adjust emphasis (see
[§10.2](#102-component-interpretation)–[§12.2](#122-component-interpretation))
but never these profile-independent safety and accessibility rules.
This document does not silently select or approve any of the
seventeen pending KBDL-008 policies — see
[§37](#37-kbdl-008-approval-boundary-audit).

- **`KBDL-PRO-021`** — KBDL-008 system-component semantics, focus
  models, modality, status meaning, and recovery behavior **must**
  remain unchanged and identical across Showcase, Precision, and Flow.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates and extends the already- Approved `KBDL-CMP-066` explicitly to this module's own mapping
  - Related requirement: `KBDL-CMP-066`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§21](#21-system-component-mapping).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual cross-profile component-semantics review.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 22. Content and Communication Considerations

- **`KBDL-PRO-022`** — Every profile **must** use plain language,
  purpose-specific actions, clear labels, explicit errors, safe
  diagnostic language, honest system-state claims, consistent
  terminology, accessible instructions, and non-color-dependent status
  communication; a profile's content-tone emphasis (editorial,
  scannable, or reassuring) **must not** create separate semantics or
  weaker error disclosure.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not
    verified.
  - Authority: restates the already-Approved Consumer Comprehension principle, [principles.md §6.3](principles.md#63-consumer-comprehension), and the already-Approved `KBDL-CMP-101`/`103` honest-system-state- communication rules
  - Related requirement: `KBDL-PRN-003`, `KBDL-CMP-101`, `KBDL-CMP-103`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22](#22-content-and-communication-considerations).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual content review. Showcase may emphasize editorial storytelling and project narrative; Precision may emphasize scannable labels and operational precision; Flow may emphasize reassuring instructions and recovery guidance — none of these emphases changes the shared requirements above.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 23. Security, Privacy, and Correctness

- **`KBDL-PRO-023`** — No profile **may** use visual emphasis as
  authorization, hide a restricted action as the sole access control,
  expose sensitive information, claim a saved, synchronized, queued, or
  completed state prematurely, obscure a destructive consequence,
  reduce a confirmation or error-prevention requirement, weaken
  permission-denied or not-found privacy behavior, or use profile
  emphasis to justify a less-visible error or inaccessible
  authentication.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates the already-Approved `KBDL-CMP-063`, `064`, `098`, `101`, `103`, `104` security and correctness principles, extended explicitly to profile emphasis by the approved KBDL-009 prompt's Security Requirements section
  - Related requirement: `KBDL-CMP-063`, `KBDL-CMP-064`, `KBDL-CMP-098`, `KBDL-CMP-101`, `KBDL-CMP-103`, `KBDL-CMP-104`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-security-privacy-and-correctness).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual security review. Precision density must not obscure permissions or errors; Showcase expression must not expose private media or metadata; Flow reassurance must not make unconfirmed success claims — each restates the shared rule above for its own emphasis area.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

## 24. Profile Conflicts and Exception Handling

- **`KBDL-PRO-024`** — When profile emphasis conflicts with safety or
  data integrity, accessibility, user task or comprehension, an
  Approved KBDL requirement, content hierarchy, responsive constraints,
  or performance, the profile emphasis **must** yield, per the Approved
  design-decision hierarchy; a profile exception affecting a locked or
  Approved rule **must** stop implementation, name the affected
  requirement, explain the conflict, identify impact, record
  alternatives, follow KBDL governance, receive explicit project-owner
  approval, and be entered in the decision register where required.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: restates [principles.md §8](principles.md#8-design-decision-hierarchy) and [governance.md § Exception process](governance.md#exception-process)
  - Related requirement: `KBDL-PRN-006`, `KBDL-GOV-002`, `KBDL-GOV-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24](#24-profile-conflicts-and-exception-handling).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review of any proposed exception against the governance exception process.
  - Known limitation: Implementation-level profile behavior is not verified; no coded project profile exists yet to test against.

- **`KBDL-PRO-025`** — This document **must not** create or approve any
  profile exception.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not applicable.
  - Authority: scope-control requirement, explicit mandatory clause of the approved KBDL-009 prompt
  - Related requirement: `KBDL-PRO-024`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24](#24-profile-conflicts-and-exception-handling).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual scope-compliance review (performed, see implementation report).
  - Known limitation: Not applicable — scope-control requirement, not independently testable against an implementation.

## 25. Profile Adoption and Change Management

- **`KBDL-PRO-026`** — A project-level profile adoption record **must**
  document: initial profile selection; owner; rationale; scope; review
  date; approved exceptions; pending recommendations; affected product
  areas; change history; and validation status.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not applicable.
  - Authority: explicit mandatory field list from the approved KBDL-009 prompt's Profile Adoption and Change Management section
  - Related requirement: `KBDL-PRO-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-profile-adoption-and-change-management).
  - Decision-packet destination: None — Approved requirement; not awaiting packet approval
  - Pending dependencies: None.
  - Validation method: Manual review of a project's adoption record once one exists.
  - Known limitation: No project profile adoption record exists yet to review against this requirement's field list.

Whether a profile may change after adoption, whether a project may have
multiple profile scopes, and how migration is governed are new
decisions:

- **`KBDL-PRO-027`** — Adopt a profile-change and migration governance
  policy: whether a profile may change after adoption, whether a
  project may have multiple concurrent profile scopes, and how a
  migration between profiles is reviewed and recorded.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-026`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-profile-adoption-and-change-management), [§33](#33-kbdl-009-decision-packet) item 3.
  - Decision-packet destination: Approval-ready item 3
  - Pending dependencies: None.
  - Validation method: Project-owner review (not yet performed).
  - Known limitation: Recommended — grants no implementation authority pending project-owner review; see the decision packet.

- **`KBDL-PRO-029`** — Adopt a default profile-adoption-record review
  cadence.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a PRO ID does not grant implementation authority.
  - Related requirement: `KBDL-PRO-026`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-profile-adoption-and-change-management), [§33](#33-kbdl-009-decision-packet) item 5.
  - Decision-packet destination: Approval-ready item 5
  - Pending dependencies: None.
  - Validation method: Project-owner review (not yet performed).
  - Known limitation: Recommended — grants no implementation authority pending project-owner review; see the decision packet.

Manual customization of a project's KBDL implementation is out of scope
for this document and belongs to a later roadmap module (`CUS`).

## 26. Conforming Examples

Documentation examples only; none has been implementation-tested.

1. **Showcase, marketing surface, light theme.** A portfolio landing
   page uses large display typography and a full-bleed hero image,
   preserving a 4.5:1 text-over-media contrast and a single clear
   primary action. *Requirements:* `KBDL-PRO-001`, `010`. *Shared
   requirements:* foundation contrast rules, WCAG baseline. *Emphasis:*
   display typography, media hierarchy. *Locked rules preserved:*
   accessibility baseline, semantic hierarchy. *Pending dependency:*
   None. *Validation method:* Manual contrast/hierarchy review.
2. **Showcase, project-detail consumption, dark theme, reduced motion.**
   A case-study page lets entrance motion settle once content loads,
   then remains still while the user reads, honoring the reduced-motion
   preference identically to every other profile. *Requirements:*
   `KBDL-PRO-010`. *Locked rules preserved:* `KBDL-MOT-026` reduced-
   motion parity. *Pending dependency:* None.
3. **Precision, dashboard, keyboard.** A metrics dashboard uses a
   Static Data Table with correct header association, fully operable
   by keyboard with a visible focus indicator. *Requirements:*
   `KBDL-PRO-011`, `014`. *Locked rules preserved:* `KBDL-CMP-070`
   native-table semantics, `KBDL-CMP-006` focus visibility. *Pending
   dependency:* None (this example does not use a data-dense
   transformation).
4. **Precision, repeated operational task, narrow viewport.** A filter-
   and-review workflow preserves the same relative information priority
   at `compact` width as at `wide`, per the shared responsive
   content-priority rule. *Requirements:* `KBDL-PRO-011`,
   [§18](#18-responsive-mapping). *Pending dependency:* Exact
   breakpoint value (`KBDL-RSP-002`, unapproved) is not required for
   this example's content-priority claim.
5. **Flow, onboarding, screen reader.** A multi-step account-setup flow
   exposes its current step and total step count programmatically, with
   one primary action per step. *Requirements:* `KBDL-PRO-012`, `015`.
   *Locked rules preserved:* `KBDL-A11Y-040` accessibility floor.
   *Pending dependency:* None.
6. **Flow, checkout process, offline recovery.** A payment step that
   loses connectivity shows an accurate "not yet confirmed" state
   rather than a false success claim, with a persistent retry path.
   *Requirements:* `KBDL-PRO-015`, `023`; `KBDL-CMP-103`. *Locked rules
   preserved:* honest system-state communication. *Pending dependency:*
   None.
7. **Cross-profile, pending-dependency handling.** A project documents
   in its adoption record that its Precision dashboard's exact grid
   column count is not yet finalized because `KBDL-RSP-003` remains
   unapproved, and that the dashboard uses the shared responsive
   content-priority rule in the interim. *Requirements:* `KBDL-PRO-007`,
   `017`. *Pending dependency:* `KBDL-RSP-003`, explicitly recorded, not
   used as authority.

## 27. Non-Conforming Examples

1. **Non-conforming — Showcase replacing accessibility with spectacle.**
   A portfolio hero uses low-contrast text over a busy background image
   to look "artistic." *Fails:* `KBDL-PRO-003`, `KBDL-A11Y-040`.
   *Correction:* Add a solid backing or increase contrast until the
   WCAG threshold is met; the accessibility floor is not adjustable by
   Showcase's expressive emphasis.
2. **Non-conforming — Precision shrinking targets.** A dense dashboard
   reduces button targets below the Approved 24×24 CSS-pixel minimum to
   fit more controls. *Fails:* `KBDL-PRO-014`, `KBDL-CMP-010`.
   *Correction:* Preserve the Approved minimum; increase information
   density through layout, not through violating target size.
3. **Non-conforming — Flow forcing one primary action via semantics.**
   A checkout step disables the Cancel button's semantics to visually
   force the primary action. *Fails:* `KBDL-PRO-015`, `020`.
   *Correction:* Use visual hierarchy (already an approved technique)
   to emphasize the primary action; do not alter a button's semantics.
4. **Non-conforming — Profile-only theme-role inventory.** A project
   defines a "Showcase-only" surface role not present in
   [themes/semantic-roles.md](themes/semantic-roles.md). *Fails:*
   `KBDL-PRO-001`, `KBDL-THM-006`. *Correction:* Use only the shared
   semantic-role inventory; express Showcase's richer accent use within
   existing roles.
5. **Non-conforming — Profile-only timing architecture.** A project
   defines a "Flow easing curve" not present in
   [motion/timing-easing.md](motion/timing-easing.md). *Fails:*
   `KBDL-PRO-001`, [§17](#17-motion-mapping). *Correction:* Select
   among the existing Approved easing categories; profile emphasis
   governs frequency and category choice, not new curve definitions.
6. **Non-conforming — Treating a pending recommendation as Approved.**
   A project cites `KBDL-CMP-041` (navigation collapse threshold) as
   authority for a Precision navigation redesign. *Fails:*
   `KBDL-PRO-006`, [§37](#37-kbdl-008-approval-boundary-audit).
   *Correction:* Treat `KBDL-CMP-041` as unapproved context only until
   its own contingent dependencies are resolved.
7. **Non-conforming — Switching profile by viewport.** A project
   declares "Precision on desktop, Flow on mobile" for the same
   product. *Fails:* `KBDL-PRO-002` (profile is not a viewport class).
   *Correction:* Select one profile (or a documented hybrid model, once
   `KBDL-PRO-009` is approved) independent of viewport; use responsive
   behavior, not profile switching, to adapt to viewport.
8. **Non-conforming — Treating dark mode as a profile.** A project's
   adoption record lists "Dark" as its selected profile. *Fails:*
   `KBDL-PRO-002`. *Correction:* Select Showcase, Precision, or Flow;
   dark mode is an independent theme-mode preference.
9. **Non-conforming — Undocumented hybrid precedence.** A project mixes
   Precision density with Flow progression with no documented
   precedence rule for conflicting guidance. *Fails:* `KBDL-PRO-007`,
   `009` (undecided). *Correction:* Document a single primary profile
   until a hybrid-profile model is approved.
10. **Non-conforming — Profile bypassing responsive requirements.** A
    project claims its Showcase profile is exempt from 320px reflow
    because "Showcase is desktop-first." *Fails:* `KBDL-PRO-003`,
    [§18](#18-responsive-mapping). *Correction:* All profiles preserve
    the same reflow requirement; Showcase may prioritize different
    content, not skip the requirement.
11. **Non-conforming — Incompatible profile-specific anatomy.** A
    project gives its Precision Button an extra required part not in
    the shared component anatomy. *Fails:* `KBDL-PRO-020`,
    `KBDL-CMP-051`. *Correction:* Use only the shared anatomy; express
    Precision's density preference through spacing, not new parts.
12. **Non-conforming — Hiding feedback to reduce noise.** A Precision
    dashboard suppresses error toasts entirely to appear "cleaner."
    *Fails:* `KBDL-PRO-023`, `KBDL-CMP-090`. *Correction:* Reduce
    visual noise through severity-appropriate presentation, not by
    removing required error communication.

## 28. Normative Requirements

See each section above ([§5](#5-profile-architecture) through
[§25](#25-profile-adoption-and-change-management)) for the full text of
every `KBDL-PRO-001` through `KBDL-PRO-029` requirement — including
`KBDL-PRO-028` (§8) and `KBDL-PRO-029` (§25), each with exactly one
authoritative normative record. This section is a pointer, not a
duplicate, consistent with the single-authoritative-location pattern
already used in
[components-system.md §27](components-system.md#27-normative-requirements).

**Authoritative status summary** (derived directly from the
per-requirement lifecycle field above, not a separately maintained
count):

```text
Total requirements: 29 (KBDL-PRO-001 through KBDL-PRO-029)
Approved:           22
Recommended:         7
Unresolved:          0
Deferred:            0
Blocked:             0
```

The seven `Recommended` requirements are exactly: `KBDL-PRO-009`, `016`,
`017`, `018`, `027`, `028`, `029` — see
[§38](#38-decision-packet-coverage-audit) for the exact, verified list
and its one-to-one packet mapping.

## 29. Requirement Coverage Matrix

| ID | Title | Scope | Category | Lifecycle | Provenance | Validation status | Authority | Specification location | Decision-packet destination | Pending dependency | Known limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `KBDL-PRO-001` | Shared profile architecture | Shared | Architecture | Approved | Confirmed | Not verified | Prior-KBDL | §5 | None | None | Implementation-dependent |
| `KBDL-PRO-002` | Profile terminology distinction | Shared | Terminology | Approved | Confirmed | Not verified | Prior-KBDL + prompt | §5 | None | None | Implementation-dependent |
| `KBDL-PRO-003` | Locked-decision protection | Shared | Governance | Approved | Confirmed | Not verified | Prior-KBDL | §7 | None | None | Implementation-dependent |
| `KBDL-PRO-004` | Controlled-variable integrity | Shared | Governance | Approved | Confirmed | Not verified | Prior-KBDL | §7 | None | None | Implementation-dependent |
| `KBDL-PRO-005` | Open-expression subordination | Shared | Governance | Approved | Confirmed | Not verified | Prior-KBDL | §7 | None | None | Not independently testable |
| `KBDL-PRO-006` | No silent earlier-module conversion | Shared | Scope control | Approved | Confirmed | Not applicable | Prompt | §7 | None | None | Not independently testable |
| `KBDL-PRO-007` | Profile declaration fields | Shared | Process | Approved | Confirmed | Not applicable | Prompt | §8 | None | None | No declaration exists yet |
| `KBDL-PRO-008` | Prohibited selection rationale | Shared | Process | Approved | Confirmed | Not applicable | Prompt + prior-KBDL | §8 | None | None | No declaration exists yet |
| `KBDL-PRO-009` | Primary/secondary/hybrid policy | Shared | Governance | Recommended | Assumed | Not applicable | N/A | §8 | Approval-ready item 1 | None | Recommended, unapproved |
| `KBDL-PRO-010` | Showcase purpose/emphasis | Showcase | Definition | Approved | Confirmed | Not verified | Prior-KBDL | §10.1 | None | None | Implementation-dependent |
| `KBDL-PRO-011` | Precision purpose/emphasis | Precision | Definition | Approved | Confirmed | Not verified | Prior-KBDL | §11.1 | None | None | Implementation-dependent |
| `KBDL-PRO-012` | Flow purpose/emphasis | Flow | Definition | Approved | Confirmed | Not verified | Prior-KBDL | §12.1 | None | None | Implementation-dependent |
| `KBDL-PRO-013` | Showcase component interpretation | Showcase | Components | Approved | Confirmed | Not verified | Prior-KBDL | §10.2 | None | None | Implementation-dependent |
| `KBDL-PRO-014` | Precision component interpretation | Precision | Components | Approved | Confirmed | Not verified | Prior-KBDL | §11.2 | None | `KBDL-CMP-105`, `KBDL-RSP-011` (context only) | Implementation-dependent |
| `KBDL-PRO-015` | Flow component interpretation | Flow | Components | Approved | Confirmed | Not verified | Prior-KBDL | §12.2 | None | `KBDL-CMP-015`, `036` (context only) | Implementation-dependent |
| `KBDL-PRO-016` | Showcase composition defaults | Showcase | Discretionary | Recommended | Assumed | Not applicable | N/A | §10.2 | Contingent — §33.3 | `KBDL-CMP-067` (blocking) | Contingent, unapproved |
| `KBDL-PRO-017` | Precision density defaults | Precision | Discretionary | Recommended | Assumed | Not applicable | N/A | §11.2 | Approval-ready item 2 | None (context: `KBDL-RSP-002`/`003`) | Recommended, unapproved |
| `KBDL-PRO-018` | Flow action defaults | Flow | Discretionary | Recommended | Assumed | Not applicable | N/A | §12.2 | Contingent — §33.3 | `KBDL-CMP-015`, `036` (blocking) | Contingent, unapproved |
| `KBDL-PRO-019` | Principles mapping completeness | Shared | Mapping | Approved | Confirmed | Not verified | Prior-KBDL | §14 | None | None | Implementation-dependent |
| `KBDL-PRO-020` | Core-component mapping integrity | Shared | Mapping | Approved | Confirmed | Not verified | Prior-KBDL | §20 | None | None | Implementation-dependent |
| `KBDL-PRO-021` | System-component mapping integrity | Shared | Mapping | Approved | Confirmed | Not verified | Prior-KBDL | §21 | None | None | Implementation-dependent |
| `KBDL-PRO-022` | Content consistency | Shared | Content | Approved | Confirmed | Not verified | Prior-KBDL | §22 | None | None | Implementation-dependent |
| `KBDL-PRO-023` | Security and correctness baseline | Shared | Security | Approved | Confirmed | Not verified | Prior-KBDL + prompt | §23 | None | None | Implementation-dependent |
| `KBDL-PRO-024` | Conflict-resolution process | Shared | Governance | Approved | Confirmed | Not verified | Prior-KBDL | §24 | None | None | Implementation-dependent |
| `KBDL-PRO-025` | No exception creation | Shared | Scope control | Approved | Confirmed | Not applicable | Prompt | §24 | None | None | Not independently testable |
| `KBDL-PRO-026` | Adoption-record fields | Shared | Process | Approved | Confirmed | Not applicable | Prompt | §25 | None | None | No adoption record exists yet |
| `KBDL-PRO-027` | Change/migration governance | Shared | Governance | Recommended | Assumed | Not applicable | N/A | §25 | Approval-ready item 3 | None | Recommended, unapproved |
| `KBDL-PRO-028` | Profile-selection rubric | Shared | Discretionary | Recommended | Assumed | Not applicable | N/A | §8 | Approval-ready item 4 | None | Recommended, unapproved |
| `KBDL-PRO-029` | Adoption-record review cadence | Shared | Discretionary | Recommended | Assumed | Not applicable | N/A | §25 | Approval-ready item 5 | None | Recommended, unapproved |

## 30. Cross-Module Mapping Matrix

| Module | Every profile consumes | No Approved requirement disappears | No pending recommendation used as authority | No separate system created |
| --- | --- | --- | --- | --- |
| Principles | `KBDL-PRN-007`, nine core principles | Confirmed — [§14](#14-principles-mapping) | Not applicable (no pending PRN items) | Confirmed |
| Foundations | `KBDL-FND-008`, all foundation roles/values | Confirmed — [§15](#15-foundation-mapping) | Not applicable (no pending FND items) | Confirmed |
| Themes | `KBDL-THM-006`, full semantic-role inventory | Confirmed — [§16](#16-theme-mapping) | Confirmed — no opacity/translucent/forced-colors adopted | Confirmed |
| Motion | `KBDL-MOT-026`, `034`, full timing/easing architecture | Confirmed — [§17](#17-motion-mapping) | Not applicable (motion decision packet already fully approved) | Confirmed |
| Responsive | Content-priority logic, Approved outcomes | Confirmed — [§18](#18-responsive-mapping) | Confirmed — [§35](#35-kbdl-006-approval-boundary-audit) | Confirmed |
| Accessibility | `KBDL-A11Y-040`, complete WCAG 2.2 AA baseline | Confirmed — [§19](#19-accessibility-mapping) | Confirmed — [§35](#35-kbdl-006-approval-boundary-audit) | Confirmed |
| KBDL-007 components | `KBDL-CMP-051`, full semantic/anatomy contract | Confirmed — [§20](#20-core-component-mapping) | Confirmed — [§36](#36-kbdl-007-approval-boundary-audit) | Confirmed |
| KBDL-008 components | `KBDL-CMP-066`, full architecture/focus/status contract | Confirmed — [§21](#21-system-component-mapping) | Confirmed — [§37](#37-kbdl-008-approval-boundary-audit) | Confirmed |
| Governance | Design-decision hierarchy, exception process | Confirmed — [§24](#24-profile-conflicts-and-exception-handling) | Not applicable | Confirmed |
| Future customization (`CUS`) | Not yet reached | Not applicable | Not applicable | Not applicable — locked |
| Future validation (`VAL`) | Not yet reached | Not applicable | Not applicable | Not applicable — locked |

## 31. Profile-Invariant Validation Matrix

| Invariant | Validation method | Status |
| --- | --- | --- |
| Identity (`KBDL-PRO-001`) | Manual identity-statement review | Not verified |
| Foundations (`KBDL-FND-008`) | Manual foundation-value review | Not verified |
| Theme (`KBDL-THM-006`) | Manual semantic-role parity review | Not verified |
| Motion (`KBDL-MOT-026`) | Manual timing/easing architecture review | Not verified |
| Responsive outcomes | Manual reflow/content-priority review | Not verified |
| Accessibility (`KBDL-A11Y-040`) | Manual WCAG 2.2 AA review | Not verified |
| Component semantics (`KBDL-CMP-051`) | Manual semantic-contract review | Not verified |
| Component anatomy (`KBDL-CMP-051`) | Manual anatomy review | Not verified |
| Security (`KBDL-PRO-023`) | Manual security review | Not verified |
| Correctness (`KBDL-PRO-023`) | Manual correctness-claim review | Not verified |
| Performance | Manual performance-cost review | Not verified |

## 32. Profile-Specific Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| Showcase emphasis (`KBDL-PRO-010`, `013`) | Manual cross-module consistency review | Not verified |
| Precision emphasis (`KBDL-PRO-011`, `014`) | Manual cross-module consistency review | Not verified |
| Flow emphasis (`KBDL-PRO-012`, `015`) | Manual cross-module consistency review | Not verified |
| Selection rationale (`KBDL-PRO-008`) | Manual review of a project's stated rationale | Not verified |
| Cross-module consistency ([§30](#30-cross-module-mapping-matrix)) | Manual matrix audit (performed for this document, see implementation report) | Verified for this document's own internal consistency; Not verified for any project's implementation |
| Pending dependencies ([§35](#35-kbdl-006-approval-boundary-audit)–[§37](#37-kbdl-008-approval-boundary-audit)) | Manual boundary-audit review (performed, see implementation report) | Verified for this document's own boundary compliance |
| Content and communication (`KBDL-PRO-022`) | Manual content review | Not verified |
| Responsive behavior ([§18](#18-responsive-mapping)) | Manual reflow review | Not verified |
| Motion behavior ([§17](#17-motion-mapping)) | Manual reduced/no-motion parity review | Not verified |
| System-state behavior (`KBDL-PRO-021`) | Manual review | Not verified |

Documentation-level validation (marked "performed" above) confirms this
specification's own internal consistency; it does not constitute
implementation-level validation, which remains `Not verified` for every
row until a coded project exists to test against.

## 33. KBDL-009 Decision Packet

### 33.1 Already-Approved Profile Architecture (context only)

Not awaiting approval — provided as context. Directly supported by
prior approved decisions: shared architecture (`KBDL-PRO-001`);
profile-terminology distinction (`KBDL-PRO-002`); locked/controlled/
open classification (`KBDL-PRO-003`–`005`); the no-silent-conversion
scope rule (`KBDL-PRO-006`); the declaration and prohibited-rationale
requirements (`KBDL-PRO-007`, `008`); Showcase, Precision, and Flow
purpose and component interpretation (`KBDL-PRO-010`–`015`); principles,
core-component, and system-component mapping integrity (`KBDL-PRO-019`,
`020`, `021`); content, security, conflict, and adoption-record
requirements (`KBDL-PRO-022`–`026`).

### 33.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Responsive impact | Theme impact | Motion impact | Component impact | Security/privacy impact | Profile impact | Dependencies | Exact affected requirements | Approval scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Primary/secondary/hybrid profile policy | Adopt a policy on primary-profile exclusivity, secondary-profile permission, and hybrid precedence (`KBDL-PRO-009`) | Prevents undocumented, inconsistent profile-mixing across projects | No policy, decided per project (rejected — risks silent fragmentation) | Requires documenting precedence for any approved hybrid case | None beyond what the declaration process already requires | None | None | None | None | None | Applies to how any profile is declared | None | `KBDL-PRO-009` | Item 1 only |
| 2 | Precision density and component-emphasis defaults | Adopt exact Precision spacing-intensity and table-presentation defaults (`KBDL-PRO-017`) | Gives Precision projects a consistent starting density | Leaving density fully per-project (rejected — inconsistent cross-project recognizability) | Exact spacing values remain bound by the already-approved spacing scale | Target-size minimum (`KBDL-CMP-010`) unaffected either way | Depends on eventual `KBDL-RSP-002`/`003` values for exact grid interaction, cited as context only | None | None | Static Data Table/Grid distinction (`KBDL-CMP-070`) unaffected | None | Precision only | `KBDL-CMP-010`, `KBDL-CMP-070` | `KBDL-PRO-017` | Item 2 only |
| 3 | Change and migration governance | Adopt a profile-change and migration review policy (`KBDL-PRO-027`) | Gives profile changes a consistent, auditable process | No governance, changes undocumented (rejected — loses adoption-history integrity) | Requires review-date tracking in the adoption record | None significant | None | None | None | None | None | Applies to any project changing profile | `KBDL-PRO-026` | `KBDL-PRO-027` | Item 3 only |
| 4 | Profile-selection rubric | Adopt a qualitative rubric (not a numeric score) for matching project characteristics to a profile | Gives projects a consistent, repeatable selection method beyond ad hoc judgment | A numeric scoring model (rejected for now — risks false precision without validated weighting) | Requires periodic review as new project types emerge | None significant | None | None | None | None | None | Applies to profile selection generally | `KBDL-PRO-007`, `KBDL-PRO-008` | `KBDL-PRO-028` | Item 4 only |
| 5 | Profile review cadence | Adopt a default review-date interval for profile adoption records | Keeps profile fit and pending-dependency status current | No default cadence, left to each project (rejected — risks stale declarations) | None significant | None | None | None | None | None | None | Applies to any adopted profile | `KBDL-PRO-026` | `KBDL-PRO-029` | Item 5 only |

### 33.3 Unresolved or Not Approval-Ready

- **Showcase composition and component-emphasis defaults
  (contingent, not independently approval-ready)** — maps to
  `KBDL-PRO-016`, which remains `Recommended`. It depends directly on
  the unapproved KBDL-008 card-variant taxonomy (`KBDL-CMP-067`) and
  **cannot be approved independently through the KBDL-009 packet**. It
  may become approval-ready only after `KBDL-CMP-067` itself is
  approved or replaced. It grants no implementation authority and
  approves no exact card variant. Related: `KBDL-CMP-067`.
- **Flow action-progression and workflow-component defaults
  (contingent, not independently approval-ready)** — maps to
  `KBDL-PRO-018`, which remains `Recommended`. It depends directly on
  the unapproved KBDL-007 button-hierarchy (`KBDL-CMP-015`) and
  form-action-row-ordering (`KBDL-CMP-036`) recommendations and
  **cannot be approved independently through the KBDL-009 packet**. It
  may become approval-ready only after `KBDL-CMP-015`/`036` are
  approved or replaced. It grants no implementation authority. Related:
  `KBDL-CMP-015`, `KBDL-CMP-036`.
- **Profile-specific content guidance beyond the Approved shared
  baseline** ([§22](#22-content-and-communication-considerations)) —
  depends on foundation typography values not yet finalized in some
  areas; out of scope here.
- **Profile-specific validation-requirement specifics** beyond the
  documentation-versus-implementation distinction already Approved
  ([§32](#32-profile-specific-validation-matrix)) — depends on an
  implementation existing; `Unresolved`.
- **Exact profile-specific breakpoints, grid values, or responsive
  transformations** — depend on the unapproved `KBDL-RSP-002`–`005`,
  `008`, `011`; not proposed here.
- **Exact profile-specific motion frequency quotas** — depend on the
  underlying motion-pattern-matrix rows themselves remaining
  `Recommended`; not re-proposed here.
- **Profile-specific theme opacity or data-visualization palettes** —
  depend on unapproved theme opacity and data-visualization-palette
  values; not proposed here.
- **Profile-specific token implementation, coded components, product
  templates, Figma libraries, or framework APIs** — explicitly out of
  scope for a design-language specification.
- **Actual screen-reader/browser matrix for any profile** — depends on
  the unapproved `KBDL-A11Y-035`.
- **Manual customization of a profile** — deferred to the later Manual
  Customization module (`CUS`).
- **Implementation-level profile validation and production
  conformance** — require an implementation that does not exist yet.

### 33.4 Additional Discretionary Items

Items 4 and 5 above are backed by `KBDL-PRO-028` and `KBDL-PRO-029`
respectively. Their complete, single authoritative normative records
appear in [§8, Profile Selection and Declaration](#8-profile-selection-and-declaration)
and [§25, Profile Adoption and Change Management](#25-profile-adoption-and-change-management),
not here — this section does not redefine them, consistent with the
single-authoritative-location rule stated in
[§28](#28-normative-requirements).

**Exact scope of a future approval:** an `APPROVE` response to
[§33.2](#332-recommended-decisions--ready-for-approval) would authorize
exactly items 1–5 above (`KBDL-PRO-009`, `017`, `027`, `028`, `029`). It
would **not** approve `KBDL-PRO-016` or `018` (contingent,
[§33.3](#333-unresolved-or-not-approval-ready)), any other
[§33.3](#333-unresolved-or-not-approval-ready) item, any of the nine
KBDL-006 recommendations, any of the ten KBDL-007 recommendations, any
of the seventeen KBDL-008 recommendations, or any KBDL-010-or-later
content. It would not itself constitute validation of any item — see
[§31](#31-profile-invariant-validation-matrix)–[§32](#32-profile-specific-validation-matrix).

## 34. Approval-Ready versus Contingent Decisions

Independently approval-ready: items 1–5 in
[§33.2](#332-recommended-decisions--ready-for-approval)
(`KBDL-PRO-009`, `017`, `027`, `028`, `029`) — none depends on approving
a pending KBDL-006, KBDL-007, KBDL-008, theme, motion, or later-
customization value for its own approval.

Contingent, not approval-ready: `KBDL-PRO-016` (blocked on the
unapproved KBDL-008 `KBDL-CMP-067`) and `KBDL-PRO-018` (blocked on the
unapproved KBDL-007 `KBDL-CMP-015`/`036`) — see
[§33.3](#333-unresolved-or-not-approval-ready) for each item's blocker,
affected requirement, and what future approval would be needed. Neither
grants implementation authority, and neither is included in the future-
approval scope stated in [§33](#33-kbdl-009-decision-packet).

## 35. KBDL-006 Approval-Boundary Audit

| KBDL-006 requirement | Referenced? | Contextual or contingent | Exact profile impact | Used normatively | Approval status | Packet destination |
| --- | --- | --- | --- | --- | --- | --- |
| `KBDL-RSP-002` (exact breakpoint thresholds) | Referenced | Contextual only | Cited for Precision density defaults (item 2) and responsive mapping | No | Unapproved | Cited context, item 2 |
| `KBDL-RSP-003` (grid columns) | Referenced | Contextual only | Cited for Precision density defaults (item 2) | No | Unapproved | Cited context, item 2 |
| `KBDL-RSP-004` (container widths) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-RSP-005` (gutters) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-RSP-008` (navigation collapse thresholds) | Not referenced (KBDL-009 introduces no new navigation-collapse guidance beyond KBDL-007/008 boundaries) | Not applicable | None | No | Unapproved | Not used |
| `KBDL-RSP-011` (data-dense strategy) | Referenced | Contextual only | Cited in Precision component interpretation (§11.2) | No | Unapproved | Cited context only |
| `KBDL-A11Y-011` (forced-colors policy) | Not referenced (this module introduces no new forced-colors guidance) | Not applicable | None | No | Unapproved | Not used |
| `KBDL-A11Y-021` (44×44 preferred target) | Referenced | Contextual only | Cited in accessibility mapping (§19) as not presented as Approved | No | Unapproved | Cited context only |
| `KBDL-A11Y-035` (preferred testing matrix) | Referenced | Contextual only | Cited in §33.3 as a future validation dependency | No | Unapproved | Cited context only |

None of the nine is treated as implementation authority anywhere in
this document.

## 36. KBDL-007 Approval-Boundary Audit

| KBDL-007 requirement | Referenced? | Contextual or contingent | Exact profile impact | Used normatively | Approval status | Packet destination |
| --- | --- | --- | --- | --- | --- | --- |
| `KBDL-CMP-015` (button hierarchy taxonomy) | Referenced | Contingent dependency | Blocks `KBDL-PRO-018` (Flow action defaults) | No | Unapproved | Contingent, §33.3 |
| `KBDL-CMP-017` (icon-only visible-label threshold) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-020` (button-group composition) | Not referenced (no profile-specific button-group guidance introduced) | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-025` (search-field model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-029` (combobox-justification threshold) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-036` (form-action-row reflow order) | Referenced | Contingent dependency | Blocks `KBDL-PRO-018` (Flow action defaults) | No | Unapproved | Contingent, §33.3 |
| `KBDL-CMP-041` (navigation collapse threshold, itself contingent) | Referenced | Contextual only | Cited in §27 non-conforming example 6 as a caution against misuse | No | Unapproved | Cited context only |
| `KBDL-CMP-044` (breadcrumb truncation model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-046` (tabs activation model) | Not referenced (Precision's Tabs use remains KBDL-007 scope; no profile-specific activation variant introduced) | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-048` (pagination truncation model) | Not referenced | Not applicable | None | No | Unapproved | Not used |

None of the ten is treated as implementation authority anywhere in
this document.

## 37. KBDL-008 Approval-Boundary Audit

| KBDL-008 requirement | Referenced? | Contextual or contingent | Exact profile impact | Used normatively | Approval status | Packet destination |
| --- | --- | --- | --- | --- | --- | --- |
| `KBDL-CMP-067` (Card-variant taxonomy) | Referenced | Contingent dependency | Blocks `KBDL-PRO-016` (Showcase composition defaults) | No | Unapproved | Contingent, §33.3 |
| `KBDL-CMP-069` (Accordion open model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-073` (Tooltip timing) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-074` (Popover taxonomy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-076` (Menu interaction model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-080` (Modal sizing/nesting) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-083` (Drawer/Sheet taxonomy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-085` (Overlay nesting policy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-089` (Banner severity taxonomy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-091` (Toast lifecycle model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-099` (Empty-state taxonomy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-102` (Error/system-state severity taxonomy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-105` (Grid-versus-table threshold) | Referenced | Contextual only | Cited in Precision component interpretation (§11.2) | No | Unapproved | Cited context only |
| `KBDL-CMP-106` (Treegrid justification threshold) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-108` (Carousel auto-rotation policy) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-110` (Data-visualization interaction model) | Not referenced | Not applicable | None | No | Unapproved | Not used |
| `KBDL-CMP-111` (Responsive transformation policy) | Not referenced | Not applicable | None | No | Unapproved | Not used |

None of the seventeen is treated as implementation authority anywhere
in this document.

## 38. Decision-Packet Coverage Audit

```text
Total PRO requirements:                    29
Approved:                                  22
Recommended:                                7
Unresolved:                                 0
Deferred:                                   0
Blocked:                                    0

Independently approval-ready recommendations: 5
Contingent recommendations:                    2
Unresolved tracking count (prose-only, no dedicated ID): 4
```

Every `Recommended` `KBDL-PRO-###` requirement maps to exactly one
packet item — either an independently approval-ready item in
[§33.2](#332-recommended-decisions--ready-for-approval) or a contingent
item in [§33.3](#333-unresolved-or-not-approval-ready) — and every
approval-ready packet item maps to exactly one `Recommended`
requirement:

| Recommended requirement | Packet item | Independently approval-ready | Dependency |
| --- | --- | --- | --- |
| `KBDL-PRO-009` | 1 | Yes | None |
| `KBDL-PRO-017` | 2 | Yes | None (`KBDL-RSP-002`/`003` cited as unapproved context for the exact grid-interaction point only) |
| `KBDL-PRO-027` | 3 | Yes | None |
| `KBDL-PRO-028` | 4 | Yes | None |
| `KBDL-PRO-029` | 5 | Yes | None |
| `KBDL-PRO-016` | Contingent item (§33.3) | No — depends on unapproved `KBDL-CMP-067` | `KBDL-CMP-067` |
| `KBDL-PRO-018` | Contingent item (§33.3) | No — depends on unapproved `KBDL-CMP-015`/`036` | `KBDL-CMP-015`, `KBDL-CMP-036` |

Five `Recommended` requirements map one-to-one to the five
approval-ready packet items; two `Recommended` requirements
(`KBDL-PRO-016`, `018`) map to the two contingent items described in
§33.3. The remaining four items referenced in §33.3 prose (profile-
specific content guidance beyond baseline, profile-specific validation
specifics, exact profile breakpoints/motion/theme values, and
implementation-level validation) are tracked as `Unresolved`/`Deferred`
prose without a dedicated `KBDL-PRO-###` ID, consistent with the
pattern already established in `components-system.md §40` for
value-only placeholders that are not independently testable rules. No
`Recommended` requirement is orphaned, no approval-ready packet item is
orphaned, no `Approved` requirement is presented as awaiting approval,
no pending earlier-module dependency is hidden, and no KBDL-006,
KBDL-007, or KBDL-008 recommendation is represented as approved
anywhere in this document.

**Exact scope of a future approval:** restated from
[§33](#33-kbdl-009-decision-packet) — an `APPROVE` response to
[§33.2](#332-recommended-decisions--ready-for-approval) authorizes
exactly items 1–5. It does not approve `KBDL-PRO-016`, `018`, any other
[§33.3](#333-unresolved-or-not-approval-ready) item, or any pending
earlier-module recommendation.

## 39. Deferred and Unresolved Items

- Manual customization of a profile — deferred to the Manual
  Customization module (`CUS`).
- Profile-specific token implementation, coded components, framework
  APIs, product templates, and Figma libraries — out of scope.
- Exact profile-specific density values, component sizes, breakpoints,
  and grid values — depend on unapproved KBDL-006 values.
- Exact profile-specific motion frequency and component-specific motion
  — depend on the underlying motion-pattern-matrix rows themselves
  remaining `Recommended`.
- Profile-specific theme opacity and data-visualization palettes —
  depend on unapproved theme and data-visualization values.
- Browser-support policy and the actual screen-reader/browser matrix —
  depend on unapproved `KBDL-A11Y-035`.
- Implementation-level profile validation and production conformance —
  `Not verified`, no implementation exists.
- Profile analytics and automated profile-selection tooling — out of
  scope for a design-language specification.
- Use of any of the nine unapproved KBDL-006, ten unapproved KBDL-007,
  or seventeen unapproved KBDL-008 recommendations as implementation
  authority — explicitly excluded throughout this document (see
  [§35](#35-kbdl-006-approval-boundary-audit)–[§37](#37-kbdl-008-approval-boundary-audit)).

## 40. Traceability

See [traceability-matrix.md](traceability-matrix.md) for how each
`KBDL-PRO-###` requirement traces to its blueprint origin, approval
status, provenance, authority, validation status, and evidence, and
[decision-register.md](decision-register.md) for any decision recorded
as part of this module. No decision-register entry has been created for
KBDL-009, since no packet review has yet occurred.
