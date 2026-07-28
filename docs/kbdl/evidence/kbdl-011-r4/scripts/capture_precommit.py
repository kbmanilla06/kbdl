#!/usr/bin/env python3
"""Capture exact R4 precommit commands, streams, and exit codes."""
from pathlib import Path
import subprocess
REPO=Path(__file__).resolve().parents[5]; OUT=REPO/'docs/kbdl/evidence/kbdl-011-r4/precommit-transcript.txt'
commands=[
 ('Refresh remote state',['git','fetch','origin']),('Identify remotes',['git','remote','-v']),('Identify branch',['git','branch','--show-current']),
 ('Inspect worktree',['git','status','--short']),('Record HEAD',['git','rev-parse','HEAD']),('Record remote HEAD',['git','rev-parse','origin/main']),
 ('Inspect recent history',['git','log','--oneline','--decorate','-15']),('Inspect immutable baseline',['git','show','--no-patch','--format=fuller','d7108bd']),
 ('Generate direct-authority ledger',['python3','docs/kbdl/evidence/kbdl-011-r4/scripts/generate_authoritative_ledger.py']),
 ('Run independent validator',['python3','docs/kbdl/evidence/kbdl-011-r4/scripts/validate_authoritative_ledger.py']),
 ('Check patch whitespace',['git','diff','--check'])]
parts=[]
for purpose,cmd in commands:
    p=subprocess.run(cmd,cwd=REPO,text=True,capture_output=True)
    parts += [f'PURPOSE: {purpose}',f'COMMAND: {" ".join(cmd)}','STDOUT:',p.stdout or '(empty)','STDERR:',p.stderr or '(empty)',f'EXIT CODE: {p.returncode}',f'RESULT: {"PASS" if p.returncode==0 else "FAIL"}','']
OUT.write_text('\n'.join(parts))
print(f'Captured {len(commands)} commands in {OUT.relative_to(REPO)}')
