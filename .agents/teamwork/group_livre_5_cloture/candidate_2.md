# Rapport d'Audit Critique et Formel — Segment Livre 5 Clôture (pp. 529-585)
**Document audité** : `documents/Compendium.pdf` (Édition de novembre 2026)  
**Segment** : `segment_livre_5_cloture` (Chapitres 47 à 50, transitions vers Annexes B et I, pages 529 à 585)  
**Rôle** : Analyste L0_2 (Rigueur formelle R2 & Audit bibliographique R3)  
**Date d'évaluation** : 3 novembre 2026  

---

## 1. Synthèse exécutive du segment

Le segment « Livre V — Livrer et clore » (pp. 527-585) constitue la conclusion architecturale et opérationnelle du Compendium. Il est articulé en deux mouvements fondamentaux :
1. **L'agent comme livrable logiciel** (Chapitres 47 et 48) : la provenance de ses composants (SBOM, SLSA, in-toto, profils d'IA CycloneDX/SPDX), sa mise en service non reproductible (versionnement à cinq horloges, tests métamorphiques), et sa sémantique d'effet (idempotence des outils, compensation distribuée par sagas, réconciliation des flux financiers).
2. **L'horizon prospectif et la clôture documentaire** (Chapitres 49 et 50, complétés par les Annexes B et I) : la prospective technologique et réglementaire 2027-2032 (statuts PROGRAMMÉ, PROJETÉ, SPÉCULATIF), la frontière de la connaissance vérifiable, les événements de péremption, et le protocole de revalidation du socle de connaissances.

### Appréciation globale
Le segment se distingue par une lucidité épistémique remarquable concernant la fragilité des consensus industriels actuels : l'auteur explicite systématiquement les niveaux de preuve ([A], [B], [C]) et les degrés d'absence documentaire (degré 1 : fait négatif vérifié ; degré 2 : fait négatif établi ; degré 3 : absence de documentation). La formalisation de la sémantique d'effet et du versionnement composite aborde des angles morts critiques de l'entreprise agentique.

Néanmoins, un audit approfondi sous les axes **R2 (Rigueur formelle et algorithmique)** et **R3 (Vérification bibliographique et état de l'art)** révèle des défaillances majeures :
1. **Une substitution de portée bloquante au Chapitre 50** : alors que le chapitre promet d'établir le protocole de péremption, de recertification et de décommissionnement sécurisé *de l'agent logiciel*, il dévie entièrement vers un protocole d'auto-maintenance éditoriale et de revalidation textuelle *du manuscrit lui-même*. L'ingénierie du décommissionnement opérationnel de l'agent est totalement absente (zéro occurrence dans tout le volume).
2. **Une erreur factuelle critique sur l'idempotence (R3)** : le texte qualifie d'« expiré sans avenir » le standard d'en-tête d'idempotence de l'IETF (`draft-ietf-httpapi-idempotency-key-header`), ignorant la soumission active de la révision `-08` le 22 octobre 2026 sur la voie des standards.
3. **Un saut logique formel sur l'effet « exactly-once » (R2)** : l'affirmation selon laquelle la composition d'une livraison au-moins-une-fois et d'un consommateur idempotent garantit un effet exactement-une-fois méconnaît le problème de la double écriture (Dual-Write Problem) et les défaillances partielles des mutations distribuées multi-cibles.
4. **Une lacune algorithmique sur les Sagas (R2)** : l'analyse de compensation omet la notion mathématique de transaction pivot ($T_{\text{pivot}}$), rendant caduque la modélisation des flux financiers irréversibles.
5. **L'omission des bornes de calculabilité (théorème de Rice)** dans l'analyse de la vérifiabilité des politiques de sécurité des agents autonomes.
6. **Des corruptions typographiques et tabulaires sévères** (Tableau 47.2, p. 530 ; Tableau récapitulatif de l'Annexe I, p. 585 ; coupure textuelle au §47.4, p. 533) résultant d'erreurs d'assemblage du générateur documentaire.

---

## 2. Matrice détaillée des défauts classés par sévérité

### Légende de sévérité
- **[Bloquant / Erreur formelle]** : Invalide un théorème, une démonstration, une attribution factuelle centrale ou détruit la lisibilité d'une section entière.
- **[Majeur / Lacune méthodologique]** : Flaw conceptuel, hypothèse non démontrée ou omission structurante affaiblissant la portée des recommandations.
- **[Mineur / Clarté & Typographie]** : Coquille, saut de ligne corrompu, incohérence locale de notation sans impact sur la validité globale.

---

### DÉFAUT 1 : [Bloquant / Erreur formelle]
- **Localisation** : Chapitre 50, pp. 568-577 (§50.1 à §50.4, Tableau 50.1, Figures 50.2, 50.3, 50.4).
- **Citation textuelle** :
  > Titre : « 50 · Péremption et protocole de revalidation »  
  > §50.2 : « Tableau 50.1 — Les quatorze événements de péremption de la somme [...] »  
  > §50.3 : « Le principe : amender le socle d’abord, les chapitres ensuite — jamais l’inverse. Un fait qui évolue est d’abord constaté à sa source primaire et consigné dans un rapport de revalidation daté ; l’entrée du socle est amendée... »  
  > §50.4 : « Ce que le registre doit porter, chapitre par chapitre : statut et date de gel [...] »
- **Diagnostic causal approfondi** :
  Glissement sémantique et substitution complète d'objet. Le plan général de l'ouvrage et l'introduction du Livre V annonçaient un chapitre dédié aux « critères objectifs de fin de vie d’un modèle ou agent, tests périodiques de recertification, protocole de décommissionnement sécurisé ». Or, le texte rédigé traite exclusivement de la péremption documentaire, des dates de gel éditorial et de la maintenance textuelle des chapitres du Compendium ! Le terme « décommissionnement » n'apparaît pas une seule fois dans le chapitre ni dans l'ensemble des 663 pages du Compendium. L'ingénieur ou l'architecte d'entreprise ne dispose d'aucun protocole opérationnel pour :
  1. Révoquer cryptographiquement les clés d'identité (DIDs, Agent Cards, certificats mTLS) lors du retrait d'un agent ;
  2. Assurer le drainage gracieux des tâches en cours et des sagas non finalisées (*graceful draining*) ;
  3. Purger les mémoires épisodiques, caches sémantiques et représentations vectorielles contenant des renseignements personnels (conformément à l'art. 12.1 de la Loi 25 québécoise et à la LPRPDE/PIPEDA) ;
  4. Archiver de façon infalsifiable les traces d'audit et attestations probantes.
- **Correctif formel ou contre-exemple** :
  Scinder le Chapitre 50 en deux parties étanches :
  - **Partie I (§50.1 à §50.4 restructurés)** : Protocole opérationnel de cycle de vie et de fin de vie des agents :
    * Critères objectifs de fin de vie : dérive de calibration statistique ($KL > \epsilon$), dépréciation de l'API sous-jacente du modèle par le fournisseur, faille critique CVE non patchable sur le serveur d'outils, expiration d'accréditation prudentielle (OSFI E-23).
    * Protocole de recertification périodique : exécution automatisée de bancs de tests métamorphiques (Chen et al., 2018), validation d'intégrité de la sandbox d'exécution, audit des frontières d'autorisation.
    * Protocole formel de décommissionnement sécurisé en 5 phases : (1) Isolement réseau / coupure de trafic au PDP/PEP, (2) Dépouillement des mandats et révocation dans le registre gouverné (CRL / OCSP / DID revokable status list), (3) Drainage et terminaison compensée des transactions asynchrones, (4) Purge cryptographique des mémoires locales et des contextes de session, (5) Scellement et horodatage de l'archive d'audit probatoire.
  - **Partie II (§50.5)** : Protocole d'actualisation documentaire du socle de connaissances.

---

### DÉFAUT 2 : [Bloquant / Erreur formelle]
- **Localisation** : Chapitre 48, p. 544, §48.5 (dernière sous-section, 4e paragraphe).
- **Citation textuelle** :
  > « Le brouillon draft-ietf-httpapi-idempotency-key-header, The Idempotency-Key HTTP Header Field, de Jena et Dalal, groupe de travail httpapi de l’IETF [...] Son statut se dit à chaque mention et il est sévère : révision −07 du 15 octobre 2025, et le document est EXPIRÉ — il n’a pas atteint le stade de RFC, et rien n’établit qu’il l’atteindra. La conclusion du § 48.2 n’est donc pas levée : l’écosystème n’a même pas d’en-tête normalisé pour dire « ceci est un réessai » — il en a eu un projet, et ce projet a expiré, ce qui est un constat plus dur que l’absence pure. »
- **Diagnostic causal approfondi** :
  Erreur factuelle et anachronisme bibliographique contredisant l'état de l'art à la date de compilation de l'ouvrage (fin octobre 2026).
  Le projet de standard `draft-ietf-httpapi-idempotency-key-header` n'a jamais été abandonné. La révision `draft-ietf-httpapi-idempotency-key-header-08` a été officiellement soumise le **22 octobre 2026** par Jayadeba Jena et Sanjay Dalal au sein du groupe de travail IETF HTTPAPI, renouvelant sa validité active jusqu'au **25 avril 2027** sur la voie des standards (Standards Track).
  L'auteur a confondu l'expiration calendaire automatique (cycle semestriel des Internet-Drafts) avec une clôture de projet. Cette erreur vicie directement la conclusion du chapitre 48, affirmant à tort que l'industrie a renoncé à standardiser la clé d'idempotence au niveau applicatif HTTP.
- **Correctif formel ou contre-exemple** :
  Remplacer le passage par :
  > « Le brouillon `draft-ietf-httpapi-idempotency-key-header`, *The Idempotency-Key HTTP Header Field* (Jena & Dalal), a franchi sa révision −08 le 22 octobre 2026 au sein du groupe IETF HTTPAPI, restant actif jusqu’au 25 avril 2027 sur la voie des standards. Si l’en-tête `Idempotency-Key` progresse activement vers la publication en RFC, son intégration obligatoire au niveau des protocoles agentiques (MCP, A2A) demeure non spécifiée : la clé reste un mécanisme de couche transport HTTP, découplé de la sémantique de planification de l’agent. »

---

### DÉFAUT 3 : [Bloquant / Erreur formelle]
- **Localisation** : Chapitre 47, p. 530, Tableau 47.2.
- **Citation textuelle** :
  > Tableau 47.2 :
  > Ligne 2 : « obre 2025 par l’OWASP et Ecma International, normalisée ECMA-424 le 10 décembre 2025 ; précision relevée le 30 juillet 2026 : c’en est la 2ᵉ édition... » (Colonne 2 vide).  
  > Ligne 3 : « ée sous la Fondation Linux, organisée en deux pistes — Build et Source ; approuvée le 24 novembre 2025... »  
  > Colonne 2 de la ligne 3 : « 2026) ; le projet se déclare norme internationale ISO/IEC 5962:2021 »  
  > Colonne 3 de la ligne 3 : fusionne sans transition la réserve de SLSA et la réserve de SPDX.  
  > Texte orphelin rejeté sous la table : « 2026, et elle se résout »
- **Diagnostic causal approfondi** :
  Corruption majeure du tableau source LaTeX / Pandoc lors de la compilation du PDF (visible sur `page-530.png`).
  1. Le titre de CycloneDX 1.7 est tronqué (« obre 2025 » au lieu de « CycloneDX 1.7, publié en octobre 2025... »), placé en colonne 1 au lieu de la colonne 2, laissant la colonne de description vide.
  2. Le titre de SLSA v1.2 est tronqué (« ée sous la Fondation Linux » au lieu de « SLSA v1.2, spécification développée sous la Fondation Linux... »).
  3. L'entrée SPDX 3.0 a perdu sa ligne propre : ses attributs sont écrasés dans la colonne 2 de la ligne SLSA (« le projet se déclare norme internationale ISO/IEC 5962:2021 »).
  4. La colonne des réserves fusionne en un seul bloc textuel la fin de la réserve SLSA (sur l'énumération des niveaux) et la réserve SPDX (sur le fait qu'ISO/IEC 5962:2021 fixe SPDX 2.2.1 et non 3.x).
  5. Un fragment orphelin (« 2026, et elle se résout ») flotte sous le tableau.
  La table est structurellement inintelligible dans l'édition imprimée.
- **Correctif formel ou contre-exemple** :
  Rétablir la table selon la structure suivante à 5 rangées strictes :
  | Document relevé | Ce que la relève porte | Réserve portée par la relève elle-même |
  | :--- | :--- | :--- |
  | **in-toto Attestation Framework** (spécification v1) | Cadre d’attestation du projet in-toto, hébergé par la CNCF. | Le niveau de maturité CNCF du projet n’est pas porté par la page relevée. |
  | **CycloneDX v1.7** (ECMA-424, 2ᵉ édition) | Publié en octobre 2025 par l’OWASP et normalisé ECMA-424 le 10 décembre 2025 (2ᵉ éd. succédant à la 1ʳᵉ éd. sur v1.6 en juin 2024). | Fait à distinguer d’un format d’éditeur : c’est une nomenclature devenue norme d’organisme. Doit se citer avec son édition. |
  | **SLSA v1.2** (Supply-chain Levels for Software Artifacts) | Spécification développée sous la Fondation Linux, organisée en deux pistes — Build et Source ; approuvée le 24 novembre 2025. | Spécifie les Verification Summary Attestations (VSAs) ; l’énumération des niveaux Source (L1-L4) reste à instruire à source primaire. |
  | **SPDX 3.0** (profils AI et Dataset) | Modèle d'échange d'informations logicielles et d'IA de la Fondation Linux ; le projet se déclare norme internationale ISO/IEC 5962:2021. | **Réserve levée contre l'énoncé du projet** : ISO/IEC 5962:2021 fixe formellement SPDX 2.2.1, et non la version 3.0. |
  | **NIST SP 800-218A** | Secure Software Development Practices for Generative AI and Dual-Use Foundation Models (SSDF Community Profile, 26 juillet 2024). | Profil communautaire d'orientation, non une norme imposant conformité réglementaire directe. |

---

### DÉFAUT 4 : [Bloquant / Erreur formelle]
- **Localisation** : Chapitre 48, p. 539, §48.1.
- **Citation textuelle** :
  > « Le ch. 1 § 1.5.2 établit que la livraison exactement-une-fois est irréalisable sous pannes — instance du problème des deux généraux —, et que la voie praticable est le traitement exactement-une-fois, obtenu en combinant une livraison au-moins-une-fois avec un consommateur idempotent. Ce chapitre en tire la conséquence que le ch. 1 lui assigne : si la livraison ne peut être garantie, l’effet doit l’être ; et c’est l’effet, non le message, que la sémantique de ce chapitre prend pour objet. »
- **Diagnostic causal approfondi** :
  Raisonnement formel fallacieux sur la composition distribuée de l'idempotence sous pannes partielles.
  L'affirmation selon laquelle « la livraison au-moins-une-fois + un consommateur idempotent garantit un traitement exactement-une-fois (ou un effet exactement-une-fois) » est mathématiquement et algorithmiquement fausse sans hypothèses additionnelles très contraignantes :
  1. **Le problème de la double écriture (*Dual-Write Problem*)** : Si le consommateur exécute la mutation de l'effet de bord sur un système tiers (ex. virement bancaire, appel d'outil MCP externe) et s'effondre avant d'enregistrer la clé d'idempotence dans son magasin local d'état, le rejeu entraînera l'exécution d'un doublon de l'effet de bord. L'effet n'est donc pas « exactement-une-fois ».
  2. **Atomicité multi-cibles** : Un agent produit rarement une mutation atomique unique. S'il invoque l'outil A puis l'outil B, l'idempotence unitaire de A et de B ne protège pas contre un crash survenu entre A et B.
  3. **Concurrence sans linéarisation** : Si deux requêtes identiques arrivent simultanément sur deux réplicas de l'agent ou de l'outil, en l'absence d'un verrou distribué linéarisable (ex. CAS distribué sur consensus Raft), les deux exécutions s'exécutent en parallèle avant que la clé ne soit marquée « en cours » ou « complétée ».
- **Correctif formel ou contre-exemple** :
  Corriger la démonstration :
  Soit $S$ l'état du système d'enregistrement et $f: S \times A \to S$ l'effet d'une action $a$. L'idempotence ($f(f(s, a), a) = f(s, a)$) ne garantit un effet *exactly-once* sous modèle de panne par crash-recovery que si la transition d'état et l'enregistrement du jeton d'idempotence $k \in K$ constituent une transaction atomique isolée :
  $$\langle s', K \cup \{k\} \rangle = \text{AtomicCommit}(s, a, k)$$
  Dès lors que l'action $a$ implique un effet externe distribué hors de la frontière transactionnelle du gestionnaire de clés (cas systématique des serveurs d'outils distants en MCP/A2A), le théorème de non-coordination et le problème de la double écriture interdisent de garantir formellement l'effet *exactly-once* sans protocole de consensus à deux phases (2PC) ou patron Outbox transactionnel.

---

### DÉFAUT 5 : [Majeur / Lacune méthodologique]
- **Localisation** : Chapitre 48, pp. 541-542 (§48.3, Figure 48.3).
- **Citation textuelle** :
  > « Une saga classique suppose que l’ensemble des étapes soit connu du concepteur : la compensation de l’étape k est écrite en même temps que l’étape k. Un agent qui compose sa trajectoire à l’exécution [...] produit des suites d’étapes que personne n’a écrites, donc des suites dont personne n’a écrit les compensations. »
- **Diagnostic causal approfondi** :
  Modélisation tronquée du patron Saga et confusion sur l'inversion de trajectoire :
  1. **Omission de la transaction pivot ($T_{\text{pivot}}$)** : Dans la théorie formelle des Sagas (Garcia-Molina & Salem, 1987), toute saga se décompose rigoureusement en trois classes d'étapes :
     - Les transactions compensables ($T_1, \dots, T_{p-1}$), associées à des compensations sémantiques ($C_1, \dots, C_{p-1}$) ;
     - La transaction pivot ($T_p$), point de non-retour qui ne peut être ni annulé ni compensé ;
     - Les transactions rejouables ($T_{p+1}, \dots, T_n$), qui doivent obligatoirement réussir et être réessayées jusqu'à succès (*forward recovery*).
     L'affirmation du Compendium prétendant que toute étape non annulable relève d'une compensation sémantique est formellement fausse : un virement de fonds irréversible ou un tir réel est une transaction pivot. En aval du pivot, la compensation est impossible et seule la stratégie *forward recovery* est admissible.
  2. **Génération dynamique des compensations** : L'affirmation selon laquelle « personne n'a écrit les compensations » pour un plan dynamique ignore les architectures d'outils modernes où chaque capacité atomique $t_i$ déclare son opérateur inverse $C(t_i)$ (ex. `réserver_chambre` $\leftrightarrow$ `annuler_réservation`). L'orchestrateur déterministe applique simplement la règle d'inversion algébrique du mot d'exécution : si le plan exécuté est $w = t_1 t_2 \dots t_k$, le plan compensatoire est $w^{-1} = C(t_k) \dots C(t_2) C(t_1)$.
  3. **Défaillance de l'action compensatoire** : Le texte ignore totalement le scénario critique où la compensation $C_i$ elle-même échoue (ex. timeout, indisponibilité de l'API bancaire), ce qui plonge le système dans un état d'incohérence irréversible sans procédure d'escalade.
- **Correctif formel ou contre-exemple** :
  Introduire la formalisation complète de Garcia-Molina & Salem (1987) :
  $$\text{Saga} = \langle (T_1, C_1), (T_2, C_2), \dots, T_{\text{pivot}}, T_{p+1}, \dots, T_n \rangle$$
  Poser les règles d'architecture impératives pour les agents planificateurs :
  - Interdiction pour un planificateur dynamique d'exécuter des actions à compensation non définie en amont du pivot.
  - Obligation d'idempotence stricte sur chaque action compensatoire $C_i$.
  - Définition d'un protocole d'escalade en quarantaine (*quarantine state*) lorsque $C_i$ échoue de manière répétée.

---

### DÉFAUT 6 : [Majeur / Lacune méthodologique]
- **Localisation** : Chapitre 49, pp. 552-554 (§49.6.2, §49.6.5) et pp. 558-559 (§49.10).
- **Citation textuelle** :
  > §49.6.2 : « Garanties composables sur des acteurs probabilistes [...] sous quelles conditions une propriété vérifiée localement sur chaque agent se transmet-elle à leur agencement ? »  
  > §49.10 : « Le verrou est formel, et c’est un résultat d’impossibilité : le Vol. I relève un théorème selon lequel aucun cadre de gouvernance ne peut satisfaire simultanément quatre propriétés — attributabilité, borne de prévisibilité, non-vacuité et complétude — pour des collectifs humains-agents. Statut SPÉCULATIF mais argumenté... »
- **Diagnostic causal approfondi** :
  1. **Omission des limites de calculabilité (Théorème de Rice, 1953)** : Le Compendium débat de la sécurité formelle des frontières, de la composition de contrats de sécurité et de la vérification dynamique sans jamais faire référence au théorème de Rice : toute propriété sémantique non triviale portant sur le comportement d'un programme Turing-complet est indécidable. Un agent autonome couplé à un LLM et à des outils arbitraires constituant un système universel, la vérification statique ou dynamique a priori de son alignement, de son absence d'effets malveillants ou de sa conformité à une politique de sécurité complexe est formellement indécidable. L'omission de cette borne théorique amène le texte à traiter comme de simples « défis d'outillage » des limites fondamentales de l'informatique théorique.
  2. **Oxymore épistémique au §49.10** : Qualifier un « théorème » mathématique de résultat au statut « SPÉCULATIF » constitue une contradiction méthodologique majeure. Si un énoncé est un théorème, il dispose d'une preuve formelle dans un système axiomatique donné (et relève donc d'un FAIT ÉTABLI sous ces axiomes). S'il n'est pas démontré, il s'agit d'une conjecture ou d'une intuition de recherche. De plus, les quatre propriétés mentionnées (« attributabilité, borne de prévisibilité, non-vacuité et complétude ») ne reçoivent aucune définition formelle, mathématique ou logique dans l'ensemble de l'ouvrage, et aucune source ou papier fondateur n'est cité pour ce prétendu résultat.
- **Correctif formel ou contre-exemple** :
  - Réarticuler le §49.6 autour des limites formelles de Schneider (2000) et Rice (1953) : démontrer que seules les propriétés de sécurité (*safety properties*, exprimables par des automates de sécurité tronquant les traces interdites au PDP/PEP) sont décidables à l'exécution, tandis que les propriétés de vivacité (*liveness*) ou les propriétés hyper-spécifiques d'alignement global sont indécidables.
  - Rectifier le §49.10 : requalifier le prétendu « théorème » en *conjecture de gouvernance multi-agents*, ou formaliser mathématiquement l'incompatibilité sous forme d'un théorème d'impossibilité de choix social (analogue aux théorèmes d'Arrow ou de Gibbard-Satterthwaite appliqués aux systèmes multi-agents), en citant explicitement la preuve et les conditions de bord.

---

### DÉFAUT 7 : [Majeur / Lacune méthodologique]
- **Localisation** : Chapitre 47, pp. 527-529 (§47.1, Tableau 47.1) et p. 535 (§47.8, §47.8.1).
- **Citation textuelle** :
  > Tableau 47.1 : Les cinq composants : « Poids de modèle, Serveurs d’outils, Bibliothèques et hôte d’exécution, Invites et fichiers d’instructions, Politique d’autorisation ».  
  > §47.8 : « La thèse du second mouvement pose cinq horloges — modèle, invites, outils, politique, et le harnais — et le § 47.1 en a inventorié cinq composants ; les deux quintets ne se recouvrent pas. L’écart n’est pas une erreur d’arithmétique : le tableau 47.1 distingue les bibliothèques et l’hôte d’exécution des serveurs d’outils, là où la thèse les range ensemble, et il ne porte pas le harnais, que la thèse porte. Le chapitre suit la thèse pour le décompte et le tableau pour l’inventaire... »
- **Diagnostic causal approfondi** :
  Divergence taxonomique non arbitrée au sein d'un même chapitre.
  Le modèle d'artefact logiciel de l'agent est le pilier du Livre V. Or, l'auteur maintient délibérément deux quintuplets incompatibles :
  - Quintuplet 1 (Tableau 47.1) : Modèle, Outils, Bibliothèques/Hôte, Invites, Politique.
  - Quintuplet 2 (Thèse & §47.8) : Modèle, Invites, Outils, Politique, Harnais.
  Cette dissonance paralyse la mise en œuvre pratique de l'ingénierie de release (CI/CD GitOps) décrite au §47.10 : quel est l'objet scellé dans le manifeste SBOM / SLSA ? Le harnais est-il un composant de l'agent ou son environnement d'accueil ? En laissant cette question sans réponse (« le chapitre suit la thèse pour le décompte et le tableau pour l'inventaire »), le texte abdique son rôle de spécification d'architecture.
- **Correctif formel ou contre-exemple** :
  Formaliser une taxonomie rigoureuse à deux niveaux (modèle conteneur / contenu) :
  $$\text{Artefact}_{\text{Agent}} = \langle \text{ExecutionHarness}, \text{AgentPayload} \rangle$$
  où :
  1. $\text{ExecutionHarness}$ englobe le binaire hôte, le runtime et les bibliothèques d'exécution (versionné par l'éditeur / la plateforme) ;
  2. $\text{AgentPayload}$ est un quadruplet déclaré : $\langle \text{ModelWeightsURI}_{\text{hash}}, \text{SystemPrompts}_{\text{hash}}, \text{ToolContractSet}_{\text{hash}}, \text{SecurityPolicy}_{\text{hash}} \rangle$.
  Cette formalisation réconcilie immédiatement les deux vues sous un schéma de manifeste unique et vérifiable par in-toto / SLSA.

---

### DÉFAUT 8 : [Mineur / Clarté & Typographie]
- **Localisation** : Chapitre 48, p. 542, §48.3.
- **Citation textuelle** :
  > « Un fait est consigné ici parce qu’il se lit mal ailleurs : cette section est la seule occurrence de « sagas » de toute la somme, et elle l’est au grain d’une action unique. »
- **Diagnostic causal approfondi** :
  Contradiction textuelle interne flagrante.
  Le terme « sagas » / « patron saga » et les travaux fondateurs de Garcia-Molina et Salem (1987) apparaissent explicitement :
  1. Au Chapitre 1, §1.6.2.2 (p. 20, ligne 1776 du texte brut) : « Le patron saga (Garcia-Molina et Salem, 1987) renonce à l’atomicité globale au profit d’une suite de transactions locales... » ;
  2. Dans l'Annexe I (p. 611, ligne 55272 du texte brut) : entrée bibliographique complète de Garcia-Molina & Salem (1987).
  L'assertion du §48.3 est donc factuellement réfutée par le texte même du Compendium.
- **Correctif formel ou contre-exemple** :
  Corriger la formulation :
  > « Cette section est la seule occurrence de l'application du patron saga à la compensation d'une trajectoire agentique composée dynamiquement à l'exécution, son socle pré-agentique ayant été posé au ch. 1 § 1.6.2.2. »

---

### DÉFAUT 9 : [Mineur / Clarté & Typographie]
- **Localisation** : Chapitre 47, p. 533, §47.4.
- **Citation textuelle** :
  > « ...le retournement a un grain plus fin que le serveur d’outils — l’extension déclarative du harnais —, [saut de paragraphe]
  > Cette section ne rejoue pas le retournement : elle le relit. Le ch. 20 § 20.1 en est le siège [...] sans prescrire de le relier à ce qui avait été consenti. et l’incident public candidat est décrit au ch. 47 § 47.7, qui l’instruit et déclare son propre défaut d’attribution. »
- **Diagnostic causal approfondi** :
  Erreur de découpage de paragraphe et d'insertion textuelle (visible sur `page-533.png`).
  Le premier paragraphe en texte romain se termine de façon suspendue par un tiret cadratin et une virgule (« ...du harnais —, »). La proposition qui devait logiquement achever cette phrase a été injectée par accident au milieu du paragraphe suivant en italique (« ...consenti. et l’incident public... »), débutant par une minuscule après un point.
- **Correctif formel ou contre-exemple** :
  Rétablir la continuité syntaxique :
  1. Fin du paragraphe 1 : « ...le retournement a un grain plus fin que le serveur d’outils — l’extension déclarative du harnais —, et l’incident public candidat est décrit au ch. 47 § 47.7, qui l’instruit et déclare son propre défaut d’attribution. »
  2. Paragraphe 2 en italique : clore la phrase sur « ...sans prescrire de le relier à ce qui avait été consenti. Forme re-vérifiée mot à mot contre sa cible au 28 juillet 2026... »

---

### DÉFAUT 10 : [Mineur / Clarté & Typographie]
- **Localisation** : Annexe I, p. 585 (Tableau récapitulatif des mesures et pied de page).
- **Citation textuelle** :
  > Tableau « Mesure / Valeur » :
  > « Entrées relevées aux sept bibliographies du Vol. I : 1263 »  
  > « Doublons fondus par identifiant normalisé : [vide] »  
  > « Entrées uniques de la présente annexe : [vide] »  
  > « Adresses primaires reprises des socles des Vol. II et III : 0 »  
  > Sous la table (en puce isolée) : « • 134 1065 »
- **Diagnostic causal approfondi** :
  Rupture de mise en page LaTeX / Markdown (visible sur `page-585.png`).
  Les valeurs numériques correspondant aux doublons (134) et aux entrées uniques (1065) ont débordé de l'environnement de table et ont été éjectées sous la forme d'un élément de liste orphelin « • 134 1065 ».
  De plus, un problème arithmétique non explicité apparaît :
  $$1263 - 134 = 1129 \neq 1065$$
  Il existe un différentiel de 64 entrées (1129 - 1065 = 64) qui n'est ni commenté ni justifié (s'agit-il de notices rejetées, d'entrées non résolues ou d'un calcul erroné de doublons : $1263 - 198 = 1065$ ?).
- **Correctif formel ou contre-exemple** :
  Réinsérer les valeurs dans les cellules du tableau et expliciter la réconciliation arithmétique : indiquer si le nombre réel de doublons éliminés est de 198, ou identifier formellement les 64 références exclues pour défaut d'identifiant.

---

## 3. Audit bibliographique et état de l'art (Axe R3)

### 3.1 Vérification des références citées dans le segment

| Référence citée | Statut vérifié | Précision bibliographique & Analyse critique |
| :--- | :---: | :--- |
| **Chen et al. (2018)**, *Metamorphic Testing: A Review of Challenges and Opportunities*, ACM CSUR 51(1), art. 4. | **EXACT** | DOI `10.1145/3143561`. Référence fondatrice sur le problème de l'oracle dans les systèmes non déterministes. Cité très opportunément au §47.9 pour la barrière de mise en service. |
| **NIST SP 800-218A** (26 juillet 2024), *Secure Software Development Practices for Generative AI...* | **EXACT** | Version finale du profil communautaire SSDF v1.1 publiée le 26 juillet 2024. Cité adéquatement comme cadre d'orientation non prescriptif au §47.2. |
| **RFC 9334** (Janvier 2023), *RATS Architecture*. | **EXACT** | RFC Informational publiée par Birkholz, Thaler, Richardson, Smith, Pan. Les rôles (Attester, Verifier, Relying Party) sont fidèlement transcrits au §47.3.1. |
| **CycloneDX 1.7 / ECMA-424 (2ᵉ éd.)** (Déc. 2025). | **EXACT** | Ratification officielle par l'Assemblée générale d'Ecma International en décembre 2025 de CycloneDX 1.7 sous ECMA-424 2nd edition. |
| **SLSA v1.2** (Build & Source Tracks). | **EXACT** | Évolution de SLSA 1.0 intégrant la formalisation de la piste Source (Source L1-L4) et des attestations de vérification VSA via in-toto. |
| **Garcia-Molina & Salem (1987)**, *Sagas*, ACM SIGMOD, pp. 249-259. | **EXACT** | DOI `10.1145/38713.38742`. Papier princeps sur les transactions longues sans verrous globaux. |
| **Trout et al. (juillet 2026)**, *Underwriting the Agent Economy...*, arXiv:2607.11999. | **EXACT** | Prépublication réelle `cs.CY` (Trout, Koyejo, Romanosky et al.) modélisant une pile d'assurance à 8 couches pour les agents autonomes. |
| **Règlement Omnibus Numérique IA (UE) 2026/1744** (29 juin 2026). | **EXACT** | Adoption par le Conseil de l'UE le 29 juin 2026 reportant l'application du haut-risque (Annexe III) au 2 décembre 2027. Cité correctement au §49.1.4. |
| **`draft-ietf-httpapi-idempotency-key-header`** (Jena & Dalal). | **ERRONÉ** | Faussement qualifié d'« expiré définitivement ». La révision `-08` a été soumise le 22 octobre 2026 au groupe IETF HTTPAPI (actif jusqu'en avril 2027). |

---

### 3.2 Références fondamentales et récentes (2024-2026) omises

L'analyse du Livre V souffre de lacunes bibliographiques critiques qui affaiblissent directement les démonstrations techniques :

1. **Calculabilité et décidabilité des politiques de sécurité (Ch. 49) :**
   - **Rice, H. G. (1953)**, *Classes of Recursively Enumerable Sets and Their Decision Problems*, Transactions of the American Mathematical Society, 74(2), pp. 358-366.  
     *Impact de l'omission* : Fondement mathématique absolu démontrant l'indécidabilité de la vérification sémantique dynamique des agents autonomes.
   - **Schneider, F. B. (2000)**, *Enforceable Security Policies*, ACM Transactions on Information and System Security (TISSEC), 3(1), pp. 30-50.  
     *Impact de l'omission* : Établit la frontière formelle entre ce qu'un moniteur de référence (PEP/PDP) peut exécuter (propriétés de sûreté / *safety properties*) et ce qu'il ne peut pas interdire sans blocage complet (*liveness properties*). Indispensable pour théoriser le confinement d'agents au §49.6.5.

2. **Ingénierie transactionnelle distribuée et exécution durable (Ch. 48) :**
   - **Richardson, C. (2018)**, *Microservices Patterns: With examples in Java*, Manning Publications (Chapitre 4 : *Managing transactions with sagas* & Chapitre 3 : *The Transactional Outbox Pattern*).  
     *Impact de l'omission* : Fournit la solution architecturale au *Dual-Write Problem* et à la persistance coordonnée des clés d'idempotence et des effets d'outils.
   - **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985)**, *Impossibility of Distributed Consensus with One Unreliable Process (FLP)*, Journal of the ACM, 32(2), pp. 374-382.  
     *Impact de l'omission* : Démontre l'impossibilité d'atteindre un accord déterministe en asynchronie pure, ce qui invalide l'hypothèse d'une réconciliation sans heuristique sur les réseaux inter-agents ouverts.

3. **Décommissionnement, fin de vie et gouvernance opérationnelle de l'IA (Ch. 50) :**
   - **NIST AI 100-1 (2023)**, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, Section « Govern » & « Manage » (directives spécifiques sur le décommissionnement et le retrait sécurisé des modèles).
   - **ISO/IEC 42001:2023**, *Information technology — Artificial intelligence — Management system*, Annexe A.8 (Cycle de vie et mise hors service des systèmes d'intelligence artificielle).
   - **BSIF / OSFI (2025)**, *Ligne directrice E-23 : Gestion du risque de modélisation*, section sur la clôture du modèle, l'invalidation des hypothèses et l'archivage réglementaire probatoire.  
     *Impact de l'omission* : L'absence de ces cadres institutionnels dans le Chapitre 50 est directement responsable de la substitution de l'objet du chapitre par une procédure d'actualisation de texte.

4. **Nomenclatures d'IA et packaging d'agents (Ch. 47) :**
   - **Mitchell, M. et al. (2019)**, *Model Cards for Model Reporting*, Proceedings of the ACM FAccT, pp. 220-229. Origine directe des classes d'attributs intégrées dans CycloneDX 1.6/1.7 et SPDX 3.0.
   - **OpenSSF (2025/2026)**, *SLSA for Machine Learning (SLSA-ML Specification)* : adaptation spécifique des niveaux SLSA à la traçabilité des jeux de données, des hyperparamètres et des poids de modèles.

---

## 4. Recommandations concrètes pour le segment

1. **Restructurer d'urgence le Chapitre 50** : Rédiger le protocole opérationnel de décommissionnement des agents d'entreprise (révocation cryptographique, purge mémoire Loi 25/PIPEDA, drainage des sagas, archivage légal) et déplacer la procédure de revalidation du manuscrit dans un chapitre d'appareil documentaire (Annexe N).
2. **Corriger la notice IETF au Chapitre 48 (§48.5)** : Réintégrer la révision active `draft-ietf-httpapi-idempotency-key-header-08` du 22 octobre 2026 et requalifier la conclusion sur l'en-tête d'idempotence.
3. **Rigidifier la démonstration de la sémantique d'effet au §48.1** : Éliminer la fausse équivalence sur l'effet « exactly-once », expliciter le problème de la double écriture et formaliser le patron *Transactional Outbox* comme condition sine qua non de l'idempotence des outils distribués.
4. **Compléter la théorie des Sagas au §48.3** : Intégrer les concepts formels de transaction pivot ($T_{\text{pivot}}$), d'inversion dynamique de trace d'exécution ($w^{-1}$) et de gestion des défaillances de compensation.
5. **Intégrer les limites de calculabilité (Rice, Schneider) au Chapitre 49** : Refonder la réflexion sur la vérifiabilité des politiques d'agents en distinguant formellement l'indécidabilité de l'alignement sémantique dynamique et la décidabilité du confinement par automates finis d'exécution.
6. **Résoudre l'incohérence taxonomique du Chapitre 47** : Fusionner le Tableau 47.1 et la thèse du §47.8 sous un modèle rigoureux liant le harnais d'exécution (hôte) et le manifeste composite (modèle, invites, outils, politique).
7. **Corriger les 3 corruptions matérielles de mise en page dans le pipeline Pandoc/LaTeX** :
   - Recomposer intégralement le Tableau 47.2 (p. 530) ;
   - Rétablir la continuité textuelle au §47.4 (p. 533) ;
   - Corriger la table de ventilation de l'Annexe I (p. 585) et son différentiel arithmétique.
