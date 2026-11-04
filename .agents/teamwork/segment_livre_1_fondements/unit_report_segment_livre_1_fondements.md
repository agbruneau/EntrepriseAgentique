**Segment scope**: Livre I — Fondements de l’interopérabilité et ingénierie agentique (pp. 1-79, Liminaires et Chapitres 1 à 6, amorce du Chapitre 7 ; segments S01 à S07 de `REVIEW_PLAN.md` et `ANALYSIS_PARTITION.md`).

# Potential Mistakes and Improvements

---

## 1. Verdict Exécutif sur la Thèse du Livre I : La fausse promesse de linéarité mécanique face à l'entropie stochastique

Le Livre I d'*Interopérabilité et Orchestration en Entreprise Agentique* entreprend une tâche ambitieuse et nécessaire : fonder l'ingénierie des systèmes d'agents autonomes sur le demi-siècle d'histoire de l'intégration logicielle distribuée (EAI, SOA, EDA, API Web, Zero Trust, Web Sémantique). L'ouvrage déploie une culture technique impressionnante et une réelle hauteur de vue architecturale.

Toutefois, l'audit critique et contradictoire approfondi mené au niveau racine révèle une faille épistémologique et théorique cardinale qui traverse l'ensemble des six premiers chapitres : **la fausse promesse de linéarité mécanique face à l'entropie stochastique**.

L'argument directeur de l'auteur repose sur une analogie séduisante mais erronée : de même que l'EAI et les bus de services (ESB) auraient « ramené le coût quadratique $N(N-1)/2$ du point-à-point à un coût linéaire en $2N$ grâce au modèle de données canonique », l'adoption des protocoles agentiques standardisés (MCP, A2A) permettrait de surmonter le fardeau de l'interopérabilité agentique par une simple extension de la pile d'abstraction logicielle classique.

Cette construction théorique s'effondre sous l'analyse contradictoire rigoureuse :
1. **Falsification topologique et économique** : La formule $N(N-1)/2$ est le nombre d'arêtes d'un graphe complet non orienté ($K_N$), une hypothèse de clique démentie par la sparsité des réseaux applicatifs d'entreprise ($|E| = \mathcal{O}(N)$). De surcroît, le coût de possession d'un modèle canonique partagé (CDM) sous évolution continue est lui-même quadratique $\mathcal{O}(N^2)$ en raison de l'invalidation récursive des adaptateurs et de l'explosion combinatoire du consensus organisationnel.
2. **Déplacement de la complexité vers l'entropie d'inférence** : Dans un réseau d'agents autonomes, le défi de l'intégration ne réside plus dans le tirage de liaisons statiques (résolu en $\mathcal{O}(1)$ par les déclarations d'outils JSON-RPC), mais dans **l'explosion combinatoire de l'espace des trajectoires multi-agents** ($\mathcal{O}(|\mathcal{A}|^{N \cdot T})$), la consommation exponentielle de jetons de contexte, la latence stochastique et le risque d'interférences destructives d'état.
3. **Impuissance des mécanismes déterministes classiques** : Le compendium tente d'endiguer l'incertitude des modèles de langage par des briques déterministes empruntées aux systèmes distribués transactionnels (réessais exponentiels, budgets de jetons, validation Zero Trust NIST SP 800-207, schémas OWL 2 DL et SHACL). Or :
   - Les pannes d'agents sont des pannes sémantiques distributionnelles et non des congestions réseau transitoires : un réessai exponentiel sans altération de la distribution de probabilité répète la défaillance à l'identique.
   - Les budgets de pas ne garantissent nullement la terminaison correcte, mais forcent un avortement arbitraire qui laisse des effets de bord financiers ou transactionnels suspendus.
   - Le Zero Trust réseau L4/L5 valide cryptographiquement l'infrastructure hôte (certificats SPIFFE SVID), mais demeure aveugle à la corruption de l'intention par injection indirecte (L7 sémantique).
   - OWL 2 DL souffre d'une intraitabilité algorithmique en 2NEXPTIME et d'une monotonicité stricte qui engendre une explosion déductive (*ex falso quodlibet*) dès qu'un agent révise empiriquement une croyance erronée.
   - L'auto-compaction de contexte viole l'inégalité de traitement de l'information (Shannon), provoquant une amnésie épistémique irréversible que la rétention d'un pointeur passif ne peut compenser.

Le Livre I doit donc être refondé : non pas comme le récit triomphal d'une linéarisation mécanique de l'intégration, mais comme **la théorie de la contention de l'entropie stochastique sous contraintes d'auditabilité juridique et prudentielle**.

---

## 2. Matrice Récapitulative des Défauts (Bloquants, Majeurs, Mineurs)

| Identifiant | Sévérité | Chapitre & Localisation | Nature du Défaut Formel | Impact Systémique |
| :--- | :---: | :--- | :--- | :--- |
| **DEF-01** | **[Critical]** | Ch. 1, pp. 5-6, 14, 22 | Falsification du modèle de coût $N(N-1)/2$, illusion de la linéarité $2N$ du format pivot et allégation erronée sur l'adjonction de système. | Invalide le modèle économique et topologique fondateur du Livre I. |
| **DEF-02** | **[Critical]** | Ch. 1, pp. 8-10 ; Ch. 7, p. 80 | Rupture taxonomique du LCIM (amputation du niveau 6 Conceptuel), conflit d'ordre partiel EIF/LCIM, omission des couplages stochastiques. | Supprime le palier d'opposabilité réglementaire et fausse la modélisation des dépendances LLM. |
| **DEF-03** | **[Critical]** | Ch. 6, p. 76 (Table 6.2, Fig. 6.4) | Falsification de la métrique $pass^k$ de $\tau$-bench et confusion mathématique avec l'effondrement intra-trajectoire $q^T$. | Confusion probabiliste élémentaire entre réplication inter-essais et composition géométrique temporelle. |
| **DEF-04** | **[Critical]** | Ch. 3, pp. 36-37, 39-41 | Rupture du modèle AAA / Zero Trust face au détournement sémantique, à l'injection indirecte et inadaptation de RFC 8693. | Faille de sécurité structurelle : l'infrastructure valide l'émetteur mais ignore la subversion de l'intention. |
| **DEF-05** | **[Critical]** | Ch. 2, pp. 32-34 (Fig. 2.3) | Faux parallélisme d'extensibilité GAV vs LAV, omission de GLAV/BAV, et intraitabilité computationnelle d'OWL 2 DL (2NEXPTIME). | Masque la NP-complétude de la réécriture de requêtes et prescrit des technologies inopérantes au runtime. |
| **DEF-06** | **[Critical]** | Ch. 4, pp. 51-54, 58, 60 | Effondrement stochastique de ReAct ($p^T$ et super-exponentiel), invalidité de ReWOO en univers POMDP, et illusion du décodage contraint. | Fausse assurance de terminaison ; méconnaissance des limites du décodage grammatical face aux contraintes d'état métier. |
| **DEF-07** | **[Critical]** | Ch. 5, pp. 63-64, 67-68 | Irréversibilité informationnelle de la compaction mémorielle (Shannon/DPI), amnésie épistémique et pathologie de classement du RRF. | Inégalité de Shannon violée ; inversion mathématique aberrante des rangs documentaires en recherche hybride. |
| **DEF-08** | **[Major]** | Ch. 1, pp. 23-24 (§ 1.6.2.2) | Évasion théorique majeure : exclusion arbitraire du consensus distribué et de la coordination sous partition réseau en finance. | Fragilise la crédibilité de l'ouvrage face aux exigences prudentielles et transactionnelles du secteur financier. |
| **DEF-09** | **[Major]** | Ch. 3, pp. 38, 40-41 | Angles morts du Zero Trust face aux plans multi-sauts, confusion d'identité SPIFFE vs mandat, inexactitude SAML 2.0 et omission ReBAC. | Absence de suivi de teinte (taint tracking) et limitation d'IAM aux topologies linéaires pré-agentiques. |
| **DEF-10** | **[Major]** | Ch. 4, p. 49 ; Ch. 6, pp. 72-73 ; Ch. 7, pp. 81-82 | Falsification du diagnostic d'échec de FIPA-ACL, omission des engagements sociaux décidables, et réfutation de la force illocutoire dans MCP/A2A. | Réductionnisme historique sur les causes de rejet logiciel de FIPA-ACL et méconnaissance de la pragmatique MCP/A2A. |
| **DEF-11** | **[Major]** | Ch. 2, pp. 31-32, 34 | Conflit logique formel entre la monotonicité stricte d'OWL 2 DL et le non-déterminisme des flux d'agents. | Incohérence déductive (*ex falso quodlibet*) lors de la révision empirique des croyances d'un agent. |
| **DEF-12** | **[Major]** | Ch. 3, pp. 44-45 (§ 3.4.5, § 3.4.6) | Absence de valeur probatoire et de non-répudiation des traces OpenTelemetry et W3C Trace Context pour l'auditabilité financière. | Confusion entre métrologie opérationnelle non sécurisée et journalisation d'audit opposable sous BSIF E-23 / Loi 25. |
| **DEF-13** | **[Major]** | Ch. 6, pp. 71-72 ; Ch. 5, pp. 61-62 ; Ch. 6, p. 76 | Omission des topologies d'essaim (Swarm), de tableau noir et de marché, et duplications verbatim systématiques tableaux/figures. | Lacune taxinomique fondamentale sur les architectures de coordination décentralisée et gonflage artificiel de volume. |
| **DEF-14** | **[Major]** | Ch. 4, p. 53 (§ 4.2.3) | Chimère bibliographique et fausse attribution sur Plan-and-Solve Prompting. | Confusion d'équipes de recherche (Wang, Wei, Schuurmans vs Wang, Xu, Lan et coll.) au sein de la même phrase. |
| **DEF-15** | **[Major]** | Ch. 4, pp. 53, 59-60 | Sous-spécification des canaux d'exfiltration pour CodeAct et des attaques adversariales multimodales pour Computer Use. | Sous-estimation des vecteurs d'attaque par canaux auxiliaires DNS/temporels et injections visuelles indirectes. |
| **TYP-01** | **[Minor]** | Ch. 2, p. 32 (§ 2.3.3) | Transposition matérielle et inversion de paragraphe lors de la mise en page (fragment SHACL orphelin). | Coquille structurelle de composition rompant la syntaxe logique de deux paragraphes consécutifs. |
| **TYP-02** | **[Minor]** | Ch. 7, p. 79 (§ 7.0) | Télescopage textuel entre l'encadré Thèse et le corps du second paragraphe (rupture sur « ses »). | Fragment égaré dans l'encadré Thèse laissant la transition vers le Chapitre 7 syntaxiquement incomplète. |
| **TYP-03** | **[Minor]** | Ch. 1, p. 11 (§ 1.1.4.1) | Ponctuation manquante en fin de phrase (« deux premiers Le point »). | Coquille typographique élémentaire. |
| **TYP-04** | **[Minor]** | Ch. 4, p. 47 (§ 4.0.2) | Césure fautive et troncation de mot en bas de page (« délibé »). | Rupture lexicale lors du saut de page dans le flux textuel. |
| **TYP-05** | **[Minor]** | Ch. 6, p. 75 (§ 6.3.3) | Ponctuation manquante et fusion de titre dans le corps de texte. | Absence de point final et défaut de mise en relief de l'intertitre. |
| **TYP-06** | **[Minor]** | Ch. 2, p. 25 (§ 2.1.1) | Troncation du numéro de page dans le pied de page (« Page 25 s »). | Artefact de composition typographique. |
| **TYP-07** | **[Minor]** | Ch. 2, p. 27 (Tableau 2.1) | Classification erronée de la compatibilité de schéma (Transitive érigée en modalité disjointe). | Confusion entre modalité de compatibilité et propriété de clôture temporelle (Pairwise vs Transitive). |
| **TYP-08** | **[Minor]** | Liminaires & Ch. 1, Ch. 6 | Incohérence interne de la doctrine de gel documentaire (27 juillet 2026 vs insertions tardives d'octobre 2026). | Contradiction méthodologique entre la déclaration de gel liminaire et le corps du texte. |
| **TYP-09** | **[Minor]** | Ch. 1 à 6 (pp. 7, 9, 16, 20, 29, 31, 40, 42, 51, etc.) | Numérotation discontinue et non standardisée des figures d'après l'indice de sous-section. | Crée l'impression erronée de figures manquantes lors de la lecture séquentielle. |

---

## 3. Défauts Bloquants [Critical]

### DEF-01 : Falsification du modèle de coût d'intégration $N(N-1)/2$, illusion de la linéarité en $2N$ du modèle canonique (CDM), et allégation erronée sur l'adjonction d'un système

- **Localisation exacte** : Chapitre 1, pp. 5-6 (§ 1.0.1), p. 14 (§ 1.3.1.1), et p. 22 (§ 1.6.1).
- **Citations textuelles exactes du manuscrit** :
  - Page 5 (§ 1.0.1) : *« Cette intégration point-à-point engendre une croissance combinatoire du nombre de connexions : raccorder N systèmes susceptibles de dialoguer deux à deux peut requérir jusqu’à N(N−1)/2 liaisons, chacune avec sa logique de transport, de format et de correspondance. »*
  - Page 6 (§ 1.0.1) : *« ...notamment par l’introduction d’un intermédiaire et d’un format pivot qui ramènent la complexité de N×N à un ordre linéaire (voir § 1.6.1). »*
  - Page 14 (§ 1.3.1.1) : *« ...la prolifération des connexions point-à-point engendre une dette d’intégration dont le coût croît quadratiquement avec le nombre de systèmes. La SOA propose de substituer à ce maillage N×N une médiation par services réutilisables... »*
  - Page 22 (§ 1.6.1) : *« Lorsque N applications doivent s’échanger des données, le couplage par traductions directes croît en N×N : chaque paire exige son propre traducteur, et l’ajout d’un système impose de modifier tous les autres. Le modèle de données canonique brise cette explosion combinatoire en introduisant un format pivot indépendant des applications : chaque système ne traduit qu’entre son format propre et le canonique, ramenant le coût d’intégration à un ordre linéaire, en 2N. »*
- **Diagnostic causal approfondi** :
  Ce passage cumule plusieurs erreurs mathématiques, topologiques et conceptuelles qui vicient la thèse économique du chapitre :
  1. *Confusion formelle entre graphes orientés et non orientés* : La formule $\binom{N}{2} = \frac{N(N-1)}{2}$ correspond strictement au nombre d'arêtes d'un graphe complet non orienté $K_N$. Or, en intégration logicielle, les transformations de schémas sont directionnelles et asymétriques : un adaptateur $T_{A \to B}: \mathcal{S}_A \to \mathcal{S}_B$ ne réalise pas la transformation réciproque $T_{B \to A}: \mathcal{S}_B \to \mathcal{S}_A$ en raison des projections d'attributs non injectives. Dans le pire cas d'un maillage bilatéral exhaustif, le nombre de traducteurs orientés est strictement $N(N-1) = N^2 - N$. Par ailleurs, prétendre p. 22 qu'un modèle pivot exige « $2N$ » adaptateurs correspond précisément à la réduction d'un graphe orienté complet $N(N-1)$ vers une topologie en étoile avec flux bidirectionnels ($2 \times N$), ce qui contredit directement la valeur de référence $\frac{N(N-1)}{2}$ avancée p. 5.
  2. *Affirmation factuellement et formellement fausse relative à l'adjonction d'un système* : Le texte affirme péremptoirement p. 22 que *« l'ajout d'un système impose de modifier tous les autres »*. C'est rigoureusement inexact en intégration point-à-point. L'introduction d'un $(N+1)$-ième nœud requiert d'écrire au plus $N$ nouvelles liaisons (soit $2N$ adaptateurs orientés) pour raccorder ce nouvel entrant aux systèmes existants. Les $\frac{N(N-1)}{2}$ liaisons bilatérales préexistantes demeurent strictement intactes et n'exigent aucune modification, en vertu du principe de découplage des interfaces pair-à-pair.
  3. *Hypothèse topologique irréaliste (clique $K_N$ vs graphe clairsemé)* : Dans les architectures d'entreprise réelles, la topologie d'intégration n'est jamais une clique complète $K_N$, mais un graphe clairsemé (*sparse graph*), généralement sans échelle (*scale-free*) ou hiérarchique, où le degré moyen des nœuds est borné par une constante $\langle k \rangle \ll N$. Le nombre effectif d'arêtes est $|E| = \frac{1}{2} N \langle k \rangle = \mathcal{O}(N)$, conférant déjà à l'intégration point-à-point un coût structurel linéaire.
  4. *Fausse linéarité du modèle de données canonique (CDM) sous évolution sémantique* : Prétendre que le format pivot garantit un coût en $2N$ postule un schéma canonique $\mathcal{C}$ universel et immuable. Dès qu'un système source évolue ou émet des concepts non couverts par $\mathcal{C}$, le schéma pivot doit être révisé ($\mathcal{C} \to \mathcal{C}'$). Toute modification de $\mathcal{C}$ force l'audit et la réécriture potentielle des $2N$ adaptateurs existants. En théorie de l'intégration (Halevy, 2001 ; Bernstein, 2003), le coût d'arbitrage de gouvernance d'un modèle pivot croît de manière combinatoire en fonction des comités de normalisation inter-équipes ($\mathcal{O}(N^2)$ interactions humaines).
  5. *Inadéquation doctrinale pour l'intégration agentique* : Les systèmes multi-agents contemporains (via MCP ou A2A) n'adoptent ni le maillage d'adaptateurs statiques en $\mathcal{O}(N^2)$, ni le carcan rigide du CDM en $2N$. Chaque agent expose dynamiquement son schéma d'outil en $\mathcal{O}(1)$. La médiation est déplacée au runtime dans la fenêtre d'attention du LLM (*in-context dynamic grounding*). Le véritable coût n'est plus un coût de développement logiciel linéaire ou quadratique, mais un coût opérationnel récurrent stochastique par inférence (consommation de jetons, latence, dérive sémantique) et un risque d'interférences dans l'espace d'états conjoints.
- **Démonstration mathématique formelle et correctif** :
  Remplacer le modèle informel par une formalisation explicite en théorie des graphes :
  Soit un réseau d'intégration modélisé par un graphe orienté $G = (V, E)$ où $|V| = N$. Le nombre d'adaptateurs point-à-point requis est $|E| = \sum_{i=1}^N d^+(v_i)$. Dans le cas d'une clique orientée complète, $|E| = N(N-1) \approx N^2$. Dans un réseau d'entreprise réel à degré sortant borné par $k_{\max} \ll N$, $|E| \le k_{\max} N = \mathcal{O}(N)$.
  Lors de l'introduction d'un nouveau nœud $v_{N+1}$, le nombre d'arêtes ajoutées est $\Delta |E| = d^+(v_{N+1}) + d^-(v_{N+1}) \le 2N$, avec une invariance stricte des liaisons préexistantes :
  $$\forall (u, w) \in E, \quad \Delta E_{(u,w)} = 0$$
  Pour le modèle canonique, intégrer la dynamique d'évolution temporelle continue sur un horizon $T$ :
  $$TCO_{\text{CDM}}(T) = 2N \cdot c_{\text{build}} + \sum_{t=1}^T \sum_{i=1}^N \lambda_i(t) \left[ c_{\Delta \mathcal{C}} + \sum_{j \neq i} \rho_{ij} \cdot c_{\text{update}}(\mathcal{S}_j \leftrightarrow \mathcal{C}') \right]$$
  où $\lambda_i$ est le taux d'évolution du domaine $i$ et $\rho_{ij} \in [0, 1]$ est la probabilité d'impact collatéral sur l'adaptateur du domaine $j$. Dès que le réseau est sémantiquement couplé ($\rho_{ij} > 0$), la maintenance récurrente du format pivot est strictement en $\mathcal{O}(N^2)$.
  Pour l'intégration agentique, formaliser l'espérance de coût d'inférence stochastique :
  $$\mathbb{E}[C_{\text{agentic}}] = \sum_{(u, v) \in E} \mathbb{E}[\text{Tokens}(u \to v)] \cdot c_{\text{token}} + \sum_{v \in V} \frac{\tau_{\text{exec}}(v)}{1 - P(\text{erreur}_v)}$$
  tandis que l'espace des trajectoires conjointes sur un horizon $T$ croît en $\mathcal{O}(|\mathcal{A}|^{N \cdot T})$.

---

### DEF-02 : Rupture taxonomique du LCIM (amputation du niveau 6 Conceptuel, conflit d'ordre partiel EIF/LCIM) et omission des couplages stochastiques

- **Localisation exacte** : Chapitre 1, pp. 8-10 (§ 1.1.2, Figure 1.1, § 1.1.3.1) et Chapitre 7, p. 80 (§ 7.1.2 et Tableau 7.1).
- **Citations textuelles exactes du manuscrit** :
  - Page 9 (§ 1.1.2) : *« Le Levels of Conceptual Interoperability Model (LCIM) approfondit la couche sémantique en distinguant des degrés de maturité conceptuelle de l’échange. À la pile technique-syntaxique-sémantique, il superpose les niveaux pragmatique, dynamique et conceptuel, articulés autour de trois notions : l’integratability (...), l’interoperability (...) et la composability (...). Le modèle a été raffiné en une échelle à sept niveaux, du niveau 0 — absence d’interopérabilité — jusqu’à l’interopérabilité conceptuelle, où les hypothèses et abstractions des modèles sont elles-mêmes documentées et alignées. »*
  - Page 9 (Figure 1.1) : *« Pile canonique : 1 Technique, 2 Syntaxique, 3 Sémantique, 4 Organisationnel. Extension LCIM : Pragmatique · Dynamique · Conceptuel. Superposés à la couche sémantique. »*
  - Page 10 (§ 1.1.3.1) : *« Lecture de l’auteur — les protocoles agentiques ne réduisent pas le couplage de manière uniforme : ils traitent avec vigueur le couplage de format et d’interaction, laissent largement ouvert le couplage de localisation... et rétablissent un couplage de confiance... »*
  - Page 80 (Tableau 7.1) : *« Tableau 7.1 — Les cinq niveaux du LCIM appliqués à la pile agentique. Niveau : Technique, Syntaxique, Sémantique, Pragmatique, Dynamique. »*
- **Diagnostic causal approfondi** :
  1. *Amputation injustifiée du niveau 6 (Conceptuel) dans le Tableau 7.1* : Dans sa formulation canonique établie par Andreas Tolk et coll. (2003, 2007, 2009), le LCIM comprend formellement **sept niveaux cumulatifs**, indexés de 0 à 6 :
     - $L_0$ : *No Interoperability* (Systèmes isolés).
     - $L_1$ : *Technical Interoperability* (Transport physique, bits et octets).
     - $L_2$ : *Syntactic Interoperability* (Grammaires, formats, protocoles d'encodage).
     - $L_3$ : *Semantic Interoperability* (Sens partagé, schémas, ontologies de domaine).
     - $L_4$ : *Pragmatic Interoperability* (Contexte d'usage, flux de processus, actes de langage).
     - $L_5$ : *Dynamic Interoperability* (États d'exécution en ligne, ré-ordonnancement, découverte).
     - $L_6$ : *Conceptual Interoperability* (Alignement des modèles conceptuels sous-jacents, hypothèses du monde, contraintes de finalité).
     Alors que la page 9 mentionne l'échelle complète à 7 niveaux, le Tableau 7.1 en page 80 titre de manière erronée : « Les cinq niveaux du LCIM appliqués à la pile agentique », en éliminant complètement le niveau 6 (*Conceptual*) ainsi que le niveau 0. Cette suppression détruit la cohérence de l'ouvrage : le niveau 6 est précisément le lieu où s'opèrent l'alignement des modèles du monde (*World Models*), l'opposabilité juridique des contraintes de finalité, et le respect des normes prudentielles (BSIF E-23, Loi 25 québécoise art. 12.1). Réduire le modèle au niveau dynamique rétrograde l'agentique à un automate d'états finis.
  2. *Conflit d'ordre partiel dans la Figure 1.1* : En juxtaposant la pile européenne quadri-couche (EIF : Technique $\prec$ Sémantique $\prec$ Organisationnel $\prec$ Juridique) et en greffant latéralement les niveaux $L_4, L_5, L_6$ du LCIM au niveau de la seule couche sémantique, la Figure 1.1 introduit une rupture d'ordre partiel mathématiquement indécidable. Où se situe le niveau Organisationnel par rapport à Dynamique ($L_5$) et Conceptuel ($L_6$) ? Dans le LCIM, la pragmatique ($L_4$) et la dynamique ($L_5$) intègrent déjà les règles de coordination inter-organisationnelle. Le modèle cumulatif strict de Tolk interdit de considérer $L_4, L_5, L_6$ comme une simple sous-branche de $L_3$.
  3. *Omission des facettes de couplage propres aux agents stochastiques* : La typologie en 5 facettes héritée de Hohpe (2003) (technologie, format, localisation, temporalité, interaction) a été conçue pour des systèmes déterministes. Dans un écosystème multi-agents piloté par des LLMs, trois dimensions de couplage additionnelles sont critiques :
     - *Couplage d'état latent et de fenêtre de contexte* ($\mathcal{C}_{\text{state}}$) : dépendance forte à la taille du contexte actif, à la gestion du cache KV et à la dérive de l'historique d'attention.
     - *Couplage de distribution probabiliste et fragilité d'invite* ($\mathcal{C}_{\text{distrib}}$) : sensibilité extrême aux variations lexicales infimes d'un prompt (*prompt fragility*), où une modification sans rupture syntaxique altère drastiquement la distribution de sortie du modèle.
     - *Couplage épistémique et d'intégrité de croyance* ($\mathcal{C}_{\text{epistemic}}$) : dépendance d'un agent aval à la véracité factualisée et à la non-contamination de l'agent amont par injection d'invite indirecte.
  4. *Contradiction factuelle sur l'atténuation du couplage de format par MCP/A2A* : Prétendre que les protocoles agentiques « traitent avec vigueur le couplage de format » (p. 10) est inexact. MCP (Model Context Protocol) impose des schémas JSON Schema stricts pour la déclaration des outils (`tools/call`). Tout argument non conforme déclenche un rejet syntaxique immédiat (`-32602 Invalid params`). De plus, le cycle requête-réponse synchrone de JSON-RPC 2.0 (sur stdio ou SSE) impose un couplage d'interaction temporellement bloquant.
- **Correctif formel explicite** :
  - Rétablir l'échelle canonique intégrale du LCIM à 7 niveaux dans le Tableau 7.1 :
    $$\mathcal{L}_{\text{LCIM}} = \{ L_0: \text{Isolé}, L_1: \text{Technique}, L_2: \text{Syntaxique}, L_3: \text{Sémantique}, L_4: \text{Pragmatique}, L_5: \text{Dynamique}, L_6: \text{Conceptuel} \}$$
    en formalisant le rôle du niveau $L_6$ comme la frontière de validation formelle de l'alignement de finalité et du risque de modèle (BSIF E-23).
  - Clarifier la relation entre l'EIF et le LCIM en définissant un opérateur de projection explicite :
    $$\Pi_{\text{EIF}} : \text{LCIM} \to \{ \text{Technique}, \text{Syntaxique}, \text{Sémantique}, \text{Organisationnel}, \text{Juridique} \}$$
    où $L_1 \mapsto \text{Technique}$, $L_2 \mapsto \text{Syntaxique}$, $L_3 \mapsto \text{Sémantique}$, et $\{L_4, L_5, L_6\} \mapsto \text{Organisationnel} \times \text{Juridique/Conceptuel}$.
  - Formaliser le vecteur de couplage agentique sous la forme d'un 8-uplet :
    $$\mathbf{C} = \langle c_{\text{tech}}, c_{\text{format}}, c_{\text{loc}}, c_{\text{temp}}, c_{\text{inter}}, c_{\text{state}}, c_{\text{distrib}}, c_{\text{epistemic}} \rangle$$
    et rectifier l'affirmation de la page 10 en actant que MCP rigidifie le contrat syntaxique au lieu de le relâcher.

---

### DEF-03 : Falsification de la métrique d'évaluation $pass^k$ de $\tau$-bench et confusion mathématique avec l'effondrement intra-trajectoire $q^T$

- **Localisation exacte** : Chapitre 6, § 6.4.2 (p. 76), Tableau 6.2 et Figure 6.4 (p. 76).
- **Citations textuelles exactes du manuscrit** :
  - Tableau 6.2 (p. 76) : *« pass^k ... la probabilité que les k tentatives réussissent toutes — la consistance. Chute brutalement dès que la fiabilité par étape s’éloigne de la perfection. »*
  - Page 76 (§ 6.4.2) : *« La seconde — pass^k, introduite par τ-bench (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues et multi-étapes. Cette dégradation — où une probabilité d’échec par pas même faible se compose géométriquement sur une longue trajectoire — est l’un des constats les plus robustes du domaine, et l’une des questions que le ch. 49 laisse ouvertes. »*
  - Figure 6.4 (p. 76) : *« pass^k — LA CONSISTANCE ... Les k tentatives réussissent toutes ... chute brutale dès que la fiabilité par étape s'éloigne de la perfection ... s'effondre avec k ... Une probabilité d’échec par pas même faible SE COMPOSE GÉOMÉTRIQUEMENT sur une longue trajectoire : c’est l’un des constats les plus robustes du domaine, et la raison pour laquelle un agent se caractérise par sa courbe de consistance... »*
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
  La probabilité conjointe que $k$ essais indépendants d'une tâche à $T$ étapes réussissent tous s'écrit formellement :
  $$\text{pass}^k(T) = \left( \prod_{t=1}^T q_t \right)^k$$
  Remplacer au Tableau 6.2 « fiabilité par étape » par « taux de succès global par exécution complète ».

---

### DEF-04 : Rupture fondamentale du modèle AAA / Zero Trust face à la compromission d'intention sémantique, à l'injection indirecte et limites du Token Exchange

- **Localisation exacte** : Chapitre 3, § 3.1.1 (pp. 36-37), § 3.2.3 (pp. 39-40), § 3.3.1 (pp. 40-41).
- **Citations textuelles exactes du manuscrit** :
  - Page 36 (§ 3.1.1) : *« Le mandataire confus (confused deputy)... une passerelle qui réutilise ses propres droits au lieu de propager ceux du client transforme tout point d’entrée en vecteur d’escalade. C’est le défaut le plus important de cette sous-section pour la suite du Livre : il connaît une variante moderne dans les architectures agentiques, où une injection d’invite indirecte détourne le plan d’un agent en lui faisant traiter comme instructions des contenus externes. »*
  - Page 40 (§ 3.3.1) : *« Le zero-trust formalise le principe ne jamais faire confiance, toujours vérifier... point de décision et point d’application de politique, évaluation continue par requête... L’application du zero-trust aux services exige une identité pour les acteurs non humains, à durée de vie courte et vérifiable. SPIFFE et son implémentation de référence SPIRE fournissent à chaque charge un identifiant et un document d’identité vérifiable... »*
  - Page 41 (§ 3.3.1) : *« Lecture de l’auteur — c’est l’un des rares endroits de ce Livre où une classe entière d’incidents disparaît plutôt que de se déplacer. »*
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

### DEF-05 : Faux parallélisme d'extensibilité GAV vs LAV en intégration sémantique, omission de GLAV/BAV, et intraitabilité computationnelle d'OWL 2 DL (2NEXPTIME) face aux flux d'agents

- **Localisation exacte** : Chapitre 2, § 2.3.3 (p. 32), § 2.3.4 (pp. 32-33), § 2.4.1 (pp. 34-35).
- **Citations textuelles exactes du manuscrit** :
  - Page 33 (§ 2.3.4) : *« Le formalisme distingue ici deux régimes de correspondance, et le choix entre eux est structurant :
  • GAV (Global-As-View) — chaque concept global est défini comme une vue sur les sources. Réécriture de requête simple ; ajout de source coûteux, puisqu’il faut revoir les définitions globales.
  • LAV (Local-As-View) — chaque source est décrite comme une vue sur le schéma global. Extensibilité supérieure — ajouter une source n’affecte pas les autres — au prix d’une réécriture de requête plus complexe.
  Ce choix rejoue, au niveau du sens, l’arbitrage entre couplage et évolutivité qui structure tout le Livre : GAV optimise le présent, LAV optimise l’arrivée du prochain participant. »*
  - Page 34 (§ 2.4.1) : *« La gouvernance du sens en environnement distribué impose donc de traiter la sortie du modèle comme une proposition soumise à validation — par SHACL (§ 2.3.3), par revue experte, par confrontation aux axiomes ontologiques — et non comme un contrat établi. »*
- **Diagnostic causal approfondi** :
  1. *Omission de la NP-complétude et de l'indécidabilité de LAV* : Qualifier la réécriture de requête en LAV de simplement « plus complexe » occulte des résultats fondamentaux de la théorie des bases de données. Dans le paradigme LAV (*Answering Queries Using Views*, Levy et al., 1995 ; Halevy, 2001 ; Lenzerini, 2002), trouver la réécriture maximale contenue (*maximally contained rewriting*) pour des requêtes conjonctives est un problème **NP-complet** en la taille de la requête (Abiteboul & Duschka, 1998). Des algorithmes comme *Bucket* ou *MiniCon* (Pottinger & Halevy, 2001) subissent une explosion combinatoire exponentielle dès que le schéma s'étend, et le problème devient indécidable en présence de contraintes d'intégrité référentielle ou d'axiomes ontologiques expressifs (TBox OWL).
  2. *Inadéquation cognitive des LLMs et omission de GLAV* : Un agent LLM est incapable de garantir mathématiquement la correction d'une réécriture LAV sans un moteur Datalog déterministe sous-jacent. De plus, la pratique moderne de l'intégration sémantique a dépassé la dichotomie GAV/LAV au profit de **GLAV (Global-and-Local-As-View)** et des dépendances génératrices de tuples (*tgds*, Fagin et coll., 2005 : $\phi_{\mathcal{S}}(\mathbf{x}) \to \exists \mathbf{y} \psi_{\mathcal{G}}(\mathbf{x}, \mathbf{y})$), seul formalisme capable d'associer des vues sources à des vues globales pour des flux d'agents hétérogènes.
  3. *Intraitabilité computationnelle d'OWL 2 DL face aux flux d'agents* : La logique de description sous-jacente à OWL 2 DL est $\mathcal{SROIQ}(\mathcal{D})$. Le test de cohérence en $\mathcal{SROIQ}(\mathcal{D})$ est **2NEXPTIME-complet** (Kazakov, 2008). Dans une boucle agentique en temps réel où des messages JSON-RPC transitent à haute fréquence, soumettre chaque transaction à un raisonneur OWL 2 DL complet engendre des latences prohibitives (secondes voire minutes), incompatibles avec les contraintes d'exécution interactives.
  4. *Inapplicabilité opérationnelle de SHACL au runtime des agents* : Recommander SHACL pour valider les sorties d'agents en direct (§ 2.4.1) méconnaît les exigences de performance temps réel. SHACL requiert la sérialisation d'un graphe RDF et l'exécution d'un moteur de règles sur graphe en lot (*batch*). En production agentique contemporaine, la validation sémantique et syntaxique à l'exécution est garantie au niveau des tokens par **décodage guidé par grammaires** (*grammar-guided decoding* / *structured outputs* via JSON Schema projeté sur des automates à pile déterministes sur logits, implémenté dans vLLM, SGLang, Outlines), reléguant SHACL à l'audit asynchrone des graphes de connaissances.
- **Correctif formel et contre-exemple explicite** :
  Exposer le théorème d'impossibilité de réécriture équivalente par un contre-exemple concret :
  Soit une ontologie globale $\mathcal{G}$ avec les relations $\text{Agent}(x)$, $\text{Mandat}(x, y)$, $\text{Institution}(y)$.
  En LAV, soient deux vues d'agents $V_1, V_2$ définies par :
  $$V_1(x) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$$
  $$V_2(y) \leftarrow \text{Institution}(y)$$
  Pour une requête globale $Q(x, y) \leftarrow \text{Agent}(x) \wedge \text{Mandat}(x, y) \wedge \text{Institution}(y)$, aucune réécriture exacte équivalente n'existe à partir de $V_1$ et $V_2$ car la variable de jointure $y$ est projetée hors de $V_1$. Seule une réécriture contenue non équivalente est dérivable.
  Prescrire formellement l'utilisation de médiateurs GLAV déterministes et substituer au raisonneur OWL 2 DL complet les profils polynomiaux :
  - **OWL 2 QL** (fondé sur DL-Lite), garantissant une réécriture de requêtes en $\text{AC}^0$ (LogSpace sur les données) ;
  - **OWL 2 EL** (fondé sur $\mathcal{EL}^{++}$), garantissant un raisonnement en temps polynomial $\text{PTIME}$.

---

### DEF-06 : Effondrement stochastique de la boucle ReAct ($p^T$ et super-exponentiel), invalidité formelle de ReWOO en univers partiellement observable (POMDP), et illusion du décodage contraint (JSON Schema)

- **Localisation exacte** : Chapitre 4, § 4.1.5 (p. 51), § 4.2.1 (pp. 51-52), § 4.2.3 (pp. 53-54), § 4.4.1 (p. 58), § 4.4.4 (p. 60).
- **Citations textuelles exactes du manuscrit** :
  - Page 51 (§ 4.1.5) : *« les horizons longs — les agents s’effondrent sur les tâches à nombreuses étapes, où l’erreur se compose pas après pas... »*
  - Page 52 (§ 4.2.3) : *« L’entrelacement raisonnement-action — ReAct... à chaque pas, une étape de raisonnement verbalisé et une action dont le résultat est réinjecté avant le pas suivant... Chaque tour consomme des jetons en proportion du contexte accumulé... Sur les trajectoires longues, ce patron dérive — accumulation d’erreurs non corrigées, boucles répétitives, perte du but initial à mesure que le contexte se dilue. »*
  - Page 52 (Mise en œuvre) : *« Le critère d’arrêt n’est pas un détail mais une garantie de terminaison. Une boucle sans budget d’appels explicite ni détection de stagnation peut diverger... Fixer dès la conception un budget de pas, un plafond de jetons et une condition d’échec contrôlé relève du contrat opérationnel de l’agent... »*
  - Page 53 (§ 4.2.3) : *« ReWOO (...) pousse le découplage plus loin en planifiant l’ensemble des appels d’outils avant d’observer leurs résultats, ce qui regroupe le raisonnement en un seul passage... »*
  - Page 58 (§ 4.4.1) : *« Les sorties structurées garantissent que l’argument respecte le schéma — typage, énumérations, champs requis —, ce qui transforme un problème de génération ouverte en un problème de remplissage contraint, plus vérifiable et plus robuste à l’analyse syntaxique. »*
  - Page 60 (§ 4.4.4) : *« La robustesse repose sur des mécanismes empruntés à l’ingénierie des systèmes distribués — le disjoncteur et le cloisonnement... auxquels s’ajoutent les réessais avec temporisation exponentielle... »*
- **Diagnostic causal approfondi** :
  1. *Absence de modélisation mathématique et effondrement super-exponentiel* :
     - *Modèle à fidélité constante par étape* : Soit une trajectoire agentique de $T$ étapes séquentielles. À chaque étape $t$, la fidélité unitaire dépend de quatre sous-processus stochastiques :
       $$p_t = p_{\text{plan}}(t) \cdot p_{\text{syntax}}(t) \cdot p_{\text{exec}}(t) \cdot p_{\text{obs\_int}}(t)$$
       Si la fidélité moyenne par étape est bornée par $p_t \le 1 - \epsilon$ avec $\epsilon > 0$, la probabilité de succès global décroît de façon géométrique :
       $$P(\text{Succès}_T) = \prod_{t=1}^T p_t \le (1 - \epsilon)^T \approx e^{-\epsilon T}$$
       Pour $T = 20$ étapes avec une fidélité unitaire de $95\%$ ($\epsilon = 0.05$), $P(\text{Succès}_{20}) = (0.95)^{20} \approx 35.8\%$. Pour $T = 50$, $P(\text{Succès}_{50}) \approx 7.7\%$.
     - *Modèle sous dilution d'attention (Attention Dilution / Context Rot)* : Dans une boucle ReAct réelle, l'accumulation de tours dégrade la transition correcte selon la longueur de l'historique : $p_t = p_0 (1 - \lambda)^t$ ($\lambda \in (0, 1)$). La probabilité de succès s'effondre alors selon une loi **super-exponentielle** :
       $$P(\text{Succès}_T) = \prod_{t=0}^{T-1} p_0 (1 - \lambda)^t = p_0^T \cdot (1 - \lambda)^{\frac{T(T-1)}{2}}$$
       Au-delà d'un horizon critique $T^* \approx \sqrt{\frac{2}{\lambda} \ln(1/p_0)}$, l'effondrement stochastique est quasi certain ($P \to 0$).
     - *Échec démontré de l'auto-correction verbale intrinsèque* : Des résultats empiriques récents (Huang et al., 2023, ICLR 2024 ; Stechly et al., 2024) démontrent que sans signal de vérité externe déterministe (oracle d'exécution, test unitaire formel), l'auto-correction verbale (*self-reflection*) dégrade la performance dans plus de 60 % des cas.
  2. *Confusion entre avortement sur dépassement et terminaison correcte* : Déclarer qu'un budget de pas ou un plafond de jetons constitue une « garantie de terminaison » confond l'avortement forcé sur expiration de délai (*timeout abort*) et la terminaison bien fondée de l'algorithme (*total correctness*). Lorsque le budget $K$ est atteint, la tâche est interrompue arbitrairement dans un état intermédiaire incohérent, laissant des effets de bord partiels non annulés.
  3. *Invalidité formelle de ReWOO en univers partiellement observable (POMDP)* : En page 49, le compendium qualifie l'environnement des agents de POMDP. Or, dans un POMDP, l'état $s_t$ n'est accessible qu'à travers une observation stochastique $o_t \sim O(s_t, a_t)$. Pré-planifier en boucle ouverte l'ensemble des appels d'outils (comme le fait ReWOO) n'est valide que si le graphe d'exécution est un DAG statique déterministe. Dès qu'un argument d'outil ou un branchement logique dépend du retour d'une API (solde bancaire, statut HTTP), ReWOO échoue mathématiquement.
  4. *L'illusion du décodage contraint (JSON Schema)* : L'affirmation p. 58 confond la validité grammaticale dans le langage formel $\mathcal{L}(\mathcal{G}_{\text{JSON}})$ et l'admissibilité sémantique dans l'espace d'états d'entreprise. Un appel d'outil JSON Schema valide peut contenir un montant négatif (`"amount": -500000.00`) ou des identifiants non autorisés, causant une défaillance métier majeure sans aucune infraction grammaticale.
- **Correctif formel explicite** :
  - Intégrer la dérivation mathématique de la fiabilité séquentielle supervisée par oracle déterministe :
    $$P(\text{Succès}_T) = \prod_{t=1}^T \left[ p_t + (1 - p_t) \cdot \mathbb{P}(\text{détection} \mid \text{erreur}) \cdot \mathbb{P}(\text{réparation} \mid \text{détection}) \right]$$
    démontrant que l'atteinte d'une fiabilité industrielle ($P \ge 0.99$) impose un oracle déterministe garantissant $\mathbb{P}(\text{détection}) = 1$.
  - Remplacer le budget passif par un **automate de surveillance externe déterministe (Safety Supervisor Automaton)** adossé au patron Saga : si le plafond $K$ est atteint, l'automate déclenche immédiatement les transactions compensatoires de rollback.
  - Restreindre formellement ReWOO aux tâches purement projectives à graphe statique sans branchement conditionnel.

---

### DEF-07 : Irréversibilité informationnelle de l'auto-compaction mémorielle (Shannon / Théorème du traitement de l'information), amnésie épistémique et pathologie de classement du RRF (Reciprocal Rank Fusion)

- **Localisation exacte** : Chapitre 5, § 5.1.2-5.1.3 (pp. 63-64), § 5.2.1-5.2.2 (pp. 65-66), § 5.3.2 (pp. 67-68).
- **Citations textuelles exactes du manuscrit** :
  - Page 63 (§ 5.1.2) : *« La perte au milieu (lost in the middle, Liu et coll., 2023) établit que l’information placée au centre d’un long contexte est nettement moins bien utilisée... La dégradation progressive de la qualité à mesure que la fenêtre se remplit (context rot) s’y ajoute. »*
  - Page 64 (§ 5.1.3) : *« L’enjeu de conception est la réversibilité. Une compaction agressive risque d’effacer un détail qui redeviendra pertinent ; une compaction trop prudente ne libère pas assez de budget. La bonne pratique consiste à compacter en conservant un pointeur vers la trace intégrale, déportée dans un magasin persistant, de sorte que le résumé reste augmentable à la demande sans peser sur la fenêtre courante. »*
  - Page 66 (§ 5.2.2) : *« Une mémoire mal gérée devient une source d’hallucinations : un agent qui rappelle un fait erroné avec aplomb propage l’erreur sur toute la trajectoire... la différence avec une hallucination ordinaire tiendrait à ce que l’hallucination mémorielle est persistante et auto-confirmante, l’agent relisant le souvenir erroné à la session suivante. »*
  - Page 67 (§ 5.3.2) : *« Les listes de résultats sont fusionnées par la fusion de rangs réciproques (Reciprocal Rank Fusion, RRF), qui combine les rangs sans recalibrer les scores, puis un réordonnanceur (...) affine le classement final sur un petit ensemble de candidats. »*
- **Diagnostic causal approfondi** :
  1. *Violation du Théorème de Traitement de l'Information et illusion de réversibilité* :
     - La génération successive de résumés d'historique forme une chaîne de Markov sur l'espace des contextes :
       $$H_0 \xrightarrow{f_1} S_1 \xrightarrow{f_2} S_2 \dots \xrightarrow{f_n} S_n$$
     - En vertu du Théorème de Traitement de l'Information (Cover & Thomas, 2006) :
       $$I(X; S_n) \le I(X; S_{n-1}) \le \dots \le I(X; H_0)$$
       où $X$ représente les variables critiques d'état (identifiants d'entités, clauses de mandats, montants de transactions).
     - Qualifier un résumé périodique par LLM de « compaction réversible » contredit la théorie de l'information : le résumé textuel $f : \mathcal{V}^N \to \mathcal{V}^M$ ($M \ll N$) est une compression avec perte irréversible ($H(X \mid f(X)) > 0$).
     - Préconiser de « conserver un pointeur vers la trace intégrale » est une solution illusoire : le modèle étant conditionné au pas suivant par le résumé $S_n$ (qui a effacé les détails négatifs et les contraintes discrètes), il ne dispose d'aucun signal d'attention pour déclencher la relecture du pointeur (*amnésie épistémique*).
  2. *Démonstration de la pathologie mathématique de classement du RRF (Reciprocal Rank Fusion)* :
     - La formule canonique du RRF (Cormack, Clarke & Büttcher, 2009) s'écrit :
       $$\text{RRF}(d) = \sum_{m \in \mathcal{M}} \frac{1}{k + r_m(d)}$$
       où $k$ est une constante de lissage empirique (généralement $k = 60$) et $r_m(d)$ est le rang du document $d$ selon le système $m$.
     - En écrasant l'amplitude des scores de confiance au profit des seuls rangs ordinaux, le RRF provoque des anomalies d'inversion de classement sévères.
     - *Démonstration numérique par contre-exemple* :
       Soient deux documents $d_1$ et $d_2$ évalués par un système dense (similarité cosinus) et un système lexical (BM25) avec $k = 60$ :
       - Document $d_1$ (document critique ciblé) : score de similarité cosinus dense $\sigma_{\text{dense}}(d_1) = 0.99$ (pertinence quasi absolue, rang $r_{\text{dense}} = 2$). En raison de l'absence de chevauchement lexical exact (termes synonymes), son rang lexical est $r_{\text{BM25}} = 60$.
         $$\text{RRF}(d_1) = \frac{1}{60 + 2} + \frac{1}{60 + 60} = \frac{1}{62} + \frac{1}{120} \approx 0.01613 + 0.00833 = 0.02446$$
       - Document $d_2$ (document médiocre contenant des mots-clés fréquents) : faible pertinence sémantique dense $\sigma_{\text{dense}}(d_2) = 0.45$ (rang $r_{\text{dense}} = 10$). Rang lexical $r_{\text{BM25}} = 10$.
         $$\text{RRF}(d_2) = \frac{1}{60 + 10} + \frac{1}{60 + 10} = \frac{1}{70} + \frac{1}{70} \approx 0.01428 + 0.01428 = 0.02857$$
       Le document médiocre $d_2$ surclasse le document critique $d_1$ ($\text{RRF}(d_2) > \text{RRF}(d_1)$), alors même que le détecteur dense indiquait une certitude sémantique extrême ($\sigma = 0.99$). Dans un contexte réglementé d'entreprise (audit bancaire, conformité juridique), cette pathologie élimine les preuves clés avant l'étape de réordonnancement.
- **Correctif formel explicite** :
  - Bannir le terme « compaction réversible » et structurer la mémoire de travail autour d'un magasin déterministe d'invariants (Key-Value Store immuable) exclu de toute compression statistique.
  - Imposer un système de maintien de la vérité basé sur les dépendances (Assumption-based Truth Maintenance System - ATMS, de Kleer, 1986 ; Doyle, 1979) : chaque fait consigné $F_i$ doit comporter un graphe de justification formel $J(F_i) = \langle \text{SourcesPrimaires}, \text{RèglesInférence}, \text{Timestamp}, \text{StatutValidité} \rangle$.
  - Remplacer le RRF par une fusion pondérée de scores étalonnés (normalisation z-score ou min-max) :
    $$\text{Score}_{\text{fusion}}(d) = \alpha \cdot \tilde{\sigma}_{\text{dense}}(d) + (1 - \alpha) \cdot \tilde{\sigma}_{\text{lexical}}(d)$$

---

## 4. Défauts Majeurs [Major]

### DEF-08 : Évasion théorique majeure : exclusion arbitraire du consensus distribué et de la coordination sous partition réseau en environnement financier (§ 1.6.2.2)

- **Localisation exacte** : Chapitre 1, § 1.6.2.2 (pp. 23-24).
- **Citation textuelle exacte du manuscrit** :
  - Page 23-24 : *« ...l’accord entre agents sous asynchronie et défaillance partielle — ce que deux agents tiennent pour vrai quand le réseau se partitionne — est en revanche hors du périmètre de la somme, et cela se dit ici plutôt que de se laisser découvrir. Ce périmètre est une décision d’auteur, prise le 27 juillet 2026 : assumé et déclaré. La somme ne traitera pas cette matière — ni ici, ni au ch. 6, ni au ch. 37, ni au ch. 48, les trois points d’atterrissage d’abord prévus étant fermés par la même décision. »*
- **Diagnostic causal approfondi** :
  Dans un compendium de 663 pages intitulé *Interopérabilité et Orchestration en Entreprise Agentique*, dont le sous-titre cible expressément les « services financiers réglementés (2024-2032) », déclarer que l'accord distribué sous partition réseau est hors périmètre constitue une dérobade théorique préjudiciable :
  1. *Nature distribuée asynchrone des réseaux d'agents financiers* : Lorsque des agents de compensation, d'exécution d'ordres ou de règlement (protocoles AP2, ISO 20022, Lynx) communiquent à travers des frontières organisationnelles, les partitions réseau, les congestions et les défaillances de nœuds sont inéluctables.
  2. *Théorèmes d'impossibilité de référence* : Le théorème CAP (Brewer, 2000 ; Gilbert & Lynch, 2002) et le théorème d'impossibilité FLP (Fischer, Lynch, Paterson, 1985) s'appliquent pleinement aux collectifs d'agents. Refuser de modéliser ce que deux agents tiennent pour vrai sous partition réseau fragilise l'ensemble des Livres III et V, qui prétendent bâtir une orchestration déterministe et une sémantique d'effet sans disposer d'un modèle d'accord formel sous défaillance.
- **Correctif formel et remédiation** :
  Réintégrer la théorie du consensus distribué dans l'architecture agentique : spécifier comment les protocoles de consensus déterministes (Raft, Paxos ou Byzantine Fault Tolerance BFT) s'articulent avec les patrons Saga et la réconciliation compensatoire asynchrone pour borner les fenêtres d'incohérence financière temporaire.

---

### DEF-09 : Angles morts du Zero Trust NIST SP 800-207 face aux plans multi-sauts, confusion d'identité SPIFFE vs mandat, inexactitude normative sur SAML 2.0 et omission de ReBAC

- **Localisation exacte** : Chapitre 3, § 3.2.1 (p. 38) et § 3.3.1 (pp. 40-41).
- **Citations textuelles exactes du manuscrit** :
  - Page 38 (§ 3.2.1) : *« (c) L’assertion transporte des attributs, non une autorisation : elle dit qui est le sujet et ce qu’on sait de lui ; ce que le sujet a le droit de faire reste une décision du consommateur. C’est le troisième trait qui voyage le plus loin dans la somme... »*
  - Page 40 (§ 3.3.1) : *« Le zero-trust formalise le principe ne jamais faire confiance, toujours vérifier en une architecture où aucune confiance n’est dérivée de la localisation réseau. L’architecture de référence NIST SP 800-207 en pose les composants — point de décision et point d’application de politique, évaluation continue par requête (...) SPIFFE et son implémentation de référence SPIRE fournissent à chaque charge un identifiant et un document d’identité vérifiable... »*
  - Page 41 (§ 3.3.1) : *« Lecture de l’auteur — c’est l’un des rares endroits de ce Livre où une classe entière d’incidents disparaît plutôt que de se déplacer. »*
- **Diagnostic causal approfondi** :
  1. *Évaluation par requête atomique inopérante face aux plans multi-étapes* : NIST SP 800-207 prescrit une vérification atomique par requête au niveau du PEP. Or, une attaque agentique par exfiltration se compose d'une suite d'actions individuellement licites :
     $$\pi = \langle a_1: \text{read\_public\_doc}(), a_2: \text{extract\_internal\_data}(), a_3: \text{call\_external\_api}() \rangle$$
     Si le PEP évalue chaque action de façon isolée sans corrélation causale avec le flux de données, chaque requête est validée avec succès.
  2. *Confusion entre identité de charge logicielle et mandat d'agent* : SPIFFE/SPIRE atteste l'intégrité de la charge logicielle hôte ($W_{\text{host}}$). Un conteneur d'agent est un interpréteur stochastique générique exécutant des requêtes pour de multiples mandants humains ($U_k$) sous des portées variables ($\text{Scope}_k$). Valider le SVID X.509 ne garantit aucunement que l'action s'inscrit dans le mandat consenti, rouvrant la brèche du mandataire confus. De plus, affirmer qu'avec SPIFFE « une classe entière d'incidents disparaît » est un sophisme : l'attaque se déplace vers le socket local de l'API Workload (`/tmp/spire-agent/public/api.sock`) ou la falsification des attesteurs de nœuds.
  3. *Inexactitude normative sur SAML 2.0* : La norme OASIS SAML 2.0 (Core Specification, Section 2.7) définit explicitement trois types d'assertions formelles : `AuthenticationStatement`, `AttributeStatement`, et `AuthzDecisionStatement`. Cette dernière transporte expressément une décision d'autorisation (`DecisionType` = Permit | Deny | Indeterminate) prise par un PDP. Affirmer que SAML ne transporte jamais d'autorisation est formellement erroné.
  4. *Omission du contrôle d'accès fondé sur les relations (ReBAC)* : Le chapitre restreint l'IAM à RBAC, ABAC et OAuth/OIDC, omettant ReBAC (Google Zanzibar, OpenFGA, Cedar), pourtant indispensable pour modéliser les graphes de délégation d'autorité entre agents autonomes.
- **Correctif formel explicite** :
  - Modéliser le PEP agentique sous forme d'automate de sécurité à états (Schneider, 2000) maintenant le suivi de contamination des flux (*taint tracking*) : $\mathcal{M}_{\text{PEP}} = \langle Q, \Sigma, \delta, q_0, F \rangle$.
  - Définir le jeton d'autorisation de l'agent comme une liaison cryptographique liant identité de charge, mandant et empreinte du mandat :
    $$\text{Token}_{\text{Auth}} = \text{Sign}_{\text{IdP}}\left( \text{spiffe\_id} \parallel \text{user\_sub} \parallel \text{mandate\_hash} \parallel \text{session\_nonce} \parallel \text{validity\_epoch} \right)$$
  - Rectifier la description de SAML 2.0 et introduire ReBAC comme socle relationnel des graphes de mandats.

---

### DEF-10 : Falsification du diagnostic d'échec de FIPA-ACL, omission des protocoles d'engagements sociaux décidables (Social Commitments), et réfutation de l'absence de force illocutoire dans MCP/A2A

- **Localisation exacte** : Chapitre 4, § 4.1.3 (p. 49) ; Chapitre 6, § 6.2 et § 6.2.1 (pp. 72-73) ; Chapitre 7, § 7.2.1 (pp. 81-82).
- **Citations textuelles exactes du manuscrit** :
  - Page 73 (§ 6.2.1) : *« Communiquer suppose trois accords, et les protocoles agentiques n’en portent qu’un... (c) Un accord sur la force illocutoire — ce que l’émetteur fait en émettant : demande-t-il, informe-t-il, s’engage-t-il, refuse-t-il, propose-t-il ? C’est celui-là qui manque. Le contraste avec l’héritage multi-agents classique est net... KQML... puis FIPA-ACL... avaient fait de la force illocutoire un champ obligatoire du message... Les protocoles agentiques de 2025-2026 ne portent pas cette information : un message y transporte une charge utile typée dont l’intention se déduit du contenu, c’est-à-dire du langage naturel, c’est-à-dire du modèle. »*
- **Diagnostic causal approfondi** :
  1. *Cause réelle de l'échec industriel de FIPA-ACL* : L'auteur note avec réserve que le socle ne documente pas les motifs du déclin de FIPA-ACL. Or, la recherche en systèmes multi-agents a formellement documenté cette cause (Singh, 1998, 2000 ; Wooldridge, 2002) : la sémantique de FIPA-ACL était fondée sur des états mentaux internes inobservables (logique BDI de Cohen et Levesque), exigeant qu'un agent vérifie la « sincérité » de l'émetteur. Il était impossible pour un vérificateur tiers ou un tribunal d'auditer la conformité d'un agent sans accéder à ses états cognitifs privés. À cela s'ajoutaient des obstacles d'ingénierie rédhibitoires : la syntaxe verbeuse en S-expressions LISP, la dépendance à des couches middleware complexes (CORBA IIOP) et l'absence de sécurité au niveau transport.
  2. *Omission de la théorie moderne des engagements sociaux (Social Commitments)* : Le dépassement de FIPA-ACL a consisté à formaliser les **engagements sociaux** (Singh, 2000 ; Fornara & Colombetti, 2004) sous forme d'engagements conditionnels auditables :
     $$C(\text{débiteur}, \text{créancier}, \text{antécédent}, \text{conséquent})$$
     Les transitions d'état de l'engagement (Créé, Actif, Rempli, Violé, Annulé) sont calculables par des automates d'états finis déterministes à partir des messages publics échangés, sans spéculer sur la psychologie interne de l'agent.
  3. *Contradiction factuelle sur l'absence de force illocutoire dans MCP et A2A* : Prétendre que la force illocutoire est totalement absente des protocoles agentiques récents est inexact :
     - Dans MCP, les méthodes JSON-RPC encodent formellement les actes de langage de Searle : `tools/call` est une directive impérative d'action ; `resources/read` est une assertion interrogative d'état ; `notifications` est une assertion déclarative unilatérale sans réponse.
     - Dans A2A, les transitions de l'enveloppe de tâche (`tasks/send`, `tasks/update`, `tasks/cancel`) encadrent explicitement l'intention pragmatique de négociation contractuelle.
- **Correctif formel explicite** :
  - Compléter la rétrospective sur FIPA-ACL en articulant l'obstacle sémantique mentaliste avec les facteurs matériels de rejet logiciel (CORBA, LISP, absence d'APIs Web).
  - Prescrire formellement une couche d'engagements sociaux décidables adossée à A2A pour garantir l'opposabilité juridique des transactions inter-agents.
  - Rectifier la présentation de MCP et A2A en démontrant comment leurs méthodes portent nativement la qualification illocutoire.

---

### DEF-11 : Conflit logique formel entre la monotonicité d'OWL 2 DL et le non-déterminisme des flux d'agents (explosion déductive *ex falso quodlibet*)

- **Localisation exacte** : Chapitre 2, § 2.3.1 et § 2.3.3 (pp. 31-32), § 2.4.1 (p. 34).
- **Citations textuelles exactes du manuscrit** :
  - Page 32 (§ 2.3.3) : *« OWL sert l’inférence sous hypothèse de monde ouvert — déduire des faits implicites ; SHACL sert la validation sous hypothèse de monde clos — constater qu’un fait requis manque... »*
  - Page 34 (§ 2.4.1) : *« La gouvernance du sens en environnement distribué impose donc de traiter la sortie du modèle comme une proposition soumise à validation — par SHACL (§ 2.3.3), par revue experte, par confrontation aux axiomes ontologiques — et non comme un contrat établi. »*
- **Diagnostic causal approfondi** :
  Le compendium recommande d'adosser l'interopérabilité sémantique des agents à OWL 2 et SHACL, mais ignore une incompatibilité logique fondamentale :
  1. *Monotonicité stricte d'OWL 2 DL* : Dans OWL 2 DL (fondé sur la logique de description $\mathcal{SROIQ}(\mathcal{D})$), le raisonnement déductif est strictement monotone : l'adjonction d'un nouvel axiome ne peut en aucun cas invalider une conclusion précédemment démontrée.
  2. *Nature non-monotone de la délibération agentique* : Un agent autonome opérant dans un environnement dynamique procède par hypothèses révisables et raisonnement par défaut (Reiter, 1980 ; AGM Belief Revision, 1985). Si un agent insère dans le triplestore OWL un fait provisoire $\alpha$, puis découvre par retour d'outil que $\neg \alpha$ est vrai, la base de connaissances devient logiquement inconsistante ($\mathcal{K} \models \bot$). En logique classique, une base inconsistante engendre une explosion déductive (*ex falso quodlibet* ou principe de pseudo-scotus), permettant de déduire n'importe quelle proposition fausse et paralysant tous les raisonneurs sémantiques.
- **Correctif formel explicite** :
  Restreindre strictement l'usage d'OWL 2 DL aux vocabulaires terminologiques invariants (TBox stables). Interdire l'écriture directe d'assertions conjoncturelles d'agents dans l'ABox OWL sans passer par une couche de réconciliation fondée sur des logiques non monotones (Answer Set Programming - ASP ou Datalog avec négation stratifiée).

---

### DEF-12 : Absence de valeur probatoire et de non-répudiation des traces OpenTelemetry et W3C Trace Context pour l'auditabilité financière réglementaire

- **Localisation exacte** : Chapitre 3, § 3.4.5 et § 3.4.6 (pp. 44-45).
- **Citation textuelle exacte du manuscrit** :
  - Page 45 (§ 3.4.6) : *« L’observabilité ne sert pas que le diagnostic : elle fonde l’auditabilité, c’est-à-dire la capacité à démontrer après coup, preuves à l’appui, comment une intégration s’est comportée... Dans la banque ouverte... l’auditabilité des appels y est une condition de conformité, non un agrément. »*
- **Diagnostic causal approfondi** :
  Le texte affirme que la pile OpenTelemetry (spans distribués et W3C Trace Context) constitue le socle de l'auditabilité réglementaire. Il s'agit d'une confusion critique entre métrologie opérationnelle et preuve juridique :
  - Les spans OpenTelemetry sont conçus pour la surveillance des performances (APM) et le débogage. Ils transitent sur le réseau via des protocoles sans signature cryptographique (OTLP sur gRPC/HTTP) et sont stockés dans des bases de données de séries temporelles (Tempo, Jaeger, Elasticsearch) modifiables par les administrateurs système.
  - En droit bancaire et financier (notamment sous les lignes directrices BSIF E-23, Sarbanes-Oxley § 404 et l'article 12.1 de la Loi 25 québécoise), une trace d'audit requiert des garanties formelles de **non-répudiation, d'intégrité temporelle et d'immutabilité**. Une trace OpenTelemetry brute n'a aucune valeur probatoire devant une autorité de contrôle ou un tribunal, car elle peut être altérée ou purgée a posteriori sans rupture d'intégrité cryptographique.
- **Correctif formel explicite** :
  Établir une distinction étanche entre *télémétrie opérationnelle non opposable* (OTel) et *journalisation d'audit probatoire opposable*. Exiger que chaque transition d'état et appel d'outil contractuel émette un enregistrement scellé :
  $$\text{AuditEntry} = \text{Sign}_{K_{\text{Agent}}}(\text{TraceID} \parallel \text{Timestamp} \parallel \text{ContextHash} \parallel \text{Decision} \parallel \text{ToolArguments})$$
  consigné dans un registre immuable à arbre de Merkle (*Append-Only Log* certifié RFC 6962 / RFC 9162).

---

### DEF-13 : Omission des topologies d'essaim (Swarm), de tableau noir et de marché, et duplications verbatim systématiques entre tableaux et figures

- **Localisation exacte** : Chapitre 6, § 6.1.2 (pp. 71-72), Tableau 6.1 et Figure 6.1 ; Chapitre 5, § 5.0 (pp. 61-62), Tableau 5.1 et Figure 5.0 ; Chapitre 6, § 6.4.2 (p. 76), Tableau 6.2 et Figure 6.4.
- **Citations textuelles exactes du manuscrit** :
  - Tableau 6.1 (p. 71) et Figure 6.1 (p. 72) : Liste strictement identique : Étoile (*« Un orchestrateur délègue à des travailleurs »*), Chaîne (*« La sortie d'un agent est l'entrée du suivant »*), Arbre (*« Délégation hiérarchique »*), Graphe (*« Interactions arbitraires »*).
  - Tableau 6.2 (p. 76) et Figure 6.4 (p. 76) : Reproduction verbatim des mêmes définitions de $pass@k$ et $pass^k$ sur la même page.
- **Diagnostic causal approfondi** :
  1. *Omission de topologies canoniques de coordination multi-agents* : Le plan d'audit du socle (Review Plan S07) et la table des matières annoncent l'étude des topologies de marché et d'essaim. Or, dans le corps du texte (pp. 71-72), la taxonomie se restreint arbitrairement à quatre structures statiques de graphes (Étoile, Chaîne, Arbre, Graphe). Les architectures de coordination par **stigmergie / essaim** (OpenAI Swarm, espaces de tuples de Gelernter) et les architectures de **marché** (enchères de Vickrey, allocation par prix d'équilibre, Contract Net Protocol étendu) sont complètement ignorées.
  2. *Duplications verbatim systématiques* :
     - Le Tableau 6.1 et la Figure 6.1 répètent mot pour mot les quatre mêmes définitions sans qu'aucun diagramme visuel d'architecture ne vienne justifier la présence de la figure.
     - Un doublon identique apparaît entre le Tableau 5.1 (p. 61) et la Figure 5.0 (p. 62) sur le triptyque Mémoire / RAG / Protocole.
     - Au § 6.4.2 (p. 76), le Tableau 6.2 et la Figure 6.4 coexistent sur la même page en répétant verbatim les mêmes définitions. Cette pratique gonfle artificiellement le volume du manuscrit tout en appauvrissant l'analyse technique.
- **Correctif formel explicite** :
  Compléter la typologie des coordinations par l'ajout formel de l'Essaim (*Swarm* / coordination stigmergique sur espace de tuples) et du Marché (*Market-based dynamic bidding*). Remplacer les figures textuelles redondantes par de véritables schémas conceptuels de flux d'information.

---

### DEF-14 : Chimère bibliographique et fausse attribution sur Plan-and-Solve Prompting (§ 4.2.3, p. 53)

- **Localisation exacte** : Chapitre 4, § 4.2.3 (Page 53).
- **Citation textuelle exacte du manuscrit** :
  - Page 53 : *« Plan-and-Solve (Wang, Wei, Schuurmans et coll., 2023) sépare explicitement la planification de l’exécution : une invite demande d’abord de décomposer le problème en sous-tâches ordonnées, puis d’exécuter chaque sous-tâche — Wang, Xu, Lan et coll. (2023), Plan-and-Solve Prompting, arXiv:2305.04091. »*
- **Diagnostic causal approfondi** :
  Ce passage comporte une contradiction interne immédiate et une fausse attribution d'article scientifique au sein de la même phrase :
  - L'article fondateur de Plan-and-Solve Prompting (ACL 2023, arXiv:2305.04091) est intitulé *Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models*, rédigé par **Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee et Ee-Peng Lim**.
  - Les chercheurs Jason Wei et Dale Schuurmans (avec Xuezhi Wang) sont les auteurs de *Self-Consistency Improves Chain of Thought Reasoning in Language Models* (ICLR 2023 / arXiv:2203.11171), cité plus loin p. 55.
  - L'auteur a confondu les équipes de recherche en attribuant d'abord Plan-and-Solve à « Wang, Wei, Schuurmans et coll. (2023) », avant de citer correctement « Wang, Xu, Lan et coll. (2023) » quelques mots plus loin dans la même phrase ! Cette chimère bibliographique traduit une contamination de notes de lecture non révisées.
- **Correctif formel explicite** :
  Rectifier le début de la phrase à la page 53 en supprimant la fausse attribution : remplacer « *Plan-and-Solve (Wang, Wei, Schuurmans et coll., 2023)* » par « *Plan-and-Solve (Wang, Xu, Lan et coll., 2023)* ».

---

### DEF-15 : Sous-spécification des canaux d'exfiltration pour CodeAct et des attaques adversariales multimodales pour Computer Use

- **Localisation exacte** : Chapitre 4, § 4.2.3 (p. 53), § 4.4.3 (pp. 59-60).
- **Citations textuelles exactes du manuscrit** :
  - Page 53 (§ 4.2.3) : *« L’action comme code exécutable — CodeAct... exécuter du code généré par un modèle exige un environnement confiné, faute de quoi l’agent dispose d’une capacité d’action quasi illimitée sur le système hôte. »*
  - Page 59 (§ 4.4.3) : *« L’exécution de code est l’outil universel le plus puissant... Le confinement est ici une mesure de sécurité non négociable... »*
  - Page 60 (§ 4.4.3) : *« Le pilotage d’interface... Le choix entre structure et vision est ainsi autant une décision de surface d’attaque qu’une décision de robustesse... »*
- **Diagnostic causal approfondi** :
  L'auteur prescrit le « confinement » sans caractériser la surface d'attaque spécifique aux LLMs :
  1. *Canaux cachés et exfiltration sous CodeAct* : Un code Python généré dans un bac à sable conteneurisé standard sans privilèges root conserve l'accès aux appels réseau si la tâche requiert des requêtes externes. Un modèle subverti peut exfiltrer des variables d'environnement, des clés d'API ou des données de contexte par requêtes DNS asynchrones, par stéganographie dans les en-têtes HTTP ou via des canaux auxiliaires temporels (*timing attacks*).
  2. *Vulnérabilités adversariales multimodales dans Computer Use* : Dans le pilotage par vision (captures d'écran), l'agent est vulnérable aux attaques par injection visuelle indirecte (*adversarial visual patches*, typoglyphie invisible à faible opacité ou perturbations imperceptibles de pixels). Une image affichée à l'écran peut forcer le modèle de vision à cliquer sur des coordonnées hostiles ou à interpréter des instructions malveillantes dissimulées dans l'arrière-plan graphique. Traiter la vision comme un simple compromis de coût par rapport au DOM est une sous-estimation substantielle du vecteur d'attaque multimodal.
- **Correctif formel explicite** :
  - Pour CodeAct : imposer une isolation par MicroVM (type Firecracker ou gVisor) avec interdiction stricte de sortie réseau directe (*Air-Gapped Sandbox*), tout appel externe devant obligatoirement transiter par un proxy mandataire d'inspection L7 à schéma validé.
  - Pour Computer Use : prescrire un assainisseur visuel (*Visual Pre-Processing Defense*) et la validation croisée déterministe de l'arbre d'accessibilité DOM avant toute exécution d'action périphérique (clic ou saisie clavier).

---

## 5. Section R3 : Vérification Bibliographique Exhaustive & État de l'Art 2024-2026

L'audit contradictoire a procédé à la vérification systématique de l'ensemble des références bibliographiques, citations d'articles scientifiques, normes industrielles (RFC, W3C, OASIS, ISO, NIST) et dates de parution mentionnées dans les pages 1 à 79 du manuscrit, confrontées aux bases de données officielles (arXiv, DBLP, ACM, IEEE, IETF Datatracker, W3C Technical Reports).

| Référence citée / Norme | Localisation | Citation dans le Manuscrit | Statut de Vérification Factuelle | Diagnostic de Conformité & Rectification Opposable |
| :--- | :--- | :--- | :---: | :--- |
| **Plan-and-Solve Prompting** | Ch. 4, p. 53 (§ 4.2.3) | « Plan-and-Solve (Wang, Wei, Schuurmans et coll., 2023) ... Wang, Xu, Lan et coll. (2023), arXiv:2305.04091 » | **ERRONÉ (Chimère)** | Attribution croisée erronée. Les auteurs réels sont Lei Wang, Wanyu Xu, Yihuai Lan et coll. (ACL 2023). Wei et Schuurmans sont les auteurs de *Self-Consistency* (ICLR 2023). Remplacer la première citation par Wang, Xu, Lan et coll. |
| **SAML 2.0 Core Spec** | Ch. 3, p. 38 (§ 3.2.1) | « L’assertion transporte des attributs, non une autorisation... » | **ERRONÉ (Normatif)** | La spécification OASIS SAML 2.0 définit formellement `AuthzDecisionStatement` à la Section 2.7. Corriger l'affirmation en précisant que l'autorisation est portée par cette déclaration bien que peu employée en SSO web. |
| **$\tau$-bench (Tau-Bench)** | Ch. 6, p. 76 (§ 6.4.2) | « pass^k, introduite par τ-bench (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues... » | **DÉTOURNÉ (Métrique)** | Yao et al. (arXiv:2406.12045) définissent $pass^k = \mathbb{E}[p^k]$ comme la consistance sur $k$ essais indépendants de la tâche complète, et non sur une séquence temporelle intra-trajectoire multi-étapes. |
| **pass@k Unbiased Estimator** | Ch. 6, p. 76 (Tableau 6.2) | « pass@k : la probabilité qu’au moins une parmi k tentatives réussisse » | **INCOMPLET (Métrique)** | Chen et al. (HumanEval, 2021) démontrent que la formule naïve $1-(1-p)^k$ est biaisée. L'estimateur sans biais canonique est $\text{pass@k} = \mathbb{E}\left[ 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}} \right]$. |
| **RFC 8693 (Token Exchange)** | Ch. 3, p. 39 (§ 3.2.3) | « OAuth 2.0 Token Exchange (RFC 8693)... » | **VALIDE** | Cité correctement pour la délégation linéaire, mais ses limites de performance dans les topologies décentralisées doivent être signalées (absence d'atténuation hors-ligne type Macaroons/Biscuit). |
| **NIST SP 800-207** | Ch. 3, p. 40 (§ 3.3.1) | « L’architecture de référence NIST SP 800-207 en pose les composants... » | **INCOMPLET (Contexte)** | Cité fidèlement pour l'architecture Zero Trust, mais son incapacité à traiter l'injection sémantique sans suivi de teinte (IFC) doit être expressément soulignée. |
| **LCIM (Tolk & Muguira)** | Ch. 1, p. 9 ; Ch. 7, p. 80 | « Les cinq niveaux du LCIM... » (p. 80) vs « échelle à sept niveaux » (p. 9) | **CONTRADICTOIRE** | Tolk & Muguira (2003) et Wang, Tolk & Wang (2009) ont formellement standardisé 7 niveaux ($L_0$ à $L_6$). Le Tableau 7.1 ampute sans justification le niveau 6 Conceptuel. Rétablir les 7 niveaux. |
| **Lost in the Middle** | Ch. 5, p. 63 (§ 5.1.2) | « Liu et coll., 2023 » (arXiv:2307.03172 / TACL 2024) | **VALIDE** | Phénomène de dégradation au centre de la fenêtre d'attention correctement attribué à Nelson F. Liu et al. (Stanford/Berkeley). |
| **Reciprocal Rank Fusion** | Ch. 5, p. 67 (§ 5.3.2) | « fusion de rangs réciproques (Reciprocal Rank Fusion, RRF)... » | **INCOMPLET (Pathologie)** | Cormack, Clarke & Büttcher (SIGIR 2009). La pathologie mathématique d'inversion des rangs en présence de scores denses à haute confiance doit être documentée. |
| **GAV / LAV / GLAV** | Ch. 2, p. 33 (§ 2.3.4) | « Le formalisme distingue ici deux régimes de correspondance : GAV ... LAV ... » | **OBSOLÈTE (Théorie)** | Présentation réductrice omettant GLAV (Friedman, Levy, Millstein, 1999) et BAV (McBrien & Poulovassilis, 2003) qui dominent la littérature de médiation sémantique depuis 2002. |
| **OWL 2 / SHACL** | Ch. 2, pp. 31-34 | « OWL sert l’inférence... SHACL sert la validation... » | **INAPPLICABLE (Runtime)** | La complexité 2NEXPTIME d'OWL 2 DL ($\mathcal{SROIQ}(\mathcal{D})$) et la validation par lot de SHACL sont inadaptées aux boucles agents temps réel. Prescrire OWL 2 QL/EL et décodage contraint par grammaires. |
| **FIPA-ACL vs Engagements** | Ch. 6, p. 73 ; Ch. 7, p. 81 | « FIPA-ACL... sémantique mentaliste... » | **RÉDUCTEUR (Histoire)** | Attribue l'échec de FIPA à la seule sémantique mentaliste en omettant les causes logicielles déterminantes (CORBA IIOP, S-expressions LISP, absence d'APIs Web). Omet la théorie des engagements sociaux (Singh, 2000). |
| **Distinction Flux vs Agent** | Ch. 4, p. 48 (§ 4.1.1) | « Anthropic (2024), Building effective agents » | **BIAIS DE SOURCE** | Anthropic a popularisé la distinction fin 2024, mais la dichotomie flux déterministes vs boucles autonomes était déjà formalisée dès 2023 dans AutoGen (Wu et al.) et LangGraph. |
| **Gel au 27 juillet 2026** | Liminaires vs pp. 11, 72, 76 | « Faits gelés au 27 juillet 2026 » vs actualisations 28 juil., 30 juil., 23 oct. 2026 | **INCOHÉRENCE INTERNE** | Les mentions explicites de dates postérieures au 27 juillet 2026 dans le corps du texte violent la doctrine déclarée en page de garde. Harmoniser ou basculer en Annexe N. |

---

## 6. Recommandations Architecturales Directrices pour la Suite de l'Ouvrage (Livres II à V)

Pour préserver la rigueur scientifique de l'ouvrage et garantir l'opposabilité de son cadre architectural dans les déploiements financiers réglementés (2024-2032), les recommandations suivantes doivent être intégrées dans les tomes ultérieurs :

1. **Refonte de la théorie du couplage dans le Livre II (Protocoles Agentiques MCP & A2A)** :
   - Abandonner l'allégation selon laquelle MCP « élimine le couplage de format » : acter formellement que MCP remplace le couplage de code par un **couplage de schéma rigide JSON Schema** et un **couplage d'interaction synchrone RPC**.
   - Structurer le dialogue inter-agents autour d'une couche d'**engagements sociaux vérifiables (Social Commitments)** adossée aux enveloppes A2A, permettant l'auditabilité déterministe des obligations contractuelles sans dépendre de l'interprétation probabiliste du LLM.
2. **Élévation du modèle de sécurité dans le Livre III (Identité, Autorité et Gouvernance)** :
   - Compléter l'architecture Zero Trust (NIST SP 800-207 / SPIFFE) par un moteur de **Contrôle des Flux d'Information (Information Flow Control - IFC)** capable de maintenir un graphe de teinte (*taint graph*) sur les données absorbées dans la fenêtre d'attention.
   - Substituer aux flux linéaires de RFC 8693 des mécanismes de délégation cryptographique atténuables localement et vérifiables hors-ligne (**jetons Biscuit / UCAN** fondés sur Datalog).
   - Introduire **ReBAC (Relationship-Based Access Control)** pour modéliser les graphes d'autorité multi-mandats.
3. **Formalisation de la robustesse dans le Livre IV (Orchestration et Mémoire)** :
   - Rejeter la notion d'« auto-compaction réversible » de contexte. Prescrire une architecture à **mémoire duale** : un registre déterministe d'invariants métier immuables (Key-Value Constraint Store) combiné à un système de maintien de la vérité basé sur les dépendances (ATMS).
   - Remplacer le RRF par une fusion de scores étalonnés (z-score) pour éliminer les inversions aberrantes de pertinence documentaire.
   - Encadrer les boucles délibératives (ReAct) par des **automates de surveillance d'état finis (Safety Automata)** couplés au patron Saga, garantissant le rollback automatique en cas d'avortement sur budget de pas.
4. **Intégration du consensus distribué dans le Livre V (Sémantique d'Effet et Résilience Financière)** :
   - Révoquer la clause d'exclusion du § 1.6.2.2 : formaliser explicitement le comportement des réseaux d'agents sous asynchronie et partition réseau (théorèmes FLP et CAP), en articulant les protocoles de consensus déterministes (Raft / BFT) avec la réconciliation financière asynchrone (ISO 20022 / Lynx).
   - Imposer la journalisation probatoire opposable sur **registres immuables à arbres de Merkle** (RFC 6962 / RFC 9162) pour satisfaire aux exigences des lignes directrices prudentielles BSIF E-23 et de la Loi 25 québécoise.

---

# Minor Corrections and Typos

1. **Chapitre 2, Page 32 (§ 2.3.3, Lignes 7-13 / Lignes 2526-2536)** : Collision matérielle et inversion de paragraphe lors de la mise en page :
   - *Texte actuel* : « Ces travaux ne sont pas cités comme acquis : leur ancre de version se fixe au moment de citer, et cette réserve est reconduite ici sans être levée. intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. Un graphe RDF est, par construction, ouvert et sans schéma : tout triplet est licite, l’absence d’information n’est pas une faute, et rien n’interdit a priori d’attribuer une date de naissance à une facture. Pour l’intégration, cette permissivité est SHACL remplit ce rôle... »
   - *Diagnostic causal* : La proposition « intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API. » a été accidentellement coupée de la fin du second paragraphe et collée à la fin du premier paragraphe. Le second paragraphe reste suspendu sur l'auxiliaire « est ».
   - *Correction textuelle prête à l'application* : Rétablir la syntaxe exacte :
     « ...et cette réserve est reconduite ici sans être levée. »
     « Un graphe RDF est, par construction, ouvert et sans schéma : tout triplet est licite, l’absence d’information n’est pas une faute, et rien n’interdit a priori d’attribuer une date de naissance à une facture. Pour l’intégration, cette permissivité est **intenable ; il faut un pendant sémantique aux schémas qui gardent les frontières des API.** »
     « **SHACL** remplit ce rôle... »

2. **Chapitre 7, Page 79 (§ 7.0, Lignes 6500-6508 / Lignes 3487-3492)** : Collision éditoriale entre l'encadré Thèse et le corps du second paragraphe :
   - *Texte actuel* : Dans l'encadré Thèse : « ...fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres. » et dans le second paragraphe : « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses [saut de paragraphe] La proposition directrice tient en un déplacement... »
   - *Diagnostic causal* : Le membre de phrase du second paragraphe a été coupé et collé par inadvertance à l'intérieur de l'encadré Thèse immédiatement après « instruit au ch. 10. ». Le second paragraphe reste suspendu sur le possessif « ses ».
   - *Correction textuelle prête à l'application* : Supprimer le fragment intrus dans l'encadré Thèse après « instruit au ch. 10. » et le rétablir dans le second paragraphe :
     « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses **outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.** »

3. **Chapitre 1, Page 11 (§ 1.1.4.1, Lignes 681-683)** : Ponctuation manquante en fin de phrase :
   - *Texte actuel* : « ...quel que soit le soin apporté aux deux premiers Le point est repris au ch. 7... »
   - *Correction* : Insérer le point final manquant : « ...aux deux premiers**.** Le point est repris au ch. 7... »

4. **Chapitre 4, Page 47 (§ 4.0.2, Lignes 2029-2030 / Lignes 3774-3776)** : Troncation de mot en bas de page :
   - *Texte actuel* : « ...l’agent rationnel, l’héritage des architectures délibé » (ou coupure de césure non restituée).
   - *Correction* : Rétablir le mot complet sans coupure : « ...l’héritage des architectures **délibératives**... ».

5. **Chapitre 6, Page 75 (§ 6.3.3)** : Ponctuation manquante et fusion de titre dans le corps de texte :
   - *Texte actuel* : « ...sans encore le rejoindre Des annonces d’éditeurs revendiquent depuis... Raisonnement général, outils et tâches d’entreprise. Une seconde famille évalue... »
   - *Correction* : Insérer un point après « rejoindre**.** » et formater « Raisonnement général, outils et tâches d’entreprise » en titre de sous-section distinct du paragraphe.

6. **Chapitre 2, Page 25 (§ 2.1.1)** : Troncation du numéro de page dans le pied de page :
   - *Texte actuel* : « Gel au 27 juillet 2026 · actualisation du 1er novembre 2026 Page 25 s »
   - *Correction* : Rétablir « Page 25 **sur 663** ».

7. **Chapitre 2, Page 27 (Tableau 2.1)** : Classification de la compatibilité de schéma :
   - *Texte actuel* : Classement de « Transitive » comme 4e modalité disjointe au même rang que Backward, Forward, Full.
   - *Correction* : Clarifier que la transitivité est un modificateur d'orthogonalité temporelle (Pairwise vs Transitive) applicable à chacun des trois régimes, et non une modalité mutuellement exclusive.

8. **Liminaires & Ch. 1, Ch. 6 (pp. 1, 10-11, 72, 76)** : Incohérence interne de la doctrine de gel documentaire :
   - *Observation* : L'ouvrage stipule solennellement que les faits doctrinaux sont gelés au 27 juillet 2026 et que seules les annexes intègrent les actualisations postérieures. Or, le corps du texte intègre directement des actualisations datées du 28 juillet, 30 juillet et 23 octobre 2026 (pp. 11, 72, 76).
   - *Correction* : Basculer ces actualisations en notes de bas de page renvoyant à l'Annexe N ou harmoniser la mention liminaire pour acter que le Livre I a été révisé jusqu'au 24 octobre 2026.

9. **Ensemble des chapitres 1 à 6** : Numérotation discontinue et non standardisée des figures :
   - *Observation* : Les figures sont indicées d'après la sous-section hôte (Fig. 1.0, 1.1, 1.3, 1.5 ; Fig. 2.1, 2.3 ; Fig. 5.0, 5.3 ; Fig. 6.1, 6.4) plutôt que séquentiellement dans le chapitre, créant une fausse impression de figures manquantes (ex. absence apparente de Fig. 1.2, Fig. 1.4, Fig. 6.2, Fig. 6.3).
   - *Correction* : Adopter la numérotation séquentielle standardisée (Figure 1.1, Figure 1.2, Figure 1.3, etc.).
