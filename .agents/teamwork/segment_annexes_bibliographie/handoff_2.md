# Rapport d'Audit Critique — Segment Annexes et Bibliographie (Candidat 2)
**Document audité** : *Interopérabilité et Orchestration en Entreprise Agentique* (Compendium 2026, André-Guy Bruneau M.Sc. IT).  
**Segment assigné** : `segment_annexes_bibliographie` (Pages 584 à 663 — S54 à S60).  
**Périmètre spécifique Candidat 2** : Focus chirurgical sur les entrées bibliographiques 151 à 350 (pp. 595-608) et les pages 606 à 640 (entrées 319 à 883) de l'Annexe I.1 ; vérification des standards techniques (RFC IETF, W3C, ISO/NIST) ; détection des hallucinations, faux DOI, doublons et anachronismes ; audit de l'appareil critique (Annexe B, Annexe I.2, Annexe N) ; inventaire des travaux fondamentaux omis jusqu'en 2026.  
**Date d'évaluation** : Novembre 2026.

---

## 1. Résumé exécutif du segment et verdict global

Le segment des Annexes et de la Bibliographie (pp. 584-663) constitue l'infrastructure probatoire et réglementaire de l'ensemble du Compendium. Il réunit l'achèvement du répertoire des sources primaires (Annexe B, pp. 584-585), la Bibliographie générale consolidée (Annexe I, pp. 585-651), l'explication de non-consolidation des volumes II et III (Annexe I.2, p. 651), et l'Actualisation réglementaire et protocolaire au 1er novembre 2026 (Annexe N, pp. 652-663).

### Verdict Global : Réserves Majeures (Non-conformité structurelle de l'appareil critique et défaillance du dédoublonnage)

L'audit approfondi révèle un contraste saisissant entre la haute valeur empirique de certaines vérifications et de graves défaillances méthodologiques et formelles :

1. **Rupture de la promesse de consolidation (Annexe I & I.2)** : L'ouvrage affiche en titre une « Bibliographie générale consolidée », mais admet explicitement en Annexe I.2 (§ I.2, p. 651) qu'il ne s'agit que de la bibliographie du Volume I. Les Volumes II et III n'y versent strictement aucune entrée résoluble (0 référence). Les affirmations juridiques, prudentielles et d'architecture d'entreprise des Livres II et III reposent donc sur des citations en prose non résolubles par des tiers.
2. **Défaillance massive du dédoublonnage et bogue typographique d'assemblage (Annexe I.1, p. 585 et passim)** : Le protocole déclarait avoir fondu 134 doublons pour atteindre 1065 entrées uniques depuis 1263 entrées sources. Or, d'une part, l'arithmétique est incohérente ($1263 - 134 = 1129 \neq 1065$, soit un écart inexpliqué de 64 entrées), d'autre part, la page 585 présente un bogue visuel de composition où les chiffres `134 1065` ont été expulsés du tableau pour former une puce orpheline en bas de page. Plus grave encore, l'analyse automatique révèle **82 paires de quasi-doublons** non purgés dans le texte publié, incluant des triplicatas consécutifs (OAuth 2.1 répété 3 fois de suite, pp. 610-611) et des quadruplicatas (IETF WIMSE Architecture répété 4 fois consécutivement, p. 613).
3. **Pollution éditoriale par des notes internes non purgées** : Des fragments de consignes internes d'audit, de doutes de recherche ou de mémos (« Raison de l'écart : URL non confirmée... À sur le site Finastra », « fixer le numéro de version arXiv au moment de citer », « version finale à confirmer ») ont été imprimés textuellement au sein des notices bibliographiques définitives (ex. Finastra p. 605, Dun Yuan p. 650, EBA p. 602, Sparx Systems p. 640).
4. **Distorsion épistémologique du corpus (Axe R3)** : Malgré des ambitions théoriques fortes sur la décidabilité des politiques (ch. 48-49), la tolérance aux pannes byzantines, la composition multi-agents et la sécurité des protocoles, le corpus bibliographique présente un **vide total de la littérature de pointe en informatique théorique, systèmes et réseaux**. Les conférences phares STOC, FOCS, OSDI, ACM CCS, IEEE S&P et NDSS totalisent un score de zéro (0) article dans l'ensemble de l'Annexe I.1 (à l'exception unique d'un article de 1975 à SOSP et d'un atelier AISec à CCS). Le corpus est massivement sur-pondéré en prépublications arXiv volatiles et en billets de blogue marketing/analystes (Gartner, Bain, Forrester), au détriment des piliers académiques formels (Macaroons, moniteurs de sécurité de Schneider, consensus Raft, logique temporelle ATL).
5. **Bifurcation épistémologique non résolue de l'Annexe N** : L'Annexe N constitue un excellent travail d'actualisation factuelle au 1er novembre 2026 (réalisé par un agent LLM Claude sous consigne de source primaire), mais le protocole s'arrête au premier des trois gestes prescrits par le chapitre 50 : les entrées du socle (Annexe B) et les chapitres concernés (ch. 21, 27, 42, 49) ne sont pas modifiés. Il en résulte une scission interne : le corps de l'ouvrage affirme des propositions que l'annexe déclare périmées ou devenues fausses, sans aucun renvoi bidirectionnel dynamique dans le texte.

---

## 2. Évaluation détaillée Axe R2 (Appareil critique, Annexe B, Annexe I.2, Annexe N)

### 2.1 Annexe B — Répertoire des sources primaires (p. 584)

La page 584 clôt le répertoire des 159 faits de socle ($S-001$ à $S-159$). On y observe la ventilation suivante :
- **Volume II** : 46 entrées ($S-001$ à $S-046$).
- **Volume III** : 96 entrées ($S-047$ à $S-142$).
- **Volume I** : 17 entrées ($S-143$ à $S-159$).

#### Analyse critique des entrées $S-143$ à $S-159$ :
1. **Uniformité suspecte de niveau de preuve** : Les 17 entrées du Volume I sont toutes, sans exception, qualifiées de degré `[C]` (source prospective, projection ou citation interne), là où les volumes précédents comportaient des faits vérifiés de niveau `[A]` et `[B]`.
2. **Médiation systématique par le Volume III** : Toutes les entrées $S-143$ à $S-159$ sont indexées sous la formule « par Vol. III H-xx §7.3 ». Le Volume I ne s'adosse donc pas directement à des sources primaires autonomes dans ce socle, mais à des hypothèses prospectives répertoriées dans le Volume III.
3. **Aveu de citations non rejouables** :
   - $S-153$ (« L'invariant à quatre termes ») : mentionne textuellement *« Citation non rejouable »*.
   - $S-154$ (« La délégation au-delà de deux sauts ») : mentionne *« Citation non rejouable »*.
   - $S-156$ (« Le plan de contrôle obligatoire ») : mentionne *« Citation non rejouable »*.
   - $S-158$ (« Le cas fil rouge ») : mentionne *« Fait négatif non rejouable (cible supprimée) »*.
   Ce constat affaiblit substantiellement la prétention d'auditabilité scientifique du Compendium : des axiomes structurants (l'invariant de la somme, le problème des deux sauts) sont étiquetés dans le socle de faits comme impossibles à rejouer par un auditeur indépendant.
4. **Coquille de référencement interne ($S-158$)** : La notice $S-158$ porte une syntaxe tronquée : *« Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 »*, révélant une collision de balises lors de la génération.

### 2.2 Annexe I — Régime d'autorité et incohérence arithmétique (p. 585)

L'introduction de l'Annexe I (p. 585) définit le statut juridique et méthodologique du corpus :
- Elle stipule que l'annexe est une *« RÉUNION, non une vérification »*, chaque entrée étant reprise verbatim sans autorité propre.
- Le tableau récapitulatif présente les métriques d'assemblage :
  - Entrées relevées aux 7 bibliographies du Vol. I : **1263**
  - Doublons fondus par identifiant normalisé : **134** (valeur absente du tableau, rejetée hors-cadre)
  - Entrées uniques de la présente annexe : **1065** (valeur absente du tableau, rejetée hors-cadre)
  - Adresses primaires reprises des socles des Vol. II et III : **0**

#### Les deux défauts majeurs de la page 585 :
1. **Incohérence mathématique flagrante** :
   $$\text{Entrées uniques théoriques} = 1263 - 134 = 1129 \neq 1065$$
   Il existe un déficit de **64 entrées** ($1129 - 1065 = 64$) qui ont disparu entre le dépouillement et l'inventaire final sans qu'aucune règle d'élagage ne soit explicitée. Si 1065 est le décompte réel d'entrées uniques, le nombre de doublons fondus était de $1263 - 1065 = 198$ et non de 134.
2. **Bogue d'affichage et rupture typographique** :
   Dans l'image compilée (`page-585.png`), les cellules en regard de « Doublons fondus » et « Entrées uniques » sont totalement vides. Les nombres ont été éjectés sous le tableau sous la forme d'un paragraphe textuel incongru : `• 134 1065`. Ce défaut visuel nuit gravement à la présentation professionnelle du document.

### 2.3 Annexe I.2 — L'asymétrie documentaire structurelle (p. 651)

L'Annexe I.2 (§ I.2, p. 651), rédigée le 30 juillet 2026, documente avec lucidité une tare majeure du projet :
- Les Volumes II et III ne portaient aucune bibliographie formalisée, mais uniquement des mentions en prose dans leurs fiches de socle ($F-xx$).
- L'audit du 19 octobre 2026 a constaté qu'aucune adresse résoluble n'était récupérable automatiquement sans « déduire une adresse d'un nom d'éditeur », geste interdit par la rigueur de l'ouvrage.
- **Conséquence directe** : Le Compendium échoue à fournir une bibliographie consolidée de l'entreprise agentique. L'ensemble des développements sur la réglementation financière (Loi 25, BSIF E-23, DORA, AI Act), la jurisprudence (Moffatt c. Air Canada) et les architectures bancaires réelles repose sur des sources primaires introuvables dans l'index bibliographique principal.

### 2.4 Annexe N — Actualisation de novembre 2026 (pp. 652-663)

L'Annexe N applique le protocole de revalidation du chapitre 50 à la date du 1er novembre 2026 :
- **Transparence sur l'usage de l'IA** : L'annexe divulgue honnêtement que les relevés ont été conduits par un modèle Claude (Anthropic) avec consigne stricte de source primaire, un échantillon ayant été contre-vérifié manuellement.
- **Le problème de la non-répercussion dans le corps** :
  L'annexe explicite la règle : *« Un rapport de revalidation, non une reprise... Elle n'amende aucune entrée S-nnn et ne reprend aucun chapitre »*. Cela génère une dette de synchronisation :
  - Le tableau N.1 (pp. 653-655) ré-instruit les 14 événements du tableau 50.1 (ex. le retard du rail temps réel RTR de Paiements Canada, le statut du projet de loi fédéral C-36, la publication de NIST IR 8547 final en octobre 2026).
  - Mais le lecteur des chapitres 21, 33 ou 50 n'a aucun moyen de savoir que les faits qu'il lit sont qualifiés de « non actuels » ou « devenus faux » sans se reporter spontanément à l'Annexe N.
- **Rapports de la Note AMF IA (Section N.3, pp. 658-660)** :
  L'intégration de la Note AMF IA (`CRE-IA-2026-01-QC` du 31 octobre 2026) est minutieuse :
  - Première question ouverte du § 27.3 close : la ligne directrice finale de l'AMF est analysée (17 pages, 41 regroupements d'attentes, entrée en vigueur au 1er mai 2027).
  - Vide de socle du tableau 42.1 : la ligne AMF dispose désormais de son premier terme, mais les cellules d'intersection avec les protocoles (MCP, A2A, AP2) restent en suspens.
- **Lacunes d'actualisation non résolues (Section N.4, pp. 660-663)** :
  Plusieurs sources clés n'ont pu être jointes le 1er novembre 2026 en raison de blocages techniques documentés :
  - Site de l'AMF et PDF : Erreur HTTP 403 (Cloudflare/WAF).
  - EUR-Lex (Journal officiel de l'UE) : Réponse HTTP 202 sans contenu (date exacte du règlement d'exécution non confirmée).
  - Révision NIST SP 800-131A et échéances de la frise 49.1 non ré-ouvertes.

---

## 3. Évaluation détaillée Axe R3 (Vérifications bibliographiques et état de l'art 2024-2026)

L'audit approfondi par recherche Web (`search_web`) a porté sur l'échantillon obligatoire des entrées 151 à 350 (pp. 595-608) et sur les entrées des pages 606 à 640 (entrées 319 à 883).

### 3.1 Vérification de l'existence réelle des publications récentes (2024-2026)

Contrairement aux dérives fréquentes où des modèles génératifs hallucinent des références plausibles, les articles scientifiques récents cités dans ce segment correspondent à des publications authentiques et vérifiables :

1. **AITH — Délégation post-quantique (Entrée [164], p. 595)** :
   *Chen, Z. (2026). AITH: A Post-Quantum Continuous Delegation Protocol for Human-AI Trust Establishment. arXiv:2604.07695.*  
   -> **Vérifié réel** : Prépublication arXiv d'avril 2026 introduisant le protocole AITH basé sur les signatures post-quantiques ML-DSA-87 (FIPS 204), moteur de vérification à 6 étapes et révocation rapide en moins d'une seconde.
2. **Agent Network Protocol (Entrée [157], p. 595)** :
   *Chang, Gaowei et al. (2025). Agent Network Protocol (ANP) Technical White Paper. arXiv:2508.00007.*  
   -> **Vérifié réel** : Livre blanc déposé en juillet 2025 (arXiv:2508.00007) par Gaowei Chang, Eidan Lin et al., décrivant l'architecture 3 couches (DIDs, négociation de méta-protocole, couche application).
3. **StockBench (Entrée [163], p. 595)** :
   *Chen, Y., Yao, Z., Liu, Y. et al. (2025). StockBench: Can LLM Agents Trade Stocks Profitably in Real-World Markets? arXiv:2510.02209.*  
   -> **Vérifié réel** : Benchmark multi-mois d'agents financiers sur actions du DJIA (arXiv:2510.02209).
4. **Mem0 (Entrée [166], p. 596)** :
   *Chhikara, P., Khant, D., Aryan, S., Singh, T., Yadav, D. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv:2504.19413.*  
   -> **Vérifié réel** : Article introduisant Mem0 et Mem0g (graphe dynamique de mémoire avec résolution de conflits, p95 latence réduite de 91 %).
5. **Whispers of Wealth (Entrée [234], p. 600)** :
   *Debi, Tanusree ; Zhu, Wentian ; Sen Gupta, Pranjol (2026). Whispers of Wealth : Red-Teaming Google’s Agent Payments Protocol via Prompt Injection. arXiv:2601.22569.*  
   -> **Vérifié réel** : Red-teaming d'AP2 démontrant les attaques Branded Whisper et Vault Whisper sur Gemini-2.5-Flash.
6. **DeepSeek-R1 (Entrée [236], p. 600)** :
   *DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. Nature vol. 645, pp. 633-638, DOI:10.1038/s41586-025-09422-z.*  
   -> **Vérifié réel** : Publication conjointe arXiv:2501.12948 et Nature 2025 avec attribution exacte du DOI.
7. **ProtocolBench (Entrée [254], p. 601)** :
   *Du, Hongyi ; Su, Jiaqi ; Li, Jisen et al. (2025). Which LLM Multi-Agent Protocol to Choose? arXiv:2510.17149.*  
   -> **Vérifié réel** : Comparaison formelle de protocoles (JSON-RPC, A2A, ANP, ACP) et introduction du routeur dynamique ProtocolRouter.
8. **Agentifying Agentic AI (Entrée [247], p. 601)** :
   *Dignum, V., Dignum, F. (2025). Agentifying Agentic AI. arXiv:2511.17332.*  
   -> **Vérifié réel** : Plaidoyer méthodologique d'Umeå University pour réinjecter les modèles BDI et le design institutionnel d'AAMAS dans les agents LLM.
9. **Internet of Agents Cisco (Entrée [330], p. 606)** :
   *Fleming, C., Muscariello, L., Pandey, V., Kompella, R. (2025). A Layered Protocol Architecture for the Internet of Agents. arXiv:2511.19699.*  
   -> **Vérifié réel** : Article Cisco formalisant les couches L8 (Agent Communication) et L9 (Semantic Negotiation).
10. **SoK MCP Security (Entrée [342], p. 607)** :
    *Gaire, S., Gyawali, S., Mishra, S. et al. (2025). Systematization of Knowledge : Security and Safety in the Model Context Protocol Ecosystem. arXiv:2512.08290.*  
    -> **Vérifié réel** : Taxonomie unifiée des risques de sécurité (injection indirecte) et de sûreté (alignement, délégation d'outils).
11. **Réglementation bancaire US (Entrées [295]-[296], p. 604)** :
    *Federal Reserve, OCC & FDIC (2026). SR 26-2 / OCC Bulletin 2026-13 — Model Risk Management: Revised Guidance (17.4.2026).*  
    -> **Vérifié réel** : Révision majeure abrogeant formellement SR 11-7 au 17 avril 2026, avec exclusion explicite de l'IA générative et agentique du périmètre immédiat.
12. **Partenariat bancaire FIS / Anthropic (Entrée [326], p. 606)** :
    *FIS / Anthropic (2026). FIS Brings Agentic AI to Banking with Anthropic... 4.5.2026.*  
    -> **Vérifié réel** : Déploiement de l'agent de lutte contre le crime financier (AML) avec BMO et Amalgamated Bank, sous supervision humaine stricte.

### 3.2 Audit des standards techniques normatifs

L'audit confirme l'exactitude des désignations et des statuts des standards IETF, W3C, ISO et NIST :
- **OAuth 2.1** : Référencé sous `draft-ietf-oauth-v2-1-15` (mars 2026) dans le corps (pp. 610-611), puis re-daté à `draft-ietf-oauth-v2-1-17` (31 octobre 2026) en Annexe N ([AN-23]). Statut conforme : document en cours sur le Standards Track, non encore publié comme RFC.
- **IETF WIMSE** : Cité sous `draft-ietf-wimse-arch-07` dans le corps, et `draft-ietf-wimse-arch-08` en Annexe N. `draft-ietf-wimse-workload-identity-practices-08` correctement identifié comme étant en Last Call jusqu'au 13 novembre 2026 ([AN-12]).
- **IETF RFCs** :
  - **RFC 8693** (OAuth 2.0 Token Exchange, 2020) : Auteurs (Jones, Nadalin, Campbell, Bradley, Mortimore) et DOI exacts.
  - **RFC 9901** (Selective Disclosure for JWT / SD-JWT, 2025) : Publication et attribution conformes.
  - **RFC 9700** (OAuth 2.0 Security BCP, BCP 240, 2025) : Identifiant exact.
  - **RFC 9728** (OAuth 2.0 Protected Resource Metadata, 2025) : Standardisant la découverte de métadonnées de ressources, critique pour MCP.
  - **RFC 9745** (The Deprecation HTTP Response Header Field, 2025) : Exact.
  - **RFC 9449** (DPoP, 2023) et **RFC 9421** (HTTP Message Signatures, 2024) : Rigoureusement exacts.
- **W3C Standards** :
  - **DID v1.0** (Rec. 19 juillet 2022) et **DID v1.1** (Candidate Recommendation Snapshot du 5 mars 2026) : Dates et URLs conformes.
  - **Verifiable Credentials (VC)** : **VC Data Model v2.0** officiellement publié comme W3C Recommendation le 15 mai 2025 ; **VC Data Model v2.1** correctement référencé comme Working Draft du 22 octobre 2026 ([AN-9]).
- **NIST Post-Quantum** :
  - FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) publiés en août 2024.
  - NIST IR 8547 final (« Transition to Post-Quantum Cryptography Standards ») publié le 27 octobre 2026 (DOI:10.6028/NIST.IR.8547), dépréciant la crypto classique après 2030 et l'interdisant après 2035 ([AN-14]).

### 3.3 Défaillance critique : La prolifération des doublons non purgés

Bien que les sources soient réelles, le processus d'assemblage et de dédoublonnage de l'Annexe I.1 a échoué de manière spectaculaire. L'analyse révèle **82 paires de doublons immédiats ou quasi-immédiats**, dont voici les cas les plus probants :

| Entrée A | Entrée B | Nature de la duplication | Localisation |
|---|---|---|---|
| **Hardt et al. (2026)** — OAuth 2.1 draft-15 (2 mars 2026) | **Hardt et al. (2026)** — OAuth 2.1 draft-15 (mars 2026) | **Triplicata** : 3 entrées consécutives pour la même spécification (la 3e est en haut de la p. 611). | p. 610, lignes 55558, 55564 ; p. 611, ligne 55576 |
| **IETF WIMSE (2026)** — draft-wimse-arch-07 | **IETF WIMSE (2026)** — draft-wimse-arch-07 | **Quadruplicata** : 4 entrées pour le même draft WIMSE, dont 2 identiques au mot près. | p. 613, lignes 55796, 55802, 55806, 55812 |
| **Challapally et al. (2025)** (MIT NANDA) | **Challapally et al. (2025)** / MIT NANDA | Même rapport, URLs différentes (nanda.media.mit.edu vs mlq.ai). | p. 595, lignes 54130, 54136 |
| **Courtney et al. (2026)** — ANS v2 | **Courtney et al. (2026)** — ANS v2 | Entrées consécutives strictement identiques (l'une sans URL, l'autre avec URL). | p. 599, lignes 54496, 54502 |
| **FIDO Alliance (2026)** — AI Agent Interactions | **FIDO Alliance (2026)** — AI Agent Interactions | Même communiqué de presse d'avril 2026 sur AP2 et Verifiable Intent. | p. 604, lignes 55012, 55018 |
| **FSB (2025)** — Monitoring Adoption of AI... | **FSB (2025)** — Monitoring Adoption of AI... | Même rapport du FSB du 10 oct. 2025 (PDF P101025). | p. 605, lignes 55044, 55052 |
| **NIST AI RMF 1.0 (2023)** | **NIST AI RMF 1.0 (2023)** | Même document NIST AI 100-1 (l'un avec DOI, l'autre avec URL et chapitres). | p. 627, lignes 57072, 57076 |
| **NIST AI 600-1 GenAI Profile (2024)** | **NIST AI 600-1 GenAI Profile (2024)** | Même profil NIST AI 600-1 du 26 juillet 2024 en double consécutif. | p. 627, lignes 57082, 57086 |
| **W3C Trace Context Level 1 (2021)** | **W3C Trace Context Level 1 (2021)** | Deux notices identiques au mot près, l'une sans lien, l'autre avec lien. | p. 646, lignes 58740, 58744 |
| **Eclipse LMOS (2025)** — ADL | **Eclipse LMOS (2025)** — ADL | Même annonce de presse du 28 oct. 2025. | p. 602, lignes 54802, 54816 |

**Diagnostic causal** : Le filtre de dédoublonnage s'est appuyé sur une correspondance exacte d'URL ou de DOI. Dès lors qu'une monographie source avait cité une ressource par son DOI et qu'une autre l'avait citée par son URL ou par son titre textuel, l'algorithme a échoué à les fusionner.

### 3.4 Présence inacceptable de notes internes de rédaction dans le texte publié

L'audit met au jour des traces évidentes de travail préparatoire et de commentaires d'auteurs non purgés lors de l'assemblage :

1. **Finastra (Entrée [309], p. 605, ligne 55068)** :
   > *« ...how-agentic-ai-is-transforming-retail-banking — **Raison de l’écart : URL non confirmée par recherche, slug ne correspondant pas exactement au titre annoncé, page Viewpoints non datée et susceptible de changer. À sur le site Finastra et à citer avec date de consultation avant tout usage en §5.7/§5.11.** »*
   Une phrase incomplète (« À sur le site Finastra ») et une consigne d'investigation interne ont été directement coulées dans le livre !
2. **Dun Yuan et al. (p. 650, ligne 59158)** :
   > *« arXiv:2604.02369. **[Prépublication : fixer le numéro de version arXiv au moment de citer.]** »*
   Consigne éditoriale brute demeurée entre crochets.
3. **South, Tobin et al. (Entrée [881], p. 640, ligne 58240)** :
   > *« **[Whitepaper OpenID et sa prépublication arXiv sont le même document ; entrée unique, cf. cat. 4 fusionnée ici.]** »*
4. **Sparx Systems (Entrée [882], p. 640, ligne 58244)** :
   > *« ...IA conversationnelle via tiers, **ex. Kernaro AI, à dater** »*
5. **EBA (Entrée [262], p. 602, ligne 54782)** :
   > *« ...consultation close 8.10.2025 ; **version finale à confirmer** »*

---

## 4. Matrice détaillée des défauts classés par sévérité

| Identifiant | Sévérité | Localisation exacte | Description & Diagnostic Causal | Correctif Explicite |
|---|---|---|---|---|
| **DEF-ANN-01** | **Bloquant** | p. 585 (Tableau & bas de page) | **Bogue typographique et incohérence arithmétique** : Les métriques de dédoublonnage sont éjectées hors du tableau sous forme de puce orpheline `• 134 1065`. De plus, $1263 - 134 = 1129 \neq 1065$ (écart inexpliqué de 64 entrées). | Réinsérer les valeurs dans les cellules du tableau. Rectifier le calcul : si 1065 entrées uniques sont conservées, indiquer $198$ doublons fondus ($1263 - 1065 = 198$), ou si 134 doublons ont été fondus, afficher $1129$ entrées uniques. |
| **DEF-ANN-02** | **Bloquant** | p. 651 (§ I.2) & p. 585 | **Rupture de la consolidation bibliographique** : L'Annexe I s'intitule « Bibliographie générale consolidée », mais n'intègre aucune référence des Volumes II et III (0 reprise). Les affirmations prudentielles, légales et d'architecture d'entreprise de ces volumes demeurent orphelines. | Renommer honnêtement l'annexe « Bibliographie du Volume I » OU intégrer un corpus résolu pour les sources des Volumes II et III (adresses institutionnelles AMF, BSIF, jurisprudence, standards). |
| **DEF-ANN-03** | **Majeur** | pp. 610-611, 613, 627 (Annexe I.1) | **Multiplicatas consécutifs non purgés** : Présence de triplicatas (OAuth 2.1, pp. 610-611) et quadruplicatas (IETF WIMSE, p. 613), ainsi que de 82 paires de doublons (NIST AI RMF, FIDO, Courtney ANS, Challapally). Falsifie la prétention de dédoublonnage de la p. 585. | Exécuter une passe de déduplication sémantique floue (fuzzy matching sur titre normalisé + auteurs) fusionnant les notices disposant d'un DOI et celles disposant d'une URL. |
| **DEF-ANN-04** | **Majeur** | p. 605, l. 55068 ; p. 650, l. 59158 ; p. 640, l. 58240 | **Pollution par des notes éditoriales internes** : Inclusion de commentaires bruts d'auteurs (« Raison de l'écart... À sur le site », « fixer le numéro de version », « fusionnée ici ») au sein des notices publiées. | Supprimer les métadonnées de travail et harmoniser les notices sous le format bibliographique standard de l'ouvrage. |
| **DEF-ANN-05** | **Majeur** | p. 584 (Annexe B, S-153, S-154, S-156, S-158) | **Faits de socle non vérifiables** : Quatre faits structurants du Volume I sont formellement étiquetés « Citation non rejouable » ou « Cible supprimée », ce qui ruine leur opposabilité scientifique. | Remplacer ces citations fermées par des références publiées ouvertes (ex. pour la délégation au-delà de deux sauts, référencer RFC 8693 ou AITH arXiv:2604.07695). |
| **DEF-ANN-06** | **Majeur** | pp. 652-663 (Annexe N) | **Bifurcation épistémologique du manuscrit** : L'Annexe N ré-évalue les 14 événements du chapitre 50 sans modifier le socle (Annexe B) ni les chapitres 21, 27, 33, 42 et 49. Le corps contient des énoncés faux ou périmés sans avertissement textuel. | Ajouter dans les chapitres concernés des mentions de renvoi vers l'Annexe N (« Énoncé périmé au 1er novembre 2026, cf. Annexe N.2 ») ou exécuter la passe complète de reprise. |
| **DEF-ANN-07** | **Mineur** | p. 584, l. 53196 (S-158) | **Syntaxe de section tronquée** : « Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 ». | Nettoyer la chaîne pour afficher : « Vol. I, Monographie Annexe B, et Architecture de solutions §7.4.3 ». |
| **DEF-ANN-08** | **Mineur** | p. 627, l. 57072-57088 | **Redondance des profils NIST** : Double citation consécutive de NIST AI 100-1 et NIST AI 600-1 sous deux identités d'auteurs (« NIST » vs « NIST, U.S. Dept. of Commerce »). | Unifier sous l'autorité émettrice standard « NIST ». |

---

## 5. Liste des travaux fondamentaux omis jusqu'en 2026

Malgré un volume de 1066 notices, le Compendium souffre d'un angle mort critique : **l'omission quasi totale des conférences académiques majeures en systèmes d'exploitation, réseaux, sécurité et théorie informatique (SOSP, OSDI, ACM CCS, IEEE S&P, NDSS, STOC, FOCS)**. Alors que l'ouvrage prétend fonder une ingénierie déterministe d'entreprise (OO4) et une architecture Zero Trust pour agents, il s'appuie presque exclusivement sur des prépublications arXiv de 2024-2026 et omet les fondations théoriques évaluées par les pairs :

### 5.1 Sécurité des systèmes et délégation d'autorité (ACM CCS / IEEE S&P)
1. **Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., & Vrable, M. (ACM CCS 2014)** : *Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud*.  
   *Pourquoi cette omission affaiblit le livre* : Le Compendium consacre les chapitres 12 à 17 à la délégation de mandat, aux jetons d'atténuation et aux contraintes contextuelles. Les Macaroons constituent la base cryptographique formelle de l'atténuation de tokens sans état et de la délégation chaînée à preuve contextuelle. Ne pas les citer prive l'ouvrage de son ancrage canonique.
2. **Schneider, Fred B. (ACM TISSEC 2000)** : *Enforceable Security Policies*.  
   *Pourquoi cette omission affaiblit le livre* : Au cœur des chapitres 37, 48 et 49 se trouve l'architecture PEP/PDP et la formalisation du filtrage des actions de l'agent. Le théorème de Schneider définit mathématiquement ce qui est exécutable par un moniteur de référence (les propriétés de sûreté / *safety properties* vs les propriétés de vivacité / *liveness properties*). L'absence de Schneider affaiblit le « Théorème de Décidabilité des Politiques » formulé au chapitre 48.
3. **Greshake, K. et al. (ACM CCS / AISec 2023)** : Bien que mentionné en fin de bibliographie (p. 609), le compendium omet les travaux fondateurs d'IEEE S&P sur la sécurité du contrôle d'accès dans les architectures orientées mandats (ex. *Capabilities and Confused Deputies* dans les architectures modernes).

### 5.2 Systèmes distribués, consensus et transactions (OSDI / SOSP / VLDB)
1. **Ongaro, D., & Ousterhout, J. (USENIX ATC 2014)** : *In Search of an Understandable Consensus Algorithm (Raft)*.  
   *Pourquoi cette omission affaiblit le livre* : Le Compendium cite le résultat négatif classique FLP (Fischer, Lynch, Paterson 1985, p. 606), mais n'inclut aucune référence sur le consensus moderne pratique régissant les registres distribués d'agents et la synchronisation de clusters (Raft ou Paxos moderne).
2. **Corbett, J. C. et al. (USENIX OSDI 2012)** : *Spanner: Google’s Globally-Distributed Database*.  
   *Pourquoi cette omission affaiblit le livre* : Crucial pour les transactions distribuées cohérentes avec horloges synchronisées (TrueTime), indispensable pour confronter le paradigme transactionnel Saga du chapitre 48.
3. **Helland, P., & Campbell, D. (CIDR 2009)** : *Building on Quicksand*.  
   *Pourquoi cette omission affaiblit le livre* : C'est le texte séminal démontrant pourquoi les transactions ACID traditionnelles sont impossibles dans les systèmes autonomes hautement distribués et justifiant l'obligation des modèles de compensation par entités autonomes.

### 5.3 Informatique théorique, logique et vérification multi-agents (STOC / FOCS / LICS)
1. **Alur, R., Henzinger, T. A., & Kupferman, O. (FOCS 1997 / Journal of the ACM 2002)** : *Alternating-time Temporal Logic (ATL)*.  
   *Pourquoi cette omission affaiblit le livre* : L'ouvrage mobilise la vérification de politiques et cite les automates d'interface (de Alfaro & Henzinger 2001), mais ignore l'ATL, qui est la logique temporelle formelle standard permettant de vérifier les propriétés stratégiques dans les systèmes multi-agents où des coalitions d'agents coopèrent ou rivalisent.
2. **Nisan, N., Roughgarden, T., Tardos, É., & Vazirani, V. (2007)** : *Algorithmic Game Theory* (Cambridge University Press).  
   *Pourquoi cette omission affaiblit le livre* : Les topologies d'essaims et de marchés du Livre I (ch. 6) et les mécanismes d'arbitrage financier manquent d'ancrage dans la théorie des jeux algorithmique et la conception de mécanismes incitatifs.

### 5.4 Standards normatifs ouverts (W3C / OpenID / ISO)
1. **OpenID Foundation (2024-2026)** : *OpenID for Verifiable Credential Issuance (OID4VCI)* et *OpenID for Verifiable Presentations (OID4VP)*.  
   *Pourquoi cette omission affaiblit le livre* : Le Compendium cite abondamment les livres blancs conceptuels d'OpenID AIIM, mais omet les spécifications normatives concrètes qui lient aujourd'hui OAuth 2.0 / OIDC aux Verifiable Credentials du W3C dans les portefeuilles d'identité numérique d'entreprise.

---

## 6. Conclusion et recommandations

L'appareil critique du Compendium démontre un travail de collecte considérable et une veille pointue sur les prépublications de 2025-2026. Cependant, la présence de 82 paires de doublons non purgés, de bogues de composition visuelle sur la page 585, de notes internes orphelines, et l'absence totale de consolidation des Volumes II et III dégradent la crédibilité académique de l'ouvrage.

**Actions correctives immédiates recommandées** :
1. Nettoyer les doublons dans l'Annexe I.1 et fusionner les notices en doublon (OAuth 2.1, WIMSE, NIST, Courtney ANS, Challapally).
2. Purger immédiatement les 5 notes internes résiduelles (Finastra, Dun Yuan, South, Sparx Systems, EBA).
3. Corriger le tableau de la page 585 en réintégrant les nombres dans leurs cellules respectives et en résolvant l'équation arithmétique ($1263 - 198 = 1065$).
4. Clarifier la portée de l'Annexe I en mentionnant explicitement en titre « Bibliographie du Volume I » tant que le dépouillement des Volumes II et III n'est pas réalisé.
5. Enrichir la bibliographie avec les 6 piliers académiques omis (Macaroons de Birgisson, Schneider 2000, Raft d'Ongaro, Helland 2009, Spanner de Corbett, ATL d'Alur & Henzinger).
