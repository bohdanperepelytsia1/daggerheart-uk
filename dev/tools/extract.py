import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
# usage: extract.py prefix file1 file2 ...  -> work/prefix.src.tsv with new unique strings
import sys,json,re
sys.path.insert(0,_os.path.join(DEV,'tools'))
from flat import strings
from tm import esc,load_src
pref=sys.argv[1]; files=sys.argv[2:]
known=set(load_src().values())
seen=[];ss=set()
for f in files:
    for p,s in strings(f):
        if p[0]=='label' or p[0]=='folders' or True:
            if s in known or s in ss: continue
            ss.add(s); seen.append(s)
with open(_os.path.join(DEV,'work',f'{pref}.src.tsv'),'w',encoding='utf-8') as o:
    for i,s in enumerate(seen): o.write(f'{pref}{i:04d}\t{esc(s)}\n')
print(len(seen))
