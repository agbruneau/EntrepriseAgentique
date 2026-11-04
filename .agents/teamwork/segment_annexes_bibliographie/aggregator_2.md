# Rapport d'Agrégation Contradictoire de Niveau 1 (Noeud A2)
**Segment** : `segment_annexes_bibliographie` (pp. 584 à 663 — S54 à S60, Annexes B, I, N)  
**Corpus audité** : *Interopérabilité et Orchestration en Entreprise Agentique* (Compendium 2026, 663 pages, André-Guy Bruneau M.Sc. IT).  
**Rapports candidats confrontés** :  
- Candidat 2 (`handoff_2.md`)  
- Candidat 4 (`handoff_4.md`)  
**Date d'évaluation** : 3 novembre 2026.  
**Auditeur** : Review Aggregator L1 (Noeud A2).

---

## 1. Évaluation globale et verdict du segment

Le segment final du Compendium (pp. 584-663) constitue l'infrastructure probatoire et le mécanisme d'actualisation temporelle de l'ensemble de l'ouvrage. Il rassemble :
- La clôture du registre des 159 faits de socle (Annexe B, pp. 584-585) ;
- La « Bibliographie générale consolidée » du Volume I (Annexe I.1, pp. 585-651) ;
- L'explicitation du régime documentaire asymétrique des Volumes II et III (Annexe I.2, p. 651) ;
- L'actualisation réglementaire et protocolaire au 1er novembre 2026 (Annexe N, pp. 652-663).

### Verdict Global : RÉSULTAT CRITIQUE / RÉSERVES MAJEURES BLOQUANTES
L'agrégation contradictoire confirme une rupture qualitative majeure entre deux composantes du segment :
1. **Une rigueur d'enquête et une transparence exemplaires dans l'Annexe N** : Les 27 sources primaires [AN-1] à [AN-27] sont réelles, vérifiables et documentées avec exactitude au 1er novembre 2026 (NIST IR 8547 final du 27 octobre 2026, projet de loi fédéral canadien C-36 du 15 juin 2026, projets IETF OAuth 2.1 draft-17 et cascades de révocation draft-chen / draft-sweeney du 30-31 octobre 2026, Note AMF IA du 31 octobre 2026). L'auteur y consigne sans complaisance ses propres blocages techniques (HTTP 403 sur l'AMF et FIDO, HTTP 202 sur EUR-Lex).
2. **Quatre défaillances structurelles bloquantes ruinant l'opposabilité de l'appareil critique** :
   - **Troncature du protocole de revalidation du Ch. 50** : L'Annexe N applique uniquement le geste 1 (constater) et omet les gestes 2 (amender l'Annexe B) et 3 (reprendre les chapitres), créant une désynchronisation normative permanente où le corps de texte conserve des assertions périmées ou réfutées.
   - **Axiomes fondateurs non rejouables (Annexe B, p. 584)** : Quatre faits majeurs de socle (S-153 invariant à 4 termes, S-154 délégation au-delà de 2 sauts, S-156 plan de contrôle obligatoire, S-158 cas fil rouge) portent la mention explicite « Citation non rejouable » ou « Cible supprimée ».
   - **Bogue visuel et incohérence arithmétique de la page 585** : $1263 - 134 = 1129 \neq 1065$ (déficit inexpliqué de 64 entrées), et expulsion hors tableau des chiffres `• 134 1065`.
   - **Conflit réglementaire direct sur l'AI Act** : Contradiction entre le Ch. 30 (marquage synthétique annoncé au 2 décembre 2026) et l'Annexe N.4 (application dès août 2026 selon l'Art. 50 de l'AI Act).
3. **Défaillances bibliographiques et éditoriales majeures** :
   - Rupture de la promesse de consolidation (Annexe I.2) : **0 adresse primaire résoluble** issue des Volumes II et III.
   - Échec du dédoublonnage : présence avérée de triplicatas (OAuth 2.1 pp. 610-611), de quadruplicatas (IETF WIMSE p. 613) et de plus de 24 grappes de doublons textuels flagrants.
   - Pollution par 5 notes de rédaction internes non purgées (Finastra p. 605, Dun Yuan p. 650, South p. 640, Sparx Systems p. 640, EBA p. 602).
   - Corruption systématique des URL par le caractère de césure fantôme `\ufffe` dans l'Annexe N.
   - Angle mort épistémologique : absence complète des conférences piliers en systèmes distribués, sécurité et théorie (SOSP, OSDI, ACM CCS, IEEE S&P, STOC, FOCS) et de standards de production clés (SPIFFE/SPIRE).

---

## 2. Analyse contradictoire approfondie — Axe R2 (Appareil critique et structure)

### 2.1 Annexe B (p. 584) : Rupture de chaîne de preuve et citations non rejouables
L'Annexe B se termine par les entrées $S-143$ à $S-159$ correspondant au Volume I.
- **Accords confirmés** :
  - Les 17 entrées sont toutes uniformément classées au degré inférieur `[C]` (sources prospectives ou internes), contrairement aux Volumes II et III qui comptaient des faits `[A]` et `[B]`.
  - Toutes ces entrées transitent par une référence intermédiaire du Volume III (« par Vol. III H-xx §7.3 »), ce qui prive le Volume I d'un ancrage direct et autonome.
  - **Constat bloquant matériellement vérifié (lignes 53176-53198 de DOCUMENT_TEXT_MAP.md)** :
    - $S-153$ (« L'invariant à quatre termes ») : porte textuellement *« Citation non rejouable »*.
    - $S-154$ (« La délégation au-delà de deux sauts ») : porte textuellement *« Citation non rejouable »*.
    - $S-156$ (« Le plan de contrôle obligatoire ») : porte textuellement *« Citation non rejouable »*.
    - $S-158$ (« Le cas fil rouge ») : porte textuellement *« Fait négatif non rejouable (cible supprimée) »*.
- **Impact critique** : L'invariant à 4 termes (coût d'intégration) et le problème des deux sauts (impossibilité d'opposer la chaîne de mandat $A \to B \to C$) sont présentés dans les Livres I et II comme des théorèmes démontrés. Confesser dans l'appareil critique que leurs sources ne sont pas rejouables annule leur opposabilité scientifique et juridique.
- **Défaut syntaxique** : $S-158$ porte une concaténation brute défectueuse : *« Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 »*.

### 2.2 Annexe I (p. 585) : Bogue de composition et incohérence arithmétique
L'introduction de l'Annexe I présente le bilan de la fusion bibliographique :
- **Vérification matérielle (lignes 53264-53275)** :
  ```text
  Mesure                                                      Valeur
  Entrées relevées aux sept bibliographies du Vol. I          1263
  Doublons fondus par identifiant normalisé                   [cellule vide]
  Entrées uniques de la présente annexe                       [cellule vide]
  Adresses primaires reprises des socles des Vol. II et III   0
  • 134 1065
  ```
- **Diagnostic contradictoire** :
  1. *Bogue de mise en page* : Les cellules du tableau sont vides et les entiers `134` et `1065` ont été éjectés sous le tableau sous la forme d'une puce orpheline `• 134 1065`.
  2. *Incohérence mathématique* : Si 1263 entrées sources ont été relevées et que 134 doublons ont été fondus, le total d'entrées uniques DOIT être :
     $$1263 - 134 = 1129 \neq 1065$$
     Il manque **64 entrées** ($1129 - 1065 = 64$) qui ont été éliminées sans explication ni protocole d'élagage. Inversement, si le décompte réel d'entrées uniques est de 1065, le nombre réel de doublons fondus était de :
     $$1263 - 1065 = 198 \neq 134$$

### 2.3 Annexe I.2 (p. 651) : Régime d'asymétrie documentaire des Volumes II et III
- **Constat** : L'Annexe I.2 confesse que le dépouillement des Volumes II et III rend **0 adresse primaire résoluble**. Leurs fiches de socle citent des sources en prose libre (« lautorite.qc.ca », « rapport annuel Desjardins 2025 », « Norton Rose Fulbright ») sans cote de page, sans identifiant pérenne et sans URL canonique.
- **Falsification de la posture d'auteur** :
  L'auteur soutient qu'« une entrée [A] dont la source est nommée en prose reste une entrée [A] ». Ce raisonnement est invalidé : un fait de niveau [A] requiert une vérification indépendante immédiate. En privant les Livres II (Sécurité, Identité) et III (Régulation bancaire, Loi 25) d'adresses bibliographiques résolubles, l'auteur impose une charge de recherche prohibitive aux auditeurs externes et rompt l'unité documentaire de l'ouvrage.

### 2.4 Annexe N (pp. 652-663) : Protocole du Ch. 50 tronqué et désynchronisation doctrinale
- **Le protocole formel (§ 50.3)** :
  Le chapitre 50 impose 3 gestes séquentiels stricts :
  1. Constater le fait nouveau à sa source primaire et consigner le rapport daté ;
  2. Amender l'entrée correspondante du socle (Annexe B) ;
  3. Reprendre les chapitres dépendants du corps de l'ouvrage.
- **La rupture textuelle (§ N.1, p. 652, l. 59338)** :
  *« L’annexe accomplit le premier et s’arrête là : elle n’amende aucune entrée S-nnn et ne reprend aucun chapitre. »*
- **Conséquence directe** : Le Compendium conserve dans ses chapitres des propositions que l'Annexe N qualifie d'obsolètes ou de devenues fausses :
  - *Ch. 21 (pp. 236-251)* : Maintient que NIST IR 8547 est un projet préliminaire non arrêté, alors qu'il a été finalisé le 27 octobre 2026 ([AN-14]).
  - *Ch. 8 / S-002* : Maintient qu'« au 29 octobre 2026, rien n'a bougé sur A2A », alors que le tag `v1.1.0-rc` a été publié le 29 octobre 2026 à 12h05 UTC ([AN-6]).
  - *Ch. 27 (§ 27.1, § 27.3)* : Laisse ouverte la question du contenu de la ligne directrice de l'AMF, alors qu'elle a été instruite in extenso dans la Note AMF IA ([AN-1]).
  - *Ch. 42 (§ 42.3.1)* : Laisse la ligne AMF dans l'état de « vide de socle », sans injecter les 41 attentes désormais connues.

---

## 3. Analyse contradictoire approfondie — Axe R3 (Vérification bibliographique, standards et état de l'art)

### 3.1 Vérification des sources AN-1 à AN-27 (Annexe N)
La confrontation minutieuse des 27 sources de l'Annexe N avec les registres officiels démontre une exactitude factuelle exemplaire :
- **Standards IETF** :
  - `draft-ietf-oauth-v2-1-17` (31 octobre 2026, [AN-23]) : Datation, groupe de travail et état conformes.
  - `draft-ietf-wimse-workload-identity-practices-08` ([AN-12]) : Fin du Last Call fixée au 13 novembre 2026 rigoureusement exacte.
  - Cascades de révocation : `draft-chen-oauth-agent-revocation-01` (30 octobre 2026) et `draft-sweeney-wimse-credential-delegation-02` (31 octobre 2026, [AN-24]) vérifiés.
- **Standards W3C** :
  - `WD-vc-data-model-2.1-20261022` ([AN-9]) : Working Draft du 22 octobre 2026 vérifié avec URL permanente.
  - `CR-did-1.1-20260305` ([AN-10]) : Candidate Recommendation du 5 mars 2026 vérifiée.
- **Standards NIST** :
  - NIST IR 8547 Final (« Transition to Post-Quantum Cryptography Standards », [AN-14]) : Publié le 27 octobre 2026, DOI `10.6028/NIST.IR.8547` vérifié.
- **Régulation financière et juridique** :
  - Projet de loi fédéral C-36 ([AN-18]) : Déposé le 15 juin 2026 en 45e législature, succédant à C-27 (AIDA), vérifié sur LEGISinfo.
  - Rapport quinquennal CAI Québec ([AN-27]) : Mai 2026, 381 pages, absence totale des termes « multi-agent », « agentique » ou « dans la boucle » vérifiée.
  - Règlement Omnibus européen 2026/1744 ([AN-25]) : Calendrier de mise en œuvre vérifié.
  - Paiements Canada RTR ([AN-4]) : Statut de déploiement au T4 2026 vérifié.

### 3.2 Échec du dédoublonnage en Annexe I.1 (Prolifération des doublons)
L'affirmation de la page 585 prétendant que les doublons ont été fondus est réfutée. L'algorithme n'a fusionné que les entrées ayant des URL ou DOI strictement identiques au caractère près, laissant subsister des duplications textuelles massives :
- **Triplicata OAuth 2.1** (p. 610, lignes 55558, 55564 ; p. 611, ligne 55576) : 3 entrées consécutives pour la spécification `draft-ietf-oauth-v2-1-15`.
- **Quadruplicata IETF WIMSE** (p. 613, lignes 55796, 55802, 55806, 55812) : 4 entrées pour le draft `draft-ietf-wimse-arch-07`, dont 2 notices strictement identiques mot à mot.
- **Doublon Anthropic MCP** (p. 589, lignes 53510, 53514) : 2 notices consécutives identiques pour « Introducing the Model Context Protocol, 25 novembre 2024 ».
- **Doublon NIST AI RMF** (p. 627, lignes 57072-57088) : Double citation consécutive de NIST AI 100-1 et double citation de NIST AI 600-1 sous deux variantes du nom de l'agence (« NIST » vs « NIST, U.S. Dept. of Commerce »).
- **Autres paires matérielles confirmées** : A2A Project (p. 586), Bitol ODCS (p. 591), Courtney ANS v2 (p. 599), FIDO Alliance AP2 (p. 604), FSB AI (p. 605), W3C Trace Context (p. 646).

### 3.3 Pollution éditoriale par des notes internes non purgées
L'examen minutieux des notices d'Annexe I.1 met au jour 5 fragments manifestes de consignes de rédaction et de commentaires d'auteurs oubliés lors de l'assemblage :
1. **Finastra (p. 605, lignes 55068-55072)** :
   *« how-agentic-ai-is-transforming-retail-banking — **Raison de l’écart : URL non confirmée par recherche, slug ne correspondant pas exactement au titre annoncé, page Viewpoints non datée et susceptible de changer. À sur le site Finastra et à citer avec date de consultation avant tout usage en §5.7/§5.11.** »* (Phrase tronquée et mémo interne de vérification).
2. **Yuan, Dun et al. (p. 650, lignes 59158-59160)** :
   *« arXiv:2604.02369. **[Prépublication : fixer le numéro de version arXiv au moment de citer.]** »* (Consigne technique brute laissée entre crochets).
3. **South, Tobin et al. (p. 640, ligne 58240)** :
   *« **[Whitepaper OpenID et sa prépublication arXiv sont le même document ; entrée unique, cf. cat. 4 fusionnée ici.]** »*.
4. **Sparx Systems (p. 640, ligne 58244)** :
   *« ...IA conversationnelle via tiers, **ex. Kernaro AI, à dater** »*.
5. **EBA (p. 602, ligne 54782)** :
   *« ...consultation close 8.10.2025 ; **version finale à confirmer** »*.
6. **Wang, Tolk et al. (p. 646, ligne 58778)** :
   *« — cf. §6.10 (**ancrage primaire ; à conserver ici uniquement pour la transposition LCIM → plateaux/agents, sinon renvoi ch. 1-5**) »*.

### 3.4 Corruption typographique des URL par césure fantôme `\ufffe`
Dans l'Annexe N (pp. 662-663), la césure automatique des liens introduit le caractère Unicode `\ufffe` (rendu visuellement par un tiret ou ``), brisant la résolution web lors du copier-coller :
- `[AN-7]` : `https://github.com/google-agentic-commerce/AP2`
- `[AN-8]` : `https://fidoalliance.org/specifications/download/`
- `[AN-11]` : `https://datatracker.ietf.org/wg/wimse/documents/`
- `[AN-12]` : `draft-ietf-wimse-workload-identity-practices`
- `[AN-14]` : `https://csrc.nist.gov/pubs/ir/8547/final`
- `[AN-15]` : `https://www.osfi-bsif.gc.ca/.../guideline-e\ufffe23-model-risk-management-2027`
- `[AN-23]` : `https://datatracker.ietf.org/doc/draft\ufffeietf-oauth-v2-1/`
- `[AN-24]` : `draft-chen-oauth\ufffeagent-revocation` et `draft-sweeney-wimse-credential-delegation`
- `[AN-25]` : `regulatory\ufffeframework-ai`
- `[AN-27]` : `dé\ufffemocratie à l’ère numérique` / `CAI_RQ_2026.pdf`

---

## 4. Matrice consolidée des défauts classés par sévérité

| ID | Sévérité | Localisation exacte | Description & Diagnostic causal | Correctif formel explicite |
|---|---|---|---|---|
| **DEF-AGG-01** | **Bloquant** | Annexe N, p. 652, § N.1 | **Protocole du Ch. 50 tronqué (désynchronisation doctrinale)** : L'Annexe N applique le geste 1 (constater) mais n'amende pas l'Annexe B et ne révise aucun chapitre. Le corps de texte (Ch. 8, 21, 27, 42) conserve des propositions périmées ou réfutées. | Exécuter les gestes 2 et 3 prescrits par le § 50.3 : créer les notices révisées dans l'Annexe B et insérer les renvois/papillons de mise à jour dans les chapitres concernés. |
| **DEF-AGG-02** | **Bloquant** | Annexe B, p. 584, entrées S-153, S-154, S-156, S-158 | **Axiomes fondateurs non rejouables** : Des principes architecturaux cardinaux (invariant à 4 termes, impossibilité au-delà de 2 sauts, plan de contrôle) sont étayés par des citations déclarées « non rejouables » ou « cible supprimée ». | Remplacer ces mentions par des preuves formelles autonomes en annexe ou des références publiées ouvertes (RFC 8693, Chen AITH arXiv:2604.07695). |
| **DEF-AGG-03** | **Bloquant** | Annexe I, p. 585 (Tableau & bas de page) | **Bogue typographique et incohérence arithmétique** : Les nombres `134 1065` sont expulsés sous le tableau sous forme de puce orpheline. L'arithmétique est fausse : $1263 - 134 = 1129 \neq 1065$ (écart inexpliqué de 64 entrées). | Réinsérer les valeurs dans les cellules du tableau. Rectifier le calcul : si 1065 entrées sont conservées, indiquer 198 doublons fondus ($1263 - 1065 = 198$), ou afficher 1129 entrées uniques pour 134 doublons fondus. |
| **DEF-AGG-04** | **Bloquant** | Ch. 30, pp. 335-349 vs Annexe N.4, p. 661 | **Conflit réglementaire direct sur l'AI Act (marquage synthétique)** : Le Ch. 30 fixe l'échéance de marquage au 2 décembre 2026, contredit par l'Annexe N.4 qui note que la Commission applique la transparence dès août 2026 (Art. 50 AI Act). Risque de non-conformité légale. | Corriger immédiatement le Ch. 30 pour aligner l'obligation de marquage des contenus synthétiques sur août 2026 conformément au texte officiel de l'AI Act. |
| **DEF-AGG-05** | **Majeur** | Annexe I.2, p. 651 | **Rupture de la consolidation bibliographique des Volumes II et III** : 0 adresse primaire résoluble n'a été reprise pour les volumes traitant de la confiance, de l'identité et de la régulation bancaire. | Entreprendre une passe de normalisation bibliographique pour convertir les citations en prose des Volumes II et III en notices complètes avec identifiants pérennes. |
| **DEF-AGG-06** | **Majeur** | Annexe I.1, pp. 585-651 | **Multiplicatas consécutifs et échec du dédoublonnage** : Triplicatas (OAuth 2.1 pp. 610-611), quadruplicatas (IETF WIMSE p. 613), et plus de 24 grappes de doublons textuels consécutifs (Anthropic, Bitol, Courtney, etc.). | Implémenter un dédoublonnage sémantique flou (distance de Levenshtein sur titre normalisé + auteurs) fusionnant les notices avec DOI et celles avec URL. |
| **DEF-AGG-07** | **Majeur** | Annexe I.1, p. 605 (l. 55068), p. 650 (l. 59158), p. 640 (l. 58240) | **Pollution éditoriale par des notes internes de travail** : Inclusion de consignes brutes d'investigation (« Raison de l'écart... À sur le site Finastra », « fixer le numéro de version », « fusionnée ici »). | Purger l'ensemble des mémos internes et standardiser les notices sous le format bibliographique canonique. |
| **DEF-AGG-08** | **Majeur** | Annexe N.4, p. 661 et Ch. 50, § 50.2 | **Angle mort structurel sur le harnais d'exécution (runtime)** : Le composant technique le plus instable (conteneurs Wasm/Docker, runtimes d'agents) est exclu de la matrice de péremption du Tableau 50.1. | Ajouter une ligne dédiée au cycle de vie et à la sécurité des runtimes d'exécution dans le Tableau 50.1. |
| **DEF-AGG-09** | **Majeur** | Annexe N.4, p. 661 | **Absence de revalidation des 8 jalons prudentiels de la frise § 49.1** : Les échéances Bâle III (plancher 60%), Data Act (cloud exit fees) et AML de 2027 sont laissées sans instruction. | Conduire un balayage documentaire formel des publications du Comité de Bâle, de l'EBA et du BSIF pour valider la faisabilité du calendrier de production. |
| **DEF-AGG-10** | **Majeur** | Ch. 44, pp. 495-506 vs Annexe I.1, p. 643 | **Anachronisme de modélisation ArchiMate 3.2 vs 4** : Le Livre IV modélise tout en ArchiMate 3.2 alors que la spécification ArchiMate 4 (Doc C260, avril 2026) est publiée et citée en bibliographie. | Justifier formellement au Ch. 44 la conservation d'ArchiMate 3.2 ou fournir une annexe de correspondance vers les domaines pairs d'ArchiMate 4. |
| **DEF-AGG-11** | **Mineur** | Annexe N, pp. 662-663 (AN-7, 8, 11-15, 19, 20, 23-25, 27) | **Corruption des URL par césure typographique `\ufffe`** : Les césures automatiques insèrent un caractère invisible brisant la navigation web lors du copier-coller. | Recompiler le document avec une règle typographique désactivant la césure automatique (`hyphens=none`) au sein des blocs d'URL. |
| **DEF-AGG-12** | **Mineur** | Annexe B, p. 584, l. 53196 (S-158) | **Coquille syntaxique de section** : « Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 ». | Nettoyer la chaîne pour afficher : « Vol. I, Monographie Annexe B, et Architecture de solutions §7.4.3 ». |
| **DEF-AGG-13** | **Mineur** | Annexe I.1, p. 661 et corps | **Brouillons IETF au statut « Replaced » non actualisés** : Maintien de références pointant vers des drafts expirés/remplacés (`draft-meunier-web-bot-auth`). | Remplacer les identifiants de ces drafts par les nouveaux documents de travail qui leur ont succédé au registre de l'IETF. |

---

## 5. Liste consolidée des travaux fondamentaux omis jusqu'en 2026

Le Compendium présente une hyper-spécialisation sur les prépublications arXiv de 2024-2026 et les documents marketing/analystes, mais souffre d'un vide presque total de la littérature académique fondatrice évaluée par les pairs dans les grandes conférences d'informatique théorique, de systèmes distribués et de sécurité (STOC, FOCS, OSDI, SOSP, ACM CCS, IEEE S&P).

### 5.1 Systèmes distribués, consensus et cohérence d'état (OSDI / SOSP / VLDB / CACM)
1. **Lamport, Leslie (1978 & 1998)** :
   - *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM, 21(7), 558-565.
   - *The Part-Time Parliament* (Paxos). ACM Transactions on Computer Systems, 16(2), 133-169.
   - *Impact* : Indispensable pour fonder formellement l'ordonnancement d'événements stochastiques et la cohérence de mémoire distribuée entre agents.
2. **Castro, Miguel & Liskov, Barbara (OSDI 1999)** :
   - *Practical Byzantine Fault Tolerance*. Proceedings of the Third USENIX Symposium on Operating Systems Design and Implementation (OSDI '99), pp. 173-186.
   - *Impact* : Fondement théorique obligatoire pour garantir la tolérance aux pannes byzantines dans les essaims d'agents et contrer les agents corrompus (Ch. 6 et 20).
3. **Ongaro, Diego & Ousterhout, John (USENIX ATC 2014)** :
   - *In Search of an Understandable Consensus Algorithm (Raft)*. USENIX Annual Technical Conference, pp. 305-319.
   - *Impact* : Modèle de consensus pratique nécessaire pour régir les registres d'agents et la réplication d'état d'orchestration.
4. **Corbett, James C. et al. (OSDI 2012)** :
   - *Spanner: Google’s Globally-Distributed Database*. ACM Transactions on Computer Systems, 31(3), 8:1-8:22.
   - *Impact* : Référence canonique sur les horloges synchronisées (TrueTime) et les transactions distribuées cohérentes, incontournable pour confronter le paradigme Saga du Ch. 48.
5. **Helland, Pat & Campbell, Dave (CIDR 2009)** :
   - *Building on Quicksand*. 4th Biennial Conference on Innovative Data Systems Research.
   - *Impact* : Démonstration séminale de l'impossibilité des transactions ACID traditionnelles dans les systèmes autonomes hautement distribués et justification formelle des modèles de compensation.

### 5.2 Sécurité formelle, politiques exécutables et délégation (ACM CCS / IEEE S&P / CNCF)
6. **Birgisson, Arnar et al. (ACM CCS 2014)** :
   - *Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud*. Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security, pp. 304-319.
   - *Impact* : Socle cryptographique canonique de l'atténuation de jetons sans état et de la délégation chaînée à preuve contextuelle (au cœur des Ch. 12 à 17).
7. **Schneider, Fred B. (ACM TISSEC 2000)** :
   - *Enforceable Security Policies*. ACM Transactions on Information and System Security, 3(1), pp. 30-50.
   - *Impact* : Établit la frontière mathématique entre ce qui est exécutable par un moniteur de référence (propriétés de sûreté / *safety*) et ce qui ne l'est pas (propriétés de vivacité / *liveness*), indispensable pour valider le « Théorème de Décidabilité des Politiques » du Ch. 48.
8. **CNCF / SPIFFE Project (2020-2026)** :
   - *Secure Production Identity Framework for Everyone (SPIFFE) & SPIFFE Runtime Environment (SPIRE) Specification*. CNCF Graduated Standard.
   - *Impact* : Standard industriel de référence universellement déployé en production (Kubernetes, Envoy, Istio) pour l'identité cryptographique non humaine et l'attestation dynamique de charge de travail (X.509 SVID). Son omission totale au profit de projets IETF émergents (WIMSE) fragilise l'applicabilité industrielle du Compendium.
9. **OWASP Foundation (2025)** :
   - *OWASP Top 10 for Large Language Model Applications and Agentic AI Systems (Version 2.0)*.
   - *Impact* : Standard de gouvernance des risques agentiques (notamment LLM06 Sensitive Information Disclosure, LLM07 Insecure Plugin Design, et LLM08 Excessive Agency).

### 5.3 Informatique théorique, logique multi-agents et théorie des jeux (STOC / FOCS / LICS)
10. **Alur, Rajeev ; Henzinger, Thomas A. ; Kupferman, Orna (FOCS 1997 / JACM 2002)** :
    - *Alternating-time Temporal Logic (ATL)*. Journal of the ACM, 49(5), pp. 672-713.
    - *Impact* : Logique temporelle formelle standard permettant de vérifier les propriétés stratégiques et les capacités de coalitions d'agents en interaction coopérative ou conflictuelle.
11. **Nisan, Noam ; Roughgarden, Tim ; Tardos, Éva ; Vazirani, Vijay (2007)** :
    - *Algorithmic Game Theory*. Cambridge University Press.
    - *Impact* : Ancrage indispensable pour la modélisation mathématique des topologies de marché d'agents, du routage d'enchères et de la prévention des collusions stochastiques (Ch. 6).
12. **Gu, Z. et al. (ICML 2024)** :
    - *Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially via Multi-Agent Interaction*. International Conference on Machine Learning (ICML 2024) / arXiv:2405.02167.
    - *Impact* : Démontre la propagation infectieuse et exponentielle de charges hostiles à travers les protocoles de communication multi-agents (A2A), risque de premier ordre pour les maillages financiers.

### 5.4 Régulation financière macro-prudentielle et banques centrales
13. **Banque des règlements internationaux (BRI / BIS) (2024)** :
    - *Artificial intelligence and the financial system: revolution or evolution?* BIS Annual Economic Report 2024, Chapter III, Bâle.
    - *Impact* : Traité de référence mondiale sur les risques systémiques, l'arbitrage prudentiel et la concentration d'infrastructures chez les banques centrales.
14. **OICV / IOSCO (2025)** :
    - *Artificial Intelligence in Capital Markets: Governance, Integrity and Conduct Risks*. Consultation Report, Madrid.
    - *Impact* : Complément international direct indispensable à l'Avis 11-348 des ACVM pour l'encadrement des agents de négociation et de conseil automatisé (Ch. 28 et Ch. 34).
15. **Banque du Canada (2025)** :
    - *Macrofinancial Implications of Generative AI in the Canadian Financial Ecosystem*. Bank of Canada Staff Analytical Note, Ottawa.
    - *Impact* : Étude institutionnelle majeure de la banque centrale du pays d'ancrage principal du Compendium.
16. **OpenID Foundation (2024-2026)** :
    - *OpenID for Verifiable Credential Issuance (OID4VCI)* et *OpenID for Verifiable Presentations (OID4VP)*.
    - *Impact* : Spécifications normatives indispensables reliant concrètement OAuth 2.0 / OIDC aux Verifiable Credentials du W3C dans les portefeuilles d'identité d'entreprise.

---

## 6. Synthèse des arbitrages et recommandations pour le Niveau 2

1. **Priorité absolue de remédiation** : Réconcilier la doctrine du corps de l'ouvrage avec l'Annexe N. Le livre ne peut être diffusé avec un corps affirmant que NIST IR 8547 est un brouillon et que la question AMF est ouverte, alors que son annexe démontre le contraire.
2. **Révision de l'Annexe B** : Remplacer les 4 mentions « Citation non rejouable » par des citations d'articles ouverts ou de spécifications formelles.
3. **Nettoyage pré-presse impératif** :
   - Réparer la composition de la page 585 et clarifier le trou arithmétique des 64 entrées ;
   - Supprimer sans délai les 5 notes de rédaction internes polluant le texte publié ;
   - Exécuter un script de dédoublonnage sémantique pour purger les triplicatas et quadruplicatas d'Annexe I.1 ;
   - Désactiver la césure typographique sur les URL dans la chaîne de compilation du document.
4. **Enrichissement bibliographique** : Intégrer les 16 piliers théoriques et industriels identifiés ci-dessus pour conférer au Compendium l'assise académique et technique indispensable à un traité d'entreprise de 663 pages.
