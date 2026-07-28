#!/usr/bin/env python3
"""Capture required R3 pre-commit commands and complete outputs."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[5];OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r3/precommit-transcript.txt'
commands=[['git','fetch','origin'],['git','remote','-v'],['git','branch','--show-current'],['git','status','--short'],['git','rev-parse','HEAD'],['git','rev-parse','origin/main'],['git','log','--oneline','--decorate','-15'],['git','show','--no-patch','--format=fuller','5d4ecd5'],['git','diff','--check'],['python3','docs/kbdl/evidence/kbdl-011-r3/scripts/build_traceability_metadata.py'],['python3','docs/kbdl/evidence/kbdl-011-r3/scripts/validate_traceability_metadata.py'],['python3','docs/kbdl/evidence/kbdl-011-r1/scripts/repository_documentation_validator.py']]
parts=[];fail=0
for i,c in enumerate(commands,1):
 r=subprocess.run(c,cwd=ROOT,text=True,capture_output=True);fail+=r.returncode!=0;parts += [f'COMMAND {i}: '+subprocess.list2cmdline(c),'STDOUT:',r.stdout.rstrip(),'STDERR:',r.stderr.rstrip(),f'EXIT CODE: {r.returncode}',f'RESULT: {"PASS" if r.returncode==0 else "FAIL"}','']
OUT.write_text('\n'.join(parts)+'\n');print(f'Commands: {len(commands)}; failures: {fail}; transcript: {OUT.relative_to(ROOT)}');raise SystemExit(bool(fail))
