# Consolidation tranche 3 — § 7.3 à 7.10, chapitre 8, début du chapitre 9, pages 91-122

## Synthèse (10 lignes au plus)
1. Sources : audit_10, audit_11, audit_12 (107 constats bruts, tous repris); `audit_lit.md` absent, les faits externes gardent le statut « à vérifier » des rapports bruts.
2. Après dédoublonnage et contre-vérification dans `full.txt` : 82 défauts (3 BLOQUANT, 38 MAJEUR, 41 MINEUR); aucun constat entièrement écarté, 6 écartés en partie, 5 rétrogradés.
3. La thèse T3 (« ne jamais refaire une action terminée ») ne tient pas telle quelle : une compensation peut précéder l'effet tardif de l'original (3.01), et tout arrêt (coupe-circuit, plafond, échéance de délégation, révocation) interdit les compensations qu'il rend nécessaires (3.02).
4. La thèse T5 (approbation liée à l'action exacte) a trois brèches : différentiel d'analyse JSON entre passerelle et serveur (3.03), écran d'approbation non dérivé des arguments hachés (3.22), état référencé modifiable pendant 15 minutes (3.23).
5. Conflit transversal central : l'usage unique du jeton d'approbation contre les réessais idempotents, la reprise durable et les répliques de passerelle (3.04); l'exemple C.6 place pourtant la clé d'idempotence dans les arguments hachés, ce qui fournit l'arbitrage (A3).
6. Thèse T2 : le chapitre 8 confie à la seule passerelle des contrôles qu'EXIG-IAM-17 ne lui fait pas voir pour les appels intradomaine (3.28).
7. Thèse T7 : « le plus strict » n'est pas un ordre défini (3.25); les seuils n'ont pas d'unité d'agrégation (3.27); plusieurs exigences renvoient à la « figure 15 » au lieu du contrôle calculé par AUT-10 (3.35).
8. Dérives inter-chapitres principales : ORC-16 contre OBS-12 (arguments en clair), AUT-11 contre IAM-18, AUT-14 (DEVRAIT) contre tableaux 31 et 46 (DOIT), AUT-22/23 contre CON-07/08, AUT-05 contre CON-03, IAM-07 contre GOV-13, AUT-15 contre GOV-04, unité du seuil p. 109 contre catalogue C.1.
9. Dix arbitrages de conception proposés, dont quatre touchent au moins trois autres tranches (A1, A3, A4, A5).

## Matrice des défauts

### [3.01] [BLOQUANT - Erreur formelle/architecturale] Compensation d'une étape incertaine : course avec un original encore en vol
- Constats d'origine : 10-01 (voir aussi 10-09 pour les tests, 10-12 pour la replanification)
- Localisation exacte : § 7.5, EXIG-ORC-16, p. 96 : « Une étape dont l'issue est inconnue est traitée comme possiblement exécutée : sa compensation est déclenchée et reste sans effet si l'action n'a pas eu lieu. »
- Diagnostic par premiers principes : vérifié p. 95-96. « Issue inconnue » ne veut pas dire « terminée ou jamais commencée » : la requête peut être en file ou en traitement chez le service visé. Une compensation conditionnelle (« rembourser si débité ») évalue sa condition à l'instant t et ne se rejoue pas si l'original s'exécute à t + ε (TOCTOU). La garantie couvre « n'a pas eu lieu », pas « aura lieu ». ORC-17 (réessayer d'abord) et ORC-22 (409 si l'original est en cours) atténuent le cas courant, mais pas celui où les réessais épuisés ont tous expiré ni celui où le 409 est compté comme un échec. ORC-16 fait aussi agir automatiquement dans le doute, à rebours de PRIN-12. L'échec est silencieux : la saga se croit compensée.
- Contre-exemple explicite : T3 « Débiter le client » expire à 30 s, les réessais expirent aussi (passerelle de paiement saturée); C3 « rembourser si débité » s'exécute à 90 s et ne trouve rien; le débit d'origine passe à 120 s. Client débité, saga marquée compensée, aucune alerte.
- Correctif proposé : réécrire la seconde phrase d'ORC-16 : « Une étape dont l'issue est inconnue DOIT être résolue avant toute compensation : par relance de la requête d'origine avec la même clé d'idempotence jusqu'à un résultat définitif (résultat mémorisé, rejet 422, ou absence de traitement attestée par le service), une réponse 409 valant attente et non échec; ou par révocation de la clé auprès du service, qui garantit le rejet d'un original tardif. À défaut de résolution dans le délai déclaré, la saga passe en file humaine (EXIG-ORC-18) sans compenser. » Ajouter à ORC-22 : « Le service DOIT permettre d'interroger l'état d'une clé et DEVRAIT permettre de la révoquer. » Reformuler la règle 2 (p. 95) dans le même sens et ajouter le test « original tardif après compensation » à ORC-20 (voir 3.11).

### [3.02] [BLOQUANT - Erreur formelle/architecturale] Les arrêts interdisent les compensations qu'ils rendent nécessaires
- Constats d'origine : 10-02, 10-10, 12-18
- Localisation exacte : EXIG-ORC-28, p. 100 : « L'arrêt bloque toute nouvelle étape, conserve l'état pour analyse et laisse les sagas en cours dans un état connu, suspendues ou compensées selon la procédure. » Aussi ORC-26 (p. 100), AUT-18 (p. 114), IAM-07 (p. 121), IAM-20 (p. 129).
- Diagnostic par premiers principes : vérifié. Une compensation est une étape (journalisée par ORC-16, exécutée par l'orchestrateur). « Bloque toute nouvelle étape » et « compensées » sont donc incompatibles. IAM-20 suspend l'agent « sur toutes les passerelles » et « désactive l'identité de l'agent », IAM-07 révoque « ses jetons actifs et ses délégations », AUT-18 arrête l'agent à l'échéance de sa délégation, ORC-26 arrête la boucle au plafond d'appels ou de coût : dans les quatre cas, plus aucune identité ni budget ne permet d'appeler un outil de compensation. Aucune exigence ne relie compensation et arrêt (recherche dans `full.txt` : aucune). L'« état connu » promis est en fait incohérent (stock réservé, verrous ORC-19 maintenus), et le lever réactive l'agent compromis.
- Contre-exemple explicite : coupe-circuit global pendant une injection; 200 sagas ont réservé du stock (T2) sans débiter. Elles restent figées, stock et verrous sémantiques compris. Variante : plafond de 10 appels atteint après T3; compenser T1 et T2 porte le total à 12, au-delà du plafond.
- Correctif proposé : appliquer l'arbitrage A1. Dans ORC-28, remplacer la phrase citée par : « L'arrêt bloque toute nouvelle étape métier vers l'avant et conserve l'état pour analyse. Les compensations des sagas en cours s'exécutent par le canal de compensation (section 7.5), sous une identité de service de compensation distincte, non révoquée par l'arrêt, limitée aux outils de compensation déclarés au catalogue; une saga passée au pivot termine ses étapes réessayables par ce canal ou passe en file humaine. » Ajouter à ORC-26 : « Les compensations disposent d'un budget réservé, distinct des plafonds d'exécution. » Ajouter à AUT-18 un état de drainage (plus de nouvelle tâche avant l'échéance, marge au moins égale à la durée maximale d'une saga). Ajouter à IAM-07 et IAM-20 : « sans préjudice du canal de compensation (EXIG-ORC-28) ».

### [3.03] [BLOQUANT - Erreur formelle/architecturale] L'empreinte h ne garantit pas que l'appel exécuté est l'appel approuvé (différentiel d'analyse JSON)
- Constats d'origine : 11-01, 12-05
- Localisation exacte : § 8.5, figure 16, étape 7, p. 111 : « recalcule h : toute modification des arguments invalide l'approbation »; EXIG-AUT-12 : « la passerelle DOIT vérifier la signature, l'expiration et l'usage unique, puis recalculer h ».
- Diagnostic par premiers principes : vérifié p. 111 et C.6 (p. 221 : « recalcule h sur l'appel reçu »). La RFC 8785 opère sur une valeur JSON analysée (I-JSON, nombres double IEEE 754). La passerelle analyse donc les arguments, puis les canonise. Rien n'exige qu'elle rejette les entrées non I-JSON (clés dupliquées, entiers au-delà de 2^53, substituts isolés) ni qu'elle transmette au serveur d'outil les octets canoniques sur lesquels h a été calculé. Deux analyseurs différents (premier ou dernier doublon retenu) lisent alors deux actions sous le même h. La propriété annoncée p. 111 (« change un seul argument [...] l'appel est refusé ») est fausse telle que spécifiée, sur le seul mécanisme qui protège les P3.
- Contre-exemple explicite : approbation de `{"beneficiaire":"A","montant":100}`; l'agent injecté émet `{"beneficiaire":"A","montant":100,"montant":100000}`. La passerelle garde la première occurrence (h identique, appel admis), le serveur MCP garde la dernière : virement de 100 000 $. Même effet avec un numéro de compte numérique de 20 chiffres, arrondi par la canonisation.
- Correctif proposé : ajouter à EXIG-AUT-12 : « La passerelle DOIT rejeter tout argument non conforme à I-JSON (RFC 7493 : clés dupliquées, nombres hors de la plage exacte d'un double, chaînes invalides) et DOIT transmettre au serveur d'outil exactement la forme canonique sur laquelle h a été calculé. » Ajouter à EXIG-AUT-08 ou au § 6.8 : « Dans les schémas des outils P2 et P3, montants et identifiants sont des chaînes ou des entiers en unités mineures. » Ajouter deux tests négatifs à l'annexe A (clé dupliquée, grand entier). Mettre à jour la lecture de C.6.

### [3.04] [MAJEUR - Lacune méthodologique/omission] Usage unique du jeton d'approbation contre réessai idempotent, reprise durable et répliques de passerelle
- Constats d'origine : 10-14, 11-04, 12-04
- Localisation exacte : EXIG-AUT-12, p. 111 : « un identifiant à usage unique »; figure 16 : « une seule fois et pendant 15 minutes au plus »; EXIG-ORC-21, p. 98 : clé « réutilisée telle quelle à chaque réessai ».
- Diagnostic par premiers principes : vérifié. Le chapitre 7 assume la réexécution (nœud LangGraph rejoué, activité Temporal réessayée, tableau 27); le chapitre 8 consomme le `jti` au premier passage. (a) Un appel P3 dont l'issue est inconnue après consommation du `jti` ne peut plus être réessayé avec la même clé : la passerelle le refuse avant que le service, seul à savoir si l'effet a eu lieu (Pourquoi d'ORC-22), ne réponde. (b) Une reprise après 15 minutes trouve le jeton expiré et redemande une approbation pour une action peut-être exécutée, terreau d'approbation machinale (§ 8.7). (c) Avec plusieurs répliques, l'usage unique exige un registre de `jti` partagé à inscription atomique, non exigé. Fait utile à l'arbitrage : en C.6 (p. 221-222), `idempotency_key` figure dans les arguments hachés, donc h lie déjà l'approbation à la clé d'idempotence.
- Contre-exemple explicite : délai dépassé vers le serveur de virement après consommation du `jti`; Temporal réessaie; la passerelle refuse (`jti` consommé); l'opérateur réapprouve un nouveau jeton, ou la saga compense un virement peut-être émis. Cas (c) : deux répliques reçoivent le même jeton à 2 ms d'intervalle et l'exécutent toutes deux.
- Correctif proposé : appliquer l'arbitrage A3. Dans AUT-12, remplacer « un identifiant à usage unique » par « un identifiant (jti) qui autorise une seule exécution de l'action d'empreinte h; tant que le jeton n'est pas expiré, la passerelle admet la représentation du même jti avec le même h (donc la même clé d'idempotence, incluse dans les arguments canonisés) pour un réessai, et le service visé déduplique (EXIG-ORC-22) ». Ajouter : « Le registre des jti DOIT être partagé entre les instances de la passerelle, à écriture conditionnelle atomique, et refuser en mode fermé s'il est indisponible. Après expiration, un réessai n'exige pas de nouvelle approbation si le service atteste, par la clé, que l'effet a déjà eu lieu; sinon, il en exige une. » Exiger qu'un outil P3 inclue la clé d'idempotence dans ses arguments déclarés (comme C.1). Renvoyer à AUT-12 depuis ORC-21; ajouter un test de concurrence à l'annexe A.

### [3.05] [MAJEUR - Lacune méthodologique/omission] Palier et approbation des compensations non définis
- Constats d'origine : 10-05
- Localisation exacte : EXIG-ORC-17, p. 96 : « Chaque compensation DOIT être idempotente et définie en termes métier (remboursement, avis rectificatif, libération de stock) ».
- Diagnostic par premiers principes : vérifié p. 96, 108-109. Un remboursement est un virement, un avis rectificatif une « communication externe officielle » : deux exemples P3 du tableau 31. Par EXIG-AUT-08, un outil d'écriture sans compensation déclarée est P3, ce qui est le cas de tout outil de compensation. AUT-09 interdit tout P3 sans approbation propre à l'appel. Soit les compensations échappent à l'approbation (brèche de PRIN-05), soit elles l'exigent, et ORC-16 (compensation « déclenchée ») et ORC-18 (deux échecs) deviennent inapplicables en incident, quand les approbateurs saturent.
- Contre-exemple explicite : panne de l'ERP; 500 compensations « remboursement » attendent chacune une approbation hors bande; les jetons expirent, ORC-18 compte des échecs, la file humaine déborde.
- Correctif proposé : appliquer l'arbitrage A2. Ajouter à ORC-17 : « Le palier de chaque outil de compensation est déclaré au catalogue. La compensation exacte d'une étape approuvée, bornée à son montant et liée à sa clé d'idempotence, est approuvée avec l'étape d'origine (empreinte de la compensation incluse dans la demande) et n'exige pas de nouvelle approbation; toute autre compensation P3 suit EXIG-AUT-09. » Ajouter l'exception correspondante à AUT-08 et AUT-09.

### [3.06] [MAJEUR - Lacune méthodologique/omission] La figure 13 enseigne un débit P3 avant le pivot et une formule de compensation erronée
- Constats d'origine : 10-03, 10-40
- Localisation exacte : figure 13, p. 95 : « T3 ✗ échec Débiter le client non reprenable [...] T4 · pivot Confirmation officielle irréversible · approbation »; « échec définitif → compenser de k−1 à 1 ».
- Diagnostic par premiers principes : vérifié p. 95-96, 108, 215. ORC-15 exige que « toute étape de palier P3 [...] se place au pivot ou après »; le tableau 31 classe le virement en P3 et l'annexe B (p. 215) dit que « l'émission d'un paiement, de palier P3, exige toujours une approbation signée hors bande ». La figure de référence montre un débit externe exécuté avant le pivot et sans approbation. « Non reprenable » n'est aucune des trois sortes d'étapes du texte. « De k−1 à 1 » omet Ck quand l'issue de Tk est incertaine (règle 2), ce que la note sous la figure dit sans corriger la formule.
- Contre-exemple explicite : une équipe calque sa saga sur la figure : le client est débité sans approbation, et le remboursement C3, lui-même P3 (3.05), attend une approbation.
- Correctif proposé : redessiner la figure : T3 « Préautoriser le paiement (sans capture) », compensable par annulation de la préautorisation (P2 déclaré); T4 pivot « Capturer le paiement et confirmer », approuvé. Remplacer « non reprenable » par « compensable ». Écrire « compenser de k−1 à 1 (de k à 1 si l'issue de Tk est incertaine) ». Ajouter au § 7.5 la règle : « une préautorisation annulable est P2; la capture est P3 ».

### [3.07] [MAJEUR - Lacune méthodologique/omission] Après le pivot, rien n'exige que les étapes réussissent à terme
- Constats d'origine : 10-04
- Localisation exacte : EXIG-ORC-15, p. 96 : « toute étape de palier P3 [...] se place au pivot ou après, une fois les validations critiques réussies et l'approbation humaine obtenue ».
- Diagnostic par premiers principes : vérifié. La saga à pivot (Microsoft [67], cité p. 95) suppose que les étapes postérieures sont « réessayables, idempotentes [...] jusqu'au terme ». ORC-15 admet au contraire plusieurs P3 « au pivot ou après » sans exiger qu'elles réussissent par réessai; après le pivot, un échec non transitoire n'a ni compensation ni escalade (ORC-17 et ORC-18 ne visent que les compensations). « L'approbation humaine obtenue », au singulier, se lit comme une approbation par saga, alors qu'AUT-09 l'exige par appel.
- Contre-exemple explicite : pivot = virement émis; étape suivante = avis officiel au client, refusé définitivement (adresse invalide). Aucune exigence ne dit quoi faire.
- Correctif proposé : réécrire la fin d'ORC-15 : « [...] le pivot, unique, est identifié; les étapes qui le suivent DOIVENT être idempotentes et réessayables jusqu'au succès, ou dotées d'une file humaine nommée pour l'échec définitif; chaque étape P3 reçoit sa propre approbation (EXIG-AUT-09, EXIG-AUT-12). » Ajouter le test « échec définitif après le pivot » à ORC-20.

### [3.08] [MAJEUR - Lacune méthodologique/omission] Ordre et dépendances des compensations présupposés, jamais déclarés
- Constats d'origine : 10-06
- Localisation exacte : EXIG-ORC-18, p. 96 : « poursuivre les compensations qui n'en dépendent pas »; figure 13 : « COMPENSATIONS (ORDRE INVERSE, IDEMPOTENTES) »; règle 3 : « ne suit pas toujours l'ordre inverse exact ».
- Diagnostic par premiers principes : vérifié. ORC-18 suppose un graphe de dépendances entre compensations, que ni ORC-15, ni ORC-16, ni le catalogue (§ 6.8) n'obligent à déclarer; la figure impose l'ordre inverse que la règle 3 relativise. Sans graphe, deux orchestrateurs conformes divergent.
- Contre-exemple explicite : C2 (libérer le stock) échoue deux fois; C1 (annuler le transport) en dépend-elle? Un orchestrateur exécute C1, un autre s'abstient.
- Correctif proposé : ajouter à ORC-15 : « La définition de la saga déclare l'ordre de compensation (ordre inverse par défaut) et les dépendances entre compensations; ORC-18 s'applique selon ce graphe. » Ajouter à ORC-20 la vérification de cet ordre.

### [3.09] [MAJEUR - Lacune méthodologique/omission] Une chorégraphie n'a pas d'orchestrateur, or ORC-16 à 18 en exigent un
- Constats d'origine : 10-07
- Localisation exacte : EXIG-ORC-08, p. 92 : chorégraphie qui « DOIT avoir un propriétaire de bout en bout inscrit au registre, une saga explicite »; ORC-16 et ORC-18 : « l'orchestrateur DOIT ».
- Diagnostic par premiers principes : vérifié p. 91-92 et 96. Par définition, « dans une chorégraphie, aucun composant central ne voit l'ensemble » (p. 75). Le journal tenu avant l'action, la décision sur l'incertain et le décompte des échecs sont attribués à « l'orchestrateur »; un propriétaire au registre n'est pas un composant d'exécution. La figure 12 oriente vers la chorégraphie tout déclenchement par événement : le cas est fréquent.
- Contre-exemple explicite : trois consommateurs Kafka exécutent T1-T3; T3 échoue : personne ne tient le journal corrélé ni ne compte les deux échecs de C2.
- Correctif proposé : ajouter à ORC-08 : « Une chorégraphie qui produit des effets dans plusieurs systèmes d'enregistrement DOIT disposer d'un coordinateur de saga (composant d'exécution) qui tient le journal d'ORC-16 et applique ORC-16 à ORC-18. » Dans ORC-16 à 18, remplacer « l'orchestrateur » par « l'orchestrateur ou le coordinateur de saga ».

### [3.10] [MAJEUR - Lacune méthodologique/omission] Verrou sémantique sans échéance et sans portée sur les écrivains hors saga
- Constats d'origine : 10-08
- Localisation exacte : § 7.5, p. 96 : verrou « réservation en attente », visible des autres sagas; EXIG-ORC-19, p. 97 : « Lorsque plusieurs sagas ou agents peuvent modifier les mêmes enregistrements ».
- Diagnostic par premiers principes : vérifié. Un verrou sémantique ne protège que contre les écrivains qui le respectent; ORC-19 ne vise pas les humains, traitements en lot et intégrations historiques. Aucune échéance ni propriétaire de verrou n'est exigé, alors qu'ORC-18 (file humaine), ORC-28 (suspension) et interrupt() (attente « sans limite », p. 93) prolongent la saga indéfiniment.
- Contre-exemple explicite : saga en file humaine un vendredi; le verrou bloque les ventes en ligne jusqu'au lundi, pendant que la vente au comptoir, hors saga, vend l'article.
- Correctif proposé : réécrire ORC-19 : « Lorsque plusieurs sagas, agents ou autres écrivains du système d'enregistrement peuvent modifier les mêmes enregistrements [...]. Tout verrou sémantique DOIT avoir une échéance, un propriétaire et une procédure de libération en cas de suspension ou d'escalade. »

### [3.11] [MAJEUR - Lacune méthodologique/omission] Les quatre tests d'ORC-20 omettent les cas les plus dangereux
- Constats d'origine : 10-09
- Localisation exacte : EXIG-ORC-20, p. 97 : « échec forcé de chaque étape Tk [...]; plantage entre l'écriture au journal et l'action; double exécution de chaque compensation; double échec d'une compensation ».
- Diagnostic par premiers principes : vérifié. Le plantage entre journal et action ne produit qu'une étape non exécutée, le cas facile. Le cas qui fonde la règle 2 (effet réalisé, résultat perdu) n'est pas testé, ni l'original tardif (3.01), ni les sagas concurrentes (ORC-19), ni l'échec après le pivot (3.07), ni l'arrêt en cours de saga (3.02), ni le plantage pendant une compensation. Les doublures ne reproduisent pas l'idempotence réelle du service, que seul ce service connaît (Pourquoi d'ORC-22).
- Contre-exemple explicite : une saga réussit les quatre tests; en production, un délai expiré sur un débit réussi déclenche une compensation pendant qu'un réessai double le débit.
- Correctif proposé : remplacer « quatre tests » par « les tests suivants » et ajouter : effet réalisé et résultat perdu; original tardif après compensation; sagas concurrentes sur le même enregistrement; échec définitif après le pivot; arrêt par coupe-circuit en cours de saga; plantage pendant une compensation. Ajouter : « un test de contrat d'idempotence DOIT s'exécuter contre l'environnement d'essai du service visé ». Renommer l'exigence (« Tests d'injection de fautes ») et mettre à jour l'annexe D.

### [3.12] [MAJEUR - Lacune méthodologique/omission] Aucune durée de conservation des clés d'idempotence
- Constats d'origine : 10-11
- Localisation exacte : EXIG-ORC-22, p. 98 : « un doublon ne produit aucun effet supplémentaire; une clé réutilisée avec des arguments différents est rejetée ».
- Diagnostic par premiers principes : vérifié (aucune clause de durée). La déduplication ne vaut que pendant la conservation des clés par le service. Les exécutions du cadre durent des jours (attente de trois jours, p. 93; interrupt() « sans limite »; Temporal « sans limite de durée »; Step Functions jusqu'à un an). L'expiration des clés prévue par le brouillon IETF [78] reste à vérifier (source externe), mais toute mise en œuvre réelle purge les clés.
- Contre-exemple explicite : service qui garde les clés 24 h; reprise à 72 h après approbation; T2 rejouée avec une clé purgée : stock réservé deux fois.
- Correctif proposé : ajouter à ORC-22 : « La durée de conservation des clés est déclarée au catalogue; elle DOIT être au moins égale à la durée maximale d'exécution (EXIG-ORC-26) augmentée de la fenêtre de compensation. L'orchestrateur NE DOIT PAS reprendre une étape au-delà de cette durée sans résolution explicite (EXIG-ORC-16). »

### [3.13] [MAJEUR - Lacune méthodologique/omission] La sémantique de step_id ne couvre ni les itérations, ni la replanification d'une étape incertaine, ni les bifurcations
- Constats d'origine : 10-12
- Localisation exacte : EXIG-ORC-21, p. 98 : « Une étape replanifiée avec d'autres arguments reçoit un nouvel identifiant d'étape, donc une nouvelle clé. »
- Diagnostic par premiers principes : vérifié. (1) Une itération légitime (boucle évaluateur-optimiseur, ORC-05) sans indice d'itération dans step_id est absorbée comme doublon ou rejetée en 422. (2) Replanifier une étape dont l'issue est incertaine crée une nouvelle clé et un second effet; rien n'exige de résoudre l'ancienne d'abord. (3) Le voyage dans le temps de LangGraph (p. 94) bifurque avec les mêmes identifiants.
- Contre-exemple explicite : « réserver 10 unités » expire; replanification « réserver 12 unités » sous un nouveau step_id : 22 unités réservées.
- Correctif proposé : ajouter à ORC-21 : « step_id encode le chemin de l'étape dans le plan, l'indice d'itération et le numéro de bifurcation. Une étape dont l'issue est incertaine NE DOIT PAS être replanifiée avant sa résolution (EXIG-ORC-16). Une bifurcation par voyage dans le temps reçoit un nouvel espace de clés. »

### [3.14] [MAJEUR - Lacune méthodologique/omission] Déduplication « par son adaptateur » contre « seul le système visé sait »
- Constats d'origine : 10-13
- Localisation exacte : EXIG-ORC-22, p. 98 : « DOIT vérifier la clé côté serveur, directement ou par son adaptateur »; Pourquoi : « seul le système visé sait si l'effet a déjà eu lieu ».
- Diagnostic par premiers principes : vérifié. Un adaptateur qui inscrit la clé puis appelle un système non idempotent n'est pas atomique avec l'effet; s'il plante entre les deux, il ignore si l'effet a eu lieu, exactement ce que le Pourquoi reconnaît.
- Contre-exemple explicite : l'adaptateur MCP d'un ERP inscrit K « en cours », l'ERP crée la commande, l'adaptateur plante; au réessai, 409 sans fin, ou purge de K et seconde commande.
- Correctif proposé : ajouter à ORC-22 : « Un adaptateur n'est admis que s'il inscrit la clé dans la même transaction que l'effet, ou s'il peut interroger le système visé par une référence externe dérivée de la clé (p. ex. numéro de commande); sinon l'outil est classé P3. »

### [3.15] [MAJEUR - Lacune méthodologique/omission] « Déplacer après le point de pause » ne règle pas le réessai (ORC-12, AUT-17)
- Constats d'origine : 10-15, 12-16
- Localisation exacte : EXIG-ORC-12, p. 94 : « Tout effet de bord placé avant un point de pause ou dans une étape réessayable DOIT être idempotent; sinon, il DOIT être déplacé après le point de pause. » EXIG-AUT-17, p. 113 : « s'il ne peut pas être déplacé, il DOIT porter une clé d'idempotence ».
- Diagnostic par premiers principes : vérifié. Déplacer l'effet après interrupt() règle la réexécution du nœud interrompu, pas celle d'une étape réessayable ni celle du nœud qui échoue plus loin ou contient plusieurs interrupt(). L'échappatoire contredit ORC-21 (clé obligatoire pour toute écriture P2/P3). AUT-17 inverse la logique : un NE DOIT PAS levé dès que l'appel « ne peut pas être déplacé » est un DEVRAIT sans juge de l'impossibilité, et une clé générée dans le nœud (UUID aléatoire) change à chaque redémarrage. Les effets de bord hors P2/P3 (notification, événement, appel de modèle facturé) ne sont couverts par aucune des deux.
- Contre-exemple explicite : notification non idempotente placée après interrupt(); erreur réseau plus loin dans le même nœud; le nœud est réessayé et la notification part deux fois.
- Correctif proposé : remplacer la seconde phrase d'ORC-12 par : « Tout effet de bord, écriture ou non, DOIT être idempotent par une clé déterministe (EXIG-ORC-21) ou isolé dans une étape journalisée exécutée au plus une fois; son emplacement par rapport au point de pause n'en dispense pas. » Réduire AUT-17 à : « [...] Un appel à effet de bord NE DOIT PAS précéder le point d'interruption dans la même étape (EXIG-ORC-12). » et supprimer l'exception.

### [3.16] [MAJEUR - Lacune méthodologique/omission] ORC-11 : portée sans proportionnalité et granularité que les cadriciels cités ne tiennent pas
- Constats d'origine : 10-16, 10-17
- Localisation exacte : EXIG-ORC-11, p. 94 : « Tout flux de plus d'une étape [...] DOIT s'exécuter sur un moteur d'exécution durable qui persiste l'état après chaque transition (appel de modèle, appel d'outil, décision, réponse humaine) ».
- Diagnostic par premiers principes : vérifié p. 93-94. (1) Un agent N1 qui fait deux lectures P0-P1 est un « flux de plus d'une étape » : persister après chaque appel de modèle ajoute latence, coût et RP stockés (ORC-13) sans aucun risque de double effet, contre PRIN-08. (2) Le texte décrit lui-même Microsoft Agent Framework comme persistant « à la fin de chaque étape de calcul du flux » (p. 93), non après chaque appel de modèle ou d'outil interne à un exécuteur; LangGraph persiste par super-étape (à vérifier, [124]). Le tableau 27 présente ces produits sans signaler l'écart.
- Contre-exemple explicite : un exécuteur MAF fait cinq appels d'outils dans une étape et plante au quatrième; la reprise rejoue les cinq, protégée par les seules clés d'idempotence.
- Correctif proposé : réécrire ORC-11 : « Tout flux qui comporte au moins une étape P2 ou P3, une attente humaine ou une durée supérieure à un seuil déclaré DOIT s'exécuter sur un moteur d'exécution durable qui persiste l'état après chaque étape journalisée; chaque appel non déterministe à effet est sa propre étape (EXIG-ORC-12). Les autres flux DEVRAIENT le faire. » Ajouter aux « Points d'attention » de LangGraph et de MAF, tableau 27 : « granularité de persistance à aligner sur EXIG-ORC-11 ».

### [3.17] [MAJEUR - Lacune méthodologique/omission] Réessais : ni gigue, ni couche unique, ni borne, ni décompte dans les plafonds
- Constats d'origine : 10-19
- Localisation exacte : EXIG-ORC-27, p. 100 : « des réessais à temporisation exponentielle (exponential backoff) limités aux erreurs transitoires et un disjoncteur ».
- Diagnostic par premiers principes : vérifié (absence de ces clauses). Sans gigue, les clients se resynchronisent après une panne. Les réessais s'empilent par couche (SDK, passerelle de modèles, activité Temporal, passerelle d'agents, sous-agent) : n essais sur k couches donnent nᵏ appels. ORC-26 ne dit pas si les réessais comptent dans les plafonds. La politique de réessai par défaut de Temporal (tentatives illimitées?) reste à vérifier (source externe).
- Contre-exemple explicite : panne de 10 minutes du fournisseur de modèle; trois couches de cinq réessais donnent 125 appels par requête, synchronisés; pic de facturation et quota saturé à la reprise.
- Correctif proposé : compléter ORC-27 : « [...] temporisation exponentielle avec gigue, un nombre de tentatives borné et déclaré, une seule couche propriétaire des réessais par dépendance (les autres à zéro), et un budget de réessai global; les réessais comptent dans les plafonds d'EXIG-ORC-26. »

### [3.18] [MAJEUR - Lacune méthodologique/omission] Circulation des jetons (délégué, approbation) non spécifiée, contre EXIG-IAM-06
- Constats d'origine : 10-20, 12-07
- Localisation exacte : EXIG-ORC-23, p. 99 : message « limité [...] au jeton délégué du mandant »; exemple p. 98 : « "jeton_delegue": "<jeton délégué du mandant, audience = agent-credit>" »; figure 16 : « rejoue l'appel avec le jeton ».
- Diagnostic par premiers principes : vérifié. IAM-06 (p. 121) : « aucun jeton, certificat ni secret n'entre dans le contexte du modèle, dans la mémoire de l'agent, dans les arguments d'un outil ou dans les traces ». Le jeton délégué placé dans le corps du message de délégation devient arguments d'outil (agent utilisé comme outil), entre dans le contexte du modèle exécutant, dans le point de contrôle (ORC-13 : « y compris les messages en attente ») et dans le journal d'ORC-16 (« ses arguments »). Pour le jeton d'approbation, la figure 16 ne dit pas par où il transite; le renvoyer au modèle dans un résultat d'outil viole IAM-06.
- Contre-exemple explicite : l'orchestrateur appelle l'agent de crédit comme outil; le jeton entre dans le contexte de l'exécutant, puis dans le point de contrôle PostgreSQL; une injection dans un état financier le fait recopier en sortie.
- Correctif proposé : appliquer l'arbitrage A5. Dans ORC-23, remplacer « au jeton délégué du mandant (section 9.3) » par « à la référence de délégation; le jeton délégué voyage dans l'en-tête d'authentification du transport (A2A, MCP), injecté par le code d'exécution ou la passerelle, et il est exclu des points de contrôle, des journaux et du contexte du modèle (EXIG-IAM-06) »; corriger l'exemple (`"delegation": "<transmise en en-tête, hors message>"`). Dans la figure 16 et § 8.5 : « la passerelle conserve le jeton et rattache la reprise à la demande d'approbation; le jeton ne transite jamais par le contexte du modèle ».

### [3.19] [MAJEUR - Lacune méthodologique/omission] Le message de délégation exclut les identifiants nécessaires à des clés stables
- Constats d'origine : 10-21
- Localisation exacte : EXIG-ORC-23, p. 99 : message « limité au sous-objectif, aux critères d'acceptation, aux paramètres requis, aux références d'artefacts, au jeton délégué [...], au contexte de trace [...], au budget restant et au schéma de retour ».
- Diagnostic par premiers principes : vérifié (liste fermée). L'exécutant doit dériver des clés stables d'un réessai de délégation à l'autre (ORC-21), mais ne reçoit ni task_id, ni step_id, ni clé parente; le traceparent change de span-id à chaque essai. La liste omet aussi le palier maximal et le niveau d'autonomie autorisés.
- Contre-exemple explicite : délégation « réserver le stock »; la réponse se perd, l'orchestrateur réessaie; le sous-agent crée un nouveau task_id et réserve deux fois.
- Correctif proposé : ajouter à la liste d'ORC-23 « la clé d'idempotence de la délégation (dérivée du task_id et du step_id de l'orchestrateur), dont l'exécutant dérive ses propres clés, et le palier maximal autorisé »; compléter l'exemple p. 98.

### [3.20] [MAJEUR - Lacune méthodologique/omission] Journal de compensation : arguments en clair, sans contrôles ni lien avec le journal d'audit
- Constats d'origine : 10-23
- Localisation exacte : EXIG-ORC-16, p. 96 : « consigner dans un journal durable, en ajout seul et corrélé à la trace, l'étape, ses arguments, sa clé d'idempotence et la compensation ».
- Diagnostic par premiers principes : vérifié p. 96 et 151. Ce journal stocke des arguments en clair (montants, identifiants de clients). EXIG-OBS-12 écrit au contraire que, dans le journal d'audit, « les arguments d'outil n'y figurent que par leur empreinte SHA-256 », et ORC-13 impose accès restreint, chiffrement et élagage aux seuls points de contrôle. ORC-16 n'impose ni l'un ni l'autre, ni conservation, ni destruction (EXIG-CON-10), et ne dit pas s'il se confond avec le journal d'audit ou l'historique du moteur durable. Dérive inter-chapitres ch. 7 / ch. 10.
- Contre-exemple explicite : un journal en ajout seul de 24 mois contient numéros de clients et montants en clair, lisible par l'exploitation hors des contrôles du journal d'audit.
- Correctif proposé : ajouter à ORC-16 : « Ce journal est soumis aux contrôles d'EXIG-ORC-13 (accès, chiffrement, conservation, élagage au plus tard à la clôture de la saga augmentée d'un délai déclaré); l'historique du moteur durable PEUT en tenir lieu. Il est distinct du journal d'audit (EXIG-OBS-11), qui n'en reçoit que les empreintes. »

### [3.21] [MAJEUR - Lacune méthodologique/omission] ORC-30 ne fait pas démontrer les capacités propres au chapitre 7
- Constats d'origine : 10-24
- Localisation exacte : EXIG-ORC-30, p. 102 : « la persistance durable des points de contrôle et la reprise après panne; la pause pour approbation humaine sans perte d'état; l'émission de traces OpenTelemetry [...] ».
- Diagnostic par premiers principes : vérifié. La preuve de concept omet la propagation d'une clé d'idempotence stable (ORC-21), la compensation et l'escalade de saga (ORC-15 à 18), les plafonds par exécution (ORC-26), le coupe-circuit ciblé et global (ORC-28), la cohabitation des versions (ORC-14) et la granularité d'ORC-11. Le tableau 27 signale d'ailleurs un coupe-circuit « annoncé » à « vérifier selon la version déployée » (p. 102).
- Contre-exemple explicite : une plateforme SaaS réussit la preuve de concept mais n'offre ni plafond de coût par exécution ni arrêt ciblé d'un outil; l'écart apparaît à l'homologation de l'agent.
- Correctif proposé : ajouter à la liste d'ORC-30 : « la propagation d'une clé d'idempotence stable; l'exécution des compensations et de l'escalade de saga (tests d'EXIG-ORC-20); les plafonds par exécution; l'arrêt ciblé et global ».

### [3.22] [MAJEUR - Lacune méthodologique/omission] Ce que voit l'approbateur n'est pas tenu de correspondre à ce que couvre h
- Constats d'origine : 11-02, 12-20
- Localisation exacte : EXIG-AUT-19, p. 114 : « L'écran d'approbation DOIT présenter l'action exacte, ses paramètres, son effet attendu »; C.6, p. 221 : authorization_details « pour l'écran d'approbation et l'audit, sans remplacer l'empreinte ».
- Diagnostic par premiers principes : vérifié p. 111, 114, 221-222. Le jeton porte deux représentations : h (ce qui sera exécuté) et authorization_details (ce qui est montré). Aucune exigence n'impose que l'écran soit une fonction déterministe des arguments canonisés ni que les deux concordent; l'auteur d'authorization_details et de l'« effet attendu » n'est pas désigné (s'il s'agit de l'agent, AUT-13 l'exclut). Dans C.6, authorization_details omet `lignes` (SKU, quantités, prix) et `statut_demande`, présents dans les arguments hachés : l'approbateur approuve une empreinte dont il n'a pas vu tout le contenu.
- Contre-exemple explicite : une injection remplace un SKU par un article non autorisé, au même total; l'écran tiré d'authorization_details montre fournisseur, total et centre de coût exacts; l'approbateur approuve et h concorde.
- Correctif proposé : ajouter à AUT-19 : « L'écran est produit par le service d'approbation à partir des seuls arguments canonisés et du schéma de l'outil inscrit au catalogue, jamais d'un texte fourni par l'agent; il montre tous les champs, sauf ceux que le catalogue déclare non significatifs. authorization_details, s'il est présent, DOIT être dérivé de ces arguments par le service d'approbation et vérifié avant signature. » Compléter authorization_details dans C.6 (lignes, statut) ou déclarer au catalogue C.1 les champs non significatifs.

### [3.23] [MAJEUR - Lacune méthodologique/omission] h lie les arguments, pas l'état des ressources qu'ils désignent (TOCTOU)
- Constats d'origine : 11-03
- Localisation exacte : § 8.5, p. 110 : « Une approbation n'a de valeur que si elle porte sur l'action exacte qui sera exécutée »; AUT-12 : « Le jeton DOIT expirer au plus 15 minutes après sa signature. »
- Diagnostic par premiers principes : vérifié (aucune précondition d'état exigée). Les arguments P3 désignent souvent des ressources par identifiant (facture, fournisseur). Pendant les 15 minutes, un autre processus peut modifier le référent; l'action exécutée n'est plus celle approuvée.
- Contre-exemple explicite : approbation de `payer_facture{"facture":"F-123"}` à 10 h; à 10 h 05 le compte bénéficiaire du fournisseur est changé; à 10 h 10 le paiement part vers le nouveau compte avec un h valide.
- Correctif proposé : ajouter à AUT-12 : « Pour un outil P3, les arguments approuvés DOIVENT inclure les valeurs résolues qui déterminent l'effet (bénéficiaire, montant) ou une précondition de version (ETag, numéro de version) vérifiée par le serveur de ressources à l'exécution. »

### [3.24] [MAJEUR - Lacune méthodologique/omission] Vérification du jeton incomplète; la double approbation n'est ni représentée ni vérifiée
- Constats d'origine : 11-05, 11-23, 12-03, 12-11
- Localisation exacte : EXIG-AUT-12, p. 111 : « vérifier la signature, l'expiration et l'usage unique, puis recalculer h »; EXIG-AUT-15, p. 112 : « deux approbateurs distincts DOIVENT approuver ».
- Diagnostic par premiers principes : vérifié p. 111-112, 221, 223. La liste de vérification omet : l'émetteur et l'audience (présents en C.6 mais absents du contenu minimal); la concordance de l'agent et de la tâche avec l'appelant (AUT-13 l'exige sous forme négative, h ne contient ni agent ni tâche); l'habilitation de l'approbateur au registre (AUT-15); le nombre d'approbateurs requis. Le jeton ne porte qu'un approbateur, l'audit C.8 un seul champ `approbateur` et un seul `approbation_jti`; un pseudonyme non stable empêche de constater que deux jetons viennent de deux personnes. La figure 16 omet aussi agent et jti.
- Contre-exemple explicite : un employé non habilité mais connu du fournisseur d'identité approuve par CIBA un P3; ou un seul jeton valide arrive pour un P3 de classe élevée. Dans les deux cas, toutes les vérifications d'AUT-12 passent.
- Correctif proposé : réécrire la vérification d'AUT-12 : « [...] la passerelle DOIT vérifier la signature, l'émetteur, l'audience (elle-même), l'expiration et l'usage unique (A3), la concordance de l'agent et de la tâche avec l'appel, puis recalculer h. » Ajouter : « Le service d'approbation vérifie avant de signer que chaque approbateur est habilité au registre pour le contrôle visé; le jeton porte la liste des approbateurs (pseudonymes stables par personne au sein du service), tous sur le même h, et la passerelle vérifie leur nombre et leur distinction selon le contrôle calculé (EXIG-AUT-10). » Adapter la figure 16 (`{ h, approbateurs[], agent, tâche, jti, exp }`), C.6 et C.8 (`approbateurs[]`).

### [3.25] [MAJEUR - Lacune méthodologique/omission] « Le plus strict » n'est pas défini sur des contrôles non comparables
- Constats d'origine : 11-06
- Localisation exacte : EXIG-AUT-10, p. 110 : « en retenant le plus strict des éléments suivants : la cellule classe × palier de la figure 15, le niveau d'autonomie de l'agent et les déclencheurs d'approbation ».
- Diagnostic par premiers principes : vérifié p. 109-110. Les cellules mêlent contrôles techniques (jeton délégué, masquage, filtrage par ligne), traçabilité (audit), revue (« finalité vérifiée, minimisation ») et approbation (conditionnelle, systématique, à deux). Ces éléments ne forment pas un ordre total; « retenir le plus strict » peut se lire « remplacer » au lieu de « cumuler » (T7).
- Contre-exemple explicite : agent modéré, outil P1 (« jeton délégué, filtrage par ligne »), déclencheur actif; si l'approbation « l'emporte », le filtrage par ligne disparaît.
- Correctif proposé : réécrire AUT-10 : « [...] le contrôle exigé est l'union des contrôles de la cellule, du niveau et des déclencheurs; pour l'approbation, on retient la forme la plus forte selon l'ordre : aucune < au-delà du seuil < à chaque appel < à chaque appel avec second approbateur < refus. » Reprendre cet ordre dans la légende de la figure 15 et au § 8.4.

### [3.26] [MAJEUR - Lacune méthodologique/omission] Déclencheur de cumul plus étroit que SEC-04; « session » non définie
- Constats d'origine : 11-07
- Localisation exacte : EXIG-AUT-10, p. 110 : « cumul de contenu non fiable, de données sensibles et d'action externe »; exemple p. 110 : outil P2 qui « tombe donc sous approbation ».
- Diagnostic par premiers principes : vérifié p. 110 et 134. La branche [C] de Meta et d'EXIG-SEC-04 couvre tout changement d'état (« outils P2, P3 ou envoi externe »); AUT-10 ne vise que l'« action externe » et, lu à la lettre, ne déclenche rien dans son propre exemple (P2 interne). SEC-04 couvre le cas, mais par une autre exigence que celle qui calcule le contrôle à la passerelle. « Session » n'est définie nulle part (glossaire : aucune entrée); pour un N4 « en continu » ou un agent à mémoire persistante, la session ne finit jamais, ou se découpe arbitrairement pour échapper à la règle.
- Contre-exemple explicite : un N3 lit un courriel piégé, lit un dossier client et appelle « mise à jour de statut » (P2); une passerelle conforme à AUT-10 ne déclenche rien.
- Correctif proposé : dans AUT-10, remplacer « et d'action externe » par « et de changement d'état ou de communication externe (outils P2, P3 ou envoi externe, au sens d'EXIG-SEC-04) ». Ajouter au glossaire « Session » selon l'arbitrage A7 (contexte du modèle depuis le dernier contexte vierge, mémoire persistante comprise, propagée aux agents délégués).

### [3.27] [MAJEUR - Lacune méthodologique/omission] Seuils sans unité d'agrégation : contournement par fractionnement
- Constats d'origine : 11-08
- Localisation exacte : tableau 31, p. 108 : « seuil métier au catalogue (p. ex. 5 000 $); approbation au-delà du seuil »; p. 109 : « le seuil déclaré de l'outil est de 25 par tâche ».
- Diagnostic par premiers principes : vérifié. Le seuil s'exprime tour à tour par appel (C.1, p. 218 : `"approval_threshold": { "argument": "montant_total_cad", "max_without_approval_cad": 5000 }`), par tâche (p. 109), par exécution (tableau 30, AUT-07) ou par heure (tableau 28). Aucune exigence ne fixe la portée d'agrégation (appel, tâche, agent, mandant, fenêtre); recherche de « fractionn » et « agrég » : rien. Dérive inter-chapitres : l'exemple de la p. 109 (par tâche) n'est pas exprimable dans le format du catalogue C.1 (par argument d'un appel).
- Contre-exemple explicite : 40 factures en deux appels de 20; ou 50 avoirs de 4 999 $ sous un seuil de 5 000 $ par appel : aucune approbation.
- Correctif proposé : ajouter à AUT-08 : « Chaque seuil inscrit au catalogue déclare son unité et sa portée d'agrégation : par appel et en cumul par tâche, par agent et par mandant sur une fenêtre déclarée; la passerelle tient ces compteurs et applique le seuil au cumul. » Étendre `approval_threshold` en C.1 (champs `scope`, `window`) et ajouter un test de fractionnement à l'annexe A.

### [3.28] [MAJEUR - Lacune méthodologique/omission] La passerelle ne voit pas tous les appels que le chapitre 8 lui fait contrôler
- Constats d'origine : 11-09
- Localisation exacte : EXIG-AUT-10, p. 110 : « Pour chaque appel d'outil, la passerelle d'agents DOIT »; EXIG-IAM-17, p. 129 : « À l'intérieur d'un domaine, la décision par appel (EXIG-IAM-02) est appliquée par le serveur de ressources ».
- Diagnostic par premiers principes : vérifié. IAM-17 ne fait passer par la passerelle que les appels vers un serveur MCP, vers un agent ou ceux qui franchissent une frontière de domaine. Un appel intradomaine à une API non MCP y échappe. Or AUT-01 (plafond de niveau), AUT-10 (contrôle calculé), AUT-11 (mode fermé) et AUT-12 (jeton et h) ne désignent que la passerelle. Pour ces appels, aucun composant n'applique le chapitre 8 (T2).
- Contre-exemple explicite : un N3 appelle directement l'API de facturation de son domaine (action P3); le serveur de ressources applique OAuth, mais ni jeton d'approbation ni h.
- Correctif proposé : appliquer l'arbitrage A4. Ajouter à IAM-17 : « Tout appel d'outil P2 ou P3 passe par la passerelle d'agents, quelle que soit la frontière. » À défaut, remplacer « la passerelle d'agents » par « le point d'application des politiques (passerelle ou serveur de ressources, EXIG-IAM-17) » dans AUT-01, AUT-10, AUT-11 et AUT-12, avec obligation pour le serveur de ressources de vérifier le jeton d'approbation.

### [3.29] [MAJEUR - Lacune méthodologique/omission] EXIG-AUT-11 indécidable si le catalogue est en panne, et non réconciliée avec EXIG-IAM-18
- Constats d'origine : 11-10
- Localisation exacte : EXIG-AUT-11, p. 110 : « Si le service d'approbation, le catalogue ou le service de politiques est indisponible [...], la passerelle DOIT refuser tout appel P3 et tout appel P2 au-delà du seuil »; IAM-18, p. 129 : « elle continue d'appliquer la dernière politique distribuée ».
- Diagnostic par premiers principes : vérifié. (1) Le palier et le seuil viennent du catalogue : catalogue indisponible, la passerelle ne peut pas savoir ce qui est P3 ou P2 au-delà du seuil, faute de règle de cache. (2) Service de politiques indisponible : IAM-18 applique la dernière politique (un P3 approuvé passe), AUT-11 refuse tout P3. (3) Service d'approbation indisponible pour un N2 : AUT-11 ne vise pas le P2 sous le seuil, qui exige pourtant une approbation à ce niveau. Le cas « aucune politique » est, lui, réglé par le renvoi à IAM-18 (voir constats écartés).
- Contre-exemple explicite : panne du catalogue; un outil reclassé de P2 à P3 figure encore en P2 dans le cache de la passerelle; l'appel passe.
- Correctif proposé : réécrire AUT-11 par cas : « Catalogue indisponible : la passerelle applique le dernier instantané signé s'il date de moins de T déclaré; au-delà, tout outil d'écriture est traité comme P3. Service de politiques indisponible : dernière politique distribuée (EXIG-IAM-18), sauf pour P3, refusé. Service d'approbation indisponible : refus de tout appel dont le contrôle calculé (EXIG-AUT-10) exige une approbation. Aucune politique applicable : refus (EXIG-IAM-18). » Ajouter à IAM-18 un renvoi à AUT-11.

### [3.30] [MAJEUR - Lacune méthodologique/omission] Règle d'or inopérante tant que les seuils ne sont pas approuvés (ouverture par défaut)
- Constats d'origine : 11-12
- Localisation exacte : EXIG-AUT-07, p. 108 : « atteignent les seuils d'étalonnage approuvés par le comité »; p. 107 : « Aucune source reconnue ne propose de valeurs universelles. »
- Diagnostic par premiers principes : vérifié. Sans seuils publiés (phase de fondations, nouveau type d'outil), la condition ne peut pas être « atteinte » et la règle ne s'applique pas, contre PRIN-12; elle n'est pas vérifiable en revue.
- Contre-exemple explicite : premier agent de facturation homologué avant la publication des seuils : rien n'empêche formellement un N3.
- Correctif proposé : ajouter à AUT-07 : « En l'absence de seuil approuvé pour un critère, ce critère est réputé atteint. » Ajouter à la phase 0 du ch. 15 (ou au catalogue initial) la publication de valeurs par défaut prudentes.

### [3.31] [MAJEUR - Lacune méthodologique/omission] Statut normatif de l'approbation « hors bande » incohérent
- Constats d'origine : 11-13, 12-10
- Localisation exacte : tableau 31, p. 108 : « Approbation humaine hors bande à chaque appel »; EXIG-AUT-14, p. 112 : « DEVRAIT passer par OpenID Connect CIBA »; tableau 46, p. 171 : « P3 toujours soumis à une approbation hors bande ».
- Diagnostic par premiers principes : vérifié. Le caractère hors bande du P3 est obligatoire aux tableaux 28, 31 et 46 (normatif par EXIG-CON-02), mais aucun bloc EXIG ne le pose en DOIT : AUT-09 et AUT-12 n'en parlent pas, AUT-14 est un DEVRAIT qui porte sur le moyen (CIBA). AUT-13 exclut par ailleurs « une confirmation locale dans l'interface de l'agent » pour toute approbation : la distinction « P2 : approbation signée; P3 : hors bande » (tableau 28, figure 14) ne désigne aucune différence opérable. « Hors bande » n'est pas au glossaire.
- Contre-exemple explicite : deux équipes mettent en œuvre l'approbation P3 dans une fenêtre du portail d'approbation ouverte depuis l'interface de l'agent; l'une se juge conforme (DEVRAIT écarté), l'autre en écart au tableau 31.
- Correctif proposé : appliquer l'arbitrage A8. Ajouter à AUT-09 : « [...] approbation humaine préalable, propre à cet appel, obtenue hors bande, c'est-à-dire sur un appareil et dans une session distincts de ceux de l'agent. » Laisser AUT-14 en DEVRAIT pour le moyen (CIBA). Ajouter « Hors bande » au glossaire et préciser au tableau 28 ce qui distingue l'approbation P2 (service d'approbation, même appareil admis) de l'approbation P3.

### [3.32] [MAJEUR - Lacune méthodologique/omission] N3 et N4 indiscernables pour la passerelle
- Constats d'origine : 11-14
- Localisation exacte : § 8.1, p. 103 : « Chaque niveau se définit donc par deux éléments observables : le rôle de la personne et l'étendue de ce que l'agent peut faire sans approbation »; tableau 28, N4 : « Comme N3; P3 toujours approuvé ».
- Diagnostic par premiers principes : vérifié p. 24, 103-104. N3 et N4 ont les mêmes paliers permis, donc la même « étendue sans approbation ». Ce qui les sépare (selon le § 3.3 : déclenchement sur événements, exécution continue et absence de la personne, en conjonction) n'est pas une propriété d'un appel d'outil; la passerelle ne peut pas « refuser ce qui excède » un plafond N3 (AUT-01). Le tableau 28 attribue « s'autodéclenche » au seul N4, alors que le § 3.3 admet des ambiants N1 à N3.
- Contre-exemple explicite : un agent modéré plafonné à N3, abonné à un flux, traite seul les billets 24 h sur 24 sous le seuil : N3 ambiant permis ou N4 non autorisé? Aucun contrôle ne tranche.
- Correctif proposé : reprendre au tableau 28 (colonne « Ce que fait l'agent », N4) la conjonction du § 3.3 et ajouter à AUT-01 : « Le niveau N4 se contrôle à l'émission de la délégation de longue durée (EXIG-AUT-18) et à l'abonnement aux événements, non à la passerelle d'outils : un agent sans délégation N4 inscrite ne peut pas s'abonner pour agir sans supervision en temps réel. » Corriger « deux éléments observables » en « deux éléments, observables appel par appel sauf pour N4 ».

### [3.33] [MAJEUR - Lacune méthodologique/omission] Capacité d'approbation : ni dimensionnement, ni issue au dépassement
- Constats d'origine : 11-15, 12-22
- Localisation exacte : EXIG-AUT-05, p. 106 : « Tant que la réévaluation n'est pas faite, l'agent DOIT fonctionner au niveau immédiatement inférieur »; EXIG-AUT-20, p. 115 : « La fréquence des demandes adressées à chaque approbateur DOIT être plafonnée ».
- Diagnostic par premiers principes : vérifié. Un plafond par approbateur sur un bassin fini donne une capacité finie; le texte ne dit pas ce que deviennent les demandes au-delà (file, refus, suspension AUT-11); l'expiration en refus n'est prévue que pour les ambiants (AUT-16). Un changement de version de modèle chez un fournisseur rétrograde en même temps tous les N3 qui l'utilisent (AUT-05); chaque P2 exige alors une approbation, sans liste d'approbateurs exigée pour cette combinaison (AUT-15) ni détection prescrite du changement de version. La priorisation par risque permet à un attaquant d'affamer les demandes légitimes (T10).
- Contre-exemple explicite : retrait d'un modèle un vendredi; 40 agents N3 passent à N2; des milliers de demandes arrivent; 10 approbateurs plafonnés à 30 par heure : déni de service ou approbations machinales.
- Correctif proposé : ajouter à AUT-20 : « Le bassin d'approbateurs est dimensionné au registre (volume prévu, y compris en niveau rétrogradé, avec marge); un plafond de demandes par agent et par tâche s'ajoute au plafond par approbateur; au-delà, la tâche est suspendue dans un état reprenable et l'agent émetteur suspendu au-delà d'un seuil (coupe-circuit ciblé). » Ajouter à AUT-05 : « la version de modèle servie est épinglée et vérifiée par la passerelle de modèles; à défaut de capacité d'approbation pour le niveau inférieur, l'agent est suspendu plutôt que rétrogradé ».

### [3.34] [MAJEUR - Lacune méthodologique/omission] Un outil P0 de recherche publique est un canal d'exfiltration non marqué
- Constats d'origine : 11-16
- Localisation exacte : tableau 31, p. 108, P0 : « Recherche documentaire publique [...] Identité de charge de travail, limitation de débit, journalisation de l'usage ».
- Diagnostic par premiers principes : vérifié p. 108 et 135. Le palier classe l'effet sur l'état, mais un outil de lecture publique transmet ses arguments à un tiers : c'est une communication externe au sens de la branche [C]. EXIG-SEC-06 retire « les outils d'envoi vers l'extérieur » et refuse les destinations hors liste d'autorisation après lecture de contenu non fiable, ce qui couvre une partie du risque; mais rien ne classe un moteur de recherche autorisé comme « outil d'envoi », et le tableau 31 ne prévoit aucun contrôle des arguments sortants (T4).
- Contre-exemple explicite : après une injection, l'agent appelle `recherche_publique{"q":"<numéro de dossier et RP du client>"}`, vers un moteur autorisé : exfiltration journalisée mais non bloquée.
- Correctif proposé : ajouter au tableau 31 et à AUT-08 un attribut de catalogue « sortie de données » (outil dont les arguments quittent l'entreprise), orthogonal au palier; un tel outil compte comme [C] dans SEC-04 et AUT-10 et comme « outil d'envoi vers l'extérieur » dans SEC-06; ajouter pour P0 et P1 externes un contrôle DLP des arguments.

### [3.35] [MAJEUR - Lacune méthodologique/omission] Plusieurs exigences renvoient à la « figure 15 » au lieu du contrôle calculé par AUT-10
- Constats d'origine : 12-01 (rétrogradé de BLOQUANT), 12-02, 12-08, 12-21
- Localisation exacte : EXIG-AUT-20, p. 115 : « Les actions que la figure 15 classe comme automatiques ne sont pas soumises à approbation. »; AUT-12 : « Toute approbation exigée par la figure 15 »; AUT-15 : « Chaque combinaison de classe et de palier soumise à approbation »; ATTENTION, p. 114; légende de la figure 16.
- Diagnostic par premiers principes : vérifié p. 109-115. AUT-10 retient le plus strict de la cellule, du niveau et des déclencheurs, et la légende de la figure 15 précise « plus strict, jamais plus souple ». AUT-20 exempte pourtant les cellules « Automatique » sans réserve, AUT-12 n'exige un jeton que pour les approbations « exigées par la figure 15 » (pas celles du niveau N2 ni des déclencheurs), AUT-15 n'exige de liste d'approbateurs que pour les cellules soumises à approbation, l'ATTENTION parle de ce que la figure « classe à faible risque » (la figure ne classe pas de risque), et la figure 16 limite le parcours au « P3 » alors que C.6 l'applique à un P2 au-delà du seuil. Rétrogradé : la légende de la figure 15, AUT-10 et le tableau 28 (N2 : « approbation signée ») permettent de résoudre la contradiction; elle reste exploitable à la lettre. Dérive inter-chapitres : EXIG-GOV-04 (p. 162) exige des approbateurs « pour chaque combinaison de classe de risque et de palier d'outil », plus largement qu'AUT-15.
- Contre-exemple explicite : agent faible N3, lecture P1 « Automatique » hors périmètre (déclencheur « comportement atypique ») : AUT-10 exige une approbation, AUT-20 dit qu'elle n'est pas soumise à approbation. Variante : agent modéré N2, P2 sous le seuil : approbation exigée par le niveau, mais ni jeton (AUT-12 à la lettre) ni liste d'approbateurs (AUT-15).
- Correctif proposé : appliquer l'arbitrage A6. Dans AUT-20, AUT-12 et AUT-15, remplacer « figure 15 » ou « combinaison [...] soumise à approbation » par « contrôle calculé selon l'EXIG-AUT-10 »; dans AUT-15, définir les listes par classe × palier × motif (cellule, niveau, déclencheur), en cohérence avec GOV-04. ATTENTION, p. 114 : « automatise ce dont le contrôle calculé (EXIG-AUT-10) est automatique ». Légende de la figure 16 et tableau 32 (« Réviser ») : « l'appel soumis à approbation selon l'EXIG-AUT-10 (P3, P2 au-delà du seuil, niveau N2 ou déclencheur) ».

### [3.36] [MAJEUR - Lacune méthodologique/omission] Approbateurs « inscrits et formés » : inapplicable à l'approbation par le mandant de sa propre action
- Constats d'origine : 12-13
- Localisation exacte : EXIG-AUT-15, p. 112 : « L'approbateur DOIT [...] posséder la compétence du domaine et l'autorité de refuser, et avoir été formé aux modes de défaillance des agents. »
- Diagnostic par premiers principes : vérifié p. 108-112. L'« envoi » est P3 (figure 15) et exige une approbation à chaque appel (AUT-09). Pour un assistant interactif, l'approbateur naturel est le mandant, qui devrait alors figurer à une liste du registre et être formé; rien n'est prévu pour les mandants externes (clients). Le cadre n'estime ni la population ni le coût.
- Contre-exemple explicite : assistant de courriel déployé à 10 000 employés : soit les 10 000 sont inscrits et formés, soit chaque envoi passe par un approbateur central qui sature (3.33).
- Correctif proposé : distinguer dans AUT-15 « l'approbation par le mandant de sa propre action sans effet sur autrui (authentification forte et écran fidèle selon AUT-19; inscription et formation non requises) » et « l'approbation par un tiers habilité (classe élevée, effet sur une personne autre que le mandant) », seule soumise à la liste et à la formation. Réexaminer au tableau 31 le classement de l'envoi interne (P2 compensable?).

### [3.37] [MAJEUR - Lacune méthodologique/omission] L'édition d'une action ne déclenche pas expressément le recalcul du contrôle
- Constats d'origine : 12-14
- Localisation exacte : § 8.6, p. 113 : « Éditer une action revient à approuver une autre action : la passerelle calcule l'empreinte des arguments modifiés, et c'est cette version que couvre le jeton. »
- Diagnostic par premiers principes : vérifié. Le texte ne recalcule que h. AUT-10 s'applique « pour chaque appel », mais rien ne dit que l'action éditée repasse comme nouvel appel avant l'émission du jeton; le seuil, l'indicateur de risque (AUT-19) et le nombre d'approbateurs peuvent changer. L'approbateur qui édite devient l'auteur de l'action qu'il approuve, ce qui contourne les quatre yeux quand le contrôle recalculé en exige deux.
- Contre-exemple explicite : bon de commande de 4 000 $, soumis à approbation par un déclencheur, porté à 9 000 $ par l'approbateur pendant l'édition; le jeton est émis pour le nouveau h sans réévaluation du seuil.
- Correctif proposé : ajouter après la phrase citée : « L'action éditée repasse par l'EXIG-AUT-10 avant l'émission du jeton, avec un nouvel indicateur de risque; si le contrôle recalculé exige plus d'un approbateur, l'éditeur ne peut pas être le seul. »

### [3.38] [MAJEUR - Lacune méthodologique/omission] Échantillonnage a posteriori à proportion fixe : coût non borné, puissance nulle à faible volume
- Constats d'origine : 12-23
- Localisation exacte : EXIG-AUT-21, p. 115 : « une revue humaine a posteriori DOIT porter sur un échantillon d'au moins 5 % des actions de classe modérée et 1 % de celles de classe faible ».
- Diagnostic par premiers principes : vérifié. L'unité « action » n'est pas définie (appel, tâche, écriture). Une proportion fixe impose une charge énorme à fort volume, qui concurrence les approbations (AUT-20), et un échantillon inutile à faible volume. La comparaison à la médiane ne détecte rien avec un ou deux approbateurs. Aucun objectif de détection ne fonde les pourcentages (« choix du cadre » non justifié).
- Contre-exemple explicite : 2 millions d'appels P2 par mois imposent 100 000 revues; 80 actions par mois en imposent une.
- Correctif proposé : réécrire la seconde phrase d'AUT-21 : « [...] une revue humaine a posteriori DOIT porter sur un échantillon d'actions à effet, stratifié par risque, avec un minimum et un plafond absolus, dimensionné pour détecter un taux d'anomalie cible avec une confiance fixée par le comité (valeurs par défaut : 5 % et 1 %, sous ces bornes). » Ajouter : « la comparaison à la médiane exige au moins trois approbateurs, ou une référence entre cas d'usage ».

### [3.39] [MAJEUR - Lacune méthodologique/omission] « Exclusivement automatisée » jugé par une mesure mensuelle, alors que l'avis est dû au moment de la décision
- Constats d'origine : 12-24
- Localisation exacte : EXIG-AUT-23, p. 116 : « et exerce une influence réelle mesurée par l'EXIG-AUT-21 ».
- Diagnostic par premiers principes : vérifié. AUT-21 produit des indicateurs mensuels agrégés; l'avis de l'art. 12.1 est dû « au plus tard au moment de la communication de la décision » (AUT-22). Au moment de décider, la qualification est indécidable; le premier mois (aucune mesure) n'est pas couvert. « Compétence voulue » et « temps nécessaire » n'ont pas de mesure (§ 1.5 : exigence vérifiable).
- Contre-exemple explicite : nouveau cas d'usage N2 au mois 1 : faut-il l'avis? Si la mesure du mois 2 révèle une approbation machinale, les décisions du mois 1 étaient exclusivement automatisées et sans avis, motif de sanction (art. 90.1).
- Correctif proposé : réécrire la fin d'AUT-23 : « La qualification est faite a priori par cas d'usage dans l'EFVP; la décision est réputée exclusivement automatisée tant que la preuve contraire n'y est pas consignée (temps minimal d'examen et accès aux données sources journalisés). Les indicateurs de l'EXIG-AUT-21 servent de contrôle a posteriori et déclenchent la requalification et, au besoin, les avis dus. »

### [3.40] [MAJEUR - Lacune méthodologique/omission] AUT-22/23 et CON-07/08/09 : même obligation légale, deux contenus normatifs
- Constats d'origine : 12-25
- Localisation exacte : EXIG-AUT-22, p. 116 (avis, explication, rectification, canal, conservation); EXIG-CON-07, p. 176 : « avec leur importance relative [...] un membre du personnel nommément désigné [...] au plus 30 jours ».
- Diagnostic par premiers principes : vérifié p. 116 et 176-177. CON-07 ajoute l'importance relative des facteurs, un membre du personnel nommément désigné et un délai de 30 jours, absents d'AUT-22; AUT-23 pose cinq conditions, CON-08 trois. Pas de contradiction stricte, mais un lecteur du chapitre 8 omet trois obligations du chapitre 12, sur une obligation sanctionnée. Dérive inter-chapitres ch. 8 / ch. 12.
- Contre-exemple explicite : une équipe applique AUT-22 à la lettre : canal générique, sans personne désignée ni délai : non conforme à CON-07.
- Correctif proposé : appliquer l'arbitrage A9. Réduire AUT-22 à : « Tout agent [...] DOIT être de classe élevée et satisfaire aux EXIG-CON-07 à EXIG-CON-09. » Aligner les conditions d'AUT-23 et de CON-08 (une seule liste, dans CON-08, à laquelle AUT-23 renvoie).

### [3.41] [MAJEUR - Lacune méthodologique/omission] Décision par appel selon l'état de la tâche : course entre répliques de passerelle
- Constats d'origine : 12-28
- Localisation exacte : EXIG-IAM-02, p. 119 : décision « rendue d'après l'identité de l'agent, le mandant, le palier de l'outil, le niveau d'autonomie, l'état de la tâche et les signaux de risque ».
- Diagnostic par premiers principes : vérifié (aucune clause de cohérence). La garantie suppose que le marquage « contenu non fiable lu » et le budget consommé soient visibles de toute instance qui décide de l'appel suivant, y compris pour des appels parallèles émis par le modèle. Ni le lieu de cet état, ni sa cohérence, ni le refus s'il est indisponible ne sont fixés (T4). Même racine que le registre des jti de 3.04.
- Contre-exemple explicite : la lecture d'un courriel externe traverse la réplique A, dont le marquage met 200 ms à se propager; l'appel d'envoi suivant arrive à la réplique B, qui voit une tâche « propre ».
- Correctif proposé : appliquer l'arbitrage A7. Ajouter à IAM-02 : « L'état de la tâche pris en compte est tenu dans un magasin à cohérence forte par tâche (lecture de sa propre écriture), ou les appels d'une même tâche sont acheminés vers la même instance; état indisponible ou périmé : refus (EXIG-IAM-18). »

### Mineurs — orchestration, état et saga (§ 7.3-7.10)

### [3.42] [MINEUR - Dérive de notation/clarté] Clés et empreintes construites par concaténation ambiguë
- Constats d'origine : 10-25, 11-22, 12-06
- Localisation exacte : § 7.6, p. 97 : « cle = hex( SHA-256( task_id + "|" + step_id ) ) » et « task_id = "tache-7f3c2a" »; § 8.5, p. 111 : « h = SHA-256(identifiant de l'outil ‖ arguments canonisés) ».
- Diagnostic : la concaténation avec « | » n'est pas injective si un identifiant contient « | »; ‖ sans séparateur ni grammaire d'identifiant fixée, sans étiquette de domaine (risque faible : les arguments commencent par `{`). Le task_id de l'exemple a 24 bits d'entropie, alors que le brouillon met en garde contre les clés à faible entropie; une clé prévisible permet de préempter une clé si le service ne cloisonne pas par client. Le cadre emploie la RFC 8785 ailleurs (OBS-12), pas ici.
- Correctif proposé : § 7.6 : « cle = hex(SHA-256(JCS(["idem-v1", task_id, step_id]))), task_id aléatoire d'au moins 122 bits (UUIDv4) »; exiger le cloisonnement des clés par client à ORC-22. § 8.5 et AUT-12 : « h = SHA-256(JCS({"v":1,"outil":<identifiant>,"arguments":<arguments>})) »; mettre à jour C.6 (lecture et valeur de h).

### [3.43] [MINEUR - Dérive de notation/clarté] « Logique de coordination déterministe » non définie
- Constats d'origine : 10-26
- Localisation exacte : EXIG-ORC-12, p. 94 : « La logique de coordination DOIT rester déterministe ».
- Diagnostic : dans les patrons agent unique et orchestrateur-exécutants, le modèle choisit l'étape suivante; lu à la lettre, ORC-12 interdit des patrons autorisés au § 7.2.
- Correctif proposé : « La logique de coordination DOIT rester déterministe une fois relus les résultats journalisés des appels non déterministes ».

### [3.44] [MINEUR - Dérive de notation/clarté] Magasin en mémoire : périmètre d'interdiction et contrainte LangGraph
- Constats d'origine : 10-27, 12-17
- Localisation exacte : EXIG-ORC-11, p. 94 : « Un magasin en mémoire NE DOIT PAS être utilisé hors du poste de développement. »; p. 113 : « interrupt() exige un mécanisme de points de contrôle persistant ».
- Diagnostic : la première formule interdit l'intégration continue et les doublures d'ORC-20, usages sans risque; la seconde présente comme contrainte de l'API ce qui est une exigence de production (interrupt() exige un checkpointer, qui peut être InMemorySaver, à vérifier [82]; le § 7.4 dit d'ailleurs qu'InMemorySaver « sert à l'expérimentation »).
- Correctif proposé : ORC-11 : « NE DOIT PAS être utilisé en production ni dans un environnement qui traite des données réelles ». P. 113 : « interrupt() exige un mécanisme de points de contrôle (checkpointer), qui doit être persistant en production ».

### [3.45] [MINEUR - Dérive de notation/clarté] ORC-13 : attribution brouillée et états modifiés à dessein
- Constats d'origine : 10-28
- Localisation exacte : EXIG-ORC-13, p. 94 : « (constat du cadre, non tiré de la source)[105] »; « NE DOIT PAS charger de point de contrôle d'origine non vérifiée ».
- Diagnostic : l'appel [105] porte sur une phrase déclarée non sourcée; le voyage dans le temps (« bifurquer après correction de l'état », p. 94) produit un état d'origine humaine dont le statut « vérifié » n'est pas défini.
- Correctif proposé : séparer la phrase sourcée [105] de la phrase du cadre; ajouter : « toute modification manuelle de l'état est re-signée par le service d'orchestration et journalisée en audit ».

### [3.46] [MINEUR - Dérive de notation/clarté] Temporal « sans limite de durée » : limites d'historique et de charge utile tues
- Constats d'origine : 10-29
- Localisation exacte : § 7.4, p. 93 : « Temporal garantit qu'une exécution de flux se poursuit jusqu'à son terme, sans limite de durée imposée »; tableau 27, p. 102.
- Diagnostic : à vérifier (documentation Temporal, « Limits ») : historique d'événements et charge utile bornés; les invocations d'agent journalisées comme activités y stockent invites et réponses.
- Correctif proposé : ajouter aux « Points d'attention » de Temporal : « historique et charge utile bornés : Continue-As-New et passage par référence (magasin d'artefacts, EXIG-ORC-24) pour les résultats volumineux ».

### [3.47] [MINEUR - Dérive de notation/clarté] ORC-16 « avant chaque étape » vise aussi les lectures
- Constats d'origine : 10-30
- Localisation exacte : EXIG-ORC-16, p. 96 : « Avant chaque étape, l'orchestrateur DOIT consigner [...] la compensation à exécuter. »
- Diagnostic : une lecture P0-P1 n'a ni clé (ORC-21) ni compensation.
- Correctif proposé : « Avant chaque étape d'écriture (P2 ou P3) ».

### [3.48] [MINEUR - Dérive de notation/clarté] ORC-18 : unité de décompte de « deux échecs » ambiguë
- Constats d'origine : 10-31
- Localisation exacte : EXIG-ORC-18, p. 96 : « Lorsqu'une même compensation échoue deux fois de suite (erreur non transitoire ou politique de réessai épuisée) ».
- Diagnostic : tentative ou épuisement d'une politique? Relancer une erreur non transitoire est inutile (règle 5, Temporal).
- Correctif proposé : « Lorsqu'une compensation subit une erreur non transitoire, ou épuise deux fois de suite la politique de réessai déclarée ».

### [3.49] [MINEUR - Dérive de notation/clarté] ORC-09 : décompte, « chevauchement » et critère de décision indéfinis
- Constats d'origine : 10-32
- Localisation exacte : EXIG-ORC-09, p. 93 : « Dès qu'un agent dépasse 15 outils [...], ou dès que des outils se chevauchent ».
- Diagnostic : outils au catalogue de l'agent ou chargés au début du tour? « Se chevauchent » rend l'exigence universelle; aucun seuil de précision ne dit quand scinder.
- Correctif proposé : compter « les outils disponibles au début d'un tour »; définir le chevauchement par la confusion mesurée sur le jeu d'évaluation; exiger un seuil de précision déclaré à la fiche.

### [3.50] [MINEUR - Dérive de notation/clarté] Le champ « echeance » contient une durée
- Constats d'origine : 10-33
- Localisation exacte : § 7.7, p. 98 : « "echeance": "PT10M" ».
- Diagnostic : une échéance est un instant; une durée relative s'allonge à chaque file d'attente.
- Correctif proposé : « "echeance": "2026-10-27T14:13:12Z" » (instant absolu UTC).

### [3.51] [MINEUR - Dérive de notation/clarté] ORC-25 : filtrage « selon les droits du mandant » non testable pour les contenus dérivés
- Constats d'origine : 10-34
- Localisation exacte : EXIG-ORC-25, p. 99 : « Chaque agent DOIT filtrer ses résultats selon les droits du mandant ».
- Diagnostic : vérifiable pour des enregistrements, non pour une synthèse; le risque réel vient des agents qui lisent sous leurs propres droits (agent de sanctions, p. 92).
- Correctif proposé : rattacher les lectures à l'intersection des droits (§ 9.3) et exiger, pour un agent à frontière de sécurité distincte, un schéma de retour à champs déclassifiés.

### [3.52] [MINEUR - Dérive de notation/clarté] ORC-27 : disjoncteur obligatoire non signalé comme choix du cadre
- Constats d'origine : 10-35
- Localisation exacte : EXIG-ORC-27, Pourquoi, p. 100 : « recommande d'envisager des disjoncteurs; la temporisation exponentielle et la limitation aux erreurs transitoires sont des choix du cadre ».
- Diagnostic : passer d'« envisager » à DOIT est aussi un choix du cadre, contre la règle de distinction du § 1.4.
- Correctif proposé : ajouter « ; le disjoncteur obligatoire est un choix du cadre (PRIN-12) ».

### [3.53] [MINEUR - Dérive de notation/clarté] File humaine « recevant le contexte complet » contre minimisation
- Constats d'origine : 10-36
- Localisation exacte : EXIG-ORC-27, p. 100 : « file humaine nommée recevant le contexte complet ».
- Diagnostic : ORC-23 justifie le contexte minimal par l'exposition des données; la Loi 25 impose la minimisation.
- Correctif proposé : « file humaine nommée recevant le contexte nécessaire à la reprise, sous les droits du mandant ».

### [3.54] [MINEUR - Dérive de notation/clarté] ORC-28 : délai mesuré sans cible; périmètre de l'exercice non précisé
- Constats d'origine : 10-37
- Localisation exacte : EXIG-ORC-28, p. 100 : « Un exercice d'arrêt DOIT avoir lieu au moins une fois par trimestre et son délai mesuré DOIT être consigné. »
- Diagnostic : IAM-20 (p. 129) fixe un « délai maximal de bout en bout [...] fixé par l'entreprise »; ORC-28 ne s'y réfère pas et ne dit pas si le coupe-circuit global s'exerce en production.
- Correctif proposé : « [...] consigné et comparé au délai maximal d'EXIG-IAM-20; l'arrêt ciblé s'exerce en production, l'arrêt global dans un environnement représentatif ».

### [3.55] [MINEUR - Dérive de notation/clarté] Force normative d'ORC-10 incohérente (DEVRAIT rendu obligatoire, Pourquoi contraire à ORC-23)
- Constats d'origine : 10-22 (rétrogradé de MAJEUR), 10-38
- Localisation exacte : EXIG-ORC-10 · DEVRAIT, p. 93; tableau 26, p. 100 : « Découpage par frontières de contexte (EXIG-ORC-10) »; EXIG-ORC-29 : « NE DOIT PAS présenter l'un des anti-patrons du tableau 26 ».
- Diagnostic : l'anti-patron du tableau 26 rend ORC-10 obligatoire sans dérogation formelle; la nuance « une tâche à fortes dépendances reste à un seul agent » (p. 98) n'est dans aucune exigence. Rétrogradé : ORC-23 admet l'historique brut « sauf exception justifiée à la fiche », ce qui ouvre déjà une voie.
- Correctif proposé : promouvoir ORC-10 en DOIT pour les tâches d'écriture : « une tâche d'écriture à fortes dépendances DOIT rester à un seul agent »; admettre dans ORC-23 « un registre structuré des décisions prises » parmi les éléments transmis; mettre à jour l'annexe D.

### [3.56] [MINEUR - Dérive de notation/clarté] Le tableau 26 cite des éléments absents d'ORC-05
- Constats d'origine : 10-39
- Localisation exacte : tableau 26, p. 101 : « Critères concrets, tests négatifs, suite complète (EXIG-ORC-05) ».
- Diagnostic : vérifié p. 90 : ORC-05 n'exige ni tests négatifs ni suite complète; le tableau, rendu normatif par ORC-29, crée une obligation hors bloc EXIG.
- Correctif proposé : ajouter à ORC-05 « des critères qui incluent des tests négatifs et l'exécution de la suite complète », ou ramener la cellule à « Critères vérifiables et évaluateur distinct (EXIG-ORC-05) ».

### [3.57] [MINEUR - Dérive de notation/clarté] MAST : intitulé de la troisième catégorie abrégé
- Constats d'origine : 10-41
- Localisation exacte : § 7.9, p. 100 : « conception du système, désalignement entre agents et vérification des tâches ».
- Diagnostic : à vérifier [292] : la catégorie s'intitulerait « Task Verification and Termination », ce qui couvre l'anti-patron « victoire prématurée ».
- Correctif proposé : « vérification et terminaison des tâches », sous réserve de l'audit bibliographique.

### [3.58] [MINEUR - Dérive de notation/clarté] ORC-14 : version ancienne maintenue sans borne, même vulnérable
- Constats d'origine : 10-18 (rétrogradé de MAJEUR)
- Localisation exacte : EXIG-ORC-14, p. 94 : « DEVRAIT laisser chaque exécution en cours se terminer sur la version avec laquelle elle a commencé ».
- Diagnostic : ni durée maximale de cohabitation, ni exception de sécurité, ni lien avec le retrait (§ 11.5). Rétrogradé : ORC-14 n'est qu'un DEVRAIT, l'écart de sécurité reste permis, mais il n'est pas prescrit.
- Correctif proposé : ajouter : « La cohabitation est bornée par le plafond de durée d'EXIG-ORC-26; le retrait d'une version pour motif de sécurité DOIT suspendre ou migrer (migration testée) les exécutions en cours. »

### Mineurs — autonomie, paliers, combinaison (§ 8.1-8.4)

### [3.59] [MINEUR - Dérive de notation/clarté] Tableau 30 et règle d'or : redondance et vocabulaire
- Constats d'origine : 11-11 (rétrogradé de MAJEUR)
- Localisation exacte : tableau 30, p. 107 : « Une détection lente impose un contrôle avant l'action (N2) plutôt qu'après. »; EXIG-AUT-07, p. 108 : « (rayon élevé, réversibilité faible, détection lente) ».
- Diagnostic : le tableau 30 (normatif par AUT-02) plafonne à N2 sur le seul critère de détection; AUT-07 exige la conjonction des trois. Rétrogradé : AUT-07 n'autorise rien, il interdit; les deux règles s'appliquent et donnent N2, mais AUT-07 devient redondante et le lecteur croit à deux fonctions de décision. « Rayon large » (tableau 30) contre « rayon élevé » (AUT-07).
- Correctif proposé : expliciter au tableau 30 la valeur plafonnante de chaque critère et présenter AUT-07 comme le cas extrême (« même avec d'excellents résultats aux essais »); unifier en « rayon élevé ».

### [3.60] [MINEUR - Dérive de notation/clarté] Classement : capacité P3 sous le seuil et capacité soumise à approbation
- Constats d'origine : 11-17 (rétrogradé de MAJEUR, écarté en partie), 11-18
- Localisation exacte : tableau 46, p. 171, Faible : « Données publiques ou internes non confidentielles; lecture seule ou actions internes réversibles »; EXIG-AUT-06 : « fondée sur les permissions effectives ».
- Diagnostic : la règle « un seul suffit » n'a pas de sens pour la classe la plus basse : un agent qui ne traite que des données publiques mais dispose d'un outil P3 irréversible sous le seuil remplit un critère « faible » et aucun critère supérieur; il tombe en classe faible malgré une capacité irréversible. Le cadre ne dit pas non plus si une capacité accessible seulement après approbation (exemple p. 109 : 40 factures) compte dans le classement.
- Correctif proposé : au tableau 46, faire de la classe faible la classe par défaut (« aucun critère des classes supérieures ») et ajouter à la classe modérée « toute capacité P3, quel que soit le seuil »; préciser dans AUT-06 que les actions possibles après approbation hors bande comptent dans le classement.

### [3.61] [MINEUR - Dérive de notation/clarté] Figure 14 et tableau 28 divergent sur les contrôles et les paliers
- Constats d'origine : 11-19
- Localisation exacte : figure 14, p. 103 : N1 « accès circonscrit, DLP, essais d'exactitude »; N4 « évaluation continue, retour arrière rapide »; N2 « P2 et P3 après approbation signée »; tableau 28, p. 104 : « retour arrière rapide » en N3, pas de DLP en N1, « (P3 : hors bande) » en N2.
- Diagnostic : les contrôles étant cumulatifs, l'écart change ce qu'on exige d'un N1 et d'un N3; la figure omet le hors bande du N2.
- Correctif proposé : aligner la figure sur le tableau (retour arrière rapide en N3, DLP ajoutée au tableau en N1 ou retirée de la figure, « P3 hors bande » en N2) et écrire sous la figure « le tableau 28 fait foi ».

### [3.62] [MINEUR - Dérive de notation/clarté] Cellules de la figure 15 imprécises ou en retrait du tableau 31
- Constats d'origine : 11-20
- Localisation exacte : figure 15, p. 109 : Faible × P1 « Automatique / jeton délégué, masquage »; Modéré × P1 « Automatique + audit »; Élevé × P1 « Audit + revue »; Faible × P2 « Autonome sous seuil » contre Modéré × P2 « Approbation au-delà du seuil métier déclaré ».
- Diagnostic : le tableau 31 rend l'audit et le contrôle par ligne obligatoires pour tout P1, que la cellule faible semble omettre et que « + audit » présente comme un supplément; les deux cellules P2 disent la même chose autrement; la « revue » de Élevé × P1 n'est pas située (avant ou après).
- Correctif proposé : en-tête de grille « en plus des contrôles du palier (tableau 31) »; harmoniser les cellules P2 faible et modérée; « revue a posteriori par échantillonnage » pour Élevé × P1.

### [3.63] [MINEUR - Dérive de notation/clarté] N0 présenté comme niveau d'un agent
- Constats d'origine : 11-26
- Localisation exacte : EXIG-AUT-01, p. 105 : « Chaque agent DOIT avoir un niveau d'autonomie N0 à N4 »; AUT-05 : « ramené à un flux déterministe sans autonomie (N0) ».
- Diagnostic : N0 est « aucun modèle » (tableau 28) : ce n'est pas un agent au sens du § 3.2; « ramener à N0 » suppose qu'un flux de repli existe.
- Correctif proposé : AUT-01 : « niveau N1 à N4 (N0 désigne le flux déterministe) »; AUT-05 : « est suspendu, ou remplacé par le flux déterministe de repli s'il existe ».

### [3.64] [MINEUR - Dérive de notation/clarté] Déclencheurs de réévaluation : AUT-05 et CON-03 divergent
- Constats d'origine : 11-27
- Localisation exacte : EXIG-AUT-05, p. 106 : « changement de modèle [...], d'invite système [...], d'outil en écriture, de population visée ou d'ODD »; EXIG-CON-03, p. 172 : « de catégorie de données, de finalité, [...] ou de lieu de traitement ».
- Diagnostic : vérifié. Un changement de finalité ou de catégorie de données peut faire passer la classe à élevée (plafond N2) sans déclencher AUT-05; les deux exigences appliquent en outre deux logiques (blocage avant production contre fonctionnement rétrogradé). Dérive ch. 8 / ch. 12.
- Correctif proposé : ajouter à AUT-05 « ou de tout changement visé par l'EXIG-CON-03 », et à CON-03 « ou de tout changement visé par l'EXIG-AUT-05 ».

### [3.65] [MINEUR - Dérive de notation/clarté] Tableau 29 : statut contradictoire des correspondances avec Feng et al.
- Constats d'origine : 11-28
- Localisation exacte : p. 106 : « Les correspondances avec Gartner, AWS et Feng et al. reposent sur les sources citées »; note du tableau : « celles avec Feng et al., Morris et al. et SAE J3016 sont indicatives ».
- Diagnostic : vérifié; « L4 Approbateur » associé à N3 se lit mal à côté de N2 (la personne « approuve chaque écriture »).
- Correctif proposé : trancher (indicatives) dans les deux phrases; ajouter que l'« approbateur » de Feng n'intervient que sur exception.

### [3.66] [MINEUR - Dérive de notation/clarté] Analogie SAE J3016 : lieu du repli contradictoire; N3 relève du niveau 4 de SAE
- Constats d'origine : 11-29
- Localisation exacte : AUT-04, Pourquoi, p. 105 : « par la partie qui assure le repli hors du domaine »; p. 107 : « le système assure lui-même le repli dans son domaine »; tableau 29 : N3 ↔ « Niveau 3 : l'humain reprend la main ».
- Diagnostic : vérifié; AUT-04 impose aux N3 un repli assuré par le système, ce qui correspond au niveau 4 de SAE. La révision « J3016_202609 » (p. 106) est à vérifier (la dernière connue des réviseurs est J3016_202104).
- Correctif proposé : écrire « la partie qui assure le repli à la sortie du domaine » aux deux endroits; au tableau 29, N3 ↔ « Niveau 4 (repli par le système), par analogie »; confirmer la révision de J3016.

### [3.67] [MINEUR - Dérive de notation/clarté] ASI09 cité à contresens dans EXIG-AUT-09
- Constats d'origine : 11-30
- Localisation exacte : EXIG-AUT-09, Pourquoi, p. 109 : « l'OWASP range l'absence de confirmation des actions sensibles parmi les vulnérabilités (ASI09) »; p. 114 : ASI09 « vise la surconfiance ».
- Diagnostic : incohérence interne vérifiée; contenu d'OWASP à vérifier [28].
- Correctif proposé : « l'OWASP recommande l'approbation explicite des actions à fort impact (ASI02) ».

### [3.68] [MINEUR - Dérive de notation/clarté] Références en double ou secondaires
- Constats d'origine : 11-31
- Localisation exacte : p. 112 : WIMSE AIMS cité [309] (AUT-13) puis [93, 311] (AUT-14); p. 107 : Gartner [305] (ITPro) au lieu de [95]; RIA art. 14 et 26 cités par [290] et [94] (Future of Life Institute).
- Diagnostic : vérifié : deux entrées de bibliographie pour draft-ietf-wimse-aims-00, avec deux URL; préférence d'une source B à la source A disponible (annexe F, T8).
- Correctif proposé : fusionner [93] et [309]; citer [95] dans AUT-06; citer le texte du RIA (EUR-Lex ou [412]) pour les articles 14 et 26.

### [3.69] [MINEUR - Dérive de notation/clarté] Une prévision d'analyste présentée comme « constat »
- Constats d'origine : 11-32
- Localisation exacte : § 8.1, p. 103 : « Deux constats la fondent. [...] la firme prévoit que, d'ici 2027, 40 % des entreprises rétrograderont ou désactiveront des agents autonomes ».
- Diagnostic : vérifié; un communiqué de prévision sans méthode publiée n'est pas un constat.
- Correctif proposé : « Deux arguments la fondent »; « selon une prévision de Gartner (communiqué, méthode non publiée) ».

### Mineurs — approbation, agents ambiants, approbation machinale (§ 8.5-8.8)

### [3.70] [MINEUR - Dérive de notation/clarté] Clause « au moins un autre que le mandant » tautologique
- Constats d'origine : 11-21, 12-12
- Localisation exacte : EXIG-AUT-15, p. 112 : « deux approbateurs distincts DOIVENT approuver, dont au moins un autre que le mandant ».
- Diagnostic : deux personnes distinctes ne peuvent pas être toutes deux le mandant; l'indépendance voulue n'est pas exprimée (mandant et subordonné direct satisfont la règle).
- Correctif proposé : « dont au moins un indépendant du mandant, de sa ligne hiérarchique et du parrain de l'agent ».

### [3.71] [MINEUR - Dérive de notation/clarté] Authentification « au moins deux facteurs » faible contre la fatigue d'approbation
- Constats d'origine : 11-24
- Localisation exacte : EXIG-AUT-15, p. 112 : « authentification forte (au moins deux facteurs) ».
- Diagnostic : admet l'OTP par SMS et la notification poussée sans appariement, vecteurs de T10, sur la dernière barrière P3.
- Correctif proposé : ajouter « résistante à l'hameçonnage (FIDO2/WebAuthn) pour les approbations P3 ».

### [3.72] [MINEUR - Dérive de notation/clarté] binding_message : « affiché sur les deux appareils » et rôle surestimé
- Constats d'origine : 11-25, 12-09
- Localisation exacte : EXIG-AUT-14, p. 112 : « ou celle que requiert un agent sans interface [...] un binding_message court, affiché sur les deux appareils, rattache la demande à l'action ».
- Diagnostic : un agent sans interface n'a pas d'appareil d'affichage; le binding_message de CIBA apparie des appareils, il ne lie pas cryptographiquement l'action (rôle de h). Sémantique CIBA à vérifier [310].
- Correctif proposé : « un binding_message court, dérivé de h ou de la tâche, affiché à l'approbateur et consigné dans la demande et dans le jeton, aide à reconnaître la demande; le lien à l'action repose sur h ».

### [3.73] [MINEUR - Dérive de notation/clarté] Patrons « Notifier » et « Questionner » et champs obligatoires d'AUT-16
- Constats d'origine : 12-15
- Localisation exacte : EXIG-AUT-16, p. 113 : « Chaque demande DOIT indiquer le patron, la tâche, l'agent, l'effet attendu et une échéance »; tableau 32, Notifier : « Signale sans agir. »
- Diagnostic : une notification n'a pas d'effet attendu; l'issue de l'expiration n'est pas définie pour Notifier et Questionner.
- Correctif proposé : « l'effet attendu (patron Réviser) »; ajouter : « À l'échéance, une notification est escaladée si sa politique l'exige; une question sans réponse suspend la tâche puis l'escalade ».

### [3.74] [MINEUR - Dérive de notation/clarté] « Délégation » désigne un mandat de 12 mois et un jeton de 15 minutes
- Constats d'origine : 12-19
- Localisation exacte : EXIG-AUT-18, p. 114 : « La délégation qui permet à un agent ambiant de niveau N3 ou N4 d'agir DOIT expirer à une échéance inscrite à sa fiche ».
- Diagnostic : vérifié p. 114 et 125 (IAM-15 : « délégation de longue durée »); au § 9.3, la délégation est l'échange RFC 8693 à jetons de 15 minutes.
- Correctif proposé : introduire « mandat d'agent ambiant » dans AUT-18, IAM-15 et le glossaire; réserver « délégation » à l'échange de jetons.

### [3.75] [MINEUR - Dérive de notation/clarté] Portée ambiguë d'AUT-22, plus large que le tableau 46
- Constats d'origine : 12-26
- Localisation exacte : EXIG-AUT-22, p. 116 : « Tout agent qui rend une décision concernant une personne, ou la prépare sans révision humaine significative, à partir d'un traitement automatisé de ses RP ».
- Diagnostic : « sans révision humaine significative » qualifie-t-il « rend » ou seulement « prépare »? Dans la seconde lecture, toute décision rendue, même révisée, exige l'avis, au-delà du tableau 46 (« fondée exclusivement »).
- Correctif proposé : « Tout agent dont les décisions concernant une personne sont fondées exclusivement, au sens de l'EXIG-AUT-23, sur un traitement automatisé de ses RP [...] » (cohérent avec 3.40).

### Mineurs — confiance zéro et identité (§ 9.1-9.2)

### [3.76] [MINEUR - Dérive de notation/clarté] EXIG-IAM-02 omet les appels aux modèles
- Constats d'origine : 12-27
- Localisation exacte : EXIG-IAM-02, p. 119 : « Chaque appel d'un agent vers un outil, une ressource ou un autre agent DOIT être authentifié et autorisé individuellement. »
- Diagnostic : le tableau 33 fait de la passerelle de modèles un PEP; l'envoi de RP sensibles à un modèle externe échappe à la décision par appel.
- Correctif proposé : « vers un outil, une ressource, un modèle ou un autre agent ».

### [3.77] [MINEUR - Dérive de notation/clarté] L'exemple d'IAM-02 n'illustre pas l'apport de la décision par appel
- Constats d'origine : 12-29
- Localisation exacte : EXEMPLE, p. 119 : « il tente d'appeler l'outil d'envoi de courriels [...] Une autorisation accordée à l'ouverture de la session l'aurait laissé passer. »
- Diagnostic : vérifié; l'envoi est P3 et exige une approbation à chaque appel (AUT-09), quel que soit l'état de la session.
- Correctif proposé : prendre un outil P2 interne (écriture dans un dossier client), autorisé seul sous le seuil, qui ne bascule en approbation qu'à cause du contenu non fiable (SEC-04).

### [3.78] [MINEUR - Dérive de notation/clarté] IAM-01 : « toute communication » contre stdio local; force implicite
- Constats d'origine : 12-30
- Localisation exacte : EXIG-IAM-01 · NE DOIT PAS, p. 119 : « Toute communication entre composants est mutuellement authentifiée et chiffrée, y compris à l'intérieur d'un réseau privé. »
- Diagnostic : vérifié; EXIG-MCP-08 (p. 53-54) admet stdio sur le poste d'un développeur; phrase à l'indicatif dans un bloc NE DOIT PAS.
- Correctif proposé : « Toute communication réseau entre composants DOIT être mutuellement authentifiée et chiffrée (mTLS), y compris à l'intérieur d'un réseau privé; le transport stdio local relève de l'EXIG-MCP-08. »

### [3.79] [MINEUR - Dérive de notation/clarté] « Renouvelé automatiquement » ne convient pas au JWT-SVID
- Constats d'origine : 12-31
- Localisation exacte : EXIG-IAM-04, p. 120 : « de courte durée, renouvelé automatiquement et valide au plus pour la vie de l'instance »; p. 119 : « le JWT-SVID [...] est redemandé au besoin ».
- Diagnostic : vérifié; le texte distingue lui-même les deux modes puis exige le premier des deux options.
- Correctif proposé : « renouvelé automatiquement ou réémis à la demande par la plateforme ».

### [3.80] [MINEUR - Dérive de notation/clarté] Le gabarit Entra Agent ID n'est pas confronté aux IAM-03 à 05
- Constats d'origine : 12-32
- Localisation exacte : p. 120 : « un gabarit (agent identity blueprint) qui porte les justificatifs et les politiques d'accès conditionnel héritées par toutes ses identités ».
- Diagnostic : justificatifs partagés par toutes les identités (NHI9), possiblement un secret client de longue durée (IAM-05); « vie de l'instance » sans équivalent évident en SaaS. À vérifier [90].
- Correctif proposé : ajouter : « Le gabarit DOIT reposer sur un justificatif fédéré ou une identité gérée, sans secret client (EXIG-IAM-05); le profil de plateforme au catalogue définit l'instance au sens d'EXIG-IAM-04. »

### [3.81] [MINEUR - Dérive de notation/clarté] Agents orphelins : IAM-07 et GOV-13 divergent
- Constats d'origine : 12-33
- Localisation exacte : EXIG-IAM-07, p. 121 : « Une revue trimestrielle détecte les agents orphelins [...], qui sont désactivés »; EXIG-GOV-13 : « désactiver ceux qui ne sont pas régularisés ».
- Diagnostic : vérifié; désactivation immédiate contre délai de régularisation; objet de l'attestation différent (« encore requis » contre finalité, mandants, portées, classe, niveau). Dérive ch. 9 / ch. 11.
- Correctif proposé : dans IAM-07, remplacer les deux dernières phrases par « La revue périodique et l'attestation suivent l'EXIG-GOV-13; la désactivation qui en résulte révoque l'identité et les justificatifs selon la présente exigence. »

### [3.82] [MINEUR - Dérive de notation/clarté] NHI3 rattaché à IAM-17 : correspondance faible
- Constats d'origine : 12-34
- Localisation exacte : tableau 34, p. 121 : NHI3 → « EXIG-IAM-17; chaîne d'approvisionnement (section 9.8); clauses (section 13.3) ».
- Diagnostic : NHI3 vise les identités non humaines détenues par des tiers (octrois OAuth entrants); IAM-17 ne régit que les appels sortants des agents (portée de NHI3 déduite par le réviseur).
- Correctif proposé : rattacher NHI3 à une exigence d'inventaire et de revue des octrois accordés à des tiers (§ 9.8 ou § 13.3), ou le déclarer « partiellement couvert ».

### Récapitulatif des dérives inter-chapitres de la tranche
- Arguments en clair (ORC-16) contre empreintes seules (OBS-12) : 3.20.
- AUT-11 contre IAM-18 (dernière politique distribuée) : 3.29.
- AUT-14 (DEVRAIT) contre tableaux 28, 31 et 46 (hors bande obligatoire) : 3.31.
- AUT-15 (combinaisons soumises à approbation) contre GOV-04 (toutes les combinaisons) : 3.35.
- AUT-22/23 contre CON-07/08/09 : 3.40. AUT-05 contre CON-03 : 3.64. IAM-07 contre GOV-13 : 3.81.
- Unité du seuil : « 25 par tâche » (p. 109) contre seuil par argument d'appel (C.1, p. 218) : 3.27.
- Parcours d'approbation « P3 » (figure 16) contre P2 au-delà du seuil (C.6) : 3.35.
- Figure 13 contre ORC-15, tableau 31 et annexe B (p. 215) : 3.06.
- Figure 14 contre tableau 28 : 3.61. Feng et al. sourcé / indicatif (p. 106) : 3.65.
- Constance vérifiée : 15 minutes (AUT-12, figure 16, C.6, IAM-15), seuil de 5 000 $ (tableau 31, C), task_id « tache-7f3c2a » (§ 7.6 et C.6), forces normatives ORC et AUT identiques au registre de l'annexe D.

## Arbitrages transversaux proposés (défauts qui touchent d'autres tranches : la décision à prendre, l'option recommandée, les sections touchées)

**A1. Une compensation passe-t-elle le coupe-circuit, le plafond, l'échéance de délégation et la révocation?** (3.02, 3.05)
- Option recommandée : oui, par un canal de compensation distinct. Arrêt « vers l'avant » seulement; les compensations s'exécutent sous une identité de service de compensation non révoquée par l'arrêt, limitée aux outils de compensation déclarés au catalogue, toujours via la passerelle et journalisée en audit; budget de compensation réservé hors plafonds; état de drainage avant l'échéance d'un mandat d'agent ambiant. Option écartée : lever l'arrêt pour compenser (réactive l'agent compromis).
- Sections touchées : 7.5 (ORC-15 à 18), 7.8 (ORC-26, ORC-28), 8.6 (AUT-18), 9.2 (IAM-07), 9.4 (IAM-20, figure 18), 11.5 (retrait), annexe A, annexe D.

**A2. Une compensation P3 exige-t-elle une nouvelle approbation?** (3.05, 3.06)
- Option recommandée : non pour la compensation exacte d'une étape approuvée : son empreinte figure dans la demande d'approbation de l'étape d'origine, bornée au montant d'origine et liée à sa clé d'idempotence; oui pour toute autre compensation P3. Classer une préautorisation annulable en P2 et la capture en P3.
- Sections touchées : 7.5, 8.3 (tableau 31, AUT-08, AUT-09), 8.5 (AUT-12), annexe C (C.1 : champ `compensation`, C.6).

**A3. Usage unique du jeton d'approbation contre réessai idempotent et reprise durable.** (3.04, 3.41)
- Option recommandée : « une exécution par (jti, h) », où h inclut la clé d'idempotence (déjà le cas en C.6, `idempotency_key` dans les arguments hachés); représentation admise jusqu'à `exp` pour un réessai, le service dédupliquant; registre de jti partagé, atomique, fermé en cas d'indisponibilité; après `exp`, pas de nouvelle approbation si le service atteste l'effet par la clé. Rendre obligatoire, pour tout outil P2/P3, l'argument déclaré de clé d'idempotence (comme C.1).
- Sections touchées : 7.4, 7.6 (ORC-21, ORC-22), 8.5 (AUT-12, figure 16), 9.4 (passerelle, haute disponibilité), 10.3 (OBS-12), annexes A et C (C.6, C.8).

**A4. La passerelle couvre-t-elle l'intradomaine?** (3.28)
- Option recommandée : tout appel P2 ou P3 passe par la passerelle d'agents, quelle que soit la frontière; l'intradomaine P0-P1 peut rester au serveur de ressources (IAM-17). Option de repli : un « point d'application des politiques » abstrait (passerelle ou serveur de ressources) tenu d'appliquer AUT-01 et AUT-10 à 12, y compris la vérification du jeton et de h, ce qui multiplie les implémentations à homologuer.
- Sections touchées : 5.1 (règle centrale, ARC-01), 6.5 (MCP-01, MCP-08), 8.1-8.5, 9.4 (IAM-17 à 19), 15 (phase 2 « premiers N3 intradomaine »).

**A5. Où voyagent les jetons (délégué, approbation)?** (3.18)
- Option recommandée : jamais dans un contenu logique ni dans le contexte du modèle : en-tête d'authentification du transport, injecté et retiré par le code d'exécution ou la passerelle; exclus des points de contrôle, du journal de compensation et des traces; jeton d'approbation conservé par la passerelle, la reprise se rattachant à la demande.
- Sections touchées : 7.4 (ORC-13), 7.5 (ORC-16), 7.7 (ORC-23 et exemple), 8.5 (figure 16), 9.2 (IAM-06), 9.3 (délégation), 10.1-10.2 (contenu des traces), annexe C.

**A6. Référence unique pour « ce qui exige une approbation ».** (3.35, 3.25)
- Option recommandée : toute exigence renvoie au « contrôle calculé selon l'EXIG-AUT-10 », défini comme l'union des contrôles avec l'ordre d'approbation de 3.25; la figure 15 n'en est qu'une composante.
- Sections touchées : 8.4-8.7 (AUT-10, 12, 15, 20, ATTENTION, tableau 32, figure 16), 11.2 (GOV-04), annexe A, annexe C.

**A7. Définition de la session et cohérence de l'état de tâche à la passerelle.** (3.26, 3.41)
- Option recommandée : session = contexte du modèle depuis le dernier contexte vierge, mémoire persistante comprise, héritée par les agents délégués; état de tâche (marquage de contenu non fiable, budgets, compteurs de seuil) tenu dans un magasin à cohérence forte par tâche; état indisponible : refus.
- Sections touchées : 8.4 (AUT-10), 9.1 (IAM-02), 9.6 (SEC-04, SEC-06), 9.4, 5.5 (mémoire), glossaire.

**A8. Statut du hors bande.** (3.31, 3.72)
- Option recommandée : hors bande (appareil et session distincts de l'agent) en DOIT pour tout P3 dans AUT-09; CIBA reste un DEVRAIT pour le moyen (AUT-14); définition au glossaire.
- Sections touchées : 8.1 (tableau 28, figure 14), 8.3 (tableau 31), 8.5, 12.1 (tableau 46), annexe B, glossaire.

**A9. Source normative unique pour l'art. 12.1.** (3.39, 3.40, 3.75)
- Option recommandée : chapitre 12 (CON-07 à 09) source unique; AUT-22 et AUT-23 renvoient; qualification a priori dans l'EFVP avec défaut prudent.
- Sections touchées : 8.8, 12.2, 12.9 (évaluation d'impact), annexe D.

**A10. Unité et portée d'agrégation des seuils.** (3.27)
- Option recommandée : chaque seuil du catalogue déclare unité, portée (appel, tâche, agent, mandant) et fenêtre; la passerelle tient les compteurs.
- Sections touchées : 6.8 (catalogue), 8.2-8.4, 10.6 (enveloppe budgétaire), annexes A et C (C.1, C.7).

## Constats écartés à la contre-vérification (identifiant, raison)
Aucun constat n'est entièrement écarté. Écartés en partie :
- 11-17, partie « cellules Faible × P1 et Faible × P3 inatteignables » : les exemples « dossier client, paie » et « virement, suppression, envoi » sont des en-têtes de colonne de la figure 15, pas des contenus de cellule; Faible × P3 est atteignable (un seul critère suffit, p. ex. données publiques). Le résidu est conservé en 3.60.
- 11-11, partie « contradiction » et contre-exemple « autorisé à N3 selon AUT-07 » : AUT-07 est une interdiction, non une autorisation; les deux règles donnent N2. Résidu (redondance, vocabulaire) en 3.59.
- 11-10, point (2) « aucune politique ne couvre l'action » : réglé par le renvoi d'AUT-11 au « refus général de tout appel dépourvu de décision de politique valide (EXIG-IAM-18) ». Les autres points restent en 3.29.
- 12-01, gravité BLOQUANT : la légende de la figure 15 (« plus strict, jamais plus souple ») et AUT-10 permettent de résoudre la contradiction; rétrogradé en MAJEUR (3.35).
- 10-22, partie « ORC-23 interdit de transmettre ce qui rendrait la scission sûre » : ORC-23 admet l'historique « sauf exception justifiée à la fiche ». Rétrogradé en MINEUR (3.55).
- 12-14, partie « la passerelle ne réévalue pas le seuil » : AUT-10 s'applique « pour chaque appel »; seul reste non dit le repassage de l'action éditée avant l'émission du jeton, et la règle des quatre yeux (3.37).

Rétrogradés sans écartement : 10-18 (MAJEUR → MINEUR, ORC-14 n'est qu'un DEVRAIT). Relevés par fusion : 12-05 (MAJEUR → BLOQUANT avec 11-01), 12-07, 12-10, 12-16, 11-23, 12-08, 12-21, 10-40 (MINEUR → intégrés à un MAJEUR).

conso_3.md : 82 défauts (3 BLOQUANT, 38 MAJEUR, 41 MINEUR), 0 constats écartés
