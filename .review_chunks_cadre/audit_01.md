# Audit chunk_01 — pages 1-12

## Synthèse
Le chunk couvre la page de titre, l'historique des versions, la méthode, les tables des matières, le sommaire exécutif (figure 1, dix décisions, « Par où commencer ») et les § 1.1-1.3 (pages 11-12 en recouvrement : seuls les constats de couture y sont retenus). Le texte est dense, bien renvoyé, et les numéros de page des tables des matières sont exacts. Il reste trois défauts graves. (1) Les décisions sont énoncées de façon absolue (passerelle, clés, homologation), alors que la feuille de route tolère des contournements pendant la transition et que les règles de transition n'ont aucune force normative selon le § 1.4. (2) L'idempotence promise sur « chaque écriture » ne tient pas avec des API « jamais réécrites » et une vérification déléguée à un adaptateur. (3) La « matrice de correspondance unique » annoncée pour E-23 n'existe pas : le tableau 50 ne comporte aucune colonne E-23.

## Constats

### [01-01] [MAJEUR] Décisions absolues contre régime transitoire non normatif
- **Axe** : A
- **Localisation** : sommaire, p. 8, décision 2 : « Rien ne contourne la passerelle ni le catalogue. »; p. 9 : « Aucun agent ne passe en production sans franchir la grille d’homologation de l’annexe A. »; historique v1.1, p. 2 : « N3 entre domaines conditionné au passage par la passerelle ».
- **Diagnostic** : EXIG-ARC-01 (DOIT, p. 34) impose déjà le passage par la passerelle pour tout appel MCP, tout appel vers un autre agent et toute donnée hors domaine, sans clause transitoire. Pourtant, la passerelle d'agents n'arrive qu'en phase Plateforme (tableau 58, p. 201), et le § 15.1 (p. 202) admet : « Tant qu’un appel interdomaines d’un agent contourne la passerelle, les actions de cet agent hors de son domaine sont plafonnées à N2 ». Trois conséquences. (a) Le changement v1.1 « N3 conditionné à la passerelle » est soit redondant avec un DOIT existant, soit l'aveu d'une tolérance de contournement que l'exigence interdit. (b) Selon le § 1.4 (p. 13), seuls les blocs EXIG des chapitres 5 à 13, les PRIN et les tableaux qu'une exigence vise expressément sont normatifs. Aucune exigence ne renvoie au tableau 58 (vérifié par recherche), si bien que les plafonds de phase et les « règles de progression » sont informatifs. (c) Le § 14 (p. 199) affirme que le modèle « ne suspend aucune exigence » et ramène pourtant les agents existants en conformité « selon la feuille de route, sous les plafonds de phase ». La décision 5 (« Aucun compte partagé ni clé statique ») subit le même écart : le tableau 58 maintient un « secret propre par agent au coffre sous dérogation transitoire ».
- **Contre-exemple ou scénario de défaillance** : au mois 2, un agent N1 existant, de classe modérée, appelle un serveur MCP d'un autre domaine sans passerelle (elle n'existe pas encore). Il viole EXIG-ARC-01 (DOIT). Aucune dérogation n'est requise par un texte normatif, puisque le plafond de phase est informatif. Le comité ne peut donc ni sanctionner l'écart ni démontrer la conformité en audit.
- **Correctif proposé** : créer une exigence de transition (p. ex. EXIG-GOV-xx) qui rend normatif le tableau 58, énumère les exigences suspendues par phase (ARC-01, IAM sur les clés statiques) avec leur échéance, et exige une dérogation collective inscrite au registre pour chaque agent existant non conforme. Reformuler les décisions 2 et 5 en « état cible au jalon 3 », avec renvoi à cette exigence. Retirer de la v1.1 la condition redondante ou la rattacher à l'exception transitoire.
- **Confiance** : vérifié dans le texte (EXIG-ARC-01, § 1.4, tableau 58, § 15.1, § 14); conséquence déduite.

### [01-02] [MAJEUR] Idempotence garantie par un adaptateur devant des API « jamais réécrites »
- **Axe** : A
- **Localisation** : sommaire, p. 8, décision 1 : « Les API existantes sont exposées par adaptateurs, jamais réécrites. »; décision 7 : « chaque écriture porte une clé d’idempotence ».
- **Diagnostic** : EXIG-ARC-14 (DOIT, p. 37) interdit de réécrire les services d'origine. EXIG-ORC-22 (p. 98) autorise la vérification de la clé « directement ou par son adaptateur », alors que sa propre justification énonce : « seul le système visé sait si l’effet a déjà eu lieu ». Un adaptateur externe ne peut garantir « aucun effet supplémentaire » que si le système d'enregistrement offre une écriture conditionnelle ou une clé naturelle consultable. Sinon, l'écriture dans le système et la mémorisation de la clé par l'adaptateur ne sont pas atomiques. Le postulat implicite (tout système d'enregistrement permet une déduplication externe) n'est énoncé nulle part.
- **Contre-exemple ou scénario de défaillance** : l'adaptateur transmet un virement P3 à un ERP sans prise en charge de clé. L'ERP valide, puis l'adaptateur plante avant d'enregistrer « clé K = traitée ». Au réessai avec K, l'adaptateur ne trouve pas K et réémet le virement : double effet, malgré une conformité apparente à ORC-21 et ORC-22.
- **Correctif proposé** : exiger, pour un outil P2 ou P3 inscrit au catalogue, la preuve d'un mécanisme atomique, soit côté système (clé ou écriture conditionnelle), soit par une transaction locale ou une boîte d'envoi (outbox) partagée avec le système. À défaut, classer l'outil comme non idempotent, ce qui impose une approbation à chaque appel et interdit le réessai automatique. Nuancer « jamais réécrites » en « sans réécriture, sauf l'ajout minimal requis pour l'idempotence ».
- **Confiance** : vérifié dans le texte (EXIG-ARC-14, ORC-21, ORC-22); scénario déduit.

### [01-03] [MAJEUR] E-23 absent de la « matrice de correspondance unique »
- **Axe** : C
- **Localisation** : sommaire, p. 8, décision 10 : « sont intégrés aux exigences et à une matrice de correspondance unique (chapitre 12) ».
- **Diagnostic** : la décision 10 range E-23 parmi les référentiels intégrés à la matrice unique. Or le tableau 50 (p. 184) ne comporte que les colonnes NIST, ISO/IEC 42001, Loi 25 (Loi sur le privé seulement), RIA et artefacts. E-23 n'y figure pas, l'article 65.2 de la Loi sur l'accès non plus, alors que la v1.1 l'a ajouté aux critères de la classe élevée (p. 2). EXIG-CON-18 étiquette chaque preuve « selon le tableau 50 » : pour une institution financière fédérale, les preuves E-23 restent hors de la base de preuves unique.
- **Contre-exemple ou scénario de défaillance** : à l'examen du BSIF, l'audit interne cherche dans la base de preuves les validations E-23 d'un agent. Aucune étiquette E-23 n'existe, puisque la matrice ne prévoit pas la colonne, et il faut un dossier distinct. C'est précisément la duplication que vise à éviter EXIG-CON-18.
- **Correctif proposé** : ajouter au tableau 50 une colonne E-23 (inventaire, validation, revue indépendante, liens vers EXIG-CON-12) et une mention de l'art. 65.2 de la Loi sur l'accès pour les organismes publics, ou corriger la décision 10.
- **Confiance** : vérifié dans le texte.

### [01-04] [MAJEUR] La méthode surestime la couverture de vérification des sources
- **Axe** : B
- **Localisation** : historique v1.0, p. 2 : « validation de chacune des 121 références » et « réouverture et contrôle de chacune des références citées »; méthode, p. 2 : « Chacune des 121 références de la recherche documentaire a été ouverte lorsque la page était accessible (108 sur 121) ».
- **Diagnostic** : le seul paragraphe de méthode du liminaire décrit la validation de 121 références. Or F.2 (p. 242) précise que 88 d'entre elles ont été remplacées ou retirées et que 33 seulement sont conservées, alors que l'annexe G en compte 473. Le F.1 (p. 242) indique que l'audit final a rouvert « les 428 références alors citées », puis ajouté 49 sources. L'affirmation « chacune des références citées » ne couvre donc pas, à la lettre, les références ajoutées pendant l'audit, dont la vérification n'est pas décrite. Le lecteur du liminaire attribue à 473 références une méthode décrite pour 121.
- **Contre-exemple ou scénario de défaillance** : une des 49 références ajoutées appuie une exigence. Rien n'atteste qu'elle a été confrontée affirmation par affirmation, et le liminaire affirme le contraire.
- **Correctif proposé** : dans « Méthode », donner les trois populations (121 de la recherche, dont 33 conservées; 428 rouvertes à l'audit final; 49 ajoutées, avec leur mode de vérification) et le total de 473. Rapprocher 428 + 49 = 477 du total de 473 (4 retraits à expliciter).
- **Confiance** : vérifié dans le texte pour les chiffres; absence de vérification des 49 ajouts déduite. Pour trancher : le registre de l'audit final (tableau 69 ou annexe de travail).

### [01-05] [MINEUR] Portée de la décision 2 plus étroite qu'EXIG-ARC-01
- **Axe** : C
- **Localisation** : p. 8, décision 2 : « tout appel d’un agent vers un outil MCP ou vers une donnée ou un agent d’un autre domaine traverse la passerelle d’agents ».
- **Diagnostic** : EXIG-ARC-01 vise « un autre agent », sans qualificatif de domaine. La décision 2 restreint le passage obligé aux agents d'un autre domaine, et la règle centrale du ch. 5 (p. 32) restreint, elle, tout (outils compris) au « hors de son domaine ». Trois formulations, deux portées.
- **Contre-exemple ou scénario de défaillance** : une équipe lit le sommaire et relie en A2A direct deux agents du même domaine, hors passerelle. Ce montage respecte le sommaire et viole EXIG-ARC-01.
- **Correctif proposé** : aligner le sommaire sur EXIG-ARC-01 (« vers tout outil, ressource ou invite MCP, tout autre agent et toute donnée d'un autre domaine ») et signaler l'incohérence de la p. 32 au chunk 04.
- **Confiance** : vérifié dans le texte.

### [01-06] [MINEUR] La décision 6 diverge d'EXIG-SEC-06 (déclencheur, portée, échappatoire)
- **Axe** : C
- **Localisation** : p. 8, décision 6 : « Tout contenu reçu est une donnée, jamais une instruction. Dès qu’un agent a lu du contenu non fiable, ses capacités d’envoi vers l’extérieur lui sont retirées de façon déterministe ».
- **Diagnostic** : (a) La présomption porte sur « tout contenu reçu », le déclencheur sur le contenu « non fiable ». Lu à la lettre, tout contenu est présumé injecté et le retrait se déclenche dès la première lecture d'outil. EXIG-SEC-06 (p. 135) tranche par le marquage du catalogue, ce que le sommaire ne dit pas. (b) Le sommaire parle de l'« agent », EXIG-SEC-06 de la « session », pour le reste de la session : la persistance du marquage d'une session à l'autre par la mémoire n'est pas évoquée (point à examiner aux chunks 04 et 14). (c) Le sommaire omet le retrait des outils P3 et la levée par approbation humaine liée à l'action.
- **Contre-exemple ou scénario de défaillance** : un agent lit un courriel externe (non fiable) et en écrit un résumé en mémoire sémantique. À la session suivante, il relit ce résumé, qui ne porte aucune marque de contenu non fiable, et récupère ses outils d'envoi.
- **Correctif proposé** : reformuler : « Dès qu'une session a consommé un contenu marqué non fiable au catalogue, la passerelle retire les outils d'envoi et P3 pour le reste de la session, sauf approbation liée à l'action ». Renvoyer à la règle de propagation du marquage par la mémoire, si elle existe.
- **Confiance** : (a) et (c) vérifiés dans le texte; (b) déduit, aucune règle de propagation trouvée par recherche.

### [01-07] [MINEUR] Plafond par classe : renvois et formulation non alignés sur la « source unique »
- **Axe** : C
- **Localisation** : p. 8, décision 4 : « Les niveaux N0 à N4 plafonnent ce qu’un agent peut faire seul selon la classe de risque »; p. 12, § 1.3, étape 2 : « fixer le niveau d’autonomie sous le plafond de la classe (section 8.1) ».
- **Diagnostic** : la v1.1 annonce le plafond « ramené à une seule source normative (EXIG-CON-02) ». Pourtant, le sommaire et le § 1.3 renvoient au ch. 8 ou au § 8.1, pas à EXIG-CON-02 (§ 12.1). La décision 4 inverse en outre la relation : c'est la classe qui plafonne le niveau, et non les niveaux qui plafonnent selon la classe. Enfin, le tableau 46 (p. 171) garde pour la classe modérée « N3, avec des seuils plus bas et une revue a posteriori renforcée », des conditions absentes d'EXIG-CON-02. Même si la note du tableau dit qu'EXIG-CON-02 « fait foi », le statut de ces conditions reste orphelin.
- **Contre-exemple ou scénario de défaillance** : un agent modéré déclaré N3 sans seuils abaissés est conforme à EXIG-CON-02, qui fait foi, et non conforme au tableau 46, que vise EXIG-CON-01. Deux revues aboutissent à deux verdicts.
- **Correctif proposé** : renvoyer partout à EXIG-CON-02; écrire « la classe de risque plafonne le niveau N0 à N4 »; intégrer les conditions de la classe modérée à EXIG-CON-02 ou les retirer du tableau 46.
- **Confiance** : vérifié dans le texte.

### [01-08] [MINEUR] « Journal d'audit inaltérable » : propriété surestimée
- **Axe** : A
- **Localisation** : p. 8, décision 8 : « journal d’audit inaltérable » (aussi dans la figure 1, p. 7).
- **Diagnostic** : le mécanisme décrit au § 10.3 (chaînage `precedent_sha256`, signature, canonisation RFC 8785) rend toute altération détectable, pas impossible. L'inaltérabilité exige en plus un support en écriture unique (WORM) ou un ancrage externe. Sans ancrage, quiconque détient la clé de signature du service d'audit peut réécrire la chaîne entière à partir d'un point.
- **Contre-exemple ou scénario de défaillance** : un administrateur compromis tronque le journal au rang n et re-signe des entrées n+1… La chaîne reste valide, et rien ne détecte la troncature sans point d'ancrage externe.
- **Correctif proposé** : écrire « inviolable de façon détectable (chaîné et signé) », et exiger un ancrage périodique de la tête de chaîne hors du domaine d'administration, ou un stockage WORM.
- **Confiance** : déduit, à confirmer au chunk 15 (§ 10.3).

### [01-09] [MINEUR] Surcharge du terme « palier »
- **Axe** : C
- **Localisation** : p. 8, décision 4 : « Les outils sont classés P0 à P3 »; décision 8 : « évaluation en trois paliers » (aussi dans l'historique v0.2, p. 2, et la figure 1).
- **Diagnostic** : « palier » désigne à la fois le risque d'un outil (P0-P3) et l'étage d'évaluation (1-3), alors que le § 3.1 insiste pour qu'on ne confonde jamais les échelles. « Palier 2 » devient ambigu (p. ex. p. 152 : « Palier 2 : trajectoires »).
- **Contre-exemple ou scénario de défaillance** : « l'outil a franchi le palier 2 » peut se lire comme une écriture réversible ou comme une évaluation de trajectoire réussie.
- **Correctif proposé** : renommer les étages d'évaluation (« niveaux d'évaluation E1-E3 » ou « étages »).
- **Confiance** : vérifié dans le texte.

### [01-10] [MINEUR] Confusion entre catalogue d'entreprise et catalogue des protocoles
- **Axe** : C
- **Localisation** : p. 2, Avertissements : « les versions applicables sont fixées au catalogue d’entreprise, révisé chaque trimestre ».
- **Diagnostic** : le cadre distingue le catalogue des protocoles (§ 6.3, révisé chaque trimestre) du catalogue d'entreprise des contrats et outils (« À distinguer du catalogue des protocoles », p. 24). La page 1 et la décision 1 attribuent correctement la révision trimestrielle au catalogue des protocoles; les Avertissements l'attribuent au catalogue d'entreprise. La décision 1 (« fixées au catalogue ») et la décision 2 (« absent du catalogue ») emploient le même mot nu pour les deux objets.
- **Contre-exemple ou scénario de défaillance** : une équipe croit que l'inscription d'un nouvel outil au catalogue d'entreprise attend la révision trimestrielle.
- **Correctif proposé** : écrire « catalogue des protocoles » dans les Avertissements et dans la décision 1.
- **Confiance** : vérifié dans le texte.

### [01-11] [MINEUR] Le coupe-circuit « global » trimestriel n'est pas ce qu'exige EXIG-ORC-28
- **Axe** : B
- **Localisation** : p. 8, décision 7 : « un coupe-circuit global est testé chaque trimestre (chapitre 7) ».
- **Diagnostic** : EXIG-ORC-28 (p. 99) exige un coupe-circuit global et « un exercice d’arrêt » trimestriel, sans préciser s'il doit être global. Le sommaire durcit l'exigence. Un arrêt global réel chaque trimestre en production suspend toutes les sagas (coût et risque opérationnels), et un arrêt global simulé n'éprouve pas la propagation réelle.
- **Contre-exemple ou scénario de défaillance** : une organisation exerce chaque trimestre un arrêt ciblé et respecte ORC-28, mais ne respecte pas le sommaire. Une autre déclenche un arrêt global réel et laisse des sagas « suspendues » au-delà de leurs délais métier.
- **Correctif proposé** : préciser dans ORC-28 la portée de l'exercice (global, au moins une fois par an, en environnement représentatif; ciblé chaque trimestre) et aligner le sommaire.
- **Confiance** : vérifié dans le texte; la question de faisabilité est déduite.

### [01-12] [MINEUR] « Pourquoi maintenant » : des prévisions présentées comme données probantes
- **Axe** : B
- **Localisation** : p. 7 : « 40 % des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026, contre moins de 5 % en 2025 (prévision Gartner, août 2025) ».
- **Diagnostic** : trois des quatre chiffres sont des prévisions d'analyste, sans population ni méthode. La première vise une échéance (fin 2026) tombée deux mois après l'état des sources : citée en octobre 2026, elle aurait dû être confrontée à une mesure observée. Le saut de « moins de 15 » à « plus de 150 000 » agents par entreprise (×10⁴ en trois ans) dépend entièrement de la définition d'« agent », que le sommaire ne donne pas. Le ch. 15 (p. 205) l'admet (« ordre de grandeur prospectif »), le sommaire non. Le tableau 66 range les « communiqués des firmes d'analystes » en catégorie A, « appui de toute exigence et de tout fait » : il confond la fidélité de la citation et la fiabilité de la prévision.
- **Contre-exemple ou scénario de défaillance** : un comité invoque le 40 % en 2027 pour dimensionner la passerelle. Si le chiffre réel est de 15 %, le dimensionnement et l'argumentaire ne reposent sur rien de vérifiable.
- **Correctif proposé** : qualifier ces chiffres de « prévisions » dans le sommaire, reprendre la mise en garde du ch. 15, préférer une donnée observée pour 2026, et créer au tableau 66 une sous-catégorie « prévision d'analyste » limitée aux faits de contexte.
- **Confiance** : vérifié dans le texte; exactitude des chiffres à vérifier (voir questions).

### [01-13] [MINEUR] Le chiffre de 13 % n'a aucun appel de référence
- **Axe** : C
- **Localisation** : p. 7 : « 13 % des organisations estiment avoir la bonne gouvernance de leurs agents (Gartner, avril 2026) ».
- **Diagnostic** : ce chiffre ne réapparaît nulle part dans le corps (vérifié par recherche), et aucun appel [n] ne l'accompagne. Il échappe ainsi à la règle « chaque fait sourcé ». La source vraisemblable est [2] (communiqué Gartner du 28 avril 2026), mais c'est une supposition. La population (« des organisations ») n'est pas précisée.
- **Contre-exemple ou scénario de défaillance** : un lecteur ne peut pas retracer ce chiffre jusqu'à sa source, ce qui contredit F (« retracer l'origine d'un fait »).
- **Correctif proposé** : ajouter l'appel [2] (ou la bonne référence) et la population d'enquête; reprendre le chiffre au § 2.1.
- **Confiance** : vérifié dans le texte; attribution à [2] supposée.

### [01-14] [MINEUR] Dates de l'état des sources et de la version 1.0 incohérentes
- **Axe** : C
- **Localisation** : p. 1 : « Faits, versions et dates vérifiés aux 27 et 28 octobre 2026 »; p. 2, Avertissements : « reflètent l’état des sources au 27 octobre 2026 »; historique, ligne 1.0 datée « 27 oct. 2026 », qui inclut l'« Audit final du 28 octobre 2026 ».
- **Diagnostic** : deux dates d'état des sources circulent (27, ou 27 et 28). La version 1.0 décrit un audit postérieur à sa propre date. Les tableaux portent « état au 27 octobre », alors que les corrections de l'audit final, du 28, y ont été intégrées.
- **Contre-exemple ou scénario de défaillance** : un fait modifié le 28 octobre (p. ex. un statut corrigé à l'audit final) est daté du 27 dans un tableau. L'annexe H, qui compare l'état au 1er novembre à celui du 27, applique alors un mauvais point de référence.
- **Correctif proposé** : fixer une seule date d'état des sources (le 28 octobre, fin de l'audit) ou dissocier l'état des sources (27) de la date de l'audit (28); dater la v1.0 du 28 ou séparer « 1.0 » et « 1.0 audit ».
- **Confiance** : vérifié dans le texte.

### [01-15] [MINEUR] Gestion de version : actualisation sans incrément et statut ambigu
- **Axe** : C
- **Localisation** : p. 1, Statut : « Version finale consolidée, soumise à l’approbation du comité »; pied de chaque page : « Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026 ».
- **Diagnostic** : l'annexe H (1er novembre) modifie le document, notamment par un tableau d'errata proposant des lectures corrigées (p. ex. « Lire neuf entreprises », H.4) qui touchent des chapitres normatifs. Pourtant, ni le numéro de version ni l'historique ne changent : deux artefacts distincts portent l'identifiant « 1.1 ». Le statut juxtapose « finale » et « soumise à l'approbation ». Le sommaire affirme « Il est normatif » sans dire à partir de quand, avant ou après l'approbation.
- **Contre-exemple ou scénario de défaillance** : une revue d'architecture cite la « v1.1 » : impossible de savoir si elle porte sur la version avec ou sans annexe H et errata.
- **Correctif proposé** : numéroter l'actualisation (1.1.1 ou 1.2-informative) et l'inscrire à l'historique; écrire « version finale proposée, en vigueur à l'approbation du comité ».
- **Confiance** : vérifié dans le texte.

### [01-16] [MINEUR] Dérives du résumé de la feuille de route (jalons, durées, échéances)
- **Axe** : C
- **Localisation** : p. 9 : « La mise en œuvre suit quatre phases séparées par trois jalons, vise le niveau 3 de maturité, « Défini », en 18 mois »; p. 2 (v1.1) : « jalon J2a de conformité au RIA avant le 2 décembre 2027 » et « migration MCP avancée dans la phase Plateforme et datée au jalon 2 ».
- **Diagnostic** : (a) La même phrase parle de « trois jalons », puis des « jalons 4 et 5 ». Le ch. 15 en compte six (J1, J2, J2a, J3, J4, J5). (b) Le tableau 59 place J3 « début juill. 2028 » pour un mois 0 au 1er décembre 2026, soit 19 mois. (c) Le ch. 15 et l'annexe H fixent J2a « au plus tard le 1er novembre 2027 »; l'historique écrit « avant le 2 décembre 2027 ». (d) La migration MCP est exigée au 28 juillet 2027 (EXIG-MCP-22), alors que J2 tombe « début oct. 2027 » : la migration n'est pas « datée au jalon 2 », elle y est seulement constatée, deux mois après l'échéance.
- **Contre-exemple ou scénario de défaillance** : un serveur non migré au 28 juillet n'est détecté qu'au constat de J2, en octobre, ce qui laisse deux mois de non-conformité sans point de contrôle.
- **Correctif proposé** : écrire « quatre phases ouvertes par trois jalons de passage, plus trois jalons de suivi (J2a, J4, J5) »; « en 18 mois environ (19 avec les congés) »; aligner J2a sur le 1er novembre 2027; ajouter un point de contrôle de migration au 28 juillet 2027.
- **Confiance** : vérifié dans le texte (tableaux 58 et 59, § 15.1, H.2).

### [01-17] [MINEUR] Nombre d'annexes : table des matières A-H contre « sept annexes, de A à G »
- **Axe** : C
- **Localisation** : p. 3 : « H Actualisation de novembre 2026 » sous « Annexes — Outils d’application »; § 1.5, p. 13 : « Sept annexes, de A à G ».
- **Diagnostic** : la table des matières compte huit annexes, le § 1.5 sept. Le chapeau « Outils d'application » coiffe aussi G (références) et H (actualisation), qui ne sont pas des outils. Constat non consigné en H.4.
- **Contre-exemple ou scénario de défaillance** : un renvoi ou un contrôle de complétude fondé sur le § 1.5 ignore l'annexe H et ses errata.
- **Correctif proposé** : écrire « huit annexes, de A à H » au § 1.5 et retitrer le chapeau (« Annexes »).
- **Confiance** : vérifié dans le texte.

### [01-18] [MINEUR] Libellés de la figure 1
- **Axe** : C
- **Localisation** : p. 7, figure 1 : « Risques et conformité (chapitres 12 et 13) »; « annexes : grille d’homologation, fiche d’agent, contrats types, registre des exigences, glossaire, validation des sources ».
- **Diagnostic** : le ch. 13 traite de l'approvisionnement, pas de la conformité. La liste d'annexes omet G et H. « BSIF » désigne un régulateur là où la ligne voisine nomme des textes (Loi 25, RIA) : il faudrait « E-23 ».
- **Contre-exemple ou scénario de défaillance** : sans objet, il s'agit de clarté.
- **Correctif proposé** : « Risques, conformité et approvisionnement (chapitres 12 et 13) »; « E-23 (BSIF) »; ajouter « références, actualisation ».
- **Confiance** : vérifié dans le texte.

### [01-19] [MINEUR] « Vérifiables en revue ou en test » : toutes les exigences ne le sont pas
- **Axe** : B
- **Localisation** : p. 7 : « les chapitres 5 à 13 énoncent des exigences identifiées, vérifiables en revue d’architecture ou en test ».
- **Diagnostic** : certaines exigences reposent sur un jugement sans critère opposable. EXIG-AUT-01 (p. 104) en donne un exemple : « Le niveau déclaré DOIT être le plus bas qui permet d’atteindre l’objectif métier ». Aucun test ne prouve qu'un niveau inférieur ne suffirait pas, et la revue ne peut vérifier que la présence d'une justification.
- **Contre-exemple ou scénario de défaillance** : deux réviseurs jugent différemment le même dossier N3, et les deux verdicts sont « conformes » à la lettre.
- **Correctif proposé** : écrire « vérifiables en revue ou en test, ou, à défaut, par la présence d'une justification consignée », et marquer dans l'annexe D le mode de vérification de chaque exigence (test, revue factuelle, revue de justification).
- **Confiance** : vérifié dans le texte.

### [01-20] [MINEUR] Force différente : « n'oblige pas à modifier » contre « jamais réécrites »
- **Axe** : C
- **Localisation** : p. 11, tableau 1, hors portée : « Systèmes d’enregistrement eux-mêmes, que le cadre n’oblige pas à modifier »; p. 8 : « jamais réécrites ».
- **Diagnostic** : le tableau 1 exprime une absence d'obligation, alors que le sommaire et EXIG-ARC-14 (DOIT « sans réécriture des services d’origine ») expriment une interdiction. Une modernisation volontaire d'une API (p. ex. pour ajouter l'en-tête `Idempotency-Key`) serait permise selon le tableau 1 et interdite selon ARC-14. Ce constat est lié à 01-02.
- **Contre-exemple ou scénario de défaillance** : une équipe ajoute la prise en charge d'une clé d'idempotence à son service REST et se voit opposer EXIG-ARC-14 en revue.
- **Correctif proposé** : reformuler ARC-14 en « n'exige pas la réécriture » et la décision 1 en « exposées par adaptateurs, sans réécriture obligatoire ».
- **Confiance** : vérifié dans le texte.

### [01-21] [MINEUR] Fenêtre de validation initiale E-23 très courte
- **Axe** : B
- **Localisation** : p. 2 (v1.1) : « validation initiale des agents visés par E-23 avant le 1er mai 2027 ».
- **Diagnostic** : selon le calage (tableau 59), la phase Plateforme s'ouvre à la mi-mars 2027. La validation initiale des agents et modèles inscrits à l'inventaire E-23 doit donc tenir en environ six semaines, au début d'une phase qui met aussi en place la passerelle, les identités et le traçage. Aucune hypothèse de capacité (nombre de modèles, validateurs indépendants) n'est posée. La règle « les échéances externes passent en tête de phase » ne crée pas de capacité.
- **Contre-exemple ou scénario de défaillance** : l'inventaire du jalon 1 révèle 40 modèles à risque non négligeable, dont des modèles de fournisseurs. La validation indépendante est infaisable en six semaines, et l'institution se trouve non conforme dès l'entrée en vigueur.
- **Correctif proposé** : faire commencer la validation E-23 en phase Fondations pour les agents déjà inventoriés, fixer un critère de priorisation par risque et prévoir le cas d'un plan de validation documenté à l'échéance. L'attente réelle du BSIF au 1er mai 2027 reste à vérifier.
- **Confiance** : déduit; l'attente du BSIF est à vérifier (source externe).

## Points forts
Les numéros de page des tables des matières (100 tableaux et figures, 23 chapitres et annexes) correspondent tous au corps, vérifié par script. Le liminaire distingue clairement exigence externe et choix du cadre, et chaque décision renvoie à son chapitre. L'historique v1.1 énumère honnêtement les modifications corrélatives. Les cas limites de portée (§ 1.2 : premier outil, fonction « agentique » rebaptisée, doute traité comme visé) sont tranchés par des règles simples.

## Questions pour l'audit bibliographique
- p. 7 : le communiqué Gartner du 28 avril 2026 [2] contient-il le « 13 % » et le « > 150 000 agents par entreprise du Fortune 500 d'ici 2028, contre moins de 15 en 2025 »? Population et définition d'« agent »?
- p. 7 : [1] (26 août 2025, 40 % des applications d'ici 2026) et [3] (25 juin 2025, plus de 40 % de projets annulés d'ici fin 2027) : à ma connaissance, les chiffres et les dates sont exacts; à confirmer.
- p. 8 : A2A versé à l'AAIF (billet du 27 août 2026) : déjà consigné en H.4 (no 2), confirmé; la date d'approbation du 4 août reste non vérifiée.
- p. 8 : la formation de l'AAIF le 9 décembre 2025 avec MCP [4] me semble exacte; à confirmer.
- p. 8, réf. [6] : auteur noté « Erik S. »; *Building effective agents* est signé Erik Schluntz et Barry Zhang : forme de l'auteur à corriger dans l'annexe G.
- p. 9 : « MCP sans état » : la révision 2026-07-28 retire-t-elle effectivement les sessions protocolaires et `Mcp-Session-Id` (SEP-2567, SEP-2575)? Existence d'« A2A 1.0 »?
- p. 2 : le règlement (UE) 2026/1744 reporte-t-il l'annexe III au 2 décembre 2027 et l'annexe I au 2 août 2028? (EUR-Lex non rouvert selon H.5.)
- p. 2, p. 8 : E-23 (2027) en vigueur le 1er mai 2027, applicable aux institutions financières fédérales; le BSIF exige-t-il à cette date une validation complète des modèles existants ou un plan?
- p. 2 : l'art. 65.2 de la Loi sur l'accès vise-t-il bien les décisions fondées exclusivement sur un traitement automatisé par un organisme public (pendant de l'art. 12.1 de la Loi sur le privé)? Je le crois exact.
- p. 7 : le European Interoperability Framework (EIF) retient-il bien quatre niveaux (juridique, organisationnel, sémantique, technique)? Je le crois exact.
- p. 12 : Gartner (juin 2025, [3]) parle-t-il bien de produits rebaptisés « agentiques » (*agent washing*)? Je le crois exact.

audit_01.md : 21 constats (0 BLOQUANT, 4 MAJEUR, 17 MINEUR)
