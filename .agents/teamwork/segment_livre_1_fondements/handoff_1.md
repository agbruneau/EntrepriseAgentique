**Segment scope**: Livre I — Fondements de l’interopérabilité et ingénierie des systèmes agentiques (pp. 1-79, Liminaires et Chapitres 1 à 6, segments S01 à S07 de REVIEW_PLAN.md).

# Potential Mistakes and Improvements

### 1. **[Critical]** Falsification du modèle de coût d'intégration quadratique $N(N-1)/2$ vs linéarité $2N$, et allégation erronée sur l'impact d'ajout d'un système en intégration point-à-point
- **Localisation exacte** : Chapitre 1, pp. 5-6 (§ 1.0.1) et p. 22 (§ 1.6.1).
- **Citations textuelles exactes** :
  - Page 5 : *« raccorder N systèmes susceptibles de dialoguer deux à deux peut requérir jusqu’à N(N−1)/2 liaisons, chacune avec sa logique de transport, de format et de correspondance. »*
  - Page 6 : *« ramènent la complexité de N×N à un ordre linéaire (voir § 1.6.1) »*
  - Page 22 : *« Lorsque N applications doivent s’échanger des données, le couplage par traductions directes croît en N×N : chaque paire exige son propre traducteur, et l’ajout d’un système impose de modifier tous les autres. Le modèle de données canonique brise cette explosion combinatoire en introduisant un format pivot indépendant des applications : chaque système ne traduit qu’entre son format propre et le canonique, ramenant le coût d’intégration à un ordre linéaire, en 2N. »*
- **Diagnostic causal approfondi** :
  Ce passage cumule trois erreurs formelles, topologiques et méthodologiques :
  1. *Confusion formelle d'orientation et d'ordre de grandeur* : Le texte oscille sans rigueur entre $N(N-1)/2$ (arêtes d'un graphe complet non orienté $K_N$), $N \times N$ (matrice d'adjacence avec boucles réflexives, ou $N^2$), et $N(N-1)$ (arêtes d'un graphe complet orienté). En intégration logicielle, les transformations de schémas sont asymétriques ($A \to B$ ne résout pas $B \to A$). Dans le pire cas d'un maillage bilatéral exhaustif asymétrique, le nombre de traducteurs est strictement $N(N-1) = N^2 - N$, et non $N(N-1)/2$.
  2. *Affirmation factuellement et mathématiquement fausse quant à l'ajout d'un système* : Le texte affirme péremptoirement que *« l'ajout d'un système impose de modifier tous les autres »*. C'est rigoureusement inexact en intégration point-à-point classique. L'adjonction d'un $(N+1)$-ième système nécessite d'établir au plus $N$ nouvelles liaisons bilatérales (soit $2N$ traducteurs orientés) le reliant aux nœuds existants. Les $\frac{N(N-1)}{2}$ liaisons préexistantes entre les $N$ premiers systèmes ne sont nullement modifiées ni réécrites, en vertu du découplage strict des interfaces pair-à-pair.
  3. *Fausse linéarité du modèle de données canonique (CDM) $2N$ sous évolution* : L'affirmation selon laquelle le format pivot ramène la complexité à $O(N)$ (en $2N$) repose sur le postulat implicite et intenable d'un schéma canonique $\mathcal{C}$ universel, complet et immuable. Dès que les schémas sources évoluent ou expriment des besoins non couverts par $\mathcal{C}$, le schéma canonique doit être étendu ($\mathcal{C} \to \mathcal{C}'$). Or, toute mutation de $\mathcal{C}$ invalide ou force l'audit et l'adaptation des $2N$ adaptateurs existants. En théorie de l'intégration (Halevy, 2001 ; Bernstein, 2003), le coût de gouvernance sémantique d'un modèle pivot face à des besoins distribués croît de manière combinatoire en fonction des comités d'arbitrage organisationnels ($O(N^2)$ interactions humaines).
  4. *Inadéquation pour l'intégration agentique* : Les agents n'adoptent ni le maillage $O(N^2)$ d'adaptateurs statiques, ni le goulot d'étranglement $2N$ d'un CDM rigide. Chaque agent expose son schéma d'outil en $O(1)$ (via MCP ou A2A). La médiation est reportée à l'exécution dans le contexte du LLM (in-context dynamic schema grounding). Le coût d'intégration n'est plus un coût de développement logiciel linéaire ou quadratique, mais un coût opérationnel récurrent stochastique par inférence (tokens, latence, dérive de prompt) et un risque de divergence d'état.
- **Correctif formel et contre-exemple explicite** :
  Remplacer le modèle informel par une formalisation explicite en théorie des graphes :
  Soit un réseau d'intégration modélisé par un graphe orienté $G = (V, E)$ où $|V| = N$. Le nombre d'adaptateurs point-à-point requis est $|E| = \sum_{i=1}^N \deg^+(v_i)$. Dans les architectures réelles d'entreprise, $G$ n'est jamais un graphe complet $K_N$, mais un graphe sans échelle (scale-free network, Barabási-Albert) ou hiérarchique où le degré moyen $\langle k \rangle \ll N$, conférant déjà au point-à-point un coût effectif de $O(N)$.
  Lors de l'introduction d'un nouveau nœud $v_{N+1}$, le delta d'arêtes est $\Delta |E| = \deg^+(v_{N+1}) + \deg^-(v_{N+1}) \le 2N$, avec une invariance stricte des arêtes existantes : $\forall (u, w) \in E, \Delta E_{(u,w)} = 0$.
  Pour le modèle canonique, modéliser le coût de cycle de vie en intégrant la probabilité de révision du schéma pivot :
  $$\mathbb{E}[\text{Coût}_{\text{CDM}}] = 2N \cdot c_{\text{adapt}} + \sum_{t=1}^T P(\Delta \mathcal{C}_t \neq \emptyset) \cdot [2N \cdot c_{\text{reval}} + c_{\text{gouv}}(N^2)]$$
  où $c_{\text{gouv}}(N^2)$ capture l'explosion combinatoire du consensus sémantique inter-équipes.

---

### 2. **[Critical]** Falsification de la métrique d'évaluation $\text{pass}^k$ de $\tau$-bench et confusion mathématique avec l'effondrement intra-trajectoire $q^T$
- **Localisation exacte** : Chapitre 6, p. 76 (§ 6.4.2), Tableau 6.2 et Figure 6.4 (p. 76).
- **Citations textuelles exactes** :
  - Tableau 6.2 : *« pass^k ... la probabilité que les k tentatives réussissent toutes — la consistance. Chute brutalement dès que la fiabilité par étape s’éloigne de la perfection. »*
  - Page 76 : *« La seconde — pass^k, introduite par τ-bench (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues et multi-étapes. Cette dégradation — où une probabilité d’échec par pas même faible se compose géométriquement sur une longue trajectoire — est l’un des constats les plus robustes du domaine, et l’une des questions que le ch. 49 laisse ouvertes. »*
  - Figure 6.4 : *« pass^k — LA CONSISTANCE ... Les k tentatives réussissent toutes ... chute brutale dès que la fiabilité par étape s'éloigne de la perfection ... s'effondre avec k ... Une probabilité d’échec par pas même faible SE COMPOSE GÉOMÉTRIQUEMENT sur une longue trajectoire : c’est l’un des constats les plus robustes du domaine, et la raison pour laquelle un agent se caractérise par sa courbe de consistance... »*
- **Diagnostic causal approfondi** :
  Ce passage introduit un contresens mathématique et méthodologique majeur en confondant deux phénomènes stochastiques complètement orthogonaux :
  1. *La définition formelle de $\text{pass}^k$ dans $\tau$-bench (Yao et coll., 2024)* : Dans $\tau$-bench, $k$ représente le nombre de **réplications indépendantes (trials / runs)** de la *totalité d'une tâche*. Si un agent a une probabilité $p \in [0, 1]$ de réussir une tâche de bout en bout, la métrique de consistance $\text{pass}^k$ mesure l'espérance que l'agent réussisse $k$ exécutions complètes indépendantes : $\text{pass}^k = \mathbb{E}[p^k]$. L'exposant $k$ est le nombre d'essais répétés, PAS la longueur de la conversation ni le nombre d'étapes !
  2. *La décomposition intra-trajectoire multi-étapes* : Si une tâche comporte un horizon de $T$ étapes séquentielles, et si l'agent a une probabilité de succès par étape $q_t = P(\text{étape}_t \text{ valide} \mid \text{historique})$, le taux de succès global de la tâche sur un seul run est $p = \prod_{t=1}^T q_t$. Si $q_t \equiv q < 1$, alors $p = q^T$. Ici, l'exposant $T$ est la *profondeur temporelle de la trajectoire*.
  L'auteur attribue textuellement l'effondrement de $\text{pass}^k$ à la composition d'une probabilité d'échec par pas sur une longue trajectoire ! C'est un contresens probabiliste élémentaire :
  - Un agent testé sur une tâche élémentaire en 1 seule étape ($T=1$) avec un taux de succès $p = 0.8$ verra son $\text{pass}^8 = (0.8)^8 \approx 0.168$ s'effondrer à 16.8 %, alors qu'il n'y a AUCUNE longue trajectoire ni composition multi-étapes !
  - Réciproquement, un agent opérant sur une trajectoire longue de $T = 50$ étapes peut avoir une consistance inter-essais mesurée à $k=1, 2, \dots$, sans que $k$ n'ait le moindre rapport avec $T$.
  Lier la métrique $\text{pass}^k$ de $\tau$-bench à la composition géométrique des défaillances le long d'une trajectoire est une erreur formelle de modélisation.
- **Correctif formel explicite** :
  Dissocier rigoureusement les deux variables stochastiques dans le texte et le Tableau 6.2 :
  1. *Fiabilité intra-trajectoire (horizon temporel $T$)* : Pour une trajectoire de longueur $T$, le taux de succès au run $j$ est :
     $$P(S_j) = \prod_{t=1}^T P(a_t \in \mathcal{A}^* \mid s_t) = \prod_{t=1}^T q_t \le (\bar{q})^T$$
     qui tend vers 0 lorsque $T \to \infty$ dès que $\bar{q} < 1$.
  2. *Consistance inter-essais ($\text{pass}^k$ de $\tau$-bench)* : Pour $k$ réplications indépendantes d'une tâche dont le taux de succès global est $p = P(S)$, la métrique de consistance est :
     $$\text{pass}^k = \mathbb{E}_{j=1 \dots k}\left[ \prod_{j=1}^k \mathbb{I}(S_j) \right] = p^k$$
  La composition complète pour $k$ essais sur une tâche à $T$ pas s'écrit $\text{pass}^k(T) = \left( \prod_{t=1}^T q_t \right)^k$. Rectifier le Tableau 6.2 et la Figure 6.4 en remplaçant « fiabilité par étape » par « taux de succès global par essai complet ».

---

### 3. **[Critical]** Brèche fondamentale dans le modèle AAA / Zero Trust face au confused deputy sémantique et à l'injection indirecte
- **Localisation exacte** : Chapitre 3, pp. 36-37 (§ 3.1.1) et pp. 40-41 (§ 3.3.1).
- **Citations textuelles exactes** :
  - Page 36 : *« Le mandataire confus (confused deputy)... une passerelle qui réutilise ses propres droits au lieu de propager ceux du client transforme tout point d’entrée en vecteur d’escalade. C’est le défaut le plus important de cette sous-section pour la suite du Livre : il connaît une variante moderne dans les architectures agentiques, où une injection d’invite indirecte détourne le plan d’un agent en lui faisant traiter comme instructions des contenus externes. »*
  - Page 40 : *« Le zero-trust formalise le principe ne jamais faire confiance, toujours vérifier... point de décision et point d’application de politique, évaluation continue par requête... L’application du zero-trust aux services exige une identité pour les acteurs non humains, à durée de vie courte et vérifiable. SPIFFE et son implémentation de référence SPIRE fournissent à chaque charge un identifiant et un document d’identité vérifiable... »*
- **Diagnostic causal approfondi** :
  Le chapitre érige l'architecture Zero Trust (NIST SP 800-207) et les identités de charge de travail (SPIFFE/SPIRE, mTLS, FAPI 2.0) en fondements transposables à l'entreprise agentique. Or, il existe une rupture systémique non résolue :
  1. *Inopérance du PEP/PDP réseau face au détournement sémantique* : Le point d'application de politique (PEP) classique valide les requêtes à partir de métadonnées d'enveloppe : adresse IP, jeton cryptographique JWT/SVID, méthode HTTP, ressource ciblée. Lorsqu'un agent autonome est subverti par injection indirecte (e.g. prompt malveillant dissimulé dans un PDF ingéré par RAG ou un ticket de support), l'appel d'outil émis par l'agent (`transfererFonds(destinataire, montant)`) est émis par le conteneur légitime de l'agent, avec son identité SPIFFE valide et ses droits IAM accordés. Le PEP valide la requête sans aucune alerte !
  2. *Rupture de l'authentification d'intention (Intent Authenticity Collapse)* : Le modèle AAA hérité (Authentication, Authorization, Accounting) est fondé sur le postulat que l'authenticité de l'émetteur implique l'authenticité de l'intention. Chez un agent fondé sur un LLM, cette équivalence est fausse : un émetteur authentique peut formuler une intention hostile dictée par des données non fiables.
  3. *Absence de modèle formel de contrôle des flux d'information (IFC)* : Présenter SPIFFE/SPIRE et le Zero Trust comme le socle de sécurité sans y intégrer formellement un modèle de traçage de teinte (Taint Tracking) au niveau des données du LLM masque le fait que la couche d'infrastructure est structurellement aveugle aux attaques de couche sémantique.
- **Correctif formel et contre-exemple explicite** :
  Formaliser l'inadéquation du triplet de contrôle d'accès traditionnel $\mathcal{AC} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O} \rangle$ (Sujet, Action, Objet).
  Introduire le modèle étendu de contrôle de flux d'information (Information Flow Control, Myers & Liskov, 1997 ; Denning, 1976) :
  $$\mathcal{AC}_{\text{agent}} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O}, \mathcal{L}_{\text{input}}, \mathcal{L}_{\text{output}} \rangle$$
  où $\mathcal{L}_{\text{input}}$ représente le niveau de classification de sécurité de toutes les données absorbées dans la fenêtre de contexte de l'agent. Énoncer l'invariant de non-interférence sémantique (Goguen & Meseguer, 1982) :
  $$\forall d \in \text{Context}(\text{Agent}), \quad \text{Tainted}(d) \implies \text{Capabilities}(\text{Agent}) \cap \text{SideEffectTools} = \emptyset$$
  Tout agent ayant ingéré des données non fiables doit voir ses privilèges d'effets de bord révoqués dynamiquement au point d'application, indépendamment de son identité SPIFFE.

---

### 4. **[Critical]** Faux parallélisme d'extensibilité GAV vs LAV en intégration sémantique et omission de l'indécidabilité de réécriture pour les flux d'agents
- **Localisation exacte** : Chapitre 2, pp. 32-33 (§ 2.3.4).
- **Citations textuelles exactes** :
  - Page 33 : *« Le formalisme distingue ici deux régimes de correspondance, et le choix entre eux est structurant :
  • GAV (Global-As-View) — chaque concept global est défini comme une vue sur les sources. Réécriture de requête simple ; ajout de source coûteux, puisqu’il faut revoir les définitions globales.
  • LAV (Local-As-View) — chaque source est décrite comme une vue sur le schéma global. Extensibilité supérieure — ajouter une source n’affecte pas les autres — au prix d’une réécriture de requête plus complexe.
  Ce choix rejoue, au niveau du sens, l’arbitrage entre couplage et évolutivité qui structure tout le Livre : GAV optimise le présent, LAV optimise l’arrivée du prochain participant. »*
- **Diagnostic causal approfondi** :
  1. *Omission de la complexité algorithmique intrinsèque de LAV* : Qualifier la réécriture de requête en LAV de simplement « plus complexe » est un euphémisme qui masque des résultats d'impossibilité algorithmique. Dans le formalisme LAV (Answering Queries Using Views, Halevy, 2001 ; Lenzerini, 2002), trouver la réécriture maximale contenue (maximally contained rewriting) pour des requêtes conjonctives est un problème NP-complet en taille de la requête, et devient exponentiel voire indécidable en présence de contraintes d'intégrité référentielle, d'ontologies expressives (TBox OWL) ou de dépendances fonctionnelles.
  2. *Inadéquation cognitive des LLMs face à LAV* : Le compendium soutient que les protocoles agentiques négocient des schémas dynamiques. Or, si les agents opèrent dans une architecture LAV, la traduction des requêtes impose des algorithmes formels de résolution symbolique (Bucket algorithm, MiniCon de Pottinger & Halevy 2001, ou Inverse Rules). Un agent LLM est fondamentalement incapable de garantir mathématiquement la correction et la complétude d'une réécriture LAV sans un moteur Datalog déterministe sous-jacent.
  3. *Omission de GLAV (Global-and-Local-As-View)* : La pratique industrielle de l'intégration sémantique a abandonné la dichotomie stricte GAV/LAV au profit de GLAV / tuple-generating dependencies (tgds) (Fagin et coll., 2005), seul formalisme capable d'associer des vues sur les sources à des vues sur le schéma global ($\phi_{\mathcal{S}}(\mathbf{x}) \to \exists \mathbf{y} \psi_{\mathcal{G}}(\mathbf{x}, \mathbf{y})$), indispensable pour l'hétérogénéité des schémas d'agents.
- **Correctif formel et contre-exemple mathématique** :
  Illustrer l'effondrement de la réécriture naïve par un contre-exemple explicite :
  Soit une ontologie globale $\mathcal{G}$ avec les prédicats $\text{Agent}(x)$, $\text{Mandat}(x, y)$, $\text{Institution}(y)$.
  En LAV, soit deux sources d'agents $V_1, V_2$ définies par :
  $$V_1(x) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$$
  $$V_2(y) \leftarrow \text{Institution}(y)$$
  Pour une requête globale $Q(x, y) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$, aucune réécriture exacte équivalente n'existe à partir de $V_1$ et $V_2$ car la variable $y$ est projetée hors de $V_1$. Seule une réécriture contenue non équivalente est calculable. Expliciter que le déploiement d'agents dans une architecture sémantique exige une couche formelle de médiation GLAV à base de règles logiques matérielles, interdisant de confier la réécriture de requêtes aux capacités d'inférence floues des modèles génératifs.

---

### 5. **[Critical]** Amplification stochastique dans la boucle ReAct, divergence cumulative et illusion de terminaison par budget
- **Localisation exacte** : Chapitre 4, pp. 51-53 (§ 4.2.1, § 4.2.3, Figure 4.2).
- **Citations textuelles exactes** :
  - Page 52 : *« L’entrelacement raisonnement-action — ReAct... à chaque pas, une étape de raisonnement verbalisé et une action dont le résultat est réinjecté avant le pas suivant... Chaque tour consomme des jetons en proportion du contexte accumulé... Sur les trajectoires longues, ce patron dérive — accumulation d’erreurs non corrigées, boucles répétitives, perte du but initial à mesure que le contexte se dilue. »*
  - Page 52 (Mise en œuvre) : *« Le critère d’arrêt n’est pas un détail mais une garantie de terminaison. Une boucle sans budget d’appels explicite ni détection de stagnation peut diverger... Fixer dès la conception un budget de pas, un plafond de jetons et une condition d’échec contrôlé relève du contrat opérationnel de l’agent... »*
- **Diagnostic causal approfondi** :
  1. *L'illusion de la terminaison par budget de pas* : Affirmer qu'un plafond de jetons ou un budget de pas constitue une « garantie de terminaison » confond l'arrêt d'urgence (*timeout abort*) et la terminaison correcte (*well-founded termination / total correctness*). Lorsque le budget d'appels $K$ est atteint, la tâche n'est pas résolue : elle est interrompue arbitrairement dans un état intermédiaire potentiellement instable, laissant des effets de bord partiels non annulés dans les systèmes cibles (ex. fichier partiellement écrit, réservation non confirmée).
  2. *Modélisation mathématique de l'amplification d'erreur en boucle fermée* :
     Dans ReAct, l'inférence au pas $t$ est conditionnée par toute la trajectoire précédente :
     $$P(a_t, r_t \mid s_0, r_1, a_1, o_1, \dots, r_{t-1}, a_{t-1}, o_{t-1})$$
     Dès lors qu'une hallucination ou une observation erronée pénètre l'historique au temps $\tau < t$, cette erreur fait désormais partie du contexte conditionnant d'auto-attention. Contrairement à un filtre de Kalman ou à un estimateur bayésien qui révisent leur distribution de croyance par rapport à un modèle physique, l'attention du LLM souffre d'un biais d'auto-confirmation (context pollution). Le taux d'erreur au pas $t$ n'est pas une constante $\epsilon$, mais une fonction croissante de la trajectoire : $\epsilon_t = g(t, \text{erreurs passées})$ avec $\lim_{t \to \infty} \epsilon_t = 1$.
  3. *L'impossibilité de détection de stagnation par le modèle lui-même* : Le compendium suggère la « détection de stagnation », mais si cette détection est confiée au modèle (comme dans Self-Refine ou ReAct), l'agent demeure piégé dans sa chambre d'écho cognitive.
- **Correctif formel et modélisation explicite** :
  Établir formellement que la boucle ReAct est un processus non-markovien non stationnaire à accumulation d'entropie d'attention. Remplacer la préconisation du budget de pas passif par un automate de surveillance externe déterministe (Safety Supervisor Automaton) :
  Soit $S$ l'état des systèmes externes. Chaque action $a_t$ émise par l'agent doit être interceptée par un automate d'états finis $\mathcal{M} = \langle Q, \Sigma, \delta, q_0, F \rangle$ qui valide les préconditions avant exécution. Si le budget $K$ est atteint sans atteindre $F$, l'automate déclenche immédiatement un protocole de compensation déterministe (pattern Saga / Rollback compensatoire) pour rétablir $S$ à son état invariant $S_0$.

---

### 6. **[Critical]** Irréversibilité informationnelle de la compaction mémorielle et boucle de rétroaction positive des hallucinations persistantes
- **Localisation exacte** : Chapitre 5, pp. 63-66 (§ 5.1.2, § 5.1.3, § 5.2.1, § 5.2.2).
- **Citations textuelles exactes** :
  - Page 64 : *« L’enjeu de conception est la réversibilité. Une compaction agressive risque d’effacer un détail qui redeviendra pertinent ; une compaction trop prudente ne libère pas assez de budget. La bonne pratique consiste à compacter en conservant un pointeur vers la trace intégrale, déportée dans un magasin persistant, de sorte que le résumé reste augmentable à la demande sans peser sur la fenêtre courante. »*
  - Page 66 : *« Une mémoire mal gérée devient une source d’hallucinations : un agent qui rappelle un fait erroné avec aplomb propage l’erreur sur toute la trajectoire... la différence avec une hallucination ordinaire tiendrait à ce que l’hallucination mémorielle est persistante et auto-confirmante, l’agent relisant le souvenir erroné à la session suivante. »*
- **Diagnostic causal approfondi** :
  1. *L'impossibilité de la réversibilité par pointeurs (paradoxe épistémique de l'agent)* : Le compendium affirme qu'un résumé reste « augmentable à la demande » grâce à un pointeur vers la trace brute. Or, du point de vue de la décision séquentielle, l'agent décide d'aller chercher la trace brute uniquement en se fondant sur les informations résidant *dans son contexte actif*. Si le résumé compacté a omis un détail critique $D$, l'agent n'a plus conscience de l'existence de $D$. Il ne dispose d'aucun signal pour déclencher la résolution du pointeur vers la mémoire brute. En théorie de l'information (théorème de perte d'information de Shannon), la compression sémantique opérée par un LLM est une fonction non injective irréversible :
     $$I(X; S) < H(X)$$
     Prétendre que cette compaction est réversible par simple conservation de pointeurs est une illusion d'ingénierie.
  2. *Dynamique de divergence de l'hallucination mémorielle (Epistemic Drift)* : Dans les architectures de mémoire long terme (Mem0, Letta, Zep), le processus d'écriture repose sur l'extraction de faits par un LLM. Si un fait erroné $\hat{F}$ est consigné dans la base vectorielle, lors des interactions futures, $\hat{F}$ est extrait avec un score de similarité cosinus élevé et injecté dans le system prompt comme « contexte attesté ». Le modèle conditionne alors ses nouveaux raisonnements sur $\hat{F}$, générant de nouveaux faits dérivés $\hat{G}_1, \hat{G}_2$ qui sont à leur tour stockés en mémoire. Il s'agit d'une instabilité en boucle fermée conduisant à une divergence épistémique incurable sans audit externe.
- **Correctif formel et démonstration mathématique** :
  Modéliser la compaction mémorielle comme un canal avec bruit à distorsion de débit $R(D)$. Imposer un système de maintien de la vérité (Truth Maintenance System - TMS, de Kleer, 1986 / Doyle, 1979) :
  Chaque fait $F_i$ mémorisé doit être assorti de son justification graph $J(F_i) = \langle \text{Sources}, \text{Inférences}, \text{Timestamp}, \text{Validité} \rangle$.
  Toute rétraction ou invalidation d'une source primaire $S_k$ doit déclencher une propagation d'invalidation automatique sur l'arbre de dérivation :
  $$\text{Si } S_k \to \bot, \quad \forall F \text{ tel que } S_k \in J(F), \quad F \gets \text{Invalide}$$
  interdisant la ré-ingestion de faits orphelins dans les fenêtres d'inférence futures.

---

### 7. **[Major]** Falsification du diagnostic d'échec de FIPA-ACL et omission des protocoles d'engagements sociaux décidables
- **Localisation exacte** : Chapitre 4, p. 49 (§ 4.1.3), Chapitre 6, pp. 72-73 (§ 6.2 et § 6.2.1).
- **Citations textuelles exactes** :
  - Page 73 : *« Communiquer suppose trois accords, et les protocoles agentiques n’en portent qu’un... (c) Un accord sur la force illocutoire — ce que l’émetteur fait en émettant : demande-t-il, informe-t-il, s’engage-t-il, refuse-t-il, propose-t-il ? C’est celui-là qui manque. Le contraste avec l’héritage multi-agents classique est net... KQML... puis FIPA-ACL... avaient fait de la force illocutoire un champ obligatoire du message... Les protocoles agentiques de 2025-2026 ne portent pas cette information : un message y transporte une charge utile typée dont l’intention se déduit du contenu, c’est-à-dire du langage naturel, c’est-à-dire du modèle. »*
- **Diagnostic causal approfondi** :
  Si l'analyse de la perte de la force illocutoire dans MCP et A2A est exacte, le diagnostic historique et méthodologique présente deux lacunes majeures :
  1. *Pourquoi FIPA-ACL a échoué dans l'industrie* : L'auteur note avec précaution que le socle ne documente ni l'adoption ni les motifs du déclin de FIPA-ACL. Or, la littérature scientifique a parfaitement élucidé ce déclin (Singh, 1998, 2000 ; Wooldridge, 2002) : la sémantique de FIPA-ACL était fondée sur des états mentaux internes (logique BDI de Cohen et Levesque), exigeant qu'un agent vérifie la "sincérité" de l'émetteur. Il était rigoureusement impossible pour un vérificateur tiers de tester la conformité d'un agent sans avoir accès à ses structures mentales privées ! C'est ce défaut d'observabilité objective qui a condamné FIPA-ACL dans les transactions inter-entreprises.
  2. *Omission de la théorie moderne des engagements sociaux (Social Commitments)* : Le dépassement de FIPA-ACL n'a pas consisté à abandonner la force illocutoire au profit de prose LLM floue, mais à formaliser les *engagements sociaux* (Singh, 2000 ; Fornara & Colombetti, 2004) sous la forme d'engagements conditionnels vérifiables :
     $$C(\text{débiteur}, \text{créancier}, \text{antécédent}, \text{conséquent})$$
     Les transitions d'état d'un engagement (Créé, Actif, Rempli, Violé, Annulé) sont calculables par des automates d'états finis déterministes à partir des messages échangés, sans spéculer sur la psychologie ou la complétion textuelle du LLM. Le compendium passe à côté de cette alternative formelle qui résout exactement l'opposabilité exigée au Livre II.
- **Correctif formel** :
  Remplacer la nostalgie de FIPA-ACL par la spécification d'une couche d'engagements sociaux au-dessus d'A2A. Formaliser chaque message inter-agents non comme du langage naturel libre, mais comme une opération sur le cycle de vie d'un engagement social auditable, garantissant l'opposabilité juridique des délégations multi-agents.

---

### 8. **[Major]** Conflit logique entre la monotonicité d'OWL DL et le non-déterminisme des flux d'agents
- **Localisation exacte** : Chapitre 2, pp. 31-32 (§ 2.3.1 et § 2.3.3) et p. 34 (§ 2.4.1).
- **Citations textuelles exactes** :
  - Page 32 : *« OWL sert l’inférence sous hypothèse de monde ouvert — déduire des faits implicites ; SHACL sert la validation sous hypothèse de monde clos — constater qu’un fait requis manque... »*
  - Page 34 : *« La gouvernance du sens en environnement distribué impose donc de traiter la sortie du modèle comme une proposition soumise à validation — par SHACL (§ 2.3.3), par revue experte, par confrontation aux axiomes ontologiques — et non comme un contrat établi. »*
- **Diagnostic causal approfondi** :
  Le compendium recommande d'adosser l'interopérabilité sémantique des agents à OWL 2 et SHACL. Or, il omet une incompatibilité fondamentale de logique mathématique :
  1. *Monotonicité de la logique de description* : Dans OWL 2 DL (adossé au fragment $\mathcal{SROIQ}(\mathcal{D})$), l'inférence est strictement monotone. L'ajout d'une assertion ne peut jamais supprimer une conclusion préalablement déduite.
  2. *Nature non-monotone de la délibération agentique* : Un agent opérant dans le monde réel procède par hypothèses révisables (Default Reasoning, Reiter 1980 ; AGM Belief Revision, 1985). Si un agent insère dans le triplestore OWL un fait provisoire $\alpha$, puis découvre par rétroaction d'un outil que $\neg \alpha$ est vrai, la base OWL devient inconsistante ($\mathcal{K} \models \bot$). En logique classique, une ontologie inconsistante permet de déduire trivialement n'importe quelle proposition fausse (principe de pseudo-scotus / explosion), paralysant tous les raisonneurs sémantiques.
  3. *Inadéquation de SHACL face aux sorties probabilistes* : SHACL valide des contraintes strictes. Or, les prédictions sémantiques des LLMs sont associées à des distributions de probabilité. L'absence d'une sémantique probabiliste dans SHACL interdit le filtrage par seuil de confiance épistémique.
- **Correctif formel** :
  Déclarer explicitement la restriction d'OWL DL aux référentiels terminologiques invariants (TBox stables). Interdire l'écriture directe des inférences intermédiaires d'agents dans l'A-Box OWL. Prescrire une couche de découplage exploitant des logiques non-monotones (Answer Set Programming - ASP ou Datalog avec négation stratifiée) pour la réconciliation des états dynamiques des agents.

---

### 9. **[Major]** Absence de non-répudiation probatoire dans les traces OpenTelemetry et W3C Trace Context pour la conformité financière
- **Localisation exacte** : Chapitre 3, pp. 44-45 (§ 3.4.5 et § 3.4.6).
- **Citations textuelles exactes** :
  - Page 45 : *« L’observabilité ne sert pas que le diagnostic : elle fonde l’auditabilité, c’est-à-dire la capacité à démontrer après coup, preuves à l’appui, comment une intégration s’est comportée... Dans la banque ouverte... l’auditabilité des appels y est une condition de conformité, non un agrément. »*
- **Diagnostic causal approfondi** :
  Le texte pose que la pile OpenTelemetry (traces distribuées avec W3C Trace Context) constitue le socle de l'auditabilité réglementaire. Il s'agit d'une lacune juridique et technique substantielle :
  - Les spans OpenTelemetry sont conçus pour la performance opérationnelle et le débogage (APM). Ils circulent sur le réseau via des protocoles non signés (OTLP sur gRPC/HTTP) et sont collectés dans des bases de données de séries temporelles modifiables par les administrateurs système.
  - En droit bancaire et financier (notamment sous les régimes BSIF E-23, Sarbanes-Oxley § 404, et l'article 12.1 de la Loi 25 québécoise), une trace d'audit exige des garanties formelles de **non-répudiation, d'intégrité temporelle et d'immutabilité**. Une simple trace OpenTelemetry n'a aucune valeur probatoire devant un tribunal ou un régulateur financier car elle peut être réécrite, purgée ou falsifiée a posteriori sans laisser de trace cryptographique.
- **Correctif formel** :
  Établir une séparation étanche entre *télémétrie opérationnelle non opposable* (OTel) et *journalisation d'audit probatoire opposable*. Exiger que chaque décision agentique à effet contractuel ou réglementaire génère un enregistrement scellé cryptographiquement :
  $$\text{AuditEntry} = \text{Sign}_{K_{\text{Agent}}}(\text{TraceID} \parallel \text{Timestamp} \parallel \text{ContextHash} \parallel \text{Decision} \parallel \text{ToolCallArguments})$$
  ancré de manière immuable dans un registre à arbre de Merkle auditable (Append-Only Log certifié RFC 6962 / RFC 9162).

---

### 10. **[Major]** Sous-spécification des canaux d'exfiltration pour CodeAct et des attaques adversariales multimodales pour Computer Use
- **Localisation exacte** : Chapitre 4, p. 53 (§ 4.2.3) et pp. 59-60 (§ 4.4.3).
- **Citations textuelles exactes** :
  - Page 53 : *« L’action comme code exécutable — CodeAct... exécuter du code généré par un modèle exige un environnement confiné, faute de quoi l’agent dispose d’une capacité d’action quasi illimitée sur le système hôte. »*
  - Page 59 : *« L’exécution de code est l’outil universel le plus puissant... Le confinement est ici une mesure de sécurité non négociable... »*
  - Page 60 : *« Le pilotage d’interface... Le choix entre structure et vision est ainsi autant une décision de surface d’attaque qu’une décision de robustesse... »*
- **Diagnostic causal approfondi** :
  L'auteur prescrit le « confinement » sans caractériser les canaux cachés et la surface d'attaque spécifique aux LLMs :
  1. *Échappement et canaux auxiliaires sous CodeAct* : Un code Python généré dans un bac à sable standard (même conteneurisé sans privilèges root) conserve l'accès aux appels réseau si la tâche requiert des requêtes externes. Un modèle subverti peut exfiltrer des variables d'environnement, des clés d'API ou des données de contexte par stéganographie dans les en-têtes HTTP, par requêtes DNS asynchrones, ou par canaux temporels (timing attacks).
  2. *Attaques adversariales multimodales dans Computer Use* : Dans le pilotage par vision (captures d'écran), l'agent est vulnérable aux attaques par injection visuelle indirecte (adversarial patches, typoglyphie invisible à basse opacité, ou perturbations de pixels imperceptibles). Une image affichée à l'écran peut contraindre le modèle de vision à cliquer sur des coordonnées arbitraires ou à lire des instructions hostiles masquées en arrière-plan. Traiter la vision comme un simple compromis de coût par rapport à l'arbre DOM est une sous-estimation grave du vecteur d'attaque multimodal.
- **Correctif formel** :
  Spécifier les exigences architecturales impératives pour l'exécution d'outils universels :
  - Pour CodeAct : isolation au niveau micro-noyau / MicroVM (type Firecracker ou gVisor) avec interdiction absolue du réseau sortant vers l'Internet public (Air-Gapped Sandbox), tout appel d'API devant obligatoirement transiter par un proxy mandataire d'inspection sémantique L7 à schéma strict.
  - Pour Computer Use : implémentation obligatoire d'un assainisseur visuel (Visual Pre-Processing Defense) et validation de l'arbre d'accessibilité DOM par un analyseur déterministe avant toute exécution de clic ou de saisie clavier.

---

# Minor Corrections and Typos

1. **Chapitre 1, p. 11 (§ 1.1.4.1)** : Ponctuation manquante à la fin de phrase :
   - *Texte actuel* : « quel que soit le soin apporté aux deux premiers Le point est repris au ch. 7... »
   - *Correction* : Ajouter le point final manquant après « premiers » : « ...aux deux premiers**.** Le point est repris au ch. 7... »

2. **Chapitre 2, p. 25 (§ 2.1.1)** : Troncation typographique en pied de page dans le flux textuel :
   - *Texte actuel* : « Gel au 27 juillet 2026 · actualisation du 1er novembre 2026 Page 25 s »
   - *Correction* : Corriger la mention de bas de page en « Page 25 sur 663 ».

3. **Chapitre 2, p. 27 (Tableau 2.1)** : Classification formelle des modes de compatibilité de schéma :
   - *Texte actuel* : Classement de « Transitive » comme 4e régime au même rang que Backward, Forward, Full.
   - *Correction* : Clarifier que la transitivité est un modificateur d'orthogonalité temporelle (Pairwise vs Transitive) et non un quatrième régime disjoint.

4. **Chapitre 2, p. 32 (§ 2.3.3)** : Collision et inversion éditoriale flagrante de paragraphe (constatée sur le PDF imprimé p. 32) :
   - *Texte actuel* : « Ces travaux ne sont pas cités comme acquis : leur ancre de version se fixe au moment de citer, et cette réserve est reconduite ici sans être levée. intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. Un graphe RDF est, par construction, ouvert et sans schéma : tout triplet est licite, l’absence d’information n’est pas une faute, et rien n’interdit a priori d’attribuer une date de naissance à une facture. Pour l’intégration, cette permissivité est SHACL remplit ce rôle... »
   - *Diagnostic et Correction* : La proposition « intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. » a été accidentellement déplacée de la fin du paragraphe suivant vers la fin du paragraphe précédent. Rétablir l'enchaînement syntaxique exact :
     « ...et cette réserve est reconduite ici sans être levée. »
     « Un graphe RDF est, par construction, ouvert et sans schéma... Pour l’intégration, cette permissivité est **intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API.** »
     « **SHACL** remplit ce rôle... »

5. **Chapitre 6, p. 75 (§ 6.3.3)** : Ponctuation manquante et titre de section fusionné dans le corps de texte :
   - *Texte actuel* : « ...sans encore le rejoindre Des annonces d’éditeurs revendiquent depuis... un instantané ne la porte pas. Raisonnement général, outils et tâches d’entreprise. Une seconde famille évalue... »
   - *Correction* : Insérer un point et un saut de paragraphe après « rejoindre. ». Formater « Raisonnement général, outils et tâches d’entreprise » en titre de sous-section ou en intertitre gras distinct du paragraphe courant.

6. **Chapitre 7, p. 79 (§ 7.0)** : Phrase tronquée et collision textuelle dans l'encadré de thèse :
   - *Texte actuel* : « ...instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres. »
   - *Correction* : Rétablir le membre de phrase manquant entre « ch. 10. » et « outils » : « ...instruit au ch. 10. **Ce mouvement analyse l'accès aux** outils, le dialogue entre agents, la découverte... »
