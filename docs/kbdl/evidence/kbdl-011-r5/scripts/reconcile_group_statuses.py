#!/usr/bin/env python3
"""Mechanically reconcile readable-group validation summaries to per-ID ledger values."""
from pathlib import Path
import csv,re
R=Path(__file__).resolve().parents[5];D=R/'docs/kbdl';P=D/'traceability-matrix.md';rows={x['Requirement ID']:x['Validation classification'] for x in csv.DictReader(open(D/'traceability-metadata.csv'))}
def ids(block):
 m=re.search(r'(?ms)^- \*\*Requirement ID[^:]*:\*\*\s*(.*?)(?=^- \*\*|\Z)',block)
 if not m:return []
 raw=m.group(1);p=re.search(r'KBDL-([A-Z0-9]+)-',raw)
 if not p:return []
 mod=p.group(1);raw=raw.split('(37 requirements;')[0];out=[]
 for x in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',raw):
  a,b=x.group(1),x.group(2);out += [f'KBDL-{mod}-{n:03}' for n in range(int(a),int(b)+1)] if b else [f'KBDL-{mod}-{a}']
 return out
def label(rid):return rid if rid.endswith(tuple('abcdefghijklmnopqrstuvwxyz')) else rid
parts=re.split(r'(?m)(?=^### )',P.read_text());changed=0
for i,b in enumerate(parts):
 group=ids(b)
 if not group or not re.search(r'(?m)^- \*\*Validation status:\*\*',b):continue
 by={}
 for rid in group:by.setdefault(rows[rid],[]).append(rid)
 if len(by)==1:new=next(iter(by))
 else:new='; '.join(f'{status}: '+', '.join(vals) for status,vals in by.items())
 b2=re.sub(r'(?ms)(^- \*\*Validation status:\*\*\s*).*?(?=^- \*\*|\Z)',lambda m:m.group(1)+new+'\n',b,count=1)
 changed += b2!=b;parts[i]=b2
P.write_text(''.join(parts));print(f'Reconciled {changed} readable validation-status fields')
