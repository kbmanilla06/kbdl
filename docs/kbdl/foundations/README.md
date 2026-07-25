# KBDL Foundations — Index

Lifecycle status: `Approved` (this index, the foundation status model, the
profile-adjustment summary, the conformance rules, and the `KBDL-FND-###`
requirements below). The specific default values proposed throughout the
foundation documents are `Recommended`, not `Approved` — see
[§3 Foundation Status Model](#3-foundation-status-model).

Return to the [specification index](../README.md). Status labels are
defined in [conventions.md §1](../conventions.md#1-status-labels);
requirement IDs in
[conventions.md §2](../conventions.md#2-requirement-identification).

---

## 1. Purpose

This is the entry point for KBDL-003: Core Visual Foundations. It defines
KBDL's reusable visual-foundation **architecture** (roles, relationships,
and rules — `Approved`, derived directly from
[principles.md](../principles.md)) and proposes **recommended default
values** for color, typography, spacing/layout, shape/depth, and
iconography/media (all `Recommended`, pending project-owner approval).

Foundations documents:

- [color.md](color.md) — primitive, neutral, accent, semantic, status, and
  data-display color architecture.
- [typography.md](typography.md) — type-role architecture, type scale, and
  typeface model.
- [spacing-layout.md](spacing-layout.md) — spacing system, layout/grid
  principles, and breakpoint philosophy.
- [shape-depth.md](shape-depth.md) — shape/corner language, borders and
  dividers, and elevation/depth model.
- [iconography-media.md](iconography-media.md) — iconography and imagery/
  media guidance.

This module does **not** define adaptive-theme mappings (KBDL-004), motion
timings (KBDL-005), detailed responsive interaction behavior (KBDL-006),
component anatomy, or any implementation code.

## 2. What Was Inspected

Before writing this module, the following were reviewed in full:
[principles.md](../principles.md) (identity, nine principles, locked/
controlled/open identity elements, design-decision hierarchy, profile
interpretation), [conventions.md](../conventions.md) (status-label
dimensions and requirement-ID scheme), [governance.md](../governance.md)
(approval, exception, and evidence rules), [decision-register.md](../decision-register.md)
(KBDL-DEC-001 through KBDL-DEC-011), [traceability-matrix.md](../traceability-matrix.md),
[conformance-checklist.md](../conformance-checklist.md), and
[glossary.md](../glossary.md). No conflicts were found between these
sources and this module's content; every architectural rule in the
foundation documents traces to an existing principle or locked rule rather
than introducing new, unreviewed policy.

## 3. Foundation Status Model

Every statement in the foundation documents falls into exactly one of four
categories, layered on top of the three status dimensions from
[conventions.md §1](../conventions.md#1-status-labels) (lifecycle,
provenance, validation):

### 3.1 Approved rules

Rules directly derived from the approved blueprint, KBDL-001 governance,
or KBDL-002 principles. Lifecycle status: `Approved`. These describe
*architecture* — roles, relationships, and required/prohibited behavior —
never a specific numeric or hex value. Examples: "accessibility takes
priority over aesthetic treatment," "visual hierarchy must remain
recognizable," "project profiles may change emphasis but not foundation
logic," "open brand expression may not override interaction clarity."

### 3.2 Recommended defaults

Newly proposed values, scales, ratios, families, or classifications (for
example, the neutral color scale in [color.md](color.md) or the modular
spacing scale in [spacing-layout.md](spacing-layout.md)). Lifecycle
status: `Recommended`. These require project-owner approval — see
[§6 Foundation Decision Packet](#6-foundation-decision-packet) — before
they may be treated as authorizing implementation, per
[conventions.md §1.1](../conventions.md#11-lifecycle--approval-status).
**No recommended default in these documents is labeled `Approved`.**

### 3.3 Controlled options

Permitted alternatives that preserve KBDL consistency (for example, a
project selecting its own accent hue within the accent role in
[color.md §2.8](color.md#28-project-customization-boundaries), or its own
typeface within the typeface model in
[typography.md §5](typography.md#5-typeface-model)). These correspond to
the "controlled visual variables" category in
[principles.md §5.2](../principles.md#52-controlled-visual-variables).

### 3.4 Unresolved decisions

Material choices that cannot yet be responsibly recommended (for example,
final typeface family selection pending licensing verification, or an
authoring color space beyond hex). Each foundation document lists these in
its own "Unresolved" section. Lifecycle status: `Unresolved`.

### 3.5 Required fields for every new foundation decision

Every new foundation decision (recommended default, controlled option, or
unresolved item) states: lifecycle status, provenance, validation status,
rationale, profiles affected, related principle, related future module,
and validation method. This is applied consistently across
[color.md](color.md), [typography.md](typography.md),
[spacing-layout.md](spacing-layout.md), [shape-depth.md](shape-depth.md),
and [iconography-media.md](iconography-media.md).

## 4. Project Profile Adjustments — Foundation Summary

Detailed per-area guidance lives in each foundation document; this table
summarizes the pattern common to all of them, consistent with
[principles.md §9](../principles.md#9-profile-level-interpretation) and
its shared constraint that profiles adjust emphasis, never foundation
logic.

### 4.1 Showcase

May emphasize: larger typographic contrast (display role, see
[typography.md §3.1](typography.md#31-display)), more editorial
composition (see
[spacing-layout.md §2](spacing-layout.md#2-layout-and-grid-principles-approved-architecture)),
richer media treatment (see [iconography-media.md §2](iconography-media.md#2-imagery-and-media)),
greater surface drama (see
[shape-depth.md §3.5](shape-depth.md#35-profile-level-intensity)), more
generous spacing (see
[spacing-layout.md §1.5](spacing-layout.md#15-density-variations-profile-level)),
and stronger brand imagery.

Must preserve: reading comfort, navigation clarity, responsive content
order, foundation hierarchy, and accessible contrast — all `Approved`
rules that no profile may override.

### 4.2 Precision

May emphasize: compact but readable spacing, strong alignment, structured
surfaces, clear separators (see
[shape-depth.md §2](shape-depth.md#2-borders-and-dividers)), tabular
numeric treatment (see
[typography.md §3.6](typography.md#36-numeric-and-tabular)), and reduced
decorative depth (see
[shape-depth.md §3.5](shape-depth.md#35-profile-level-intensity)).

Must preserve: touch usability, readable density, state clarity, fast
scanning, and consumer comprehension.

### 4.3 Flow

May emphasize: comfortable spacing, friendly typography, clear action
hierarchy, simplified composition, reassuring media, and balanced visual
expression.

Must preserve: predictable navigation, clear progression, recovery
visibility, responsive simplicity, and KBDL identity.

### 4.4 Shared constraint (Approved)

Profiles may alter emphasis but must not define separate foundation
systems — every profile draws from the same color roles, type roles,
spacing scale, shape system, elevation model, and icon/media rules defined
in this module; only the *intensity and frequency* of use differs, per
[principles.md §9.4](../principles.md#94-shared-constraints-across-profiles).

## 5. Foundation Conformance Rules

For every foundation area (color, typography, spacing/layout, shape/
depth, iconography/media), conformance is assessed against: required
behavior (the `Approved` architectural rules in that document), the
recommended default in use (if any), any controlled alternative in use,
prohibited usage (the "must not" statements in that document), profile
considerations (§4 above), accessibility implications, responsive
implications, theme dependencies (deferred to KBDL-004), motion
dependencies (deferred to KBDL-005), and the validation questions below.

### 5.1 Validation questions (per area)

- Does every semantic role trace to an architectural role defined in this
  module, rather than an ad hoc addition?
- Is every "must not" rule in the relevant foundation document satisfied?
- Where a recommended default is used, is it labeled `Recommended` rather
  than presented as `Approved`?
- Where a project has substituted a controlled option, does it still
  satisfy the architectural rule it is a variant of?
- Does the usage hold across all three profiles' shared constraints (§4.4)?

### 5.2 Conceptual conforming and non-conforming examples

Each foundation document (
[color.md §5](color.md#5-conceptual-conformance-examples),
[typography.md](typography.md),
[spacing-layout.md §6](spacing-layout.md#6-conceptual-conformance-examples),
[shape-depth.md §4](shape-depth.md#4-conceptual-conformance-examples),
[iconography-media.md §3](iconography-media.md#3-conceptual-conformance-examples))
includes at least one conforming and one non-conforming conceptual
example specific to that area. These remain conceptual; none define a
component specification.

## 6. Foundation Decision Packet

The choices below are `Recommended`, not `Approved`. Each is summarized
here for project-owner review; full detail is in the linked foundation
document. **Approving this packet approves the specific values recommended
below; it does not by itself approve any later module's content.**

| # | Decision | Recommended choice | Rationale | Alternatives considered | Trade-offs | Profiles affected | Accessibility impact | Performance impact | Later prompts depend on approval? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Color architecture | Role-based architecture in [color.md §2](color.md#2-color-role-architecture-approved) (`Approved` as architecture) | Keeps hue changes from breaking meaning; see [color.md §1](color.md#1-architectural-principles-approved) | A hue-named token system (rejected — breaks theme portability) | None beyond initial setup cost | Showcase, Precision, Flow | Enables consistent contrast/status rules | None | Yes — KBDL-004 theme mappings depend on these roles |
| 2 | Default neutral direction | Cool-neutral 8-step scale, [color.md §3.1](color.md#31-core-neutral-architecture) | Supports "technological" quality without sterility | Warm-neutral scale; fully neutral (no undertone) scale | A cool undertone may read as slightly cold if overused | Showcase, Precision, Flow | Verified contrast pairs, §4 evidence | None | Yes — KBDL-004 |
| 3 | Accent-family direction | Muted indigo/violet two-step accent, [color.md §3.2](color.md#32-primary-technological-accent-family) | Reads as "technological luxury" without neon association (identity exclusion in [principles.md §1](../principles.md#1-identity-statement)) | Blue accent (more generic "tech" default); teal accent | Indigo can trend toward "startup default" if not paired with restraint elsewhere | Showcase, Precision, Flow | 6.07:1 / 8.87:1 contrast verified | None | Yes — KBDL-004 |
| 4 | Typography-role model | Function-based roles, [typography.md §2](typography.md#2-typeface-role-architecture-approved) (`Approved` as architecture) | Decouples hierarchy from a specific font choice, supporting open brand typefaces | A fixed single-typeface identity (rejected — conflicts with open brand expression) | None significant | Showcase, Precision, Flow | Preserves readability priority | None | Yes — later components depend on roles |
| 5 | Typeface strategy | Humanist sans-serif with tabular figures and verified open license, plus a monospace family for the narrow Code role, [typography.md §6](typography.md#6-recommended-default-type-strategy) | Balances legibility, licensing certainty, and KBDL's approachable-but-precise identity | A geometric sans (more "cold-tech"); a licensed commercial family (licensing unverified) | Open-license options may have a smaller weight range than premium commercial families | Showcase, Precision, Flow | Must still verify per-typeface legibility | Web-font loading cost must be managed | Yes — depends on final licensing verification |
| 6 | Type-scale logic | Ratio-based scale relative to body (1×), [typography.md §3](typography.md#3-type-scale-and-text-roles) | Keeps hierarchy proportional and predictable across roles | A purely arbitrary per-role size list (rejected — no rhythm) | None significant | Showcase, Precision, Flow | Must remain resizable by user | None | Yes — implementation needs final unit values |
| 7 | Spacing-system logic | 8-step modular scale, [spacing-layout.md §1.3](spacing-layout.md#13-recommended-modular-spacing-system) | Provides a deliberate, limited rhythm per the locked spacing rule | A continuous/arbitrary spacing approach (rejected — violates locked rule) | A limited step set requires exception-based extension | Showcase, Precision, Flow | Preserves touch-target minimums | None | Yes — KBDL-006 responsive behavior depends on this |
| 8 | Layout and grid model | Content-priority-driven reflow, [spacing-layout.md §2](spacing-layout.md#2-layout-and-grid-principles-approved-architecture) (`Approved` as architecture) | Enforces the locked responsive-content-priority rule | A fixed-column-count grid regardless of content (rejected — risks "shrunk desktop" pattern) | Requires more design judgment than a rigid grid | Showcase, Precision, Flow | Preserves source-order and safe areas | None | Yes — KBDL-006 |
| 9 | Breakpoint philosophy | Named, content-justified breakpoints (compact/standard/expanded/wide), [spacing-layout.md §3.6](spacing-layout.md#36-recommended-breakpoint-set) | Avoids device-name coupling; ties breakpoints to actual content needs | Device-named breakpoints (rejected per required principle in [spacing-layout.md §3.1](spacing-layout.md#31-required-principle-approved)) | Naming requires clear documentation to stay meaningful | Showcase, Precision, Flow | Preserves content priority at every size | None | Yes — exact pixel values deferred to KBDL-006 |
| 10 | Shape and corner model | Softened-structured character, 5-step named corner system, [shape-depth.md §1](shape-depth.md#1-shape-and-corner-language) | Balances "premium" softness with "technical" precision, per identity statement | A fully sharp system (too cold); a fully rounded/pill-heavy system (risks generic "friendly SaaS" look) | Requires discipline to avoid pill overuse | Showcase, Precision, Flow | None directly; supports focus-outline legibility (§ borders) | None | Yes — KBDL-004 theme values depend on named steps |
| 11 | Elevation model | 5-level semantic elevation scale, [shape-depth.md §3.2](shape-depth.md#32-recommended-semantic-elevation-scale) | Ties depth to functional meaning, not decoration | A purely decorative depth system (rejected — violates required principles) | Requires a simplified fallback for reduced-effects contexts | Showcase, Precision, Flow | Must remain legible without shadow/blur (§3.6) | Simplified fallback required on constrained devices | Yes — KBDL-004 shadow/blur values depend on these levels |
| 12 | Iconography strategy | Stroke-based, consistent-optical-size icon system, [iconography-media.md §1.6](iconography-media.md#16-recommended-icon-strategy) | Pairs well with the softened-structured shape character; legible at small sizes | A filled-icon-only system (heavier visual weight at small sizes); mixed stroke/fill (rejected — breaks consistency) | Stroke icons can read as less "bold" at very small sizes if stroke weight is not tuned | Showcase, Precision, Flow | Icons must not be sole state/status indicator (§ required principles) | None | No — can be finalized independently of other modules |
| 13 | Media strategy | Named aspect-treatment set with focal-point preservation, [iconography-media.md §2.3](iconography-media.md#23-aspect-relationships-cropping-and-focal-point-preservation) | Prevents ad hoc cropping that loses meaning; supports responsive reflow | Arbitrary per-instance cropping (rejected — inconsistent, risks losing focal content) | Requires more upfront asset preparation discipline | Showcase, Precision, Flow | Must anticipate alt-text and reduced-motion needs | Low-cost placeholders required for large media | No — can be finalized independently of other modules |

## 7. Normative Requirements

Lifecycle status `Approved` for requirements 1–6 (directly restating
approved architecture from KBDL-001/002); `Recommended` where a
requirement's obligation is to use a *specific proposed default*, which
itself requires approval (noted per requirement). Provenance
`User-provided`/`Confirmed` as noted. Validation status `Not verified`
unless stated otherwise — writing a requirement does not verify it.

- **KBDL-FND-001** — Every KBDL color role **must** be named
  semantically, independent of its underlying hue, per
  [color.md §1](color.md#1-architectural-principles-approved); a project
  **must not** name a role after a specific color.
  - Lifecycle: Approved. Provenance: Confirmed (derived from KBDL-002).
    Validation: Not verified.
  - Related principle: [principles.md §7](../principles.md#7-visual-consistency).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [color.md §1–§2](color.md#1-architectural-principles-approved).
  - Related future modules: Adaptive Themes (KBDL-004).
  - Validation method: Manual review of role names against hue-independence at each later module's approval gate.

- **KBDL-FND-002** — Color **must not** be the sole carrier of meaning for
  any state or status; every meaningful color distinction **must** be
  paired with an icon, label, or pattern, per
  [color.md §1](color.md#1-architectural-principles-approved) and
  [principles.md §5.1](../principles.md#51-locked-identity-rules).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [color.md §2.4](color.md#24-status-roles), [iconography-media.md §1.1](iconography-media.md#11-required-principles-approved).
  - Related future modules: Components (KBDL-008/009).
  - Validation method: Manual review at component-design time (later module) plus this module's conceptual examples.

- **KBDL-FND-003** — Spacing **must** follow the deliberate, repeated
  rhythm established as a locked rule; a project **must not** introduce
  arbitrary one-off spacing values without an approved exception, per
  [spacing-layout.md §1.1](spacing-layout.md#11-required-principles-approved).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §5.1](../principles.md#51-locked-identity-rules), [principles.md §7](../principles.md#7-visual-consistency).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [spacing-layout.md §1](spacing-layout.md#1-spacing-and-sizing-logic).
  - Related future modules: Responsive Behavior (KBDL-006).
  - Validation method: Manual review of spacing usage against the named step set; exceptions checked against [governance.md § Exception process](../governance.md#exception-process).

- **KBDL-FND-004** — Responsive layout changes **must** be justified by
  content and interaction needs, not device names alone; a layout
  **must not** be produced by uniformly scaling a "desktop" composition
  down, per
  [spacing-layout.md §3](spacing-layout.md#3-content-driven-breakpoint-philosophy-approved-principle-recommended-values).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §5.1](../principles.md#51-locked-identity-rules) (responsive content priority).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [spacing-layout.md §3](spacing-layout.md#3-content-driven-breakpoint-philosophy-approved-principle-recommended-values).
  - Related future modules: Responsive Behavior (KBDL-006).
  - Validation method: Manual review of a layout's content-priority ranking at each supported breakpoint.

- **KBDL-FND-005** — Elevation **must** communicate functional
  relationship and priority (never decoration alone), and every elevation
  level **must** remain understandable without shadow, blur, or
  translucency, per
  [shape-depth.md §3.1](shape-depth.md#31-required-principles-approved).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury), [principles.md §6.9](../principles.md#69-performance-aware-enhancement).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [shape-depth.md §3](shape-depth.md#3-elevation-and-depth).
  - Related future modules: Adaptive Themes (KBDL-004).
  - Validation method: Manual review confirming a simplified fallback exists for each elevation level.

- **KBDL-FND-006** — Every functional icon **must** be understandable
  through recognition or a paired label, and **must not** be the sole
  indicator of a component's state or status, per
  [iconography-media.md §1.1](iconography-media.md#11-required-principles-approved).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §5.1](../principles.md#51-locked-identity-rules), [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [iconography-media.md §1](iconography-media.md#1-iconography).
  - Related future modules: Components (KBDL-008/009).
  - Validation method: Manual review of icon usage against the label-pairing rule.

- **KBDL-FND-007** — Media **must** anticipate reduced-motion and
  accessible-text-alternative requirements before those requirements are
  formally specified in later modules, per
  [iconography-media.md §2.1](iconography-media.md#21-required-principles-approved).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default), [principles.md §6.9](../principles.md#69-performance-aware-enhancement).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [iconography-media.md §2](iconography-media.md#2-imagery-and-media).
  - Related future modules: Motion (KBDL-005), Accessibility (KBDL-007).
  - Validation method: Manual review confirming a static/paused equivalent and an anticipated accessible-text plan exist per media asset type.

- **KBDL-FND-008** — Project profiles **must** share one foundation
  architecture (color roles, type roles, spacing scale, shape system,
  elevation model, icon/media rules); a profile **must not** define a
  separate foundation system, per
  [§4.4](#44-shared-constraint-approved) and
  [principles.md §9.4](../principles.md#94-shared-constraints-across-profiles).
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.7](../principles.md#67-adaptability-without-fragmentation).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [§4](#4-project-profile-adjustments--foundation-summary) (all foundation documents).
  - Related future modules: Project Profiles (KBDL-010).
  - Validation method: Manual cross-profile review once the project-profiles module is approved.

- **KBDL-FND-009** — The recommended color values in
  [color.md §3](color.md#3-recommended-default-foundation) **should** be
  adopted as KBDL's default neutral and accent families, pending
  project-owner approval; a project **may** substitute its own accent hue
  within the accent role per
  [color.md §2.8](color.md#28-project-customization-boundaries).
  - Lifecycle: Recommended (requires project-owner approval before this
    becomes `Approved`). Provenance: Assumed. Validation: Verified for the
    contrast calculations only (see [color.md §4](color.md#4-contrast-evidence-illustrative-not-a-theme-mapping)); Not verified for suitability as a final brand palette.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [color.md §3–§4](color.md#3-recommended-default-foundation).
  - Related future modules: Adaptive Themes (KBDL-004).
  - Validation method: Contrast calculation (completed, see evidence); brand suitability review (not yet performed).

- **KBDL-FND-010** — The recommended type-scale ratios and typeface
  strategy in [typography.md §3](typography.md#3-type-scale-and-text-roles)
  and [§6](typography.md#6-recommended-default-type-strategy) **should**
  be adopted pending project-owner approval and typeface-licensing
  verification.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not verified.
  - Related principle: [principles.md §6.3](../principles.md#63-consumer-comprehension).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [typography.md §3, §5, §6](typography.md#3-type-scale-and-text-roles).
  - Related future modules: Components (KBDL-008/009).
  - Validation method: Licensing verification (not yet performed) plus project-owner review.

- **KBDL-FND-011** — The recommended 8-step spacing scale and named
  breakpoint set in [spacing-layout.md §1.3](spacing-layout.md#13-recommended-modular-spacing-system)
  and [§3.6](spacing-layout.md#36-recommended-breakpoint-set) **should**
  be adopted pending project-owner approval.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not verified.
  - Related principle: [principles.md §7](../principles.md#7-visual-consistency).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [spacing-layout.md §1.3, §3.6](spacing-layout.md#13-recommended-modular-spacing-system).
  - Related future modules: Responsive Behavior (KBDL-006).
  - Validation method: Project-owner review; exact pixel values validated once chosen.

- **KBDL-FND-012** — The recommended 5-step corner system and 5-level
  elevation scale in [shape-depth.md §1.3](shape-depth.md#13-recommended-corner-system)
  and [§3.2](shape-depth.md#32-recommended-semantic-elevation-scale)
  **should** be adopted pending project-owner approval.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not verified.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related foundation section: [shape-depth.md §1.3, §3.2](shape-depth.md#13-recommended-corner-system).
  - Related future modules: Adaptive Themes (KBDL-004).
  - Validation method: Project-owner review.

## 8. Traceability

See [traceability-matrix.md](../traceability-matrix.md) for how each
`KBDL-FND-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](../decision-register.md) for any decision recorded
as part of this module.
