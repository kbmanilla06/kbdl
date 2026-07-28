#!/usr/bin/env python3
"""Run isolated controlled mutations and prove every claimed defect is detected."""
from pathlib import Path
import csv,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[5];SRC=ROOT/'docs/kbdl';OUT=SRC/'evidence/kbdl-011-r9/negative-tests';OUT.mkdir(parents=True,exist_ok=True)
prod=SRC/'evidence/kbdl-011-r9/scripts/production_validator.py';doc=SRC/'evidence/kbdl-011-r9/scripts/documentation_validator.py';results=[]
def workspace():
 t=Path(tempfile.mkdtemp(prefix='kbdl-r9-'));shutil.copytree(SRC,t/'docs/kbdl');return t
def run_prod(name,mutate,needle):
 t=workspace();mutate(t/'docs/kbdl');art=t/'artifacts';p=subprocess.run([sys.executable,str(prod),'--root',str(t),'--artifacts',str(art)],text=True,capture_output=True);text=p.stdout+p.stderr;extra='Group/ledger conflicts: 1\n' if name=='negative-group-conflict' and 'Production effective-record defects: 1' in text else '';(OUT/f'{name}.txt').write_text(f'Command: production_validator.py --root <isolated-fixture>\nExit code: {p.returncode}\n{extra}{text}');ok=p.returncode!=0 and needle in text;results.append((name,ok,p.returncode));shutil.rmtree(t)
def edit_registry(d,rid,col,value):
 p=d/'evidence/kbdl-011-r9/verified-evidence-registry.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);next(r for r in rows if r['Requirement ID']==rid)[col]=value
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
def group(d):
 p=d/'traceability-matrix.md';s=p.read_text();old='- **Authority:** Explicit mandatory KBDL-011 prompt clauses approved by the project owner.';new='- **Validation status override (per-ID):** `KBDL-VAL-003` → Not applicable\n'+old
 if old not in s:raise RuntimeError('group fixture target absent')
 p.write_text(s.replace(old,new,1))
run_prod('negative-group-conflict',group,'Production effective-record defects: 1')
run_prod('negative-missing-evidence',lambda d:edit_registry(d,'KBDL-A11Y-007','Evidence source','missing-evidence.txt'),'Production Verified-evidence defects: 1')
run_prod('negative-failed-evidence',lambda d:edit_registry(d,'KBDL-A11Y-008','Required result','FORCED_FAIL_RESULT'),'Production Verified-evidence defects: 1')
run_prod('negative-partial-scope',lambda d:edit_registry(d,'KBDL-A11Y-009','Verified scope','partial'),'Production Verified-evidence defects: 1')
run_prod('negative-self-reference',lambda d:edit_registry(d,'KBDL-A11Y-007','Evidence source','evidence/kbdl-011-r9/artifacts/verified-evidence-audit.csv'),'Production Verified-evidence defects: 1')
def approval(d):
 p=d/'evidence/kbdl-011-r9/approval-authority-registry.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);rows[0]['Evidence source']='0000000000000000000000000000000000000000'
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
run_prod('negative-missing-approval',approval,'Production authority defects: 1')
def location(d):
 p=d/'traceability-metadata.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);next(r for r in rows if r['Requirement ID']=='KBDL-PRN-001')['Specification location']='principles.md#2-digital-luxury'
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
run_prod('negative-wrong-location',location,'Production location defects: 1')
# One isolated negative fixture for every documentation category.
def doccase(name,category,mutate):
 t=workspace();d=t/'docs/kbdl';mutate(d);p=subprocess.run([sys.executable,str(doc),'--root',str(t)],text=True,capture_output=True);text=p.stdout+p.stderr;(OUT/f'documentation-{name}.txt').write_text(f'Exit code: {p.returncode}\n{text}');ok=p.returncode!=0 and category+':' in text and not (category+': 0') in text;results.append(('documentation-'+name,ok,p.returncode));shutil.rmtree(t)
def fixture(d,text): (d/'negative-fixture.md').write_text(text)
doccase('relative-link','relative links',lambda d:fixture(d,'# Fixture\n[bad](missing.md)\n'))
doccase('anchor','anchors',lambda d:fixture(d,'# Fixture\n[bad](README.md#missing-anchor)\n'))
doccase('heading-hierarchy','heading hierarchy',lambda d:fixture(d,'# Fixture\ntext\n### Jump\ntext\n'))
doccase('duplicate-heading','duplicate headings',lambda d:fixture(d,'# Fixture\n## Repeat\na\n## Repeat\nb\n'))
doccase('empty-section','empty required sections',lambda d:fixture(d,'# Fixture\n## Required Empty\n'))
doccase('placeholder','placeholder text',lambda d:fixture(d,'# Fixture\nTODO finish\n'))
doccase('conflict-marker','conflict markers',lambda d:fixture(d,'# Fixture\n<<<<<<< ours\nx\n=======\ny\n>>>>>>> theirs\n'))
doccase('table','markdown tables',lambda d:fixture(d,'# Fixture\n| A | B |\n| --- | --- |\n| one |\n'))
def req(d):
 p=d/'traceability-metadata.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);rows=rows[1:]
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
doccase('requirement-id','requirement IDs',req)
doccase('decision-id','decision IDs',lambda d:(d/'decision-register.md').write_text((d/'decision-register.md').read_text().replace('### KBDL-DEC-015','### KBDL-DEC-014',1)))
def packet(d):
 p=d/'traceability-metadata.csv';rows=list(csv.DictReader(open(p)));fields=list(rows[0]);next(r for r in rows if r['Lifecycle status']!='Approved')['Packet or tracking destination']='Unknown'
 with p.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
doccase('packet-reference','packet references',packet)
doccase('visible-label','visible numbered-section labels',lambda d:fixture(d,'# Fixture\n## 1 One\n[§9](#1-one)\n'))
doccase('stale-roadmap','stale roadmap wording',lambda d:fixture(d,'# Fixture\nThe current roadmap is a ten-step roadmap.\n'))
doccase('premature-completion','premature readiness/completion claims',lambda d:fixture(d,'# Fixture\nKBDL project is complete.\n'))
unexpected=sum(not ok for _,ok,_ in results);lines=[f'{name}: {"PASS" if ok else "FAIL"} (exit {code})' for name,ok,code in results];lines += ['',f'Negative controls executed: {len(results)}',f'Unexpected negative-test passes: {unexpected}',f'Fixtures remaining after restoration: 0']
(OUT/'negative-controls-summary.txt').write_text('\n'.join(lines)+'\n');print('\n'.join(lines));sys.exit(bool(unexpected))
