# KBDL-011-SMR2-VC-0001 (reissued) — Implementation Report

Prompt: `KBDL-011-SMR2-VC-0001`, reissued after `KBDL-011-SMR2-FSRG1` passed
planning-agent validation. The earlier blocked version is superseded and was not
resumed.

Baseline commit: `718b0431af9e430a1fe52a88c99b520c1593bfb1`
(parent `ad729c8cee17cac70f6e867d0afdca8901098b71`).

Implementation authorization status: NOT AUTHORIZED

## Root cause

**The value was already `Not verified`.** Both the traceability ledger and the
readable traceability group showed it. What was missing was an *authoritative*
source for it.

**Its normative source parsed as `ABSENT`** because the label was split across a
line wrap in `docs/kbdl/accessibility.md`:

```
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.1.1,
    Level A, and SC 1.4.5, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
```

The field parser looks for `Validation status` followed by a colon. Across the
wrap the text is `Validation\n    status:` — the literal single space in the
pattern cannot match a newline plus indentation, and `Validation` alone is not
followed by a colon either. No match, so the normative value was `ABSENT`.

**The ledger and readable group could not resolve it by themselves** because
`Validation classification` is `A — Normative-owned`. A traceability candidate
is not permitted to prove the field it is a candidate for; treating it as proof
would be exactly the source-model self-proof KBDL-011-SMR1 catalogued. So the
row reported `Authoritative expected value: UNRESOLVED`, `Validation result:
FAIL`, even though the displayed value was correct and uncontested.

**How this resolves it without creating validation evidence.** The approved
owner decision supplies current, non-retroactive *decision authority* for
retaining the classification. Recording that authority in the normative record —
and making the field contiguous so it is independently parseable — lets the
field resolve from its permitted source class. No test was run, no evidence was
created, and the value did not change. Authority and evidence stay separate, and
the requirement's validation method remains unexecuted.

## Metadata architecture determination

Inspection established that the line wrap was the **complete** cause: making the
label contiguous resolves the row with **no generator change**. This was proven
in a sandbox before touching the repository. Two variants were tested:

* **Variant A** used the label `Validation-classification authority:` verbatim.
  It resolved the target row but also caused two unwanted effects: the word
  `authority:` matched the generator's `Authority` field parser, so the
  requirement's *Authority* row began reporting the validation-classification
  decision record as its normative value; and because the edit added lines, the
  `Primary basis` of three unrelated requirements (`KBDL-A11Y-011`, `-021`,
  `-035`) changed, since packet-destination bases carry line numbers.
* **Variant B**, adopted, is **line-count neutral** (three lines replaced by
  three) and uses the label `Validation-classification authority record:`. The
  trailing `record` prevents the `Authority` parser from matching, and the
  neutral line count leaves every packet-destination basis untouched.

Variant B changes exactly the two authorized rows and nothing else. The repo
already contains 30 lines longer than 100 characters (longest 799), so the
longer lines are within existing formatting convention.

## Changes made

### Normative module — `docs/kbdl/accessibility.md`

Only the administrative metadata lines of the `KBDL-A11Y-001` block changed. The
requirement sentence is byte-identical.

Before:

```
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.1.1,
    Level A, and SC 1.4.5, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
```

After:

```
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.1.1, Level A, and SC 1.4.5, Level AA). Provenance: Confirmed.
  - Validation status: Not verified.
  - Validation-classification authority record: `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29` — current and non-retroactive project-owner decision authority for retaining this classification; decision authority only, not validation evidence.
```

Lifecycle, provenance, related requirement, applicable profiles, specification
location, and validation method are unchanged.

### Traceability metadata — `docs/kbdl/traceability-metadata.csv`

One row (`KBDL-A11Y-001`), one field (`Notes or exclusions`), appended:

```
 Validation-classification authority: KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29 — current and non-retroactive decision authority only; not validation evidence.
```

No column added, no column reordered, no other row touched, 21 columns
preserved. The reference is deliberately **not** placed in `Validation
evidence`; the classification stays `Not verified`; the known limitation,
validation method, and lifecycle authority are unchanged.

### Issue register

`SMR1-VC-0001` only: `Authoritative source found` now names the durable record
and its path, qualified as "current, non-retroactive project-owner decision
authority; not validation evidence"; `Resolution status` advances from
`OWNER DECISION RECORDED — AWAITING PLANNING-AGENT VALIDATION` to
`METADATA RECORDED — AWAITING PLANNING-AGENT VALIDATION`. Owner decision, date,
and evidence are unchanged. Exactly one physical line changed, CRLF preserved.

### Live registry

Regenerated through the approved FSRG1 generator; never hand-edited. `--check`
confirms it reproduces byte-for-byte.

## Validation architecture added

* `scripts/validate_smr2_vc_0001.py` — 30 fail-closed checks.
* `scripts/smr2_vc_0001_fixtures.py` — 24 negative fixtures, 6 positive controls.
* `decision_state.py` — the new `METADATA RECORDED — AWAITING PLANNING-AGENT
  VALIDATION` status is permitted **only** when MD1–MD8 all hold, plus new check
  `7e` rejecting any final resolved/closed/verified/validated claim. Existing
  owner-decision checks are unchanged.
* `smr2_vc_0001_integration.py` — nine read-only `VC1.*` checks in the SMR1
  packet validator.

## Scope deviation to report

Two files outside the prompt's Allowed Files list were changed, both forced by
one unavoidable consequence of the authorized edits:

* `docs/kbdl/evidence/kbdl-011-smr2-fsrg1/scripts/validate_fsrg1.py`
* `docs/kbdl/evidence/kbdl-011-source-model-resolution/scripts/fsrg1_integration.py`

FSRG1's `PROT` gate compares a fixed protected-path list against the hard-coded
baseline `dc16473a`, and that list contains exactly the three files this prompt
authorizes changing (`accessibility.md`, `traceability-metadata.csv`,
`issue-register.csv`). Left as written, the gate fails for any authorized
recording, permanently. The change advances the baseline to `718b0431` and adds
an explicitly enumerated `AUTHORIZED_RECORDING_PATHS` exemption.

**It does not weaken the gate.** Every other protected path is still compared
byte-for-byte; a new check, `PROT.authorized_recording_changes_declared`, fails
if anything outside the enumerated set changed; and each exempted path is
validated field-by-field instead — checks 06–17 (normative and traceability
fields), 21–22 (registry scope and counts), 18–19 (sibling issues), plus MD1–MD8.
No schema version, column, domain, row key, sort key, generator behavior, or
historical registry was touched. This is flagged for the planning agent.

## Regression results

Project-wide R16 regression, run into a temporary directory (never into
`kbdl-011-r16/artifacts`, which is byte-identical afterwards):

| Category | Published R16 baseline | Now |
| --- | --- | --- |
| Total defect rows | 693 | 690 |
| `UNRESOLVED_FIELD_SOURCE` | 335 | 333 |
| `CIRCULAR_AUTHORITY` | 1 | 0 |
| `LIMITATION_MISMATCH` | 229 | 229 |
| `LOCATION_MISMATCH` | 63 | 63 |
| `MISSING_STANDARD_BASIS` | 20 | 20 |
| `STANDARD_CLAUSE_MISMATCH` | 20 | 20 |
| `EVIDENCE_MISMATCH` | 14 | 14 |
| `EVIDENCE_SCOPE_RELATIONSHIP` | 11 | 11 |

`KBDL-A11Y-001 / Validation classification` is **no longer** in
`unresolved-field-sources.csv`. Of the two `UNRESOLVED_FIELD_SOURCE` reductions,
one is this recording and one is the earlier `KBDL-011-SMR1-BH-AGC1` authority
correction, which also removed the single `CIRCULAR_AUTHORITY` finding.

`KBDL-A11Y-001` still carries two defect rows — `LIMITATION_MISMATCH` and
`UNRESOLVED_FIELD_SOURCE` for `Known limitation`. Those are `SMR1-KL-0001`,
which remains `PENDING` and is explicitly out of scope.

**Remaining VAL-003 and VAL-006 defects are pre-existing and outside scope.**
VAL-003 and VAL-006 remain `Not verified`; this step does not restore them and
does not claim to.

## What this step did not do

The classification is unchanged. No lifecycle, provenance, validation method,
validation evidence, or known limitation changed. `SMR1-KL-0001` remains
pending. The other 58 Batch A validation-classification issues remain pending.
No decision was created — counts remain 4 durably recorded / 417 pending. No VAL
status, candidate readiness, implementation conformance, or completion status
moved. No R13–R16 artifact, `traceability-matrix.md`, `validation.md`,
`decision-register.md`, owner-decision record, or `project-owner-review.md`
changed. No dependency was added. No implementation is authorized.

## Validation remediation (post-review)

The orchestrator returned **REMEDIATION REQUIRED**, approving the two-file
validator scope expansion as **Required** within an exact boundary, and naming
five remaining items. All five are addressed:

**1. Unlock-map contradiction removed.** The FSRG1 entry asserted both that
planning-agent validation had *passed* and that it *had not occurred*, with a
`Status:` line still reading `LOCKED — PLANNING-AGENT VALIDATION REQUIRED`. The
stale clause is now an explicitly marked historical note, and the status
advances to the sanctioned value `ELIGIBLE FOR FUTURE PROMPT AFTER APPROVAL` —
no fifth vocabulary value was introduced — accompanied by prose stating exactly
what it does not unlock: Batch A stays `LOCKED — OWNER DECISION REQUIRED`, the
other 58 issues stay undecided, `KBDL-011-SMR2-VC-0001` stays `LOCKED` pending
validation of its own recording, no VAL status moved, and no implementation is
authorized.

**2. Fail-closed validation for that exact contradiction.** `fsrg1_roadmap.py`
gains:

* **FR7** — no roadmap entry may claim planning-agent validation passed *and*
  state that the same validation has not occurred / remains pending. A
  historical marker in the same bullet rescues a preserved account of a past
  state; an unmarked current-state claim fails.
* **FR8** — a validated entry must not still demand planning-agent validation,
  and the downstream entry must remain `LOCKED`.
* **FR5**, tightened: the downstream entry must be `LOCKED` always; FSRG1 may
  leave `LOCKED` only while a passed-validation claim is recorded.

Four new fixtures cover the contradiction in both phrasings, the stale
`Status:` line, and an unlocked downstream entry; a third positive control
proves a historically marked past state is still accepted. Fixture 8's premise
had inverted — it asserted FSRG1 must always be `LOCKED`, which stopped being
true once FSRG1 was genuinely validated — so it now tests the meaningful
invariant: unlocked *without* a validation claim must fail. Suite: 17/17.

**3. Exit codes captured verbatim.** Transcript section 15 records the command
and `[exit=0]` for all seven fixture suites: `negative_fixtures`,
`dr1_r1_fixtures`, `authority_graph_fixtures`, `agc1_narrow_diff_fixtures`,
`fsrg1_roadmap_fixtures`, `fsrg1_fixtures`, and `smr2_vc_0001_fixtures` — with
zero nonzero exits anywhere in the section.

**4. Ref equality reconfirmed** from the final remediation commit; see the
Publication table below.

**5. Preservation during remediation.** `git diff --exit-code` against
`4aba456` returns 0 for `accessibility.md`, `traceability-metadata.csv`,
`issue-register.csv`, the live registry, the FSRG1 generator and schema, all
four R13–R16 packages, `traceability-matrix.md`, `validation.md`,
`decision-register.md`, both owner-decision records, and
`project-owner-review.md`. The remediation touched none of them.

Scope: the remediation changed `implementation-unlock-map.md` (already
allowed), `fsrg1_roadmap.py`, and `fsrg1_roadmap_fixtures.py`, plus evidence
records. The two roadmap files are declared in the validator as
`REMEDIATION_AUTHORIZED`, deliberately kept **separate** from
`DECLARED_SCOPE_DEVIATIONS` so the retroactively approved FSRG1 baseline
expansion cannot silently grow; check 31 enforces that separation.

## Status

Metadata is recorded. **Planning-agent validation of this recording is
required.** `SMR1-VC-0001` is `METADATA RECORDED — AWAITING PLANNING-AGENT
VALIDATION` — not resolved, closed, verified, or validated.
