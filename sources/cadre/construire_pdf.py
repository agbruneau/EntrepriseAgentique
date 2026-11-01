"""Recompose le Cadre de référence CRE-IA-2026-01 à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, imprimée par Chrome, lue dans git au commit
        ORIGINE, recomposée dans documents/Cadre de Référence.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt : le PDF fait foi. sources/commun/extraire.py
relit son balisage, sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - balisage de Chrome : en-tête courant (y ≈ 33) et pied (y ≈ 750) écartés par les
    marges; le pied, rangé sous le H1 du chapitre suivant, rend ces H1 « multipages »;
  - page de titre et fiche du document (p. 1-2) : couverture et fiche du gabarit;
    l'historique des versions et la méthode restent en préambule;
  - table des matières, listes des tableaux et des figures (p. 5-10) : régénérées;
    les listes d'origine servent à contrôler les légendes et donnent le titre court
    des figures;
  - titres : parties (H1 « Fondements »…) au niveau 1, chapitres et annexes (H1) au
    niveau 2, puis H2 -> 3, H3 -> 4, H4 -> 5;
  - schémas (28 Figure) : recadrés en PDF vectoriel depuis la page d'origine et
    intégrés tels quels (texte compris), légende reprise;
  - légendes « Tableau N — … » (paragraphes en gras avant le tableau) : remises en
    légende; numéros gardés en toutes lettres, sans numérotation de Typst;
  - blocs d'exigence (EXIG-XXX-NN) et encadrés (À RETENIR, ATTENTION…) : regroupés
    selon le rectangle de fond qui les contient dans l'original, puis stylés;
  - blocs de code (NonStruct en chasse fixe) : <pre>, ligne visuelle par ligne
    (retours de Chrome gardés, corps réduit pour que la plus longue tienne);
  - code en ligne : pastilles de Chrome lues sans leur marge interne (extracteur
    commun, pastilles=True); renvois d'exigences de la grille d'homologation (lus en
    exposant) remis en fin d'item;
  - Typst (schemas.typ) : code en ligne long coupé seulement après « / » ou « - »;
  - « André-Guy » : le « é » est un span à part, suivi d'un blanc.

Contrôles : complétude de l'extraction (écarts connus listés), recadrage sans perte
du texte des schémas, retouches du script sans perte, contrôle mot à mot de
composer(), numéros des tableaux et des figures conformes aux listes d'origine.

Actualisation du 1er novembre 2026 : annexe H, informative, rédigée en HTML dans ce dossier
(actualisation-2026-11.html) et composée après l'annexe G; ses tableaux et ses références
continuent les suites du document (tableau 70, référence 474). Elle ne modifie aucune exigence.
"""
import atexit, collections, html, pathlib, re, shutil, subprocess, sys, tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as C
from composer import ACTUALISATION, DOCUMENTS, actualisation, chaine_typst, composer, mots
from extraire import MONO, Extracteur, cadre, controler_extraction, texte_controle, vers_html, zones_ecartees
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Cadre de Référence.pdf'
# Édition d'origine (Chrome, 28 oct. 2026) : le PDF recomposé ne doit pas servir de
# source à son tour. Elle porte, au commit ORIGINE, le nom long du document (renommé
# le 31 oct. 2026).
ORIGINE = 'd28324a'
NOM_ORIGINE = 'Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf'
OUT = pathlib.Path(args[1]) if len(args) > 1 else SORTIE
if args:
    SRC = pathlib.Path(args[0])
else:
    SRC = pathlib.Path(tempfile.mkdtemp()) / 'origine.pdf'
    atexit.register(shutil.rmtree, SRC.parent, True)
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{NOM_ORIGINE}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

MARGES = (50, 50)          # en-tête courant à y ≈ 33-42, pied à y ≈ 750; texte entre 57 et 728
PAGES_TDM = range(4, 10)   # p. 5 à 10 : table des matières, listes des figures et des tableaux
PREAMBULE = ('Fiche du document', 'Historique des versions', 'Méthode et avertissements')
PARTIES = ('Fondements', 'Architecture, interopérabilité et orchestration', 'Confiance et exploitation',
           'Gouvernance, conformité et mise en œuvre', 'Outils d’application')
LARGEUR = 468              # justification du gabarit (pt)
EXIG = re.compile(r'EXIG-[A-Z0-9]{3}-\d{2}')

# Écarts connus du contrôle de complétude (les en-têtes de tableau répétés, absorbés par
# l'extracteur, en sont soustraits) : « André » (p. 1 et 2) est composé de deux spans
# séparés par un blanc; le PDF se lit « Andr » + « é », l'extraction donne « André ».
ECARTS_CONNUS = {'andr': 2, 'é': 2}


def niveau(n, texte):
    t = re.sub(r'\s+', ' ', texte).strip()
    if n == 1:
        return 1 if t in PARTIES else 2
    if n == 2 and t in PREAMBULE:
        return 2
    return n + 1


class Cadre(Extracteur):
    """Extracteur commun, plus trois traitements propres au balisage de Chrome : schémas
    (Figure) rendus en image, blocs de code, regroupement des encadrés."""

    def __init__(self, pdf, **params):
        super().__init__(pdf, **params)
        self.cadres = {}            # clé de Figure intérieure -> (page, Rect de structure)
        self.schemas = []           # [(clé intérieure, page, Rect)], dans l'ordre du texte
        self.fonds = {}             # page -> rectangles de fond pleins, larges

    def lire_page(self, page):
        def marcher(b, chemin):
            if b['type'] != 2:
                return
            cle = chemin + (b['index'],)
            enfants = [c for c in b.get('blocks', []) if c['type'] == 2]
            if b.get('raw') == 'Figure' and not any(c.get('raw') == 'Figure' for c in enfants):
                assert cle not in self.cadres, f'figure sur deux pages : {cle}'
                self.cadres[cle] = (page.number, pymupdf.Rect(b['bbox']))
            for c in b.get('blocks', []):
                marcher(c, cle)
        for b in page.get_text('dict', flags=pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            marcher(b, ())
        self.fonds[page.number] = [it['rect'] for it in page.get_drawings()
                                   if it.get('fill') and it['rect'].width > 300 and it['rect'].height > 15]
        return super().lire_page(page)

    # les lignes d'un schéma sont éparses : le recasement les disperserait
    def recaser(self):
        figs = self.feuilles & set(self.cadres)
        self.feuilles -= figs
        super().recaser()
        self.feuilles |= figs

    def code(self, cle):
        """Bloc en chasse fixe sur plusieurs lignes : texte ligne à ligne, blancs de tête
        gardés (Chrome les conserve, pre-wrap)."""
        runs = [r for r in self.runs_de(cle) if r.texte.strip()]
        if not runs or not all(MONO.search(r.police) for r in runs):
            return None
        lignes = self.lignes_visuelles(self.runs_de(cle))
        if len(lignes) < 2:
            return None
        texte = '\n'.join(''.join(r.texte for r in l).rstrip() for l in lignes)
        return '<pre><code>' + html.escape(texte, quote=False) + '</code></pre>'

    def rendre(self, cle, legende=None):
        n = self.noeuds[cle]
        interieures = [c for c in n.enfants if c in self.cadres]
        if n.role == 'Figure' and interieures:
            autres = [c for c in n.enfants if c not in interieures and self.noeuds[c].role != 'Caption'
                      and self.runs_de(c)]
            assert len(interieures) == 1 and not autres, f'figure inattendue : {cle}'
            cap = next(c for c in n.enfants if self.noeuds[c].role == 'Caption')
            p, r = self.cadres[interieures[0]]
            self.schemas.append((interieures[0], p, r))
            k = len(self.schemas)
            return (f'<figure><img src="schema-{k:02}.pdf"><figcaption>{self.en_ligne_html(cap)}'
                    '</figcaption></figure>')
        if cle in self.feuilles and n.role not in ('TD', 'TH', 'LI', 'LBody', 'Caption') \
                and not re.fullmatch(r'H\d?', n.role):
            h = self.code(cle)
            if h:
                return h
        return super().rendre(cle, legende)

    def rendre_suite(self, enfants, legende=None):
        out = super().rendre_suite(enfants, legende)
        if out and self.noeuds[out[0][0]].parent in self.racines:
            out = self.encadrer(out)
        return out

    def fond(self, cle):
        """Rectangle de fond (page, Rect) qui contient le début d'un bloc, s'il y en a un."""
        runs = [r for r in self.runs_de(cle) if r.texte.strip()]
        if not runs:
            return None
        r0 = min(runs, key=lambda r: (r.page, r.bbox[1], r.bbox[0]))
        x, y = (r0.bbox[0] + r0.bbox[2]) / 2, (r0.bbox[1] + r0.bbox[3]) / 2
        dedans = [f for f in self.fonds.get(r0.page, ()) if f.x0 <= x <= f.x1 and f.y0 <= y <= f.y1]
        return (r0.page, min(dedans, key=lambda f: f.width * f.height)) if dedans else None

    def encadrer(self, out):
        """Blocs consécutifs posés sur un même fond -> un <div> (exigence ou encadré).
        Un fond coupé par un saut de page continue en tête de la page suivante."""
        groupes = []
        for cle, h in out:
            f = None if re.match(r'<(table|figure|h\d|pre)', h) else self.fond(cle)
            g = groupes[-1] if groupes else None
            # une exigence ouvre toujours son propre groupe (deux exigences voisines
            # de part et d'autre d'un saut de page ne se fondent pas)
            neuve = EXIG.match(re.sub(r'<[^>]+>', '', h).strip())
            if f and g and g[0] and not neuve and not g[2]:
                (p0, r0), (p1, r1) = g[0], f
                meme = p0 == p1 and r0 == r1
                suite = p1 == p0 + 1 and r0.y1 > 792 - MARGES[1] - 30 and r1.y0 < MARGES[0] + 30
                if meme or suite:
                    g[0] = f
                    g[1].append((cle, h))
                    continue
            groupes.append([f, [(cle, h)], bool(neuve)])
        res = []
        for f, items, _ in groupes:
            if not f:
                res += items
                continue
            corps = '\n'.join(h for _, h in items)
            texte = re.sub(r'<[^>]+>', '', corps)
            genre = 'exig' if EXIG.match(texte.strip()) else 'encadre'
            if genre == 'exig':
                corps = re.sub(r'<p>(Pourquoi\s:.*?)</p>', lambda m: f'<div id="pourquoi-{len(res)}"><p>{m.group(1)}</p></div>',
                               corps, flags=re.S)
            res.append((items[0][0], f'<div id="{genre}-{len(res)}">\n{corps}\n</div>'))
        return res


def recadrer(src, p, rect, dest, runs_rect):
    """Schéma de la page p, recadré (texte et tracés hors cadre retirés), réduit au
    besoin à la justification du gabarit."""
    r = pymupdf.Rect(rect)
    if runs_rect:
        r |= runs_rect
    # les tracés débordent parfois du rectangle de structure (figure 15) : on prend
    # ceux qui le chevauchent, sauf un fond plus grand que la figure elle-même
    coeur = r + (2, 2, -2, -2)
    for it in src[p].get_drawings():
        d = it['rect']
        if d.intersects(coeur) and d.get_area() < 1.5 * r.get_area():
            r |= d
    r = (r + (-4, -4, 4, 4)) & src[p].rect
    tmp = pymupdf.open()
    tmp.insert_pdf(src, from_page=p, to_page=p)
    pg = tmp[0]
    W, H = pg.rect.width, pg.rect.height
    for z in ((0, 0, W, r.y0), (0, r.y1, W, H), (0, r.y0, r.x0, r.y1), (r.x1, r.y0, W, r.y1)):
        pg.add_redact_annot(pymupdf.Rect(z))
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE, graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
    s = min(1, (LARGEUR - 6) / r.width)
    out = pymupdf.open()
    page = out.new_page(width=r.width * s, height=r.height * s)
    page.show_pdf_page(page.rect, tmp, 0, clip=r)
    out.save(dest, garbage=4, deflate=True)
    return ' '.join(w[4] for w in pymupdf.open(dest)[0].get_text('words'))


def couverture(pdf):
    """Page de titre : surtitre (espacé), titre (31 pt), sous-titre (12 pt)."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    surtitre = 'Cadre de référence d’architecture d’entreprise'
    espace = next(t for s, t in lignes if s == 9)
    assert re.sub(r'\s', '', espace).lower() == re.sub(r'\s', '', surtitre).lower(), espace
    titre = ' '.join(t for s, t in lignes if s == 31)
    sous_titre = ' '.join(t for s, t in lignes if s == 12)
    return dict(surtitre=surtitre, titre=titre, sous_titre=sous_titre)


def listes_origine(blocs):
    """Entrées « Tableau N — titre » et « Figure N — titre » des listes d'origine (p. 9-10)."""
    t = html.unescape(re.sub(r'<[^>]+>', '\n', '\n'.join(b.html for b in blocs if b.page in PAGES_TDM)))
    lire = lambda genre: [(int(n), re.sub(r'\s+', ' ', x).strip()) for n, x in
                          re.findall(rf'^{genre}\s(\d+)\s—\s(.+?)\s+\d+\s*$', t, flags=re.M)]
    return lire('Tableau'), lire('Figure')


def corps(blocs, tableaux, figures):
    h = [b.html for b in blocs if b.page not in PAGES_TDM and b.page > 0]
    # p. 2 : la fiche du document passe sur la couverture
    s = '\n'.join(h)
    m = re.match(r'<h2>Fiche du document</h2>\s*(<table>.*?</table>)\s*', s, re.S)
    assert m, s[:200]
    fiche, s = m.group(1), s[m.end():]
    s = s.replace('André -Guy', 'André-Guy')
    fiche = fiche.replace('André -Guy', 'André-Guy')
    # légendes de tableaux : paragraphe en gras juste avant le tableau
    s, k = re.subn(r'<p><strong>(Tableau\xa0?\s?\d+ — [^<]*)</strong></p>\s*<table>',
                   lambda m: f'<table><caption>{m.group(1)}</caption>', s)
    legendes = [(int(n), re.sub(r'\s+', ' ', html.unescape(t)).strip())
                for n, t in re.findall(r'<caption>Tableau\s(\d+) — ([^<]*)</caption>', s)]
    assert [n for n, _ in legendes] == list(range(1, len(legendes) + 1)), legendes
    assert legendes == tableaux, set(legendes) ^ set(tableaux)
    # légendes de figures : « Figure N — titre court. Explication… »
    caps = [html.unescape(re.sub(r'<[^>]+>', '', c)).replace('\xa0', ' ')
            for c in re.findall(r'<figcaption>(.*?)</figcaption>', s, re.S)]
    assert len(caps) == len(figures) and all(c.startswith(f'Figure {n} — {t}') for c, (n, t) in zip(caps, figures)), \
        [(c[:50], t) for c, (n, t) in zip(caps, figures) if not c.startswith(f'Figure {n} — {t}')]
    # parties : « PARTIE I » espacé + H1 -> un titre de niveau 1; le chapitre suivant
    # commence sur une page neuve
    def partie(m):
        libelle = re.sub(r'\s', '', m.group(1))
        libelle = 'Annexes' if libelle == 'ANNEXES' else 'Partie ' + libelle[len('PARTIE'):]
        return f'<h1>{libelle} — {m.group(2)}</h1>'
    s, np = re.subn(r'<p><strong>((?:P ?A ?R ?T ?I ?E [IVX ]+?)|(?:A ?N ?N ?E ?X ?E ?S))</strong></p>\s*<h1>([^<]*)</h1>',
                    partie, s)
    assert np == len(PARTIES), np
    s = re.sub(r'(<h1>.*?</h1>.*?)(?=<h2>)', r'\1<div data-typst="pagebreak(weak: true)"></div>\n', s, flags=re.S)
    # exigences : identifiant et degré d'obligation sur une ligne
    s, nx = re.subn(r'(<div id="exig-\d+">\n)<p><strong><code>(EXIG-[A-Z0-9]{3}-\d{2})</code></strong></p>\n'
                    r'<p><strong>((?:NE )?(?:DOIT|DEVRAIT|PEUT)(?: PAS)?)</strong></p>',
                    r'\1<p><strong><code>\2</code> · \3</strong></p>', s)
    assert nx == s.count('<div id="exig-'), (nx, s.count('<div id="exig-'))
    # dates « 27 oct. 2026 » insécables (colonne Date de l'historique)
    s = re.sub(r'(\d{1,2}) ([a-zéû]{3,5}\.) (\d{4})', '\\1\xa0\\2\xa0\\3', s)
    # espace ordinaire collée à une insécable (lien voisin d'un « : ») : une seule
    morceaux = re.split(r'(<pre\b.*?</pre>)', s, flags=re.S)
    s = ''.join(m if i % 2 else re.sub(r' ?\xa0 ?', '\xa0', m) for i, m in enumerate(morceaux))
    # grille d'homologation (annexe A) : les renvois d'exigences, alignés à droite sur la
    # première ligne de l'item, sont lus comme un exposant en milieu de phrase; ils
    # passent en fin d'item
    def renvoi(m):
        r = re.search(r'\s*<code><sup>([^<]*)</sup></code>\s*', m.group(1))
        return f'<li>{m.group(1)[:r.start()]} {m.group(1)[r.end():]} — <code>{r.group(1)}</code></li>'
    s, nr = re.subn(r'<li>((?:(?!</li>).)*<code><sup>(?:(?!</li>).)*)</li>', renvoi, s, flags=re.S)
    assert nr == 49 and '<code><sup>' not in s, nr
    # références : en drapeau (longues URL)
    i = s.index('<h2>G Références</h2>') + len('<h2>G Références</h2>')
    s = s[:i] + '\n<div id="references">\n' + s[i:] + '\n</div>'
    debut = s.index('<h2>Méthode et avertissements</h2>')
    fin = s.index('<h2>', debut + 1)
    return fiche, s[:fin], s[fin:]


def main():
    e = Cadre(SRC, niveaux=niveau, marges=MARGES, pastilles=True)
    blocs = e.extraire()
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    src = pymupdf.open(SRC)

    # schémas : recadrés depuis l'original, texte compris
    travail = pathlib.Path(tempfile.mkdtemp())
    atexit.register(shutil.rmtree, travail, True)
    extras, texte_schemas = [], []
    for k, (cle, p, r) in enumerate(e.schemas, 1):
        runs = [x.bbox for x in e.runs_de(cle) if x.page == p]
        f = travail / f'schema-{k:02}.pdf'
        texte_schemas.append(recadrer(src, p, r, f, pymupdf.Rect(cadre(runs)) if runs else None))
        extras.append(f)
    schemas_mots = mots(' '.join(texte_schemas))
    figures_mots = collections.Counter()
    for cle, _, _ in e.schemas:
        figures_mots += mots(' '.join(x.texte for x in e.runs_de(cle)))
    # le recadrage garde tout le texte balisé du schéma
    perdu = figures_mots - schemas_mots
    if perdu:
        sys.exit(f'recadrage des schémas incomplet : {dict(perdu)}')

    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) se retrouve dans l'extraction ou dans un schéma, aux écarts connus près
    ecarter = zones_ecartees(SRC) + [(i, src[i].rect) for i in PAGES_TDM]
    manque, surplus = controler_extraction(SRC, brut, marges=MARGES, ecarter=ecarter)
    manque -= figures_mots
    inexplique = manque - collections.Counter(ECARTS_CONNUS)
    if inexplique:
        sys.exit(f'extraction incomplète : {dict(inexplique.most_common(40))}')
    print(f'extraction : {len(blocs)} blocs, {len(e.schemas)} schémas; écarts connus seulement'
          f' ({sum(manque.values())} mots)')

    p = couverture(SRC)
    tableaux, figures = listes_origine(blocs)
    assert len(tableaux) == 69 and len(figures) == len(e.schemas) == 28, (len(tableaux), len(figures))
    fiche_html, preambule, texte = corps(blocs, tableaux, figures)
    rangs = re.findall(r'<tr><th>(?:<strong>)?(.*?)(?:</strong>)?</th><td>(.*?)</td></tr>', fiche_html)
    assert len(rangs) == 10, rangs
    fiche = ('<div class="fiche"><table><tbody>' +
             ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rangs) +
             f'<tr><td>Actualisation</td><td>{ACTUALISATION}, annexe H (informative)</td></tr>'
             '</tbody></table></div>')
    annexe, refs_annexe = actualisation(ICI)
    champs = {html.unescape(a): html.unescape(re.sub(r'<[^>]+>', '', b)) for a, b in rangs}
    version, date = champs['Version et date'].split(' — ')

    (travail / 'schemas.typ').write_text(SCHEMAS_TYP.replace('%FIGURES%', ', '.join(
        chaine_typst(C.typographie(f'>Figure {n} — {t}<')[1:-1]) for n, t in figures)), encoding='utf8')
    extras.append(travail / 'schemas.typ')
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#import "schemas.typ": *
#set document(title: {chaine_typst(p['titre'])},
  description: "Cadre de référence d’architecture d’entreprise {champs['Identifiant normatif']}, version {version}, {date}.",
  keywords: ("IA agentique", "interopérabilité", "orchestration", "MCP", "A2A", "OAuth", "OpenTelemetry", "Loi 25", "gouvernance"))
#show: note.with(titre-court: "{champs['Identifiant normatif']} · Cadre de référence",
  pied: [Version {version} · {date} · actualisation du {ACTUALISATION}])
#show: regles
#couverture(surtitre: {typo(p['surtitre'])}, titre: text(hyphenate: false, {typo(p['titre'])}),
  sous-titre: text(hyphenate: false, {typo(p['sous_titre'])}), auteur: {chaine_typst(champs['Auteur'])}, date: [Version {version} · {date}],
  fiche: include "fiche.typ")
#include "preambule.typ"
#sommaire()
#listes()
#include "corps.typ"
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    source = ' '.join(texte_controle(t) for t in (p['surtitre'], p['titre'], p['sous_titre'], fiche, preambule, texte,
                                                  annexe, refs_annexe))
    source += ' ' + ' '.join(texte_schemas)
    if HTML:
        HTML.with_suffix('.schemas.txt').write_text('\n'.join(texte_schemas), encoding='utf8')
        HTML.with_suffix('.source.txt').write_text(source, encoding='utf8')
    # les retouches du script ne perdent rien : tout mot de l'extraction (hors table des
    # matières, couverture) se retrouve dans la source composée
    perte = mots(texte_controle(vers_html([b for b in blocs if b.page not in PAGES_TDM and b.page > 0]))) - mots(source)
    # libellés de partie réécrits (« PA R T I E I V », « A N N E X E S »)
    perte -= mots('PA R T I E I V X A N N E X E S ' * 5)
    perte -= mots('Fiche du document')   # titre de la p. 2 : la fiche passe sur la couverture
    assert not perte, perte
    composer({'fiche': fiche, 'preambule': preambule, 'corps': texte, 'actualisation': annexe,
              'references-actualisation': refs_annexe}, main_typ, OUT, source, extras=extras)
    verifier_numeros(OUT, tableaux, figures)


def verifier_numeros(pdf, tableaux, figures):
    """Les légendes du PDF composé portent les numéros d'origine, dans l'ordre."""
    t = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf)).replace('­', ''))
    for genre, liste in (('Tableau', tableaux), ('Figure', figures)):
        for n, titre in liste:
            assert t.count(f'{genre} {n} — {titre}') >= 2, f'{genre} {n} introuvable (légende et liste)'
    print(f'numérotation : {len(tableaux)} tableaux et {len(figures)} figures, légendes et listes conformes')


SCHEMAS_TYP = r'''// Règles propres au Cadre de référence, appliquées après #show: note.
#import "gabarit.typ": *
#let titres-figures = (%FIGURES%,)

#let regles(body) = {
  // numéros des tableaux et figures : ceux de l'original, en toutes lettres
  set figure(numbering: none)
  show figure.where(kind: table): set figure.caption(position: top)
  show figure.caption.where(position: top): it => block(sticky: true, it)
  show figure.where(kind: image): set block(above: 14pt, below: 16pt)
  // identifiants en chasse fixe (EXIG-AUT-09, tools/call) : insécables. Une URL (texte
  // d'un lien, que Typst coupe à n'importe quel signe) ou un long nom : coupé seulement
  // après « / » ou « - », chaque morceau insécable.
  show raw.where(block: false): it => {
    if it.text.len() <= 40 { return if it.text.contains(" ") { it } else { box(it) } }
    let morceaux = it.text.matches(regex("[^/-]+[/-]*|[/-]+")).map(m => m.text)
    if morceaux.len() <= 1 { return it }
    morceaux.map(m => raw(m)).join(sym.zws)
  }
  // blocs de code : lignes de Chrome gardées; 6,8 pt pour que la plus longue (109
  // signes) tienne sur la justification
  show raw.where(block: true): it => block(width: 100%, fill: zebre, inset: 7pt, radius: 2pt,
    stroke: 0.4pt + filet, text(size: 6.8pt, it))
  // exigences et encadrés : <div id="exig-N"> et <div id="encadre-N"> de l'extraction
  show block: it => {
    if not it.has("label") { return it }
    let l = str(it.label)
    if l.starts-with("exig-") {
      set par(spacing: 0.6em)
      block(width: 100%, breakable: true, above: 12pt, below: 12pt, inset: (left: 11pt, right: 8pt, y: 7pt),
        stroke: (left: 2.5pt + accent, top: 0.4pt + filet, bottom: 0.4pt + filet, right: 0.4pt + filet), it.body)
    } else if l == "references" {
      set par(justify: false)
      it.body
    } else if l.starts-with("encadre-") {
      block(width: 100%, breakable: true, above: 12pt, below: 12pt, inset: 9pt, radius: 2pt,
        fill: accent-pale, it.body)
    } else if l.starts-with("pourquoi-") {
      set text(size: 9.6pt, fill: gris)
      it.body
    } else { it }
  }
  body
}

// Listes des tableaux et des figures, régénérées (titres courts des figures : ceux de
// la liste d'origine).
#let entree(titre, loc) = {
  set par(justify: false, hanging-indent: 1.2em)
  link(loc, titre)
  h(4pt)
  box(width: 1fr, repeat(gap: 3pt)[.])
  h(2pt)
  link(loc, str(counter(page).at(loc).first()))
  linebreak()
}
#let listes() = page(header: none, {
  set text(font: sans, size: 8.6pt)
  for (titre, corps) in (
    ([Liste des tableaux], context {
      for f in query(figure.where(kind: table)).filter(f => f.caption != none) {
        entree(f.caption.body, f.location())
      }
    }),
    ([Liste des figures], context {
      let fs = query(figure.where(kind: image))
      assert(fs.len() == titres-figures.len(), message: "figures : " + str(fs.len()))
      for (f, t) in fs.zip(titres-figures) { entree(t, f.location()) }
    }),
  ) {
    v(24pt, weak: true)
    text(size: 18pt, weight: "semibold", fill: accent, titre)
    v(4pt)
    line(length: 100%, stroke: 0.6pt + filet)
    v(8pt)
    corps
  }
})
'''

if __name__ == '__main__':
    main()
