# chunk_24 — pages PDF 231 à 242 (sur 283)



---
## [Page PDF 231]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
E Glossaire
Ce glossaire réunit, par ordre alphabétique, les termes et les sigles du cadre, avec leur équivalent anglais 
d’usage courant et une définition brève qui renvoie à la section où chacun est traité. Les définitions 
reprennent le sens que le document donne à chaque terme; lorsqu’un terme vient d’une norme ou d’un texte 
de loi, la source est indiquée, et ce que le cadre y ajoute est signalé comme un choix du cadre. En cas d’écart 
entre une définition abrégée et le corps du document, le corps du document prévaut.
Conventions
• Classement. Les entrées suivent l’ordre alphabétique du terme français, sans tenir compte des accents, 
des apostrophes ni du contenu des parenthèses. Un sigle d’usage courant suit le terme entre parenthèses; 
les sigles et les noms propres sans équivalent français (par exemple A2A, AAIF, CIBA, CloudEvents, 
FinOps, MCP, OAuth, OBO, OpenTelemetry, SPIFFE) sont classés tels quels.
• Typographie. L’équivalent anglais figure en italique. Les noms de champs, de méthodes, d’en-têtes et 
d’attributs sont en police à chasse fixe.
• Force normative. Le glossaire ne crée aucune exigence. Les mots doit, devrait et peut gardent le sens 
fixé à la section 1.4, et les définitions normatives des termes de base figurent à la section 3.1.
Tableau 65 — Glossaire des termes et des sigles du cadre
Terme (sigle)
Équivalent anglais
Définition
A2A (protocole 
Agent2Agent)
Agent2Agent (A2A) protocol
Protocole ouvert d’intégration horizontale qui relie un agent à un 
autre agent autonome, potentiellement opaque, qui raisonne et 
conserve un état sur plusieurs tours. Projet de l’AAIF, annoncé publi­
quement le 17 août 2026, il est retenu par le cadre dans sa version 
de protocole 1.0, avec trois liaisons standard (JSON-RPC, gRPC, 
HTTP+JSON) et l’en-tête A2A-Version à chaque requête[5, 68]. Voir la 
section 6.6.
AAIF
Agentic AI Foundation
Fonds dirigé de la Linux Foundation, créé le 9 décembre 2025 et 
cofondé par Anthropic, Block et OpenAI, qui héberge des projets 
agentiques sous gouvernance neutre, dont MCP, A2A, agentgateway 
et Agent Router; il en compte dix au 22 octobre 2026[4, 130, 193]. Un 
projet n’est un « standard AAIF » qu’une fois son admission approu­
vée et annoncée. Voir la section 6.9.
Agent
AI agent
Selon ISO/IEC 22989:2022 (3.1.1), entité automatisée qui perçoit son 
environnement, y réagit et agit pour atteindre ses buts[59]. Dans le 
cadre : système logiciel qui poursuit un objectif en dirigeant lui-
même sa boucle « raisonner, agir, observer » (ReAct) au moyen d’un 
modèle, d’outils et d’un état, sous un niveau d’autonomie déclaré[84]. 
Un agent n’est ni une personne, ni un compte d’utilisateur, ni un 
principal de service partagé; une personne nommée en répond. Voir 
les sections 3.1 et 3.4.
Agent ambiant
ambient agent
Agent qui écoute un flux d’événements et agit en conséquence, 
éventuellement sur plusieurs événements à la fois, sans être néces­
sairement entièrement autonome (définition de LangChain)[86]. Il tra­
vaille en arrière-plan, à la différence d’un agent interactif, sollicité par 
une personne qui attend sa réponse, et rejoint les personnes par une 
boîte de réception persistante (notifier, questionner, réviser). Voir les 
sections 3.3 et 8.6.
Analyse d’impact sur 
les droits fondamen­
taux (AIDF)
fundamental rights impact 
assessment (FRIA)
Analyse que l’article 27 du RIA exige de certains déployeurs de sys­
tèmes à haut risque avant la première utilisation; elle peut renvoyer 
aux sections pertinentes de l’analyse d’impact relative à la protection 
des données (AIPD) du Règlement général sur la protection des 
données (RGPD) ou en intégrer des parties[58, 61]. Le cadre l’intègre à 
l’évaluation d’impact unifiée de chaque agent de classe élevée. Voir 
la section 12.9.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 231 sur 283


---
## [Page PDF 232]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Annotation d’outil
tool annotation
Métadonnée qu’un serveur MCP déclare sur un outil : un titre (title) 
et quatre indices (readOnlyHint, destructiveHint, idempotentHint, 
openWorldHint). La spécification demande aux clients de tenir les 
annotations pour non fiables, sauf si elles proviennent de serveurs 
de confiance[197]. Le palier, le seuil et la compensation d’un outil se 
lisent au catalogue d’entreprise, jamais dans ses annotations. Voir la 
section 6.5.
Approbation humaine
human approval
Décision explicite d’une personne habilitée qui autorise une action 
précise avant son exécution. Dans le cadre, elle prend la forme d’un 
jeton d’approbation signé, lié à l’action exacte et vérifié par la passe­
relle d’agents. Un acquiescement dans la conversation, un résumé 
rédigé par l’agent ou une confirmation locale dans son interface n’en 
sont jamais une. Voir la section 8.5.
Approbation machinale
rubber-stamping
Approbation donnée sans examen réel, sous l’effet du volume, de 
la fatigue ou du biais d’automatisation, soit la tendance à se fier 
excessivement à une sortie automatisée. L’OWASP (Open Worldwide 
Application Security Project) range la saturation délibérée des appro­
bateurs parmi les menaces (T10, Overwhelming Human in the Loop)
[87]. Le cadre la prévient par des files priorisées selon le risque et par 
la mesure du taux d’approbation sans modification. Voir la section 
8.7.
AsyncAPI
AsyncAPI
Spécification ouverte qui décrit de façon lisible par machine les 
canaux, les opérations d’envoi (send) ou de réception (receive) et les 
messages d’une application asynchrone. Le cadre retient la version 
3.x (3.0.0 du 5 décembre 2023; 3.1.0 du 31 janvier 2026, version 
mineure sans rupture) pour le contrat de chaque sujet du bus 
d’événements[174, 249]. Voir la section 6.7.
Bac à sable
sandbox
Environnement d’exécution isolé, éphémère et sans privilèges où 
s’exécute le code qu’un agent génère ou reçoit d’une source non 
fiable : microVM (Firecracker, Kata Containers), gVisor ou WebAs­
sembly (WASI), jamais un conteneur à noyau partagé (choix du 
cadre). Il démarre sans accès réseau, ne contient aucun secret, ap­
plique des délais à trois niveaux et est journalisé de l’extérieur. Voir 
la section 9.7.
Bloc de construction 
d’architecture (ABB) et 
de solution (SBB)
architecture building block; 
solution building block
Notions de TOGAF : l’ABB capture les exigences d’architecture et 
oriente le développement des SBB; le SBB est le produit ou le com­
posant qui met en œuvre la fonction et dépend du fournisseur[121]. 
Dans le cadre, la passerelle d’agents est un ABB neutre et durable; le 
produit qui la réalise est un SBB remplaçable. Voir la section 5.4.
Bus d’événements
event bus; event broker
Courtier qui transporte des événements entre producteurs et 
consommateurs qui s’ignorent, par exemple Apache Kafka. Il dé­
couple les échanges dans le temps, admet plusieurs abonnés et 
permet le rejeu des entrées, mais Kafka livre par défaut « au moins 
une fois »[140] : un effet réel n’est protégé que par l’idempotence du 
consommateur et du système cible. Voir la section 6.7.
Cadriciel
framework; agent framework
Bibliothèque logicielle qui structure la logique d’un agent ou d’une 
orchestration, par exemple LangGraph, Microsoft Agent Framework, 
Google ADK ou OpenAI Agents SDK. Le cadre le traite comme 
un bloc de solution remplaçable : entre agents, seuls les contrats 
publiés font foi. Voir la section 7.10.
Carte d’agent
Agent Card
Document JSON par lequel un agent A2A déclare son identité, 
ses compétences, ses interfaces et ses exigences de sécurité. En 
A2A 1.0, elle compte huit champs obligatoires (name, description, 
supportedInterfaces, version, capabilities, defaultInputModes, 
defaultOutputModes, skills), et un agent exposé la publie à 
/.well-known/agent-card.json [68]. Le cadre exige qu’elle soit signée 
(JWS sur la carte canonisée JCS), versionnée selon SemVer et inscrite 
au registre. Voir la section 6.6 et l’annexe C.
Catalogue d’entreprise
enterprise catalog
Source unique de ce qu’un agent peut joindre : outils, serveurs MCP, 
cartes d’agent et contrats d’événements, chacun avec sa version et 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 232 sur 283


---
## [Page PDF 233]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
son empreinte approuvées, son palier, son seuil, sa compensation et 
son propriétaire. La passerelle d’agents en tire sa liste d’autorisation; 
un élément absent du catalogue est injoignable. Le registre répond à 
« qui, quoi, pourquoi et avec quel risque », le catalogue à « par quel 
contrat et dans quelle version ». Voir les sections 6.8 et 11.4.
Catalogue des proto­
coles
protocol and standards cata­
log
Liste des protocoles et standards admis par le cadre, avec leur 
version de référence et l’un de quatre statuts : Adopter (usage par 
défaut), Évaluer (pilotes encadrés), Surveiller (veille, hors production) 
ou Contenir (existant toléré derrière un adaptateur, sans nouvel 
usage). Le comité le révise au moins chaque trimestre. Voir les sec­
tions 6.3 et 11.7.
Chorégraphie
choreography
Coordination décentralisée dans laquelle chaque agent réagit aux 
événements d’un bus et publie les siens, sans composant central qui 
dirige le flux. Le cadre l’assortit d’un propriétaire de bout en bout, 
d’une saga explicite, d’un contexte de trace et d’un compteur de 
sauts. Voir les sections 6.7 et 7.2.
CIBA
Client-Initiated Backchannel 
Authentication
Spécification finale de l’OpenID Foundation (CIBA Core 1.0) qui 
découple l’appareil où s’exécute le client de celui où la personne 
s’authentifie; un court binding_message, affiché sur les deux appareils, 
rattache la demande à l’action[310]. Le cadre la recommande pour 
l’approbation hors bande, notamment des actions P3 et des agents 
sans interface. Voir la section 8.5.
Classe de risque
risk class
Mesure de ce qui arrive si l’agent se trompe : faible, modérée ou 
élevée. La classe retenue est la plus élevée dont un critère est rempli, 
jamais une moyenne. Elle fixe le plafond d’autonomie : N2 pour la 
classe élevée, qui comprend les systèmes à haut risque du RIA et les 
décisions visées par l’article 12.1 de la Loi sur le privé; N3 pour les 
classes modérée et faible; N4 pour la classe faible, sur décision du 
comité. Voir les sections 8.1 et 12.1.
CloudEvents
CloudEvents
Spécification de la Cloud Native Computing Foundation (CNCF) qui 
normalise l’enveloppe d’un événement. Le cadre retient la version 
1.0 (révision 1.0.2), dont les quatre attributs requis sont id, source, 
specversion et type [248]. Le contrat de chaque sujet se décrit en 
AsyncAPI 3.x, et le cadre ajoute des extensions de gouvernance 
(contexte de trace, mandant, classification, compteur de sauts). Voir 
la section 6.7.
Comité d’architecture et 
des risques agentiques
agentic architecture and risk 
committee
Instance décisionnelle du cadre, dotée d’un mandat écrit. Le comité 
approuve les agents de classe élevée et tout niveau N4, accorde 
les dérogations, approuve le catalogue des protocoles et révise le 
cadre chaque semestre; ses décisions sont motivées et consignées 
au registre. Voir la section 11.1.
Commission d’accès à 
l’information (CAI)
Commission d’accès à 
l’information (nom officiel)
Organisme québécois chargé de surveiller l’application des lois sur 
l’accès à l’information et sur la protection des renseignements per­
sonnels. Elle reçoit les avis d’incidents de confidentialité présentant 
un risque de préjudice sérieux et peut imposer des sanctions admi­
nistratives pécuniaires[317]. Le cadre recommande son guide d’EFVP. 
Voir les sections 12.2 et 12.8.
Compensation
compensating transaction
Action métier qui neutralise ou corrige l’effet d’une étape déjà 
exécutée lorsqu’une saga ne peut aboutir : remboursement, avis rec­
tificatif, libération de stock. Elle ne rétablit pas forcément l’état initial. 
Le cadre exige qu’elle soit déclarée au catalogue, idempotente, jour­
nalisée avant l’action qu’elle couvre et déclenchée seulement après 
l’épuisement des réessais. Voir la section 7.5.
Compétence
skill
Capacité qu’un agent publie dans sa carte d’agent; en A2A 1.0, 
chaque compétence exige id, name, description et tags et peut por­
ter ses propres exigences de sécurité[192]. Le cadre associe une portée 
OAuth dédiée à chaque compétence. Le terme désigne aussi les pa­
quets de compétences d’agents, traités comme des composants de 
la chaîne d’approvisionnement. Voir les sections 6.6 et 9.8.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 233 sur 283


---
## [Page PDF 234]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Compteur de sauts
hop count
Extension CloudEvents propre au cadre (xagenthopcount, avec le pla­
fond xagentmaxhops, fixé à 4 par défaut) qui compte les publications 
d’agents dans une chaîne causale. Un agent qui reçoit un événement 
ayant atteint le plafond ne le traite pas, le dirige vers la file de lettres 
mortes et lève une alerte : les boucles entre agents sont coupées de 
façon déterministe. Voir la section 6.7.
Confiance zéro
zero trust
Modèle de sécurité défini par la publication NIST SP 800-207 
(août 2020) : aucune confiance implicite n’est accordée selon 
l’emplacement réseau, et l’authentification et l’autorisation pré­
cèdent l’accès à chaque ressource[112]. Le cadre va au-delà de l’accès 
par session : chaque appel d’un agent est authentifié et autorisé 
individuellement. Voir la section 9.1.
Contenu non fiable
untrusted content
Tout contenu qui ne provient ni du mandant authentifié ni de 
la configuration approuvée de l’agent : pages Web, courriels, do­
cuments téléversés, champs libres des systèmes d’enregistrement, 
réponses d’outils, entrées de mémoire, messages et cartes d’autres 
agents. Il est traité comme une donnée, jamais comme une instruc­
tion; sa lecture entraîne le retrait des outils d’envoi externe et des 
outils P3 pour le reste de la session. Voir la section 9.6.
Contrat
contract
Description lisible par machine qui fait foi entre un agent ou un 
outil et ses consommateurs : définition d’outil MCP, carte d’agent, 
contrat AsyncAPI ou OpenAPI. Le contrat d’agent précise en outre les 
entrées, les sorties, les limites, le niveau d’autonomie et les niveaux 
de service. Tout contrat est versionné, épinglé et inscrit au catalogue; 
la description d’un outil en fait partie. Voir la section 6.8 et l’annexe 
C.
Coupe-circuit
kill switch
Mécanisme qui, en une seule action, suspend un agent, un outil, un 
serveur MCP ou une catégorie d’actions sur toutes les passerelles, 
désactive l’identité de l’agent et diffuse la révocation aux systèmes 
raccordés, par exemple au moyen des événements du Continuous 
Access Evaluation Profile (CAEP) du Shared Signals Framework[344]. 
Son délai de bout en bout est mesuré lors d’un exercice au moins 
trimestriel (choix du cadre). Voir les sections 7.8 et 9.4.
Décision fondée exclu­
sivement sur un traite­
ment automatisé
decision based exclusively 
on automated processing
Décision concernant une personne fondée exclusivement sur un trai­
tement automatisé de ses RP (art. 12.1 de la Loi sur le privé; art. 
65.2 de la Loi sur l’accès). La personne en est informée au plus 
tard au moment de la décision, peut obtenir les RP utilisés et 
les principaux facteurs et paramètres, et présenter ses observations 
à un membre du personnel en mesure de réviser la décision[160]. 
Selon l’interprétation gouvernementale de l’article 65.2 (organismes 
publics), une intervention humaine mineure ne retire pas ce carac­
tère; la CAI n’a pas publié de critères pour le secteur privé, et le 
cadre applique cette interprétation par analogie à l’article 12.1. Voir 
les sections 8.8 et 12.2.
Délégation
delegation
Transfert, borné en portée et en durée, du droit d’agir d’un mandant 
vers un agent, ou d’une tâche d’un agent vers un autre. Au sens 
de la RFC 8693, l’acteur conserve une identité distincte de celle 
du sujet pour lequel il agit; dans l’usurpation d’identité (impersona­
tion), l’acteur devient indiscernable du sujet[69]. Le cadre interdit 
l’usurpation et exige la délégation explicite. Voir la section 9.3.
Déployeur
deployer
Selon l’article 3(4) du RIA, personne ou organisme qui utilise un sys­
tème d’IA sous sa propre autorité[61]. Un déployeur devient fournis­
seur s’il appose son nom ou sa marque sur un système à haut risque 
déjà mis sur le marché, s’il y apporte une modification substantielle 
ou s’il modifie la destination d’un système non classé à haut risque 
de sorte qu’il le devienne (art. 25(1)). Voir la section 12.4.
Dérogation
waiver; exception
Exception écrite, temporaire et compensée à une exigence du cadre, 
accordée pour un agent ou un composant précis par le comité 
(ou, par délégation, par l’architecture d’entreprise pour un agent de 
classe faible, alors pour 90 jours au plus), pour six mois au plus et 
renouvelable une seule fois. Aucune dérogation n’est possible pour 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 234 sur 283


---
## [Page PDF 235]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
le niveau NX, une action P3 sans approbation humaine, l’usurpation 
d’identité, un agent sans fiche ni parrain, le dépassement du plafond 
d’autonomie ou une obligation légale. Voir la section 11.6.
Domaine de concep­
tion opérationnel (ODD), 
aussi appelé « domaine 
d’exploitation » dans le 
cadre
operational design domain
Notion de la conduite automatisée des véhicules routiers, empruntée 
par analogie; la taxonomie SAE J3016 est une pratique recomman­
dée et non une norme de sécurité[304]. Dans le cadre, périmètre do­
cumenté (systèmes, données, outils, seuils, volumes, plages horaires) 
hors duquel un agent s’arrête en état sûr, compense ou escalade. 
Il est exigé aux niveaux N3 et N4; le niveau N4 suppose un ODD 
certifié. Voir la section 8.1.
Échec en mode fermé
fail-closed
Comportement par lequel un composant refuse ou suspend plutôt 
que d’agir lorsqu’il ne peut pas obtenir une décision valide : ser­
vice de politiques ou d’approbation indisponible, politique absente, 
doute. La passerelle d’agents n’ouvre jamais le passage par défaut, 
et l’orchestrateur suspend la tâche dans un état reprenable. Voir les 
sections 8.4 et 9.4.
Empoisonnement 
d’outil
tool poisoning
Attaque qui cache des instructions malveillantes dans la description, 
le schéma ou les valeurs de retour d’un outil. L’ombrage (tool shado­
wing), variante voisine, laisse la description d’un serveur malveillant 
modifier l’usage des outils d’un autre serveur[221]. Le cadre y répond 
par l’épinglage des définitions par empreinte et par l’isolement de 
chaque serveur. Voir les sections 6.5 et 9.8.
Empreinte
digest; fingerprint
Condensé cryptographique, par exemple SHA-256, calculé sur un 
contenu canonisé selon la RFC 8785 (JCS), RFC informative de la 
filière indépendante[236]. Le cadre s’en sert pour épingler les défini­
tions approuvées des outils et des cartes, tout écart bloquant l’appel 
jusqu’à une nouvelle approbation, et pour lier une approbation à 
l’action exacte : h = SHA-256(identifiant de l’outil ‖ arguments cano­
nisés). Voir les sections 6.8 et 8.5.
Entreprise agentique
agentic enterprise
Organisation où des agents exécutent une part croissante des pro­
cessus, aux côtés des personnes et des systèmes existants, sous une 
supervision humaine proportionnée au risque. Voir la section 2.1.
Enveloppe budgétaire
task budget envelope
Ensemble des plafonds attribués à une tâche à son ouverture (jetons, 
coût, appels d’outils, itérations, durée d’exécution et durée totale), 
transmis avec les montants restants à chaque appel descendant. 
L’atteinte d’un plafond arrête la boucle en état sûr et déclenche 
l’escalade prévue; elle n’est jamais rapportée comme un succès. Voir 
les sections 7.8 et 10.6.
Équipe rouge
red team
Équipe indépendante de l’équipe de développement qui attaque un 
agent comme le ferait un adversaire : détournement d’objectif, exfil­
tration, empoisonnement d’outil et de mémoire, abus de délégation. 
Le cadre l’exige avant la mise en production des agents de classe 
modérée ou élevée, puis au moins chaque année. Voir la section 9.9.
Évaluation continue
continuous evaluation
Mesure répétée de la qualité, de la sécurité et du coût d’un agent, 
avant et pendant la production, en trois paliers : tests de contrats, 
jeux de trajectoires, y compris adverses, et échantillon du trafic réel. 
Elle est relancée à chaque changement de modèle, d’invite système 
ou d’outil, et ses résultats conditionnent l’homologation. Voir la sec­
tion 10.4.
Évaluation des facteurs 
relatifs à la vie privée 
(EFVP)
privacy impact assessment 
(PIA)
Évaluation exigée par la Loi sur le privé pour tout projet 
d’acquisition, de développement ou de refonte d’un système 
d’information impliquant des RP (art. 3.3) et avant toute communica­
tion de RP hors du Québec, autres provinces comprises (art. 17)[160]. 
Le cadre l’exige terminée avant le pilote, avec un inventaire des RP 
par outil, par délégation et par mémoire. Voir la section 12.2.
Exécutant
worker; subagent
Agent auquel un orchestrateur délègue une sous-tâche et qui rend 
une synthèse conforme au schéma de retour déclaré, ses livrables 
volumineux étant transmis par référence. Le cadre limite la déléga­
tion à deux niveaux : un exécutant ne délègue pas à son tour sans 
dérogation. Voir les sections 7.2 et 7.7.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 235 sur 283


---
## [Page PDF 236]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Exécution durable
durable execution
Mode d’exécution dans lequel un moteur persiste l’état d’une tâche 
hors du processus après chaque transition, de sorte qu’elle reprend 
où elle s’était arrêtée après une panne, un redéploiement ou une 
longue attente d’approbation. La persistance n’empêche pas, à elle 
seule, qu’une action soit répétée : les effets doivent aussi être idem­
potents. Voir la section 7.4.
FinOps
FinOps
Pratique de gestion financière qui maximise la valeur d’affaires de 
la technologie et rend les coûts imputables; le cadre FinOps cite la 
dépense d’IA agentique (par exemple pour la productivité des déve­
loppeurs) comme pouvant former un périmètre de dépenses (Scope) 
distinct[406, 469]. La spécification FOCUS normalise les données de 
facturation, pas les indicateurs par agent : le coût par tâche réussie 
se calcule en joignant ces données à la télémétrie et aux résultats 
métier. Voir les sections 10.5 et 10.6.
Flux déterministe
deterministic workflow
Séquence prédéterminée (graphe ou machine à états) dont le code 
fixe le chemin; certaines étapes peuvent appeler un modèle ou un 
agent borné pour traiter de l’information non structurée, ce qu’on 
appelle aussi un flux de travail assisté par IA. Anthropic distingue de 
même les flux de travail, orchestrés par des chemins de code prédé­
finis, des agents, où le modèle dirige son propre processus[65]. C’est 
le patron par défaut du cadre. Voir les sections 3.2 et 7.2.
Garde-fou
guardrail
Contrôle automatisé qui filtre ou valide les entrées, les sorties ou 
les actions d’un agent : validation de schéma, détection d’injection, 
masquage des RP et des secrets. Il s’applique à l’entrée, aux appels 
d’outils, aux réponses d’outils et à la sortie finale. Un garde-fou 
probabiliste réduit le risque sans l’éliminer et ne remplace jamais un 
contrôle déterministe. Voir les sections 7.7 et 9.6.
Homologation
go-live approval
Décision consignée au registre qui autorise la mise en production 
d’un agent à un niveau d’autonomie donné, sur la foi de preuves : 
rapport d’évaluation, tests de sécurité, EFVP au besoin et grille 
d’homologation de l’annexe A. Le responsable technique d’un agent 
ne peut pas l’homologuer. Voir la section 11.5 et l’annexe A.
Humain dans la boucle 
(HITL)
human in the loop
Mode de supervision dans lequel une personne approuve chaque 
action en écriture avant son exécution, au moyen d’une approbation 
liée à l’action exacte; il caractérise le niveau N2. Voir les sections 8.1 
et 8.5.
Humain sur la boucle 
(HOTL)
human on the loop
Mode de supervision dans lequel l’agent agit seul sous des seuils 
déclarés, tandis qu’une personne supervise par exception, traite les 
escalades, peut interrompre et revoit a posteriori un échantillon des 
actions; il caractérise le niveau N3. Au niveau N4, la personne est 
hors de la boucle d’exécution, mais reste sur la boucle de gouver­
nance. Voir la section 8.1.
IA fantôme
shadow AI
Usage de l’IA hors de la gouvernance de l’entreprise. Un agent 
fantôme est un agent créé ou exploité hors du registre, sans proprié­
taire nommé ni moyen de révocation; le cadre le détecte par un 
rapprochement mensuel du registre avec des sources indépendantes 
et le place en quarantaine jusqu’à son inscription ou son retrait. Voir 
les sections 2.1 et 11.4.
Idempotence
idempotency
Propriété d’une opération dont l’exécution répétée produit le même 
effet qu’une exécution unique. Le cadre exige, pour toute écriture 
P2 ou P3, une clé d’idempotence dérivée des identifiants de la tâche 
et de l’étape, réutilisée à chaque réessai et vérifiée par le service 
visé; l’en-tête Idempotency-Key n’est encore qu’un brouillon de l’IETF 
(Internet Engineering Task Force)[78]. Voir la section 7.6.
Identité non humaine
non-human identity (NHI)
Identité attribuée à une charge de travail, à un service ou à un agent 
plutôt qu’à une personne. Dans le cadre, chaque agent possède la 
sienne, fondée sur un justificatif cryptographique de courte durée 
émis par la plateforme, jamais partagée ni utilisée par une personne. 
L’OWASP Non-Human Identities Top 10 (2025) en recense les dix 
risques principaux, de NHI1 à NHI10[470]. Voir la section 9.2.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 236 sur 283


---
## [Page PDF 237]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Injection d’instructions
prompt injection
Attaque par laquelle un texte placé par un tiers dans un contenu 
que lit le modèle (page Web, document, réponse d’outil, message 
d’agent) est interprété comme une consigne; elle est dite indirecte 
lorsqu’elle n’arrive pas par la personne qui utilise l’agent. Le cadre 
présume l’injection possible dès qu’un modèle lit du contenu non 
fiable, comme le recommande le NIST[97]. Voir la section 9.6.
Interopérabilité
interoperability
Capacité de systèmes et d’agents hétérogènes à échanger de 
l’information et à l’utiliser correctement sans adaptation propre à 
chaque paire. Le cadre l’examine aux quatre niveaux du Cadre 
européen d’interopérabilité (EIF, 2017) : juridique, organisationnel, 
sémantique et technique, sous une gouvernance intégrée[157]. Voir la 
section 6.1.
Invite
prompt
Texte d’instructions et de contexte fourni à un modèle. L’invite 
système d’un agent relève de sa mémoire procédurale et se gère 
comme du code : revue, version, évaluation avant déploiement. Dans 
MCP, une invite est aussi une primitive serveur, soit un gabarit réuti­
lisable obtenu par prompts/get. Voir les sections 5.5 et 6.5.
Jeton (unité de texte)
token
Unité de texte que lit ou produit un modèle de langage; elle sert 
d’unité de mesure de la consommation et de la facturation de 
l’inférence. À ne pas confondre avec le jeton d’accès OAuth, qui 
porte des droits. Voir les sections 10.5 et 10.6.
Jeton contraint à 
l’émetteur
sender-constrained token
Jeton d’accès lié à une clé ou à un certificat que seul son déten­
teur légitime peut présenter : mTLS (RFC 8705, revendication cnf 
« x5t#S256 ») dans le maillage de services, ou DPoP (RFC 9449, 
preuve JWT à chaque requête) hors du maillage. La RFC 9700 
recommande cette contrainte[175]; le cadre l’exige pour tout jeton qui 
donne accès à un outil P2 ou P3 ou que détient un agent de classe 
élevée. Voir la section 9.3.
Jeton d’approbation
approval token
Jeton signé par le service d’approbation adossé au fournisseur 
d’identité, qui contient au minimum l’empreinte de l’action approu­
vée, l’identifiant pseudonymisé de l’approbateur, les identifiants de 
la tâche et de l’agent, une date d’expiration et un identifiant à usage 
unique. La passerelle recalcule l’empreinte avant l’exécution; le cadre 
en limite la validité à 15 minutes. Voir la section 8.5 et l’annexe C.
Jeton délégué
delegated token
Jeton d’accès obtenu à chaque saut par échange de jetons (RFC 
8693); le cadre l’exige de courte durée et à audience unique. Il dé­
signe le mandant (sub) et l’agent courant (act), avec un act imbriqué 
par acteur antérieur[70]. Sa portée ne dépasse jamais les droits effec­
tifs, soit droits du mandant ∩ portée de l’agent ∩ portée de la tâche 
(choix du cadre), intersection appliquée par le serveur d’autorisation 
à chaque échange. Voir la section 9.3 et l’annexe C.
Journal d’audit
audit log
Enregistrement inaltérable et signé, distinct des traces, de chaque 
action d’agent : mandant, agent et version, outil et empreinte de 
ses arguments, modèle et version, approbation, identifiants de tâche 
et de trace, règle appliquée par la passerelle. Il sert à la preuve, à 
l’explication des décisions et à l’enquête. Voir la section 10.3.
Loi 25
Law 25; Act to modernize 
legislative provisions as re­
gards the protection of per­
sonal information
Loi modernisant des dispositions législatives en matière de protec­
tion des renseignements personnels (L.Q. 2021, c. 25), en vigueur 
dans son ensemble depuis le 22 septembre 2024, dernière étape 
(droit à la portabilité)[7, 56]. Elle modifie la Loi sur la protection des 
renseignements personnels dans le secteur privé (RLRQ, c. P-39.1, 
« Loi sur le privé ») et la Loi sur l’accès aux documents des orga­
nismes publics et sur la protection des renseignements personnels 
(RLRQ, c. A-2.1, « Loi sur l’accès »). Voir la section 12.2.
Mandant
principal
Personne, application ou agent au nom duquel une tâche est exécu­
tée; pour un déclencheur système, identité du service et de son pro­
priétaire nommé. Le mandant est établi à l’entrée, transporté dans 
chaque appel par le jeton délégué et consigné au journal d’audit; les 
droits d’un agent ne dépassent jamais les siens. Voir les sections 5.2 
et 9.3.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 237 sur 283


---
## [Page PDF 238]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
MCP (Model Context 
Protocol)
Model Context Protocol
Protocole ouvert d’intégration verticale qui relie un agent à des ou­
tils, à des ressources et à des invites exposés par des serveurs; l’hôte, 
soit l’application d’IA, crée un client MCP par serveur. Annoncé par 
Anthropic le 25 novembre 2024 et confié à l’AAIF le 9 décembre 
2025, il est versionné par date[20, 34]. Le cadre retient la révision 
2026-07-28, sans état, exposée par Streamable HTTP en environne­
ment serveur (choix du cadre). Voir la section 6.5.
Mémoire d’agent
agent memory
Ce qu’un agent conserve au-delà d’un appel au modèle. La taxono­
mie CoALA distingue une mémoire de travail et trois mémoires à 
long terme : épisodique (expériences passées), sémantique (connais­
sances) et procédurale (savoir-faire) [100]; le cadre limite cette der­
nière aux invites système, aux contrats de compétences et aux flux 
d’outils validés. Le contexte du modèle n’est pas une mémoire, et la 
mémoire procédurale se gère comme du code. Voir la section 5.5.
Modèle
model; large language mo­
del (LLM)
Composant probabiliste, le plus souvent un grand modèle de lan­
gage, qui produit une sortie à partir d’une invite. Un agent désigne 
ses modèles par un alias logique et ne les appelle que par la passe­
relle de modèles; la version réellement servie est consignée dans la 
télémétrie, et tout changement de modèle déclenche une réévalua­
tion. Voir les sections 5.2 et 11.5.
Moindre agence
least agency
Principe de l’OWASP selon lequel les outils et l’autonomie d’un 
agent se limitent à ce que la tâche exige : un comportement 
agentique déployé sans nécessité élargit la surface d’attaque sans 
ajouter de valeur[28]. Il complète le moindre privilège dans le principe 
PRIN-03. Voir les sections 4.1 et 8.1.
Niveau d’autonomie
autonomy level
Plafond déclaré au registre, de N0 à N4, qui fixe le rôle de la 
personne et ce que l’agent peut faire sans approbation : N0 automa­
tisation déterministe, sans modèle; N1 consultatif, sans écriture; N2 
exécution approuvée (HITL); N3 autonomie bornée et supervisée 
(HOTL); N4 autonomie étendue sous ODD certifié. NX, l’autonomie 
non bornée, est interdite. Le niveau ne dépend ni du nombre 
d’agents ni de la capacité du modèle. Voir la section 8.1.
OAuth 2.0 et OAuth 2.1
OAuth 2.0; OAuth 2.1
Cadre d’autorisation de l’IETF. Le cadre se réfère à OAuth 2.0 profi­
lé par la RFC 9700 (BCP 240, janvier 2025). OAuth 2.1 reste un 
Internet-Draft, dont la version −16 date de septembre 2026[175, 176] : 
le cadre s’aligne sur son profil (PKCE, ni octroi implicite ni octroi par 
mot de passe) sans le présenter comme une norme publiée. Voir les 
sections 6.3 et 9.3.
OBO
On-Behalf-Of
Patron de délégation par lequel un service obtient un jeton pour agir 
au nom d’un utilisateur; ce n’est pas une norme. Le flux OBO de Mi­
crosoft Entra, par exemple, repose sur l’octroi jwt-bearer et non sur 
la RFC 8693[326], que le cadre retient comme référence normative en 
profilant au catalogue les variantes des fournisseurs. Voir la section 
9.3.
OpenTelemetry
OpenTelemetry (OTel)
Projet de la CNCF qui normalise la production et l’export des 
traces, des métriques et des journaux (API, SDK, protocole OTLP). 
Ses conventions sémantiques GenAI, qui nomment les spans et les 
attributs des modèles, des agents et des outils, sont au niveau de 
stabilité Development : un nom peut y changer sans processus de 
dépréciation[181, 188]. Le cadre en épingle donc une version. Voir la 
section 10.1.
Orchestrateur
orchestrator
Composant déterministe, agentique ou hybride qui décompose une 
demande, affecte les tâches à des agents ou à des outils, suit l’état, 
gère la reprise et consolide les résultats. Il choisit un chemin, mais 
n’accorde ni n’élargit aucun droit. Voir les sections 5.2 et 7.2.
Outil
tool
Capacité exposée à un agent (fonction, requête, action), décrite par 
un contrat d’entrée et de sortie et exécutée par un serveur MCP 
ou un adaptateur; un outil n’a aucune autonomie de décision. Règle 
du cadre : une cible aux entrées et aux sorties définies est un outil, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 238 sur 283


---
## [Page PDF 239]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
même si elle emploie un modèle en interne. Chaque outil reçoit un 
palier au catalogue. Voir les sections 6.2 et 6.5.
OWASP Top 10 agen­
tique (ASI)
OWASP Top 10 for Agentic 
Applications
Référentiel de menaces publié le 9 décembre 2025 par l’OWASP Ge­
nAI Security Project, de ASI01 (détournement de l’objectif de l’agent) 
à ASI10 (agents dévoyés)[28]. Le cadre en fait la base de la modélisa­
tion des menaces, obligatoire pour les agents de classe modérée ou 
élevée. Voir la section 9.5.
Palier d’outil
tool risk tier
Classement d’un outil selon l’effet de ses appels : P0 lecture pu­
blique; P1 lecture interne ou sensible; P2 écriture réversible ou com­
pensable, avec approbation au-delà d’un seuil; P3 action critique, 
externe ou irréversible, jamais exécutée seule par un agent. Le palier 
est attribué au catalogue après revue, jamais déduit des annotations 
du serveur; un outil d’écriture sans compensation déclarée est classé 
P3. Voir la section 8.3.
Passage de jeton (ou re­
lais de jeton)
token passthrough
Fait de retransmettre tel quel à un autre service un jeton reçu. 
La spécification d’autorisation MCP l’interdit[209], et le cadre étend 
l’interdiction à tout agent, outil ou serveur : chaque audience exige 
un nouveau jeton, obtenu par échange de jetons. Voir les sections 
6.5 et 9.3.
Passerelle d’agents
agent gateway
Mandataire inverse placé devant tous les serveurs MCP et tous les 
pairs A2A, pour le trafic entrant comme sortant, qui sert de point 
d’application des politiques. À chaque appel, elle authentifie l’agent 
et le mandant, vérifie le catalogue, autorise, applique les garde-fous, 
vérifie l’approbation, limite le budget, injecte les justificatifs en aval, 
filtre la sortie, puis trace et journalise. Voir les sections 5.2 et 9.4.
Passerelle de modèles
model gateway; LLM gate­
way
Point de passage obligatoire de tout appel d’inférence : elle centra­
lise les identifiants des fournisseurs, résout les alias logiques, assure 
le routage, le repli, le cache et les quotas de jetons, et impute les 
coûts. Aucun agent ne détient de clé de fournisseur de modèles ni 
n’appelle un fournisseur directement. Voir la section 5.2.
Patron d’orchestration
orchestration pattern
Topologie de coordination déclarée au registre parmi les huit 
patrons autorisés : flux déterministe, chaîne séquentielle, routage 
et transfert, parallélisation, orchestrateur et exécutants, évaluateur-
optimiseur, chorégraphie événementielle et agent unique outillé; le 
clavardage de groupe en est une variante encadrée. Le patron est 
distinct du niveau d’autonomie. Voir les sections 7.2 et 7.3.
Plan transversal
cross-cutting plane
Ensemble de services communs fournis à toutes les couches de 
l’architecture de référence : A Identité et sécurité; B Observabilité, 
évaluation et FinOps; C Gouvernance et registre. L’équipe plateforme 
les fournit une fois; un projet n’en déploie pas d’équivalent parallèle 
sans dérogation. Voir la section 5.3.
Point d’application des 
politiques (PEP)
policy enforcement point
Composant logique de la confiance zéro qui ouvre, surveille et 
termine les connexions selon la décision du moteur de politiques 
(PE), l’administrateur de politiques (PA) établissant ou coupant le 
chemin[112]. Dans le cadre, la passerelle d’agents et la passerelle de 
modèles sont des PEP, et le service de politiques tient le rôle de PE. 
Voir la section 9.1.
Point de contrôle
checkpoint; gate
(1) Instantané persistant de l’état complet d’une tâche, pris à chaque 
transition par le moteur d’exécution durable; il constitue une fron­
tière de confiance et se protège comme une donnée de production. 
(2) Porte du cycle de vie d’un agent, de la proposition au retrait, dont 
le franchissement est consigné au registre avec ses preuves. Voir les 
sections 7.4 et 11.5.
Propriétaire métier (par­
rain)
business owner; sponsor
Personne nommée qui répond de la finalité, des résultats, des effets 
et du retrait d’un agent; elle demande son niveau d’autonomie, le 
finance et atteste au moins tous les 12 mois, tous les 6 mois pour 
la classe élevée, qu’il est encore requis. Ce n’est jamais une équipe 
ni un fournisseur. Le rôle reprend la notion de parrain de Microsoft 
Entra Agent ID, sans dépendre du produit. Voir la section 11.1.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 239 sur 283


---
## [Page PDF 240]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Registre d’entreprise
enterprise agent registry
Inventaire faisant autorité des agents et des serveurs MCP qui 
agissent dans le périmètre de l’entreprise, qu’ils soient internes, 
intégrés à un logiciel-service ou exploités par un partenaire. Cha­
cun y a une fiche (propriétaires, finalité, classe de risque, niveau 
d’autonomie, outils et paliers, modèles, données, état du cycle de 
vie); sans fiche complète, aucun justificatif de production. Il est dis­
tinct du registre officiel MCP, en préversion, qui ne prend pas en 
charge les serveurs privés[43]. Voir la section 11.4 et l’annexe B.
Règlement européen 
sur l’IA (RIA)
EU Artificial Intelligence Act 
(AI Act)
Règlement (UE) 2024/1689, en vigueur depuis le 1er août 2024 et 
modifié par le règlement (UE) 2026/1744, qui reporte au 2 décembre 
2027 les obligations des systèmes à haut risque de l’annexe III et au 
2 août 2028 celles de l’annexe I[58, 61]. Il vise aussi les fournisseurs et 
les déployeurs établis hors de l’Union lorsque les sorties du système 
y sont utilisées. Voir la section 12.4.
Renseignements per­
sonnels (RP)
personal information
Renseignements qui concernent une personne physique et per­
mettent de l’identifier, au sens de la Loi sur le privé et de la 
Loi sur l’accès; un renseignement dépersonnalisé demeure un rensei­
gnement personnel. Le cadre traite comme des RP les inférences 
qu’un agent produit sur une personne et les plongements vectoriels 
(embeddings) calculés à partir de RP. Voir la section 12.2.
Responsable de la pro­
tection des renseigne­
ments personnels (RPRP)
person in charge of the pro­
tection of personal informa­
tion
Fonction exercée par la personne ayant la plus haute autorité dans 
l’entreprise, qui peut la déléguer par écrit (art. 3.1 de la Loi sur le 
privé)[160]. Le cadre le consulte dès le début de tout projet d’agent 
impliquant des RP et lui confie l’encadrement des EFVP et des inci­
dents de confidentialité. Voir la section 11.1.
Ressource
resource
Primitive MCP : donnée contextuelle adressée par URI, lue par 
resources/read et pouvant être mise en cache; pour le cadre, cette 
lecture n’a aucun effet de bord. Elle convient lorsque l’entité à char­
ger est connue d’avance; une recherche, un calcul ou une écriture 
relèvent d’un outil. Voir la section 6.5.
Saga
saga
Patron défini par Garcia-Molina et Salem en 1987[284], qui remplace 
une transaction globale par une suite de transactions locales, 
chacune appariée à une compensation; les étapes compensables 
précèdent le pivot, point de non-retour, que suivent des étapes 
réessayables[67]. Le cadre l’exige pour toute tâche qui écrit dans plu­
sieurs systèmes d’enregistrement sans transaction commune. Voir la 
section 7.5.
Serveur MCP
MCP server
Programme qui expose des outils, des ressources et des invites par 
MCP; c’est un adaptateur sans état cognitif, qui ne raisonne pas. 
Dans l’entreprise, tout serveur MCP est inscrit au registre et au 
catalogue, publié derrière la passerelle d’agents et traité comme un 
domaine de sécurité distinct. Voir les sections 6.5 et 11.4.
SPIFFE, SPIRE et SVID
Secure Production Identi­
ty Framework For Everyone; 
SPIFFE Runtime Environ­
ment; SPIFFE Verifiable Iden­
tity Document
Standard et mise en œuvre de référence de l’identité de charge de 
travail, projets diplômés de la CNCF. Un SPIFFE ID prend la forme 
spiffe://domaine-de-confiance/chemin; le justificatif, ou SVID, existe 
en X.509-SVID, à privilégier et renouvelé automatiquement, et en 
JWT-SVID, de courte durée et redemandé au besoin; la Workload API 
délivre les deux sans secret préalable[322, 471]. Voir la section 9.2.
Substitution après ap­
probation
rug pull
Attaque par laquelle l’éditeur d’un serveur ou d’un outil en modifie 
les définitions une fois celui-ci approuvé, par exemple pour y glisser 
de nouvelles consignes. La passerelle d’agents la neutralise en com­
parant à chaque appel l’empreinte des définitions présentées à celle 
qui est épinglée au catalogue. Voir les sections 6.5 et 9.8.
Système de manage­
ment de l’IA (SMIA)
AI management system
Système de management dont ISO/IEC 42001:2023 spécifie les exi­
gences selon la structure harmonisée des normes de systèmes de 
management (articles 4 à 10), complétée par 38 mesures en annexe 
A; la norme est certifiable par tierce partie (ISO/IEC 42006:2025)[450, 
451]. À ne pas confondre avec le brouillon IETF WIMSE « AI Identity 
Management System » (AIMS), qui porte sur l’identité des agents. 
Voir la section 12.5.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 240 sur 283


---
## [Page PDF 241]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Système 
d’enregistrement
system of record
Système qui fait foi pour une donnée de l’entreprise : ERP, CRM, 
système de dossiers, entrepôt de données, logiciel-service. Un agent 
n’y écrit que par une interface qui applique les contrôles métier de 
ce système, jamais par un accès direct aux tables. Voir la section 5.2.
Système d’IA
AI system
Selon l’article 3(1) du RIA, système automatisé conçu pour fonc­
tionner à différents niveaux d’autonomie, qui peut faire preuve 
d’adaptabilité après son déploiement et qui déduit, à partir des 
entrées qu’il reçoit, la manière de générer des sorties (prédictions, 
contenus, recommandations ou décisions) pouvant influencer des 
environnements physiques ou virtuels[61]. Le cadre considère tout 
agent comme un système d’IA. Voir la section 12.4.
Tâche (A2A)
task
Unité de travail A2A créée par l’agent serveur, qui lui attribue 
son identifiant (taskId); contextId regroupe les tâches et les 
messages d’une même interaction. Une tâche suit une machine 
à huit états de cycle de vie (l’énumération compte neuf va­
leurs avec TASK_STATE_UNSPECIFIED), dont deux états interrompus 
(INPUT_REQUIRED, AUTH_REQUIRED) et quatre états terminaux, et produit 
des artefacts composés de parties (Part)[68]. Voir la section 6.6.
Traçage
distributed tracing
Reconstitution de bout en bout du chemin d’une demande au 
moyen de traces OpenTelemetry, faites de spans reliés par un même 
contexte W3C Trace Context (en-tête traceparent), défini pour HTTP; 
le cadre exige de le propager aussi dans le champ _meta de MCP, 
dans A2A et dans l’extension CloudEvents Distributed Tracing[103, 162, 
253]. Le traceparent n’est pas un identifiant métier, et la trace ne 
remplace pas le journal d’audit. Voir la section 10.1.
Transfert
handoff
Cession explicite du contrôle d’une session, avec son contexte utile, 
d’un agent source vers un agent cible mieux qualifié; l’agent source 
se retire. Le transfert vise une liste fermée de destinataires et porte le 
mandant, pas tout l’historique. Voir la section 7.2.
Triade létale
lethal trifecta
Combinaison, nommée par Simon Willison, de l’accès à des données 
privées, de l’exposition à du contenu non fiable et de la capacité de 
communiquer vers l’extérieur, qui rend l’exfiltration possible[354]. La 
« règle de deux » de Meta en tire une règle de session : au plus deux 
des trois propriétés sans supervision[307]. Voir la section 9.6.
F Validation des sources et des ébauches
Cette annexe rend compte de la vérification qui fonde la version 1.0 : comment les 121 références de la 
recherche documentaire ont été validées, ce que la vérification a révélé, et quelles affirmations des ébauches 
ont été corrigées ou retirées. Elle permet à tout lecteur de retracer l’origine d’un fait et le degré de confiance 
qu’on peut lui accorder.
F.1 Méthode
La vérification s’est déroulée en trois passes, les 27 et 28 octobre 2026.
1. Validation référence par référence. Chacune des 121 références de la recherche documentaire a fait 
l’objet d’une tentative d’ouverture; pour les 13 pages bloquées, payantes ou redirigées, on s’est limité 
au résumé public ou à une source primaire. On a consigné son accessibilité, son éditeur, sa date et sa 
catégorie de crédibilité, puis confronté chaque affirmation qui la citait au contenu réel de la page (427 
liens affirmation-source au total). Lorsqu’une page n’appuyait pas une affirmation, une source primaire 
a été recherchée pour la confirmer ou la réfuter.
2. Vérification thématique. Onze vérifications ont confronté les affirmations des quatre ébauches aux 
textes primaires  : MCP; A2A et protocoles connexes; plateformes et fondations; identité; sécurité; 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 241 sur 283


---
## [Page PDF 242]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
observabilité, contrats et événements; orchestration; autonomie; droit québécois et canadien; référen­
tiels internationaux; économie et données de marché. Elles ont aussi recueilli les faits complémentaires 
intégrés au cadre.
3. Audit final. Le 28 octobre 2026, chacune des 428 références alors citées dans le corps du cadre a été 
rouverte à sa source et confrontée, affirmation par affirmation, aux passages qui s’y appuient (1 409 
affirmations examinées). L’identité de chaque référence (auteurs, titre, date, éditeur), sa catégorie et 
son statut à cette date ont été contrôlés, et les écarts les plus graves ont été recontrôlés par un second 
examinateur indépendant, qui a réfuté plusieurs reclassements proposés. En parallèle, tous les chapitres 
et annexes ont été relus pour la cohérence interne, l’exactitude factuelle et juridique, la formulation des 
exigences et la langue. Les corrections retenues ont été intégrées au texte; 49 sources ont été ajoutées au 
registre, et le texte des exigences, les échelles et les renvois ont été harmonisés. Après l’intégration de 
ces corrections, l’annexe G compte 473 références, toutes citées dans le corps du cadre. Les arbitrages 
d’architecture et de gouvernance relevés lors de cet audit ont également été tranchés et intégrés à la 
présente version.
Tableau 66 — Catégories de crédibilité des sources
Catégorie
Définition
Usage dans le cadre
A
Source primaire ou officielle : organismes de normalisation et leurs dépôts 
(IETF, W3C, ISO, NIST, OWASP, CNCF, OpenTelemetry, Linux Foundation et 
sites des projets), textes législatifs et organismes de réglementation, docu­
mentation officielle d’un éditeur sur son propre produit, articles scientifiques 
d’auteurs identifiables, communiqués des firmes d’analystes.
Appui de toute exigence et de 
tout fait.
B
Source secondaire reconnue : grande presse spécialisée, cabinets juridiques, 
experts reconnus.
Appui d’un fait de contexte, 
jamais seul pour une exigence.
C
Blogue de positionnement, agrégateur, site inconnu ou contenu généré en 
série.
Jamais cité; remplacé par une 
source A ou B, ou fait retiré.
F.2 Bilan chiffré
Les décomptes ci-dessous portent sur les 121 références et sur les 427 liens affirmation-source de la recherche 
documentaire.
121
références validées une à une, dont 108 accessibles et 13 bloquées, payantes ou redirigées
61
références de catégorie C (50 %), dont 33 présentant les marques d’un contenu généré en série
88
références remplacées (71) ou retirées (17); 33 conservées comme sources A ou B
705
sources admissibles (A ou B) recensées pour la version finale, dont 632 de catégorie A (primaires ou 
officielles); 49 ont été ajoutées lors de l’audit final
Tableau 67 — Verdicts sur les 427 liens affirmation-source de la recherche documentaire
Verdict
Nombre
Part
Signification
Appuyée
125
29 %
La source citée confirme l’affirmation telle qu’écrite.
Partiellement ap­
puyée
214
50 %
Le fond est juste, mais un détail (date, chiffre, version, portée) diffère : l’énoncé a 
été corrigé.
Non appuyée
55
13 %
La source ne contient pas l’affirmation : source primaire trouvée ou fait retiré.
Contredite
14
3 %
La source ou une source primaire dit le contraire : fait corrigé.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 242 sur 283
