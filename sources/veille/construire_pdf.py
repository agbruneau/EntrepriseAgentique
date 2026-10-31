"""Recompose le PDF de la Veille technologique à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Veille Technologique.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt : le PDF fait foi, reprise et errata du
29 oct. 2026 compris. sources/commun/extraire.py le relit (PDF balisé; repli géométrique
pour l'annexe du 29 octobre, pp. 145-152, fusionnée sans balisage), puis
sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : titre, sous-titre, auteur et date passent sur la couverture, la
    mention de révision dans la fiche;
  - Résumé et Abstract : leur intitulé en gras devient un titre; l'Abstract est
    composé en anglais (césure);
  - titres : sections (H1) en chapitres, sous-sections (H2) en sections; les
    sous-sous-sections (4.11.1, 4.13.1…), balisées H2 elles aussi, en niveau 4;
  - retouches du 29 octobre (lignes recomposées directement dans le PDF) : l'extraction
    recase leurs lignes, mais quelques frontières de paragraphe ou d'item restent
    déplacées; RECOLLER et SCINDER les rétablissent d'après le rendu d'origine;
  - en-têtes de tableau répétés aux sauts de page : rendus en paragraphes après le
    tableau, ils sont retirés (copies exactes de l'en-tête, vérifiées);
  - Références : le chapeau en italique, recasé dans la référence 1, en ressort; les
    références sont composées en drapeau, comme à l'origine;
  - annexe du 29 octobre : ses références [343] à [371], composées en grille (numéro
    aligné à droite) et relues ligne à ligne par le repli, redeviennent une liste
    numérotée comme celles du corps; césures (trait conditionnel) reprises du PDF;
    leurs liens d'origine, posés par ligne entière, sont remplacés comme au corps;
  - URL : celles que l'origine coupait en fin de ligne sont recollées (l'extraction y
    mettait une espace), puis toutes deviennent des liens, coupés à leurs barres et
    points seulement;
  - tableaux de l'annexe de traçabilité : largeurs de colonnes bornées à la page;
  - légendes « Tableau N. – … » : la numérotation passe à Typst (même suite, contrôlée);
  - gras : celui de la police seulement. Le PDF balise en Strong des passages composés
    en romain (intitulés des constats, de paragraphes, d'items); le rendu d'origine fait foi;
  - code : balise Code et police à chasse fixe -> <code>, laissé littéral par composer.
"""
import atexit, collections, html, pathlib, re, shutil, subprocess, sys, tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as composer_mod
from composer import DOCUMENTS, chaine_typst, composer, mots
from extraire import SHY, controler_extraction, extraire, texte_controle, vers_html, zones_ecartees
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Veille Technologique.pdf'
# Dernière édition d'origine (Typst, retouchée le 29 oct. 2026) : le PDF recomposé ne
# doit pas servir de source à son tour.
ORIGINE = 'd28324a'
OUT = pathlib.Path(args[1]) if len(args) > 1 else SORTIE
if args:
    SRC = pathlib.Path(args[0])
else:
    SRC = pathlib.Path(tempfile.mkdtemp()) / 'origine.pdf'
    atexit.register(shutil.rmtree, SRC.parent, True)
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{SORTIE.name}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

# Écarts connus du contrôle de complétude (mots du PDF d'origine absents de l'extraction) :
#  - en-têtes répétés des tableaux de l'annexe non balisée, que le repli range une seule
#    fois dans le tableau : tableau 25 (« Objet / Au 15 août 2026 / Au 29 octobre 2026 /
#    Réf. », répété pp. 146 et 147) et tableau 26 (« No Où Erreur Correction Traitement »,
#    répété p. 149). Ceux des tableaux balisés sont retirés par entetes_repetes();
#  - p. 1 et 95 : le contrôle lit le PDF mot à mot dans l'ordre du flux; les lignes
#    retouchées y sont rangées en fin de page, si bien que « méca-/nisme », « dé-/posi-
#    taire » se recollent de travers (« mécadécrivent »). L'extraction, qui range par
#    position, a les bons mots (mécanisme, dépositaire, décrivent).
ECARTS_CONNUS = {'no': 1, 'où': 1, 'erreur': 1, 'correction': 1, 'traitement': 1,
                 'objet': 2, 'au': 4, '15': 2, 'août': 2, '2026': 4, '29': 2, 'octobre': 2, 'réf': 2,
                 'mécadécrivent': 1, 'nisme': 1, 'déposi': 1, 'taire': 1}

# Frontières déplacées par les retouches : (avant, après). « recoller » réunit deux blocs
# que l'extraction a séparés ([balise fermante + ouvrante] retirées entre les deux
# chaînes); « scinder » ouvre un bloc avant la chaîne. Chaque retouche doit s'appliquer
# exactement une fois.
RECOLLER = [
    # p. 2, Abstract, 3e paragraphe : « twelve individual / drafts submitted… »
    ('enforceable traceability — twelve individual', ' ', 'drafts submitted to the IETF'),
    # p. 7, constat 2 : « (quatre / SDK Tier-1 en bêta) »
    ('non sa révision courante (quatre', ' ', 'SDK Tier-1 en bêta)'),
    # p. 8, constat 9 : « Au-/delà de deux sauts »
    ('commandité par Token Security</strong>). Au-', '', 'delà de deux sauts, douze'),
    # p. 65, § 7.10 : « revérifié sur le texte le 15 août 2026, / A2A v1.0.0 … »
    ('<em>revérifié sur le texte le 15 août 2026</em>,', ' ', 'A2A v1.0.0 ne mentionne'),
    # p. 76, question 2 : « aucun / adopté : reste lequel, quand »
    ('chaînes à N sauts [162] [276] [277], aucun', ' ', 'adopté : reste <strong>lequel, quand</strong>.'),
]
SCINDER = [
    # Abstract : le 4e paragraphe s'ouvre sur « The edition of 15 August 2026 »
    ('p', 'The edition of 15 August 2026 extends'),
    # Sommaire exécutif : un paragraphe par constat
    ('p', '2. L’adoption précède l’assurance.'),
    ('p', '10. Le corpus compagnon compte'),
    # § 7.10 : « Le fait négatif n'en est que plus net » ouvre un paragraphe
    ('p', 'Le fait négatif n’en est que plus net'),
    # § 11, question 3
    ('li', '<strong>Découverte digne de confiance.</strong>'),
    # § 12.3 : chaque pari ouvre un paragraphe
    ('p', '<strong>La convergence de l’identité.</strong>'),
]


def borner_colonnes(typ):
    """Largeurs de colonnes ramenées à 100 % de la justification quand leur somme
    l'excède. Le filtre commun réserve à chaque colonne son mot le plus long sur une
    ligne; un chemin en <code> (« a2a-protocol.org/latest/specification/ ») y compte pour
    un seul mot, alors que Typst le coupe après « / » ou « - » : dans les tableaux 19 à 21
    (annexe de traçabilité), la somme passe 170 % et le tableau déborde de la page."""
    def borner(m):
        v = [float(x) for x in re.findall(r'([\d.]+)%', m.group(1))]
        if sum(v) <= 100.05:
            return m.group(0)
        return 'columns: (' + ', '.join(f'{x * 100 / sum(v):.2f}%' for x in v) + '),'
    return re.sub(r'columns: \(([^)]*)\),', borner, typ)


_pandoc = composer_mod.pandoc


def pandoc(fragment, dest, imports=()):
    _pandoc(fragment, dest, imports)
    dest.write_text(borner_colonnes(dest.read_text(encoding='utf8')), encoding='utf8')


composer_mod.pandoc = pandoc   # composer() appelle pandoc() par le module


def niveau(n, texte):
    """H1 -> chapitre (2), H2 -> section (3); les sous-sous-sections (4.11.1…), balisées
    H2 dans le PDF, passent au niveau 4."""
    if n == 2 and re.match(r'\d+\.\d+\.\d+\s', texte):
        return 4
    return {1: 2, 2: 3}.get(n, n + 1)


def page_de_titre(pdf):
    """Titre (15 pt), sous-titre (12 pt), ligne auteur · courriel · date, mention de révision."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    titre = next(t for s, t in lignes if s == 15)
    sous_titre = next(t for s, t in lignes if s == 12)
    auteur, courriel, date = next(t for s, t in lignes if '·' in t and '@' in t).split(' · ')
    revision = next(t for s, t in lignes if t.startswith('Révision du'))
    return dict(titre=titre, sous_titre=sous_titre, auteur=auteur, courriel=courriel, date=date, revision=revision)


def retoucher(s):
    for avant, joint, apres in RECOLLER:
        motif = re.escape(avant) + r'</(p|li)>\n<\1>' + re.escape(apres)
        assert len(re.findall(motif, s)) == 1, f'retouche introuvable : {avant!r}'
        s = re.sub(motif, lambda m: avant + joint + apres, s)
    for balise, debut in SCINDER:
        assert s.count(debut) == 1, f'scission introuvable : {debut!r}'
        i = s.index(debut)
        s = s[:i].rstrip(' ') + f'</{balise}>\n<{balise}>' + s[i:]
    return s


def lignes_cesurees(pdf, pages):
    """Texte (sans trait conditionnel, blancs réduits) des lignes du PDF qui finissent par
    une césure : le repli les rend en paragraphes séparés, sans le trait."""
    doc, fins = pymupdf.open(pdf), set()
    for i in pages:
        for b in doc[i].get_text('dict')['blocks']:
            for l in b.get('lines', []):
                t = ''.join(s['text'] for s in l['spans']).rstrip()
                if t.endswith(SHY):
                    fins.add(' '.join(t.replace(SHY, '').split()))
    return fins


def references_reprise(s, cesures):
    """Références [343] à [371] : une ligne du PDF par <p> -> <ol start="343">."""
    debut = s.index('<h3>Références de la reprise</h3>\n') + len('<h3>Références de la reprise</h3>\n')
    lignes = re.findall(r'<p>(.*?)</p>\n?', s[debut:])
    assert ''.join(f'<p>{l}</p>\n' for l in lignes).rstrip('\n') == s[debut:].rstrip('\n'), \
        'références de la reprise : bloc inattendu'
    # au saut de page, la dernière ligne d'une page et la première de la suivante (une
    # référence neuve) se suivent dans le même <p> : on les sépare
    lignes = [re.sub(r'</?a\b[^>]*>', '', l) for l in lignes]   # liens posés sur la ligne entière
    lignes = [x for l in lignes for x in re.split(r' (?=3[4-7]\d\. [A-Z])', l)]
    refs = []
    for l in lignes:
        brut = ' '.join(html.unescape(re.sub(r'<[^>]+>', '', l)).split())
        m = re.match(r'(\d+)\. ', l)
        if m and int(m.group(1)) == 343 + len(refs):
            refs.append([l[m.end():], brut])
            continue
        assert refs, l
        fin, prec = refs[-1][0].rstrip(), refs[-1][1]
        if prec in cesures:
            joint = ''
        elif prec.endswith(('-', '/')) and brut[:1].isalnum():
            joint = ''   # trait d'union, URL ou chemin en <code> coupés : gardés tels quels
        else:
            joint = ' '
        refs[-1] = [fin + joint + l.lstrip(), brut]
    assert len(refs) == 371 - 342, len(refs)
    corps = '\n'.join(f'<li><p>{r}</p></li>' for r, _ in refs)
    # balises de style adjacentes après recollage (<code>a</code><code>b</code>)
    corps = re.sub(r'</(code|em|strong)><\1>', '', corps)
    return s[:debut] + f'<ol start="343">\n{corps}\n</ol>'


def recoller_url(s):
    """URL coupée en fin de ligne dans l'édition d'origine (Typst coupe les liens sans
    trait : « https://cloudsecurit / yalliance.org/… ») : l'extraction, qui joint deux
    lignes par une espace, l'a scindée. On recolle quand la suite a l'allure d'une URL
    (point, barre, trait, égal ou chiffre) et que l'URL ne finit pas sur une ponctuation;
    une URL qui finit sur un point (« https://arxiv. / org/abs/… ») se recolle à toute
    suite en minuscule ou en chiffre (une phrase neuve prend la majuscule)."""
    motif = re.compile(r'(https?://[^\s<>"]*[^\s<>",;:)\]]) (?=([^\s<>"]+))')

    def suite(m):
        u, n = m.groups()
        if u.endswith('.'):
            return m.group(1) if n[:1].islower() or n[:1].isdigit() else m.group(0)
        if n[:1].isupper() or n[:1] in '«([—–' or not re.search(r'[./=\d-]', n):
            return m.group(0)
        return m.group(1)
    while True:
        s2 = motif.sub(suite, s)
        if s2 == s:
            return s
        s = s2


def lier_url(s):
    """URL du texte courant -> liens, que la règle show link de main.typ ne coupe qu'à
    leurs barres, points et traits (en texte simple, Typst les césure). Hors <code> et
    hors balises existantes."""
    def lier(m):
        u = m.group(0).rstrip('.,;:)»')
        return f'<a href="{u}">{u}</a>' + m.group(0)[len(u):]
    morceaux = re.split(r'(<code\b.*?</code>|<a\b.*?</a>|<[^>]+>)', s, flags=re.S)
    return ''.join(m if i % 2 else re.sub(r'https?://[^\s<>"]+', lier, m) for i, m in enumerate(morceaux))


def entetes_repetes(s):
    """En-têtes de tableau répétés aux sauts de page : le PDF ne les range pas dans le
    tableau, l'extraction en fait des paragraphes à la suite de celui-ci (une ou plusieurs
    copies, parfois sur plusieurs lignes). On retire les <p> qui suivent un tableau tant
    que leur texte, mis bout à bout, reproduit exactement son en-tête, une fois ou plus.
    Rend le HTML et les mots retirés (que le contrôle de complétude tolère)."""
    texte = lambda t: ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split())
    lignes, out, retires = s.split('\n'), [], []
    i = 0
    while i < len(lignes):
        out.append(lignes[i])
        m = re.search(r'<thead>(.*?)</thead>', lignes[i]) if lignes[i].startswith('<table>') else None
        i += 1
        if not m:
            continue
        tete, acc, fin = texte(m.group(1)), '', None
        j = i
        while j < len(lignes) and lignes[j].startswith('<p>'):
            acc = (acc + ' ' + texte(lignes[j])).strip()
            if not ' '.join([tete] * 9).startswith(acc):
                break
            j += 1
            if acc in {' '.join([tete] * k) for k in range(1, 9)}:
                fin = j
        if fin:
            retires += lignes[i:fin]
            i = fin
    return '\n'.join(out), retires


def corps(blocs, p):
    # la page de titre : bloc du titre et mention de révision, repris sur la couverture
    assert p['titre'] in blocs[0].html and p['revision'] in blocs[1].html, 'page de titre inattendue'
    s, retires = entetes_repetes(retoucher('\n'.join(b.html for b in blocs[2:])))
    h = s.split('\n')
    # Résumé, Abstract : intitulé en gras de tête -> titre; l'Abstract court jusqu'aux
    # mots-clés
    for i, b in enumerate(h):
        m = re.match(r'<p><strong>(Résumé|Abstract)</strong> ', b)
        if m:
            h[i] = f'<h2>{m.group(1)}</h2>\n<p>' + b[m.end():]
    debut = next(i for i, b in enumerate(h) if b.startswith('<h2>Abstract'))
    fin = next(i for i, b in enumerate(h) if i > debut and b.startswith(('<h2>', '<p><strong>Mots-clés')))
    h[debut:fin] = [h[debut].split('\n', 1)[0], '<div lang="en">', h[debut].split('\n', 1)[1], *h[debut + 1:fin],
                    '</div>']
    s = '\n'.join(h)
    # Références : le chapeau en italique, recasé dans la référence 1, passe devant la liste
    m = re.search(r'<h2>Références</h2>\n<ol>\n<li><p>(<em>Plusieurs références renvoient[^<]*</em>) ', s)
    assert m, 'chapeau des références introuvable'
    s = s[:m.start()] + f'<h2>Références</h2>\n<p>{m.group(1)}</p>\n<ol>\n<li><p>' + s[m.end():]
    return references_reprise(s, lignes_cesurees(SRC, range(144, 152))), retires


def legendes(s):
    # légendes : « Tableau N. – » laisse la place à la numérotation de Typst
    nums = [int(n) for n in re.findall(r'<caption>Tableau\xa0(\d+)\.\xa0– ', s)]
    assert nums == list(range(1, len(nums) + 1)) and s.count('<caption>') == len(nums), nums
    return re.sub(r'<caption>Tableau\xa0\d+\.\xa0– ', '<caption>', s)


def main():
    blocs = extraire(SRC, niveaux=niveau, styles_balises={'Em': 'em', 'Code': 'code'})
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    p = page_de_titre(SRC)
    texte, retires = corps(blocs, p)
    if HTML:
        HTML.with_suffix('.corps.html').write_text(texte, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) doit se retrouver dans l'extraction mise en forme. Le contrôle porte sur
    # le HTML retouché : le repli rend les références de la reprise ligne à ligne, sans
    # leurs traits conditionnels (« sep / tembre »), que references_reprise() recolle.
    # Tolérés : les écarts connus et les en-têtes répétés retirés (copies vérifiées).
    manque, _ = controler_extraction(SRC, blocs[0].html + blocs[1].html + texte, ecarter=zones_ecartees(SRC))
    tolere = mots(' '.join(texte_controle(r) for r in retires)) + collections.Counter(ECARTS_CONNUS)
    inexplique = {m: n for m, n in manque.items() if n > tolere[m]}
    if inexplique:
        sys.exit(f'extraction incomplète : {inexplique}')
    inutiles = {m: n for m, n in tolere.items() if manque[m] < n}
    assert not inutiles, f'écarts tolérés qui ne se produisent pas : {inutiles}'
    print(f'extraction : {len(blocs)} blocs, {len(retires)} lignes d’en-tête répété retirées;'
          f' écarts connus seulement ({sum(manque.values())} mots)')
    # URL rescindées : recollées après le contrôle (l'origine les porte coupées), en ne
    # retirant que des espaces
    recolle = recoller_url(texte)
    assert recolle.replace(' ', '') == texte.replace(' ', ''), 'recollage des URL : texte altéré'
    print(f'URL recollées : {texte.count(" ") - recolle.count(" ")}')
    texte = lier_url(legendes(recolle))
    revision = p['revision'].removeprefix('Révision du ').strip()
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(p["auteur"])} · {html.escape(p["courriel"])}</td></tr>'
             f'<tr><td>Faits gelés au</td><td>{html.escape(p["date"])}</td></tr>'
             f'<tr><td>Révision</td><td>{html.escape(revision)}</td></tr>'
             '</tbody></table></div>')
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#set document(title: {chaine_typst(p['titre'])},
  description: "{p['sous_titre']}. Faits gelés au {p['date']}; reprise datée et errata du 29 octobre 2026 en annexe.",
  keywords: ("veille technologique", "agents", "interopérabilité", "orchestration", "MCP", "A2A"))
#show: note.with(titre-court: "Veille technologique", pied: [Faits gelés au {p['date']} · révision du 29 octobre 2026])
// légendes au-dessus des tableaux, comme dans l'édition d'origine, et jamais seules
// en bas de page
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
// URL : coupées à leurs barres, points et traits seulement. Typst coupe sinon un lien
// n'importe où, sans trait (« cloudsecurityallia / nce »), ce qui le rend illisible et
// que le contrôle mot à mot ne peut recoller : chaque segment alphanumérique est mis
// en boîte.
#show link: it => {{
  show regex("[\\\\p{{L}}\\\\p{{N}}_]+"): box
  it
}}
#couverture(surtitre: [Veille technologique], titre: {typo(p['titre'])},
  sous-titre: {typo(p['sous_titre'])}, auteur: {chaine_typst(p['auteur'])}, date: {chaine_typst(p['date'])},
  fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
// références : en drapeau, comme dans l'édition d'origine (URL longues)
#[#set par(justify: false, linebreaks: "simple")
#include "references.typ"]
#include "reprise.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-reprise.typ"]
'''
    source = ' '.join(texte_controle(t) for t in (p['titre'], p['sous_titre'], fiche, texte))
    # quatre fragments : corps, références, annexe de la reprise, ses références
    a = texte.index('<h2>Références</h2>')
    b = texte.index('<h2>Annexe : reprise du 29 octobre 2026</h2>')
    c = texte.index('<h3>Références de la reprise</h3>')
    assert a < b < c
    fragments = {'fiche': fiche, 'corps': texte[:a], 'references': texte[a:b], 'reprise': texte[b:c],
                 'references-reprise': texte[c:]}
    composer(fragments, main_typ, OUT, source)


if __name__ == '__main__':
    main()
