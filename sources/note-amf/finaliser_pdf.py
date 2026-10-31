"""Retouche du PDF exporté de Claude Docs pour la Note AMF IA.

Usage : python finaliser_pdf.py <export.pdf> <sortie.pdf>

L'export de Claude Docs sort la date et la pagination en anglais et laisse le titre
du § 11.3 seul sur sa page. Le script remonte le tableau sous son titre, supprime la
page devenue vide, met le pied de page en français (« Page X sur N »), redessine la
ligne date/auteur de la page 1 et renseigne les métadonnées.
"""
import pymupdf, re, sys
SRC, OUT = sys.argv[1], sys.argv[2]
src=pymupdf.open(SRC); d=pymupdf.open(SRC)
fonts={f[3].split('+')[-1]:f[0] for f in d[0].get_fonts()}
dv=pymupdf.Font(fontbuffer=d.extract_font(fonts['DejaVuSans'])[3])
sans=pymupdf.Font(fontbuffer=d.extract_font(fonts['AnthropicSansPrint-Regular'])[3])
for ch in 'Page sur0123456789': assert dv.has_glyph(ord(ch)), ch
for ch in '31 octobre 2026@André-GuyBruneau': assert sans.has_glyph(ord(ch)), ch
NO_GFX=dict(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)

def spans(pg):
    return [s for b in pg.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l['spans']]

# 1. titre 11.3 orphelin : remonter le tableau de la page suivante sous le titre
i48=next(i for i,p in enumerate(d) if p.get_text().count('\n')<8 and '11.3 Où les régimes se rejoignent' in p.get_text())
head=[s for s in spans(d[i48]) if s['text'].startswith('11.3')][0]
top=head['bbox'][3]+12
clip=pymupdf.Rect(50,49,570,738)
sc=(d[i48].rect.height-34-top)/clip.height  # garde 34 pt au-dessus du pied de page
sc=min(sc,1.0)
d[i48].show_pdf_page(pymupdf.Rect(clip.x0,top,clip.x0+clip.width*sc,top+clip.height*sc),src,i48+1,clip=clip)
d.delete_page(i48+1)
print('page fusionnée', i48+1, 'échelle', round(sc,3))

# 2. pied de page : « Page X of N » -> « Page X sur N »
N=d.page_count
for i,pg in enumerate(d):
    for s in spans(pg):
        if re.fullmatch(r'Page \d+ of \d+',s['text']):
            r=pymupdf.Rect(s['bbox']); pg.add_redact_annot(r)
            pg.apply_redactions(**NO_GFX)
            txt=f'Page {i+1} sur {N}'; w=dv.text_length(txt,fontsize=6)
            tw=pymupdf.TextWriter(pg.rect); tw.append((r.x1-w,s['origin'][1]),txt,font=dv,fontsize=6)
            tw.write_text(pg,color=(0x6b/255,)*3)
# 3. date et auteur de la page 1 : pastilles redessinées à la largeur du texte français
pg=d[0]
sp=spans(pg)
dt=[x for x in sp if x['text']=='Oct 31, 2026'][0]; dot=[x for x in sp if x['text']==' · '][0]
au=[x for x in sp if 'Andre-Guy' in x['text']][0]
pills=[dr for dr in pg.get_drawings() if dr['rect'].y0>170 and dr['rect'].y1<205]
fill=pills[0]['fill']; py0,py1=pills[0]['rect'].y0,pills[0]['rect'].y1; pad=dt['bbox'][0]-pills[0]['rect'].x0
zone=pymupdf.Rect(pills[0]['rect'].x0-1,py0-3,pills[1]['rect'].x1+1,py1+1)
pg.add_redact_annot(zone)
pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
def pill(x0,txt,size):
    w=sans.text_length(txt,fontsize=size)+2*pad
    r=pymupdf.Rect(x0,py0,x0+w,py1)
    pg.draw_rect(r,color=None,fill=fill,radius=0.25)
    return r
t1='31 octobre 2026'; t2='@André-Guy Bruneau'
r1=pill(pills[0]['rect'].x0,t1,dt['size'])
gap_dot=dot['bbox'][0]-pills[0]['rect'].x1; dot_w=dot['bbox'][2]-dot['bbox'][0]; gap2=pills[1]['rect'].x0-dot['bbox'][2]
xdot=r1.x1+gap_dot
r2=pill(xdot+dot_w+gap2,t2,au['size'])
tw=pymupdf.TextWriter(pg.rect)
tw.append((r1.x0+pad,dt['origin'][1]),t1,font=sans,fontsize=dt['size'])
tw.append((r2.x0+pad,au['origin'][1]),t2,font=sans,fontsize=au['size'])
tw.write_text(pg,color=tuple(c/255 for c in (0x0b,0x0b,0x0b)))
tw=pymupdf.TextWriter(pg.rect); tw.append((xdot,dot['origin'][1]),' · ',font=sans,fontsize=dot['size']); tw.write_text(pg,color=tuple(c/255 for c in (0x1f,0x1e,0x1d)))
d.set_metadata({'title':"La ligne directrice de l'AMF sur l'utilisation de l'IA, instruite attente par attente et rapportée aux agents",
 'author':'André-Guy Bruneau','subject':"Profil d'application québécois CRE-IA-2026-01-QC (version 1.0 — 31 octobre 2026)",
 'keywords':'AMF; intelligence artificielle; agents; CRE-IA-2026-01-QC','creator':'Claude Docs (Chromium)','producer':'Skia/PDF m153; PyMuPDF','modDate':pymupdf.get_pdf_now()})
d.save(OUT,garbage=3,deflate=True)
print(N,'pages')
