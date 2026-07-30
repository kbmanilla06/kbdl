# KBDL Themes — Index

> **KBDL Design Language v1 — active guidance.** Per-requirement
> lifecycle and approval labels below are historical provenance annotations
> from the retired specification programme; they are not pending decisions and
> they do not gate v1. Concrete values are consolidated in
> [tokens](../tokens/README.md). Values a project may legitimately vary are
> labelled *Project-controlled*, not unresolved. See [STATUS](../STATUS.md).

**Updated under KBDL-004-A1.** The project owner approved all ten items
in the theme decision packet (§10.2) — see
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).
Lifecycle status is `Approved` for: the terminology, semantic-role
architecture, semantic parity, profile-sharing rule, and the narrow
precedence/override cores that were already directly supported by a
prior KBDL decision (see [§9](#9-normative-requirements)); **and now
also** the full six-level selection-precedence ordering, persistence
guidance, the detailed project-override list, the local-contrast-context
set, the conceptual theme-transition guidance (beyond the pre-existing
reduced-motion rule), the **exact opaque semantic-role mappings** (light
and dark theme values), **status-family theme colors**, the **opaque-
caption-band gradient strategy**, and **color-value expression
convention**. Lifecycle status remains `Recommended`/`Not verified` for
everything explicitly excluded from that approval — Accent-surface,
Scrim, and Selection-background opacity; any translucent caption-band
variant; project-specific media composites; account synchronization;
high-contrast/forced-colors mode; the full data-visualization palette;
and all implementation-layer choices (see
[§10.3](#103-unresolved-or-not-approval-ready)). Approval is a lifecycle
change; it is separate from, and does not itself constitute,
implementation validation — see [§9](#9-normative-requirements) for each
requirement's own Validation status.

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
see [§10](#10-theme-decision-packet-approved-under-kbdl-004-a1).

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

**Updated under KBDL-004-A1:** all sixteen requirements below are now
`Approved`. `KBDL-THM-001`, `KBDL-THM-002`, `KBDL-THM-003` (narrowed
core), `KBDL-THM-005` (narrowed core), `KBDL-THM-006`, and
`KBDL-THM-012a` were `Approved` prior to KBDL-004-A1, each directly and
explicitly supported by a prior approved KBDL decision. `KBDL-THM-004`,
`KBDL-THM-007` through `KBDL-THM-015` were `Recommended` and became
`Approved` under KBDL-004-A1, per the project owner's explicit approval
of the ten-item theme decision packet — see
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).
`KBDL-THM-007`, `KBDL-THM-008`, and `KBDL-THM-010` are approved with a
narrowed scope (opaque mappings / opaque caption-band gradient only) —
their own entries below state exactly what remains excluded. Approval is
a lifecycle change, separate from validation: writing or contrast-
testing a requirement never made it `Approved`, and approval does not
itself constitute implementation validation — see each requirement's own
Validation status.

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

- **KBDL-THM-003** — *(Narrowed under KBDL-004-R1 to its approved core;
  the full precedence ordering moved to `KBDL-THM-013`.)* Explicit
  current-session or persisted user theme choice **must** take
  precedence over system preference where a theme control exists; system
  preference **must** be used only when no explicit user choice exists.
  - Lifecycle: Approved — directly and explicitly stated in the KBDL-004
    preconditions ("explicit user theme choice taking precedence where a
    control exists" and "system preference as the default source when no
    user choice exists"). Provenance: Confirmed. Validation: Not
    verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-theme-selection-precedence).
  - Related future modules: Components.
  - Validation method: Manual review of precedence logic once implemented.

- **KBDL-THM-004** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  Theme preference persistence **must not** require authentication,
  **must not** contain sensitive personal information, and **must not**
  block product use on failure.
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).
    Validation: Not verified — approval authorizes this baseline; it does
    not itself constitute implementation validation.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-persistence-guidance).
  - Related future modules: Not applicable.
  - Validation method: Manual review of persistence design once implemented (not yet performed — approval does not require this to have happened).

- **KBDL-THM-005** — *(Narrowed under KBDL-004-R1 to its approved core;
  the detailed permitted-override list moved to `KBDL-THM-014`.)* A
  project theme **must not** weaken contrast, remove the Focus indicator
  treatment, or otherwise reduce accessibility below the threshold
  documented for any semantic role, regardless of any other
  customization it applies.
  - Lifecycle: Approved — directly derived from the locked, already-
    approved accessibility rule in
    [governance.md § KBDL-GOV-002](../governance.md#kbdl-gov-002--accessibility-requirements-are-protected)
    and [principles.md §6.8](../principles.md#68-accessibility-by-default);
    accessibility cannot be weakened by a project override. Provenance:
    Confirmed. Validation: Not verified.
  - Related principle: [principles.md §5](../principles.md#5-stable-and-variable-identity-elements).
  - Related foundation requirement: `KBDL-FND-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §1.2](adaptation.md#12-projects-must-not).
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

- **KBDL-THM-007** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
  — narrowed to the opaque scope actually approved, since
  [light-theme.md](light-theme.md) also documents unresolved opacity
  values that remain outside this approval.)* KBDL projects **must** use
  the **exact opaque semantic mappings** in [light-theme.md](light-theme.md)
  — every role **except** Accent-surface, Scrim, and Selection-background
  opacity, which remain `Recommended`/`Not verified` and are **excluded**
  from this approval (see
  [validation.md §5](validation.md#5-items-not-verified)).
  - Lifecycle: Approved (opaque mappings only; the three excluded opacity
    values remain Recommended). Provenance: User-provided (project-owner
    approval). Validation: Verified for the opaque contrast pairs listed
    in [light-theme.md](light-theme.md) and [validation.md](validation.md);
    Not verified for the excluded opacity values or for suitability
    beyond the tested pairs.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: `KBDL-FND-001`, `KBDL-FND-009`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [light-theme.md](light-theme.md).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-008** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
  — narrowed to the opaque scope actually approved, since
  [dark-theme.md](dark-theme.md) also documents unresolved opacity
  values that remain outside this approval.)* KBDL projects **must** use
  the **exact opaque semantic mappings** in [dark-theme.md](dark-theme.md)
  — every role **except** Accent-surface, Scrim, and Selection-background
  opacity, which remain `Recommended`/`Not verified` and are **excluded**
  from this approval (see
  [validation.md §5](validation.md#5-items-not-verified)).
  - Lifecycle: Approved (opaque mappings only; the three excluded opacity
    values remain Recommended). Provenance: User-provided (project-owner
    approval). Validation: Verified for the opaque contrast pairs listed
    in [dark-theme.md](dark-theme.md) and [validation.md](validation.md);
    Not verified for the excluded opacity values or for suitability
    beyond the tested pairs.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: `KBDL-FND-001`, `KBDL-FND-009`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [dark-theme.md](dark-theme.md).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-009** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL projects **must** use the status-family theme mappings in
  [adaptation.md §5](adaptation.md#5-status-family-theme-behavior).
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval). Validation: Verified for the contrast pairs listed (see
    validation.md); Not verified for suitability beyond the tested pairs.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: `KBDL-FND-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §5](adaptation.md#5-status-family-theme-behavior).
  - Related future modules: Components.
  - Validation method: WCAG relative-luminance contrast calculation (completed, see validation.md); project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-010** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
  — scoped to the **opaque caption-band** gradient strategy already
  documented in [adaptation.md §4](adaptation.md#4-gradient-strategy);
  any translucent caption-band variant remains outside this approval,
  per that same section.)* KBDL projects **must** use the two-anchor
  accent gradient strategy in
  [adaptation.md §4](adaptation.md#4-gradient-strategy); a gradient
  **must not** be used to rescue weak hierarchy or convey status meaning
  alone, and text **must not** be placed directly on raw gradient
  pixels.
  - Lifecycle: Approved (opaque caption-band strategy only; translucent
    variants remain Not verified and excluded). Provenance: User-provided
    (project-owner approval). Validation: Verified for the opaque
    caption-band pair and both gradient endpoints (see validation.md);
    Not verified for any translucent variant.
  - Related principle: [principles.md §2](../principles.md#2-digital-luxury).
  - Related foundation requirement: Not applicable (extends the pending
    [color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy)
    recommendation).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §4](adaptation.md#4-gradient-strategy).
  - Related future modules: Motion (KBDL-005, for any future animated variant, explicitly out of scope here).
  - Validation method: Manual review of worst-case text-over-gradient contrast (performed for the documented example, see validation.md); project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-011** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL projects **must** use the color-value expression convention in
  [adaptation.md §6](adaptation.md#6-color-value-expression); it **must
  not** be treated as requiring a specific CSS function or token format.
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval). Validation: Not applicable (a documentation convention,
    not a testable claim).
  - Related principle: Not applicable.
  - Related foundation requirement: Not applicable (extends the pending
    [color.md §3.5](../foundations/color.md#35-consistent-value-expression-method)
    recommendation).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §6](adaptation.md#6-color-value-expression).
  - Related future modules: Not applicable.
  - Validation method: Project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-012** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL projects **must** follow the conceptual theme-transition guidance
  in [adaptation.md §7](adaptation.md#7-theme-transition-guidance); exact
  durations and easing **must not** be introduced here (deferred to
  KBDL-005). This requirement covers only the *conceptual*, KBDL-004-
  specific transition guidance (which elements may/must-not animate,
  initial-render-mismatch avoidance, etc.) — the pre-existing requirement
  that reduced-motion preference **must** be respected is a separate,
  already-`Approved` accessibility rule (`KBDL-THM-012a`, see below),
  unaffected by this item either way.
  - Lifecycle: Approved (conceptual guidance only; no timing/easing
    value exists or is approved here). Provenance: User-provided
    (project-owner approval). Validation: Not verified.
  - Related principle: [principles.md §6.9](../principles.md#69-performance-aware-enhancement).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §7](adaptation.md#7-theme-transition-guidance).
  - Related future modules: Motion (KBDL-005) — eligible for its own future prompt; not started by this approval.
  - Validation method: Manual review confirming no timing/easing values were introduced (performed); project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-012a** — Reduced-motion preference **must** be respected
  during any theme transition; this is a locked accessibility rule, not
  a controlled or recommended variable, and is unaffected by whether
  `KBDL-THM-012`'s detailed transition guidance is approved.
  - Lifecycle: Approved — directly derived from the already-approved
    enhanced motion-safety requirement
    ([decision-register.md § KBDL-DEC-010](../decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety)).
    Provenance: Confirmed. Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §7.1](adaptation.md#71-requirements).
  - Related future modules: Motion (KBDL-005).
  - Validation method: Manual review confirming reduced-motion behavior is honored once implemented.

- **KBDL-THM-013** — *(Split out of the original `KBDL-THM-003` under
  KBDL-004-R1; approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL themes **must** use the full six-level theme-selection precedence
  in [§5](#5-theme-selection-precedence) — including where required
  accessibility constraints, persisted-versus-current-session ordering,
  approved project-specific policy, and the documented light fallback
  sit relative to one another.
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval). Validation: Not verified.
  - Related principle: [principles.md §6.8](../principles.md#68-accessibility-by-default).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-theme-selection-precedence).
  - Related future modules: Components.
  - Validation method: Manual review of the full precedence flow once implemented; project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-014** — *(Split out of the original `KBDL-THM-005` under
  KBDL-004-R1; approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL projects **must** follow the detailed permitted project-override
  list and documentation requirement in
  [adaptation.md §1.1, §1.3](adaptation.md#1-project-controlled-adaptation).
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval). Validation: Not verified.
  - Related principle: [principles.md §5](../principles.md#5-stable-and-variable-identity-elements).
  - Related foundation requirement: `KBDL-FND-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §1.1, §1.3](adaptation.md#1-project-controlled-adaptation).
  - Related future modules: Components, Customization.
  - Validation method: Manual review of the override list once a project theme exists; project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

- **KBDL-THM-015** — *(Approved under KBDL-004-A1, per
  [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).)*
  KBDL projects **must** use the named local-contrast-context set and
  nesting rules in
  [adaptation.md §2](adaptation.md#2-local-contrast-contexts).
  - Lifecycle: Approved. Provenance: User-provided (project-owner
    approval). Validation: Not verified.
  - Related principle: [principles.md §7](../principles.md#7-visual-consistency).
  - Related foundation requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [adaptation.md §2](adaptation.md#2-local-contrast-contexts).
  - Related future modules: Components.
  - Validation method: Manual review of context usage against the defined set and rules once implemented; project-owner approval (recorded, see [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).

## 10. Theme Decision Packet (Approved under KBDL-004-A1)

**All ten items in §10.2 are `Approved`**, per the project owner's
explicit "APPROVE THEME DECISIONS" response — see
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).
This packet still separates already-approved architecture (§10.1,
provided as context — approved independently of this packet, via prior
KBDL decisions) from the ten decisions the project owner just approved
(§10.2) and items that remain outside this approval (§10.3, still
`Recommended`/`Unresolved`/`Not verified` as applicable). The historical
restructuring performed under KBDL-004-R1/R2 (adding three previously-
missing items and correcting overstated evidence) is preserved below
for context; §10.2 is no longer a request awaiting approval.

### 10.1 Already-Approved Architecture (context only)

Not awaiting approval — provided as context for §10.2. **Narrowed under
KBDL-004-R1** to only what a prior KBDL decision directly and explicitly
supports (see [§9](#9-normative-requirements) for the exact wording of
each corresponding requirement):

- **Color-role architecture, neutral scale, and accent family** —
  [foundations/color.md §1–§3.2](../foundations/color.md#1-architectural-principles-approved),
  approved via [KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
- **Elevation scale and corner/geometric character** —
  [foundations/shape-depth.md](../foundations/shape-depth.md), approved
  via the same decision.
- **Semantic-role architecture and light/dark parity requirement**
  (`KBDL-THM-001`, `KBDL-THM-002`) — directly restates the approved
  color-role architecture and the adaptability-without-fragmentation
  principle.
- **The two core precedence facts** (`KBDL-THM-003`): explicit user
  choice outranks system preference where a control exists; system
  preference applies only absent an explicit choice. **The full six-
  level precedence ordering is not included here** — see §10.2, item 6.
- **Accessibility cannot be weakened by a project override**
  (`KBDL-THM-005`, narrowed). **The detailed permitted-override list is
  not included here** — see §10.2, item 8.
- **Profiles share one theme architecture** (`KBDL-THM-006`).
- **Reduced-motion preference must be respected during any theme
  transition** (`KBDL-THM-012a`). **The rest of the transition guidance
  is not included here** — see §10.2, item 10.

### 10.2 Approved Decisions (KBDL-004-A1)

Each item below has a clear, complete scope with all required mappings
present and all required contrast tests passing (or an accurately
disclosed, accepted decorative exemption — never a hidden or
mislabeled failure), and is now `Approved` per
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved):

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs / limitations (accurately disclosed) | Accessibility impact | Performance impact | Privacy impact | Profiles affected | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Light-theme semantic mapping — **opaque mappings only** | Adopt the **exact opaque semantic mappings** in [light-theme.md](light-theme.md) — every role except Accent-surface, Scrim, and Selection-background opacity, which are explicitly **excluded** from this item (see §10.3) | Uses only approved foundation values plus the KBDL-004-R2-corrected Informational role assignment; every required normal-text/essential-border pair passes its threshold with a fully-calculated, non-composited value | A higher-contrast, less nuanced 3-value palette (rejected — less expressive, no material benefit) | Four accepted decorative exemptions (Default border 1.46:1, data-display grid 1.20:1, and the equivalent dark-mode pair) never carry required information alone; `neutral-50` remains restricted to large text/non-text/decorative use (unchanged, not a new limitation); the Accent-surface/Scrim/Selection-background *opacity values* are not part of this item at all | All opaque required pairs verified with exact foreground/background values and no alpha compositing; see [validation.md §3](validation.md#3-consolidated-contrast-evidence) | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-001`, `KBDL-FND-009` |
| 2 | Dark-theme semantic mapping — **opaque mappings only** | Adopt the **exact opaque semantic mappings** in [dark-theme.md](dark-theme.md) — every role except Accent-surface, Scrim, and Selection-background opacity, which are explicitly **excluded** from this item (see §10.3) | Independently designed (not inverted); reuses approved values with mode-appropriate step selection | A mechanically inverted light theme (rejected — fails contrast, e.g. `neutral-60` "secondary text" would compute to 3.32:1 on `neutral-100`, below threshold) | One accepted decorative exemption (Default/Subtle border, 2.08:1); the Accent-surface/Scrim/Selection-background *opacity values* are not part of this item at all | All opaque required pairs verified with exact foreground/background values and no alpha compositing; see [validation.md §3](validation.md#3-consolidated-contrast-evidence) | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-001`, `KBDL-FND-009` |
| 3 | Status-family theme values | Adopt light values (Informational revised to `#164499` under KBDL-004-R1; Positive/Caution/Critical unchanged) plus new dark-mode variants in [adaptation.md §5](adaptation.md#5-status-family-theme-behavior) | Every sub-role (text/icon/border/subtle-surface/strong-surface/on-strong-surface-content) now passes 4.5:1 (text) or 3:1 (non-text) in both modes with no restriction | Reusing light-mode hues unchanged in dark mode (rejected — fails contrast against a dark canvas); keeping the original `#2F6FED` Informational value with a large-text-only restriction (rejected under KBDL-004-R1 — a status role must support normal-sized text, not only large text) | None remaining — the two prior Informational failures (3.78:1, 4.21:1) are fully resolved, not merely restricted | All pairs verified, zero restrictions remaining; see [validation.md §3](validation.md#3-consolidated-contrast-evidence) | None | Not applicable | Showcase, Precision, Flow | `KBDL-FND-002` |
| 4 | Gradient strategy — **opaque caption band only** | Adopt [adaptation.md §4](adaptation.md#4-gradient-strategy): the two-anchor accent gradient, with a mandatory rule that text never sits directly on the raw gradient, and must instead sit on a **fully opaque** `neutral-100` caption band. A **translucent** caption band is explicitly **excluded** from this item (see §10.3) | Both gradient endpoints were calculated against both candidate text colors; no single text color passes across the full range (1.94:1–7.32:1), so text is required to sit on a verified, opaque, bounded solid content surface instead | Unrestricted gradient-with-direct-text use (rejected — fails contrast, see [validation.md §3](validation.md#3-consolidated-contrast-evidence)); a translucent caption band (rejected for this item — its effective color would require an alpha-composite calculation against the gradient that has not been performed) | The mandatory opaque-content-surface requirement adds a small amount of composition overhead in exchange for guaranteed legibility | The opaque caption-band pair (`neutral-10` on `neutral-100`, 17.17:1) is directly correct, not composited or inherited; direct gradient-to-text use is prohibited, not left unverified; translucent variants are excluded from this item entirely | Simplified/removed fallback required on constrained devices | Not applicable | Showcase (primary), Precision/Flow (rare) | Extends [color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy) |
| 5 | Color-value expression convention | Hex primary + optional perceptual reference, per [adaptation.md §6](adaptation.md#6-color-value-expression) | Portable, framework-neutral, human-reviewable | A single required CSS function (rejected — couples the spec to one implementation technology) | None significant | Not applicable | Not applicable | Not applicable | Showcase, Precision, Flow | Extends [color.md §3.5](../foundations/color.md#35-consistent-value-expression-method) |
| 6 | Full six-level selection-precedence ordering | Adopt the complete flow in [§5](#5-theme-selection-precedence) (`KBDL-THM-013`) | Only two of the six levels are directly pre-approved (see §10.1); the remaining ordering — where accessibility constraints, project policy, and the light fallback sit — is new KBDL-004 policy requiring its own review | A shorter, three-level precedence (rejected — cannot express project-specific policy or a documented fallback) | None identified | Places accessibility constraints at the top of the order, never below | Not applicable | Not applicable | Showcase, Precision, Flow | None |
| 7 | Persistence baseline | Adopt [§7](#7-persistence-guidance) (`KBDL-THM-004`) | No prior KBDL decision addresses theme persistence specifically; this baseline is new policy, not a restatement | Mandating a specific storage mechanism (rejected — implementation-specific, out of scope) | None identified | Preference must never gate access; failure must not block use | Negligible | No sensitive data stored; not authentication | Showcase, Precision, Flow | None |
| 8 | Detailed project-override boundaries | Adopt the permitted/prohibited lists in [adaptation.md §1.1–§1.3](adaptation.md#1-project-controlled-adaptation) (`KBDL-THM-014`) | New KBDL-004 policy; the narrower "must not weaken accessibility" core is already approved separately (`KBDL-THM-005`) | An unrestricted override model (rejected — risks semantic drift and profile fragmentation) | None identified | The accessibility floor is fixed regardless of this item's approval | Not applicable | Not applicable | Showcase, Precision, Flow | `KBDL-FND-008` |
| 9 | Local contrast contexts | Adopt the named context set and nesting rules in [adaptation.md §2](adaptation.md#2-local-contrast-contexts) (`KBDL-THM-015`) | No prior KBDL decision defines local contexts; new architecture requiring its own review | No bounded-context mechanism at all (rejected — would force projects toward uncontrolled global theme switching instead) | Nested contexts require per-combination contrast re-verification, an ongoing review cost | Focus and status meaning are preserved by rule in every context | Not applicable | Not applicable | Showcase, Precision, Flow | None |
| 10 | Theme-transition guidance (beyond reduced-motion) | Adopt [adaptation.md §7](adaptation.md#7-theme-transition-guidance) (`KBDL-THM-012`) | Prevents flashing/blocking without pre-selecting timing (deferred to KBDL-005); the reduced-motion requirement itself is already approved separately (`KBDL-THM-012a`) | Defining exact durations now (rejected — explicitly out of KBDL-004 scope) | None identified | Reduced-motion is unaffected by this item either way | Must not block interaction | Not applicable | Showcase, Precision, Flow | Motion (KBDL-005) |

### 10.3 Unresolved or Not Approval-Ready

These are explicitly **not** included in §10.2 and are not ready for a
project-owner approval decision:

- **Unverified opacity values** — Accent-surface, Scrim, and Selection-
  background opacity (both modes; see
  [validation.md §5](validation.md#5-items-not-verified)). No exact
  opacity has been calculated against a worst-case background.
- **Any translucent caption-band variant** (gradient or media) — the
  opaque caption band used in §10.2 items 1, 2, and 4 is `Verified`; a
  translucent version of that same band is a different, uncalculated
  pair (see [validation.md §5](validation.md#5-items-not-verified)).
- **Project-specific media testing** — Media-overlay contrast against
  actual (non-placeholder) images is inherently project-specific.
- **Account-level theme synchronization mechanism.**
- **High-contrast/forced-colors mode** (a separate, explicitly out-of-
  scope theme unless later approved).
- **Full data-visualization categorical palette** — deferred, not yet
  designed.
- **Browser-support policy, implementation framework, token-file
  format, and theme API** — implementation-layer decisions outside a
  design-language specification.

**Exact scope of this approval:** the project owner's "APPROVE THEME
DECISIONS" response authorized exactly items 1–10 above as `Approved`
— specifically, for items 1, 2, and 4, only the **exact opaque semantic
mappings and role assignments** they describe. It did **not** approve
any §10.3 item — in particular, it did **not** approve Accent-surface,
Scrim, or Selection-background opacity, or any translucent caption-band
variant, regardless of whether those values are mentioned elsewhere in
`light-theme.md`/`dark-theme.md`/`adaptation.md` for context. It also
did **not** approve any KBDL-005 or later module's content, and it does
not itself constitute validation of any item — see
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
for the full record.

## 11. Traceability

See [traceability-matrix.md](../traceability-matrix.md) for how each
`KBDL-THM-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](../decision-register.md) for any decision recorded
as part of this module.
