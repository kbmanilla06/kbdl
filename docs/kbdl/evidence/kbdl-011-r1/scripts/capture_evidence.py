#!/usr/bin/env python3
"""Run and capture the complete KBDL-011-R1 validation command transcript."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[5]
OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r1/validation-transcript.txt'
commands=[
 ['git','fetch','origin'], ['git','remote','-v'], ['git','branch','--show-current'],
 ['git','status','--short'], ['git','rev-parse','HEAD'], ['git','rev-parse','origin/main'],
 ['git','log','--oneline','--decorate','-15'], ['git','show','--no-patch','--format=fuller','b5bb0a3'],
 ['git','diff','--check'],
 *[['python3',str(p.relative_to(ROOT))] for p in sorted((Path(__file__).parent).glob('*_validator.py'))]
]
parts=[]; failures=0
for number,command in enumerate(commands,1):
    result=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
    failures += result.returncode != 0
    parts.extend([f'COMMAND {number}: '+subprocess.list2cmdline(command),
                  'PURPOSE: required Git inspection' if command[0]=='git' else 'PURPOSE: reproducible KBDL-011-R1 validation',
                  'STDOUT:',result.stdout.rstrip(),'STDERR:',result.stderr.rstrip(),
                  f'EXIT CODE: {result.returncode}',f'RESULT: {"PASS" if result.returncode==0 else "FAIL"}',''])
OUT.write_text('\n'.join(parts)+'\n')
print(f'Transcript: {OUT.relative_to(ROOT)}')
print(f'Commands: {len(commands)}; failures: {failures}')
raise SystemExit(bool(failures))
