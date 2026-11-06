import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
import json,sys,re
sys.path.insert(0,_os.path.join(DEV,'tools'))
from tm import load_tm
TM=load_tm()
en=json.load(open(_os.path.join(REPO,'original','lang','en.json')))
miss=[];bad=[]
def tr(o,p=''):
    if isinstance(o,dict): return {k:tr(v,p+'.'+k) for k,v in o.items()}
    if isinstance(o,str):
        if o in TM:
            u=TM[o]
            if sorted(re.findall(r'\{[^}]+\}',o))!=sorted(re.findall(r'\{[^}]+\}',u)) and '@' not in o: bad.append((p,o,u))
            return u
        miss.append(p); return o
    return o
out=tr(en)
json.dump(out,open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('missing',len(miss),miss[:5]); print('placeholder mismatch',len(bad))
for b in bad: print(b)
