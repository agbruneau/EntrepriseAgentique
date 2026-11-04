"""Légendes et renvois alignés sur les libellés corrigés dans les schémas (orchestrateur).

Les libellés d'une ligne des figures 1, 2, 3, 4, 13, 22, 25 et 28 sont corrigés dans le
dessin même (construire_pdf.py, LIBELLES). Ce module retire des légendes et du texte les
mentions d'écart devenues fausses; les écarts de structure (flèches, branches, ordre des
étapes) restent corrigés par la légende, comme le consignent les modules 01 à 06.
"""
NBSP = '\xa0'

CORRECTIONS = [
    # § 10.4 : la figure 22 dit désormais « étages »
    ('en trois étages, E1 à E3 (figure 22, qui les nomme «' + NBSP + 'paliers' + NBSP + '»).',
     'en trois étages, E1 à E3 (figure 22).', ['A-27']),
    # figure 22 : légende
    ('</strong> Le palier 1 vérifie les contrats à chaque modification, le palier 2 mesure les trajectoires sur un '
     'jeu de référence en préproduction, le palier 3 échantillonne la production.',
     '</strong> L’étage E1 vérifie les contrats à chaque modification, l’étage E2 mesure les trajectoires sur un '
     'jeu de référence en préproduction, l’étage E3 échantillonne la production.', ['A-27']),
    (' Le texte nomme ces paliers «' + NBSP + 'étages' + NBSP + '» (E1 à E3), et l’étage E3 évalue aussi toutes les '
     'traces qui ont atteint un plafond (EXIG-EVA-04).',
     ' L’étage E3 évalue aussi toutes les traces qui ont atteint un plafond (EXIG-EVA-04).', ['A-27']),
    # figure 13 : le dessin montre désormais la préautorisation compensable
    (' Le dessin simplifie deux points, que le texte corrige.', '', ['A-06']),
    ('T3 se lit «' + NBSP + 'préautoriser le paiement, sans capture' + NBSP + '», étape compensable (P2) par '
     'l’annulation de la préautorisation,',
     'T3 préautorise donc le paiement, sans capture, étape compensable (P2) par l’annulation de la préautorisation,',
     ['A-06']),
    # figure 25 : le dessin dit désormais « jalons du cycle de vie »
    ('un jalon du cycle de vie («' + NBSP + 'point de contrôle' + NBSP + '» dans la figure) consigné au registre;',
     'un jalon du cycle de vie consigné au registre;', ['A-27']),
    # figure 28 : la ligne de la passerelle d'agents s'ouvre désormais au palier P3
    ('La ligne de la passerelle d’agents s’arrête au palier P2' + NBSP + ': la passerelle s’ouvre aussi au palier P3, '
     'avec l’approbation signée',
     'La passerelle d’agents s’ouvre au palier P3, avec l’approbation signée', ['A-26']),
]

JOURNAL = [
    ('Figures 1, 2, 3, 4, 13, 22, 25 et 28 (dessins)',
     'Libellés corrigés dans le schéma même, dans sa police d’origine : audit « chaîné et ancré », évaluation en '
     '« étages » E1 à E3, « Risques, conformité et approvisionnement », « BSIF E-23 », « un point d’application », '
     'isolation « par mandant ou par locataire », état « qui n’existe qu’en mémoire de processus », T3 « Préautoriser '
     'le paiement · compensable (P2) », « 50 scénarios au moins », « Jalons du cycle de vie », pilote « du niveau '
     'inférieur au visé », passerelle d’agents « P0 à P3 », « inventaire E-23 ». Ces libellés remplacent, pour ces '
     'figures, les mentions « figure non modifiable » des lignes précédentes; les écarts de structure (flèches, '
     'branches et ordre des étapes, notamment des figures 9, 12, 14, 16 et 26) restent corrigés par la légende, qui '
     'fait foi.', ['A-06', 'A-19', 'A-26', 'A-27', 'lissage']),
    ('Légendes des figures 13, 22, 25 et 28; § 10.4',
     'Mentions d’écart devenues fausses retirées, après la correction des libellés du dessin.', ['lissage']),
]
