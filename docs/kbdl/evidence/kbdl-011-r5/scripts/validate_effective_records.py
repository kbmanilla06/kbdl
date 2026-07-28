#!/usr/bin/env python3
"""Independent effective group-plus-ledger traceability audit."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import csv,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[5]; DOC=ROOT/'docs/kbdl'; ART=DOC/'evidence/kbdl-011-r5/artifacts';ART.mkdir(parents=True,exist_ok=True);BASE='7c096942ce6ed0cea4968e5f8588d0045839642e'
FILES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']; RX=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
def plain(x):
 x=' '.join(re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',x).replace('`','').replace('**','').split()).strip();x=re.sub(r'\s+-\s*$','',x);return x.rstrip('.')
def value(block,label):
 pattern=label.replace(' ',r'\s+');m=re.search(r'(?is)\b'+pattern+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status)?|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Validation\s+method(?:/evidence)?|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependenc(?:y|ies))\s*:|\n\s*- (?:Related|Applicable)[^:]*:|\Z)',block)
 return plain(m.group(1)) if m else ''
def parse_sources(source_text):
 out={}
 for fn,t in source_text.items():
  starts=list(RX.finditer(t))
  for i,m in enumerate(starts):
   end=starts[i+1].start() if i+1<len(starts) else len(t);h=re.search(r'(?m)^## ',t[m.end():end]);end=m.end()+h.start() if h else end;out.setdefault(m.group(1),(fn,t[m.start():end]))
 return out
texts={f:(DOC/f).read_text() for f in FILES};auth=parse_sources(texts);gov=(DOC/'governance.md').read_text()
for n in range(1,4):auth[f'KBDL-GOV-{n:03d}']=('governance.md',gov)
def gf(block,label):
 m=re.search(r'(?ms)^- \*\*'+label+r'(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|^### |^## |\Z)',block,re.I);return plain(m.group(1)) if m else ''
groups={};raw_groups={}
for block in re.split(r'(?m)^### ',(DOC/'traceability-matrix.md').read_text())[1:]:
 raw=gf(block,'Requirement ID');p=re.search(r'KBDL-([A-Z0-9]+)-',raw)
 if not p:continue
 mod=p.group(1);scope=raw.split('(37 requirements;')[0];ids=[]
 for m in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',scope):
  a,b=m.group(1),m.group(2);ids += [f'KBDL-{mod}-{x:03}' for x in range(int(a),int(b)+1)] if b else [f'KBDL-{mod}-{a}']
 for rid in ids:groups.setdefault(rid,{k:gf(block,k) for k in ('Blueprint section','Roadmap prompt','Specification location','Approval status','Lifecycle status','Provenance','Validation status','Authority','Validation method','Validation evidence','Known limitation','Packet destination','Decision-packet destination','Pending dependencies')});raw_groups[rid]=block
ledger=list(csv.DictReader(open(DOC/'traceability-metadata.csv')));rows={r['Requirement ID']:r for r in ledger};count=Counter(r['Requirement ID'] for r in ledger)
missing=sorted(set(auth)-set(rows)-set(groups));dups=sorted(k for k,n in count.items() if n!=1);aud=[];conf=[];locaudit=[];authaudit=[];elaudit=[];pdaudit=[]
status_bad=[];fileonly=[];badanchor=[];locbad=[];lifefallback=[];unresolved=[];authbad=[];method_evidence=[];generic_lim=[];packetbad=[];depbad=[]
dec=(DOC/'decision-register.md').read_text();approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec));allids=set(auth)
def astat(rid,b):
 if rid.startswith('KBDL-GOV-'):return 'Verified' if rid in ('KBDL-GOV-001','KBDL-GOV-003') else 'Not verified'
 v=value(b,'Validation status') or value(b,'Validation');hasv=bool(re.search(r'(?<!not )\bverified\b',v,re.I));hasn='not verified' in v.lower();hasa='not applicable' in v.lower();k=[x for x,y in [('Verified',hasv),('Not verified',hasn),('Not applicable',hasa)] if y];return 'Mixed — '+' / '.join(k) if len(k)>1 else (k[0] if k else 'Not verified')
def headings(path):
 seen=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',path.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');n=seen[s];seen[s]+=1;out.add(s if not n else f'{s}-{n}')
 return out
for rid,(src,b) in sorted(auth.items()):
 r=rows.get(rid,{});g=groups.get(rid,{});alife='Approved' if rid.startswith('KBDL-GOV-') else (value(b,'Lifecycle status') or value(b,'Lifecycle')).split(' — ',1)[0].split(' (',1)[0];aprov='Historical KBDL-001 prompt and approved decision record' if rid.startswith('KBDL-GOV-') else value(b,'Provenance');aval=astat(rid,b);evals=r.get('Validation classification','')
 # A simple single-status group is an explicit override; composite summaries defer to the per-ID ledger.
 gv=g.get('Validation status','');tokens=set(re.findall(r'(?i)(?<!not )\bVerified\b|Not verified|Not applicable',gv));single=(len(tokens)==1 and not re.search(r'KBDL-[A-Z]+-\d',gv))
 gc=[]
 if single and next(iter(tokens)).lower()!=evals.lower():gc.append('validation status')
 if (g.get('Lifecycle status') or g.get('Approval status')) and alife.lower() not in (g.get('Lifecycle status') or g.get('Approval status')).lower():gc.append('lifecycle')
 if gc:conf.append({'Requirement ID':rid,'Fields':'; '.join(gc),'Group validation':gv,'Ledger validation':evals})
 if evals!=aval:status_bad.append(rid)
 loc=r.get('Specification location','');lm=re.search(r'(?ms)^- \*\*Specification location(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|\Z)',raw_groups.get(rid,''),re.I);location_links=re.findall(r'\[[^]]+\]\(([^)]+)\)',lm.group(1)) if lm else []
 if not location_links or not ('§' in loc or '#' in loc):fileonly.append(rid)
 invalid=[]
 for link in location_links:
  target,_,anchor=link.partition('#');p=(DOC/target if target else DOC/src).resolve()
  if not p.exists() or (anchor and unquote(anchor) not in headings(p)):invalid.append(link)
 if invalid:badanchor.append(rid)
 if plain(g.get('Specification location',''))!=loc:locbad.append(rid)
 locaudit.append({'Requirement ID':rid,'Effective location':loc,'Group location':g.get('Specification location',''),'Ledger location':r.get('Specification location',''),'Links checked':'; '.join(location_links),'Invalid links':'; '.join(invalid) or 'None'})
 authority=r.get('Authority','');
 if re.match(r'^Lifecycle authority:\s*(?:Approved|Recommended|Deferred)\s*$',authority):lifefallback.append(rid)
 targets=set(re.findall(r'KBDL-(?:DEC-\d{3}|(?:GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)',authority));absent=[x for x in targets if (x.startswith('KBDL-DEC-') and x not in approved_dec) or (not x.startswith('KBDL-DEC-') and x not in allids)]
 validauth=bool(authority) and bool(re.search(r'KBDL-(?:DEC|GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-|WCAG|WAI-ARIA|ARIA|approved .*prompt|project-owner-approved|adopted',authority,re.I)) and not re.search(r'pending explicit|not applicable|Lifecycle authority:\s*Approved$',authority,re.I) and not absent
 if alife=='Approved' and not validauth:unresolved.append(rid)
 if absent:authbad.append(rid)
 authaudit.append({'Requirement ID':rid,'Lifecycle':alife,'Authority source':'Authoritative field, lifecycle rationale, approved module prompt, decision, standard, or prior Approved requirement','Effective authority':authority,'Targets':'; '.join(sorted(targets)) or 'None','Missing targets':'; '.join(absent) or 'None','Resolved':validauth})
 method=r.get('Validation method','');evidence=r.get('Validation evidence','');lim=r.get('Known limitation','')
 if method==evidence:method_evidence.append(rid)
 if lim in ('None documented','Method not yet fully executed','No additional limitation identified by the recorded review'):generic_lim.append(rid)
 elaudit.append({'Requirement ID':rid,'Validation method':method,'Validation evidence':evidence,'Known limitation':lim,'Method copied as evidence':method==evidence,'Generic limitation':rid in generic_lim})
 packet=r.get('Packet or tracking destination','');dep=r.get('Pending dependencies','');life=alife
 if life=='Approved':pok=packet=='None — Approved'
 else:pok=bool(re.search(r'item \d+|Approval-ready item \d+|Contingent|Deferred',packet,re.I)) and not re.search(r'owning module|generic|fallback|unknown',packet,re.I)
 expected=value(b,'Pending dependencies') or value(b,'Pending dependency') or 'None';dok=dep==expected
 if not pok:packetbad.append(rid)
 if not dok:depbad.append(rid)
 pdaudit.append({'Requirement ID':rid,'Packet destination':packet,'Pending dependencies':dep,'Packet match':pok,'Dependency match':dok})
 defects=[]
 for label,test in [('group/ledger conflict',rid in {x['Requirement ID'] for x in conf}),('validation mismatch',rid in status_bad),('location',rid in fileonly or rid in badanchor or rid in locbad),('authority',rid in lifefallback or rid in unresolved or rid in authbad),('evidence/limitation',rid in method_evidence or rid in generic_lim),('packet/dependency',rid in packetbad or rid in depbad)]:
  if test:defects.append(label)
 aud.append({'Requirement ID':rid,'Authoritative lifecycle':alife,'Effective lifecycle':r.get('Lifecycle status'),'Authoritative provenance':aprov,'Effective provenance':r.get('Provenance'),'Authoritative validation status':aval,'Effective validation status':evals,'Authority source':'authoritative/prompt/decision/standard/prior Approved requirement','Effective authority':authority,'Exact specification location':loc,'Group location':g.get('Specification location',''),'Ledger location':r.get('Specification location',''),'Validation method':method,'Validation evidence':evidence,'Known limitation':lim,'Packet destination':packet,'Pending dependencies':dep,'Match result':'PASS' if not defects else 'FAIL','Defect details':'; '.join(defects) or 'None'})
def write(name,data,cols=None):
 with (ART/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=cols or list(data[0]),lineterminator='\n');w.writeheader();w.writerows(data)
write('effective-record-audit.csv',aud);write('group-ledger-conflicts.csv',conf,['Requirement ID','Fields','Group validation','Ledger validation']);write('exact-location-audit.csv',locaudit);write('authority-resolution.csv',authaudit);write('evidence-limitation-audit.csv',elaudit);write('packet-dependency-audit.csv',pdaudit)
# Protected authoritative metadata is compared directly to the immutable baseline.
unauth=[]
for fn in FILES+['governance.md']:
 old=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{fn}'],cwd=ROOT,text=True,capture_output=True,check=True).stdout;new=(DOC/fn).read_text()
 if fn!='validation.md' and old!=new:unauth.append(fn)
completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',dec)
errors=sum(map(len,[missing,dups,conf,status_bad,fileonly,badanchor,locbad,lifefallback,unresolved,authbad,method_evidence,generic_lim,packetbad,depbad,unauth,completion]))
out=[f'Requirements audited: {len(auth)}',f'Effective traceability records: {len(aud)}',f'Missing effective records: {len(missing)}',f'Duplicate effective records: {len(dups)}','',f'Group/ledger conflicts: {len(conf)}',f'Validation-status mismatches: {len(status_bad)}',f'File-only specification locations: {len(fileonly)}',f'Invalid location anchors: {len(badanchor)}',f'Effective location mismatches: {len(locbad)}','',f'Lifecycle-only authority fallbacks: {len(lifefallback)}',f'Approved requirements with unresolved authority: {len(unresolved)}',f'Authority inconsistencies: {len(authbad)}',f'Method-as-evidence fallbacks: {len(method_evidence)}',f'Unsupported generic limitations: {len(generic_lim)}','',f'Packet-destination mismatches: {len(packetbad)}',f'Dependency mismatches: {len(depbad)}',f'Unauthorized metadata changes: {len(unauth)}',f'Completion decisions: {len(completion)}','','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING',f'Errors: {errors}']
(ART/'validation-output.txt').write_text('\n'.join(out)+'\n');print('\n'.join(out));sys.exit(bool(errors))
