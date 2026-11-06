import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
import sys,glob
sys.path.insert(0,_os.path.join(DEV,'tools'))
pref=sys.argv[1]; a=int(sys.argv[2]) if len(sys.argv)>2 else 0; b=int(sys.argv[3]) if len(sys.argv)>3 else 99999
done=set()
for f in glob.glob(_os.path.join(DEV,'tm','*.tsv')):
    for l in open(f):
        if '\t' in l: done.add(l.split('\t',1)[0])
n=0
for l in open(_os.path.join(DEV,'work',f'{pref}.src.tsv')):
    k=l.split('\t',1)[0]
    if k in done: continue
    n+=1
    if a<=n<=b: print(l.rstrip('\n'))
print('#remaining',n,file=sys.stderr)
