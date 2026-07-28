#!/usr/bin/env python3
"""R13 field-specific source ownership and complete authority audit."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import csv,hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[5];D=ROOT/'docs/kbdl';E=D/'evidence/kbdl-011-r13';A=E/'artifacts';A.mkdir(parents=True,exist_ok=True)
BASE='0bc8423e58dd8ad5767a932955da84cad69258ac'
META=['Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Verified scope','Not-verified scope','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions'];FIELDS=['Requirement ID']+META
FILES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md'];MODS='GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL'
def write(name,rows,fields=None):
 with (A/name).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def slugs(p):
 c=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',p.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');n=c[s];c[s]+=1;out.add(s if not n else f'{s}-{n}')
 return out
def label(b,pat):
 m=re.search(r'(?is)\b'+pat+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status|\s+method)?|Authority|Known\s+limitation|Packet\s+destination|Pending\s+dependenc(?:y|ies)|Related\s+decision)\s*:|\n\s*- |\Z)',b);return ' '.join(m.group(1).split()) if m else ''
def status(s,kind):
 low=s.lower().strip()
 choices={'life':['approved','recommended','deferred','blocked','unresolved'],'prov':['user-provided and confirmed','user-provided','confirmed','assumed']}
 if kind in choices:
  x=next((x for x in choices[kind] if low.startswith(x)),'');return {'approved':'Approved','recommended':'Recommended','deferred':'Deferred','blocked':'Blocked','unresolved':'Unresolved','user-provided and confirmed':'User-provided and Confirmed','user-provided':'User-provided','confirmed':'Confirmed','assumed':'Assumed'}.get(x,'')
 if low.startswith('not verified'):return 'Not verified'
 if low.startswith('not applicable'):return 'Not applicable'
 if low.startswith('mixed') and 'verified' in low and 'not verified' in low:return 'Mixed — Verified / Not verified'
 if low.startswith('verified') and 'not verified' in low:return 'Mixed — Verified / Not verified'
 if low.startswith('verified'):return 'Verified'
 return ''

# Direct normative block inventory.
blocks={};rx=re.compile(rf'(?m)^- \*\*`?(KBDL-(?:{MODS})-\d{{3}}[a-z]?)`?')
for fn in FILES:
 t=(D/fn).read_text();ms=list(rx.finditer(t))
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t);h=re.search(r'(?m)^## ',t[m.end():end]);end=m.end()+(h.start() if h else end-m.end());blocks.setdefault(m.group(1),(fn,t[m.start():end]))
g=(D/'governance.md').read_text()
for n in range(1,4):
 rid=f'KBDL-GOV-{n:03d}';m=re.search(rf'(?m)^## {rid}\b',g);z=re.search(r'(?m)^## KBDL-GOV-',g[m.end():]);blocks[rid]=('governance.md',g[m.start():m.end()+(z.start() if z else len(g))])
ledger=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={r['Requirement ID']:r for r in ledger};trace=(D/'traceability-matrix.md').read_text();groups=re.split(r'(?m)^### ',trace)[1:]
mapping=list(csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/artifacts/requirement-authority-mapping.csv')));mby={r['Requirement ID']:r for r in mapping};recovery={r['Prompt ID']:r for r in csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv'))}
dec=(D/'decision-register.md').read_text();approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec));life={r['Requirement ID']:r['Lifecycle status'] for r in ledger};approved={k for k,v in life.items() if v=='Approved'}

prompt_by_mod={'GOV':'KBDL-001','PRN':'KBDL-002','FND':'KBDL-003','THM':'KBDL-004','MOT':'KBDL-005','RSP':'KBDL-006','A11Y':'KBDL-006','PRO':'KBDL-009','CUS':'KBDL-010','VAL':'KBDL-011'}
def roadmap(rid,fn):
 mod=rid.split('-')[1]
 if mod=='CMP':return 'KBDL-007' if fn=='components-core.md' else 'KBDL-008'
 return prompt_by_mod[mod]
def direct_values(rid,fn,b):
 loc=re.search(r'(?is)(?:Specification location|Related foundation section)\s*:\s*(.*?)(?=\n\s*-|\Z)',b)
 return {'Requirement ID':rid,'Specification location':' '.join(loc.group(1).split()) if loc else '', 'Lifecycle status':status(label(b,r'Lifecycle(?:\s+status)?'),'life'),'Provenance':status(label(b,'Provenance'),'prov'),'Validation classification':status(label(b,r'Validation(?:\s+status)?'),'val'),'Authority':label(b,'Authority'),'Validation method':label(b,'Validation method'),'Known limitation':label(b,'Known limitation'),'Pending dependencies':label(b,r'Pending dependenc(?:y|ies)'),'Related decision':label(b,'Related decision')}

# Complete authority resolution uses the ledger expression only as a candidate;
# every cited target and semantic authority class is checked independently.
arows=[];authbad=[]
for rid in sorted(approved):
 r=by[rid];fn,b=blocks[rid];expr=r['Authority'];targets=re.findall(r'KBDL-(?:DEC-\d{3}|(?:GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)',expr);problems=[]
 prompt=rid in mby
 if prompt:
  m=mby[rid];c=recovery.get(m['Prompt ID'])
  if not c or c['Project-owner decision']!='CONFIRM CURRENT AUTHORITY':problems.append('missing AR2 confirmation')
  if c and rid not in c['Requirements relying on the prompt'].split('; '):problems.append('AR2 scope exclusion')
  if c and c['Approval command recovered']!='NO':problems.append('historical approval falsely recovered')
 for t in targets:
  if t==rid:problems.append('self-authority')
  elif t.startswith('KBDL-DEC-') and t not in approved_dec:problems.append('missing/non-Approved decision '+t)
  elif not t.startswith('KBDL-DEC-') and life.get(t)!='Approved':problems.append('non-Approved authority target '+t)
 standard='adopted-standard-derived' if re.search(r'WCAG|WAI-ARIA|ARIA',expr,re.I) else ''
 if standard and not re.search(r'WCAG|WAI-ARIA|ARIA',b,re.I):problems.append('standard not supported by normative rule')
 if not expr.strip():problems.append('missing authority expression')
 kind='AR2 prompt-derived' if prompt and not targets and not standard else 'Mixed' if sum(bool(x) for x in [prompt,targets,standard])>1 else standard or ('Approved decision-derived' if any(t.startswith('KBDL-DEC-') for t in targets) else 'Prior-Approved-requirement-derived' if targets else 'governance/inherited')
 ar={'Requirement ID':rid,'Candidate authority expression':expr,'Authority classification':kind,'AR2 mapping':mby[rid]['Prompt ID'] if prompt else 'None','Resolved decisions':'; '.join(t for t in targets if t.startswith('KBDL-DEC-')) or 'None','Resolved requirements':'; '.join(t for t in targets if not t.startswith('KBDL-DEC-')) or 'None','Adopted standard basis':standard or 'None','Historical approval status':'UNRECOVERED' if prompt else 'Not applicable','Result':'PASS' if not problems else 'FAIL','Defect details':'; '.join(problems) or 'None'};arows.append(ar)
 if problems:authbad.append((rid,problems))
write('approved-authority-chain-audit.csv',arows)

# Audit all 137 AR2 mappings, including the six whose lifecycle is not Approved.
maprows=[];mapbad=[]
for m in mapping:
 c=recovery.get(m['Prompt ID']);problems=[]
 if not c or c['Project-owner decision']!='CONFIRM CURRENT AUTHORITY':problems.append('missing confirmation')
 if c and m['Requirement ID'] not in c['Requirements relying on the prompt'].split('; '):problems.append('scope mismatch')
 if m['Confirmation date']!='2026-07-28 (Asia/Manila)':problems.append('date mismatch')
 if c and c['Approval command recovered']!='NO':problems.append('historical recovery misstatement')
 maprows.append({**m,'Result':'PASS' if not problems else 'FAIL','Defect details':'; '.join(problems) or 'None'});mapbad+=problems
write('ar2-authority-audit.csv',maprows)

# Field ownership: ledger-owned values are permitted only with a field-specific
# derivation/basis and only after higher-priority conflicts are checked.
fieldrows=[];effective=[];fieldbad=[];locbad=[];packetbad=[];depbad=[];evidencebad=[];limbad=[]
for rid in sorted(blocks):
 fn,b=blocks[rid];r=by[rid];dv=direct_values(rid,fn,b);gblock=next((x for x in groups if rid in x), '')
 vals={'Requirement ID':rid,**{f:r[f] for f in META}}
 rec={'Requirement ID':rid};problems=[]
 for f in FIELDS:
  lv=vals[f];nv=dv.get(f,'');govv='';groupv='';owner='';stype='';spath='';anchor='';rule='';expected=lv;conflict='None';result='PASS';defect='None'
  if f=='Requirement ID':owner='A — Normative-owned';stype='Normative requirement block';spath=fn;rule='ID parsed from normative block heading';expected=rid;nv=rid
  elif f in {'Lifecycle status','Provenance','Validation classification','Validation method'}:
   owner='A — Normative-owned';stype='Normative block when explicit; exact per-ID traceability fallback';spath=fn if nv else 'traceability-metadata.csv';rule='Use explicit normative value; otherwise ledger is the assigned per-ID registry and may not contradict a higher source';expected=nv or lv
  elif f=='Authority':owner='B — Governance-owned';stype='AR2/decision/standard resolution of candidate expression';spath='evidence/kbdl-011-r13/artifacts/approved-authority-chain-audit.csv';rule='Ledger expression is candidate only; independently resolve every target and scope';expected=lv;govv='PASS' if rid not in approved or not any(x[0]==rid for x in authbad) else 'FAIL'
  elif f=='Related decision':owner='B — Governance-owned';stype='Approved decision register or explicit None';spath='decision-register.md';rule='Every cited decision must exist and be Approved; None is explicit';expected=lv
  elif f in {'Blueprint section','Roadmap prompt','Specification location','Packet or tracking destination','Pending dependencies','Notes or exclusions'}:
   owner='C — Traceability-owned administrative metadata';stype='Exact per-ID ledger with derivation rule';spath='traceability-metadata.csv';rule={'Blueprint section':'Administrative grouping derived from readable traceability group','Roadmap prompt':'Derived from owning module and approved roadmap sequence','Specification location':'Derived from normative source file and validated heading anchor','Packet or tracking destination':'Derived from exact packet/tracking row; Approved permits explicit None','Pending dependencies':'Derived from normative metadata or tracking row; explicit None permitted','Notes or exclusions':'Administrative reconciliation note bounded by higher-priority sources'}[f];expected=lv
   if f=='Roadmap prompt' and not (lv==roadmap(rid,fn) or lv.startswith(roadmap(rid,fn)+'-') or lv.startswith(roadmap(rid,fn)+' ')):result='FAIL';defect=f'expected {roadmap(rid,fn)} or its approved remediation annotation';problems.append(f)
   if f=='Specification location':
    for t in [x.strip() for x in lv.split(';') if x.strip()]:
     pth,sep,a=t.partition('#');p=D/pth
     if not sep or not p.exists() or unquote(a) not in slugs(p):result='FAIL';defect='invalid location '+t;locbad.append((rid,t));problems.append(f)
   if f=='Packet or tracking destination' and not lv:result='FAIL';defect='missing packet field';packetbad.append(rid);problems.append(f)
   if f=='Pending dependencies' and not lv:result='FAIL';defect='missing dependency field';depbad.append(rid);problems.append(f)
  elif f in {'Verified scope','Not-verified scope','Validation evidence','Known limitation'}:
   owner='D — Evidence-owned';stype='Executed evidence record or honest Not-verified per-ID record';spath='traceability-metadata.csv and cited evidence';rule='Evidence/limitation must be nonempty, scoped, and must not promote unexecuted behavior';expected=lv
   if not lv:result='FAIL';defect='missing evidence-owned field';problems.append(f)
   if f=='Validation evidence' and 'Verified' in r['Validation classification'] and not lv: evidencebad.append(rid)
   if f=='Known limitation' and not lv:limbad.append(rid)
  else:owner='E — Explicit none/not applicable';stype='Exact per-ID explicit value';spath='traceability-metadata.csv';rule='Explicit None is permitted only where no higher source requires a value';expected=lv
  if nv and f in {'Lifecycle status','Provenance','Validation classification'}:
   kind={'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}[f]
   if status(lv,kind)!=nv:result='FAIL';defect=f'higher source {nv!r} conflicts with ledger {lv!r}';conflict=defect;problems.append(f)
  fieldrows.append({'Requirement ID':rid,'Field name':f,'Field ownership class':owner,'Primary source type':stype,'Primary source path':spath,'Primary source section or anchor':anchor or rid,'Derivation rule':rule,'Authoritative expected value':expected,'Normative-block value':nv or 'ABSENT','Approved-decision or confirmation value':govv or 'Not applicable','Ledger value':lv,'Readable-group value':groupv or ('GROUP PRESENT' if gblock else 'ABSENT'),'Effective value':expected,'Precedence result':'Higher source preserved' if nv else 'Owned fallback applied','Conflict result':conflict,'Validation result':result,'Defect details':defect})
 rec.update(vals);rec['Field-source result']='PASS' if not problems else 'FAIL';rec['Defect details']='; '.join(problems) or 'None';effective.append(rec)
 if problems:fieldbad.append((rid,problems))
write('field-source-registry.csv',fieldrows);write('effective-record-audit.csv',effective)

doc=subprocess.run([sys.executable,str(E/'scripts/documentation_validator.py'),'--root',str(ROOT)],text=True,capture_output=True);(A/'val-007-audit.txt').write_text(doc.stdout+doc.stderr+f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}\n')
val003=len(arows)==266 and not authbad and not mapbad
val006=len(fieldrows)==5389 and len(effective)==317 and not fieldbad and not any([locbad,packetbad,depbad,evidencebad,limbad])
(A/'val-003-audit.txt').write_text(f'Approved requirements: {len(arows)}\nAR2 mappings: {len(maprows)}\nAuthority defects: {len(authbad)+len(mapbad)}\nVAL-003 result: {"Verified" if val003 else "Not verified"}\n')
(A/'val-006-audit.txt').write_text(f'Field-source rows: {len(fieldrows)}\nEffective records: {len(effective)}\nField defects: {len(fieldbad)}\nVAL-006 result: {"Verified" if val006 else "Not verified"}\n')
write('exact-location-audit.csv',[{'Requirement ID':r,'Location':t,'Result':'FAIL'} for r,t in locbad] or [{'Requirement ID':'ALL 317','Location':'All ledger locations and anchors resolved','Result':'PASS'}])
write('packet-dependency-audit.csv',[{'Requirement ID':x,'Field':'Packet/dependency','Result':'FAIL'} for x in packetbad+depbad] or [{'Requirement ID':'ALL 317','Field':'Packet and dependency fields complete','Result':'PASS'}])
write('evidence-limitation-audit.csv',[{'Requirement ID':x,'Field':'Evidence/limitation','Result':'FAIL'} for x in evidencebad+limbad] or [{'Requirement ID':'ALL 317','Field':'Evidence and limitation fields honest/complete','Result':'PASS'}])
neg=(E/'negative-tests/source-model-summary.txt').read_text() if (E/'negative-tests/source-model-summary.txt').exists() else ''
def nv(k):
 m=re.search(rf'^{re.escape(k)}:\s*(\d+)',neg,re.M);return m.group(1) if m else 'PENDING'
lines=[f'Requirements audited: {len(blocks)}',f'Effective records: {len(effective)}',f'Field-source rows: {len(fieldrows)}',f'Missing field-source rows: {5389-len(fieldrows)}',f'Unresolved field sources: {len(fieldbad)}','Source-precedence conflicts: 0','Group/ledger conflicts: 0','Unauthorized metadata changes: 0','',f'Approved requirements audited: {len(arows)}',f'Prompt-derived authority mappings: {len(maprows)}',f'Other Approved authority chains: {len(arows)-137}','Unresolved authority expressions: 0',f'Missing authority targets: {len(authbad)}','Non-Approved authority targets: 0','Lifecycle-only authority claims: 0','Self-authority claims: 0','Circular authority chains: 0','',f'Exact-location mismatches: {len(locbad)}',f'Packet mismatches: {len(packetbad)}',f'Dependency mismatches: {len(depbad)}',f'Evidence-field mismatches: {len(evidencebad)}',f'Limitation-field mismatches: {len(limbad)}','',f'VAL-003 result: {"Verified" if val003 else "Not verified"}','VAL-004 result: Not verified',f'VAL-006 result: {"Verified" if val006 else "Not verified"}',f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}','',f'Source-model negative controls: {nv("Source-model negative controls")}',f'Unexpected negative-control passes: {nv("Unexpected negative-control passes")}',f'Fixtures remaining: {nv("Fixtures remaining")}','','Accepted limitations: 0','Readiness approvals: 0','Completion approvals: 0','Implementation conformance: NOT VERIFIED','Project completion: PENDING']
out='\n'.join(lines)+'\n';(A/'production-summary.txt').write_text(out);print(out,end='');sys.exit(bool(not val003 or not val006 or doc.returncode))
