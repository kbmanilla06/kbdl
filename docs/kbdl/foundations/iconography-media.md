# KBDL Foundations — Iconography and Media

Lifecycle status of this document's **architecture and rules**: `Approved`,
derived from [principles.md](../principles.md). Lifecycle status of the
**recommended icon and media strategy**: `Recommended` — requires
project-owner approval; see
[foundations/README.md § Foundation Status Model](README.md#3-foundation-status-model).

Return to the [foundations index](README.md) · [specification index](../README.md).

This document defines KBDL's iconography and imagery/media guidance. It
does not select a required icon library and does not define detailed
file-handling implementation.

---

## 1. Iconography

This section defines KBDL's icon architecture: required principles, role
categories, optical treatment, state behavior, and a recommended default
strategy.

### 1.1 Required principles (Approved)

- **Functional icons must be understandable.** An icon used for a
  functional action must be recognizable or paired with a label; novelty
  icons are not acceptable for critical actions.
- **Ambiguous icons require labels or supporting text.** If user testing
  or reasonable judgment suggests an icon's meaning is not immediately
  clear, a label is required, not optional.
- **Icons must not be the only state indicator**, consistent with the
  locked component-state-clarity rule
  ([principles.md §5.1](../principles.md#51-locked-identity-rules)) and
  [color.md](color.md)'s "color must not be the only carrier of meaning."
- **Multiple unrelated icon families must not be mixed.** A project uses
  one consistent icon style throughout; mixing filled, outlined, and
  hand-drawn styles in the same interface breaks visual consistency
  ([principles.md §7](../principles.md#7-visual-consistency)).
- **Decorative icons must not resemble interactive controls.** A purely
  decorative icon must be visually distinguishable from a functional,
  clickable icon (e.g., through placement, size, or absence of an
  interactive affordance).
- **Stroke and fill styles must have defined usage**, not mixed
  arbitrarily within one interface (see §1.3).
- **Accessibility names belong to application implementation but must be
  anticipated** — every functional icon must have a planned accessible
  name (e.g., an ARIA label) even though assigning the actual markup is
  an implementation-level task outside this specification's scope.

### 1.2 Icon purpose and style consistency (Approved architecture)

- **Functional icons** — represent an action or navigate; always paired
  with a label or an anticipated accessible name.
- **Status icons** — reinforce a status role from
  [color.md §2.4](color.md#24-status-roles); always paired with a status
  color and, where space allows, a text label.
- **Decorative icons** — support visual interest only; never carry
  meaning required to complete a task.

### 1.3 Optical sizing, stroke/fill relationships, corner treatment, alignment, bounding boxes, visual weight

- Icons are drawn at a small number of defined optical sizes (e.g., a
  compact size for inline label pairing, a standard size for controls, a
  larger size for empty-state or feature illustration use) rather than
  arbitrary per-instance sizing.
- A single **stroke-based** or **filled** treatment is chosen as KBDL's
  default functional-icon style (recommended in §1.6); the two are not
  mixed within the same functional context, though a filled variant of
  the same icon may be used specifically to indicate a "selected" or
  "active" state of an otherwise stroke-based icon.
- Icon corner treatment (e.g., rounded stroke caps) should echo the
  shape system's recommended geometric character once approved (see
  [shape-depth.md §1.2](shape-depth.md#12-geometric-character-recommended)),
  not introduce an unrelated geometric language.
- Icons align to the same optical center as their paired text, and share
  a consistent bounding-box convention so mixed icon sets from a single
  family render at visually equal weight.
- Visual weight (stroke thickness relative to size) stays consistent
  across the icon set so no single icon appears heavier or lighter than
  its neighbors at the same optical size.

### 1.4 State treatment and status communication

- An icon's state (default, hover, active, disabled) follows the same
  interactive-role model as other controls
  ([color.md §2.2](color.md#22-semantic-surface-and-text-roles)), never
  inventing a separate icon-only state model.
- Status communication via icon always pairs with the status color and,
  where reasonably possible, a text label — see §1.1.

### 1.5 Label pairing, profile-level use, project-owned iconography, custom icon review

- **Label pairing:** functional icons in Precision and Flow should default
  to icon-plus-label for anything beyond extremely common, universally
  understood actions; Showcase may use icon-only treatments more freely
  in editorial contexts where meaning is reinforced by surrounding
  content.
- **Project-owned iconography:** a project may introduce custom icons for
  brand-specific concepts (open brand expression, per
  [principles.md §5.3](../principles.md#53-open-brand-expression)),
  provided they are reviewed against §1.1–§1.4 before adoption.
- **Custom icon review** checks: style consistency with the chosen family
  (§1.2), optical sizing conformance (§1.3), and that the icon is not
  required as the sole carrier of critical meaning.

### 1.6 Recommended icon strategy

Status: `Recommended`, `Assumed` provenance, `Not verified` validation.

A stroke-based, geometrically consistent icon style, at a small set of
defined optical sizes, is recommended as KBDL's default functional-icon
treatment, since stroke icons pair well with the recommended (not yet
approved) "softened-structured" geometric character candidate (see
[shape-depth.md §1.2](shape-depth.md#12-geometric-character-recommended))
and remain legible at small interface sizes. No specific icon library is
selected here; library selection (open-source vs. custom-drawn vs.
licensed) is deferred to the
[foundation decision packet](README.md#6-foundation-decision-packet).

## 2. Imagery and Media

This section defines KBDL's imagery and media architecture: required
principles, media categories, aspect handling, overlays, performance, and
accessibility expectations.

### 2.1 Required principles (Approved)

- **Media must support content rather than merely fill space.** An image
  or video's presence must be justified by what it communicates, not used
  as decorative filler.
- **Text placed over media must remain readable**, verified against the
  same contrast expectations as any other text-on-surface pairing (see
  [color.md §2.6](color.md#26-transparency-constraints) for the
  translucency-over-content case).
- **Autoplay and animated media must anticipate reduced-motion
  requirements.** Any autoplaying video or animated image must have a
  static or paused equivalent for users who have requested reduced
  motion; exact reduced-motion substitution behavior is defined in
  KBDL-005 (Motion), but the *anticipation* of this requirement is
  established here.
- **Cropping must not remove essential information** — a crop must
  preserve the image's communicative focal point (see §2.3).
- **Portfolio media may be dominant but must not obstruct navigation**
  (Showcase).
- **Dashboard media must remain secondary to task information**
  (Precision) — imagery supports context, never competes with data for
  primary attention.
- **Consumer media must support comprehension and trust** (Flow) — e.g.,
  product imagery that accurately represents what a user will receive.
- **Large media must have lower-cost fallbacks** — a lower-resolution or
  static placeholder must be available while a full-resolution asset
  loads, so perceived performance is protected.

### 2.2 Media categories (Approved architecture)

- **Photography** — realistic imagery for brand, product, or editorial
  use.
- **Illustration** — stylized graphics for concepts, empty states, or
  onboarding.
- **Product imagery** — imagery depicting the actual product or service.
- **Portfolio media** — project or work-sample imagery (Showcase-
  specific emphasis).
- **Dashboard imagery** — supporting imagery within Precision contexts
  (e.g., a small avatar or thumbnail), always secondary to data.
- **Consumer-app media** — imagery supporting trust and comprehension in
  Flow contexts (e.g., product photos, confirmation illustrations).
- **Video / motion media** — any moving-image content; see §2.1's
  reduced-motion anticipation requirement.

### 2.3 Aspect Relationships, Cropping, and Focal-Point Preservation

- Media should be defined with a small set of named aspect treatments
  (e.g., a wide editorial aspect, a standard content aspect, and a square
  aspect for avatars/thumbnails) rather than arbitrary per-instance
  cropping, consistent with the "systematic, not arbitrary" principle
  applied elsewhere in these foundations (e.g.,
  [shape-depth.md §1.1](shape-depth.md#11-required-principles-approved)).
- Any crop must preserve the subject's focal point; where a fixed aspect
  would cut off essential content, the underlying asset or aspect choice
  should change rather than accepting a crop that loses meaning.
- At different breakpoints (see
  [spacing-layout.md §3.4](spacing-layout.md#34-how-columns-collapse-navigation-adapts-density-changes-media-behaves)),
  media reflows its aspect to preserve its focal point rather than being
  uniformly scaled.

### 2.4 Overlays, Captions, Decorative Backgrounds

- **Overlays** (a scrim or gradient over media to support text
  legibility) must be verified for contrast per §2.1 and
  [color.md §2.6](color.md#26-transparency-constraints).
- **Captions** use the Captions text role from
  [typography.md §3.9](typography.md#39-captions) and must remain legible
  against their background independent of the image beneath them (e.g.,
  via a caption-specific background treatment where needed).
- **Decorative backgrounds** built from imagery must respect the same
  "must not obscure content hierarchy" rule as decorative depth (see
  [shape-depth.md §3.1](shape-depth.md#31-required-principles-approved)).

### 2.5 Loading Behavior and Performance Considerations

- Media loading must provide a low-cost placeholder (e.g., a neutral
  fill using a role from [color.md](color.md), or a blurred low-resolution
  preview) so layout does not shift once the asset loads.
- Performance-aware enhancement
  ([principles.md §6.9](../principles.md#69-performance-aware-enhancement))
  applies directly here: high-resolution or autoplaying media must be
  weighed against its cost on constrained devices or networks.

### 2.6 Accessibility Expectations

- Every meaningful image must have a planned accessible text alternative
  (e.g., alt text), anticipated here even though assigning the actual
  markup is an implementation-level task.
- Purely decorative images must be anticipated as excluded from assistive-
  technology narration (e.g., treated as decorative/presentational),
  so they do not add noise for screen-reader users.
- Video content must anticipate the eventual need for captions or a text
  alternative once video is actually implemented.

### 2.7 Project-Brand Ownership

Photography, illustration style, and campaign-specific imagery are open
brand expression (see
[principles.md §5.3](../principles.md#53-open-brand-expression)) and
remain project-owned, provided they satisfy §2.1's required principles.

## 3. Conceptual Conformance Examples

**Conforming:** A Showcase project hero uses a large photograph with a
readable text overlay verified at the required contrast ratio, and the
photo's focal subject remains visible across all named aspect treatments
at every breakpoint.

**Non-conforming:** A Precision dashboard uses a large animated background
video behind its data tables "for atmosphere," competing with the data for
attention and offering no static fallback for reduced-motion users —
violates "dashboard media must remain secondary to task information" and
the reduced-motion anticipation principle simultaneously.

## 4. Unresolved Iconography/Media Decisions

- Specific icon library or custom-icon production approach —
  `Unresolved`, deferred to the
  [foundation decision packet](README.md#6-foundation-decision-packet).
- Exact named aspect-ratio values — `Unresolved`, deferred pending an
  implementation-unit convention.
- Video hosting/delivery approach — `Unresolved`, out of this
  specification's scope entirely (implementation concern).
