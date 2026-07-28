#!/usr/bin/env python3
"""Validate KBDL Markdown files, local links/anchors, tables, and roadmap wording."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import re, sys
ROOT=Path(__file__).resolve().parents[5]
DOC=ROOT/'docs/kbdl'; errors=[]; files=sorted(DOC.rglob('*.md'))
def slug(s):
    s=re.sub(r'<[^>]+>','',s).strip().lower().replace('`','')
    return re.sub(r'[^\w\- ]','',s).replace(' ','-')
anchors={}
for p in files:
    counts=Counter(); found=set()
    for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',p.read_text(),re.M):
        base=slug(h); n=counts[base]; counts[base]+=1; found.add(base if not n else f'{base}-{n}')
    anchors[p.resolve()]=found
for p in files:
    text=p.read_text()
    if re.search(r'<<<<<<<|=======|>>>>>>>',text): errors.append(f'conflict marker: {p}')
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
        target=target.split()[0].strip('<>')
        if re.match(r'^[a-z]+:',target) or target.startswith('mailto:'): continue
        filepart,_,frag=target.partition('#'); dest=((p.parent/unquote(filepart)).resolve() if filepart else p.resolve())
        if not dest.exists(): errors.append(f'broken link: {p.relative_to(DOC)} -> {target}'); continue
        if frag and dest.suffix=='.md' and unquote(frag) not in anchors.get(dest,set()): errors.append(f'broken anchor: {p.relative_to(DOC)} -> {target}')
    lines=text.splitlines()
    for i,line in enumerate(lines):
        if line.startswith('|') and i+1<len(lines) and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[i+1]):
            width=line.count('|')
            j=i+1
            while j<len(lines) and lines[j].startswith('|'):
                if lines[j].count('|')!=width: errors.append(f'table width: {p.relative_to(DOC)}:{j+1}')
                j+=1
joined='\n'.join(p.read_text() for p in files)
stale=len(re.findall(r'first seven steps of a ten-step|current (?:approved )?roadmap.{0,30}ten-step',joined,re.I))
if stale: errors.append(f'stale current-roadmap claims: {stale}')
print(f'Markdown files: {len(files)}')
print(f'Stale ten-step current-roadmap claims: {stale}')
print(f'Documentation errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
