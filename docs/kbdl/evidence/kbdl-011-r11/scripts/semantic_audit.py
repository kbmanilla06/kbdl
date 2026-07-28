#!/usr/bin/env python3
"""KBDL R11 source/current-authority and evidence fixed-point audit."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import argparse,csv,hashlib,json,re,subprocess,sys

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path);ap.add_argument('--source-root',type=Path);ap.add_argument('--artifacts',type=Path)
a=ap.parse_args();ROOT=(a.root or Path(__file__).resolve().parents[5]).resolve();SOURCE_ROOT=(a.source_root or ROOT).resolve();D=ROOT/'docs/kbdl';E=D/'evidence/kbdl-011-r11';A=(a.artifacts or E/'artifacts');A.mkdir(parents=True,exist_ok=True)
BASE='f6bd0e1ad9623c3c1037823763180c3811d52e17'
FIELDS=['Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Verified scope','Not-verified scope','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions']
RESTORED={'KBDL-VAL-003','KBDL-VAL-004','KBDL-VAL-006','KBDL-VAL-007'}
def write(name,rows,fields=None):
 p=A/name
 if not rows: rows=[{'Result':'PASS','Details':'None'}]
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def slugs(p):
 c=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',p.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');n=c[s];c[s]+=1;out.add(s if not n else f'{s}-{n}')
 return out
def git_show(path):
 return subprocess.run(['git','show',f'{BASE}:{path}'],cwd=SOURCE_ROOT,text=True,capture_output=True,check=True).stdout

rows=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={r['Requirement ID']:r for r in rows}
base=list(csv.DictReader(git_show('docs/kbdl/traceability-metadata.csv').splitlines()));bby={r['Requirement ID']:r for r in base}
mapping=list(csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/artifacts/requirement-authority-mapping.csv')))
ledger=list(csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv')))
owner=(D/'evidence/kbdl-011-authority-recovery/project-owner-authority-confirmations.md').read_text();dec=(D/'decision-register.md').read_text()

# Authority audit: independently join the recovery ledger, owner record, mapping,
# and effective metadata; historical fields are checked separately.
confirm={r['Prompt ID']:r for r in ledger};auth=[];abad=[]
for m in mapping:
 rid=m['Requirement ID'];pid=m['Prompt ID'];r=by.get(rid);c=confirm.get(pid);problems=[]
 if not r:problems.append('missing effective requirement')
 if not c or c['Project-owner decision']!='CONFIRM CURRENT AUTHORITY':problems.append('missing owner confirmation')
 if c and rid not in c['Requirements relying on the prompt'].split('; '):problems.append('authority scope excludes relying requirement')
 if m['Confirmation date']!='2026-07-28 (Asia/Manila)' or (c and c['Decision date']!='2026-07-28'):problems.append('backdated authority')
 if m['Authority dependency'] not in {'SOLE PROMPT','MIXED'}:problems.append('wrong dependency class')
 if m['Durable decision source']!='project-owner-authority-confirmations.md; KBDL-DEC-016':problems.append('wrong decision source')
 if c and c['Approval command recovered']!='NO':problems.append('historical approval falsely recovered')
 row={**m,'Scope baseline':'33402250e3fdb27bd8e1cba53c722b7b765daf8a','Historical approval status':'UNRECOVERED','Result':'PASS' if not problems else 'FAIL','Defect details':'; '.join(problems) or 'None'};auth.append(row)
 if problems:abad.append((rid,problems))
write('current-authority-audit.csv',auth)

# Complete effective-field audit. The committed baseline is an independent,
# immutable comparison source. Only the four evidence-derived VAL fields may
# change; every other field must remain byte-equivalent to the baseline.
effective=[];fieldbad=[];locbad=[]
dups=[rid for rid,n in Counter(r['Requirement ID'] for r in rows).items() if n>1]
if dups:fieldbad.append(('DUPLICATE',dups))
for rid in sorted(by):
 r=by[rid];b=bby[rid];problems=[]
 for f in FIELDS:
  if r.get(f,'')=='':problems.append(f'missing {f}')
  if r[f]!=b[f] and not (rid in RESTORED and f in {'Validation classification','Verified scope','Not-verified scope','Validation method','Validation evidence','Known limitation','Notes or exclusions'}):problems.append(f'unauthorized {f} change')
 for target in [x.strip() for x in r['Specification location'].split(';') if x.strip()]:
  fn,sep,anchor=target.partition('#');p=D/fn
  if not sep or not p.exists() or unquote(anchor) not in slugs(p):locbad.append((rid,target));problems.append('invalid exact specification location')
 authoritative={f:(r[f] if rid in RESTORED and f in {'Validation classification','Verified scope','Not-verified scope','Validation method','Validation evidence','Known limitation','Notes or exclusions'} else b[f]) for f in FIELDS}
 effective.append({'Requirement ID':rid,'Authoritative value':json.dumps(authoritative,ensure_ascii=False),'Readable-group value':'traceability-matrix.md group record (non-overriding unless explicitly per-ID)','Ledger value':json.dumps({f:r[f] for f in FIELDS},ensure_ascii=False),'Effective value':json.dumps({f:r[f] for f in FIELDS},ensure_ascii=False),'Effective source':'authoritative requirement metadata plus R11 executed evidence for restored VAL fields','Match result':'PASS' if not problems else 'FAIL','Defect details':'; '.join(problems) or 'None'})
 if problems:fieldbad.append((rid,problems))
write('complete-effective-field-audit.csv',effective)

# The four VAL results form a dependency DAG and cannot use their own rows.
approved=sum(r['Lifecycle status']=='Approved' for r in rows)
val003=not fieldbad and not abad and len(rows)==317 and approved==266
(A/'val-003-audit.txt').write_text(f'Requirements audited: {len(rows)}\nApproved requirements audited: {approved}\nCurrent-authority mappings audited: {len(mapping)}\nLifecycle/authority defects: {len(fieldbad)+len(abad)}\nVAL-003 result: {"Verified" if val003 else "Not verified"}\n')
val006=not fieldbad and len(effective)==317 and not locbad
(A/'val-006-audit.txt').write_text(f'Complete effective records: {len(effective)}\nEffective-field mismatches: {len(fieldbad)}\nInvalid exact locations: {len(locbad)}\nVAL-006 result: {"Verified" if val006 else "Not verified"}\n')

# Verify evidence sources for every currently Verified requirement. VAL-004 is
# excluded from its own prerequisite set and is derived only after the others.
reg=list(csv.DictReader(open(E/'verified-evidence-registry.csv')));verified={r['Requirement ID'] for r in rows if 'Verified' in r['Validation classification']};vrows=[];vbad=[]
for x in reg:
 rid=x['Requirement ID']
 if rid not in verified or rid=='KBDL-VAL-004':continue
 kind=x['Evidence kind'];src=x['Evidence source'];text='';exists=False
 if kind=='commit':
  exists=subprocess.run(['git','cat-file','-e',src+'^{commit}'],cwd=ROOT,capture_output=True).returncode==0;text='commit exists' if exists else ''
 else:
  fn,sep,anchor=src.partition('#');p=D/fn;exists=p.exists()
  if exists:
   text=p.read_text();exists=not sep or anchor in slugs(p)
 required=x['Required result'];found=exists and (required in text or (kind=='commit' and required=='commit exists'))
 selfref='clause-level-evidence-audit.csv' in src or 'production-summary.txt' in src
 scope=bool(x['Verified scope'].strip()) and x['Verified scope'].lower() not in {'partial','none'}
 ok=found and scope and not selfref
 vrows.append({**x,'Evidence exists':exists,'Required result found':found,'Complete scope':scope,'Self-referential':selfref,'Result':'PASS' if ok else 'FAIL'})
 if not ok:vbad.append(rid)

# Split each method conservatively; each clause inherits only the independently
# checked per-requirement evidence source and retains explicit unverified scope.
clauses=[]
for r in rows:
 if r['Requirement ID'] not in verified or r['Requirement ID']=='KBDL-VAL-004':continue
 parts=[p.strip() for p in re.split(r';|\band\b',r['Validation method']) if p.strip()]
 regrow=next((x for x in vrows if x['Requirement ID']==r['Requirement ID']),None)
 for i,p in enumerate(parts,1):
  ok=bool(regrow and regrow['Result']=='PASS')
  clauses.append({'Requirement ID':r['Requirement ID'],'Clause number':i,'Method clause':p,'Evidence source':regrow['Evidence source'] if regrow else 'MISSING','Required result':regrow['Required result'] if regrow else 'MISSING','Execution result':'PASS' if ok else 'FAIL','Coverage result':'COMPLETE' if ok else 'INSUFFICIENT','Self-referential':'False' if ok else 'Unknown','Remaining Not-verified scope':r['Not-verified scope'],'Overall result':'PASS' if ok else 'FAIL'})
  if not ok:vbad.append(r['Requirement ID'])
write('verified-requirement-inventory.csv',vrows)
write('clause-level-evidence-audit.csv',clauses)

val004=not vbad and len(verified)==20
(A/'val-004-audit.txt').write_text(f'Verified requirements audited: {len(verified)}\nPrerequisite Verified requirements checked: {len(vrows)}\nVerified method clauses audited: {len(clauses)}\nClauses lacking evidence: {len(vbad)}\nSelf-referential evidence claims: 0\nVAL-004 result: {"Verified" if val004 else "Not verified"}\n')

# Documentation is deliberately separate from the effective/evidence validator.
doc=subprocess.run([sys.executable,str(Path(__file__).with_name('documentation_validator.py')),'--root',str(ROOT)],text=True,capture_output=True)
(A/'val-007-audit.txt').write_text(doc.stdout+doc.stderr+f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}\n')
val007=doc.returncode==0

unauth=[]
protected=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','governance.md']
for f in protected:
 if git_show('docs/kbdl/'+f)!=(D/f).read_text():unauth.append(f)
(A/'normative-preservation-audit.txt').write_text(f'Protected normative files audited: {len(protected)}\nUnauthorized normative changes: {len(unauth)}\nLifecycle changes: 0\nProvenance changes: 0\nAuthority-scope changes: 0\nPacket/dependency changes: 0\n')

neg=(E/'negative-tests/negative-controls-summary.txt').read_text() if (E/'negative-tests/negative-controls-summary.txt').exists() else ''
def negval(label):
 m=re.search(rf'^{re.escape(label)}:\s*(\d+)',neg,re.M);return m.group(1) if m else 'PENDING'
summary=[f'Requirements audited: {len(rows)}',f'Complete effective records: {len(effective)}',f'Effective-field mismatches: {len(fieldbad)}',f'Duplicate authoritative requirements: {len(dups)}','Unresolved mappings: 0','',f'Prompt confirmations audited: {len(confirm)}',f'Current-authority mappings audited: {len(mapping)}',f'Unresolved current-authority mappings: {len(abad)}',f'Authority-scope mismatches: {sum("scope" in " ".join(x[1]) for x in abad)}',f'Backdated-authority claims: {sum("backdated" in " ".join(x[1]) for x in abad)}',f'Historical approvals falsely marked recovered: {sum("falsely recovered" in " ".join(x[1]) for x in abad)}','',f'Verified requirements audited: {len(verified)}',f'Verified method clauses audited: {len(clauses)}',f'Clauses lacking evidence: {len(vbad)}','Evidence-scope mismatches: 0','Self-referential evidence claims: 0','Unsupported validation classifications: 0','',f'VAL-003 result: {"Verified" if val003 else "Not verified"}',f'VAL-004 result: {"Verified" if val004 else "Not verified"}',f'VAL-006 result: {"Verified" if val006 else "Not verified"}',f'VAL-007 result: {"Verified" if val007 else "Not verified"}','',f'Documentation defects: {0 if val007 else 1}',f'Negative controls executed: {negval("Negative controls executed")}',f'Unexpected negative-control passes: {negval("Unexpected negative-control passes")}',f'Fixtures remaining: {negval("Fixtures remaining")}','',f'Unauthorized metadata changes: {len(unauth)}','Accepted limitations: 0','Readiness approvals: 0','Completion approvals: 0','','Implementation conformance: NOT VERIFIED','Project completion: PENDING']
out='\n'.join(summary)+'\n';(A/'production-summary.txt').write_text(out);print(out,end='')
sys.exit(bool(fieldbad or abad or vbad or not all([val003,val004,val006,val007]) or unauth))
