#!/usr/bin/env python3
from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[5];O=R/'docs/kbdl/evidence/kbdl-011-r5/precommit-transcript.txt'
CMDS=[('Refresh origin',['git','fetch','origin']),('Record remotes',['git','remote','-v']),('Record branch',['git','branch','--show-current']),('Record tree',['git','status','--short']),('Record HEAD',['git','rev-parse','HEAD']),('Record origin/main',['git','rev-parse','origin/main']),('Inspect history',['git','log','--oneline','--decorate','-15']),('Inspect baseline',['git','show','--no-patch','--format=fuller','7c09694']),('Build effective ledger',['python3','docs/kbdl/evidence/kbdl-011-r5/scripts/build_effective_ledger.py']),('Validate effective records',['python3','docs/kbdl/evidence/kbdl-011-r5/scripts/validate_effective_records.py']),('Validate documentation',['python3','docs/kbdl/evidence/kbdl-011-r1/scripts/repository_documentation_validator.py']),('Check whitespace',['git','diff','--check'])]
out=[]
for purpose,cmd in CMDS:
 p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);out += [f'PURPOSE: {purpose}',f'COMMAND: {" ".join(cmd)}','STDOUT:',p.stdout or '(empty)','STDERR:',p.stderr or '(empty)',f'EXIT CODE: {p.returncode}',f'RESULT: {"PASS" if p.returncode==0 else "FAIL"}','']
O.write_text('\n'.join(out));print(f'Captured {len(CMDS)} commands')
