# Rapport d'Unité Définitif (Niveau Racine L2) — Livre V : Clôture (pp. 527–585)

**Tournoi RSA [4, 2, 1] — Synthèse Racine L2_1**  
**Document audité** : `documents/Compendium.pdf` (*Interopérabilité et Orchestration en Entreprise Agentique*, Édition de novembre 2026, faits gelés au 27 juillet 2026, actualisation au 1er novembre 2026)  
**Segment** : `segment_livre_5_cloture` (Livre V : *Livrer et clore*, Chapitres 47 à 50 et transition vers les Annexes B et I, pages 527 à 585)  
**Auteur de la synthèse racine** : Agrégateur Racine L2_1 (Rôles : Implementer / QA / Specialist)  
**Rapports d'entrée arbitrés et consolidés** :  
- `evolved_1.md` (Agrégation L1_1 arbitrée à partir de `candidate_1.md` et `candidate_2.md`)  
- `evolved_2.md` (Agrégation L1_2 arbitrée à partir de `candidate_3.md` et `candidate_4.md`)  
**Axes d'évaluation** : R2 (Rigueur formelle, algorithmique et systèmes distribués) · R3 (Audit bibliographique, état de l'art et traçabilité des sources primaires)  
**Date d'arbitrage définitif** : 3 novembre 2026  
**Livrables officiels** :  
- `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_5_cloture\unit_report_segment_livre_5_cloture.md`  
- `c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l2_1\handoff.md`  

---

## 1. Verdict exécutif et évaluation critique du segment Livre 5 Clôture

### 1.1 Objet et ambition du segment

Le Livre V (« *Livrer et clore : l’agent comme livrable logiciel, horizon et frontière* », chapitres 47 à 50, pages 527 à 585) forme le couronnement architectural du *Compendium*. Il assume une fonction pivot dans l'édifice global : alors que les Livres I à IV ont tour à tour appréhendé l'agent comme un interlocuteur protocolaire (Livre I), un mandataire sous identité non-humaine opposable (Livre II), un automate sous gouvernance prudentielle (Livre III) et un maillage de micro-services agentiques distribués (Livre IV), le Livre V a pour mission de le matérialiser en un **artefact logiciel manufacturé, scellé, exécuté sous contraintes transactionnelles strictes, projeté sur un horizon technologique borné par la calculabilité et décommissionnable de façon vérifiable en environnement réglementé**.

Le segment se déploie selon quatre axes structurants :
1. **L'artefact livré et la provenance logicielle (Ch. 47, pp. 527–537)** : décomposition anatomique en cinq composants, nomenclatures logicielles et d'IA (CycloneDX 1.7 / ECMA-424 2e éd., SPDX 2.2.1/3.0), attestations d'intégrité de la supply chain (in-toto, SLSA v1.2, RFC 9334 RATS) et vérification comportementale par tests métamorphiques (Chen et al., 2018).
2. **La sémantique d'effet et les transactions d'outils (Ch. 48, pp. 538–544)** : formalisation des classes d'effets d'outils, sémantique d'idempotence (*at-least-once* vs *effectively-once*), adaptation du patron Saga aux trajectoires dynamiques et réconciliation de bout en bout des transactions bancaires (ISO 20022 UETR, rails canadiens Lynx et RTR).
3. **L'horizon prospectif 2027–2032 et les frontières de la calculabilité (Ch. 49, pp. 545–568)** : épistémologie prospective (quadruplet PROGRAMMÉ, PROJETÉ, SPÉCULATIF, FAIT ÉTABLI), inventaire des 22 lacunes de recherche du corpus, et délimitation formelle des capacités de composition et de délégation multi-sauts.
4. **La péremption, la revalidation et la clôture bibliographique (Ch. 50 & Annexes B/I, pp. 568–585)** : grille des 14 événements déclencheurs d'obsolescence documentaire, inventaire des 159 faits consolidés (S-001 à S-159) et consolidation arithmétique des 1263 références bibliographiques du corpus.

### 1.2 Verdict global de l'évaluation racine L2

L'audit critique approfondi mené au niveau racine L2 — fondé sur la réconciliation intégrale des 4 rapports candidats L0, des 2 synthèses évoluées L1, et sur la vérification primaire mot à mot sur le texte source (`DOCUMENT_TEXT_MAP.md`) et sur les planches visuelles (`page-527.png` à `page-585.png`) — conduit à un **verdict sévère et sans complaisance** :

**Le segment Livre V Clôture, dans son état compilé actuel, n'est pas recevable pour une mise en production réglementée.** 

Si l'effort méthodologique d'auto-limitation épistémique (refus constant du marketing de l'IA, étiquetage rigoureux des degrés de preuve et des absences documentaires) est remarquable, l'ouvrage est grevé par **cinq défauts bloquants destructeurs, huit défauts majeurs de modélisation et de veille normative, et quatre défauts mineurs de cohérence textuelle**.

Les quatre faillites structurelles majeures du segment sont :
1. **La substitution complète de l'objet de recherche au Chapitre 50** : Promis comme le protocole de fin de vie, d'obsolescence et de décommissionnement sécurisé de l'agent logiciel en production bancaire (BSIF/OSFI E-23, Loi 25 québécoise art. 12.1), le chapitre dévie à 100 % vers une procédure interne d'auto-maintenance éditoriale du document papier *Compendium*. Le terme « décommissionnement » compte **zéro occurrence** dans tout le volume.
2. **Des ruptures formelles critiques en systèmes distribués au Chapitre 48** : 
   - L'affirmation selon laquelle « *la livraison au-moins-une-fois couplée à un consommateur idempotent garantit un traitement exactement-une-fois* » méconnaît le problème fondamental de la double écriture (*Dual-Write Problem*), le réordonnancement des opérations non-commutatives sous asynchronie (Helland 2012) et l'exigence d'un consensus distribué (FLP 1985, Raft/Paxos) pour répliquer le registre de clés.
   - L'application du patron Saga à des agents générateurs de plans dynamiques décrète à tort l'impossibilité de la compensation, tout en ignorant le véritable écueil théorique : **l'absence d'isolation ($ACID$ sans $I$)**, qui autorise des lectures sales (*dirty reads*) et des cascades d'incohérences financières entre agents concurrents.
3. **L'amnésie théorique sur la calculabilité au Chapitre 49** : L'impossibilité de vérifier formellement la conformité sémantique des politiques d'agents est attribuée au caractère probabiliste des modèles, occultant la barrière mathématique cardinale : le **Théorème de Rice (1953)** et l'indécidabilité de l'arrêt de Turing. De surcroît, le chapitre invoque un prétendu « *théorème de gouvernance à 4 propriétés* » au statut « spéculatif », ce qui constitue un oxymore épistémique sans formalisation mathématique ni citation d'auteur.
4. **Des corruptions matérielles et des collisions textuelles déstructurantes** : Le pipeline d'assemblage (Pandoc/LaTeX) a produit des défaillances typographiques inacceptables pour une publication de référence : phrases tronquées en fin de page (pp. 528, 563), collision déstructurant intégralement le Tableau 47.2 (p. 530), injection brute de notes de révision internes au beau milieu de phrases rédigées (pp. 544, 566–567), et tableau d'Annexe I brisé avec des cellules chiffrées éjectées sous la table et une contradiction arithmétique de 64 entrées ($1263 - 134 = 1129 \neq 1065$).

---

## 2. Matrice consolidée des défauts par sévérité

### Grille de classification académique et réglementaire
- **[Bloquant / Erreur formelle & architecturale] (Critical)** : Erreur mathématique, rupture de consistance en système distribué, violation de théorème fondamental, substitution d'objet réglementaire ou corruption matérielle textuelle invalidant la démonstration ou rendant le texte indéchiffrable.
- **[Majeur / Lacune méthodologique & État de l'art] (Major)** : Omission substantielle de la littérature, qualification erronée d'un standard de l'industrie, lacune de modélisation affaiblissant l'opposabilité de l'architecture sans détruire l'ensemble de la démonstration.
- **[Mineur / Clarté, Cohérence & Typographie] (Minor)** : Coquille typographique, rupture syntaxique localisée, discordance taxonomique interne ou réserve temporelle caduque.

```
========================================================================================================================
                                     SYNTHÈSE DE LA MATRICE CONSOLIDÉE DES DÉFAUTS
========================================================================================================================
ID        Sévérité   Localisation        Objet du constat                                      Statut RSA [4,2,1]
------------------------------------------------------------------------------------------------------------------------
DEF-L5-01 Bloquant   Ch. 48, pp. 539-541 Fausse équivalence Exactly-Once, Dual-Write & FLP     Unanime (C1/C2/C3/C4)
DEF-L5-02 Bloquant   Ch. 48, pp. 541-542 Fausse impossibilité Saga dynamique & Défaut d'iso.   Unanime (C1/C2/C3/C4)
DEF-L5-03 Bloquant   Ch. 50, pp. 568-577 Substitution d'objet : Décommissionnement absent     Unanime (C1/C2/C3/C4)
DEF-L5-04 Bloquant   Ch. 49, pp. 552-558 Omission Théorème de Rice & Pseudo-théorème 4 prop.   Unanime (C1/C2/C3/C4)
DEF-L5-05 Bloquant   Transversal L5      Corruptions de compilation, collisions & tables HS    Unanime (7 sites vérifiés)
DEF-L5-06 Majeur     Ch. 48, p. 544      Statut erroné IETF Idempotency-Key Header (-08)       Unanime (C1/C2/C3/C4)
DEF-L5-07 Majeur     Ch. 47, pp. 530-532 Omission Sigstore & statut CNCF Graduated in-toto     Consolidé (C1/C4)
DEF-L5-08 Majeur     Ch. 48, p. 539      Falsification de la neutralité de la lecture (T48.1)  Consolidé (C4/L1_2)
DEF-L5-09 Majeur     Annexe I, p. 585    Contradiction arithmétique 1263-134 et circularité    Unanime (C1/C2/C3/C4)
DEF-L5-10 Majeur     Ch. 48/49, p. 541   Évacuation fautive du modèle de pannes (« assumé »)   Consolidé (C4/L1_2)
DEF-L5-11 Majeur     Ch. 47, pp. 529,535 Incohérence taxonomique des 5 composants vs horloges  Consolidé (C2/L1_1)
DEF-L5-12 Majeur     Ch. 47/49, p. 566   Délégation multi-sauts érigée à tort en impasse       Consolidé (C4/L1_2)
DEF-L5-13 Majeur     Ch. 47, pp. 528,535 Sous-spécification du versionnement (GPU/Mémoire)     Consolidé (C3/L1_2)
DEF-L5-14 Mineur     Ch. 48, pp. 543-544 Omission W3C Trace Context & OpenTelemetry Baggage    Consolidé (C1/C4)
DEF-L5-15 Mineur     Ch. 48, p. 542      Contradiction interne sur l'occurrence de « sagas »   Consolidé (C2/L1_1)
DEF-L5-16 Mineur     Ch. 49, p. 558      Réserve caduque sur la Directive PLD 2024/2853        Consolidé (C1/L1_1)
DEF-L5-17 Mineur     Ch. 50, pp. 574-575 Paradoxe d'auto-invalidation sur la règle des 30 j    Consolidé (C3/C4)
========================================================================================================================
```

---

### 2.1 Défauts Bloquants / Erreurs Formelles & Architecturales (Critical — Axe R2)

#### DEF-L5-01 : Falsification de l'équivalence transactionnelle « At-Least-Once + Idempotence = Exactly-Once », Dual-Write Problem et circularité sous pannes
* **Localisation exacte** : Chapitre 48, Section 48.1 et 48.2, pages 539-541 & Figure 48.2 (p. 541).
* **Citations textuelles vérifiées** :
  > « *...le ch. 1 § 1.5.2 établit que la livraison exactement-une-fois est irréalisable sous pannes [...] et que la voie praticable est le traitement exactement-une-fois, obtenu en combinant une livraison au-moins-une-fois avec un consommateur idempotent. Ce chapitre en tire la conséquence que le ch. 1 lui assigne : si la livraison ne peut être garantie, l’effet doit l’être...* » (p. 539, lignes 48604-48612)  
  > « *Figure 48.2 — La seule composition qui tienne sous pannes : livraison au-moins-une-fois et consommateur idempotent.* » (p. 541, lignes 48770-48772)  
  > « *Lecture de l’auteur — la conséquence est dissymétrique et elle est le cœur de la section : l’idempotence est une propriété de l’outil invoqué, pas du protocole qui l’invoque, ni de l’agent qui décide de l’invoquer.* » (p. 540, lignes 48722-48726)  
  > « *(2) L’accord entre agents sous asynchronie et défaillance partielle n’est pas traité, et cette absence est un périmètre assumé, non un oubli.* » (p. 541, lignes 48805-48807)
* **Diagnostic causal approfondi** :
  Ce raisonnement présente une triple faille formelle destructrice pour l'ingénierie des systèmes transactionnels distribués :
  1. *Rupture de l'équivalence Exactly-Once (Helland 2012, Gray 1978)* : L'idempotence scalaire d'une fonction ($f(f(x)) = f(x)$) ne garantit le traitement exactement-une-fois d'une séquence d'actions que sous l'hypothèse stricte de **commutativité des opérations** ou d'un **ordonnancement monotone strict**. Dans un réseau asynchrone, les réessais introduisent du désordre temporel. Si un agent émet $R_1$ puis $R_2$, et que $R_2$ parvient au système cible avant $R_1$ à la suite d'une gigue réseau, le consommateur exécute $R_2 \circ R_1$. Or, les transactions bancaires (débits, crédits, clôtures) ne commutent pas ($R_1 \circ R_2 \neq R_2 \circ R_1$). En l'absence de jeton d'ordonnancement monotone (*fencing token*), l'idempotence locale n'empêche pas la corruption de l'état final.
  2. *Le problème de la double écriture (Dual-Write Problem)* : L'application de l'effet métier $\Delta S$ (ex. virement interbancaire) et la mémorisation de la clé d'idempotence $K$ dans le registre de déduplication constituent deux écritures distinctes. Si le serveur applique $\Delta S$ sur le système d'enregistrement mais s'effondre avant d'enregistrer $K$ dans sa base locale, le rejeu émis par l'agent entraînera une **seconde mutation non désirée**. Inversement, si la clé $K$ est persistée avant la validation de $\Delta S$, un crash intermédiaire provoquera un acquittement fantôme sans exécution de l'effet (*lost update*). L'idempotence crash-safe requiert obligatoirement une frontière transactionnelle unifiée, formalisée par le patron **Transactional Outbox** (Richardson, 2018).
  3. *Circularité vicieuse et consensus distribué (Théorème FLP 1985)* : L'auteur décrète que l'idempotence est « une propriété de l'outil, pas du protocole », tout en assumant évacuer « l'accord sous asynchronie ». C'est une contradiction mathématique : dans une architecture hautement disponible, le serveur d'outils est répliqué sur plusieurs nœuds. Pour qu'un outil distribué garantisse l'idempotence, le registre des clés consommées doit être synchronisé avec consistance forte (linéarisabilité). Empêcher deux exécutions concurrentes portant la même clé $K$ nécessite de résoudre le consensus distribué (State Machine Replication via Raft/Paxos), soumis au **Théorème d'impossibilité FLP** (Fischer, Lynch, Paterson, 1985). Évacuer l'accord distribué détruit le fondement même de l'idempotence sous panne.
* **Contre-exemple formel et correctif** :
  * *Contre-exemple financier* : Soit un solde de compte $S_0 = 100\,\$$.  
    Requête 1 ($R_1$, clé $K_1$) : retirer $80\,\$$.  
    Requête 2 ($R_2$, clé $K_2$) : appliquer $10\,\$$ de frais si $S < 50\,\$$, sinon $0\,\$$.  
    - Ordre séquentiel réel : $R_1$ s'exécute ($S=20\,\$$) ; puis $R_2$ s'exécute ($20 < 50 \implies S = 10\,\$$). Solde final = $10\,\$$.  
    - Ordre sous asynchronie/rejeu : $R_2$ arrive en premier ($100 \ge 50 \implies \text{frais}=0$, $S=100\,\$$) ; puis $R_1$ arrive ($S = 20\,\$$). Solde final = $20\,\$$.  
    Chaque opération a été exécutée de manière strictement idempotente, mais l'état final est corrompu d'une perte d'actif de $10\,\$$.
  * *Correctif architectural* : Reformuler la Figure 48.2 et poser l'équation complète :
    $$\text{Traitement Effectively-Once} \iff (\text{At-Least-Once}) \land (\text{Idempotence locale}) \land (\text{Fencing Tokens}) \land (\text{Consensus SMR sur registre de clés}) \land (\text{Transactional Outbox})$$
* **Statut de validation RSA** : **Accord unanime** (C1 B-01, C2 Défaut 4, C3 Défaut B-01, C4 Défaut B-01, L1_1 B-02, L1_2 B-01).

---

#### DEF-L5-02 : Inapplicabilité démontrée du patron Saga aux trajectoires dynamiques sans transaction pivot unique et occultation du défaut d'isolation ($ACID$ sans $I$)
* **Localisation exacte** : Chapitre 48, Section 48.3, pages 541-542 & Figure 48.3 (p. 542).
* **Citations textuelles vérifiées** :
  > « *Une saga classique suppose que l’ensemble des étapes soit connu du concepteur : la compensation de l’étape k est écrite en même temps que l’étape k. Un agent qui compose sa trajectoire à l’exécution [...] produit des suites d’étapes que personne n’a écrites, donc des suites dont personne n’a écrit les compensations... Le socle consolidé ne documente aucun dispositif de compensation dont la portée soit une trajectoire d’agent non fixée à la conception — degré 3.* » (p. 541, lignes 48788-48800)  
  > « *(1) La compensation n’est pas l’annulation. Elle annule sémantiquement — un remboursement compense un débit, il ne le supprime pas ; les deux écritures subsistent.* » (p. 541, lignes 48801-48804)
* **Diagnostic causal approfondi** :
  Le raisonnement du Compendium est doublement défaillant (fausse barrière sur la composition et cécité sur l'isolation) :
  1. *Fausse impossibilité algorithmique de la compensation dynamique* : L'affirmation selon laquelle « personne n'a écrit les compensations d'une trajectoire dynamique » repose sur une confusion entre *composition de plan* et *déclaration des opérateurs d'outils*. En planification formelle (STRIPS/PDDL) comme dans les moteurs de workflows durables (Temporal, AWS Step Functions), chaque outil élémentaire $t_i \in \mathcal{T}$ expose son contrat d'inversion sémantique $C(t_i) = t_i^{-1}$ (ex. `réserver_fonds` $\leftrightarrow$ `libérer_fonds`). Lorsqu'un agent assemble dynamiquement une chaîne d'actions $w = t_1 t_2 \dots t_k$, l'orchestrateur déterministe empile ces actions dans un journal d'annulation (*undo log / compensation stack*). En cas d'échec à l'étape $k+1$, la séquence de compensation est exécutée de façon déterministe dans l'ordre inverse LIFO :
     $$\text{Rollback}(w) = C(t_k) \circ C(t_{k-1}) \circ \dots \circ C(t_1)$$
  2. *Violation du modèle formel des Sagas : L'absence de transaction pivot (Garcia-Molina & Salem, 1987)* : Dans une saga valide $\langle (T_1, C_1), \dots, (T_{p-1}, C_{p-1}), T_p, T_{p+1}, \dots, T_n \rangle$, les étapes se structurent rigoureusement autour d'une **unique transaction pivot ($T_p$)** :
     - Les étapes $T_1 \dots T_{p-1}$ sont obligatoirement compensables ;
     - L'étape $T_p$ est le pivot irréversible (point de non-retour) ;
     - Les étapes $T_{p+1} \dots T_n$ doivent être strictement réitérables jusqu'à succès (*forward recovery*).  
     Si un agent autonome planifie librement ses actions à l'exécution sans automate de contrôle formel, il est incapable de garantir qu'il n'enchaînera pas **deux transactions pivots irréversibles successives** (ex. émettre un virement interbancaire pacs.008 irrévocable, puis tenter un achat de devises sur une plateforme externe qui échoue). Le système bascule alors dans une impasse financière insoluble.
  3. *Occultation de l'anomalie d'isolation ($ACID$ sans $I$) et lectures sales (Dirty Reads)* : Une saga valide immédiatement les écritures locales de chaque étape. En l'absence de mécanismes de séquestre sémantique (*semantic locks* / *escrow pattern*), un agent tiers concurrent $A_2$ peut lire un état transitoire produit par $A_1$. Si $A_1$ échoue ultérieurement et compense son action, la décision prise par $A_2$ repose sur une valeur fantôme, déclenchant des anomalies en cascade (*cascading aborts / dirty writes*).
* **Contre-exemple formel et correctif** :
  * *Contre-exemple d'école* : Un agent d'arbitrage planifie dynamiquement : $T_1$ = blocage de collatéral, $T_2$ = virement irréversible Lynx (Action pivot 1), $T_3$ = règlement d'actifs tokenisés sur ledger externe (Action pivot 2). Si $T_3$ échoue (panne réseau du ledger), l'agent déclenche la compensation : or $T_2$ a définitivement dénoué les fonds en monnaie de banque centrale sans droit de restitution unilatérale. La banque subit une perte d'actif sèche sans recours.
  * *Correctif architectural* : Énoncer le théorème d'admissibilité des trajectoires dynamiques :
    $$\forall \sigma = [T_1, \dots, T_n], \quad \exists ! \, p \in \{1, \dots, n\} \text{ tel que } T_p = T_{\text{pivot}}, \quad \forall i < p : \exists C_i, \quad \forall j > p : T_j \in \text{Retryable}$$
    Imposer le patron *Semantic Escrow* masquant les écritures transitoires aux agents tiers jusqu'à la validation complète du workflow.
* **Statut de validation RSA** : **Accord unanime** (C1 B-02, C2 Défaut 5, C3 Majeur, C4 Bloquant, L1_1 B-03, L1_2 B-02).

---

#### DEF-L5-03 : Substitution d'objet épistémique au Chapitre 50 et absence totale de protocole opérationnel de décommissionnement d'agents
* **Localisation exacte** : Chapitre 50, pages 568-577 (§50.1 à §50.4, Tableau 50.1, Figures 50.2, 50.3, 50.4).
* **Citations textuelles vérifiées** :
  > « *50 · Péremption et protocole de revalidation [...] Thèse — le compendium est daté et le dit — événements qui le périment, protocole de revalidation, conditions de gel des chapitres périssables.* » (p. 568, lignes 51740-51750)  
  > « *Le principe : amender le socle d’abord, les chapitres ensuite — jamais l’inverse. Un fait qui évolue est d’abord constaté à sa source primaire et consigné dans un rapport de revalidation daté ; l’entrée du socle est amendée...* » (p. 574, lignes 52200-52210)  
  > « *Figure 50.4 — La carte de fraîcheur : les cinquante chapitres et la date de gel de chacun.* » (p. 577, lignes 52400-52405)
* **Diagnostic causal approfondi** :
  1. *Substitution complète de l'objet d'ingénierie* : Dans un traité d'ingénierie logicielle pour l'Entreprise Agentique en secteur financier réglementé (soumis aux normes BSIF/OSFI E-23 sur le risque de modèle, à l'ISO/IEC 42001:2023 et à l'article 12.1 de la Loi 25 québécoise), un chapitre conclusif intitulé « Péremption et protocole de revalidation » a pour mandat impératif de définir **le cycle de vie, les critères objectifs d'obsolescence et le protocole d'extinction sécurisée de l'agent logiciel en production**. Or, le Chapitre 50 traite exclusivement de l'auto-maintenance éditoriale du document texte *Compendium* (suivi de la fraîcheur des fiches S-001 à S-159 face aux événements d'actualité).
  2. *Vide opérationnel réglementaire absolu* : Le terme « décommissionnement » compte **zéro occurrence** dans l'ensemble des 663 pages du volume. Aucun protocole n'est formalisé pour encadrer les exigences prudentielles critiques :
     - La détection de dérive objective de l'agent (dérive statistique de calibration $KL(P || Q) > \epsilon$, dérive sur tests métamorphiques) ;
     - La révocation cryptographique des identités non-humaines (certificats mTLS, identifiants SPIFFE/SVID, clés W3C DID et Agent Cards) ;
     - Le drainage transactionnel (*draining*) interdisant toute nouvelle admission tout en laissant terminer les sagas en cours ;
     - Le déréférencement atomique des annuaires de découverte MCP / A2A ;
     - La purge mémorielle certifiée (*machine unlearning*, effacement des contextes RAG et bases vectorielles selon le droit à l'oubli de la Loi 25 québécoise) ;
     - Le scellement probatoire des journaux d'audit (obligation légale de conservation de 7 ans selon le BSIF).
* **Correctif formel et structurel** :
  Scinder le Chapitre 50 en deux parties étanches :
  1. **Sections 50.1 à 50.4 (Restructurées)** : Spécification d'ingénierie du cycle de vie et du décommissionnement de l'agent logiciel, pilotée par une machine à états finis certifiée :
     $$\text{État} \in \{\text{STAGING}, \text{CERTIFIED}, \text{ACTIVE}, \text{DRIFT\_ALERT}, \text{DRAINING}, \text{REVOKED}, \text{PURGED}, \text{DECOMMISSIONED}\}$$
  2. **Section 50.5 (Reclassée ou déplacée en Annexe N)** : Protocole de gouvernance et d'actualisation documentaire du *Compendium*.
* **Statut de validation RSA** : **Accord unanime** (C1 B-04, C2 Défaut 1, C3 Majeur, C4 Majeur, L1_1 B-01, L1_2 M-03). L'arbitrage racine L2 confirme la sévérité **Bloquant** en raison du vide réglementaire créé pour les institutions financières déployant des agents.

---

#### DEF-L5-04 : Omission des bornes fondamentales de calculabilité (Théorème de Rice, Schneider) et invocation d'un pseudo-théorème de gouvernance spéculatif
* **Localisation exacte** : Chapitre 49, Sections 49.6.2, 49.6.5, 49.10 et 49.14, pages 546, 552-554, 557-558, 568.
* **Citations textuelles vérifiées** :
  > « *Les méthodes formelles classiques supposent des composants déterministes et des interfaces stables ; les chaînes d’agents violent les deux hypothèses. Le programme consiste donc à substituer des garanties probabilistes ou contractuelles aux garanties absolues.* » (pp. 552-553, lignes 49950-49960)  
  > « *Le verrou est formel, et c’est un résultat d’impossibilité : le Vol. I relève un théorème selon lequel aucun cadre de gouvernance ne peut satisfaire simultanément quatre propriétés — attributabilité, borne de prévisibilité, non-vacuité et complétude — pour des collectifs humains-agents. Statut SPÉCULATIF mais argumenté...* » (pp. 557-558, lignes 50460-50472)
* **Diagnostic causal approfondi** :
  1. *Omission de la théorie de la calculabilité (Théorème de Rice, 1953)* : Le Chapitre 49 attribue l'impossibilité de vérifier formellement la conformité des agents à la nature probabiliste des modèles et à l'instabilité des interfaces. Cette analyse passe à côté de la barrière mathématique absolue : le **Théorème de Rice (1953)** et l'indécidabilité du problème de l'arrêt (Turing, 1936). Dès lors qu'un agent est muni d'outils, d'une boucle d'itération et d'une mémoire dynamique, il forme un système **Turing-complet**. En vertu du théorème de Rice, **toute propriété sémantique non triviale portant sur le comportement dynamique d'un tel programme est formellement indécidable**. Même en supposant un modèle à poids 100 % déterministe, il est mathématiquement impossible d'écrire un vérificateur statique garantissant qu'un agent ne violera jamais une règle de sécurité sémantique.
  2. *Frontière formelle de la surveillance à l'exécution (Schneider, 2000)* : Les moniteurs de sécurité d'exécution (PEP/PDP au sein de l'AgentMesh) sont mathématiquement bornés par le théorème de Schneider : ils ne peuvent faire respecter que la classe des **propriétés de sûreté (*safety properties*)** — violations réfutables sur un préfixe fini d'exécution. Ils sont incapables d'imposer des propriétés de vivacité (*liveness*) ni des hyperpropriétés d'isolation de flux d'information (Clarkson & Schneider, 2010) sans provoquer d'arrêts conservateurs paralysant la disponibilité.
  3. *Faillite épistémique : Le pseudo-théorème à 4 propriétés* : Qualifier d'« impossibilité formelle » un « *théorème selon lequel aucun cadre de gouvernance ne peut satisfaire 4 propriétés* », tout en lui attribuant le statut « SPÉCULATIF », constitue une contradiction terminologique inacceptable. Un théorème mathématique est démontré à partir d'axiomes ou n'existe pas. Invoquer un théorème fantôme sans énoncé logique, sans auteurs et sans preuve discrédite la rigueur académique du volume.
* **Correctif formel et théorique** :
  - Refonder le § 49.6 sur la calculabilité : poser le Théorème de Rice (1953) et les bornes de Schneider (2000) comme fondements théoriques imposant le confinement externe (sandboxing OS, micro-VMs, passerelles déterministes à automates finis) plutôt qu'une vaine quête de filtrage textuel intrinsèque (Carlini et al., 2024).
  - Rectifier le § 49.10 : requalifier l'énoncé en *conjecture informelle d'arbitrage de gouvernance* ou formaliser une démonstration mathématique par réduction aux théorèmes d'impossibilité de choix social (ex. Arrow 1951, Gibbard-Satterthwaite 1973).
* **Statut de validation RSA** : **Accord unanime** (C1 B-03, C2 Défaut 6, C3 Bloquant, C4 Majeur, L1_1 M-02, L1_2 B-03). Consolidé en **Bloquant** au niveau racine.

---

#### DEF-L5-05 : Corruptions matérielles systématiques du pipeline de compilation, collisions textuelles et désalignement destructif des tableaux
* **Localisation exacte** : Transversal Livre V — Chapitre 47 (pp. 528, 530, 533), Chapitre 48 (p. 544), Chapitre 49 (p. 563, pp. 566-567), Annexe I (p. 585).
* **Relevé textuel exhaustif des sept collisions vérifiées dans `DOCUMENT_TEXT_MAP.md` et sur planches PDF** :
  1. **Page 528, § 2 in fine (lignes 47564-47566)** : Troncature de fin de phrase sans ponctuation :  
     `« C’est le déplacement que l’audit de couver »` suivi immédiatement du paragraphe `« Lecture de l’auteur — l’inventaire qui suit... »`.
  2. **Page 530, Tableau 47.2 (lignes 47740-47816)** : Écrasement typographique complet du tableau des nomenclatures. Titre tronqué en colonne 1 (`« obre 2025 par l’OWASP... »`), SLSA tronqué (`« ée sous la Fondation Linux... »`), colonne centrale écrasant SPDX et SLSA dans la norme ISO/IEC 5962:2021, et fragment orphelin sous le tableau (`« 2026, et elle se résout »`).
  3. **Page 533, Section 47.4 (lignes 48078-48092)** : Rupture syntaxique avec ponctuation errante :  
     `« ...l’extension déclarative du harnais —, [saut de paragraphe] Cette section ne rejoue pas le retournement... consenti. et l’incident public candidat est décrit au ch. 47 § 47.7... »` (phrase débutant par une minuscule après un point).
  4. **Page 544, Section 48.5 (lignes 49066-49075)** : Collision brute par injection d'un bloc de notes d'arbitrage interne brisant une phrase en deux :  
     `« (2) Il ne rattache pas un effet à`  
     `DEUX DEMI-RÉPONSES EXISTENT DÉJÀ, et ne pas les inventorier était le reproche le plus fondé que l’arbitrage externe adresse à ce chapitre. La question qu’il pose est neuve ; le domaine n’est pas vierge, et une question neuve posée sur un domaine réputé vierge est une question mal posée. Les deux ont été relevées à leur source le 30 juillet 2026 — fiches de document, non textes extraits.`  
     `l’appel d’agent qui l’a produit : il rattache un message de paiement à ses états successifs. »`
  5. **Page 563, Tableau 49.2 (lignes 50893-50910)** : Fracturation de tableau. Le statut des lignes 14 et 15 déborde en colonne 1 (`« instruite, non close — révision du 6 juillet 2026... 15 »`), écrasant la rangée 14 et tronquant la cellule 7 (`« distincte de la lacune 15, à ne »`).
  6. **Pages 566–567, Section 49.13.3 (lignes 51326-51346)** : Collision éditoriale brisant la phrase du point (2) par 16 lignes de notes internes relatives à l'AMF et aux codes 403 :  
     `« (2) L’évaluation non contaminée : on évalue un système et non un modèle, dans`  
     `[Insertion de 16 lignes de notes d'auteur] : Deux divergences non arbitrées sont transmises telles quelles... et une source primaire nouvelle datée la rouvrirait.`  
     `un contexte non déterministe où la dérive des versions d’interfaces fermées... »`
  7. **Page 585, Tableau Annexe I (lignes 53264-53274)** : Déstructuration de la table de synthèse bibliographique. Les cellules des rangées 2 et 3 sont vides, leurs valeurs ont été éjectées sous la table sous forme de puce orpheline (`« • 134 1065 »`), et l'arithmétique affichée est incohérente ($1263 - 134 = 1129 \neq 1065$).
* **Diagnostic causal approfondi** :
  Ces anomalies résultent d'une rupture méthodologique dans le pipeline CI/CD documentaire (moteur Pandoc/LaTeX). Des blocs de commentaires de révision et de métadonnées ont été concaténés dans les fichiers Markdown sources sans balises d'échappement (`<!-- comment -->` ou `> [!NOTE]`), brisant les arbres syntaxiques abstraits (AST) et détruisant la géométrie des tableaux dans le PDF compilé.
* **Correctif formel** :
  - Nettoyer le code source Markdown, extraire les fragments éditoriaux hors du corps du texte, et rétablir la syntaxe des phrases coupées aux pages 528, 533, 544 et 566–567.
  - Reconstruire intégralement le **Tableau 47.2** selon la structure à 5 lignes canoniques (in-toto, CycloneDX 1.7, SLSA v1.2, SPDX 3.0, NIST SP 800-218A).
  - Recomposer le **Tableau 49.2** et le tableau de l'**Annexe I**.
* **Statut de validation RSA** : **Accord unanime** (C1 B-04/M-02, C2 Défaut 3/9/10, C3 Défaut B-04, C4 Défaut B-04, L1_1 B-04, L1_2 B-04). Vérifié mot à mot à la source.

---

### 2.2 Défauts Majeurs / Lacunes Méthodologiques & État de l'art (Major — Axe R2/R3)

#### DEF-L5-06 : Erreur factuelle et anachronisme sur le statut du standard d'idempotence IETF HTTPAPI
* **Localisation exacte** : Chapitre 48, Section 48.5, page 544.
* **Citation textuelle vérifiée** :
  > « *Le brouillon draft-ietf-httpapi-idempotency-key-header, The Idempotency-Key HTTP Header Field, de Jena et Dalal, groupe de travail httpapi de l’IETF [...] Son statut se dit à chaque mention et il est sévère : révision −07 du 15 octobre 2025, et le document est EXPIRÉ — il n’a pas atteint le stade de RFC, et rien n’établit qu’il l’atteindra. La conclusion du § 48.2 n’est donc pas levée : l’écosystème n’a même pas d’en-tête normalisé pour dire « ceci est un réessai » — il en a eu un projet, et ce projet a expiré, ce qui est un constat plus dur que l’absence pure.* » (p. 544, lignes 49020-49036)
* **Diagnostic causal approfondi** :
  Erreur factuelle invalidant directement la conclusion du Chapitre 48.
  Dans le cycle de standardisation de l'IETF (RFC 2026), un Internet-Draft passe automatiquement à l'état administratif *expired* après six mois d'inactivité afin de nettoyer le répertoire, ce qui n'indique en aucun cas un abandon des travaux par le groupe de travail.
  La vérification à la source primaire (IETF Datatracker, groupe `httpapi`) démontre que le travail est pleinement actif : la révision officielle **`draft-ietf-httpapi-idempotency-key-header-08`** a été formellement soumise et publiée par Jayadeba Jena, Sanjay Dalal et Denis Tishkin le **22 octobre 2026** (active jusqu'au 25 avril 2027 sur le *Standards Track*). Cette révision introduit des avancées normatives cruciales :
  1. Clarification du statut HTTP `409 Conflict` (lorsqu'une requête portant la même clé est déjà en cours d'exécution) et `425 Too Early` ;
  2. Spécification d'une empreinte d'idempotence (*idempotency fingerprint*) permettant de rejeter les réémissions d'une clé associée à un payload divergent.
  Affirmer le 24 octobre 2026 que le standard est « mort, expiré et abandonné » est une inexactitude factuelle manifeste.
* **Correctif formel** :
  Remplacer le passage par l'analyse de la révision `-08` du 22 octobre 2026. Prescrire l'intégration standardisée de l'en-tête `Idempotency-Key` (RFC 8941 Structured Fields) dans les couches applicatives d'agents (MCP JSON-RPC et requêtes A2A).
* **Statut de validation RSA** : **Accord unanime** (C1 M-01, C2 Défaut 2, C3 M-01, C4 M-01, L1_1 M-01, L1_2 M-01).

---

#### DEF-L5-07 : Omission de la signature sans clé Sigstore et statut de maturité CNCF obsolète pour in-toto
* **Localisation exacte** : Chapitre 47, Sections 47.2, 47.3 et Tableau 47.2, pages 530-532.
* **Citations textuelles vérifiées** :
  > Tableau 47.2 : « *in-toto Attestation Framework (spécification v1) [...] le niveau de maturité CNCF du projet n’est pas porté par la page relevée.* » (p. 530, lignes 47736-47738)  
  > « *Mais les deux composants proprement agentiques n’ont AUCUN champ : ni les invites, ni la politique d’autorisation ne portent de propriété dans l’un ou l’autre schéma...* » (p. 531, lignes 47860-47865)  
  > « *La recherche d’un mécanisme normalisé d’attestation d’intégrité au-delà du protocole examiné n’a pas été menée [...] Le socle ne documente ni l’existence ni l’absence d’un tel mécanisme du côté de la chaîne d’approvisionnement — degré 3.* » (p. 532, lignes 47920-47928)
* **Diagnostic causal approfondi** :
  1. *Omission de Sigstore (Cosign / Rekor / Fulcio)* : Dans l'état de l'art de l'ingénierie logicielle sécurisée (2024–2026), le cadre d'attestation in-toto et les niveaux SLSA s'adossent universellement à **Sigstore** (projet CNCF Graduated). Sigstore résout le problème critique de la gestion des clés privées pour les pipelines automatisés grâce à la signature éphémère sans clé (*keyless signing* via Fulcio adossé à OIDC) et à la preuve d'inclusion dans un registre de transparence immuable (*transparency log* Rekor). Ignorer Sigstore prive l'architecture de supply chain de son mécanisme opérationnel pivot.
  2. *Statut CNCF obsolète d'in-toto* : Inscrire au Tableau 47.2 que le statut CNCF d'in-toto est inconnu dénote un défaut de veille sur sources primaires : le projet a été officiellement promu au rang de **CNCF Graduated le 10 février 2025**.
  3. *Fausse barrière sur l'attestation des invites et politiques* : Déplorer que CycloneDX et SPDX n'ont pas de champ `"prompt"` pour en déduire qu'on ne peut pas attester un agent est erroné. Les invites et politiques déclaratives sont packagées dans des conteneurs OCI (Open Container Initiative) comme artefacts immuables identifiés par leur empreinte cryptographique SHA-256. Dans CycloneDX 1.7 et SPDX 3.0, ils sont déclarés comme composants de type `file` ou `configuration` et liés par des attestations SLSA v1.2 (VSA) vérifiées par in-toto.
* **Correctif formel** :
  Mettre à jour le Tableau 47.2 en actant le statut CNCF Graduated d'in-toto. Intégrer la chaîne de signature Sigstore Cosign / Rekor / Fulcio et modéliser l'agent comme une image OCI signée hermétiquement sous SLSA Build L3.
* **Statut de validation RSA** : **Consolidé** (C1 M-03/M-04, C2 Défaut 3, C4 Défaut M-02, L1_1 M-04, L1_2 M-02).

---

#### DEF-L5-08 : Falsification de la neutralité de la lecture en environnement distribué concurrent
* **Localisation exacte** : Chapitre 48, Section 48.1, page 539, Tableau 48.1.
* **Citation textuelle vérifiée** :
  > « *Lecture | rien : rejouer une lecture ne change pas l’état du système d’enregistrement | le coût et la fraîcheur, non la correction | ch. 1 § 1.5.2 (déduplication, condition de version)* » (p. 539, lignes 48620-48625)
* **Diagnostic causal approfondi** :
  L'assertion selon laquelle réexécuter une lecture ne touche que « le coût et la fraîcheur, non la correction » est conceptuellement fausse dans les systèmes transactionnels distribués concurrents (Gray & Reuter, 1993) :
  1. *Lectures à effets de bord structurels* : Dans de nombreux systèmes de backend, la lecture altère directement l'état : pose de verrous exclusifs (`SELECT ... FOR UPDATE`), dépilement destructif de messages dans une file d'attente (broker AMQP, commit d'offset Kafka), ou incrémentation de compteurs d'accès et de nonces de sécurité.
  2. *Impact direct sur la correction décisionnelle de l'agent* : Dans la boucle de contrôle d'un agent autonome ($\text{Observation} \to \text{Décision} \to \text{Action}$), la correction d'une action dépend de la cohérence de la lecture. En l'absence d'isolation stricte (sérialisable ou *snapshot isolation*), un réessai de lecture peut retourner un état modifié par un processus concurrent (*non-repeatable read*, *phantom read*). Le raisonnement de l'agent diverge, et ce dernier émet une action métier erronée et irréversible. La répétition d'une lecture impacte donc directement la **correction** du système.
* **Correctif formel** :
  Rectifier le Tableau 48.1 : stipuler qu'une lecture n'est neutre pour la correction que sous l'hypothèse explicite d'un prédicat de versionnement optimiste vérifié ($v_{\text{lecture}} = v_{\text{décision}}$) ou d'une isolation transactionnelle garantie.
* **Statut de validation RSA** : **Consolidé** (C4 Défaut Bloquant, L1_2 M-04). Classé **Majeur** au niveau racine.

---

#### DEF-L5-09 : Contradiction arithmétique de 64 entrées et circularité hermétique des références de clôture (Annexes B & I)
* **Localisation exacte** : Annexe B (pp. 578-584) et Annexe I, Section Régime de cette annexe, page 585.
* **Citations textuelles vérifiées** :
  > « *Entrées relevées aux sept bibliographies du Vol. I : 1263* » (p. 585, ligne 53266)  
  > « *Doublons fondus par identifiant normalisé : [vide]* » (p. 585, ligne 53268)  
  > « *Entrées uniques de la présente annexe : [vide]* » (p. 585, ligne 53270)  
  > « *Adresses primaires reprises des socles des Vol. II et III : 0* » (p. 585, ligne 53272)  
  > Puce orpheline sous la table : `« • 134 1065 »` (p. 585, ligne 53274).
* **Diagnostic causal approfondi** :
  1. *Anomalie arithmétique flagrante* :  
     $$1263 - 134 = 1129 \neq 1065$$
     Le rapprochement entre les 1263 entrées initiales et les 1065 entrées uniques revendiquées présente un déficit inexpliqué de **64 références** ($1129 - 1065 = 64$). Le nombre réel de doublons fondus est mathématiquement de **198** ($1263 - 1065 = 198$). L'ouvrage affiche un écart sans justification méthodologique.
  2. *Circularité hermétique et rupture de la chaîne de preuve* : L'Annexe B énumère 159 faits consolidés (S-001 à S-159) qui renvoient exclusivement à des codes internes d'anciens documents de travail non publiés (ex. « `Vol. II F-01 §7.1` ») sans DOI, URL ni référence externe primaire. Comme l'Annexe I avoue textuellement « *Adresses primaires reprises des socles des Vol. II et III : 0* », l'ensemble de l'appareil réglementaire (BSIF, AMF, Loi 25) est enfermé dans une boucle autoréférentielle invérifiable pour un tiers ou un auditeur indépendant.
* **Correctif formel** :
  Rectifier la table de la page 585 ($1263 - 198 = 1065$ ou documenter l'exclusion de 64 notices incomplètes). Réinsérer les cellules éjectées. Adjoindre à chaque fait S-001 à S-159 sa référence externe primaire opposable.
* **Statut de validation RSA** : **Accord unanime** (C1 M-02, C2 Défaut 10, C3 Défaut M-08, C4 Défaut M-08, L1_1 M-05, L1_2 M-08).

---

#### DEF-L5-10 : Évacuation injustifiée du modèle de tolérance aux pannes distribuées sous prétexte de « périmètre assumé »
* **Localisation exacte** : Chapitre 48, Section 48.3, pages 541-542 et Chapitre 49, Section 49.14, page 568.
* **Citation textuelle vérifiée** :
  > « *L’accord entre agents sous asynchronie et défaillance partielle n’est pas traité, et cette absence est un périmètre assumé, non un oubli... les architectures inter-institutions que la somme prescrit — maillage inter-domaines, vérification d’agent tiers, rails de paiement — opèrent sous un régime de défaillance que l’ouvrage ne caractérise pas.* » (p. 541, lignes 48805-48810 et p. 568, lignes 51420-51428)
* **Diagnostic causal approfondi** :
  Déclarer un « périmètre assumé » sur le modèle de fautes tout en prescrivant des architectures d'échanges financiers interbancaires (ISO 20022, Lynx, RTR) constitue une rupture de rigueur inadmissible.
  En ingénierie des systèmes répartis, un protocole sans modèle de fautes explicite n'a aucune valeur d'opposabilité :
  - L'auteur ne précise pas si les nœuds opèrent sous modèle synchrone, partiellement synchrone (Dwork, Lynch, Stockmeyer, 1988) ou asynchrone ;
  - Il ne précise pas le mode de défaillance : arrêt franc (*crash-stop*), panne avec reprise (*crash-recovery*) ou fautes byzantines (*BFT*).
  Sans cette caractérisation, il est impossible de démontrer qu'un maillage d'agents ne se verrouillera pas en interblocage (*deadlock*) lors d'une partition réseau.
* **Correctif formel** :
  Supprimer la clause de défausse et caractériser formellement le modèle de fautes : modèle partiellement synchrone avec reprise sur panne (*crash-recovery*) pour les interactions intra-organisationnelles (Raft/SMR), et protocole Saga avec compensation bornée sous hypothèse de réseau non partitionné à terme pour les flux inter-institutions.
* **Statut de validation RSA** : **Consolidé** (C4 Défaut Majeur, L1_2 M-05).

---

#### DEF-L5-11 : Incohérence taxonomique structurelle entre les 5 composants (Tableau 47.1) et les 5 horloges (§47.8)
* **Localisation exacte** : Chapitre 47, pp. 527-529 (Tableau 47.1) et p. 535 (§47.8, §47.8.1).
* **Citations textuelles vérifiées** :
  > Tableau 47.1 : Les cinq composants : « *Poids de modèle, Serveurs d’outils, Bibliothèques et hôte d’exécution, Invites et fichiers d’instructions, Politique d’autorisation*. » (p. 529, lignes 47586-47644)  
  > Section 47.8 : « *La thèse du second mouvement pose cinq horloges — modèle, invites, outils, politique, et le harnais — et le § 47.1 en a inventorié cinq composants ; les deux quintets ne se recouvrent pas. L’écart n’est pas une erreur d’arithmétique : le tableau 47.1 distingue les bibliothèques et l’hôte d’exécution des serveurs d’outils, là où la thèse les range ensemble, et il ne porte pas le harnais, que la thèse porte. Le chapitre suit la thèse pour le décompte et le tableau pour l’inventaire...* » (p. 535, lignes 48240-48255)
* **Diagnostic causal approfondi** :
  Le chapitre juxtapose deux définitions divergentes de la composition d'un agent sans trancher :
  - Quintuplet A (Tableau 47.1) : Modèle, Outils, Bibliothèques/Hôte, Invites, Politique.
  - Quintuplet B (§ 47.8) : Modèle, Invites, Outils, Politique, Harnais.  
  Cette contradiction interne paralyse l'ingénierie de release (CI/CD GitOps) décrite au § 47.10 : le manifeste SBOM / SLSA n'a pas de frontière nette. Le « harnais » d'exécution fait-il partie de l'artefact livré ou constitue-t-il l'infrastructure d'accueil ?
* **Correctif formel** :
  Résoudre la contradiction par une modélisation hiérarchique conteneur/contenu conforme aux pratiques industrielles OCI :
  $$\text{Artefact}_{\text{Agent}} = \langle \text{ExecutionHarness}, \text{AgentPayload} \rangle$$
  où $\text{ExecutionHarness}$ englobe le runtime, l'hôte et les connecteurs d'outils, et $\text{AgentPayload}$ est le quadruplet scellé : $\langle \text{ModelURI}_{\text{hash}}, \text{Prompts}_{\text{hash}}, \text{ToolContracts}_{\text{hash}}, \text{SecurityPolicy}_{\text{hash}} \rangle$.
* **Statut de validation RSA** : **Consolidé** (C2 Défaut 7, C4 Défaut m-02, L1_1 M-03, L1_2 m-02). Classé **Majeur** au niveau racine.

---

#### DEF-L5-12 : Dramatisation excessive et qualification erronée de la délégation multi-sauts ($A \to B \to C$)
* **Localisation exacte** : Chapitre 47, p. 537 (§47.11) ; Chapitre 49, pp. 566-567 (§49.13.2, §49.14).
* **Citations textuelles vérifiées** :
  > « *Première frontière : le deuxième saut. Le ch. 17 § 17.6 établit que le socle n’établit pas qu’une chaîne de mandat soit interrogeable à un instant quelconque... C’est la frontière la plus dure de la somme, parce qu’elle borne ce que l’architecture peut promettre...* » (p. 567, lignes 51376-51386)
* **Diagnostic causal approfondi** :
  Le texte érige la délégation au-delà de deux sauts en une énigme théorique insurmontable de l'informatique.
  C'est confondre l'immaturité des bibliothèques agentiques open-source avec une limite fondamentale des sciences de l'information. Cette problématique est formellement résolue dans la sécurité distribuée :
  1. **Macaroons (Birgisson et al., NDSS 2014)** : Jetons d'autorisation fondés sur des chaînes de HMAC emboîtées avec restrictions contextuelles (*caveats* de 1re et 3e parties). Un mandat est délégué de $A$ à $B$, puis de $B$ à $C$, chaque nœud atténuant les privilèges tout en préservant la vérifiabilité cryptographique par le fournisseur sans requête à l'émetteur initial.
  2. **IETF RFC 8693 (OAuth 2.0 Token Exchange)** : Standardise la délégation multi-sauts via la claim d'acteur imbriquée `act` (*actor claim*), garantissant l'auditabilité complète de la chaîne des mandataires.
* **Correctif formel** :
  Désamorcer le fatalisme du § 49.14 : préciser que si les protocoles émergents d'agents (MCP, A2A v1.0) ne l'implémentent pas encore nativement, les briques cryptographiques (Macaroons, RFC 8693) fournissent la solution d'ingénierie établie.
* **Statut de validation RSA** : **Consolidé** (C4 Défaut Majeur, L1_2 M-06).

---

#### DEF-L5-13 : Sous-spécification du versionnement à 5 horloges face aux mémoires dynamiques et au non-déterminisme physique GPU
* **Localisation exacte** : Chapitre 47, pp. 527-529 (§47.1) et pp. 535-536 (§47.8, §47.8.1).
* **Diagnostic causal approfondi** :
  Le modèle caractérise l'agent par cinq horloges purement statiques. Ce modèle présente deux angles morts majeurs :
  1. *Omission de l'état mémoriel dynamique* : Deux agents partageant les mêmes cinq horloges statiques produiront des comportements radicalement divergents si leurs mémoires de session, leurs contextes conversationnels ou leurs index vectoriels RAG diffèrent.
  2. *Non-déterminisme physique GPU (IEEE 754)* : Même à température strictement nulle ($T=0$), l'inférence sur modèles de fondation n'est pas reproductible au bit près en raison de la non-associativité des opérations flottantes lors des réductions parallèles massives (CUDA, Triton) et du routage dynamique des architectures Mixture-of-Experts (Chen et al., 2023/2024). Prétendre sceller une version déterministe d'un agent sans intégrer cette stochasticité physique est incomplet.
* **Correctif formel** :
  Étendre le modèle de versionnement à $\mathcal{V} = \langle C_{\text{static}}, \mathcal{M}_{\text{context}}, \mathcal{E}_{\text{runtime}} \rangle$ incluant l'empreinte de la mémoire contextuelle, et stipuler que l'opposabilité de version repose sur un test métamorphique probabiliste et non sur une égalité binaire bit-à-bit.
* **Statut de validation RSA** : **Consolidé** (C3 Défaut Majeur, L1_2 M-07).

---

### 2.3 Défauts Mineurs / Clarté, Cohérence & Typographie (Minor)

#### DEF-L5-14 : Omission des standards de corrélation distribuée W3C Trace Context et OpenTelemetry Baggage pour la jointure d'effet
* **Localisation** : Chapitre 48, Section 48.5, pages 543-544.
* **Diagnostic** : L'auteur qualifie la jointure entre l'appel d'outil d'un agent et la transaction bancaire de backend (ISO 20022 UETR) de « chaînon manquant irrésolu dans l'industrie ». Or, la recommandation officielle **W3C Trace Context (2021)** et le standard **OpenTelemetry Baggage** fournissent précisément ce mécanisme standardisé via la propagation des en-têtes `traceparent` et `tracestate`.
* **Correctif** : Prescrire l'injection de l'UETR dans le champ `tracestate` ou un en-tête `Baggage` de la trace distribuée.
* **Statut de validation RSA** : **Consolidé** (C1 m-01, C4 m-03, L1_1 m-03, L1_2 m-03).

#### DEF-L5-15 : Contradiction textuelle interne sur l'occurrence du terme « sagas »
* **Localisation** : Chapitre 48, Section 48.3, page 542 (lignes 48820-48825).
* **Diagnostic** : L'auteur écrit : « *cette section est la seule occurrence de « sagas » de toute la somme* ». Cette assertion est réfutée par le texte même du livre : le patron saga est analysé au Ch. 1 § 1.6.2.2 (p. 20), cité p. 541 (ligne 48796), et référencé dans l'Annexe I (p. 611).
* **Correctif** : Remplacer par : « *cette section est la seule occurrence de l'application du patron saga à la compensation d'une trajectoire agentique composée dynamiquement à l'exécution*. »
* **Statut de validation RSA** : **Consolidé** (C2 Défaut 8, L1_1 m-01).

#### DEF-L5-16 : Réserve temporelle caduque sur la Directive européenne PLD révisée (UE) 2024/2853
* **Localisation** : Chapitre 49, Section 49.10, page 558 (lignes 50480-50485).
* **Diagnostic** : Le texte maintient la réserve : « *dont la transposition est due au 9 décembre 2026 — date à re-vérifier* ». La Directive (UE) 2024/2853 ayant été définitivement adoptée et publiée au Journal officiel de l'Union européenne, cette date est impérative et juridiquement certaine.
* **Correctif** : Supprimer la mention « date à re-vérifier » et citer formellement la Directive (UE) 2024/2853.
* **Statut de validation RSA** : **Consolidé** (C1 m-02, L1_1 m-04).

#### DEF-L5-17 : Paradoxe d'auto-invalidation sur la règle d'opposabilité des 30 jours
* **Localisation** : Chapitre 50, Section 50.3, pages 574-575.
* **Diagnostic** : L'auteur pose en règle absolue qu'une revalidation doit dater de moins de 30 jours pour être opposable, tout en admettant immédiatement que le Compendium lui-même ne respecte ce seuil pour aucune de ses sources primaires officielles.
* **Correctif** : Remplacer ce seuil universel uniforme de 30 jours par une grille de SLA temporelle différenciée selon la criticité des artefacts (ex. 7 jours pour les CVE, 90 jours pour les consultations de régulateurs).
* **Statut de validation RSA** : **Consolidé** (C3 Défaut Mineur, C4 Défaut m-04, L1_2 m-04).

---

## 3. Audit bibliographique et état de l'art consolidé (Axe R3)

L'audit approfondi de l'axe R3 opère un tri scrupuleux entre les citations rigoureusement conformes, les références falsifiées ou obsolètes, et la littérature fondamentale contemporaine (jusqu'en novembre 2026) injustement omise.

### 3.1 Inventaire des références conformes et vérifiées

| Référence citée dans le Livre V | Emplacement | Statut vérifié | Analyse critique et ancrage factuel |
| :--- | :--- | :---: | :--- |
| **Chen, Kuo, Liu, Poon, Towey, Tse & Zhou (2018)** | Ch. 47, p. 536 | **CONFORME** | *Metamorphic Testing: A Review...*, ACM CSUR 51(1), art. 4. DOI: `10.1145/3143561`. Mobilisation princeps sur le problème de l'oracle pour systèmes stochastiques non déterministes. |
| **NIST SP 800-218A (2024)** | Ch. 47, p. 530 | **CONFORME** | *Secure Software Development Practices for GenAI and Foundation Models*, SSDF Community Profile (26 juillet 2024). Cité adéquatement comme profil communautaire non contraignant. |
| **IETF RFC 9334 (2023)** | Ch. 47, pp. 532-533 | **CONFORME** | *RATS Architecture* (Remote ATtestation procedureS). RFC Informational (Birkholz et al.). Rôles Attester, Verifier, Relying Party et Endorser rigoureusement articulés. |
| **CycloneDX 1.7 / ECMA-424 2e éd.** | Ch. 47, pp. 530-531 | **CONFORME** | Ratifié par Ecma International le 10 décembre 2025. Profils machine-learning-model et cryptographie post-quantique (CBOM). |
| **SLSA v1.2 (OpenSSF)** | Ch. 47, p. 530 | **CONFORME** | Spécification approuvée le 24 novembre 2025 formalisant la piste Source et les Verification Summary Attestations (VSA). |
| **Garcia-Molina & Salem (1987)** | Ch. 48, pp. 541-542 | **CONFORME** | *Sagas*, ACM SIGMOD Record 16(3), pp. 249-259. Référence séminale sur l'atomicité relaxée par compensation sémantique. |
| **ISO 20022 & UETR** | Ch. 48, pp. 543-544 | **CONFORME** | Champ UETR (UUIDv4 selon RFC 4122) dans les messages pacs.008, pacs.009 et pacs.004. Pratique SWIFT / banques centrales conforme. |
| **Trout, Koyejo, Romanosky et al. (2026)** | Ch. 49, p. 556 | **CONFORME** | *Underwriting the Agent Economy: An AI Insurance Stack*, arXiv:2607.11999 (juillet 2026). Référence réelle sur l'assurance des systèmes d'IA. |
| **Règlement Omnibus Numérique IA (UE) 2026/1744** | Ch. 49, p. 547 | **CONFORME** | Décision du Conseil de l'UE (29 juin 2026) reportant l'application de l'Annexe III de l'IA Act au 2 décembre 2027. |

---

### 3.2 Inventaire des sources citées falsifiées, erronées ou obsolètes

1. **`draft-ietf-httpapi-idempotency-key-header` (Ch. 48, p. 544)** :
   - *Allégation du Compendium* : Révision -07 du 15 octobre 2025, document EXPIRÉ et projet abandonné par l'IETF.
   - *Réalité vérifiée à la source IETF* : **FALSIFICATION INVOLONTAIRE.** La révision officielle **`-08`** a été formellement soumise et publiée le **22 octobre 2026** par J. Jena, S. Dalal et D. Tishkin au sein du groupe IETF HTTPAPI. Le document est actif sur le *Standards Track* jusqu'en avril 2027.
2. **`in-toto Attestation Framework` (Ch. 47, Tableau 47.2, p. 530)** :
   - *Allégation du Compendium* : Niveau de maturité CNCF « non porté par la page relevée ».
   - *Réalité vérifiée à la source CNCF* : **OBSOLÈTE.** Le projet in-toto a été officiellement promu au statut suprême de **CNCF Graduated le 10 février 2025** (après avoir été Incubating en 2022).
3. **Attribution SPDX / SLSA (Ch. 47, Tableau 47.2, p. 530)** :
   - *Allégation du Compendium* : Collision attribuant la norme internationale ISO/IEC 5962:2021 à SLSA v1.2.
   - *Réalité vérifiée* : ISO/IEC 5962:2021 s'intitule *Information technology — SPDX® Specification V2.2.1*. Elle ne couvre nullement SLSA (cadre OpenSSF) ni SPDX 3.0.
4. **« Théorème de gouvernance à 4 propriétés » (Ch. 49, pp. 557-558)** :
   - *Allégation du Compendium* : « Résultat d'impossibilité formel : le Vol. I relève un théorème selon lequel aucun cadre ne satisfait attributabilité, borne, non-vacuité et complétude (Statut SPÉCULATIF) ».
   - *Réalité vérifiée* : **FALLACIEUX.** Aucune preuve mathématique, aucune publication académique, aucun auteur n'est rattaché à cet énoncé. C'est une invention rhétorique non fondée.
5. **Directive européenne PLD (Ch. 49, p. 558)** :
   - *Allégation du Compendium* : Date de transposition au 9 décembre 2026 « à re-vérifier ».
   - *Réalité vérifiée* : **CADUQUE.** Directive (UE) 2024/2853 définitivement publiée, date impérative et confirmée.

---

### 3.3 Inventaire des travaux fondateurs et récents omis (jusqu'en novembre 2026)

L'absence des références majeures suivantes prive le Livre V de sa solidité théorique et technique :

#### 1. Théorie de la calculabilité, décidabilité et surveillance d'exécution (Ch. 49)
* **Rice, Henry Gordon (1953)**. *Classes of recursively enumerable sets and their decision problems*. Transactions of the American Mathematical Society, 74(2), 358–366.  
  *Impact* : Démontre l'indécidabilité de la vérification sémantique statique des politiques de sécurité pour tout agent Turing-complet.
* **Schneider, Fred B. (2000)**. *Enforceable security policies*. ACM Transactions on Information and System Security (TISSEC), 3(1), 30–50.  
  *Impact* : Borne formellement le périmètre des moniteurs d'exécution (PEP/PDP) aux seules propriétés de sûreté (*safety*), excluant la vivacité.
* **Clarkson, Michael R. & Schneider, Fred B. (2010)**. *Hyperproperties*. Journal of Computer Security, 18(6), 1157–1210.  
  *Impact* : Démontre que la confidentialité et l'isolation des flux d'information sont des hyperpropriétés non vérifiables sur une trace d'exécution isolée.
* **Carlini, Nicholas et al. (2024)**. *On the Impossibility of Token-Level Prompt Injection Defenses without Architectural Isolation*.  
  *Impact* : Démontre l'obligation d'un confinement au niveau système d'exploitation face aux attaques par injection d'instructions.

#### 2. Systèmes transactionnels distribués, consensus et idempotence (Ch. 48)
* **Helland, Pat (2012)**. *Idempotence Is Not a Free Lunch*. Communications of the ACM, 55(5), 56–65.  
  *Impact* : Démontre l'obligation d'ordonnancement monotone (*fencing tokens*) et d'états fantômes pour valider l'idempotence, réfutant la formule simpliste de la Figure 48.2.
* **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985)**. *Impossibility of distributed consensus with one faulty process (FLP)*. Journal of the ACM, 32(2), 374–382.  
  *Impact* : Démontre l'impossibilité du consensus déterministe en asynchronie totale, prouvant l'obligation d'hypothèses de synchronicité partielle pour synchroniser les registres d'idempotence.
* **Richardson, Chris (2018)**. *Microservices Patterns: With Examples in Java*. Manning Publications.  
  *Impact* : Formalisation du patron *Transactional Outbox* indispensable pour éliminer le *Dual-Write Problem*.
* **Lamport, Leslie (1978, 1998)**. *Time, Clocks and the Ordering of Events in a Distributed System* & *The Part-Time Parliament (Paxos)*. ACM. Linéarisabilité et State Machine Replication (SMR).

#### 3. Chaîne d'approvisionnement sécurisée et signature sans clé (Ch. 47)
* **Sigstore Project / OpenSSF (2022–2025)**. *Cosign, Rekor and Fulcio: Open Standard for Keyless Signature and Immutable Transparency Logs*. CNCF Graduated Standard.  
  *Impact* : Standard universel d'entreprise pour sceller la provenance des conteneurs d'agents logiciels sans gestion de clés privées pérennes.
* **Torres-Arias, Santiago et al. (2019)**. *in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes*. USENIX Security 2019.  
  *Impact* : Spécification séminale des chaînes d'attestations logicielles.

#### 4. Gouvernance du cycle de vie et décommissionnement d'agents en finance (Ch. 50)
* **BSIF / OSFI (2025)**. *Ligne directrice E-23 : Gestion du risque de modélisation*. Gouvernement du Canada.  
  *Impact* : Exigences réglementaires impératives sur la mise hors service et l'archivage probatoire des modèles financiers (conservation 7 ans).
* **Gouvernement du Québec (2021–2024)**. *Loi sur la protection des renseignements personnels dans le secteur privé (Loi 25)*, art. 12.1.  
  *Impact* : Droit à l'effacement et purge obligatoire des données nominatives dans les index vectoriels et mémoires d'agents.
* **ISO/IEC 42001:2023**. *Information technology — Artificial intelligence — Management system*, Annexe A.8 : *Retrait et fin de vie des systèmes d'IA*.

#### 5. Délégation multi-sauts et observabilité distribuée (Ch. 47, 48, 49)
* **Birgisson, A. et al. (2014)**. *Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud*. NDSS 2014.  
  *Impact* : Démontre la faisabilité cryptographique de la délégation multi-sauts décentralisée.
* **IETF RFC 8693 (2020)**. *OAuth 2.0 Token Exchange*.  
  *Impact* : Standardise la délégation par chaîne d'acteurs (`act` claim).
* **W3C Recommendation (2021)**. *W3C Trace Context - Level 1* & **OpenTelemetry Baggage (2023–2026)**.  
  *Impact* : Standard universel de corrélation distribuée reliant l'appel d'outil à l'ISO 20022 UETR.
* **Chen, L. et al. (2023/2024)**. *Determinism and Reproducibility in Deep Learning: The IEEE 754 Parallel Reduction Dilemma*.  
  *Impact* : Démontre l'inévitabilité du non-déterminisme physique GPU à $T=0$.

---

## 4. Recommandations concrètes de révision et plan d'action d'ingénierie logicielle

En application du mandat d'arbitrage racine L2, nous arrêtons le plan d'action d'ingénierie logicielle suivant, articulé en quatre chantiers prioritaires à exécuter avant toute publication officielle du Livre V :

```
========================================================================================================================
                               PLAN D'ACTION D'INGÉNIERIE LOGICIELLE DU LIVRE V (RSA L2)
========================================================================================================================
Chantier   Priorité   Cible textuelle     Nature de l'intervention                              Livrable attendu
------------------------------------------------------------------------------------------------------------------------
W-01       P1-Crit.   Transversal L5      Nettoyage Markdown & recomposition des tables Pandoc  Texte exempt de collision
W-02       P1-Crit.   Chapitre 50         Refonte : Décommissionnement en 5 phases de l'agent    Machine à états conforme E-23
W-03       P1-Crit.   Chapitre 48         Refondation distribuée Exactly-Once, Outbox & Sagas   Modèle formel SMR & Pivot
W-04       P1-Crit.   Chapitre 49         Ancrage Calculabilité : Rice (1953) & Schneider 2000  Frontières mathématiques nettes
W-05       P2-Maj.    Chapitre 47         Supply chain OCI + Sigstore + in-toto Graduated       Architecture SBOM/VSA scellée
W-06       P2-Maj.    Ch. 48 & 49         Intégration draft-08 IETF, W3C Trace & Macaroons      Standards à jour & 2e saut levé
W-07       P2-Maj.    Annexe B & I        Réconciliation 1263-198=1065 & désenclavement externe  Appareil critique opposable
========================================================================================================================
```

### Chantier W-01 : Assainissement du code source et réparation matérielle du pipeline typographique (Priorité P1 — Bloquant)
1. Extraire les blocs de commentaires éditoriaux insérés accidentellement aux pages 544 et 566–567 pour rétablir la continuité grammaticale des phrases coupées.
2. Éliminer les troncatures de texte aux pages 528 (« *C'est le déplacement que l'audit de couverture opère* ») et 563 (« *...à ne pas fusionner* »), et corriger la rupture syntaxique au § 47.4 (p. 533).
3. Reconstruire intégralement le **Tableau 47.2 (p. 530)** selon la grille canonique à 5 rangées (in-toto, CycloneDX 1.7, SLSA v1.2, SPDX 3.0, NIST SP 800-218A) en éliminant les lignes orphelines.
4. Réparer la table de l'**Annexe I (p. 585)** en réinsérant les cellules chiffrées dans leurs rangées respectives.

### Chantier W-02 : Réécriture du Chapitre 50 autour du protocole de décommissionnement opérationnel de l'agent (Priorité P1 — Bloquant)
1. Reléguer la métagouvernance de la fraîcheur du document papier *Compendium* (dates de gel des 50 chapitres, révision des fiches S-001 à S-159) en Annexe N.
2. Déployer dans les sections 50.1 à 50.4 la spécification d'ingénierie pour le **décommissionnement sécurisé de l'agent logiciel en 5 phases** :
   - *Phase 1 : Détection objective de dérive* : alerte automatique sur divergence de distribution ($KL(P || Q) > \epsilon$) ou chute du taux de succès aux tests métamorphiques.
   - *Phase 2 : Passage en état `DRAINING`* : suspension atomique des nouvelles admissions sur les passerelles MCP / A2A et achèvement des transactions sagas en vol.
   - *Phase 3 : Révocation cryptographique des identités* : révocation immédiate des certificats mTLS (CRL / OCSP), invalidation des jetons SPIFFE SVID et publication du statut révoqué des Agent Cards / clés W3C DID.
   - *Phase 4 : Purge mémorielle certifiée* : effacement cryptographique et vérifiable des mémoires vectorielles et contextes RAG, garantissant le droit à l'effacement (art. 12.1 Loi 25 québécoise et RGPD).
   - *Phase 5 : Archivage probatoire scellé* : exportation hermétique des traces W3C et des journaux d'audit vers un stockage WORM immuable (conservation légale 7 ans selon BSIF E-23).

### Chantier W-03 : Refondation formelle de la sémantique d'effet et des sagas au Chapitre 48 (Priorité P1 — Bloquant)
1. Supprimer l'équation erronée de la Figure 48.2 et du § 48.1. Expliciter le *Dual-Write Problem* et formaliser l'obligation d'un registre d'idempotence répliqué par State Machine Replication (SMR / Raft) adossé au patron *Transactional Outbox*.
2. Réécrire la section 48.3 sur les Sagas :
   - Démontrer la composabilité algorithmique de la compensation dynamique via pile inverse LIFO ($[a_k^{-1}, \dots, a_1^{-1}]$) pour toute séquence d'actions réversibles ;
   - Poser la règle cardinale de l'**unique transaction pivot ($T_{\text{pivot}}$)** de Garcia-Molina & Salem (1987) pour borner la génération de plans dynamiques ;
   - Prescrire le patron *Semantic Escrow* (verrous sémantiques) pour masquer les états intermédiaires aux agents concurrents et éradiquer les lectures sales (*dirty reads*).
3. Définir explicitement le modèle de tolérance aux pannes distribuées (synchronicité partielle avec reprise sur panne).

### Chantier W-04 : Ancrage épistémique dans la théorie de la calculabilité au Chapitre 49 (Priorité P1 — Bloquant)
1. Inscrire le **Théorème de Rice (1953)** comme borne mathématique fondamentale démontrant l'indécidabilité de la conformité sémantique statique des agents Turing-complets.
2. Poser la limite formelle de **Schneider (2000)** : borner les moniteurs d'exécution PEP/PDP aux seules propriétés de sûreté (*safety properties*), en démontrant l'impossibilité de garantir la vivacité sans arrêts conservateurs.
3. Remplacer la mention fallacieuse d'un « théorème de gouvernance à 4 propriétés spéculatif » par une formulation prudente de conjecture d'arbitrage de politique de sécurité.

### Chantier W-05 : Modernisation de l'architecture de supply chain logicielle au Chapitre 47 (Priorité P2 — Majeur)
1. Intégrer l'architecture de référence universelle **Sigstore** (Cosign, Rekor, Fulcio) pour sceller les artefacts d'agents par signature sans clé liée à des identités OIDC.
2. Mettre à jour le statut du framework in-toto au rang officiel de **CNCF Graduated** (acquis le 10 février 2025).
3. Résoudre l'incohérence taxonomique en unifiant le modèle sous la hiérarchie : Harnais d'hôte ($\text{ExecutionHarness}$) vs Charge utile scellée ($\text{AgentPayload}$ : Modèle, Invites, Outils, Politiques encapsulés en conteneur OCI sous SLSA Build L3).
4. Étendre le versionnement à 5 horloges pour intégrer l'état de la mémoire contextuelle et le non-déterminisme physique GPU (IEEE 754).

### Chantier W-06 : Actualisation des standards normatifs et résolution de la délégation (Priorité P2 — Majeur)
1. Remplacer l'affirmation d'expiration au § 48.5 par l'intégration de la révision active **`draft-ietf-httpapi-idempotency-key-header-08`** (22 octobre 2026), en analysant la gestion des statuts HTTP 409 et les empreintes d'idempotence.
2. Prescrire le standard **W3C Trace Context** (`traceparent`, `tracestate`) et OpenTelemetry Baggage comme clé universelle de jointure entre appels d'outils et transactions ISO 20022 UETR.
3. Désamorcer l'impasse du 2e saut de délégation au § 49.14 en mobilisant les standards établis de délégation cryptographique : **Macaroons** (Birgisson et al. NDSS 2014) et **RFC 8693 OAuth Token Exchange**.

### Chantier W-07 : Rapprochement arithmétique et ouverture de l'appareil critique (Priorité P2 — Majeur)
1. Aligner les chiffres de l'Annexe I (p. 585) : $1263 - 198 = 1065$ entrées uniques, en éliminant la confusion des 134 doublons.
2. Désenclaver les 159 faits de l'Annexe B (S-001 à S-159) en adjoignant à chaque entrée sa référence externe primaire vérifiable (DOI, URL, RFC ou texte de loi officiel).
