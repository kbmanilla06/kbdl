# Change-Impact Assessment — KBDL-011-SMR1

Non-normative. This assessment classifies **future, not-yet-authorized**
changes that each decision group in `issue-register.csv` could lead to,
if and only if the project owner later approves a specific decision and a
separate remediation prompt implements it. Preparing this assessment adds
nothing to current scope; no classification below is itself a change.

Classification key: **Required** (the decision, however resolved, will
require some documentation change) / **Recommended** (a documentation
change is advisable but a no-op resolution is possible) / **Optional**
(depends entirely on which option the owner selects) / **Future**
(deferred past SMR1's follow-on prompt; not actionable even after owner
approval without further scoping).

## Batch A — Validation-classification authority (59 issues)

- Requirements affected: 59 (see `issue-register.csv`, Category =
  `Validation classification`).
- Modules affected: accessibility, components, governance, motion,
  patterns, responsive (wherever the 59 IDs live).
- Normative metadata impact: **Required** if any ID's classification is
  revised; **Optional** if all 59 are set to Not verified or deferred.
- Governance impact: Recommended — a governance note recording the
  review outcome, distinct from re-approving the requirement itself.
- Validation impact: Required re-run of VAL-003/VAL-006 scoring for any
  ID whose classification changes.
- Traceability impact: Required update to `traceability-metadata.csv`
  candidate value only after a decision is recorded (not by this packet).
- Documentation impact: Optional, per-ID, depending on option chosen.
- Security impact: None identified.
- Accessibility impact: Recommended review for the 7 `KBDL-A11Y-*` IDs in
  this batch specifically, since a classification change affects
  disclosed accessibility conformance claims.
- Implementation impact: None — classification is a documentation/status
  field, not implementation code.
- Roadmap impact: Optional — may inform a future KBDL-011 remediation
  prompt's scope.
- Regression risk: Low per-ID; Moderate in aggregate if resolved without
  individual review (bulk-approval risk called out in
  `project-owner-review.md`).
- Rollback complexity: Low — a single `git revert` of the future
  recording commit restores prior text.
- Documentation-only or runtime-dependent: Documentation-only.

## Batch B — Authority-field sources (21 issues)

- Requirements affected: 21, including `KBDL-MOT-007` (also touched by
  Batch H).
- Modules affected: accessibility, components, motion, responsive.
- Normative metadata impact: **Required** for any REVISE or REJECT
  outcome; authority text is itself normative-adjacent metadata.
- Governance impact: Required — authority-graph edges may need
  regeneration (`authority-graph-audit.csv`, `authority-reference-classification.csv`).
- Validation impact: Required re-run of VAL-003 (lifecycle/authority
  integrity) for every changed ID.
- Traceability impact: Required — `field-source-registry.csv` and
  `approved-authority-population.csv` would need regeneration, not
  hand-editing.
- Documentation impact: Required for REVISE/REJECT outcomes.
- Security/Accessibility impact: None identified beyond the A11Y IDs
  already covered under Batch A.
- Implementation impact: None directly; a rejected authority could,
  later, affect whether a dependent requirement is implementable.
- Roadmap impact: Optional.
- Regression risk: Moderate — authority-graph changes can introduce a
  new cycle if reviewed in bulk (this is the same risk class as the MOT
  cycle in Batch H).
- Rollback complexity: Moderate — reverting an authority-graph
  regeneration requires reverting the generating script's inputs, not
  just the output file.
- Documentation-only or runtime-dependent: Documentation-only.

## Batch C — Validation-evidence mappings (14 issues)

- Requirements affected: 14, spanning accessibility, foundations, themes,
  and the VAL-series requirements themselves.
- Modules affected: accessibility, foundations, themes, validation.
- Normative metadata impact: Optional.
- Governance impact: None identified.
- Validation impact: **Required** — this batch directly gates VAL-004.
- Traceability impact: Required update to evidence citation fields.
- Documentation impact: Required for any REVISE/CONFIRM-SCOPE outcome.
- Security impact: None. Accessibility impact: Recommended review for the
  3 `KBDL-A11Y-*` IDs in this batch.
- Implementation impact: **Future** — any option that requires new
  evidence gathering is implementation-adjacent work not authorized here.
- Roadmap impact: Recommended — likely informs the VAL-004 remediation
  roadmap item directly.
- Regression risk: Low per-ID.
- Rollback complexity: Low.
- Documentation-only or runtime-dependent: Documentation-only for the
  decision itself; any resulting evidence-gathering work would be
  runtime-dependent and is explicitly out of SMR1 scope.

## Batch D — Validation-method sources (12 issues)

- Requirements affected: all 12 `KBDL-VAL-*` requirements.
- Modules affected: validation only.
- Normative metadata impact: Optional.
- Governance impact: None identified.
- Validation impact: **Required** — this batch directly gates VAL-004
  and indirectly affects every other VAL gate whose method is reviewed
  here.
- Traceability impact: Recommended.
- Documentation impact: Required for REVISE outcomes.
- Security/Accessibility impact: None identified.
- Implementation impact: **Future** — several methods are explicitly
  implementation-dependent or belong to VAL-004's locked scope; SMR1 does
  not execute any of them regardless of the owner's eventual choice.
- Roadmap impact: Recommended.
- Regression risk: Low.
- Rollback complexity: Low.
- Documentation-only or runtime-dependent: Mixed — the decision itself is
  documentation-only; several potential follow-on methods are
  runtime-dependent.

## Batch E — Limitation mappings (229 issues)

- Requirements affected: 229 — the majority of the project's requirement
  set, spanning every module.
- Modules affected: accessibility, components, custom, foundations,
  governance, motion, principles, product, responsive, themes,
  validation.
- Normative metadata impact: Optional per-ID; **Required** in aggregate
  if any REVISE/REMOVE option is selected for a widely shared limitation
  string (many of the 229 rows reuse identical limitation text — see
  `limitation-scope-audit.csv`).
- Governance impact: Recommended.
- Validation impact: **Required** — this batch directly gates VAL-005
  and VAL-006.
- Traceability impact: Required.
- Documentation impact: **Required** given the batch size; even a
  DEFER-DECISION outcome across the batch should be recorded as a single
  governance note to avoid re-litigating identical text 229 times.
- Security impact: None. Accessibility impact: Recommended review for
  the `KBDL-A11Y-*` subset (limitation text there discloses WCAG
  conformance boundaries).
- Implementation impact: None directly.
- Roadmap impact: Recommended — this is the largest single blocker to
  VAL-006 and merits its own follow-on prompt.
- Regression risk: **High** if resolved without individual review, given
  the batch size and shared text; **Low** per individually reviewed row.
- Rollback complexity: Low per-ID; Moderate in aggregate.
- Documentation-only or runtime-dependent: Documentation-only.

## Batch F — Exact locations (63 issues)

- Requirements affected: 63, spanning components, custom, foundations,
  governance, principles, product, themes, validation.
- Modules affected: as above.
- Normative metadata impact: **Required** for any REVISE outcome —
  location fields are read by traceability tooling.
- Governance impact: None identified.
- Validation impact: **Required** re-run of VAL-006 (traceability) and
  VAL-007 (anchor resolution) for changed IDs.
- Traceability impact: **Required**.
- Documentation impact: **Required** for REVISE outcomes — anchor
  changes ripple to every cross-reference of the changed section.
- Security/Accessibility impact: None identified.
- Implementation impact: None.
- Roadmap impact: Optional.
- Regression risk: Moderate — anchor changes can silently break
  cross-references elsewhere in the same module; VAL-007's link-integrity
  method would need to be re-run project-wide, not just for the changed
  IDs.
- Rollback complexity: Moderate — anchor reverts must be paired with
  reverting any cross-reference edits made in the same remediation.
- Documentation-only or runtime-dependent: Documentation-only.

## Batch G — Standard-clause mappings (20 issues)

- Requirements affected: 20, spanning accessibility, components,
  responsive.
- Modules affected: accessibility, components, responsive.
- Normative metadata impact: **Required** for CONFIRM/REVISE outcomes —
  standard citations are part of the requirement's authority basis.
- Governance impact: Recommended.
- Validation impact: **Required** re-run of VAL-003 for changed IDs.
- Traceability impact: Recommended.
- Documentation impact: **Required** for any outcome other than DEFER —
  a generic reference either gets an exact clause or an explicit
  supporting/analogy/removed classification.
- Security impact: None. Accessibility impact: **Recommended** — the
  majority of this batch is accessibility-adjacent (WCAG/WAI-ARIA
  citations).
- Implementation impact: None.
- Roadmap impact: Optional.
- Regression risk: Low per-ID.
- Rollback complexity: Low.
- Documentation-only or runtime-dependent: Documentation-only.

## Batch H — MOT-007/MOT-008 authority cycle (3 issues)

- Requirements affected: `KBDL-MOT-007`, `KBDL-MOT-008` directly; related
  by citation: `KBDL-MOT-009`, `KBDL-MOT-033` (share decision packet item
  2 context), `KBDL-MOT-012` (cited alongside MOT-008 in roadmap item 6).
- Modules affected: motion (`timing-easing.md`, `README.md`).
- Normative metadata impact: **Required** if either edge is revised —
  the authority-graph representation for both requirements would change.
- Governance impact: **Required** — `KBDL-DEC-014`'s decision-packet
  mapping table (`motion/README.md` §10.2.1) references item 2 for both
  requirements; any edge revision needs a corresponding governance note,
  not a silent edit.
- Validation impact: **Required** — this is the sole `CIRCULAR_AUTHORITY`
  finding and the only remaining blocker of that specific type for
  VAL-003.
- Traceability impact: Required regeneration of
  `authority-graph-audit.csv` and `authority-cycle-audit.csv` once a
  decision is recorded.
- Documentation impact: Required for any option other than "preserve the
  cycle."
- Security/Accessibility impact: None identified.
- Implementation impact: None — this is a documentation/governance
  relationship, not implementation code; no runtime timing behavior
  exists yet to be affected.
- Roadmap impact: **Recommended** — this is a natural, self-contained
  follow-on prompt once decided.
- Regression risk: **High** if decided without reviewing both edges
  together (could silently orphan one requirement's authority); **Low**
  if reviewed as specified in `project-owner-review.md` Batch H.
- Rollback complexity: Low — `git revert` of the future graph-regeneration
  commit.
- Documentation-only or runtime-dependent: Documentation-only.

## Cross-batch note

91 requirements appear in more than one batch (see
`source-model-resolution-ledger.csv`, "Cross-category dependency count").
Deciding one batch for such a requirement without checking the others can
produce an internally inconsistent effective record. `issue-register.csv`
rows for the same Requirement ID should be reviewed together even when
they fall in different batches.

## What this assessment does not authorize

No item above is Required, Recommended, Optional, or Future in the sense
of being scheduled, scoped, or begun. Every future change described here
remains contingent on (a) an explicit owner decision recorded through a
later prompt, and (b) planning-agent validation of that recording, before
any file changes.
