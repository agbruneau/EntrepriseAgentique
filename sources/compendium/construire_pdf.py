"""Recompose le PDF du Compendium à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Compendium.pdf; --html garde l'extraction brute)

Aucune source amont n'est versée au dépôt (README, « Documents absents du dépôt ») :
le PDF Typst du 24 oct. 2026 fait foi. sources/commun/extraire.py le relit (PDF balisé),
puis sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : surtitre, titre, sous-titre, auteur et édition vont sur la couverture;
    la mention « Livrable du dépôt » (pied de la table des matières d'origine) et les
    dates de gel et de compilation vont dans la fiche; la présentation des cinq livres et
    l'exergue forment une page liminaire, avant le sommaire;
  - table des matières d'origine (balisée en Div et Link, non en TOC) : écartée, le
    gabarit en régénère une;
  - structure : les cinq livres (page d'ouverture « L I V R E / I / Coopérer ») passent
    au niveau 1, les chapitres (H1, précédés de « C H A P I T R E / n ») au niveau 2 sous
    la forme « n · titre », les sections H2, H3 et H4 aux niveaux 3, 4 et 5; les deux
    annexes (« A N N E X E ») passent au niveau 1 et leurs sections remontent d'un cran;
  - figures (118, dessins vectoriels Typst : cadres, flèches et texte) : chacune est rendue
    en PNG à 200 dpi depuis sa zone de page et insérée à sa place, sous sa légende
    d'origine; son texte, devenu image, est repris dans le texte de remplacement (alt);
  - légendes « Figure n.n — » et « Tableau n.n — » : numérotation d'origine (par chapitre)
    gardée telle quelle, celle de Typst désactivée; les légendes de tableau égarées en
    paragraphe rejoignent leur tableau;
  - encadrés « Thèse — … » de tête de chapitre (balisés comme un paragraphe) : en citation;
  - titres balisés en paragraphe gras : promus d'après les signets d'origine (912, tous
    retrouvés dans l'ordre);
  - balisage abîmé par des retouches directes du PDF d'origine : l'extracteur commun
    traite éléments vides, étiquettes de liste porteuses de texte, en-têtes de tableau
    répétés, haut de page rattaché au mauvais bloc et lignes de cellule dans la colonne
    voisine; la sous-classe Extracteur ajoute les paragraphes balisés dans le tableau qui
    les suit et la bibliographie de l'annexe I (p. 941-1000), relue par sa géométrie;
  - adresses : coupables à leurs traits d'union (U+200B), sans césure, contrôlées à part;
  - traces de production (plan de rédaction, décisions et garde-fous, portes, remontées,
    lots de travail) : retirées du corps et de la fiche par retraits.py, sur le texte
    extrait, avant composition.

Contrôles laissés dans le code : complétude de l'extraction (écarts connus listés),
figures (texte dans la zone rendue, zone sans mot étranger), colonnes de tableau, ordre
du texte par page, structure du corps (livres, chapitres, annexes, légendes), retraits
comptés et aucune trace de production restante, contrôle mot à mot de composer(),
adresses d'un seul tenant.
"""
import atexit, collections, dataclasses, html, pathlib, re, shutil, subprocess, sys, tempfile, time

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as composer_mod
import extraire as extraire_mod
import retraits
from composer import DOCUMENTS, NBSP, chaine_typst, composer, date_fr, mots
from extraire import ECARTES, controler_extraction, texte_controle, vers_html
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Compendium.pdf'
# Édition d'origine (Typst 0.15.1, compilée le 24 oct. 2026) : le PDF recomposé ne doit
# pas servir de source à son tour.
ORIGINE = 'd28324a'
OUT = pathlib.Path(args[1]) if len(args) > 1 else SORTIE
TMP = pathlib.Path(tempfile.mkdtemp())
atexit.register(shutil.rmtree, TMP, True)
if args:
    SRC = pathlib.Path(args[0])
else:
    SRC = TMP / 'origine.pdf'
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{SORTIE.name}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

# Date de gel : README (tableau des livrables, « Gel au 27 juill. 2026 »); le PDF ne la
# porte pas sur sa page de titre. La date de compilation vient des métadonnées du PDF.
GEL = '27 juillet 2026'
DPI = 200
# Adresses : avec schéma, ou domaine suivi d'un chemin (cloudsecurityalliance.org/…)
ZWSP = '\u200b'
URL = r'(?:https?://|\b[\w-]+(?:\.[\w-]+)+/)\S*'
# En-tête courant à y 6-17 pt, folio des ouvertures de livre à y 752 et de chapitre à
# y 775; le texte courant descend jusqu'à y 744 (p. 152, 165) : marges du gabarit
# commun (60, 60) trop larges en bas.
MARGES = (30, 45)
# Bibliographie de l'annexe I, relue par sa géométrie (Extracteur.lire_biblio)
PAGES_BIBLIO = range(940, 1000)
# Justification d'origine (x de 85 à 533 pt) : la largeur d'une figure s'y rapporte.
JUSTIF_ORIGINE = 448

# Écarts connus du contrôle de complétude (mots du PDF d'origine absents de l'extraction).
# Le texte des figures est compté à part (il passe dans l'image). Reste « don-/née »,
# coupé au saut des p. 71-72 : en fin de page, le contrôle recolle une césure du texte
# courant au mot suivant du flux, ici un autre (« Le »); le mot entier est bien dans
# l'extraction. Enfin, l'en-tête du tableau des mesures de l'annexe I, répété en haut de
# la p. 941 (« Mesure Valeur ») : une fois dans l'extraction, deux fois dans le PDF.
ECARTS_CONNUS = dict.fromkeys('don née mesure valeur'.split(), 1)
# Lignes de cellule encore hors de leur colonne après recolonner() (controler_colonnes) :
#  - p. 905, dernière rangée du tableau des lacunes : retouche directe du PDF d'origine,
#    dont le texte de la 3e colonne est dessiné sous la 1re (« instruite, non close —
#    révision du 6 juillet… ») et la 4e (« ch. 17 § 17.1 ») reste seule à sa place.
COLONNES_CONNUES = ('p. 905, colonne 3 : « ch. 17 § 17.1',)


# ---- figures ------------------------------------------------------------------------

@dataclasses.dataclass(eq=False)
class Figure:
    page: int
    cle: tuple
    bbox: pymupdf.Rect      # zone du texte balisé
    clip: pymupdf.Rect = None   # zone rendue : texte et dessins
    numero: int = 0
    runs: list = dataclasses.field(default_factory=list)

    @property
    def fichier(self):
        return f'figure-{self.numero:03d}.png'


def inventorier_figures(doc):
    """Éléments Figure de l'arborescence : page, clé (chemin d'index), zone. La zone rendue
    s'étend aux dessins (cadres, flèches, fonds) qui touchent le texte de la figure."""
    figures = []
    for p in doc:
        def marcher(b, chemin):
            if b['type'] != 2:
                return
            cle = chemin + (b['index'],)
            if 'Figure' in (b.get('raw'), b.get('std')):
                figures.append(Figure(p.number, cle, pymupdf.Rect(b['bbox'])))
                return
            for c in b.get('blocks', []):
                marcher(c, cle)
        for b in p.get_text('dict', flags=pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            marcher(b, ())
    for i, f in enumerate(figures, 1):
        f.numero = i
        p = doc[f.page]
        clip = pymupdf.Rect(f.bbox)
        dessins = [d['rect'] for d in p.get_drawings()]
        change = True
        while change:   # un cadre peut en toucher un autre (fond, puis bordure)
            change = False
            for r in dessins:
                if r.intersects(clip + (-3, -3, 3, 3)) and not r in clip and r.height < 0.8 * p.rect.height:
                    clip |= r
                    change = True
        f.clip = (clip + (-2, -2, 2, 2)) & p.rect
    return figures


def rendre_figures(doc, figures, dossier):
    for f in figures:
        pix = doc[f.page].get_pixmap(dpi=DPI, clip=f.clip)
        pix.set_dpi(DPI, DPI)
        pix.save(dossier / f.fichier)


class Extracteur(extraire_mod.Extracteur):
    """Extracteur commun, plus les figures : leur texte est retiré de l'arborescence à la
    lecture de la page (il passe dans l'image, et recaser() ne doit pas le redistribuer),
    et l'élément Figure se rend en <figure><img>."""

    def __init__(self, pdf, figures, **params):
        super().__init__(pdf, **params)
        self.figures = {f.cle: f for f in figures}
        self.par_page = collections.defaultdict(list)
        for f in figures:
            self.par_page[f.page].append(f)
        self.ancetres = {f.cle[:k] for f in figures for k in range(1, len(f.cle))}
        self.biblio = self.liste_biblio = None   # élément en cours de la bibliographie relue

    def lire_page(self, page):
        ok = super().lire_page(page)
        for f in self.par_page.get(page.number, []):
            pile = [f.cle]
            while pile:
                n = self.noeuds[pile.pop()]
                f.runs += [r for r in n.runs if r.page == page.number]
                n.runs = [r for r in n.runs if r.page != page.number]
                pile += n.enfants
            # texte dessiné dans la figure mais balisé dans l'élément voisin (p. 788 :
            # « § 45.7 », rangé dans le paragraphe suivant) : il suit la figure
            for n in self.noeuds.values():
                egares = [r for r in n.runs if r.page == page.number and pymupdf.Rect(r.bbox) in f.clip]
                if egares:
                    self.ecarts.append(f'p. {page.number + 1} : « {self.texte_runs(egares)[:60]} », balisé hors '
                                       f'de la figure {f.numero} qui le dessine, rendu avec elle')
                    f.runs += egares
                    n.runs = [r for r in n.runs if r not in egares]
        if page.number in PAGES_BIBLIO:
            self.lire_biblio(page)
        return ok

    def lire_biblio(self, page):
        """Bibliographie de l'annexe I (p. 941-1000) : l'arborescence y range chaque page
        dans un seul item de liste, puces, titres de lettre et entrées confondus, et
        recaser() en disperse les lignes. La page est relue par sa géométrie, hors du
        tableau balisé qui la précède (p. 941) : titre (gras, 13 pt et plus), entrée (ligne
        qui commence par une puce), alinéa (ligne en retrait), suite (toute autre ligne :
        l'entrée ou l'alinéa en cours, d'une page à l'autre)."""
        p = page.number
        tableau = [r for k, n in self.noeuds.items() if n.role == 'Table' for r in self.runs_de(k) if r.page == p]
        haut = min((r.bbox[1] for r in tableau), default=0)
        bas = max((r.bbox[3] for r in tableau), default=0)
        dans = lambda r: haut - 1 <= r.bbox[1] and r.bbox[3] <= bas + 2
        entete = []
        for n in self.noeuds.values():
            # le tableau garde ses lignes, balisées ou non (p. 941 : valeurs retouchées
            # « 134 » et « 1065 », hors arborescence, que recaser() remet en cellule)
            entete += [r for r in n.runs if r.page == p and r.bbox[3] < haut - 1]
            n.runs = [r for r in n.runs if r.page != p or r in tableau or dans(r)]
        if any(r.texte.strip() for r in entete):
            # p. 941 : en-tête du tableau répété en haut de page, hors arborescence
            self.ecarts.append(f'p. {p + 1} : en-tête de tableau répété écarté (« {self.texte_runs(entete)[:40]} »)')
        liens = [(l['from'], l['uri']) for l in page.get_links() if l.get('kind') == pymupdf.LINK_URI]
        runs = [r for b in page.get_text('dict', flags=extraire_mod.STRUCTURE & ~pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']
                if b['type'] == 0 for r in self.spans(page, b, liens) if r.bbox[3] > bas + 2]
        racine = self.racines[0]
        nouveau = lambda role, parent: self.noeud(('biblio', p, len(self.noeuds)), role, parent).cle
        lignes = self.lignes_visuelles([r for r in runs if r.texte.strip()])
        gauche = min((l[0].bbox[0] for l in lignes), default=0)
        for l in lignes:
            t = self.texte_runs(l)
            if all(r.flags & 16 for r in l) and max(r.taille for r in l) >= 13:
                niveau = 2 if max(r.taille for r in l) >= 16 else 3   # I.1 / I.2, lettres
                if self.biblio and self.biblio[0] == 'titre' and self.biblio[2] == p:
                    cle = self.biblio[1]          # titre sur deux lignes
                else:
                    cle = nouveau(f'H{niveau}', racine)
                self.biblio = ('titre', cle, p)
            elif t.startswith('•'):
                if not (self.biblio and self.biblio[0] == 'item'):
                    self.liste_biblio = nouveau('L', racine)
                cle = nouveau('LI', self.liste_biblio)
                l = [r for r in l if r.texte.strip() != '•']
                if l and l[0].texte.lstrip().startswith('•'):
                    l[0].texte = l[0].texte.lstrip()[1:].lstrip()
                self.biblio = ('item', cle, p)
            elif self.biblio and (self.biblio[0] == 'item' or
                                  self.biblio[0] == 'p' and l[0].bbox[0] <= gauche + 10):
                cle = self.biblio[1]
            else:
                cle = nouveau('P', racine)
                self.biblio = ('p', cle, p)
            self.noeuds[cle].runs += l

    def sortir_du_tableau(self, table):
        """Texte dessiné au-dessus de l'en-tête d'un tableau mais balisé dans ses rangées
        (p. 597, 763, 803, 822, 841, 851, 901, 904, 940 : paragraphe ou légende qui précède
        le tableau) : il en sort, en paragraphes placés avant lui (un alinéa en retrait
        ouvre un paragraphe)."""
        trs = list(self.rangees(table))
        if not trs:
            return
        for p in sorted({r.page for r in self.runs_de(table)}):
            tete = [r for r in self.runs_de(trs[0]) if r.page == p and r.texte.strip()]
            if not tete:
                continue
            y0 = min(r.bbox[1] for r in tete)
            dessus = [r for tr in trs[1:] for r in self.runs_de(tr) if r.page == p and r.bbox[3] < y0 - 1]
            if not any(r.texte.strip() for r in dessus):
                continue
            for r in dessus:
                self.noeuds[self.proprietaire(r)].runs.remove(r)
            lignes = self.lignes_visuelles(dessus)
            gauche = min(l[0].bbox[0] for l in lignes)
            alineas = []
            for l in lignes:
                if not alineas or l[0].bbox[0] > gauche + 8:
                    alineas.append([])
                alineas[-1] += l
            # juste avant le tableau (ou l'ancêtre qui le porte dans sa section)
            ancetre = table
            while self.noeuds[ancetre].parent is not None and \
                    self.noeuds[self.noeuds[ancetre].parent].role not in extraire_mod.SECTIONS:
                ancetre = self.noeuds[ancetre].parent
            parent = self.noeuds[ancetre].parent or ancetre
            for a in alineas:
                hote = parent + (len(self.noeuds), 'retouche')
                self.noeuds[hote] = extraire_mod.Noeud(hote, 'P', parent)
                freres = self.noeuds[parent].enfants
                freres.insert(freres.index(ancetre), hote)
                self.feuilles.add(hote)
                for r in a:
                    # les éléments en ligne de la cellule (Strong d'en-tête…) ne valent pas
                    # pour lui : son style vient de la police (gras, italique)
                    r.bloc, r.en_ligne = hote, ()
                    self.noeuds[hote].runs.append(r)
            self.ecarts.append(f'p. {p + 1} : {len(alineas)} paragraphe(s) balisé(s) dans le tableau qui les '
                               f'suit, sorti(s) avant lui (« {self.texte_runs(lignes[0])[:50]} »)')

    def recaser(self):
        super().recaser()
        for cle in [k for k, n in self.noeuds.items() if n.role == 'Table']:
            self.sortir_du_tableau(cle)
            for _ in range(2):
                self.completer_rangees(cle)
                self.recolonner(cle)

    def rendre(self, cle, legende=None):
        f = self.figures.get(cle)
        if f:
            alt = re.sub(r'\s+', ' ', ' '.join(' '.join(r.texte for r in l) for l in self.lignes_visuelles(f.runs)))
            largeur = min(100, round(100 * f.clip.width / JUSTIF_ORIGINE))
            return (f'<figure data-figure="{f.numero}"><img src="{f.fichier}" width="{largeur}%" '
                    f'alt="{html.escape(alt.strip())}"></figure>')
        if cle in self.ancetres and not self.runs_de(cle):
            # conteneur sans texte propre : ses enfants, figure comprise
            return '\n'.join(h for c in self.noeuds[cle].enfants
                             if self.noeuds[c].role not in ECARTES and (h := self.rendre(c)))
        return super().rendre(cle, legende)


def controler_figures(doc, figures):
    """Chaque figure a du texte, et tout ce texte tient dans la zone rendue; la zone ne
    mord sur aucun mot étranger à la figure (légende, paragraphe voisin)."""
    fautes = []
    for f in figures:
        assert f.runs, f'figure {f.numero} (p. {f.page + 1}) sans texte'
        dehors = [r.texte for r in f.runs if not pymupdf.Rect(r.bbox) in f.clip + (-1, -1, 1, 1)]
        assert not dehors, f'figure {f.numero} (p. {f.page + 1}) : texte hors zone {dehors[:3]}'
        siens = [pymupdf.Rect(r.bbox) for r in f.runs]
        p = doc[f.page]
        intrus = [w[4] for w in p.get_text('words') if pymupdf.Rect(w[:4]).intersects(f.clip)
                  and w[1] > 60 and not any(pymupdf.Rect(w[:4]).intersects(s) for s in siens)]
        if intrus:
            fautes.append(f'figure {f.numero} (p. {f.page + 1}) : la zone {f.clip} mord sur {intrus[:8]}')
    assert not fautes, '\n'.join(fautes)


def controler_ordre(doc, brut, seuil=0.9):
    """Ordre du texte courant (corps 10 pt et plus : ni tableaux ni figures) : part des
    suites de cinq mots de chaque page d'origine retrouvées telles quelles dans
    l'extraction. Rend les pages sous le seuil."""
    norm = lambda t: re.findall(r'[^\W_]+', t.replace('\xad', '').lower())
    h = ' ' + ' '.join(norm(texte_controle(brut))) + ' '
    faibles = []
    for p in doc:
        lignes = [''.join(s['text'] for s in l['spans']) for b in p.get_text('dict')['blocks']
                  for l in b.get('lines', []) if l['spans'][0]['size'] >= 10
                  and MARGES[0] < l['bbox'][3] and l['bbox'][1] < p.rect.height - MARGES[1]]
        w = norm(re.sub(r'\xad\s*\n', '', '\n'.join(lignes)).replace('\n', ' '))
        suites = [' ' + ' '.join(w[i:i + 5]) + ' ' for i in range(0, max(0, len(w) - 5), 3)]
        if len(suites) >= 10:
            part = sum(s in h for s in suites) / len(suites)
            if part < seuil:
                faibles.append((p.number + 1, round(part, 2)))
    return faibles


def controler_colonnes(e):
    """Lignes de cellule qui commencent au début d'une autre colonne que la leur (début
    de colonne : le plus fréquent du rang, par page) : reste de balisage croisé."""
    restes = []
    for cle in [k for k, n in e.noeuds.items() if n.role == 'Table']:
        trs = [[c for c in e.noeuds[tr].enfants if e.noeuds[c].role in ('TD', 'TH')] for tr in e.rangees(cle)]
        lignes = [(j, l) for cells in trs for j, c in enumerate(cells)
                  for l in e.lignes_visuelles([r for r in e.runs_de(c) if r.texte.strip()])]
        cols = collections.defaultdict(collections.Counter)
        for j, l in lignes:
            cols[(l[0].page, j)][round(l[0].bbox[0])] += 1
        debut = {pj: c.most_common(1)[0][0] for pj, c in cols.items()}
        for j, l in lignes:
            p, x0 = l[0].page, l[0].bbox[0]
            autre = [jj for (pp, jj), x in debut.items() if pp == p and jj != j and abs(x - x0) < 3]
            if abs(debut[(p, j)] - x0) > 6 and autre:
                restes.append(f'p. {p + 1}, colonne {j + 1} : « {e.texte_runs(l)[:50]} »')
    return restes


# ---- structure ------------------------------------------------------------------------

ESPACE = lambda mot: ' '.join(mot)   # « L I V R E »


def strip(h):
    return re.sub(r'<[^>]+>', '', h).strip()


def surtitres(page):
    """Surtitres de la page de titre, en capitales espacées (« C O M P E N D I U M ») :
    une lettre par mot PyMuPDF; un blanc de plus de 5 pt sépare deux mots."""
    out = []
    for b in page.get_text('dict')['blocks'][:1]:
        for s in (s for l in b['lines'] for s in l['spans']):
            lettres = [w for w in page.get_text('words') if pymupdf.Rect(w[:4]).intersects(pymupdf.Rect(s['bbox']))]
            mot, mots_ = '', []
            for a, w in zip([None] + lettres, lettres):
                if a and w[0] - a[2] > 5:
                    mots_.append(mot)
                    mot = ''
                mot += w[4]
            mots_.append(mot)
            assert ' '.join(mots_).replace(' ', '') == s['text'].replace(' ', ''), s['text']
            out.append(' '.join(mots_).capitalize())
    return out


def page_de_titre(blocs, doc):
    """Page 1 : surtitres espacés, titre, sous-titre, auteur, édition, cinq livres, exergue."""
    h = vers_html([b for b in blocs if b.page == 0]).split('\n')
    assert len(h) == 11 and h[0].startswith('<p>' + ESPACE('COMPENDIUM')), h[:2]
    st = surtitres(doc[0])
    assert ' '.join(' '.join(x.upper()) for x in st).replace('   ', ' ') == strip(h[0]).replace('  ', ' '), st
    surtitre = ' · '.join(st)
    livres = [re.fullmatch(r'<p><strong>(Livre [IV]+ — [^<]+)</strong> (.+)</p>', x).groups() for x in h[5:10]]
    assert h[10].startswith('<p><em>'), h[10]
    return dict(surtitre=surtitre, titre=strip(h[1]), sous_titre=strip(h[2]), auteur=strip(h[3]),
                edition=strip(h[4]), livres=livres, exergue=h[10])


def promouvoir_titres(lignes, toc):
    """Les signets d'origine font foi pour les titres : un titre que l'arborescence
    balise en paragraphe gras (§ 44.0.4, § 45.4, I.1, I.2, lettres de l'annexe I) redevient
    un titre du niveau de son signet (signet n -> H n du PDF, rendu h n+1 comme les autres).
    Les signets se retrouvent dans l'ordre, chacun après le précédent."""
    norm = lambda t: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t)).replace(NBSP, ' ')
                            .replace('’', "'")).strip()
    # espace insécable des signets lue « € » (0xA0 du PDFDocEncoding, mal décodé)
    signets = [(n, norm(t.replace('€', ' '))) for k, (n, t, _) in enumerate(toc) if k == 0 or toc[k - 1][:2] != [n, t]]
    titre = re.compile(r'<h(\d)>(.*)</h\1>')
    gras = re.compile(r'<p><strong>(?:<em>)?([^<]*)(?:</em>)?</strong></p>')
    out, i, promus = list(lignes), 0, []
    for n, t in signets:
        while i < len(out):
            m = titre.fullmatch(out[i]) or gras.fullmatch(out[i])
            if m and norm(m.group(m.lastindex)) == t:
                break
            i += 1
        else:
            raise AssertionError(f'signet introuvable dans le corps : {t}')
        if not out[i].startswith('<h'):
            out[i] = f'<h{n + 1}>{m.group(1)}</h{n + 1}>'
            promus.append(t)
        i += 1
    print(f'titres : {len(signets)} signets retrouvés, dont {len(promus)} balisés en paragraphe et promus')
    return out


def corps(blocs, p, toc):
    """Corps du livre (des livres aux annexes), et ce que la page de titre et la table des
    matières d'origine laissent à la fiche."""
    debut = next(i for i, b in enumerate(blocs) if b.html.startswith(f'<p>{ESPACE("LIVRE")}</p>'))
    avant = blocs[:debut]
    # avant le livre I : page de titre (p. 1) et table des matières (p. 2-14), dont seule
    # la mention « Livrable du dépôt » est du texte courant
    assert all(b.page is not None and b.page < 14 for b in avant), 'liminaires inattendus'
    statut = [l for l in vers_html(avant).split('\n') if l.startswith('<p><strong>Livrable du dépôt.</strong>')]
    assert len(statut) == 1
    # une ligne par élément de premier rang (les listes et les tableaux en comptent
    # plusieurs, sans effet sur les motifs cherchés ici)
    h = promouvoir_titres(vers_html(blocs[debut:]).split('\n'), toc)
    out, annexe, i = [], False, 0
    livres = chapitres = annexes = entetes = 0
    while i < len(h):
        b = h[i]
        if b == f'<p>{ESPACE("LIVRE")}</p>':
            num, titre, sous = h[i + 1:i + 4]
            num, titre = re.fullmatch(r'<p><strong>([IV]+)</strong></p>', num).group(1), strip(titre)
            assert sous.startswith('<p><em>'), sous
            out += [f'<h1>Livre {num} — {titre}</h1>', sous]
            livres += 1
            i += 4
            continue
        if b == f'<p>{ESPACE("CHAPITRE")}</p>':
            num = re.fullmatch(r'<p><strong>(\d+)</strong></p>', h[i + 1]).group(1)
            m = re.fullmatch(r'<h2>(.+)</h2>', h[i + 2])
            chapitres += 1
            assert m and int(num) == chapitres, (num, h[i + 2][:80])
            out.append(f'<h2>{num} · {m.group(1)}</h2>')
            i += 3
            continue
        if b == f'<p>{ESPACE("ANNEXE")}</p>':
            # titre d'annexe : H1 (Annexe I) ou paragraphe en gras (Annexe B, titre balisé
            # en P dans l'arborescence)
            m = re.fullmatch(r'<h2>(Annexe\s.+)</h2>|<p><strong>(Annexe\s[^<]+)</strong></p>', h[i + 1])
            assert m, h[i + 1][:80]
            out.append(f'<h1>{(m.group(1) or m.group(2)).replace(NBSP, " ")}</h1>')
            annexe, annexes = True, annexes + 1
            i += 2
            continue
        if annexe:   # sections d'annexe : un cran plus haut (h3 -> h2…)
            b = re.sub(r'<(/?)h([3-6])>', lambda m: f'<{m.group(1)}h{int(m.group(2)) - 1}>', b)
        m = re.fullmatch(r'<p><strong>([^<]+)</strong></p>', b)
        if m and out and out[-1].startswith('<table'):
            # reste d'en-tête répété que l'extracteur commun n'a pas absorbé (texte
            # étranger intercalé) : ses mots sont tous ceux de l'en-tête qui précède
            tete = re.sub(r'<[^>]+>|\s', '', out[-1].split('</thead>')[0]).lower()
            if all(x in tete for x in re.findall(r'\w+', html.unescape(m.group(1)).lower())):
                entetes += 1
                i += 1
                continue
        out.append(b)
        i += 1
    assert (livres, chapitres, annexes) == (5, 50, 2), (livres, chapitres, annexes)
    print(f"corps : {entetes} reste(s) d'en-tête de tableau répété écarté(s)")
    s = '\n'.join(out)
    # encadrés de thèse
    s, n = re.subn(r'<p><strong>Thèse</strong> —(.*?)</p>', r'<blockquote><p><strong>Thèse</strong> —\1</p></blockquote>', s)
    # légendes de figure : rejoignent l'image qui les suit (ou, à défaut, qui les précède)
    leg = r'<p>(<strong>Figure \d+\.\d+[a-z]?</strong> —(?:(?!</p>).)*)</p>'
    fig = r'<figure (data-figure="\d+")>(<img [^>]*>)</figure>'
    s = re.sub(leg + r'\n' + fig, r'<figure \2>\3<figcaption>\1</figcaption></figure>', s)
    s = re.sub(fig + r'\n' + leg, r'<figure \1>\2<figcaption>\3</figcaption></figure>', s)
    # légendes de tableau égarées dans un paragraphe, juste avant leur tableau
    s = re.sub(r'<p>(<strong>Tableau \d+\.\d+</strong> —(?:(?!</p>).)*)</p>\n<table>(?:<caption></caption>)?(?!<caption>)',
               r'<table><caption>\1</caption>', s)
    s = s.replace('<caption></caption>', '')
    # rangées entièrement vides (cellules vidées par une retouche du PDF : p. 849)
    s = re.sub(r'<tr>(?:<td></td>)+</tr>', '', s)
    return couper_adresses(s), statut[0]


def controler_corps(s, nb_figures):
    """Structure du corps : légendes en place, figures toutes posées et légendées."""
    figs = re.findall(r'<figure data-figure="(\d+)">(?:(?!</figure>).)*</figure>', s)
    assert [int(n) for n in figs] == list(range(1, nb_figures + 1)), 'figures manquantes ou en désordre'
    sans = re.findall(r'<figure data-figure="(\d+)"><img [^>]*></figure>', s)
    egarees = re.findall(r'<p><strong>(?:Figure|Tableau) \d+\.\d+[a-z]?</strong> —', s)
    nums = lambda k: re.findall(rf'<(?:figcaption|caption)><strong>{k} (\d+\.\d+[a-z]?)</strong>', s)
    return dict(figures=len(figs), figures_sans_legende=sans, legendes_egarees=len(egarees),
                legendes_figure=len(nums('Figure')), legendes_tableau=len(nums('Tableau')))


# ---- Typst ------------------------------------------------------------------------------

def pandoc_sans_images(fragment, dest, imports=()):
    """composer.pandoc(), plus deux retouches propres au Compendium :
      - il importe chaque fichier d'« extras » dans chaque fragment : les images en sont
        exclues (un PNG ne s'importe pas);
      - largeurs de colonnes : le plancher de filtre.lua (mot le plus long d'une ligne)
        dépasse parfois la justification à lui seul (identifiants draft-ietf-…, p. 148
        et 467 recomposées) : la somme est ramenée à 100 %, l'identifiant se coupant
        à ses traits d'union."""
    PANDOC(fragment, dest, [i for i in imports if i.endswith('.typ')])

    def ramener(m):
        parts = [float(x) for x in re.findall(r'([\d.]+)%', m.group(1))]
        if sum(parts) <= 100:
            return m.group(0)
        return 'columns: (' + ', '.join(f'{x * 100 / sum(parts):.2f}%' for x in parts) + ')'
    typ = dest.read_text(encoding='utf8')
    dest.write_text(re.sub(r'columns: \(((?:[\d.]+%,? ?)+)\)', ramener, typ), encoding='utf8')


def couper_adresses(h):
    """Adresses du texte (hors balises et code) : une coupure possible (U+200B) après
    chaque trait d'union. Sans elle, filtre.lua met en boîte insécable le segment
    « a2a-protocol-surpasses-150-… » d'une adresse, qui déborde alors de la page."""
    morceaux = re.split(r'(<pre\b.*?</pre>|<code\b.*?</code>|<[^>]+>)', h, flags=re.S)
    return ''.join(m if i % 2 else re.sub(URL, lambda u: u.group(0).replace('-', '-' + ZWSP), m)
                   for i, m in enumerate(morceaux))


PANDOC = composer_mod.pandoc
composer_mod.pandoc = pandoc_sans_images
DUREES = collections.defaultdict(float)


class Chrono:
    """subprocess de composer.py, chronométré par commande (pandoc, typst)."""
    def __getattr__(self, nom):
        return getattr(subprocess, nom)

    @staticmethod
    def run(cmd, *a, **k):
        t = time.time()
        try:
            return subprocess.run(cmd, *a, **k)
        finally:
            DUREES[pathlib.Path(cmd[0]).stem] += time.time() - t


composer_mod.subprocess = Chrono()


def main():
    t0 = time.time()
    doc = pymupdf.open(SRC)
    figures = inventorier_figures(doc)
    e = Extracteur(SRC, figures, niveaux={1: 2, 2: 3, 3: 4, 4: 5}, marges=MARGES,
                   styles_balises={'Em': 'em', 'Strong': 'strong', 'Code': 'code'})
    blocs = e.extraire()
    controler_figures(doc, figures)
    restes = controler_colonnes(e)
    inexplique = [r for r in restes if not r.startswith(COLONNES_CONNUES)]
    assert not inexplique, inexplique
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges) se retrouve dans
    # l'extraction, sauf le texte des figures, contrôlé à part (dans la zone rendue)
    zones = [(f.page, pymupdf.Rect(r.bbox)) for f in figures for r in f.runs]
    manque, _ = controler_extraction(SRC, brut, marges=MARGES, ecarter=zones)
    # en-têtes de tableau répétés à chaque page : écartés à dessein (une fois dans
    # l'extraction, à chaque page dans le PDF)
    inexplique = {m: n for m, n in manque.items() if n > ECARTS_CONNUS.get(m, 0)}
    if inexplique:
        sys.exit(f'extraction incomplète ({sum(inexplique.values())} mots) : '
                 f'{dict(collections.Counter(inexplique).most_common(40))}')
    # ordre : les pages de tableaux retouchés (p. 736, 803, 905, 940) restent sous 90 %
    faibles = controler_ordre(doc, brut)
    print(f'ordre : {len(faibles)} page(s) sous 90 % de suites retrouvées {faibles}')
    assert len(faibles) <= 6, faibles
    mots_figures = sum(len(re.findall(r'\w+', r.texte)) for f in figures for r in f.runs)
    print(f'extraction : {len(blocs)} blocs, {len(figures)} figures ({mots_figures} mots en image), '
          f'écarts connus seulement ({sum(manque.values())} mots), {time.time() - t0:.0f} s')
    for x in e.ecarts:
        print('  ' + x)

    p = page_de_titre(blocs, doc)
    texte, statut = corps(blocs, p, doc.get_toc())
    texte, statut, n = retraits.retirer_traces(texte, statut)
    print(f'traces de production : {n} substitutions et motifs comptés, aucune trace restante')
    bilan = controler_corps(texte, len(figures))
    print('structure :', bilan)
    assert not bilan['figures_sans_legende'] and not bilan['legendes_egarees'], bilan

    m = re.match(r'D:(\d{4})(\d\d)(\d\d)', doc.metadata['creationDate'])
    compile_le = date_fr(*map(int, m.groups()))
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(p["auteur"])}</td></tr>'
             f'<tr><td>Édition</td><td>{html.escape(p["edition"])}</td></tr>'
             f'<tr><td>Faits gelés au</td><td>{GEL}</td></tr>'
             f'<tr><td>Compilé le</td><td>{compile_le}</td></tr>'
             f'<tr><td>Statut</td><td>{statut[3:-4]}</td></tr>'
             '</tbody></table></div>')
    liminaire = ''.join(f'<p><strong>{html.escape(t)}</strong><br>{d}</p>' for t, d in p['livres'])
    liminaire += f'<blockquote>{p["exergue"]}</blockquote>'
    meta = doc.metadata
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#set document(title: {typo(meta['title'])}, description: {typo(meta['subject'])},
  keywords: ({', '.join(chaine_typst(k.strip()) for k in meta['keywords'].split(','))}))
#show: note.with(titre-court: "Compendium", pied: [Gel au {GEL} · édition de {p['edition'].lower()}])
// numérotation d'origine (par chapitre) gardée dans les légendes : celle de Typst se tait
#set figure(numbering: none)
// légendes au-dessus des tableaux, sous les figures, comme dans l'édition d'origine
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
#show figure.where(kind: image): set block(above: 14pt, below: 16pt)
// sections de quatrième rang (H4 d'origine, 1.1.3.1…)
#show heading.where(level: 5): it => block(above: 10pt, below: 5pt, sticky: true,
  text(font: sans, size: 9.5pt, weight: "regular", style: "italic", fill: gris, it.body))
#show quote.where(block: true): it => block(width: 100%, inset: (left: 12pt, y: 6pt),
  stroke: (left: 2pt + accent), fill: accent-pale, it.body)
// adresses : coupées à leurs traits d'union ou barres obliques, jamais par une césure
// qui leur ajouterait un trait
#show regex({chaine_typst(URL)}): it => text(hyphenate: false, it)
#couverture(surtitre: {typo(p['surtitre'])}, titre: text(hyphenate: false, {typo(p['titre'])}),
  sous-titre: {typo(p['sous_titre'])}, auteur: {typo(p['auteur'])}, date: {typo(p['edition'])},
  fiche: include "fiche.typ")
#page(header: none, {{
  v(30pt)
  set par(justify: false)
  include "liminaire.typ"
}})
#sommaire()
#include "corps.typ"
'''
    dossier = TMP / 'figures'
    dossier.mkdir()
    rendre_figures(doc, figures, dossier)
    source = ' '.join(texte_controle(t) for t in (p['surtitre'], p['titre'], p['sous_titre'], fiche, liminaire, texte))
    # adresses (URL, chemins) : Typst les coupe en fin de ligne n'importe où, sans trait
    # (« cloudsecuri|tyalliance ») ; contrôlées à part, d'un seul tenant, blancs ôtés
    source = source.replace(ZWSP, '')
    adresses = re.findall(URL, source)
    source = re.sub(URL, ' ', source)
    t1 = time.time()
    brouillon = TMP / OUT.name
    composer({'fiche': fiche, 'liminaire': liminaire, 'corps': texte}, main_typ, brouillon, source,
             extras=sorted(dossier.iterdir()))
    # hors en-têtes et pieds, comme composer.controler()
    rendu = re.sub(r'[\s\xad\u200b]+', '', ''.join(w[4] for pg in pymupdf.open(brouillon) for w in pg.get_text('words')
                                             if w[1] > 70 and w[3] < pg.rect.height - 60))
    absentes = [a for a in adresses if re.sub(r'\s+', '', a) not in rendu]
    if absentes:
        shutil.copy(brouillon, OUT.with_name(OUT.stem + ' (rejeté).pdf'))
        sys.exit(f'{len(absentes)} adresse(s) absente(s) du PDF : {absentes[:10]}')
    shutil.copy(brouillon, OUT)
    print(f'adresses : {len(adresses)}, toutes présentes; composition : {time.time() - t1:.0f} s '
          f'(pandoc {DUREES["pandoc"]:.0f} s, typst {DUREES["typst"]:.0f} s); {OUT}')


if __name__ == '__main__':
    main()
