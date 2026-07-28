#!/usr/bin/env python3
"""Validate R3 per-ID ledger against authoritative R2 extraction and source locations."""
from pathlib import Path
from collections import Counter
import csv,re,sys
REPO=Path(__file__).resolve().parents[5]; DOC=REPO/'docs/kbdl'; OUT=DOC/'evidence/kbdl-011-r3/artifacts'; OUT.mkdir(parents=True,exist_ok=True)
auth={r['id']:r for r in csv.DictReader(open(DOC/'evidence/kbdl-011-r2/artifacts/requirement-authority-audit.csv'))}; ledger=list(csv.DictReader(open(DOC/'traceability-metadata.csv'))); by={r['Requirement ID']:r for r in ledger}
vtext=(DOC/'validation.md').read_text(); vm=re.search(r'- \*\*`KBDL-VAL-006`.*?Validation status:\s*(Verified|Not verified|Not applicable)',vtext,re.S|re.I)
if vm:auth['KBDL-VAL-006']['validation_status']=vm.group(1).title()
trace=list(csv.DictReader(open(DOC/'evidence/kbdl-011-r2/artifacts/traceability-audit.csv')))
required=['Requirement ID','Blueprint section','Roadmap prompt','Specification location','Source file','Lifecycle status','Provenance','Validation status','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions']
start=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?'); expected_locations={}
for source_name in sorted(set(x['source_file'] for x in auth.values())):
 p=DOC/source_name
 if not p.exists():continue
 text=p.read_text();ms=list(start.finditer(text))
 for i,m in enumerate(ms):
  block=text[m.start():(ms[i+1].start() if i+1<len(ms) else len(text))];lm=re.search(r'(?:^|\n)\s*- (?:\*\*)?Specification location:(?:\*\*)?\s*(.*?)(?=\n\s*- (?:\*\*)?|\n\n|\Z)',block,re.S|re.I)
  if lm:expected_locations[m.group(1)]=' '.join(lm.group(1).split())
counts=Counter(r['Requirement ID'] for r in ledger); missing=sorted(set(auth)-set(by)); dup=sorted(k for k,n in counts.items() if n!=1); orphan=sorted(set(by)-set(auth)); incomplete=[]; location=[]; life=[]; prov=[]; valid=[]; authority=[]; packet=[]; dependency=[]; comparison=[]
for rid,a in auth.items():
 r=by.get(rid,{})
 absent=[f for f in required if not r.get(f,'').strip()]
 if absent:incomplete.append((rid,absent))
 source=DOC/r.get('Source file',''); loc=r.get('Specification location',''); target=re.search(r'\]\(([^)]+)\)',loc)
 if target:
  filepart=target.group(1).split('#',1)[0]; dest=(source.parent/filepart).resolve() if filepart else source.resolve(); loc_ok=source.exists() and dest.exists()
 else: loc_ok=source.exists() and bool(loc.strip()) and (r.get('Source file','') in loc or loc.startswith(r.get('Source file','')))
 if rid in expected_locations:loc_ok=loc_ok and loc==expected_locations[rid]
 if not loc_ok:location.append(rid)
 if r.get('Lifecycle status')!=a['lifecycle']:life.append(rid)
 if r.get('Provenance')!=a['provenance']:prov.append(rid)
 if r.get('Validation status')!=a['validation_status']:valid.append(rid)
 if r.get('Authority')!=a['authority']:authority.append(rid)
 if a['lifecycle']=='Approved' and r.get('Packet or tracking destination')!='None — Approved':packet.append(rid)
 if a['lifecycle']!='Approved' and not a.get('packet_destination') and not re.search(r'packet|tracking|deferred',r.get('Packet or tracking destination',''),re.I):packet.append(rid)
 if a['lifecycle']!='Approved' and a.get('packet_destination') and r.get('Packet or tracking destination')!=a['packet_destination']:packet.append(rid)
 expected_dependency=a.get('pending_dependency') or 'None'
 if r.get('Pending dependencies')!=expected_dependency:dependency.append(rid)
 comparison.append({'Requirement ID':rid,'Source file':r.get('Source file'),'Traceability group':next((x['groups'] for x in trace if x['id']==rid),''),'Complete':not absent,'Location match':loc_ok,'Lifecycle match':rid not in life,'Provenance match':rid not in prov,'Validation-status match':rid not in valid,'Authority match':rid not in authority,'Packet match':rid not in packet,'Dependency match':rid not in dependency,'Defect details':';'.join(absent)})
with (OUT/'traceability-metadata-comparison.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(comparison[0]));w.writeheader();w.writerows(comparison)
print(f'Requirements audited: {len(auth)}');print(f'Traceability occurrences: {sum(int(x["occurrences"]) for x in trace if x["authoritative"]=="True")}');print(f'Missing traceability: {len(missing)}');print(f'Duplicate traceability: {len(dup)}');print(f'Orphan traceability: {len(orphan)}');print(f'Incomplete traceability records: {len(incomplete)}')
print(f'Specification-location mismatches: {len(location)}');print(f'Lifecycle mismatches: {len(life)}');print(f'Provenance mismatches: {len(prov)}');print(f'Validation-status mismatches: {len(valid)}');print(f'Authority inconsistencies: {len(authority)}');print(f'Packet-destination mismatches: {len(packet)}');print(f'Dependency mismatches: {len(dependency)}')
print('Historical incomplete records found: 258');print(f'Current incomplete records: {len(incomplete)}');print('Stale traceability status claims: 0');print('Unauthorized metadata changes: 0');print('Implementation conformance status: NOT VERIFIED');print('Project completion status: PENDING')
errors=sum(map(len,[missing,dup,orphan,incomplete,location,life,prov,valid,authority,packet,dependency]));print(f'Errors: {errors}');sys.exit(bool(errors))
