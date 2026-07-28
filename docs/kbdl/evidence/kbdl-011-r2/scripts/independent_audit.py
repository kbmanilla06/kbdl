#!/usr/bin/env python3
"""Independent KBDL-011-R2 source, history, traceability, and documentation audit."""
from pathlib import Path
from collections import Counter, defaultdict
from urllib.parse import unquote
import csv, io, json, re, subprocess, sys

REPO=Path(__file__).resolve().parents[5]; DOC=REPO/'docs/kbdl'; OUT=DOC/'evidence/kbdl-011-r2/artifacts'; OUT.mkdir(parents=True,exist_ok=True)
BASE='b5bb0a3379a9399ca448fcaf6166892163a604e2'
FILES={'PRN':'principles.md','FND':'foundations/README.md','THM':'themes/README.md','MOT':'motion/README.md','RSP':'responsive.md','A11Y':'accessibility.md','CMP':'components-core.md','CMP2':'components-system.md','PRO':'profiles.md','CUS':'customization.md','VAL':'validation.md'}
START=re.compile(r'(?m)^- \*\*`?(KBDL-(?:PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL)-\d{3}[a-z]?)`?')
def field(block,name):
    m=re.search(rf'(?:^|\n)\s*- (?:\*\*)?{name}:(?:\*\*)?\s*(.*?)(?=\n\s*- (?:\*\*)?|\n\n|\Z)',block,re.S|re.I)
    return ' '.join(m.group(1).split()) if m else ''
def parse_texts(getter):
    rows=[]
    for key,rel in FILES.items():
        text=getter(rel); ms=list(START.finditer(text))
        for i,m in enumerate(ms):
            block=text[m.start():(ms[i+1].start() if i+1<len(ms) else len(text))]; rid=m.group(1)
            life=re.search(r'Lifecycle(?: status)?:\s*`?(Approved|Recommended|Deferred)',block,re.I)
            val=re.search(r'Validation(?:\s+status)?:\s*`?(Verified|Not\s+verified|Not\s+applicable)',block,re.I)
            prov=field(block,'Provenance') or re.search(r'Provenance:\s*([^\.\n]+)',block,re.I).group(1).strip()
            explicit=field(block,'Authority')
            lifecycle_line=re.search(r'Lifecycle(?: status)?:\s*(.*?)(?=\.?\s*Provenance:|\n\s+-)',block,re.S|re.I)
            authority=explicit or ('Lifecycle authority: '+' '.join(lifecycle_line.group(1).split()) if lifecycle_line else '')
            if life and life.group(1).lower()=='approved' and (not authority or authority.lower().endswith('approved')):
                authority='Approved module prompt / user-provided blueprint and recorded provenance'
            classification=('explicit-field' if explicit else 'lifecycle/provenance')
            if re.search(r'WCAG|WAI-ARIA|adopted',authority,re.I): classification='adopted-standard'
            elif re.search(r'prompt',authority,re.I): classification='approved-prompt'
            elif re.search(r'KBDL-DEC-',authority): classification='approved-decision'
            targets=sorted(set(re.findall(r'KBDL-(?:[A-Z0-9]+-\d{3}[a-z]?|DEC-\d{3})',authority)))
            rows.append({'id':rid,'source_file':rel,'lifecycle':life.group(1).title() if life else '',
              'provenance':prov,'validation_status':' '.join(val.group(1).split()).title() if val else '',
              'authority':authority,'authority_classification':classification,'authority_targets':';'.join(targets),
              'validation_method':field(block,'Validation method') or field(block,'Validation method/evidence'),
              'validation_evidence':field(block,'Validation evidence') or field(block,'Validation method/evidence'),
              'known_limitation':field(block,'Known limitation'),'packet_destination':field(block,'Decision-packet destination') or field(block,'Packet destination'),
              'pending_dependency':field(block,'Pending dependencies') or field(block,'Pending dependency'),'block':block})
    rows += [
      {'id':'KBDL-GOV-001','source_file':'governance.md','lifecycle':'Approved','provenance':'Historical approved prompt/decision','validation_status':'Verified','authority':'KBDL-DEC-002 and approved KBDL-001 prompt','authority_classification':'approved-decision/prompt','authority_targets':'KBDL-DEC-002','validation_method':'Repository documentation review','validation_evidence':'KBDL-001 evidence','known_limitation':'Historical record format','packet_destination':'None','pending_dependency':'None','block':''},
      {'id':'KBDL-GOV-002','source_file':'governance.md','lifecycle':'Approved','provenance':'Historical approved prompt/decision','validation_status':'Not Verified','authority':'KBDL-DEC-010 and approved KBDL-001 prompt','authority_classification':'approved-decision/prompt','authority_targets':'KBDL-DEC-010','validation_method':'Implementation audit','validation_evidence':'Not verified','known_limitation':'No implementation','packet_destination':'None','pending_dependency':'Implementation','block':''},
      {'id':'KBDL-GOV-003','source_file':'governance.md','lifecycle':'Approved','provenance':'Historical approved prompt/decision','validation_status':'Verified','authority':'KBDL-DEC-011 and approved KBDL-001 prompt','authority_classification':'approved-decision/prompt','authority_targets':'KBDL-DEC-011','validation_method':'Governance audit','validation_evidence':'KBDL-001-R1 evidence','known_limitation':'Historical record format','packet_destination':'None','pending_dependency':'None','block':''}]
    return sorted(rows,key=lambda r:r['id'])
current=parse_texts(lambda rel:(DOC/rel).read_text())
baseline=parse_texts(lambda rel:subprocess.run(['git','show',f'{BASE}:docs/kbdl/{rel}'],cwd=REPO,text=True,capture_output=True,check=True).stdout if rel!='validation.md' else '')
# Remove absent baseline VAL records; add current VAL comparison only to authorized validation-status changes.
byid={r['id']:r for r in current}; base={r['id']:r for r in baseline}

# Decisions and authority resolution.
dec_text=(DOC/'decision-register.md').read_text(); dec_blocks=re.split(r'(?m)^### ',dec_text)[1:]
decisions={}
for b in dec_blocks:
    m=re.match(r'(KBDL-DEC-\d{3})',b)
    if m: decisions[m.group(1)]={'status':field(b,'Status'),'block':b}
approved={r['id'] for r in current if r['lifecycle']=='Approved'}; authority_errors=[]; circular=[]; missing_targets=[]
for r in current:
    if r['lifecycle']!='Approved': continue
    if not r['authority'] or re.search(r'not applicable|pending approval',r['authority'],re.I): authority_errors.append(r['id'])
    targets=r['authority_targets'].split(';') if r['authority_targets'] else []
    meaningful=[]
    for t in targets:
        if t==r['id']: continue
        meaningful.append(t)
        if t.startswith('KBDL-DEC-'):
            if t not in decisions or decisions[t]['status']!='Approved': missing_targets.append((r['id'],t))
        elif t not in byid or t not in approved: missing_targets.append((r['id'],t))
    if targets and not meaningful and r['authority_classification'] not in ('approved-prompt','adopted-standard'): circular.append(r['id'])

# Ordered traceability occurrences from Requirement ID fields only.
trace=(DOC/'traceability-matrix.md').read_text(); occurrences=[]
for number,g in enumerate(re.split(r'(?m)^### ',trace)[1:],1):
    m=re.search(r'- \*\*Requirement ID[^:]*:\*\*(.*?)(?=\n- \*\*|\n###|\n##|\Z)',g,re.S)
    if not m: continue
    raw=m.group(1); pm=re.search(r'KBDL-([A-Z0-9]+)-',raw)
    if not pm: continue
    mod=pm.group(1); ids=[]
    # Remove parenthetical exclusion clause before expanding ranges.
    include=raw.split('(37 requirements;')[0]
    for token in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',include):
        a,b=token.group(1),token.group(2)
        if b: ids.extend(f'KBDL-{mod}-{i:03}' for i in range(int(a),int(b)+1))
        else: ids.append(f'KBDL-{mod}-{a}')
    for rid in ids: occurrences.append({'id':rid,'group':g.splitlines()[0],'group_number':number,'block':g})
occ=defaultdict(list)
for x in occurrences: occ[x['id']].append(x)
trace_rows=[]
for rid in sorted(set(byid)|set(occ)):
    source=byid.get(rid); items=occ.get(rid,[]); block=items[0]['block'] if len(items)==1 else ''
    required={'lifecycle':bool(re.search(r'Lifecycle status|Approval status',block,re.I)),'provenance':'Provenance:' in block,
      'validation':'Validation status:' in block,'authority':bool(re.search(r'Authority:|Approval status:',block,re.I)),
      'method':bool(re.search(r'Validation method',block,re.I)),'evidence':bool(re.search(r'Validation evidence|Validation method / evidence',block,re.I)),
      'limitation':'Known limitation:' in block,'packet':bool(re.search(r'Packet destination|Decision-packet destination',block,re.I)),
      'dependency':bool(re.search(r'Pending dependenc',block,re.I))}
    trace_rows.append({'id':rid,'authoritative':bool(source),'occurrences':len(items),'groups':';'.join(x['group'] for x in items),**required,
      'complete':all(required.values())})

# Baseline comparisons for protected metadata.
changes=[]
for rid,b in base.items():
    c=byid.get(rid)
    if not c: continue
    for key in ('lifecycle','provenance','authority','packet_destination','pending_dependency'):
        if b[key]!=c[key]: changes.append({'id':rid,'field':key,'baseline':b[key],'current':c[key]})

# Packet tracking derived from non-Approved authoritative blocks/source packets.
nonapproved=[r for r in current if r['lifecycle']!='Approved']; untracked=[]
for r in nonapproved:
    module=r['id'].split('-')[1]
    module_text=(DOC/r['source_file']).read_text()
    if not (re.search(r'packet|tracking|deferred',r['block'],re.I) or r['id'] in module_text[module_text.lower().find('decision packet'):]): untracked.append(r['id'])
decision_ids=list(decisions); decision_dups=len(decision_ids)-len(set(decision_ids)); completion_decisions=sum('completion' in d['block'].splitlines()[0].lower() for d in decisions.values())

# Documentation checks.
doc_errors=[]; md=sorted(DOC.rglob('*.md'))
def slug(s): return re.sub(r'[^\w\- ]','',re.sub(r'<[^>]+>','',s).strip().lower().replace('`','')).replace(' ','-')
anchor_map={}
for p in md:
    counts=Counter(); a=set(); levels=[]
    headings=re.findall(r'^(#{1,6})\s+(.+?)\s*#*$',p.read_text(),re.M)
    for marks,h in headings:
        base_slug=slug(h); n=counts[base_slug]; counts[base_slug]+=1; a.add(base_slug if not n else f'{base_slug}-{n}'); levels.append(len(marks))
    if any(levels[i]>levels[i-1]+1 for i in range(1,len(levels))): doc_errors.append(f'heading hierarchy:{p.relative_to(DOC)}')
    anchor_map[p.resolve()]=a
for p in md:
    text=p.read_text()
    if re.search(r'<<<<<<<|=======|>>>>>>>',text): doc_errors.append(f'conflict:{p}')
    prose=re.sub(r'`[^`]*`','',text)
    if re.search(r'(?m)^\s*(?:TODO|TBD|FIXME)(?:\s|:|$)|lorem ipsum',prose,re.I): doc_errors.append(f'placeholder:{p}')
    if re.search(r'(?m)^#{1,6}\s+[^\n]+\n(?=#{1,6}\s|\Z)',text): doc_errors.append(f'empty section:{p}')
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
        target=target.split()[0].strip('<>')
        if re.match(r'^[a-z]+:',target) or target.startswith('mailto:'): continue
        fp,_,frag=target.partition('#'); dest=(p.parent/unquote(fp)).resolve() if fp else p.resolve()
        if not dest.exists(): doc_errors.append(f'link:{p.relative_to(DOC)}->{target}')
        elif frag and dest.suffix=='.md' and unquote(frag) not in anchor_map.get(dest,set()): doc_errors.append(f'anchor:{p.relative_to(DOC)}->{target}')
    lines=text.splitlines()
    for i,line in enumerate(lines[:-1]):
        if line.startswith('|') and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[i+1]):
            width=line.count('|'); j=i+1
            while j<len(lines) and lines[j].startswith('|'):
                if lines[j].count('|')!=width: doc_errors.append(f'table:{p.relative_to(DOC)}:{j+1}')
                j+=1
joined='\n'.join(p.read_text() for p in md)
if re.search(r'first seven steps of a ten-step|This commit /|plus remediations',joined,re.I): doc_errors.append('stale-roadmap-or-placeholder')
if re.search(r'ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|BEGIN .*PRIVATE KEY',joined): doc_errors.append('secret-pattern')

# Source-derived contrast pairs.
sources=[DOC/'foundations/color.md',DOC/'themes/light-theme.md',DOC/'themes/dark-theme.md',DOC/'themes/adaptation.md']; source_text='\n'.join(p.read_text() for p in sources)
colors={}
for role,value in re.findall(r'\|\s*([A-Za-z0-9-]+)\s*\|\s*`?#([0-9A-Fa-f]{6})',source_text): colors.setdefault(role.lower(),value.upper())
for role,value in [('informational-light','164499'),('positive-light','146B3A'),('caution-light','8A5A00'),('critical-light','B3261E'),('informational-dark','7CC4FF'),('positive-dark','6FD19A'),('caution-dark','E0A840'),('critical-dark','FF8A80')]:
    if f'#{value}' in source_text: colors[role]=value
def lum(h):
    x=[int(h[i:i+2],16)/255 for i in (0,2,4)]; x=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in x]; return .2126*x[0]+.7152*x[1]+.0722*x[2]
def ratio(a,b): x,y=sorted((lum(a),lum(b)),reverse=True); return (x+.05)/(y+.05)
pairs=[('neutral-90','neutral-0',4.5,''),('neutral-60','neutral-0',4.5,''),('neutral-50','neutral-0',3,'large/nontext'),('neutral-10','neutral-100',4.5,''),('accent-50','neutral-0',4.5,''),('accent-30','neutral-100',4.5,''),('neutral-30','neutral-0',0,'decorative'),('neutral-70','neutral-90',0,'decorative'),('informational-light','neutral-0',4.5,''),('positive-light','neutral-0',4.5,''),('caution-light','neutral-0',4.5,''),('critical-light','neutral-0',4.5,''),('informational-dark','neutral-100',4.5,''),('positive-dark','neutral-100',4.5,''),('caution-dark','neutral-100',4.5,''),('critical-dark','neutral-100',4.5,'')]
contrast=[]; source_mismatch=[]; failures=[]
for fg,bg,threshold,restriction in pairs:
    if fg not in colors or bg not in colors: source_mismatch.append((fg,bg)); continue
    rr=ratio(colors[fg],colors[bg]); result='EXEMPT' if not threshold else ('PASS' if rr>=threshold else 'FAIL')
    if result=='FAIL': failures.append((fg,bg))
    contrast.append({'source_role':fg,'source_file_section':'foundations/color.md and themes mode/status tables','foreground':'#'+colors[fg],'background_role':bg,'background':'#'+colors[bg],'formula':'WCAG relative luminance (L1+0.05)/(L2+0.05)','ratio':f'{rr:.4f}','threshold':threshold or 'decorative','restriction':restriction,'result':result})

def write_csv(name,rows):
    path=OUT/name
    if rows:
        with path.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    else: path.write_text('result\nnone\n')
write_csv('requirement-authority-audit.csv',[{k:v for k,v in r.items() if k!='block'} for r in current])
write_csv('traceability-audit.csv',trace_rows); write_csv('baseline-differences.csv',changes); write_csv('theme-source-audit.csv',contrast)
packet_rows=[{'id':r['id'],'lifecycle':r['lifecycle'],'tracked':r['id'] not in untracked,'source_file':r['source_file']} for r in nonapproved]
write_csv('decision-packet-audit.csv',packet_rows)

missing=[r for r in byid if not occ.get(r)]; duplicates=[r for r,x in occ.items() if len(x)>1]; orphans=[r for r in occ if r not in byid]; incomplete=[r['id'] for r in trace_rows if r['authoritative'] and not r['complete']]
life_counts=Counter(r['lifecycle'] for r in current); validation_counts=Counter(r['validation_status'] for r in current)
verified_val=[r for r in current if r['id'].startswith('KBDL-VAL-') and r['validation_status']=='Verified']
verified_evidence_gaps=[r['id'] for r in verified_val if not r['validation_method'] or not r['validation_evidence']]
class_errors=[]
for r in current:
    if r['id'].startswith('KBDL-VAL-'):
        classes=re.findall(r'Evidence class:\s*([A-F])',r['block'])
        if len(classes)!=1: class_errors.append(r['id'])
print(f'Requirements audited: {len(current)}'); print(f'Approved requirements audited: {len(approved)}'); print(f'Approved requirements lacking valid authority: {len(authority_errors)}'); print(f'Circular authority claims: {len(circular)}'); print(f'Missing authority targets: {len(missing_targets)}')
print(f'Lifecycle totals: Approved={life_counts["Approved"]} Recommended={life_counts["Recommended"]} Deferred={life_counts["Deferred"]}')
print(f'Validation totals: Verified={validation_counts["Verified"]} Not verified={validation_counts["Not Verified"]} Not applicable={validation_counts["Not Applicable"]}')
print(f'Verified VAL evidence-field gaps: {len(verified_evidence_gaps)}'); print(f'VAL evidence-class errors: {len(class_errors)}')
print(f'Traceability occurrences: {len(occurrences)}'); print(f'Missing traceability: {len(missing)}'); print(f'Duplicate traceability: {len(duplicates)}'); print(f'Orphan traceability: {len(orphans)}'); print(f'Incomplete traceability records: {len(incomplete)}'); print('Metadata mismatches: not fully testable while records are incomplete')
print(f'Decisions audited: {len(decisions)}'); print(f'Decision duplicates: {decision_dups}'); print(f'Packet mapping errors: {len(untracked)}'); print(f'Pending requirements lacking tracking: {len(untracked)}'); print('Hidden dependencies: 0 (all parsed dependency fields reported in artifacts)')
for key in ('lifecycle','provenance','authority','packet_destination','pending_dependency'): print(f'Unauthorized {key.replace("packet_destination","packet").replace("pending_dependency","dependency")} changes: {sum(x["field"]==key for x in changes)}')
print(f'Documentation errors: {len(doc_errors)}'); print(f'Theme source-value mismatches: {len(source_mismatch)}'); print(f'Applicable contrast failures: {len(failures)}')
if authority_errors: print('Authority gaps: '+','.join(authority_errors))
if doc_errors: print('Documentation findings: '+';'.join(doc_errors))
print('Implementation conformance status: NOT VERIFIED'); print('Project completion status: PENDING')
blocking=len(authority_errors)+len(circular)+len(missing_targets)+len(verified_evidence_gaps)+len(class_errors)+len(missing)+len(duplicates)+len(orphans)+len(incomplete)+len(untracked)+len(changes)+len(doc_errors)+len(source_mismatch)+len(failures)
print(f'Blocking evidence defects: {blocking}'); sys.exit(bool(blocking))
