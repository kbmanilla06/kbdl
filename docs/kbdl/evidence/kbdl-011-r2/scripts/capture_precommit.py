#!/usr/bin/env python3
"""Capture required pre-commit commands with separate stdout/stderr/exit code."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[5]; OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r2/precommit-transcript.txt'
commands=[['git','fetch','origin'],['git','remote','-v'],['git','branch','--show-current'],['git','status','--short'],['git','rev-parse','HEAD'],['git','rev-parse','origin/main'],['git','log','--oneline','--decorate','-15'],['git','show','--no-patch','--format=fuller','eab3b41'],['git','diff','--check'],['python3','docs/kbdl/evidence/kbdl-011-r2/scripts/independent_audit.py']]
parts=[]
for i,c in enumerate(commands,1):
 r=subprocess.run(c,cwd=ROOT,text=True,capture_output=True); parts += [f'COMMAND {i}: '+subprocess.list2cmdline(c),'STDOUT:',r.stdout.rstrip(),'STDERR:',r.stderr.rstrip(),f'EXIT CODE: {r.returncode}',f'RESULT: {"PASS" if r.returncode==0 else "FINDINGS REPORTED"}','']
OUT.write_text('\n'.join(parts)+'\n'); print(f'captured {len(commands)} commands to {OUT.relative_to(ROOT)}')
