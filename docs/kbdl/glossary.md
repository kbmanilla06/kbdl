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

- **Accordion** — A surface component that pairs a KBDL-007 disclosure trigger with an expandable/collapsible panel, exposing its expanded state on the trigger. Tracked under module code `CMP`. See [components-system.md §9.4](components-system.md#94-accordion-surface).

- **Action** — A component whose activation performs an operation within the
  current context, as distinct from navigation (see Link). Realized as the
  Button, Icon Button, and Toggle Button components. Tracked under module
  code `CMP`. See [components-core.md §20](components-core.md#20-action-components).

- **Adaptive theme** — A KBDL theme that changes its presentation in response
  to the user's light or dark preference while preserving the same underlying
  design language. Tracked under module code `THM`. See
  [themes/README.md](themes/README.md).

- **Alert** — A feedback component reserved for important, time-sensitive messages using the `alert` role, distinct from Alert Dialog (which requires a response) and Status (routine updates). See [components-system.md §14.2](components-system.md#142-alert).

- **Alert Dialog** — A modal overlay reserved for urgent messages requiring an explicit user response, using the `alertdialog` role, distinct from an ordinary Dialog or Alert. See [components-system.md §11.7](components-system.md#117-alert-dialog).

- **Badge** — A feedback component conveying a count or status marker; meaningful badges require an accessible text equivalent, while purely decorative badges carry no required semantics. See [components-system.md §14.6](components-system.md#146-badge-or-count-indicator).

- **Banner** — A page- or section-level feedback component communicating a severity-scoped message, distinct from the site header/banner landmark. See [components-system.md §14.3](components-system.md#143-banner).

- **Breadcrumb** — A navigation component communicating hierarchical location
  via an ordered list of ancestor destinations, ending in the current,
  non-linked page. See [components-core.md §24.5](components-core.md#245-breadcrumb).

- **Breakpoint** — A named viewport-width threshold at which layout,
  navigation, or interaction structure changes to serve content or
  interaction needs, never to match a specific device. KBDL's four named
  roles are `compact`, `standard`, `expanded`, and `wide`. Tracked under
  module code `RSP`. See [responsive.md §3, §6](responsive.md#3-responsive-terminology).

- **Button** — An action component performing an immediate operation within
  the current context, using native button semantics. See
  [components-core.md §20.1](components-core.md#201-button).

- **Card** — A summary or preview surface with heading/content hierarchy, an optional media relationship, and optional actions, distinct from Panel and Container Surface. See [components-system.md §9.3](components-system.md#93-card).

- **Carousel** — A complex-presentation component cycling through a collection of slides via previous/next and picker controls; automatic rotation, where used, must satisfy the WCAG 2.2 pause/stop/hide requirement. See [components-system.md §18.3](components-system.md#183-carousel).

- **Cognitive-function test** — An authentication step requiring a user to
  remember, transcribe, or solve something (a password, a puzzle, a
  memorized code) — restricted by WCAG 2.2 unless an alternative method is
  also available. See [accessibility.md §36](accessibility.md#36-authentication-accessibility).

- **Combobox** — A custom widget combining a text input with a popup list of
  options, documented only where native select behavior is insufficient. See
  [components-core.md §22.6](components-core.md#226-combobox-boundary).

- **Component** — A reusable interface element defined by KBDL (for example an
  action, form, navigation, surface, overlay, feedback, or system-state
  element) that has documented anatomy, states, and accessibility behavior.
  Tracked under module code `CMP`. See
  [components-core.md](components-core.md) for the core action, form, and
  navigation components.

- **Component anatomy** — The documented structural parts that make up a
  component (for example a button's label, icon slot, and container). See
  [components-core.md §7](components-core.md#7-component-anatomy-model).

- **Component state** — A documented condition a component can be in (for
  example default, hover, focus, active, disabled, loading, or error). See
  [components-core.md §8](components-core.md#8-component-state-model).

- **Component token** — A design token scoped to a single component, built
  from semantic tokens, used only where a component's needs cannot be met by
  semantic tokens alone.

- **Conformance** — The condition of a project or component meeting all
  applicable KBDL requirements for the scope being assessed, where each
  requirement's lifecycle status is `Approved` and its validation status is
  `Verified`. Meeting only one of these two conditions is not conformance.

- **Container Surface** — A neutral grouping surface with no semantics by default, distinct from Panel (which may carry section-level identity) and Card (which carries summary/preview purpose). See [components-system.md §9.1](components-system.md#91-container-surface).

- **Controlled variable** — An aspect of KBDL's design that a project profile
  or implementer may adjust only within explicitly documented bounds, as
  opposed to an open brand expression or a locked rule.

- **Current** — A component state indicating location within a set (for
  example the active page in navigation), distinct from Selected (a user
  choice) and Pressed (a toggled binary state). See
  [components-core.md §8](components-core.md#8-component-state-model).

- **Customization rule** — Documented guidance describing how and where manual
  customization of KBDL is permitted. Tracked under module code `CUS`.

- **Manual customization** — A human-chosen, documented project choice within
  Approved KBDL bounds, or a governed request beyond them; it is never an
  automated or silent mutation. See [customization.md §4](customization.md#4-customization-terminology).

- **Customization request** — The intake description of a desired project
  outcome before authority and implementation eligibility are established.

- **Customization record** — The auditable project record of a customization's
  classification, source authority, scope, impacts, evidence, history, and rollback.

- **Approved option selection** — Selection of an explicitly permitted option
  within its owning requirement's Approved bounds; selection does not change
  KBDL lifecycle status.

- **Project-local customization** — A bounded customization intended for one
  project only.

- **Reusable customization** — A customization intended for multiple projects;
  it must be reviewed as a possible KBDL extension rather than copied silently.

- **Proposed KBDL extension** — A proposed reusable role, meaning, variant,
  option, or policy that remains non-Approved until KBDL governance approves it.

- **Customization exception** — An Approved, recorded project deviation from a
  locked rule or Approved requirement under the governance exception process.

- **Stale customization** — A customization record requiring review because
  its source, Profile, scope, dependency, or authority changed.

- **Customization conformance** — The condition in which a customization is
  both authorized and validated against every applicable Approved requirement
  and its exact record scope.

- **Data Table** — A surface presenting tabular data using native `<table>`, caption, and header semantics; distinguished from Grid, which applies only where genuine interactive, cell-level operation is required. See [components-system.md §9.5](components-system.md#95-static-data-table).

- **Data Visualization** — A complex-presentation component conveying data graphically, requiring non-color-dependent encoding and a text or data-table alternative; its exact chart taxonomy and palette remain unapproved. See [components-system.md §18.4](components-system.md#184-data-visualization).

- **Decision record** — A single entry in the [decision register](decision-register.md)
  capturing a governance-relevant decision, its rationale, and its status.

- **Dialog** — An overlay with a programmatically associated accessible name and a keyboard-operable close mechanism; a Modal Dialog additionally requires focus containment and background inertness. See [components-system.md §11.5](components-system.md#115-dialog).

- **Disabled** — A component state that removes an element from interaction
  and from the tab order, distinct from Read-only (which preserves
  focusability). See [components-core.md §8](components-core.md#8-component-state-model).

- **Disclosure** — A trigger component that reveals or conceals associated
  content, exposing its expanded/collapsed state programmatically. See
  [components-core.md §20.6](components-core.md#206-disclosure-and-menu-triggers).

- **Design language** — The overall set of principles, foundations, themes,
  motion behavior, and component guidance that defines how KBDL looks, feels,
  and behaves across projects, independent of any single implementation.

- **Design system** — The implementation-facing counterpart to a design
  language: the concrete tokens, components, and tooling that realize a
  design language in a specific codebase or platform. KBDL is a design
  language; a project's design system is built by applying KBDL.

- **Drawer** — An edge-attached overlay surface, modal or non-modal depending on its adopted default, distinct from Dialog and Sheet; a drawer used for collapsed navigation preserves the KBDL-007 navigation-trigger contract and approves no exact collapse threshold. See [components-system.md §11.8](components-system.md#118-drawer-and-sheet).

- **Empty State** — A system state communicating a genuine absence of content, distinguished from No-Results State (which relates to a current query or filter). See [components-system.md §16.2](components-system.md#162-empty-state).

- **Error State** — A system state communicating a recoverable or blocking failure, requiring a stated recovery path where recoverable and never exposing internal diagnostic detail. See [components-system.md §16.4](components-system.md#164-error-state).

- **Exception** — An approved, documented, time-bound or scope-bound deviation
  from a locked rule or accessibility requirement, recorded in the
  [decision register](decision-register.md).

- **Field** — A labeled input or control within a form, together with its
  supporting label, description, instructions, and validation message.
  Tracked under module code `CMP`. See
  [components-core.md §21](components-core.md#21-form-architecture).

- **Field group** — A set of related fields sharing a group label and,
  where applicable, a group-level error. See
  [components-core.md §22.11](components-core.md#2211-field-group).

- **Flow Profile** — The KBDL project profile intended for consumer-facing web
  applications. See [profiles.md §12](profiles.md#12-flow-profile).

- **Focus order** — The sequence in which interactive elements receive
  keyboard focus, which must be logical and must not contradict visual
  presentation. See [accessibility.md §10](accessibility.md#10-reading-and-focus-order).

- **Foundation** — The base layer of KBDL (visual foundations such as color,
  type, and spacing primitives) that all themes, components, and profiles are
  built on. Tracked under module code `FND`. See
  [foundations/README.md](foundations/README.md).

- **Grid** — An interactive complex-presentation component applying a composite-widget keyboard model (roving tabindex, arrow-key cell navigation), used only where genuinely justified over a static Data Table. See [components-system.md §18.1](components-system.md#181-interactive-grid).

- **Hybrid profile** — A project configuration blending emphasis from more than one Project Profile without a documented single primary. Whether KBDL permits hybrid profiles, and any required precedence rule, is `Recommended`, not yet approved. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Inert** — The state of content that cannot receive focus or be reached by sequential or assistive-technology navigation, required for background content while a modal overlay is open. See [components-system.md §6](components-system.md#6-system-component-terminology).

- **Input modality** — A distinct means of providing input to an interface
  (touch, pointer, keyboard, gesture, voice), each of which must retain
  equivalent interaction meaning per KBDL's input-parity requirements. See
  [responsive.md §23](responsive.md#23-touch-pointer-keyboard-and-hybrid-input).

- **Invalid** — A component state indicating a field or value fails
  validation, distinct from a system-level error; must be paired with a
  non-color cue. See [components-core.md §8](components-core.md#8-component-state-model).

- **KBDL** — The name of this reusable web design language, combining digital
  luxury, technical utility, controlled expressive motion, cross-project
  visual consistency, responsive and mobile-friendly behavior, adaptive
  light/dark presentation, and WCAG 2.2 Level AA accessibility with enhanced
  reduced-motion safeguards.

- **Listbox** — A popup surface exposing `listbox`/`option` roles that maintains a KBDL-007 combobox's active-descendant relationship; using a listbox popup does not itself approve the KBDL-007 custom-combobox-justification recommendation. See [components-system.md §11.4](components-system.md#114-listbox-popup).

- **Live region** — A programmatically identified region of content whose
  updates are announced to assistive technology without requiring the user's
  focus, used for status messages. See
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication).

- **Locked rule** — A KBDL rule (most often an accessibility or motion-safety
  rule) that cannot be modified by a project profile or customization without
  an approved exception.

- **Log** — A live-region role for an ordered stream of updates, distinct from Status (a single advisory update) and Alert (an urgent, assertive message). See [components-system.md §14.5](components-system.md#145-status-region-and-log).

- **Menu** — An overlay surface exposing `menu`/`menuitem` roles that maintains a KBDL-007 menu-button trigger's `aria-expanded`/`aria-controls` relationship, used only for genuine command or choice behavior. See [components-system.md §11.3](components-system.md#113-menu-surface).

- **Meter** — A feedback component exposing a current value within a known range (with minimum/maximum), distinct from Progress Indicator, which communicates operation completion. See [components-system.md §14.8](components-system.md#148-meter).

- **Modal** — An overlay that requires user response before other content can be operated; background content is rendered inert. See [components-system.md §6](components-system.md#6-system-component-terminology).

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

- **No-Results State** — A system state communicating that a current query or filter produced no matches, distinguished from Empty State by preserving the user's entered criteria. See [components-system.md §16.3](components-system.md#163-no-results-state).

- **Non-conformance** — The condition of failing one or more applicable KBDL
  requirements for the scope being assessed — that is, a requirement whose
  lifecycle status is `Approved` is either not implemented as specified, or
  its validation status is not `Verified` where verification has been
  attempted and failed.

- **Non-modal** — An overlay that coexists with an operable background, never trapping focus. See [components-system.md §6](components-system.md#6-system-component-terminology).

- **Offline State** — A system state communicating a confirmed or suspected loss of connectivity; it must not claim a saved, synchronized, or queued status before the relevant system confirms it. See [components-system.md §16.5](components-system.md#165-offline-and-reconnecting-state).

- **Open brand expression** — An aspect of KBDL explicitly left open for a
  project or profile to express its own brand identity, within the bounds set
  by foundations and locked rules.

- **Overlay** — A surface rendered above the normal document flow, anchored to a trigger or the viewport, that opens and closes; modal or non-modal. See [components-system.md §6](components-system.md#6-system-component-terminology).

- **Pagination** — A navigation component for moving between pages of a
  larger content set, marking the current page and providing
  previous/next actions. See [components-core.md §24.7](components-core.md#247-pagination).

- **Panel** — A section-level grouping surface with an optional heading and description, using `region` semantics only when its content is a significant, independently navigable section. See [components-system.md §9.2](components-system.md#92-panel).

- **Popover** — A non-modal overlay surface for supplemental interactive content, anchored to a trigger, distinct from Tooltip (non-interactive) and Menu (fixed command/choice content). See [components-system.md §11.2](components-system.md#112-popover-or-non-modal-dialog).

- **Precision Profile** — The KBDL project profile intended for SaaS
  dashboards. See [profiles.md §11](profiles.md#11-precision-profile).

- **Pressed** — A component state exposing a toggled binary condition (see
  Toggle button), distinct from Selected (set membership) and Current
  (location). See [components-core.md §8](components-core.md#8-component-state-model).

- **Primary profile** — The Project Profile a project treats as its dominant configuration. Whether every project must select exactly one is `Recommended`, not yet approved. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Primitive token** — The most basic form of a design value in KBDL (for
  example a raw color or spacing value) that semantic and component tokens are
  built from.

- **Profile conflict** — A case where Project Profile emphasis would require overriding a higher-priority concern in the design-decision hierarchy. See [profiles.md §24](profiles.md#24-profile-conflicts-and-exception-handling).

- **Profile conformance** — The condition of a project's use of KBDL meeting every locked rule and every requirement applicable to its declared Project Profile. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Profile declaration** — A project's documented record of its selected Project Profile, selection rationale, and applicable requirements. See [profiles.md §8](profiles.md#8-profile-selection-and-declaration).

- **Profile emphasis** — The permitted variation in frequency, intensity, or composition of an already-approved controlled variable, used to express a Project Profile's purpose without changing shared architecture or meaning. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Profile exception** — An approved, documented deviation from a locked or Approved rule for a specific project's Project Profile, recorded per the governance exception process. See [profiles.md §24](profiles.md#24-profile-conflicts-and-exception-handling).

- **Profile fit** — The qualitative match between a project's documented characteristics and a Project Profile's purpose; not a numeric score unless a future approval defines one. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Profile invariant** — A rule, value, or meaning that must hold identically across every Project Profile. See [profiles.md §9](profiles.md#9-cross-profile-invariants).

- **Progress Indicator** — A feedback component exposing determinate or indeterminate operation progress, distinct from Meter, which communicates a measurement within a known range. See [components-system.md §14.7](components-system.md#147-progress-indicator).

- **Project Profile** — A documented KBDL configuration that adjusts emphasis
  (not foundations) for a category of project. KBDL's initial profiles are
  Showcase, Precision, and Flow. Tracked under module code `PRO`. A profile
  is distinct from theme mode, brand identity, user role or persona, viewport
  class, device category, accessibility preference, product tier, and
  component variant. See [profiles.md §4–§5](profiles.md#4-project-profile-terminology).

- **Read-only** — A component state that preserves focusability and allows
  copying but not editing a control's value, distinct from Disabled. See
  [components-core.md §8](components-core.md#8-component-state-model).

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

- **Scrim** — A dimming layer behind a modal or floating surface, mapped to the approved Scrim/backdrop theme role; this specification does not assign an exact opacity value. See [components-system.md §6](components-system.md#6-system-component-terminology).

- **Secondary profile** — A Project Profile applied to a bounded portion of a project alongside its primary profile. Whether KBDL permits secondary profiles at all is `Recommended`, not yet approved. See [profiles.md §4](profiles.md#4-project-profile-terminology).

- **Selected** — A component state indicating a user's chosen membership in
  a set (for example a checked checkbox or a highlighted list item),
  distinct from Current (location) and Pressed (a toggled action). See
  [components-core.md §8](components-core.md#8-component-state-model).

- **Semantic token** — A design token that assigns meaning (for example
  "surface-background" or "danger-text") by referencing primitive tokens,
  forming the layer components consume.

- **Sheet** — An edge-attached overlay surface variant of Drawer; see Drawer for the shared taxonomy and boundary rules. See [components-system.md §11.8](components-system.md#118-drawer-and-sheet).

- **Showcase Profile** — The KBDL project profile intended for portfolios and
  creative showcases. See [profiles.md §10](profiles.md#10-showcase-profile).

- **Skeleton** — A decorative loading-placeholder surface hidden from assistive technology, requiring an equivalent loading announcement through a separate status mechanism. See [components-system.md §14.9](components-system.md#149-skeleton).

- **Skip link** — A navigation component providing first-focus bypass of
  repeated content blocks, directing focus to the main content landmark.
  See [components-core.md §24.1](components-core.md#241-skip-link).

- **Snackbar** — A transient feedback surface variant of Toast; see Toast for the shared lifecycle model. See [components-system.md §14.4](components-system.md#144-toast-or-snackbar).

- **Status** — A live-region role for an advisory update not requiring the user's focus, distinct from Alert (urgent, assertive) and Log (an ordered stream). See [components-system.md §14.5](components-system.md#145-status-region-and-log).

- **Status message** — Programmatically determinable content communicating
  a state change (loading, progress, success, error) without requiring the
  user's focus or depending only on visual animation or color. See
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication).

- **System Status** — A system state presenting an accessible, ongoing update stream about current system condition, distinct from a transient Alert or Toast. See [components-system.md §16.9](components-system.md#169-system-status).

- **Tab** — A control within a tablist that selects which associated tab
  panel is visible. See [components-core.md §24.6](components-core.md#246-tabs).

- **Tab panel** — The content region associated with and disclosed by a
  selected tab. See [components-core.md §24.6](components-core.md#246-tabs).

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

- **Toast** — A transient feedback surface for non-critical updates; critical information must never be presented only in a toast without an accessible, persistent path also being available. See [components-system.md §14.4](components-system.md#144-toast-or-snackbar).

- **Toggle button** — An action component exposing a persistent pressed/
  unpressed state tied to a stable action identity, distinct from a switch
  (an immediate setting) and a checkbox (a form-field selection). See
  [components-core.md §20.3](components-core.md#203-toggle-button).

- **Tooltip** — An informational, non-interactive overlay describing its trigger; it must never be the sole source of its trigger's accessible name. See [components-system.md §11.1](components-system.md#111-tooltip).

- **Touch target** — A pointer target specifically sized and spaced for
  finger-based activation on a touchscreen; see Target size for the
  applicable minimum. See [responsive.md §23](responsive.md#23-touch-pointer-keyboard-and-hybrid-input).

- **Tree** — A complex-presentation component exposing hierarchical parent/child relationships with expand/collapse and selection behavior, used only where genuinely justified. See [components-system.md §18.2](components-system.md#182-tree-and-treegrid).

- **Treegrid** — A complex-presentation component combining Tree's hierarchical relationships with Grid's tabular interaction, used only where both are genuinely required. See [components-system.md §18.2](components-system.md#182-tree-and-treegrid).

- **Accepted limitation** — A known validation limitation explicitly accepted
  by the authority required for completion; recording it does not convert
  missing evidence into conformance.

- **Candidate final status** — A KBDL-011 readiness recommendation made from
  the evidence available to the validation run. It is not project completion
  and does not bypass planning-agent review or project-owner approval.

- **Completion approval** — The project owner's explicit authorization to
  mark the KBDL roadmap complete after independent validation has passed and
  applicable limitations have been accepted.

- **Documentation validation** — Class A validation of document structure,
  links, tables, identifiers, metadata, and inventory using repository
  evidence.

- **Evidence sufficiency** — The rule that a validation conclusion may extend
  only as far as the executed method and retained evidence support.

- **Final validation** — The KBDL-011 audit of the complete specification
  repository. It assesses documentation readiness while keeping implementation
  and project evidence separate.

- **Implementation conformance** — Demonstrated agreement between a real
  implementation and applicable Approved KBDL requirements. It remains `Not
  verified` when no implementation evidence exists.

- **Implementation-dependent validation** — Class E validation requiring an
  executable implementation and runtime evidence, such as browser, device,
  assistive-technology, security, performance, or rollback results.

- **Production readiness** — A candidate release state indicating that the
  evaluated scope has no known blocking defect. In KBDL-011, any such state is
  explicitly scoped to documentation unless production evidence exists.

- **Project-specific validation** — Class F validation requiring evidence from
  an adopting project, such as configuration, customization, deployment, or
  production operation.

- **Specification release readiness** — The readiness of the KBDL documents
  for specification release, assessed separately from implementation
  conformance and production deployment.

- **Static consistency validation** — Class C validation of relationships and
  invariants that can be established by comparing specification text without
  executing an implementation.

- **Theme calculation validation** — Class D validation that reproduces a
  theme calculation from recorded source values and formula; it does not cover
  unknown alpha-composited or runtime contexts.

- **Validation class** — One of KBDL-011's evidence classes: documentation
  (A), governance (B), static consistency (C), calculation-based (D),
  implementation-dependent (E), or project-specific (F).

- **Validation criterion** — A documented, checkable condition used to
  determine whether a requirement is `Verified`. Tracked under module code
  `VAL`.

- **Validation defect** — A specific inconsistency, missing record, broken
  reference, unsupported claim, or failed check discovered during validation.
