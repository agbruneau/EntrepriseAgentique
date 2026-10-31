"""Chaîne de composition commune aux livrables du corpus.

HTML structuré -> pandoc 3 (filtre.lua) -> Typst 0.15.1 (gabarit.typ) -> PDF, puis
contrôle que chaque mot du texte source se retrouve dans le PDF.

Un script de document appelle composer() avec :
  - fragments : {nom: html} ; chaque fragment devient <nom>.typ, à inclure par main ;
  - main : le fichier Typst principal (couverture, sommaire, #include des fragments) ;
  - extras : fichiers Typst propres au document, copiés à côté (figures…) ;
  - source_controle : le texte que le PDF doit contenir mot pour mot.
"""
import collections, html, pathlib, re, shutil, subprocess, sys, tempfile, unicodedata
import pymupdf

COMMUN = pathlib.Path(__file__).resolve().parent
DOCUMENTS = COMMUN.parents[1] / 'documents'
MOIS = 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split()
NBSP = ' '


def date_fr(a, m, j):
    return f'{j}{"er" if j == 1 else ""} {MOIS[m - 1]} {a}'


def typographie(fragment):
    """Espaces insécables et apostrophe typographique, dans le texte seulement : ni dans
    les balises, ni dans <code> ou <pre>, dont le contenu reste littéral."""
    def texte(t):
        t = t.replace('&#39;', '’').replace("'", '’')
        t = re.sub(r' ([:;?!»])', NBSP + r'\1', t)
        t = re.sub(r'« ', '«' + NBSP, t)
        t = re.sub(r'§ ', '§' + NBSP, t)
        return t
    morceaux = re.split(r'(<pre\b.*?</pre>|<code\b.*?</code>)', fragment, flags=re.S)
    return ''.join(m if i % 2 else re.sub(r'>([^<]+)<', lambda x: '>' + texte(x.group(1)) + '<', m)
                   for i, m in enumerate(morceaux))


def pandoc(fragment, dest, imports=()):
    subprocess.run(['pandoc', '-f', 'html', '-t', 'typst', '--wrap=none', '--lua-filter', str(COMMUN / 'filtre.lua'),
                    '-o', str(dest)], input=typographie(fragment).encode('utf8'), check=True)
    # pandoc centre ses tableaux (align(center)[...]) : les cellules en héritent
    typ = dest.read_text(encoding='utf8').replace('align(center)[#table(', '[#table(')
    entete = ''.join(f'#import "{i}": *\n' for i in ('gabarit.typ', *imports))
    dest.write_text(entete + typ, encoding='utf8')


def chaine_typst(t):
    return '"' + t.replace('\\', '\\\\').replace('"', '\\"') + '"'


def texte_html(fragment):
    return re.sub(r'<[^>]+>', ' ', html.unescape(fragment))


def mots(t):
    t = unicodedata.normalize('NFC', t).replace('’', "'")
    # l'extraction colle parfois deux cellules voisines (« 2026-10-31Relecture ») :
    # on coupe à chaque passage minuscule ou chiffre -> majuscule, des deux côtés
    t = re.sub(r'(?<=[a-zà-ÿ0-9])(?=[A-ZÀ-Ý])', ' ', t)
    return collections.Counter(re.findall(r"[^\W_]+", t.lower()))


def controler(source, pdf):
    """Chaque mot de la source doit figurer dans le PDF.

    Le PDF est lu mot à mot (deux cellules voisines ne se collent pas), hors en-têtes
    et pieds de page; une césure de Typst laisse un trait conditionnel (U+00AD) en fin
    de ligne, retiré pour recoller le mot. Quand la coupure tombe sur un saut de page
    au milieu d'un tableau, l'en-tête répété s'intercale : le mot compte alors si son
    début (avant le trait conditionnel) et sa fin se trouvent tous deux dans le PDF.
    Les mots se comparent hors traits d'union.
    """
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


def composer(fragments, main, sortie, source_controle, extras=()):
    sortie = pathlib.Path(sortie)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copy(COMMUN / 'gabarit.typ', tmp)
        for f in extras:
            shutil.copy(f, tmp)
        for nom, frag in fragments.items():
            pandoc(frag, tmp / f'{nom}.typ', [pathlib.Path(f).name for f in extras])
        (tmp / 'main.typ').write_text(main, encoding='utf8')
        brouillon = tmp / 'main.pdf'
        subprocess.run(['typst', 'compile', '--root', str(tmp), str(tmp / 'main.typ'), str(brouillon)], check=True)
        pages, manquants = controler(source_controle, brouillon)
        if manquants:
            rejet = sortie.with_name(sortie.stem + ' (rejeté).pdf')
            shutil.copy(brouillon, rejet)
            sys.exit(f'{manquants} mot(s) manquant(s) : {sortie.name} non remplacé, brouillon dans {rejet}')
        shutil.copy(brouillon, sortie)
    print(f'{sortie} : {pages} pages, texte source intégralement présent')
    return pages
