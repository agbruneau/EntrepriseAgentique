"""Dernier correctif de fond (22-23) et suivi des constats non retenus aux étapes antérieures.

SUIVI donne, pour les constats qu'un module a laissés « non retenus » et qu'un module
ultérieur ou un arbitrage a corrigés sous d'autres numéros, où ils l'ont été; section_h6()
les classe au tableau 73. FAUX liste les constats démontrés faux, seuls à rester au
tableau 74 : ils n'appellent aucun correctif.
"""

CORRECTIONS = [
    # 22-23 : la carte C.3 présente un agent qui recommande sans décider; le scénario du § 6.6
    # l'alignait sur une décision inscrite
    ('<li>Prêt à inscrire sa décision, il passe à <code>INPUT_REQUIRED</code>',
     '<li>Prêt à inscrire sa recommandation motivée (il n’accorde ni ne refuse aucun crédit, carte C.3), il passe à '
     '<code>INPUT_REQUIRED</code>', ['22-23']),
]

JOURNAL = [
    ('§ 6.6, déroulement d’une délégation, étape 6',
     'L’agent crédit inscrit une recommandation motivée, non une décision, comme le dit sa carte (C.3).', ['22-23']),
]

# constat d'origine : où il est corrigé
SUIVI = {
    '1.10': 'tableau 50, colonne BSIF et E-23 (module 05_t5); la décision 10 est exacte',
    '01-03': 'tableau 50, colonne BSIF et E-23 (module 05_t5)',
    '03-12': 'EXIG-AUT-07 ajoutée aux non-dérogeables de l’EXIG-GOV-17 et à l’annexe A (module 99_t8_tableaux)',
    '1.27': 'EXIG-AUT-07 ajoutée aux non-dérogeables (module 99_t8_tableaux)',
    '1.90': 'version 1.2, fiche, en-tête et historique (module 00_version et construire_pdf.py)',
    '01-15': 'version 1.2 et ligne d’historique (module 00_version)',
    '1.92': 'historique 1.2 : inventaire E-23 au lieu d’une validation initiale (module 99_t8_tableaux)',
    '01-21': 'historique 1.2 et § 15.1 : inventaire E-23 (modules 05_t5 et 99_t8_tableaux)',
    '1.94': 'figure 1 corrigée dans le dessin (construire_pdf.py, LIBELLES)',
    '01-18': 'figure 1 corrigée dans le dessin (construire_pdf.py, LIBELLES)',
    '28-05': 'version 1.2, historique, et « huit annexes, de A à H » au § 1.5 (modules 00_version et 01_t1)',
    '5.08': 'corrigé par l’arbitrage A-24 dans l’EXIG-GOV-12 (ancienne version en service, sinon suspension), '
            'au lieu de la voie d’urgence proposée',
    '5.51': 'corrigé par l’arbitrage A-24 : source unique des déclencheurs à l’EXIG-GOV-12, à laquelle renvoient '
            'les autres listes',
    '5.41': 'corrigé par l’arbitrage A-26 : exigibilité par capacité et forme minimale de A.1',
    '5.39': 'corrigé dans les cinq dimensions existantes (critères de supervision et de réversibilité), sans '
            'sixième dimension',
    '12-13': 'corrigé par la confirmation du mandant (EXIG-AUT-15), l’envoi externe restant P3 selon A-27',
}

FAUX = {'06-18', '07-13', '08-15', '09-18', '09-27', '10-41', '18-24', '21-29', 'audit_28, note finale'}


def transformer(s):
    """Préfixe DNS inversé des attributs d'entreprise : ca.ent (domaine ent.ca), comme les types
    d'événements CloudEvents (constats 08-13, 22-17)."""
    n = s.count('ca.entreprise.')
    JOURNAL[1:] = [('§ 10.1, § 10.3, figure 21, annexes B et C', f'Préfixe des attributs d’entreprise aligné sur le '
                    f'domaine ent.ca : « ca.entreprise. » devient « ca.ent. » ({n} occurrences, figure 21 comprise).',
                    ['08-13', '22-17'])]
    return s.replace('ca.entreprise.', 'ca.ent.'), ['ca.entreprise.'] * n
