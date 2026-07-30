# KBDL Components

Design specifications for the core interface components. These are
framework-independent: they describe intent, anatomy, states, behaviour, and
accessibility requirements, not implementation code.

**Every component inherits these rules**, so they are stated once here rather
than repeated 24 times:

* **Semantics** — implement with the host platform's native semantics where one
  exists. A button is a button element, not a clickable div.
* **Focus** — every interactive element shows a visible focus indicator using
  `focus.ring-width` / `focus.ring-offset` / `focus.ring-color`. Focus is never
  removed, only restyled.
* **Keyboard** — everything operable by pointer is operable by keyboard.
  `Tab` moves between components, arrow keys move within a composite.
* **Targets** — pointer targets meet `size.target-minimum` (24px); prefer
  `size.target-comfortable` (44px) on touch-first surfaces.
* **States** — default, hover, focus, active/pressed, selected, disabled,
  read-only, loading, error. Disabled and read-only are visually and
  semantically distinct: read-only content is still readable and selectable.
* **Non-color** — state and meaning are never carried by color alone.
* **Motion** — use `motion.duration.*` and `motion.easing.*`; all motion honours
  reduced-motion (see [motion](../motion/README.md)).
* **Contrast** — text meets 4.5:1, non-text boundaries 3:1.

Sizes below refer to `size.control-height-small|medium|large` (32/40/48px).

---

## 1. Button

**Purpose** — trigger an action.
**When to use** — submitting, confirming, opening a dialog, any state change.
**When not to use** — navigation between pages; use a text link.
**Anatomy** — container; optional leading icon; label; optional trailing icon.
**Variants** — primary (one per view), secondary, tertiary/ghost, destructive.
**Sizes** — small, medium (default), large.
**States** — default, hover, focus, pressed, disabled, loading.
**Interaction** — activates on release inside bounds; loading state disables
re-submission and announces busy status.
**Responsive** — may go full-width in compact; never shrink below the target
minimum.
**Keyboard** — `Enter` and `Space` activate.
**Focus** — ring outside the container, never clipped.
**Accessibility** — label describes the outcome ("Save changes"), not "Click
here". Icon-only variants require an accessible name.
**Content** — sentence case, verb-first, 1–3 words.
**Tokens** — `color.action.primary`, `color.action.primary-text`,
`radius.subtle`, `space.3`/`space.4`, `size.control-height-*`,
`motion.duration.immediate`.
**Do** — one primary action per view; keep destructive actions visually distinct.
**Avoid** — three or more primary buttons competing; disabling submit without
explaining why.

## 2. Text link

**Purpose** — navigate to another location.
**When to use** — in-sentence navigation, references, breadcrumb entries.
**When not to use** — actions that change state; use a button.
**Anatomy** — inline text; optional external-link indicator.
**Variants** — inline, standalone, external.
**Sizes** — inherits surrounding type.
**States** — default, hover, focus, visited, active.
**Interaction** — activates on click or `Enter`.
**Responsive** — wraps with surrounding text; never truncated mid-word.
**Keyboard** — `Enter` activates.
**Focus** — visible ring around the text bounds, including wrapped lines.
**Accessibility** — distinguishable from body text by more than color alone
(underline by default). Link text makes sense out of context.
**Content** — describe the destination; never "click here" or a bare URL.
**Tokens** — `color.text.link`, `typography.*`, `focus.*`.
**Do** — mark links that open in a new context.
**Avoid** — styling a link as a button when it navigates, and vice versa.

## 3. Icon button

**Purpose** — a compact action where the icon meaning is unambiguous.
**When to use** — toolbars, dense controls, close/dismiss affordances.
**When not to use** — where the icon's meaning is not universally understood
without a label.
**Anatomy** — square target; single icon; optional tooltip.
**Variants** — standard, ghost, destructive, toggle.
**Sizes** — small, medium, large; target never below `size.target-minimum`.
**States** — default, hover, focus, pressed, selected (toggle), disabled.
**Interaction** — toggle variants report pressed state.
**Responsive** — spacing may tighten; target size may not.
**Keyboard** — `Enter` and `Space` activate.
**Focus** — ring follows the target, not the glyph.
**Accessibility** — always has an accessible name. A tooltip is not a
substitute for one.
**Content** — name states the action ("Close dialog").
**Tokens** — `size.icon-*`, `size.target-*`, `radius.subtle`, `opacity.hover-state`.
**Do** — pair with a tooltip for discoverability.
**Avoid** — icon-only destructive actions without confirmation.

## 4. Text input

**Purpose** — collect a single line of text.
**When to use** — names, emails, short freeform values.
**When not to use** — long text (textarea); constrained choice (select).
**Anatomy** — label; optional description; field; optional prefix/suffix;
optional error message.
**Variants** — standard, password, search, with prefix/suffix.
**Sizes** — small, medium, large.
**States** — default, hover, focus, filled, disabled, read-only, error.
**Interaction** — validates on blur or submit, not on every keystroke.
**Responsive** — full-width within its container in compact.
**Keyboard** — standard text editing; `Escape` clears search variants.
**Focus** — ring on the field container.
**Accessibility** — a persistent visible label, programmatically associated.
Placeholder is never the label. Errors are associated with the field and
announced.
**Content** — label is a noun phrase; description explains format before the
user errs.
**Tokens** — `color.border.default`, `color.border.focus`, `radius.subtle`,
`space.3`, `size.control-height-*`.
**Do** — show format requirements up front.
**Avoid** — placeholder-only labelling; clearing input on error.

## 5. Textarea

**Purpose** — collect multi-line text.
**When to use** — comments, descriptions, messages.
**When not to use** — single-line values.
**Anatomy** — label; optional description; multi-line field; optional counter;
optional resize handle.
**Variants** — fixed height, auto-growing.
**Sizes** — small, medium, large (by rows).
**States** — default, hover, focus, filled, disabled, read-only, error.
**Interaction** — auto-grow to a stated maximum, then scroll internally.
**Responsive** — full-width in compact; height adapts to available space.
**Keyboard** — `Enter` inserts a newline; it does not submit.
**Focus** — ring on the field container.
**Accessibility** — a character counter must be announced politely, never
assertively on every keystroke.
**Content** — state limits before they are reached.
**Tokens** — as text input, plus `typography.line-height.body`.
**Do** — allow resizing where layout permits.
**Avoid** — hard limits with no warning.

## 6. Select

**Purpose** — choose one option from a known list.
**When to use** — 5+ mutually exclusive options.
**When not to use** — 2–4 options (radio group); multi-select without a
dedicated pattern.
**Anatomy** — label; trigger showing current value; indicator; option list.
**Variants** — native select (default), custom combobox with filtering.
**Sizes** — small, medium, large.
**States** — default, hover, focus, open, selected, disabled, error.
**Interaction** — prefer the native control. Use a custom combobox only when
filtering, grouping, or rich option content is genuinely required — a custom
one must reimplement everything the native control gives free.
**Responsive** — may present as a full-screen sheet in compact.
**Keyboard** — arrows move, `Enter` selects, `Escape` closes and returns focus,
typing jumps to a match.
**Focus** — returns to the trigger on close.
**Accessibility** — expanded state, active option, and selection are exposed.
**Content** — option labels are parallel in structure.
**Tokens** — `layer.overlay`, `shadow.level-2`, `radius.subtle`.
**Do** — keep the current value visible in the trigger.
**Avoid** — a custom combobox where a native select would do.

## 7. Checkbox

**Purpose** — toggle an independent option, or several from a set.
**When to use** — opt-in, multi-select lists, "select all".
**When not to use** — mutually exclusive choice (radio); immediate-effect
setting (switch).
**Anatomy** — box; check or indeterminate mark; label; optional description.
**Variants** — single, group, with indeterminate parent.
**Sizes** — small, medium.
**States** — unchecked, checked, indeterminate, focus, disabled, error.
**Interaction** — the label is part of the target.
**Responsive** — stacks vertically in compact.
**Keyboard** — `Space` toggles.
**Focus** — ring around box and label together.
**Accessibility** — indeterminate is a real tri-state, not a styled checked
state. Group has a group label.
**Content** — positive phrasing; avoid double negatives.
**Tokens** — `color.action.primary`, `radius.subtle`, `size.target-*`.
**Do** — make the whole row clickable.
**Avoid** — using a checkbox for an action that takes effect immediately.

## 8. Radio group

**Purpose** — choose exactly one option from a small set.
**When to use** — 2–4 visible, comparable options.
**When not to use** — many options (select); independent toggles (checkbox).
**Anatomy** — group label; radio controls; labels; optional descriptions.
**Variants** — vertical (default), horizontal, card-style.
**Sizes** — small, medium.
**States** — unselected, selected, focus, disabled, error.
**Interaction** — selecting one deselects the rest; no deselect-to-empty once
chosen unless a "none" option exists.
**Responsive** — horizontal collapses to vertical in compact.
**Keyboard** — `Tab` enters the group; arrows move and select within it.
**Focus** — follows the selected radio, or the first when none is selected.
**Accessibility** — the group is a labelled radiogroup; options share a name.
**Content** — options are mutually exclusive and collectively exhaustive.
**Tokens** — `color.action.primary`, `space.3`.
**Do** — provide an explicit "none" option when that is valid.
**Avoid** — a single radio with no alternative.

## 9. Switch

**Purpose** — turn a setting on or off with immediate effect.
**When to use** — settings that apply instantly.
**When not to use** — anything requiring submit; use a checkbox.
**Anatomy** — track; thumb; label; optional description.
**Variants** — standard, with status text.
**Sizes** — small, medium.
**States** — off, on, focus, disabled, loading (async).
**Interaction** — applies immediately; if it can fail, show pending state and
revert visibly with an explanation.
**Responsive** — label wraps; control stays fixed.
**Keyboard** — `Space` toggles.
**Focus** — ring around the control.
**Accessibility** — exposes on/off state; state is not conveyed by position
alone.
**Content** — label names the thing controlled, not the current state.
**Tokens** — `color.action.primary`, `radius.pill`, `motion.duration.fast`.
**Do** — confirm asynchronous failures.
**Avoid** — pairing a switch with a Save button.

## 10. Form field and validation message

**Purpose** — the shared wrapper giving any control its label, help, and error.
**When to use** — every form control.
**When not to use** — non-form controls.
**Anatomy** — label; optional required indicator; optional description;
control; validation message.
**Variants** — stacked (default), inline label, compact.
**Sizes** — inherits the control.
**States** — default, filled, disabled, read-only, error, success.
**Interaction** — validate on blur and on submit. Never validate mid-typing on
first entry.
**Responsive** — inline labels become stacked in compact.
**Keyboard** — label activation moves focus to the control.
**Focus** — moves to the first invalid field on failed submit.
**Accessibility** — description and error are both programmatically associated.
Errors are announced. Required state is conveyed in text, not by an asterisk
alone.
**Content** — errors say what is wrong and how to fix it: "Enter a date in the
future", not "Invalid input".
**Tokens** — `color.feedback.critical-text`, `space.2`, `typography.size.label`.
**Do** — keep the message adjacent to its field.
**Avoid** — clearing valid input when another field fails.

## 11. Card

**Purpose** — group related content into a single scannable unit.
**When to use** — collections of comparable items.
**When not to use** — as decoration around unrelated content.
**Anatomy** — surface; optional media; optional header; body; optional actions.
**Variants** — static, interactive (whole card is a link), with media, with
actions.
**Sizes** — fluid; height driven by content.
**States** — default, hover, focus, pressed, selected, disabled.
**Interaction** — a card is either entirely one target or contains discrete
targets — never both, which creates nested interactive elements.
**Responsive** — grid reflows to a single column in compact.
**Keyboard** — interactive cards are a single tab stop.
**Focus** — ring around the whole surface.
**Accessibility** — an interactive card has one accessible name, usually its
heading.
**Content** — lead with the most identifying information.
**Tokens** — `color.background.surface`, `radius.standard`, `shadow.level-1`,
`space.4`.
**Do** — keep cards in a set structurally consistent.
**Avoid** — burying the primary action below the fold of the card.

## 12. Badge / tag

**Purpose** — label, categorise, or show a short status.
**When to use** — status, counts, categories.
**When not to use** — as a button; as body text.
**Anatomy** — container; optional dot or icon; short label; optional remove
affordance.
**Variants** — neutral, informational, positive, caution, critical, removable.
**Sizes** — small, medium.
**States** — static, removable-hover, removable-focus.
**Interaction** — non-interactive unless removable.
**Responsive** — wraps; never truncates a status word.
**Keyboard** — removable badges are focusable; `Backspace`/`Delete` removes.
**Focus** — ring on the remove control.
**Accessibility** — status meaning is in the text, never color alone. Count
badges have an accessible name ("3 unread").
**Content** — one or two words.
**Tokens** — `color.status.*`, `radius.pill`, `typography.size.caption`.
**Do** — use a consistent status vocabulary.
**Avoid** — dense rows of badges where a single value would read better.

## 13. Alert

**Purpose** — communicate an important in-page message.
**When to use** — validation summaries, system status, contextual warnings.
**When not to use** — transient confirmations (toast); blocking decisions
(dialog).
**Anatomy** — container; status icon; title; message; optional actions; optional
dismiss.
**Variants** — informational, positive, caution, critical.
**Sizes** — inline, page-level.
**States** — default, dismissible-hover/focus.
**Interaction** — persists until resolved or dismissed; never auto-hides
critical content.
**Responsive** — actions stack below the message in compact.
**Keyboard** — dismiss is reachable; focus moves sensibly after dismissal.
**Focus** — critical alerts appearing after an action receive or announce focus.
**Accessibility** — critical alerts use an assertive live region; informational
ones polite. Icon plus text, never icon alone.
**Content** — state the problem and the next step.
**Tokens** — `color.feedback.*`, `radius.subtle`, `space.4`.
**Do** — place validation summaries above the form and link to fields.
**Avoid** — stacking many alerts; the first stops being read.

## 14. Toast / notification

**Purpose** — brief, transient confirmation of a completed action.
**When to use** — "Saved", "Copied", "Message sent".
**When not to use** — errors needing action; anything the user must read.
**Anatomy** — container; optional icon; message; optional single action;
optional dismiss.
**Variants** — neutral, positive, caution, critical.
**Sizes** — single line preferred; two maximum.
**States** — entering, visible, exiting, paused.
**Interaction** — auto-dismisses after a readable interval; pauses on hover and
on focus; queue rather than stack indefinitely.
**Responsive** — full-width at the bottom in compact; corner-anchored above.
**Keyboard** — reachable without a mouse; `Escape` dismisses when focused.
**Focus** — never steals focus.
**Accessibility** — polite live region. Anything requiring action belongs in an
alert, not a toast, because a toast may vanish before it is read.
**Content** — past tense, under about eight words.
**Tokens** — `layer.toast`, `shadow.level-3`, `motion.duration.standard`.
**Do** — offer undo for destructive actions instead of pre-confirming.
**Avoid** — more than one toast at a time.

## 15. Dialog

**Purpose** — interrupt for a focused decision or task.
**When to use** — confirmation of consequence, short focused input.
**When not to use** — long forms; content that belongs on a page.
**Anatomy** — scrim; container; title; body; actions; close control.
**Variants** — modal, non-modal, confirmation, destructive confirmation,
full-screen (compact).
**Sizes** — small, medium, large.
**States** — opening, open, closing.
**Interaction** — modal dialogs trap focus and block the page beneath.
**Responsive** — becomes a full-screen sheet in compact.
**Keyboard** — `Escape` closes; `Tab` cycles inside; focus never escapes a
modal.
**Focus** — moves to the dialog on open (title or first control) and returns to
the trigger on close.
**Accessibility** — labelled by its title; marked modal; background content is
inert.
**Content** — title states the decision; the confirm button names the outcome
("Delete project"), not "OK".
**Tokens** — `layer.dialog`, `shadow.level-4`, `radius.pronounced`,
`color.background.overlay-scrim`.
**Do** — make destructive confirmation buttons explicit and distinct.
**Avoid** — dialogs opening dialogs.

## 16. Tooltip

**Purpose** — supplementary, non-essential explanation on hover or focus.
**When to use** — clarifying an icon button or a truncated value.
**When not to use** — essential information; interactive content; anything
needed on touch.
**Anatomy** — trigger; container; short text; optional pointer.
**Variants** — plain text only.
**Sizes** — sized to content, with a maximum width.
**States** — hidden, showing, shown, hiding.
**Interaction** — short delay in, minimal delay out; stays while the pointer
moves toward it; dismissible with `Escape` while it remains hoverable.
**Responsive** — not a touch mechanism; provide a visible alternative in
compact.
**Keyboard** — appears on focus, not only on hover.
**Focus** — never receives focus itself.
**Accessibility** — never the only place information exists. Never contains
interactive content.
**Content** — one short phrase, no punctuation needed.
**Tokens** — `layer.tooltip`, `radius.subtle`, `motion.duration.fast`.
**Do** — pair with icon-only controls.
**Avoid** — putting a link or button inside a tooltip.

## 17. Tabs

**Purpose** — switch between sibling views in the same context.
**When to use** — 2–6 peer sections of comparable importance.
**When not to use** — sequential steps (use a stepper); navigation between
pages.
**Anatomy** — tab list; tabs; active indicator; panels.
**Variants** — underline, contained, scrollable.
**Sizes** — small, medium.
**States** — default, hover, focus, selected, disabled.
**Interaction** — v1 default is **manual activation**: arrows move focus,
`Enter` or `Space` activates. Automatic activation is acceptable only when
panel content is instant and lightweight.
**Responsive** — becomes horizontally scrollable rather than wrapping to two
rows; may become a select in compact.
**Keyboard** — arrows move within the list; `Home`/`End` jump; `Tab` leaves the
list to the panel.
**Focus** — the tab list is a single tab stop.
**Accessibility** — tabs and panels are associated; the selected tab is exposed.
**Content** — short parallel nouns.
**Tokens** — `color.action.primary`, `space.4`, `motion.duration.fast`.
**Do** — keep panel content at a comparable level of importance.
**Avoid** — hiding required form fields inside an unselected tab.

## 18. Primary navigation

**Purpose** — move between the main areas of a product.
**When to use** — top-level product structure.
**When not to use** — in-page section links.
**Anatomy** — container; brand or home link; items; optional grouping; current
indicator; optional collapse trigger.
**Variants** — horizontal bar, sidebar, collapsible drawer.
**Sizes** — standard, compact/condensed.
**States** — default, hover, focus, current, disabled.
**Interaction** — collapses to a drawer below the width at which items no
longer fit — a content-driven threshold, not a device guess.
**Responsive** — drawer in compact; persistent from `standard` upward when
space allows.
**Keyboard** — reachable early in tab order; a skip link precedes it; drawer
traps focus while open and `Escape` closes.
**Focus** — returns to the trigger when the drawer closes.
**Accessibility** — a labelled navigation landmark; current item is
programmatically current, not styled-only.
**Content** — short, stable, predictable labels.
**Tokens** — `layer.navigation`, `color.background.surface`, `space.4`.
**Do** — always provide a skip link.
**Avoid** — hiding primary navigation behind a menu on large viewports.

## 19. Breadcrumb

**Purpose** — show position in a hierarchy and allow moving up it.
**When to use** — nested structures more than two levels deep.
**When not to use** — flat products; as a history trail.
**Anatomy** — list of links; separators; current page as plain text.
**Variants** — full, truncated with overflow.
**Sizes** — single size, small type.
**States** — default, hover, focus, current.
**Interaction** — truncation collapses the middle and keeps the first and
immediate parent reachable.
**Responsive** — truncates rather than wrapping in compact.
**Keyboard** — normal link behaviour.
**Focus** — standard link focus.
**Accessibility** — a labelled navigation landmark; the current page is marked
current and is not a link.
**Content** — mirror the real hierarchy and the page titles.
**Tokens** — `typography.size.body-small`, `color.text.secondary`, `space.2`.
**Do** — keep the parent level always reachable.
**Avoid** — breadcrumbs that show history instead of hierarchy.

## 20. Table / structured list

**Purpose** — present comparable records across shared attributes.
**When to use** — scanning and comparing rows of data.
**When not to use** — layout; single-record display.
**Anatomy** — optional caption; header row; body rows; cells; optional
selection, sort, and row actions; optional footer.
**Variants** — plain, sortable, selectable, expandable rows, sticky header.
**Sizes** — comfortable, compact, dense (Precision).
**States** — default, hover, focus, selected, sorted, loading, empty.
**Interaction** — sorting states which column and direction; selection reports
how many are selected.
**Responsive** — do not squeeze every column into compact. Either scroll
horizontally with a pinned identifying column, or switch to stacked
label-and-value cards. Never silently drop data.
**Keyboard** — headers that sort are buttons; row actions are individually
reachable.
**Focus** — visible per cell or per row, consistently.
**Accessibility** — real table semantics with header associations. A caption or
accessible name describes the content. Sort state is exposed.
**Content** — align numbers right, text left; keep units in the header.
**Tokens** — `color.border.subtle`, `space.3`, `typography.size.body-small`.
**Do** — keep the identifying column visible while scrolling.
**Avoid** — nested tables and horizontal scrolling without an affordance.

## 21. Pagination

**Purpose** — move through a set too large to show at once.
**When to use** — long, ordered result sets.
**When not to use** — short lists; continuous feeds (use load-more).
**Anatomy** — previous; page numbers with truncation; next; optional page-size
selector; optional result count.
**Variants** — numbered, previous/next only, load-more.
**Sizes** — small, medium.
**States** — default, hover, focus, current, disabled at boundaries.
**Interaction** — truncation always keeps first, last, current, and current's
neighbours reachable.
**Responsive** — reduces to previous/next plus a position indicator in compact.
**Keyboard** — every control is a button or link; current page is not a link.
**Focus** — after navigating, focus moves to the results region or its heading.
**Accessibility** — a labelled navigation landmark; current page is marked
current; the result count is announced.
**Content** — "Page 3 of 20", not just "3".
**Tokens** — `space.2`, `size.target-*`, `radius.subtle`.
**Do** — show total results where known.
**Avoid** — hiding the last page.

## 22. Loading indicator

**Purpose** — show that work is in progress.
**When to use** — waits long enough to notice (roughly 300ms+).
**When not to use** — instant operations; replacing meaningful content that
could be shown progressively.
**Anatomy** — indeterminate spinner or determinate bar; optional label;
optional percentage.
**Variants** — indeterminate, determinate, inline, full-region.
**Sizes** — small (inline), medium, large.
**States** — active, complete, error.
**Interaction** — determinate when progress is genuinely known; never fake it.
**Responsive** — scales with its container.
**Keyboard** — non-interactive; does not take focus.
**Focus** — focus stays where it was; it does not jump to the indicator.
**Accessibility** — busy state and completion are announced politely. Long
waits get a text label, not a bare spinner. Continuous rotation respects
reduced-motion by slowing or substituting a non-animated indicator.
**Content** — say what is happening: "Loading results".
**Tokens** — `motion.duration.extended`, `color.action.primary`.
**Do** — keep surrounding layout stable so nothing jumps on completion.
**Avoid** — a full-page spinner for a small regional update.

## 23. Skeleton

**Purpose** — preview the shape of content that is about to arrive.
**When to use** — predictable layouts on first load.
**When not to use** — unknown result shapes; very short waits; error states.
**Anatomy** — neutral blocks matching the real content's geometry.
**Variants** — text lines, media block, card, table row.
**Sizes** — matches the content it stands in for.
**States** — shimmering or static; replaced by content.
**Interaction** — non-interactive; never clickable.
**Responsive** — reflows exactly as the real content will.
**Keyboard** — not focusable.
**Focus** — none.
**Accessibility** — the region is marked busy; skeletons are hidden from
assistive technology, which gets a single "loading" message instead of dozens
of empty shapes. Shimmer respects reduced-motion.
**Content** — none; never fake words.
**Tokens** — `color.background.surface-raised`, `radius.subtle`,
`motion.duration.extended`.
**Do** — match the real layout so nothing shifts on arrival.
**Avoid** — skeletons that stay indefinitely when a request has failed.

## 24. Empty state

**Purpose** — explain why there is nothing here and what to do next.
**When to use** — no data yet, no results, cleared, or an error left nothing.
**When not to use** — while still loading.
**Anatomy** — optional illustration or icon; heading; explanation; optional
primary action; optional secondary help.
**Variants** — first-use, no-results, error, cleared/completed.
**Sizes** — inline (within a region), full-page.
**States** — static.
**Interaction** — the action resolves the emptiness — create the first item,
clear filters, retry.
**Responsive** — centred and constrained in width; illustration may drop in
compact.
**Keyboard** — the action is reachable in normal order.
**Focus** — after filtering to nothing, focus or announcement lands on the empty
state so the change is not silent.
**Accessibility** — the message is real text, not text baked into an image.
Decorative illustrations are hidden from assistive technology.
**Content** — distinguish "you have no projects yet" from "no projects match
these filters"; they need different actions.
**Tokens** — `space.8`, `typography.size.heading-3`, `color.text.secondary`.
**Do** — offer the exact action that fixes it.
**Avoid** — a bare "No data" with no explanation or way forward.

---

## Composition rules

* Prefer composing these components over creating new ones.
* A new component needs a distinct purpose no existing one covers, and must
  reuse existing tokens and states.
* Never nest interactive elements inside other interactive elements.
* Keep one primary action per view or per dialog.
* Components adapt across profiles by density, motion intensity, and surface
  treatment — never by changing semantics, keyboard behaviour, or accessibility
  requirements. See [profiles](../profiles.md).

## Related

[Tokens](../tokens/README.md) · [Patterns](../patterns.md) ·
[Accessibility](../accessibility.md) · [Motion](../motion/README.md) ·
[Responsive](../responsive.md)

Deeper per-requirement component detail is retained in
[components-core.md](../components-core.md) and
[components-system.md](../components-system.md).
