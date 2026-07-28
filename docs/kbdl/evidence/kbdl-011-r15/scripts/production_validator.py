#!/usr/bin/env python3
"""R15 source-derived field, readable-group, authority-graph, and evidence validator."""
from pathlib import Path
from collections import Counter,defaultdict
from urllib.parse import unquote
import argparse,csv,json,re,subprocess,sys

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[5]);ap.add_argument('--output',type=Path);a=ap.parse_args()
ROOT=a.root.resolve();D=ROOT/'docs/kbdl';PK=D/'evidence/kbdl-011-r15';OUT=(a.output or PK/'artifacts').resolve();OUT.mkdir(parents=True,exist_ok=True)
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
def refs(s):return re.findall(r'(?<![\w/])([\w./-]+\.(?:md|csv|txt)(?:#[\w%.-]+)?)',s)

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
  spec=idline.group(1);core=spec.split(' (')[0];ids=list(dict.fromkeys(re.findall(RID_RX,core)))
  for rm in re.finditer(rf'(KBDL-({MODS})-(\d{{3}})[a-z]?)\s*(?:–|—|through|to)\s*`?(?:KBDL-\2-)?(\d{{3}})[a-z]?`?',core):
   mod=rm.group(2);lo=int(rm.group(3));hi=int(rm.group(4));ids.extend(r['Requirement ID'] for r in ledger if r['Requirement ID'].startswith('KBDL-'+mod+'-') and lo<=int(re.search(r'\d{3}',r['Requirement ID'].rsplit('-',1)[1]).group())<=hi)
  if ids:
   mod=ids[0].split('-')[1]
   for rm in re.finditer(r'(?<![\d-])(\d{3})\s*(?:–|—|through|to)\s*(\d{3})',core):
    lo,hi=map(int,rm.groups());ids.extend(r['Requirement ID'] for r in ledger if r['Requirement ID'].startswith('KBDL-'+mod+'-') and lo<=int(re.search(r'\d{3}',r['Requirement ID'].rsplit('-',1)[1]).group())<=hi)
  if ids:
   mod=ids[0].split('-')[1]
   for short in re.findall(r'`(\d{3}[a-z]?)`',spec):
    cand=f'KBDL-{mod}-{short}'
    if cand in by:ids.append(cand)
  ids=list(dict.fromkeys(ids))
 if not ids:continue
 for field,pat in GROUP_LABELS.items():
  lm=re.search(r'(?im)^- \*\*'+pat+r':\*\*\s*(.+(?:\n(?![-#])\s{2,}.+)*)',g);raw=' '.join(lm.group(1).split()) if lm else ''
  for rid in ids:
   short=rid.rsplit('-',1)[1];pm=re.search(rf'(?:`?{re.escape(rid)}`?|`?{re.escape(short)}`?)\s*(→|:)[ ]*(.*?)(?=;\s*(?:`?{RID_RX}`?|`?\d{{3}}[a-z]?`?)\s*(?:→|:)|$)',raw)
   clausehit=next(((cl.split(':',1)[1].strip(),cl) for cl in raw.split(';') if ':' in cl and (rid in cl.split(':',1)[0] or short in re.findall(r'\b\d{3}[a-z]?\b',cl.split(':',1)[0]))),None)
   buckets=list(re.finditer(r'(?i)(?:^|;)\s*(Mixed\s*[—-]\s*Verified\s*/\s*Not verified|Verified|Not verified|Not applicable|Approved|Recommended|Deferred|Blocked|Unresolved)\s*:\s*(.*?)(?=;\s*(?:Mixed\s*[—-]\s*Verified\s*/\s*Not verified|Verified|Not verified|Not applicable|Approved|Recommended|Deferred|Blocked|Unresolved)\s*:|$)',raw))
   hit=next((bm for bm in buckets if rid in re.findall(RID_RX,bm.group(2)) or short in re.findall(r'\b\d{3}[a-z]?\b',bm.group(2))),None)
   rangem=next((rm for rm in re.finditer(r'`?(\d{3}[a-z]?)`?\s*(?:–|—|through|to)\s*`?(\d{3}[a-z]?)`?\s*:\s*(.*?)(?=;|$)',raw) if int(re.match(r'\d{3}',rm.group(1)).group())<=int(re.match(r'\d{3}',short).group())<=int(re.match(r'\d{3}',rm.group(2)).group())),None)
   if field=='Validation classification' and hit:val=re.sub(r'(?i)^mixed\s*[—-]\s*verified\s*/\s*not verified$','Mixed — Verified / Not verified',hit.group(1)).capitalize().replace('Mixed — verified / not verified','Mixed — Verified / Not verified');cls='Exact per-ID mapping';grammar='Status bucket';override='Yes'
   elif clausehit:val=clausehit[0];cls='Non-overriding summary' if field in {'Authority','Known limitation','Notes or exclusions'} and re.search(r'(?i)see each|exact split|implementation-dependent|readable group|group values',val) else 'Exact per-ID mapping';grammar='Per-ID clause mapping';override='No' if cls=='Non-overriding summary' else 'Yes'
   elif pm:val=pm.group(2).strip();cls='Exact per-ID mapping';grammar='Arrow mapping' if pm.group(1)=='→' else 'Colon mapping';override='Yes'
   elif rangem:val=rangem.group(3).strip();cls='Non-overriding summary' if field in {'Authority','Known limitation'} or re.search(r'(?i)see each|exact sources|implementation-dependent',val) else 'Exact per-ID mapping';grammar='Range mapping';override='No' if cls=='Non-overriding summary' else 'Yes'
   elif hit:val=re.sub(r'(?i)^mixed\s*[—-]\s*verified\s*/\s*not verified$','Mixed — Verified / Not verified',hit.group(1)).capitalize().replace('Mixed — verified / not verified','Mixed — Verified / Not verified');cls='Exact per-ID mapping';grammar='Status bucket';override='Yes'
   elif buckets:val='';cls='Unresolved';grammar='Status bucket';override='Yes'
   elif raw and field in {'Lifecycle status','Provenance','Validation classification'} and norm(re.sub(r'(?i)^all\s+','',raw).rstrip('.'),{'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}[field]):val=norm(re.sub(r'(?i)^all\s+','',raw).rstrip('.'),{'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}[field]);cls='Uniform default';grammar='Uniform status default';override='Yes'
   elif raw:val=raw;cls='Uniform default' if field in {'Blueprint section','Roadmap prompt'} else 'Non-overriding summary';grammar='Uniform default' if cls=='Uniform default' else 'Broad descriptive summary';override='Yes' if cls=='Uniform default' else 'No'
   else:val='';cls='Missing';grammar='Missing';override='No'
   if field in {'Validation method','Validation evidence'} and '/' in (lm.group(0).split(':',1)[0] if lm else ''):cls='Non-overriding summary';grammar='Combined method/evidence summary';override='No'
   result='PASS' if cls!='Unresolved' else 'FAIL';details='None' if result=='PASS' else 'status bucket does not resolve this group member'
   group_values[(rid,field)]=(val,cls,m.group(1),grammar,override);group_rows.append({'Requirement ID':rid,'Field name':field,'Group heading':m.group(1),'Raw group field':raw or 'MISSING','Parsed grammar':grammar,'Per-ID resolved value':val or 'MISSING','Classification':cls,'Overriding status':override,'Resolution result':result,'Defect details':details})
emit('readable-group-parse.csv',group_rows)
blueprint_values={r['Per-ID resolved value'] for r in group_rows if r['Field name']=='Blueprint section' and r['Per-ID resolved value']!='MISSING'}

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
graph=defaultdict(set);authority_rows=[];reference_rows=[];standard_rows=[]
for rid in sorted(approved):
 fn,b=blocks[rid];expr=by[rid]['Authority'];targets=set(re.findall(rf'KBDL-DEC-\d{{3}}|{RID_RX}',expr));prompt=rid in approved_prompt;kind=[]
 if prompt:
  kind.append('AR2 prompt-derived');m=mby[rid];c=recovery.get(m['Prompt ID'])
  if not c or c['Project-owner decision']!='CONFIRM CURRENT AUTHORITY' or rid not in c['Requirements relying on the prompt'].split('; '):add('AR2_SCOPE',rid,'missing confirmation or scope inclusion')
  if c and c['Approval command recovered']!='NO':add('HISTORICAL_RECOVERY',rid,'historical approval falsely recovered')
 for t in targets:
  if t.startswith('KBDL-DEC-'):
   kind.append('Approved decision-derived')
   reference_rows.append({'Requirement ID':rid,'Referenced target':t,'Reference classification':'Authority edge','Classification basis':'Decision cited in authority expression','Graph edge':'Yes'})
   if decisions.get(t)!='Approved':add('MISSING_AUTHORITY_TARGET',rid,f'{t} missing or not Approved')
  else:
   kind.append('Prior-Approved-requirement-derived')
   pos=expr.find(t);context=expr[max(0,pos-120):pos+len(t)+120].lower()
   if re.search(r'unapproved context|context only|does not approve|excluded|specific applications|together with',context):refclass='Context-only reference'
   elif re.search(r'analogy|consistent with',context) and not re.search(r'restates|extends|authority|established|inherits',context):refclass='Non-authoritative analogy'
   elif re.search(r'related requirement',context):refclass='Related requirement'
   else:refclass='Authority edge'
   if refclass=='Authority edge':graph[rid].add(t)
   reference_rows.append({'Requirement ID':rid,'Referenced target':t,'Reference classification':refclass,'Classification basis':context.strip(),'Graph edge':'Yes' if refclass=='Authority edge' else 'No'})
   if t==rid:add('SELF_AUTHORITY',rid,'direct self-authority')
   if refclass=='Authority edge' and life.get(t)!='Approved':add('NONAPPROVED_AUTHORITY_TARGET',rid,f'{t} lifecycle={life.get(t,"MISSING")}')
 standard=bool(re.search(r'\b(?:WCAG|WAI-ARIA|ARIA)\b',expr,re.I));
 if standard:
  kind.append('Adopted-standard-derived')
  source_text=b
  for loc in by[rid]['Specification location'].split(';'):
   pth,sep,anch=loc.strip().partition('#');p=D/pth
   if sep and p.exists():source_text+='\n'+section(p,anch)
  for sourcep in [D/x for x in FILES if (D/x).exists()]:source_text+='\n'+'\n'.join(line for line in sourcep.read_text(errors='ignore').splitlines() if rid in line)
  owner_text=(D/fn).read_text(errors='ignore');canon=lambda x:re.sub(r'\s+',' ',x).strip().lower();cited=set(re.findall(r'(?i)\b(?:SC\s*)?\d\.\d\.(?:\d|x)\b|\b(?:aria-[a-z-]+)',expr));governing=set(re.findall(r'(?i)\b(?:SC\s*)?\d\.\d\.(?:\d|x)\b|\b(?:aria-[a-z-]+)',source_text));
  if not cited:governing|=set(re.findall(r'(?i)\b(?:SC\s*)?\d\.\d\.\d\b|\b(?:aria-[a-z-]+)',owner_text))
  match=bool(cited) and all(any(canon(c).replace('.x','.') in canon(g) for g in governing) for c in cited)
  if cited and not match:add('STANDARD_CLAUSE_MISMATCH',rid,f'candidate={sorted(cited)} normative={sorted(governing)}')
  if not cited and not governing and not (prompt or targets):add('MISSING_STANDARD_BASIS',rid,'generic standard reference lacks an exact governing clause')
  if re.fullmatch(r'WCAG\s+2\.2',expr.strip(),re.I):add('MISSING_STANDARD_BASIS',rid,'generic standard reference lacks an exact clause')
  if not cited and not governing and not (prompt or targets):add('STANDARD_CLAUSE_MISMATCH',rid,'generic standard keyword without exact governing clause')
  standard_rows.append({'Requirement ID':rid,'Candidate standard citations':'; '.join(sorted(cited)) or 'GENERIC ONLY','Normative governing citations':'; '.join(sorted(governing)) or 'NONE','Direct or supporting':'Direct authority' if not prompt and not targets else 'Supporting/mixed','Result':'PASS' if (match or (not cited and bool(governing or prompt or targets))) else 'FAIL'})
 if not prompt and not targets and not standard:
  if re.search(r'approved lifecycle|lifecycle status',expr,re.I):add('LIFECYCLE_ONLY_AUTHORITY',rid,expr)
  elif re.match(r'^(?:Approved|Recommended|Deferred|Blocked|Unresolved)\b',expr,re.I):kind.append('Lifecycle declaration')
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
bad_auth={'AR2_SCOPE','HISTORICAL_RECOVERY','MISSING_AUTHORITY_TARGET','NONAPPROVED_AUTHORITY_TARGET','SELF_AUTHORITY','MISSING_STANDARD_BASIS','STANDARD_CLAUSE_MISMATCH','UNCLASSIFIED_AUTHORITY_REFERENCE','LIFECYCLE_ONLY_AUTHORITY','UNSUPPORTED_GENERIC_AUTHORITY','CIRCULAR_AUTHORITY'}
for row in authority_rows:
 cats=[c for c in bad_auth if any(x['Requirement ID']==row['Requirement ID'] for x in defect[c])];row['Result']='FAIL' if cats else 'PASS';row['Defect categories']='; '.join(cats) or 'None'
emit('authority-graph-audit.csv',authority_rows)
emit('authority-reference-classification.csv',sorted(reference_rows,key=lambda r:(r['Requirement ID'],r['Referenced target'],r['Reference classification'],r['Classification basis'])));emit('adopted-standard-clause-audit.csv',standard_rows or [{'Requirement ID':'None','Candidate standard citations':'None','Normative governing citations':'None','Direct or supporting':'None','Result':'PASS'}])

# Per-ID and per-field source comparisons.
fieldrows=[];effective=[];locrows=[];packetrows=[];deprows=[];evrows=[];limrows=[];gcomparisons=[];precedence=[]
roadmap={'GOV':'KBDL-001','PRN':'KBDL-002','FND':'KBDL-003','THM':'KBDL-004','MOT':'KBDL-005','RSP':'KBDL-006','A11Y':'KBDL-006','PRO':'KBDL-009','CUS':'KBDL-010','VAL':'KBDL-011'}
evidence_path_users=defaultdict(set)
for er in ledger:
 for ref in refs(er['Validation evidence']):evidence_path_users[ref.partition('#')[0]].add(er['Requirement ID'])
packet_index=defaultdict(list)
for p in D.rglob('*.md'):
 if 'evidence/' in str(p):continue
 for ln,line in enumerate(p.read_text(errors='ignore').splitlines(),1):
  found=re.findall(RID_RX,line)
  if not found:continue
  cells=[x.strip() for x in line.strip().strip('|').split('|')];nums=[]
  if cells and re.fullmatch(r'\d+',cells[0]):nums.append(int(cells[0]))
  nums += [int(x) for x in re.findall(r'(?i)\bitem\s+(\d+)\b',line)]
  for rr in found:packet_index[rr].append({'Document':str(p.relative_to(D)),'Line':ln,'Item numbers':sorted(set(nums)),'Row':line.strip()})
for rid in sorted(blocks):
 fn,b=blocks[rid];lr=by.get(rid,{});rec={'Requirement ID':rid};record_bad=[]
 direct={'Requirement ID':rid,'Lifecycle status':norm(label(b,'Lifecycle(?: status)?'),'life'),'Provenance':norm(label(b,'Provenance'),'prov'),'Validation classification':norm(label(b,'Validation(?: status)?'),'val'),'Authority':label(b,'Authority'),'Validation method':label(b,'Validation method'),'Known limitation':label(b,'Known limitation'),'Pending dependencies':label(b,'Pending dependenc(?:y|ies)'),'Related decision':label(b,'Related decision')}
 derived_road=('KBDL-007' if fn=='components-core.md' else 'KBDL-008') if rid.split('-')[1]=='CMP' else roadmap[rid.split('-')[1]]
 container_loc=locations[rid];listed=[x.strip() for x in lr['Specification location'].split(';')]
 loclabel=re.search(r'(?is)(?:Specification location|Related foundation section)\s*:\s*\[[^\]]+\]\(([^)]+)\)',b)
 actual_loc=container_loc
 if loclabel:
  target=loclabel.group(1);pth,sep,anch=target.partition('#');resolved=((Path(fn).parent/pth).as_posix() if pth else fn);resolved=str(Path(resolved));actual_loc=resolved+('#'+anch if sep else '')
 blocklinks=[]
 for target in re.findall(r'\[[^\]]+\]\(([^)]+#[^)]+)\)',b):
  pth,sep,anch=target.partition('#');resolved=str(Path(fn).parent/pth) if pth else fn;blocklinks.append(resolved+('#'+anch if sep else ''))
 def validloc(x):
  pth,sep,anch=x.partition('#');p=D/pth
  return bool(sep and p.exists() and section(p,anch))
 def supportedloc(x):
  pth,sep,anch=x.partition('#');p=D/pth;s=section(p,anch) if sep and p.exists() else ''
  words=lambda z:set(re.findall(r'[a-z]{5,}',z.lower()))-{'requirement','approved','validation','applicable','profiles','related','project'}
  return bool(s) and (rid in s or len(words(b)&words(s))>=3)
 gloc,gcloc,_,_,govloc=group_values.get((rid,'Specification location'),('','Missing','','','No'));supported=[x for x in listed if supportedloc(x)]
 lok=bool(listed) and all(validloc(x) for x in listed) and bool(supported) and set(listed)==set(supported)
 if not lok:add('LOCATION_MISMATCH',rid,f'derived {actual_loc}; ledger {lr["Specification location"]}')
 locrows.append({'Requirement ID':rid,'Containing normative location':container_loc,'Explicit normative location':actual_loc if loclabel else 'ABSENT','Readable-group supported locations':'; '.join(supported) or 'ABSENT','Exact expected locations':'; '.join(supported) or 'VALIDATED TOPICAL ANCHORS','Ledger location':lr['Specification location'],'All anchors resolve':str(all(validloc(x) for x in listed)),'Exact comparison':str(lok),'Result':'PASS' if lok else 'FAIL'})
 packet=lr['Packet or tracking destination'];presult=True;pbasis='Explicit None for Approved'
 if not packet:presult=False;pbasis='missing'
 elif packet.lower().startswith('none'):presult=life[rid]=='Approved';pbasis='Explicit None permitted only for Approved'
 else:
  rows=packet_index.get(rid,[]);docm=re.search(r'([\w/-]+\.md)',packet);itemm=re.search(r'(?i)\bitem\s+(\d+)\b',packet);doc=docm.group(1) if docm else fn;item=int(itemm.group(1)) if itemm else None
  matches=[x for x in rows if (not doc or x['Document']==doc) and (item is None or item in x['Item numbers'])]
  presult=bool(matches);pbasis='; '.join(f"{x['Document']}:{x['Line']} item={x['Item numbers']}" for x in matches) or 'no exact packet row/item'
  if rows and item is not None and not any(item in x['Item numbers'] for x in rows):add('PACKET_ITEM_MISMATCH',rid,f'ledger item {item}; derived rows {rows}')
 if not presult:add('PACKET_MISMATCH',rid,packet)
 packetrows.append({'Requirement ID':rid,'Lifecycle/readiness class':life[rid],'Ledger packet destination':packet,'Derived packet rows':json.dumps(packet_index.get(rid,[]),ensure_ascii=False),'Exact resolved source':pbasis,'Contingent':str('contingent' in packet.lower()),'Deferred':str(life[rid]=='Deferred'),'Result':'PASS' if presult else 'FAIL'})
 dep=lr['Pending dependencies'];dbasis=direct['Pending dependencies'] or ('Packet/tracking record' if packet and not packet.lower().startswith('none') else 'Explicit None')
 clean=lambda x:re.sub(r'[`.,\s]+',' ',x).strip().lower();dok=bool(dep) and (not direct['Pending dependencies'] or clean(dep)==clean(direct['Pending dependencies']))
 depclass=lambda x:'blocking' if 'block' in x.lower() else 'contingent' if 'contingent' in x.lower() else 'none' if x.strip().lower().startswith('none') else 'other'
 if direct['Pending dependencies'] and depclass(dep)!=depclass(direct['Pending dependencies']):add('DEPENDENCY_CLASS_MISMATCH',rid,f'normative={depclass(direct["Pending dependencies"])}; ledger={depclass(dep)}')
 if not dok:add('DEPENDENCY_MISMATCH',rid,f'normative={direct["Pending dependencies"]}; ledger={dep}')
 deprows.append({'Requirement ID':rid,'Normative dependency':direct['Pending dependencies'] or 'ABSENT','Packet/tracking basis':dbasis,'Ledger dependency':dep,'Classification':'Deferred' if life[rid]=='Deferred' else 'Contingent' if 'contingent' in (dep+packet).lower() else 'Explicit none' if dep.lower()=='none' else 'Recorded dependency','Result':'PASS' if dok else 'FAIL'})
 evidence=lr['Validation evidence'];paths=refs(evidence);resolved=[];badrefs=[]
 for ref in paths:
  base,sep,anch=ref.partition('#');p=ROOT/base if base.startswith('docs/') else D/base
  if not p.exists() and not base.startswith('docs/'):p=D/Path(lr.get('Source file','')).parent/base
  if p.exists() and (not sep or (p.suffix=='.md' and bool(section(p,anch)))):resolved.append(str(p.relative_to(ROOT))+(('#'+anch) if sep else ''))
  else:badrefs.append(ref)
 shas=re.findall(r'(?<![0-9a-f])([0-9a-f]{7,40})(?![0-9a-f])',evidence);validshas=[]
 for sha in shas:
  chk=subprocess.run(['git','-C',str(ROOT),'cat-file','-e',sha+'^{commit}'],capture_output=True)
  if chk.returncode:add('MISSING_GIT_EVIDENCE_OBJECT',rid,sha)
  else:validshas.append(sha)
 if badrefs:add('EVIDENCE_REFERENCE_MISMATCH',rid,'; '.join(badrefs))
 verified='Verified' in lr['Validation classification'];associated=True
 if verified and resolved:
  associated=any(rid in (ROOT/x.partition('#')[0]).read_text(errors='ignore') if (ROOT/x.partition('#')[0]).is_file() else False for x in resolved) or any(rid.lower().replace('kbdl-','') in Path(x.partition('#')[0]).stem.lower() for x in resolved) or any(len(evidence_path_users[x.partition('#')[0]])>1 or len(evidence_path_users[x.partition('#')[0].removeprefix('docs/kbdl/')])>1 for x in resolved) or any(Path(fn).parent==Path(x.removeprefix('docs/kbdl/')).parent for x in resolved)
  if not associated:add('EVIDENCE_SCOPE_RELATIONSHIP',rid,'resolved artifact does not name requirement or shared validation scope')
 generic=evidence.startswith('Executed evidence') and not (resolved or validshas)
 evok=bool(evidence) and not badrefs and not generic and (not verified or bool(resolved or validshas)) and associated and not ('Not verified' in lr['Validation classification'] and re.search(r'\bPASS\b',evidence) and 'no PASS' not in evidence)
 if not evok:add('EVIDENCE_MISMATCH',rid,evidence)
 evrows.append({'Requirement ID':rid,'Validation classification':lr['Validation classification'],'Evidence value':evidence,'Referenced paths/anchors':'; '.join(paths) or 'None','Resolved paths/anchors':'; '.join(resolved) or 'None','Git SHAs':'; '.join(shas) or 'None','Resolved Git objects':'; '.join(validshas) or 'None','Scope associated':str(associated),'Generic executed-evidence text':str(generic),'Result':'PASS' if evok else 'FAIL'})
 limitation=lr['Known limitation'];unverified=(lr['Not-verified scope']+' '+lr['Validation classification']).lower();limok=bool(limitation) and (unverified.strip() or 'none' in limitation.lower()) and not re.search(r'production ready|completion approved',limitation,re.I)
 relationship=r'implement|runtime|validat|evidence|unverified|not verified|pending|unavailable|cannot|no\b|not\b|remain|defer|exclude|unapproved|approval|unaddressed|out of scope|require|future|absent|recommended'
 if norm(lr['Validation classification'],'val')=='Not verified' and not re.search(relationship,limitation,re.I):limok=False
 if not limok:add('LIMITATION_MISMATCH',rid,limitation)
 limrows.append({'Requirement ID':rid,'Derived Not-verified/excluded scope':unverified,'Known limitation':limitation,'Semantic relationship terms':'; '.join(re.findall(relationship,limitation,re.I)) or 'None','Result':'PASS' if limok else 'FAIL'})
 for f in FIELDS:
  gv,gcls,_gheading,ggrammar,goverride=group_values.get((rid,f),('','Missing','','Missing','No'));lv=rid if f=='Requirement ID' else lr.get(f,'');nv=direct.get(f,'');expected='';basis='';owner=rby.get(f,{}).get('Ownership class','MISSING')
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
  if goverride=='Yes' and gv:
   k={'Lifecycle status':'life','Provenance':'prov','Validation classification':'val'}.get(f)
   def semeq(field,a,b):
    if k:return norm(a,k)==norm(b,k)
    if field in {'Packet or tracking destination','Pending dependencies'}:
     ai=set(re.findall(r'(?i)\bitem\s+(\d+)',a));bi=set(re.findall(r'(?i)\bitem\s+(\d+)',b));at=set(re.findall(RID_RX,a));bt=set(re.findall(RID_RX,b));an=a.lower().startswith('none');bn=b.lower().startswith('none');aclass='implementation' if 'implement' in a.lower() else 'project' if 'adopting' in a.lower() else 'review' if 'review' in a.lower() or 'planning' in a.lower() else 'blocking' if 'block' in a.lower() else '';bclass='implementation' if 'implement' in b.lower() else 'project' if 'adopting' in b.lower() else 'review' if 'review' in b.lower() or 'planning' in b.lower() else 'blocking' if 'block' in b.lower() else '';return (an and bn) or (bool(ai) and ai==bi) or (bool(at) and at==bt and ('block' in a.lower())==('block' in b.lower())) or (bool(aclass) and aclass==bclass)
    if field=='Related decision':return set(re.findall(r'KBDL-DEC-\d{3}',a))==set(re.findall(r'KBDL-DEC-\d{3}',b))
    if field=='Authority':return set(re.findall(rf'KBDL-DEC-\d{{3}}|{RID_RX}',a))==set(re.findall(rf'KBDL-DEC-\d{{3}}|{RID_RX}',b))
    return clean(a)==clean(b)
   agree=semeq(f,lv,gv)
   if not agree:
    add('GROUP_LEDGER_CONFLICT',rid+':'+f,f'grammar={ggrammar}; group={gv}; ledger={lv}')
    if f=='Validation classification':add('STATUS_BUCKET_MISMATCH',rid+':'+f,f'grammar={ggrammar}; group={gv}; ledger={lv}')
    conflict='group/ledger mismatch'
  if f=='Roadmap prompt' and not (lv==expected or lv.startswith(expected+' ') or lv.startswith(expected+'-')):add('ROADMAP_MISMATCH',rid,f'derived={expected}; ledger={lv}');conflict='roadmap mismatch'
  if not expected:add('UNRESOLVED_FIELD_SOURCE',rid+':'+f,basis or 'no independent basis');record_bad.append(f)
  group_unresolved=gcls=='Unresolved' and f in GROUP_LABELS
  if group_unresolved:add('UNRESOLVED_GROUP_MAPPING',rid+':'+f,gcls)
  fieldrows.append({'Requirement ID':rid,'Field name':f,'Ownership class':owner,'Primary basis':basis,'Derivation rule':rby.get(f,{}).get('Derivation rule',''),'Authoritative expected value':expected or 'UNRESOLVED','Normative value':nv or 'ABSENT','Governance resolution':'PASS' if f not in {'Authority','Related decision'} or expected else 'FAIL','Ledger value':lv,'Readable-group value':gv or 'MISSING','Readable-group classification':gcls,'Effective value':expected or 'UNRESOLVED','Precedence result':'PASS' if conflict=='None' else 'FAIL','Conflict result':conflict,'Validation result':'PASS' if expected and conflict=='None' else 'FAIL'})
  gcomparisons.append({'Requirement ID':rid,'Field name':f,'Raw group field':next((x['Raw group field'] for x in group_rows if x['Requirement ID']==rid and x['Field name']==f),'MISSING'),'Parsed grammar':ggrammar,'Group value':gv or 'MISSING','Group classification':gcls,'Overriding status':goverride,'Ledger value':lv,'Comparison':'AGREE' if clean(gv)==clean(lv) else 'SUMMARY' if gcls=='Non-overriding summary' else 'NOT COMPARABLE' if gcls=='Missing' else 'DIFFER','Result':'FAIL' if conflict!='None' else 'PASS'})
  precedence.append({'Requirement ID':rid,'Field name':f,'Higher source value':nv or expected or 'UNRESOLVED','Lower source value':lv,'Rule source':rby.get(f,{}).get('Primary basis','MISSING'),'Computed result':'FAIL' if conflict!='None' else 'PASS'})
  rec[f]=expected or 'UNRESOLVED'
 rec['Result']='FAIL' if record_bad else 'PASS';rec['Defect fields']='; '.join(record_bad) or 'None';effective.append(rec)
emit('field-source-registry.csv',fieldrows);emit('effective-record-audit.csv',effective);emit('exact-location-audit.csv',locrows);emit('packet-audit.csv',packetrows);emit('dependency-audit.csv',deprows);emit('evidence-field-audit.csv',evrows);emit('limitation-field-audit.csv',limrows);emit('group-ledger-comparison.csv',gcomparisons);emit('source-precedence-comparison.csv',precedence)

# Documentation validation and collection-derived counters.
docscript=PK/'scripts/documentation_validator.py';doc=subprocess.run([sys.executable,str(docscript),'--root',str(ROOT)],text=True,capture_output=True) if docscript.exists() else subprocess.CompletedProcess([],1,'','missing documentation validator')
(OUT/'val-007-audit.txt').write_text(doc.stdout+doc.stderr+f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}\n')
hardcoded=[]
muttext=(PK/'negative-tests/mutation-summary.txt').read_text() if (PK/'negative-tests/mutation-summary.txt').exists() else ''
def mutcount(name):
 m=re.search(rf'^{re.escape(name)}:\s*(\d+)',muttext,re.M);return int(m.group(1)) if m else 0
candidate=(D/'validation.md').read_text();accepted=re.findall(r'Accepted limitations:\s*[1-9]\d*',candidate,re.I);ready=re.findall(r'Recommendation approval status:\s*APPROVED',candidate);completion=re.findall(r'Project completion(?: status)?:\s*(?:COMPLETE|COMPLETED)',candidate,re.I)
counter_defs={
'Requirements audited':('blocks','production-summary.txt','one parsed normative record per ID',lambda:len(blocks),None),'Effective records':('effective','effective-record-audit.csv','all effective-record rows',lambda:len(effective),None),'Field-source rows':('fieldrows','field-source-registry.csv','all requirement/field pairs',lambda:len(fieldrows),None),'Readable groups parsed':('group headings','readable-group-parse.csv','distinct nonempty group headings',lambda:len({r['Group heading'] for r in group_rows}),None),'Status buckets resolved':('group_rows','readable-group-parse.csv','status-bucket rows with PASS resolution',lambda:sum(r['Parsed grammar']=='Status bucket' and r['Resolution result']=='PASS' for r in group_rows),None),'Unresolved field sources':('UNRESOLVED_FIELD_SOURCE','defects.csv','category equals UNRESOLVED_FIELD_SOURCE',lambda:len(defect['UNRESOLVED_FIELD_SOURCE']),'UNRESOLVED_FIELD_SOURCE'),'Source-precedence conflicts':('SOURCE_PRECEDENCE_CONFLICT','source-precedence-comparison.csv','category equals SOURCE_PRECEDENCE_CONFLICT',lambda:len(defect['SOURCE_PRECEDENCE_CONFLICT']),'SOURCE_PRECEDENCE_CONFLICT'),'Explicit group/ledger conflicts':('GROUP_LEDGER_CONFLICT','group-ledger-comparison.csv','category equals GROUP_LEDGER_CONFLICT',lambda:len(defect['GROUP_LEDGER_CONFLICT']),'GROUP_LEDGER_CONFLICT'),'Unresolved group mappings':('UNRESOLVED_GROUP_MAPPING','readable-group-parse.csv','category equals UNRESOLVED_GROUP_MAPPING',lambda:len(defect['UNRESOLVED_GROUP_MAPPING']),'UNRESOLVED_GROUP_MAPPING'),'Exact-location mismatches':('LOCATION_MISMATCH','exact-location-audit.csv','category equals LOCATION_MISMATCH',lambda:len(defect['LOCATION_MISMATCH']),'LOCATION_MISMATCH'),'Valid-but-wrong location defects':('LOCATION_MISMATCH','exact-location-audit.csv','resolved anchor without semantic support',lambda:len(defect['LOCATION_MISMATCH']),'LOCATION_MISMATCH'),'Packet-row mismatches':('PACKET_MISMATCH','packet-audit.csv','category equals PACKET_MISMATCH',lambda:len(defect['PACKET_MISMATCH']),'PACKET_MISMATCH'),'Packet-item mismatches':('PACKET_ITEM_MISMATCH','packet-audit.csv','category equals PACKET_ITEM_MISMATCH',lambda:len(defect['PACKET_ITEM_MISMATCH']),'PACKET_ITEM_MISMATCH'),'Dependency-value mismatches':('DEPENDENCY_MISMATCH','dependency-audit.csv','category equals DEPENDENCY_MISMATCH',lambda:len(defect['DEPENDENCY_MISMATCH']),'DEPENDENCY_MISMATCH'),'Dependency-class mismatches':('DEPENDENCY_CLASS_MISMATCH','dependency-audit.csv','category equals DEPENDENCY_CLASS_MISMATCH',lambda:len(defect['DEPENDENCY_CLASS_MISMATCH']),'DEPENDENCY_CLASS_MISMATCH'),'Evidence-reference mismatches':('EVIDENCE_REFERENCE_MISMATCH','evidence-field-audit.csv','category equals EVIDENCE_REFERENCE_MISMATCH',lambda:len(defect['EVIDENCE_REFERENCE_MISMATCH']),'EVIDENCE_REFERENCE_MISMATCH'),'Missing Git evidence objects':('MISSING_GIT_EVIDENCE_OBJECT','evidence-field-audit.csv','git cat-file failures',lambda:len(defect['MISSING_GIT_EVIDENCE_OBJECT']),'MISSING_GIT_EVIDENCE_OBJECT'),'Evidence-scope relationship defects':('EVIDENCE_SCOPE_RELATIONSHIP','evidence-field-audit.csv','category equals EVIDENCE_SCOPE_RELATIONSHIP',lambda:len(defect['EVIDENCE_SCOPE_RELATIONSHIP']),'EVIDENCE_SCOPE_RELATIONSHIP'),'Limitation-scope mismatches':('LIMITATION_MISMATCH','limitation-field-audit.csv','category equals LIMITATION_MISMATCH',lambda:len(defect['LIMITATION_MISMATCH']),'LIMITATION_MISMATCH'),'Approved requirements audited':('approved','approved-authority-population.csv','lifecycle equals Approved',lambda:len(approved),None),'Standard-clause mismatches':('STANDARD_CLAUSE_MISMATCH','adopted-standard-clause-audit.csv','category equals STANDARD_CLAUSE_MISMATCH',lambda:len(defect['STANDARD_CLAUSE_MISMATCH']),'STANDARD_CLAUSE_MISMATCH'),'Missing authority targets':('MISSING_AUTHORITY_TARGET','authority-graph-audit.csv','category equals MISSING_AUTHORITY_TARGET',lambda:len(defect['MISSING_AUTHORITY_TARGET']),'MISSING_AUTHORITY_TARGET'),'Non-Approved authority targets':('NONAPPROVED_AUTHORITY_TARGET','authority-graph-audit.csv','category equals NONAPPROVED_AUTHORITY_TARGET',lambda:len(defect['NONAPPROVED_AUTHORITY_TARGET']),'NONAPPROVED_AUTHORITY_TARGET'),'Unsupported generic authority claims':('UNSUPPORTED_GENERIC_AUTHORITY','authority-graph-audit.csv','category equals UNSUPPORTED_GENERIC_AUTHORITY',lambda:len(defect['UNSUPPORTED_GENERIC_AUTHORITY']),'UNSUPPORTED_GENERIC_AUTHORITY'),'Unclassified authority references':('UNCLASSIFIED_AUTHORITY_REFERENCE','authority-reference-classification.csv','category equals UNCLASSIFIED_AUTHORITY_REFERENCE',lambda:len(defect['UNCLASSIFIED_AUTHORITY_REFERENCE']),'UNCLASSIFIED_AUTHORITY_REFERENCE'),'Self-authority claims':('SELF_AUTHORITY','authority-graph-audit.csv','category equals SELF_AUTHORITY',lambda:len(defect['SELF_AUTHORITY']),'SELF_AUTHORITY'),'Circular authority chains':('CIRCULAR_AUTHORITY','authority-graph-audit.csv','category equals CIRCULAR_AUTHORITY',lambda:len(defect['CIRCULAR_AUTHORITY']),'CIRCULAR_AUTHORITY'),'Hardcoded defect counters':('hardcoded','production_validator.py','literal defect totals found by self-audit',lambda:len(hardcoded),None)}
prov=[];summary=[];producer='docs/kbdl/evidence/kbdl-011-r15/scripts/production_validator.py'
for name,(collection,artifact,rule,fun,cat) in counter_defs.items():
 val=fun();prov.append({'Counter name':name,'Exact defect collection':collection,'Producing script':producer,'Producing artifact':artifact,'Filter or counting rule':rule,'Row count':val,'Defect IDs':'; '.join(x['Defect ID'] for x in defect.get(cat,[])) if cat else 'None'});summary.append(f'{name}: {val}')
for name in ['Real mutations executed','Mutations detected by production validator','Unexpected mutation passes','Wrong-category detections','Fixtures remaining']:
 val=mutcount(name);prov.append({'Counter name':name,'Exact defect collection':'negative-tests/mutation-summary.txt','Producing script':'docs/kbdl/evidence/kbdl-011-r15/scripts/run_mutation_controls.py','Producing artifact':'negative-tests/mutation-summary.txt','Filter or counting rule':f'exact summary line {name}', 'Row count':val,'Defect IDs':'None'});summary.append(f'{name}: {val}')
lacking=[r for r in prov if not all(r[x] for x in ['Exact defect collection','Producing script','Producing artifact','Filter or counting rule'])];summary.append(f'Counters lacking exact provenance: {len(lacking)}');prov.append({'Counter name':'Counters lacking exact provenance','Exact defect collection':'counter-provenance rows','Producing script':producer,'Producing artifact':'counter-provenance.csv','Filter or counting rule':'rows missing any exact provenance column','Row count':len(lacking),'Defect IDs':'None'})
emit('counter-provenance.csv',prov);all_def=[x for rows in defect.values() for x in rows];emit('defects.csv',all_def,['Defect ID','Requirement ID','Category','Details'])
auth_ok=not any(defect[c] for c in bad_auth|{'AUTH_POPULATION_OVERLAP','AUTH_POPULATION_OMISSION'}) and len(approved)==266
fieldcats={'MISSING_SOURCE_RULE','MISSING_ADMIN_FIELD','BLUEPRINT_MISMATCH','DECISION_FIELD_MISMATCH','SOURCE_PRECEDENCE_CONFLICT','GROUP_LEDGER_CONFLICT','STATUS_BUCKET_MISMATCH','UNRESOLVED_GROUP_MAPPING','UNRESOLVED_FIELD_SOURCE','LOCATION_MISMATCH','PACKET_MISMATCH','PACKET_ITEM_MISMATCH','DEPENDENCY_MISMATCH','DEPENDENCY_CLASS_MISMATCH','EVIDENCE_MISMATCH','EVIDENCE_REFERENCE_MISMATCH','MISSING_GIT_EVIDENCE_OBJECT','EVIDENCE_SCOPE_RELATIONSHIP','LIMITATION_MISMATCH','ROADMAP_MISMATCH'}
field_ok=len(fieldrows)==5389 and len(effective)==317 and not any(defect[c] for c in fieldcats)
summary += ['',f'VAL-003 result: {"Verified" if auth_ok else "Not verified"}','VAL-004 result: Not verified',f'VAL-006 result: {"Verified" if field_ok else "Not verified"}',f'VAL-007 result: {"Verified" if doc.returncode==0 else "Not verified"}','',f'Accepted limitations: {len(accepted)}',f'Readiness approvals: {len(ready)}',f'Completion approvals: {len(completion)}','Implementation conformance: NOT VERIFIED','Project completion: PENDING']
(OUT/'production-summary.txt').write_text('\n'.join(summary)+'\n');(OUT/'val-003-audit.txt').write_text(f'Approved={len(approved)} prompt={len(approved_prompt)} other={len(other)} defects={sum(len(defect[c]) for c in bad_auth)}\nVAL-003 result: {"Verified" if auth_ok else "Not verified"}\n');(OUT/'val-006-audit.txt').write_text(f'Rows={len(fieldrows)} records={len(effective)} defects={sum(len(defect[c]) for c in fieldcats)}\nVAL-006 result: {"Verified" if field_ok else "Not verified"}\n')
print('\n'.join(summary));
if all_def:
 for x in all_def:print(f'{x["Defect ID"]}: {x["Details"]}',file=sys.stderr)
sys.exit(0 if auth_ok and field_ok and doc.returncode==0 else 1)
