# paragraph-level segmentation of long HTML strings (journals)
import re
BLK=re.compile(r'(<(p|h[1-6]|li|td|th|figcaption|blockquote)(?:\s[^>]*)?>)(.*?)(</\2>)',re.S)
NEST=re.compile(r'<(p|h[1-6]|li|td|th|ul|ol|table|blockquote)[\s>]')
def is_long(s): return isinstance(s,str) and len(s)>600 and '<' in s
def _txt(inner): return re.search('[A-Za-z]{2}',re.sub(r'<[^>]+>|@\w+\[[^\]]*\]','',inner))
def segments(html):
    out=[]
    for m in BLK.finditer(html):
        inner=m.group(3)
        if NEST.search(inner): out+=segments(inner)
        elif _txt(inner): out.append(inner.strip())
    return out
def translate(html,tm):
    def rep(m):
        inner=m.group(3)
        if NEST.search(inner): return m.group(1)+translate(inner,tm)+m.group(4)
        t=tm.get(inner.strip())
        return m.group(1)+t+m.group(4) if t is not None else m.group(0)
    return BLK.sub(rep,html)
