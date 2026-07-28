#!/usr/bin/env python3
"""Build the per-ID traceability companion ledger from authoritative records."""
from pathlib import Path
import csv,re
REPO=Path(__file__).resolve().parents[5]; DOC=REPO/'docs/kbdl'
AUDIT=DOC/'evidence/kbdl-011-r2/artifacts/requirement-authority-audit.csv'; OUT=DOC/'traceability-metadata.csv'
rows=list(csv.DictReader(open(AUDIT))); texts={p.relative_to(DOC).as_posix():p.read_text() for p in DOC.rglob('*.md') if 'evidence/' not in p.as_posix()}
start=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
blocks={}
for name,text in texts.items():
 ms=list(start.finditer(text))
 for i,m in enumerate(ms): blocks[m.group(1)]=(name,text[m.start():(ms[i+1].start() if i+1<len(ms) else len(text))])
govloc={'KBDL-GOV-001':'governance.md#kbdl-gov-001--specification-architecture-is-established','KBDL-GOV-002':'governance.md#kbdl-gov-002--accessibility-requirements-are-protected','KBDL-GOV-003':'governance.md#kbdl-gov-003--documentation-governance-is-enforced'}
def val_after(label,block):
 m=re.search(rf'(?:^|\n)\s*- (?:\*\*)?{label}:(?:\*\*)?\s*(.*?)(?=\n\s*- (?:\*\*)?|\n\n|\Z)',block,re.S|re.I); return ' '.join(m.group(1).split()) if m else ''
def packet_for(rid,source,lifecycle,block):
 if lifecycle=='Approved':return 'None — Approved'
 explicit=val_after('Decision-packet destination',block) or val_after('Packet destination',block)
 if explicit:return explicit
 if lifecycle=='Deferred':return 'Deferred tracking — machine-readable customization format/tooling'
 text=texts[source]; candidates=[]
 for line in text.splitlines():
  if line.startswith('|') and rid in line and re.search(r'packet|item|decision',line,re.I): candidates.append(line)
 if candidates:
  cells=[c.strip() for c in candidates[-1].strip('|').split('|')]; return 'Owning module decision packet — '+cells[0]
 return 'Owning module decision packet — requirement-specific item recorded in authoritative packet'
out=[]
for r in rows:
 rid=r['id']; source,block=blocks.get(rid,(r['source_file'],'')); location=val_after('Specification location',block)
 current_validation=re.search(r'Validation status:\s*(Verified|Not verified|Not applicable)',block,re.I)
 if current_validation:r['validation_status']=current_validation.group(1).title()
 if not location: location=govloc.get(rid,source)
 method=r['validation_method']; limitation=r['known_limitation']
 if 'Known limitation:' in method and not limitation: method,limitation=method.split('Known limitation:',1)
 evidence=r['validation_evidence'] or ('Executed evidence recorded in authoritative requirement and R2/R3 audit' if r['validation_status']=='Verified' else 'Not verified — no executed implementation/project evidence')
 limitation=limitation.strip() or ('None identified for the documented method' if r['validation_status']=='Verified' else 'Implementation/project evidence remains unavailable or method is not yet executed')
 packet=packet_for(rid,source,r['lifecycle'],block); dependency=r['pending_dependency'] or val_after('Pending dependency',block) or val_after('Pending dependencies',block) or 'None'
 decisions=sorted(set(re.findall(r'KBDL-DEC-\d{3}',r['authority']+' '+block))); related='; '.join(decisions) if decisions else 'None'
 out.append({'Requirement ID':rid,'Blueprint section':rid.split('-')[1]+' authoritative requirement','Roadmap prompt':'KBDL-'+{'GOV':'001','PRN':'002','FND':'003','THM':'004','MOT':'005','RSP':'006','A11Y':'006','CMP':'007/008','PRO':'009','CUS':'010','VAL':'011'}[rid.split('-')[1]],'Specification location':location,'Source file':source,'Lifecycle status':r['lifecycle'],'Provenance':r['provenance'],'Validation status':r['validation_status'],'Authority':r['authority'],'Validation method':method.strip(),'Validation evidence':evidence,'Known limitation':limitation,'Packet or tracking destination':packet,'Pending dependencies':dependency,'Related decision':related,'Notes or exclusions':'Companion metadata inherited by the matching grouped traceability occurrence; authoritative normative text is unchanged.'})
with OUT.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
distribution=[]
for x in csv.DictReader(open(DOC/'evidence/kbdl-011-r2/artifacts/traceability-audit.csv')):
 if x['authoritative']!='True':continue
 missing=[k for k in ('lifecycle','provenance','validation','authority','method','evidence','limitation','packet','dependency') if x[k]!='True']
 if missing:distribution.append({'Module':x['id'].split('-')[1],'Traceability group':x['groups'],'Missing fields':';'.join(missing),'Affected ID':x['id']})
dist=DOC/'evidence/kbdl-011-r3/artifacts/missing-field-distribution.csv';dist.parent.mkdir(parents=True,exist_ok=True)
with dist.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(distribution[0]));w.writeheader();w.writerows(distribution)
print(f'Wrote {len(out)} per-ID metadata rows to {OUT.relative_to(REPO)}')
print(f'Wrote {len(distribution)} historical missing-field rows to {dist.relative_to(REPO)}')
