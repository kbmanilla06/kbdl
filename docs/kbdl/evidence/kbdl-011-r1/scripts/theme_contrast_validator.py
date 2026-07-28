#!/usr/bin/env python3
"""Reproduce the approved opaque KBDL theme contrast subset."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[5]/'docs/kbdl'
C={'n0':'FFFFFF','n10':'F5F6F8','n30':'D3D6DC','n50':'8A8F99','n60':'636872','n70':'52565F','n90':'23252B','n100':'121317','a30':'A9ACFF','a50':'4A4EE0','infoL':'164499','posL':'146B3A','cautL':'8A5A00','critL':'B3261E','infoD':'7CC4FF','posD':'6FD19A','cautD':'E0A840','critD':'FF8A80'}
def lum(h):
    x=[int(h[i:i+2],16)/255 for i in (0,2,4)]; x=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in x]; return .2126*x[0]+.7152*x[1]+.0722*x[2]
def ratio(a,b):
    x,y=sorted((lum(C[a]),lum(C[b])),reverse=True); return (x+.05)/(y+.05)
pairs=[('light primary','n90','n0',4.5),('light secondary','n60','n0',4.5),('light large/nontext','n50','n0',3),('dark primary','n10','n100',4.5),('dark secondary','n50','n100',4.5),('light accent','a50','n0',4.5),('dark accent','a30','n100',4.5),('light structural','n70','n0',3),('light decorative','n30','n0',0),('dark structural','n50','n90',3),('dark decorative','n70','n90',0),('light informational','infoL','n0',4.5),('light positive','posL','n0',4.5),('light caution','cautL','n0',4.5),('light critical','critL','n0',4.5),('light info on strong','n10','infoL',4.5),('dark informational','infoD','n100',4.5),('dark positive','posD','n100',4.5),('dark caution','cautD','n100',4.5),('dark critical','critD','n100',4.5),('dark info subtle','infoD','n90',4.5),('dark positive subtle','posD','n90',4.5),('dark caution subtle','cautD','n90',4.5),('dark critical subtle','critD','n90',4.5),('opaque caption','n10','n100',4.5)]
fail=[]
for name,a,b,t in pairs:
    r=ratio(a,b); result='EXEMPT' if not t else ('PASS' if r>=t else 'FAIL'); print(f'{name}: #{C[a]}/#{C[b]} {r:.2f}:1 threshold={t or "decorative"} {result}')
    if t and r<t: fail.append(name)
print(f'Pairs: {len(pairs)}; applicable failures: {len(fail)}')
sys.exit(bool(fail))
