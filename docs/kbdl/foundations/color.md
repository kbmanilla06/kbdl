# KBDL Foundations — Color Architecture

Lifecycle status of this document's **architecture** (roles and rules):
`Approved`, derived from [principles.md](../principles.md). Lifecycle
status of the **recommended default values** in this document: `Recommended`
— they require project-owner approval before use; see
[foundations/README.md § Foundation Status Model](README.md#3-foundation-status-model).

Return to the [foundations index](README.md) · [specification index](../README.md).

This document defines KBDL's color **architecture**: the roles colors play
and the rules that govern them. It proposes illustrative recommended
default values with contrast evidence. It does **not** define complete
light-mode or dark-mode semantic mappings — that is KBDL-004 (Adaptive
Themes, see [README.md § Document Hierarchy](../README.md#document-hierarchy)).

---

## 1. Architectural Principles (Approved)

These principles are directly derived from
[principles.md](../principles.md) and are `Approved`:

- **Semantic names must be independent of individual hue names.** A role
  like "critical" or "accent" must not be named after a specific color
  (e.g., "red-500"), because the underlying hue may change per theme or
  future revision without the role's meaning changing.
- **Color must not be the only carrier of meaning**, per
  [principles.md §11 non-conforming pattern 13](../principles.md#11-non-conforming-design-directions)
  and the locked component-state-clarity rule
  ([principles.md §5.1](../principles.md#51-locked-identity-rules)). Every
  meaningful color distinction must be paired with an icon, label, or
  pattern.
- **Accent colors must be used selectively.** The accent family signals
  brand and primary action; using it pervasively erodes its ability to
  draw attention, contradicting
  [principles.md §6.1 Clarity Before Spectacle](../principles.md#61-clarity-before-spectacle).
- **Decorative glow must not become the primary hierarchy mechanism.**
  Glow, when used, is a controlled variable applied sparingly — hierarchy
  must be legible without it, consistent with the identity exclusions in
  [principles.md §1](../principles.md#1-identity-statement).
- **Neutral surfaces must support content clarity.** Neutral tones exist to
  let content and accent colors read clearly, not to carry their own
  decorative interest.
- **Status colors must remain distinguishable from brand accents.** A
  status role (positive, caution, critical, informational) must never be
  confusable with the accent role, so users do not mistake system state for
  brand emphasis or vice versa.
- **Transparency must preserve text, icon, control, and focus contrast.**
  Any translucent surface must be verified against contrast requirements
  before use; this directly enforces
  [principles.md §2](../principles.md#2-digital-luxury)'s exclusion of
  low-contrast translucent surfaces and non-conforming pattern 2 (unrestricted
  glassmorphism).
- **Gradients must support hierarchy or identity, not mask weak
  composition.** A gradient is a controlled variable, not a substitute for
  correct spacing, hierarchy, or contrast.
- **Theme-specific mappings belong to KBDL-004.** This document defines
  roles and illustrative values; it does not assign final light-mode or
  dark-mode pairings.

## 2. Color Role Architecture (Approved)

The following roles are `Approved` as an architecture; the values assigned
to them below are `Recommended`.

### 2.1 Primitive color families

- **Neutral family** — an ordered scale from lightest to darkest, used for
  surfaces, borders, and default text.
- **Accent family** — one primary technological accent used for brand
  identity and primary actions.
- **Supporting families** — informational, positive, caution, and critical,
  used exclusively for status roles (see §2.4).

### 2.2 Semantic surface and text roles

- **Surface roles** — base plane, raised surface, floating surface, modal
  surface (see [shape-depth.md](shape-depth.md) for the elevation model
  these surfaces participate in).
- **Text roles** — primary text, secondary text, tertiary/disabled text,
  inverse text (for use on filled or dark accent surfaces).
- **Border roles** — structural border, subtle separator, strong separator,
  focus outline, selected-state outline (see
  [shape-depth.md § Borders and Dividers](shape-depth.md#2-borders-and-dividers)).
- **Interactive roles** — default, hover, active/pressed, focus, disabled —
  applied consistently across all interactive elements regardless of
  component.

### 2.3 Data-display considerations

- Data visualizations (charts, graphs) require a distinct, color-blind-safe
  categorical set, separate from the status family, so a data series is
  never mistaken for a status signal.
- Sequential and diverging data scales must be perceptually even (equal
  perceived steps), not just evenly spaced in a single channel like hue.
- Data color must never be the sole differentiator between series; shape,
  pattern, or direct labeling must be available as a fallback.

### 2.4 Status roles

- **Informational** — neutral system feedback that is not urgent.
- **Positive** — success, completion, confirmation.
- **Caution** — a warning that does not block the user but requires
  attention.
- **Critical** — an error or blocking condition.

Status roles are semantically fixed; which specific hue expresses each
role may vary by theme (KBDL-004) but the four-role structure itself is
`Approved` and locked.

### 2.5 Gradient use

Gradients are a **controlled variable** (see
[principles.md §5.2](../principles.md#52-controlled-visual-variables)).
When used, a gradient must:

- Reinforce an existing hierarchy relationship (e.g., a hero surface),
  never invent one.
- Preserve the contrast of any text or icon placed over it at every point
  along the gradient, not just at its lightest or darkest stop.
- Be removable without breaking comprehension, per
  [principles.md §4](../principles.md#4-relationship-between-luxury-and-utility).

### 2.6 Transparency constraints

Translucent surfaces are permitted only where:

- Contrast for text, icons, controls, and focus indicators is verified
  against the *worst-case* content that could appear behind the surface,
  not just an assumed neutral background.
- A solid fallback exists for accessibility settings that reduce
  transparency (matching the operating system's "reduce transparency"
  preference where available).

### 2.7 Profile-level emphasis (color)

- **Showcase** — may use the accent and gradient families more visibly, and
  may allow richer, more saturated status/data color in editorial
  contexts, provided contrast and color-blind-safe differentiation are
  preserved.
- **Precision** — favors neutral-dominant surfaces with restrained accent
  use, reserving stronger color for state and status roles that carry
  functional meaning.
- **Flow** — uses a balanced accent presence focused on the primary action
  and progress feedback, avoiding competing accent applications on one
  screen.

All three profiles share the same role architecture; only the *frequency
and intensity* of use varies (see
[principles.md §9.4](../principles.md#94-shared-constraints-across-profiles)).

### 2.8 Project customization boundaries

- A project **may** substitute its own accent hue within the accent role,
  provided the replacement meets the same contrast and distinguishability
  requirements as the recommended default.
- A project **must not** repurpose a status role's hue as its brand accent,
  or vice versa, since this breaks the "status colors must remain
  distinguishable from brand accents" principle.
- A project **must not** introduce additional primitive families beyond
  neutral, accent, and the four status families without an approved
  exception (see
  [governance.md § Exception process](../governance.md#exception-process)).

## 3. Recommended Default Foundation

Status: `Recommended` — requires project-owner approval per
[foundations/README.md § Foundation Decision Packet](README.md#6-foundation-decision-packet).
Provenance: `Assumed` (a working starting point, not yet reviewed against
a specific project). Validation status: `Verified` for the contrast
calculations shown in §4 only; `Not verified` for suitability as a final
brand palette.

### 3.1 Core neutral architecture

A cool-neutral scale (slight blue undertone, supporting KBDL's
"technological" quality without tipping into a colder, sterile register):

| Step | Hex | Intended use (illustrative) |
| --- | --- | --- |
| neutral-0 | `#FFFFFF` | Lightest surface reference |
| neutral-10 | `#F5F6F8` | Raised surface on light backgrounds |
| neutral-20 | `#E8EAEE` | Subtle separators, disabled fills |
| neutral-30 | `#D3D6DC` | Structural borders on light surfaces |
| neutral-50 | `#8A8F99` | **Not for ordinary interface or body text at any size.** Reserved for large text meeting the WCAG 1.4.3 large-text size/weight threshold, non-text UI boundaries and graphics meeting WCAG 1.4.11 (3:1), or purely decorative use carrying no required meaning (see §4). |
| neutral-60 | `#636872` | Secondary/tertiary text at normal reading size — verified 4.5:1+ on neutral-0 (see §4). This is the correct value for ordinary secondary or tertiary body/interface text. |
| neutral-70 | `#52565F` | Structural borders on dark surfaces |
| neutral-90 | `#23252B` | Primary text on light surfaces |
| neutral-100 | `#121317` | Darkest surface reference |

### 3.2 Primary technological accent family

| Step | Hex | Intended use (illustrative) |
| --- | --- | --- |
| accent-30 | `#A9ACFF` | Accent text/icon on dark surfaces |
| accent-50 | `#4A4EE0` | Accent text/icon/fill on light surfaces, primary action |

### 3.3 Supporting status families

| Role | Hex | Intended use (illustrative) |
| --- | --- | --- |
| informational-text | `#2F6FED` | Informational text/icon on light surfaces |
| positive-text | `#146B3A` | Positive/success text/icon on light surfaces |
| caution-text | `#8A5A00` | Caution text/icon on light surfaces |
| critical-text | `#B3261E` | Critical/error text/icon on light surfaces |

### 3.4 Restrained gradient strategy

Recommended default: a single **accent-to-neutral** gradient (accent-50 to
accent-30) reserved for large, bounded Showcase-profile hero surfaces only
— never for body text backgrounds, form controls, or repeated Precision-
profile UI. This is a starting proposal, not an approved pattern.

### 3.5 Consistent value-expression method

Recommended: express all primitive values as 6-digit hex (`#RRGGBB`) in
specification documents, since hex is the most broadly portable
web-readable format. A perceptual reference (e.g., an OKLCH or CIELAB
equivalent) **should** be added once a color-tooling decision is made in a
later module; this document does not select that tooling.

## 4. Contrast Evidence (Illustrative, Not a Theme Mapping)

The pairs below are **isolated contrast checks** used to sanity-test the
recommended values above. They are not a complete light/dark theme mapping
and do not assign these pairs to specific components — that assignment is
KBDL-004's responsibility.

Contrast was calculated using the WCAG 2.x relative-luminance formula
(`L = 0.2126R + 0.7152G + 0.0722B` on linearized sRGB channels, contrast
ratio `(L1 + 0.05) / (L2 + 0.05)`), computed directly from the hex values
above using a local, dependency-free script; see the KBDL-003 validation
evidence for the exact script and per-pair output.

| Pair tested | Ratio | WCAG 2.2 AA normal-text threshold (4.5:1) | Result |
| --- | --- | --- | --- |
| neutral-90 text on neutral-0 surface | 15.32:1 | 4.5:1 | Passes with large margin |
| neutral-10 text on neutral-100 surface | 17.17:1 | 4.5:1 | Passes with large margin |
| accent-50 on neutral-0 | 6.07:1 | 4.5:1 | Passes |
| accent-30 on neutral-100 | 8.87:1 | 4.5:1 | Passes |
| informational-text on neutral-0 | 4.55:1 | 4.5:1 | Passes, narrow margin |
| positive-text on neutral-0 | 6.57:1 | 4.5:1 | Passes |
| caution-text on neutral-0 | 5.93:1 | 4.5:1 | Passes |
| critical-text on neutral-0 | 6.54:1 | 4.5:1 | Passes |
| neutral-50 on neutral-0 (large text / non-text UI boundary only) | 3.25:1 | 4.5:1 (normal text) / 3:1 (large text or UI components) | **Fails** the 4.5:1 normal-text threshold. `neutral-50` is therefore prohibited for ordinary body, interface, label, or any other normal-sized text — it is defined only for WCAG 1.4.3 large text, WCAG 1.4.11 non-text UI boundaries/graphics, or purely decorative use. |
| neutral-60 on neutral-0 (secondary/tertiary normal-sized text) | 5.59:1 | 4.5:1 | Passes with a margin of +1.09, comfortably above threshold. This is the value to use for secondary or tertiary text at normal reading size. |

**This is not a claim of complete WCAG conformance.** Only the specific
pairs above were tested, in isolation, against a plain background. Real
usage must be re-verified once actual surface, overlay, and translucency
combinations are defined in KBDL-004, and once component-level usage is
defined in later component modules.

## 5. Conceptual Conformance Examples

**Conforming:** A critical-text error message is paired with an error icon
and the word "Error," using critical-text at the recommended value —
satisfies both the color-is-not-the-only-carrier-of-meaning principle and
the contrast evidence above.

**Non-conforming:** A dashboard uses the accent hue for both the primary
call-to-action button and a "warning" banner. This violates "status colors
must remain distinguishable from brand accents" and risks users
misreading a warning as a promoted action.

## 6. Unresolved Color Decisions

- Whether KBDL adopts a wide-gamut/perceptual color space (e.g., OKLCH) for
  its authoring format, beyond the hex values shown here — `Unresolved`,
  deferred to a future module or an explicit tooling decision.
- Exact data-visualization categorical palette — `Unresolved`, deferred;
  only the requirement for color-blind-safe, non-status-colliding
  treatment is established here.
- Final accent hue — `Recommended` only; requires project-owner approval
  per the [foundation decision packet](README.md#6-foundation-decision-packet).
