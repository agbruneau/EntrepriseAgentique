# chunk_08 — pages PDF 71 à 82 (sur 283)



---
## [Page PDF 71]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
ÉTATS ACTIFS
ÉTATS INTERROMPUS
ÉTATS TERMINAUX
TASK_STATE_
SUBMITTED
TASK_STATE_
WORKING
TASK_STATE_
INPUT_REQUIRED
précision ou approbation
TASK_STATE_
AUTH_REQUIRED
justificatif supplémentaire
TASK_STATE_COMPLETED
TASK_STATE_FAILED
TASK_STATE_CANCELED
TASK_STATE_REJECTED
fin de traitement
l’agent distant refuse la tâche
Un message vers une tâche terminale renvoie UnsupportedOperationError; annuler une tâche terminale renvoie TaskNotCancelableError. Valeur zéro : TASK_STATE_UNSPECIFIED.
Figure 8 — Cycle de vie d’une tâche A2A 1.0. Une tâche passe de soumise à en cours, peut s’interrompre pour obtenir une précision, 
une approbation ou un justificatif, puis aboutit à l’un des quatre états terminaux, après lesquels elle n’accepte plus de message. Source : 
A2A Project, a2a.proto, version de protocole 1.0.
Le protocole définit les opérations SendMessage, SendStreamingMessage, GetTask, ListTasks, CancelTask, 
SubscribeToTask, GetExtendedAgentCard et quatre opérations de gestion des configurations de notifica­
tion push. Par défaut, SendMessage attend que la tâche atteigne un état terminal ou interrompu; avec 
returnImmediately: true, il rend la main dès la création de la tâche. ListTasks pagine par curseur et 
omet les artefacts par défaut, ce qui convient aux tableaux de bord d’exploitation[68]. Le client suit une 
tâche longue de trois façons : interrogation périodique (GetTask), flux en continu (SSE, pour Server-Sent 
Events, ou gRPC) ou notifications push[29, 68]. Dans la liaison HTTP+JSON, une erreur prend la forme d’un 
google.rpc.Status accompagné d’un google.rpc.ErrorInfo du domaine a2a-protocol.org [68].
EXIG-A2A-07 · DOIT
Suivi des tâches longues
Lorsque la durée attendue d’une tâche dépasse 5 secondes (seuil fixé par le cadre), le client DOIT 
la suivre par flux en continu (SendStreamingMessage) ou par notification push. L’interrogation par 
GetTask et la reprise par SubscribeToTask PEUVENT servir à rétablir le suivi après une coupure, mais 
NE DOIVENT PAS servir au suivi courant.
Pourquoi  : une connexion bloquante longue se heurte aux délais des intermédiaires réseau, et une boucle 
d’interrogation consomme sans rien apprendre; la spécification laisse ce choix au client, d’où cette règle interne.
Liaisons, versions et sécurité
A2A 1.0 définit trois liaisons standard dérivées d’un même modèle abstrait : JSON-RPC 2.0 sur HTTP(S), 
gRPC sur HTTP/2 avec TLS, et HTTP+JSON (REST), dont le JSON est structurellement équivalent 
aux définitions Protobuf. La spécification exige d’un agent qui offre plusieurs liaisons une équivalence 
fonctionnelle (mêmes opérations, résultats sémantiquement équivalents, mêmes erreurs, mêmes schémas 
d’authentification), et d’une liaison personnalisée un comportement cohérent avec les opérations abs­
traites[68]. Le cadre retient JSON-RPC comme liaison commune, car certaines passerelles ne relaient que 
celle-là : Azure API Management, par exemple, n’importe les API d’agents A2A qu’en JSON-RPC[109]. La 
liaison SLIMRPC d’AGNTCY est expérimentale et ne fait pas partie des liaisons standard[239] (section 6.9).
Chaque requête porte l’en-tête A2A-Version au format majeur.mineur (p. ex. 1.0), ou le paramètre de requête 
équivalent. Un en-tête vide est interprété comme la version 0.3 (la spécification ne dit rien de l’en-tête 
absent, que le cadre assimile à un en-tête vide), et un agent qui ne prend pas en charge la version demandée 
renvoie VersionNotSupportedError [68] : un client 1.0 qui omet l’en-tête échoue donc contre un serveur 1.0 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 71 sur 283


---
## [Page PDF 72]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
strict. Le type média application/a2a+json est recommandé pour la seule liaison HTTP+JSON; JSON-RPC 
emploie application/json, les flux text/event-stream et gRPC Protobuf[68].
Pour la sécurité, la spécification pose les bases et le cadre les durcit. La sécurité de transport est obligatoire 
en production; la spécification recommande TLS 1.3, et le guide d’implémentation en entreprise admet 
TLS 1.2 ou plus[68, 161]. L’identité relève de la couche transport : les justificatifs s’obtiennent hors bande et 
voyagent dans les en-têtes HTTP; le serveur authentifie chaque requête (401 si le justificatif manque ou est 
invalide, 403 s’il est insuffisant) et autorise avant toute opération susceptible de divulguer de l’information. 
L’autorisation peut se faire par compétence, chaque AgentSkill pouvant porter ses propres exigences de 
sécurité[161, 192]. La version 1.0 retire les flux OAuth implicite et par mot de passe, et ajoute le flux Device Code 
et PKCE[30]. Le champ tenant permet à un point de terminaison d’héberger plusieurs agents ou locataires, 
les résultats devant rester dans le périmètre autorisé de l’appelant. Enfin, l’agent valide tous ses paramètres 
d’entrée, limite la taille des messages et des fichiers, et ne journalise ni justificatifs ni renseignements 
personnels sans protection[68].
Les notifications push demandent une attention particulière : c’est l’agent serveur qui appelle une URL 
fournie par le client, un point de rappel HTTP (webhook), ce qui en fait une cible de falsification de requête 
côté serveur (SSRF). La spécification exige que l’agent joigne les justificatifs prévus par la configuration et 
tente au moins une livraison; elle recommande un délai d’expiration de 10 à 30 secondes, des reprises avec 
repli exponentiel et le rejet des URL visant 127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 
localhost ou une adresse lien-local. Le récepteur doit valider l’authenticité de la notification et répondre 
par un code 2xx; il devrait vérifier que la tâche signalée est l’une des siennes. La livraison est tentée « au 
moins une fois », sans garantie de succès (reprises facultatives) et avec des doublons possibles, d’où un 
traitement idempotent[68].
EXIG-A2A-08 · DOIT
Version annoncée et liaisons standard
Tout client A2A DOIT envoyer A2A-Version à chaque requête. Tout agent DOIT exposer la liaison 
JSON-RPC et PEUT ajouter gRPC ou HTTP+JSON lorsque la passerelle d’agents les prend en charge, 
à condition d’offrir par chaque liaison les mêmes opérations, les mêmes erreurs et les mêmes schémas 
d’authentification. Une liaison non standard, dont SLIMRPC, NE DOIT PAS servir en production hors 
d’un pilote approuvé par le comité d’architecture.
Pourquoi : la version explicite évite les replis silencieux vers 0.3, et une liaison commune garde chaque agent 
joignable par toutes les plateformes retenues.
EXIG-A2A-09 · DOIT
Transport chiffré et authentification à chaque requête
Tout échange A2A DOIT utiliser TLS 1.3 par défaut, TLS 1.2 étant le plancher toléré (versions 
antérieures désactivées), avec validation des certificats, transiter par la passerelle d’agents et être 
authentifié à chaque requête. L’agent serveur DOIT autoriser avant toute opération qui lit ou divulgue 
de l’information, valider ses paramètres et borner la taille des messages et des fichiers.
Pourquoi : la passerelle applique au trafic entre agents les contrôles déjà appliqués aux outils; la documentation A2A 
recommande fortement une solution de gestion d’API pour les agents exposés[161].
EXIG-A2A-10 · DOIT
Autorisation par compétence et par locataire
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 72 sur 283


---
## [Page PDF 73]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Chaque compétence publiée DOIT être associée à une portée OAuth dédiée, déclarée dans ses 
securityRequirements et inscrite au catalogue. L’appelant DOIT présenter un jeton délégué dont 
l’audience est l’agent appelé (section 9.3). Lorsqu’un point de terminaison sert plusieurs locataires, la 
passerelle DOIT vérifier que le tenant demandé correspond aux droits du jeton, sans jamais le déduire 
du seul contenu de la requête.
Pourquoi : le moindre privilège s’applique à la compétence, pas à l’agent entier; un jeton valide pour analyser un 
dossier ne doit pas permettre d’accorder un prêt.
EXIG-A2A-11 · NE DOIT PAS
Flux OAuth retirés
Les agents et leurs clients NE DOIVENT PAS employer l’octroi implicite ni l’octroi par mot de passe. 
Ils DOIVENT utiliser le code d’autorisation avec PKCE[175] (ou le Device Code pour un appareil sans 
navigateur) quand une personne s’authentifie, les justificatifs client pour un agent qui agit en son nom 
propre et, pour la délégation, l’échange de jetons de la RFC 8693[70].
Pourquoi : A2A 1.0 a retiré ces flux[240], et la RFC 9700 interdit l’octroi par mot de passe et déconseille l’octroi 
implicite[175].
EXIG-A2A-12 · DOIT
Notifications push durcies
Le cadre rend obligatoires les recommandations de la spécification. L’agent serveur DOIT valider l’URL 
de webhook contre la SSRF à l’enregistrement et à chaque livraison, après résolution DNS (plages 
privées, boucle locale et lien-local refusées), appliquer un délai d’expiration compris entre 10 et 30 
secondes et des reprises à repli exponentiel. Le récepteur DOIT authentifier la notification, vérifier que 
l’identifiant de tâche lui appartient et traiter chaque notification de façon idempotente.
Pourquoi : un webhook non filtré permet à un client malveillant de faire sonder le réseau interne par l’agent.
EXIG-A2A-13 · DOIT
Traçage et corrélation des tâches
Chaque appel A2A DOIT propager l’en-tête W3C traceparent et être tracé côté appelant par un span 
invoke_agent de type CLIENT. Le journal d’audit DOIT consigner taskId, contextId et l’identifiant 
de trace (section 10.1 et section 10.3).
Pourquoi : la v1.41.0 des conventions OpenTelemetry n’a pas de convention propre à A2A (une convention A2A, 
au niveau Development, figure depuis peu dans la branche principale du dépôt semantic-conventions-genai, sans 
version étiquetée)[241]; la convention des agents trace un agent distant par un span invoke_agent CLIENT[120], et la 
documentation A2A recommande le traçage distribué[161].
Déroulement d’une délégation avec approbation
La figure 9 montre comment A2A, MCP et l’approbation humaine se combinent. Un orchestrateur confie 
l’analyse d’un dossier de crédit commercial à un agent spécialiste; l’inscription de la décision dans l’ERP est 
classée P3 au catalogue et exige donc une approbation humaine (section 8.3).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 73 sur 283


---
## [Page PDF 74]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Utilisateur
et approbateur
Orchestrateur
client A2A
Registre
cartes signées
Passerelle
d’agents
Agent crédit
serveur A2A
Serveurs MCP
bureau de crédit, ERP
1
« Analyser le dossier 8841 »
2
compétence « risque de crédit »
carte d’agent (signature vérifiée)
3
SendStreamingMessage
A2A-Version: 1.0 · jeton délégué · traceparent
4
WORKING
tools/call lire_dossier
5
INPUT_REQUIRED : approbation requise
6
action exacte à approuver
jeton d’approbation signé
7
SendMessage (même taskId) + approbation
8
tools/call enregistrer
+ clé d’idempotence
9
artefact + COMPLETED
10
confirmation + réf. d’audit
Figure 9 — Délégation A2A avec appel MCP et approbation humaine. Les numéros renvoient aux étapes ci-dessous. La passerelle 
d’agents se trouve sur chaque appel, et l’écriture n’a lieu qu’avec un jeton d’approbation lié à l’action exacte. Source : élaboration du 
cadre, d’après la spécification A2A 1.0 et MCP 2026-07-28.
1. L’utilisateur demande à l’orchestrateur d’analyser le dossier 8841.
2. L’orchestrateur cherche au registre la compétence « risque de crédit », obtient la carte de l’agent 
spécialiste et en vérifie la signature.
3. Il obtient un jeton délégué dont l’audience est l’agent crédit, puis envoie SendStreamingMessage par la 
passerelle avec A2A-Version: 1.0, le jeton et traceparent. Le message porte le sous-objectif structuré 
et des références de documents, jamais l’historique brut de la conversation (section 7.7).
4. L’agent crédit passe à WORKING et lit le dossier par un outil MCP (tools/call), sous un jeton échangé 
pour l’audience du serveur MCP.
5. Prêt à inscrire sa décision, il passe à INPUT_REQUIRED et décrit, dans une partie data, l’action exacte à 
approuver : outil, arguments, montant.
6. L’orchestrateur soumet cette action à un approbateur habilité, hors de la conversation; l’approbation 
produit un jeton signé lié à l’empreinte de l’action (section 8.5).
7. L’orchestrateur envoie un nouveau message rattaché au même taskId, qui transmet le jeton 
d’approbation.
8. L’agent crédit appelle l’outil d’écriture de l’ERP avec le jeton d’approbation et une clé d’idempotence 
(section 7.6); la passerelle vérifie que le jeton correspond exactement à cet appel avant de le relayer.
9. L’agent livre son artefact, et la tâche passe à COMPLETED.
10. L’orchestrateur confirme le résultat à l’utilisateur avec la référence du journal d’audit.
Si l’approbateur refuse ou si le délai d’approbation expire, l’orchestrateur annule la tâche (CancelTask) et 
aucune écriture n’a lieu. Un « oui » saisi dans la conversation n’est jamais une approbation : seul compte 
le jeton signé, vérifié par la passerelle.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 74 sur 283


---
## [Page PDF 75]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Migration et compatibilité
Une carte 1.0 peut annoncer à la fois des interfaces 0.3 et 1.0, distinguées par protocolVersion, et les 
SDK officiels assurent la rétrocompatibilité[29, 68]. Les principaux changements à absorber sont les suivants : 
supportedInterfaces remplace url, preferredTransport et additionalInterfaces; les parties sont uni­
fiées; les états prennent le préfixe TASK_STATE_; l’opération de flux devient SendStreamingMessage [235]. Les 
SDK n’ont pas atteint la 1.0 en même temps : celui de JavaScript n’est en disponibilité générale que depuis 
le 22 juillet 2026[242]. La trousse a2a-tck teste les trois liaisons standard, à partir des interfaces déclarées 
dans la carte, selon trois niveaux : MUST (échec bloquant), SHOULD (échec signalé, non bloquant) et MAY 
(test sauté si la fonction n’est pas déclarée)[243]. L’interface en ligne de commande officielle, présentée le 1er 
octobre 2026 (versions publiées dès le 9 septembre 2026), s’insère dans les chaînes d’intégration grâce à sa 
sortie JSON et à ses codes de sortie prévisibles, par exemple pour des tests de fumée[244, 245].
EXIG-A2A-14 · DOIT
Compatibilité vérifiée avant inscription
Un agent DOIT réussir tous les tests de niveau MUST d’a2a-tck, sur chaque liaison déclarée, avant 
son inscription au registre et à chaque nouvelle version mineure ou majeure de sa carte. Tout échec de 
niveau SHOULD DOIT être consigné à la fiche, avec une échéance de correction.
Pourquoi : la conformité se prouve par un test reproductible, pas par une déclaration du fournisseur.
EXIG-A2A-15 · DEVRAIT
Migration bornée depuis la version 0.3
Un agent encore en 0.3 DEVRAIT migrer par double publication : sa carte annonce une interface 1.0 et 
une interface 0.3, cette dernière portant une date de retrait inscrite au catalogue, au plus six mois après 
l’ouverture de l’interface 1.0 (choix du cadre). Passé cette date, la passerelle DOIT refuser les requêtes 
sans en-tête A2A-Version.
Pourquoi : la coexistence évite de basculer tous les clients le même jour, et l’échéance empêche la version obsolète 
de devenir permanente.
6.7 Interopérabilité événementielle
Cette section encadre les échanges asynchrones  : un agent ou un système publie un fait sur un bus 
d’événements, et un ou plusieurs agents y réagissent sans que l’émetteur les connaisse. Elle fixe l’enveloppe, 
les contrats, les attributs de gouvernance et les garanties sur lesquelles une conception peut réellement 
compter.
Quand préférer l’événement
MCP et A2A fonctionnent par demande et réponse : l’appelant connaît son destinataire et attend un résultat. 
L’événement convient mieux dans trois cas. Découplage dans le temps : le traitement peut attendre, ou le 
consommateur peut être indisponible un moment (lots de nuit, pointes de charge, réaction aux changements 
d’état d’un ERP). Plusieurs abonnés : un même fait intéresse plusieurs agents, et l’on veut en ajouter sans 
toucher à l’émetteur. Rejeu : on veut relire la séquence des faits pour un audit ou pour évaluer une nouvelle 
version d’agent. Par exemple, une alerte de rupture de stock intéresse la planification, l’approvisionnement 
et le service à la clientèle; publiée une fois, elle les atteint tous les trois sans que le détecteur les connaisse.
S’y ajoute un argument de topologie : relier N agents deux à deux exige jusqu’à N(N−1)/2 liaisons, alors 
que N agents reliés à un courtier n’en exigent que N. Le gain porte sur le nombre de connexions; les 
sujets, les schémas et les contrats restent à gouverner. L’abonnement évite aussi le délai propre aux boucles 
d’interrogation. Comme le souligne Kai Waehner, conseiller indépendant en diffusion de données en continu 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 75 sur 283


---
## [Page PDF 76]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
(data streaming), MCP n’offre ni garantie de livraison ni cohérence, alors qu’un journal persistant et ordonné 
découple producteurs et consommateurs : les deux approches se complètent[167, 246].
EXIG-EVT-01 · DEVRAIT
Recours au bus pour l’asynchrone
Une interaction qui n’attend pas de réponse immédiate, qui intéresse plusieurs consommateurs ou qui 
doit pouvoir être rejouée DEVRAIT passer par le bus d’événements de l’entreprise plutôt que par une 
chaîne d’appels A2A ou MCP. Le choix suit la matrice de la section 6.4 et le patron de chorégraphie de 
la section 7.2.
Pourquoi : une chaîne d’appels synchrones lie la disponibilité de chaque agent à celle de tous les autres.
Enveloppe et contrats
Le cadre retient CloudEvents 1.0 comme enveloppe. La dernière révision publiée est la 1.0.2 (février 2022), les 
producteurs indiquent toujours specversion « 1.0 », et le projet a obtenu le statut « Graduated » de la CNCF 
le 25 janvier 2024[173, 247, 248]. CloudEvents exige quatre attributs de contexte (id, source, specversion, type) 
et en propose quatre facultatifs (datacontenttype, dataschema, subject, time)[248]. Le contrat de chaque 
sujet se décrit en AsyncAPI 3.x : la 3.0.0 date du 5 décembre 2023, et la 3.1.0, publiée le 31 janvier 2026, est 
une version mineure sans rupture[174, 249].
Sur Kafka, la liaison CloudEvents offre un mode binaire (attributs, sauf datacontenttype porté par l’en-
tête content-type, dans des en-têtes préfixés ce_; données telles quelles dans la valeur) et un mode 
structuré (événement complet en application/cloudevents+json); un « Key Mapper » facultatif, à activer 
explicitement, peut copier partitionkey dans la clé Kafka[250]. Le cadre retient le mode binaire par défaut : 
les données restent intactes, et les intermédiaires filtrent sur les attributs sans désérialiser la charge 
utile. Un consommateur détermine le mode d’après l’en-tête content-type : un type qui commence par 
application/cloudevents indique le mode structuré, tout autre type le mode binaire[250]. Un exemple 
d’événement complet figure à l’annexe C.
EXIG-EVT-02 · DOIT
Enveloppe CloudEvents complète
Tout événement produit ou consommé par un agent DOIT respecter CloudEvents 1.0 et porter, en plus 
des quatre attributs requis, time, datacontenttype et dataschema (exigence du cadre). Le type DOIT 
être un nom en domaine inversé qui inclut sa version (exigence du cadre; la norme recommande seule­
ment le préfixe en domaine inversé), par exemple ca.entreprise.logistique.alerte.rupture.v1.
Pourquoi : un consommateur doit savoir, sans ouvrir la charge utile, ce qu’il reçoit, quand le fait s’est produit (ou, si 
cet instant est inconnu, l’heure que la source retient de façon uniforme) et quel schéma le valide.
EXIG-EVT-03 · DOIT
Contrat AsyncAPI au catalogue
Chaque sujet du bus DOIT être décrit par un contrat AsyncAPI 3.x inscrit au catalogue d’entreprise. Le 
contrat précise le schéma versionné des données et la clé de partition; l’entrée de catalogue précise le 
propriétaire, la classification et les producteurs et consommateurs autorisés, pour lesquels AsyncAPI ne 
définit aucun champ normalisé (section 6.8). Un changement incompatible de schéma crée un nouveau 
type versionné, selon les règles de la section 6.8.
Pourquoi : sans contrat, chaque consommateur devine le format et casse au premier changement.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 76 sur 283


---
## [Page PDF 77]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Extensions de gouvernance
Les attributs requis par CloudEvents ne disent ni quel agent a lancé la chaîne, ni au nom de qui, ni à quel coût. 
Le cadre ajoute donc des extensions, en privilégiant celles que CloudEvents documente déjà; ces extensions 
documentées n’ont pas de statut officiel et peuvent évoluer, et trois d’entre elles (Auth Context, Data Classi­
fication et Expiry Time) ne figurent pas dans la révision 1.0.2, qui ne documente que Dataref, Distributed 
Tracing, Partitioning, Sampling et Sequence[251][187], si bien que le cadre fige au catalogue la version qu’il en 
retient. Un nom d’attribut ne contient que des minuscules ASCII et des chiffres, et ne devrait pas dépasser 
20 caractères; le préfixe x n’est ni exigé ni défini par la norme, et le cadre le garde pour signaler ses propres 
extensions[248]. Pour désigner l’initiateur, l’extension documentée Auth Context remplace une extension 
maison : elle est purement informative, déconseille les renseignements personnels dans authid et interdit 
d’inclure dans authclaims des justificatifs permettant d’usurper directement l’identité du mandant[252].
Le contexte de trace mérite une précision. L’extension Distributed Tracing prévoit que, pour une transmis­
sion en plusieurs sauts, traceparent porte la trace de départ et non celle de chaque saut; elle ne remplace 
pas les en-têtes de traçage du transport[253]. Les conventions OpenTelemetry de messagerie, au niveau 
Development, recommandent que le producteur injecte le contexte de création dans le message et relient 
par défaut producteur et consommateur par des liens de span plutôt que par parenté (la parenté n’étant 
admise que pour un message unique)[254].
Tableau 20 — Attributs d’extension CloudEvents exigés par le cadre
Attribut
Origine
Contenu
Règle du cadre
traceparent (tracestate facul­
tatif)
Extension documentée Distri­
buted Tracing
Contexte W3C Trace Context 
de la trace que poursuit 
l’agent émetteur
Obligatoire; jamais un identi­
fiant métier
authtype, authid
Extension documentée Auth 
Context
Type de mandant, se­
lon les valeurs recomman­
dées par l’extension (app_user 
pour l’utilisateur final d’une 
application, user pour 
un compte d’infrastructure, 
service_account, api_key, 
system pour une identi­
té volontairement masquée, 
unauthenticated, unknown), et 
son identifiant
Obligatoires; authid pseudo­
nyme
dataclassification, 
dataregulation, datacategory
Extension documentée Data 
Classification[255]
étiquettes recommandées par 
l’extension lorsque aucun ré­
gime n’en définit : public, 
internal, confidential ou 
restricted; régime applicable 
(liste séparée par des virgules); 
catégorie selon le régime 
(p. ex. sensitive-pii, exemple 
américain de l’extension)
dataclassification obliga­
toire; les deux autres dès 
que l’événement touche des 
RP
xagentorigin
Propre au cadre
Identifiant au registre et ver­
sion de l’agent qui a publié 
le premier événement de la 
chaîne
Obligatoire sur tout événe­
ment publié par un agent
xagenthopcount
Propre au cadre
Entier (type Integer de Clou­
dEvents) : nombre de publica­
tions d’agents dans la chaîne 
causale (1 pour la première)
Obligatoire; augmenté de 1 
à chaque republication
xagentmaxhops
Propre au cadre
Entier (type Integer de Clou­
dEvents) : plafond de sauts 
fixé au contrat du flux; 
l’événement dont le compteur 
Obligatoire; 4 par défaut; re­
copié sans modification
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 77 sur 283


---
## [Page PDF 78]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Attribut
Origine
Contenu
Règle du cadre
atteint ce plafond n’est pas 
traité
xcostcenter
Propre au cadre
Centre de coûts imputé
Obligatoire; valeur du réfé­
rentiel financier
partitionkey, sequence, 
expirytime, dataref
Extensions documentées
Clé de partition, rang, 
échéance, référence externe 
aux données
Au besoin, de préférence à 
toute extension maison
EXIG-EVT-04 · DOIT
Attributs de gouvernance présents et vérifiés
Tout événement publié par un agent DOIT porter les attributs obligatoires du tableau 20. Un consom­
mateur DOIT refuser un événement d’agent qui en est dépourvu et le diriger vers la file de lettres 
mortes (dead-letter queue). Il DOIT aussi tenir compte de dataclassification et rejeter l’événement 
dont il ne peut respecter les exigences ou dont il ne reconnaît pas la valeur, comme l’exige l’extension 
Data Classification, qui demande aussi aux intermédiaires de ne pas modifier ces attributs[255]. Un 
intermédiaire qui relaie un événement NE DOIT PAS modifier traceparent; un agent qui publie un 
nouvel événement en réaction y DOIT recopier le traceparent de l’événement reçu (ou, s’il ouvre la 
chaîne, celui de la trace qu’il ouvre) (section 10.1).
Pourquoi : sans ces attributs, une chaîne d’agents n’est ni traçable, ni imputable, ni bornée.
EXIG-EVT-05 · NE DOIT PAS
Aucun renseignement personnel dans les attributs
Les attributs d’un événement, lus par chaque intermédiaire et recopiés dans les journaux et les traces, 
NE DOIVENT PAS contenir de renseignement personnel direct (nom, courriel, numéro de compte) 
ni de justificatif; une personne n’y figure que sous un identifiant pseudonyme opaque, qui demeure 
un renseignement personnel (section 12.2) et dont la table de correspondance reste hors du bus. 
Les données personnelles volumineuses ou sensibles restent dans le système source; l’événement ne 
transmet qu’une référence (dataref), sans data, dont l’accès est contrôlé.
Pourquoi : un bus réplique chaque événement chez tous ses abonnés; limiter les RP qu’il transporte réduit d’autant 
la surface à protéger au titre de la Loi 25 (section 12.2).
Prévention des tempêtes d’événements
Dans une chorégraphie, aucun composant central ne voit l’ensemble. Deux agents qui réagissent chacun 
aux événements de l’autre peuvent donc s’entretenir indéfiniment : la planification révise une prévision, 
l’approvisionnement ajuste une commande, ce qui déclenche une nouvelle révision, et ainsi de suite. Chaque 
tour consomme des jetons et peut produire des effets réels. Le compteur de sauts coupe cette boucle de 
façon déterministe, sans dépendre du jugement d’un modèle (figure 10). Ce compteur et son plafond sont 
des conventions propres au cadre : aucune extension CloudEvents normalisée ne les couvre[187].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 78 sur 283


---
## [Page PDF 79]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Bus d’événements de l’entreprise · sujets régis par contrats AsyncAPI · enveloppe CloudEvents
Détecteur de rupture
publie l’alerte
saut 1/4
Planification
consomme, republie
saut 2/4
Approvisionnement
consomme, republie
saut 3/4
Agent N
reçoit saut 4/4
File de lettres mortes
+ alerte d’observabilité
boucle interrompue
Règle de chaque consommateur
si xagenthopcount ≥ xagentmaxhops
→ lettres mortes + alerte
sinon traiter, publier hop + 1
Chaque événement porte le contexte de la trace poursuivie (traceparent), l’agent d’origine, l’initiateur et le centre de coûts.
Figure 10 — Chorégraphie événementielle et compteur de sauts. Chaque republication augmente xagenthopcount; l’événement 
qui atteint le plafond (4 par défaut) n’est pas traité : il part en file de lettres mortes et déclenche une alerte. Source : élaboration du 
cadre; enveloppe CloudEvents 1.0.
EXIG-EVT-06 · DOIT
Compteur de sauts et coupure des boucles
Le premier agent qui publie dans une chaîne DOIT fixer xagenthopcount à 1, xagentorigin à son 
identifiant et xagentmaxhops à la valeur du contrat du flux (4 par défaut). Tout agent qui publie en 
réaction à un événement reçu DOIT augmenter le compteur de 1 et recopier les deux autres valeurs sans 
les modifier. Un agent qui reçoit un événement dont xagenthopcount atteint ou dépasse xagentmaxhops 
DOIT s’abstenir de le traiter, le diriger vers la file de lettres mortes et lever une alerte. Le plafond d’un 
flux ne se relève que par une modification revue de son contrat.
Pourquoi : une règle locale, appliquée par chaque consommateur, borne la longueur de toute chaîne d’événements 
qui ne traverse que des consommateurs conformes (un composant qui n’applique pas la règle, ou qui n’est pas un 
agent, rompt la chaîne causale).
EXIG-EVT-07 · DOIT
Autorisation fondée sur l’identité, pas sur les attributs
Le droit de publier ou de consommer sur un sujet DOIT reposer sur l’identité authentifiée de l’agent 
auprès du courtier et sur des listes de contrôle d’accès par sujet, tirées de l’entrée de catalogue du sujet 
(producteurs et consommateurs autorisés). Une décision d’autorisation NE DOIT PAS se fonder sur 
authtype, authid ou un autre attribut de l’événement pour accorder un accès (dataclassification 
ne peut que le restreindre). Les données reçues DOIVENT être traitées comme du contenu non fiable 
(section 9.6).
Pourquoi : l’extension Auth Context est informative et n’est pas un mécanisme de sécurité[252]; n’importe quel 
producteur peut y écrire n’importe quoi.
Garanties réelles d’un bus
Apache Kafka sert ici d’exemple parce que ses garanties sont documentées avec précision; un autre courtier 
se juge sur les mêmes questions. Le tableau 21 distingue ce que le courtier garantit de ce qui reste à la charge 
de la conception.
Tableau 21 — Garanties d’un bus Kafka et responsabilités de la conception
Propriété
Ce que Kafka garantit
Ce qui reste à la conception
Livraison
« Au moins une fois » par défaut; le producteur idempotent 
(depuis 0.11.0.0) évite les doublons dans le journal lors des 
reprises[140]
Consommateurs idempotents et dédu­
plication
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 79 sur 283


---
## [Page PDF 80]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Propriété
Ce que Kafka garantit
Ce qui reste à la conception
Exactement une 
fois
Cycle lecture-traitement-écriture entre sujets Kafka (transactions, 
consommateur read_committed); un système externe doit coopé­
rer[140, 256]
Clé d’idempotence vérifiée par le sys­
tème cible; patron de la boîte d’envoi
Ordre
Par partition seulement; les événements de même clé vont dans la 
même partition[257]
Choisir la clé selon l’entité dont l’ordre 
compte
Répartition du 
travail
Rééquilibrage natif des groupes de consommateurs; files coopéra­
tives (share groups) dont l’ordre n’est garanti qu’à l’intérieur d’un 
lot[258]
Réserver les files coopératives aux 
tâches indépendantes
Rejeu
Relecture depuis un décalage sauvegardé, dans la limite de la 
rétention configurée[140]
Rétention suffisante; rejeu isolé; au­
cune promesse de décisions identiques
Quelques repères de version aident à fixer au catalogue la version plancher du courtier. Kafka 4.0 (18 mars 
2025) est la première version majeure entièrement sans ZooKeeper et généralise le nouveau protocole de 
rééquilibrage des groupes[259]. Les files coopératives sont prêtes pour la production depuis Kafka 4.2.0 (17 
février 2026), et Kafka 4.4.0 (22 octobre 2026) leur ajoute des files de lettres mortes[260, 261].
La conséquence pratique tient en une phrase  : un effet réel n’est jamais protégé par le bus, mais par 
l’idempotence du consommateur et du système cible. Kafka seul n’empêche pas un double paiement. Pour 
publier de façon fiable un changement d’état et l’événement qui l’annonce, le producteur applique le patron 
de la boîte d’envoi (transactional outbox) : il écrit l’événement dans une table de sa base, dans la même 
transaction locale que le changement, puis un relais le publie. Aucun événement ne part ainsi pour une 
transaction annulée, et aucun changement validé ne reste sans événement.
Le rejeu appelle la même prudence. Confluent présente le rejeu déterministe des événements comme le 
fondement de l’investigation d’un incident, de l’audit réglementaire, de la validation de modèle et des mises 
à jour sûres des agents[262]. Rejouer les entrées ne garantit pourtant pas que l’agent reprendra les mêmes 
décisions, car rien n’assure qu’un modèle produise la même sortie à entrées identiques. Le cadre parle donc 
de rejeu des entrées pour l’audit et la réévaluation, jamais de reproduction des décisions.
EXIG-EVT-08 · DOIT
Effets réels protégés par l’idempotence
Tout consommateur dont le traitement produit un effet hors du bus DOIT être idempotent  : il 
déduplique sur l’identité de l’événement (source et id; le producteur et le relais de la boîte d’envoi 
DOIVENT les conserver à chaque renvoi du même événement, ce que la norme permet sans l’imposer) 
et transmet au système cible une clé d’idempotence que ce dernier vérifie (section 7.6). Un producteur 
qui publie à la suite d’un changement dans sa base DOIT appliquer le patron de la boîte d’envoi ou un 
mécanisme transactionnel équivalent. La sémantique « exactement une fois » du courtier NE DOIT 
PAS être invoquée comme protection contre un double effet externe.
Pourquoi : la livraison est « au moins une fois »[140]; sans idempotence, une seule reprise suffit à payer deux fois une 
facture.
EXIG-EVT-09 · DOIT
Ordre garanti par la clé de partition
Lorsqu’un flux exige l’ordre des événements d’une même entité (dossier, commande, session), la 
clé de partition DOIT être l’identifiant technique de cette entité, sans renseignement personnel 
(EXIG-EVT-05), porté par partitionkey et précisé au contrat AsyncAPI. Le producteur DOIT aussi 
copier cette valeur dans la clé du message Kafka, au moyen d’un « Key Mapper » à activer explicitement, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 80 sur 283


---
## [Page PDF 81]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
car la liaison reprend par défaut la clé fournie par l’utilisateur[250]. Les files coopératives NE DOIVENT 
PAS servir à un tel flux; elles conviennent aux bassins d’exécutants dont les tâches sont indépendantes.
Pourquoi : Kafka ne garantit l’ordre qu’au sein d’une partition, et une file coopérative ne le garantit qu’à l’intérieur 
d’un lot.
EXIG-EVT-10 · DOIT
Conservation des entrées et rejeu isolé
Les sujets qui alimentent des agents de classe de risque modérée ou élevée DOIVENT conserver leurs 
événements au moins pendant la fenêtre d’enquête inscrite à la fiche de l’agent (au moins 90 jours 
pour la classe modérée et un an pour la classe élevée, sans excéder la rétention des traces et journaux 
d’audit fixée au chapitre 10), dans la limite du calendrier de conservation applicable aux RP. Tout rejeu 
DOIT s’exécuter dans un environnement isolé où les outils à effet sont remplacés par des doublures; 
ses résultats servent à l’audit et à l’évaluation continue (section 10.4), jamais à répéter des actions en 
production.
Pourquoi : rejouer des entrées contre des outils réels répéterait leurs effets, et un modèle peut décider autrement la 
seconde fois.
6.8 Contrats, versionnage et catalogue d’entreprise
Cette section fixe ce que chaque interface offerte à un agent doit déclarer, comment ses versions évoluent 
sans briser ses consommateurs et ce que contient le catalogue d’entreprise.
Ce que chaque contrat déclare
Un contrat a deux faces : ce que le fournisseur publie dans le format du protocole, et ce que l’entreprise fixe 
au catalogue. Comme les annotations MCP sont des indices non fiables (EXIG-MCP-14) et que la carte A2A 
n’admet aucun champ de gouvernance hors norme (EXIG-A2A-05), tout ce qui commande une décision de 
sécurité vit au catalogue (tableau 22; exemples à l’annexe C).
Tableau 22 — Contenu minimal des contrats, par type d’interface
Interface
Contrat publié
Entrée fixée au catalogue
Outil MCP
Nom préfixé par le domaine; description destinée au 
modèle, qui dit ce que fait l’outil et ce qu’il ne fait 
pas; inputSchema et, au besoin, outputSchema en JSON 
Schema 2020-12; clé d’idempotence pour tout outil à 
effet (section 7.6)
Version et empreinte; palier P0 à P3 et seuil 
(section 8.3); compensation de toute écriture P2; 
propriétaire et équipe de garde; classification maxi­
male des données
Ressource et in­
vite MCP
Ressource adressée par URI; invite nommée et décrite
Version et empreinte; classification
Agent A2A
Carte A2A 1.0 signée (section 6.6)
Version et empreinte; portée OAuth par compé­
tence; renvoi à la fiche du registre
Sujet 
d’événement
Contrat AsyncAPI 3.x et type versionné (section 6.7)
Producteurs et consommateurs autorisés; classifi­
cation; plafond de sauts
API existante
Contrat OpenAPI 3.1.x ou 3.2.x; erreurs au format RFC 
9457[171]
Outils MCP qui l’exposent, chacun avec son entrée
EXIG-INT-12 · DOIT
Contrat complet avant l’inscription
Toute interface offerte à un agent DOIT disposer, avant son inscription au catalogue d’entreprise, d’un 
contrat publié et d’une entrée de catalogue qui contiennent au minimum les éléments du tableau 22. 
Un élément manquant bloque l’inscription.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 81 sur 283


---
## [Page PDF 82]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Pourquoi : la passerelle n’applique que des règles écrites; sans palier ni compensation déclarés, l’agent déciderait 
seul de ce qui est sûr.
Versionnage sémantique
La version d’un protocole ne dit rien des contrats publiés sur lui. Or la définition d’un outil MCP ne comporte 
aucun champ de version[197], et le champ version d’une carte A2A est de format libre[68]. Le cadre impose 
donc aux contrats le versionnage sémantique (SemVer), de forme MAJEUR.MINEUR.CORRECTIF, tenu au 
catalogue :
• majeur : tout changement qui peut faire échouer ou tromper un consommateur (élément retiré ou 
renommé, nouveau paramètre obligatoire, valeurs admises restreintes en entrée, valeur ajoutée à une 
énumération de sortie, changement de sens à format constant);
• mineur : ajout compatible et toute reformulation d’une description;
• correctif : correction qui ne change ni la définition publiée ni le comportement attendu.
Le changement de sens est le plus dangereux, car aucun validateur ne le voit : un montant qui passe de hors 
taxes à toutes taxes comprises reste un nombre valide (section 6.1). A2A applique la même logique à ses 
extensions, dont tout changement incompatible exige une nouvelle URI[238].
EXIG-INT-13 · DOIT
Versionnage sémantique des contrats
Tout contrat inscrit au catalogue DOIT porter une version SemVer, incrémentée à chaque publication 
selon les règles ci-dessus : au moins mineure pour toute modification de la définition publiée (nom, 
description, schémas, annotations, compétences), majeure pour tout changement incompatible, y 
compris de sens. Pour un agent A2A, c’est le champ version de sa carte (EXIG-A2A-04).
Pourquoi : un numéro régi par des règles connues dit au consommateur s’il peut migrer sans risque (règle du cadre).
EXIG-INT-14 · DOIT
Coexistence d’au moins 60 jours
À la publication d’une version majeure, la version majeure précédente DOIT rester disponible au moins 
60 jours (choix du cadre), avec une date de retrait inscrite au catalogue dès ce moment et annoncée aux 
consommateurs connus. Seul un motif de sécurité, sur décision du comité, justifie un retrait anticipé.
Pourquoi : un délai connu permet de planifier les migrations; il concorde avec le préavis de retrait d’un agent 
(section 11.5).
Épinglage et approbation des changements
Un consommateur ne suit jamais « la dernière version ». Il dépend d’une version identifiée par son numéro 
et par son empreinte, soit le condensé SHA-256 de la définition canonisée selon la RFC 8785[236]. Le numéro 
dit ce que le fournisseur affirme; l’empreinte prouve ce que l’agent reçoit. La fiche d’agent consigne ces 
dépendances (annexe B), et la passerelle vérifie l’empreinte à l’exécution (EXIG-MCP-20, EXIG-SEC-18). 
L’OWASP recommande d’épingler les définitions par empreinte et de redemander le consentement à chaque 
modification[221].
EXIG-INT-15 · DOIT
Dépendances épinglées par version et empreinte
Chaque agent DOIT déclarer dans sa fiche, pour chaque outil, ressource, invite, agent appelé et sujet 
d’événement, la version épinglée et l’empreinte approuvée. Une dépendance NE DOIT PAS désigner 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 82 sur 283
