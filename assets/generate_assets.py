import textwrap, html, os, sys
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
BG='#0d1117';CARD='#161b22';BR='#30363d';T1='#e6edf3';T2='#8b949e';G='#39d353';B='#58a6ff';Y='#e3b341';P='#bc8cff';TE='#2dd4bf'
F="font-family=\"-apple-system,Segoe UI,Helvetica,Arial,sans-serif\""
e=html.escape
def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title>{body}</svg>'
def card(x,y,w,h,fill=CARD):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{BR}"/>'
def t(x,y,s,size=13,fill=T1,wt=400,anchor='start',extra=''):
    return f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{wt}" fill="{fill}" text-anchor="{anchor}" {extra}>{e(s)}</text>'
def chip(x,y,s,color,size=11):
    w=len(s)*size*0.58+18
    return f'<rect x="{x}" y="{y}" width="{w:.0f}" height="22" rx="11" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-opacity="0.5"/>'+t(x+w/2,y+15,s,size,color,600,'middle'),w+8
def chips(x,y,items,maxw,color_cycle):
    s='';cx=x;cy=y
    for i,it in enumerate(items):
        c,w=chip(cx,cy,it,color_cycle[i%len(color_cycle)])
        if cx+w>x+maxw: cx=x;cy+=28;c,w=chip(cx,cy,it,color_cycle[i%len(color_cycle)])
        s+=c;cx+=w
    return s,cy+28
def wrap(x,y,s,width,size=12,fill=T2,lh=17):
    r='';
    for l in textwrap.wrap(s,width):
        r+=t(x,y,l,size,fill);y+=lh
    return r,y
W=960;g=16;cw=222
col=lambda i:12+i*(cw+g)
# ---------- BENTO ----------
b=f'<rect width="{W}" height="700" rx="18" fill="{BG}"/>'
# hero
b+=card(col(0),12,2*cw+g,2*130+g)
b+=f'<circle cx="{col(0)+52}" cy="64" r="30" fill="#0f2e2a" stroke="{TE}" stroke-width="2"/>'+t(col(0)+52,73,'SM',22,TE,700,'middle')
b+=t(col(0)+96,56,'Sunil Mandloi',24,T1,700)+t(col(0)+96,78,'@sunilnarayan419-ui  ·  University of Hyderabad',12,T2)
r,y=wrap(col(0)+24,118,'Integrated M.Sc. Life Sciences student building computational tools and analytical workflows for biological problems, with a long-term interest in biotechnology strategy, economics and commercialization.',62,12.5,T2,18)
b+=r
c,y=chips(col(0)+24,y+6,['Life Sciences','Computational Biology','AI / ML','Python','Biotech Strategy','Economics'],2*cw+g-48,[G,B,P,Y,TE])
b+=c
b+=t(col(0)+24,12+2*130+g-16,'Learning in public · evidence first · limitations stated',11,T2)
# stats
stats=[('5','FEATURED PROJECTS',T1),('35','LOGGED EXPERIMENTS',Y),('0.762','CV ROC-AUC (HOME CREDIT)',G),('46','ENGINEERED FEATURES',P)]
pos=[(2,0),(3,0),(2,1),(3,1)]
for (n,l,c),(cx,cy) in zip(stats,pos):
    x=col(cx);yy=12+cy*(130+g)
    b+=card(x,yy,cw,130)+t(x+cw/2,yy+68,n,38,c,700,'middle')+t(x+cw/2,yy+98,l,10,T2,600,'middle','letter-spacing="1"')
# framework
y0=12+2*130+g+g
b+=card(12,y0,W-24,150)+t(32,y0+30,'Interdisciplinary framework',13,T2,600)
steps=['Biological\nproblem','Scientific\nevidence','Computational\nanalysis','Technical\nfeasibility','Economics','Market &\ncompetition','Strategic\ndecision']
cols=[G,TE,B,B,Y,P,G]
sw=(W-24-40-6*14)/7
for i,(s,c) in enumerate(zip(steps,cols)):
    x=32+i*(sw+14)
    b+=f'<rect x="{x:.0f}" y="{y0+48}" width="{sw:.0f}" height="66" rx="10" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-opacity="0.55"/>'
    for j,l in enumerate(s.split('\n')):
        b+=t(x+sw/2,y0+78+j*16-(8 if '\n' not in s else 0)+(8 if '\n' not in s else 0),l,12,c,600,'middle')
    if i<6: b+=t(x+sw+7,y0+86,'›',20,T2,400,'middle')
b+=t(32,y0+136,'Each stage filters the next: biology constrains the data, the data constrains the model, the model constrains the economics.',11,T2)
# focus + interests
y1=y0+150+g
b+=card(12,y1,W/2-20,200)+t(32,y1+30,'Active project domains',13,T2,600)
c,yy=chips(32,y1+46,['Python & FastAPI tooling','Transcriptomic data audit','Churn-risk ML','Credit-risk ML','Pharma market analysis'],W/2-70,[G,B,Y,P,TE]);b+=c
b+=t(32,yy+20,'Learning',13,T2,600)
c,yy=chips(32,yy+30,['Bioinformatics','Statistics','Applied ML','Economics & finance'],W/2-70,[TE,B,P,Y]);b+=c
x2=W/2+4
b+=card(x2,y1,W/2-16,200)+t(x2+20,y1+30,'Research interests (not publications)',13,T2,600)
c,yy=chips(x2+20,y1+46,['Molecular & cellular biology','Genomics & transcriptomics','Computational biology','Translational research','Drug discovery','Plant biotechnology','AI for life sciences'],W/2-56,[G,B,P,Y,TE]);b+=c
b+=t(x2+20,y1+186,'No published findings claimed; see ResearchGate.',11,T2)
open(f'{out}/bento.svg','w').write(svg(W,y1+212,b.replace('height="700"',f'height="{y1+212}"'),'Profile overview: Sunil Mandloi, life sciences student, with key facts, interdisciplinary framework, focus areas and research interests'))
# ---------- PROJECT CARDS ----------
P_=[('algal','AlgalPathogenRisk-ML',TE,['Python','pandas','FastAPI','Pydantic','pytest'],
 'Research prototype on Chlamydomonas reinhardtii transcriptomics (GEO GSE128981): metadata audit script, typed API with dataset-audit and break-even economics endpoints, documentation.',
 'No validated predictive model. Dataset has no infection or culture-collapse labels, so no pathogen-risk claims.'),
('churn','Churn Handset Targeting',B,['scikit-learn','FastAPI','Docker','pytest','CI'],
 'Calibrated gradient-boosting churn model (100k customers, 97 features) with retention economics, pilot sizing, cohort endpoints, model and data cards. Built to plan a randomised retention pilot.',
 'Test ROC-AUC 0.693 on an enriched ~50% churn sample vs ~1% assumed base rate; no temporal validation; associations, not treatment effects.'),
('homecredit','Home Credit Default Risk',G,['LightGBM','XGBoost','CatBoost','pytest','CI'],
 'Installable pipeline for a course competition: 46 engineered features, 35 logged experiments, blended boosting models, leakage tests and submission validation.',
 '5-fold CV AUC 0.670 baseline to 0.762 blend, slightly optimistic. Data not included. Educational, not a lending system.'),
('novo','Novo Nordisk: Insulin India Strategy',P,['Market analysis','Strategy','Healthcare access'],
 'Research and strategic analysis of insulin access and market dynamics in India.',
 'Independent, self-directed analysis; not affiliated with or commissioned by Novo Nordisk.'),
('celltimer','Cell Division Timer',Y,['Python','Biological data'],
 'Quantitative cell-division timing and biological data analysis linking programming to a cell-biology problem.',
 'Small learning project.')]
for k,name,ac,tech,desc,stat in P_:
    w=468;bd=f'<rect width="{w}" height="10" fill="none"/>'
    s=t(22,36,name,16,T1,700)+f'<rect x="0" y="14" width="4" height="26" rx="2" fill="{ac}"/>'
    c,yy=chips(22,50,tech,w-44,[ac]);s+=c
    r,yy=wrap(22,yy+14,desc,66);s+=r
    s+=f'<line x1="22" x2="{w-22}" y1="{yy+4}" y2="{yy+4}" stroke="{BR}"/>'
    s+=t(22,yy+24,'STATUS',10,Y,700,'start','letter-spacing="1"')
    r,yy2=wrap(22,yy+42,stat,66,12,'#c9d1d9');s+=r
    h=yy2+10
    open(f'{out}/project-{k}.svg','w').write(svg(w,h,card(1,1,w-2,h-2)+s,f'{name} project card'))
# ---------- STACK ----------
rows=[('Used in projects',G,['Python','pandas','NumPy','scikit-learn','LightGBM','XGBoost','CatBoost','FastAPI','Pydantic','pytest','Docker','Git / GitHub']),
('Quality & docs',B,['Ruff','GitHub Actions CI','MkDocs Material','Model / data cards']),
('Learning',Y,['Bioinformatics workflows','NetworkX / Neo4j','SQL','R','Statistics']),
('Planned',P,['Nextflow (if raw sequencing is added)','Deeper statistical modelling'])]
s='';y=34
for lab,c,items in rows:
    s+=t(24,y+16,lab.upper(),10,c,700,'start','letter-spacing="1"')
    cc,yy=chips(190,y,items,W-230,[c]);s+=cc;y=max(yy,y+30)+12
s+=t(24,y+4,'Learning-in-progress toolkit; proficiency varies by tool. Planned items are not claimed skills.',11,T2)
h=y+22
open(f'{out}/stack.svg','w').write(svg(W,h,card(1,1,W-2,h-2)+s,'Technology stack grouped by used, quality, learning and planned'))
# ---------- ROADMAP ----------
R=['Life-science\nfoundations','Programming\n& statistics','Scientific\ndata analysis','Bioinformatics','ML & computational\nmodelling','Economics\n& finance','Biotech strategy &\ncommercialization']
st=['done','active','active','learning','learning','learning','goal']
cm={'done':G,'active':TE,'learning':B,'goal':P}
bw=(W-24)/7
s=''
for i,(r_,sx) in enumerate(zip(R,st)):
    x=12+i*bw;c=cm[sx]
    s+=f'<polygon points="{x:.0f},20 {x+bw-14:.0f},20 {x+bw-2:.0f},60 {x+bw-14:.0f},100 {x:.0f},100 {x+12:.0f},60" fill="{c}" fill-opacity="0.14" stroke="{c}" stroke-opacity="0.6"/>'
    for j,l in enumerate(r_.split('\n')): s+=t(x+bw/2-2,56+j*15-(0 if '\n' in r_ else -8),l,11,c,600,'middle')
    s+=t(x+bw/2-2,122,sx.upper(),9,c,700,'middle','letter-spacing="1"')
s+=t(W/2,148,'A direction of travel, not a list of credentials.',11,T2,400,'middle')
open(f'{out}/roadmap.svg','w').write(svg(W,164,f'<rect width="{W}" height="164" rx="14" fill="{CARD}" stroke="{BR}"/>'+s,'Learning roadmap from life-science foundations to biotech strategy'))
