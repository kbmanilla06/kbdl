# Adopting KBDL

KBDL is framework-independent. Implement it in React, Vue, Svelte, Angular,
SwiftUI, Jetpack Compose, plain HTML and CSS, or anything else. KBDL ships
documentation and tokens; you build the components.

## 1. Read the principles

Start with [principles](principles.md) and [STATUS](STATUS.md). The principles
explain *why* KBDL resolves conflicts the way it does, which matters the first
time your product needs something the docs do not literally cover.

## 2. Select a profile

Pick [Showcase, Precision, or Flow](profiles.md) based on what your product
actually is — an expressive brand experience, a dense operational tool, or a
guided consumer flow. The profile sets density, motion intensity, and surface
treatment. It does not change semantics or accessibility requirements.

Products with genuinely distinct areas may use different profiles per area, as
long as navigation and component behaviour stay consistent between them.

## 3. Import or map tokens

Take [`tokens/kbdl.tokens.json`](tokens/kbdl.tokens.json) as your source of
truth and generate whatever your stack consumes — CSS custom properties, a
Tailwind theme, SCSS variables, iOS/Android resources, Figma variables.

Rules that keep this maintainable:

* Generate, do not hand-copy. Re-running the transform should reproduce your
  theme exactly.
* Reference **semantic** tokens (`color.text.primary`) in components, not
  primitives (`color.neutral.90`).
* Keep the light and dark values of a semantic token together; switch themes by
  swapping the resolved set, not by overriding colours per component.
* Record every override in one place (see step 9).

## 4. Apply foundations

Set up global type, spacing, layout containers, radii, elevation, and focus
treatment from [foundations](foundations/README.md) before building any
component. Getting the base rhythm right first prevents per-component
correction later.

## 5. Implement core components

Work through [components](components/README.md) in dependency order — button,
link, form field and inputs, then composites like dialog, tabs, and table.

For each one: native semantics first; all states including disabled, read-only,
loading, and error; keyboard behaviour; visible focus; the accessible name.

## 6. Apply responsive rules

Build mobile-first per [responsive](responsive.md). Use the named breakpoints
(`compact`, `standard`, `expanded`, `wide`) as content thresholds — introduce a
breakpoint where your content stops working, not where a device is rumoured to
be.

## 7. Apply accessibility requirements

Work through [accessibility](accessibility.md) as you build, not as a pass at
the end. Contrast, focus order, keyboard operability, target size, labelling,
error identification, and reduced-motion are all cheaper to build in than to
retrofit.

## 8. Test the product implementation

KBDL cannot verify your product for you. Test the real build:

* keyboard-only, through every flow
* at least one screen reader per target platform
* 200% zoom and 320px-wide reflow
* light and dark themes
* reduced-motion enabled
* automated contrast and semantics checks in CI

**Conformance is a property of your implementation, not of KBDL.** KBDL
provides accessibility design requirements and implementation guidance;
conformance must be verified in each product implementation.

## 9. Document project-specific extensions

Keep one file in your repository recording every deviation: the token
overridden or added, the component varied, what problem it solved, and whether
it is a candidate to contribute upstream. Undocumented drift is what turns a
design language back into a pile of one-off decisions.

## 10. Contribute improvements back

If you solved something generally useful — a missing component, a clearer
accessibility rule, a token gap — propose it via
[governance](governance.md). Bring the problem and the evidence, not just the
solution.

---

## Designer checklist

- [ ] Profile chosen and recorded
- [ ] Type scale, spacing scale, and grid set from tokens
- [ ] Light and dark both designed, not one derived late from the other
- [ ] Contrast checked for text (4.5:1) and non-text boundaries (3:1)
- [ ] Every interactive element has hover, focus, active, disabled, and where
      relevant read-only, loading, and error designs
- [ ] Focus indicator visible on every interactive element in both themes
- [ ] Touch targets meet the minimum
- [ ] Empty, loading, and error states designed — not just the happy path
- [ ] Layouts checked at compact, standard, expanded, and wide
- [ ] Motion has a reduced-motion alternative
- [ ] Any new pattern checked against existing components first

## Developer checklist

- [ ] Tokens generated from `kbdl.tokens.json`, not hand-copied
- [ ] Semantic tokens used in components; primitives only in theme definitions
- [ ] Native elements and semantics used where they exist
- [ ] Keyboard operation complete, including composite widgets
- [ ] Visible focus preserved everywhere; never `outline: none` without a
      replacement
- [ ] Accessible names on all icon-only controls
- [ ] Form labels persistent and associated; errors associated and announced
- [ ] Live regions used with the right politeness
- [ ] Reduced-motion honoured for CSS, scripted, and scroll-linked motion
- [ ] Theme applied before first paint; system preference respected
- [ ] Tested with keyboard, screen reader, 200% zoom, and 320px reflow
- [ ] Extensions documented

---

## Related

[Tokens](tokens/README.md) · [Components](components/README.md) ·
[Patterns](patterns.md) · [Profiles](profiles.md) ·
[Governance](governance.md)
