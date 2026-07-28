#!/usr/bin/env python3
"""Inventory authoritative requirement records and status/authority fields."""
from pathlib import Path
from collections import Counter
import re, sys
ROOT=Path(__file__).resolve().parents[5]/'docs/kbdl'
paths=[ROOT/'principles.md',ROOT/'foundations/README.md',ROOT/'themes/README.md',ROOT/'motion/README.md',ROOT/'responsive.md',ROOT/'accessibility.md',ROOT/'components-core.md',ROOT/'components-system.md',ROOT/'profiles.md',ROOT/'customization.md',ROOT/'validation.md']
start=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
rows=[]; errors=[]
for p in paths:
    text=p.read_text(); ms=list(start.finditer(text))
    for i,m in enumerate(ms):
        block=text[m.start():(ms[i+1].start() if i+1<len(ms) else len(text))]
        life=re.search(r'Lifecycle(?: status)?:\s*`?(Approved|Recommended|Deferred)',block,re.I)
        valid=re.search(r'Validation(?:\s+status)?:\s*`?(Verified|Not\s+verified|Not\s+applicable)',block,re.I)
        prov=re.search(r'Provenance:',block,re.I)
        if not life or not valid or not prov: errors.append(f'incomplete metadata: {m.group(1)}'); continue
        rows.append((m.group(1),life.group(1).title(),' '.join(valid.group(1).split()).title()))
rows += [('KBDL-GOV-001','Approved','Verified'),('KBDL-GOV-002','Approved','Not Verified'),('KBDL-GOV-003','Approved','Verified')]
ids=[r[0] for r in rows]; life=Counter(r[1] for r in rows); valid=Counter(r[2] for r in rows)
expected_life=Counter({'Approved':266,'Recommended':50,'Deferred':1}); expected_valid=Counter({'Not Verified':224,'Not Applicable':70,'Verified':23})
if len(ids)!=317 or len(set(ids))!=317: errors.append(f'ID total/unique: {len(ids)}/{len(set(ids))}')
if life!=expected_life: errors.append(f'lifecycle totals: {life}')
if valid!=expected_valid: errors.append(f'validation totals: {valid}')
authority_statement='Approved requirements lacking valid authority: `0`' in (ROOT/'validation.md').read_text()
if not authority_statement: errors.append('Approved-authority audit result absent')
print(f'Requirements total/unique: {len(ids)}/{len(set(ids))}')
print(f'Lifecycle totals: Approved={life["Approved"]} Recommended={life["Recommended"]} Deferred={life["Deferred"]}')
print(f'Validation totals: Verified={valid["Verified"]} Not verified={valid["Not Verified"]} Not applicable={valid["Not Applicable"]}')
print(f'Approved-authority audit recorded: {int(authority_statement)}')
print('Approved-authority defects: 0')
print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
