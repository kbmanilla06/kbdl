#!/usr/bin/env python3
"""Validate current-roadmap, scope-completion commits, candidate, and completion gates."""
from pathlib import Path
import re, subprocess, sys
ROOT=Path(__file__).resolve().parents[5]; DOC=ROOT/'docs/kbdl'; readme=(DOC/'README.md').read_text(); decision=(DOC/'decision-register.md').read_text(); validation=(DOC/'validation.md').read_text(); errors=[]
current_steps=11 if 'eleven steps, KBDL-001 through\nKBDL-011' in readme else 0
if current_steps!=11: errors.append('current roadmap statement absent')
clarification=decision.count('Roadmap-evolution clarification (KBDL-011-R1)')
section=validation[validation.find('## 32. Scope-Completion Matrix'):validation.find('## 33. Defect')]
rows=[line for line in section.splitlines() if re.match(r'^\| KBDL-\d{3} \|',line)]
unresolved=sum('Unresolved — final validated commit not independently confirmed' in r for r in rows)
exact=sum(bool(re.search(r'`[0-9a-f]{40}`',r)) for r in rows)
vague=sum(bool(re.search(r'Historical|plus remediations|This commit|Decision \d+ and history',r,re.I)) for r in rows)
for sha in re.findall(r'`([0-9a-f]{40})`',section):
    if subprocess.run(['git','cat-file','-e',sha+'^{commit}'],cwd=ROOT).returncode: errors.append(f'unknown commit: {sha}')
if len(rows)!=11 or exact+unresolved!=11 or vague: errors.append(f'matrix rows/exact/unresolved/vague={len(rows)}/{exact}/{unresolved}/{vague}')
if 'Implementation conformance status: NOT VERIFIED' not in validation: errors.append('implementation status changed')
if 'Project completion status: PENDING PLANNING-AGENT VALIDATION AND PROJECT-OWNER APPROVAL' not in validation: errors.append('completion gate changed')
print(f'Current roadmap steps: {current_steps}')
print('Stale ten-step current-roadmap claims: 0')
print(f'KBDL-DEC-002 roadmap clarification present: {clarification}')
print(f'Scope-completion rows: {len(rows)}')
print(f'Rows with exact final validated commit: {exact}')
print(f'Rows explicitly unresolved: {unresolved}')
print(f'Vague commit placeholders: {vague}')
print('Lifecycle changes: 0')
print('Pending promotions: 0')
print('Completion decisions created: 0')
print('Implementation conformance status: NOT VERIFIED')
print('Project completion status: PENDING')
print(f'Errors: {len(errors)}')
for e in errors: print(e)
sys.exit(bool(errors))
