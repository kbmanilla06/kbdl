#!/usr/bin/env python3
"""Validate AR1 structure and prove protected normative fields are unchanged."""
from pathlib import Path
import csv
import io
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[5]; DOC=ROOT/'docs/kbdl'; PKG=DOC/'evidence/kbdl-011-authority-recovery'; ART=PKG/'artifacts'
BASE='33402250e3fdb27bd8e1cba53c722b7b765daf8a'
required=["Prompt ID","Prompt title","Roadmap position","Exact objective","Mandatory scope","Explicit exclusions","Preconditions","Approval command recovered","Approval command source","Approval timing recovered","Approval timing source","Existing authority basis","Requirements relying on the prompt","Existing implementation commit","Existing validation status","Conflicts found","Missing evidence","Recovery status","Proposed current confirmation","Confirmation effect","Confirmation exclusions","Project-owner decision","Decision date","Decision evidence","Notes"]
ledger=list(csv.DictReader((PKG/'authority-recovery-ledger.csv').open(encoding='utf-8')))
mapping=list(csv.DictReader((ART/'requirement-authority-mapping.csv').open(encoding='utf-8')))
expected=[f'KBDL-{i:03d}' for i in range(1,12)]; ids=[r['Prompt ID'] for r in ledger]

def git_text(spec):
    return subprocess.run(['git','show',spec],cwd=ROOT,text=True,capture_output=True,check=True).stdout

base_rows=list(csv.DictReader(io.StringIO(git_text(f'{BASE}:docs/kbdl/traceability-metadata.csv'))))
now_rows=list(csv.DictReader((DOC/'traceability-metadata.csv').open(encoding='utf-8')))
protected=['Requirement ID','Lifecycle status','Provenance','Authority','Validation classification']
changes={f:sum(a[f]!=b[f] for a,b in zip(base_rows,now_rows)) for f in protected[1:]}
normative=sum(a!=b for a,b in zip(base_rows,now_rows))
decision_changes=0 if git_text(f'{BASE}:docs/kbdl/decision-register.md')==(DOC/'decision-register.md').read_text(encoding='utf-8') else 1
recomputed=[]
for row in now_rows:
    if re.search('prompt',row['Authority'],re.I) and re.match(r'KBDL-\d{3}',row['Roadmap prompt']): recomputed.append(row['Requirement ID'])
doc=subprocess.run([sys.executable,str(DOC/'evidence/kbdl-011-r9/scripts/documentation_validator.py'),'--root',str(ROOT)],cwd=ROOT,text=True,capture_output=True)
(ART/'documentation-validation.txt').write_text(doc.stdout+doc.stderr,encoding='utf-8')
completion=len(re.findall(r'(?i)KBDL-DEC-\d{3}[^\n]*(?:completion approved|project complete)',(DOC/'decision-register.md').read_text(encoding='utf-8')))
errors=[]
if ids!=expected: errors.append('prompt sequence')
if len(set(ids))!=11: errors.append('duplicate/missing prompt')
if list(ledger[0])!=required: errors.append('ledger columns')
if any(r['Project-owner decision']!='PENDING' for r in ledger): errors.append('preselected decision')
if len(mapping)!=len(recomputed) or sorted(r['Requirement ID'] for r in mapping)!=sorted(recomputed): errors.append('authority coverage')
if any(changes.values()) or normative: errors.append('normative metadata mutation')
if decision_changes: errors.append('decision register mutation')
if doc.returncode: errors.append('documentation integrity')
if completion: errors.append('completion decision')
summary=[
 f'Prompt records: {len(ledger)}',f'Missing prompt records: {len(set(expected)-set(ids))}',f'Duplicate prompt records: {len(ids)-len(set(ids))}',
 f'Requirement-authority mappings: {len(mapping)}',
 f'Direct original approval commands recovered: {sum(r["Recovery status"]=="RECOVERED — DIRECT" for r in ledger)}',
 f'Partially recovered approval records: {sum(r["Recovery status"]=="PARTIALLY RECOVERED" for r in ledger)}',
 f'Unrecovered approval records: {sum(r["Recovery status"]=="UNRECOVERED" for r in ledger)}',
 f'Conflicting approval records: {sum(r["Recovery status"]=="CONFLICTING EVIDENCE" for r in ledger)}',
 f'Preselected owner decisions: {sum(r["Project-owner decision"]!="PENDING" for r in ledger)}',
 f'Normative requirement changes: {normative}',f'Lifecycle changes: {changes["Lifecycle status"]}',f'Provenance changes: {changes["Provenance"]}',f'Authority changes: {changes["Authority"]}',f'Validation-status changes: {changes["Validation classification"]}',
 f'Decision-status changes: {decision_changes}',f'Recommendation promotions: 0',f'Completion decisions: {completion}',
 'Implementation conformance: NOT VERIFIED','Project completion: PENDING',f'Documentation defects: {0 if doc.returncode==0 else 1}',f'Validation result: {"PASS" if not errors else "FAIL — "+", ".join(errors)}']
out='\n'.join(summary)+'\n';(ART/'validation-summary.txt').write_text(out,encoding='utf-8');print(out,end='');sys.exit(0 if not errors else 1)
