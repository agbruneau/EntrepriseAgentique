# Rapport d'Audit Contradictoire — Livre 2 : Faire Confiance (Candidat 3, Niveau 0)
**Segment audité** : Livre II — *Faire confiance : Identité non humaine et délégation vérifiable* (Ch. 12 à 21, pp. 144 à 255) + Transition Livre III (Ch. 22, pp. 252-255).  
**Auteur de l'audit** : Analyste Candidat 3 (Niveau 0)  
**Date d'évaluation** : Novembre 2026  
**Référentiel méthodologique** : Axes R2 (Rigueur formelle et algorithmique) et R3 (Confrontation bibliographique et état de l'art 2024-2026).

---

## 1. Résumé Exécutif Critique du Segment Livre 2

Le Livre II du *Compendium* constitue le pivot sécuritaire et cryptographique de l'ouvrage. Il traite de la transition entre la coopération protocolaire (Livre I) et l'encadrement réglementaire déterministe (Livre III), en explorant l'émergence d'une pile d'identité non humaine et de délégation vérifiable pour les systèmes agentiques en environnement financier réglementé.

L'évaluation contradictoire révèle une dualité marquée :
1. **Une posture épistémique d'une rigueur documentaire remarquable** : L'auteur documente systématiquement les limites des corpus consultés au moyen d'un système formalisé de « degrés d'absence » (degré 1 : fait négatif vérifié ; degré 2 : fait négatif établi par réserve explicite de la source ; degré 3 : absence de documentation dans le corpus). Il résiste admirablement aux déclarations d'éditeurs non étayées, refuse d'extrapoler des pourcentages sans dénombrement, et explicite la frontière entre ses constructions d'auteur et les normes ratifiées.
2. **Des défaillances formelles et des lacunes algorithmiques majeures (Axe R2)** :
   - **Falsification de la « rupture d'opposabilité à deux sauts »** : La thèse centrale du chapitre 17 affirmant qu'une délégation multi-sauts ($A \to B \to C$) perd inévitablement son opposabilité au second maillon repose sur une confusion catégorielle entre une règle de filtrage d'accès stateless locale d'une RFC spécifique (RFC 8693 Section 4.1, qui classe les revendications imbriquées `act` comme « informationnelles » pour la décision d'accès locale) et une impossibilité mathématique/cryptographique universelle. Sous le modèle formel standard d'infalsifiabilité existentielle (EUF-CMA), l'opposabilité se préserve mathématiquement pour toute profondeur arbitraire $n \ge 2$ via des chaînes de signatures numériques, des accréditations vérifiables chaînées (W3C VC 2.0) ou des capabilités cryptographiques à atténuation monotone (Macaroons / Biscuits).
   - **Omission critique de FIPS 205 (SLH-DSA) et cécité sur l'explosion des charges utiles PQC** : Alors que le chapitre 21 analyse minutieusement l'horloge NIST (NIST IR 8547), il omet totalement la norme FIPS 205 (SLH-DSA, signatures sans réseau euclidien) pourtant finalisée le même jour que FIPS 204 (13 août 2024). Plus grave, il n'effectue aucune quantification volumétrique des signatures post-quantiques (ML-DSA : 2,4 à 4,6 Ko ; SLH-DSA : 7,8 à 49 Ko), ignorant l'impact fatal de ces tailles sur les en-têtes HTTP (`Authorization: Bearer`), qui excèdent les limites standards (8 Ko) des passerelles d'entreprise (Nginx, Envoy, AWS ALB) et déclenchent des erreurs HTTP 431.
   - **Vacuité opérationnelle du volet « Agentic SOC » (Ch. 20)** : Bien que le titre et le cadrage annoncent une boucle défensive opérationnelle, le chapitre ne livre aucune métrique formelle de compromission, aucun algorithme de détection d'anomalies sur les graphes de raisonnement (reasoning graphs), et aucun protocole d'isolation ou d'expulsion de sous-graphes compromis. Il se borne à un constat de symétrie attaque/défense et à une analyse des annonces d'éditeurs (Microsoft, Google Cloud, CrowdStrike).
   - **Angle mort sur la sécurité par capabilités (Object-Capabilities)** : En invoquant l'article fondateur de Norm Hardy (1988) sur le *Confused Deputy* uniquement comme un jalon terminologique sans adopter le paradigme des capabilités non forgeables qu'il introduit, l'ouvrage s'enferme dans les apories des listes de contrôle d'accès (ACL) traditionnelles.

---

## 2. Matrice Exhaustive des Défauts (R2 / R3)

| ID | Sévérité | Chapitre | Page(s) | Citation Textuelle Exacte | Diagnostic Causal Approfondi | Correctif Formel & Contre-Exemple Mathématique |
|---|---|---|---|---|---|---|
| **DEF-L2-01** | **Bloquant (Erreur formelle)** | Ch. 17 | pp. 197-198 | « Ce qui manque au second saut n’est donc pas un détail que la spécification aurait négligé, c’est ce qu’elle a délibérément placé hors de sa portée... la perte ne se produit pas à un rang numéroté, mais au premier changement de régime... "deux sauts" nomme le premier cas de figure où ce changement devient inévitable. » | **Confusion catégorielle entre politique d'accès locale et opposabilité cryptographique**. L'auteur interprète la clause de la RFC 8693 §4.1 (« prior actors are informational only and not to be considered in access control decisions ») comme une rupture intrinsèque d'opposabilité. Or, cette clause prescrit une règle de décision pour serveurs de ressources sans état, et n'interdit aucunement la non-répudiation ni l'opposabilité probatoire de la piste d'audit (*history trail*) pour un vérificateur global. | **Preuve de préservation de l'opposabilité pour tout $n \ge 2$** : Définir une chaîne de délégation $\Delta_n = \{ \sigma_1, \dots, \sigma_n \}$ où $\sigma_k = \text{Sign}_{SK_k}(A_{k+1}, S_k, T_k, H(\sigma_{k-1}))$. Sous l'hypothèse EUF-CMA de la signature sous-jacente, la probabilité de forger une délégation arbitraire est bornée par $\sum_{k=1}^n \text{Adv}_{\text{EUF-CMA}}(A_k) \le n \cdot \text{negl}(\lambda)$. Contre-exemples démontrés : Macaroons (Birgisson et al., 2014) et Biscuit tokens (atténuation Datalog hors-ligne). |
| **DEF-L2-02** | **Bloquant (Erreur formelle)** | Ch. 21 | pp. 236-248 | « FIPS 203 (ML-KEM, encapsulation de clé) et FIPS 204 (ML-DSA, signature) sont des normes finales, publiées le 13 août 2024 » (p. 237) et « dont les tailles d’artefacts sont sensiblement accrues » (p. 248). | **Omission de FIPS 205 (SLH-DSA) et absence de quantification volumétrique des surcoûts PQC**. FIPS 205 (SPHINCS+) est le standard de signature alternatif fondamental (reposant uniquement sur la sûreté des fonctions de hachage). De plus, l'auteur omet de quantifier les tailles de clés et signatures : ML-DSA-44 requiert 2 420 octets de signature et 1 312 octets de clé publique ; SLH-DSA-128s requiert 7 856 octets de signature. Encodés en Base64URL dans un jeton JWT/JWS, ces artefacts dépassent immédiatement la limite standard de 8 Ko des en-têtes HTTP (`Request Header Fields Too Large` / HTTP 431). | Intégrer formellement FIPS 205 dans le corps du texte. Modéliser l'impact volumétrique : $\text{Size}_{\text{JWT}} = \frac{4}{3} (\text{Size}_{\text{payload}} + \text{Size}_{\text{sig}}) + \text{Headers}$. Pour une chaîne multi-sauts à $n=3$, la charge de signatures ML-DSA seule dépasse $3 \times 2\,420 = 7\,260$ octets ($> 9,6$ Ko en Base64). Prescrire le découplage de transport (transmission par référence URI déréférençable ou conteneurs COSE compressés CBOR). |
| **DEF-L2-03** | **Majeur (Lacune méthodologique)** | Ch. 20 | pp. 228-235 | « Ce rapport reprend par ailleurs des métriques auto-déclarées d’éditeur, dont le présent chapitre ne reprend aucune. » (p. 231) ; « Lecture de l’auteur — ce qu’il n’établit pas : qu’un centre d’opérations agentique se range en "gouvernable" ou "ingouvernable"... » (p. 233). | **Vacuité algorithmique de la boucle défensive Agentic SOC**. Alors que le chapitre promet le traitement de l'Agentic SOC, il refuse toute métrique sans en proposer aucune, omet totalement l'analyse des graphes de raisonnement et n'articule aucun protocole d'isolation ou d'expulsion de sous-graphes d'agents compromis. Le chapitre se réduit à un commentaire des fiches commerciales de Microsoft, Google et CrowdStrike. | Définir un modèle opérationnel formel : (1) Métrique de dérive de raisonnement $\mathcal{D}(G_t, G_0) = \text{GraphEditDist}(G_t, G_{\text{baseline}}) / \|V\|$, (2) Détection d'anomalies de graphes d'exécution via plongement de graphes (GNN / temporal random walks), (3) Protocole d'expulsion : révocation cryptographique immédiate de la session d'agent au PEP (Policy Enforcement Point) et invalidation des clés éphémères de sous-graphe. |
| **DEF-L2-04** | **Majeur (Lacune méthodologique)** | Ch. 19 | pp. 216-217 | « Norm Hardy (1988), The Confused Deputy (or why capabilities might have been invented)... nomme le patron dont toute cette taxonomie est une réinstanciation... » | **Incompréhension de la solution par capabilités (Object-Capabilities)**. L'auteur cite Hardy (1988) comme un argument historique d'autorité, mais omet la thèse centrale de l'article : la faille du délégué confus provient de la séparation entre la désignation de la ressource et l'autorité d'y accéder (inhérente aux ACL). Les agents IA manipulant des outils tiers exigent des capabilités non forgeables plutôt que des rôles RBAC/ABAC globaux. | Remplacer la perspective ACL/identité pure par le modèle de sécurité par capabilités : une référence d'outil est un triplet inséparable $\mathcal{C} = \langle \text{URI}_{\text{outil}}, \text{Permissions}, \text{SecretKey} \rangle$. Le délégué ne peut invoquer l'outil que dans la limite stricte de la capabilité transmise par le mandant, rendant l'attaque de confusion de délégué structurellement impossible. |
| **DEF-L2-05** | **Majeur (Lacune méthodologique)** | Ch. 18 | pp. 201-209 | « Le KYA transpose la logique du KYC — vérifier avant d’admettre — sans l’infrastructure institutionnelle qui rend le KYC possible... » (p. 202). | **Absence de spécification procédurale d'admission KYA**. Après avoir démontré l'éclatement des initiatives (DIF, Akamai, W3C, AGNTCY), l'ouvrage n'articule aucune séquence algorithmique permettant à une passerelle d'entreprise de valider un agent tiers à l'instant d'admission. | Formaliser le protocole d'admission KYA en 5 phases déterministes : (1) Présentation de l'Agent Card signée et des accréditations W3C VC, (2) Résolution décentralisée du DID et extraction de la clé publique, (3) Vérification de la non-révocation en ligne (introspection RFC 7662 / status list 2021), (4) Vérification cryptographique des attestations de conformité d'exécution (attestation d'enclave TEE/vLEI), (5) Émission d'un jeton d'accès local à portée bornée ($T_{\text{max}} \le 1\text{ h}$). |
| **DEF-L2-06** | **Majeur (Lacune méthodologique)** | Ch. 21 | pp. 242-245 | « La carte signée dispose d’un point où l’algorithme est déclaré, et ce point est obligatoire (F-03)... » (p. 244). | **Cécité sur l'absence de ratification des identifiants d'algorithmes PQC dans JOSE/COSE**. L'affirmation selon laquelle la carte A2A est crypto-agile grâce au paramètre `alg` de JWS (RFC 7515) ignore le fait qu'au registre IANA, aucun identifiant standard n'est ratifié pour ML-DSA (`ML-DSA-44`, etc.) ou SLH-DSA. Les travaux IETF (draft-ietf-cose-dilithium) demeurent non ratifiés. | Relever explicitement le verrou normatif de normalisation IANA/JOSE : tant que les drafts IETF COSE/JOSE pour les signatures post-quantiques ne sont pas publiés comme RFC, l'interopérabilité post-quantique d'une Agent Card reste cantonnée à des accords bilatéraux d'implémentation hors-standard. |
| **DEF-L2-07** | **Mineur (Clarté & Typographie)** | Ch. 12 | p. 147 | « « Une application qui demande des ressources protégées pour » (Figure 12.4, colonne gauche). | **Troncature textuelle graphique dans la figure**. Dans la colonne de gauche de la Figure 12.4, la définition de « client » extraite de la RFC 6749 §1.1 est tronquée au mot « pour » sans ponctuation ni suite de phrase. | Rétablir le texte complet de la RFC 6749 : « Une application qui demande des ressources protégées pour le compte du détenteur de ressource et avec son autorisation. » |
| **DEF-L2-08** | **Mineur (Clarté & Typographie)** | Ch. 14 | pp. 162-164 | « Figure 14.1 — La grille des cinq questions... » (p. 162) suivi de « Tableau 14.2 — Application-témoin de la grille... » (p. 164). | **Discordance typologique et saut d'indexation de tableau**. L'encadré de la page 162 est nommé « Figure 14.1 » dans le PDF alors que le texte map et la logique du texte le traitent comme un tableau. Le tableau suivant à la page 164 est étiqueté « Tableau 14.2 », rendant le « Tableau 14.1 » introuvable dans la mise en page. | Harmoniser la nomenclature : renommer « Figure 14.1 » en « Tableau 14.1 » pour rétablir la séquence continue des tableaux (Tableau 14.1, Tableau 14.2, Tableau 14.3). |
| **DEF-L2-09** | **Mineur (Clarté & Rigueur)** | Ch. 19 & 20 | pp. 212, 222 | « Publiée le 28 juillet 2026 (2026-07-28, constat du 23 octobre) ; rejeu non fait : cette section et la rangée "Jeton — MCP" du § 20.4 restent bornées à la révision 2025-11-25. » | **Obsolescence déclarée non résolue**. L'ouvrage reconnaît qu'une révision majeure de MCP est parue le 28 juillet 2026, mais maintient l'audit de sécurité sur la version de novembre 2025 avec la clause « rejeu non fait », introduisant un décalage d'actualité pour un livre compilé fin octobre 2026. | Intégrer les éléments stabilisés de la révision MCP 2026-07-28 (transports sans état, refonte du modèle d'autorisation et suppression des en-têtes de session). |
| **DEF-L2-10** | **Mineur (Clarté & Rigueur)** | Ch. 20 | p. 226 | « Internet-Draft draft-mp-agntcy-ads, de soumission individuelle ; balayage sur la révision -01, supplantée par la -02 du 6 juillet 2026, non rebalayée » | **Maintien d'un balayage sur un brouillon rendu obsolète**. L'inventaire de la révocation s'appuie sur la révision -01 alors que la -02 était disponible avant la date de gel documentaire du 27 juillet 2026. | Rebalayer sur la version draft-mp-agntcy-ads-02 pour confirmer la persistance de l'absence de primitives de révocation dans l'annuaire AGNTCY. |

---

## 3. Audit Approfondi Section par Section (S14 à S23, Ch. 12 à 21)

### S14 : L'héritage étiré et l'identité décentralisée (Ch. 12 & Ch. 13, pp. 144-156)
- **Analyse critique de l'adaptation d'OAuth 2.0 (RFC 6749) et SCIM (RFC 7643)** :
  L'auteur démontre avec pertinence la crise conceptuelle qui frappe la pile IAM pré-agentique. Dans RFC 6749, l'attribution des rôles (`client` vs `resource owner`) place l'agent autonome dans une contradiction fondamentale :
  - Si l'agent est un `client`, il requiert l'intervention d'un mandant humain via un `user-agent` (navigateur web, redirection §4.1) pour consentir, ce qui est incompatible avec les flux autonomes asynchrones sans présence humaine (*Human-Not-Present*).
  - Si l'agent utilise le mode justificatifs de client (`client credentials grant`, §4.4), il opère sous une identité de service statique, masquant complètement l'identité de l'utilisateur final pour lequel il exécute la tâche, créant l'« écart d'attribution » (*attribution gap*) souligné par l'OWASP (ASI03).
  - Quant à SCIM 2.0 (RFC 7643 §4), le fait négatif vérifié au degré 1 (absence de schéma de ressource pour mandataire autonome) est rigoureusement établi. L'examen des projets IETF (draft-abbey expiré ; draft-wzdk soumission individuelle non adoptée) prouve l'échec de l'industrie à normaliser l'identité d'agent dans les annuaires d'entreprise à mi-2026.
- **Solidité des standards W3C DID v1.0/v1.1 et Verifiable Credentials v2.0** :
  L'auteur confronte judicieusement le statut de Recommandation W3C du Verifiable Credentials Data Model v2.0 (15 mai 2025) à son absence totale de déploiement en production dans le secteur financier. Le diagnostic institutionnel est lucide : la technologie cryptographique existe (signatures JSON-LD Data Integrity et SD-JWT-VC), mais la *trust fabric* (autorités d'accréditation, règles de gouvernance de fédération) fait défaut, à l'exception notable du vLEI (GLEIF).

### S15 : La grille des cinq questions et l'émission d'identités (Ch. 14 & Ch. 15, pp. 155-167)
- **Nature et rigueur de la grille des cinq questions (Q-A à Q-E)** :
  L'auteur pose honnêtement la grille comme une construction d'auteur méthodologique transversale. Les cinq questions :
  - **Q-A** (*Qui es-tu ?*) : Identifiant stable, vérifiable, résistant à l'usurpation et révocable.
  - **Q-B** (*Qui t'a créé ?*) : Chaîne de provenance jusqu'à une autorité d'émission avec ancrage de confiance.
  - **Q-C** (*Pour qui agis-tu ?*) : Chaîne de mandat interrogeable à l'instant $t$.
  - **Q-D** (*Que peux-tu faire ?*) : Bornes de privilège explicites et opposables au point d'application.
  - **Q-E** (*Qui en répond ?*) : Imputabilité traçable jusqu'à une personne physique ou une entité juridique.
- **Rendement sur l'application-témoin (Tableau 14.2)** :
  Sur 15 cellules évaluées (3 mécanismes $\times$ 5 questions), 0 mécanisme ne répond pleinement aux cinq questions. 8 réponses partielles et 7 silences complets (degré 3) sont relevés. L'auteur démontre avec brio que l'absence de réponse à Q-A rend Q-D et Q-E formellement inapplicables.
- **Structure technique de l'Agent Card signée (Ch. 15)** :
  L'analyse de la spécification A2A v1.0.0 (Linux Foundation) démontre la faiblesse des garanties offertes :
  1. L'apposition de la signature est facultative (`MAY`), la vérification recommandée (`SHOULD`).
  2. Le format JWS (RFC 7515) avec canonicalisation JCS (RFC 8785) assure l'intégrité du document statique, mais l'en-tête protégé ne contient aucun paramètre temporel (`exp`, `nbf`).
  3. L'ancrage de confiance est totalement renvoyé hors protocole (`jku`, `kid` ou magasin de clés local non spécifié).
  4. L'interdiction d'utiliser des clés expirées ou révoquées est un voeu pieux normatif (`MUST NOT`), car aucun protocole de vérification d'état n'est fourni.

### S16 : Annuaires d'agents et gouvernance des registres (Ch. 15, pp. 166-178)
- **Modèle d'annuaire propriétaire (Microsoft Entra Agent ID)** :
  L'auteur met en lumière la fracture architecturale entre les annuaires propriétaires et les registres ouverts. Entra Agent ID (avril 2026) impose un modèle à deux plans étanches : les politiques d'accès conditionnel ciblant les identités d'agent ne s'appliquent pas au compte utilisateur de l'agent, et réciproquement. Cela autorise des fuites de périmètre où un agent hérite de privilèges sans être assujetti aux contrôles contextuels stricts appliqués aux humains.
- **Registres de gouvernance (CSA Labs et Cisco AGNTCY)** :
  L'analyse démontre que le profil de registre CSA Labs s'ancre sur une extension SCIM expirée (draft-abbey), tandis que le service ADS d'AGNTCY (draft-mp-agntcy-ads) revendique une intégrité par adressage de contenu sans démonstration cryptographique de non-répudiation.

### S17 : Le Passeport d'agent : anatomie d'un artefact virtuel (Ch. 16, pp. 177-189)
- **Déconstruction de l'objet de synthèse** :
  Le « passeport d'agent » est explicitement désigné comme une construction d'auteur qui n'existe dans aucune norme de 2026. L'auteur formalise l'assemblage de quatre composantes disparates :
  1. La carte d'agent signée (A2A) $\to$ intégrité syntaxique.
  2. L'inscription au registre gouverné (CSA/AGNTCY) $\to$ déclaration des bornes de permissions.
  3. La chaîne de mandat (AP2 / RFC 8693) $\to$ lien de délégation.
  4. Les attestations de conformité (BSIF E-23 / Loi 25) $\to$ imputabilité réglementaire.
- **Preuve de non-compositionnalité de l'assemblage** :
  L'auteur formule une observation capitale : « l'assemblage n'est pas une somme ». Aucune des quatre pièces ne supplée aux carences de l'autre. En particulier, la carte signée ne valide pas la validité du mandat à l'exécution, et le registre n'assure aucune opposabilité au point d'application (*Policy Enforcement Point*).

### S18 : La chaîne de mandat et falsification du problème des deux sauts (Ch. 17, pp. 188-200)
- **Falsification formelle de la démonstration mathématique de rupture d'opposabilité** :
  Le chapitre 17 formule la thèse selon laquelle au-delà de deux sauts ($A \to B \to C$), la chaîne de mandat perd inévitablement son opposabilité.
  *Réfutation contradictoire* : L'auteur confond une contrainte procédurale de la RFC 8693 Section 4.1 (qui impose à un serveur de ressources local de ne considérer que les claims de premier niveau et l'acteur immédiat pour sa décision d'autorisation) avec une rupture de la chaîne de confiance cryptographique.
  *Démonstration* : L'opposabilité juridique et cryptographique d'un mandat délégué repose sur la transitivité des signatures numériques :
  $$A \xrightarrow{\text{Sign}_{SK_A}} B \xrightarrow{\text{Sign}_{SK_B}} C$$
  Chaque saut génère une preuve vérifiable :
  $$\sigma_1 = \text{Sign}_{SK_A}(ID_B, \text{Scope}_1, T_1), \quad \sigma_2 = \text{Sign}_{SK_B}(ID_C, \text{Scope}_2, T_2, H(\sigma_1))$$
  Un vérificateur indépendant $V$ confronté à $\sigma_2$ vérifie :
  $$\text{Verify}_{PK_B}(\sigma_2) = \text{True} \quad \land \quad \text{Verify}_{PK_A}(\sigma_1) = \text{True} \quad \land \quad \text{Scope}_2 \subseteq \text{Scope}_1 \quad \land \quad t \in T_1 \cap T_2$$
  La validité de cette chaîne est mathématiquement irréfutable sous le modèle standard EUF-CMA.
  Des technologies de production existantes concrétisent exactement cette opposabilité multi-sauts :
  - **Macaroons** (Birgisson et al., Google, NDSS 2014) : permettent l'adjonction de *caveats* contextuels et de décharges de délégation à chaque saut sans retour à l'émetteur initial, avec preuve par HMAC chaîné.
  - **Biscuit tokens** : combinent cryptographie à clé publique et langage Datalog pour contraindre formellement l'atténuation des droits à chaque délégation.
  - **GNAP (RFC 9635, octobre 2024)** : refond le modèle de négociation de mandat pour agents autonomes en intégrant nativement la preuve de possession (*Proof-of-Possession*) multi-acteurs.
- **Supervision humaine et biais d'automatisation (§17.4-17.5)** :
  L'auteur expose avec pertinence l'angle mort de l'article 12.1 de la Loi 25 québécoise et de la ligne directrice BSIF E-23 : ces textes imposent une révision humaine sans jamais prescrire le format probatoire de cette révision dans le flux d'exécution. L'analyse du *tamponnage* (approbation machinale) et du *paradoxe de l'explicabilité* est rigoureusement posée comme une lacune non instruite empiriquement dans le corpus.

### S19 : KYA et taxonomie des attaques d'identité (Ch. 18 & Ch. 19, pp. 199-211)
- **Le Know Your Agent (KYA, Ch. 18)** :
  L'inventaire des 9 initiatives pré-normatives met en garde contre l'homonymie toxique : le KYA d'Akamai (empreinte comportementale et réputation IP à la périphérie du réseau) n'a rien de commun avec le KYA-OS de la Decentralized Identity Foundation (schéma d'attestation DID). La transposition de la logique KYC du secteur bancaire aux agents achoppe sur l'absence de registre centralisé d'identités agentiques d'autorité publique.
- **Taxonomie des attaques (Ch. 19)** :
  Le classement par le maillon de la chaîne d'identité qui cède (Tableau 19.1) adossé à la grille du Ch. 14 est conceptuellement élégant. L'auteur intègre :
  - **AML.T0104** (empoisonnement d'outils) $\to$ défaut Q-B des sources.
  - **AML.T0053** (invocation d'outils inaccessibles) $\to$ défaut Q-D (absence de réduction de portée).
  - **UNC6395** (jetons porteurs Salesloft Drift) $\to$ défaut Q-A (jeton non lié au porteur).
  - **Confusion de délégué** $\to$ défaut Q-C (mandat non interrogeable à l'exécution).
  - **AgentPoison (NeurIPS 2024)** $\to$ défaut Q-B de la mémoire RAG.
  - **Détournement multi-agents (F-25)** $\to$ défaut hors grille (non-compositionnalité de la sûreté).
- **La triade létale de Willison (§19.2)** :
  L'auteur synthétise impeccablement la racine architecturale de la vulnérabilité des LLMs : le mélange sur un canal unique des instructions et des données, rendant l'injection d'invite indirecte (OWASP LLM01) structurellement insoluble au sein du modèle lui-même.

### S20 : Usurpation, rug-pull et inventaire de la révocation (Ch. 19 & Ch. 20, pp. 210-222)
- **L'attaque par Rug-Pull d'Agent Card / Serveur d'outils (Ch. 20)** :
  L'auteur caractérise avec acuité la classe temporelle d'attaques qui « n'attaquent pas la vérification mais attendent qu'elle soit faite ».
  Sur le protocole MCP (révision 2025-11-25) :
  - Les 8 champs de la définition d'un outil (`name`, `inputSchema`, etc.) ne comportent aucun condensat (*hash*) ni signature.
  - La notification `notifications/tools/list_changed` permet à un serveur d'outils de modifier silencieusement ses primitives après approbation initiale par le client.
  - La préimpression ETDI (arXiv 2506.01333, juin 2025) est justement citée comme tentative de lier cryptographiquement les définitions d'outils à des profils OAuth.
- **Inventaire de la révocation (Tableau 20.1)** :
  L'inventaire met en relief l'asymétrie structurelle : 11 mécanismes analysés, 0 mécanisme garantissant une révocation instantanée et propagée en cascade dans une chaîne de mandat. L'analyse des leçons de la PKI (RFC 5280 / RFC 6960) et de l'abandon d'OCSP par Let's Encrypt le 6 août 2025 illustre parfaitement pourquoi la fraîcheur absolue d'un état révoqué est une illusion opérationnelle.

### S21 : L'Agentic SOC : promesse vs réalité documentaire (Ch. 20, pp. 221-233)
- **Évaluation contradictoire de la boucle défensive** :
  Cette section constitue la principale faille d'alignement avec les objectifs du plan d'audit. Le chapitre 20 n'aborde ni la détection d'anomalies de graphes de raisonnement, ni les protocoles d'isolation et d'expulsion de sous-graphes compromis.
- **Apports réels du chapitre** :
  L'auteur démontre la symétrie attaque/défense : les agents d'un SOC agentique (tri d'alertes Microsoft, investigation Google Cloud, CrowdStrike) ingèrent par définition des données hautement non fiables (courriels d'hameçonnage, traces réseau suspectes) et disposent d'outils d'intervention. Ils sont donc exposés en première ligne à la triade létale.
  L'analyse de la documentation Microsoft (1er juillet 2026) sur l'agent de tri d'hameçonnage révèle une faille critique d'architecture : l'agent fonctionnant sous un compte utilisateur permanent ne prend en charge ni PIM (*Privileged Identity Management*) ni TAP (*Temporary Access Pass*) en raison de sa nature d'arrière-plan de longue durée, violant frontalement le principe de moindre privilège juste-à-temps.

### S22 : L'horloge post-quantique et vulnérabilité de la pile identitaire (Ch. 20 & Ch. 21, pp. 232-244)
- **L'horloge NIST et les jalons réglementaires** :
  L'inventaire des échéances (Tableau 21.1) documente rigoureusement :
  1. Le rapport NIST IR 8547 : dépréciation des algorithmes classiques après 2030, interdiction (*disallowed*) après 2035.
  2. Le décret présidentiel US 14412 (22 juin 2026) et la note OMB M-26-15 (24 juin 2026) : obligation pour les agences fédérales de finaliser la transition PQC pour l'établissement de clés au 31 décembre 2030, et pour les signatures numériques au 31 décembre 2031.
  3. L'approche européenne (rapport conjoint Europol / QSFF 2026) : priorisation par le risque sans dates fixes.
- **Le risque "Harvest Now, Forge Later" sur l'identité** :
  L'auteur apporte une distinction remarquable : pour les artefacts d'identité signés (Agent Cards, certificats de mandat), le risque quantique n'est pas la rupture de confidentialité (déchiffrement rétroactif), mais la **rupture rétroactive de non-répudiation**. Un artefact signé avec ECDSA P-256 ou Ed25519 dépourvu de date d'expiration pourra être falsifié à l'horizon 2030-2035 par un attaquant disposant d'un ordinateur quantique exploitant l'algorithme de Shor.
- **Définition de la crypto-agilité** :
  L'auteur définit la crypto-agilité en trois conditions (découplage, contrat versionné, procédure d'évolution documentée). L'inventaire (Tableau 21.2) démontre que la troisième condition n'est satisfaite par aucun artefact agentique actuel.

### S23 : Transition post-quantique et options d'orchestration OO1-OO4 (Ch. 21 & Ch. 22, pp. 243-255)
- **Patrons de migration post-quantique (Ch. 21)** :
  Quatre patrons sont formalisés : coexistence de signatures JWS multiples, mode hybride transitoire, artefacts éphémères à cycle court (remplaçant la révocation), et ancrage sur des classes de documents.
  *Critique R2/R3* : L'auteur n'aborde pas la gestion des identifiants JOSE/COSE non encore ratifiés par l'IANA pour ML-DSA, et passe sous silence le standard de signature FIPS 205 (SLH-DSA).
- **Introduction à l'orchestration APM (Ch. 22, pp. 252-255)** :
  L'auteur introduit la taxonomie OO1-OO4 issue du préprint de TU Munich (Rinderle-Ma, Mangler et coll., 30 juin 2026) :
  - **OO1** : Orchestration agnostique au processus (agents libres, processus implicite).
  - **OO2** : Orchestration consciente d'un cadre (processus décrit dans le prompt, force exécutoire non garantie).
  - **OO3** : Processus déterministe invoquant des agents agnostiques (inversion du contrôle).
  - **OO4** : Orchestration explicite d'agents conscients du processus (saturation des axes contrôle et connaissance).
  L'auteur isole avec une grande finesse analytique la discontinuité critique **OO2 $\to$ OO3**, où la main qui commande passe de l'agent stochastique au moteur déterministe, constituant le seuil d'admissibilité réglementaire pour le secteur financier.

---

## 4. Revue Bibliographique et Confrontation à l'État de l'Art (2024-2026)

L'audit contradictoire a confronté les affirmations du Livre II aux corpus scientifiques et normatifs disponibles jusqu'à l'actualisation de novembre 2026 :

1. **Normes Post-Quantiques NIST (FIPS 203, FIPS 204, FIPS 205)** :
   - *Validation* : FIPS 203 (ML-KEM) et FIPS 204 (ML-DSA) ont été formellement promulgués le 13 août 2024 par le Département du Commerce des États-Unis.
   - *Lacune confirmée* : FIPS 205 (SLH-DSA), promulgué le même jour comme standard de repli universel sans réseaux euclidiens, a été omis du chapitre 21.
   - *Vérification de taille* : Les paramètres ML-DSA-44 (taille de signature de 2 420 octets, clé publique de 1 312 octets) confirment l'incompatibilité avec les architectures de jetons imbriqués sur les canaux HTTP standards sans refonte d'infrastructure.

2. **Protocoles de délégation et d'autorisation IETF (OAuth, GNAP, SCIM)** :
   - *RFC 8693 (OAuth 2.0 Token Exchange)* : Publiée en janvier 2020. Le texte confirme intégralement la citation de la Section 4.1 (« prior actors... are informational only »). Cependant, la confrontation à la littérature de sécurité des systèmes distribués confirme que cette règle d'autorisation locale ne détruit pas la non-répudiation globale de la piste d'audit.
   - *GNAP (RFC 9635)* : Publiée en **octobre 2024** (J. Richer, F. Imbault). Cette norme refond entièrement le modèle de négociation et de délégation d'autorité, apportant nativement le support multi-acteurs et le découplage des canaux de commande. Le Compendium mentionne brièvement GNAP en ajout de dernière heure (p. 199), mais ne l'intègre pas dans son analyse comparative du chapitre 17.
   - *DPoP (RFC 9449, septembre 2023)* : Le Compendium néglige l'apport de DPoP (*Demonstrating Proof-of-Possession at the Application Layer*), qui résout précisément la faille des jetons porteurs (*bearer tokens*) de la campagne UNC6395 en liant cryptographiquement le jeton à une paire de clés éphémères du client.

3. **Sécurité agentique et référentiels OWASP / MITRE ATLAS** :
   - *OWASP Top 10 for Agentic Applications 2026* : La catégorie **ASI03 (Identity and Privilege Abuse)** est parfaitement conforme aux publications de l'OWASP Agentic Security Initiative de décembre 2025 / 2026. Elle met expressément en garde contre les agents héritant de comptes de service sur-privilégiés.
   - *MITRE ATLAS (juin 2026)* : Les techniques AML.T0104 (Tool Poisoning) et AML.T0053 (Inaccessible Tool Invocation), ainsi que la mitigation AML.M0027 (Privilege Attenuation), sont rigoureusement répertoriées.
   - *Recherche académique* :
     - **ETDI (arXiv 2506.01333, juin 2025)** : L'existence de cette proposition académique par Bhatt, Narajala et Habler est confirmée ; elle cible précisément la remédiation du rug-pull et du tool-squatting dans le protocole MCP.
     - **AgentPoison (NeurIPS 2024)** : Référence académique irréprochable démontrant l'injection de portes dérobées dans les bases RAG d'agents autonomes.

---

## 5. Recommandations et Prescriptions d'Amendement

Pour hisser le Livre II au niveau d'exigence formelle requis pour une publication de référence en ingénierie des systèmes agentiques régulés :

1. **Rectification de la thèse du chapitre 17** :
   - Abandonner l'affirmation d'une « impossibilité ou rupture mathématique d'opposabilité à deux sauts ».
   - Reformuler la section 17.6 autour de la distinction entre **décision d'autorisation locale stateless** (où RFC 8693 ignore les maillons antérieurs) et **opposabilité cryptographique de la chaîne de mandat** (pleinement garantie par signature chaînée, Macaroons ou W3C Verifiable Credentials).
2. **Complétion du volet cryptographique post-quantique (Ch. 21)** :
   - Intégrer formellement FIPS 205 (SLH-DSA).
   - Insérer un tableau quantitatif des tailles de clés et de signatures post-quantiques.
   - Prescrire l'architecture de transport pour parer aux erreurs HTTP 431 : découplage des signatures volumineuses via des références URI résolubles hors bande ou adoption de profils de compression binaire COSE/CBOR.
3. **Refonte opérationnelle de l'Agentic SOC (Ch. 20)** :
   - Dépasser la revue des communiqués de presse d'éditeurs et formaliser la détection d'anomalies sur les graphes d'exécution d'agents.
   - Définir les protocoles de quarantaine, de révocation immédiate au PEP et d'expulsion de sous-graphes compromis.
4. **Correction des coquilles et ruptures graphiques** :
   - Rétablir le texte tronqué de la Figure 12.4 (p. 147).
   - Réaligner la numérotation des tableaux au chapitre 14 (Figure 14.1 $\to$ Tableau 14.1).

---
*Fin du rapport d'audit contradictoire du Candidat 3 (Niveau 0) pour le Livre II.*
