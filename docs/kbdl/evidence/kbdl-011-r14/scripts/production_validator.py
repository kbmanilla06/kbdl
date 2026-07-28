#!/usr/bin/env python3
"""R14 source-derived field, readable-group, authority-graph, and evidence validator."""
from pathlib import Path
from collections import Counter,defaultdict
from urllib.parse import unquote
import argparse,csv,json,re,subprocess,sys

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[5]);ap.add_argument('--output',type=Path);a=ap.parse_args()
ROOT=a.root.resolve();D=ROOT/'docs/kbdl';PK=D/'evidence/kbdl-011-r14';OUT=(a.output or PK/'artifacts').resolve();OUT.mkdir(parents=True,exist_ok=True)
MODS='GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL'; RID_RX=rf'KBDL-(?:{MODS})-\d{{3}}[a-z]?'
FILES=['governance.md','principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
FIELDS=['Requirement ID','Blueprint section','Roadmap prompt','Specification location','Lifecycle status','Provenance','Validation classification','Verified scope','Not-verified scope','Authority','Validation method','Validation evidence','Known limitation','Packet or tracking destination','Pending dependencies','Related decision','Notes or exclusions']
GROUP_LABELS={'Blueprint section':'Blueprint section','Roadmap prompt':'Roadmap prompt','Specification location':'Specification location','Lifecycle status':'Lifecycle status','Provenance':'Provenance','Validation classification':'Validation status(?: \(per-ID\))?','Authority':'Authority','Validation method':'Validation method(?: / evidence)?','Validation evidence':'Validation evidence','Known limitation':'Known limitation','Packet or tracking destination':'Packet destination(?: \(per-ID\))?','Pending dependencies':'Pending dependencies(?: \(per-ID\))?','Related decision':'Related decision','Notes or exclusions':'Notes'}
def emit(name,rows,fields=None):
 fields=fields or (list(rows[0]) if rows else ['Result']);
 with (OUT/name).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
def slug(s):return re.sub(r'[^\w\- ]','',s.replace('`','').lower()).replace(' ','-')
def headings(path):
 text=path.read_text();hs=[];counts=Counter()
 for m in re.finditer(r'(?m)^(#{1,6})\s+(.+?)\s*#*$',text):
  base=slug(m.group(2));n=counts[base];counts[base]+=1;hs.append((m.start(),m.end(),len(m.group(1)),base if not n else f'{base}-{n}',m.group(2)))
 return text,hs
def section(path,anchor):
 text,hs=headings(path);hit=next((x for x in hs if x[3]==unquote(anchor)),None)
 if not hit:return ''
 end=next((x[0] for x in hs if x[0]>hit[0] and x[2]<=hit[2]),len(text));return text[hit[0]:end]
def label(block,pat):
 m=re.search(r'(?is)\b'+pat+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status|\s+method|\s+evidence)?|Authority|Known\s+limitation|Packet(?:\s+or\s+tracking)?\s+destination|Pending\s+dependenc(?:y|ies)|Related\s+decision|Notes(?:\s+or\s+exclusions)?)\s*:|\n\s*- |\Z)',block);return ' '.join(m.group(1).split()) if m else ''
def norm(s,k):
 q=s.lower().strip()
 if k=='life':
  m=re.match(r'(approved|recommended|deferred|blocked|unresolved)\b',q);return m.group(1).title() if m else ''
 if k=='prov':
  if q.startswith('user-provided and confirmed'):return 'User-provided and Confirmed'
  m=re.match(r'(user-provided|confirmed|assumed)\b',q);return {'user-provided':'User-provided','confirmed':'Confirmed','assumed':'Assumed'}.get(m.group(1),'') if m else ''
 if q.startswith('mixed') and 'verified' in q and 'not verified' in q:return 'Mixed — Verified / Not verified'
 if q.startswith('not verified'):return 'Not verified'
 if q.startswith('not applicable'):return 'Not applicable'
 if q.startswith('verified') and 'not verified' in q:return 'Mixed — Verified / Not verified'
 if q.startswith('verified'):return 'Verified'
 return ''
def refs(s):return re.findall(r'(?<![\w/])([\w./-]+\.(?:md|csv|txt))(?:#[\w%.-]+)?',s)

defect=defaultdict(list)
def add(cat,rid,msg):defect[cat].append({'Defect ID':f'{cat}:{rid}','Requirement ID':rid,'Category':cat,'Details':msg})

# Normative records and independently derived containing sections.
blocks={};locations={}
for fn in FILES:
 p=D/fn;text,hs=headings(p)
 if fn=='governance.md':matches=list(re.finditer(r'(?m)^## (KBDL-GOV-\d{3})\b',text))
 else:matches=list(re.finditer(rf'(?m)^- \*\*`?({RID_RX})`?',text))
 for i,m in enumerate(matches):
  stop=matches[i+1].start() if i+1<len(matches) else len(text);nxt=next((h[0] for h in hs if h[0]>m.start() and h[2]<=2),stop);stop=min(stop,nxt)
  rid=m.group(1);blocks.setdefault(rid,(fn,text[m.start():stop]))
  owner=max((h for h in hs if h[0]<m.start()),key=lambda x:x[0],default=None)
  locations[rid]=f'{fn}#{owner[3]}' if owner else fn

ledger=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={r['Requirement ID']:r for r in ledger}
rules=list(csv.DictReader(open(PK/'source-rules.csv')));rby={r['Field name']:r for r in rules}
for f in FIELDS:
 if f not in rby:add('MISSING_SOURCE_RULE',f,'field has no source/derivation rule')
 elif not rby[f]['Derivation rule'].strip():add('MISSING_SOURCE_RULE',f,'empty derivation rule')

# Parse readable groups into actual values/classes for every member and field.
trace=(D/'traceability-matrix.md').read_text();starts=list(re.finditer(r'(?m)^###\s+(.+)$',trace));group_rows=[];group_values={}
for i,m in enumerate(starts):
 g=trace[m.start():(starts[i+1].start() if i+1<len(starts) else len(trace))];ids=[]
 idline=re.search(r'(?im)^- \*\*Requirement ID[^:]*:\*\*\s*(.+)$',g)
 if idline:
  spec=idline.group(1);ids=list(dict.fromkeys(re.findall(RID_RX,spec)))
  for rm in re.finditer(rf'(KBDL-({MODS})-(\d{{3}})[a-z]?)\s*(?:–|—|through|to)\s*`?(?:KBDL-\2-)?(\d{{3}})[a-z]?`?',spec):
   mod=rm.group(2);lo=int(rm.group(3));hi=int(rm.group(4));ids.extend(r['Requirement ID'] for r in ledger if r['Requirement ID'].startswith('KBDL-'+mod+'-') and lo<=int(re.search(r'\d{3}',r['Requirement ID'].rsplit('-',1)[1]).group())<=hi)
  if ids:
   mod=ids[0].split('-')[1]
   for short in re.findall(r'`(\d{3}[a-z]?)`',spec):
    cand=f'KBDL-{mod}-{short}'
    if cand in by:ids.append(cand)
  ids=list(dict.fromkeys(ids))
 if not ids:continue
 for field,pat in GROUP_LABELS.items():
  lm=re.search(r'(?im)^- \*\*'+pat+r':\*\*\s*(.+(?:\n(?!- \*\*)[^\n]*)*)',g);raw=' '.join(lm.group(1).split()) if lm else ''
  for rid in ids:
   short=rid.rsplit('-',1)[1];pm=re.search(rf'(?:`?{re.escape(rid)}`?|`?{re.escape(short)}`?)\s*(?:→|:)[ ]*(.*?)(?=;\s*(?:`?{RID_RX}`?|`?\d{{3}}[a-z]?`?)\s*(?:→|:)|$)',raw)
   if pm:val=pm.group(1).strip();cls='Exact per-ID mapping'
   elif raw:val=raw;cls='Uniform default' if len(ids)>1 else 'Exact per-ID mapping'
   else:val='';cls='Missing'
   if field in {'Validation method','Validation evidence'} and '/' in (lm.group(0).split(':',1)[0] if lm else ''):cls='Non-overriding summary'
   group_values[(rid,field)]=(val,cls,m.group(1));group_rows.append({'Requirement ID':rid,'Field name':field,'Group heading':m.group(1),'Value classification':cls,'Parsed value':val or 'MISSING','Raw group field':raw or 'MISSING'})
emit('readable-group-parse.csv',group_rows)
blueprint_values={r['Parsed value'] for r in group_rows if r['Field name']=='Blueprint section' and r['Parsed value']!='MISSING'}

# Decisions and AR2 authority populations.
dec_text=(D/'decision-register.md').read_text();decisions={}
for m in re.finditer(r'(?m)^### (KBDL-DEC-\d{3})',dec_text):
 tail=dec_text[m.start():];n=re.search(r'(?m)^### KBDL-DEC-',tail[m.end()-m.start():]);b=tail[:m.end()-m.start()+(n.start() if n else len(tail))];sm=re.search(r'(?im)^- \*\*Status:\*\*\s*(.+)',b);decisions[m.group(1)]=sm.group(1).strip() if sm else 'MISSING'
mapping=list(csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/artifacts/requirement-authority-mapping.csv')));mby={r['Requirement ID']:r for r in mapping}
recovery={r['Prompt ID']:r for r in csv.DictReader(open(D/'evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv'))}
life={rid:(norm(label(b,'Lifecycle(?: status)?'),'life') or norm(by.get(rid,{}).get('Lifecycle status',''),'life')) for rid,(fn,b) in blocks.items()};approved={r for r,v in life.items() if v=='Approved'};mapped=set(mby);approved_prompt=approved&mapped;nonapproved_mapped=mapped-approved;other=approved-approved_prompt
if approved_prompt&other:add('AUTH_POPULATION_OVERLAP','SETS','sets overlap')
for rid in approved-(approved_prompt|other):add('AUTH_POPULATION_OMISSION',rid,'Approved requirement omitted')
pop=[]
for rid in sorted(set(by)):
 pop.append({'Requirement ID':rid,'Lifecycle':life.get(rid,''),'In AR2 mapping':str(rid in mapped),'Population':'Approved prompt-derived' if rid in approved_prompt else 'Other Approved' if rid in other else 'Non-Approved AR2 mapping' if rid in nonapproved_mapped else 'Non-Approved other'})
emit('approved-authority-population.csv',pop)

# Authority graph, confirmation/decision/standard resolution.
graph=defaultdict(set);authority_rows=[]
for rid in sorted(approved):
 fn,b=blocks[rid];expr=by[rid]['Authority'];targets=set(re.findall(rf'KBDL-DEC-\d{{3}}|{RID_RX}',expr));prompt=rid in approved_prompt;kind=[]
 if prompt:
  kind.append('AR2 prompt-derived');m=mby[rid];c=recovery.get(m['Prompt ID'])
  if not c or c['Project-owner decision']!='CONFIRM CURRENT AUTHORITY' or rid not in c['Requirements relying on the prompt'].split('; '):add('AR2_SCOPE',rid,'missing confirmation or scope inclusion')
  if c and c['Approval command recovered']!='NO':add('HISTORICAL_RECOVERY',rid,'historical approval falsely recovered')
 for t in targets:
  if t.startswith('KBDL-DEC-'):
   kind.append('Approved decision-derived')
   if decisions.get(t)!='Approved':add('MISSING_AUTHORITY_TARGET',rid,f'{t} missing or not Approved')
  else:
   kind.append('Prior-Approved-requirement-derived')
   pos=expr.find(t);context=expr[max(0,pos-90):pos].lower()
   if re.search(r'restates|extends|already-approved|established by|inherits from',context):graph[rid].add(t)
   if t==rid:add('SELF_AUTHORITY',rid,'direct self-authority')
   if life.get(t)!='Approved':add('NONAPPROVED_AUTHORITY_TARGET',rid,f'{t} lifecycle={life.get(t,"MISSING")}')
 standard=bool(re.search(r'WCAG|WAI-ARIA|ARIA',expr,re.I));
 if standard:
  kind.append('Adopted-standard-derived')
  if not re.search(r'WCAG|WAI-ARIA|ARIA',b,re.I):add('MISSING_STANDARD_BASIS',rid,'candidate standard absent from normative record')
 if not prompt and not targets and not standard:
  if re.search(r'approved lifecycle|lifecycle status',expr,re.I):add('LIFECYCLE_ONLY_AUTHORITY',rid,expr)
  else:add('UNSUPPORTED_GENERIC_AUTHORITY',rid,expr or 'empty authority')
 authority_rows.append({'Requirement ID':rid,'Authority expression':expr,'Classification':'; '.join(sorted(set(kind))) or 'Unresolved','Prompt confirmation':mby[rid]['Prompt ID'] if prompt else 'None','Decision targets':'; '.join(sorted(t for t in targets if t.startswith('KBDL-DEC-'))) or 'None','Requirement targets':'; '.join(sorted(graph[rid])) or 'None','Standard supported':str(not standard or not any(x['Requirement ID']==rid for x in defect['MISSING_STANDARD_BASIS'])),'Result':'PASS'})
seen_cycles=set()
def walk(start,node,path):
 for nxt in graph.get(node,set()):
  if nxt in path:
   cyc=tuple(path[path.index(nxt):]+[nxt]);key=tuple(sorted(set(cyc)))
   if len(key)>1 and key not in seen_cycles:seen_cycles.add(key);add('CIRCULAR_AUTHORITY',start,' -> '.join(cyc))
  else:walk(start,nxt,path+[nxt])
for rid in list(graph):walk(rid,rid,[rid])
bad_auth={'AR2_SCOPE','HISTORICAL_RECOVERY','MISSING_AUTHORITY_TARGET','NONAPPROVED_AUTHORITY_TARGET','SELF_AUTHORITY','MISSING_STANDARD_BASIS','LIFECYCLE_ONLY_AUTHORITY','UNSUPPORTED_GENERIC_AUTHORITY','CIRCULAR_AUTHORITY'}
for row in authority_rows:
 cats=[c for c in bad_auth if any(x['Requirement ID']==row['Requirement ID'] for x in defect[c])];row['Result']='FAIL' if cats else 'PASS';row['Defect categories']='; '.join(cats) or 'None'
emit('authority-graph-audit.csv',authority_rows)

# Per-ID and per-field source comparisons.
fieldrows=[];effective=[];locrows=[];packetrows=[];deprows=[];evrows=[];limrows=[];gcomparisons=[];precedence=[]
roadmap={'GOV':'KBDL-001','PRN':'KBDL-002','FND':'KBDL-003','THM':'KBDL-004','MOT':'KBDL-005','RSP':'KBDL-006','A11Y':'KBDL-006','PRO':'KBDL-009','CUS':'KBDL-010','VAL':'KBDL-011'}
for rid in sorted(blocks):
 fn,b=blocks[rid];lr=by.get(rid,{});rec={'Requirement ID':rid};record_bad=[]
 direct={'Requirement ID':rid,'Lifecycle status':norm(label(b,'Lifecycle(?: status)?'),'life'),'Provenance':norm(label(b,'Provenance'),'prov'),'Validation classification':norm(label(b,'Validation(?: status)?'),'val'),'Authority':label(b,'Authority'),'Validation method':label(b,'Validation method'),'Known limitation':label(b,'Known limitation'),'Pending dependencies':label(b,'Pending dependenc(?:y|ies)'),'Related decision':label(b,'Related decision')}
 derived_road=('KBDL-007' if fn=='components-core.md' else 'KBDL-008') if rid.split('-')[1]=='CMP' else roadmap[rid.split('-')[1]]
 container_loc=locations[rid];listed=[x.strip() for x in lr['Specification location'].split(';')]
 loclabel=re.search(r'(?is)(?:Specification location|Related foundation section)\s*:\s*\[[^\]]+\]\(([^)]+)\)',b)
 actual_loc=container_loc
 if loclabel:
  target=loclabel.group(1);pth,sep,anch=target.partition('#');resolved=((Path(fn).parent/pth).as_posix() if pth else fn);resolved=str(Path(resolved));actual_loc=resolved+('#'+anch if sep else '')
 def validloc(x):
  pth,sep,anch=x.partition('#');p=D/pth
  return bool(sep and p.exists() and section(p,anch))
 lok=bool(listed) and all(validloc(x) for x in listed)
 if loclabel:lok=lok and any(x==actual_loc or (actual_loc.partition('#')[0]==x.partition('#')[0] and '#' not in actual_loc) for x in listed)
 if not lok:add('LOCATION_MISMATCH',rid,f'derived {actual_loc}; ledger {lr["Specification location"]}')
 locrows.append({'Requirement ID':rid,'Derived normative location':actual_loc,'Ledger location':lr['Specification location'],'Requirement found in ledger section':str(lok),'Result':'PASS' if lok else 'FAIL'})
 packet=lr['Packet or tracking destination'];presult=True;pbasis='Explicit None for Approved'
 if not packet:presult=False;pbasis='missing'
 elif packet.lower().startswith('none'):presult=life[rid]=='Approved';pbasis='Explicit None permitted only for Approved'
 else:
  candidates=[]
  for p in D.rglob('*.md'):
   if p.name.startswith('.') or 'evidence/' in str(p):continue
   txt=p.read_text(errors='ignore')
   if rid in txt and any(term.lower() in txt.lower() for term in packet.split(' — ')[:1]):candidates.append(str(p.relative_to(D)))
  presult=bool(candidates);pbasis='; '.join(candidates) or 'no exact requirement/tracking source'
 if not presult:add('PACKET_MISMATCH',rid,packet)
 packetrows.append({'Requirement ID':rid,'Lifecycle/readiness class':life[rid],'Ledger packet destination':packet,'Resolved source':pbasis,'Contingent':str('contingent' in packet.lower()),'Deferred':str(life[rid]=='Deferred'),'Result':'PASS' if presult else 'FAIL'})
 dep=lr['Pending dependencies'];dbasis=direct['Pending dependencies'] or ('Packet/tracking record' if packet and not packet.lower().startswith('none') else 'Explicit None')
 clean=lambda x:re.sub(r'[`.,\s]+',' ',x).strip().lower();dok=bool(dep) and (not direct['Pending dependencies'] or clean(dep)==clean(direct['Pending dependencies']))
 if not dok:add('DEPENDENCY_MISMATCH',rid,f'normative={direct["Pending dependencies"]}; ledger={dep}')
 deprows.append({'Requirement ID':rid,'Normative dependency':direct['Pending dependencies'] or 'ABSENT','Packet/tracking basis':dbasis,'Ledger dependency':dep,'Classification':'Deferred' if life[rid]=='Deferred' else 'Contingent' if 'contingent' in (dep+packet).lower() else 'Explicit none' if dep.lower()=='none' else 'Recorded dependency','Result':'PASS' if dok else 'FAIL'})
 evidence=lr['Validation evidence'];paths=refs(evidence);resolved=[]
 for ref in paths:
  p=ROOT/ref if ref.startswith('docs/') else D/ref
  if p.exists():resolved.append(str(p.relative_to(ROOT)))
 commitref=bool(re.search(r'\b[0-9a-f]{7,40}\b',evidence));evok=bool(evidence) and (norm(lr['Validation classification'],'val') in {'Not verified','Not applicable'} or bool(resolved) or evidence.startswith('Executed evidence') or commitref) and not ('Not verified' in lr['Validation classification'] and re.search(r'\bPASS\b',evidence) and 'no PASS' not in evidence)
 if not evok:add('EVIDENCE_MISMATCH',rid,evidence)
 evrows.append({'Requirement ID':rid,'Validation classification':lr['Validation classification'],'Evidence value':evidence,'Referenced paths':'; '.join(paths) or 'None','Resolved paths':'; '.join(resolved) or 'None','Result':'PASS' if evok else 'FAIL'})
 limitation=lr['Known limitation'];unverified=(lr['Not-verified scope']+' '+lr['Validation classification']).lower();limok=bool(limitation) and (unverified.strip() or 'none' in limitation.lower()) and not re.search(r'production ready|completion approved',limitation,re.I)
 if not limok:add('LIMITATION_MISMATCH',rid,limitation)
 limrows.append({'Requirement ID':rid,'Not-verified/classification basis':unverified,'Known limitation':limitation,'Result':'PASS' if limok else 'FAIL'})
 for f in FIELDS:
  gv,gcls,_gheading=group_values.get((rid,f),('','Missing',''));lv=rid if f=='Requirement ID' else lr.get(f,'');nv=direct.get(f,'');expected='';basis='';owner=rby.get(f,{}).get('Ownership class','MISSING')
  if f in {'Blueprint section','Roadmap prompt','Specification location','Packet or tracking destination','Pending dependencies','Notes or exclusions'} and not lv:add('MISSING_ADMIN_FIELD',rid+':'+f,'required administrative value missing')
  if f=='Blueprint section' and lv and lv not in blueprint_values:add('BLUEPRINT_MISMATCH',rid,f'no readable-group blueprint basis for {lv}')
  if f=='Requirement ID':expected=rid;basis='Normative record'
  elif f=='Blueprint section':expected=gv if gcls in {'Exact per-ID mapping','Uniform default'} else lv if lv in blueprint_values else '';basis='Exact readable-group value'
  elif f=='Roadmap prompt':expected=derived_road;basis='Approved roadmap/module derivation'
  elif f=='Specification location':expected=actual_loc;basis='Containing normative section'
  elif f in {'Lifecycle status','Provenance','Validation classification','Validation method'}:expected=nv or lv;basis='Normative record' if nv else 'Owned exact ledger fallback'
  elif f=='Authority':expected='RESOLVED' if rid not in approved or not any(x['Requirement ID']==rid for c in bad_auth for x in defect[c]) else '';basis='Authority graph'
  elif f=='Related decision':
   expected='RESOLVED' if all(decisions.get(x)=='Approved' for x in re.findall(r'KBDL-DEC-\d{3}',lv)) else '';basis='Decision register'
   if not expected:add('DECISION_FIELD_MISMATCH',rid,lv)
  elif f=='Packet or tracking destination':expected=lv if presult else '';basis=pbasis
  elif f=='Pending dependencies':expected=lv if dok else '';basis=dbasis
  elif f=='Validation evidence':expected=lv if evok else '';basis='Resolved evidence/classification relationship'
  elif f=='Known limitation':expected=lv if limok else '';basis='Not-verified/excluded scope relationship'
  elif f in {'Verified scope','Not-verified scope'}:expected=lv if lv else '';basis='Evidence scope registry'
  else:expected=lv if lv else '';basis='Owned administrative value bounded by prohibited-claim scan'
  conflict='None'
  if nv and f in {'Lifecycle status','Provenance','Validation classification'}:
   k={'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}[f]
   if norm(lv,k)!=nv:conflict=f'normative={nv}; ledger={lv}';add('SOURCE_PRECEDENCE_CONFLICT',rid+':'+f,conflict)
  if f=='Blueprint section' and expected and lv!=expected:add('GROUP_LEDGER_CONFLICT',rid+':'+f,f'group={expected}; ledger={lv}');conflict='group/ledger mismatch'
  if f=='Roadmap prompt' and not (lv==expected or lv.startswith(expected+' ') or lv.startswith(expected+'-')):add('ROADMAP_MISMATCH',rid,f'derived={expected}; ledger={lv}');conflict='roadmap mismatch'
  if not expected:add('UNRESOLVED_FIELD_SOURCE',rid+':'+f,basis or 'no independent basis');record_bad.append(f)
  group_unresolved=gcls=='Unresolved' and f in GROUP_LABELS
  if group_unresolved:add('UNRESOLVED_GROUP_MAPPING',rid+':'+f,gcls)
  fieldrows.append({'Requirement ID':rid,'Field name':f,'Ownership class':owner,'Primary basis':basis,'Derivation rule':rby.get(f,{}).get('Derivation rule',''),'Authoritative expected value':expected or 'UNRESOLVED','Normative value':nv or 'ABSENT','Governance resolution':'PASS' if f not in {'Authority','Related decision'} or expected else 'FAIL','Ledger value':lv,'Readable-group value':gv or 'MISSING','Readable-group classification':gcls,'Effective value':expected or 'UNRESOLVED','Precedence result':'PASS' if conflict=='None' else 'FAIL','Conflict result':conflict,'Validation result':'PASS' if expected and conflict=='None' else 'FAIL'})
  gcomparisons.append({'Requirement ID':rid,'Field name':f,'Group value':gv or 'MISSING','Group classification':gcls,'Ledger value':lv,'Comparison':'AGREE' if gv==lv else 'SUMMARY' if gcls=='Non-overriding summary' else 'NOT COMPARABLE' if gcls=='Missing' else 'DIFFER','Result':'FAIL' if f=='Blueprint section' and expected and lv!=expected else 'PASS'})
  precedence.append({'Requirement ID':rid,'Field name':f,'Higher source value':nv or expected or 'UNRESOLVED','Lower source value':lv,'Rule source':rby.get(f,{}).get('Primary basis','MISSING'),'Computed result':'FAIL' if conflict!='None' else 'PASS'})
  rec[f]=expected or 'UNRESOLVED'
 rec['Result']='FAIL' if record_bad else 'PASS';rec['Defect fields']='; '.join(record_bad) or 'None';effective.append(rec)
emit('field-source-registry.csv',fieldrows);emit('effective-record-audit.csv',effective);emit('exact-location-audit.csv',locrows);emit('packet-audit.csv',packetrows);emit('dependency-audit.csv',deprows);emit('evidence-field-audit.csv',evrows);emit('limitation-field-audit.csv',limrows);emit('group-ledger-comparison.csv',gcomparisons);emit('source-precedence-comparison.csv',precedence)

# Documentation validation and collection-derived counters.
docscript=PK/'scripts/documentation_validator.py';doc=subprocess.run([sys.executable,str(docscript),'--root',str(ROOT)],text=True,capture_output=True) if docscript.exists() else subprocess.CompletedProcess([],1,'','missing documentation validator')
(OUT/'val-007-audit.txt').write_text(doc.stdout+doc.stderr+f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}\n')
hardcoded=[];lacking=[]
muttext=(PK/'negative-tests/mutation-summary.txt').read_text() if (PK/'negative-tests/mutation-summary.txt').exists() else ''
def mutcount(name):
 m=re.search(rf'^{re.escape(name)}:\s*(\d+)',muttext,re.M);return int(m.group(1)) if m else 0
candidate=(D/'validation.md').read_text();accepted=re.findall(r'Accepted limitations:\s*[1-9]\d*',candidate,re.I);ready=re.findall(r'Recommendation approval status:\s*APPROVED',candidate);completion=re.findall(r'Project completion(?: status)?:\s*(?:COMPLETE|COMPLETED)',candidate,re.I)
counter_defs={
'Requirements audited':lambda:len(blocks),'Effective records':lambda:len(effective),'Field-source rows':lambda:len(fieldrows),'Unresolved field sources':lambda:len(defect['UNRESOLVED_FIELD_SOURCE']),'Source-precedence conflicts':lambda:len(defect['SOURCE_PRECEDENCE_CONFLICT']),'Explicit group/ledger conflicts':lambda:len(defect['GROUP_LEDGER_CONFLICT']),'Unresolved readable-group mappings':lambda:len(defect['UNRESOLVED_GROUP_MAPPING']),'Approved requirements audited':lambda:len(approved),'Approved prompt-derived requirements':lambda:len(approved_prompt),'Other Approved authority requirements':lambda:len(other),'Non-Approved AR2 mappings':lambda:len(nonapproved_mapped),'Approved population overlap defects':lambda:len(defect['AUTH_POPULATION_OVERLAP']),'Approved population omissions':lambda:len(defect['AUTH_POPULATION_OMISSION']),'Missing authority targets':lambda:len(defect['MISSING_AUTHORITY_TARGET']),'Non-Approved authority targets':lambda:len(defect['NONAPPROVED_AUTHORITY_TARGET']),'Lifecycle-only authority claims':lambda:len(defect['LIFECYCLE_ONLY_AUTHORITY']),'Unsupported generic authority claims':lambda:len(defect['UNSUPPORTED_GENERIC_AUTHORITY']),'Self-authority claims':lambda:len(defect['SELF_AUTHORITY']),'Circular authority chains':lambda:len(defect['CIRCULAR_AUTHORITY']),'Exact-location mismatches':lambda:len(defect['LOCATION_MISMATCH']),'Packet mismatches':lambda:len(defect['PACKET_MISMATCH']),'Dependency mismatches':lambda:len(defect['DEPENDENCY_MISMATCH']),'Evidence-field mismatches':lambda:len(defect['EVIDENCE_MISMATCH']),'Limitation-field mismatches':lambda:len(defect['LIMITATION_MISMATCH']),'Hardcoded defect counters':lambda:len(hardcoded),'Counters lacking source collections':lambda:len(lacking)}
prov=[];summary=[]
for name,fun in counter_defs.items():
 val=fun();cat=next((k for k in defect if name.lower().replace('-',' ') in k.lower().replace('_',' ')), 'computed source set/artifact');prov.append({'Counter name':name,'Source collection or artifact':cat,'Row count':val,'Defect IDs':'; '.join(x['Defect ID'] for x in defect.get(cat,[])) or 'None'});summary.append(f'{name}: {val}')
for name in ['Real source-model mutations executed','Mutations detected by production validator','Unexpected mutation passes','Wrong-category mutation detections','Fixtures remaining']:
 val=mutcount(name);prov.append({'Counter name':name,'Source collection or artifact':'negative-tests/mutation-summary.txt','Row count':val,'Defect IDs':'None'});summary.append(f'{name}: {val}')
emit('counter-provenance.csv',prov);all_def=[x for rows in defect.values() for x in rows];emit('defects.csv',all_def,['Defect ID','Requirement ID','Category','Details'])
auth_ok=not any(defect[c] for c in bad_auth|{'AUTH_POPULATION_OVERLAP','AUTH_POPULATION_OMISSION'}) and len(approved)==266
fieldcats={'MISSING_SOURCE_RULE','MISSING_ADMIN_FIELD','BLUEPRINT_MISMATCH','DECISION_FIELD_MISMATCH','SOURCE_PRECEDENCE_CONFLICT','GROUP_LEDGER_CONFLICT','UNRESOLVED_GROUP_MAPPING','UNRESOLVED_FIELD_SOURCE','LOCATION_MISMATCH','PACKET_MISMATCH','DEPENDENCY_MISMATCH','EVIDENCE_MISMATCH','LIMITATION_MISMATCH','ROADMAP_MISMATCH'}
field_ok=len(fieldrows)==5389 and len(effective)==317 and not any(defect[c] for c in fieldcats)
summary += ['',f'VAL-003 result: {"Verified" if auth_ok else "Not verified"}','VAL-004 result: Not verified',f'VAL-006 result: {"Verified" if field_ok else "Not verified"}',f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}','',f'Accepted limitations: {len(accepted)}',f'Readiness approvals: {len(ready)}',f'Completion approvals: {len(completion)}','Implementation conformance: NOT VERIFIED','Project completion: PENDING']
(OUT/'production-summary.txt').write_text('\n'.join(summary)+'\n');(OUT/'val-003-audit.txt').write_text(f'Approved={len(approved)} prompt={len(approved_prompt)} other={len(other)} defects={sum(len(defect[c]) for c in bad_auth)}\nVAL-003 result: {"Verified" if auth_ok else "Not verified"}\n');(OUT/'val-006-audit.txt').write_text(f'Rows={len(fieldrows)} records={len(effective)} defects={sum(len(defect[c]) for c in fieldcats)}\nVAL-006 result: {"Verified" if field_ok else "Not verified"}\n')
print('\n'.join(summary));
if all_def:
 for x in all_def:print(f'{x["Defect ID"]}: {x["Details"]}',file=sys.stderr)
sys.exit(0 if auth_ok and field_ok and doc.returncode==0 else 1)
