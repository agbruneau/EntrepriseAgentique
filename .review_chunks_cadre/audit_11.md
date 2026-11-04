# Audit chunk_11 — pages 101-112

## Synthèse
Le chunk couvre la fin du § 7.10 (tableau 27, EXIG-ORC-29 et -30, pages de recouvrement) et le cœur du chapitre 8 : échelle N0-N4/NX (figure 14, tableaux 28-29), critères (tableau 30, AUT-06, AUT-07), paliers P0-P3 (tableau 31, AUT-08, AUT-09), grille classe × palier (figure 15, AUT-10, AUT-11) et jeton d'approbation (figure 16, AUT-12 à AUT-15). Le texte est dense, bien sourcé et honnête sur ce qui relève d'un « choix du cadre ». Les trois défauts les plus graves : (1) l'empreinte h, calculée sur des arguments réanalysés puis canonisés, n'interdit pas un différentiel d'analyse JSON entre passerelle et serveur d'outil, ce qui permet d'exécuter un appel P3 autre que celui approuvé; (2) la règle « le plus strict l'emporte » (AUT-10) n'est pas définie sur des contrôles non comparables, et les seuils n'ont aucune unité d'agrégation, d'où un contournement par fractionnement; (3) l'application est confiée à la seule passerelle (AUT-01, -10, -11, -12), alors qu'EXIG-IAM-17 laisse les appels intradomaine hors de son passage, et AUT-11 contredit IAM-18 en cas de panne du catalogue.

## Constats

### [11-01] [BLOQUANT] L'empreinte h ne garantit pas que l'appel exécuté est celui approuvé (différentiel d'analyse JSON)
- **Axe** : A
- **Localisation** : § 8.5, p. 111, figure 16 (étape 7) et EXIG-AUT-12 : « recalcule h : toute modification des arguments invalide l'approbation »; « Avant l'exécution, la passerelle DOIT vérifier la signature, l'expiration et l'usage unique, puis recalculer h ». Voir aussi annexe C.6 (p. 221) : « les nombres normalisés (12 480,00 devient 12480) ».
- **Diagnostic** (premiers principes) : la RFC 8785 opère sur une valeur JSON *analysée* (I-JSON, nombres IEEE 754 double). Le calcul de h exige donc que la passerelle analyse les arguments reçus, puis les sérialise sous forme canonique. Rien n'exige que les octets transmis au serveur d'outil soient ces octets canoniques, ni que la passerelle rejette les entrées non conformes à I-JSON. Deux charges utiles distinctes peuvent ainsi produire le même h, et le serveur d'outil peut en lire une autre que la passerelle : clés dupliquées (le premier ou le dernier gagne, selon l'analyseur), entiers au-delà de 2^53, chaînes avec substituts isolés. La propriété « toute modification des arguments invalide l'approbation » est fausse telle que spécifiée.
- **Contre-exemple ou scénario de défaillance** : l'approbateur valide `{"beneficiaire":"A","montant":100}`. Une injection fait émettre à l'agent `{"beneficiaire":"A","montant":100,"montant":100000}`. L'analyseur de la passerelle garde la première occurrence : h identique, appel accepté. L'analyseur du serveur MCP garde la dernière : virement de 100 000 $. Même scénario avec un numéro de compte numérique de 20 chiffres, que la canonisation arrondit.
- **Correctif proposé** : ajouter à EXIG-AUT-12 : « la passerelle DOIT rejeter tout argument non conforme à I-JSON (RFC 7493 : clés dupliquées, nombres hors de la plage exacte d'un double, chaînes invalides) et DOIT transmettre au serveur d'outil exactement les octets canoniques sur lesquels h a été calculé ». Exiger que les montants et identifiants soient des chaînes dans les schémas des outils P2 et P3. Ajouter un test négatif à l'annexe A (clé dupliquée, grand entier).
- **Confiance** : vérifié dans le texte (absence de ces clauses); comportement de la RFC 8785 et des analyseurs : déduit de connaissances sûres.

### [11-02] [MAJEUR] Ce que voit l'approbateur n'est pas lié cryptographiquement à h (WYSIWYS)
- **Axe** : A
- **Localisation** : figure 16, étape 3, p. 111 : « présente l'action exacte, ses paramètres et son effet attendu »; EXIG-AUT-14, p. 112 : « un binding_message court, affiché sur les deux appareils, rattache la demande à l'action ». Annexe C.6 : authorization_details sert « pour l'écran d'approbation et l'audit, sans remplacer l'empreinte ».
- **Diagnostic** : le jeton porte deux représentations de l'action : h, qui couvre ce qui sera exécuté, et authorization_details (ou un rendu), qui couvre ce qui est montré. Aucune exigence n'impose que l'écran soit dérivé de façon déterministe des arguments canoniques par le service d'approbation, ni que les deux représentations concordent. L'« effet attendu » n'a pas d'auteur désigné; s'il vient de l'agent, il tombe sous l'interdit d'EXIG-AUT-13 (« un résumé ou une justification rédigés par l'agent »). Le binding_message, court, sert à apparier les deux appareils : ce n'est pas un lien à l'action.
- **Contre-exemple** : l'agent fournit des arguments où le montant vaut 12 480 et un authorization_details où il vaut 1 248. L'écran affiche 1 248, l'approbateur valide, h couvre 12 480 : la passerelle exécute un appel « approuvé ».
- **Correctif proposé** : « Le service d'approbation DOIT produire l'écran d'approbation à partir des seuls arguments canoniques et du schéma de l'outil inscrit au catalogue, jamais d'un texte fourni par l'agent; s'il est présent, authorization_details DOIT être généré par ce service et vérifié contre les arguments avant signature. »
- **Confiance** : vérifié dans le texte.

### [11-03] [MAJEUR] Fenêtre TOCTOU sur l'état référencé : h lie les arguments, pas leurs référents
- **Axe** : A
- **Localisation** : EXIG-AUT-12, p. 111 : « Le jeton DOIT expirer au plus 15 minutes après sa signature »; § 8.5 : « Une approbation n'a de valeur que si elle porte sur l'action exacte qui sera exécutée ».
- **Diagnostic** : les arguments d'un outil P3 désignent souvent des ressources par identifiant (facture, fournisseur, compte). h fige l'identifiant, pas l'état de la ressource. Pendant les 15 minutes de validité, un autre processus, un autre agent ou une saga concurrente peut modifier le référent (coordonnées bancaires du fournisseur, montant de la facture). L'« action exacte » approuvée n'est alors plus celle exécutée.
- **Contre-exemple** : approbation de `payer_facture{"facture":"F-123"}` à 10 h 00, pendant que F-123 vaut 2 000 $ au compte X. À 10 h 05, un agent fournisseurs, ou une fraude, change le compte bénéficiaire du fournisseur. À 10 h 10, le paiement s'exécute avec un h valide vers le compte Y.
- **Correctif proposé** : exiger que les arguments des outils P3 incluent une précondition de version (ETag, numéro de version, empreinte de l'état pertinent), vérifiée par le serveur de ressources à l'exécution, ou que l'action soit présentée et hachée sous forme résolue (bénéficiaire et montant effectifs, pas seulement des références).
- **Confiance** : déduit.

### [11-04] [MAJEUR] Usage unique contre réessais, rejeu durable et répliques de passerelle (couture § 7.10 / § 8.5)
- **Axe** : A / B
- **Localisation** : tableau 27, p. 101 (LangGraph) : « Nœud réexécuté à la reprise »; p. 102 (Temporal) : « reprise à partir du dernier événement consigné »; EXIG-AUT-12, p. 111 : « un identifiant à usage unique »; figure 16 : « le jeton signé ne vaut que pour cette empreinte, une seule fois ».
- **Diagnostic** : le chapitre 7 assume la réexécution (nœud rejoué à la reprise, réessais d'activité, idempotence au § 7.6). Le chapitre 8 consomme le jeton au premier passage. Trois cas ne sont pas traités. (a) L'appel échoue après consommation du jeton, avec un résultat inconnu (délai dépassé) : le réessai idempotent est refusé, ce qui oblige à une seconde approbation humaine d'une action peut-être déjà exécutée. Autoriser ce réessai violerait l'usage unique. (b) La reprise d'un nœud LangGraph qui a déjà obtenu l'approbation redemande une approbation : demandes en double, propices à l'approbation machinale. (c) Avec plusieurs instances de passerelle (haute disponibilité), l'usage unique exige un magasin de jti partagé, à vérification et inscription atomiques; sinon deux répliques acceptent le même jeton en concurrence.
- **Contre-exemple** : délai réseau dépassé vers le serveur de virement après consommation du jti; Temporal réessaie l'activité; la passerelle refuse (jti consommé); l'opérateur réapprouve; le premier virement avait abouti : doublon. Dans le cas (c), deux répliques reçoivent le même rejeu à 2 ms d'intervalle et l'exécutent toutes les deux.
- **Correctif proposé** : lier le jti à la clé d'idempotence de l'appel (§ 7.6). Préciser que l'usage unique s'entend « une exécution par clé d'idempotence » : les réessais portant la même clé et le même h sont admis jusqu'à exp, et le serveur d'outil déduplique. Exiger un magasin de jti partagé, cohérent et atomique, et un test de concurrence à l'annexe A.
- **Confiance** : vérifié dans le texte (aucune articulation entre jti et clé d'idempotence); scénario déduit.

### [11-05] [MAJEUR] Approbateur pseudonymisé et double approbation : invérifiables par la passerelle
- **Axe** : A
- **Localisation** : EXIG-AUT-12, p. 111 : « l'identifiant pseudonymisé de l'approbateur »; EXIG-AUT-15, p. 112 : « deux approbateurs distincts DOIVENT approuver, dont au moins un autre que le mandant »; annexe C.6 : un seul `sub`.
- **Diagnostic** : la structure du jeton ne prévoit qu'un approbateur, et la liste de vérification d'AUT-12 omet l'habilitation de l'approbateur (liste d'AUT-15), la distinction entre deux approbateurs et l'altérité par rapport au mandant. Si le pseudonyme varie d'un jeton à l'autre, la passerelle ne peut ni constater que deux jetons viennent de deux personnes, ni que l'une n'est pas le mandant. Rien ne dit non plus s'il faut deux jetons ou un jeton à deux signataires.
- **Contre-exemple** : la même personne approuve deux fois depuis deux sessions et obtient deux jetons aux `sub` différents, ce qui contourne le second approbateur exigé pour la classe élevée.
- **Correctif proposé** : pseudonyme stable par personne (identifiant opaque mais déterministe au sein du service); le service d'approbation vérifie l'habilitation (AUT-15) et la distinction avant de signer, et inscrit dans un seul jeton la liste des approbateurs et la preuve de leur distinction; la passerelle vérifie le nombre requis selon classe × palier.
- **Confiance** : vérifié dans le texte.

### [11-06] [MAJEUR] « Le plus strict » n'est pas défini sur des contrôles non comparables; il faut cumuler
- **Axe** : A
- **Localisation** : EXIG-AUT-10, p. 110 : « en retenant le plus strict des éléments suivants : la cellule classe × palier de la figure 15, le niveau d'autonomie de l'agent et les déclencheurs d'approbation »; figure 15, p. 109.
- **Diagnostic** : les cellules de la figure 15 mêlent des natures de contrôle différentes : technique (jeton délégué, masquage, filtrage par ligne), traçabilité (audit), revue humaine (« finalité vérifiée, minimisation »), approbation conditionnelle ou systématique, second approbateur. Ces éléments ne forment pas un ordre total. « Retenir le plus strict » suppose une relation d'ordre que le cadre ne définit pas (thèse T7), et peut se lire comme « remplacer » au lieu de « cumuler ».
- **Contre-exemple** : agent modéré, outil P1 (cellule : « jeton délégué, filtrage par ligne »), déclencheur de cumul actif (approbation). Si l'on retient « le plus strict » et que l'approbation l'est, le filtrage par ligne disparaît : l'approbateur valide une lecture non filtrée.
- **Correctif proposé** : « le contrôle exigé est l'union des contrôles de la cellule, du niveau et des déclencheurs; pour l'approbation, on retient la forme la plus forte selon l'ordre : aucune < au-delà du seuil < à chaque appel < à chaque appel avec second approbateur < refus ». Publier cet ordre dans le tableau.
- **Confiance** : vérifié dans le texte.

### [11-07] [MAJEUR] Déclencheur de cumul : « action externe » (AUT-10) contre P2 interne (exemple, SEC-04); « session » non définie
- **Axe** : A / C
- **Localisation** : EXIG-AUT-10, p. 110 : « cumul de contenu non fiable, de données sensibles et d'action externe »; même page : « Un agent N3 qui a lu un courriel externe, consulté un dossier P1 et s'apprête à appeler un outil P2 tombe donc sous approbation ». EXIG-SEC-04 (p. 134) : « [C] il modifie un état ou communique vers l'extérieur (outils P2, P3 ou envoi externe) ».
- **Diagnostic** : la troisième branche d'AUT-10 (« action externe ») est plus étroite que la branche [C] de Meta et d'EXIG-SEC-04, qui couvre tout changement d'état, P2 compris. Lu à la lettre, AUT-10 ne déclenche pas l'approbation dans l'exemple donné juste avant (outil P2 interne). De plus, « session » n'est définie nulle part (aucune entrée au glossaire, d'après une recherche dans full.txt). Pour un agent N4 qui « opère en continu », ou un agent à mémoire persistante, soit la session ne finit jamais (tout P2 exige alors une approbation, et N4 dégénère en N2), soit elle se découpe arbitrairement, ce qui permet d'échapper à la règle.
- **Contre-exemple** : un agent N3 lit un courriel piégé, lit un dossier client et appelle « mise à jour de statut » (P2). La passerelle conforme à AUT-10 ne déclenche rien, alors qu'EXIG-SEC-04 l'exige.
- **Correctif proposé** : dans AUT-10, remplacer « action externe » par « changement d'état ou communication externe (P2, P3, envoi externe), au sens d'EXIG-SEC-04 »; définir la session (frontière de contexte du modèle, mémoire comprise) et sa propagation entre agents.
- **Confiance** : vérifié dans le texte.

### [11-08] [MAJEUR] Seuils sans unité d'agrégation : contournement par fractionnement
- **Axe** : A
- **Localisation** : tableau 30, p. 107 : « en une exécution ininterrompue »; tableau 31, p. 108 : « seuil métier au catalogue (p. ex. 5 000 $); approbation au-delà du seuil »; p. 109 : « le seuil déclaré de l'outil est de 25 par tâche »; tableau 28 : « sous un plafond horaire »; AUT-07, exemple : « 10 000 comptes par exécution ».
- **Diagnostic** : le seuil s'exprime tour à tour par appel, par tâche, par exécution ou par heure, et la passerelle l'évalue « pour chaque appel » (AUT-10). Aucune exigence ne fixe la portée d'agrégation (appel, tâche, agent, mandant, fenêtre glissante), ni le cumul entre tâches ou entre agents d'un même mandant. Une recherche de « fractionn », « cumul » et « agrégé » dans full.txt ne trouve rien.
- **Contre-exemple** : les 40 factures de l'exemple de la p. 109 passent en deux appels de 20, ou en deux tâches de 20 : aucune approbation. Un agent N3 émet 50 avoirs de 4 999 $ chacun sous un seuil de 5 000 $ par appel.
- **Correctif proposé** : exiger que chaque seuil inscrit au catalogue déclare son unité et sa portée d'agrégation (par appel et cumul par tâche, par agent et par mandant, sur une fenêtre de durée D), et que la passerelle tienne ces compteurs; ajouter un test de fractionnement à l'annexe A.
- **Confiance** : vérifié dans le texte (aucune règle d'agrégation).

### [11-09] [MAJEUR] La passerelle ne voit pas tous les appels que le chapitre 8 lui fait contrôler
- **Axe** : A
- **Localisation** : EXIG-AUT-01, p. 105 : « La passerelle d'agents DOIT refuser tout appel d'outil qui excède ce plafond »; EXIG-AUT-10 : « Pour chaque appel d'outil, la passerelle d'agents DOIT ». EXIG-IAM-17 (p. 129) : « À l'intérieur d'un domaine, la décision par appel (EXIG-IAM-02) est appliquée par le serveur de ressources ».
- **Diagnostic** : IAM-17 ne fait passer par la passerelle que les appels vers un serveur MCP, vers un agent, ou ceux qui franchissent une frontière de domaine, « dans tout environnement serveur ». Les appels intradomaine à une API (non MCP) et le mode local y échappent. Le chapitre 8 attribue pourtant à la seule passerelle le plafond de niveau, le calcul classe × palier, l'échec en mode fermé et la vérification du jeton. Pour ces appels, aucun composant n'est désigné pour appliquer AUT-07 à AUT-12 (thèse T2).
- **Contre-exemple** : un agent N3 appelle directement l'API interne de facturation de son propre domaine, une action P3 au catalogue. Le serveur de ressources applique l'autorisation OAuth, mais ni le jeton d'approbation ni le calcul de h.
- **Correctif proposé** : soit exiger que tout appel d'outil P2 ou P3 passe par la passerelle, quelle que soit la frontière, soit étendre AUT-01, -10, -11 et -12 au « point d'application des politiques (passerelle ou serveur de ressources, EXIG-IAM-17) », avec obligation pour le serveur de ressources de vérifier le jeton d'approbation.
- **Confiance** : vérifié dans le texte.

### [11-10] [MAJEUR] EXIG-AUT-11 inapplicable si le catalogue est en panne, et en tension avec EXIG-IAM-18
- **Axe** : A / C
- **Localisation** : EXIG-AUT-11, p. 110 : « Si le service d'approbation, le catalogue ou le service de politiques est indisponible, ou si aucune politique ne couvre l'action demandée, la passerelle DOIT refuser tout appel P3 et tout appel P2 au-delà du seuil »; EXIG-IAM-18 (p. 129) : « Si le plan de contrôle est indisponible, elle continue d'appliquer la dernière politique distribuée ».
- **Diagnostic** : (1) Le palier et le seuil proviennent du catalogue (AUT-08). Catalogue indisponible, la passerelle ne peut pas savoir si un appel est P0, P2 sous le seuil ou P3, à moins d'un cache dont la règle n'est pas écrite. Refuser « seulement P3 et P2 au-delà du seuil » est alors indécidable. (2) Le cas « aucune politique ne couvre l'action » refuse seulement P3 et P2 au-delà du seuil, ce qui laisse croire que P0 à P2 passent. IAM-18 refuse pourtant tout appel sans décision valide : la clause est soit redondante, soit contradictoire, et « sans préjudice » ne tranche pas. (3) Panne du service de politiques : IAM-18 applique la dernière politique, ce qui permet un P3 dûment approuvé, alors qu'AUT-11 refuse tout P3. Les deux régimes ne sont pas réconciliés. (4) Approbation indisponible pour un agent N2 : AUT-11 ne vise pas le P2 sous le seuil, qui exige pourtant une approbation au niveau N2.
- **Contre-exemple** : panne du catalogue; un outil nouvellement reclassé de P2 à P3 figure encore en P2 dans le cache de la passerelle; l'appel passe.
- **Correctif proposé** : « Catalogue indisponible : la passerelle applique le dernier instantané signé, s'il date de moins de T; au-delà, elle traite tout outil d'écriture comme P3. Aucune politique applicable : refus de tout appel (IAM-18). Service de politiques indisponible : dernière politique distribuée (IAM-18), sauf pour P3, refusé. Service d'approbation indisponible : refus de tout appel qui exige une approbation selon AUT-10. »
- **Confiance** : vérifié dans le texte.

### [11-11] [MAJEUR] Deux règles de plafonnement incompatibles : tableau 30 (un critère suffit) contre AUT-07 (trois critères conjoints)
- **Axe** : C / A
- **Localisation** : tableau 30, p. 107 : « Une détection lente impose un contrôle avant l'action (N2) plutôt qu'après »; EXIG-AUT-07, p. 108 : « dont le rayon d'impact, la réversibilité et le délai de détection atteignent les seuils […] NE DOIT PAS être autorisé au-delà de N2 ».
- **Diagnostic** : AUT-02 rend le tableau 30 normatif (« DOIT être évalué selon les critères du tableau 30 »). Or ce tableau plafonne à N2 dès que la détection est lente, alors que la « règle d'or » n'y plafonne que si les trois conditions sont réunies. Soit AUT-07 est redondante, soit le tableau surcontraint. Notation dérivante au passage : « rayon large » (tableau 30) contre « rayon élevé » (AUT-07).
- **Contre-exemple** : un agent à rayon faible, entièrement réversible, mais à détection lente. Il est plafonné à N2 selon le tableau 30, autorisé à N3 selon AUT-07 : deux réviseurs concluent différemment.
- **Correctif proposé** : rendre explicite la fonction de décision : par critère, la valeur qui plafonne (p. ex. « détection lente ⇒ N2 au plus »), et faire d'AUT-07 un cas particulier, ou supprimer l'effet plafonnant du tableau 30 et le formuler comme « abaisse les seuils ». Unifier le vocabulaire (« rayon élevé »).
- **Confiance** : vérifié dans le texte.

### [11-12] [MAJEUR] Règle d'or inopérante tant que les seuils d'étalonnage ne sont pas approuvés (ouverture par défaut)
- **Axe** : B
- **Localisation** : EXIG-AUT-07, p. 108 : « atteignent les seuils d'étalonnage approuvés par le comité »; p. 107 : « Aucune source reconnue ne propose de valeurs universelles ».
- **Diagnostic** : la condition d'AUT-07 renvoie à des seuils que le comité doit publier. Avant leur publication (phase de fondations, ou nouveau type d'outil), la condition ne peut pas être « atteinte » et la règle ne s'applique pas. C'est contraire à PRIN-12 (échec en mode fermé), et la règle n'est pas vérifiable en revue.
- **Contre-exemple** : premier agent de facturation homologué avant que le comité ait fixé les seuils de rayon et de délai : rien n'empêche formellement un N3.
- **Correctif proposé** : « En l'absence de seuils approuvés pour un critère, celui-ci est réputé atteint »; publier des valeurs par défaut prudentes avec le catalogue initial.
- **Confiance** : déduit.

### [11-13] [MAJEUR] Statut normatif de l'approbation « hors bande » incohérent
- **Axe** : C / A
- **Localisation** : tableau 31, p. 108, colonne « Contrôles obligatoires » : « Approbation humaine hors bande à chaque appel »; tableau 28 : « P3 après approbation hors bande »; EXIG-AUT-14, p. 112 : « DEVRAIT passer par OpenID Connect CIBA »; EXIG-AUT-13 : exclut « une confirmation locale dans l'interface de l'agent ».
- **Diagnostic** : le caractère hors bande du P3 est obligatoire dans les tableaux 28, 31 et 46, mais aucun bloc EXIG ne le pose en DOIT : AUT-09 et AUT-12 n'en parlent pas, et AUT-14 n'est qu'un DEVRAIT, qui porte d'ailleurs sur le moyen (CIBA). À l'inverse, AUT-13 interdit toute confirmation dans l'interface de l'agent, pour toute approbation. Toute approbation est donc de fait hors bande, et la distinction « P2 : approbation signée; P3 : hors bande » (tableau 28, figure 14) ne désigne aucune différence opérable.
- **Contre-exemple** : une équipe met en œuvre l'approbation P3 dans une fenêtre du portail du service d'approbation, ouverte depuis l'interface de l'agent, et soutient qu'elle respecte AUT-12 et ne déroge qu'à un DEVRAIT. Une autre, avec la même mise en œuvre, se juge en écart avec le tableau 31. Les deux lectures se défendent.
- **Correctif proposé** : ajouter à AUT-09 « par un canal hors bande au sens d'AUT-14 (appareil et session distincts de ceux de l'agent) »; définir « hors bande » au glossaire; distinguer clairement, pour P2, ce qui est permis (canal du service d'approbation dans la même session de l'utilisateur?) et ce qui ne l'est pas.
- **Confiance** : vérifié dans le texte.

### [11-14] [MAJEUR] N3 et N4 indiscernables pour la passerelle; « deux éléments observables » ne les départagent pas
- **Axe** : A / B
- **Localisation** : § 8.1, p. 103 : « Chaque niveau se définit donc par deux éléments observables : le rôle de la personne et l'étendue de ce que l'agent peut faire sans approbation »; tableau 28, N4 : « Comme N3; P3 toujours approuvé »; EXIG-AUT-01 : « La passerelle d'agents DOIT refuser tout appel d'outil qui excède ce plafond ».
- **Diagnostic** : N3 et N4 ont les mêmes paliers permis, donc la même « étendue sans approbation ». Ce qui les sépare (autodéclenchement, exécution continue, absence de la personne) n'est pas une propriété d'un appel d'outil. La passerelle ne peut donc pas, appel par appel, « refuser ce qui excède » un plafond N3 pour un agent qui se comporte en N4. Le tableau 28 et la figure 14 présentent par ailleurs « s'autodéclenche » comme un trait de N4, alors que le § 3.3 (p. 24) admet des agents ambiants N1 à N3 et que le § 8.6 (p. 112) rappelle qu'ils ne sont « pas nécessairement entièrement autonomes ». La seule distinction est la conjonction posée au § 3.3, absente du chapitre 8.
- **Contre-exemple** : un agent modéré plafonné à N3, abonné à un flux d'événements, traite seul les billets 24 heures sur 24 avec des outils P2 sous le seuil. Est-ce un N3 ambiant permis ou un N4 non autorisé? Aucun test de la passerelle ne le dit.
- **Correctif proposé** : définir N4 par des attributs contrôlables (déclencheur sans demande humaine *et* délégation de longue durée selon EXIG-AUT-18 *et* absence de supervision en temps réel), reprendre au tableau 28 la conjonction du § 3.3, et désigner le point de contrôle (abonnement aux événements, émission de la délégation) plutôt que la passerelle d'outils.
- **Confiance** : vérifié dans le texte.

### [11-15] [MAJEUR] Rétrogradation automatique d'EXIG-AUT-05 : tempête d'approbations et approbateurs absents
- **Axe** : B
- **Localisation** : EXIG-AUT-05, p. 106 : « Tant que la réévaluation n'est pas faite, l'agent DOIT fonctionner au niveau immédiatement inférieur à son niveau déclaré ».
- **Diagnostic** : un changement de version de modèle chez un fournisseur, comme le retrait d'un modèle, touche en même temps tous les agents qui l'utilisent. Les agents N3 passent alors à N2 : chaque écriture P2 exige une approbation. AUT-15 n'impose de liste d'approbateurs que pour les combinaisons « soumises à approbation », dont P2 sous le seuil ne fait pas partie pour un N3. Ces listes peuvent donc ne pas exister, et le volume tombe dans la saturation des approbateurs (menace T10, § 8.7). Rien ne dit non plus qui détecte le changement de version (alias de modèle mis à jour en silence), ni qui applique la rétrogradation (registre? passerelle?).
- **Contre-exemple** : retrait d'un modèle un vendredi; 40 agents N3 passent à N2; des milliers de demandes d'approbation arrivent sans approbateur inscrit; la passerelle refuse, ou les approbations deviennent machinales.
- **Correctif proposé** : exiger, pour tout agent N3 ou N4, une liste d'approbateurs et un plan de capacité pour le niveau inférieur; un épinglage de version de modèle détectable par la passerelle (refus si la version servie diffère de la version homologuée); une suspension ordonnée plutôt qu'une rétrogradation lorsque la capacité d'approbation manque.
- **Confiance** : déduit.

### [11-16] [MAJEUR] Un outil « P0 » de recherche publique est un canal d'exfiltration
- **Axe** : A
- **Localisation** : tableau 31, p. 108, P0 : « Recherche documentaire publique […] Identité de charge de travail, limitation de débit, journalisation de l'usage »; p. 108 : « La frontière entre paliers suit l'effet, pas le serveur ».
- **Diagnostic** : le palier classe les outils selon l'effet sur l'état. Or un outil de lecture publique transmet ses arguments (la requête) à un tiers : c'est une communication vers l'extérieur au sens de la branche [C] de la règle de deux et de la triade létale. Le tableau 31 ne prévoit aucun contrôle des arguments sortants pour P0, et AUT-10, qui ne vise que l'« action externe », ne fait pas forcément de la recherche publique un tel cas (voir 11-07).
- **Contre-exemple** : après une injection, l'agent appelle `recherche_publique{"q":"<numéro de dossier et RP du client>"}`. Ce P0 « automatique » journalise l'appel et exfiltre les données vers le moteur tiers.
- **Correctif proposé** : ajouter un attribut « sortie de données » orthogonal au palier, déclaré au catalogue, pour tout outil dont les arguments quittent l'entreprise; le compter comme [C] dans EXIG-SEC-04 et AUT-10; contrôle DLP des arguments pour P0 et P1 externes.
- **Confiance** : déduit (vérifié : le tableau 31 ne prévoit pas ce contrôle).

### [11-17] [MAJEUR] Grille classe × palier : cellules incompatibles avec le tableau 46, et classe indéfinie pour un P3 sous le seuil
- **Axe** : A / C
- **Localisation** : figure 15, p. 109 : ligne « Faible », colonnes « P1 · lecture interne / dossier client, paie » et « P3 · action critique / virement, suppression, envoi »; tableau 46 (p. 171), classe faible : « lecture seule ou actions internes réversibles; aucun effet sur une personne »; classe élevée : « action financière, juridique ou irréversible au-delà des seuils déclarés ».
- **Diagnostic** : un agent qui lit la paie (RP, voire RP sensibles) ou exécute un virement ne peut pas être de classe faible selon le tableau 46. Les exemples des cellules Faible × P1 et Faible × P3 désignent donc des combinaisons inatteignables, et la cellule Faible × P3 (« Approbation signée à chaque appel », un seul approbateur) peut induire un concepteur en erreur. Inversement, un outil P3 financier ou irréversible *sous* le seuil déclaré ne remplit aucun critère du tableau 46 : il n'est pas réversible (exclu de la classe faible), il n'est pas P2 (critère de la classe modérée), et il reste sous le seuil (critère de la classe élevée). « La plus élevée dont un critère est rempli » n'a alors pas de valeur : c'est une combinaison non couverte (thèse T7).
- **Contre-exemple** : un agent de remboursement de frais qui ne fait que des virements de moins de 100 $ à des employés n'a pas de classe déterminable.
- **Correctif proposé** : dans la figure 15, remplacer les exemples des lignes faible et modérée par des cas atteignables, ou griser les cellules impossibles; au tableau 46, fixer une classe par défaut (« toute capacité P3 ⇒ au moins modérée ») ou un critère explicite pour P3 sous le seuil.
- **Confiance** : vérifié dans le texte (tableau 46 lu dans full.txt); conclusion déduite.

### [11-18] [MINEUR] Exemple de la p. 109 : la capacité soumise à approbation compte-t-elle dans le classement?
- **Axe** : A / C
- **Localisation** : p. 109 : « Un agent de classe modérée, déclaré N3 […] veut modifier l'échéance de 40 factures alors que le seuil déclaré de l'outil est de 25 par tâche »; EXIG-AUT-06 : classement « fondé sur les permissions effectives ».
- **Diagnostic** : selon AUT-06, ce sont les permissions effectives qui classent l'agent. Or l'agent peut, avec approbation, agir au-delà du seuil sur une donnée financière, ce qui correspond au critère de la classe élevée du tableau 46. Le cadre ne dit pas si une capacité conditionnée à une approbation compte dans le classement. Selon la lecture, l'agent de l'exemple est de classe élevée et plafonné à N2.
- **Correctif proposé** : préciser dans AUT-06 et au tableau 46 que le classement considère (ou exclut) les actions possibles seulement après approbation hors bande.
- **Confiance** : déduit.

### [11-19] [MINEUR] Différences entre la figure 14 et le tableau 28 sur les contrôles minimaux
- **Axe** : C
- **Localisation** : figure 14, p. 103, N4 : « évaluation continue, retour arrière rapide »; N1 : « accès circonscrit, DLP, essais d'exactitude ». Tableau 28, p. 104 : « retour arrière rapide » rangé en N3; aucune DLP en N1.
- **Diagnostic** : la figure place le retour arrière rapide en N4, le tableau en N3; la DLP figure en N1 dans la figure, mais pas dans le tableau. Comme les contrôles sont cumulatifs, l'écart change ce qu'on exige d'un N3, ou d'un N1.
- **Correctif proposé** : aligner la figure sur le tableau et dire lequel fait foi.
- **Confiance** : vérifié dans le texte.

### [11-20] [MINEUR] Cellules de la figure 15 imprécises ou en retrait du tableau 31
- **Axe** : C
- **Localisation** : figure 15, p. 109 : Faible × P1 « Automatique / jeton délégué, masquage »; Modéré × P1 « Automatique + audit »; Élevé × P1 « Audit + revue »; Faible × P2 « Autonome sous seuil » contre Modéré × P2 « Approbation au-delà du seuil métier déclaré ».
- **Diagnostic** : (a) Le tableau 31 rend le journal d'audit et le contrôle d'accès « au document ou à la ligne » obligatoires pour tout P1 : la cellule Faible × P1 semble les omettre, et le « + audit » de la ligne modérée laisse entendre que l'audit est un supplément, alors qu'AUT-10 consigne chaque appel au journal d'audit. (b) Les cellules faible et modérée en P2 disent la même chose en termes différents, ce qui suggère à tort une différence. (c) Pour Élevé × P1, on ne sait pas si la « revue » précède ou suit l'appel : avant chaque lecture, ce serait inexploitable.
- **Correctif proposé** : faire de chaque cellule un complément explicite au tableau 31 (« en plus des contrôles du palier »); préciser « revue a posteriori par échantillonnage » pour Élevé × P1; harmoniser le libellé P2 des lignes faible et modérée.
- **Confiance** : vérifié dans le texte.

### [11-21] [MINEUR] « Dont au moins un autre que le mandant » est tautologique
- **Axe** : C
- **Localisation** : EXIG-AUT-15, p. 112 : « deux approbateurs distincts DOIVENT approuver, dont au moins un autre que le mandant ».
- **Diagnostic** : de deux personnes distinctes, une au plus peut être le mandant : la clause n'ajoute rien. L'intention probable (indépendance vis-à-vis du demandeur, ou séparation des tâches) n'est pas exprimée.
- **Correctif proposé** : « dont aucun n'est le mandant », ou « dont au moins un n'appartient pas à la chaîne hiérarchique du mandant », selon l'intention.
- **Confiance** : vérifié dans le texte.

### [11-22] [MINEUR] Concaténation « ‖ » sans séparation de domaine ni encodage fixé
- **Axe** : A
- **Localisation** : p. 111 : « h = SHA-256(identifiant de l'outil ‖ arguments canonisés) »; annexe C.6 : « immédiatement suivi des arguments canonisés ».
- **Diagnostic** : la concaténation brute n'est sans ambiguïté que si l'identifiant ne peut contenir aucun préfixe d'une sérialisation JSON, ce qui n'est pas spécifié (jeu de caractères de l'identifiant, encodage UTF-8, normalisation Unicode). Aucune étiquette de domaine ne distingue non plus ce hachage des autres SHA-256 du cadre, comme le chaînage d'audit. Le risque pratique est faible, puisque les arguments MCP sont des objets, mais la construction n'est pas robuste par conception.
- **Correctif proposé** : h = SHA-256(JCS({"v":1,"outil":<id>,"arguments":<args>})), ou bien un préfixe de domaine suivi d'un champ de longueur.
- **Confiance** : déduit.

### [11-23] [MINEUR] Liste de vérification d'AUT-12 incomplète; la figure 16 omet des champs du jeton
- **Axe** : C
- **Localisation** : EXIG-AUT-12 : « vérifier la signature, l'expiration et l'usage unique, puis recalculer h »; figure 16, étape 5 : « { h, approbateur, tâche, exp } ».
- **Diagnostic** : la vérification n'inclut ni l'audience, ni la concordance entre l'agent ou la tâche du jeton et ceux de l'appel. AUT-13 l'exige pourtant (« une autre tâche ou un autre agent »). La figure omet l'identifiant de l'agent et le jti, qu'AUT-12 rend obligatoires.
- **Correctif proposé** : ajouter à AUT-12 « l'audience et la concordance de l'agent et de la tâche avec l'appel », et compléter la figure.
- **Confiance** : vérifié dans le texte.

### [11-24] [MINEUR] Authentification « au moins deux facteurs » insuffisante contre la fatigue d'approbation
- **Axe** : B
- **Localisation** : EXIG-AUT-15 : « L'approbateur DOIT s'authentifier par authentification forte (au moins deux facteurs) ».
- **Diagnostic** : deux facteurs admettent l'OTP par SMS et la notification poussée sans appariement de nombre. Ce sont précisément les vecteurs du bombardement d'approbations (menace T10). L'approbation P3 est la dernière barrière.
- **Correctif proposé** : exiger un authentifiant résistant à l'hameçonnage (FIDO2/WebAuthn) pour les approbations P3, et un appariement par binding_message vérifié par saisie, plutôt qu'un simple affichage.
- **Confiance** : déduit.

### [11-25] [MINEUR] binding_message « affiché sur les deux appareils » alors qu'AUT-14 vise aussi un agent sans interface
- **Axe** : C
- **Localisation** : EXIG-AUT-14, p. 112 : « ou celle que requiert un agent sans interface […] un binding_message court, affiché sur les deux appareils ».
- **Diagnostic** : un agent sans interface n'a pas d'appareil de consommation où afficher le message. La formule est inapplicable dans le cas même qu'elle vise.
- **Correctif proposé** : « affiché à l'approbateur et consigné dans la demande et dans le jeton ».
- **Confiance** : vérifié dans le texte.

### [11-26] [MINEUR] N0 « aucun modèle » présenté comme niveau d'un agent
- **Axe** : C
- **Localisation** : EXIG-AUT-01 : « Chaque agent DOIT avoir un niveau d'autonomie N0 à N4 »; tableau 28, N0 : « Aucun modèle »; EXIG-AUT-05 : « un agent de niveau N1 est suspendu ou ramené à un flux déterministe sans autonomie (N0) ».
- **Diagnostic** : un système sans modèle n'est pas un agent au sens du § 3.2. « Ramener un agent à N0 », c'est le remplacer par un autre système, et cela suppose qu'un flux déterministe équivalent existe. L'option relève donc de la suspension.
- **Correctif proposé** : borner AUT-01 à N1-N4 pour les agents (N0 désigne le flux), et écrire dans AUT-05 « est suspendu, ou remplacé par le flux déterministe de repli s'il existe ».
- **Confiance** : vérifié dans le texte.

### [11-27] [MINEUR] Déclencheurs de réévaluation : AUT-05 et CON-03 divergent
- **Axe** : C
- **Localisation** : EXIG-AUT-05 : « changement de modèle ou de version de modèle, d'invite système […], d'outil en écriture, de population visée ou d'ODD »; EXIG-CON-03 (p. 172) : « modèle ou de fournisseur, d'outil ou de palier d'outil, de catégorie de données, de finalité, de population visée ou de lieu de traitement ».
- **Diagnostic** : un changement de finalité ou de catégorie de données peut faire passer la classe à élevée et abaisser le plafond à N2, sans déclencher AUT-05 : l'agent reste N3 au-delà de son nouveau plafond, jusqu'à ce que quelqu'un applique AUT-02. CON-03 réévalue la classe avant la production, AUT-05 laisse l'agent fonctionner en mode rétrogradé : deux logiques de blocage différentes.
- **Correctif proposé** : faire de tout déclencheur de CON-03 un déclencheur d'AUT-05, et réciproquement, ou renvoyer à une liste unique.
- **Confiance** : vérifié dans le texte.

### [11-28] [MINEUR] Tableau 29 : statut contradictoire des correspondances avec Feng et al.
- **Axe** : C
- **Localisation** : p. 106, avant le tableau : « Les correspondances avec Gartner, AWS et Feng et al. reposent sur les sources citées […]; celles avec Morris et al. et SAE J3016 sont indicatives »; note sous le tableau : « celles avec Feng et al., Morris et al. et SAE J3016 sont indicatives ».
- **Diagnostic** : Feng et al. sont rangés tantôt parmi les correspondances sourcées, tantôt parmi les indicatives. Le libellé « L4 Approbateur » de Feng, associé à N3, se lit en outre mal à côté de N2, où la personne « approuve chaque écriture ».
- **Correctif proposé** : trancher, et ajouter une ligne expliquant que l'« approbateur » de Feng n'intervient que sur exception.
- **Confiance** : vérifié dans le texte.

### [11-29] [MINEUR] Analogie SAE J3016 : « hors du domaine » contre « dans son domaine »; le repli des N3 est celui du niveau 4 de SAE
- **Axe** : C / A
- **Localisation** : EXIG-AUT-04, Pourquoi, p. 105 : « par la partie qui assure le repli hors du domaine »; p. 107 : « son niveau 4, où le système assure lui-même le repli dans son domaine »; tableau 29 : N3 ↔ « Niveau 3 : l'humain reprend la main ».
- **Diagnostic** : les deux formulations se contredisent sur le lieu du repli. Surtout, AUT-04 impose aux agents N3 un repli assuré par le système (« arrêt en état sûr, compensation ou escalade »), ce qui correspond au niveau 4 de SAE et non au niveau 3. L'analogie N3 ↔ SAE 3 contredit l'exigence qu'elle est censée éclairer.
- **Correctif proposé** : unifier la formulation (« le repli à la sortie du domaine ») et noter que N3 et N4 relèvent tous deux, pour le repli, du niveau 4 de SAE.
- **Confiance** : vérifié dans le texte; sens de J3016 : sûr.

### [11-30] [MINEUR] ASI09 cité à contresens dans EXIG-AUT-09
- **Axe** : C
- **Localisation** : EXIG-AUT-09, Pourquoi, p. 109 : « l'OWASP range l'absence de confirmation des actions sensibles parmi les vulnérabilités (ASI09) »; p. 113 : « Le risque ASI09 "Human-Agent Trust Exploitation" vise la surconfiance ».
- **Diagnostic** : le document définit lui-même ASI09 comme l'exploitation de la confiance humaine (surconfiance, explications fabriquées), non comme l'absence de confirmation. Celle-ci relèverait plutôt des mesures d'atténuation d'ASI02, que le cadre cite à la p. 111.
- **Correctif proposé** : citer ASI02 (mésusage d'outils) pour l'absence de confirmation, ou reformuler en « parmi les mesures d'atténuation d'ASI09 ».
- **Confiance** : vérifié dans le texte (incohérence interne); contenu d'OWASP : à vérifier.

### [11-31] [MINEUR] Références en double ou secondaires pour un même fait
- **Axe** : C
- **Localisation** : p. 112 : WIMSE AIMS cité [309] (AUT-13) puis [93, 311] (AUT-14); annexe G : [93] et [309] désignent tous deux draft-ietf-wimse-aims-00, avec des URL et des dates différentes. p. 107 (AUT-06) : Gartner cité par [305], un article d'ITPro, alors que le communiqué primaire [95] est cité à la p. 103 pour la même idée. RIA, art. 14 : [290] (Future of Life Institute) aux p. 105, alors qu'EXIG-CON-02 cite [412] (Commission européenne) pour l'article 14(3); art. 26 : [94] (Future of Life Institute).
- **Diagnostic** : doublon bibliographique, et préférence d'une source de catégorie B à la source de catégorie A disponible, contraire à la méthode de l'annexe F (thèse T8).
- **Correctif proposé** : fusionner [93] et [309]; citer [95] dans AUT-06; citer le texte du RIA (EUR-Lex ou [412]) pour les articles 14 et 26.
- **Confiance** : vérifié dans le texte.

### [11-32] [MINEUR] Une prévision d'analyste présentée comme « constat » fondateur
- **Axe** : B
- **Localisation** : § 8.1, p. 103 : « Deux constats la fondent. […] la firme prévoit que, d'ici 2027, 40 % des entreprises rétrograderont ou désactiveront des agents autonomes ».
- **Diagnostic** : le second « constat » repose sur un communiqué de presse de Gartner, qui livre une opinion et une prévision sans population ni méthode publiques. Le présenter comme constat surestime la force de la preuve.
- **Correctif proposé** : écrire « Deux arguments la fondent », et qualifier la source (« selon une prévision de Gartner, sans méthode publiée »).
- **Confiance** : vérifié dans le texte; contenu du communiqué : à vérifier.

## Points forts
Distinction nette entre classe, niveau, palier et topologie; palier tiré du catalogue et non des annotations MCP, avec la nuance juste sur « should never ».
Approbation pensée comme objet cryptographique lié à l'action, à usage unique, avec liste explicite de ce qui n'en est jamais une (AUT-13) et échec en mode fermé (AUT-11).
Honnêteté épistémique : chaque plafond et chaque seuil est marqué « choix du cadre », et les correspondances avec les autres échelles sont qualifiées d'indicatives.

## Questions pour l'audit bibliographique
- p. 106, [304] : existe-t-il une révision SAE J3016_202609? La dernière que je connaisse est J3016_202104.
- p. 103-112, [76] : IMDA, *Model AI Governance Framework for Agentic AI*, « version 1.5 » : vérifier la version et les passages cités (portée et réversibilité, chaîne de pensée, refus par défaut, quatre catégories de déclencheurs).
- p. 103, [95] : Gartner, communiqué du 26 mai 2026 : la prévision « 40 % d'ici 2027 » et la « gouvernance binaire ».
- p. 104, [95] : les niveaux Gartner Observer, Conseiller, Agir avec approbation et Agir de façon autonome, et l'inclusion des contrôles Observer dans Conseiller.
- p. 106, [75] : la matrice de portée d'AWS associe-t-elle la portée 2 à une approbation avant chaque action et la portée 3 à des interrupteurs d'arrêt?
- p. 105, [83] : Feng et al. : « certificat d'autonomie », « évaluation assistée » et renouvellement à chaque changement.
- p. 108, [197, 201] : MCP 2026-07-28 : les annotations d'outils sont-elles tenues pour non fiables (MUST) dans la page Tools, et la formule « should never » figure-t-elle au schéma?
- p. 109 et 111, [28] : OWASP Top 10 agentique : ASI09 traite-t-il de l'absence de confirmation, et ASI02 recommande-t-il l'approbation explicite par action à fort impact?
- p. 109-110, [307] : Meta, *Agents Rule of Two*, 31 octobre 2025 : la formulation de la branche [C] (« change state or communicate externally »).
- p. 111, [68] : A2A 1.0 emploie-t-il la RFC 8785 pour signer les cartes d'agent?
- p. 112, [93]/[309] : draft-ietf-wimse-aims-00 dit-il qu'une confirmation locale dans l'interface ne suffit pas, et cite-t-il CIBA en notant ses limites en cours d'exécution?
- p. 105 et 112, [290], [94] : libellés exacts du RIA, art. 14(3), art. 14(4)(e) et art. 26(2).
- p. 106, [8] : E-23 du BSIF en vigueur le 1er mai 2027; critères de « modification importante ».
- p. 112, [310] : statut final de CIBA Core 1.0 et sémantique du binding_message (affichage sur les deux appareils).
