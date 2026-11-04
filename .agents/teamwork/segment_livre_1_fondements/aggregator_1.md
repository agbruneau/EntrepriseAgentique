**Segment scope**: Livre I — Fondements de l’interopérabilité et ingénierie des systèmes agentiques (pp. 1-79, Liminaires et Chapitres 1 à 6, amorce du Chapitre 7).

# Potential Mistakes and Improvements

### 1. **[Critical]** Falsification du modèle de coût d'intégration $N(N-1)/2$ vs $2N$, allégation erronée sur l'adjonction d'un système et illusion de linéarité en intégration agentique

- **Localisation exacte** : Chapitre 1, § 1.0.1 (pp. 5-6), § 1.3.1.1 (p. 14), § 1.6.1 (p. 22).
- **Citations textuelles exactes** :
  - Page 5 (§ 1.0.1) : *« Cette intégration point-à-point engendre une croissance combinatoire du nombre de connexions : raccorder N systèmes susceptibles de dialoguer deux à deux peut requérir jusqu’à N(N−1)/2 liaisons, chacune avec sa logique de transport, de format et de correspondance. »*
  - Page 6 (§ 1.0.1) : *« ...notamment par l’introduction d’un intermédiaire et d’un format pivot qui ramènent la complexité de N×N à un ordre linéaire (voir § 1.6.1). »*
  - Page 14 (§ 1.3.1.1) : *« ...la prolifération des connexions point-à-point engendre une dette d’intégration dont le coût croît quadratiquement avec le nombre de systèmes. La SOA propose de substituer à ce maillage N×N une médiation par services réutilisables... »*
  - Page 22 (§ 1.6.1) : *« Lorsque N applications doivent s’échanger des données, le couplage par traductions directes croît en N×N : chaque paire exige son propre traducteur, et l’ajout d’un système impose de modifier tous les autres. Le modèle de données canonique brise cette explosion combinatoire en introduisant un format pivot indépendant des applications : chaque système ne traduit qu’entre son format propre et le canonique, ramenant le coût d’intégration à un ordre linéaire, en 2N. »*
- **Diagnostic causal approfondi** :
  Ce passage cumule plusieurs erreurs mathématiques, topologiques et architecturales fondamentales :
  1. *Confusion formelle entre graphes orientés et non orientés* : La formule $N(N-1)/2$ correspond strictement au nombre d'arêtes d'un graphe complet non orienté $K_N$. Or, en intégration logicielle, les transformations de schémas sont asymétriques et directionnelles : un adaptateur $T_{A \to B}: \mathcal{S}_A \to \mathcal{S}_B$ ne réalise aucunement la transformation réciproque $T_{B \to A}: \mathcal{S}_B \to \mathcal{S}_A$ en raison des projections d'attributs non injectives. Dans le pire cas d'un maillage bilatéral exhaustif, le nombre de traducteurs orientés est strictement $N(N-1) = N^2 - N$. Par ailleurs, l'affirmation p. 22 selon laquelle un modèle pivot exige « $2N$ » adaptateurs (deux par système) correspond précisément à la réduction d'un graphe orienté complet $N(N-1)$ vers une topologie en étoile avec flux bidirectionnels ($2 \times N$), ce qui contredit directement la valeur de référence $N(N-1)/2$ avancée p. 5.
  2. *Affirmation factuellement et formellement fausse relative à l'adjonction d'un système* : Le texte affirme péremptoirement p. 22 que *« l'ajout d'un système impose de modifier tous les autres »*. C'est rigoureusement inexact en intégration point-à-point. L'introduction d'un $(N+1)$-ième nœud requiert au plus d'écrire $N$ nouvelles liaisons (soit $2N$ adaptateurs orientés) pour raccorder ce nouvel entrant aux systèmes existants. Les $\frac{N(N-1)}{2}$ liaisons bilatérales préexistantes demeurent strictement intactes et n'exigent aucune modification, en vertu du principe élémentaire de découplage des interfaces pair-à-pair.
  3. *Hypothèse topologique irréaliste (clique complète vs graphe clairsemé)* : Dans les architectures d'entreprise réelles, la topologie d'intégration n'est jamais une clique complète $K_N$, mais un graphe clairsemé (*sparse graph*), généralement sans échelle (*scale-free*) ou hiérarchique, où le degré moyen des nœuds est borné par une constante $\langle k \rangle \ll N$. Le nombre effectif d'arêtes est $|E| = \frac{1}{2} N \langle k \rangle = \mathcal{O}(N)$, conférant déjà à l'intégration point-à-point un coût structurel linéaire.
  4. *Fausse linéarité du modèle de données canonique (CDM) sous évolution sémantique* : Prétendre que le format pivot garantit un coût en $2N$ postule un schéma canonique $\mathcal{C}$ universel et immuable. Dès qu'un système source évolue ou émet des concepts non couverts par $\mathcal{C}$, le schéma pivot doit être révisé ($\mathcal{C} \to \mathcal{C}'$). Toute modification de $\mathcal{C}$ force l'audit et la réécriture potentielle des $2N$ adaptateurs existants. En théorie de l'intégration (Halevy, 2001 ; Bernstein, 2003), le coût d'arbitrage de gouvernance d'un modèle pivot croît de manière combinatoire en fonction des comités de normalisation inter-équipes ($\mathcal{O}(N^2)$ interactions humaines).
  5. *Inadéquation doctrinale pour l'intégration agentique* : Les systèmes multi-agents contemporains (via MCP ou A2A) n'adoptent ni le maillage d'adaptateurs statiques en $\mathcal{O}(N^2)$, ni le carcan rigide du CDM en $2N$. Chaque agent expose dynamiquement son schéma d'outil en $\mathcal{O}(1)$. La médiation est déplacée au runtime dans la fenêtre d'attention du LLM (*in-context dynamic grounding*). Le véritable coût n'est plus un coût de développement logiciel linéaire ou quadratique, mais un coût opérationnel récurrent stochastique par inférence (consommation de jetons, latence, dérive sémantique) et un risque de dégradation de la précision de sélection d'outils dès que le catalogue d'outils $M$ dépasse la vingtaine.
- **Correctif formel et modélisation rigoureuse** :
  Remplacer le modèle informel par une formalisation explicite en théorie des graphes :
  Soit un réseau d'intégration modélisé par un graphe orienté $G = (V, E)$ où $|V| = N$. Le nombre d'adaptateurs point-à-point requis est $|E| = \sum_{i=1}^N d^+(v_i)$. Dans le cas d'une clique orientée complète, $|E| = N(N-1) \approx N^2$. Dans un réseau d'entreprise réel à degré sortant borné par $k_{\max} \ll N$, $|E| \le k_{\max} N = \mathcal{O}(N)$.
  Lors de l'introduction d'un nouveau nœud $v_{N+1}$, le nombre d'arêtes ajoutées est $\Delta |E| = d^+(v_{N+1}) + d^-(v_{N+1}) \le 2N$, avec une invariance stricte des liaisons préexistantes : $\forall (u, w) \in E, \Delta E_{(u,w)} = 0$.
  Pour le modèle canonique, intégrer la probabilité d'évolution du schéma pivot :
  $$\mathbb{E}[\text{Coût}_{\text{CDM}}] = 2N \cdot c_{\text{adapt}} + \sum_{t=1}^T P(\Delta \mathcal{C}_t \neq \emptyset) \cdot [2N \cdot c_{\text{reval}} + c_{\text{gouv}}(N^2)]$$
  où $c_{\text{gouv}}(N^2)$ modélise l'explosion combinatoire du consensus organisationnel.

---

### 2. **[Critical]** Falsification de la métrique d'évaluation $\text{pass}^k$ de $\tau$-bench et confusion mathématique avec l'effondrement intra-trajectoire $q^T$

- **Localisation exacte** : Chapitre 6, § 6.4.2 (p. 76), Tableau 6.2 et Figure 6.4 (p. 76).
- **Citations textuelles exactes** :
  - Tableau 6.2 : *« pass^k ... la probabilité que les k tentatives réussissent toutes — la consistance. Chute brutalement dès que la fiabilité par étape s’éloigne de la perfection. »*
  - Page 76 : *« La seconde — pass^k, introduite par τ-bench (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues et multi-étapes. Cette dégradation — où une probabilité d’échec par pas même faible se compose géométriquement sur une longue trajectoire — est l’un des constats les plus robustes du domaine, et l’une des questions que le ch. 49 laisse ouvertes. »*
  - Figure 6.4 : *« pass^k — LA CONSISTANCE ... Les k tentatives réussissent toutes ... chute brutale dès que la fiabilité par étape s'éloigne de la perfection ... s'effondre avec k ... Une probabilité d’échec par pas même faible SE COMPOSE GÉOMÉTRIQUEMENT sur une longue trajectoire : c’est l’un des constats les plus robustes du domaine, et la raison pour laquelle un agent se caractérise par sa courbe de consistance... »*
- **Diagnostic causal approfondi** :
  Ce passage introduit une confusion probabiliste et méthodologique majeure en fusionnant deux grandeurs stochastiques orthogonales :
  1. *Définition formelle de $\text{pass}^k$ dans $\tau$-bench (Yao et coll., 2024)* : Dans le benchmark $\tau$-bench (*A Benchmark for Tool-Agent-User Interaction in Real-World Domains*, arXiv:2406.12045), la variable $k$ désigne le nombre de **réplications indépendantes (trials / runs)** de la *totalité d'une tâche*. Si un agent résout une tâche de bout en bout avec une probabilité globale $p \in [0, 1]$, la métrique de consistance $\text{pass}^k$ évalue la probabilité que l'agent réussisse $k$ exécutions complètes indépendantes : $\text{pass}^k = \mathbb{E}[p^k]$. L'exposant $k$ représente le nombre d'essais répétés, et non la longueur de la conversation ni le nombre d'étapes de la tâche.
  2. *Décomposition séquentielle intra-trajectoire* : Si une tâche comporte un horizon de $T$ étapes séquentielles, et que l'agent présente une probabilité de transition valide au pas $t$ notée $q_t = P(\text{étape}_t \text{ valide} \mid h_{t-1})$, la probabilité de succès global sur un run unique est $p = \prod_{t=1}^T q_t$. Si $q_t \equiv q < 1$, alors $p = q^T$. L'exposant $T$ est ici la profondeur temporelle de la trajectoire.
  L'auteur attribue formellement et textuellement l'effondrement de $\text{pass}^k$ à la composition géométrique d'une probabilité d'échec par étape sur une longue trajectoire. Ce contresens est patent :
  - Un agent évalué sur une tâche élémentaire en une seule étape ($T=1$) avec un taux de succès par run $p = 0.8$ voit son $\text{pass}^8 = (0.8)^8 \approx 0.168$ chuter à 16.8 %, alors qu'il n'existe aucune trajectoire multi-étapes.
  - Inversement, un agent opérant sur une trajectoire longue de $T=50$ pas peut présenter une consistance inter-essais mesurée pour $k=1, 2, \dots$, sans que la variable $k$ ne soit liée à l'horizon temporel $T$.
  Lier la métrique $\text{pass}^k$ de $\tau$-bench à la composition géométrique intra-trajectoire constitue une falsification de la littérature empirique de référence.
- **Correctif formel explicite** :
  Dissocier rigoureusement les deux concepts dans le corps du texte, le Tableau 6.2 et la Figure 6.4 :
  1. *Fiabilité intra-trajectoire (horizon temporel $T$)* : Pour une trajectoire de longueur $T$, le taux de succès d'une exécution $j$ est :
     $$P(S_j) = \prod_{t=1}^T P(a_t \in \mathcal{A}^* \mid s_t, h_{t-1}) = \prod_{t=1}^T q_t \le (\bar{q})^T$$
     qui tend vers 0 lorsque $T \to \infty$ dès que $\bar{q} < 1$.
  2. *Consistance inter-essais ($\text{pass}^k$ de $\tau$-bench)* : Pour $k$ réplications indépendantes d'une tâche de taux de succès global $p = P(S)$, la métrique de consistance est :
     $$\text{pass}^k = \mathbb{E}\left[ \prod_{j=1}^k \mathbb{I}(S_j) \right] = p^k$$
  La probabilité conjointe que $k$ essais indépendants d'une tâche à $T$ étapes réussissent tous s'écrit $\text{pass}^k(T) = \left( \prod_{t=1}^T q_t \right)^k$. Remplacer au Tableau 6.2 « fiabilité par étape » par « taux de succès global par exécution complète ».

---

### 3. **[Critical]** Rupture fondamentale du modèle AAA / Zero Trust face à la compromission d'intention sémantique, à l'injection indirecte et limites du Token Exchange

- **Localisation exacte** : Chapitre 3, § 3.1.1 (pp. 36-37), § 3.2.3 (pp. 39-40), § 3.3.1 (pp. 40-41).
- **Citations textuelles exactes** :
  - Page 36 : *« Le mandataire confus (confused deputy)... une passerelle qui réutilise ses propres droits au lieu de propager ceux du client transforme tout point d’entrée en vecteur d’escalade. C’est le défaut le plus important de cette sous-section pour la suite du Livre : il connaît une variante moderne dans les architectures agentiques, où une injection d’invite indirecte détourne le plan d’un agent en lui faisant traiter comme instructions des contenus externes. »*
  - Page 40 : *« Le zero-trust formalise le principe ne jamais faire confiance, toujours vérifier... point de décision et point d’application de politique, évaluation continue par requête... L’application du zero-trust aux services exige une identité pour les acteurs non humains, à durée de vie courte et vérifiable. SPIFFE et son implémentation de référence SPIRE fournissent à chaque charge un identifiant et un document d’identité vérifiable... »*
- **Diagnostic causal approfondi** :
  Le chapitre érige l'architecture Zero Trust (NIST SP 800-207) et les identités de charge de travail (SPIFFE/SPIRE, mTLS, JWT éphémères) en socle de sécurité pour l'entreprise agentique. Or, une rupture doctrinale et structurelle majeure est dissimulée :
  1. *Inopérance du PEP/PDP d'infrastructure face au détournement sémantique* : Les points d'application de politique (PEP) traditionnels filtrent les requêtes sur des métadonnées d'infrastructure (L4/L5) : adresse IP source, certificat X.509 SVID SPIFFE, jeton OAuth, méthode HTTP et URL cible. Lorsqu'un agent est subverti par injection de prompt indirecte (ex. données hostiles ingérées par RAG, ticket de support ou document non fiable), l'appel d'outil malveillant (`executerVirement(compte_attaquant, montant)`) est émis par le conteneur officiel de l'agent, muni de son certificat SPIFFE valide et de ses jetons IAM légitimes. Le PEP réseau valide la requête sans aucune anomalie constatable.
  2. *Effondrement de l'authenticité d'intention (Intent Authenticity Collapse)* : Le modèle AAA classique (Authentication, Authorization, Accounting) repose sur le postulat implicite que l'authenticité de l'émetteur garantit la légitimité de son intention. En présence d'un agent orchestré par un LLM, cette équivalence s'effondre : une charge cryptographiquement authentique peut formuler une intention hostile dictée par des données tierces non fiables.
  3. *Inadéquation de RFC 8693 (OAuth 2.0 Token Exchange) aux topologies agentiques complexes* : Le mécanisme de token exchange décrit p. 39 est conçu pour des flux d'appels linéaires statiques ($A \to B \to C$). Dans un essaim multi-agents avec délégation récursive, embranchements concurrents et sous-tâches asynchrones, RFC 8693 impose un aller-retour synchrone vers le serveur d'autorisation centralisé (AS) à chaque délégation, créant un goulot d'étranglement et empêchant l'atténuation cryptographique locale hors ligne (telle que garantie par les jetons *Biscuit*, *UCAN* ou *Macaroons*).
- **Correctif formel et modèle de contrôle des flux d'information (IFC)** :
  Formaliser l'inadéquation du triplet classique de contrôle d'accès $\mathcal{AC} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O} \rangle$ (Sujet, Action, Objet).
  Intégrer le modèle formel de contrôle des flux d'information (Information Flow Control, Myers & Liskov, 1997 ; Denning, 1976) :
  $$\mathcal{AC}_{\text{agent}} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O}, \mathcal{L}_{\text{input}}, \mathcal{L}_{\text{output}} \rangle$$
  où $\mathcal{L}_{\text{input}}$ consigne le niveau d'intégrité et de classification de toutes les données absorbées dans le contexte d'attention du modèle. Poser l'invariant de non-interférence sémantique (Goguen & Meseguer, 1982) :
  $$\forall d \in \text{Context}(\text{Agent}), \quad \text{Tainted}(d) \implies \text{Capabilities}(\text{Agent}) \cap \text{SideEffectTools} = \emptyset$$
  Tout agent ayant absorbé des données non fiables doit voir ses autorisations d'effets de bord révoquées dynamiquement au PEP sémantique.
  Pour la délégation dynamique, remplacer RFC 8693 par une infrastructure d'autorisations cryptographiquement atténuables localement (jetons *Biscuit* fondés sur des prédicats Datalog atténuables sans consultation du serveur d'autorisation).

---

### 4. **[Critical]** Amplification stochastique dans la boucle ReAct, divergence cumulative et illusion de terminaison par budget

- **Localisation exacte** : Chapitre 4, § 4.2.1 (pp. 51-52), § 4.2.3 (pp. 53-54), § 4.4.4 (p. 60).
- **Citations textuelles exactes** :
  - Page 52 : *« L’entrelacement raisonnement-action — ReAct... à chaque pas, une étape de raisonnement verbalisé et une action dont le résultat est réinjecté avant le pas suivant... Chaque tour consomme des jetons en proportion du contexte accumulé... Sur les trajectoires longues, ce patron dérive — accumulation d’erreurs non corrigées, boucles répétitives, perte du but initial à mesure que le contexte se dilue. »*
  - Page 52 (Mise en œuvre) : *« Le critère d’arrêt n’est pas un détail mais une garantie de terminaison. Une boucle sans budget d’appels explicite ni détection de stagnation peut diverger... Fixer dès la conception un budget de pas, un plafond de jetons et une condition d’échec contrôlé relève du contrat opérationnel de l’agent... »*
  - Page 60 : *« La robustesse repose sur des mécanismes empruntés à l’ingénierie des systèmes distribués — le disjoncteur et le cloisonnement... auxquels s’ajoutent les réessais avec temporisation exponentielle... »*
- **Diagnostic causal approfondi** :
  1. *Confusion entre avortement sur dépassement et terminaison correcte* : Déclarer qu'un budget de pas ou un plafond de jetons constitue une « garantie de terminaison » confond l'avortement forcé sur expiration de délai (*timeout abort*) et la terminaison bien fondée de l'algorithme (*well-founded termination / total correctness*). Lorsque le budget de pas $K$ est atteint, la tâche n'est pas résolue : elle est interrompue arbitrairement dans un état intermédiaire incohérent, laissant des effets de bord partiels non annulés dans les systèmes cibles (ex. virement pré-autorisé non complété, fichier temporaire verrouillé).
  2. *Inadéquation des réessais temporels exponentiels face aux pannes sémantiques* : Dans les systèmes distribués, la temporisation exponentielle résout des contentions réseau transitoires. Dans une boucle agentique, si un appel d'outil échoue en raison d'un argument halluciné, d'un schéma non respecté ou d'une prémisse fausse, réitérer l'appel sans altérer la distribution de probabilité du LLM reproduit la défaillance à l'identique.
  3. *Amplification stochastique en boucle fermée et piège d'auto-correction* : Dans ReAct, l'inférence au pas $t$ est conditionnée par l'historique complet :
     $$P(a_t, r_t \mid s_0, r_1, a_1, o_1, \dots, r_{t-1}, a_{t-1}, o_{t-1})$$
     Dès qu'une observation erronée ou un raisonnement fautif pénètre le contexte au temps $\tau < t$, cette erreur pollue l'auto-attention. Les travaux empiriques (Huang et al., 2023 ; Stechly et al., 2024) démontrent que réinjecter l'erreur dans la fenêtre de contexte d'un modèle sans oracle ou vérificateur externe déterministe dégrade la performance dans plus de 60 % des cas. De plus, comme ReAct entrelace pensée et action ($2K$ étapes stochastiques pour $K$ actions), la probabilité de complétion sans erreur s'effondre en $(1 - \epsilon)^{2K} \ll (1 - \epsilon)^K$.
- **Correctif formel et modèle POMDP supervisé** :
  Formaliser la délibération comme un Processus de Décision Markovien Partiellement Observable (POMDP). Remplacer la prescription du budget passif et des réessais aveugles par un **automate de surveillance externe déterministe (Safety Supervisor Automaton)** adossé au patron Saga :
  Soit $S$ l'état des systèmes externes. Chaque action $a_t$ émise par l'agent doit être filtrée par un automate d'états finis $\mathcal{M} = \langle Q, \Sigma, \delta, q_0, F \rangle$ validant les préconditions d'intégrité transactionnelle. Si le plafond de pas $K$ est atteint sans atteindre l'état final $F$, l'automate bloque l'agent et exécute automatiquement un protocole déterministe de rollback compensatoire pour restaurer l'état initial $S_0$.

---

### 5. **[Critical]** Faux parallélisme d'extensibilité GAV vs LAV en intégration sémantique, indécidabilité de réécriture et inapplicabilité de SHACL au runtime

- **Localisation exacte** : Chapitre 2, § 2.3.3 (p. 32), § 2.3.4 (pp. 32-33), § 2.4.1 (pp. 34-35).
- **Citations textuelles exactes** :
  - Page 33 : *« Le formalisme distingue ici deux régimes de correspondance, et le choix entre eux est structurant :
  • GAV (Global-As-View) — chaque concept global est défini comme une vue sur les sources. Réécriture de requête simple ; ajout de source coûteux, puisqu’il faut revoir les définitions globales.
  • LAV (Local-As-View) — chaque source est décrite comme une vue sur le schéma global. Extensibilité supérieure — ajouter une source n’affecte pas les autres — au prix d’une réécriture de requête plus complexe.
  Ce choix rejoue, au niveau du sens, l’arbitrage entre couplage et évolutivité qui structure tout le Livre : GAV optimise le présent, LAV optimise l’arrivée du prochain participant. »*
  - Page 34 : *« La gouvernance du sens en environnement distribué impose donc de traiter la sortie du modèle comme une proposition soumise à validation — par SHACL (§ 2.3.3), par revue experte, par confrontation aux axiomes ontologiques — et non comme un contrat établi. »*
- **Diagnostic causal approfondi** :
  1. *Omission de la NP-complétude et de l'indécidabilité de LAV* : Qualifier la réécriture de requête en LAV de simplement « plus complexe » occulte des résultats fondamentaux de la théorie des bases de données. Dans le paradigme LAV (*Answering Queries Using Views*, Levy et al., 1995 ; Halevy, 2001 ; Lenzerini, 2002), trouver la réécriture maximale contenue (*maximally contained rewriting*) pour des requêtes conjonctives est un problème **NP-complet** en la taille de la requête (Abiteboul & Duschka, 1998). Des algorithmes comme *Bucket* ou *MiniCon* (Pottinger & Halevy, 2001) subissent une explosion combinatoire exponentielle dès que le schéma s'étend, et le problème devient indécidable en présence de contraintes d'intégrité référentielle ou d'axiomes ontologiques expressifs (TBox OWL).
  2. *Inadéquation cognitive des LLMs et omission de GLAV* : Un agent LLM est incapable de garantir mathématiquement la correction d'une réécriture LAV sans un moteur Datalog déterministe sous-jacent. De plus, la pratique moderne de l'intégration sémantique a dépassé la dichotomie GAV/LAV au profit de **GLAV (Global-and-Local-As-View)** et des dépendances génératrices de tuples (*tgds*, Fagin et coll., 2005 : $\phi_{\mathcal{S}}(\mathbf{x}) \to \exists \mathbf{y} \psi_{\mathcal{G}}(\mathbf{x}, \mathbf{y})$), seul formalisme capable d'associer des vues sources à des vues globales pour des flux d'agents hétérogènes.
  3. *Inapplicabilité opérationnelle de SHACL au runtime des agents* : Recommander SHACL pour valider les sorties d'agents en direct (§ 2.4.1) méconnaît les exigences de performance temps réel. SHACL requiert la sérialisation d'un graphe RDF et l'exécution d'un moteur de règles sur graphe, induisant une pénalité de latence de plusieurs secondes par appel d'outil. En production agentique contemporaine, la validation sémantique et syntaxique à l'exécution est garantie au niveau des tokens par **décodage guidé par grammaires** (*grammar-guided decoding* / *structured outputs* via JSON Schema projeté sur des automates à pile déterministes sur logits, implémenté dans vLLM, SGLang, Outlines), reléguant SHACL à l'audit asynchrone des graphes de connaissances.
- **Correctif formel et contre-exemple explicite** :
  Exposer le théorème d'impossibilité de réécriture équivalente par un contre-exemple concret :
  Soit une ontologie globale $\mathcal{G}$ avec les relations $\text{Agent}(x)$, $\text{Mandat}(x, y)$, $\text{Institution}(y)$.
  En LAV, soient deux vues d'agents $V_1, V_2$ définies par :
  $$V_1(x) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$$
  $$V_2(y) \leftarrow \text{Institution}(y)$$
  Pour une requête globale $Q(x, y) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$, aucune réécriture exacte équivalente n'existe à partir de $V_1$ et $V_2$ car la variable de jointure $y$ est projetée hors de $V_1$. Seule une réécriture contenue non équivalente est dérivable.
  Prescrire formellement l'utilisation de médiateurs GLAV déterministes et substituer au contrôle SHACL synchrone le décodage contraint par automates finis sur logits.

---

### 6. **[Critical]** Irréversibilité informationnelle de la compaction mémorielle et boucle d'amplification des hallucinations persistantes (dérive épistémique)

- **Localisation exacte** : Chapitre 5, § 5.1.2 (pp. 63-64), § 5.2.1-5.2.2 (pp. 65-66).
- **Citations textuelles exactes** :
  - Page 64 : *« L’enjeu de conception est la réversibilité. Une compaction agressive risque d’effacer un détail qui redeviendra pertinent ; une compaction trop prudente ne libère pas assez de budget. La bonne pratique consiste à compacter en conservant un pointeur vers la trace intégrale, déportée dans un magasin persistant, de sorte que le résumé reste augmentable à la demande sans peser sur la fenêtre courante. »*
  - Page 66 : *« Une mémoire mal gérée devient une source d’hallucinations : un agent qui rappelle un fait erroné avec aplomb propage l’erreur sur toute la trajectoire... la différence avec une hallucination ordinaire tiendrait à ce que l’hallucination mémorielle est persistante et auto-confirmante, l’agent relisant le souvenir erroné à la session suivante. »*
- **Diagnostic causal approfondi** :
  1. *Paradoxe épistémique de l'agent et illusion de réversibilité* : Le texte soutient qu'un résumé compacté demeure « augmentable à la demande » grâce à la conservation d'un pointeur vers la trace brute déportée. Or, dans un processus de décision séquentielle, l'agent décide de requérir la trace brute uniquement à partir des données présentes dans sa fenêtre d'attention active. Si le résumé compacté a omis un détail contextuel critique $D$, l'agent ne dispose d'aucun signal pour savoir que $D$ a existé, ni qu'il devrait déréférencer le pointeur. En théorie de l'information (théorème de Shannon sur la compression avec perte), la compaction sémantique par un LLM est une projection non injective irréversible :
     $$I(X; S) < H(X)$$
     Qualifier cette compaction de « réversible » par simple stockage d'un pointeur passif est une illusion conceptuelle.
  2. *Instabilité en boucle fermée de l'hallucination mémorielle (Epistemic Drift)* : Dans les architectures de mémoire long terme (Mem0, Letta, Zep), les faits mémorisés sont extraits par un LLM. Si un fait erroné $\hat{F}$ est consigné dans le magasin vectoriel, il est ultérieurement rappelé lors d'un prompt futur avec un score de similarité élevé et réinjecté comme « fait d'ancrage vérifié ». Le modèle dérive alors de nouveaux faits fallacieux $\hat{G}_1, \hat{G}_2$ qui sont réécrits en mémoire. Cette rétroaction positive induit une divergence épistémique irréversible en l'absence de vérification externe.
- **Correctif formel et maintien de la vérité (Truth Maintenance System)** :
  Modéliser la compaction mémorielle comme un canal à distorsion de débit $R(D)$. Imposer un système de maintien de la vérité basé sur les dépendances (Assumption-based Truth Maintenance System - ATMS, de Kleer, 1986 ; Doyle, 1979) :
  Chaque fait consigné $F_i$ doit comporter un graphe de justification formel :
  $$J(F_i) = \langle \text{SourcesPrimaires}, \text{RèglesInférence}, \text{Timestamp}, \text{StatutValidité} \rangle$$
  Toute rétraction d'une source primaire $S_k \to \bot$ doit déclencher une cascade d'invalidation automatique sur l'arbre de dépendances :
  $$\forall F \text{ tel que } S_k \in J(F), \quad F \gets \text{Invalide}$$
  interdisant la ré-injection de croyances orphelines dans les contextes futurs.

---

### 7. **[Major]** Évasion théorique majeure : exclusion arbitraire du consensus distribué et de la coordination sous partition réseau en environnement financier

- **Localisation exacte** : Chapitre 1, § 1.6.2.2 (pp. 23-24).
- **Citation textuelle exacte** :
  - Page 23-24 : *« ...l’accord entre agents sous asynchronie et défaillance partielle — ce que deux agents tiennent pour vrai quand le réseau se partitionne — est en revanche hors du périmètre de la somme, et cela se dit ici plutôt que de se laisser découvrir. Ce périmètre est une décision d’auteur, prise le 27 juillet 2026 : assumé et déclaré. La somme ne traitera pas cette matière — ni ici, ni au ch. 6, ni au ch. 37, ni au ch. 48, les trois points d’atterrissage d’abord prévus étant fermés par la même décision. »*
- **Diagnostic causal approfondi** :
  - Dans un ouvrage de 663 pages intitulé *Interopérabilité et Orchestration en Entreprise Agentique*, dont le sous-titre cible spécifiquement les « services financiers réglementés (2024-2032) », décréter que le problème de l'accord distribué sous partition réseau est hors périmètre constitue une dérobade doctrinale injustifiable.
  - Les systèmes multi-agents en finance sont des systèmes distribués asynchrones par nature. Lorsque des agents de compensation, de paiement (AP2, Lynx, ISO 20022) ou d'arbitrage de liquidité interagissent, les partitions réseau et les délais de propagation de messages sont inévitables.
  - Le théorème CAP (Brewer ; Gilbert & Lynch, 2002) et le théorème d'impossibilité FLP (Fischer, Lynch, Paterson, 1985) s'appliquent de plein droit aux réseaux d'agents. Déclarer forfait sur ce que deux agents « tiennent pour vrai quand le réseau se partitionne » fragilise les fondements des Livres III et V, qui prétendent bâtir une orchestration déterministe et une sémantique d'effet sans disposer d'un modèle d'accord robuste sous défaillance.
- **Correctif formel** :
  Réintégrer la théorie du consensus distribué dans l'architecture agentique : spécifier comment les protocoles de consensus déterministes (Raft, Paxos ou Byzantine Fault Tolerance pour les domaines sans confiance) s'articulent avec les patrons Saga et la réconciliation compensatoire pour borner les fenêtres d'incohérence financière temporaire.

---

### 8. **[Major]** Incohérence taxonomique structurelle entre la pile canonique EIF et les paliers du LCIM, et caractérisation contradictoire du couplage agentique sous MCP

- **Localisation exacte** : Chapitre 1, § 1.1.2 (p. 8), Figure 1.1 (p. 9), § 1.1.3.1 (p. 10), § 1.2.1 (p. 11).
- **Citations textuelles exactes** :
  - Page 9 (Figure 1.1) : *« Figure 1.1 — La pile canonique d’interopérabilité, son extension par le LCIM et le palier où opèrent MCP et A2A. »*
  - Page 10 (§ 1.1.3.1) : *« Lecture de l’auteur — les protocoles agentiques ne réduisent pas le couplage de manière uniforme : ils traitent avec vigueur le couplage de format et d’interaction... »*
  - Page 11 (§ 1.2.1) : *« L’articulation canonique retient quatre niveaux : juridique... organisationnel... sémantique... et technique... »*
- **Diagnostic causal approfondi** :
  1. *Collision taxonomique EIF / LCIM* : À la page 8 et sur la Figure 1.1 (p. 9), l'auteur pose une pile canonique à 4 niveaux : 1 Technique $\to$ 2 Syntaxique $\to$ 3 Sémantique $\to$ 4 Organisationnel. Deux pages plus loin (§ 1.2.1, p. 11), il définit l'« articulation canonique » selon l'European Interoperability Framework (EIF) avec 4 niveaux : Technique $\to$ Sémantique $\to$ Organisationnel $\to$ Juridique (éliminant le niveau syntaxique pour insérer le juridique au sommet). Parallèlement, sur la Figure 1.1, il greffe les niveaux Pragmatique, Dynamique et Conceptuel du LCIM en les plaçant en vis-à-vis de la couche sémantique, tout en conservant le niveau « Organisationnel » au-dessus. Or, dans le modèle formel LCIM (Tolk & Muguira, 2003), le niveau 4 (Pragmatique) correspond précisément à l'alignement des procédures et des flux métier (le niveau organisationnel de l'EIF), tandis que le niveau 6 (Conceptuel) porte sur les hypothèses d'ingénierie du domaine. Cette hybridation confuse empêche de situer où se formalise juridiquement et opérationnellement l'accord entre agents.
  2. *Caractérisation erronée de l'effet de MCP sur le couplage* : L'affirmation selon laquelle les protocoles agentiques « traitent avec vigueur le couplage de format et d’interaction » est contredite par la spécification technique de MCP :
     - *Couplage de format* : MCP impose un couplage fort via JSON-RPC 2.0 et des schémas JSON Schema stricts. Si un argument d'appel d'outil diverge d'un type ou omet un champ requis, le serveur MCP rejette la requête immédiatement avec l'erreur `-32602 Invalid params`. L'inférence du LLM ne dispose d'aucune tolérance structurelle magique face à un schéma d'outil rigide.
     - *Couplage d'interaction* : MCP est un protocole de type requête-réponse synchrone et bloquant (sur stdio ou Server-Sent Events). Il ne fournit aucun mécanisme natif d'interaction asynchrone, de chorégraphie découplée ou de reprise sur incident.
- **Correctif formel** :
  Harmoniser les définitions en séparant nettement le cadre organisationnel de gouvernance (EIF : Technique, Sémantique, Organisationnel, Juridique) et le cadre de maturité de composabilité des systèmes (LCIM : 7 niveaux de 0 à 6). Rectifier la qualification de MCP en soulignant qu'il standardise le méta-contrat de transport et de découverte, mais maintient un couplage de format rigide et une interaction synchrone bloquante.

---

### 9. **[Major]** Falsification du diagnostic d'échec de FIPA-ACL et omission des protocoles d'engagements sociaux décidables

- **Localisation exacte** : Chapitre 4, § 4.1.3 (p. 49), Chapitre 6, § 6.2 et § 6.2.1 (pp. 72-73).
- **Citation textuelle exacte** :
  - Page 73 : *« Communiquer suppose trois accords, et les protocoles agentiques n’en portent qu’un... (c) Un accord sur la force illocutoire — ce que l’émetteur fait en émettant : demande-t-il, informe-t-il, s’engage-t-il, refuse-t-il, propose-t-il ? C’est celui-là qui manque. Le contraste avec l’héritage multi-agents classique est net... KQML... puis FIPA-ACL... avaient fait de la force illocutoire un champ obligatoire du message... Les protocoles agentiques de 2025-2026 ne portent pas cette information : un message y transporte une charge utile typée dont l’intention se déduit du contenu, c’est-à-dire du langage naturel, c’est-à-dire du modèle. »*
- **Diagnostic causal approfondi** :
  Si le constat de la perte de la force illocutoire explicite dans MCP et A2A est pertinent, le diagnostic historique et l'alternative architecturale souffrent d'une lacune majeure :
  1. *Cause réelle de l'échec industriel de FIPA-ACL* : L'auteur note avec réserve que le socle ne documente pas les motifs du déclin de FIPA-ACL. Or, la recherche en systèmes multi-agents a formellement documenté cette cause (Singh, 1998, 2000 ; Wooldridge, 2002) : la sémantique de FIPA-ACL était fondée sur des états mentaux internes inobservables (logique BDI de Cohen et Levesque), exigeant qu'un agent vérifie la « sincérité » de l'émetteur. Il était rigoureusement impossible pour un vérificateur tiers ou un tribunal d'auditer la conformité d'un agent sans accéder à ses états cognitifs privés, ce qui a disqualifié FIPA-ACL dans les transactions inter-entreprises.
  2. *Omission de la théorie moderne des engagements sociaux (Social Commitments)* : Le dépassement de FIPA-ACL n'a pas consisté à abandonner la force illocutoire au profit de prose probabiliste non typée, mais à formaliser les **engagements sociaux** (Singh, 2000 ; Fornara & Colombetti, 2004) sous forme d'engagements conditionnels auditables :
     $$C(\text{débiteur}, \text{créancier}, \text{antécédent}, \text{conséquent})$$
     Les transitions du cycle de vie d'un engagement (Créé, Actif, Rempli, Violé, Annulé) sont calculables par des automates d'états finis déterministes à partir des messages publics échangés, sans spéculer sur la psychologie interne de l'agent.
- **Correctif formel** :
  Substituer à la déploration passive de FIPA-ACL la prescription d'une couche d'engagements sociaux formels adossée à A2A, garantissant l'opposabilité juridique et contractuelle des transactions inter-agents sans dépendre d'inférences floues de LLM.

---

### 10. **[Major]** Conflit logique formel entre la monotonicité d'OWL 2 DL et le non-déterminisme des flux d'agents

- **Localisation exacte** : Chapitre 2, § 2.3.1 et § 2.3.3 (pp. 31-32), § 2.4.1 (p. 34).
- **Citations textuelles exactes** :
  - Page 32 : *« OWL sert l’inférence sous hypothèse de monde ouvert — déduire des faits implicites ; SHACL sert la validation sous hypothèse de monde clos — constater qu’un fait requis manque... »*
  - Page 34 : *« La gouvernance du sens en environnement distribué impose donc de traiter la sortie du modèle comme une proposition soumise à validation — par SHACL (§ 2.3.3), par revue experte, par confrontation aux axiomes ontologiques — et non comme un contrat établi. »*
- **Diagnostic causal approfondi** :
  Le compendium recommande d'adosser l'interopérabilité sémantique des agents à OWL 2 et SHACL, mais ignore une incompatibilité logique fondamentale :
  1. *Monotonicité stricte d'OWL 2 DL* : Dans OWL 2 DL (fondé sur la logique de description $\mathcal{SROIQ}(\mathcal{D})$), le raisonnement déductif est strictement monotone : l'adjonction d'un nouvel axiome ne peut en aucun cas invalider une conclusion précédemment démontrée.
  2. *Nature non-monotone de la délibération agentique* : Un agent autonome opérant dans un environnement dynamique procède par hypothèses révisables et raisonnement par défaut (Reiter, 1980 ; AGM Belief Revision, 1985). Si un agent insère dans le triplestore OWL un fait provisoire $\alpha$, puis découvre par retour d'outil que $\neg \alpha$ est vrai, la base de connaissances devient logiquement inconsistante ($\mathcal{K} \models \bot$). En logique classique, une base inconsistante engendre une explosion déductive (*ex falso quodlibet* ou principe de pseudo-scotus), permettant de déduire n'importe quelle proposition fausse et paralysant tous les raisonneurs sémantiques.
- **Correctif formel** :
  Restreindre strictement l'usage d'OWL 2 DL aux vocabulaires terminologiques invariants (TBox stables). Interdire l'écriture directe d'assertions conjoncturelles d'agents dans l'ABox OWL sans passer par une couche de réconciliation fondée sur des logiques non-monotones (Answer Set Programming - ASP ou Datalog avec négation stratifiée).

---

### 11. **[Major]** Absence de valeur probatoire et de non-répudiation des traces OpenTelemetry et W3C Trace Context pour l'auditabilité financière

- **Localisation exacte** : Chapitre 3, § 3.4.5 et § 3.4.6 (pp. 44-45).
- **Citation textuelle exacte** :
  - Page 45 : *« L’observabilité ne sert pas que le diagnostic : elle fonde l’auditabilité, c’est-à-dire la capacité à démontrer après coup, preuves à l’appui, comment une intégration s’est comportée... Dans la banque ouverte... l’auditabilité des appels y est une condition de conformité, non un agrément. »*
- **Diagnostic causal approfondi** :
  Le texte affirme que la pile OpenTelemetry (spans distribués et W3C Trace Context) constitue le socle de l'auditabilité réglementaire. Il s'agit d'une confusion critique entre télémétrie opérationnelle et preuve juridique :
  - Les spans OpenTelemetry sont conçus pour la surveillance des performances (APM) et le débogage. Ils transitent sur le réseau via des protocoles sans signature cryptographique (OTLP sur gRPC/HTTP) et sont stockés dans des bases de données de séries temporelles (ex. Jaeger, Tempo, Elasticsearch) modifiables par les administrateurs système.
  - En droit bancaire et financier (notamment sous les lignes directrices BSIF E-23, Sarbanes-Oxley § 404 et l'article 12.1 de la Loi 25 québécoise), une trace d'audit requiert des garanties formelles de **non-répudiation, d'intégrité temporelle et d'immutabilité**. Une trace OpenTelemetry brute n'a aucune valeur probatoire devant une autorité de contrôle ou un tribunal, car elle peut être altérée ou purgée a posteriori sans rupture d'intégrité cryptographique.
- **Correctif formel** :
  Établir une distinction étanche entre *télémétrie opérationnelle non opposable* (OTel) et *journalisation d'audit probatoire opposable*. Exiger que chaque transition d'état et appel d'outil contractuel émette un enregistrement scellé :
  $$\text{AuditEntry} = \text{Sign}_{K_{\text{Agent}}}(\text{TraceID} \parallel \text{Timestamp} \parallel \text{ContextHash} \parallel \text{Decision} \parallel \text{ToolArguments})$$
  consigné dans un registre immuable à arbre de Merkle (*Append-Only Log* auditable certifié RFC 6962 / RFC 9162).

---

### 12. **[Major]** Omission des topologies d'essaim et de marché, et redondances textuelles verbatim entre tableaux et figures

- **Localisation exacte** : Chapitre 6, § 6.1.2 (pp. 71-72), Tableau 6.1 et Figure 6.1 ; Chapitre 5, § 5.0 (pp. 61-62), Tableau 5.1 et Figure 5.0 ; Chapitre 6, § 6.4.2 (p. 76), Tableau 6.2 et Figure 6.4.
- **Citations textuelles exactes** :
  - Tableau 6.1 (p. 71) et Figure 6.1 (p. 72) : Liste strictement identique : Étoile (*« Un orchestrateur délègue à des travailleurs »*), Chaîne (*« La sortie d'un agent est l'entrée du suivant »*), Arbre (*« Délégation hiérarchique »*), Graphe (*« Interactions arbitraires »*).
  - Tableau 6.2 (p. 76) et Figure 6.4 (p. 76) : Reproduction verbatim des mêmes définitions de $pass@k$ et $pass^k$ sur la même page.
- **Diagnostic causal approfondi** :
  1. *Omission des topologies d'essaim et de marché* : Le plan d'audit du socle (Review Plan S07, p. 110) et la table des matières du Chapitre 6 annoncent l'étude des topologies de **marché** et d'**essaim**. Or, dans le corps du texte (pp. 71-72), la taxonomie se restreint arbitrairement à quatre structures statiques de graphes (Étoile, Chaîne, Arbre, Graphe). Les architectures de coordination par **stigmergie / essaim** (où les agents interagissent indirectement par modification d'un environnement partagé ou d'un *blackboard*) et les architectures de **marché** (enchères de Vickrey, allocation par prix d'équilibre, dérivées du Contract Net Protocol) sont complètement ignorées.
  2. *Duplications verbatim systématiques* :
     - Le Tableau 6.1 et la Figure 6.1 répètent mot pour mot les quatre mêmes définitions sans qu'aucun diagramme visuel d'architecture ne vienne justifier la présence de la figure.
     - Un doublon identique apparaît entre le Tableau 5.1 (p. 61) et la Figure 5.0 (p. 62) sur le triptyque Mémoire / RAG / Protocole.
     - Au § 6.4.2 (p. 76), le Tableau 6.2 et la Figure 6.4 coexistent sur la même page en répétant verbatim les mêmes définitions. Cette pratique gonfle artificiellement le volume du manuscrit tout en appauvrissant l'analyse technique.
- **Correctif formel** :
  Compléter la typologie des coordinations par l'ajout formel de l'Essaim (*Swarm* / coordination stigmergique sur espace de tuples) et du Marché (*Market-based dynamic bidding*). Remplacer les figures textuelles redondantes par de véritables schémas conceptuels de flux d'information.

---

### 13. **[Major]** Sous-spécification des canaux d'exfiltration pour CodeAct et des attaques adversariales multimodales pour Computer Use

- **Localisation exacte** : Chapitre 4, § 4.2.3 (p. 53), § 4.4.3 (pp. 59-60).
- **Citations textuelles exactes** :
  - Page 53 : *« L’action comme code exécutable — CodeAct... exécuter du code généré par un modèle exige un environnement confiné, faute de quoi l’agent dispose d’une capacité d’action quasi illimitée sur le système hôte. »*
  - Page 59 : *« L’exécution de code est l’outil universel le plus puissant... Le confinement est ici une mesure de sécurité non négociable... »*
  - Page 60 : *« Le pilotage d’interface... Le choix entre structure et vision est ainsi autant une décision de surface d’attaque qu’une décision de robustesse... »*
- **Diagnostic causal approfondi** :
  L'auteur prescrit le « confinement » sans caractériser la surface d'attaque spécifique aux LLMs :
  1. *Canaux cachés et exfiltration sous CodeAct* : Un code Python généré dans un bac à sable conteneurisé standard sans privilèges root conserve l'accès aux appels réseau si la tâche requiert des requêtes externes. Un modèle subverti peut exfiltrer des variables d'environnement, des clés d'API ou des données de contexte par requêtes DNS asynchrones, par stéganographie dans les en-têtes HTTP ou via des canaux auxiliaires temporels (*timing attacks*).
  2. *Vulnérabilités adversariales multimodales dans Computer Use* : Dans le pilotage par vision (captures d'écran), l'agent est vulnérable aux attaques par injection visuelle indirecte (*adversarial visual patches*, typoglyphie invisible à faible opacité ou perturbations imperceptibles de pixels). Une image affichée à l'écran peut forcer le modèle de vision à cliquer sur des coordonnées hostiles ou à interpréter des instructions malveillantes dissimulées dans l'arrière-plan graphique. Traiter la vision comme un simple compromis de coût par rapport au DOM est une sous-estimation substantielle du vecteur d'attaque multimodal.
- **Correctif formel** :
  - Pour CodeAct : imposer une isolation par MicroVM (type Firecracker ou gVisor) avec interdiction stricte de sortie réseau directe (*Air-Gapped Sandbox*), tout appel externe devant obligatoirement transiter par un proxy mandataire d'inspection L7 à schéma validé.
  - Pour Computer Use : prescrire un assainisseur visuel (*Visual Pre-Processing Defense*) et la validation croisée déterministe de l'arbre d'accessibilité DOM avant toute exécution d'action périphérique (clic ou saisie clavier).

---

# Minor Corrections and Typos

1. **Chapitre 2, p. 32 (§ 2.3.3)** : Collision matérielle et inversion de paragraphe lors de la mise en page :
   - *Texte actuel* : « Ces travaux ne sont pas cités comme acquis : leur ancre de version se fixe au moment de citer, et cette réserve est reconduite ici sans être levée. intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. Un graphe RDF est, par construction, ouvert et sans schéma : tout triplet est licite, l’absence d’information n’est pas une faute, et rien n’interdit a priori d’attribuer une date de naissance à une facture. Pour l’intégration, cette permissivité est SHACL remplit ce rôle... »
   - *Correction* : La proposition « intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. » a été accidentellement coupée de la fin du second paragraphe et collée à la fin du premier. Rétablir la syntaxe exacte :
     « ...et cette réserve est reconduite ici sans être levée. »
     « Un graphe RDF est, par construction, ouvert et sans schéma... Pour l’intégration, cette permissivité est **intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API.** »
     « **SHACL** remplit ce rôle... »

2. **Chapitre 7, p. 79 (§ 7.0)** : Collision éditoriale entre l'encadré Thèse et le corps du texte :
   - *Texte actuel* : Dans l'encadré Thèse : « ...fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres. » et dans le second paragraphe : « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses [saut de paragraphe] La proposition directrice tient en un déplacement... »
   - *Correction* : Supprimer le fragment intrus dans l'encadré Thèse après « instruit au ch. 10. » et le rétablir dans le second paragraphe : « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses **outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.** »

3. **Chapitre 1, p. 11 (§ 1.1.4.1)** : Ponctuation manquante en fin de phrase :
   - *Texte actuel* : « ...quel que soit le soin apporté aux deux premiers Le point est repris au ch. 7... »
   - *Correction* : Insérer le point final manquant : « ...aux deux premiers**.** Le point est repris au ch. 7... »

4. **Chapitre 6, p. 75 (§ 6.3.3)** : Ponctuation manquante et fusion de titre dans le corps de texte :
   - *Texte actuel* : « ...sans encore le rejoindre Des annonces d’éditeurs revendiquent depuis... Raisonnement général, outils et tâches d’entreprise. Une seconde famille évalue... »
   - *Correction* : Insérer un point après « rejoindre. » et formater « Raisonnement général, outils et tâches d’entreprise » en titre de sous-section distinct du paragraphe.

5. **Chapitre 2, p. 25 (§ 2.1.1)** : Troncation du numéro de page en bas de page dans le flux textuel :
   - *Texte actuel* : « Gel au 27 juillet 2026 · actualisation du 1er novembre 2026 Page 25 s »
   - *Correction* : Rétablir « Page 25 sur 663 ».

6. **Chapitre 2, p. 27 (Tableau 2.1)** : Classification de la compatibilité de schéma :
   - *Texte actuel* : Classement de « Transitive » comme 4e modalité disjointe au même rang que Backward, Forward, Full.
   - *Correction* : Clarifier que la transitivité est un modificateur d'orthogonalité temporelle (Pairwise vs Transitive) applicable à chacun des trois régimes, et non une modalité disjointe.

7. **Liminaires & Ch. 1, Ch. 6 (pp. 1, 10-11, 72, 76)** : Incohérence interne de la doctrine de gel documentaire :
   - *Observation* : L'ouvrage stipule solennellement que les faits doctrinaux sont gelés au 27 juillet 2026 et que seules les annexes intègrent les actualisations postérieures. Or, le corps du texte intègre directement des actualisations datées du 28 juillet, 30 juillet et 23 octobre 2026 (pp. 11, 72, 76).
   - *Correction* : Basculer ces actualisations en notes de bas de page renvoyant à l'Annexe N ou modifier la mention liminaire pour acter que le Livre I a été révisé jusqu'au 24 octobre 2026.

8. **Ensemble des chapitres 1 à 6** : Numérotation discontinue et non standardisée des figures :
   - *Observation* : Les figures sont indicées d'après la sous-section hôte (Fig. 1.0, 1.1, 1.3, 1.5 ; Fig. 2.1, 2.3 ; Fig. 5.0, 5.3 ; Fig. 6.1, 6.4) plutôt que séquentiellement dans le chapitre, créant une fausse impression de figures manquantes (ex. absence apparente de Fig. 1.2, Fig. 1.4, Fig. 6.2, Fig. 6.3).
   - *Correction* : Adopter la numérotation séquentielle standard (Figure 1.1, Figure 1.2, Figure 1.3, etc.).
