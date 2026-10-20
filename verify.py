from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).parent/'dist'
class Doc(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.h1=0;self.panels=[];self.imgs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if 'data-panel' in a:self.panels.append(a.get('id'))
  if tag=='img':self.imgs.append(a)
  for k in ['src','href']:
   if k in a:self.links.append(a[k])
docs={}
for f in ROOT.rglob('*.html'):
 d=Doc();d.feed(f.read_text());docs[f.resolve()]=d
 assert len(d.ids)==len(set(d.ids)),f
 assert d.h1==1,f
 assert all(i.get('alt') for i in d.imgs),f
for f,d in docs.items():
 for u in d.links:
  p=urlsplit(u)
  if p.scheme or p.netloc:
   assert p.scheme=='https',(f,u)
   continue
  target=(f.parent/unquote(p.path)).resolve() if p.path else f
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(f,u)
  if p.fragment and target in docs:assert p.fragment in docs[target].ids,(f,u)
styles=json.loads((ROOT.parent/'curriculum.json').read_text())
assert len(styles)==32 and len({s['id'] for s in styles})==32
assert len(docs)==36
for s in styles:
 d=docs[(ROOT/'styles'/s['id']/'index.html').resolve()]
 assert d.panels==['overview','origins','vocabulary','examples','construction'],s['id']
 assert len(s['traits'])==3 and len(s['build'])==2 and s['examples'] and s['exercise']
for f in (ROOT/'assets').glob('*.svg'):ET.parse(f)
assert len(list((ROOT/'assets').glob('*.svg')))==33
print('PASS: 36 pages; 32 complete studies; 160 lesson sections; all local links, anchors, image labels, and 33 SVGs.')
