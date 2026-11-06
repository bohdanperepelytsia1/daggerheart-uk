import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
import json,sys,glob,os,re
sys.path.insert(0,_os.path.join(DEV,'tools'))
from tm import load_tm
TM=load_tm()
src=_os.path.join(REPO,'original'); dst=_os.path.join(REPO,'module','translations')
os.makedirs(dst,exist_ok=True)
tot=0;done=0
def tr(o,top=None):
    global tot,done
    if isinstance(o,str):
        if not re.search('[A-Za-z]',o): return o
        tot+=1
        if o in TM: done+=1; return TM[o]
        return o
    if isinstance(o,dict): return {k:(v if k=='mapping' and top else tr(v)) for k,v in o.items()}
    if isinstance(o,list): return [tr(v) for v in o]
    return o
for f in sorted(glob.glob(src+'/daggerheart.*.json')):
    d=json.load(open(f)); tot=done=0
    out={k:(v if k=='mapping' else tr(v)) for k,v in d.items()}
    json.dump(out,open(os.path.join(dst,os.path.basename(f)),'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(os.path.basename(f),f'{done}/{tot}')
