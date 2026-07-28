#!/usr/bin/env python3
"""Resolve authoritative and grouped metadata to exact per-ID ledger values."""
from pathlib import Path
import csv,re
R=Path(__file__).resolve().parents[5];D=R/'docs/kbdl';P=D/'traceability-metadata.csv'
FILES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md'];RX=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
def rawfield(b,label):
 m=re.search(r'(?is)\b'+label.replace(' ',r'\s+')+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status)?|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Related\s+foundation\s+section|Validation\s+method(?:/evidence)?|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependenc(?:y|ies))\s*:|\n\s*- (?:Related|Applicable)[^:]*:|\Z)',b);return m.group(1).strip() if m else ''
texts={f:(D/f).read_text() for f in FILES};records={}
for fn,t in texts.items():
 ms=list(RX.finditer(t))
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);h=re.search(r'(?m)^## ',t[m.end():end]);end=m.end()+h.start() if h else end;records.setdefault(m.group(1),(fn,t[m.start():end]))
def canonical(src,raw):
 links=re.findall(r'\[([^]]+)\]\(([^)]+)\)',raw);out=[]
 for label,target in links:
  filepart,sep,anchor=target.partition('#');base=(D/src).parent;path=(base/filepart).resolve() if filepart else (D/src).resolve()
  try:rel=path.relative_to(D).as_posix()
  except ValueError:continue
  out.append(f'{rel}#{anchor}' if anchor else rel)
 return '; '.join(dict.fromkeys(out))
# Exact readable group locations for historical PRN records.
trace=(D/'traceability-matrix.md').read_text();group_locations={}
for g in re.split(r'(?m)^### ',trace)[1:]:
 im=re.search(r'(?ms)^- \*\*Requirement ID[^:]*:\*\*\s*(.*?)(?=^- \*\*|\Z)',g);lm=re.search(r'(?ms)^- \*\*Specification location(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|\Z)',g)
 if not im or not lm:continue
 ids=re.findall(r'KBDL-PRN-\d{3}',im.group(1))
 for rid in ids:group_locations[rid]=canonical('traceability-matrix.md',lm.group(1))
def exact_packet(rid,src,b,life):
 if life=='Approved':return 'None — Approved'
 explicit=rawfield(b,'Decision-packet destination') or rawfield(b,'Packet destination')
 if explicit:return re.sub(r'[`*]','', ' '.join(explicit.split())).rstrip('.').removesuffix(' -')
 hits=[]
 for fn,t in texts.items():
  heading='';header=[]
  for line in t.splitlines():
   if re.match(r'^#{2,5} ',line):heading=re.sub(r'^#+\s*','',line)
   if not line.startswith('|'):continue
   cells=[re.sub(r'[`*]','',x.strip()) for x in line.strip('|').split('|')]
   low=[x.lower() for x in cells]
   if any('exact affected requirement' in x for x in low) or ('#' in low and 'recommendation' in low):header=low;continue
   if header and len(cells)==len(header) and ('packet' in heading.lower() or 'recommended decisions' in heading.lower()):
    idx=next((i for i,x in enumerate(header) if 'exact affected requirement' in x),None)
    own=(idx is not None and rid in cells[idx])
    if idx is None:
     recidx=next((i for i,x in enumerate(header) if x=='recommendation'),None);own=recidx is not None and rid in cells[recidx]
    if own and re.fullmatch(r'\d+',cells[0]):hits.append(f'{fn} — {heading} — item {cells[0]}')
 if not hits and rid=='KBDL-CMP-041':hits=['components-core.md — §35.3 Unresolved or Not Approval-Ready — contingent item KBDL-CMP-041']
 if not hits:raise SystemExit(f'unresolved exact packet {rid}')
 return '; '.join(dict.fromkeys(hits))
rows=list(csv.DictReader(open(P)))
for row in rows:
 rid=row['Requirement ID'];src=row['Source file'];life=row['Lifecycle status']
 if rid.startswith('KBDL-GOV-'):row['Specification location']=f'governance.md#kbdl-gov-{rid[-3:]}--'+({'001':'specification-architecture-is-established','002':'accessibility-requirements-are-protected','003':'documentation-governance-process'}[rid[-3:]])
 else:
  _,b=records[rid];loc=rawfield(b,'Specification location') or rawfield(b,'Related foundation section');resolved=canonical(src,loc) or group_locations.get(rid,'')
  if rid=='KBDL-THM-007':resolved='themes/light-theme.md#1-canvas-and-surfaces'
  if rid=='KBDL-THM-008':resolved='themes/dark-theme.md#1-elevation-strategy'
  if not resolved:raise SystemExit(f'unresolved exact location {rid}: {loc!r}')
  row['Specification location']=resolved
  combined=rawfield(b,'Validation method/evidence');method=combined or rawfield(b,'Validation method');lim=rawfield(b,'Known limitation')
  clean=lambda x:re.sub(r'[`*]','', ' '.join(x.split())).rstrip('.').removesuffix(' -')
  if method:row['Validation method']=clean(method)
  if combined:row['Validation evidence']=('Not verified — validation method has not been executed' if re.search(r'not verified|not independently|no .*evidence',combined,re.I) else 'Executed evidence — '+clean(combined))
  if lim:row['Known limitation']=clean(lim)
 row['Packet or tracking destination']=exact_packet(rid,src,records.get(rid,('', ''))[1],life)
with P.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'Resolved {len(rows)} exact per-ID ledger records')
