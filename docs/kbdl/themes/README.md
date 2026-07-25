# KBDL Themes — Index

Lifecycle status: `Approved` for the terminology, architecture, selection
precedence, persistence guidance, project-override rules, profile
interpretation, and `KBDL-THM-###` requirements below (derived from
approved KBDL-001/002/003 decisions). The **exact semantic-role mappings**
(light and dark theme values), **status-family theme colors**, **gradient
strategy**, and **color-value expression convention** are `Recommended`,
pending project-owner approval — see
[§10 Theme Decision Packet](#10-theme-decision-packet).

Return to the [specification index](../README.md). Status labels are
defined in [conventions.md §1](../conventions.md#1-status-labels);
requirement IDs in
[conventions.md §2](../conventions.md#2-requirement-identification).

---

## 1. Purpose

This is the entry point for KBDL-004: Adaptive Theme System. It defines
KBDL's theme architecture, terminology, semantic-role inventory, light and
dark mappings, selection precedence, persistence guidance, project-
controlled adaptation, local contrast contexts, and validation model.

Theme documents:

- [semantic-roles.md](semantic-roles.md) — the complete semantic-role
  inventory and light/dark parity rules.
- [light-theme.md](light-theme.md) — the recommended light-theme mapping.
- [dark-theme.md](dark-theme.md) — the recommended dark-theme mapping,
  designed independently, not by inversion.
- [adaptation.md](adaptation.md) — project-controlled adaptation, local
  contrast contexts, surface/elevation mapping, transparency, gradient
  strategy, status-family theme behavior, color-value expression, and
  theme-transition guidance.
- [validation.md](validation.md) — theme validation and conformance,
  including the consolidated contrast-evidence record and parity check.

This module does **not** define motion timings or easing (KBDL-005),
detailed responsive/accessibility rules (KBDL-006), component anatomy, or
implementation code.

## 2. What Was Inspected

Before writing this module, the following were reviewed in full:
[principles.md](../principles.md), [conventions.md](../conventions.md),
[governance.md](../governance.md), [decision-register.md](../decision-register.md)
(`KBDL-DEC-001` through `KBDL-DEC-012`), [traceability-matrix.md](../traceability-matrix.md),
[conformance-checklist.md](../conformance-checklist.md), [glossary.md](../glossary.md),
and every file under [foundations/](../foundations/README.md), with
particular attention to [foundations/color.md](../foundations/color.md)
and [foundations/shape-depth.md](../foundations/shape-depth.md).

**Confirmed approved (usable without new approval):** the color-role
architecture; the neutral scale (`neutral-0` through `neutral-100`,
including the `neutral-50`/`neutral-60` contrast-safe distinction from
KBDL-003-R1); the accent family (`accent-30`, `accent-50`); the
five-level elevation scale and its purposes; the corner system and
geometric character; the shared-foundation-across-profiles rule
(`KBDL-FND-008`) — all per
[KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).

**Confirmed still pending (not approved by KBDL-DEC-012 or any later
decision):** the status-family color values
([color.md §3.3](../foundations/color.md#33-supporting-status-families)),
the gradient strategy
([color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy)),
and the color-value expression convention
([color.md §3.5](../foundations/color.md#35-consistent-value-expression-method)).
No decision after `KBDL-DEC-012` changes this. This module reviews and
extends these three pending items but does not itself approve them —
see [§10](#10-theme-decision-packet).

## 3. Theme Terminology

- **Foundation color** — An approved primitive or family-level color from
  KBDL foundations (e.g., `neutral-60`, `accent-50`), independent of any
  theme or mode. See
  [foundations/color.md](../foundations/color.md).
- **Semantic role** — A purpose-based color role (e.g., "primary text,"
  "critical status border") that is independent of a specific visual
  mode. A semantic role is mapped to a foundation color per mode. See
  [semantic-roles.md](semantic-roles.md).
- **Theme** — A complete mapping of every semantic role to a specific
  foundation color, for one mode. "The KBDL light theme" and "the KBDL
  dark theme" are the two themes this module defines.
- **Mode** — The presentation state a theme is active in: `light`,
  `dark`, or `automatic` (system-following). Mode is not the same as
  Project Profile (Showcase/Precision/Flow, see
  [glossary.md](../glossary.md), "Project Profile" entry); a project has one
  Profile and may present in either mode.
- **Project theme** — A project's own controlled variation of a KBDL
  theme, built by adjusting only the controlled overrides permitted in
  [adaptation.md §1](adaptation.md#1-project-controlled-adaptation).
- **Local contrast context** — A bounded region within a page that
  remaps a subset of semantic roles for a specific purpose (inverse,
  accent, media-overlay, status, or promotional), without becoming a
  separate theme. See [adaptation.md §2](adaptation.md#2-local-contrast-contexts).
- **User preference** — An explicit mode choice made by the user through
  a theme control.
- **System preference** — The operating-system or browser-level light/
  dark preference, used when no explicit user preference exists.
- **Project default** — The project's documented fallback mode, used
  when neither a user preference nor a usable system preference is
  available.
- **Theme parity** — The requirement that light and dark themes carry
  the same semantic-role inventory and the same functional meaning for
  each role, even though the exact foundation-color mapping differs. See
  [semantic-roles.md §2](semantic-roles.md#2-semantic-parity).
- **Theme transition** — The visual change that occurs when the active
  theme mapping changes (e.g., light to dark). See
  [adaptation.md §7](adaptation.md#7-theme-transition-guidance).
- **Persistence** — Retaining a user's explicit mode preference across
  sessions or devices. See [§7](#7-persistence-guidance).

"Theme," "mode," and "Project Profile" are never used interchangeably in
this specification: a *mode* (light/dark/automatic) selects which
*theme* is active; a *Project Profile* (Showcase/Precision/Flow) selects
emphasis within whichever theme is active (see
[§8](#8-project-profile-theme-interpretation)).

## 4. Theme Architecture

KBDL's theme system has six ownership layers:

| Layer | Owner | Consumed by | Customizable by projects? | Requires exception to change? |
| --- | --- | --- | --- | --- |
| 1. Foundation values | KBDL (approved, KBDL-003) | All later layers | No | Yes |
| 2. Semantic roles | KBDL (this module) | Themes, components | No (naming/purpose fixed) | Yes |
| 3. Mode-specific semantic mappings (light/dark themes) | KBDL (this module, `Recommended` pending approval) | Project themes, components | No (base mapping fixed once approved) | Yes |
| 4. Project-controlled theme variations | Project, within documented limits | Components | Yes, within [adaptation.md §1](adaptation.md#1-project-controlled-adaptation) | Only beyond documented limits |
| 5. Local contrast contexts | KBDL (architecture) + Project (application) | Components | Yes, application only — the context set itself is fixed | Yes, to add a new context type |
| 6. Component-level theme tokens | Deferred to later component modules | Application code | Not applicable yet | Not applicable yet |

**Aliases and references:** a semantic role may reference another
semantic role directly (e.g., "Selected border uses the same value as
Accent text") rather than duplicating a value; such aliases must be
stated explicitly, not left implicit.

**Retirement and supersession:** a semantic role or mapping is retired
using the `Deprecated`/`Superseded` lifecycle labels from
[conventions.md §1.1](../conventions.md#11-lifecycle--approval-status),
never silently removed.

**Incomplete mappings:** if a semantic role has no mapping yet in one
mode, this is recorded as `Unresolved` with a stated reason in the parity
matrix ([semantic-roles.md §2](semantic-roles.md#2-semantic-parity)) —
never silently omitted.

Layer 6 (component-level tokens) is explicitly out of scope for
KBDL-004.

## 5. Theme Selection Precedence

Given multiple possible sources for the active mode, KBDL resolves them
in this fixed order:

1. **Required accessibility and legibility constraints** — if a
   constraint (e.g., a forced-colors or high-contrast operating-system
   mode) requires a specific presentation, it overrides every source
   below.
2. **Explicit current-session user choice** — a choice the user just
   made in this session (e.g., clicking "Dark" in a theme control).
3. **Persisted user choice** — a previously saved explicit preference,
   loaded at the start of a new session (see [§7](#7-persistence-guidance)).
4. **Approved project-specific mode policy** — a documented, exception-
   approved restriction (e.g., a project that only offers dark mode for
   a specific product reason).
5. **System preference** — the operating-system or browser light/dark
   setting, used when no explicit choice exists at levels 2–4.
6. **Documented KBDL fallback** — light mode, used only when no signal
   exists at any level above.

Rules:

- A project **may** provide a default mode but **must not** silently
  override an explicit user choice (level 2 or 3 always outranks level
  4's default).
- System preference (level 5) is used **only** when no explicit user
  choice exists — it never overrides an explicit choice.
- A project **may** restrict available modes **only** with a documented
  product reason and an approved exception (see
  [governance.md § Exception process](../governance.md#exception-process));
  restricting modes without an exception is a locked-rule violation.
- Accessibility requirements (level 1) always override brand or
  visual-design preference, per
  [principles.md §4](../principles.md#4-relationship-between-luxury-and-utility).
- The selected mode **must** remain stable during a task unless the user
  changes it, or the system preference changes while automatic mode
  (level 5) is active.
- Content entering the viewport **must not** automatically switch the
  global theme without an approved, predictable rule (see
  [adaptation.md §2](adaptation.md#2-local-contrast-contexts) for the
  bounded-local-context alternative).

### Decision flow

```text
Is a required accessibility/legibility constraint active?
├─ Yes → use the constrained presentation (overrides everything below)
└─ No → Does an explicit current-session user choice exist?
    ├─ Yes → use it
    └─ No → Does a persisted user choice exist?
        ├─ Yes → use it
        └─ No → Does an approved project-specific mode policy apply?
            ├─ Yes → use the policy's mode
            └─ No → Is a usable system preference available?
                ├─ Yes → use it (automatic mode)
                └─ No → use the documented KBDL fallback (light)
```

## 6. User Theme Controls

Conceptual requirements for a future theme control (component anatomy is
deferred to a later module):

- **Supported choices:** Light, Dark, System/Auto.
- **Clear current-state indication:** the control always shows which
  choice is currently active, not just available options.
- **Keyboard operability:** fully operable without a pointer.
- **Screen-reader-readable labels:** each choice has a clear, unambiguous
  accessible name; the current state is announced.
- **Touch accessibility:** meets the same touch-target rules as any other
  control (see
  [foundations/spacing-layout.md §1.4](../foundations/spacing-layout.md#14-touch-and-pointer-considerations)).
- **No color-only state communication:** the active choice is indicated
  through more than color alone (e.g., an icon, label, or selected-state
  border per [semantic-roles.md](semantic-roles.md)).
- **No hidden mode change:** a mode never changes as a side effect of an
  unrelated action.
- **Immediate but non-disruptive feedback:** the interface updates
  promptly without a jarring flash (see
  [adaptation.md §7](adaptation.md#7-theme-transition-guidance)).
- **Graceful operation without animation:** the control and its effect
  must work correctly with all transition animation disabled.
- **Behavior when persistence is unavailable:** the control still
  changes the current session's mode even if the choice cannot be saved
  (see [§7 Persistence Guidance](#7-persistence-guidance)).
- **Behavior when the system preference changes:** if automatic mode is
  active, the interface follows the new system preference; if an
  explicit user choice is active, the system-preference change has no
  effect.
- **Behavior when a project does not expose a control:** the project
  must still follow the precedence in [§5](#5-theme-selection-precedence)
  using system preference and the documented fallback.

## 7. Persistence Guidance

Persistence is defined conceptually; no storage API or framework is
prescribed.

- Explicit user preference **may** be retained locally.
- Theme preference **must not** require authentication to set or use.
- Theme preference **must not** contain sensitive personal information —
  it is a presentation setting, never authentication or authorization
  data, and must never be treated as such.
- Account-level synchronization is **optional** and remains project-
  specific unless separately approved.
- A user **must** be able to return to system-following (automatic) mode
  after making an explicit choice.
- Persistence failure **must not** block product use — if saving or
  reading the preference fails, the product still functions, falling
  back per the precedence in [§5](#5-theme-selection-precedence).
- The initial rendered theme **should** minimize an avoidable visible
  mismatch (e.g., a flash of the wrong theme before the persisted or
  system preference is applied).

**Precedence among persistence sources**, consistent with [§5](#5-theme-selection-precedence):
current-session selection → persisted local preference → optional
account preference → system preference → project fallback. Account-sync
behavior is `Unresolved`/project-specific unless a project has an
approved exception describing it.

## 8. Project Profile Theme Interpretation

Showcase, Precision, and Flow share one theme architecture and semantic-
role inventory; they differ only in emphasis, per
[principles.md §9.4](../principles.md#94-shared-constraints-across-profiles)
and [foundations/README.md §4.4](../foundations/README.md#44-shared-constraint-approved).

### Showcase

May emphasize: richer accent surfaces, stronger inverse contexts, more
expressive media overlays, selective gradients (once approved), greater
contrast between visual moments.

Must preserve: reading comfort, stable navigation, theme parity,
accessible media captions, controlled brightness in dark presentation.

### Precision

May emphasize: restrained accent use, strong surface hierarchy,
predictable borders, readable dense information, clear status
differentiation.

Must preserve: scanning speed, low visual noise, stable focus and
selection, non-color state indicators, comfortable extended use.

### Flow

May emphasize: approachable neutral surfaces, clear primary-action
emphasis, reassuring status feedback, balanced media and utility,
comfortable theme defaults.

Must preserve: trust, comprehension, predictable progression, recovery
visibility, mobile clarity.

## 9. Normative Requirements

Lifecycle status `Approved` for `KBDL-THM-001` through `KBDL-THM-006`
(architecture, terminology, precedence, persistence, and profile rules,
directly restating or extending approved KBDL-001/002/003 decisions).
`Recommended` for `KBDL-THM-007` through `KBDL-THM-012` (specific light/
dark mappings, status-family values, gradient strategy, and value-
expression convention), pending project-owner approval — writing or
contrast-testing these does not make them `Approved`.

- **KBDL-THM-001** — KBDL themes **must** use the semantic-role
  architecture in [semantic-roles.md](semantic-roles.md); a theme
  **must not** introduce a role outside that inventory without an
  approved exception.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §7](../principles.md#7-visual-consistency).
  - Related foundation requirement: `KBDL-FND-001`, `KBDL-FND-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory).
  - Related future modules: Components.
  - Validation method: Manual review of role usage against the inventory at each later module's approval gate.

- **KBDL-THM-002** — Light and dark themes **must** maintain semantic
  parity: every required role **must** have a mapping in both modes or a
  documented non-applicability reason; a role **must not** be silently
  omitted from one mode.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Verified (see [semantic-roles.md §2](semantic-roles.md#2-semantic-parity) parity matrix).
  - Related principle: [principles.md §6.7](../principles.md#67-adaptability-without-fragmentation).
  - Related foundation requirement: `KBDL-FND-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [semantic-roles.md §2](semantic-roles.md#2-semantic-parity).
  - Related future modules: Components.
  - Validation method: Parity-matrix completeness check (performed, see validation.md).

- **KBDL-THM-003** — Theme selection **must** follow the precedence in
  [§5](#5-theme-selection-precedence); a project **must not** override an
  explicit user choice, and system preference **must** be used only when
  no explicit choice exists.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-theme-selection-precedence).
  - Related future modules: Components.
  - Validation method: Manual review of precedence logic once implemented.

- **KBDL-THM-004** — Theme preference persistence **must not** require
  authentication, **must not** contain sensitive personal information,
  and **must not** block product use on failure.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-persistence-guidance).
  - Related future modules: Not applicable.
  - Validation method: Manual review of persistence design once implemented.

- **KBDL-THM-005** — A project **may** control theme presentation only
  within the documented boundaries in
  [adaptation.md §1](adaptation.md#1-project-controlled-adaptation); a
  project **must not** change semantic meaning, remove required roles,
  weaken contrast, replace focus treatment, or create unrelated light/
  dark identities.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §5](../principles.md#5-stable-and-variable-identity-elements).
  - Related foundation requirement: `KBDL-FND-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §1](adaptation.md#1-project-controlled-adaptation).
  - Related future modules: Components, Customization.
  - Validation method: Manual review of any project theme against the documented boundaries.

- **KBDL-THM-006** — Showcase, Precision, and Flow **must** share the
  same theme architecture and semantic-role inventory; a profile
  **must not** define a separate theme system.
  - Lifecycle: Approved. Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §9.4](../principles.md#94-shared-constraints-across-profiles).
  - Related foundation requirement: `KBDL-FND-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-project-profile-theme-interpretation).
  - Related future modules: Project Profiles (KBDL-009).
  - Validation method: Manual cross-profile review once the project-profiles module is approved.

- **KBDL-THM-007** — KBDL projects **should** adopt the light-theme
  mapping in [light-theme.md](light-theme.md), pending project-owner
  approval.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Verified
    for the contrast pairs listed in [light-theme.md](light-theme.md) and
    [validation.md](validation.md); Not verified for suitability beyond
    the tested pairs.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: `KBDL-FND-001`, `KBDL-FND-009`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [light-theme.md](light-theme.md).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner review (not yet performed).

- **KBDL-THM-008** — KBDL projects **should** adopt the dark-theme
  mapping in [dark-theme.md](dark-theme.md), pending project-owner
  approval.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Verified
    for the contrast pairs listed in [dark-theme.md](dark-theme.md) and
    [validation.md](validation.md); Not verified for suitability beyond
    the tested pairs.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: `KBDL-FND-001`, `KBDL-FND-009`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [dark-theme.md](dark-theme.md).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner review (not yet performed).

- **KBDL-THM-009** — KBDL projects **should** adopt the status-family
  theme mappings in
  [adaptation.md §5](adaptation.md#5-status-family-theme-behavior),
  pending project-owner approval; a status color **must not** be
  approved or implemented without that approval.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Verified
    for the contrast pairs listed (see validation.md); Not verified for
    suitability beyond the tested pairs.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: `KBDL-FND-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §5](adaptation.md#5-status-family-theme-behavior).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner review (not yet performed).

- **KBDL-THM-010** — The gradient strategy in
  [adaptation.md §4](adaptation.md#4-gradient-strategy) **should** be
  adopted pending project-owner approval; a gradient **must not** be
  used to rescue weak hierarchy or convey status meaning alone.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not
    verified.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: Not applicable (extends the pending
    [color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy)
    recommendation).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §4](adaptation.md#4-gradient-strategy).
  - Related future modules: Motion (KBDL-005, for any future animated variant, explicitly out of scope here).
  - Validation method: Manual review of worst-case text-over-gradient contrast (performed for the documented example, see validation.md).

- **KBDL-THM-011** — The color-value expression convention in
  [adaptation.md §6](adaptation.md#6-color-value-expression) **should**
  be adopted pending project-owner approval; it **must not** be treated
  as requiring a specific CSS function or token format.
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not
    applicable.
  - Related principle: Not applicable.
  - Related foundation requirement: Not applicable (extends the pending
    [color.md §3.5](../foundations/color.md#35-consistent-value-expression-method)
    recommendation).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §6](adaptation.md#6-color-value-expression).
  - Related future modules: Not applicable.
  - Validation method: Project-owner review (not yet performed).

- **KBDL-THM-012** — The theme-transition guidance in
  [adaptation.md §7](adaptation.md#7-theme-transition-guidance)
  **should** be adopted pending project-owner approval; exact durations
  and easing **must not** be introduced here (deferred to KBDL-005).
  - Lifecycle: Recommended. Provenance: Assumed. Validation: Not
    verified.
  - Related principle: [principles.md §6.9](../principles.md#69-performance-aware-enhancement).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §7](adaptation.md#7-theme-transition-guidance).
  - Related future modules: Motion (KBDL-005).
  - Validation method: Manual review confirming no timing/easing values were introduced (performed).

## 10. Theme Decision Packet

This packet separates already-approved architecture (§10.1, provided
only as context) from the specific theme decisions that require
project-owner approval (§10.2) and items not yet ready for approval
(§10.3).

### 10.1 Already-Approved Architecture (context only)

Not awaiting approval — provided as context for §10.2:

- **Color-role architecture, neutral scale, and accent family** —
  [foundations/color.md §1–§3.2](../foundations/color.md#1-architectural-principles-approved),
  approved via [KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
- **Elevation scale and corner/geometric character** —
  [foundations/shape-depth.md](../foundations/shape-depth.md), approved
  via the same decision.
- **Theme architecture, terminology, selection precedence, persistence
  baseline, project-override boundaries, and profile interpretation**
  (this document, §3–§8) — directly derived from approved KBDL-001/002
  governance and principles; not new brand or visual decisions.

### 10.2 Recommended Theme Decisions — Approval Requested

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Performance impact | Privacy impact | Profiles affected | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Light-theme semantic mapping | Adopt [light-theme.md](light-theme.md) in full | Uses only approved foundation values; every text/border pair has documented contrast evidence | A higher-contrast, less nuanced 3-value palette (rejected — less expressive, no material benefit) | None beyond the documented restrictions (e.g., `neutral-50` large-text-only) | All pairs verified per role; see validation.md | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-001`, `KBDL-FND-009` |
| 2 | Dark-theme semantic mapping | Adopt [dark-theme.md](dark-theme.md) in full | Independently designed (not inverted); reuses approved values with mode-appropriate step selection | A mechanically inverted light theme (rejected — explicitly prohibited by this prompt and produces poor dark-mode contrast, as shown by the rejected `neutral-70`/`neutral-60` pairs in validation.md) | Slightly less "value symmetry" between modes, which is intentional | All pairs verified per role; see validation.md | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-001`, `KBDL-FND-009` |
| 3 | Status-family theme values | Adopt light values from [color.md §3.3](../foundations/color.md#33-supporting-status-families) plus new dark-mode variants in [adaptation.md §5](adaptation.md#5-status-family-theme-behavior) | Distinguishable from accent hue-wise; verified contrast in both modes | Reusing light-mode hues unchanged in dark mode (rejected — fails contrast against a dark canvas, see validation.md) | Informational strong-surface content is restricted to large text/icons (4.21:1, below normal-text threshold) | Verified per pair, one documented restriction | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-002` |
| 4 | Gradient strategy | Adopt [adaptation.md §4](adaptation.md#4-gradient-strategy) | Extends the KBDL-003 gradient recommendation with mode-specific and worst-case contrast rules | No gradient support at all (rejected — removes an approved-in-principle controlled variable); unrestricted gradient use (rejected — risk of hierarchy/contrast failure) | Requires discipline to avoid overuse | Worst-case text-over-gradient contrast documented for the one defined example | Simplified/removed fallback required on constrained devices | Not applicable | Showcase (primary), Precision/Flow (rare) | Extends [color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy) |
| 5 | Color-value expression convention | Hex primary + optional perceptual reference, per [adaptation.md §6](adaptation.md#6-color-value-expression) | Portable, framework-neutral, human-reviewable | A single required CSS function (rejected — couples the spec to one implementation technology) | None significant | Not applicable | Not applicable | Not applicable | Showcase, Precision, Flow | Extends [color.md §3.5](../foundations/color.md#35-consistent-value-expression-method) |
| 6 | Persistence baseline | As documented in [§7](#7-persistence-guidance) | Matches the already-approved precedence and accessibility priorities; introduces no new technical choice | Mandating a specific storage mechanism (rejected — implementation-specific, out of scope) | None | Preference must never gate access | Negligible | No sensitive data stored; not authentication | Showcase, Precision, Flow | None |
| 7 | Theme-transition guidance | As documented in [adaptation.md §7](adaptation.md#7-theme-transition-guidance) | Prevents flashing/blocking without pre-selecting timing (deferred to KBDL-005) | Defining exact durations now (rejected — explicitly out of KBDL-004 scope) | None | Must respect reduced-motion preference | Must not block interaction | Not applicable | Showcase, Precision, Flow | Motion (KBDL-005) |

### 10.3 Unresolved or Project-Specific Choices (not ready for approval)

- Account-level theme synchronization mechanism.
- High-contrast/forced-colors mode (a separate, explicitly out-of-scope
  theme unless later approved).
- Browser-support policy, implementation framework, token-file format,
  and theme API — all implementation-layer decisions outside a design-
  language specification.

**Exact scope of a future approval:** an `APPROVE` response to §10.2
would authorize exactly items 1–7 above (the light and dark theme
mappings, status-family values, gradient strategy, value-expression
convention, persistence baseline, and transition guidance) as `Approved`.
It would **not** approve §10.3's unresolved items, and it would **not**
approve any KBDL-005 or later module's content.

## 11. Traceability

See [traceability-matrix.md](../traceability-matrix.md) for how each
`KBDL-THM-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](../decision-register.md) for any decision recorded
as part of this module.
