import json,sys,re
def flat(o,p=()):
    if isinstance(o,str): yield p,o
    elif isinstance(o,dict):
        for k,v in o.items(): yield from flat(v,p+(k,))
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from flat(v,p+(i,))
def strings(fn,skip_mapping=True):
    d=json.load(open(fn))
    for p,s in flat(d):
        if p and p[0]=='mapping': continue
        if not re.search('[A-Za-z]',s): continue
        yield p,s
