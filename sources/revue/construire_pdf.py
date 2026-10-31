"""Recompose le PDF de la Revue de littérature à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Revue de littérature.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt (README, « Documents absents du dépôt ») :
le PDF fait foi, corrections du 29 oct. 2026 comprises. sources/commun/extraire.py
le relit (PDF balisé; repli géométrique pour l'annexe du 29 octobre, fusionnée sans
balisage), puis sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : titre, sous-titre, auteur et date passent sur la couverture, la
    mention de révision dans la fiche;
  - Résumé et Abstract : leur intitulé en gras devient un titre; l'Abstract est
    composé en anglais (césure);
  - titres : sections (H1) en chapitres, sous-sections (H2) en sections du gabarit;
  - légendes « Tableau N. – … » : la numérotation passe à Typst (même suite, contrôlée);
  - gras : celui de la police seulement. Le PDF balise en Strong des passages composés
    en romain (résumé, mentions des références); le rendu d'origine fait foi.
"""
import atexit, html, pathlib, re, shutil, subprocess, sys, tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
from composer import DOCUMENTS, chaine_typst, composer
from extraire import controler_extraction, extraire, texte_controle, vers_html, zones_ecartees
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Revue de littérature.pdf'
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
#  - l'en-tête du tableau 11 est répété en tête de la p. 63 (« No Où Erreur Correction
#    Traitement ») : une fois dans l'extraction, deux fois dans le PDF;
#  - « excep-/tions » est coupé entre les p. 62 et 63, dans une cellule : le contrôle lit le
#    PDF mot à mot et ne recolle une césure qu'avec le mot qui la suit immédiatement.
ECARTS_CONNUS = {'no': 1, 'où': 1, 'erreur': 1, 'correction': 1, 'traitement': 1, 'excep': 1, 'tions': 1}


def page_de_titre(pdf):
    """Titre (15 pt), sous-titre (12 pt), ligne auteur · courriel · date, mention de révision."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    titre = next(t for s, t in lignes if s == 15)
    sous_titre = next(t for s, t in lignes if s == 12)
    auteur, courriel, date = next(t for s, t in lignes if '·' in t and '@' in t).split(' · ')
    revision = next(t for s, t in lignes if t.startswith('Révision du'))
    return dict(titre=titre, sous_titre=sous_titre, auteur=auteur, courriel=courriel, date=date, revision=revision)


def corps(blocs, p):
    # la page de titre : bloc du titre et mention de révision, repris sur la couverture
    assert p['titre'] in blocs[0].html and p['revision'] in blocs[1].html, 'page de titre inattendue'
    h = [b.html for b in blocs[2:]]
    # Résumé, Abstract : intitulé en gras de tête -> titre; l'Abstract court jusqu'au
    # premier chapitre
    for i, b in enumerate(h):
        m = re.match(r'<p><strong>(Résumé|Abstract)</strong> ', b)
        if m:
            h[i] = f'<h2>{m.group(1)}</h2>\n<p>' + b[m.end():]
    debut = next(i for i, b in enumerate(h) if b.startswith('<h2>Abstract'))
    fin = next(i for i, b in enumerate(h) if i > debut and b.startswith('<h2>'))
    h[debut:fin] = [h[debut].split('\n', 1)[0], '<div lang="en">', *h[debut:fin], '</div>']
    h[debut + 2] = h[debut + 2].split('\n', 1)[1]
    s = '\n'.join(h)
    # légendes : « Tableau N. – » laisse la place à la numérotation de Typst
    nums = [int(n) for n in re.findall(r'<caption>Tableau\xa0(\d+)\.\xa0– ', s)]
    assert nums == list(range(1, len(nums) + 1)) and s.count('<caption>') == len(nums), nums
    return re.sub(r'<caption>Tableau\xa0\d+\.\xa0– ', '<caption>', s)


def main():
    blocs = extraire(SRC, niveaux={1: 2, 2: 3}, styles_balises={'Em': 'em', 'Code': 'code'})
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) doit se retrouver dans l'extraction
    manque, _ = controler_extraction(SRC, brut, ecarter=zones_ecartees(SRC))
    inexplique = {m: n for m, n in manque.items() if n > ECARTS_CONNUS.get(m, 0)}
    if inexplique:
        sys.exit(f'extraction incomplète : {inexplique}')
    print(f'extraction : {len(blocs)} blocs, écarts connus seulement ({sum(manque.values())} mots)')

    p = page_de_titre(SRC)
    texte = corps(blocs, p)
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
  keywords: ("revue de littérature", "agents", "interopérabilité", "orchestration", "arXiv"))
#show: note.with(titre-court: "Revue de littérature", pied: [Faits gelés au {p['date']} · révision du 29 octobre 2026])
// légendes au-dessus des tableaux, comme dans l'édition d'origine, et jamais seules
// en bas de page
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
#couverture(surtitre: [Revue de littérature], titre: {typo(p['titre'])},
  sous-titre: {typo(p['sous_titre'])}, auteur: {chaine_typst(p['auteur'])}, date: {chaine_typst(p['date'])},
  fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
'''
    source = ' '.join(texte_controle(t) for t in (p['titre'], p['sous_titre'], fiche, texte))
    composer({'fiche': fiche, 'corps': texte}, main_typ, OUT, source)


if __name__ == '__main__':
    main()
