"""Version 1.2 du 3 novembre 2026 : ligne de l'historique des versions (orchestrateur)."""
NBSP = '\xa0'

LIGNE_12 = (
    '<tr><td><strong>1.2</strong></td><td><strong>3' + NBSP + 'nov.' + NBSP + '2026</strong></td><td>'
    '<strong>Revue contradictoire du 3 novembre 2026</strong>' + NBSP + ': application, à leur place, '
    'des correctifs de la revue (29 audits de tranche, consolidation en 623 défauts, dont 14 bloquants, '
    'audit bibliographique de 83 faits) et des 34 arbitrages transversaux qu’elle retient. Portée unique '
    'de la passerelle d’agents, étendue au courtier d’événements; régime des agents intégrés aux '
    'logiciels-services; canal de compensation qui traverse le coupe-circuit, le mode fermé et les '
    'plafonds; jeton d’approbation compté par opération; canonisation stricte et seuils sur grandeur '
    'vérifiée; propagation du marquage de contenu non fiable à l’échelle du système; régimes du contenu '
    '(télémétrie, débogage, dossier de décision, évaluation); ancrage externe du journal d’audit; '
    'force normative des méta-règles et régime transitoire. Neuf exigences ajoutées (EXIG-ARC-26, '
    'EXIG-EVT-11, EXIG-ORC-31, EXIG-AUT-24, EXIG-IAM-22, EXIG-OBS-14, EXIG-EVA-07, EXIG-GOV-21, '
    'EXIG-APP-18), 296 au total; errata de l’annexe H reportés dans le corps; brouillons IETF réépinglés. '
    'Le détail des correctifs figure à la section H.6.</td></tr>'
)

CORRECTIONS = [
    # historique : la 1.1 n'est plus la version courante; ligne 1.2 ajoutée
    ('<td><strong>1.1</strong></td><td><strong>28' + NBSP + 'oct.' + NBSP + '2026</strong></td>',
     '<td>1.1</td><td>28' + NBSP + 'oct.' + NBSP + '2026</td>', ['A-31']),
    ('et article 65.2 de la Loi sur l’accès ajouté aux critères de la classe élevée. Modifications '
     'corrélatives' + NBSP + ': sommaire, figure 1, sections 1.1, 3.1, 4.1 et 14.2, EXIG-AUT-02, annexe F.</td></tr>',
     'et article 65.2 de la Loi sur l’accès ajouté aux critères de la classe élevée. Modifications '
     'corrélatives' + NBSP + ': sommaire, figure 1, sections 1.1, 3.1, 4.1 et 14.2, EXIG-AUT-02, annexe F.</td></tr>'
     + LIGNE_12, ['A-31']),
]

JOURNAL = [
    ('Historique des versions', 'Ligne de la version 1.2 ajoutée; la version 1.1 n’est plus marquée comme courante.',
     ['A-31']),
    ('Fiche du document, en-tête et pied de page', 'Version et date portées à « 1.2 — 3 novembre 2026 ».', ['A-31']),
]
