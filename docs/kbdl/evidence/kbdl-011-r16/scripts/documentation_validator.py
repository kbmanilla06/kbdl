#!/usr/bin/env python3
"""Complete dependency-free KBDL documentation validator with category output."""
from pathlib import Path
from collections import Counter,defaultdict
from urllib.parse import unquote
import argparse,csv,re,sys
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path);a=ap.parse_args();ROOT=(a.root or Path(__file__).resolve().parents[5]).resolve();D=ROOT/'docs/kbdl'
cats=['relative links','anchors','heading hierarchy','duplicate headings','empty required sections','placeholder text','conflict markers','markdown tables','requirement IDs','decision IDs','packet references','visible numbered-section labels','stale roadmap wording','premature readiness/completion claims'];err=defaultdict(list)
files=sorted(D.rglob('*.md'))
def slug(s):return re.sub(r'[^\w\- ]','',re.sub(r'<[^>]+>','',s).strip().lower().replace('`','')).replace(' ','-')
anchors={};headings={}
for p in files:
 hs=re.findall(r'(?m)^(#{1,6})\s+(.+?)\s*#*$',p.read_text());headings[p]=hs;c=Counter();aset=set()
 for _,h in hs:
  b=slug(h);n=c[b];c[b]+=1;aset.add(b if not n else f'{b}-{n}')
 for h,n in c.items():
  if n>1 and 'evidence/' not in p.relative_to(D).as_posix() and p.name!='traceability-matrix.md':err['duplicate headings'].append(f'{p.relative_to(D)}:{h}')
 anchors[p.resolve()]=aset
 prev=0
 for marks,h in hs:
  level=len(marks)
  if prev and level>prev+1:err['heading hierarchy'].append(f'{p.relative_to(D)}:{h}')
  prev=level
 # A heading with no non-heading content before the next heading is empty.
 # Only a leaf required section (next heading same/higher level) may be empty.
 matches=list(re.finditer(r'(?m)^(#{1,6})\s+(.+?)\s*#*$',p.read_text()))
 for i,h in enumerate(matches):
  body=p.read_text()[h.end():(matches[i+1].start() if i+1<len(matches) else len(p.read_text()))].strip();next_level=len(matches[i+1].group(1)) if i+1<len(matches) else 0
  if not body and (not next_level or next_level<=len(h.group(1))) and re.search(r'(?i)required|mandatory',h.group(2)):err['empty required sections'].append(f'{p.relative_to(D)}:{h.group(2)}')
for p in files:
 text=p.read_text();lines=text.splitlines()
 if re.search(r'(?m)^(?:<<<<<<<|=======|>>>>>>>)',text):err['conflict markers'].append(str(p.relative_to(D)))
 if re.search(r'(?im)^\s*(?:TODO|TBD|FIXME)\b|<placeholder>',text):err['placeholder text'].append(str(p.relative_to(D)))
 for target in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',text):
  target=target.split()[0].strip('<>')
  if re.match(r'^[a-z]+:',target) or target.startswith('mailto:'):continue
  fn,sep,frag=target.partition('#');dest=((p.parent/unquote(fn)).resolve() if fn else p.resolve())
  if not dest.exists():err['relative links'].append(f'{p.relative_to(D)}->{target}');continue
  if sep and dest.suffix=='.md' and unquote(frag) not in anchors.get(dest,set()):err['anchors'].append(f'{p.relative_to(D)}->{target}')
 for i,line in enumerate(lines):
  if line.startswith('|') and i+1<len(lines) and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[i+1]):
   width=line.count('|');j=i+1
   while j<len(lines) and lines[j].startswith('|'):
    if lines[j].count('|')!=width:err['markdown tables'].append(f'{p.relative_to(D)}:{j+1}')
    j+=1
 # Visible § labels must agree with numeric target anchors when both are explicit.
 for label,target in re.findall(r'\[([^]]+)\]\(([^)]+)\)',text):
  m=re.fullmatch(r'§\s*(\d+(?:\.\d+)?)',label)
  if not m or '#' not in target:continue
  shown=''.join(m.group(1).split('.'));anch=target.rsplit('#',1)[1].split('-',1)[0]
  if shown and anch.isdigit() and shown!=anch:err['visible numbered-section labels'].append(f'{p.relative_to(D)}:{label}->{target}')
rows=list(csv.DictReader(open(D/'traceability-metadata.csv')));rids=[r['Requirement ID'] for r in rows]
if len(rids)!=317 or len(set(rids))!=317:err['requirement IDs'].append(f'ledger count={len(rids)} unique={len(set(rids))}')
authoritative='\n'.join((D/f).read_text() for f in ['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md'])+(D/'governance.md').read_text()
for rid in rids:
 if rid not in authoritative:err['requirement IDs'].append(f'missing authoritative {rid}')
dec=(D/'decision-register.md').read_text();dids=re.findall(r'(?m)^### (KBDL-DEC-\d{3})\b',dec)
if len(dids)!=16 or len(set(dids))!=16 or dids!=[f'KBDL-DEC-{i:03}' for i in range(1,17)]:err['decision IDs'].append(f'count/order/unique defect: {dids}')
for r in rows:
 if r['Lifecycle status']!='Approved' and not re.search(r'item \d+|Approval-ready item \d+|Contingent|Deferred',r['Packet or tracking destination'],re.I):err['packet references'].append(r['Requirement ID'])
joined='\n'.join(p.read_text() for p in files)
current_joined='\n'.join(p.read_text() for p in files if 'evidence/' not in p.relative_to(D).as_posix())
if re.search(r'first seven steps of a ten-step|current (?:approved )?roadmap.{0,30}ten-step|validate KBDL-011-R8 next|NOT READY pending durable prompt-authority recovery',current_joined,re.I):err['stale roadmap wording'].append('stale roadmap/readiness phrase')
if re.search(r'(?i)(?:KBDL project is complete|completion approved|implementation conformance\s*(?:is|:)\s*(?:verified|pass))',current_joined):err['premature readiness/completion claims'].append('premature completion/conformance claim')
total=sum(map(len,err.values()));print(f'Markdown files: {len(files)}')
for c in cats:print(f'{c}: {len(err[c])}')
print(f'Documentation defects: {total}')
for c in cats:
 for x in err[c]:print(f'{c}: {x}')
sys.exit(bool(total))
