# Audit chunk_27 — pages 261-272

## Synthèse
Le chunk couvre les références [211] à [433] de l'annexe G (MCP, A2A, événementiel, orchestration, autonomie, IAM, sécurité, bacs à sable, observabilité, FinOps, droit québécois et canadien). Les 223 entrées sont toutes appelées dans le corps (vérifié par extraction des appels, retours à la ligne compris), et les dates et versions concordent avec le corps dans la très grande majorité des cas. Les trois défauts les plus graves : (1) une vingtaine de doublons, qui contredisent l'affirmation de F.1 selon laquelle l'identité de chaque référence a été contrôlée et faussent le décompte de 473 références; (2) des blogues de positionnement (catégorie C) qui portent seuls le « Pourquoi » d'exigences DOIT et DEVRAIT; (3) le site non officiel du Future of Life Institute, seul appui d'obligations légales du RIA, alors qu'une source officielle du même article existe ([412]).

## Constats

### [27-01] [MAJEUR] Doublons systémiques dans l'annexe G, en contradiction avec l'audit final
- **Axe** : A
- **Localisation** : annexe G, p. 261-272, et entrées hors chunk; F.1, p. 241 : « L'identité de chaque référence (auteurs, titre, date, éditeur), sa catégorie et son statut à cette date ont été contrôlés » et « l'annexe G compte 473 références ».
- **Diagnostic** : la même source occupe plusieurs numéros, souvent avec des métadonnées qui divergent (date, auteurs, éditeur, URL). Un contrôle d'identité référence par référence aurait dû fusionner ces entrées. Le chiffre de 473 compte donc des numéros, pas des sources distinctes, ce qui affaiblit T8.
  | Même source | Numéros (pages où elles sont appelées) | Écart de métadonnées |
  |---|---|---|
  | RFC 9728 | [211] (p. 60), [330] (p. 125) | « avril 2025 » / « 2025-04 »; /doc/html/ / /doc/ |
  | RFC 9207 | [212] (p. 60), [329] (p. 125) | auteurs nommés / « IETF » |
  | RFC 8785 (JCS) | [236] (8 pages), [308] (p. 111) | « RFC Editor » / « IETF Datatracker » |
  | SagaLLM, PVLDB 18(12) | [287], [288] (appelées ensemble, p. 96) | seul l'arXiv les distingue |
  | OWASP Top 10 LLM 2025 | [347], [348] (appelées ensemble, p. 131) | « Gen AI » / « GenAI », deux URL |
  | Firecracker, NSDI '20 | [360], [363] (ensemble, p. 137-138) | page de présentation / PDF |
  | OAuth 2.1 −16 | [176], [327] | « (2026) » / « 3 septembre 2026 » |
  | Transaction Tokens −11 | [179], [332] (appelées ensemble, p. 127) | « IETF (2026-07-30) » / auteurs nommés |
  | WIMSE AIMS −00 | [93], [309] | « 15 septembre 2026 » / « (2026) » |
  | OWASP NHI Top 10 2025 | [91], [349], [470] | trois entrées, deux domaines |
  | Livre blanc de l'OIDF sur l'identité des agents | [311], [466], plus l'annonce [325] | « South, T. et al. » / « South, T. (dir.) »; même recommandation SCIM appelée [311] p. 124 et [466] p. 195 |
  | Enterprise-Managed Authorization | [178], [218] (appelées ensemble, p. 62) | site officiel / fichier brut GitHub |
  | ISO/IEC 42001:2023 | [395], [450] | ISO / Standards Norway, titre FR / EN |
  | RIA, art. 14 | [290] (FLI), [412] (Commission) | voir 27-03 |
  | OWASP Agentic Skills Top 10 | [350], [374] | page du projet / owasp.github.io |
  | OWASP Top 10 agentique | [28], [345] | document / billet d'annonce |
  | What's New in A2A v1.0 | [235], [240] (p. 262, recouvrement) | GitHub / site |
  | gVisor | [134], [361], [368] | page générique / sous-pages |
  | Introduction à Kafka | [257], [468] | /44/ / /intro |
  | CloudEvents 1.0.2 | [173], [248] | page des versions / balise |
  | Conventions OTel pour MCP | [219], [386] | branche main du dépôt genai / v1.41.0 |
  | Mise à l'échelle des agents (Google) | [273], [274] | [273] contient déjà l'arXiv de [274] |
- **Contre-exemple ou scénario de défaillance** : un relecteur qui corrige la date de [327] laisse [176] intact. Le même brouillon porte alors deux dates, et l'actualisation de H (−17, [481]) doit viser deux numéros au lieu d'un.
- **Correctif proposé** : fusionner chaque groupe sous un seul numéro (en gardant la variante la plus primaire et la plus précise), renuméroter les appels, puis corriger le décompte (473 devient environ 445) dans F.1 et partout où il est repris.
- **Confiance** : vérifié dans le texte (comparaison automatique des titres et identifiants sur l'annexe G entière, puis lecture).

### [27-02] [MAJEUR] Blogues de positionnement (catégorie C) à l'appui d'exigences
- **Axe** : A
- **Localisation** : [276], [277], [289], [262]. P. 87 : « Cette prise de position d'ingénierie recommande par défaut un agent linéaire à fil unique[276] ». EXIG-ORC-07 (DOIT), p. 91 : « Pourquoi : des écritures concurrentes se contredisent[277]. » EXIG-ORC-10, p. 93 : « [275, 276] ».
- **Diagnostic** : le § 1.7 (p. 14) et le tableau 66 définissent la catégorie C comme « blogue de positionnement » et la déclarent « jamais citée ». Le corps qualifie lui-même [276] de prise de position. [277] (LangChain Blog, un éditeur qui défend son cadriciel) est le seul appui d'une exigence DOIT. Or même une source B ne peut porter seule une exigence (tableau 66). [289] prolonge [276]. Le billet de Confluent [262], un essai d'architecture et non de la documentation de produit, est classé A en annexe F (ligne 18 du tableau 68), contrairement à la définition A du tableau 66 (« documentation officielle d'un éditeur sur son propre produit »).
- **Contre-exemple ou scénario de défaillance** : un auditeur conteste EXIG-ORC-07. La seule source du « Pourquoi » est un billet promotionnel, ce qui rend la justification irrecevable au regard de la règle que le cadre s'impose.
- **Correctif proposé** : fonder EXIG-ORC-07 sur une source A, par exemple Cemri et al. [292] (taxonomie des défaillances multiagents) ou un résultat de cohérence en écriture concurrente, ou la déclarer « choix du cadre ». Requalifier [276], [277], [289] et [262] en B (expert reconnu) ou en C, et les retirer ou les reléguer au contexte.
- **Confiance** : vérifié dans le texte (classement en C : déduit de la définition du tableau 66).

### [27-03] [MAJEUR] Un site non officiel, seul appui d'obligations légales du RIA
- **Axe** : A
- **Localisation** : [290], [375], [394], [315] (artificialintelligenceact.eu). EXIG-AUT-02, p. 105 : « Pourquoi : le RIA exige des mesures de contrôle humain proportionnées […] (art. 14, par. 3)[290] ». EXIG-CON-15, p. 182 : « Pourquoi : la composition d'agents peut […] faire basculer l'entreprise dans le rôle de fournisseur[375]. » Le corps qualifie lui-même ce site de « site non officiel du Future of Life Institute » (p. 181).
- **Diagnostic** : le même alinéa (art. 14(3)) est appuyé par [412] (Commission européenne) à la p. 172, mais par [290] seul à la p. 105. Le tableau 66 réserve la catégorie A aux « textes législatifs et organismes de réglementation » : un miroir annoté par une ONG n'en fait pas partie. Aux p. 99, 105, 114 et 144, [290] porte seul des obligations de l'art. 14(4) b) et e).
- **Contre-exemple ou scénario de défaillance** : le règlement (UE) 2026/1744 renumérote ou modifie un alinéa, et le miroir tarde à le refléter. L'exigence cite alors un texte périmé sans que le registre des sources le détecte.
- **Correctif proposé** : citer EUR-Lex [58] ou le Service Desk de la Commission [412] partout où une obligation légale est invoquée, et garder FLI comme aide à la lecture (catégorie B). Fusionner [290] avec [412].
- **Confiance** : vérifié dans le texte.

### [27-04] [MINEUR] Projet de loi C-36 : deux titres différents pour le même projet
- **Axe** : C
- **Localisation** : [430], p. 272 : « Loi visant à protéger la vie privée et les données des consommateurs »; [431] : « Loi sur la protection de la vie privée et des données des consommateurs »; tableau 48, p. 178, qui suit [431].
- **Diagnostic** : un même projet de loi, à la même date, porte deux titres. L'un est probablement le titre intégral et l'autre le titre abrégé, mais rien ne le dit. (La mention « deuxième lecture » est déjà consignée en H.4 comme simple précision.)
- **Contre-exemple ou scénario de défaillance** : une recherche du titre exact dans LEGISinfo n'aboutit que pour l'une des deux formulations.
- **Correctif proposé** : reprendre le titre officiel tel qu'il figure à LEGISinfo et préciser « titre abrégé » s'il y a lieu. Fusionner [430] et [431] ou distinguer explicitement la fiche et le texte de première lecture.
- **Confiance** : vérifié dans le texte (titre officiel à vérifier).

### [27-05] [MINEUR] Coquille probable dans l'URL de [353]
- **Axe** : A
- **Localisation** : [353], p. 268 : « …/guide-use-agentic-artificial-antelligence.html ».
- **Diagnostic** : « antelligence » pour « intelligence ». Sauf coquille présente dans l'URL officielle elle-même, le lien est mort. [353] appuie trois passages (p. 133, 179, 204).
- **Contre-exemple ou scénario de défaillance** : le vérificateur de liens renvoie une erreur 404, et la source devient invérifiable.
- **Correctif proposé** : vérifier l'URL sur canada.ca et la corriger.
- **Confiance** : à vérifier (source externe).

### [27-06] [MINEUR] [427] « art. 10.1 » ne couvre pas toute l'affirmation qu'il appuie
- **Axe** : A
- **Localisation** : tableau 48, p. 178 : « toutes les atteintes sont consignées, registre conservé 24 mois[426, 427] »; [427] : « PIPEDA […], art. 10.1 ».
- **Diagnostic** : d'après mes connaissances, la tenue du registre relève de l'art. 10.3 de la LPRPDE, et la durée de 24 mois vient du Règlement sur les atteintes aux mesures de sécurité (DORS/2018-64, art. 6), non de l'art. 10.1. [426] couvre probablement le point, mais le libellé de [427] est trop étroit. Autre détail : [426] porte un titre français avec une URL anglaise (/en/).
- **Contre-exemple ou scénario de défaillance** : un juriste qui ouvre l'art. 10.1 n'y trouve pas les 24 mois.
- **Correctif proposé** : citer « art. 10.1 et 10.3 » et ajouter le règlement DORS/2018-64; aligner la langue de l'URL de [426] sur celle du titre.
- **Confiance** : déduit (articles de loi de mémoire, à vérifier).

### [27-07] [MINEUR] Versions épinglées citées par des URL mouvantes
- **Axe** : C
- **Localisation** : [219] (semantic-conventions-genai, branche main) pour un fait que [386] épingle en v1.41.0; [231], [237], [238] (a2a-protocol.org/latest/…) alors que le cadre épingle A2A 1.0 et qu'une v1.1.0-rc existe ([478]); [252], [253], [255] (CloudEvents, branche main) face à 1.0.2 [248].
- **Diagnostic** : une URL « latest » ou « main » change sans préavis, alors que l'entrée ne donne pas de date de consultation. Le corps reconnaît l'écart pour CloudEvents (p. 77), mais pas pour [219] ni pour les pages A2A.
- **Contre-exemple ou scénario de défaillance** : une fois A2A 1.1 publié, [237] (« Agent Discovery ») décrit la 1.1 alors que le cadre exige la 1.0.
- **Correctif proposé** : pointer vers la balise de version (v1.0.0, v1.41.0) ou ajouter « consulté le 27 octobre 2026 » à chaque entrée non épinglée. Remplacer [219] par [386].
- **Confiance** : vérifié dans le texte.

### [27-08] [MINEUR] Entrée [273] mal formée
- **Axe** : C
- **Localisation** : [273], p. 263 : « https://research.google/blog/towards-a-science-of-scaling-agent -systems-… (article : arXiv:2512.08296). https://research.google/blog/… »
- **Diagnostic** : l'URL est répétée, la première occurrence est coupée par une espace, l'arXiv de [274] y est incorporé, et la date suit un format inversé (« 2026, 28 janvier »).
- **Contre-exemple ou scénario de défaillance** : un extracteur de liens retient l'URL tronquée.
- **Correctif proposé** : une seule URL, sans renvoi à l'arXiv (déjà en [274]), et le format de date de l'annexe.
- **Confiance** : vérifié dans le texte (l'espace peut venir de l'extraction, mais pas le doublement de l'URL).

### [27-09] [MINEUR] Notation bibliographique hétérogène
- **Axe** : C
- **Localisation** : dans tout le chunk. Dates : « (avril 2025) » [211], « (2023-09) » [213], « (2026, 28 janvier) » [273], [398], date après le titre [249], [259], [299], [300], [340]. « (s.d.) » [317], [405], [414], [419] contre « (s. d.) » ailleurs. Auteurs collectifs : « OWASP Gen AI » [346], [347] / « OWASP GenAI » [345], [348]; « Projet gVisor » [361] / « gVisor » [362]; « Microsoft » [278] / « Microsoft Learn » [294] / « Microsoft (GitHub) » [293]; « A2A Project » / « Agent2Agent (A2A) Project » [232] / « A2A Project (Linux Foundation) » [240]; auteurs des RFC nommés en [212] et [236], omis en [211], [213], [312], [328].
- **Diagnostic** : l'absence de gabarit unique empêche la détection mécanique des doublons (cause probable de 27-01).
- **Contre-exemple ou scénario de défaillance** : sans objet (lisibilité et outillage).
- **Correctif proposé** : un seul gabarit (Auteur, date ISO ou « j mois aaaa », titre, éditeur, URL, date de consultation), appliqué par script.
- **Confiance** : vérifié dans le texte.

### [27-10] [MINEUR] [218] : URL brute, sans rapport avec la publication de l'éditeur
- **Axe** : A
- **Localisation** : [218], p. 261 : « https://raw.githubusercontent.com/modelcontextprotocol/ext-auth/main/specification/stable/… .mdx ».
- **Diagnostic** : la source est un fichier source brut de la branche main, alors que l'éditeur publie la page sur modelcontextprotocol.io ([178]). Le titre « (2026-07-28) » laisse croire à un épinglage que l'URL contredit.
- **Contre-exemple ou scénario de défaillance** : une modification sur main change le contenu cité sous une étiquette datée.
- **Correctif proposé** : fusionner avec [178], ou pointer vers la balise ou le chemin daté du dépôt.
- **Confiance** : vérifié dans le texte.

### [27-11] [MINEUR] [246] : une page « About » appelée avec une affirmation technique, et un statut d'auteur qui varie
- **Axe** : A
- **Localisation** : p. 76 : « MCP n'offre ni garantie de livraison ni cohérence […][167, 246] »; p. 37 : « comme le souligne l'architecte Kai Waehner[167] »; p. 75 : « conseiller indépendant en diffusion de données en continu ».
- **Diagnostic** : [246] ne sert qu'à justifier la qualité de l'auteur. Il est pourtant appelé avec l'affirmation technique, qui relève de la spécification MCP (catégorie A). Le statut de l'auteur varie d'une page à l'autre, et son indépendance à l'égard d'un éditeur de Kafka conditionne le classement B de [167].
- **Contre-exemple ou scénario de défaillance** : un lecteur prend [246] pour une source de l'affirmation sur MCP.
- **Correctif proposé** : appuyer l'affirmation sur la spécification MCP (absence de garantie de livraison), placer [246] après la qualification de l'auteur et harmoniser cette qualification.
- **Confiance** : vérifié dans le texte (indépendance de l'auteur : à vérifier).

### [27-12] [MINEUR] [305] : un fait de Gartner relayé par la presse
- **Axe** : A
- **Localisation** : EXIG-AUT-06, p. 107 : « Pourquoi : Gartner situe la cause de nombreux échecs […][305] »; [305] : ITPro.
- **Diagnostic** : le tableau 66 range les communiqués d'analystes en A. Citer Gartner par l'intermédiaire d'ITPro (B) dégrade la preuve sans raison. Le « Pourquoi » reste soutenu par l'IMDA [76].
- **Contre-exemple ou scénario de défaillance** : la presse reformule ou attribue mal le constat de Gartner.
- **Correctif proposé** : citer le communiqué ou la note de Gartner, ou bien écrire « selon ITPro, qui rapporte Gartner ».
- **Confiance** : vérifié dans le texte.

### [27-13] [MINEUR] [242] : un billet de tiers, seul appui d'un fait de version
- **Axe** : A
- **Localisation** : p. 75 : « celui de JavaScript n'est en disponibilité générale que depuis le 22 juillet 2026[242] »; [242] : un guide de contributeur publié sur le blogue de l'AAIF.
- **Diagnostic** : une date de publication de SDK se prouve par la page des versions du SDK (catégorie A). Un guide de contributeur est au mieux B.
- **Contre-exemple ou scénario de défaillance** : le guide confond la date de la préversion et celle de la version générale.
- **Correctif proposé** : citer la page des versions du SDK JavaScript dans a2aproject.
- **Confiance** : vérifié dans le texte (la date elle-même reste à vérifier).

### [27-14] [MINEUR] Attribution qui varie pour « les transferts perdent des décisions implicites »
- **Axe** : C
- **Localisation** : p. 87, attribution à Cognition [276]; p. 93 (EXIG-ORC-10) : « [275, 276] »; p. 100 (tableau des anti-patrons) : « Les transferts perdent des décisions implicites[275] ».
- **Diagnostic** : la thèse vient de Cognition d'après la p. 87, mais le tableau de la p. 100 ne cite que l'article d'Anthropic. Soit [275] la formule aussi, et il faut le dire, soit l'appel est mal ciblé.
- **Contre-exemple ou scénario de défaillance** : un vérificateur ne trouve pas la formule dans [275].
- **Correctif proposé** : aligner les trois appels après vérification du contenu de [275].
- **Confiance** : déduit (contenu de [275] non vérifiable ici).

### [27-15] [MINEUR] URL qui ne correspondent pas aux titres ou à l'éditeur
- **Axe** : A
- **Localisation** : [228] « Announcing a complete developer toolkit for scaling A2A agents » avec le chemin « …/agent2agent-protocol-is-getting-an-upgrade »; [299] « microsoft.com/en-us/copilot/blog/… », alors que [298] et [300] utilisent « microsoft.com/en-us/microsoft-copilot/blog/… ».
- **Diagnostic** : le chemin de [228] correspond au titre « Agent2Agent protocol is getting an upgrade », et non au titre donné. Pour [299], le chemin diffère des deux autres billets du même blogue.
- **Contre-exemple ou scénario de défaillance** : le titre cité ne figure pas sur la page ouverte.
- **Correctif proposé** : relever le titre exact de la page et l'URL canonique.
- **Confiance** : à vérifier (source externe).

## Points forts
Toutes les références du chunk sont appelées dans le corps, et les versions (conformité MCP 0.1.16 / 0.2.0-alpha.12, a2a-cli, Kafka 4.0 à 4.4, AsyncAPI 3.0.0 / 3.1.0, brouillons OAuth) concordent avec le texte. Les références classiques que j'ai pu contrôler de mémoire sont exactes : Sagas (SIGMOD 1987, p. 249-259, DOI), Parasuraman et al. 2000 et 2010, Firecracker NSDI '20, RFC 9207, 9449, 8705, 9396, 9420 et 8785. Le statut des brouillons (expiré, file de l'éditeur des RFC, soumission individuelle) est indiqué avec soin.

## Questions pour l'audit bibliographique
- p. 265, [304] : la révision SAE J3016_202609 existe-t-elle? (La révision connue la plus récente est J3016_202104.) Le texte de la p. 107 la dit « en vigueur ».
- p. 268, [346] : un OWASP Top 10 for LLM Applications 2026 (août 2026) existe-t-il, et l'agentivité excessive y passe-t-elle de LLM06 à LLM03 (p. 131)?
- p. 264, [287] et [288] : SagaLLM a-t-il paru dans PVLDB 18(12), p. 4874-4886?
- p. 264, [280] : vérifier l'existence d'arXiv:2608.10218 (« Mind Viruses ») et sa conclusion « risque réel mais actuellement limité » (p. 90).
- p. 263, [260] et [261] : files coopératives prêtes pour la production en Kafka 4.2.0, files de lettres mortes en 4.4.0 du 22 octobre 2026 (p. 80).
- p. 262, [255] : existence de l'extension CloudEvents Data Classification sur main et de l'exigence faite aux intermédiaires de ne pas modifier ces attributs (p. 77).
- p. 266-267, [323], [333], [334] : numéros des brouillons et statuts (« soumis à l'IESG », « RFC Ed Queue »), et liste d'auteurs de [334].
- p. 270, [393] : date du Candidate Recommendation Snapshot de W3C Baggage (30 mai 2024?).
- p. 271, [411] : annonce de la « AI Agent Standards Initiative » du NIST CAISI, 17 février 2026.
- p. 272, [424] : 514 avis d'incidents, +16 %, 80 % du privé, 251 accès non autorisés (p. 186).
- p. 272, [430] et [431] : titre officiel du projet de loi C-36 (45-1).
- p. 268, [353] : URL exacte du guide fédéral sur l'IA agentique.
- p. 265, [297] : domaine officiel de la documentation ADK (adk.dev ou google.github.io/adk-docs).
- p. 262, [246] : statut actuel de Kai Waehner (indépendant ou rattaché à un éditeur).
- p. 261, [228] et p. 265, [299] : titres et URL canoniques.
- p. 262, [242] : date de disponibilité générale du SDK A2A JavaScript (22 juillet 2026).
