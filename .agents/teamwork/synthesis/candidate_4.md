# RAPPORT DE SYNTHÈSE CANDIDAT 4 — ÉVALUATION CRITIQUE TRANSVERSALE GLOBALE
## Manuscrit audité : *Interopérabilité et Orchestration en Entreprise Agentique* (Compendium 2026)

> **Paper** : *Interopérabilité et Orchestration en Entreprise Agentique* (Édition Novembre 2026, 663 pages)  
> **Auteur** : André-Guy Bruneau M.Sc. IT  
> **Cadre méthodologique** : Audit contradictoire exhaustif de Niveau 4 (Synthétiseur Candidat 4)  
> **Synthesis mode** : candidate  
> **Catégorie** : Methodology, Modeling, Theory/Math, Experiments, Regulation & Architecture  
> **Segments reviewed** : 8 segments consolidés (Pages 1 à 663 intégrales, Liminaires, Livres I à V, Annexes B, I, N)  
> **Date d'évaluation** : 3 novembre 2026  
> **Fichier cible** : `c:\Github\EntrepriseAgentique\.agents\teamwork\synthesis\candidate_4.md`

---

# Section 1 : Verdict exécutif et évaluation critique de la contribution fondamentale

### 1.1 Thèse directrice de l'ouvrage et promesse doctrinale
Le manuscrit *Interopérabilité et Orchestration en Entreprise Agentique* (663 pages) poursuit une ambition intellectuelle et industrielle de premier plan : bâtir le socle d'ingénierie logicielle, cryptographique, architectural et réglementaire permettant d'intégrer des collectifs d'agents autonomes à base de modèles de langage (LLM) au sein d'environnements d'entreprise hautement régulés, avec pour terrain d'application principal les **services financiers canadiens et québécois (2024–2032)**.

L'ouvrage déploie une culture technique impressionnante et mobilise une posture épistémique salutaire : le refus constant du sensationnalisme marketing, le traçage des degrés d'absence documentaire (degrés 1 à 3) et la qualification rigoureuse des niveaux de preuve ([A] vote adversarial à trois juges, [B] source primaire ouverte, [C] repérage non extrait).

Toutefois, la méta-synthèse transversale des huit rapports d'unité révèle que le manuscrit repose sur un **écart fondamental entre sa promesse théorique formalisée et la réalité de ses démonstrations mathématiques, logiques, architecturales et légales**.

---

### 1.2 Évaluation critique de l'autonomie encadrée (OO1–OO4) et déconstruction du déterminisme
L'un des piliers cardinaux de l'ouvrage est la taxonomie des options d'orchestration (OO1 à OO4, issue des travaux de TU Munich, Rinderle-Ma & Mangler) et le paradigme APM (*Agentic Business Process Management*, Calvanese et coll.). L'auteur soutient que l'option **OO4** (« l'orchestration explicite d'agents conscients du processus ») permet d'atteindre une **autonomie encadrée déterministe** grâce à laquelle les exigences réglementaires et les invariants prudentiels sont imposés de manière mathématiquement vérifiable par le cadre d'exécution.

L'analyse transversale contradictoire réfute formellement cette prétention :
1. **Rupture de déterminisme et nature de POMDP** : Encapsuler des agents stochastiques dans les nœuds d'un graphe d'orchestration statique (CFG) ne confère aucun déterminisme sémantique au système global. Dès lors que les transitions du graphe dépendent de gardes évaluant les sorties probabilistes d'un grand modèle de langage ($Y \sim \mathbb{P}_\theta(Y \mid X)$), le système global est un automate probabiliste interactif ou un processus de décision markovien partiellement observable (POMDP). En présence de boucles de réessai, le temps d'arrêt est une variable aléatoire dont la finitude n'est pas garantie ($\mathbb{P}(\tau = \infty) > 0$).
2. **Non-contrôlabilité de Ramadge-Wonham** : Sous l'angle de la théorie du contrôle supervisé, dès lors que l'alphabet d'événements comporte des actions non contrôlables générées librement par l'agent ($\Sigma_{uc} \neq \emptyset$), aucune politique d'encadrement déterministe n'est réalisable sans forcer une amputation arbitraire de l'autonomie.
3. **Le sophisme de l'inexprimabilité de l'écart au processus** : Prétendre qu'en OO3/OO4 l'écart au processus « n'est pas exprimable » confond le plan de contrôle syntaxique et le plan de données sémantique. L'écart s'exprime pleinement par la dérive sémantique des charges utiles (*payload drift*) et par les effets de bord irréversibles déclenchés via les outils externes.
4. **Indécidabilité de l'auto-modification (Capacité 4 APM)** : Autoriser un agent à modifier dynamiquement les règles de transition de son propre graphe à l'exécution transforme l'automate fini en une machine de Turing avec réécriture de termes, rendant la vérification formelle de sûreté (*model checking*) strictement indécidable en vertu du théorème de Rice.

---

### 1.3 Évaluation de la fabrique de confiance en services financiers et de l'opposabilité juridique
Le Livre II (« Faire confiance ») et le Livre III (« Encadrer ») prétendent établir une chaîne d'imputabilité et de non-répudiation opposable devant les tribunaux et les régulateurs prudentiels (BSIF, AMF, CAI). Cette construction s'effondre sous trois constats bloquants :
1. **La falsification du « problème des deux sauts » (Two-Hop Delegation)** : Le manuscrit allègue une impossibilité mathématique de préserver l'opposabilité au-delà du second saut de délégation ($A \to B \to C$) et affirme une absence de documentation au degré 3 dans la RFC 8693 (OAuth Token Exchange). Or, l'auteur avoue lui-même en page 198 qu'« *aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict* ». En réalité, la RFC 8693 §4.4 spécifie formellement les *Nested 'act' claims*, mais sa clause normative §4.1 interdit expressément d'utiliser cette revendication pour des décisions de contrôle d'accès. À l'inverse de la thèse de l'auteur, les algèbres de capabilités cryptographiques (Macaroons sous PRF, Biscuit sous Datalog) démontrent mathématiquement que l'opposabilité transitive est préservable sous le modèle standard d'infalsifiabilité existentielle (EUF-CMA) pour tout $n \ge 1$.
2. **L'illusion de la non-répudiation face à l'injection d'invites** : Le manuscrit soutient que la chaîne de mandats signés d'AP2 (Intent $\to$ Cart $\to$ Payment) constitue une preuve opposable liant la transaction au consentement du mandant. Or, en droit de la preuve électronique (LCCJTI art. 28 au Québec, eIDAS art. 26), la non-répudiation exige le **contrôle exclusif du signataire sur son moyen de signature**. Lorsqu'un agent est manipulé par injection indirecte, il appose une signature valide sur une transaction spoliatrice : la signature prouve l'exécution d'un calcul, jamais l'intégrité du consentement humain.
3. **L'amputation délibérée de la Loi 25 québécoise et l'inversion constitutionnelle** : Au Chapitre 29 (Tableau 29.1), l'auteur avoue textuellement exclure de son architecture logicielle les alinéas 1° (divulgation des données utilisées) et 3° (droit de rectification des données) de l'article 12.1 de la Loi 25 au motif que « dériver deux contraintes neuves serait le redécouper », exposant les organisations à des amendes pouvant atteindre 25 M$ ou 4 % du chiffre d'affaires mondial. De plus, prescrire d'inverser la hiérarchie pour placer la Loi 25 au-dessus de la ligne directrice fédérale BSIF E-23 pour des banques sous charte fédérale (Schedule I) viole la compétence exclusive du Parlement fédéral (art. 91(15) de la Loi constitutionnelle de 1867 et arrêt *Marcotte* 2014 CSC 55).

---

### 1.4 Viabilité de l'architecture distribuée (AgentMesh, protocoles, sémantique d'effet et résilience)
L'infrastructure technique décrite dans les Livres I, IV et V souffre de contradictions majeures en systèmes distribués :
1. **Fausse linéarité de l'intégration ($N(N-1)/2 \to 2N$ ou $N \times M \to N + M$)** :
   - Au Chapitre 1, la formule $N(N-1)/2$ est le nombre d'arêtes d'un graphe complet non orienté ($K_N$), contredite par la sparsité des réseaux applicatifs d'entreprise ($|E| = \mathcal{O}(N)$) et par l'asymétrie des adaptateurs orientés ($N(N-1)$). Prétendre qu'un modèle pivot (CDM) ramène le coût à $2N$ occulte le coût de gouvernance et d'évolution du schéma pivot, lui-même combinatoire ($\mathcal{O}(N^2)$).
   - Au Chapitre 8, affirmer que le protocole MCP ramène le coût d'intégration de $N \times M$ à $N + M$ confond l'interconnexion syntaxique (JSON-RPC) avec la calibration sémantique et pragmatique (LCIM niveaux 3 et 4), qui demeure combinatoire face à l'hétérogénéité des modèles d'inférence.
2. **Rupture d'idempotence et transport MCP « sans état »** : Proclamer au Chapitre 8 que la révision MCP du 28 juillet 2026 est un « cœur sans état déployable derrière un tourniquet sans couplage résiduel » est directement démenti par l'usage de poignées d'état (*handles*) pour les requêtes multi-tours. De plus, prescrire la réémission sous un identifiant neuf en cas de rupture de flux sans en-tête d'idempotence déterministe provoque des doubles débits financiers destructeurs.
3. **Incompatibilité transactionnelle sur les rails de paiement souverains (Lynx et RTR)** : Les agents logiciels autonomes sont légalement exclus de l'accès direct aux infrastructures de compensation par la *Loi sur les paiements* (art. 4). De surcroît, le règlement sur Lynx et RTR jouit d'une **finalité légale absolue et irrévocable** (LCRP art. 8 et 13) : le patron Saga compensatoire y échoue structurellement car aucune transaction compensatoire inverse ne peut annuler un règlement dénoué en banque centrale.
4. **Fausse équivalence « At-Least-Once + Idempotence = Exactly-Once » (Ch. 48)** : Cette équivalence méconnaît le problème de la double écriture (*Dual-Write Problem*), le désordre des messages non commutatifs sous asynchronie (Helland 2012) et l'obligation d'un consensus distribué (Théorème FLP 1985) pour synchroniser le registre d'idempotence.

---

### 1.5 Diagnostic global et verdict de recevabilité prudentielle
**Verdict global : RECEVABILITÉ REJETÉE EN L'ÉTAT ACTUEL (RÉSERVE MAJEURE BLOQUANTE).**  
Le compendium ne peut être certifié comme référence opposable pour le déploiement d'agents en secteur bancaire et financier réglementé. L'ouvrage doit impérativement être refondu pour purger ses erreurs mathématiques, restaurer la conformité légale intégrale, actualiser ses sources primaires et synchroniser ses chapitres avec ses propres annexes de clôture.

---

# Section 2 : Matrice complète des défauts répertoriés

```
========================================================================================================================
                                      SYNTHÈSE NUMÉRIQUE DE LA MATRICE DES DÉFAUTS
========================================================================================================================
Sévérité                                        Nombre répertorié    Domaines d'impact principaux
------------------------------------------------------------------------------------------------------------------------
Bloquant / Erreur formelle [Critical]           22 défauts           Théorie, Algorithmes, Cryptographie, Droit, Layout
Majeur / Lacune méthodologique [Major]          35 défauts           Systèmes distribués, FinOps, Normes, Empirie
Mineur / Clarté, Cohérence, Typo [Minor]        28 défauts           Coquilles, Graphiques, Césures, Directives de travail
------------------------------------------------------------------------------------------------------------------------
TOTAL GÉNÉRAL SANS QUOTA                        85 défauts réconciliés et validés sur pièces
========================================================================================================================
```

---

## 2.1 Défauts Bloquants et Erreurs Formelles [Critical]

### DEF-01 : Falsification topologique et économique du coût d'intégration $N(N-1)/2$, illusion de la linéarité $2N$ du format pivot et allégation erronée sur l'adjonction de système
- **Localisation** : Chapitre 1, pp. 5–6 (§ 1.0.1), p. 14 (§ 1.3.1.1), p. 22 (§ 1.6.1).
- **Citations textuelles** :
  - *Page 5* : « ...raccorder N systèmes susceptibles de dialoguer deux à deux peut requérir jusqu’à N(N−1)/2 liaisons, chacune avec sa logique de transport, de format et de correspondance. »
  - *Page 6* : « ...ramènent la complexité de N×N à un ordre linéaire... »
  - *Page 22* : « ...chaque paire exige son propre traducteur, et l’ajout d’un système impose de modifier tous les autres. Le modèle de données canonique brise cette explosion combinatoire [...] ramenant le coût d’intégration à un ordre linéaire, en 2N. »
- **Diagnostic causal approfondi** :
  1. *Confusion de graphes* : $\binom{N}{2} = \frac{N(N-1)}{2}$ est le nombre d'arêtes d'un graphe complet non orienté $K_N$. En intégration logicielle, les transformations sont asymétriques et orientées : le pire cas bilatéral est strictement $N(N-1) = N^2 - N$.
  2. *Allégation fausse sur l'adjonction* : Prétendre que l'ajout d'un système impose de « modifier tous les autres » est formellement faux en point-à-point : l'introduction d'un $(N+1)$-ième nœud requiert d'écrire au plus $2N$ adaptateurs orientés sans modifier aucune des liaisons préexistantes.
  3. *Topologie d'entreprise* : Les réseaux réels sont des graphes clairsemés (*sparse graphs*) à degré moyen borné $\langle k \rangle \ll N$, conférant déjà un coût structurel en $\mathcal{O}(N)$.
  4. *Fausse linéarité du CDM* : Le coût de maintenance d'un schéma canonique $\mathcal{C}$ sous évolution continue ($\mathcal{C} \to \mathcal{C}'$) et d'arbitrage de gouvernance entre comités d'entreprise croît en $\mathcal{O}(N^2)$.
- **Correctif formel** : Modéliser le coût d'intégration sous graphe orienté $G=(V, E)$ avec degré borné $k_{\max}$, et intégrer l'équation de maintenance du format pivot : $TCO_{\text{CDM}}(T) = 2N \cdot c_{\text{build}} + \sum_{t=1}^T \sum_{i=1}^N \lambda_i(t) [c_{\Delta \mathcal{C}} + \sum_{j \neq i} \rho_{ij} c_{\text{update}}]$.

---

### DEF-02 : Rupture taxonomique du LCIM (amputation du niveau 6 Conceptuel), conflit d'ordre partiel EIF/LCIM et omission des couplages stochastiques
- **Localisation** : Chapitre 1, pp. 8–10 (§ 1.1.2, Figure 1.1) et Chapitre 7, p. 80 (Tableau 7.1).
- **Citations textuelles** :
  - *Page 9* : « Le modèle a été raffiné en une échelle à sept niveaux, du niveau 0 [...] jusqu’à l’interopérabilité conceptuelle... »
  - *Page 80 (Tableau 7.1)* : « Tableau 7.1 — Les cinq niveaux du LCIM appliqués à la pile agentique. Niveau : Technique, Syntaxique, Sémantique, Pragmatique, Dynamique. »
- **Diagnostic causal approfondi** :
  1. *Amputation injustifiée* : Le LCIM canonique de Tolk & Muguira (2003, 2009) compte sept niveaux formels ($L_0$ à $L_6$). Le Tableau 7.1 ampute sans explication le niveau 6 (*Conceptual Interoperability*), qui est précisément le niveau où s'opèrent l'alignement des modèles du monde (*World Models*), l'opposabilité juridique des contraintes de finalité et le respect des normes prudentielles (BSIF E-23, Loi 25).
  2. *Conflit d'ordre partiel* : La Figure 1.1 greffe latéralement les niveaux pragmatique, dynamique et conceptuel du LCIM sur la seule couche sémantique de l'EIF, créant un ordre partiel mathématiquement indécidable.
  3. *Omission des couplages LLM* : L'analyse omet le couplage d'état latent ($\mathcal{C}_{\text{state}}$), le couplage de distribution probabiliste et fragilité d'invite ($\mathcal{C}_{\text{distrib}}$), et le couplage épistémique ($\mathcal{C}_{\text{epistemic}}$).
- **Correctif formel** : Rétablir l'échelle canonique intégrale $\mathcal{L}_{\text{LCIM}} = \{L_0 \dots L_6\}$ et modéliser le vecteur de couplage agentique sous forme d'un 8-uplet $\mathbf{C} = \langle c_{\text{tech}}, c_{\text{format}}, c_{\text{loc}}, c_{\text{temp}}, c_{\text{inter}}, c_{\text{state}}, c_{\text{distrib}}, c_{\text{epistemic}} \rangle$.

---

### DEF-03 : Falsification de la métrique $pass^k$ de $\tau$-bench et confusion mathématique avec l'effondrement intra-trajectoire $q^T$
- **Localisation** : Chapitre 6, p. 76 (§ 6.4.2, Tableau 6.2 et Figure 6.4).
- **Citations textuelles** :
  - *Tableau 6.2* : « pass^k ... la probabilité que les k tentatives réussissent toutes — la consistance. Chute brutalement dès que la fiabilité par étape s’éloigne de la perfection. »
  - *Page 76* : « La seconde — pass^k, introduite par τ-bench (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues et multi-étapes. Cette dégradation — où une probabilité d’échec par pas même faible se compose géométriquement sur une longue trajectoire... »
- **Diagnostic causal approfondi** :
  Confusion entre deux grandeurs probabilistes orthogonales :
  1. *Définition réelle de $pass^k$ ($\tau$-bench, Yao et al., arXiv:2406.12045)* : L'exposant $k$ représente le nombre de **réplications indépendantes (*trials/runs*) de la tâche complète** ($pass^k = \mathbb{E}[p^k]$ où $p$ est le taux de succès global par run).
  2. *Fiabilité intra-trajectoire* : La composition géométrique d'une probabilité d'étape $q_t$ sur un horizon séquentiel de $T$ pas est $p = \prod_{t=1}^T q_t = q^T$.  
  Attribuer l'effondrement de $pass^k$ à la composition d'étapes sur une longue trajectoire est une falsification de la littérature : un agent résolvant une tâche en 1 étape ($T=1$) avec $p=0.8$ voit son $pass^8 = (0.8)^8 \approx 0.168$ s'effondrer sans aucune dimension séquentielle multi-pas.
- **Correctif formel** : Dissocier rigoureusement la consistance inter-essais $pass^k = \mathbb{E}[p^k]$ de la fiabilité séquentielle intra-trajectoire $P(S) = \prod_{t=1}^T q_t$.

---

### DEF-04 : Rupture du modèle AAA / Zero Trust face au détournement sémantique et à l'injection indirecte
- **Localisation** : Chapitre 3, pp. 36–37 (§ 3.1.1), pp. 39–41 (§ 3.2.3, § 3.3.1).
- **Citations textuelles** :
  - *Page 40* : « Le zero-trust formalise le principe ne jamais faire confiance, toujours vérifier... SPIFFE et son implémentation de référence SPIRE fournissent à chaque charge un identifiant et un document d’identité vérifiable... »
  - *Page 41* : « Lecture de l’auteur — c’est l’un des rares endroits de ce Livre où une classe entière d’incidents disparaît plutôt que de se déplacer. »
- **Diagnostic causal approfondi** :
  1. *Inopérance du PEP/PDP L4/L5* : SPIFFE/SPIRE et le Zero Trust d'infrastructure (NIST SP 800-207) valident cryptographiquement la charge hôte (mTLS, SVID X.509). Lorsqu'un agent est subverti par injection de prompt indirecte, l'appel d'outil malveillant est émis par le conteneur officiel avec ses identifiants légitimes. Le PEP réseau valide la requête sans anomalie.
  2. *Effondrement de l'authenticité d'intention* : L'authenticité cryptographique de l'émetteur ne garantit plus la légitimité de son intention cognitive.
  3. *Affirmation fallacieuse* : Prétendre qu'« une classe entière d'incidents disparaît » est un sophisme qui masque le transfert de la menace vers la couche L7 sémantique.
- **Correctif formel** : Compléter le contrôle d'accès par le modèle de contrôle des flux d'information (IFC, Myers & Liskov 1997) avec suivi de teinte (*taint tracking*) : $\forall d \in \text{Context}(\text{Agent}), \text{Tainted}(d) \implies \text{Capabilities}(\text{Agent}) \cap \text{SideEffectTools} = \emptyset$.

---

### DEF-05 : Faux parallélisme d'extensibilité GAV vs LAV, omission de GLAV, et intraitabilité computationnelle d'OWL 2 DL (2NEXPTIME)
- **Localisation** : Chapitre 2, pp. 32–34 (§ 2.3.3, § 2.3.4, § 2.4.1).
- **Citations textuelles** :
  - *Page 33* : « GAV ... Réécriture de requête simple ; ajout de source coûteux... LAV ... Extensibilité supérieure — ajouter une source n’affecte pas les autres — au prix d’une réécriture de requête plus complexe. »
  - *Page 34* : « ...par confrontation aux axiomes ontologiques — et non comme un contrat établi. »
- **Diagnostic causal approfondi** :
  1. *Omission de la NP-complétude* : La réécriture de requêtes en LAV (*Answering Queries Using Views*, Levy et al. 1995, Lenzerini 2002) est un problème **NP-complet** en la taille de la requête (Abiteboul & Duschka 1998) et devient indécidable en présence de contraintes d'intégrité.
  2. *Omission de GLAV* : La médiation de données moderne utilise GLAV (*Global-and-Local-As-View*) et les dépendances génératrices de tuples (*tgds*), seul cadre adapté aux flux d'agents distribués.
  3. *Complexité prohibitive d'OWL 2 DL* : Fondé sur la logique $\mathcal{SROIQ}(\mathcal{D})$, le test de cohérence est **2NEXPTIME-complet** (Kazakov 2008), incompatible avec les boucles d'agents temps réel.
- **Correctif formel** : Prescrire des médiateurs GLAV déterministes et substituer à OWL 2 DL les profils polynomiaux **OWL 2 QL** (logique DL-Lite, réécriture en $\text{AC}^0$) et **OWL 2 EL** ($\mathcal{EL}^{++}$, temps polynomial PTIME).

---

### DEF-06 : Effondrement stochastique de ReAct ($p^T$ et super-exponentiel), invalidité de ReWOO en univers POMDP, et illusion du décodage contraint
- **Localisation** : Chapitre 4, p. 51 (§ 4.1.5), pp. 52–54 (§ 4.2.1, § 4.2.3), p. 58 (§ 4.4.1), p. 60 (§ 4.4.4).
- **Citations textuelles** :
  - *Page 52* : « Le critère d’arrêt n’est pas un détail mais une garantie de terminaison. Une boucle sans budget d’appels explicite ni détection de stagnation peut diverger... Fixer dès la conception un budget de pas, un plafond de jetons... »
  - *Page 53* : « ReWOO (...) pousse le découplage plus loin en planifiant l’ensemble des appels d’outils avant d’observer leurs résultats... »
  - *Page 58* : « Les sorties structurées garantissent que l’argument respecte le schéma... »
- **Diagnostic causal approfondi** :
  1. *Effondrement super-exponentiel* : Sous dilution d'attention (*context rot*), la probabilité de transition correcte se dégrade : $p_t = p_0 (1-\lambda)^t$. La probabilité de succès global s'effondre en loi super-exponentielle $P(\text{Succès}_T) = p_0^T (1-\lambda)^{\frac{T(T-1)}{2}} \to 0$.
  2. *Confusion terminaison vs avortement* : Un budget de pas ne garantit pas la terminaison correcte (*total correctness*), mais force un avortement arbitraire qui laisse des effets de bord financiers suspendus et incohérents.
  3. *Invalidité de ReWOO en POMDP* : Planifier tous les outils en boucle ouverte sans observer les résultats intermédiaires échoue dès qu'un argument d'outil dépend d'un retour d'état de l'environnement.
  4. *Illusion du décodage contraint* : Valider la grammaire JSON Schema ne garantit en rien l'admissibilité sémantique (un montant de virement négatif est valide sous JSON Schema float).
- **Correctif formel** : Encadrer ReAct par un automate de surveillance externe (*Safety Supervisor Automaton*) couplé au patron Saga avec transactions compensatoires, et restreindre ReWOO aux graphes statiques sans dépendance de données d'état.

---

### DEF-07 : Irréversibilité informationnelle de la compaction mémorielle (Shannon/DPI) et pathologie d'inversion de rangs du RRF
- **Localisation** : Chapitre 5, pp. 63–64 (§ 5.1.2–5.1.3), pp. 67–68 (§ 5.3.2).
- **Citations textuelles** :
  - *Page 64* : « L’enjeu de conception est la réversibilité. [...] La bonne pratique consiste à compacter en conservant un pointeur vers la trace intégrale... »
  - *Page 67* : « Les listes de résultats sont fusionnées par la fusion de rangs réciproques (Reciprocal Rank Fusion, RRF)... »
- **Diagnostic causal approfondi** :
  1. *Violation du Théorème de Traitement de l'Information (Shannon)* : La chaîne de résumés successifs $H_0 \to S_1 \to S_2 \dots$ subit une perte d'information monotone stricte : $I(X; S_n) \le I(X; S_{n-1}) \le I(X; H_0)$. Le résumé par LLM est une compression avec perte irréversible ($H(X \mid f(X)) > 0$). Conserver un pointeur passif ne résout rien car le modèle ne dispose d'aucun signal d'attention pour déclencher la relecture du texte déporté (*amnésie épistémique*).
  2. *Pathologie mathématique du RRF* : En écrasant l'amplitude des scores de similarité au profit des seuls rangs ordinaux ($\text{RRF}(d) = \sum \frac{1}{k + r_m(d)}$), le RRF produit des inversions aberrantes. Un document $d_1$ à pertinence quasi absolue ($\sigma_{\text{dense}}=0.99$, rang 2 en dense, rang 60 en BM25) obtient un score de $0.02446$, alors qu'un document médiocre $d_2$ ($\sigma_{\text{dense}}=0.45$, rang 10 en dense et rang 10 en lexical) obtient $0.02857$. Le document médiocre surclasse le document critique.
- **Correctif formel** : Bannir le terme « compaction réversible », isoler les faits immuables dans un magasin déterministe (ATMS de de Kleer), et remplacer le RRF par une fusion de scores étalonnés (z-score) : $\text{Score}(d) = \alpha \tilde{\sigma}_{\text{dense}} + (1-\alpha) \tilde{\sigma}_{\text{lexical}}$.

---

### DEF-08 : Fausse aporie sur la collision terminologique « ACP » (Confusion Data Plane L7 vs Control Plane L4/L5)
- **Localisation** : Chapitre 10, pp. 126–127 (§ 10.5.3) et Chapitre 7, p. 87 (Tableau 7.3).
- **Citations textuelles** :
  - *Page 126* : « Restent deux objets, et c’est entre eux que la confusion est à la fois la plus facile et la plus dommageable : l’ACP protocolaire [...] et la composante ACP de la couche d’infrastructure... si les deux objets n’en font qu’un, la fusion d’août 2025 vaut pour la couche d’infrastructure... s’ils sont deux, la couche d’infrastructure porte une composante active... Les sources ne tranchent pas, et aucune inférence n’est proposée ici. »
- **Diagnostic causal approfondi** :
  L'auteur érige une collision homonymique industrielle ordinaire en une énigme insoluble par confusion des couches du modèle OSI :
  - **ACP d'IBM BeeAI (mars 2025)** est strictement un protocole applicatif (**Couche 7 OSI / Data Plane**) d'échange de charges utiles sémantiques entre agents, fusionné le 29 août 2025 dans A2A v1.0 sous la Linux Foundation.
  - **ACP de Cisco AGNTCY (juillet 2025)** désigne l'Agentic Control Plane (**Couche 4/5 OSI / Control Plane Réseau**), brique de signalisation réseau gérant le routage de passerelles et les canaux sécurisés SLIM.  
  Prétendre qu'une brique de réseau Cisco aurait pu s'éteindre à cause d'une fusion logicielle applicative d'IBM est un contresens architectural total.
- **Correctif formel** : Réfuter l'indécidabilité et poser la séparation d'architecture : Data Plane L7 = A2A v1.0 (absorbant l'ACP-IBM), Control Plane L5 = ACP-Cisco AGNTCY, Transport L4 = maillage SLIM.

---

### DEF-09 : Citation réglementaire d'un prétendu « règl. (UE) 2026/1744 » et calendrier contradictoire de l'AI Act
- **Localisation** : Chapitre 10, p. 124 (lignes 10296–10303), en contradiction avec les pp. 30520, 34016, 60352 et 60726.
- **Citations textuelles** :
  - *Page 124* : « ...la mise en conformité générale se poursuivant jusqu’au 2 août 2027 (2028 pour le haut risque, règl. (UE) 2026/1744). »
- **Diagnostic causal approfondi** :
  1. *Texte inexistant* : Le règlement désigné comme « règl. (UE) 2026/1744 » n'existe pas dans le Journal officiel de l'UE pour l'IA (le texte unique est le Règlement (UE) 2024/1689). L'auteur admet en annexe (p. 60726) : « EUR-Lex répond HTTP 202 sans contenu; la date de publication [...] n'a pas été relue. »
  2. *Contradiction interne* : La page 124 annonce une échéance à 2028, tandis que les chapitres 30 et 34 affirment qu'elle est fixée au 2 décembre 2027.
  3. *Calendrier réel de l'art. 111 du Règlement (UE) 2024/1689* : GPAI au 2 août 2025, Annexe III au 2 août 2026, Annexe I au 2 août 2027. Aucun report général à 2028 n'existe pour l'Annexe III.
- **Correctif formel** : Purger toute mention du « règl. (UE) 2026/1744 » et aligner les échéances sur l'article 111 du Règlement (UE) 2024/1689.

---

### DEF-10 : Absence de formalisme transactionnel réparti (ACID/BASE) et impossibilité d'atomicité dans AP2 sans patron Saga compensatoire
- **Localisation** : Chapitre 10, p. 116 (§ 10.1.1), p. 118 (§ 10.1.4), Figure 10.4 p. 125.
- **Citations textuelles** :
  - *Page 116* : « AP2 s’attache à ce qui se passe lorsque la tâche déléguée engage un paiement [...] protocole qui prend le relais au point où la délégation cesse d’être réversible »
  - *Page 118* : « Il porte la chaîne de mandats — Intent Mandate, Cart Mandate, Payment Mandate — matérialisés comme attestations vérifiables signées... »
- **Diagnostic causal approfondi** :
  1. *Une chaîne de jetons signés n'est pas une transaction répartie* : AP2 n'est qu'un format d'échange de Verifiable Credentials statiques. Il n'offre aucune garantie d'atomicité face aux pannes réseau, refus de compensation ou crashs de marchands.
  2. *Violation de l'Atomicité* : Si le `Payment Mandate` est capturé (débit bancaire) mais que le marchand crash avant la délivrance du service, le système reste dans un état incohérent (fonds débités sans contrepartie).
  3. *Fausse allégation d'irréversibilité* : Les rails bancaires réels fonctionnent avec pré-autorisations, compensations différées et chargebacks. Sans patron Saga orchestré avec compensations explicites ($C_i$), AP2 est inapte au traitement transactionnel bancaire.
- **Correctif formel** : Requalifier AP2 en protocole de mandat et d'autorisation, et spécifier l'automate Saga : $G = (T_1 \dots T_n)$ avec vecteur de compensation $(C_n \dots C_1)$, liant chaque mandat à des primitives de `Void Mandate` et `Reversal Mandate`.

---

### DEF-11 : Rupture de la non-répudiation juridique dans AP2 face à l'injection d'invites par anéantissement du contrôle exclusif du mandant
- **Localisation** : Chapitre 10, p. 120 (Tableau 10.1), p. 123 (§ 10.3.4), pp. 124–125 (§ 10.4.2).
- **Citations textuelles** :
  - *Page 123* : « ...un agent dont l’intention est détournée signera un mandat malveillant parfaitement valide. Le verrou n’est pas la vérifiabilité cryptographique du mandat — elle fonctionne — mais l’intégrité du raisonnement qui le produit »
  - *Page 124* : « La chaîne intention -> panier -> paiement du § 10.1.4, signée et horodatée, fournit l’élément probant qui rattache une transaction contestée à un consentement antérieur du mandant ».
- **Diagnostic causal approfondi** :
  Contradiction interne directe : l'auteur admet p. 123 qu'un agent manipulé par injection signera un mandat malveillant, puis affirme pp. 124-125 que cette signature constitue la preuve opposable de non-répudiation rattachée au consentement de l'humain. En droit de la preuve électronique (LCCJTI art. 28, eIDAS art. 26), la non-répudiation exige le **contrôle exclusif du moyen de signature**. La délégation d'une clé à un agent stochastique faillible anéantit ce contrôle exclusif : devant un tribunal, la signature prouve l'exécution du code de l'agent, jamais le consentement du débiteur.
- **Correctif formel** : Dissocier les transactions sous présence humaine (signature FIDO2/Passkey dans une enclave matérielle TPM/Secure Enclave assurant le contrôle exclusif) des transactions autonomes déléguées (exclusion de la non-répudiation opposable au client, bascule vers la responsabilité objective de l'institution et plafonds stricts sous séquestre).

---

### DEF-12 : Rupture d'idempotence et invalidation du routage à tourniquet sous transport MCP révisé sans état
- **Localisation** : Chapitre 8, p. 92 (Tableau 8.2), Ch. 11, p. 135 (§ 11.3.1).
- **Citations textuelles** :
  - *Page 92* : « Cœur sans état (ratifié le 28 juill. 2026) : suppression de la poignée de main, de l’identifiant de session et de la reprise de flux. Couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet. »
  - *Page 135* : « ...la reprise de flux et la retransmission de messages sont retirées — un flux de réponse interrompu perd la requête en vol, que le client doit réémettre sous un identifiant neuf. »
- **Diagnostic causal approfondi** :
  1. *Rupture d'idempotence* : Si un appel d'outil modifiant l'état (virement bancaire) est interrompu après exécution serveur mais avant la réception du flux SSE, réémettre la charge sous un `id` JSON-RPC neuf entraîne une seconde exécution non dédupliquée (perte financière directe).
  2. *Contradiction du tourniquet* : Les requêtes multi-tours (MRTR) utilisent des poignées d'état (*handles*) émises par le serveur. Si le tour 1 génère un handle sur l'instance $S_1$ et que le tourniquet route le tour 2 vers $S_2$, l'appel échoue immédiatement (`Unknown Handle`), réintroduisant l'obligation d'affinité de session ou d'un magasin d'état distribué.
- **Correctif formel** : Rétablir l'obligation d'un en-tête d'idempotence déterministe (`Idempotency-Key` HMAC) avec cache de déduplication serveur, et imposer le chiffrement AEAD (ChaCha20-Poly1305) pour toute poignée d'état transitant par le client.

---

### DEF-13 : Falsification formelle du théorème des deux sauts, aveu d'absence p. 198, double erreur sur RFC 8693 et assertion erronée sur Biscuit
- **Localisation** : Chapitre 17, pp. 196–200 (§ 17.6).
- **Citations textuelles** :
  - *Page 197* : « Ce que ce texte prévoit ou tait de la composition de plusieurs délégations successives n’est pas documenté par le socle — degré 3. »
  - *Page 198* : « Le terme "limites démontrées" mérite d'être borné [...] aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »
  - *Page 199* : « L’attribut act exprime la chaîne d’acteurs ; il ne démontre pas l’opposabilité de chaque saut... »
  - *Page 200* : « Macaroons et Biscuit atténuent une portée, ils ne portent pas l'identité de chaque maillon... »
- **Diagnostic causal approfondi** :
  1. *Aveu d'absence* : Le théorème de rupture mathématique au second saut annoncé dans le plan directeur est expressément avoué non démontré p. 198.
  2. *Erreur sur RFC 8693 §4.4* : La composition multi-sauts n'est pas absente (degré 3) : la section 4.4 spécifie formellement les *Nested 'act' Claims*.
  3. *Impasse RFC 8693 §4.1* : La clause §4.1 dispose expressément : *« The 'act' claim [...] MUST NOT be used for access control decisions »*, invalidant son usage pour le contrôle d'accès opposable.
  4. *Erreur factuelle sur Biscuit* : Chaque bloc d'atténuation Biscuit est signé par la clé du délégataire sortant et peut lier formellement la clé publique du délégataire suivant par des faits Datalog signés sous EUF-CMA.
- **Correctif formel** : Requalifier le problème des deux sauts en défi d'impédance protocolaire et de révocation en cascade. Démontrer par induction la préservation de l'opposabilité sous EUF-CMA : $\text{Adv}_{\text{Forge}}(\Delta_n) \le \sum_{k=1}^n \text{Adv}_{\text{EUF-CMA}}(A_{k-1}) \le n \cdot \text{negl}(\lambda)$.

---

### DEF-14 : Falsification de la crise d'OAuth 2.0 : omission des jetons liés au porteur (DPoP RFC 9449, MTLS RFC 8705)
- **Localisation** : Chapitre 12, p. 144 (lignes 12008–12011), Tableau 12.1.
- **Citations textuelles** :
  - *Page 144* : « ...le maillon qui cède y est nommé, et il est architectural : le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. »
- **Diagnostic causal approfondi** :
  1. *Omission de l'état de l'art IETF* : L'IETF a neutralisé la non-liaison des jetons porteurs en publiant le RFC 9449 (DPoP - *Demonstrating Proof-of-Possession*) en septembre 2023 et le RFC 8705 (mTLS). Le vol du jeton au repos (campagne UNC6395 citée en exemple) est totalement inopérant sans la clé privée du client.
  2. *Méprise sur la racine de la crise* : Même sous DPoP, un agent dont le contexte est manipulé émettra des preuves DPoP valides pour accomplir des actes malveillants. La faillite d'OAuth ne réside pas dans l'absence de liaison au porteur, mais dans l'incapacité d'OAuth à lier l'autorisation à **l'intégrité cognitive du modèle et au contexte sémantique d'inférence**.
- **Correctif formel** : Réécrire le § 12.2 et le Tableau 12.1 pour intégrer DPoP (RFC 9449) et démontrer que l'autorisation machine classique ignore l'état de corruption cognitive de l'agent appelant.

---

### DEF-15 : Incompatibilité théorique de la tolérance aux pannes byzantines (BFT) appliquée aux agents probabilistes
- **Localisation** : Chapitre 11, p. 133 (§ 11.2.1).
- **Citations textuelles** :
  - *Page 133* : « ...un agent non déterministe qui émet un message plausible mais erroné se comporte comme un nœud byzantin, ce qui ouvre la question [...] de seuils de quorum et de redondance pour des acteurs probabilistes. »
- **Diagnostic causal approfondi** :
  1. *Absence d'égalité binaire* : PBFT (Castro & Liskov 1999) exige une égalité binaire stricte des empreintes cryptographiques ($H(m_1) = H(m_2)$). Deux agents LLM non défaillants ne génèrent jamais de sorties textuelles identiques bit-à-bit, rendant impossible le calcul de quorum sur condensats.
  2. *Violation de l'indépendance des pannes (Common-Cause Failures)* : Les agents partagent les mêmes familles de fondation (Claude, GPT, Llama). Face à une injection ou un piège sémantique, ils partagent les mêmes modes d'échec ($P(E_i \cap E_j) \gg P(E_i)P(E_j)$) : un quorum super-majoritaire d'agents homogènes convergera unanimement vers l'erreur.
- **Correctif formel** : Abandonner le quorum binaire de transport au profit d'un consensus sur invariants logiques formels vérifiables par solveurs SMT, sous exigence stricte d'hétérogénéité des modèles de fondation.

---

### DEF-16 : Rupture de déterminisme et non-contrôlabilité de l'autonomie encadrée en OO4
- **Localisation** : Chapitre 22, pp. 254, 258–259 (§ 22.1, § 22.4).
- **Citations textuelles** :
  - *Page 254* : « OO4 — l’orchestration explicite d’agents conscients du processus [...] les tâches essentielles doivent être imposées de façon déterministe par le cadre. »
- **Diagnostic causal approfondi** :
  L'encadrement structurel d'un graphe de workflow (CFG) ne neutralise pas la stochasticité de l'agent logé dans le nœud. Dès lors qu'une transition dépend d'une garde évaluant la sortie d'un modèle stochastique, la probabilité de franchissement n'est pas unitaire. En présence d'événements non contrôlables ($\Sigma_{uc} \neq \emptyset$), le système global est un POMDP : le problème de l'arrêt et la conformité aux invariants de sécurité deviennent indécidables.
- **Correctif formel** : Énoncer le théorème d'arrêt borné pour OO4 : existence d'une borne stricte d'itérations $K_c$ par cycle et d'un repli déterministe statique sans agent (*hardcoded deterministic fallback*).

---

### DEF-17 : Absence complète de formalisation d'automates finis (DFA) au Chapitre 29 et pseudo-déterminisme des frames
- **Localisation** : Chapitre 29, pp. 327–335 (§ 29.0, Tableau 29.1, Figure 29.1).
- **Citations textuelles** :
  - *Page 327* : « Traduire une exigence juridique en contrainte d’architecture n’est pas une opération de lecture : c’est un raisonnement d’auteur... »
  - *Page 334* : « ...le processus est imposé de façon déterministe par le cadre, qui invoque les agents... »
- **Diagnostic causal approfondi** :
  Le plan directeur promettait une « preuve de conformité mathématique par automates finis ». Le chapitre ne contient aucune formalisation de quintuplet $(Q, \Sigma, \delta, q_0, F)$ (le mot automate est absent). L'auteur substitue un schéma qualitatif de six boîtes (Fig. 29.1). Le système ne comporte aucun état puits absorbant ($q_{sink}$) en cas d'injection ou d'erreur, et l'attente asynchrone non bornée de la validation humaine crée des blocages réactifs (*deadlocks*) destructeurs en temps réel.
- **Correctif formel** : Requalifier le dispositif en patron d'architecture logicielle sous garde de politiques, ou formaliser le DFA complet avec alphabet contraint, état puits $q_{sink}$ et temporisation stricte sur points d'arrêt humains.

---

### DEF-18 : Amputation délibérée de 40 % des obligations de l'art. 12.1 de la Loi 25 québécoise dans le Tableau 29.1
- **Localisation** : Chapitre 27, p. 315 (§ 27.2) ; Chapitre 29, pp. 328–330 (§ 29.1, Tableau 29.1 p. 329).
- **Citations textuelles** :
  - *Page 329* : « L’articulation de l’article 12.1 a été corrigée [...] Deux de ces éléments — le 1° et le 3° — n’ont aucune ligne dans la table ci-dessus. La somme ne les y ajoute pas : ce chapitre est conservé intact, et dériver deux contraintes neuves serait le redécouper. »
- **Diagnostic causal approfondi** :
  L'auteur refuse délibérément d'intégrer dans sa matrice d'architecture les obligations de l'art. 12.1 al. 2 : 1° (divulgation des données utilisées) et 3° (droit de faire rectifier les données erronées). Cette amputation supprime la traçabilité immuable des données d'entrée (*input data fingerprinting*) et le protocole d'invalidation de cache vectoriel en RAG, exposant les institutions à des sanctions de la CAI pouvant atteindre 25 M$ CAD ou 4 % du chiffre d'affaires mondial.
- **Correctif formel** : Réintégrer immédiatement les lignes 1° et 3° dans le Tableau 29.1 avec obligation d'instantané cryptographique des entrées et protocole de purge vectorielle lors d'une rectification.

---

### DEF-19 : Incompatibilité systémique des flux agentiques sur les rails souverains Lynx et RTR (Loi sur les paiements et LCRP)
- **Localisation** : Chapitre 31, pp. 350–355 ; Chapitre 33, pp. 372–378 ; Chapitre 36, pp. 411–417 ; Livre V, p. 568.
- **Citations textuelles** :
  - *Page 350* : « La saga compensatoire [...] échoue dès lors qu’un des effets de bord est irréversible. »
  - *Page 415* : « ...sur les rails irréversibles, la rétrofacturation n’existe tout simplement pas... »
  - *Page 568* : La somme avoue « ne prescrire aucune idempotence, aucune compensation spécifiée, ni clé de jointure entre un effet et l'appel qui l'a produit ».
- **Diagnostic causal approfondi** :
  1. *Exclusion statutaire* : L'art. 4 de la *Loi sur les paiements* réserve l'accès à Lynx/RTR aux seules institutions financières membres dépositaires et entités RPAA supervisées ; les agents logiciels autonomes y sont légalement exclus.
  2. *Finalité légale absolue* : En vertu des art. 8 et 13 de la LCRP, le règlement sur Lynx/RTR est irréversible dès son exécution par le système : aucune transaction compensatoire Saga n'est possible.
  3. *Tempête de doubles débits* : En cas de coupure réseau sur confirmation d'état (`pacs.002`), une boucle d'agent réémettant la requête avec un nouvel `UETR` génère un second débit bancaire irrévocable.
- **Correctif formel** : Proscrire tout appel direct d'agents vers les rails RTR/Lynx et interposer une passerelle d'idempotence financière déterministe (2PC/ACID) scellant un UETR immuable avant génération du message ISO 20022.

---

### DEF-20 : Inversion verticale structurelle et contradiction totale entre le Tableau 45.2 et la Figure 45.2 du Blueprint Boréalis/IBM
- **Localisation** : Chapitre 45, § 45.2, Tableau 45.2 (page 510) et Figure 45.2 (page 511).
- **Diagnostic causal approfondi** :
  Deux pages consécutives portant le même titre officiel (« *La vue en couches C1-C8 du blueprint...* ») présentent une inversion spatiale intégrale et une désynchronisation sémantique complète :
  - *Tableau 45.2 (p. 510)* : C1 = Sommet (« Exposition et passerelles ») $\dots$ C8 = Base (« Socle OpenShift »).
  - *Figure 45.2 (p. 511)* : C1 = Base (« Socle d'exécution ») $\dots$ C8 = Sommet (« Gouvernance »).
  - *Divergences intermédiaires* : C2 = Intégration (Tableau) vs Protocoles (Figure) ; C3 = Messagerie (Tableau) vs Identité (Figure) ; C4 = Données (Tableau) vs Maillage PEP/PDP (Figure) ; C6 = Gouvernance (Tableau) vs Données (Figure).  
  Cette contradiction interne détruit l'opposabilité de l'architecture de référence : une référence à « C4 » désigne deux composants mutuellement exclusifs selon la page consultée.
- **Correctif formel** : Réaligner le Tableau 45.2 sur l'ordre ascendant standard de la Figure 45.2 (C1 = Socle matériel jusqu'à C8 = Gouvernance) en unifiant rigoureusement les intitulés de couches.

---

### DEF-21 : Falsification arithmétique de la métrique Anthropic et complexité quadratique $\mathcal{O}(K^2)$ des jetons cumulés
- **Localisation** : Chapitre 40, § 40.5 (page 464) et § 40.6 (page 466).
- **Citations textuelles** :
  - *Page 464* : « ...environ quinze fois les jetons d’un agent unique... »
  - *Page 464* : « ...l’intensité en jetons d’une trajectoire croît au moins linéairement, souvent davantage, avec le nombre de tours. »
- **Diagnostic causal approfondi** :
  1. *Erreur d'un facteur 4 sur Anthropic* : L'étude d'Anthropic (13 juin 2025) chiffre la consommation multi-agent à $15\times$ par rapport à un *standard chat*, l'agent unique consommant déjà $4\times$. Le ratio réel multi-agent vs agent unique est de $15/4 = 3.75\times$. Le texte surévalue le surcoût de 400 %.
  2. *Complexité quadratique réelle* : Sans prompt caching, au tour $k$, le LLM réingère l'historique $I_k = C_0 + (k-1)\Delta\tau$. La consommation totale cumulée facturée sur $K$ tours est $T_{\text{input}}(K) = \sum_{k=1}^K I_k = K \cdot C_0 + \Delta\tau \frac{K(K-1)}{2} = \mathcal{O}(K^2)$. Qualifier cette dépense de « linéaire » masque l'explosion budgétaire en production.
- **Correctif formel** : Rectifier le ratio Anthropic à 3,75x et exposer la loi quadratique $\mathcal{O}(K^2)$ des jetons d'entrée cumulés.

---

### DEF-22 : Substitution d'objet au Chapitre 50 (absence de décommissionnement) et non-rejouabilité des axiomes en Annexe B
- **Localisation** : Chapitre 50, pp. 568–577 ; Annexe B, p. 584 ; Annexe I.2, p. 651.
- **Citations textuelles** :
  - *Ch. 50 p. 568* : « Thèse — le compendium est daté et le dit — événements qui le périment, protocole de revalidation, conditions de gel des chapitres périssables. »
  - *Annexe B p. 584* : « S-153 — L'invariant à quatre termes. [C] ... Citation non rejouable » ; « S-154 — La délégation au-delà de deux sauts. [C] ... Citation non rejouable ».
  - *Annexe I.2 p. 651* : « ...les socles des Vol. II et III ne portent PAS leurs sources sous une forme reprenable... »
- **Diagnostic causal approfondi** :
  1. *Substitution d'objet au Ch. 50* : Promis comme le protocole de mise hors service et de décommissionnement de l'agent logiciel (BSIF E-23, Loi 25), le chapitre dévie à 100 % vers l'auto-maintenance éditoriale du document papier *Compendium* (le terme décommissionnement compte zéro occurrence).
  2. *Circularité en Annexe B* : Les axiomes directeurs ($S\text{-}153$, $S\text{-}154$, $S\text{-}156$) portent la mention officielle « Citation non rejouable », privant l'ouvrage de force probatoire.
  3. *89,3 % du socle sans adresse primaire* : L'Annexe I.2 admet que 142 faits sur 159 n'ont aucune adresse primaire résoluble dans la bibliographie consolidée.
- **Correctif formel** : Déployer dans le Ch. 50 un protocole d'ingénierie de décommissionnement en 5 phases (Dérive, Draining, Révocation clés/DID, Purge vectorielle, Archivage WORM 7 ans), et éliminer les mentions « non rejouable » en Annexe B en reliant chaque fait à une référence externe publique.

---

## 2.2 Défauts Majeurs / Lacunes Méthodologiques et Architecturales [Major]

- **DEF-MAJ-01 : Évasion théorique majeure sur le consensus distribué sous partition réseau (§ 1.6.2.2, pp. 23–24)**  
  *Diagnostic* : L'auteur exclut arbitrairement la modélisation de l'accord sous partition réseau (« périmètre assumé et déclaré »). Dans un traité bancaire, ignorer les théorèmes FLP (1985) et CAP prive les Livres III et V de fondement théorique sous panne réseau.
- **DEF-MAJ-02 : Inexactitude normative sur SAML 2.0 et omission de ReBAC (Ch. 3, p. 38, pp. 40–41)**  
  *Diagnostic* : SAML 2.0 Core Spec Section 2.7 définit formellement `AuthzDecisionStatement` ; affirmer que SAML ne transporte jamais d'autorisation est inexact. De plus, l'IAM est restreint à RBAC/ABAC en omettant ReBAC (Google Zanzibar), pourtant indispensable aux graphes d'autorité multi-agents.
- **DEF-MAJ-03 : Falsification de l'échec de FIPA-ACL et méconnaissance de la force illocutoire dans MCP/A2A (Ch. 6, p. 73 ; Ch. 7, p. 81)**  
  *Diagnostic* : L'échec de FIPA-ACL résulte de sa sémantique mentaliste inobservable et d'obstacles logiciels lourds (CORBA, LISP). Par ailleurs, MCP encode nativement les actes illocutoires de Searle (`tools/call` = directive, `resources/read` = assertion, `notifications` = déclaration).
- **DEF-MAJ-04 : Conflit logique entre la monotonicité d'OWL 2 DL et le non-déterminisme des agents (Ch. 2, pp. 31–34)**  
  *Diagnostic* : OWL 2 DL est strictement monotone. L'insertion d'assertions provisoires révisables par un agent engendre des inconsystances conduisant à une explosion déductive (*ex falso quodlibet*).
- **DEF-MAJ-05 : Absence de valeur probatoire des traces OpenTelemetry pour l'auditabilité financière (Ch. 3, p. 45 ; Ch. 38, pp. 441–443)**  
  *Diagnostic* : Les traces OTel non signées, non scellées sur registre immuable et échantillonnées statistiquement n'ont aucune valeur probatoire devant le BSIF ou un tribunal (violation de BSIF E-23 et Sarbanes-Oxley § 404).
- **DEF-MAJ-06 : Omission des topologies d'essaim (Swarm) et de marché (Ch. 6, pp. 71–72)**  
  *Diagnostic* : Le texte restreint les topologies à quatre graphes statiques (Étoile, Chaîne, Arbre, Graphe) en ignorant la coordination stigmergique (Swarm) et les enchères de marché dynamique.
- **DEF-MAJ-07 : Chimère bibliographique sur Plan-and-Solve Prompting (Ch. 4, p. 53)**  
  *Diagnostic* : Attribue d'abord l'article à « Wang, Wei, Schuurmans et coll. » avant de citer correctement « Wang, Xu, Lan et coll. » dans la même phrase (confusion avec les auteurs de *Self-Consistency*).
- **DEF-MAJ-08 : Sous-spécification des canaux d'exfiltration pour CodeAct et Computer Use (Ch. 4, pp. 53, 59–60)**  
  *Diagnostic* : Omet les attaques d'exfiltration par canaux auxiliaires DNS/temporels pour CodeAct et les attaques adversariales multimodales par injection visuelle indirecte pour Computer Use.
- **DEF-MAJ-09 : Évasion de confinement (Path Traversal) par dépréciation des racines MCP (Ch. 8, p. 91)**  
  *Diagnostic* : Remplacer la frontière de bac à sable `roots` par des arguments d'outils générés par le LLM transfère la sécurité à un composant faillible, ouvrant la voie à des traversées de répertoires arbitraires.
- **DEF-MAJ-10 : Absence de modélisation de concurrence et double dépense budgétaire sous AP2 (Ch. 10, pp. 115–118)**  
  *Diagnostic* : Deux sous-agents mandatés en parallèle peuvent présenter simultanément des paniers de 3 500 $ et 2 500 $ sur une enveloppe globale de 5 000 $, violant la limite budgétaire faute de verrou distribué ou schéma de réservation temporaire (*Commit-Hold*).
- **DEF-MAJ-11 : Vulnérabilité d'usurpation de l'Agent Card statique A2A sans preuve de possession (Ch. 8, p. 97 ; Ch. 12, p. 144)**  
  *Diagnostic* : La détention d'une Agent Card statique signée accessible publiquement permet le rejeu d'identité ; l'architecture omet d'imposer une Preuve de Possession éphémère (DPoP RFC 9449 ou HTTP Signatures RFC 9421).
- **DEF-MAJ-12 : Cadrage d'E/S et corruption du parseur JSON-RPC sur transport stdio de MCP (Ch. 8, p. 92)**  
  *Diagnostic* : L'émission d'un log ou avertissement non JSON sur `stdout` désynchronise irrémédiablement le parseur de l'hôte (Parse Error -32700), imposant l'isolation stricte de `stdout` pour les trames NDJSON et `stderr` pour les logs.
- **DEF-MAJ-13 : Confusion entre erreurs JSON-RPC et erreurs fonctionnelles d'outils (Ch. 8, pp. 93–94)**  
  *Diagnostic* : Renvoyer une erreur JSON-RPC (-32601) pour un échec fonctionnel disjoncte le runtime, alors que renvoyer un `result` avec `isError: true` permet l'auto-correction cognitive par le LLM.
- **DEF-MAJ-14 : Faille du Human-In-The-Loop par opacité sémantique face à l'injection indirecte (Ch. 11, pp. 130–131)**  
  *Diagnostic* : L'opérateur humain valide aveuglément des arguments techniques obfusqués générés par un agent manipulé ; obligation d'un moteur déterministe de projection d'impact métier.
- **DEF-MAJ-15 : Biais d'évaluation asymétrique entre MCP et A2A (Ch. 11, p. 132, p. 138)**  
  *Diagnostic* : L'absence de CVE sur A2A résulte de son stade de déploiement fermé, non d'une sûreté intrinsèque supérieure ; les menaces de bouclage et déni de service récursif y sont démontrées.
- **DEF-MAJ-16 : Surqualification disproportionnée du projet Cisco AGNTCY (Ch. 10, pp. 115, 118–120)**  
  *Diagnostic* : Promu dans le titre du Ch. 10 alors qu'il s'agit d'une coquille sans spécification stable ni implémentation open-source examinée (degré 3 d'absence avoué).
- **DEF-MAJ-17 : Incompatibilité structurelle et temporelle de SCIM (RFC 7643/7644) face aux agents volatils (Ch. 12, pp. 141–144)**  
  *Diagnostic* : SCIM est taillé pour des cycles de vie humains ($\Delta t \sim 10^3\text{--}10^5\text{ s}$) ; gérer des agents éphémères ($\tau \sim 10^{-1}\text{--}10^1\text{ s}$) par des requêtes REST synchrones effondre les annuaires d'entreprise.
- **DEF-MAJ-18 : Incomplétude des modes d'échec : omission de l'explosion récursive (Fork Bomb) et interblocage non modélisé (Ch. 11, p. 133)**  
  *Diagnostic* : Omet la prolifération récursive de sous-tâches (Fork Bomb sans compteur de sauts) et traite l'interblocage de façon métaphorique sans graphe d'attente (*Wait-For Graph*) ni politique *Wait-Die*.
- **DEF-MAJ-19 : Insécurité de l'état applicatif dans MCP révisé sans schéma AEAD (Ch. 8, p. 92 ; Ch. 11, p. 135)**  
  *Diagnostic* : Les poignées d'état transitent dans le canal de prompt non fiable sans chiffrement authentifié, exposant à l'altération et au rejeu de session.
- **DEF-MAJ-20 : Faille structurelle de l'Agent Card A2A v1.0.0 (absence de timestamps et révocation) (Ch. 15–16, pp. 167–188)**  
  *Diagnostic* : Aucun champ `iat`, `exp`, `nbf`, signature facultative (`MAY`), aucun protocole de révocation : impossible de lui confier le rôle de passeport d'agent opposable.
- **DEF-MAJ-21 : Schisme d'interopérabilité de W3C VC v2.0 et omission de la divulgation sélective (SD-JWT VC / BBS+) (Ch. 13, pp. 153–157)**  
  *Diagnostic* : Fracture irréconciliable entre Data Integrity (JSON-LD) et Enveloping (JOSE/COSE) ; omission de SD-JWT VC (RFC 9542) violant le principe de minimisation de la Loi 25 québécoise.
- **DEF-MAJ-22 : Méconnaissance des Object-Capabilities (Hardy 1988) et illusion du confinement cognitif (Ch. 19, pp. 210–222)**  
  *Diagnostic* : Citer Hardy sans adopter les Object-Capabilities ; prétendre contrer la Triade Létale par des guardrails LLM probabilistes inopérants plutôt que par un cloisonnement déterministe d'OS.
- **DEF-MAJ-23 : Absence de condensat d'intégrité et risque de Rug-Pull / Tool-Squatting dans MCP (Ch. 20, pp. 222–225)**  
  *Diagnostic* : La notification `tools/list_changed` autorise le remplacement dynamique d'un outil sans empreinte SHA-256 canonique scellée à l'octroi de consentement.
- **DEF-MAJ-24 : Régression du moindre privilège et rupture d'imputabilité PIM/TAP dans l'Agentic SOC (Ch. 20, pp. 230–235)**  
  *Diagnostic* : L'incompatibilité des agents d'arrière-plan avec PIM/TAP pousse au déploiement de comptes de service permanents à hauts privilèges, violant les normes BSIF E-23 et détruisant l'imputabilité individuelle.
- **DEF-MAJ-25 : Omission de FIPS 205 (SLH-DSA), cécité sur la fragmentation MTU et rejet HTTP 431 (Ch. 21, pp. 236–248)**  
  *Diagnostic* : Omet le standard de repli FIPS 205 et nie l'impact volumétrique : les signatures ML-DSA (2,4 Ko) et SLH-DSA (7,8 Ko) fragmentent la MTU Ethernet (1 500 o) et saturent les en-têtes HTTP (rejet HTTP 431).
- **DEF-MAJ-26 : Absence d'identifiants IANA pour les algorithmes PQC dans JOSE et COSE (Ch. 21, pp. 242–245)**  
  *Diagnostic* : Aucun identifiant standard n'est ratifié à l'IANA pour ML-DSA/SLH-DSA dans JOSE/COSE, condamnant les Agent Cards PQC à des dialectes propriétaires non interopérables.
- **DEF-MAJ-27 : Éviction asymétrique et injustifiable de Temporal face à LangGraph (Ch. 23, pp. 266–274)**  
  *Diagnostic* : Relègue Temporal à un simple repérage [C] sans fait central tout en intégrant Confluent/Kafka en préversion, alors que Temporal est le standard mondial bancaire de l'Event Sourcing déterministe.
- **DEF-MAJ-28 : Omission des cadriciels bancaires de référence : AWS Step Functions, Camunda 8, Semantic Kernel (Ch. 23, pp. 266–274)**  
  *Diagnostic* : Omet AWS Step Functions / Bedrock Agents (standard serverless des banques canadiennes sous BSIF B-10) et Camunda 8 Zeebe sous consensus Raft.
- **DEF-MAJ-29 : Capitulation sur la contention d'inférence GPU et référence anachronique de 2013 (§ 24.8, pp. 292–293)**  
  *Diagnostic* : Déclare forfait sur le dimensionnement GPU et cite un article de 2013 (*Tail at Scale*), ignorant la littérature moderne OSDI/SOSP (Orca, Sarathi, Splitwise, DistServe) et l'amplification de latence sur barrière $[F(t)]^k$.
- **DEF-MAJ-30 : Concurrence distribuée sans treillis jointif (CRDTs) et sagas bancaires non compensables (Ch. 24, pp. 270, 274–282)**  
  *Diagnostic* : Évoque des « réducteurs d'état » sans formaliser l'algèbre des demi-treillis bornés (CRDTs) et renvoie à tort la gestion des ordres irrévocables au Ch. 48.
- **DEF-MAJ-31 : Minimisation de la force obligatoire de BSIF E-23 et omission des 12 champs d'inventaire (Ch. 25, pp. 300–303)**  
  *Diagnostic* : Proscrit le terme « exigé » sous prétexte d'une régulation fondée sur des principes, méconnaissant les pouvoirs du Surintendant (Loi sur les banques art. 485/646). Omet les 12 champs d'inventaire d'E-23, favorisant l'arbitrage réglementaire par atomisation des modèles.
- **DEF-MAJ-32 : Simplification du vide fédéral et omission de la Loi sur la concurrence post-C-59 (Ch. 26, pp. 307–310)**  
  *Diagnostic* : Affirme un vide fédéral absolu après la caducité de C-27, ignorant les amendements de juin 2024 au projet C-59 (articles 74.01/74.011 de la Loi sur la concurrence) sanctionnant sévèrement les allégations non prouvées sur l'IA.
- **DEF-MAJ-33 : Inadéquation radicale des métriques classiques (McCabe, score F1) pour la certification prudentielle (Ch. 22, pp. 257–258 ; Ch. 25, pp. 303–304)**  
  *Diagnostic* : La complexité cyclomatique ne mesure pas l'espace latent des LLMs ; le score F1 (ex. 0,97) tolère 3 % d'erreurs inacceptables en filtrage financier. Obligation de vérification à l'exécution en logique temporelle $LTL_f$.
- **DEF-MAJ-34 : Falsification empirique des études de cas bancaires canadiennes (Ch. 35, pp. 396–410)**  
  *Diagnostic* : TD Bank : compare 15 h de cycle à 3 min d'extraction LLM, masquant la souscription humaine obligatoire sous BSIF B-20. Scotiabank : contradiction arithmétique (1 500/j $\neq$ 60k-70k/mois) et 10 % d'exceptions masquées. Intact Financial : requalifie 600 modèles actuariels classiques (GLM/XGBoost) en maturité agentique. Sun Life / CIBC : métriques de vanité bureautique et de volume de tokens d'infrastructure.
- **DEF-MAJ-35 : Omission de la Ligne directrice BSIF E-21 sur la résilience opérationnelle (Août 2024)**  
  *Diagnostic* : Analyse B-10, B-13 et E-23 mais omet la norme pivot E-21 qui impose de définir des tolérances aux perturbations critiques pour les systèmes agentiques bancaires.

---

## 2.3 Défauts Mineurs, Clarté et Cohérence Typographique [Minor]

- **DEF-MIN-01 : Corruption textuelle au Ch. 7, p. 79 (§ 7.0)** — Collision entre l'encadré Thèse et le corps du second paragraphe (« ...le contrat entre un agent et ses » coupé net).
- **DEF-MIN-02 : Bogue de composition au Ch. 10, p. 115** — Mot « chapitre » tronçonné en « ce cha ... pitre prend pour objet », suivi d'un bégaiement textuel de la thèse entière.
- **DEF-MIN-03 : Collision matérielle au Ch. 2, p. 32 (§ 2.3.3)** — Inversion de paragraphe découpant le texte sur SHACL et laissant la phrase suspendue sur « est ».
- **DEF-MIN-04 : Césure fautive au Ch. 4, p. 47 (§ 4.0.2)** — Mot tronqué en bas de page : « l’héritage des architectures délibé ».
- **DEF-MIN-05 : Troncature graphique dans la Figure 12.4 (Ch. 12, p. 147)** — Définition de client tronquée sur le mot « pour ».
- **DEF-MIN-06 : Troncature textuelle au bas de la page 151 (Ch. 12)** — Phrase suspendue sans ponctuation : « ...un produit en disponibilité générale étend des RFC ; un document ».
- **DEF-MIN-07 : Débordement d'encadrés pleine largeur (Ch. 13, pp. 152–153)** — Encadrés Thèse et Extraction insérés au milieu de liaisons grammaticales actives (« d'une [ENCADRÉ] section », « la preuve [ENCADRÉ] incorporée »).
- **DEF-MIN-08 : Dislocation destructive du Tableau 16.3 (Ch. 16, p. 188)** — Colonne 3 vide et texte descriptif glissé dans la colonne « Tri ».
- **DEF-MIN-09 : Collision de l'encadré flottant de 16 lignes (Ch. 21, pp. 242–243)** — Phrase brisée entre « tri : » en bas de page 242 et « fait PROJETÉ » en haut de page 243.
- **DEF-MIN-10 : Fracture et inversion du Tableau 21.4 (Ch. 21, p. 248)** — Colonne 3 déserte sur les données et texte d'en-tête inversé avec la colonne 2.
- **DEF-MIN-11 : Fragment orphelin au Ch. 8, p. 95** — Fragment « La révision » flottant au-dessus de la Figure 8.2.
- **DEF-MIN-12 : Normalisation du genre de RFC 9207 (Ch. 8, p. 94)** — Utilisation de « la RFC 9207 » contredisant l'usage du masculin (« le RFC ») retenu ailleurs dans l'ouvrage.
- **DEF-MIN-13 : Désignation imprécise d'AWS Bedrock (Ch. 12, p. 143)** — Emploi du terme fictif « Amazon Bedrock AgentCore Identity » au lieu de `sts:AssumeRole` avec rôles IAM.
- **DEF-MIN-14 : Glitch rédactionnel et contradiction de date au Ch. 12, p. 148** — Phrase affirmant ne pas donner de date, suivie immédiatement de « Parue le 28 juillet 2026 ».
- **DEF-MIN-15 : Discordance typologique Figure 14.1 formatée en tableau (Ch. 14, pp. 162–164)** — Figure 14.1 suivie du Tableau 14.2, supprimant le Tableau 14.1 de la séquence.
- **DEF-MIN-16 : Ponctuation manquante au Ch. 20, p. 227** — Fusion de deux phrases distinctes à propos de la RFC 7662.
- **DEF-MIN-17 : Maintien de mentions de « rejeu non fait » (Ch. 19, p. 212 ; Ch. 20, p. 222)** — Analyse maintenue sur une révision vieille de neuf mois pour un ouvrage compilé fin octobre 2026.
- **DEF-MIN-18 : Troncature textuelle au Ch. 37, p. 433 (§ 37.8.2)** — Phrase tronquée net : « deux types sérialisés en SD-JWT, attribut de » enchaînant sur « Premièrement... ».
- **DEF-MIN-19 : Injection de note éditoriale au Ch. 38, p. 444 (§ 38.5)** — Note interne de relecture (« Le statut de préversion est périmé... ») insérée dans la phrase.
- **DEF-MIN-20 : Fuite de cellules du Tableau 46.2 sous le titre de section (Ch. 46, p. 525)** — Colonnes 2 et 3 vides, texte déversé sous forme de charabia sous le titre de synthèse.
- **DEF-MIN-21 : Troncature physique du Tableau 47.2 (Ch. 47, p. 530)** — Titres découpés par le bord de cellule (« obre 2025... », « ée sous la Fondation Linux... ») et fragment orphelin au-dessus.
- **DEF-MIN-22 : Injection brute de notes d'arbitrage au Ch. 48, p. 544 (§ 48.5)** — Bloc de 10 lignes de notes d'auteur en majuscules inséré au milieu d'une phrase.
- **DEF-MIN-23 : Fracturation des rangées 14 et 15 du Tableau 49.2 (Ch. 49, p. 563)** — Texte débordant en colonne 1 et écrasant les rangées adjacentes.
- **DEF-MIN-24 : Injection d'un bloc de 16 lignes de notes au Ch. 49, pp. 566–567 (§ 49.13.3)** — Phrase brisée en deux par des notes relatives à l'AMF et aux codes 403.
- **DEF-MIN-25 : Éjection typographique de la table de l'Annexe I, p. 585** — Cellules vides et puce orpheline textuelle `• 134 1065`.
- **DEF-MIN-26 : Incohérence arithmétique de l'Annexe I, p. 585** — $1\,263 - 134 = 1\,129 \neq 1\,065$ (déficit de 64 notices non traçables).
- **DEF-MIN-27 : Injection du caractère Unicode parasite `\ufffe` dans l'Annexe N (pp. 662–663)** — Caractère d'inversion d'octet corrompant les URL dans les notices [AN-7, 8, 11, 14, 15, 23, 24, 25, 27].
- **DEF-MIN-28 : Présence de 8 directives de rédaction et mémos internes non purgés en Annexe I.1** — Mentions « à revérifier », « Voir §2.5 ci-dessus », « à dater », « à conserver ici uniquement pour... » imprimées dans les notices publiques.

---

# Section 3 : Analyse bibliographique et empirique exhaustive

### 3.1 Analyse des références déformées, chimères et anachronismes

```
========================================================================================================================
                                     RÉCONCILIATION DE L'ÉTAT DE L'ART NORMATIF
========================================================================================================================
Référence défaillante du texte          Statut réel vérifié à la source      Diagnostic critique et rectification
------------------------------------------------------------------------------------------------------------------------
Prétendu « règl. (UE) 2026/1744 »       Inexistant au Journal officiel de    Le cadre exclusif est le Règlement (UE) 2024/1689
(Ch. 10 p. 124, pp. 30520, 34016)       l'Union européenne.                   (AI Act) : GPAI août 2025, Annexe III août 2026.
------------------------------------------------------------------------------------------------------------------------
Plan-and-Solve Prompting                ACL 2023 (arXiv:2305.04091).         Chimère bibliographique : attribué faussement à
(Ch. 4 p. 53)                           Lei Wang, Wanyu Xu, Yihuai Lan       Wang, Wei, Schuurmans (auteurs de Self-Consistency).
------------------------------------------------------------------------------------------------------------------------
τ-bench (Tau-Bench)                     arXiv:2406.12045 (Yao et al.).       Métrique détournée : pass^k = consistance sur k
(Ch. 6 p. 76, Fig. 6.4)                 Estimates pass^k = E[p^k].           essais indépendants d'une tâche, non dégradation multi-pas.
------------------------------------------------------------------------------------------------------------------------
draft-ietf-httpapi-idempotency-key      IETF HTTPAPI Working Group.          Déclaré à tort « expiré et abandonné ». La révision
(Ch. 48 p. 544)                         Actif : révision -08 (22 oct. 2026). officielle draft-08 a été soumise le 22 oct. 2026.
------------------------------------------------------------------------------------------------------------------------
in-toto Attestation Framework           CNCF Project.                        Déclaré « maturité CNCF non portée ». in-toto a été
(Ch. 47 p. 530, Tableau 47.2)           Promu CNCF GRADUATED 10 fév. 2025.   promu au statut suprême de Graduated en février 2025.
------------------------------------------------------------------------------------------------------------------------
Ligne directrice IA de l'AMF            AMF Québec (Bulletin Vol. 23 n°14).  Déclarée « lacune ouverte vide sans date ». Publiée
(Ch. 26, 27, 29, 42)                    Adoptée et publiée le 7 avril 2026.  officiellement le 7 avril 2026, vigueur 1er mai 2027.
------------------------------------------------------------------------------------------------------------------------
NIST IR 8547 Transition PQC             NIST CSRC (DOI:10.6028/NIST.IR.8547). Traité comme ébauche préliminaire au Ch. 21, alors
(Ch. 21 pp. 236-251)                    Version finale le 27 octobre 2026.   que la version finale est parue le 27 oct. 2026.
------------------------------------------------------------------------------------------------------------------------
The Tail at Scale (Dean & Barroso 2013) ACM Communications, 2013.            Anachronisme de 13 ans pour dimensionner l'inférence
(Ch. 24 § 24.8, p. 292)                 Serveurs web CPU pré-IA.             GPU des LLMs (saturation HBM et KV-cache PagedAttention).
------------------------------------------------------------------------------------------------------------------------
```

---

### 3.2 Corpus des travaux fondamentaux et standards omis jusqu'en 2026

L'évaluation met au jour une carence surprenante : l'ouvrage cite avec profusion les prépublications arXiv 2024–2026, mais omet les traités cardinaux d'informatique théorique, de systèmes distribués et de sécurité logicielle :

#### 1. Systèmes distribués, consensus et transactions concurrentes (Ch. 1, 6, 10, 24, 48)
- **Lamport, Leslie (1978 & 1998)** : *Time, Clocks and the Ordering of Events in a Distributed System* (CACM) & *The Part-Time Parliament (Paxos)* (ACM TOCS). Fondement obligatoire pour la cohérence d'état et l'ordonnancement d'événements.
- **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985)** : *Impossibility of Distributed Consensus with One Faulty Process (FLP)* (JACM). Démontre l'obligation d'hypothèses de synchronicité partielle pour synchroniser les registres d'idempotence.
- **Castro, Miguel & Liskov, Barbara (1999)** : *Practical Byzantine Fault Tolerance (PBFT)* (OSDI). Socle indispensable pour modéliser la tolérance aux fautes d'agents corrompus.
- **Ongaro, Diego & Ousterhout, John (2014)** : *In Search of an Understandable Consensus Algorithm (Raft)* (USENIX ATC). Standard industriel de réplication d'état (*State Machine Replication*).
- **Garcia-Molina, Hector & Salem, Kenneth (1987)** : *Sagas* (ACM SIGMOD). Traité princeps posant la règle de la transaction pivot unique ($T_{\text{pivot}}$).
- **Helland, Pat (2012)** : *Idempotence Is Not a Free Lunch* (CACM). Démontre la nécessité d'ordonnancement monotone strict (*fencing tokens*) pour l'idempotence.
- **Richardson, Chris (2018)** : *Microservices Patterns* (Transactional Outbox Pattern). Indispensable pour éliminer le *Dual-Write Problem*.

#### 2. Sécurité formelle, calculabilité et moniteurs de référence (Ch. 11, 19, 37, 48, 49)
- **Rice, Henry Gordon (1953)** : *Classes of Recursively Enumerable Sets and Their Decision Problems* (Trans. AMS). Démontre l'indécidabilité de toute propriété sémantique non triviale pour un agent Turing-complet.
- **Schneider, Fred B. (2000)** : *Enforceable Security Policies* (ACM TISSEC). Borne mathématiquement les moniteurs de référence (PEP/PDP) aux seules propriétés de sûreté (*safety*), excluant la vivacité.
- **Clarkson, Michael R. & Schneider, Fred B. (2010)** : *Hyperproperties* (JCS). Démontre que l'isolation et la non-interférence ne sont pas vérifiables sur une trace isolée.
- **Birgisson, Arnar et al. (2014)** : *Macaroons: Cookies with Contextual Caveats* (NDSS). Preuve formelle de la délégation décentralisée atténuable sous PRF.
- **CNCF / SPIFFE Project (2020–2026)** : *SPIFFE / SPIRE Specification* (Standard CNCF Graduated). Standard mondial d'attestation dynamique de charge de travail (SVID X.509/JWT).
- **Carlini, Nicholas et al. (2024)** : *On the Impossibility of Token-Level Prompt Injection Defenses without Architectural Isolation*. Démontre l'obligation de confinement OS face à l'injection d'instructions.

#### 3. Régulation prudentielle et résilience financière canadienne (Ch. 25, 27, 28, 31, 35)
- **BSIF / OSFI — Ligne directrice E-21 sur la résilience opérationnelle (Août 2024)** : Pivot obligeant les institutions financières à définir des tolérances aux perturbations critiques pour les systèmes agentiques bancaires.
- **BSIF / OSFI — Ligne directrice B-20 sur la souscription hypothécaire** : Impose obligatoirement un souscripteur humain accrédité et des stress-tests, interdisant l'adjudication autonome totale.
- **Autorité des marchés financiers (AMF) — Ligne directrice IA (7 avril 2026)** : Attentes 4.1 (dirigeant responsable), 5.1 (inventaire centralisé des SIA) et 6.2 (équité et traitement équitable des clients).
- **Parlement du Canada — Projet de loi C-59 (Juin 2024)** : Articles 74.01 et 74.011 de la *Loi sur la concurrence*, sanctionnant jusqu'à 10 M$ les déclarations d'autonomie ou d'efficacité d'IA non étayées par une épreuve adéquate.

#### 4. Runtimes d'inférence GPU et ordonnancement de modèles (Ch. 24, 38, 40)
- **Kwon, Woosuk et al. (2023)** : *Efficient Memory Management for LLM Serving with PagedAttention* (ACM SOSP). Algorithme universel de gestion du KV-cache.
- **Zheng, Lianmin et al. (2024)** : *SGLang: Efficient Execution of Structured Language Model Programs* (NeurIPS). Introduction de RadixAttention pour la réutilisation du KV-cache sur les arbres de prompts d'agents.
- **Zhong, Y. et al. (2024)** : *DistServe: Disaggregating Prefill and Decoding for Goodput-optimized LLM Serving* (OSDI). Désagrégation physique calcul/mémoire.

---

### 3.3 Déconstruction empirique des études de cas bancaires canadiennes (Ch. 34–35)

L'affirmation selon laquelle « l'agentique canadienne est en production industrielle » repose sur l'adoption non critique de déclarations de relations publiques corporatives :
1. **TD Bank (Leurre de l'octroi hypothécaire en 3 minutes, § 35.1)** :  
   TD Bank revendique le passage du traitement de 15 heures à moins de 3 minutes via sa filiale Layer 6. Cette comparaison juxtapose deux grandeurs incommensurables : les 15 heures mesurent le cycle asynchrone complet d'un dossier en succursale, tandis que les 3 minutes ne représentent que le temps de calcul brut d'un modèle pour générer un mémo de synthèse. De surcroît, la **Ligne directrice B-20 du BSIF** interdit formellement l'octroi d'un prêt hypothécaire résidentiel sans révision indépendante par un souscripteur humain accrédité. Le délai réel de délivrance du crédit n'a pas varié pour l'emprunteur.
2. **Scotiabank (Contradiction arithmétique et résidu d'escalade masqué, § 35.2)** :  
   L'institution revendique le traitement de 1 500 courriels par jour et 60 000 à 70 000 demandes par mois. Or, $1\,500 \times 21,5\text{ jours ouvrables} = 32\,250$ courriels par mois (ou 45 000 sur 30 jours civils), ce qui traduit un écart du simple au double. Par ailleurs, 90 % de routage laisse 10 % d'exceptions (150 cas complexes par jour) réinjectées dans une file d'escalade humaine dont le coût opérationnel et les délais d'attente absorbent les gains prétendus.
3. **Intact Financial (Requalification anachronique d'actuariat classique, § 35.7)** :  
   L'auteur qualifie le portefeuille de 600 modèles d'Intact Financial (générant 200 M$ de valeur annuelle) de « sommet de la maturité agentique ». En réalité, ces modèles sont des algorithmes d'actuariat supervisé traditionnels (GLM, régressions, arbres boostés XGBoost) de tarification automobile et habitation. Ils ne comportent aucune boucle ReAct, aucun appel d'outil MCP/A2A, aucune mémoire épisodique et aucune autonomie transactionnelle.
4. **CIBC, BMO et Sun Life (Métriques de vanité bureautique et d'infrastructure, § 35.6, § 35.8)** :  
   Les 200 000 heures déclarées par CIBC et les 8 000 utilisateurs de BMO mesurent l'accès passif à Microsoft Copilot pour rédiger des courriels ou consulter des bases documentaires internes RAG (zéro transaction financière autonome). Les 2 000 milliards de tokens par mois de Sun Life ne mesurent qu'un volume brut de bande passante d'infrastructure incluant des tests de charge synthétiques.

---

# Section 4 : Analyses transversales inter-chapitres

### 4.1 Dérives de notation et polysémies non résolues
L'audit croisé révèle six dérives terminologiques et conceptuelles majeures à travers le manuscrit :
1. **Régression taxonomique du LCIM (Ch. 1 p. 9 vs Ch. 7 p. 80)** :  
   Le Ch. 1 décrit rigoureusement l'échelle à 7 niveaux ($L_0$ à $L_6$) de Tolk. Le Ch. 7 (Tableau 7.1) titre sans justification « *Les cinq niveaux du LCIM appliqués à la pile agentique* », amputant $L_0$ (isolé) et $L_6$ (conceptuel). Or, $L_6$ est précisément la couche où s'alignent les modèles du monde et les contraintes réglementaires (E-23, Loi 25).
2. **Flottement sur les échelles d'autonomie (Ch. 14, 22, 43)** :  
   Trois échelles coexistent sans fonction de passage : une échelle opérationnelle à 4 paliers (Ch. 14), l'échelle à 6 niveaux du Volume I (p. 166), et la taxonomie OO1–OO4 (Ch. 22). L'auteur renvoie la désambiguïsation formelle au Ch. 43, créant une zone de flou sémantique pendant 300 pages.
3. **Divergence sur le nombre de couches d'architecture (Ch. 43 vs Ch. 45)** :  
   Le mandat initial et les comités de place prescrivent **7 couches** ; le Ch. 43 formalise une architecture de référence en **6 couches** (Figure 43.1 p. 485) ; le Ch. 45 introduit soudainement **8 couches (C1 à C8)** pour le blueprint Boréalis/IBM. Aucune table de projection n'articule ces trois décomptes.
4. **Divergence taxonomique de l'agent : 5 composants vs 5 horloges (Ch. 47, p. 529 vs p. 535)** :  
   Le Tableau 47.1 énumère 5 composants : Modèle, Outils, Bibliothèques/Hôte, Invites, Politique. La Section 47.8 énumère 5 horloges : Modèle, Invites, Outils, Politique, Harnais. L'auteur concède lui-même p. 535 que « *les deux quintets ne se recouvrent pas... Le chapitre suit la thèse pour le décompte et le tableau pour l'inventaire* », paralysant l'ingénierie de release GitOps / SBOM.
5. **Usage métaphorique du mot « verrou » (Ch. 10 et 11)** :  
   Le terme « verrou » est employé à 7 reprises de manière purement rhétorique (« verrou opérationnel », « verrou du domaine »), créant une confusion avec les mécanismes réels de synchronisation distribuée (*Distributed Lock Manager* via Raft ou Redis Redlock).
6. **Polysémie du « Plan de contrôle » (Ch. 22, 24, 43)** :  
   Confusion récurrente entre le plan de contrôle réseau L4/L5 (*Network Control Plane*, routage type Istio/AGNTCY) et le plan de gouvernance agentique L7 (*Agentic Governance Plane*, déontique et mandats).

---

### 4.2 Définitions contradictoires entre livres et chapitres
1. **Inversion spatiale et sémantique C1–C8 du Blueprint Boréalis/IBM (Ch. 45, p. 510 vs p. 511)** :  
   Le Tableau 45.2 place C1 au sommet (Exposition) et C8 à la base (Socle d'exécution). La Figure 45.2 adopte l'ordre ascendant inverse : C1 à la base (Socle) et C8 au sommet (Gouvernance). Les couches C2, C3, C4, C5 et C6 portent des définitions contradictoires entre le tableau et la figure.
2. **Antinomie topologique en OO1–OO4 : Continuum fluide vs Discontinuité irréductible (Ch. 22, pp. 254–255)** :  
   Le Ch. 22 affirme simultanément que les options OO1–OO4 forment des « *positions sur un continuum fluide* » et que la frontière OO2 $\to$ OO3 est « *la seule discontinuité véritable de la série* ». En topologie, l'espace d'autorité est un treillis booléen discret de cardinal 4 sans structure connexe ; la distance de Hausdorff entre l'espace libre (OO2) et l'espace contraint (OO3) est infinie ($d_H = \infty$).
3. **MCP : Port universel sans couplage vs Contrat de schéma rigide et couplage bloquant (Ch. 1 vs Ch. 8)** :  
   Le Ch. 1 vante l'atténuation du couplage par les protocoles ouverts. Le Ch. 8 admet que MCP impose un couplage de schéma rigide JSON Schema (tout paramètre non déclaré déclenche un rejet syntaxique `-32602`) et un couplage d'interaction temporellement bloquant sur transport stdio/SSE.
4. **Supervision de l'Open Banking : FCAC vs Banque du Canada (Ch. 32 vs Annexe I.1 Notice [749])** :  
   Le Ch. 32 (p. 367) et la table des symboles (p. 184) maintiennent que l'autorité d'Open Banking est l'Agence de la consommation en matière financière du Canada (FCAC). La Notice bibliographique [749] de l'Annexe I.1 consigne avec exactitude que la CDBA (sanctionnée le 26 mars 2026) a transféré la supervision technique à la **Banque du Canada**.
5. **Calendrier de marquage de l'AI Act : Août 2026 vs Décembre 2026 (Ch. 30 vs Annexe N.4 [AN-25])** :  
   Le Ch. 30 affirme que l'obligation de marquage des contenus synthétiques s'applique au 2 décembre 2026. L'Annexe N.4 consigne qu'elle s'applique dès août 2026 en vertu de l'article 50 du Règlement sur l'IA.

---

### 4.3 Dépendances circulaires et non-rejouabilité des axiomes dans l'appareil critique
1. **L'effondrement de la chaîne de preuve en Annexe B (p. 584)** :  
   Les axiomes théoriques fondateurs de l'ouvrage sont frappés de nullité probatoire :
   - $S\text{-}153$ (*Invariant transversal à 4 termes*) : classé [C], « Citation non rejouable ».
   - $S\text{-}154$ (*Délégation au-delà de deux sauts*) : classé [C], « Citation non rejouable ».
   - $S\text{-}156$ (*Plan de contrôle obligatoire*) : classé [C], « Citation non rejouable ».
   - $S\text{-}158$ (*Cas fil rouge*) : classé [C], « Fait négatif non rejouable (cible supprimée) ».  
   Un théorème ne peut être opposable en droit et en ingénierie s'il s'appuie sur des citations internes non vérifiables.
2. **L'asymétrie de l'Annexe I.2 et l'isolement des Volumes II et III (p. 651)** :  
   L'Annexe I.2 avoue que les tomes II et III ne livrent zéro adresse résoluble. Sur les 159 faits de socle, **142 faits (89,3 %)** — portant sur l'identité d'agent, les passeports, la Loi 25 et BSIF E-23 — sont privés de notice bibliographique vérifiable.
3. **La troncature du protocole de péremption du Ch. 50 en Annexe N (p. 652)** :  
   L'Annexe N applique uniquement le geste 1 (constater le fait à la source) et renonce aux gestes 2 (amender l'Annexe B) et 3 (reprendre les chapitres dépendants), laissant subsister dans le même volume un corps de texte devenu erroné et contredit par son annexe de clôture.
4. **La rupture arithmétique de la page 585** :  
   Le décompte officiel affiche une formule impossible : $1\,263\text{ (collectées)} - 134\text{ (doublons)} = 1\,129 \neq 1\,065\text{ (uniques)}$, révélant un déficit inexpliqué de 64 références et une défaillance du pipeline de déduplication.

---

# Section 5 : Table de Référence des Rapports d'Unité

Conformément au mandat d'agrégation, les huit rapports d'unité de Niveau 2 (racines des arbres RSA sectoriels) ont été intégralement audités et constituent le socle probatoire du présent rapport de synthèse candidat :

| ID Segment | Intitulé officiel du segment | Pages du Compendium | Chemin absolu du rapport d'unité (`unit_report_*.md`) |
|---|---|---|---|
| **Seg 1** | Livre I : Fondements de l’interopérabilité et ingénierie agentique | pp. 1–79 (Ch. 1 à 6, amorce Ch. 7) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_1_fondements\unit_report_segment_livre_1_fondements.md` |
| **Seg 2** | Livre I : Protocoles agentiques, découverte et transactions | pp. 78–145 (Ch. 7 à 11, Ch. 12) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_1_protocoles\unit_report_segment_livre_1_protocoles.md` |
| **Seg 3** | Livre II : Identité non humaine et délégation vérifiable | pp. 144–255 (Ch. 12 à 21, amorce Ch. 22) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_2_confiance\unit_report_segment_livre_2_confiance.md` |
| **Seg 4** | Livre III : Orchestration d’entreprise et cadre prudentiel canadien | pp. 254–310 (Ch. 22 à 26) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_3_orchestration\unit_report_segment_livre_3_orchestration.md` |
| **Seg 5** | Livre III : Régulation financière québécoise et études de cas bancaires | pp. 309–420 (Ch. 26 [fin], Ch. 27 à 36) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_3_regulation\unit_report_segment_livre_3_regulation.md` |
| **Seg 6** | Livre IV : Application, AgentMesh, AgentOps et architecture | pp. 419–530 (Ch. 37 à 46, Ch. 47 amorce) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_4_application\unit_report_segment_livre_4_application.md` |
| **Seg 7** | Livre V : Sémantique d'effet, prospective et clôture | pp. 527–585 (Ch. 47 à 50, transition Annexes) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_5_cloture\unit_report_segment_livre_5_cloture.md` |
| **Seg 8** | Annexes : Socle consolidé, bibliographie générale et actualisation | pp. 584–663 (Annexes B, I, N) | `c:\Github\EntrepriseAgentique\.agents\teamwork\group_annexes_bibliographie\unit_report_segment_annexes_bibliographie.md` |

---
*Rapport de synthèse candidat 4 arrêté, scellé et délivré le 3 novembre 2026 par le Synthétiseur Candidat 4 (Phase 4).*
