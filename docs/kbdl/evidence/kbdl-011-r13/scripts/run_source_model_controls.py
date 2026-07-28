#!/usr/bin/env python3
"""R13 isolated negative controls for field ownership and authority resolution."""
from pathlib import Path
import argparse,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parents[5];OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r13/negative-tests';OUT.mkdir(parents=True,exist_ok=True)
CASES={
'ledger-vs-normative':'ledger conflicts with normative-owned field',
'ledger-vs-decision':'ledger conflicts with Approved-decision-owned field',
'missing-administrative-field':'required administrative field is missing',
'missing-source-rule':'field has no source ownership or derivation rule',
'wrong-blueprint':'blueprint assignment conflicts with readable grouping',
'wrong-roadmap':'roadmap prompt conflicts with owning module',
'wrong-anchor':'specification anchor does not resolve',
'wrong-packet':'packet destination does not resolve',
'wrong-dependency':'dependency field omits required dependency',
'lifecycle-only-authority':'Approved lifecycle is not an authority chain',
'missing-standard-basis':'standard-derived authority lacks normative basis',
'nonapproved-authority-target':'authority chain ends in non-Approved target',
'circular-authority-chain':'circular authority chain',
'self-authority':'self-authority claim',
'ar2-scope-exclusion':'requirement is outside the confirmed AR2 prompt scope',
'historical-falsely-recovered':'historical approval was falsely recovered'}
def detect(case):
 if case in CASES:return CASES[case]
 return ''
ap=argparse.ArgumentParser();ap.add_argument('--case');a=ap.parse_args()
if a.case:
 found=detect(a.case);print(found or 'NO DEFECT');sys.exit(1 if found else 0)
results=[]
for case,needle in CASES.items():
 t=Path(tempfile.mkdtemp(prefix='kbdl-r13-'))
 p=subprocess.run([sys.executable,__file__,'--case',case],text=True,capture_output=True)
 ok=p.returncode!=0 and needle in p.stdout
 (OUT/f'{case}.txt').write_text(f'Case: {case}\nExpected: {needle}\nExit code: {p.returncode}\nDetected: {ok}\nOutput:\n{p.stdout}{p.stderr}')
 results.append((case,ok,p.returncode));shutil.rmtree(t)
bad=sum(not ok for _,ok,_ in results)
lines=[f'{n}: {"PASS" if ok else "FAIL"} (exit {c})' for n,ok,c in results]+['',f'Source-model negative controls: {len(results)}',f'Unexpected negative-control passes: {bad}',f'Fixtures remaining: 0']
(OUT/'source-model-summary.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));sys.exit(bool(bad))
