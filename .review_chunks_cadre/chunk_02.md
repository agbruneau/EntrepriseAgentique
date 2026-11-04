# chunk_02 — pages PDF 11 à 22 (sur 283)



---
## [Page PDF 11]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
1 Objet, portée et mode d’emploi
Ce chapitre dit ce que le cadre règle, à quels systèmes il s’applique et à qui il s’adresse. Il explique comment 
lire une exigence, comment le document est organisé et comment il évolue. Il présente enfin la méthode qui 
a servi à l’établir et à vérifier ses faits.
1.1 Objet
Le cadre CRE-IA-2026-01 fixe les règles communes qui permettent aux agents d’IA de l’entreprise de se 
brancher aux systèmes, de collaborer entre eux et d’être orchestrés de façon sûre, traçable, réversible et 
économiquement maîtrisée, quel que soit le fournisseur. La présente version 1.1, datée du 28 octobre 2026, 
est soumise à l’approbation du comité d’architecture et des risques agentiques. Le cadre poursuit quatre 
objectifs :
• donner à toutes les équipes un vocabulaire commun (chapitre 3);
• fixer les protocoles retenus, les patrons d’orchestration autorisés et les niveaux d’autonomie permis 
(chapitres 5 à 8);
• encadrer l’identité, la sécurité, l’observabilité, les coûts, la gouvernance et la conformité des agents 
(chapitres 9 à 13);
• offrir une trajectoire de maturité mesurable et une grille d’homologation applicable à chaque projet 
(chapitres 14 et 15, annexe A).
Le cadre est normatif et neutre à l’égard des fournisseurs. Il règle ce qui doit rester sous le contrôle de 
l’entreprise, quelle que soit la plateforme : contrats d’interface, identités et délégations, passage obligé par la 
passerelle d’agents, traces et journal d’audit, registre, plafonds d’autonomie et de coûts. Il ne choisit aucun 
produit : ceux qu’il cite sont des exemples non limitatifs, à l’état du 27 octobre 2026. Il ne tient pas lieu d’avis 
juridique (chapitre 12).
1.2 Portée
Cette section délimite les systèmes visés. Le critère est fonctionnel : ce qui compte n’est pas l’étiquette 
commerciale d’un système, mais sa capacité à appeler des outils ou à agir sur des systèmes et des données 
de l’entreprise.
Tableau 1 — Portée du cadre
Catégorie
Dans la portée
Hors portée
Agents internes
Tout agent bâti à l’interne, en pilote ou en produc­
tion, qui lit ou modifie des systèmes ou des données 
de l’entreprise
Assistant conversationnel sans outil ni capacité 
d’action, régi par la politique d’usage de l’IA
Agents achetés
Agents intégrés aux logiciels-services (software as a 
service, SaaS) et aux progiciels, dès que l’entreprise 
ou une équipe métier les active
Fonction dite « agentique » qui n’appelle au­
cun outil et n’agit sur rien
Agents de tiers
Agents de partenaires, de fournisseurs ou de clients 
qui échangent avec les agents ou les systèmes de 
l’entreprise
Fonctionnement interne de ces agents : le 
cadre en régit les interfaces, les identités et les 
contrats
Outils et données
Serveurs MCP internes ou externes, outils, API, événe­
ments et sources de données exposés aux agents
Systèmes d’enregistrement eux-mêmes, que le 
cadre n’oblige pas à modifier
Plateformes
Plateformes et moteurs d’orchestration, passerelles 
d’agents et de modèles, registres et catalogues
Choix des fournisseurs de modèles, qui re­
lève de l’architecture d’entreprise et de 
l’approvisionnement
Modèles et automati­
sation
Usage des modèles par les agents; flux déterministe 
qui appelle un agent ou qui est appelé par lui
Entraînement et ajustement fin des modèles; 
automatisation robotisée des processus (RPA) 
sans composante agentique
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 11 sur 283


---
## [Page PDF 12]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
Trois règles tranchent les cas limites. Un assistant qui reçoit un premier outil, même en lecture seule, entre 
dans la portée dès ce moment. À l’inverse, une fonction qu’un éditeur qualifie d’agentique n’y entre que si 
elle appelle des outils ou agit : Gartner observait d’ailleurs, en juin 2025, que de nombreux produits existants 
étaient simplement rebaptisés « agentiques »[3]. En cas de doute, le système est traité comme visé et inscrit 
au registre (section 11.4).
1.3 Public cible et usages par rôle
Le cadre s’adresse à toutes les fonctions qui conçoivent, exploitent, financent ou contrôlent des agents. 
Personne n’a besoin de tout lire : le tableau 2 indique, pour chaque rôle, par où commencer.
Tableau 2 — Parcours de lecture par rôle
Rôle
À lire en priorité
Direction TI et comité d’architecture et des risques agentiques
Sommaire, chapitres 2, 4, 14 et 15
Architectes d’entreprise et de solutions
Chapitres 3 à 8, annexe A
Équipes de plateforme et d’intégration
Chapitres 5, 6, 9 et 10, annexe C
Équipes produit qui bâtissent des agents
Chapitres 3, 7, 8 et 10, annexes A à C
Sécurité de l’information
Chapitres 8 et 9, section 12.8
Risques, conformité, affaires juridiques et protection des rensei­
gnements personnels (RP)
Chapitres 11 et 12, section 8.8
FinOps
Sections 10.5 et 10.6, chapitre 13
Responsables métier, parrains d’agents
Sommaire, chapitres 3, 8 et 11, annexe B
Approvisionnement
Chapitre 13, section 6.3
Audit interne
Annexes A et D, sections 11.4 et 12.6
Appliquer le cadre à un projet
1. Vérifier la portée et inscrire le système au registre dès la conception (annexe B).
2. Classer le risque (section 12.1), fixer le niveau d’autonomie sous le plafond de la classe (section 8.1) et 
déterminer les évaluations d’impact requises (section 12.9).
3. Retenir l’option la plus simple qui suffit, puis le patron d’orchestration (section 7.3).
4. Choisir les protocoles (section 6.3) et publier les contrats au catalogue d’entreprise (section 6.8).
5. Appliquer les exigences pertinentes (annexe D); justifier par écrit tout écart à une recommandation 
(niveau DEVRAIT) et obtenir une dérogation pour tout écart à une obligation (niveau DOIT) (section 
11.6).
6. Remplir la grille d’homologation (annexe A) avant toute mise en production.
1.4 Force normative
Cette section explique comment lire une exigence. Le cadre emploie trois degrés d’obligation, inspirés des 
mots-clés de la RFC 2119 de l’Internet Engineering Task Force (IETF) et mis en évidence dans le texte.
Tableau 3 — Degrés d’obligation
Expression
Sens
Écart admis
doit, ne doit pas
Obligation
Aucun, sauf dérogation écrite approuvée par le comité (ou, pour un agent de 
classe faible, par l’architecture d’entreprise sur délégation du comité), limitée dans 
le temps et assortie de mesures compensatoires (section 11.6). Certaines obligations 
n’admettent aucune dérogation (section 4.3 et EXIG-GOV-17).
devrait, ne de­
vrait pas
Recommandation
Admis s’il est justifié par écrit dans la fiche d’agent ou la décision d’architecture; la 
revue d’architecture contrôle la justification.
peut
Option
Sans objet.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 12 sur 283


---
## [Page PDF 13]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
Chaque exigence occupe un bloc qui réunit un identifiant stable (par exemple EXIG-AUT-09), son degré 
d’obligation, un titre court, un énoncé vérifiable en revue d’architecture ou en test, et une justification 
introduite par « Pourquoi ». Seuls ces blocs d’exigences (chapitres 5 à 13), les principes directeurs PRIN-01 
à PRIN-12 (chapitre 4) et les tableaux auxquels une exigence renvoie expressément créent une obligation 
normative; le reste du texte, les exemples et les figures sont informatifs.
Exigence externe ou choix du cadre
Le cadre distingue toujours ce qui vient d’un texte externe de ce qu’il décide lui-même. « La spécification 
MCP exige » ou « selon l’article 14 du règlement (UE) 2024/1689 sur l’IA (RIA) » rapportent le contenu d’une 
norme ou d’une loi, vérifié à la source. « Le cadre fixe » ou « choix du cadre » signalent une décision interne, 
que le comité peut réviser. Exemple : Microsoft exige un plafond d’itérations pour la boucle producteur-
vérificateur, sans en fixer la valeur[9]; le plafond de trois itérations retenu au chapitre 7 est donc un choix 
du cadre. Le cadre n’attribue jamais à une norme une exigence qu’elle ne contient pas et présente ses seuils 
chiffrés (délais, plafonds, fréquences) comme les siens.
À RETENIR
Trois règles de lecture : un fait externe porte sa source et sa date; un chiffre de fournisseur est présenté 
comme une allégation de ce fournisseur; un produit cité est un exemple, jamais une exigence.
1.5 Structure du document et identifiants
Le document compte quinze chapitres en quatre parties : Fondements (chapitres 1 à 4); Architecture, inter­
opérabilité et orchestration (5 à 8); Confiance et exploitation (9 et 10); Gouvernance, conformité et mise en 
œuvre (11 à 15). Sept annexes, de A à G, fournissent les outils d’application, le glossaire et les références.
Les douze principes directeurs portent les identifiants PRIN-01 à PRIN-12. Chaque exigence porte un identi­
fiant de la forme EXIG-XXX-NN : un préfixe de trois caractères propre à un domaine, puis un numéro à deux 
chiffres, continu pour chaque préfixe. Les chapitres 1 à 4, 14 et 15 et les annexes ne créent pas d’exigences 
numérotées; l’annexe D récapitule toutes les exigences dans l’ordre du document. Choix du cadre : un 
identifiant n’est jamais réattribué, et une exigence retirée lors d’une révision conserve son numéro, marqué 
« retirée ». Le tableau 4 donne la liste des préfixes.
Tableau 4 — Identifiants des principes et préfixes des exigences
Identifiant ou préfixe
Domaine
Emplacement
PRIN-01 à PRIN-12
Principes directeurs
Chapitre 4
EXIG-ARC
Architecture de référence
Chapitre 5
EXIG-INT
Interopérabilité, contrats et catalogue d’entreprise
Sections 6.1 à 6.4, 6.8 et 6.9
EXIG-MCP
Model Context Protocol
Section 6.5
EXIG-A2A
Protocole Agent2Agent
Section 6.6
EXIG-EVT
Interopérabilité événementielle
Section 6.7
EXIG-ORC
Orchestration
Chapitre 7
EXIG-AUT
Autonomie et supervision humaine
Chapitre 8
EXIG-IAM
Confiance zéro, identité, délégation et passerelle d’agents
Sections 9.1 à 9.4
EXIG-SEC
Menaces propres aux agents et défenses
Sections 9.5 à 9.9
EXIG-OBS
Traçage et journal d’audit
Chapitre 10
EXIG-EVA
Évaluation continue
Chapitre 10
EXIG-FIN
Économie de l’inférence et maîtrise des coûts
Chapitre 10
EXIG-GOV
Gouvernance et cycle de vie
Chapitre 11
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 13 sur 283


---
## [Page PDF 14]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
Identifiant ou préfixe
Domaine
Emplacement
EXIG-CON
Risques, conformité et réglementation
Chapitre 12
EXIG-APP
Approvisionnement et clauses contractuelles
Chapitre 13
Un terme anglais figure entre parenthèses et en italique à sa première occurrence, comme transfert (handoff); 
les noms de protocoles, de champs et de méthodes restent en police à chasse fixe, comme tools/call. Les 
appels de citation renvoient à l’annexe G.
1.6 Relation avec les autres politiques et cycle de révision
Le cadre complète, sans les remplacer, les politiques de sécurité de l’information, de gouvernance des 
données, de protection des RP, d’usage de l’IA, de gestion des risques et d’approvisionnement. Celles-ci 
continuent de régir leur objet; le cadre en précise l’application aux agents. Choix du cadre : lorsqu’une règle 
du cadre et celle d’une autre politique visent le même objet, la plus stricte s’applique, et toute contradiction 
est soumise au comité. Le droit applicable et les engagements contractuels priment toujours (section 4.3).
Deux rythmes de révision coexistent, semestriel pour le cadre et trimestriel pour le catalogue; les versions 
applicables suivent celui du catalogue.
• Le cadre est révisé chaque semestre par le comité, à partir des dérogations accordées, des incidents, des 
résultats d’homologation et de la veille; une révision extraordinaire suit tout incident agentique grave 
ou changement réglementaire majeur. Une dérogation souvent renouvelée signale une règle à revoir.
• Le catalogue des protocoles et standards est révisé au moins chaque trimestre (section 6.3 et section 
11.7); un correctif de sécurité peut justifier une révision extraordinaire.
• Les versions applicables, comme MCP 2026-07-28 ou A2A 1.0, sont fixées au catalogue et non dans le 
texte : en cas d’écart, le catalogue fait foi.
Chaque révision porte un numéro de version et une date, et s’accompagne d’un relevé des modifications. 
La mise en conformité des agents déjà en service suit les phases et les jalons du chapitre 15.
1.7 Méthode d’élaboration
La version 1.0 consolide quatre ébauches : une recherche documentaire appuyée sur 121 références, deux 
versions de travail successives du cadre et une version structurée en exigences. Elle suit la structure de la 
version de travail la plus récente, y intègre les exigences des autres ébauches et les réécrit pour qu’elles 
soient vérifiables. Chaque fait a ensuite été vérifié, aux 27 et 28 octobre 2026, contre des sources primaires 
ou, à défaut, secondaires reconnues, en trois passes :
1. la validation, une à une, des 121 références : chaque affirmation qui en citait une a été confrontée à la 
source (427 liens au total), au contenu réel de la page lorsqu’elle était accessible (108 références sur 121) 
et, sinon, à des sources équivalentes, faute de quoi elle a été déclarée invérifiable;
2. onze vérifications thématiques, de MCP au droit québécois, qui ont confronté les ébauches aux textes 
primaires et recueilli des faits complémentaires;
3. un audit final de cohérence interne, factuelle et juridique de l’ensemble des chapitres et des références 
citées.
Les sources sont classées en trois catégories : A, primaires ou officielles; B, secondaires reconnues; C, blogues 
de positionnement ou agrégateurs. Seules les catégories A et B sont citées. Un fait réfuté ou invérifiable 
a été corrigé, retiré ou, lorsqu’il exprimait une décision utile, conservé comme choix du cadre et signalé 
comme tel.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 14 sur 283


---
## [Page PDF 15]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
La vérification a deux limites. Elle reflète l’état des textes aux 27 et 28 octobre 2026, alors que plusieurs 
standards évoluent d’un trimestre à l’autre. Certains textes payants, comme les normes ISO/IEC, ont été 
vérifiés par leur fiche de catalogue et des sources secondaires concordantes; le cadre évite donc de les citer 
textuellement. L’annexe F détaille la méthode, le bilan et les corrections.
2 Contexte et enjeux
Les agents d’IA se multiplient plus vite que les règles qui les relient entre eux et aux systèmes de l’entreprise. 
Ce chapitre dresse l’état des lieux au 27 octobre 2026 à partir de données datées et attribuées, retrace la 
consolidation des standards ouverts depuis 2024 et nomme les huit enjeux qui motivent le cadre. Il explique 
enfin pourquoi agir maintenant : les protocoles se sont stabilisés, mais la gouvernance de chaque plateforme 
s’arrête à sa propre frontière.
2.1 Où en est l’entreprise agentique en 2026
Cette section situe le cadre dans les faits. L’entreprise agentique désigne ici une organisation où des agents 
exécutent une part croissante des processus, aux côtés des personnes et des systèmes existants, sous une 
supervision humaine proportionnée au risque. Les chiffres qui suivent donnent des ordres de grandeur; ils 
ne remplacent pas les mesures que chaque organisation tire de son propre registre.
40 %
des applications d’entreprise intégreront des agents spécialisés par tâche d’ici la fin de 2026, contre moins 
de 5 % en 2025 (prévision Gartner, août 2025)
[1]
> 40 %
des projets d’IA agentique seront annulés d’ici la fin de 2027 (prévision Gartner, juin 2025)
[3]
98 %
des répondants FinOps gèrent désormais des dépenses d’IA, contre 31 % en 2024 (State of FinOps 2026)
[10]
82 : 1
identités machines par identité humaine, selon une enquête de fournisseur (CyberArk, avril 2025)
[11]
Une adoption large, une industrialisation encore rare
Les prévisions des analystes décrivent une diffusion rapide. Gartner prévoit que 40 % des applications 
d’entreprise intégreront des agents spécialisés d’ici la fin de 2026 et que l’IA agentique pourrait représenter 
environ 30 % des revenus des logiciels d’application d’entreprise d’ici 2035[1]. Le même cabinet anticipe 
qu’en 2028, au moins 15 % des décisions de travail quotidiennes seront prises de façon autonome par l’IA 
agentique, contre 0 % en 2024[3].
Les enquêtes montrent toutefois un écart entre l’expérimentation et la production. Selon l’édition 2025 de 
l’enquête de McKinsey (novembre 2025; dernière édition dont les résultats détaillés sont publiés à cette 
adresse), 88 % des répondants disent que leur organisation utilise régulièrement l’IA dans au moins une 
fonction, mais seulement 39 % déclarent un effet sur le bénéfice avant intérêts et impôts (BAII) à l’échelle de 
l’entreprise. Si 62 % des organisations au moins expérimentent des agents, 23 % seulement disent déployer 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 15 sur 283


---
## [Page PDF 16]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
à l’échelle un système agentique quelque part dans l’entreprise; dans une fonction d’affaires donnée, cette 
part ne dépasse pas 10 %[12].
Les plateformes et les protocoles, eux, sont déjà largement diffusés. En mai 2025, Microsoft indiquait que 
plus de 230 000 organisations, dont 90 % du Fortune 500, avaient déjà utilisé Copilot Studio; il s’agit d’un 
usage cumulatif, non d’un nombre de déploiements actifs[13]. En décembre 2025, le Model Context Protocol 
(MCP) comptait 10 000 serveurs actifs et plus de 97 millions de téléchargements mensuels de ses trousses 
de développement[14]. En avril 2026, le protocole Agent2Agent (A2A) réunissait plus de 150 organisations 
et était intégré à Azure AI Foundry, à Copilot Studio et à Amazon Bedrock AgentCore[15]. Côté dépenses, 
Menlo Ventures estime, selon un sondage auprès d’entreprises américaines, que les entreprises ont consacré 
37 G$ US à l’IA générative en 2025, soit 3,2 fois plus que les 11,5 G$ US estimés pour 2024 (estimation hors 
inférence)[16].
Des échecs annoncés et une pression sur les coûts
Gartner prévoit que plus de 40 % des projets d’IA agentique seront annulés d’ici la fin de 2027 en raison 
de coûts croissants, d’une valeur d’affaires incertaine ou de contrôles des risques inadéquats. Le cabinet 
dénonce aussi l’étiquetage agentique abusif (agent washing), soit des produits existants rebaptisés « agen­
tiques » : seuls quelque 130 des milliers de fournisseurs qui se disent agentiques le seraient réellement[3].
La pression financière est déjà visible. Selon le rapport State of FinOps 2026 (1 192 répondants), 98 % des 
répondants FinOps gèrent des dépenses d’IA, contre 63 % en 2025 et 31 % en 2024, et la gestion des coûts 
de l’IA est la première compétence à développer[10]. La forme même du système pèse sur la facture : selon 
Anthropic, un agent consomme environ 4 fois plus de jetons qu’une conversation, et un système multiagent 
environ 15 fois plus[17]. Le choix du patron d’orchestration est donc aussi une décision économique (section 
7.1 et section 10.5).
Une surface de risque qui s’élargit
Selon IBM et le Ponemon Institute (juillet 2025), 13 % des organisations ont déclaré une violation touchant 
un modèle ou une application d’IA; parmi elles, 97 % n’avaient pas de contrôles d’accès propres à l’IA. Les 
organisations où l’IA fantôme (shadow AI) est répandue ont payé en moyenne 670 000 $ US de plus par 
violation, et une organisation sur cinq a subi une violation attribuable à cette IA non gouvernée[18]. L’édition 
2026 établit le coût moyen mondial d’une violation à 4,99 M$ US (hausse de 12 %) et recommande, pour les 
agents, des contrôles d’accès dynamiques fondés sur l’identité et appliqués en continu à l’exécution[19].
Les identités non humaines dépassent déjà largement les identités humaines. Dans l’enquête 2025 de 
CyberArk (2 600 décideurs de 20 pays, dont le Canada; dernière édition dont ce ratio est publiquement 
vérifié), on compte 82 identités non humaines (« identités machines » selon CyberArk) par identité humaine; 
68 % des répondants déclarent que leur organisation manque de contrôles de sécurité des identités pour 
l’IA[11]. Face à la prolifération des agents, Gartner (avril 2026) recommande six mesures, dont un inventaire 
centralisé qui inclut les agents fantômes, et observe que bloquer les agents pousse les employés vers l’IA 
fantôme[2].
ATTENTION
Les chiffres de Gartner sont des prévisions; ceux de McKinsey, de la FinOps Foundation, d’IBM 
et de Menlo Ventures proviennent d’enquêtes ou d’estimations; ceux de CyberArk, de Microsoft et 
d’Anthropic sont des données de fournisseurs. Le cadre n’en tire aucune exigence chiffrée. Il exige plutôt 
que chaque organisation mesure ses propres valeurs (agents inscrits, identités non humaines, coût par 
tâche réussie) à partir de son registre et de sa télémétrie (section 10.6, section 11.4 et chapitre 15).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 16 sur 283


---
## [Page PDF 17]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
2.2 La consolidation des standards ouverts
En deux ans, les échanges entre agents et outils, puis entre agents, sont passés de protocoles lancés par des 
éditeurs à des projets sous gouvernance neutre. Le tableau 5 retrace les jalons vérifiés qui fondent les choix 
du catalogue des protocoles (section 6.3).
Tableau 5 — Chronologie vérifiée de la consolidation des standards agentiques (novembre 2024 à octobre 2026)
Date
Jalon
Portée pour l’entreprise
25 nov. 2024
Anthropic annonce le Model Context Protocol (MCP), norme 
ouverte de raccordement des agents aux outils et aux don­
nées[20]
Naissance du standard vertical agent 
→ outil
9 avr. 2025
Google annonce le protocole Agent2Agent (A2A) avec plus de 
50 partenaires[21]
Premier protocole agent → agent lar­
gement appuyé
23 juin 2025
A2A est confié à la Linux Foundation; plus de 100 entreprises 
l’appuient[22]
Gouvernance neutre de l’axe horizon­
tal
29 juill. 2025
La Linux Foundation accueille AGNTCY, lancé par Cisco en 
mars 2025 avec LangChain et Galileo[23]
Briques de découverte, d’identité et de 
messagerie, hors de l’Agentic AI Foun­
dation (AAIF)
Août 2025
L’Agent Communication Protocol (ACP) d’IBM fusionne dans 
A2A[24]
Un protocole concurrent de moins 
entre agents
8 sept. 2025
Lancement du registre officiel MCP en préversion[25]
Découverte publique; les serveurs pri­
vés restent à la charge de l’entreprise
Sept. 2025
Google publie l’Agent Payments Protocol (AP2, 16 sep­
tembre); OpenAI et Stripe publient l’Agentic Commerce Proto­
col (29 septembre)[26, 27]
Le commerce agentique démarre en 
ordre dispersé
9 déc. 2025
La Linux Foundation crée l’Agentic AI Foundation (AAIF), 
cofondée par Anthropic, Block et OpenAI; MCP, goose et 
AGENTS.md en sont les projets fondateurs[4]. Le même jour, 
l’Open Worldwide Application Security Project (OWASP) pu­
blie son Top 10 des applications agentiques[28]
MCP passe sous gouvernance neutre; 
un référentiel commun des menaces 
apparaît
12 mars 2026
Publication d’A2A 1.0.0, première version stable; correctif 1.0.1 
le 28 mai 2026[29, 30]
Base contractuelle stable pour les 
cartes d’agent
4 juin 2026
agentgateway (créé par Solo.io, à la Linux Foundation depuis 
août 2025) devient un projet de l’AAIF[31, 32]
Passerelle ouverte pour MCP, A2A et 
les modèles
28 juill. 2026
Publication de la révision MCP 2026-07-28 : protocole sans 
état et cycle de vie formel des fonctionnalités[33, 34]
Exploitation à grande échelle; dépré­
ciations à planifier
17 août 2026
A2A est annoncé comme projet de l’AAIF au stade « Growth » 
(approbation du conseil d’administration le 4 août)[5, 35]
MCP et A2A relèvent de la même fon­
dation
9 sept. 2026
Envoy AI Gateway, renommé Agent Router, rejoint l’AAIF[36]
Autre option ouverte de passerelle de 
modèles et d’outils
12 oct. 2026
Cisco propose AGNTCY à l’AAIF (proposition no 57, sans déci­
sion au 27 octobre 2026) [37]
AGNTCY reste un projet de la Linux 
Foundation, candidat à l’AAIF
22 oct. 2026
L’AAIF annonce quatre nouveaux projets et en héberge désor­
mais dix[38]
Écosystème en expansion, à suivre 
chaque trimestre
Ce que la consolidation règle
Les deux axes principaux d’interaction relèvent désormais d’une même fondation neutre. Le guide officiel 
d’A2A les distingue clairement : MCP relie un agent à des outils et à des ressources dont les entrées et 
les sorties sont définies, souvent sans état; A2A relie des agents autonomes, potentiellement opaques, qui 
raisonnent et conservent un état au fil d’échanges à plusieurs tours[39]. Les règles d’évolution deviennent 
aussi prévisibles : depuis la révision 2026-07-28, une fonctionnalité MCP dépréciée reste dans la spécification 
au moins douze mois avant de pouvoir être retirée, sauf retrait accéléré exceptionnel d’au moins 90 jours[34]. 
Pour l’entreprise, le choix d’un protocole n’est plus un pari sur un éditeur.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 17 sur 283


---
## [Page PDF 18]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
Ce qu’elle ne règle pas
La convergence reste partielle. AGNTCY n’est pas un projet de l’AAIF, et le commerce agentique demeure 
fragmenté entre l’Agentic Commerce Protocol d’OpenAI et de Stripe, AP2, confié à la FIDO Alliance, et 
l’Universal Commerce Protocol (UCP), porté par Google et des détaillants; l’AAIF a d’ailleurs ouvert un 
groupe de travail sur le commerce agentique[40, 41]. L’admission à l’AAIF suit un processus formel : un projet 
n’est officiel qu’une fois son admission approuvée et annoncée[42]. Enfin, le registre officiel MCP demeure 
en préversion, ne prend pas en charge les serveurs privés et recommande aux entreprises d’héberger leur 
propre registre MCP privé[43]. Le catalogue d’entreprise reste donc une responsabilité interne (section 6.8 et 
section 11.4); la veille sur les protocoles émergents est traitée à la section 6.9.
À RETENIR
Les protocoles disent comment les agents se parlent. Ils ne disent ni qui a le droit d’agir, ni ce qui doit 
être journalisé, ni combien une tâche peut coûter. Ces règles relèvent de l’entreprise : c’est l’objet du 
présent cadre.
2.3 Huit enjeux qui motivent le cadre
Sans règles communes, chaque équipe recrée ses connecteurs, ses accès et ses contrôles, et l’entreprise perd 
la vue d’ensemble. Le premier enjeu, la prolifération des intégrations, est le plus visible; la figure 2 l’illustre.
Sans cadre commun
Chaque agent a ses connecteurs : N × M intégrations
Agent RH
Agent ventes
Agent TI
Agent finance
ERP
CRM
GED
Entrepôt
SaaS
4 × 5 = 20 connecteurs propriétaires
Avec le cadre
Protocoles communs et catalogue : N + M contrats
Agent RH
Agent ventes
Agent TI
Agent finance
Passerelle
et catalogue
MCP · A2A
MCP · ERP
MCP · CRM
MCP · GED
MCP · Entrepôt
MCP · SaaS
4 + 5 = 9 contrats réutilisables, une politique
Figure 2 — Du maillage N × M aux contrats communs N + M. À gauche, chaque agent possède ses propres connecteurs vers 
chaque système : quatre agents et cinq systèmes exigent vingt intégrations, chacune avec sa sécurité. À droite, chaque agent et chaque 
système publient un seul contrat derrière la passerelle et le catalogue : neuf contrats réutilisables, soumis à une politique unique. 
Source : élaboration du cadre CRE-IA-2026-01; exemple illustratif.
Anthropic présente MCP comme un protocole unique qui remplace des connecteurs sur mesure et fragmen­
tés[20]; l’expression « N × M » est une vulgarisation de ce bénéfice, non un énoncé de la spécification. Le calcul 
illustre l’ordre de grandeur : 50 agents et 200 systèmes représentent 10 000 intégrations potentielles, contre 
250 contrats. Le gain n’existe toutefois que si le catalogue est unique; des catalogues multiples recréent le 
maillage au niveau de la gouvernance. Le tableau 6 présente les huit enjeux et la réponse que le cadre leur 
apporte.
Tableau 6 — Huit enjeux, leurs symptômes et la réponse du cadre
Enjeu
Symptôme sans cadre
Réponse du cadre
1. Prolifération des 
intégrations
N agents × M systèmes = N × M connecteurs 
propriétaires à maintenir et à sécuriser
Protocoles communs et catalogue d’entreprise 
unique (PRIN-01, PRIN-02; section 6.3 et section 6.8)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 18 sur 283


---
## [Page PDF 19]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
Enjeu
Symptôme sans cadre
Réponse du cadre
2. Logique métier 
confiée au mo­
dèle
Routage, calculs et règles d’affaires laissés au 
raisonnement probabiliste : dérives, boucles, ré­
sultats non reproductibles
Flux déterministe autour du modèle et patron le plus 
simple qui suffit (PRIN-08; chapitre 7)
3. Silos d’agents
Les agents de plateformes différentes ne peuvent 
pas se déléguer de tâches; les mêmes capacités 
sont bâties plusieurs fois
Carte d’agent, protocole A2A et catalogue 
d’entreprise comme source de découverte (section 
6.6 et section 6.8)
4. Accès excessifs 
et identités non 
humaines
Comptes de service partagés, clés d’API statiques, 
droits larges et permanents; impossible de savoir 
quel agent a agi
Identité propre à chaque agent, délégation par jeton, 
moindre privilège et moindre agence (PRIN-03; cha­
pitre 9)
5. Décisions non 
traçables
Impossible d’expliquer une action ou de remon­
ter la chaîne mandant → agent → outil
Traçage de bout en bout et journal d’audit inalté­
rable (PRIN-06; section 10.1 et section 10.3)
6. Effets non maîtri­
sés et coûts
Boucles, actions irréversibles sans approbation, 
factures d’inférence imprévisibles
Niveaux d’autonomie N0 à N4, paliers d’outils 
P0 à P3, compensation et enveloppes budgétaires 
(PRIN-04, PRIN-05; chapitre 8 et section 10.6)
7. Agents fantômes
Agents créés hors inventaire, sans propriétaire 
nommé ni moyen de révocation
Registre obligatoire, aucun jeton de production sans 
fiche complète et à jour, cycle de vie contrôlé (cha­
pitre 11)
8. Obligations lé­
gales
Renseignements personnels (RP) traités sans éva­
luation; décisions automatisées non divulguées; 
incidents impossibles à reconstituer
Évaluation des facteurs relatifs à la vie privée (EFVP), 
transparence, droit à la révision et gestion des inci­
dents (chapitre 12)
Ces enjeux se présentent rarement isolément. Prenons un agent créé dans une plateforme SaaS par une 
équipe métier, hors inventaire, qui utilise un compte de service partagé pour mettre à jour un système 
financier sans approbation humaine et sans laisser de trace exploitable. À lui seul, il réunit les enjeux 4, 5, 
6 et 7. C’est pourquoi le cadre traite ensemble l’identité, la passerelle, le registre et le traçage, plutôt que 
comme des chantiers séparés.
2.4 Pourquoi un cadre commun maintenant
Trois évolutions convergent en 2026 et rendent un cadre commun à la fois possible et nécessaire.
La gouvernance native s’arrête à la frontière de chaque plateforme
Des éditeurs de passerelles soutiennent que la gouvernance native d’une plateforme ne se transfère pas aux 
autres : selon TrueFoundry, une règle de prévention des fuites de données d’un écosystème ne s’applique 
pas à l’agent d’un autre; selon MuleSoft, la gouvernance native d’un nuage devient insuffisante dès que 
plusieurs environnements d’exécution coexistent[44, 45]. Ces fournisseurs ont un intérêt commercial dans la 
thèse; il s’agit d’un argument d’architecture, non d’un constat mesuré. Les faits publiés vont néanmoins 
dans le même sens. Microsoft Agent 365, en disponibilité générale depuis le 1er mai 2026, offre un registre 
et des contrôles comme le blocage des agents non gérés, mais sa synchronisation avec Amazon Bedrock 
et Google Cloud est en préversion et les actions de cycle de vie sur les agents infonuagiques de tiers sont 
seulement annoncées[46]. ServiceNow a annoncé le 5 mai 2026 l’extension de son AI Control Tower pour 
découvrir et gouverner l’IA déployée dans n’importe quel système[47]. Chaque éditeur propose son plan de 
contrôle; une entreprise qui exploite plusieurs plateformes en aura plusieurs, et la couverture de l’ensemble 
de ses agents par un seul d’entre eux reste à démontrer.
Exemple concret : un agent de Copilot Studio délègue par A2A une vérification à un agent Agentforce, qui 
met à jour un dossier dans ServiceNow par MCP. Les trois plateformes prennent en charge ces protocoles 
(pour ServiceNow, un serveur MCP en disponibilité générale, ainsi que A2A et MCP par l’AI Agent Fabric)
[48, 49, 50, 51], mais la demande traverse trois registres, trois moteurs de politiques et trois journaux. Le 
mandant, l’identifiant de trace et les plafonds de la tâche doivent pourtant la suivre de bout en bout. Gartner 
recommande en ce sens une structure unifiée en couches qui combine gestion, orchestration et application 
des politiques, capable d’arrêter rapidement un agent qui dérape (résumé public, août 2026)[52]. Le cadre 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 19 sur 283


---
## [Page PDF 20]

CRE-IA-2026-01 · Cadre de référence
2 Contexte et enjeux
place ce point de contrôle neutre au niveau du transport : passerelle d’agents, identité et registre (chapitre 
5 et section 9.4).
Le risque de verrouillage s’est déplacé des protocoles vers les plateformes
Avec MCP et A2A sous gouvernance neutre, le risque ne tient plus au choix du protocole, mais à ce que les 
plateformes conservent : extensions propriétaires, définitions d’orchestration, mémoires, identités et unités 
de facturation. Depuis juillet 2026, par exemple, Copilot Studio crée automatiquement une identité Microsoft 
Entra Agent ID pour chaque nouvel agent, sans possibilité de désactivation au niveau de l’environnement[48]. 
Chaque éditeur a aussi ses propres unités : les crédits Copilot, qui servent à facturer l’usage, chez Microsoft; 
chez Salesforce, les crédits Flex, qui servent à facturer l’usage, et les « Agentic Work Units », qui mesurent 
l’activité agentique livrée sans être une unité de facturation[53, 54, 55]. Le cadre exige donc que l’entreprise 
garde la propriété de sa logique d’orchestration, de ses contrats d’outils et de sa mémoire (PRIN-09), et 
qu’elle l’inscrive dans ses contrats d’approvisionnement (section 13.3 et section 13.1).
Les obligations se précisent
Le contexte réglementaire ne laisse plus de place à l’improvisation. La Loi 25 (L.Q. 2021, c. 25) est en vigueur 
pour l’essentiel depuis le 22 septembre 2024, date de sa dernière étape majeure, le droit à la portabilité. 
Depuis le 22 septembre 2023, elle exige, dans les cas prévus, l’évaluation des facteurs relatifs à la vie privée 
(EFVP) et encadre les décisions fondées exclusivement sur un traitement automatisé[7, 56]. Le règlement 
(UE) 2024/1689 sur l’intelligence artificielle (RIA) s’applique de façon générale depuis le 2 août 2026 aux 
organisations qui relèvent de son champ d’application (art. 2), y compris hors de l’Union lorsque les sorties 
d’un système y sont utilisées, et le règlement (UE) 2026/1744 fixe au 2 décembre 2027 l’application aux 
systèmes à haut risque de l’annexe III[57, 58]. Au fédéral, la ligne directrice E-23 du Bureau du surintendant des 
institutions financières (BSIF), en vigueur le 1er mai 2027 pour les institutions financières fédérales, attend 
un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs[8]. Pour y 
répondre, une organisation a besoin d’un inventaire, d’une classification des risques et de traces conservées 
au moment des faits, faute de pouvoir les reconstituer après coup (chapitre 12).
À RETENIR
Le cadre ne choisit pas de plateforme. Il fixe ce qui reste sous le contrôle de l’entreprise, quelle que 
soit la plateforme : contrats, identités, passerelle, traces, registre et budgets. Ces règles s’imposent plus 
facilement à quelques dizaines d’agents qu’à des milliers : c’est maintenant qu’il faut les poser.
3 Concepts et définitions
« Agent », « orchestrateur » ou « autonomie » ne désignent pas la même chose d’une équipe ou d’un 
fournisseur à l’autre. Ce chapitre fixe le sens des termes employés dans tout le cadre, distingue les flux de 
travail des agents et les agents interactifs des agents ambiants, puis précise ce qu’un agent n’est pas. Le 
glossaire de l’annexe E complète ces définitions.
3.1 Définitions normatives
Les définitions du tableau 7 font foi dans tout le cadre et dans les documents qui s’y rattachent. Lorsqu’une 
norme ou une loi définit déjà un terme, le cadre reprend sa définition et la précise au besoin.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 20 sur 283


---
## [Page PDF 21]

CRE-IA-2026-01 · Cadre de référence
3 Concepts et définitions
Tableau 7 — Définitions normatives du cadre
Terme
Définition
Référence
Agent
Selon ISO/IEC 22989, entité automatisée qui perçoit son environnement, 
y réagit et agit pour atteindre ses buts. Pour le cadre, système logiciel 
qui poursuit un objectif en dirigeant lui-même sa boucle « raisonner, agir, 
observer » au moyen d’un modèle, d’outils et d’un état, sous un niveau 
d’autonomie déclaré.
ISO/IEC 22989:2022; 
oneM2M TR-0081, v0.2.0 
(version préliminaire)[59, 60]; 
cadre
Système d’IA
Système automatisé conçu pour fonctionner à différents niveaux 
d’autonomie, qui peut faire preuve d’une capacité d’adaptation après son 
déploiement et qui, pour des objectifs explicites ou implicites, déduit, 
à partir des entrées qu’il reçoit, la manière de générer des sorties 
(prédictions, contenus, recommandations, décisions) pouvant influencer 
des environnements physiques ou virtuels. Le cadre considère tout agent 
comme un système d’IA.
Règlement (UE) 2024/1689 
(RIA), art. 3(1)[61, 62]
Déployeur
Personne ou organisme qui utilise un système d’IA sous sa propre auto­
rité. Si le RIA s’applique à elle (art. 2), l’entreprise l’est pour les agents 
qu’elle exploite, y compris ceux qu’elle achète (section 12.4).
RIA, art. 3(4)[61]
Outil
Capacité exposée à un agent (fonction, API, action), décrite par un contrat 
typé et classée P0 à P3 au catalogue; un outil ne prend aucune décision. 
Dans MCP, fonction exécutable que le modèle choisit d’appeler.
MCP[63]; cadre
Ressource
Donnée contextuelle identifiée par une URI, qu’un serveur met à la dispo­
sition d’un agent. Pour le cadre, sa lecture n’a aucun effet de bord; toute 
opération qui modifie un état est un outil.
MCP[63, 64]; cadre
Invite (prompt)
Instructions et contenu en langage naturel fournis à un modèle. Dans 
MCP, la primitive Prompts désigne des gabarits d’invite réutilisables 
qu’expose un serveur.
MCP[63]
Flux déterministe
Suite d’étapes dont le code fixe le chemin (graphe ou machine à états). 
Quand certaines étapes appellent un modèle, c’est un flux de travail assis­
té par IA : le chemin reste fixé par le code.
Anthropic (workflows)[65]
Orchestrateur, exé­
cutant
L’orchestrateur décompose une demande, affecte les sous-tâches, suit 
l’état, gère la reprise et consolide les résultats; l’exécutant, agent ou outil, 
traite une sous-tâche bornée. Le cadre limite la délégation à deux niveaux 
(choix du cadre, EXIG-ORC-04, section 7.2).
Cadre; Anthropic[65]
Transfert (handoff)
Cession explicite du contrôle d’une session, avec le contexte utile et 
le mandant, d’un agent source à un agent cible mieux qualifié; l’agent 
source se retire.
OpenAI[66]
Chorégraphie
Coordination sans composant central : chaque agent réagit aux événe­
ments d’un bus et publie les siens, ce qui complique le suivi et expose aux 
cycles.
Microsoft[67]
Carte d’agent (Agent 
Card)
Document lisible par machine, défini par A2A, par lequel un agent décrit 
son identité, ses interfaces, ses compétences et ses exigences de sécurité; 
en A2A 1.0, il est publié à /.well-known/agent-card.json.
A2A 1.0[68]
Contrat d’agent
Engagement formel d’un agent : carte d’agent, entrées et sorties typées, 
niveau d’autonomie, limites, niveaux de service et voie d’escalade. Outils 
et événements ont leurs équivalents; tout contrat est versionné au cata­
logue d’entreprise.
Cadre (EXIG-INT-03, sec­
tion 6.1; section 6.8)
Mandant
Personne, application ou agent au nom duquel une tâche est exécutée. 
Ses droits bornent ceux de l’agent, et son identité accompagne chaque 
appel de bout en bout.
Cadre
Délégation
Attribution à un agent de droits bornés en portée et en durée pour 
agir au nom d’un mandant, l’agent restant identifiable. Le cadre interdit 
l’usurpation, où l’agent devient indiscernable du mandant. Par extension, 
envoi d’une tâche à un autre agent, sans plus de droits que n’en a le 
mandant.
RFC 8693, § 1.1[69]; cadre
Jeton délégué
Jeton d’accès de courte durée, obtenu par échange de jetons, qui identi­
fie le mandant (sub) et l’agent acteur (act) et ne vaut que pour un seul 
service; sa portée ne s’élargit jamais d’un saut à l’autre.
RFC 8693, 8707 et 9068[70, 
71, 72]; cadre (durée courte, 
audience unique, portée ja­
mais élargie)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 21 sur 283


---
## [Page PDF 22]

CRE-IA-2026-01 · Cadre de référence
3 Concepts et définitions
Terme
Définition
Référence
Passerelle d’agents
Point d’application des politiques placé devant les outils et les agents : 
authentification, autorisation, garde-fous, plafonds, injection des secrets 
et journalisation de chaque appel.
Cadre; NIST SP 800-207[73]
Passerelle de mo­
dèles
Passage obligatoire entre les agents et les fournisseurs de modèles : clés, 
routage, cache, repli, quotas, mesure des jetons et filtrage des données 
sortantes.
Cadre (section 5.2)
Catalogue 
d’entreprise
Source unique des contrats des interfaces joignables (outils, cartes 
d’agent, événements), avec version et empreinte approuvées, palier et 
propriétaire. À distinguer du catalogue des protocoles (section 6.3).
Cadre (section 6.8)
Registre
Inventaire faisant autorité des agents et des serveurs MCP : une fiche 
par élément, avec propriétaire nommé, finalité, classe de risque, niveau 
d’autonomie et état de cycle de vie.
Cadre (section 11.4); GO­
VERN 1.6[74]
Garde-fou
Contrôle automatisé qui filtre ou bloque une entrée, une sortie ou 
une action d’un agent. Un garde-fou probabiliste réduit un risque sans 
l’éliminer.
Microsoft[9]; cadre
Humain dans la 
boucle (HITL), sur la 
boucle (HOTL), hors 
de la boucle (human 
in the loop, human on 
the loop, human out 
of the loop)
HITL : une personne approuve chaque action en écriture avant son exécu­
tion. HOTL : elle supervise, traite les exceptions et peut interrompre, sans 
approbation préalable. Hors de la boucle : aucune intervention pendant 
l’exécution; restent la surveillance automatisée, l’audit et l’arrêt.
AWS; IMDA (Infocomm 
Media Development Au­
thority, Singapour), section 
1.1.3, pour la gradation de 
l’implication humaine, les 
sigles HITL et HOTL n’y fi­
gurant pas[75, 76]
Niveau d’autonomie
Plafond, déclaré au registre, de ce qu’un agent fait sans approbation 
humaine : N0 à N4, NX étant interdit (définitions ci-dessous).
Cadre (section 8.1)
Palier d’outil
Risque propre à un outil, de P0 à P3, attribué au catalogue après revue et 
jamais déduit des déclarations du serveur (définitions ci-dessous).
Cadre (section 8.3)
Compensation
Action métier qui neutralise l’effet d’une étape déjà exécutée quand un 
flux échoue, par exemple un remboursement. Elle ne rétablit pas forcé­
ment l’état initial et doit pouvoir être réessayée sans danger.
Microsoft[77]
Idempotence
Propriété d’une opération dont la répétition produit le même effet qu’une 
seule exécution. Une clé d’idempotence, identique à chaque nouvel essai, 
permet de reconnaître une requête déjà reçue.
IETF; Temporal[78, 79]
Exécution durable
Persistance de l’état d’une exécution à chaque transition (point de 
contrôle), qui permet de reprendre après une panne ou un déploiement. 
Elle n’empêche pas à elle seule qu’un effet soit rejoué : il faut aussi 
l’idempotence.
Temporal; LangGraph[80, 81, 
82]
Les deux échelles du cadre
Ces échelles s’appliquent partout; le chapitre 8 en précise les contrôles.
Niveaux d’autonomie
• N0 Automatisation déterministe : aucun modèle; flux codé, règles, RPA, API (repère de base hors 
portée agentique, section 1.2).
• N1 Consultatif : l’agent lit, analyse, recommande, rédige; aucun effet en écriture; l’humain exécute; 
outils P0 et P1 seulement.
• N2 Exécution approuvée : l’agent prépare; chaque action en écriture attend une approbation explicite 
(humain dans la boucle).
• N3 Autonomie bornée et supervisée : l’agent exécute seul les actions P2 réversibles ou compensables 
sous des seuils déclarés, dans un domaine de conception opérationnel documenté (ODD, operational 
design domain); il escalade les exceptions; une action P3 exige une approbation hors bande (humain sur 
la boucle).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 22 sur 283
