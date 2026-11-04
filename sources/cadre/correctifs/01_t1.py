"""Correctifs de la revue du 3 novembre 2026 — tranche : Méthode et avertissements, sommaire exécutif, chapitres 1 à 5, sections 6.1 à 6.3."""
import re

NBSP = '\xa0'
FINE = ' '


def T(s):
    """Typographie du corps : apostrophe courbe, insécables devant « : », « % », « » » et après « « »."""
    s = s.replace("'", '’')
    s = s.replace(' :', NBSP + ':').replace(' %', NBSP + '%')
    s = s.replace('« ', '«' + NBSP).replace(' »', NBSP + '»')
    return s


_C = [
    # ---------------------------------------------------------------- Méthode et avertissements
    # [1.11, A-31] trois populations, total de l'annexe G, règle des catégories
    ("""Cette version consolide quatre documents de travail. Chacune des 121 références de la recherche documentaire a été ouverte""",
     """Cette version consolide quatre documents de travail. La vérification a porté sur trois populations de références, qui ne se recouvrent qu'en partie. Chacune des 121 références de la recherche documentaire a été ouverte""",
     ['1.11', 'A-31']),
    ("""et publications officielles des éditeurs. Seules des sources de catégorie A (primaires ou officielles) ou B (secondaires reconnues) sont citées. Le bilan détaillé""",
     """et publications officielles des éditeurs. L'audit final du 28 octobre 2026 a ensuite rouvert chacune des 428 références alors citées et examiné 1""" + FINE + """409 affirmations; 49 sources ont été ajoutées au registre pendant les corrections. L'annexe G compte 473 entrées, doublons compris, chaque doublon étant signalé dans son entrée; l'écart entre ce total et la somme des deux dernières populations n'est pas réconcilié dans la présente version. Le registre des affirmations examinées n'est pas joint au cadre : une vérification se retrace par la référence citée et par l'annexe F, non affirmation par affirmation. Seules des sources de catégorie A (primaires ou officielles) ou B (secondaires reconnues) appuient une exigence, une obligation légale ou un fait; un argument d'éditeur est rapporté comme tel. Le bilan détaillé""",
     ['1.11', 'A-31']),
    # [1.69, 1.89, A-31, A-23] état des sources, catalogue des protocoles
    ("""Les versions, dates et chiffres reflètent l'état des sources au 27 octobre 2026; les versions applicables sont fixées au catalogue d'entreprise, révisé chaque trimestre.""",
     """Les versions, dates et chiffres reflètent l'état des sources au 27 octobre 2026; vérifications des 27 et 28 octobre 2026 (section 1.7). Les versions de référence des protocoles sont épinglées au catalogue des protocoles, révisé chaque trimestre (section 1.6).""",
     ['1.69', '1.89', 'A-31', 'A-23']),
    # ---------------------------------------------------------------- Sommaire exécutif
    ("""énoncent des exigences identifiées, vérifiables en revue d'architecture ou en test.</p>""",
     """énoncent des exigences identifiées, vérifiables en revue d'architecture ou en test ou, à défaut, par une justification consignée (section 1.4).</p>""",
     ['1.66']),
    ("""<p>des organisations estiment avoir la bonne gouvernance de leurs agents (Gartner, avril 2026)</p>""",
     """<p>des organisations estiment avoir la bonne gouvernance de leurs agents (Gartner, avril 2026; population et méthode non publiées)<strong><sup>[2]</sup></strong></p>""",
     ['1.71']),
    ("""contre moins de 15 en 2025 (prévision Gartner, avril 2026)</p>""",
     """contre moins de 15 en 2025 (prévision Gartner, avril 2026, sans méthode publiée : ordre de grandeur prospectif)<strong><sup>[2]</sup></strong></p>""",
     ['1.70']),
    # décision 1 [1.04, 1.69, 1.12, A-09, A-23]
    ("""Les API existantes sont exposées par adaptateurs, jamais réécrites. Les versions applicables sont fixées au catalogue, révisé chaque trimestre (chapitre 6).</li>""",
     """Les API existantes sont exposées par adaptateurs, sans réécriture de leur logique métier; l'ajout minimal qui rend une écriture idempotente reste permis (EXIG-ARC-14). Les versions de référence sont épinglées au catalogue des protocoles, révisé chaque trimestre; celles que cite le texte en sont les valeurs initiales (section 1.6, chapitre 6).</li>""",
     ['1.04', '1.69', '1.12', 'A-09', 'A-23']),
    # décision 2 [1.01, 1.03, 1.19, 1.69, A-01, A-02, A-26]
    ("""<li><strong>Rien ne contourne la passerelle ni le catalogue.</strong> En environnement serveur, tout appel d'un agent vers un outil MCP ou vers une donnée ou un agent d'un autre domaine traverse la passerelle d'agents, qui authentifie, autorise, applique les garde-fous, limite les coûts, injecte les secrets et journalise. Un outil absent du catalogue est injoignable (chapitre 5, chapitre 9).</li>""",
     """<li><strong>Rien ne contourne les points d'application.</strong> Hors d'un poste de développement individuel, tout appel d'un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 traversent la passerelle d'agents, qui authentifie, autorise, applique les garde-fous, limite les coûts, injecte les secrets et journalise; l'inférence passe par la passerelle de modèles et les événements par le courtier (EXIG-EVT-11). Un outil absent du catalogue d'entreprise est injoignable. C'est l'état cible : les agents déjà en service à l'adoption y sont ramenés selon le régime transitoire de l'EXIG-GOV-21 (chapitre 5, chapitre 9).</li>""",
     ['1.01', '1.03', '1.19', '1.69', 'A-01', 'A-02', 'A-26']),
    # décision 4 [1.28, 1.16, A-12, A-14, A-27]
    ("""Les niveaux N0 à N4 plafonnent ce qu'un agent peut faire seul selon la classe de risque; l'autonomie non bornée (NX) est interdite. Les outils sont classés P0 à P3 au catalogue; la règle la plus stricte l'emporte, et toute action critique, externe ou irréversible (P3) exige une approbation humaine signée et liée à l'action exacte (chapitre 8).</li>""",
     """Le niveau d'autonomie (N1 à N4; N0 qualifie un flux sans choix laissé au modèle) borne ce qu'un agent peut faire seul, et la classe de risque plafonne ce niveau (EXIG-CON-02); l'autonomie non bornée (NX) est interdite. Les outils sont classés P0 à P3 au catalogue; le contrôle appliqué à un appel réunit tous ceux qu'exigent ces axes (EXIG-AUT-10), et toute action critique, externe ou irréversible (P3) exige une approbation humaine hors bande, signée et liée à l'action exacte (chapitre 8).</li>""",
     ['1.28', '1.16', 'A-12', 'A-14', 'A-27']),
    # décision 5 [1.03, A-26]
    ("""des droits délégués et de courte durée.</strong> Aucun compte partagé ni clé statique;""",
     """des droits délégués et de courte durée.</strong> Aucun compte partagé ni clé statique (état cible; agents existants : EXIG-GOV-21);""",
     ['1.03', 'A-26']),
    # décision 6 [1.08, A-17]
    ("""Tout contenu reçu est une donnée, jamais une instruction. Dès qu'un agent a lu du contenu non fiable, ses capacités d'envoi vers l'extérieur lui sont retirées de façon déterministe;""",
     """Tout contenu reçu est une donnée, jamais une instruction. Dès qu'une session (la tâche racine et tout ce qui en dérive, section 3.1) a consommé un contenu non fiable, la passerelle lui retire de façon déterministe, pour le reste de la session, les outils d'envoi vers l'extérieur et les outils P3, sauf approbation liée à l'action; le marquage suit la donnée d'un agent à l'autre (EXIG-SEC-04, EXIG-SEC-06);""",
     ['1.08', 'A-17']),
    # décision 7 [1.50, A-05, A-06]
    ("""un coupe-circuit global est testé chaque trimestre (chapitre 7).</li>""",
     """un coupe-circuit global est éprouvé à l'exercice trimestriel de l'EXIG-SEC-26, et une saga interrompue reste compensable par un canal distinct (EXIG-ORC-31) (chapitres 7 et 9).</li>""",
     ['1.50', 'A-05', 'A-06']),
    # décision 8 [1.96, 1.97, A-19, A-27]
    ("""journal d'audit inaltérable, évaluation en trois paliers,""",
     """journal d'audit chaîné et ancré hors du domaine d'administration du service d'audit, évaluation en trois étages (E1 à E3),""",
     ['1.96', '1.97', 'A-19', 'A-27']),
    # décision 9 [1.97, A-27]
    ("""cycle de vie à points de contrôle,""", """cycle de vie à jalons,""", ['1.97', 'A-27']),
    # Par où commencer [1.91, A-26]
    ("""La mise en œuvre suit quatre phases séparées par trois jalons, vise le niveau 3 de maturité, « Défini », en 18 mois, puis""",
     """La mise en œuvre suit quatre phases ouvertes par trois jalons de passage, plus trois jalons de suivi (J2a, J4 et J5), vise le niveau 3 de maturité, « Défini », en 18 mois environ (19 au calendrier du tableau 59, congés compris), puis""",
     ['1.91']),
    ("""Aucun agent ne passe en production sans franchir la grille d'homologation de l'annexe A.</p>""",
     """Aucun agent ne passe en production sans franchir la grille d'homologation de l'annexe A. La feuille de route ordonne la planification; l'exigibilité se règle agent par agent, selon les paliers, les niveaux et les topologies qu'il exerce (EXIG-GOV-21).</p>""",
     ['1.03', 'A-26']),
    # ---------------------------------------------------------------- Chapitre 1
    # tableau 1 [1.68, 1.02, A-03]
    ("""et aux progiciels, dès que l'entreprise ou une équipe métier les active</td>""",
     """et aux progiciels, dès qu'ils peuvent agir sur des systèmes ou des données de l'entreprise, qu'ils aient été activés par l'éditeur, par une équipe ou par un employé (EXIG-ARC-26)</td>""",
     ['1.68', '1.02', 'A-03']),
    # [1.04, A-09]
    ("""<td>Systèmes d'enregistrement eux-mêmes, que le cadre n'oblige pas à modifier</td>""",
     """<td>Systèmes d'enregistrement eux-mêmes, dont le cadre n'impose pas la réécriture (un ajout minimal pour l'idempotence ou la trace reste permis, EXIG-ARC-14)</td>""",
     ['1.04', 'A-09']),
    # [1.16, A-27]
    ("""<td>Usage des modèles par les agents; flux déterministe qui appelle un agent ou qui est appelé par lui</td>""",
     """<td>Usage des modèles par les agents; flux de travail assisté par IA (section 3.2); flux déterministe qui appelle un agent ou qui est appelé par lui, soumis aux contrôles de cet agent</td>""",
     ['1.16', 'A-27']),
    # § 1.2 [1.67, 1.99]
    ("""Un assistant qui reçoit un premier outil, même en lecture seule, entre dans la portée dès ce moment. À l'inverse, une fonction qu'un éditeur qualifie d'agentique n'y entre que si elle appelle des outils ou agit : Gartner observait d'ailleurs, en juin 2025, que de nombreux produits existants étaient simplement rebaptisés « agentiques »<strong><sup>[3]</sup></strong>.""",
     """Un assistant qui reçoit un premier outil, même en lecture seule, ou un premier accès à une ressource ou à des données de l'entreprise (un index documentaire, par exemple), entre dans la portée dès ce moment. À l'inverse, une fonction qu'un éditeur qualifie d'agentique n'y entre que si elle appelle des outils ou agit; l'étiquetage agentique abusif que relève Gartner est traité à la section 2.1<strong><sup>[3]</sup></strong>.""",
     ['1.67', '1.99']),
    # § 1.3 [1.28, A-24]
    ("""fixer le niveau d'autonomie sous le plafond de la classe (section 8.1)""",
     """fixer le niveau d'autonomie sous le plafond de la classe (EXIG-CON-02, section 12.1)""",
     ['1.28', 'A-24']),
    # tableau 3 [1.33, A-24]
    ("""sur délégation du comité), limitée dans le temps et assortie de mesures compensatoires (section 11.6). Certaines obligations n'admettent aucune dérogation (section 4.3 et EXIG-GOV-17).</td>""",
     """sur délégation du comité, pour 90 jours au plus et par une autre personne que celle qui a instruit la demande), limitée dans le temps et assortie de mesures compensatoires (section 11.6, EXIG-GOV-15). Les points de l'EXIG-GOV-17, seule liste qui fasse foi, n'admettent aucune dérogation.</td>""",
     ['1.33', 'A-24']),
    # § 1.4 [1.66]
    ("""un titre court, un énoncé vérifiable en revue d'architecture ou en test, et une justification introduite par""",
     """un titre court, un énoncé vérifiable en revue d'architecture ou en test (ou, à défaut, par une justification consignée), et une justification introduite par""",
     ['1.66']),
    # § 1.4 périmètre normatif [1.15, 1.03, A-23, A-25, A-26]
    ("""Seuls ces blocs d'exigences (chapitres 5 à 13), les principes directeurs PRIN-01 à PRIN-12 (chapitre 4) et les tableaux auxquels une exigence renvoie expressément créent une obligation normative; le reste du texte, les exemples et les figures sont informatifs.</p>""",
     """Créent une obligation normative :</p>
<ul>
<li>les blocs d'exigences (chapitres 5 à 13) et les principes directeurs PRIN-01 à PRIN-12 (chapitre 4);</li>
<li>les règles d'interprétation des sections 1.2 (critère de portée et règle du doute), 1.5, 1.6, 4.2 (devoir de l'architecte) et 4.3;</li>
<li>les définitions du tableau 7; pour les niveaux d'autonomie et les paliers d'outils, les tableaux 28 et 31 font foi, et la section 3.1 en donne un résumé;</li>
<li>les tableaux et les structures d'annexe auxquels une exigence renvoie expressément : l'annexe A par l'EXIG-GOV-11, le contenu (non la forme) de l'annexe B par l'EXIG-GOV-07, C.1 et C.2 par l'EXIG-ORC-22 et l'EXIG-MCP-20, C.6 par l'EXIG-AUT-12, C.8 par l'EXIG-OBS-12;</li>
<li>le tableau 58, pour les seules phases d'exigibilité de l'EXIG-GOV-21.</li>
</ul>
<p>Le reste du texte, y compris l'annexe H, les exemples et les figures, est informatif. Est une mise en production tout usage d'un agent avec des justificatifs de production ou des données réelles, pilote compris (EXIG-GOV-08).</p>""",
     ['1.15', '1.03', 'A-23', 'A-25', 'A-26']),
    # [1.82]
    ("""Exemple : Microsoft exige un plafond d'itérations pour la boucle producteur-vérificateur, sans en fixer la valeur""",
     """Exemple : le guide de Microsoft recommande un plafond d'itérations pour la boucle producteur-vérificateur (évaluateur-optimiseur au chapitre 7), sans en fixer la valeur""",
     ['1.82']),
    # § 1.5 [1.93, A-31, A-30]
    ("""Sept annexes, de A à G, fournissent les outils d'application, le glossaire et les références.</p>""",
     """Huit annexes, de A à H, fournissent les outils d'application, le glossaire et les références; l'annexe H, informative, consigne l'actualisation du 1<sup>er</sup>""" + NBSP + """novembre 2026.</p>""",
     ['1.93', 'A-31']),
    ("""marqué « retirée ». Le tableau 4""",
     """marqué « retirée »; une exigence devenue un renvoi garde son identifiant et son titre. Le tableau 4""",
     ['A-30']),
    # tableau 4 [1.95, A-30]
    ("""<td>Traçage et journal d'audit</td><td>Chapitre 10</td>""",
     """<td>Traçage et journal d'audit</td><td>Sections 10.1 à 10.3</td>""", ['1.95', 'A-30']),
    ("""<td>Évaluation continue</td><td>Chapitre 10</td>""",
     """<td>Évaluation continue</td><td>Section 10.4</td>""", ['1.95', 'A-30']),
    ("""<td>Économie de l'inférence et maîtrise des coûts</td><td>Chapitre 10</td>""",
     """<td>Économie de l'inférence et maîtrise des coûts</td><td>Sections 10.5 et 10.6</td>""", ['1.95', 'A-30']),
    # § 1.6 [1.13, 1.14, A-23]
    ("""lorsqu'une règle du cadre et celle d'une autre politique visent le même objet, la plus stricte s'applique, et toute contradiction est soumise au comité. Le droit applicable et les engagements contractuels priment toujours (section 4.3).</p>""",
     """lorsqu'une règle du cadre et celle d'une autre politique visent le même objet, les deux s'appliquent si elles sont cumulables; sinon, l'ordre de départage de la section 4.3 tranche et la contradiction est soumise au comité. Le droit applicable prime toujours; les engagements contractuels en vigueur à l'adoption du cadre priment pour une transition bornée et inscrite au registre, sauf sur les points de l'EXIG-GOV-17 (section 4.3).</p>""",
     ['1.13', '1.14', 'A-23']),
    # [1.36, A-22]
    ("""<li><strong>Le catalogue des protocoles et standards</strong> est révisé au moins chaque trimestre (section 6.3 et section 11.7); un correctif de sécurité peut justifier une révision extraordinaire.</li>""",
     """<li><strong>Le catalogue des protocoles et standards</strong> est révisé au moins chaque trimestre par l'architecture d'entreprise, qui soumet les changements de statut à l'approbation du comité (EXIG-GOV-18, sections 6.3 et 11.7); la publication d'une version incompatible ou d'une dépréciation d'un standard adopté, ou un correctif de sécurité, déclenche une révision extraordinaire.</li>""",
     ['1.36', 'A-22']),
    # [1.12, A-23]
    ("""<li><strong>Les versions applicables</strong>, comme MCP 2026-07-28 ou A2A 1.0, sont fixées au catalogue et non dans le texte : en cas d'écart, le catalogue fait foi.</li>""",
     """<li><strong>Les versions applicables</strong>, comme MCP 2026-07-28 ou A2A 1.0, sont épinglées au catalogue des protocoles. Là où une exigence renvoie à « la version épinglée au catalogue », le catalogue fait foi, et la version citée dans le texte en est la valeur initiale; une échéance datée par une exigence (la migration MCP de l'EXIG-MCP-22, par exemple) reste dans le texte et ne change que par une révision du cadre.</li>""",
     ['1.12', 'A-23']),
    # [1.03, A-26]
    ("""La mise en conformité des agents déjà en service suit les phases et les jalons du chapitre 15.</p>""",
     """La mise en conformité des agents déjà en service suit le régime transitoire de l'EXIG-GOV-21; les phases et les jalons du chapitre 15 en ordonnent la planification.</p>""",
     ['1.03', 'A-26']),
    # § 1.7 [1.11, 1.89, A-31]
    ("""<li>un audit final de cohérence interne, factuelle et juridique de l'ensemble des chapitres et des références citées.</li>""",
     """<li>un audit final de cohérence interne, factuelle et juridique de l'ensemble des chapitres, le 28 octobre 2026, qui a rouvert les 428 références alors citées et examiné 1""" + FINE + """409 affirmations; 49 sources ont été ajoutées pendant les corrections, et l'annexe G compte 473 entrées, doublons compris (annexe F.1).</li>""",
     ['1.11', 'A-31']),
    ("""Seules les catégories A et B sont citées.""",
     """Une source de catégorie C n'appuie jamais une exigence, une obligation légale ni un fait; un argument d'éditeur peut seulement être rapporté comme tel.""",
     ['1.65', 'A-31']),
    ("""Elle reflète l'état des textes aux 27 et 28 octobre 2026,""",
     """Elle reflète l'état des sources au 27 octobre 2026, vérifié les 27 et 28 octobre 2026,""",
     ['1.89', 'A-31']),
    # ---------------------------------------------------------------- Chapitre 2
    # [1.77, 1.74]
    ("""En décembre 2025, le Model Context Protocol (MCP) comptait""",
     """En décembre 2025, selon le projet, le Model Context Protocol (MCP) comptait""", ['1.77', '1.74']),
    ("""En avril 2026, le protocole Agent2Agent (A2A) réunissait""",
     """En avril 2026, selon la Linux Foundation, le protocole Agent2Agent (A2A) réunissait""", ['1.74']),
    # [1.76, 1.74]
    ("""Côté dépenses, Menlo Ventures estime""",
     """Côté dépenses, Menlo Ventures, investisseur du secteur, estime""", ['1.74', '1.76']),
    (""" (estimation hors inférence)<strong><sup>[16]</sup></strong>""",
     """<strong><sup>[16]</sup></strong>""", ['1.76']),
    # [1.75]
    ("""La pression financière est déjà visible. Selon le rapport State of FinOps 2026 (1""" + FINE + """192 répondants),""",
     """La gestion des dépenses d'IA entre déjà dans la pratique FinOps. Selon le rapport State of FinOps 2026 (1""" + FINE + """192 répondants; l'échantillon change d'une édition à l'autre, si bien que la série n'est qu'indicative),""",
     ['1.75']),
    # [1.72]
    ("""selon Anthropic, un agent consomme environ 4 fois plus de jetons""",
     """selon les mesures d'Anthropic sur son système de recherche multiagent, un agent consomme environ 4 fois plus de jetons""",
     ['1.72']),
    # [1.73]
    ("""Selon IBM et le Ponemon Institute (juillet 2025), 13 % des organisations ont déclaré une violation""",
     """Selon IBM et le Ponemon Institute (juillet 2025), parmi les organisations étudiées, qui ont toutes subi une violation, 13 % ont déclaré une violation""",
     ['1.73']),
    ("""et une organisation sur cinq a subi une violation""",
     """et une organisation étudiée sur cinq a subi une violation""", ['1.73']),
    # [1.74]
    ("""<p>Les chiffres de Gartner sont des prévisions; ceux de McKinsey, de la FinOps Foundation, d'IBM et de Menlo Ventures proviennent d'enquêtes ou d'estimations; ceux de CyberArk, de Microsoft et d'Anthropic sont des données de fournisseurs.""",
     """<p>Les chiffres de Gartner sont des prévisions, et ses enquêtes ne publient ni leur population ni leur méthode; ceux de McKinsey et de la FinOps Foundation proviennent d'enquêtes; ceux d'IBM (étude menée par le Ponemon Institute pour IBM), de CyberArk, de Microsoft et d'Anthropic viennent de fournisseurs qui ont un intérêt dans le sujet; l'estimation de Menlo Ventures vient d'un investisseur du secteur; ceux de MCP et d'A2A sont déclarés par les projets eux-mêmes.""",
     ['1.74', '1.70']),
    # tableau 5 [1.11, 1.99]
    ("""Le tableau 5 retrace les jalons vérifiés qui fondent""",
     """Le tableau 5 retrace les jalons, vérifiés sauf mention contraire, qui fondent""", ['1.11']),
    ("""<td>Briques de découverte, d'identité et de messagerie, hors de l'Agentic AI Foundation (AAIF)</td>""",
     """<td>Briques de découverte, d'identité et de messagerie, toujours hors de l'Agentic AI Foundation (AAIF) au 27 octobre 2026</td>""",
     ['1.99']),
    (""" au stade « Growth » (approbation du conseil d'administration le 4 août)<strong><sup>[5, 35]</sup></strong>""",
     """ au stade « Growth »<strong><sup>[5, 35]</sup></strong>""", ['1.11']),
    # § 2.2 [1.83, A-22]
    ("""sauf retrait accéléré exceptionnel d'au moins 90 jours<strong><sup>[34]</sup></strong>. Pour l'entreprise, le choix d'un protocole n'est plus un pari sur un éditeur.</p>""",
     """sauf retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée), avec un préavis d'au moins 90 jours<strong><sup>[34]</sup></strong>. Pour l'entreprise, le choix d'un protocole n'est plus un pari sur un seul éditeur; il reste une dépendance envers le calendrier de la fondation, que le catalogue des protocoles absorbe.</p>""",
     ['1.83', 'A-22']),
    # figure 2 et § 2.3 [1.83]
    ("""neuf contrats réutilisables, soumis à une politique unique.""",
     """neuf contrats réutilisables, soumis à un point d'application unique, les autorisations restant fixées par couple agent-outil.""",
     ['1.83']),
    ("""représentent 10""" + FINE + """000 intégrations potentielles, contre 250 contrats.""",
     """représentent au plus 10""" + FINE + """000 intégrations point à point, maximum théorique que la pratique n'atteint pas, contre 250 contrats.""",
     ['1.83']),
    # tableau 6 [1.96, A-19]
    ("""<td>Traçage de bout en bout et journal d'audit inaltérable (PRIN-06;""",
     """<td>Traçage de bout en bout et journal d'audit chaîné et ancré (PRIN-06;""", ['1.96', 'A-19']),
    # § 2.4 [1.02, A-03]
    ("""Le cadre place ce point de contrôle neutre au niveau du transport : passerelle d'agents, identité et registre (chapitre 5 et section 9.4).</p>""",
     """Le cadre place ce point de contrôle neutre au point d'entrée des interfaces de l'entreprise : passerelle d'agents, identité et registre (chapitre 5 et section 9.4). Il ne tient que si les systèmes de l'entreprise ne sont joignables que par la passerelle; un agent qui s'exécute chez l'éditeur d'un logiciel-service relève des contrôles compensatoires de l'EXIG-ARC-26.</p>""",
     ['1.02', 'A-03']),
    ("""(section 13.3 et section 13.1)""", """(sections 13.1 et 13.3)""", ['1.99']),
    # [1.84, 1.85]
    ("""La Loi 25 (L.Q. 2021, c. 25) est en vigueur pour l'essentiel depuis le 22 septembre 2024, date de sa dernière étape majeure, le droit à la portabilité. Depuis le 22 septembre 2023, elle exige, dans les cas prévus,""",
     """La Loi 25 (L.Q. 2021, c. 25) est en vigueur pour l'essentiel depuis le 22 septembre 2023, et entièrement depuis le 22 septembre 2024, date de sa dernière étape, le droit à la portabilité. Depuis le 22 septembre 2023, elle exige notamment, dans les cas prévus,""",
     ['1.84']),
    ("""et le règlement (UE) 2026/1744 fixe au 2 décembre 2027 l'application aux systèmes à haut risque de l'annexe III<strong><sup>[57, 58]</sup></strong>.""",
     """et, selon le calendrier que publie la Commission européenne, le règlement modificatif (UE) 2026/1744 porte au 2 décembre 2027 l'application aux systèmes à haut risque de l'annexe III, date à confirmer par la relecture de ce règlement au Journal officiel (annexe H)<strong><sup>[57, 58]</sup></strong>.""",
     ['1.85']),
    # ---------------------------------------------------------------- Chapitre 3
    ("""<p>Les définitions du tableau 7 font foi dans tout le cadre et dans les documents qui s'y rattachent.""",
     """<p>Les définitions du tableau 7 font foi dans tout le cadre et dans les documents qui s'y rattachent (section 1.4); pour les niveaux d'autonomie et les paliers d'outils, les tableaux 28 et 31 font foi, et les échelles ci-dessous en sont un résumé.""",
     ['1.15', 'A-23']),
    ("""<td>Selon ISO/IEC 22989, entité automatisée qui perçoit""",
     """<td>D'après ISO/IEC 22989 (paraphrase vérifiée par la fiche de catalogue et des sources secondaires, non au texte de la norme, section 1.7), entité automatisée qui perçoit""",
     ['1.79']),
    ("""classée P0 à P3 au catalogue; un outil ne prend aucune décision. Dans MCP""",
     """classée P0 à P3 au catalogue. Un outil ne choisit pas lui-même, au moyen d'un modèle, les actions qu'il exécute, même s'il conserve l'état d'une tâche ou demande une précision (Tasks, élicitation MCP); une cible qui les choisit est un agent (section 6.2). Dans MCP""",
     ['1.22', 'A-20']),
    ("""c'est un flux de travail assisté par IA : le chemin reste fixé par le code.</td>""",
     """c'est un flux de travail assisté par IA : le chemin reste fixé par le code, et le flux est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle (section 3.2).</td>""",
     ['1.16', 'A-27']),
    ("""<td>Personne, application ou agent au nom duquel une tâche est exécutée. Ses droits bornent ceux de l'agent, et son identité accompagne chaque appel de bout en bout.</td>""",
     """<td>Personne ou application au nom de laquelle une tâche est exécutée ou, en l'absence de mandant humain, agent initiateur de la chaîne. Le mandant d'une chaîne de délégation est toujours l'entité d'origine; un agent intermédiaire n'y apparaît que comme acteur (<code>act</code>). Les droits du mandant bornent ceux de l'agent, et son identité accompagne chaque appel de bout en bout.</td>""",
     ['1.26', 'A-16']),
    ("""Par extension, envoi d'une tâche à un autre agent, sans plus de droits que n'en a le mandant.</td>""",
     """Par extension, envoi d'une tâche à un autre agent, avec des droits effectifs au plus égaux à l'intersection des droits du mandant, de la portée de l'agent au registre et de la portée nécessaire à la tâche, sans élargissement d'un saut à l'autre (EXIG-IAM-10).</td>""",
     ['1.26', 'A-16']),
    ("""sans approbation humaine : N0 à N4, NX étant interdit (définitions ci-dessous).</td>""",
     """sans approbation humaine : N1 à N4, NX étant interdit; N0 qualifie un flux, non un agent (définitions ci-dessous).</td>""",
     ['1.16', 'A-27']),
    # [A-17, A-01, 1.19] nouvelles définitions
    ("""<td>Temporal; LangGraph<strong><sup>[80, 81, 82]</sup></strong></td></tr></tbody></table>""",
     """<td>Temporal; LangGraph<strong><sup>[80, 81, 82]</sup></strong></td></tr><tr><td><strong>Session</strong></td><td>Au sens des EXIG-SEC-04 et EXIG-SEC-06 : la tâche racine et tout ce qui en dérive (sous-tâches, délégations A2A, reprises depuis un point de contrôle, événements publiés au titre de la tâche). Son état (contenu non fiable consommé, données sensibles consultées) est tenu par la passerelle dans un magasin à cohérence forte; un état illisible impose le refus. Un contexte vierge exclut tout rechargement de mémoire, de point de contrôle ou d'artefact étiqueté après la contamination.</td><td>Cadre (section 9.6)</td></tr><tr><td><strong>Environnement serveur</strong></td><td>Tout environnement d'exécution autre qu'un poste de développement individuel sans justificatif de production : développement partagé, préproduction et production, mais aussi poste de travail, navigateur, mobile ou périphérie dès qu'un agent y agit sur des systèmes ou des données de l'entreprise.</td><td>Cadre (EXIG-ARC-01)</td></tr></tbody></table>""",
     ['A-17', 'A-01', '1.19']),
    # échelles [1.16, 1.17, 1.18, 1.29, A-27]
    ("""<li><strong>N0 Automatisation déterministe</strong> : aucun modèle; flux codé, règles, RPA, API (repère de base hors portée agentique, section 1.2).</li>""",
     """<li><strong>N0 Automatisation déterministe</strong> : aucun choix d'action laissé à un modèle; le code fixe chaque pas (flux codé, règles, RPA, API), et un modèle peut y transformer une donnée sans choisir l'action. N0 qualifie un flux, non un agent : repère de base hors portée agentique, il entre dans la portée dès qu'il appelle un agent ou qu'un agent l'appelle, et suit alors les contrôles de cet agent (section 1.2).</li>""",
     ['1.16', 'A-27']),
    ("""<li><strong>N3 Autonomie bornée et supervisée</strong> : l'agent exécute seul les actions P2 réversibles ou compensables sous des seuils déclarés, dans un domaine de conception opérationnel documenté (ODD, <em>operational design domain</em>); il escalade les exceptions; une action P3 exige une approbation hors bande (humain sur la boucle).</li>""",
     """<li><strong>N3 Autonomie bornée et supervisée</strong> : sur une tâche demandée par une personne, l'agent exécute seul les actions P2 sous des seuils déclarés, dans un domaine de conception opérationnel documenté (ODD, <em>operational design domain</em>); il escalade les exceptions à une personne désignée, qui les traite dans un délai borné déclaré à la fiche; une action P3 exige une approbation hors bande, une à une (humain sur la boucle, et dans la boucle pour les actions P3).</li>""",
     ['1.17', '1.18', '1.29', 'A-27']),
    ("""<li><strong>N4 Autonomie étendue sous ODD certifié</strong> : l'agent s'autodéclenche sur des événements et opère en continu; l'humain est hors de la boucle d'exécution, mais sur la boucle de gouvernance; une action P3 est toujours approuvée; ce niveau exige une décision du comité.</li>""",
     """<li><strong>N4 Autonomie étendue sous ODD certifié</strong> : l'agent exécute seul des tâches déclenchées sans demande d'une personne (événement, horaire), dans un ODD certifié; la passerelle lit l'origine de la tâche, attribut posé par l'orchestrateur ou par le courtier, et refuse une tâche autodéclenchée à un agent qui n'est pas N4; l'humain est hors de la boucle d'exécution, mais sur la boucle de gouvernance; une action P3 est toujours approuvée hors bande, une à une; ce niveau n'est permis qu'à un agent de classe faible, sur décision du comité (EXIG-CON-02).</li>""",
     ['1.17', '1.29', 'A-27']),
    ("""<strong>P0</strong> lecture publique; <strong>P1</strong> lecture interne ou sensible; <strong>P2</strong> écriture réversible; <strong>P3</strong> action critique, externe ou irréversible, jamais exécutée seule par un agent.</p>""",
     """<strong>P0</strong> lecture publique (un outil de recherche publique dont la requête est en texte libre reste un outil d'envoi au sens de l'EXIG-SEC-06); <strong>P1</strong> lecture interne ou sensible; <strong>P2</strong> écriture réversible, ou compensable vers un état métier équivalent, à impact borné; <strong>P3</strong> action critique, externe ou irréversible, même si une compensation est déclarée, jamais exécutée seule par un agent (tableau 31, EXIG-AUT-08).</p>""",
     ['1.18', 'A-27', 'A-17']),
    ("""Pour une action, le contrôle le plus strict l'emporte (section 8.4).</p>""",
     """Pour un appel, le contrôle appliqué est l'union des contrôles qu'exigent ces axes, calculée par la passerelle selon l'EXIG-AUT-10 (section 8.4).</p>""",
     ['A-14']),
    # § 3.2 [1.81, 1.16, A-27]
    ("""(ALFWorld, WebShop) dans les essais de ses auteurs""",
     """(ALFWorld, WebShop) dans les essais de ses auteurs, au prix d'une exactitude parfois moindre sur les questions à plusieurs étapes (HotpotQA)""",
     ['1.81']),
    ("""réglementé ou audité. C'est le patron par défaut du cadre.</li>""",
     """réglementé ou audité. C'est le patron par défaut du cadre; il est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle (sans approbation : N3 et ODD).</li>""",
     ['1.16', 'A-27']),
    # § 3.3 [1.30, 1.17, A-27]
    ("""<td>Dans la session; une action P3 reste approuvée hors bande (section 8.5)</td>""",
     """<td>Dans la session, par un jeton d'approbation signé émis hors de l'interface de l'agent (EXIG-AUT-12, EXIG-AUT-13); une action P3 est approuvée hors bande (section 8.5)</td>""",
     ['1.30']),
    ("""Un agent ambiant peut se borner à signaler (N1), préparer des actions soumises à approbation (N2) ou agir seul sous seuils (N3); seul le niveau N4 combine le déclenchement sur événements, l'exécution continue et l'absence de la personne dans la boucle d'exécution.""",
     """Un agent ambiant peut se borner à signaler (N1) ou préparer des actions soumises à approbation (N2). Dès qu'il exécute seul des écritures sur des tâches déclenchées sans demande d'une personne, il relève du niveau N4 : c'est l'origine de la tâche, lue par la passerelle, qui distingue N4 de N3 (section 3.1).""",
     ['1.17', 'A-27']),
    # § 3.4 [1.32, 1.86]
    ("""et chaque instance la sienne au besoin<strong><sup>[92]</sup></strong>.""",
     """et chaque instance la sienne dès que des instances servent des mandants différents ou doivent pouvoir être révoquées séparément<strong><sup>[92]</sup></strong>.""",
     ['1.32']),
    ("""le RIA oblige le déployeur d'un système à haut risque à confier la supervision humaine à des personnes compétentes, formées et dotées de l'autorité nécessaire<strong><sup>[94]</sup></strong>;""",
     """l'art. 26, par. 2, du RIA oblige le déployeur d'un système à haut risque, à compter de la date d'application à ces systèmes (section 12.4), à confier la supervision humaine à des personnes physiques compétentes, formées et dotées de l'autorité nécessaire<strong><sup>[61, 94]</sup></strong>;""",
     ['1.86']),
    # ---------------------------------------------------------------- Chapitre 4
    ("""(PRIN-03 à PRIN-06, PRIN-10 et PRIN-12). Qui a autorisé""",
     """(PRIN-03 à PRIN-06, PRIN-10 et PRIN-12; PRIN-07, qui porte sur ce que l'agent lit, relève d'une autre question). Qui a autorisé""",
     ['1.98']),
    # PRIN-03 [1.26, A-16]
    ("""Ses droits sont minimaux, de courte durée et jamais supérieurs à ceux de son mandant.""",
     """Ses droits effectifs sont minimaux, de courte durée et au plus égaux à l'intersection des droits de son mandant, de sa portée au registre et de la portée nécessaire à la tâche.""",
     ['1.26', 'A-16']),
    ("""<p>Conséquences : les droits effectifs d'un agent délégué ne dépassent jamais l'intersection des droits du mandant et de ceux de l'agent<strong><sup>[96]</sup></strong>; le serveur d'autorisation l'applique à chaque échange de jetons (section 9.3).</p>""",
     """<p>Conséquences : les droits effectifs d'un agent délégué ne dépassent jamais l'intersection des droits du mandant, de la portée de l'agent au registre et de la portée nécessaire à la tâche<strong><sup>[96]</sup></strong>, et ne s'élargissent jamais d'un saut à l'autre. Le serveur d'autorisation borne les portées à chaque échange de jetons; le serveur de ressources applique, à chaque appel, les droits du mandant sur les données (EXIG-IAM-10, section 9.3). Le mandant d'une chaîne reste l'entité d'origine; un agent intermédiaire n'y apparaît que comme acteur.</p>""",
     ['1.26', 'A-16']),
    # PRIN-04 [1.28, A-24, A-27]
    ("""Le niveau d'autonomie, de N0 à N4, est un plafond déclaré au registre et fixé par la classe de risque de l'agent.""",
     """Le niveau d'autonomie d'un agent, de N1 à N4, est un plafond déclaré au registre, au plus bas niveau suffisant, sous le plafond que fixe la classe de risque de l'agent (EXIG-CON-02).""",
     ['1.28', 'A-27']),
    ("""fixé par EXIG-CON-02 (section 8.1, section 12.1).""",
     """fixé par l'EXIG-CON-02, seule source de ce plafond (section 12.1).""", ['1.28', 'A-24']),
    # PRIN-06 [1.96, A-19]
    ("""journal d'audit inaltérable et distinct des traces, en accord avec l'OWASP, qui recommande des journaux immuables et signés des actions d'agents<strong><sup>[28]</sup></strong>;""",
     """journal d'audit chaîné, ancré hors du domaine d'administration du service d'audit et distinct des traces (choix du cadre, section 10.3);""",
     ['1.96', 'A-19']),
    # PRIN-07 [1.08, A-17]
    ("""<p>Conséquences : les contrôles décisifs sont déterministes, par exemple le retrait des outils d'envoi externe après la lecture de contenu non fiable. La détection""",
     """<p>Conséquences : les contrôles sur lesquels repose la défense sont déterministes et suivent le flux d'information, non un agent isolé : un contenu non fiable marque la session (section 3.1), le marquage se propage avec la donnée d'un agent à l'autre, et la passerelle retire alors les outils d'envoi vers l'extérieur et les outils P3 (EXIG-SEC-04, EXIG-SEC-06). La détection""",
     ['1.08', 'A-17']),
    # PRIN-09 [1.02, A-03]
    ("""il passe par la passerelle de modèles (section 5.2). Les contrats d'approvisionnement""",
     """il passe par la passerelle de modèles (section 5.2). Un agent intégré à un logiciel-service, dont l'entreprise ne contrôle pas l'exécution, relève des contrôles compensatoires de l'EXIG-ARC-26. Les contrats d'approvisionnement""",
     ['1.02', 'A-03']),
    # PRIN-10 [A-34]
    ("""sans propriétaire inscrit au registre, et ce propriétaire atteste""",
     """sans parrain inscrit au registre, et ce parrain atteste""", ['A-34']),
    # PRIN-12 [1.06, A-06, A-05]
    ("""En cas de doute, le système échoue en mode fermé : il s'arrête ou escalade plutôt que d'agir.</p>""",
     """En cas de doute, le système échoue en mode fermé vers l'avant : il refuse toute nouvelle action, s'arrête ou escalade, mais ne laisse jamais une saga à moitié exécutée faute de pouvoir compenser; les compensations déclarées passent par un canal distinct, qui reste ouvert (EXIG-ORC-31).</p>""",
     ['1.06', 'A-06']),
    ("""le coupe-circuit est testé chaque trimestre, fréquence choisie par le cadre (section 7.8).</p>""",
     """le coupe-circuit est éprouvé à l'exercice trimestriel de l'EXIG-SEC-26, fréquence choisie par le cadre (sections 7.8 et 9.9).</p>""",
     ['1.50', 'A-05']),
    # tableau 9 [1.98]
    ("""<td>PRIN-02 Contrat avant code</td><td>6.5, 6.6, 6.8, annexe C</td><td>EXIG-INT, EXIG-MCP, EXIG-A2A</td>""",
     """<td>PRIN-02 Contrat avant code</td><td>6.5 à 6.8, annexe C</td><td>EXIG-INT, EXIG-MCP, EXIG-A2A, EXIG-EVT</td>""",
     ['1.98']),
    ("""<td>PRIN-06 Traçabilité</td><td>10.1, 10.3, 10.6</td><td>EXIG-OBS, EXIG-FIN</td>""",
     """<td>PRIN-06 Traçabilité</td><td>10.1, 10.3, 10.4, 10.6</td><td>EXIG-OBS, EXIG-EVA, EXIG-FIN</td>""",
     ['1.98']),
    ("""<td>PRIN-12 Dégradation maîtrisée</td><td>7.8, 9.4, 12.8</td><td>EXIG-ORC, EXIG-IAM, EXIG-CON</td>""",
     """<td>PRIN-12 Dégradation maîtrisée</td><td>7.8, 9.4, 10.4, 12.8</td><td>EXIG-ORC, EXIG-IAM, EXIG-EVA, EXIG-CON</td>""",
     ['1.98']),
    # § 4.3 [1.13, 1.14, A-23]
    ("""<li>Le droit applicable et les engagements contractuels, qu'aucun principe ne peut écarter (chapitre 12).</li>""",
     """<li>Le droit applicable, qu'aucun principe ne peut écarter (chapitre 12), et les engagements contractuels en vigueur à l'adoption du cadre, pour une transition bornée et inscrite au registre, sauf sur les points de l'EXIG-GOV-17; un contrat conclu ou renouvelé après l'adoption ne peut comporter de clause contraire à ces points (EXIG-APP-18).</li>""",
     ['1.13', 'A-23']),
    ("""<p>À rang égal, on retient l'option la plus simple qui respecte les deux principes en présence, et l'arbitrage est consigné dans la décision d'architecture. Le tableau 10""",
     """<p>Le départage entre règles suit cet ordre : droit applicable; EXIG-GOV-17; DOIT sur DEVRAIT; source unique désignée sur renvoi; disposition spéciale sur disposition générale. À rang égal, deux contraintes cumulables s'appliquent toutes deux, et entre deux principes on retient l'option la plus simple qui les respecte l'un et l'autre; si aucune option ne les respecte, l'action est refusée jusqu'à la décision du comité, qui statue dans un délai fixé. L'arbitrage est consigné dans la décision d'architecture. Le tableau 10""",
     ['1.14', 'A-23']),
    # tableau 10 [1.01, A-01]
    ("""<td>PRIN-01 vise les échanges qui franchissent une frontière de domaine; à l'intérieur, une fonction locale suffit. Dès qu'un second consommateur apparaît, l'outil passe au catalogue.</td>""",
     """<td>Une fonction locale suffit si elle est de palier P0 ou P1, exécutée dans l'unité de déploiement de l'agent, sur les données de son propre domaine, et inscrite au catalogue avec son palier (EXIG-ARC-01). Un outil P2 ou P3 est toujours exposé comme outil MCP derrière la passerelle; dès qu'un second consommateur apparaît, l'outil passe aussi par MCP.</td>""",
     ['1.01', 'A-01']),
    # [1.88, A-18]
    ("""<td>La protection des RP l'emporte : les métadonnées sont toujours tracées; par choix du cadre, le contenu est exclu par défaut, activé sur décision documentée et conservé hors des traces (section 10.2).</td>""",
     """<td>La protection des RP l'emporte : les métadonnées sont toujours tracées, et le contenu est interdit dans la télémétrie de production (EXIG-OBS-07); une capture de diagnostic, décidée et documentée, détruite après 14 jours au plus, est conservée hors des traces (EXIG-OBS-08, section 10.2).</td>""",
     ['1.88', 'A-18']),
    # [1.80, 1.31]
    ("""CaMeL (Debenedetti et coll., mars 2025)""",
     """CaMeL (Debenedetti et coll., mars 2025; chiffres de la version 2 du 24 juin 2025)""", ['1.80']),
    ("""<td>La classe de risque tranche : pour la classe de risque élevé, on accepte la perte d'utilité. Si le risque""",
     """<td>La classe de risque tranche : en classe élevée, un patron de défense par conception est obligatoire et la perte d'utilité est acceptée (EXIG-SEC-07); en classe modérée, il est recommandé; en classe faible, le retrait de l'EXIG-SEC-06 suffit. Si le risque""",
     ['1.31']),
    # dérogations [1.34, 1.33]
    ("""<p>Un écart à un principe doit faire l'objet d'une dérogation écrite, approuvée par le comité d'architecture et des risques agentiques (ou, pour un agent de classe faible, par délégation à l'architecture d'entreprise, pour 90 jours au plus),""",
     """<p>Un écart à un principe ou à une exigence (identifiant PRIN-xx ou EXIG-xxx-nn) doit faire l'objet d'une dérogation écrite, approuvée par le comité d'architecture et des risques agentiques (ou, pour un agent de classe faible, par délégation à l'architecture d'entreprise, pour 90 jours au plus, par une autre personne que celle qui a instruit la demande),""",
     ['1.34', '1.33']),
    ("""sinon l'écart est corrigé ou l'agent passe à l'état « suspendu ».</p>""",
     """sinon l'écart est corrigé ou l'agent passe à l'état « suspendu ». À l'échéance d'une dérogation qui vise un composant, celui-ci est retiré du catalogue, et les agents qui en dépendent, nommés dans la demande, sont suspendus.</p>""",
     ['1.34']),
    # [1.33, A-24]
    ("""<p>Choix du cadre : aucune dérogation n'est admise pour l'autonomie non bornée (NX), pour l'exécution par un agent seul d'une action de palier P3, pour la mise en production d'un agent sans personne nommée qui en répond, pour l'usurpation, par un agent, de l'identité de son mandant, ni pour le dépassement du plafond d'autonomie de la classe de risque (EXIG-GOV-17). Une dérogation ne peut pas non plus écarter une obligation légale ou réglementaire.</p>""",
     """<p>Choix du cadre : l'EXIG-GOV-17 est la seule liste des points qui n'admettent aucune dérogation, et cet encadré n'en est qu'un rappel. Elle vise notamment l'autonomie non bornée (NX), l'exécution par un agent seul d'une action de palier P3, l'exploitation d'un agent sans fiche au registre ou sans parrain nommé, l'usurpation, par un agent, de l'identité de son mandant, le dépassement du plafond d'autonomie de la classe de risque et le manquement à une obligation légale ou réglementaire.</p>""",
     ['1.33', 'A-24']),
    # ---------------------------------------------------------------- Chapitre 5
    ("""Sa règle centrale est simple : aucun agent n'atteint un outil, une donnée ou un autre agent hors de son domaine sans passer par la passerelle d'agents et le catalogue d'entreprise.""",
     """Sa règle centrale est simple : hors d'un poste de développement individuel, tout appel d'un agent vers un serveur MCP ou un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 passent par la passerelle d'agents, vers un élément inscrit au catalogue d'entreprise (EXIG-ARC-01).""",
     ['1.01', 'A-01']),
    ("""qui la tient ensemble; figure 3 la résume.""", """qui la tient ensemble; la figure 3 la résume.""", ['1.99']),
    ("""et la passerelle d'agents ferme tout chemin qui contournerait le catalogue. Source : CRE-IA-2026-01.</figcaption>""",
     """et la passerelle d'agents ferme tout chemin qui contournerait le catalogue; sa portée exacte, tout appel MCP ou A2A quel que soit le domaine et toute action P2 ou P3, est celle de l'EXIG-ARC-01. Source : CRE-IA-2026-01.</figcaption>""",
     ['1.01', 'A-01']),
    # EXIG-ARC-01 [1.01, 1.19, 1.44, A-01]
    ("""<p>Dans tout environnement serveur, tout appel d'un agent vers un outil, une ressource ou une invite MCP, vers une donnée d'un autre domaine ou vers un autre agent <strong>DOIT</strong> transiter par la passerelle d'agents et viser un élément inscrit au catalogue d'entreprise à une version approuvée (seule exception : un serveur MCP local en transport <code>stdio</code> sur un poste de développement, encadré par l'EXIG-MCP-08; les appels internes à un même domaine applicatif sans serveur MCP ni pair A2A sont régis par l'EXIG-IAM-17). La passerelle <strong>DOIT</strong> refuser tout appel vers un élément absent du catalogue.</p>""",
     """<p>Dans tout environnement serveur, c'est-à-dire tout environnement autre qu'un poste de développement individuel sans justificatif de production (tableau 7), tout appel d'un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 <strong>DOIVENT</strong> passer par la passerelle d'agents et viser un élément inscrit au catalogue d'entreprise à une version et une empreinte approuvées. Une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Seule une fonction locale de palier P0 ou P1, exécutée dans l'unité de déploiement de l'agent, sur les données de son propre domaine et inscrite au catalogue avec son palier, peut s'en dispenser; l'accès direct à une ressource de son domaine reste soumis à la décision par appel du serveur de ressources (EXIG-IAM-17). Une instance de la passerelle <strong>PEUT</strong> être déployée au plus près de l'agent (<em>sidecar</em>), à condition de partager la politique, le registre des identifiants de jetons d'approbation (<code>jti</code>) et le journal d'audit des autres instances. Sur un poste de développement, un serveur MCP local en <code>stdio</code>, ou en Streamable HTTP sur la boucle locale, obéit à l'EXIG-MCP-08; les événements relèvent du courtier (EXIG-ARC-13). La passerelle <strong>DOIT</strong> refuser tout appel vers un élément absent du catalogue.</p>""",
     ['1.01', '1.19', '1.44', 'A-01', 'A-02']),
    ("""un seul chemin de contournement suffit à rendre ces contrôles illusoires.</p></div>""",
     """un seul chemin de contournement suffit à rendre ces contrôles illusoires. La fonction locale admise ne peut ni écrire ni agir à l'extérieur : toute vérification d'approbation reste ainsi à la passerelle.</p></div>""",
     ['1.01', 'A-01']),
    # EXIG-ARC-02 [1.37, A-34]
    ("""(jeton délégué, ou identité de l'agent autonome et de son propriétaire), le contexte de trace et les plafonds restants de la tâche (jetons, coût, appels d'outils, délai).""",
     """(jeton délégué, ou identité de l'agent autonome et de son parrain), le contexte de trace et la part restante de l'enveloppe de la tâche (EXIG-FIN-04 : jetons de modèle, coût, appels d'outils, délai).""",
     ['1.37', 'A-34']),
    ("""Chaque boîte de figure 3""", """Chaque boîte de la figure 3""", ['1.99']),
    # EXIG-ARC-04 [1.39, 1.40]
    ("""soit, pour un déclencheur système, l'identité du service et son propriétaire nommé. Il <strong>DOIT</strong> aussi ouvrir ou poursuivre une trace conforme à W3C Trace Context avant de transmettre la demande<strong><sup>[103]</sup></strong>.</p>""",
     """soit, pour un déclencheur système (planificateur, consommateur d'événements), l'identité du service et son propriétaire nommé, jamais un attribut porté par l'événement reçu (EXIG-EVT-07). Il <strong>DOIT</strong> aussi ouvrir une trace conforme à W3C Trace Context avant de transmettre la demande<strong><sup>[103]</sup></strong>; il ne poursuit une trace entrante que si elle vient d'une source de confiance, et la redémarre à une frontière de confiance (section 10.1).</p>""",
     ['1.39', '1.40']),
    # § 5.2 couche 2 [1.49, 1.05, A-09]
    ("""Temporal, par exemple, poursuit une exécution jusqu'à son terme sans limite de temps imposée et la reprend en rejouant son historique d'événements<strong><sup>[81]</sup></strong>. Les flux Standard d'AWS Step Functions durent jusqu'à un an avec une sémantique d'exécution exactement une fois, alors que""",
     """Temporal, par exemple, poursuit une exécution jusqu'à son terme sans limite de durée imposée et la reprend en rejouant son historique d'événements<strong><sup>[81]</sup></strong>. La documentation de Temporal borne toutefois cet historique (51""" + FINE + """200 événements ou 50""" + NBSP + """Mo), si bien qu'une longue exécution doit repartir sous un nouvel historique (<em>Continue-As-New</em>), et ses activités sont réessayées sans limite par défaut, d'où la borne qu'exige l'EXIG-ORC-27 pour une activité à effet. Les flux Standard d'AWS Step Functions durent jusqu'à un an et n'exécutent jamais une tâche plus d'une fois, sauf si une règle <code>Retry</code> est déclarée, alors que""",
     ['1.49', '1.05', 'A-09']),
    # EXIG-ARC-05 [1.36]
    ("""attend une approbation humaine ou s'étend sur plus d'un échange <strong>DOIT</strong>""",
     """attend une approbation humaine ou compte plus d'une étape (déclencheur commun avec l'EXIG-ORC-11) <strong>DOIT</strong>""",
     ['1.36']),
    # EXIG-ARC-06 [1.05, 1.36, A-09]
    ("""refuser de reprendre une exécution à partir d'un point de contrôle dont la provenance n'est pas vérifiée.</p>""",
     """refuser de reprendre une exécution à partir d'un point de contrôle dont la provenance n'est pas vérifiée, ou plus ancien que la durée de conservation des clés d'idempotence des outils à effet de la tâche (EXIG-ORC-21); les autres règles de protection des points de contrôle sont celles de l'EXIG-ORC-13.</p>""",
     ['1.05', '1.36', 'A-09']),
    # EXIG-ARC-07 [1.26]
    ("""reste soumis à l'autorisation de la passerelle selon le mandant et le palier de l'outil.</p>""",
     """reste soumis à l'autorisation de la passerelle selon les droits effectifs de la chaîne (PRIN-03) et le palier de l'outil, décidée à chaque appel (EXIG-IAM-02).</p>""",
     ['1.26']),
    # EXIG-ARC-08 [1.42, 1.02, A-03]
    ("""<p>Tout appel d'inférence <strong>DOIT</strong> passer par la passerelle de modèles de l'entreprise. Un agent <strong>DOIT</strong> n'accéder aux modèles que par cette passerelle, sans détenir de clé de fournisseur de modèles ni appeler un fournisseur directement.</p>""",
     """<p>Tout appel d'inférence fait par un agent dont l'entreprise contrôle l'exécution, ou pour son compte (plongements, juges d'évaluation et classifieurs de garde-fous compris), <strong>DOIT</strong> passer par la passerelle de modèles de l'entreprise; l'agent ne détient aucune clé de fournisseur de modèles et n'appelle jamais un fournisseur directement. Un agent intégré à un logiciel-service relève de l'EXIG-ARC-26.</p>""",
     ['1.42', '1.02', 'A-03']),
    # EXIG-ARC-09 [1.41, A-24]
    ("""de sorte qu'un changement de modèle ou de fournisseur s'effectue par configuration, suivi d'une réévaluation (section 10.4), sans modification du code de l'agent.</p>""",
     """de sorte qu'un changement de modèle ou de fournisseur s'effectue par configuration, sans modification du code de l'agent, et toujours après la réévaluation qu'exige l'EXIG-GOV-12. L'alias se résout vers un instantané daté du modèle, épinglé et inscrit au registre.</p>""",
     ['1.41', 'A-24']),
    # couche 4 [1.47]
    ("""la passerelle d'agents, mandataire inverse devant les serveurs MCP et les pairs A2A;""",
     """la passerelle d'agents, devant les serveurs MCP et les pairs A2A, mandataire inverse pour le trafic entrant et mandataire sortant pour le trafic qui quitte l'entreprise;""",
     ['1.47']),
    # EXIG-ARC-11 [A-01, A-03]
    ("""et devant tous les pairs A2A, pour le trafic interdomaine comme pour celui qui entre dans l'entreprise ou qui en sort, et réévaluer l'autorisation à chaque appel.""",
     """et devant tous les pairs A2A, pour le trafic intradomaine et interdomaine comme pour celui qui entre dans l'entreprise ou qui en sort, et réévaluer l'autorisation à chaque appel. Un agent intégré à un logiciel-service n'atteint les systèmes d'enregistrement de l'entreprise que par elle, comme client externe (EXIG-ARC-26).""",
     ['1.01', '1.02', 'A-01', 'A-03']),
    # EXIG-ARC-12 [1.07, A-04]
    ("""Aucune liste propre à un projet ne fait foi.</p>""",
     """Aucune liste propre à un projet ne fait foi. La passerelle <strong>DOIT</strong> aussi appliquer la liste de suspension (agents, outils, versions) reçue par le canal signé de l'EXIG-IAM-22, même quand le plan de contrôle est indisponible.</p>""",
     ['1.07', 'A-04']),
    ("""une source unique permet de retirer partout, en une seule opération, un outil compromis.</p></div>""",
     """une source unique permet de retirer partout, par une seule décision, un outil compromis, y compris pendant une panne du plan de contrôle.</p></div>""",
     ['1.07', 'A-04']),
    # EXIG-ARC-13 [1.09, 1.38, A-02]
    ("""et ses producteurs comme ses consommateurs <strong>DOIVENT</strong> s'authentifier auprès du bus.</p>""",
     """et ses producteurs comme ses consommateurs <strong>DOIVENT</strong> s'authentifier auprès du bus et être autorisés par sujet selon l'entrée de catalogue (EXIG-EVT-07). Le courtier et l'intercepteur de publication sont le point d'application des politiques pour les événements (EXIG-EVT-11) : une publication par une session marquée non fiable y subit le même retrait que les outils d'envoi (EXIG-SEC-06), et toute action P2 ou P3 qu'un consommateur exécute à la suite d'un événement passe par la passerelle d'agents (EXIG-ARC-01).</p>""",
     ['1.09', '1.38', 'A-02']),
    # EXIG-ARC-14 [1.04, A-09]
    ("""placés devant les API en place, sans réécriture des services d'origine.</p>""",
     """placés devant les API en place, sans réécriture de la logique métier des services d'origine. L'ajout minimal qui rend une écriture idempotente ou traçable (champ de clé d'idempotence, référence de trace, lecture par clé, écriture conditionnelle) est permis. Un adaptateur qui ne dispose ni d'un tel mécanisme du service, ni d'un registre de clés durable mis à jour dans la même transaction que l'effet ou complété par une requête d'état qui le constate, déclare l'outil non idempotent (EXIG-ORC-22).</p>""",
     ['1.04', 'A-09']),
    # EXIG-ARC-16 [1.26]
    ("""<p>Un outil <strong>DOIT</strong> filtrer ses résultats selon les droits du mandant, de sorte qu'aucun agent ne reçoive une donnée que le mandant ne pourrait pas consulter lui-même.</p>""",
     """<p>Un outil <strong>DOIT</strong> filtrer ses résultats selon les droits effectifs de la chaîne (PRIN-03), de sorte qu'aucun agent ne reçoive une donnée que le mandant ne pourrait pas consulter lui-même ou qui excède la portée de l'agent au registre.</p>""",
     ['1.26']),
    # § 5.3 [1.99, 1.96, 1.02]
    ("""consommés partout; tableau 11 indique""", """consommés partout; le tableau 11 indique""", ['1.99']),
    ("""S'y ajoutent le journal d'audit inaltérable, distinct des traces,""",
     """S'y ajoutent le journal d'audit chaîné et ancré, distinct des traces,""", ['1.96', 'A-19']),
    ("""D'où l'exigence d'un coupe-circuit appliqué à la passerelle, quel que soit l'éditeur de l'agent (section 9.4).</p>""",
     """D'où l'exigence d'un coupe-circuit appliqué à la passerelle à tout agent qui la traverse, quel que soit son éditeur (section 9.4); un agent qui s'exécute chez l'éditeur d'un logiciel-service est arrêté par le mécanisme propre de l'EXIG-ARC-26.</p>""",
     ['1.02', 'A-03']),
    # EXIG-ARC-19 [1.48]
    ("""être fournis par l'équipe plateforme et consommés""",
     """être fournis par l'équipe plateforme (section 11.1) et consommés""", ['1.48']),
    # EXIG-ARC-20 [1.35, 1.99]
    ("""<p>Toute solution agentique présentée à l'homologation <strong>DOIT</strong> documenter la correspondance entre les ABB de tableau 12 et les SBB qu'elle emploie. L'homologation <strong>DOIT</strong> être refusée tant qu'un ABB de tableau 12 nécessaire à la solution n'a pas de SBB désigné.</p>""",
     """<p>Toute solution agentique présentée à l'homologation <strong>DOIT</strong> documenter la correspondance entre les ABB du tableau 12 et les SBB qu'elle emploie. L'homologation <strong>DOIT</strong> être refusée tant qu'un ABB du tableau 12 nécessaire à la solution n'a pas de SBB désigné. Sont toujours nécessaires la passerelle d'agents (EXIG-ARC-01) et les services des plans transversaux (EXIG-ARC-19), ainsi que, selon la solution, le moteur d'exécution durable pour toute écriture ou approbation (EXIG-ARC-05), la passerelle de modèles pour toute inférence (EXIG-ARC-08) et le bac à sable pour tout code généré (EXIG-ARC-10); une solution ne peut déclarer non nécessaire un ABB qu'exige l'une de ces exigences.</p>""",
     ['1.35', '1.99']),
    # nouvelle EXIG-ARC-26 [1.02, 1.24, A-03]
    ("""<div id="pourquoi-292"><p>Pourquoi : le risque de verrouillage s'est déplacé des protocoles vers les plateformes et leurs extensions (section 13.1).</p></div>
</div>""",
     """<div id="pourquoi-292"><p>Pourquoi : le risque de verrouillage s'est déplacé des protocoles vers les plateformes et leurs extensions (section 13.1).</p></div>
</div>
<div id="exig-arc-26">
<p><strong><code>EXIG-ARC-26</code> · DOIT</strong></p>
<p><strong>Agents intégrés aux logiciels-services</strong></p>
<p>PRIN-09, l'EXIG-ARC-03 et l'EXIG-ARC-08 visent les agents dont l'entreprise contrôle l'exécution. Un agent intégré à un logiciel-service, qui s'exécute chez son éditeur, <strong>DOIT</strong> :</p>
<ul>
<li>être inscrit au registre avec sa classe, son niveau d'autonomie et les actions qu'il exécute dans le logiciel-service;</li>
<li>n'atteindre les systèmes d'enregistrement de l'entreprise que par la passerelle d'agents, comme client externe;</li>
<li>relever d'un contrat qui comporte les clauses des EXIG-APP-05, EXIG-APP-06, EXIG-APP-08 et EXIG-APP-13, dont un préavis opposable de changement de modèle;</li>
<li>disposer d'un mécanisme d'arrêt propre (fournisseur d'identité, retrait des consentements OAuth, CAEP), documenté à la fiche et éprouvé à l'exercice de l'EXIG-SEC-26;</li>
<li>n'employer que des schémas d'outils de tiers épinglés et approuvés au catalogue (EXIG-INT-02).</li>
</ul>
<p>Une action P3 exécutée dans le logiciel-service exige un mécanisme d'approbation du fournisseur jugé équivalent à l'EXIG-AUT-12 à l'homologation. À défaut, l'agent est plafonné à N2, et chaque action P3 est approuvée dans la console de l'éditeur, approbation consignée à la fiche. La quarantaine (EXIG-GOV-10) et la suspension d'un tel agent passent par son mécanisme d'arrêt propre, et non par la passerelle.</p>
<div id="pourquoi-arc-26"><p>Pourquoi : un agent qui infère et agit chez son éditeur ne peut ni passer par la passerelle de modèles ni être arrêté par la passerelle d'agents; sans régime propre, chaque plateforme du tableau 12 serait non conforme par construction, ou homologuée contre des DOIT. Les contrôles compensatoires portent donc sur ce que l'entreprise maîtrise : l'accès à ses systèmes, ses contrats et ses identités.</p></div>
</div>""",
     ['1.02', '1.24', 'A-03']),
    # § 5.4 [1.45]
    ("""le comité les révise chaque trimestre, avec le catalogue des protocoles (section 11.7).</p>""",
     """le comité les révise chaque trimestre, avec le catalogue des protocoles (section 11.7). Un SBB qui ne couvre pas toutes les capacités exigées de son ABB (par exemple une passerelle limitée aux outils MCP, ou un environnement d'exécution sans A2A ni OpenTelemetry documentés) n'est admis qu'avec un SBB complémentaire ou une dérogation (EXIG-ARC-21); à défaut, l'homologation est refusée (EXIG-ARC-20).</p>""",
     ['1.45']),
    # tableau 12 [1.47, 1.45, 1.02, A-03]
    ("""<td>Mandataire inverse, autorisation par appel, garde-fous, plafonds, journalisation, coupe-circuit</td>""",
     """<td>Mandataire inverse en entrée et mandataire sortant en sortie, autorisation par appel, garde-fous, plafonds, journalisation, coupe-circuit</td>""",
     ['1.47']),
    ("""IBM ContextForge (licence Apache 2.0; modèle de soutien non précisé par le projet);""",
     """IBM ContextForge (licence Apache 2.0; modèle de soutien non précisé par le projet)<strong><sup>[113]</sup></strong>;""",
     ['1.45']),
    ("""<td>Plateforme SaaS à agents intégrés</td><td>MCP et A2A natifs, identité par agent, télémétrie exportable</td>""",
     """<td>Plateforme SaaS à agents intégrés</td><td>MCP et A2A natifs, identité par agent, télémétrie exportable; contrôles compensatoires de l'EXIG-ARC-26 (accès aux systèmes de l'entreprise par la passerelle, clauses contractuelles, arrêt propre)</td>""",
     ['1.02', 'A-03']),
    # encadré latence [1.46]
    ("""inférieure à 5""" + NBSP + """ms, alors que son propre banc d'essai (page d'architecture) mesure""",
     """inférieure à 5""" + NBSP + """ms, et son propre banc d'essai (page d'architecture), dans d'autres conditions, mesure""",
     ['1.46']),
    # § 5.5 [1.99, 1.52, 1.25, 1.51]
    ("""<strong><sup>[151]</sup></strong>. figure 4 et tableau 13 en présentent l'organisation.</p>""",
     """<strong><sup>[151]</sup></strong>. La figure 4 et le tableau 13 en présentent l'organisation.</p>""", ['1.99']),
    ("""les trois mémoires longues sont persistées hors du modèle, récupérées au besoin et protégées par les mêmes contrôles d'écriture.""",
     """les trois mémoires longues sont persistées hors du modèle et récupérées au besoin; les mémoires épisodique et sémantique sont protégées par les contrôles d'écriture de l'EXIG-ARC-23, la mémoire procédurale par le processus de changement logiciel (EXIG-ARC-24). Le tableau 13 fait foi pour l'isolation de chaque type.""",
     ['1.52', '1.25']),
    ("""<td>Contexte minimal, compaction, aucun état en mémoire de processus (EXIG-ARC-05)</td>""",
     """<td>Contexte minimal, compaction, aucun état qui n'existe qu'en mémoire de processus (EXIG-ARC-05)</td>""", ['1.51']),
    ("""<td>Provenance de chaque entrée, filtrage des RP, isolation par mandant, expiration</td>""",
     """<td>Provenance de chaque entrée, filtrage des RP, isolation par locataire, par mandant et par serveur MCP, expiration par entrée (EXIG-ARC-23)</td>""",
     ['1.25']),
    ("""<td>Mise à jour par les propriétaires des données; filtrage selon le mandant (EXIG-ARC-16)</td>""",
     """<td>Mise à jour par les propriétaires des données; isolation par locataire et par serveur MCP; filtrage en lecture selon les droits effectifs (EXIG-ARC-16); expiration avec la validité de la source (EXIG-ARC-23)</td>""",
     ['1.25']),
    # [1.55, 1.87]
    ("""Le cadre accepte les deux modes, à condition qu'ils passent par les mêmes contrôles.""",
     """Le cadre accepte les deux modes, à condition qu'ils passent par les mêmes contrôles. En arrière-plan, le tampon des transcriptions en attente de consolidation porte l'identité du mandant captée pendant la session, est chiffré, a une durée de rétention maximale déclarée à la fiche et est purgé après la consolidation.""",
     ['1.55']),
    ("""dans le secteur privé (EXIG-CON-10, section 12.2).</p>""",
     """dans le secteur privé (RLRQ, c. P-39.1, ci-après « Loi sur le privé ») (EXIG-CON-10, section 12.2).</p>""",
     ['1.87']),
    # EXIG-ARC-22 [1.53]
    ("""<p>L'historique brut des échanges <strong>NE DOIT PAS</strong> être réinjecté en entier dans le contexte du modèle ni conservé tel quel comme mémoire longue. Ce qui doit durer est consolidé (résumé, fait, décision) dans la limite d'une fenêtre de contexte bornée à la fiche de l'agent, persisté hors du modèle et récupéré au besoin.</p>""",
     """<p>L'historique brut des échanges <strong>NE DOIT PAS</strong> être réinjecté dans le contexte du modèle au-delà de la borne de contexte, exprimée en jetons, que déclare la fiche de l'agent (annexe B), ni conservé tel quel comme mémoire longue. Au-delà de cette borne, l'historique est compacté; ce qui doit durer est consolidé (résumé, fait, décision), persisté hors du modèle et récupéré au besoin.</p>""",
     ['1.53']),
    # EXIG-ARC-23 [1.25, 1.54, A-17]
    ("""retirent les secrets et les renseignements personnels non nécessaires, l'isolent par locataire, par mandant et par serveur MCP, lui fixent une date d'expiration et permettent de restaurer un instantané antérieur.</p>""",
     """retirent les secrets et les renseignements personnels non nécessaires et permettent de restaurer un instantané antérieur. En mémoire épisodique, l'entrée est en outre isolée par locataire, par mandant et par serveur MCP, et porte une date d'expiration (EXIG-CON-10). En mémoire sémantique, connaissance partagée du domaine, elle est isolée par locataire et par serveur MCP, filtrée en lecture selon les droits effectifs (EXIG-ARC-16) et expire avec la validité de sa source. Valider la source d'un résumé produit par un modèle, c'est le contrôler contre un schéma qui fixe les champs admis et exclut le texte libre issu des outils. Une entrée écrite par une session marquée porte l'étiquette de cette session (EXIG-SEC-04); toute entrée relue est un contenu non fiable (EXIG-SEC-03), et l'outil de mémoire est marqué au catalogue.</p>""",
     ['1.25', '1.54', 'A-17']),
    # EXIG-ARC-25 [1.56]
    ("""ou par un service de mémoire qui applique les contrôles de l'exigence EXIG-ARC-23.</p>""",
     """ou par un service de mémoire qui applique les contrôles de l'EXIG-ARC-23, n'accepte que des écritures conditionnelles (ETag ou numéro de version) et tient un journal des écritures. Sont isolés des composants qui ont des identités de charge de travail et des espaces de noms distincts.</p>""",
     ['1.56']),
    ("""<li>Conserver l'état en mémoire de processus : le""",
     """<li>Conserver un état qui n'existe qu'en mémoire de processus : le""", ['1.51']),
    # § 5.6 [1.57, 1.58, A-10, A-13, A-15, A-16, A-06]
    ("""et obtient un jeton délégué au nom de la conseillère (section 9.3); l'état est persisté.</li>""",
     """et obtient pour l'agent un jeton délégué au nom de la conseillère, destiné à la passerelle (section 9.3); l'état est persisté.</li>""",
     ['1.57', 'A-16']),
    ("""qui vérifie le catalogue, restreint le jeton à l'audience du serveur MCP (paramètre <code>resource</code>, RFC 8707) et propage la trace;""",
     """qui vérifie le catalogue, obtient en tant que client, par échange de jetons (RFC 8693, paramètre <code>resource</code> de la RFC 8707), un jeton à audience unique pour ce serveur, et propage la trace;""",
     ['1.57', 'A-16']),
    ("""l'orchestrateur délègue la sous-tâche par A2A à l'agent de ce domaine""",
     """une branche du flux, déclarée au registre, délègue la sous-tâche par A2A à l'agent de ce domaine""", ['1.58']),
    ("""Le montant dépasse le seuil déclaré : le moteur suspend la tâche, état persisté, et présente l'action exacte à une approbatrice, dont la décision produit un jeton signé lié à cette action (section 8.5).</li>""",
     """Le montant, calculé par la passerelle à partir des arguments, dépasse le seuil déclaré : le moteur suspend la tâche, état persisté, et l'action exacte est présentée à une approbatrice, dont la décision produit un jeton signé lié à cette action, remis à la passerelle et jamais à l'agent (section 8.5).</li>""",
     ['1.58', 'A-10', 'A-13', 'A-15']),
    ("""<li><strong>Écriture.</strong> Le moteur reprend la tâche. L'appel passe par la passerelle avec le jeton d'approbation et une clé d'idempotence;""",
     """<li><strong>Écriture.</strong> Le moteur reprend la tâche, et l'agent rejoue l'appel avec sa clé d'idempotence et la référence de la demande d'approbation. La passerelle obtient un nouveau jeton délégué, ce qui revérifie les droits actuels de la conseillère (EXIG-IAM-02), apparie à l'appel le jeton d'approbation qu'elle conserve et le relaie; l'approbation sépare les tâches sans ajouter de droit, et la conseillère doit détenir elle-même le droit d'émettre l'avoir;""",
     ['1.58', 'A-10', 'A-15']),
    ("""L'artefact remonte au canal et la conseillère reçoit la confirmation avec la référence d'audit. Si une étape ultérieure échoue sans reprise possible, le moteur exécute la compensation déclarée, ici l'annulation de l'avoir (section 7.5).</li>""",
     """L'artefact remonte au canal, et la conseillère reçoit la confirmation, avec la référence d'audit, une fois la dernière étape compensable terminée. Si une étape ultérieure échoue avant ce point sans reprise possible, le moteur exécute la compensation déclarée, ici l'annulation de l'avoir, sous l'identité de compensation de l'orchestrateur (EXIG-ORC-31), et en avise la conseillère et l'approbatrice (section 7.5).</li>""",
     ['1.58', 'A-06']),
    ("""le mandant, le contexte de trace et les plafonds restants.""",
     """le mandant, le contexte de trace et la part restante de l'enveloppe de la tâche.""", ['1.37']),
    ("""En environnement serveur, aucun appel n'atteint un outil MCP, un agent ou un système d'un autre domaine sans traverser la passerelle, et aucune""",
     """En environnement serveur, aucun appel MCP ou A2A, quel que soit le domaine, ni aucune action P2 ou P3 n'échappe à la passerelle, et aucune""",
     ['1.01', 'A-01']),
    # ---------------------------------------------------------------- § 6.1 à 6.3
    ("""(art. 17 de la Loi sur la protection des renseignements personnels dans le secteur privé, RLRQ, c. P-39.1, ci-après « Loi sur le privé »)""",
     """(art. 17 de la Loi sur le privé)""", ['1.87']),
    ("""exigences propres au cadre.</figcaption>""",
     """exigences propres au cadre, dont le tableau 14 donne la formulation qui fait foi.</figcaption>""", ['1.62']),
    ("""<td>Accord d'interopérabilité par intégration; gestion du changement des contrats;""",
     """<td>Accord d'interopérabilité pour toute intégration qui franchit la frontière d'un domaine métier ou de l'entreprise (EXIG-INT-03); gestion du changement des contrats;""",
     ['1.62']),
    # EXIG-INT-01 [1.63]
    ("""avant sa mise en production, d'une revue couvrant les niveaux juridique, organisationnel, sémantique et technique du tableau 14.""",
     """avant sa mise en production, d'une revue proportionnée selon le tableau 14 : niveaux sémantique et technique pour une intégration intradomaine qui n'emploie que des outils P0 ou P1 et ne traite pas de renseignements personnels; les quatre niveaux, juridique, organisationnel, sémantique et technique, dans tous les autres cas.""",
     ['1.63']),
    # EXIG-INT-02 [1.24, 1.59, A-03]
    ("""le format par défaut étant le Schema Object d'AsyncAPI) et s'appuyer sur le vocabulaire métier et les données de référence de l'entreprise (taxonomies, listes de codes, unités et devises explicites). Ces schémas <strong>DOIVENT</strong> être gérés au niveau de l'entreprise, et non par chaque équipe d'agent.</p>""",
     """le format par défaut étant le Schema Object d'AsyncAPI; la chaîne d'outils qui lit ces contrats est éprouvée sur ce format avant l'inscription au catalogue). Les schémas produits par l'entreprise <strong>DOIVENT</strong> s'appuyer sur le vocabulaire métier et les données de référence de l'entreprise (taxonomies, listes de codes, unités et devises explicites) et être gérés au niveau de l'entreprise, et non par chaque équipe d'agent. Un schéma de tiers (serveur MCP, carte d'agent ou contrat d'événement d'un éditeur ou d'un partenaire) <strong>DOIT</strong> être inscrit au catalogue avec son empreinte, épinglé et approuvé; sa correspondance avec le vocabulaire d'entreprise est tenue à l'adaptateur ou à la passerelle.</p>""",
     ['1.24', '1.59', 'A-03']),
    # § 6.2 [1.65, 1.22, A-20, A-01, A-02, 1.09]
    ("""L'événement comble un troisième besoin, car MCP ne garantit ni la livraison ni la cohérence des données, alors qu'un journal d'événements persistant découple producteurs et consommateurs, comme le souligne l'architecte Kai Waehner<strong><sup>[167]</sup></strong>.</p>""",
     """L'événement comble un troisième besoin : un appel d'outil MCP est un échange requête-réponse point à point, sans rétention, ni rejeu, ni diffusion à plusieurs abonnés, alors qu'un journal d'événements persistant découple producteurs et consommateurs dans le temps (voir aussi Kai Waehner<strong><sup>[167]</sup></strong>).</p>""",
     ['1.65']),
    ("""la cible raisonne-t-elle? Si elle exécute une fonction aux entrées et aux sorties définies, c'est un outil, même si elle emploie un modèle en interne (règle du cadre). Si elle planifie, conserve un état et peut renvoyer une question, c'est un agent. Si l'émetteur ne doit pas connaître ses destinataires, c'est un événement. Dans tous les cas, l'échange qui sort d'un domaine passe par la passerelle d'agents (section 9.4);""",
     """la cible choisit-elle elle-même ses actions? Elle est un agent si elle choisit elle-même, au moyen d'un modèle, les actions qu'elle exécute; sinon, c'est un outil, même si elle emploie un modèle en interne pour transformer une donnée, conserve l'état d'une tâche ou demande une précision (Tasks, élicitation MCP) (règle du cadre, tableau 7). Si l'émetteur ne doit pas connaître ses destinataires, c'est un événement. Tout appel MCP ou A2A, quel que soit le domaine, passe par la passerelle d'agents, et tout événement par le courtier (EXIG-ARC-01, EXIG-ARC-13; section 9.4);""",
     ['1.22', '1.09', 'A-20', 'A-01', 'A-02']),
    ("""Les trois passent par la passerelle d'agents et par le catalogue d'entreprise.</p>""",
     """Rien ne contourne les points d'application : la passerelle d'agents pour MCP, A2A et les actions P2 ou P3, la passerelle de modèles pour l'inférence et le courtier pour les événements (EXIG-EVT-11), tous alimentés par le catalogue d'entreprise.</p>""",
     ['1.09', 'A-01', 'A-02']),
    # EXIG-INT-04 [1.21, 1.43, A-20]
    ("""A2A pour la délégation à un autre agent; CloudEvents, décrit par un contrat AsyncAPI, pour les événements. Tout connecteur""",
     """A2A pour toute délégation à un agent d'un autre domaine, d'un autre cadriciel, d'un tiers ou d'un autre processus (EXIG-A2A-01, sauf coexistence bornée de l'EXIG-A2A-15); CloudEvents, décrit par un contrat AsyncAPI, pour les événements; pour l'interface utilisateur, AG-UI en pilote ou le flux SSE structuré produit par l'orchestrateur (tableau 15). L'appel d'inférence relève de l'EXIG-ARC-08. Tout connecteur""",
     ['1.21', '1.43', 'A-20']),
    # EXIG-INT-05 devient renvoi [1.21, 1.22, A-20]
    ("""<p>Un agent d'un autre domaine ou d'un tiers, qui planifie, conserve un état ou peut demander une précision, <strong>DEVRAIT</strong> être invoqué par A2A plutôt qu'enveloppé dans un outil MCP. L'enveloppe « agent comme outil » reste permise à l'intérieur d'un même agent ou d'un même domaine de confiance.</p>""",
     """<p>Voir l'EXIG-A2A-01, qui impose A2A pour toute délégation à un agent d'un autre domaine, d'un autre cadriciel, d'un tiers ou d'un autre processus. Règle résiduelle : l'enveloppe « agent comme outil » n'est permise qu'entre sous-agents d'un même orchestrateur, dans un même processus; le critère qui distingue un agent d'un outil est celui de la section 6.2.</p>""",
     ['1.21', '1.22', 'A-20', 'A-30']),
    # § 6.3 statuts [1.20, A-21]
    ("""Chaque entrée porte l'un des quatre statuts suivants, éventuellement assorti d'une réserve :</p>""",
     """Chaque entrée porte l'un des cinq statuts suivants, éventuellement assorti d'une réserve :</p>""", ['A-21']),
    ("""<li>Contenir existant toléré derrière un adaptateur, sans nouvel usage, avec un plan de sortie daté.</li>""",
     """<li>Contenir existant toléré derrière un adaptateur, sans nouvel usage, avec un plan de sortie daté;</li>
<li>Suspendu prononcé pour un motif de sécurité (EXIG-INT-14, EXIG-GOV-14) : la passerelle cesse immédiatement de servir l'élément, sans attendre la fin d'une coexistence.</li>""",
     ['1.20', 'A-21']),
    # tableau 15 [1.23, 1.60, 1.61, 1.43, A-21, A-29, A-31]
    ("""courante au 27 octobre 2026<strong><sup>[34, 168]</sup></strong></td>""",
     """courante au 27 octobre 2026<strong><sup>[34, 168]</sup></strong>; révision 2025-11-25 au statut Contenir jusqu'au 28 juillet 2027 (EXIG-MCP-22)</td>""",
     ['1.23', 'A-21']),
    ("""<td>OpenAPI 3.1.x ou 3.2.x (3.2.1 du 10 septembre 2026)""",
     """<td>OpenAPI 3.1.x comme version de référence, 3.2.x admise (3.2.1 du 10 septembre 2026)""", ['1.60']),
    ("""AsyncAPI 3.x pour le contrat<strong>[173, 174]</strong></td>""",
     """AsyncAPI 3.0 pour le contrat, versions 3.x ultérieures admises après essai de la chaîne d'outils<strong>[173, 174]</strong></td>""",
     ['1.60']),
    ("""<td>Tout événement produit ou consommé par un agent; extensions de gouvernance et compteur de sauts (6.7).</td>""",
     """<td>Tout événement produit ou consommé par un agent; extensions de gouvernance et compteur de sauts (6.7), sous réserve : ces extensions documentées n'ont aucun statut officiel.</td>""",
     ['1.61']),
    ("""<td>OAuth 2.1, Internet-Draft (draft-ietf-oauth-v2-1-16, septembre 2026)<strong><sup>[176]</sup></strong></td>""",
     """<td>OAuth 2.1, Internet-Draft du groupe de travail OAuth, à la révision épinglée au catalogue (draft-ietf-oauth-v2-1-16 du 3 septembre 2026 à l'état des sources)<strong><sup>[176]</sup></strong></td>""",
     ['A-31']),
    ("""version épinglée (v1.41.0 ou première version étiquetée du dépôt <code>semantic-conventions-genai</code>)""",
     """version de référence v1.41.0 (ligne v1.41, correctif v1.41.1 admis), jusqu'à l'homologation d'une version étiquetée du dépôt <code>semantic-conventions-genai</code>""",
     ['1.60', 'A-29']),
    ("""<td>Couche de correspondance dans les tableaux de bord; attributs d'entreprise""",
     """<td>Version émise par chaque composant consignée au catalogue; couche de correspondance versionnée dans le collecteur, qui la ramène à la version de référence (EXIG-OBS-01); attributs d'entreprise""",
     ['A-29']),
    ("""<td>Pilotes; à défaut, flux SSE structuré produit par l'orchestrateur.</td>""",
     """<td>Pilotes. En production : flux SSE structuré produit par l'orchestrateur, patron interne au statut Adopter, dont le format d'événements est consigné au catalogue.</td>""",
     ['1.43', 'A-21']),
    # figure 6 [1.60, 1.61]
    ("""et ce qui reste en veille. Source""",
     """et ce qui reste en veille; le bandeau de veille réunit des entrées aux statuts Évaluer (pilotes) et Surveiller (hors production), et « OAuth 2.x » y désigne OAuth 2.0 profilé par la RFC 9700, le profil OAuth 2.1 restant un brouillon. Le tableau 15 fait foi pour les versions et les statuts. Source""",
     ['1.60', '1.61']),
    # [1.36, A-22, A-23]
    ("""<p>Les versions sont fixées au catalogue, pas dans chaque contrat d'agent : une montée de version se décide une fois, pour tout le parc. Le comité révise le catalogue chaque trimestre (section 11.7); un correctif de sécurité peut justifier une révision extraordinaire.</p>""",
     """<p>Les versions sont épinglées au catalogue, pas dans chaque contrat d'agent : une montée de version se décide une fois, pour tout le parc (section 1.6). L'architecture d'entreprise révise le catalogue chaque trimestre et le comité en approuve les changements de statut (EXIG-GOV-18, section 11.7); la publication d'une version incompatible ou d'une dépréciation d'un standard adopté, ou un correctif de sécurité, déclenche une révision extraordinaire.</p>""",
     ['1.36', 'A-22', 'A-23']),
    # EXIG-INT-06 [1.20, A-21]
    ("""<p>Un protocole, un standard ou une extension de protocole <strong>DOIT</strong> figurer au catalogue avec le statut Adopter pour être employé en production. Le statut Évaluer limite l'usage à des pilotes; le statut Surveiller l'exclut de la production; le statut Contenir interdit tout nouvel usage.</p>""",
     """<p>Tout nouvel usage en production d'un protocole, d'un standard ou d'une extension de protocole <strong>DOIT</strong> reposer sur une entrée du catalogue au statut Adopter. Un usage existant au statut Contenir reste permis derrière un adaptateur jusqu'à l'échéance de son plan de sortie, sans nouvel usage. Le statut Évaluer limite l'usage aux pilotes (EXIG-GOV-20); le statut Surveiller exclut tout usage en production; le statut Suspendu, prononcé pour un motif de sécurité, fait cesser immédiatement le service par la passerelle.</p>""",
     ['1.20', 'A-21']),
    # EXIG-INT-07 [1.23, A-21]
    ("""déclarer les versions qu'il prend en charge; une déclaration incompatible avec le catalogue <strong>DOIT</strong> bloquer l'inscription au registre.</p>""",
     """déclarer les versions qu'il prend en charge. Une déclaration est compatible si elle inclut la version de référence, ou une version au statut Contenir assortie d'une date de migration inscrite au catalogue (EXIG-MCP-22, EXIG-A2A-15); une déclaration incompatible <strong>DOIT</strong> bloquer l'inscription au registre.</p>""",
     ['1.23', 'A-21']),
    # EXIG-INT-08 [1.36, A-22]
    ("""<p>Le comité d'architecture et des risques agentiques <strong>DOIT</strong> réviser le catalogue des protocoles au moins une fois par trimestre et consigner, pour chaque entrée, la date de révision, le statut retenu et sa justification. Tout changement de statut est notifié aux propriétaires des agents qui emploient l'entrée.</p>""",
     """<p>Le catalogue des protocoles <strong>DOIT</strong> être révisé au moins une fois par trimestre selon l'EXIG-GOV-18 : l'architecture d'entreprise rédige la révision, et le comité d'architecture et des risques agentiques en approuve les changements de statut. Chaque entrée porte la date de révision, le statut retenu et sa justification. Tout changement de statut est notifié aux parrains des agents qui emploient l'entrée.</p>""",
     ['1.36', 'A-22', 'A-34']),
    # EXIG-INT-09 [A-22, A-31]
    ("""brouillon individuel, préversion ou projet hébergé par une fondation.</p>""",
     """brouillon individuel, préversion ou projet hébergé par une fondation. Pour une extension qui déclare un stade de maturité (Experimental, Beta, Stable), le catalogue l'inscrit extension par extension, et une extension au stade Beta porte une réserve.</p>""",
     ['A-22']),
    ("""(la version -16 d'OAuth 2.1 expire le 7 mars 2027)""",
     """(la révision -16 d'OAuth 2.1, du 3 septembre 2026, expirait le 7 mars 2027; la révision -17 l'a remplacée le 31 octobre 2026)""",
     ['A-31']),
]

CORRECTIONS = [(T(a), T(b), k) for a, b, k in _C]

_J = [
    # (localisation, correctif ou motif de non-retenue, constats)
    ('Sommaire, décision 2; ch. 5, intro; figure 3 (légende); EXIG-ARC-01; tableau 10; § 5.6 (À RETENIR); § 6.2', "Portée unique de la passerelle (A-01) : tout appel MCP et A2A quel que soit le domaine et toute action P2-P3; seule une fonction locale P0-P1 inscrite au catalogue s'en dispense. EXIG-MCP-01 et EXIG-IAM-17 relèvent des tranches t2 et t4; figure 3 non modifiable : « hors de son domaine » reste dans le schéma, la légende renvoie à l'EXIG-ARC-01.", ['1.01', '03-08', '04-01', '01-05', 'A-01']),
    ('§ 5.4, EXIG-ARC-26 (nouvelle exigence); PRIN-09; § 2.4; § 5.3 (plan C); EXIG-ARC-08, ARC-11; tableaux 1 et 12', "Nouvelle exigence EXIG-ARC-26 « Agents intégrés aux logiciels-services » (A-03) : contrôles compensatoires (inscription, accès par la passerelle, clauses APP-05, 06, 08, 13, arrêt propre, schémas épinglés), approbation P3 équivalente ou plafond N2; renvois depuis PRIN-09, § 2.4, plan C, ARC-08, ARC-11 et tableaux 1 et 12. Annexe D à compléter (t6).", ['1.02', '04-03', '03-10', '02-06', 'A-03']),
    ('Sommaire, décisions 2 et 5 et « Par où commencer »; § 1.4; § 1.6', "Décisions 2 et 5 présentées comme état cible, avec renvoi au régime transitoire de l'EXIG-GOV-21 (A-26, exigence créée par t5); tableau 58 rendu normatif pour les seules phases d'exigibilité.", ['1.03', '01-01', 'A-26']),
    ('Sommaire, décision 1; tableau 1; EXIG-ARC-14', "« Jamais réécrites » devient « sans réécriture de la logique métier »; l'ajout minimal pour l'idempotence est permis, et l'adaptateur sans mécanisme atomique déclare l'outil non idempotent (A-09). La reformulation d'EXIG-ORC-22 relève de t2.", ['1.04', '01-02', '04-05', '01-20', 'A-09']),
    ('§ 5.2 (Temporal, Step Functions); EXIG-ARC-06', "Reprise interdite depuis un point de contrôle plus ancien que la conservation des clés d'idempotence (A-09); limites d'historique de Temporal et réserve « Retry » de Step Functions ajoutées (lit. 70-71). Durée de conservation des clés à l'EXIG-ORC-21 et ORC-13 : t2/t3.", ['1.05', '04-07', '04-06', 'A-09']),
    ('PRIN-12; sommaire, décision 7', "Mode fermé « vers l'avant » et canal de compensation distinct (EXIG-ORC-31, A-06). Objectif de disponibilité (EXIG-IAM-22) et alinéas d'EXIG-AUT-11 et IAM-18 : t3 et t4.", ['1.06', '03-11', '04-04', 'A-06', 'A-04']),
    ('EXIG-ARC-12', "La passerelle applique la liste de suspension reçue par le canal signé de l'EXIG-IAM-22, même sans plan de contrôle; Pourquoi reformulé (« par une seule décision »). Validité de la politique en cache (EXIG-IAM-18, 22) : t4.", ['1.07', '04-09', 'A-04']),
    ('Sommaire, décision 6; PRIN-07; § 3.1 (paliers, P0)', "Retrait rattaché à la session définie au tableau 7, étendu aux outils P3, marquage propagé avec la donnée, outil de recherche P0 à requête libre traité comme outil d'envoi (A-17). Définition dans l'EXIG-SEC-06 : t4.", ['1.08', '03-09', '01-06', 'A-17']),
    ('§ 6.2 (À RETENIR et règle de départage); EXIG-ARC-13', "Les événements passent par le courtier et l'intercepteur de publication (EXIG-EVT-11, A-02), autorisation par sujet et retrait appliqué à la publication par une session marquée.", ['1.09', '05-04', 'A-02']),
    ('Sommaire, décision 10', "Non retenu dans t1 : la décision 10 est exacte une fois le tableau 50 doté de sa colonne E-23 (A-24), correctif qui relève de t5.", ['1.10', '01-03', 'A-24']),
    ('Méthode; § 1.7; § 2.2 (tableau 5)', "Trois populations (121, 428, 49 ajoutées) et total de 473 entrées doublons compris; écart non réconcilié et registre par affirmation non publié énoncés comme limites; date d'approbation du 4 août retirée du tableau 5 (lit. 41, non vérifiée) et jalons dits « vérifiés sauf mention contraire ». Titre du tableau 5 non modifié (liste des tableaux).", ['1.11', '01-04', '02-05', 'A-31']),
    ('§ 1.6; sommaire, décision 1; Avertissements', "Le catalogue fait foi pour la version épinglée là où une exigence y renvoie; la version citée est la valeur initiale; les échéances datées restent au texte (A-23). Reformulation d'A2A-01, MCP-22, APP-07 et APP-08 : t2 et t5.", ['1.12', '02-01', 'A-23']),
    ('§ 1.6; § 4.3, rang 1', "Les engagements contractuels ne priment que s'ils sont en vigueur à l'adoption, pour une transition bornée, et jamais sur l'EXIG-GOV-17; renvoi à la nouvelle EXIG-APP-18 (t5).", ['1.13', '02-02', '03-07', 'A-23']),
    ('§ 1.6; § 4.3', "Ordre de départage d'A-23 (droit, GOV-17, DOIT sur DEVRAIT, source unique, spécial sur général), cumul des contraintes cumulables et refus jusqu'à la décision du comité. La règle « plus stricte par dimension » et « préserver la preuve » de la tranche n'est pas retenue : l'arbitrage A-23 la remplace.", ['1.14', '02-03', '03-06', 'A-23']),
    ('§ 1.4; § 3.1 (intro)', "Périmètre normatif d'A-23 : règles d'interprétation des § 1.2, 1.5, 1.6, 4.2 et 4.3, tableau 7, tableaux 28 et 31 qui font foi sur le § 3.1, structures d'annexe visées, tableau 58 pour l'exigibilité; définition de la mise en production (A-25).", ['1.15', '02-04', '03-15', 'A-23', 'A-25']),
    ('§ 3.1 (tableau 7, N0); § 3.2; tableau 1; sommaire, décision 4; PRIN-04', "N0 qualifie un flux sans choix laissé au modèle, non un agent; flux assisté par IA inscrit avec le niveau de ses écritures (A-27). Tableau 28 et EXIG-AUT-01 et 02 : t3.", ['1.16', '03-01', '02-22', 'A-27']),
    ('§ 3.1 (N3, N4); § 3.3', "N4 se distingue de N3 par l'origine de la tâche, lue par la passerelle; N3 sur demande d'une personne, avec escalade à une personne désignée dans un délai borné (A-27). Tableaux 28 et 30 : t3.", ['1.17', '03-02', 'A-27']),
    ('§ 3.1 (paliers, N3)', "P2 = réversible ou compensable vers un état métier équivalent à impact borné; P3 même si une compensation est déclarée; « réversibles ou compensables » retiré de N3 (A-27). EXIG-AUT-08 : t3.", ['1.18', '03-03', '03-13', 'A-27']),
    ('EXIG-ARC-01; tableau 7 (« Environnement serveur »)', "Environnement serveur défini (tout environnement autre qu'un poste de développement individuel sans justificatif de production, poste de travail, navigateur, mobile et périphérie compris). MCP-08 et IAM-17 : t2, t4.", ['1.19', '04-02', 'A-01']),
    ('§ 6.3 (statuts); EXIG-INT-06', "Statut Adopter exigé pour tout nouvel usage; usage existant Contenir permis jusqu'au plan de sortie; statut Suspendu ajouté (A-21). EXIG-GOV-20 : t5.", ['1.20', '05-01', 'A-21']),
    ('EXIG-INT-04; EXIG-INT-05', "INT-04 reprend la portée d'A2A-01 (autre domaine, cadriciel, tiers ou processus); INT-05 devient un renvoi à A2A-01, avec la règle résiduelle de l'enveloppe entre sous-agents d'un même orchestrateur (A-20, A-30).", ['1.21', '05-02', 'A-20']),
    ('Tableau 7 (Outil); § 6.2; EXIG-INT-05', "Critère unique d'A-20 : est un agent la cible qui choisit elle-même, au moyen d'un modèle, ses actions; l'état et l'élicitation n'en font pas un agent. Le critère « conserve un état » de la tranche n'est pas retenu (A-20).", ['1.22', '05-03', 'A-20']),
    ('Tableau 15 (MCP); EXIG-INT-07', "Révision 2025-11-25 inscrite au statut Contenir jusqu'au 28 juillet 2027; déclaration compatible définie (A-21).", ['1.23', '05-08', 'A-21']),
    ('EXIG-INT-02', "Gestion d'entreprise limitée aux schémas produits par l'entreprise; schéma de tiers inscrit avec son empreinte, épinglé et approuvé, correspondance tenue à l'adaptateur ou à la passerelle (A-03).", ['1.24', '05-09', 'A-03']),
    ('EXIG-ARC-23; tableau 13; figure 4 (légende)', "Règles scindées : épisodique (isolation par mandant, expiration par entrée), sémantique (isolation par locataire et serveur, filtrage en lecture, expiration avec la source). Figure non modifiable : le schéma montre encore « isolation par locataire et par serveur MCP » sans distinction; la légende renvoie au tableau 13.", ['1.25', '05-07']),
    ('PRIN-03; tableau 7 (Mandant, Délégation); EXIG-ARC-07, ARC-16', "Droits effectifs à trois termes (mandant, portée au registre, portée de la tâche), sans élargissement; mandant d'une chaîne = entité d'origine (A-16).", ['1.26', '03-04', '03-05', '04-14', 'A-16']),
    ('Encadré « Sans dérogation possible »', "Non retenu dans t1 : l'ajout d'EXIG-AUT-07 aux non-dérogeables ou au tableau 46 relève de t5 (EXIG-GOV-17, source unique selon A-24); l'encadré devient un simple rappel.", ['1.27', '03-12', 'A-24']),
    ('Sommaire, décision 4; § 1.3, étape 2; PRIN-04', "La classe plafonne le niveau, renvoi à l'EXIG-CON-02 seule source. Intégration des conditions de la classe modérée à CON-02 (tableau 46) : t5.", ['1.28', '01-07', '03-22', 'A-24']),
    ('§ 3.1 (N3, N4)', "Étiquettes HOTL et « hors de la boucle » limitées : les actions P3 sont approuvées une à une, hors bande.", ['1.29', '03-14']),
    ('Tableau 8', "Approbation dans la session par un jeton signé émis hors de l'interface de l'agent (EXIG-AUT-12, AUT-13); P3 hors bande.", ['1.30', '03-20']),
    ('Tableau 10, ligne « PRIN-07 et utilité »', "Arbitrage par classe : élevée, patron obligatoire (EXIG-SEC-07); modérée, recommandé; faible, retrait de l'EXIG-SEC-06. CaMeL daté de la version 2 (lit. 46).", ['1.31', '03-19']),
    ('§ 3.4', "Identité par instance dès que les instances servent des mandants différents ou doivent être révocables séparément.", ['1.32', '03-25']),
    ('Tableau 3; § 4.3 (Dérogations, encadré)', "Délégation de 90 jours et séparation entre instruction et décision reprises; GOV-17 désignée seule liste. Le « ni » de l'EXIG-GOV-17 (« sans fiche ou sans parrain ») relève de t5; l'encadré emploie déjà « ou ».", ['1.33', '02-26', '03-17', 'A-24']),
    ('§ 4.3, Dérogations', "Dérogation à un principe ou à une exigence, identifiant requis; à l'échéance d'une dérogation de composant, retrait du catalogue et suspension des agents dépendants.", ['1.34', '03-18']),
    ('EXIG-ARC-20', "ABB toujours nécessaires énumérés dans l'exigence (passerelle d'agents, plans transversaux; selon le cas ARC-05, 08, 10). La colonne « obligatoire si » au tableau 12 n'est pas ajoutée (un tableau se corrige cellule par cellule).", ['1.35', '04-08']),
    ('EXIG-ARC-05, ARC-06; EXIG-INT-08; § 1.6; § 6.3', "Déclencheur unifié avec ORC-11 (« plus d'une étape »); ARC-06 renvoie à ORC-13; INT-08 renvoie à GOV-18 (l'architecture révise, le comité approuve, A-22). Les blocs gardent leur énoncé propre, réduit à un renvoi partiel.", ['1.36', '04-11', '05-22', 'A-22']),
    ('EXIG-ARC-02; § 5.6 (À RETENIR)', "« Plafonds restants » devient « part restante de l'enveloppe » (EXIG-FIN-04), « jetons de modèle ». La phrase du ch. 7 (« budget restant ») relève de t2/t3.", ['1.37', '04-13']),
    ('EXIG-ARC-13', "Autorisation par sujet selon le catalogue (EXIG-EVT-07) ajoutée.", ['1.38', '04-15']),
    ('EXIG-ARC-04', "Trace entrante poursuivie seulement si sa source est de confiance, redémarrée à une frontière de confiance.", ['1.39', '04-16']),
    ('EXIG-ARC-04', "Mandant d'un déclencheur système : identité du service et propriétaire, jamais un attribut de l'événement (EXIG-EVT-07).", ['1.40', '04-26']),
    ('EXIG-ARC-09', "Changement de modèle toujours après la réévaluation de l'EXIG-GOV-12 (A-24); alias résolu vers un instantané daté, épinglé.", ['1.41', '04-17', 'A-24']),
    ('EXIG-ARC-08', "Phrases fusionnées; appel d'inférence défini (plongements, juges, classifieurs de garde-fous); portée limitée aux agents dont l'entreprise contrôle l'exécution. L'exclusion d'un modèle embarqué n'est pas tranchée.", ['1.42', '04-27']),
    ('EXIG-INT-04; tableau 15 (AG-UI)', "Interface utilisateur : AG-UI en pilote ou flux SSE structuré, patron interne Adopter (A-21); inférence renvoyée à l'EXIG-ARC-08.", ['1.43', '05-21', 'A-21']),
    ('EXIG-ARC-01', "« À une version et une empreinte approuvées ».", ['1.44', '04-28']),
    ('§ 5.4; tableau 12', "Règle des SBB incomplets ajoutée (SBB complémentaire, dérogation EXIG-ARC-21 ou refus EXIG-ARC-20); appel [113] ajouté à IBM ContextForge. Non retenu en partie : références primaires d'Azure API Center, MuleSoft Agent Registry, AgentCore Runtime et ServiceNow AI Agent Fabric (aucune source vérifiée à citer) et persistance d'ADK (fait externe non vérifié).", ['1.45', '04-18', '04-19']),
    ('§ 5.4, encadré ATTENTION', "« Alors que » remplacé par « dans d'autres conditions ». Non retenu dans t1 : regrouper l'encadré au § 13.2 et fixer un budget de latence relève de t4 et t5.", ['1.46', '04-20']),
    ('§ 5.2, couche 4; tableau 12', "Mandataire inverse en entrée, mandataire sortant en sortie.", ['1.47', '04-23']),
    ('EXIG-ARC-19', "Renvoi « (section 11.1) » pour l'équipe plateforme.", ['1.48', '04-24']),
    ('§ 5.2, couche 2', "Réserve « Retry » de Step Functions et limite d'historique de Temporal (Continue-As-New), réessais d'activités bornés (lit. 70-71).", ['1.49', '04-10', 'A-09']),
    ('Sommaire, décision 7; PRIN-12', "Un seul exercice trimestriel, celui de l'EXIG-SEC-26 (A-05). L'exercice global annuel proposé n'est pas retenu : A-05 fixe un exercice unique. EXIG-ORC-28 et figure 18 : t3, t4.", ['1.50', '01-11', 'A-05']),
    ('Tableau 13; anti-patrons du § 5.5', "« Aucun état qui n'existe qu'en mémoire de processus ». Figure 4 non modifiable : le schéma garde « état conservé en mémoire de processus ».", ['1.51', '04-12']),
    ('Figure 4 (légende)', "Contrôles distingués : ARC-23 pour l'épisodique et la sémantique, ARC-24 pour la procédurale. Figure non modifiable : la figure 3 garde le placement des mémoires par couche.", ['1.52', '04-25', '05-14']),
    ('EXIG-ARC-22', "Borne de contexte en jetons déclarée à la fiche; compaction au-delà. Le champ correspondant de l'annexe B relève de t6.", ['1.53', '05-15']),
    ('EXIG-ARC-23', "Validation de source d'un résumé définie (schéma, champs admis, pas de texte libre d'outil); entrée relue non fiable et outil marqué; étiquette de session portée par l'entrée (A-17).", ['1.54', '05-16', 'A-17']),
    ('§ 5.5, « Écrire en mémoire longue »', "Tampon de transcriptions borné (identité du mandant, chiffrement, rétention déclarée, purge).", ['1.55', '05-17']),
    ('EXIG-ARC-25', "Écritures conditionnelles, journal des écritures et définition d'« isolés ».", ['1.56', '05-18']),
    ('§ 5.6, étapes 3 et 5', "La passerelle obtient, comme client, un jeton à audience unique par échange de jetons; jeton délégué de l'agent destiné à la passerelle (A-16).", ['1.57', '05-05', 'A-16']),
    ('§ 5.6, étapes 6 à 9', "Branche de flux déclarée; montant calculé par la passerelle; jeton d'approbation conservé par la passerelle et apparié au rejeu (A-10, A-15); nouveau jeton délégué à la reprise; confirmation après la dernière étape compensable; compensation sous l'identité de l'orchestrateur et notifiée (A-06).", ['1.58', '05-06', '05-24', 'A-10', 'A-15', 'A-06']),
    ('EXIG-INT-02', "Chaîne d'outils éprouvée sur le format 2020-12 avant inscription (choix du cadre); la liste des formats obligatoires d'AsyncAPI 3.x n'est pas affirmée, faute de vérification dans audit_lit.", ['1.59', '05-10']),
    ('Tableau 15 (OpenAPI, AsyncAPI, OpenTelemetry); figure 6 (légende)', "Version de référence par standard (OpenAPI 3.1.x, AsyncAPI 3.0, OpenTelemetry v1.41.0 avec correctif v1.41.1 admis, A-29); couche de correspondance au collecteur. Figure 6 non modifiable : « OpenAPI 3.1 » y concorde désormais avec le tableau.", ['1.60', '05-11', 'A-29']),
    ('Tableau 15 (CloudEvents); figure 6 (légende)', "Réserve sur les extensions CloudEvents sans statut officiel; la légende de la figure 6 précise les statuts du bandeau de veille et le sens d'« OAuth 2.x ». La colonne « statut normatif » n'est pas ajoutée (tableau corrigé cellule par cellule); figure non modifiable.", ['1.61', '05-12', '05-13']),
    ('Tableau 14; figure 5 (légende)', "Accord d'interopérabilité aligné sur l'EXIG-INT-03; la légende de la figure 5 renvoie au tableau 14, qui fait foi. Figure non modifiable.", ['1.62', '05-19']),
    ('EXIG-INT-01', "Revue proportionnée : sémantique et technique pour P0-P1 intradomaine sans RP; quatre niveaux sinon.", ['1.63', '05-20']),
    ('Tableau 15 (MCP, extensions)', "Non retenu : la nature « extension officielle » de l'autorisation dans MCP 2026-07-28 est un fait externe qu'audit_lit ne vérifie pas; le texte n'est pas démontré faux.", ['1.64', '05-26']),
    ('§ 6.2; § 1.7; § 2.4', "Argument de Kai Waehner remplacé par les propriétés de l'échange MCP, la référence [167] restant en « voir aussi ». § 2.4 et § 5.1 présentent déjà [44] et [45] comme des thèses de fournisseurs; leur reclassement en catégorie C à l'annexe F relève de t6.", ['1.65', '02-07', '05-25', 'A-31']),
    ('Sommaire; § 1.4', "« Ou, à défaut, par une justification consignée ». Le mode de vérification par exigence à l'annexe D relève de t6.", ['1.66', '01-19', '02-31']),
    ('§ 1.2', "Premier accès à une ressource ou à des données (index documentaire) fait entrer dans la portée.", ['1.67', '02-24']),
    ('Tableau 1', "Agents achetés dans la portée dès qu'ils peuvent agir, quel que soit qui les a activés.", ['1.68', '02-25']),
    ('Avertissements; sommaire, décisions 1 et 2', "« Catalogue des protocoles » et « catalogue d'entreprise » distingués.", ['1.69', '01-10']),
    ('Sommaire, « Pourquoi maintenant »; § 2.1 (ATTENTION)', "Chiffre de 150 000 qualifié de prévision sans méthode publiée, ordre de grandeur prospectif (lit. 43). La sous-catégorie « prévision d'analyste » du tableau 66 relève de t6.", ['1.70', '01-12']),
    ('Sommaire, 13 %', "Appel [2] ajouté (lit. 43 : source confirmée) et mention « population et méthode non publiées ».", ['1.71', '01-13']),
    ('§ 2.1', "Multiplicateurs rattachés aux mesures d'Anthropic sur son système de recherche multiagent (lit. 49).", ['1.72', '02-10']),
    ('§ 2.1', "Population de l'étude d'IBM et du Ponemon Institute précisée : organisations qui ont toutes subi une violation.", ['1.73', '02-11']),
    ('§ 2.1, encadré ATTENTION et paragraphe des plateformes', "Règle unique de classement (prévisions, enquêtes, fournisseurs intéressés, investisseur, déclarations des projets); « selon le projet » et « selon la Linux Foundation » ajoutés.", ['1.74', '02-12']),
    ('§ 2.1', "Inférence « pression financière » retirée; échantillons variables d'une édition à l'autre signalés.", ['1.75', '02-13']),
    ('§ 2.1', "Mention « estimation hors inférence » retirée, faute de vérification de la ventilation de [16]; Menlo Ventures présenté comme investisseur du secteur. Le périmètre géographique reste celui du sondage américain déjà indiqué.", ['1.76', '02-14']),
    ('§ 2.1', "Chiffre attribué au projet (« selon le projet »). Non retenu en partie : « plus de » et « publics » ne sont pas vérifiés dans audit_lit.", ['1.77', '02-15']),
    ('§ 2.1 (« Azure AI Foundry »)', "Non retenu : le nom employé par [15] n'est pas vérifié dans audit_lit; à relire à la source avant correction.", ['1.78', '02-16']),
    ('Tableau 7 (Agent)', "Définition marquée comme paraphrase d'ISO/IEC 22989 vérifiée par la fiche de catalogue, non au texte.", ['1.79', '02-23']),
    ('Tableau 10 (CaMeL)', "Chiffres datés de la version 2 du 24 juin 2025 (lit. 46). Non retenu en partie : la mention des canaux latéraux n'est pas vérifiée; l'épinglage de [101] relève de t6.", ['1.80', '03-23']),
    ('§ 3.2 (ReAct)', "Exactitude parfois moindre sur HotpotQA ajoutée.", ['1.81', '03-24']),
    ('§ 1.4', "« Le guide de Microsoft recommande »; équivalence producteur-vérificateur et évaluateur-optimiseur précisée.", ['1.82', '02-19']),
    ('Figure 2 (légende); § 2.3; § 2.2', "Point d'application unique, autorisations par couple agent-outil; 10 000 intégrations présentées comme maximum théorique; « pari sur un seul éditeur » nuancé. Figure non modifiable : le schéma garde « une politique ».", ['1.83', '02-09', '02-30']),
    ('§ 2.4 (Loi 25)', "Essentiel en vigueur depuis le 22 septembre 2023, entièrement depuis le 22 septembre 2024 (lit. 24).", ['1.84', '02-17']),
    ('§ 2.4 (RIA)', "Date de l'annexe III rattachée au calendrier de la Commission (lit. 21), sous réserve de la relecture du règlement (UE) 2026/1744 au Journal officiel (lit. 22, A-26).", ['1.85', '02-18', 'A-26']),
    ('§ 3.4', "Art. 26, par. 2, du RIA cité avec sa date d'application; appel [61] ajouté à [94].", ['1.86', '03-26']),
    ('§ 5.5; § 6.1', "Abréviation « Loi sur le privé » définie à la première occurrence (§ 5.5) et retirée du § 6.1. Redéfinitions des ch. 8, 12, 13 et de l'annexe E : t3, t5, t6.", ['1.87', '05-23']),
    ('Tableau 10, ligne PRIN-06', "Contenu interdit dans la télémétrie de production (EXIG-OBS-07); capture de diagnostic bornée à 14 jours, hors des traces (A-18).", ['1.88', '03-27', 'A-18']),
    ('Avertissements; § 1.7', "Formule unique d'A-31 : état des sources au 27 octobre 2026, vérifications des 27 et 28 octobre. Non retenu dans t1 : la date de la version 1.0 à l'historique appartient à l'orchestrateur.", ['1.89', '01-14', '02-08', 'A-31']),
    ('Page de titre; § 1.1; historique', "Non retenu dans t1 : numéro de version, statut de la version et historique appartiennent à l'orchestrateur (A-31).", ['1.90', '01-15', 'A-31']),
    ('Sommaire, « Par où commencer »', "Trois jalons de passage plus trois jalons de suivi; « 18 mois environ (19 au calendrier du tableau 59) ». Les dates de J2a et de la migration MCP à l'historique relèvent de l'orchestrateur.", ['1.91', '01-16', 'A-26']),
    ('Historique 1.1; § 15.1', "Non retenu dans t1 : la fenêtre de validation E-23 figure à l'historique (orchestrateur) et au § 15.1 (t5); A-26 la reformule en inventaire.", ['1.92', '01-21', 'A-26']),
    ('§ 1.5', "« Huit annexes, de A à H », annexe H informative (A-31). Le chapeau de la table des matières est généré par la composition, hors des correctifs du corps.", ['1.93', '01-17', '02-20', 'A-31']),
    ('Figure 1', "Non retenu : figure non modifiable (libellés « Risques, conformité et approvisionnement », « E-23 », liste des annexes); la légende ne comporte pas ces libellés.", ['1.94', '01-18']),
    ('Tableau 4', "Rattachements OBS (10.1 à 10.3, OBS-07 à 10 étant au § 10.2), EVA (10.4) et FIN (10.5 et 10.6) corrigés (A-30). Le décompte de H.3 relève de t6.", ['1.95', '02-21', 'A-30']),
    ('Sommaire, décision 8; tableau 6; plan B (§ 5.3); PRIN-06', "« Inaltérable » devient « chaîné et ancré » (A-19). Figure 1 non modifiable.", ['1.96', '01-08', '02-28', 'A-19']),
    ('Sommaire, décisions 8 et 9', "« Étages E1 à E3 » et « jalons » du cycle de vie (A-27); les « points de contrôle » des EXIG-ARC-05 et 06 désignent des points de reprise et restent. Figure 3 non modifiable (« 3 paliers »); historique 0.2 : orchestrateur; EXIG-EVA-01 : t4.", ['1.97', '01-09', '03-21', '04-21', 'A-27']),
    ('§ 4.1 (À RETENIR); tableau 9', "EVA rattachée à PRIN-06 et PRIN-12, EVT à PRIN-02; exclusion de PRIN-07 des trois questions expliquée.", ['1.98', '03-16', '03-28']),
    ('§ 1.2; § 2.4; tableau 5; § 5.1, 5.3, 5.4, 5.5', "Renvoi du § 1.2 vers le § 2.1; « (sections 13.1 et 13.3) »; AAIF « au 27 octobre 2026 »; « la figure », « le tableau », « du tableau » rétablis au texte. La correction du gabarit qui produit ces renvois est hors des correctifs du corps.", ['1.99', '02-27', '02-29', '02-32', '04-22']),
    ('§ 1.4; § 1.6; § 3.1', "Arbitrage A-23 appliqué dans t1 (périmètre normatif, catalogue, rang 1, départage).", ['A-23']),
    ('§ 6.3; EXIG-INT-08, INT-09; § 2.2', "Arbitrage A-22 appliqué dans t1 : révision par l'architecture et approbation du comité, déclencheurs de révision extraordinaire, stades Experimental/Beta/Stable, retrait accéléré pour risque de sécurité actif (lit. 4).", ['A-22']),
    ('Tableau 15 (OAuth 2.1); EXIG-INT-09 (Pourquoi)', "Brouillon OAuth 2.1 cité à la révision épinglée au catalogue; -16 expirée de fait, remplacée par la -17 du 31 octobre 2026 (lit. 29, A-31).", ['A-31']),
    ('PRIN-10; EXIG-ARC-02; EXIG-INT-08', "« Propriétaire » employé seul pour un agent remplacé par « parrain » (A-34).", ['A-34']),
]

JOURNAL = [(a, T(b), k) for a, b, k in _J]
