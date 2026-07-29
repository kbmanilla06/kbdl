#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-AGC1-VF1 regression fixtures for the narrow
authorized-diff commit-range mechanism (`agc1_narrow_diff.py`).

Every fixture below builds its own disposable, temporary Git repository
under `tempfile.mkdtemp()` (via `git init`), makes commits inside it
programmatically, points `agc1_narrow_diff.check_narrow_authorized_diff`
at that temporary repository (never the real KBDL repository), asserts
the expected pass/reject outcome, and then deletes the temporary
repository. This script never runs `git` against, and never mutates,
the real repository at REPO -- it only reads real-repository file
hashes before and after, to prove nothing there changed.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

REPO = "/Users/kbmanilla/Desktop/KBDL"
PKT = f"{REPO}/docs/kbdl/evidence/kbdl-011-source-model-resolution"

sys.path.insert(0, os.path.join(PKT, "scripts"))
import agc1_narrow_diff as nd

REAL_FILES_TO_WATCH = [
    f"{REPO}/docs/kbdl/motion/README.md",
    f"{REPO}/docs/kbdl/traceability-metadata.csv",
    f"{PKT}/scripts/validate_packet.py",
    f"{PKT}/scripts/agc1_narrow_diff.py",
]


def _hash(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def _real_snapshot():
    return {p: _hash(p) for p in REAL_FILES_TO_WATCH if os.path.exists(p)}


README_007 = (
    "# Motion requirements (fixture)\n\n"
    "- **KBDL-MOT-007** Timing classes.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2, "
    "together with KBDL-MOT-008, as one timing system).\n"
)
README_008 = (
    "- **KBDL-MOT-008** Duration recommendations.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2, "
    "together with KBDL-MOT-007, as one timing system).\n"
)
README_009 = (
    "- **KBDL-MOT-009** Unrelated requirement.\n"
    "  - Lifecycle status: Approved (unrelated authority).\n"
)

README_BEFORE = README_007 + README_008 + README_009
README_AFTER_VALID = (
    "# Motion requirements (fixture)\n\n"
    "- **KBDL-MOT-007** Timing classes.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2).\n"
    "  - Related requirement: KBDL-MOT-008 -- related requirement only.\n"
    "- **KBDL-MOT-008** Duration recommendations.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2).\n"
    "  - Related requirement: KBDL-MOT-007 -- related requirement only.\n"
    "- **KBDL-MOT-009** Unrelated requirement.\n"
    "  - Lifecycle status: Approved (unrelated authority).\n"
)
README_AFTER_UNRELATED_TOUCHED = (
    "# Motion requirements (fixture)\n\n"
    "- **KBDL-MOT-007** Timing classes.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2, "
    "together with KBDL-MOT-008, as one timing system).\n"
    "- **KBDL-MOT-008** Duration recommendations.\n"
    "  - Lifecycle status: Approved (per KBDL-DEC-014, decision packet item 2, "
    "together with KBDL-MOT-007, as one timing system).\n"
    "- **KBDL-MOT-009** Unrelated requirement CHANGED.\n"
    "  - Lifecycle status: Approved (unrelated authority, edited).\n"
)

CSV_HEADER = "Requirement ID,Notes\n"
CSV_007_BEFORE = 'KBDL-MOT-007,"together with KBDL-MOT-008, as one timing system"\n'
CSV_008_BEFORE = 'KBDL-MOT-008,"together with KBDL-MOT-007, as one timing system"\n'
CSV_009_BEFORE = 'KBDL-MOT-009,"unrelated row"\n'
CSV_010_BEFORE = 'KBDL-MOT-010,"another unrelated row"\n'

CSV_BEFORE = CSV_HEADER + CSV_007_BEFORE + CSV_008_BEFORE + CSV_009_BEFORE
CSV_AFTER_VALID = (
    CSV_HEADER
    + 'KBDL-MOT-007,"decision packet item 2 only; related requirement KBDL-MOT-008"\n'
    + 'KBDL-MOT-008,"decision packet item 2 only; related requirement KBDL-MOT-007"\n'
    + CSV_009_BEFORE
)
CSV_AFTER_ONE_ROW_ONLY = (
    CSV_HEADER
    + 'KBDL-MOT-007,"decision packet item 2 only; related requirement KBDL-MOT-008"\n'
    + CSV_008_BEFORE
    + CSV_009_BEFORE
)
CSV_AFTER_UNRELATED_ROW_TOUCHED = (
    CSV_HEADER
    + CSV_007_BEFORE
    + CSV_008_BEFORE
    + 'KBDL-MOT-009,"unrelated row CHANGED"\n'
)
CSV_AFTER_ROW_ADDED = CSV_AFTER_VALID + CSV_010_BEFORE
CSV_AFTER_ROW_DELETED = CSV_HEADER + 'KBDL-MOT-007,"decision packet item 2 only; related requirement KBDL-MOT-008"\n'


def _git(repo, *args):
    r = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {args} failed in {repo}: {r.stderr}")
    return r.stdout.strip()


def _init_repo():
    tmp = tempfile.mkdtemp(prefix="agc1-narrow-diff-fixture-")
    _git(tmp, "init", "-q")
    _git(tmp, "config", "user.email", "fixture@example.invalid")
    _git(tmp, "config", "user.name", "AGC1 VF1 Fixture")
    os.makedirs(os.path.join(tmp, "docs", "kbdl", "motion"), exist_ok=True)
    return tmp


def _write(repo, readme_text, csv_text):
    with open(os.path.join(repo, "docs", "kbdl", "motion", "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_text)
    with open(os.path.join(repo, "docs", "kbdl", "traceability-metadata.csv"), "w", encoding="utf-8") as f:
        f.write(csv_text)


def _commit(repo, message):
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def _run(repo, base_sha, target_sha):
    return nd.check_narrow_authorized_diff(
        repo,
        base_sha=base_sha,
        target_sha=target_sha,
        readme_path="docs/kbdl/motion/README.md",
        csv_path="docs/kbdl/traceability-metadata.csv",
    )


def _all_pass(results):
    return len(results) > 0 and all(ok for _, ok, _ in results)


real_snapshot_before = _real_snapshot()

results_log = []


def record(case_name, expected_all_pass, results, extra=""):
    actual_all_pass = _all_pass(results)
    ok = actual_all_pass == expected_all_pass
    results_log.append({
        "case": case_name,
        "expected": "PASS(all)" if expected_all_pass else "REJECT(at least one FAIL)",
        "actual": "PASS(all)" if actual_all_pass else "REJECT(at least one FAIL)",
        "ok": ok,
        "detail": extra or "; ".join(f"{n}={'PASS' if o else 'FAIL'}({d})" for n, o, d in results if not o),
    })
    return ok


# Case 1: valid two-row AGC1-style committed change passes from a clean
# post-commit state.
repo1 = _init_repo()
_write(repo1, README_BEFORE, CSV_BEFORE)
base1 = _commit(repo1, "base")
_write(repo1, README_AFTER_VALID, CSV_AFTER_VALID)
target1 = _commit(repo1, "AGC1-style correction")
record("1. valid 2-row committed change passes clean post-commit", True, _run(repo1, base1, target1))

# Case 2: empty base-to-target diff is rejected.
repo2 = _init_repo()
_write(repo2, README_BEFORE, CSV_BEFORE)
base2 = _commit(repo2, "base")
# allow-empty commit with identical tree -> empty diff vs base
_git(repo2, "commit", "--allow-empty", "-q", "-m", "empty follow-up")
target2 = _git(repo2, "rev-parse", "HEAD")
record("2. empty base..target diff rejected", False, _run(repo2, base2, target2))

# Case 3: a working-tree-only (uncommitted) implementation is rejected as
# insufficient -- dirty working tree, but target_sha == base_sha (HEAD
# has not advanced), so the commit-range diff is still empty.
repo3 = _init_repo()
_write(repo3, README_BEFORE, CSV_BEFORE)
base3 = _commit(repo3, "base")
_write(repo3, README_AFTER_VALID, CSV_AFTER_VALID)  # uncommitted!
record("3. working-tree-only uncommitted change rejected (target==base)", False, _run(repo3, base3, base3))

# Case 4: a change to only one target CSV row is rejected.
repo4 = _init_repo()
_write(repo4, README_BEFORE, CSV_BEFORE)
base4 = _commit(repo4, "base")
_write(repo4, README_AFTER_VALID, CSV_AFTER_ONE_ROW_ONLY)
target4 = _commit(repo4, "only one row changed")
record("4. only-one-CSV-row change rejected", False, _run(repo4, base4, target4))

# Case 5: a change to an unrelated CSV requirement row is rejected.
repo5 = _init_repo()
_write(repo5, README_BEFORE, CSV_BEFORE)
base5 = _commit(repo5, "base")
_write(repo5, README_AFTER_VALID, CSV_AFTER_UNRELATED_ROW_TOUCHED)
target5 = _commit(repo5, "unrelated row touched")
record("5. unrelated CSV requirement row change rejected", False, _run(repo5, base5, target5))

# Case 6: an added or deleted CSV requirement row is rejected.
repo6a = _init_repo()
_write(repo6a, README_BEFORE, CSV_BEFORE)
base6a = _commit(repo6a, "base")
_write(repo6a, README_AFTER_VALID, CSV_AFTER_ROW_ADDED)
target6a = _commit(repo6a, "row added")
ok6a = record("6a. added CSV requirement row rejected", False, _run(repo6a, base6a, target6a))

repo6b = _init_repo()
_write(repo6b, README_BEFORE, CSV_BEFORE)
base6b = _commit(repo6b, "base")
_write(repo6b, README_AFTER_VALID, CSV_AFTER_ROW_DELETED)
target6b = _commit(repo6b, "row deleted")
ok6b = record("6b. deleted CSV requirement row rejected", False, _run(repo6b, base6b, target6b))

# Case 7: an unrelated MOT README change is rejected.
repo7 = _init_repo()
_write(repo7, README_BEFORE, CSV_BEFORE)
base7 = _commit(repo7, "base")
_write(repo7, README_AFTER_UNRELATED_TOUCHED, CSV_AFTER_VALID)
target7 = _commit(repo7, "unrelated MOT README change")
record("7. unrelated MOT README change rejected", False, _run(repo7, base7, target7))

# Case 8: a target commit with the wrong parent is rejected.
repo8 = _init_repo()
_write(repo8, README_BEFORE, CSV_BEFORE)
base8 = _commit(repo8, "base")
# Create a decoy commit NOT descended from base8's intended lineage by
# checking out an orphan branch, so the "target" commit's real parent is
# the decoy rather than base8.
_git(repo8, "checkout", "--orphan", "decoy")
_write(repo8, README_BEFORE, CSV_BEFORE)
decoy8 = _commit(repo8, "decoy base")
_write(repo8, README_AFTER_VALID, CSV_AFTER_VALID)
target8 = _commit(repo8, "correction on top of decoy, not base8")
record("8. wrong-parent target commit rejected", False, _run(repo8, base8, target8))

# Case 9: a missing base or target commit is rejected.
repo9 = _init_repo()
_write(repo9, README_BEFORE, CSV_BEFORE)
base9 = _commit(repo9, "base")
_write(repo9, README_AFTER_VALID, CSV_AFTER_VALID)
target9 = _commit(repo9, "valid correction")
fake_sha = "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef"
record("9a. missing base commit rejected", False, _run(repo9, fake_sha, target9))
record("9b. missing target commit rejected", False, _run(repo9, base9, fake_sha))

# Case 10 (mandatory): the valid historical range still passes when the
# repository HEAD has advanced to a later child commit -- proves the
# validator is no longer tied to symbolic HEAD.
repo10 = _init_repo()
_write(repo10, README_BEFORE, CSV_BEFORE)
base10 = _commit(repo10, "base")
_write(repo10, README_AFTER_VALID, CSV_AFTER_VALID)
target10 = _commit(repo10, "AGC1-style correction")
result_at_target_head = _run(repo10, base10, target10)
ok_before_advance = _all_pass(result_at_target_head)
# Advance HEAD further, simulating this very VF1 commit landing on top.
_write(repo10, README_AFTER_VALID, CSV_AFTER_VALID + 'KBDL-MOT-099,"later unrelated VF1-style commit, not part of AGC1 range"\n')
later_child10 = _commit(repo10, "later VF1-style child commit")
head_now = _git(repo10, "rev-parse", "HEAD")
result_after_advance = _run(repo10, base10, target10)  # same fixed base/target SHAs
ok_after_advance = _all_pass(result_after_advance)
case10_ok = ok_before_advance and ok_after_advance and head_now == later_child10 and head_now != target10
results_log.append({
    "case": "10. historical range still passes after HEAD advances past target (HEAD-independence)",
    "expected": "PASS(all) both before and after HEAD advances, with HEAD != target",
    "actual": f"before_advance_pass={ok_before_advance} after_advance_pass={ok_after_advance} head_moved={head_now != target10}",
    "ok": case10_ok,
    "detail": f"base={base10} target={target10} head_after_advance={head_now}",
})

# Cleanup all temporary repositories.
for repo in (repo1, repo2, repo3, repo4, repo5, repo6a, repo6b, repo7, repo8, repo9, repo10):
    shutil.rmtree(repo, ignore_errors=True)
cleanup_ok = all(not os.path.exists(r) for r in (repo1, repo2, repo3, repo4, repo5, repo6a, repo6b, repo7, repo8, repo9, repo10))

real_snapshot_after = _real_snapshot()
real_unchanged = real_snapshot_before == real_snapshot_after

print("=" * 70)
all_ok = True
for entry in results_log:
    status = "PASS" if entry["ok"] else "FAIL"
    if not entry["ok"]:
        all_ok = False
    print(f"[{status}] {entry['case']}")
    print(f"    expected: {entry['expected']}")
    print(f"    actual:   {entry['actual']}")
    if entry["detail"]:
        print(f"    detail:   {entry['detail']}")
print("=" * 70)
print(f"Temporary fixture repositories cleaned up: {cleanup_ok}")
print(f"Real repository files unchanged after all fixtures: {real_unchanged}")
print(f"All {len(results_log)} narrow-diff fixtures produced the expected pass/rejection: {all_ok}")
print("=" * 70)

sys.exit(0 if (all_ok and cleanup_ok and real_unchanged) else 1)
