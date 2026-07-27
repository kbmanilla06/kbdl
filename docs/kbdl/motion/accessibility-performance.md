# KBDL Motion — Reduced Motion, Safety, Performance, and Input Methods

**Updated under KBDL-005-A1.** Lifecycle status: `Approved` throughout.
The reduced-motion/no-motion parity core requirement, motion-safety
prohibitions, and the performance and input-method requirements below
(each directly restates an already-`Approved` KBDL-002 principle,
`KBDL-DEC-010`, or `KBDL-THM-012a`) were `Approved` from the start; see
[motion/README.md §9](README.md#9-normative-requirements)
(`KBDL-MOT-022` through `KBDL-MOT-025`) for exact wording. The detailed
per-category substitution matrix in [§1.4](#14-per-category-parity-matrix)
is separate KBDL-005 documentation, now `Approved` (`KBDL-MOT-032`) per
the project owner's approval of
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved)
via [motion/README.md §10](README.md#10-motion-decision-packet).
Per-pattern matrix entries remain `Not verified` until implementation
exists — approval is a lifecycle decision, not validation evidence.

Return to the [motion index](README.md) · [specification index](../README.md).

## 1. Reduced-Motion and No-Motion Parity

A motion-specific accessibility model, extending KBDL's enhanced
motion-safety baseline (`KBDL-DEC-010`) and the already-`Approved`
reduced-motion requirement (`KBDL-THM-012a`).

### 1.1 Motion normally removed under reduced motion

- Large parallax.
- Simulated camera movement.
- Continuous decorative drift (ambient motion).
- Repeated attention motion beyond a single static emphasis.
- Large scale changes.
- Non-essential rotation.
- Animated backgrounds.
- Any motion with no state-comprehension purpose.

### 1.2 Motion that may simplify under reduced motion

- Instant state change (replacing most transitions).
- Short crossfade (replacing directional or spatial transitions where a
  before/after relationship still needs to register).
- Small opacity change (replacing scale/translate combinations).
- Direct input response without inertial "settle" flourish (the direct
  tracking itself is preserved; only the release flourish simplifies).
- Non-animated progress text (replacing animated progress bars, while
  still communicating real progress).

### 1.3 Motion or feedback that may remain when needed

- Input acknowledgment (as an instant state change, not necessarily
  motion, but never removed entirely).
- Direct manipulation tracking (functional, not decorative).
- Focus visibility (never delayed or removed).
- Progress comprehension (in a static or textual form).
- Error recovery feedback (as static emphasis).
- State continuity (as an instant but still perceivable change).
- Safety-critical feedback (never removed, only its motion
  simplified).

### 1.4 Per-category parity matrix

| Category | Full-motion behavior | Reduced-motion behavior | No-motion behavior | Meaning preserved | Validation method |
| --- | --- | --- | --- | --- | --- |
| Immediate feedback | Small scale/opacity change, Immediate/Responsive | Instant color/state change | Same as reduced (already instant) | Input was acknowledged | Manual review of instant-state equivalence |
| State transition | Opacity/height/clip, Fast–Standard | Instant swap | Same as reduced | New state is identifiable | Manual review |
| Spatial navigation | Directional translate/crossfade, Standard | Instant swap or short crossfade | Same as reduced | Destination is reachable and identifiable | Manual review |
| Content change | Opacity/height, bounded stagger | Instant insert/remove/reorder | Same as reduced | Item identity preserved | Manual review |
| System feedback | Determinate fill, low-intensity indeterminate | Static/textual progress | Same as reduced | Progress and completion are knowable | Manual review |
| Attention | Bounded-repetition emphasis | Static emphasis (color/icon/label) | Same as reduced | Attention-worthy state is identifiable without motion | Manual review |
| Direct manipulation | Continuous tracking, spring settle | Tracking preserved; settle simplified to instant | Same as reduced settle | Manipulation result is clear | Manual review |
| Media | User-controlled or bounded muted autoplay | Non-essential autoplay suppressed | Static poster frame | Essential media information available statically | Manual review |
| Ambient | Slow, bounded, low-contrast loop | Removed | Static frame | No functional loss (ambient motion is never essential) | Manual review |
| Theme transition | 150–250ms simultaneous crossfade | Instant switch (`Approved`, `KBDL-THM-012a`) | Same as reduced | Theme changes correctly and readably | Manual review (performed, see [patterns.md §8](patterns.md#8-theme-transition-motion)) |

**Requirements:**

- Reduced motion must not mean reduced functionality — every capability
  available in full motion remains available.
- Motion safety must not rely only on a global reduced-motion
  preference; individual projects must still avoid intrinsically
  hazardous motion regardless of the setting (see [§2](#2-motion-safety)).
- No-motion fallback must remain fully usable, not a degraded
  experience.
- Reduced-motion changes must not introduce abrupt flashing as a side
  effect of removing a smoother transition.
- Motion parity must be reviewed separately from visual similarity — a
  reduced-motion variant does not need to look identical, only to
  preserve the same meaning and functionality.
- User preference must take precedence over decorative intent in every
  case.

## 2. Motion Safety

Prohibited or tightly restricted behavior, extending KBDL's enhanced
motion-safety requirements (`KBDL-DEC-010`):

- Large, rapid movement across the viewport.
- Repeated shaking.
- Continuous zoom.
- Simulated camera movement.
- Rapid alternating direction.
- Unexpected automatic movement the user did not trigger, in
  task-focused contexts.
- High-frequency flashing.
- Full-screen brightness changes.
- Large parallax during reading.
- Uninterruptible long sequences.
- Motion triggered without user cause in task-focused contexts (as
  opposed to Showcase editorial moments, which must still remain
  interruptible and bounded).
- Repeated pulsing near text.
- Essential information available only during animation (it must remain
  available before, during, and after).

Exact safety thresholds (e.g., precise flash-frequency limits) are now
recorded in
[accessibility.md §30](../accessibility.md#30-flashing-vestibular-and-motion-safety-limits)
(KBDL-006), which adopts WCAG 2.2's three-flashes-or-below-threshold
rule (SC 2.3.1) without inventing an additional numeric threshold.
KBDL-005 still defines the enforceable qualitative constraints above,
which apply regardless of and in addition to that WCAG numeric
threshold.

## 3. Performance Requirements

- Motion must not block input — no animation may make a control
  unresponsive while it plays.
- Motion must not intentionally trigger unnecessary layout
  recalculation; prefer transformations that avoid reflow where
  possible.
- Off-screen and hidden motion should pause where practical (e.g., an
  ambient loop in a background tab).
- Decorative animation must be removable without functional loss —
  this is a direct consequence of `KBDL-MOT-001`'s purpose requirement.
- Lower-performance contexts must support simpler movement (reduced
  distance, scale, and concurrent element count).
- Motion should preserve content stability — no unrelated layout shift
  caused by an animation elsewhere on the page.
- Large numbers of independently animated elements are prohibited by
  default (see [foundations.md §5](foundations.md#5-choreography-and-sequencing)
  on batching).
- Performance claims must not be marked `Verified` without
  implementation evidence — a manual design review is not a performance
  measurement.

No rendering technology, animation library, or framework is prescribed;
this remains implementation-neutral per
[motion/README.md §1](README.md#1-repository-and-roadmap-context).

## 4. Mobile and Input-Method Considerations

Motion implications for small screens, touch, pointer, keyboard,
screen-reader interaction, orientation change, virtual-keyboard
appearance, reduced viewport, device rotation, coarse pointer, and
one-handed use.

**Requirements:**

- Mobile motion must avoid excessive off-screen travel relative to the
  smaller viewport.
- Touch feedback must acknowledge input quickly (Immediate timing
  class).
- Motion must not obscure the target of a move or drag operation.
- Keyboard interactions must receive equivalent feedback to pointer/
  touch interactions for the same logical action.
- Screen-reader users must not depend on visual animation for state
  information — every state communicated by motion must also be
  communicated through accessible markup/announcement.
- Orientation change must not trigger a decorative replay of entrance
  motion that already played.
- Virtual-keyboard layout changes (e.g., a text field gaining focus on
  mobile) must not cause unnecessary decorative animation of unrelated
  content.
- Motion must not make small-screen navigation harder to track — prefer
  simpler, shorter transitions on small viewports.

Detailed responsive breakpoint and layout rules are now defined in
[responsive.md](../responsive.md) (KBDL-006); this section is not
restated or reopened there.

## 5. Traceability

See [motion/README.md §9](README.md#9-normative-requirements) for
`KBDL-MOT-022` through `KBDL-MOT-025` and
[traceability-matrix.md](../traceability-matrix.md) for status and
evidence.
