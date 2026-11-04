# Revue approfondie et contradictoire — Cadre de référence CRE-IA-2026-01

- **Document** : *Interopérabilité et Orchestration en Entreprise Agentique*, cadre de référence d'architecture d'entreprise CRE-IA-2026-01, `documents/Cadre de Référence.pdf`, 283 pages, 287 exigences (EXIG) et 12 principes (PRIN). Auteur : André-Guy Bruneau.
- **Version auditée** : 1.1 du 28 octobre 2026, avec l'actualisation du 1er novembre 2026 (annexe H, informative). État des sources du corps : 27-28 octobre 2026.
- **Date de la revue** : 3 novembre 2026.
- **Méthode, en quatre phases** :
  1. Plan de revue : structure, notations, thèses T1 à T8 (`REVIEW_PLAN_CADRE.md`).
  2. Audit contradictoire en 29 tranches de 12 pages, avec 2 pages de recouvrement : 29 rapports bruts, environ 860 constats.
  3. Consolidation en six tranches, avec contre-vérification de chaque constat dans le texte intégral, puis audit bibliographique séparé (`audit_lit.md` : 83 faits externes vérifiés à la source primaire le 3 novembre 2026, soit 69 confirmés, 3 inexacts, 5 obsolètes et 6 non vérifiés; 16 travaux omis).
  4. Méta-audit croisé : fusion des défauts transversaux, arbitrage unique des décisions de conception, évaluation.
- **Décompte** : 623 défauts consolidés, soit 14 BLOQUANT, 216 MAJEUR et 393 MINEUR. 34 constats ont été écartés ou rétrogradés à la contre-vérification. La présente synthèse regroupe 28 défauts transversaux (12 BLOQUANT, 16 MAJEUR) qui couvrent les 14 BLOQUANT et la majorité des MAJEUR, et elle retient 34 arbitrages.
- **Convention** : « [1.01] » renvoie au défaut 01 de la tranche consolidée 1 (matrice de la section 2), « A-nn » à un arbitrage de la section 2.0.1, et « lit. n » à la ligne n du tableau 1 d'`audit_lit.md`.

## 1. Verdict exécutif

### 1.1 Thèse centrale du cadre

Le cadre soutient qu'une entreprise peut confier des actions réelles à des agents fondés sur des modèles de langage sans perdre le contrôle. Il faut pour cela réunir quatre conditions. (1) Tout échange passe par des protocoles ouverts (MCP 2026-07-28, A2A 1.0, CloudEvents) et par un point unique d'application des politiques, la passerelle d'agents, adossée à un catalogue et à un registre qui font foi. (2) L'autonomie se règle sur quatre axes distincts (classe de risque, niveau N0 à N4, palier d'outil P0 à P3, topologie), combinés par la règle la plus stricte et plafonnés par la classe. (3) Le déterminisme entoure le modèle : exécution durable, saga, idempotence, approbation humaine signée et liée à l'empreinte de l'action exacte, retrait des capacités d'envoi après lecture de contenu non fiable, journal d'audit chaîné. (4) La conformité (Loi 25, E-23, RIA, NIST, ISO/IEC 42001) se traite dans les mêmes artefacts, selon une feuille de route en quatre phases.

### 1.2 Évaluation de la contribution

**Forces réelles.**
- La séparation des axes (classe, niveau, palier, topologie) et leur combinaison par plafond est l'apport conceptuel le plus utile du document. Le palier tiré du catalogue plutôt que des annotations de l'outil (EXIG-AUT-08) est juste : la spécification MCP impose de tenir les annotations pour non fiables (lit. 7).
- Le socle factuel est exact. MCP 2026-07-28, A2A 1.0 et 1.0.1, les RFC 8693, 9068 et 9396, OpenTelemetry v1.41.0, E-23, ainsi que les articles 3.3, 12.1, 17, 65.2 et 90.1 se confirment jusqu'au détail normatif (lit. 1-20, 25-31). Aucune référence inventée n'a été trouvée parmi celles qui ont été vérifiées.
- La lecture de la RFC 8693 sur les acteurs imbriqués (informatifs seulement) est correcte (lit. 30), tout comme le principe d'une approbation liée à une empreinte canonisée selon la RFC 8785.
- La discipline rédactionnelle est réelle : un « Pourquoi » par exigence, la distinction entre exigence externe et choix du cadre, la règle « agent unique d'abord, multiagent sur gain mesuré » (que la littérature appuie, voir 3.1, travaux 12 et 13), et une annexe H qui publie ses propres errata.

**Faiblesses structurelles.** Elles ne sont pas des fautes de détail, mais des manières récurrentes de spécifier :
1. **Le point d'application central est décrit de six façons** (T-01). La règle que tout le reste suppose (« rien ne contourne la passerelle ») n'est vraie pour aucune des lectures possibles : l'intradomaine, les événements, les agents intégrés aux logiciels-services et le poste local y échappent.
2. **Les propriétés d'exécution sont affirmées, pas spécifiées avec leurs modes de défaillance** : idempotence, usage unique, compensation, chaînage d'audit, coupe-circuit. Chacune est juste dans le cas nominal et fausse ou indécidable sous réessai, panne, concurrence ou arrêt (T-03, T-04, T-05, T-13, T-14, T-17).
3. **Les contrôles de sécurité sont conçus agent par agent, alors que les menaces sont systémiques** : la triade létale, la délégation et les chaînes d'événements traversent les agents (T-07, T-09, T-01).
4. **L'échec en mode fermé est posé partout sans sémantique de défaillance.** Il bloque les compensations qu'il rend nécessaires, et aucune exigence de disponibilité ne vise les composants obligatoires (T-03, T-15).
5. **Les sources de vérité sont multipliées** : quatre sources pour l'art. 12.1, trois listes de déclencheurs de réévaluation, deux listes de non-dérogeables, un catalogue qui « fait foi » contre des blocs DOIT qui figent les versions (T-18, T-19).
6. **La feuille de route est informative et incompatible avec les exigences** : la passerelle n'est jamais ouverte au palier P3, des obligations légales sont planifiées en phase, et aucun régime transitoire ne vise les agents existants (T-20).
7. **Aucune preuve de faisabilité n'est fournie** : ni banc d'essai de la passerelle, ni règle de décision statistique pour les portes et les seuils (T-24).
8. **L'hygiène bibliographique ne suit pas la méthode déclarée** : sources de catégorie C citées, doublons, versions IETF déjà dépassées, règlement (UE) 2026/1744 non relu à la source (T-27).

**Verdict sur les thèses.**
- **T1 — Le verrouillage s'est déplacé des protocoles vers les plateformes : plausible, non démontrée.** Les faits de consolidation sont confirmés (MCP à l'AAIF le 9 décembre 2025, A2A le 17 août 2026; lit. 39-40). L'appui chiffré repose toutefois sur des prévisions d'analystes sans méthode publiée (lit. 43). Surtout, le cadre ne tire pas la conséquence de sa propre thèse : les plateformes à agents intégrés, qu'il désigne comme le lieu du verrouillage, n'ont aucun régime applicable (T-02). La thèse reste une prise de position et doit être présentée comme telle.
- **T2 — La passerelle suffit : réfutée telle qu'énoncée.** La portée est contradictoire (T-01), le bus d'événements la contourne ([2.02]), l'intradomaine échappe aux contrôles du chapitre 8 ([3.28]) et aucune exigence de disponibilité n'existe ([4.13]). La politique en cache n'a pas de durée de validité ([6.15]) et la liaison mTLS ne traverse pas une terminaison TLS ([4.10]). La thèse devient tenable avec A-01, A-02, A-04 et A-16, et après le banc d'essai de la section 3.3.
- **T3 — Idempotence, exécution durable et saga évitent de refaire une action terminée : réfutée telle qu'énoncée.** Une compensation peut précéder l'effet tardif de l'original ([3.01]). Les arrêts interdisent les compensations qu'ils rendent nécessaires ([3.02]). La rétention des clés n'est pas bornée ([3.12]), et la déduplication est confiée à un adaptateur devant un système qui seul sait si l'effet a eu lieu ([1.04]), contre l'argument de bout en bout (3.1, travail 11). La thèse devient tenable avec A-06, A-07 et A-09.
- **T4 — Le retrait déterministe neutralise la triade létale : vraie pour un agent isolé, réfutée à l'échelle du système.** La décomposition multiagent, la mémoire, la récupération et les tâches A2A entrantes contournent le marquage, qui ne lit que les sorties d'outils ([4.01]). « Session » n'est défini nulle part ([6.16]). La littérature sur le contrôle de flux d'information (FIDES) donne le modèle qui manque, et les attaques adaptatives relativisent tout taux mesuré sur des attaques statiques (3.1, travaux 4, 5 et 7). La thèse devient tenable avec A-17.
- **T5 — L'approbation liée à l'action exacte est vérifiable et ne dégénère pas en approbation machinale : partiellement soutenue.** Le principe est sain. L'exécution comporte toutefois quatre brèches : un différentiel d'analyse JSON ([3.03]), un écran qui n'est pas dérivé des arguments hachés ([3.22]), un seuil mesuré sur un argument déclaré par l'agent ([6.01]) et l'absence de liaison à l'appelant ([6.11]). Le format ne prévoit pas la double approbation ([6.14]). Contre l'approbation machinale, le cadre plafonne la fréquence (EXIG-AUT-20) sans dimensionner la charge que crée sa propre présomption d'injection ([3.33], [4.21]). La thèse devient tenable avec A-10 à A-14, à condition de mesurer l'approbation machinale (section 3.3).
- **T6 — La délégation à audience unique reste sûre en chaîne : partiellement soutenue.** La lecture de la RFC 8693 est exacte, mais l'EXIG-ORC-04 la contredit ([2.04]). Les échanges successifs prolongent la délégation sans plafond de durée ([4.05]), la portée de la tâche n'a aucune représentation dans le jeton ([4.03]), l'agent ambiant ne peut pas obtenir le jeton d'un mandant absent ([4.08]), et l'exemple C.5 contredit le modèle à deux jetons ([6.04]). La thèse devient tenable avec A-16.
- **T7 — Les classes, les plafonds et la règle la plus stricte forment un treillis cohérent : réfutée.** « Le plus strict » n'est pas un ordre sur des contrôles non comparables ([3.25]). P2 et P3 ne sont pas disjoints ([1.18]), N3 et N4 sont indiscernables pour la passerelle ([3.32]) et la classification est circulaire avec le caractère automatisé de la décision ([5.16]). La feuille de route n'ouvre jamais le palier P3 ([5.40]). La thèse devient tenable avec A-14, A-25, A-26 et A-27.
- **T8 — La méthode de validation des sources est fiable et reproductible : fiable sur le fond, non reproductible.** 69 des 83 faits vérifiés sont confirmés, mais la méthode ne couvre pas toutes les références ([1.11], [6.18]). L'annexe G contient des doublons qui gonflent le total de 473 ([6.22]; lit., section 2), des sources de catégorie C sont citées à l'appui d'exigences ([6.20], [6.21]), cinq brouillons IETF ont changé de révision entre le 30 octobre et le 2 novembre (lit. 29, 62, 67-69), et le règlement (UE) 2026/1744 n'a pas pu être relu sur EUR-Lex (lit. 22). La thèse devient tenable avec A-31.

### 1.3 Verdict

**Acceptable après révisions majeures, pas à refondre.** L'architecture (axes séparés, passerelle, catalogue, registre, approbation liée à l'empreinte) est défendable. Les 14 défauts bloquants relèvent de huit causes, et chacune a un correctif rédigeable sans changer la thèse centrale. En l'état, le cadre ne peut pas servir de référentiel d'homologation : deux équipes de bonne foi qui l'appliquent arrivent à des passerelles de portées différentes, à des sagas bloquées sous coupe-circuit et à des preuves légales sans magasin.

Conditions pour lever le verdict :
1. Appliquer les arbitrages A-01 à A-34 dans une révision 1.2. Les errata seuls font l'objet d'une 1.1.1 (A-31).
2. Fermer les 14 défauts BLOQUANT, et vérifier chacun par un test négatif ajouté à l'annexe A.
3. Produire au moins les preuves 1 à 6 de la section 3.3 avant d'homologuer un agent N3 ou un premier palier P3.
4. Relire le règlement (UE) 2026/1744 au JO et réépingler les brouillons IETF avant de geler le jalon J2a (section 3.2).
5. Recompter les exigences et les références après la révision (A-30, A-31).

## 2. Matrice des défauts

### 2.0 Défauts transversaux et dérives inter-chapitres

Chaque entrée fusionne des défauts que plusieurs tranches ont vus séparément. La gravité retenue est celle du défaut de tranche le plus grave. Le correctif renvoie à l'arbitrage qui le règle.

#### T-01 [BLOQUANT - Erreur formelle/architecturale] Portée des points d'application : six énoncés incompatibles de la règle centrale
- **Défauts fusionnés** : 1.01, 1.09, 1.19, 1.44, 1.57, 2.01, 2.02, 2.11, 2.26, 2.27, 2.28, 3.28, 4.60, 4.99 (m), 5.43.
- **Localisations** :
  - décision 2, p. 8 (« Rien ne contourne la passerelle ni le catalogue »);
  - tableau 10, p. 29 (« à l'intérieur, une fonction locale suffit »);
  - EXIG-ARC-01, p. 33 (intradomaine « régi par l'EXIG-IAM-17 »; « Dans tout environnement serveur »);
  - § 6.2, À RETENIR, p. 49 (« Les trois passent par la passerelle »);
  - EXIG-MCP-01, p. 54 (« Tout outil »);
  - EXIG-EVT-07, p. 79;
  - EXIG-AUT-10, p. 110 (« Pour chaque appel d'outil, la passerelle »);
  - EXIG-IAM-17, p. 129;
  - règle de progression, p. 202, et tableau 61, p. 205 (couverture limitée à l'interdomaine).
- **Diagnostic** : un point d'application des politiques n'a de valeur que si l'ensemble des chemins qui mènent à un effet le traverse. Le texte définit cet ensemble tantôt par la frontière de domaine, tantôt par le protocole (MCP, A2A), tantôt par l'outil (« tout outil »). Les événements, eux, n'ont aucun point d'application. Or le chapitre 8 confie à la seule passerelle la vérification du jeton d'approbation, du palier et du seuil. Tout chemin qui ne la traverse pas exécute donc un P3 sans vérificateur, alors que l'approbation P3 est non dérogeable (EXIG-GOV-17).
- **Contre-exemple** : une fonction locale d'un agent de paie, dans le même domaine que le système de paie, émet un virement (P3). Selon le tableau 10 et l'EXIG-ARC-01, l'appel ne passe pas par la passerelle. Selon l'EXIG-IAM-17, le serveur de ressources décide, mais il ne vérifie aucun jeton d'approbation. Le virement part sans approbation, sans qu'aucune exigence ait été violée à la lettre. Variante : un événement « commande révisée » déclenche chez un consommateur une écriture P2 au nom d'une personne, sans intersection des droits ni compteur de délégation ([2.02]).
- **Correctif** : A-01 (passerelle), A-02 (courtier d'événements), A-03 (agents intégrés aux logiciels-services), A-26 (régime transitoire de contournement).

#### T-02 [BLOQUANT - Erreur formelle/architecturale] Agents intégrés aux logiciels-services : dans la portée, recommandés, non conformes par construction
- **Défauts fusionnés** : 1.02, 1.24, 5.10, 5.12.
- **Localisations** : PRIN-09, p. 27; § 2.4, p. 20; EXIG-ARC-01, -03 et -08, p. 33-35; tableau 12, p. 41 (« Plateforme SaaS à agents intégrés »); EXIG-INT-02, p. 47; EXIG-GOV-07 et ATTENTION, p. 165; EXIG-GOV-10; EXEMPLE, p. 167 (versions de modèles hébergés); EXIG-APP-13.
- **Diagnostic** : l'EXIG-ARC-08 (aucune clé de fournisseur, modèles par la passerelle) et l'EXIG-ARC-01 supposent que l'entreprise contrôle l'exécution de l'agent. Un agent de Copilot Studio, d'Agentforce ou de ServiceNow s'exécute chez l'éditeur. Il ne peut satisfaire aucune des deux, et la suspension « à la passerelle » (p. 165) n'a pas de prise sur lui. Le cadre recommande ces plateformes comme SBB sans régime dérogatoire ni contrôle compensatoire.
- **Contre-exemple** : un agent Agentforce, de classe modérée, modifie des dossiers clients dans le CRM. Il est inscrit au registre, mais aucune passerelle ne voit ses appels, le coupe-circuit de l'EXIG-IAM-20 ne l'atteint pas, et le fournisseur change de modèle sans préavis opposable. Soit l'homologation est refusée à toute plateforme recommandée, soit elle est accordée contre des DOIT.
- **Correctif** : A-03.

#### T-03 [BLOQUANT - Erreur formelle/architecturale] Les arrêts interdisent les compensations qu'ils rendent nécessaires
- **Défauts fusionnés** : 1.06, 2.35, 3.02, 3.09, 4.16, 4.49, 5.09.
- **Localisations** : PRIN-12, p. 28 (« jamais rester à moitié exécuté »); EXIG-EVT-06, p. 79 (plafond de sauts); EXIG-ORC-16 à 18, p. 95-96; EXIG-ORC-26 et 28, p. 100 (« bloque toute nouvelle étape »); EXIG-AUT-11, p. 110; EXIG-AUT-18, p. 114; EXIG-IAM-07, p. 121; EXIG-IAM-18 et 20, p. 129-130; EXIG-FIN-04 et 05, p. 156; EXIG-GOV-08, 09 et 16; § 12.8, étapes 1 et 4, p. 186-187.
- **Diagnostic** : une saga n'est sûre que si sa compensation reste exécutable après n'importe quel arrêt. Le cadre définit sept arrêts : coupe-circuit, suspension, révocation, mode fermé, budget épuisé, plafond de sauts et échéance du mandat. Chacun bloque tout appel de l'identité visée, compensations comprises. L'EXIG-ORC-28 promet pourtant de laisser les sagas « suspendues ou compensées ». En chorégraphie, aucun orchestrateur n'existe pour porter les EXIG-ORC-16 à 18.
- **Contre-exemple** : une saga de commande a débité le client (T2) quand le coupe-circuit désactive l'identité de l'agent. Le remboursement (compensation de T2) est un appel de cette identité. La passerelle le refuse, et le client reste débité pour une commande annulée jusqu'à une intervention manuelle que rien ne déclenche.
- **Correctif** : A-06, A-08.

#### T-04 [BLOQUANT - Erreur formelle/architecturale] Compensation d'une étape incertaine : course avec l'original encore en vol
- **Défauts fusionnés** : 3.01, 3.11, 3.13, 6.19.
- **Localisations** : EXIG-ORC-16, p. 96 (« sa compensation est déclenchée et reste sans effet si l'action n'a pas eu lieu »); EXIG-ORC-20 (tests); EXIG-ORC-21 (replanification); tableau 68, no 31, p. 244 (présenté comme corrigé).
- **Diagnostic** : « sans effet si l'action n'a pas eu lieu » ne vaut qu'au moment où la compensation s'exécute. Si l'original est encore en transit (file, réessai du système cible, livraison au moins une fois), il produit son effet après la compensation, et l'ordre final est faux. Une compensation n'est sûre qu'après la clôture de l'opération chez le système visé.
- **Contre-exemple** : un virement expire côté client, mais il reste dans la file du système bancaire. La compensation « annuler le virement k » ne trouve rien et réussit à vide. Le virement s'exécute 40 secondes plus tard, et la saga est déclarée compensée avec un effet net non nul.
- **Correctif** : A-07.

#### T-05 [BLOQUANT - Erreur formelle/architecturale] L'empreinte h ne garantit pas que l'action exécutée est l'action approuvée
- **Défauts fusionnés** : 3.03, 3.22, 3.23, 3.24, 3.37, 4.92, 6.11, 6.13, 6.14.
- **Localisations** : § 8.5, figure 16, étape 7, p. 111; EXIG-AUT-12, p. 110-111; EXIG-AUT-15, p. 112; EXIG-AUT-19, p. 114; § 8.6, p. 113 (édition); C.6, p. 221; C.8, p. 223-224 (« ce qui prouve que l'action exécutée est bien celle qui a été approuvée »); Pourquoi de l'EXIG-OBS-12.
- **Diagnostic** : la preuve suppose que l'objet haché soit l'objet exécuté, l'objet présenté, l'objet de l'appelant et l'objet de l'état approuvé. Le texte n'en garantit aucun :
  - clés JSON dupliquées ou grands nombres analysés différemment par la passerelle et par le serveur;
  - écran alimenté par `authorization_details`, distinct des arguments hachés;
  - `agent_id` et `task_id` présents dans le jeton sans être comparés à l'appelant;
  - définition de l'outil hors de h;
  - état de la ressource modifiable pendant 15 minutes;
  - un seul approbateur dans le format, alors que l'EXIG-AUT-15 en exige deux;
  - auto-approbation du mandant non tracée.
- **Contre-exemple** : l'agent envoie `{"beneficiaire":"A","beneficiaire":"B"}`. La passerelle canonise en gardant la première occurrence et l'écran montre A. Le serveur, en Python, garde la dernière et paie B. L'audit « prouve » une action qui n'a pas eu lieu.
- **Correctif** : A-11, A-12.

#### T-06 [BLOQUANT - Erreur formelle/architecturale] Seuils d'approbation mesurés sur une grandeur que l'agent choisit, appel par appel
- **Défauts fusionnés** : 3.27, 3.30, 6.01, 6.03, 6.06.
- **Localisations** : tableau 31, p. 108; p. 109 (« 25 par tâche »); EXIG-AUT-07, p. 108; C.1, p. 216-217 (`montant_total_cad`); C.2, p. 218 (`approval_threshold.argument`); fiche B, p. 215 (`threshold_cad`).
- **Diagnostic** : un seuil est un contrôle seulement si la grandeur mesurée est hors du contrôle de celui qu'il borne. Dans l'exemple de référence, le seuil porte sur un argument redondant que l'agent fixe, il est évalué appel par appel et il est inscrit deux fois (fiche et catalogue) sans règle de préséance. Tant que les seuils d'étalonnage ne sont pas approuvés, la règle d'or est inopérante, et le défaut est en ouverture.
- **Contre-exemple** : l'agent crée un bon de 4 999 $ avec `montant_total_cad: 4999`, alors que les lignes totalisent 49 990 $. Ou bien il émet dix bons de 4 999 $ dans la même tâche. Aucune approbation n'est demandée.
- **Correctif** : A-13.

#### T-07 [BLOQUANT - Erreur formelle/architecturale] Triade létale évaluée agent par agent, sur une « session » non définie, alimentée par le seul marquage des outils
- **Défauts fusionnés** : 1.08, 1.54, 3.26, 3.34, 4.01, 4.18, 4.19, 4.20, 6.16, 6.63.
- **Localisations** : PRIN-07, p. 27; décision 6, p. 8; EXIG-ARC-23, p. 43; EXIG-AUT-10, p. 110 (déclencheur de cumul); tableau 31, P0, p. 108; EXIG-SEC-03, 04 et 06, p. 133-135; glossaire, « Contenu non fiable » et « Triade létale », p. 234 et 241.
- **Diagnostic** : la triade est une propriété du flux d'information. Le cadre l'évalue sur une fiche, de façon statique, et la détection dynamique ne lit que les sorties d'outils marquées. Elle laisse sans étiquette plusieurs entrées de contexte : mémoire injectée, récupération, déclencheur, tâche A2A entrante, événement. Une source non marquée passe pour fiable, contre PRIN-12. « Session » n'est défini nulle part, alors que MCP 2026-07-28 est sans état. Enfin, un outil P0 de recherche publique dont la requête est du texte libre est un canal d'envoi non marqué.
- **Contre-exemple** : voir [4.01]. Y lit un document piégé et le dossier client, puis délègue la « mise en forme » à X par A2A. X dispose d'un outil de courriel. Chaque fiche respecte la règle de deux, et le dossier sort.
- **Correctif** : A-17.

#### T-08 [BLOQUANT - Erreur formelle/architecturale] Les preuves de contenu qu'exigent la loi, l'évaluation et l'enquête n'ont aucun magasin admis
- **Défauts fusionnés** : 1.88, 3.20, 4.37, 4.41, 4.88, 5.01, 5.25, 5.30, 5.37.
- **Localisations** : EXIG-ORC-16, p. 96 (arguments en clair au journal de compensation); EXIG-AUT-22, p. 116; EXIG-OBS-07 et 08, p. 149; EXIG-OBS-12 et 13, p. 151; EXIG-EVA-02 et 04, p. 153; EXIG-CON-09, p. 177; EXIG-CON-18, p. 184; EXIG-CON-23 et 25, p. 187-188; EXIG-APP-09, 10 et 14, p. 193-195; tableau 58 (base de preuves en Industrialisation).
- **Diagnostic** : le cadre interdit le contenu dans la télémétrie, ne garde dans l'audit que des empreintes et détruit les captures de débogage après 14 jours. Il exige pourtant de produire pendant un an les renseignements personnels qui ont servi à une décision (art. 11 de la Loi sur le privé, EXIG-CON-09), d'enrichir le jeu d'évaluation à partir de la production, de remplir l'avis d'incident « à partir de la télémétrie » et de tenir un « dépôt de preuves unique » qui contredit la séparation du journal d'audit. Aucun magasin ne peut satisfaire ces exigences à la fois.
- **Contre-exemple** : une personne demande, dix mois après un refus de crédit, les renseignements et les facteurs qui ont fondé la décision (art. 12.1). Les traces n'ont pas de contenu, l'audit n'a que h, et la capture est détruite depuis neuf mois. Une obligation légale non dérogeable devient impossible à exécuter.
- **Correctif** : A-18, A-19.

#### T-09 [BLOQUANT - Erreur formelle/architecturale] Délégation : profondeur, chaîne de jetons, intersection et durée non spécifiées de façon cohérente
- **Défauts fusionnés** : 1.57, 1.58, 2.04, 2.07, 2.33, 3.18, 4.03, 4.04, 4.05, 4.06, 4.07, 4.08, 4.09, 4.10, 5.99, 6.04, 6.17, 6.64, 6.69.
- **Localisations** : PRIN-03, p. 26; § 5.6, étapes 5 et 8, p. 44; figure 7, p. 56; EXIG-ORC-04, p. 90; EXIG-ORC-23, p. 99; § 9.3 et EXIG-IAM-08 à 16, p. 122-127; tableau 35; EXIG-APP-08, p. 193; C.5, p. 220-221; glossaire, « Jeton délégué » et « Mandant ».
- **Diagnostic** :
  - l'EXIG-ORC-04 fait rejeter par la passerelle selon les `act` imbriqués, ce que la RFC 8693 (lit. 30) et l'EXIG-IAM-11 interdisent;
  - la passerelle qui termine TLS brise la liaison `cnf`;
  - la passerelle qui refait l'échange ajoute ou efface un acteur;
  - la portée de la tâche n'est pas représentée dans le jeton;
  - aucun plafond de durée ne borne les échanges successifs;
  - l'agent ambiant n'a pas de `subject_token`;
  - l'exécutant peut « blanchir » le niveau et la classe de l'appelant;
  - le « mandant » peut être un agent.
- **Contre-exemple** : l'agent A (N2, classe élevée) délègue à B (N3, classe modérée). B agit au palier P2 sans approbation, parce que la passerelle applique le niveau de B. Ou bien B échange de nouveau, toutes les 15 minutes, le jeton qu'il a reçu, et la délégation d'une tâche d'une heure dure une semaine.
- **Correctif** : A-15, A-16.

#### T-10 [BLOQUANT - Erreur formelle/architecturale] Frontière A2A / « agent comme outil » et critère agent/outil indécidables
- **Défauts fusionnés** : 1.21, 1.22, 6.02, 6.75.
- **Localisations** : § 3.1 (Outil); § 6.2, p. 48 (« planifie, conserve un état et peut renvoyer une question »); EXIG-INT-04 et 05, p. 49; EXIG-A2A-01, p. 68; glossaire, « Outil », p. 238-239.
- **Diagnostic** : l'EXIG-INT-05 (DEVRAIT) permet l'enveloppe « agent comme outil » dans un « domaine de confiance ». L'EXIG-A2A-01 (DOIT) impose A2A pour un autre cadriciel ou un autre domaine. Le critère agent/outil est une conjonction au § 6.2 et une disjonction dans l'EXIG-INT-05. Un serveur MCP qui gère des tâches et l'élicitation remplit le critère « agent ».
- **Contre-exemple** : un agent LangGraph appelle comme outil MCP un agent CrewAI du même domaine. Selon l'EXIG-INT-05, c'est permis; selon l'EXIG-A2A-01, c'est interdit.
- **Correctif** : A-20.

#### T-11 [BLOQUANT - Erreur formelle/architecturale] Statuts du catalogue et retrait : Contenir interdit, retrait de sécurité interdit, coexistence sans mécanisme
- **Défauts fusionnés** : 1.20, 1.23, 2.03, 2.13, 2.29, 2.30, 4.80, 5.03.
- **Localisations** : statut Contenir, p. 49; EXIG-INT-06 et 07, p. 51; tableau 15 (ligne MCP sans coexistence); EXIG-INT-14 à 19, p. 82-84; EXIG-MCP-20 contre EXIG-SEC-18 (granularité de la suspension); EXIG-GOV-14, p. 168; EXIG-GOV-20, p. 170.
- **Diagnostic** : les états du catalogue ne forment pas une machine cohérente. Contenir « tolère l'existant », alors que l'EXIG-INT-06 et l'EXIG-GOV-20 l'interdisent en production. L'EXIG-INT-14 autorise un retrait anticipé de sécurité que l'EXIG-INT-18 interdit. L'EXIG-INT-07 bloque les serveurs MCP antérieurs que l'EXIG-MCP-22 tolère jusqu'au 28 juillet 2027. La coexistence de deux versions majeures n'a aucun mécanisme de service, alors qu'une définition d'outil MCP ne porte aucune version.
- **Contre-exemple** : un serveur MCP en production présente une vulnérabilité exploitée. L'EXIG-INT-18 interdit de retirer sa version avant la fin de la coexistence de 60 jours, et aucun état « suspendu » ne permet de cesser de la servir sans la retirer.
- **Correctif** : A-21, A-22.

#### T-12 [BLOQUANT - Erreur formelle/architecturale] OpenTelemetry : une version d'émission impossible à garantir est exigée, et l'épinglage dérive
- **Défauts fusionnés** : 1.60, 2.94, 4.02, 4.35, 4.99 (d), 6.91.
- **Localisations** : tableau 15, p. 50; § 10.1, p. 145 (« L'épinglage ne dicte toutefois pas ce que les bibliothèques d'instrumentation émettent »; v1.41.1 désignée comme dernière version en vigueur); EXIG-OBS-01, p. 145 (v1.41.0); EXIG-OBS-05, p. 148; fiche B (`"genai_semconv": "1.41.0"`); p. 85.
- **Diagnostic** : l'exigence impose d'émettre selon la v1.41.0, alors que le paragraphe qui la précède établit que les instrumentations émettent par défaut la v1.36.0 ou une version antérieure. La conformité ne peut être mesurée qu'à la sortie d'une couche de correspondance, que le texte ne place qu'en lecture. Les composants de tiers n'émettent pas vers le collecteur de l'entreprise. Le corps hésite entre v1.41.0 et v1.41.1. `audit_lit` confirme que la v1.42.0 déplace GenAI vers un dépôt sans version étiquetée (lit. 35).
- **Contre-exemple** : un agent instrumenté par défaut émet `gen_ai.system` au lieu de `gen_ai.provider.name`. L'EXIG-OBS-05 interdit de l'homologuer, et l'option d'adhésion émet une version postérieure, tout aussi non conforme.
- **Correctif** : A-29.

#### T-13 [MAJEUR - Lacune méthodologique/omission] Usage unique du jeton d'approbation contre réessai idempotent, reprise durable et répliques
- **Défauts fusionnés** : 1.58, 2.05, 3.04, 3.41, 4.14, 6.10.
- **Localisations** : figure 9, étape 8, p. 74; EXIG-MCP-17, p. 64 (`requestState`); EXIG-ORC-21, p. 98 (clé « réutilisée telle quelle à chaque réessai »); EXIG-AUT-12 et figure 16, p. 111 (« une seule fois »); figure 18, p. 128; EXIG-SEC-25; C.6, p. 221.
- **Diagnostic** : si l'appel approuvé atteint la passerelle puis expire, le réessai présente un `jti` consommé et il est refusé. C'est sûr, mais il faut une nouvelle approbation, ce qui alimente la saturation des approbateurs (T10 de l'OWASP). Avec plusieurs répliques sans registre de `jti` atomique, l'usage unique n'est même pas garanti. Quatre tranches proposent la même issue sous des formes voisines.
- **Contre-exemple** : un paiement approuvé expire pendant le relais. L'orchestrateur réessaie avec la même clé : refus pour `jti` consommé. Une seconde approbation est demandée pour une action peut-être déjà exécutée.
- **Correctif** : A-10.

#### T-14 [MAJEUR - Erreur formelle/architecturale] Idempotence : vérifiée au mauvais endroit, clés instables à travers A2A et les événements, sans rétention ni borne de réessai
- **Défauts fusionnés** : 1.04, 1.05, 2.06, 3.12, 3.13, 3.14, 3.15, 3.17, 3.19, 3.42, 6.07.
- **Localisations** : décision 1, p. 8 (API « jamais réécrites »); EXIG-ARC-14, p. 37; § 5.2, p. 34 (Temporal, Step Functions); EXIG-ORC-12, p. 94; EXIG-ORC-21 à 23, p. 98-99; EXIG-ORC-27, p. 100; EXIG-AUT-17, p. 113; EXIG-EVT-08, p. 80; § 6.6, p. 70; fiche B, p. 215 (outil P3 sans clé).
- **Diagnostic** : seule l'extrémité qui produit l'effet sait si elle l'a déjà produit (argument de bout en bout, 3.1, travail 11). L'adaptateur d'un service « jamais réécrit » ne le sait pas sans un registre transactionnel. La clé dérive d'un identifiant de tâche local, qui change à travers A2A (le serveur attribue l'identifiant) et chez un consommateur d'événements. Aucune durée de conservation n'existe, alors que les exécutions durables n'ont pas de limite (lit. 70-71 : activités Temporal réessayées sans limite par défaut, Step Functions Standard réexécuté sous `Retry`). La spécification de la clé d'idempotence laisse la rétention à la charge du serveur (lit. 34).
- **Contre-exemple** : la clé d'une étape est purgée après 24 heures. Une exécution Temporal reprend au jour 3 depuis un point de contrôle antérieur et rejoue l'étape avec la même clé. Le service, qui n'a plus la clé, réexécute le paiement.
- **Correctif** : A-09.

#### T-15 [MAJEUR - Erreur formelle/architecturale] Mode dégradé : politique en cache sans validité, composants obligatoires sans objectif de disponibilité
- **Défauts fusionnés** : 1.06 (volet disponibilité), 1.07, 3.29, 4.12, 4.13, 5.11, 6.15.
- **Localisations** : EXIG-ARC-12, p. 36 (« en une seule opération »); EXIG-AUT-11, p. 110; EXIG-IAM-18, p. 129 (« la dernière politique distribuée »); § 11.4, p. 164 (registre consulté à chaque appel).
- **Diagnostic** : l'EXIG-AUT-11 refuse le P3 quand le service de politiques est indisponible. L'EXIG-IAM-18 continue d'appliquer la dernière politique. Le même appel a donc deux issues. Une politique en cache sans âge maximal fige le coupe-circuit et le retrait d'outil pendant la panne du plan de contrôle. La passerelle, le registre, le service d'approbation et le service d'audit sont obligatoires et fermés en cas de panne, mais aucun n'a d'objectif de disponibilité.
- **Contre-exemple** : le plan de contrôle tombe à 9 h. À 9 h 05, le comité suspend un serveur MCP compromis. La passerelle continue de servir l'outil jusqu'au rétablissement, puisque la suspension voyage par le plan de contrôle.
- **Correctif** : A-04.

#### T-16 [MAJEUR - Erreur formelle/architecturale] Coupe-circuit et révocation : portée dépendante de la durée des jetons, cibles divergentes, exercice prescrit trois fois
- **Défauts fusionnés** : 3.54, 3.81, 4.15, 4.99 (a, b), 5.36, 5.48.
- **Localisations** : EXIG-ORC-28, p. 100; EXIG-IAM-07, p. 121; EXIG-IAM-15, p. 126; EXIG-IAM-20, p. 130; EXIG-SEC-26, p. 144; EXIG-GOV-13; EXIG-APP-06 et 16, p. 193-195 (« 24 heures »); tableau 61 et § 15.3, p. 205-206 (15 minutes).
- **Diagnostic** : l'arrêt n'atteint que les systèmes qui prennent en charge SSF ou CAEP. Ailleurs, un jeton émis reste valide jusqu'à son expiration, si bien que la cible de 15 minutes n'est atteignable que si la durée des jetons y est bornée. La cible est un DEVRAIT à un endroit, un DOIT à un autre et une « cible proposée » au tableau 61. Le délai contractuel du fournisseur est de 24 heures.
- **Contre-exemple** : un jeton d'une heure, émis vers un système sans CAEP, reste utilisable 59 minutes après l'arrêt, et l'exercice trimestriel mesure pourtant « 15 minutes ».
- **Correctif** : A-05.

#### T-17 [MAJEUR - Erreur formelle/architecturale] Journal d'audit : écrit après l'effet, chaînage sans ancrage, troncature indétectable
- **Défauts fusionnés** : 1.96, 4.14 (volet audit), 4.39, 4.91, 6.09, 6.12.
- **Localisations** : décision 8, p. 8 (« inaltérable »); figure 18, p. 128 (« RETOUR : 9 · Tracer et journaliser »); EXIG-OBS-11 à 13, p. 151; C.8, p. 223-224.
- **Diagnostic** : `audit_lit` invalide l'affirmation « le chaînage rend toute suppression détectable » (Crosby-Wallach 2009, RFC 9162; lit., section 3, travaux 1 et 2). Un chaînage linéaire signé par le service lui-même ne détecte ni la troncature de la queue ni la réécriture par le détenteur de la clé. « Même flux » n'est pas défini. La purge à l'échéance rompt la chaîne. L'enregistrement est produit au retour : une action exécutée sans réponse n'est pas auditée.
- **Contre-exemple** : l'administrateur du service d'audit supprime les 200 derniers enregistrements d'une heure. La chaîne restante est valide, et rien ne détecte la suppression.
- **Correctif** : A-19.

#### T-18 [MAJEUR - Erreur formelle/architecturale] Force normative : périmètre, annexes, catalogue qui « fait foi », contrats de rang 1, départage
- **Défauts fusionnés** : 1.12, 1.13, 1.14, 1.15, 3.25, 6.05, 6.23, 6.26.
- **Localisations** : § 1.4, p. 13; § 1.5, p. 13; § 1.6, p. 14; § 3.1, p. 20 (« font foi »); § 4.3, p. 29; annexe B, p. 212 (« normatif par son contenu »); annexe C, p. 215 (« normatifs par leur forme »); H.1, p. 275; page de titre et historique.
- **Diagnostic** : le § 1.4 limite le normatif aux blocs EXIG, aux PRIN et aux tableaux expressément visés. Il en exclut pourtant les règles d'interprétation (§ 1.2, 1.5, 1.6, 4.3), les définitions qui « font foi » et les annexes B et C, qui se déclarent normatives. Le catalogue « fait foi » sur des versions que des DOIT figent dans le texte. Un engagement contractuel de rang 1 peut écarter un non-dérogeable. « Le plus strict » n'a pas d'ordre défini. Deux PDF portent « Version 1.1 ».
- **Contre-exemple** : un contrat d'éditeur signé après l'adoption permet à son agent d'exécuter des P3 sans approbation. Le rang 1 du § 4.3 le fait primer sur l'EXIG-GOV-17.
- **Correctif** : A-23, A-14.

#### T-19 [MAJEUR - Erreur formelle/architecturale] Sources de vérité multiples pour une même obligation
- **Défauts fusionnés** : 3.39, 3.40, 3.64, 3.75, 4.42, 4.99 (f), 5.08, 5.13, 5.16, 5.17, 5.42, 5.68, 5.73, 6.08.
- **Localisations** :
  - réévaluation : EXIG-AUT-05, EXIG-ARC-09, EXIG-EVA-01, EXIG-SEC-01, -02 et -24, EXIG-GOV-12, EXIG-CON-03, annexe B;
  - art. 12.1 : EXIG-AUT-22 et 23, EXIG-CON-07, 08 et 21, A.5;
  - non-dérogeables : EXIG-GOV-17, § 4.3, grille A.1 à A.8;
  - conservation : EXIG-CON-10 et 16, J2a;
  - plafond : § 8.1 ou EXIG-CON-02.
- **Diagnostic** : quand deux textes normatifs énoncent la même obligation avec des contenus différents, l'un des deux est nécessairement violé ou vidé. Les divergences sont de fond. La réévaluation suit le changement de modèle au lieu de le précéder ([4.42]). L'avis de l'art. 12.1 est rattaché à une mesure mensuelle alors qu'il est dû au moment de la décision ([3.39]). La classification est circulaire avec le caractère automatisé de la décision ([5.16]). Deux durées de conservation coexistent ([5.73]).
- **Contre-exemple** : un changement d'invite système déclenche une réévaluation selon l'EXIG-GOV-12, mais non selon l'EXIG-CON-03. L'équipe qui applique le chapitre 12 met en production sans réévaluer.
- **Correctif** : A-24, A-25.

#### T-20 [MAJEUR - Lacune méthodologique/omission] Feuille de route informative, incompatible avec les exigences et sans régime transitoire
- **Défauts fusionnés** : 1.03, 1.91, 5.05, 5.07, 5.40, 5.41, 5.42, 5.43, 5.44, 5.45, 5.108.
- **Localisations** : sommaire, p. 8-9; figure 28 et tableau 58, p. 200-201 (« Pass. d'agents (P0, P1 puis P2) »); règles de progression et ATTENTION, p. 199-202; tableau 60, p. 203; tableau 61, p. 204-206; annexe B, p. 212; § 11.4-11.5.
- **Diagnostic** : le chapitre 15 est informatif. Il tolère des contournements que des DOIT interdisent, planifie en phases des obligations légales déjà en vigueur et n'ouvre jamais la passerelle au palier P3, dont dépend l'approbation signée. Il ouvre aussi le palier P2 avant les sagas et les compensations que l'EXIG-AUT-08 exige pour le P2. Le plafond N2 « hors domaine » d'un appel qui contourne la passerelle n'a aucun point d'application. Les agents existants n'ont pas de régime : sans fiche, ils n'obtiennent aucun jeton. Le pilote reçoit des données réelles avant l'équipe rouge et l'homologation. Des choix du cadre (validation E-23 de tous les modèles, migration MCP) sont présentés comme des échéances externes, alors qu'E-23 ne fixe aucune échéance de validation des modèles existants (lit. 23).
- **Contre-exemple** : au jalon J2, un agent N2 doit exécuter un paiement P3 approuvé. La passerelle n'est ouverte qu'aux paliers P0 à P2 : soit le paiement contourne la passerelle (EXIG-GOV-17 violée), soit l'agent ne peut pas fonctionner à son niveau homologué.
- **Correctif** : A-25, A-26.

#### T-21 [MAJEUR - Erreur formelle/architecturale] Échelles mal bornées : N0, flux assisté, P2/P3, N3/N4
- **Défauts fusionnés** : 1.16, 1.17, 1.18, 3.05, 3.32, 3.60, 3.63.
- **Localisations** : § 3.1, p. 21-23; § 3.2, p. 23 (flux assisté, « patron par défaut »); § 3.3, p. 24; tableau 28, p. 104; tableau 31, p. 108; EXIG-AUT-08, p. 109; EXIG-ORC-17.
- **Diagnostic** : N0 (« aucun modèle ») est un niveau d'agent, alors qu'un agent emploie un modèle par définition. Le patron par défaut, le flux assisté par IA, n'a aucun niveau. « Compensable » n'exclut pas « irréversible », si bien qu'un effet externe compensable (un courriel suivi d'un rectificatif) peut être classé P2. N4 ne se distingue de N3 par aucun attribut que la passerelle observe. Les compensations n'ont pas de palier.
- **Contre-exemple** : un envoi de lettre à un client, « compensé » par une lettre rectificative, est classé P2 et exécuté sans approbation par un agent N3.
- **Correctif** : A-27, A-08.

#### T-22 [MAJEUR - Lacune méthodologique/omission] Approbation : renvois à la figure 15 au lieu du contrôle calculé, hors bande sans statut, charge des approbateurs non dimensionnée
- **Défauts fusionnés** : 3.31, 3.33, 3.35, 3.36, 3.72, 4.21, 4.61.
- **Localisations** : tableau 31 (« hors bande à chaque appel »); EXIG-AUT-09, 12, 14, 15 et 20, p. 108-115; ATTENTION, p. 114; figure 16; tableau 46, p. 171 (« P3 toujours soumis à une approbation hors bande »); EXIG-SEC-03 à 06.
- **Diagnostic** : le hors bande est un DOIT au tableau 46, une ligne de tableau au chapitre 8 et un DEVRAIT (CIBA) à l'EXIG-AUT-14. Plusieurs exigences renvoient à la figure 15, qui n'est qu'une composante du contrôle calculé par l'EXIG-AUT-10. La présomption d'injection multiplie les approbations sans aucun dimensionnement, ce qui alimente l'approbation machinale. Le WIMSE AIMS précise qu'une confirmation locale ne suffit pas (lit. 62).
- **Correctif** : A-12, A-14.

#### T-23 [MAJEUR - Erreur formelle/architecturale] Règles de sortie réseau (anti-SSRF) dispersées et incohérentes
- **Défauts fusionnés** : 2.17, 2.18, 4.24, 4.74.
- **Localisations** : EXIG-MCP-12, p. 61; EXIG-MCP-19, p. 64-65; EXIG-A2A-12, p. 73; EXIG-SEC-12, p. 139.
- **Diagnostic** : quatre listes de plages bloquées, deux règles contraires sur les redirections (« ne pas suivre » ou « valider chaque redirection »), aucun traitement de la réassociation DNS entre la vérification et la connexion, ni du *domain fronting* que le texte décrit lui-même. Les cibles internes légitimes, elles, sont bloquées.
- **Correctif** : A-33.

#### T-24 [MAJEUR - Lacune méthodologique/omission] Portes, seuils et comparaisons sans règle de décision statistique
- **Défauts fusionnés** : 2.32, 3.38, 4.34, 4.43, 5.38, 5.46, 5.47.
- **Localisations** : EXIG-ORC-02, p. 87; EXIG-AUT-21, p. 115 (5 % et 1 %); EXIG-SEC-24, p. 144; EXIG-EVA-02 à 04 et tableau 42, p. 153; § 14.2, p. 198; tableau 61, p. 204-206.
- **Diagnostic** : « moins de 0,5 % de réponses non ancrées » sur un jeu de 50 à 200 scénarios n'est pas démontrable. Il faut au moins 600 essais sans échec pour borner le taux à 0,5 % avec 95 % de confiance (règle de trois). « Le gain couvre le surcoût » n'a ni protocole ni intervalle. L'échantillonnage à proportion fixe n'a aucune puissance à faible volume. La reproductibilité de la maturité est affirmée sans mesure d'accord entre évaluateurs.
- **Correctif** : A-32 et preuves 9 à 11 de la section 3.3.

#### T-25 [MAJEUR - Erreur formelle/architecturale] Contrôles de localisation et de finalité confiés à des passerelles qui ne voient pas les flux visés
- **Défauts fusionnés** : 4.99 (j), 5.18, 5.95.
- **Localisations** : EXIG-CON-05 et 06, p. 175; EXIG-APP-11, p. 194; p. 154 (résidence).
- **Diagnostic** : les usages secondaires (entraînement, analytique) ne transitent pas par la passerelle d'agents. Le plan mémoire et les index ne passent pas par la passerelle de modèles. La notion de résidence est incohérente (« canadienne » contre « hors du Québec », art. 17).
- **Correctif** : A-28.

#### T-26 [MAJEUR - Erreur formelle/architecturale] Rôles et indépendance : RACI autocontrôlée, équipe FinOps inexistante, « propriétaire » ambigu
- **Défauts fusionnés** : 4.51, 4.97, 4.99 (i), 5.02.
- **Localisations** : tableaux 43 et 44, p. 160-162; EXIG-GOV-03, p. 161; A.2, p. 209; EXIG-FIN-03 et 10; figure 23; C.7.
- **Diagnostic** : le responsable technique est A et R de sa propre évaluation, et le parrain approuve le niveau qu'il demande. L'EXIG-GOV-03 est respectée à la lettre, mais l'argument d'indépendance de la p. 162 tombe. Des DOIT visent une équipe FinOps absente des rôles.
- **Correctif** : A-34.

#### T-27 [MAJEUR - Lacune méthodologique/omission] Méthode des sources non reproductible, catégorie C citée, doublons, versions déjà dépassées, identité documentaire
- **Défauts fusionnés** : 1.11, 6.18, 6.20, 6.21, 6.22, 6.24, 6.25, 6.26, 6.27, 6.28, 6.29, 6.30, 6.31, 6.86, 6.90.
- **Localisations** : Méthode, p. 2; § 1.7, p. 14; F.1 à F.4, p. 241-249; tableau 66; annexe G; H.1 à H.5.
- **Diagnostic** : 121, 428 puis 473 références sont annoncées, et le décompte inclut des doublons. `audit_lit` en vérifie quatre ([6]/[65], [69]/[70], [287]/[288], [360]/[363]) et deux paires de doubles citations ([176]/[327], [87]). La tranche 6 en relève une vingtaine. Les deux constats sont compatibles, puisqu'`audit_lit` n'a vérifié qu'un échantillon. Des blogues et un agrégateur, de catégorie C (« jamais cité »), appuient des obligations du RIA. L'annexe H corrige le corps tout en se déclarant sans effet, et sa règle de divergence est fausse pour les errata. Le signal « révision de MCP » est déclaré survenu sous la mauvaise exigence, et une exigence bloquante repose sur une suite de tests alpha.
- **Correctif** : A-22, A-31.

#### T-28 [MAJEUR - Dérive de notation/clarté] Dérives de chiffres, de dates, de versions et de renvois entre chapitres
- **Défauts fusionnés** : 1.10, 1.89, 1.93, 1.95, 1.97, 4.99 (c, e, g, h, k), 5.26, 5.61, 5.62, 5.88, 5.105, 6.77, 6.92, 6.106, 6.109, 6.114.
- **Dérives relevées** :
  - **E-23** : annoncée dans la « matrice de correspondance unique » (décision 10), mais absente du tableau 50, que l'EXIG-CON-18 utilise comme schéma d'étiquetage (MAJEUR).
  - **Décompte des exigences** : 287 dans le corps, 272 au report 7 de H.3. Le recomptage dans `full.txt` donne 287 blocs (ARC 25, INT 23, MCP 22, A2A 15, EVT 10, ORC 30, AUT 23, IAM 21, SEC 26, OBS 13, EVA 6, FIN 10, GOV 20, CON 26, APP 17), plus 2 identifiants EXIG-AMF propres à l'annexe H. Le « 272 » omet le préfixe A2A.
  - **Dates de l'état des sources** : 27 ou 28 octobre.
  - **Nombre d'annexes** : « sept annexes, de A à G » au § 1.5, alors que le document en compte huit.
  - **Comité A2A** : « huit entreprises » aux § 6.6 et 13.1, alors que la source indique neuf sièges et que l'erratum ne vise que le § 6.6.
  - **Retrait accéléré de MCP** : « exceptionnel » (p. 17 et 57) contre « risque de sécurité actif » (p. 169). La source confirme la seconde formule (lit. 4).
  - **Révision du catalogue** : confiée au comité (§ 6.3) ou à l'architecture d'entreprise (EXIG-GOV-18).
  - **ISO/IEC 42001** : associée au niveau de maturité 4 ou au niveau 5.
  - **Loi 25** : « pour l'essentiel depuis 2024 » à la p. 20, alors que l'essentiel est en vigueur depuis 2023 (lit. 24).
  - **OAuth 2.1** : la révision −16 et son expiration sont dépassées (lit. 29).
  - **Homonymes** : « palier » (évaluation et outil) et « point de contrôle ».
  - **Enveloppe** : quatre ou cinq dimensions selon le passage.
  - **Encadré sur la latence** : répété trois fois, en trois versions.
- **Correctif** : A-30, A-31, et les correctifs ponctuels des défauts cités.

### 2.0.1 Arbitrages transversaux retenus

**Réconciliation des options divergentes des tranches.** Les tranches ont proposé, sous des numéros différents, des options qui se recoupent. Sept désaccords réels ont été tranchés comme suit, et le reste des propositions converge.

| Sujet | Options des tranches | Retenu | Motif |
|---|---|---|---|
| Portée de la passerelle | t1 A1 : tout MCP, A2A et P2-P3, avec un point d'application local équivalent admis; t2 A1 : entrée de catalogue sans MCP; t3 A4 : tout P2-P3; t4 A1 : tout MCP et A2A, et P2-P3 par MCP | A-01 : tout MCP et A2A, et tout P2-P3 par un outil MCP derrière la passerelle; un déploiement en *sidecar* est une instance de la passerelle, pas une autre implémentation | Un seul vérificateur d'approbation et un seul registre de `jti`; l'option de repli de la t3 multiplie les implémentations à homologuer |
| Politique en cache échue | t4 A4 : seul P0 passe; t6 A14 : refus de P2 et P3 | A-04 : seul P0 passe | Une lecture P1 sensible, après une révocation non reçue, est une fuite |
| Source unique des déclencheurs de réévaluation | t4 A8 et t6 A11 : EXIG-GOV-12; t5 A10 : EXIG-CON-03 | A-24 : EXIG-GOV-12 | Le cycle de vie porte le « avant la mise en production »; l'EXIG-CON-03 garde le lien avec E-23 par renvoi |
| Source unique de l'art. 12.1 | t3 A9 : CON-07 à 09, AUT-22 et 23 en renvoi; t5 A10 : CON-07, avec AUT-23 pour le test | A-24 : CON-07 (obligations) et CON-08 (test de révision significative, repris d'AUT-23); AUT-22 et AUT-23 deviennent des renvois | Une obligation légale relève d'un seul chapitre, le chapitre 12 |
| Identité de compensation | t3 A1 : service de compensation; t4 A2 : moteur durable; t5 A3 : orchestrateur | A-06 : identité de compensation de l'orchestrateur, ou du coordinateur de saga, distincte de celle de l'agent | Les trois options désignent le même composant; le nom est unifié |
| Session | t3 A7 : contexte du modèle depuis le dernier contexte vierge; t6 A7 : tâche racine et dérivées | A-17 : tâche racine et tout ce qui en dérive, et contexte vierge défini par l'absence de données étiquetées | Le contexte du modèle n'est pas observable par la passerelle, contrairement à la tâche |
| Auto-approbation du mandant | t6 A4 (c) : approbateur toujours distinct du mandant (DOIT); t3 (3.36) : le cas du mandant qui approuve sa propre action existe | A-12 : la confirmation du mandant est admise sauf pour un P3 de classe élevée, rôle tracé dans l'audit | L'interdire rendrait impossible tout assistant N2 interactif; le risque est traité par la traçabilité et la double approbation là où il est élevé |
| Critère agent/outil | t6 A10 : « choisit des actions à effet ou conserve un état » | A-20 : « choisit lui-même, au moyen d'un modèle, les actions qu'il exécute » | Avec « conserve un état », un serveur MCP qui gère des tâches deviendrait un agent ([1.22]) |
| Jeton d'approbation | t6 A4 : lié à l'agent par `cnf`; t3 A5 : conservé par la passerelle | A-10 et A-15 : conservé par la passerelle, apparié à l'appelant authentifié | Le jeton reste ainsi hors du contexte du modèle (WIMSE AIMS, lit. 62), et la liaison à l'appelant devient implicite |

**Nouveaux identifiants.** Les nouveaux identifiants sont attribués ici, une fois pour toutes, afin que les six implémenteurs n'entrent pas en collision. Aucun identifiant existant n'est réattribué.

| Identifiant | Objet | Arbitrage |
|---|---|---|
| EXIG-ARC-26 | Agents intégrés aux logiciels-services | A-03 |
| EXIG-AUT-24 | Grandeur, unité, portée et fenêtre des seuils | A-13 |
| EXIG-ORC-31 | Canal de compensation | A-06 |
| EXIG-EVT-11 | Courtier d'événements, point d'application | A-02 |
| EXIG-IAM-22 | Disponibilité et validité de la politique en cache | A-04 |
| EXIG-OBS-14 | Dossier de décision | A-18 |
| EXIG-EVA-07 | Dépôt d'évaluation | A-18 |
| EXIG-GOV-21 | Régime transitoire et exigibilité | A-26 |
| EXIG-APP-18 | Aucune clause contraire à l'EXIG-GOV-17 | A-23 |

---

**A-01 — Portée de la passerelle d'agents.**
- **Décision** : la passerelle est le passage obligé de tout appel MCP et A2A, et de toute action P2 ou P3, quel que soit le domaine.
- **Règle** :
  - EXIG-ARC-01 : « Dans tout environnement autre qu'un poste de développement individuel sans justificatif de production, tout appel d'un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3, DOIVENT passer par la passerelle d'agents, vers une version et une empreinte approuvées. Une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Seule une fonction locale de palier P0 ou P1, exécutée dans l'unité de déploiement de l'agent, sur les données de son propre domaine et inscrite au catalogue avec son palier, peut s'en dispenser; l'accès direct à une ressource de son domaine reste soumis à la décision par appel du serveur de ressources (EXIG-IAM-17). Une instance de la passerelle peut être déployée au plus près de l'agent (*sidecar*), à condition de partager la politique, le registre des jti et le journal d'audit des autres instances. »
  - « Environnement serveur » est défini au glossaire par renvoi à cette règle.
  - EXIG-MCP-01 : ajouter « sauf la fonction locale P0-P1 de l'EXIG-ARC-01 ».
  - EXIG-IAM-17 : « tout appel vers un serveur MCP ou un pair A2A, quel que soit le domaine, et tout accès à une ressource d'un autre domaine ».
  - Tableau 10 : « fonction locale P0-P1 seulement ».
  - Décision 2 et § 6.2 : « Rien ne contourne les points d'application : la passerelle d'agents (MCP, A2A, P2-P3), la passerelle de modèles (inférence) et le courtier (événements, EXIG-EVT-11). »
  - Tableau 61 : la couverture compte tous les appels MCP et A2A.
  - Stdio et serveur local en Streamable HTTP sur boucle locale : permis seulement sur un poste de développement sans justificatif de production (EXIG-MCP-08).
- **Touche** : sommaire (décision 2); tableau 10; § 5.1, 5.6; § 6.2; EXIG-ARC-01, MCP-01, MCP-08, AUT-10, IAM-17; tableau 61; glossaire; annexe A (test négatif : outil local P3 hors passerelle refusé à l'homologation).
- **Résout** : 1.01, 1.19, 1.44, 2.01, 2.11, 3.28, 4.60, 4.99 (m).

**A-02 — Le courtier d'événements, point d'application des politiques.**
- **Décision** : le courtier, avec l'intercepteur de publication de la plateforme, est un point d'application au même titre que la passerelle, pour la publication et la consommation. Il ne remplace pas la passerelle pour l'effet.
- **Règle** (nouvelle EXIG-EVT-11) :
  - « Le courtier et l'intercepteur de publication DOIVENT authentifier le producteur, appliquer les listes de contrôle d'accès par sujet, poser eux-mêmes les attributs de gouvernance (identité de l'agent producteur, délégation, compteur et plafond de sauts, étiquettes de l'A-17) et refuser un événement dont le schéma n'est pas épinglé. »
  - « Est un événement d'agent tout événement publié sous une identité d'agent inscrite au registre. »
  - « Le plafond de sauts appliqué est le minimum du plafond du flux et de celui de chaque sujet traversé, et un plafond de largeur (événements par trace) s'y ajoute. »
  - « Toute action P2 ou P3 qu'un consommateur exécute à la suite d'un événement passe par la passerelle (A-01), sous la délégation référencée par l'événement ou, à défaut, sous un mandat de service inscrit pour le sujet. »
  - EXIG-EVT-07 est maintenue (aucune décision sur `authtype` ou `authid` fournis par le producteur).
- **Touche** : § 6.2, 6.7 (EXIG-EVT-04, 06, 07, 08); EXIG-ORC-04 et 08; § 9.4; § 10.1; décision 2.
- **Résout** : 1.09, 2.02, 2.26, 2.27, 2.28, avec 2.35 par A-06.

**A-03 — Agents intégrés aux logiciels-services.**
- **Décision** : un régime propre, fondé sur des contrôles compensatoires contractuels et d'identité, plutôt qu'une dérogation au cas par cas.
- **Règle** (nouvelle EXIG-ARC-26) : « PRIN-09, EXIG-ARC-03 et EXIG-ARC-08 visent les agents dont l'entreprise contrôle l'exécution. Un agent intégré à un logiciel-service DOIT :
  - (a) être inscrit au registre avec sa classe, son niveau et les actions qu'il exécute dans le logiciel-service;
  - (b) n'atteindre les systèmes d'enregistrement de l'entreprise que par la passerelle d'agents, comme client externe;
  - (c) relever d'un contrat qui comporte les clauses des EXIG-APP-05, 06, 08 et 13 (préavis de changement de modèle opposable);
  - (d) disposer d'un mécanisme d'arrêt propre (fournisseur d'identité, retrait des consentements OAuth, CAEP), documenté à la fiche et éprouvé à l'exercice de l'EXIG-SEC-26;
  - (e) utiliser des schémas d'outils de tiers épinglés par l'entreprise (EXIG-INT-02 : "gérés" signifie "épinglés et approuvés").

  Une action P3 exécutée dans le logiciel-service exige un mécanisme d'approbation du fournisseur jugé équivalent à l'EXIG-AUT-12 à l'homologation. À défaut, l'agent est plafonné à N2 et chaque action P3 est approuvée dans la console de l'éditeur, approbation consignée à la fiche. »
- La quarantaine (EXIG-GOV-10) et la suspension (ATTENTION, p. 165) se définissent par type de source : passerelle pour les agents contrôlés, mécanisme (d) pour les autres.
- **Touche** : PRIN-09; § 2.4; § 5.2 (EXIG-ARC-03, 08, 11); tableau 12; EXIG-INT-02; EXIG-FIN-03; § 11.4-11.5 (EXIG-GOV-07, 08, 10); EXEMPLE, p. 167; ch. 13 (EXIG-APP-05, 06, 13); annexe B.
- **Résout** : 1.02, 1.24, 5.10, 5.12.

**A-04 — Mode dégradé et disponibilité.**
- **Décision** : une politique en cache vaut service disponible pendant sa durée de validité, et seulement pendant celle-ci. Les composants obligatoires ont un objectif de disponibilité.
- **Règle** (nouvelle EXIG-IAM-22) :
  - « La passerelle d'agents, le registre, le catalogue, le service de politiques, le service d'approbation, le registre des jti et le service d'audit DOIVENT avoir un objectif de disponibilité fixé par l'entreprise, inscrit au catalogue et mesuré, ainsi qu'une redondance qui le tient. »
  - « Chaque politique distribuée porte une durée de validité inscrite au catalogue. Tant qu'elle n'est pas échue, elle vaut service disponible au sens de l'EXIG-AUT-11. Échue, la passerelle ne laisse passer que les appels P0. »
  - « Un état dynamique illisible (marquage, compteurs, état de la fiche) impose le refus. »
  - « La liste de suspension (agents, outils, versions) DOIT être poussée par un canal signé indépendant du plan de contrôle, et appliquée même quand celui-ci est indisponible. »
  - EXIG-IAM-18 : remplacer « la dernière politique distribuée » par « la dernière politique distribuée, tant qu'elle n'est pas échue (EXIG-IAM-22) ».
  - EXIG-AUT-11 : ajouter le service d'audit et le registre des jti à la liste des dépendances. Les compensations suivent l'A-06.
  - La porte 3 des « sept portes » (p. 129) est reformulée en conséquence.
- **Touche** : § 5.3 (tableau 33); EXIG-ARC-12; EXIG-AUT-11; § 9.4 (EXIG-IAM-17, 18, 20, portes); § 11.4; § 13.2; glossaire (« plan de contrôle », « service de politiques »).
- **Résout** : 1.06 (volet disponibilité), 1.07, 3.29, 4.12, 4.13, 5.11, 6.15.

**A-05 — Coupe-circuit et révocation.**
- **Décision** : une source unique de la cible, une durée de jeton bornée par la cible, un seul exercice.
- **Règle** :
  - EXIG-IAM-20 est la source unique : « Le coupe-circuit arrête l'agent vers l'avant : il refuse tout nouvel appel sous l'identité de l'agent, sur toutes les instances de la passerelle, par le canal de l'EXIG-IAM-22. Il ne vise pas le canal de compensation (EXIG-ORC-31), sauf décision distincte. Le délai mesuré va de la décision d'arrêt au refus du dernier appel dans tous les systèmes (tableau 61). La cible est fixée par l'entreprise, proposée à 15 minutes. »
  - EXIG-IAM-15 (DOIT) : « Un jeton destiné à un système qui ne prend en charge ni SSF ni CAEP DOIT avoir une durée de vie au plus égale à la cible, ou ce système DOIT n'être joignable que par la passerelle. »
  - Un seul exercice trimestriel, porté par l'EXIG-SEC-26, auquel renvoient l'EXIG-ORC-28 et l'EXIG-IAM-20.
  - EXIG-APP-16 : distinguer la coupure côté entreprise (mécanisme de l'EXIG-APP-06, cible de l'EXIG-IAM-20) de la révocation et de la destruction côté fournisseur en fin de contrat (24 heures).
  - EXIG-IAM-07 et EXIG-GOV-13 sont alignées sur un seul traitement des agents orphelins.
- **Touche** : § 7.8 (EXIG-ORC-28); § 9.2-9.4 (EXIG-IAM-07, 15, 20); § 9.9 (EXIG-SEC-26); § 11.4 (EXIG-GOV-13); § 13.3 (EXIG-APP-06, 16); § 15.3; tableau 61.
- **Résout** : 3.54, 3.81, 4.15, 4.99 (a, b), 5.36, 5.48.

**A-06 — Canal de compensation.**
- **Décision** : les arrêts agissent vers l'avant. Une compensation déclarée d'une étape journalisée comme exécutée passe par un canal distinct, qui reste ouvert.
- **Règle** (nouvelle EXIG-ORC-31) : « Les compensations DOIVENT s'exécuter sous une identité de compensation propre à l'orchestrateur de la saga, ou au coordinateur de saga en chorégraphie, distincte de celle de l'agent et inscrite au registre. Cette identité :
  - (a) n'est autorisée qu'aux outils de compensation déclarés au catalogue pour une étape inscrite comme exécutée au journal de compensation de la même tâche;
  - (b) passe toujours par la passerelle ou par le courtier, et chaque appel est audité;
  - (c) n'est touchée ni par le coupe-circuit, ni par la suspension, ni par la révocation de l'agent, ni par l'épuisement de son enveloppe, ni par le plafond de sauts, ni par l'échéance de son mandat;
  - (d) dispose d'une réserve de budget calculée à la conception, hors de l'enveloppe de l'agent;
  - (e) peut être suspendue par une décision distincte, motivée et journalisée.

  Si la passerelle est indisponible, la compensation entre dans une file persistée et l'EXIG-ORC-18 (escalade humaine) s'applique à l'échéance fixée à la fiche. »
- Toute chorégraphie qui produit des effets sur plusieurs systèmes d'enregistrement DOIT avoir un coordinateur de saga inscrit au registre, qui tient le rôle de l'orchestrateur des EXIG-ORC-16 à 18.
- La suspension de sécurité (immédiate) est distinguée de la suspension administrative (nouvelles tâches bloquées, avis préalable). La compensation automatique (sagas en cours) est distinguée de la réparation métier (actions terminées, décidée par le propriétaire métier, § 12.8, étape 4).
- PRIN-12 : « échouer en mode fermé vers l'avant; ne jamais laisser une saga à moitié exécutée faute de pouvoir compenser ».
- **Touche** : PRIN-12; § 6.7 (EXIG-EVT-06); § 7.2 (EXIG-ORC-08); § 7.5 (EXIG-ORC-15 à 18); § 7.8 (EXIG-ORC-26, 28); EXIG-AUT-11 et 18; § 9.2-9.4 (EXIG-IAM-07, 18, 20, figure 18); § 10.6 (EXIG-FIN-04, 05); § 11.4-11.5 (EXIG-GOV-08, 09, 16); § 12.8 (EXIG-CON-23); C.7; annexe A.
- **Résout** : 1.06, 2.35, 3.02, 3.09, 4.16, 4.49, 5.09.

**A-07 — Compensation d'une étape incertaine.**
- **Décision** : on ne compense pas une étape dont l'issue est inconnue avant d'avoir clôturé l'opération chez le système visé.
- **Règle** : remplacer dans l'EXIG-ORC-16 la phrase « Une étape dont l'issue est inconnue est traitée comme possiblement exécutée… » par : « Avant de compenser une étape dont l'issue est inconnue, l'orchestrateur DOIT soit clôturer l'opération chez le système visé (annulation ou révocation de la clé d'idempotence, de sorte que toute arrivée tardive soit rejetée), soit l'interroger par sa clé jusqu'à une issue définitive. Si aucune des deux voies n'existe, l'étape passe en réconciliation différée, confiée à une personne (EXIG-ORC-18), et n'est ni compensée ni replanifiée à l'aveugle. »
- Une étape incertaine NE DOIT PAS être replanifiée avec d'autres arguments (nouvelle clé) avant sa résolution. L'EXIG-ORC-21 est modifiée en conséquence.
- L'EXIG-ORC-20 ajoute trois tests : arrivée tardive de l'original après la compensation, compensation sous coupe-circuit et compensation pendant une panne de la passerelle.
- Le tableau 68, no 31, n'est plus présenté comme corrigé.
- **Touche** : § 7.5 (EXIG-ORC-16, 17, 20, figure 13); § 7.6 (EXIG-ORC-21, 22); tableau 68; glossaire (« Compensation »).
- **Résout** : 3.01, 3.11, 3.13, 6.19.

**A-08 — Palier et approbation des compensations.**
- **Décision** : une compensation est un outil, avec son propre palier. La compensation exacte d'une étape approuvée est approuvée avec elle.
- **Règle** :
  - EXIG-ORC-17 : « Chaque compensation est un outil inscrit au catalogue avec son palier, référencé par le champ `compensation` de l'outil d'origine (C.1). »
  - EXIG-AUT-12 : « La demande d'approbation d'une étape P2 ou P3 inclut l'empreinte de sa compensation déclarée, bornée au montant et aux bénéficiaires d'origine et liée à la même clé d'idempotence. Cette compensation est approuvée avec l'étape. Toute autre compensation P3 exige une nouvelle approbation. »
  - Exemple normatif : une préautorisation annulable est P2, la capture est P3.
  - La figure 13 est corrigée : aucun débit P3 avant le pivot, et la compensation se fait de k à 1 pour les étapes exécutées.
- **Touche** : § 7.5 (figure 13, EXIG-ORC-15, 17); § 8.3 (tableau 31, EXIG-AUT-08, 09); § 8.5 (EXIG-AUT-12); C.1; C.6.
- **Résout** : 3.05, 3.06, 3.07 (en partie), 3.08 (ordre déclaré au catalogue).

**A-09 — Idempotence de bout en bout.**
- **Décision** : l'idempotence se vérifie chez celui qui produit l'effet. La clé dérive d'une opération racine stable, et sa rétention couvre toute fenêtre de rejeu.
- **Règle** :
  - EXIG-ORC-22 : « Chaque outil P2 ou P3 DOIT déclarer au catalogue un argument de clé d'idempotence et son mode : (a) natif, vérifié par le système d'enregistrement; (b) par adaptateur, avec un registre de clés durable, mis à jour dans la même transaction que l'effet ou complété par une requête d'état qui constate l'effet. Un outil sans (a) ni (b) est classé P3, n'est jamais réessayé automatiquement, et une issue inconnue y déclenche une réconciliation humaine. »
  - EXIG-ORC-21 : « La clé dérive d'un identifiant d'opération racine stable de bout en bout : l'identifiant de tâche de l'appelant d'origine et l'identifiant d'étape, propagés dans le message de délégation A2A (EXIG-ORC-23) et, pour un événement, le couple (source, id). L'identifiant d'étape distingue les itérations (index). La construction est la canonisation JCS d'un objet, et non une concaténation. »
  - « La rétention d'une clé DOIT couvrir la durée de vie maximale de la tâche durable, plus la fenêtre de reprise et le délai de réconciliation. Une reprise depuis un point de contrôle plus ancien que la rétention des clés est interdite (EXIG-ARC-06). »
  - EXIG-ORC-27 : « Les réessais sont bornés (nombre maximal déclaré, `maximumAttempts` pour les activités Temporal à effet), avec gigue, dans une seule couche, et comptent dans l'enveloppe. »
  - EXIG-ORC-12 et EXIG-AUT-17 : « un effet de bord non idempotent ne précède jamais un point de pause ni ne se trouve dans une étape réessayable ».
  - La fiche B donne une clé à l'outil P3 de l'exemple.
  - La spécification A2A ne rend pas la déduplication par `messageId` obligatoire (lit. 17) : l'exigence est présentée comme un choix du cadre.
- **Touche** : décision 1; § 5.2 (EXIG-ARC-06, 14; Temporal et Step Functions, lit. 70-71); § 6.5 (Tasks); § 6.6; § 6.7 (EXIG-EVT-08); § 7.4 à 7.7 (EXIG-ORC-11, 12, 21, 22, 23, 27); EXIG-AUT-17; annexe B; C.1; C.2.
- **Résout** : 1.04, 1.05, 2.06, 3.12, 3.13, 3.14, 3.15, 3.17, 3.19, 3.42, 6.07.

**A-10 — Jeton d'approbation : une opération, plusieurs présentations.**
- **Décision** : l'« usage unique » vise une opération, et non une requête.
- **Règle** (EXIG-AUT-12) :
  - « Le jeton couvre une seule opération, identifiée par h, qui inclut la clé d'idempotence. La passerelle le conserve et ne le remet ni à l'agent ni à son modèle (A-15). Jusqu'à son expiration, elle relaie toute présentation de la même opération (même appelant authentifié, même tâche, même h), et le système visé déduplique par la clé (A-09). »
  - « Toute présentation avec une autre empreinte est refusée comme rejeu (EXIG-SEC-25). »
  - « Un passage soldé par `input_required` ou par un refus ne consomme pas le jeton. »
  - « Après l'expiration, si l'issue est inconnue, la passerelle interroge le système visé par la clé. Si l'effet est attesté, aucune nouvelle approbation n'est demandée. Sinon, une nouvelle approbation est requise. »
  - « Le registre des jti est partagé par toutes les instances, atomique et fermé en cas d'indisponibilité (EXIG-IAM-22). »
  - La même sémantique s'applique au `requestState` de l'EXIG-MCP-17 : une relance portant le même `requestState` renvoie le résultat mémorisé.
  - Figure 16 : à l'étape 5, le jeton est remis à la passerelle; à l'étape 6, l'agent rejoue l'appel avec la même clé et la référence de la demande, une donnée non secrète.
- **Touche** : § 5.6, étape 8; § 6.5 (EXIG-MCP-17); § 6.6 (figure 9); § 7.6; § 8.5 (EXIG-AUT-12, figure 16); § 9.4 (figure 18); § 9.9 (EXIG-SEC-25); § 10.3; C.6; C.8; annexe A.
- **Résout** : 1.58, 2.05, 3.04, 3.41, 4.14 (volet réessai), 6.10.

**A-11 — Empreinte, canonisation et liaison de l'approbation.**
- **Décision** : h lie l'appelant, la définition et les octets transmis, et l'écran se dérive de ce que h couvre.
- **Règle** (EXIG-AUT-12 et EXIG-AUT-19) :
  - « h = SHA-256 de la canonisation RFC 8785 de l'objet {outil, version, definition_digest, agent_id, task_id, arguments}. »
  - « La passerelle DOIT rejeter tout argument non conforme à I-JSON (RFC 7493 : clés dupliquées, nombres hors de la plage exacte d'un double, chaînes invalides) et transmettre au serveur exactement la forme canonique hachée. »
  - « Dans les schémas des outils P2 et P3, les montants et les identifiants sont des chaînes ou des entiers en unités mineures. »
  - « La passerelle vérifie que `agent_id` et `task_id` concordent avec l'appelant authentifié. »
  - « L'écran d'approbation et `authorization_details` sont produits par la passerelle à partir des arguments canonisés, jamais fournis par l'agent. »
  - « L'édition d'une action par l'approbateur est une nouvelle action : la passerelle recalcule le contrôle de l'EXIG-AUT-10 et h avant d'émettre le jeton. »
  - « Un outil P3 qui agit sur une ressource modifiable DEVRAIT accepter une précondition de version (version ou ETag de la ressource) incluse dans les arguments hachés. À défaut, la fiche déclare le risque résiduel de modification entre l'approbation et l'exécution. »
  - Dire que l'emploi d'`authorization_details` dans un jeton d'approbation est un profil du cadre, non prévu par la RFC 9396 (lit. 32).
  - L'empreinte des arguments à faible entropie, dans l'audit, est salée ou soumise à un HMAC sous une clé de l'audit.
  - Le C.8 et le Pourquoi de l'EXIG-OBS-12 sont reformulés : h « atteste que les octets transmis sont ceux qui ont été approuvés », et non que l'effet est celui qui était attendu.
- **Touche** : § 8.5-8.6 (EXIG-AUT-12, 19, figure 16); § 6.8; § 10.3 (EXIG-OBS-12); C.1; C.6; C.8; glossaire (« Empreinte »); annexe A (tests négatifs : clé dupliquée, grand entier, appelant différent).
- **Résout** : 3.03, 3.22, 3.23, 3.37, 4.92, 6.11.

**A-12 — Approbateurs, double approbation et hors bande.**
- **Décision** : le hors bande est obligatoire pour tout P3. La confirmation du mandant est admise et tracée. La double approbation porte deux jetons.
- **Règle** :
  - EXIG-AUT-09 (DOIT) : « Toute approbation d'un appel P3 est hors bande : sur un appareil et dans une session distincts de ceux de l'agent, avec une authentification forte résistante à l'hameçonnage. » CIBA reste le moyen recommandé (EXIG-AUT-14, DEVRAIT). Le terme est défini au glossaire.
  - EXIG-AUT-15 : « L'approbation peut être donnée par le mandant lui-même (confirmation), sauf pour un appel P3 d'un agent de classe élevée, qui exige deux approbateurs distincts dont au moins un n'est pas le mandant. Les exigences d'inscription et de formation visent les approbateurs autres que le mandant. Le rôle de chaque approbateur (mandant ou tiers) est consigné. »
  - « La double approbation se fait par deux jetons sur le même h. La passerelle vérifie les deux avant le relais, et l'audit porte une liste `approbations`. »
  - EXIG-AUT-20 : la fréquence par approbateur est plafonnée et la capacité d'approbation est dimensionnée à la conception, avec la charge que crée l'EXIG-SEC-06. Au dépassement, les actions sont mises en file, jamais approuvées par défaut.
- **Touche** : § 8.1 (tableau 28, figure 14); § 8.3 (tableau 31); § 8.5-8.7 (EXIG-AUT-09, 14, 15, 19, 20); § 12.1 (tableau 46); EXIG-GOV-03; C.6; C.8; annexe B; glossaire.
- **Résout** : 3.24, 3.31, 3.33, 3.36, 3.70, 3.72, 4.21, 6.13, 6.14.

**A-13 — Seuils.**
- **Décision** : un seuil se mesure sur une grandeur que l'agent ne choisit pas, sur une portée et une fenêtre déclarées.
- **Règle** (nouvelle EXIG-AUT-24) : « Chaque seuil inscrit au catalogue DOIT déclarer :
  - (a) une grandeur dérivée de l'effet, calculée par la passerelle à partir des arguments canonisés (somme des lignes, par exemple) ou fournie par le système visé, jamais un argument redondant déclaré par l'agent;
  - (b) son unité;
  - (c) sa portée (appel, tâche, agent, mandant ou contrepartie);
  - (d) sa fenêtre.

  La passerelle tient les compteurs dans un magasin à cohérence forte, et un compteur illisible impose le refus. La valeur du seuil est fixée au catalogue seulement; la fiche ne peut fixer qu'une valeur plus stricte. Tant que le comité n'a pas approuvé les seuils d'étalonnage de l'EXIG-AUT-07, l'outil est traité comme s'il les dépassait. »
- C.1, C.2 et la fiche B sont corrigées : `montant_total_cad` est retiré ou devient une grandeur calculée, et un seuil par tâche est exprimé. C.6 affiche la grandeur calculée.
- Les contraintes par argument (bénéficiaires admis, plages) sont admises au catalogue, plus fines que le palier (Progent, 3.1, travail 8).
- **Touche** : § 6.8; § 8.2-8.4 (EXIG-AUT-07, 10); § 10.6; annexes A et B; C.1; C.2; C.6; C.7.
- **Résout** : 3.27, 3.30, 6.01, 6.03, 6.06.

**A-14 — Contrôle calculé et sens de « le plus strict ».**
- **Décision** : une seule référence, l'EXIG-AUT-10, définie comme l'union des contrôles requis.
- **Règle** (EXIG-AUT-10) :
  - « Le contrôle d'un appel est l'union des contrôles exigés par la cellule classe × palier de la figure 15, par le niveau d'autonomie le plus contraignant de la chaîne de délégation (A-16), par les déclencheurs d'approbation (seuil de l'EXIG-AUT-24, cumul de l'A-17) et par les non-dérogeables. »
  - « Entre exigences d'approbation, l'ordre est : refus > approbation hors bande à deux approbateurs > approbation hors bande > approbation > exécution automatique avec revue a posteriori > exécution automatique. Le plus strict est le plus élevé dans cet ordre. »
  - Toute exigence qui renvoie à la « figure 15 » pour dire ce qui exige une approbation renvoie au « contrôle calculé selon l'EXIG-AUT-10 » : EXIG-AUT-12, 15 et 20, ATTENTION de la p. 114, légende de la figure 16, EXIG-GOV-04.
- **Touche** : § 8.2-8.7; EXIG-GOV-04; annexes A et C.
- **Résout** : 3.25, 3.35, 3.60, 3.61, 3.62, 4.61.

**A-15 — Circulation des jetons.**
- **Décision** : les jetons ne passent jamais par le contexte d'un modèle.
- **Règle** :
  - EXIG-IAM-06 : « Jetons délégués et jetons d'approbation circulent dans les en-têtes d'authentification du transport. Ils sont injectés et retirés par le code d'exécution ou par la passerelle, et ne figurent jamais dans le contexte du modèle, dans un message logique, dans un point de contrôle, dans le journal de compensation ni dans une trace. »
  - Le jeton d'approbation est conservé par la passerelle (A-10). Le message de délégation de l'EXIG-ORC-23 porte une référence de délégation, non le jeton, et l'exemple de la p. 98 est corrigé.
  - Fondement : le WIMSE AIMS interdit au modèle l'accès aux justificatifs (lit. 62).
- **Touche** : § 7.4 (EXIG-ORC-13); § 7.5 (EXIG-ORC-16); § 7.7 (EXIG-ORC-23 et exemple); § 8.5 (figure 16); § 9.2 (EXIG-IAM-06); § 9.3; § 10.1-10.2; C.5; C.6.
- **Résout** : 3.18, 1.58 (volet reprise).

**A-16 — Délégation.**
- **Décision** : la profondeur et la portée se vérifient au serveur d'autorisation, les données au serveur de ressources. La passerelle refait l'échange sans devenir un acteur, et le contexte de délégation transporte le niveau et la classe les plus contraignants.
- **Règle** :
  - EXIG-ORC-04 : « Le serveur d'autorisation DOIT vérifier la profondeur à chaque échange de jetons et refuser l'échange qui l'excède. La passerelle ne fonde aucune décision sur les acteurs imbriqués (RFC 8693, § 4.1). Toute délégation entre agents, même sans mandant humain, passe par un échange dont le sujet est le mandant d'origine, ou l'agent initiateur s'il n'y a pas de mandant. Un transfert remplace l'acteur courant sans ajouter de niveau. »
  - PRIN-03 et EXIG-IAM-10 : « droits effectifs = droits du mandant ∩ portée de l'agent au registre ∩ portée nécessaire à la tâche ». Le serveur d'autorisation borne les portées. Le serveur de ressources applique, à chaque appel, les droits du `sub` sur les données. « Le mandant d'une chaîne est toujours l'entité d'origine; un agent intermédiaire n'apparaît que comme `act`. »
  - La portée de la tâche est représentée dans le jeton par `authorization_details`, ou par une portée paramétrée inscrite au catalogue. À défaut, l'exemple d'Alice (p. 124) est reformulé.
  - EXIG-IAM-08 : « l'expiration d'un jeton échangé ne dépasse jamais celle du `subject_token`; aucun échange ne prolonge une délégation ». Changer d'audience sans élargir la portée est permis. Une demande incrémentale est approuvée par le mandant et journalisée.
  - Chaîne à travers la passerelle (EXIG-IAM-11, 14, C.5) : jeton 1, de l'agent à la passerelle (`aud` = passerelle, `cnf` = agent); jeton 2, de la passerelle au serveur (`aud` = serveur, `cnf` = passerelle, `client_id` = passerelle, `act` = agent, acteurs antérieurs imbriqués). La passerelle vérifie le `cnf` du jeton 1 et le serveur n'accepte que la passerelle, par mTLS. L'échange refait par la passerelle n'ajoute pas de niveau de profondeur.
  - « Le niveau d'autonomie et la classe les plus contraignants de la chaîne voyagent dans le contexte de délégation et s'imposent à l'exécutant (A-14). »
  - Agent ambiant (EXIG-AUT-18 et EXIG-IAM-15) : le mandat de longue durée est un consentement inscrit au serveur d'autorisation. Celui-ci émet, à la demande de l'agent, des jetons d'au plus 15 minutes (`sub` = mandant, `act` = agent), tant que le mandat est valide et que le mandant est actif.
  - Les « jetons délégués » de plusieurs heures et les mandats de 12 mois portent des noms distincts au glossaire.
  - L'EXIG-IAM-11 admet la variante de fournisseur que l'EXIG-IAM-08 admet déjà.
  - Les capacités atténuables (macarons) sont mentionnées comme option évaluée et écartée, avec le motif : révocation, audience, audit centralisé (3.1, travail 10).
- **Touche** : PRIN-03; § 5.6; § 6.5 (figure 7); § 7.2 (EXIG-ORC-04); § 7.7 (EXIG-ORC-23); § 8.4 (EXIG-AUT-10); § 8.6 (EXIG-AUT-18); § 9.3 (EXIG-IAM-08 à 16, figure 17, tableau 35); § 13.3 (EXIG-APP-08); C.5; glossaire.
- **Résout** : 1.57, 2.04, 2.07, 2.33, 3.74, 4.03 à 4.10, 4.52 à 4.55, 5.99, 6.04, 6.17, 6.64, 6.69.

**A-17 — Session, propagation du marquage et règle de deux à l'échelle du système.**
- **Décision** : la contamination et la sensibilité sont des étiquettes de flux, tenues par tâche racine et propagées avec la donnée. Le retrait par session est maintenu.
- **Règle** :
  - Glossaire et § 3.1 : « Session (au sens des EXIG-SEC-04 et SEC-06) : la tâche racine et tout ce qui en dérive (sous-tâches, délégations A2A, reprises depuis un point de contrôle, événements publiés au titre de la tâche). Son état (contenu non fiable consommé, données sensibles consultées) est tenu par la passerelle dans un magasin à cohérence forte; un état illisible impose le refus. »
  - EXIG-SEC-03 : « Toute source de contexte (outil, mémoire, index de récupération, déclencheur, téléversement, message ou tâche A2A entrant, événement) DOIT être inscrite au catalogue avec son étiquette de fiabilité; une source non inscrite est non fiable. Le contenu d'une pièce jointe ou d'un document est non fiable, quel que soit son canal, même s'il vient du mandant; seule la demande saisie par le mandant authentifié est fiable. »
  - EXIG-SEC-04 : « La règle de deux s'évalue sur la session composée. Toute donnée produite par une session marquée (artefact, entrée de mémoire, message ou tâche A2A, événement) porte l'étiquette, et la consommer marque la session du consommateur. Une donnée sensible reçue d'un pair confère [B]. La fiche déclare les propriétés de l'agent, et la passerelle applique la règle à l'exécution. »
  - « Un contexte vierge exclut tout rechargement de mémoire, de point de contrôle ou d'artefact étiqueté postérieur à la contamination. »
  - EXIG-SEC-06 : « Est un outil d'envoi tout outil dont un argument peut atteindre une destination hors du périmètre de confiance, y compris la requête en texte libre d'un outil de recherche publique P0 ». Le retrait vise ces outils, les outils P3 et toute destination absente de la liste d'autorisation.
  - [B] reprend la formulation de Meta (« systèmes sensibles ou données privées », lit. 55).
  - Le déclencheur de cumul de l'EXIG-AUT-10 renvoie à l'EXIG-SEC-04.
  - Le contrôle de flux d'information (FIDES) est cité comme fondement, et le masquage sélectif comme option pour réduire les refus (3.1, travail 7).
- **Touche** : PRIN-07; décision 6; § 3.1; § 5.5 (EXIG-ARC-23); § 6.6; § 6.7; § 7.7 (EXIG-ORC-24, 25); § 8.4 (EXIG-AUT-10); tableau 31 (P0); § 9.6 (EXIG-SEC-03 à 07, figure 19); § 9.9 (EXIG-SEC-25); glossaire.
- **Résout** : 1.08, 1.54, 3.26, 3.34, 4.01, 4.17, 4.18, 4.19, 4.20, 4.69, 4.72, 6.16, 6.63.

**A-18 — Régimes du contenu : télémétrie, débogage, décision, évaluation, incident.**
- **Décision** : six magasins distincts, chacun avec sa finalité, ses droits et sa rétention. Le contenu reste interdit dans la télémétrie.
- **Règle** :
  1. **Télémétrie** (EXIG-OBS-07) : jamais de contenu. L'interdit s'étend aux messages d'exception, aux descriptions de statut, aux noms de spans et au bagage.
  2. **Audit** (EXIG-OBS-11 à 13) : empreintes, références et métadonnées (A-19).
  3. **Captures de débogage** (EXIG-OBS-08) : sur décision, 14 jours au plus, sauf gel (point 6).
  4. **Dossier de décision** (nouvelle EXIG-OBS-14) : « Pour toute décision visée par l'art. 12.1 de la Loi sur le privé ou l'art. 65.2 de la Loi sur l'accès, l'agent DOIT verser à un dossier chiffré, sous le contrôle du responsable de la protection des renseignements personnels, les RP en entrée, les versions de l'agent, du modèle et des outils, les facteurs retenus et les approbations. Le dossier est relié à l'audit par empreinte et conservé au moins un an après la décision (art. 11), puis détruit sauf gel. »
  5. **Dépôt d'évaluation** (nouvelle EXIG-EVA-07) : « échantillon caviardé de traces et de contenus, finalité déclarée à l'EFVP, rétention bornée, accès réservé à l'équipe d'évaluation; c'est la seule source des scénarios ajoutés au titre de l'EXIG-EVA-02 et du contenu évalué au titre de l'EXIG-EVA-04 ».
  6. **Dossier d'incident** (EXIG-CON-23) : ouvert au gel. Il suspend les destructions, et le gel comprend les bacs à sable en cours (non détruits), le contexte et les captures de débogage. La contention précède la cause, mais le gel des preuves volatiles précède la destruction (figure 26).
- L'EXIG-CON-18 devient un index de preuves, étiqueté par identifiant d'exigence, chaque preuve restant dans son magasin d'origine. L'EXIG-CON-25 remplit l'avis d'incident à partir de l'audit et du dossier d'incident, non « de la télémétrie ».
- L'EXIG-ORC-16 ne garde au journal de compensation que les références et les arguments chiffrés nécessaires à la compensation.
- L'EXIG-APP-14 (destruction en fin de contrat) réserve les preuves sous gel et les dossiers de décision non échus (EXIG-APP-09, 12).
- La lecture de l'art. 11 (conservation d'au moins un an) est celle du cadre. Le texte consolidé n'a pas pu être relu (`audit_lit`, section 4) et doit l'être.
- **Touche** : tableau 10; § 7.5 (EXIG-ORC-16); § 8.8 (EXIG-AUT-22); § 10.2-10.4 (EXIG-OBS-07, 08, EXIG-EVA-02, 04); § 12.2 (EXIG-CON-09, 10); § 12.6 (EXIG-CON-18); § 12.8 (EXIG-CON-23, 25, figure 26); § 13.3 (EXIG-APP-09, 12, 14); annexe B; tableau 58.
- **Résout** : 1.88, 3.20, 4.37, 4.41, 4.88, 5.01, 5.25, 5.30, 5.37.

**A-19 — Journal d'audit.**
- **Décision** : intention avant l'effet, chaînage par flux défini, ancrage hors du domaine d'administration de l'audit.
- **Règle** :
  - EXIG-OBS-11 : « Avant de relayer un appel P2 ou P3, la passerelle DOIT écrire un enregistrement d'intention chaîné; l'enregistrement d'issue suit. Le service d'audit fait partie des dépendances de l'EXIG-AUT-11 : s'il est indisponible, P2 et P3 sont refusés. »
  - EXIG-OBS-12 : « Un flux est la séquence numérotée d'une instance d'écriture, inscrite à un registre des flux. Au moins toutes les heures, un point de contrôle signé et daté de la tête de chaque flux (numéro de séquence, empreinte) DOIT être publié hors du domaine d'administration du service d'audit (témoin ou registre de transparence, modèle de la RFC 9162, ou stockage WORM sous une autre administration). La cohérence est vérifiée par une fonction indépendante. »
  - Pourquoi de l'EXIG-OBS-12 : « le chaînage détecte la modification ou la suppression interne; la troncature et la réécriture ne se détectent que par les points de contrôle externes ».
  - EXIG-OBS-13 : « purge par segments clos par un point de reprise signé; anonymisation par destruction de la table des pseudonymes; les clés de vérification sont conservées toute la durée de rétention ».
  - Décision 8 : « journal d'audit chaîné et ancré », et non « inaltérable ».
  - L'extrait du § 10.3 est aligné sur C.8.
  - Fondements : Schneier et Kelsey 1999, Crosby et Wallach 2009, RFC 9162 (3.1, travaux 1 à 3).
- **Touche** : décision 8; figure 1; tableau 6; § 9.4 (figure 18); § 10.3 (EXIG-OBS-11 à 13); C.8; glossaire (« Passerelle d'agents »); EXIG-CON-10; H.5 (IR 8547).
- **Résout** : 1.96, 4.14 (volet audit), 4.39, 4.91, 6.09, 6.12.

**A-20 — A2A et « agent comme outil ».**
- **Décision** : A2A est obligatoire hors du même processus. L'enveloppe n'est permise qu'entre sous-agents d'un même orchestrateur.
- **Règle** :
  - EXIG-A2A-01 et EXIG-INT-04 : « Toute délégation à un agent d'un autre domaine, d'un autre cadriciel, d'un tiers ou d'un autre processus DOIT utiliser A2A (sauf coexistence bornée de l'EXIG-A2A-15). »
  - EXIG-INT-05 devient un renvoi : « L'enveloppe "agent comme outil" n'est permise qu'entre sous-agents d'un même orchestrateur, dans un même processus. »
  - Critère, au § 3.1, au § 6.2 et au glossaire : « une cible est un agent si elle choisit elle-même, au moyen d'un modèle, les actions qu'elle exécute; sinon c'est un outil, même si elle conserve l'état d'une tâche ou demande une précision (Tasks, élicitation MCP) ».
- **Touche** : § 3.1; § 6.2 (EXIG-INT-04, 05); § 6.6 (EXIG-A2A-01); § 7.2; annexe D; glossaire (« Outil »).
- **Résout** : 1.21, 1.22, 6.02, 6.75.

**A-21 — États du catalogue et des versions.**
- **Décision** : une machine d'états unique pour les standards, les versions de contrat et les agents. Un état « Suspendu » est ajouté.
- **Règle** :
  - EXIG-INT-06 : « Tout nouvel usage en production exige le statut Adopter. Un usage existant au statut Contenir reste permis derrière un adaptateur jusqu'à l'échéance de son plan de sortie. Le statut Évaluer limite l'usage aux pilotes (EXIG-GOV-20). Le statut Surveiller exclut tout usage. Le statut Suspendu, prononcé pour un motif de sécurité, fait cesser immédiatement le service par la passerelle. »
  - EXIG-GOV-20 est alignée sur cette règle.
  - EXIG-INT-18 : « … jamais avant la fin de la coexistence, sauf suspension de sécurité (EXIG-INT-14, EXIG-GOV-14) ».
  - La granularité de la suspension est l'outil, ou toute la version du composant si l'empreinte du serveur change (EXIG-MCP-20, EXIG-SEC-18).
  - Tableau 15, ligne MCP : la révision 2025-11-25 est au statut Contenir jusqu'au 28 juillet 2027, ce qui accorde l'EXIG-INT-07 et l'EXIG-MCP-22.
  - « Flux SSE structuré produit par l'orchestrateur » est inscrit comme patron interne au statut Adopter.
  - La coexistence des versions majeures est servie par la passerelle sous des noms d'outils suffixés par la version majeure. Les mineures sont servies pendant une fenêtre de migration en lot.
  - Les tiers relèvent d'un régime propre : préavis contractuel, sinon suspension assumée (EXIG-INT-14, 16 et 19).
- **Touche** : § 6.3 (tableau 15, statuts); EXIG-INT-06, 07, 14 à 19; EXIG-MCP-20, 22; § 9.8 (EXIG-SEC-18); § 11.4-11.5 (EXIG-GOV-14); § 11.7 (EXIG-GOV-20); ch. 13 (clauses).
- **Résout** : 1.20, 1.23, 2.03, 2.13, 2.29, 2.30, 4.80, 5.03.

**A-22 — Révision des standards et suites de conformité.**
- **Décision** : l'EXIG-GOV-18 est le seul déclencheur de révision extraordinaire pour un standard au statut Adopter.
- **Règle** :
  - EXIG-GOV-18 : « une révision extraordinaire est déclenchée par la publication d'une version incompatible ou d'une dépréciation, ou par un correctif de sécurité (DOIT) ». Une annonce de date relève de la révision trimestrielle.
  - L'EXIG-INT-23 est limitée aux statuts Évaluer et Surveiller, et « révision de MCP » sort de ses signaux.
  - Le tableau 72, no 3, n'inscrit pas le signal comme « survenu ».
  - L'EXIG-GOV-19 et l'EXIG-INT-09 reçoivent les stades Experimental, Beta et Stable, appliqués extension par extension, avec une réserve inscrite pour Beta.
  - Une suite de tests bloquante est épinglée à une étiquette. Tant qu'elle est alpha (a2a-tck), ses résultats sont consignés et bloquants seulement sur les tests qui ont été stables pendant deux versions. La suite MCP reçoit le même régime, d'où la symétrie.
  - L'EXIG-GOV-18 désigne l'architecture d'entreprise comme rédactrice et le comité comme approbateur, et le § 6.3 est aligné.
  - Le retrait accéléré de MCP est décrit partout comme « pour un risque de sécurité actif (avis publié ou exploitation documentée), au moins 90 jours » (lit. 4).
- **Touche** : § 2.2; § 6.3; § 6.5; § 6.8 (EXIG-INT-19); § 6.9 (EXIG-INT-23); EXIG-INT-09; § 11.7 (EXIG-GOV-18, 19); ch. 13; annexe H.
- **Résout** : 2.25, 5.14, 5.15, 5.61, 5.62, 6.27, 6.28, 6.29.

**A-23 — Force normative et méta-règles.**
- **Décision** : une seule révision du § 1.4 et du § 4.3 fixe le périmètre normatif, la préséance et le départage.
- **Règle** :
  - **§ 1.4, périmètre normatif** : « Créent une obligation :
    - (a) les blocs EXIG et les principes PRIN;
    - (b) les règles d'interprétation des sections 1.2 (critère de portée et règle du doute), 1.5, 1.6, 4.2 (devoir de l'architecte) et 4.3;
    - (c) les définitions du tableau 7; pour les niveaux et les paliers, les tableaux 28 et 31 font foi, et le § 3.1 en est un résumé;
    - (d) les tableaux et les structures d'annexe auxquels une exigence renvoie expressément : annexe A par l'EXIG-GOV-11, annexe B (contenu, non forme) par l'EXIG-GOV-07, C.1 et C.2 par l'EXIG-ORC-22 et l'EXIG-MCP-20, C.6 par l'EXIG-AUT-12, C.8 par l'EXIG-OBS-12;
    - (e) le tableau 58, pour les seules phases d'exigibilité de l'EXIG-GOV-21.

    Le reste, y compris l'annexe H, est informatif. »
  - La règle « Source de vérité » de l'annexe B est convertie en exigence (EXIG-GOV-07, alinéa ajouté).
  - **Catalogue** (§ 1.6) : « Le catalogue fait foi pour la version épinglée là où une exigence renvoie à "la version épinglée au catalogue"; la version citée dans le texte en est la valeur initiale. Les échéances datées restent dans le texte. » Les DOIT qui figent une version sont reformulés selon ce modèle.
  - **Rang 1** (§ 1.6 et 4.3) : « le droit applicable; les engagements contractuels en vigueur à l'adoption du cadre, pour une transition bornée et inscrite au registre, sauf sur les points de l'EXIG-GOV-17 ».
  - Nouvelle EXIG-APP-18 : « Un contrat conclu ou renouvelé après l'adoption NE DOIT PAS comporter de clause contraire à un point de l'EXIG-GOV-17. »
  - **Départage** (§ 1.6 et 4.3) : « Ordre : droit applicable; EXIG-GOV-17; DOIT sur DEVRAIT; source unique désignée (A-24) sur renvoi; disposition spéciale sur disposition générale. Si deux contraintes du même rang sont cumulables, toutes deux s'appliquent; sinon, l'action est refusée jusqu'à la décision du comité, qui DOIT statuer dans un délai fixé. »
  - **Version** : application de l'A-31.
- **Touche** : historique; § 1.4, 1.5, 1.6; § 3.1; § 4.2, 4.3; annexes A, B, C et H; EXIG-GOV-07, 11; ch. 13; EXIG-MCP-22; EXIG-A2A-01; EXIG-OBS-01; tableau 15.
- **Résout** : 1.12, 1.13, 1.14, 1.15, 6.05, 6.23 (avec A-31).

**A-24 — Sources uniques.**
- **Décision** : une source normative par obligation, les autres textes deviennent des renvois sans contenu propre.
- **Règle** :
  - **Déclencheurs de réévaluation : EXIG-GOV-12**, liste enrichie : modèle servi (y compris derrière un alias, `gen_ai.response.model`), invite système, outils et versions majeures de contrat, version de protocole, palier, propriétés [A], [B] et [C], mémoire, corpus de récupération, juge, ODD, population, données, fournisseur et lieu de traitement, taxonomies de menaces (rythme semestriel pour ATLAS). La réévaluation précède toujours la mise en service. L'exception « si le changement ne peut attendre » est remplacée par : « l'ancienne version reste en service; à défaut, l'agent est suspendu ». Elle ne permet jamais de fonctionner au-dessus du plafond de classe. Renvoient à l'EXIG-GOV-12 : l'EXIG-AUT-05, l'EXIG-ARC-09, l'EXIG-EVA-01, l'EXIG-SEC-01, -02 et -24, l'EXIG-CON-03 (qui garde le lien avec la « modification importante » d'E-23), l'annexe B, `renew_on` et les figures 22 et 25.
  - **Art. 12.1 et 65.2** : l'EXIG-CON-07 porte les obligations envers la personne. L'EXIG-CON-08 porte le test de révision humaine significative, repris de l'EXIG-AUT-23 : autorité, compétence, accès à toutes les données pertinentes, temps. La qualification se fait a priori, à l'EFVP et à la fiche, avec un défaut prudent (« exclusivement automatisée »). La mesure de l'EXIG-AUT-21 sert de contrôle a posteriori, qui requalifie en cas d'échec. L'EXIG-AUT-22 et l'EXIG-AUT-23 deviennent des renvois. L'EXIG-CON-21 (transparence générale) renvoie à l'EXIG-CON-07 pour le cas de l'art. 12.1. « Importance relative » devient « principaux facteurs et paramètres » (texte de la loi, lit. 25), et elle est établie à partir des facteurs déterministes du processus, jamais du raisonnement affiché du modèle.
  - **Non-dérogeables : EXIG-GOV-17**, liste enrichie de la triade létale (EXIG-SEC-06), de l'existence du journal d'audit (EXIG-OBS-11) et de l'approbation hors bande des P3 (A-12). La grille A en est la projection, point par point. Tout point de grille qui reprend une obligation légale est marqué « bloquant, non dérogeable ». Les ajouts propres à la grille (audience unique, absence de relais) sont versés à l'EXIG-GOV-17 ou retirés.
  - **Cibles de révocation** : EXIG-IAM-20, avec le tableau 61 pour les valeurs (A-05).
  - **Minimums de conservation** : une table unique dans l'EXIG-CON-10. Pour chaque magasin de l'A-18, la durée minimale et sa source; la plus longue l'emporte. Elle tranche entre 6 et 24 mois.
  - **Plafonds** : l'EXIG-CON-02 seule. Le § 8.1 et l'EXIG-GOV-17 y renvoient.
  - **Tableau 50** : il reçoit une colonne E-23 (décision 10). L'EXIG-CON-18 étiquette les preuves par identifiant d'exigence, et le tableau 50 relie ces identifiants aux référentiels.
- **Touche** : § 5.2; § 8.2, 8.8; § 9.5, 9.9; § 10.4; § 11.5-11.6; § 12.1-12.6; annexes A et B.
- **Résout** : 1.10, 3.39, 3.40, 3.64, 3.75, 4.42, 4.99 (f), 5.08, 5.13, 5.17, 5.26, 5.42 (avec A-26), 5.68, 5.73, 6.08.

**A-25 — Classification et entrée en pilote.**
- **Décision** : la classe s'établit une fois, avant l'inscription, sur l'autonomie maximale envisagée. Un pilote sur données réelles est une mise en production.
- **Règle** :
  - EXIG-CON-01 : « La classe est attribuée par la fonction risques et conformité avant l'inscription au registre (état "proposé" avec classe approuvée). Elle est évaluée sur l'autonomie maximale envisagée et sur le parcours de décision déclaré (A-24), avant tout plafonnement. Le niveau demandé au-delà du plafond de l'EXIG-CON-02 est refusé. » Le § 11.5, étapes 1 et 2, et A.2 sont alignés. Le report 8 de la Note AMF est traité ainsi.
  - § 11.5 et EXIG-GOV-08 : « L'entrée en pilote avec des justificatifs de production ou des données réelles est une mise en production. Elle exige la classification définitive, l'EFVP, l'équipe rouge (classes modérée et élevée, EXIG-SEC-23) et une homologation provisoire bornée au niveau du pilote. L'homologation de l'étape 4 confirme pour la production complète. »
- **Touche** : § 1.4 (définition de la mise en production); § 11.4-11.5; EXIG-AUT-05; EXIG-SEC-23; EXIG-CON-01, 02, 13, 26; annexe A (A.2); tableau 52; H.3.
- **Résout** : 5.05, 5.07, 5.16, 6.31.

**A-26 — Régime transitoire et exigibilité.**
- **Décision** : la feuille de route reste un ordre de planification. L'exigibilité se règle agent par agent, selon les capacités qu'il exerce, et non selon le calendrier.
- **Règle** (nouvelle EXIG-GOV-21) : « (a) Aucun agent NE DOIT exercer un palier, un niveau ou une topologie avant que les contrôles qui les conditionnent soient en service et homologués. En particulier :
  - aucun P2 sans compensation déclarée et canal de compensation (A-06);
  - aucun P3 tant que la passerelle ne vérifie pas le jeton d'approbation (A-10, A-11);
  - aucun appel interdomaines hors de la passerelle.

  (b) Chaque point de la grille A porte sa condition d'exigibilité (tout agent, P2 et plus, P3, N3 et plus, interdomaine, multiagent). Les obligations légales et les points de l'EXIG-GOV-17 sont exigibles immédiatement.

  (c) Un agent en exploitation à l'adoption reçoit le statut "existant inventorié", sous une mesure transitoire de cohorte : une décision du comité vise une liste d'agents, avec une échéance liée à un jalon. Cette mesure permet l'émission de justificatifs sur la base d'une fiche minimale (champs de l'étape Proposition), n'admet aucun point de l'EXIG-GOV-17, et limite les appels qui contournent encore la passerelle au palier P0-P1, par des justificatifs en lecture seule chez le système cible.

  (d) Une échéance externe (loi, autorité) ne bouge pas. Une échéance du cadre (migration MCP au 28 juillet 2027, EXIG-MCP-22) ne change que par une révision (§ 1.6). »
- Le tableau 58 et la figure 28 ouvrent la passerelle aux paliers P0, P1, P2, puis P3 avec approbation signée avant tout N2 qui exécute des P3. Les sagas et la compensation sont livrées avec le premier P2.
- La règle de progression « plafonnées à N2 » est remplacée par le point (c).
- L'EXIG-CON-12 et le tableau 58 deviennent : « inventaire E-23 des modèles avec cote de risque et état de validation au 1er mai 2027 ». E-23 ne fixe aucune échéance de validation des modèles existants (lit. 23).
- J2a et l'annexe III du RIA restent sous réserve de la relecture du règlement (UE) 2026/1744 au JO (lit. 22).
- La dérogation au plafond de phase ne permet jamais de dépasser le plafond de classe (A-24).
- Les indicateurs du tableau 61 qui exigent une déclaration humaine sont marqués comme tels, et la valeur de référence est mesurée au premier trimestre suivant J1.
- **Touche** : sommaire (p. 8-9); historique; § 1.4; ch. 14 (p. 199); ch. 15 (figure 28, tableaux 58 à 61, règles de progression, ATTENTION); annexe A (colonne d'exigibilité); annexe B; EXIG-GOV-15 à 17; EXIG-CON-12; EXIG-MCP-22.
- **Résout** : 1.03, 1.91, 5.40, 5.41, 5.42, 5.43, 5.44, 5.45, 5.46 (en partie), 5.108.

**A-27 — Échelles.**
- **Décision** : N0 n'est pas un niveau d'agent. P2 et P3 sont disjoints par l'effet. N4 se distingue de N3 par l'origine de la tâche.
- **Règle** :
  - § 3.1 et tableau 28 : « N0 : aucun choix d'action laissé à un modèle; le code fixe chaque pas, et un modèle peut transformer une donnée sans choisir l'action. N0 qualifie un flux, non un agent. »
  - § 3.2 : « un flux assisté par IA est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle (sans approbation : N3 et ODD) ».
  - EXIG-AUT-08 : « un effet irréversible ou externe est P3, même si une compensation est déclarée; P2 suppose une écriture réversible, ou compensable vers un état métier équivalent avec un impact borné ». Le § 3.1 est aligné sur le tableau 31.
  - Tableau 28 et § 3.3 : « N4 : tâches déclenchées sans demande d'une personne (événement, horaire), dans un ODD certifié. La passerelle lit l'origine de la tâche (attribut posé par l'orchestrateur ou par le courtier) et applique le niveau inscrit au registre; une tâche autodéclenchée d'un agent qui n'est pas N4 est refusée. »
  - Renommage : « étages d'évaluation E1 à E3 » (au lieu de « paliers ») et « jalons du cycle de vie » (au lieu de « points de contrôle »).
- **Touche** : § 1.2; § 3.1-3.3; § 8.1 (tableau 28, figure 14); § 8.3 (tableau 31, EXIG-AUT-08); § 10.4 (EXIG-EVA-01, figure 22); § 11.5 (figure 25); figures 1 et 3; glossaire.
- **Résout** : 1.16, 1.17, 1.18, 1.97, 3.32, 3.63.

**A-28 — Contrôles de données.**
- **Décision** : la passerelle d'agents n'est pas le point d'application des usages secondaires.
- **Règle** :
  - EXIG-CON-05 : « La localisation s'applique sur les trois chemins (passerelle de modèles, passerelle d'agents, plan mémoire et index), par route déclarée au catalogue. »
  - EXIG-CON-06 : « La finalité s'applique aux points de sortie des magasins, par la plateforme de données; la passerelle d'agents la vérifie pour les seuls flux agentiques. »
  - Résidence : « toute zone hors du Québec relève de l'art. 17 », formulé de la même façon à la p. 154 et dans l'EXIG-APP-11.
- **Touche** : § 9.4; § 10.5 (p. 154); § 12.2 (EXIG-CON-05, 06); § 13.3 (EXIG-APP-11).
- **Résout** : 4.99 (j), 5.18, 5.95.

**A-29 — OpenTelemetry.**
- **Décision** : la conformité se mesure à la sortie du collecteur, par rapport à une version de référence, et non à l'émission.
- **Règle** :
  - EXIG-OBS-01 : « Chaque composant émet selon une version des conventions GenAI consignée au catalogue pour ce composant (version émise et réglage d'`OTEL_SEMCONV_STABILITY_OPT_IN`). Une couche de correspondance versionnée du collecteur la ramène à la version de référence épinglée : la ligne v1.41 (v1.41.0, correctif v1.41.1 admis). »
  - EXIG-OBS-05 : « chaque span DOIT porter, à la sortie du collecteur, après correspondance, les attributs du tableau 41 ».
  - Un composant de tiers qui n'émet pas vers le collecteur est couvert par les spans de la passerelle (client) et par une clause contractuelle d'export.
  - Le § 10.1, le tableau 15 et la fiche B sont alignés. La p. 85 parle de « première version étiquetée du dépôt semantic-conventions-genai ».
  - Avant d'admettre la v1.41.1 comme équivalente, vérifier que son écart avec la v1.41.0 ne touche pas `gen_ai.*`. `audit_lit` désigne la v1.41.0 comme dernière version étiquetée vérifiée (lit. 35), alors que le corps cite la v1.41.1.
- **Touche** : tableau 15; § 6.9 (p. 85); § 10.1 (EXIG-OBS-01, 05, tableau 41); annexe B.
- **Résout** : 1.60, 2.94, 4.02, 4.35, 4.99 (d), 6.91.

**A-30 — Décompte et identifiants.**
- **Décision** : 287 est exact pour la version 1.1. La révision 1.2 en compte 296.
- **Règle** :
  - Le corps de la version 1.1 compte 287 exigences (ARC 25, INT 23, MCP 22, A2A 15, EVT 10, ORC 30, AUT 23, IAM 21, SEC 26, OBS 13, EVA 6, FIN 10, GOV 20, CON 26, APP 17).
  - La révision 1.2 ajoute les 9 identifiants du tableau des nouveaux identifiants (2.0.1), soit 296. Le tableau 4, l'annexe D (296 lignes, dans l'ordre du document) et toute mention du total sont mis à jour.
  - H.3, report 7 : « Annexe D (287 lignes dans la version 1.1) ».
  - EXIG-AMF-05 et EXIG-AMF-07 sont des identifiants de la Note AMF IA, et non du cadre. L'annexe H l'écrit en toutes lettres (« EXIG-AMF-05 de la Note AMF IA »). Le tableau 4 ne reçoit aucun préfixe AMF tant que le comité n'a pas statué sur le report 7.
  - Le tableau 4 corrige les rattachements de section (OBS aux § 10.1 et 10.3, EVA au § 10.4, FIN aux § 10.5 et 10.6).
  - Les exigences devenues des renvois (EXIG-AUT-22, AUT-23, INT-05) gardent leur identifiant, qui n'est jamais réattribué.
- **Touche** : § 1.5 (tableau 4); annexe D; H.3; sommaire.
- **Résout** : 1.95, 6.114.

**A-31 — Sources, état des sources et identité documentaire.**
- **Décision** : appliquer le tableau 66 à la lettre, dédoublonner, réépingler, et distinguer les errata (1.1.1) de la révision (1.2).
- **Règle** :
  - Aucune source de catégorie C n'appuie une exigence ni une obligation légale. Les blogues et l'agrégateur FLI sont remplacés par EUR-Lex, le Service Desk de la Commission européenne ou les spécifications. Au plus un « argument d'éditeur » peut être nommé comme tel dans le texte, sans appel d'appui.
  - L'annexe G est dédoublonnée par script, après normalisation du gabarit, puis recomptée. Le total de 473 est corrigé partout.
  - Le tableau 69 reçoit les colonnes « no G » et « décision à l'audit final », et chaque entrée de G reçoit une catégorie.
  - La Méthode et le § 1.7 donnent la population couverte par chaque passe (121, 428, 473) et l'écart expliqué.
  - L'état des sources est formulé partout : « état des sources au 27 octobre 2026; vérifications des 27 et 28 octobre 2026 ».
  - Les brouillons IETF sont réépinglés ou cités sans numéro de révision (section 3.2).
  - **Errata** : appliqués au corps sous le numéro 1.1.1, avec une ligne d'historique. L'annexe H reste informative pour ses constats et ses propositions. Règle de divergence : « un erratum prime à toute date ».
  - Le § 1.5 annonce « huit annexes, de A à H ».
  - L'erratum no 1 vise les § 6.6 et 13.1 : « comité directeur technique de neuf sièges ».
  - L'annexe H corrige son tri H.2 / H.4 : un fait antérieur au 27 octobre est un erratum ou une omission, non une nouveauté. Elle dit qui a vérifié quoi et selon quel régime. L'EN 18286 n'est plus présentée comme donnant présomption de conformité à l'art. 17 du RIA tant que sa citation au JO comme norme harmonisée n'est pas établie.
- **Touche** : page de titre; historique; Méthode; § 1.5, 1.7; annexes F, G et H; appels des p. 17, 19, 33, 48, 76, 87, 91, 93, 105, 112, 129, 150, 182, 187, 190-191, 224.
- **Résout** : 1.11, 1.89, 1.93, 5.88, 6.18, 6.20, 6.21, 6.22, 6.23, 6.24, 6.25, 6.26, 6.30, 6.77, 6.86, 6.90, 6.106, 6.109.

**A-32 — Règles de décision statistiques.**
- **Décision** : toute porte, tout seuil d'évaluation et toute comparaison déclare sa règle de décision.
- **Règle** :
  - Nouvel alinéa de l'EXIG-EVA-03 : « Toute porte (EXIG-SEC-24, EXIG-EVA-03, EXIG-EVA-04, tableau 42) et toute comparaison (EXIG-ORC-02) DOIT déclarer la taille d'échantillon, la statistique, l'intervalle de confiance et la règle de décision. Un taux cible p n'est démontré que si la borne supérieure de l'intervalle à 95 % est inférieure à p, ce qui exige au moins 3/p essais sans échec. »
  - Le jeu de référence n'est plus plafonné à 200 scénarios. Il est stratifié, avec un sous-ensemble réservé et non publié aux équipes (3.1, travail 13).
  - Le seuil d'attaque de l'EXIG-SEC-24 est fixé par la fonction risques et conformité, non par l'équipe qui déploie, et il est mesuré contre des attaques adaptatives (3.1, travaux 4 et 5).
  - L'EXIG-AUT-21 remplace la proportion fixe par une taille d'échantillon minimale par période et par une proportion.
  - L'accord entre évaluateurs de la maturité est mesuré (kappa), et le § 14.2 ne revendique la reproductibilité qu'à ce titre.
- **Touche** : § 7.1-7.3 (EXIG-ORC-02); § 8.7 (EXIG-AUT-21); § 9.9 (EXIG-SEC-23, 24); § 10.4 (EXIG-EVA-02 à 06, tableau 42); § 14.2; tableau 61.
- **Résout** : 2.32, 3.38, 4.33, 4.34, 4.43, 5.38, 5.47 (en partie).

**A-33 — Règle de sortie réseau unique.**
- **Décision** : une seule règle, à l'EXIG-SEC-12, à laquelle renvoient l'EXIG-MCP-12, l'EXIG-MCP-19 et l'EXIG-A2A-12.
- **Règle** : « Toute connexion sortante initiée à partir d'une donnée externe (URL, `jku`, icône, notification push, redirection) DOIT :
  - viser une destination inscrite nommément à la liste d'autorisation;
  - être résolue une fois, puis connectée à l'adresse résolue, qui est vérifiée hors des plages à usage spécial (IANA) avant la connexion;
  - revalider chaque redirection selon la même règle, avec un plafond de redirections;
  - refuser le *domain fronting* (SNI et en-tête `Host` concordants) quand le mandataire termine TLS.

  Une cible interne légitime est atteinte par une entrée de catalogue, jamais par une URL fournie. » La RFC 8725, § 3.10, est citée pour `jku` (lit. 33). Une icône SVG est rendue en image matricielle ou refusée.
- **Touche** : § 6.5 (EXIG-MCP-12, 19); § 6.6 (EXIG-A2A-12); C.3 (p. 219); § 9.7 (EXIG-SEC-12, 14).
- **Résout** : 2.17, 2.18, 4.24, 4.74.

**A-34 — Rôles et indépendance.**
- **Décision** : l'indépendance de la p. 162 devient vérifiable dans la RACI, et les DOIT de l'économie de l'inférence visent un rôle existant.
- **Règle** :
  - Tableau 44 : pour « Évaluer », R = équipe d'évaluation désignée, distincte de l'équipe de construction. Pour « Fixer le niveau d'autonomie » et « Homologuer », A = fonction risques et conformité (classes faible et modérée) ou comité (classe élevée), le parrain restant demandeur.
  - L'EXIG-GOV-03 vise aussi l'évaluation.
  - Le rôle « Équipe FinOps » est ajouté au tableau 43, avec des activités FIN au tableau 44.
  - « Propriétaire » employé seul est proscrit : on écrit « parrain » ou « responsable technique ». Le rôle *manager* d'Entra est mentionné (lit. 76).
- **Touche** : § 10.5-10.6 (EXIG-FIN-03, 04, 10, figure 23); § 11.1-11.2 (tableaux 43 et 44, EXIG-GOV-03); A.2; C.7; glossaire.
- **Résout** : 4.51, 4.97, 4.99 (i), 5.02.

## 3. État de l'art manquant et preuves exigées

### 3.1 Travaux omis

D'après `audit_lit.md`, section 3. L'effet est qualifié selon que le travail invalide, nuance ou précède le choix du cadre.

| # | Référence | Effet | Section touchée et correctif |
|---|---|---|---|
| 1 | Crosby et Wallach (2009), *Efficient Data Structures for Tamper-Evident Logging*, USENIX Security | Invalide « le chaînage rend toute suppression détectable » | EXIG-OBS-12, C.8 : points de contrôle externes et preuves de cohérence (A-19) |
| 2 | RFC 9162, *Certificate Transparency 2.0* (2021) | Nuance et fournit le remède (têtes signées, preuves de cohérence) | EXIG-OBS-12, 13 : modèle des points de contrôle (A-19) |
| 3 | Schneier et Kelsey (1999), *Secure Audit Logs to Support Computer Forensics*, ACM TISSEC | Précède (intégrité prospective, clés qui évoluent) | Ch. 10, audit : fondement et clés de signature par période |
| 4 | Nasr, Carlini et coll. (2025), *The Attacker Moves Second*, arXiv:2510.09023 | Nuance fortement : 12 défenses contournées par attaques adaptatives | § 9.5-9.6 (ATTENTION, p. 136), ch. 10 : mesurer contre des attaques adaptatives (A-32) |
| 5 | Zhan, Fang, Panchal et Kang (2025), *Adaptive Attacks Break Defenses Against IPI*, NAACL Findings | Nuance : 8 défenses contournées | § 9.6 : idem |
| 6 | Greshake et coll. (2023), *Not What You've Signed Up For*, AISec '23 | Précède : article fondateur de l'injection indirecte | PRIN-07, § 9.6 : citer à la définition de la menace |
| 7 | Costa et coll. (2025), *Securing AI Agents with Information-Flow Control* (FIDES), arXiv:2505.23643 | Précède et nuance T4 : étiquettes de confidentialité et d'intégrité, propagation | § 9.6 : fondement de l'A-17 |
| 8 | Shi et coll. (2025), *Progent: Securing AI Agents with Privilege Control*, arXiv:2504.11703v3 | Nuance : une politique par argument est plus fine que le palier | § 8.4, 9.6 : contraintes par argument au catalogue (A-13) |
| 9 | Hardy (1988), *The Confused Deputy*, ACM SIGOPS OSR | Précède | p. 62 et 122 : citer à l'« adjoint confus » |
| 10 | Birgisson et coll. (2014), *Macaroons*, NDSS | Nuance T6 : non-élargissement par construction | § 9.3 : option évaluée et motif du rejet (A-16) |
| 11 | Saltzer, Reed et Clark (1984), *End-to-End Arguments in System Design*, ACM TOCS | Nuance T3 : la déduplication se garantit à l'extrémité | § 7.6 : idempotence vérifiée chez le producteur de l'effet (A-09) |
| 12 | Wang et coll. (2024), *Rethinking the Bounds of LLM Reasoning*, ACL | Précède et appuie « agent unique d'abord » | § 7.3, 7.9 : donnée probante d'EXIG-ORC-02 |
| 13 | Kapoor et coll. (2024), *AI Agents That Matter*, arXiv:2407.01502 | Nuance : front coût-exactitude, jeux réservés, reproductibilité | Ch. 10 : EXIG-EVA et EXIG-FIN (A-32) |
| 14 | draft-klrc-aiagent-auth-00 (IETF, expiré) | Nuance (veille) | § 9.3 : veille, avec statut |
| 15 | draft-rosenberg-oauth-aauth-02 (IETF, 1er nov. 2026) | Nuance (veille) | § 9.3 : veille |
| 16 | draft-mcguinness-oauth-ai-agent-instance-00 (IETF, 4 juil. 2026) | Nuance : un `client_id` pour de nombreuses instances | § 9.2-9.3 : identité par instance, veille |

Les entrées 14 à 16 ont été repérées par recherche dans le datatracker, sans ouverture de la page : leur contenu reste à lire.

### 3.2 Citations inexactes ou obsolètes à corriger

Renvoi à `audit_lit.md`, sections 1 et 2. Les correctifs sont à appliquer sous l'A-31.

- **Inexactes (3)** :
  - p. 20, Loi 25 « pour l'essentiel depuis 2024 » : l'essentiel est en vigueur depuis le 22 septembre 2023, l'ensemble depuis le 22 septembre 2024 (lit. 24);
  - p. 17, retrait accéléré MCP « exceptionnel » : il s'agit d'un « risque de sécurité actif » (lit. 4);
  - p. 34, Step Functions : réserve sur `Retry` pour le mode Standard, et mode Express synchrone « au plus une fois » (lit. 70).
- **Obsolètes (5)** : OAuth 2.1 −16 vers −17, avec expiration du 4 mai 2027 ([176]/[327], p. 52 et 125; lit. 29); WIMSE AIMS −00 vers −01 ([93], [309]; lit. 62); ID-JAG −04 vers −06 ([177]; lit. 67); workload-identity-practices −07 vers −08, en dernier appel IETF jusqu'au 13 novembre 2026 ([323]; lit. 68); spiffe-client-auth −02 vers −03 ([334]; lit. 69).
- **Non vérifiés (6), à trancher avant de geler les échéances qui en dépendent** :
  - règlement (UE) 2026/1744 : date d'adoption du 8 juillet, dates fixes ou conditionnelles, art. 25(4), 111(2) et 113 (lit. 22; trancherait le JO L du 24.7.2026). D'ici là, citer le Service Desk [57] pour les dates d'application (lit. 21);
  - approbation de l'A2A par le conseil de l'AAIF le 4 août 2026 (lit. 41);
  - chiffres du billet Google du 28 janvier 2026 (lit. 53);
  - [87] OWASP *Threats and Mitigations* « version 1.1 », T16 et T17 (lit. 60);
  - ASI10 « immuables et signés » (lit. 61);
  - NIST AI 100-2 E2025, NISTAML.015 (lit. 83).
- **Doublons et attributions** : fusionner [6]/[65], [69]/[70], [287]/[288] (ajouter doi:10.14778/3750601.3750611), [360]/[363] et [176]/[327]. Les doublons supplémentaires relevés en tranche ([6.22], [4.99 l]) sont confirmés par le dédoublonnage scripté de l'A-31. Pour les « 1 000 à 2 000 jetons », citer [149] et non [17] (lit. 49).
- **Précisions** : versions arXiv de CaMeL (v2), MAST (v3) et Kim et coll. (v3) (lit. 46, 48, 52); date de [76] (IMDA v1.5, 20 mai 2026) et de [318] (mise à jour du 20 octobre 2025); A2A au stade « Growth » à l'AAIF (lit. 40); Gartner [2] qualifié de prévision sans méthode publiée (lit. 43); Gartner [95] : le cumul des contrôles n'est explicite que jusqu'au niveau 2 (lit. 45); Temporal : limite d'historique de 51 200 événements ou 50 Mo, à mentionner (lit. 71); RFC 9396 : le jeton d'approbation est un profil du cadre (lit. 32); RFC 8725, § 3.10, à citer en C.3 (lit. 33); « 5 Mo » plutôt que « 5 Mio » (lit. 54); balise CloudEvents ce@v1.0.2 à relire ([250], lit. 38).
- **Constat écarté par `audit_lit`** : « Erik S. » est la signature publiée de [6] (lit. 82). Le constat d'audit_01 est infondé.
- **Point resté ouvert** (tranche 4, 14-26) : le statut normatif du guide *Security Best Practices* de MCP [208]. `audit_lit` ne l'a pas tranché. Trancherait la lecture de la page dans l'arborescence de la révision 2026-07-28.

### 3.3 Preuves, essais et expérimentations additionnels exigés

Le cadre ne mesure rien lui-même. Les essais suivants conditionnent la tenabilité des exigences citées. Chacun produit un rapport versé à la base de preuves (index de l'EXIG-CON-18) et déclare sa règle de décision (A-32). Les essais 1 à 6 sont des préalables à l'homologation d'un premier agent N3 ou d'un premier palier P3 (1.3, condition 3).

1. **Banc d'essai de la passerelle sous contention** (EXIG-IAM-17 à 22, A-01, A-04).
   - Latence p50 et p99 de chacun des neuf contrôles de la figure 18, et de bout en bout, sous charge croissante, avec N répliques.
   - Atomicité du registre des `jti` sous réessais concurrents : aucune opération relayée deux fois avec deux empreintes, et aucun refus d'un réessai légitime.
   - Bascule de la politique en cache à l'échéance de sa validité.
   - Partition du plan de contrôle pendant une suspension poussée par le canal signé.
   - Coût du réchange de jetons à la terminaison TLS (A-16).
   - Disponibilité mesurée contre l'objectif inscrit.
   - Critère : objectifs inscrits au catalogue tenus au p99 sur la charge de pointe déclarée.
2. **Essais de compensation sous arrêts** (A-06, A-07, EXIG-ORC-20).
   - Saga à k étapes, avec arrêt injecté à chaque transition, par chacun des sept arrêts : coupe-circuit, suspension, révocation, mode fermé, budget épuisé, plafond de sauts, échéance du mandat.
   - Arrivée tardive de l'original après un délai d'expiration.
   - Double exécution et double échec de chaque compensation.
   - Compensations non commutatives, dans un ordre déclaré.
   - Panne de la passerelle pendant la compensation (file persistée).
   - Critère : effet net nul ou escalade humaine tracée dans 100 % des cas.
3. **Essais d'injection adaptative et d'exfiltration systémique** (A-17, EXIG-SEC-24).
   - Attaques adaptatives selon Nasr et coll. et Zhan et coll., en plus des jeux statiques (AgentDojo, ASB).
   - Contre-exemple de [4.01] (deux agents, A2A) et empoisonnement de la mémoire chargée au démarrage.
   - Exfiltration par la requête d'un outil P0.
   - Événement publié depuis une session marquée.
   - Critère : aucune exfiltration par un chemin déterministe couvert. Le taux résiduel des filtres probabilistes est rapporté sans relâcher aucun contrôle.
4. **Différentiel d'analyse JSON** (A-11).
   - Corpus de clés dupliquées, de grands entiers, de nombres en notation exponentielle, de séquences Unicode et de chaînes invalides.
   - Soumis à l'analyseur de la passerelle et à ceux des SDK MCP de niveau 1 (TypeScript, Python, Go, C#; lit. 9).
   - Critère : tout cas divergent est rejeté par la passerelle.
5. **Détection de troncature du journal d'audit** (A-19).
   - Suppression de la queue, réécriture complète par le détenteur de la clé, purge d'un segment, rotation des clés.
   - Critère : détection par la fonction indépendante au prochain point de contrôle.
6. **Exercice de coupe-circuit de bout en bout** (A-05, EXIG-SEC-26).
   - Délai entre la décision d'arrêt et le dernier refus dans tous les systèmes, y compris ceux sans SSF ni CAEP et les agents intégrés aux logiciels-services (A-03).
   - Critère : cible fixée par l'entreprise.
7. **Tests négatifs de délégation** (A-16).
   - Profondeur excédentaire refusée à l'échange.
   - Élargissement par changement d'audience.
   - Prolongation par échanges successifs.
   - Adjoint confus entre agents autonomes.
   - Blanchiment du niveau par l'exécutant.
   - Ajout à l'annexe A.
8. **Mesure de l'approbation machinale** (A-12, EXIG-AUT-20).
   - Actions piégées, fautives et connues, insérées dans le flux d'approbation.
   - Taux d'approbation, temps de décision et charge par approbateur et par jour, sous la présomption d'injection de l'EXIG-SEC-06.
   - Critère : taux de détection des actions piégées au-dessus d'un seuil fixé, et charge sous le plafond.
9. **Protocole de comparaison multiagent** (EXIG-ORC-02, A-32).
   - Comparaison appariée sur le jeu de référence : coût par tâche réussie (définition unique, [4.46]), intervalles de confiance, jeux réservés.
10. **Démonstration des cibles d'évaluation** (tableau 42, EXIG-EVA-03).
    - Taille d'échantillon conforme à la règle de trois. Par exemple, au moins 600 essais sans échec pour démontrer un taux inférieur à 0,5 %.
11. **Reproductibilité des classements**.
    - Accord entre évaluateurs (kappa) sur la classe de risque (tableau 46) et sur la cotation de maturité (§ 14.2), avec deux évaluateurs indépendants et un échantillon d'agents.
12. **Fractionnement des seuils** (A-13).
    - Suite de tests : appels juste sous le seuil, répétés dans une tâche et entre tâches d'un même mandant.
    - Critère : approbation déclenchée selon la portée et la fenêtre déclarées.
13. **Conformité OpenTelemetry au collecteur** (A-29).
    - Instrumentations courantes, au réglage par défaut et avec l'option d'adhésion.
    - Critère : les attributs du tableau 41 sont présents après correspondance.
14. **Conformité aux protocoles** (A-22).
    - a2a-tck et suite MCP, épinglées à une étiquette.
    - Rapport de stabilité des tests sur deux versions avant de les rendre bloquants.
15. **Vérifications documentaires préalables aux jalons**.
    - Relecture du règlement (UE) 2026/1744 au JO, avant J2a.
    - Lecture des textes consolidés de la Loi 25 sur LégisQuébec : art. 11, 63.3, 63.5, 18.3 et le règlement sur les incidents.
    - PDF de l'OWASP *Threats and Mitigations* et de NIST AI 100-2 E2025.

synth.md : 28 défauts transversaux, 34 arbitrages retenus
