#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,re
R=Path(__file__).resolve().parents[5];S=Path(__file__).parent;A=R/'docs/kbdl/evidence/kbdl-011-r9/artifacts';A.mkdir(parents=True,exist_ok=True)
prod=subprocess.run([sys.executable,str(S/'production_validator.py')],cwd=R,text=True,capture_output=True)
neg=subprocess.run([sys.executable,str(S/'run_negative_controls.py')],cwd=R,text=True,capture_output=True)
def val(pattern,text,default='?'):
 m=re.search(pattern,text,re.M);return m.group(1) if m else default
summary=(R/'docs/kbdl/evidence/kbdl-011-r9/negative-tests/negative-controls-summary.txt').read_text() if (R/'docs/kbdl/evidence/kbdl-011-r9/negative-tests/negative-controls-summary.txt').exists() else ''
names=['group-conflict','missing-evidence','failed-evidence','partial-scope','self-reference','missing-approval','wrong-location']
patterns=['Production requirements audited','Production effective-record defects','Production authority defects','Production Verified-evidence defects','Production location defects','Production documentation defects']
lines=[name+': '+val(re.escape(name)+r': (\d+)',prod.stdout) for name in patterns]+['']
for n in names:lines.append(f'Negative {n} fixture detected: {"PASS" if re.search(r"negative-"+re.escape(n)+r": PASS",summary) else "FAIL"}')
docs=all(re.search(r'documentation-'+re.escape(x)+r': PASS',summary) for x in ['relative-link','anchor','heading-hierarchy','duplicate-heading','empty-section','placeholder','conflict-marker','table','requirement-id','decision-id','packet-reference','visible-label','stale-roadmap','premature-completion'])
metrics=[('Unexpected negative-test passes',summary),('Fixtures remaining after restoration',summary),('Unauthorized metadata changes',prod.stdout),('Completion decisions',prod.stdout)]
lines += [f'Negative documentation fixtures detected: {"PASS" if docs else "FAIL"}','']+[name+': '+val(re.escape(name)+r': (\d+)',text) for name,text in metrics]+['','Implementation conformance status: NOT VERIFIED','Project completion status: PENDING']
out='\n'.join(lines)+'\n';(A/'final-validation-output.txt').write_text(out);print(out,end='');sys.exit(bool(prod.returncode or neg.returncode or 'FAIL' in out or '?' in out))
