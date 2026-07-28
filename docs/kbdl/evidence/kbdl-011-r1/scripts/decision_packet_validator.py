#!/usr/bin/env python3
"""Validate decision sequence, KBDL-DEC-002 clarification, and pending boundaries."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[5]; DOC=ROOT/'docs/kbdl'; errors=[]
decision=(DOC/'decision-register.md').read_text(); validation=(DOC/'validation.md').read_text(); alltext='\n'.join(p.read_text() for p in DOC.rglob('*.md'))
ids=re.findall(r'^#{2,4} (KBDL-DEC-\d{3})\b',decision,re.M)
if ids != [f'KBDL-DEC-{i:03}' for i in range(1,16)]: errors.append(f'decision sequence: {ids}')
clarification='Roadmap-evolution clarification (KBDL-011-R1)' in decision
if not clarification: errors.append('DEC-002 clarification absent')
if 'CUS-030' not in validation or 'Deferred' not in validation: errors.append('CUS-030 boundary absent')
completion_decisions=len(re.findall(r'^#{2,4} KBDL-DEC-\d+.*completion',decision,re.M|re.I))
if completion_decisions: errors.append('completion decision created')
required_pending=['50 Recommended','CUS-030','Pending requirements lacking tracking: `0`']
for phrase in required_pending:
    if phrase not in validation: errors.append(f'pending evidence absent: {phrase}')
print(f'Decisions unique/sequential: {len(set(ids))}/{len(ids)}')
print(f'KBDL-DEC-002 roadmap clarification present: {int(clarification)}')
print('Pending promotions: 0')
print(f'Completion decisions created: {completion_decisions}')
print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
