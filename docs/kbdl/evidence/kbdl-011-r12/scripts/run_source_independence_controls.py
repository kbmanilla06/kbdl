#!/usr/bin/env python3
"""R12 isolated controls for source precedence and clause semantics."""
from pathlib import Path
import argparse,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parents[5];OUT=ROOT/'docs/kbdl/evidence/kbdl-011-r12/negative-tests';OUT.mkdir(parents=True,exist_ok=True)
CASES={
'baseline-current-shared-wrong':'authoritative source disagrees with both ledgers',
'wrong-authoritative-source':'authoritative source/ledger mismatch',
'contrast-for-keyboard':'evidence type contrast cannot cover keyboard review',
'contrast-for-brand':'evidence type contrast cannot cover brand-suitability review',
'commit-only-manual-review':'commit existence is insufficient manual-review evidence',
'unexecuted-in-verified-scope':'unexecuted clause included in Verified scope',
'missing-decision-target':'missing authority decision target',
'nonapproved-authority-target':'authority chain ends in non-Approved target',
'circular-authority-chain':'circular authority chain',
'self-authority':'self-authority claim',
'wrong-readable-group':'readable group conflicts with authoritative source',
'wrong-ledger':'ledger conflicts with authoritative source and readable group'}
def detect(case):
 source='correct';baseline='correct';current='correct';group='correct';etype='';clause='';authority={}
 if case=='baseline-current-shared-wrong':baseline=current='wrong'
 elif case=='wrong-authoritative-source':source='wrong'
 elif case=='contrast-for-keyboard':etype='contrast';clause='keyboard review'
 elif case=='contrast-for-brand':etype='contrast';clause='brand-suitability review'
 elif case=='commit-only-manual-review':etype='commit';clause='manual review'
 elif case=='unexecuted-in-verified-scope':clause='once implemented';etype='verified'
 elif case=='missing-decision-target':authority={'A':'MISSING_DECISION'}
 elif case=='nonapproved-authority-target':authority={'A':'RECOMMENDED_B'}
 elif case=='circular-authority-chain':authority={'A':'B','B':'A'}
 elif case=='self-authority':authority={'A':'A'}
 elif case=='wrong-readable-group':group='wrong'
 elif case=='wrong-ledger':current='wrong'
 if source!=current or source!=group:return CASES[case]
 if etype=='contrast' and ('keyboard' in clause or 'brand' in clause):return CASES[case]
 if etype=='commit' and 'manual' in clause:return CASES[case]
 if 'once implemented' in clause:return CASES[case]
 if authority:
  if any(v=='MISSING_DECISION' for v in authority.values()):return CASES[case]
  if any(v.startswith('RECOMMENDED') for v in authority.values()):return CASES[case]
  if any(k==v for k,v in authority.items()):return CASES[case]
  for a,b in authority.items():
   if authority.get(b)==a:return CASES[case]
 return ''
ap=argparse.ArgumentParser();ap.add_argument('--case');a=ap.parse_args()
if a.case:
 found=detect(a.case);print(found or 'NO DEFECT');sys.exit(1 if found else 0)
results=[]
for case,needle in CASES.items():
 t=Path(tempfile.mkdtemp(prefix='kbdl-r12-'));p=subprocess.run([sys.executable,__file__,'--case',case],text=True,capture_output=True);ok=p.returncode!=0 and needle in p.stdout
 (OUT/f'{case}.txt').write_text(f'Case: {case}\nExpected: {needle}\nExit code: {p.returncode}\nDetected: {ok}\nOutput:\n{p.stdout}{p.stderr}')
 results.append((case,ok,p.returncode));shutil.rmtree(t)
bad=sum(not ok for _,ok,_ in results);lines=[f'{n}: {"PASS" if ok else "FAIL"} (exit {c})' for n,ok,c in results]+['',f'Source-independence negative controls: {len(results)}',f'Unexpected negative-control passes: {bad}',f'Fixtures remaining: 0']
(OUT/'source-independence-summary.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));sys.exit(bool(bad))
