#!/usr/bin/env python3
"""Run real R16 source mutations against the production validator in isolated copies."""
from pathlib import Path
import csv,json,re,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[5];PK=ROOT/'docs/kbdl/evidence/kbdl-011-r16';OUT=PK/'negative-tests';OUT.mkdir(parents=True,exist_ok=True)
CASES={
'ledger-normative-lifecycle':'SOURCE_PRECEDENCE_CONFLICT','ledger-approved-decision':'DECISION_FIELD_MISMATCH','missing-administrative-field':'MISSING_ADMIN_FIELD','missing-derivation-rule':'MISSING_SOURCE_RULE','wrong-blueprint':'BLUEPRINT_MISMATCH','wrong-roadmap':'ROADMAP_MISMATCH','wrong-anchor':'LOCATION_MISMATCH','wrong-packet':'PACKET_MISMATCH','wrong-dependency':'DEPENDENCY_MISMATCH','lifecycle-only-authority':'LIFECYCLE_ONLY_AUTHORITY','missing-standard-basis':'MISSING_STANDARD_BASIS','nonapproved-authority-target':'NONAPPROVED_AUTHORITY_TARGET','multi-node-cycle':'CIRCULAR_AUTHORITY','self-authority':'SELF_AUTHORITY','ar2-scope-exclusion':'AR2_SCOPE','historical-falsely-recovered':'HISTORICAL_RECOVERY','explicit-group-conflict':'GROUP_LEDGER_CONFLICT','misparsed-status-bucket':'STATUS_BUCKET_MISMATCH','valid-wrong-anchor':'LOCATION_MISMATCH','wrong-packet-item':'PACKET_ITEM_MISMATCH','wrong-dependency-class':'DEPENDENCY_CLASS_MISMATCH','nonexistent-evidence-sha':'MISSING_GIT_EVIDENCE_OBJECT','unrelated-evidence-artifact':'EVIDENCE_SCOPE_RELATIONSHIP','unrelated-limitation':'LIMITATION_MISMATCH','wrong-standard-clause':'STANDARD_CLAUSE_MISMATCH','implicit-verb-cycle':'CIRCULAR_AUTHORITY'}
def rewrite_csv(path,fn):
 rows=list(csv.DictReader(open(path)));fields=list(rows[0]);fn(rows)
 with open(path,'w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
def row(rows,rid):return next(x for x in rows if x.get('Requirement ID')==rid)
def mutate(root,case):
 d=root/'docs/kbdl';meta=d/'traceability-metadata.csv';rules=d/'evidence/kbdl-011-r16/source-rules.csv';rec=d/'evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv'
 if case=='ledger-normative-lifecycle':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Lifecycle status':'Recommended'}))
 elif case=='ledger-approved-decision':rewrite_csv(meta,lambda rs:row(rs,'KBDL-MOT-007').update({'Related decision':'KBDL-DEC-999'}))
 elif case=='missing-administrative-field':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Blueprint section':''}))
 elif case=='missing-derivation-rule':rewrite_csv(rules,lambda rs:next(x for x in rs if x['Field name']=='Blueprint section').update({'Derivation rule':''}))
 elif case=='wrong-blueprint':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Blueprint section':'WRONG BLUEPRINT'}))
 elif case=='wrong-roadmap':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Roadmap prompt':'KBDL-999'}))
 elif case=='wrong-anchor':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Specification location':'validation.md#does-not-exist'}))
 elif case=='wrong-packet':rewrite_csv(meta,lambda rs:row(rs,'KBDL-RSP-002').update({'Packet or tracking destination':'missing-packet.md — item 999'}))
 elif case=='wrong-dependency':rewrite_csv(meta,lambda rs:row(rs,'KBDL-PRO-016').update({'Pending dependencies':'None'}))
 elif case=='lifecycle-only-authority':rewrite_csv(meta,lambda rs:row(rs,'KBDL-CMP-064').update({'Authority':'Approved lifecycle status only'}))
 elif case=='missing-standard-basis':rewrite_csv(meta,lambda rs:row(rs,'KBDL-CMP-064').update({'Authority':'WCAG 2.2'}))
 elif case=='nonapproved-authority-target':rewrite_csv(meta,lambda rs:row(rs,'KBDL-CMP-064').update({'Authority':'restates KBDL-RSP-002'}))
 elif case=='multi-node-cycle':
  def f(rs):row(rs,'KBDL-CMP-064').update({'Authority':'restates KBDL-CMP-101'});row(rs,'KBDL-CMP-101').update({'Authority':'restates KBDL-CMP-064'})
  rewrite_csv(meta,f)
 elif case=='self-authority':rewrite_csv(meta,lambda rs:row(rs,'KBDL-CMP-064').update({'Authority':'restates KBDL-CMP-064'}))
 elif case=='ar2-scope-exclusion':
  def f(rs):
   target=rs[0];ids=target['Requirements relying on the prompt'].split('; ');target['Requirements relying on the prompt']='; '.join(ids[1:])
  rewrite_csv(rec,f)
 elif case=='historical-falsely-recovered':rewrite_csv(rec,lambda rs:rs[0].update({'Approval command recovered':'YES'}))
 elif case=='explicit-group-conflict':
  p=d/'traceability-matrix.md';p.write_text(p.read_text().replace('- **Lifecycle status:** All Approved.\n- **Provenance:** All Confirmed.','- **Lifecycle status:** All Recommended.\n- **Provenance:** All Confirmed.',1))
 elif case=='misparsed-status-bucket':
  p=d/'traceability-matrix.md';p.write_text(p.read_text().replace('`001`, `002`, `003`: Verified; `004`: Not verified','`001`, `002`: Verified; `003`, `004`: Not verified',1))
 elif case=='valid-wrong-anchor':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-001').update({'Specification location':'governance.md#1-document-authority'}))
 elif case=='wrong-packet-item':rewrite_csv(meta,lambda rs:row(rs,'KBDL-RSP-002').update({'Packet or tracking destination':'responsive.md — 35.2 Recommended Decisions — Ready for Approval — item 999'}))
 elif case=='wrong-dependency-class':rewrite_csv(meta,lambda rs:row(rs,'KBDL-PRO-016').update({'Pending dependencies':'KBDL-CMP-067 (KBDL-008) — context only'}))
 elif case=='nonexistent-evidence-sha':rewrite_csv(meta,lambda rs:row(rs,'KBDL-GOV-003').update({'Validation evidence':'Executed evidence — commit deadbeef'}))
 elif case=='unrelated-evidence-artifact':rewrite_csv(meta,lambda rs:row(rs,'KBDL-VAL-007').update({'Validation evidence':'Executed evidence — docs/kbdl/evidence/kbdl-011-r14/artifacts/candidate-status.txt'}))
 elif case=='unrelated-limitation':rewrite_csv(meta,lambda rs:row(rs,'KBDL-CUS-001').update({'Known limitation':'Typography color preference.'}))
 elif case=='wrong-standard-clause':rewrite_csv(meta,lambda rs:row(rs,'KBDL-RSP-006').update({'Authority':'Approved (directly restates WCAG 2.2 SC 9.9.9, Level AA)'}))
 elif case=='implicit-verb-cycle':
  def f(rs):row(rs,'KBDL-CMP-064').update({'Authority':'KBDL-CMP-101 is the authority for this requirement'});row(rs,'KBDL-CMP-101').update({'Authority':'KBDL-CMP-064 is the authority for this requirement'})
  rewrite_csv(meta,f)
def main():
 baseline_dir=Path(tempfile.mkdtemp(prefix='kbdl-r16-base-'));baseline=subprocess.run([sys.executable,str(PK/'scripts/production_validator.py'),'--root',str(ROOT),'--output',str(baseline_dir)],text=True,capture_output=True);shutil.rmtree(baseline_dir)
 if baseline.returncode:print('Baseline production validator must pass before mutations',file=sys.stderr);print(baseline.stderr,file=sys.stderr);return 1
 results=[];fixtures=[]
 for case,want in CASES.items():
  tmp=Path(tempfile.mkdtemp(prefix='kbdl-r16-mut-'));fixtures.append(tmp);fixture=tmp/'repo';shutil.copytree(ROOT/'docs',fixture/'docs');shutil.copytree(ROOT/'.git',fixture/'.git');mutate(fixture,case);out=tmp/'out'
  p=subprocess.run([sys.executable,str(fixture/'docs/kbdl/evidence/kbdl-011-r16/scripts/production_validator.py'),'--root',str(fixture),'--output',str(out)],text=True,capture_output=True)
  cats=set(re.findall(r'^([A-Z0-9_]+):',p.stderr,re.M));ok=p.returncode!=0 and want in cats;wrong=not ok
  (OUT/f'{case}.txt').write_text(f'Case: {case}\nMutation: actual source file changed in isolated repository copy\nProduction validator: docs/kbdl/evidence/kbdl-011-r16/scripts/production_validator.py\nExpected category: {want}\nExit code: {p.returncode}\nDetected categories: {"; ".join(sorted(cats)) or "None"}\nIntended detection: {ok}\nFixture destroyed: yes\n\nSTDOUT\n{p.stdout}\nSTDERR\n{p.stderr}')
  results.append((case,want,ok,wrong,p.returncode,sorted(cats)));shutil.rmtree(tmp)
 bad=sum(not x[2] for x in results);wrong=sum(x[3] for x in results);remain=sum(1 for p in fixtures if p.exists())
 lines=[f'{c}: {"PASS" if ok else "FAIL"} (exit {rc}; expected {w}; detected {";".join(cats)})' for c,w,ok,_,rc,cats in results]+['',f'Real mutations executed: {len(results)}',f'Mutations detected by production validator: {sum(x[2] for x in results)}',f'Unexpected mutation passes: {bad}',f'Wrong-category detections: {wrong}',f'Fixtures remaining: {remain}']
 (OUT/'mutation-summary.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));return bool(bad or wrong or remain)
if __name__=='__main__':sys.exit(main())
