#!/usr/bin/env python3
"""Correct per-ID evidence attribution without changing authoritative requirements."""
from pathlib import Path
import csv
R=Path(__file__).resolve().parents[5];P=R/'docs/kbdl/traceability-metadata.csv';rows=list(csv.DictReader(open(P)))
changed=[]
limitations={'KBDL-FND-005':'No implementation exists to execute the stated typography validation method.','KBDL-FND-006':'No implementation exists to execute the stated iconography validation method.','KBDL-FND-007':'No implementation exists to execute the stated spacing validation method.','KBDL-PRN-006':'Later-module conflict-resolution behavior has not been executed.'}
for r in rows:
 rid=r['Requirement ID']
 if rid.startswith('KBDL-A11Y-') and rid not in ('KBDL-A11Y-007','KBDL-A11Y-008','KBDL-A11Y-009'):
  expected=('Not verified — the requirement’s stated validation method has not been executed.' if 'Not verified' in r['Validation classification'] else 'Not applicable — no executed implementation claim is asserted for this requirement.')
  if r['Validation evidence']!=expected:r['Validation evidence']=expected;changed.append(rid)
 if rid in limitations:r['Known limitation']=limitations[rid]
 if rid.startswith('KBDL-VAL-') and 'Verified' in r['Validation classification']:
  artifact='verified-evidence-audit.csv' if rid=='KBDL-VAL-004' else 'validation-output.txt'
  r['Validation evidence']=f'Executed evidence — docs/kbdl/evidence/kbdl-011-r8/artifacts/{artifact}; stated repository method PASS.'
with P.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'Corrected evidence attribution for {len(changed)} requirements')
