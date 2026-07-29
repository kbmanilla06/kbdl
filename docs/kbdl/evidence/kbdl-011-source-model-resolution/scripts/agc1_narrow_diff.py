#!/usr/bin/env python3
"""KBDL-011-SMR1-BH-AGC1-VF1 narrow authorized-diff module.

Root-cause fix for VF1: the three `AG.narrow_authorized_diff.*` checks in
`validate_packet.py` originally compared the *working tree* against the
*symbolic* `HEAD` (`git diff -U0 HEAD -- <file>`). That was meaningful
only pre-commit, when the working tree still held the uncommitted AGC1
correction against the old HEAD. Once the correction was committed and
published (commit `AGC1_TARGET_SHA`, parent `AGC1_BASE_SHA`) and the
working tree became clean, `git diff HEAD` against the new HEAD is empty
for both commits -- so the checks either failed on an empty diff (the
row-count check, added=0 removed=0) or passed vacuously on an empty diff
(the two "only touches MOT-007/008" checks, which are trivially true of
nothing).

This module replaces that design. It inspects the fixed, immutable,
historical commit range `AGC1_BASE_SHA..AGC1_TARGET_SHA` -- never
symbolic `HEAD`, `HEAD^`, the working tree, the index, or "whatever the
latest commit is" -- so the same, correct result is produced regardless
of how many later commits (including this VF1 commit itself) exist on
top of it.

Every check here fails closed: if either commit is unresolvable, if the
target's direct parent is not the expected base, if `git diff` cannot be
run, or if the resulting diff is empty, the relevant check(s) FAIL --
they never report a vacuous PASS.

This module is read-only with respect to whatever repository path it is
given: it only ever runs `git diff`/`git rev-parse`/`git cat-file`
(via explicit argument-array subprocess calls, never shell strings) and
never mutates anything. `agc1_narrow_diff_fixtures.py` exercises it
against temporary, disposable Git repositories it creates and destroys
itself; it never points this module at, or mutates, the real KBDL
repository working tree.
"""
import re
import subprocess

# Immutable AGC1 correction range. These are commit-identity constants,
# not "current HEAD" or "current HEAD's parent" -- they name the exact,
# historical, already-published correction commit and its exact parent,
# and must never be replaced by a symbolic ref.
AGC1_BASE_SHA = "46104c57f86a924b197f6ed380a5b1127eddbf7d"
AGC1_TARGET_SHA = "0fadb9713299fb861830e419e06da8d82175ea1a"

README_PATH = "docs/kbdl/motion/README.md"
CSV_PATH = "docs/kbdl/traceability-metadata.csv"

MOT_OTHER_RE = re.compile(r"KBDL-MOT-(?!007\b|008\b)\d+")


def _git(repo, args):
    """Run git with an explicit argument array (never shell interpolation)
    rooted at `repo`. Returns the CompletedProcess; callers must check
    returncode themselves -- this never raises on a nonzero exit."""
    return subprocess.run(
        ["git", "-C", repo] + args,
        capture_output=True,
        text=True,
    )


def commit_exists(repo, sha):
    r = _git(repo, ["cat-file", "-e", f"{sha}^{{commit}}"])
    return r.returncode == 0


def resolve_parent(repo, sha):
    """Returns (parent_sha_or_None, error_detail)."""
    r = _git(repo, ["rev-parse", f"{sha}^"])
    if r.returncode != 0:
        return None, r.stderr.strip() or f"git rev-parse {sha}^ failed"
    return r.stdout.strip(), ""


def verify_ancestry(repo, base_sha, target_sha):
    """Fail-closed parent check: target's DIRECT parent must be exactly
    base_sha. Not "an ancestor somewhere" -- the exact direct parent, so
    this cannot be satisfied by an unrelated commit that merely descends
    from base_sha."""
    parent, err = resolve_parent(repo, target_sha)
    if parent is None:
        return False, f"could not resolve {target_sha}^: {err}"
    if parent != base_sha:
        return False, f"expected direct parent {base_sha}, found {parent}"
    return True, ""


def diff_added_removed(repo, base_sha, target_sha, path):
    """Returns (added_lines, removed_lines, raw_stdout_or_None, error).
    On any git failure returns (None, None, None, detail) -- callers
    must treat that as a hard FAIL, never as an empty-but-passing diff."""
    r = _git(repo, ["diff", "-U0", "--no-color", f"{base_sha}", f"{target_sha}", "--", path])
    if r.returncode != 0:
        return None, None, None, (r.stderr.strip() or f"git diff exited {r.returncode}")
    raw = r.stdout
    lines = raw.splitlines()
    added = [l[1:] for l in lines if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in lines if l.startswith("-") and not l.startswith("---")]
    return added, removed, raw, ""


def check_narrow_authorized_diff(
    repo,
    base_sha=AGC1_BASE_SHA,
    target_sha=AGC1_TARGET_SHA,
    readme_path=README_PATH,
    csv_path=CSV_PATH,
):
    """Returns the list of (check_name, passed, detail) tuples for the
    three AG.narrow_authorized_diff.* checks, evaluated against the
    immutable commit range `base_sha..target_sha` rather than the
    working tree or symbolic HEAD. Every failure mode below fails
    closed -- there is no path that reports PASS from a missing commit,
    wrong-parent commit, failed git invocation, or empty diff."""
    results = []

    def add(name, ok, detail=""):
        results.append((name, bool(ok), detail))

    base_ok = commit_exists(repo, base_sha)
    target_ok = commit_exists(repo, target_sha)
    add(
        "AG.narrow_authorized_diff.commits_resolvable",
        base_ok and target_ok,
        f"base({base_sha})_exists={base_ok} target({target_sha})_exists={target_ok}",
    )
    if not (base_ok and target_ok):
        reason = "cannot inspect AGC1 range: base and/or target commit unavailable"
        add("AG.narrow_authorized_diff.parent_matches_base", False, reason)
        add("AG.narrow_authorized_diff.readme_only_mot007_008", False, reason)
        add("AG.narrow_authorized_diff.csv_only_mot007_008", False, reason)
        add("AG.narrow_authorized_diff.csv_row_count_unchanged", False, reason)
        return results

    parent_ok, parent_detail = verify_ancestry(repo, base_sha, target_sha)
    add("AG.narrow_authorized_diff.parent_matches_base", parent_ok, parent_detail)
    if not parent_ok:
        reason = f"fail closed: {parent_detail}"
        add("AG.narrow_authorized_diff.readme_only_mot007_008", False, reason)
        add("AG.narrow_authorized_diff.csv_only_mot007_008", False, reason)
        add("AG.narrow_authorized_diff.csv_row_count_unchanged", False, reason)
        return results

    readme_added, readme_removed, readme_raw, readme_err = diff_added_removed(
        repo, base_sha, target_sha, readme_path
    )
    if readme_added is None:
        add(
            "AG.narrow_authorized_diff.readme_only_mot007_008",
            False,
            f"fail closed: git diff failed for {readme_path}: {readme_err}",
        )
    else:
        readme_lines = readme_added + readme_removed
        readme_nonempty = bool(readme_lines)
        other_mot_touched = any(MOT_OTHER_RE.search(l) for l in readme_lines)
        add(
            "AG.narrow_authorized_diff.readme_only_mot007_008",
            readme_nonempty and not other_mot_touched,
            f"nonempty_diff={readme_nonempty} other_mot_requirement_touched={other_mot_touched} "
            f"(range {base_sha}..{target_sha})",
        )

    csv_added, csv_removed, csv_raw, csv_err = diff_added_removed(
        repo, base_sha, target_sha, csv_path
    )
    if csv_added is None:
        reason = f"fail closed: git diff failed for {csv_path}: {csv_err}"
        add("AG.narrow_authorized_diff.csv_only_mot007_008", False, reason)
        add("AG.narrow_authorized_diff.csv_row_count_unchanged", False, reason)
    else:
        csv_lines = csv_added + csv_removed
        csv_other_mot_touched = any(MOT_OTHER_RE.search(l) for l in csv_lines)
        csv_nonempty = bool(csv_lines)
        add(
            "AG.narrow_authorized_diff.csv_only_mot007_008",
            csv_nonempty and not csv_other_mot_touched,
            f"nonempty_diff={csv_nonempty} other_mot_requirement_touched={csv_other_mot_touched} "
            f"(range {base_sha}..{target_sha})",
        )
        add(
            "AG.narrow_authorized_diff.csv_row_count_unchanged",
            len(csv_added) == len(csv_removed) == 2,
            f"expected exactly 2 changed rows (MOT-007, MOT-008); "
            f"added={len(csv_added)} removed={len(csv_removed)} (range {base_sha}..{target_sha})",
        )

    return results
