# KBDL Patterns

Recurring solutions built from KBDL [components](components/README.md). Each
states the user goal, a recommended structure, the components involved, and the
responsive and accessibility considerations that most often get missed.

---

## Page structure

**User goal** — orient quickly and find the main content.
**Structure** — skip link → header with primary navigation → optional
breadcrumb → single `h1` → main content → optional complementary region →
footer. One `main` landmark per page.
**Components** — primary navigation, breadcrumb.
**Responsive** — navigation collapses to a drawer in compact; content stays
single-column; the container follows `container.*` widths.
**Accessibility** — real landmarks, one `h1`, heading levels never skipped, skip
link first in tab order.
**Common mistakes** — multiple `h1`s; visual hierarchy that does not match
heading order; a skip link that is present but never focusable.

## Navigation hierarchy

**User goal** — understand where I am and how to move.
**Structure** — primary (product areas) → section navigation → breadcrumb for
depth → in-page anchors for long content.
**Components** — primary navigation, breadcrumb, tabs.
**Responsive** — one navigation level visible at a time in compact.
**Accessibility** — every navigation region is labelled and distinguishable;
current location is programmatically current.
**Common mistakes** — using tabs for page navigation; breadcrumbs that record
history instead of hierarchy.

## Form layout

**User goal** — understand what is being asked and complete it without
re-reading.
**Structure** — one column; logical grouping with legends; labels above
controls; help text before the control; the primary action last.
**Components** — form field, text input, select, checkbox, radio, switch,
button.
**Responsive** — always single-column in compact; side-by-side only for
genuinely paired values like city and postcode.
**Accessibility** — persistent visible labels; grouped controls have a group
label; required state stated in text.
**Common mistakes** — placeholder-as-label; multi-column forms that break the
reading order; asterisk-only required marking.

## Form submission

**User goal** — submit with confidence and know the outcome.
**Structure** — validate on blur and on submit → disable the submit control
only while the request is in flight → confirm success in place → keep entered
data on failure.
**Components** — button, alert, toast, loading indicator.
**Responsive** — action row is full-width and sticky in compact if the form is
long.
**Accessibility** — busy state announced; on success move focus or announce; on
failure move focus to the summary.
**Common mistakes** — clearing the form on error; a spinner with no accessible
announcement; double submission.

## Validation and error recovery

**User goal** — fix what is wrong quickly.
**Structure** — summary alert at the top listing each error as a link to its
field → inline message at each field → focus the first invalid field.
**Components** — alert, form field.
**Responsive** — the summary stays above the form at every size.
**Accessibility** — errors associated with fields and announced; message says
what to do, not just that something is wrong.
**Common mistakes** — colour-only error indication; validating aggressively as
the user first types; generic "invalid input".

## Loading

**User goal** — know something is happening and roughly how long.
**Structure** — under ~300ms show nothing; short waits get an inline indicator;
predictable layouts get skeletons; known progress gets a determinate bar.
**Components** — loading indicator, skeleton.
**Responsive** — indicators sit within the region that is loading, not over the
whole page.
**Accessibility** — the region is marked busy; one announcement, not one per
skeleton; reduced-motion substitutes for shimmer and spin.
**Common mistakes** — full-page spinners for regional updates; layout shifting
when content lands; fake progress.

## Empty states

**User goal** — understand why nothing is here and what to do.
**Structure** — heading naming the situation → one sentence of explanation →
the action that resolves it.
**Components** — empty state, button.
**Responsive** — centred, width-constrained; illustration optional in compact.
**Accessibility** — real text; the transition into empty is announced after
filtering.
**Common mistakes** — treating "no data yet" and "no matches" the same;
showing an empty state while still loading.

## Success confirmation

**User goal** — know the action worked.
**Structure** — match weight to consequence — inline for minor, toast for
routine, in-page alert or a dedicated view for significant outcomes.
**Components** — toast, alert.
**Responsive** — toasts are bottom-anchored full-width in compact.
**Accessibility** — polite announcement; never rely on a toast alone for
something the user must retain.
**Common mistakes** — a toast for an outcome the user needs a record of.

## Destructive confirmation

**User goal** — avoid losing something irreversibly by accident.
**Structure** — prefer undo over confirm. Where confirmation is genuinely
needed: dialog naming the object and the consequence; confirm button naming the
action; cancel is the safe default.
**Components** — dialog, button, toast (for undo).
**Responsive** — full-screen sheet in compact with actions clearly separated.
**Accessibility** — focus moves into the dialog and returns to the trigger;
consequence is stated in text, not conveyed by red alone.
**Common mistakes** — "Are you sure?" with OK/Cancel; destructive action as the
default focused button; confirming trivial reversible actions.

## Search and filtering

**User goal** — narrow a large set to what I need.
**Structure** — search input → active filters shown as removable badges →
result count → results → empty state when nothing matches.
**Components** — text input (search), badge, select, checkbox, empty state,
pagination.
**Responsive** — filters move into a drawer or sheet in compact, with a clear
"N filters applied" trigger.
**Accessibility** — result count is announced when it changes; applied filters
are visible and individually removable; debounce live results so they are not
announced on every keystroke.
**Common mistakes** — hiding which filters are active; no way to clear all;
results updating silently.

## Dense-data presentation

**User goal** — compare many records efficiently.
**Structure** — table with sticky header and a pinned identifying column;
sorting on meaningful columns; row actions consistent across rows; pagination
or virtualisation for volume.
**Components** — table, pagination, badge, icon button.
**Responsive** — horizontal scroll with a pinned column, or stacked cards.
Never drop columns silently.
**Accessibility** — real table semantics; sort state exposed; row actions
individually named ("Edit invoice 1042", not "Edit").
**Common mistakes** — layout-only tables; hidden columns with no way to see
them; identical accessible names on every row action.

## Responsive navigation

**User goal** — reach any area at any screen size.
**Structure** — persistent navigation while items fit; a drawer below that
threshold, triggered by a labelled control.
**Components** — primary navigation, icon button, dialog behaviour for the
drawer.
**Responsive** — the collapse point is where the content stops fitting, not a
device width.
**Accessibility** — the trigger exposes expanded state; the drawer traps focus
and closes on `Escape`, returning focus to the trigger.
**Common mistakes** — an unlabelled hamburger; navigation hidden behind a menu
on wide viewports; focus lost when the drawer closes.

## Theme selection

**User goal** — use the product in my preferred appearance.
**Structure** — offer light, dark, and "match system"; default to system;
persist the explicit choice; apply before first paint to avoid a flash.
**Components** — radio group or select, switch.
**Responsive** — the control lives in settings, reachable at every size.
**Accessibility** — contrast requirements hold in both themes; the control is a
labelled group; the change is announced or visibly obvious.
**Common mistakes** — a two-state toggle with no way back to system; a flash of
the wrong theme on load; contrast verified in light only.

## Onboarding and first use

**User goal** — reach value quickly without a lecture.
**Structure** — a purposeful empty state beats a tour. Where guidance is
needed, keep it short, skippable, and resumable.
**Components** — empty state, dialog, alert, button.
**Responsive** — never block the whole compact viewport with guidance.
**Accessibility** — fully keyboard operable and dismissible; never traps focus
without an exit; respects reduced-motion.
**Common mistakes** — unskippable multi-step tours; coach marks that break at
small sizes.

## Progressive disclosure

**User goal** — see what I need now, reach the rest when I want it.
**Structure** — show the common path; put advanced options behind a labelled
disclosure; keep defaults safe.
**Components** — disclosure/expand controls, tabs, dialog.
**Responsive** — more content is collapsed by default in compact.
**Accessibility** — the trigger exposes expanded state and controls the region;
content is in the DOM order that matches its visual position.
**Common mistakes** — hiding required fields inside a collapsed section;
disclosure state that is styled but not exposed.

## Reduced-motion behaviour

**User goal** — use the product comfortably without vestibular discomfort.
**Structure** — honour the reduced-motion preference everywhere. Substitute:
large translations and parallax become instant or a short crossfade; looping
ambient motion stops; auto-playing media does not start; essential feedback
stays but shortens toward instant.
**Components** — all animated components.
**Responsive** — the preference applies at every size.
**Accessibility** — the preference is respected without the user losing
information or state feedback — reduced motion means less movement, not less
communication.
**Common mistakes** — treating reduced-motion as "no animation at all" and
removing needed feedback; honouring it for CSS transitions but not for
scripted or scroll-linked motion.

---

## Related

[Components](components/README.md) · [Tokens](tokens/README.md) ·
[Accessibility](accessibility.md) · [Responsive](responsive.md) ·
[Motion](motion/README.md) · [Profiles](profiles.md)
