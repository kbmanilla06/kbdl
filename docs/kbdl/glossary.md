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

- **Adaptive theme** — A KBDL theme that changes its presentation in response
  to the user's light or dark preference while preserving the same underlying
  design language. Tracked under module code `THM`.

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

- **Foundation** — The base layer of KBDL (visual foundations such as color,
  type, and spacing primitives) that all themes, components, and profiles are
  built on. Tracked under module code `FND`. See
  [foundations/README.md](foundations/README.md).

- **KBDL** — The name of this reusable web design language, combining digital
  luxury, technical utility, controlled expressive motion, cross-project
  visual consistency, responsive and mobile-friendly behavior, adaptive
  light/dark presentation, and WCAG 2.2 Level AA accessibility with enhanced
  reduced-motion safeguards.

- **Locked rule** — A KBDL rule (most often an accessibility or motion-safety
  rule) that cannot be modified by a project profile or customization without
  an approved exception.

- **Motion pattern** — A named, reusable way that an interface element moves
  or transitions, described independent of exact timing values. Tracked under
  module code `MOT`.

- **Motion tier** — A defined level of motion intensity or purpose (for
  example functional versus expressive motion) that KBDL motion patterns are
  organized into.

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

- **Reduced motion** — The accessibility-driven behavior KBDL uses to safely
  reduce or remove non-essential motion for users who request it, exceeding
  baseline WCAG motion requirements.

- **Requirement traceability** — The documented connection between a
  requirement, its origin (blueprint or roadmap), its specification location,
  its status, and its validation evidence, maintained in the
  [traceability matrix](traceability-matrix.md).

- **Semantic token** — A design token that assigns meaning (for example
  "surface-background" or "danger-text") by referencing primitive tokens,
  forming the layer components consume.

- **Showcase Profile** — The KBDL project profile intended for portfolios and
  creative showcases.

- **Theme** — A defined visual mode of KBDL (see also Adaptive theme).
  Tracked under module code `THM`.

- **Validation criterion** — A documented, checkable condition used to
  determine whether a requirement is `Verified`. Tracked under module code
  `VAL`.
