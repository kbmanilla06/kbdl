#!/usr/bin/env python3
"""Independently validate the R4 ledger against Markdown and Git history."""
from pathlib import Path
from collections import Counter
import csv, hashlib, re, subprocess, sys

REPO=Path(__file__).resolve().parents[5]; DOC=REPO/'docs/kbdl'; EVD=DOC/'evidence/kbdl-011-r4/artifacts'; EVD.mkdir(parents=True,exist_ok=True)
BASE='d7108bd18e329aef2f79e7b38e992fb777b6500f'
SOURCES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']
BEGIN=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
STOP=r'(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status)?|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Validation\s+method(?:/evidence)?|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependenc(?:y|ies))\s*:|\n\s*- (?:Related|Applicable)[^:]*:|\Z)'
def norm(v):
    v=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',v).replace('`','').replace('**','')
    v=' '.join(v.split()).strip(); v=re.sub(r'\s+-\s*$','',v)
    return v.rstrip('.')
def take(block,names):
    for name in names:
        flexible=name.replace(' ',r'\s+')
        m=re.search(r'(?is)\b'+flexible+r'\s*:\s*(.*?)'+STOP,block)
        if m:return norm(m.group(1))
    return ''
def source_records(texts):
    result={}
    for source,text in texts.items():
        starts=list(BEGIN.finditer(text))
        for i,m in enumerate(starts):
            end=starts[i+1].start() if i+1<len(starts) else len(text); heading=re.search(r'(?m)^## ',text[m.end():end])
            if heading:end=m.end()+heading.start()
            result.setdefault(m.group(1),(source,text[m.start():end]))
    return result
texts={x:(DOC/x).read_text() for x in SOURCES}; records=source_records(texts)
gov=(DOC/'governance.md').read_text()
for n in range(1,4):records[f'KBDL-GOV-{n:03d}']=('governance.md',gov)
ledger=list(csv.DictReader(open(DOC/'traceability-metadata.csv'))); by={x['Requirement ID']:x for x in ledger}; counts=Counter(x['Requirement ID'] for x in ledger)
missing=sorted(set(records)-set(by)); duplicate=sorted(x for x,n in counts.items() if n!=1); orphan=sorted(set(by)-set(records))
prov_bad=[]; truncated=[]; mixed_bad=[]; authority_bad=[]; missing_targets=[]; circular=[]; generic=[]; packet_bad=[]; dependency_bad=[]; location_bad=[]; comparison=[]; scope_rows=[]; authority_rows=[]; packet_rows=[]
decision_text=(DOC/'decision-register.md').read_text(); approved_decisions=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',decision_text))
for rid,(source,block) in sorted(records.items()):
    row=by.get(rid,{})
    if rid.startswith('KBDL-GOV-'):
        expected_prov='Historical KBDL-001 prompt and approved decision record'; expected_life='Approved'; expected_auth='Approved KBDL-001 prompt and KBDL-DEC-001/KBDL-DEC-002'; validation='Verified' if rid.endswith(('001','002')) else 'Not verified'
    else:
        expected_prov=take(block,['Provenance']); rawlife=take(block,['Lifecycle status','Lifecycle']); expected_life=rawlife.split(' — ',1)[0].split(' (',1)[0]
        expected_auth=take(block,[r'Authority(?:,\s*split by clause)?']) or 'Lifecycle authority: '+rawlife
        validation=take(block,['Validation status','Validation'])
    if row.get('Provenance')!=expected_prov:prov_bad.append(rid)
    if expected_prov and (row.get('Provenance','').endswith(' and') or len(row.get('Provenance',''))<len(expected_prov)):truncated.append(rid)
    has_v=bool(re.search(r'(?<!Not )\bVerified\b',validation,re.I)); has_nv='not verified' in validation.lower(); has_na='not applicable' in validation.lower()
    expected_class=('Mixed — '+' / '.join(x for x,yes in [('Verified',has_v),('Not verified',has_nv),('Not applicable',has_na)] if yes)) if sum((has_v,has_nv,has_na))>1 else ('Verified' if has_v else 'Not applicable' if has_na else 'Not verified')
    if row.get('Validation classification')!=expected_class or (has_v and row.get('Verified scope')!=validation) or (has_nv and row.get('Not-verified scope')!=validation):mixed_bad.append(rid)
    scope_rows.append({'Requirement ID':rid,'Authoritative validation':validation,'Expected classification':expected_class,'Ledger classification':row.get('Validation classification'),'Match':rid not in mixed_bad})
    if row.get('Authority')!=expected_auth:authority_bad.append(rid)
    targets=sorted(set(re.findall(r'KBDL-(?:DEC-\d{3}|(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)',expected_auth)))
    absent=[x for x in targets if (x.startswith('KBDL-DEC-') and x not in approved_decisions) or (not x.startswith('KBDL-DEC-') and x not in records)]
    if absent:missing_targets.append(rid)
    if targets==[rid]:circular.append(rid)
    authority_rows.append({'Requirement ID':rid,'Authority':expected_auth,'Targets':'; '.join(targets) or 'None','Missing targets':'; '.join(absent) or 'None','Circular':targets==[rid]})
    packet=row.get('Packet or tracking destination',''); dependency=row.get('Pending dependencies','')
    if re.search(r'owning module|requirement-specific|generic|fallback|to be determined|unknown',packet,re.I):generic.append(rid)
    if expected_life=='Approved':
        okpacket=packet=='None — Approved'
    else:
        matches=[]
        for ps,pt in texts.items():
            heading=''
            for line in pt.splitlines():
                if re.match(r'^#{2,5} ',line):heading=norm(line.lstrip('# '))
                if line.startswith('|') and rid in line and ('packet' in heading.lower() or 'recommended decisions' in heading.lower()):
                    cells=[norm(c) for c in line.strip('|').split('|')]
                    if re.fullmatch(r'\d+',cells[0]):matches.append((ps,cells[0]))
        okpacket=bool(matches) and all(f'item {item}' in packet for ps,item in matches if ps==source) if any(ps==source for ps,item in matches) else bool(matches) and all(f'item {item}' in packet for ps,item in matches)
        explicit=take(block,['Decision-packet destination','Packet destination'])
        if explicit:okpacket=packet==explicit
    if not okpacket:packet_bad.append(rid)
    expected_dep=take(block,['Pending dependencies','Pending dependency']) or 'None'
    if dependency!=expected_dep:dependency_bad.append(rid)
    loc=row.get('Specification location',''); location_ok=bool(loc) and (DOC/source).exists()
    if not location_ok:location_bad.append(rid)
    packet_rows.append({'Requirement ID':rid,'Lifecycle':expected_life,'Packet/tracking destination':packet,'Pending dependencies':dependency,'Packet match':okpacket,'Dependency match':dependency==expected_dep})
    comparison.append({'Requirement ID':rid,'Source file':source,'Lifecycle match':row.get('Lifecycle status')==expected_life,'Provenance match':rid not in prov_bad,'Validation-scope match':rid not in mixed_bad,'Authority match':rid not in authority_bad,'Packet match':rid not in packet_bad,'Dependency match':rid not in dependency_bad,'Location match':location_ok})

def write(name,rows,fields=None):
    with (EVD/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
write('authoritative-comparison.csv',comparison);write('provenance-mismatches.csv',[{'Requirement ID':x,'Expected':take(records[x][1],['Provenance']),'Actual':by[x]['Provenance']} for x in prov_bad],['Requirement ID','Expected','Actual']);write('mixed-validation-scopes.csv',scope_rows);write('authority-resolution.csv',authority_rows);write('packet-dependency.csv',packet_rows)

# Baseline comparison is independently computed from Git, not a generated artifact.
changed={k:[] for k in ('lifecycle','provenance','authority','packet','dependency')}
for name in SOURCES+['governance.md']:
    before=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{name}'],cwd=REPO,text=True,capture_output=True,check=True).stdout
    if before!=(DOC/name).read_text():
        old=source_records({name:before}); new=source_records({name:(DOC/name).read_text()})
        for rid in set(old)&set(new):
            for key,labels in [('lifecycle',['Lifecycle status','Lifecycle']),('provenance',['Provenance']),('authority',[r'Authority(?:,\s*split by clause)?']),('packet',['Decision-packet destination','Packet destination']),('dependency',['Pending dependencies','Pending dependency'])]:
                if take(old[rid][1],labels)!=take(new[rid][1],labels):changed[key].append(rid)
baseline_rows=[{'Metadata class':k,'Changed IDs':'; '.join(v) or 'None','Unauthorized count':len(v)} for k,v in changed.items()];write('baseline-differences.csv',baseline_rows)
scripts=list((EVD.parent/'scripts').glob('*.py')); hardcoded=[]
for script in scripts:
    for n,line in enumerate(script.read_text().splitlines(),1):
        if re.search(r'print\([^)]*(?:mismatches|changes|claims|fallbacks|decisions)[^)]*:\s*0',line,re.I):hardcoded.append(f'{script.name}:{n}')
stale=[x for x in (DOC/'traceability-matrix.md').read_text().splitlines() if re.search(r'current incomplete records\s*[:`]\s*[1-9]',x,re.I)]
completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',decision_text)
incomplete=[r['Requirement ID'] for r in ledger if any(not str(v).strip() for v in r.values())]
historical_rows=list(csv.DictReader(open(DOC/'evidence/kbdl-011-r2/artifacts/traceability-audit.csv')))
historical_incomplete=sum(1 for r in historical_rows if r.get('authoritative')=='True' and any(r.get(k)!='True' for k in ('lifecycle','provenance','validation','authority','method','evidence','limitation','packet','dependency')))
errors=sum(map(len,[missing,duplicate,orphan,incomplete,prov_bad,truncated,mixed_bad,authority_bad,missing_targets,circular,generic,packet_bad,dependency_bad,location_bad,hardcoded]))+sum(len(v) for v in changed.values())
lines=[f'Requirements audited: {len(records)}',f'Ledger rows: {len(ledger)}',f'Missing rows: {len(missing)}',f'Duplicate rows: {len(duplicate)}',f'Orphan rows: {len(orphan)}','',f'Truncated provenance values: {len(truncated)}',f'Provenance mismatches: {len(prov_bad)}',f'Mixed validation-scope mismatches: {len(mixed_bad)}',f'Authority inconsistencies: {len(authority_bad)}',f'Missing authority targets: {len(missing_targets)}',f'Circular authority claims: {len(circular)}',f'Generic packet fallbacks: {len(generic)}',f'Packet-destination mismatches: {len(packet_bad)}',f'Dependency mismatches: {len(dependency_bad)}',f'Specification-location mismatches: {len(location_bad)}','',f'Unauthorized lifecycle changes: {len(changed["lifecycle"])}',f'Unauthorized provenance changes: {len(changed["provenance"])}',f'Unauthorized authority changes: {len(changed["authority"])}',f'Unauthorized packet changes: {len(changed["packet"])}',f'Unauthorized dependency changes: {len(changed["dependency"])}','',f'Historical incomplete count: {historical_incomplete}',f'Current incomplete count: {len(incomplete)}',f'Stale traceability status claims: {len(stale)}',f'Completion decisions: {len(completion)}',f'Hardcoded validation-result lines: {len(hardcoded)}','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING',f'Errors: {errors}']
print('\n'.join(lines)); (EVD/'validation-output.txt').write_text('\n'.join(lines)+'\n')
sys.exit(bool(errors))
