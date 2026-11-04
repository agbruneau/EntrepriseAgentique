# chunk_05 — pages PDF 41 à 52 (sur 283)



---
## [Page PDF 41]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Couche
ABB
Capacités exigées
Exemples de SBB (non limitatifs, état au 
27 octobre 2026)
5. Outils et données
Serveurs MCP de domaine 
et adaptateurs
Outils conçus pour la 
tâche, effets déclarés, 
filtrage selon le man­
dant
Conversion d’API en outils par AgentCore 
Gateway, Azure API Management ou IBM 
ContextForge; serveur MCP Action Fabric 
de ServiceNow[50]
5. Outils et données
Index et graphes de 
connaissances
Recherche hybride avec 
citations, provenance, 
validité temporelle
GraphRAG (génération augmentée par ré­
cupération sur graphe); Zep et Graphiti 
(section 5.5)
6. Systèmes 
d’enregistrement
Systèmes existants
Contrôles métier 
conservés; corrélation 
des écritures
Aucun nouveau SBB : seuls des adapta­
teurs s’ajoutent
Plan A
Identité de charge de tra­
vail; serveur d’autorisation; 
moteur de politiques; 
coffre de secrets
Identité par agent, je­
tons délégués, décision 
par appel
SPIFFE/SPIRE; Microsoft Entra Agent ID[90]; 
AgentCore Identity et AgentCore Policy 
(langage de règles compatible avec Cedar)
[102]
Plan B
Collecte et traitement de la 
télémétrie; évaluation
Collecte OpenTeleme­
try, caviardage, évalua­
tion continue
OpenTelemetry Collector et son processeur 
de caviardage (redaction)[141]; AgentCore 
Observability et Evaluations[102]
Plan C
Registre et plan de 
contrôle des agents
Inventaire, quarantaine, 
cycle de vie, coupe-cir­
cuit
Microsoft Agent 365; ServiceNow AI 
Control Tower[47, 51]; AgentCore Registry; 
MuleSoft Agent Fabric
Couches 1 à 3
Plateforme SaaS à agents 
intégrés
MCP et A2A natifs, iden­
tité par agent, télémé­
trie exportable
Microsoft Copilot Studio (A2A en disponi­
bilité générale depuis avril 2026; identité 
Entra Agent ID créée pour chaque nouvel 
agent)[48]; Salesforce Agentforce (A2A en­
trant et sortant, client et serveur MCP)[49]; 
ServiceNow AI Agent Fabric
ATTENTION
Les performances annoncées par les fournisseurs ne remplacent pas une mesure. L’équipe 
d’agentgateway déclare environ 500 000 requêtes par seconde et une latence P99 inférieure à 0,2 ms 
à 30 000 requêtes par seconde, sans préciser le type de trafic ni le matériel[142]; la documentation de 
TrueFoundry annonce, dans la FAQ de sa page d’introduction, une latence ajoutée « typiquement » 
inférieure à 5 ms, alors que son propre banc d’essai (page d’architecture) mesure de 7 à 12 ms[143, 144]. 
Le cadre ne fixe donc aucun seuil de latence chiffré : la latence ajoutée (P50 et P99) se mesure dans les 
conditions de l’entreprise, politiques et traçage activés (section 13.2).
5.5 Mémoire des agents
Cette section distingue le contexte du modèle de la mémoire, définit quatre types de mémoire et fixe les 
contrôles qui encadrent leur écriture.
Le contexte n’est pas une mémoire
Les fenêtres de contexte atteignent environ un million de jetons chez les modèles de pointe, par exemple 
GPT-6.1 Sol d’OpenAI et Gemini 3 (novembre 2025); GPT-5.5 (avril 2026) offrait déjà 1,05  million de 
jetons[145, 146, 147]. Elles ne rendent pas la mémoire inutile, pour trois raisons. D’abord, la qualité baisse quand 
le contexte s’allonge : les modèles exploitent mieux l’information placée au début ou à la fin de l’entrée 
qu’au milieu, même lorsqu’ils sont conçus pour les longs contextes[148]. Anthropic décrit ce phénomène de 
« pourrissement du contexte » (context rot) : le rappel diminue à mesure que les jetons s’accumulent, et le 
contexte doit être traité comme une ressource finie[149]; une étude de Chroma sur 18 modèles montre qu’un 
seul distracteur suffit à réduire la performance[150]. Ensuite, chaque jeton réinjecté se paie à chaque appel. 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 41 sur 283


---
## [Page PDF 42]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Enfin, le contexte disparaît à la fin de la session. La règle qui en découle : ce qui doit durer est persisté hors 
du modèle, puis récupéré au moment où il sert.
Quatre types de mémoire
Le cadre reprend la taxonomie CoALA (Sumers et al., 2024), qui distingue une mémoire de travail à court 
terme et trois mémoires à long terme : épisodique (expériences passées), sémantique (connaissances sur 
le monde et sur l’agent lui-même) et procédurale (savoir-faire)[100]. Pour CoALA, la mémoire procédurale 
comprend aussi les poids du modèle; l’ajustement des modèles étant hors de la portée du cadre, celui-ci la 
limite aux invites système, aux contrats de compétences et aux flux d’outils validés. LangChain applique 
la même grille : des faits sur l’utilisateur relèvent de la mémoire sémantique, des exemples tirés d’actions 
antérieures de la mémoire épisodique, et l’invite système de la mémoire procédurale[151]. figure 4 et tableau 
13 en présentent l’organisation.
Agent en cours d’exécution
1 · Mémoire de travail
Fenêtre de contexte du modèle :
instructions, contrats d’outils,
sous-objectif, derniers échanges
État de la tâche persisté hors du
modèle à chaque transition (points
de contrôle du moteur durable)
Durée : la tâche · coût : chaque jeton
réinjecté est payé à chaque appel
Ce qui doit durer est persisté hors du modèle.
récupérer
consolider
2 · Mémoire épisodique
Résumés horodatés des interactions, trajectoires d’outils et résolutions
passées; provenance consignée pour chaque entrée
Calendrier de conservation · exposée en ressources ou outils MCP
3 · Mémoire sémantique
Connaissances du domaine : index vectoriels et lexicaux, graphes de
connaissances, documentation; recherche hybride avec citations
Mise à jour par les propriétaires des données · exposée par MCP
4 · Mémoire procédurale
Savoir-faire : invites système versionnées, contrats de compétences,
flux et séquences d’outils validés
Gérée comme du code : revue, version, évaluation avant déploiement
Contrôles obligatoires avant toute écriture en mémoire longue
Validation et provenance de la source · isolation par locataire et par serveur MCP · expiration · instantanés restaurables
Interdits : état conservé en mémoire de processus · transcriptions brutes comme mémoire longue · magasin partagé entre serveurs non isolés
Figure 4 — Quatre types de mémoire et contrôles d’écriture. La mémoire de travail vit dans le contexte du modèle et dans les 
points de contrôle du moteur durable; les trois mémoires longues sont persistées hors du modèle, récupérées au besoin et protégées 
par les mêmes contrôles d’écriture. Source : CRE-IA-2026-01, d’après la taxonomie CoALA (Sumers et al., 2024).
Tableau 13 — Types de mémoire des agents et contrôles applicables
Type
Contenu
Durée de vie
Exposition
Contrôles
Travail
Instructions, contrats d’outils, 
sous-objectif, derniers 
échanges; état de la tâche
La tâche; état persis­
té à chaque transi­
tion
Fenêtre de 
contexte; points 
de contrôle du 
moteur durable
Contexte minimal, compac­
tion, aucun état en mémoire 
de processus (EXIG-ARC-05)
Épisodique
Résumés horodatés des in­
teractions, trajectoires d’outils, 
résolutions passées
Durée liée à la fi­
nalité, avec expi­
ration par entrée 
(EXIG-CON-10)
Ressources ou ou­
tils MCP
Provenance de chaque en­
trée, filtrage des RP, isolation 
par mandant, expiration
Sémantique
Connaissances du domaine : 
index vectoriels et lexicaux, 
graphes de connaissances, do­
cumentation
Tant que la source 
est valide
Ressources ou ou­
tils MCP; re­
cherche hybride 
avec citations
Mise à jour par les pro­
priétaires des données; fil­
trage selon le mandant 
(EXIG-ARC-16)
Procédurale
Invites système versionnées, 
contrats de compétences, flux 
et séquences d’outils validés
La version de l’agent
Déployée avec 
l’agent; inscrite au 
registre
Revue, version, évaluation 
avant déploiement; aucune 
modification par l’agent
Écrire en mémoire longue
L’écriture peut se faire dans le chemin critique, en temps réel (transparente, mais plus lente), ou en arrière-
plan (sans latence, mais avec une fréquence à choisir)[151]. Le cadre accepte les deux modes, à condition qu’ils 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 42 sur 283


---
## [Page PDF 43]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
passent par les mêmes contrôles. Anthropic, pour son outil mémoire exécuté côté client, exige de valider 
chaque chemin d’accès contre la traversée de répertoires et recommande de filtrer les données sensibles 
avant l’écriture, de plafonner la taille des fichiers et de supprimer les mémoires longtemps inutilisées[152]. 
Les renseignements personnels conservés en mémoire sont détruits ou anonymisés une fois leurs fins 
accomplies, comme l’exige l’article 23 de la Loi sur la protection des renseignements personnels dans le 
secteur privé (EXIG-CON-10, section 12.2).
EXIG-ARC-22 · NE DOIT PAS
Pas d’historique brut comme mémoire
L’historique brut des échanges NE DOIT PAS être réinjecté en entier dans le contexte du modèle ni 
conservé tel quel comme mémoire longue. Ce qui doit durer est consolidé (résumé, fait, décision) dans 
la limite d’une fenêtre de contexte bornée à la fiche de l’agent, persisté hors du modèle et récupéré au 
besoin.
Pourquoi : un historique brut coûte à chaque appel, dégrade le rappel et accumule du bruit sans limite.
EXIG-ARC-23 · DOIT
Contrôles avant toute écriture en mémoire longue
Toute écriture en mémoire épisodique ou sémantique DOIT passer par des contrôles qui consignent 
la provenance de l’entrée, valident sa source, retirent les secrets et les renseignements personnels non 
nécessaires, l’isolent par locataire, par mandant et par serveur MCP, lui fixent une date d’expiration et 
permettent de restaurer un instantané antérieur.
Pourquoi : une information fausse inscrite en mémoire oriente toutes les décisions suivantes; l’OWASP en fait un 
risque distinct, l’empoisonnement de la mémoire et du contexte (ASI06 Memory & Context Poisoning) [28].
EXIG-ARC-24 · DOIT
Mémoire procédurale gérée comme du code
Toute modification de la mémoire procédurale (invites système, contrats de compétences, flux et 
séquences d’outils validés) DOIT suivre le processus de changement logiciel : revue, version, évaluation 
avant déploiement et inscription au registre. Un agent DOIT être privé de tout droit d’écriture sur sa 
propre mémoire procédurale en production.
Pourquoi : CoALA juge l’écriture en mémoire procédurale nettement plus risquée que l’écriture épisodique ou 
sémantique[100]; elle change le comportement de l’agent pour toutes les tâches à venir, comme un déploiement de 
code.
EXIG-ARC-25 · NE DOIT PAS
Aucun magasin de mémoire partagé sans isolation
Une mémoire longue NE DOIT PAS être accessible en écriture à des agents ou à des serveurs MCP 
qui ne sont pas isolés les uns des autres; le partage passe par des ressources en lecture seule ou par un 
service de mémoire qui applique les contrôles de l’exigence EXIG-ARC-23.
Pourquoi : le Centre d’architecture Azure proscrit le partage d’état mutable entre agents concurrents[9]; un magasin 
partagé permet à un composant compromis d’empoisonner tous les autres.
ANTI-PATRONS PROSCRITS
• Conserver l’état en mémoire de processus : le checkpointer en mémoire de LangGraph, par exemple, 
perd ses points de contrôle au redémarrage[124].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 43 sur 283


---
## [Page PDF 44]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
• Archiver les transcriptions brutes comme mémoire longue.
• Partager une table de mémoire modifiable entre serveurs MCP non isolés.
• Stocker des secrets, des jetons ou des approbations dans la mémoire d’un agent.
• Laisser un agent réécrire ses propres invites système ou contrats de compétences.
Plusieurs technologies réalisent ces rôles; elles sont citées à titre d’exemples non normatifs. LangGraph 
sépare les checkpointers, qui conservent l’état par fil d’exécution, d’un magasin distinct pour la mémoire 
à long terme partagée entre fils[124]. Letta maintient le patron MemGPT, qui déplace l’information entre le 
contexte et un stockage externe à la manière d’une mémoire virtuelle[153, 154]. Zep s’appuie sur Graphiti, 
un graphe de connaissances temporel qui conserve l’historique des relations, utile pour l’audit puisqu’on 
peut savoir à quel moment un fait était vrai[155]. GraphRAG construit un graphe d’entités et des résumés de 
communautés qui aident à répondre aux questions de synthèse sur un vaste corpus[156]. Le cadre ne fixe ni 
produit ni latence cible : ces paramètres se mesurent dans l’environnement de l’entreprise.
5.6 Parcours d’une demande de bout en bout
Cette section suit une demande à travers les six couches pour montrer comment les règles s’enchaînent. 
Exemple : une conseillère du service à la clientèle demande l’émission d’un avoir de 1 200 $ sur la facture d’un 
client. L’agent de facturation est de classe de risque modérée, plafonné au niveau N3; l’outil emettre_avoir 
est de palier P2 (écriture réversible), et le catalogue lui fixe un seuil d’exécution autonome de 500 $, valeur 
propre à l’exemple.
1. Canal. La conseillère formule sa demande dans l’outil de collaboration. Le canal l’authentifie, établit 
le mandant, ouvre la trace et transmet l’intention sans la transformer (EXIG-ARC-03, EXIG-ARC-04).
2. Routage. Le routeur qualifie l’intention («  émettre un avoir  ») et choisit le flux déterministe de 
traitement des avoirs inscrit au registre, plutôt qu’un agent libre; ce choix ne confère aucun droit 
(EXIG-ARC-07).
3. Ouverture de la tâche. Le moteur d’exécution durable crée la tâche, lui attribue son enveloppe 
budgétaire (jetons, coût, appels d’outils, délai) et obtient un jeton délégué au nom de la conseillère 
(section 9.3); l’état est persisté.
4. Raisonnement. L’étape d’analyse invoque l’agent de facturation, qui appelle son modèle par la 
passerelle de modèles; celle-ci résout l’alias, applique les quotas et impute jetons et coût au centre de 
coûts (EXIG-ARC-08, EXIG-ARC-09).
5. Lecture. L’agent appelle l’outil MCP consulter_situation_compte (palier P1) par la passerelle 
d’agents, qui vérifie le catalogue, restreint le jeton à l’audience du serveur MCP (paramètre resource, 
RFC 8707) et propage la trace; l’outil filtre ses résultats selon les droits de la conseillère (EXIG-ARC-16).
6. Délégation éventuelle. Si une vérification relève d’un autre domaine, la conformité par exemple, 
l’orchestrateur délègue la sous-tâche par A2A à l’agent de ce domaine, toujours par la passerelle; la 
séquence détaillée figure à la section 6.6.
7. Approbation. L’agent prépare l’appel à emettre_avoir. Le montant dépasse le seuil déclaré  : le 
moteur suspend la tâche, état persisté, et présente l’action exacte à une approbatrice, dont la décision 
produit un jeton signé lié à cette action (section 8.5).
8. Écriture. Le moteur reprend la tâche. L’appel passe par la passerelle avec le jeton d’approbation et 
une clé d’idempotence; le serveur MCP de facturation appelle l’API de l’ERP, qui applique ses propres 
contrôles et enregistre l’avoir avec la référence de trace (EXIG-ARC-17, EXIG-ARC-18).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 44 sur 283


---
## [Page PDF 45]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
9. Résultat ou compensation. L’artefact remonte au canal et la conseillère reçoit la confirmation 
avec la référence d’audit. Si une étape ultérieure échoue sans reprise possible, le moteur exécute la 
compensation déclarée, ici l’annulation de l’avoir (section 7.5).
10. Audit et apprentissage. Le journal d’audit consigne le mandant, l’agent et sa version, le modèle, 
l’outil et l’empreinte de ses arguments, ainsi que l’approbation (section 10.3). Les traces alimentent 
l’évaluation continue et le coût par tâche réussie; un résumé validé de la résolution entre en mémoire 
épisodique (EXIG-ARC-23).
À RETENIR
Trois éléments descendent avec chaque appel : le mandant, le contexte de trace et les plafonds restants. 
Trois éléments remontent : le résultat, ses artefacts et les mesures de coût et de qualité. En environ­
nement serveur, aucun appel n’atteint un outil MCP, un agent ou un système d’un autre domaine 
sans traverser la passerelle, et aucune écriture n’atteint un système d’enregistrement sans ses propres 
contrôles métier.
6 Interopérabilité
Ce chapitre fixe la manière dont les agents de l’entreprise se relient aux outils, aux données, aux autres 
agents, aux événements et aux personnes. Il s’appuie sur des protocoles ouverts sous gouvernance neutre : 
MCP pour l’intégration verticale (agent vers outil), A2A pour l’intégration horizontale (agent vers agent), 
CloudEvents et AsyncAPI pour les échanges asynchrones. Chaque intégration est examinée à quatre 
niveaux, du juridique au technique, et n’emploie que des standards inscrits au catalogue, à une version fixée. 
Les sections 6.5 à 6.7 détaillent chaque protocole; les sections 6.8 et 6.9 traitent des contrats, du versionnage 
et de la veille.
6.1 Quatre niveaux d’interopérabilité et gouvernance intégrée
Une connexion technique ne suffit pas : deux agents qui échangent sans s’entendre sur le sens des données 
ni sur les responsabilités produisent des erreurs silencieuses. Le cadre transpose donc aux agents le modèle 
du Cadre européen d’interopérabilité (European Interoperability Framework, EIF).
Le nouvel EIF, publié par la Commission européenne en 2017, décrit l’interopérabilité en quatre couches 
(juridique, organisationnelle, sémantique et technique), encadrées par une composante transversale, la 
gouvernance intégrée des services publics, et par une couche de fond, la gouvernance de l’interopérabilité[157, 
158]. Il énonce 12 principes et 47 recommandations, dont la conclusion d’accords d’interopérabilité dans 
toutes les couches (recommandation 26)[157]. Le texte reste vivant : le règlement (UE) 2024/903 pour une 
Europe interopérable, en vigueur depuis le 11 avril 2024, confie sa mise à jour au comité pour une Europe 
interopérable[159]. L’EIF vise les services publics européens; le cadre en retient la structure, pas le champ 
d’application.
Appliqués aux agents, les quatre niveaux posent quatre questions simples :
• Juridique : l’échange respecte-t-il les lois et les contrats? Par exemple, un agent qui confie l’analyse 
d’une réclamation à l’agent d’un partenaire hébergé en Ontario communique des renseignements 
personnels à l’extérieur du Québec, ce qui exige une EFVP préalable (art. 17 de la Loi sur la protection 
des renseignements personnels dans le secteur privé, RLRQ, c. P-39.1, ci-après « Loi sur le privé »)[160].
• Organisationnel  : qui répond de quoi, de part et d’autre? L’EIF parle d’aligner les processus, les 
responsabilités et les attentes pour atteindre des objectifs communs[157].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 45 sur 283


---
## [Page PDF 46]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
• Sémantique : les parties comprennent-elles la même chose? L’EIF y inclut l’aspect syntaxique, soit le 
format exact des informations échangées, pour que ce qui est envoyé soit ce qui est compris[157].
• Technique : les systèmes peuvent-ils se joindre de façon sûre? Le niveau couvre les spécifications 
d’interface, les services d’interconnexion et d’intégration de données et les protocoles de communication 
sécurisés[157].
La gouvernance intégrée tient le tout dans la durée. L’EIF y exige notamment des structures, des rôles et 
des responsabilités définis, des ententes de niveau de service, la gestion des accords d’interopérabilité, des 
procédures de gestion du changement et des plans de continuité et de qualité des données, parce que les 
changements législatifs, organisationnels et technologiques perturbent régulièrement l’interopérabilité[157]. 
Dans le cadre, ce rôle revient au registre, au catalogue d’entreprise et au comité d’architecture et des risques 
agentiques (chapitre 11).
Gouvernance intégrée : registre, catalogue, comité
Juridique
L’échange respecte-t-il
les lois et les contrats?
Exigences pour les agents
Finalité et base légale de chaque flux de renseignements personnels; EFVP; entente écrite
pour toute communication hors Québec; clauses contractuelles pour les agents de tiers
Organisationnel
Qui répond de quoi,
de part et d’autre?
Exigences pour les agents
Propriétaire métier nommé, équipe de garde, niveaux de service et voie d’escalade inscrits
au contrat d’agent; processus métier alignés de part et d’autre de la délégation
Sémantique
Les parties comprennent-
elles la même chose?
Exigences pour les agents
Vocabulaire métier commun, modèles de données canoniques, schémas JSON versionnés,
descriptions d’outils et de compétences rédigées pour être comprises par un modèle
Technique
Les systèmes peuvent-ils
se joindre de façon sûre?
Exigences pour les agents
Protocoles du catalogue (MCP, A2A, CloudEvents, OpenAPI), TLS 1.3, authentification
normalisée (OAuth 2.x), contexte de trace W3C propagé à chaque appel
Figure 5 — Quatre niveaux d’interopérabilité appliqués aux agents. Chaque intégration d’agent se lit de haut en bas : le juridique 
fixe ce qui est permis, l’organisationnel désigne qui en répond, le sémantique établit le sens des données et le technique, la façon dont 
elles circulent. La gouvernance intégrée encadre les quatre niveaux. Source : adapté du nouveau Cadre européen d’interopérabilité 
(Commission européenne, 2017); exigences propres au cadre.
Tableau 14 — Niveaux d’interopérabilité et exigences minimales pour une intégration d’agent
Niveau
Question à trancher
Exigences minimales
Traité à
Juridique
L’échange respecte-t-il les 
lois et les contrats?
Finalité et fondement (consentement ou excep­
tion prévue par la loi) documentés pour chaque 
flux de renseignements personnels; EFVP lorsque 
la loi l’exige, notamment avant toute communi­
cation hors Québec; entente écrite avec chaque 
tiers; clauses contractuelles pour les agents et 
serveurs MCP de tiers.
Chapitres 12 
et 13
Organisationnel
Qui répond de quoi, de 
part et d’autre?
Propriétaire métier nommé et équipe de garde 
de chaque côté; niveaux de service et voie 
d’escalade inscrits au contrat d’agent; processus 
métier modélisés et alignés de part et d’autre de 
la délégation.
Sections 11.1 
et 11.4
Sémantique
Les parties comprennent-
elles la même chose?
Vocabulaire métier commun; données de réfé­
rence (taxonomies, listes de codes); schémas 
JSON Schema 2020-12 versionnés; unités, de­
vises, assiettes de taxes et fuseaux horaires expli­
cites; descriptions d’outils et de compétences ré­
digées pour être comprises par un modèle.
Section 6.8
Technique
Les systèmes peuvent-ils se 
joindre de façon sûre?
Protocole du catalogue à la version fixée; TLS 
1.3 par défaut et TLS 1.2 toléré comme plan­
cher (choix du cadre, conforme aux recomman­
Sections 6.3 à 
6.7; chapitres 
9 et 10
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 46 sur 283


---
## [Page PDF 47]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Niveau
Question à trancher
Exigences minimales
Traité à
dations d’A2A[68, 161]); authentification normalisée; 
contexte de trace W3C propagé à chaque appel.
Gouvernance intégrée 
(transversale)
L’échange restera-t-il inter­
opérable dans le temps?
Accord d’interopérabilité par intégration; gestion 
du changement des contrats; plan de continuité; 
fiche d’agent et catalogue à jour.
Section 6.8; 
chapitre 11
Gouvernance de 
l’interopérabilité (fond)
Qui choisit les standards et 
qui arbitre?
Catalogue des protocoles révisé chaque tri­
mestre; dérogations instruites par le comité.
Sections 6.3, 
11.6 et 11.7
EXEMPLE : UNE ERREUR QUE LE PROTOCOLE NE VOIT PAS
L’agent de facturation d’une filiale transmet par A2A un artefact dont le champ montant vaut 1 149,75. 
L’agent de rapprochement du siège le lit comme un montant hors taxes, alors qu’il inclut la TPS et la 
TVQ. Les deux agents respectent le protocole à la lettre; seule la revue sémantique (schéma commun, 
unité et assiette déclarées) prévient l’écart.
EXIG-INT-01 · DOIT
Revue d’interopérabilité à quatre niveaux
Toute intégration d’un agent avec un outil, une ressource, un autre agent ou un flux d’événements DOIT 
faire l’objet, avant sa mise en production, d’une revue couvrant les niveaux juridique, organisationnel, 
sémantique et technique du tableau 14. Le résultat DOIT être consigné dans la fiche d’agent (annexe B).
Pourquoi : une intégration techniquement valide peut être illicite, sans responsable ou fausse sur le sens; l’EIF 
promeut l’interopérabilité dès la conception[157].
EXIG-INT-02 · DOIT
Vocabulaire et schémas d’entreprise
Les données échangées entre agents, entre agents et outils et sur le bus d’événements DOIVENT être 
décrites par des schémas JSON Schema 2020-12 versionnés (dans AsyncAPI 3.x, en déclarant explici­
tement schemaFormat à JSON Schema 2020-12, le format par défaut étant le Schema Object d’AsyncAPI) 
et s’appuyer sur le vocabulaire métier et les données de référence de l’entreprise (taxonomies, listes de 
codes, unités et devises explicites). Ces schémas DOIVENT être gérés au niveau de l’entreprise, et non 
par chaque équipe d’agent.
Pourquoi : l’EIF demande une gestion de l’information coordonnée au plus haut niveau et appuyée sur des données 
de référence[157]; JSON Schema 2020-12 est le dialecte par défaut de MCP[162, 163].
EXIG-INT-03 · DOIT
Accord d’interopérabilité et gestion du changement
Toute intégration qui franchit la frontière d’un domaine métier ou de l’entreprise DOIT être couverte 
par un accord d’interopérabilité, intégré au contrat d’agent ou d’outil, qui nomme le propriétaire de 
chaque partie, les niveaux de service, la voie d’escalade et la procédure de gestion du changement 
(préavis, période de coexistence, tests de non-régression).
Pourquoi : l’EIF recommande des accords d’interopérabilité dans toutes les couches et une gestion explicite du 
changement[157].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 47 sur 283


---
## [Page PDF 48]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
6.2 Carte des interactions et protocoles retenus
Le cadre associe un protocole à chaque type d’interaction d’un agent. La figure 6 situe ces interactions 
autour de l’agent : verticalement vers les outils, horizontalement vers les autres agents, de façon asynchrone 
vers le bus d’événements et, du côté humain, vers l’interface.
Agent
raisonne, planifie, appelle
des outils, délègue, publie
Agent → interface utilisateur
AG-UI · flux SSE
état partagé, formulaires d’approbation
Agent → outils et données
MCP
outils, ressources, invites;
API existantes via OpenAPI 3.1
et adaptateurs
intégration verticale
Agent → agent pair opaque
A2A
carte d’agent, tâche à états,
diffusion en continu, notifications;
autre cadriciel, autre organisation
horizontale
Agent ↔ bus d’événements
CloudEvents · AsyncAPI
découplage temporel, plusieurs
abonnés, rejeu; Kafka ou
équivalent infonuagique
asynchrone
Identité et autorisation
OAuth 2.x, échange de jetons (RFC 8693),
OpenID Connect, SPIFFE; mTLS ou DPoP
Observabilité
OpenTelemetry (conventions GenAI),
contexte W3C Trace Context
Découverte et confiance
Catalogue d’entreprise, cartes d’agent
signées, registre de serveurs MCP,
versions épinglées et empreintes
À surveiller (pilotes seulement)
Protocoles de commerce et de paiement
agentiques; formats propriétaires
contenus derrière un adaptateur
Figure 6 — Carte des interactions de l’agent et protocoles retenus. L’agent occupe le centre; chaque liaison correspond à un type 
d’interaction et au protocole retenu. Les bandeaux du bas rappellent les fonctions transversales (identité, observabilité, découverte et 
confiance) et ce qui reste en veille. Source : cadre CRE-IA-2026-01; répartition MCP et A2A conforme au guide officiel du projet A2A.
• Agent → outils et données : MCP. La cible a des entrées et des sorties définies, souvent sans état; 
l’agent appelant garde la boucle de raisonnement. Les API existantes y sont exposées par des adaptateurs, 
sans réécriture (section 6.5).
• Agent → agent : A2A. La cible est un agent autonome, potentiellement opaque, qui raisonne, garde un 
état sur plusieurs tours et peut demander une précision (section 6.6).
• Agent ↔ bus d’événements : CloudEvents et AsyncAPI. L’émetteur ignore ses consommateurs; 
l’échange admet plusieurs abonnés, le découplage dans le temps et le rejeu des entrées (section 6.7).
• Agent → interface : AG-UI ou flux SSE (Server-Sent Events) structuré. AG-UI est un protocole 
ouvert et événementiel (31 types d’événements standard selon la documentation, licence MIT), né d’un 
partenariat de CopilotKit avec LangChain et CrewAI; il n’impose pas de transport (SSE, WebSockets, 
webhooks, etc.) et complète MCP et A2A[164, 165, 166]. Il demeure au statut Évaluer.
Cette répartition reprend le guide officiel du projet A2A  : MCP relie un agent à des outils et à des 
ressources aux entrées et aux sorties définies, souvent sans état, alors qu’A2A relie des agents autonomes, 
potentiellement opaques, qui raisonnent et conservent un état sur des échanges à plusieurs tours[39]. Les 
deux se complètent  : l’agent spécialiste joint par A2A utilise lui-même des outils MCP. L’événement 
comble un troisième besoin, car MCP ne garantit ni la livraison ni la cohérence des données, alors qu’un 
journal d’événements persistant découple producteurs et consommateurs, comme le souligne l’architecte 
Kai Waehner[167].
Une question départage la plupart des cas : la cible raisonne-t-elle? Si elle exécute une fonction aux entrées 
et aux sorties définies, c’est un outil, même si elle emploie un modèle en interne (règle du cadre). Si elle 
planifie, conserve un état et peut renvoyer une question, c’est un agent. Si l’émetteur ne doit pas connaître 
ses destinataires, c’est un événement. Dans tous les cas, l’échange qui sort d’un domaine passe par la 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 48 sur 283


---
## [Page PDF 49]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
passerelle d’agents (section 9.4); la documentation d’A2A recommande d’ailleurs fortement une solution de 
gestion d’API devant tout serveur exposé à l’externe[161].
À RETENIR
MCP pour ce qui s’exécute, A2A pour ce qui raisonne, l’événement pour ce qui se diffuse. Les trois 
passent par la passerelle d’agents et par le catalogue d’entreprise.
EXIG-INT-04 · DOIT
Protocole désigné par type d’interaction
Chaque interaction d’un agent DOIT emprunter le protocole que le catalogue désigne pour son type : 
MCP pour l’accès aux outils, aux ressources et aux invites; A2A pour la délégation à un autre agent; 
CloudEvents, décrit par un contrat AsyncAPI, pour les événements. Tout connecteur propriétaire ou 
format hors catalogue exige une dérogation (section 11.6).
Pourquoi : un protocole commun par type d’interaction ramène le maillage de N × M connecteurs à N + M contrats 
(chapitre 2) et permet à la passerelle d’appliquer une politique uniforme.
EXIG-INT-05 · DEVRAIT
Agent pair invoqué par A2A, pas déguisé en outil
Un agent d’un autre domaine ou d’un tiers, qui planifie, conserve un état ou peut demander une préci­
sion, DEVRAIT être invoqué par A2A plutôt qu’enveloppé dans un outil MCP. L’enveloppe « agent 
comme outil » reste permise à l’intérieur d’un même agent ou d’un même domaine de confiance.
Pourquoi : A2A expose le cycle de vie de la tâche (entrée requise, authentification requise, annulation, artefacts), 
que l’enveloppe en outil masque; l’approbation humaine et l’audit en dépendent[68].
6.3 Catalogue des protocoles et standards
Le catalogue des protocoles dit quel standard employer, à quelle version et avec quel degré de confiance. Il 
distingue ce qui est une norme publiée, ce qui n’est qu’un brouillon et ce qui relève encore de l’annonce. 
Chaque entrée porte l’un des quatre statuts suivants, éventuellement assorti d’une réserve :
• Adopter usage par défaut, exigé pour toute nouvelle intégration du type visé;
• Évaluer pilotes encadrés, derrière la passerelle d’agents (section 6.9); passage en production seulement 
après une décision du comité qui fait passer l’entrée au statut Adopter;
• Surveiller veille et essais hors production, sans données réelles;
• Contenir existant toléré derrière un adaptateur, sans nouvel usage, avec un plan de sortie daté.
Tableau 15 — Catalogue des protocoles et standards (état au 27 octobre 2026)
Interaction
Standard et version de référence
Statut
Règle d’usage
Agent → outils et 
données
Model Context Protocol (MCP), révision 2026-07-28, courante 
au 27 octobre 2026[34, 168]
Adopter
Serveurs inscrits au ca­
talogue et joints par 
la passerelle; Streamable 
HTTP en environne­
ment serveur; exten­
sions officielles (Tasks, 
Apps, autorisation; 
Enterprise-Managed Au­
thorization reste au sta­
tut Évaluer), désactivées 
par défaut dans MCP, 
activées seulement si 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 49 sur 283


---
## [Page PDF 50]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Interaction
Standard et version de référence
Statut
Règle d’usage
elles sont inscrites au ca­
talogue[169] (6.5).
Agent → agent
Agent2Agent (A2A), version de protocole 1.0 (publication 1.0.0 
du 12 mars 2026; correctif 1.0.1 du 28 mai 2026)[29, 30]
Adopter
Carte d’agent signée et 
inscrite; liaisons stan­
dard JSON-RPC, gRPC 
ou HTTP+JSON; en-tête 
A2A-Version à chaque 
requête; interfaces 0.3 
seulement en coexis­
tence bornée (6.6).
Agent → API exis­
tante
OpenAPI 3.1.x ou 3.2.x (3.2.1 du 10 septembre 2026)[170]; er­
reurs au format RFC 9457[171]
Adopter
Aucun appel d’API sans 
contrat; exposition aux 
agents par des adapta­
teurs déclaratifs qui pro­
duisent des outils orien­
tés tâche, sans réécrire 
les services.
Séquences 
d’appels d’API
Arazzo 1.1.0 (OpenAPI Initiative, 17 mai 2026)[172]
Évaluer
Description lisible par 
machine des flux déter­
ministes d’appels d’API.
Schémas de don­
nées
JSON Schema 2020-12[163]
Adopter
Dialecte unique des 
contrats d’outils, 
de compétences et 
d’événements; aucun 
$ref vers une URI réseau 
non autorisée[162].
Événements asyn­
chrones
CloudEvents 1.0 (révision 1.0.2) pour l’enveloppe; AsyncAPI 3.x 
pour le contrat[173, 174]
Adopter
Tout événement pro­
duit ou consommé par 
un agent; extensions de 
gouvernance et comp­
teur de sauts (6.7).
Identité et autori­
sation
OAuth 2.0 profilé par la RFC 9700 (BCP 240); OpenID Connect; 
échange de jetons (RFC 8693); SPIFFE et SPIRE, projets diplô­
més de la CNCF[70, 116, 117, 175]
Adopter
Identité propre à chaque 
agent; jetons délégués à 
audience restreinte (cha­
pitre 9).
Identité et autori­
sation
OAuth 2.1, Internet-Draft (draft-ietf-oauth-v2-1-16, septembre 
2026)[176]
Adopter 
avec réserve
S’aligner sur son profil 
(PKCE, ni octroi implicite 
ni octroi par mot de 
passe) sans le présenter 
comme une norme pu­
bliée.
Identité et autori­
sation
Identity Assertion JWT Authorization Grant (ID-JAG, brouillon 
de groupe de travail) et extension MCP Enterprise-Managed 
Authorization[177, 178]
Évaluer
Accès des employés aux 
serveurs MCP décidé par 
le fournisseur d’identité 
de l’entreprise.
Identité et autori­
sation
Transaction Tokens (draft-ietf-oauth-transaction-tokens-11)
[179]
Évaluer
Propagation du contexte 
d’identité dans la chaîne 
d’appels interne d’un 
domaine.
Observabilité
OpenTelemetry; conventions sémantiques GenAI au niveau 
Development, version épinglée (v1.41.0 ou première version 
étiquetée du dépôt semantic-conventions-genai)[180, 181]
Adopter
Couche de correspon­
dance dans les ta­
bleaux de bord; attributs 
d’entreprise sous pré­
fixe de domaine inversé 
(chapitre 10).
Observabilité
W3C Trace Context, Recommandation[103]
Adopter
Contexte propagé dans 
HTTP, dans le champ 
_meta de MCP, dans A2A 
et dans CloudEvents.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 50 sur 283


---
## [Page PDF 51]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Interaction
Standard et version de référence
Statut
Règle d’usage
Agent → interface 
utilisateur
AG-UI (Agent-User Interaction Protocol)[164]
Évaluer
Pilotes; à défaut, flux 
SSE structuré produit par 
l’orchestrateur.
Infrastructure mul­
tiagent
AGNTCY : OASF (Open Agentic Schema Framework) et Agent 
Directory Service (ADS); SLIM (Secure Low-Latency Interactive 
Messaging) et Identity[182]
Évaluer 
OASF, ADS 
Surveiller 
SLIM, Identity
Projet de la Linux Foun­
dation candidat à l’AAIF; 
aucune dépendance de 
production sans décision 
du comité (6.9).
Commerce et paie­
ments agentiques
Agentic Commerce Protocol (OpenAI et Stripe), AP2, UCP[41, 
183, 184]
Surveiller
Aucun paiement initié 
par un agent hors des 
règles de la section 6.9.
Réseaux d’agents 
ouverts, à identité 
décentralisée (DID 
du W3C)
Agent Network Protocol (ANP), projet communautaire[185, 186]
Surveiller
Aucune adoption en 
production.
Formats propres à 
un fournisseur
Variable
Contenir
Tolérés derrière un 
adaptateur, jamais ex­
posés directement aux 
autres agents; plan de 
sortie daté.
Les versions sont fixées au catalogue, pas dans chaque contrat d’agent : une montée de version se décide 
une fois, pour tout le parc. Le comité révise le catalogue chaque trimestre (section 11.7); un correctif de 
sécurité peut justifier une révision extraordinaire.
ATTENTION : NORMES, BROUILLONS ET PRÉVERSIONS
Plusieurs entrées ne sont pas des normes publiées : OAuth 2.1, ID-JAG et Transaction Tokens sont des 
Internet-Drafts; les extensions documentées de CloudEvents (Auth Context, Data Classification, Distri­
buted Tracing, etc.) n’ont aucun statut officiel et peuvent être modifiées ou retirées[187]; les conventions 
GenAI d’OpenTelemetry sont au niveau Development, où des changements incompatibles, voire un 
retrait, peuvent survenir sans garantie de dépréciation préalable[119, 188]; le registre officiel MCP est en 
préversion[43]. Le cadre les emploie pour ce qu’ils sont : à une version épinglée, derrière une couche 
d’adaptation.
EXIG-INT-06 · DOIT
Statut au catalogue avant tout usage en production
Un protocole, un standard ou une extension de protocole DOIT figurer au catalogue avec le statut 
Adopter pour être employé en production. Le statut Évaluer limite l’usage à des pilotes; le statut 
Surveiller l’exclut de la production; le statut Contenir interdit tout nouvel usage.
Pourquoi : l’ajout silencieux d’un protocole recrée les intégrations ad hoc que le cadre veut éliminer et soustrait les 
échanges aux contrôles de la passerelle.
EXIG-INT-07 · DOIT
Version de référence fixée au catalogue
Le catalogue DOIT fixer, pour chaque standard adopté, la version de référence (révision MCP, version 
de protocole A2A, version des conventions OpenTelemetry, de CloudEvents et d’AsyncAPI). Chaque 
serveur, agent et passerelle DOIT déclarer les versions qu’il prend en charge; une déclaration incom­
patible avec le catalogue DOIT bloquer l’inscription au registre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 51 sur 283


---
## [Page PDF 52]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Pourquoi 
: 
MCP 
et 
A2A 
rejettent 
explicitement 
une 
version 
non 
prise 
en 
charge 
(erreurs 
UnsupportedProtocolVersion et VersionNotSupportedError)[68, 162]; un parc aux versions mêlées échoue de façon 
imprévisible.
EXIG-INT-08 · DOIT
Révision trimestrielle du catalogue des protocoles
Le comité d’architecture et des risques agentiques DOIT réviser le catalogue des protocoles au moins 
une fois par trimestre et consigner, pour chaque entrée, la date de révision, le statut retenu et sa 
justification. Tout changement de statut est notifié aux propriétaires des agents qui emploient l’entrée.
Pourquoi : entre mars 2025 et juillet 2026, MCP a publié quatre révisions (2025-03-26, 2025-06-18, 2025-11-25 et 
2026-07-28) et A2A est passé de la version 0.1 à la version 1.0[30, 34, 189]; un catalogue figé devient faux en quelques mois.
EXIG-INT-09 · NE DOIT PAS
Statut normatif exact
Une exigence d’architecture, une clause contractuelle ou une entrée du catalogue NE DOIT PAS pré­
senter un brouillon (Internet-Draft), une préversion ou une annonce de fournisseur comme une norme 
publiée. Le catalogue indique le statut exact de chaque élément : norme, recommandation, brouillon de 
groupe de travail, brouillon individuel, préversion ou projet hébergé par une fondation.
Pourquoi : un brouillon peut changer ou expirer (la version −16 d’OAuth 2.1 expire le 7 mars 2027)[176]; une exigence 
qui s’y appuie doit pouvoir évoluer sans renégocier un contrat.
6.4 Matrice de sélection
La matrice traduit la carte de la figure 6 en règle de choix pour les cas courants. Elle se lit par scénario : le 
protocole découle du type de cible, du couplage recherché et de l’endroit où vit l’état.
Tableau 16 — Matrice de sélection des protocoles
Scénario
Protocole
Couplage
État côté appelé
Raison du choix
Processus 
connu à étapes 
fixes (réglemen­
té ou audité)
Flux déterministe 
(chapitre 7) qui 
appelle des outils 
MCP ou des API
Piloté par le moteur
Dans le moteur d’exécution 
durable
Prévisible et au­
ditable; le mo­
dèle n’intervient 
qu’aux étapes qui 
l’exigent.
Agent → ou­
til, base de don­
nées ou mo­
teur de re­
cherche docu­
mentaire
MCP sur Strea­
mable HTTP
Synchrone et court; réponse 
JSON ou flux SSE propre à la re­
quête[190]
Aucun état cognitif; état appli­
catif par identifiant explicite, 
revalidé à chaque appel
Découverte 
des schémas et 
contrôle d’accès 
unifié à la passe­
relle.
Agent → traite­
ment d’outil de 
longue durée
MCP avec 
l’extension offi­
cielle Tasks, si elle 
est inscrite au ca­
talogue[191]
Asynchrone, par interrogation
Tâche durable (identifiant, du­
rée de vie)
Évite de garder 
une connexion ou­
verte; annulation 
coopérative.
API REST exis­
tante → parc 
d’agents
Contrat OpenAPI 
exposé en outils 
MCP par un adap­
tateur
Synchrone
Aucun
Réutilise le patri­
moine d’API sans 
connecteur propre 
à chaque agent.
Agent → agent 
spécialiste, 
tâche interac­
tive ou en plu­
sieurs tours
A2A
Lâche, par compétence; réponse 
bloquante, en continu ou par 
notification push
Tâche à états (huit états de 
cycle de vie en A2A 1.0, neuf 
valeurs d’énumération avec 
TASK_STATE_UNSPECIFIED) [192]
Suivi de progres­
sion, demandes de 
précision, échange 
d’artefacts entre 
cadriciels distincts.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 52 sur 283
