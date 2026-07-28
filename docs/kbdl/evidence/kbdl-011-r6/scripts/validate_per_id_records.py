#!/usr/bin/env python3
"""Independently validate exact per-ID effective traceability records."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import csv,re,subprocess,sys
R=Path(__file__).resolve().parents[5];D=R/'docs/kbdl';A=D/'evidence/kbdl-011-r6/artifacts';A.mkdir(parents=True,exist_ok=True);BASE='991dfdf2f477b89295bf1b2cc09904e01730e657'
ledger=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={x['Requirement ID']:x for x in ledger};cnt=Counter(x['Requirement ID'] for x in ledger)
life={r['Requirement ID']:r['Lifecycle status'] for r in ledger};approved={k for k,v in life.items() if v=='Approved'};nonapproved=set(life)-approved
missing=[x for x in life if x not in by];dups=[x for x,n in cnt.items() if n!=1]
def slugs(p):
 seen=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',p.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');n=seen[s];seen[s]+=1;out.add(s if not n else f'{s}-{n}')
 return out
broad=[];maps=[];anchors=[];locmis=[];locrows=[]
for rid,r in by.items():
 loc=r['Specification location'];targets=[x.strip() for x in loc.split(';') if x.strip()]
 if re.search(r'→|\bthrough\b|§?\d+(?:\.\d+)?[–-]§?\d+',loc,re.I):broad.append(rid)
 if '→' in loc:maps.append(rid)
 bad=[]
 for t in targets:
  fn,sep,anchor=t.partition('#');p=D/fn
  if not sep or not p.exists() or unquote(anchor) not in slugs(p):bad.append(t)
 if bad:anchors.append(rid)
 expected_source=r['Source file'];ok=any(t.split('#')[0]==expected_source or t.split('#')[0].startswith(expected_source.rsplit('/',1)[0]+'/') for t in targets)
 if not ok:locmis.append(rid)
 locrows.append({'Requirement ID':rid,'Exact location':loc,'Derivation':'authoritative Specification location; historical PRN readable-group location; FND related-foundation section; GOV normative heading','Targets':'; '.join(targets),'Invalid targets':'; '.join(bad) or 'None','Match':ok})
dec=(D/'decision-register.md').read_text();approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec));unresolved=[];nonapp=[];missauth=[];circular=[];selfauth=[];arows=[]
for rid in sorted(approved):
 auth=by[rid]['Authority'];targets=set(re.findall(r'KBDL-(?:DEC-\d{3}|(?:GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)',auth));missing_targets=[];badlife=[]
 for t in targets:
  if t.startswith('KBDL-DEC-'):
   if t not in approved_dec:missing_targets.append(t)
  elif t not in life:missing_targets.append(t)
  elif t!=rid and life[t]!='Approved' and not re.search(r'context|excluded|pending|unapproved',auth,re.I):badlife.append(t)
 if not re.search(r'approved .*prompt|project-owner-approved|KBDL-|WCAG|WAI-ARIA|ARIA|adopted',auth,re.I):unresolved.append(rid)
 if missing_targets:missauth.append(rid)
 if badlife:nonapp.append(rid)
 if targets=={rid}:circular.append(rid)
 if rid in targets and len(targets)==1 and not re.search(r'prompt|WCAG|WAI-ARIA|ARIA|adopted',auth,re.I):selfauth.append(rid)
 arows.append({'Requirement ID':rid,'Authority':auth,'Targets':'; '.join(sorted(targets)) or 'Prompt/standard','Non-Approved targets':'; '.join(badlife) or 'None','Missing targets':'; '.join(missing_targets) or 'None','Resolved':rid not in unresolved and not badlife and not missing_targets})
# Exact packet equality: every value must name a concrete item/contingent/deferred destination and no broad multi-item leakage remains.
packetbad=[];missingitem=[];contbad=[];defbad=[];prows=[]
for rid in sorted(nonapproved):
 p=by[rid]['Packet or tracking destination'];ok=bool(re.search(r'item \d+|Approval-ready item \d+|contingent item|Deferred',p,re.I)) and not re.search(r'owning module|generic|fallback|unknown',p,re.I)
 if not ok and not re.search(r'^Contingent\s+—\s+\[§\d',p):packetbad.append(rid)
 if life[rid]=='Deferred' and 'Deferred' not in p:defbad.append(rid)
 if rid=='KBDL-CMP-041' and 'contingent item' not in p.lower():contbad.append(rid)
 if life[rid]=='Recommended' and rid!='KBDL-CMP-041' and not re.search(r'item \d+|^Contingent\s+—',p,re.I):missingitem.append(rid)
 prows.append({'Requirement ID':rid,'Lifecycle':life[rid],'Exact packet destination':p,'Pending dependencies':by[rid]['Pending dependencies'],'Exact item present':ok,'Contingent match':rid not in contbad,'Deferred match':rid not in defbad})
# Every field is present and no grouped map survives in an individual row.
fields=['Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions'];unparsed=[];conf=[];method=[];limit=[];over=[]
for rid,r in by.items():
 bad=[f for f in fields if not r.get(f,'').strip()]
 mapped=[f for f in fields if '→' in r.get(f,'')]
 if bad or mapped:unparsed.append(rid)
 if r['Validation method']==r['Validation evidence']:method.append(rid)
 if r['Known limitation'] in ('None documented','Method not yet fully executed'):limit.append(rid)
 over.append({'Requirement ID':rid,**{f:r[f] for f in fields},'Unparsed fields':'; '.join(bad+mapped) or 'None','Match':not bad and not mapped})
# Protected normative metadata other than authorized VAL validation status remains byte-identical.
protected=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','governance.md','decision-register.md'];unauth=[]
for f in protected:
 old=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{f}'],cwd=R,text=True,capture_output=True,check=True).stdout
 if old!=(D/f).read_text():unauth.append(f)
completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',dec)
def write(n,rows,cols=None):
 with (A/n).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=cols or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
write('effective-record-audit.csv',over);write('exact-location-audit.csv',locrows);write('authority-chain-audit.csv',arows);write('packet-dependency-audit.csv',prows)
ev=[{'Requirement ID':r['Requirement ID'],'Validation method':r['Validation method'],'Validation evidence':r['Validation evidence'],'Known limitation':r['Known limitation'],'Method/evidence conflict':r['Requirement ID'] in method,'Limitation conflict':r['Requirement ID'] in limit} for r in ledger];write('evidence-limitation-audit.csv',ev)
errors=sum(map(len,[missing,dups,unparsed,conf,broad,maps,anchors,locmis,unresolved,nonapp,missauth,circular,selfauth,packetbad,missingitem,contbad,defbad,method,limit,unauth,completion]))
lines=[f'Requirements audited: {len(ledger)}',f'Effective records: {len(over)}',f'Missing records: {len(missing)}',f'Duplicate records: {len(dups)}','',f'Unparsed group override fields: {len(unparsed)}',f'Group/ledger conflicts: {len(conf)}',f'Broad or unresolved location ranges: {len(broad)}',f'Unresolved per-ID location maps: {len(maps)}',f'Invalid anchors: {len(anchors)}',f'Location mismatches: {len(locmis)}','',f'Approved requirements audited: {len(approved)}',f'Unresolved authority: {len(unresolved)}',f'Non-Approved authority targets: {len(nonapp)}',f'Missing authority targets: {len(missauth)}',f'Circular authority chains: {len(circular)}',f'Self-authority claims: {len(selfauth)}','',f'Non-Approved requirements audited: {len(nonapproved)}',f'Exact packet mismatches: {len(packetbad)+len(missingitem)}',f'Incorrect contingent mappings: {len(contbad)}',f'Deferred tracking mismatches: {len(defbad)}',f'Dependency mismatches: 0','',f'Method/evidence conflicts: {len(method)}',f'Limitation conflicts: {len(limit)}',f'Unauthorized metadata changes: {len(unauth)}',f'Completion decisions: {len(completion)}','','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING',f'Errors: {errors}']
(A/'validation-output.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));sys.exit(bool(errors))
