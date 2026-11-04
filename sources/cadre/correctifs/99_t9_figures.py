"""Légendes et texte alignés sur les figures corrigées dans le dessin même (tranche t9).

Les écarts que les modules 01 à 06 consignaient « figure non modifiable » sont corrigés dans le
schéma (construire_pdf.py, LIBELLES : libellés, lignes ajoutées, flèches et cases redessinées) pour
les figures 1, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 23 et 26. Ce module retire des
légendes et du texte les mentions d'écart devenues fausses (« le schéma simplifie », « le texte
fait foi là où la figure diffère », etc.).
"""
NBSP = '\xa0'

CORRECTIONS = [
    # figure 6 : le bandeau dit désormais « À surveiller ou à contenir » et « OAuth 2.0 (RFC 9700) »
    ('et ce qui reste en veille; le bandeau de veille réunit des entrées aux statuts Évaluer (pilotes) et '
     'Surveiller (hors production), et «' + NBSP + 'OAuth 2.x' + NBSP + '» y désigne OAuth 2.0 profilé par la '
     'RFC 9700, le profil OAuth 2.1 restant un brouillon.',
     'et ce qui reste à surveiller ou à contenir' + NBSP + ': le commerce et les paiements agentiques au statut '
     'Surveiller (veille hors production), les formats propres à un fournisseur au statut Contenir (usage existant '
     'derrière un adaptateur). OAuth 2.0 y est profilé par la RFC 9700, le profil OAuth 2.1 restant un brouillon.',
     ['05-12', '05-13']),
    # figure 9 : étape 7 en flux continu, jeton remis à la passerelle, couloir « Personnes »
    ('Le texte qui suit fait foi là où la figure diffère' + NBSP + ': l’étape 7 emploie '
     '<code>SendStreamingMessage</code>, le jeton d’approbation reste à la passerelle, et l’utilisateur et '
     'l’approbateur, réunis dans un même couloir, sont deux rôles distincts.',
     'Le couloir «' + NBSP + 'Personnes' + NBSP + '» réunit l’utilisateur et l’approbateur, deux rôles distincts '
     '(section 8.5); le jeton d’approbation reste à la passerelle, qui n’en communique que la référence, donnée '
     'non secrète.', ['08-01', '08-09']),
    # section 7.3 et figure 12 : l'arbre redessiné applique les trois règles
    ('L’arbre se lit sous trois règles, qui priment sur le dessin de la figure. D’abord',
     'L’arbre applique trois règles. D’abord', ['09-23']),
    ('Enfin, deux feuilles absentes du dessin sont admises' + NBSP + ': la chaîne séquentielle',
     'Enfin, deux feuilles complètent les patrons de base' + NBSP + ': la chaîne séquentielle', ['09-23']),
    ('la première réponse qui conclut fixe le patron, sous les trois règles du texte qui précède' + NBSP + ': le '
     'déclenchement par événement ne mène pas à lui seul à la chorégraphie, l’agent unique se teste avant le '
     'routage, et la chaîne séquentielle et le clavardage de groupe restent admis. Les encadrés du bas '
     's’ajoutent à n’importe quel patron',
     'la première réponse qui conclut fixe le patron. Le mode de déclenchement n’y entre pas' + NBSP + ': seule la '
     'réaction de plusieurs domaines faiblement couplés à un même fait mène à la chorégraphie, et l’agent unique '
     'se teste avant le routage. L’encadré du haut, à droite, s’ajoute à n’importe quel patron', ['09-23']),
    # figure 14 : contrôles alignés sur le tableau 28
    (' En cas d’écart entre la figure et le tableau 28, le tableau fait foi' + NBSP + ': approbation hors bande '
     'des P3 dès N2, retour arrière rapide dès N3; la DLP indiquée en N1 n’est pas un contrôle minimal.',
     ' Le tableau 28 détaille les contrôles minimaux de chaque niveau.', ['11-19']),
    # section 8.4 et figure 15 : cumul des contrôles (EXIG-AUT-10), cellules harmonisées
    ('du palier de l’outil; la règle la plus stricte l’emporte.</p>',
     'du palier de l’outil; les contrôles se cumulent, et l’approbation la plus stricte l’emporte (EXIG-AUT-10).</p>',
     ['11-06']),
    (' «' + NBSP + 'Audit + revue' + NBSP + '» désigne une revue a posteriori par échantillonnage; les cellules P2 '
     'des classes faible et modérée énoncent la même règle (approbation au-delà du seuil déclaré).',
     '', ['11-20']),
    # figure 16 : jeton remis à la passerelle, rejeu avec la clé et la référence, champs du jeton
    (' Le dessin simplifie trois points, que l’EXIG-AUT-12 précise' + NBSP + ': à l’étape 5, le jeton est remis à '
     'la passerelle, qui le conserve, et non à l’agent; à l’étape 6, l’agent rejoue l’appel avec la même clé '
     'd’idempotence et la référence de la demande, donnée non secrète; le jeton porte aussi l’agent, l’identifiant '
     'jti et le rôle de l’approbateur, et une double approbation se fait par deux jetons sur le même h.',
     ' Le jeton est remis à la passerelle, qui le conserve (étape 5); l’agent rejoue l’appel avec la même clé '
     'd’idempotence et la référence de la demande, donnée non secrète (étape 6); une double approbation se fait '
     'par deux jetons sur le même h (EXIG-AUT-12).', ['12-01', '12-02', '12-08']),
    # figure 17 : second jeton, deux audiences, extrait et JWT-SVID dans le dessin
    (' Le schéma simplifie trois points que le texte précise' + NBSP + ': après vérification, la passerelle obtient '
     'pour le serveur un jeton qui la désigne comme client, sans ajouter de niveau d’<code>act</code> '
     '(EXIG-IAM-14); le serveur MCP et le système cible, réunis dans une même boîte, sont deux audiences '
     'distinctes (EXIG-IAM-12); le jeton représenté est un extrait, et «' + NBSP + 'SVID' + NBSP + '» y désigne le '
     'JWT-SVID présenté comme <code>actor_token</code>.',
     ' Après vérification, la passerelle obtient pour le serveur un second jeton, qui la désigne comme client sans '
     'ajouter de niveau d’<code>act</code> (EXIG-IAM-14); le serveur MCP et le système cible, réunis dans une même '
     'boîte, sont deux audiences distinctes (EXIG-IAM-12).', ['4.55', '4.06', 'A-16']),
    # figure 18 : intention, contrôles 5 à 7 et filtre dans le dessin
    ('À l’aller, sept contrôles s’appliquent dans l’ordre avant que l’appel n’atteigne l’outil ou le pair;',
     'À l’aller, sept contrôles s’appliquent dans l’ordre avant que l’appel n’atteigne l’outil ou le pair, la '
     'limitation de débit dès l’authentification;', ['4.62']),
    (' Le schéma simplifie trois points que la liste ci-dessous précise' + NBSP + ': pour un appel P2 ou P3, '
     'l’enregistrement d’intention est écrit avant le relais (EXIG-OBS-11), et non au seul retour; le contrôle 5 '
     'vise aussi toute écriture d’un agent de niveau N2; le contrôle 7 ne s’applique que lorsqu’une injection est '
     'prévue (EXIG-IAM-19). Au retour, le filtre masque la sortie; il n’annule pas un effet déjà produit.',
     ' Pour un appel P2 ou P3, l’enregistrement d’intention est écrit avant le relais (EXIG-OBS-11); le contrôle 5 '
     'vise aussi toute écriture d’un agent de niveau N2, et le contrôle 7 ne s’applique que lorsqu’une injection '
     'est prévue (EXIG-IAM-19).', ['4.11', '4.14', '4.61']),
    # figure 19 : approbation de l'action exacte et [B] élargi dans le dessin
    (' Le schéma abrège deux points que l’EXIG-SEC-04 précise' + NBSP + ': la «' + NBSP + 'supervision humaine'
     + NBSP + '» y est l’approbation de l’action exacte, et [B] y vise les données et les systèmes sensibles, en '
     'lecture comme en écriture.',
     ' Les propriétés sont celles de l’EXIG-SEC-04' + NBSP + ': [B] vise les données et les systèmes sensibles, en '
     'lecture comme en écriture.', ['4.69']),
    # figure 23 : cinq dimensions et alerte au responsable technique dans le dessin
    (' Le schéma omet le plafond d’étapes ou d’itérations de l’EXIG-ORC-26, et l’alerte qu’il attribue au «'
     + NBSP + 'propriétaire' + NBSP + '» va au responsable technique.',
     ' L’enveloppe porte les cinq dimensions de l’EXIG-ORC-26' + NBSP + ': étapes ou itérations, appels d’outils, '
     'jetons, coût et durée.', ['4.48', 'A-34']),
]

JOURNAL = [
    ('Figures 1, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 23 et 26 (dessins)',
     'Écarts corrigés dans le schéma même, aux couleurs et dans la police du schéma (IBM Plex Sans; les lignes en '
     'chasse fixe modifiées y sont réécrites), au lieu de la légende : figure 1, annexes « références, '
     'actualisation »; figure 3, chemin interdit « hors fonction locale P0-P1 (EXIG-ARC-01) » et mémoires placées '
     'selon le tableau 13 (travail en couche 3, épisodique et sémantique en couche 5); figure 5, EFVP « lorsque la '
     'loi l’exige », TLS 1.2 en plancher, OAuth 2.0 (RFC 9700); figure 6, OAuth 2.0 (RFC 9700) et bandeau « À '
     'surveiller ou à contenir »; figure 7, « un client par point d’accès », jeton « émis pour ce point d’accès de '
     'la passerelle », EMA au statut Évaluer; figure 9, couloirs « Personnes » et « Catalogue », jeton remis à la '
     'passerelle (flèche prolongée), étape 7 en SendStreamingMessage avec la référence d’approbation; figure 10, '
     'l’agent N reçoit 3/4 et republie 4/4, non traité; figure 11, modèle ou invite distincts, itération définie; '
     'figure 12, question « des domaines faiblement couplés réagissent-ils au même fait? », agent unique avant '
     'routage (cases échangées), feuilles « ou chaîne séquentielle » et « ou clavardage de groupe »; figure 14, '
     'DLP retirée de N1, hors bande en N2, retour arrière rapide en N3; figure 15, cellules P1 et P2 harmonisées, '
     'revue a posteriori, contrôles cumulés; figure 16, appel soumis à approbation, jeton remis à la passerelle '
     '(flèche raccourcie), champs agent, rôle et jti, rejeu avec la clé et la référence; figure 17, second jeton, '
     'deux audiences, extrait, JWT-SVID; figure 18, cnf, contrôle 5 en N2, débit dès l’étape 1, injection si '
     'prévue, intention avant le relais, filtre sans effet sur l’action; figure 19, approbation de l’action exacte, '
     '[B] élargi; figure 21, attente en deux événements reliés par un lien de span; figure 23, rangée « Étapes », '
     'enveloppe tenue par la passerelle de modèles, alerte au responsable technique; figure 26, contention sans '
     'destruction, gel étendu, préservation et avis en parallèle, sagas compensées et réparation métier, étages '
     'd’évaluation. Ces corrections remplacent les mentions « figure non modifiable » des modules 01 à 06 et la '
     'réserve du module des figures sur les écarts de structure (figures 9, 12, 14, 16 et 26).',
     ['01-18', '03-08', '04-25', '05-12', '05-13', '05-19', '06-02', '06-17', '06-32', '07-29', '08-01', '08-08',
      '08-09', '08-18', '09-23', '09-25', '11-06', '11-19', '11-20', '12-01', '12-02', '12-08', '4.06', '4.10',
      '4.11', '4.14', '4.36', '4.48', '4.55', '4.61', '4.62', '4.69', '5.09', '5.30', 'A-01', 'A-16', 'A-27',
      'A-34']),
    ('Légendes des figures 6, 9, 12, 14, 15, 16, 17, 18, 19 et 23; sections 7.3 et 8.4',
     'Mentions d’écart devenues fausses retirées après la correction des dessins (« le schéma simplifie », « le '
     'texte fait foi là où la figure diffère », « en cas d’écart »); section 8.4 : contrôles cumulés et approbation '
     'la plus stricte, comme l’EXIG-AUT-10 et la figure 15; figure 12 : l’encadré à combiner est en haut à droite.',
     ['09-23', '11-06', '11-19', '11-20', 'lissage']),
]
