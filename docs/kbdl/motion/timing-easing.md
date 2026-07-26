# KBDL Motion — Timing, Duration, Easing, and Conceptual Tokens

Lifecycle status: `Recommended` for every timing class, exact duration,
easing category, exact curve, and token category in this document —
pending project-owner approval via
[motion/README.md §10](README.md#10-motion-decision-packet). `User-provided`
provenance. `Not applicable`/`Not verified` validation — these are
numerical and naming recommendations, not yet testable implementation
claims. See [motion/README.md §9](README.md#9-normative-requirements)
(`KBDL-MOT-007`, `KBDL-MOT-008`, `KBDL-MOT-009`, and `KBDL-MOT-033` for
the conceptual motion-token architecture in [§4](#4-conceptual-motion-tokens))
for exact requirement wording.

Return to the [motion index](README.md) · [specification index](../README.md).

## 1. Timing Architecture

A semantic timing model, used instead of ad hoc per-component durations
(`KBDL-MOT-007`).

| Class | Purpose | Typical interaction | User-perceived effect | Interruption expectation | Profile adjustment | Reduced-motion behavior | Lifecycle | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Instant | No perceptible transition | State that must never appear to lag (disabled state, focus ring) | Immediate | N/A (no duration to interrupt) | None | Same (already instant) | Recommended | Not applicable |
| Immediate | Acknowledge input | Press, toggle, selection | Feels directly connected to input | Always interruptible by next input | None | Becomes Instant | Recommended | Not applicable |
| Fast | Small, local state change | Hover/pointer feedback, small expand/collapse | Quick but perceptible | Interruptible by opposing state | Precision favors this; Showcase uses it for routine elements | Becomes Instant | Recommended | Not applicable |
| Standard | Ordinary surface or content transition | Navigation, overlay entrance/exit, content insertion | Smooth, unhurried, still brisk | Interruptible by a new navigation or state request | Balanced across profiles | Becomes Instant or a short crossfade | Recommended | Not applicable |
| Deliberate | A transition where pacing itself communicates intent | Expressive reveals, larger overlay/modal moments | Feels considered, not rushed | Interruptible; must resolve gracefully | Showcase uses more; Precision rarely | Becomes Standard or Instant | Recommended | Not applicable |
| Extended | A rare, significant compositional moment | Exceptional-hierarchy entrance sequences | Cinematic without becoming slow | Must remain interruptible; never traps the user | Showcase only | Becomes Instant | Recommended | Not applicable |
| Continuous or indefinite | Motion that persists without a fixed end | Ambient loops, indeterminate loading | Ongoing, low-attention | Must be pausable and bounded in intensity | Showcase (ambient) most; system feedback (loading) in all profiles | Removed or reduced to static | Recommended | Not applicable |

**Requirements:**

- Input acknowledgment (Immediate class) must feel immediate — no
  perceptible delay before feedback begins.
- Required interaction must not wait for decorative motion to complete.
- Repeated workflows should use shorter timing (Fast/Standard) than rare
  expressive moments (Deliberate/Extended).
- Exit motion should not unnecessarily delay removal — exits typically
  use the same or a faster class than the corresponding entrance.
- Blocking system states (errors requiring acknowledgment, required
  confirmations) must not rely on long animations to reach an actionable
  state.
- Longer sequences (Deliberate/Extended) require interruption or skip
  behavior where practical.
- Timing must scale with movement distance and visual complexity — a
  longer distance or more complex sequence may justify a longer class,
  never the reverse.
- Multiple sequential transitions (e.g., a multi-step reveal) must not
  create excessive cumulative delay; the total sequence should stay
  within the Deliberate range even if composed of several Standard
  steps.

New duration values below remain `Recommended` pending project-owner
approval (`KBDL-MOT-008`).

## 2. Duration Recommendations

Implementation-neutral, named or bounded-range durations. Exact
per-component variants remain deferred to the Components module.

| Recommendation | Duration/range | Purpose | Allowed profiles | Interruption behavior | Reduced-motion replacement | Performance impact | Lifecycle | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Press feedback | 80–120ms | Acknowledge a press | All | Always interruptible | Instant | Negligible | Recommended | Not applicable |
| Hover/pointer feedback | 100–150ms | Acknowledge pointer proximity | All | Always interruptible | Instant | Negligible | Recommended | Not applicable |
| Selection feedback | 100–150ms | Communicate selection state | All | Re-triggerable | Instant | Negligible | Recommended | Not applicable |
| Toggle change | 120–180ms | Communicate a binary state change | All | Interruptible by opposing toggle | Instant | Negligible | Recommended | Not applicable |
| Small state transition | 150–200ms | Local expand/collapse, small reveal | All | Interruptible | Instant | Low | Recommended | Not applicable |
| Standard surface transition | 200–280ms | Card, panel, or sheet state change | All | Interruptible | Instant or short crossfade | Low to moderate | Recommended | Not applicable |
| Overlay entrance and exit | 220–320ms | Modal, dialog, sheet appearance/dismissal | All | Interruptible; exit should not exceed entrance duration | Instant | Moderate | Recommended | Not applicable |
| Navigation transition | 220–320ms | Route or view change | All (Precision favors the lower bound) | New navigation cancels in-progress transition | Instant or short crossfade | Moderate | Recommended | Not applicable |
| Content insertion and removal | 150–250ms | List/content add or remove | All | Superseding update resolves in-progress change first | Instant | Low to moderate (bounded at scale, see `KBDL-MOT-011`) | Recommended | Not applicable |
| Progress change | Matches real operation duration (no artificial fixed duration) | Determinate progress fill | All | Reflects actual operation state | Static/textual progress | Negligible | Recommended | Not applicable |
| Attention cue | 400–600ms per repetition, bounded total repetitions (see [patterns.md §4](patterns.md#4-attention-motion)) | Direct attention | All | Stops on interaction with the attended element | Static emphasis | Low | Recommended | Not applicable |
| Expressive reveal | 320–480ms | Showcase entrance/editorial reveal | Mostly Showcase | Interruptible | Instant or short crossfade | Moderate | Recommended | Not applicable |
| Theme transition | 150–250ms | Light/dark theme switch (see [patterns.md §8](patterns.md#8-theme-transition-motion)) | All (shared architecture, `KBDL-THM-006`) | Rapid repeated toggles resolve to latest requested theme | Instant (already `Approved`, `KBDL-THM-012a`) | Low | Recommended | Not applicable |
| Ambient-loop cycle | 4–8 seconds per cycle, low-contrast | Background/ambient motion | Mostly Showcase | Pausable at any point | Removed or static | Low (by design — slow, infrequent repaint) | Recommended | Not applicable |
| Reduced-motion replacement | 0–100ms (effectively instant) | Any pattern under reduced-motion preference | All | Always interruptible (trivially, given near-zero duration) | Is itself the reduced-motion replacement | Minimal | Recommended | Not applicable |

## 3. Easing Architecture

Semantic, framework-independent easing categories (`KBDL-MOT-009`).

| Category | Perceptual purpose | Suitable direction | Permitted categories | Prohibited usage | Interruption behavior | Reversal behavior | Relationship to duration | Accessibility | Performance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Linear | Mechanical, constant-rate change | Progress indication, direct-manipulation tracking | System feedback, direct manipulation | Entrances/exits (feels mechanical, contradicts Digital Luxury) | N/A (constant rate, trivially interruptible) | Trivial (constant rate reverses identically) | Independent of duration | Predictable, never disorienting | Cheapest to compute |
| Responsive | Fast start, matching direct input | Direct manipulation, immediate feedback | Immediate feedback, direct manipulation | Long, deliberate entrances | Always interruptible | Reverses cleanly from current position | Pairs with Immediate/Fast durations | Feels connected to input | Low cost |
| Enter | Decelerating arrival (starts fast, settles) | Entrances | State transition, spatial navigation, content change (insertion) | Exits (wrong perceptual direction) | Interruptible; settling phase may be cut short | Reversing mid-entrance becomes an Exit-curve exit | Pairs with Standard/Deliberate durations | Clear arrival cue | Low to moderate cost |
| Exit | Accelerating departure (starts slow, speeds up) | Exits | State transition, spatial navigation, content change (removal) | Entrances (wrong perceptual direction) | Interruptible; may be cut short without visual artifact | Reversing mid-exit becomes an Enter-curve entrance | Pairs with Standard durations, often shorter than the paired Enter | Clear departure cue | Low to moderate cost |
| Standard | Balanced ease-in-out for state changes without a strong directional arrival/departure | State transition, content change | Toggle, small state transition | Direct manipulation (feels disconnected from live input) | Interruptible | Symmetrical, reverses naturally | Pairs with Fast/Standard durations | Neutral, unobtrusive | Low cost |
| Emphasized | Pronounced deceleration for significant, attention-worthy moments | Expressive reveals, Exceptional-level entrances | Media, ambient (bounded), theme transition (only if a stronger arrival is later approved) | Immediate feedback (too slow-feeling for routine interaction) | Interruptible; must not trap the user | Reverses into a matching Exit-style curve | Pairs with Deliberate/Extended durations | Must remain interruptible to avoid trapping motion-sensitive users | Moderate cost |
| Direct manipulation | Zero or near-zero easing lag, tracks input 1:1 | Drag, swipe, resize, scrub | Direct manipulation only | Any non-input-driven transition | Always interruptible (it *is* the input) | N/A — position is the input's position | Independent of duration (continuous) | Predictable, matches proprioceptive expectation | Must sustain the display's native responsive rate |
| Spring-like | Naturalistic settle with slight overshoot damping | Release/settle after direct manipulation | Direct manipulation (settle phase only) | Any motion requiring exact, predictable end timing (e.g., choreographed sequences) | Interruptible by new input at any point | Settles from current velocity/position, not a restart | Duration is inherently variable (settles based on physics-like behavior, not a fixed time) | Overshoot must stay small enough not to make targets feel unstable | Slightly higher cost if computed per-frame; a closed-form approximation is acceptable |
| Step or discrete | Instant, discrete jumps with no interpolation | Instant class transitions, reduced-motion replacements | Any category, as the reduced-motion substitute | Anything meant to feel smooth or continuous | Trivially interruptible (no in-between state to interrupt) | Trivial | Independent of duration (effectively zero) | This *is* the accessible fallback for every other category | Cheapest |

**Exact curves (`Recommended`, semantic names, framework-neutral
cubic-bezier-equivalent descriptions):**

- **Standard-Enter** — decelerating curve, roughly equivalent to
  `cubic-bezier(0.05, 0.7, 0.1, 1.0)`. Used for entrances at Standard
  duration. Reversal: transitions into Standard-Exit's curve shape from
  the current position. Interruption: safe to cut at any point; no
  overshoot to resolve.
- **Standard-Exit** — accelerating curve, roughly equivalent to
  `cubic-bezier(0.3, 0.0, 1.0, 1.0)`. Used for exits at Standard or Fast
  duration. Reversal: transitions into Standard-Enter's curve shape.
  Interruption: safe to cut at any point.
- **Emphasized-Enter** — a stronger deceleration, roughly equivalent to
  `cubic-bezier(0.05, 0.8, 0.05, 1.0)`. Used for Deliberate/Extended
  expressive entrances. Reversal: transitions into Emphasized-Exit.
  Interruption: must remain cuttable at any point despite the stronger
  curve.
- **Emphasized-Exit** — a stronger acceleration, roughly equivalent to
  `cubic-bezier(0.3, 0.0, 0.8, 0.15)`. Used for Deliberate expressive
  exits. Reversal: transitions into Emphasized-Enter.
- **Standard** (balanced ease-in-out) — roughly equivalent to
  `cubic-bezier(0.4, 0.0, 0.2, 1.0)`. Used for symmetrical state changes
  with no strong directional arrival/departure. Reversal: symmetrical,
  reverses through the same shape.

Every exact curve above is: marked `Recommended`; named semantically
(not by its numeric value alone); explained above; conceptually tested
for interruption and reversal in the table; kept independent of any
animation framework; and included in
[motion/README.md §10.2](README.md#102-recommended-decisions--ready-for-approval)
item 3. No spring-physics library or specific animation engine is
required — the Spring-like category is described qualitatively and may
be approximated with a closed-form curve.

## 4. Conceptual Motion Tokens

An implementation-neutral semantic motion-token architecture. No CSS
custom properties, JSON files, or framework-specific format are created
here — this defines naming categories only.

| Token category | What it names | Example semantic names (illustrative, not final) | Notes |
| --- | --- | --- | --- |
| Duration | A named timing-class value from [§1](#1-timing-architecture)/[§2](#2-duration-recommendations) | `duration-immediate`, `duration-standard`, `duration-deliberate` | Maps to a range, not a single hardcoded number, until implementation |
| Easing | A named easing category from [§3](#3-easing-architecture) | `easing-standard-enter`, `easing-emphasized-exit` | Framework-neutral curve description |
| Delay | A named offset before a motion begins | `delay-none`, `delay-short` | Used sparingly; most motion should begin immediately |
| Stagger | A named per-item offset within a sequence | `stagger-tight`, `stagger-loose` | Bounded per [foundations.md §5](foundations.md#5-choreography-and-sequencing) |
| Distance | A named movement-distance class | `distance-small`, `distance-moderate`, `distance-large` | Qualitative; exact pixel values deferred to Components |
| Scale | A named scale-change class | `scale-subtle`, `scale-moderate` | Qualitative; exact values deferred to Components |
| Opacity | A named opacity-change class | `opacity-fade-partial`, `opacity-fade-full` | Used for entrance/exit and state-change motion |
| Rotation | A named rotation class | `rotation-none`, `rotation-small` | Reserved for meaningful rotation only, per [foundations.md §6](foundations.md#6-spatial-movement) |
| Motion level | A named hierarchy level from [foundations.md §3](foundations.md#3-motion-hierarchy) | `motion-level-functional`, `motion-level-expressive` | Ties a pattern to its review requirements |
| Repetition | A named bounded-repetition count | `repetition-none`, `repetition-bounded` | Used for attention motion, per [patterns.md §4](patterns.md#4-attention-motion) |
| Sequence | A named choreography pattern | `sequence-lead-follow`, `sequence-crossfade` | Ties to [foundations.md §5](foundations.md#5-choreography-and-sequencing) |
| Reduced-motion substitution | A named mapping from a full-motion token set to its reduced/no-motion equivalent | `reduced-motion-instant`, `reduced-motion-crossfade` | Every full-motion token combination must have a documented substitution, per [accessibility-performance.md §1](accessibility-performance.md#1-reduced-motion-and-no-motion-parity) |

**Requirements:**

- Token names must be semantic (tied to purpose or timing class), not
  tied to a specific component.
- The token architecture must not require CSS, JSON, JavaScript, or any
  specific design tool to exist conceptually.
- The exact token-file format remains deferred (implementation-layer,
  out of scope for this specification).
- Tokens must distinguish lifecycle approval (is this token's value
  authorized for use) from implementation validation (has it actually
  been implemented and checked) — the same three-dimension model as
  every other KBDL requirement.
- Project overrides of motion tokens must remain bounded by the
  [controlled visual variables](../principles.md#52-controlled-visual-variables)
  model (motion amplitude is itself a controlled variable).
- Profiles must share one token architecture, varying only which named
  value is selected per pattern, not the category structure itself.
- Reduced-motion substitutions must be addressable conceptually for
  every token combination that produces visible motion.

## 5. Traceability

See [motion/README.md §9](README.md#9-normative-requirements) for
`KBDL-MOT-007`, `KBDL-MOT-008`, `KBDL-MOT-009` and
[traceability-matrix.md](../traceability-matrix.md) for status and
evidence.
