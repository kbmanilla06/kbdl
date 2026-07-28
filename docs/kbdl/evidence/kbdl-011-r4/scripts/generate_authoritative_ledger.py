#!/usr/bin/env python3
"""Generate the traceability ledger only from authoritative Markdown."""
from pathlib import Path
import csv, re

REPO = Path(__file__).resolve().parents[5]
DOC = REPO / "docs/kbdl"
OUT = DOC / "traceability-metadata.csv"
MODULE_PROMPT = {"GOV":"KBDL-001","PRN":"KBDL-002","FND":"KBDL-003","THM":"KBDL-004","MOT":"KBDL-005","RSP":"KBDL-006","A11Y":"KBDL-006","CMP":"KBDL-007/008","PRO":"KBDL-009","CUS":"KBDL-010","VAL":"KBDL-011"}
START = re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
LABEL = re.compile(r'(?i)(Lifecycle\s+status|Lifecycle|Provenance|Validation\s+status|Validation|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Validation\s+method/evidence|Validation\s+method|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependencies|Pending\s+dependency)\s*:')

def clean(value):
    value = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', value)
    value = value.replace('`','').replace('**','')
    return ' '.join(value.split()).strip().rstrip('.')

def fields(block):
    marks=list(LABEL.finditer(block)); result={}
    for i,m in enumerate(marks):
        key=' '.join(m.group(1).lower().split()).replace(' status','').replace('decision-','').replace(' dependencies',' dependency')
        if key.startswith('authority'): key='authority'
        raw=block[m.end():(marks[i+1].start() if i+1<len(marks) else len(block))]
        raw=re.split(r'\n\s*- (?:Related|Applicable|Specification|Validation|Known|Packet|Decision-packet|Pending)[^:]*:',raw,1)[0]
        raw=re.sub(r'\n\s*-\s*$','',raw)
        value=clean(raw)
        result[key]=value
    return result

def scopes(value):
    low=value.lower(); kinds=[]
    if re.search(r'(?<!not )\bverified\b',low): kinds.append('Verified')
    if 'not verified' in low: kinds.append('Not verified')
    if 'not applicable' in low: kinds.append('Not applicable')
    if not kinds: kinds=['Not verified']
    classification='Mixed — '+' / '.join(kinds) if len(kinds)>1 else kinds[0]
    return classification, value if 'Verified' in kinds else 'None', value if 'Not verified' in kinds else 'None', value if 'Not applicable' in kinds else 'None'

AUTHORITATIVE=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
texts={name:(DOC/name).read_text() for name in AUTHORITATIVE}
records={}
for source,text in texts.items():
    matches=list(START.finditer(text))
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(text)
        heading=re.search(r'(?m)^## ',text[m.end():end])
        if heading:end=m.end()+heading.start()
        records.setdefault(m.group(1),(source,text[m.start():end]))

# The three KBDL-001 governance records use the documented historical format.
gov=(DOC/'governance.md').read_text()
for n in range(1,4):
    rid=f'KBDL-GOV-{n:03d}'; marker=re.search(rf'(?m)^## {re.escape(rid)}\b',gov)
    nextm=re.search(r'(?m)^## KBDL-GOV-',gov[marker.end():]) if marker else None
    block=gov[marker.start():marker.end()+(nextm.start() if nextm else len(gov))] if marker else ''
    records[rid]=('governance.md',block)

def packet_lookup(rid, source, block, lifecycle):
    if lifecycle=='Approved': return 'None — Approved'
    f=fields(block); explicit=f.get('packet destination','')
    if explicit: return explicit
    found=[]
    for packet_source,packet_text in texts.items():
      heading=''
      for line in packet_text.splitlines():
        if re.match(r'^#{2,5} ',line): heading=clean(line.lstrip('# '))
        if line.startswith('|') and rid in line and ('packet' in heading.lower() or 'recommended decisions' in heading.lower()):
            cells=[clean(x) for x in line.strip('|').split('|')]; item=cells[0]
            if item and not re.match(r'^[-:]+$',item): found.append((packet_source,item,f'{packet_source} — {heading} — item {item}'))
    primary=[x[2] for x in found if x[0]==source and re.fullmatch(r'\d+',x[1])]
    if len(set(primary))==1:return primary[0]
    numeric=[x[2] for x in found if re.fullmatch(r'\d+',x[1])]
    if numeric:return '; '.join(sorted(set(numeric)))
    if len(set(x[2] for x in found))==1:return found[0][2]
    raise ValueError(f'{rid}: exact {lifecycle!r} packet destination unresolved ({found})')

rows=[]
for rid,(source,block) in sorted(records.items()):
    f=fields(block)
    if rid.startswith('KBDL-GOV-'):
        lifecycle='Approved'; provenance='Historical KBDL-001 prompt and approved decision record'
        validation='Verified' if rid in ('KBDL-GOV-001','KBDL-GOV-002') else 'Not verified'
        authority='Approved KBDL-001 prompt and KBDL-DEC-001/KBDL-DEC-002'
        location=f'governance.md#{rid.lower()}'; method='Historical governance-record review'; evidence=block; limitation='Historical record predates per-field metadata format'
    else:
        lifecycle=f.get('lifecycle','').split(' — ',1)[0].split(' (',1)[0].strip()
        provenance=f.get('provenance',''); validation=f.get('validation','')
        authority=f.get('authority') or ('Lifecycle authority: '+f.get('lifecycle',''))
        location=f.get('specification location') or source
        method=f.get('validation method/evidence') or f.get('validation method','')
        evidence=f.get('validation evidence') or method
        limitation=f.get('known limitation') or ('None documented' if 'verified' in validation.lower() else 'Method not yet fully executed')
    classification,verified,notverified,na=scopes(validation)
    dependency=f.get('pending dependency','') or 'None'
    depclass=('None' if dependency=='None' else 'Deferred' if lifecycle=='Deferred' else 'Context-only' if re.search(r'context|reference|does not block',dependency,re.I) else 'Later implementation validation' if re.search(r'implementation|once implemented',dependency,re.I) else 'Blocking')
    decisions='; '.join(sorted(set(re.findall(r'KBDL-DEC-\d{3}',authority+' '+block)))) or 'None'
    module=rid.split('-')[1]
    rows.append({'Requirement ID':rid,'Blueprint section':module+' authoritative requirement','Roadmap prompt':MODULE_PROMPT[module],
      'Specification location':location,'Source file':source,'Lifecycle status':lifecycle,'Provenance':provenance,
      'Validation classification':classification,'Verified scope':verified,'Not-verified scope':notverified,'Not-applicable scope':na,
      'Authority':authority,'Authority targets':decisions,'Validation method':method,'Validation evidence':evidence,'Known limitation':limitation,
      'Packet or tracking destination':packet_lookup(rid,source,block,lifecycle),'Pending dependencies':dependency,
      'Dependency classification':depclass,'Related decision':decisions,'Notes or exclusions':'Authoritative Markdown extraction; whitespace normalized only.'})

if len(rows)!=317: raise SystemExit(f'expected 317 records, found {len(rows)}')
with OUT.open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=list(rows[0]),lineterminator='\n'); writer.writeheader(); writer.writerows(rows)
print(f'Wrote {len(rows)} authoritative rows to {OUT.relative_to(REPO)}')
