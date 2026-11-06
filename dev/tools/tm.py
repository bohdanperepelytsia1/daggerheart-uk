import os as _os
DEV=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO=_os.path.dirname(DEV)
import glob,os
def esc(s): return s.replace('\\','\\\\').replace('\n','\\n').replace('\t','\\t')
def unesc(s):
    out=[];i=0
    while i<len(s):
        c=s[i]
        if c=='\\' and i+1<len(s):
            n=s[i+1]; out.append({'n':'\n','t':'\t','\\':'\\'}.get(n,'\\'+n)); i+=2
        else: out.append(c); i+=1
    return ''.join(out)
def load_src():
    M={}
    for f in glob.glob(_os.path.join(DEV,'work','*.src.tsv')):
        for l in open(f,encoding='utf-8'):
            if '\t' in l:
                k,v=l.rstrip('\n').split('\t',1); M[k]=unesc(v)
    return M
def load_tm():
    src=load_src(); TM={}
    for f in sorted(glob.glob(_os.path.join(DEV,'tm','*.tsv'))):
        for n,l in enumerate(open(f,encoding='utf-8')):
            l=l.rstrip('\n')
            if not l or l.startswith('#'): continue
            if '\t' not in l: print('BADLINE',f,n+1,l[:60]); continue
            k,v=l.split('\t',1)
            if k not in src: print('UNKNOWN ID',f,k); continue
            TM[src[k]]=unesc(v)
    return TM
