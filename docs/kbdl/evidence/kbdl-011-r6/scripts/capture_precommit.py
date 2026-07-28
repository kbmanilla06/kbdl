#!/usr/bin/env python3
from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[5];O=R/'docs/kbdl/evidence/kbdl-011-r6/precommit-transcript.txt'
C=[('Fetch origin',['git','fetch','origin']),('Remote',['git','remote','-v']),('Branch',['git','branch','--show-current']),('Tree',['git','status','--short']),('HEAD',['git','rev-parse','HEAD']),('Remote HEAD',['git','rev-parse','origin/main']),('History',['git','log','--oneline','--decorate','-15']),('Baseline',['git','show','--no-patch','--format=fuller','991dfdf']),('Resolve per-ID ledger',['python3','docs/kbdl/evidence/kbdl-011-r6/scripts/resolve_per_id_ledger.py']),('Independent validation',['python3','docs/kbdl/evidence/kbdl-011-r6/scripts/validate_per_id_records.py']),('Documentation validation',['python3','docs/kbdl/evidence/kbdl-011-r1/scripts/repository_documentation_validator.py']),('Whitespace',['git','diff','--check'])]
o=[]
for purpose,cmd in C:
 p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);o += [f'PURPOSE: {purpose}',f'COMMAND: {" ".join(cmd)}','STDOUT:',p.stdout or '(empty)','STDERR:',p.stderr or '(empty)',f'EXIT CODE: {p.returncode}',f'RESULT: {"PASS" if p.returncode==0 else "FAIL"}','']
O.write_text('\n'.join(o));print(f'Captured {len(C)} commands')
