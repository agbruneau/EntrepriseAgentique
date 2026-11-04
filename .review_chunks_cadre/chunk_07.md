# chunk_07 — pages PDF 61 à 72 (sur 283)



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


---
## [Page PDF 63]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Les serveurs internes DOIVENT néanmoins déclarer leurs annotations, qui DOIVENT concorder 
avec la classification du catalogue; un écart DOIT bloquer l’homologation. Aucune propriété propre à 
l’entreprise n’est ajoutée à l’objet annotations.
Pourquoi : la spécification tient les annotations pour des indices non fiables[197]; elles servent l’ergonomie (affichage, 
demande de confirmation), non la décision de sécurité. L’entrée de catalogue type figure à l’annexe C.
Sécurité propre à MCP
Le passage au protocole sans état supprime le détournement d’identifiant de session, mais déplace le risque 
vers les identifiants d’état applicatifs et le requestState, que le serveur doit traiter comme une entrée 
contrôlée par l’attaquant[200, 208]. L’analyse de la version candidate publiée par Akamai le 25 juin 2026 relève 
notamment le détournement de flux entre agents par des identifiants ou des objets d’état prévisibles, la 
manipulation du champ _meta contrôlé par le client, la désynchronisation des en-têtes et du corps, la fuite 
de données par x-mcp-header, le script intersites stocké par MCP Apps et le déni de service par tâches 
asynchrones[203]. La spécification contient déjà l’essentiel des contre-mesures; les exigences qui suivent s’y 
appuient. Les menaces communes à tous les agents, comme l’injection d’instructions et l’exécution de code, 
sont traitées aux sections 9.5 à 9.7.
EXEMPLE : LA DÉSYNCHRONISATION
Une requête porte l’en-tête Mcp-Name: recherche_publique, mais son corps appelle supprimer_base. 
Un pare-feu applicatif qui ne lit que l’en-tête laisse passer, et le serveur exécute l’outil destructeur. La 
spécification ferme cette brèche en obligeant tout serveur qui traite le corps à rejeter l’écart; le cadre 
ajoute que la passerelle décide d’après le corps analysé, jamais d’après les seuls en-têtes.
EXIG-MCP-15 · DOIT
Concordance des en-têtes et du corps
La passerelle et chaque serveur DOIVENT vérifier que MCP-Protocol-Version, Mcp-Method, Mcp-Name 
et chaque en-tête Mcp-Param-{nom} (après décodage Base64 éventuel) concordent avec le corps 
JSON-RPC et sa clé _meta, et rejeter toute divergence ou tout en-tête obligatoire absent par HTTP 400 
et l’erreur −32020. La passerelle fonde ses décisions d’autorisation sur le corps analysé; une politique 
fondée sur les en-têtes ne s’applique qu’aux requêtes de la révision 2026-07-28.
Pourquoi : la spécification impose ce rejet à tout serveur qui traite le corps et recommande à un intermédiaire 
dont la politique repose sur ces en-têtes de rejeter les requêtes d’une révision antérieure, qui n’imposait pas cette 
validation[190].
Dans MCP, le code HTTP 403 signale un en-tête Origin invalide (transport) ou des portées invalides 
ou des permissions insuffisantes (autorisation); une divergence d’en-têtes relève du code 400[190, 209]. Le 
champ _meta, lui, ne peut pas être purgé en bloc : les clés io.modelcontextprotocol/protocolVersion 
et io.modelcontextprotocol/clientCapabilities y sont obligatoires, sous peine de rejet par l’erreur −32602, et 
les clés traceparent, tracestate et baggage y transportent le contexte de trace selon W3C Trace Context 
et W3C Baggage (SEP-414)[162, 168]. Les conventions OpenTelemetry pour MCP, au niveau Development, 
nomment les spans d’après la méthode appelée (attribut mcp.method.name)[219]; leur emploi est réglé à la 
section 10.1. Un serveur ne se fie pas non plus à une capacité que le client n’a pas déclarée : il renvoie alors 
l’erreur −32021[162].
EXIG-MCP-16 · DOIT
Traitement du champ _meta
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 63 sur 283


---
## [Page PDF 64]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
La passerelle et les serveurs DOIVENT conserver les clés réservées de _meta (protocole, capacités du 
client, contexte de trace), ignorer ou filtrer les clés non reconnues et ne fonder aucun routage, aucun 
choix de locataire ni aucune autorisation sur _meta, clientInfo ou serverInfo. L’identité du mandant 
provient exclusivement du jeton vérifié, par exemple de sa revendication sub.
Pourquoi : clientInfo et serverInfo sont auto-déclarés et ne devraient pas servir aux décisions de sécurité[162]; 
Akamai illustre l’élévation de privilèges qu’obtient un attaquant lorsqu’un serveur se fie à {"tenant": "admin", 
"authenticated": true} placé dans _meta [203].
EXIG-MCP-17 · DOIT
État explicite protégé
Un serveur qui conserve un état entre deux appels DOIT émettre des identifiants d’état aléatoires, 
imprévisibles et à durée de vie bornée, liés côté serveur à l’utilisateur authentifié (clé de la forme 
utilisateur:identifiant, l’utilisateur étant tiré du jeton vérifié); la possession d’un identifiant ne 
vaut jamais authentification. Il DOIT traiter tout requestState reçu comme une entrée contrôlée par 
un attaquant et, dès que cet état influence l’autorisation, l’accès aux ressources ou la logique métier, en 
protéger l’intégrité par HMAC ou par chiffrement authentifié (AEAD), y inclure le mandant, une courte 
durée de vie et l’empreinte de la requête d’origine, et en garantir l’usage unique lorsque l’étape l’exige.
Pourquoi : la spécification impose de traiter tout requestState comme une entrée contrôlée par un attaquant, d’en 
protéger l’intégrité (HMAC ou AEAD) dès qu’il influence l’autorisation, l’accès aux ressources ou la logique métier, 
et de faire respecter l’usage unique côté serveur quand il est requis; elle ne fait que recommander l’inclusion du 
mandant, d’une courte durée de vie et de l’empreinte de la requête d’origine, et n’offre qu’une orientation non 
normative sur les identifiants d’état aléatoires liés à l’utilisateur (durcissement du cadre)[197, 200]; sans elles, un 
identifiant deviné permet d’accéder à l’état d’un autre utilisateur, et un état rejoué par un autre mandant n’est rejeté 
que si le serveur l’a lié au mandant[200, 208].
La directive x-mcp-header recopie un argument d’outil dans un en-tête Mcp-Param-{nom}. Elle ne s’applique 
qu’à des types primitifs (chaîne, entier, booléen, à l’exclusion de number), à une propriété atteignable 
statiquement et sous un nom unique; un client Streamable HTTP doit écarter de tools/list tout outil dont 
la directive est invalide[190, 197].
EXIG-MCP-18 · NE DOIT PAS
Aucune donnée sensible en en-tête
La directive x-mcp-header NE DOIT PAS marquer une propriété qui contient un secret (mot de passe, 
clé d’API, jeton), un renseignement personnel ou toute autre donnée confidentielle. Elle est réservée aux 
valeurs utiles au routage ou à l’imputation, comme un centre de coûts; les schémas d’outils DOIVENT 
être analysés en intégration continue pour le vérifier.
Pourquoi : les en-têtes sont visibles des intermédiaires (répartiteurs de charge, passerelles, outils d’observabilité); la 
spécification recommande de ne pas y marquer de paramètres sensibles[190, 197], et le cadre en fait une interdiction.
EXIG-MCP-19 · DOIT
Schémas, URL et icônes : des entrées non fiables
Les hôtes, les clients hébergés et la passerelle DOIVENT traiter comme non fiables les schémas, URL 
et icônes fournis par un serveur. Concrètement : ne jamais déréférencer automatiquement un $ref 
pointant vers une URI réseau et borner la profondeur et le nombre de sous-schémas; lors de la décou­
verte OAuth, n’accepter que HTTPS, bloquer les plages d’adresses privées, de bouclage et lien-local, 
valider chaque redirection et passer par un mandataire de sortie; n’ouvrir une URL d’autorisation que si 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 64 sur 283


---
## [Page PDF 65]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
son schéma est https (http en bouclage, pour le développement seulement), jamais par un interpréteur 
de commandes; n’accepter une icône qu’en https ou data:, de même origine que le serveur, récupérée 
sans identifiants et dont le type est validé par signature binaire.
Pourquoi : un serveur malveillant peut se servir d’un schéma pour un déni de service, de la découverte OAuth pour 
une SSRF vers les métadonnées infonuagiques ou les services internes, d’une URL ou d’une icône SVG pour exécuter 
du code[162, 208].
Trois attaques visent les définitions d’outils elles-mêmes. L’empoisonnement d’outil (tool poisoning) 
cache des instructions malveillantes dans une description, un schéma ou une valeur de retour. La substi­
tution après approbation (rug pull) modifie les définitions d’un serveur une fois celui-ci approuvé. 
L’ombrage (tool shadowing) laisse la description d’un serveur malveillant modifier l’usage des outils d’un 
autre serveur. Invariant Labs a décrit les trois le 1er avril 2025, et la fiche de sécurité MCP de l’OWASP 
les reprend avec l’injection par valeurs de retour[220, 221]. Cette fiche recommande de traiter chaque serveur 
comme un domaine de sécurité indépendant et non fiable, et rappelle que la signature des messages ne fait 
pas partie du cœur de MCP[221]. L’épinglage au catalogue est réglé à la section 6.8; l’exigence suivante en 
assure l’application à l’exécution.
EXIG-MCP-20 · DOIT
Empreintes des définitions et isolement des serveurs
À l’homologation, à chaque tools/list et avant l’exécution (EXIG-SEC-18), la passerelle DOIT calculer 
l’empreinte de chaque définition d’outil complète (nom, titre, description, icônes, schémas d’entrée 
et de sortie, annotations et _meta) et la comparer à l’empreinte épinglée au catalogue; un outil dont 
l’empreinte diffère est retiré de la liste remise à l’agent et suspendu jusqu’à une nouvelle approbation. 
La passerelle DOIT traiter chaque serveur comme un domaine de sécurité distinct : aucun serveur 
ne référence ni ne modifie les outils d’un autre, et la sortie de tout outil est une donnée non fiable 
(section 9.6).
Pourquoi : l’OWASP recommande d’épingler les définitions par empreinte, de les revérifier avant l’exécution et de 
redemander le consentement lorsqu’elles changent[221]; l’empoisonnement d’outil est le risque MCP03 de l’OWASP 
MCP Top 10[222].
Lorsque l’hôte fait exécuter par le modèle du code qui appelle des outils (« mode code »), ce code s’exécute 
dans un bac à sable sans accès réseau direct; l’hôte, qui détient les identifiants, applique à chaque appel la 
même politique d’approbation qu’à un appel direct, et les résultats d’un serveur restent non fiables pour un 
autre[204]. Les exigences de cloisonnement figurent à la section 9.7.
L’élicitation reste le canal par lequel un serveur sollicite une personne, désormais à l’intérieur d’un 
InputRequiredResult. Elle offre deux modes : « form », pour des données structurées selon un schéma plat 
de types primitifs, et « url », pour une interaction hors bande. Le client doit indiquer quel serveur demande 
l’information, offrir le refus et l’annulation, afficher l’URL complète et obtenir le consentement avant de 
l’ouvrir. En mode URL, le serveur ne place ni renseignement sensible ni URL préauthentifiée dans l’URL, 
vérifie que la personne qui l’ouvre est celle qui a déclenché la demande, et les identifiants tiers ainsi obtenus 
ne transitent jamais par le client MCP[223].
EXIG-MCP-21 · NE DOIT PAS
Élicitation : ni secret ni approbation déguisée
Un serveur NE DOIT PAS demander de secret (mot de passe, clé d’API, jeton, donnée de paiement) par 
élicitation en mode formulaire; ces cas passent par le mode URL. Une réponse d’élicitation NE DOIT 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 65 sur 283


---
## [Page PDF 66]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
PAS non plus tenir lieu d’approbation humaine pour une action qui en exige une (palier P3; palier P2 
au-delà du seuil déclaré; toute écriture d’un agent de niveau N2) : seule compte l’approbation signée, 
liée à l’action exacte, décrite à la section 8.5.
Pourquoi : la spécification interdit les secrets en mode formulaire[223]; le brouillon IETF WIMSE AIMS précise qu’une 
confirmation locale dans l’interface ne suffit pas comme autorisation[93].
Le projet OWASP MCP Top 10, édition 2025 encore en phase bêta, fournit une grille de menaces 
commune[222]. Le tableau 18 la met en correspondance avec les exigences du cadre; cette correspondance 
est une interprétation interne. Pour l’analyse de menaces par phase, Hou et al. décrivent le cycle de vie 
d’un serveur MCP en quatre phases (création, déploiement, exploitation, maintenance) et seize scénarios de 
menace répartis entre quatre types d’attaquants[224].
Tableau 18 — Correspondance entre l’OWASP MCP Top 10 (bêta) et les exigences du cadre
Risque OWASP MCP Top 10 (2025, bêta)
Exigences et sections du cadre
MCP01 Gestion des jetons et exposition de secrets
EXIG-MCP-11, EXIG-MCP-18, EXIG-MCP-21; section 9.2
MCP02 Élévation de privilèges par dérive des portées
EXIG-MCP-10; section 9.3
MCP03 Empoisonnement d’outil
EXIG-MCP-14, EXIG-MCP-20
MCP04 Chaîne d’approvisionnement
EXIG-MCP-02, EXIG-MCP-20; section 9.8
MCP05 Injection et exécution de commandes
EXIG-MCP-08, EXIG-MCP-19; section 9.7
MCP06 Injection d’invite par charges contextuelles
EXIG-MCP-20; section 9.6
MCP07 Authentification et autorisation insuffisantes
EXIG-MCP-09, EXIG-MCP-12, EXIG-MCP-13
MCP08 Absence d’audit et de télémétrie
EXIG-MCP-10, EXIG-MCP-16; chapitre 10
MCP09 Serveurs MCP fantômes
EXIG-MCP-01, EXIG-MCP-02; section 11.4
MCP10 Injection de contexte et surpartage
EXIG-MCP-03, EXIG-MCP-16, EXIG-MCP-17
Migration vers la révision 2026-07-28
Les deux générations du protocole coexisteront pendant un temps. Un client peut détecter la génération 
d’un serveur en tentant une requête moderne et en examinant l’erreur 400 éventuelle avant de revenir à 
initialize; sur stdio, server/discover sert de sonde de rétrocompatibilité. Un serveur qui ne connaît que 
2026-07-28 devrait répondre 405 aux requêtes GET et DELETE et ignorer les en-têtes Mcp-Session-Id et 
Last-Event-ID [168, 190]; une version non prise en charge entraîne l’erreur −32022[162]. La migration suit les 
étapes suivantes.
1. Inventorier les serveurs et les clients et inscrire leur révision au catalogue : server/discover pour les 
serveurs à jour, réponse à initialize pour les autres.
2. Ouvrir à la passerelle une double prise en charge bornée : les requêtes 2026-07-28 sont validées par en-
têtes et par corps; les requêtes antérieures ne sont acceptées que pour les serveurs inscrits avec une date 
de migration et sont contrôlées par inspection du corps.
3. Remplacer l’état de session par des identifiants explicites (EXIG-MCP-17) et les requêtes initiées par le 
serveur par MRTR.
4. Remplacer Sampling par des appels à la passerelle de modèles, Roots par des paramètres d’outil ou des 
URI de ressource, et la journalisation protocolaire par la sortie d’erreur standard ou OpenTelemetry 
(section 10.1).
5. Remplacer le DCR par le préenregistrement ou les CIMD (EXIG-MCP-12).
6. Faire passer les tests de contrat et de conformité (section 6.8). Le cadre officiel de tests de conformité 
MCP reste en préversion (versions 0.x : 0.1.16 courante, 0.2.0-alpha.12 publiée le 1er octobre 2026) : ses 
résultats complètent les tests internes sans les remplacer[225, 226].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 66 sur 283


---
## [Page PDF 67]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
7. Retirer de la passerelle la prise en charge de la révision antérieure à l’échéance fixée.
EXIG-MCP-22 · DOIT
Migration bornée et abandon des fonctions dépréciées
La passerelle DOIT accepter les deux générations de MCP pendant une période de coexistence bornée, 
chaque serveur antérieur étant inscrit au catalogue avec sa date de migration. Tous les serveurs et 
clients en production DOIVENT avoir migré vers la révision 2026-07-28 au plus tard le 28 juillet 2027, 
et un nouveau développement NE DOIT PAS s’appuyer sur une fonction dépréciée (Roots, Sampling, 
journalisation protocolaire, DCR, transport HTTP+SSE). Pendant la transition, les clients traitent 
−32002 (serveurs antérieurs) et −32602 comme « ressource introuvable » en réponse à resources/read 
seulement.
Pourquoi : Roots, Sampling, la journalisation et le DCR deviennent admissibles au retrait à partir de la première 
révision publiée le 28 juillet 2027 ou après (le transport HTTP+SSE obéit à une échéance distincte : trois mois après 
que la SEP-2596 atteint l’état final)[196]; l’échéance retenue, choix du cadre, évite qu’une révision future ne rompe 
des intégrations en production. La spécification recommande aux clients d’accepter aussi −32002, code employé par 
les versions antérieures pour « ressource introuvable »[227].
6.6 Intégration horizontale : protocole Agent2Agent
Cette section fixe les règles d’usage du protocole Agent2Agent (A2A), qui relie un agent à un autre agent 
lorsque l’appelant délègue un sous-objectif complet sans connaître le fonctionnement interne de l’appelé. 
MCP (section 6.5) relie un agent à des outils dont les entrées et les sorties sont définies; A2A relie des agents 
autonomes, potentiellement opaques, qui raisonnent et conservent un état sur des échanges à plusieurs 
tours[39]. Le cadre retient la version de protocole 1.0 (publication 1.0.0 du 12 mars 2026, correctif 1.0.1 du 28 
mai 2026)[30].
Rôle, historique et gouvernance
Google a annoncé A2A le 9 avril 2025 avec plus de 50 partenaires[21], puis l’a confié à la Linux Foundation le 
23 juin 2025[22]. La version 0.3.0 (30 juillet 2025) a ajouté gRPC et les cartes d’agent signées, et renommé en 
agent-card.json le chemin de découverte[228, 229]. L’Agent Communication Protocol (ACP) d’IBM Research 
a fusionné avec A2A à la fin d’août 2025 : fusion annoncée le 25 août, dépôt archivé le 27 août, annonce de 
la fondation LF AI & Data (Linux Foundation) le 29 août[24, 230]. La version 1.0.0, première version stable, a 
paru le 12 mars 2026[29]. A2A est devenu un projet de stade « Growth » de l’Agentic AI Foundation (AAIF), 
transfert annoncé le 17 août 2026 et confirmé par le billet du projet du 27 août 2026[5, 35]. La chronologie 
d’ensemble figure à la section 2.2.
Trois faits fondent le choix d’A2A comme protocole agent-agent par défaut. Sa gouvernance est neutre : un 
comité directeur technique de huit entreprises (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, 
SAP et ServiceNow; composition annoncée le 12 mars 2026) le pilote[29], sous l’égide de la fondation qui 
héberge aussi MCP. Son adoption est large : plus de 150 organisations le soutiennent (Linux Foundation, 
9 avril 2026), et Microsoft et AWS l’ont intégré à leurs plateformes d’agents[15]. Son outillage est ouvert : 
six SDK officiels (Python, JavaScript, Java, Go, .NET et Rust), une trousse de compatibilité (a2a-tck), un 
inspecteur et une interface en ligne de commande[231, 232].
ATTENTION : QUATRE PROTOCOLES « ACP »
Le sigle désigne (1) l’Agent Communication Protocol d’IBM, fusionné dans A2A; (2) l’Agent Connect 
Protocol d’AGNTCY, dont le dépôt est archivé depuis le 11 avril 2026; (3) l’Agent Client Protocol, créé par 
Zed pour relier les éditeurs de code aux agents de codage; (4) l’Agentic Commerce Protocol d’OpenAI et 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 67 sur 283


---
## [Page PDF 68]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
de Stripe[183, 233, 234]. Toute offre qui invoque un « ACP » pour coordonner des agents se vérifie au regard 
de ces quatre sens.
EXIG-A2A-01 · DOIT
A2A 1.0 pour toute délégation entre agents
Toute interaction par laquelle un agent délègue une tâche à un agent d’un autre domaine, d’un autre 
cadriciel ou d’un tiers DOIT utiliser A2A, version de protocole 1.0 (sauf pendant la coexistence bornée 
de l’EXIG-A2A-15). Un protocole agent-agent propriétaire DOIT être contenu derrière un adaptateur, 
conformément au catalogue (section 6.3). Les transferts entre sous-agents d’un même orchestrateur, 
dans un même processus, n’y sont pas tenus.
Pourquoi : un contrat d’échange unique évite une intégration ad hoc par paire d’agents et garde l’agent appelé 
remplaçable.
Carte d’agent 1.0
La carte d’agent (Agent Card) est le contrat public d’un agent  : un document JSON qui dit qui il est, 
ce qu’il sait faire, où le joindre et comment s’authentifier. Un agent exposé la publie à https://{domaine}/
.well-known/agent-card.json; l’ancien chemin /.well-known/agent.json appartient aux versions 0.1 et 0.2, 
désormais obsolètes[30, 68]. La définition normative des objets est le fichier a2a.proto, sérialisé en ProtoJSON; 
les énumérations s’écrivent en majuscules préfixées, par exemple TASK_STATE_WORKING [68]. Le tableau 19 
résume les champs et les règles du cadre; un exemple complet figure à l’annexe C.
Tableau 19 — Champs de la carte d’agent A2A 1.0 et règles du cadre
Champ
Statut dans A2A 1.0
Règle du cadre
name, description
Obligatoires
Nom identique à la fiche du registre; description qui 
dit ce que fait l’agent et ce qu’il ne fait pas.
supportedInterfaces
Obligatoire; liste ordonnée, la pre­
mière entrée est préférée; chaque 
entrée exige url, protocolBinding et 
protocolVersion, tenant est faculta­
tif
Adresses de la passerelle d’agents, jamais l’adresse di­
recte de l’agent.
version
Obligatoire; format libre
SemVer (versionnage sémantique; voir la section 6.8), 
incrémentée à chaque changement publié; sert d’ETag.
capabilities
Obligatoire; sous-champs faculta­
tifs streaming, pushNotifications, 
extensions, extendedAgentCard
Déclarer le comportement réel; extensions approuvées 
seulement.
defaultInputModes, 
defaultOutputModes
Obligatoires
Types média effectivement acceptés et produits.
skills
Obligatoire; chaque compétence 
exige id, name, description et tags
id stable, en minuscules séparées par des traits 
d’union (kebab-case) (convention du cadre); une por­
tée OAuth par compétence.
securitySchemes, 
securityRequirements
Facultatifs; aucun secret dans la 
carte
Obligatoires; renvoient au fournisseur d’identité de 
l’entreprise.
signatures
Facultatif
Obligatoire : signature JWS (JSON Web Signature) sur 
la carte canonisée.
provider, documentationUrl, 
iconUrl
Facultatifs
provider renseigné par la direction responsable.
Sources : spécification A2A 1.0 et a2a.proto [192, 235]; règles : choix du cadre.
Signature. La carte peut être signée en JWS (RFC 7515) après canonisation JCS (JSON Canonicalization 
Scheme), le champ signatures étant exclu du contenu signé; la spécification recommande au client de 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 68 sur 283


---
## [Page PDF 69]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
vérifier au moins une signature avant de faire confiance à la carte et interdit de vérifier avec une clé expirée 
ou révoquée[68, 236]. Le cadre rend la signature obligatoire : une carte non signée s’imite aussi facilement 
qu’une page web.
Carte étendue. La capacité extendedAgentCard active l’opération GetExtendedAgentCard, qui exige une 
authentification et vérifie les permissions du client; la carte étendue ne devrait pas contenir d’information 
sensible exploitable en cas de fuite[68]. On publie ainsi une carte publique minimale et l’on réserve les 
compétences internes aux clients autorisés.
Découverte et cache. La spécification admet trois modes de découverte : URI bien connue, registre organisé 
(sans API de registre normalisée) et configuration directe; l’accès aux cartes peut être restreint par mTLS, 
filtrage réseau ou OAuth[237]. Dans l’entreprise, le registre (section 11.4) est la source de découverte autorisée. 
Le guide de découverte recommande un en-tête Cache-Control, un ETag dérivé du champ version ou d’un 
hachage, et des requêtes conditionnelles (If-None-Match)[237]. Comme la spécification n’impose pas SemVer 
pour version [68], le cadre l’impose : sans incrément fiable, un client garderait en cache une carte périmée.
Métadonnées de gouvernance. La carte 1.0 n’a pas de champ libre au premier niveau, et une extension ne 
peut pas modifier les structures de base[192, 238]. Le niveau d’autonomie, la classe de risque, le centre de coûts 
et la classification maximale des données restent donc à la fiche du registre (annexe B). Si un pair doit les 
lire, ils se déclarent comme extension de données dans capabilities.extensions. Une extension y figure 
avec son URI, qui porte la version, une description, l’indicateur required et ses paramètres; elle s’active 
par l’en-tête A2A-Extensions, un changement incompatible exige une nouvelle URI, et aucune extension 
ne doit contourner les contrôles de sécurité de l’agent[238].
EXIG-A2A-02 · DOIT
Carte publiée et inscrite au registre
Tout agent invocable par d’autres agents DOIT publier une carte conforme à A2A  1.0, l’inscrire 
au catalogue d’entreprise (et la rattacher à sa fiche au registre, section 11.4) et déclarer dans 
supportedInterfaces les adresses de la passerelle d’agents. Un agent exposé hors de l’entreprise DOIT 
aussi publier sa carte à l’URI bien connue; un agent interne ne la publie pas.
Pourquoi : la découverte passe par une source contrôlée, et aucun appel ne contourne la passerelle (section 9.4).
EXIG-A2A-03 · DOIT
Carte signée et vérifiée
Toute carte inscrite au catalogue d’entreprise DOIT porter au moins une signature JWS valide, calculée 
sur la carte canonisée JCS avec une clé de l’émetteur de la carte (clé gérée par l’entreprise pour ses 
propres agents; pour un agent de tiers, clé dont le catalogue consigne la confiance). La passerelle 
d’agents et les clients DOIVENT rejeter une carte sans signature valide ou signée par une clé expirée 
ou révoquée. La carte NE DOIT PAS contenir de secret.
Pourquoi : une carte usurpée détournerait des tâches et des données vers un faux agent, risque que l’OWASP classe 
sous ASI07, communication inter-agents non sécurisée[28].
EXIG-A2A-04 · DOIT
Version de carte et revalidation du cache
Le champ version de la carte DOIT suivre SemVer et être incrémenté à chaque changement publié 
(règle du cadre). Le serveur DOIT fournir un ETag dérivé de cette version et un Cache-Control; le 
catalogue et les clients DOIVENT revalider leur copie par requête conditionnelle. Les règles de compa­
tibilité et de coexistence des versions sont celles de la section 6.8.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 69 sur 283


---
## [Page PDF 70]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Pourquoi : un incrément fiable est le signal sur lequel le cadre fonde l’invalidation des copies en cache des clients 
(le guide de découverte admet aussi un ETag dérivé d’un hachage).
EXIG-A2A-05 · NE DOIT PAS
Aucun champ hors norme dans la carte
Une carte NE DOIT PAS contenir de champ non défini par A2A 1.0, par exemple 
x-enterprise-governance. Une extension NE DOIT PAS être publiée sauf si son URI figure au 
catalogue d’entreprise parmi les extensions approuvées, après revue de sécurité; l’indicateur required: 
true DOIT recevoir une dérogation du comité d’architecture (EXIG-APP-02).
Pourquoi : un champ hors norme n’a aucune sémantique garantie chez les pairs, et une extension obligatoire exclut 
tout client qui ne la prend pas en charge (erreur ExtensionSupportRequiredError) [68].
EXIG-A2A-06 · DOIT
Compétences internes dans la carte étendue
Les compétences réservées à des consommateurs internes DOIVENT être publiées dans la carte 
étendue, servie par GetExtendedAgentCard après authentification et contrôle des permissions. La carte 
publique se limite aux compétences destinées aux appelants externes.
Pourquoi : la carte publique est lisible par tous; elle ne doit pas cartographier la surface interne de l’entreprise.
Tâches, messages et artefacts
A2A organise le travail en tâches (Task). Le client envoie un message; le serveur crée la tâche et lui attribue 
son identifiant, le client ne pouvant pas en imposer un pour une nouvelle tâche; contextId regroupe les 
tâches et les messages d’une même interaction[68]. Les messages et les artefacts, c’est-à-dire les résultats 
produits par la tâche, se composent de parties (Part). En 1.0, une partie porte exactement un des membres 
text, raw (octets encodés en base64), url ou data (JSON structuré), avec mediaType, filename et metadata 
facultatifs; elle remplace les anciens TextPart, FilePart et DataPart [192, 235].
Une tâche suit une machine à huit états réels (neuf valeurs d’énumération avec la valeur zéro) (figure 8). 
Deux états sont actifs (SUBMITTED, WORKING); deux sont interrompus : INPUT_REQUIRED quand l’agent attend 
une précision ou une approbation, AUTH_REQUIRED quand il lui faut un justificatif supplémentaire; quatre 
sont terminaux (COMPLETED, FAILED, CANCELED, REJECTED); la valeur zéro TASK_STATE_UNSPECIFIED ne dé­
signe aucun état réel[192]. Une tâche terminale n’accepte plus de message (UnsupportedOperationError) et 
ne peut plus être annulée (TaskNotCancelableError)[68]. Les graphies minuscules comme input-required 
appartiennent aux versions 0.x et ne s’emploient plus.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 70 sur 283


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
