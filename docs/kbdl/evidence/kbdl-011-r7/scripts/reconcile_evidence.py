#!/usr/bin/env python3
"""Correct per-ID evidence attribution without changing authoritative requirements."""
from pathlib import Path
import csv
R=Path(__file__).resolve().parents[5];P=R/'docs/kbdl/traceability-metadata.csv';rows=list(csv.DictReader(open(P)))
changed=[]
for r in rows:
 rid=r['Requirement ID']
 if rid.startswith('KBDL-A11Y-') and rid not in ('KBDL-A11Y-007','KBDL-A11Y-008','KBDL-A11Y-009'):
  expected=('Not verified — the requirement’s stated validation method has not been executed.' if 'Not verified' in r['Validation classification'] else 'Not applicable — no executed implementation claim is asserted for this requirement.')
  if r['Validation evidence']!=expected:r['Validation evidence']=expected;changed.append(rid)
with P.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'Corrected evidence attribution for {len(changed)} requirements')
