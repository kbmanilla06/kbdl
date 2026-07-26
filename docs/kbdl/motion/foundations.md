# KBDL Motion — Foundations

Lifecycle status: `Approved` for the structural requirement that every
category below document purpose, intensity, transformations,
interruption, reduced-motion, performance, and profile guidance
(`KBDL-MOT-004`); `Recommended` for the specific hierarchy levels,
intensity model, spatial-movement ranges, and choreography guidance
introduced as new KBDL-005 policy — see
[motion/README.md §9](README.md#9-normative-requirements) for exact
per-requirement status.

Return to the [motion index](README.md) · [specification index](../README.md).

## 1. Motion Purposes

Every KBDL motion pattern must serve at least one purpose below
(`KBDL-MOT-001`). Motion without a documented purpose is decorative and
must remain removable without functional loss.

| Purpose | When motion is justified | When motion is unnecessary | Appropriate intensity | Reduced-motion equivalent | Failure risk | Validation question |
| --- | --- | --- | --- | --- | --- | --- |
| Acknowledge input | Any user-initiated action (press, toggle, submit) | Never — some acknowledgment is always required, though it may be non-animated | Functional | Instant visual state change | Input feels ignored or delayed | Does feedback begin immediately on input? |
| Confirm completion | An operation finishes and the result changes visible state | The result is already obvious without motion (e.g., navigation already occurred) | Functional to Supportive | Static success state, no animated flourish | User cannot tell whether the action finished | Would the user know the action completed without watching the animation? |
| Communicate state change | A component moves between two meaningfully different states | The states look identical, or the change is announced another way (e.g., a full navigation) | Supportive | Instant or short crossfade preserving the same before/after cue | User loses track of what changed | Can the user identify the new state without having watched the transition? |
| Preserve spatial continuity | Navigation or reorganization where the user's mental map of "where things are" matters | A full context switch where no prior spatial relationship exists to preserve | Supportive | Instant relocation, preserving scroll/focus position | User loses their place after navigating | Does the user know where the thing they were looking at went? |
| Explain hierarchy | Multiple elements change together and their relative importance matters | A single, isolated element changes with nothing else to relate it to | Supportive | Simultaneous instant change, no sequencing | Secondary elements appear to compete with primary ones | Is it clear which change mattered most, with or without motion? |
| Reveal or conceal content | Expand/collapse, progressive disclosure, or reveal-on-demand | Content is always visible regardless of state | Functional to Supportive | Instant show/hide | User cannot tell where revealed content came from | Is the source and destination of revealed content clear without motion? |
| Communicate progress | An operation takes perceptible time and partial completion is knowable | The operation is effectively instantaneous | Functional | Static or textual progress indication | User believes the system is frozen or unresponsive | Does the user have some sense of how much longer to wait? |
| Communicate interruption | An in-progress operation or motion is stopped before completion | Nothing was in progress to interrupt | Functional | Instant resolution to a valid state | The interface appears to freeze mid-change | Does the interface reach a coherent state immediately after interruption? |
| Communicate error or recovery | A validation failure, system error, or successful recovery occurs | The error is already obvious from static text/iconography alone | Functional to Supportive | Static emphasis (color, icon, label), no shake or repeated motion | The user cannot tell an error occurred, or motion overstates it | Does the user understand what went wrong and what to do next, without relying on the motion itself? |
| Direct attention | A relevant, time-sensitive change occurs that the user has not yet seen | The user is already looking at, or has just caused, the change | Functional to Supportive | Static emphasis, bounded in time | Attention motion competes with or obscures active focus | Does directing attention here serve the user's actual task right now? |
| Establish relationship | Motion shows that two elements are connected (e.g., a trigger and its result) | The relationship is already obvious from layout or labeling | Supportive | Static visual grouping (proximity, shared container) | The user cannot tell which elements are related | Would the relationship be clear from layout alone, without motion? |
| Support orientation | The user needs to understand where they are within a larger structure (steps, hierarchy, navigation) | Orientation is already conveyed by persistent static UI (breadcrumbs, step indicators) | Functional to Supportive | Static indicator, no animated transition required | The user loses track of their position in a flow | Is there a static way to answer "where am I" without the motion? |
| Express brand character | A bounded, intentional moment reinforcing KBDL's identity (see [motion/README.md §3](README.md#3-motion-identity)) | Any routine, repeated interaction | Expressive to Exceptional (rare) | Reduced to a short crossfade or instant change | Brand expression is applied to frequent interactions, adding fatigue or delay | Would removing this motion make the moment forgettable, and is that acceptable here? |
| Provide delight without blocking | A bounded, optional moment that adds warmth without gating any task | Any required or frequently repeated interaction | Supportive to Expressive (rare) | Removed entirely; no functional loss | Delight motion delays or blocks the user's actual goal | Can the user complete their task exactly as fast with this motion removed? |

## 2. Motion Categories

Every category documents purpose, default intensity, permitted and
prohibited transformations, interruption behavior, reduced-motion
response, performance considerations, profile-level variation, and
related future component modules (`KBDL-MOT-004`).

### 2.1 Immediate feedback

- **Purpose:** Acknowledge input (press, selection, toggle, drag
  response).
- **Default intensity:** Functional.
- **Permitted:** Small opacity/scale change, color-state change.
- **Prohibited:** Large translation, rotation, or anything delaying
  visible acknowledgment.
- **Interruption:** Always interruptible by the next input; never
  queues.
- **Reduced motion:** Instant state change; the state itself (not the
  motion) is the feedback.
- **Performance:** Must never wait on a network or async operation to
  begin.
- **Profile variation:** Intensity is nearly identical across profiles;
  this category is the least profile-differentiated.
- **Related future modules:** Components (`CMP`, action/form controls).

### 2.2 State transition

- **Purpose:** Communicate state change (open, close, expand, collapse,
  enable, disable).
- **Default intensity:** Functional to Supportive.
- **Permitted:** Opacity, scale, height/clip change, color-state change.
- **Prohibited:** Full-screen movement for a small, local state change.
- **Interruption:** Must be interruptible by an opposing state request
  (e.g., collapsing while still expanding).
- **Reduced motion:** Instant state swap.
- **Performance:** Must not trigger unnecessary layout recalculation
  across unrelated elements.
- **Profile variation:** Precision favors the low end (Functional);
  Showcase may use Supportive intensity for editorial state changes.
- **Related future modules:** Components (all categories).

### 2.3 Spatial navigation

- **Purpose:** Preserve spatial continuity during route, pane, step, or
  hierarchy changes.
- **Default intensity:** Supportive.
- **Permitted:** Directional translation, crossfade, shared-axis
  transition.
- **Prohibited:** Large off-screen travel that implies a false
  hierarchy; motion that delays access to the destination's content.
- **Interruption:** A second navigation request must cancel and resolve
  to the newest destination, not queue both.
- **Reduced motion:** Instant swap or short crossfade; destination
  content available immediately either way.
- **Performance:** Must not block input during the transition.
- **Profile variation:** Showcase may use directional/shared-element
  transitions more; Precision favors instant or very short crossfade for
  speed.
- **Related future modules:** Components (navigation), Responsive
  (`RSP`).

### 2.4 Content change

- **Purpose:** Communicate insert, remove, reorder, filter, sort, or
  refresh.
- **Default intensity:** Functional to Supportive.
- **Permitted:** Opacity/height change for insert/remove; position
  interpolation for reorder (bounded count).
- **Prohibited:** Animating every item in a long list individually by
  default; movement that breaks item identity during reorder.
- **Interruption:** A new content update must resolve any in-progress
  change to a valid final state before applying.
- **Reduced motion:** Instant insert/remove/reorder.
- **Performance:** Must scale to large lists without degrading
  responsiveness (batch, don't animate per-item at scale).
- **Profile variation:** Precision keeps this category especially
  restrained given data density; Showcase may allow more visible
  reordering feedback for smaller collections.
- **Related future modules:** Components (data display), Responsive.

### 2.5 System feedback

- **Purpose:** Communicate loading, progress, success, warning, failure,
  recovery.
- **Default intensity:** Functional.
- **Permitted:** Determinate progress fill, low-intensity indeterminate
  indication, static-to-motion state swap on completion.
- **Prohibited:** Indeterminate motion continuing after the operation
  actually finishes; motion implying progress that is not real.
- **Interruption:** Cancelling the underlying operation must stop the
  motion immediately, not let it visually continue.
- **Reduced motion:** Static or textual progress indication.
- **Performance:** Must not compete for main-thread resources with the
  operation it represents.
- **Profile variation:** Consistent across profiles; this is a
  Technical Utility category, not an expressive one.
- **Related future modules:** Components (feedback, system-state).

### 2.6 Attention

- **Purpose:** Direct attention to notification, changed value,
  validation issue, or incoming content.
- **Default intensity:** Functional to Supportive.
- **Permitted:** Bounded-repetition emphasis (color/scale pulse), static
  badge/indicator.
- **Prohibited:** Indefinite repetition, screen-wide flashing, motion
  that moves or steals keyboard focus.
- **Interruption:** User interaction with the attended element stops
  the attention motion immediately.
- **Reduced motion:** Static emphasis (color, icon, label) only.
- **Performance:** Must not run continuously once the bounded repetition
  count is reached.
- **Profile variation:** Consistent across profiles; attention motion is
  a Technical Utility/accessibility category.
- **Related future modules:** Components (feedback).

### 2.7 Direct manipulation

- **Purpose:** Respond continuously to dragging, swiping, resizing,
  scrubbing.
- **Default intensity:** Functional (tracks input 1:1) with a Supportive
  settle on release.
- **Permitted:** Position/size following input directly; a brief,
  bounded settle animation on release.
- **Prohibited:** Unbounded overshoot; motion that lags noticeably
  behind input.
- **Interruption:** Must support cancel-and-return-to-origin.
- **Reduced motion:** Direct tracking is preserved (it is required
  feedback, not decoration); only the release "settle" flourish is
  simplified.
- **Performance:** Must track input at the display's native responsive
  rate; must not introduce input lag.
- **Profile variation:** Consistent across profiles; this category
  serves usability directly.
- **Related future modules:** Components, Responsive (touch/pointer).

### 2.8 Media

- **Purpose:** Present video, animated illustration, or rich portfolio
  media.
- **Default intensity:** Supportive to Expressive (Showcase); Functional
  to Supportive elsewhere.
- **Permitted:** User-initiated playback, bounded autoplay (muted, with
  pause/stop) for decorative media.
- **Prohibited:** Autoplay with sound; autoplay that cannot be paused or
  stopped when significant.
- **Interruption:** Must pause cleanly; must not resume unexpectedly
  after navigation away and back.
- **Reduced motion:** Non-essential autoplay motion is suppressed where
  feasible; essential media remains user-controlled.
- **Performance:** Must degrade to a static poster frame on constrained
  devices.
- **Profile variation:** Showcase uses this category most prominently;
  Precision keeps media subordinate to tasks; Flow uses media to support
  comprehension and trust.
- **Related future modules:** Foundations (`FND`, media strategy),
  Components.

### 2.9 Ambient

- **Purpose:** Provide low-priority, non-essential visual life
  (decorative background movement, slow gradients, animated
  illustration loops).
- **Default intensity:** Functional to Supportive; never Expressive.
- **Permitted:** Slow, low-contrast, bounded-area movement.
- **Prohibited:** Movement near sustained reading content; large-area or
  high-contrast ambient motion; motion the user cannot pause or avoid.
- **Interruption:** Must pause when the user is reading nearby content,
  and always under reduced motion.
- **Reduced motion:** Removed or reduced to a static frame.
- **Performance:** Must support a static fallback on constrained
  devices.
- **Profile variation:** Showcase uses ambient motion exceptionally;
  Precision essentially never; Flow conservatively.
- **Related future modules:** None (conceptual only; no implementation
  introduced here).

### 2.10 Theme transition

- **Purpose:** Present the approved conceptual KBDL-004 theme-switch
  behavior with concrete, non-blocking timing.
- **Default intensity:** Functional.
- **Permitted:** Short color crossfade on surfaces, borders, and text.
- **Prohibited:** Anything that delays interaction, flashes a large
  high-contrast region, or drops below the applicable contrast threshold
  mid-transition.
- **Interruption:** A rapid repeated toggle must resolve to the latest
  requested theme, not queue transitions.
- **Reduced motion:** Instant switch (already `Approved`,
  `KBDL-THM-012a`).
- **Performance:** Must not block input during the transition.
- **Profile variation:** Identical across profiles — theme architecture
  is shared (`KBDL-THM-006`).
- **Related future modules:** None (this module supplies what KBDL-004
  deferred).

## 3. Motion Hierarchy

Governs how much visual emphasis a motion pattern may receive
(`KBDL-MOT-005`).

| Level | Name | Purpose | Max concurrency | Typical transformations | Suitable contexts | Profile applicability | Reduced-motion equivalent | Required review | Project-owner approval needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | None | Static or instant change | Unlimited | None | Any context where motion adds no value | All | Same (already static) | None | No |
| 1 | Functional | Minimal motion required for feedback or state comprehension | High (routine, frequent) | Opacity/color/small-scale change | Buttons, toggles, form fields, loading indicators | All | Instant state change | Design review | No |
| 2 | Supportive | Moderate motion preserving continuity and hierarchy | Moderate | Translation, crossfade, height/clip | Navigation, expand/collapse, content updates | All | Instant or short crossfade | Design review | No |
| 3 | Expressive | Stronger but bounded motion supporting identity or a significant moment | Low (one primary sequence at a time) | Choreographed multi-element sequences, larger movement within bounds | Entrance moments, editorial reveals, onboarding | Mostly Showcase, occasionally Flow | Simplified to Supportive or instant | Design review + motion-consistency check | Recommended for review |
| 4 | Exceptional | Rare, explicitly justified motion for major Showcase or campaign moments | Very low (isolated, one-off) | Any transformation within motion-safety bounds | Major Showcase landing or campaign moments only | Showcase only | Instant or simplified crossfade | Design review + project-owner review | Yes |

## 4. Motion Intensity

Intensity is a composite of the factors below, never duration alone
(`KBDL-MOT-006`):

- **Duration** — how long the motion runs.
- **Distance** — how far an element travels.
- **Scale change** — how much an element grows or shrinks.
- **Rotation** — degree of rotational change.
- **Opacity change** — how much visibility changes.
- **Blur or depth change** — how much focus/elevation changes.
- **Number of moving elements** — how many elements animate together.
- **Stagger** — how spread out multiple elements' timing is.
- **Repetition** — how many times a motion repeats.
- **Screen coverage** — what proportion of the viewport is affected.
- **Input independence** — whether motion continues without further
  user input (ambient/continuous motion scores higher here regardless of
  its individual duration).
- **Contrast change** — how much the motion changes perceptual contrast
  mid-transition.
- **Directional complexity** — how many simultaneous directions of
  movement are present.

**Assessing intensity:** rate each factor qualitatively (low/moderate/
high); overall intensity is the highest-scoring factor, not an average —
a short-duration but large-distance, high-repetition motion is high
intensity despite its brief duration.

**Cumulative intensity:** several individually low-intensity motions
occurring simultaneously (e.g., five small items each fading and
scaling at once) can combine into a high-intensity experience; assess
concurrent motion as a group, not only per-element.

**Maximum recommended simultaneous emphasis:** no more than one
Expressive-or-higher motion should play at a time; Functional and
Supportive motion may overlap it only if serving a different, subordinate
purpose (e.g., a loading indicator continuing during an entrance
sequence).

**Profile adjustment:** Showcase tolerates higher intensity more often;
Precision keeps intensity low by default; Flow uses a middle range,
favoring reassurance over impact.

**Mobile adjustment:** reduce distance, scale, and screen coverage on
small viewports, where large movement is proportionally more disruptive.

**Reduced-motion adjustment:** reduced motion removes or minimizes every
factor above except what is required for state comprehension (see
[accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity)).

**Review trigger:** any motion reaching Level 3 (Expressive) or higher
on the hierarchy, or scoring high on three or more intensity factors
simultaneously, requires design review before use.

## 5. Choreography and Sequencing

Choreography governs timing relationships among multiple changing
elements (`KBDL-MOT-011`).

- **Parent-child sequencing** — a container's own transition leads; its
  contents follow, never the reverse.
- **Sibling sequencing** — related siblings change together unless a
  clear priority order exists between them.
- **Stagger** — a small, controlled offset applied between similar
  sibling elements to reinforce grouping, bounded so total sequence time
  stays short.
- **Overlap** — a following element may begin before a leading element
  fully completes, when their purposes do not conflict (e.g., new
  content fading in slightly before old content finishes fading out).
- **Lead and follow** — the primary state change leads; secondary
  decoration follows, never the reverse.
- **Shared-axis transitions** — related views transition along a
  consistent axis (e.g., forward navigation moves one direction,
  backward the other).
- **Crossfade** — simultaneous opacity exchange, used when no spatial
  relationship needs to be preserved.
- **Enter-before-exit / exit-before-enter** — chosen based on whether
  layout space must be reserved (enter-before-exit avoids a layout gap;
  exit-before-enter avoids visual crowding).
- **Simultaneous transition** — used only when elements are unrelated
  and do not compete for attention.
- **Progressive disclosure** — sequenced reveal of related content,
  bounded so the user is not kept waiting for later items to matter.
- **Batch content updates** — many simultaneous data changes are
  presented as one coherent update, not many competing individual
  animations.

**Requirements:**

- Sequence must reflect hierarchy — primary state change leads secondary
  decoration.
- Critical information must not wait behind ornamental motion.
- Stagger must not create excessive cumulative delay across a sequence.
- Long lists must not animate every item individually by default; batch
  or skip animation past a reasonable count.
- Reordering must preserve item identity (the same logical item is
  never replaced by a different one mid-animation).
- Content changes must remain understandable when motion is entirely
  absent.
- Interrupted sequences must resolve to a valid, complete state, never a
  partial or inconsistent one.

## 6. Spatial Movement

KBDL motion uses translation, scale, rotation, opacity, clipping/reveal,
shape transition, elevation change, blur, perspective, and parallax,
bounded by the constraints below (`KBDL-MOT-010`):

- Movement direction must correspond to spatial or structural meaning
  (e.g., forward navigation moves one direction consistently).
- Large movement must be rare — reserved for Expressive/Exceptional
  hierarchy levels.
- Off-screen travel must not imply a false information hierarchy (an
  element leaving the screen must not seem more or less important than
  its actual role).
- Scale must not make controls feel unstable — avoid scale changes large
  enough to make a target hard to acquire mid-transition.
- Rotation must not be used for ordinary state change without clear
  meaning (e.g., a chevron rotating to indicate expand/collapse is
  meaningful; rotating a card for no reason is not).
- Opacity-only transitions must not hide state continuity when position
  also matters — pair opacity with position change when both are part of
  the meaning.
- Blur must not be required for comprehension — any blur-based depth
  effect must have a non-blurred equivalent.
- Perspective effects must not interfere with reading.
- Parallax must be optional and must reduce or be removed under
  reduced-motion preference.
- Depth changes must preserve the approved elevation hierarchy from
  [foundations/shape-depth.md](../foundations/shape-depth.md).

**Recommended ranges (qualitative, exact values remain `Recommended`
pending [motion/README.md §10](README.md#10-motion-decision-packet)):**
small movement/scale for Functional and Supportive levels; moderate
movement/scale reserved for Expressive; large movement/scale reserved
for Exceptional and used rarely. Exact pixel or percentage values are
deferred to the Components module, since they depend on component size.

## 7. Entrance and Exit Behavior

- **Entrance motion is useful** when introducing new content whose
  origin or relationship to existing content benefits from being shown.
- **New content should appear immediately** when its origin is already
  obvious (e.g., typed text appearing in a field) or when speed matters
  more than framing.
- **Exit motion is useful** when removal benefits from being
  acknowledged (e.g., a dismissed notification).
- **Removal should be immediate** when speed matters more than
  framing, or when exit motion would delay a subsequent required action.
- **Directional relationships** — an entrance's direction should be the
  logical reverse of its exit's, preserving a coherent mental model.
- **Scale relationships** — entering content may scale up slightly from
  a smaller state; exiting content may scale down, never the reverse of
  what would feel like "arriving" versus "leaving."
- **Opacity behavior** — entrances typically fade in; exits typically
  fade out; both may combine with position or scale.
- **Focus handling** — new content must not steal focus solely because
  it animated in; focus moves only per standard interaction rules.
- **Layout stability** — entrance and exit must not cause unrelated
  content to jump or reflow unexpectedly.
- **Interrupted entrance** — must resolve to the fully-entered state
  when interrupted by continued relevance, or reverse cleanly if the
  triggering condition is cancelled.
- **Interrupted exit** — must resolve to fully removed, not a partial,
  lingering state.
- **Reversal** — an in-progress exit may reverse into an entrance (and
  vice versa) from its current visual position, not by restarting.

**Requirements (`KBDL-MOT-012`):**

- Exits should usually be equal to or faster than entrances.
- Destructive or safety-critical actions must not rely on exit animation
  as confirmation — the action's real effect must be confirmed some
  other way.
- Removed content must not remain focusable.
- New content must not steal focus solely because it animated.
- Reduced-motion behavior must preserve arrival and departure meaning
  even when instant.

## 8. State-Change Motion

Conceptual guidance only — no component variants are defined here (that
belongs to the Components module).

| State family | Required feedback | Motion purpose | Suitable intensity | Interruption behavior | Reduced-motion equivalent | Prohibited behavior | Validation question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Selected / unselected | Visible state indicator change | Communicate state change | Functional | Instantly re-triggerable | Instant indicator swap | Relying on color alone | Is the selection state clear without color? |
| Expanded / collapsed | Visible content reveal/conceal | Reveal or conceal content | Functional to Supportive | Reversible mid-animation | Instant show/hide | Losing scroll position on collapse | Does collapsing preserve the user's place in the surrounding content? |
| Enabled / disabled | Visible affordance change | Communicate state change | Functional | Not interruptible mid-toggle (instant) | Instant | Making disabled state visually ambiguous with enabled | Can a user tell at a glance whether a control is usable? |
| Loading / loaded | Visible progress-to-content transition | Communicate progress, confirm completion | Functional | Cancellable | Static "loading" text/indicator to static content | Content popping in with no acknowledgment of the wait | Does the user know when loading finished? |
| Empty / populated | Visible placeholder-to-content transition | Communicate state change | Functional to Supportive | Not typically interrupted | Instant swap | Empty state that looks like an error | Is "nothing here yet" distinguishable from "something went wrong"? |
| Valid / invalid | Visible validation feedback | Communicate error or recovery | Functional to Supportive | Re-triggerable on each input | Static emphasis, no shake | Repeated shake/flash motion | Does the user understand what is invalid without relying on motion? |
| Success / failure | Visible outcome confirmation | Communicate error or recovery, confirm completion | Functional to Supportive | Not interrupted once shown | Static icon/label | Failure motion that startles or repeats | Is the outcome unambiguous from static content alone? |
| Online / offline | Visible connectivity indicator | Communicate state change | Functional | Debounced against rapid flapping | Static indicator | Rapid flicker during unstable connectivity | Does the indicator avoid flickering during brief connectivity blips? |
| Saved / unsaved | Visible save-state indicator | Confirm completion | Functional | Not interrupted | Static text/icon | Implying saved when a save actually failed | Would the user notice if a save silently failed? |
| New / acknowledged | Visible unread-to-read transition | Direct attention, communicate state change | Functional | Cleared immediately on acknowledgment | Static badge/count | Motion that persists after acknowledgment | Does the indicator clear immediately once seen or opened? |
| Dragging / dropped | Continuous position feedback, settle on drop | Acknowledge input, communicate state change | Functional (tracking) to Supportive (settle) | Cancellable mid-drag | Direct tracking preserved; settle simplified | Drop feedback with no visible settle or confirmation | Is it clear the drop succeeded and where the item landed? |
| Active / inactive | Visible emphasis change | Communicate state change | Functional | Not interrupted | Instant | Ambiguous or absent inactive-state treatment | Can the user tell which item is currently active? |

## 9. Traceability

See [motion/README.md §9](README.md#9-normative-requirements) for the
full `KBDL-MOT-###` list and [traceability-matrix.md](../traceability-matrix.md)
for status and evidence.
