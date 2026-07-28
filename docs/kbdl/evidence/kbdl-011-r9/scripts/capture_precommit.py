#!/usr/bin/env python3
from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[5];O=R/'docs/kbdl/evidence/kbdl-011-r9/precommit-transcript.txt'
cmds=['git fetch origin','git remote -v','git branch --show-current','git status --short','git rev-parse HEAD','git rev-parse origin/main','git log --oneline --decorate -15','git show --no-patch --format=fuller e8bc06efd0a6399178213fed28907f370c923176','python3 docs/kbdl/evidence/kbdl-011-r5/scripts/build_effective_ledger.py','python3 docs/kbdl/evidence/kbdl-011-r6/scripts/resolve_per_id_ledger.py','python3 docs/kbdl/evidence/kbdl-011-r8/scripts/reconcile_evidence.py','python3 docs/kbdl/evidence/kbdl-011-r9/scripts/run_full_validation.py','python3 docs/kbdl/evidence/kbdl-011-r9/scripts/documentation_validator.py --root .','git diff --check']
out=[]
for c in cmds:
 p=subprocess.run(c,shell=True,cwd=R,text=True,capture_output=True);out += ['$ '+c,'[stdout]',p.stdout.rstrip() or '(empty)','[stderr]',p.stderr.rstrip() or '(empty)',f'[exit code] {p.returncode}','']
O.write_text('\n'.join(out));print(f'Wrote {O.relative_to(R)}')
