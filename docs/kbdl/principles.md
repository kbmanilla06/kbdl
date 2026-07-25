# KBDL Principles

Lifecycle status: `Approved` (KBDL-002 deliverable). Validation status:
`Not verified` unless stated otherwise per requirement below. Provenance:
`User-provided` for blueprint-sourced statements, `Confirmed` where derived
directly from KBDL-001, `Assumed` where explicitly marked.

Return to the [specification index](README.md). Status labels are defined
in [conventions.md §1](conventions.md#1-status-labels); requirement IDs in
[conventions.md §2](conventions.md#2-requirement-identification).

This document defines KBDL's identity, design philosophy, core principles,
and cross-project visual-consistency rules. It does not define final
colors, typefaces, measurements, motion timings, or component
specifications — those belong to later roadmap modules (see the
[document hierarchy](README.md#document-hierarchy)) and must not be
introduced here.

---

## 1. Identity Statement

KBDL is a reusable web design language for building responsive,
mobile-friendly digital products that feel premium and considered while
remaining fast, clear, and usable by general consumers. It gives multiple,
otherwise unrelated projects a shared visual and behavioral identity, so
that a portfolio, a SaaS dashboard, and a consumer web application can all
be immediately recognizable as built from the same system, even though each
serves a different audience and task.

KBDL serves:

- **General consumers**, who need clarity, predictability, and
  accessibility more than novelty.
- **Design and engineering teams**, who need a shared, documented reference
  so decisions are consistent without requiring a new visual language per
  project.
- **Three initial project categories**: Showcase (portfolios and creative
  showcases), Precision (SaaS dashboards and information-dense
  applications), and Flow (consumer-facing web applications). See the
  [glossary](glossary.md) for the "Project Profile" definition.

The experience KBDL intends to create is one of **quiet confidence**: an
interface that presents information precisely, moves with intention rather
than decoration, and never makes the user work to find what matters. It is
technological in construction but never alienating in presentation.

What makes KBDL distinct from generic technology-branded design systems is
that it treats **restraint as a luxury signal** rather than treating visual
richness as the signal. Many technology-branded systems communicate
"advanced" through density, glow, or constant motion; KBDL communicates it
through precision, hierarchy, and material coherence, while still allowing
controlled expressive moments where a project's context calls for them.

KBDL refuses to become:

- **A cyberpunk theme.** KBDL does not adopt neon-on-black futurism as its
  identity. Motion and accent expression are controlled tools, not a
  default aesthetic layer.
- **A neon visual-effects collection.** Glow, gradients, and light effects
  are, at most, controlled variables applied sparingly — never the source
  of KBDL's identity.
- **A glassmorphism library.** Translucent, blurred surfaces are not a
  default KBDL surface treatment; any such treatment must be justified
  against contrast and legibility requirements defined in later modules.
- **A dashboard-only system.** KBDL must work equally for editorial,
  data-dense, and conversational contexts.
- **A portfolio-only system.** KBDL must work equally for repeated,
  efficiency-driven workflows.
- **An animation showcase.** Motion serves comprehension and feedback
  first; spectacle is never the primary justification for movement.
- **A specific front-end framework.** KBDL is a design language, not a code
  library, framework, or component kit — see the [glossary](glossary.md)
  entries for "Design language" versus "Design system."
- **A single brand identity.** KBDL defines shared foundations and
  behavior; each project retains its own brand expression within the
  [open brand expression](#5-stable-and-variable-identity-elements) category.

KBDL is, in short: **premium but functional, technological but
understandable, expressive but controlled, flexible but visually
consistent, modern without depending on short-lived visual trends, and
suitable for general consumers.**

---

## 2. Digital Luxury

**Digital Luxury** is the KBDL quality that makes an interface feel
considered, precise, and high-value without relying on decoration.

Digital Luxury is produced through:

- **Precision** — elements are positioned, sized, and aligned with evident
  intent, not approximate placement.
- **Deliberate hierarchy** — the most important content and actions are
  unmistakable; nothing competes with them by accident.
- **Restraint** — every visual addition (an effect, a flourish, an
  animation) must earn its place by supporting comprehension or brand
  feeling; if it does not, it is removed.
- **Material coherence** — surfaces, elevation, and depth behave according
  to one consistent internal logic, so the interface reads as a single
  considered material system rather than a collection of unrelated
  effects.
- **Typographic control** — type establishes rhythm and hierarchy
  deliberately; this principle governs *relationships*, not final
  typefaces or scales, which are defined in a later module.
- **Proportion** — relationships between elements (not their exact
  measurements) feel intentional and balanced.
- **Space** — space is used to create emphasis and separation, not left
  over by default or added without purpose.
- **High-quality transitions** — state changes and navigational transitions
  feel smooth and purposeful; this governs motion *character*, not
  duration or easing values, which belong to the motion module.
- **Clear content presentation** — content is presented so it can be
  scanned and understood quickly, never obscured for aesthetic effect.
- **Attention to states and details** — every interactive state (hover,
  focus, active, disabled, loading, error) is deliberately designed, not
  left as a browser default or omitted.

Digital Luxury does **not** mean:

- Excessive decoration.
- Constant glow.
- Heavy blur used everywhere as a default surface treatment.
- Unnecessary animation added for visual interest alone.
- Low-contrast translucent surfaces that compromise legibility.
- Large amounts of empty space used without a hierarchy or rhythm purpose.
- Small or inaccessible controls justified as "minimal" or "clean."
- Hiding functionality in the name of aesthetic purity.
- Expensive-looking effects that reduce performance or usability.

This definition governs *relationships and qualities*. It does not select
final colors, shadows, typography, or measurements — those are defined in
the visual foundations, themes, and motion modules once approved.

---

## 3. Technical Utility

**Technical Utility** is the KBDL quality that makes an interface reliably
usable, predictable, and efficient for the task at hand.

Technical Utility is expressed through:

- **Clear hierarchy** — the structure of information and controls is
  legible at a glance.
- **Predictable behavior** — the same kind of control behaves the same way
  everywhere in a KBDL project.
- **Strong alignment** — elements align to a consistent underlying
  structure, so the eye can track relationships without effort.
- **State visibility** — the current state of any component or process is
  always perceivable, not just implied.
- **Information organization** — related content and controls are grouped
  so the structure of a screen matches the structure of the task.
- **Efficient repeated interaction** — workflows a user performs
  frequently are optimized for speed and low friction over visual
  spectacle.
- **Responsive feedback** — the interface acknowledges input immediately,
  even before an operation completes.
- **Error prevention** — the interface is structured to reduce the chance
  of user error before it happens.
- **Recovery support** — when an error does occur, the interface makes the
  path to recovery clear.
- **Accessibility** — utility that excludes users is not utility; see
  [Section 4](#4-relationship-between-luxury-and-utility) for how
  accessibility is prioritized against every other quality.
- **Performance awareness** — visual and motion choices account for their
  cost to load time and responsiveness.

Technical Utility does **not** mean:

- Visual density without prioritization — cramming controls together is
  not efficiency.
- Developer-oriented terminology presented to general consumers.
- Terminal-inspired styling as a default aesthetic.
- Monospaced typography used everywhere by default.
- Exposing internal system complexity (implementation details, technical
  states, or raw data) to end users who do not need it.
- Removing visual character in the name of "function only" design.
- Overloading interfaces with controls "just in case" they are needed.
- Treating accessibility as an optional mode rather than a baseline
  requirement.

---

## 4. Relationship Between Luxury and Utility

Digital Luxury and Technical Utility are not opposing forces to balance
case by case — they are resolved through a fixed priority order that
applies whenever they appear to conflict:

1. **Correctness and safety** — the interface must not mislead, corrupt
   data, or cause unintended action.
2. **Accessibility** — WCAG 2.2 Level AA and KBDL's enhanced motion-safety
   requirements (see [decision-register.md § KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety)).
3. **Task completion and comprehension** — the user's ability to
   understand and complete their task.
4. **Clear hierarchy** — legible structure of content and controls.
5. **Responsive performance** — the interface responds quickly across
   device sizes and conditions.
6. **Visual consistency** — recognizable KBDL relationships (see
   [Section 7](#7-visual-consistency)).
7. **Expressive character** — Digital Luxury's precision, restraint, and
   material coherence.
8. **Decorative enhancement** — the least prioritized layer; anything
   purely ornamental.

The following statements govern how this order is applied:

- Luxury cannot justify inaccessible behavior. An effect that reduces
  contrast, hides focus, or excludes assistive technology is rejected
  regardless of how refined it looks.
- Expressiveness cannot delay frequent actions. A signature transition
  that adds latency to a task a user repeats often must be shortened,
  simplified, or removed for that context.
- Utility should not require visual sterility. Efficient, information-dense
  interfaces (particularly in the Precision Profile) must still carry
  KBDL's hierarchy, proportion, and material coherence — utility is not an
  excuse to abandon Digital Luxury.
- Visual simplification should preserve character. Reducing visual
  complexity for clarity or performance must preserve KBDL's hierarchy and
  proportion logic, not flatten the interface into a generic, unstyled
  state.
- Decorative effects must be removable without breaking hierarchy. If
  removing an ornamental effect (for accessibility, performance, or reduced
  motion) breaks a user's ability to understand the interface, the effect
  was carrying functional weight it should not have carried and must be
  redesigned.
- Repeated workflows should favor efficiency over spectacle. The more often
  a user performs an action, the less that action should depend on
  expressive or decorative flourishes.
- High-impact brand or showcase moments may use greater expression when
  core usability remains intact — for example, an editorial landing
  moment in the Showcase Profile may use stronger compositional gestures
  than a repeated dashboard action in the Precision Profile, provided
  accessibility and task comprehension are not compromised.

### Conflict Examples

**Example 1 — Translucency versus contrast.** A project wants a
translucent, layered surface treatment for a navigation panel because it
feels premium. If the translucency reduces text or icon contrast below
accessible levels, contrast wins: the surface must gain a solid backing,
increased opacity, or an alternative treatment before it may ship. Luxury
expression adapts to preserve legibility; legibility does not adapt to
preserve the effect.

**Example 2 — Animation versus task speed.** A signature entrance
animation plays every time a frequently used list is filtered. Because this
is a repeated, task-critical interaction, task completion speed outranks
the animation: the motion must be shortened, made conditional on first-view
only, or removed for this interaction, even if the same animation is
appropriate for a first-time onboarding moment.

**Example 3 — Large editorial typography versus dashboard density.** A
Showcase-style hero moment uses large, expressive typographic scale to
create impact; a Precision dashboard needs to show many data points in
limited space. Both are valid expressions of one system: the *relationship*
principles (proportion, hierarchy, rhythm) are the same in both places, but
their *application* differs by context and profile, which is expected and
does not create inconsistency. Neither profile is permitted to abandon
hierarchy or accessibility to achieve its density or impact goal.

**Example 4 — Brand expression versus component consistency.** A project
wants a custom interactive control that behaves differently from KBDL's
standard control anatomy, to strengthen its brand identity. Component
consistency outranks open brand expression: the project may restyle within
[controlled visual variables](#5-stable-and-variable-identity-elements),
but it may not introduce a control with different interaction meaning or
anatomy without an approved exception (see
[Section 8](#8-design-decision-hierarchy)).

**Example 5 — Visual minimalism versus discoverability.** A project wants
to hide secondary controls until hover, for a cleaner appearance. If this
removes discoverability for touch or keyboard users (who cannot "hover"),
accessibility and task comprehension outrank the minimalist goal: the
controls must remain discoverable through a KBDL-compliant mechanism
(for example, a persistent affordance) that does not depend on a
pointer-only interaction.

No conflict example above introduces a final token value; each resolution
is expressed as a relationship or priority outcome, to be made concrete by
later modules.

---

## 5. Stable and Variable Identity Elements

KBDL identity elements fall into exactly three categories.

### 5.1 Locked identity rules

These establish KBDL's recognizable identity and **cannot be changed
without an approved exception** (see
[governance.md § Exception process](governance.md#exception-process)):

- **Hierarchy logic** — the principle that the most important content and
  action are always the most visually and structurally prominent element.
- **Spacing relationships** — the principle that space follows a
  deliberate, repeated rhythm rather than ad hoc values (the specific
  rhythm scale is defined in the visual foundations module).
- **Component-state clarity** — every component state must be
  distinguishable without relying on color alone.
- **Motion purpose** — motion must always serve feedback, hierarchy, or
  continuity; it is never purely decorative filler.
- **Accessibility requirements** — WCAG 2.2 Level AA and KBDL's enhanced
  motion-safety requirements, as protected by
  [governance.md § KBDL-GOV-002](governance.md#kbdl-gov-002--accessibility-requirements-are-protected).
- **Responsive content priority** — the same content must retain the same
  relative priority across breakpoints; smaller viewports reorganize, they
  do not silently drop what matters.
- **Surface relationship logic** — the rule that depth and elevation
  communicate a consistent, single system of layering (the specific values
  belong to the visual foundations module).
- **Interaction predictability** — a given interaction pattern must mean
  the same thing everywhere in a KBDL project.

### 5.2 Controlled visual variables

These **may vary within limits that future modules will document.** This
prompt does not define the allowed ranges:

- Accent family
- Neutral temperature
- Typography personality
- Corner character
- Surface richness
- Border prominence
- Depth intensity
- Gradient intensity
- Motion amplitude
- Content density
- Image treatment

### 5.3 Open brand expression

These remain **project-owned**:

- Logo
- Photography
- Illustration
- Campaign graphics
- Content voice
- Brand motifs
- Marketing composition
- Project-specific media

Open brand expression must still respect accessibility, hierarchy, and
interaction requirements defined by KBDL's locked identity rules. A
project's logo, photography, or content voice never overrides a locked
rule or an approved KBDL requirement.

---

## 6. Core Principles

Eight core principles govern KBDL design decisions. Each is written as a
usable decision rule, not an aspiration.

### 6.1 Clarity Before Spectacle

- **Normative statement:** A design decision that increases visual impact
  at the expense of comprehension or task speed must not proceed without
  redesign.
- **Purpose:** Prevents expressive ambition from undermining the
  interface's core job of being understood and used.
- **Required behavior:** Evaluate every expressive addition against
  whether it helps or hinders the user's understanding of the current
  screen.
- **Prohibited behavior:** Adding visual flourish because it is
  technically possible or trend-aligned, without checking comprehension
  impact.
- **Showcase:** May use stronger compositional gestures, provided the
  primary message and action remain unmistakable.
- **Precision:** Spectacle is rare; clarity of data and state dominates.
- **Flow:** Spectacle is used sparingly, mainly to reinforce successful
  task completion.
- **Accessibility implications:** Spectacle must never obscure focus
  indicators, reading order, or assistive-technology semantics.
- **Responsive implications:** Spectacle that depends on large viewport
  space must degrade gracefully on small viewports without breaking
  clarity.
- **Motion implications:** Motion used for spectacle must yield to motion
  used for feedback when both compete for the user's attention.
- **Review questions:** Does this addition make the interface easier or
  harder to understand? Would removing it change what the user can
  accomplish?

### 6.2 Precision and Intentionality

- **Normative statement:** Every visual relationship (alignment, spacing,
  proportion) must be attributable to a deliberate rule, not an
  approximation.
- **Purpose:** Produces the "considered" feeling central to Digital
  Luxury.
- **Required behavior:** Justify placement, sizing, and spacing choices
  against KBDL's hierarchy and rhythm relationships.
- **Prohibited behavior:** "Eyeballing" layout decisions or accepting
  default framework spacing without evaluating it against KBDL rhythm.
- **Showcase:** Precision governs large compositional layouts as strictly
  as small ones.
- **Precision:** Precision is especially visible in dense data layouts,
  where misalignment is most noticeable.
- **Flow:** Precision supports a sense of trustworthiness in guided
  workflows.
- **Accessibility implications:** Precise alignment supports predictable
  reading and tab order.
- **Responsive implications:** Precision relationships must hold across
  breakpoints, not only at one reference size.
- **Motion implications:** Motion paths and transforms should respect the
  same alignment logic as static layout.
- **Review questions:** Can every position and gap be explained by a rule?
  Would a design reviewer be able to reproduce this relationship
  elsewhere?

### 6.3 Consumer Comprehension

- **Normative statement:** Interfaces must be understandable by general
  consumers without specialized or technical knowledge.
- **Purpose:** Keeps KBDL usable by its primary audience across all three
  profiles.
- **Required behavior:** Use plain language, familiar interaction
  patterns, and progressive disclosure for complexity.
- **Prohibited behavior:** Presenting internal system states, technical
  jargon, or developer-oriented terminology to end users.
- **Showcase:** Comprehension governs how creative content is framed, not
  just controls.
- **Precision:** Complex data must still be explained in consumer-legible
  terms, even for professional users.
- **Flow:** Comprehension is paramount; guided flows must never assume
  prior technical knowledge.
- **Accessibility implications:** Plain language is itself an accessibility
  requirement (cognitive accessibility).
- **Responsive implications:** Comprehension must not degrade when content
  is condensed for small viewports.
- **Motion implications:** Motion should clarify cause and effect, not
  require the user to infer it.
- **Review questions:** Would a first-time user understand this without
  help? Does any label or icon assume prior technical knowledge?

### 6.4 Visual Hierarchy

- **Normative statement:** Every screen must make its single most
  important element unambiguous.
- **Purpose:** Directs attention correctly regardless of profile or
  content density.
- **Required behavior:** Establish one clear primary focus per screen or
  view, with secondary and tertiary elements clearly subordinate.
- **Prohibited behavior:** Presenting multiple competing focal points with
  equal visual weight.
- **Showcase:** Hierarchy foregrounds creative or editorial content.
- **Precision:** Hierarchy foregrounds the data or action most relevant to
  the current task.
- **Flow:** Hierarchy foregrounds the single next action in a guided
  process.
- **Accessibility implications:** Visual hierarchy must be matched by
  semantic hierarchy (heading levels, landmark structure) for
  assistive-technology users.
- **Responsive implications:** The primary element must remain primary
  across breakpoints, even if its visual treatment changes.
- **Motion implications:** Motion may be used to draw attention to the
  primary element, but never to distract from it.
- **Review questions:** Is it obvious, without instructions, what matters
  most on this screen? Does the semantic structure match the visual one?

### 6.5 Controlled Expression

- **Normative statement:** Expressive or decorative elements must operate
  within KBDL's [controlled visual variables](#5-stable-and-variable-identity-elements)
  and must never be introduced as one-off, ungoverned effects.
- **Purpose:** Preserves cross-project recognizability while still
  allowing brand and profile personality.
- **Required behavior:** Draw expressive choices from the documented set
  of controlled variables; escalate anything outside that set through the
  [design-decision hierarchy](#8-design-decision-hierarchy).
- **Prohibited behavior:** Introducing bespoke effects, motion, or
  treatments that have no basis in a controlled variable or an approved
  exception.
- **Showcase:** Uses the upper range of controlled expression (motion
  amplitude, gradient intensity) more often than other profiles.
- **Precision:** Uses the lower range of controlled expression, favoring
  restraint.
- **Flow:** Uses a balanced middle range, favoring reassurance over
  intensity.
- **Accessibility implications:** Expression must always respect reduced-
  motion and contrast requirements regardless of profile.
- **Responsive implications:** Expressive intensity may be reduced on
  smaller viewports where space or performance is constrained.
- **Motion implications:** Motion amplitude is itself a controlled
  variable and must stay within documented bounds once defined.
- **Review questions:** Is this expressive choice traceable to a
  controlled variable? Would it need a new exception to justify it?

### 6.6 Consistent System Behavior

- **Normative statement:** A given interaction pattern must behave
  identically everywhere it appears within a KBDL project and across
  projects, regardless of profile.
- **Purpose:** Builds user trust and reduces relearning cost.
- **Required behavior:** Reuse the same interaction meaning (not
  necessarily the same visual intensity) for the same kind of action
  across the system.
- **Prohibited behavior:** Giving the same control type different
  behavior in different parts of a project, or between profiles, without
  an approved exception.
- **Showcase:** Interaction meaning stays constant even as visual
  presentation is more expressive.
- **Precision:** Consistency is critical for efficient repeated use.
- **Flow:** Consistency builds the trust needed for guided conversion
  paths.
- **Accessibility implications:** Consistent behavior is required for
  assistive-technology users who rely on predictable patterns.
- **Responsive implications:** Interaction meaning must be preserved when
  an interaction pattern adapts from pointer to touch.
- **Motion implications:** The same interaction should trigger
  recognizably similar motion feedback across contexts.
- **Review questions:** Does this control behave the way its counterparts
  behave elsewhere? Would a returning user be surprised by this behavior?

### 6.7 Adaptability Without Fragmentation

- **Normative statement:** Profiles and projects may adapt emphasis, but
  the result must still be recognizable as one system, not a fragmented
  set of unrelated designs.
- **Purpose:** Allows KBDL to serve three different profiles without
  becoming three different design languages.
- **Required behavior:** Apply the same principles and locked rules across
  Showcase, Precision, and Flow, adjusting only within controlled
  variables and profile-level emphasis (see
  [Section 9](#9-profile-level-interpretation)).
- **Prohibited behavior:** Creating profile-specific component anatomy,
  interaction meaning, or accessibility exceptions.
- **Showcase:** Adapts through stronger compositional and editorial
  emphasis.
- **Precision:** Adapts through density and information-hierarchy
  emphasis.
- **Flow:** Adapts through approachability and guided-progression
  emphasis.
- **Accessibility implications:** Adaptation must never reduce
  accessibility below the shared baseline.
- **Responsive implications:** Adaptation across breakpoints must follow
  the same responsive content-priority rule for every profile.
- **Motion implications:** Motion character stays recognizable across
  profiles even as amplitude varies.
- **Review questions:** If this screen were shown without its logo, would
  it still be recognizable as KBDL? Does this adaptation touch a locked
  rule?

### 6.8 Accessibility by Default

- **Normative statement:** Accessibility requirements apply to every
  component, profile, and expressive choice by default, not as an
  optional enhancement.
- **Purpose:** Reflects KBDL's WCAG 2.2 Level AA baseline and enhanced
  motion-safety requirements as non-negotiable, per
  [KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety).
- **Required behavior:** Evaluate every design decision — including
  expressive and decorative ones — against accessibility requirements
  before it is considered final.
- **Prohibited behavior:** Treating accessibility as an add-on pass
  performed after visual design is otherwise complete.
- **Showcase:** Editorial expression must remain fully accessible,
  including for media-heavy layouts.
- **Precision:** Dense data presentation must remain fully accessible,
  including for screen-reader table and state semantics.
- **Flow:** Guided flows must remain fully accessible, including for
  users relying on assistive technology to complete a transaction.
- **Accessibility implications:** This principle *is* the accessibility
  implication; it exists to prevent accessibility from being deferred.
- **Responsive implications:** Accessibility requirements apply at every
  breakpoint, not only the primary design reference size.
- **Motion implications:** Enhanced reduced-motion behavior applies
  regardless of profile or expressive intent.
- **Review questions:** Was accessibility considered from the first
  design decision, or only checked afterward? Does any decorative choice
  compromise a WCAG 2.2 AA success criterion?

### 6.9 Performance-Aware Enhancement

- **Normative statement:** Any visual or motion enhancement must account
  for its performance cost before it is adopted.
- **Purpose:** Prevents Digital Luxury from degrading the responsiveness
  that Technical Utility requires.
- **Required behavior:** Weigh the perceptual benefit of an enhancement
  against its cost to load time, frame rate, and battery/network
  conditions relevant to the target platform.
- **Prohibited behavior:** Adding effects (blur, layered transparency,
  continuous animation) without considering their runtime cost.
- **Showcase:** May accept higher enhancement cost for a bounded, high-
  impact moment (for example, an entrance sequence), not for continuous
  states.
- **Precision:** Enhancement cost must stay low, since interfaces are used
  intensively and repeatedly.
- **Flow:** Enhancement cost should stay low enough not to threaten
  perceived responsiveness of guided actions.
- **Accessibility implications:** Performance problems disproportionately
  harm users on constrained devices or connections, which is itself an
  accessibility concern.
- **Responsive implications:** Enhancement cost must be reassessed per
  breakpoint and device class, not assumed constant.
- **Motion implications:** Continuous or expensive motion must be
  justified against its performance cost, and must always respect
  reduced-motion preferences.
- **Review questions:** What is the measurable cost of this enhancement?
  Would it still be acceptable on a constrained device or network?

---

## 7. Visual Consistency

The following relationships must hold across every KBDL project,
regardless of profile, without yet defining final values:

- **Hierarchy** — the most important element is always the most visually
  and structurally prominent; hierarchy is established through the same
  combination of position, scale, and emphasis logic everywhere.
- **Proportion** — relationships between element sizes follow a
  deliberate, repeatable logic rather than being sized independently per
  screen.
- **Spacing relationships** — spacing follows a deliberate, repeated
  rhythm; the specific scale is defined later, but the *presence* of a
  rhythm (versus arbitrary per-instance spacing) is a locked rule.
- **Alignment** — elements align to a shared underlying structure so
  relationships between them are perceivable without conscious effort.
- **Typography relationships** — type establishes hierarchy through
  consistent relationships between weight, size step, and role (heading,
  body, caption), not through selecting a specific typeface or scale here.
- **Shape relationships** — corner treatment and geometric character are
  applied consistently across similar component types, whatever the final
  corner values turn out to be.
- **Surface composition** — surfaces (cards, panels, sheets) are composed
  according to one consistent logic for how content sits on a surface.
- **Border use** — borders, where used, follow a consistent purpose
  (separation, containment, or emphasis) rather than being applied
  arbitrarily.
- **Depth logic** — elevation communicates a single, consistent meaning
  (for example, "higher elevation = more temporarily focused content")
  across the system, without yet defining shadow values.
- **Icon treatment** — icons follow one consistent stylistic family and
  weight logic, rather than mixing incompatible icon styles.
- **Media treatment** — images, video, and illustration are framed and
  cropped according to one consistent logic appropriate to the content's
  role.
- **State presentation** — every component state (hover, focus, active,
  disabled, loading, error, success) is presented through a consistent
  combination of cues, never through color alone.
- **Motion character** — motion feels like it comes from the same
  "material," using consistent easing character and purpose logic, without
  yet defining exact durations or curves.
- **Theme relationships** — light and dark presentations express the same
  hierarchy and material logic; a theme changes surface values, not the
  underlying relationships.
- **Responsive behavior** — layouts reorganize content according to one
  consistent content-priority logic across breakpoints, rather than each
  screen defining its own responsive behavior independently.

---

## 8. Design-Decision Hierarchy

When a visual or interaction decision must be made, or when two
requirements appear to conflict, resolve using this order:

1. Safety and data integrity
2. Accessibility
3. User task and comprehension
4. Approved KBDL requirements
5. Content hierarchy
6. Responsive constraints
7. Performance
8. Project Profile
9. Controlled project customization
10. Open brand expression
11. Decorative preference

**Handling conflicts:** When two levels of this hierarchy appear to
conflict, the higher-numbered (lower-priority) concern yields. The
resolution and its rationale are recorded wherever the decision is
made — in the affected requirement's notes, or in a
[decision-register.md](decision-register.md) entry if the resolution sets
a precedent beyond a single instance.

**When an exception is required:** Any decision that would modify a
[locked identity rule](#5-stable-and-variable-identity-elements) or an
`Approved` requirement (levels 1–4) requires an approved exception per
[governance.md § Exception process](governance.md#exception-process).
Decisions at levels 5–11 do not require an exception, but must still be
documented if they establish a new pattern others will reuse.

**When a decision must stop for approval:** Any decision that would
expand scope beyond the currently active roadmap step, or that touches
levels 1–4, stops and is escalated to the project owner rather than
resolved unilaterally, per
[governance.md § Scope-change process](governance.md#scope-change-process).

**Sources that cannot override higher-priority requirements:** Project
Profile emphasis (level 8), controlled customization (level 9), and open
brand expression (level 10–11) can never override safety, accessibility,
approved requirements, content hierarchy, responsive constraints, or
performance (levels 1–7).

**Recording unapproved project requests:** A request that would require
overriding a higher-priority level is recorded as `Unresolved` or
`Recommended` (never silently implemented) in the
[traceability matrix](traceability-matrix.md), with a note describing what
approval would be required.

This hierarchy is consistent with KBDL's status semantics
([conventions.md §1](conventions.md#1-status-labels)): only requirements
with `Approved` lifecycle status may be implemented, and this hierarchy
governs how conflicts among already-approved concerns, and requests for
new exceptions, are resolved.

---

## 9. Profile-Level Interpretation

Showcase, Precision, and Flow are three expressions of one system: they
share every locked rule and core principle, and differ only in emphasis.

### 9.1 Showcase Profile

- **Editorial emphasis** — content and imagery are given more compositional
  weight than in the other profiles.
- **Media hierarchy** — photography, video, and illustration may take a
  primary structural role, not just a decorative one.
- **Stronger expression** — controlled variables (motion amplitude,
  gradient intensity) are used toward their upper documented range.
- **Larger compositional gestures** — layout may use bolder scale
  relationships to create impact, within proportion rules.
- **Reading and viewing comfort** — despite stronger expression, text and
  media must remain comfortable to read and view for extended periods.
- **Motion that settles during content consumption** — entrance or
  transition motion is appropriate, but motion must not continue
  indefinitely while a user is reading or viewing content.

### 9.2 Precision Profile

- **Information hierarchy** — structure favors fast scanning of data and
  state over compositional impact.
- **Repeated workflow efficiency** — controls used often are optimized for
  speed, per [Section 4](#4-relationship-between-luxury-and-utility).
- **Clear states** — state visibility is especially critical given the
  volume of concurrent information.
- **Density control** — density is deliberately managed against
  [Section 6.1](#61-clarity-before-spectacle), never allowed to exceed
  what supports clarity.
- **Predictable navigation** — navigation patterns remain stable across
  the product to support frequent, task-focused use.
- **Restrained signature effects** — controlled variables are used toward
  their lower documented range.

### 9.3 Flow Profile

- **Approachability** — tone and structure favor ease of entry for
  first-time users.
- **Clear primary actions** — every screen surfaces one unambiguous next
  step.
- **Guided progression** — multi-step processes make progress and next
  steps explicit.
- **Reassuring feedback** — feedback favors clarity and confidence over
  novelty.
- **Responsive simplicity** — layouts simplify gracefully on small
  viewports without losing guided structure.
- **Balanced expression** — controlled variables are used toward a
  middle range between Showcase and Precision.

### 9.4 Shared Constraints Across Profiles

Profiles may alter emphasis but cannot:

- Replace KBDL foundations.
- Remove accessibility rules.
- Change core interaction meaning.
- Introduce inconsistent component anatomy.
- Ignore reduced-motion behavior.
- Create unrelated visual identities.

---

## 10. Conforming Design Directions

These are conceptual examples only. No final mockups, palettes, fonts,
tokens, or component specifications are defined.

1. **Showcase, light presentation, high-expression marketing moment.** An
   editorial landing section uses large-scale typography and a bold media
   composition to introduce a project.
   - *Why it conforms:* Applies stronger expression within
     [controlled variables](#5-stable-and-variable-identity-elements)
     while preserving hierarchy and accessibility.
   - *Principles demonstrated:* Clarity Before Spectacle, Precision and
     Intentionality, Controlled Expression.
   - *Flexible elements:* Compositional scale, media treatment, motion
     amplitude.
   - *Rules that must remain unchanged:* Hierarchy logic, accessibility
     requirements, reduced-motion behavior.
   - *What would break conformance:* Sacrificing legible contrast or
     focus visibility for compositional impact.

2. **Showcase, dark presentation, content-consumption moment.** A project
   detail page in dark theme lets entrance motion settle once content
   loads, then remains still while the user reads.
   - *Why it conforms:* Motion serves an entrance/feedback purpose and
     then stops, per Motion Purpose and Section 9.1.
   - *Principles demonstrated:* Accessibility by Default,
     Performance-Aware Enhancement.
   - *Flexible elements:* Entrance motion character, media framing.
   - *Rules that must remain unchanged:* Motion must not continue
     indefinitely during reading; reduced-motion preference must be
     respected.
   - *What would break conformance:* A looping decorative animation that
     persists while the user reads.

3. **Precision, light presentation, repeated utility workflow.** A
   dashboard's filter-and-review workflow uses restrained, low-amplitude
   feedback and a stable, predictable layout across sessions.
   - *Why it conforms:* Prioritizes repeated-workflow efficiency per
     Section 4 and 9.2.
   - *Principles demonstrated:* Consistent System Behavior, Technical
     Utility's efficient repeated interaction.
   - *Flexible elements:* Density within clarity limits, accent use for
     status indicators.
   - *Rules that must remain unchanged:* Component-state clarity,
     interaction predictability.
   - *What would break conformance:* Adding a decorative transition that
     measurably slows the filter action.

4. **Precision, dark presentation, mobile layout.** A dashboard's mobile
   view reorganizes a data table into prioritized cards, preserving which
   data matters most.
   - *Why it conforms:* Follows responsive content-priority as a locked
     rule, per Section 5.1 and 7.
   - *Principles demonstrated:* Adaptability Without Fragmentation, Visual
     Hierarchy.
   - *Flexible elements:* Card layout, information density per card.
   - *Rules that must remain unchanged:* Relative priority of information
     must match the desktop view.
   - *What would break conformance:* Dropping secondary-but-important data
     entirely instead of reorganizing it.

5. **Flow, light presentation, guided workflow.** A checkout-style flow
   presents one primary action per step, with reassuring progress
   indication and balanced, non-distracting motion.
   - *Why it conforms:* Matches Section 9.3's guided-progression and
     reassuring-feedback emphasis.
   - *Principles demonstrated:* Consumer Comprehension, Consistent System
     Behavior.
   - *Flexible elements:* Illustration style, progress-indicator
     treatment.
   - *Rules that must remain unchanged:* One unambiguous primary action
     per step; accessible error recovery.
   - *What would break conformance:* Presenting multiple equally weighted
     calls to action on one step.

6. **Flow, mobile layout, dark presentation.** A mobile onboarding flow in
   dark theme uses simplified layout, large touch targets, and calm
   entrance motion.
   - *Why it conforms:* Applies responsive simplicity and balanced
     expression per Section 9.3, and accessible target sizing per Section
     6.8.
   - *Principles demonstrated:* Accessibility by Default, Performance-Aware
     Enhancement.
   - *Flexible elements:* Illustration, exact motion amplitude within
     documented range.
   - *Rules that must remain unchanged:* Touch target accessibility,
     reduced-motion behavior, single clear next action.
   - *What would break conformance:* Small, closely packed controls that
     are hard to target on touch devices.

---

## 11. Non-Conforming Design Directions

For each pattern: why it violates KBDL, which principle it breaks, the
risk it creates, and how to correct it without prescribing final token
values.

1. **Excessive neon as the primary identity.**
   - *Why it violates KBDL:* Contradicts the identity exclusions in
     Section 1 — KBDL is not a cyberpunk theme.
   - *Principle broken:* Precision and Intentionality; Clarity Before
     Spectacle.
   - *Risk:* Identity fragmentation and reduced legibility from
     high-saturation, high-contrast accents used pervasively.
   - *Correction:* Treat accent intensity as a controlled variable used
     selectively, not as the dominant visual language.

2. **Unrestricted glassmorphism.**
   - *Why it violates KBDL:* Section 1 explicitly excludes glassmorphism
     as a default identity; Section 2 prohibits low-contrast translucent
     surfaces.
   - *Principle broken:* Accessibility by Default; Digital Luxury's
     material coherence.
   - *Risk:* Contrast failures and inconsistent surface legibility.
   - *Correction:* Limit translucency to specific, justified surfaces with
     contrast verified against accessibility requirements once defined.

3. **Continuous decorative motion.**
   - *Why it violates KBDL:* Violates Motion Purpose (Section 5.1): motion
     must serve feedback, hierarchy, or continuity, never run
     indefinitely as decoration.
   - *Principle broken:* Performance-Aware Enhancement; Accessibility by
     Default (motion-safety).
   - *Risk:* Distraction, motion sickness for sensitive users, and battery
     or performance cost.
   - *Correction:* Bound motion to a triggered event (entrance, state
     change) rather than a looping ambient effect, and honor
     reduced-motion preferences.

4. **Animation that delays interaction.**
   - *Why it violates KBDL:* Violates Section 4's priority that
     expressiveness cannot delay frequent actions.
   - *Principle broken:* Technical Utility's responsive feedback;
     Performance-Aware Enhancement.
   - *Risk:* Perceived sluggishness and task abandonment.
   - *Correction:* Decouple the visual flourish from the action's
     completion, or shorten/remove it for repeated interactions.

5. **Low-contrast luxury styling.**
   - *Why it violates KBDL:* Directly contradicts Section 2's exclusion of
     low-contrast translucent surfaces as "luxury."
   - *Principle broken:* Accessibility by Default.
   - *Risk:* WCAG 2.2 AA contrast failure; excludes low-vision users.
   - *Correction:* Redesign the surface or text treatment to meet
     accessible contrast while preserving hierarchy through other means
     (weight, spacing, structure).

6. **Technical density without content priority.**
   - *Why it violates KBDL:* Violates Technical Utility's prohibition on
     "visual density without prioritization."
   - *Principle broken:* Visual Hierarchy; Consumer Comprehension.
   - *Risk:* Cognitive overload, especially for general consumers in the
     Precision Profile.
   - *Correction:* Apply content-priority and progressive-disclosure
     logic before adding density.

7. **Different component behavior between profiles.**
   - *Why it violates KBDL:* Violates Adaptability Without Fragmentation
     and Section 9.4's shared constraints.
   - *Principle broken:* Consistent System Behavior.
   - *Risk:* User confusion when moving between KBDL projects; erodes the
     "one system" identity.
   - *Correction:* Keep interaction meaning identical across profiles;
     vary only emphasis within controlled variables.

8. **Mobile interfaces that merely shrink desktop layouts.**
   - *Why it violates KBDL:* Violates the locked rule of responsive
     content priority (Section 5.1, 7).
   - *Principle broken:* Adaptability Without Fragmentation; Consumer
     Comprehension.
   - *Risk:* Illegible or unusable small-viewport experiences.
   - *Correction:* Reorganize content by priority for the viewport, rather
     than uniformly scaling down a larger layout.

9. **Excessive use of monospaced type.**
   - *Why it violates KBDL:* Contradicts Technical Utility's exclusion of
     "monospaced typography everywhere."
   - *Principle broken:* Consumer Comprehension.
   - *Risk:* Reduced readability and an unintended "developer tool"
     impression for general consumers.
   - *Correction:* Reserve monospaced treatment for genuinely tabular or
     code-like content only, once typography roles are defined.

10. **Arbitrary project-specific spacing.**
    - *Why it violates KBDL:* Violates the locked spacing-relationships
      rule (Section 5.1, 7).
    - *Principle broken:* Precision and Intentionality.
    - *Risk:* Visual inconsistency that erodes cross-project
      recognizability.
    - *Correction:* Derive spacing from the shared rhythm once the visual
      foundations module defines it, rather than per-project values.

11. **Inconsistent state treatment.**
    - *Why it violates KBDL:* Violates the locked component-state-clarity
      rule (Section 5.1).
    - *Principle broken:* Consistent System Behavior; Technical Utility's
      state visibility.
    - *Risk:* Users cannot reliably tell what state a component is in.
    - *Correction:* Apply one documented state model consistently once
      the components module defines it.

12. **Decorative effects that conceal focus.**
    - *Why it violates KBDL:* Violates Accessibility by Default and the
      locked accessibility-requirements rule.
    - *Principle broken:* Accessibility by Default.
    - *Risk:* Keyboard users cannot track focus; WCAG failure.
    - *Correction:* Ensure any decorative treatment layers behind, never
      over, the focus indicator.

13. **Using color alone for meaning.**
    - *Why it violates KBDL:* Violates the locked component-state-clarity
      rule directly.
    - *Principle broken:* Accessibility by Default; Technical Utility's
      state visibility.
    - *Risk:* Excludes color-blind and low-vision users; fails WCAG 2.2
      AA.
    - *Correction:* Pair color with an icon, label, or pattern for every
      meaningful distinction.

14. **Branding that replaces KBDL foundations.**
    - *Why it violates KBDL:* Violates Section 5.3 — open brand expression
      must respect, not override, locked rules and approved requirements.
    - *Principle broken:* Adaptability Without Fragmentation.
    - *Risk:* The project stops being recognizable as KBDL, undermining
      the cross-project consistency strategy (KBDL-DEC-003).
    - *Correction:* Reframe the brand goal within controlled variables and
      open brand-expression categories, or escalate through the
      [design-decision hierarchy](#8-design-decision-hierarchy) for an
      approved exception.

15. **Multiple simultaneous signature animations.**
    - *Why it violates KBDL:* Violates Motion Purpose and Clarity Before
      Spectacle — competing motion has no single clear purpose.
    - *Principle broken:* Visual Hierarchy; Performance-Aware Enhancement.
    - *Risk:* Cognitive overload and unclear cause-and-effect between
      motion and user action.
    - *Correction:* Sequence or prioritize motion so only one signature
      moment plays at a time, tied to a clear trigger.

16. **Removing controls for visual minimalism.**
    - *Why it violates KBDL:* Violates Technical Utility's prohibition on
      "hiding functionality for aesthetic purity" and Digital Luxury's
      matching exclusion.
    - *Principle broken:* Consumer Comprehension; Technical Utility.
    - *Risk:* Users cannot discover or complete needed tasks.
    - *Correction:* Find a KBDL-compliant way to reduce visual weight
      (grouping, progressive disclosure) that preserves discoverability.

---

## 12. Normative Requirements

The following requirements make this specification enforceable. All carry
lifecycle status `Approved` (this is the approved KBDL-002 deliverable) and
validation status `Not verified` unless stated otherwise — writing a
requirement does not verify it; verification requires recorded review
evidence per [governance.md](governance.md#evidence-required-to-declare-a-requirement-verified).

- **KBDL-PRN-001** — KBDL implementations **must** present the identity
  described in [Section 1](#1-identity-statement) and **must not** adopt
  any of the explicitly excluded identities (cyberpunk theme, neon
  visual-effects collection, glassmorphism library, dashboard-only system,
  portfolio-only system, animation showcase, single front-end framework, or
  single brand identity).
  - Lifecycle status: Approved. Provenance: User-provided (blueprint) and
    Confirmed (derived from KBDL-001 decisions). Validation status: Not
    verified.
  - Related principle: Section 1 (Identity Statement).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Visual foundations, Themes, Components.
  - Validation method: Manual design review against this section at each
    later module's approval gate.

- **KBDL-PRN-002** — Any KBDL design decision **must** resolve conflicts
  between Digital Luxury and Technical Utility using the priority order in
  [Section 4](#4-relationship-between-luxury-and-utility); a decision
  **must not** allow expressive character or decorative enhancement to
  override correctness, accessibility, task comprehension, hierarchy,
  performance, or visual consistency.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 4; Section 6.1, 6.8, 6.9.
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Motion, Accessibility, Components.
  - Validation method: Manual review of design decisions against the
    priority order; disputes escalated per Section 8.

- **KBDL-PRN-003** — Every KBDL project **must** implement the nine core
  principles in [Section 6](#6-core-principles) as decision rules; a
  design or implementation choice that violates a principle's "prohibited
  behavior" **must not** proceed without an approved exception.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 6 (all nine principles).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: All later modules.
  - Validation method: Manual review using each principle's review
    questions, at each later module's approval gate.

- **KBDL-PRN-004** — KBDL projects **must** preserve the fifteen visual-
  consistency relationships in [Section 7](#7-visual-consistency) across
  themes, profiles, and breakpoints; a project **must not** define final
  values that are inconsistent with these relationships once later modules
  approve them.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 7.
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Visual foundations, Themes, Responsive
    behavior.
  - Validation method: Manual cross-reference review once foundation,
    theme, and responsive modules are approved.

- **KBDL-PRN-005** — The [locked identity rules](#51-locked-identity-rules)
  **must not** be modified by any project, profile, or customization
  without an approved exception recorded per
  [governance.md § Exception process](governance.md#exception-process);
  [controlled visual variables](#52-controlled-visual-variables) **may**
  vary only within limits defined by later modules; [open brand
  expression](#53-open-brand-expression) **must** respect locked rules and
  approved requirements at all times.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 5.
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Visual foundations, Themes, Motion,
    Customization.
  - Validation method: Manual review of any proposed exception against
    the exception process.

- **KBDL-PRN-006** — Any visual or interaction decision **must** be
  resolved using the [design-decision hierarchy](#8-design-decision-hierarchy)
  in Section 8; a decision **must not** allow Project Profile emphasis,
  controlled customization, or open brand expression to override safety,
  accessibility, approved requirements, content hierarchy, responsive
  constraints, or performance.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 8.
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: All later modules; Governance.
  - Validation method: Manual review of decision records against the
    hierarchy; conflicts escalated per governance's conflict-resolution
    process.

- **KBDL-PRN-007** — Showcase, Precision, and Flow **must** share every
  locked identity rule and core principle; a profile **must not** replace
  KBDL foundations, remove accessibility rules, change core interaction
  meaning, introduce inconsistent component anatomy, ignore reduced-motion
  behavior, or create an unrelated visual identity, as stated in
  [Section 9.4](#94-shared-constraints-across-profiles).
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 9.
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Project profiles, Components.
  - Validation method: Manual cross-profile consistency review once the
    project-profiles module is approved.

- **KBDL-PRN-008** — Design and implementation work **must not** introduce
  any of the [non-conforming patterns](#11-non-conforming-design-directions)
  in Section 11 without an approved exception; where such a pattern is
  found, it **must** be corrected using the direction given for that
  pattern.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: Section 11; Section 6 (all principles referenced
    per pattern).
  - Applicable profiles: Showcase, Precision, Flow.
  - Related future modules: Visual foundations, Themes, Motion,
    Accessibility, Components.
  - Validation method: Manual conformance review against the pattern list
    at each later module's approval gate, recorded in the
    [conformance checklist](conformance-checklist.md).

---

## 13. Traceability

See [traceability-matrix.md](traceability-matrix.md) for how each
requirement above traces to its blueprint origin, approval status,
validation status, and evidence. See
[decision-register.md](decision-register.md) for any decision recorded as
part of this module.
