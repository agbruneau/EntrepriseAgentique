"""En-têtes de force des exigences calculés d'après leur énoncé (constats 4.68, 23-19).

Une exigence dont l'énoncé combine plusieurs forces (p. ex. DOIT et NE DOIT PAS) l'affiche
désormais dans son en-tête, dans l'ordre DOIT, NE DOIT PAS, DEVRAIT, NE DEVRAIT PAS; PEUT,
qui accorde une permission, n'y figure que pour une exigence entièrement permissive.
Le registre de l'annexe D (99_zz_registre.py) reprend ces en-têtes.
"""
import re

CORRECTIONS = []
ORDRE = ['DOIT', 'NE DOIT PAS', 'DEVRAIT', 'NE DEVRAIT PAS']
NORME = {'DOIVENT': 'DOIT', 'NE DOIVENT PAS': 'NE DOIT PAS', 'DEVRAIENT': 'DEVRAIT', 'NE DEVRAIENT PAS': 'NE DEVRAIT PAS',
         'PEUVENT': 'PEUT', 'NE PEUT PAS': 'NE DOIT PAS', 'NE PEUVENT PAS': 'NE DOIT PAS'}
BLOC = re.compile(r'(<div id="exig-[^"]+">\s*<p><strong><code>(EXIG-[A-Z0-9]{3}-\d{2})</code> · )([^<]*)(</strong></p>)'
                  r'(.*?)(?=<div id="pourquoi)', re.S)
FORCE = re.compile(r'<strong>((?:NE )?(?:DOIT|DOIVENT|DEVRAIT|DEVRAIENT|PEUT|PEUVENT)(?: PAS)?)</strong>')
JOURNAL = []


def transformer(s):
    changes, retires = [], []

    def entete(m):
        forces = {NORME.get(x, x) for x in FORCE.findall(m.group(5))}
        h = ' · '.join(o for o in ORDRE if o in forces) or ('PEUT' if 'PEUT' in forces else m.group(3))
        if h != m.group(3):
            changes.append(m.group(2))
            retires.append(m.group(3))
        return m.group(1) + h + m.group(4) + m.group(5)

    s = BLOC.sub(entete, s)
    JOURNAL[:] = [('En-têtes des exigences (corps et annexe D)',
                   f'{len(changes)} en-têtes portent désormais toutes les forces de leur énoncé ('
                   + ', '.join(changes) + ').', ['4.68', '23-19'])]
    return s, retires
