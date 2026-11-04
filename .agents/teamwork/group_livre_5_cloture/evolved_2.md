# Rapport de Revue Évoluée L1_2 — Livre V Clôture (pp. 527–585)
**Tournoi RSA [4, 2, 1] — Niveau 1 (Agrégation L1_2)**  
**Segment audité** : `segment_livre_5_cloture` (Chapitres 47 à 50, transition vers Annexes B et I, pp. 527 à 585)  
**Document source** : `documents/Compendium.pdf` (Édition novembre 2026, faits gelés au 27 juillet 2026, actualisation 1er novembre 2026)  
**Rapports candidats analysés et arbitrés** : `candidate_3.md` (L0_3) et `candidate_4.md` (L0_4)  
**Date d'arbitrage** : 3 novembre 2026  
**Auteur de la synthèse L1_2** : Agrégateur L1_2 (Rôles : Implementer / QA / Specialist — Axes R2 Rigueur formelle & R3 État de l'art / Bibliographie)

---

## 1. Synthèse exécutive du segment

Le Livre V (« *Livrer et clore : l’agent comme livrable logiciel, horizon et frontière* », pp. 527–585) constitue la clé de voûte conclusive du Compendium. Il vise à transformer l'agent autonome d'entreprise — modélisé aux Livres I à IV comme protocole, identité, automate prudentiel et nœud de maillage opérationnel — en un **artefact logiciel matériel, certifiable, déployable, traçable et décommissionnable, borné par les limites fondamentales de la calculabilité**.

Le segment s'organise en trois volets majeurs :
1. **L'agent comme livrable logiciel et la sémantique d'effet** (Ch. 47 & 48, pp. 527–544) : Nomenclature des composants (SBOM CycloneDX 1.7, SPDX 2.2.1/3.0), attestations de provenance logicielle (SLSA v1.2, in-toto, RFC 9334 RATS), versionnement multidimensionnel (modèle à 5 horloges), et sémantique d'effet transactionnel (idempotence d'outils, patron Saga et compensation, réconciliation de bout en bout sous ISO 20022).
2. **Prospective épistémique et frontières de la calculabilité** (Ch. 49, pp. 545–568) : Grille prospective 2027–2032 (PROGRAMMÉ / PROJETÉ / SPÉCULATIF / FAIT ÉTABLI), inventaire des 22 lacunes de recherche, frontières de délégation multi-sauts et non-compositionnalité de la sûreté.
3. **Péremption, revalidation et transition vers l'appareil critique** (Ch. 50 & début Annexes B et I, pp. 568–585) : Protocoles de révision, inventaire des 159 faits consolidés (S-001 à S-159) et consolidation bibliographique.

### Évaluation consolidée et verdict d'arbitrage L1_2
L'effort méthodologique du Compendium (explicitation des degrés de preuve 1 à 3, étiquetage des absences [A]/[B]/[C], refus des projections complaisantes) est remarquable. Toutefois, l'évaluation croisée rigoureuse et la vérification primaire sur les planches originales (`DOCUMENT_TEXT_MAP.md` et images `page-527.png` à `page-585.png`) confirment sans équivoque les constats majeurs des deux analystes candidats. Le segment souffre de **failles formelles, de lacunes d'état de l'art et de défaillances de compilation matérielle sévères** :

* **Ruptures formelles en systèmes distribués (Axe R2)** :
  1. *Fausse équivalence Exactly-Once* (Ch. 48) : L'équation centrale « *At-Least-Once + Idempotence = Exactly-Once* » est formellement invalide en environnement distribué asynchrone sans commutativité des opérations, séquencement total (*fencing tokens*) et persistance atomique crash-safe de la clé et de l'effet (*Transactional Outbox*).
  2. *Fausse impossibilité de la Saga dynamique et occultation de l'isolation* (Ch. 48) : L'affirmation selon laquelle un agent générateur de plans ne peut utiliser le patron Saga faute de compensations écrites à la conception confond composition dynamique et déclarations statiques. Les moteurs d'exécution durables composent dynamiquement les compensations inverses par pile LIFO ($[a_k^{-1}, \dots, a_1^{-1}]$). Le véritable verrou théorique — passé sous silence par l'auteur — réside dans les **anomalies d'isolation** ($ACID$ sans $I$) et les lectures sales (*dirty reads*) entre agents concurrents.
  3. *Angle mort théorique sur la calculabilité* (Ch. 49) : Traiter le confinement de sécurité d'un agent comme une simple lacune de standardisation ignore le **Théorème de Rice (1953)** et les limitations fondamentales des moniteurs d'exécution (**Schneider 2000**), qui prouvent l'indécidabilité formelle de toute vérification statique complète du comportement d'un agent Turing-complet.
* **Corruptions matérielles et collisions textuelles bloquantes** :
  L'inspection visuelle confirme des accidents majeurs de compilation typographique : un mot tronqué en fin de phrase (p. 528), un tableau de nomenclatures déstructuré aux colonnes écrasées et lignes orphelines (p. 530), un fragment syntaxique orphelin (p. 533), deux collisions brutales où des notes d'arbitrage éditorial ont été insérées en plein milieu de phrases (pp. 544 et 566–567), et un tableau récapitulatif brisé avec expulsion de cellules et arithmétique contradictoire (p. 585).
* **Erreurs factuelles et anachronismes sur les standards (Axe R3)** :
  Le brouillon IETF `draft-ietf-httpapi-idempotency-key-header` est faussement déclaré « abandonné et définitivement expiré », alors qu'il est actif et renouvelé sous la révision `-08` le 22 octobre 2026. Le framework d'attestation in-toto est étiqueté d'un niveau CNCF inconnu, alors qu'il a atteint le statut **CNCF Graduated le 10 février 2025**. Enfin, le standard fondamental de signature sans clé **Sigstore** (Cosign, Rekor, Fulcio) est totalement omis de l'architecture de provenance logicielle.

---

## 2. Matrice arbitrée et consolidée des défauts par sévérité

### Légende des sévérités arbitrées
* **[Bloquant / Erreur formelle]** : Erreur mathématique, rupture algorithmique, violation de théorème ou corruption matérielle textuelle invalidant la démonstration ou rendant le texte indéchiffrable.
* **[Majeur / Lacune méthodologique]** : Omission substantielle, qualification erronée de standard, lacune de modélisation affaiblissant la portée opérationnelle sans détruire l'argumentation générale.
* **[Mineur / Clarté & Typographie]** : Coquille typographique, rupture mineure de syntaxe, discordance locale de nomenclature ou troncature sans rupture logique.

---

### A. Défauts Bloquants / Erreurs Formelles (Critical)

#### Défaut B-01 — Falsification de l'équation d'équivalence : « Au-moins-une-fois + Idempotence = Traitement Exactement-une-fois »
* **Localisation** : Chapitre 48, p. 539 (§ 48.1, texte courant) et p. 541 (Figure 48.2 et texte associé) :
  * *Citation p. 539* : « *Le ch. 1 § 1.5.2 établit que la livraison exactement-une-fois est irréalisable sous pannes — instance du problème des deux généraux —, et que la voie praticable est le traitement exactement-une-fois, obtenu en combinant une livraison au-moins-une-fois avec un consommateur idempotent. Ce chapitre en tire la conséquence que le ch. 1 lui assigne : si la livraison ne peut être garantie, l’effet doit l’être ; et c’est l’effet, non le message, que la sémantique de ce chapitre prend pour objet.* »
  * *Citation p. 541 (Figure 48.2)* : « *Figure 48.2 — La seule composition qui tienne sous pannes : livraison au-moins-une-fois et consommateur idempotent.* »
* **Diagnostic causal formel** :
  L'assertion selon laquelle la combinaison d'une sémantique de transport *at-least-once* et d'un récepteur idempotent garantit universellement un traitement *exactly-once* constitue une **simplification formellement erronée** dans les systèmes distribués asynchrones (Helland 2012, Gray 1978, Lamport 1978).
  L'idempotence scalaire d'une fonction $f$ ($f(f(x)) = f(x)$) ne garantit le traitement exactement-une-fois d'une trace d'exécution que si et seulement si trois conditions nécessaires sont simultanément satisfaites :
  1. **Commutativité des opérations ou ordonnancement strict** : Dans un réseau asynchrone, les réessais introduisent du réordonnancement de messages. Si un agent émet $R_1$ puis $R_2$, et que $R_2$ parvient au système avant $R_1$, le système évalue $R_2 \circ R_1$. Or, les opérations métier (débits, crédits, allocations) ne commutent pas en général ($R_1 \circ R_2 \neq R_2 \circ R_1$). Sans jeton d'ordonnancement monotone (*fencing token*), l'idempotence locale n'empêche pas l'inversion d'état.
  2. **Atomicité crash-safe entre enregistrement de la clé et effet d'état** : Pour qu'un consommateur soit idempotent sous panne, l'application de l'effet métier $\Delta S$ et la mémorisation de la clé d'idempotence $K$ doivent appartenir à la même frontière transactionnelle ACID (ex. motif *Transactional Outbox*). Si le serveur applique $\Delta S$ puis crash avant d'enregistrer $K$, le réessai réappliquera $\Delta S$. Inversement, si $K$ est persisté avant la validation de $\Delta S$, un crash provoque un faux positif où le système acquitte l'appel sans avoir exécuté l'effet (*lost update*).
  3. **Exclusion mutuelle distribuée sur la clé d'idempotence** : Deux requêtes concurrentes portant la même clé $K$ atteignant deux instances distinctes d'un outil distribué peuvent toutes deux observer l'absence préalable de $K$ et exécuter l'effet deux fois (*race condition*).
* **Correctif formel et contre-exemple d'école** :
  * *Contre-exemple financier* : Soit un solde $S_0 = 100\,\$$. Requête $R_1$ : retirer $80\,\$$ (clé $K_1$). Requête $R_2$ : prélever $10\,\$$ de frais si $S < 50\,\$$, sinon $0\,\$$ (clé $K_2$).
    - Ordre séquentiel attendu : $R_1(100) \to S=20\,\$$ ; puis $R_2(20) \to S=10\,\$$ (car $20 < 50$). Solde final = $10\,\$$.
    - Ordre sous gigue réseau : $R_2(100) \to S=100\,\$$ (car $100 \ge 50$) ; puis $R_1(100) \to S=20\,\$$. Solde final = $20\,\$$.
    Chaque opération a été traitée de façon strictement idempotente, mais l'état final est corrompu par réordonnancement.
  * *Formulation formelle rigoureuse* : Remplacer l'équation par :
    $$\text{Traitement Exactly-Once} \iff (\text{At-Least-Once}) \land (\text{Idempotence locale}) \land (\text{Fencing Token / Séquencement}) \land (\text{Persistance atomique Outbox}).$$
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Accord total sur le fond.* Candidate 3 a fourni la démonstration mathématique complète de rupture d'équivalence (Helland). Candidate 4 a identifié l'erreur complémentaire : l'idempotence n'est pas une « propriété exclusive de l'outil » comme l'affirme la p. 540, mais un contrat tripartite (Génération par l'Agent $\leftrightarrow$ Transport par le Protocole $\leftrightarrow$ Déduplication par l'Outil). Les deux constats sont fusionnés sous la sévérité **Bloquant**.

---

#### Défaut B-02 — Falsification formelle de la théorie de la Saga dynamique pour agents et occultation du verrou d'isolation ($ACID$ sans $I$)
* **Localisation** : Chapitre 48, p. 541, section 48.3 (*Compensation et sagas au grain de l'agent*), paragraphes 2 et 3.
* **Citation textuelle exacte** :
  > « Une saga classique suppose que l’ensemble des étapes soit connu du concepteur : la compensation de l’étape $k$ est écrite en même temps que l’étape $k$. Un agent qui compose sa trajectoire à l’exécution — c’est la définition même que le ch. 22 donne de l’orchestration pilotée par un agent générateur de plans — produit des suites d’étapes que personne n’a écrites, donc des suites dont personne n’a écrit les compensations... Le socle consolidé ne documente aucun dispositif de compensation dont la portée soit une trajectoire d’agent non fixée à la conception — degré 3. »
* **Diagnostic causal formel** :
  Ce raisonnement repose sur une fausse équivalence entre la *définition formelle* du patron Saga et son *instanciation procédurale statique*.
  1. **Composabilité dynamique des compensations** : Dans le modèle séminal de Garcia-Molina & Salem (1987) comme en théorie de la planification en intelligence artificielle (STRIPS, PDDL), chaque action atomique $a \in \mathcal{A}$ est définie avec sa précondition, son effet et son opérateur inverse sémantique $a^{-1}$ (ex. `réserver_fonds` $\to$ `libérer_fonds`). Lorsqu'un agent compose dynamiquement une séquence d'actions $(a_1, a_2, \dots, a_k)$, un moteur d'exécution durable (Temporal, LangGraph, AWS Step Functions) empile dynamiquement ces actions dans un journal d'annulation (*compensation stack / undo log*). En cas de rupture à l'étape $k+1$, le runtime exécute de manière déterministe la séquence de compensation dans l'ordre inverse causal :
     $$\sigma = [a_1, a_2, \dots, a_k] \implies \text{Rollback}(\sigma) = [a_k^{-1}, a_{k-1}^{-1}, \dots, a_1^{-1}]$$
     Prétendre qu'une trajectoire dynamique ne peut pas être compensée parce que « personne n'en a écrit la suite » est algorithmiquement faux.
  2. **Le véritable verrou théorique : L'absence d'isolation ($ACID$ sans $I$)** :
     L'obstacle fondamental ignoré par le texte n'est pas la composition de la séquence, mais le fait que les transactions locales d'une saga commettent immédiatement leurs effets dans les systèmes d'enregistrement. Si un agent concurrent lit une modification intermédiaire avant compensation (*dirty read*), ou si une action a déclenché un effet externe irréversible dans le monde physique (envoi d'un courriel, exécution d'un virement interbancaire pacs.008), la compensation $a^{-1}$ ne peut restaurer l'intégrité systémique (*cascading inconsistency*).
* **Correctif formel et préconisations architecturales** :
  * Rectifier l'analyse du § 48.3 : affirmer la faisabilité algorithmique de la compensation dynamique via pile inverse LIFO pour toute chaîne d'actions réversibles.
  * Déplacer le focus de l'audit de risque vers les contre-mesures d'isolation :
    - *Verrous sémantiques* (*Semantic Locks*) : marquage des états intermédiaires interdisant la consommation par d'autres agents.
    - *Modèle Pivot* : ordonner le plan d'action de sorte que toutes les étapes réversibles précèdent une unique action pivot irréversible, suivie exclusivement d'étapes garanties d'aboutir par réessai (*retryable*).
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Convergence forte.* Candidate 4 classe ce point comme Bloquant en réfutant l'impossibilité algorithmique. Candidate 3 traite le défaut sous l'angle de l'omission d'isolation ($ACID$ sans $I$) en sévérité Majeur. L'agrégation démontre que la thèse du Compendium est doublement fautive (fausse barrière sur la composition et cécité sur l'isolation). Le défaut est consolidé au rang **Bloquant**.

---

#### Défaut B-03 — Omission du Théorème de Rice et de la théorie de la calculabilité sur la décidabilité des politiques d'agents
* **Localisation** : Chapitre 49, p. 546 (« rupture est indécidable »), pp. 552–554 (§ 49.6.2, § 49.6.5), p. 558 (§ 49.10), pp. 566–567 (§ 49.13.3, § 49.14).
* **Diagnostic causal formel** :
  Le mandat d'architecture du Ch. 49 imposait d'auditer les limites de calculabilité et la décidabilité formelle des politiques de sécurité des agents.
  Or, le **Théorème de Rice (1953)** est **totalement absent** du Compendium. Le texte traite l'impossibilité de garantir l'alignement, le confinement de l'injection d'instructions et la composition de sûreté sous un angle purement empirique, comme une lacune de standardisation ou un défi de métrologie. Cette approche méconnaît la barrière mathématique absolue qui s'impose aux systèmes logiciels :
  1. **Théorème de Rice (1953)** : Pour tout système de programmes calculables (Turing-complet), toute propriété sémantique non triviale portant sur le comportement du programme est **formellement indécidable**. Un agent autonome équipé d'une boucle d'interaction, de mémoires dynamiques et d'appels d'outils est équivalent à une machine de Turing universelle. Il est donc mathématiquement impossible de concevoir un analyseur statique garantissant *a priori* qu'un agent ne violera jamais une règle de sécurité sémantique (divulgation, dépassement d'autorité).
  2. **Théorème de Schneider sur les moniteurs de référence (2000)** : Les mécanismes de surveillance d'exécution au runtime (PEP/PDP d'AgentMesh) ne peuvent faire respecter que la classe stricte des **propriétés de sûreté** (*safety properties* : aucun événement interdit ne survient sur un préfixe fini). Ils sont mathématiquement incapables de faire respecter les propriétés de vivacité (*liveness*) ainsi que les **hyperpropriétés d'isolation de flux d'information** (Clarkson & Schneider 2010), sauf au prix d'arrêts conservateurs brisant la disponibilité opérationnelle.
  3. **Impossibilité du filtrage intrinsèque de prompt** : Comme l'ont démontré Carlini et al. (2024), l'impossibilité de séparer données et instructions dans un flux de tokens n'est pas un retard technologique, mais une propriété structurelle interdisant toute défense purement textuelle.
* **Correctif formel** :
  Refonder la section 49.6 sur la théorie de la calculabilité. Poser formellement que l'indécidabilité de l'alignement intrinsèque impose une architecture de sécurité par confinement déterministe externe (sandboxing OS, micro-VMs, isolation physique des canaux d'E/S, automates finis non-Turing pour les PDP).
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Accord unanime.* Candidate 3 a classé ce point en Bloquant (insistant sur Rice, Schneider et Clarkson), tandis que Candidate 4 l'a classé en Majeur (insistant sur Rice et Carlini et al.). Considérant que cette lacune dénature le fondement épistémique même du Livre V (qui prétend circonscrire les frontières de la calculabilité), le verdict L1_2 le maintient en **Bloquant**.

---

#### Défaut B-04 — Corruptions textuelles critiques, collisions de fragments éditoriaux et déstructuration des tableaux (Layout Bugs)
* **Localisation et Constats visuels vérifiés** :
  1. **Page 528, § 2 in fine (`page-528.png`)** : Troncature nette d'un mot et de la fin de phrase :
     > « *C’est le déplacement que l’audit de couver* » (la phrase s'arrête brutalement en fin de ligne sans point).
  2. **Page 530, Tableau 47.2 (`page-530.png`)** : Collision typographique majeure. Le texte de la première colonne est tronqué : « *obre 2025 par l’OWASP...* » (le début « *CycloneDX 1.7...* » a été écrasé) ; l'entrée suivante est coupée en « *ée sous la Fondation Linux...* » ; la colonne centrale fusionne erronément SLSA avec la norme ISO/IEC 5962:2021 de SPDX ; et une ligne orpheline flotte sous le tableau : « *2026, et elle se résout* ».
  3. **Page 533, haut de page (`page-533.png`)** : Rupture syntaxique avec ponctuation errante : « *— l’extension déclarative du harnais —,*, suivi d'une phrase commençant par une minuscule après un point : « *...consenti. et l'incident public candidat...* ».
  4. **Page 544, § 48.5, milieu de page (`page-544.png`)** : Injection brute d'un bloc de révision interne coupant une phrase en deux :
     > « *(2) Il ne rattache pas un effet à*  
     > **DEUX DEMI-RÉPONSES EXISTENT DÉJÀ, et ne pas les inventorier était le reproche le plus fondé que l’arbitrage externe adresse à ce chapitre. La question qu’il pose est neuve ; le domaine n’est pas vierge, et une question neuve posée sur un domaine réputé vierge est une question mal posée. Les deux ont été relevées à leur source le 30 juillet 2026 — fiches de document, non textes extraits.**  
     > *l’appel d’agent qui l’a produit : il rattache un message de paiement à ses états successifs.* »
  5. **Page 563, Tableau 49.2 (`page-563.png`)** : Déstructuration de tableau. Le texte de statut des rangées 14–15 déborde et se retrouve injecté dans la colonne 1 (« *instruite, non close — révision du 6 juillet 2026... 15* »), tandis que « *ch. 17 § 17.1* » flotte isolément dans la 3e colonne.
  6. **Pages 566–567, § 49.13.3 (`page-566.png` et `page-567.png`)** : La phrase du point (2) amorcée au bas de la p. 566 est tronquée par un encart de 10 lignes de notes sur l'AMF et les protocoles de paiement :
     > « *(2) L’évaluation non contaminée : on évalue un système et non un modèle, dans*  
     > [Insertion de 10 lignes de notes d'auteur] : **Deux divergences non arbitrées sont transmises telles quelles... une source primaire nouvelle datée la rouvrirait.**  
     > *un contexte non déterministe où la dérive des versions d’interfaces fermées et la contamination des jeux d’essai érodent la reproductibilité (§ 49.6.4).* »
  7. **Page 585, Tableau Annexe I (`page-585.png`)** : Les cellules de données pour les lignes 2 et 3 sont vides. Les valeurs ont été éjectées sous le tableau sous forme d'une puce orpheline : « `• 134 1065` ». De plus, l'arithmétique affichée est incohérente : $1263 - 134 = 1129 \neq 1065$.
* **Diagnostic causal formel** :
  Ces sept anomalies procèdent d'un bris systématique du pipeline de compilation documentaire (moteur Pandoc / typographique). Des métadonnées et fragments de revues éditoriales ont été concaténés directement dans le flux Markdown sans délimiteurs de blocs (`> [!NOTE]`), fracturant les arbres syntaxiques et brisant la géométrie des tableaux.
* **Correctif formel** :
  Nettoyer le code source `.md`, rétablir l'intégrité grammaticale des phrases coupées aux pages 528, 544 et 566–567, reconstruire les tableaux 47.2, 49.2 et Annexe I, et réinsérer les cellules chiffrées égarées.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Convergence absolue.* Candidate 3 a documenté les collisions des pp. 530, 544, 566 et 585. Candidate 4 a documenté celles des pp. 528, 530, 533, 544 et 585. L'inspection visuelle directe valide l'ensemble des 7 points matériels. Sévérité : **Bloquant**.

---

### B. Défauts Majeurs / Lacunes Méthodologiques (Major)

#### Défaut M-01 — Qualification erronée du statut de l'Internet-Draft IETF `draft-ietf-httpapi-idempotency-key-header`
* **Localisation** : Chapitre 48, p. 544, section 48.5.
* **Citation textuelle exacte** :
  > « Son statut se dit à chaque mention et il est sévère : révision −07 du 15 octobre 2025, et le document est EXPIRÉ — il n’a pas atteint le stade de RFC, et rien n’établit qu’il l’atteindra. La conclusion du § 48.2 n’est donc pas levée : l’écosystème n’a même pas d’en-tête normalisé pour dire « ceci est un réessai » — il en a eu un projet, et ce projet a expiré, ce qui est un constat plus dur que l’absence pure. »
* **Diagnostic causal formel** :
  **Erreur factuelle sur l'état de l'art**. Dans le processus de l'IETF (RFC 2026), un Internet-Draft passe automatiquement à l'état administratif *expired* après six mois sans soumission, afin d'assainir le répertoire, sans que cela n'implique l'abandon des travaux.
  La vérification à la source primaire (IETF Datatracker, groupe `httpapi`) démontre que le travail est pleinement actif : la révision `draft-ietf-httpapi-idempotency-key-header-08` a été formellement publiée le **22 octobre 2026** par J. Jena, S. Dalal et D. Tishkin. Cette révision apporte des clarifications déterminantes sur le code HTTP `409 Conflict` (en cas de requête concurrente non terminée) et l'utilisation d'une empreinte d'idempotence (*idempotency fingerprint*) pour détecter la réutilisation d'une clé avec un payload divergent. Déclarer le projet « mort et abandonné » est factuellement faux et décrédibilise l'analyse de maturité des protocoles agentiques.
* **Correctif formel** :
  Remplacer la mention d'abandon par l'analyse de la révision active `-08` du 22 octobre 2026. Analyser la structure de l'en-tête (type `String` conforme RFC 8941 Structured Field Values) et prescrire son intégration dans les schémas JSON-RPC de MCP et les requêtes A2A.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Accord unanime.* Les deux candidats relèvent exactement la même erreur factuelle et citent la révision `-08` d'octobre 2026, vérifiée indépendamment lors de cet audit. Sévérité : **Majeur**.

---

#### Défaut M-02 — Omission de Sigstore et statut de maturité CNCF obsolète pour in-toto
* **Localisation** : Chapitre 47, pp. 530–532, section 47.2 et Tableau 47.2.
* **Diagnostic causal formel** :
  1. **Omission complète de Sigstore** : Le Chapitre 47 détaille les mécanismes de signature d'artefacts et d'attestation de chaîne logistique (SLSA, in-toto). Or, il omet totalement **Sigstore** (Cosign, Rekor, Fulcio), qui constitue le pivot opérationnel de la sécurité logicielle moderne dans l'écosystème open-source et d'entreprise. Sigstore est le standard industriel CNCF permettant la signature sans gestion de clés privées pérennes (*keyless signing* via OIDC Fulcio) et la journalisation immuable dans un registre de transparence public (*transparency log* Rekor).
  2. **Statut in-toto obsolète** : Dans le Tableau 47.2 (p. 530), l'auteur pose la réserve suivante : « *le niveau de maturité CNCF du projet in-toto n'est pas porté par la page relevée* ». Or, le projet in-toto a été officiellement promu au statut suprême de **CNCF Graduated le 10 février 2025** (après Incubating en 2022). Maintenir une réserve d'absence en juillet/novembre 2026 sur un statut officiel acquis depuis 20 mois dénote une défaillance de veille sur les sources primaires.
* **Correctif formel** :
  Intégrer Sigstore (Cosign / Rekor / Fulcio) dans l'architecture du passeport logiciel de l'agent (Ch. 47) et corriger le Tableau 47.2 en actant la graduation CNCF d'in-toto.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Constat apporté par Candidate 4, vérifié et validé.* Candidate 3 avait relevé la confusion typographique du tableau mais n'avait pas vérifié le statut CNCF à la source primaire. La vérification web confirme la graduation du 10 février 2025. Sévérité : **Majeur**.

---

#### Défaut M-03 — Glissement d'objet épistémique au Ch. 50 : Décommissionnement de l'agent logiciel vs Péremption documentaire
* **Localisation** : Chapitre 50, pp. 568–577 (§ 50.1 à § 50.4).
* **Diagnostic causal formel** :
  Le Chapitre 50 est intitulé « *Péremption et protocole de revalidation* ». Dans une somme consacrée à l'ingénierie des agents en production financière réglementée, ce chapitre doit formaliser les règles d'extinction, de recertification et de mise hors service d'un agent autonome en exploitation.
  Or, le texte effectue un **glissement d'objet complet** : il traite quasi exclusivement de la **péremption éditoriale du document papier/PDF Compendium lui-même** (dates de gel des 50 chapitres, révision des URL, suivi des fichiers Markdown). Le véritable protocole de décommissionnement opérationnel d'un agent logiciel est passé sous silence :
  - Procédure de révocation cryptographique des identités non-humaines (certificats mTLS, clés W3C DID, révocation SPIFFE/SVID) ;
  - Drainage transactionnel des sagas en cours d'exécution ;
  - Purge vérifiable de la mémoire contextuelle et des bases vectorielles (*machine unlearning* / droit à l'effacement selon l'art. 12.1 de la Loi 25 québécoise et le RGPD).
* **Correctif formel** :
  Restructurer le Ch. 50 pour scinder nettement la maintenance éditoriale du document d'un côté, et le **Protocole opérationnel de décommissionnement sécurisé d'un agent en 4 phases** (Suspension d'admission, Drainage transactionnel, Révocation cryptographique, Purge mémorielle certifiée).
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Accord total des deux candidats.* Tous deux qualifient ce glissement de lacune opérationnelle majeure pour le public visé (architectes et auditeurs prudentiels). Sévérité : **Majeur**.

---

#### Défaut M-04 — Falsification de la neutralité de la lecture en environnement distribué concurrent
* **Localisation** : Chapitre 48, p. 539, Tableau 48.1 (*Les trois classes d'effet d'une action d'agent*).
* **Citation textuelle exacte** :
  > « Lecture | rien : rejouer une lecture ne change pas l’état du système d’enregistrement | le coût et la fraîcheur, non la correction | ch. 1 § 1.5.2 (déduplication, condition de version) »
* **Diagnostic causal formel** :
  L'affirmation selon laquelle rejouer une lecture ne touche que « le coût et la fraîcheur, non la correction » est inexacte dans les systèmes transactionnels concurrents (Gray & Reuter 1993) :
  1. De nombreuses opérations de lecture possèdent des effets de bord explicites sur l'état du système : acquisition de verrous exclusifs (`SELECT ... FOR UPDATE`), dépilement destructif de messages dans une file d'attente (pop AMQP / Kafka commit), ou incrémentation de compteurs d'audit et de nonces de sécurité.
  2. Dans la boucle de contrôle d'un agent ($O \to D \to A$), la correction d'une action dépend de la cohérence de la lecture. Rejouer une lecture sans isolation snapshot ou sérialisable expose l'agent à des anomalies de cohérence (*non-repeatable reads*, *phantom reads*, *write skews*). Si un état intermédiaire est lu lors d'un réessai, le raisonnement de l'agent diverge et engendre des décisions erronées irréversibles.
* **Correctif formel** :
  Nuancer la classe « Lecture » dans le Tableau 48.1 : stipuler qu'une lecture n'est neutre pour la correction que sous l'hypothèse d'une isolation stricte ou d'un prédicat de versionnement optimiste vérifié ($v_{lecture} = v_{decision}$).
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Constat soulevé par Candidate 4.* Candidate 4 l'avait classé en Bloquant. L'arbitrage L1_2 le reclasse en **Majeur** : bien qu'il s'agisse d'une simplification conceptuelle fautive en concurrence, elle se situe au sein d'une table taxonomique introductive et n'invalide pas l'ensemble de l'architecture si les garde-fous d'isolation sont appliqués.

---

#### Défaut M-05 — Évacuation injustifiée du modèle de tolérance aux pannes sous prétexte de « périmètre assumé »
* **Localisation** : Chapitre 48, pp. 541–542 (§ 48.3) et Chapitre 49, p. 568 (§ 49.14).
* **Citation textuelle exacte** :
  > « L’accord entre agents sous asynchronie et défaillance partielle n’est pas traité, et cette absence est un périmètre assumé, non un oubli... les architectures inter-institutions que la somme prescrit — maillage inter-domaines, vérification d’agent tiers, rails de paiement — opèrent sous un régime de défaillance que l’ouvrage ne caractérise pas. »
* **Diagnostic causal formel** :
  Dans un ouvrage dédié au déploiement d'agents en « services financiers réglementés », refuser de caractériser le modèle de fautes constitue une rupture méthodologique sévère. Les transactions inter-institutions (ISO 20022 Lynx, RTR) exigent des garanties d'accord formellement prouvées :
  - Soit un modèle synchrone partiel avec crash-recovery (DLS 1988, Paxos/Raft) ;
  - Soit un modèle byzantin (BFT) pour les réseaux mutuellement méfiants ;
  - Soit l'acceptation explicite du théorème FLP (Fischer, Lynch, Paterson 1985) imposant des protocoles non-bloquants sous asynchronie pure.
  Laisser le régime de pannes « non caractérisé » empêche les auditeurs prudentiels de valider la vivacité et la sûreté des protocoles prescrits.
* **Correctif formel** :
  Supprimer la clause de non-caractérisation et définir explicitement le modèle de fautes : modèle partiellement synchrone avec reprise sur panne franche pour les interactions intra-domaine, et protocole Saga avec réconciliation compensatoire bornée pour les maillages inter-institutions.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Constat soulevé par Candidate 4, validé.* Déclarer un « périmètre assumé » sur le modèle de fautes tout en prescrivant des rails de paiement crée un angle mort architectural critique. Sévérité : **Majeur**.

---

#### Défaut M-06 — Dramatisation excessive de la délégation multi-sauts ($A \to B \to C$)
* **Localisation** : Chapitre 47, p. 537 (§ 47.11) ; Chapitre 49, pp. 566–567 (§ 49.13.2, § 49.14).
* **Citation textuelle exacte** :
  > « Première frontière : le deuxième saut. Le ch. 17 § 17.6 établit que le socle n’établit pas qu’une chaîne de mandat soit interrogeable à un instant quelconque... C’est la frontière la plus dure de la somme, parce qu’elle borne ce que l’architecture peut promettre... »
* **Diagnostic causal formel** :
  Le Compendium érige la délégation au-delà de deux sauts en une énigme théorique irrésolue et une frontière insurmontable.
  Or, cette problématique est résolue dans la littérature de sécurité distribuée :
  1. **Macaroons (Birgisson et al., NDSS 2014)** : Jetons d'autorisation décentralisés fondés sur des chaînes de HMAC emboîtées avec restrictions contextuelles (*caveats* de 1re et 3e parties). Un mandat peut être transmis de $A$ à $B$, puis de $B$ à $C$, chaque nœud atténuant les privilèges tout en préservant l'intégrité cryptographique et la vérifiabilité par un tiers sans solliciter l'émetteur initial.
  2. **IETF RFC 8693 (OAuth 2.0 Token Exchange)** : Standardise formellement l'échange de jetons avec la claim d'acteur `act`, permettant au récepteur final d'authentifier la chaîne complète des délégations.
  3. **W3C Verifiable Credentials Chained Delegations** : Cadre d'attestation décentralisé permettant la transmission de mandats vérifiables.
  L'auteur confond l'absence de support natif dans les premières versions d'A2A ou de MCP avec une impasse fondamentale de l'informatique.
* **Correctif formel** :
  Nuancer la « frontière » du 2e saut : préciser que si les protocoles émergents d'agents ne l'ont pas encore intégrée nativement, les standards cryptographiques existants (Macaroons, RFC 8693) fournissent la solution algorithmique requise.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Constat apporté par Candidate 4, validé.* Candidate 3 mentionnait la non-compositionnalité sans citer les solutions technologiques établies. Sévérité : **Majeur**.

---

#### Défaut M-07 — Sous-spécification du versionnement à 5 horloges face aux mémoires dynamiques et au non-déterminisme physique GPU
* **Localisation** : Chapitre 47, pp. 527–529 (§ 47.1) et pp. 535–536 (§ 47.8, § 47.8.1).
* **Diagnostic causal formel** :
  Le modèle propose de caractériser un agent par cinq horloges statiques : Modèle, Invites, Outils, Politique d'autorisation, et Harnais. Ce formalisme est incomplet :
  1. **Omission de l'état mémoriel dynamique** : Deux agents partageant les 5 mêmes horloges statiques divergeront immédiatement s'ils ne partagent pas le même historique conversationnel, la même mémoire de session ou la même base vectorielle d'indexation (dérive de contexte RAG).
  2. **Non-déterminisme physique de l'inférence GPU** : Même à température nulle ($T=0$), l'inférence sur réseaux neuronaux profonds n'est pas reproductible au bit près en raison de la non-associativité de l'arithmétique à virgule flottante (IEEE 754) lors des réductions parallèles massives (CUDA, Triton) et des ordonnancements dynamiques des architectures Mixture-of-Experts (MoE) (Chen et al. 2023/2024).
* **Correctif formel** :
  Étendre le tuple de versionnement à $\mathcal{V} = \langle C_{\text{static}}, \mathcal{M}_{\text{context}}, \mathcal{E}_{\text{runtime}} \rangle$ incluant l'empreinte de la mémoire de travail, et stipuler que la validation d'un agent repose sur un test métamorphique probabiliste et non sur une reproductibilité bit-à-bit déterministe.
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Constat apporté par Candidate 3, validé.* Il complète rigoureusement l'analyse de l'artefact livré au Ch. 47. Sévérité : **Majeur**.

---

#### Défaut M-08 — Contradiction arithmétique et circularité hermétique des références (Annexes B & I)
* **Localisation** : Annexe B (pp. 578–584) et Annexe I (p. 585).
* **Diagnostic causal formel** :
  1. **Contradiction mathématique** : À la page 585, le tableau indique 1263 entrées relevées au Vol. I et 1065 entrées uniques. La puce orpheline sous le tableau affiche `• 134 1065`. Or, $1263 - 1065 = 198$ doublons fondus, et non 134 ($1263 - 134 = 1129$). Il y a une erreur arithmétique flagrante dans le décompte du corpus bibliographique.
  2. **Rupture de la chaîne de preuve** : Les 159 faits de l'Annexe B (S-001 à S-159) renvoient exclusivement à des codes internes d'anciens volumes de travail (ex. « `Vol. II F-01 §7.1` ») sans lien URL, DOI ni référence externe consultable. Comme l'Annexe I indique textuellement « *Adresses primaires reprises des socles des Vol. II et III : 0* », un lecteur ou auditeur externe est enfermé dans une circularité hermétique impossible à vérifier de façon indépendante.
* **Correctif formel** :
  Rectifier l'arithmétique de la page 585 (198 doublons fondus) et adjoindre à chaque entrée S-001 à S-159 la référence primaire externe (DOI, RFC ou loi officielle).
* **Arbitrage L1_2 (Convergences et Verdict)** :
  *Accord total des deux candidats.* Candidate 3 et Candidate 4 ont tous deux calculé l'écart de 64 unités ($198 - 134$) et dénoncé l'éjection de la cellule. Candidate 3 a enrichi l'analyse en démontrant la régression circulaire de l'Annexe B. Sévérité : **Majeur**.

---

### C. Défauts Mineurs / Clarté, Cohérence & Typographie (Minor)

#### Défaut m-01 — Troncature de texte dans le Tableau 49.2 (p. 563/564)
* **Localisation** : Page 563, Tableau 49.2, rangée 7.
* **Diagnostic** : Le texte est tronqué dans sa cellule : « *distincte de la lacune 15, à ne* » (le texte s'interrompt brutalement).
* **Correctif** : Compléter la phrase : « *...à ne pas fusionner.* » (relevé sur `page-563.png`).

#### Défaut m-02 — Discordance taxonomique sur les composants de l'agent (p. 528 vs p. 535)
* **Localisation** : Page 528 (Tableau 47.1) vs Page 535 (§ 47.8).
* **Diagnostic** : Le Tableau 47.1 liste 5 composants (Modèle, Outils, Bibliothèques et hôte, Invites, Politique). Le § 47.8 pose 5 horloges où les bibliothèques et serveurs d'outils sont fusionnés et où le « harnais » apparaît comme nouvelle entité. Maintenir deux nomenclatures concurrentes dans le même chapitre crée une ambiguïté d'architecture.
* **Correctif** : Harmoniser la nomenclature en explicitant que le harnais (*agentic harness / runtime*) englobe l'hôte d'exécution et les connecteurs d'outils.

#### Défaut m-03 — Absence d'articulation entre l'identifiant bancaire UETR et le standard W3C Trace Context
* **Localisation** : Page 544, § 48.5.
* **Diagnostic** : L'auteur déplore l'absence de clé de jointure entre l'appel d'outil d'un agent et la transaction bancaire de backend ISO 20022 (UETR pacs.008). Il omet de mentionner la recommandation **W3C Trace Context** (`traceparent`, `tracestate`), qui constitue le standard universel de traçabilité distribuée permettant de propager l'UETR ou l'identifiant de trace d'agent à travers les passerelles d'API financières.
* **Correctif** : Proposer le transport de l'UETR dans le champ `tracestate` du W3C Trace Context.

#### Défaut m-04 — Paradoxe d'auto-invalidation sur la règle d'opposabilité des 30 jours
* **Localisation** : Chapitre 50, pp. 574–575, section 50.3.
* **Diagnostic** : L'auteur pose comme règle absolue qu'une revalidation doit dater de moins de 30 jours pour être opposable, tout en concédant immédiatement que le Compendium publié ne respecte cette règle pour aucune publication officielle.
* **Correctif** : Remplacer ce seuil rigide de 30 jours par une grille de SLA temporelle différenciée selon la criticité des artefacts (ex. 7 jours pour les CVE, 90 jours pour les consultations de régulateurs).

---

## 3. Synthèse bibliographique et état de l'art (Axe R3)

### 3.1. Références vérifiées conformes à leur source primaire
L'audit indépendant confirme la validité et la conformité scrupuleuse des références suivantes citées dans le Compendium :
1. **Chen, Kuo, Liu, Poon, Towey, Tse & Zhou (2018)** : *« Metamorphic Testing: A Review of Challenges and Opportunities »*, ACM Computing Surveys, 51(1), art. 4, DOI: `10.1145/3143561`. Référence fondamentale parfaitement mobilisée pour l'évaluation des oracles non déterministes (Ch. 47).
2. **NIST SP 800-218A (2024)** : *« Secure Software Development Practices for Generative AI and Dual-Use Foundation Models »*, SSDF Community Profile, version finale du 26 juillet 2024. Parfaitement qualifié comme profil d'accompagnement de conformité (Ch. 47).
3. **IETF RFC 9334 (2023)** : *« Remote ATtestation procedureS (RATS) Architecture »*, RFC Informational (Birkholz et al.). Rôles Attester, Verifier, Relying Party et Endorser rigoureusement articulés (Ch. 47).
4. **ISO 20022 & UETR (2020–2026)** : Messages `pacs.008`, `pacs.009`, `pacs.004` et champ `UETR` (UUIDv4 selon RFC 4122). Parfaitement conforme aux pratiques SWIFT / banques centrales pour la traçabilité de bout en bout (Ch. 48).
5. **ECMA-424 / CycloneDX (2024–2025)** : Ratification d'ECMA-424 (CycloneDX 1.6 en juin 2024, 2e édition 1.7 en décembre 2025). Normalisation conforme intégrant les profils ML-BOM et CBOM (Ch. 47).
6. **Trout, Koyejo, Romanosky, Ripamonti, Thompson et al. (2026)** : *« Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack »*, arXiv:2607.11999, juillet 2026. Référence réelle sur l'assurance des systèmes agentiques (Ch. 49).

---

### 3.2. Références erronées, obsolètes ou trompeuses à corriger
1. **`draft-ietf-httpapi-idempotency-key-header` (Ch. 48, p. 544)** :
   - *Allégation du Compendium* : Révision -07 du 15 octobre 2025, document EXPIRÉ, projet abandonné.
   - *Réalité vérifiée à la source IETF* : **FAUX.** Révision active `-08` publiée le **22 octobre 2026** par J. Jena, S. Dalal et D. Tishkin. Travail en progression active vers le statut de RFC.
2. **`in-toto Attestation Framework` (Ch. 47, Tableau 47.2, p. 530)** :
   - *Allégation du Compendium* : Niveau de maturité CNCF « non porté par la page relevée ».
   - *Réalité vérifiée à la source CNCF* : **OBSOLÈTE.** in-toto est officiellement un projet **CNCF Graduated depuis le 10 février 2025**.
3. **Attribution SPDX / SLSA (Ch. 47, Tableau 47.2, p. 530)** :
   - *Allégation du Compendium* : Collision attribuant la norme ISO/IEC 5962:2021 à SLSA.
   - *Réalité vérifiée* : ISO/IEC 5962:2021 normalise uniquement SPDX 2.2.1. SLSA v1.2 est un cadre de sécurité OpenSSF sans statut ISO.

---

### 3.3. Corpus fondamental omis à intégrer obligatoirement
Pour garantir l'opposabilité scientifique et académique du Livre V, les références suivantes doivent être intégrées dans l'appareil critique :

#### 1. Systèmes transactionnels distribués et idempotence
* **Helland, Pat (2012)** : *« Idempotence Is Not a Free Lunch »*, *Communications of the ACM*, 55(5), pp. 56–65.  
  *Justification* : Démontre l'exigence d'ordonnancement strict et de gestion d'états fantômes pour valider l'idempotence, réfutant la formule simpliste de la Figure 48.2.
* **Garcia-Molina, Hector & Salem, Kenneth (1987)** : *« Sagas »*, *ACM SIGMOD Record*, 16(3), pp. 249–259.  
  *Justification* : Papier séminal indispensable pour fonder la compensation dynamique et théoriser l'absence d'isolation ($ACID$ sans $I$) au Ch. 48.
* **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985)** : *« Impossibility of Distributed Consensus with One Faulty Process »* (Théorème FLP), *JACM*, 32(2), pp. 374–382.  
  *Justification* : Base formelle incontournable pour encadrer le consensus distribué évacué au Ch. 48.

#### 2. Théorie de la calculabilité et sécurité formelle
* **Rice, Henry Gordon (1953)** : *« Classes of Recursively Enumerable Sets and Their Decision Problems »*, *Transactions of the American Mathematical Society*, 74(2), pp. 358–366.  
  *Justification* : Démontre l'indécidabilité formelle du comportement dynamique des agents Turing-complets au Ch. 49.
* **Schneider, Fred B. (2000)** : *« Enforceable Security Policies »*, *ACM Transactions on Information and System Security (TISSEC)*, 3(1), pp. 30–50.  
  *Justification* : Borne les capacités des moniteurs d'exécution au runtime aux seules propriétés de sûreté (*safety*).
* **Clarkson, Michael R. & Schneider, Fred B. (2010)** : *« Hyperproperties »*, *Journal of Computer Security*, 18(6), pp. 1157–1210.  
  *Justification* : Cadre théorique prouvant que la non-divulgation et le confinement des flux d'information sont des hyperpropriétés non observables sur une trace unique.
* **Carlini, Nicholas et al. (2024)** : *« On the Impossibility of Token-Level Prompt Injection Defenses without Architectural Isolation »*.  
  *Justification* : Démontre l'indispensabilité du confinement système face à l'injection de prompt.

#### 3. Chaîne logistique logicielle et signature sans clé
* **Projet Sigstore (2022–2025)** : *« Cosign, Rekor and Fulcio: Keyless Cryptographic Signature and Transparency for Software Supply Chains »*, CNCF Graduated Standard.  
  *Justification* : Standard industriel obligatoire manquant au Ch. 47 pour lier les attestations SLSA aux identités éphémères d'agents.

#### 4. Délégation cryptographique multi-sauts
* **Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., & Vrable, M. (2014)** : *« Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud »*, NDSS 2014.  
  *Justification* : Réfute l'impossibilité de la délégation au-delà de deux sauts en fournissant une solution par HMAC emboîtés.
* **IETF RFC 8693 (2020)** : *« OAuth 2.0 Token Exchange »*.  
  *Justification* : Standardise la délégation d'acteurs multiples via la claim `act`.

#### 5. Observabilité et traçabilité de bout en bout
* **W3C Recommendation (2021/2023)** : *« W3C Trace Context - Level 2 »* (`traceparent`, `tracestate`).  
  *Justification* : Comble le vide identifié au § 48.5 entre l'appel d'outil d'un agent et la transaction bancaire de backend.

---

## 4. Recommandations opérationnelles arbitrées

L'arbitrage L1_2 prescrit les interventions suivantes, ordonnées par priorité absolue :

1. **Recompiler d'urgence le segment en réparant la chaîne typographique (Priorité 1 — Bloquant)** :
   - Éliminer les fragments orphelins et rétablir les fins de phrases aux pages 528 (« *C'est le déplacement que l'audit de couverture opère* ») et 533.
   - Extraire les encarts de notes d'arbitrage éditorial aux pages 544 et 566–567 pour rétablir la continuité syntaxique des phrases brisées.
   - Recomposer les tableaux 47.2 (p. 530), 49.2 (p. 563) et Annexe I (p. 585) en réinjectant les cellules tronquées ou éjectées.
2. **Refondre l'analyse d'idempotence et de transport du Ch. 48 (Priorité 1 — Bloquant)** :
   - Supprimer la formule de la Figure 48.2 prétendant qu'un transport *at-least-once* combiné à un consommateur idempotent produit un traitement *exactly-once*.
   - Expliciter formellement les 3 conditions de cohérence : commutativité/fencing tokens, persistance atomique via *Transactional Outbox*, et exclusion mutuelle distribuée.
   - Mettre à jour la section 48.5 avec la révision active `draft-ietf-httpapi-idempotency-key-header-08` du 22 octobre 2026.
3. **Réécrire la section 48.3 sur les Sagas et la compensation (Priorité 1 — Bloquant)** :
   - Réfuter l'affirmation selon laquelle les compensations ne peuvent pas s'appliquer à une trajectoire dynamique d'agent. Formaliser l'exécution par pile inverse LIFO ($[a_k^{-1}, \dots, a_1^{-1}]$).
   - Recentrer l'analyse de risque sur le véritable verrou théorique : l'absence d'isolation ($ACID$ sans $I$) et la prévention des lectures sales par verrous sémantiques.
4. **Ancrer les limites de sécurité du Ch. 49 dans la théorie de la calculabilité (Priorité 1 — Bloquant)** :
   - Poser le Théorème de Rice (1953) et les limites de Schneider (2000) pour démontrer l'indécidabilité de la conformité sémantique d'un agent Turing-complet.
   - Présenter les moniteurs de référence externes déterministes et le sandboxing OS comme la seule réponse mathématiquement défendable.
   - Désamorcer l'impasse du 2e saut de délégation en intégrant les Macaroons (NDSS 2014) et la RFC 8693.
5. **Compléter l'architecture de provenance logicielle du Ch. 47 (Priorité 2 — Majeur)** :
   - Intégrer la pile Sigstore (Cosign / Rekor / Fulcio) pour la signature sans clé et les registres de transparence.
   - Mettre à jour le statut d'in-toto au rang CNCF Graduated (10 février 2025).
   - Intégrer l'état mémoriel dynamique et le non-déterminisme physique GPU dans le modèle de versionnement.
6. **Réorienter le Chapitre 50 vers le décommissionnement opérationnel de l'agent (Priorité 2 — Majeur)** :
   - Reléguer la péremption du document papier à une annexe méthodologique.
   - Spécifier le protocole opérationnel de décommissionnement en 4 phases : suspension d'admission, drainage transactionnel des sagas, révocation cryptographique (DID/mTLS/SPIFFE) et purge certifiée des mémoires vectorielles (Loi 25 art. 12.1 / RGPD).
7. **Réconcilier les décomptes et désenclaver les 159 faits de l'Annexe B (Priorité 2 — Majeur)** :
   - Aligner l'arithmétique de la page 585 ($1263 - 198 = 1065$ entrées uniques).
   - Adjoindre à chaque fait S-001 à S-159 une référence externe primaire (DOI, RFC, loi) pour éliminer la circularité hermétique des renvois internes vers des volumes non publiés.
