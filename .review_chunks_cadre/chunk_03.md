# chunk_03 — pages PDF 21 à 32 (sur 283)



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


---
## [Page PDF 23]

CRE-IA-2026-01 · Cadre de référence
3 Concepts et définitions
• N4 Autonomie étendue sous ODD certifié : l’agent s’autodéclenche sur des événements et opère en 
continu; l’humain est hors de la boucle d’exécution, mais sur la boucle de gouvernance; une action P3 
est toujours approuvée; ce niveau exige une décision du comité.
• NX Autonomie non bornée : l’agent fixe ses objectifs, modifie ses permissions ou exécute du code 
hors contraintes. Ce niveau est interdit.
Le niveau est un plafond déclaré au registre, à la manière du « certificat d’autonomie » de Feng, McDonald 
et Zhang[83]; il est distinct de la topologie (le nombre d’agents) et de la capacité du modèle. Plafond par 
classe de risque : celui que fixe EXIG-CON-02 selon la classe attribuée au tableau 46 (section 12.1).
Paliers d’outils : P0 lecture publique; P1 lecture interne ou sensible; P2 écriture réversible; P3 action 
critique, externe ou irréversible, jamais exécutée seule par un agent.
À RETENIR
Quatre axes à ne pas confondre : classe de risque de l’agent (section 12.1), niveau d’autonomie, palier 
de l’outil et topologie (chapitre 7). Pour une action, le contrôle le plus strict l’emporte (section 8.4).
3.2 Flux de travail ou agent?
Cette section distingue deux façons de faire travailler un modèle, qui n’appellent ni les mêmes contrôles ni 
les mêmes coûts.
Selon Anthropic, un flux de travail orchestre le modèle et les outils par des chemins de code prédéfinis, alors 
qu’un agent dirige lui-même son processus et l’usage de ses outils. Les deux reposent sur la même brique, 
le modèle augmenté (augmented LLM), doté de capacités de recherche, d’outils et de mémoire[65]. Un agent 
fonctionne en boucle : la méthode ReAct fait alterner raisonnement et actions sur des sources externes, ce 
qui a réduit les hallucinations par rapport à la chaîne de pensée seule et amélioré le taux de réussite sur les 
tâches interactives (ALFWorld, WebShop) dans les essais de ses auteurs[84].
Quand chacun convient
La question décisive est simple : qui doit choisir le prochain pas, le code ou le modèle? La section 7.3 en fait 
un arbre de décision.
• Code ou règle (N0). Si une fonction suffit, on écrit la fonction plutôt qu’un agent[85].
• Appel direct au modèle. Pour une transformation en un seul passage : classer, résumer, traduire[9].
• Flux de travail assisté par IA. Quand le chemin est connu d’avance, réglementé ou audité. C’est le 
patron par défaut du cadre.
• Agent unique outillé. Quand les étapes dépendent de ce que l’agent découvre en chemin, pour des 
requêtes variées dans un même domaine.
• Système multiagent. Quand il faut protéger le contexte, paralléliser des pistes réellement indépen­
dantes, spécialiser les outils ou séparer des frontières de sécurité, et seulement sur preuve mesurée de 
gain (section 7.1 et section 7.3).
Les deux se combinent : un flux peut contenir une étape agentique, et un agent peut appeler un flux 
comme un outil. La distinction ne dit rien de l’autonomie : un agent N1 choisit ses étapes, mais ne fait que 
recommander.
À RETENIR
Le modèle ne décide que là où le chemin ne peut pas être écrit d’avance. Ce qu’une règle peut trancher 
(routage, calcul, contrôle de sécurité) reste dans le code (PRIN-08).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 23 sur 283


---
## [Page PDF 24]

CRE-IA-2026-01 · Cadre de référence
3 Concepts et définitions
3.3 Agents interactifs et agents ambiants
Cette section distingue deux modes de déclenchement, qui pèsent sur la conception d’un agent.
Un agent interactif répond à une personne présente, dans une conversation ou une application. Un 
agent ambiant, selon LangChain, écoute un flux d’événements et agit en conséquence, éventuellement sur 
plusieurs événements à la fois, sans être nécessairement entièrement autonome; une tâche planifiée peut 
aussi le lancer[86]. Le tableau 8 en tire les conséquences.
Tableau 8 — Agents interactifs et agents ambiants : conséquences de conception
Dimension
Agent interactif
Agent ambiant
Déclencheur
Demande d’une personne dans un canal
Événement (message, alerte, changement d’état) ou 
tâche planifiée
Contrainte de 
temps
Réponse attendue en direct : appels d’outils et ité­
rations bornés en conséquence
Délai relâché : traitement de fond, par lots au besoin
Interaction hu­
maine
Dans la session; une action P3 reste approuvée 
hors bande (section 8.5)
File persistante : notifier, questionner, réviser (section 
8.6)
État et reprise
Persistance requise dès qu’une approbation ou 
une tâche longue intervient
Exécution durable, qui survit aux pannes et aux redé­
ploiements (section 7.4)
Risque dominant
Un « oui » dans la conversation pris à tort pour 
une approbation
Volume : saturation des approbateurs (menace T10 de 
l’OWASP)[87] et tempêtes d’événements (section 6.7)
Le mode de déclenchement ne fixe pas le niveau d’autonomie. Un agent ambiant peut se borner à signaler 
(N1), préparer des actions soumises à approbation (N2) ou agir seul sous seuils (N3); seul le niveau N4 
combine le déclenchement sur événements, l’exécution continue et l’absence de la personne dans la boucle 
d’exécution. Pour les traitements de fond non urgents, Anthropic et OpenAI accordent chacun, au 27 octobre 
2026, un rabais de 50 % sur les jetons traités par lots, dans une fenêtre de 24 heures[88, 89] (section 10.6).
3.4 Ce qu’un agent n’est pas
Cette section écarte trois confusions qui minent la sécurité et l’imputabilité; les chapitres 9 et 11 en tirent 
les exigences.
Pas un compte d’utilisateur
Un agent n’emprunte jamais le compte d’une personne, même pour agir en son nom. Microsoft déconseille 
d’attribuer aux agents un compte d’utilisateur ordinaire ou un principal de service traditionnel, et a créé 
pour eux un type d’identité propre[90]. À l’inverse, une personne n’utilise jamais l’identité d’un agent : 
l’OWASP range cet usage parmi les dix principaux risques des identités non humaines (NHI10)[91]. Pour agir 
au nom de quelqu’un, l’agent reçoit une délégation qui l’identifie aux côtés de la personne (section 9.3).
Pas un principal de service partagé
Chaque agent a sa propre identité, et chaque instance la sienne au besoin[92]. Un compte ou une clé d’API 
commun à plusieurs agents empêche de savoir lequel a agi et de révoquer l’un sans arrêter les autres. Le 
brouillon « AI Identity Management System » (AIMS) du groupe de travail WIMSE de l’IETF exige un 
identifiant unique par agent et qualifie les clés d’API statiques d’antipatron; l’OWASP classe la réutilisation 
d’identités non humaines parmi les risques majeurs (NHI9)[91, 93].
Pas un responsable
Un agent ne répond pas de ses actes, ne consent pas et n’approuve rien. Une personne nommée, le proprié­
taire métier (parrain), répond de chaque agent, de ses effets et de son retrait (section 11.1). Le droit et la 
pratique vont dans ce sens : le RIA oblige le déployeur d’un système à haut risque à confier la supervision 
humaine à des personnes compétentes, formées et dotées de l’autorité nécessaire[94]; Microsoft Entra Agent 
ID associe à chaque agent un parrain, responsable métier, et un propriétaire au sens d’Entra, chargé de 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 24 sur 283


---
## [Page PDF 25]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
l’administration technique (le responsable technique du cadre, section 11.1)[90]. Une approbation exigée par 
le cadre vient donc toujours d’une personne, jamais d’un autre agent (section 8.5).
À RETENIR
Un agent a une identité propre, des droits délégués et bornés, et une personne nommée qui en répond. 
Sans ces trois conditions, il ne satisfait pas aux exigences des chapitres 9 et 11.
4 Principes directeurs
Douze principes guident toute décision d’architecture agentique, de la conception d’un agent à l’achat d’une 
plateforme. Ils expliquent le pourquoi des exigences des chapitres 5 à 13 et tranchent les situations que ces 
exigences ne prévoient pas. Ce chapitre les énonce, montre où chacun est mis en œuvre et fixe la manière 
d’arbitrer entre eux.
4.1 Les douze principes
Chaque principe tient en un énoncé et en ses conséquences pour la conception; les principes sont présentés 
par paires, selon la question qu’ils règlent. En cas de conflit avec une préférence d’équipe, un usage local 
ou la recommandation d’un fournisseur, le principe l’emporte, sauf dérogation approuvée (section 4.3).
À RETENIR
Trois questions résument l’essentiel des principes qui encadrent l’action des agents (PRIN-03 à PRIN-06, 
PRIN-10 et PRIN-12). Qui a autorisé cette action, et au nom de qui? Peut-on la défaire, ou au moins 
l’arrêter? Peut-on reconstituer après coup ce qui s’est passé et ce que cela a coûté?
Interopérer par des contrats ouverts
Un agent de service bâti sur une plateforme de logiciel-service (SaaS) doit pouvoir déléguer à un agent conçu 
à l’interne, qui appelle des outils exposés par une autre équipe. Sans protocole commun, chaque paire exige 
son connecteur et les intégrations se multiplient (chapitre 2). Les deux premiers principes remplacent ce 
maillage par des contrats publiés une fois et consommés par tous.
PRIN-01
Standards ouverts avant intégrations propriétaires
Tout échange qui franchit la frontière d’un domaine (agent vers outil, agent vers agent, événement) passe 
par un protocole inscrit au catalogue des protocoles (section 6.3). Un connecteur propriétaire point à point 
exige une dérogation.
Conséquences : on privilégie les protocoles sous gouvernance neutre, comme MCP et A2A, hébergés par 
l’Agentic AI Foundation (AAIF) de la Linux Foundation depuis décembre 2025 et août 2026 respectivement[4, 
35]. Une plateforme qui ne les prend pas en charge est isolée derrière un adaptateur.
PRIN-02
Contrat avant code, mise en œuvre opaque
Chaque agent et chaque outil publient un contrat lisible par machine (définition d’outil, carte d’agent (Agent 
Card), contrat d’événement) avant leur mise en service. Seul ce contrat fait foi : un consommateur ne dépend 
jamais du cadriciel, du modèle ni de la structure interne d’un pair.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 25 sur 283


---
## [Page PDF 26]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
Conséquences : le contrat est versionné, épinglé et inscrit au catalogue d’entreprise. La description d’un 
outil, que le modèle lit pour décider, en fait partie : la modifier exige une nouvelle approbation (section 6.8). 
La mise en œuvre, elle, change librement.
Borner le pouvoir d’agir
Ce qu’un agent peut atteindre et ce qu’il peut faire sans personne sont deux questions distinctes. Selon 
Gartner (mai 2026), les échecs de gouvernance des agents tiennent notamment à la confusion entre la capa­
cité d’agir d’un agent et la portée des accès qui lui sont accordés[95]. Exemple : un agent de remboursement 
lit les pièces du dossier du client utiles à la demande, mais n’émet un remboursement qu’après approbation.
PRIN-03
Identité propre, moindre privilège et moindre agence
Chaque agent possède sa propre identité non humaine, jamais un compte d’utilisateur ni un secret partagé. 
Ses droits sont minimaux, de courte durée et jamais supérieurs à ceux de son mandant. Ses outils et son 
autonomie se limitent à ce que la tâche exige : c’est la moindre agence (Least-Agency) de l’OWASP, pour qui 
un comportement agentique déployé sans nécessité élargit la surface d’attaque sans ajouter de valeur[28].
Conséquences  : les droits effectifs d’un agent délégué ne dépassent jamais l’intersection des droits du 
mandant et de ceux de l’agent[96]; le serveur d’autorisation l’applique à chaque échange de jetons (section 
9.3).
PRIN-04
Autonomie proportionnée au risque
Le niveau d’autonomie, de N0 à N4, est un plafond déclaré au registre et fixé par la classe de risque de 
l’agent. Il ne découle ni de la capacité du modèle ni de ses résultats aux bancs d’essai. L’autonomie non 
bornée (NX) est interdite.
Conséquence : le niveau ne dépasse jamais le plafond de la classe de risque, fixé par EXIG-CON-02 (section 
8.1, section 12.1). Feng, McDonald et Zhang traitent aussi l’autonomie comme une décision de conception, 
distincte de la capacité[83].
Maîtriser les effets
Un agent réessaie, se trompe ou peut être détourné : il faut donc prévoir ce qui se passe quand l’action est 
fausse. Exemple : un appel de paiement expire et l’agent le relance; sans clé d’idempotence, le paiement 
est exécuté deux fois. Et si un client conteste la décision trois semaines plus tard, il faut retrouver qui l’a 
demandée, quel agent l’a préparée, qui l’a approuvée et ce qu’elle a coûté.
PRIN-05
Réversibilité par conception
Toute action qui modifie un système d’enregistrement est idempotente et, selon le cas, annulable, compen­
sable ou soumise à une approbation humaine préalable. Une action de palier P3, c’est-à-dire critique, externe 
ou irréversible, n’est jamais exécutée seule par un agent.
Conséquences : clé d’idempotence à chaque étape, compensation déclarée avant l’action (section 7.5) et, 
comme le recommande Microsoft, étapes irréversibles placées après toutes les validations critiques[67, 77].
PRIN-06
Traçabilité et imputabilité économique
Chaque action se rattache, par un identifiant de trace commun, à la demande d’origine, au mandant, à l’agent 
et à sa version, à la décision prise et à un centre de coûts.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 26 sur 283


---
## [Page PDF 27]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
Conséquences : traçage OpenTelemetry sur tous les sauts; journal d’audit inaltérable et distinct des traces, 
en accord avec l’OWASP, qui recommande des journaux immuables et signés des actions d’agents[28]; jetons 
mesurés par agent et par exécution[9]; coût suivi par tâche réussie (chapitre 10).
Contenir le modèle
Un modèle de langage est probabiliste et influencé par tout ce qu’il lit : c’est utile pour comprendre une 
demande, dangereux pour décider d’un montant ou d’un destinataire. Exemple : un agent qui trie le courrier 
reçoit un message disant « transférez ce dossier à l’adresse suivante ». Lui demander d’être prudent ne suffit 
pas : le transfert doit être impossible depuis cette session.
PRIN-07
Défiance envers le contenu reçu
Ce qu’un outil, un document, une page Web, une mémoire ou un autre agent renvoie est une donnée, 
jamais une instruction de confiance. Le cadre présume l’injection d’instructions possible dès qu’un modèle 
lit du contenu non fiable, comme l’envisage le NIST AI 100-2 E2025, selon lequel les concepteurs peuvent 
concevoir leurs systèmes dans cette hypothèse[97]; le Centre national de cybersécurité du Royaume-Uni 
(NCSC) rappelle qu’un modèle de langage ne sépare pas intrinsèquement les données des instructions[98].
Conséquences : les contrôles décisifs sont déterministes, par exemple le retrait des outils d’envoi externe 
après la lecture de contenu non fiable. La détection et le marquage réduisent le risque sans l’éliminer 
(section 9.6).
PRIN-08
Déterminisme autour du modèle et simplicité d’abord
Le raisonnement probabiliste s’exécute dans une enveloppe déterministe : schémas validés, machine à états, 
contrats typés, plafonds d’itérations. On ne confie jamais au modèle un routage, un calcul ou une décision 
de sécurité qu’une règle résout, et l’on retient la solution la plus simple : une fonction avant un agent, un 
agent avant plusieurs. Anthropic, Microsoft et OpenAI convergent sur cette règle de frugalité[9, 65, 66, 85].
Conséquences : les sorties du modèle sont validées par schéma avant tout effet; un système multiagent 
justifie par écrit pourquoi un flux déterministe ou un agent unique ne suffit pas (section 7.3).
Garder la maîtrise
L’entreprise doit pouvoir changer de modèle quand le prix, la qualité ou la résidence des données l’exigent, 
et savoir à tout moment qui répond de chaque agent. Le premier point protège sa logique métier; le second, 
les personnes touchées par les décisions des agents.
PRIN-09
Découplage des fournisseurs et propriété de la logique
Modèles, plateformes et cadriciels sont remplaçables. L’entreprise garde la propriété de sa logique 
d’orchestration, de ses contrats d’outils, de ses invites et de ses mémoires, dans des formats exportables. 
Avec MCP et A2A sous gouvernance neutre, le risque de verrouillage s’est déplacé vers les plateformes et 
leurs extensions propriétaires (section 13.1).
Conséquences : aucun agent n’appelle directement un fournisseur de modèles; il passe par la passerelle de 
modèles (section 5.2). Les contrats d’approvisionnement prévoient la réversibilité et la sortie (section 13.3).
PRIN-10
Humain imputable
Une personne nommée, le propriétaire métier (parrain), répond de chaque agent, de ses effets et de son 
retrait; l’agent n’est jamais responsable. Le NIST AI RMF, cadre volontaire, attend des politiques qui 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 27 sur 283


---
## [Page PDF 28]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
définissent les rôles et responsabilités humain-IA (GOVERN 3.2)[99], et l’IMDA de Singapour fait de la 
responsabilisation réelle des humains l’une des quatre dimensions de son cadre[76].
Conséquences : aucun agent n’entre en production sans propriétaire inscrit au registre, et ce propriétaire 
atteste périodiquement que l’agent reste nécessaire (sections 11.4 et 11.5).
Concevoir pour durer et pour défaillir
Les agents de longue durée traversent pannes, déploiements et changements de version. Exemple : si le 
fournisseur de modèles tombe en panne pendant le traitement de 300 dossiers, chacun doit reprendre où il 
s’était arrêté, basculer vers un modèle de repli ou passer à une personne, jamais rester à moitié exécuté à 
l’insu de tous.
PRIN-11
Découplage du raisonnement, de l’action et de la mémoire
La logique de l’agent (invites, choix du modèle), ses capacités d’action (serveurs MCP, API) et son état 
(mémoires de travail, épisodique et sémantique) se déploient, se sécurisent et évoluent séparément; la 
mémoire procédurale, déployée avec l’agent, suit le cycle de sa logique. L’état ne vit jamais seulement dans 
la mémoire du processus : Microsoft recommande de persister l’état partagé à l’extérieur[9].
Conséquences : on change de modèle sans toucher aux outils et on révoque un outil sans redéployer l’agent. 
L’écriture en mémoire procédurale, jugée plus risquée par la taxonomie CoALA (Cognitive Architectures for 
Language Agents)[100], est gérée comme un changement de code (section 5.5).
PRIN-12
Dégradation maîtrisée
L’architecture prévoit les erreurs de modèle, les dépassements de délai, les boucles et les pannes de 
fournisseur : délais, reprises, disjoncteurs, plafonds d’itérations et de coûts, modèles de repli, escalade vers 
une personne. En cas de doute, le système échoue en mode fermé : il s’arrête ou escalade plutôt que d’agir.
Conséquences : les mécanismes de fiabilité que décrit Microsoft (délais, reprises, disjoncteurs, validation des 
sorties avant transmission) deviennent obligatoires[9]; l’action est refusée si l’approbation requise est impos­
sible à obtenir, comme le recommande l’IMDA[76]; le coupe-circuit est testé chaque trimestre, fréquence 
choisie par le cadre (section 7.8).
4.2 Application des principes
Les principes se traduisent en exigences vérifiables dans les chapitres 5 à 13. Le tableau 9 indique, pour 
chacun, les sections qui le mettent en œuvre, les familles d’exigences concernées et la preuve qu’une revue 
d’architecture contrôle.
Tableau 9 — Mise en œuvre des principes directeurs
Principe
Sections
Exigences
Preuve contrôlée en revue
PRIN-01 Standards ouverts
6.2, 6.3, 6.9, 11.7
EXIG-INT, EXIG-MCP, 
EXIG-A2A, EXIG-EVT, 
EXIG-GOV
Protocole retenu au catalogue pour chaque in­
terface
PRIN-02 Contrat avant code
6.5, 6.6, 6.8, annexe 
C
EXIG-INT, EXIG-MCP, 
EXIG-A2A
Contrat publié, versionné et épinglé
PRIN-03 Identité et moindre 
agence
9.2, 9.3, 9.4
EXIG-IAM
Identité propre, jeton délégué à audience 
unique
PRIN-04 Autonomie propor­
tionnée
8.1 à 8.4, 12.1
EXIG-AUT, EXIG-CON
Niveau déclaré au registre, sous le plafond de 
la classe
PRIN-05 Réversibilité
7.5, 7.6, 8.5
EXIG-ORC, EXIG-AUT
Idempotence, compensation, approbation des 
actions P3
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 28 sur 283


---
## [Page PDF 29]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
Principe
Sections
Exigences
Preuve contrôlée en revue
PRIN-06 Traçabilité
10.1, 10.3, 10.6
EXIG-OBS, EXIG-FIN
Trace complète, journal d’audit, coût par tâche
PRIN-07 Défiance
9.5, 9.6, 9.9
EXIG-SEC
Tests d’injection concluants, outils d’envoi reti­
rés
PRIN-08 Déterminisme et 
simplicité
7.1 à 7.3, 7.9
EXIG-ORC
Patron justifié, sorties validées, plafonds décla­
rés
PRIN-09 Découplage des 
fournisseurs
5.2, 5.4, 13.3
EXIG-ARC, EXIG-APP
Passerelle de modèles, formats exportables, 
clause de sortie
PRIN-10 Humain imputable
11.1, 11.2, 11.4, 11.5
EXIG-GOV
Propriétaire nommé, attestation à jour
PRIN-11 Découplage interne
5.2, 5.5, 7.4
EXIG-ARC, EXIG-ORC
Déploiements distincts, état persisté hors pro­
cessus
PRIN-12 Dégradation maîtri­
sée
7.8, 9.4, 12.8
EXIG-ORC, EXIG-IAM, 
EXIG-CON
Repli configuré, coupe-circuit testé
Lorsqu’aucune exigence ne couvre une situation (nouveau protocole, nouveau type d’agent, usage imprévu), 
l’architecte doit consigner dans la décision d’architecture le raisonnement tenu à partir des principes, en 
nommant les principes invoqués. Le comité d’architecture et des risques agentiques décide ensuite s’il faut 
créer une exigence à la révision suivante du cadre.
4.3 Arbitrage entre principes et dérogations
Les principes se renforcent le plus souvent, mais ils peuvent tirer en sens contraires. Choix du cadre : en 
cas de conflit, l’ordre de préséance suivant s’applique.
1. Le droit applicable et les engagements contractuels, qu’aucun principe ne peut écarter (chapitre 12).
2. Les principes qui protègent les personnes et les systèmes et qui fondent l’imputabilité : PRIN-03 à 
PRIN-07, PRIN-10 et PRIN-12.
3. Les principes d’architecture : PRIN-01, PRIN-02, PRIN-08, PRIN-09 et PRIN-11.
À rang égal, on retient l’option la plus simple qui respecte les deux principes en présence, et l’arbitrage est 
consigné dans la décision d’architecture. Le tableau 10 illustre les tensions les plus fréquentes.
Tableau 10 — Tensions fréquentes entre principes et arbitrage retenu
Principes en tension
Situation
Arbitrage du cadre
PRIN-01 et PRIN-08
Un outil ne sert qu’à un seul agent, 
dans la même unité de déploiement; 
l’exposer par MCP ajoute un compo­
sant.
PRIN-01 vise les échanges qui franchissent une frontière de 
domaine; à l’intérieur, une fonction locale suffit. Dès qu’un 
second consommateur apparaît, l’outil passe au catalogue.
PRIN-05 et PRIN-10
Exiger une approbation humaine pour 
chaque action semble plus sûr, mais 
des approbateurs saturés approuvent 
machinalement.
Une approbation donnée sans examen n’apporte ni sécurité 
ni imputabilité; l’OWASP range cette saturation parmi les 
menaces (T10)[87]. On rend l’action compensable quand c’est 
possible et aux niveaux N3 et N4, l’on réserve l’approbation 
aux actions P3 et aux dépassements de seuils (au niveau N2, 
chaque écriture reste approuvée) (section 8.7).
PRIN-06 et protec­
tion des renseigne­
ments personnels (RP)
Tracer le contenu des invites et des ré­
ponses aide au diagnostic, mais expose 
des RP.
La protection des RP l’emporte : les métadonnées sont tou­
jours tracées; par choix du cadre, le contenu est exclu par 
défaut, activé sur décision documentée et conservé hors des 
traces (section 10.2).
PRIN-07 et utilité
Une défense par conception coûte en 
utilité : sur le banc d’essai AgentDojo, 
CaMeL (Debenedetti et coll., mars 2025) 
accomplit 77 % des tâches avec une 
sécurité démontrable, contre 84 % pour 
un système sans défense[101].
La classe de risque tranche : pour la classe de risque élevé, 
on accepte la perte d’utilité. Si le risque résiduel reste intolé­
rable, le NCSC estime qu’un modèle de langage n’est peut-
être pas la bonne solution[98].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 29 sur 283


---
## [Page PDF 30]

CRE-IA-2026-01 · Cadre de référence
4 Principes directeurs
Dérogations
Un écart à un principe doit faire l’objet d’une dérogation écrite, approuvée par le comité d’architecture et 
des risques agentiques (ou, pour un agent de classe faible, par délégation à l’architecture d’entreprise, pour 
90 jours au plus), limitée à six mois au plus, assortie de mesures compensatoires et d’un plan de retour à 
la conformité, et inscrite au registre (section 11.6). Une dérogation vise un agent ou un composant précis, 
jamais une catégorie entière; à son échéance, elle ne peut être renouvelée qu’une seule fois, par décision du 
comité (EXIG-GOV-16); sinon l’écart est corrigé ou l’agent passe à l’état « suspendu ».
SANS DÉROGATION POSSIBLE
Choix du cadre : aucune dérogation n’est admise pour l’autonomie non bornée (NX), pour l’exécution 
par un agent seul d’une action de palier P3, pour la mise en production d’un agent sans personne 
nommée qui en répond, pour l’usurpation, par un agent, de l’identité de son mandant, ni pour le 
dépassement du plafond d’autonomie de la classe de risque (EXIG-GOV-17). Une dérogation ne peut 
pas non plus écarter une obligation légale ou réglementaire.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 30 sur 283


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
