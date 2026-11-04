# Questions pour l'audit bibliographique (extraites des rapports audit_01 à audit_25)


## audit_01.md
- p. 7 : le communiqué Gartner du 28 avril 2026 [2] contient-il le « 13 % » et le « > 150 000 agents par entreprise du Fortune 500 d'ici 2028, contre moins de 15 en 2025 »? Population et définition d'« agent »?
- p. 7 : [1] (26 août 2025, 40 % des applications d'ici 2026) et [3] (25 juin 2025, plus de 40 % de projets annulés d'ici fin 2027) : à ma connaissance, les chiffres et les dates sont exacts; à confirmer.
- p. 8 : A2A versé à l'AAIF (billet du 27 août 2026) : déjà consigné en H.4 (no 2), confirmé; la date d'approbation du 4 août reste non vérifiée.
- p. 8 : la formation de l'AAIF le 9 décembre 2025 avec MCP [4] me semble exacte; à confirmer.
- p. 8, réf. [6] : auteur noté « Erik S. »; *Building effective agents* est signé Erik Schluntz et Barry Zhang : forme de l'auteur à corriger dans l'annexe G.
- p. 9 : « MCP sans état » : la révision 2026-07-28 retire-t-elle effectivement les sessions protocolaires et `Mcp-Session-Id` (SEP-2567, SEP-2575)? Existence d'« A2A 1.0 »?
- p. 2 : le règlement (UE) 2026/1744 reporte-t-il l'annexe III au 2 décembre 2027 et l'annexe I au 2 août 2028? (EUR-Lex non rouvert selon H.5.)
- p. 2, p. 8 : E-23 (2027) en vigueur le 1er mai 2027, applicable aux institutions financières fédérales; le BSIF exige-t-il à cette date une validation complète des modèles existants ou un plan?
- p. 2 : l'art. 65.2 de la Loi sur l'accès vise-t-il bien les décisions fondées exclusivement sur un traitement automatisé par un organisme public (pendant de l'art. 12.1 de la Loi sur le privé)? Je le crois exact.
- p. 7 : le European Interoperability Framework (EIF) retient-il bien quatre niveaux (juridique, organisationnel, sémantique, technique)? Je le crois exact.
- p. 12 : Gartner (juin 2025, [3]) parle-t-il bien de produits rebaptisés « agentiques » (*agent washing*)? Je le crois exact.

audit_01.md : 21 constats (0 BLOQUANT, 4 MAJEUR, 17 MINEUR)


## audit_02.md
1. p. 16, [16] Menlo Ventures : les 37 G$ US comprennent-ils les API de modèles, donc l'inférence ? Quel est le périmètre (États-Unis ou monde) et quelle est la taille de l'échantillon ?
2. p. 16, [18] IBM 2025 : quelle est la population du 13 % et du « une sur cinq » (organisations ayant subi une violation) ? p. 16, [19] : édition 2026, 4,99 M$ US et hausse de 12 % (4,44 × 1,12 ≈ 4,97).
3. p. 16, [14] : le libellé exact est-il « 10 000+ active public servers » ? [15] : la Linux Foundation emploie-t-elle « Azure AI Foundry » ou « Microsoft Foundry » ?
4. p. 16, [10] State of FinOps 2026 : 1 192 répondants et 98 %. [11] CyberArk : 2 600 répondants, 20 pays, Canada inclus, 68 %; la source est un communiqué reproduit par Silicon UK (source secondaire).
5. p. 16, [17] : contexte exact des multiplicateurs 4× et 15×.
6. p. 17, [28] : date de publication du Top 10 agentique de l'OWASP (9 ou 10 décembre 2025). [29, 30] : A2A 1.0.0 du 12 mars 2026 et 1.0.1 du 28 mai 2026. [31, 32] : entrée d'agentgateway à l'AAIF le 4 juin 2026. [36] : Agent Router le 9 septembre 2026. [38] : quatre projets le 22 octobre 2026.
7. p. 17, [5, 35] : approbation du conseil le 4 août (non vérifiée, déjà consigné en H.4 n° 2). p. 17, [34] : 12 mois et 90 jours dans la politique de cycle de vie de MCP 2026-07-28.
8. p. 18, [40, 41] : AP2 a-t-il été « confié à la FIDO Alliance » ? Qui porte l'UCP ? Existe-t-il un groupe de travail de l'AAIF sur le commerce agentique ?
9. p. 19, [46] : Agent 365 en disponibilité générale le 1er mai 2026 et synchronisation en préversion. [47] : ServiceNow, 5 mai 2026. [52] : Gartner, document 8214461, « résumé public, août 2026 » (la référence ne porte pas de mois).
10. p. 20, [48] : création automatique de l'Entra Agent ID depuis juillet 2026, non désactivable. [53-55] : crédits Copilot, crédits Flex et « Agentic Work Units ».
11. p. 20, [58] : règlement (UE) 2026/1744 du 8 juillet 2026. La date du 2 décembre 2027 est-elle fixe ou une date butoir assortie d'un déclenchement anticipé ?
12. p. 20, [8] : E-23 parle-t-elle d'un inventaire des modèles « à risque non négligeable », ou de tous les modèles ?
13. p. 21, [59] : la fiche de Standards Norway contient-elle la définition de « AI agent » ? Sinon, quelle source appuie le texte ? [76] : IMDA, version 1.5, et section 1.1.3.

audit_02.md : 32 constats (0 BLOQUANT, 6 MAJEUR, 26 MINEUR)


## audit_03.md
- p. 23, [83] : le « certificat d'autonomie » figure-t-il bien dans Feng, McDonald et Zhang, arXiv:2506.12469 v2?
- p. 23, [84] : ReAct : réduction des hallucinations par rapport à CoT et exactitude sur HotpotQA (voir 03-24).
- p. 24, [88, 89] : au 27 octobre 2026, le rabais par lots est-il de 50 % avec une fenêtre de 24 h, chez Anthropic comme chez OpenAI?
- p. 24, [87] : T10 correspond-elle à « Overwhelming Human in the Loop » dans la v1.1 des Threats and Mitigations de l'OWASP?
- p. 24, [91] : NHI9 (réutilisation) et NHI10 (usage humain d'une NHI) dans l'OWASP NHI Top 10 2025.
- p. 24, [93] : draft-ietf-wimse-aims-00 est-il adopté par le groupe de travail WIMSE? Le titre est-il bien « AI Identity Management System »? Le brouillon qualifie-t-il les clés d'API statiques d'antipatron?
- p. 24-25, [90, 92] : Microsoft déconseille-t-il les principaux de service traditionnels pour les agents? Entra Agent ID distingue-t-il « sponsor » et « owner »?
- p. 24, [94] : texte de l'art. 26(2) du RIA, et date d'application aux systèmes de l'annexe III.
- p. 25, [4, 35] : AAIF a-t-elle accueilli MCP en décembre 2025 et A2A le 17 août 2026? A2A était sous gouvernance neutre de la Linux Foundation dès juin 2025.
- p. 26, [95] : communiqué Gartner du 26 mai 2026 sur la « confusion » entre capacité d'agir et portée des accès.
- p. 27, [97, 98] : NIST AI 100-2 E2025 (concevoir dans l'hypothèse d'une injection) et billet du NCSC (pas de séparation intrinsèque entre données et instructions).
- p. 28, [99] : libellé de GOVERN 3.2 du NIST AI RMF.
- p. 28, [76] : les quatre dimensions du cadre agentique de l'IMDA, et son § 1.1.3 (p. 22).
- p. 28, [100] : CoALA juge-t-elle l'écriture en mémoire procédurale plus risquée?
- p. 29, [101] : version arXiv de CaMeL qui donne 77 % et 84 % (voir 03-23).


## audit_04.md
- p. 34 [104] : AWS Step Functions. Le « exactement une fois » des flux Standard porte-t-il sur l'exécution du flux seulement, effets des tâches réessayées exclus? Durées confirmées : Standard ≤ 1 an, Express ≤ 5 min.
- p. 34 [81] : Temporal, « sans limite de temps imposée ». Quelle est la limite de taille de l'historique qui impose Continue-As-New?
- p. 35 [36, 106] et p. 40 [130] : Envoy AI Gateway, renommé Agent Router, a-t-il rejoint l'AAIF le 9 septembre 2026? p. 40 [31] : agentgateway à l'AAIF le 4 juin 2026?
- p. 35 [107] : nom exact de la politique `llm-token-limit` d'Azure API Management.
- p. 36 [111] : greffon AI A2A Proxy de Kong, version 3.14 et plus, édition AI Gateway Enterprise.
- p. 36 [28] : l'identifiant ASI05 « Unexpected Code Execution » de l'OWASP Top 10 for Agentic Applications 2026.
- p. 37 [9] : le Centre d'architecture Azure demande-t-il le filtrage de sécurité (security trimming) « dans chaque agent »?
- p. 38 [119, 120] : `invoke_workflow` figure-t-il parmi les valeurs de `gen_ai.operation.name` dans la version épinglée (v1.41.0) des conventions GenAI?
- p. 38 [46] : Microsoft Agent 365 est-il en disponibilité générale depuis le 1er mai 2026, avec les actions de cycle de vie sur les agents tiers « à venir »?
- p. 38 [116, 117] : SPIFFE et SPIRE sont-ils des projets diplômés de la CNCF (selon moi, depuis 2022)?
- p. 40 [122] : l'intégration de Temporal avec l'OpenAI Agents SDK est-elle en disponibilité générale depuis le 23 mars 2026? [125] : Microsoft Agent Framework 1.0? [126] : les agents de flux de Google ADK persistent-ils l'état hors processus après chaque transition?
- p. 40 [140] : Kafka garantit-il par défaut une livraison au moins une fois, compte tenu des réglages du producteur idempotent par défaut depuis la 3.0 et du commit automatique côté consommateur?
- p. 41 [48] : A2A est-il en disponibilité générale dans Copilot Studio depuis avril 2026, avec une identité Entra Agent ID pour chaque nouvel agent? [49] : A2A entrant et sortant dans Agentforce?
- p. 41 [143, 144] : les conditions du banc d'essai de TrueFoundry (1 vCPU, de 200 à 370 requêtes par seconde) et de sa FAQ (« typiquement < 5 ms ») sont-elles comparables?
- [04-07] : combien de temps les API de paiement et les ERP courants gardent-ils les clés d'idempotence (par exemple 24 h)?

audit_04.md : 28 constats (1 BLOQUANT, 8 MAJEUR, 19 MINEUR)


## audit_05.md
- p. 43 : Anthropic, outil mémoire côté client [152]. Validation des chemins contre la traversée « exigée », recommandations sur la taille et la suppression des mémoires inutilisées : formulation exacte (exige ou recommande).
- p. 43 : CoALA [100] juge-t-il expressément l'écriture procédurale « nettement plus risquée »? Centre d'architecture Azure [9] : proscription du partage d'état mutable entre agents concurrents (patron concurrent).
- p. 45 : nouvel EIF 2017 [157]. Vérifier « 12 principes et 47 recommandations » et l'objet de la recommandation 26 (accords d'interopérabilité dans toutes les couches).
- p. 45 : règlement (UE) 2024/903. Entrée en vigueur le 11 avril 2024; rôle du comité pour une Europe interopérable dans la mise à jour de l'EIF [159].
- p. 47 : AsyncAPI 3.x (3.1.0). Liste des valeurs de `schemaFormat` que les outils doivent obligatoirement reconnaître; JSON Schema 2020-12 en fait-il partie? (voir 05-10)
- p. 47 : MCP [162, 163]. JSON Schema 2020-12 comme dialecte par défaut (depuis 2025-11-25) toujours valide en 2026-07-28.
- p. 48 : AG-UI [164-166]. « 31 types d'événements standard », licence MIT, « partenariat de CopilotKit avec LangChain et CrewAI » (LangGraph?).
- p. 48 : affiliation de Kai Waehner [167] (voir 05-25).
- p. 49 : documentation A2A [161]. Formulation « strongly recommend » d'une solution de gestion d'API pour les serveurs exposés.
- p. 49 : MCP 2026-07-28 [169]. Liste des extensions officielles; statut de l'autorisation (cœur ou extension) (voir 05-26).
- p. 50 : OpenAPI 3.2.1 (10 septembre 2026) [170]; Arazzo 1.1.0 (17 mai 2026) [172] (l'annexe H, réf. [486], confirme l'étiquette 1.1.0, mais pas la date); draft-ietf-oauth-v2-1-16 (septembre 2026) et son expiration le 7 mars 2027 [176]; draft-ietf-oauth-transaction-tokens-11 [179]; statut « brouillon de groupe de travail » d'ID-JAG [177].
- p. 50 : A2A 1.0. En-tête `A2A-Version` obligatoire à chaque requête; dates de 1.0.0 (12 mars 2026) et de 1.0.1 (28 mai 2026) [29, 30].
- p. 51 : AGNTCY « candidat à l'AAIF » (cohérent avec le § 6.9 et le tableau 5 : à confirmer à la source [37, 182]).

audit_05.md : 26 constats (0 BLOQUANT, 9 MAJEUR, 17 MINEUR)


## audit_06.md
- p. 54 : la date d'annonce de MCP (25 novembre 2024), le don à l'AAIF le 9 décembre 2025 et la liste des membres platine au lancement [4, 20, 193].
- p. 54 : les chiffres « environ 10 000 serveurs actifs » et « plus de 97 millions de téléchargements mensuels » [14] (déclarés par le projet, sans mesure indépendante).
- p. 54 : depuis 2026-07-28, une SEP prend-elle la forme d'une demande de tirage, et une extension exige-t-elle une implémentation de référence dans un SDK officiel [168, 169]?
- p. 54 : version candidate verrouillée le 21 mai 2026; prise en charge par les SDK TypeScript, Python, Go et C# à la sortie, Rust en bêta [33, 194]; règle « AAAA-MM-JJ = dernier changement incompatible » (voir 06-18).
- p. 54 : registre MCP lancé en préversion le 8 septembre 2025 et toujours en préversion, sans prise en charge des serveurs privés [25, 43].
- p. 55 : l'identifiant non nul est-il nouveau en 2026-07-28 ou acquis depuis 2024-11-05 (voir 06-19)? Champ `resultType` [162].
- p. 57 : numéros de SEP (2567, 2575, 2243, 2322, 2549, 2663, 2106, 2596) et codes −32020, −32021, −32022; passage de « ressource introuvable » de −32002 à −32602 [162, 168, 190].
- p. 57 : fondement des retraits immédiats de `ping`, `logging/setLevel` et `notifications/roots/list_changed` face à la règle des 12 mois (voir 06-20).
- p. 58 : méthodes et états de l'extension Tasks (`tasks/get`, `tasks/update`, `tasks/cancel`; working, input_required, completed, failed, cancelled) [191]; clés `_meta.ui.*` de MCP Apps [202].
- p. 58 : affirmation d'Akamai sur le déni de service par tâches asynchrones et le XSS stocké par les interfaces générées [203].
- p. 58 : règle des préfixes réservés (« deuxième libellé » `modelcontextprotocol` ou `mcp`) [169].
- p. 59 : seuil « de l'ordre de 1 à 5 % de la fenêtre de contexte » des bonnes pratiques MCP [204]; chiffres de 77 000, 8 700 et 72 000 jetons et base de calcul des 85 % [205].
- p. 59 : HTTP 403 sur un `Origin` invalide et terme « DNS rebinding » [190].
- p. 60 : citation par MCP 2026-07-28 du brouillon OAuth 2.1 −13; `iss` (RFC 9207) « devrait » côté serveur d'autorisation et rejet s'il est absent alors qu'il est annoncé [209, 212].
- p. 61 : CIMD −02 (limite d'environ 5 Ko, interdiction du secret partagé) et référence −00 dans MCP [216]; dépréciation du DCR en 2026-07-28 [168, 215].
- p. 62 : EMA (ID-JAG par RFC 8693, puis RFC 7523) et extension OAuth Client Credentials « stables depuis 2026-07-28 » [217, 218]; valeurs par défaut des annotations et formulation « should never » [197, 201].


## audit_07.md
- p. 63 : date (25 juin 2026) et contenu de l'analyse d'Akamai [203]. Cinq zones de risque ou six vecteurs?
- p. 63 : SEP-414 (contexte de trace dans `_meta`) et codes −32020, −32021, −32022 [162, 168, 190].
- p. 63 : conventions OpenTelemetry pour MCP au niveau Development, nom de span d'après `mcp.method.name` [219].
- p. 64 : x-mcp-header limitée à string, integer et boolean, à l'exclusion de number; obligation pour le client d'écarter les outils dont la directive est invalide [190, 197].
- p. 65 : Invariant Labs, 1er avril 2025. Les trois attaques (empoisonnement, rug pull, ombrage) figurent-elles dans le même billet [220]? Fiche OWASP MCP [221].
- p. 66 : Hou et al. [224], quatre phases et seize scénarios répartis entre quatre types d'attaquants. Ce décompte dépend de la version arXiv, à préciser.
- p. 66 : liste et intitulés de l'OWASP MCP Top 10 2025 (bêta) [222].
- p. 66 : cadre de conformité MCP, versions 0.1.16 et 0.2.0-alpha.12 (1er octobre 2026) [225, 226].
- p. 66 : brouillon IETF « WIMSE AIMS » [93], intitulé exact et passage sur la confirmation locale.
- p. 67 : A2A 0.3.0 (30 juillet 2025 : gRPC, cartes signées, renommage en `agent-card.json`) [228, 229]; fusion de l'ACP d'IBM (25, 27 et 29 août 2025) [24, 230]; plus de 150 organisations (Linux Foundation, 9 avril 2026) [15]; six SDK officiels, dont Rust [231, 232].
- p. 67 : dépôt de l'Agent Connect Protocol d'AGNTCY archivé le 11 avril 2026 [233].
- p. 68 : champs obligatoires et facultatifs de la carte 1.0 (`supportedInterfaces`, `securityRequirements`, `capabilities.extendedAgentCard`) [192, 235].
- p. 69 : la spécification « interdit » de vérifier avec une clé expirée ou révoquée (MUST NOT ou SHOULD NOT?) et traitement de `jku` [68, 236].
- p. 70 : graphie de l'énumération en 1.0, TASK_STATE_CANCELED ou TASK_STATE_CANCELLED (a2a.proto); table de transitions; erreur renvoyée pour un message vers une tâche terminale (UnsupportedOperationError) [68, 192].
- p. 70 : la spécification 1.0 prévoit-elle une déduplication par identifiant de message (voir 07-02)?


## audit_08.md
- p. 71 : A2A 1.0, nom exact et sémantique de `returnImmediately`; UnsupportedOperationError pour un message envoyé à une tâche terminale; ListTasks qui omet les artefacts par défaut [68].
- p. 71 : en A2A 1.0, un message A2A ou SendMessageRequest a-t-il un champ désignant l'AgentSkill (décisif pour 08-03)? Le flux SSE se ferme-t-il à l'entrée d'un état interrompu [68]?
- p. 71-72 : en-tête vide ⇒ 0.3; paramètre de requête équivalent; TLS 1.3 « recommandé »; liste SSRF et délai de 10 à 30 s pour les notifications push [68, 161].
- p. 72 : A2A 1.0 ajoute-t-il un flux Device Code et un indicateur PKCE [30, 240]?
- p. 73 : existence et statut du dépôt `open-telemetry/semantic-conventions-genai` et de sa convention A2A (Development, non étiquetée) [241].
- p. 75 : SDK JavaScript en disponibilité générale le 22 juillet 2026 [242]; niveaux MUST/SHOULD/MAY d'a2a-tck [243]; interface en ligne de commande présentée le 1er octobre 2026, versions dès le 9 septembre [244, 245].
- p. 75-76 : qualité de Kai Waehner, « conseiller indépendant » (anciennement Field CTO chez Confluent?) [167, 246].
- p. 76 : CloudEvents 1.0.2 (février 2022) et statut Graduated de la CNCF le 25 janvier 2024 [173, 247, 248]; AsyncAPI 3.1.0 publiée le 31 janvier 2026 [249].
- p. 76, 81 : comportement par défaut du « Key Mapper » dans la liaison Kafka 1.0.2 [250] (08-32).
- p. 77 : Auth Context, Data Classification et Expiry Time absentes de la 1.0.2 [251]; valeurs et définitions d'authtype (notamment `user`, `system`) [252]; obligation de rejet et d'intégrité par les intermédiaires dans Data Classification [255]; règle multi-sauts de Distributed Tracing [253].
- p. 77 : conventions OpenTelemetry de messagerie, liens par défaut et parenté admise pour un message unique [254].
- p. 79-80 : ordre limité au lot pour les files coopératives (KIP-932) [258]; Kafka 4.0 du 18 mars 2025, sens de « généralise » le protocole de rééquilibrage (KIP-848 : disponibilité générale ou valeur par défaut côté client?) [259]; files coopératives prêtes pour la production en 4.2.0 (17 février 2026) et files de lettres mortes en 4.4.0 (22 octobre 2026) [260, 261]; propos de Confluent sur le rejeu déterministe [262].
- p. 81 : sens de [238] (une nouvelle URI pour tout changement incompatible d'une extension A2A); OWASP sur l'épinglage par empreinte et le nouveau consentement [221].

audit_08.md : 32 constats (1 BLOQUANT, 13 MAJEUR, 18 MINEUR)


## audit_09.md
- p. 90 : RFC 8693 § 4.1 : les `act` imbriqués sont-ils « informational only » et exclus des décisions d'accès ? (tranche 09-02)
- p. 82 : la définition `Tool` de MCP 2026-07-28 est-elle bien sans champ de version [197], et le champ `version` d'une carte A2A est-il de format libre [68] ? Une extension A2A incompatible exige-t-elle une nouvelle URI [238] ?
- p. 82 : l'OWASP [221] recommande-t-il l'épinglage par empreinte et un nouveau consentement à chaque modification ?
- p. 83 : le cycle Active, Deprecated, Removed de MCP [34]; registre officiel toujours en préversion [43].
- p. 84 : état de la suite de conformité MCP (0.2.0-alpha) [225, 226]; AAIF à dix projets au 22 octobre 2026 [38, 130]; processus d'admission [42, 263].
- p. 84 : AGNTCY à la Linux Foundation le 29 juillet 2025 [23]; proposition no 57 du 12 octobre 2026 et 81 organisations [37]; OASF inspiré d'OCSF, ADS sur OCI, SLIM sur gRPC et MLS RFC 9420, Agent Badges [264-270]; brouillons IETF individuels [271, 272].
- p. 85 : ACP en bêta, portée du jeton partagé (marchand, montant, échéance ?) [183, 27]; AP2 0.2 et Human Not Present, don à la FIDO Alliance le 28 avril 2026 [26, 41]; UCP de janvier 2026 [184]; existence d'autres protocoles (Visa TAP, Mastercard Agent Pay, x402).
- p. 86 : Google Research, billet du 28 janvier 2026 (180 configurations; +80,9 %; −39 à −70 %; 17,2 fois et 4,4 fois) [273] et version 3 du 8 avril 2026 (260 configurations; +80,8 % à −70,0 %) [274]; auteurs « Kim, Liu et coll. ».
- p. 86 : article d'Anthropic du 23 janvier 2026, surcoût de 3 à 10 fois, trois cas justifiant le multiagent, « victoire prématurée » [275].
- p. 87 : Cognition [276], LangChain [277], Centre d'architecture Azure (niveaux de complexité, trois motifs) [9].
- p. 89 : Agentforce, un seul niveau de délégation multiorganisation [49]; Magentic-One dans Microsoft Agent Framework [278, 279].
- p. 90 : « Mind Viruses », Papadopoulos et coll., août 2026 [280]; recommandation de Microsoft de limiter le clavardage de groupe à trois agents, gestionnaire compris ou non [9].
- p. 92 : OpenAI, moins de 20 fonctions [115] et 15 ou 10 outils [66]; Anthropic, de 30 à 50 outils [281]; recherche d'outils (−85 %; 49 → 74 %; 79,5 → 88,1 %) [205].


## audit_10.md
- p. 97 : existence et date de draft-ietf-httpapi-idempotency-key-header-08 (« 22 octobre 2026 »); codes 409 et 422; recommandation d'UUID; politique d'expiration des clés (utile à 10-11) [78].
- p. 97 : A2A 1.0, notifications push : « au moins une tentative de livraison (reprises facultatives, doublons possibles) » [68].
- p. 93 et 102 : politique de réessai par défaut des activités Temporal (nombre de tentatives illimité?) [79]; limites d'historique et de charge utile [80, 81] (10-19, 10-29).
- p. 95 : recommandation Temporal d'inscrire la compensation avant l'activité et de poursuivre après une erreur non réessayable [286].
- p. 96 : Microsoft, patron Saga : trois anomalies et six contre-mesures, mauvaise adéquation aux dépendances cycliques [67].
- p. 96 : SagaLLM, Chang et Geng, PVLDB 2025 : lieu et année exacts de publication [287, 288].
- p. 94 : Microsoft Agent Framework, magasins Python à liste blanche de types à la désérialisation; granularité des points de contrôle [105].
- p. 94 : LangGraph, voyage dans le temps (réexécution des nœuds suivants) [283]; persistance par super-étape [124].
- p. 94 : Anthropic, déploiements « arc-en-ciel » [17].
- p. 98 : Cognition (Yan, 22 avril 2026), nuance « écritures à fil unique » [289].
- p. 98 : Anthropic, synthèses de sous-agents « souvent de 1 000 à 2 000 jetons » [17, 149].
- p. 99-100 : RIA art. 14(4)e) (arrêt sûr) [290]; NIST AI RMF MANAGE 2.4 [99]; OpenAI, interruption ciblée ou générale [291].
- p. 100 : MAST : « plus de 1 600 traces », « sept cadriciels », 14 modes, intitulés des trois catégories [292].
- p. 92-93 (couture) : Anthropic, recherche d'outils : -85 % de jetons; 49 → 74 % (Opus 4) et 79,5 → 88,1 % (Opus 4.5) [205]; OpenAI « moins de 20 fonctions » [115].


## audit_11.md
- p. 106, [304] : existe-t-il une révision SAE J3016_202609? La dernière que je connaisse est J3016_202104.
- p. 103-112, [76] : IMDA, *Model AI Governance Framework for Agentic AI*, « version 1.5 » : vérifier la version et les passages cités (portée et réversibilité, chaîne de pensée, refus par défaut, quatre catégories de déclencheurs).
- p. 103, [95] : Gartner, communiqué du 26 mai 2026 : la prévision « 40 % d'ici 2027 » et la « gouvernance binaire ».
- p. 104, [95] : les niveaux Gartner Observer, Conseiller, Agir avec approbation et Agir de façon autonome, et l'inclusion des contrôles Observer dans Conseiller.
- p. 106, [75] : la matrice de portée d'AWS associe-t-elle la portée 2 à une approbation avant chaque action et la portée 3 à des interrupteurs d'arrêt?
- p. 105, [83] : Feng et al. : « certificat d'autonomie », « évaluation assistée » et renouvellement à chaque changement.
- p. 108, [197, 201] : MCP 2026-07-28 : les annotations d'outils sont-elles tenues pour non fiables (MUST) dans la page Tools, et la formule « should never » figure-t-elle au schéma?
- p. 109 et 111, [28] : OWASP Top 10 agentique : ASI09 traite-t-il de l'absence de confirmation, et ASI02 recommande-t-il l'approbation explicite par action à fort impact?
- p. 109-110, [307] : Meta, *Agents Rule of Two*, 31 octobre 2025 : la formulation de la branche [C] (« change state or communicate externally »).
- p. 111, [68] : A2A 1.0 emploie-t-il la RFC 8785 pour signer les cartes d'agent?
- p. 112, [93]/[309] : draft-ietf-wimse-aims-00 dit-il qu'une confirmation locale dans l'interface ne suffit pas, et cite-t-il CIBA en notant ses limites en cours d'exécution?
- p. 105 et 112, [290], [94] : libellés exacts du RIA, art. 14(3), art. 14(4)(e) et art. 26(2).
- p. 106, [8] : E-23 du BSIF en vigueur le 1er mai 2027; critères de « modification importante ».
- p. 112, [310] : statut final de CIBA Core 1.0 et sémantique du binding_message (affichage sur les deux appareils).


## audit_12.md
- p. 111 : A2A 1.0 emploie-t-il la RFC 8785 pour signer les cartes d'agent (signatures JWS d'AgentCard)? Trancher dans la spécification A2A 1.0 (a2a.proto et section sur les signatures), réf. [68].
- p. 112 : le brouillon WIMSE AIMS (draft-ietf-wimse-aims-00, 15 sept. 2026) dit-il qu'une confirmation locale dans l'interface ne suffit pas comme autorisation, et cite-t-il CIBA avec ses limites en cours d'exécution? Réf. [93], [309].
- p. 112 : RIA, art. 26, par. 2 (compétence, formation, autorité des personnes chargées du contrôle humain) : numérotation à confirmer dans le texte consolidé, réf. [94].
- p. 113 : dépôt `langchain-ai/agent-inbox` archivé en lecture seule depuis le 20 septembre 2026? Réf. [313]. Le billet LangChain sur les agents ambiants date-t-il de janvier 2025 et contient-il les trois patrons? Réf. [86].
- p. 113 : la recommandation de Microsoft de distinguer approbation et rétroaction et de persister l'état aux points d'approbation est-elle bien dans [9]?
- p. 114 : RIA modifié par le règlement (UE) 2026/1744 : application de l'art. 14 au 2 décembre 2027 (annexe III) et au 2 août 2028 (annexe I). L'annexe H.5 reconnaît que le texte n'a pas pu être relu sur EUR-Lex. Réf. [58], [315].
- p. 114 : OpenAI [291] recommande-t-il des expirations périodiques qui gardent l'agent à l'arrêt jusqu'à réautorisation? Contrôler la formulation exacte.
- p. 114 : OWASP T10 « Overwhelming Human in the Loop » [87]; ASI09 « Human-Agent Trust Exploitation » [28] et sa recommandation d'un résumé de risque en langage clair plutôt qu'une justification produite par le modèle (p. 114, Pourquoi de l'EXIG-AUT-19).
- p. 115 : Loi sur le privé, art. 90.1, par. 5° : le défaut visé par l'art. 12.1 y figure-t-il bien comme motif de sanction administrative pécuniaire? Réf. [56], [317].
- p. 115-116 : source de l'« interprétation gouvernementale » de l'art. 65.2 [318] : existence, date, et mention du mot « principaux »; absence de critères publiés par la CAI pour le secteur privé (encadré DROIT APPLICABLE, p. 116).
- p. 119 : dates de passage au niveau Graduated de SPIFFE (23 août 2022) et de SPIRE (22 août 2022) contre l'annonce de la CNCF du 20 septembre 2022, réf. [116], [117], [321]. L'annexe H.5 indique que SPIFFE et SPIRE n'ont pas été relus.
- p. 120 : draft-ietf-wimse-workload-identity-practices-07 du 22 sept. 2026, soumis à l'IESG le 30 juin 2026 : une version -07 postérieure à la soumission est plausible, mais à confirmer sur le Datatracker, réf. [323].
- p. 120 : création automatique d'une identité Entra Agent ID par Copilot Studio depuis juillet 2026 [48]; licence Microsoft Agent 365 requise pour l'accès conditionnel et la protection des identités [324].
- p. 121 : périodicité d'attestation de 6 à 12 mois et revue trimestrielle des orphelins recommandées par Microsoft [92]; livre blanc de l'OpenID Foundation annoncé le 7 octobre 2025, avec recommandation SCIM DELETE [311], [325].


## audit_13.md
- p. 124 : MCP 2026-07-28, autorisation : 403 `insufficient_scope`, autorisation incrémentale et plafond de tentatives [209].
- p. 124-125 : revendications des jetons d'accès Entra v2 (`typ`, `client_id` ou `azp`, `jti` ou `uti`) et absence d'`act` imbriqué dans l'OBO [326] (trancherait [13-08]).
- p. 125 : MCP 2026-07-28 exige-t-il que le client valide `iss` (RFC 9207)?
- p. 125 : draft-ietf-oauth-v2-1-16 du 3 septembre 2026, expirant le 7 mars 2027 [176, 327] (arithmétique cohérente à 185 jours).
- p. 126 : durées Entra (60 à 90 min, minimum 10 min, CAE jusqu'à 28 h) [331]; formule « quelques minutes ou moins » dans Transaction Tokens −11, § 6 [179].
- p. 126 et 127 : extensions MCP « OAuth Client Credentials » et « Enterprise-Managed Authorization » stables depuis la révision 2026-07-28 [217, 218]; ID-JAG −04 du 21 mai 2026 [177].
- p. 127 : états IETF de identity-chaining −17 (file de l'éditeur des RFC), spiffe-client-auth −02 (15 juin 2026), draft-oauth-ai-agents-on-behalf-of-user −02 (26 août 2025, expiré le 27 février 2026) [333-335].
- p. 127 : NCCoE, document de réflexion de février 2026; synthèse du 29 septembre 2026, « plus de 600 répondants », cas d'usage DevSecOps [337, 338].
- p. 128 : couverture d'Azure API Management (outils MCP seulement; A2A en JSON-RPC seulement) [108, 109]; Kong AI A2A Proxy, Gateway 3.14+, édition Enterprise, sans gestion d'état [111]; appartenance d'agentgateway et d'Agent Router à l'AAIF [36, 130, 339]; Omni Gateway, ancien Flex Gateway [341].
- p. 129 : documentation Vercel Sandbox (dépendance à SNI, terminaison TLS, règle générique) [342].
- p. 130 : disponibilité générale de Microsoft Agent 365 le 1er mai 2026 et actions de cycle de vie « à venir » [46]; date de finalisation de SSF 1.0 et CAEP 1.0 (29 août 2025?) et liste des événements CAEP [343, 344].
- p. 130-131 : chiffres d'agentgateway (500 000 req/s, 512 connexions, P99 < 0,2 ms à 30 000 req/s) [142]; FAQ et banc d'essai TrueFoundry [143, 144].
- p. 131 : date de publication du Top 10 agentique de l'OWASP (9 décembre 2025) [345]; T16 et T17 dans la v1.1 de « Threats and Mitigations » [87]; LLM Top 10 2026 (août 2026, agentivité excessive en LLM03) [346]; chiffres de MITRE ATLAS 2026.09 [352].

audit_13.md : 35 constats (0 BLOQUANT, 17 MAJEUR, 18 MINEUR)


## audit_14.md
- p. 133 : le NIST AI 100-2 E2025 attribue-t-il bien l'identifiant NISTAML.015 à l'injection d'invite indirecte? L'article du NCSC sur l'injection d'invite date-t-il bien de décembre 2025? Que dit exactement le guide du gouvernement du Canada sur l'IA agentique [353]?
- p. 133 : la règle de deux de Meta [307] est-elle datée du 31 octobre 2025, et ses propriétés [A], [B], [C] sont-elles formulées ainsi (« sensitive systems or private data »)?
- p. 133 : la correspondance NHI1 → ASI04, NHI2 → ASI02 et ASI06, NHI4 → ASI03 et ASI07 figure-t-elle dans la table officielle de [28]? (voir [14-28])
- p. 134 : Hines et al. [355] donnent-ils bien « plus de 50 % → moins de 2 % » sur des modèles GPT, avec un effet minime sur la tâche?
- p. 135 : Microsoft Learn [356] indique-t-il que les Prompt Shields analysent, en préversion, les réponses d'outils, et que la performance hors de l'anglais peut varier?
- p. 135-136 : Beurer-Kellner et al. [357] énumèrent-ils bien les six patrons, et signalent-ils que plan puis exécution ne protège pas les arguments? (voir [14-09])
- p. 136 : chiffres de CaMeL [101] : 77 % contre 84 % sur AgentDojo, selon la version de l'arXiv 2503.18813 (une version antérieure donnait peut-être 67 %). L'article est-il attribué à Google DeepMind et à l'ETH Zurich en mars 2025?
- p. 136 : Agent Security Bench [359] (ICLR 2025) : 84,30 % est-il bien le taux moyen d'ASR le plus élevé?
- p. 137 : Kata Containers relève-t-il toujours de l'OpenInfra Foundation en 2026, après son intégration annoncée à la Linux Foundation?
- p. 137 : la documentation de gVisor [361] dit-elle « aucun surcoût » sur l'exécution brute, ou un surcoût minime?
- p. 138 : versions des périphériques de Firecracker [133] : virtio-rng depuis la 1.4, virtio-pmem et virtio-mem depuis la 1.14, transport PCI depuis la 1.13. Le ballon (virtio-balloon) est-il omis à tort? Le filtre seccomp de 24 appels système et 30 ioctl relève-t-il du jailer ou du processus Firecracker [363]?
- p. 138 : la liste des GPU pris en charge par gVisor (T4, A100, A10G, L4, H100) et l'absence de validation des tampons DMA par nvproxy [368] sont-elles exactes? Les bacs à sable GPU de Modal ne sont-ils offerts qu'avec gVisor [369]?
- p. 138 : temps de reprise de Blaxel (< 25 ms) et d'E2B (~1 s) [366, 367].
- p. 139 : le document [208] (Security Best Practices, 2026-07-28) emploie-t-il SHOULD pour bloquer 169.254.0.0/16 côté client? Pour le comportement d'IMDSv2 [371, 372] (refus si l'en-tête X-Forwarded-For est présent, limite de sauts par défaut égale à 1), cette valeur par défaut vaut-elle pour toutes les images, AL2023 compris?
- p. 139 : draft-ietf-wimse-aims-00 [93] contient-il une interdiction (MUST NOT) d'accès du modèle aux justificatifs? Les « Client Best Practices » de MCP [204] décrivent-elles l'hôte courtier pour l'appel d'outils programmatique?
- p. 140 : le délai par défaut des bacs à sable Modal est-il de 5 minutes [369]? L'OWASP associe-t-il les listes d'autorisation sortantes à ASI02 ou à ASI05 [28]?
- p. 141 : kubernetes-sigs/agent-sandbox [137] relève-t-il de SIG Apps, avec les ressources Sandbox, SandboxTemplate, SandboxWarmPool et SandboxClaim en v1beta1? RuntimeClass est-il stable depuis la 1.20 (node.k8s.io/v1)?

audit_14.md : 31 constats (1 BLOQUANT, 12 MAJEUR, 18 MINEUR)


## audit_15.md
- p. 141 : `kubernetes-sigs/agent-sandbox` relève-t-il de SIG Apps, et ses ressources Sandbox, SandboxTemplate, SandboxWarmPool et SandboxClaim sont-elles en `v1beta1` (et non en `v1alpha1`)? [137]
- p. 141 : la date du 1er avril 2025 du billet d'Invariant Labs sur l'empoisonnement d'outil et la substitution après approbation [220].
- p. 141 : la numérotation du MCP Top 10 de l'OWASP (MCP03 empoisonnement, MCP04 chaîne d'approvisionnement, MCP09 serveurs fantômes) [222] et celle de l'AST10 (AST01, AST02, AST07) [374].
- p. 141 : Hou et coll. décrivent-ils bien quatre phases (création, déploiement, exploitation, maintenance) et 16 scénarios répartis entre quatre types d'attaquants? Une version antérieure de l'article comptait trois phases (création, exploitation, mise à jour). Préciser la version citée [224].
- p. 142 : l'exclusion du champ `signatures` du contenu signé JCS et la règle « au moins une signature » de la spécification A2A 1.0 [68]; le mécanisme de liaison de la clé (`jku`/`kid`) qu'elle prévoit.
- p. 142 : « ASI02 » recommande-t-il bien les noms pleinement qualifiés avec versions épinglées contre le typosquattage [28]?
- p. 143 : la portée de l'art. 25(4) du RIA après le règlement (UE) 2026/1744 [61, 375].
- p. 143 : la date du 27 juillet 2025 du guide de l'OWASP sur la sécurisation des applications agentiques (version 1.0) [377].
- p. 143 : l'existence et l'intitulé des techniques AML.T0110, AML.T0124 et AML.T0133 de MITRE ATLAS [352].
- p. 144 : le principe 11 de l'Énoncé de principes québécois et sa mention de l'IA agentique et des mécanismes d'arrêt d'urgence [379].
- p. 145 : les dates v1.41.0 (28 avril 2026), v1.41.1 (11 mai 2026) et v1.42.0 (12 juin 2026); le déplacement vers `semantic-conventions-genai`; la règle de stabilité « v1.36.0 ou antérieure par défaut »; l'instrumentation Python d'OpenAI à la v1.30.0 [119, 180, 381-385].
- p. 146 : MCP 2026-07-28 réserve-t-il bien `traceparent`, `tracestate` et `baggage` dans `_meta` [162]?
- p. 147-148 : `gen_ai.agent.version` ajouté en v1.40.0 [180]; `gen_ai.provider.name` qui remplace `gen_ai.system` en v1.37.0 [387]; les niveaux du tableau 41 (notamment `gen_ai.agent.*` « Conditionnels »); les valeurs de `gen_ai.operation.name` en v1.41.0, dont `invoke_workflow` [119, 120].
- p. 149 : v1.38.0 pour `gen_ai.tool.call.arguments`/`result` [391]; la variable `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` et ses quatre valeurs sur la branche principale [392]; la stabilité Beta/Alpha du processeur `redaction` et la couverture des corps de journaux [141]; le statut de W3C Baggage (recommandation candidate) [393].
- p. 150 : la date d'application du 2 décembre 2027 pour l'annexe III (art. 113 modifié) [394]; ISO/IEC 42001 A.6.2.8 [395].
- p. 152 : l'énoncé d'AutoGenBench sur la répétition et l'isolation [279]; le juge d'Anthropic qui rend un score de 0,0 à 1,0 et un verdict en un seul appel [17]; les attributs de `gen_ai.evaluation.result` [396].

audit_15.md : 33 constats (1 BLOQUANT, 16 MAJEUR, 16 MINEUR)


## audit_16.md
- p. 154 [399] : grille d'Anthropic d'octobre 2026 : Haiku 5.5 à 0,10 / 0,50 $ US (≤ 100 000 jetons) et 0,50 / 2,50 $ US au-delà; Fable 5.1 à 10 / 50 $ US, avec ou sans majoration au-delà de 100 000 jetons; segmenteur des modèles 4.7 et suivants donnant « environ 30 % » de jetons en plus; majoration de 10 % pour l'inférence restreinte aux États-Unis et pour les points de terminaison régionaux des partenaires.
- p. 154 [401] : multiplicateurs de lecture en cache de 0,05 (Opus 5.5, Sonnet 5.5) et 0,025 (Fable 5.1); écriture à 1,25 (5 min) et à 2 (1 h).
- p. 154 [402] : seuil de 1 024 jetons « pour GPT-5.6 et les suivants ». Le même seuil s'appliquait déjà aux modèles antérieurs depuis 2024 : la formulation laisse-t-elle croire à tort à une nouveauté?
- p. 154 [400] : absence de zone canadienne dans la résidence des données de l'API d'Anthropic, et prise en charge éventuelle de la restriction géographique pour les lots (FIN-08).
- p. 154 [397] : le chiffre « plus de 280 fois » (AI Index 2025) est-il repris, révisé ou contredit dans l'édition 2026?
- p. 154 [205] : 58 outils pour environ 55 000 jetons (billet du 24 novembre 2025).
- p. 155 [403] : Belcak et coll. (2025) est un article de position; les « 40 à 70 % » sont-ils des estimations des auteurs sur trois études de cas (MetaGPT, Open Operator, Cradle) plutôt que des mesures?
- p. 155 [53] : Copilot Studio : 5 crédits par action d'agent, 10 crédits par 1 000 jetons pour un modèle de raisonnement, désactivation des agents personnalisés au-delà de 125 % de la capacité prépayée.
- p. 155 [55] : Agentforce : crédit à 0,005 $ US, environ 0,10 $ US par action standard.
- p. 156 [404] et p. 157 [405] : niveau de risque « élevé » de GENCOST05-BP01; le Generative AI Lens retient-il bien « trois principes », ou cinq pratiques (GENCOST01 à 05)?
- p. 156 [107] : comportement de `llm-token-limit` (compteurs par passerelle ou région, estimation en diffusion, dépassement en concurrence).
- p. 157 [119] : la convention v1.41.0 demande-t-elle (SHOULD) que `gen_ai.usage.input_tokens` inclue les jetons servis depuis le cache, et nomme-t-elle l'attribut `gen_ai.usage.cache_read.input_tokens`?
- p. 157 [9] : le Centre d'architecture Azure recommande-t-il explicitement un modèle proportionné par agent et la mesure des jetons par agent et par exécution?
- p. 158 [408, 409] : FOCUS 1.4 sans colonne native de jetons : la colonne ConsumedUnit ne peut-elle pas porter des « tokens »? Granularité des exports FOCUS des fournisseurs d'inférence (par clé, par espace, par requête).
- p. 160 [56] : Loi sur l'accès, art. 8 et 8.1 (responsable et comité obligatoire), en complément des art. 63.3 et 63.5.
- p. 160 [90] : Entra Agent ID distingue-t-il aussi un rôle « manager » en plus du sponsor et de l'owner?

audit_16.md : 31 constats (1 BLOQUANT, 14 MAJEUR, 16 MINEUR)


## audit_17.md
- p. 164 : le registre officiel MCP est-il toujours « en préversion » au 27 octobre 2026, et sa documentation dit-elle ne pas prendre en charge les serveurs privés et recommander des sous-registres d'entreprise [25, 43]? (Lancement en préversion le 8 septembre 2025 : conforme à ce que je sais.)
- p. 164 : E-23 du BSIF, « en vigueur le 1er mai 2027 », exige-t-elle un inventaire couvrant les modèles des fournisseurs et une cote de risque qui module la gouvernance [8]? Le texte de l'E-23 dit-il « revue indépendante » sur modification (p. 167), ou seulement « critères de modification importante » (EXIG-AUT-05)?
- p. 165 : Microsoft Agent 365 en disponibilité générale le 1er mai 2026, synchronisation avec Bedrock et Google Cloud en préversion publique à cette date [46]; Amazon Bedrock AgentCore Registry (fonctions décrites) [102]; Azure API Center comme registre MCP privé [108]; annonce ServiceNow du 5 mai 2026 (30 intégrations, coupe-circuit) [47].
- p. 166 : Copilot Studio crée-t-il automatiquement une identité Entra Agent ID pour chaque nouvel agent depuis juillet 2026 [48]?
- p. 167 : dans Entra Agent ID, la désactivation d'un « agent identity blueprint » bloque-t-elle toutes les identités dérivées [92]? La recommandation Microsoft « 6 à 12 mois » et « chaque trimestre » est-elle exacte [92]?
- p. 164 et 167 : Feng, McDonald et Zhang (niveaux d'autonomie, « certificat d'autonomie » délivré par un tiers et renouvelé à chaque changement) [83] : conforme à ce que je sais, à confirmer.
- p. 168 : le livre blanc de l'OpenID Foundation recommande-t-il un retrait propagé par SCIM DELETE [311]? Les événements CAEP cités [344] (CAEP 1.0 final du 29 août 2025)?
- p. 169 : politique de cycle de vie MCP (SEP-2596) : douze mois, ou 90 jours en retrait accéléré, « pour un risque de sécurité actif » ou « exceptionnel » [34, 196]? OAuth 2.1 toujours Internet-Draft (draft-16, septembre 2026) [176]? Conventions GenAI d'OpenTelemetry toujours au niveau Development [181, 188]?
- p. 169 : Cadre européen d'interopérabilité sur la gestion du changement [157].
- p. 170 : processus d'admission de l'AAIF (étapes énumérées) [42, 263]; « huit groupes de travail » de l'AAIF [40]; lancement par le CAISI de l'AI Agent Standards Initiative le 17 février 2026 [411]; synthèse du NCCoE du 29 septembre 2026 (« plus de 600 intervenants ») [338], que l'annexe H.5 dit non rouverte; brouillons WIMSE sur la délégation [336].
- p. 165-167 : NIST AI RMF GOVERN 1.6, 1.7, 6.1, 6.2 et MANAGE 2.4 [74] : libellés conformes à ce que je sais; OWASP NHI Top 10, NHI1 = Improper Offboarding [91] : conforme.

audit_17.md : 35 constats (2 BLOQUANT, 14 MAJEUR, 19 MINEUR)


## audit_18.md
- p. 173 : dates d'entrée en vigueur de la Loi 25, dont les « dispositions accessoires » du 22 septembre 2021 [7, 56].
- p. 174 : guide EFVP de la CAI, « version 3.1, avril 2024 », et citations « améliorer un modèle d’intelligence artificielle » et « rendre une décision automatisée » [413].
- p. 175 : cadre fédéral de souveraineté numérique (novembre 2025) et affirmation qu'aucun cas documenté d'accès étranger n'a été relevé [418]; libellé de 18 U.S.C. § 2713 [417].
- p. 176 : art. 90.1, par. 5°, comme motif visant l'art. 12.1 [56, 317].
- p. 177 : position de la CAI sur l'impossibilité d'anonymiser les données génétiques, biométriques et de géolocalisation [420]; IA-RI-2025-003-OP, en vigueur le 5 décembre 2025, et son contenu [421]; Énoncé de principes (édition 2025), 12 principes, principe 11 sur l'IA agentique [379], et caractère contraignant de l'Énoncé pour les organismes publics (p. 178).
- p. 178 : Énoncé de politique de souveraineté numérique (février 2026) [422]; outils gouvernementaux [423]; absence de sanction de la CAI liée aux décisions automatisées [424]; rapport quinquennal de la CAI du 11 juin 2026 et ses 74 recommandations [425]; récidive à l'art. 92.1 ([18-23]).
- p. 178 : C-36, dépôt le 15 juin 2026, art. 62, 63, 113 et 114, plafond de 10 M$ ou 3 % [430, 431]; Directive sur la prise de décisions automatisée, champ « après le 1er avril 2020 » et EIA à 65 et 41 questions [432, 433].
- p. 179 : Guide fédéral sur l'IA agentique (2026) [353]; avis du BSIF sur les incidents « en vigueur depuis le 13 août 2021 » [434]; Ligne directrice IA de l'AMF (avril 2026, en vigueur le 1er mai 2027), non relue selon H.5; Loi concernant la cybersécurité (L.C. 2026, ch. 9, sanctionnée le 15 juin 2026), en particulier la présence des systèmes bancaires parmi les services critiques ([18-11]) [439]; état de C-22 au Sénat [440].
- p. 180 : règlement (UE) 2026/1744 du 8 juillet 2026 (numéro, date, entrée en vigueur le 27 juillet 2026), reports au 2 décembre 2027 et au 2 août 2028, nouvelles interdictions au 2 décembre 2026, bac à sable au 2 août 2027 (cités en partie à [57] plutôt qu'au texte; H.5 : EUR-Lex non relu) [57, 58, 443]; sort de l'art. 4 (maîtrise de l'IA) après l'omnibus ([18-10]).
- p. 182 : NIST AI RMF « en cours de révision » dans le cadre du plan d'action américain [99, 448].


## audit_19.md
- p. 182-183 : AI RMF « en cours de révision » dans le cadre du plan d'action américain, « examen formel au plus tard en 2028 » (NIST AI 100-1, § « Next steps »; page [448]).
- p. 183 : CAISI AI Agent Standards Initiative « lancée le 17 février 2026 »; COSAiS renommé « COSIS, Control Overlays for Super Intelligence Systems » et date réelle du renommage [411, 455]; note de concept du 7 avril 2026 sur un profil pour les infrastructures critiques [456].
- p. 183 : ISO/IEC 42001 publiée le 18 décembre 2023; ISO/IEC 22989, terme « AI agent » au 3.1.1; ISO/IEC 42006:2025 [395, 451, 453].
- p. 185 : délai transitoire de l'art. 50(2) au 2 décembre 2026 selon le règlement (UE) 2026/1744 (voir aussi H.4); art. 27(4) « tel que modifié » (p. 188) [57, 461].
- p. 186 : Specter Aviation c. Laprade, 2025 QCCS 3521, sanction de 5 000 $ au titre de l'art. 342 C.p.c. [458].
- p. 186 : CAI 2024-2025 : 514 avis, hausse de 16 %, 80 % du secteur privé, 251 accès non autorisés [424].
- p. 187 : nombre d'éléments de l'avis à la CAI (« onze ») selon le Règlement sur les incidents de confidentialité, et numérotation des articles cités dans le pourquoi d'EXIG-CON-24 (« articles 7 et 8 du règlement » : registre et conservation figurent peut-être aux art. 6 et 7) [460].
- p. 187 : avis du BSIF sur le signalement des incidents liés à la technologie et à la cybersécurité : date de la version en vigueur (« 2021 ») et délai de 24 heures [62].
- p. 187 : LPRPDE : conservation du registre pendant 24 mois; avis aux organisations susceptibles de réduire le risque (art. 10.2).
- p. 190 : AAIF : membres Platine; A2A projet hébergé le 17 août 2026; candidature d'AGNTCY sans décision au 27 octobre 2026 [4, 5, 35, 37, 42].
- p. 190 : exemples du tableau 53 : Azure API Management (outils MCP seulement, A2A en JSON-RPC seulement) [108, 109]; Kong AI A2A Proxy 3.14 [111]; Agentforce (un niveau, sept sous-agents) [49]; Entra Agent ID d'office depuis juillet 2026 [48]; Agent 365 [46, 324]; Copilot Studio, seuil de 125 % [53]; extensions MCP à préfixe DNS inversé, désactivées par défaut [169].


## audit_20.md
- p. 195 et 202 : le règlement (UE) 2026/1744 modifie-t-il bien l'art. 25(4) et fixe-t-il le 2 décembre 2027 (annexe III) et le 2 août 2028 (annexe I)? Le texte EUR-Lex n'a pas été rouvert (H.5).
- p. 194 : l'avis du BSIF sur les incidents fixe-t-il un point de départ au délai de 24 h (constat, détermination de la gravité)? C'est ce que conteste « sans fixer le point de départ ».
- p. 193 : A2A 1.0 prévoit-il une période minimale de maintien des versions dépréciées (EXIG-APP-07)?
- p. 193 : RFC 8693, § 4.1, statut des revendications `act` imbriquées (« informational only »?).
- p. 199 : ISO/IEC 42001:2023, l'art. 6.1.3 exige-t-il la déclaration d'applicabilité? Les intitulés A.5, A.6.2.6, A.6.2.8 et A.10 sont-ils exacts? ISO/IEC 42006:2025 est-elle bien publiée?
- p. 193-194 : libellés des art. 11, 12.1, 17, 18.3 et 32 de la Loi sur le privé (conservation d'un an, droit d'observation, « extérieur du Québec », « tentative de violation », 30 jours).
- p. 194 : document fédéral [418] (stockage au Canada et compétence étrangère, aucun cas documenté) : titre et date.
- p. 198 : Feng, McDonald et Zhang [83] et Morris et al. [302] soutiennent-ils l'autonomie comme décision de conception et un niveau de déploiement inférieur au maximum possible?
- p. 199 : intitulés NIST AI RMF de MAP 3.5, MEASURE 2.7 et MANAGE 4.1, et absence de gabarit de profil (« does not prescribe profile templates »).


## audit_21.md
- p. 204 et 206, [2] Gartner, 28 avril 2026 : « plus de 150 000 agents » par entreprise du Fortune 500 d'ici 2028, contre « moins de 15 en 2025 », et constat sur l'IA fantôme. Population, méthode et formulation exacte, et rôle de [467] (Computerworld) comme relais.
- p. 206, [95] Gartner, 26 mai 2026 : « 40 % des entreprises rétrograderont ou désactiveront des agents autonomes d'ici 2027 ».
- p. 206, [3] Gartner, 25 juin 2025 : plus de 40 % de projets annulés d'ici la fin de 2027. Je le crois exact; à confirmer.
- p. 206, [275] Phillips (Anthropic, 23 janvier 2026) : fourchette « 3 à 10 fois » et son contexte.
- p. 202, [8] E-23 : la ligne directrice vise-t-elle les modèles « à risque non négligeable »? Exige-t-elle que la validation soit faite à la date d'entrée en vigueur, ou seulement le cadre de gestion et l'inventaire?
- p. 202, [57, 58] règlement (UE) 2026/1744 (du 8 juillet 2026, JO du 24 juillet 2026) : dates du 2 décembre 2027 (annexe III) et du 2 août 2028 (annexe I), et maintien ou modification de l'art. 111(2). Le texte n'a pas pu être lu le 1er novembre selon H.5.
- p. 206, [76] IMDA, Model AI Governance Framework for Agentic AI v1.5 : la recommandation de surveiller conjointement le taux d'approbation et le temps de réponse.
- p. 206, [407] FinOps Foundation : la recommandation de commencer par la refacturation indicative (showback).
- p. 204, [91] OWASP NHI Top 10 2025 : NHI2 (fuite de secrets), NHI7 (secrets de longue durée) et NHI9 (réutilisation). Je les crois exacts.
- p. 206, [314] : le biais d'automatisation « touche les novices comme les experts » et « ne se prévient pas par la seule formation » (vraisemblablement Parasuraman et Manzey, 2010).
- p. 212, [92] Microsoft Entra Agent ID : l'attestation du parrain tous les 6 à 12 mois.
- p. 203 : le NIST AI RMF prévoit-il un examen formel « au plus tard en 2028 »? Je le crois exact.
- p. 203 : les dates des vacances de la construction 2027 au Québec (CCQ).

audit_21.md : 31 constats (2 BLOQUANT, 10 MAJEUR, 19 MINEUR)


## audit_22.md
- p. 212 : Feng, McDonald et Zhang [83] décrivent-ils un « certificat d'autonomie » renouvelé « à chaque changement de l'agent ou de son environnement », et délivré par un tiers?
- p. 212 : les bonnes pratiques de Microsoft Entra Agent ID [92] prévoient-elles une attestation par le parrain tous les 6 à 12 mois?
- p. 212 : le guide d'EFVP de la CAI [413] recommande-t-il la mise à jour de l'EFVP lorsqu'un projet change?
- p. 216-217 : la révision MCP 2026-07-28 définit-elle `x-mcp-header` dans `inputSchema` et l'en-tête `Mcp-Param-<Nom>`? JSON Schema 2020-12 y est-il le dialecte par défaut?
- p. 219 : A2A 1.0 (a2a.proto) compte-t-il exactement huit champs obligatoires dans `AgentCard`? Les noms `supportedInterfaces`, `protocolBinding`, `extendedAgentCard`, `securityRequirements` (`schemes`/`list`) et le schéma mTLS sont-ils exacts? À quelle section de la spécification renvoie « 8.4.1 »?
- p. 219 : la RFC 8725 met-elle en garde contre le suivi de `jku`/`x5u`, et à quelle section?
- p. 220 : l'extension CloudEvents Data Classification admet-elle la valeur `internal`, et quelles autres? `service_account` est-il une valeur d'`authtype` de l'extension Auth Context?
- p. 220 : la liaison Kafka de CloudEvents 1.0.2 [250] décrit-elle le « Key Mapper » comme facultatif, et exclut-elle `datacontenttype` des en-têtes `ce_` au profit de `content-type`?
- p. 221 : la RFC 9068 exige-t-elle exactement `iss`, `exp`, `aud`, `sub`, `client_id`, `iat` et `jti`, et la RFC 8693 réserve-t-elle les `act` imbriqués à l'information (je le crois, avec une confiance élevée)?

audit_22.md : 29 constats (1 BLOQUANT, 7 MAJEUR, 21 MINEUR)


## audit_23.md
- p. 224 : OWASP Top 10 for Agentic Applications 2026 [28] recommande-t-il expressément des journaux d'audit « immuables et signés »? Trancher sur le texte de l'entrée concernée.
- p. 224 : dates d'application RIA (annexe III le 2 décembre 2027, annexe I le 2 août 2028) et article 113 modifié par le règlement (UE) 2026/1744 : vérifier sur EUR-Lex, puisque [94] et [394] (Future of Life Institute) ne le portent peut-être pas.
- p. 224 : art. 26, par. 6 du RIA, « au moins six mois [...] durée adaptée à la destination » : vérifier la formulation du texte consolidé.
- p. 221 : RFC 9396, est-il admis d'employer authorization_details dans un JWT qui n'est ni une demande ni un jeton d'accès, avec des champs propres au type (fournisseur_id, montant_total_cad)? Vérifier au § 2 de la RFC (champs propres au type permis).
- p. 221 : CIBA Core 1.0 [310] produit des jetons d'identité ou d'accès, pas un « approbation+jwt ». Vérifier que le cadre présente bien l'émission du jeton d'approbation comme une étape propre au service d'approbation, et que binding_message peut porter h.
- p. 232 : OWASP Agentic AI Threats and Mitigations [87], T10 « Overwhelming Human in the Loop » : vérifier l'intitulé et le numéro.

audit_23.md : 22 constats (1 BLOQUANT, 10 MAJEUR, 11 MINEUR)


## audit_24.md
- p. 234 : « interprétation gouvernementale de l'article 65.2 » (intervention humaine mineure) : confirmer le texte et la date de [318].
- p. 234 : CAEP du Shared Signals Framework [344] : statut final (1.0) et date.
- p. 236 : OWASP Non-Human Identities Top 10 (2025) [470] : édition et intitulés NHI1-NHI10.
- p. 236 : brouillon IETF Idempotency-Key, version -08 du 22 octobre 2026 [78] : existence et numéro.
- p. 238 : OAuth 2.1, version -16 de septembre 2026 [176] (expiration annoncée le 7 mars 2027, p. 52) : vérifier sur datatracker.
- p. 238 : MCP « versionné par date », annonce du 25 novembre 2024 et transfert du 9 décembre 2025 [20, 34] (conforme à mes connaissances); révision 2026-07-28 sans état [33] : à confirmer.
- p. 239 : OWASP Top 10 for Agentic Applications publié le 9 décembre 2025 [28, 345] : date exacte de publication (9 ou 10 décembre).
- p. 239 : « parrain » (sponsor) de Microsoft Entra Agent ID : terminologie du produit à vérifier.
- p. 240 : registre officiel MCP « en préversion » au 27 octobre 2026 [43] : statut à cette date.
- p. 240 : règlement (UE) 2026/1744 : numéro, dates de report (2 décembre 2027, annexe III; 2 août 2028, annexe I).
- p. 240 : brouillon IETF WIMSE « AI Identity Management System » (AIMS) : existence et rattachement au groupe WIMSE.
- p. 240 : ISO/IEC 42006:2025 (exigences pour les organismes de certification d'un SMIA) : date de publication.
- p. 241 (couture) : « règle de deux » de Meta, 31 octobre 2025 [307] : date et libellé exact de la propriété [C].

audit_24.md : 19 constats (0 BLOQUANT, 3 MAJEUR, 16 MINEUR)


## audit_25.md
- p. 244, no 17 : liste exacte des périphériques dans l'article NSDI '20 de Firecracker (quatre, ou cinq avec vsock?).
- p. 244, no 16 : chiffres de Kim et Liu, billet de 2026 et versions arXiv ([273], [274]); 3 à 10 fois selon [275].
- p. 244, no 19 : dans l'ASB, 84,30 % est-il le taux moyen d'attaque mixte le plus élevé, et non un taux de « détournement d'objectif »?
- p. 244, no 20 et p. 250, [11] : ratio de 82 pour 1 et date du 23 avril 2025 (rapport CyberArk 2025).
- p. 244, no 23 : Specter Aviation c. Laprade (Cour supérieure, art. 342 C.p.c., 5 000 $); absence d'amende supérieure à 500 000 $ en vertu de la Loi 25.
- p. 244, no 25 : numéro du règlement (UE) 2026/1744 et échéances du 2 décembre 2027 et du 2 août 2028 (EUR-Lex; H.5 signale lui-même qu'il n'a pas pu les rouvrir).
- p. 244, no 28 : Menlo Ventures, 37 G$ US contre 11,5 G$ US.
- p. 244, no 29 : arXiv 2506.02153 (Belcak et al.) et facteur de 10 à 30 en coût de calcul.
- p. 243, no 9 : disponibilité générale de MCP dans Copilot Studio le 29 mai 2025 ([300]).
- p. 243, no 12 : ajout de gen_ai.agent.version en v1.40.0 et contenu en opt-in depuis v1.37.0 (CHANGELOG [180]).
- p. 243, no 2 : la révision MCP 2026-07-28 compte-t-elle toujours cinq propriétés de ToolAnnotations?
- p. 243, no 4 : code d'erreur −32020 et HTTP 400 pour la non-concordance entre en-têtes et corps (Streamable HTTP, 2026-07-28).
- p. 246, no 41 : accès bloqué à arXiv 2506.12469 (invraisemblable).

audit_25.md : 16 constats (0 BLOQUANT, 5 MAJEUR, 11 MINEUR)
