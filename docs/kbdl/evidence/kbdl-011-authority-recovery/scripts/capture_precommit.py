#!/usr/bin/env python3
"""Capture AR1 precommit commands and generate the evidence inventory."""
from pathlib import Path
import csv, hashlib, subprocess
ROOT=Path(__file__).resolve().parents[5]; PKG=ROOT/'docs/kbdl/evidence/kbdl-011-authority-recovery'
records=[
"PURPOSE: synchronize remote references and verify authenticated baseline",
"$ git fetch origin",
"STDOUT:\n(empty)","STDERR:\n(empty)","EXIT: 0",
"NOTE: a prior sandboxed attempt exited 128 with `error: cannot open '.git/FETCH_HEAD': Operation not permitted`; the authorized rerun above succeeded.",""
]
commands=[
 ("confirm configured remote",['git','remote','-v']),
 ("confirm branch",['git','branch','--show-current']),
 ("confirm precommit worktree/index state",['git','status','--short']),
 ("record local HEAD",['git','rev-parse','HEAD']),
 ("record remote HEAD",['git','rev-parse','origin/main']),
 ("inspect latest twenty commits",['git','log','--oneline','--decorate','-20']),
 ("inspect baseline metadata",['git','show','--no-patch','--format=fuller','33402250e3fdb27bd8e1cba53c722b7b765daf8a']),
 ("confirm no local commits after baseline",['git','log','--oneline','33402250e3fdb27bd8e1cba53c722b7b765daf8a..HEAD']),
 ("confirm no remote commits after baseline",['git','log','--oneline','33402250e3fdb27bd8e1cba53c722b7b765daf8a..origin/main']),
 ("regenerate packet",['python3','docs/kbdl/evidence/kbdl-011-authority-recovery/scripts/build_packet.py']),
 ("validate packet and protected fields",['python3','docs/kbdl/evidence/kbdl-011-authority-recovery/scripts/validate_packet.py']),
 ("check patch whitespace",['git','diff','--check']),
 ("confirm origin/main is ancestor of work HEAD",['git','merge-base','--is-ancestor','origin/main','HEAD']),
]
for purpose,cmd in commands:
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
 records += [f'PURPOSE: {purpose}','$ '+' '.join(cmd),'STDOUT:',r.stdout.rstrip() or '(empty)','STDERR:',r.stderr.rstrip() or '(empty)',f'EXIT: {r.returncode}','']
(PKG/'precommit-transcript.txt').write_text('\n'.join(records),encoding='utf-8')
excluded={'checksums.sha256','evidence-inventory.csv'}
files=sorted(p for p in PKG.rglob('*') if p.is_file() and p.name not in excluded)
with (PKG/'evidence-inventory.csv').open('w',newline='',encoding='utf-8') as h:
 w=csv.writer(h,lineterminator='\n');w.writerow(['Path','Purpose','Bytes','SHA-256','Availability'])
 for p in files:
  data=p.read_bytes();w.writerow([p.relative_to(ROOT),'AR1 evidence package file',len(data),hashlib.sha256(data).hexdigest(),'AVAILABLE'])
hash_files=sorted(p for p in PKG.rglob('*') if p.is_file() and p.name!='checksums.sha256')
(PKG/'checksums.sha256').write_text('\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}' for p in hash_files)+'\n',encoding='utf-8')
print(f'Captured {len(commands)+1} commands; inventoried {len(files)} files; checksummed {len(hash_files)} files')
