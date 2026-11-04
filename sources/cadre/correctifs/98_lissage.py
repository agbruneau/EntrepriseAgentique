"""Passe de lissage de la revue du 3 novembre 2026 : coutures entre les six tranches.

S'applique après les modules 01 à 06 et avant 99_registre.py (qui régénère les lignes de
l'annexe D à partir des blocs EXIG; les titres retouchés ici y passent d'eux-mêmes).
Chaque passage d'origine est repris du corps déjà corrigé par les tranches. Aucun
identifiant, numéro de tableau, de figure ou de référence n'est modifié, ni le texte des
figures (légendes des figures 22 et 25 comprises).
"""
NBSP = '\xa0'


def T(s):
    """Typographie du corps : apostrophe courbe, insécables devant « : » et à l'intérieur des guillemets."""
    s = s.replace("'", '’')
    s = s.replace(' :', NBSP + ':')
    s = s.replace('« ', '«' + NBSP).replace(' »', NBSP + '»')
    return s


L = ['lissage']

_C = [
    # ---------------------------------------------------------------- 1. champ compensation (C.2)
    ("référencé par le champ <code>compensation</code> de l'outil d'origine (annexe C, C.1).",
     "référencé par le champ <code>compensation</code> de l'entrée de catalogue de l'outil d'origine (annexe C, C.2).",
     ['A-08', 'lissage']),

    # ---------------------------------------------------------------- 2. décompte des références (A-31)
    ("L'annexe G compte 473 entrées, doublons compris, chaque doublon étant signalé dans son entrée; l'écart entre ce total et la somme des deux dernières populations n'est pas réconcilié dans la présente version.",
     "L'annexe G compte 473 entrées, dont 25 doublons signalés (448 sources distinctes); l'écart de 45 entrées entre l'audit final et l'annexe G n'est pas ventilé dans la présente version (annexe F.1).",
     ['A-31', 'lissage']),
    ("et l'annexe G compte 473 entrées, doublons compris (annexe F.1).</li>",
     "et l'annexe G compte 473 entrées, dont 25 doublons signalés (448 sources distinctes; annexe F.1).</li>",
     ['A-31', 'lissage']),
    ("La liste compte 473 entrées, dont 25 doublons signalés (« Même source que [n] »); les numéros",
     "La liste compte 473 entrées, dont 25 doublons signalés (« Même source que [n] »), soit 448 sources distinctes; les numéros",
     ['A-31', 'lissage']),

    # ---------------------------------------------------------------- 3. N4 et agents ambiants (A-27)
    # Le § 3.3 et le glossaire admettent un agent ambiant N1 ou N2; le refus vise l'écriture
    # sans approbation d'un agent non N4 sur une tâche autodéclenchée, non la tâche elle-même.
    ("et refuse une tâche autodéclenchée à un agent qui n'est pas N4;",
     "et refuse à un agent qui n'est pas N4 toute écriture sans approbation au titre d'une tâche ainsi déclenchée;",
     ['A-27', 'lissage']),
    ("La passerelle lit l'origine de la tâche et refuse une tâche ainsi déclenchée pour un agent qui n'est pas N4.</td>",
     "La passerelle lit l'origine de la tâche et refuse à un agent qui n'est pas N4 toute écriture sans approbation au titre d'une tâche ainsi déclenchée.</td>",
     ['A-27', 'lissage']),
    ("ainsi que toute tâche déclenchée sans demande d'une personne pour un agent qui n'est pas N4, d'après l'attribut d'origine posé par l'orchestrateur ou par le courtier.</p>",
     "ainsi que, pour un agent qui n'est pas N4, toute écriture sans approbation au titre d'une tâche déclenchée sans demande d'une personne, d'après l'attribut d'origine posé par l'orchestrateur ou par le courtier; un agent ambiant N1 ou N2 peut donc traiter une telle tâche (section 3.3).</p>",
     ['A-27', 'lissage']),
    ("N4 autonomie étendue sous ODD certifié, qui couvre les tâches déclenchées sans demande d'une personne (événement, horaire),",
     "N4 autonomie étendue sous ODD certifié, qui couvre l'exécution sans approbation de tâches déclenchées sans demande d'une personne (événement, horaire),",
     ['A-27', 'lissage']),

    # ---------------------------------------------------------------- 4. étages E1 à E3 et jalons (A-27)
    ("extensions CloudEvents, évaluation en trois paliers, exemples de contrats.</td>",
     "extensions CloudEvents, évaluation en trois étages, exemples de contrats.</td>",
     ['A-27', 'lissage']),
    ("<p><strong>Paliers franchis et relancés à chaque changement</strong></p>\n<p>Tout agent",
     "<p><strong>Étages franchis et relancés à chaque changement</strong></p>\n<p>Tout agent",
     ['A-27', 'lissage']),
    ("<h3>11.5 Cycle de vie et points de contrôle</h3>",
     "<h3>11.5 Cycle de vie et jalons</h3>",
     ['A-27', 'lissage']),
    ("<p><strong>Points de contrôle consignés</strong></p>\n<p>Un agent",
     "<p><strong>Jalons du cycle de vie consignés</strong></p>\n<p>Un agent",
     ['A-27', 'lissage']),
    ("<td><em>checkpoint; gate</em></td><td>(1) Instantané persistant de l'état complet d'une tâche, pris à chaque transition par le moteur d'exécution durable; il constitue une frontière de confiance et se protège comme une donnée de production. (2) Jalon du cycle de vie d'un agent, de la proposition au retrait, dont le franchissement est consigné au registre avec ses preuves; pour éviter l'homonymie, le cadre dit « jalon » en ce sens. Voir les sections 7.4 et 11.5.</td>",
     "<td><em>checkpoint</em></td><td>(1) Instantané persistant de l'état complet d'une tâche, pris à chaque transition par le moteur d'exécution durable; il constitue une frontière de confiance et se protège comme une donnée de production. (2) Dans le journal d'audit, état signé et daté de la tête d'un flux (numéro de séquence, empreinte), publié hors du domaine d'administration du service d'audit (EXIG-OBS-12). Le terme ne désigne pas les jalons du cycle de vie d'un agent (section 11.5), que la figure 25 nomme encore « points de contrôle ». Voir les sections 7.4, 10.3 et 11.5.</td>",
     ['A-27', 'A-19', 'lissage']),

    # ---------------------------------------------------------------- 5. définitions
    ("de point de contrôle ou d'artefact étiqueté après la contamination.</td><td>Cadre (section 9.6)</td>",
     "de point de contrôle ou d'artefact étiqueté postérieur à la contamination.</td><td>Cadre (section 9.6)</td>",
     ['A-17', 'lissage']),
    # « session » au sens d'A-17 (tâche racine) n'est pas la session d'authentification de l'approbateur
    ("obtenue hors bande, c'est-à-dire sur un appareil et dans une session distincts de ceux de l'agent,",
     "obtenue hors bande, c'est-à-dire sur un appareil et dans une session d'authentification distincts de ceux de l'agent,",
     ['A-12', 'A-17', 'lissage']),
    ("<td>Se dit d'une approbation donnée sur un appareil et dans une session distincts de ceux de l'agent,",
     "<td>Se dit d'une approbation donnée sur un appareil et dans une session d'authentification distincts de ceux de l'agent (et non une session au sens des EXIG-SEC-04 et EXIG-SEC-06),",
     ['A-12', 'A-17', 'lissage']),
    ("<tr><td><strong>Injection d'instructions</strong>",
     "<tr><td><strong>Incident grave</strong></td><td><em>serious incident</em></td><td>Au sens du cadre, tout incident de gravité S1 ou S2, sur l'échelle S1 à S4 qu'attribue la fonction risques et conformité, ainsi que tout incident grave au sens du RIA (art. 3(49)). Il déclenche notamment la réévaluation de l'EXIG-GOV-12. Voir la section 12.8.</td></tr><tr><td><strong>Injection d'instructions</strong>",
     ['lissage']),
    ("une révision extraordinaire suit tout incident agentique grave ou changement réglementaire majeur.",
     "une révision extraordinaire suit tout incident grave (section 12.8) ou changement réglementaire majeur.",
     ['lissage']),

    # ---------------------------------------------------------------- 6. nouvelles exigences et renvois
    # EXIG-OBS-14 : même contenu du dossier que l'EXIG-CON-09
    ("les RP en entrée, les versions de l'agent, du modèle et des outils, les facteurs retenus et les approbations. Le dossier est distinct",
     "les RP en entrée, les résultats d'outils qui ont servi à décider, les versions de l'agent, du modèle et des outils, les facteurs retenus et les approbations. Le dossier est distinct",
     ['A-18', 'lissage']),
    # EXIG-EVT-11 et EXIG-ORC-04 : même règle de profondeur pour un saut d'événement
    ("un tel saut compte dans la profondeur de délégation de l'EXIG-ORC-04.</p>",
     "un saut exécuté sous la délégation que référence l'événement compte comme un niveau dans la profondeur de délégation de l'EXIG-ORC-04.</p>",
     ['A-02', 'A-16', 'lissage']),
    ("Un saut d'événement qui agit pour une personne compte comme un niveau (EXIG-EVT-11).</p>",
     "Un saut d'événement exécuté sous la délégation que référence l'événement compte comme un niveau (EXIG-EVT-11).</p>",
     ['A-02', 'A-16', 'lissage']),
    # EXIG-CON-10, table unique des durées (A-24) : le dépôt d'évaluation de l'EXIG-EVA-07 y manquait
    ("captures de débogage, 14 jours au plus (EXIG-OBS-08). À l'échéance,",
     "captures de débogage, 14 jours au plus (EXIG-OBS-08); dépôt d'évaluation, durée bornée à la fiche, 30 jours par défaut (EXIG-EVA-07). À l'échéance,",
     ['A-18', 'A-24', 'lissage']),

    # ---------------------------------------------------------------- 7. décomptes (A-30)
    ("l'annexe D récapitule toutes les exigences dans l'ordre du document.",
     "l'annexe D récapitule toutes les exigences dans l'ordre du document, soit 296 dans la version 1.2 (287 dans la version 1.1).",
     ['A-30', 'lissage']),
    ("avec la force de leur bloc (DOIT, NE DOIT PAS, DEVRAIT).",
     "avec la force de leur bloc (DOIT, NE DOIT PAS, DEVRAIT), soit 296 exigences dans la version 1.2 (287 dans la version 1.1).",
     ['A-30', 'lissage']),

    # ---------------------------------------------------------------- 8. autres coutures
    # § 1.6 et § 6.3 alignés sur les déclencheurs de l'EXIG-GOV-18 (A-22)
    ("(EXIG-GOV-18, sections 6.3 et 11.7); la publication d'une version incompatible ou d'une dépréciation d'un standard adopté, ou un correctif de sécurité, déclenche une révision extraordinaire.",
     "(EXIG-GOV-18, sections 6.3 et 11.7); pour un standard au statut Adopter ou Contenir, la publication d'une version incompatible, d'une dépréciation, d'un retrait accéléré ou d'un correctif de sécurité déclenche une révision extraordinaire, dans les 15 jours ouvrables.",
     ['A-22', 'lissage']),
    ("(EXIG-GOV-18, section 11.7); la publication d'une version incompatible ou d'une dépréciation d'un standard adopté, ou un correctif de sécurité, déclenche une révision extraordinaire.",
     "(EXIG-GOV-18, section 11.7); pour un standard au statut Adopter ou Contenir, la publication d'une version incompatible, d'une dépréciation, d'un retrait accéléré ou d'un correctif de sécurité déclenche une révision extraordinaire, dans les 15 jours ouvrables.",
     ['A-22', 'lissage']),
    # « propriétaire » employé seul pour un agent (A-34) : parrain ou responsable technique
    ("Dans le cadre, « propriétaire » ne s'emploie jamais seul :",
     "Dans le cadre, pour un agent, « propriétaire » ne s'emploie jamais seul :",
     ['A-34', 'lissage']),
    ("inventaire de tous les agents et serveurs MCP, propriétaire nommé pour chacun,",
     "inventaire de tous les agents et serveurs MCP, parrain nommé pour chacun,",
     ['A-34', 'lissage']),
    ("<td>Agents créés hors inventaire, sans propriétaire nommé ni moyen de révocation</td>",
     "<td>Agents créés hors inventaire, sans parrain nommé ni moyen de révocation</td>",
     ['A-34', 'lissage']),
    ("un agent créé ou exploité hors du registre, sans propriétaire nommé ni moyen de révocation;",
     "un agent créé ou exploité hors du registre, sans parrain nommé ni moyen de révocation;",
     ['A-34', 'lissage']),
    ("une fiche par élément, avec propriétaire nommé, finalité,",
     "une fiche par élément, avec parrain nommé, finalité,",
     ['A-34', 'lissage']),
    ("<td>EXIG-GOV</td><td>Propriétaire nommé, attestation à jour</td>",
     "<td>EXIG-GOV</td><td>Parrain nommé, attestation à jour</td>",
     ['A-34', 'lissage']),
    ("le niveau d'autonomie (N0 à N4), le propriétaire et l'état du cycle de vie de chaque agent",
     "le niveau d'autonomie (N0 à N4), le parrain, le responsable technique et l'état du cycle de vie de chaque agent",
     ['A-34', 'lissage']),
    ("registre avec propriétaire nommé (section 11.4);",
     "registre avec parrain nommé (section 11.4);",
     ['A-34', 'lissage']),
    ("<td>Risques et conformité, responsable de la protection des RP, propriétaires</td>",
     "<td>Risques et conformité, responsable de la protection des RP, propriétaires métier</td>",
     ['A-34', 'lissage']),
    # environnement serveur : même définition que le tableau 7 (A-01)
    ("sans justificatif de production (développement partagé, préproduction, production), un serveur MCP",
     "sans justificatif de production (environnement serveur, tableau 7), un serveur MCP",
     ['A-01', 'lissage']),
    ("<strong>Rien ne contourne les points d'application.</strong> Hors d'un poste de développement individuel, tout appel",
     "<strong>Rien ne contourne les points d'application.</strong> Hors d'un poste de développement individuel sans justificatif de production, tout appel",
     ['A-01', 'lissage']),
    ("Sa règle centrale est simple : hors d'un poste de développement individuel, tout appel",
     "Sa règle centrale est simple : hors d'un poste de développement individuel sans justificatif de production, tout appel",
     ['A-01', 'lissage']),
]

CORRECTIONS = [(T(a), T(b), k) for a, b, k in _C]

_J = [
    ('EXIG-ORC-17', 'Le champ compensation est situé à l’entrée de catalogue (C.2), et non à la définition MCP (C.1).', ['A-08', 'lissage']),
    ('Méthode, section 1.7 et annexe G', 'Décompte aligné sur l’annexe F : 473 entrées, dont 25 doublons signalés (448 sources distinctes); écart de 45 entrées non ventilé.', ['A-31', 'lissage']),
    ('Section 3.1, tableau 28, EXIG-AUT-01, glossaire (Niveau d’autonomie)', 'Refus de la passerelle limité à l’écriture sans approbation d’un agent non N4 sur une tâche autodéclenchée, conformément au § 3.3 (agent ambiant N1 ou N2 admis).', ['A-27', 'lissage']),
    ('Historique (version 0.2), EXIG-EVA-01', '« Paliers » d’évaluation renommés « étages ».', ['A-27', 'lissage']),
    ('Section 11.5, EXIG-GOV-11, glossaire (Point de contrôle)', 'Titres renommés en « jalons »; l’entrée du glossaire ne garde que l’exécution durable et ajoute le point de contrôle du journal d’audit (EXIG-OBS-12).', ['A-27', 'A-19', 'lissage']),
    ('Tableau 7 (Session)', 'Formulation alignée sur le glossaire (« postérieur à la contamination »).', ['A-17', 'lissage']),
    ('EXIG-AUT-09, glossaire (Hors bande)', 'Session d’authentification distinguée de la session au sens des EXIG-SEC-04 et SEC-06.', ['A-12', 'A-17', 'lissage']),
    ('Glossaire, section 1.6', 'Entrée « Incident grave » ajoutée (S1 ou S2, ou incident grave au sens du RIA, section 12.8); « incident agentique grave » ramené à ce terme.', ['lissage']),
    ('EXIG-OBS-14', 'Contenu du dossier aligné sur l’EXIG-CON-09 (résultats d’outils qui ont servi à décider).', ['A-18', 'lissage']),
    ('EXIG-EVT-11, EXIG-ORC-04', 'Même règle de profondeur : le saut d’événement exécuté sous la délégation référencée compte comme un niveau.', ['A-02', 'A-16', 'lissage']),
    ('EXIG-CON-10', 'Dépôt d’évaluation (EXIG-EVA-07) ajouté à la table unique des durées.', ['A-18', 'A-24', 'lissage']),
    ('Section 1.5, annexe D', 'Total indiqué : 296 exigences en version 1.2, 287 en version 1.1.', ['A-30', 'lissage']),
    ('Sections 1.6 et 6.3', 'Déclencheurs de la révision extraordinaire alignés sur l’EXIG-GOV-18 (statuts Adopter et Contenir, retrait accéléré, 15 jours ouvrables).', ['A-22', 'lissage']),
    ('Par où commencer, sections 2.3, 3.1 (tableau 7), 4.2, 5.3, 12.6 et 15.2, glossaire (Agent fantôme), section 11.1', '« Propriétaire » employé seul pour un agent remplacé par « parrain » ou « propriétaire métier »; règle de la section 11.1 limitée aux agents.', ['A-34', 'lissage']),
    ('Décision 2, chapitre 5, EXIG-MCP-08', 'Exception du poste de développement et environnement serveur alignés sur le tableau 7 et l’EXIG-ARC-01.', ['A-01', 'lissage']),
]

JOURNAL = [(a, T(b), k) for a, b, k in _J]
