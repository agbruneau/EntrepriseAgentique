# Rapport d'Audit Critique — Livre V : Clôture (Chapitres 47 à 50 & Transition Annexes B et I)
**Document audité** : `documents/Compendium.pdf` (pages 527 à 585)  
**Segment** : `segment_livre_5_cloture` (Segments S49 à S53 de REVIEW_PLAN.md)  
**Rôle** : Analyste L0_1 (Groupe Livre 5 Clôture)  
**Date d'audit** : 3 novembre 2026  
**Fichier cible** : `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_5_cloture\candidate_1.md`  
**Axes d'évaluation** : R2 Rigueur formelle & algorithmique · R3 Audit bibliographique & état de l'art  

---

## 1. Synthèse exécutive du segment

Le Livre V (« Livrer et clore », chapitres 47 à 50, pages 527 à 585) constitue l'aboutissement architectural du *Compendium*. Il opère un déplacement conceptuel majeur : après avoir traité l'agent comme un interlocuteur communicant (Livre I) puis comme une entité délégataire sous autorité (Livres II et III), il aborde l'agent sous l'angle de **l'artefact logiciel livré, exécuté sous contraintes transactionnelles distribuées et projeté dans le temps**. 

Ce segment s'articule autour de quatre volets critiques :
1. **L'artefact livré et la provenance des composants (Ch. 47, pp. 527-537)** : la décomposition en composants (modèle, outils, invites, politiques, harnais d'exécution), les nomenclatures SBOM/AIBOM (CycloneDX 1.7 / ECMA-424, SPDX 3.0), les cadres d'attestation (in-toto, SLSA v1.2) et les tests métamorphiques pour artefacts non déterministes.
2. **La sémantique d'effet (Ch. 48, pp. 538-544)** : la formalisation transactionnelle des outils d'agents, les garanties d'idempotence (clés d'idempotence, sémantique *at-least-once* vs *effectively-once*), le patron Saga appliqué aux trajectoires dynamiques, et la réconciliation des flux de valeur financiers (ISO 20022 / UETR).
3. **L'horizon prospectif 2027-2032 et la frontière de la connaissance vérifiable (Ch. 49, pp. 545-568)** : la classification épistémique des projections (Programmé, Projeté, Spéculatif), les limites formelles de la composition comportementale et le registre exhaustif des lacunes résiduelles de la somme.
4. **La péremption et le protocole de revalidation (Ch. 50, pp. 568-577) ainsi que la transition vers les Annexes B et I (pp. 578-585)** : la grille des quatorze événements déclencheurs d'obsolescence et le cadre de citation consolidé.

### Appréciation globale et constats d'audit

Si le segment fait preuve d'une rigueur épistémique et métrologique interne remarquable — notamment par sa discipline d'étiquetage des sources (degrés 1 à 3, faits négatifs vérifiés vs absences de documentation) et son refus des extrapolations commerciales complaisantes —, **notre audit R2 (formel et algorithmique) et R3 (bibliographique et état de l'art) met en lumière des failles théoriques, des omissions architecturales et des erreurs factuelles substantielles** :

* **Rupture de consistance en systèmes distribués (Ch. 48)** : L'affirmation selon laquelle « la seule composition qui tienne sous pannes est livraison au-moins-une-fois et consommateur idempotent » (Fig. 48.2) constitue une simplification réductrice invalidée par la réplication de machines à états (SMR) et le consensus distribué. De surcroît, le chapitre évacue l'accord sous asynchronie et défaillance partielle (modèle FLP), créant une circularité vicieuse : l'idempotence distribuée requiert elle-même un consensus pour la tenue du registre de clés d'idempotence.
* **Effondrement des Sagas dynamiques et défaut d'isolation (Ch. 48)** : L'application du patron Saga à des agents composant leur plan à l'exécution omet les contraintes d'ordonnancement de la transaction pivot (point de non-retour) et le problème critique des anomalies d'isolation inter-sagas (*dirty reads*, mises à jour perdues) en finance de marché.
* **Erreur factuelle sur la normalisation de l'idempotence IETF (Ch. 48)** : Le document affirme que la spécification `draft-ietf-httpapi-idempotency-key-header` est « expirée » et abandonnée depuis octobre 2025 (p. 544). En réalité, la révision `-08` a été soumise le **22 octobre 2026**, démontrant la vitalité continue du groupe HTTPAPI vers le standard RFC.
* **Absence d'ancrage dans la théorie de la calculabilité (Ch. 49)** : L'impossibilité de garantir formellement la conformité et l'alignement des agents est attribuée à tort à leur caractère probabiliste, occultant l'obstacle premier : le **Théorème de Rice (1953)** et l'indécidabilité de l'arrêt (Turing 1936), qui frappent toute vérification statique d'un agent Turing-complet. De plus, un mystérieux « théorème d'impossibilité de gouvernance à 4 propriétés » est invoqué sans démonstration ni référence académique.
* **Dérive d'objet et vide opérationnel de décommissionnement (Ch. 50)** : Le chapitre confond la maintenance éditoriale du document lui-même avec le protocole d'ingénierie logicielle régissant la fin de vie des agents en production (drainage asynchrone, révocation cryptographique des clés, purge mémorielle selon la Loi 25 québécoise et le RGPD, recertification périodique BSIF E-23).
* **Anomalie arithmétique dans l'appareil critique (Annexe I, p. 585)** : Le décompte bibliographique affiche une contradiction mathématique immédiate : $1263\text{ entrées brutes} - 134\text{ doublons fondus} = 1129 \neq 1065\text{ entrées uniques}$, soit un écart inexpliqué de 64 références.

---

## 2. Matrice détaillée des défauts classés par sévérité

### 2.1 Défauts Bloquants (Erreurs formelles, algorithmiques et théoriques — R2)

---

#### DÉFAUT B-01 : Réduction erronée de la résilience distribuée et circularité logique de l'idempotence sous pannes partielles
* **Localisation** : Chapitre 48, Section 48.2, page 540-541 & Figure 48.2 (p. 541).
* **Citations textuelles** :
  > « Figure 48.2 — La seule composition qui tienne sous pannes : livraison au-moins-une-fois et consommateur idempotent. » (p. 541)  
  > « Lecture de l’auteur — la conséquence est dissymétrique et elle est le cœur de la section : l’idempotence est une propriété de l’outil invoqué, pas du protocole qui l’invoque, ni de l’agent qui décide de l’invoquer. » (p. 540)  
  > « (2) L’accord entre agents sous asynchronie et défaillance partielle n’est pas traité, et cette absence est un périmètre assumé, non un oubli. [...] les architectures inter-institutions que la somme prescrit opèrent sous un régime de défaillance que l’ouvrage ne caractérise pas. » (p. 541-542)
* **Diagnostic causal approfondi** :
  1. *Non-unicité théorique* : En théorie des systèmes distribués, l'affirmation selon laquelle la livraison au-moins-une-fois (*at-least-once*) couplée à un consommateur idempotent est « la seule composition qui tienne sous pannes » est fausse. La réplication par machine à états finis déterministe (*State Machine Replication* - SMR, Lamport 1978, Schneider 1990) adossée à un consensus distribué tolérant aux pannes (Paxos, Raft) permet d'assurer une exécution unique stricte (*effectively-once* ou *exactly-once processing*, comme formalisé dans les architectures de streaming transactionnel à deux phases 2PC et instantanés de Chandy-Lamport).
  2. *Contradiction protocolaire* : Déclarer que l'idempotence est « une propriété de l'outil invoqué, pas du protocole qui l'invoque » méconnaît la sémantique même des opérations avec effets de bord. Pour qu'une action non naturellement idempotente (ex. `debit_account`) devienne idempotente, le serveur doit s'appuyer sur un contrat protocolaire bilatéral transportant une **clé d'idempotence** générée par l'agent client. Sans cette transmission protocolaire standardisée et intègre, le serveur est incapable de distinguer une réémission d'une seconde transaction légitime identique.
  3. *Circularité fatale* : Pour qu'un outil garantisse l'idempotence dans un environnement d'entreprise hautement disponible (multi-instances), l'enregistrement de la clé d'idempotence doit être répliqué avec consistance forte. Si le réseau est asynchrone et sujet à des partitions, garantir que la clé n'est pas acquise concurremment par deux nœuds requiert de résoudre le consensus distribué (soumis aux bornes de Fischer-Lynch-Paterson 1985). En décrétant que l'accord sous asynchronie n'est pas traité, l'auteur postule une idempotence locale « magique » qui s'effondre dès lors que le serveur d'outils est lui-même distribué.
* **Correctif formel & Contre-exemple** :
  * *Contre-exemple* : Soit un cluster bancaire d'outils agentiques composé de deux nœuds réplicas $N_1$ et $N_2$. Un agent émet une requête de virement avec la clé $K$. À la suite d'un timeout de transport, l'agent réémet la même requête avec la même clé $K$. Si une partition réseau isole $N_1$ et $N_2$ (absence de consensus à quorum Paxos/Raft), $N_1$ et $N_2$ traitent chacun la requête en croyant être le premier à voir $K$, provoquant un double débit immédiat sur le compte du client malgré la prétention d'idempotence.
  * *Correctif formel* : Remplacer l'absolutisme de la Figure 48.2 par : « Découplage robuste sous pannes : livraison au-moins-une-fois adossée à une déduplication par registre d'idempotence répliqué par consensus (SMR) ». Modéliser formellement le protocole d'idempotence sous forme d'automate à états finis :
    $$\text{État}(K) \in \{\text{UNSEEN}, \text{IN\_PROGRESS}(t_{\text{start}}, \text{hash}(P)), \text{COMMITTED}(R), \text{FAILED}(E)\}$$

---

#### DÉFAUT B-02 : Inapplicabilité du patron Saga aux trajectoires dynamiques d'agents et absence d'isolation inter-sagas
* **Localisation** : Chapitre 48, Section 48.3, pages 541-542 & Figure 48.3 (p. 542).
* **Citations textuelles** :
  > « Une saga classique suppose que l’ensemble des étapes soit connu du concepteur : la compensation de l’étape k est écrite en même temps que l’étape k. Un agent qui compose sa trajectoire à l’exécution — c’est la définition même que le ch. 22 donne de l’orchestration pilotée par un agent générateur de plans — produit des suites d’étapes que personne n’a écrites, donc des suites dont personne n’a écrit les compensations. [...] Le socle consolidé ne documente aucun dispositif de compensation dont la portée soit une trajectoire d’agent non fixée à la conception — degré 3. » (p. 541)
  > « (1) La compensation n’est pas l’annulation. Elle annule sémantiquement — un remboursement compense un débit, il ne le supprime pas ; les deux écritures subsistent. » (p. 541)
* **Diagnostic causal approfondi** :
  1. *Violation de la structure fondamentale des Sagas (Garcia-Molina & Salem 1987)* : Dans une Saga $S = \{(T_1, C_1), \dots, (T_n, C_n)\}$, l'atomicité relaxée repose sur la distinction mathématique stricte entre trois catégories d'étapes :
     * Les étapes *compensables* ($T_1, \dots, T_{p-1}$).
     * La transaction *pivot* ($T_p$) : étape critique non compensable qui détermine le succès ou l'échec global (point de non-retour). **Une saga ne peut comporter qu'une seule étape pivot.**
     * Les étapes *réitérables* ($T_{p+1}, \dots, T_n$) : étapes postérieures au pivot qui doivent être déterministes, sans échec définitif et idempotentes.
     Or, si un agent LLM planifie dynamiquement ses actions à chaud sans modèle statique préalable, il est incapable de garantir qu'il n'ordonnancera pas deux étapes pivots irréversibles successives.
  2. *Anomalies graves d'isolation inter-agents* : Le patron Saga sacrifie l'isolation (propriété $I$ d'ACID). Les effets de chaque étape locale $T_i$ sont immédiatement visibles par les autres agents du système avant la clôture de la saga globale. En finance, si un agent $A_1$ exécute un débit temporaire sur une ligne de crédit, un agent concurrent $A_2$ lisant le solde disponible refusera une transaction commerciale légitime (*dirty read*). Si $A_1$ échoue ultérieurement à l'étape $T_{i+1}$ et compense via $C_i$, l'agent $A_2$ aura pris une décision financière erronée sur la base d'un état intermédiaire éphémère. Le chapitre ignore totalement les techniques indispensables de **verrouillage sémantique (*semantic locks*)** et de **transactions sous séquestre (*escrow transactions*)**.
* **Correctif formel & Contre-exemple** :
  * *Contre-exemple* : Un agent financier d'arbitrage planifie dynamiquement la séquence suivante : $T_1$ = verrouillage de collatéral interne (compensable par $C_1$), $T_2$ = virement irréversible temps réel RTR/Lynx vers un tiers (action pivot), $T_3$ = souscription de contrat dérivé externe sur une bourse tierce (action pivot 2). Si $T_3$ est rejeté par la bourse pour limite de risque dépassée, l'agent tente de compenser : mais $T_2$ a déjà réglé définitivement les fonds sans droit de rétrofacturation unilatéral. Le système se retrouve dans un état d'incohérence financière irréversible avec perte sèche d'actif.
  * *Correctif formel* : Énoncer le théorème d'admissibilité d'une trajectoire agentique :
    $$\forall \text{ trajectoire } (T_1, \dots, T_n), \quad \exists ! \, p \in \{1, \dots, n\} \text{ tel que } T_p \text{ est l'unique transaction pivot, et } \forall k > p, \, T_k \text{ est strictement réitérable et infaillible.}$$
    Imposer un protocole de réservation de ressources (*escrow pattern*) pour masquer les écritures intermédiaires aux agents tiers jusqu'à la validation complète de la saga.

---

#### DÉFAUT B-03 : Omission des limites de calculabilité (Rice, Turing) et invocation non rigoureuse d'un « pseudo-théorème » de gouvernance
* **Localisation** : Chapitre 49, Sections 49.6.2, 49.6.5 et 49.10, pages 552-553, 557-558.
* **Citations textuelles** :
  > « Les méthodes formelles classiques supposent des composants déterministes et des interfaces stables ; les chaînes d’agents violent les deux hypothèses. Le programme consiste donc à substituer des garanties probabilistes ou contractuelles aux garanties absolues. » (p. 552-553)  
  > « Le verrou est formel, et c’est un résultat d’impossibilité : le Vol. I relève un théorème selon lequel aucun cadre de gouvernance ne peut satisfaire simultanément quatre propriétés — attributabilité, borne de prévisibilité, non-vacuité et complétude — pour des collectifs humains-agents. Statut SPÉCULATIF mais argumenté... » (p. 557-558)
* **Diagnostic causal approfondi** :
  1. *Omission de la théorie de la calculabilité (Théorème de Rice)* : L'auteur affirme que la vérification formelle échoue à cause du caractère probabiliste des LLM et de l'instabilité des interfaces. C'est passer à côté de la barrière fondamentale : **le théorème de Rice (1953)** et **l'indécidabilité de l'arrêt (Turing 1936)**. Dès lors qu'un agent dispose d'outils et de boucles de raisonnement lui conférant l'équivalence d'une machine de Turing, **toute propriété sémantique non triviale de sa trajectoire d'exécution est formellement indécidable**. Même si les modèles d'IA étaient 100 % déterministes, il demeurerait rigoureusement impossible de vérifier statiquement si un agent respectera en toutes circonstances une politique de conformité financière complexe sans simuler son exécution jusqu'à l'arrêt.
  2. *Méconnaissance des limites des moniteurs de sécurité (Schneider 2000)* : En surveillance à l'exécution (*runtime enforcement*), Fred B. Schneider a démontré que les moniteurs de sécurité (automates d'exécution) ne peuvent appliquer que la classe des **propriétés de sûreté (*safety properties*)**, c'est-à-dire des propriétés où une violation est constatable sur un préfixe fini d'exécution (ex. interdiction d'accès à un outil). Les **propriétés de vivacité (*liveness properties*)** — telles que l'obligation de compenser à terme ou de finaliser un virement — sont fondamentalement inapplicables par simple troncature dynamique.
  3. *Invention d'un résultat d'impossibilité non démontré* : Le prétendu « théorème selon lequel aucun cadre de gouvernance ne peut satisfaire simultanément quatre propriétés — attributabilité, borne de prévisibilité, non-vacuité et complétude » ne repose sur aucun énoncé mathématique, aucune référence de littérature et aucune preuve. Invoquer un « théorème » sans formalisation axiomatique constitue une faute épistémique grave dans un ouvrage prétendant à la rigueur formelle.
* **Correctif formel & Références** :
  - Restructurer la section 49.6 en distinguant : (a) l'indécidabilité statique issue du Théorème de Rice pour les agents Turing-complets, (b) la frontière d'applicabilité dynamique de Schneider (2000) séparant les politiques de sûreté (applicables par passerelle PEP/PDP) et les politiques de vivacité (indécidables à l'exécution).
  - Rétrograder le « théorème de gouvernance » au rang de simple « conjecture d'arbitrage heuristique » ou en fournir la preuve complète dans une annexe mathématique formelle.

---

#### DÉFAUT B-04 : Dérive d'objet du Chapitre 50 et absence totale de protocole opérationnel de décommissionnement d'agents
* **Localisation** : Chapitre 50, Sections 50.1 à 50.4, pages 568-577 & Tableau 50.1 (pp. 570-573).
* **Citations textuelles** :
  > « 50 · Péremption et protocole de revalidation [...] Le principe : amender le socle d’abord, les chapitres ensuite — jamais l’inverse. Un fait qui évolue est d’abord constaté à sa source primaire et consigné dans un rapport de revalidation daté ; l’entrée du socle est amendée, avec son niveau de preuve ; les chapitres qui en dépendent sont alors repris et portent une nouvelle date de gel. » (p. 574)  
  > « Figure 50.4 — La carte de fraîcheur : les cinquante chapitres et la date de gel de chacun. » (p. 577)
* **Diagnostic causal approfondi** :
  1. *Substitution de l'objet de recherche* : Le mandat d'architecture d'un chapitre intitulé « Péremption et protocole de revalidation » au sein d'une entreprise agentique réglementée (soumise à la ligne directrice BSIF/OSFI E-23 et à la gouvernance de l'AMF) est de spécifier le **cycle de vie opérationnel des agents et modèles IA en production** : quand et comment décommissionner un agent, sur quels critères de dérive, et comment exécuter son retrait sécurisé. Or, le Chapitre 50 s'est intégralement transformé en un guide de maintenance éditoriale du document lui-même (la fraîcheur des fiches de lecture S-001 à S-159 face à des événements d'actualité).
  2. *Vide opérationnel en environnement financier* : Le texte présente un décompte de **zéro occurrence** pour les notions indispensables de *décommissionnement*, *fin de vie*, *recertification*, *drainage de tâches*, et *purge de mémoire*. En pratique bancaire, le décommissionnement d'un agent impose pourtant :
     - La détection de dérive objective : dégradation de la métrique d'alignement ou dérive de concept (*concept drift*) mesurée sur des jeux d'essais métamorphiques au-delà d'un seuil critique $\epsilon$.
     - Le protocole de mise hors service en 5 phases : (1) Passage à l'état `DRAINING` (rejet de nouvelles sollicitations, terminaison des transactions et sagas en vol), (2) Révocation cryptographique des identités (certificats mTLS, identifiants SPIFFE SVID, clés de signature de passeport W3C DID), (3) Déréférencement atomique dans les annuaires et catalogues d'outils MCP/A2A, (4) Purge mémorielle sécurisée (effacement des contextes et des vecteurs de mémoire associative conformément aux obligations légales de l'art. 12.1 de la Loi 25 québécoise et du RGPD), (5) Scellement probatoire et archivage immuable des journaux d'audit pour les régulateurs (conservation minimale 7 ans).
* **Correctif formel** :
  - Scinder le Chapitre 50 en deux parties distinctes :
    * **§ 50.1 - Protocole d'ingénierie logicielle pour le cycle de vie, la recertification et le décommissionnement sécurisé des agents** (formalisation de la machine à états : `STAGING` $\rightarrow$ `CERTIFIED` $\rightarrow$ `ACTIVE` $\rightarrow$ `DRIFT_ALERT` $\rightarrow$ `DRAINING` $\rightarrow$ `DECOMMISSIONED`).
    * **§ 50.2 - Métagouvernance documentaire et protocole de mise à jour des connaissances du Compendium**.

---

### 2.2 Défauts Majeurs (Lacunes méthodologiques, bibliographiques et architecturales — R2/R3)

---

#### DÉFAUT M-01 : Erreur factuelle sur le statut du standard d'idempotence HTTP de l'IETF
* **Localisation** : Chapitre 48, Section 48.5, page 544.
* **Citation textuelle** :
  > « Le brouillon draft-ietf-httpapi-idempotency-key-header, The Idempotency-Key HTTP Header Field, de Jena et Dalal, groupe de travail httpapi de l’IETF, spécifie un en-tête par lequel un client marque une requête non idempotente [...] Son statut se dit à chaque mention et il est sévère : révision −07 du 15 octobre 2025, et le document est EXPIRÉ — il n’a pas atteint le stade de RFC, et rien n’établit qu’il l’atteindra. La conclusion du § 48.2 n’est donc pas levée : l’écosystème n’a même pas d’en-tête normalisé pour dire « ceci est un réessai » — il en a eu un projet, et ce projet a expiré, ce qui est un constat plus dur que l’absence pure. » (p. 544)
* **Diagnostic causal approfondi** :
  - L'auteur tire une conclusion négative radicale (« l'écosystème n'a même pas d'en-tête normalisé... ce projet a expiré, ce qui est un constat plus dur que l'absence pure ») en se basant sur la péremption temporaire de la version draft-07.
  - Or, la révision officielle **`draft-ietf-httpapi-idempotency-key-header-08`** a été formellement soumise et publiée au sein du groupe de travail HTTPAPI de l'IETF le **22 octobre 2026** (par J. Jena, S. Dalal et D. Tishkin).
  - Le document n'était donc nullement abandonné ni expiré à la date de gel final du Compendium (24-27 octobre 2026). Présenter un travail en cours d'avancement actif comme un échec définitif constitue une falsification involontaire de l'état de l'art normatif.
* **Correctif formel & Référence** :
  - Mettre à jour l'identifiant documentaire : citer `draft-ietf-httpapi-idempotency-key-header-08` (22 octobre 2026).
  - Rectifier le constat : l'IETF consolide activement le standard de l'en-tête `Idempotency-Key`, prévoyant l'intégration des codes de retour HTTP 409 (*Conflict*) et 425 (*Too Early*) pour les requêtes concurrentes réémises, fournissant ainsi la brique protocolaire manquante aux architectures agentiques.

---

#### DÉFAUT M-02 : Incohérence arithmétique et déséquilibre structurel de la bibliographie consolidée
* **Localisation** : Annexe I, Section Régime de cette annexe, page 585.
* **Citation textuelle** :
  > « Mesure Valeur  
  > Entrées relevées aux sept bibliographies du Vol. I : 1263  
  > Doublons fondus par identifiant normalisé : • 134  
  > Entrées uniques de la présente annexe : 1065  
  > Adresses primaires reprises des socles des Vol. II et III : 0 » (p. 585)
* **Diagnostic causal approfondi** :
  1. *Anomalie de calcul mathématique* :
     $$1263 - 134 = 1129 \neq 1065$$
     Il subsiste un déficit de **64 entrées** ($1129 - 1065 = 64$) qui ont été omises ou éliminées du décompte sans la moindre explication de méthode (entrées corrompues ? filtres d'exclusion non documentés ? coquille de saisie ?). Dans une annexe dont l'objet déclaré est la métrologie documentaire absolue, une telle contradiction numérique viole les exigences élémentaires de rigueur.
  2. *Asymétrie épistémique des volumes* :
     La mention « Adresses primaires reprises des socles des Vol. II et III : 0 » révèle que l'Annexe I ne contient aucune source primaire provenant des Volumes II (L'autonomie encadrée) et III (L'entreprise agentique). Ces volumes, qui fondent la réglementation bancaire canadienne (BSIF, AMF, Loi 25) et l'architecture de sécurité (AgentMesh, OAuth, DID/VC), se trouvent ainsi privés d'un appareil bibliographique primaire consolidé et vérifiable par les pairs, affaiblissant l'assise scientifique de toute la seconde moitié de l'ouvrage.
* **Correctif formel** :
  - Rectifier immédiatement le tableau de la page 585 : ajuster le nombre de doublons fondus à 198 (si 1065 est le nombre d'entrées réelles) ou expliciter une ligne `Entrées écartées pour métadonnées incomplètes : 64`.
  - Effectuer la convergence bibliographique en intégrant les références primaires des Volumes II et III dans l'Annexe I.

---

#### DÉFAUT M-03 : Méconnaissance de l'outillage de supply chain sécurisée OCI / Sigstore et limitation artificielle du packaging SBOM
* **Localisation** : Chapitre 47, Sections 47.2, 47.3 et 47.8, pages 530-532, 535-536.
* **Citations textuelles** :
  > « Le volet « profils d’IA » du corpus est INSTRUIT le 30 juillet 2026 [...] Des cinq composants du § 47.1 : les poids de modèle sont couverts par des champs nommés dans les deux nomenclatures [...] Mais les deux composants proprement agentiques n’ont AUCUN champ : ni les invites, ni la politique d’autorisation ne portent de propriété dans l’un ou l’autre schéma... » (p. 531)  
  > « La recherche d’un mécanisme normalisé d’attestation d’intégrité au-delà du protocole examiné n’a pas été menée, registre officiel, mécanismes de provenance de paquets et catalogues d’éditeurs n’ayant pas été ouverts. Le socle ne documente ni l’existence ni l’absence d’un tel mécanisme du côté de la chaîne d’approvisionnement — degré 3. » (p. 532)
* **Diagnostic causal approfondi** :
  - L'auteur déplore l'absence de champs explicites dans CycloneDX et SPDX pour les fichiers d'invites (`prompts`) et les politiques, et en déduit l'impossibilité de garantir la provenance logicielle d'un agent.
  - C'est ignorer l'architecture de distribution et de scellement logiciel universellement adoptée dans l'industrie en 2024-2026 :
    1. **Conteneurisation OCI (Open Container Initiative)** : Un agent complet est packagé sous la forme d'un artefact conteneur OCI unifié (regroupant le runtime, le descripteur d'outils, les invites de commande versionnées dans des couches dédiées et les politiques déclaratives).
    2. **Écosystème Sigstore / Cosign & In-toto** : Les spécifications *in-toto Attestation Framework* (spécification v1.0) combinées à la signature sans clé (*keyless signing*) via Sigstore (Fulcio pour les certificats éphémères adossés à OIDC, Rekor pour le registre de transparence immuable) et aux attestations de niveau **SLSA Build L3** permettent de signer cryptographiquement l'empreinte SHA-256 de chaque composant d'agent dès sa compilation en pipeline CI/CD hermétique.
    3. Dans CycloneDX 1.7 et SPDX 3.0, les fichiers d'invites et de politiques sont parfaitement modélisables via des composants de type `file` ou `configuration` assortis d'empreintes cryptographiques de contenu (`hashes`). L'absence d'une étiquette textuelle littérale `"prompt"` n'empêche en rien l'intégrité de la chaîne de provenance.
* **Correctif formel & Références d'état de l'art** :
  - Compléter la section 47.3 en intégrant l'architecture de référence SLSA L3 + in-toto + Sigstore Cosign pour conteneurs OCI.
  - Références à inclure : *Torres-Arias et al. (2019), in-toto*, USENIX Security ; *OpenSSF SLSA Specification v1.2* (Source & Build Tracks, nov. 2025).

---

### 2.3 Défauts Mineurs (Imprécisions de traçabilité, formulations et annotations)

---

#### DÉFAUT m-01 : Omission des standards de corrélation distribuée W3C Trace Context et OpenTelemetry Baggage
* **Localisation** : Chapitre 48, Section 48.5, pages 543-544.
* **Citation textuelle** :
  > « La question est étroite : ce qu’une trace d’exécution enregistre est un appel, non son effet. La somme situe le chaînon manquant au ch. 38 § 38.5, et ce chapitre le prolonge au seul grain qui lui appartient : ce qui manque n’est pas la trace de l’appel, c’est la jointure entre l’appel tracé et l’effet enregistré ailleurs. » (p. 543)
* **Diagnostic causal** :
  - L'auteur traite la liaison entre l'appel de l'agent et l'effet persisté dans un système tiers comme un « problème non résolu faute de standard ».
  - Or, la recommandation officielle **W3C Trace Context (2021)** et le standard **OpenTelemetry Baggage** définissent précisément le mécanisme universel de propagation de contexte d'exécution (`traceparent`, `tracestate`, métadonnées de corrélation métier). En transmettant le `trace_id` et l'identifiant d'action dans les métadonnées de l'appel d'outil, le système récepteur persiste cet identifiant au sein de sa transaction de données, matérialisant la clé de jointure exacte recherchée.
* **Correctif** :
  - Citer le standard W3C Trace Context comme mécanisme formel de jointure déterministe entre l'observabilité agentique et la persistance des systèmes d'enregistrement.

---

#### DÉFAUT m-02 : Statut de la directive révisée sur la responsabilité du fait des produits (PLD)
* **Localisation** : Chapitre 49, Section 49.10, page 558.
* **Citation textuelle** :
  > « ...dont la transposition est due au 9 décembre 2026 — date à re-vérifier — et qui ne s’applique qu’aux produits mis sur le marché après ce terme... » (p. 558)
* **Diagnostic causal** :
  - Le texte porte la mention d'incertitude « date à re-vérifier ».
  - Notre vérification légale confirme formellement que la **Directive (UE) 2024/2853** a été définitivement adoptée et publiée au Journal officiel de l'Union européenne, fixant la date butoir impérative de transposition nationale par les États membres au **9 décembre 2026**.
* **Correctif** :
  - Lever la réserve : supprimer la mention « date à re-vérifier » et citer la référence officielle *Directive (UE) 2024/2853 du Parlement européen et du Conseil*.

---

## 3. Audit bibliographique et état de l'art (R3)

### 3.1 Vérification rigoureuse des références citées dans le segment

| Réf. / Citation | Emplacement | Statut d'audit | Constat, DOI et Ancrage Factuel |
| :--- | :--- | :--- | :--- |
| **Chen et al. (2018)** *Metamorphic Testing: A Review...* | Ch. 47, p. 536 | **VÉRIFIÉ** | ACM Computing Surveys 51(1), art. 4, 2018. DOI: `10.1145/3143561`. Référence fondatrice sur le problème de l'oracle de test pour systèmes non déterministes. |
| **Morris et al. (2023)** *Levels of AGI...* | Ch. 49, p. 555 | **VÉRIFIÉ** | Google DeepMind, arXiv:2311.02462. Taxonomie standardisée des niveaux d'autonomie et de généralité d'agents. |
| **Gao et al. (2025)** *A Survey of Self-Evolving Agents...* | Ch. 49, p. 555 | **VÉRIFIÉ** | arXiv:2507.21046 (juillet 2025). État de l'art sur l'auto-évolution des modèles et mémoires d'agents. |
| **Directive (UE) 2024/2853** (PLD Révisée) | Ch. 49, p. 558 | **VÉRIFIÉ** | Directive officielle sur la responsabilité du fait des produits défectueux incluant les logiciels et systèmes d'IA. Échéance de transposition confirmée au 9 décembre 2026. |
| **CycloneDX 1.7 / ECMA-424 2e éd.** | Ch. 47, pp. 530-531 | **VÉRIFIÉ** | Standard OWASP / Ecma TC54 normalisé en 2e édition (2025/2026) avec profils machine-learning-model et CBOM post-quantique. |
| **SLSA v1.2** (Source & Build Tracks) | Ch. 47, p. 530 | **VÉRIFIÉ** | Spécification OpenSSF approuvée le 24 novembre 2025, introduisant la piste Source Track à côté de la piste Build Track. |
| **NIST SP 800-218A** (SSDF GenAI) | Ch. 47, p. 530 | **VÉRIFIÉ** | Profil communautaire du Secure Software Development Framework pour l'IA générative, version finale publiée le 26 juillet 2024. |
| **IETF draft-ietf-httpapi-idempotency-key** | Ch. 48, p. 544 | **ERRONÉ** | Déclaré à tort « EXPIRÉ » sous révision -07 d'octobre 2025. Révision `-08` active publiée le 22 octobre 2026 par l'IETF. |
| **« Pseudo-théorème » de gouvernance** | Ch. 49, p. 553, 558 | **NON SOURCÉ** | Aucune référence académique, aucun auteur, aucun formalisme mathématique. Affirmation non scientifique à déclassifier. |

---

### 3.2 Littérature fondamentale et récente (jusqu'en 2026) omise

L'absence des références suivantes constitue une lacune majeure pour un ouvrage de niveau doctoral en ingénierie des systèmes et interopérabilité agentique :

1. **Calculabilité, décidabilité et moniteurs de sécurité formels** :
   * **Rice, H. G. (1953)**. *Classes of recursively enumerable sets and their decision problems*. Transactions of the American Mathematical Society, 74(2), 358–366.  
     *Justification d'omission* : Fondement mathématique absolu démontrant pourquoi la vérification statique de conformité comportementale d'un agent capable d'appels d'outils arbitraires (Turing-complet) est indécidable.
   * **Schneider, F. B. (2000)**. *Enforceable security policies*. ACM Transactions on Information and System Security (TISSEC), 3(1), 30–50.  
     *Justification d'omission* : Référence incontournable délimitant formellement ce qu'une passerelle Zero Trust / PEP peut intercepter à l'exécution (propriétés de sûreté vs de vivacité).
2. **Systèmes distribués, atomicité relaxée et consensus sous défaillance** :
   * **Garcia-Molina, H., & Salem, K. (1987)**. *Sagas*. ACM SIGMOD Record, 16(3), 249–259.  
     *Justification d'omission* : Définition formelle des transactions compensables, pivots et réitérables, indispensable pour éviter l'effondrement des plans d'agents financiers.
   * **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985)**. *Impossibility of distributed consensus with one faulty process (FLP)*. Journal of the ACM, 32(2), 374–382.  
     *Justification d'omission* : Démonstration de l'impossibilité d'obtenir un consensus déterministe en asynchronie totale, explicitant les limites réelles de l'idempotence distribuée.
   * **Lamport, L. (1978 / 1998)**. *The Part-Time Parliament (Paxos)* & *Time, Clocks and the Ordering of Events*. ACM TOCS / CACM.
3. **Sécurité de la chaîne d'approvisionnement logicielle et attestation cryptographique** :
   * **Torres-Arias, S. et al. (2019)**. *in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes*. In 28th USENIX Security Symposium, pp. 1393–1410.  
     *Justification d'omission* : Cadre standard d'attestation de pipeline permettant de relier le code source, les invites de commande et les politiques aux artefacts exécutables.
   * **Sigstore Architecture Specification (Linux Foundation / OpenSSF, 2022-2025)**. Spécifications des protocoles Fulcio (OIDC PKI), Rekor (transparency log) et Cosign pour le scellement d'images d'agents OCI.
4. **Observabilité distribuée et traçabilité de bout en bout** :
   * **W3C Recommendation (2021)**. *W3C Trace Context - Level 1*. World Wide Web Consortium.  
     *Justification d'omission* : Standard industriel résolvant la jointure entre l'appel d'outil et l'effet persisté dans les systèmes d'enregistrement via propagation de contexte.

---

## 4. Recommandations concrètes pour le segment

À la lumière des constats d'audit, nous formulons six recommandations directes d'ingénierie et de révision textuelle pour le Livre V :

1. **Restructurer formellement le Chapitre 48 (Sémantique d'effet)** :
   * Remplacer la règle absolue de la Figure 48.2 par une modélisation rigoureuse de la déduplication distribuée par consensus (SMR).
   * Intégrer les conditions nécessaires d'ordonnancement du patron Saga pour agents autonomes : interdiction stricte de composer dynamiquement plus d'une transaction pivot non compensable, et obligation de verrous sémantiques (*semantic escrow*) pour prévenir les anomalies de lecture sale (*dirty reads*).
   * Mettre à jour la citation du standard IETF `draft-ietf-httpapi-idempotency-key-header` en intégrant la révision active `-08` du 22 octobre 2026.
2. **Introduire les limites de calculabilité dans le Chapitre 49** :
   * Poser le Théorème de Rice (1953) comme borne théorique infranchissable de la conformité statique des agents.
   * Borner les mécanismes de contrôle d'accès et d'interception Zero Trust aux seules propriétés de sûreté selon la formalisation de Schneider (2000).
   * Supprimer l'appellation « théorème » pour l'arbitrage de gouvernance à 4 propriétés, ou en fournir la preuve axiomatique complète.
3. **Refondre le Chapitre 50 pour y inscrire le protocole de décommissionnement opérationnel** :
   * Rédiger la spécification d'ingénierie logicielle pour la fin de vie des agents en production : machine d'états de mise hors service, drainage des sessions asynchrones (`DRAINING`), révocation des certificats mTLS / SPIFFE / DID, déréférencement MCP/A2A, purge mémorielle chiffrée selon la Loi 25 et le RGPD, et archivage probatoire des pistes d'audit.
   * Déplacer la gestion de fraîcheur des fiches de lecture du Compendium dans une section de gouvernance documentaire distincte.
4. **Compléter le modèle de provenance du Chapitre 47** :
   * Décrire le patron canonique de packaging d'agent sous format d'image OCI, scellée par attestations in-toto (SLSA Build L3) et signée via Sigstore/Cosign.
   * Clarifier comment les invites de commande et politiques d'accès sont encapsulées comme des fichiers de configuration intègres identifiés par hash SHA-256 dans les nomenclatures CycloneDX 1.7 et SPDX 3.0.
5. **Corriger l'arithmétique de l'Annexe I (p. 585)** :
   * Rectifier immédiatement l'incohérence mathématique : $1263 - 134 = 1129 \neq 1065$, en indiquant la répartition exacte des doublons réels et des entrées filtrées.
   * Engager le rapprochement bibliographique pour intégrer les sources primaires des Volumes II et III dans l'Annexe I.
6. **Harmoniser la terminologie d'observabilité avec OpenTelemetry et W3C** :
   * Préciser que la jointure entre trace d'appel et effet persisté s'opère par injection des identifiants `traceparent` et `Baggage` dans les requêtes d'outils et messages financiers ISO 20022.
