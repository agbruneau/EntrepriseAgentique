# Plan de Revue Exhaustif et Contradictoire — Compendium (2026)
**Document audité** : `documents/Compendium.pdf` (*Interopérabilité et Orchestration en Entreprise Agentique*, André-Guy Bruneau M.Sc. IT, Édition Novembre 2026, 663 pages).  
**Statut** : Plan de partitionnement, cartographie structurelle, table des symboles/axiomes et matrice d'orchestration (Phase 1).  
**Date de gel des faits** : 27 juillet 2026 (Actualisation 1er novembre 2026).

---

## 1. Table des matières complète et structure globale du manuscrit

Le compendium est structuré en cinq Livres doctrinaux et techniques majeurs, complétés par trois annexes critiques (dont une bibliographie générale consolidée et l'actualisation réglementaire de novembre 2026).

### 1.1 Architecture en Livres et Grands Mouvements

| Livre / Partie | Titre & Thématique Centrale | Plage de Pages | Chapitres Inclus | Thèse Directrice |
|---|---|---|---|---|
| **Front Matter** | Titre, mentions légales, division générale, Table des matières | pp. 1-4 | Liminaires | Positionnement des 5 livres et principes de gel documentaire au 27 juillet 2026. |
| **Livre I** | **Coopérer** : Fondements de l’interopérabilité et couche protocolaire agentique | pp. 5-139 | Chapitres 1 à 11 | L’interopérabilité n’est pas un état mais une propriété à maintenir dans le temps sous contrainte de découplage, contrat et évolution. |
| **Livre II** | **Faire confiance** : Identité non humaine et délégation vérifiable | pp. 140-251 | Chapitres 12 à 21 | Établissement d’un passeport d’agent opposable, résistance en environnement hostile et crypto-agilité post-quantique. |
| **Livre III** | **Encadrer** : Orchestration déterministe en entreprise et régulation financière | pp. 252-419 | Chapitres 22 à 36 | Autonomie sous contrôle de finalité : conciliation de l’orchestration APM (OO1-OO4) avec les normes BSIF E-23, Loi 25, AMF IA et ISO 20022. |
| **Livre IV** | **Appliquer, exploiter, produire et composer** : AgentMesh, AgentOps et architecture | pp. 420-526 | Chapitres 37 à 46 | Maillage zero trust (PEP/PDP), observabilité runtime, fabrique d’agents réémissible et modélisation formelle ArchiMate. |
| **Livre V** | **Livrer et clore** : L’agent comme artefact logiciel, sémantique d’effet et prospective | pp. 527-577 | Chapitres 47 à 50 | Provenance de l’artefact, idempotence et compensation, horizons technologiques 2027-2032 et protocole de revalidation. |
| **Annexes** | Références sources, Bibliographie consolidée et Actualisation nov. 2026 | pp. 578-663 | Annexes B, I, N | Registre exhaustif des sources primaires S-001 à S-159, corpus bibliographique et intégration de la Note AMF IA. |

---

### 1.2 Table des Matières Détaillée des 50 Chapitres et Annexes

#### Livre I — Coopérer (pp. 5-139)
- **Ch. 1** (pp. 5-24) : *L’interopérabilité comme problème d’intégration d’entreprise* — Coût de la non-interopérabilité, dette d’intégration, couplage, contrat, évolution et modèles LCIM / ISO 11354.
- **Ch. 2** (pp. 25-35) : *Données, sémantique et ontologies* — Taxonomie des formats, GAV vs LAV, triplets RDF/OWL/SHACL, schémas canoniques et impuissance sémantique de l’agent sans contrat partagé.
- **Ch. 3** (pp. 36-45) : *Sécurité, identité et gouvernance de l’interopérabilité* — Modèle AAA hérité, frontière périmétrique vs Zero Trust, gouvernance des interfaces et registres.
- **Ch. 4** (pp. 46-60) : *L’ingénierie des systèmes agentiques : anatomie, raisonnement, outils* — Boucle Perception-Raisonnement-Action, ReAct, Plan-and-Solve, Tool Use et faillibilité stochastique.
- **Ch. 5** (pp. 61-69) : *Ancrage informationnel : mémoire, contexte, RAG agentique* — Mémoire de travail, fenêtres d'attention, dérive contextuelle, RAG vectoriel vs graphe ontologique.
- **Ch. 6** (pp. 70-78) : *Systèmes multi-agents, évaluation et sûreté* — Typologie des topologies (hiérarchique, marché, essaim), benchmarks de sûreté, alignement opérationnel.
- **Ch. 7** (pp. 79-88) : *Généalogie et gouvernance : des projets propriétaires aux standards ouverts* — Historique de FIPA-ACL aux protocoles contemporains, rôle des consortiums ouverts.
- **Ch. 8** (pp. 89-102) : *Anatomie : MCP (agent-outil) et A2A (agent-agent)* — Spécifications JSON-RPC 2.0 de MCP (Anthropic), sémantique de négociation A2A (Google / LF), contrats de transport SSE et stdio.
- **Ch. 9** (pp. 103-114) : *Découverte, registres, portabilité et pile protocolaire* — Annuaires dynamiques, DNS d'agents, métadonnées de capabilité, portabilité multi-cloud.
- **Ch. 10** (pp. 115-127) : *Transaction et infrastructure : AP2 et AGNTCY* — Agent Payment Protocol (AP2), protocole de routage sécurisé Cisco AGNTCY, rails de règlement.
- **Ch. 11** (pp. 128-139) : *Modes d’échec et taxonomie des risques protocolaires* — Désynchronisation d'état, rupture de contrat de schéma, injection indirecte via payloads protocolaires, boucles de récursion infinie.

#### Livre II — Faire confiance (pp. 140-251)
- **Ch. 12** (pp. 140-151) : *L’héritage et les standards étirés : un demi-siècle d’identités non humaines, puis OAuth, OIDC et SCIM face à l’agent* — Limites des Service Principals, faiblesses d'OAuth 2.0 face à l'autonomie dynamique.
- **Ch. 13** (pp. 152-159) : *L’identité décentralisée : VC, DID et la promesse du portable* — W3C Decentralized Identifiers (DID), Verifiable Credentials (VC), cryptographie asymétrique et ancrage d'identité.
- **Ch. 14** (pp. 160-166) : *La grille des cinq questions* — Qui émet ? Qui agit ? Qui répond juridiquement ? Quelle est la portée du mandat ? Quelle est la preuve cryptographique d'exécution ?
- **Ch. 15** (pp. 167-179) : *Émettre : Agent Card signée, annuaires, registres gouvernés* — Structure JSON signée de l'Agent Card, ancrage PKI, validation de signature et révocation.
- **Ch. 16** (pp. 180-188) : *Le passeport d’agent : synthèse d’un objet encore virtuel* — Spécification d'un passeport opposable fédérant identité d'entité, mandat utilisateur et attestation de pile logicielle.
- **Ch. 17** (pp. 189-200) : *La chaîne de mandat et le problème des deux sauts* — Démonstration de la rupture d'opposabilité lors de délégations imbriquées (A -> B -> C), token exchange RFC 8693 étendu.
- **Ch. 18** (pp. 201-209) : *Know Your Agent : la vérification d’agent tiers inter-domaines* — Procédure KYA calquée sur KYC/KYB pour l'admission d'agents externes en zone réglementée.
- **Ch. 19** (pp. 210-219) : *Taxonomie des attaques d’identité et de délégation* — Rug-pull d'Agent Card, substitution de clé, attaque du député confus (Confused Deputy), replay de Verifiable Presentations.
- **Ch. 20** (pp. 220-235) : *Usurpation, révocation et boucle défensive : du rug-pull à l’agentic SOC* — Détection temps réel des dérives de signature, listes de révocation dynamiques, SOC adapté aux entités logicielles autonomes.
- **Ch. 21** (pp. 236-251) : *L’horloge post-quantique : menace sur la pile identitaire, crypto-agilité et dette de migration* — Vulnérabilité de RSA et ECDSA face aux algorithmes de Shor, standards NIST FIPS 203/204/205 (ML-KEM, ML-DSA, SLH-DSA) appliqués aux certificats d'agents.

#### Livre III — Encadrer (pp. 252-419)
- **Ch. 22** (pp. 252-265) : *Options d’orchestration et paradigme APM : la taxonomie OO1-OO4 et l’autonomie encadrée* — Classification formelle de OO1 (Black-box autonome) à OO4 (Autonomie encadrée déterministe / State Machine formelle).
- **Ch. 23** (pp. 266-273) : *Les frameworks d’orchestration d’entreprise* — Analyse comparative (LangGraph, Semantic Kernel, AutoGen, CrewAI, Temporal, AWS Step Functions) face aux exigences de déterminisme.
- **Ch. 24** (pp. 274-296) : *Le passage à l’échelle de l’entreprise* — Modèles de concurrence, partitionnement d'état, gestion de file d'attente distribuée et isolation multi-tenant.
- **Ch. 25** (pp. 297-305) : *E-23 : le risque de modèle à l’ère de l’IA* — Application de la ligne directrice BSIF/OSFI E-23 aux modèles fondationnels et aux agents décisionnels.
- **Ch. 26** (pp. 306-310) : *Le vide fédéral : de C-27 à C-36* — Analyse de l'impact du retard législatif fédéral canadien (AIDA/C-27) et implications opérationnelles pour le secteur financier.
- **Ch. 27** (pp. 311-322) : *Québec : la ligne directrice IA de l’AMF et l’article 12.1 de la Loi 25* — Obligation d'avis préalable, explicabilité et traçabilité des décisions entièrement automatisées.
- **Ch. 28** (pp. 323-326) : *Valeurs mobilières : l’avis ACVM 11-348* — Encadrement des systèmes automatisés et conseils financiers algorithmiques par les autorités en valeurs mobilières.
- **Ch. 29** (pp. 327-334) : *Le pont : des contraintes réglementaires aux frames déterministes* — Traduction algorithmique des exigences juridiques en automates d'états finis vérifiables.
- **Ch. 30** (pp. 335-349) : *Le maillage réglementaire international et la normalisation institutionnelle* — NIST AI RMF, ISO/IEC 42001, EU AI Act et convergence réglementaire transfrontalière.
- **Ch. 31** (pp. 350-366) : *Le vertical financier : pourquoi l’agentique y est durcie* — Risque systémique, intégrité transactionnelle, séparation des pouvoirs et opposabilité juridique.
- **Ch. 32** (pp. 367-371) : *Le cadre des services bancaires axés sur le consommateur* — Open Banking canadien (FCAC) et mandat d'accès aux données financières par agent mandaté.
- **Ch. 33** (pp. 372-377) : *ISO 20022 : Lynx accompli, RTR visé* — Intégration de messages ISO 20022 (pacs, camt, pain) dans les pipelines de paiement automatisés.
- **Ch. 34** (pp. 378-395) : *Les sous-domaines financiers : banque, assurance, patrimoine* — Déclinaison de l'autonomie encadrée dans le prêt hypothécaire, la souscription d'assurance et la gestion discrétionnaire de portefeuille.
- **Ch. 35** (pp. 396-409) : *Études de cas : la production agentique canadienne (2025-2026)* — Retours d'expérience industriels sur les déploiements pilotes dans les banques de l'Annexe I.
- **Ch. 36** (pp. 410-419) : *Prospective : AP2 sur les rails canadiens ?* — Faisabilité de l'ancrage du protocole AP2 sur le système de paiement Lynx et RTR de Paiements Canada.

#### Livre IV — Appliquer, exploiter, produire et composer (pp. 420-526)
- **Ch. 37** (pp. 420-435) : *Le maillage d’agents : du service mesh au point d’application (PEP/PDP et zero trust agentique)* — Architecture PEP/PDP agentique, interception de trafic agent-agent, inspection de mandat en ligne.
- **Ch. 38** (pp. 436-445) : *L’observabilité agentique* — Télémétrie OpenTelemetry pour agents, traçabilité des graphes de raisonnement, span contexts et capture des états intermédiaires.
- **Ch. 39** (pp. 446-455) : *Le cycle de vie opérationnel : évaluation continue, dérive et incident* — Monitoring de dérive de raisonnement (reasoning drift), dégradation de calibration et gestion des pannes agentiques.
- **Ch. 40** (pp. 456-466) : *Les indicateurs de l’AgentOps et le FinOps des agents* — Métriques clés : Coût par tâche (CpT), consommation de tokens, taux de succès au premier passage, arbitrage coût/latence.
- **Ch. 41** (pp. 467-473) : *La fabrique d’agents : produire, certifier et réémettre le parc* — Pipeline CI/CD d'agents, tests de régression comportementale, certification de conformité et réémission automatique.
- **Ch. 42** (pp. 474-481) : *La matrice protocoles × exigences réglementaires* — Croisement matriciel rigoureux entre protocoles (MCP, A2A, AP2) et exigences (E-23, Loi 25, SOC 2, ISO 42001).
- **Ch. 43** (pp. 482-494) : *L’architecture de référence unifiée par couches* — Les 7 couches de la pile agentique d'entreprise (Infrastructure, Modèle, Protocole, Identité, Orchestration, Observabilité, Métier).
- **Ch. 44** (pp. 495-506) : *La formalisation ArchiMate* — Métamodèle ArchiMate 3.2 instancié pour les systèmes agentiques (éléments actifs, processus d'orchestration, objets de données et services).
- **Ch. 45** (pp. 507-519) : *Le blueprint instancié et son cycle de vie : de Boréalis au portefeuille IBM, puis la naissance, la vie et la mort d’un agent d’entreprise* — Étude de blueprint d'architecture complet d'un agent de réconciliation financière.
- **Ch. 46** (pp. 520-526) : *Instrumentation et feuille de route vers le 1ᵉʳ mai 2027* — Jalons de mise en conformité et trajectoire d'industrialisation du parc agentique.

#### Livre V — Livrer et clore (pp. 527-577)
- **Ch. 47** (pp. 527-537) : *L’artefact livré : provenance des composants et mise en service* — SBOM (Software Bill of Materials), signature de chaîne d'approvisionnement (SLSA/Sigstore) et validation d'intégrité de l'agent.
- **Ch. 48** (pp. 538-544) : *La sémantique d’effet : idempotence, compensation, réconciliation* — Conception transactionnelle des outils d'agents, gestion des effets de bord et patrons Saga pour actions distribuées.
- **Ch. 49** (pp. 545-567) : *L’horizon 2027-2032 et la frontière de la connaissance vérifiable* — Prospective technologique, limites de la décidabilité et frontière formelle de l'autonomie agentique en environnement critique.
- **Ch. 50** (pp. 568-577) : *Péremption et protocole de revalidation* — Critères de fin de vie d'un modèle ou agent, tests périodiques de recertification et protocole de décommissionnement.

#### Annexes (pp. 578-663)
- **Annexe B** (pp. 578-584) : *Liste des références* — Sources codifiées S-001 à S-046 (Vol. II), S-047 à S-142 (Vol. III) et S-143 à S-159 (Vol. I).
- **Annexe I** (pp. 585-651) : *Bibliographie générale consolidée* — Répertoire bibliographique exhaustif du Volume I (I.1) et explicitation des régimes documentaires distincts (I.2).
- **Annexe N** (pp. 652-663) : *Actualisation de novembre 2026* — Prise en compte de la Note AMF IA, revalidations du protocole du chapitre 50 et inventaire des éléments non revalidés.

---

## 2. Plan de Découpage Logique en 60 Segments

Conformément à la spécification stricte (segments de 10 à 15 pages avec un recouvrement exact de 2 pages entre segments adjacents), le compendium de 663 pages est découpé en exactement **60 segments logiques**.
- Longueur de chaque segment : **13 à 14 pages** (100% conforme à l'intervalle [10, 15]).
- Chevauchement entre segments $S_i$ et $S_{i+1}$ : **exactement 2 pages** ($start_{i+1} = end_i - 1$).
- Couverture : page 1 à page 663 intégrale sans omission ni troncation.

| ID | Plage Pages | Longueur | Chapitres Couverts | Livre / Partie | Catégorie | Instructions Ciblées d'Audit Contradictoire |
|---|---|---|---|---|---|---|
| **S01** | pp. 1-13 | 13 | Liminaires, Ch. 1 | Front Matter, Livre I | Methodology | Auditer la complétude de la table des matières, la cohérence du cadre pré-agentique, et falsifier la formule du coût d'intégration quadratique $N(N-1)/2$. |
| **S02** | pp. 12-24 | 13 | Ch. 1 | Livre I | Methodology | Vérifier la taxonomie du LCIM, les 5 facettes du couplage, et la solidité formelle des contrats d'interface face à l'hétérogénéité d'entreprise. |
| **S03** | pp. 23-35 | 13 | Ch. 1, Ch. 2 | Livre I | Methodology | Examiner la transition couplage -> sémantique. Évaluer la pertinence de GAV vs LAV et la résistance des ontologies OWL/SHACL dans les flux d'agents. |
| **S04** | pp. 34-46 | 13 | Ch. 2, Ch. 3, Ch. 4 | Livre I | Methodology | Analyser l'héritage AAA/IAM, la transition périmètre -> Zero Trust, et la définition anatomique de la boucle Perception-Raisonnement-Action. |
| **S05** | pp. 45-57 | 13 | Ch. 4 | Livre I | Methodology | Évaluer la robustesse des patrons ReAct et Plan-and-Solve face aux défaillances stochastiques des LLMs en utilisation d'outils. |
| **S06** | pp. 56-68 | 13 | Ch. 4, Ch. 5 | Livre I | Theory / Math | Auditer la modélisation de la mémoire agentique (court terme vs long terme), la dérive contextuelle et la perte d'ancrage informationnel en RAG. |
| **S07** | pp. 67-79 | 13 | Ch. 5, Ch. 6, Ch. 7 | Livre I | Argument & Analysis | Vérifier les protocoles d'évaluation multi-agents, les topologies d'essaim et la perspective historique des protocoles de communication multi-agents (FIPA). |
| **S08** | pp. 78-90 | 13 | Ch. 7, Ch. 8 | Livre I | Methodology | Examiner l'émergence des standards ouverts et disséquer l'anatomie protocolaire de MCP (Model Context Protocol, JSON-RPC 2.0). |
| **S09** | pp. 89-101 | 13 | Ch. 8 | Livre I | Methodology | Falsifier la comparaison MCP (agent-outil) vs A2A (agent-agent) : vérifier les garanties de typage, transport SSE/stdio et négociation de capacités. |
| **S10** | pp. 100-112 | 13 | Ch. 8, Ch. 9 | Livre I | Methodology | Auditer la découverte dynamique d'agents, les mécanismes de registres distribués et la gestion de la portabilité entre clouds hétérogènes. |
| **S11** | pp. 111-123 | 13 | Ch. 9, Ch. 10 | Livre I | Modeling | Vérifier la modélisation des transactions d'agents sous AP2 (Agent Payment Protocol) et l'infrastructure de routage réseau sécurisé Cisco AGNTCY. |
| **S12** | pp. 122-134 | 13 | Ch. 10, Ch. 11 | Livre I | Argument & Analysis | Auditer les hypothèses de concurrence d'AP2 et disséquer la taxonomie des risques protocolaires (injection indirecte, collision de verrous). |
| **S13** | pp. 133-145 | 13 | Ch. 11, Ch. 12 | Livre I, Livre II | Argument & Analysis | Évaluer la synthèse des modes d'échec du Livre I et analyser la crise des protocoles d'identité humaine (OAuth 2.0, OIDC, SCIM) appliqués aux agents. |
| **S14** | pp. 144-156 | 13 | Ch. 12, Ch. 13 | Livre II | Theory / Math | Falsifier l'adaptation des jetons de service OAuth aux entités autonomes et auditer la fondation cryptographique des identifiants décentralisés (W3C DID). |
| **S15** | pp. 155-167 | 13 | Ch. 13, Ch. 14, Ch. 15 | Livre II | Theory / Math | Vérifier la grille des cinq questions fondamentales d'attribution juridique et examiner la structure technique de l'Agent Card signée. |
| **S16** | pp. 166-178 | 13 | Ch. 15 | Livre II | Modeling | Auditer le cycle de vie des annuaires d'agents, les autorités d'émission de certificats et la gestion des révocations cryptographiques. |
| **S17** | pp. 177-189 | 13 | Ch. 15, Ch. 16, Ch. 17 | Livre II | Theory / Math | Analyser le concept de passeport d'agent opposable et disséquer formellement le problème des deux sauts dans la chaîne de mandat. |
| **S18** | pp. 188-200 | 13 | Ch. 17 | Livre II | Theory / Math | Falsifier la démonstration mathématique de rupture d'opposabilité dans les délégations récursives (A -> B -> C) et valider le correctif par token exchange. |
| **S19** | pp. 199-211 | 13 | Ch. 17, Ch. 18, Ch. 19 | Livre II | Argument & Analysis | Auditer la procédure Know Your Agent (KYA) et la taxonomie des attaques spécifiques aux architectures de délégation agentique. |
| **S20** | pp. 210-222 | 13 | Ch. 19, Ch. 20 | Livre II | Argument & Analysis | Vérifier la formalisation des attaques par substitution d'Agent Card (rug-pull) et la détection d'usurpation dans la boucle défensive Agentic SOC. |
| **S21** | pp. 221-233 | 13 | Ch. 20 | Livre II | Modeling | Évaluer l'architecture opérationnelle de l'Agentic SOC : métriques de compromission, détection d'anomalies de comportement et isolation de sous-graphes. |
| **S22** | pp. 232-244 | 13 | Ch. 20, Ch. 21 | Livre II | Theory / Math | Auditer l'impact de l'ordinateur quantique sur la chaîne d'identité des agents et la vulnérabilité des signatures ECDSA/Ed25519 actuelles. |
| **S23** | pp. 243-255 | 13 | Ch. 21, Ch. 22 | Livre II, Livre III | Theory / Math | Vérifier la feuille de route de migration vers les algorithmes post-quantiques NIST (ML-DSA, SLH-DSA) et introduire la taxonomie d'orchestration OO1-OO4. |
| **S24** | pp. 254-266 | 13 | Ch. 22, Ch. 23 | Livre III | Modeling | Falsifier la démonstration de supériorité de l'autonomie encadrée déterministe (OO4) et comparer les postulats d'orchestration APM. |
| **S25** | pp. 265-277 | 13 | Ch. 23, Ch. 24 | Livre III | Methodology | Auditer la critique comparative des frameworks d'orchestration (LangGraph, Semantic Kernel, Temporal) face aux exigences de déterminisme d'entreprise. |
| **S26** | pp. 276-288 | 13 | Ch. 24 | Livre III | Modeling | Vérifier les modèles de passage à l'échelle : persistance d'état distribué, isolation mémoire des agents et gestion de la concurrence à haut débit. |
| **S27** | pp. 287-299 | 13 | Ch. 24, Ch. 25 | Livre III | Argument & Analysis | Analyser les défaillances de passage à l'échelle et introduire l'application de la ligne directrice BSIF/OSFI E-23 sur le risque de modèle aux agents IA. |
| **S28** | pp. 298-310 | 13 | Ch. 25, Ch. 26 | Livre III | Argument & Analysis | Auditer la transposition des exigences E-23 (gouvernance, inventaire, validation indépendante) et analyser le vide législatif fédéral canadien (C-27/AIDA). |
| **S29** | pp. 309-321 | 13 | Ch. 26, Ch. 27 | Livre III | Argument & Analysis | Examiner les impacts de l'absence de loi fédérale et disséquer les exigences québécoises : Loi 25 (article 12.1) et Ligne directrice IA de l'AMF. |
| **S30** | pp. 320-332 | 13 | Ch. 27, Ch. 28, Ch. 29 | Livre III | Modeling | Auditer l'avis ACVM 11-348 et évaluer formellement le pont algorithmique traduisant les contraintes juridiques en frames déterministes. |
| **S31** | pp. 331-343 | 13 | Ch. 29, Ch. 30 | Livre III | Modeling | Vérifier la preuve de conformité mathématique par automates d'états finis et confronter le cadre aux standards internationaux (NIST AI RMF, ISO 42001). |
| **S32** | pp. 342-354 | 13 | Ch. 30, Ch. 31 | Livre III | Argument & Analysis | Analyser l'interopérabilité réglementaire internationale (EU AI Act vs US vs Canada) et justifier le durcissement extrême dans le vertical financier. |
| **S33** | pp. 353-365 | 13 | Ch. 31 | Livre III | Argument & Analysis | Auditer les exigences d'intégrité transactionnelle, de non-répudiation et de cloisonnement étanche des mandats en environnement financier régulé. |
| **S34** | pp. 364-376 | 13 | Ch. 31, Ch. 32, Ch. 33 | Livre III | Methodology | Vérifier l'articulation entre services bancaires axés sur le consommateur (FCAC), open banking et la modernisation des paiements ISO 20022 (Lynx). |
| **S35** | pp. 375-387 | 13 | Ch. 33, Ch. 34 | Livre III | Methodology | Analyser l'implémentation de la messagerie financière ISO 20022 (RTR) et disséquer les applications spécifiques aux sous-domaines bancaires et d'assurance. |
| **S36** | pp. 386-398 | 13 | Ch. 34, Ch. 35 | Livre III | Experiments | Auditer les cas d'usage en gestion de patrimoine et évaluer la représentativité des études de cas de production canadienne (2025-2026). |
| **S37** | pp. 397-409 | 13 | Ch. 35 | Livre III | Experiments | Falsifier les métriques de succès annoncées dans les études de cas bancaires canadiennes : vérifier le taux d'intervention humaine et les coûts réels. |
| **S38** | pp. 408-420 | 13 | Ch. 35, Ch. 36, Ch. 37 | Livre III, Livre IV | Modeling | Auditer la faisabilité prospective d'AP2 sur les rails canadiens et introduire l'architecture AgentMesh (PEP/PDP zero trust). |
| **S39** | pp. 419-431 | 13 | Ch. 37 | Livre IV | Modeling | Examiner la conception formelle du Policy Enforcement Point (PEP) et du Policy Decision Point (PDP) adaptés aux flux stochastiques d'agents. |
| **S40** | pp. 430-442 | 13 | Ch. 37, Ch. 38 | Livre IV | Experiments | Auditer le maillage zero trust et analyser la pile d'observabilité OpenTelemetry : capture des traces distribuées d'agents et contexte de raisonnement. |
| **S41** | pp. 441-453 | 13 | Ch. 38, Ch. 39 | Livre IV | Experiments | Falsifier les mécanismes de détection de dérive de raisonnement (reasoning drift) et les protocoles de gestion d'incidents agentiques en temps réel. |
| **S42** | pp. 452-464 | 13 | Ch. 39, Ch. 40 | Livre IV | Experiments | Auditer les métriques AgentOps et le cadre FinOps : vérifier la cohérence des formules de calcul du coût par tâche et de l'efficience de contexte. |
| **S43** | pp. 463-475 | 13 | Ch. 40, Ch. 41, Ch. 42 | Livre IV | Methodology | Vérifier l'architecture de la fabrique d'agents (CI/CD comportemental) et auditer la matrice protocoles × exigences réglementaires. |
| **S44** | pp. 474-486 | 13 | Ch. 42, Ch. 43 | Livre IV | Modeling | Falsifier les croisements de la matrice réglementaire et disséquer l'architecture de référence unifiée en 7 couches. |
| **S45** | pp. 485-497 | 13 | Ch. 43, Ch. 44 | Livre IV | Modeling | Auditer la formalisation ArchiMate 3.2 de la pile agentique : vérifier la conformité syntaxique et sémantique des diagrammes et métamodèles. |
| **S46** | pp. 496-508 | 13 | Ch. 44, Ch. 45 | Livre IV | Modeling | Examiner la traçabilité des éléments ArchiMate vers les composants runtime et analyser le blueprint d'architecture instancié (Boréalis / IBM). |
| **S47** | pp. 507-519 | 13 | Ch. 45 | Livre IV | Modeling | Falsifier le cycle de vie complet de l'agent d'entreprise décrit dans le blueprint : de l'instanciation initiale au décommissionnement sécurisé. |
| **S48** | pp. 518-530 | 13 | Ch. 45, Ch. 46, Ch. 47 | Livre IV, Livre V | Experiments | Auditer la feuille de route d'instrumentation vers mai 2027 et examiner la gestion de la provenance de l'artefact livré (SBOM, SLSA). |
| **S49** | pp. 529-541 | 13 | Ch. 47, Ch. 48 | Livre V | Theory / Math | Falsifier les garanties formelles de sémantique d'effet : analyser les preuves d'idempotence, de compensation (Saga) et de réconciliation d'état. |
| **S50** | pp. 540-552 | 13 | Ch. 48, Ch. 49 | Livre V | Theory / Math | Auditer la gestion des pannes partielles en environnements distribués et évaluer la vision prospective sur l'horizon technologique 2027-2032. |
| **S51** | pp. 551-563 | 13 | Ch. 49 | Livre V | Theory / Math | Examiner les limites épistémiques de la connaissance vérifiable, les limites de calculabilité et la décidabilité des politiques de sécurité d'agents. |
| **S52** | pp. 562-574 | 13 | Ch. 49, Ch. 50 | Livre V | Methodology | Auditer le protocole formel de revalidation et les critères objectifs de mise en péremption d'un modèle ou agent d'entreprise. |
| **S53** | pp. 573-585 | 13 | Ch. 50, Annexe B, Annexe I | Livre V, Annexes | Other | Vérifier les conditions de clôture du manuscrit, la structure du registre de références S-001 à S-159 et le régime de citation de l'Annexe I. |
| **S54** | pp. 584-596 | 13 | Annexe I (I.1) | Annexes | Other | Vérifier la conformité et la validité des entrées bibliographiques 1 à 70 du Volume I : identifier les hallucinations de citation et erreurs d'attribution. |
| **S55** | pp. 595-607 | 13 | Annexe I (I.1) | Annexes | Other | Auditer les entrées bibliographiques 71 à 150 : vérifier la correspondance des DOI, dates de publication et affiliations institutionnelles. |
| **S56** | pp. 606-618 | 13 | Annexe I (I.1) | Annexes | Other | Auditer les entrées bibliographiques 151 à 230 : confronter les citations aux articles originaux (STOC, NeurIPS, SOSP, RFC, W3C). |
| **S57** | pp. 617-629 | 13 | Annexe I (I.1) | Annexes | Other | Auditer les entrées bibliographiques 231 à 310 : identifier les biais de sélection ou omissions d'articles fondamentaux postérieurs à 2024. |
| **S58** | pp. 628-640 | 13 | Annexe I (I.1) | Annexes | Other | Auditer les entrées bibliographiques 311 à 390 : vérifier l'exactitude des sources normatives et des rapports industriels cités. |
| **S59** | pp. 639-651 | 13 | Annexe I (I.1, I.2) | Annexes | Other | Auditer la fin de la bibliographie consolidée et examiner la justification méthodologique de la non-consolidation des références des Vol. II et III. |
| **S60** | pp. 650-663 | 14 | Annexe I (I.2), Annexe N | Annexes | Other | Auditer l'Annexe N (Actualisation de nov. 2026) : vérifier la transcription de la Note AMF IA, la revalidation du chapitre 50 et l'inventaire des lacunes résiduelles. |

---

## 3. Table Exhaustive des Symboles, Axiomes et Définitions Globales

### 3.1 Table des Symboles, Acronymes et Notations

| Symbole / Acronyme | Domaine / Portée | Définition Formelle & Rôle Architectural dans le Compendium |
|---|---|---|
| **AAA** | Sécurité / IAM | *Authentication, Authorization, Accounting* : Modèle de sécurité traditionnel périmétrique mis en échec par l'autonomie dynamique de l'agent. |
| **A2A** | Protocoles | *Agent-to-Agent* : Protocole de communication et de négociation décentralisé entre agents autonomes (Linux Foundation / Google). |
| **AIDA** | Réglementation | *Artificial Intelligence and Data Act* : Projet de loi fédéral canadien (partie du projet de loi C-27) gelé en commission parlementaire. |
| **AMF** | Réglementation | *Autorité des marchés financiers* (Québec) : Régulateur provincial émetteur de la Ligne directrice sur la gouvernance de l'IA. |
| **AP2** | Protocoles / Finance | *Agent Payment Protocol* : Protocole transactionnel permettant à un agent d'exécuter un mandat de paiement opposable avec engagement cryptographique. |
| **APM** | Orchestration | *Agent Process Management* : Paradigme d'orchestration d'entreprise subordonnant l'autonomie stochastique à des règles déterministes. |
| **BSIF / OSFI** | Réglementation | *Bureau du surintendant des institutions financières* (Canada) : Régulateur prudentiel fédéral, auteur de la ligne directrice E-23. |
| **CpT** | FinOps / Métriques | *Cost per Task* : Coût économique total (tokens, inférence, stockage, réseau) pour l'exécution vérifiée d'une tâche d'agent. |
| **CWA** | Ontologies / Logique | *Closed-World Assumption* : Postulat selon lequel tout ce qui n'est pas affirmé comme vrai dans la base de connaissances est réputé faux. |
| **DID** | Identité Décentralisée | *Decentralized Identifier* (W3C) : Identifiant cryptographique persistant, mondialement unique et résoluble sans autorité centrale. |
| **E-23** | Réglementation | Ligne directrice du BSIF sur la gestion du risque de modèle, étendue aux modèles fondationnels et systèmes agentiques. |
| **FCAC / ACFC** | Réglementation | *Financial Consumer Agency of Canada* : Organisme supervisant le Cadre des services bancaires axés sur le consommateur (Open Banking). |
| **FSM** | Algorithmique | *Finite State Machine* : Automate d'états finis déterministe garantissant le respect strict des transitions permises en mode OO4. |
| **GAV** | Intégration de données | *Global-As-View* : Approche d'intégration où chaque concept global est défini comme une vue sur les sources locales. |
| **ISO 20022** | Norme bancaire | Norme internationale de messagerie financière riche (XML/JSON), socle des systèmes canadiens Lynx et RTR. |
| **KYA** | Identité / Sécurité | *Know Your Agent* : Cadre d'admission et de validation vérifiable de l'identité, du code et du mandat d'un agent tiers avant interconnexion. |
| **LAV** | Intégration de données | *Local-As-View* : Approche où chaque source locale est modélisée comme une vue sur un schéma global canonique. |
| **LCIM** | Théorie Interopérabilité | *Levels of Conceptual Interoperability Model* : Modèle de maturité en 7 couches (Technique, Syntactique, Sémantique, Pragmatique, Dynamique, Conceptuel). |
| **Loi 25** | Réglementation | Loi québécoise modernisant les dispositions sur la protection des renseignements personnels (notamment article 12.1 sur la décision automatisée). |
| **MCP** | Protocoles | *Model Context Protocol* (Anthropic) : Protocole ouvert standardisant l'exposition d'outils, de ressources et de prompts vers les modèles. |
| **ML-DSA / ML-KEM** | Cryptographie | Algorithmes cryptographiques post-quantiques normalisés par le NIST (FIPS 203 et 204), fondés sur les réseaux euclidiens (Module-Lattice). |
| **OO1 à OO4** | Orchestration | Taxonomie des options d'orchestration : de OO1 (Black-box autonome) à OO4 (Autonomie encadrée déterministe). |
| **OWA** | Ontologies / Logique | *Open-World Assumption* : Postulat selon lequel une affirmation non connue n'est pas fausse mais simplement indéterminée. |
| **PDP** | Architecture Zero Trust | *Policy Decision Point* : Composant décisionnel évaluant les requêtes de l'agent au regard des politiques de conformité. |
| **PEP** | Architecture Zero Trust | *Policy Enforcement Point* : Composant d'interception bloquant ou autorisant les appels d'outils et messages de l'agent. |
| **RTR** | Paiements Canada | *Real-Time Rail* : Système national de paiement de détail en temps réel d'heure en heure au Canada. |
| **SBOM** | Sécurité logicielle | *Software Bill of Materials* : Inventaire formel de tous les composants, bibliothèques et poids de modèles composant l'artefact d'agent. |
| **SHACL** | Données sémantiques | *Shapes Constraint Language* (W3C) : Langage pour valider des graphes RDF contre un ensemble de contraintes structurelles. |
| **SLSA** | Sécurité logicielle | *Supply-chain Levels for Software Artifacts* : Cadre garantissant l'intégrité de la chaîne de compilation et d'émission de l'agent. |
| **VC / VP** | Identité Décentralisée | *Verifiable Credential / Verifiable Presentation* (W3C) : Attestation signée numériquement contenant des attributs et preuves de mandat opposables. |

---

### 3.2 Table des Axiomes, Invariants et Théorèmes Centraux

| Intitulé / Notion | Localisation | Énoncé Formel & Portée Technique | Implications Critiques & Falsifiabilité |
|---|---|---|---|
| **Invariant Transversal de la Somme** | ch. 1 (§ 1.0.2), p. 6 & Avant-propos | L'interopérabilité durable repose sur quatre notions solidairement nécessaires : **Découplage**, **Contrat**, **Évolution**, **Exploitation**. Aucun terme ne supplée l'absence d'un autre. | Falsifiable si un système démontre une interopérabilité durable sans support formel de contrat ou sans observabilité d'exploitation. |
| **Principe d'Intégration Quadratique** | ch. 1 (§ 1.0.1), p. 5 | Raccorder $N$ systèmes autonomes deux à deux sans intermédiaire engendre jusqu'à $\frac{N(N-1)}{2}$ connexions dédiées, générant une dette d'intégration combinatoire. | Justifie l'obligation d'un modèle pivot et d'une couche protocolaire découplée (MCP/A2A). |
| **Théorème de Non-Compositionnalité** | ch. 6, p. 74 & ch. 22, p. 256 | La composition de plusieurs agents localement optimisés et alignés ne garantit pas la stabilité ni l'alignement global du système multi-agents en boucle fermée. | Réfute le postulat de l'émergence bienveillante spontanée et impose un encadrement déterministe (OO4). |
| **Le Problème des Deux Sauts (Two-Hop)** | ch. 17 (§ 17.1), pp. 189-195 | Dans une chaîne de délégation $Client \to Agent_1 \to Agent_2$, le mandat initial est rompu au second saut si $Agent_1$ agit sous son identité propre sans preuve cryptographique opposable liant $Agent_2$ au consentement du client. | Impose l'utilisation de Verifiable Presentations imbriquées ou de tokens échangés sous contrainte de finalité (RFC 8693 durci). |
| **Invariant de Finalité Institutionnelle** | ch. 22 (§ 22.3), p. 260 | Un agent logiciel ne possède aucune personnalité juridique ni autorité intrinsèque ; tout pouvoir découle d'un mandat humain délégué, strictement borné dans le temps et dans sa portée. | Interdit les délégations ouvertes et exige l'invalidation automatique dès dépassement du périmètre de mandat. |
| **Théorème de Décidabilité des Politiques** | ch. 48, p. 542 & ch. 49, p. 555 | La vérification a priori qu'un plan d'actions généré stochastiquement respecte l'ensemble des contraintes de sécurité est indécidable dans le cas général (réduction au problème de l'arrêt) sans restriction à un langage de politique non Turing-complet. | Impose la séparation stricte entre le moteur de raisonnement (Turing-complet/stochastique) et le vérificateur PEP (automate d'états finis/décidable). |
| **Principe de Sémantique d'Effet Réversible** | ch. 48 (§ 48.2), pp. 538-541 | Toute action de modification du monde réel exécutée par un agent doit être idempotente ou posséder une action compensatoire formellement spécifiée (patron Saga). | Falsifiable si une action critique irréversible est déléguée à un agent sans garde-fou de validation humaine préalable (Human-in-the-Loop). |
| **Théorème CAP Appliqué à l'Agentique** | ch. 1, p. 18 & ch. 24, p. 280 | Dans un système multi-agents distribué, il est impossible de garantir simultanément la Cohérence (partage d'état parfait), la Disponibilité (réponse immédiate de l'agent) et la Tolérance au Partitionnement (résilience aux coupures d'outils). | Les frameworks d'agents doivent expliciter leur compromis : cohérence forte (orchestration centralisée) vs disponibilité locale (agents autonomes déconnectés). |

---

## 4. Taxonomies Formelles et Cadres de Référence

### 4.1 Taxonomie des Options d'Orchestration (OO1 à OO4)

| Niveau | Désignation | Mode d'Exécution | Contrôle et Déterminisme | Applicabilité en Services Financiers |
|---|---|---|---|---|
| **OO1** | *Black-Box Autonome* | Boucle LLM pure (ReAct libre sans contrainte d'état). | Nul : chemin d'exécution imprévisible, boucle infinie possible. | **Totalement prohibé** (violation E-23, Loi 25 et auditabilité). |
| **OO2** | *Encadrement Statique* | Règles hardcodées, filtrage d'entrées/sorties par regex/listes. | Faible : contournable par jailbreak ou reformulation sémantique. | Insuffisant pour la conformité réglementaire. |
| **OO3** | *Encadrement Dynamique* | Guardrails LLM, classificateurs de sécurité, modérateurs. | Moyen : probabiliste (risque de faux négatifs dans la modération). | Toléré pour les fonctions de conseil informatif sans effet transactionnel. |
| **OO4** | *Autonomie Encadrée Déterministe* | Automate d'états finis (FSM/DAG), PEP/PDP formel, sémantique d'effet transactionnelle. | Total : chaque transition d'état et appel d'outil est vérifié mathématiquement avant exécution. | **Obligatoire** pour tout processus impliquant des données financières, des transactions ou des décisions automatisées. |

---

### 4.2 Taxonomie des Niveaux d'Interopérabilité (LCIM Étendu)

1. **Niveau 0 — Aucune interopérabilité** : Systèmes totalement isolés.
2. **Niveau 1 — Technique** : Transport de bits et connectivité réseau physique/logique (TCP/IP, HTTP/2, WebSockets).
3. **Niveau 2 — Syntactique** : Formats de données et encodage structuré (JSON, XML, Protobuf, schémas de message).
4. **Niveau 3 — Sémantique** : Signification partagée des concepts via ontologies et vocabulaires formels (RDF, OWL, ISO 20022).
5. **Niveau 4 — Pragmatique** : Accord sur l'intention, le contexte d'usage et les préconditions/postconditions des services (MCP Tools, OpenAPI).
6. **Niveau 5 — Dynamique** : Négociation temps réel, synchronisation d'état et adaptation aux changements de comportements (A2A).
7. **Niveau 6 — Conceptuel** : Alignement complet des modèles du monde et des postulats opérationnels entre systèmes d'entreprise.

---

### 4.3 Taxonomie des Attaques d'Identité et de Délégation (Ch. 19 & 20)

- **ATK-01 : Rug-Pull d'Agent Card** — Remplacement frauduleux de la clé publique ou de l'URL de service d'un agent après son admission dans l'annuaire.
- **ATK-02 : Attaque du Député Confus (Confused Deputy)** — Manipulation d'un agent légitime disposant de privilèges élevés pour lui faire exécuter une action hors contexte via une injection de prompt indirecte.
- **ATK-03 : Rupture de Chaîne de Mandat (Mandate Stripping)** — Élimination délibérée des restrictions de mandat lors du passage inter-domaines.
- **ATK-04 : Rejeu de Verifiable Presentation (VP Replay)** — Interception et rejeu d'une attestation de délégation non liée temporellement ou dépourvue de nonce/PoP.
- **ATK-05 : Empoisonnement de Registre de Découverte (Registry Poisoning)** — Enregistrement de faux agents imitateurs de services institutionnels.

---

## 5. Protocole d'Audit Contradictoire et Méthodologie d'Essaim

Chaque segment sera audité par un essaim d'agents dédiés selon trois axes d'évaluation stricts :

1. **Axe 1 — Rigueur Formelle et Algorithmique** :
   - Falsification des preuves et des prétentions théoriques (notamment sur la décidabilité, l'idempotence et les garanties d'opposabilité).
   - Vérification de la complétude des équations, des invariants d'état et des modèles formels (ArchiMate, FSM).
   - Identification des non-sequiturs mathématiques et des postulats non démontrés.

2. **Axe 2 — Solidité Architecturale et Empirique** :
   - Faisabilité industrielle en environnement bancaire réel (latence réseau, débits de messages, coût d'inférence, compatibilité legacy).
   - Résistance aux pannes distribuées (modes de déconnexion, reprise sur sinistre, désynchronisation de registre).
   - Évaluation de la reproductibilité des benchmarks et études de cas citées (ch. 35).

3. **Axe 3 — Confrontation Bibliographique et État de l'Art (2024-2026)** :
   - Vérification des références bibliographiques : identification des articles inventés, des citations détournées ou des affirmations anachroniques.
   - Confrontation aux standards publiés jusqu'en novembre 2026 : IETF, W3C, NIST PQC, ISO 20022, et littératures académiques de pointe (STOC, NeurIPS, SOSP, OSDI, ICLR).
   - Audit spécifique de la conformité réglementaire québécoise et canadienne (Loi 25, BSIF E-23, AMF Note IA de nov. 2026).
