#!/usr/bin/env python3
"""SMR1 packet integration for the KBDL-011-SMR2-FSRG1 package.

Narrow integration helper added by the KBDL-011-SMR2-FSRG1 implementation, kept
out of `validate_packet.py` so the same logic can be exercised against
temporary copies and so no existing check in that file is disturbed.

It asserts, from the SMR1 packet's point of view, that:

  FSRG1.package_present            the FSRG1 package and its required files exist
  FSRG1.schema_present             the declared schema document exists
  FSRG1.generator_present          the standalone generator exists
  FSRG1.artifact_present           the live registry artifact exists and is non-empty
  FSRG1.validator_passes           `validate_fsrg1.py` exits 0
  FSRG1.package_checksums_verify   the package's own checksums verify
  FSRG1.historical_registries_unchanged   R13-R16 still match their round digests
  FSRG1.effective_metadata_unchanged      protected/normative files match the baseline
  FSRG1.decision_counts_unchanged  4 recorded / 417 pending
  FSRG1.smr2_vc_0001_locked        the downstream prompt is still LOCKED
  FSRG1.no_val_or_readiness_movement      VAL/readiness/conformance/completion intact

This module is read-only. It never regenerates the live registry, never writes
to any package, and treats a failed sub-invocation as a failure, never a pass.
"""
import csv
import hashlib
import os
import re
import subprocess
import sys

FSRG1_REL = "docs/kbdl/evidence/kbdl-011-smr2-fsrg1"
ARTIFACT_REL = f"{FSRG1_REL}/artifacts/field-source-registry.csv"
GENERATOR_REL = f"{FSRG1_REL}/scripts/field_source_registry.py"
SCHEMA_REL = f"{FSRG1_REL}/field-source-registry-schema.md"
VALIDATOR_REL = f"{FSRG1_REL}/scripts/validate_fsrg1.py"
FIXTURES_REL = f"{FSRG1_REL}/scripts/fsrg1_fixtures.py"

SMR1_REL = "docs/kbdl/evidence/kbdl-011-source-model-resolution"
BASELINE_COMMIT = "dc16473a63e446bd685640e18d64417d120b702e"

HISTORICAL_ROUNDS = ["r13", "r14", "r15", "r16"]
REGISTRY_REL = "docs/kbdl/evidence/kbdl-011-{r}/artifacts/field-source-registry.csv"
INVENTORY_REL = "docs/kbdl/evidence/kbdl-011-{r}/evidence-inventory.csv"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

BASELINE_PROTECTED = [
    "docs/kbdl/traceability-metadata.csv",
    "docs/kbdl/traceability-matrix.md",
    "docs/kbdl/validation.md",
    "docs/kbdl/decision-register.md",
    "docs/kbdl/motion/timing-easing.md",
    "docs/kbdl/motion/README.md",
    "docs/kbdl/accessibility.md",
    "docs/kbdl/governance.md",
    "docs/kbdl/principles.md",
    "docs/kbdl/foundations/README.md",
    "docs/kbdl/themes/README.md",
    "docs/kbdl/responsive.md",
    "docs/kbdl/components-core.md",
    "docs/kbdl/components-system.md",
    "docs/kbdl/profiles.md",
    "docs/kbdl/customization.md",
    f"{SMR1_REL}/issue-register.csv",
    f"{SMR1_REL}/project-owner-review.md",
    f"{SMR1_REL}/batch-h-owner-decision-record.md",
    f"{SMR1_REL}/batch-a-smr1-vc-0001-owner-decision-record.md",
]

REQUIRED_PACKAGE_FILES = [
    "README.md",
    "field-source-registry-schema.md",
    "implementation-report.md",
    "evidence-manifest.md",
    "evidence-inventory.csv",
    "checksums.sha256",
    "fsrg1-validation-transcript.txt",
    "artifacts/field-source-registry.csv",
    "scripts/field_source_registry.py",
    "scripts/validate_fsrg1.py",
    "scripts/fsrg1_fixtures.py",
]

EXPECTED_RECORDED = 4
EXPECTED_PENDING = 417


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)


def _recorded_digest(repo, round_name):
    inv = os.path.join(repo, INVENTORY_REL.format(r=round_name))
    rel = REGISTRY_REL.format(r=round_name)
    if not os.path.isfile(inv):
        return None
    with open(inv, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or rel not in row[0]:
                continue
            digests = [x.strip() for x in row if SHA256_RE.match(x.strip())]
            return digests[0] if len(digests) == 1 else None
    return None


def compute(repo):
    """Return a list of (name, ok, detail) checks in validate_packet's shape."""
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))
        return bool(ok)

    pkg = os.path.join(repo, FSRG1_REL)
    missing = [f for f in REQUIRED_PACKAGE_FILES
               if not os.path.isfile(os.path.join(pkg, f))]
    package_ok = check("FSRG1.package_present — FSRG1 package and required files exist",
                       os.path.isdir(pkg) and not missing, f"missing={missing}")

    check("FSRG1.schema_present — declared registry schema document exists",
          os.path.isfile(os.path.join(repo, SCHEMA_REL)))
    check("FSRG1.generator_present — standalone deterministic generator exists",
          os.path.isfile(os.path.join(repo, GENERATOR_REL)))

    artifact = os.path.join(repo, ARTIFACT_REL)
    artifact_ok = os.path.isfile(artifact) and os.path.getsize(artifact) > 0
    check("FSRG1.artifact_present — live field-source registry artifact exists and is non-empty",
          artifact_ok, f"path={ARTIFACT_REL}")

    # The FSRG1 validator must pass. Its own fixture suite is skipped here to
    # avoid running the fixtures twice per packet validation; the fixture suite
    # is a separate required command in the FSRG1 transcript.
    if package_ok:
        result = subprocess.run(
            [sys.executable, os.path.join(repo, VALIDATOR_REL),
             "--repo-root", repo, "--skip-fixtures"],
            capture_output=True, text=True)
        tail = (result.stdout.strip().splitlines() or ["<no output>"])[-1]
        fails = [ln for ln in result.stdout.splitlines() if ln.startswith("[FAIL]")]
        check("FSRG1.validator_passes — validate_fsrg1.py exits 0 with no failed gate",
              result.returncode == 0 and not fails,
              f"rc={result.returncode} last={tail} failed={fails[:3]}")
    else:
        check("FSRG1.validator_passes — validate_fsrg1.py exits 0 with no failed gate",
              False, "package incomplete; validator not run")

    sums = os.path.join(pkg, "checksums.sha256")
    if os.path.isfile(sums):
        bad = []
        with open(sums, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                digest, _, rel = line.rstrip("\n").partition("  ")
                target = os.path.join(repo, rel)
                if not os.path.isfile(target):
                    bad.append(f"MISSING:{rel}")
                elif _sha256(target) != digest:
                    bad.append(f"MISMATCH:{rel}")
        check("FSRG1.package_checksums_verify — FSRG1 checksums verify on disk",
              not bad, f"{bad[:5]}")
    else:
        check("FSRG1.package_checksums_verify — FSRG1 checksums verify on disk",
              False, "checksums.sha256 absent")

    hist_bad = []
    for r in HISTORICAL_ROUNDS:
        path = os.path.join(repo, REGISTRY_REL.format(r=r))
        recorded = _recorded_digest(repo, r)
        if recorded is None:
            hist_bad.append((r, "no recorded digest"))
        elif not os.path.isfile(path):
            hist_bad.append((r, "registry missing"))
        elif _sha256(path) != recorded:
            hist_bad.append((r, "digest mismatch"))
    check("FSRG1.historical_registries_unchanged — R13-R16 match their own round digests",
          not hist_bad, f"{hist_bad}")

    diff = _git(repo, "diff", "--name-only", BASELINE_COMMIT, "--", *BASELINE_PROTECTED)
    changed = [x for x in diff.stdout.splitlines() if x.strip()]
    check("FSRG1.effective_metadata_unchanged — protected/normative files match the baseline",
          diff.returncode == 0 and not changed,
          f"rc={diff.returncode} changed={changed}")

    hist_diff = _git(repo, "diff", "--name-only", BASELINE_COMMIT, "--",
                     *[f"docs/kbdl/evidence/kbdl-011-{r}" for r in HISTORICAL_ROUNDS])
    changed_hist = [x for x in hist_diff.stdout.splitlines() if x.strip()]
    check("FSRG1.historical_packages_unchanged — no R13-R16 evidence file changed",
          hist_diff.returncode == 0 and not changed_hist, f"changed={changed_hist}")

    sys.path.insert(0, os.path.join(repo, SMR1_REL, "scripts"))
    try:
        import decision_state
        _c, stats = decision_state.compute(os.path.join(repo, SMR1_REL))
        check("FSRG1.decision_counts_unchanged — 4 durably recorded / 417 pending",
              stats["recorded_count"] == EXPECTED_RECORDED
              and stats["pending_count"] == EXPECTED_PENDING,
              f"recorded={stats['recorded_count']} pending={stats['pending_count']}")
    except Exception as exc:  # fail closed
        check("FSRG1.decision_counts_unchanged — 4 durably recorded / 417 pending",
              False, f"{type(exc).__name__}: {exc}")

    unlock_path = os.path.join(repo, SMR1_REL, "implementation-unlock-map.md")
    unlock = open(unlock_path, encoding="utf-8").read() if os.path.isfile(unlock_path) else ""
    section = ""
    for chunk in unlock.split("\n## "):
        if "KBDL-011-SMR2-VC-0001" in chunk.split("\n", 1)[0]:
            section = chunk
    statuses = re.findall(r"Status:\s*`([^`]+)`", section)
    check("FSRG1.smr2_vc_0001_locked — the downstream prompt remains LOCKED and reissue-only",
          bool(statuses) and all(s.startswith("LOCKED") for s in statuses)
          and bool(re.search(r"(?i)reissued", section)),
          f"statuses={statuses}")

    val_path = os.path.join(repo, "docs/kbdl/validation.md")
    flat = " ".join(open(val_path, encoding="utf-8").read().split()) if os.path.isfile(val_path) else ""
    state_ok = all(s in flat for s in (
        "Specification release candidate recommendation: NOT READY",
        "Implementation conformance status: NOT VERIFIED",
        "Project completion status: PENDING",
        "`KBDL-VAL-003`, `KBDL-VAL-004`, `KBDL-VAL-005`, and `KBDL-VAL-006` are `Not verified`",
    ))
    check("FSRG1.no_val_or_readiness_movement — VAL/readiness/conformance/completion intact",
          state_ok, "a VAL, readiness, conformance, or completion declaration changed")

    return checks
