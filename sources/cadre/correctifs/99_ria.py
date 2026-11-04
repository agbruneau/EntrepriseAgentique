"""Règlement (UE) 2026/1744 : réserves levées sur ses dates (orchestrateur, 4 novembre 2026).

Le 4 novembre 2026, les extraits du texte publié au Journal officiel (L, 24.7.2026), indexés
depuis EUR-Lex, confirment le titre, la date du 8 juillet 2026 et l'application du chapitre
III, sections 1 à 3, au 2 décembre 2027 pour l'annexe III et au 2 août 2028 pour l'annexe I;
une source secondaire (ActuIA) concorde, avec l'entrée en vigueur au 27 juillet 2026 et la
transition de l'article 50(2) au 2 décembre 2026. EUR-Lex reste illisible pour l'outillage :
le texte intégral n'est pas relu, ce que le cadre continue de dire.
"""

CORRECTIONS = [
    ('l’annexe III, date à confirmer par la relecture de ce règlement au Journal officiel (annexe H)',
     'l’annexe III, date confirmée le 4 novembre 2026 sur des extraits du texte publié au Journal officiel '
     '(annexe H, section H.6)', ['lit. 22', '5.88']),
    ('les dates qui découlent du règlement (UE) 2026/1744 sont à confirmer sur le texte publié au Journal officiel '
     'avant de geler le jalon 2a.',
     'les dates qui découlent du règlement (UE) 2026/1744 ont été confirmées le 4 novembre 2026 sur des extraits du '
     'texte publié au Journal officiel; le comité les revérifie sur le texte intégral avant de geler le jalon 2a.',
     ['lit. 22', '5.88']),
    ('Texte non relu au Journal officiel lors de la revue du 3 novembre 2026 (EUR-Lex inaccessible); les dates '
     'd’application sont citées d’après [57].',
     'Titre, date et dates d’application (2 décembre 2027 pour l’annexe III, 2 août 2028 pour l’annexe I) '
     'confirmés le 4 novembre 2026 sur des extraits du texte indexés depuis EUR-Lex; entrée en vigueur le 27 juillet '
     '2026 et transition de l’article 50(2) au 2 décembre 2026 selon la Commission [57]; texte intégral non relu, '
     'EUR-Lex restant inaccessible à l’outillage.', ['lit. 22', '6.30']),
]

JOURNAL = [
    ('§ 2.4, § 15.1 et référence [58] (règlement (UE) 2026/1744)',
     'Réserves « à confirmer » levées : le titre, la date du 8 juillet 2026, la publication au JO le 24 juillet 2026 '
     'et les dates d’application du haut risque (annexe III : 2 décembre 2027; annexe I : 2 août 2028) sont confirmés '
     'le 4 novembre 2026 sur des extraits du texte indexés depuis EUR-Lex, et une source secondaire concorde. Le texte '
     'intégral n’a pas pu être relu (EUR-Lex illisible pour l’outillage); le comité le revérifie avant de geler J2a.',
     ['lit. 22', '5.88', '6.30']),
]
