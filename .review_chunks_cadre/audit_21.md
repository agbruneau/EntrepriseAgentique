# Audit chunk_21 — pages 201-212

## Synthèse
Le chunk couvre la fin du § 15.1 (tableau 58, règles de progression, J2a, calage du tableau 59), le § 15.2 (90 jours, tableau 60), le § 15.3 (indicateurs, tableau 61), le § 15.4 (facteurs de succès, tableau 62) et l'annexe A (grille d'homologation), avec l'amorce de l'annexe B. La feuille de route est soignée et son arithmétique calendaire tient, mais elle s'articule mal avec les règles non dérogeables et avec la grille. Les trois défauts les plus graves :
1. Des obligations légales déclarées « sans dérogation » restent dérogeables par la grille et par le tableau 61.
2. Le plafond N2 imposé aux appels interdomaines qui contournent la passerelle ne peut pas s'appliquer, puisque c'est la passerelle qui applique les plafonds.
3. Le chapitre 15 transforme EXIG-CON-12 (inscrire un « état de validation ») en une validation initiale exigible le 1er mai 2027, présentée comme une échéance externe.

## Constats

### [21-01] [BLOQUANT] Obligations légales « sans dérogation » rendues dérogeables par la grille et le tableau 61
- **Axe** : A, C
- **Localisation** :
  - § 15.1, encadré ATTENTION, p. 202 : « Les obligations déjà en vigueur, comme les articles 3.3, 12.1 et 17 de la Loi sur le privé, ne suivent pas le rythme des phases et ne souffrent aucune dérogation ».
  - § 15.3, p. 205 : « sauf celles qui reprennent une exigence (registre, secrets, passerelles, traçabilité, EFVP), qui ne s'écartent que par dérogation ».
  - A.1 point 2, p. 209 : « Un point non conforme exige une dérogation écrite ».
- **Diagnostic** : EXIG-GOV-17 (p. 169) interdit toute dérogation au « manquement à une obligation légale ou réglementaire ». Quatre éléments du chunk le contredisent :
  - Le tableau 61 prévoit expressément qu'on s'écarte de la cible EFVP (art. 3.3 et 17) par dérogation.
  - Dans la grille, les points qui portent des obligations légales ne sont pas marqués non dérogeable : A.5 « Si décision sur une personne » (art. 12.1), A.8 « Si renseignements personnels » et « Si traitement hors Québec » (art. 3.3 et 17), A.8 « Régimes applicables… obligations du déployeur » (RIA, art. 26). Par la règle générale de A.1, un « Non conforme » sur ces points se traite donc par dérogation.
  - Le tableau 58 inscrit la « transparence envers les personnes, notamment pour les décisions visées par l'article 12.1 » parmi les livrables de la phase Plateforme (mois 3 à 9). L'obligation suit donc le rythme des phases, contrairement à l'encadré.
  - Le tableau 60 ne « lance » les EFVP des agents existants qu'aux semaines 9 et 10, avec pour livrable « EFVP planifiées ou en cours ». Entre-temps, un agent qui communique des RP hors Québec continue d'opérer, ce qui revient à une dérogation de fait à l'art. 17.
- **Contre-exemple** : un agent existant de tri de dossiers clients transmet des RP à un modèle hébergé aux États-Unis, sans EFVP. Le comité accorde une dérogation de six mois sur le point A.8, ce que la grille et le tableau 61 autorisent. L'entreprise viole alors l'art. 17 pendant toute la durée de cette dérogation, renouvelable une fois.
- **Correctif proposé** :
  - Marquer non dérogeable tout point de la grille qui reprend une obligation légale (A.5 décisions automatisées, A.8 EFVP et hors Québec, A.8 obligations du déployeur RIA, transparence).
  - Retirer « EFVP » de la liste des cibles dérogeables du § 15.3.
  - Retirer l'art. 12.1 des livrables de phase.
  - Prévoir, pour un agent existant non conforme à une obligation légale, la suspension ou une mise en conformité immédiate, et non un calendrier.
- **Confiance** : vérifié dans le texte (p. 169, 201, 202, 204, 205, 209-212)

### [21-02] [BLOQUANT] Plafond N2 « hors domaine » inapplicable pour les appels qui contournent la passerelle
- **Axe** : A
- **Localisation** :
  - Règles de progression, p. 202 : « Tant qu'un appel interdomaines d'un agent contourne la passerelle, les actions de cet agent hors de son domaine sont plafonnées à N2. »
  - Tableau 61, p. 205 : « 100 % dès le jalon 2 pour les agents N3 ».
  - A.6, p. 211 : « Tous Passerelle d'agents en coupure de tout appel […] interdomaine ».
- **Diagnostic** :
  - La règle admet qu'un appel interdomaines contourne la passerelle et prétend le borner à N2. Or le cadre confie à la passerelle à la fois l'application du plafond (EXIG-AUT-01 : « La passerelle d'agents DOIT refuser tout appel d'outil qui excède ce plafond ») et le recalcul de l'empreinte d'approbation avant exécution (EXIG-OBS-12). Sur le chemin qui contourne la passerelle, ni le plafond N2 ni l'approbation de chaque action ne peuvent être vérifiés : le plafond se réduit à une déclaration.
  - La règle introduit en outre un niveau par action (« actions hors de son domaine »), alors que le niveau est un attribut unique de l'agent au registre (EXIG-AUT-01).
  - Elle contredit enfin deux autres passages : la phrase qui la précède (« ne doit le faire que par la passerelle »), qui exclut le contournement, et la cible du tableau 61, qui exige 100 % pour les agents N3 dès J2.
  - La grille, qui exige la passerelle pour « Tous », impose plutôt une dérogation. Le même cas reçoit donc trois traitements : interdit, toléré à N2, dérogation.
- **Contre-exemple** : en phase Plateforme, un agent N3 intradomaine de classe modérée conserve un appel direct hérité vers l'API de facturation d'un autre domaine. Selon la règle, il y est « N2 ». Mais aucune file d'approbation n'intercepte cet appel, et l'agent écrit en P2 sans approbation : le comportement réel est N3 hors domaine, ce qui est précisément ce que la règle voulait interdire.
- **Correctif proposé** : remplacer la seconde phrase par une règle unique et applicable. Un agent dont un appel interdomaines contourne la passerelle ne peut être déclaré au-delà de N1 pour ces outils (lecture seule, retrait des outils en écriture hors domaine), ou alors l'appel est coupé. Aligner la grille et le tableau 61 sur cette règle.
- **Confiance** : vérifié dans le texte (EXIG-AUT-01 p. 104-105, EXIG-OBS-12 p. 150, p. 202, 205, 211)

### [21-03] [MAJEUR] E-23 : le chapitre 15 exige une validation que l'EXIG-CON-12 n'exige pas, et la présente comme externe
- **Axe** : A, C
- **Localisation** :
  - Tableau 58, p. 201 : « validation initiale des agents et des modèles inscrits à l'inventaire E-23 avant le 1er mai 2027 (EXIG-CON-12) ».
  - p. 203 : « la validation initiale E-23 reste exigible le 1er mai 2027 ».
- **Diagnostic** :
  - EXIG-CON-12 (p. 180) exige, au plus tard le 1er mai 2027, l'inscription à l'inventaire « avec propriétaire, cote de risque, version et état de validation ». Inscrire un état (par exemple « non validé, validation planifiée ») n'oblige pas à avoir validé.
  - L'encadré de la p. 202 reconnaît lui-même que l'état de validation est un ajout du cadre (« le cadre y ajoute l'état de validation »). Le chapitre 15 en fait pourtant une validation initiale complète, qu'il range parmi les « échéances externes » qui « ne bougent pas » et qui passent devant les jalons.
  - S'il fallait vraiment valider avant le 1er mai, le calendrier ne le permettrait pas : selon le tableau 59, la phase Plateforme s'ouvre à la mi-mars 2027, ce qui laisse environ six semaines pour valider tous les agents et modèles visés, y compris ceux des fournisseurs, avec une plateforme encore en construction.
- **Contre-exemple** : une institution financière fédérale exploite 40 agents qui s'appuient sur 12 modèles de fournisseurs. Lue au pied de la lettre, la feuille de route exige 52 validations en six semaines. EXIG-CON-12 n'en exige aucune avant cette date, seulement l'inscription de leur état.
- **Correctif proposé** : écrire « inventaire E-23 complet, avec l'état de validation de chaque agent et modèle, au 1er mai 2027 (EXIG-CON-12) », et planifier la validation selon la cote de risque. Si le cadre veut une validation préalable, il doit modifier EXIG-CON-12 et qualifier ce choix de « choix du cadre ».
- **Confiance** : vérifié dans le texte (p. 180, 201-203). L'exigence propre d'E-23 sur la validation à la date d'entrée en vigueur est à vérifier par l'audit bibliographique.

### [21-04] [MAJEUR] L'échéance MCP du 28 juillet 2027, choix du cadre, est traitée comme une échéance externe
- **Axe** : C
- **Localisation** :
  - p. 202 : « Les travaux qui découlent d'une échéance externe (J2a, la migration MCP exigée par EXIG-MCP-22 et la validation initiale E-23) sont datés par cette échéance ».
  - p. 203 : « Les échéances externes ne bougent pas : […] la migration MCP le 28 juillet 2027 ».
- **Diagnostic** : le « Pourquoi » de l'EXIG-MCP-22 (p. 66) dit au contraire : « l'échéance retenue, choix du cadre ». La spécification rend seulement certaines fonctions admissibles au retrait à partir de la première révision publiée le 28 juillet 2027 ou après. Classer cette date parmi les échéances externes lui donne deux privilèges : elle échappe au contrôle par les jalons (« le jalon qui précède ne les bloque pas ») et elle devient intangible, alors que le comité devrait pouvoir l'arbitrer contre d'autres priorités. Le tableau 59 la range d'ailleurs dans la colonne « Échéances externes à tenir ».
- **Contre-exemple** : la prochaine révision de MCP est annoncée pour le 30 mars 2027 (H.2). Le comité veut alors décaler la migration pour viser directement cette révision. Le chapitre 15 le lui interdit au motif d'une échéance « externe », alors qu'il s'agit de sa propre décision.
- **Correctif proposé** : distinguer deux catégories, les « échéances externes » (E-23, RIA, Loi 25) et les « échéances internes à date fixe » (EXIG-MCP-22). Les règles de priorité peuvent s'appliquer aux deux, mais il faut dire qui peut modifier la seconde et selon quelle procédure.
- **Confiance** : vérifié dans le texte (p. 66, 202, 203)

### [21-05] [MAJEUR] La dérogation au plafond de phase ouvre une brèche dans le plafond de classe, qui est non dérogeable
- **Axe** : A
- **Localisation** : règles de progression, p. 202 : « Un agent existant dont le niveau dépasse le plafond de la phase doit être ramené sous ce plafond […] ou faire l'objet d'une dérogation limitée dans le temps (section 11.6). »
- **Diagnostic** : le plafond effectif est le plus strict entre le plafond de phase et le plafond de classe (puce précédente). Or la dérogation offerte porte sur « le plafond de la phase », sans exclure le cas où le dépassement est aussi un dépassement du plafond de classe. Ce dernier est non dérogeable (EXIG-GOV-17, A.2). Le § 14 (p. 199) reprend la même formule pour tous les agents existants : « sous les plafonds de phase ou par dérogation bornée ». Pour un agent existant de classe élevée opérant en N3, la règle est donc indécidable.
- **Contre-exemple** : en semaine 10, un agent existant de classe élevée opère en N3, au-dessus du plafond de phase (N1) et du plafond de classe (N2). Le parrain demande une dérogation de six mois au titre de la règle de progression. Le texte du chapitre 15 permet de l'accorder, EXIG-GOV-17 l'interdit.
- **Correctif proposé** : écrire que la dérogation ne peut viser que l'écart entre le plafond de phase et le plafond de classe, jamais le dépassement de ce dernier. Un agent existant au-dessus de son plafond de classe est ramené sous ce plafond ou suspendu sans délai. Corriger le § 14 en conséquence.
- **Confiance** : vérifié dans le texte (p. 169, 199, 202, 209)

### [21-06] [MAJEUR] Agents existants pendant la phase Fondations : exploitation sans fiche ou avec une fiche incomplète
- **Axe** : A, B
- **Localisation** :
  - Tableau 60, p. 204 : « Ouvrir une fiche par agent (champs de l'étape Proposition, annexe B) » (semaines 3 et 4).
  - Annexe B, p. 212 : « avant cela, l'agent n'obtient aucun jeton d'exécution en production ».
  - Tableau 58, J1 : « registre complet ».
- **Diagnostic** :
  - EXIG-GOV-17 interdit, sans dérogation possible, « l'exploitation d'un agent sans fiche au registre ni parrain nommé ». Or, pendant les semaines 1 à 4, les agents existants (y compris les agents fantômes découverts) opèrent sans fiche, et le propriétaire métier n'est nommé qu'aux semaines 3 et 4. Le cadre ne dit pas s'ils sont suspendus ou tolérés.
  - Après les semaines 3 et 4, leur fiche ne contient que les champs de l'étape Proposition. L'annexe B la déclare donc incomplète, et un agent dont la fiche est incomplète n'obtient « aucun jeton d'exécution en production ». Appliquée à la lettre, la règle arrête toute la production existante.
  - « Registre complet » au J1 est ambigu : tous les agents inscrits, ou toutes les fiches complètes au sens de l'annexe B?
- **Contre-exemple** : en semaine 2, la sécurité découvre un agent fantôme dans un logiciel-service, qui opère pour 300 utilisateurs. EXIG-GOV-17 l'interdit sans dérogation possible, alors que le tableau 60 ne prévoit sa fiche que deux semaines plus tard. L'équipe ne sait pas si elle doit le couper.
- **Correctif proposé** : définir un statut transitoire « existant inventorié » (fiche minimale, parrain nommé dans les cinq jours ouvrables suivant la découverte, sinon désactivation), le soustraire explicitement à la règle de l'annexe B sur les jetons pendant la phase Fondations, et définir « registre complet » au J1 (fiche ouverte et parrain nommé pour 100 % des agents actifs).
- **Confiance** : vérifié dans le texte (p. 169, 201, 204, 212). La règle transitoire n'a été trouvée nulle part dans full.txt (recherche de « agent existant » et de « agents existants »).

### [21-07] [MAJEUR] Des points « Tous » de la grille dépendent de livrables de la phase Industrialisation, alors que J2 exige des pilotes homologués selon l'annexe A
- **Axe** : B, A
- **Localisation** :
  - Tableau 58, J2 : « pilotes homologués selon l'annexe A ».
  - A.7, p. 211 : « Tous Coûts : enveloppe appliquée à chaque étape, quotas et plafond mensuel par agent, […] imputation par centre de coûts ».
- **Diagnostic** : le § 14 (p. 199) exige que « tout nouvel agent » soit homologué selon l'annexe A, « quel que soit le niveau de l'entreprise ». Plusieurs points de la grille exigent pourtant des moyens que le tableau 58 ne livre qu'en Industrialisation (mois 9 à 18) :
  - « enveloppes budgétaires et imputation par centre de coûts » (point A.7 Coûts, applicable à Tous);
  - « évaluation continue dans la chaîne CI/CD » (point A.7 Évaluation, applicable à Tous, et cible de 100 % du tableau 61);
  - « équipe rouge régulière », alors que A.6 exige pour la classe modérée une « suite d'attaques intégrée à la chaîne d'intégration »;
  - « sagas et compensation », alors que A.4 exige quatre tests d'injection de fautes dans la chaîne d'intégration;
  - « toutes les interactions interdomaines par la passerelle », alors que A.6 l'exige pour Tous.

  Les pilotes de la phase Plateforme ne peuvent donc pas être homologués sans dérogations, ce qui rend le critère de J2 inatteignable tel qu'il est écrit.
- **Contre-exemple** : un pilote N2 de classe modérée, en juin 2027, ne peut produire ni la suite d'attaques en CI ni l'imputation par centre de coûts. Il obtient « Non conforme » sur deux points, et le comité doit accorder deux dérogations par pilote pour constater J2.
- **Correctif proposé** : soit avancer ces capacités, au moins sous une forme minimale, dans la phase Plateforme, soit indiquer dans la grille, pour chaque point, la phase à partir de laquelle il devient exigible, avec la mesure transitoire admise.
- **Confiance** : vérifié dans le texte (p. 199, 201, 210-211)

### [21-08] [MAJEUR] La justification de la cible de révocation de 15 minutes ne tient pas
- **Axe** : A
- **Localisation** : p. 206 : « elle correspond à la durée de vie cible des jetons délégués (section 9.3), qui borne l'exposition résiduelle si un système en aval accepte encore un jeton déjà émis ».
- **Diagnostic** :
  - L'indicateur mesure le temps écoulé jusqu'au « refus de son dernier appel, dans tous les systèmes ». Prenons un système en aval qui ne prend pas en charge SSF ni CAEP (cas prévu par EXIG-IAM-20 : « aux systèmes raccordés qui les prennent en charge »). Un jeton émis juste avant que la révocation prenne effet, au temps d (délai de décision et de propagation), y reste valable jusqu'à d + 15 min. Le pire cas est donc d + durée de vie, toujours supérieur à 15 min.
  - Assimiler la cible à la durée de vie confond deux grandeurs : le délai de révocation active et l'exposition résiduelle passive, qui s'additionnent.
  - De plus, EXIG-IAM-15 n'est qu'un DEVRAIT « lorsque le fournisseur d'identité le permet ». Le § 9.3 rappelle que, chez Entra, la durée par défaut est de 60 à 90 minutes et que CAE peut la porter à 28 heures. La cible repose donc sur une hypothèse que le cadre lui-même n'impose pas.
- **Contre-exemple** : décision d'arrêt à 10 h 00, identité désactivée à 10 h 04, jeton de 15 minutes émis à 10 h 03 vers un logiciel-service sans CAEP. Le dernier appel accepté a lieu à 10 h 17 : la cible est manquée alors que chaque composant respecte le cadre.
- **Correctif proposé** : décomposer l'indicateur en deux mesures, le délai de refus aux passerelles (cible de quelques minutes) et l'exposition résiduelle maximale (durée de vie maximale des jetons en circulation, par système). Fixer la cible sur la somme et faire du tableau de bord la liste des systèmes qui ne prennent pas en charge la révocation active.
- **Confiance** : déduit (raisonnement sur le texte des p. 122-127, EXIG-IAM-15 et EXIG-IAM-20, et p. 206)

### [21-09] [MAJEUR] La valeur de référence au J1 n'est pas mesurable pour la plupart des indicateurs
- **Axe** : B
- **Localisation** :
  - p. 205 : « la valeur de référence est mesurée au jalon 1 ».
  - p. 204 : « chaque indicateur doit être calculé à partir du registre, des passerelles, des traces et du journal d'audit ».
- **Diagnostic** : au J1 (fin de la phase Fondations), plusieurs sources de données n'existent pas encore :
  - le journal d'audit et l'approbation signée sont des livrables de la phase Plateforme;
  - la passerelle d'agents est ouverte en Plateforme;
  - l'évaluation en CI/CD et l'imputation par centre de coûts arrivent en Industrialisation;
  - le traçage ne porte que sur « deux ou trois agents représentatifs ».

  Traçabilité, Couverture des passerelles interdomaines, Couverture de l'évaluation, Approbation sans modification (aucune approbation n'existe en N0 et N1), Coût par tâche réussie, Délai d'intégration et Réutilisation n'ont donc pas de valeur de référence calculable au J1. Le tableau 60 (semaines 12 et 13) la demande pourtant.
- **Contre-exemple** : au J1, l'indicateur « Traçabilité » n'a pas de dénominateur, puisqu'aucune action P2 ou P3 n'est permise en Fondations, et pas de source, puisque le journal d'audit n'existe pas encore. La « référence » consignée est vide ou déclarée par les équipes, ce que la première règle interdit.
- **Correctif proposé** : pour chaque indicateur, indiquer le jalon de première mesure (J1, J2 ou J3) et la source disponible à ce moment; ne mesurer au J1 que la couverture du registre, les secrets et la passerelle de modèles.
- **Confiance** : vérifié dans le texte (p. 201, 204, 205)

### [21-10] [MAJEUR] Plusieurs indicateurs ne peuvent pas être « calculés » sans déclaration humaine
- **Axe** : B
- **Localisation** : p. 204 : « et non déclaré par les équipes ». Tableau 61 : « Inférieur au coût du processus de référence sans agent »; « Temps nécessaire pour brancher à un agent un outil déjà inscrit au catalogue ».
- **Diagnostic** : trois indicateurs exigent des données que ni le registre, ni les passerelles, ni les traces, ni le journal ne produisent :
  - le coût du processus de référence sans agent est une estimation comptable externe;
  - le délai d'intégration suppose un début et une fin de projet, données qui relèvent de l'outil de gestion de travail et non des traces;
  - « intervention humaine imprévue » (Réussite des tâches) exige de qualifier chaque intervention de prévue ou d'imprévue, et la « réussite » d'une tâche est un jugement.

  La règle « non déclaré » est donc impossible à respecter pour ces indicateurs, ou elle oblige à un instrumentation qui n'est pas spécifiée.
- **Contre-exemple** : une équipe déclare un coût de référence surévalué (traitement manuel à 40 $ par dossier) et son agent passe sous la cible. Rien dans les sources autorisées ne permet de le contester.
- **Correctif proposé** : admettre explicitement une catégorie « donnée de référence attestée » (coût de référence établi par la finance, daté et versé à la fiche), définir l'événement de début et de fin du délai d'intégration (inscription de la demande au catalogue jusqu'au premier appel réussi en trace), et définir « intervention imprévue » comme toute escalade non prévue au contrat d'agent.
- **Confiance** : vérifié dans le texte (p. 204-206)

### [21-11] [MAJEUR] Les critères du J4 sont sous-spécifiés et créent une incitation perverse
- **Axe** : B
- **Localisation** :
  - Tableau 58, J4 : « quatre trimestres consécutifs d'indicateurs conformes aux cibles chiffrées ».
  - Tableau 61 : « Aucun incident grave ».
  - p. 206 : « Une cible déclenche une analyse; elle ne sert pas à récompenser une équipe. »
- **Diagnostic** :
  - Plusieurs cibles sont propres à chaque agent (« Seuil fixé au contrat d'agent », « Fourchette fixée au contrat », « Seuil d'alerte fixé par cas d'usage »). Le texte ne dit pas comment on les agrège pour juger qu'un trimestre est « conforme » au niveau de l'entreprise : tous les agents, une proportion, une médiane?
  - Avec « Aucun incident grave », un seul incident grave remet le compteur de quatre trimestres à zéro, quel que soit le volume d'activité. Ce critère ne se normalise pas avec la croissance (le § 15.4 annonce des milliers d'agents).
  - Faire d'un jalon de certification un critère à zéro incident pousse à sous-classer la gravité des incidents, ce qui contredit l'encadré : la cible devient bel et bien un enjeu de récompense.
- **Contre-exemple** : au mois 33, une seule fuite de RP classée grave reporte J4, et donc l'audit ISO/IEC 42001 lancé à ce jalon, d'au moins un an. Le comité est alors tenté de reclasser l'incident en « modéré ».
- **Correctif proposé** : définir la règle d'agrégation (par exemple 95 % des agents dans leur seuil contractuel), remplacer « aucun incident grave » par un taux normalisé, assorti d'un délai de confinement et d'une analyse des causes close pour chaque incident grave, et confier le classement de gravité à une fonction indépendante de l'équipe mesurée.
- **Confiance** : déduit (lecture des p. 201, 205, 206)

### [21-12] [MAJEUR] La transition fondée sur des dérogations par agent risque d'engorger le comité
- **Axe** : B
- **Localisation** : tableau 60, semaines 5 et 6, p. 204 : « ce secret transitoire s'inscrit comme dérogation bornée dans le temps (EXIG-IAM-05, section 11.6) ». Voir aussi les règles de progression (p. 202) et le § 14 (p. 199) : « par dérogation bornée ».
- **Diagnostic** : la phase Fondations s'appuie sur des dérogations pour tous les secrets transitoires, pour les agents au-dessus du plafond de phase et, par effet du constat 21-07, pour les pilotes. Or :
  - une dérogation « vise un agent ou un composant précis, jamais une catégorie entière » (p. 30);
  - elle se demande par écrit, est instruite par l'architecture d'entreprise avec l'avis de la sécurité et des risques, puis est accordée par le comité (EXIG-GOV-15);
  - elle dure six mois au plus et ne se renouvelle qu'une fois (EXIG-GOV-16).

  Pour plusieurs centaines d'agents existants, cela représente des centaines de dossiers dans les semaines 5 à 10, juste au moment où le comité vient d'être mandaté. Le tableau 62 cite justement le risque de « Plateforme centrale devenue goulot », sans le transposer au comité.
- **Contre-exemple** : 400 agents inventoriés donnent 400 dérogations de secrets en semaine 6. Si la phase Plateforme glisse au-delà de janvier 2028, ces dérogations atteignent leur durée maximale de 12 mois et tous les agents passent à l'état « suspendu » (EXIG-GOV-16).
- **Correctif proposé** : créer un régime de « mesure transitoire de la feuille de route », approuvé une seule fois par le comité pour une cohorte inscrite au registre, avec une échéance liée au jalon et non à la durée de six mois. Si le cadre maintient le principe « jamais une catégorie », il doit chiffrer la charge prévue.
- **Confiance** : déduit (p. 30, 168, 199, 202, 204)

### [21-13] [MINEUR] Les points « non dérogeable » de la grille ne recoupent pas la liste de l'EXIG-GOV-17
- **Axe** : C
- **Localisation** :
  - A.6, p. 211 : « Si agit pour une personne non dérogeable Délégation explicite par échange de jetons; aucune usurpation; portée jamais élargie; jeton à audience unique; aucun relais de jeton ».
  - A.5 : « par jeton signé lié à l'action exacte ».
  - A.2 : « Fiche complète au registre : identifiant, version, […] équipe de garde, finalité, mandants autorisés ».
- **Diagnostic** : EXIG-GOV-17 ne rend non dérogeables que l'usurpation, l'action P3 sans approbation humaine et l'agent « sans fiche au registre ni parrain nommé ». La grille étend ce caractère à tout le paquet EXIG-IAM-08 à -12 (audience unique, absence de relais), à la forme signée de l'approbation et à la complétude de la fiche (équipe de garde, mandants). Les deux listes divergent sans que l'une renvoie à l'autre. Elles divergent aussi dans l'autre sens, voir 21-01.
- **Contre-exemple** : une dérogation sur l'audience unique (EXIG-IAM-10) est permise selon EXIG-GOV-17 et interdite selon A.6.
- **Correctif proposé** : faire de la grille la projection exacte de la liste de l'EXIG-GOV-17, ou modifier cette exigence pour qu'elle reprenne les ajouts de la grille.
- **Confiance** : vérifié dans le texte (p. 169, 209-211)

### [21-14] [MINEUR] Des points de la grille mêlent des exigences DOIT et DEVRAIT
- **Axe** : A
- **Localisation** :
  - A.1 point 2 : « Un écart à une exigence formulée avec DEVRAIT (par exemple EXIG-IAM-15 et −19) se justifie par écrit à la fiche, sans dérogation ».
  - A.6 : « Tous Profil OAuth […] — EXIG-IAM-13 à -16 » et point passerelle « EXIG-IAM-17, -18, -19, -21 ».
- **Diagnostic** : EXIG-IAM-15 et -19 sont des DEVRAIT, regroupés dans un même point avec des DOIT (IAM-13, -14, -16, -17, -18, -21). La grille n'admet que trois réponses par point. Un écart à IAM-15 rend tout le point « Non conforme », donc soumis à dérogation, alors que A.1 dit l'inverse : la grille ne permet pas de trancher.
- **Correctif proposé** : isoler les exigences DEVRAIT dans des points distincts ou ajouter la réponse « Écart justifié (DEVRAIT) ».
- **Confiance** : vérifié dans le texte (p. 123, 129, 209, 211)

### [21-15] [MINEUR] La grille ne vérifie pas le plafond de phase
- **Axe** : C
- **Localisation** : A.2, p. 209 : « Niveau d'autonomie déclaré (N0 à N4), dans le plafond de la classe de risque ».
- **Diagnostic** : la règle de progression (p. 202) combine plafond de phase et plafond de classe, mais la grille, qui conditionne la mise en production, ne contrôle que le second. Un agent faible N3 pourrait être homologué en phase Fondations.
- **Correctif proposé** : écrire « dans le plafond de la classe de risque et de la phase en cours (tableau 58) ».
- **Confiance** : vérifié dans le texte

### [21-16] [MINEUR] Qui remplit la grille : A.1 contredit la matrice RACI pour la classe élevée et pour N4
- **Axe** : C
- **Localisation** : A.1, p. 209 : « Le responsable technique de l'agent remplit la grille et joint les preuves ».
- **Diagnostic** : selon le § 11.2 (p. 162), pour un agent de classe élevée ou visant N4, « le comité devient A pour le niveau d'autonomie et l'homologation, et le propriétaire métier devient R ». A.1 reprend le passage du rôle A au comité mais laisse le rôle R au responsable technique.
- **Correctif proposé** : ajouter « pour la classe élevée ou N4, le propriétaire métier en répond (R) ».
- **Confiance** : vérifié dans le texte

### [21-17] [MINEUR] A.5 déforme le moment de l'avis exigé par l'art. 12.1
- **Axe** : A
- **Localisation** : A.5, p. 211 : « avis au plus tard au moment de la décision ».
- **Diagnostic** : l'art. 12.1, tel que le cadre le cite lui-même (p. 115 et 174), et l'exigence correspondante fixent l'avis « au plus tard au moment où la décision lui est communiquée ». Le moment de la décision et le moment de sa communication diffèrent dans un traitement asynchrone. La grille introduit donc une troisième formulation.
- **Correctif proposé** : reprendre la formule de l'exigence.
- **Confiance** : vérifié dans le texte

### [21-18] [MINEUR] J2a ne retient que les six mois du RIA pour la conservation des journaux, alors que le cadre exige 24 mois
- **Axe** : C
- **Localisation** : p. 203 : « dont une conservation des journaux configurée pour au moins six mois ».
- **Diagnostic** : EXIG-OBS-13 impose au moins 24 mois et EXIG-CON-16 précise que « le cadre exige davantage ». Comme critère de jalon, « au moins six mois » laisse croire que six mois suffisent.
- **Correctif proposé** : écrire « au moins six mois au sens du RIA, 24 mois selon EXIG-OBS-13 ».
- **Confiance** : vérifié dans le texte (p. 150, 181, 203)

### [21-19] [MINEUR] La règle d'interdiction de J2a est plus stricte que le régime transitoire du RIA sans être présentée comme un choix du cadre
- **Axe** : A
- **Localisation** : p. 203 : « À compter du 2 décembre 2027, les sorties d'un agent visé qui ne satisfait pas à ces critères ne doivent pas être utilisées dans l'Union. »
- **Diagnostic** : d'après mes connaissances, l'art. 111(2) du RIA exempte les systèmes à haut risque mis en service avant la date d'application, sauf modification importante de leur conception (avec un régime particulier pour les autorités publiques). La règle de J2a vise tout agent, y compris ceux mis en service avant cette date. C'est défendable, mais il faut le qualifier de choix du cadre, comme le cadre le fait ailleurs. Le tableau 62 (« dont la mise en service est prévue à compter du 2 décembre 2027 ») suggère d'ailleurs la lecture fondée sur la date de mise en service.
- **Correctif proposé** : ajouter « (choix du cadre, plus strict que l'art. 111) » ou aligner la règle sur la date de mise en service.
- **Confiance** : à vérifier (source externe : art. 111 du RIA tel que modifié par le règlement (UE) 2026/1744)

### [21-20] [MINEUR] Tableau 59 : l'annexe I n'a pas de jalon, et deux échéances sont mal placées
- **Axe** : C
- **Localisation** : tableau 59, p. 203 : ligne « Début juill. 2028 | J3 | RIA, annexe I, le 2 août 2028 ». Ligne « Juill. 2028 – 2030 » : « Examen formel du NIST AI RMF au plus tard en 2028 ».
- **Diagnostic** :
  - Le 2 août 2028 tombe pendant la phase Mise à l'échelle, après J3, mais il est rangé sur la ligne de J3.
  - Aucun jalon de type J2a n'est prévu pour les obligations de l'annexe I, alors que J2a existe pour l'annexe III.
  - L'examen du NIST peut survenir entre janvier et juin 2028, donc pendant la phase Industrialisation, mais il est rangé dans la ligne Mise à l'échelle.
- **Correctif proposé** : déplacer ces deux échéances sur des lignes datées, et soit ajouter un jalon J3a pour l'annexe I, soit déclarer explicitement que les agents relevant de l'annexe I sont hors de portée.
- **Confiance** : vérifié dans le texte

### [21-21] [MINEUR] L'expiration d'une ébauche OAuth figure parmi les « échéances externes à tenir »
- **Axe** : C
- **Localisation** : tableau 59, ligne J1 : « Expiration de l'ébauche OAuth 2.1 −16 le 7 mars 2027 ».
- **Diagnostic** : l'expiration d'un Internet-Draft n'impose rien à l'entreprise, puisque la référence normative reste OAuth 2.0. C'est un signal de veille, pas une échéance. La caducité de la −16, remplacée par la −17 qui expire le 4 mai 2027, est déjà consignée à l'annexe H, dans le tableau des signaux et non en H.4. Le classement en « échéance » est, lui, un constat nouveau. L'arithmétique de 185 jours est exacte (du 3 sept. 2026 au 7 mars 2027).
- **Correctif proposé** : déplacer la mention dans une colonne « Signaux de veille » ou la supprimer du tableau 59.
- **Confiance** : vérifié dans le texte (p. 203; annexe H)

### [21-22] [MINEUR] Vacances de la construction : l'échéance MCP avancée de fait n'est pas reportée ailleurs
- **Axe** : C, B
- **Localisation** : tableau 59, p. 203 : « migration MCP le 28 juillet 2027, à terminer avant les vacances de la construction (deux dernières semaines de juillet) ».
- **Diagnostic** :
  - Les deux dernières semaines de juillet englobent le 28 juillet. Terminer avant ces vacances revient à fixer une échéance interne vers le 16 juillet 2027, que ni le tableau 61 (« au 28 juillet 2027 »), ni le tableau 62 (« à trois mois de l'échéance du 28 juillet »), ni la grille ne reprennent.
  - La règle d'allongement de deux semaines pour les vacances de la construction est généralisée à toute organisation, alors que ce congé collectif est propre à l'industrie de la construction. Beaucoup de services informatiques ne ferment pas à ce moment.
- **Correctif proposé** : soit nommer explicitement l'échéance interne et la reporter dans les tableaux 61 et 62, soit retirer la mention. Présenter les congés collectifs comme un paramètre à fixer par l'entreprise.
- **Confiance** : vérifié dans le texte. Les dates exactes des vacances de la construction en 2027 sont à vérifier.

### [21-23] [MINEUR] Les « 90 premiers jours » durent environ 105 jours civils
- **Axe** : C
- **Localisation** : § 15.2, p. 203 : « Ces 13 semaines sont des semaines travaillées : une période de congés collectifs s'y ajoute ».
- **Diagnostic** : 13 semaines travaillées plus 2 semaines de congés donnent environ 15 semaines, soit environ 105 jours (du 1er décembre à la mi-mars, selon le tableau 59). Le titre « Les 90 premiers jours » est donc trompeur pour qui pilote en jours civils.
- **Correctif proposé** : écrire « Les 13 premières semaines travaillées ».
- **Confiance** : vérifié dans le texte

### [21-24] [MINEUR] Le tableau 58 ne mentionne que les serveurs MCP, le tableau 60 inclut les clients
- **Axe** : C
- **Localisation** : tableau 58, Fondations, p. 201 : « chaque serveur MCP antérieur y étant inscrit avec sa date de migration ». Tableau 60, semaines 7 et 8 : « chaque serveur et client MCP antérieur ».
- **Diagnostic** : EXIG-MCP-22 vise les serveurs et les clients. Le livrable de la phase Fondations omet les clients, alors que le plan détaillé et J2 les incluent.
- **Correctif proposé** : écrire « chaque serveur et client MCP antérieur » au tableau 58.
- **Confiance** : vérifié dans le texte

### [21-25] [MINEUR] Les cibles « au jalon 1 » du tableau 61 ne figurent pas parmi les critères de sortie du J1
- **Axe** : C
- **Localisation** : tableau 58, J1 : « registre complet, comité en fonction ». Tableau 61 : « 100 % au jalon 1 » (secrets), « Modèles : 100 % au jalon 1 ».
- **Diagnostic** : le texte ne dit pas si J1 peut être constaté alors que les secrets partagés ou les appels directs aux fournisseurs ne sont pas à 100 %. Le tableau 60 en fait des livrables des semaines 5 et 6, mais le tableau 58 ne les reprend pas comme critères.
- **Correctif proposé** : ajouter les deux cibles aux critères de J1, ou préciser qu'il s'agit de cibles de pilotage et non de critères bloquants.
- **Confiance** : vérifié dans le texte

### [21-26] [MINEUR] La liste des cibles non ajustables du tableau 61 est incomplète
- **Axe** : C
- **Localisation** : p. 205 : « sauf celles qui reprennent une exigence (registre, secrets, passerelles, traçabilité, EFVP) ».
- **Diagnostic** : deux cibles reprennent elles aussi une exigence mais ne figurent pas dans l'exception. « Conformité au catalogue » reprend EXIG-MCP-22 et EXIG-INT-04 et -06. « Couverture de l'évaluation » reprend EXIG-EVA. Le comité pourrait donc assouplir par écrit la cible MCP du 28 juillet 2027, que le § 15.1 dit pourtant immuable.
- **Correctif proposé** : énumérer les exigences reprises par identifiant, ou ajouter « catalogue, évaluation » à la liste.
- **Confiance** : vérifié dans le texte

### [21-27] [MINEUR] L'indicateur de couverture du registre ne voit que les agents déjà connus
- **Axe** : B
- **Localisation** : tableau 61 : « Part des agents actifs, déclarés ou découverts, qui ont une fiche à jour au registre », avec une cible de 100 %.
- **Diagnostic** : le dénominateur ne comprend que les agents connus. Un agent fantôme non découvert n'abaisse pas le taux, si bien que 100 % mesure l'efficacité de la tenue du registre, pas la couverture réelle.
- **Correctif proposé** : y adjoindre un indicateur de découverte (agents découverts hors registre pendant le trimestre, et délai entre la première trace réseau ou le consentement OAuth et l'inscription au registre).
- **Confiance** : déduit

### [21-28] [MINEUR] La quote-part de plateforme désavantage les premiers pilotes
- **Axe** : B
- **Localisation** : tableau 61 : « Coût total imputé (inférence, outils, quote-part de la plateforme) ». § 15.4, facteur 5 : « un pilote qui ne fait pas mieux s'arrête ou se redéfinit ».
- **Diagnostic** : en phase Plateforme, la quote-part se répartit sur très peu de tâches. Les premiers pilotes ont donc toutes les chances d'échouer à la comparaison et d'être arrêtés pour un coût qui disparaîtrait à l'échelle.
- **Correctif proposé** : pour le critère d'arrêt d'un pilote, comparer le coût marginal (inférence et outils) et suivre la quote-part à part.
- **Confiance** : déduit

### [21-29] [MINEUR] Multiagent : le ratio « 3 à 10 fois » cohabite avec le ratio d'environ 3,75 tiré d'Anthropic
- **Axe** : C, B
- **Localisation** : p. 206 : « une architecture multiagent consomme habituellement de 3 à 10 fois plus de jetons qu'un agent unique[275] ».
- **Diagnostic** : le § 2.1 (p. 16) et le § 7.1 citent Anthropic [17] : environ 4 fois une conversation pour un agent, environ 15 fois pour un système multiagent, soit environ 3,75 fois par rapport à un agent unique. La fourchette « 3 à 10 », attribuée à une autre source [275], et l'adverbe « habituellement » ne se déduisent pas de [17]. La borne haute est à vérifier.
- **Correctif proposé** : citer la fourchette exacte de [275], ou s'en tenir au ratio dérivé de [17] en précisant le banc d'essai.
- **Confiance** : à vérifier (source externe [275])

### [21-30] [MINEUR] Le facteur 6 annonce des livrables de la phase Plateforme absents du tableau 58
- **Axe** : C
- **Localisation** : p. 206 : « Les files d'approbation, les seuils et les indicateurs de la section 8.7 font partie des livrables de la phase Plateforme. »
- **Diagnostic** : le tableau 58 ne mentionne que l'« approbation humaine signée ». Ni les files priorisées, ni la rotation des approbateurs, ni les indicateurs de supervision n'y figurent, alors que le tableau 62 les invoque comme parade.
- **Correctif proposé** : les ajouter aux livrables de la phase Plateforme du tableau 58.
- **Confiance** : vérifié dans le texte

### [21-31] [MINEUR] Exercice trimestriel du coupe-circuit « pour l'agent » : le texte ne dit pas comment il passe à l'échelle
- **Axe** : B
- **Localisation** : A.4, p. 210 : « Coupe-circuit opérationnel pour l'agent et inclus dans l'exercice trimestriel ».
- **Diagnostic** : le texte ne dit pas si chaque agent doit être exercé chaque trimestre, ce qui paraît irréaliste face aux volumes que le § 15.4 cite (« plus de 150 000 agents » par entreprise d'ici 2028), ou si un échantillon suffit. Le tableau 61 mesure un seul délai par exercice.
- **Correctif proposé** : préciser le périmètre de l'exercice : échantillon par classe de risque, avec tous les agents de classe élevée et N4, plus une rotation des autres.
- **Confiance** : déduit

## Points forts
- L'arithmétique calendaire est cohérente : les mois 0, 3, 9, 18, 36 et 48 correspondent aux dates du tableau 59, avec la marge de congés, et l'expiration de la −16 tombe exactement 185 jours après sa publication.
- La règle « le plus strict » entre plafond de phase et plafond de classe, et la datation des travaux réglementaires par leur échéance plutôt que par la durée des phases, sont bien construites.
- Les indicateurs sont reliés aux exigences, aux sous-catégories du NIST AI RMF (GOVERN 1.6, MANAGE 2.4, citées correctement) et à des risques précédés de leurs signes avant-coureurs.

## Questions pour l'audit bibliographique
- p. 204 et 206, [2] Gartner, 28 avril 2026 : « plus de 150 000 agents » par entreprise du Fortune 500 d'ici 2028, contre « moins de 15 en 2025 », et constat sur l'IA fantôme. Population, méthode et formulation exacte, et rôle de [467] (Computerworld) comme relais.
- p. 206, [95] Gartner, 26 mai 2026 : « 40 % des entreprises rétrograderont ou désactiveront des agents autonomes d'ici 2027 ».
- p. 206, [3] Gartner, 25 juin 2025 : plus de 40 % de projets annulés d'ici la fin de 2027. Je le crois exact; à confirmer.
- p. 206, [275] Phillips (Anthropic, 23 janvier 2026) : fourchette « 3 à 10 fois » et son contexte.
- p. 202, [8] E-23 : la ligne directrice vise-t-elle les modèles « à risque non négligeable »? Exige-t-elle que la validation soit faite à la date d'entrée en vigueur, ou seulement le cadre de gestion et l'inventaire?
- p. 202, [57, 58] règlement (UE) 2026/1744 (du 8 juillet 2026, JO du 24 juillet 2026) : dates du 2 décembre 2027 (annexe III) et du 2 août 2028 (annexe I), et maintien ou modification de l'art. 111(2). Le texte n'a pas pu être lu le 1er novembre selon H.5.
- p. 206, [76] IMDA, Model AI Governance Framework for Agentic AI v1.5 : la recommandation de surveiller conjointement le taux d'approbation et le temps de réponse.
- p. 206, [407] FinOps Foundation : la recommandation de commencer par la refacturation indicative (showback).
- p. 204, [91] OWASP NHI Top 10 2025 : NHI2 (fuite de secrets), NHI7 (secrets de longue durée) et NHI9 (réutilisation). Je les crois exacts.
- p. 206, [314] : le biais d'automatisation « touche les novices comme les experts » et « ne se prévient pas par la seule formation » (vraisemblablement Parasuraman et Manzey, 2010).
- p. 212, [92] Microsoft Entra Agent ID : l'attestation du parrain tous les 6 à 12 mois.
- p. 203 : le NIST AI RMF prévoit-il un examen formel « au plus tard en 2028 »? Je le crois exact.
- p. 203 : les dates des vacances de la construction 2027 au Québec (CCQ).

audit_21.md : 31 constats (2 BLOQUANT, 10 MAJEUR, 19 MINEUR)
