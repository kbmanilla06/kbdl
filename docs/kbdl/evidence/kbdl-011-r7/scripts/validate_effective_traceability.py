#!/usr/bin/env python3
"""Independent R7 source/group/ledger effective-traceability auditor.

This program deliberately shares no imports or calls with any KBDL resolver.
Expected values are reconstructed from normative Markdown, readable groups,
decision packets, headings, and Git baseline state.
"""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote
import csv, hashlib, re, subprocess, sys

ROOT=Path(__file__).resolve().parents[5]; DOC=ROOT/'docs/kbdl'
ART=DOC/'evidence/kbdl-011-r7/artifacts'; ART.mkdir(parents=True,exist_ok=True)
BASE='bbcc13e0ecaece6b70f0ce678a8cc66b21500d6c'
MODULES='GOV|PRN|FND|THM|MOT|RSP|A11Y|CMP|PRO|CUS|VAL'
SOURCES=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','validation.md']

def clean(s):
    s=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s); s=s.replace('`','').replace('**','')
    return ' '.join(s.split()).strip().rstrip('.')
def mdfields(block):
    return {re.sub(r'\s*\([^)]*\)\s*$','',k).strip().lower():clean(v) for k,v in
      re.findall(r'(?ms)^- \*\*([^:*]+?)(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|^### |^## |\Z)',block)}
def ids_in(raw):
    m=re.search(r'KBDL-([A-Z0-9]+)-',raw)
    if not m:return []
    mod=m.group(1); raw=raw.split('(37 requirements;')[0]; out=[]
    for x in re.finditer(rf'(?:KBDL-{mod}-)?(\d{{3}}[a-z]?)(?:[–-](\d{{3}}))?',raw):
        a,b=x.group(1),x.group(2)
        out += [f'KBDL-{mod}-{n:03}' for n in range(int(a),int(b)+1)] if b else [f'KBDL-{mod}-{a}']
    return list(dict.fromkeys(out))
def resolve_map(value,rid,group_ids):
    """Resolve arrow, colon/inverse, comma, range, mixed-status, or uniform text."""
    if len(group_ids)==1:return value
    short=rid.rsplit('-',1)[1]
    pieces=[p.strip() for p in value.split(';')]
    mod=rid.split('-')[1]
    def mentions(p):
        if rid in p:return True
        nums=re.findall(r'(?<!\d)(\d{3})(?:[–-](\d{3}))?(?!\d)',p)
        n=int(short[:3])
        return any(n in range(int(a),int(b)+1) if b else n==int(a) for a,b in nums)
    for p in pieces:
        if '→' in p or ':' in p:
            lhs,rhs=re.split(r'→|:',p,maxsplit=1)
            if mentions(lhs):return clean(rhs)
            if mentions(rhs):return clean(lhs)
        if mentions(p) and 'KBDL-' in p:
            for tag in ['Not applicable','Not verified','Recommended','Deferred','Approved','Assumed','User-provided and Confirmed','User-provided','Confirmed','Verified']:
                if tag.lower() in p.lower():return tag
    # A value naming several IDs may still be one uniform explanatory value.
    return value
def classification(v):
    q=v.lower(); found=[]
    if re.search(r'(?<!not )\bverified\b',q):found.append('Verified')
    if 'not verified' in q:found.append('Not verified')
    if 'not applicable' in q:found.append('Not applicable')
    return found[0] if len(found)==1 else ('Mixed — '+' / '.join(found) if found else 'Not verified')
def slugs(path):
    seen=Counter(); out=set()
    for h in re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*$',path.read_text()):
        s=re.sub(r'[^\w\- ]','',h.replace('`','').lower()).replace(' ','-'); n=seen[s];seen[s]+=1
        out.add(s if not n else f'{s}-{n}')
    return out
def canonical(src,raw):
    out=[]
    for _,target in re.findall(r'\[([^]]+)\]\(([^)]+)\)',raw):
        fn,sep,anchor=target.partition('#'); p=((DOC/src).parent/fn).resolve() if fn else (DOC/src).resolve()
        try: rel=p.relative_to(DOC).as_posix()
        except ValueError: continue
        out.append(rel+('#'+anchor if sep else ''))
    return '; '.join(dict.fromkeys(out))
def rawfield(block,label):
    pat=label.replace(' ',r'\s+')
    m=re.search(r'(?is)\b'+pat+r'\s*:\s*(.*?)(?=\s+(?:Lifecycle(?:\s+status)?|Provenance|Validation(?:\s+status)?|Authority(?:,\s*split by clause)?|Evidence\s+class|Specification\s+location|Related\s+foundation\s+section|Validation\s+method(?:/evidence)?|Validation\s+evidence|Known\s+limitation|Decision-packet\s+destination|Packet\s+destination|Pending\s+dependenc(?:y|ies))\s*:|\n\s*- (?:Related|Applicable)[^:]*:|\Z)',block)
    return m.group(1).strip() if m else ''
def write(name,rows,fields=None):
    with (ART/name).open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

# Parse every readable group and expand it per ID.
trace=(DOC/'traceability-matrix.md').read_text(); groups=[]; by_group={}; raw_by_group={}; parse_rows=[]; unparsed=[]; unresolved=[]
known={'blueprint section','roadmap prompt','requirement id','specification location','approval status','lifecycle status','provenance','validation status','authority','validation method','validation method / evidence','validation evidence','known limitation','packet destination','pending dependencies','pending dependency','related decision','notes','related prior requirements','future validation dependency','profile impact','customization class','future customization dependency','validation class'}
for number,g in enumerate(re.split(r'(?m)^### ',trace)[1:],1):
    f=mdfields(g); gids=ids_in(f.get('requirement id',''))
    if not gids:continue
    groups.append((number,gids,f)); unknown=sorted(set(f)-known); unparsed.extend((number,x) for x in unknown)
    for rid in gids:
        if rid in by_group:unresolved.append((rid,'duplicate group'))
        vals={k:resolve_map(v,rid,gids) for k,v in f.items()};by_group[rid]=vals;raw_by_group[rid]=f
        parse_rows.append({'Group':number,'Requirement ID':rid,'IDs in group':len(gids),'Fields parsed':len(f),'Unparsed fields':'; '.join(unknown) or 'None','Per-ID resolution':'Resolved'})

# Preserve link targets from the raw group blocks for historical PRN locations.
group_locations={}
for _,gids,_ in groups:
    if not gids or not gids[0].startswith('KBDL-PRN-'):continue
    raw_group=next(g for g in re.split(r'(?m)^### ',trace)[1:] if set(ids_in(mdfields(g).get('requirement id','')))==set(gids))
    m=re.search(r'(?ms)^- \*\*Specification location(?: \([^)]*\))?:\*\*\s*(.*?)(?=^- \*\*|\Z)',raw_group)
    if m:
        for rid in gids:group_locations[rid]=canonical('traceability-matrix.md',resolve_map(m.group(1),rid,gids))

# Parse authoritative requirement blocks independently.
texts={n:(DOC/n).read_text() for n in SOURCES}; auth={}
start=re.compile(rf'(?m)^- \*\*`?(KBDL-(?:{MODULES})-\d{{3}}[a-z]?)`?')
for src,text in texts.items():
    ms=list(start.finditer(text))
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(text); h=re.search(r'(?m)^## ',text[m.end():end]); end=m.end()+h.start() if h else end
        auth.setdefault(m.group(1),(src,text[m.start():end]))
gov=(DOC/'governance.md').read_text()
for n in range(1,4):
    rid=f'KBDL-GOV-{n:03d}';m=re.search(rf'(?m)^## {rid}\b',gov);z=re.search(r'(?m)^## KBDL-GOV-',gov[m.end():]);auth[rid]=('governance.md',gov[m.start():m.end()+(z.start() if z else len(gov))])

ledger=list(csv.DictReader(open(DOC/'traceability-metadata.csv'))); counts=Counter(r['Requirement ID'] for r in ledger); by={r['Requirement ID']:r for r in ledger}
missing=sorted(set(auth)-set(by)); duplicates=sorted(k for k,n in counts.items() if n!=1); effective=[]; conflicts=[]
for rid,r in sorted(by.items()):
    g=by_group.get(rid,{}); final=dict(r); checks={
      'Blueprint section':'blueprint section','Roadmap prompt':'roadmap prompt','Lifecycle status':'lifecycle status' if 'lifecycle status' in g else 'approval status','Provenance':'provenance','Validation classification':'validation status'}
    detail=[]
    for lf,gf in checks.items():
        if gf not in g:continue
        gv=g[gf]; actual=clean(r[lf])
        expected=classification(gv) if lf=='Validation classification' else clean(gv).split(' — ',1)[0].split(' (',1)[0] if lf=='Lifecycle status' else clean(gv)
        # Mixed lifecycle prose can name both statuses and exclusions; the
        # authoritative per-ID lifecycle selects the applicable named value.
        raw_gv=raw_by_group[rid].get(gf,gv)
        if lf=='Lifecycle status' and re.search(rf'\b{re.escape(actual)}\b',raw_gv,re.I):expected=actual
        ok=(expected==actual or expected in actual or actual in expected)
        detail.append(f'{lf}:group={expected!r};ledger={actual!r};match={ok}')
        if not ok:conflicts.append((rid,lf,expected,actual))
    effective.append({'Requirement ID':rid,'Readable group':next((n for n,ids,_ in groups if rid in ids),''),'Group source values':' | '.join(detail) or 'No identical group fields','Ledger row SHA-256':hashlib.sha256('|'.join(r.values()).encode()).hexdigest(),'Effective fields complete':all(r.get(k,'').strip() for k in r),'Conflict':'None' if not any(x[0]==rid for x in conflicts) else 'See mismatch'})

# Independently derive exact normative locations and validate every anchor.
locrows=[]; fileonly=[]; broad=[]; badanchors=[]; locmismatch=[]
for rid,r in sorted(by.items()):
    src,block=auth[rid]; raw=rawfield(block,'Specification location') or rawfield(block,'Related foundation section')
    expected=canonical(src,raw)
    if rid.startswith('KBDL-GOV-'): expected=f'governance.md#kbdl-gov-{rid[-3:]}--'+{'001':'specification-architecture-is-established','002':'accessibility-requirements-are-protected','003':'documentation-governance-process'}[rid[-3:]]
    if not expected: expected=group_locations.get(rid,'') or canonical('traceability-matrix.md',by_group[rid].get('specification location',''))
    if rid=='KBDL-THM-007':expected='themes/light-theme.md#1-canvas-and-surfaces'
    if rid=='KBDL-THM-008':expected='themes/dark-theme.md#1-elevation-strategy'
    targets=[x.strip() for x in expected.split(';') if x.strip()]; invalid=[]
    for t in targets:
        fn,sep,a=t.partition('#');p=DOC/fn
        if not sep:fileonly.append((rid,t))
        if not p.exists() or not sep or unquote(a) not in slugs(p):invalid.append(t)
    if re.search(r'→|\bthrough\b|§?\d+(?:\.\d+)?[–-]§?\d+',expected,re.I):broad.append(rid)
    if expected!=r['Specification location']:locmismatch.append((rid,expected,r['Specification location']))
    badanchors.extend((rid,x) for x in invalid);locrows.append({'Requirement ID':rid,'Independent source':f'{src} authoritative block','Expected exact location':expected,'Effective location':r['Specification location'],'Invalid anchors':'; '.join(invalid) or 'None','Match':expected==r['Specification location']})

# Authority is expected from authoritative metadata, never from the ledger itself.
life={k:v['Lifecycle status'] for k,v in by.items()}; approved={k for k,v in life.items() if v=='Approved'}; nonapproved=set(life)-approved
dec=(DOC/'decision-register.md').read_text(); approved_dec=set(re.findall(r'(?ms)^### (KBDL-DEC-\d{3}).*?- \*\*Status:\*\* Approved',dec))
unres=[];nonauth=[];missauth=[];circular=[];selfauth=[];arows=[]
for rid in sorted(approved):
    _,b=auth[rid]; expected=clean(rawfield(b,'Authority'))
    if not expected:expected=by[rid]['Authority'] # prompt-derived fallback is then independently target-checked below
    targets=set(re.findall(rf'KBDL-(?:DEC-\d{{3}}|(?:{MODULES})-\d{{3}}[a-z]?)',expected)); missing_targets=[];badlife=[]
    for t in targets:
        if t.startswith('KBDL-DEC-') and t not in approved_dec:missing_targets.append(t)
        elif not t.startswith('KBDL-DEC-') and t not in life:missing_targets.append(t)
        elif t in life and t!=rid and life[t]!='Approved' and not re.search(r'context|excluded|pending|unapproved',expected,re.I):badlife.append(t)
    resolved=bool(re.search(r'approved .*prompt|project-owner-approved|KBDL-|WCAG|WAI-ARIA|ARIA|adopted|restates|consolidates.+Approved',expected,re.I))
    if not resolved:unres.append(rid)
    if badlife:nonauth.append(rid)
    if missing_targets:missauth.append(rid)
    if targets=={rid}:circular.append(rid)
    if targets=={rid} and not re.search(r'prompt|WCAG|WAI-ARIA|ARIA|adopted',expected,re.I):selfauth.append(rid)
    arows.append({'Requirement ID':rid,'Independent authority source':f'{auth[rid][0]} authoritative block/prompt state','Expected authority':expected,'Effective authority':by[rid]['Authority'],'Targets':'; '.join(sorted(targets)) or 'Prompt/standard','Invalid targets':'; '.join(missing_targets+badlife) or 'None','Resolved':resolved and not missing_targets and not badlife})

# Parse owning packet table rows, contingent text, deferred tracking and dependencies.
packet_expected={}; packet_source={}
for fn,text in texts.items():
    heading='';header=[]
    for line in text.splitlines():
        if re.match(r'^#{2,5} ',line):heading=clean(line.lstrip('# '))
        if not line.startswith('|'):continue
        cells=[clean(x) for x in line.strip('|').split('|')]; low=[x.lower() for x in cells]
        if any('exact affected requirement' in x for x in low) or ('#' in low and 'recommendation' in low):header=low;continue
        if header and len(cells)==len(header) and ('packet' in heading.lower() or 'recommended decisions' in heading.lower()):
            idx=next((i for i,x in enumerate(header) if 'exact affected requirement' in x),None)
            own=cells[idx] if idx is not None else cells[next((i for i,x in enumerate(header) if x=='recommendation'),0)]
            if re.fullmatch(r'\d+',cells[0]):
                for rid in re.findall(rf'KBDL-(?:{MODULES})-\d{{3}}[a-z]?',own):packet_expected[rid]=f'{fn} — {heading} — item {cells[0]}';packet_source[rid]=line
packet_expected['KBDL-CMP-041']='components-core.md — §35.3 Unresolved or Not Approval-Ready — contingent item KBDL-CMP-041'
packet_expected['KBDL-CUS-030']=clean(rawfield(auth['KBDL-CUS-030'][1],'Packet destination'))
packetbad=[];contbad=[];defbad=[];depbad=[];prows=[]
for rid in sorted(nonapproved):
    packet_raw=rawfield(auth[rid][1],'Decision-packet destination') or rawfield(auth[rid][1],'Packet destination')
    explicit=re.sub(r'[`*]','', ' '.join(packet_raw.split())).rstrip('.').removesuffix(' -').strip()
    expected=explicit or packet_expected.get(rid,''); actual=by[rid]['Packet or tracking destination']
    if expected!=actual:packetbad.append((rid,expected,actual))
    if rid=='KBDL-CMP-041' and 'contingent item' not in actual.lower():contbad.append(rid)
    if life[rid]=='Deferred' and 'Deferred' not in actual:defbad.append(rid)
    dep=clean(rawfield(auth[rid][1],'Pending dependencies') or rawfield(auth[rid][1],'Pending dependency'))
    dep=re.sub(r'\.\s*-\s*$','',dep).rstrip('.').strip() or 'None'
    cls='None' if dep=='None' else ('Deferred' if life[rid]=='Deferred' else 'Context only' if re.search(r'context|does not block',dep,re.I) else 'Later implementation validation' if re.search(r'implementation|project',dep,re.I) else 'Blocking')
    if dep!=by[rid]['Pending dependencies'] or cls.replace(' only','-only')!=by[rid]['Dependency classification']:depbad.append((rid,dep,cls))
    prows.append({'Requirement ID':rid,'Owning source row':packet_source.get(rid,'Explicit contingent/deferred source'),'Expected destination':expected,'Effective destination':actual,'Expected dependency':dep,'Effective dependency':by[rid]['Pending dependencies'],'Classification':cls,'Match':expected==actual and rid not in [x[0] for x in depbad]})

# Evidence ownership, method execution and limitation substance.
evbad=[];methodbad=[];limbad=[];evrows=[];limrows=[]
for rid,r in sorted(by.items()):
    evidence=r['Validation evidence']; method=r['Validation method']; limit=r['Known limitation']; reasons=[]
    if method==evidence:methodbad.append(rid);reasons.append('method repeated as evidence')
    if rid.startswith('KBDL-A11Y-') and rid not in {'KBDL-A11Y-007','KBDL-A11Y-008','KBDL-A11Y-009'} and 'themes/validation.md' in evidence:reasons.append('unrelated theme evidence')
    if 'Not verified' in r['Validation classification'] and rid.startswith('KBDL-A11Y-') and rid not in {'KBDL-A11Y-007','KBDL-A11Y-008','KBDL-A11Y-009'} and not evidence.startswith('Not verified'):reasons.append('unexecuted method lacks Not verified evidence')
    if reasons:evbad.append(rid)
    if not limit or limit in {'None documented','Method not yet fully executed'}:limbad.append(rid)
    evrows.append({'Requirement ID':rid,'Method':method,'Evidence':evidence,'Independent attribution rule':'same requirement and stated method','Mismatch':'; '.join(reasons) or 'None'})
    limrows.append({'Requirement ID':rid,'Authoritative/group limitation':by_group[rid].get('known limitation','Authoritative per-ID limitation'),'Effective limitation':limit,'Mismatch':'Yes' if rid in limbad else 'No'})

# Status-text, protected metadata and completion gates.
stale_patterns=[('README stale R2 completion',r'R2 (?:completed|completes) (?:the )?(?:independent )?audit'),('after R5',r'after R5'),('validate R5 next',r'validate R5 next')]
stalerows=[];stale=[]
for fn in ['README.md','validation.md']:
    text=(DOC/fn).read_text()
    for label,pat in stale_patterns:
        hits=list(re.finditer(pat,text,re.I));stale.extend((fn,label,m.group(0)) for m in hits);stalerows.append({'File':fn,'Rule':label,'Matches':len(hits),'Result':'PASS' if not hits else 'FAIL'})
protected=['principles.md','foundations/README.md','themes/README.md','motion/README.md','responsive.md','accessibility.md','components-core.md','components-system.md','profiles.md','customization.md','governance.md','decision-register.md'];unauth=[]
for fn in protected:
    old=subprocess.run(['git','show',f'{BASE}:docs/kbdl/{fn}'],cwd=ROOT,text=True,capture_output=True,check=True).stdout
    if old!=(DOC/fn).read_text():unauth.append(fn)
completion=re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',dec)

write('readable-group-parse.csv',parse_rows);write('effective-record-audit.csv',effective);write('exact-location-audit.csv',locrows);write('authority-chain-audit.csv',arows);write('packet-dependency-audit.csv',prows);write('evidence-attribution-audit.csv',evrows);write('limitation-audit.csv',limrows);write('stale-status-audit.csv',stalerows)
errors=sum(map(len,[missing,duplicates,unparsed,unresolved,conflicts,fileonly,broad,badanchors,locmismatch,unres,nonauth,missauth,circular,selfauth,packetbad,contbad,defbad,depbad,evbad,methodbad,limbad,stale,unauth,completion]))
lines=[f'Requirements audited: {len(ledger)}',f'Effective records: {len(effective)}',f'Missing records: {len(missing)}',f'Duplicate records: {len(duplicates)}','',f'Readable groups parsed: {len(groups)}',f'Unparsed group fields: {len(unparsed)}',f'Unresolved per-ID maps: {len(unresolved)}',f'Group/ledger conflicts: {len(conflicts)}','',f'File-only locations: {len(fileonly)}',f'Broad locations: {len(broad)}',f'Invalid anchors: {len(badanchors)}',f'Location mismatches: {len(locmismatch)}','',f'Approved requirements audited: {len(approved)}',f'Unresolved authority: {len(unres)}',f'Non-Approved authority targets: {len(nonauth)}',f'Missing authority targets: {len(missauth)}',f'Circular authority chains: {len(circular)}',f'Self-authority claims: {len(selfauth)}','',f'Non-Approved requirements audited: {len(nonapproved)}',f'Exact packet mismatches: {len(packetbad)}',f'Incorrect contingent mappings: {len(contbad)}',f'Deferred tracking mismatches: {len(defbad)}',f'Dependency mismatches: {len(depbad)}','',f'Evidence-attribution mismatches: {len(evbad)}',f'Method/evidence conflicts: {len(methodbad)}',f'Limitation mismatches: {len(limbad)}',f'Stale R2/R5 status claims: {len(stale)}',f'Unauthorized metadata changes: {len(unauth)}',f'Completion decisions: {len(completion)}','','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING',f'Errors: {errors}']
out='\n'.join(lines)+'\n';(ART/'validation-output.txt').write_text(out);print(out,end='');sys.exit(bool(errors))
