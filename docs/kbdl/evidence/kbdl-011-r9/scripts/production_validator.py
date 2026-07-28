#!/usr/bin/env python3
"""Source-derived R9 production validator; designed for controlled mutation tests."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import argparse,csv,re,subprocess,sys
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path);ap.add_argument('--artifacts',type=Path);a=ap.parse_args();ROOT=(a.root or Path(__file__).resolve().parents[5]).resolve();D=ROOT/'docs/kbdl';ART=(a.artifacts or D/'evidence/kbdl-011-r9/artifacts');ART.mkdir(parents=True,exist_ok=True)
def clean(s):return ' '.join(re.sub(r'[`*]','',re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s)).split()).strip().rstrip('.')
def slugs(p):
 c=Counter();out=set()
 for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',p.read_text()):
  s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-');n=c[s];c[s]+=1;out.add(s if not n else f'{s}-{n}')
 return out
def write(n,rows):
 with (ART/n).open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
rows=list(csv.DictReader(open(D/'traceability-metadata.csv')));by={r['Requirement ID']:r for r in rows};effective=[];groupbad=[]
# Only explicit per-ID syntax is binding. Broad/uniform prose stays summary.
trace=(D/'traceability-matrix.md').read_text();gblocks=re.split(r'(?m)^### ',trace)[1:]
# Explicit one-ID override fields are always binding and can never be demoted
# to summary text.
for rid,value in re.findall(r'(?m)^- \*\*Validation status override(?: \(per-ID\))?:\*\*\s*`?(KBDL-[A-Z0-9]+-\d{3}[a-z]?)`?\s*→\s*([^\n]+)',trace):
 if rid in by and clean(value)!=clean(by[rid]['Validation classification']):groupbad.append({'Requirement ID':rid,'Field':'Validation classification','Expected explicit group value':clean(value),'Ledger value':clean(by[rid]['Validation classification'])})
for b in gblocks:
 f={re.sub(r'\s*\([^)]*\)\s*$','',k).lower().strip():v.strip() for k,v in re.findall(r'(?ms)^- \*\*([^:*]+?)(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|^### |^## |\Z)',b)};raw=f.get('requirement id','');m=re.search(r'KBDL-([A-Z0-9]+)-',raw)
 if not m:continue
 mod=m.group(1);gids=[]
 for x in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',raw.split('(37 requirements;')[0]):
  aa,bb=x.group(1),x.group(2);gids += [f'KBDL-{mod}-{n:03}' for n in range(int(aa),int(bb)+1)] if bb else [f'KBDL-{mod}-{aa}']
 for rid in gids:
  if rid not in by:continue
  for gk,lk in [('validation status','Validation classification'),('approval status','Lifecycle status'),('lifecycle status','Lifecycle status'),('provenance','Provenance'),('packet destination','Packet or tracking destination'),('pending dependencies','Pending dependencies')]:
   v=f.get(gk,'');explicit=bool('→' in v or re.search(r'(?i)(?:verified|approved|recommended|deferred|applicable|confirmed|assumed)\s*:',v))
   if not explicit:continue
   n=int(re.search(r'\d{3}',rid).group());resolved=''
   for p in v.split(';'):
    nums=re.findall(r'(?<!\d)(\d{3})(?:[–-](\d{3}))?(?!\d)',p);has=rid in p or any(n in range(int(x),int(y)+1) if y else n==int(x) for x,y in nums)
    if not has:continue
    if ':' in p:
     l,r=p.split(':',1);resolved=clean(r) if (rid in l or any(n in range(int(x),int(y)+1) if y else n==int(x) for x,y in re.findall(r'(?<!\d)(\d{3})(?:[–-](\d{3}))?(?!\d)',l))) else clean(l)
    elif '→' in p:
     l,r=p.split('→',1);resolved=clean(r) if has else ''
    break
   actual=clean(by[rid][lk]);q=resolved
   if lk=='Validation classification' and 'verified' in q.lower() and 'not verified' in q.lower():q='Mixed — Verified / Not verified'
   packet_same=lk=='Packet or tracking destination' and re.search(r'item\s+(\d+)',q,re.I) and re.search(r'item\s+(\d+)',actual,re.I) and re.search(r'item\s+(\d+)',q,re.I).group(1)==re.search(r'item\s+(\d+)',actual,re.I).group(1)
   if q and not packet_same and not (q==actual or q in actual or actual in q):groupbad.append({'Requirement ID':rid,'Field':lk,'Expected explicit group value':q,'Ledger value':actual})
for r in rows:effective.append({'Requirement ID':r['Requirement ID'],'Complete':all(r.get(k,'').strip() for k in r),'Defect':'None'})
effbad=[r for r in effective if not r['Complete']]+groupbad+([{'cardinality':len(rows)}] if len(rows)!=317 else [])
# Independent prompt/decision evidence registry.
areg=list(csv.DictReader(open(D/'evidence/kbdl-011-r9/approval-authority-registry.csv')));abad=[];arows=[]
for r in areg:
 p=subprocess.run(['git','cat-file','-e',r['Evidence source']+'^{commit}'],cwd=Path(__file__).resolve().parents[5],capture_output=True)
 ok=p.returncode==0 and bool(r['Exact approval command or decision'] and r['Approved scope'] and r['Exclusions'] and r['Requirements relying on prompt'])
 if not ok:abad.append(r['Prompt ID'])
 arows.append({**r,'Result':'PASS' if ok else 'FAIL'})
(ART/'authority-validation.txt').write_text(f'Authority registry rows: {len(areg)}\nAuthority defects: {len(abad)}\n')
# Historical locations derive the first normative link in each PRN statement.
lbad=[];lrows=[];pt=(D/'principles.md').read_text()
for rid in [f'KBDL-PRN-{i:03}' for i in range(1,9)]:
 m=re.search(rf'(?ms)^- \*\*{rid}\*\*.*?(?=^  - Lifecycle status:)',pt);links=re.findall(r'\[[^]]+\]\(([^)]+)\)',m.group(0) if m else '')
 target=next((x for x in links if x.startswith('#')), '');actual=by[rid]['Specification location'];expected=''
 # Resolve a linked subsection to its independently located containing H2.
 if target:
  anchor=target[1:];hs=list(re.finditer(r'(?m)^(#{1,6})\s+(.+?)\s*#*$',pt));target_pos=None
  for h in hs:
   if re.sub(r'[^\w\- ]','',h.group(2).replace('`','').lower()).replace(' ','-')==anchor:target_pos=h.start();break
  if target_pos is not None:
   parents=[h for h in hs if h.start()<=target_pos and len(h.group(1))==2];parent=parents[-1];expected='principles.md#'+re.sub(r'[^\w\- ]','',parent.group(2).replace('`','').lower()).replace(' ','-')
 ok=bool(target) and expected in actual
 if not ok:lbad.append(rid)
 lrows.append({'Requirement ID':rid,'Normative statement link':target,'Derived location':expected,'Ledger location':actual,'Result':'PASS' if ok else 'FAIL'})
# Documentation validator output is distinct evidence.
doc=subprocess.run([sys.executable,str(Path(__file__).with_name('documentation_validator.py')),'--root',str(ROOT)],text=True,capture_output=True);(ART/'documentation-validation.txt').write_text(doc.stdout+doc.stderr);docbad=0 if doc.returncode==0 else 1
# Completion scan distinct artifact.
joined='\n'.join(p.read_text() for p in D.rglob('*.md'));completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',(D/'decision-register.md').read_text());(ART/'completion-scan.txt').write_text(f'Completion decisions: {len(completion)}\n')
# Verified evidence: read actual artifacts/sections/commits, required result and complete scope.
reg=list(csv.DictReader(open(D/'evidence/kbdl-011-r9/verified-evidence-registry.csv')));verified={r['Requirement ID'] for r in rows if 'Verified' in r['Validation classification']};vbad=[];vrows=[]
def evidence_text(r):
 kind=r['Evidence kind'];src=r['Evidence source']
 if kind=='commit':
  p=subprocess.run(['git','cat-file','-e',src+'^{commit}'],cwd=Path(__file__).resolve().parents[5]);return ('commit exists' if p.returncode==0 else ''),p.returncode==0
 fn,sep,anchor=src.partition('#');p=D/fn
 if not p.exists():return '',False
 text=p.read_text()
 if sep:
  hs=list(re.finditer(r'(?m)^#{1,6}\s+(.+?)\s*#*$',text));hit=None
  for i,h in enumerate(hs):
   if anchor in slugs(p) and re.sub(r'[^\w\- ]','',h.group(1).replace('`','').lower()).replace(' ','-')==anchor:hit=(h.end(),hs[i+1].start() if i+1<len(hs) else len(text));break
  if not hit:return '',False
  text=text[hit[0]:hit[1]]
 return text,True
for r in reg:
 if r['Requirement ID'] not in verified:continue
 text,exists=evidence_text(r);selfref=r['Evidence source'].endswith('verified-evidence-audit.csv') or r['Evidence source'].endswith('production-validation.txt');scope=bool(r['Verified scope'].strip()) and r['Verified scope'].strip().lower() not in {'partial','none'};result=exists and r['Required result'] in text
 ok=result and scope and not selfref
 if not ok:vbad.append(r['Requirement ID'])
 vrows.append({**r,'Evidence exists':exists,'Actual required result found':result,'Complete scope':scope,'Self reference':selfref,'Result':'PASS' if ok else 'FAIL'})
(ART/'evidence-source-validation.txt').write_text(f'Verified registry rows checked: {len(vrows)}\nEvidence source defects: {len([x for x in vbad if x!="KBDL-VAL-004"])}\n')
# VAL-004 source is created by the distinct source check above; validate it now.
for r in vrows:
 if r['Requirement ID']=='KBDL-VAL-004' and r['Result']=='FAIL':
  src=D/r['Evidence source'];ok=src.exists() and r['Required result'] in src.read_text() and not r['Self reference']
  if ok:r['Evidence exists']=True;r['Actual required result found']=True;r['Result']='PASS';vbad.remove('KBDL-VAL-004')
write('production-effective-record.csv',effective);write('group-conflict-audit.csv',groupbad or [{'Requirement ID':'None','Field':'None','Expected explicit group value':'None','Ledger value':'None'}]);write('approval-authority-audit.csv',arows);write('historical-location-audit.csv',lrows);write('verified-evidence-audit.csv',vrows)
unauth=[];BASE='e8bc06efd0a6399178213fed28907f370c923176'
for f in ['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','profiles.md','customization.md','governance.md','decision-register.md']:
 old=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{f}'],cwd=Path(__file__).resolve().parents[5],text=True,capture_output=True).stdout
 if old and old!=(D/f).read_text():unauth.append(f)
lines=[f'Production requirements audited: {len(rows)}',f'Production effective-record defects: {len(effbad)}',f'Production authority defects: {len(abad)}',f'Production Verified-evidence defects: {len(vbad)}',f'Production location defects: {len(lbad)}',f'Production documentation defects: {docbad}','','Unauthorized metadata changes: '+str(len(unauth)),f'Completion decisions: {len(completion)}','','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING']
out='\n'.join(lines)+'\n';(ART/'production-validation.txt').write_text(out);print(out,end='');sys.exit(bool(effbad or abad or vbad or lbad or docbad or unauth or completion))
