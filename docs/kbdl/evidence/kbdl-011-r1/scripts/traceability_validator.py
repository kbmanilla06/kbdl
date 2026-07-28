#!/usr/bin/env python3
"""Validate roadmap traceability sections and requirement references."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[5]/'docs/kbdl'; trace=(ROOT/'traceability-matrix.md').read_text(); errors=[]
for step in range(1,12):
    if not re.search(rf'^## KBDL-{step:03}\b',trace,re.M): errors.append(f'missing section KBDL-{step:03}')
for module,total in [('GOV',3),('PRN',8),('FND',12),('THM',16),('MOT',34),('RSP',22),('A11Y',40),('CMP',111),('PRO',29),('CUS',30),('VAL',12)]:
    found=set(re.findall(rf'KBDL-{module}-(\d{{3}}[a-z]?)',trace))
    for block in re.findall(r'- \*\*Requirement ID[^:]*:\*\*(.*?)(?=\n- \*\*|\n###|\n##|\Z)',trace,re.S):
        if f'KBDL-{module}-' in block:
            found.update(re.findall(r'(?<![§\d])(\d{3}[a-z]?)(?!\d)',block))
            for first,last in re.findall(r'(\d{3})[–-](\d{3})',block):
                found.update(f'{i:03}' for i in range(int(first),int(last)+1))
    if len(found)!=total: errors.append(f'{module} trace IDs unique={len(found)} expected={total}')
val=trace[trace.find('## KBDL-011'):trace.find('## Notes on Scope')]
for i in range(1,13):
    rid=f'KBDL-VAL-{i:03}'
    if rid not in val: errors.append(f'missing {rid}')
print('Traceability roadmap sections: 11')
print('Requirement traceability expected: 317')
print(f'Traceability errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
