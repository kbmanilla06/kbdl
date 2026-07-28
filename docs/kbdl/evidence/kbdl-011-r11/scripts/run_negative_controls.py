#!/usr/bin/env python3
"""Execute the twenty required R11 semantic mutations in isolated copies."""
from pathlib import Path
import csv,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[5];SRC=ROOT/'docs/kbdl';OUT=SRC/'evidence/kbdl-011-r11/negative-tests';OUT.mkdir(parents=True,exist_ok=True)
AUD=SRC/'evidence/kbdl-011-r11/scripts/semantic_audit.py';results=[]
def workspace():
 t=Path(tempfile.mkdtemp(prefix='kbdl-r11-'));shutil.copytree(SRC,t/'docs/kbdl');return t
def table(path,fn):
 rows=list(csv.DictReader(open(path)));fields=list(rows[0]);fn(rows)
 with path.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
def metadata(d,rid,field,value):table(d/'traceability-metadata.csv',lambda rows:next(r for r in rows if r['Requirement ID']==rid).__setitem__(field,value))
def mapping(d,rid,field,value):table(d/'evidence/kbdl-011-authority-recovery/artifacts/requirement-authority-mapping.csv',lambda rows:next(r for r in rows if r['Requirement ID']==rid).__setitem__(field,value))
def recovery(d,pid,field,value):table(d/'evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv',lambda rows:next(r for r in rows if r['Prompt ID']==pid).__setitem__(field,value))
def registry(d,rid,field,value):table(d/'evidence/kbdl-011-r11/verified-evidence-registry.csv',lambda rows:next(r for r in rows if r['Requirement ID']==rid).__setitem__(field,value))
def run(name,mutate,needle):
 t=workspace();d=t/'docs/kbdl';mutate(d);art=t/'artifacts';p=subprocess.run([sys.executable,str(AUD),'--root',str(t),'--source-root',str(ROOT),'--artifacts',str(art)],text=True,capture_output=True)
 detail=p.stdout+p.stderr+'\n'+'\n'.join(x.read_text(errors='replace') for x in art.glob('*') if x.is_file());ok=p.returncode!=0 and needle in detail
 (OUT/f'{name}.txt').write_text(f'Fixture: {name}\nExpected detector: {needle}\nExit code: {p.returncode}\nDetected: {ok}\n\n{p.stdout}{p.stderr}')
 results.append((name,ok,p.returncode));shutil.rmtree(t)

run('wrong-blueprint-section',lambda d:metadata(d,'KBDL-PRN-001','Blueprint section','WRONG BLUEPRINT'),'Effective-field mismatches: 1')
run('wrong-roadmap-prompt',lambda d:metadata(d,'KBDL-PRN-001','Roadmap prompt','KBDL-999'),'Effective-field mismatches: 1')
run('wrong-exact-location',lambda d:metadata(d,'KBDL-PRN-001','Specification location','principles.md#missing'),'invalid exact specification location')
run('wrong-lifecycle',lambda d:metadata(d,'KBDL-PRN-001','Lifecycle status','Deferred'),'Effective-field mismatches: 1')
run('wrong-provenance',lambda d:metadata(d,'KBDL-PRN-001','Provenance','Assumed'),'Effective-field mismatches: 1')
run('wrong-validation-classification',lambda d:metadata(d,'KBDL-PRN-001','Validation classification','Verified'),'Effective-field mismatches: 1')
run('wrong-authority-mapping',lambda d:mapping(d,'KBDL-PRN-001','Durable decision source','WRONG'),'wrong decision source')
run('authority-scope-exclusion',lambda d:recovery(d,'KBDL-002','Requirements relying on the prompt','KBDL-PRN-002'),'authority scope excludes relying requirement')
run('missing-owner-confirmation',lambda d:recovery(d,'KBDL-002','Project-owner decision','PENDING'),'missing owner confirmation')
run('backdated-authority',lambda d:mapping(d,'KBDL-PRN-001','Confirmation date','2026-07-27'),'backdated authority')
run('wrong-packet-item',lambda d:metadata(d,'KBDL-RSP-002','Packet or tracking destination','responsive.md item 999'),'Effective-field mismatches: 1')
run('wrong-dependency-class',lambda d:mapping(d,'KBDL-PRN-001','Authority dependency','UNKNOWN'),'wrong dependency class')
run('missing-evidence',lambda d:registry(d,'KBDL-A11Y-007','Evidence source','missing.txt'),'VAL-004 result: Not verified')
run('failed-evidence-result',lambda d:registry(d,'KBDL-A11Y-008','Required result','FORCED_FAILURE'),'VAL-004 result: Not verified')
run('partial-evidence-scope',lambda d:registry(d,'KBDL-A11Y-009','Verified scope','partial'),'VAL-004 result: Not verified')
run('self-referential-evidence',lambda d:registry(d,'KBDL-A11Y-007','Evidence source','evidence/kbdl-011-r11/artifacts/clause-level-evidence-audit.csv'),'VAL-004 result: Not verified')
run('unsupported-no-limitation',lambda d:metadata(d,'KBDL-A11Y-001','Known limitation','None'),'Effective-field mismatches: 1')
def duplicate(d):
 p=d/'traceability-metadata.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);rows.append(dict(rows[0]));
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
run('duplicate-authoritative-requirement',duplicate,'Duplicate authoritative requirements: 1')
run('stale-readiness-statement',lambda d:(d/'negative-fixture.md').write_text('# Fixture\nThe specification release candidate status: NOT READY pending durable prompt-authority recovery.\n'),'stale roadmap wording:')
run('premature-completion-statement',lambda d:(d/'negative-fixture.md').write_text('# Fixture\nKBDL project is complete.\n'),'premature readiness/completion claims:')

bad=sum(not ok for _,ok,_ in results);lines=[f'{n}: {"PASS" if ok else "FAIL"} (exit {c})' for n,ok,c in results]+['',f'Negative controls executed: {len(results)}',f'Unexpected negative-control passes: {bad}',f'Fixtures remaining: 0']
(OUT/'negative-controls-summary.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));sys.exit(bool(bad))
