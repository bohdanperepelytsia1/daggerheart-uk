import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
# list unique strings still English in built translations for given packs, mapped to src ids
import json,sys,re
sys.path.insert(0,_os.path.join(DEV,'tools'))
from tm import load_src,esc,load_tm
from segs import is_long,segments
TMX=load_tm()
src=load_src(); inv={}
for k,v in sorted(src.items()): inv.setdefault(v,k)
packs=sys.argv[1].split(','); lim=int(sys.argv[2]) if len(sys.argv)>2 else 10**9
seen=[];ss=set();chars=0;cnt={};ctx={};cur=[None]
def walk(o,t,top=False):
    if isinstance(o,str) and is_long(o) and o not in TMX:
        osegs=set(segments(o))
        for sg in segments(t if isinstance(t,str) else o):
            if sg in osegs and sg not in TMX:
                cnt[sg]=cnt.get(sg,0)+1
                if sg not in ss: ss.add(sg); seen.append(sg); ctx[sg]=cur[0]
        return
    if isinstance(o,str):
        if t==o and re.search('[A-Za-z]{2}',o):
            cnt[o]=cnt.get(o,0)+1
            if o not in ss: ss.add(o); seen.append(o); ctx[o]=cur[0]
    elif isinstance(o,dict):
        for k,v in o.items():
            if k=='mapping' and top: continue
            walk(v,t.get(k) if isinstance(t,dict) else None)
    elif isinstance(o,list):
        for i,v in enumerate(o): walk(v,t[i] if isinstance(t,list) and i<len(t) else None)
for p in packs:
    a=json.load(open(_os.path.join(REPO,'original',f'daggerheart.{p}.json')))
    b=json.load(open(_os.path.join(REPO,'module','translations',f'daggerheart.{p}.json')))
    for en,ev in a['entries'].items():
        cur[0]=en; walk(ev,b['entries'].get(en))
    cur[0]=None; walk({k:v for k,v in a.items() if k!='entries'},b,True)
print('#remaining',len(seen),'chars',sum(len(s) for s in seen))
last=None
off=int(sys.argv[3]) if len(sys.argv)>3 else 0
for s in seen[off:off+lim]:
    if ctx[s]!=last: print('##',ctx[s]); last=ctx[s]
    print(f'{inv.get(s,"??")}\t{"[x%d] "%cnt[s] if cnt[s]>1 else ""}{esc(s)}')
