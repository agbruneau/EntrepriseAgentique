**Segment scope**: Audit contradictoire et synthèse de niveau 1 (L1_2) pour le segment `segment_livre_3_regulation` (Pages 309 à 420, Chapitres 26 [clôture], 27 à 36), intégrant l'encadrement réglementaire financier (Loi 25 art. 12.1, Ligne directrice AMF IA, Avis ACVM 11-348, BSIF E-23, vide fédéral C-27/C-36), la falsification formelle du prétendu pont vers les automates finis déterministes (Ch. 29), l'audit des protocoles transactionnels (ISO 20022, Lynx, RTR, AP2) et l'évaluation critique empirique des études de cas bancaires canadiennes (Ch. 35).

# Potential Mistakes and Improvements

### [Critical] Falsification mathématique du « pont déterministe » (Ch. 29) — Absence d'automate fini déterministe (DFA), vice de composition stochastique, carence d'états puits ($q_{sink}$) et blocages réactifs (*deadlocks*)
- **Localisation précise :** Chapitre 29, pages 327 à 335 (§ 29.0, Tableau 29.1 pp. 327-328, Figure 29.1 p. 331, § 29.4 pp. 333-334, § 29.4.1 pp. 334-335).
- **Citations textuelles fidèles :**
  > *Page 327 :* « Traduire une exigence juridique en contrainte d’architecture n’est pas une opération de lecture : c’est un raisonnement d’auteur, qui engage la somme et non le régulateur. Le lecteur trouvera donc ici plus d’inférences marquées que partout ailleurs dans le Livre [...] Et la somme n’émet aucun avis juridique. »  
  > *Page 334 :* « Sous exigence réglementaire stricte, le processus est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n’orchestrent pas le processus. Dans le vocabulaire des options d’orchestration du ch. 22 § 22.1, ce sont les positions OO3 et OO4... »  
  > *Page 335 :* « Le pont du Livre n’est donc pas une déduction. C’est un raisonnement, exposé pour être contesté... »
- **Diagnostic causal approfondi :**  
  Le compendium opère une confusion conceptuelle entre la topologie statique d'un graphe de contrôle (workflow DAG de niveau OO3 ou OO4) et le déterminisme de l'exécution d'un système. L'inspection visuelle rigoureuse de la Figure 29.1 (`page-331.png`) et du corps du texte confirme qu'aucun modèle formel d'automate fini n'est formulé : le terme même d'« automate » n'apparaît à aucun moment dans le chapitre 29. L'auteur substitue à une démonstration mathématique un tableau qualitatif d'ingénierie logicielle (Tableau 29.1) fondé sur des inférences d'auteur non démontrées.
- **Démonstration mathématique et falsification formelle :**
  1. *Inexistence du modèle d'automate :* Un automate fini déterministe (DFA) est formellement défini par le quintuplet $M = (Q, \Sigma, \delta, q_0, F)$, où $Q$ est l'ensemble fini des états, $\Sigma$ l'alphabet fini des symboles d'entrée, $\delta : Q \times \Sigma \to Q$ la fonction de transition totale, $q_0 \in Q$ l'état initial, et $F \subseteq Q$ l'ensemble des états acceptants. Le compendium ne spécifie aucun de ces éléments constitutifs.
  2. *Vice de composition stochastique (The Compositionality Fallacy) :* En position OO3/OO4, le cadre ordonnance des étapes qui invoquent des agents logiciels autonomes alimentés par des modèles de fondation probabilistes (LLM). La sortie d'un agent pour une tâche $T$ à l'état $q_i$ est une variable aléatoire $Y \sim \mathbb{P}_\theta(Y \mid X)$. Si la transition vers l'état suivant dépend d'une garde sémantique conditionnelle $g(Y) \in \{0, 1\}$ (par exemple l'évaluation d'un critère d'admissibilité au crédit), la transition d'état devient intrinsèquement stochastique :
     $$\mathbb{P}(q_{t+1} = q_{succ} \mid q_t = q_i) = \mathbb{E}_{Y \sim \mathbb{P}_\theta}[\mathbb{I}(g(Y) = 1)] \neq 1$$
     Par conséquent, encapsuler des agents stochastiques dans un ordonnanceur séquentiel ne produit en aucun cas un automate déterministe, mais un processus décisionnel markovien (MDP) ou un automate stochastique. La fixité du graphe ne garantit ni la reproductibilité de l'état d'arrivée ni l'absence de bifurcations erronées.
  3. *Absence d'états puits d'absorption sécurisée ($q_{sink}$) :* Dans tout automate régissant des décisions réglementées, toute dérive sémantique, hallucination ou entrée non conforme doit déterministement router le système vers un état puits d'arrêt sécurisé :
     $$\forall \sigma \notin \Sigma_{valide}, \quad \delta(q, \sigma) = q_{sink}, \quad \text{avec } \delta(q_{sink}, \cdot) = q_{sink}$$
     Faute de définir un tel état puits et son protocole d'escalade immuable, les défaillances de l'agent entraînent un comportement d'exécution indéfini (*undefined execution path*).
  4. *Blocage réactif (*Deadlock*) et rupture temporelle :* L'introduction de points d'arrêt humains (« libération humaine », révision art. 12.1) transforme l'automate en un système réactif ouvert. Si l'humain n'intervient pas, le système entre dans un état d'attente bloquant ($q_{\text{wait\_human}}$). En l'absence de spécification déterministe d'un délai d'attente borné ($\tau > \tau_{\max}$) associé à une compensation et à la libération des verrous de fonds, le système subit un gel d'instance indéfini, incompatible avec les exigences de temps de traitement des rails financiers instantanés (RTR).
- **Correctif recommandé :**  
  Bannir toute allégation selon laquelle le cadre OO3/OO4 réalise un « pont mathématique déterministe ». Requalifier l'architecture en « moteur d'orchestration statique sous politique d'enveloppe de sécurité (*runtime policy enforcement*) ». Spécifier formellement le quintuplet du DFA au niveau de la couche d'orchestration, avec typage strict des transitions par grammaires formelles (JSON-Schema / EBNF), définition explicite de l'état puits $q_{sink}$ d'interruption et gestion bornée des temporisations (*timeouts*) pour toute intervention humaine.

---

### [Critical] Amputation délibérée de 40 % des obligations de l'article 12.1 de la Loi 25 québécoise dans la matrice d'architecture logicielle (Ch. 29)
- **Localisation précise :** Chapitre 27, page 315 (§ 27.2) et Chapitre 29, pages 328 à 330 (§ 29.1, Tableau 29.1, page 329).
- **Citations textuelles fidèles :**
  > *Page 315 (Ch. 27 § 27.2) :* « Le décompte des obligations a été corrigé au socle [...] Le relevé du Vol. III, conduit sur le texte officiel le 21 juillet 2026, compte une obligation inconditionnelle, trois informations dues sur demande — dont la rectification —, plus un alinéa distinct portant l’occasion de présenter des observations (Vol. III F-89, [B]). »  
  > *Page 329 (Ch. 29 § 29.1) :* « Le décompte des obligations a été corrigé au socle [...] Deux de ces éléments — le 1° et le 3° — n’ont aucune ligne dans la table ci-dessus. La somme ne les y ajoute pas : ce chapitre est conservé intact, et dériver deux contraintes neuves serait le redécouper. »
- **Diagnostic causal approfondi :**  
  L'auteur a reconnu au chapitre 27 l'incomplétude de son décompte antérieur et a rétabli les cinq exigences formelles de l'article 12.1 de la *Loi sur la protection des renseignements personnels dans le secteur privé* (RLRQ c. P-39.1). Toutefois, parvenu au chapitre 29 qui synthétise les contraintes d'architecture logicielle, il refuse expressément d'insérer l'obligation 1° (communication des renseignements personnels précis utilisés) et l'obligation 3° (droit de faire rectifier les données utilisées) dans le Tableau 29.1, afin de maintenir artificiellement intact le découpage d'un texte rédigé antérieurement.
- **Falsification juridique et scénarios de défaillance logicielle :**  
  L'article 12.1 alinéa 2 prescrit que l'entreprise doit informer la personne concernée, à sa demande :
  - 1° des renseignements personnels utilisés pour rendre la décision ;
  - 3° de son droit de faire rectifier les renseignements personnels utilisés dans les cas prévus par la loi.  
  *Scénarios d'infraction caractérisée :*  
  1. *Violation du 1° (Traçabilité des données d'entrée) :* Dans un système agentique de crédit déployé selon le gabarit du Tableau 29.1, le cadre journalise la décision finale et les facteurs explicatifs macroscopiques, mais n'impose aucun mécanisme de capture immuable des données au moment exact de l'inférence (*input feature store snapshot hashing*). Lorsqu'un client exige la divulgation des données exactes ayant alimenté la décision, l'institution est incapable de reconstruire le vecteur d'entrée historique et viole directement le 1°.
  2. *Violation du 3° (Rétraction et propagation de la rectification) :* Le cadre n'implémente aucune primitive logicielle permettant de rétro-propager une rectification dans les bases vectorielles, les caches de contexte RAG ou la mémoire de session des agents (*vector retraction & cache invalidation*). L'agent continue d'opérer des inférences sur des données périmées ou inexactes, exposant l'institution aux sanctions pécuniaires administratives prévues par la Loi 25 (pouvant atteindre 25 M$ ou 4 % du chiffre d'affaires mondial).
- **Correctif recommandé :**  
  Rétablir sans concession la complétude réglementaire en insérant deux lignes dédiées dans le Tableau 29.1 :
  1. Pour l'art. 12.1 al. 2 1° : contraindre l'architecture à sceller un instantané cryptographique immuable des données d'inférence (`InputDataFingerprint`) stocké avec l'identifiant de décision.
  2. Pour l'art. 12.1 al. 2 3° : spécifier une primitive transactionnelle d'invalidation de mémoire contextuelle et de purge rétroactive des représentations vectorielles erronées.

---

### [Critical] Incompatibilité systémique des flux agentiques sur les rails souverains Lynx et RTR — Irréversibilité légale, échec structurel des Sagas et absence d'idempotence financière déterministe
- **Localisation précise :** Chapitre 31, pages 350-351 (§ 31.1.1) ; Chapitre 33, pages 372-377 (§ 33.1, § 33.2) ; Chapitre 36, pages 412-418 (§ 36.2.1, § 36.2.6, § 36.2.7).
- **Citations textuelles fidèles :**
  > *Page 350 (Ch. 31 § 31.1.1) :* « Le règlement financier possède une propriété que l’ingénierie d’intégration classique ne connaît qu’à la marge : la finalité [...] La saga compensatoire — qui suppose qu’une transaction distribuée s’annule en rejouant des compensations en sens inverse — échoue dès lors qu’un des effets de bord est irréversible. »  
  > *Page 415 (Ch. 36 § 36.2.6) :* « ...et sur les rails irréversibles, la rétrofacturation n’existe tout simplement pas [...] l’achat non intentionnel n’a pas d’espace où se défaire. »  
  > *Page 417 (Ch. 36 § 36.3) :* « Le socle ne porte pas l’anatomie technique du protocole : il en donne la fonction déclarée et rien de plus [...] Toute phrase décrivant comment un mandat de paiement agentique se traduirait en message de la couche sémantique serait une invention, et la somme n’en produira pas. »
- **Diagnostic causal approfondi :**  
  Le compendium identifie avec perspicacité la notion de « finalité » du règlement financier régie par la *Loi sur la compensation et le règlement des paiements* (LCRP) et le fait que les transactions compensatoires (Sagas) échouent sur les rails irréversibles. Néanmoins, au chapitre 36, il envisage le déploiement opérationnel d'agents sous protocole AP2 sur le rail de paiement en temps réel (RTR), sans fournir de cadre d'idempotence financière déterministe ni résoudre l'incompatibilité avec les règles d'accès de Paiements Canada.
- **Falsification algorithmique et financière :**
  1. *Scénario de tempête de réémissions (Retry Storm) et double débit irrévocable :*  
     Considérons un agent autonome exécutant un virement de fonds instantané sur RTR via un message ISO 20022 (`pacs.008`). Le rail effectue le règlement brut en temps réel de façon instantanée et irrévocable. En cas de timeout HTTP, de micro-coupure réseau ou de retard sur la confirmation d'état (`pacs.002`), la boucle de réessai de l'agent LLM se déclenche. Faute d'une couche d'idempotence externe qui force la réutilisation stricte de l'identifiant de transaction unique de bout en bout (`UETR` conforme RFC 4122) et du numéro d'instruction (`InstructionId`), l'agent génère une nouvelle instruction dotée d'un identifiant régénéré. Le rail RTR traite cette requête comme une opération distincte et débite une seconde fois le compte donneur d'ordre. Le règlement étant définitif sous l'empire de la LCRP, aucun mécanisme automatique de compensation inverse n'est opérant.
  2. *Obstacle légal de la Loi sur les paiements :*  
     Les règles de Paiements Canada et la *Loi sur les paiements* restreignent l'accès direct aux comptes de règlement sur Lynx et RTR aux seules institutions financières membres autorisées (banques à charte, coopératives centrales, Banque du Canada). Aucun agent logiciel autonome ne peut émettre de paiement en mode machine-à-machine (M2M) direct sans transiter par une interface bancaire d'initiation rigoureusement encadrée.
- **Correctif recommandé :**  
  Conclure formellement à l'inapplicabilité du patron Saga sur les rails de règlement brut en temps réel (RTGS/RTR). Interdire toute émission directe de messages de paiement par une boucle agentique stochastique. Imposer une passerelle d'idempotence financière déterministe (*Deterministic Payment Gateway*) interposée entre le système agentique et le connecteur ISO 20022, assurant le verrouillage d'état à deux phases (2PC) et l'injection d'un `UETR` immuable et non régénérable.

---

### [Major] Rupture de cohérence documentaire interne : Maintien artificiel de la Ligne directrice IA de l'AMF comme « lacune ouverte »
- **Localisation précise :** Chapitre 26, page 309 (Tableau 26.1) ; Chapitre 27, pages 311-313 (§ 27.1, Tableau 27.3) ; Chapitre 29, page 328 (Tableau 29.1).
- **Citations textuelles fidèles :**
  > *Page 309 :* « Ligne directrice IA de l’AMF [...] Date opposable : 1er mai 2027. »  
  > *Page 328 (Tableau 29.1) :* « Ligne directrice IA de l’AMF : le calendrier seulement — et une modalité, une articulation et une définition versées par le Vol. III [...] rien de dérivable — le contenu du texte n’est pas au socle. Statut du lien : lacune ouverte — la seule entrée qui ne produise rien du tout. »
- **Diagnostic causal approfondi :**  
  Le compendium allègue qu'en raison d'erreurs d'extraction automatisée lors des gels documentaires de juillet 2026, le contenu de la Ligne directrice sur l'IA de l'AMF est demeuré inaccessible, laissant cinq cases vides sur cinq et produisant « zéro contrainte » dans la matrice d'architecture logicielle.
- **Falsification bibliographique et documentaire interne :**  
  1. *Réfutation irréfutable par les artefacts du dépôt :* L'examen des pièces maîtresses du projet démontre l'existence physique du fichier `c:\Github\EntrepriseAgentique\documents\Note AMF IA.pdf` (daté du 31 octobre 2026, 44 pages, rédigé par André-Guy Bruneau). Cette note instruit de façon exhaustive les 41 attentes de la version définitive de la *Ligne directrice sur la gestion du risque lié à l'intelligence artificielle* de l'AMF, formellement publiée le **7 avril 2026** (Bulletin officiel de l'AMF, Vol. 23, n° 14), avec prise d'effet au 1er mai 2027.
  2. *Contraintes d'architecture de premier plan occultées :* Le texte de l'AMF formule des attentes impératives qui s'imposent à toute architecture logicielle financière québécoise :
     - Imputabilité nominative d'un membre de la haute direction pour l'ensemble des systèmes d'IA (Attente 4.1) ;
     - Tenue d'un inventaire centralisé exhaustif avec cotation du niveau de risque et cartographie des dépendances de données (Attente 5.1) ;
     - Obligation de transparence et de traitement équitable interdisant les résultats biaisés ou discriminatoires envers les consommateurs (Attente 6.2) ;
     - Obligation d'application cumulative de la ligne directrice IA avec la ligne directrice sur la gestion du risque de modèle.  
  Conserver au sein du compendium de novembre 2026 l'affirmation que l'AMF est une « lacune ouverte » qui « ne produit rien du tout » constitue une contradiction interne manifeste avec les travaux d'instruction déjà achevés par l'auteur.
- **Correctif recommandé :**  
  Synchroniser immédiatement le compendium avec les conclusions de `Note AMF IA.pdf`. Remplacer la case vide du Tableau 29.1 par les contraintes d'architecture dérivées des attentes de l'AMF, garantissant ainsi l'applicabilité du cadre pour les institutions financières québécoises (telles que le Mouvement Desjardins et les assureurs sous tutelle de l'AMF).

---

### [Major] Falsification empirique des études de cas bancaires canadiennes (Ch. 35) — Biais d'incommensurabilité temporelle, contradictions arithmétiques et requalification indue d'assistants bureautiques
- **Localisation précise :** Chapitre 35, pages 399 à 408 (§ 35.1 TD, § 35.2 Scotiabank, § 35.3 RBC, § 35.6 CIBC, § 35.8.1 BMO, § 35.8.2 Sun Life).
- **Citations textuelles fidèles :**
  > *Page 399 (§ 35.1) :* « Métrique auto-déclarée : selon le communiqué de cette institution du 21 mai 2026, le traitement passe d’environ quinze heures à moins de trois minutes pour les hypothèques et les lignes de crédit garanties, à titre de résultats préliminaires. »  
  > *Page 400 (§ 35.2) :* « Métriques auto-déclarées : selon la source primaire de l’institution (juillet 2025), le système traite environ 90 % d’environ 1 500 courriels par jour [...] La même source y associe un second ordre de grandeur : 60 000 à 70 000 demandes par mois. »  
  > *Page 404 (§ 35.6) :* « Métrique auto-déclarée : l’économie déclarée durant le pilote est de plus de 200 000 heures [...] Le communiqué [...] décrit une IA générative assistive : il ne mentionne ni IA agentique, ni agents autonomes... »  
  > *Page 407 (§ 35.8.2) :* « ...le consortium déclare que son programme phare est déjà en production en environnement réglementé et traite plus de deux mille milliards de jetons par mois... »
- **Diagnostic causal approfondi :**  
  Pour étayer la thèse selon laquelle « l'agentique canadienne est en production », le compendium agrège des métriques issues de communiqués de presse corporatifs sans appliquer de grille critique rigoureuse, mélangeant de simples outils d'aide à la saisie bureautique et de véritables architectures agentiques autonomes.
- **Falsification empirique détaillée :**
  1. *Fausse équivalence temporelle chez TD (15 h vs 3 min) :*  
     L'affirmation d'une division du temps de traitement par 300 repose sur la comparaison trompeuse de deux grandeurs incommensurables : les 15 heures mesuraient un délai de cycle asynchrone de bout en bout (incluant files d'attente intermédiaires et contrôles), tandis que les 3 minutes ne représentent que le temps d'inférence brute du modèle pour générer un mémo de synthèse. En vertu de la Ligne directrice B-20 du BSIF, l'adjudication finale du crédit hypothécaire exige l'évaluation humaine obligatoire d'un souscripteur accrédité (évitant simultanément la qualification de décision exclusivement automatisée sous l'art. 12.1 de la Loi 25). Le goulot d'étranglement décisionnel humain subsiste intégralement, et le gain de temps global de bout en bout n'a jamais été audité.
  2. *Contradiction arithmétique et charge du résidu chez Scotiabank :*  
     L'institution revendique le traitement de 1 500 courriels/jour et l'acheminement de 60 000 à 70 000 demandes/mois. Or, 1 500 courriels par jour sur 21 jours ouvrables bancaires représentent 31 500 courriels/mois (ou 45 000 sur 30 jours civils). Ces deux métriques ne mesurent manifestement pas le même périmètre opérationnel. De surcroît, un taux d'automatisation de 90 % abandonne un résidu de 10 % d'escalade humaine, soit 150 dossiers par jour. Dans une grande banque, ces 150 exceptions non résolues concentrent l'extrême complexité opérationnelle (fraude, instructions urgentes, transferts de fonds) ; le coût cognitif et salarial requis pour traiter manuellement ces cas escaladés annule une part substantielle de la rentabilité proclamée.
  3. *Surqualification taxonomique abusive (RBC, CIBC, Sun Life) :*  
     Les 27 000 utilisateurs chez RBC ou les 200 000 heures déclarées chez CIBC correspondent à des copilotes d'assistance bureautique interne (recherche documentaire, aide à la rédaction de courriels), dénués de toute délégation d'autorité ou d'interaction avec des outils transactionnels. Quant aux 2 000 milliards de tokens par mois de Sun Life, il s'agit d'un indicateur de consommation d'infrastructure informatique (coût cloud facturable), qui ne prouve en rien la qualité, la traçabilité ou l'efficacité opérationnelle des systèmes.
- **Correctif recommandé :**  
  Requalifier formellement les métriques du Chapitre 35 en déclarations promotionnelles corporatives non auditées (*unaudited marketing claims*). Introduire un tableau d'évaluation critique rectifiant les biais d'incommensurabilité et intégrant la charge opérationnelle de l'humain dans la boucle (*human-in-the-loop operational load*).

---

### [Major] Requalification anachronique du patrimoine actuariel d'Intact Financial Corporation en « IA agentique » (Ch. 35 § 35.7)
- **Localisation précise :** Chapitre 35, pages 405 à 406 (§ 35.7).
- **Citations textuelles fidèles :**
  > *Page 405 (§ 35.7) :* « Intact : l’industrialisation sans le vocabulaire [...] Ce cas est l’inverse de tous les précédents : la maturité opérationnelle la plus élevée du chapitre, et pas un mot d’agentique. Métriques auto-déclarées : le rapport annuel 2025, publié le 26 mars 2026, documente une capacité déclarée dont l’échelle n’a d’équivalent chez aucune autre institution du chapitre — plus de 600 experts au Canada et en Asie exploitant près de 600 modèles en production ; plus de 200 millions de dollars de bénéfices annuels attribués à cette capacité... »
- **Diagnostic causal approfondi :**  
  L'auteur constate qu'Intact Corporation exploite 600 modèles en production générant 200 M$ de bénéfices annuels sans employer le vocabulaire de l'agentique. Au lieu d'en déduire que l'institution déploie de l'apprentissage automatique prédictif traditionnel, l'auteur opère une requalification anachronique en affirmant qu'Intact incarne la « maturité agentique opérationnelle la plus élevée du chapitre ».
- **Falsification méthodologique et technologique :**  
  1. *Absence des attributs agentiques fondamentaux :* Les 600 modèles d'Intact sont des modèles statistiques supervisés (modèles linéaires généralisés - GLM, arbres de décision boostés XGBoost) utilisés pour la tarification du risque actuariel en assurance de dommages (auto, habitation) et le scoring de fraude aux réclamations. Ils ne possèdent aucune boucle d'autonomie ReAct, aucun protocole d'appel d'outils dynamique (MCP/function calling), aucune mémoire de session et ne participent à aucune topologie multi-agents.
  2. *Anachronisme de causalité financière :* Les 200 millions de dollars de valeur proviennent de quinze années d'optimisation mathématique du risque sous la supervision de la Ligne directrice BSIF E-23, et non de l'émergence récente des architectures d'agents logiciels autonomes.
- **Correctif recommandé :**  
  Rétablir la rigueur taxonomique en requalifiant le cas d'Intact comme une référence d'industrialisation du *Machine Learning* actuariel prédictif classique. Supprimer l'affirmation selon laquelle Intact représente le sommet de la maturité agentique canadienne.

---

### [Major] Incompatibilité réglementaire entre le modèle en « boucle fermée » d'AP2 et la Loi sur les services bancaires axés sur les consommateurs (CDBA / C-15)
- **Localisation précise :** Chapitre 36, pages 415 à 416 (§ 36.2.6).
- **Citations textuelles fidèles :**
  > *Page 415 (§ 36.2.6) :* « La voie de résolution privilégiée est le modèle en boucle fermée : une couche de confiance partagée entre participants, où l’autorisation porte sur le réseau lui-même plutôt que sur chaque interaction bilatérale, et où les règles de participation définissent les responsabilités en cas d’écart. »
- **Diagnostic causal approfondi :**  
  Pour résoudre le problème critique du « trou de responsabilité » (achats non intentionnels initiés par des agents sur des rails irrévocables où la rétrofacturation n'existe pas), le compendium préconise un consortium privé fonctionnant en « boucle fermée ».
- **Falsification d'architecture réglementaire :**  
  Cette préconisation heurte de plein fouet le cadre juridique fédéral de l'Open Banking :
  1. La *Loi sur les services bancaires axés sur les consommateurs* (CDBA, issue du projet de loi C-15 sanctionné le 26 mars 2026, analysée au Ch. 32) proscrit expressément les accords fermés bilatéraux et les barrières d'accès discriminatoires.
  2. L'objectif légal de la CDBA est précisément d'abolir les jardins clos bancaires (*walled gardens*) en imposant des règles communes d'accréditation et des interfaces de programmation (API) standardisées et ouvertes sous la supervision de la Banque du Canada.
  3. Conditionner la viabilité d'AP2 à un réseau fermé consortial contredit la vocation d'universalité de l'Open Banking canadien et disqualifie le protocole pour l'usage du grand public et des tiers indépendants accrédités.
- **Correctif recommandé :**  
  Abandonner la préconisation du modèle en boucle fermée comme réponse au trou de responsabilité d'AP2. Élaborer des mécanismes de garantie conformes aux exigences de l'Open Banking ouvert (mécanismes de fonds séquestres / *escrow*, polices d'assurance contre les transactions erronées, ou cautionnements d'initiation) compatibles avec les règles non discriminatoires de la CDBA.

---

### [Major] Flou constitutionnel quant à l'applicabilité de l'article 12.1 de la Loi 25 aux banques fédérales de l'Annexe I
- **Localisation précise :** Chapitre 27, pages 315-316 (§ 27.3) et Chapitre 29, pages 328 à 333 (§ 29.1, § 29.3).
- **Citations textuelles fidèles :**
  > *Page 316 (Ch. 27 § 27.3) :* « Troisième : le régime de l’article 12.1 atteint-il les institutions sous charte fédérale, celles qu’E-23 vise au ch. 25 ? Le socle porte le déclencheur — "toute personne qui exploite une entreprise" — et rien sur la portée du régime à leur égard [...] et le ch. 27 § 27.3 a laissé ouverte la question de savoir si l’article 12.1 atteint les institutions sous charte fédérale. »
- **Diagnostic causal approfondi :**  
  Le compendium érige l'article 12.1 de la Loi 25 québécoise en exigence de conception architecturale cardinale du système financier canadien, mais maintient délibérément en suspens la question de son application juridique aux banques fédérales de l'Annexe I (RBC, TD, BMO, BNS, CIBC).
- **Falsification juridique constitutionnelle :**  
  1. *Partage des compétences législatives :* En vertu de l'article 91(15) de la *Loi constitutionnelle de 1867*, le secteur bancaire relève de la compétence exclusive du Parlement fédéral.
  2. *Régime de protection des renseignements personnels :* Selon la jurisprudence constante de la Cour suprême du Canada et la doctrine constitutionnelle, les activités bancaires des banques à charte fédérale sont régies par la loi fédérale *Loi sur la protection des renseignements personnels et les documents électroniques* (LPRPDE / PIPEDA), sous la surveillance exclusive du Commissariat à la protection de la vie privée du Canada (CPVP).
  3. L'application directe de l'art. 12.1 de la Loi 25 québécoise aux décisions automatisées d'octroi de crédit rendues par des banques fédérales se heurte à la doctrine de l'inapplicabilité constitutionnelle (exclusivité des compétences) et à la doctrine de la prépondérance fédérale en cas de conflit avec les lignes directrices prudentielles du BSIF (E-23 et B-20).
  4. Laisser entendre qu'une banque fédérale doit nécessairement concevoir son infrastructure d'adjudication pancanadienne selon les contraintes spécifiques de l'art. 12.1 sans opérer de distinction juridictionnelle constitue une approximation normative substantielle.
- **Correctif recommandé :**  
  Établir une stricte partition juridictionnelle : l'article 12.1 de la Loi 25 constitue un impératif d'architecture absolu pour les institutions à charte provinciale québécoise (le Mouvement Desjardins, les sociétés de fiducie et les assureurs autorisés par l'AMF) ; pour les banques sous charte fédérale de l'Annexe I, le cadre directeur applicable est constitué de la LPRPDE fédérale, couplée aux lignes directrices E-23 et B-20 du BSIF.

---

# Minor Corrections and Typos

1. **[Minor] Date de publication officielle de la Ligne directrice IA de l'AMF**  
   - *Localisation :* Chapitre 26, page 309 (Tableau 26.1) et Chapitre 27, pages 312-313 (§ 27.1, Tableau 27.1).  
   - *Description :* Le texte indique que la publication de la ligne directrice « n'est pas datée au jour près » et retient la mention indéterminée « Avril 2026 ».  
   - *Correction :* La date de publication officielle de la version définitive de la *Ligne directrice sur la gestion du risque lié à l'intelligence artificielle* par l'Autorité des marchés financiers est le **7 avril 2026** (attestée par le Bulletin de l'Autorité, Vol. 23, n° 14).

2. **[Minor] Attribution institutionnelle de la supervision technique de l'Open Banking (CDBA / C-15)**  
   - *Localisation :* Chapitre 32, pages 367 à 370 (§ 32.1, § 32.2) et titres transversaux du compendium.  
   - *Description :* Les directives d'évaluation font couramment référence au « cadre FCAC d'open banking ».  
   - *Correction :* Il convient de confirmer la parfaite exactitude du Chapitre 32 sur ce point : le projet de loi C-15 (sanctionné le 26 mars 2026) a déchargé l'Agence de la consommation en matière financière du Canada (ACFC / FCAC) de la supervision technique au profit de la **Banque du Canada** (adossée à la RPAA), l'ACFC conservant son mandat d'éducation et de protection des consommateurs. Aligner la terminologie transversale du compendium sur cette réalité institutionnelle.

3. **[Minor] Règlement administratif n° 10 de Paiements Canada (RTR) : Date d'entrée en vigueur vs mise en service opérationnelle**  
   - *Localisation :* Chapitre 33, page 377 (§ 33.3) et Chapitre 36, page 417 (Tableau 36.2).  
   - *Description :* Le texte cite l'enregistrement du règlement administratif n° 10 (DORS/2026-133) le 18 juin 2026 et son entrée en vigueur le **24 août 2026**.  
   - *Correction :* L'énoncé est rigoureusement exact. Il convient toutefois de préciser explicitement que l'entrée en vigueur juridique du règlement administratif au 24 août 2026 ne préjuge pas de la mise en service industrielle du rail RTR, celle-ci demeurant visée pour le quatrième trimestre 2026.

4. **[Minor] Sous-estimation du contenu normatif de l'Avis ACVM 11-348 (Marchés de capitaux)**  
   - *Localisation :* Chapitre 28, page 325 (§ 28.2).  
   - *Description :* Le compendium note que « le socle n'établit pas si l'avis formule des attentes au-delà du constat d'applicabilité ».  
   - *Correction :* Le personnel des Autorités canadiennes en valeurs mobilières (ACVM) formule des attentes explicites relatives au respect de l'obligation de convenance (*suitability* sous le Règlement 31-103), à la surveillance active des algorithmes de négociation pour prévenir les manipulations de marché et la collusion tacite, ainsi qu'aux devoirs de gestion des conflits d'intérêts lors de l'usage d'agents autonomes.

5. **[Minor] Levée de l'ambiguïté sur l'exercice financier de Paiements Canada pour le T4 2026**  
   - *Localisation :* Chapitre 33, pages 375 à 377 (§ 33.2–33.3).  
   - *Description :* Le texte mentionne que le socle ne précise pas si Paiements Canada retient le trimestre civil pour l'ouverture du T4 2026.  
   - *Correction :* Paiements Canada opère selon l'année civile (1er janvier – 31 décembre). L'ouverture du T4 correspond sans indétermination au 1er octobre 2026.
