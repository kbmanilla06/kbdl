# Owner-Decision Brief — SMR1-VC-0002 (KBDL-A11Y-004)

**This brief is informational. It records no decision, selects no option, and
changes no metadata.** It exists so the project owner can review one issue with
the facts in front of them. Every choice below is unselected, and
`SMR1-VC-0002`'s owner fields remain literally `PENDING`.

Implementation authorization status: NOT AUTHORIZED

## 1. Confirmed facts

| | |
| --- | --- |
| Resolution issue | `SMR1-VC-0002` |
| Requirement | `KBDL-A11Y-004` |
| Field | Validation classification |
| Candidate value | `Not verified` |
| Candidate source | `traceability-metadata.csv` — candidate only |
| Ownership class | `A — Normative-owned` |
| Independent authoritative source found | **None** |
| Current defect | `UNRESOLVED_FIELD_SOURCE` |
| Affected gates | VAL-003, VAL-006 |
| Live-registry result | `Authoritative expected value: UNRESOLVED`, `Normative value: ABSENT`, `Validation result: FAIL` |
| Owner decision / date / evidence | `PENDING` / `PENDING` / `PENDING` |
| Resolution status | `SOURCE EVIDENCE REQUIRED` |

The requirement itself: *Every page **must** have a descriptive title; heading
levels **must** reflect actual hierarchy; landmarks **must** be programmatically
identifiable.* Lifecycle `Approved`, provenance `Confirmed`.

Validation method: **`Automated static check + manual review once implemented`.**
Validation evidence states that this method **has not been executed**.

Related known-limitation issue: **`SMR1-KL-0004`** (same requirement) — still
`PENDING`, and explicitly outside this review.

## 2. Why the issue exists

The normative block in `docs/kbdl/accessibility.md` displays `Not verified`, but
the label is split across a line wrap:

```
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.2,
    Level A, and SC 2.4.6, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
```

The live generator looks for `Validation status` followed by a colon; across the
wrap the text is `Validation\n    status:`, which does not match. The normative
field is therefore not independently parsed, and the registry reports it as
`ABSENT` / `UNRESOLVED`.

Because `Validation classification` is **normative-owned**, the ledger and the
readable traceability group cannot resolve it. Both already show `Not verified`,
but a candidate source may not prove the field it is a candidate for — that is
the source self-proof the SMR1 audit exists to prevent.

**Formatting alone does not authorize a correction.** Making the label
contiguous makes the field *parseable*; it does not supply the *authority* the
field is missing. That authority is what this decision is about. A reformat
without a recorded owner decision would resolve the row on the strength of a
candidate value, which is precisely what is prohibited.

## 3. Available owner choices

Exactly five. None is selected.

### 3.1 `PROVIDE ORIGINAL OR APPROVED SOURCE`

* **Effect** — an existing approved source becomes the field's authority; the
  classification derives from it rather than from a new decision.
* **Evidence needed** — the actual approval or governance record: a decision
  entry, an approved prompt, or dated owner approval naming this requirement's
  classification.
* **Non-retroactive boundary** — this is the *only* option that could establish
  historical authority, and only if the evidence genuinely predates and covers
  the classification. Nothing may be reconstructed or inferred.
* **Validation-evidence implications** — none. A source for the *classification*
  is not evidence that the *validation method* ran.
* **Later recording** — a separate metadata-recording prompt plus its own
  planning-agent validation would still be required.
* **Risk / trade-off** — strongest outcome if the evidence exists; blocks
  indefinitely if it does not. Producing nothing is a legitimate answer here.

### 3.2 `CONFIRM CURRENT CLASSIFICATION AS NEW CURRENT AUTHORITY`

* **Effect** — the owner adopts `Not verified` as a current decision, making the
  classification authoritative from now on.
* **Evidence needed** — none beyond the owner's decision itself.
* **Non-retroactive boundary** — current-dated only. It does not assert the
  classification was ever previously approved.
* **Validation-evidence implications** — none created.
* **Later recording** — separate recording prompt and validation required.
* **Risk / trade-off** — substantively identical in outcome to §3.4 for this
  issue, since the confirmed value *is* `Not verified`; §3.4 states the
  conservative intent more plainly and is the recommended phrasing.

### 3.3 `REVISE CLASSIFICATION`

* **Effect** — the classification changes to a different value (`Verified`,
  `Not applicable`, or a mixed value).
* **Evidence needed** — for `Verified`, executed evidence for the stated method:
  an automated static check plus manual review, against a real implementation.
  For `Not applicable`, a reasoned basis that no meaningful method applies.
* **Non-retroactive boundary** — a revision is current-dated and cannot
  retroactively assert a past state.
* **Validation-evidence implications** — **`Verified` is not available on the
  current record.** No implementation exists and the method has not run;
  selecting it would fabricate validation evidence.
* **Later recording** — separate recording prompt and validation required, and
  for `Verified` an evidence-gathering engagement first.
* **Risk / trade-off** — highest risk. Overstates conformance if chosen without
  executed evidence.

### 3.4 `SET TO NOT VERIFIED`

* **Effect** — the classification is retained as `Not verified`, backed by a
  new, current, non-retroactive project-owner decision that supplies the
  missing authority.
* **Evidence needed** — none beyond the decision.
* **Non-retroactive boundary** — creates current authority only; asserts no
  historical approval and does not claim the value was ever anything else.
* **Validation-evidence implications** — **none.** This is decision authority
  only. It is not evidence that accessibility testing, screen-reader testing,
  automated checking, or WCAG conformance assessment occurred.
* **Later recording** — a separate metadata-recording prompt and its own
  planning-agent validation are required before the decision has any effect in
  normative or traceability metadata.
* **Risk / trade-off** — the most conservative option. It resolves the source
  defect without asserting anything untrue. It does not improve conformance and
  does not move VAL-003 or VAL-006 by itself.

### 3.5 `DEFER DECISION`

* **Effect** — the issue stays `PENDING`; nothing changes.
* **Evidence needed** — none.
* **Non-retroactive boundary** — not applicable.
* **Validation-evidence implications** — none.
* **Later recording** — none; no prompt becomes eligible.
* **Risk / trade-off** — zero risk, zero progress. VAL-003 and VAL-006 stay
  blocked by this issue among others.

## 4. Recommended starting answer

**`SET TO NOT VERIFIED`** — recommended, **not approved and not selected.**

Reasoning:

* No independent authoritative source is currently recorded for this field.
* The stated validation method has not been executed, so no stronger
  classification is truthfully available.
* It preserves the conservative classification already displayed.
* It claims no conformance and creates no validation evidence.
* It avoids ledger/readable-group self-proof by supplying real decision
  authority instead of promoting a candidate value.

Selecting this option would create **new current, non-retroactive project-owner
authority for retaining `Not verified`**. It would **not** create validation
evidence and would **not** reconstruct historical authority.

This recommendation carries no weight until the owner selects it. The owner may
choose any of the five options, and choosing differently is not an error.

## 5. Unresolved — for the owner only

* Whether the owner holds an approved source for this classification that the
  repository does not record (§3.1).
* Whether the owner wants a different classification than `Not verified`.
* The owner's final choice.

These cannot be answered from the repository. No answer is assumed here.

## 6. Prohibited outcomes

This brief does not, and no downstream step may on its strength alone:

* automatically select any option;
* bulk-approve Batch A or any group of issues;
* record metadata for `KBDL-A11Y-004`;
* regenerate the live field-source registry;
* restore `KBDL-VAL-003` or `KBDL-VAL-006`;
* authorize implementation;
* resolve `SMR1-KL-0004`.

`SMR1-VC-0002` remains entirely pending. Batch A remains
`LOCKED — OWNER DECISION REQUIRED`. No metadata-recording prompt for this issue
is released, approved, ready, or eligible.
