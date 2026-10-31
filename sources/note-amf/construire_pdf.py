"""Compose le PDF de la Note AMF IA à partir de l'export HTML de Claude Docs.

Usage : python construire_pdf.py [source.html] [sortie.pdf]
        (par défaut : note-amf-ia.html -> ../../documents/Note AMF IA.pdf)

Chaîne : HTML -> pandoc 3 (filtre.lua) -> Typst 0.15 (gabarit.typ) -> PDF.
Le script retire de l'HTML la page de titre et la fiche signalétique pour les poser
sur la couverture, remplace le calendrier intégré (absent de l'export) par la figure
du gabarit, insère les espaces insécables de la typographie française, puis contrôle
que chaque mot du texte source se retrouve dans le PDF.
"""
import collections, html, pathlib, re, shutil, subprocess, sys, tempfile, unicodedata
import pymupdf

ICI = pathlib.Path(__file__).resolve().parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ICI / 'note-amf-ia.html'
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ICI.parents[1] / 'documents' / 'Note AMF IA.pdf'
AUTEUR = 'André-Guy Bruneau'  # la mention @u_… de l'export ne se résout pas hors de Claude Docs
MOIS = 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split()
NBSP = ' '


def typographie(fragment):
    """Espaces insécables et apostrophe typographique, dans le texte seulement (pas dans les balises)."""
    def texte(t):
        t = t.replace('&#39;', '’')
        t = re.sub(r' ([:;?!»])', NBSP + r'\1', t)
        t = re.sub(r'« ', '«' + NBSP, t)
        t = re.sub(r'§ ', '§' + NBSP, t)
        return t
    return re.sub(r'>([^<]+)<', lambda m: '>' + texte(m.group(1)) + '<', fragment)


def decouper(s):
    titre = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    sous_titre = re.search(r'<p><em>(.*?)</em></p>', s[titre.end():], re.S)
    date = re.search(r'<time[^>]*datetime="(\d{4})-(\d{2})-(\d{2})"', s)
    fiche = re.search(r'<table>.*?</table>', s, re.S)
    assert titre.start() < fiche.start() and 'Rubrique' in fiche.group(0)
    a, m, j = (int(x) for x in date.groups())
    corps = s[fiche.end():]
    corps, n = re.subn(r'<figure data-embed="[^"]*">.*?</figure>', '<div class="calendrier"></div>', corps, flags=re.S)
    assert n == 1, f'{n} figure(s) intégrée(s); le gabarit n\'en dessine qu\'une'
    return dict(titre=html.unescape(titre.group(1)), sous_titre=html.unescape(sous_titre.group(1)),
                date=f'{j}{"er" if j == 1 else ""} {MOIS[m - 1]} {a}',
                fiche='<div class="fiche">' + fiche.group(0) + '</div>', corps=corps)


def pandoc(fragment, dest):
    subprocess.run(['pandoc', '-f', 'html', '-t', 'typst', '--wrap=none', '--lua-filter', str(ICI / 'filtre.lua'),
                    '-o', str(dest)], input=typographie(fragment).encode('utf8'), check=True)
    # pandoc centre ses tableaux (align(center)[...]) : les cellules en héritent
    typ = dest.read_text(encoding='utf8').replace('align(center)[#table(', '[#table(')
    dest.write_text('#import "gabarit.typ": *\n' + typ, encoding='utf8')


def chaine_typst(t):
    return '"' + t.replace('\\', '\\\\').replace('"', '\\"') + '"'


def mots(t):
    t = unicodedata.normalize('NFC', t).replace('’', "'")
    # l'extraction colle parfois deux cellules voisines (« 2026-10-31Relecture ») :
    # on coupe à chaque passage minuscule ou chiffre -> majuscule, des deux côtés
    t = re.sub(r'(?<=[a-zà-ÿ0-9])(?=[A-ZÀ-Ý])', ' ', t).replace(NBSP, ' ').replace(' ', ' ')
    return collections.Counter(w for w in re.findall(r"[^\W_]+", t.lower()))


def controler(parties, pdf):
    """Chaque mot de la source doit figurer dans le PDF.

    Le PDF est lu mot à mot (deux cellules voisines ne se collent pas); une césure de
    Typst laisse un trait conditionnel (U+00AD) en fin de ligne, retiré pour recoller
    le mot. Quand la coupure tombe sur un saut de page au milieu d'un tableau, l'en-tête
    répété s'intercale : le mot compte alors si son début (avant le trait conditionnel)
    et sa fin se trouvent tous deux dans le PDF. Les mots se comparent hors traits
    d'union. L'en-tête de la fiche signalétique (« Rubrique », « Valeur ») n'est pas
    repris sur la couverture.
    """
    fiche = re.sub(r'<thead>.*?</thead>', '', parties['fiche'], flags=re.S)
    source = ' '.join(re.sub(r'<[^>]+>', ' ', html.unescape(t))
                      for t in (parties['titre'], parties['sous_titre'], fiche, parties['corps']))
    doc = pymupdf.open(pdf)
    corps = lambda p: [w[4] for w in p.get_text('words') if w[1] > 70 and w[3] < p.rect.height - 60]
    rendu = ' '.join(w for p in doc for w in corps(p))
    lu = mots(rendu.replace('­ ', ''))
    debuts = {m.group(1).lower() for m in re.finditer(r'(\w+)­', rendu)}
    manque = mots(source) - lu
    for m in list(manque):
        if any(m.startswith(d) and lu[m[len(d):]] for d in debuts):
            del manque[m]
    if manque:
        print('Mots de la source absents du PDF :', dict(manque.most_common(30)))
    return doc.page_count, sum(manque.values())


def main():
    parties = decouper(SRC.read_text(encoding='utf8'))
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copy(ICI / 'gabarit.typ', tmp)
        pandoc(parties['fiche'], tmp / 'fiche.typ')
        pandoc(parties['corps'], tmp / 'corps.typ')
        titre = parties['titre']
        (tmp / 'note.typ').write_text(f'''#import "gabarit.typ": *
#set document(title: {chaine_typst(titre)},
  description: "Profil d'application québécois CRE-IA-2026-01-QC (version 1.0, {parties['date']})",
  keywords: ("AMF", "intelligence artificielle", "agents", "CRE-IA-2026-01-QC"))
#show: note.with(titre-court: "Note AMF IA", identifiant: "CRE-IA-2026-01-QC", version: "1.0")
#couverture(titre: {chaine_typst(titre.replace("'", '’'))}, sous-titre: {chaine_typst(parties['sous_titre'].replace("'", '’'))},
  auteur: {chaine_typst(AUTEUR)}, date: {chaine_typst(parties['date'])}, fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
''', encoding='utf8')
        brouillon = tmp / 'note.pdf'
        subprocess.run(['typst', 'compile', '--root', str(tmp), str(tmp / 'note.typ'), str(brouillon)], check=True)
        pages, manquants = controler(parties, brouillon)
        if manquants:
            rejet = OUT.with_name(OUT.stem + ' (rejeté).pdf')
            shutil.copy(brouillon, rejet)
            sys.exit(f'{manquants} mot(s) manquant(s) : {OUT.name} non remplacé, brouillon dans {rejet}')
        shutil.copy(brouillon, OUT)
    print(f'{OUT} : {pages} pages, texte source intégralement présent')


if __name__ == '__main__':
    main()
