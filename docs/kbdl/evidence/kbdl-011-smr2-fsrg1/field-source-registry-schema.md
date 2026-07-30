# Live Field-Source Registry — Schema Contract

**Schema version: 1**

This document is the declared contract for
`artifacts/field-source-registry.csv`, the live current-state field-source
registry produced by `scripts/field_source_registry.py`. The generator mirrors
this contract in `SCHEMA_VERSION`, `COLUMNS`, and `FIELD_SPEC`;
`scripts/validate_fsrg1.py` enforces it fail-closed.

**The live registry is a derived, non-authoritative description of the current
source model. It is not itself authority, a normative source, validation
evidence, an owner-decision record, or implementation authorization.** It never
appears in the KBDL source-of-truth hierarchy, and it is never an input to its
own generation.

This schema is independently versioned. It reuses the *shape* of the R13–R16
round registries so the two remain comparable, but it does not inherit,
redefine, or correct them: those four artifacts remain immutable point-in-time
audit evidence under their own rounds' schemas.

## 1. Encoding and file format

| Property | Value |
| --- | --- |
| Encoding | UTF-8, no byte-order mark |
| Line ending | `\n` (LF) on every line, including the last |
| Final newline | Required |
| Format | RFC 4180 CSV as produced by Python's `csv` module |
| Quoting | `csv.QUOTE_MINIMAL` — a field is quoted only when it contains `,`, `"`, `\r`, or `\n` |
| Escaping | An embedded `"` is doubled (`""`) |
| Header | Required, exactly once, as the first line |
| Empty file | Prohibited; at least one data row is required |

## 2. Columns

Exactly fifteen columns, in exactly this order. No extra column, no missing
column, and no reordering is permitted.

| # | Column | Meaning |
| --- | --- | --- |
| 1 | `Requirement ID` | The requirement this row describes, parsed from its normative record. |
| 2 | `Field name` | Which field of that requirement this row describes. Domain in §4. |
| 3 | `Ownership class` | Which source class owns this field. Domain in §5.1. |
| 4 | `Primary basis` | The specific basis the generator used to resolve this cell (free text, derived — never hand-authored). |
| 5 | `Derivation rule` | The declared rule for this field, fixed per field name by §4. |
| 6 | `Authoritative expected value` | The value an independent authoritative source supports, or `UNRESOLVED`. |
| 7 | `Normative value` | The value parsed from the normative requirement record, or `ABSENT`. |
| 8 | `Governance resolution` | `PASS`/`FAIL` — governance-owned fields must resolve. §5.2. |
| 9 | `Ledger value` | The candidate value in `traceability-metadata.csv`. Candidate only; never authoritative. |
| 10 | `Readable-group value` | The value the readable traceability group maps to this ID, or `MISSING`. |
| 11 | `Readable-group classification` | How that group value was parsed. Domain in §5.3. |
| 12 | `Effective value` | The value in effect given precedence, or `UNRESOLVED`. Equals column 6 by construction. |
| 13 | `Precedence result` | `PASS`/`FAIL` — whether a higher source conflicts with a lower one. §5.2. |
| 14 | `Conflict result` | `None`, or a description of the detected conflict. §5.4. |
| 15 | `Validation result` | `PASS`/`FAIL` — the row-level result. §6. |

## 3. Row key, sort key, duplicates, coverage

* **Row key:** `(Requirement ID, Field name)`. Unique across the whole file.
* **Duplicate policy:** any repeated row key is a schema violation. The
  generator cannot emit one (it iterates each requirement once and each field
  once); the validator rejects one if present.
* **Sort key:** `Requirement ID` ascending (byte order), then `Field name` in
  the declared §4 order — *not* alphabetically. Row order is fully determined;
  it never depends on dictionary, filesystem, or glob iteration order.
* **Coverage:** every requirement with a current normative record appears
  exactly once for every one of the seventeen field names. The row count is
  therefore `requirements × 17` exactly.

## 4. `Field name` domain and per-field derivation rule

Exactly these seventeen values, in this order. This is a closed domain; no
wildcard or free-text field name is permitted.

| # | Field name | Ownership class | Derivation rule |
| --- | --- | --- | --- |
| 1 | `Requirement ID` | A — Normative-owned | Parse the ID from the normative record |
| 2 | `Blueprint section` | C — Traceability-owned administrative | Parse exact group heading or explicit per-ID mapping |
| 3 | `Roadmap prompt` | C — Traceability-owned administrative | Derive base prompt from module/file and validate any remediation annotation |
| 4 | `Specification location` | A — Normative-owned | Derive file and containing heading anchor around the requirement record |
| 5 | `Lifecycle status` | A — Normative-owned | Parse explicit lifecycle and compare every lower source |
| 6 | `Provenance` | A — Normative-owned | Parse explicit provenance and compare every lower source |
| 7 | `Validation classification` | A — Normative-owned | Parse explicit validation status and compare every lower source |
| 8 | `Verified scope` | D — Evidence-owned | Require evidence-compatible scope |
| 9 | `Not-verified scope` | D — Evidence-owned | Require honest unexecuted scope |
| 10 | `Authority` | B — Governance-owned | Resolve every component and graph edge |
| 11 | `Validation method` | D — Evidence-owned | Compare method to evidence classification without ledger self-proof |
| 12 | `Validation evidence` | D — Evidence-owned | Resolve paths and prevent unsupported execution claims |
| 13 | `Known limitation` | D — Evidence-owned | Require consistency with validation scope |
| 14 | `Packet or tracking destination` | C — Traceability-owned administrative | Resolve file section item owner and readiness class |
| 15 | `Pending dependencies` | C — Traceability-owned administrative | Resolve and classify dependency source |
| 16 | `Related decision` | B — Governance-owned | Resolve every cited decision and status |
| 17 | `Notes or exclusions` | C — Traceability-owned administrative | Reject unsupported promotion or completion claims |

`Ownership class` and `Derivation rule` are a fixed function of `Field name`.
A row whose pair disagrees with this table is a schema violation.

## 5. Controlled value domains

### 5.1 `Ownership class`

```
A — Normative-owned
B — Governance-owned
C — Traceability-owned administrative
D — Evidence-owned
```

### 5.2 `Governance resolution`, `Precedence result`, `Validation result`

```
PASS
FAIL
```

`Governance resolution` is `FAIL` only when a governance-owned field
(`Authority`, `Related decision`) failed to resolve; it is `PASS` for every
other field by construction. `Precedence result` is `FAIL` exactly when
`Conflict result` is not `None`.

### 5.3 `Readable-group classification`

```
Exact per-ID mapping
Uniform default
Non-overriding summary
Unresolved
Missing
```

`Unresolved` means a status bucket exists in the group but does not resolve
this member; it is a defect state, retained rather than silently repaired.

### 5.4 `Conflict result`

Either the literal `None`, or one of:

* `normative=<value>; ledger=<value>` — a normative-owned field disagrees with
  the ledger candidate.
* `group/ledger mismatch` — an overriding readable-group value disagrees with
  the ledger candidate.
* `roadmap mismatch` — the ledger roadmap prompt does not match the derived one.

### 5.5 Null, missing, absent, unresolved, and not-applicable

There is no empty-string convention in this registry. Each absence has one
explicit spelling:

| Situation | Column | Representation |
| --- | --- | --- |
| No independent authoritative source resolves the field | 6, 12 | `UNRESOLVED` |
| The normative record carries no such labelled field | 7 | `ABSENT` |
| The readable group maps no value to this ID | 10 | `MISSING` |
| The readable group was not parsed for this field | 11 | `Missing` |
| No conflict detected | 14 | `None` |
| Ledger cell is genuinely empty | 9 | empty string (the ledger's own state, reproduced verbatim) |

`Not applicable` appears only as a *validation classification value* inside
columns 6, 7, 9, 10, or 12 — it is a KBDL domain value, not a null marker.

`UNRESOLVED` is a factual statement that no authoritative source was found. It
must never be repaired by copying the ledger or readable-group value into it:
doing so would let a candidate source prove itself.

## 6. `Validation result` policy

`Validation result` is `PASS` when, and only when, the row has a resolved
`Authoritative expected value` **and** `Conflict result` is `None`. Any
unresolved source or any detected conflict yields `FAIL`.

`FAIL` rows are expected and are not defects in the registry: they are the
registry honestly reporting unresolved source model state, which is exactly
what KBDL-011-SMR1 catalogued. The registry never suppresses, downgrades, or
auto-repairs a `FAIL`.

## 7. Determinism requirements

The emitted bytes are a pure function of repository content. The file must not
contain, and the generator must never emit:

* a timestamp, date, or clock value
* a hostname, username, or process ID
* an absolute filesystem path
* a random or hash-seeded value
* locale-dependent number, case, or collation formatting
* `\r\n` line endings

The source-model commit SHA is deliberately **not** a column: it is recorded in
the package evidence records instead, so the artifact stays identical across
regenerations of the same tree.

## 8. Schema-version policy

`SCHEMA_VERSION` is `1`.

* Adding, removing, reordering, or renaming a column is a **breaking** change
  and requires a version increment plus a schema-document revision.
* Adding a value to a controlled domain (§5) is a breaking change.
* Adding a `Field name` to the §4 domain is a breaking change.
* Widening free-text content in `Primary basis` or `Conflict result` is not.

A version increment never rewrites a previously published registry: prior
artifacts stay as published, under the schema version they were emitted with.
This registry is versioned independently of the R13–R16 round registries, which
are frozen historical evidence and are never migrated to this schema.
