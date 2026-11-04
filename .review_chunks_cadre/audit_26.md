# Audit chunk_26 — pages 251-262

## Synthèse
Le chunk couvre les références [12] à [253] de l'annexe G. Les entrées sont dans l'ensemble exactes (auteurs, dates et identifiants des RFC, articles arXiv, NIST et annonces de 2025 concordent avec ce que je connais), et chacune des 242 entrées est appelée au moins une fois dans le corps. Les trois défauts les plus graves : (1) des blogues de positionnement d'éditeurs ([44], [45], [167]) restent cités, contre la règle du § 1.7 et du tableau 66, et l'un d'eux fonde les critères d'acceptation de la passerelle; (2) des obligations du RIA reposent sur un site agrégateur (Future of Life Institute, [62], [94]), parfois seul, et [62] est appelée pour une affirmation qu'elle ne contient pas; (3) des doublons font passer une même source pour deux, jusque dans un même appel ([73, 112], [173, 247, 248], [178, 218]).
Note de méthode : les pages 251-252 et 261-262 sont des pages de recouvrement de part et d'autre (chunks 25 et 27). Elles ne sont donc propres à aucun chunk. J'y rapporte les constats sur les entrées, marqués « [recouvrement] », pour que la consolidation élimine les doublons.

## Constats

### [26-01] [MAJEUR] Blogues de positionnement d'éditeurs cités malgré le § 1.7, et repris comme critères d'acceptation
- **Axe** : A
- **Localisation** : annexe G, p. 252 [recouvrement], [44] « TrueFoundry (2026). Governing AI Agents Across Multiple Platforms. https://www.truefoundry.com/blog/… » et [45] « Dhimate, Y. (2026). A Framework for Architecting Agent Control Plane. MuleSoft Blog ». Appels : p. 19, 33, 129, 190, 191. P. 129 : « Le cadre retient ces sept portes comme critères d'acceptation d'une passerelle d'agents (choix du cadre) ».
- **Diagnostic** : le § 1.7 (p. 14) dit : « Seules les catégories A et B sont citées ». Le tableau 66 classe en C le « Blogue de positionnement » et prescrit « Jamais cité ». Or le corps reconnaît lui-même la nature de ces sources (p. 19 : « Ces fournisseurs ont un intérêt commercial dans la thèse »). Ce sont des billets d'opinion sur une catégorie de produits que vendent leurs auteurs, et non la documentation d'un éditeur sur son propre produit (catégorie A). Le cadre les cite donc en connaissance de cause, contre sa propre règle. Pire, à la p. 129, les « sept portes » du billet [45] deviennent les critères d'acceptation d'une passerelle d'agents, qui portent l'EXIG-ARC-01 et le chapitre 13. Une exigence repose ainsi sur une source C.
- **Contre-exemple ou scénario de défaillance** : en approvisionnement (ch. 13), un fournisseur concurrent de MuleSoft conteste la grille au motif que ses critères d'acceptation viennent du billet marketing d'un soumissionnaire. Le cadre ne peut pas invoquer son propre § 1.7 pour se défendre.
- **Correctif proposé** : soit retirer [44] et [45] et présenter les sept portes comme un choix du cadre, sans attribution; soit ajouter au tableau 66 une catégorie explicite, « argument d'éditeur, cité comme tel, jamais à l'appui d'une exigence », et corriger le § 1.7. Dans les deux cas, citer pour la thèse « la gouvernance native s'arrête à la frontière » des faits de catégorie A (par exemple [46] et [47], déjà appelées p. 19).
- **Confiance** : vérifié dans le texte (règle, entrées et appels)

### [26-02] [MAJEUR] Obligations du RIA appuyées sur un agrégateur, parfois seul, et un appel qui ne soutient pas l'affirmation
- **Axe** : A
- **Localisation** : p. 253, [62] « Future of Life Institute (2026). Article 3: Definitions. https://artificialintelligenceact.eu/article/3 »; p. 255, [94] « Future of Life Institute (2026). Article 26: Obligations of Deployers… ». Appels : p. 112, « (art. 26, par. 2)[94] », seule source du « Pourquoi » d'une exigence DOIT (approbateurs habilités); p. 224, « (art. 26, par. 6)[94, 394] », deux pages du même agrégateur; p. 187, tableau des délais de notification, « RIA[56, 62, 426, 427, 434, 459, 460] ».
- **Diagnostic** : artificialintelligenceact.eu est un site tiers qui reproduit le règlement et le commente. Ce n'est pas le texte officiel : c'est au mieux une source B, et le tableau 66 dit d'une source B « jamais seul pour une exigence ». Le texte officiel est pourtant déjà en bibliographie ([61], EUR-Lex), et son entrée énumère précisément les articles 3, 26 et 113. Le même procédé se répète hors du chunk ([375], [394], [459]). Par ailleurs, au tableau de la p. 187, [62] (la page « Article 3: Definitions ») est appelée à l'appui de délais de notification d'incidents graves (15 jours, 10 jours, 2 jours), qui relèvent de l'article 73 : l'entrée ne contient pas l'affirmation. [459] la couvre probablement, ce qui rend [62] superflue à cet endroit.
- **Contre-exemple ou scénario de défaillance** : le site agrégateur affiche la version initiale de l'article 113, et non celle que modifie le règlement (UE) 2026/1744, ou une traduction non officielle. Le lecteur qui suit [94] lit alors une date d'application fausse. La p. 150 combine pourtant [58, 61, 94, 394] précisément sur la date modifiée.
- **Correctif proposé** : citer les articles par [61] (version consolidée sur EUR-Lex) et [58], et ne garder les pages du Future of Life Institute qu'en complément, sinon les supprimer. Retirer [62] de l'appel de la p. 187. Ajouter l'article 73 à la liste d'articles de [61] si [61] doit le couvrir.
- **Confiance** : vérifié dans le texte (entrées et appels); la nature du site est une connaissance générale

### [26-03] [MAJEUR] Doublons : une même source sous plusieurs numéros, parfois dans le même appel
- **Axe** : A
- **Localisation** :
  - [73] et [112] : NIST SP 800-207 (mêmes auteurs et même année; DOI pour l'un, csrc pour l'autre); appel commun « [73, 112] » p. 118.
  - [74] et [99] : NIST AI 100-1 (« NIST (2023-01) » pour l'un, « National Institute of Standards and Technology (2023) » pour l'autre).
  - [69], [70] et [118] : RFC 8693, trois fois.
  - [173] et [248] : CloudEvents 1.0.2; appel « [173, 247, 248] » p. 76.
  - [178] et [218], avec [217] : Enterprise-Managed Authorization; appel « [178, 218] » p. 62.
  - [235] et [240] : « What's New in A2A Protocol v1.0 » (copie GitHub et copie du site).
  - [30] et [229] : les publications A2A, la v0.3.0 étant comprise dans les deux.
  - [36] et [106] : le même événement (9 septembre 2026), appel « [36, 106] » p. 35.
- **Diagnostic** : la méthode (§ 1.7, annexe F, thèse T8) se prévaut de décomptes précis : 473 références, 705 sources admissibles. Les doublons gonflent ces décomptes. Un appel du genre « [73, 112] » donne en outre l'apparence d'une corroboration par deux sources, alors qu'il s'agit d'un seul document. Les formats divergents entre les entrées doublées (auteur « NIST » ou nom développé; date « 2023-01 » ou « 2023 ») montrent qu'elles ont été ajoutées par des passes différentes, sans dédoublonnage.
- **Contre-exemple ou scénario de défaillance** : un auditeur recompte les sources indépendantes qui appuient la définition de la confiance zéro (p. 118) et en trouve une, non deux. Il recompte ensuite les 473 références et obtient un chiffre inférieur, ce qui fragilise le bilan de l'annexe F.
- **Correctif proposé** : fusionner chaque groupe sous un seul numéro, en gardant le DOI ou l'URL canonique de l'éditeur. Pour RFC 8693, garder une seule entrée et préciser la section dans l'appel (« [69, § 4.1] »). Mettre à jour les décomptes de l'annexe F.
- **Confiance** : vérifié dans le texte

### [26-04] [MINEUR] Blogue personnel et page « About » comme seul appui du « Pourquoi » de l'EXIG-EVT-01
- **Axe** : A
- **Localisation** : p. 258, [167] « Waehner, K. (2026). MCP vs. REST/HTTP API vs. Kafka… https://www.kai-waehner.de/blog/… »; p. 262, [246] « Waehner, K. (s. d.). About. kai-waehner.de ». Appels : p. 48 et p. 76 (« les deux approches se complètent[167, 246] », juste avant l'EXIG-EVT-01).
- **Diagnostic** : [167] est un blogue personnel. Son auteur est lié à un éditeur de diffusion en continu (à vérifier), ce qui en fait un blogue de positionnement au sens du tableau 66. La page « About » [246] ne soutient aucune affirmation : elle sert seulement à hisser l'auteur au rang d'« expert reconnu » (catégorie B), ce qui revient à se qualifier soi-même. Même admise en B, la source ne peut « jamais [être] seul[e] pour une exigence ». Or l'affirmation centrale (« MCP n'offre ni garantie de livraison ni cohérence ») porte sur MCP et se démontre par la spécification ([198], [190]).
- **Contre-exemple ou scénario de défaillance** : un lecteur conteste l'EXIG-EVT-01. La seule justification externe qu'il trouve est le billet d'un promoteur de Kafka, appuyé par sa propre biographie.
- **Correctif proposé** : appuyer l'affirmation sur la spécification MCP (transports et absence de garantie de livraison) et sur [140]. Retirer [246], et garder [167] au plus comme illustration.
- **Confiance** : vérifié dans le texte; l'affiliation de l'auteur est à vérifier

### [26-05] [MINEUR] Définition du glossaire tirée d'un billet d'éditeur, sans date précise
- **Axe** : A
- **Localisation** : p. 255, [86] « Chase, H. (2025). Introducing ambient agents. LangChain ». Appels : p. 24, p. 34, p. 112 (« son billet de janvier 2025 ») et p. 231 (glossaire, « définition de LangChain »).
- **Diagnostic** : un terme du glossaire (annexe E) est défini par le billet de lancement d'un concept commercial. Selon le tableau 66, la catégorie se discute (B au mieux). L'entrée donne « (2025 » sans mois, alors que le corps précise « janvier 2025 ».
- **Correctif proposé** : présenter la définition comme un choix du cadre inspiré de [86], et dater l'entrée (janvier 2025, jour à vérifier).
- **Confiance** : vérifié dans le texte

### [26-06] [MINEUR] ISO/IEC 22989 cité par la fiche d'un revendeur, qui ne contient pas la définition
- **Axe** : A
- **Localisation** : p. 253, [59] « ISO/IEC 22989:2022 … (fiche catalogue, édition 1). Standards Norway. https://online.standard.no/en/isoiec-22989-2022-3 ». Appel : p. 21, tableau 7, définition d'« Agent », « ISO/IEC 22989:2022; oneM2M TR-0081, v0.2.0 (version préliminaire)[59, 60]; cadre ».
- **Diagnostic** : l'URL ne relève pas de l'éditeur (ISO/IEC), mais d'un organisme national qui revend la norme. Une fiche de catalogue ne reproduit pas le contenu de la norme : elle ne peut donc pas appuyer une définition, comme le § 1.7 l'admet lui-même pour les textes payants (p. 15). La définition est en outre à demi tirée d'un projet de rapport technique (oneM2M v0.2.0).
- **Correctif proposé** : citer la fiche iso.org, ou la plateforme de consultation en ligne (OBP) de l'ISO, qui affiche les termes et définitions (à vérifier). Indiquer, pour la ligne « Agent », quelle partie de la définition vient de 22989 et quelle partie relève du cadre.
- **Confiance** : vérifié dans le texte; la disponibilité de l'OBP est à vérifier

### [26-07] [MINEUR] Nom d'auteur tronqué et note éditoriale d'attribution ambiguë
- **Axe** : A
- **Localisation** : p. 254, [65] « Anthropic (Erik S. et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note de l'éditeur : l'outillage décrit a changé depuis décembre 2024 ».
- **Diagnostic** : « Erik S. » n'est pas un nom bibliographique; l'auteur est Erik Schluntz (selon mes connaissances). « Note de l'éditeur » laisse croire à une note d'Anthropic, alors qu'il s'agit vraisemblablement d'un commentaire du cadre. Des commentaires semblables figurent dans d'autres entrées ([113], [116]).
- **Correctif proposé** : écrire « Schluntz, E. et Zhang, B. », et remplacer « Note de l'éditeur » par « Note du cadre ».
- **Confiance** : déduit (nom d'auteur, de mémoire); l'ambiguïté est vérifiée dans le texte

### [26-08] [MINEUR] URL non épinglées pour des versions épinglées
- **Axe** : A
- **Localisation** :
  - p. 254, [68] « Specification, version 1.0 (correctif 1.0.1 du 28 mai 2026) … https://a2a-protocol.org/latest/specification »;
  - p. 259, [172] « Arazzo Specification 1.1.0 … arazzo/latest.html »;
  - p. 251 [recouvrement], [19] « Cost of a Data Breach Report 2026 … https://www.ibm.com/reports/data-breach », sans date.
- **Diagnostic** : l'annexe H ([478]) relève une v1.1.0-rc d'A2A au 29 octobre 2026. Quand la 1.1 paraîtra, « latest » cessera de désigner la 1.0.1 qu'exigent l'EXIG-A2A-01 et 36 appels de [68]. De même, la page IBM pointe toujours vers la dernière édition, si bien que le chiffre « 4,99 M$ US (hausse de 12 %) » (p. 16) cessera d'être vérifiable par le lien dès l'édition 2027.
- **Correctif proposé** : épingler les liens par version (balises v1.0.1 de a2aproject/A2A et 1.1.0 d'Arazzo; PDF daté de l'édition 2026 d'IBM), et dater [19].
- **Confiance** : vérifié dans le texte

### [26-09] [MINEUR] Conventions OpenTelemetry épinglées à v1.41.0, quand le corps désigne v1.41.1 comme dernière version valide
- **Axe** : A / C
- **Localisation** : p. 256, [119] et [120], « …/blob/v1.41.0/docs/gen-ai/… ». Corps p. 145 : « la dernière version publiée qui les contient comme conventions en vigueur est la v1.41.1 (correctif du 11 mai 2026 de la v1.41.0 du 28 avril 2026) ». Tableau p. 50 : « v1.41.0 ou première version étiquetée du dépôt semantic-conventions-genai ».
- **Diagnostic** : le cadre épingle la version d'origine et non son correctif, sans dire pourquoi. Si la v1.41.1 corrige un attribut cité au tableau 41, les références et l'épinglage divergent.
- **Correctif proposé** : épingler v1.41.1 (références et tableaux), ou justifier le choix de v1.41.0 en précisant que le correctif ne touche pas les conventions gen_ai.*.
- **Confiance** : vérifié dans le texte; le contenu du correctif v1.41.1 est à vérifier

### [26-10] [MINEUR] Brouillon OAuth 2.1 −13 conservé, et parenthèse dédoublée dans l'appel
- **Axe** : C
- **Localisation** : p. 260, [210] « draft-ietf-oauth-v2-1-13 (Internet-Draft, version remplacée par la −16) ». Appel p. 60 : « dans sa version −13 (la version −16 est la plus récente au 27 octobre 2026; voir la section 6.3), que la spécification MCP cite encore (la version −16 est la plus récente au 27 octobre 2026; voir la section 6.3)[209, 210] ».
- **Diagnostic** : il est légitime de garder [210], puisque MCP cite la −13. Mais la parenthèse de l'appel est répétée mot pour mot, un défaut de composition du corps qui touche directement l'appel de [210]. Par ailleurs, la −16 a été remplacée à son tour par la −17 le 31 octobre 2026 ([481], annexe H) : la mention « remplacée par la −16 » est datée, ce qu'expliquerait l'état des sources au 27 octobre.
- **Correctif proposé** : supprimer la parenthèse répétée. Écrire dans [210] « version citée par MCP 2026-07-28; remplacée (−16 au 27 octobre 2026, −17 au 31 octobre) ».
- **Confiance** : vérifié dans le texte

### [26-11] [MINEUR] Gartner : l'appel renvoie à un « résumé public, août 2026 », l'entrée à un document réservé et non daté
- **Axe** : A
- **Localisation** : p. 253, [52] « Gartner (2026). Implement 3 Layers of Oversight… (document 8214461, accès réservé aux clients) ». Appel p. 19 : « (résumé public, août 2026)[52] ».
- **Diagnostic** : le tableau 66 admet en A les « communiqués des firmes d'analystes », pas les documents réservés. Le corps dit s'appuyer sur un résumé public, mais l'entrée ne le désigne pas et ne donne pas de date. L'affirmation n'est donc pas vérifiable à partir de l'entrée.
- **Correctif proposé** : donner l'URL et la date du résumé public, ou réduire l'énoncé à ce que le titre seul établit.
- **Confiance** : vérifié dans le texte

### [26-12] [MINEUR] Titre et URL discordants
- **Axe** : A
- **Localisation** : p. 261 [recouvrement], [228] « Announcing a complete developer toolkit for scaling A2A agents on Google Cloud … /agent2agent-protocol-is-getting-an-upgrade »; p. 257, [142] « Sun, L. (4 juin 2026). Designing agentgateway… AAIF (republié sur agentgateway.dev). https://agentgateway.dev/blog/… ».
- **Diagnostic** : pour [228], le chemin de l'URL évoque un autre titre, « Agent2Agent protocol (A2A) is getting an upgrade » (de mémoire, à vérifier) : soit le titre cité est un sous-titre, soit l'URL vise un autre billet. Pour [142], l'éditeur nommé est l'AAIF, mais l'URL est celle de la republication et non de l'original.
- **Correctif proposé** : aligner le titre sur la page visée, et pour [142] citer l'URL de l'original (aaif.io) ou nommer agentgateway comme éditeur.
- **Confiance** : à vérifier (source externe)

### [26-13] [MINEUR] Dates de passage au niveau « Graduated » différentes pour SPIFFE et SPIRE
- **Axe** : A
- **Localisation** : p. 256, [116] « niveau « Graduated » depuis le 23 août 2022 »; [117] « niveau « Graduated » depuis le 22 août 2022 ».
- **Diagnostic** : les deux projets sont passés au niveau « Graduated » conjointement; CNCF l'a annoncé, de mémoire, en septembre 2022. Un jour d'écart entre deux pages est plausible s'il reflète leurs métadonnées respectives, mais une coquille l'est aussi. Accord à corriger au passage : « consultée » ([116]) mais « consulté » ([232]).
- **Correctif proposé** : vérifier les deux pages CNCF et l'annonce officielle, et harmoniser.
- **Confiance** : à vérifier (source externe)

### [26-14] [MINEUR] Sources faibles pour des faits de chronologie
- **Axe** : A
- **Localisation** : p. 259, [189] « Documentation Index (llms.txt) », appelée p. 52 et p. 54 pour la liste des révisions de MCP; p. 252, [30] « Releases (v0.3.0, v1.0.0, v1.0.1) », appelée p. 52 pour « A2A est passé de la version 0.1 à la version 1.0[30, 34, 189] ».
- **Diagnostic** : un fichier d'index pour robots n'est pas un document de référence, et le registre de versions [34] suffit. Quant à [30], la description de l'entrée ne couvre pas la version 0.1 invoquée dans l'appel.
- **Correctif proposé** : retirer [189] des deux appels; étendre la description de [30] (« v0.1.0 à v1.0.1 ») ou citer [21] pour la 0.1.
- **Confiance** : vérifié dans le texte

### [26-15] [MINEUR] Formats hétérogènes des dates, des éditeurs et des auteurs institutionnels
- **Axe** : C
- **Localisation** : dans l'ensemble du chunk.
  - Dates : « (2025, 5 novembre) » [12], « (25 novembre 2024) » [20], « (2026-10-23) » [85], « (2020-01) » [69], « (janvier 2020) » [118], et date reportée après le titre (« Communiqué, 9 avril 2026 » [15], [31], [32], [38], [45]-[47]).
  - Années seules, alors que le corps donne le jour : [14] (« (2025) », billet du 9 décembre), [33], [147].
  - Éditeurs des RFC : « IETF / RFC Editor », « IETF », « IETF Datatracker ».
  - Plateforme en position d'auteur : « Microsoft Learn » [85].
- **Diagnostic** : rien de faux, mais le dédoublonnage (26-03) et la vérification des dates contre le corps en deviennent difficiles.
- **Correctif proposé** : adopter un seul gabarit, par exemple APA : Auteur (AAAA, jour mois). Titre. Éditeur. URL.
- **Confiance** : vérifié dans le texte

## Points forts
Chacune des entrées [12]-[253] est appelée dans le corps (aucune entrée orpheline détectée par Grep), et les dates clés concordent entre entrées et corps (ACP : 25, 27 et 29 août 2025; A2A 1.0.0 et 1.0.1; MCP 2026-07-28; Kafka 4.4.0 du 22 octobre 2026). Les appels vérifiés pour [12], [13], [16], [17], [18] et [140] soutiennent l'affirmation telle qu'écrite. Les brouillons IETF sont identifiés par leur numéro de version, et les sources préliminaires ou en statut Development sont signalées comme telles.

## Questions pour l'audit bibliographique
- p. 251, [19] : coût moyen mondial 2026 de 4,99 M$ US (+12 %); le chiffre 2025 de 4,44 M$ US donnerait 4,97 M$ US. Trancher avec le PDF de l'édition 2026.
- p. 253, [58] : le titre du règlement (UE) 2026/1744 vise-t-il bien aussi le règlement (UE) 2023/1230 (machines), et la publication au JO est-elle du 24.7.2026? L'annexe H.5 dit le texte inaccessible sur EUR-Lex le 1er novembre.
- p. 254, [76] : existence d'une « version 1.5 » du Model AI Governance Framework for Agentic AI de l'IMDA (de mémoire, la v1.0 date de janvier 2026).
- p. 254, [78] : liste des auteurs du draft-ietf-httpapi-idempotency-key-header-08 (« Tishkin, D. »?).
- p. 255, [93] : auteurs et date du draft-ietf-wimse-aims-00.
- p. 256, [126] : adk.dev est-il le domaine officiel de la documentation ADK (jusqu'ici, google.github.io/adk-docs)?
- p. 257, [135] : l'éditeur de Kata Containers est-il toujours l'OpenInfra Foundation, qui a rejoint la Linux Foundation en 2025?
- p. 257, [145] et [146] : existence et fenêtres de contexte de « GPT-6.1 Sol » et de « GPT-5.5 » (avril 2026, 1,05 million de jetons), appelés p. 41.
- p. 259, [170], [172] et [174] : dates d'OpenAPI 3.2.1 (10 septembre 2026), d'Arazzo 1.1.0 (17 mai 2026) et d'AsyncAPI 3.1.0 (31 janvier 2026).
- p. 256, [116] et [117] : dates exactes de passage au niveau « Graduated » de SPIFFE et de SPIRE (voir 26-13).
- p. 261, [228] : titre exact du billet de Google Cloud du 31 juillet 2025 (voir 26-12).
- p. 258, [167] : affiliation professionnelle de K. Waehner, pour la catégorisation (voir 26-04).
