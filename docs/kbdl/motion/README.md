# KBDL Motion — Expressive Motion Language

Lifecycle status: mixed. `Approved` only for the terminology, identity
translation, purpose model, and category-completeness structure defined
below, where each directly restates an already-`Approved` KBDL-002
principle, KBDL-004 theme rule, or the motion-safety baseline
(`KBDL-DEC-010`) — see [§9](#9-normative-requirements) for exact
requirement-level status. `Recommended` for the five-level motion
hierarchy, the intensity model, and every **exact** duration, easing
curve, distance, scale, stagger, repetition default, substitution-matrix
detail, token-naming architecture, profile-level intensity adjustment,
and pattern default proposed in this module — `User-provided`
provenance, `Not verified`/`Not applicable` validation, pending
project-owner approval via [§10](#10-motion-decision-packet). No
`Recommended` value in this module authorizes implementation on its
own — see [conventions.md §1.1](../conventions.md#11-lifecycle--approval-status).

Return to the [specification index](../README.md).

This document is the entry point for KBDL's motion language (KBDL-005).
Detailed guidance lives in companion documents:

- [foundations.md](foundations.md) — motion categories, hierarchy detail,
  intensity model, spatial movement, choreography, entrance/exit, and
  state-change motion.
- [timing-easing.md](timing-easing.md) — timing architecture, duration
  recommendations, easing architecture, and the conceptual motion-token
  architecture.
- [patterns.md](patterns.md) — navigation, loading, direct manipulation,
  attention, ambient, scroll-linked, and media motion; theme-transition
  motion; interruption/reversal; profile interpretation; the motion
  pattern matrix; and conformance examples.
- [accessibility-performance.md](accessibility-performance.md) —
  reduced-motion and no-motion parity, motion-safety constraints,
  performance requirements, and mobile/input-method considerations.
- [validation.md](validation.md) — motion validation specification and
  conformance criteria.

## 1. Repository and Roadmap Context

KBDL-001 (governance), KBDL-002 (principles), KBDL-003 (visual
foundations), and KBDL-004 (adaptive themes, including the ten-item
theme decision packet recorded under
[KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved))
are `Approved`. KBDL-005 (Motion) is the next eligible roadmap step. This
module does not begin KBDL-006 (Responsive and Accessibility) or any
later step, and does not reopen any approved KBDL-004 theme decision —
it only supplies the timing and easing that KBDL-004's theme-transition
guidance explicitly deferred (see [patterns.md §8](patterns.md#8-theme-transition-motion)).

The following remain outside this module's scope, unchanged from
KBDL-004-A1: Accent-surface, Scrim, and Selection-background opacity;
translucent caption-band or media-overlay variants; project-specific
media composites; account-level theme synchronization; high-contrast or
forced-colors mode; the data-visualization palette; and any
implementation-layer format (CSS custom properties, JSON tokens,
component-level tokens, framework APIs, animation libraries).

## 2. Motion Terminology

- **Motion** — any visible change over time. The broadest term; every
  other term below names a specific kind of motion.
- **Animation** — a designed visual transition or repeated visual
  behavior, authored rather than incidental.
- **Transition** — movement between two defined states (e.g., closed to
  open). Every transition has a clear "before" and "after."
- **Transformation** — a specific visual change applied during motion:
  translation, scale, rotation, opacity, or shape change.
- **Choreography** — the timing relationships among multiple elements
  changing together (see [foundations.md §5](foundations.md#5-choreography-and-sequencing)).
- **Sequence** — an ordered series of motion events with a defined start
  order.
- **Stagger** — a controlled time offset applied between otherwise
  similar, related elements in a sequence.
- **Direct manipulation** — visual response tied continuously to live
  user input (e.g., a dragged element following the pointer).
- **Feedback motion** — motion whose purpose is confirming input, a
  state, or a system response.
- **Navigation motion** — motion that preserves spatial or structural
  continuity while the user moves between views.
- **Attention motion** — motion used to direct focus toward a relevant
  change, bounded and non-exclusive (see [patterns.md §4](patterns.md#4-attention-motion)).
- **Ambient motion** — non-essential motion that may continue without
  direct user input (see [patterns.md §5](patterns.md#5-ambient-and-continuous-motion)).
- **Continuous motion** — motion that repeats or persists rather than
  running once to completion.
- **Scroll-linked motion** — motion whose progress is tied to the user's
  scroll position (see [patterns.md §6](patterns.md#6-scroll-linked-motion)).
- **Entrance** — the introduction of content or a state into view.
- **Exit** — the removal of content or a state from view.
- **Interruption** — stopping motion before it completes, typically
  because of new input or a new state.
- **Reversal** — returning from an in-progress transition back toward
  its previous state, rather than continuing forward.
- **Reduced motion** — a presentation that removes or significantly
  simplifies non-essential movement in response to user preference (see
  [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity)).
- **No-motion fallback** — an instant or static state change that
  preserves all functionality and meaning when motion is unavailable or
  disabled.
- **Motion parity** — the property that full-motion, reduced-motion, and
  no-motion presentations of the same interaction communicate the same
  meaning and preserve the same functionality.

These terms are distinct and must not be used interchangeably: an
**animation** is one way of presenting a **transition**; a **transition**
is one instance of **motion**; **choreography** governs how multiple
**transitions** relate in time; **ambient** and **continuous** motion are
not **feedback** or **attention** motion, and must never be required for
comprehension.

## 3. Motion Identity

### 3.1 Digital Luxury in motion

Digital Luxury (per [principles.md §2](../principles.md#2-digital-luxury))
is expressed in motion through: precision (motion starts and ends at
exact, deliberate points, never approximate); deliberate pacing (timing
communicates confidence, not haste or delay); controlled sequencing
(choreography reflects hierarchy, never randomness); smooth state
continuity (nothing jumps or flickers unexpectedly); refined arrival and
departure (entrance and exit feel considered, not abrupt or excessive);
high-quality interruption behavior (motion resolves gracefully when
interrupted, never freezing or glitching); restraint (motion is used
because it serves a purpose, not because it is possible); and attention
to detail (every interactive state has deliberate motion feedback, not a
platform default).

Digital Luxury in motion must **not** mean: slow interfaces; excessive
cinematic transitions; constant floating or drifting; large parallax
effects; decorative delay before required content or actions appear;
constant overshoot or bounce applied everywhere; uninterruptible
sequences; or motion that obscures content.

### 3.2 Technical Utility in motion

Technical Utility (per [principles.md §3](../principles.md#3-technical-utility))
is expressed in motion through: predictable feedback (the same
interaction produces recognizably similar motion everywhere); state
continuity (motion shows the relationship between the old and new
state, not just the new state); fast response to input (acknowledgment
motion begins immediately, never waiting for a decorative cue);
efficient repeated interaction (frequently used motion is short);
visible progress (ongoing operations show real, honest progress where
available); reversible transitions (a transition can be interrupted and
reversed without producing an invalid state); stable spatial
relationships (motion never relocates content in a way that breaks the
user's mental map); and accessible alternatives (every meaningful motion
has a reduced- or no-motion equivalent that preserves meaning).

Technical Utility in motion must **not** mean: mechanically instant
behavior everywhere (removing all motion is not efficiency — it can
remove necessary feedback); sterile or abrupt state changes; excessive
dashboard micro-animation; terminal-like motion metaphors; or motion used
to expose internal system complexity to end users.

### 3.3 Relationship and conflict resolution

When expressive motion character conflicts with usability, KBDL resolves
in this order (extending [principles.md §4](../principles.md#4-relationship-between-luxury-and-utility)
with motion-specific detail):

1. **Safety and correctness** — motion must never mislead about system
   state or hide a destructive or irreversible action.
2. **Accessibility and motion safety** — reduced-motion preference and
   the [motion-safety constraints](accessibility-performance.md#2-motion-safety)
   always win.
3. **Immediate input acknowledgment** — the interface must acknowledge
   input before any decorative motion plays.
4. **Task completion** — motion must not add latency to completing a
   task.
5. **State comprehension** — motion must clarify, not obscure, what
   changed.
6. **Spatial continuity** — motion should preserve the user's sense of
   where things are, when practical.
7. **Performance** — motion must respect the [performance requirements](accessibility-performance.md#3-performance-requirements).
8. **KBDL motion consistency** — motion should match established KBDL
   motion character.
9. **Expressive character** — Digital Luxury's pacing, sequencing, and
   restraint.
10. **Decorative embellishment** — the lowest priority; purely ornamental
    motion yields to everything above it.

**Conflict example 1 — Signature entrance versus repeated filtering.** A
Precision dashboard's list-filter action currently plays a 400ms
signature entrance animation on every filter change. Because filtering
is a frequent, task-critical action, task completion (level 4) outranks
expressive character (level 9): the entrance must be shortened
dramatically or removed for this interaction, even though the same
entrance remains appropriate for a rare, first-time onboarding moment.

**Conflict example 2 — Ambient background motion during reading.** A
Showcase project detail page has a slowly drifting background gradient
that continues while the user reads body copy. Because sustained,
uncontrolled motion near reading content risks distraction and motion
sickness, accessibility and motion safety (level 2) outrank expressive
character (level 9): the ambient motion must pause, or slow to
imperceptibility, once the user is reading, per
[patterns.md §5](patterns.md#5-ambient-and-continuous-motion).

**Conflict example 3 — Theme-transition duration versus flash
avoidance.** A longer, more luxurious theme-transition duration is
proposed to make the light/dark switch feel more deliberate. Because a
longer duration on a full-surface color change risks an intermediate
low-contrast or jarring state, accessibility (level 2) and state
comprehension (level 5) outrank expressive character (level 9): the
transition duration must stay short enough that no intermediate frame
becomes illegible, per [patterns.md §8](patterns.md#8-theme-transition-motion).

**Conflict example 4 — Parallax hero versus performance on constrained
devices.** A Showcase landing hero proposes large parallax movement
tied to scroll. On a lower-performance device, this risks dropped frames
and input lag. Performance (level 7) and accessibility (level 2, via
motion safety's large-parallax restriction) outrank expressive character
(level 9): parallax amplitude must be bounded and must degrade to a
static or minimally-parallaxed fallback, per
[patterns.md §6](patterns.md#6-scroll-linked-motion).

**Conflict example 5 — Attention motion versus keyboard focus.** A
notification badge pulses continuously to draw attention while a
keyboard user is mid-task elsewhere on the page. Because attention
motion must never steal or obscure keyboard focus, accessibility (level
2) and state comprehension (level 5) outrank expressive character (level
9): the pulse must be bounded in repetition and must never move focus or
visually compete with the actual focus indicator, per
[patterns.md §4](patterns.md#4-attention-motion).

## 4. Motion Purposes and Categories

Every KBDL motion pattern must serve at least one documented purpose;
see [foundations.md §1](foundations.md#1-motion-purposes) for the full
purpose model (acknowledge input, confirm completion, communicate state
change, preserve spatial continuity, explain hierarchy, reveal or
conceal content, communicate progress, communicate interruption,
communicate error or recovery, direct attention, establish relationship,
support orientation, express brand character, provide delight without
blocking) and [foundations.md §2](foundations.md#2-motion-categories) for
the ten motion categories (immediate feedback, state transition, spatial
navigation, content change, system feedback, attention, direct
manipulation, media, ambient, theme transition). Motion without a
documented purpose is decorative and must remain removable without
functional loss.

## 5. Motion Hierarchy and Intensity

See [foundations.md §3](foundations.md#3-motion-hierarchy) for the
five-level hierarchy (None, Functional, Supportive, Expressive,
Exceptional) governing how much visual emphasis motion may receive, and
[foundations.md §4](foundations.md#4-motion-intensity) for the intensity
model (duration, distance, scale, rotation, opacity, blur/depth, element
count, stagger, repetition, screen coverage, input independence,
contrast change, and directional complexity — never duration alone).

## 6. Timing, Duration, and Easing

See [timing-easing.md](timing-easing.md) for the full timing
architecture, duration recommendations, easing architecture, and the
conceptual motion-token architecture. All exact values in that document
are `Recommended` pending [§10](#10-motion-decision-packet).

## 7. Patterns, Profiles, and Conformance

See [patterns.md](patterns.md) for spatial movement, choreography,
entrance/exit, state-change motion, navigation continuity, loading and
progress, direct manipulation, attention, ambient and scroll-linked
motion, media motion, theme-transition motion, interruption/reversal,
profile-level interpretation, the motion pattern matrix, and conformance
examples.

## 8. Accessibility and Performance

See [accessibility-performance.md](accessibility-performance.md) for the
reduced-motion and no-motion parity matrix, motion-safety constraints,
performance requirements, and mobile/input-method considerations.

## 9. Normative Requirements

Requirement IDs use the `KBDL-MOT-###` scheme
([conventions.md §2](../conventions.md#2-requirement-identification)).
Requirements directly and explicitly supported by an already-`Approved`
KBDL-002 principle or KBDL-004 theme rule carry lifecycle status
`Approved`; requirements introducing new KBDL-005 policy (timing values,
easing curves, distances, scales, stagger, intensity defaults, pattern
defaults) carry lifecycle status `Recommended` pending
[§10](#10-motion-decision-packet). Writing or manually reviewing a
requirement does not make its implementation behavior `Verified` — see
[validation.md](validation.md).

- **KBDL-MOT-001** — KBDL motion **must** serve at least one documented
  purpose from [foundations.md §1](foundations.md#1-motion-purposes);
  motion with no documented purpose **must** be treated as decorative and
  removable.
  - Lifecycle status: Approved (directly restates the locked Motion
    Purpose rule, [principles.md §5.1](../principles.md#51-locked-identity-rules)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-005` (locked identity rules).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §1](foundations.md#1-motion-purposes).
  - Related future modules: Components (`CMP`), where per-component
    motion purpose is assigned.
  - Validation method: Manual review confirming every documented motion
    pattern cites a purpose from the approved list.

- **KBDL-MOT-002** — Terminology defined in [§2](#2-motion-terminology)
  **must** be used consistently; "motion," "animation," "transition," and
  "choreography" **must not** be used interchangeably in KBDL
  documentation or specifications.
  - Lifecycle status: Approved. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-PRN-003` (core principles, Precision and
    Intentionality).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§2](#2-motion-terminology).
  - Related future modules: All later modules referencing motion.
  - Validation method: Manual terminology-consistency review.

- **KBDL-MOT-003** — Motion **must** resolve conflicts between expressive
  character and usability using the ten-level order in
  [§3.3](#33-relationship-and-conflict-resolution); motion **must not**
  allow expressive character or decorative embellishment to override
  safety, accessibility, input acknowledgment, task completion, state
  comprehension, spatial continuity, performance, or KBDL motion
  consistency.
  - Lifecycle status: Approved (directly extends `KBDL-PRN-002`).
    Provenance: Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§3.3](#33-relationship-and-conflict-resolution).
  - Related future modules: Components, Accessibility (`A11Y`).
  - Validation method: Manual review of motion decisions against the
    priority order; disputes escalated per
    [governance.md](../governance.md).

- **KBDL-MOT-004** — Every motion category in
  [foundations.md §2](foundations.md#2-motion-categories) **must**
  document purpose, default intensity, permitted and prohibited
  transformations, interruption behavior, reduced-motion response,
  performance considerations, and profile-level variation.
  - Lifecycle status: Approved (structural requirement; the categories'
    exact intensity defaults remain `Recommended`, see `KBDL-MOT-006`).
    Provenance: User-provided. Validation status: Not verified.
  - Related principle: `KBDL-PRN-004` (visual-consistency relationships,
    motion character).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §2](foundations.md#2-motion-categories).
  - Related future modules: Components.
  - Validation method: Manual completeness review per category.

- **KBDL-MOT-005** — The five-level motion hierarchy in
  [foundations.md §3](foundations.md#3-motion-hierarchy) **must** govern
  how much visual emphasis any motion pattern may receive; Level 4
  (Exceptional) motion **must** require explicit project-owner approval
  before use.
  - Lifecycle status: Recommended (new KBDL-005 architecture; the
    concept that emphasis must be governed by a hierarchy is consistent
    with `KBDL-PRN-002`, but the specific five-level structure and names
    are new policy). Provenance: User-provided. Validation status: Not
    verified.
  - Related principle: `KBDL-PRN-002`, `KBDL-PRN-004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §3](foundations.md#3-motion-hierarchy).
  - Related future modules: Components, Project profiles (`PRO`).
  - Validation method: Manual review of Exceptional-level usage once
    implemented; project-owner review (not yet performed).

- **KBDL-MOT-006** — Motion intensity **must** be assessed using the
  multi-factor model in [foundations.md §4](foundations.md#4-motion-intensity)
  (duration, distance, scale, rotation, opacity, blur/depth, element
  count, stagger, repetition, screen coverage, input independence,
  contrast change, directional complexity); duration alone **must not**
  be treated as a complete intensity measure.
  - Lifecycle status: Recommended (new KBDL-005 model). Provenance:
    User-provided. Validation status: Not verified.
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §4](foundations.md#4-motion-intensity).
  - Related future modules: Components.
  - Validation method: Manual review of intensity assessments once
    implemented; project-owner review (not yet performed).

- **KBDL-MOT-007** — The semantic timing classes in
  [timing-easing.md §1](timing-easing.md#1-timing-architecture) **must**
  be used for any KBDL motion; required interaction **must not** wait for
  decorative motion to complete.
  - Lifecycle status: Recommended (new KBDL-005 timing model; the
    underlying rule that "required interaction must not wait for
    decorative motion" restates `KBDL-PRN-002`/§4's task-completion
    priority and is itself Approved, but the specific timing-class names
    and ranges are new). Provenance: User-provided. Validation status:
    Not verified.
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [timing-easing.md §1](timing-easing.md#1-timing-architecture).
  - Related future modules: Components.
  - Validation method: Manual review of timing-class usage once
    implemented; project-owner review (not yet performed).

- **KBDL-MOT-008** — The exact duration recommendations in
  [timing-easing.md §2](timing-easing.md#2-duration-recommendations)
  **must not** be treated as `Approved` until the project owner approves
  them via [§10](#10-motion-decision-packet).
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable (a numerical recommendation, not yet a
    testable implementation claim).
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [timing-easing.md §2](timing-easing.md#2-duration-recommendations).
  - Related future modules: Components.
  - Validation method: Project-owner review (not yet performed); manual
    implementation review once an implementation exists.

- **KBDL-MOT-009** — The semantic easing categories and exact curves in
  [timing-easing.md §3](timing-easing.md#3-easing-architecture) **must**
  remain framework-independent and **must** each be evaluated for
  interruption and reversal behavior before use.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable (conceptual review only; no implementation
    exists).
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [timing-easing.md §3](timing-easing.md#3-easing-architecture).
  - Related future modules: Components.
  - Validation method: Manual conceptual review (performed, see
    [timing-easing.md §3](timing-easing.md#3-easing-architecture));
    project-owner approval (not yet performed).

- **KBDL-MOT-010** — Spatial movement **must** follow the constraints in
  [foundations.md §6](foundations.md#6-spatial-movement) — movement
  direction must correspond to spatial or structural meaning, large
  movement must remain rare, and parallax must reduce or disable under
  reduced motion.
  - Lifecycle status: Recommended (the individual constraints extend
    already-Approved principles and theme rules, but the consolidated
    spatial-movement architecture is new KBDL-005 policy). Provenance:
    User-provided. Validation status: Not verified.
  - Related principle: `KBDL-PRN-004`; `KBDL-THM-012a` (reduced motion).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §6](foundations.md#6-spatial-movement).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-011** — Choreography **must** reflect hierarchy — primary
  state change **must** lead secondary decoration, and stagger **must
  not** create excessive cumulative delay, per
  [foundations.md §5](foundations.md#5-choreography-and-sequencing).
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-PRN-004`, `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §5](foundations.md#5-choreography-and-sequencing).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-012** — Destructive or safety-critical actions **must not**
  rely on exit animation as confirmation; removed content **must not**
  remain focusable, per
  [foundations.md §7](foundations.md#7-entrance-and-exit-behavior).
  - Lifecycle status: Approved (directly restates the safety/correctness
    priority already established in `KBDL-PRN-002` and
    [§3.3](#33-relationship-and-conflict-resolution)). Provenance:
    Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §7](foundations.md#7-entrance-and-exit-behavior).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-013** — Navigation motion **must** reinforce information
  structure and **must not** delay access to required content or disrupt
  focus location, per
  [patterns.md §1](patterns.md#1-navigation-and-spatial-continuity).
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-PRN-002`, `KBDL-PRN-004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §1](patterns.md#1-navigation-and-spatial-continuity).
  - Related future modules: Components (`CMP`, navigation components).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-014** — Loading and progress motion **must not** imply
  progress that is not occurring, **must** stop when loading ends, and
  **must** remain understandable without motion, per
  [patterns.md §2](patterns.md#2-loading-and-progress).
  - Lifecycle status: Approved (directly restates Technical Utility's
    "visible progress" and "error prevention" qualities). Provenance:
    Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-002` (Technical Utility).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §2](patterns.md#2-loading-and-progress).
  - Related future modules: Components (feedback/system-state).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-015** — Direct-manipulation motion **must** track input
  directly, **must** support cancellation or reversal where the
  interaction permits, and **must** provide a keyboard or control
  alternative for gesture-only behavior, per
  [patterns.md §3](patterns.md#3-direct-manipulation-and-gesture-response).
  - Lifecycle status: Approved (directly restates accessibility's
    requirement for a non-gesture equivalent). Provenance: Confirmed.
    Validation status: Not verified.
  - Related principle: `KBDL-PRN-002` (Accessibility by Default).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §3](patterns.md#3-direct-manipulation-and-gesture-response).
  - Related future modules: Components, Responsive (`RSP`).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-016** — Attention motion **must not** be the sole indicator
  of a state, **must** stop rather than repeat indefinitely, **must not**
  steal keyboard focus, and **must** provide a static reduced-motion
  alternative, per [patterns.md §4](patterns.md#4-attention-motion).
  - Lifecycle status: Approved (directly restates the locked
    component-state-clarity rule — "must not rely on color/motion
    alone" — and Accessibility by Default). Provenance: Confirmed.
    Validation status: Not verified.
  - Related principle: `KBDL-PRN-005` (locked identity rules).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §4](patterns.md#4-attention-motion).
  - Related future modules: Components (feedback).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-017** — Ambient and continuous motion **must** be
  non-essential for comprehension, **must** be pausable or avoidable by
  the user, and **must** stop or simplify under reduced-motion
  preference, per
  [patterns.md §5](patterns.md#5-ambient-and-continuous-motion).
  - Lifecycle status: Approved (directly restates the locked Motion
    Purpose rule that continuous motion must be controlled, and the
    already-Approved reduced-motion requirement `KBDL-THM-012a`).
    Provenance: Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-005`; `KBDL-THM-012a`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §5](patterns.md#5-ambient-and-continuous-motion).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-018** — Scroll-linked motion **must not** be required for
  access to essential content, **must not** trap or override normal
  scrolling, and **must** reduce or disable parallax under reduced-motion
  preference, per
  [patterns.md §6](patterns.md#6-scroll-linked-motion).
  - Lifecycle status: Approved (directly restates accessibility's
    requirement that content remain accessible without script/animation,
    and the reduced-motion requirement). Provenance: Confirmed.
    Validation status: Not verified.
  - Related principle: `KBDL-PRN-002`; `KBDL-THM-012a`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §6](patterns.md#6-scroll-linked-motion).
  - Related future modules: Components, Responsive (`RSP`).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-019** — Media motion **must not** autoplay with sound,
  **must** provide a static or textual equivalent for essential
  information, and **must** support pause or stop for significant
  autoplay motion, per [patterns.md §7](patterns.md#7-media-motion).
  - Lifecycle status: Approved (directly restates WCAG 2.2 AA's
    autoplay-with-sound prohibition and pause/stop requirement, already
    adopted under `KBDL-DEC-010`). Provenance: Confirmed. Validation
    status: Not verified.
  - Related principle: `KBDL-DEC-010` (WCAG 2.2 AA baseline).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §7](patterns.md#7-media-motion).
  - Related future modules: Components, Foundations (`FND`, media
    strategy).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-020** — Theme-transition motion **must** use the recommended
  duration and easing classes in
  [patterns.md §8](patterns.md#8-theme-transition-motion) only once
  approved, **must not** reopen any approved KBDL-004 theme mapping, and
  **must** continue to satisfy every KBDL-004 theme-transition
  requirement (`KBDL-THM-012`, `KBDL-THM-012a`).
  - Lifecycle status: Recommended (the exact duration/easing values are
    new; the underlying non-blocking, readable, focus-preserving
    requirements are already `Approved` under `KBDL-THM-012`/`012a` and
    unaffected). Provenance: User-provided. Validation status: Not
    verified.
  - Related principle: `KBDL-THM-012`, `KBDL-THM-012a`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §8](patterns.md#8-theme-transition-motion).
  - Related future modules: None (this is the deferred KBDL-004 item
    now addressed).
  - Validation method: Manual review of the worked example (performed,
    see [patterns.md §8](patterns.md#8-theme-transition-motion));
    project-owner review (not yet performed).

- **KBDL-MOT-021** — Motion **must** resolve to a valid state after
  interruption, cancellation, replacement, or navigation away; interrupted
  exits **must not** leave inaccessible or focusable remnants, per
  [patterns.md §9](patterns.md#9-interruption-reversal-and-recovery).
  - Lifecycle status: Approved (directly restates safety/correctness and
    state-comprehension priorities). Provenance: Confirmed. Validation
    status: Not verified.
  - Related principle: `KBDL-PRN-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §9](patterns.md#9-interruption-reversal-and-recovery).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-022** — Every major motion pattern **must** define a
  full-motion, reduced-motion, and no-motion behavior preserving
  equivalent meaning and functionality, per
  [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity);
  reduced motion **must not** mean reduced functionality.
  - Lifecycle status: Approved (directly restates `KBDL-THM-012a` and
    KBDL's enhanced motion-safety baseline, `KBDL-DEC-010`). Provenance:
    Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-THM-012a`; `KBDL-DEC-010`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity).
  - Related future modules: Accessibility (`A11Y`).
  - Validation method: Manual parity review per pattern (performed, see
    [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity));
    implementation-level review not yet performed.

- **KBDL-MOT-023** — Motion **must not** use hazardous patterns
  (repeated shaking, continuous zoom, simulated camera movement, rapid
  alternating direction, high-frequency flashing, large rapid viewport
  movement, or full-screen brightness changes), per
  [accessibility-performance.md §2](accessibility-performance.md#2-motion-safety).
  - Lifecycle status: Approved (directly restates KBDL's enhanced
    motion-safety requirement, `KBDL-DEC-010`). Provenance: Confirmed.
    Validation status: Not verified.
  - Related principle: `KBDL-DEC-010`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [accessibility-performance.md §2](accessibility-performance.md#2-motion-safety).
  - Related future modules: Accessibility (`A11Y`).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-024** — Motion **must not** block input, and off-screen or
  hidden motion **should** pause where practical, per
  [accessibility-performance.md §3](accessibility-performance.md#3-performance-requirements);
  performance claims **must not** be marked `Verified` without
  implementation evidence.
  - Lifecycle status: Approved (directly restates Performance-Aware
    Enhancement, `KBDL-PRN-003`/§6.9). Provenance: Confirmed. Validation
    status: Not verified.
  - Related principle: `KBDL-PRN-003` (Performance-Aware Enhancement).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [accessibility-performance.md §3](accessibility-performance.md#3-performance-requirements).
  - Related future modules: Components.
  - Validation method: Implementation-level performance measurement (not
    yet performed — no implementation exists).

- **KBDL-MOT-025** — Motion **must** preserve equivalent meaning across
  touch, pointer, keyboard, and screen-reader interaction, per
  [accessibility-performance.md §4](accessibility-performance.md#4-mobile-and-input-method-considerations);
  screen-reader users **must not** depend on visual animation for state
  information.
  - Lifecycle status: Approved (directly restates Accessibility by
    Default). Provenance: Confirmed. Validation status: Not verified.
  - Related principle: `KBDL-PRN-003` (Accessibility by Default).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [accessibility-performance.md §4](accessibility-performance.md#4-mobile-and-input-method-considerations).
  - Related future modules: Responsive (`RSP`), Accessibility (`A11Y`).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-026** — Showcase, Precision, and Flow **must** share one
  motion architecture, adjusting only emphasis per
  [patterns.md §10](patterns.md#10-profile-level-motion-interpretation);
  a profile **must not** define a separate timing or easing architecture
  without an approved exception.
  - Lifecycle status: Approved (directly restates `KBDL-PRN-007`,
    Adaptability Without Fragmentation). Provenance: Confirmed.
    Validation status: Not verified.
  - Related principle: `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §10](patterns.md#10-profile-level-motion-interpretation).
  - Related future modules: Project profiles (`PRO`).
  - Validation method: Manual cross-profile review once the
    project-profiles module is approved.

- **KBDL-MOT-027** — Newly proposed motion defaults (durations, curves,
  distances, scales, stagger, intensity levels, pattern defaults) **must
  not** be marked `Approved` or implemented until the project owner
  approves them via [§10](#10-motion-decision-packet).
  - Lifecycle status: Approved (this governance rule itself directly
    restates [conventions.md §1.1](../conventions.md#11-lifecycle--approval-status)).
    Provenance: Confirmed. Validation status: Not applicable.
  - Related principle: `KBDL-PRN-002`, `KBDL-PRN-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-motion-decision-packet).
  - Related future modules: All later modules.
  - Validation method: Manual review confirming no `Recommended` motion
    value is implemented or marked `Approved` without a decision-register
    entry.

- **KBDL-MOT-028** — Exits **should** use a duration equal to or shorter
  than their paired entrance's duration, per
  [§10.2](#102-recommended-decisions--ready-for-approval) item 6; this is
  new KBDL-005 timing policy, distinct from `KBDL-MOT-012`'s
  already-`Approved` safety core (destructive actions must not rely on
  exit animation as confirmation; removed content must not remain
  focusable), which is unaffected by this requirement's status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable (a timing-relationship recommendation, not
    yet a testable implementation claim).
  - Related principle: `KBDL-MOT-012`, `KBDL-MOT-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [foundations.md §7](foundations.md#7-entrance-and-exit-behavior).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-029** — Attention motion **should** repeat no more than 2–3
  times before holding a static emphasized state, per
  [§10.2](#102-recommended-decisions--ready-for-approval) item 7; this
  exact repetition default is new KBDL-005 policy, distinct from
  `KBDL-MOT-016`'s already-`Approved` core (attention motion must not be
  the sole indicator, must stop rather than repeat indefinitely, and
  must not steal focus), which is unaffected by this requirement's
  status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable.
  - Related principle: `KBDL-MOT-016`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §4](patterns.md#4-attention-motion).
  - Related future modules: Components (feedback).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-030** — The detailed ambient-motion boundaries in
  [patterns.md §5](patterns.md#5-ambient-and-continuous-motion)
  (rare, bounded, pausable, reading-safe) are new KBDL-005 policy,
  distinct from `KBDL-MOT-017`'s already-`Approved` core (ambient motion
  must be non-essential and must honor reduced motion), which is
  unaffected by this requirement's status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-MOT-017`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §5](patterns.md#5-ambient-and-continuous-motion).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-031** — The detailed scroll-linked-motion boundaries in
  [patterns.md §6](patterns.md#6-scroll-linked-motion) (bounded
  parallax, no replay on small scroll changes) are new KBDL-005 policy,
  distinct from `KBDL-MOT-018`'s already-`Approved` core (essential
  content must not depend on scroll-triggered animation), which is
  unaffected by this requirement's status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-MOT-018`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §6](patterns.md#6-scroll-linked-motion).
  - Related future modules: Components, Responsive (`RSP`).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-032** — The detailed per-category reduced-motion
  substitution matrix in
  [accessibility-performance.md §1.4](accessibility-performance.md#14-per-category-parity-matrix)
  is new KBDL-005 documentation, distinct from `KBDL-MOT-022`'s
  already-`Approved` core requirement (every major pattern must define a
  full-motion, reduced-motion, and no-motion behavior preserving
  equivalent meaning), which is unaffected by this requirement's status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable (a documentation-completeness recommendation,
    reviewed conceptually per [motion/validation.md §3](validation.md#3-reduced-motion-matrix-review-performed)).
  - Related principle: `KBDL-MOT-022`; `KBDL-THM-012a`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [accessibility-performance.md §1.4](accessibility-performance.md#14-per-category-parity-matrix).
  - Related future modules: Accessibility (`A11Y`).
  - Validation method: Manual review (performed, see
    [motion/validation.md §3](validation.md#3-reduced-motion-matrix-review-performed));
    project-owner review (not yet performed).

- **KBDL-MOT-033** — The conceptual motion-token naming architecture in
  [timing-easing.md §4](timing-easing.md#4-conceptual-motion-tokens)
  (duration, easing, delay, stagger, distance, scale, opacity, rotation,
  motion level, repetition, sequence, reduced-motion substitution) is
  new KBDL-005 policy; no prior KBDL decision defines motion tokens.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not applicable (a naming architecture, not a testable
    claim).
  - Related principle: `KBDL-MOT-007`, `KBDL-MOT-009`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [timing-easing.md §4](timing-easing.md#4-conceptual-motion-tokens).
  - Related future modules: Components.
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-MOT-034** — The specific per-profile motion-intensity
  adjustments in
  [patterns.md §10](patterns.md#10-profile-level-motion-interpretation)
  (what each profile "may emphasize" and "must preserve") are new
  KBDL-005 policy, distinct from `KBDL-MOT-026`'s already-`Approved` core
  (profiles must share one motion architecture, adjusting only
  emphasis), which is unaffected by this requirement's status.
  - Lifecycle status: Recommended. Provenance: User-provided. Validation
    status: Not verified.
  - Related principle: `KBDL-MOT-026`; `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [patterns.md §10](patterns.md#10-profile-level-motion-interpretation).
  - Related future modules: Project profiles (`PRO`).
  - Validation method: Manual cross-profile review once the
    project-profiles module is approved; project-owner review (not yet
    performed).

## 10. Motion Decision Packet

### 10.1 Already-Approved Motion Architecture (context only)

Not awaiting approval — provided as context. Directly supported by prior
approved KBDL decisions (see [§9](#9-normative-requirements) for exact
requirement wording): motion must serve a documented purpose and must
never be purely decorative (`KBDL-MOT-001`, restating the locked Motion
Purpose rule); motion terminology must be used consistently
(`KBDL-MOT-002`); conflicts between expressive character and usability
resolve via the priority order (`KBDL-MOT-003`); destructive actions
must not rely on exit animation as confirmation (`KBDL-MOT-012`);
loading motion must be truthful and stoppable (`KBDL-MOT-014`); direct
manipulation must support a non-gesture alternative (`KBDL-MOT-015`);
attention motion must not be the sole indicator and must stop
(`KBDL-MOT-016`); ambient motion must remain non-essential and honor
reduced motion (`KBDL-MOT-017`); scroll-linked motion must not gate
essential content (`KBDL-MOT-018`); media motion must not autoplay with
sound (`KBDL-MOT-019`); motion must resolve to a valid state after
interruption (`KBDL-MOT-021`); every pattern needs full/reduced/no-motion
parity (`KBDL-MOT-022`); hazardous motion is prohibited
(`KBDL-MOT-023`); motion must not block input (`KBDL-MOT-024`); motion
must preserve meaning across input methods (`KBDL-MOT-025`); and
profiles must share one motion architecture (`KBDL-MOT-026`).

### 10.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs / limitations | Accessibility impact | Performance impact | UX impact | Profile impact | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Motion hierarchy | Adopt the five-level hierarchy (None/Functional/Supportive/Expressive/Exceptional) in [foundations.md §3](foundations.md#3-motion-hierarchy) (`KBDL-MOT-005`) | Gives every motion decision a bounded emphasis scale tied to review requirements | A three-level scale (rejected — cannot distinguish routine feedback from rare showcase moments) | Exceptional-level use requires per-instance project-owner review, an ongoing process cost | Higher levels require explicit review before shipping, preventing accidental overuse | Not applicable at this level | Provides a shared vocabulary for motion emphasis across teams | Showcase uses Levels 2–4 more; Precision mostly Levels 0–2 | None |
| 2 | Timing architecture and duration classes/values | Adopt the semantic timing classes in [timing-easing.md §1](timing-easing.md#1-timing-architecture) (`KBDL-MOT-007`) and the seven named duration classes and ranges in [timing-easing.md §2](timing-easing.md#2-duration-recommendations) (`KBDL-MOT-008`) together, as one timing system | Named classes tied to interaction category keep timing consistent without hardcoding a single value per component | Per-component duration values (rejected — fragments consistency, harder to review) | Ranges require a project to pick a specific value within range; guidance for choosing is provided but not exhaustive | Longer classes are excluded from safety-critical acknowledgment paths | Shorter classes bound worst-case input-to-feedback latency | Consistent timing reinforces "one system" recognizability | Showcase may use Deliberate/Extended more; Precision favors Immediate/Fast | `KBDL-MOT-007`, `KBDL-MOT-008` |
| 3 | Easing categories and exact curves | Adopt the semantic categories and cubic-bezier-equivalent curves in [timing-easing.md §3](timing-easing.md#3-easing-architecture) (`KBDL-MOT-009`) | Named, framework-neutral curves give motion a consistent "material" feel without committing to an animation library | Linear-only easing (rejected — reads as mechanical, contradicts Digital Luxury) | Every curve must be re-evaluated for interruption/reversal per use; this review has been done conceptually, not against a live implementation | Reduced-motion bypasses easing entirely (instant change), unaffected | No curve requires physics simulation; all are closed-form | Establishes a recognizable, consistent motion "voice" | All profiles share the same easing set; only which curve is used varies by category | `KBDL-MOT-009` |
| 4 | Movement-distance and scale ranges | Adopt the bounded ranges in [foundations.md §6](foundations.md#6-spatial-movement) (`KBDL-MOT-010`) | Prevents unbounded or inconsistent movement/scale choices across implementations | Unbounded, per-instance movement (rejected — risks disorienting, inconsistent motion) | Ranges are qualitative bounds (small/moderate/large), not exact pixel values, since exact values depend on component size (deferred to Components) | Large movement is restricted to rare, reviewed moments | Larger movement/scale costs more to composite; ranges bias toward cheaper defaults | Predictable movement preserves the user's spatial mental model | Showcase may use the upper bound rarely; Precision/Flow stay low | None |
| 5 | Stagger and overlap guidance | Adopt the guidance in [foundations.md §5](foundations.md#5-choreography-and-sequencing) (`KBDL-MOT-011`) | Prevents long lists or groups from accumulating excessive total animation time | No stagger (rejected — flattens hierarchy in multi-element changes); unbounded stagger (rejected — creates excessive cumulative delay) | Guidance is qualitative (cap total sequence time), not an exact per-item millisecond value, since item count varies by context | Cumulative-delay cap protects users who rely on completion before acting | Bounded stagger keeps total animated-element count and time low | Reinforces hierarchy without feeling sluggish for larger groups | Showcase may stagger more items in rare moments; Precision limits stagger to small counts | `KBDL-MOT-011` |
| 6 | Entrance-versus-exit relationship | Adopt the rule that exits are equal to or faster than entrances, in [foundations.md §7](foundations.md#7-entrance-and-exit-behavior) (`KBDL-MOT-028`) | Faster removal keeps the interface feeling responsive and avoids blocking subsequent actions | Symmetrical entrance/exit timing (rejected — exits feel sluggish relative to the new content already needing attention) | None identified | Faster exits reduce the risk of an exiting element remaining focusable longer than necessary | Faster exits reduce total animated time per interaction | Matches common platform conventions users already expect | Applies identically across profiles | `KBDL-MOT-008`, `KBDL-MOT-012` |
| 7 | Attention repetition limits | Adopt a bounded repetition count (attention motion plays a small, fixed number of times, then stops and holds a static state) in [patterns.md §4](patterns.md#4-attention-motion) (`KBDL-MOT-029`) | Prevents indefinite, distracting repetition while still drawing initial attention | Unlimited repetition until dismissed (rejected — violates motion-safety and distraction concerns) | A bounded count may under-emphasize an attention cue in a very busy interface; static fallback (color/icon/label) compensates | Bounded repetition directly supports the motion-safety prohibition on continuous pulsing near text | Bounded repetition caps ongoing compositing cost | Attention is drawn without becoming an ongoing distraction | Applies identically across profiles | `KBDL-MOT-016` |
| 8 | Ambient-motion boundaries | Adopt the boundaries in [patterns.md §5](patterns.md#5-ambient-and-continuous-motion) (rare, bounded, pausable, reading-safe) (`KBDL-MOT-030`) | Keeps ambient motion decorative and non-essential without prohibiting it outright | No ambient motion permitted (rejected — overly restrictive for Showcase's editorial character) | Requires a documented pause/avoidance mechanism, an implementation cost | Reduced motion removes ambient motion entirely; full-motion mode still avoids reading-content proximity | Ambient motion must support a static fallback for constrained devices | Preserves Showcase's ability to feel alive without becoming distracting | Showcase uses ambient motion more; Precision/Flow use it rarely or not at all | `KBDL-MOT-017` |
| 9 | Scroll-linked-motion boundaries | Adopt the boundaries in [patterns.md §6](patterns.md#6-scroll-linked-motion) (bounded parallax, no essential-content gating, reduced-motion disables parallax) (`KBDL-MOT-031`) | Allows expressive scroll storytelling in Showcase while protecting accessibility and normal scroll behavior everywhere | Prohibiting scroll-linked motion entirely (rejected — overly restrictive) | Large parallax remains excluded by default; a specific exception would need its own review | Essential-content-must-not-depend-on-scroll-animation rule is unaffected regardless of approval | Scroll-linked motion must not repeatedly replay on small scroll changes, bounding cost | Supports Showcase storytelling without breaking Precision/Flow scanning | Showcase primary use; Precision/Flow rare or none | `KBDL-MOT-018` |
| 10 | Theme-transition duration and easing | Adopt a short, non-blocking duration/easing pairing from the Standard timing and easing classes for the KBDL-004 theme-transition rules, per [patterns.md §8](patterns.md#8-theme-transition-motion) (`KBDL-MOT-020`) | Resolves the exact timing KBDL-004 deferred, using values already proposed here rather than inventing a separate scheme | A distinct, theme-specific timing scale (rejected — fragments the timing architecture for no added benefit) | Must remain short enough that no intermediate frame drops below the applicable contrast threshold; verified conceptually against the worked example, not a live implementation | Reduced motion replaces the transition with an instant switch, per already-Approved `KBDL-THM-012a` | A short, simple crossfade is inexpensive to composite | Theme switching feels deliberate without feeling slow | Applies identically across profiles (theme architecture is shared, per `KBDL-THM-006`) | `KBDL-MOT-007`, `KBDL-MOT-009`, `KBDL-THM-012` |
| 11 | Reduced-motion substitution matrix | Adopt the full-motion/reduced-motion/no-motion matrix in [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity) (`KBDL-MOT-032`) | Makes reduced-motion behavior auditable per pattern rather than left to individual interpretation | A single global "disable everything" reduced-motion rule (rejected — removes necessary feedback along with decoration, harming comprehension) | Requires each new pattern to document its own row in the matrix going forward, an ongoing documentation cost | This is itself the accessibility deliverable — it operationalizes `KBDL-THM-012a` per pattern | Reduced/no-motion variants are cheaper to render, a secondary performance benefit | Preserves functionality for users who need reduced motion, without a degraded experience | Applies identically across profiles | `KBDL-MOT-022`, `KBDL-THM-012a` |
| 12 | Motion-token naming architecture | Adopt the conceptual token categories in [timing-easing.md §4](timing-easing.md#4-conceptual-motion-tokens) (duration, easing, delay, stagger, distance, scale, opacity, rotation, motion level, repetition, sequence, reduced-motion substitution) (`KBDL-MOT-033`) | Gives future implementation work a semantic naming target without committing to CSS, JSON, or any specific format | Component-scoped ad hoc naming per implementation (rejected — fragments consistency, harder to review across projects) | Exact token-file format and technology remain deferred; this is naming architecture only | Not applicable at this conceptual level | Not applicable at this conceptual level | Establishes a shared vocabulary implementers can reference consistently | Applies identically across profiles | None |
| 13 | Profile-level motion-intensity adjustments | Adopt the per-profile emphasis guidance in [patterns.md §10](patterns.md#10-profile-level-motion-interpretation) (`KBDL-MOT-034`) | Lets Showcase, Precision, and Flow express their documented character (per [principles.md §9](../principles.md#9-profile-level-interpretation)) through motion without fragmenting the architecture | Identical motion intensity across all profiles (rejected — contradicts the already-approved profile-emphasis model) | Requires per-profile review when a new pattern is added, to confirm the shared-architecture constraint holds | Reduced-motion and motion-safety rules apply identically regardless of profile, unaffected | Precision/Flow's lower-intensity defaults reduce average rendering cost | Reinforces each profile's documented character (editorial, efficient, guided) | Directly defines the adjustment itself | `KBDL-MOT-026`, `KBDL-PRN-007` |
| 14 | Multi-factor motion-intensity model | Adopt the intensity model in [foundations.md §4](foundations.md#4-motion-intensity) (`KBDL-MOT-006`), which assesses intensity through duration, distance, scale, rotation, opacity change, blur/depth, number of moving elements, stagger, repetition, screen coverage, input independence, contrast change, and directional complexity — duration alone is insufficient | Prevents an intensity judgment from being made on duration alone, which can misclassify a short-duration but large-distance/high-repetition motion as low intensity | A duration-only intensity heuristic (rejected — demonstrably misclassifies motion, e.g. a brief but large-distance, high-repetition change) | The model is qualitative (low/moderate/high per factor), not a scored formula; assessing cumulative intensity across concurrent elements still requires judgment, per [foundations.md §4](foundations.md#4-motion-intensity) | Ties directly to the motion-hierarchy review triggers (item 1), preventing high-intensity motion from shipping unreviewed | No additional runtime cost — this is a design-time assessment method, not a runtime calculation | Gives designers and reviewers a consistent, repeatable way to judge "how much" a motion pattern communicates | Showcase tolerates higher aggregate intensity more often; Precision keeps it low by default; Flow uses a middle range | `KBDL-MOT-005` |
| 15 | Navigation-motion architecture | Adopt the navigation and spatial-continuity guidance in [patterns.md §1](patterns.md#1-navigation-and-spatial-continuity) (`KBDL-MOT-013`) — motion reinforces information structure, forward/back directional consistency, spatial continuity, immediate access to required content, focus continuity, predictable browser navigation, reduced-motion substitution, and exceptional-only treatment of full-page cinematic transitions | Gives route/step/panel/modal transitions one consistent, accessible architecture instead of ad hoc per-view treatment | No navigation-motion guidance at all (rejected — leaves directional consistency and focus continuity unspecified, risking disorientation) | Full-page cinematic transitions remain restricted to Level 4 (Exceptional) per the motion hierarchy (item 1), an ongoing review cost for Showcase | Browser back/forward must remain predictable and unhijacked; focus location must remain understandable after every navigation | New navigation cancels an in-progress transition rather than queuing it, bounding worst-case transition time | Preserves the user's spatial mental model across route/step/panel changes | Showcase may use directional/shared-element transitions more; Precision favors instant or very short crossfade | `KBDL-MOT-005`, `KBDL-MOT-007` |

### 10.2.1 Recommended-Requirement Coverage

Every `Recommended` `KBDL-MOT-###` requirement maps to exactly one
decision above:

| Requirement | Approval decision |
| --- | --- |
| `KBDL-MOT-005` | Item 1 |
| `KBDL-MOT-006` | Item 14 |
| `KBDL-MOT-007` | Item 2 |
| `KBDL-MOT-008` | Item 2 |
| `KBDL-MOT-009` | Item 3 |
| `KBDL-MOT-010` | Item 4 |
| `KBDL-MOT-011` | Item 5 |
| `KBDL-MOT-013` | Item 15 |
| `KBDL-MOT-020` | Item 10 |
| `KBDL-MOT-028` | Item 6 |
| `KBDL-MOT-029` | Item 7 |
| `KBDL-MOT-030` | Item 8 |
| `KBDL-MOT-031` | Item 9 |
| `KBDL-MOT-032` | Item 11 |
| `KBDL-MOT-033` | Item 12 |
| `KBDL-MOT-034` | Item 13 |

Sixteen `Recommended` requirements, fifteen decisions (item 2 covers two
requirements, `KBDL-MOT-007` and `KBDL-MOT-008`, as one timing system).
This table records mapping only; it does not itself change any
lifecycle or validation status.

### 10.3 Unresolved or Not Approval-Ready

- **Exact pixel/percentage movement and scale values** — [§10.2](#102-recommended-decisions--ready-for-approval)
  item 4 sets qualitative ranges only; exact per-component values depend
  on component size and are deferred to the Components module (`CMP`).
- **Exact stagger interval (milliseconds) and maximum concurrent
  animated-element count** — qualitative caps only are proposed; exact
  numeric limits depend on implementation and device-performance
  measurement not yet available.
- **Device-performance detection strategy** — how an implementation
  would detect a "lower-performance device" to apply a simplified
  fallback is an implementation-layer decision, out of scope for this
  design-language specification.
- **Animation library or rendering-technology selection** —
  implementation-layer, out of scope.
- **Exact motion-token file format (CSS custom properties, JSON, or
  other)** — implementation-layer, explicitly out of scope, consistent
  with the KBDL-004 precedent.
- **Component-specific animation specifications** (e.g., a specific
  button's press animation) — deferred to the Components module (`CMP`).
- **Browser-support policy for motion features** — implementation-layer,
  out of scope.
- **Scroll-threshold exact values** — qualitative review criteria are
  proposed in [patterns.md §6](patterns.md#6-scroll-linked-motion);
  exact thresholds depend on content and viewport and are left to
  per-implementation review.

**Exact scope of a future approval:** an `APPROVE` response to
[§10.2](#102-recommended-decisions--ready-for-approval) would authorize
exactly items 1–15 above as `Approved` — the motion hierarchy, the
timing architecture and duration classes/values, easing categories/
curves, movement-distance and scale ranges, stagger/overlap guidance,
the entrance-versus-exit rule, attention-repetition limits,
ambient-motion boundaries, scroll-linked-motion boundaries,
theme-transition duration/easing, the reduced-motion substitution
matrix, the motion-token naming architecture, profile-level intensity
adjustments, the multi-factor motion-intensity model, and the
navigation-motion architecture. It would **not** approve any
[§10.3](#103-unresolved-or-not-approval-ready) item, any excluded
KBDL-004 theme item (Accent-surface/Scrim/Selection-background opacity,
translucent variants, and the other exclusions listed in
[§1](#1-repository-and-roadmap-context)), or any KBDL-006-or-later
content. It would not itself constitute validation of any item — see
[validation.md](validation.md).

## 11. Traceability

See [traceability-matrix.md](../traceability-matrix.md) for how each
`KBDL-MOT-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](../decision-register.md) for any decision recorded
as part of this module.
