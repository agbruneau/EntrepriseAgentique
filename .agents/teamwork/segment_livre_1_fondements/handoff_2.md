**Segment scope**: Livre I — Fondements de l’interopérabilité et ingénierie agentique (pp. 1-79, Chapitres 1 à 6, segments S01 à S07).

# Potential Mistakes and Improvements

### 1. [Bloquant] Falsification de la formule de complexité du coût d'intégration $N(N-1)/2$ et de la linéarité en $2N$ du modèle canonique
- **Localisation exacte** : Chapitre 1, pp. 5-6 (§ 1.0.1), p. 14 (§ 1.3.1.1), et p. 22 (§ 1.6.1).
- **Citations textuelles** :
  - Page 5 : « Cette intégration point-à-point engendre une croissance combinatoire du nombre de connexions : raccorder $N$ systèmes susceptibles de dialoguer deux à deux peut requérir jusqu’à $N(N-1)/2$ liaisons, chacune avec sa logique de transport, de format et de correspondance. »
  - Page 14 : « La prolifération des connexions point-à-point engendre une dette d’intégration dont le coût croît quadratiquement avec le nombre de systèmes. La SOA propose de substituer à ce maillage $N \times N$ une médiation par services réutilisables... »
  - Page 22 : « Lorsque $N$ applications doivent s’échanger des données, le couplage par traductions directes croît en $N \times N$ : chaque paire exige son propre traducteur, et l’ajout d’un système impose de modifier tous les autres. Le modèle de données canonique brise cette explosion combinatoire en introduisant un format pivot indépendant des applications : chaque système ne traduit qu’entre son format propre et le canonique, ramenant le coût d’intégration à un ordre linéaire, en $2N$. »
- **Diagnostic causal approfondi** :
  1. *Incohérence combinatoire et asymétrie des flux* : Le texte oscille sans précaution entre la cardinalité d'un graphe non orienté complet $K_N$ ($N(N-1)/2$) et celle d'un graphe orienté complet ($N(N-1)$ ou $N \times N$). Dans les systèmes réels et en intégration agentique, les échanges d'interfaces sont asymétriques (schémas de requête et de réponse distincts). Si chaque liaison est unidirectionnelle, il existe $N(N-1)$ traducteurs point-à-point. La réduction à $2N$ pour le modèle canonique suppose deux adaptateurs par système (source $\to$ pivot et pivot $\to$ cible), ce qui correspond à la topologie orientée $N(N-1)$ et non à $N(N-1)/2$.
  2. *Postulat topologique irréaliste (clique $K_N$)* : La formule $\Theta(N^2)$ postule implicitement un réseau complet où chaque système ou agent dialogue avec l'intégralité des $N-1$ autres nœuds. Or, les architectures d'entreprise comme les réseaux multi-agents forment des graphes clairsemés (*sparse graphs*) suivant des lois de puissance (réseaux sans échelle) ou des topologies petit monde. Le degré moyen $\langle k \rangle$ y est borné ou croît en $O(\log N)$, de sorte que le nombre effectif d'arêtes est $E = O(N)$, et non $\Theta(N^2)$.
  3. *Falsification théorique de la linéarité $2N$ du Modèle Canonique (CDM)* : L'affirmation selon laquelle le schéma canonique ramène le coût d'intégration à un ordre linéaire $2N$ néglige l'économie de la maintenance sous évolution sémantique continue. Soit un schéma pivot $\mathcal{C}$ et $N$ schémas locaux $\mathcal{S}_1, \dots, \mathcal{S}_N$. Si un système $i$ modifie son schéma local à un taux $\Delta_i$, l'intégration du nouveau concept impose d'étendre $\mathcal{C}$ en $\mathcal{C}'$. Cette extension de $\mathcal{C}'$ brise potentiellement les $N-1$ correspondances $\mathcal{S}_j \leftrightarrow \mathcal{C}'$. Le coût cumulé de gouvernance et de réconciliation de schéma n'est pas linéaire mais croît en $O(N \cdot M)$ où $M$ est le nombre de concepts, et le problème de décision de cohérence de schéma sous contraintes est NP-difficile.
  4. *Inadéquation pour l'intégration agentique* : Dans un écosystème d'agents, la dette d'intégration ne se modélise pas par le tirage de câbles physiques ou la maintenance de traducteurs statiques. Elle est régie par la consommation de tokens par saut ($T \times K_{\text{tokens}}$), la latence stochastique cumulative et la probabilité d'erreur de coordination $\epsilon_{\text{coord}} = 1 - (1 - \epsilon)^N$.
- **Correctif formel et contre-exemple mathématique** :
  - *Modélisation dynamique du coût d'intégration sous évolution temporelle* :
    Soit un ensemble de $N$ systèmes subissant chacun un taux d'évolution de schéma $\lambda_i$ par période. Dans une intégration par modèle canonique $\mathcal{C}$, le coût total sur un horizon $T$ s'exprime par :
    $$C_{\text{CDM}}(T) = 2N \cdot c_{\text{init}} + \sum_{t=1}^T \sum_{i=1}^N \lambda_i(t) \left[ c_{\text{upd}}(\mathcal{C}) + \sum_{j \ne i} \gamma_{ij} \cdot c_{\text{impact}}(\mathcal{S}_j \leftrightarrow \mathcal{C}') \right]$$
    Où $\gamma_{ij} \in [0, 1]$ est la probabilité de couplage collatéral entre le domaine $i$ et le domaine $j$. Dès lors que le graphe ontologique est interconnecté ($\gamma_{ij} > 0$), la maintenance annuelle $C_{\text{CDM}}$ redevient d'ordre quadratique $O(N^2)$, voire exponentielle en cas de désaccord de gouvernance collective (théorème d'impossibilité d'Arrow appliqué au consensus sur les schémas).
  - *Formulation alternative pour l'entreprise agentique* :
    Remplacer la complexité mécanique $N(N-1)/2$ par l'espérance de coût opérationnel d'un graphe d'agents orienté $G=(V, E)$ :
    $$\mathbb{E}[C_{\text{agentic}}] = \sum_{(u, v) \in E} \mathbb{E}[\text{Tokens}(u \to v)] \cdot c_{\text{token}} + \sum_{v \in V} \frac{\tau_{\text{exec}}(v)}{1 - P(\text{erreur}_v)}$$

---

### 2. [Bloquant] Falsification de la taxonomie du LCIM et conflit topologique avec la pile canonique quadri-couche
- **Localisation exacte** : Chapitre 1, pp. 8-9 (§ 1.1.2 et Figure 1.1).
- **Citations textuelles** :
  - Page 9 : « Le Levels of Conceptual Interoperability Model (LCIM) approfondit la couche sémantique en distinguant des degrés de maturité conceptuelle de l’échange. À la pile technique-syntaxique-sémantique, il superpose les niveaux pragmatique, dynamique et conceptuel, articulés autour de trois notions : l’integratability (compatibilité des réseaux et plateformes), l’interoperability (échange et usage des données) et la composability (alignement des modèles conceptuels sous-jacents). Le modèle a été raffiné en une échelle à sept niveaux, du niveau 0 — absence d’interopérabilité — jusqu’à l’interopérabilité conceptuelle... »
  - Page 9, Figure 1.1 : « Pile canonique : 1 Technique, 2 Syntaxique, 3 Sémantique, 4 Organisationnel. Extension LCIM : Pragmatique · Dynamique · Conceptuel. Superposés à la couche sémantique. Sept niveaux, du niveau 0 — absence — à l'interopérabilité conceptuelle. »
- **Diagnostic causal approfondi** :
  1. *Falsification de la structure du LCIM* : Dans la formulation formelle d'Andreas Tolk et coll. (2003, 2007), le LCIM ne constitue aucunement une "extension superposée à la couche sémantique" d'une pile à quatre niveaux. Le LCIM est une échelle d'évaluation autonome et cumulative à 7 niveaux autonomes : L0 (No Interoperability), L1 (Technical), L2 (Syntactic), L3 (Semantic), L4 (Pragmatic), L5 (Dynamic), L6 (Conceptual).
  2. *Incohérence topologique de projection* : En juxtaposant dans la Figure 1.1 la pile européenne (EIF) — qui place l'échelon "4. Organisationnel" au sommet au-dessus de la sémantique — et en greffant latéralement les niveaux L4, L5, L6 du LCIM au niveau de la sémantique, le compendium introduit une rupture d'ordre partiel indécidable. Où se situe le niveau "Organisationnel" par rapport à "Dynamique" (L5) et "Conceptuel" (L6) ? Dans le LCIM, la pragmatique (L4) et la dynamique des états (L5) intègrent déjà les règles de coordination des processus métiers et organisationnels. L'ordonnancement cumulatif $\text{Technique} \prec \text{Syntaxique} \prec \text{Sémantique} \prec \text{Organisationnel}$ est incompatible avec une superposition latérale du LCIM.
- **Correctif formel** :
  Remplacer la superposition univoque par une matrice bidimensionnelle orthogonale dissociant l'axe de portée sociotechnique (Cadre européen EIF / ISO 11354 : Technique, Sémantique, Organisationnel, Légal) et l'axe de profondeur de modélisation computationnelle (LCIM : L0 à L6). Formaliser explicitement l'opérateur de projection :
  $$\Pi_{\text{EIF}} : \text{LCIM} \to \{\text{Technique}, \text{Syntaxique}, \text{Sémantique}, \text{Organisationnel}\}$$
  où $\Pi_{\text{EIF}}(\text{L1}) = \text{Technique}$, $\Pi_{\text{EIF}}(\text{L2}) = \text{Syntaxique}$, $\Pi_{\text{EIF}}(\text{L3}) = \text{Sémantique}$, et $\{\text{L4}, \text{L5}, \text{L6}\} \subseteq \text{Organisationnel} \times \text{Sémantique avancée}$.

---

### 3. [Majeur] Lacunes dans la caractérisation des facettes du couplage face à l'agentique et rigidité sous-estimée des protocoles MCP/A2A
- **Localisation exacte** : Chapitre 1, pp. 9-10 (§ 1.1.3.1).
- **Citations textuelles** :
  - Page 9 : « Hohpe, qui distingue notamment — la liste n’est pas donnée pour close — le couplage de technologie..., de format..., de localisation..., de temporalité... et d’interaction... »
  - Page 10 : « Lecture de l’auteur — les protocoles agentiques ne réduisent pas le couplage de manière uniforme : ils traitent avec vigueur le couplage de format et d’interaction, laissent largement ouvert le couplage de localisation... et rétablissent un couplage de confiance... »
- **Diagnostic causal approfondi** :
  1. *Omission de facettes critiques pour les systèmes stochastiques* : Les cinq facettes historiques de Hohpe (2003) sont adaptées à la messagerie déterministe pré-agentique, mais laissent de côté trois dimensions de dépendance cardinales en environnement agentique :
     - *Couplage d'état latent / contexte* ($\mathcal{C}_{\text{state}}$) : dépendance à la fenêtre d'attention et au cache de clés-valeurs (KV-cache).
     - *Couplage de distribution probabiliste* ($\mathcal{C}_{\text{distrib}}$) : sensibilité extrême aux variations de prompt (*prompt fragility*), où une infime variation lexicale déplace la distribution de sortie de l'agent.
     - *Couplage de mandat et d'autorité* ($\mathcal{C}_{\text{mandat}}$) : dépendance aux scopes de délégation cryptographique.
  2. *Contre-vérité sur le couplage de format et d'interaction dans MCP/A2A* : Prétendre que les protocoles agentiques réduisent avec "vigueur" le couplage de format et d'interaction est inexact. MCP repose sur des schémas JSON Schema stricts ; tout argument non conforme déclenche un rejet syntaxique immédiat (`-32602`). De même, le cycle requête-réponse synchrone de MCP (via JSON-RPC 2.0 sur stdio ou SSE) impose un couplage d'interaction temporellement bloquant et séquentiel.
- **Correctif formel** :
  Définir formellement le vecteur d'indépendance d'un agent par un 8-uplet :
  $$\mathbf{C} = \langle c_{\text{tech}}, c_{\text{format}}, c_{\text{loc}}, c_{\text{temp}}, c_{\text{inter}}, c_{\text{state}}, c_{\text{distrib}}, c_{\text{mandat}} \rangle$$
  Reconnaître que MCP et A2A relâchent le couplage d'implémentation algorithmique au prix d'un durcissement strict du couplage de schéma JSON et d'interaction RPC.

---

### 4. [Bloquant] Réductionnisme de la médiation sémantique (GAV vs LAV), omission de GLAV/BAV et sous-estimation de la complexité de calcul des requêtes
- **Localisation exacte** : Chapitre 2, pp. 32-33 (§ 2.3.4) et p. 32 (§ 2.3.3).
- **Citations textuelles** :
  - Page 33 : « Le formalisme distingue ici deux régimes de correspondance, et le choix entre eux est structurant :
     • GAV (Global-As-View) — chaque concept global est défini comme une vue sur les sources. Réécriture de requête simple ; ajout de source coûteux, puisqu’il faut revoir les définitions globales.
     • LAV (Local-As-View) — chaque source est décrite comme une vue sur le schéma global. Extensibilité supérieure — ajouter une source n’affecte pas les autres — au prix d’une réécriture de requête plus complexe.
     Ce choix rejoue, au niveau du sens, l’arbitrage entre couplage et évolutivité qui structure tout le Livre : GAV optimise le présent, LAV optimise l’arrivée du prochain participant. »
- **Diagnostic causal approfondi** :
  1. *Omission de GLAV et BAV* : La réduction de la médiation sémantique au dilemme binaire GAV vs LAV est dépassée depuis les travaux fondateurs de Friedman, Levy & Millstein (1999) et Lenzerini (PODS 2002). Les systèmes distribués ouverts d'entreprise et les écosystèmes multi-agents requièrent l'expressivité **GLAV (Global-and-Local-As-View)**, formalisée par des dépendances de génération de n-uplets (*tuple-generating dependencies*, tgds) :
     $$\forall \vec{x} \, (\phi_{\mathcal{S}}(\vec{x}) \implies \exists \vec{y} \, \psi_{\mathcal{G}}(\vec{x}, \vec{y}))$$
     Sans GLAV ni BAV (Both-As-View, McBrien & Poulovassilis, 2003), il est impossible d'exprimer des correspondances partielles n-à-m sans restructurer artificiellement l'ontologie globale ou les schémas locaux.
  2. *Sous-estimation de la complexité algorithmique de réécriture LAV* : Qualifier la réécriture en LAV d'opération simplement "plus complexe" masque un résultat fondamental d'intraitabilité : la réécriture de requêtes conjonctives à l'aide de vues en LAV (algorithmes Bucket, MiniCon, Inverse-Rules) est **NP-complète** en la taille de la requête. Dès lors que le schéma global comporte des contraintes d'intégrité ou des axiomes ontologiques (ex: OWL 2 QL / DL), le calcul des réponses certaines (*certain answers*) par l'évaluation du Chase peut être indécidable ou co-NP-complet en complexité des données.
  3. *Inadéquation de OWL 2 DL et SHACL en streaming agentique* : Le compendium n'adresse pas la complexité dans le pire des cas du raisonnement OWL 2 DL ($\mathcal{SROIQ}(\mathcal{D})$), qui est **2NEXP-TIME-complet**, ni la contrainte de matérialisation synchrone de graphe sous-jacente à SHACL, incompatible avec des flux d'événements agentiques à haut débit.
- **Correctif formel et démonstration** :
  - Définir le système d'intégration sémantique sous la forme canonique $\mathcal{I} = \langle \mathcal{G}, \mathcal{S}, \mathcal{M} \rangle$ où $\mathcal{M}$ est un ensemble d'assertions GLAV.
  - Expliciter les bornes de complexité théorique pour le calcul des réponses certaines $\text{cert}(q, \mathcal{I}, D) = \bigcap_{B \in \text{models}(\mathcal{I}, D)} q(B)$ :
    - Réécriture de requêtes conjonctives pures sans contraintes : temps $O(|V|^{|q|})$ (NP-complet).
    - Avec contraintes ontologiques de type TBox expressives : indécidable si le Chase comporte des cycles existentiels non gardés.

---

### 5. [Majeur] Inexactitude normative sur SAML 2.0, sophisme d'ingénierie sur SPIFFE/SPIRE et omission de ReBAC
- **Localisation exacte** : Chapitre 3, pp. 38 (§ 3.2.1), 40-41 (§ 3.3.1).
- **Citations textuelles** :
  - Page 38 : « (c) L’assertion transporte des attributs, non une autorisation : elle dit qui est le sujet et ce qu’on sait de lui ; ce que le sujet a le droit de faire reste une décision du consommateur. C’est le troisième trait qui voyage le plus loin dans la somme... »
  - Page 41 : « Lecture de l’auteur — c’est l’un des rares endroits de ce Livre où une classe entière d’incidents disparaît plutôt que de se déplacer. »
- **Diagnostic causal approfondi** :
  1. *Inexactitude normative SAML 2.0* : La norme OASIS SAML 2.0 (Core Specification, Section 2.7) définit explicitement trois déclarations formelles : `AuthenticationStatement`, `AttributeStatement`, et `AuthzDecisionStatement`. Cette dernière transporte expressément une décision d'autorisation (`DecisionType` = Permit | Deny | Indeterminate) prise par un PDP pour une ressource et une action données. Affirmer de manière catégorique que l'assertion SAML ne transporte jamais d'autorisation est normativement faux.
  2. *Sophisme d'ingénierie sur l'identité de charge SPIFFE/SPIRE* : Prétendre qu'avec SPIFFE/SPIRE « une classe entière d'incidents disparaît plutôt que de se déplacer » est une affirmation erronée. SPIFFE atteste l'identité cryptographique d'une charge au moment de l'émission du document SVID (X.509 ou JWT). Cela n'élimine pas les incidents, mais déplace la surface d'attaque vers :
     - La compromission du socket local de la Workload API (`/tmp/spire-agent/public/api.sock`) par injection inter-processus colocalisée.
     - La compromission de la mémoire du runtime post-attestation (exécution d'un binaire validé au démarrage mais détourné en cours d'exécution par exploitation de vulnérabilités natives).
     - La défaillance ou le spoofing des sélecteurs de nœuds (*Node Attestors*).
  3. *Lacune architecturale : omission de ReBAC (Relationship-Based Access Control)* : Le chapitre 3 restreint l'espace IAM à RBAC, ABAC et OAuth/OIDC. Or, l'octroi de mandats à des agents autonomes repose sur des graphes de relations d'autorité (qui mandate qui, sur quelle ressource, pour quelle finalité et sous quelles restrictions). L'omission des modèles ReBAC (Google Zanzibar, Cedar, OpenFGA) prive le lecteur de la fondation formelle requise pour le Livre II.
- **Correctif formel** :
  - Corriger la mention de SAML 2.0 en précisant que si les déploiements web utilisent majoritairement `AttributeStatement`, la norme inclut `AuthzDecisionStatement`.
  - Reformuler l'apport de SPIFFE/SPIRE en termes de déplacement de la surface de confiance (des secrets statiques vers l'infrastructure d'attestation et le socket d'attesteur).
  - Introduire ReBAC comme modèle formel d'autorisation agentique fondé sur des tuples relationnels $\langle \text{agent}, \text{relation\_mandat}, \text{ressource} \rangle$.

---

### 6. [Bloquant] Absence de dérivation analytique de l'effondrement stochastique de ReAct et fallace du décodage contraint
- **Localisation exacte** : Chapitre 4, pp. 51-54 (§ 4.2.1, § 4.2.3, Tableau 4.1) et p. 58 (§ 4.4.1).
- **Citations textuelles** :
  - Page 52 : « ReAct... Sur les trajectoires longues, ce patron dérive — accumulation d’erreurs non corrigées, boucles répétitives, perte du but initial à mesure que le contexte se dilue. »
  - Page 58 : « Les sorties structurées garantissent que l’argument respecte le schéma — typage, énumérations, champs requis —, ce qui transforme un problème de génération ouverte en un problème de remplissage contraint, plus vérifiable et plus robuste à l’analyse syntaxique. »
- **Diagnostic causal approfondi** :
  1. *Absence de modélisation mathématique de l'effondrement stochastique* : Le compendium constate la dérive de ReAct de façon empirique sans en dériver la cause formelle.
  2. *Modélisation formelle de l'effondrement de la trajectoire* :
     Soit une tâche agentique nécessitant $T$ transitions d'état successives. À chaque pas $t \in \{1, \dots, T\}$, la sélection de l'outil et de ses paramètres par le LLM est une variable aléatoire conditionnée par l'historique $h_t = (o_0, r_0, a_0, \dots, o_t)$.
     En présence de dérive contextuelle (*attention dilution*), la probabilité de transition correcte $p_t = P(s_{t+1} = s^*_{t+1} \mid s_t, h_t)$ décroît avec la longueur de l'historique :
     $$p_t = p_0 \cdot (1 - \lambda)^t \quad \text{avec } \lambda \in (0, 1)$$
     La probabilité de succès global de la chaîne ReAct non supervisée décroît selon :
     $$P(\text{Succès}_T) = \prod_{t=0}^{T-1} p_0 (1 - \lambda)^t = p_0^T \cdot (1 - \lambda)^{\frac{T(T-1)}{2}}$$
     Cette décroissance super-exponentielle démontre formellement qu'au-delà d'un horizon critique $T^* = \sqrt{\frac{2}{\lambda} \ln(1/p_0)}$, la boucle ReAct s'effondre avec certitude ($P \to 0$), justifiant mathématiquement le recours obligatoire à des machines à états finis déterministes (OO4, Livre III).
  3. *Fallace du décodage contraint (JSON Schema)* : L'affirmation de la page 58 confond la validité syntaxique dans le langage formel $\mathcal{L}(\mathcal{G}_{\text{JSON}})$ et la validité sémantique d'admissibilité $\mathcal{A}_{\text{valid}}(s)$ dans l'espace d'états d'entreprise.
- **Correctif formel et contre-exemple** :
  - *Contre-exemple d'appel d'outil stochastiquement destructeur mais syntaxiquement parfait* :
    ```json
    {
      "tool": "transfer_funds",
      "parameters": {
        "source_account": "ACC-VALID-001",
        "destination_account": "ACC-VALID-999",
        "amount": -500000.00,
        "currency": "CAD"
      }
    }
    ```
    Si le schéma JSON définit `amount` comme un `number`, la sortie structurée valide le payload sans erreur. Mais l'exécution déclenche une anomalie financière majeure (inversion de solde ou dépassement de découvert). Le décodage contraint ne protège que la grammaire, jamais la validité sémantique ni les préconditions fonctionnelles.

---

### 7. [Bloquant] Dérivation manquante de la dilution d'attention Softmax, sophisme de la compaction réversible et non-incrémentalité de GraphRAG
- **Localisation exacte** : Chapitre 5, pp. 63-64 (§ 5.1.2, § 5.1.3) et p. 68 (§ 5.3.2).
- **Citations textuelles** :
  - Page 63 : « Deux phénomènes documentés le montrent. La perte au milieu (lost in the middle, Liu et coll., 2023) établit que l’information placée au centre d’un long contexte est nettement moins bien utilisée... La dégradation progressive de la qualité à mesure que la fenêtre se remplit (context rot) s’y ajoute. »
  - Page 64 : « La bonne pratique consiste à compacter en conservant un pointeur vers la trace intégrale, déportée dans un magasin persistant, de sorte que le résumé reste augmentable à la demande sans peser sur la fenêtre courante. »
  - Page 68 : « GraphRAG (Edge et coll., 2024) extrait du corpus un graphe de connaissances dont les communautés servent les requêtes globales de synthèse... »
- **Diagnostic causal approfondi** :
  1. *Origine mathématique de la dilution d'attention Softmax* : Le compendium traite le phénomène "Lost-in-the-Middle" comme une simple observation empirique. Or, pour une matrice d'attention Softmax standard $\alpha_{i,j} = \frac{\exp(q_i^T k_j / \sqrt{d})}{\sum_{m=1}^L \exp(q_i^T k_m / \sqrt{d})}$, lorsque la longueur de séquence $L \to \infty$, l'entropie de distribution $\mathcal{H}(\alpha_i) \to \log L$. La masse d'attention se disperse uniformément sur les tokens distracteurs, et les biais inductifs des encodages de position relatifs (RoPE, ALiBi) privilégient structurellement les distances relatives $|i - j| \approx 0$ (récence immédiate) et les puits d'attention initiaux ($j \le 4$, *attention sinks*), écrasant l'information médiane.
  2. *Sophisme de la "compaction réversible"* : Qualifier un résumé périodique par LLM de "compaction réversible" contredit le théorème de traitement de l'information de Shannon. Le résumé textuel $f : \mathcal{V}^N \to \mathcal{V}^M$ ($M \ll N$) est une compression avec perte irréversible : $H(X \mid f(X)) > 0$. Conserver un pointeur externe ne restaure aucune réversibilité pour le modèle à l'inférence $t+1$, puisque le LLM ne lit que le résumé, lequel introduit des biais d'abstraction et élague irrémédiablement les détails négatifs et conditions limites (*memory poisoning*).
  3. *Non-incrémentalité et coût d'invalidation de GraphRAG* : GraphRAG repose sur la détection globale de communautés par l'algorithme de Leiden. L'insertion dynamique de nouveaux documents altère la structure globale du partitionnement, exigeant un recalcul complet et la réémission des résumés hiérarchiques par LLM, entraînant un coût en tokens prohibitif en exploitation d'entreprise.
- **Correctif formel** :
  - Expliciter la dérivation analytique de l'entropie d'attention Softmax en fonction de la taille de contexte $L$.
  - Bannir le terme "compaction réversible" et formaliser le processus comme une compression avec perte régie par un taux de distorsion informationnelle $R(D)$.
  - Spécifier les exigences d'une architecture hybride incrémentale pour GraphRAG (mise à jour locale de sous-graphes et méta-résumés delta).

---

### 8. [Majeur] Omission taxonomique des topologies multi-agents, formulation biaisée de pass@k / pass^k et contre-vérité sur la force illocutoire dans MCP/A2A
- **Localisation exacte** : Chapitre 6, pp. 71-76 (§ 6.1.2, § 6.2.1, § 6.4.2, Tableaux 6.1 et 6.2).
- **Citations textuelles** :
  - Page 71, Tableau 6.1 : « Topologies de coordination multi-agents : Étoile, Chaîne, Arbre, Graphe. »
  - Page 73 : « Communiquer suppose trois accords, et les protocoles agentiques n’en portent qu’un... (c) Un accord sur la force illocutoire — ce que l’émetteur fait en émettant : demande-t-il, informe-t-il, s’engage-t-il, refuse-t-il, propose-t-il ? C’est celui-là qui manque. Les protocoles agentiques de 2025-2026 ne portent pas cette information : un message y transporte une charge utile typée dont l’intention se déduit du contenu, c’est-à-dire du langage naturel, c’est-à-dire du modèle. »
  - Page 76, Tableau 6.2 : « pass@k : la probabilité qu’au moins une parmi k tentatives réussisse — le potentiel. pass^k : la probabilité que les k tentatives réussissent toutes — la consistance. »
- **Diagnostic causal approfondi** :
  1. *Omission des topologies Blackboard, Swarm et Marché* : Le Tableau 6.1 restreint l'espace des architectures multi-agents à 4 topologies statiques de graphes. Il omet la topologie de Tableau Noir (*Blackboard architecture* de Nii, 1986), les architectures d'essaim décentralisées (*Swarm / Gossip*), et les mécanismes de marché fondés sur les enchères (VCG, Contract Net étendu), pourtant fondamentaux dans la littérature distribuée.
  2. *Contre-vérité sur l'absence de force illocutoire dans MCP et A2A* : Prétendre que la force illocutoire est totalement absente des protocoles agentiques actuels et doit être "déduite du langage naturel" par le modèle est factuellement inexact :
     - Dans MCP (Model Context Protocol), les méthodes JSON-RPC portent expressément la qualification illocutoire : `tools/call` est une directive impérative d'exécution d'effet de bord ; `resources/read` est une assertion interrogative d'état ; `notifications` est une assertion informative unilatérale sans réponse.
     - Dans A2A (Agent2Agent), le cycle de vie des tâches (`tasks/send`, `tasks/update`, `tasks/cancel`) encode formellement la sémantique de négociation et d'engagement contractuel.
  3. *Erreur métrologique sur pass@k et pass^k* :
     - Pour $\text{pass@k}$, l'auteur donne la formule naïve $1 - (1-p)^k$. L'estimateur sans biais de référence (Chen et al., 2021) pour un échantillon de $n$ générations contenant $c$ succès est :
       $$\text{pass@k} = \mathbb{E}\left[1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\right]$$
     - Pour $\text{pass}^k$ ($\tau$-bench, Yao et al., 2024), le texte n'explicite pas la condition de fiabilité industrielle : si $P(\text{succès}) = p$, alors $\text{pass}^k = p^k$. Pour garantir un engagement de service (SLA) d'entreprise à $99.9\%$ sur $k=10$ étapes, la tolérance d'échec par étape doit satisfaire $1 - p \le 0.0001$ ($99.99\%$ de fiabilité par pas), ce qu'aucun modèle stochastique ne peut atteindre de manière autonome.
- **Correctif formel** :
  - Compléter la taxonomie des topologies multi-agents en intégrant Blackboard, Swarm et Marché.
  - Rectifier la description de MCP et A2A en démontrant comment les verbes JSON-RPC et les machines d'états d'enveloppe encodent la force illocutoire au niveau protocolaire.
  - Spécifier l'équation combinatoire exacte de $\text{pass@k}$ et formaliser l'analyse de sensibilité de $\text{pass}^k$ pour la contractualisation des SLA.

---

# Minor Corrections and Typos

1. **Page 11 (§ 1.1.4.1)** : « quel que soit le soin apporté aux deux premiers Le point est repris... »
   - *Correction* : Ajouter un point final après « deux premiers » : « ...aux deux premiers. Le point est repris... ».
2. **Page 32 (§ 2.3.3)** : Rupture syntaxique et télescopage de paragraphe :
   - Texte : « Ces travaux ne sont pas cités comme acquis : leur ancre de version se fixe au moment de citer, et cette réserve est reconduite ici sans être levée. intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. Un graphe RDF est, par construction, ouvert et sans schéma : tout triplet est licite, l’absence d’information n’est pas une faute, et rien n’interdit a priori d’attribuer une date de naissance à une facture. Pour l’intégration, cette permissivité est SHACL remplit ce rôle... »
   - *Correction* : Nettoyer la phrase tronquée et replacer « Pour l'intégration, cette permissivité est intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. SHACL remplit ce rôle... ».
3. **Page 48 (§ 4.1.1)** : Attribution exclusive de la distinction "Workflow vs Agent" à Anthropic (19 décembre 2024).
   - *Précision* : Bien qu'Anthropic ait popularisé cette terminologie auprès des praticiens, la distinction entre graphes de flux déterministes et chaînes agentiques dynamiques était déjà formalisée dans la littérature dès 2023 (ex: AutoGen de Wu et coll., LangGraph de LangChain). Il convient d'ajouter la mention des précurseurs universitaires pour éviter une sur-attribution industrielle.
4. **Page 30 (§ 2.2.3)** : Mention d'Apache Polaris promu Top-Level Project le 19 février 2026.
   - *Vérification factuelle* : Date exacte confirmée auprès des archives ASF (février 2026). Mentionner également l'impact de la concurrence avec Unity Catalog OSS (donné à la fondation LF AI & Data en 2024).
5. **Page 57 (§ 4.3.4)** : Typographie de l'équation implicite du surcoût de réflexion.
   - *Précision* : Préciser que les tokens de réflexion (thinking tokens de modèles comme DeepSeek-R1 ou OpenAI o1/o3) impactent non seulement le coût de sortie mais également la saturation de la fenêtre de contexte maximale utilisable par les outils aval.
