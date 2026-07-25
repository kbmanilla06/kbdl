# KBDL Themes — Adaptation, Contexts, and Cross-Cutting Rules

Lifecycle status: `Approved` for the architecture and rules — the
Surface and Elevation Requirements below, §1 (project-override
boundaries), §2 (local-context architecture), and §7's transition
*requirements* (all directly derived from approved principles and
foundations). `Recommended` for the specific values — §3 (transparency
opacity), §4 (gradient strategy), §5 (status-family colors), and §6
(color-value expression convention) — pending project-owner approval;
see
[themes/README.md § Theme Decision Packet](README.md#10-theme-decision-packet).

Return to the [themes index](README.md) · [specification index](../README.md).

---

## Surface and Elevation Requirements (cross-reference)

Exact per-mode elevation values live in
[light-theme.md §1](light-theme.md#1-canvas-and-surfaces) and
[dark-theme.md §1](dark-theme.md#1-elevation-strategy) /
[dark-theme.md §2](dark-theme.md#2-canvas-and-surfaces). The
cross-cutting requirements every mode must satisfy, derived from
[foundations/shape-depth.md §3.1](../foundations/shape-depth.md#31-required-principles-approved):

- Depth **must** remain understandable without blur — a border or
  spacing cue must accompany every elevation change.
- Shadows **must not** be the only separator between surfaces; light
  mode pairs shadow with border/spacing, dark mode pairs a lightness
  step with a mandatory border (see [dark-theme.md §1](dark-theme.md#1-elevation-strategy)).
- Modal and Temporary-overlay surfaces **must** remain visually distinct
  from Raised/Floating surfaces (via the scrim, in the modal case, and
  via transience/positioning, in the overlay case).
- Sticky surfaces **must** preserve separation from the content
  scrolling beneath them at all times, not only at rest.
- Lower-performance contexts **must** support a simplified depth
  fallback — border-only separation, no shadow — per
  [foundations/shape-depth.md §3.6](../foundations/shape-depth.md#36-simplified-depth-fallback).
- Dark-mode elevation **must not** depend only on lighter backgrounds —
  the mandatory border requirement in
  [dark-theme.md §1](dark-theme.md#1-elevation-strategy) exists
  specifically to satisfy this.
- Light-mode elevation **must not** become a stack of indistinguishable
  white cards — every Raised/Floating/Modal/Overlay surface in
  [light-theme.md §1](light-theme.md#1-canvas-and-surfaces) is required
  to pair its shared `neutral-0` background with a border or shadow cue.

Exact shadow parameters (blur radius, offset, spread) remain outside
KBDL-004 unless already approved; none are introduced here.

## 1. Project-Controlled Adaptation

Projects may adapt a KBDL theme without fragmenting the system, within
these documented limits.

### 1.1 Projects may control

- **Accent expression** — a project may substitute its own accent hue
  within the accent role, per
  [foundations/color.md §2.8](../foundations/color.md#28-project-customization-boundaries),
  provided the replacement independently meets the same contrast
  requirements documented for `accent-30`/`accent-50` in
  [light-theme.md](light-theme.md)/[dark-theme.md](dark-theme.md).
- **Neutral temperature** — a project may shift the neutral scale's
  undertone (cooler/warmer), provided the shifted scale is re-verified
  against every contrast pair in
  [light-theme.md](light-theme.md)/[dark-theme.md](dark-theme.md) that
  uses it.
- **Surface richness** — a project may increase or decrease shadow/
  border intensity within the approved elevation model
  ([foundations/shape-depth.md §3.5](../foundations/shape-depth.md#35-profile-level-intensity)).
- **Border prominence** — within the roles and contrast floors defined
  in [semantic-roles.md §1.3](semantic-roles.md#13-borders-and-focus).
- **Gradient intensity** — within the bounds in [§4](#4-gradient-strategy),
  once approved.
- **Media-overlay treatment** — within the contrast rules in
  [§3](#3-transparency-and-glass-like-effects).
- **Profile-specific visual emphasis** — per
  [themes/README.md §8](README.md#8-project-profile-theme-interpretation).

### 1.2 Projects must not

- Change a semantic role's **meaning** (e.g., repurposing Critical for a
  non-error use).
- **Remove** a required role from
  [semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory).
- **Weaken contrast** below the threshold documented for any role.
- **Replace** the Focus indicator treatment or reduce its contrast.
- Make status colors **indistinguishable** from each other or from the
  accent role.
- **Override an explicit user preference** without an approved exception
  (see [themes/README.md §5](README.md#5-theme-selection-precedence)).
- Create **unrelated light and dark identities** — the two modes of a
  project theme must still satisfy the parity rules in
  [semantic-roles.md §2](semantic-roles.md#2-semantic-parity).
- Use a **separate theme architecture per profile** — Showcase,
  Precision, and Flow share one project theme, adjusted only by emphasis
  (`KBDL-THM-006`).

### 1.3 Project theme documentation requirement

Every project theme **must** document:

- Parent KBDL theme (light/dark base this project theme extends).
- Controlled overrides applied (from §1.1 only).
- Reason for each override.
- Confirmation of light/dark parity (re-run the parity matrix from
  [semantic-roles.md §2](semantic-roles.md#2-semantic-parity)).
- Contrast evidence for every overridden pair.
- Accessibility impact of each override.
- Profile applicability.
- Approval status (a project theme is itself subject to the same
  lifecycle/provenance/validation model as any KBDL decision).

## 2. Local Contrast Contexts

A **local contrast context** is a bounded region that remaps a subset of
semantic roles for a specific purpose, without becoming a separate
theme or triggering an uncontrolled global switch.

### 2.1 Defined contexts

| Context | When used | Roles remapped |
| --- | --- | --- |
| Default | The theme's normal presentation. | None (baseline). |
| Inverse | A bounded region using the opposite luminance direction (e.g., a dark call-out band inside a light page). | Canvas/Base → Inverse surface; Primary/Secondary text → Inverse text; borders re-verified against the inverse surface. |
| Accent | A bounded region emphasizing the accent role (e.g., a promotional banner). | Base surface → Accent surface; text roles re-verified against it. |
| Media-overlay | Text or controls placed directly over media. | Canvas/Base → Media overlay; text → the role verified against the overlay, not the raw media. |
| Status | A bounded region communicating a status (e.g., an alert banner). | Base surface → the relevant status Subtle/Strong surface; text/icon/border → the matching status roles. |
| High-emphasis promotional | A bounded, intentionally maximal-impact moment (Showcase primarily). | May combine Accent + Inverse + Gradient roles, still subject to every rule below. |

### 2.2 Rules

- A context is **bounded** — it applies to a defined region, never the
  whole page, and never persists after the user navigates away from
  that region.
- **Remapped roles only**: a context changes which semantic roles apply
  to a region; it never introduces a role outside
  [semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory).
- **Context boundaries must be communicated** visually (a container
  edge, spacing, or explicit surface change) so users perceive where the
  context begins and ends.
- **Nested contexts** are permitted only when each nested level's
  contrast is independently re-verified against its actual immediate
  background — an Accent context nested inside an Inverse context, for
  example, must be checked against the Inverse surface, not the page's
  Default surface.
- **Focus must remain visible** inside any context — the Focus
  indicator's contrast is re-verified against that context's surface.
- **Interactive elements retain their meaning** — a Primary action
  inside an Inverse context is still the page's primary action; a
  context changes appearance, not semantics.
- **Status meaning must not be redefined** by a context — a Status
  context uses the real status roles, never a look-alike substitute.
- Local contexts are how KBDL supports bounded visual variety **without**
  the prohibited behaviors in §2.3.

### 2.3 Prohibited

- A **theme change triggered merely by scroll position** without a
  predictable design reason (a Status or Inverse context entering the
  viewport as *content*, by design, is permitted; an arbitrary scroll-
  linked global theme flip is not).
- **Rapid alternating light and dark sections** without a clear content
  reason — this creates a strobing effect and harms readability.
- **Content-based automatic switching that causes flashing or
  disorientation** — a context transition must be as calm as the
  guidance in [§7](#7-theme-transition-guidance).
- **Local contexts that redefine status meaning.**
- **Nested contexts with unresolved contrast** — every nesting
  combination actually used must have documented evidence, not an
  assumption that "it probably still passes."

## 3. Transparency and Glass-Like Effects

Per [principles.md §1](../principles.md#1-identity-statement) and
[foundations/color.md §2.6](../foundations/color.md#26-transparency-constraints),
translucency is a **controlled, optional** effect, never a foundational
requirement.

### 3.1 Requirements

- Translucency is **optional** — every translucent surface has a
  documented non-translucent fallback (see §3.2 for the Scrim example).
- Text and controls placed over a translucent surface **must** remain
  readable against the **worst plausible background** that could appear
  behind it, not just an assumed neutral case.
- **Blur cannot substitute for contrast** — if content is hard to read
  through a translucent surface, the fix is opacity/contrast, never
  additional blur.
- A **non-translucent fallback must exist conceptually** for every
  translucent role (e.g., matching an operating-system "reduce
  transparency" setting).
- **Focus indicators must remain visible** through any translucent
  surface they appear on or near.
- **Status meaning must not depend on transparency** — a status role's
  meaning is carried by its hue/icon/label, never by how transparent its
  surface is.
- **Large translucent areas must be limited** — translucency is
  appropriate for bounded surfaces (scrims, overlays), not full-page
  backgrounds.
- **Mobile and lower-performance contexts** may simplify or remove
  translucent effects entirely, falling back to the solid value.
- **Precision** should use translucency more conservatively than
  **Showcase** marketing moments; **Flow** should prioritize trust and
  clarity over decorative translucency.

### 3.2 Documented Translucent Roles (from light/dark-theme.md)

| Role | Light | Dark | Non-translucent fallback |
| --- | --- | --- | --- |
| Scrim / backdrop | `neutral-100` at reduced opacity | `neutral-100` at increased opacity | Solid `neutral-90` (light) / solid `neutral-100` (dark) |
| Accent surface | `accent-50` tint | `accent-30` tint | Solid `neutral-20` (light) / solid `neutral-90` (dark) with an accent border instead |
| Selection background | `accent-50`/`accent-30` tint | (same) | Solid `neutral-20`/`neutral-90` with underline emphasis |
| Media overlay | `neutral-100` graduated opacity | (same) | A solid caption band (see Media caption role) |

### 3.3 Validation Checklist for Translucent Surfaces

Before a translucent surface may be marked `Verified`:

- [ ] Contrast tested against the lightest plausible background it can
      appear over.
- [ ] Contrast tested against the darkest plausible background it can
      appear over.
- [ ] A non-translucent fallback is documented and independently passes
      contrast.
- [ ] Focus indicator contrast re-verified through the translucent
      surface.
- [ ] Confirmed the surface is bounded, not full-page.
- [ ] Confirmed status meaning (if any) does not depend on the
      transparency itself.

All four translucent roles in §3.2 remain `Not verified` against a
worst-case background — see
[validation.md § Items Not Verified](validation.md#5-items-not-verified) —
because no specific opacity value has been approved yet.

## 4. Gradient Strategy

Extends the pending recommendation in
[foundations/color.md §3.4](../foundations/color.md#34-restrained-gradient-strategy).
Status: `Recommended`, `Assumed` provenance, `Not verified` beyond the one
worked example below.

### 4.1 Permitted purposes

- **Accent gradients** — the approved `accent-50`/`accent-30` pairing,
  reinforcing an existing hierarchy relationship (see
  [light-theme.md §6](light-theme.md#6-media-and-decorative-context)/
  [dark-theme.md §7](dark-theme.md#7-media-and-decorative-context)).
- **Surface gradients** — a subtle tonal gradient within the neutral
  scale, for large bounded Showcase surfaces only.
- **Media overlays** — a graduated-opacity neutral gradient supporting
  caption legibility (see §3.2).

### 4.2 Prohibited

- Gradients used to **rescue weak hierarchy** — if removing a gradient
  breaks comprehension, the underlying hierarchy was wrong.
- **Uncontrolled multi-hue backgrounds** (more than the two approved
  anchor colors per gradient).
- **Animated gradients** — explicitly out of scope for KBDL-004; any
  future animated gradient is a KBDL-005 (Motion) decision.
- **Status meaning conveyed only by a gradient.**
- **Text over a gradient without worst-case contrast review** (see §4.3).
- Gradient use that makes light and dark themes **unrelated** — both
  modes use the same two-anchor accent gradient, only reordered (light:
  `accent-50 → accent-30`; dark: `accent-30 → accent-50`) to keep the
  higher-contrast-for-that-mode accent step nearer any overlaid text.

### 4.3 Worked Example — Worst-Case Contrast

For the Showcase hero gradient (`accent-50 → accent-30` in light mode),
text placed over it uses `neutral-10` content. The worst case is the
*lightest* stop (`accent-30`, `#A9ACFF`):

- `neutral-10` `#F5F6F8` on `accent-30` `#A9ACFF`: this pair has **not**
  been calculated and is recorded as `Not verified` — see
  [validation.md § Items Not Verified](validation.md#5-items-not-verified).
  Any project adopting this gradient with overlaid text must run this
  calculation before marking the combination `Verified`.

### 4.4 Reduced-complexity fallback and profile intensity

- A **reduced-complexity fallback** (a flat fill using the gradient's
  darker anchor color) must be available for lower-performance contexts.
- **Showcase** is the primary user of gradients; **Precision** and
  **Flow** use them rarely, and never as a primary-action or data
  background.

## 5. Status-Family Theme Behavior

Extends the pending recommendation in
[foundations/color.md §3.3](../foundations/color.md#33-supporting-status-families).
Status: `Recommended`, `Assumed` provenance, `Verified` for the contrast
pairs shown (see [validation.md](validation.md)).

### 5.1 Requirements

- Every normal-sized status text pair **must** meet 4.5:1 against its
  documented surface.
- Statuses **must** remain distinguishable without color alone (icon or
  label always required, per [semantic-roles.md §1.5](semantic-roles.md#15-status)).
- **Caution and Positive must not collapse** into similar luminance and
  meaning — light-mode Caution (`#8A5A00`, 5.93:1) and Positive
  (`#146B3A`, 6.57:1) are distinct hues at distinct luminance; dark-mode
  Caution (`#E0A840`) and Positive (`#6FD19A`) likewise.
- **Critical must remain distinct from the accent** — light-mode
  Critical (`#B3261E`, a red) versus accent (`#4A4EE0`, an indigo-
  violet) are unrelated hues; dark-mode Critical (`#FF8A80`) versus
  accent (`#A9ACFF`) likewise.
- **Status surfaces must remain legible in both modes** — see the
  Subtle- and Strong-surface rows in
  [light-theme.md §5](light-theme.md#5-status-families) and
  [dark-theme.md §6](dark-theme.md#6-status-families).
- **No status value may be marked `Approved`** without project-owner
  approval — writing or contrast-testing these values (as done here)
  does not approve them.

### 5.2 Two documented restrictions

Informational (`#2F6FED`) is the status hue with the least contrast
margin, and fails 4.5:1 in two light-mode contexts:

- **On-strong-surface content** (`neutral-10` on `#2F6FED` fill):
  **4.21:1** — below the 4.5:1 normal-text threshold, though above the
  3:1 large-text/icon threshold.
- **Text directly on the Informational Subtle surface**
  (`#2F6FED` on `neutral-20`): **3.78:1** — also below 4.5:1, and below
  even the 3:1 large-text threshold.

Both roles are therefore restricted: Informational badges, fills, and
subtle-surface text in light mode **must** use large text or an
icon-only treatment, never small normal-weight text, until a darker
Informational hue is proposed and re-verified. This restriction does not
apply to Informational text used directly on the Base or Canvas surface
(4.55:1, passes), only to the two surface combinations above.

## 6. Color-Value Expression

Extends the pending recommendation in
[foundations/color.md §3.5](../foundations/color.md#35-consistent-value-expression-method).
Status: `Recommended`, `Assumed` provenance, `Not applicable` validation
(a documentation convention, not a testable claim).

### 6.1 Recommendation

- **Canonical format:** 6-digit hex (`#RRGGBB`), as already used
  throughout [light-theme.md](light-theme.md) and
  [dark-theme.md](dark-theme.md) — the most broadly portable, human-
  readable, and tool-independent web format.
- **Optional perceptual-space reference:** a project **should** add an
  OKLCH or CIELAB equivalent for design-review purposes once a color-
  tooling decision is made; this is not required to use this
  specification.
- **Human-readable semantic name:** every value is referenced by its
  role name (e.g., "Secondary text") and its foundation-scale name
  (e.g., `neutral-50`), never by a bare hex code alone in prose.
- **Contrast evidence:** every exact pair states its ratio and pass/fail
  result directly in the surrounding text, not only in a table (per the
  Documentation UX requirement to "explain contrast results in text as
  well as numbers").
- **Gamut limitations:** hex/sRGB values may render slightly differently
  on wide-gamut displays; this is a known, accepted limitation pending a
  future color-space decision.
- **Fallback behavior:** if a future token format cannot represent a
  value exactly, the nearest in-gamut equivalent is used, and the
  substitution is documented.
- **Future token portability:** this convention intentionally avoids
  committing to CSS custom properties, a specific token-file format, or
  any implementation technology.

## 7. Theme-Transition Guidance

Status: `Recommended`, `Assumed` provenance, `Not verified`. No duration,
easing, or animation-distance value is introduced — all belong to
KBDL-005 (Motion).

### 7.1 Requirements

- Theme changes **must not** block interaction — the interface remains
  usable while a transition (if any) plays.
- Theme changes **must not** flash large high-contrast regions — a
  transition, once timed in KBDL-005, must avoid a jarring instant among
  large areas.
- Content **must** remain readable throughout any transition — no
  intermediate state may drop below the applicable contrast threshold.
- Transition behavior **must** work correctly when motion is disabled —
  an instant, non-animated theme swap is always a valid fallback.
- **Reduced-motion preference must be respected** — this is a locked
  accessibility requirement, not a controlled variable.
- **Initial page rendering should avoid** an unnecessary incorrect-theme
  flash (e.g., briefly rendering light mode before applying a persisted
  dark preference).
- **Media, charts, and overlays must update coherently** — if a theme
  change affects a chart's colors, all affected elements update
  together, not piecemeal.
- **Focus and selection states must not disappear** during a transition.

### 7.2 Elements that may transition, change immediately, or must not animate

- **May transition:** surface background colors, border colors, text
  colors (a smooth cross-fade is acceptable once timed by KBDL-005).
- **Should change immediately:** the Focus indicator's presence and
  position (its color may transition, but its visibility must never
  lapse).
- **Must not animate:** anything already respecting a reduced-motion
  preference — for those users, every change is instant.

### 7.3 Failure and fallback behavior

If a transition mechanism is unavailable or fails, the theme change
**must** still apply correctly and immediately — an instant switch is
always an acceptable fallback, never a broken or partial theme state.
