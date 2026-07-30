# KBDL Tokens

The single active source of KBDL design values is
[`kbdl.tokens.json`](kbdl.tokens.json). It is plain, framework-independent
data: no CSS, no JavaScript, no component library, no product branding. Map it
into whatever your project uses — CSS custom properties, Tailwind config, iOS
or Android resources, Figma variables.

## Naming convention

```
group.subgroup.name
```

* lowercase, dot-separated, hierarchical
* hyphens inside a name segment (`surface-raised`, `heading-1`)
* semantic before literal — prefer `color.text.primary` over `color.neutral.90`
* one meaning per token; no synonyms for the same value

Colors that differ per theme carry `light` and `dark` children:

```
color.text.primary.light   #23252B
color.text.primary.dark    #F5F6F8
```

Primitive ramps (`color.neutral.*`, `color.accent.*`, `color.status.*`) are the
raw palette. **Use semantic tokens in designs and components**; reference
primitives only when defining a new semantic role.

## Token groups

| Group | Purpose |
| --- | --- |
| `color` | Palette primitives plus semantic background, text, border, action, feedback, and selection roles |
| `typography` | Families, weights, sizes, line heights, letter spacing, scale ratios |
| `space` | Spacing scale, multiples of the 4px base unit |
| `size` | Control heights, touch targets, icon sizes |
| `breakpoint` | Named responsive thresholds |
| `container` | Max widths and gutters per breakpoint |
| `radius` | Corner scale |
| `border` | Widths and default style |
| `shadow` | Elevation levels 0–4 |
| `opacity` | Disabled, muted, scrim, and state-overlay values |
| `motion` | Durations, easings, distances, stagger |
| `layer` | Stacking order |
| `focus` | Focus-ring width, offset, style, color |

## Core scales

**Spacing** — base unit `4px`; steps are the approved multiples:

| Token | Value | Use |
| --- | --- | --- |
| `space.1` | 4px | Icon-to-label gap |
| `space.2` | 8px | Tight component-internal spacing |
| `space.3` | 12px | Standard component-internal spacing |
| `space.4` | 16px | Between related controls |
| `space.6` | 24px | Between related content blocks |
| `space.8` | 32px | Section spacing within a page |
| `space.12` | 48px | Major section separation |
| `space.16` | 64px | Macro rhythm for large compositions (Showcase) |

**Type** — body base `16px`; sizes follow the approved ratios (display ≈2.5×,
heading-1 ≈1.9×, heading-2 ≈1.5×, heading-3 ≈1.25×).

**Radius** — `sharp` 0 · `subtle` 4px (controls, inputs) · `standard` 8px
(cards, panels) · `pronounced` 16px (modals, sheets) · `pill` fully rounded
(tags, compact actions).

**Breakpoints** — `compact` 0 · `standard` 600px · `expanded` 905px ·
`wide` 1280px. Named for content behaviour, not devices.

**Motion** — `instant` 0 · `immediate` 100ms · `fast` 150ms · `standard` 240ms
· `deliberate` 320ms · `extended` 480ms, with `standard`, `*-enter`, `*-exit`,
`emphasized-*`, and `direct` easings.

## Where the values come from

Colors, the spacing step ratios, the type scale ratios, the corner
classification, and the motion duration and easing classes are carried forward
from the KBDL foundations and motion documentation.

Some concrete numbers — the 4px base unit, breakpoint pixel values, radius
values, and specific durations within each approved class — were previously
left to implementations. **v1 fixes them as the KBDL default** so the token
file is directly usable. Projects may override them; see
[adoption](../adoption.md).

## Project-controlled

Deliberately adaptable, not defects:

* Type families (v1 ships a system-font stack)
* Brand accent hue, if a project substitutes its own
* Additional semantic roles a product genuinely needs
* Density preference within a profile's stated range

Override by remapping semantic tokens — not by editing primitives in place,
which would break the contrast relationships the palette was built for.

## Contrast responsibilities

`color.text.secondary.light` (`#636872`) is the correct value for ordinary
secondary text: it meets 4.5:1 on white. `color.neutral.50` (`#8A8F99`) does
**not** meet 4.5:1 for normal-size text — reserve it for large text meeting the
WCAG 1.4.3 threshold, non-text boundaries meeting 1.4.11 (3:1), or decorative
use. See [accessibility](../accessibility.md).
