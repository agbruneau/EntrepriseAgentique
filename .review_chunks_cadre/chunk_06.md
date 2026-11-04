# chunk_06 — pages PDF 51 à 62 (sur 283)



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


---
## [Page PDF 53]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Scénario
Protocole
Couplage
État côté appelé
Raison du choix
Agent → agent 
d’une autre or­
ganisation
A2A par la passe­
relle, carte signée, 
jeton délégué
Lâche et contractuel
Tâche à états, opaque pour 
l’appelant
La confiance re­
pose sur la si­
gnature de la 
carte, le contrat et 
l’échange de je­
tons, pas sur le ré­
seau.
Système ou 
agent → plu­
sieurs agents 
réactifs
CloudEvents et 
AsyncAPI sur le 
bus d’événements
Découplé (publication-abonne­
ment)
Journal durable, rejouable dans 
la limite de la rétention[140]
Résilience, absorp­
tion des pointes, 
ajout d’abonnés 
sans toucher 
l’émetteur.
Agent → inter­
face utilisateur 
riche
AG-UI (Évaluer) ou 
flux SSE structuré
Temps réel
Session d’interface partagée
Synchronise l’état 
de l’agent et 
les formulaires 
d’approbation.
Lorsqu’un cas ne figure pas dans la matrice, quatre questions, posées dans l’ordre, mènent au bon choix :
1. Les étapes sont-elles connues d’avance? Si oui, un flux déterministe orchestre le travail et n’emploie un 
agent qu’aux étapes de jugement.
2. La cible est-elle un outil ou une donnée aux entrées et aux sorties définies? Si oui, MCP.
3. La cible raisonne-t-elle, garde-t-elle un état, peut-elle demander une précision ou une autorisation? Si 
oui, A2A; au-delà de 5 secondes (seuil fixé par le cadre, EXIG-A2A-07), la diffusion en continu ou les 
notifications push s’imposent (section 6.6).
4. L’émetteur doit-il ignorer qui consomme, ou faut-il plusieurs abonnés ou un rejeu? Si oui, un événement.
La quatrième question a une base arithmétique simple : relier N agents deux à deux exige jusqu’à N(N−1)/2 
intégrations, contre N connexions vers un courtier. Le bus réduit le nombre de liaisons, pas la gouvernance 
des sujets, des schémas et des contrats, qui reste entière.
EXIG-INT-10 · DOIT
Choix de protocole justifié par la matrice
Le protocole retenu pour chaque intégration DOIT être justifié dans la fiche d’agent par renvoi à une 
ligne du tableau 16. Un scénario absent de la matrice, ou un choix qui s’en écarte, DOIT être soumis à 
l’architecture d’entreprise avant la construction.
Pourquoi : la justification écrite rend le choix vérifiable en revue et alimente la mise à jour de la matrice.
EXIG-INT-11 · DEVRAIT
Diffusion d’un changement d’état par événement
Lorsqu’un changement d’état intéresse plusieurs consommateurs, l’agent ou le système émetteur 
DEVRAIT publier un événement plutôt qu’appeler chaque consommateur par A2A ou par MCP.
Pourquoi : l’appel direct couple l’émetteur à chaque consommateur et propage leurs pannes; le bus absorbe les 
pointes et accepte de nouveaux abonnés sans modifier l’émetteur.
6.5 Intégration verticale : Model Context Protocol
Cette section fixe la manière dont l’entreprise relie ses agents à leurs outils, à leurs ressources et à leurs 
invites au moyen du Model Context Protocol (MCP), dans sa révision 2026-07-28. Elle distingue ce que la 
spécification exige de ce que le cadre ajoute pour exploiter le protocole à l’échelle de l’entreprise : passerelle 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 53 sur 283


---
## [Page PDF 54]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
d’agents, catalogue d’entreprise, autorisation obligatoire et contrôles de sécurité propres au protocole. Les 
règles générales de contrat et de versionnage sont à la section 6.8; l’identité et la délégation, au chapitre 9.
Rôle et gouvernance du protocole
MCP normalise le lien vertical entre un agent et les systèmes qu’il consulte ou modifie. Au lieu d’écrire un 
connecteur pour chaque couple agent-système, on expose chaque système une seule fois par un serveur 
MCP, que tout agent conforme peut ensuite utiliser. Anthropic a annoncé MCP comme norme ouverte le 25 
novembre 2024[20]. La formule « N × M » qui résume ce bénéfice (chapitre 2) est une vulgarisation, non un 
énoncé de la spécification.
Le 9 décembre 2025, Anthropic a donné MCP à l’Agentic AI Foundation (AAIF), fonds dirigé de la Linux 
Foundation cofondé par Anthropic, Block et OpenAI; MCP en est un projet fondateur, aux côtés de goose 
et d’AGENTS.md[4, 193]. Au lancement, les membres platine étaient Amazon Web Services, Anthropic, 
Block, Bloomberg, Cloudflare, Google, Microsoft et OpenAI[4]. Le modèle de gouvernance technique est 
resté inchangé : des responsables principaux arbitrent l’évolution de la spécification, qui progresse par des 
propositions d’amélioration (SEP, Specification Enhancement Proposals), tandis que le conseil de l’AAIF gère 
la stratégie, le budget et les adhésions[14]. Depuis la révision 2026-07-28, une SEP prend la forme d’une 
demande de tirage versée au dépôt de la spécification; une extension officielle suit une filière distincte et 
exige au moins une implémentation de référence dans un SDK officiel[168, 169]. Selon les responsables du 
projet, on comptait en décembre 2025 environ 10 000 serveurs actifs et plus de 97 millions de téléchargements 
mensuels des SDK[14].
La spécification est versionnée par date : l’identifiant AAAA-MM-JJ correspond au dernier changement 
incompatible. Les révisions publiées sont 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25 et 2026-07-28, 
révision courante au 27 octobre 2026[34, 168, 189]. Cette dernière a été publiée le 28 juillet 2026, après une version 
candidate verrouillée le 21 mai 2026 et dix semaines de validation; les SDK TypeScript, Python, Go et C# la 
prenaient en charge dès sa sortie, le SDK Rust en version bêta[33, 194]. La feuille de route publiée le 22 août 
2026 n’annonce aucune date pour la prochaine révision. Elle donne priorité à la messagerie agentique, à un 
transport natif HTTP (y compris pour les serveurs locaux), à l’identité des agents et à la sécurité d’entreprise 
(DPoP, fédération d’identité de charge de travail, ID-JAG, échange de jetons), à un contrat unique pour les 
résultats de tools/call et à la découverte progressive des outils[195].
Le registre officiel MCP, lancé en préversion le 8 septembre 2025, l’est toujours selon sa documentation. 
Il n’héberge que des métadonnées qui renvoient aux paquets, authentifie les espaces de noms, délègue 
l’analyse de sécurité aux registres de paquets et ne prend pas en charge les serveurs privés; pour ceux-
ci, il recommande d’héberger son propre registre MCP privé[25, 43]. Le catalogue d’entreprise est donc un 
composant distinct, sous la responsabilité de l’entreprise (section 6.8 et section 11.4).
EXIG-MCP-01 · DOIT
Exposition des capacités par MCP, derrière la passerelle
Tout outil, toute ressource et toute invite mis à la disposition d’un agent DOIVENT l’être par un serveur 
MCP inscrit au catalogue d’entreprise et, dans tout environnement serveur, publié derrière la passerelle 
d’agents (sur un poste de développement, l’exécution locale par stdio obéit à l’EXIG-MCP-08). Un 
hôte ne se connecte jamais directement à un serveur de domaine. Un format d’appel propriétaire n’est 
toléré que derrière un adaptateur, conformément au statut « Contenir » du catalogue des protocoles 
(section 6.3).
Pourquoi : un contrat unique, appliqué en un seul point, permet de filtrer, de journaliser et de révoquer l’accès sans 
modifier les agents.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 54 sur 283


---
## [Page PDF 55]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
EXIG-MCP-02 · DOIT
Révision de référence vérifiée par la découverte
Tout serveur MCP mis en production après l’approbation du cadre DOIT mettre en œuvre la révision 
2026-07-28, y compris la méthode server/discover. La révision prise en charge par chaque serveur 
est inscrite et épinglée au catalogue; la passerelle la vérifie par server/discover, en contournant son 
propre cache (le résultat porte ttlMs et cacheScope), à l’homologation et à chaque déploiement, et 
refuse un serveur dont les versions ou capacités annoncées diffèrent de l’inscription.
Pourquoi : la spécification oblige tout serveur 2026-07-28 à implémenter server/discover, qui renvoie en une 
requête ses versions, ses capacités et son identité[168]; le catalogue dispose ainsi d’un relevé uniforme à comparer à 
l’inscription; ce relevé est déclaré par le serveur lui-même (serverInfo est auto-déclaré et ne devrait pas fonder une 
décision de sécurité) : il ne prouve ni l’identité ni l’intégrité du serveur.
Architecture hôte-client-serveur et primitives
MCP suit une architecture client-serveur à trois rôles. L’hôte est l’application d’IA  : un orchestrateur, 
un agent ou un poste de travail. Il crée un client MCP pour chaque serveur, et chaque client entretient 
une connexion dédiée[63]. Le protocole comporte deux couches : une couche de données, faite d’échanges 
JSON-RPC 2.0 (découverte, primitives, notifications), et une couche de transport, qui règle la connexion, le 
tramage et l’autorisation[63]. En 2026-07-28, l’identifiant d’une requête ne peut pas être nul et tout résultat 
porte un champ resultType [162].
Un serveur expose trois primitives : les outils, fonctions exécutables découvertes par tools/list et appelées 
par tools/call sous le contrôle du modèle; les ressources, données contextuelles identifiées par URI et 
lues par resources/list et resources/read; les invites, gabarits réutilisables obtenus par prompts/list 
et prompts/get [63, 64]. Côté client, l’élicitation, qui permet au serveur de demander une information ou 
une confirmation à la personne, demeure active; l’échantillonnage (Sampling) et les racines (Roots) sont 
dépréciés depuis 2026-07-28[196].
Dans l’entreprise, la passerelle d’agents s’insère entre les hôtes et les serveurs (figure 7). Elle agit en manda­
taire inverse et applique à chaque requête les contrôles décrits à la section 9.4. Elle peut publier chaque 
serveur sous son propre point d’accès ou en agréger plusieurs derrière un point d’accès virtuel. Dans ce 
second cas, elle préfixe les noms d’outils par un identifiant de serveur : la spécification signale le risque de 
collision de noms et précise que le nom annoncé dans serverInfo n’est pas garanti unique[197].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 55 sur 283


---
## [Page PDF 56]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Hôte MCP
agent, orchestrateur ou poste
Client MCP no 1
→ serveur CRM
Client MCP no 2
→ serveur ERP
Client MCP no 3
→ serveur GED
Un client par serveur;
l’hôte applique le consentement,
l’approbation et les délais.
Streamable
HTTP + TLS
Passerelle d’agents
• valide le jeton (audience)
• compare en-têtes et corps
Mcp-Method, Mcp-Name
• filtre tools/list selon
les portées du jeton
• applique paliers P0–P3
• cache selon cacheScope
• ignore _meta non reconnu
• propage traceparent
• bloque tout serveur
absent du catalogue
• journalise chaque appel
Serveur MCP de domaine
Outils
tools/call
Ressources
resources/read
Invites
prompts/get
Découverte : server/discover
Contrats : JSON Schema 2020-12
Erreurs métier : isError: true
État explicite par identifiant revalidé
Interaction humaine : MRTR
InputRequiredResult → elicitation
Extensions (activation explicite) :
tasks · apps · auth (EMA)
API OpenAPI, bases de données, SaaS, ERP, CRM
Requête 2026-07-28 : autonome, sans session
POST /mcp · MCP-Protocol-Version: 2026-07-28 · Mcp-Method: tools/call · Mcp-Name: erp_creer_bon
Authorization: Bearer <jeton émis pour ce serveur>
{"method":"tools/call","params":{"name":"erp_creer_bon","arguments":{…},
"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","traceparent":"00-…"}}}
Figure 7 — MCP 2026-07-28 derrière la passerelle d’agents. L’hôte crée un client par serveur; chaque requête, autonome et sans 
session, traverse la passerelle, qui vérifie le jeton, la concordance des en-têtes et du corps, le palier de l’outil et le catalogue avant de 
joindre le serveur de domaine. La requête illustrée est abrégée : une requête complète porte aussi les capacités du client dans _meta. 
Source : cadre CRE-IA-2026-01, d’après la spécification MCP 2026-07-28[198].
Requête tools/call conforme à la révision 2026-07-28 (extrait)
{"jsonrpc": "2.0", "id": 42, "method": "tools/call",
 "params": {
   "name": "approvisionnement_creer_bon_commande",
   "arguments": {"idempotency_key": "…", "centre_cout": "CC-4410", "…": "…"},
   "_meta": {
     "io.modelcontextprotocol/protocolVersion": "2026-07-28",
     "io.modelcontextprotocol/clientCapabilities": {"…": "…"},
     "traceparent": "00-…-…-01"}}}
POST /mcp HTTP/1.1
Host: passerelle-agents.interne.exemple
Content-Type: application/json
Accept: application/json, text/event-stream
Authorization: Bearer <jeton émis pour ce serveur seulement>
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: approvisionnement_creer_bon_commande
Mcp-Param-Cost-Center: CC-4410
Quatre traits ressortent. La requête se suffit à elle-même  : aucun identifiant de session. Les en-têtes 
Mcp-Method et Mcp-Name recopient le corps pour permettre le routage sans l’analyser, d’où l’obligation de 
vérifier leur concordance (EXIG-MCP-15). Le jeton n’est valable que pour ce serveur (EXIG-MCP-11). Enfin, 
l’en-tête Mcp-Param-Cost-Center provient d’un argument marqué x-mcp-header; un centre de coûts s’y 
prête, une donnée sensible jamais (EXIG-MCP-18).
À RETENIR
Un serveur MCP est un adaptateur sans état cognitif : il expose des capacités à entrées et sorties définies 
et ne conduit pas la boucle de raisonnement de l’agent appelant. Le modèle propose d’utiliser un outil; 
la passerelle et le catalogue décident si l’appel est permis, à quelles conditions et sous quel jeton.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 56 sur 283


---
## [Page PDF 57]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Ce qui change avec la révision 2026-07-28
La révision 2026-07-28 rend le protocole sans état. Pour l’exploitation, c’est une simplification : tout nœud 
d’un parc peut traiter n’importe quelle requête, sans affinité de session, y compris sur une plateforme sans 
serveur[162, 168]. Pour la sécurité, le risque se déplace des sessions vers les identifiants d’état applicatifs et les 
nouveaux en-têtes. Le tableau 17 résume les changements et leur effet pour l’entreprise.
Tableau 17 — Principaux changements de la révision MCP 2026-07-28 et effet pour l’entreprise
Changement
Effet pour l’entreprise
Protocole sans état. Retrait de la poignée de main initialize, des sessions 
protocolaires et de l’en-tête Mcp-Session-Id (SEP-2567, SEP-2575); chaque requête 
porte dans _meta sa version de protocole et les capacités du client[162, 168].
Plus de répartiteurs de charge à sessions 
persistantes (sticky sessions) ni de magasin 
de sessions partagé. L’état qui doit durer 
passe par un identifiant explicite émis par le 
serveur (EXIG-MCP-17).
Découverte. Méthode server/discover, obligatoire pour le serveur, facultative 
pour le client : versions prises en charge, capacités (extensions comprises) et iden­
tité, dans une réponse que l’on peut mettre en cache (ttlMs et cacheScope)[168, 199].
Sonde d’inventaire et d’homologation; 
contrôle de cohérence avec le catalogue 
(EXIG-MCP-02).
En-têtes de routage. Chaque POST porte Mcp-Method et, pour tools/call, 
resources/read et prompts/get, Mcp-Name (SEP-2243); MCP-Protocol-Version doit 
égaler la valeur de _meta; tout écart entraîne HTTP 400 et l’erreur −32020 
(HeaderMismatch) [168, 190].
Routage et politiques possibles sans analy­
ser le corps, à la condition expresse de véri­
fier la concordance (EXIG-MCP-15).
Requêtes à allers-retours multiples (MRTR, SEP-2322). Les requêtes initiées 
par le serveur (roots/list, sampling/createMessage, elicitation/create) cèdent 
la place à un résultat InputRequiredResult; le client relance la requête d’origine 
avec les réponses et un requestState opaque. MRTR s’applique à tools/call, 
resources/read et prompts/get [200].
Une précision ou une décision humaine 
s’obtient sans flux ouvert de longue durée; 
le requestState devient une entrée non 
fiable à protéger (EXIG-MCP-17).
Indices de cache. ttlMs et cacheScope obligatoires sur les résultats com­
plets de tools/list, prompts/list, resources/list, resources/templates/list, 
resources/read (SEP-2549) et server/discover [168, 201].
Cache de passerelle possible; un cache 
« private » n’est jamais partagé entre jetons 
(EXIG-MCP-03).
Abonnements. subscriptions/listen remplace le point d’accès GET et 
resources/subscribe; la reprise de flux par Last-Event-ID est retirée[168, 190].
Notifications limitées aux types demandés 
par le client; les méthodes GET et DELETE ne 
servent plus.
Extensions officielles. Selon le journal des modifications de la révision 
2026-07-28, les tâches longues quittent le cœur pour l’extension officielle 
io.modelcontextprotocol/tasks (SEP-2663); MCP Apps est une extension officielle; 
toute extension est désactivée par défaut et s’active explicitement des deux 
côtés[168, 169, 191, 202].
Liste d’extensions autorisées au catalogue, 
quotas pour les tâches, revue des interfaces 
(EXIG-MCP-04).
Schémas. inputSchema et outputSchema acceptent tout mot-clé de JSON Schema 
2020-12 (SEP-2106), dialecte par défaut; un autre dialecte peut être déclaré par 
$schema [168, 197, 201].
Contrats plus expressifs; validateurs à durcir 
contre les références réseau (EXIG-MCP-19).
Cycle de vie. États Active, Deprecated et Removed (SEP-2596) : une fonctionnalité 
dépréciée reste dans la spécification au moins douze mois, ou au moins 90 jours 
en cas de retrait accéléré exceptionnel[34, 196].
Migrations planifiées au catalogue, avec 
échéances (EXIG-MCP-22).
Dépréciations et retraits. Sont dépréciés Roots, Sampling, la journalisation 
protocolaire, l’enregistrement dynamique de clients (DCR), l’ancien transport 
HTTP+SSE et les valeurs includeContext « thisServer » et « allServers »; ping, 
logging/setLevel et notifications/roots/list_changed sont retirés. Le retrait de 
Roots, de Sampling, de la journalisation et du DCR est possible à partir de la 
première révision publiée le 28 juillet 2027 ou après (celui d’includeContext suit 
Sampling; celui du transport HTTP+SSE, trois mois après que la SEP-2596 atteint 
l’état final)[168, 196].
Paramètres d’outil ou URI de ressource au 
lieu de Roots; appels aux modèles par la 
passerelle de modèles au lieu de Sampling; 
sortie d’erreur standard ou OpenTelemetry 
au lieu de la journalisation protocolaire.
Codes d’erreur. « Ressource introuvable » passe de −32002 à −32602; la plage 
−32020 à −32099 est réservée à MCP, dont −32021 (capacité client requise 
absente) et −32022 (version non prise en charge)[162, 168].
Clients tolérants aux deux codes pendant la 
transition; supervision des nouveaux codes.
Une liste d’outils peut varier selon l’autorisation présentée, par exemple pour ne montrer que les outils 
permis par les portées du jeton, mais jamais selon la connexion ni par effet de bord d’autres requêtes; une 
liste qui dépend du jeton devrait alors porter cacheScope « private »[197, 199].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 57 sur 283


---
## [Page PDF 58]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
EXIG-MCP-03 · DOIT
Listes stables et cache conforme à cacheScope
Les serveurs MCP internes DOIVENT renvoyer leurs outils dans un ordre déterministe, identique d’une 
requête à l’autre tant que l’ensemble ne change pas. La passerelle DOIT respecter ttlMs et cacheScope : 
sa clé de cache inclut la méthode et les paramètres de la requête (curseur, URI) et, pour une réponse 
« private », le contexte d’autorisation; une réponse « private » n’est servie qu’à ce même contexte; 
seule une réponse « public » peut l’être par un cache partagé, ce qui ne dispense pas des contrôles 
d’accès par primitive; un résultat intermédiaire input_required et le résultat d’une relance MRTR 
(inputResponses ou requestState) ne sont jamais mis en cache.
Pourquoi : la spécification recommande l’ordre déterministe pour améliorer le taux de succès du cache d’invites, 
et le cadre l’exige pour ses serveurs (section 10.6); elle interdit de partager un cache « private » entre contextes 
d’autorisation, ce qui réduit le risque de fuite entre locataires (la spécification précise que cacheScope ne remplace 
pas les contrôles d’accès propres à chaque primitive)[197, 199, 201].
L’extension Tasks confie un travail long à un identifiant durable : le serveur renvoie un taskId, une durée 
de vie et un intervalle d’interrogation; le client suit l’avancement par tasks/get, fournit une entrée par 
tasks/update et peut annuler par tasks/cancel; les états sont working, input_required, completed, 
failed et cancelled [191]. Une tâche MCP ne remplace pas l’exécution durable de l’orchestrateur : celui-
ci consigne le taskId dans son point de contrôle pour reprendre le suivi après une panne (section 7.4). 
Avec MCP Apps, un outil désigne dans _meta.ui.resourceUri une ressource ui://; l’hôte l’affiche dans 
une iframe cloisonnée qu’il contrôle, l’application ne dialogue avec lui que par postMessage et n’appelle 
des outils qu’à travers lui, et _meta.ui.csp et _meta.ui.permissions encadrent les origines et les permis­
sions[202].
EXIG-MCP-04 · DOIT
Extensions activées sur liste d’autorisation
Une extension MCP DOIT figurer au catalogue pour le serveur concerné avant d’être activée. Les 
extensions internes portent le préfixe DNS inversé de l’entreprise, jamais un préfixe réservé (dont le 
deuxième libellé est modelcontextprotocol ou mcp). Pour l’extension Tasks, la passerelle impose un 
quota de tâches actives par mandant et une durée de vie maximale. Pour MCP Apps, chaque gabarit 
ui:// est revu avant l’homologation, servi sous une politique de sécurité du contenu restrictive, et le 
contenu généré qu’il affiche est encodé.
Pourquoi : les extensions sont désactivées par défaut et s’identifient par un préfixe DNS inversé[169]; Akamai signale le 
déni de service par tâches asynchrones et le script intersites stocké par les interfaces générées[203]. La revue préalable 
des gabarits est une exigence du cadre, que la documentation officielle n’énonce pas.
Règles d’usage des primitives
Chaque primitive répond à un besoin distinct. Une ressource convient quand on sait quelle entité charger : 
crm://comptes/9482/sommaire se lit sans effet sur le système et se met en cache selon ttlMs. Un outil 
convient aux recherches dynamiques, aux calculs et aux écritures, sous un contrat d’entrée strict. Une invite 
publie une procédure normalisée d’un domaine, par exemple la vérification d’un nouveau fournisseur, pour 
que chaque agent n’ait pas à la réécrire; elle se gère comme la mémoire procédurale, c’est-à-dire comme du 
code versionné et revu (section 5.5).
La granularité compte autant que le choix de la primitive. Un serveur qui recopie une API de soixante 
opérations en soixante outils encombre le contexte du modèle et multiplie les occasions de choisir le mauvais 
outil ou le mauvais paramètre. Un outil approvisionnement_creer_bon_commande, qui valide en une seule 
opération le fournisseur, le centre de coûts et les lignes, se gouverne mieux et se teste plus facilement. 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 58 sur 283


---
## [Page PDF 59]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Les équipes ne réécrivent pas leurs services REST : des adaptateurs déclaratifs traduisent les opérations 
OpenAPI pertinentes en outils orientés tâche (section 5.2).
Lorsque les outils deviennent nombreux, les bonnes pratiques de MCP recommandent à l’hôte, au-delà d’un 
seuil de l’ordre de 1 à 5 % de la fenêtre de contexte, d’offrir un méta-outil de recherche et de ne charger 
les définitions complètes qu’au besoin, en les ajoutant après le point de rupture du cache plutôt qu’en 
réordonnant la liste[204]. Anthropic illustre, par un exemple de plus de 50 outils MCP, que sa propre fonction 
de recherche d’outils ramène la consommation totale de contexte d’environ 77 000 à environ 8 700 jetons 
(dont environ 72 000 pour les seules définitions); elle chiffre cette réduction à 85 % (les deux chiffres donnent 
plutôt près de 89 %)[205]. Le choix entre la recherche d’outils et le découpage en plusieurs agents est traité à 
la section 7.3.
EXIG-MCP-05 · DEVRAIT
Choix de la primitive selon le besoin
La lecture d’une entité connue DEVRAIT être exposée comme ressource adressée par URI; une 
recherche, un calcul ou une écriture, comme outil; une procédure normalisée de domaine, comme invite 
versionnée et revue au même titre que du code.
Pourquoi : la ressource se lit sans effet et se met en cache; l’outil porte un contrat d’entrée strict et passe par les 
contrôles de palier; l’invite rend une procédure réutilisable sans la recopier dans chaque agent.
EXIG-MCP-06 · NE DOIT PAS
Aucun miroir CRUD des API
Un serveur MCP NE DOIT PAS exposer une API en recopiant une à une ses opérations élémentaires de 
création, de lecture, de mise à jour et de suppression. Il expose des outils qui accomplissent des tâches 
métier complètes et valident eux-mêmes leurs paramètres.
Pourquoi : chaque définition d’outil consomme du contexte et chaque outil de plus est une occasion d’erreur de 
sélection; une intention métier se classe au catalogue et s’approuve plus clairement qu’une opération technique.
EXIG-MCP-07 · DOIT
Conventions de nommage et de résultat des outils
Les outils des serveurs internes DOIVENT : porter un nom de 1 à 128 caractères ASCII (lettres, chiffres, 
_, -, .) préfixé par leur domaine; renvoyer les erreurs de validation et les erreurs métier comme résultat 
d’outil marqué isError: true, en réservant les erreurs JSON-RPC aux outils inconnus, aux requêtes 
malformées et aux erreurs du serveur; déclarer un outputSchema lorsque leur résultat alimente une 
étape suivante, puis renvoyer un structuredContent conforme, accompagné du même JSON sérialisé 
dans un bloc texte.
Pourquoi : le modèle peut corriger une erreur renvoyée comme résultat, alors qu’une erreur de protocole interrompt 
l’appel; la spécification exige un structuredContent conforme dès qu’un outputSchema est déclaré et recommande 
le bloc texte pour la rétrocompatibilité[197]. Exemple complet à l’annexe C.
Transport et autorisation
MCP définit deux transports normalisés : stdio, entre processus d’une même machine, et Streamable HTTP, 
qui a remplacé le transport HTTP+SSE en 2025-03-26[206, 207]. En 2026-07-28, chaque message du client est 
un POST distinct vers un point d’accès unique; le serveur répond soit par un objet JSON, soit par un flux 
SSE propre à cette requête (que le serveur devrait clore dès que la réponse JSON-RPC finale est envoyée), et 
le client doit accepter les deux. Le serveur doit valider l’en-tête Origin sur toute connexion entrante pour 
contrer le détournement DNS, et répondre par HTTP 403 si l’en-tête est présent et invalide; un serveur 
local devrait n’écouter que sur 127.0.0.1, et tout serveur devrait authentifier les connexions[190]. Les bonnes 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 59 sur 283


---
## [Page PDF 60]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
pratiques de sécurité de MCP recommandent d’ailleurs stdio pour limiter l’accès à un serveur local[208] : 
restreindre stdio au poste de développement est donc un choix d’exploitation du cadre, non une exigence 
de MCP.
EXIG-MCP-08 · DOIT
Transport selon l’environnement
Dans tout environnement serveur (développement partagé, préproduction, production), un serveur 
MCP DOIT être exposé par Streamable HTTP, chiffré par TLS 1.3 (TLS 1.2 toléré comme plancher, 
versions antérieures désactivées), derrière la passerelle d’agents. Le transport stdio n’est permis que 
sur le poste d’un développeur, pour un serveur installé depuis le catalogue et exécuté dans un bac à 
sable aux privilèges minimaux; l’hôte affiche la commande complète avant l’installation et exige une 
approbation explicite.
Pourquoi : seul un transport réseau passe par la passerelle, donc par l’identité, la politique et la journalisation; les 
bonnes pratiques de sécurité de MCP exigent l’affichage de la commande et l’approbation explicite pour l’installation 
en un clic d’un serveur local, et recommandent son exécution en bac à sable[208].
L’autorisation est facultative dans MCP; lorsqu’elle est offerte sur HTTP, elle devrait suivre la spécification 
d’autorisation, fondée sur le brouillon OAuth 2.1 dans sa version −13 (la version −16 est la plus récente au 
27 octobre 2026; voir la section 6.3), que la spécification MCP cite encore (la version −16 est la plus récente 
au 27 octobre 2026; voir la section 6.3)[209, 210]. Le serveur MCP y est un serveur de ressources OAuth. Il doit 
publier ses métadonnées de ressource protégée (RFC 9728), que le client utilise pour découvrir le serveur 
d’autorisation, et ce dernier doit offrir la découverte RFC 8414 ou OpenID Connect[211]. Le client doit inclure 
le paramètre resource (RFC 8707), valant l’URI canonique du serveur MCP, dans ses requêtes d’autorisation 
et de jeton; le serveur doit vérifier que le jeton lui est destiné et répondre 401 sinon[71]. Le jeton circule dans 
l’en-tête Authorization: Bearer de chaque requête, jamais dans l’URL; PKCE s’emploie avec la méthode 
S256. Depuis 2026-07-28, le serveur d’autorisation devrait renvoyer le paramètre iss (RFC 9207), que le 
client doit valider s’il est présent (et rejeter la réponse s’il est absent alors que les métadonnées annoncent 
son support)[209, 212]. Comme OAuth 2.1 reste un brouillon, le cadre se réfère à OAuth 2.0 profilé par la RFC 
9700 (section 9.3).
La spécification prescrit des jetons porteurs; elle n’exige ni mTLS ni DPoP, ni durée de vie précise, et la 
finalisation de DPoP ne figure qu’à sa feuille de route[195, 209]. Les jetons contraints à l’émetteur (RFC 9449 
ou RFC 8705), appuyés sur la RFC 9700[175, 213], et les durées de vie courtes sont donc des politiques du cadre. 
Lorsque la passerelle publie un serveur, l’URI canonique annoncée aux clients est la sienne; elle obtient 
ensuite, pour le serveur de domaine, un jeton distinct par échange de jetons (section 9.3). Ce choix du cadre 
respecte l’interdiction du passage de jeton.
EXIG-MCP-09 · DOIT
Autorisation obligatoire et conforme à la spécification
Tout serveur MCP accessible ailleurs que sur un poste de développement DOIT exiger une autorisation 
OAuth conforme à la spécification MCP 2026-07-28 : métadonnées de ressource protégée (RFC 9728), 
indicateur de ressource (RFC 8707) portant l’URI canonique, vérification de l’audience à chaque requête 
et jeton transmis uniquement par l’en-tête Authorization. Les clients MCP de l’entreprise DOIVENT 
employer PKCE avec S256 (en vérifiant que les métadonnées du serveur d’autorisation annoncent 
code_challenge_methods_supported et en refusant de poursuivre sinon) et valider iss (RFC 9207) 
avant d’échanger le code d’autorisation. Les serveurs d’autorisation de l’entreprise DOIVENT publier 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 60 sur 283


---
## [Page PDF 61]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
ces annonces et toujours émettre iss (avec authorization_response_iss_parameter_supported: 
true).
Pourquoi : la spécification laisse l’autorisation facultative[209]; le cadre la rend obligatoire, car un outil sans contrôle 
d’accès ouvre directement les systèmes d’enregistrement, et l’émission de iss protège contre la confusion entre 
serveurs d’autorisation.
EXIG-MCP-10 · DOIT
Portées minimales et élévation progressive
Chaque serveur MCP DOIT publier un ensemble initial minimal de portées (scopes_supported), 
refuser les portées génériques (*, all, full-access) et signaler une portée insuffisante par une réponse 
403 insufficient_scope qui énumère les portées requises. Chaque élévation progressive (step-up) est 
journalisée avec l’identifiant de trace, et le client en limite le nombre de tentatives.
Pourquoi : un agent démarre avec le minimum et n’obtient davantage que sur une demande traçable; c’est le patron 
de minimisation des portées que décrivent la spécification et ses bonnes pratiques de sécurité[208, 209].
EXIG-MCP-11 · NE DOIT PAS
Interdiction du passage de jeton
Un serveur MCP, la passerelle comprise, NE DOIT PAS accepter un jeton qui n’a pas été émis pour lui, 
ni retransmettre en aval un jeton reçu. Pour appeler une API ou un autre serveur, il obtient son propre 
jeton, à audience unique, par échange de jetons (section 9.3).
Pourquoi : la spécification interdit explicitement le passage de jeton (token passthrough)[208, 209]; un jeton relayé 
permettrait à un serveur compromis d’agir partout où ce jeton est valable.
Pour identifier un client, la spécification recommande l’ordre suivant  : enregistrement préalable, puis 
document de métadonnées d’identifiant client (CIMD) si le serveur d’autorisation l’annonce, puis enregis­
trement dynamique (DCR) en repli, puis saisie manuelle[214]. Les CIMD, dont l’identifiant client est une 
URL HTTPS, ont été ajoutés en 2025-11-25; le DCR (RFC 7591) a été déprécié en 2026-07-28[168, 215]. Le 
brouillon CIMD, adopté par le groupe de travail OAuth de l’IETF mais qui n’est pas une RFC, interdit au 
client l’authentification par secret partagé, n’admet que des clés publiques, interdit au serveur de suivre 
automatiquement les redirections, lui fait refuser les adresses à usage spécial et recommande de limiter la 
lecture à environ 5 Ko (état de la version −02; la spécification MCP 2026-07-28 renvoie à la version −00)[216]. 
Un identifiant préenregistré ou obtenu par DCR est lié à l’émetteur qui l’a délivré : si l’émetteur change, le 
client se réenregistre[214].
EXIG-MCP-12 · DOIT
Enregistrement des clients MCP
Les clients MCP de l’entreprise DOIVENT être préenregistrés auprès du serveur d’autorisation ou, 
pour un serveur tiers qui l’annonce, identifiés par un CIMD. Le DCR NE DOIT PAS être activé pour 
une nouvelle intégration. Un serveur d’autorisation de l’entreprise qui accepte des CIMD DOIT refuser 
l’authentification par secret partagé, ne pas suivre les redirections, bloquer les adresses à usage spécial 
et borner la taille du document lu.
Pourquoi : le DCR est déprécié et voué au retrait[196]; la récupération d’un CIMD expose le serveur d’autorisation à 
la falsification de requêtes côté serveur (SSRF), que les règles du brouillon préviennent[216].
EXIG-MCP-13 · DOIT
Consentement par client des mandataires MCP
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 61 sur 283


---
## [Page PDF 62]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Un serveur MCP qui sert de mandataire auprès d’un serveur d’autorisation tiers avec un identifiant 
client statique DOIT obtenir le consentement de l’utilisateur pour chaque client avant de relayer 
l’autorisation : registre des client_id approuvés par utilisateur; page de consentement qui nomme 
le client, les portées et l’URI de redirection; protection contre la falsification de requête intersites 
et contre le détournement de clic par incrustation (clickjacking), notamment par frame-ancestors; 
correspondance exacte de redirect_uri; paramètre state aléatoire, à usage unique, fixé seulement 
après le consentement; témoins __Host- marqués Secure, HttpOnly et SameSite=Lax.
Pourquoi  : sans ce consentement, un client malveillant profite d’un consentement donné antérieurement au 
mandataire; c’est le problème de l’adjoint confus (confused deputy), que la spécification traite par ces mesures 
obligatoires[208].
Deux extensions officielles d’autorisation, stables depuis la révision 2026-07-28, complètent le cœur du 
protocole[217]. Avec Enterprise-Managed Authorization (EMA), le fournisseur d’identité de l’entreprise 
décide de l’accès : après l’authentification unique, le client obtient un ID-JAG par échange de jetons (RFC 
8693), puis l’échange contre un jeton d’accès par l’octroi JWT bearer (RFC 7523)[178, 218]. EMA évite un 
consentement par serveur et par employé et centralise les politiques d’accès et la révocation[178]; comme le 
brouillon ID-JAG qui la fonde[177], elle figure au statut « Évaluer » du catalogue (section 6.3). L’extension 
OAuth Client Credentials couvre les agents qui agissent sans utilisateur; un tel agent s’authentifie sous sa 
propre identité (section 9.2). Enfin, l’échange de jetons RFC 8693 et la revendication act ne font pas partie 
du cœur de MCP : exiger d’un fournisseur la propagation de la chaîne de délégation relève d’une clause 
contractuelle (chapitre 13), non d’une conformité MCP.
Annotations et métadonnées de gouvernance
La spécification prévoit pour chaque outil des annotations  : title, readOnlyHint (faux par défaut), 
destructiveHint (vrai par défaut), idempotentHint (faux par défaut) et openWorldHint (vrai par défaut); 
destructiveHint et idempotentHint n’ont de sens que si l’outil n’est pas en lecture seule. Ce sont des 
indices : les clients doivent les tenir pour non fiables, sauf s’ils proviennent de serveurs de confiance, et, 
selon une formulation non normative (« should never »), ne jamais fonder une décision d’usage sur les 
annotations d’un serveur non fiable[197, 201]. Les valeurs par défaut sont prudentes : un outil qui ne déclare 
rien est présumé destructif et ouvert sur l’extérieur.
L’objet annotations ne définit que cinq champs standard et aucune propriété d’extension; la spécification 
réserve _meta aux extensions. Les ébauches qui y ajoutaient des champs x-enterprise-* sortaient donc 
de ce que prévoit la spécification (le cadre en fait une règle, EXIG-MCP-14)[201]. Une métadonnée propre 
à l’entreprise peut figurer dans le champ _meta de l’outil, sous une clé à préfixe DNS inversé détenu par 
l’entreprise (p. ex. ca.exemple/palier-risque); déclarée par le serveur, elle n’est pas plus fiable qu’une 
annotation.
ATTENTION
Une annotation readOnlyHint: true ne prouve rien  : c’est le serveur qui l’affirme. Un serveur 
compromis ou mal configuré peut déclarer en lecture seule un outil qui supprime des données. Le palier 
P0 à P3 d’un outil est attribué au catalogue après revue (section 8.3) et appliqué par la passerelle.
EXIG-MCP-14 · DOIT
Annotations et métadonnées déclarées : de simples indices
La passerelle et les hôtes DOIVENT lire le palier de risque, le seuil d’approbation et l’outil de 
compensation d’un outil dans son entrée au catalogue, jamais dans ses annotations ni dans son _meta. 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 62 sur 283
