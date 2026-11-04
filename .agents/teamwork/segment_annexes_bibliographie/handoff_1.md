# Rapport d'Audit Contradictoire — Segment Annexes et Bibliographie (Candidat 1)
**Périmètre audité** : Manuscrit *Interopérabilité et Orchestration en Entreprise Agentique* (Édition Novembre 2026, 663 pages), pp. 584 à 663 (couvrant les segments S54 à S60 du plan de revue), incluant l'Annexe B (pp. 578-584), l'Annexe I (I.1 et I.2, pp. 585-651) et l'Annexe N (pp. 652-663).  
**Auteur de la revue** : Analyste de revue documentaire (Niveau 0, Candidat 1).  
**Date d'évaluation** : Novembre 2026.  
**Régime d'audit** : Production — Analyse chirurgicale, falsification contradictoire, vérification Web systématique et preuve empirique.

---

## 1. Résumé exécutif du segment et verdict global

### 1.1 Objet et rôle architectural du segment
Le segment des Annexes (pp. 584-663, avec l'amont immédiat de l'Annexe B débutant à la page 578) constitue la clé de voûte de l'appareil critique, du régime probatoire et de l'opposabilité juridique et technique du Compendium :
- **Annexe B (pp. 578-584)** répertorie le *socle consolidé* des 159 faits primaires codifiés ($S\text{-}001$ à $S\text{-}159$) groupés par volume d'origine, qualifiés par un niveau de preuve critique ([A] vote adversarial à trois juges, [B] source primaire ouverte sans vote complet, [C] repérage non extrait) et assortis de degrés d'absence formels (degré 1 : fait négatif vérifié, degré 2 : fait négatif établi, degré 3 : absence de documentation).
- **Annexe I (pp. 585-651)** rassemble la *bibliographie générale consolidée* : la sous-section I.1 (pp. 586-651) regroupe le corpus bibliographique alphabétique, tandis que la sous-section I.2 (p. 651) explicite le régime de non-consolidation des volumes sources II et III.
- **Annexe N (pp. 652-663)** formalise l'*actualisation de clôture au 1ᵉʳ novembre 2026*, appliquant le protocole de péremption du chapitre 50 aux 14 événements du tableau 50.1, consignant les reports de la *Note AMF IA* (CRE-IA-2026-01-QC du 31 octobre 2026) et publiant l'inventaire transparent des éléments non revalidés.

### 1.2 Verdict global : Réservé avec révisions majeures requises
Le travail de consignation, de traçabilité des dates et de transparence épistémique démontré par l'ouvrage est d'un niveau de rigueur exceptionnel dans la littérature technique et financière contemporaine. En particulier, l'Annexe N formule des aveux d'une rare lucidité institutionnelle (refus HTTP 403, lacunes non arbitrées, dépendances sur sources payantes, renvois à des volumes absents du dépôt).

Néanmoins, l'audit technique et empirique approfondi révèle **quatre défaillances structurelles majeures et une anomalie de mise en page bloquante** :
1. **Anomalie de compilation typographique et rupture arithmétique (Page 585) [Majeur à Bloquant]** : La table récapitulative du dédoublonnage de l'Annexe I présente deux cellules vides (« Doublons fondus par identifiant normalisé » et « Entrées uniques de la présente annexe »). Les valeurs numériques associées ont débordé de la table lors du rendu pour former une puce textuelle orpheline et tronquée `• 134 1065` au bas de la page. De surcroît, le calcul arithmétique sous-jacent est invalide ($1\,263 - 134 = 1\,129 \neq 1\,065$ ; et $1\,263 - 1\,065 = 198 \neq 134$).
2. **Faillite empirique du dédoublonnage de l'Annexe I.1 [Majeur]** : Alors que l'Annexe I prétend appliquer un dédoublonnage strict par identifiant normalisé (DOI, arXiv, URL) ou signature textuelle (ramenant 1 263 entrées à 1 065), le dépouillement exhaustif des entrées 1 à 150 démontre l'existence d'au moins **17 paires, triplets ou quadruplets de doublons stricts** (dont des doublons consécutifs parfaits avec URLs identiques, tels que *Anthropic 2024 MCP* p. 588, *Courtney et al. ANS v2* p. 599, *Eclipse LMOS* p. 602, *Aldasoro et al. BIS 1194* p. 587, *Aim Labs EchoLeak* p. 587).
3. **Asymétrie documentaire critique et bibliographie unilatérale (Annexe I.2) [Majeur]** : L'« Annexe I — Bibliographie générale consolidée » est un trompe-l'œil méthodologique. Elle n'intègre que la bibliographie du Volume I. Les Volumes II et III (qui fournissent 89,3 % des faits primaires du socle en Annexe B, soit 142 faits sur 159, dont la totalité des analyses sur l'identité non humaine, l'orchestration APM OO1-OO4, E-23, la Loi 25 et le cadre bancaire canadien) ne versent aucune référence résoluble à l'Annexe I. Le lecteur ou régulateur externe est donc privé de tout identifiant pérenne pour vérifier 9 faits de socle sur 10.
4. **Citations fantômes et discontinuités de l'Annexe B [Majeur]** :
   - Deux faits primaires du Volume III ($F\text{-}92$ et $F\text{-}96$) ont été exclus du socle consolidé $S\text{-}001$ à $S\text{-}159$, mais continuent d'être cités verbatim dans le corps du manuscrit (ch. 38 p. 438, ch. 39 p. 447, ch. 40 p. 463).
   - Les faits du Volume I ($S\text{-}143$ à $S\text{-}159$) sont tous dégradés au niveau [C] (non rejouable, sans source primaire extraite au dépôt), créant un vide probatoire sur les thèses fondamentales de l'interopérabilité.
   - La chaîne d'héritage $H\text{-}01$ à $H\text{-}33$ contient des sauts non expliqués ($H\text{-}13$ et $H\text{-}16$ absents) et une entrée $H\text{-}15$ abondamment citée (6 occurrences) bien qu'exclue du socle consolidé.
5. **Absence des volumes sources I, II et III du dépôt de révision [Majeur]** : Comme l'Annexe N le concède explicitement (p. 661), les textes intégraux des Volumes I, II et III ne sont pas versés au dépôt Git, rendant impossible la vérification contradictoire des contextes d'origine.

---

## 2. Évaluation détaillée Axe R2 : Rigueur de l'appareil critique et structure

### 2.1 Audit structurel de l'Annexe B (pp. 578-584)
L'Annexe B constitue l'inventaire des 159 faits primaires codifiés de la série $S\text{-}001$ à $S\text{-}159$.

#### 2.1.1 Découpage inter-volumes et cardinalités
L'en-tête de l'Annexe B (p. 578) expose la règle de groupement par volume d'origine :
- **Volume II (*L'autonomie encadrée*)** : 46 entrées, numérotées $S\text{-}001$ à $S\text{-}046$.
- **Volume III (*L'entreprise agentique*)** : 96 entrées, numérotées $S\text{-}047$ à $S\text{-}142$.
- **Volume I (*Interopérabilité agentique*)** : 17 entrées, numérotées $S\text{-}143$ à $S\text{-}159$.
- **Total** : $46 + 96 + 17 = 159$ entrées. L'intégrité de la séquence numérique globale est respectée (aucun trou de numérotation entre 001 et 159).

#### 2.1.2 Discordances de mapping interne et sauts de numérotation
L'analyse croisée des renvois internes vers les monographies sources révèle des anomalies de traçabilité :
1. **Sauts de faits dans le Volume II** :
   - $S\text{-}011$ renvoie à `Vol. II F-11 §7.4`.
   - $S\text{-}012$ saute immédiatement à `Vol. II F-15 §7.6`.
   - Les entrées sources `F-12`, `F-13` et `F-14` du Volume II ne figurent nulle part dans la série consolidée $S\text{-}001$ à $S\text{-}046$. Aucune note explicative n'indique si ces faits ont été fusionnés, invalidés ou abandonnés lors de la consolidation.
   - Présence d'un identifiant fractionnaire non normalisé : $S\text{-}021$ renvoie à `Vol. II F-23b §7.5`, venant s'intercaler après $S\text{-}020$ (`Vol. II F-23 §7.4`).
2. **Exclusion et citations fantômes dans le Volume III** :
   - Le Volume III compte originellement 98 faits identifiés (`F-01` à `F-98`). Or, seules 96 entrées figurent dans l'Annexe B ($S\text{-}047$ à $S\text{-}142$).
   - La vérification ligne à ligne montre que `F-92` (qui devait s'intercaler entre $S\text{-}137$ `F-91` et $S\text{-}138$ `F-93`) et `F-96` (entre $S\text{-}140$ `F-95` et $S\text{-}141$ `F-97`) ont été délibérément exclus du socle consolidé.
   - *Problème critique* : Dans le corps du texte (notamment au Livre IV, chapitres 38, 39 et 40, p. 438, 447, 463 et 513), l'auteur continue de citer formellement `Vol. III F-92` (ex. « applicatif renommable et facultatif (F-92 du Vol. III, vote dû, non conduit ; exclue du socle consolidé) ») et `Vol. III F-96`. Ces faits sont des **citations fantômes** : ils sont utilisés pour étayer le discours d'observabilité sans faire partie du socle opposable $S\text{-}001$ à $S\text{-}159$.
3. **Anomalies de la table d'héritage H du Volume III** :
   - Les renvois de consolidation utilisent une table d'héritage $H\text{-}01$ à $H\text{-}33$ :
     - $H\text{-}01$ à $H\text{-}12$ et $H\text{-}14$ mappent des faits du Vol. II vers le Vol. III.
     - $H\text{-}13$ et $H\text{-}16$ sont totalement absents du Compendium.
     - $H\text{-}15$ est explicitement défini au chapitre 43 (§ 43.3) comme une « construction d’auteur du Vol. II, sans niveau ni F-xx ; H-15 n'entre pas au socle ». Pourtant, $H\text{-}15$ est cité à 6 reprises comme référence de conception dans les chapitres d'architecture !
     - $H\text{-}17$ à $H\text{-}33$ servent à importer les 17 faits du Volume I ($S\text{-}143$ à $S\text{-}159$).
4. **Fragilité épistémique des 17 entrées du Volume I ($S\text{-}143$ à $S\text{-}159$)** :
   - Les 17 entrées issues du Volume I sont **toutes** qualifiées de niveau [C] (« repérage, source identifiée et contenu non extrait » ou « citation non rejouable »).
   - Pire encore, $S\text{-}153$ (L'invariant à quatre termes), $S\text{-}154$ (La délégation au-delà de deux sauts), $S\text{-}156$ (Le plan de contrôle obligatoire) et $S\text{-}158$ (Le cas fil rouge) sont explicitement estampillées « Citation non rejouable » ou « Fait négatif non rejouable (cible supprimée) ».
   - *Conséquence méthodologique* : Les piliers conceptuels du Livre I reposent sur des entrées qui ne bénéficient d'aucun niveau de preuve robuste ([A] ou [B]), ce qui fragilise l'ensemble de l'édifice théorique.

---

### 2.2 Audit du régime de non-consolidation de l'Annexe I.2 (p. 651)
La section I.2, intitulée *« Les Vol. II et III, et pourquoi cette annexe ne peut pas les servir »*, constitue une pièce essentielle de l'audit.

#### 2.2.1 Analyse de la prétention de l'auteur
L'auteur écrit :
> « Les socles des Vol. II et III ne portent PAS leurs sources sous une forme reprenable. Le dépouillement des deux volumes rendait, le 30 juillet 2026, une seule adresse pour l’ensemble des deux volumes ; il n’en rend plus aucune à l'audit du 19 octobre 2026 ; leurs entrées F-xx citent leurs sources en prose et par leur nom [...] jamais par un identifiant résoluble. [...] La consolidation est structurellement asymétrique : le Vol. I fournit une bibliographie parce qu’il en tient une ; les deux autres n’en fournissent aucune parce qu’ils n’en tiennent pas. »

#### 2.2.2 Falsification critique et impact sur la rigueur scientifique
Cette justification, bien que transparente, constitue un **renoncement méthodologique inacceptable pour un document soumis à des exigences de production et d'opposabilité réglementaire** :
1. **Tromperie sur l'intitulé** : L'Annexe s'intitule *« Annexe I — Bibliographie générale consolidée »*. Or, comme l'avoue I.2, elle n'est pas consolidée : c'est la bibliographie brute et dédoublonnée du seul Volume I.
2. **Régime de vérifiabilité à deux vitesses** :
   - Le Volume I (interopérabilité technique pure) est doté d'une bibliographie de 1 065 entrées détaillées avec DOI, liens arXiv et notices formelles.
   - Les Volumes II et III (qui traitent des sujets les plus sensibles sur le plan prudentiel et légal : conformité BSIF E-23, secret bancaire, Loi 25 québécoise, AMF, ISO 20022, architecture de sécurité zero trust) sont totalement privés d'appareil bibliographique résoluble. Un régulateur ou auditeur qui souhaite vérifier un fait du Livre II ou III doit « deviner » la source à partir d'une simple mention en prose.
3. **Contradiction interne avec la doctrine de l'ouvrage** : L'ouvrage martèle dans tout le Livre II et le Livre V que l'opposabilité repose sur la vérifiabilité formelle et la non-répudiation des traces. Tolérer que 89,3 % des faits du socle ne soient pas adossés à des références bibliographiques résolubles viole directement l'invariant de rigueur proclamé par l'auteur.

---

### 2.3 Audit de l'Annexe N (pp. 652-663) : Actualisation réglementaire et normative de nov. 2026

#### 2.3.1 Méthodologie et divulgation d'automatisation
L'Annexe N s'ouvre par une divulgation transparente (p. 652) : les relevés au 1ᵉʳ novembre 2026 ont été exécutés par un agent LLM (Claude, Anthropic) sous consigne de source primaire exclusive, puis contre-vérifiés par échantillonnage. Ce protocole est conforme aux bonnes pratiques d'actualisation documentaire assistée par IA, sous réserve de la validation humaine des points de divergence.

#### 2.3.2 Audit du Tableau N.1 (Application du chapitre 50 aux 14 événements)
Le tableau N.1 (pp. 653-656) confronte systématiquement les 14 événements de péremption du tableau 50.1 à l'état des sources primaires au 1ᵉʳ novembre 2026. L'audit valide la parfaite exactitude technique des constats suivants :
1. **Événement 8 — Jalons post-quantiques (NIST IR 8547)** : L'événement est correctement qualifié de **SURVENU**. Le rapport NIST IR 8547 est passé de l'état d'Initial Public Draft (novembre 2024) à la version finale officielle publiée le 27 octobre 2026 (`DOI:10.6028/NIST.IR.8547`). L'analyse de l'Annexe N est rigoureuse : elle note la modification textuelle fondamentale entre le projet et le texte final (le texte final déprécie *tous* les algorithmes à clé publique vulnérables au quantique après 2030, y compris ECDSA et RSA $\ge 112$ bits, avec interdiction totale après 2035).
2. **Événement 12 — Retrait de l'Assistants API d'OpenAI** : Correctement qualifié de **SURVENU** au 26 août 2026, remplacé par les APIs Responses et Conversations.
3. **Événements réglementaires canadiens (Événements 1, 2, 9, 11, 13, 14)** :
   - *Cadre bancaire (FCAC)* : Absence confirmée d'arrêté désignant l'organisme technique officiel (recherche exhaustive dans la Gazette du Canada parties I et II jusqu'au 31 octobre 2026).
   - *Rail temps réel (RTR)* : Non survenu au 1ᵉʳ novembre 2026 (cible T4 2026 maintenue par Paiements Canada sans date ferme).
   - *Projet de loi C-36* : Gel parlementaire confirmé à l'étape de la 2ᵉ lecture.
   - *Avis ACVM 11-348* : Aucune suite réglementaire publiée par les régulateurs des valeurs mobilières.
4. **Événements protocolaires (Événements 3 et 4)** :
   - *MCP* : Prise en compte exacte de la SEP-3398 (acceptée le 14 octobre 2026), qui formalise une cadence semestrielle et repousse la version attendue à fin mars 2027.
   - *A2A* : Détection précise de l'étiquette `v1.1.0-rc` posée le 29 octobre 2026 à 12 h 05 UTC, avec maintien du verdict « non survenu » tant qu'une version finale n'est pas taguée.
   - *AP2 / FIDO Alliance* : Constat exact de non-matérialisation du transfert au 1ᵉʳ novembre 2026 (aucun dépôt transféré chez FIDO, absence de charte).

#### 2.3.3 Intégration de la Note AMF IA (Section N.3, pp. 658-660)
L'intégration des travaux de la *Note AMF IA* (note d'instruction CRE-IA-2026-01-QC du 31 octobre 2026, André-Guy Bruneau) est articulée avec rigueur :
- L'analyse des 41 attentes de l'AMF regroupées en 5 familles permet de clore l'interrogation du chapitre 27 (§ 27.1 et § 27.3) sur le contenu article par article de la ligne directrice.
- La date de publication officielle de la ligne directrice de l'AMF est clarifiée : document daté de mars 2026, publié en avril 2026 sur le site officiel, avec prise d'effet au 1ᵉʳ mai 2027 (la date du 7 avril 2026 ne reposant que sur une source secondaire).
- L'inventaire relève avec acuité la discordance entre le tableau 42.1 (où la ligne AMF représentait le « vide de socle ») et l'extraction primaire réalisée dans la note.

#### 2.3.4 Audit des limites non revalidées (Section N.4, pp. 660-661)
L'inventaire N.4 constitue un modèle de déontologie scientifique en listant explicitement les zones d'ombre résiduelles (refus HTTP 403 sur le site de l'AMF et de la FIDO Alliance le 1ᵉʳ novembre, absence de revalidation de l'incident public d'usurpation de justificatif d'agent, etc.).

---

## 3. Évaluation détaillée Axe R3 : Vérifications bibliographiques, Web Search et état de l'art

### 3.1 Vérification exhaustive des entrées 1 à 150 de l'Annexe I.1 (pp. 586-596)
Conformément aux instructions ciblées de Candidat 1, nous avons procédé à un échantillonnage systématique et à une vérification croisée par recherche Web (`search_web`) des 150 premières notices bibliographiques de l'Annexe I.1.

#### 3.1.1 Falsification des identifiants, DOIs, arXiv et existence réelle des articles
L'hypothèse d'hallucinations pures de citations générées par LLM (articles inventés de toutes pièces) a été **infirmée** sur le corpus testé :
- Les articles scientifiques cités existent tous dans la réalité académique.
- Les identifiants arXiv et DOIs testés correspondent exactement aux publications réelles :
  1. `arXiv:2602.11327` : *Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP* (Zeynab Anbiaee, Mahdi Rabbani, Mansur Mirani et al., Canadian Institute for Cybersecurity, UNB) — **Vérifié et authentique**.
  2. `arXiv:2407.15909` et `DOI:10.1145/3729531` : *A Survey of Explainable Artificial Intelligence (XAI) in Financial Time Series Forecasting* (Pierre-Daniel Arsenault, Shengrui Wang, Jean-Marc Patenaude, ACM Computing Surveys) — **Vérifié et authentique**.
  3. `arXiv:2507.07901` : *The Trust Fabric: Decentralized Interoperability and Economic Coordination for the Agentic Web* (Sree Bhargavi Balija, Rekha Singal, Abhishek Singh et al., MIT / CSA) — **Vérifié et authentique**.
  4. `arXiv:2506.02153` : *Small Language Models are the Future of Agentic AI* (Peter Belcak et al., NVIDIA Research) — **Vérifié et authentique**.
  5. `arXiv:2602.22302` : *Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents* (Varun Pratap Bhardwaj) — **Vérifié et authentique**.
  6. `arXiv:2506.01333` : *ETDI: Mitigating Tool Squatting and Rug Pull Attacks in Model Context Protocol (MCP)* (Manish Bhatt, Vineeth Sai Narajala, Idan Habler) — **Vérifié et authentique**.
  7. `arXiv:2508.00828` : *Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks* (Antoine Bigeard, Langston Nashold, Rayan Krishnan, Shirley Wu) — **Vérifié et authentique**.
  8. `arXiv:2503.13657` : *Why Do Multi-Agent LLM Systems Fail?* (Mert Cemri, Melissa Z. Pan, Ion Stoica et al., UC Berkeley, NeurIPS 2025) — **Vérifié et authentique**.
  9. `arXiv:2510.02209` : *StockBench: Can LLM Agents Trade Stocks Profitably in Real-world Markets?* (Yanxu Chen, Zijun Yao et al.) — **Vérifié et authentique**.
  10. `arXiv:2604.07695` : *AITH: A Post-Quantum Continuous Delegation Protocol for Human-AI Trust Establishment* (Zhaoliang Chen et al.) — **Vérifié et authentique**.
  11. `arXiv:2504.19413` : *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory* (Prateek Chhikara et al.) — **Vérifié et authentique**.
  12. `arXiv:2601.22569` : *Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection* (Tanusree Debi, Wentian Zhu, Pranjol Sen Gupta) — **Vérifié et authentique**.
  13. `Nature vol. 645, pp. 633-638 (2025)` et `DOI:10.1038/s41586-025-09422-z` : *DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning* (DeepSeek-AI Team / Wenfeng Liang) — **Vérifié et authentique**.
  14. `CVE-2025-32711` et `arXiv:2509.10540` : *EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System* (Aim Security / M365 Copilot) — **Vérifié et authentique**.
  15. DOIs historiques vérifiés : Akkoyunlu et al. SOSP'75 (`DOI:10.1145/800213.806523`), Armbrust et al. Delta Lake VLDB'20 (`DOI:10.14778/3415478.3415560`), Besta et al. Graph of Thoughts AAAI'24 (`DOI:10.1609/aaai.v38i16.29720`), Brooks 1991 (`DOI:10.1016/0004-3702(91)90053-M`), Brewer 2000 (`DOI:10.1145/343477.343502`).

#### 3.1.2 Falsification du dédoublonnage de l'Annexe I.1 (Preuve empirique d'échec)
En page 585, l'ouvrage affirme que l'Annexe I est le résultat d'un algorithme de dédoublonnage automatique rigoureux :
> « Le dédoublonnage porte sur un identifiant normalisé — DOI, arXiv, URL — et, à défaut, sur une signature textuelle : deux formes du même document ne se voient pas à l’œil. »

**L'inspection empirique contredit formellement cette affirmation**. Dans les 150 premières entrées, nous avons recensé au moins **17 doublons et triplons flagrants**, dont la plupart partagent des URLs ou des identifiants identiques qui auraient dû être fusionnés immédiatement :

| Entrée A (Localisation) | Entrée B (Localisation) | Identifiant / Objet partagé | Nature du défaut |
|---|---|---|---|
| `A2A Project (2026). Agent2Agent Protocol Specification v1.0.0` (p. 586) | `Agent2Agent Protocol Project (2025). Agent2Agent Protocol Specification v1.0.0` (p. 586) | URL identique : `https://a2a-protocol.org/latest/specification/` | Doublon strict avec légère variante de nom d'auteur. |
| `AGNTCY / Outshift by Cisco (2025). Agent Directory Service` (p. 586) | `AGNTCY Project / Linux Foundation (2025). AGNTCY documentation` (p. 586) | Domaine `agntcy.org` | Doublon partiel de projet. |
| `Aim Labs (2025). EchoLeak (CVE-2025-32711)` (p. 587, 1re entrée) | `Aim Labs (2025). EchoLeak (arXiv:2509.10540)` (p. 587, 2e entrée) ET `Aim Security (2025). EchoLeak` (p. 587, 3e entrée) | Même vulnérabilité CVE-2025-32711 / Aim Security | **Triplon consécutif** sur la même page (lignes 28449-28457). |
| `Aldasoro, I. et al. (2024). Intelligent financial system: how AI is transforming finance. BIS WP 1194` (p. 587, ligne 28468) | `Aldasoro, I. et al. — Bank for International Settlements (2024). Intelligent Financial System. BIS WP 1194` (p. 587, ligne 28471) | Même article, même numéro de document BIS WP 1194 | **Doublon consécutif parfait** sur la même page. |
| `Anthropic (2024). Introducing the Model Context Protocol` (p. 588, ligne 28520) | `Anthropic (2024). Introducing the Model Context Protocol` (p. 588, ligne 28522) | URL identique : `anthropic.com/news/model-context-protocol` (25 nov. 2024) | **Doublon consécutif textuel parfait** à 2 lignes d'intervalle. |
| `BerriAI (2026). LiteLLM — SDK Python` (p. 592, ligne 28706) | `BerriAI (2026). LiteLLM AI Gateway` (p. 592, ligne 28708) | Même dépôt GitHub `BerriAI/litellm` | Doublon consécutif. |
| `Bitol (2025). Open Data Contract Standard v3.1.0` (p. 592, ligne 28737) | `Bitol (2025). Open Data Contract Standard v3.1.0` (p. 592, ligne 28739) | Même norme ODCS v3.1.0 (7 déc. 2025) | Doublon consécutif. |
| `Boomi (2025). Boomi Agentstudio / Agent Control Tower` (p. 593, ligne 28770) | `Boomi (2025). Boomi Launches Agentstudio` (p. 593, ligne 28772) | Même produit Boomi Agentstudio | Doublon consécutif. |
| `Challapally et al. (MIT Project NANDA) (2025). The GenAI Divide` (p. 595, ligne 28851) | `Challapally et al. / MIT Project NANDA (2025). The GenAI Divide` (p. 595, ligne 28854) | Même rapport MIT NANDA (juillet 2025) | Doublon consécutif avec deux URLs de PDF alternatives. |
| `Cloud Security Alliance (Huang et al.) (2025). Agentic AI Threat Modeling: MAESTRO` (p. 596, ligne 28930) | `Cloud Security Alliance (Huang) (2025). Agentic AI Threat Modeling: MAESTRO` (p. 597, ligne 28943) | Même publication CSA (6 fév. 2025) | Doublon à une page d'intervalle. |
| `Coinbase (2025). Introducing x402` (p. 597, ligne 28958) | `Coinbase (2025). x402: An Open Standard` (p. 597, ligne 28960) ET `Coinbase ; x402 Foundation (2025-2026). x402` (p. 597, ligne 28963) | Même standard HTTP 402 / x402 | **Triplon consécutif** sur la même page. |
| `Courtney et al. (2026). Agent Name Service v2 (ANS)` (p. 599, ligne 29046) | `Courtney et al. (2026). Agent Name Service v2 (ANS)` (p. 599, ligne 29049) | Même IETF draft `draft-narajala-courtney-ansv2-01` (13 avr. 2026) | **Doublon consécutif parfait** sur la même page. |
| `Derde & Alaerts (2020). Archi Banking Group` (p. 600, ligne 29130) | `Derde & Lankhorst (2020). Expressing BIAN Reference Model` (p. 601, ligne 29141) | Même étude de cas The Open Group BIAN/ArchiMate | Doublon partiel. |
| `Eclipse Foundation (2025). Eclipse LMOS Redefines Agentic AI` (p. 602, ligne 29208) | `Eclipse Foundation (Eclipse LMOS) (2025). Eclipse LMOS Redefines Agentic AI` (p. 602, ligne 29215) | Même communiqué Eclipse du 28 oct. 2025 | Doublon consécutif quasi-identique. |
| `EDM Council / OMG (2026). FIBO — Ontology Viewer` (p. 602, ligne 29230) | `EDM Council / OMG (2026). FIBO — dépôt de production` (p. 603, ligne 29239) | Même ontologie FIBO | Doublon de ressource. |
| `Cecchetti et al. (2025). Artificial intelligence and systemic risk. ESRB Report No 16` (p. 594, ligne 28830) | `European Systemic Risk Board ; Cecchetti et al. (2025). Artificial Intelligence and Systemic Risk` (p. 603, ligne 29266) | Même rapport ESRB Report No 16 (déc. 2025) | Doublon distant (lettre C vs lettre E). |
| `Board of Governors / OCC & FDIC (2011). SR 11-7` (p. 593, ligne 28764) | `Federal Reserve & OCC (2011). SR 11-7 / OCC Bulletin 2011-12` (p. 604, ligne 29298) | Même texte réglementaire historique SR 11-7 | Doublon distant (lettre B vs lettre F). |

Ce constat apporte la **preuve empirique incontestable que le nettoyage des bibliographies du Volume I n'a pas été exécuté selon les critères déclarés**. L'affirmation de la page 585 selon laquelle « 198 doublons ont été fondus » masque le fait que des doublons triviaux subsistent en masse dans le corps du texte.

---

## 4. Matrice détaillée des défauts (Bloquant, Majeur, Mineur)

Le tableau suivant récapitule l'ensemble des défauts constatés sur le segment, classés par ordre de sévérité décroissante :

| ID | Sévérité | Localisation exacte | Description & Citation textuelle | Diagnostic causal | Correctif explicite |
|---|---|---|---|---|---|
| **DEF-01** | **Bloquant / Majeur** | Page 585, lignes 28388-28394 / image `page-585.png` | **Tableau tronqué et puce orpheline** : Les cellules des lignes « Doublons fondus » et « Entrées uniques » sont vides dans le tableau rendu. En dessous du tableau apparaît la puce textuelle isolée `• 134 1065`. De plus, l'arithmétique est fausse ($1\,263 - 134 = 1\,129 \neq 1\,065$). | Débordement de boîte lors de la compilation typographique (LaTeX/Typst) où les cellules de tableau ont glissé hors du tableau sous forme de bloc de texte brut ; incohérence des calculs de dédoublonnage. | Réintégrer `198` dans la cellule « Doublons fondus » et `1065` dans la cellule « Entrées uniques » (vérifiant $1263 - 198 = 1065$). Supprimer la puce orpheline `• 134 1065`. |
| **DEF-02** | **Majeur** | Annexe I.1, pp. 586-604 (17 occurrences relevées) | **Présence massive de doublons consécutifs et redondances non fondues** : Ex. deux fois consécutives `Anthropic (2024). Introducing the Model Context Protocol` (p. 588) ; deux fois `Courtney et al. ANS v2` (p. 599) ; trois fois `EchoLeak` (p. 587) ; deux fois `Aldasoro et al. BIS 1194` (p. 587). | Échec du script d'ingestion et de fusion des 7 bibliographies sources du Volume I, qui n'a pas normalisé les titres ni comparé les chaînes d'URLs identiques. | Exécuter un script de dédoublonnage strict par URL canonique et par titre normalisé (Levenshtein < 0,1) pour purger les 17 doublons identifiés et ajuster le compte d'entrées uniques. |
| **DEF-03** | **Majeur** | Annexe I.2, p. 651, lignes 59260-59300 | **Asymétrie bibliographique unilatérale (Non-consolidation des Vol. II et III)** : « L’annexe ne réunit donc pas trois bibliographies — elle en réunit une, et constate l’absence des deux autres » (lignes 59278-59280). 89,3 % des faits du socle n'ont aucune notice bibliographique. | Les monographies sources des volumes II et III ont été rédigées avec des citations en prose sans identifiants pérennes (DOI/URL), empêchant leur intégration automatique à l'Annexe I. | Rétro-annoter les sources primaires des 142 entrées de socle des Vol. II et III (S-001 à S-142) avec des identifiants normalisés (URLs, DOIs, références d'éditeurs) et publier une véritable sous-section I.2 consolidée. |
| **DEF-04** | **Majeur** | Annexe B, p. 583-584, lignes 53090-53120 & corps du texte (ch. 38, 39, 40) | **Citations fantômes et exclusion de faits primaires** : `Vol. III F-92` et `Vol. III F-96` sont exclus de l'Annexe B (la numérotation saute de F-91 à F-93 et de F-95 à F-97), mais continuent d'être cités verbatim dans le corps du texte (ex. p. 438, p. 447). | Exclusion tardive de F-92 et F-96 pour « vote adversarial non conduit » sans avoir nettoyé les renvois correspondants dans les chapitres d'architecture d'AgentOps. | Soit intégrer formellement F-92 et F-96 dans l'Annexe B (en passant le total de Vol. III à 98 entrées), soit supprimer les mentions de `F-92` et `F-96` dans les chapitres 38, 39 et 40 en les remplaçant par des constats d'auteur. |
| **DEF-05** | **Majeur** | Annexe B, p. 584, lignes 53120-53155 | **Faiblesse probatoire des 17 entrées du Volume I** : Les entrées S-143 à S-159 sont toutes de niveau [C] (repérage non extrait, non rejouable), dont plusieurs faits négatifs non rejouables (S-153, S-154, S-156, S-158). | Absence d'extraction primaire et de vote adversarial sur le Volume I lors de la phase de consolidation du socle (Volume IV). | Élever le niveau de preuve des thèses fondamentales de S-143 à S-159 en menant un vote contradictoire formel et en extrayant les sources primaires dans le dépôt. |
| **DEF-06** | **Majeur** | Annexe B, pp. 578-580 & p. 584 | **Gaps de traçabilité dans la table d'héritage H et les faits F du Vol. II** : Sauts de numérotation non documentés entre F-11 et F-15 (F-12, F-13, F-14 absents) ; absence de $H\text{-}13$ et $H\text{-}16$ ; citation répétée de $H\text{-}15$ dans le texte bien qu'exclu du socle. | Fusion imparfaite des registres de travail internes des monographies intermédiaires. | Ajouter une note méthodologique en tête de l'Annexe B explicitant le sort de F-12 à F-14, normaliser le statut de $H\text{-}15$ et combler les lacunes d'indexation $H\text{-}13$ / $H\text{-}16$. |
| **DEF-07** | **Majeur** | Annexe N, p. 661, ligne 60767-60768 | **Inopposabilité par absence des volumes sources I, II et III au dépôt** : « et les renvois aux volumes I à III, absents du dépôt » (ligne 60768). | Choix de publication de ne verser au dépôt public que le Volume IV (Compendium) et la Note AMF IA, conservant les volumes 1 à 3 en privé. | Verser les fichiers sources ou des extraits d'audit des Volumes I, II et III dans un sous-répertoire d'archive du dépôt (`documents/sources_anciennes/`) pour permettre la vérification indépendante. |
| **DEF-08** | **Mineur** | Annexe I.1, pp. 586-650 (occurrences multiples) | **Césures douces (soft hyphens `\u00ad` ou `&#8203;`) brisant les URLs** : De nombreuses URLs contiennent des tirets invisibles ou des césures typographiques (ex. `a2a-​protocol.org`, `accenture-​technology-​vision`). | Paramétrage de coupure automatique de mots du moteur de rendu typographique appliqué indistinctement aux blocs de texte et aux URLs. | Encapsuler systématiquement les URLs dans des balises préservant l'intégrité brute (blocs `\url{}` ou `verbatim`) sans césure typographique logicielle. |
| **DEF-09** | **Mineur** | Annexe I.1, p. 588, lignes 28532-28542 | **Incohérence des suffixes de lettres de date d'Anthropic** : Présence de `Anthropic (2025b)`, `(2025c)`, `(2025d)`, `(2025e)` sans qu'aucune entrée `Anthropic (2025a)` n'apparaisse auparavant pour l'entité générique (seule `Anthropic (Lynch et al.) (2025a)` est listée p. 589). | Re-tri alphabétique imparfait après fusion de plusieurs bibliographies partielles. | Harmoniser les suffixes chronologiques d'Anthropic 2025 (`2025a` à `2025d`). |
| **DEF-10** | **Mineur** | Annexe N, p. 653, ligne 59570 & p. 657, ligne 60420 | **Discordance d'horodatage sur A2A v1.1.0-rc** : Le texte du corps écrit « rien n'a bougé au 29 octobre 2026 » alors que le commit/tag `v1.1.0-rc` a été posé le 29 octobre à 12 h 05 UTC. | Relevé effectué le matin du 29 octobre avant la pose de l'étiquette par les mainteneurs du projet A2A. | L'Annexe N consigne déjà l'écart avec précision ; acter la correction dans le corps du chapitre 8 lors de la prochaine révision. |

---

## 5. Liste des travaux fondamentaux et standards omis jusqu'en 2026

L'actualisation de l'état de l'art scientifique et technique jusqu'à la fin 2026 met en lumière plusieurs lacunes bibliographiques significatives dans le Compendium. L'intégration des travaux ci-dessous est recommandée pour asseoir la solidité des prochains tirages :

### 5.1 Systèmes distribués, runtime d'inférence et gestion de mémoire agentique
1. **Kwon, W., Li, Z., Zhuang, S. et al. (2023)**. *Efficient Memory Management for Large Language Model Serving with PagedAttention*. In *Proceedings of the 29th ACM Symposium on Operating Systems Principles (SOSP '23)*, pp. 611-626. DOI: `10.1145/3600006.3613165`.  
   *Justification d'omission* : Le Compendium cite le produit `vLLM (2026)` sous forme d'une notice commerciale vague (p. 638), mais omet l'article séminal de SOSP 2023. PagedAttention est pourtant le fondement algorithmique indispensable pour comprendre le partage de contexte et la réduction de mémoire KV-cache dans les systèmes multi-agents concurrents.
2. **Zheng, L., Yin, L., Xie, Z. et al. (2024)**. *SGLang: Efficient Execution of Structured Language Model Programs*. arXiv:2312.07104 (présenté à NeurIPS 2024).  
   *Justification d'omission* : Totalement absent du manuscrit. SGLang a introduit l'algorithme *RadixAttention* (réutilisation systématique du KV-cache sur les arbres de prompts partagés), qui est la référence absolue de l'industrie en 2025-2026 pour l'exécution d'agents chaînés et d'arbres de raisonnement.
3. **Qin, Y. et al. (2024-2025)**. *Mooncake: A KVCache-Centric Disaggregated Architecture for LLM Serving*. In *USENIX FAST '25* / arXiv:2407.00079.  
   *Justification d'omission* : Absent. Mooncake est l'architecture de référence pour le désaccouplement calcul/mémoire dans les clusters d'agents d'entreprise à haut débit.

### 5.2 Sécurité formelle, confinement et robustesse face aux injections de prompts
4. **Chen, S., Piet, J., Sitawarin, C., Wagner, D. (2024-2025)**. *StruQ: Defending Against Prompt Injection with Structured Queries*. In *34th USENIX Security Symposium (USENIX Security '25)* / arXiv:2402.06363.  
   *Justification d'omission* : Bien que le manuscrit consacre deux chapitres entiers (ch. 11 et ch. 19) à la taxonomie des injections indirectes et aux attaques de type « Confused Deputy », il omet la principale solution architecturale moderne : StruQ, qui sépare structurellement le canal d'instructions du canal de données par des délimiteurs typés et un entraînement contrastif.
5. **Abdelnabi, S., Greshake, K., Salem, S., Fritz, M. (2023-2024)**. *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. In *IEEE Symposium on Security and Privacy (S&P 2024)*.  
   *Justification d'omission* : L'article fondateur du benchmark BIPIA, systématiquement cité dans les référentiels OWASP et NIST, manque dans l'Annexe I.1.

### 5.3 Identité décentralisée, cryptographie et mandats programmables sur chaînes de blocs
6. **Buterin, V., De, D., Kristensen, K., et al. (2023-2024)**. *ERC-4337: Account Abstraction Using Alt Mempool*. Ethereum Improvement Proposal.  
   *Justification d'omission* : Alors que le compendium cite `ERC-8004 (Trustless Agents)` en page 600, il omet ERC-4337, qui est le standard industriel sous-jacent permettant de doter les agents autonomes de portefeuilles programmables avec limites de dépenses (*session keys*), politiques de signature multi-parties et révocation de mandats opposables.

### 5.4 Sûreté multi-agents, coordination et modélisation de la confiance
7. **Dafoe, A., Hughes, E., Bachrach, Y., et al. (2021-2024)**. *Cooperative AI: Machines Must Learn to Find Common Ground*. *Nature*, 593, pp. 33-36. DOI: `10.1038/d41586-021-01170-0`.  
   *Justification d'omission* : Texte programmatique indispensable pour étayer formellement le théorème de non-compositionnalité du chapitre 6 et justifier l'obligation d'un encadrement déterministe (OO4).
8. **Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., Bernstein, M. S. (2023)**. *Generative Agents: Interactive Simulacra of Human Behavior*. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*, pp. 1-22. DOI: `10.1145/3586183.3606763`.  
   *Justification d'omission* : L'architecture fondatrice associant mémoire épisodique, réflexion et planification d'agents autonomes, précurseur direct des architectures agentiques d'entreprise.

---

## 6. Conclusion et recommandations pour le rapport consolidé

1. **Restauration immédiate de la page 585** : La correction de la table de dédoublonnage de l'Annexe I est prioritaire pour la publication. Le tableau doit afficher `198` doublons fondus et `1065` entrées uniques, en éliminant la puce textuelle parasite `• 134 1065`.
2. **Exécution d'une passe de dédoublonnage réel sur l'Annexe I.1** : Les 17 doublons documentés ci-dessus doivent être purgés pour faire coïncider les faits observables avec les prétentions méthodologiques de l'ouvrage.
3. **Résolution du statut des citations fantômes ($F\text{-}92$, $F\text{-}96$, $H\text{-}15$)** : L'auteur doit trancher le statut de ces références dans les chapitres 38 à 43 pour éliminer toute incohérence avec l'Annexe B.
4. **Constitution d'une bibliographie minimale pour les Volumes II et III** : Pour assurer la conformité avec les exigences de révision des régulateurs financiers (BSIF, AMF), les sources primaires des 142 faits de socle des Vol. II et III doivent recevoir des adresses résolubles.
