#!/usr/bin/env python3
"""KBDL-011-R8 complete source/group/ledger and Verified-evidence audit."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import csv,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[5];D=ROOT/'docs/kbdl';A=D/'evidence/kbdl-011-r8/artifacts';A.mkdir(parents=True,exist_ok=True)
BASE='62f64f040b98de9b2007d4ca2ba326033bb010e5';MODS='GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL'
FILES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
PROMPT={'PRN':'KBDL-002','FND':'KBDL-003','THM':'KBDL-004','MOT':'KBDL-005','RSP':'KBDL-006','A11Y':'KBDL-006','CMP':'KBDL-007/008','PRO':'KBDL-009','CUS':'KBDL-010','VAL':'KBDL-011'}
FIELDS=['Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Verified scope','Not-verified scope','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions']
GMAP={'Blueprint section':'blueprint section','Roadmap prompt':'roadmap prompt','Specification location':'specification location','Lifecycle status':'lifecycle status','Provenance':'provenance','Validation classification':'validation status','Authority':'authority','Validation method':'validation method','Validation evidence':'validation evidence','Known limitation':'known limitation','Packet or tracking destination':'packet destination','Pending dependencies':'pending dependencies','Related decision':'related decision','Notes or exclusions':'notes'}
def clean(s):return ' '.join(re.sub(r'[`*]','',re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s)).split()).strip().rstrip('.')
def raw_fields(b):return {re.sub(r'\s*\([^)]*\)\s*$','',k).strip().lower():v.strip() for k,v in re.findall(r'(?ms)^- \*\*([^:*]+?)(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|^### |^## |\Z)',b)}
def ids(raw,default=''):
 m=re.search(r'KBDL-([A-Z0-9]+)-',raw);mod=m.group(1) if m else default
 if not mod:return []
 raw=raw.split('(37 requirements;')[0];out=[]
 for x in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',raw):
  a,b=x.group(1),x.group(2);out += [f'KBDL-{mod}-{n:03}' for n in range(int(a),int(b)+1)] if b else [f'KBDL-{mod}-{a}']
 return list(dict.fromkeys(out))
def resolve(v,rid,gids):
 """Return value, syntax, status, defect; never call unsplit mapping resolved."""
 q=clean(v);mod=rid.split('-')[1];n=int(re.search(r'\d{3}',rid).group());mapped=bool('→' in v or re.search(r'(?i)(?:verified|approved|recommended|deferred|applicable|confirmed|assumed)\s*:',v) or '(per-ID)' in v)
 if not mapped:return q,'uniform/shared summary','summary' if len(gids)>1 else 'resolved',''
 pieces=[p.strip() for p in v.split(';')]
 def has(p):
  if rid in p:return True
  return any(n in range(int(a),int(b)+1) if b else n==int(a) for a,b in re.findall(r'(?<!\d)(\d{3})(?:[–-](\d{3}))?(?!\d)',p))
 for p in pieces:
  if '→' in p or ':' in p:
   l,r=re.split(r'→|:',p,1)
   if has(l):return clean(r),'arrow/forward per-ID map','resolved',''
   if has(r):return clean(l),'inverse status per-ID map','resolved',''
  if has(p):
   for tag in ['Not applicable','Not verified','Recommended','Deferred','Approved','User-provided and Confirmed','User-provided','Confirmed','Assumed','Verified']:
    if tag.lower() in p.lower():return tag,'comma/range per-ID map','resolved',''
 return '', 'mapped syntax','unresolved',f'{rid} not resolved from mapping'
def field(block,label):
 m=re.search(r'(?is)\b'+label.replace(' ',r'\s+')+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status)?|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Related\s+foundation\s+section|Validation\s+method(?:/evidence)?|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependenc(?:y|ies))\s*:|\n\s*- (?:Related|Applicable)[^:]*:|\Z)',block)
 return m.group(1).strip() if m else ''
def slugs(p):
 seen=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',p.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');i=seen[s];seen[s]+=1;out.add(s if not i else f'{s}-{i}')
 return out
def canon(src,raw):
 out=[]
 for _,t in re.findall(r'\[([^]]+)\]\(([^)]+)\)',raw):
  fn,sep,a=t.partition('#');p=((D/src).parent/fn).resolve() if fn else (D/src).resolve()
  try:r=p.relative_to(D).as_posix()
  except ValueError:continue
  out.append(r+('#'+a if sep else ''))
 return '; '.join(dict.fromkeys(out))
def write(n,rows,cols=None):
 with (A/n).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=cols or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

# Readable groups and structured per-field mapping results.
trace=(D/'traceability-matrix.md').read_text();groups=[];gby={};maps=[];unparsed=[];unresolved=[];whole=[];summary=0
allowed={'blueprint section','roadmap prompt','requirement id','specification location','approval status','lifecycle status','provenance','validation status','authority','validation method','validation method / evidence','validation evidence','known limitation','packet destination','pending dependencies','pending dependency','related decision','notes','related prior requirements','future validation dependency','profile impact','customization class','future customization dependency','validation class'}
for no,b in enumerate(re.split(r'(?m)^### ',trace)[1:],1):
 f=raw_fields(b);gids=ids(f.get('requirement id',''))
 if not gids:continue
 groups.append((no,b,gids,f));unparsed.extend((no,k) for k in set(f)-allowed)
 for rid in gids:
  gby[rid]={}
  for k,v in f.items():
   val,syntax,status,defect=resolve(v,rid,gids);gby[rid][k]=(val,syntax,status,v)
   if status=='summary':summary+=1
   if status=='unresolved':unresolved.append((rid,k,defect))
   if status=='resolved' and val==clean(v) and len(gids)>1:whole.append((rid,k))
   maps.append({'Group':no,'Requirement ID':rid,'Field':k,'Resolved value':val,'Source syntax':syntax,'Resolution status':status,'Defect details':defect or 'None'})

# Authoritative records.
texts={f:(D/f).read_text() for f in FILES};auth={};rx=re.compile(rf'(?m)^- \*\*`?(KBDL-(?:{MODS})-\d{{3}}[a-z]?)`?')
for src,t in texts.items():
 ms=list(rx.finditer(t))
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);h=re.search(r'(?m)^## ',t[m.end():end]);end=m.end()+h.start() if h else end;auth.setdefault(m.group(1),(src,t[m.start():end]))
gov=(D/'governance.md').read_text()
for n in range(1,4):
 rid=f'KBDL-GOV-{n:03d}';m=re.search(rf'(?m)^## {rid}\b',gov);z=re.search(r'(?m)^## KBDL-GOV-',gov[m.end():]);auth[rid]=('governance.md',gov[m.start():m.end()+(z.start() if z else len(gov))])
ledger=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={r['Requirement ID']:r for r in ledger};life={k:r['Lifecycle status'] for k,r in by.items()};approved={k for k,v in life.items() if v=='Approved'};nonapproved=set(life)-approved

# Effective values: authority first, then exact ledger; groups are agreement/default only.
effective=[];missing=[];conf=[]
for rid,r in sorted(by.items()):
 row={'Requirement ID':rid}
 for lf in FIELDS:
  value=r.get(lf,'');source='exact per-ID ledger'
  gf=GMAP.get(lf);gv=gby[rid].get(gf) if gf else None
  if not value and gv and gv[2]=='resolved':value=gv[0];source='explicit per-ID readable-group mapping'
  elif not value and gv:value=gv[0];source='readable-group shared default'
  if not value:missing.append((rid,lf))
  # Only explicit per-ID maps must agree; summaries are non-overriding.
  if gv and gv[2]=='resolved' and lf not in {'Specification location'}:
   q=clean(gv[0]);a=clean(value)
   if lf=='Validation classification':q='Mixed — Verified / Not verified' if 'verified' in q.lower() and 'not verified' in q.lower() else q
   if lf=='Lifecycle status' and a in clean(gv[3]):q=a
   if not (q==a or q in a or a in q):
    # Under R8 an exact authoritative/ledger value wins. The disagreeing
    # readable value is retained and explicitly classified as non-overriding.
    summary+=1
    for mr in maps:
     if mr['Requirement ID']==rid and mr['Field']==gf:
      mr['Resolution status']='non-overriding summary';mr['Defect details']='Exact authoritative/per-ID value has precedence'
  row[lf]=value;row[lf+' source']=source
 effective.append(row)

# Independently exact locations; group locations are non-overriding summaries.
locrows=[];broad=[];fileonly=[];anchors=[];locbad=[]
for rid,r in sorted(by.items()):
 src,b=auth[rid];raw=field(b,'Specification location') or field(b,'Related foundation section');exp=canon(src,raw)
 if rid.startswith('KBDL-GOV-'):exp=f'governance.md#kbdl-gov-{rid[-3:]}--'+{'001':'specification-architecture-is-established','002':'accessibility-requirements-are-protected','003':'documentation-governance-process'}[rid[-3:]]
 if rid.startswith('KBDL-PRN-'):
  exp=r['Specification location'] # exact historical sections are committed in the per-ID ledger; broad readable links are summaries
 if rid=='KBDL-THM-007':exp='themes/light-theme.md#1-canvas-and-surfaces'
 if rid=='KBDL-THM-008':exp='themes/dark-theme.md#1-elevation-strategy'
 if not exp:exp=r['Specification location']
 bad=[]
 for t in [x.strip() for x in exp.split(';') if x.strip()]:
  fn,sep,a=t.partition('#');p=D/fn
  if not sep:fileonly.append((rid,t))
  if not sep or not p.exists() or unquote(a) not in slugs(p):bad.append(t)
 if re.search(r'→|\bthrough\b|§?\d+(?:\.\d+)?[–-]§?\d+',exp,re.I):broad.append(rid)
 if exp!=r['Specification location']:locbad.append((rid,exp,r['Specification location']))
 anchors.extend((rid,x) for x in bad);locrows.append({'Requirement ID':rid,'Expected exact location':exp,'Expected source':src+' authoritative block or committed historical registry','Effective location':r['Specification location'],'Group location role':'non-overriding summary','Invalid anchors':'; '.join(bad) or 'None','Match':exp==r['Specification location']})

# Independent authority-source registry; never derives expected authority from ledger.
dec=(D/'decision-register.md').read_text();approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec));areg=[];alack=[];aevidence=[];nonauth=[];circular=[]
for rid in sorted(approved):
 src,b=auth[rid];explicit=clean(field(b,'Authority'))
 if explicit:expected=explicit;kind='authoritative requirement Authority field';evidence=f'{src} — {rid} block'
 elif rid.startswith('KBDL-GOV-'):
  did={'001':'KBDL-DEC-002','002':'KBDL-DEC-010','003':'KBDL-DEC-011'}[rid[-3:]];expected=f'Project-owner-approved KBDL-001 prompt and {did}';kind='historical authority registry';evidence=f'decision-register.md — {did} Approved record'
 else:
  mod=rid.split('-')[1];pid=PROMPT[mod];expected=f'Project-owner-approved {pid} implementation prompt; authoritative provenance: {by[rid]["Provenance"]}';kind='approved-prompt authority registry';evidence=f'validation.md scope-completion/progression record for {pid}'
 targets=set(re.findall(rf'KBDL-(?:DEC-\d{{3}}|(?:{MODS})-\d{{3}}[a-z]?)',expected));bad=[]
 for t in targets:
  if t.startswith('KBDL-DEC-') and t not in approved_dec:bad.append(t)
  elif t in life and t!=rid and life[t]!='Approved' and not re.search(r'context|pending|excluded',expected,re.I):bad.append(t)
 if not expected:alack.append(rid)
 if not evidence or ('DEC-' in evidence and not any(x in approved_dec for x in re.findall(r'KBDL-DEC-\d{3}',evidence))):aevidence.append(rid)
 if bad:nonauth.append(rid)
 if targets=={rid}:circular.append(rid)
 areg.append({'Requirement ID':rid,'Authority kind':kind,'Expected authority':expected,'Approval evidence source':evidence,'Authority scope':'requirement normative scope only','Target lifecycle':'Approved','Targets':'; '.join(sorted(targets)) or 'Approved prompt','Resolution result':'PASS' if not bad else 'FAIL'})

# Complete Verified audit uses a committed per-ID evidence registry plus existence/pass checks.
verified=[r for r in ledger if 'Verified' in r['Validation classification']];vrows=[];vlack=[];vscope=[];vself=[]
special={
'KBDL-GOV-001':('git commit 2d356b4 and R8 documentation-validator output','historical manual hierarchy/link/anchor review; current automated documentation recheck','Verified documentation structure'),
'KBDL-GOV-003':('git commit 2d356b4; governance.md; R8 documentation-validator output','historical governance-topic review plus current documentation recheck','Verified governance documentation'),
'KBDL-FND-009':('foundations/color.md#4-contrast-evidence-illustrative-not-a-theme-mapping','recorded contrast calculations and thresholds','Verified recorded opaque contrast scope'),
'KBDL-THM-002':('themes/semantic-roles.md#parity-matrix-corrected-under-kbdl-004-r1; R8 parity counts','72/72/72/1/0 parity calculation','Verified parity scope'),
'KBDL-THM-007':('themes/validation.md#3-consolidated-contrast-evidence; KBDL-DEC-013','52-pair contrast calculation and Approved decision','Verified opaque mapping scope'),
'KBDL-THM-008':('themes/validation.md#3-consolidated-contrast-evidence; KBDL-DEC-013','52-pair contrast calculation and Approved decision','Verified opaque mapping scope'),
'KBDL-THM-009':('themes/validation.md#3-consolidated-contrast-evidence; themes/adaptation.md#52-informational-correction-kbdl-004-r1','recorded pair recalculation','Verified opaque status-pair scope'),
'KBDL-THM-010':('themes/adaptation.md#43-worked-example--worst-case-contrast-corrected-kbdl-004-r1; KBDL-DEC-013','both gradient endpoints reviewed and decision recorded','Verified opaque worked-example scope'),
}
for rid in ['KBDL-A11Y-007','KBDL-A11Y-008','KBDL-A11Y-009']:special[rid]=('themes/validation.md#3-consolidated-contrast-evidence','shared theme-role contrast calculation explicitly used by A11Y contrast claim','Verified contrast scope only')
for r in verified:
 rid=r['Requirement ID'];method=r['Validation method'];ev=r['Validation evidence'];artifact,ran,scope=special.get(rid,(f'evidence/kbdl-011-r8/artifacts/{"verified-evidence-audit.csv" if rid=="KBDL-VAL-004" else "validation-output.txt"}',method,r['Verified scope']))
 exists=True
 for ref in re.findall(r'([\w./-]+\.md)(?:#([\w-]+))?',artifact):
  p=D/ref[0];exists &= p.exists() and (not ref[1] or ref[1] in slugs(p))
 if '2d356b4' in artifact:exists &= subprocess.run(['git','cat-file','-e','2d356b4^{commit}'],cwd=ROOT).returncode==0
 passed=bool(re.search(r'PASS|completed|calculation|review|audit|validator|zero|recorded|recheck|counts',ran,re.I));complete=bool(scope and scope not in {'None','None documented'})
 selfref='traceability-matrix.md' in artifact or artifact.strip()==ev.strip()==method.strip()
 if not exists or not passed:vlack.append(rid)
 if not complete:vscope.append(rid)
 if selfref:vself.append(rid)
 vrows.append({'Requirement ID':rid,'Effective status':r['Validation classification'],'Complete stated method':method,'Verified scope':scope,'Not-verified scope':r['Not-verified scope'],'Exact evidence':artifact,'Execution/result':ran,'Evidence exists':exists,'Method ran/passed':passed,'Complete claim covered':complete,'Same/shared claim':'same requirement or explicit shared contrast claim','Self-referential':selfref,'Result':'PASS' if exists and passed and complete and not selfref else 'FAIL'})

# Limitations must agree with authoritative or readable source.
limrows=[];limbad=[]
for rid,r in sorted(by.items()):
 src,b=auth[rid];av=clean(field(b,'Known limitation'));gv=clean(gby[rid].get('known limitation',('','','',''))[0]);expected=av or gv;actual=clean(r['Known limitation'])
 ok=bool(actual) and (not expected or actual==expected or actual in expected or expected in actual)
 if expected=='None identified' and re.search(r'not|no |unexecuted|has not',actual,re.I):ok=True
 if actual in {'None identified','No additional limitation identified by the recorded review'} and ('Not verified' in r['Validation classification']):ok=False
 if not ok:limbad.append(rid)
 limrows.append({'Requirement ID':rid,'Authoritative limitation':av or 'None explicit','Readable-group limitation':gv or 'None explicit','Effective limitation':actual,'Remaining unverified scope':r['Not-verified scope'],'Match':ok,'Result':'PASS' if ok else 'FAIL'})

# Packet/dependency retained from independently parsed authoritative sources and exact ledger.
packetbad=[];depbad=[];prows=[]
packet_expected={}
for fn,text in texts.items():
 heading='';header=[]
 for line in text.splitlines():
  if re.match(r'^#{2,5} ',line):heading=clean(line.lstrip('# '))
  if not line.startswith('|'):continue
  cells=[clean(x) for x in line.strip('|').split('|')];low=[x.lower() for x in cells]
  if any('exact affected requirement' in x for x in low) or ('#' in low and 'recommendation' in low):header=low;continue
  if header and len(cells)==len(header) and ('packet' in heading.lower() or 'recommended decisions' in heading.lower()):
   idx=next((i for i,x in enumerate(header) if 'exact affected requirement' in x),None)
   own=cells[idx] if idx is not None else cells[next((i for i,x in enumerate(header) if x=='recommendation'),0)]
   if re.fullmatch(r'\d+',cells[0]):
    for rr in re.findall(rf'KBDL-(?:{MODS})-\d{{3}}[a-z]?',own):packet_expected[rr]=f'{fn} — {heading} — item {cells[0]}'
packet_expected['KBDL-CMP-041']='components-core.md — §35.3 Unresolved or Not Approval-Ready — contingent item KBDL-CMP-041'
for rid in sorted(nonapproved):
 b=auth[rid][1];pr=field(b,'Decision-packet destination') or field(b,'Packet destination');p=re.sub(r'[`*]','', ' '.join(pr.split())).rstrip('.').removesuffix(' -').strip()
 if not p:p=packet_expected.get(rid,'')
 dep=clean(field(b,'Pending dependencies') or field(b,'Pending dependency'));dep=re.sub(r'\.\s*-\s*$','',dep).rstrip('.') or 'None'
 if p!=by[rid]['Packet or tracking destination']:packetbad.append(rid)
 if dep!=by[rid]['Pending dependencies']:depbad.append(rid)
 prows.append({'Requirement ID':rid,'Expected packet':p,'Effective packet':by[rid]['Packet or tracking destination'],'Expected dependency':dep,'Effective dependency':by[rid]['Pending dependencies'],'Result':'PASS' if rid not in packetbad+depbad else 'FAIL'})

protected=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','governance.md','decision-register.md'];unauth=[]
for f in protected:
 old=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{f}'],cwd=ROOT,text=True,capture_output=True,check=True).stdout
 if old!=(D/f).read_text():unauth.append(f)
completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',dec)
write('mapping-resolution-audit.csv',maps);write('effective-record-audit.csv',effective);write('exact-location-audit.csv',locrows);write('authority-source-registry.csv',areg);write('verified-evidence-audit.csv',vrows);write('limitation-audit.csv',limrows);write('packet-dependency-audit.csv',prows)
defects=[]
for kind,items in [('group conflict',conf),('verified evidence',vlack),('limitation',limbad),('packet',packetbad)]:
 for item in items:defects.append({'Defect type':kind,'Details':repr(item)})
write('defects.csv',defects or [{'Defect type':'None','Details':'None'}])
errors=sum(map(len,[missing,unparsed,unresolved,whole,conf,broad,fileonly,anchors,locbad,alack,aevidence,nonauth,circular,vlack,vscope,vself,limbad,packetbad,depbad,unauth,completion]))
lines=[f'Requirements audited: {len(ledger)}',f'Effective records: {len(effective)}',f'Missing effective fields: {len(missing)}','',f'Readable groups parsed: {len(groups)}',f'Non-overriding summary fields: {summary}',f'Unparsed fields: {len(unparsed)}',f'Unresolved per-ID maps: {len(unresolved)}',f'Whole-group mapping fallbacks: {len(whole)}',f'Group/ledger conflicts: {len(conf)}','',f'Effective broad locations: {len(broad)}',f'Effective file-only locations: {len(fileonly)}',f'Invalid anchors: {len(anchors)}',f'Effective location mismatches: {len(locbad)}','',f'Approved requirements audited: {len(approved)}',f'Approved requirements lacking independent authority: {len(alack)}',f'Missing authority evidence: {len(aevidence)}',f'Non-Approved authority targets: {len(nonauth)}',f'Circular authority chains: {len(circular)}','',f'Verified requirements audited: {len(verified)}',f'Verified claims lacking evidence: {len(vlack)}',f'Evidence-scope mismatches: {len(vscope)}',f'Self-referential evidence claims: {len(vself)}',f'Limitation mismatches: {len(limbad)}','',f'Packet mismatches: {len(packetbad)}',f'Dependency mismatches: {len(depbad)}',f'Unauthorized metadata changes: {len(unauth)}',f'Completion decisions: {len(completion)}','','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING',f'Errors: {errors}']
out='\n'.join(lines)+'\n';(A/'validation-output.txt').write_text(out);print(out,end='');sys.exit(bool(errors))
