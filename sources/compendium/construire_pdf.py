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
  - balisage abîmé par des retouches directes du PDF d'origine, corrigé dans la sous-classe
    Extracteur : éléments vides qui rompent un paragraphe, étiquettes de liste porteuses de
    texte, lignes de cellule rangées dans la colonne voisine, paragraphes balisés dans le
    tableau qui les suit, en-têtes de tableau répétés à chaque page, haut de page rattaché
    au mauvais bloc, bibliographie de l'annexe I (p. 941-1000) relue par sa géométrie;
  - adresses : coupables à leurs traits d'union (U+200B), sans césure, contrôlées à part.

Contrôles laissés dans le code : complétude de l'extraction (écarts connus listés),
figures (texte dans la zone rendue, zone sans mot étranger), colonnes de tableau, ordre
du texte par page, structure du corps (livres, chapitres, annexes, légendes), contrôle
mot à mot de composer(), adresses d'un seul tenant.
"""
import atexit, collections, dataclasses, html, pathlib, re, shutil, subprocess, sys, tempfile, time

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as composer_mod
import extraire as extraire_mod
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
# Le texte des figures est compté à part (il passe dans l'image). Restent des mots coupés
# en fin de ligne dans une cellule de tableau : le contrôle lit le PDF mot à mot, rangée
# visuelle par rangée visuelle, et recolle la césure au mot de la cellule voisine
# (« préimpres- la sion ») ; le mot entier est bien dans l'extraction (donnée, attributs,
# tokenisation, communautaire, préimpression, procédure, protégé, substituabilité,
# attribuée, posée : p. 198, 345-346, 389-391, 554-555, 693-694, 723-724). Enfin, l'en-tête
# du tableau des mesures de l'annexe I, répété en haut de la p. 941 (« Mesure Valeur ») :
# une fois dans l'extraction, deux fois dans le PDF.
ECARTS_CONNUS = dict.fromkeys(
    'don née buts to kenisation taire préimpresla sion proprocédure tégé substich tuabilité communau '
    'atune po tribuée sée attriqu mesure valeur'.split(), 1)
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

    def ecarter_entetes_repetes(self):
        """En-tête de tableau répété par Typst à chaque nouvelle page : hors arborescence
        (texte anonyme « hors »), il deviendrait un paragraphe après le tableau, ou des
        lignes que recaser() verserait dans les cellules. Est écarté le texte anonyme
        posé juste au-dessus de la première ligne du tableau sur la page (60 pt au plus),
        dont tous les mots sont ceux de l'en-tête."""
        hors = collections.defaultdict(list)
        for k, n in self.noeuds.items():
            if k[0] == 'hors':
                for r in n.runs:
                    hors[r.page].append((k, r))
        self.entetes_repetes, self.mots_entetes = 0, collections.Counter()
        for cle, n in self.noeuds.items():
            if n.role != 'Table':
                continue
            trs = list(self.rangees(cle))
            if not trs:
                continue
            tete = self.runs_de(trs[0])
            # en-tête d'un seul tenant (sans blancs ni césures) : un fragment de mot coupé
            # autrement qu'à la première page (« pres- / crit ») s'y retrouve aussi
            tete_txt = re.sub(r'[\s\xad]', '', ''.join(r.texte for r in tete).lower())
            p0 = min((r.page for r in tete), default=None)
            corps = collections.defaultdict(list)
            for tr in trs:
                for r in self.runs_de(tr):
                    corps[r.page].append(r)
            for p, rs in corps.items():
                if p == p0:
                    continue
                y = min(r.bbox[1] for r in rs)
                retires = []
                for k, r in hors.get(p, ()):
                    mots_r = set(re.findall(r'\w+', r.texte.lower()))
                    if y - 60 <= r.bbox[1] < y and all(m in tete_txt for m in mots_r) and r in self.noeuds[k].runs:
                        self.noeuds[k].runs.remove(r)
                        retires.append(r)
                self.entetes_repetes += len(retires)
                # mots comptés comme le contrôle les lit : mots du PDF dans ces zones, dans
                # l'ordre du PDF, césures recollées
                zones = [pymupdf.Rect(r.bbox) for r in retires]
                lus = [w[4] for w in self.doc[p].get_text('words')
                       if any(pymupdf.Rect(w[:4]).intersects(z) for z in zones)]
                self.mots_entetes += mots(re.sub(r'\xad\s+', '', ' '.join(lus)).replace('\xad', ''))
        self.ecarts.append(f'{self.entetes_repetes} span(s) d\'en-tête de tableau répété écarté(s)')

    def classer(self):
        """Trois retouches de l'arborescence avant le classement commun :
          - en-têtes de tableau répétés : écartés (ecarter_entetes_repetes);
          - éléments vides (appels de note Note > Lbl > Link sans texte, citations vides) :
            retirés; un paragraphe qui en contient un passerait pour un conteneur de blocs
            et se romprait en un fragment par élément en ligne (p. 473-474);
          - étiquette de liste (Lbl) qui porte une phrase et non un repère (« • », « 2. ») :
            terme d'une liste à alinéa suspendu (p. 561, 563, 710); elle devient un
            paragraphe de l'item, sans quoi liste() l'écarterait avec les repères."""
        self.ecarter_entetes_repetes()
        garder = set(self.figures) | self.ancetres
        vides = {}

        def vide(cle):
            if cle not in vides:
                n = self.noeuds[cle]
                vides[cle] = not n.runs and all(vide(c) for c in n.enfants)
            return vides[cle]
        for n in list(self.noeuds.values()):
            n.enfants = [c for c in n.enfants if c in garder or not vide(c) or
                         self.noeuds[c].role in extraire_mod.EN_LIGNE | {'TD', 'TH', 'TR', 'THead', 'TBody', 'Table'}]
        self.termes = set()
        for cle, n in self.noeuds.items():
            if n.role == 'Lbl' and len(re.sub(r'\s', '', ''.join(r.texte for r in self.runs_de(cle)))) > 6:
                n.role = 'P'
                self.termes.add(cle)
        super().classer()

    def rangees(self, cle):
        n = self.noeuds[cle]
        if n.role == 'TR':
            yield cle
        elif n.role not in ECARTES:
            for c in n.enfants:
                if self.noeuds[c].role != 'Table':
                    yield from self.rangees(c)

    def colonnes(self, table):
        """Rangées (cellules) d'un tableau, et début (x, pt) de chaque colonne, le même à
        chaque page : celui des cellules de la première rangée (l'en-tête) si aucune n'est
        vide, sinon None. Une estimation par la majorité des rangées échoue quand la
        rangée mal balisée l'emporte en nombre (p. 918-920)."""
        trs = [[c for c in self.noeuds[tr].enfants if self.noeuds[c].role in ('TD', 'TH')]
               for tr in self.rangees(table)]
        if not trs:
            return trs, None
        debuts = [min([r.bbox[0] for r in self.runs_de(c) if r.texte.strip()] or [None]) for c in trs[0]]
        return trs, None if None in debuts else debuts

    def completer_rangees(self, table):
        """Rangée balisée sans ses cellules vides (coin d'un tableau à double entrée :
        p. 263, 563, 665, 682, 752…) : pandoc la décalerait à gauche. Une cellule vide est
        rétablie à chaque colonne où rien ne commence; colonnes d'après les rangées
        complètes (début le plus fréquent de chaque rang)."""
        cellules = lambda tr: [c for c in self.noeuds[tr].enfants if self.noeuds[c].role in ('TD', 'TH')]
        debut = lambda c: min([r.bbox[0] for r in self.runs_de(c) if r.texte.strip()] or [None])
        trs = list(self.rangees(table))
        n = max((len(cellules(t)) for t in trs), default=0)
        compte = collections.defaultdict(collections.Counter)
        for t in trs:
            if len(cellules(t)) == n:
                for j, c in enumerate(cellules(t)):
                    if debut(c) is not None:
                        compte[j][round(debut(c))] += 1
        if len(compte) != n:
            return
        d = [compte[j].most_common(1)[0][0] for j in range(n)]
        if d != sorted(set(d)):
            return
        for t in trs:
            cs = cellules(t)
            if len(cs) >= n or any(debut(c) is None for c in cs):
                continue
            place = {max([i for i, x in enumerate(d) if x - 3 <= debut(c)] or [0]): c for c in cs}
            if len(place) != len(cs):
                continue
            role = self.noeuds[cs[0]].role
            rangee = []
            for k in range(n):
                if k not in place:
                    place[k] = t + (len(self.noeuds), 'coin')
                    self.noeuds[place[k]] = extraire_mod.Noeud(place[k], role, t)
                rangee.append(place[k])
            self.noeuds[t].enfants = [c for c in self.noeuds[t].enfants if c not in cs] + rangee
            p = min(r.page for c in cs for r in self.runs_de(c)) + 1
            self.ecarts.append(f'p. {p} : rangée de {len(cs)} cellule(s) sur {n}, cellule(s) vide(s) rétablie(s)')

    def recolonner(self, cle):
        """Chaque span d'une rangée complète rejoint la cellule de la colonne où il est
        dessiné."""
        trs, debuts = self.colonnes(cle)
        if not debuts or len(debuts) < 2 or debuts != sorted(set(debuts)):
            return
        for tr, cells in zip(self.rangees(cle), trs):
            # cellule ajoutée par recaser() pour une ligne égarée (inserer_cellule) :
            # sa ligne rejoint, elle aussi, la cellule de sa colonne
            propres = [c for c in cells if c[-1] != 'retouche']
            if len(propres) != len(debuts):
                continue
            for c in cells:
                for r in self.runs_de(c):
                    k = max([i for i, d in enumerate(debuts) if d - 3 <= r.bbox[0]] or [0])
                    if propres[k] == c:
                        continue
                    self.noeuds[self.proprietaire(r)].runs.remove(r)
                    r.bloc = propres[k]
                    self.noeuds[propres[k]].runs.append(r)
                    self.feuilles.add(propres[k])
                    self.hors_colonne.append((r.page, r))
            n = self.noeuds[tr]
            n.enfants = [c for c in n.enfants if c[-1] != 'retouche' or self.runs_de(c)]

    def inserer_paragraphe(self, voisin, page, y):
        """inserer_paragraphe() commun, au rang près : il place le paragraphe avant le
        premier frère qui commence plus bas sur la même page, sinon en fin de section. Ici,
        tout le livre est une seule section (racine Document) : une ligne égarée en bas de
        page partait en fin de volume (p. 849, 860, 864, 883, 884, 925). Le rang retenu est
        celui du premier frère qui commence après elle, page puis hauteur."""
        nouveau = super().inserer_paragraphe(voisin, page, y)
        parent = self.noeuds[nouveau].parent
        freres = self.noeuds[parent].enfants
        freres.remove(nouveau)
        # début de chaque frère, mis en cache (les lignes déplacées ne le changent guère)
        cache = self.__dict__.setdefault('debuts', {})

        def debut(c):
            if c not in cache:
                cache[c] = min(((r.page, r.bbox[1]) for r in self.runs_de(c)), default=None)
            return cache[c]
        pos = next((i for i, c in enumerate(freres) if (d := debut(c)) is not None and d > (page, y)), len(freres))
        freres.insert(pos, nouveau)
        return nouveau

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

    def recaser_suite(self):
        """recaser() de extraire.py, recopié avec un cas de plus : un amas de lignes en haut
        de page, rangé dans un bloc qui commence plus bas sans venir de la page précédente,
        rejoint le bloc qui terminait celle-ci. Sans quoi le commun, qui garde à chaque bloc
        son amas le plus fourni, garde cet amas étranger et chasse les lignes du bloc
        lui-même : l'ordre du texte s'inverse (p. 562 : « … la vérification » avant
        « commerciales, jamais pour… », fin du paragraphe de la p. 561)."""
        par_page = collections.defaultdict(lambda: collections.defaultdict(list))
        for f in self.feuilles:
            for r in self.runs_de(f):
                par_page[r.page][f].append(r)
        pages_de = collections.defaultdict(set)
        for p, blocs in par_page.items():
            for f in blocs:
                pages_de[f].add(p)
        # bloc qui finit chaque page (ligne la plus basse) sans se poursuivre à la suivante
        # et la fin de son texte (sa ligne la plus basse, dernier span)
        dernier, fin = {}, {}
        for p, blocs in par_page.items():
            bas_page = max(((r.bbox[3], r.bbox[2], f, i) for f, rs in blocs.items() for i, r in enumerate(rs)
                            if r.texte.strip()), default=None)
            if bas_page and p + 1 not in pages_de[bas_page[2]] and \
                    self.noeuds[bas_page[2]].role in ('P', 'LBody', 'LI', 'Span'):
                dernier[p] = bas_page[2]
                fin[p] = blocs[bas_page[2]][bas_page[3]].texte.rstrip()
        # suite de phrase : la page précédente ne finit pas sur une ponctuation finale, ou
        # le haut de page commence par une minuscule (un encadré flottant en haut de page,
        # « Revalidation du 30 juillet 2026 : … », p. 154, ne se rattache pas)
        suite = lambda p, t: not re.search(r'[.!?:;»)\]]$', fin[p]) or t[:1].islower()
        for p, blocs in sorted(par_page.items()):
            etendue, tailles, egares = {}, {}, []
            haut_page = min((r.bbox[1] for rs in blocs.values() for r in rs if r.texte.strip()), default=0)
            for f, runs in blocs.items():
                amas, bas = [], None
                for r in sorted((r for r in runs if r.texte.strip()), key=lambda r: r.bbox[1]):
                    if amas and r.bbox[1] - bas < 1.5 * r.taille:
                        amas[-1].append(r)
                        bas = max(bas, r.bbox[3])
                    else:
                        amas.append([r])
                        bas = r.bbox[3]
                if not amas:
                    continue
                if len(amas) > 1 and p - 1 not in pages_de[f] and amas[0][0].bbox[1] <= haut_page + 1 \
                        and dernier.get(p - 1) not in (None, f) \
                        and suite(p - 1, self.texte_runs(self.lignes_visuelles(amas[0])[0])):
                    # amas du haut de page dans un bloc qui commence plus bas : la fin du
                    # bloc qui terminait la page précédente (p. 562 : « commerciales,
                    # jamais pour… », balisé dans le paragraphe du bas de page)
                    hote = dernier[p - 1]
                    for l in self.lignes_visuelles(amas[0]):
                        self.ecarts.append(f'p. {p + 1} : haut de page rendu au bloc de la page précédente '
                                           f'« {self.texte_runs(l)[:50]} »')
                        for r in l:
                            self.noeuds[self.proprietaire(r)].runs.remove(r)
                            r.bloc = hote
                            self.noeuds[hote].runs.append(r)
                    amas = amas[1:]
                principal = max(amas, key=lambda a: sum(len(r.texte.strip()) for r in a))
                etendue[f] = extraire_mod.cadre(principal)
                tailles[f] = {round(r.taille, 1) for r in principal}
                for a in amas:
                    if a is not principal:
                        egares += [(f, l) for l in self.lignes_visuelles(a)]

            def touche(l, g):
                x0, y0, x1, y1 = extraire_mod.cadre(l)
                gx0, gy0, gx1, gy1 = etendue[g]
                h = max(r.taille for r in l)
                ecart = max(gy0 - y1, y0 - gy1, 0)
                return ecart < 0.6 * h and x0 < gx1 and x1 > gx0 and any(
                    abs(r.taille - t) <= 0.5 for r in l for t in tailles[g])

            def deplacer(l, f, hote):
                self.ecarts.append(f'p. {p + 1} : ligne déplacée « {self.texte_runs(l)[:60]} »')
                y0, y1 = extraire_mod.cadre(l)[1], extraire_mod.cadre(l)[3]
                blancs = [r for r in blocs[f] if not r.texte.strip() and y0 - 1 <= r.bbox[1] and r.bbox[3] <= y1 + 1]
                for r in l + blancs:
                    self.noeuds[self.proprietaire(r)].runs.remove(r)
                    r.bloc = hote
                    self.noeuds[hote].runs.append(r)

            grandir = lambda g, l: etendue.__setitem__(g, extraire_mod.cadre([etendue[g], extraire_mod.cadre(l)]))
            change = True
            while change and egares:
                change = False
                for f, l in list(egares):
                    hote = f if touche(l, f) else next((g for g in etendue if g != f and touche(l, g)), None)
                    if hote is None:
                        continue
                    if hote != f:
                        deplacer(l, f, hote)
                    grandir(hote, l)
                    egares.remove((f, l))
                    change = True
            for f, l in egares:
                x0, y0, x1, y1 = extraire_mod.cadre(l)
                hote = next((g for g in etendue if 'retouche' in g and touche(l, g)), None)
                if hote is None:
                    hote = self.inserer_cellule(f, p, l) or self.inserer_paragraphe(f, p, y0)
                    etendue[hote], tailles[hote] = extraire_mod.cadre(l), {round(r.taille, 1) for r in l}
                deplacer(l, f, hote)
                grandir(hote, l)

    def recaser(self):
        """recaser_suite(), puis les cellules : sur certaines pages (p. 803, 849, 905, 918,
        922, 940), l'arborescence range dans une cellule des lignes dessinées dans la colonne
        voisine de la même rangée, et la lecture visuelle les entrelace (« sa période traverse
        deux de commentaires échéances »). Chaque ligne rejoint la cellule de la colonne où
        elle est dessinée."""
        self.recaser_suite()
        self.hors_colonne = []
        for cle in [k for k, n in self.noeuds.items() if n.role == 'Table']:
            self.sortir_du_tableau(cle)
            # deux passes : une rangée ne se complète qu'une fois ses lignes recasées
            for _ in range(2):
                self.completer_rangees(cle)
                self.recolonner(cle)
        pages = collections.Counter(p + 1 for p, _ in self.hors_colonne)
        for p, n in sorted(pages.items()):
            self.ecarts.append(f'p. {p} : {n} span(s) de tableau rendu(s) à la cellule de leur colonne')

    def rendre(self, cle, legende=None):
        if cle in getattr(self, 'termes', ()):
            return f'<p data-terme="">{self.en_ligne_html(cle)}</p>'
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
            # reste d'en-tête répété que ecarter_entetes_repetes() n'a pas reconnu (posé
            # plus haut que sa fenêtre) : ses mots sont tous ceux de l'en-tête qui précède
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
    # terme d'une liste à alinéa suspendu : il ouvre le texte de son item
    s = re.sub(r'<p data-terme="">((?:(?!</p>).)*)</p>\n<p>', r'<p>\1 ', s)
    s = re.sub(r'<p data-terme="">((?:(?!</p>).)*)</p>\n', r'\1 ', s)
    assert 'data-terme' not in s
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
    manque -= e.mots_entetes
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
