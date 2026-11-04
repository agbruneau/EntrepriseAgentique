# chunk_11 — pages PDF 101 à 112 (sur 283)



---
## [Page PDF 101]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Anti-patron
Pourquoi il est proscrit
Correctif exigé
État mutable partagé entre agents concur­
rents
Écritures contradictoires et résultats 
non reproductibles
Écrivain unique (EXIG-ORC-07); état 
d’exécution dans un magasin externe 
(EXIG-ORC-11)
Latence multisaut et contraintes de res­
sources ignorées
Délais cumulés et pointes de charge 
en mode concurrent
Délais par étape (EXIG-ORC-27), limite 
de concurrence (EXIG-ORC-07), plafonds 
(EXIG-ORC-26)
Contexte qui enfle sans contrôle, historique 
brut versé au contexte
Le rappel se dégrade quand 
l’information pertinente est noyée[148]
Compaction et références (EXIG-ORC-23, 
section 5.5)
État d’exécution en mémoire du processus
Perte de l’état au redémarrage[124]
Magasin durable (EXIG-ORC-11)
Maillage libre sans plafond de tours
Boucles, dérive, coûts imprévisibles
Patron déclaré et plafonds (EXIG-ORC-06, 
EXIG-ORC-26)
Chaîne d’écritures sans compensation ni clé 
d’idempotence
Effets partiels ou doublés impos­
sibles à défaire
Saga et idempotence (section 7.5 et sec­
tion 7.6)
Vérificateur qui déclare le succès sur 
quelques tests
Victoire prématurée[275]
Critères concrets, tests négatifs, suite 
complète (EXIG-ORC-05)
EXIG-ORC-29 · NE DOIT PAS
Aucun anti-patron sans dérogation
Une conception NE DOIT PAS présenter l’un des anti-patrons du tableau 26. La revue d’architecture 
DOIT les vérifier un à un et consigner le résultat à la fiche de l’agent, avec la décision d’homologation; 
tout écart exige une dérogation (section 11.6).
Pourquoi : une part importante des défaillances des systèmes multiagents tient à la conception du système et à la 
coordination entre agents[292].
7.10 Cadriciels et plateformes d’orchestration
Cette section situe les principaux produits par rapport aux exigences du chapitre. Seule l’exigence 
EXIG-ORC-30 y est normative; le tableau 27 ne l’est pas : les produits cités sont des exemples non limitatifs, 
décrits selon leur état au 27 octobre 2026, et le catalogue d’entreprise les réévalue chaque trimestre. On 
distingue trois familles : les cadriciels, qui portent la logique propre à l’entreprise; les moteurs d’exécution 
durable, qui en garantissent la reprise; et les plateformes SaaS, à privilégier lorsque le travail réside déjà 
dans leur système d’enregistrement.
Tableau 27 — Cadriciels, moteurs et plateformes d’orchestration (exemples non limitatifs, état au 27 octobre 2026)
Produit
Nature et modèle d’orchestration
Atouts au regard du cadre
Points d’attention
LangGraph 
(LangChain)
Cadriciel d’exécution à base de 
graphe, avec persistance intégrée de 
l’état; version 1.0 du 22 octobre 2025, 
sans changement incompatible pro­
mis jusqu’à la 2.0 (persistance par 
fil : documentation « Persistence » de 
LangGraph)[123, 124]
Points de contrôle, interrupt() 
pour l’approbation, voyage 
dans le temps[82, 283]
Nœud réexécuté à la reprise; 
magasin persistant exigé en 
production[82, 124]
Microsoft Agent 
Framework
Cadriciel sous licence MIT, successeur 
de Semantic Kernel et d’AutoGen; ver­
sions 1.0.0 pour Python et .NET le 2 
avril 2026[85, 293]
Orchestrations séquentielle, 
concurrente, clavardage de 
groupe, transfert et magné­
tique; traces OpenTelemetry 
GenAI[294, 295]
Magasin de points de contrôle 
à protéger comme frontière de 
confiance[105]
CrewAI
Cadriciel combinant des Flows (état, 
événements, embranchements) et des 
Crews (équipes d’agents à rôles)[296]
Démarche recommandée par 
l’éditeur : partir d’un Flow et 
y insérer une Crew pour une 
étape collaborative, ce qui re­
joint le flux déterministe du 
cadre
Persistance et reprise à dé­
montrer en preuve de concept 
(EXIG-ORC-30)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 101 sur 283


---
## [Page PDF 102]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Produit
Nature et modèle d’orchestration
Atouts au regard du cadre
Points d’attention
OpenAI Agents 
SDK
Trousse à peu de primitives : agents, 
transferts ou agents utilisés comme 
outils, garde-fous, sessions, traçage; 
outils MCP natifs[127]
Intégration Temporal en dispo­
nibilité générale depuis le 23 
mars 2026 : chaque invocation 
d’agent devient une activité[122]
Associer un moteur durable dès 
que le flux compte plusieurs 
étapes (EXIG-ORC-11)
Google ADK
Cadriciel ouvert en Python, TypeScript, 
Go, Java et Kotlin, indépendant du 
modèle et du lieu de déploiement; 
A2A et MCP[126]
Agents de flux SequentialAgent, 
ParallelAgent et LoopAgent, 
sans décision du modèle sur 
l’orchestration[297]
ADK 2.0 supplante ces gabarits, 
en Python et en Go, par des 
flux à base de graphes ou dyna­
miques, sans annoncer leur re­
trait : prévoir la migration[297]
Strands Agents 
(AWS)
Trousse sous licence Apache 2.0, pu­
bliée le 16 mai 2025, pilotée par le 
modèle[128]
MCP, télémétrie OpenTeleme­
try, patrons multiagents (agents 
comme outils, essaim, graphe, 
flux, A2A)
Réserver aux tâches ouvertes à 
autonomie bornée; moteur du­
rable dès que le flux compte 
plusieurs étapes (EXIG-ORC-11)
Temporal
Moteur d’exécution durable; reprise à 
partir du dernier événement consigné 
dans l’historique d’événements (rejeu)
[80, 81]
Compensations exécutées 
même après la défaillance d’un 
travailleur[286]
Isoler appels de modèles et 
d’outils dans des activités 
(EXIG-ORC-12)
AWS Step Func­
tions
Service géré de machines à états
Flux Standard d’une durée 
maximale d’un an, à séman­
tique d’exécution exactement 
une fois, sauf réessais décla­
rés[104]
Flux Express (5 minutes; au 
moins une fois en mode 
asynchrone, au plus une fois 
en mode synchrone) : actions 
idempotentes obligatoires en 
mode asynchrone
Microsoft Copi­
lot Studio
Plateforme à faible code; orchestra­
tion multiagent annoncée en pré­
version le 19 mai 2025 (Micro­
soft Build), dont plusieurs capacités 
passent en disponibilité générale à 
compter d’avril 2026[298, 299]
MCP en disponibilité générale 
depuis le 29 mai 2025, A2A de­
puis avril 2026[48, 300]
Identité Entra Agent ID créée 
pour chaque nouvel agent de­
puis juillet 2026 : l’inscrire au 
registre d’entreprise[48]
Salesforce 
Agentforce
Plateforme SaaS; orchestration SO­
MA (Single-Org, Multi-Agent) (une 
organisation Salesforce) et MOMA 
(Multi-Org, Multi-Agent) (plusieurs or­
ganisations)[49]
A2A entrant et sortant; client 
MCP et serveur MCP hébergé
Contraintes de produit : un seul 
niveau de délégation en MO­
MA; sept sous-agents connectés 
pour Agent Script, limite que 
l’éditeur qualifie d’actuelle
ServiceNow
Plateforme SaaS; AI Agent Fabric 
(annoncé le 6 mai 2025), couche 
d’échange par MCP et A2A; AI Control 
Tower en disponibilité générale le 
même jour[51]
Action Fabric expose les ac­
tions de la plateforme à tout 
agent d’IA par un serveur MCP, 
pour des actions sécurisées et 
gouvernées (annonce du 5 mai 
2026)[50]
Extensions de l’AI Control To­
wer (coupe-circuit, mesure des 
coûts) annoncées pour août 
2026 : vérifier selon la version 
déployée[47]
EXIG-ORC-30 · DOIT
Capacités démontrées avant l’inscription d’un produit
Un cadriciel, un moteur ou une plateforme d’orchestration DOIT, avant son inscription au catalogue, 
démontrer en preuve de concept, dans les conditions de l’entreprise : la persistance durable des points 
de contrôle et la reprise après panne; la pause pour approbation humaine sans perte d’état; l’émission 
de traces OpenTelemetry selon les conventions GenAI; la prise en charge de MCP et d’A2A, nativement 
ou par adaptateur; l’export des définitions de flux et de l’état dans un format documenté.
Pourquoi : l’entreprise garde la propriété de sa logique d’orchestration (PRIN-09), et une capacité se vérifie au lieu 
de se présumer sur la foi d’une fiche commerciale (chapitre 13).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 102 sur 283


---
## [Page PDF 103]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
8 Autonomie et supervision humaine
L’autonomie d’un agent n’est pas une propriété du modèle : c’est une décision d’architecture, prise par une 
personne imputable, inscrite au registre et appliquée par la passerelle d’agents. Ce chapitre fixe une échelle 
unique de niveaux (N0 à N4), quatre paliers de risque pour les outils (P0 à P3) et la règle qui les combine. 
Il précise ensuite comment rendre l’approbation humaine vérifiable, comment interagir avec les agents 
qui travaillent en arrière-plan, comment éviter l’approbation machinale et comment traiter les décisions 
automatisées visées par la Loi 25.
8.1 Une échelle unique N0 à N4
Le cadre adopte une seule échelle d’autonomie (figure 14 et tableau 28), que chaque agent déclare et que la 
plateforme fait respecter.
Deux constats la fondent. D’abord, l’autonomie est un choix de conception : Feng, McDonald et Zhang 
(2025) la distinguent de la capacité du modèle et de son environnement, et la définissent par le rôle 
laissé à l’utilisateur[83]. Ensuite, une gouvernance uniforme échoue : selon Gartner (26 mai 2026), la cause 
profonde des échecs est une gouvernance binaire, qui verrouille tout ou permet tout, et la confusion entre 
la capacité d’agir d’un agent et la portée des accès qui lui sont accordés; la firme prévoit que, d’ici 2027, 40 % 
des entreprises rétrograderont ou désactiveront des agents autonomes après des incidents de production 
révélant des lacunes de gouvernance[95].
Chaque niveau se définit donc par deux éléments observables : le rôle de la personne et l’étendue de ce 
que l’agent peut faire sans approbation. Le niveau ne dépend ni du nombre d’agents ni de la puissance 
du modèle : un système multiagent peut réunir des agents de niveaux différents, et, selon le cadre de 
gouvernance de l’IA agentique de l’Infocomm Media Development Authority (IMDA) de Singapour, l’espace 
d’action d’un agent, c’est-à-dire ses outils, se distingue de son autonomie[76, 83].
Autonomie croissante
contrôles compensatoires croissants
NX
Interdit : l’agent fixe ses objectifs ou ses permissions
N0
Automatisation déterministe
N1
Consultatif
N2
Exécution approuvée
N3
Autonomie bornée
N4
Autonomie étendue
L’AGENT
aucun modèle : flux
codé, règles, RPA, API
lit, analyse, recommande;
aucun effet en écriture
prépare l’action, attend
l’accord pour chaque écriture
exécute seul le réversible
sous seuils, dans un ODD
s’autodéclenche, opère en
continu, ODD certifié
LA PERSONNE
conçoit les règles
et exploite
exécute elle-même
(opératrice)
approuve chaque action
(dans la boucle)
supervise, traite les
exceptions (sur la boucle)
gouverne : politiques,
audit, coupe-circuit
PALIERS D’OUTILS PERMIS
hors IA
P0 et P1 en lecture
P2 et P3 après
approbation signée
P2 sous seuils; P3 après
approbation hors bande
comme N3; P3 toujours
approuvé
CONTRÔLES MINIMAUX
tests logiciels,
revue de code
accès circonscrit, DLP,
essais d’exactitude
points d’arrêt, jeton
d’approbation, audit
budgets, sagas, disjoncteurs,
revue par échantillon
évaluation continue,
retour arrière rapide
PLAFOND PAR CLASSE
risque élevé
risque modéré ou faible
décision du comité
Le niveau est un plafond inscrit au registre, distinct du nombre d’agents et de la capacité du modèle.
Toute action P3 (critique, externe ou irréversible) exige une approbation humaine, quel que soit le niveau.
Figure 14 — Échelle d’autonomie N0 à N4. Chaque marche indique ce que fait l’agent, ce que fait la personne, les paliers d’outils 
permis et les contrôles minimaux; plus l’autonomie croît, plus les contrôles compensatoires s’accumulent. Le niveau NX, hors de l’échelle, 
est interdit. Source : CRE-IA-2026-01, d’après Gartner (2026), AWS, Feng et al. (2025) et l’IMDA.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 103 sur 283


---
## [Page PDF 104]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
Tableau 28 — Niveaux d’autonomie : rôles, paliers permis et contrôles minimaux
Niveau
Ce que fait l’agent
Rôle humain et 
boucle
Paliers per­
mis
Contrôles minimaux 
(cumulatifs)
Exemple
N0 Automatisa­
tion déterministe
Aucun modèle : flux 
codé, règles, RPA, 
API.
Conçoit les règles et 
exploite le flux.
Sans objet
Tests logiciels, revue 
de code, gestion des 
changements.
Rapprochement 
bancaire quoti­
dien codé en 
règles.
N1 Consultatif
Lit, analyse, recom­
mande, rédige; au­
cun effet en écri­
ture.
La personne exécute 
elle-même toute ac­
tion (rôle d’opérateur); 
l’agent ne fait que re­
commander.
P0, P1
Accès aux données 
circonscrit, authentifi­
cation, journalisation 
de l’usage, essais de 
sécurité de base, es­
sais d’exactitude et 
d’hallucination, forma­
tion des utilisateurs à 
une confiance appro­
priée.
Résumé d’un 
dossier et texte 
de réponse af­
fiché à l’écran, 
que le conseiller 
copie, relit et en­
voie lui-même.
N2 Exécution ap­
prouvée
Planifie et prépare; 
chaque action en 
écriture attend une 
approbation expli­
cite.
Approuve chaque 
écriture avant son 
exécution : humain 
dans la boucle (HITL).
P0, P1; P2 et 
P3 après ap­
probation si­
gnée (P3 : 
hors bande)
Essais de sécuri­
té poussés, état de 
la tâche conser­
vé à chaque point 
d’approbation, jeton 
d’approbation, jour­
nal d’audit, procédure 
d’intervention propre 
aux agents.
Modifications de 
fiches fournis­
seurs préparées 
par l’agent, cha­
cune approuvée 
avant l’écriture.
N3 Autonomie 
bornée et supervi­
sée
Exécute seul les ac­
tions P2 réversibles 
ou compensables 
sous seuils décla­
rés, dans un do­
maine de concep­
tion opérationnel 
(ODD) documenté; 
escalade les excep­
tions.
Supervise par excep­
tion, traite les es­
calades, peut inter­
rompre; revue a pos­
teriori par échantillon­
nage : humain sur la 
boucle (HOTL).
P0, P1; P2 
sous seuils; P3 
après appro­
bation hors 
bande
Surveillance continue, 
seuils et budgets ap­
pliqués par la pas­
serelle, compensation 
déclarée, disjoncteurs, 
retour arrière ra­
pide, propriété claire 
du comportement de 
l’agent.
Agent de soutien 
TI qui classe, fu­
sionne et ferme 
les billets en 
double sous un 
plafond horaire, 
et escalade le 
reste.
N4 Autonomie 
étendue sous 
ODD certifié
S’autodéclenche 
sur des événements 
et opère en conti­
nu.
Hors de la boucle 
d’exécution, mais sur 
la boucle de gouver­
nance : politiques, au­
dit, coupe-circuit.
Comme N3; 
P3 toujours 
approuvé
ODD certifié, évalua­
tion continue, arrêts 
ciblé et général tes­
tés, réautorisation pé­
riodique, décision du 
comité.
Agent de qualité 
des données qui, 
sur alerte, met 
en quarantaine 
les lots suspects 
jour et nuit.
NX Autonomie 
non bornée
Fixe ses objectifs, 
modifie ses permis­
sions, écrit et exé­
cute du code hors 
contraintes.
Aucun contrôle hu­
main effectif.
—
Interdit
—
Les contrôles des niveaux N1 à N3 s’inspirent de ceux que Gartner associe à ses niveaux Observer, Conseiller, 
Agir avec approbation et Agir de façon autonome (Gartner précise que ceux du niveau Conseiller incluent 
tous ceux du niveau Observer; le cumul aux niveaux suivants est le choix du cadre); Gartner prévient 
d’ailleurs que les approbations peuvent s’affaiblir sous la pression du temps ou la fatigue d’approbation[95]. 
Les contrôles de N0 et de N4 sont fixés par le cadre. Le sigle ODD (domaine de conception opérationnel, 
operational design domain) est un concept de la conduite automatisée des véhicules routiers[301]; le cadre 
l’emploie pour désigner le périmètre documenté (systèmes, données, outils, seuils, plages horaires) hors 
duquel l’agent s’arrête ou escalade.
L’échelle n’est pas un parcours de maturité dont N4 serait le but. Morris et al. rappellent que le niveau 
d’autonomie retenu au déploiement n’a pas à être le maximum que permettent les capacités du modèle[302], 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 104 sur 283


---
## [Page PDF 105]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
et l’OWASP formule le principe de moindre agence (Least-Agency) : un comportement agentique déployé 
sans nécessité élargit la surface d’attaque sans ajouter de valeur[28]. Le bon niveau est le plus bas qui atteint 
l’objectif.
EXIG-AUT-01 · DOIT
Niveau d’autonomie déclaré et appliqué
Chaque agent DOIT avoir un niveau d’autonomie N0 à N4 (tableau 28) inscrit au registre (section 11.4) 
comme plafond, avec la date d’homologation et le nom de la personne qui l’a approuvé. Le niveau 
déclaré DOIT être le plus bas qui permet d’atteindre l’objectif métier, avec sa justification consignée 
dans la fiche d’agent. La passerelle d’agents DOIT refuser tout appel d’outil qui excède ce plafond.
Pourquoi : le principe de moindre agence de l’OWASP proscrit l’autonomie inutile[28]; Feng et al. proposent un 
« certificat d’autonomie » qui fixe le niveau maximal d’un agent et accompagne ses métadonnées[83].
EXIG-AUT-02 · DOIT
Plafond selon la classe de risque
Le niveau déclaré DOIT être évalué selon les critères du tableau 30 et respecter le plafond que fixe 
EXIG-CON-02 pour la classe de risque de l’agent (section 12.1, tableau 46).
Pourquoi : le RIA exige des mesures de contrôle humain proportionnées aux risques, au niveau d’autonomie et au 
contexte d’utilisation (art. 14, par. 3)[290]; les plafonds eux-mêmes sont un choix du cadre.
EXIG-AUT-03 · NE DOIT PAS
Autonomie non bornée interdite (NX)
Un agent NE DOIT PAS fixer d’autres objectifs que ceux qui lui sont assignés au registre, modifier 
ses propres permissions ou son niveau d’autonomie, ni écrire et exécuter du code hors des contraintes 
déclarées. Toute modification des objectifs, des outils ou du niveau d’un agent DOIT passer par le 
registre et être approuvée par une personne habilitée, la décision étant consignée au registre. Aucune 
dérogation n’est possible.
Pourquoi : choix normatif du cadre, et non exigence réglementaire. Mitchell et al. soutiennent que le risque pour 
les personnes croît avec l’autonomie et que les agents entièrement autonomes ne devraient pas être développés[303]; 
l’OWASP recommande une double vérification avant qu’un agent ne modifie ses objectifs[87].
EXIG-AUT-04 · DOIT
Domaine de conception opérationnel (ODD), repli et arrêts pour N3 et N4
Un agent de niveau N3 ou N4 DOIT avoir un ODD documenté (systèmes, données, outils, seuils, 
volumes, plages horaires) et un comportement de repli déclaré pour toute sortie de ce domaine : arrêt 
en état sûr, compensation ou escalade vers une file humaine nommée. Il DOIT aussi avoir des plafonds 
d’itérations, de durée et de coût, ainsi que deux arrêts : un arrêt ciblé, qui révoque une catégorie 
d’actions, et un arrêt général (section 7.8 et section 9.4).
Pourquoi : SAE J3016 distingue ses niveaux 3 et 4 par la partie qui assure le repli hors du domaine[304]; le RIA prévoit 
l’arrêt du système dans un état sûr (art. 14, par. 4, al. e)[290] et OpenAI recommande une interruption ciblée ou 
générale[291].
Pour homologuer un niveau, le cadre recommande l’« évaluation assistée » de Feng et al. : un utilisateur 
en attente aide l’agent sur demande et consigne chaque intervention; on augmente graduellement son 
implication, d’abord par des approbations, puis par des échanges plus fréquents. Le niveau se déduit de 
l’implication minimale qui permet d’atteindre le seuil de réussite fixé[83].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 105 sur 283


---
## [Page PDF 106]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
EXIG-AUT-05 · DOIT
Homologation et réévaluation du niveau
Le niveau d’autonomie DOIT être homologué avant la mise en production, puis réévalué à chaque 
changement de modèle ou de version de modèle, d’invite système (hors correction purement typogra­
phique attestée sans effet sur le jeu d’évaluation), d’outil en écriture, de population visée ou d’ODD. 
Tant que la réévaluation n’est pas faite, l’agent DOIT fonctionner au niveau immédiatement inférieur 
à son niveau déclaré; un agent de niveau N1 est suspendu ou ramené à un flux déterministe sans 
autonomie (N0).
Pourquoi : Feng et al. prévoient le renouvellement du certificat d’autonomie à chaque changement de l’agent ou 
de son environnement[83]; pour les institutions financières fédérales, la ligne directrice E-23 du BSIF (en vigueur 
le 1er mai 2027) attend des institutions qu’elles définissent des critères de modification importante d’un modèle, y 
compris d’IA[8].
Correspondance avec les autres échelles
Le tableau suivant situe N0 à N4 par rapport aux échelles des ébauches antérieures et à celles de la littérature. 
Les correspondances avec Gartner, AWS et Feng et al. reposent sur les sources citées sous le tableau; celles 
avec Morris et al. et SAE J3016 sont indicatives, car ces échelles mesurent autre chose que le rôle de la 
personne.
Tableau 29 — Correspondance entre l’échelle du cadre et les autres échelles d’autonomie
Cadre
Ébauches an­
térieures
Gartner (2026)
AWS (portées)
Feng et al. (rôle de 
l’utilisateur)
Morris et al. (indi­
catif)
SAE J3016 
(analogie)
N0
doc. L0 · prod. 
L0
—
—
—
0 Sans IA
—
N1
doc. L1 · v0.x 
N0 · prod. L1
1 Observer; 2 
Conseiller
Portée 1
L1 Opérateur
1 IA outil; 2 IA 
consultante
—
N2
doc. L2 · v0.x 
N1 · prod. L2
3 Agir avec ap­
probation
Portée 2
L2 Collaborateur
3 IA collaboratrice
—
N3
doc. L3 · v0.x 
N2 et N3 · prod. 
L3
4 Agir de façon 
autonome
Portée 3
L3 Consultant; L4 
Approbateur
4 IA experte
Niveau 3 : 
l’humain re­
prend la main
N4
doc. L4 · v0.x 
N4 · prod. L4, 
sans la notion 
multiagent
—
Portée 4, sous 
restrictions
L5 Observateur, 
sous restrictions
5 IA agent (le cadre 
y distingue N4, bor­
née, et NX, non bor­
née; cette distinc­
tion ne vient pas de 
Morris et al.)
Niveau 4 : 
repli assuré 
dans l’ODD
NX
doc. L5
—
—
—
5 IA agent (non 
bornée; distinction 
propre au cadre)
Niveau 5 : do­
maine illimité
Abréviations : « doc. » désigne l’ébauche documentaire (L0 à L5), « v0.x » les ébauches v0.1 et v0.2 (N0 à 
N4) et « prod. » l’ébauche dite de production (L0 à L4). Les niveaux de même numéro ne se correspondent 
pas d’une ébauche à l’autre; seule l’échelle du présent chapitre fait foi. Les sources des colonnes suivantes 
sont Gartner[95], la matrice de portée d’AWS, qui associe la portée 2 à une approbation avant chaque 
action et la portée 3 à une supervision avec interrupteurs d’arrêt[75], Feng et al.[83] et Morris et al.[302]. Les 
correspondances avec Gartner et AWS suivent la vérification des sources; celles avec Feng et al., Morris et 
al. et SAE J3016 sont indicatives, car ces échelles décrivent le rôle de l’utilisateur ou un autre objet que le 
plafond d’actions sans approbation. Les libellés L1 à L5 sont ceux de Feng et al.
SAE J3016 est une pratique recommandée (Recommended Practice) de SAE International, et non une norme de 
sécurité; sa révision en vigueur est J3016_202609. Le cadre ne lui emprunte que deux notions, par analogie : 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 106 sur 283


---
## [Page PDF 107]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
le domaine de conception opérationnel et la question du repli, qui sépare son niveau 3, où l’humain doit 
reprendre la main, de son niveau 4, où le système assure lui-même le repli dans son domaine; seul son niveau 
5 suppose un domaine illimité[301, 304]. Enfin, l’« agent entièrement autonome » de Mitchell et al., qui écrit 
et exécute son propre code, correspond à NX[303].
8.2 Classer un agent : critères
La classe de risque de l’agent (section 12.1) fixe son plafond; quatre critères déterminent ensuite le niveau 
réellement autorisé sous ce plafond.
Le cadre retient ces quatre critères comme méthode interne. Ils s’appuient sur des sources reconnues sans 
en être la transcription. L’IMDA désigne la portée des actions de l’agent, leur réversibilité et son niveau 
d’autonomie comme déterminants du risque, et recommande de borner le rayon d’action dès la concep­
tion[76]. OpenAI recommande de noter chaque outil selon qu’il lit ou écrit, sa réversibilité, les permissions 
requises et son impact financier[66]. Le NIST AI RMF demande que les processus de supervision humaine 
soient définis, évalués et documentés (MAP 3.5)[99].
Tableau 30 — Quatre critères pour fixer le niveau d’autonomie sous le plafond de la classe
Critère
Question posée
Ce qu’on examine
Effet sur le niveau
Rayon d’impact
Combien d’enregistrements, de sys­
tèmes, de personnes ou de dollars 
l’agent peut-il toucher en une exé­
cution ininterrompue?
Outils d’écriture autorisés, por­
tées des jetons, plafonds de vo­
lume et de montant.
Un rayon large abaisse le ni­
veau ou impose des seuils 
plus bas.
Réversibilité
L’effet peut-il être annulé, compen­
sé, ou est-il définitif?
Compensation déclarée au cata­
logue, délai de compensation, 
effets externes.
Une action irréversible relève 
du palier P3 : approbation 
préalable, quel que soit le ni­
veau.
Délai de détection et 
de récupération
Combien de temps s’écoule entre 
une erreur, sa détection et sa cor­
rection?
Alertes automatiques, revue par 
échantillonnage, délai de com­
pensation.
Une détection lente impose 
un contrôle avant l’action 
(N2) plutôt qu’après.
Observabilité recons­
tructive
Peut-on reconstituer ce que l’agent 
a fait, avec quelles données et sous 
quelle autorisation?
Traces d’appels d’outils, journal 
d’audit signé (section 10.3), ver­
sions épinglées.
Sans traces d’appels d’outils, 
ni N3 ni N4.
Le quatrième critère tient au fait que le raisonnement affiché par un modèle n’explique pas forcément ses 
actions : l’IMDA rappelle que la chaîne de pensée n’est pas analogue au raisonnement humain[76]. Seules les 
traces des appels d’outils prouvent ce qui a été fait.
Les seuils qui traduisent ces critères en plafonds (nombre d’enregistrements, montants, délais) sont des 
paramètres d’étalonnage du cadre : le comité d’architecture et des risques agentiques les approuve, les 
publie avec le catalogue et les révise après chaque incident. Aucune source reconnue ne propose de valeurs 
universelles. Le niveau autorisé est le plus bas de trois valeurs : le plafond de la classe, le niveau que 
permettent les quatre critères et le niveau suffisant pour l’objectif.
EXIG-AUT-06 · DOIT
Classement fondé sur les permissions effectives
L’évaluation des quatre critères DOIT se fonder sur les permissions effectives de l’agent (outils auto­
risés, portées des jetons, plafonds de volume et de montant), et non sur l’intention déclarée. Elle DOIT 
être consignée dans la fiche d’agent (annexe B) et revue par l’architecture d’entreprise et par la sécurité 
avant l’homologation du niveau.
Pourquoi : Gartner situe la cause de nombreux échecs dans la confusion entre la capacité d’agir et la portée des accès 
accordés[305]; l’IMDA recommande de borner le rayon d’action par les accès aux outils et aux systèmes[76].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 107 sur 283


---
## [Page PDF 108]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
EXIG-AUT-07 · NE DOIT PAS
Règle d’or : pas d’exécution autonome du risque cumulé
Un agent dont le rayon d’impact, la réversibilité et le délai de détection atteignent les seuils d’étalonnage 
approuvés par le comité (rayon élevé, réversibilité faible, détection lente) NE DOIT PAS être autorisé 
au-delà de N2, quels que soient ses résultats aux bancs d’essai.
Pourquoi : règle propre au cadre. L’IMDA lie le risque à la portée et à la réversibilité des actions[76], et Feng et al. 
rappellent que les bancs d’essai de capacité ne révèlent pas le niveau d’autonomie approprié[83].
EXEMPLE
Un agent de facturation peut modifier 10 000 comptes par exécution (rayon large). Ses écritures changent 
des montants facturés, difficiles à corriger une fois les factures transmises (réversibilité faible), et une 
erreur ne serait vue qu’à la fermeture mensuelle (détection lente). Malgré d’excellents résultats aux 
essais, il reste à N2. Pour viser N3, l’équipe agit sur les critères, pas sur les essais : plafond par exécution, 
détection automatisée des écarts, retenue des factures avant transmission.
8.3 Paliers de risque des outils P0 à P3
Le palier mesure le risque d’un outil, indépendamment de l’agent qui l’appelle; il forme le second axe de la 
supervision.
Un même agent peut lire sans risque et écrire avec risque. Parasuraman, Sheridan et Wickens ont proposé 
d’automatiser séparément chaque fonction (acquérir l’information, l’analyser, décider, agir), chacune à un 
niveau propre, un même système pouvant combiner des niveaux différents[306]. L’autonomie se règle donc 
aussi par action, et pas seulement par agent.
Tableau 31 — Paliers de risque des outils
Palier
Nature
Exemples
Contrôles obligatoires
P0
Lecture publique
Recherche documentaire publique, 
catalogue de produits, conversion 
d’unités.
Identité de charge de travail, limitation de débit, 
journalisation de l’usage.
P1
Lecture interne ou 
sensible
Dossier client, fiche de paie, recherche 
documentaire interne.
Jeton délégué (section 9.3), contrôle d’accès au do­
cument ou à la ligne, masquage des RP en sortie, 
journal d’audit.
P2
Écriture réversible 
ou compensable, 
impact modéré
Billet de service, brouillon de courriel, 
réservation interne, mise à jour de sta­
tut.
Jeton délégué, clé d’idempotence (section 7.6), com­
pensation déclarée (section 7.5), seuil métier au 
catalogue (p. ex. 5 000 $); approbation au-delà du 
seuil.
P3
Action critique, ex­
terne ou irréver­
sible
Virement, suppression définitive de 
données, communication externe offi­
cielle, changement d’infrastructure de 
production.
Approbation humaine hors bande à chaque appel, 
jeton d’approbation lié à l’action, second approba­
teur pour la classe élevée; jamais exécuté seul par un 
agent.
La frontière entre paliers suit l’effet, pas le serveur. Créer un brouillon de courriel est une action P2, car il 
reste dans l’entreprise et peut être supprimé; l’envoyer à un client est une action P3. Un même serveur MCP 
expose souvent les deux : chaque outil reçoit son propre palier.
Le palier ne peut pas venir du serveur lui-même. La spécification MCP 2026-07-28 exige que les clients 
considèrent les annotations d’outils comme non fiables, à moins qu’elles ne proviennent de serveurs de 
confiance; la référence du schéma précise, en des termes non normatifs (« should never »), que les clients 
ne fondent jamais une décision d’usage sur les annotations d’un serveur non fiable[197, 201]. Les métadonnées 
de gouvernance vivent donc au catalogue d’entreprise (section 6.8; pour les annotations MCP, section 6.5).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 108 sur 283


---
## [Page PDF 109]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
EXIG-AUT-08 · DOIT
Palier attribué au catalogue après revue
Chaque outil DOIT recevoir un palier P0 à P3 (tableau 31) au catalogue d’entreprise (section 6.8) après 
revue par son propriétaire et par la sécurité, avec son seuil métier et son outil de compensation s’il 
y a lieu. Le palier provient du catalogue, jamais des annotations ou des métadonnées déclarées par 
le serveur. Un outil qui combine plusieurs effets prend le palier le plus élevé; un outil d’écriture sans 
compensation déclarée est classé P3.
Pourquoi  : la spécification MCP tient les annotations pour des indices non fiables[197]; OpenAI recommande 
d’attribuer à chaque outil une cote de risque[66].
EXIG-AUT-09 · NE DOIT PAS
Aucun outil P3 exécuté seul
Un agent NE DOIT PAS exécuter un outil P3 sans une approbation humaine préalable, propre à cet 
appel, quel que soit son niveau d’autonomie.
Pourquoi : l’IMDA recommande une approbation humaine avant les actions à fort enjeu ou irréversibles, comme 
la suppression définitive, l’envoi de communications ou les paiements; OpenAI présente l’autorisation préalable 
des actions irréversibles comme le moyen usuel de limiter les défaillances graves; l’OWASP range l’absence de 
confirmation des actions sensibles parmi les vulnérabilités (ASI09)[28, 76, 291].
8.4 Combiner classe de l’agent et palier de l’outil
Le contrôle exigé pour un appel dépend de la classe de l’agent, de son niveau d’autonomie et du palier de 
l’outil; la règle la plus stricte l’emporte.
CLASSE DE L’AGENT ↓ · PALIER DE L’OUTIL →
P0 · lecture publique
catalogue, documentation
P1 · lecture interne
dossier client, paie
P2 · écriture réversible
billet, brouillon, statut
P3 · action critique
virement, suppression, envoi
Faible
plafond N3
(N4 sur décision)
Automatique
identité de charge, débit
Automatique
jeton délégué, masquage
Autonome sous seuil
idempotence, compensation
Approbation signée
à chaque appel
Modéré
plafond N3
Automatique
identité de charge, débit
Automatique + audit
jeton délégué, filtrage par ligne
Approbation au-delà
du seuil métier déclaré
Approbation signée
à chaque appel
Élevé
plafond N2
Automatique + audit
journalisation complète
Audit + revue
finalité vérifiée, minimisation
Approbation signée
à chaque action (N2)
Approbation signée
+ second approbateur
La règle la plus stricte l’emporte. Le palier d’un outil est inscrit au catalogue; la passerelle ne se fie pas aux annotations déclarées par le serveur.
Figure 15 — Contrôle exigé selon la classe de l’agent et le palier de l’outil. On lit la ligne de la classe de l’agent, puis la colonne 
du palier de l’outil; la cellule donne le contrôle minimal. Le niveau d’autonomie de l’agent et les déclencheurs d’approbation peuvent 
le rendre plus strict, jamais plus souple. Source : CRE-IA-2026-01.
Deux exemples. Un agent de classe modérée, déclaré N3, reclasse un billet de service : outil P2 sous le seuil, 
il agit seul et l’appel est journalisé. Le même agent veut modifier l’échéance de 40 factures alors que le seuil 
déclaré de l’outil est de 25 par tâche : la passerelle suspend l’appel et demande une approbation. Si l’agent 
était déclaré N2, chaque écriture exigerait une approbation, même sous le seuil : le niveau prime alors sur 
la cellule.
D’autres déclencheurs s’ajoutent à la grille. L’IMDA en énumère quatre catégories : actions à fort enjeu, 
actions irréversibles, comportements atypiques (accès hors périmètre, trajectoire anormale) et seuils fixés 
par l’utilisateur[76]. La « règle de deux » de Meta (31 octobre 2025) en fournit une autre : dans une session, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 109 sur 283


---
## [Page PDF 110]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
un agent ne devrait pas cumuler l’exposition à des entrées non fiables, l’accès à des données sensibles et 
la capacité de changer d’état ou de communiquer vers l’extérieur; si les trois sont nécessaires, il n’agit pas 
sans supervision[307]. Un agent N3 qui a lu un courriel externe, consulté un dossier P1 et s’apprête à appeler 
un outil P2 tombe donc sous approbation (section 9.6).
EXIG-AUT-10 · DOIT
Contrôle calculé à chaque appel
Pour chaque appel d’outil, la passerelle d’agents DOIT déterminer le contrôle exigé en retenant le plus 
strict des éléments suivants : la cellule classe × palier de la figure 15, le niveau d’autonomie de l’agent et 
les déclencheurs d’approbation (comportement atypique, dépassement de seuil, cumul de contenu non 
fiable, de données sensibles et d’action externe). Elle consigne la règle appliquée dans la trace et dans 
le journal d’audit (section 10.3).
Pourquoi : retenir le plus strict des éléments empêche qu’un agent peu autonome obtienne des droits étendus par un 
outil mal classé, ou qu’un outil bien classé soit utilisé au-delà du niveau de l’agent. Règle propre au cadre; l’IMDA 
lie le risque à la portée et à la réversibilité des actions[76].
EXIG-AUT-11 · DOIT
Échec en mode fermé
Si le service d’approbation, le catalogue ou le service de politiques est indisponible, ou si aucune 
politique ne couvre l’action demandée, la passerelle DOIT refuser tout appel P3 et tout appel P2 au-
delà du seuil, sans préjudice du refus général de tout appel dépourvu de décision de politique valide 
(EXIG-IAM-18). Dans tous ces cas, l’orchestrateur DOIT suspendre la tâche dans un état reprenable.
Pourquoi : l’IMDA recommande de refuser l’action par défaut lorsque l’infrastructure d’approbation fait défaut, par 
exemple si les superviseurs sont injoignables ou si aucune politique n’existe pour l’action tentée[76].
8.5 Approbation humaine vérifiable
Une approbation n’a de valeur que si elle porte sur l’action exacte qui sera exécutée et si la passerelle peut 
le vérifier sans faire confiance à l’agent.
Un « oui, je confirme » écrit dans la conversation de l’agent ne prouve rien : une injection d’instructions 
peut l’imiter, et l’agent peut modifier l’action après coup. Le cadre fait donc de l’approbation un objet 
cryptographique, émis hors de portée de l’agent et lié à l’action par une empreinte.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 110 sur 283


---
## [Page PDF 111]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
Agent
prépare l’action P3
Passerelle d’agents
point d’application
Service d’approbation
adossé au fournisseur d’identité
Approbateur
personne habilitée
1
appel d’outil P3 sans jeton
2
calcule l’empreinte et crée la demande
h = SHA-256(outil ‖ arguments canoniques)
3
présente l’action exacte, ses
paramètres et son effet attendu
4
approuve (authentification forte)
5
jeton d’approbation signé, à usage unique
{ h, approbateur, tâche, exp }
6
rejoue l’appel avec le jeton
7
vérifie la signature, l’expiration, l’usage unique et
recalcule h : toute modification des arguments
invalide l’approbation → exécution, puis audit
N’est jamais une approbation
• un « oui » écrit dans la
conversation de l’agent
• un résumé rédigé par l’agent
• une approbation donnée pour
d’autres arguments
Figure 16 — Approbation humaine signée, liée à l’action exacte. La passerelle intercepte l’appel P3, calcule l’empreinte de l’action 
et la fait approuver par une personne habilitée; le jeton signé ne vaut que pour cette empreinte, une seule fois et pendant 15 minutes 
au plus. Source : CRE-IA-2026-01.
L’empreinte se calcule ainsi : h = SHA-256(identifiant de l’outil ‖ arguments canonisés), où l’identifiant de 
l’outil est pleinement qualifié (serveur, nom et version épinglée). La canonisation suit la RFC 8785 (JSON 
Canonicalization Scheme), une RFC informative de la filière indépendante, non endossée par l’IETF, mais 
stable[308]; A2A 1.0 l’emploie déjà pour signer les cartes d’agent[68]. Sans canonisation, deux sérialisations du 
même objet JSON donneraient deux empreintes. Si l’agent, ou une injection, change un seul argument après 
l’approbation, l’empreinte recalculée par la passerelle ne correspond plus et l’appel est refusé. Un exemple 
de jeton figure à l’annexe C.
La formule est un choix de conception du cadre, pas une norme. Elle met en œuvre l’approbation explicite 
par action à fort impact que recommande l’OWASP (ASI02)[28] et s’appuie sur trois éléments normalisés : 
OpenID Connect CIBA (Client-Initiated Backchannel Authentication) pour l’approbation hors bande, la RFC 
9396 pour décrire l’action et la RFC 8785 pour la canonisation.
EXIG-AUT-12 · DOIT
Jeton d’approbation lié à l’action exacte
Toute approbation exigée par la figure 15 DOIT produire un jeton signé par le service d’approbation 
adossé au fournisseur d’identité, contenant au minimum : l’empreinte h (SHA-256 de l’identifiant plei­
nement qualifié de l’outil, suivi des arguments canonisés selon la RFC 8785), l’identifiant pseudonymisé 
de l’approbateur, les identifiants de la tâche et de l’agent, une date d’expiration et un identifiant à usage 
unique. Avant l’exécution, la passerelle DOIT vérifier la signature, l’expiration et l’usage unique, puis 
recalculer h; toute différence annule l’approbation. Le jeton DOIT expirer au plus 15 minutes après sa 
signature.
Pourquoi : un lien cryptographique entre la décision humaine et l’action exécutée détecte toute modification des 
arguments après l’approbation; ce mécanisme et la durée de validité sont des choix du cadre.
EXIG-AUT-13 · NE DOIT PAS
Ce qui n’est jamais une approbation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 111 sur 283


---
## [Page PDF 112]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
La passerelle NE DOIT PAS accepter comme approbation un message d’acquiescement dans la 
conversation de l’agent, un résumé ou une justification rédigés par l’agent, une confirmation locale 
dans l’interface de l’agent, ni une approbation donnée pour d’autres arguments, une autre tâche ou un 
autre agent.
Pourquoi : le brouillon de groupe de travail WIMSE AIMS précise qu’une confirmation locale dans l’interface ne 
suffit pas comme autorisation[309].
EXIG-AUT-14 · DEVRAIT
Approbation hors bande normalisée
L’approbation d’un appel P3, ou celle que requiert un agent sans interface, DEVRAIT passer par 
OpenID Connect CIBA  : le service d’approbation lance une demande d’authentification dorsale, 
l’approbateur confirme sur son propre appareil, et un binding_message court, affiché sur les 
deux appareils, rattache la demande à l’action. L’action DEVRAIT être décrite par le paramètre 
authorization_details de la RFC 9396 lorsqu’elle comporte des paramètres que les portées ne peuvent 
exprimer, comme un montant ou un destinataire.
Pourquoi : CIBA Core 1.0 est une spécification finale de l’OpenID Foundation qui découple l’appareil de l’agent de 
celui de l’approbateur[310]; le brouillon WIMSE AIMS cite CIBA en exemple d’autorisation par palier, tout en notant 
ses limites en cours d’exécution, et le livre blanc de l’OpenID Foundation propose CIBA pour l’approbation humaine 
des agents[93, 311]; la RFC 9396 exprime les autorisations fines que scope ne peut exprimer[312].
EXIG-AUT-15 · DOIT
Approbateurs habilités et formés
Chaque combinaison de classe et de palier soumise à approbation DOIT avoir une liste d’approbateurs 
habilités, inscrite au registre. L’approbateur DOIT s’authentifier par authentification forte (au moins 
deux facteurs), posséder la compétence du domaine et l’autorité de refuser, et avoir été formé aux modes 
de défaillance des agents. Pour un appel P3 d’un agent de classe élevée, deux approbateurs distincts 
DOIVENT approuver, dont au moins un autre que le mandant.
Pourquoi : le RIA confie le contrôle humain des systèmes à haut risque à des personnes ayant la compétence, la 
formation et l’autorité nécessaires (art. 26, par. 2)[94]; l’IMDA demande que les superviseurs connaissent les modes 
de défaillance des agents[76]. Le second approbateur est un choix du cadre.
8.6 Interaction humaine avec les agents ambiants
Un agent ambiant travaille en arrière-plan, déclenché par des événements; la personne n’est pas devant lui 
quand il a besoin d’elle, et l’interaction doit être conçue en conséquence.
LangChain définit les agents ambiants comme des agents qui écoutent un flux d’événements et agissent 
en conséquence, éventuellement sur plusieurs événements à la fois, sans être nécessairement entièrement 
autonomes (section 3.3). Pour les relier aux personnes, son billet de janvier 2025 décrit trois patrons : 
notifier, questionner et réviser[86]. Le schéma de la boîte de réception d’agents (Agent Inbox) y associe 
quatre réponses : accept, edit, response et ignore, activées une à une par les drapeaux allow_accept, 
allow_edit, allow_respond et allow_ignore [313].
Tableau 32 — Trois patrons d’interaction avec un agent ambiant
Patron
Quand l’employer
Ce que fait l’agent
Réponses admises
Notifier
Événement important que la politique in­
terdit à l’agent de traiter (p. ex. un contrat 
reçu pour signature).
Signale sans agir.
Prendre connaissance.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 112 sur 283
