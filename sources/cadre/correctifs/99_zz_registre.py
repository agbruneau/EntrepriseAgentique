"""Annexe D : registre des exigences régénéré à partir des blocs EXIG du corps corrigé.

S'applique après tous les autres modules : identifiant, force et titre de chaque ligne
sont repris du bloc de l'exigence, dans l'ordre du document, de sorte que les exigences
ajoutées, les forces et les titres modifiés par la revue du 3 novembre 2026 y figurent.
Le contrôle échoue si un bloc est mal formé ou si un identifiant apparaît deux fois.
"""
import collections, re

CORRECTIONS = []
JOURNAL = []

BLOC = re.compile(r'<div id="exig-[^"]+">\s*<p><strong><code>(EXIG-[A-Z0-9]{3}-\d{2})</code> · '
                  r'((?:NE )?(?:DOIT|DEVRAIT|PEUT)(?: PAS)?(?: · (?:NE )?(?:DOIT|DEVRAIT|PEUT)(?: PAS)?)*)'
                  r'</strong></p>\s*<p><strong>(.*?)</strong></p>', re.S)


def transformer(s):
    i = s.index('<h2>D Registre des exigences</h2>')
    j = s.index('<h2>E ', i)
    corps = s[:i]
    blocs = BLOC.findall(corps)
    nb = corps.count('<div id="exig-')
    assert len(blocs) == nb, f'registre : {nb} blocs EXIG, {len(blocs)} lisibles'
    doublons = [k for k, n in collections.Counter(b[0] for b in blocs).items() if n > 1]
    assert not doublons, f'registre : identifiants en double {doublons}'
    d = s[i:j]
    t0 = d.index('<tbody>') + len('<tbody>')
    t1 = d.rindex('</tbody>')
    assert d.count('<tbody>') == 1, 'registre : plusieurs tableaux'
    anciens = d[t0:t1]
    lignes = ''.join(f'<tr><td><code>{x}</code></td><td><strong>{f}</strong></td><td>{t}</td></tr>'
                     for x, f, t in blocs)
    d = d[:t0] + lignes + d[t1:]
    # décompte cité dans l'introduction, s'il y figure
    JOURNAL[:] = [('Annexe D', f'Registre régénéré à partir des blocs du corps : {len(blocs)} exigences, '
                   'forces et titres repris de la version 1.2.', ['A-30', '6.114'])]
    return s[:i] + d + s[j:], [anciens]
