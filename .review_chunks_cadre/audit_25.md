# Audit chunk_25 — pages 241-252

## Synthèse
Le chunk couvre la fin du glossaire (E), l'annexe F (méthode, bilan chiffré, tableau 68 des 32 corrections, registre des 121 références, tableau 69) et le début de l'annexe G ([1]-[47]). L'arithmétique est juste : le tableau 69 recompté donne exactement les totaux de F.2 et du tableau 67 (61 C, 13 non accessibles, 71/17/33, 125/214/69/19 = 427). En revanche, le registre ne permet pas de suivre la trace d'une source jusqu'à l'annexe G. Les trois défauts les plus graves : (1) des sources « remplacées » ou « retirées » restent citées dans G, et environ douze sources « conservées » en sont absentes; (2) la traçabilité revendiquée (T8) n'est pas reproductible; (3) la correction no 17 sur Firecracker contredit la section 9.7, et la correction no 31 sur la saga laisse ouvert le cas de l'effet tardif.

## Constats

### [25-01] [MAJEUR] Sources déclarées « remplacées » ou « retirées » au tableau 69, mais toujours citées dans l'annexe G
- **Axe** : C
- **Localisation** : F.4, tableau 69, p. 245-249. Légende : « remplacée = remplacée par une source primaire; retirée = sans valeur probante pour le cadre ».
- **Diagnostic** : selon la légende, une source remplacée ou retirée ne devrait plus appuyer le corps. Or au moins cinq d'entre elles figurent telles quelles dans G et y sont citées :
  - no 7, TrueFoundry, « Governing AI Agents Across Multiple Platforms », remplacée : c'est [44], cité quatre fois (p. 19 notamment, « [44, 45] »);
  - no 16, « [Project Proposal] AGNTCY #57 », remplacée : c'est [37], cité p. 17 et au tableau 68 no 8;
  - no 36, Gartner, « Implement 3 Layers of Oversight… (titre non vérifié) », retirée : c'est [52], cité p. 19 (« résumé public, août 2026 »);
  - no 41, « Levels of Autonomy for AI Agents », remplacée : c'est [83] (Feng et al.), cité p. 23 et donné comme fondement de l'échelle N0-N4 au tableau 68 no 30;
  - no 52, « TRiSM for Agentic AI », remplacée : c'est [454], cité p. 183.
- **Contre-exemple ou scénario de défaillance** : un lecteur qui remonte l'appui de « [44, 45] » (p. 19) trouve au registre que TrueFoundry a été remplacée, conclut que l'appui est caduc et rejette à tort une affirmation du corps. À l'inverse, il ne peut pas savoir si [52] est valide, puisqu'elle est à la fois retirée au registre et citée dans le corps.
- **Correctif proposé** : corriger la décision de ces lignes (« conservée », ou « remplacée puis réintroduite à l'audit final », avec la date). Ajouter au tableau 69 une colonne « no dans G ».
- **Confiance** : vérifié dans le texte (recherche des titres dans full.txt).

### [25-02] [MAJEUR] Une douzaine de sources « conservées » absentes de l'annexe G
- **Axe** : C
- **Localisation** : F.4, légende, p. 245 : « conservée = source A ou B citée là où elle appuie un fait ». G, p. 250 : toutes les références sont « citées dans le corps ». F.2, p. 242 : « 33 conservées ».
- **Diagnostic** : une source « conservée » devrait apparaître dans G. Une recherche par titre et par éditeur dans le texte complet ne trouve aucune entrée G pour les numéros 1 (Architecture & Governance Magazine), 31 (Gartner, « Enterprise Architecture 2030 »), 37 (Firecrawl), 48 (Confluent, « Real-Time Backbone »), 49 (E2B, « Best Code Execution Sandboxes » : G cite seulement [367], un autre document), 57 (Confluent Intelligence), 61 (Gartner, « Avoid Governance Mismatch »), 68 (Sequoia, « LIVE »), 69 (LangChain, « UX for Agents, Part 2 »), 81 (Confluent, « Four Design Patterns »), 94 (SYNAPSE), 99 (Auth0) et 117 (Palo Alto Networks). Le no 22 correspond probablement à [275], sous un autre titre. Le chiffre « 33 conservées » ne correspond donc pas aux sources réellement citées.
- **Contre-exemple ou scénario de défaillance** : un auditeur cherche dans G la source Gartner no 61, conservée et cotée ✓1 ◐1, qui appuierait l'échelle d'autonomie (la figure 14 cite « Gartner (2026) »). Elle n'y est pas : l'affirmation devient orpheline.
- **Correctif proposé** : soit redéfinir « conservée » comme « admissible, non nécessairement citée », soit retirer ces lignes ou les rattacher à leur numéro G. Recalculer ensuite F.2.
- **Confiance** : vérifié dans le texte. Seule réserve : une entrée G pourrait porter un titre différent, ce qu'une colonne de correspondance trancherait.

### [25-03] [MAJEUR] La traçabilité revendiquée par l'annexe F n'est pas reproductible (thèse T8)
- **Axe** : B
- **Localisation** : F, p. 241 : « Elle permet à tout lecteur de retracer l'origine d'un fait et le degré de confiance ». F.2, p. 242 : « 33 présentant les marques d'un contenu généré en série ». F.4, p. 245 : « ✗ non appuyée ou contredite ». G, p. 250 : « Toutes sont de catégorie A […] ou B ».
- **Diagnostic** : la méthode n'est pas auditable de l'extérieur, pour cinq raisons :
  - le registre ne couvre que les 121 références initiales, rien sur les 428 de l'audit final ni sur les 473 de G;
  - aucun des 427 liens affirmation-source ni des 1 409 affirmations n'est publié;
  - G ne donne pas la catégorie de chaque référence, si bien que « toutes A ou B » et « 632 de catégorie A » sont invérifiables;
  - les 33 sources « générées en série » ne sont pas identifiées au tableau 69;
  - le symbole ✗ fusionne « non appuyée » et « contredite », que le tableau 67 distingue (55 et 14) : on ne peut pas savoir quelles sources ont été contredites.
- **Contre-exemple ou scénario de défaillance** : un vérificateur veut savoir quelle source contredisait une affirmation reprise au corps. Il ne peut le savoir ni par le registre ni par G.
- **Correctif proposé** : ajouter une catégorie par entrée de G, une colonne « no G » au tableau 69 et deux symboles distincts pour « non appuyée » et « contredite ». Publier en jeu de données le registre lien par lien (affirmation, page, source, verdict), y compris celui de l'audit final.
- **Confiance** : vérifié dans le texte.

### [25-04] [MAJEUR] Tableau 68 no 17 (Firecracker) contredit la section 9.7 et cite un doublon
- **Axe** : C (et A pour le fait externe)
- **Localisation** : tableau 68, no 17, p. 244 : « quatre types de périphériques émulés (réseau et bloc virtio, port série, contrôleur de clavier i8042 partiel) […][363] ». Section 9.7, p. 138 : « Firecracker n'émule que cinq périphériques (virtio-net, virtio-block, virtio-vsock, une console série et un contrôleur de clavier minimal) », avec d'autres périphériques ajoutés dans les versions récentes.
- **Diagnostic** : la « version retenue » donne quatre périphériques, le corps en donne cinq plus des ajouts selon la version. La correction présente comme définitif un état de 2020 que le corps qualifie de dépassé. Elle reproche aussi à l'ébauche ses « six périphériques virtio », alors que ce chiffre n'est pas manifestement faux pour une version récente (net, block, vsock, balloon, rng, pmem, mem). Enfin, [363] et [360] sont le même article NSDI '20 (seule l'URL diffère), et le corps attribue les mêmes chiffres à [360].
- **Contre-exemple ou scénario de défaillance** : un architecte se fie au tableau 68, sous-estime la surface d'attaque d'une microVM 1.14 avec virtio-pmem et virtio-mem, et l'homologue avec une analyse de menace incomplète.
- **Correctif proposé** : aligner le no 17 sur la section 9.7 (« cinq en 2020 selon le site; davantage selon la version »), fusionner [360] et [363], et requalifier le reproche fait à l'ébauche.
- **Confiance** : la contradiction est vérifiée dans le texte. La liste exacte de l'article de 2020 est à vérifier (source externe).

### [25-05] [MAJEUR] Saga, no 31 : la compensation conditionnelle ne couvre pas l'action qui s'exécute après coup
- **Axe** : A
- **Localisation** : tableau 68, no 31, p. 244 : « Une étape à l'état incertain est traitée comme possiblement exécutée; sa compensation, idempotente, doit pouvoir s'exécuter sans risque ». Le texte normatif correspondant est EXIG-ORC-16, p. 96 : « sa compensation est déclenchée et reste sans effet si l'action n'a pas eu lieu ».
- **Diagnostic** : une compensation conditionnelle (« rembourser X si débité ») n'est sûre que si l'action d'origine ne peut plus survenir une fois la compensation évaluée. Rien ne garantit cette condition : requête encore en transit, réessai côté client HTTP ou côté file, traitement asynchrone dans le système cible. La séquence peut donc devenir « compensation sans effet, puis débit tardif » : l'effet persiste sans aucune compensation, ce qui est précisément le défaut que la correction prétend lever.
- **Contre-exemple ou scénario de défaillance** :
  1. Le délai expire à t0.
  2. L'orchestrateur compense à t1 : X n'est pas encore débité, donc rien n'est fait.
  3. Le débit de X, en file chez le prestataire, s'applique à t2.
  4. La saga est close comme compensée alors que le client est débité.
- **Correctif proposé** : avant de compenser, clôturer l'opération dans le système cible, en annulant ou en révoquant la clé d'idempotence (pierre tombale) pour que toute arrivée tardive soit rejetée. Sinon, interroger l'état jusqu'à une issue définitive. Dans les deux cas, ajouter une réconciliation différée des étapes incertaines. À reporter dans EXIG-ORC-16 et EXIG-ORC-17 (chunk 10).
- **Confiance** : déduit.

### [25-06] [MINEUR] Date de vérification de G incompatible avec l'audit final
- **Axe** : C
- **Localisation** : G, p. 250 : « consultées ou vérifiées au 27 octobre 2026 ». F.1, p. 242 : « Le 28 octobre 2026, chacune des 428 références […] a été rouverte » et « 49 sources ont été ajoutées ».
- **Diagnostic** : les 49 sources ajoutées et les réouvertures datent du 28 octobre. La mention « au 27 octobre » est soit l'état des sources (convention reprise en H), soit fausse pour une partie de G.
- **Contre-exemple ou scénario de défaillance** : une source modifiée le 27 au soir et rouverte le 28 n'a pas de date de vérification exacte.
- **Correctif proposé** : écrire « état des sources au 27 octobre 2026; vérifiées les 27 et 28 octobre 2026 ».
- **Confiance** : vérifié dans le texte.

### [25-07] [MINEUR] Définitions de « remplacée » et « retirée » inapplicables aux sources de catégorie A
- **Axe** : C
- **Localisation** : F.4, p. 245 : « remplacée = remplacée par une source primaire ».
- **Diagnostic** : six sources de catégorie A, donc déjà primaires selon le tableau 66, sont « remplacées » (nos 16, 41, 52, 95, 98, 100), et deux sont « retirées » comme « sans valeur probante » (nos 36 et 80). Pour les brouillons IETF −00 et −01, le vrai motif est probablement le remplacement par une version plus récente ([335]), mais la légende ne le prévoit pas.
- **Contre-exemple ou scénario de défaillance** : le no 98, brouillon IETF de catégorie A, est « remplacé par une source primaire », ce qui n'a pas de sens.
- **Correctif proposé** : ajouter des motifs à la décision : version plus récente, source plus spécifique, hors sujet.
- **Confiance** : vérifié dans le texte.

### [25-08] [MINEUR] Catégorie et verdict attribués à des pages non lues
- **Axe** : B
- **Localisation** : tableau 69 : nos 36 (« titre non vérifié », A, bloquée), 62 (« titre non confirmé », B, bloquée), 84 (« page inaccessible », B), 41 (arXiv, « bloquée », ✓1), 31 (payante, ✓1), 61 (bloquée, ✓1 ◐1).
- **Diagnostic** : une catégorie qui dépend de l'éditeur et du contenu ne peut pas être attribuée à une page dont on ignore jusqu'au titre. Un verdict ✓ (« confirme l'affirmation telle qu'écrite ») tiré d'un seul résumé public surestime le niveau de preuve. Enfin, la mention « bloquée » pour arXiv, en libre accès, est surprenante.
- **Contre-exemple ou scénario de défaillance** : une affirmation appuyée sur un résumé Gartner est notée ✓ comme si le rapport payant avait été lu.
- **Correctif proposé** : ajouter un verdict « appuyée sur résumé seulement » et noter « n. d. » comme catégorie d'une page non lue.
- **Confiance** : vérifié dans le texte (pour arXiv : déduit).

### [25-09] [MINEUR] Doublons dans l'annexe G
- **Axe** : C
- **Localisation** : G, p. 250 : « [6] Anthropic (Erik S. et Zhang, B.) (19 décembre 2024). Building effective agents », entrée identique à [65]. Même cas pour [360] et [363] (Firecracker, NSDI '20).
- **Diagnostic** : la numérotation « dans l'ordre de leur première citation » suppose un numéro unique par source. Les doublons gonflent le décompte de 473 et brouillent les renvois. La forme « Erik S. » pour Schluntz, E. est aussi incohérente avec le reste de G.
- **Contre-exemple ou scénario de défaillance** : dans la convention retenue, le nombre de sources distinctes est 471, pas 473.
- **Correctif proposé** : fusionner les doublons, renvoyer les seconds numéros vers les premiers et corriger le nom d'auteur.
- **Confiance** : vérifié dans le texte.

### [25-10] [MINEUR] Format des dates hétérogène dans G
- **Axe** : C
- **Localisation** : G, p. 250-252 : « Gartner (2025, 26 août) », « Linux Foundation (9 décembre 2025) », « Linux Foundation (2026). […] Communiqué, 9 avril 2026 », « Soria Parra, D. (2025) » alors que l'URL porte 2025-12-09; plus loin « (2026-05-25) » ([262]) et « (2023-01) » ([74]).
- **Diagnostic** : au moins quatre conventions coexistent, ce qui gêne le tri et la vérification.
- **Contre-exemple ou scénario de défaillance** : sans objet (défaut de forme).
- **Correctif proposé** : une seule forme, par exemple « (AAAA, jour mois) ».
- **Confiance** : vérifié dans le texte.

### [25-11] [MINEUR] [11] CyberArk cité par une reproduction de presse
- **Axe** : B
- **Localisation** : G, p. 250 : « [11] CyberArk […] Business Wire (reproduit par Silicon UK) »; tableau 68, no 20 : « Enquête de fournisseur la mieux documentée ».
- **Diagnostic** : le chiffre qui fonde une correction est tiré d'une copie tierce du communiqué, ni du rapport de CyberArk ni du fil Business Wire. G affirme pourtant des sources « primaires ou officielles ».
- **Contre-exemple ou scénario de défaillance** : si la page de Silicon UK disparaît ou est altérée, l'appui disparaît avec elle.
- **Correctif proposé** : citer le rapport CyberArk 2025 Identity Security Landscape ou le communiqué original.
- **Confiance** : vérifié dans le texte.

### [25-12] [MINEUR] Appels de référence incomplets dans le tableau 68
- **Axe** : C
- **Localisation** : no 1, p. 243 : « on exige OAuth 2.0 selon la RFC 9700 […][176, 209] »; no 7 : « A2A annoncé comme projet de l'AAIF le 17 août 2026 […][5, 29, 472] »; no 30, p. 244 : « fondée sur Feng et al., Gartner, AWS et l'IMDA […][76, 83] ».
- **Diagnostic** :
  - no 1 : la RFC 9700 est [175], absente de l'appel;
  - no 7 : le billet de l'AAIF du 17 août est [35], absent (la release 1.0.1 est bien [472]);
  - no 30 : Gartner et AWS sont invoqués sans référence.
- **Contre-exemple ou scénario de défaillance** : le lecteur ne peut pas vérifier la date du 17 août à partir des sources citées, qui ne la contiennent pas (le no 2 du tableau 72 confirme que ce sont deux billets distincts).
- **Correctif proposé** : ajouter [175] au no 1, [35] au no 7, et les références Gartner et AWS au no 30.
- **Confiance** : vérifié dans le texte.

### [25-13] [MINEUR] No 16 : la version retenue n'est pas la plus récente
- **Axe** : C
- **Localisation** : tableau 68, no 16, p. 244 : « +80,9 % (Finance-Agent), −39 % à −70 % (PlanCraft) […][17, 273, 275] ». Section 7.1, p. 86 : « La version 3 de l'article (8 avril 2026 […]) donne une plage de +80,8 % à −70,0 % »[274].
- **Diagnostic** : la correction retient les chiffres du billet et ignore la version 3, que le corps juge pourtant plus complète.
- **Contre-exemple ou scénario de défaillance** : un lecteur qui ne consulte que l'annexe F retient des chiffres que le corps nuance.
- **Correctif proposé** : citer [274] et mentionner la plage de la version 3.
- **Confiance** : vérifié dans le texte.

### [25-14] [MINEUR] « Cinq ans » au lieu d'« au moins cinq ans »
- **Axe** : C
- **Localisation** : tableau 68, no 21, p. 244 : « registre (art. 3.8) conservé cinq ans selon le règlement ». Section 12.8, p. 188 : « conservé au moins cinq ans ».
- **Diagnostic** : le Règlement sur les incidents de confidentialité fixe un minimum. La formulation de F laisse croire à une durée exacte, que l'on pourrait lire comme une obligation de destruction.
- **Contre-exemple ou scénario de défaillance** : un registre détruit à cinq ans pile alors qu'une instance en cours en exige la conservation.
- **Correctif proposé** : écrire « au moins cinq ans ».
- **Confiance** : vérifié dans le texte (portée exacte du règlement : à vérifier).

### [25-15] [MINEUR] « Autres provinces » : réserve à géométrie variable
- **Axe** : C
- **Localisation** : tableau 68, no 24, p. 244 : « y compris, selon l'interprétation du cadre, les autres provinces ». Glossaire, p. 235 : « autres provinces comprises (art. 17) », sans réserve.
- **Diagnostic** : le même point est présenté tantôt comme une interprétation, tantôt comme le texte de la loi. « À l'extérieur du Québec » couvre littéralement les autres provinces, donc la réserve semble superflue.
- **Contre-exemple ou scénario de défaillance** : une équipe lit « interprétation du cadre », y voit une simple option interne et omet l'EFVP pour un hébergement en Ontario.
- **Correctif proposé** : supprimer la réserve, ou l'étendre partout en citant la position de la CAI.
- **Confiance** : vérifié dans le texte (position de la CAI : à vérifier).

### [25-16] [MINEUR] No 32 : correction « Tulving » surévaluée
- **Axe** : A
- **Localisation** : tableau 68, no 32, p. 245 : « Taxonomie à quatre types […] issue de CoALA, qui la reprend de l'architecture Soar[100] ».
- **Diagnostic** : la distinction entre mémoire épisodique et mémoire sémantique remonte à Tulving (1972), et CoALA s'appuie aussi sur la psychologie cognitive. L'ébauche (« inspirée de Tulving ») était incomplète plutôt que fausse. Classer ce point parmi les « principales corrections factuelles » le grossit.
- **Contre-exemple ou scénario de défaillance** : sans objet.
- **Correctif proposé** : écrire « issue de CoALA, qui s'inspire de Soar et de la psychologie cognitive (Tulving pour l'épisodique et le sémantique) », ou sortir la ligne du tableau.
- **Confiance** : déduit (à vérifier dans [100]).

## Points forts
- Arithmétique exacte : le tableau 69 recompté ligne par ligne redonne 61 C, 108 et 13 pour l'accès, 71/17/33 pour les décisions, et 125 + 214 + 69 + 19 = 427 pour les verdicts, conformément à F.2 et au tableau 67; 302/427 vaut bien plus de sept sur dix.
- Les corrections juridiques et normatives (nos 21-26 : art. 3.5 et 91 de la Loi sur le privé, art. 65.2 et 63.1 de la Loi sur l'accès, art. 2 du RIA, MANAGE 2.4, GOVERN 1.7, MEASURE 2.4 et 2.7) sont, à ma connaissance, exactes.
- L'auteur corrige ses propres ébauches de façon transparente (nos 10, 15, 18, 28 : retrait des chiffres sans source; facteur 3,2 = +222 % bien calculé).

## Questions pour l'audit bibliographique
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
