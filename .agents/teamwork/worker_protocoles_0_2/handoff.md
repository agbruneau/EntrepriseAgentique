**Segment scope**: Livre I (fin Ch. 6, Ch. 7 à 11) et Livre II (début Ch. 12), pp. 78 à 145 — Couche protocolaire agentique (MCP, A2A, AP2, AGNTCY), registres distribués, modèles de menace et identité non humaine.

# Potential Mistakes and Improvements

### 1. [Bloquant / Erreur formelle] Falsification de la réduction combinatoire $N \times M \to N + M$ de MCP face au non-déterminisme des prompts d'outils
- **Sévérité** : Bloquant / Erreur formelle
- **Localisation précise** : Chapitre 8, page 90 (texte et Figure 8.1), lignes 7340-7346 :
  > « faire dialoguer N agents avec M outils sans standard impose N×M intégrations point-à-point ; une couche de contrat partagée ramène ce coût à N+M. C’est exactement le geste du modèle de données canonique (ch. 1 § 1.6.1), transposé à l’axe agent-outil — et il vaut d’être reconnu comme tel plutôt que présenté comme une nouveauté. »
- **Diagnostic causal approfondi** :
  Cette affirmation transpose mécaniquement un théorème valide de l'intégration d'entreprise déterministe (où un schéma canonique XSD/Protobuf et un bus RPC réduisent strictement les connecteurs logiciels de $O(N \times M)$ à $O(N + M)$) à un environnement probabiliste piloté par des modèles de fondation hétérogènes, ce qui constitue une erreur formelle de modélisation.
  Dans le protocole MCP, l'outil n'est pas uniquement défini par son schéma syntaxique (`inputSchema` en JSON Schema) : son invocation par un agent dépend au premier chef de sa description textuelle en langage naturel (`description`). Or, des modèles de raisonnement distincts ($N$ modèles : Claude 3.5, GPT-4o, Llama 3.3, Gemini 1.5/2.0, Command R+) présentent des sensibilités de prompt, des fenêtres d'attention, des tendances à l'hallucination d'arguments et des heuristiques de tool calling radicalement divergentes face à une même description d'outil. Comme le reconnaît d'ailleurs le Chapitre 9 (§ 9.4.2, p. 111) : *« la description d’un outil est, pour l’essentiel, du texte libre en langage naturel, lu par le modèle à l’inférence »*.
  En conséquence, si l'intégration technique de sérialisation JSON-RPC est bien en $O(N + M)$, la calibration sémantique et pragmatique (l'ingénierie de prompt, le prompt tuning, les exemples en contexte et les garde-fous d'invocation) exige en pratique une validation et une adaptation spécifiques pour chaque couple $(\text{Agent}_i, \text{Outil}_j)$. L'affirmation mathématique sans réserve d'un coût ramené à $N + M$ masque la composante dominante du coût d'intégration en entreprise agentique, qui demeure d'ordre combinatoire $O(N \times M)$ au niveau pragmatique du LCIM.
- **Correctif formel ou contre-exemple explicite** :
  - *Scénario d'échec / Contre-exemple* : Soit un serveur MCP exposant un outil critique `transfert_fonds(compte_source, compte_cible, montant, devise)`. La description standard fournie par l'outil convient parfaitement à un agent A (Claude 3.5 Sonnet) qui extrait rigoureusement les types. L'agent B (un modèle open-source compact 8B déployé localement) échoue systématiquement à distinguer le compte source du compte cible sans l'adjonction de directives spécifiques de formatage dans la description. Pour intégrer fiablement les $M$ outils sur les $N$ agents du parc, l'ingénierie d'entreprise doit réécrire ou surcharger les métadonnées descriptives pour chaque modèle cible, infirmant l'économie d'échelle $N+M$.
  - *Formulation corrigée* : 
    « La standardisation syntaxique du transport et des schémas JSON-RPC opérée par MCP ramène la plomberie d'interconnexion technique de $O(N \times M)$ à $O(N + M)$. En revanche, au niveau pragmatique du LCIM, l'interprétation des descriptions textuelles d'outils par des modèles stochastiques hétérogènes réintroduit une charge d'ajustement et d'évaluation combinatoire : l'assurance que $N$ modèles distincts sélectionnent et paramètrent correctement $M$ outils sans dérive sémantique ne s'obtient pas en $N+M$ sans une ontologie de capacités formellement vérifiable. »

---

### 2. [Bloquant / Erreur formelle] Contradiction architecturale sur le « cœur sans état » de MCP (2026-07-28) et l'absence prétendue de couplage résiduel face aux requêtes multi-tours (MRTR)
- **Sévérité** : Bloquant / Erreur formelle
- **Localisation précise** : Chapitre 8, page 92, Tableau 8.2 et lignes 7504-7528 :
  > « Cœur sans état (ratifié le 28 juill. 2026) : suppression de la poignée de main, de l’identifiant de session et de la reprise de flux. Couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet. »
  > « (1) Les sessions de protocole et l’en-tête qui les portait disparaissent du transport diffusable ; l’état qu’un serveur doit conserver d’un appel à l’autre passe par des poignées explicites, frappées par le serveur et transmises comme arguments d’outil ordinaires. »
- **Diagnostic causal approfondi** :
  Il existe une contradiction formelle directe entre l'affirmation d'un « couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet (round-robin) » et le fonctionnement intrinsèque du mécanisme de requêtes à tours multiples (Multi Round-Trip Requests - MRTR, p. 91) exploitant des « poignées explicites frappées par le serveur ».
  Dans un système distribué, si un client initie une requête auprès d'une instance $S_1$ d'un serveur MCP, que $S_1$ répond `input_required` avec un continuation handle $H$, et que la requête subséquente du client est acheminée par un répartiteur à tourniquet vers une instance distincte $S_2$, l'opération échoue immédiatement par erreur `Invalid/Unknown Handle` à moins que l'une des trois conditions d'architecture distribuée suivantes soit satisfaite :
  1. Le handle $H$ encode l'intégralité de l'état sérialisé, chiffré et signé (stateless continuation token / client-side state), ce qui est hautement contraint par la taille des contextes agentiques ;
  2. Les instances $S_1$ et $S_2$ partagent un magasin d'état distribué externe (distributed cache / data store partagé), ce qui réintroduit un couplage fort d'infrastructure au niveau du backend du serveur d'outils ;
  3. Le répartiteur applique un routage avec affinité de session (session affinity / sticky sessions), ce qui contredit explicitement la mention « aucun couplage résiduel » et le déploiement pur à tourniquet.
  Le manuscrit proclame l'élimination totale du couplage d'état au niveau du protocole tout en omettant de spécifier que la charge de synchronisation d'état distribué n'a pas disparu : elle a simplement été expulsée de la couche transport HTTP vers la couche applicative du serveur MCP.
- **Correctif formel ou contre-exemple explicite** :
  - *Contre-exemple* : Soit un cluster Kubernetes de serveurs MCP `database-query` à 5 répliques derrière un Service Kubernetes standard (`type: ClusterIP`, round-robin iptables). Le tour 1 crée une transaction temporaire sur $S_1$ qui renvoie un handle `tx_9872` avec `input_required`. Le tour 2 contenant la confirmation de l'agent est routé vers $S_3$. $S_3$ ne possède pas la poignée en mémoire locale et rejette la requête. La tâche échoue en plein vol.
  - *Formulation corrigée* : Remplacer dans le Tableau 8.2 la mention « Couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet » par :
    « Découplage de la couche transport (disparition des sessions HTTP et SSE dédiées). Cependant, pour les requêtes multi-tours (MRTR), un couplage d'état applicatif persiste : le déploiement horizontal derrière un répartiteur à tourniquet requiert soit des jetons d'état autonomes signés côté client, soit une couche de persistance d'état distribuée partagée entre les répliques du serveur d'outils. »

---

### 3. [Bloquant / Erreur formelle] Absence de primitives de consensus distribué et de synchronisation d'état dans A2A v1.0, et fausse équivalence d'interaction
- **Sévérité** : Bloquant / Erreur formelle
- **Localisation précise** : Chapitre 8, pp. 96-98 (§ 8.4.2 & § 8.4.3) et Chapitre 9, p. 101 (§ 8.6.3) :
  > « L’unité de travail est la tâche, objet à état traversant un cycle de vie défini — soumise, en cours, requérant une entrée ou une authentification, puis achevée, échouée, annulée ou rejetée. » (p. 97)
  > « les tâches asynchrones de l’axe vertical (§ 8.2.3) empiètent sur le terrain de la délégation de l’axe horizontal — recouvrement postérieur aux revues d’interopérabilité de l’écosystème » (p. 101)
- **Diagnostic causal approfondi** :
  L'analyse du protocole A2A v1.0 présente deux lacunes formelles sévères :
  1. **Absence de consensus distribué et de cohérence de réconciliation** : Le protocole A2A formalise le cycle de vie d'une tâche (`Task`) sous forme d'automate d'états fini côté serveur/délégataire. Or, dans une interaction pair-à-pair distribuée à travers des frontières organisationnelles hétérogènes, A2A v1.0 ne propose aucun protocole de consensus distribué (type Raft/Paxos), aucun identifiant de transaction distribuée, aucune horloge vectorielle (Vector Clocks) ni sémantique d'idempotence native pour réconcilier les états concurrents en cas de partition réseau (split-brain entre l'agent mandant et l'agent délégataire). Si un agent mandant annule une tâche (`canceled`) au moment précis où le délégataire la marque `completed` et déclenche un effet de bord externe, le protocole ne fournit aucun mécanisme déterministe de résolution de conflit.
  2. **Fausse équivalence entre MCP Tasks et A2A Tasks** : Qualifier l'extension de tâches asynchrones de MCP d'« empiètement sur le terrain de la délégation d'A2A » repose sur une confusion sémantique entre deux modèles d'interaction computationnels :
     - MCP Tasks est un modèle **RPC asynchrone asymétrique client-serveur** : l'appelant contrôle l'orchestration et interroge l'état d'un traitement passif (batch/job).
     - A2A Tasks est un modèle de **délégation d'acteur autonome pair-à-pair** : le délégataire dispose de sa propre boucle OODA (Observe-Orient-Decide-Act), d'une opacité délibérée de son raisonnement, et d'un pouvoir d'arbitrage sur la décomposition des sous-tâches et la négociation d'artefacts.
- **Correctif formel ou contre-exemple explicite** :
  - *Scénario de panne non résolue* : Une partition réseau intervient pendant qu'un agent client A2A émet une transition d'annulation `cancel_task(Task_ID_42)`. Le transport HTTP/JSON-RPC échoue avec un timeout. L'agent délégataire, n'ayant pas reçu l'annulation, finalise l'exécution et commit une réservation irréversible auprès d'un tiers. À la reconnexion, l'agent client considère la tâche annulée localement, créant une désynchronisation d'état distribué non rattrapable au niveau du protocole A2A.
  - *Correction* : Introduire explicitement dans le § 8.4 et le § 8.6 la distinction formelle entre délégation autonome (A2A) et job batch passif (MCP), et documenter l'absence de protocole de consensus/réconciliation distribué dans la spécification A2A v1.0 comme une limite critique pour les transactions financières inter-domaines.

---

### 4. [Bloquant / Erreur formelle - Axe R3] Citation réglementaire erronée d'un prétendu « règl. (UE) 2026/1744 » et distorsion du calendrier officiel de l'AI Act
- **Sévérité** : Bloquant / Erreur formelle (Axe R3 - État de l'art et sources)
- **Localisation précise** : Chapitre 10, page 124, lignes 10296-10303 :
  > « Sur le plan réglementaire, le règlement européen sur l’intelligence artificielle — Règlement (UE) 2024/1689, nommé ici parce qu’un instrument repris se désigne par son identifiant — encadre notamment les modèles à usage général, dont les obligations s’appliquent depuis août 2025, la mise en conformité générale se poursuivant jusqu’au 2 août 2027 (2028 pour le haut risque, règl. (UE) 2026/1744). »
- **Diagnostic causal approfondi** :
  Cette mention est doublement erronée et constitue une anomalie bibliographique majeure dans un ouvrage gelé en 2026 :
  1. Le numéro de règlement « règl. (UE) 2026/1744 » n'existe pas dans le droit positif européen régissant l'IA. L'unique texte législatif de l'Union européenne établissant le cadre harmonisé sur l'IA est le **Règlement (UE) 2024/1689** du Parlement européen et du Conseil du 13 juin 2024.
  2. Le calendrier officiel d'application fixé à l'Article 111 du Règlement (UE) 2024/1689 est rigoureusement le suivant :
     - Entrée en vigueur : 2 août 2024 ;
     - 2 février 2025 (6 mois) : Chapitres I et II (pratiques interdites) ;
     - 2 août 2025 (12 mois) : Chapitre III section 4 (organismes notifiés), Chapitre V (modèles d'IA à usage général - GPAI), Chapitre VII (gouvernance), Chapitre XII (sanctions) ;
     - 2 août 2026 (24 mois) : Entrée en application principale, incluant les systèmes d'IA à haut risque de l'**Annexe III** ;
     - 2 août 2027 (36 mois) : Systèmes d'IA à haut risque relevant de l'**Annexe I** (législations d'harmonisation de l'UE préexistantes, ex. dispositifs médicaux, sécurité des machines, aviation civile).
  Aucune disposition légale ne reporte l'application du haut risque à « 2028 ». La citation d'un mystérieux règlement modificatif de 2026 reportant l'échéance à 2028 est une hallucination bibliographique ou l'incorporation non vérifiée d'un projet de couloir spéculatif.
- **Correctif formel ou contre-exemple explicite** :
  - *Correctif textuel* : Supprimer immédiatement la mention `(2028 pour le haut risque, règl. (UE) 2026/1744)`.
  - *Formulation exacte* :
    « ...la mise en conformité des modèles d’IA à usage général (GPAI) s’appliquant depuis le 2 août 2025 (art. 111 § 2), l'entrée en application générale des systèmes à haut risque de l'Annexe III intervenant au 2 août 2026, et celle des systèmes embarqués de l'Annexe I au 2 août 2027 conformément à l'article 111 § 3 du Règlement (UE) 2024/1689. »

---

### 5. [Bloquant / Erreur formelle] Incompatibilité théorique de la tolérance aux pannes byzantines (BFT) classique appliquée aux agents probabilistes
- **Sévérité** : Bloquant / Erreur formelle (Axe R2 - Rigueur algorithmique)
- **Localisation précise** : Chapitre 11, page 133, lignes 11108-11118 :
  > « D’une part, le rapprochement avec la tolérance aux pannes byzantines : un agent non déterministe qui émet un message plausible mais erroné se comporte comme un nœud byzantin, ce qui ouvre la question — encore largement ouverte — de seuils de quorum et de redondance pour des acteurs probabilistes. D’autre part, la décomposition de l’exécution en sous-tâches vérifiées par consensus comme voie vers une fiabilité de qualité industrielle. »
- **Diagnostic causal approfondi** :
  L'assimilation directe d'un agent LLM stochastique à un nœud byzantin classique dans un algorithme de consensus distribué (type PBFT de Castro & Liskov, ou Paxos/Raft sous crash-fault) repose sur une faille théorique majeure touchant à la décidabilité du consensus.
  Dans les systèmes distribués classiques tolérants aux pannes byzantines, la fonction de validation d'un message $m$ est une fonction booléenne stricte $V(m) \in \{\text{true}, \text{false}\}$ et deux nœuds non défaillants (honnêtes) exécutant la même machine à états déterministe produisent exactement la même valeur binaire ou le même condensat cryptographique ($H(m_1) = H(m_2)$). Le quorum se calcule par égalité de hachage sur les signatures des nœuds.
  À l'inverse, dans un ensemble de $N$ agents pilotés par des LLMs (même initialisés avec le même prompt et des graines pseudo-aléatoires fixes sur des accélérateurs hétérogènes, ou à température $T > 0$) :
  1. Les sorties textuelles de deux agents non défaillants ne sont **jamais identiques bit-à-bit** ($H(m_1) \neq H(m_2)$ presque sûrement) ;
  2. Une hallucination stochastique subtile produit un message syntaxiquement valide, hautement plausible et cohérent en surface (ce que le texte nomme « faux accord sémantique » p. 113), échappant à tout prédicat de validation syntaxique classique ;
  3. L'application d'un quorum de vote majoritaire traditionnel ($\lfloor (N-1)/3 \rfloor$) est inapplicable sans un opérateur de réduction ou de consensus sémantique. Or, si cet opérateur de consensus sémantique est lui-même un LLM juge, il réintroduit les mêmes propriétés de défaillance stochastique au niveau du consensus lui-même (récursion infinie de l'arbitre faillible).
- **Correctif formel ou contre-exemple explicite** :
  - *Démonstration mathématique de rupture* : Soit un quorum PBFT à $3f+1$ agents chargés de synthétiser une cote de crédit agentique. Même si $2f+1$ agents sont parfaitement alignés et exempts de biais malveillant, ils produiront $2f+1$ justifications textuelles et scores numériques avec des variances marginales (p. ex. 745, 750, 748). La règle de décision par égalité exacte ne peut dégager aucun quorum de messages identiques, bloquant le protocole en timeout indéfini.
  - *Formulation corrigée* : Expliciter que le consensus byzantin sur agents probabilistes exige un changement fondamental de paradigme : la transition d'un consensus binaire de transport vers un **consensus sur invariants logiques formalisés** (extraction de predicats typés vérifiables par des solveurs SMT ou automates déterministes, tel que le pont frame-déterministe du Ch. 29), seule méthode permettant de restaurer un prédicat de décision $V(m)$ calculable sans récursion stochastique.

---

### 6. [Majeur / Lacune méthodologique] Carence de modélisation de la concurrence, des collisions de verrous et de la double dépense sous AP2
- **Sévérité** : Majeur / Lacune méthodologique
- **Localisation précise** : Chapitre 10, pp. 115-118 (§ 10.1) et p. 123 (§ 10.3.4), mis en regard des directives du REVIEW_PLAN.md (segment S12, p. 115 de REVIEW_PLAN.md).
- **Diagnostic causal approfondi** :
  Le plan de revue imposait explicitement d'« Auditer les hypothèses de concurrence d'AP2 et disséquer la taxonomie des risques protocolaires (injection indirecte, collision de verrous) ».
  Or, le Chapitre 10 élude totalement la modélisation de la concurrence et des verrous sous AP2. Le texte se retranche derrière une « absence de documentation (degré 3) » au socle pour s'abstenir de modéliser les défaillances transactionnelles élémentaires inhérentes à tout protocole de paiement délégué autonome :
  - **Risque de double dépense et dépassement d'enveloppe budgétaire (Concurrent Budget Depletion)** : Lorsqu'un agent mandant délègue en parallèle des sous-tâches d'achat à trois sous-agents avec un Intent Mandate global plafonné à 1 000 $, AP2 ne spécifie aucun mécanisme d'allocation de verrous décentralisés ou de réservation transactionnelle de fonds (Two-Phase Commit ou Distributed Lock Manager). Deux agents peuvent simultanément présenter des Cart Mandates de 800 $ valides, menant à une collision transactionnelle au niveau du Payment Mandate.
  - **Collision de verrous d'inventaire marchand** : En raison du délai de latence d'inférence des agents LLM (plusieurs secondes à plusieurs dizaines de secondes pour valider un panier), les mécanismes classiques de réservation de panier (cart locks) expirent ou entrent en collision lors de négociations d'achat haute fréquence.
- **Correctif formel ou contre-exemple explicite** :
  - *Correctif technique* : Intégrer au § 10.1.4 et au § 10.4 une formalisation des patrons de compensation :
    Démontrer que le protocole AP2 ne peut pas fonctionner comme un simple empilement de mandats statiques signés (`Intent -> Cart -> Payment`), mais doit impérativement s'adosser à un patron de coordination transactionnelle de type **Saga distribuée à compensation asynchrone** avec sérialisation stricte des allocations budgétaires au niveau du fournisseur d'identité ou du compte mandant.

---

### 7. [Majeur / Lacune méthodologique] Omission des modèles de consistance (éventuelle vs forte), des fenêtres de révocation et des attaques Sybil dans les registres distribués
- **Sévérité** : Majeur / Lacune méthodologique (Axe R2 - Systèmes distribués)
- **Localisation précise** : Chapitre 9, pages 104-105, § 9.1.4 et § 9.1.5 :
  > « Trois familles d’initiatives coexistent : un annuaire fédéré centré sur les capacités, à adressage par contenu, signature de provenance et distribution par table de hachage ; un service de noms proposant une résolution analogue au système de noms de domaine... » (p. 104)
  > « La parade tient à l’attestation à chaque étage plutôt qu’à la confiance dans un opérateur unique : provenance cryptographique et adressage par contenu contre la carte mensongère et le squattage ; révocation coordonnée et signature des descriptions contre la résolution vers un imposteur. » (p. 105)
- **Diagnostic causal approfondi** :
  Le traitement des registres d'agents et annuaires distribués dans le Chapitre 9 fait l'impasse sur les théorèmes fondamentaux des systèmes distribués (Théorème CAP, PACELC) :
  1. **Consistance éventuelle vs Révocation de sécurité (Stale Discovery Window)** : Un registre distribué par table de hachage (DHT) ou réseau fédéré pair-à-pair fonctionne sous un régime de *consistance éventuelle* (availability / partition tolerance au détriment de la consistance immédiate). Le texte préconise la « révocation coordonnée », mais n'analyse pas l'intervalle de propagation $\Delta t_{\text{prop}}$ d'une révocation d'Agent Card ou de clé compromise. Pendant cette fenêtre de latence, un agent continue d'obtenir du registre une Agent Card valide et signe des contrats avec un agent révoqué.
  2. **Vulnérabilité aux attaques Sybil et empoisonnement de routage** : Dans un registre distribué ouvert basé sur DHT sans barrière de preuve de travail ou de participation économique lourde, la génération triviale d'identifiants virtuels permet à un attaquant de contrôler les nœuds responsables du hachage d'une capacité convoitée, redirigeant les requêtes de découverte vers des agents malveillants.
- **Correctif formel ou contre-exemple explicite** :
  - *Contre-exemple* : Un certificat d'agent malveillant $A_{\text{mal}}$ est révoqué par l'autorité d'enregistrement à $t_0$. La propagation de la liste de révocation (ou CRL / OCSP agentique) dans la table de hachage fédérée prend 15 minutes. À $t_0 + 5\text{ min}$, un agent financier interroge le registre, reçoit la carte mise en cache comme valide, et délègue l'exécution d'un transfert financier.
  - *Correctif* : Préciser que dans les architectures agentiques régulées, la découverte décentralisée sur DHT à consistance éventuelle est inacceptable pour les interactions critiques ; l'architecture doit imposer des **registres à consistance forte (CP)** adossés à des journaux de transparence d'annuaire immuables (Transparency Logs type Certificate Transparency / RFC 9162) avec vérification de non-révocation synchrone à l'exécution.

---

### 8. [Majeur / Lacune méthodologique] Biais méthodologique asymétrique de sécurité entre MCP et A2A par confusion entre absence de CVE et inviolabilité
- **Sévérité** : Majeur / Lacune méthodologique
- **Localisation précise** : Chapitre 11, page 132 (§ 11.1.4) et page 138 (Tableau 11.5 et § 11.4.2) :
  > « Le socle du Vol. II ne documente aucune attaque propre au protocole agent-agent, alors même que celui-ci ouvre une surface d’une autre nature — la délégation de tâches de pair à pair. Absence de documentation, degré 3... » (p. 132)
  > « La cinquième ligne du tableau ne se comble pas, et c’est celle qui compte le plus pour un architecte. Aucune attaque propre au protocole agent-agent n’est au corpus, ni au socle du Vol. II ni aux sources du Vol. I. Ce silence doit être lu comme une limite du corpus, en aucun cas comme un certificat de sûreté. » (p. 138)
- **Diagnostic causal approfondi** :
  Bien que l'auteur tente de se prémunir en répétant que « ce silence est une limite du corpus », la structure même de l'argumentation crée une asymétrie d'évaluation injustifiée dans un ouvrage destiné à éclairer des décisions d'architecture d'entreprise :
  - Le protocole MCP est disséqué à charge à grand renfort de vulnérabilités formelles (CVE-2025-6514, CVE-2025-49596, divulgation OX Security d'avril 2026 estimant 200 000 instances exposées, prompt injection dans les descriptions d'outils).
  - Le protocole A2A est présenté comme n'ayant « aucune attaque documentée au corpus », alors que les vecteurs d'attaque sur la communication inter-agents sont formellement identifiés dans la littérature scientifique contemporaine (notamment les extensions multi-agents d'AgentDojo, Debenedetti et al., 2025, cité au Ch. 6, et l'OWASP Top 10 for Agentic Applications cité au Ch. 11 lui-même sous l'item « communication inter-agents non protégée ») :
    1. Attaque par injection de contexte partagé dans les messages de délégation multi-tours ;
    2. Déni de service par bouclage de tâches récursives circulaires (circular task ping-pong) ;
    3. Usurpation d'Agent Card par attaque sur la chaîne de résolution DNS/HTTPS du domaine déclaré (`/.well-known/agent.json`).
  L'absence de CVE déposée contre l'implémentation de référence d'A2A (qui découle simplement de sa relative jeunesse et de son déploiement initial en environnement fermé/atelier) ne doit pas être traitée comme une absence de vulnérabilité architecturale.
- **Correctif formel ou contre-exemple explicite** :
  - *Correctif* : Rééquilibrer la section 11.1 en intégrant explicitement l'analyse théorique des vecteurs d'attaque propres à la délégation A2A (bouclages de tâches, désalignement par injection transitive dans les artefacts échangés, et substitution d'Agent Card par falsification DNS), même en l'absence d'un identifiant CVE spécifique dans les dépôts de vulnérabilités logicielles.

---

### 9. [Majeur / Lacune méthodologique] Omission du standard RFC 9449 (OAuth DPoP) face à la vulnérabilité structurelle des jetons porteurs (campagne UNC6395)
- **Sévérité** : Majeur / Lacune méthodologique
- **Localisation précise** : Chapitre 12, page 144, lignes 12002-12020 :
  > « La campagne suivie sous la désignation UNC6395 a donné accès, du 8 août 2025 à au moins le 18 août 2025, à des instances Salesforce au moyen de jetons OAuth compromis d’une application tierce... Le maillon qui cède y est nommé, et il est architectural : le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. »
- **Diagnostic causal approfondi** :
  L'analyse diagnostique avec exactitude la vulnérabilité architecturale des jetons porteurs (*bearer tokens*, RFC 6750) dans les architectures de délégation agentique. Toutefois, le texte présente cette lacune comme une fatalité non résolue de la pile OAuth héritée, omettant totalement de citer le standard normatif majeur approuvé par l'IETF pour combler précisément cette faille : **OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP, RFC 9449)**.
  DPoP lie cryptographiquement chaque jeton d'accès (et chaque requête HTTP) à une paire de clés asymétriques détenue exclusivement par le client appelant via un en-tête `DPoP` signé contenant un JWT horodaté avec nonce et hash de requête. Dans le scénario de la campagne UNC6395, un jeton DPoP exfiltré est totalement inutilisable par l'attaquant sans la clé privée de l'application cliente d'origine.
  Ignorer RFC 9449 dans une section dédiée précisément aux « standards étirés d'OAuth face à l'agent » affaiblit la portée des recommandations techniques faites aux architectes d'entreprises financières.
- **Correctif formel ou contre-exemple explicite** :
  - *Correctif textuel* : Ajouter au § 12.2 et au Tableau 12.1 :
    « Pour pallier la vulnérabilité intrinsèque des jetons porteurs révélée par la campagne UNC6395, l'architecture d'identité agentique doit proscrire le profil Bearer (RFC 6750) au profit du profil normatif de preuve de possession au niveau applicatif DPoP (RFC 9449). DPoP contraint chaque invocation d'API d'agent à présenter une preuve signée par clé privée éphémère ou matérielle, interdisant le rejeu d'un jeton dérobé sur un canal non maîtrisé. »

---

### 10. [Majeur / Lacune méthodologique] Surqualification disproportionnée d'AGNTCY au titre du Chapitre 10 en contradiction avec la vacuité documentaire admise
- **Sévérité** : Majeur / Lacune méthodologique
- **Localisation précise** : Chapitre 10, page 115 (Titre du chapitre et lignes 9494-9506) et pages 118-120 (§ 10.2) :
  > « 10 · Transaction et infrastructure : AP2 et AGNTCY » (p. 115)
  > « Le contenu du projet, tel que les sources le portent, tient en deux capacités : des annuaires de découverte (discovery directories) ; un transport nommé SLIM. C’est un vocabulaire d’infrastructure, non d’application... Les sources n’en disent pas davantage : ni spécification, ni statut de maturité, ni version. Absence de documentation (degré 3). » (p. 119)
- **Diagnostic causal approfondi** :
  L'architecture du plan du Livre I élève AGNTCY au rang de composant de premier niveau, figurant dans le titre même du Chapitre 10 au même titre qu'AP2, MCP et A2A. Pourtant, le corps du texte concède explicitement aux pages 119-120 qu'AGNTCY est une quasi-coquille vide documentaire dans le corpus analysé : ni spécification publique décortiquée, ni version stable, ni métrique de maturité vérifiée, et même une incapacité totale à élucider ce qu'est sa propre « composante ACP » (§ 10.2.3 et § 10.5.3, renvoyée au chapitre 49 !).
  Consacrer la moitié de l'intitulé d'un chapitre fondamental de la pile protocolaire à un projet industriel dont l'auteur admet qu'il n'a pu analyser ni le code, ni les protocoles, ni l'architecture au-delà d'un communiqué de presse de 2025 crée un déséquilibre épistémique frappant par rapport aux chapitres 8 et 9 qui dissèquent minutieusement les spécifications techniques de MCP et d'A2A.
- **Correctif formel ou contre-exemple explicite** :
  - *Correctif d'architecture rédactionnelle* : Rétrograder AGNTCY au statut d'étude de cas exploratoire d'infrastructure réseau au sein du § 9.2 (couches de transport d'infrastructure) ou renommer le Chapitre 10 : « 10 · Transaction et infrastructure : AP2 et les couches d'acheminement agentique », en ramenant AGNTCY à sa juste proportion illustrative d'initiative d'équipementier sans lui accorder une parité artificielle avec les protocoles fondateurs de l'écosystème.

---

# Minor Corrections and Typos

1. **Rupture textuelle et télescopage éditorial majeur au Chapitre 7.0 (p. 79)** :
   - *Localisation* : Page 79, lignes 6496-6508 de `DOCUMENT_TEXT_MAP.md` :
     > « fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.
     > Le second mouvement du Livre s’ouvre ici. Les ch. 1 à 3 ont posé le socle pré-agentique ; les ch. 4 à 6, l’ingénierie de l’agent. Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses »
   - *Diagnostic* : Deux phrases sont tronquées et télescopées lors du montage du texte. La fin de la phrase de la thèse (« ...instruit au ch. 10. ») est brutalement collée à un fragment (« outils, le dialogue... »), et le paragraphe suivant s'interrompt net (« ...le contrat entre un agent et ses ») sans ponctuation ni prédicat, la phrase suivante débutant par « La proposition directrice... ».
   - *Correction* : Réinsérer le texte manquant pour clore le syntagme : « ...le contrat entre un agent et ses outils, ses pairs et ses utilisateurs. »

2. **Troncature non explicitée du modèle LCIM à 5 niveaux au lieu de 7 (pp. 80-81, Tableau 7.1 & § 7.1.2)** :
   - *Localisation* : Page 80, Tableau 7.1 : « Les cinq niveaux du LCIM appliqués à la pile agentique ».
   - *Diagnostic* : Le modèle formel LCIM de Tolk & Muguira (2003) comporte canoniquement 7 niveaux (0 à 6 : Non-interoperable, Technical, Syntactic, Semantic, Pragmatic, Dynamic, Conceptual). Le texte ne cite que 5 niveaux en sautant le niveau 6 (Conceptuel - hypothèses sous-jacentes, modèles du monde et ontologies de contexte partagées).
   - *Correction* : Expliciter en note ou en texte que le niveau Conceptuel est délibérément fusionné avec le niveau Pragmatique/Sémantique dans l'adaptation agentique, ou restituer la nomenclature à 6/7 niveaux pour respecter la source théorique.

3. **Incohérence de maturité d'A2A v1.0 entre le Tableau 9.3 et le corps du texte (pp. 107-108 vs pp. 97, 100, 114)** :
   - *Localisation* : Page 107, Tableau 9.3 :
     > « Agent-agent : production ; version 1.0 stable, écosystème large »
   - *Diagnostic* : Le tableau attribue sans réserve le statut « production ; version 1.0 stable », alors que la page 97 admet quatre lacunes fondamentales non closes (dont l'ancrage de confiance racine des signatures et la date de la v1.0), que la page 100 concède que la négociation reste purement implicite et non formalisée, et que la page 114 affirme qu'« aucun banc standardisé véritablement inter-fournisseurs ne s'impose à juin 2026 ».
   - *Correction* : Nuancer le statut dans le tableau : « production émergente / standard de fait sous réserve d'évaluation inter-fournisseurs ».

4. **Coquille de composition p. 95 (lignes 7790-7793 de `DOCUMENT_TEXT_MAP.md`)** :
   - *Localisation* : Page 95, en bas du premier bloc :
     > « Revalidation du 30 juillet 2026 : la réserve ci-dessus a été validée par l’événement, et c’est le seul endroit de la somme où cela se produit. La révision »
   - *Diagnostic* : La phrase s'interrompt brutalement sur « La révision » juste au-dessus du bloc de la Figure 8.2 sans suite immédiate.
   - *Correction* : Supprimer le mot orphelin « La révision » ou compléter la phrase avant la figure.

5. **Erreur d'homogénéité terminologique sur les SVID SPIFFE (p. 141 vs p. 143)** :
   - *Localisation* : Page 141 (SPIFFE-ID et SVID) et page 143 (certificats X.509 de vingt-quatre heures chez Google Cloud).
   - *Diagnostic* : Le texte utilise indistinctement SVID et certificats X.509 traditionnels sans rappeler qu'un SVID SPIFFE peut être matérialisé soit sous forme de certificat X.509 (X509-SVID), soit sous forme de token JWT (JWT-SVID), chacun ayant des contraintes de transport et d'inspection très différentes pour un mandataire agentique.
   - *Correction* : Spécifier explicitement `X509-SVID` à la page 143.
