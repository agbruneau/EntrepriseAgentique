# Audit chunk_19 — pages 181-192

## Synthèse
Le chunk couvre la fin du § 12.4 (tableau 49, EXIG-CON-13 à 16, pages de recouvrement), les § 12.5 (NIST AI RMF, ISO/IEC 42001), 12.6 (matrice, EXIG-CON-17 et 18), 12.7 (transparence, EXIG-CON-19 à 22), 12.8 (incidents, EXIG-CON-23 à 25), 12.9 (évaluation d'impact unifiée, EXIG-CON-26), puis le § 13.1 et le début du § 13.2 (recouvrement). Les faits sur le NIST AI RMF, ISO/IEC 42001, le RIA (art. 26, 27, 50, 73) et les délais de notification sont exacts dans l'ensemble. La faiblesse tient à l'articulation avec le reste du cadre. Les trois défauts les plus graves : (1) l'avis d'incident « produit à partir de la télémétrie » est irréalisable, car EXIG-OBS-07 et EXIG-OBS-12 bannissent le contenu de la télémétrie et de l'audit; (2) EXIG-CON-18 (dépôt de preuves unique) contredit EXIG-OBS-11 (journal d'audit dans un magasin distinct des traces); (3) la « règle la plus exigeante » d'EXIG-CON-25 est mal définie, change la force normative de la cible de 72 heures et omet le RGPD.

## Constats

### [19-01] [MAJEUR] Le « dépôt de preuves unique » contredit la séparation du journal d'audit
- **Axe** : A
- **Localisation** : § 12.6, EXIG-CON-18, p. 184-185 : « Chaque preuve […] (trace, enregistrement d'audit, […]) DOIT être conservée une seule fois dans un dépôt de preuves »
- **Diagnostic** : EXIG-OBS-11 (§ 10.3) exige que le journal d'audit soit « tenu dans un magasin distinct des traces, sous d'autres droits d'accès ». EXIG-OBS-13 impose en plus un stockage en ajout seul. Lu à la lettre, EXIG-CON-18 place traces et enregistrements d'audit dans un même dépôt, et en un seul exemplaire. La lecture charitable (un index logique qui pointe vers des magasins distincts) n'est écrite nulle part. Autre problème : une trace peut être « échantillonnée ou purgée par l'exploitation » (pourquoi d'EXIG-OBS-11), et elle devient pourtant une « preuve » conservée une seule fois. Enfin, « une seule fois » interdit à la lettre les copies de sauvegarde et de reprise après sinistre.
- **Contre-exemple ou scénario de défaillance** : un auditeur constate que le dépôt de preuves contient les enregistrements d'audit et les traces sous les mêmes droits, d'où une non-conformité à EXIG-OBS-11. Si l'on sépare les magasins, la non-conformité porte cette fois sur EXIG-CON-18. Autre cas : le dépôt unique, sans réplique, est perdu, et toutes les preuves avec lui.
- **Correctif proposé** : écrire que le dépôt de preuves est un index unique de métadonnées (étiquettes, empreintes, emplacements) et que chaque preuve reste dans son magasin d'origine (audit WORM, traces, GRC). Remplacer « une seule fois » par « une seule version faisant foi, sans duplication logique », sauvegardes exclues.
- **Confiance** : vérifié dans le texte (EXIG-OBS-11, EXIG-OBS-13, EXIG-CON-18)

### [19-02] [MAJEUR] Le tableau 50 ne peut pas servir de schéma d'étiquetage pour EXIG-CON-18
- **Axe** : C
- **Localisation** : § 12.6, tableau 50, p. 184; EXIG-CON-18 : « étiquetée avec les exigences du cadre et les dispositions externes auxquelles elle répond selon le tableau 50 »
- **Diagnostic** : EXIG-CON-18 fait du tableau 50 le référentiel d'étiquetage des preuves, mais ce tableau ne couvre que le NIST, ISO/IEC 42001, la Loi sur le privé et le RIA. Il y manque : (a) l'art. 50 du RIA (EXIG-CON-19 et 20), pourtant au tableau 49; (b) la LPRPDE, le BSIF et E-23 (§ 12.3), que vise pourtant EXIG-CON-25; (c) la Loi sur l'accès (art. 63.5, 65.2, 70.1), citée aux tableaux 46 et 52; (d) MANAGE 3.1 et 3.2 (ressources de tiers, modèles préentraînés), que le texte nomme juste après le tableau sans les reporter dans la ligne « Gérer », alors qu'elles collent aux modèles externes et aux serveurs MCP. De plus, la correspondance se fait par ligne (fonction NIST), pas par exigence : une trace étiquetée « Mesurer » répondrait indistinctement à l'art. 11, à l'art. 12.1, à l'art. 27, aux art. 12, 15 et 72 du RIA. Une telle étiquette ne permet pas de démontrer, « pour une demande précise à une date précise », qu'un engagement a été respecté.
- **Contre-exemple ou scénario de défaillance** : la CAI demande la preuve de la divulgation exigée par EXIG-CON-19, ou le BSIF celle de l'avis de 24 heures. Aucune ligne du tableau 50 ne permet d'étiqueter ces preuves.
- **Correctif proposé** : faire du tableau 50 une matrice au niveau des exigences (EXIG → disposition externe) et ajouter des colonnes ou lignes pour la LPRPDE, le BSIF (E-23, avis d'incident), la Loi sur l'accès, l'art. 50 du RIA et MANAGE 3.1 et 3.2. On peut aussi la générer à partir de l'annexe D.
- **Confiance** : vérifié dans le texte

### [19-03] [BLOQUANT] L'avis d'incident « produit à partir de la télémétrie » est interdit par EXIG-OBS-07 et EXIG-OBS-12
- **Axe** : A
- **Localisation** : § 12.8, p. 187 : « Le cadre fait produire ces champs à partir de la télémétrie des agents »; EXIG-CON-25, p. 188 : « L'événement d'incident produit à partir de la télémétrie comporte les champs de l'avis exigé par le règlement québécois »; étape 3, p. 186 : « Les traces permettent de mesurer le rayon d'atteinte : personnes »
- **Diagnostic** : l'avis à la CAI exige les renseignements visés, le nombre de personnes touchées (dont les résidents du Québec), les motifs du risque de préjudice et les mesures d'atténuation. Or EXIG-OBS-07 interdit dans la télémétrie de production les invites, les réponses, les arguments et les résultats d'outils, et la mémoire. EXIG-OBS-12 ne garde dans l'audit qu'une empreinte SHA-256 des arguments. Les personnes dont le dossier a été exposé figurent dans les résultats d'outils, absents par construction. La résidence n'est captée nulle part. Les motifs et les mesures sont des jugements, pas de la télémétrie. Les deux DOIT ne peuvent donc pas être satisfaits ensemble pour ces champs.
- **Contre-exemple ou scénario de défaillance** : un connecteur MCP trop permissif (l'exemple même du § 12.8) renvoie les dossiers de 300 clients. La trace contient execute_tool, sans résultat; l'audit contient une empreinte d'arguments. Impossible d'établir à partir de là qui est touché ni combien de résidents du Québec le sont.
- **Correctif proposé** : limiter l'exigence aux champs dérivables (identifiants, dates, agent, outils, catégories de données déclarées au catalogue pour l'outil, nombre d'appels). Prévoir une procédure de levée de pseudonymisation et de relecture des sources sous le contrôle du RPRP pour compter les personnes, et laisser explicitement à l'équipe de réponse les champs de jugement. Corriger « les traces permettent de mesurer » en « les traces bornent ».
- **Confiance** : vérifié dans le texte (EXIG-OBS-07, EXIG-OBS-12; contenu de l'avis cité p. 187)

### [19-04] [MAJEUR] La cible de 72 heures est DEVRAIT selon EXIG-CON-24 et DOIT selon EXIG-CON-25
- **Axe** : A
- **Localisation** : EXIG-CON-24, p. 188 : « une cible interne de 72 heures […] que l'équipe de réponse DEVRAIT respecter »; EXIG-CON-25 : « appliquer le plus exigeant : […] délais du tableau 51 »; tableau 51, ligne « Cadre (cible interne) »
- **Diagnostic** : le tableau 51 range la cible du cadre parmi les « régimes ». EXIG-CON-25 (DOIT) impose d'appliquer « le plus exigeant » des délais de ce tableau, ce qui donne force de DOIT à la cible de 72 heures qu'EXIG-CON-24 qualifie de DEVRAIT. La même obligation porte donc deux forces normatives (§ 1.4).
- **Contre-exemple ou scénario de défaillance** : l'avis initial est transmis à 80 heures. Au regard d'EXIG-CON-24, c'est un écart justifiable; au regard d'EXIG-CON-25, c'est une non-conformité. L'indicateur et la grille d'homologation ne peuvent pas trancher.
- **Correctif proposé** : retirer la ligne « Cadre (cible interne) » du tableau 51 (la reporter en note) ou préciser dans EXIG-CON-25 que les cibles internes gardent la force que leur donne leur propre exigence.
- **Confiance** : vérifié dans le texte

### [19-05] [MAJEUR] La « règle la plus exigeante » entre régimes n'est pas une relation d'ordre
- **Axe** : A
- **Localisation** : EXIG-CON-25, p. 188 : « recenser […] les régimes de notification applicables […] et appliquer le plus exigeant »; À RETENIR, p. 189 : « le cadre applique toujours le plus exigeant »
- **Diagnostic** : les régimes n'ont ni les mêmes destinataires (CAI, Commissariat, BSIF, autorités de l'UE), ni les mêmes déclencheurs (« préjudice sérieux », « risque réel de préjudice grave », « incident lié à la technologie », « incident grave »), ni les mêmes contenus. Il n'existe donc pas de « plus exigeant » unique : ce qu'il faut, c'est l'union des obligations, chacune avec son délai. Prise au pied de la lettre, la règle conduit à des absurdités (appliquer le délai de 24 heures du BSIF à l'avis à la CAI) ou à des omissions (ne retenir qu'un régime). La liste qui suit (« registre unique… délais du tableau 51 ») décrit d'ailleurs une union, ce qui contredit le titre.
- **Contre-exemple ou scénario de défaillance** : dans une institution financière fédérale qui opère au Québec, une fuite par un agent déclenche à la fois l'avis au BSIF (24 h), à la CAI (« avec diligence ») et au Commissariat (« dès que possible »). Une équipe qui lit « le plus exigeant » avise le seul BSIF dans les 24 heures et croit avoir satisfait la règle.
- **Correctif proposé** : renommer en « Cumul des régimes de notification ». Chaque régime applicable est satisfait selon son propre déclencheur, destinataire et délai; seuls les paramètres communs (durée de conservation du registre, contenu minimal) prennent la valeur la plus stricte.
- **Confiance** : vérifié dans le texte

### [19-06] [MAJEUR] Régimes de notification omis : RGPD (72 h), Loi sur l'accès, tiers sous la LPRPDE
- **Axe** : A
- **Localisation** : tableau 51, p. 187; EXIG-CON-25 : « (Loi 25, LPRPDE, BSIF, RIA) »; note du tableau : « Le délai de 72 heures est une cible du cadre, non une exigence de la Loi 25 »
- **Diagnostic** : le cadre reconnaît l'applicabilité possible du droit de l'UE (EXIG-CON-13; RGPD art. 35 au § 12.9), mais il omet l'art. 33 du RGPD (notification à l'autorité de contrôle dans les 72 heures) et l'art. 34 (communication aux personnes). Pour un agent qui traite des données de personnes situées dans l'UE, ces 72 heures sont une obligation légale, et non une simple cible. Le tableau 51 omet aussi le régime des organismes publics (Loi sur l'accès, art. 63.8 et suivants), alors que les tableaux 46 et 52 visent ces organismes. Il omet enfin l'avis LPRPDE aux organisations ou institutions susceptibles de réduire le risque (art. 10.2).
- **Contre-exemple ou scénario de défaillance** : un agent de service à la clientèle traite des clients européens d'une filiale (EXIG-CON-13). La fuite est avisée à la CAI à 70 heures, sans que l'autorité de contrôle de l'UE soit avisée, d'où une infraction à l'art. 33 du RGPD. Le cadre présentait pourtant ces 72 heures comme un choix interne.
- **Correctif proposé** : ajouter au tableau 51 les lignes RGPD art. 33 et 34 et Loi sur l'accès art. 63.8, ainsi que l'avis aux tiers de la LPRPDE, et les inclure dans le recensement d'EXIG-CON-25.
- **Confiance** : RGPD art. 33 et 34 : connaissance sûre; art. 63.8 de la Loi sur l'accès et art. 10.2 de la LPRPDE : à vérifier par l'audit bibliographique

### [19-07] [MAJEUR] La définition de l'incident agentique laisse des trous
- **Axe** : A
- **Localisation** : § 12.8, p. 186 : « une action non autorisée, une fuite de données, une décision erronée ayant produit un effet, un contournement de garde-fou ou un emballement des coûts imputable à un agent »; EXIG-CON-24 : « Tout incident de confidentialité impliquant un agent »
- **Diagnostic** : (a) L'indisponibilité ou la dégradation d'un agent n'y figure pas, alors que l'incident technologique au sens du BSIF (tableau 51) couvre les pannes. (b) Le critère « imputable à un agent » exclut l'agent victime : jeton volé et utilisé par un tiers, magasin de mémoire exfiltré, serveur MCP compromis. (c) EXIG-CON-24 vise « impliquant », plus large que « imputable » : un incident de confidentialité peut ainsi relever d'EXIG-CON-24 sans être un incident agentique soumis aux cinq temps d'EXIG-CON-23. L'affirmation « un incident de confidentialité […] en est un cas particulier » est donc fausse dans ces cas. (d) La « perte » de RP (suppression par un agent) n'est pas une « fuite ».
- **Contre-exemple ou scénario de défaillance** : un attaquant exfiltre l'index vectoriel d'un agent. Ce n'est pas une action de l'agent, donc pas un incident agentique : pas de coupe-circuit ni de gel prévu par EXIG-CON-23, mais une inscription au registre au titre d'EXIG-CON-24.
- **Correctif proposé** : définir l'incident agentique comme tout événement de sécurité, de confidentialité, de disponibilité ou d'intégrité qui implique un agent, ses identités, ses mémoires ou ses outils, qu'il en soit l'auteur ou la cible. Aligner EXIG-CON-23 et EXIG-CON-24 sur le même terme.
- **Confiance** : vérifié dans le texte (définition; tableau 51); portée de l'avis du BSIF : à vérifier

### [19-08] [MAJEUR] Aucune échelle de gravité : « incident grave » n'est pas défini, et les cinq temps s'appliquent uniformément
- **Axe** : B
- **Localisation** : EXIG-CON-17, p. 184 : « revue chaque année et après tout incident grave »; EXIG-CON-23, p. 187 : « Le plan de réponse aux incidents de chaque agent DOIT suivre les cinq temps de la figure 26 »
- **Diagnostic** : « incident grave » sert de déclencheur (EXIG-CON-17; réévaluation du § 11.5; grille A; indicateur « Aucun incident grave » au ch. 15), mais il n'est défini qu'au sens du RIA, qui ne s'applique qu'aux systèmes à haut risque. Le § 12.8 ne prévoit ni triage ni niveaux de gravité. Tout incident, y compris un dépassement de coût mineur, entraîne donc coupe-circuit, révocation et gel des traces, des mémoires et des versions. Les plans de réponse sont aussi définis par agent, sans plan pour les incidents systémiques : serveur MCP partagé compromis, fournisseur de modèle défaillant, cascade multiagent touchant des dizaines d'agents.
- **Contre-exemple ou scénario de défaillance** : un serveur MCP utilisé par 40 agents est compromis. Le cadre prévoit alors 40 plans distincts, 40 coupe-circuits et 40 gels, sans coordination ni propriétaire unique de l'incident. À l'inverse, un dépassement de budget de 3 % arrête un agent de production.
- **Correctif proposé** : ajouter une échelle de gravité (p. ex. S1 à S4) avec ses critères (rayon, RP, irréversibilité, régimes déclenchés), les temps obligatoires pour chaque niveau et la définition d'« incident grave » (S1-S2 ou incident grave au sens du RIA). Prévoir un plan de réponse au niveau de la plateforme pour les composants partagés (le coupe-circuit par serveur MCP d'EXIG-IAM-20 le permet déjà).
- **Confiance** : vérifié dans le texte

### [19-09] [MAJEUR] Contenir d'abord détruit des preuves volatiles que le gel n'énumère pas
- **Axe** : B
- **Localisation** : figure 26 et étapes 1-2, p. 186 : « on contient l'agent avant de chercher la cause, on fige les preuves avant de corriger »; EXIG-CON-23 : gel des « traces, du journal d'audit, des instantanés de mémoire et des versions exactes »
- **Diagnostic** : EXIG-SEC-09 exige que chaque bac à sable soit « créé pour une seule tâche ou une seule session, puis détruit ». Couper l'agent (étape 1) met fin à la session, donc détruit le bac à sable, alors que le code exécuté, les fichiers et les connexions sortantes sont souvent le vecteur de l'incident. La liste du gel omet aussi le contexte en cours d'exécution, l'état des tâches A2A déléguées (détenu par des tiers), les approbations en attente que l'étape 1 annule, et le contenu de débogage d'EXIG-OBS-08, qui est de courte durée. Les traces gelées peuvent en outre avoir été échantillonnées (EXIG-OBS-11).
- **Contre-exemple ou scénario de défaillance** : un agent exfiltre des données par un script dans son bac à sable. L'équipe de garde l'arrête, le bac à sable est détruit conformément à EXIG-SEC-09, et l'analyse des causes ne dispose plus que de spans sans contenu.
- **Correctif proposé** : faire de la contention une suspension (réseau coupé, identité désactivée) qui conserve les bacs à sable et le contexte en cours, en dérogation explicite à EXIG-SEC-09 pendant l'incident. Ajouter au gel les bacs à sable, l'état des tâches A2A (GetTask avant CancelTask) et les approbations annulées. Suspendre l'échantillonnage et les purges pour l'agent visé.
- **Confiance** : vérifié dans le texte (EXIG-SEC-09, EXIG-OBS-08, EXIG-OBS-11); l'effet de la coupure sur le bac à sable est déduit

### [19-10] [MAJEUR] « Corriger et compenser » suppose une compensabilité qu'un incident n'offre pas
- **Axe** : A
- **Localisation** : étape 4, p. 187 : « Les actions exécutées sont compensées selon le patron saga (section 7.5) »
- **Diagnostic** : (a) Les actions P3 sont par définition irréversibles ou sans compensation déclarée : l'étape ne dit rien de leurs effets résiduels (envoi externe, paiement, divulgation). (b) Le patron saga compense une saga qui a échoué; en incident, on compense des sagas réussies mais erronées, souvent anciennes, sur des données que d'autres actions légitimes ont modifiées depuis. Les compensations ne commutent pas et peuvent écraser ces modifications (T3). (c) À l'étape 1, on a révoqué les jetons et les accès de l'agent : sous quelle identité, et avec quelle autorisation, les compensations s'exécutent-elles? (d) La révocation interrompt aussi les sagas légitimes en cours, qui restent dans un état intermédiaire; le plan ne dit pas qui les reprend ou les compense.
- **Contre-exemple ou scénario de défaillance** : un agent a appliqué à tort 200 rabais (P2, compensables par une annulation). Entre-temps, 30 clients ont modifié leur commande. La compensation automatique rétablit l'ancien prix sur des commandes modifiées et efface leurs changements. Les jetons de l'agent étant révoqués, l'orchestrateur échoue d'ailleurs sur une partie des compensations.
- **Correctif proposé** : distinguer les compensations automatiques (sagas en cours au moment de la contention, sous l'identité de l'orchestrateur et non de l'agent suspendu) des réparations métier (actions terminées), qui sont décidées par le propriétaire métier, précédées d'une vérification de l'état courant et éventuellement approuvées. Ajouter un volet « effets irréversibles » : avis aux tiers, recours, mesures d'atténuation.
- **Confiance** : déduit (principes des sagas); l'identité d'exécution des compensations au § 7.5 n'a pas été vérifiée

### [19-11] [MAJEUR] L'« importance relative » des facteurs est irréalisable pour une décision d'agent à base de LLM
- **Axe** : B
- **Localisation** : EXIG-CON-21, p. 185-186 : « présente en langage clair les principaux facteurs et leur importance relative […]; le raisonnement affiché par le modèle n'en tient jamais lieu »
- **Diagnostic** : le cadre écarte, à juste titre, le raisonnement affiché, mais il n'indique pas d'où proviendraient les facteurs et leur pondération. Un LLM n'a pas de poids de facteurs interprétables, et les attributions a posteriori sont instables. L'exigence n'est réalisable que si la décision est rendue ou bornée par un composant déterministe qui expose ses facteurs (PRIN-08), ce que le texte ne prescrit pas. Le même défaut touche EXIG-CON-07 (§ 12.2), et la vérifiabilité « en revue ou en test » reste illusoire.
- **Contre-exemple ou scénario de défaillance** : un agent de préqualification de prêt (exemple du § 12.1) motive un refus. Sur demande, l'équipe ne peut produire qu'une paraphrase générée, ce que l'exigence exclut, ou une attribution SHAP sur un modèle de fondation, qui n'a rien de fiable. L'explication est donc impossible à fournir.
- **Correctif proposé** : exiger que toute décision visée par EXIG-CON-07 et EXIG-CON-21 soit rendue par une règle ou un modèle de pointage déterministe et versionné qui consigne ses facteurs et leur poids, l'agent se limitant à préparer les intrants; à défaut, interdire l'usage de l'agent pour ces décisions.
- **Confiance** : déduit (état de l'art de l'explicabilité des LLM)

### [19-12] [MINEUR] EXIG-CON-21 recoupe EXIG-CON-07 et affaiblit la règle pour les décisions partiellement automatisées
- **Axe** : C
- **Localisation** : EXIG-CON-21, p. 185 : « que la décision soit entièrement ou partiellement automatisée, DOIT indiquer le canal de révision humaine »
- **Diagnostic** : pour les décisions entièrement automatisées, EXIG-CON-07 exige déjà les RP utilisés, les facteurs, le droit de rectification, un membre du personnel nommément désigné et un délai de 30 jours. EXIG-CON-21 répète une partie de ces éléments et, pour les décisions partielles, ne précise ni le délai, ni la production des RP, ni la rectification. Pour une décision partiellement automatisée, on ne sait donc pas si le délai de 30 jours s'applique. L'extension aux décisions partielles n'est pas non plus marquée « choix du cadre » dans le bloc lui-même.
- **Contre-exemple ou scénario de défaillance** : la contestation d'une décision assistée reste sans réponse pendant 60 jours. Est-ce une non-conformité? Le texte ne permet pas de le dire.
- **Correctif proposé** : limiter EXIG-CON-21 au différentiel (« les obligations d'EXIG-CON-07 s'appliquent aussi aux décisions partiellement automatisées, choix du cadre »), ou énumérer ce qui s'applique et ce qui ne s'applique pas.
- **Confiance** : vérifié dans le texte

### [19-13] [MAJEUR] EXIG-CON-22 crée une approbation préalable obligatoire, sans portée définie et hors du treillis classe × niveau × palier
- **Axe** : A
- **Localisation** : EXIG-CON-22, p. 186 : « Tout contenu juridique, réglementaire ou contractuel produit par un agent et destiné à un usage externe (tribunal, autorité, client, partenaire) DOIT être vérifié avant sa diffusion par une personne compétente »
- **Diagnostic** : « contractuel » destiné à un « client » englobe une grande partie des réponses d'un agent de service (conditions de remboursement, garanties, modalités). L'exigence impose une vérification humaine avant diffusion, donc un fonctionnement en N2 pour ces sorties, alors qu'un agent de classe modérée a droit à N3 (EXIG-CON-02) et qu'aucun palier d'outil ne porte cette contrainte (le palier dépend de l'outil, pas de la nature du contenu). La règle vient donc s'ajouter de côté aux trois échelles (T7). « Personne compétente » n'est pas définie. Le critère de vérification (« chaque source citée existe ») est vide pour un contenu sans citation, comme une clause contractuelle rédigée.
- **Contre-exemple ou scénario de défaillance** : un agent N3 de classe modérée répond à 10 000 courriels de clients par jour, dont 30 % portent sur les conditions du contrat. Soit l'entreprise ignore EXIG-CON-22, soit elle redescend l'agent à N2 sans que le registre ou la passerelle le sache, ce qui rend le contrôle invérifiable.
- **Correctif proposé** : définir « contenu juridique » (avis juridique, acte de procédure, communication à une autorité, engagement contractuel nouveau ou modifié), exclure les réponses tirées de gabarits approuvés, rattacher l'exigence au palier P3 de l'outil d'envoi externe pour ces contenus et définir « personne compétente » (rôle inscrit à la matrice RACI).
- **Confiance** : vérifié dans le texte (EXIG-CON-02; tableau 46); conséquence opérationnelle déduite

### [19-14] [MAJEUR] Le volet « impact algorithmique » vise « tout agent », mais l'évaluation unifiée ne vise que la classe élevée
- **Axe** : A
- **Localisation** : tableau 52, p. 189, impact algorithmique : « Tout agent qui décide ou recommande à l'égard d'une personne (choix du cadre) »; EXIG-CON-26 : « Chaque agent de classe élevée DOIT disposer d'une évaluation d'impact unifiée »; § 12.9 : « un seul livrable par agent de classe élevée »
- **Diagnostic** : un agent qui recommande à l'égard d'une personne sans « effet important » (tableau 46) peut être de classe modérée. Le tableau 52 lui impose un volet d'impact algorithmique, mais EXIG-CON-26 et le tableau 46 (contrôles de la classe modérée) ne lui imposent aucune évaluation unifiée. Le volet tombe dans un vide : obligatoire selon un tableau, sans support ni approbation selon les exigences.
- **Contre-exemple ou scénario de défaillance** : un agent de classe modérée recommande à un conseiller les produits à proposer à chaque client. Le tableau 52 exige l'évaluation d'impact algorithmique, mais aucune exigence ne dit qui la produit ni qui l'approuve, ni à quel moment, et aucune revue ne la vérifie.
- **Correctif proposé** : soit restreindre le volet à la classe élevée, soit étendre EXIG-CON-26 (volet impact algorithmique seulement) à tout agent qui décide ou recommande à l'égard d'une personne, et l'ajouter aux contrôles minimaux de la classe modérée au tableau 46.
- **Confiance** : vérifié dans le texte

### [19-15] [MINEUR] Le moment d'application de la classe élevée et de l'évaluation d'impact varie selon le passage
- **Axe** : A
- **Localisation** : EXIG-CON-13, p. 182 : « DOIT être classé en classe élevée […] dès son homologation »; EXIG-CON-26, p. 189 : « avant le passage en pilote »; tableau 52 (décision sur le risque résiduel) : « Avant l'homologation »
- **Diagnostic** : au § 11.5, l'homologation est le point de contrôle de sortie du pilote. EXIG-CON-01 attribue la classe avant l'inscription au registre, et EXIG-CON-26 exige l'évaluation, volet du risque résiduel compris, avant le pilote. Avec « dès son homologation », EXIG-CON-13 laisse croire qu'un agent de l'annexe III peut piloter, avec une population réelle, sans être classé élevé. Or l'AIDF de l'art. 27 est exigée « avant la première utilisation ». Le tableau 52 et EXIG-CON-26 situent eux-mêmes la décision sur le risque résiduel à deux moments différents.
- **Contre-exemple ou scénario de défaillance** : une équipe pilote un agent de tri de candidatures (annexe III, emploi) auprès de 50 candidats avant l'homologation, en classe modérée, en invoquant EXIG-CON-13.
- **Correctif proposé** : dans EXIG-CON-13, remplacer « dès son homologation » par « dès son inscription au registre (EXIG-CON-01) »; dans le tableau 52, écrire « avant le passage en pilote, confirmée à l'homologation ».
- **Confiance** : vérifié dans le texte (§ 11.5, EXIG-CON-01, EXIG-CON-13, EXIG-CON-26, tableau 52)

### [19-16] [MINEUR] EXIG-CON-17 : métriques des seuils, « direction » et sens de l'ajustement non précisés
- **Axe** : B
- **Localisation** : EXIG-CON-17, p. 184 : « fixe, pour chaque classe, le niveau d'activités […] (contrôles, fréquence des revues, autorité d'approbation) et les seuils au-delà desquels un agent est suspendu »
- **Diagnostic** : le texte ne dit pas sur quoi portent les seuils (taux d'erreur, coût, refus de la passerelle, dérive d'évaluation) ni comment ils s'articulent avec les seuils existants (ODD de N3, budgets FinOps, paliers d'évaluation du § 10.4). La note du tableau 46 précise que la déclaration ne peut que « resserrer » les fréquences, mais EXIG-CON-17 ne le dit pas : elle « fixe ». La déclaration pourrait donc relâcher les contrôles minimaux du tableau 46. « La direction » n'est pas un rôle défini au § 11.1.
- **Contre-exemple ou scénario de défaillance** : la déclaration approuvée fixe une revue annuelle pour la classe élevée alors que le tableau 46 prévoit une revue semestrielle. Deux textes du cadre se contredisent alors, et rien ne dit lequel l'emporte.
- **Correctif proposé** : ajouter « sans être moins stricte que les tableaux 46 et 47 et les exigences du cadre », énumérer les familles de métriques de suspension et nommer l'instance d'approbation (conseil ou haute direction, comme le fait E-23).
- **Confiance** : vérifié dans le texte

### [19-17] [MINEUR] EXIG-CON-20 : « substantiellement modifié » non défini, et exception éditoriale de l'art. 50(4) écartée sans le dire
- **Axe** : A
- **Localisation** : EXIG-CON-20, p. 185 : « Tout contenu produit ou substantiellement modifié par un agent et diffusé à l'externe […] DOIT être identifié comme tel »
- **Diagnostic** : le seuil de « substantiellement » n'est pas défini, ce qui rend l'exigence invérifiable. L'art. 50(4) dispense les textes soumis à un contrôle éditorial humain; le cadre supprime cette dispense, y compris pour les brouillons N2 relus et approuvés par un employé, sans l'écrire. On ne sait pas non plus si un courriel rédigé par un agent mais envoyé sous le nom d'un employé doit porter la mention.
- **Contre-exemple ou scénario de défaillance** : deux équipes interprètent différemment une reformulation à 30 % par un copilote. Les communications de l'entreprise sont alors étiquetées de manière incohérente.
- **Correctif proposé** : définir le seuil (contenu généré dont la substance n'a pas été rédigée par une personne), dire explicitement que la relecture humaine ne dispense pas de l'identification (choix du cadre) et fixer un format d'identification par canal.
- **Confiance** : vérifié dans le texte; contenu de l'art. 50(4) : connaissance sûre

### [19-18] [MINEUR] Le résumé de l'art. 50 omet le paragraphe 3 (reconnaissance des émotions, catégorisation biométrique)
- **Axe** : A
- **Localisation** : § 12.7, p. 185 : « Les déployeurs divulguent les hypertrucages et les textes générés publiés pour informer le public »
- **Diagnostic** : l'art. 50(3) oblige les déployeurs de systèmes de reconnaissance des émotions ou de catégorisation biométrique à en informer les personnes exposées. Un agent vocal qui analyse le ton de l'interlocuteur peut y tomber. Ni le résumé ni EXIG-CON-19 et 20 ne couvrent ce cas.
- **Contre-exemple ou scénario de défaillance** : un agent de centre d'appels détecte la frustration du client pour l'acheminer vers un humain. Le client est informé qu'il parle à un agent (EXIG-CON-19), mais pas que ses émotions sont analysées.
- **Correctif proposé** : ajouter l'art. 50(3) au résumé et une phrase à EXIG-CON-19 (« et, le cas échéant, de toute analyse de ses émotions ou de ses caractéristiques biométriques »).
- **Confiance** : connaissance sûre du texte initial de l'art. 50; effet du règlement (UE) 2026/1744 à vérifier

### [19-19] [MINEUR] Portée de l'AIDF incomplète
- **Axe** : A
- **Localisation** : § 12.9, p. 188 : « obligatoire avant la première utilisation pour les déployeurs qui sont des organismes de droit public, les entités privées qui fournissent des services publics et les déployeurs de systèmes d'évaluation de la solvabilité »
- **Diagnostic** : l'art. 27(1) ne vise que les systèmes à haut risque de l'art. 6(2), à l'exception de l'annexe III, point 2 (infrastructures critiques). Le passage omet ces deux bornes : il laisse croire que tout système d'un organisme public est visé, et il ne signale pas l'exclusion des infrastructures critiques.
- **Contre-exemple ou scénario de défaillance** : une société d'État qui exploite un agent de gestion du réseau électrique (annexe III, point 2) conclut à tort qu'une AIDF est obligatoire, ou, à l'inverse, qu'un agent de classe faible l'exige.
- **Correctif proposé** : écrire « déployeurs de systèmes à haut risque visés à l'art. 6(2), sauf annexe III, point 2, qui sont… ».
- **Confiance** : connaissance sûre du texte initial; modification par le règlement (UE) 2026/1744 à vérifier

### [19-20] [MINEUR] Tableau 52 : déclencheur de l'EFVP trop large et colonne « Obligatoire lorsque » mal remplie
- **Axe** : C
- **Localisation** : tableau 52, p. 188-189 : « Projet impliquant des RP; communication hors Québec »; ligne ISO/IEC 42005 : « Méthode de référence du cadre pour tous les volets »
- **Diagnostic** : l'art. 3.3 vise les projets d'acquisition, de développement ou de refonte d'un système d'information ou d'une prestation électronique de services impliquant des RP, comme le dit correctement le § 11.5. La paraphrase du tableau est plus large et présente comme légal un déclencheur qui ne l'est pas. Dans la ligne ISO/IEC 42005, la colonne « Obligatoire lorsque » ne contient pas une condition mais une qualification.
- **Contre-exemple ou scénario de défaillance** : un lecteur exige une EFVP pour une simple modification de l'invite système d'un agent qui lit des RP, au titre de l'art. 3.3, alors que ce n'est ni une acquisition ni une refonte. Le déclencheur réel de cette mise à jour est EXIG-CON-03.
- **Correctif proposé** : reprendre le libellé du § 11.5 et marquer « (cadre) » ce qui va au-delà; dans la ligne ISO/IEC 42005, écrire « Toujours (méthode) ».
- **Confiance** : vérifié dans le texte (§ 11.5); libellé de l'art. 3.3 : connaissance sûre

### [19-21] [MINEUR] NIST AI 600-1 : « deux » risques seulement toucheraient directement les agents
- **Axe** : A
- **Localisation** : § 12.5, p. 183 : « décrit douze risques […]; deux touchent directement les agents : la configuration humain-IA […] et l'intégration de la chaîne de valeur »
- **Diagnostic** : le risque « Information Security » (injection d'invite, exfiltration), au cœur du ch. 9 et de la triade létale, la « Confabulation », motif même d'EXIG-CON-22, et « Data Privacy » touchent tout aussi directement les agents. La sélection contredit l'importance que le cadre leur donne ailleurs.
- **Contre-exemple ou scénario de défaillance** : une équipe qui construit sa déclaration d'applicabilité à partir de ce passage n'y rattache pas l'injection d'invite.
- **Correctif proposé** : écrire « au moins cinq touchent directement les agents » et rattacher chacun aux chapitres concernés (9.6, 12.7, 12.2).
- **Confiance** : intitulés des douze risques : connaissance sûre; l'appréciation est déduite

### [19-22] [MINEUR] La date du renommage de COSAiS en COSIS est déduite d'une date de mise à jour de page
- **Axe** : C
- **Localisation** : § 12.5, p. 183 : « renommé COSIS, Control Overlays for Super Intelligence Systems, le 20 octobre 2026 selon la page du projet »
- **Diagnostic** : l'annexe H (tableau de suivi NIST) ne cite comme preuve que « Updated October 20, 2026 », la date de mise à jour de la page. Que le renommage date de ce jour-là est donc une inférence, présentée comme un fait. La nouvelle appellation (« Super Intelligence ») est d'ailleurs assez inattendue pour mériter une citation littérale.
- **Contre-exemple ou scénario de défaillance** : le renommage a eu lieu plus tôt et la page a été retouchée le 20 octobre. La date consignée est alors fausse.
- **Correctif proposé** : écrire « renommé COSIS (page du projet mise à jour le 20 octobre 2026) » ou citer l'annonce.
- **Confiance** : vérifié dans le texte (annexe H); le fait externe est à vérifier

### [19-23] [MINEUR] Comité directeur technique d'A2A à « huit entreprises » (déjà consigné en H.4, no 1, mais pas pour le § 13.1)
- **Axe** : C
- **Localisation** : § 13.1, p. 189-190 : « son comité directeur technique réunit huit entreprises concurrentes : AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow »
- **Diagnostic** : l'erratum no 1 du tableau 72 corrige ce point (neuf sièges, Bloomberg depuis le 20 octobre 2026), mais sa colonne « Où » ne vise que le § 6.6. Le § 13.1 répète le même énoncé et resterait faux après application de l'erratum.
- **Contre-exemple ou scénario de défaillance** : on applique l'erratum au § 6.6 seulement, et les deux chapitres se contredisent.
- **Correctif proposé** : ajouter « § 13.1 » à la ligne 1 du tableau 72 et corriger le passage de la même façon.
- **Confiance** : vérifié dans le texte (tableau 72)

### [19-24] [MINEUR] T1 : « le risque qu'un protocole du catalogue […] passe sous le contrôle d'un seul éditeur est donc faible » est une généralisation abusive
- **Axe** : B
- **Localisation** : § 13.1, p. 190 : « Le risque qu'un protocole du catalogue disparaisse ou passe sous le contrôle d'un seul éditeur est donc faible »
- **Diagnostic** : le catalogue (§ 6.3) contient aussi l'Agentic Commerce Protocol (OpenAI et Stripe) et UCP (porté par Google), qui ne relèvent d'aucune gouvernance neutre, même s'ils sont au statut « Surveiller ». De plus, cette gouvernance « neutre » est exercée par les éditeurs de plateformes eux-mêmes (membres Platine, comité directeur technique), ceux-là mêmes chez qui le § 13.1 situe le verrouillage. Une gouvernance partagée n'empêche pas une coalition de faire évoluer les extensions à son avantage.
- **Contre-exemple ou scénario de défaillance** : un agent de paiement adopte ACP, qui est au catalogue. Le protocole évolue selon les décisions de deux entreprises.
- **Correctif proposé** : restreindre l'énoncé aux protocoles au statut « Adopter » sous fondation neutre (MCP, A2A) et nommer le risque de coalition.
- **Confiance** : vérifié dans le texte (catalogue du § 6.3)

### [19-25] [MINEUR] La contention renvoie au § 7.8, sans citer EXIG-IAM-20 ni fixer de critère de réussite
- **Axe** : C
- **Localisation** : étape 1, p. 186 : « révoque ses jetons et ses accès, suspend ses délégations en cours et annule les actions en attente d'approbation (section 7.8) »; EXIG-CON-23
- **Diagnostic** : le coupe-circuit propagé et mesuré, qui désactive l'identité sur toutes les passerelles avec un délai de révocation mesuré, est EXIG-IAM-20 (ch. 9). La grille A le rattache à EXIG-ORC-28 et EXIG-IAM-20. Ni l'étape 1 ni EXIG-CON-23 ne les citent, et aucune ne dit quand la contention est réputée acquise : jetons déjà émis (durée de vie jusqu'à 15 minutes, EXIG-IAM), tâches A2A externes qui n'honorent pas l'annulation, accès MCP en stdio local hors passerelle.
- **Contre-exemple ou scénario de défaillance** : l'équipe de garde déclare l'agent contenu, alors qu'une tâche A2A déléguée à un partenaire continue d'agir et que des jetons restent valides pendant 15 minutes.
- **Correctif proposé** : citer EXIG-IAM-20 et EXIG-ORC-28, et définir la contention comme acquise une fois le délai de révocation mesuré écoulé et l'annulation ou le refus des tâches A2A externes confirmé.
- **Confiance** : vérifié dans le texte (EXIG-IAM-20, grille A)

### [19-26] [MINEUR] Un livrable unique, des destinataires aux droits de divulgation différents
- **Axe** : B
- **Localisation** : § 12.9, p. 188 : « Un seul livrable évite que les mêmes faits soient décrits trois fois »; EXIG-CON-26
- **Diagnostic** : l'AIDF est notifiée à l'autorité de surveillance du marché, les résultats de l'EIA fédérale sont publiés, et l'EFVP et la décision sur le risque résiduel sont internes et peuvent contenir des secrets d'affaires ou de sécurité. Le texte ne dit pas comment extraire de ce livrable unique les parties communicables à chaque destinataire.
- **Contre-exemple ou scénario de défaillance** : la notification de l'AIDF à l'autorité transmet tout le livrable, y compris la section de sécurité qui décrit les garde-fous contournables.
- **Correctif proposé** : structurer le livrable en volets séparables, avec une classification de diffusion par volet.
- **Confiance** : déduit

### [19-27] [MINEUR] « Versions exactes du modèle » : impossible à figer pour un modèle hébergé par un fournisseur
- **Axe** : B
- **Localisation** : étape 2, p. 186, et EXIG-CON-23 : « le gel […] des versions exactes de l'agent, du modèle, des invites et des définitions d'outils »
- **Diagnostic** : pour un modèle consommé par API, l'entreprise ne peut figer que l'identifiant. Le fournisseur peut retirer le modèle avant la fin de l'enquête, ce qui empêche de rejouer l'incident. Rien ne relie ce gel aux clauses fournisseurs du § 13.3.
- **Contre-exemple ou scénario de défaillance** : le modèle en cause est déprécié 30 jours après l'incident, et l'analyse des causes ne peut plus reproduire le comportement.
- **Correctif proposé** : préciser « identifiant et instantané du modèle (si autohébergé), ou engagement contractuel de rétention ou d'accès en cas d'incident (§ 13.3) ».
- **Confiance** : déduit

### [19-28] [MINEUR] La figure 26, séquentielle, ignore les horloges de notification qui courent dès la prise de connaissance
- **Axe** : A
- **Localisation** : figure 26, p. 186 : « Les cinq temps se lisent de gauche à droite »; tableau 51 (BSIF : 24 h; RIA : 2 jours)
- **Diagnostic** : la lecture séquentielle place l'avis (temps 3) après la contention et un gel complet des preuves, qui peut prendre du temps. Or les délais du BSIF (24 h) et du RIA (2 jours dans les cas graves) courent dès la prise de connaissance. Inversement, pour un système à haut risque, l'art. 73(6) interdit d'altérer le système avant d'avoir informé les autorités; ce verrou devrait conditionner explicitement le temps 4, et EXIG-CON-23 n'impose que le gel avant la correction.
- **Contre-exemple ou scénario de défaillance** : le gel des mémoires et des traces de 12 agents prend 30 heures, et l'avis au BSIF est envoyé en retard.
- **Correctif proposé** : dire que la qualification et le premier avis (temps 3) démarrent en parallèle dès la contention, et que, pour un incident grave au sens du RIA, aucune correction qui altère le système n'est faite avant l'avis.
- **Confiance** : vérifié dans le texte; art. 73(6) : connaissance sûre

## Points forts
Les sous-catégories NIST, les mesures ISO/IEC 42001 (A.5, A.6.2.6, A.6.2.8, A.7, A.9, A.10) et les délais de l'art. 73 du RIA sont cités avec exactitude, et les confusions courantes (A.7, MANAGE 3.x) sont relevées explicitement. La distinction entre « exigence externe » et « choix du cadre » est tenue partout (72 h, art. 50 étendu). Le tableau 53 localise le verrouillage par des mécanismes datés plutôt que par des jugements sur des produits.

## Questions pour l'audit bibliographique
- p. 182-183 : AI RMF « en cours de révision » dans le cadre du plan d'action américain, « examen formel au plus tard en 2028 » (NIST AI 100-1, § « Next steps »; page [448]).
- p. 183 : CAISI AI Agent Standards Initiative « lancée le 17 février 2026 »; COSAiS renommé « COSIS, Control Overlays for Super Intelligence Systems » et date réelle du renommage [411, 455]; note de concept du 7 avril 2026 sur un profil pour les infrastructures critiques [456].
- p. 183 : ISO/IEC 42001 publiée le 18 décembre 2023; ISO/IEC 22989, terme « AI agent » au 3.1.1; ISO/IEC 42006:2025 [395, 451, 453].
- p. 185 : délai transitoire de l'art. 50(2) au 2 décembre 2026 selon le règlement (UE) 2026/1744 (voir aussi H.4); art. 27(4) « tel que modifié » (p. 188) [57, 461].
- p. 186 : Specter Aviation c. Laprade, 2025 QCCS 3521, sanction de 5 000 $ au titre de l'art. 342 C.p.c. [458].
- p. 186 : CAI 2024-2025 : 514 avis, hausse de 16 %, 80 % du secteur privé, 251 accès non autorisés [424].
- p. 187 : nombre d'éléments de l'avis à la CAI (« onze ») selon le Règlement sur les incidents de confidentialité, et numérotation des articles cités dans le pourquoi d'EXIG-CON-24 (« articles 7 et 8 du règlement » : registre et conservation figurent peut-être aux art. 6 et 7) [460].
- p. 187 : avis du BSIF sur le signalement des incidents liés à la technologie et à la cybersécurité : date de la version en vigueur (« 2021 ») et délai de 24 heures [62].
- p. 187 : LPRPDE : conservation du registre pendant 24 mois; avis aux organisations susceptibles de réduire le risque (art. 10.2).
- p. 190 : AAIF : membres Platine; A2A projet hébergé le 17 août 2026; candidature d'AGNTCY sans décision au 27 octobre 2026 [4, 5, 35, 37, 42].
- p. 190 : exemples du tableau 53 : Azure API Management (outils MCP seulement, A2A en JSON-RPC seulement) [108, 109]; Kong AI A2A Proxy 3.14 [111]; Agentforce (un niveau, sept sous-agents) [49]; Entra Agent ID d'office depuis juillet 2026 [48]; Agent 365 [46, 324]; Copilot Studio, seuil de 125 % [53]; extensions MCP à préfixe DNS inversé, désactivées par défaut [169].
