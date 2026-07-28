#!/usr/bin/env python3
"""Capture complete command, stdout, stderr, and exit-code evidence."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[5]
OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r7/precommit-transcript.txt'
commands=[
 'git fetch origin','git remote -v','git branch --show-current','git status --short',
 'git rev-parse HEAD','git rev-parse origin/main','git log --oneline --decorate -15',
 'git show --no-patch --format=fuller bbcc13e0ecaece6b70f0ce678a8cc66b21500d6c',
 'python3 docs/kbdl/evidence/kbdl-011-r5/scripts/build_effective_ledger.py',
 'python3 docs/kbdl/evidence/kbdl-011-r6/scripts/resolve_per_id_ledger.py',
 'python3 docs/kbdl/evidence/kbdl-011-r7/scripts/reconcile_evidence.py',
 'python3 docs/kbdl/evidence/kbdl-011-r7/scripts/validate_effective_traceability.py',
 'python3 docs/kbdl/evidence/kbdl-011-r1/scripts/repository_documentation_validator.py',
 'git diff --check']
parts=[]
for command in commands:
    p=subprocess.run(command,shell=True,cwd=ROOT,text=True,capture_output=True)
    parts += [f'$ {command}', '[stdout]', p.stdout.rstrip() or '(empty)', '[stderr]', p.stderr.rstrip() or '(empty)', f'[exit code] {p.returncode}', '']
OUT.write_text('\n'.join(parts))
print(f'Wrote {OUT.relative_to(ROOT)}')
