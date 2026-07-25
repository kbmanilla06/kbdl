# KBDL Foundations — Shape, Borders, and Depth

Lifecycle status of this document's **architecture and rules**: `Approved`,
derived from [principles.md](../principles.md). Lifecycle status of the
**recommended corner system and elevation scale**: `Recommended` —
requires project-owner approval; see
[foundations/README.md § Foundation Status Model](README.md#3-foundation-status-model).

Return to the [foundations index](README.md) · [specification index](../README.md).

This document defines KBDL's shape/corner language, border and divider
system, and elevation/depth model. It does not assign final theme-specific
border colors or shadow values — those belong to KBDL-004.

---

## 1. Shape and Corner Language

This section defines KBDL's shape architecture: required principles,
geometric character, a recommended corner system, and profile/customization
rules.

### 1.1 Required principles (Approved)

- **Shape must communicate structure and hierarchy.** A container's shape
  should signal its role (e.g., a more contained shape for a modal versus
  an inline control), not vary arbitrarily.
- **Corner variation must be systematic.** Corner treatment follows a
  small, named set of options (§1.3), not per-instance values.
- **Pill shapes must not be applied indiscriminately.** A fully rounded
  (pill) shape is reserved for specific roles (see §1.4), not a default
  for every control.
- **Decorative geometry must not interfere with reading or interaction.**
  Any decorative shape element must sit behind content and never overlap
  a focus target or reduce text contrast.
- **Profile variation must not make components appear unrelated.** A
  Showcase card and a Precision card may use different corner intensity
  (see §1.6) but must draw from the same named set (§1.3).

### 1.2 Geometric character (Approved)

Status: `Approved` — this direction was approved by the project owner via
the [foundation decision packet](README.md#6-foundation-decision-packet);
see [KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Provenance: `User-provided`. Validation status: `Not verified` — approval
authorizes this direction as KBDL's default; it does not itself constitute
rendered-usability validation.

KBDL's default geometric character is **softened-structured**: corners
rounded enough to feel approachable and premium, but restrained enough to
preserve a technical, precise character — neither sharp/clinical nor fully
organic/soft. This sits deliberately between the two extremes sometimes
seen in "luxury" (soft, rounded, organic) and "technical" (sharp, angular)
design languages, consistent with
[principles.md §1](../principles.md#1-identity-statement).

### 1.3 Default corner system

Status: `Approved` — approved by the project owner via the
[foundation decision packet](README.md#6-foundation-decision-packet); see
[KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Provenance: `User-provided`. Validation status: `Not verified` for exact
radius values (deferred to implementation); the named classification and
its role assignments are approved.

A limited, named classification (exact radius values deferred):

| Name | Role |
| --- | --- |
| corner-sharp | Rare; reserved for structural, data-dense contexts (e.g., a dense table cell) where softening would reduce density clarity |
| corner-subtle | Default for controls, inputs, and small components |
| corner-standard | Default for cards, panels, and mid-sized surfaces |
| corner-pronounced | Larger surfaces (modals, sheets, hero containers) where a more visible soften reinforces the surface's elevated role |
| corner-pill | Reserved for compact status/tag elements and specific action controls where a fully rounded form aids quick recognition (see §1.4) |

### 1.4 Nested-radius relationships, circular elements, pills and capsules

- A nested element (e.g., a button inside a card) uses a corner value at
  or below its parent's corner intensity, so nested shapes never appear
  "sharper" than their container in a way that reads as inconsistent.
- Circular elements (avatars, icon-only buttons) are a distinct case from
  `corner-pill` — fully circular treatment is reserved for genuinely
  square-aspect content (e.g., an avatar), while `corner-pill` is for
  elongated (rectangular) elements like tags or a search field.
- Pills/capsules communicate "compact, quickly scannable" — appropriate
  for status tags, filter chips, and short action labels; inappropriate
  for primary content containers (cards, panels).

### 1.5 Sharp vs. softened forms, decorative geometry, container/interactive shapes

- **Sharp forms** are the exception (`corner-sharp`), used only where
  density or tabular precision benefits from it.
- **Container shapes** (cards, panels, sheets) draw from `corner-standard`
  or `corner-pronounced`.
- **Interactive shapes** (buttons, inputs, chips) draw from
  `corner-subtle` or `corner-pill` depending on their compactness (§1.4).
- **Decorative geometry** (background shapes, accents) must sit at a
  lower depth layer than content (see §3) and must never be mistaken for
  an interactive element.

### 1.6 Profile-level expression

- **Showcase:** may use `corner-pronounced` more frequently for larger,
  more dramatic surfaces.
- **Precision:** favors `corner-subtle` and occasional `corner-sharp` for
  dense, structured data contexts.
- **Flow:** favors `corner-standard` for a balanced, approachable
  character.

### 1.7 Project customization limits

A project may select its preferred radius *values* for each named step,
but must not: introduce additional named steps beyond §1.3 without an
approved exception, or apply `corner-pill` to primary content containers.

## 2. Borders and Dividers

This section defines KBDL's border and divider architecture: required
principles, semantic roles, hierarchy, and theme/responsive considerations.

### 2.1 Required principles (Approved)

- The system must not depend entirely on shadows for separation — borders
  and dividers are a first-class, independent separation mechanism,
  important for contexts where shadow rendering is reduced or unavailable
  (see §3.6).
- Borders must not create excessive visual noise in dense interfaces;
  Precision layouts should prefer the lightest border weight that still
  achieves clear separation.
- Exact theme-specific border colors belong to KBDL-004; this document
  defines border *roles*, matching the border roles introduced in
  [color.md §2.2](color.md#22-semantic-surface-and-text-roles).

### 2.2 Border and separator roles (Approved architecture)

- **Structural border** — defines a container's outer edge where a
  surface-color change alone is insufficient (e.g., adjacent same-color
  surfaces).
- **Subtle separator** — a light-weight divider between related content
  items within one container (e.g., list rows).
- **Strong separator** — a heavier-weight divider between unrelated
  sections.
- **Focus outline** — always present for keyboard focus, at a weight and
  contrast sufficient to be clearly visible; never removed for aesthetic
  reasons (this is a locked accessibility requirement, not a controlled
  variable).
- **Selected-state outline** — indicates a selected item, always paired
  with a non-border cue (icon, background) so it does not rely on border
  presence alone as its only signal.
- **Status border** — a border-based reinforcement of a status color
  (see [color.md §2.4](color.md#24-status-roles)), used in addition to,
  not instead of, an icon or label.
- **Interactive border** — outlines an interactive control (e.g., an
  input field) at rest, and changes weight/color predictably for hover,
  focus, and error states.
- **Decorative stroke** — a non-semantic border used for compositional
  effect only; must never be confusable with any of the semantic roles
  above.

### 2.3 Border hierarchy and contrast behavior

- Border weight and contrast increase from "subtle separator" through
  "strong separator" to "focus outline," so the most functionally
  important borders are also the most visually prominent.
- A border's contrast against its adjacent surface must be verified using
  the same contrast approach as text (see
  [color.md §4](color.md#4-contrast-evidence-illustrative-not-a-theme-mapping)),
  particularly for focus outlines, which must remain visible against
  every approved surface.

### 2.4 Theme considerations and responsive simplification

- Border presence and weight may simplify (e.g., fewer visible dividers)
  at smaller breakpoints where visual noise is more costly, provided
  content grouping remains clear through spacing alone.
- Final theme-specific border colors are KBDL-004's responsibility.

## 3. Elevation and Depth

This section defines KBDL's depth architecture: required principles, a
recommended semantic elevation scale, and profile-level and fallback
behavior.

### 3.1 Required principles (Approved)

- **Depth must communicate relationship and priority** — a higher
  elevation always means "more temporarily focused" or "closer to the
  user's current task," never a decorative-only signal.
- **Decorative depth must not obscure content hierarchy.**
- **Glass-like (translucent) effects must be selective**, per
  [color.md §2.6](color.md#26-transparency-constraints) and the identity
  exclusion of glassmorphism as a default
  ([principles.md §1](../principles.md#1-identity-statement)).
- **Blur must not compensate for weak contrast** — if content is hard to
  read, the fix is contrast or spacing, never added blur behind it.
- **A surface must remain understandable when shadows or blur are
  unavailable** (e.g., in a reduced-effects or high-contrast mode) —
  elevation must also be legible through position, border, and spacing
  alone.
- **Mobile and lower-performance contexts must support simplified depth**
  — an elevation level must degrade to a simpler treatment (e.g., border
  only) without losing its meaning.
- **Theme mappings belong to KBDL-004** — this document defines the
  semantic elevation scale, not final shadow/blur values per theme.

### 3.2 Default semantic elevation scale

Status: `Approved` — approved by the project owner via the
[foundation decision packet](README.md#6-foundation-decision-packet); see
[KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Provenance: `User-provided`. Validation status: `Not verified` for final
shadow/blur values (deferred to KBDL-004); the five-level semantic
structure and its purposes are approved.

| Level | Name | Purpose |
| --- | --- | --- |
| 0 | Base plane | The page or screen's resting background; no shadow. |
| 1 | Raised surface | Cards, panels resting slightly above the base plane for grouping. |
| 2 | Floating surface | Dropdowns, popovers, tooltips — temporarily above surrounding content. |
| 3 | Modal surface | Dialogs and sheets that temporarily take primary focus, with a scrim beneath them. |
| 4 | Temporary overlay | Toasts, in-progress notifications — highest, most transient layer. |

- **Sticky elements** (see
  [spacing-layout.md § Layout and Grid Principles](spacing-layout.md#2-layout-and-grid-principles-approved-architecture))
  occupy Level 1 or 2 depending on whether they present persistent chrome
  (Level 1) or a temporarily expanded state (Level 2).
- **Decorative depth** (a background shape suggesting depth for visual
  interest) must render at or below Level 0's visual weight — it must
  never be confused with a functional elevation level.

### 3.3 Shadow intent and border-plus-shadow combinations

- Shadow (once values are defined in KBDL-004) expresses elevation
  *emphasis*; border expresses elevation *edge definition*. The two are
  complementary, not redundant: a surface may use a border alone, a
  shadow alone, or both, depending on the surface's role and the theme's
  needs, but every level must remain distinguishable by at least one of
  the two.

### 3.4 Translucency and background separation

- Where translucency is used to separate a floating or modal surface from
  its background (e.g., a scrim), it must meet the contrast constraints
  in [color.md §2.6](color.md#26-transparency-constraints) and must never
  be the sole differentiator of elevation — position and (border or
  shadow) must also be present.

### 3.5 Profile-level intensity

- **Showcase:** may use the fuller elevation range (Levels 0–4) with more
  visible shadow/translucency for compositional drama.
- **Precision:** favors Levels 0–2 with restrained shadow, relying more on
  border for separation, to reduce visual noise in dense data views.
- **Flow:** uses the middle of the range, favoring clarity of the current
  step's surface over dramatic depth.

### 3.6 Simplified-depth fallback

- On mobile or lower-performance contexts, or when a user's system
  requests reduced transparency/effects, every elevation level must have
  a simplified equivalent that relies on border and spacing rather than
  shadow or blur, so the hierarchy in §3.2 remains legible.

## 4. Conceptual Conformance Examples

**Conforming:** A modal (Level 3) uses a solid scrim, a `corner-pronounced`
container, and a visible focus outline on its first interactive element —
depth, shape, and border roles are all consistent with their defined
purposes.

**Non-conforming:** A card grid gives every card a different corner radius
"for visual interest," and a decorative background blur is used to hide
that the underlying text has insufficient contrast — violates the
"corner variation must be systematic" and "blur must not compensate for
weak contrast" principles simultaneously.

## 5. Unresolved Shape/Depth Decisions

- Exact corner radius values per named step — `Unresolved`, deferred to
  the [foundation decision packet](README.md#6-foundation-decision-packet)
  and ultimately to implementation.
- Exact shadow/blur values per elevation level, per theme — `Unresolved`,
  deferred to KBDL-004.
- Exact border weight values — `Unresolved`, deferred pending an
  implementation-unit convention (see
  [spacing-layout.md § Unresolved Spacing/Layout Decisions](spacing-layout.md#7-unresolved-spacinglayout-decisions)).
