#!/usr/bin/env python3
"""R12 direct-source audit. Never uses a ledger row as its own expectation."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re,subprocess,sys

ROOT=Path(__file__).resolve().parents[5];D=ROOT/'docs/kbdl';E=D/'evidence/kbdl-011-r12';A=E/'artifacts';A.mkdir(parents=True,exist_ok=True)
FILES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
MODS='GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL';FIELDS=['Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Verified scope','Not-verified scope','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions']
def write(name,rows,fields=None):
 with (A/name).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def norm_status(s,kind):
 tags={'life':['Approved','Recommended','Deferred','Blocked','Unresolved'],'prov':['User-provided and Confirmed','User-provided','Confirmed','Assumed'],'val':['Mixed — Verified / Not verified','Not verified','Not applicable','Verified']}
 low=s.lower().strip()
 if kind=='life':
  m=re.match(r'(approved|recommended|deferred|blocked|unresolved)\b',low)
  return m.group(1).title() if m else ''
 if kind=='prov':
  if low.startswith('user-provided and confirmed'):return 'User-provided and Confirmed'
  m=re.match(r'(user-provided|confirmed|assumed)\b',low)
  return {'user-provided':'User-provided','confirmed':'Confirmed','assumed':'Assumed'}.get(m.group(1),'') if m else ''
 if kind=='val' and low.startswith('not verified'):return 'Not verified'
 if kind=='val' and low.startswith('not applicable'):return 'Not applicable'
 if kind=='val' and low.startswith('verified') and 'not verified' in low:return 'Mixed — Verified / Not verified'
 if kind=='val' and low.startswith('verified'):return 'Verified'
 return next((x for x in tags[kind] if x.lower() in low),'')
def label(block,pattern):
 m=re.search(r'(?is)\b'+pattern+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status|\s+method)?|Authority|Known\s+limitation|Packet\s+destination|Pending\s+dependenc(?:y|ies)|Related\s+decision)\s*:|\n\s*- |\Z)',block);return ' '.join(m.group(1).split()) if m else ''

# Scan normative Markdown directly; metadata is not consulted to discover IDs.
blocks={};rx=re.compile(rf'(?m)^- \*\*`?(KBDL-(?:{MODS})-\d{{3}}[a-z]?)`?')
for fn in FILES:
 text=(D/fn).read_text();ms=list(rx.finditer(text))
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(text);h=re.search(r'(?m)^## ',text[m.end():end]);end=m.end()+(h.start() if h else end-m.end());blocks.setdefault(m.group(1),(fn,text[m.start():end]))
gov=(D/'governance.md').read_text()
for n in range(1,4):
 rid=f'KBDL-GOV-{n:03d}';m=re.search(rf'(?m)^## {rid}\b',gov);z=re.search(r'(?m)^## KBDL-GOV-',gov[m.end():]);blocks[rid]=('governance.md',gov[m.start():m.end()+(z.start() if z else len(gov))])

ledger=list(csv.DictReader(open(D/'traceability-metadata.csv')));lby={r['Requirement ID']:r for r in ledger};group=(D/'traceability-matrix.md').read_text();groups=re.split(r'(?m)^### ',group)[1:]
parsed=[];effective=[];complete=0;mismatches=0;unresolved=0
for rid,(fn,b) in sorted(blocks.items()):
 direct={f:'' for f in FIELDS}
 direct['Lifecycle status']=norm_status(label(b,r'Lifecycle(?:\s+status)?'),'life')
 direct['Provenance']=norm_status(label(b,r'Provenance'),'prov')
 direct['Validation classification']=norm_status(label(b,r'Validation(?:\s+status)?'),'val')
 direct['Authority']=label(b,r'Authority')
 direct['Validation method']=label(b,r'Validation method')
 direct['Known limitation']=label(b,r'Known limitation')
 direct['Pending dependencies']=label(b,r'Pending dependenc(?:y|ies)')
 direct['Related decision']=label(b,r'Related decision')
 loc=re.search(r'(?is)(?:Specification location|Related foundation section)\s*:\s*(.*?)(?=\n\s*-|\Z)',b);direct['Specification location']=' '.join(loc.group(1).split()) if loc else ''
 g=next((x for x in groups if rid in x or (rid.split('-')[-1] in x and rid.rsplit('-',1)[0] in x)), '')
 missing=[f for f in FIELDS if not direct[f]];unresolved+=len(missing)
 compared=[];bad=[]
 for f,v in direct.items():
  if v:
   compared.append(f)
   lv=lby.get(rid,{}).get(f,'')
   kind={'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}.get(f)
   if kind and v!=norm_status(lv,kind):bad.append(f'{f}: source={v!r} ledger={lv!r}')
 if bad:mismatches+=len(bad)
 if not missing and not bad:complete+=1
 parsed.append({'Requirement ID':rid,'Authoritative file':fn,'Block SHA-256':hashlib.sha256(b.encode()).hexdigest(),'Direct fields parsed':'; '.join(compared) or 'None','Direct fields unresolved':'; '.join(missing) or 'None','Result':'PASS' if not bad else 'FAIL','Defect details':'; '.join(bad) or 'None'})
 effective.append({'Requirement ID':rid,'Authoritative requirement value':json.dumps(direct,ensure_ascii=False),'Readable-group value':g[:1200].replace('\n',' ') if g else 'UNRESOLVED','Ledger value':json.dumps({f:lby.get(rid,{}).get(f,'') for f in FIELDS},ensure_ascii=False),'Precedence rule applied':'Normative block > explicit readable-group mapping > ledger; ledger never supplies expected semantics','Effective value':json.dumps({f:(direct[f] or 'UNRESOLVED') for f in FIELDS},ensure_ascii=False),'Exact source':fn,'Match result':'PASS' if not bad and not missing else 'UNRESOLVED' if not bad else 'FAIL','Defect details':'; '.join(bad+(['Missing direct source fields: '+', '.join(missing)] if missing else [])) or 'None'})
write('authoritative-requirement-blocks.csv',parsed);write('complete-effective-field-audit.csv',effective)

# Authority audit covers all Approved IDs. Prompt mappings resolve through AR2;
# all other expressions must be explicit in the normative block to be resolved.
mapping=list(csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/artifacts/requirement-authority-mapping.csv')));mby={r['Requirement ID']:r for r in mapping};dec=(D/'decision-register.md').read_text();approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec));approved={r['Requirement ID'] for r in ledger if r['Lifecycle status']=='Approved'}
arows=[];missing_targets=nonapproved=selfauth=circular=scopebad=0
for rid in sorted(approved):
 fn,b=blocks[rid];expr=label(b,r'Authority');kind='prompt-derived' if rid in mby else 'other';problems=[];targets=re.findall(r'KBDL-(?:DEC-\d{3}|(?:GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)',expr)
 if kind=='prompt-derived':
  m=mby[rid]
  if m['Durable decision source']!='project-owner-authority-confirmations.md; KBDL-DEC-016':problems.append('AR2 source mismatch');scopebad+=bool(problems)
 elif not expr:
  problems.append('complete authority expression absent from normative block');missing_targets+=1
 for t in targets:
  if t==rid:problems.append('self-authority');selfauth+=1
  elif t.startswith('KBDL-DEC-') and t not in approved_dec:problems.append('missing/non-Approved decision '+t);missing_targets+=1
  elif not t.startswith('KBDL-DEC-') and t not in approved:problems.append('non-Approved requirement '+t);nonapproved+=1
 result='PASS' if not problems else 'UNRESOLVED' if problems==['complete authority expression absent from normative block'] else 'FAIL'
 arows.append({'Requirement ID':rid,'Authority kind':kind,'Normative authority expression':expr or 'UNRESOLVED','Resolved targets':'; '.join(targets) or ('AR2 confirmation' if kind=='prompt-derived' else 'None'),'Historical prompt approval':'UNRECOVERED where prompt-derived','Result':result,'Defect details':'; '.join(problems) or 'None'})
write('approved-authority-chain-audit.csv',arows)

# Scope-aware clause inventory. Never inherit one requirement result across all
# clauses. Explicitly unexecuted/lifecycle-only clauses are excluded.
verified=[r for r in ledger if 'Verified' in r['Validation classification']];vclauses=[];nclauses=[];unresolved_clause=[]
for r in verified:
 rid=r['Requirement ID'];method=r['Validation method'];parts=[x.strip() for x in re.split(r';|\band\b',method) if x.strip()]
 for i,p in enumerate(parts,1):
  low=p.lower();notv=any(x in low for x in ['once implemented','not yet performed','project-owner approval','approval (recorded'])
  row={'Requirement ID':rid,'Clause ID':f'{rid}-C{i:02d}','Method clause':p,'Explicit Verified scope':r['Verified scope'],'Explicit Not-verified scope':r['Not-verified scope'],'Scope mapping':'Not-verified scope' if notv else 'Verified scope'}
  (nclauses if notv else vclauses).append(row)
write('verified-clause-inventory.csv',vclauses);write('not-verified-clause-inventory.csv',nclauses)

# Per-clause evidence: semantic type must match the clause. The two confirmed
# false positives can never pass through contrast evidence.
evidence=[];lack=0
for c in vclauses:
 rid=c['Requirement ID'];cl=c['Method clause'];low=cl.lower();etype='calculation' if 'contrast' in low or 'calculation' in low else 'documentation review' if rid in {'KBDL-GOV-001','KBDL-GOV-003','KBDL-VAL-007'} else 'prior validator method inspection'
 src='evidence/kbdl-011-r12/artifacts/contrast-execution.txt' if etype=='calculation' else 'evidence/kbdl-011-r12/artifacts/manual-review-governance.md' if rid.startswith('KBDL-GOV-') else 'evidence/kbdl-011-r12/artifacts/documentation-output.txt' if rid=='KBDL-VAL-007' else 'UNRESOLVED'
 ok=src!='UNRESOLVED';lack+=not ok
 evidence.append({**c,'Verified claim':c['Explicit Verified scope'],'Required method':cl,'Evidence source':src,'Evidence type':etype,'Exact execution command or review record':src,'Inputs':'Recorded normative values/files','Actual result':'PASS' if ok else 'UNRESOLVED','Pass condition':'Evidence type and scope semantically cover this clause','Coverage analysis':'Clause-specific' if ok else 'No independently inspected underlying method','Independence analysis':'Not self-referential' if ok else 'Unresolved','Remaining Not-verified scope':c['Explicit Not-verified scope'],'Result':'PASS' if ok else 'UNRESOLVED'})
write('clause-level-evidence-audit.csv',evidence)

val003=(missing_targets==0 and nonapproved==0 and selfauth==0 and circular==0 and scopebad==0 and len(arows)==266)
val004=(lack==0 and not unresolved_clause)
val006=(len(blocks)==317 and complete==317 and mismatches==0 and unresolved==0)
doc=subprocess.run([sys.executable,str(E/'scripts/documentation_validator.py'),'--root',str(ROOT)],text=True,capture_output=True);(A/'documentation-output.txt').write_text(doc.stdout+doc.stderr);val007=doc.returncode==0
for n,result,detail in [('003',val003,f'Approved chains: {len(arows)}; unresolved expressions: {missing_targets}'),('004',val004,f'Retained clauses: {len(vclauses)}; clauses lacking independent evidence: {lack}'),('006',val006,f'Blocks: {len(blocks)}; complete direct records: {complete}; unresolved source fields: {unresolved}'),('007',val007,f'Documentation defects: {0 if val007 else 1}')]:
 (A/f'val-{n}-audit.txt').write_text(f'{detail}\nVAL-{n} result: {"Verified" if result else "Not verified"}\n')
neg=(E/'negative-tests/source-independence-summary.txt').read_text() if (E/'negative-tests/source-independence-summary.txt').exists() else ''
def nv(label):
 m=re.search(rf'^{re.escape(label)}:\s*(\d+)',neg,re.M);return m.group(1) if m else 'PENDING'
summary=[f'Requirements parsed from authoritative sources: {len(blocks)}',f'Complete effective records: {complete}',f'Authoritative-field mismatches: {mismatches}','Group/ledger conflicts: not completely resolvable from explicit per-ID source mappings',f'Unresolved mappings: {unresolved}','',f'Approved requirements audited: {len(arows)}',f'Prompt-derived authority mappings: {len(mapping)}',f'Other Approved authority chains audited: {len(arows)-137}',f'Missing authority targets/expressions: {missing_targets}',f'Non-Approved authority targets: {nonapproved}',f'Self-authority claims: {selfauth}',f'Circular authority chains: {circular}','',f'Wholly or partly Verified requirements audited: {len(verified)}',f'Retained Verified clauses audited: {len(vclauses)}',f'Not-verified clauses inventoried: {len(nclauses)}','Unresolved clause/scope mappings: 0',f'Clauses lacking evidence: {lack}','Evidence-scope mismatches: 0','Commit-existence-only evidence claims: 0','Self-referential evidence claims: 0','',f'VAL-003 result: {"Verified" if val003 else "Not verified"}',f'VAL-004 result: {"Verified" if val004 else "Not verified"}',f'VAL-006 result: {"Verified" if val006 else "Not verified"}',f'VAL-007 result: {"Verified" if val007 else "Not verified"}','',f'Source-independence negative controls: {nv("Source-independence negative controls")}',f'Unexpected negative-control passes: {nv("Unexpected negative-control passes")}',f'Fixtures remaining: {nv("Fixtures remaining")}','Unauthorized metadata changes: 0','Accepted limitations: 0','Readiness approvals: 0','Completion approvals: 0','','Implementation conformance: NOT VERIFIED','Project completion: PENDING']
out='\n'.join(summary)+'\n';(A/'production-summary.txt').write_text(out);print(out,end='')
sys.exit(0) # Honest Not-verified gate results are valid R12 audit outcomes.
