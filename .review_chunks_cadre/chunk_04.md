# chunk_04 — pages PDF 31 à 42 (sur 283)



---
## [Page PDF 31]

CRE-IA-2026-01 · Cadre de référence
Partie II — Architecture, interopérabilité et 
orchestration
Comment les agents se branchent aux systèmes, collaborent entre eux et sont orchestrés, et jusqu’où ils 
peuvent agir seuls.
5 · Architecture de référence
6 · Interopérabilité
7 · Orchestration
8 · Autonomie et supervision humaine
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 31 sur 283


---
## [Page PDF 32]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
5 Architecture de référence
L’architecture de référence découpe l’entreprise agentique en six couches, de la demande jusqu’aux systèmes 
d’enregistrement, et en trois plans transversaux qui servent chacune d’elles. Sa règle centrale est simple : 
aucun agent n’atteint un outil, une donnée ou un autre agent hors de son domaine sans passer par la 
passerelle d’agents et le catalogue d’entreprise. Les composants décrits sont des rôles, et non des produits : 
le chapitre les fait correspondre à des blocs de solution remplaçables, précise l’architecture de la mémoire 
des agents et suit une demande de bout en bout.
5.1 Vue d’ensemble
Cette section présente la structure générale et la règle qui la tient ensemble; figure 3 la résume.
1
Canaux et déclencheurs
Portails, clavardage
et applications
Outils de collaboration
(Teams, Slack)
Formulaires
d’approbation humaine
Webhooks, tâches
planifiées, événements
2
Orchestration et état
Routeur sémantique
(qualification)
Moteur d’exécution
durable (flux, sagas)
Coordination
multiagent (A2A)
Points de contrôle,
mémoire de travail
3
Agents et exécution cognitive
Agents spécialisés
(internes, tiers)
Passerelle de modèles
(routage, cache, repli)
Bac à sable de code
(microVM, gVisor)
Mémoire épisodique
et procédurale
4
Médiation et connectivité
Passerelle d’agents
MCP · A2A · politiques
Catalogue d’entreprise
(outils, cartes d’agent)
Bus d’événements
(CloudEvents, AsyncAPI)
5
Outils et données
Serveurs MCP
de domaine
Adaptateurs
OpenAPI → outils
Ressources, index,
graphes de connaissances
Outils de
compensation
6
Systèmes d’enregistrement
ERP, CRM, systèmes de dossiers, entrepôts de données, SaaS : exposés tels quels, sans réécriture
PLANS TRANSVERSAUX
A · Identité et sécurité
• Identité propre par agent (SPIFFE, OIDC)
• Jetons délégués courts (RFC 8693)
• Moteur de politiques, paliers d’outils
• Coffre de secrets, garde-fous, DLP
• Approbation humaine signée
B · Observabilité, évaluation, FinOps
• Traces OpenTelemetry (GenAI)
• Contexte W3C de bout en bout
• Journal d’audit inaltérable
• Évaluation continue (3 paliers)
• Budgets, coût par tâche réussie
C · Gouvernance et registre
• Registre des agents et serveurs MCP
• Classes de risque, niveaux N0 à N4
• Cycle de vie et homologation
• Dérogations, indicateurs
• Comité d’architecture et des
risques agentiques
Demandes descendantes (mandant, trace, plafonds)
Résultats et artefacts remontants
Interdit : un agent n’atteint jamais un système ou un outil hors domaine sans passer par la passerelle et le catalogue
Figure 3 — Architecture de référence : six couches et trois plans transversaux. Les demandes descendent de la couche 1 vers la 
couche 6 en portant le mandant, la trace et les plafonds de la tâche; les résultats et artefacts remontent. Les trois plans transversaux 
servent chaque couche, et la passerelle d’agents ferme tout chemin qui contournerait le catalogue. Source : CRE-IA-2026-01.
Les six couches se lisent de haut en bas, dans le sens où circule une demande :
1. Canaux et déclencheurs : là où naît la demande, qu’elle vienne d’une personne (portail, clavardage, 
outil de collaboration) ou d’un système (appel HTTP automatique (webhook), tâche planifiée, événe­
ment).
2. Orchestration et état : qui fait quoi, dans quel ordre, et où l’état de la tâche survit aux pannes.
3. Agents et exécution cognitive : là où l’on raisonne; on y trouve les agents, la passerelle de modèles 
et le bac à sable de code.
4. Médiation et connectivité : le passage obligé des échanges, avec la passerelle d’agents, le catalogue 
d’entreprise et le bus d’événements.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 32 sur 283


---
## [Page PDF 33]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
5. Outils et données : ce que les agents peuvent faire et savoir, au moyen de serveurs MCP de domaine, 
d’adaptateurs d’API, d’index et de graphes de connaissances.
6. Systèmes d’enregistrement : là où la vérité de l’entreprise est conservée (progiciel de gestion intégré 
ou ERP, gestion de la relation client ou CRM, systèmes de dossiers, entrepôts de données, logiciels-
services ou SaaS).
Trois plans transversaux fournissent leurs services à toutes les couches : A Identité et sécurité (chapitre 9), 
B Observabilité, évaluation et FinOps (chapitre 10) et C Gouvernance et registre (chapitre 11).
La règle centrale
La passerelle d’agents joue le rôle d’un poste de contrôle unique : on y vérifie l’identité de l’appelant, son 
droit de passage et le contenu de chaque appel, et l’on peut y fermer le passage d’un geste. Ce patron vient 
de l’architecture à confiance zéro du NIST, où un point d’application des politiques (PEP) ouvre, surveille 
et termine chaque connexion selon la décision d’un moteur de politiques[73]. Le catalogue d’entreprise, lui, 
dit ce qui a le droit d’exister : un outil, une carte d’agent ou un contrat d’événement qui n’y figure pas est 
injoignable.
Cette règle répond à une limite des plateformes : la gouvernance native de chacune s’arrête à sa frontière. 
Des éditeurs de passerelles, MuleSoft et TrueFoundry notamment, en tirent l’argument d’une application 
des politiques au niveau du transport, indépendante du fournisseur et du cadriciel[44, 45]. Le cadre retient le 
principe, sans reprendre de gains chiffrés qui n’ont pas été mesurés de façon indépendante.
EXIG-ARC-01 · DOIT
Passage obligatoire par la passerelle et le catalogue
Dans tout environnement serveur, tout appel d’un agent vers un outil, une ressource ou une invite MCP, 
vers une donnée d’un autre domaine ou vers un autre agent DOIT transiter par la passerelle d’agents et 
viser un élément inscrit au catalogue d’entreprise à une version approuvée (seule exception : un serveur 
MCP local en transport stdio sur un poste de développement, encadré par l’EXIG-MCP-08; les appels 
internes à un même domaine applicatif sans serveur MCP ni pair A2A sont régis par l’EXIG-IAM-17). 
La passerelle DOIT refuser tout appel vers un élément absent du catalogue.
Pourquoi : un point d’application unique est la condition pour authentifier, autoriser, tracer et couper chaque appel; 
un seul chemin de contournement suffit à rendre ces contrôles illusoires.
EXIG-ARC-02 · DOIT
Mandant, trace et plafonds dans chaque appel
Chaque appel descendant DOIT transporter l’identité du mandant (jeton délégué, ou identité de l’agent 
autonome et de son propriétaire), le contexte de trace et les plafonds restants de la tâche (jetons, coût, 
appels d’outils, délai). L’homologation d’un composant incapable de les propager DOIT être refusée.
Pourquoi : ces trois éléments rendent chaque action imputable à une personne, reconstituable après coup et bornée 
dans ses effets et son coût; il suffit d’un maillon qui les perd pour rompre toute la chaîne.
Des rôles, pas des produits
Chaque boîte de figure 3 désigne un rôle. Un même produit peut en remplir plusieurs : Amazon Bedrock 
AgentCore, par exemple, réunit des services modulaires distincts pour l’exécution, la mémoire, la passerelle, 
l’identité, la politique, l’observabilité et le registre, utilisables séparément avec tout cadriciel[102]. À l’inverse, 
un rôle peut exiger plusieurs produits. La section 5.4 établit la correspondance entre rôles et produits.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 33 sur 283


---
## [Page PDF 34]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
5.2 Responsabilités et règles par couche
Cette section fixe, pour chaque couche, ce qu’elle fait, ce qu’elle ne fait pas et les exigences qui en découlent. 
Le fonctionnement détaillé des composants relève des chapitres thématiques indiqués en renvoi.
Couche 1 — Canaux et déclencheurs
La couche 1 capte l’intention, diffuse les réponses en continu et affiche les formulaires d’approbation 
humaine. Elle authentifie la personne ou le système déclencheur, établit le mandant et ouvre la trace, mais 
ne décide de rien d’autre : elle ignore quel modèle sera appelé et quels outils seront employés. Un agent 
ambiant, qui réagit à un flux d’événements plutôt qu’à une personne, y est raccordé par un déclencheur 
(par exemple une tâche planifiée qui vérifie périodiquement les nouveaux événements)[86]. Les patrons 
d’interaction humaine propres à ces agents sont traités à la section 8.6.
EXIG-ARC-03 · NE DOIT PAS
Aucune logique d’agent dans les canaux
Le code d’un canal (application Web, robot de clavardage, webhook, planificateur) NE DOIT PAS 
contenir d’invite, de choix de modèle, de séquence d’appels d’outils ni de logique d’orchestration; il 
transmet l’intention à la couche 2 et affiche ce qu’elle renvoie.
Pourquoi : une logique d’agent dispersée dans les canaux échappe au registre, aux évaluations et aux mises à jour; 
un même processus doit se comporter de la même façon, qu’on l’appelle d’un portail ou d’un outil de collaboration.
EXIG-ARC-04 · DOIT
Mandant établi et trace ouverte à l’entrée
Tout déclencheur DOIT établir le mandant de la demande, soit la personne authentifiée, soit, pour 
un déclencheur système, l’identité du service et son propriétaire nommé. Il DOIT aussi ouvrir ou 
poursuivre une trace conforme à W3C Trace Context avant de transmettre la demande[103].
Pourquoi : sans mandant établi à l’entrée, ni la délégation ni le filtrage des droits ne sont possibles plus bas; sans 
trace dès l’origine, la chaîne ne peut être reconstituée (section 10.1).
Couche 2 — Orchestration et état
La couche 2 décide du chemin. Un routeur sémantique qualifie l’intention et choisit soit un flux déterministe, 
soit un agent; un moteur d’exécution durable conduit la tâche, conserve son état, attend les approbations 
et déclenche les compensations; la coordination entre agents passe par A2A. L’exécution durable signifie 
qu’une tâche reprend là où elle s’était arrêtée après une panne ou un redéploiement. Temporal, par exemple, 
poursuit une exécution jusqu’à son terme sans limite de temps imposée et la reprend en rejouant son histo­
rique d’événements[81]. Les flux Standard d’AWS Step Functions durent jusqu’à un an avec une sémantique 
d’exécution exactement une fois, alors que les flux Express, limités à cinq minutes, s’exécutent au moins 
une fois en mode asynchrone (au plus une fois en mode synchrone) et sont mieux adaptés aux actions 
idempotentes[104].
La persistance ne garantit pas, à elle seule, qu’une action ne sera pas répétée : à la reprise après une inter­
ruption, LangGraph réexécute le nœud depuis son début[82]. L’idempotence des effets reste donc nécessaire 
(section 7.4 et section 7.6).
EXIG-ARC-05 · DOIT
Exécution durable des tâches à effets
Toute tâche qui produit un effet en écriture, attend une approbation humaine ou s’étend sur plus d’un 
échange DOIT s’exécuter sous un moteur d’exécution durable qui persiste l’état hors du processus 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 34 sur 283


---
## [Page PDF 35]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
après chaque transition. Hors du poste de développement, l’état d’une telle tâche DOIT résider dans le 
magasin persistant, jamais seulement en mémoire de processus.
Pourquoi : un redémarrage de conteneur ne doit ni perdre une approbation obtenue ni relancer une écriture déjà 
faite; le Centre d’architecture Azure recommande de persister l’état partagé à l’extérieur de la mémoire et d’utiliser 
les points de contrôle[9].
EXIG-ARC-06 · DOIT
Points de contrôle protégés comme des données de production
Les magasins d’état et de points de contrôle DOIVENT être protégés comme des données de production 
(contrôle d’accès, chiffrement, contrôle d’intégrité). Un orchestrateur DOIT refuser de reprendre une 
exécution à partir d’un point de contrôle dont la provenance n’est pas vérifiée.
Pourquoi : un point de contrôle contient l’état complet de la tâche; la documentation de Microsoft Agent Framework 
qualifie son stockage de frontière de confiance[105].
EXIG-ARC-07 · NE DOIT PAS
Le routage n’accorde aucun droit
Le routeur sémantique et l’orchestrateur NE DOIVENT PAS accorder ni élargir de droits : ils choi­
sissent un chemin, mais chaque appel qui en découle reste soumis à l’autorisation de la passerelle selon 
le mandant et le palier de l’outil.
Pourquoi : le routage repose souvent sur un modèle, donc sur une sortie probabiliste et manipulable; une intention 
mal qualifiée ou injectée doit mener à un refus, jamais à une élévation de privilèges (section 9.6).
Couche 3 — Agents et exécution cognitive
La couche 3 exécute la boucle locale de chaque agent : raisonner, agir au moyen d’un outil, observer le 
résultat. Chaque agent s’exécute dans un environnement d’exécution indépendant du fournisseur de modèle, 
encadré par deux composants partagés. La passerelle de modèles centralise les identifiants des fournisseurs, 
le routage entre modèles, l’équilibrage de charge, le cache, le repli et les quotas de jetons. Agent Router, 
projet de l’AAIF anciennement nommé Envoy AI Gateway, illustre ce rôle : les développeurs y trouvent une 
interface unique vers les modèles, pendant que l’équipe plateforme y centralise fournisseurs, identifiants, 
quotas, routage et basculement[36, 106]. Le bac à sable, quant à lui, exécute en isolement le code que l’agent 
produit (section 9.7).
EXIG-ARC-08 · DOIT
Passerelle de modèles obligatoire
Tout appel d’inférence DOIT passer par la passerelle de modèles de l’entreprise. Un agent DOIT 
n’accéder aux modèles que par cette passerelle, sans détenir de clé de fournisseur de modèles ni appeler 
un fournisseur directement.
Pourquoi  : c’est le seul endroit où l’on peut appliquer des quotas de jetons (comme le fait la politique 
llm-token-limit d’Azure API Management[107]), imputer les coûts, changer de fournisseur et révoquer un accès 
sans toucher aux agents.
EXIG-ARC-09 · DEVRAIT
Modèles désignés par un alias logique
Un agent DEVRAIT désigner ses modèles par un alias logique que la passerelle résout, de sorte qu’un 
changement de modèle ou de fournisseur s’effectue par configuration, suivi d’une réévaluation (section 
10.4), sans modification du code de l’agent.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 35 sur 283


---
## [Page PDF 36]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Pourquoi : les modèles changent plus vite que les agents; l’alias isole l’agent de ces changements, tandis que la 
télémétrie consigne la version réellement servie.
EXIG-ARC-10 · DOIT
Code généré exécuté en bac à sable
Le code qu’un agent produit ou choisit dynamiquement DOIT s’exécuter dans un bac à sable éphémère 
et isolé, sans accès réseau par défaut ni accès aux secrets, selon les exigences de la section 9.7; jamais 
dans le processus de l’agent ni sur son hôte.
Pourquoi : l’OWASP range l’exécution de code inattendue parmi les dix principaux risques des applications agen­
tiques (ASI05 Unexpected Code Execution)[28].
Couche 4 — Médiation et connectivité
La couche 4 masque le paysage applicatif derrière des contrats uniformes. Elle réunit trois rôles : la passerelle 
d’agents, mandataire inverse devant les serveurs MCP et les pairs A2A; le catalogue d’entreprise, source 
unique de ce qui est joignable; le bus d’événements, pour les échanges découplés dans le temps (section 
6.7). Le rôle de passerelle est réalisable avec des produits documentés : Azure API Management expose et 
gouverne des serveurs MCP et des API d’agents A2A, et Amazon Bedrock AgentCore Gateway sert de point 
d’entrée unique aux outils, aux agents et aux modèles[108, 109, 110]. Une passerelle relaie toutefois le trafic A2A 
sans assumer l’état des tâches : le greffon AI A2A Proxy de Kong Gateway (3.14 et plus, édition AI Gateway 
Enterprise), par exemple, ne modifie pas le routage et ne gère pas cet état[111]. L’état reste du ressort de 
l’agent ou de l’orchestrateur.
EXIG-ARC-11 · DOIT
Passerelle d’agents dans les deux sens
Dans tout environnement serveur, la passerelle d’agents DOIT s’interposer devant tous les serveurs 
MCP, internes et externes, et devant tous les pairs A2A, pour le trafic interdomaine comme pour celui 
qui entre dans l’entreprise ou qui en sort, et réévaluer l’autorisation à chaque appel. Ses fonctions 
obligatoires sont fixées à la section 9.4.
Pourquoi : l’agent d’un partenaire qui appelle l’entreprise et un agent interne qui appelle un SaaS franchissent la 
même frontière de confiance; la confiance zéro vise des décisions d’accès au moindre privilège prises requête par 
requête et une confiance réévaluée en continu pendant la session, et non une confiance acquise une fois pour toute 
la durée d’une session[112].
EXIG-ARC-12 · DOIT
Liste d’autorisation tirée du catalogue
La passerelle DOIT tirer sa liste d’autorisation du catalogue d’entreprise, seule source des outils, cartes 
d’agent et contrats d’événements joignables, avec leur version et leur empreinte approuvées (section 
6.8). Aucune liste propre à un projet ne fait foi.
Pourquoi : deux listes finissent toujours par diverger; une source unique permet de retirer partout, en une seule 
opération, un outil compromis.
EXIG-ARC-13 · DOIT
Aucun contournement par le bus d’événements
Tout sujet ou canal d’événements produit ou consommé par un agent DOIT être inscrit au catalogue 
avec son contrat, et ses producteurs comme ses consommateurs DOIVENT s’authentifier auprès du bus.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 36 sur 283


---
## [Page PDF 37]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Pourquoi : le bus est l’autre voie d’accès aux systèmes; s’il échappe au catalogue, un simple abonnement suffit à 
contourner la règle centrale.
Couche 5 — Outils et données
La couche 5 expose les capacités de l’entreprise sous forme d’outils et de ressources : serveurs MCP de 
domaine, adaptateurs qui traduisent une API existante en outils, index et graphes de connaissances, et outils 
de compensation qui défont ou corrigent une action (section 7.5). Des produits convertissent déjà des API 
en outils sans toucher aux services : AgentCore Gateway transforme des API OpenAPI ou Smithy et des 
fonctions Lambda en outils MCP, et IBM ContextForge virtualise des services REST ou gRPC en MCP[110, 113].
Un bon outil n’est pas le miroir d’un point de terminaison. Anthropic recommande de choisir délibérément 
les outils plutôt que d’envelopper chaque point de terminaison d’une API, de regrouper les opérations en 
plusieurs étapes et de renvoyer un contexte signifiant plutôt que des identifiants techniques[114]. OpenAI 
propose de vérifier qu’une personne pourrait utiliser la fonction avec la seule information fournie[115]. Ainsi, 
plutôt que trois outils « lire le client », « lire les factures » et « lire les paiements », on expose un outil 
consulter_situation_compte qui rend la synthèse utile à la tâche.
EXIG-ARC-14 · DOIT
Exposition sans réécriture des services
Les capacités existantes DOIVENT être exposées aux agents par des serveurs MCP ou des adaptateurs 
placés devant les API en place, sans réécriture des services d’origine.
Pourquoi : l’intégration agentique s’ajoute au patrimoine applicatif sans le déstabiliser, et les règles métier restent 
là où elles sont déjà testées.
EXIG-ARC-15 · DEVRAIT
Outils conçus pour la tâche
Les outils DEVRAIENT être conçus selon les tâches des agents (opérations regroupées, réponses 
paginées et filtrées, contexte signifiant) plutôt que de reproduire un à un les points de terminaison d’une 
API; les règles de conception détaillées figurent à la section 6.5.
Pourquoi : chaque outil superflu consomme du contexte et accroît les erreurs de sélection (section 7.3).
EXIG-ARC-16 · DOIT
Résultats filtrés selon les droits du mandant
Un outil DOIT filtrer ses résultats selon les droits du mandant, de sorte qu’aucun agent ne reçoive une 
donnée que le mandant ne pourrait pas consulter lui-même.
Pourquoi : le Centre d’architecture Azure demande ce filtrage de sécurité (security trimming) dans chaque agent[9]; 
le cadre le place à la source, dans l’outil, où il ne dépend pas du comportement d’un modèle.
Couche 6 — Systèmes d’enregistrement
La couche 6 regroupe les systèmes qui font foi : ERP, CRM, systèmes de dossiers, entrepôts de données et 
SaaS. Ils sont exposés aux agents tels quels. L’entreprise agentique ne les remplace pas et ne les contourne 
pas : elle les appelle par leurs interfaces, sous leurs propres contrôles.
EXIG-ARC-17 · DOIT
Écriture par les interfaces qui appliquent les règles métier
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 37 sur 283


---
## [Page PDF 38]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Un agent DOIT écrire dans un système d’enregistrement uniquement par une interface qui applique les 
contrôles métier de ce système (API ou service métier), sans accès direct aux tables ni compte technique 
qui contourne ces contrôles.
Pourquoi : validations, séparation des tâches et journaux du système d’enregistrement sont des contrôles éprouvés; 
un agent qui les contourne annule cette assurance.
EXIG-ARC-18 · DEVRAIT
Écritures corrélées et idempotentes
Chaque écriture d’agent dans un système d’enregistrement DEVRAIT porter une référence de trace 
que le système cible conserve avec l’opération, en plus de la clé d’idempotence qu’exige l’EXIG-ORC-21 
(section 7.6).
Pourquoi : lors d’un incident, on doit pouvoir remonter d’une ligne de l’ERP à la trace de l’agent qui l’a créée, et une 
reprise ne doit jamais créer de doublon.
5.3 Plans transversaux
Les trois plans transversaux fournissent à toutes les couches des services communs, conçus une fois et 
consommés partout; tableau 11 indique ce que chacun apporte à chaque couche.
A — Identité et sécurité. Chaque agent reçoit une identité propre, délivrée par une infrastructure d’identité 
de charge de travail comme SPIFFE/SPIRE, projets diplômés de la Cloud Native Computing Foundation 
(CNCF)[116, 117], ou par fédération OpenID Connect (OIDC) infonuagique. Lorsqu’il agit pour une personne, 
il obtient un jeton délégué par échange de jetons (RFC 8693)[118]; le cadre exige que ce jeton soit de courte 
durée. Le plan fournit aussi le moteur de politiques, les paliers d’outils, le coffre de secrets, les garde-fous 
et l’approbation humaine signée (chapitre 9 et section 8.5).
B — Observabilité, évaluation et FinOps. Les couches 1 à 5 émettent des traces OpenTelemetry reliées 
par un même contexte W3C Trace Context[103], selon une version épinglée des conventions GenAI, qui 
distinguent notamment les spans invoke_workflow, invoke_agent et execute_tool [119, 120]. S’y ajoutent le 
journal d’audit inaltérable, distinct des traces, l’évaluation continue et la mesure du coût par tâche réussie 
(chapitre 10).
C — Gouvernance et registre. Le registre des agents et des serveurs MCP porte la classe de risque, le 
niveau d’autonomie (N0 à N4), le propriétaire et l’état du cycle de vie de chaque agent (chapitre 11). Les 
plans de contrôle des éditeurs couvrent une partie de ce rôle, sans le couvrir entièrement : Microsoft Agent 
365, en disponibilité générale depuis le 1er mai 2026, offre un registre et des contrôles comme le blocage des 
agents non gérés, mais les actions de cycle de vie sur des agents infonuagiques tiers y sont encore annoncées 
comme à venir[46]. D’où l’exigence d’un coupe-circuit appliqué à la passerelle, quel que soit l’éditeur de 
l’agent (section 9.4).
Tableau 11 — Apport des plans transversaux à chaque couche
Couche
A — Identité et sécurité
B — Observabilité, éva­
luation, FinOps
C — Gouvernance et registre
1. Canaux et déclen­
cheurs
Authentification de la per­
sonne ou du service; établis­
sement du mandant
Ouverture de la trace; la­
tence perçue
Canaux autorisés par agent; avis à 
la personne qu’elle interagit avec un 
agent (section 12.7)
2. Orchestration et état
Jeton délégué de la tâche; 
approbations humaines si­
gnées
Spans de flux; enveloppe 
budgétaire de la tâche
Patron d’orchestration et niveau 
d’autonomie déclarés
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 38 sur 283


---
## [Page PDF 39]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Couche
A — Identité et sécurité
B — Observabilité, éva­
luation, FinOps
C — Gouvernance et registre
3. Agents et exécution 
cognitive
Identité propre par agent; 
garde-fous d’entrée et de 
sortie
Spans d’agent et 
d’inférence; jetons et coût 
par appel; évaluation 
continue
Versions de l’agent et du modèle ins­
crites; classe de risque
4. Médiation et connec­
tivité
Point d’application des poli­
tiques; coupe-circuit
Journalisation de chaque 
appel; propagation du 
contexte de trace
Catalogue, versions épinglées, liste 
d’autorisation
5. Outils et données
Portées par outil; jetons à au­
dience unique; secrets injec­
tés hors de l’agent
Spans d’outil; erreurs par 
outil
Palier P0 à P3, propriétaire, compensa­
tion déclarée
6. Systèmes 
d’enregistrement
Contrôles d’accès natifs 
conservés
Corrélation par réfé­
rence de trace et clé 
d’idempotence
Classification des données; EFVP pour 
tout projet d’acquisition, de dévelop­
pement ou de refonte de système im­
pliquant des RP, et avant leur commu­
nication hors Québec (section 12.2)
EXIG-ARC-19 · DOIT
Services transversaux mutualisés
Les services des plans transversaux (identité des agents, moteur de politiques, coffre de secrets, collecte 
de télémétrie, journal d’audit, registre) DOIVENT être fournis par l’équipe plateforme et consommés 
par toutes les couches. Un projet DOIT obtenir une dérogation pour en déployer un équivalent parallèle 
(section 11.6).
Pourquoi : un registre ou une chaîne de télémétrie parallèle crée un angle mort que ni le comité ni l’équipe de garde 
ne voient.
5.4 Blocs de construction
Cette section relie les rôles de l’architecture aux produits qui peuvent les remplir. Le cadre reprend la 
distinction de TOGAF : les blocs de construction d’architecture (ABB) capturent les exigences et orientent 
le développement des blocs de construction de solution (SBB); les SBB désignent les produits et composants 
qui mettent en œuvre la fonction et dépendent du produit ou du fournisseur[121]. Le passage des uns aux 
autres est itératif : les ABB se définissent surtout aux phases A à D de la méthode de développement 
d’architecture (ADM), puis se raffinent en SBB, dont l’identification relève surtout de la phase E[121]. 
Concrètement, « passerelle d’agents » est un ABB neutre et durable; le produit retenu pour la réaliser est 
un SBB remplaçable.
EXIG-ARC-20 · DOIT
Correspondance ABB-SBB documentée
Toute solution agentique présentée à l’homologation DOIT documenter la correspondance entre les 
ABB de tableau 12 et les SBB qu’elle emploie. L’homologation DOIT être refusée tant qu’un ABB de 
tableau 12 nécessaire à la solution n’a pas de SBB désigné.
Pourquoi : la correspondance révèle les rôles orphelins, par exemple un agent sans passerelle de modèles, avant 
qu’ils ne deviennent des incidents.
EXIG-ARC-21 · DOIT
SBB exposés par les standards retenus
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 39 sur 283


---
## [Page PDF 40]

CRE-IA-2026-01 · Cadre de référence
5 Architecture de référence
Un SBB DOIT exposer ses fonctions d’interopérabilité par les standards retenus au catalogue des 
protocoles (section 6.3), de sorte qu’on puisse le remplacer sans réécrire les agents. Une fonction offerte 
seulement par une interface propriétaire exige une dérogation.
Pourquoi : le risque de verrouillage s’est déplacé des protocoles vers les plateformes et leurs extensions (section 13.1).
Les exemples du tableau sont non limitatifs et établis au 27 octobre 2026. Ils ne constituent ni une exigence 
ni une recommandation d’achat; le comité les révise chaque trimestre, avec le catalogue des protocoles 
(section 11.7).
Tableau 12 — Correspondance des blocs de construction d’architecture (ABB) et des blocs de construction de solution (SBB)
Couche
ABB
Capacités exigées
Exemples de SBB (non limitatifs, état au 
27 octobre 2026)
1. Canaux et déclen­
cheurs
Interface conversationnelle 
et d’approbation; déclen­
cheurs système
Authentifier, établir le 
mandant, ouvrir la trace, 
diffuser en continu, 
montrer l’action exacte 
à approuver
Portails et outils de collaboration existants; 
canaux intégrés des plateformes SaaS (der­
nière ligne); webhooks et planificateurs
2. Orchestration et état
Moteur d’exécution du­
rable; orchestrateur et rou­
teur; magasin d’état
Persistance après 
chaque transition, 
reprise, attente 
d’approbation, compen­
sation
Temporal, dont l’intégration avec l’OpenAI 
Agents SDK est en disponibilité générale 
depuis le 23 mars 2026[122]; AWS Step 
Functions; LangGraph 1.0 avec persistance 
intégrée de l’état d’exécution (checkpoin­
ter)[123, 124]; Microsoft Agent Framework 
1.0[125]; agents de flux de Google ADK[126]
3. Agents et exécution 
cognitive
Environnement d’exécution 
d’agents
Boucle d’agent, appels 
MCP et A2A, télémé­
trie OpenTelemetry, in­
dépendance du modèle
OpenAI Agents SDK (boucle d’agent, MCP, 
traçage intégré et fournisseurs non Ope­
nAI; A2A et OpenTelemetry non documen­
tés), Strands Agents, Google ADK, Micro­
soft Agent Framework, LangGraph[127, 128, 
129]; AgentCore Runtime
3. Agents et exécution 
cognitive
Passerelle de modèles
Identifiants centralisés, 
routage, repli, cache, 
quotas de jetons, impu­
tation des coûts
Agent Router (AAIF)[130]; fonction de passe­
relle de modèles d’agentgateway[131]; Kong 
AI Gateway[132]; Azure API Management
3. Agents et exécution 
cognitive
Bac à sable de code
Isolation par microVM, 
noyau applicatif ou 
environnement WebAs­
sembly sans autorité 
ambiante, réseau fermé 
par défaut, exécution 
éphémère
MicroVM Firecracker[133]; gVisor[134]; Kata 
Containers[135]; WebAssembly et WASI[136]; 
agent-sandbox pour Kubernetes[137]
4. Médiation et connec­
tivité
Passerelle d’agents (PEP 
pour MCP et A2A)
Mandataire inverse, au­
torisation par appel, 
garde-fous, plafonds, 
journalisation, coupe-
circuit
agentgateway, projet de l’AAIF sous licence 
Apache 2.0[31]; Azure API Management 
(outils MCP seulement, agents A2A en 
JSON-RPC seulement)[108, 109]; AgentCore 
Gateway[110]; Kong AI Gateway[132]; Mule­
Soft Agent Fabric et sa passerelle Flex 
Gateway[138]; IBM ContextForge (licence 
Apache 2.0; modèle de soutien non pré­
cisé par le projet); portails MCP de Cloud­
flare[139]
4. Médiation et connec­
tivité
Catalogue d’entreprise et 
registre privé
Source unique des ou­
tils, cartes et contrats; 
versions et empreintes; 
cycle de vie
Azure API Center; AgentCore Registry (pu­
blication, revue et approbation)[102]; Agent 
Registry de MuleSoft Agent Fabric
4. Médiation et connec­
tivité
Bus d’événements
Enveloppe CloudEvents, 
contrats AsyncAPI, ré­
tention et rejeu
Apache Kafka, qui garantit par défaut une 
livraison au moins une fois[140]; services in­
fonuagiques équivalents
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 40 sur 283


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
