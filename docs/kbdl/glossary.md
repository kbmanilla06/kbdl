# KBDL Glossary

Status: `Approved` terms defined below reflect the approved KBDL blueprint.
Where a concept has not yet been designed (for example exact token values),
the definition describes the concept only, not its future values.

Return to the [specification index](README.md).

Terms are listed alphabetically. Each definition is scoped to what the
approved blueprint has established; it does not imply that later design
decisions (visual values, motion timings, component designs) already exist.

- **Accessibility rule** — A requirement that governs how KBDL must behave for
  people using assistive technology, keyboard navigation, or with sensory or
  cognitive access needs, in order to meet WCAG 2.2 Level AA and KBDL's
  enhanced motion-safety requirements. Tracked under module code `A11Y`.

- **Accessible description** — Programmatically determinable supplementary
  text for a component, beyond its accessible name, that provides additional
  context (for example a form field's hint text). See
  [accessibility.md §8](accessibility.md#8-semantic-structure-and-relationships).

- **Accessible name** — The programmatically determinable name assistive
  technology uses to identify a component, which must include any visible
  label text used to identify it (per `KBDL-A11Y-028`). See
  [accessibility.md §32](accessibility.md#32-forms-labels-instructions-and-autocomplete).

- **Adaptive theme** — A KBDL theme that changes its presentation in response
  to the user's light or dark preference while preserving the same underlying
  design language. Tracked under module code `THM`. See
  [themes/README.md](themes/README.md).

- **Breakpoint** — A named viewport-width threshold at which layout,
  navigation, or interaction structure changes to serve content or
  interaction needs, never to match a specific device. KBDL's four named
  roles are `compact`, `standard`, `expanded`, and `wide`. Tracked under
  module code `RSP`. See [responsive.md §3, §6](responsive.md#3-responsive-terminology).

- **Cognitive-function test** — An authentication step requiring a user to
  remember, transcribe, or solve something (a password, a puzzle, a
  memorized code) — restricted by WCAG 2.2 unless an alternative method is
  also available. See [accessibility.md §36](accessibility.md#36-authentication-accessibility).

- **Component** — A reusable interface element defined by KBDL (for example an
  action, form, navigation, surface, overlay, feedback, or system-state
  element) that has documented anatomy, states, and accessibility behavior.
  Tracked under module code `CMP`.

- **Component anatomy** — The documented structural parts that make up a
  component (for example a button's label, icon slot, and container).

- **Component state** — A documented condition a component can be in (for
  example default, hover, focus, active, disabled, loading, or error).

- **Component token** — A design token scoped to a single component, built
  from semantic tokens, used only where a component's needs cannot be met by
  semantic tokens alone.

- **Conformance** — The condition of a project or component meeting all
  applicable KBDL requirements for the scope being assessed, where each
  requirement's lifecycle status is `Approved` and its validation status is
  `Verified`. Meeting only one of these two conditions is not conformance.

- **Controlled variable** — An aspect of KBDL's design that a project profile
  or implementer may adjust only within explicitly documented bounds, as
  opposed to an open brand expression or a locked rule.

- **Customization rule** — Documented guidance describing how and where manual
  customization of KBDL is permitted. Tracked under module code `CUS`.

- **Decision record** — A single entry in the [decision register](decision-register.md)
  capturing a governance-relevant decision, its rationale, and its status.

- **Design language** — The overall set of principles, foundations, themes,
  motion behavior, and component guidance that defines how KBDL looks, feels,
  and behaves across projects, independent of any single implementation.

- **Design system** — The implementation-facing counterpart to a design
  language: the concrete tokens, components, and tooling that realize a
  design language in a specific codebase or platform. KBDL is a design
  language; a project's design system is built by applying KBDL.

- **Exception** — An approved, documented, time-bound or scope-bound deviation
  from a locked rule or accessibility requirement, recorded in the
  [decision register](decision-register.md).

- **Flow Profile** — The KBDL project profile intended for consumer-facing web
  applications.

- **Focus order** — The sequence in which interactive elements receive
  keyboard focus, which must be logical and must not contradict visual
  presentation. See [accessibility.md §10](accessibility.md#10-reading-and-focus-order).

- **Foundation** — The base layer of KBDL (visual foundations such as color,
  type, and spacing primitives) that all themes, components, and profiles are
  built on. Tracked under module code `FND`. See
  [foundations/README.md](foundations/README.md).

- **Input modality** — A distinct means of providing input to an interface
  (touch, pointer, keyboard, gesture, voice), each of which must retain
  equivalent interaction meaning per KBDL's input-parity requirements. See
  [responsive.md §23](responsive.md#23-touch-pointer-keyboard-and-hybrid-input).

- **KBDL** — The name of this reusable web design language, combining digital
  luxury, technical utility, controlled expressive motion, cross-project
  visual consistency, responsive and mobile-friendly behavior, adaptive
  light/dark presentation, and WCAG 2.2 Level AA accessibility with enhanced
  reduced-motion safeguards.

- **Live region** — A programmatically identified region of content whose
  updates are announced to assistive technology without requiring the user's
  focus, used for status messages. See
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication).

- **Locked rule** — A KBDL rule (most often an accessibility or motion-safety
  rule) that cannot be modified by a project profile or customization without
  an approved exception.

- **Motion pattern** — A named, reusable way that an interface element moves
  or transitions, described independent of exact timing values. Tracked under
  module code `MOT`. See [motion/patterns.md § Motion Pattern Matrix](motion/patterns.md#12-motion-pattern-matrix).

- **Motion parity** — The property that full-motion, reduced-motion, and
  no-motion presentations of the same interaction communicate the same
  meaning and preserve the same functionality. See
  [motion/accessibility-performance.md §1](motion/accessibility-performance.md#1-reduced-motion-and-no-motion-parity).

- **Motion tier** — A defined level of motion intensity or purpose (for
  example functional versus expressive motion) that KBDL motion patterns are
  organized into. Realized as the five-level motion hierarchy (None,
  Functional, Supportive, Expressive, Exceptional) in
  [motion/foundations.md §3](motion/foundations.md#3-motion-hierarchy).

- **No motion** — The presentation state in which all non-essential and
  decorative motion is removed entirely, distinct from Reduced motion, which
  simplifies rather than fully removes motion. See
  [motion/README.md §2](motion/README.md#2-motion-terminology).

- **Non-conformance** — The condition of failing one or more applicable KBDL
  requirements for the scope being assessed — that is, a requirement whose
  lifecycle status is `Approved` is either not implemented as specified, or
  its validation status is not `Verified` where verification has been
  attempted and failed.

- **Open brand expression** — An aspect of KBDL explicitly left open for a
  project or profile to express its own brand identity, within the bounds set
  by foundations and locked rules.

- **Precision Profile** — The KBDL project profile intended for SaaS
  dashboards.

- **Primitive token** — The most basic form of a design value in KBDL (for
  example a raw color or spacing value) that semantic and component tokens are
  built from.

- **Project Profile** — A documented KBDL configuration that adjusts emphasis
  (not foundations) for a category of project. KBDL's initial profiles are
  Showcase, Precision, and Flow. Tracked under module code `PRO`.

- **Reading order** — The order content is intended to be consumed in, which
  must match source order unless an explicit, accessible mechanism
  establishes a different but equally understandable order. See
  [responsive.md §12](responsive.md#12-source-order-and-reading-order).

- **Reduced motion** — The accessibility-driven behavior KBDL uses to safely
  reduce or remove non-essential motion for users who request it, exceeding
  baseline WCAG motion requirements.

- **Reflow** — The process by which content rearranges to fit the available
  viewport without requiring two-dimensional scrolling for reading. Tracked
  under module code `RSP`. See [responsive.md §11](responsive.md#11-layout-reflow).

- **Requirement traceability** — The documented connection between a
  requirement, its origin (blueprint or roadmap), its specification location,
  its status, and its validation evidence, maintained in the
  [traceability matrix](traceability-matrix.md).

- **Safe area** — The region of a viewport guaranteed not to be obscured by a
  device's physical cutouts, rounded corners, or system UI overlays. See
  [responsive.md §19](responsive.md#19-safe-areas-and-viewport-edges).

- **Semantic token** — A design token that assigns meaning (for example
  "surface-background" or "danger-text") by referencing primitive tokens,
  forming the layer components consume.

- **Showcase Profile** — The KBDL project profile intended for portfolios and
  creative showcases.

- **Status message** — Programmatically determinable content communicating
  a state change (loading, progress, success, error) without requiring the
  user's focus or depending only on visual animation or color. See
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication).

- **Target size** — The minimum pointer-activatable area for a control; WCAG
  2.2 sets a 24-by-24 CSS-pixel minimum, with a KBDL-preferred enhanced
  size proposed separately. See
  [accessibility.md §25](accessibility.md#25-target-sizing-and-spacing).

- **Theme** — A complete mapping of every KBDL semantic color role to a
  specific foundation color, for one mode (light or dark). See also
  Adaptive theme. Tracked under module code `THM`. Full theme
  terminology (mode, semantic role, local contrast context, theme
  parity, and related terms) is defined in
  [themes/README.md §3](themes/README.md#3-theme-terminology).

- **Touch target** — A pointer target specifically sized and spaced for
  finger-based activation on a touchscreen; see Target size for the
  applicable minimum. See [responsive.md §23](responsive.md#23-touch-pointer-keyboard-and-hybrid-input).

- **Validation criterion** — A documented, checkable condition used to
  determine whether a requirement is `Verified`. Tracked under module code
  `VAL`.
