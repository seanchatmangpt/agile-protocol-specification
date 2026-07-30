#!/usr/bin/env python3
from pathlib import Path
import re, json, hashlib, sys, collections, shutil, subprocess
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'specification-guide'/'src'
SUMMARY=SRC/'SUMMARY.md'
RECEIPTS=ROOT/'receipts'; RECEIPTS.mkdir(exist_ok=True)
fail=[]; evidence=[]
links=re.findall(r'\[[^]]+\]\(([^)]+\.md)\)', SUMMARY.read_text())
if len(links) < 15: fail.append({'code':'SUMMARY_INCOMPLETE','observed':len(links)})
paras=[]; files=[]; total_words=0
for rel in links:
 p=SRC/rel
 if not p.exists(): fail.append({'code':'CHAPTER_MISSING','path':rel}); continue
 t=p.read_text(); files.append(p); words=len(re.findall(r"\b[\w'–-]+\b",t)); total_words+=words
 h1=len(re.findall(r'(?m)^# ',t))
 if h1 != 1: fail.append({'code':'H1_CARDINALITY','path':rel,'observed':h1})
 minimum=500 if rel.startswith('v26_7_30/0') else 350
 if words < minimum: fail.append({'code':'CHAPTER_NOT_SUBSTANTIVE','path':rel,'words':words,'minimum':minimum})
 for para in re.split(r'\n\s*\n',t):
  n=' '.join(para.split())
  if len(n.split()) >= 30 and not n.startswith('```'): paras.append(n)
 evidence.append({'kind':'chapter','path':rel,'words':words,'sha256':hashlib.sha256(t.encode()).hexdigest()})
corpus='\n'.join(p.read_text() for p in files)
required=['A = μ(O*)','R ⊢ A = μ(O*)','SELECT is not DO','Zero unreceipted actuation','APS and Gall solve adjacent but non-equivalent problems','PARTIAL_ALIVE','ALIVE','BLOCKED','BUILD_BROKEN','UNKNOWN','UNSUPPORTED','same-object falsifier','evidence coordinate']
for phrase in required:
 if phrase not in corpus: fail.append({'code':'INVARIANT_MISSING','phrase':phrase})
counts=collections.Counter(paras); duplicate=sum(c-1 for c in counts.values() if c>1); ratio=duplicate/max(1,len(paras))
if ratio > 0.12: fail.append({'code':'BOILERPLATE_RATIO_EXCEEDED','ratio':ratio})
req_ids=re.findall(r'\*\*Requirement ([A-Z0-9-]+)\.\*\*', corpus)
dup_req=[x for x,c in collections.Counter(req_ids).items() if c>1]
if dup_req: fail.append({'code':'DUPLICATE_REQUIREMENT_IDS','ids':dup_req})
for schema in ['work_order.schema.json','receipt.schema.json']:
 p=ROOT/'specification-guide'/'schemas'/schema
 try: json.loads(p.read_text())
 except Exception as e: fail.append({'code':'SCHEMA_INVALID','path':schema,'error':str(e)})
 else: evidence.append({'kind':'schema','path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
if any('/book/' in str(p) for p in files): fail.append({'code':'GENERATED_OUTPUT_IN_SOURCE_MANIFEST'})
mdbook=shutil.which('mdbook')
render={'standing':'UNSUPPORTED','reason':'mdbook not installed'}
if mdbook:
 r=subprocess.run([mdbook,'build'],cwd=ROOT/'specification-guide',text=True,capture_output=True)
 render={'standing':'ALIVE' if r.returncode==0 else 'BUILD_BROKEN','returncode':r.returncode,'stdout':r.stdout[-2000:],'stderr':r.stderr[-2000:]}
 if r.returncode: fail.append({'code':'MDBOOK_BUILD_FAILED'})
standing='ALIVE' if not fail else 'BLOCKED'
receipt={'schema':'aps.receipt.v26.7.30','operation_id':'aps-v26.7.30-book-verifier','subject':'sha256:'+hashlib.sha256(corpus.encode()).hexdigest(),'coordinate':{'source':'seanchatmangpt/agile-protocol-specification','revision':'WORKTREE','command':'python3 specification-guide/scripts/verify_v26_7_30.py','toolchain':sys.version.split()[0],'environment':sys.platform},'standing':standing,'metrics':{'chapters':len(files),'words':total_words,'long_paragraphs':len(paras),'duplicate_paragraph_ratio':ratio},'render':render,'failures':fail,'evidence':evidence,'lineage':{'parents':['7a713c199e23f7b24b4c2d0d80a86996dd106f5c'],'supersedes':['heading-only mdBook source scaffold']},'replay':{'command':'python3 specification-guide/scripts/verify_v26_7_30.py','expected':'MATCH'},'nonclaims':['ALIVE is bounded to the checks recorded here','mdBook rendering is separate when the tool is unavailable','no downstream Gall checkpoint execution is claimed']}
out=RECEIPTS/'APS-v26.7.30-verifier.json'; out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'standing':standing,'chapters':len(files),'words':total_words,'duplicate_paragraph_ratio':ratio,'mdbook':render['standing'],'receipt':str(out.relative_to(ROOT)),'failures':fail},indent=2))
sys.exit(0 if not fail else 1)
