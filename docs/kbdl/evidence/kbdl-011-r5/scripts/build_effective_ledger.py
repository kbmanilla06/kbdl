#!/usr/bin/env python3
"""Build the companion ledger from authority sources plus readable groups."""
from pathlib import Path
from collections import defaultdict
import csv,re
R=Path(__file__).resolve().parents[5]; D=R/'docs/kbdl'; OUT=D/'traceability-metadata.csv'
SRC=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
PROMPT={'GOV':'KBDL-001','PRN':'KBDL-002','FND':'KBDL-003','THM':'KBDL-004','MOT':'KBDL-005','RSP':'KBDL-006','A11Y':'KBDL-006','CMP':'KBDL-007/008','PRO':'KBDL-009','CUS':'KBDL-010','VAL':'KBDL-011'}
START=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
MARK=re.compile(r'(?i)(Lifecycle\s+status|Lifecycle|Provenance|Validation\s+status|Validation|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Validation\s+method/evidence|Validation\s+method|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependencies|Pending\s+dependency)\s*:')
def tidy(v):
 v=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',v).replace('`','').replace('**','');return ' '.join(v.split()).strip().rstrip('.').removesuffix(' -')
def fields(b):
 ms=list(MARK.finditer(b));o={}
 for i,m in enumerate(ms):
  k=' '.join(m.group(1).lower().split()).replace(' status','').replace('decision-','').replace(' dependencies',' dependency');k='authority' if k.startswith('authority') else k
  raw=b[m.end():(ms[i+1].start() if i+1<len(ms) else len(b))];raw=re.split(r'\n\s*- (?:Related|Applicable|Specification|Validation|Known|Packet|Decision-packet|Pending)[^:]*:',raw,1)[0];raw=re.sub(r'\n\s*-\s*$','',raw);o[k]=tidy(raw)
 return o
texts={n:(D/n).read_text() for n in SRC}; rec={}
for src,t in texts.items():
 ms=list(START.finditer(t))
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);h=re.search(r'(?m)^## ',t[m.end():end]);end=m.end()+h.start() if h else end;rec.setdefault(m.group(1),(src,t[m.start():end]))
gov=(D/'governance.md').read_text()
for n in range(1,4):
 rid=f'KBDL-GOV-{n:03d}';m=re.search(rf'(?m)^## {rid}\b',gov);z=re.search(r'(?m)^## KBDL-GOV-',gov[m.end():]);rec[rid]=('governance.md',gov[m.start():m.end()+(z.start() if z else len(gov))])
def group_fields(g):
 o={}
 for m in re.finditer(r'(?ms)^- \*\*([^:*(]+?)(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|^### |^## |\Z)',g):o[m.group(1).strip().lower()]=tidy(m.group(2))
 return o
groups={};trace=(D/'traceability-matrix.md').read_text()
for g in re.split(r'(?m)^### ',trace)[1:]:
 gf=group_fields(g);raw=gf.get('requirement id','');mm=re.search(r'KBDL-([A-Z0-9]+)-',raw)
 if not mm:continue
 mod=mm.group(1);include=raw.split('(37 requirements;')[0];ids=[]
 for x in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',include):
  a,b=x.group(1),x.group(2);ids += [f'KBDL-{mod}-{i:03}' for i in range(int(a),int(b)+1)] if b else [f'KBDL-{mod}-{a}']
 for rid in ids:
  if rid in groups:raise SystemExit(f'duplicate readable group for {rid}')
  groups[rid]=gf
def classification(v):
 q=v.lower();k=[]
 if re.search(r'(?<!not )\bverified\b',q):k.append('Verified')
 if 'not verified' in q:k.append('Not verified')
 if 'not applicable' in q:k.append('Not applicable')
 k=k or ['Not verified'];return ('Mixed — '+' / '.join(k) if len(k)>1 else k[0],v if 'Verified' in k else 'None',v if 'Not verified' in k else 'None',v if 'Not applicable' in k else 'None')
def packet(rid,src,b,life):
 if life=='Approved':return 'None — Approved'
 f=fields(b);x=f.get('packet destination','')
 if x:return x
 hits=[]
 for ps,pt in texts.items():
  head=''
  for line in pt.splitlines():
   if re.match(r'^#{2,5} ',line):head=tidy(line.lstrip('# '))
   if line.startswith('|') and rid in line and ('packet' in head.lower() or 'recommended decisions' in head.lower()):
    c=[tidy(v) for v in line.strip('|').split('|')]
    if re.fullmatch(r'\d+',c[0]):hits.append((ps,c[0],f'{ps} — {head} — item {c[0]}'))
 own=[x[2] for x in hits if x[0]==src] or [x[2] for x in hits]
 if not own:raise SystemExit(f'no exact packet for {rid}')
 return '; '.join(sorted(set(own)))
rows=[]
for rid,(src,b) in sorted(rec.items()):
 f=fields(b);g=groups[rid];mod=rid.split('-')[1]
 if mod=='GOV':
  life='Approved';prov='Historical KBDL-001 prompt and approved decision record';val='Verified' if rid in ('KBDL-GOV-001','KBDL-GOV-003') else 'Not verified';auth={'KBDL-GOV-001':'Project-owner-approved KBDL-001 prompt and KBDL-DEC-002','KBDL-GOV-002':'Project-owner-approved KBDL-001 prompt and KBDL-DEC-010','KBDL-GOV-003':'Project-owner-approved KBDL-001 prompt and KBDL-DEC-011'}[rid]
 else:
  life=f.get('lifecycle','').split(' — ',1)[0].split(' (',1)[0];prov=f.get('provenance','');val=f.get('validation','');rawlife=f.get('lifecycle','')
  auth=f.get('authority') or (rawlife if rawlife!=life else f'Project-owner-approved {PROMPT[mod]} implementation prompt; authoritative provenance: {prov}')
  if life=='Approved' and not re.search(r'KBDL-(?:DEC|GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-|WCAG|WAI-ARIA|ARIA|approved .*prompt|project-owner-approved|adopted',auth,re.I):auth += f'; project-owner-approved {PROMPT[mod]} implementation prompt'
 loc=g.get('specification location') or f.get('specification location','')
 combined=g.get('validation method / evidence','');method=g.get('validation method') or combined or f.get('validation method/evidence') or f.get('validation method') or 'Manual documentary review'
 evidence=g.get('validation evidence','')
 if not evidence and combined:evidence=('Not verified — validation method has not been executed' if re.search(r'not verified|not yet performed|no evidence',combined,re.I) else 'Executed evidence — '+combined)
 if not evidence or evidence==method:evidence='Not verified — validation method has not been executed' if 'not verified' in val.lower() else 'Executed result is identified in the readable traceability group'
 limit=g.get('known limitation','') or ('Implementation or project evidence is unavailable for the stated unverified scope' if 'not verified' in val.lower() else 'No additional limitation identified by the recorded review')
 dep=f.get('pending dependency','') or 'None';vc,vs,ns,nas=classification(val);dec='; '.join(sorted(set(re.findall(r'KBDL-DEC-\d{3}',auth+' '+b)))) or 'None'
 rows.append({'Requirement ID':rid,'Blueprint section':g.get('blueprint section',mod+' authoritative requirement'),'Roadmap prompt':g.get('roadmap prompt',PROMPT[mod]),'Specification location':loc,'Source file':src,'Lifecycle status':life,'Provenance':prov,'Validation classification':vc,'Verified scope':vs,'Not-verified scope':ns,'Not-applicable scope':nas,'Authority':auth,'Authority targets':dec,'Validation method':method,'Validation evidence':evidence,'Known limitation':limit,'Packet or tracking destination':packet(rid,src,b,life),'Pending dependencies':dep,'Dependency classification':'None' if dep=='None' else ('Deferred' if life=='Deferred' else 'Context-only' if re.search(r'context|does not block',dep,re.I) else 'Later implementation validation' if re.search(r'implementation|project',dep,re.I) else 'Blocking'),'Related decision':dec,'Notes or exclusions':'Readable group plus authoritative per-ID ledger; group values reconciled without changing normative text.'})
if len(rows)!=317 or len(groups)!=317:raise SystemExit(f'cardinality records={len(rows)} groups={len(groups)}')
with OUT.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'Wrote {len(rows)} effective ledger rows')
