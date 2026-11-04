# Audit chunk_24 — pages 231-242

## Synthèse
Le chunk couvre l'annexe E (glossaire, tableau 65, p. 231-241) et le début de l'annexe F (F.1-F.2, p. 241-242). Le glossaire est dense, ses renvois de section sont tous justes et son ordre alphabétique est cohérent; il reprend toutefois plusieurs règles du corps sous une forme tronquée qui, lue seule, change la règle. Les trois défauts les plus graves : (1) la « règle de deux » est reformulée sur les trois propriétés de Willison, ce qui masque que les écritures P2 restent permises après une lecture non fiable; (2) la « session », sur laquelle reposent le retrait déterministe et la règle de deux, n'est définie nulle part alors que MCP 2026-07-28 est sans état; (3) l'intersection « droits du mandant ∩ … » est confiée au seul serveur d'autorisation, qui ne connaît pas les droits fins du mandant. Recouvrement : les constats purement locaux des p. 231-232 et 241-242 (p. ex. 428 + 49 ≠ 473 références; 705 sources « pour la version finale » contre 473 en annexe G; annexe F « fonde la version 1.0 » datée du 27 octobre alors que l'audit final date du 28) sont laissés aux chunks 23 et 25.

## Constats

### [24-01] [MAJEUR] La « règle de deux » du glossaire omet le changement d'état, et le retrait laisse les écritures P2 disponibles
- **Axe** : A
- **Localisation** : annexe E, « Contenu non fiable », p. 234 : « sa lecture entraîne le retrait des outils d'envoi externe et des outils P3 pour le reste de la session »; « Triade létale », p. 241 : « au plus deux des trois propriétés sans supervision ».
- **Diagnostic** : dans le glossaire, « les trois propriétés » sont celles de Willison (données privées, contenu non fiable, communication externe). Or la règle de Meta, telle que le corps la cite (§ 9.6, p. 133), a pour troisième propriété « [C] changer un état ou communiquer vers l'extérieur ». EXIG-SEC-06 (p. 135), que le glossaire résume, ne retire que l'envoi externe et le P3. Après une lecture non fiable, un agent N3 garde donc ses écritures P2 sous le seuil, sans supervision : il réunit [A], [B] et [C] au sens de Meta. Le glossaire valide implicitement ce cas, puisque « changer un état » n'y figure pas. Le retrait est en outre largement redondant : P3 couvre déjà « externe ou irréversible » et exige toujours une approbation (« jamais exécutée seule »). Son apport réel se limite aux sorties hors liste d'autorisation, et ne touche pas le canal P2.
- **Contre-exemple ou scénario de défaillance** : un agent N3 de rapprochement lit une facture fournisseur piégée (contenu non fiable) puis, sous le seuil P2, modifie le champ « coordonnées bancaires » du fournisseur dans l'ERP (écriture compensable). Aucun outil d'envoi n'est appelé, donc rien n'est retiré. Le prochain paiement, approuvé par une personne qui ne voit qu'un montant habituel, part vers le compte de l'attaquant. Autre canal : un agent écrit en P2 dans un document partagé qu'un autre agent, non contaminé et doté d'envoi externe, relaie ensuite (propagation inter-agents, T4).
- **Correctif proposé** : dans le glossaire, citer la règle de Meta avec son [C] exact. Dans EXIG-SEC-06, étendre le retrait (ou l'exigence d'approbation liée à l'action) aux écritures P2 qui touchent des champs sensibles marqués au catalogue (coordonnées de paiement, destinataires, droits), ou abaisser la session contaminée à N2. Ajouter un cas négatif d'essai « écriture P2 après lecture non fiable ».
- **Confiance** : vérifié dans le texte (glossaire, § 9.6, EXIG-SEC-06); scénario déduit.

### [24-02] [MAJEUR] « Session » : terme pivot jamais défini, alors que MCP retenu est sans état
- **Axe** : A / C
- **Localisation** : annexe E, « Contenu non fiable », p. 234 : « pour le reste de la session »; « MCP », p. 238 : « Le cadre retient la révision 2026-07-28, sans état »; « Triade létale », p. 241 : « une règle de session ».
- **Diagnostic** : le retrait déterministe (EXIG-SEC-06), la règle de deux « par session » et l'isolement des bacs à sable « par session » dépendent tous d'une frontière de session que la passerelle doit tenir. Ni le glossaire ni le § 3.1 ne la définissent (le mot revient 66 fois dans le texte; aucune occurrence de définition). MCP 2026-07-28 retire justement les sessions du protocole (§ 6.5, p. 57), donc la passerelle ne peut pas s'appuyer sur celles du protocole. Question non tranchée : une session, est-ce une tâche (task_id), une conversation, un contextId A2A, une instance d'orchestrateur avec ses exécutants? La propagation de la contamination d'un exécutant vers son orchestrateur, ou d'une tâche reprise après un point de contrôle (exécution durable), reste indéterminée.
- **Contre-exemple ou scénario de défaillance** : l'agent contaminé termine sa tâche, dont le point de contrôle conserve le texte injecté, puis la reprise ou une nouvelle tâche ouverte par l'orchestrateur repart avec une « session » neuve et récupère ses outils d'envoi. Le « nouveau départ dans un contexte vierge » de Meta devient un moyen de contourner le retrait si la mémoire épisodique ou le point de contrôle transporte le contenu.
- **Correctif proposé** : ajouter au § 3.1 et au glossaire une entrée « Session (de passerelle) » : clé de corrélation (p. ex. task_id racine), héritage de l'état contaminé par les sous-tâches, les reprises et les réponses d'exécutants, conditions de « contexte vierge » (aucune mémoire ni point de contrôle contaminé rechargé).
- **Confiance** : vérifié dans le texte (absence de définition, MCP sans état); scénario déduit.

### [24-03] [MAJEUR] L'intersection « droits du mandant ∩ … » confiée au seul serveur d'autorisation n'est pas réalisable pour les droits fins
- **Axe** : A
- **Localisation** : annexe E, « Jeton délégué », p. 237 : « droits du mandant ∩ portée de l'agent ∩ portée de la tâche (choix du cadre), intersection appliquée par le serveur d'autorisation à chaque échange ».
- **Diagnostic** : un serveur d'autorisation émet des portées (scopes, au mieux des authorization_details RFC 9396). Les « droits du mandant » sont le plus souvent des droits sur les données, tenus par le système d'enregistrement (unité, dossier, montant). Le serveur d'autorisation ne les connaît pas et ne peut pas les intersecter. Le corps (§ 9.3, p. 124) justifie ce placement en disant que la RFC 8693 interdit de fonder l'accès sur les acteurs antérieurs. C'est un non-sequitur pour le terme « mandant » : le mandant est le sub, que le serveur de ressources peut et doit contrôler; seuls les act imbriqués sont informatifs. Telle qu'écrite, la règle dispense implicitement le serveur de ressources de contrôler les droits du sub.
- **Contre-exemple ou scénario de défaillance** : exemple du corps : Alice ne voit que son unité; l'agent détient finance:read. Le serveur d'autorisation émet finance:read (intersection de portées correcte), mais rien dans le jeton n'encode « unité d'Alice, T3 ». Si l'API financière se fie au jeton, l'agent lit les dépenses de toutes les unités. Même chose si Alice perd un droit dans l'ERP après l'émission : le serveur d'autorisation n'en sait rien pendant la durée de vie du jeton.
- **Correctif proposé** : réécrire : « le serveur d'autorisation borne la portée (portée de l'agent ∩ portée de la tâche ∩ portées délégables du mandant); le serveur de ressources applique les droits du mandant (sub) sur les données à chaque appel ». Exiger que le sub soit toujours évalué par la cible, et un test négatif inter-unités.
- **Confiance** : déduit (le constat vaut aussi pour EXIG-IAM-10, § 9.3, chunk 13).

### [24-04] [MINEUR] Intersection à deux termes (PRIN-03) contre trois termes (glossaire, § 9.3)
- **Axe** : C
- **Localisation** : annexe E, « Jeton délégué », p. 237 : « droits du mandant ∩ portée de l'agent ∩ portée de la tâche »; PRIN-03, p. 26 : « l'intersection des droits du mandant et de ceux de l'agent ».
- **Diagnostic** : le principe normatif, supérieur dans la préséance, énonce une intersection à deux termes; le glossaire et EXIG-IAM-10, une intersection à trois. C'est compatible (trois termes donnent un ensemble plus petit), mais la formule de référence diffère d'un endroit à l'autre.
- **Contre-exemple ou scénario de défaillance** : un auditeur qui vérifie la conformité à PRIN-03 accepte un jeton à portée « tous les droits délégables de l'agent » pour une tâche étroite.
- **Correctif proposé** : aligner la conséquence de PRIN-03 sur la formule à trois termes, ou renvoyer explicitement à EXIG-IAM-10.
- **Confiance** : vérifié dans le texte.

### [24-05] [MINEUR] « Contenu non fiable » : le glossaire durcit et déforme EXIG-SEC-03 et SEC-06
- **Axe** : C
- **Localisation** : annexe E, p. 234 : « Tout contenu qui ne provient ni du mandant authentifié […] documents téléversés […] sa lecture entraîne le retrait des outils d'envoi externe et des outils P3 pour le reste de la session ».
- **Diagnostic** : trois écarts avec le corps. (a) EXIG-SEC-03 (p. 133) précise « documents téléversés (y compris par le mandant) ». Le glossaire omet cette précision, et sa formule « ni du mandant authentifié » laisse croire qu'un document fourni par le mandant serait fiable. (b) EXIG-SEC-06 prévoit qu'« une action ainsi retirée ne s'exécute qu'avec une approbation humaine liée à l'action exacte ». Le glossaire présente le retrait comme absolu. (c) Le déclencheur est, dans le corps, le marquage au catalogue des outils dont la sortie peut contenir du contenu de tiers. Le glossaire suggère que toute « réponse d'outil » déclenche le retrait, ce qui le déclencherait dès le premier appel d'outil, dans presque toutes les sessions.
- **Contre-exemple ou scénario de défaillance** : un concepteur qui ne lit que le glossaire refuse une conception légitime (paiement P3 approuvé après lecture d'une facture), ou traite le PDF téléversé par le mandant comme fiable.
- **Correctif proposé** : reprendre les trois éléments : « y compris par le mandant », exception d'approbation liée à l'action, déclenchement par le marquage du catalogue. Et lever dans le corps l'ambiguïté entre « toute réponse d'outil est non fiable » (SEC-03) et « seuls les outils marqués déclenchent le retrait ».
- **Confiance** : vérifié dans le texte.

### [24-06] [MINEUR] « Classe de risque » ignore l'article 65.2, ajouté en v1.1
- **Axe** : C
- **Localisation** : annexe E, p. 233 : « qui comprend les systèmes à haut risque du RIA et les décisions visées par l'article 12.1 de la Loi sur le privé ».
- **Diagnostic** : l'historique des versions (v1.1, p. 2) indique « article 65.2 de la Loi sur l'accès ajouté aux critères de la classe élevée » et liste les modifications corrélatives (sommaire, figure 1, § 1.1, 3.1, 4.1, 14.2, EXIG-AUT-02, annexe F), sans l'annexe E. Le glossaire n'a pas suivi. Le tableau 46 (p. 171) cite bien l’article 65.2.
- **Contre-exemple ou scénario de défaillance** : un organisme public classe en « modérée » un agent qui prend des décisions exclusivement automatisées, en se fiant au glossaire.
- **Correctif proposé** : ajouter « ou par l'article 65.2 de la Loi sur l'accès (organismes publics) ».
- **Confiance** : vérifié dans le texte.

### [24-07] [MINEUR] « Compensation » : « seulement après l'épuisement des réessais » contredit la règle 4 du § 7.5
- **Axe** : C
- **Localisation** : annexe E, p. 233 : « déclenchée seulement après l'épuisement des réessais ».
- **Diagnostic** : selon le § 7.5 (p. 95, règle 4), on compense « après épuisement des réessais ou devant une erreur non transitoire ». Le « seulement » du glossaire exclut ce second cas et impose de réessayer une erreur définitive, comme un refus métier.
- **Contre-exemple ou scénario de défaillance** : une réservation refusée pour « stock inexistant » est réessayée jusqu'à l'épuisement de la politique de réessai, ce qui retarde les compensations C2 et C1 et prolonge l'état incohérent visible par d'autres sagas.
- **Correctif proposé** : « déclenchée lorsque la progression devient impossible : réessais épuisés ou erreur non transitoire ».
- **Confiance** : vérifié dans le texte.

### [24-08] [MINEUR] « Empreinte » : formule de liaison amputée de l'identifiant pleinement qualifié et encodage de « ‖ » non spécifié
- **Axe** : A / C
- **Localisation** : annexe E, p. 235 : « h = SHA-256(identifiant de l'outil ‖ arguments canonisés) »; « calculé sur un contenu canonisé selon la RFC 8785 ».
- **Diagnostic** : le § 8.5 (p. 111) précise que l'identifiant est « pleinement qualifié (serveur, nom et version épinglée) ». Le glossaire l'omet : une lecture isolée autorise un identifiant nu, qui rend une approbation réutilisable entre deux serveurs exposant un outil du même nom, ou entre deux versions. Par ailleurs, ni le glossaire ni le § 8.5 ne fixent l'encodage de « ‖ » (octets UTF-8? séparateur? préfixe de longueur?), alors que la clé d'idempotence utilise un séparateur explicite « | » (p. 97). L'entrée dit aussi que l'empreinte est « calculée sur un contenu canonisé selon la RFC 8785 », alors que l'identifiant d'outil n'est pas du JSON : seule la partie arguments l'est.
- **Contre-exemple ou scénario de défaillance** : deux implémentations (passerelle et service d'approbation) concatènent différemment, avec ou sans séparateur : toutes les approbations sont refusées (échec fermé). Ou bien, avec un identifiant nu, une approbation donnée pour `crm/close_account` sur le serveur A est acceptée sur le serveur B.
- **Correctif proposé** : dans le glossaire, « identifiant pleinement qualifié (serveur, nom, version épinglée) ». Dans le § 8.5 et l'annexe C, définir l'entrée du hachage, par exemple SHA-256 de JCS({"tool": id, "args": arguments}), ce qui supprime l'ambiguïté de concaténation.
- **Confiance** : vérifié dans le texte (omission); ambiguïté d'encodage déduite.

### [24-09] [MINEUR] RFC 8785 inscrite deux fois au registre des références ([236] et [308])
- **Axe** : C
- **Localisation** : annexe E, « Empreinte », p. 235 : « RFC 8785 (JCS), RFC informative de la filière indépendante[236] »; § 8.5, p. 111, même fait cité [308].
- **Diagnostic** : l'annexe G contient [236] « Rundgren, Jordan, Erdtman (juin 2020). RFC 8785 – JSON Canonicalization Scheme » et [308], même référence. Le doublon fausse le décompte « 473 références » de F.1 et crée une dérive de citation entre le glossaire et le corps.
- **Contre-exemple ou scénario de défaillance** : l'audit bibliographique compte 473 références distinctes alors qu'il n'y en a que 472 (au moins).
- **Correctif proposé** : fusionner sur un numéro, sans le réattribuer : marquer l'autre « voir [n] ». Corriger le décompte de F.1.
- **Confiance** : vérifié dans le texte (full.txt, entrées [236] et [308]).

### [24-10] [MINEUR] Qui révise le catalogue des protocoles : le comité ou l'architecture d'entreprise?
- **Axe** : C
- **Localisation** : annexe E, « Catalogue des protocoles », p. 233 : « Le comité le révise au moins chaque trimestre ».
- **Diagnostic** : EXIG-GOV-18 (p. 169) : « L'architecture d'entreprise DOIT réviser le catalogue des protocoles au moins chaque trimestre et soumettre les changements de statut à l'approbation du comité ». L'entrée « Comité », p. 233, dit bien « approuve le catalogue ». Le glossaire, comme le § 6.3 (p. 51, « Le comité révise le catalogue chaque trimestre »), attribue la révision au comité.
- **Contre-exemple ou scénario de défaillance** : en RACI, chacun croit que l'autre fait la revue trimestrielle; l'exigence n'a pas de responsable clair.
- **Correctif proposé** : « révisé par l'architecture d'entreprise au moins chaque trimestre; changements de statut approuvés par le comité » (et même correction au § 6.3).
- **Confiance** : vérifié dans le texte.

### [24-11] [MINEUR] Deux « plafonds » d'autonomie, et un N0 « hors portée agentique » passé sous silence
- **Axe** : C
- **Localisation** : annexe E, « Niveau d'autonomie », p. 238 : « Plafond déclaré au registre, de N0 à N4 »; « Classe de risque », p. 233 : « Elle fixe le plafond d'autonomie ».
- **Diagnostic** : le même mot désigne le niveau déclaré de l'agent et le plafond de la classe (EXIG-CON-02), qui le borne. PRIN-04 (p. 26) dit même que le niveau est « un plafond déclaré au registre et fixé par la classe de risque », ce qui confond les deux : la classe fixe un maximum, le niveau se choisit en dessous. Le glossaire n'indique pas non plus que N0 est « hors portée agentique » (§ 3.1, p. 22). Or l'entrée « Agent » exige un modèle, et l'entrée « Système d'IA » (p. 241) considère « tout agent comme un système d'IA ». Une fiche N0 au registre est-elle un agent?
- **Contre-exemple ou scénario de défaillance** : un agent de classe faible déclaré N2 se croit autorisé à monter en N3 sans réhomologation, parce que « le plafond » (celui de la classe) est N3.
- **Correctif proposé** : « Niveau d'autonomie : niveau déclaré au registre, borné par le plafond de la classe (EXIG-CON-02) »; ajouter « N0 : repère hors portée agentique ».
- **Confiance** : vérifié dans le texte.

### [24-12] [MINEUR] Dérogation interdite pour « un agent sans fiche ni parrain » : la conjonction laisse passer le cas fiche sans parrain
- **Axe** : A
- **Localisation** : annexe E, « Dérogation », p. 234-235 : « Aucune dérogation n'est possible pour […] un agent sans fiche ni parrain ».
- **Diagnostic** : prise à la lettre, « sans A ni B » vise l'agent qui n'a ni fiche ni parrain. Un agent doté d'une fiche mais sans parrain sort de la liste non dérogeable. Le § 4.3 (p. 30) dit pourtant « un agent sans personne nommée qui en répond », condition suffisante à elle seule. EXIG-GOV-17 reprend la même tournure ambiguë.
- **Contre-exemple ou scénario de défaillance** : à la mutation du parrain, l'architecture d'entreprise accorde une dérogation de 90 jours (classe faible) pour exploiter l'agent sans personne imputable, en invoquant la lettre d'EXIG-GOV-17.
- **Correctif proposé** : « un agent sans fiche au registre, ou sans parrain nommé ».
- **Confiance** : vérifié dans le texte; lecture adverse déduite.

### [24-13] [MINEUR] « Mandant » peut être un agent, ce qui brouille sub et act dans le jeton délégué
- **Axe** : C
- **Localisation** : annexe E, « Mandant », p. 237 : « Personne, application ou agent au nom duquel une tâche est exécutée »; « Jeton délégué », p. 237 : « Il désigne le mandant (sub) et l'agent courant (act), avec un act imbriqué par acteur antérieur ».
- **Diagnostic** : si un agent peut être mandant, lorsqu'un orchestrateur délègue à un exécutant, le sub du jeton reste-t-il la personne d'origine (l'orchestrateur devenant un act imbriqué), ou devient-il l'orchestrateur? Les deux lectures changent les droits effectifs : « les droits d'un agent ne dépassent jamais les siens » se rapporte alors à l'agent, pas à la personne. « Délégation » (p. 234) parle de transfert « d'un mandant vers un agent, ou d'une tâche d'un agent vers un autre », ce qui suggère que l'agent délégant n'est pas mandant.
- **Contre-exemple ou scénario de défaillance** : un exécutant reçoit un jeton dont le sub est l'orchestrateur (droits larges du registre) et non Alice : l'intersection perd le terme « Alice ».
- **Correctif proposé** : préciser que le mandant d'une chaîne est toujours l'entité d'origine (personne, ou service d'un déclencheur système), et qu'un agent intermédiaire n'apparaît que comme act.
- **Confiance** : vérifié dans le texte; conséquence déduite.

### [24-14] [MINEUR] « Passerelle d'agents » : mandataire inverse pour le trafic sortant, et journalisation placée en fin de séquence
- **Axe** : C / A
- **Localisation** : annexe E, p. 239 : « Mandataire inverse placé devant tous les serveurs MCP et tous les pairs A2A, pour le trafic entrant comme sortant […] puis trace et journalise ».
- **Diagnostic** : un mandataire inverse protège des serveurs; le trafic sortant (agent interne vers pair A2A externe) relève d'un mandataire direct, ou de sortie. Le corps (§ 9.4, p. 128) ne dit que « mandataire inverse devant les serveurs MCP et les pairs A2A ». Par ailleurs, la séquence place la journalisation après l'exécution. Si la passerelle tombe entre l'effet et l'écriture du journal, l'action n'est pas auditée, alors que le cadre exige ailleurs d'écrire avant d'agir (compensation, § 7.5, règle 1). Le glossaire ne précise pas si une entrée d'intention précède l'appel.
- **Contre-exemple ou scénario de défaillance** : un appel P2 réussit, la passerelle est redémarrée avant d'écrire le journal; le journal d'audit « inaltérable » ne contient aucune trace de l'écriture.
- **Correctif proposé** : « mandataire placé sur tout le trafic MCP et A2A, en entrée (inverse) comme en sortie (direct) »; préciser « journalise l'intention avant l'appel et le résultat après » (à confirmer dans le § 10.3).
- **Confiance** : vérifié dans le texte (formulation); risque de journalisation déduit, ordre réel du § 9.4 non relu en entier.

### [24-15] [MINEUR] « Évaluation continue en trois paliers » : collision avec les paliers d'outil P0-P3
- **Axe** : C
- **Localisation** : annexe E, p. 235 : « en trois paliers : tests de contrats, jeux de trajectoires, y compris adverses, et échantillon du trafic réel ».
- **Diagnostic** : le § 3.1 insiste pour ne jamais confondre les échelles. Or « palier » est le terme réservé au palier d'outil (P0-P3), qui a sa propre entrée de glossaire (p. 239).
- **Contre-exemple ou scénario de défaillance** : « palier 3 de l'évaluation » se lit comme « évaluation des outils P3 ».
- **Correctif proposé** : « trois étages » ou « trois volets », ici et au § 10.4.
- **Confiance** : vérifié dans le texte.

### [24-16] [MINEUR] EFVP et décisions automatisées : volet public incomplet et citation manquante
- **Axe** : C
- **Localisation** : annexe E, « EFVP », p. 235 : « Évaluation exigée par la Loi sur le privé […] (art. 3.3) […] (art. 17)[160] »; « Décision fondée exclusivement… », p. 234 : « Selon l'interprétation gouvernementale de l'article 65.2 […][160] ».
- **Diagnostic** : le cadre vise aussi les organismes publics (art. 65.2, classe élevée), mais l'entrée EFVP ne cite que la Loi sur le privé et omet l'art. 63.5 de la Loi sur l'accès, que le corps cite (p. 177). L'interprétation gouvernementale de l'article 65.2 est appuyée, dans le corps, par la référence [318]; le glossaire ne cite que [160], la Loi sur le privé, qui ne contient pas cette interprétation.
- **Contre-exemple ou scénario de défaillance** : un lecteur d'organisme public conclut que l'EFVP ne le concerne pas; un vérificateur ne trouve pas l'interprétation dans [160].
- **Correctif proposé** : ajouter « (pour un organisme public, art. 63.5 de la Loi sur l'accès) » et citer [318] dans l'entrée « Décision ».
- **Confiance** : vérifié dans le texte (références [160] et [318] en annexe G).

### [24-17] [MINEUR] « Idempotence » : le glossaire omet le rejet d'une clé réutilisée avec d'autres arguments
- **Axe** : A
- **Localisation** : annexe E, p. 236 : « une clé d'idempotence dérivée des identifiants de la tâche et de l'étape, réutilisée à chaque réessai et vérifiée par le service visé ».
- **Diagnostic** : une clé fondée sur task_id et step_id seulement ne distingue pas un réessai d'un appel aux arguments modifiés sous la même étape. Le corps (p. 97) le traite : « même clé, arguments différents → rejet (422) », et une étape replanifiée prend un nouveau step_id. Le glossaire, qui énonce l'exigence du cadre, omet cette moitié de la propriété.
- **Contre-exemple ou scénario de défaillance** : l'agent corrige un montant (1 000 $ au lieu de 10 000 $) sans changer de step_id; le service renvoie le résultat mis en cache du premier appel, et l'agent croit le montant corrigé.
- **Correctif proposé** : ajouter « le service rejette une clé déjà vue avec des arguments différents; une étape replanifiée reçoit un nouvel identifiant ».
- **Confiance** : vérifié dans le texte.

### [24-18] [MINEUR] « PEP » : rôle d'administrateur de politiques (PA) non attribué
- **Axe** : C
- **Localisation** : annexe E, p. 239 : « la passerelle d'agents et la passerelle de modèles sont des PEP, et le service de politiques tient le rôle de PE ».
- **Diagnostic** : l'entrée reprend la triade PE/PA/PEP de NIST SP 800-207 mais n'affecte pas le PA, le composant qui établit ou coupe le chemin et émet les justificatifs de session. Dans le cadre, ce rôle semble partagé entre le fournisseur d'identité, le serveur d'autorisation (échange de jetons) et le coupe-circuit. Sans affectation, la correspondance avec la SP 800-207 est incomplète.
- **Contre-exemple ou scénario de défaillance** : en revue de conformité zéro confiance, l'auditeur ne peut pas situer qui révoque un chemin établi lorsqu'une politique change.
- **Correctif proposé** : « le serveur d'autorisation et le fournisseur d'identité tiennent le rôle de PA » (ou le rôle retenu par le § 9.1).
- **Confiance** : déduit (attribution au § 9.1 non relue).

### [24-19] [MINEUR] Critère outil/agent : « entrées et sorties définies » ne départage pas un agent A2A à compétences typées
- **Axe** : A
- **Localisation** : annexe E, « Outil », p. 238-239 : « un outil n'a aucune autonomie de décision. Règle du cadre : une cible aux entrées et aux sorties définies est un outil, même si elle emploie un modèle en interne ».
- **Diagnostic** : deux critères coexistent : l'absence d'autonomie de décision et le caractère défini des entrées et des sorties. Une cible qui emploie un modèle en interne peut décider (choisir une branche, refuser). Inversement, un agent A2A publie des compétences avec modes d'entrée et de sortie déclarés, et peut avoir des schémas. Le critère « entrées et sorties définies » ne tranche pas pour une cible qui raisonne sur plusieurs tours, mais derrière une interface typée. Or le choix MCP ou A2A en découle, et donc le palier, la carte et la machine à états.
- **Contre-exemple ou scénario de défaillance** : un service « analyse de contrat » à schéma fixe, qui itère en interne avec un modèle et des outils, est inscrit comme outil MCP P1. Ses propres appels d'outils échappent alors au registre des agents et au plafond d'autonomie.
- **Correctif proposé** : critère décisif explicite : une cible est un agent dès qu'elle choisit elle-même des actions à effet, ou conserve un état entre appels; sinon c'est un outil, même si elle emploie un modèle.
- **Confiance** : vérifié dans le texte; cas limite déduit.

## Points forts
Renvois de section exacts dans toutes les entrées des p. 233-240, ordre alphabétique cohérent avec la convention annoncée (accents, apostrophes, espaces).
Distinction systématique entre « exigence externe » et « choix du cadre », et mises en garde justes (annotations MCP non fiables, Idempotency-Key encore à l'état de brouillon, conventions GenAI en Development, OAuth 2.1 non publié).
Faits techniques vérifiables d'après mes connaissances : attributs requis de CloudEvents, RFC 8693 (delegation et impersonation), RFC 8705 et 9449, CIBA, 38 mesures de l'annexe A d'ISO/IEC 42001, mémoire CoALA, articles 3.1, 3.3 et 17 de la Loi sur le privé.

## Questions pour l'audit bibliographique
- p. 234 : « interprétation gouvernementale de l'article 65.2 » (intervention humaine mineure) : confirmer le texte et la date de [318].
- p. 234 : CAEP du Shared Signals Framework [344] : statut final (1.0) et date.
- p. 236 : OWASP Non-Human Identities Top 10 (2025) [470] : édition et intitulés NHI1-NHI10.
- p. 236 : brouillon IETF Idempotency-Key, version -08 du 22 octobre 2026 [78] : existence et numéro.
- p. 238 : OAuth 2.1, version -16 de septembre 2026 [176] (expiration annoncée le 7 mars 2027, p. 52) : vérifier sur datatracker.
- p. 238 : MCP « versionné par date », annonce du 25 novembre 2024 et transfert du 9 décembre 2025 [20, 34] (conforme à mes connaissances); révision 2026-07-28 sans état [33] : à confirmer.
- p. 239 : OWASP Top 10 for Agentic Applications publié le 9 décembre 2025 [28, 345] : date exacte de publication (9 ou 10 décembre).
- p. 239 : « parrain » (sponsor) de Microsoft Entra Agent ID : terminologie du produit à vérifier.
- p. 240 : registre officiel MCP « en préversion » au 27 octobre 2026 [43] : statut à cette date.
- p. 240 : règlement (UE) 2026/1744 : numéro, dates de report (2 décembre 2027, annexe III; 2 août 2028, annexe I).
- p. 240 : brouillon IETF WIMSE « AI Identity Management System » (AIMS) : existence et rattachement au groupe WIMSE.
- p. 240 : ISO/IEC 42006:2025 (exigences pour les organismes de certification d'un SMIA) : date de publication.
- p. 241 (couture) : « règle de deux » de Meta, 31 octobre 2025 [307] : date et libellé exact de la propriété [C].

audit_24.md : 19 constats (0 BLOQUANT, 3 MAJEUR, 16 MINEUR)
