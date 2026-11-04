# chunk_10 — pages PDF 91 à 102 (sur 283)



---
## [Page PDF 91]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Le clavardage de groupe ou le débat entre agents DOIT réunir trois agents participants au plus, sous 
un gestionnaire (hors décompte des trois participants) qui attribue la parole, avec un plafond de tours 
et une règle de clôture déclarés. Le maillage libre, où chaque agent sollicite les autres sans plafond, NE 
DOIT PAS être utilisé.
Pourquoi : Microsoft recommande de limiter le clavardage de groupe à trois agents[9], et des idées peuvent se propager 
d’agent en agent[280].
EXIG-ORC-07 · DOIT
Fusion déclarée et écrivain unique en parallèle
Un patron de parallélisation DOIT déclarer avant l’exécution sa règle de fusion (déterministe, vote 
ou arbitrage) et sa limite de concurrence. Les branches DOIVENT se limiter à lire et à produire des 
artefacts; un seul composant DOIT écrire le résultat final dans un système d’enregistrement.
Pourquoi : des écritures concurrentes se contredisent[277].
EXIG-ORC-08 · DOIT
Chorégraphie sous propriétaire et saga
Une chorégraphie événementielle qui produit des effets dans plusieurs systèmes d’enregistrement 
DOIT avoir un propriétaire de bout en bout inscrit au registre, une saga explicite (section 7.5) et les 
contrôles d’enveloppe de la section 6.7.
Pourquoi : sans chef d’orchestre, personne ne voit le processus entier ni ne répond de son issue.
7.3 Choisir le patron
Le choix du patron suit l’arbre de décision de la figure 12, qui part toujours de l’option la plus simple. Il se 
documente à la fiche de l’agent et se révise lorsque les mesures de production contredisent l’hypothèse de 
départ.
Une règle métier ou un
seul appel d’outil suffit?
NON
OUI
Pas d’agent
code, règle ou appel direct
Les étapes sont-elles
connues d’avance?
OUI
Flux déterministe
étapes agentiques bornées
NON
Déclenchement par une
personne ou un événement?
événement
Chorégraphie
événementielle
personne
Un spécialiste unique suffit
après qualification?
OUI
Routage et transfert
l’agent de tête se retire
NON
Un agent unique, outils bien
décrits, contexte non saturé,
suffit-il?
OUI
Agent unique
recherche d’outils si nécessaire
NON
Orchestrateur et exécutants
2 niveaux au plus · parallèle si possible
À combiner avec tout patron
La qualité se vérifie? → boucle évaluateur-optimiseur (≤ 3 itérations).
Sous-tâches indépendantes? → parallélisation (sectionnement ou vote).
Par défaut, retenir l’option la plus simple qui répond au besoin; passer au multiagent seulement sur preuve mesurée de gain.
Figure 12 — Arbre de décision du patron d’orchestration. Les questions se lisent de haut en bas; la première réponse qui conclut 
fixe le patron. Les encadrés du bas s’ajoutent à n’importe quel patron lorsque la qualité se vérifie ou que des sous-tâches sont 
indépendantes. Source : cadre CRE-IA-2026-01, d’après le Centre d’architecture Azure (niveaux de complexité) et Anthropic.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 91 sur 283


---
## [Page PDF 92]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Quand le multiagent se justifie
Anthropic retient trois cas où plusieurs agents surpassent un agent unique : la protection du contexte (une 
sous-tâche produit une exploration volumineuse qui polluerait le contexte principal), la parallélisation 
(des pistes réellement indépendantes) et la spécialisation (des outils ou des consignes incompatibles dans 
un même agent)[275]. Microsoft ajoute les frontières de sécurité distinctes : deux domaines qui ne doivent 
pas partager les mêmes droits justifient deux agents[9]. L’effort doit aussi suivre la complexité : Anthropic 
emploie un agent et de 3 à 10 appels d’outils pour une recherche factuelle simple, de 2 à 4 sous-agents pour 
une comparaison, et davantage pour une recherche complexe[17].
Surcharge d’outils : mesurer avant de scinder
Aucune source ne fixe de seuil unique. OpenAI suggère, à titre indicatif, de viser moins de 20 fonctions 
disponibles au début d’un tour[115] et souligne que le chevauchement compte plus que le nombre : certaines 
mises en œuvre gèrent avec succès plus de 15 outils distincts, d’autres peinent avec moins de 10 outils qui se 
chevauchent[66]. La documentation d’Anthropic situe la dégradation au-delà de 30 à 50 outils disponibles[281]. 
Avant de multiplier les agents, deux leviers moins coûteux existent : consolider les outils en opérations 
orientées tâche, regroupées sous des espaces de noms[114], et charger les définitions d’outils à la demande. 
Selon Anthropic, sa recherche d’outils réduit de 85 % la consommation de jetons de contexte dans son 
exemple chiffré et fait passer la précision, sur ses évaluations internes de MCP, de 49 à 74 % (Opus 4) et de 
79,5 à 88,1 % (Opus 4.5); ce sont des résultats déclarés par le fournisseur[205].
Découper par frontières de contexte
Quand plusieurs agents sont retenus, on découpe selon les frontières de contexte, et non selon le type de 
travail : une fonctionnalité et ses tests restent avec le même agent[275]. Par exemple, dans l’analyse d’un 
dossier de crédit, l’agent qui lit les états financiers calcule aussi les ratios qui en découlent; un agent distinct 
ne se justifie que pour un contexte isolable, comme la vérification des sanctions internationales, qui obéit à 
d’autres droits d’accès.
Tableau 25 — Critères comparés des principaux patrons
Critère
Flux déter­
ministe
Agent 
unique
Routage et 
transfert
Orchestrateur 
et exécutants
Évaluateur-optimiseur
Chorégra­
phie
Prévisibilité et 
auditabilité
Très élevée
Moyenne
Élevée
Moyenne
Élevée sur le résultat
Moyenne, 
émergente
Latence de 
bout en bout
Faible à 
moyenne
Variable selon 
les tours
Faible
Élevée; réduite 
si parallèle
Moyenne à élevée
Asynchrone
Profil de coût 
en jetons (re­
père)
Le plus bas
Environ 4 fois 
une conver­
sation
Cumul étape 
par étape
3 à 10 fois 
l’agent unique; 
pointes si pa­
rallèle
Croît avec les itérations
Croît avec les 
abonnés et 
les sauts
Tolérance à 
l’ambiguïté
Faible
Élevée dans 
un domaine
Moyenne
Très élevée
Moyenne
Moyenne
Ce qui borne la 
dérive
Le code
Plafonds et 
budget
Liste fermée 
de destina­
taires
Deux niveaux, 
budget, délais
Trois itérations
Compteur de 
sauts, lettres 
mortes
Les appréciations qualitatives du tableau 25 sont des repères du cadre. Les seuls ordres de grandeur retenus 
par le cadre sont ceux d’Anthropic (environ 4 fois et 15 fois une conversation; de 3 à 10 fois l’agent unique)
[17, 275] et les profils de Microsoft : coûts cumulés étape par étape pour les patrons séquentiel et de transfert, 
pointes pour le patron concurrent, coût le moins prévisible pour le patron magnétique[9]. Ces repères cèdent 
la place aux mesures de jetons par agent et par exécution dès qu’elles existent (section 10.6).
EXIG-ORC-09 · DOIT
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 92 sur 283


---
## [Page PDF 93]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Surcharge d’outils traitée avant de scinder
Dès qu’un agent dépasse 15 outils (seuil opérationnel retenu par le cadre dans la plage de 15 à 20 outils), 
ou dès que des outils se chevauchent, l’équipe DOIT mesurer la précision de sélection d’outils sur le jeu 
d’évaluation, puis essayer la consolidation des outils et leur chargement à la demande avant de scinder 
l’agent en plusieurs agents.
Pourquoi : le chevauchement compte plus que le nombre[66], et la recherche d’outils restaure une partie de la précision 
à moindre coût[205].
EXIG-ORC-10 · DEVRAIT
Découpage par frontières de contexte
Lorsqu’un système multiagent est retenu, le découpage DEVRAIT suivre les frontières de contexte et 
de sécurité plutôt que les types de travail : le même agent garde une unité de travail et sa vérification 
immédiate. Un agent distinct se justifie par un contexte isolable, un parallélisme réel, une spécialisation 
d’outils ou une frontière de sécurité, consignés à la fiche.
Pourquoi : un transfert qui ne passe que des messages, sans la trace complète, fait perdre des décisions implicites[275, 
276].
7.4 État et exécution durable
Un agent attend une approbation pendant trois jours; un serveur redémarre au milieu d’une réservation. 
Dans les deux cas, l’orchestration doit reprendre exactement où elle s’était arrêtée, sans perdre le contexte 
et sans refaire une action déjà faite. C’est le rôle de l’exécution durable.
Persister l’état hors du processus
Microsoft recommande de persister l’état partagé hors de la mémoire et d’utiliser les points de contrôle du 
cadriciel[9]. Les moteurs y parviennent de façons différentes. Temporal garantit qu’une exécution de flux 
se poursuit jusqu’à son terme, sans limite de durée imposée, et la reprend après une panne en rejouant 
son historique d’événements[81]. LangGraph conserve l’état par fil (thread_id) au moyen de checkpointers : 
InMemorySaver perd ses points de contrôle au redémarrage et sert à l’expérimentation, tandis qu’un magasin 
persistant comme PostgresSaver s’impose en production[124, 282]. Microsoft Agent Framework crée un point 
de contrôle à la fin de chaque étape de calcul du flux, avec l’état des exécuteurs, les messages et les requêtes 
en attente[105].
Ne jamais refaire une action terminée : une garantie à construire
La persistance ne suffit pas à éviter les doubles effets. Dans LangGraph, à la reprise après une interruption, le 
nœud interrompu redémarre depuis son début et le code qui précède l’interruption s’exécute de nouveau[82]; 
Temporal réessaie les activités en échec[79]. La garantie repose donc sur deux règles de conception : isoler 
chaque appel non déterministe (modèle, outil, agent distant) dans une étape journalisée dont le résultat se 
relit à la reprise, et rendre idempotent tout effet qui peut être rejoué (section 7.6). L’intégration de Temporal 
avec l’OpenAI Agents SDK applique la première règle : chaque invocation d’agent s’y exécute comme une 
activité, suivie et réessayée par le moteur[122].
Aux points d’approbation obligatoires, l’état est persisté afin de reprendre sans rejouer le travail des agents 
précédents[9]. La primitive interrupt() de LangGraph, par exemple, suspend le graphe et attend sans limite 
une reprise sur le même fil[82]. La forme de l’approbation elle-même relève de la section 8.5.
Points de contrôle, versions et rejeu
Un point de contrôle contient l’état complet d’une tâche, souvent avec des renseignements personnels (RP) 
et des extraits d’invites. Microsoft le désigne comme une frontière de confiance : on ne charge jamais un 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 93 sur 283


---
## [Page PDF 94]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
point de contrôle venant d’une source non fiable, et ses magasins Python n’acceptent qu’une liste blanche 
de types à la désérialisation[105]. Les exécutions longues posent aussi un problème de version : Anthropic 
déploie ses agents en mode « arc-en-ciel » pour ne pas interrompre ceux qui s’exécutent déjà[17]. Enfin, 
le « voyage dans le temps » de LangGraph permet de rejouer depuis un point de contrôle antérieur ou 
de bifurquer après correction de l’état; les nœuds suivants s’exécutent alors de nouveau et les appels aux 
modèles ou aux API peuvent produire d’autres résultats[283]. Le rejeu sert à l’analyse et à la correction; il ne 
reproduit pas une décision à l’identique.
EXIG-ORC-11 · DOIT
Persistance après chaque transition
Tout flux de plus d’une étape, ou susceptible d’attendre une approbation, DOIT s’exécuter sur un 
moteur d’exécution durable qui persiste l’état après chaque transition (appel de modèle, appel d’outil, 
décision, réponse humaine) dans un magasin externe au processus. Un magasin en mémoire NE DOIT 
PAS être utilisé hors du poste de développement.
Pourquoi : un redémarrage ou un déploiement ne doit faire perdre ni le contexte ni l’avancement[9, 124].
EXIG-ORC-12 · DOIT
Reprise sans double effet
La logique de coordination DOIT rester déterministe; chaque appel non déterministe DOIT s’exécuter 
comme une étape journalisée dont le résultat est relu, et non recalculé, à la reprise. Tout effet de bord 
placé avant un point de pause ou dans une étape réessayable DOIT être idempotent; sinon, il DOIT 
être déplacé après le point de pause.
Pourquoi : les moteurs réexécutent le nœud interrompu ou réessaient l’activité en échec[79, 82].
EXIG-ORC-13 · DOIT
Magasin de points de contrôle protégé
Le magasin des points de contrôle DOIT être traité comme une frontière de confiance et comme 
une donnée de production : accès limité à l’identité de l’orchestrateur, chiffrement au repos, contrôle 
d’intégrité au chargement, conservation et élagage définis. Un orchestrateur NE DOIT PAS charger de 
point de contrôle d’origine non vérifiée.
Pourquoi : un point de contrôle contient l’état complet de la tâche, y compris les messages en attente; un point de 
contrôle altéré permet donc d’en modifier l’état, et ces messages peuvent contenir des RP (constat du cadre, non tiré 
de la source)[105].
EXIG-ORC-14 · DEVRAIT
Déploiement sans interruption des exécutions longues
Le déploiement d’une nouvelle version d’agent ou de flux DEVRAIT laisser chaque exécution en cours 
se terminer sur la version avec laquelle elle a commencé; une migration d’état en cours d’exécution 
DEVRAIT se tester comme un changement de schéma.
Pourquoi : un déploiement peut casser les agents déjà en cours d’exécution, et recommencer du début coûte cher[17].
7.5 Transactions : patron saga
Lorsqu’une tâche écrit dans plusieurs systèmes qui ne partagent aucune transaction (un système de 
transport, un progiciel de gestion intégré, une passerelle de paiement), aucun retour arrière global n’existe. 
La saga remplace la transaction globale par une suite de transactions locales, chacune appariée à une 
compensation (voir la figure 13).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 94 sur 283


---
## [Page PDF 95]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Principe
Garcia-Molina et Salem ont défini la saga en 1987 : une transaction de longue durée découpée en transac­
tions plus courtes, avec la garantie que soit toutes s’exécutent, soit des transactions compensatoires défont 
l’exécution partielle[284, 285]. Microsoft distingue trois sortes d’étapes : les transactions compensables, qui 
précèdent le point de non-retour; la transaction pivot, qui est ce point de non-retour; et les transactions 
réessayables, idempotentes, qui la suivent jusqu’au terme[67]. Une saga se conçoit donc pour que tout ce 
qui est irréversible arrive le plus tard possible (PRIN-05).
TRANSACTIONS LOCALES (VERS L’AVANT)
T1 ✓
Réserver le transport
compensable
T2 ✓
Réserver le stock (ERP)
compensable
T3 ✗ échec
Débiter le client
non reprenable
T4 · pivot
Confirmation officielle
irréversible · approbation
COMPENSATIONS (ORDRE INVERSE, IDEMPOTENTES)
C1
Annuler la réservation
C2
Libérer le stock
échec définitif → compenser
de k−1 à 1
2 échecs d’une compensation
→ file humaine prioritaire
JOURNAL EN AJOUT SEUL (LA COMPENSATION EST JOURNALISÉE AVANT L’ACTION)
① journaliser
C1
② exécuter
T1 ✓
③ journaliser
C2
④ exécuter
T2 ✓
⑤ journaliser
C3
⑥ T3
échoue
⑦ exécuter
C2
⑧ exécuter
C1
T3 n’a jamais été marquée « terminée » : C3 n’est exécutée que si son effet est incertain. Le pivot T4 n’est atteint qu’après succès de T1 à T3.
Figure 13 — Saga : transactions locales, pivot et compensations. T1 et T2 réussissent; T3 échoue de façon définitive : l’orchestrateur 
exécute C2 puis C1, et le pivot T4, irréversible et soumis à approbation, n’est jamais atteint. Le journal montre que chaque compensation 
est consignée avant l’action qu’elle couvre. Source  : cadre CRE-IA-2026-01, d’après Garcia-Molina et Salem (1987), Microsoft et 
Temporal.
Cinq règles de conception
1. Journaliser la compensation avant l’action. Temporal recommande d’inscrire la compensation 
avant d’exécuter l’activité, parce qu’un effet de bord peut survenir avant que l’échec ne soit signalé : 
une carte débitée, par exemple[286]. Microsoft exige de consigner chaque étape et la façon de la défaire 
dans un magasin durable, afin de reprendre la compensation au point d’échec[77].
2. Traiter l’incertain comme exécuté. Si l’orchestrateur ignore l’issue d’une étape (délai expiré, plan­
tage entre le journal et la réponse), il la considère comme possiblement exécutée. Sa compensation doit 
alors pouvoir s’exécuter sans risque même si l’action n’a jamais eu lieu : « rembourser la transaction X 
si elle a été débitée », et non « rembourser le montant X ».
3. Compenser en termes métier. Une compensation applique des règles d’affaires : l’annulation d’un vol 
n’entraîne pas forcément un remboursement complet. Elle ne ramène pas nécessairement les données 
à leur état initial, ne suit pas toujours l’ordre inverse exact et peut parfois s’exécuter en parallèle[77]. On 
ne « désenvoie » pas un courriel : on envoie un rectificatif.
4. Réessayer avant de compenser. On ne compense que si la progression devient impossible, c’est-à-
dire après épuisement des réessais ou devant une erreur non transitoire[77].
5. Escalader l’échec persistant. Si une compensation échoue, Temporal recommande de consigner 
l’erreur, de poursuivre les autres compensations, puis d’alerter; une erreur non réessayable dans une 
compensation signifie que la saga ne peut plus revenir entièrement en arrière[286]. Microsoft prévoit la 
file de lettres mortes et la suspension des cas ambigus ou à fort impact pour revue humaine[77]. Le seuil 
de deux échecs retenu ci-dessous est un choix du cadre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 95 sur 283


---
## [Page PDF 96]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Isolation entre sagas concurrentes
Une saga n’isole pas ses étapes comme une transaction ACID (atomicité, cohérence, isolation, durabilité). 
Microsoft recense trois anomalies : mises à jour perdues, lectures sales et lectures non répétables. Les contre-
mesures sont le verrou sémantique, les mises à jour commutatives, la vue pessimiste (réordonner les étapes 
pour que les mises à jour aient lieu dans des transactions réessayables), la relecture des valeurs avant mise 
à jour, les fichiers de versions et le choix du mécanisme de concurrence selon le risque métier. La saga 
convient mal aux transactions fortement couplées et aux dépendances cycliques[67]. Exemple : deux agents 
qui réservent le même stock posent d’abord un verrou sémantique « réservation en attente », visible des 
autres sagas, plutôt que de décrémenter directement la quantité.
Pour les agents, SagaLLM (Chang et Geng, PVLDB, 2025) combine le patron saga, une mémoire persistante, 
des compensations automatisées et des agents de validation indépendants, en assouplissant les garanties 
ACID au profit d’une cohérence à l’échelle du flux[287, 288]. C’est une référence de recherche utile, et non une 
norme d’industrie.
EXIG-ORC-15 · DOIT
Saga pour toute écriture multisystème
Une tâche qui écrit dans au moins deux systèmes d’enregistrement sans transaction commune DOIT 
être modélisée comme une saga : chaque étape d’écriture P2 référence la compensation déclarée dans 
son entrée de catalogue (section 6.8), le pivot est identifié, et toute étape de palier P3 (action critique, 
externe ou irréversible) se place au pivot ou après, une fois les validations critiques réussies et 
l’approbation humaine obtenue (section 8.5).
Pourquoi : reporter l’irréversible après toutes les validations limite ce qu’il faut défaire[77].
EXIG-ORC-16 · DOIT
Journal de compensation tenu avant l’action
Avant chaque étape, l’orchestrateur DOIT consigner dans un journal durable, en ajout seul et corrélé 
à la trace, l’étape, ses arguments, sa clé d’idempotence et la compensation à exécuter. Une étape dont 
l’issue est inconnue est traitée comme possiblement exécutée : sa compensation est déclenchée et reste 
sans effet si l’action n’a pas eu lieu.
Pourquoi : un effet peut survenir avant que l’échec ne soit signalé[286].
EXIG-ORC-17 · DOIT
Compensations idempotentes et métier, après réessais
Chaque compensation DOIT être idempotente et définie en termes métier (remboursement, avis recti­
ficatif, libération de stock) avec le propriétaire du système visé. L’orchestrateur réessaie d’abord l’étape 
en échec selon sa politique de réessai et ne compense que si la progression devient impossible.
Pourquoi : une compensation peut s’exécuter plusieurs fois et ne restaure pas forcément l’état initial[77, 286].
EXIG-ORC-18 · DOIT
Escalade après deux échecs d’une compensation
Lorsqu’une même compensation échoue deux fois de suite (erreur non transitoire ou politique de réessai 
épuisée), l’orchestrateur DOIT cesser de la relancer, poursuivre les compensations qui n’en dépendent 
pas, puis placer l’état complet de la saga dans une file humaine prioritaire nommée, avec alerte et 
identifiants de corrélation.
Pourquoi : l’échec persistant exige une intervention manuelle[286]; le seuil de deux échecs est un choix du cadre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 96 sur 283


---
## [Page PDF 97]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
EXIG-ORC-19 · DOIT
Isolation sémantique des sagas concurrentes
Lorsque plusieurs sagas ou agents peuvent modifier les mêmes enregistrements, la conception DOIT 
documenter les anomalies possibles (mises à jour perdues, lectures sales, lectures non répétables) et 
appliquer au moins une contre-mesure à chacune.
Pourquoi : la saga n’offre pas l’isolation d’une transaction ACID[67].
EXIG-ORC-20 · DOIT
Quatre tests d’injection de fautes
Avant la mise en production, toute saga DOIT réussir quatre tests automatisés, exécutés contre des 
doublures des systèmes d’enregistrement : échec forcé de chaque étape Tk avec vérification des com­
pensations; plantage entre l’écriture au journal et l’action; double exécution de chaque compensation; 
double échec d’une compensation avec vérification de l’escalade.
Pourquoi : exigence propre au cadre; les chemins de compensation ne servent presque jamais en exploitation normale 
et doivent être éprouvés avant d’être nécessaires.
7.6 Idempotence
Une opération est idempotente si l’exécuter deux fois produit le même effet que l’exécuter une fois. Sans 
cette propriété, un simple réessai après un délai expiré peut débiter un client deux fois.
Les doublons ne sont pas une hypothèse d’école  : ils découlent des garanties mêmes des composants. 
Kafka livre « au moins une fois » par défaut, et sa sémantique « exactement une fois » ne couvre que le 
cycle lecture-traitement-écriture entre sujets Kafka[140, 256]. Pour les notifications push A2A, le protocole 
exige au moins une tentative de livraison (reprises facultatives, doublons possibles)[68], et les flux Express 
asynchrones d’AWS Step Functions s’exécutent selon la même garantie (les flux Express synchrones, « au 
plus une fois »), ce qui exige des actions idempotentes pour les premiers[104]. Les règles propres au bus 
d’événements figurent à la section 6.7.
Le cadre dérive la clé de l’identifiant de la tâche et de celui de l’étape. Le brouillon IETF draft-ietf-httpapi-
idempotency-key-header-08 (22 octobre 2026), qui n’est pas encore une RFC, décrit l’en-tête Idempotency-Key : le 
client renvoie la même clé à chaque réessai; le serveur répond 409 si la requête d’origine est encore en cours 
et 422 si la clé est réutilisée avec une charge utile différente. Le brouillon recommande un UUID (identifiant 
unique universel) ou un identifiant aléatoire semblable et met en garde contre les clés à faible entropie; la 
dérivation déterministe retenue par le cadre est un choix qui lui est propre, acceptable pourvu que la clé 
reste unique par opération et que le service la valide avant tout traitement[78]. Quant aux annotations d’outil 
de MCP (idempotentHint, destructiveHint), ce sont de simples indices, sur lesquels un client ne fonde 
aucune décision lorsque le serveur n’est pas digne de confiance[197, 201].
Dérivation de la clé d’idempotence (illustration)
réessai de la même étape                → même clé, aucun effet supplémentaire
même clé, arguments différents          → rejet (422 selon le brouillon IETF)
étape replanifiée avec d’autres valeurs → nouveau step_id, donc nouvelle clé
task_id         = "tache-7f3c2a"                      (attribué par l’orchestrateur)
step_id         = "etape-02/reserver-stock"
cle             = hex( SHA-256( task_id + "|" + step_id ) )
EXIG-ORC-21 · DOIT
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 97 sur 283


---
## [Page PDF 98]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Clé d’idempotence sur toute écriture
Chaque appel d’outil en écriture (P2 ou P3) DOIT porter une clé d’idempotence dérivée de l’identifiant 
de la tâche et de celui de l’étape, réutilisée telle quelle à chaque réessai. Une étape replanifiée avec 
d’autres arguments reçoit un nouvel identifiant d’étape, donc une nouvelle clé. La clé voyage dans l’en-
tête Idempotency-Key lorsque le service le prend en charge, sinon dans un champ déclaré du contrat 
d’outil.
Pourquoi : réessais, reprises et livraisons « au moins une fois » rejouent des appels[68, 140].
EXIG-ORC-22 · DOIT
Vérification de la clé par le service visé
Tout outil P2 ou P3 inscrit au catalogue DOIT vérifier la clé côté serveur, directement ou par son 
adaptateur : un doublon ne produit aucun effet supplémentaire; une clé réutilisée avec des arguments 
différents est rejetée; une requête dont l’original est encore en cours est refusée sans exécution. Ce 
comportement est déclaré dans l’entrée de catalogue; les annotations MCP n’en tiennent pas lieu[197].
Pourquoi : seul le système visé sait si l’effet a déjà eu lieu[78].
7.7 Contexte transmis entre agents
Ce qu’un agent transmet à un autre détermine à la fois la qualité du résultat, le coût et l’exposition des 
données. Le cadre impose un contexte minimal et structuré, avec une nuance importante pour les tâches 
fortement couplées.
Microsoft demande de décider quel contexte l’agent suivant requiert (contexte complet, version compactée 
ou nouvelle consigne seulement), de compacter entre agents et de limiter l’état persisté au strict nécessaire, 
pour des raisons de coût et de confidentialité[9]. Anthropic fait rendre par ses sous-agents une synthèse 
condensée, souvent de 1 000 à 2 000 jetons, et stocke leurs livrables hors du contexte pour les transmettre 
par références légères[17, 149]. La mise en garde de Cognition reste valable : un exécutant privé des décisions 
qui le concernent en prendra de contradictoires[276]. Le contexte minimal convient donc surtout aux tâches 
de lecture; une tâche à fortes dépendances reste à un seul agent (section 7.3). Cognition a depuis nuancé 
sa position (Yan, 22 avril 2026) : des agents supplémentaires peuvent apporter du jugement tant que les 
écritures restent à fil unique; ses observations d’origine tiennent toujours pour les essaims d’écrivains 
parallèles[289]. La gestion du contexte et de la mémoire de chaque agent relève de la section 5.5.
Contenu logique d’une délégation (indépendant du protocole)
{
  "sous_objectif": "Évaluer la solvabilité du client 4471 selon la politique CR-12",
  "criteres_acceptation": ["ratios calculés", "pièces citées", "aucune donnée hors dossier"],
  "parametres": { "client_id": "4471", "montant_demande": 250000 },
  "artefacts": ["artefact://dossiers/4471/etats-financiers-2025.pdf"],
  "jeton_delegue": "<jeton délégué du mandant, audience = agent-credit>",
  "traceparent": "00-<trace-id>-<span-id>-01",
  "budget_restant": { "jetons": 40000, "cout_max_cad": 2.00, "appels_outils": 10, "echeance": "PT10M" },
  "schema_retour": "schema://credit/avis-solvabilite/1.2"
}
Ce message ne contient ni l’historique de la conversation ni les données que l’exécutant peut lire lui-même 
avec les droits du mandant. Sa traduction en messages A2A relève de la section 6.6.
La sécurité suit le même chemin. Microsoft exige que chaque agent applique un filtrage de sécurité, pour 
ne jamais renvoyer une donnée inaccessible à l’utilisateur, et que des garde-fous de contenu s’appliquent 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 98 sur 283


---
## [Page PDF 99]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
à plusieurs points : entrée de l’utilisateur, appels d’outils, réponses d’outils et sortie finale, car un agent 
intermédiaire peut introduire ou propager du contenu nuisible[9].
EXIG-ORC-23 · DOIT
Contexte de délégation minimal et structuré
Une délégation DOIT transmettre un message structuré limité au sous-objectif, aux critères 
d’acceptation, aux paramètres requis, aux références d’artefacts, au jeton délégué du mandant (section 
9.3), au contexte de trace (section 10.1), au budget restant et au schéma de retour attendu. L’historique 
brut complet NE DOIT PAS être transmis, sauf exception justifiée à la fiche.
Pourquoi : un contexte minimal réduit le coût et l’exposition des données[9].
EXIG-ORC-24 · DOIT
Retour validé avant toute réutilisation
Un exécutant DOIT rendre une synthèse conforme au schéma de retour déclaré et déposer ses livrables 
volumineux dans un magasin d’artefacts, transmis par référence. L’orchestrateur DOIT valider la 
sortie (schéma, plafonds, garde-fous) avant de l’utiliser ou de la transmettre; une sortie invalide DOIT 
déclencher un réessai, une demande de précision ou l’arrêt.
Pourquoi : une sortie non validée propage l’erreur d’agent en agent[9].
EXIG-ORC-25 · DOIT
Filtrage de sécurité dans chaque agent
Chaque agent DOIT filtrer ses résultats selon les droits du mandant, de sorte qu’aucune donnée 
inaccessible à ce mandant ne remonte à l’orchestrateur ni à l’utilisateur. Les garde-fous de contenu 
s’appliquent à l’entrée, aux appels d’outils, aux réponses d’outils et à la sortie finale; le contenu reçu 
d’un autre agent est traité comme une donnée non fiable (section 9.6).
Pourquoi : un agent intermédiaire peut introduire ou propager du contenu nuisible[9].
7.8 Résilience et dégradation maîtrisée
Un modèle indisponible, un outil lent ou un agent qui tourne en rond ne doivent ni bloquer le processus 
ni produire un résultat faux en silence. Cette section met en œuvre le principe de dégradation maîtrisée 
(PRIN-12).
Microsoft prescrit pour les orchestrations d’agents des délais d’expiration et des réessais, une dégradation 
maîtrisée, la remontée des erreurs plutôt que leur masquage, la validation de la sortie d’un agent avant 
sa transmission, l’examen de disjoncteurs, l’isolement des agents sans point unique de défaillance partagé 
et des points de contrôle pour reprendre après une panne ou un déploiement[9]. Anthropic note qu’il est 
courant d’inclure des conditions d’arrêt, comme un nombre maximal d’itérations, pour garder le contrôle 
d’un agent[65]. Les plafonds de l’exécution s’inscrivent dans l’enveloppe budgétaire de la tâche (section 10.6); 
le modèle de repli s’obtient par la passerelle de modèles (chapitre 5).
Le dernier recours est l’arrêt. Pour les systèmes à haut risque, le règlement européen sur l’IA prévoit la 
possibilité d’interrompre le système de façon sûre (art. 14(4)e))[290]; le NIST AI RMF, cadre d’usage volontaire, 
demande (MANAGE 2.4) des mécanismes et des responsabilités pour remplacer, désengager ou désactiver un 
système dont les résultats s’écartent de l’usage prévu[99]. OpenAI recommande une interruption ordonnée, 
soit ciblée (révoquer une catégorie d’actions), soit générale[291]. La propagation de l’arrêt à travers les 
passerelles et les jetons relève de la section 9.4.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 99 sur 283


---
## [Page PDF 100]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
EXIG-ORC-26 · DOIT
Plafonds sur toute exécution
Chaque exécution DOIT porter des plafonds déclarés à la fiche : étapes ou itérations, appels d’outils, 
jetons, coût et durée totale. L’atteinte d’un plafond DOIT arrêter la boucle en état sûr et déclencher 
l’escalade prévue; elle NE DOIT PAS être rapportée comme un succès.
Pourquoi  : l’autonomie d’un agent entraîne des coûts plus élevés et un risque d’erreurs cumulatives, d’où des 
conditions d’arrêt pour garder le contrôle[65].
EXIG-ORC-27 · DOIT
Mécanismes de résilience et repli testé
Chaque dépendance d’une orchestration (modèle, outil, agent distant) DOIT être protégée par un délai 
d’expiration, des réessais à temporisation exponentielle (exponential backoff) limités aux erreurs transi­
toires et un disjoncteur. Les erreurs sont remontées et journalisées, jamais masquées. Le repli prévu 
(modèle de repli homologué, service dégradé ou file humaine nommée recevant le contexte complet) 
est testé avant la production.
Pourquoi : Microsoft prescrit délais d’expiration et réessais et recommande d’envisager des disjoncteurs; la tempo­
risation exponentielle et la limitation aux erreurs transitoires sont des choix du cadre[9].
EXIG-ORC-28 · DOIT
Coupe-circuit exercé chaque trimestre
Chaque agent DOIT pouvoir être arrêté de façon ciblée (retrait d’un outil ou d’une capacité) ou totale. 
La plateforme DOIT en outre disposer d’un coupe-circuit global. L’arrêt bloque toute nouvelle étape, 
conserve l’état pour analyse et laisse les sagas en cours dans un état connu, suspendues ou compensées 
selon la procédure. Un exercice d’arrêt DOIT avoir lieu au moins une fois par trimestre et son délai 
mesuré DOIT être consigné.
Pourquoi : le RIA prévoit l’interruption sûre des systèmes à haut risque (art. 14(4)e)) et le NIST AI RMF, d’usage 
volontaire, demande des mécanismes pour désactiver un système (MANAGE 2.4), le cadre l’appliquant à tous les 
agents[99, 290]; la fréquence trimestrielle est un choix du cadre.
7.9 Anti-patrons proscrits
La taxonomie MAST (Multi-Agent System Failure Taxonomy) (Cemri et coll., UC Berkeley), tirée de plus de 
1 600 traces annotées issues de sept cadriciels, recense 14 modes de défaillance des systèmes multiagents en 
trois catégories : conception du système, désalignement entre agents et vérification des tâches. Elle conclut 
que les défaillances relèvent surtout de la conception, et non des seules limites des modèles[292]. La revue 
d’architecture cible donc les défauts de conception ci-dessous; le classement des incidents selon MAST 
relève de la section 10.4.
Tableau 26 — Anti-patrons d’orchestration proscrits
Anti-patron
Pourquoi il est proscrit
Correctif exigé
Coordination multiagent là où un agent ou 
un flux suffit
Coût, latence et erreurs accrus sans 
gain mesuré[9]
EXIG-ORC-01 et EXIG-ORC-02
Agents sans spécialisation réelle, découpés 
par type de travail
Les transferts perdent des décisions 
implicites[275]
Découpage par frontières de contexte 
(EXIG-ORC-10)
Confier au modèle un contrôle de flux que 
le code sait garantir, ou figer en code un 
flux réellement ouvert
Patron inadapté à la nature du flux[9]
Arbre de décision de la section 7.3 
(PRIN-08)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 100 sur 283


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
