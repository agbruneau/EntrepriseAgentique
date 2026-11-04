# Audit chunk_02 — pages 11-22

## Synthèse
Le chunk couvre le ch. 1 (objet, portée, force normative, identifiants, révision, méthode), le ch. 2 (données de contexte, chronologie des standards, huit enjeux, « pourquoi maintenant ») et le début du § 3.1 (tableau 7, échelles N0-N4). Texte dense, bien sourcé et prudent sur les chiffres. Ses défauts touchent surtout les méta-règles. Les trois plus graves :
(1) le catalogue « fait foi » sur les versions, alors que des blocs DOIT figent MCP 2026-07-28 et A2A 1.0;
(2) « les engagements contractuels priment toujours » ouvre une brèche dans les exigences non dérogeables;
(3) les règles de préséance (« la plus stricte », catalogue, § 4.3) tombent elles-mêmes hors du périmètre normatif que fixe le § 1.4.

## Constats

### [02-01] [MAJEUR] Le catalogue « fait foi » contre des versions figées dans des blocs DOIT
- **Axe** : A
- **Localisation** : § 1.6, p. 14 : « Les versions applicables, comme MCP 2026-07-28 ou A2A 1.0, sont fixées au catalogue et non dans le texte : en cas d’écart, le catalogue fait foi. »
- **Diagnostic** : l'affirmation « non dans le texte » est fausse. L'EXIG-A2A-01 (p. 68) exige « A2A, version de protocole 1.0 », et l'EXIG-MCP-22 (p. 67) exige d'« avoir migré vers la révision 2026-07-28 au plus tard le 28 juillet 2027 ». Le catalogue n'est pas une source normative au sens du § 1.4 (blocs EXIG, PRIN, tableaux visés par une exigence), et il n'apparaît pas non plus dans l'ordre de préséance du § 4.3 (p. 29). Un artefact hors du document, révisé chaque trimestre, l'emporte donc sur des obligations versionnées et révisées chaque semestre par le comité. Le cadre peut ainsi être amendé sans passer par son propre processus de révision (§ 1.6, « numéro de version et une date »).
- **Contre-exemple** : la révision MCP de mars 2027 (annoncée en H.2, p. 279) entre au catalogue. L'EXIG-MCP-22 exige toujours la migration vers 2026-07-28 avant juillet 2027, tandis que le catalogue désigne une autre cible. Les équipes ne savent pas laquelle des deux obligations remplir, et l'audit ne sait pas contre quoi homologuer.
- **Correctif proposé** : soit retirer les numéros de version des énoncés DOIT et les remplacer par « la version inscrite au catalogue au statut Adopter », soit inscrire au § 1.4 que les entrées du catalogue font partie du périmètre normatif et que le comité les approuve, avec une place explicite dans l'ordre du § 4.3.
- **Confiance** : vérifié dans le texte.

### [02-02] [MAJEUR] « Les engagements contractuels priment toujours » : une brèche dans le non-dérogeable
- **Axe** : A
- **Localisation** : § 1.6, p. 14 : « Le droit applicable et les engagements contractuels priment toujours (section 4.3). » Voir aussi le § 4.3, p. 29, rang 1 : « qu’aucun principe ne peut écarter ».
- **Diagnostic** : l'entreprise est elle-même partie à ses contrats. Mettre ses engagements contractuels au-dessus du cadre, y compris au-dessus de l'EXIG-GOV-17 (non dérogeable, p. 169), revient à permettre que la signature d'un contrat produise l'effet d'une dérogation interdite. Le chapitre 13 (clauses normatives) suppose l'inverse : c'est le cadre qui doit contraindre les contrats. La règle est circulaire.
- **Contre-exemple** : un contrat de logiciel-service accepte que l'agent du fournisseur exécute seul des remboursements (P3) ou qu'il ne transmette pas l'identité du mandant. Au rang 1 de la préséance, ce contrat écarte l'EXIG-GOV-17 sans aucune dérogation.
- **Correctif proposé** : limiter la primauté aux engagements contractuels antérieurs à l'adoption du cadre, pour la seule durée d'une transition bornée et inscrite au registre. Ajouter qu'aucun nouvel engagement ne peut être pris contre une exigence non dérogeable (renvoi à l'EXIG-GOV-17 et au § 13.3).
- **Confiance** : vérifié dans le texte (le scénario est déduit).

### [02-03] [MAJEUR] « La plus stricte s'applique » : aucun ordre défini entre règles incomparables
- **Axe** : A
- **Localisation** : § 1.6, p. 14 : « lorsqu’une règle du cadre et celle d’une autre politique visent le même objet, la plus stricte s’applique, et toute contradiction est soumise au comité. »
- **Diagnostic** : la notion de « plus stricte » suppose un ordre total entre les règles. Or deux règles peuvent viser le même objet dans des directions opposées : l'une minimise, l'autre conserve. Le texte ne dit pas non plus quel régime s'applique pendant que le comité tranche. Le report 9 du H.3 (p. 280) soulève une variante du problème, pour deux régimes réglementaires; il ne s'agit pas d'un erratum consigné en H.4.
- **Contre-exemple** : la politique de gouvernance des données impose d'effacer des RP après 12 mois, alors que le journal d'audit du cadre (§ 10.3) exige de conserver les actions à effet plus longtemps. Aucune des deux règles n'est « plus stricte » que l'autre. En attendant la décision du comité, l'équipe ne sait ni effacer ni conserver sans enfreindre l'une d'elles.
- **Correctif proposé** : (a) définir « plus stricte » dimension par dimension : la plus restrictive pour l'accès et l'autonomie, la plus longue pour la conservation de la preuve, sous réserve du droit; (b) fixer un régime provisoire, par exemple la règle qui préserve la preuve et réduit l'action, jusqu'à la décision du comité; (c) faire consigner l'arbitrage au registre.
- **Confiance** : vérifié dans le texte (le scénario est déduit).

### [02-04] [MAJEUR] Les méta-règles et les définitions qui « font foi » tombent hors du périmètre normatif
- **Axe** : C
- **Localisation** : § 1.4, p. 13 : « Seuls ces blocs d’exigences (chapitres 5 à 13), les principes directeurs PRIN-01 à PRIN-12 (chapitre 4) et les tableaux auxquels une exigence renvoie expressément créent une obligation normative ». § 3.1, p. 20 : « Les définitions du tableau 7 font foi dans tout le cadre ».
- **Diagnostic** : selon le § 1.4, sont seulement informatives les règles qui arbitrent tout le reste :
  - la règle du doute sur la portée (§ 1.2, p. 12);
  - la non-réattribution des identifiants (§ 1.5);
  - la règle de la plus stricte et la primauté du catalogue (§ 1.6);
  - l'ordre de préséance du § 4.3, qui est un texte du chapitre 4 et non un bloc PRIN.

  Le tableau 7 et « Les deux échelles » (p. 22) énoncent des prescriptions, par exemple « une action P3 exige une approbation hors bande » ou « Passage obligatoire », et « font foi ». Pourtant aucune exigence ne renvoie au tableau 7 (vérifié par Grep). Le § 8.1 (p. 106) affirme aussi que « seule l’échelle du présent chapitre fait foi » : deux textes revendiquent donc l'autorité sur l'échelle N0-N4.
- **Contre-exemple** : un agent est contesté en homologation. Son équipe soutient que la règle du doute (§ 1.2) et la préséance du § 4.3 sont informatives au sens du § 1.4 et ne s'imposent donc pas à elle. Le texte lui donne raison à la lettre.
- **Correctif proposé** : ajouter au § 1.4 une catégorie « règles d'interprétation », normatives, qui couvre les § 1.2 (critère et règle du doute), 1.5, 1.6, 4.3 et le tableau 7. Désigner une seule source qui fait foi pour l'échelle N0-N4 (le tableau 28) et faire du § 3.1 un résumé qui y renvoie.
- **Confiance** : vérifié dans le texte.

### [02-05] [MAJEUR] Méthode du § 1.7 : couverture et reproductibilité non démontrées
- **Axe** : B
- **Localisation** : § 1.7, p. 14 : « Chaque fait a ensuite été vérifié, aux 27 et 28 octobre 2026, contre des sources primaires ou, à défaut, secondaires reconnues, en trois passes ».
- **Diagnostic** :
  - Le § 1.7 ne chiffre que la base de 121 références. Or le corps en cite 473 (annexe G). Selon l'annexe F (p. 242), l'audit final a porté sur 428 références, puis 49 sources ont été ajoutées : 428 + 49 = 477, contre 473 annoncées. L'écart n'est pas expliqué, et rien n'indique que les sources ajoutées après l'audit aient été contrôlées.
  - Aucun registre de vérification par affirmation n'est publié (affirmation, source, date, verdict). Le résultat n'est donc pas reproductible par un tiers.
  - Le tableau 5 porte le titre « Chronologie vérifiée », mais il contient une date que l'annexe H tient pour non vérifiée (« approbation du conseil d’administration le 4 août », p. 17). **Déjà consigné en H.4 (n° 2)** et en H.5 : c'est la preuve qu'un fait non vérifié a franchi les trois passes.
  - Toutes les passes ont eu lieu en deux jours, alors que la base initiale comptait 50 % de sources de catégorie C, dont 33 « générées en série » (F.2, p. 242). La charge rend la vérification exhaustive peu plausible sans outillage documenté.
- **Contre-exemple** : un auditeur interne veut retracer l'affirmation « 4,99 M$ US » (p. 16). Il ne trouve ni la passe ni la date de contrôle ni le verdict, et la référence [19] renvoie à une page générique.
- **Correctif proposé** : publier en annexe F, ou en pièce jointe, le registre des 1 409 affirmations avec leur source, leur date, leur passe et leur verdict. Concilier les décomptes 428 / 49 / 473. Mettre à jour le § 1.7 avec les chiffres de l'audit final et la couverture réelle des références ajoutées après celui-ci.
- **Confiance** : vérifié dans le texte (la plausibilité de la charge est déduite).

### [02-06] [MAJEUR] Exemple multiplateforme : la passerelle d'entreprise n'est pas sur le chemin entre logiciels-services
- **Axe** : B
- **Localisation** : § 2.4, p. 19-20 : « Le mandant, l’identifiant de trace et les plafonds de la tâche doivent pourtant la suivre de bout en bout. » Puis : « Le cadre place ce point de contrôle neutre au niveau du transport : passerelle d’agents, identité et registre ».
- **Diagnostic** : dans l'exemple (Copilot Studio, puis Agentforce par A2A, puis ServiceNow par MCP), le second saut part de l'infrastructure de Salesforce vers celle de ServiceNow. La passerelle de l'entreprise n'y est que si l'entreprise force le point de terminaison MCP de ServiceNow à n'être joignable qu'à travers elle. Il faut aussi qu'Agentforce propage `traceparent` et un jeton délégué (`act`). Ni l'un ni l'autre ne dépend du transport : ce sont des capacités du fournisseur, que le chapitre 13 doit obtenir par contrat (EXIG-APP-08, p. 192). Par ailleurs, ni l'identité ni le registre ne sont des éléments « du transport ». Le chapitre présente comme résolu un problème que le cadre déplace en réalité vers l'approvisionnement.
- **Contre-exemple** : Agentforce appelle directement l'instance ServiceNow avec un compte d'intégration. La passerelle ne voit rien, la trace s'interrompt au deuxième saut et les plafonds de la tâche ne sont pas appliqués. Le scénario reproduit exactement les enjeux 4 et 5 du tableau 6.
- **Correctif proposé** : énoncer la condition explicitement : le point de contrôle n'est neutre que si les points de terminaison des systèmes d'enregistrement ne sont joignables que par la passerelle. Renvoyer aux clauses de propagation du contexte (§ 13.3) pour les sauts entre deux logiciels-services. Remplacer « au niveau du transport » par « au point d'entrée des interfaces de l'entreprise ».
- **Confiance** : déduit. La configuration réseau réelle des plateformes est à vérifier.

### [02-07] [MINEUR] Blogues de fournisseurs classés B, contrairement à la définition de la catégorie C
- **Axe** : C
- **Localisation** : § 1.7, p. 14 : « C, blogues de positionnement ou agrégateurs. Seules les catégories A et B sont citées. » Le § 2.4 (p. 19) cite TrueFoundry et MuleSoft [44, 45].
- **Diagnostic** : l'annexe F (p. 245) classe [44] et [45] en catégorie B. Ce sont pourtant des billets d'éditeurs de passerelles qui défendent leur propre thèse, soit exactement la définition de « blogue de positionnement ». Le texte le reconnaît d'ailleurs : « Ces fournisseurs ont un intérêt commercial dans la thèse ». La règle « seules A et B » n'est donc respectée que parce que le classement est indulgent.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : reclasser [44] et [45] en C, puis les retirer ou les citer sous une rubrique explicite « allégations de fournisseurs ». Sinon, amender la définition de C.
- **Confiance** : vérifié dans le texte.

### [02-08] [MINEUR] La version 1.0, datée du 27 octobre, intègre un audit du 28 octobre
- **Axe** : C
- **Localisation** : § 1.7, p. 14, « aux 27 et 28 octobre 2026 ». L'historique (p. 2) date la version 1.0 du « 27 oct. 2026 » et y inclut l'« Audit final du 28 octobre 2026 ».
- **Diagnostic** : une version ne peut pas intégrer un audit postérieur à sa date. Le § 1.7 attribue les trois passes à la version 1.0 sans dire ce que la version 1.1 a fait vérifier.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : dater la version 1.0 du 28 octobre ou rattacher l'audit final à la version 1.1, puis aligner le § 1.7 et l'annexe F.
- **Confiance** : vérifié dans le texte.

### [02-09] [MINEUR] « N + M contrats » : la gouvernance reste en N × M
- **Axe** : B
- **Localisation** : § 2.3, figure 2, p. 18 : « 4 + 5 = 9 contrats réutilisables, une politique ». Voir aussi « 50 agents et 200 systèmes représentent 10 000 intégrations potentielles, contre 250 contrats ».
- **Diagnostic** : la réduction vaut pour les contrats d'interface. Elle ne vaut pas pour les autorisations : chaque couple agent-outil exige une portée, un palier et une version épinglée, ce qui reste en O(N × M) dans le meilleur des cas. La comparaison oppose aussi un maximum théorique (N × M) au nombre réel de contrats, au lieu de partir des arêtes effectivement utilisées. Enfin, la condition « que si le catalogue est unique » se heurte au § 2.4 et au § 11.4 : chaque plateforme a son registre, et le registre d'entreprise est « alimenté par plusieurs sources ».
- **Contre-exemple** : 50 agents utilisent chacun 6 des 200 systèmes. Le maillage réel compte 300 intégrations, et non 10 000. Le gain réel, de 300 à 250 contrats, est marginal, alors que la matrice d'autorisation compte toujours 300 entrées.
- **Correctif proposé** : présenter le gain comme une réduction des contrats et du code de connexion, et non de la politique. Nuancer « une politique » en « un point d'application ».
- **Confiance** : déduit.

### [02-10] [MINEUR] Le multiplicateur de jetons d'Anthropic est généralisé hors de son contexte
- **Axe** : B
- **Localisation** : § 2.1, p. 16 : « selon Anthropic, un agent consomme environ 4 fois plus de jetons qu’une conversation, et un système multiagent environ 15 fois plus[17] ».
- **Diagnostic** : la source [17] décrit le système de recherche multiagent d'Anthropic, mesuré sur des tâches de recherche. Le texte en fait une propriété générale des agents.
- **Contre-exemple** : un agent N1 de classement, qui fait un seul appel d'outil, consomme à peine plus qu'une conversation.
- **Correctif proposé** : ajouter « dans son système de recherche multiagent, sur des tâches de recherche ».
- **Confiance** : à vérifier (source externe). Ma mémoire de [17] situe ces chiffres dans ce contexte.

### [02-11] [MINEUR] Chiffres d'IBM et de Ponemon : la population est mal décrite
- **Axe** : B
- **Localisation** : § 2.1, p. 16 : « 13 % des organisations ont déclaré une violation touchant un modèle ou une application d’IA ».
- **Diagnostic** : l'étude Cost of a Data Breach ne porte, à ma connaissance, que sur des organisations qui ont subi une violation. « 13 % des organisations » se lit alors comme « 13 % des organisations ayant subi une violation ». Il en va de même pour « une organisation sur cinq ».
- **Contre-exemple** : un lecteur en conclut que 13 % de toutes les entreprises ont subi une violation liée à l'IA. C'est une surestimation, faute de dénominateur.
- **Correctif proposé** : préciser la population (« parmi les organisations étudiées, toutes victimes d'une violation »).
- **Confiance** : à vérifier (source externe). La méthodologie de l'étude 2025 tranchera.

### [02-12] [MINEUR] Le classement des sources de l'encadré « ATTENTION » est incohérent, et la règle du § 1.4 n'est pas appliquée
- **Axe** : C
- **Localisation** : p. 16 : « ceux de CyberArk, de Microsoft et d’Anthropic sont des données de fournisseurs ». § 1.4, p. 13 : « un chiffre de fournisseur est présenté comme une allégation de ce fournisseur ».
- **Diagnostic** :
  - IBM, éditeur de sécurité commanditaire de l'étude, est classé parmi les « enquêtes », tandis que l'enquête de CyberArk est classée « données de fournisseurs ».
  - Les chiffres de MCP (« comptait 10 000 serveurs actifs », [14], blogue du projet) et ceux d'A2A (« réunissait plus de 150 organisations », [15], communiqué de la Linux Foundation) sont des autodéclarations de projets. Ils sont énoncés comme des faits, sans « selon », et ne figurent dans aucune catégorie de l'encadré.
  - Menlo Ventures est un investisseur du secteur, sans mention d'un possible conflit d'intérêts.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : classer chaque source selon une règle unique, par exemple « commanditée par un fournisseur ». Introduire les chiffres de [14] et [15] par « selon le projet » ou « selon la Linux Foundation ».
- **Confiance** : vérifié dans le texte (le lien de Menlo avec le secteur est à vérifier).

### [02-13] [MINEUR] Tendance FinOps tirée d'échantillons annuels différents
- **Axe** : B
- **Localisation** : § 2.1, p. 16 : « 98 % des répondants FinOps gèrent des dépenses d’IA, contre 63 % en 2025 et 31 % en 2024 ».
- **Diagnostic** : les trois éditions reposent sur des échantillons autosélectionnés de praticiens FinOps, différents d'une année à l'autre. Ces données ne constituent pas une série comparable, et le fait de « gérer des dépenses d'IA » ne mesure pas une « pression financière ».
- **Contre-exemple** : sans objet.
- **Correctif proposé** : préciser que les échantillons sont autosélectionnés et changent d'une édition à l'autre. Retirer l'inférence « La pression financière est déjà visible » ou l'appuyer sur un autre indicateur.
- **Confiance** : déduit.

### [02-14] [MINEUR] Menlo Ventures : périmètre de l'estimation douteux
- **Axe** : A
- **Localisation** : § 2.1, p. 16 : « selon un sondage auprès d’entreprises américaines, que les entreprises ont consacré 37 G$ US à l’IA générative en 2025 […] (estimation hors inférence) ».
- **Diagnostic** : d'après mon souvenir du rapport [16], les 37 G$ US se répartissent entre applications et infrastructure, et l'infrastructure comprend les dépenses d'API de modèles, donc l'inférence. Si c'est exact, la mention « hors inférence » est fausse. L'estimation de marché est en outre extrapolée d'un sondage américain, sans que le texte dise si elle vaut pour les États-Unis ou pour le monde.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : vérifier la ventilation dans [16] et préciser le périmètre géographique.
- **Confiance** : à vérifier (source externe). Je n'en suis pas certain.

### [02-15] [MINEUR] Le chiffre de MCP perd ses qualificatifs
- **Axe** : C
- **Localisation** : § 2.1, p. 16 : « le Model Context Protocol (MCP) comptait 10 000 serveurs actifs ».
- **Diagnostic** : la source [14] parle, à ma connaissance, de « plus de 10 000 serveurs MCP publics actifs ». Le texte retire « plus de » et « publics ». Un comptage de serveurs publics ne dit rien des serveurs privés d'entreprise.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « plus de 10 000 serveurs publics actifs, selon le projet ».
- **Confiance** : à vérifier (source externe).

### [02-16] [MINEUR] « Azure AI Foundry » en avril 2026
- **Axe** : C
- **Localisation** : § 2.1, p. 16 : « intégré à Azure AI Foundry, à Copilot Studio et à Amazon Bedrock AgentCore[15] ».
- **Diagnostic** : je crois que le service a été renommé « Microsoft Foundry » en novembre 2025. Le nom employé serait alors périmé à la date de la source (9 avril 2026). C'est la seule occurrence dans le document.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : reprendre le nom employé par [15], ou le nom courant au 27 octobre 2026.
- **Confiance** : à vérifier (source externe).

### [02-17] [MINEUR] Loi 25 : « en vigueur pour l'essentiel depuis le 22 septembre 2024 »
- **Axe** : C
- **Localisation** : § 2.4, p. 20 : « La Loi 25 (L.Q. 2021, c. 25) est en vigueur pour l’essentiel depuis le 22 septembre 2024, date de sa dernière étape majeure ».
- **Diagnostic** : la plupart des dispositions sont en vigueur depuis le 22 septembre 2023, et la loi est pleinement en vigueur depuis le 22 septembre 2024. « Pour l'essentiel depuis 2024 » suggère à tort que l'essentiel date de 2024, ou qu'une partie ne serait pas encore en vigueur.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « entièrement en vigueur depuis le 22 septembre 2024, date de sa dernière étape (droit à la portabilité) ».
- **Confiance** : vérifié dans le texte (le fait externe relève de ma connaissance; confiance élevée).

### [02-18] [MINEUR] RIA : date d'application à l'annexe III présentée comme fixe
- **Axe** : A
- **Localisation** : § 2.4, p. 20 : « le règlement (UE) 2026/1744 fixe au 2 décembre 2027 l’application aux systèmes à haut risque de l’annexe III ».
- **Diagnostic** : la proposition « omnibus numérique » (novembre 2025) faisait du 2 décembre 2027 une date butoir, avec une application possible plus tôt, six mois après une décision de la Commission constatant que les outils d'appui sont disponibles. Si le texte adopté conserve ce mécanisme, « fixe au » est inexact et le jalon J2a pourrait devoir être avancé. Le H.5 (p. 281) indique que le texte d'EUR-Lex n'a pas été relu le 1er novembre.
- **Contre-exemple** : la Commission constate en mars 2027 que les normes sont disponibles. L'annexe III s'applique alors dès septembre 2027, avant le jalon J2a du 1er novembre 2027.
- **Correctif proposé** : vérifier l'article de prise d'effet du règlement 2026/1744 et écrire « au plus tard le 2 décembre 2027 » si le mécanisme subsiste.
- **Confiance** : à vérifier (source externe).

### [02-19] [MINEUR] « Producteur-vérificateur » au § 1.4, « évaluateur-optimiseur » au chapitre 7, et un guide présenté comme une norme
- **Axe** : C
- **Localisation** : § 1.4, p. 13 : « Microsoft exige un plafond d’itérations pour la boucle producteur-vérificateur, sans en fixer la valeur[9] ».
- **Diagnostic** : le chapitre 7 (p. 89, EXIG-ORC-05) nomme ce patron « évaluateur-optimiseur ». La source [9] est un guide de l'Azure Architecture Center : écrire « exige » contredit la règle de lecture que le même paragraphe pose (« exige » est réservé à une norme ou à une loi).
- **Contre-exemple** : sans objet.
- **Correctif proposé** : écrire « Le guide de Microsoft recommande un plafond d'itérations pour la boucle évaluateur-optimiseur », et faire la même correction aux p. 89 et 90.
- **Confiance** : vérifié dans le texte.

### [02-20] [MINEUR] « Sept annexes, de A à G », alors que le document en compte huit
- **Axe** : C
- **Localisation** : § 1.5, p. 13 : « Sept annexes, de A à G, fournissent les outils d’application, le glossaire et les références. »
- **Diagnostic** : l'annexe H (actualisation de novembre 2026, p. 275-283) existe et ajoute des références à partir de [474].
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « Huit annexes, de A à H; l'annexe H, informative, consigne l'actualisation du 1er novembre 2026. »
- **Confiance** : vérifié dans le texte.

### [02-21] [MINEUR] Tableau 4 : emplacement imprécis des préfixes OBS, EVA et FIN
- **Axe** : C
- **Localisation** : tableau 4, p. 13 : « EXIG-OBS […] Chapitre 10 », et de même pour EVA et FIN.
- **Diagnostic** : les autres lignes donnent des sections. Le décompte des blocs (vérifié) situe les OBS aux § 10.1 et 10.3, les EVA au § 10.4 et les FIN aux § 10.5 et 10.6. Les 287 exigences et l'ordre de l'annexe D sont par ailleurs conformes au § 1.5 (vérifié). Note : le report 7 du H.3 (p. 280) annonce « Annexe D (272 lignes, 284 après ajout) », alors que l'annexe D compte 287 lignes, soit 299 après ajout. Le défaut se trouve dans l'annexe H, mais il vise directement le § 1.5.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : indiquer « Sections 10.1 et 10.3 », « Section 10.4 » et « Sections 10.5 et 10.6 ». Corriger « 272 » en « 287 » dans le H.3.
- **Confiance** : vérifié dans le texte (décompte par script sur full.txt).

### [02-22] [MINEUR] N0 « hors portée » contredit le tableau 1, et l'échelle compte un niveau sans agent possible
- **Axe** : C
- **Localisation** : p. 22 : « N0 Automatisation déterministe : aucun modèle; […] (repère de base hors portée agentique, section 1.2) ». Tableau 1, p. 11, dans la portée : « flux déterministe qui appelle un agent ou qui est appelé par lui ».
- **Diagnostic** : le § 1.2 ne mentionne pas N0 et place dans la portée certains flux déterministes. De plus, la définition d'« agent » (tableau 7) exige « un modèle ». Un « agent N0 » inscrit au registre est donc vide par définition, alors que le niveau est défini comme « déclaré au registre » pour un agent.
- **Contre-exemple** : un flux Temporal sans modèle appelle un agent N3. Il est dans la portée selon le tableau 1, mais « hors portée » selon N0. Quelle fiche faut-il créer, et à quel niveau ?
- **Correctif proposé** : écrire « N0 : repère de comparaison, non attribuable à un agent; un flux déterministe en interaction avec un agent est dans la portée (section 1.2) et suit les contrôles de l'agent qu'il appelle ».
- **Confiance** : vérifié dans le texte.

### [02-23] [MINEUR] Définition ISO/IEC 22989 quasi textuelle, appuyée sur une simple fiche de catalogue
- **Axe** : C
- **Localisation** : p. 15 : « Certains textes payants, comme les normes ISO/IEC, ont été vérifiés par leur fiche de catalogue […]; le cadre évite donc de les citer textuellement ». Tableau 7, p. 21 : « Selon ISO/IEC 22989, entité automatisée qui perçoit son environnement, y réagit et agit pour atteindre ses buts. »
- **Diagnostic** : la définition de « agent » reproduit presque mot à mot une définition normative. Or la référence [59] est une fiche de catalogue (Standards Norway), qui ne contient pas les définitions. L'affirmation « vérifié à la source » ne tient donc pas, et la règle de la p. 15 n'est pas respectée.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : citer la plateforme de consultation en ligne de l'ISO (OBP), qui publie les termes en accès libre, ou marquer la définition comme paraphrase non vérifiée au texte.
- **Confiance** : vérifié dans le texte. Le contenu de [59] est déduit de sa description.

### [02-24] [MINEUR] Portée : cas de l'assistant qui ne lit que des ressources ou un index documentaire
- **Axe** : A
- **Localisation** : p. 12 : « Un assistant qui reçoit un premier outil, même en lecture seule, entre dans la portée dès ce moment. » Tableau 1 (p. 11), hors portée : « Assistant conversationnel sans outil ni capacité d’action ». Tableau 7 (p. 21) : une ressource est distincte d'un outil.
- **Diagnostic** : un assistant qui ne lit que des ressources MCP ou un index de recherche documentaire (RAG) sur des données internes n'a « aucun outil ». La ligne « Agents internes » (« qui lit […] des données de l'entreprise ») le place pourtant dans la portée. Seule la règle du doute tranche, et elle est informative (voir [02-04]).
- **Contre-exemple** : un assistant de recherche documentaire sur des dossiers RH contenant des RP échappe au registre, à l'EFVP de l'agent et à la passerelle.
- **Correctif proposé** : remplacer « reçoit un premier outil » par « reçoit un premier outil ou un premier accès à une ressource ou à des données de l'entreprise ».
- **Confiance** : vérifié dans le texte.

### [02-25] [MINEUR] Portée des agents achetés limitée à l'« activation » par l'entreprise
- **Axe** : A
- **Localisation** : tableau 1, p. 11 : « dès que l’entreprise ou une équipe métier les active ».
- **Diagnostic** : un agent activé par défaut par l'éditeur, ou par un employé seul, n'est pas « activé par l'entreprise ou une équipe métier ». Il échappe à la lettre du tableau 1, alors que l'enjeu 7 (p. 19) vise précisément ces agents fantômes et que l'EXIG-GOV-07 (p. 165) couvre « tout agent […] qui agit dans le périmètre ». La règle normative l'emporte, mais le tableau informatif induit en erreur.
- **Contre-exemple** : une mise à jour d'un logiciel-service active une fonction agentique qui écrit dans le CRM. Le parrain estime que le système n'est pas dans la portée puisque l'entreprise ne l'a pas activé.
- **Correctif proposé** : écrire « dès qu'ils peuvent agir sur des systèmes ou des données de l'entreprise, qu'ils aient été activés par l'éditeur, par une équipe ou par un employé ».
- **Confiance** : vérifié dans le texte.

### [02-26] [MINEUR] Tableau 3 : résumé incomplet du régime de dérogation
- **Axe** : C
- **Localisation** : tableau 3, p. 12 : « (ou, pour un agent de classe faible, par l’architecture d’entreprise sur délégation du comité) […] Certaines obligations n’admettent aucune dérogation (section 4.3 et EXIG-GOV-17). »
- **Diagnostic** :
  - Le tableau omet la limite de 90 jours et la séparation entre la personne qui instruit et celle qui décide, deux conditions posées par le § 4.3 (p. 30) et l'EXIG-GOV-15 (p. 168).
  - Les deux listes non dérogeables auxquelles il renvoie diffèrent. Le § 4.3 vise la « mise en production d’un agent sans personne nommée ». L'EXIG-GOV-17 vise l'« exploitation d’un agent sans fiche au registre ni parrain nommé ». Le « ni » de l'EXIG-GOV-17 peut se lire comme une conjonction des deux manques, auquel cas un agent qui a une fiche mais aucun parrain n'est pas visé.
- **Contre-exemple** : l'architecture d'entreprise accorde une dérogation de six mois à un agent de classe faible, ce que le tableau 3 semble permettre et que le § 4.3 interdit.
- **Correctif proposé** : ajouter « pour 90 jours au plus » au tableau 3. Renvoyer à la seule EXIG-GOV-17, reformulée « sans fiche au registre ou sans parrain nommé ».
- **Confiance** : vérifié dans le texte.

### [02-27] [MINEUR] Redondance sur l'étiquetage agentique abusif
- **Axe** : C
- **Localisation** : p. 12 (« Gartner observait d’ailleurs, en juin 2025, que de nombreux produits existants étaient simplement rebaptisés ») et p. 16 (« agent washing »).
- **Diagnostic** : le même fait, tiré de la même source [3], est présenté deux fois.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : garder la mention du § 2.1 et faire renvoyer le § 1.2 vers elle.
- **Confiance** : vérifié dans le texte.

### [02-28] [MINEUR] « Journal d'audit inaltérable »
- **Axe** : C
- **Localisation** : tableau 6, enjeu 5, p. 19 : « Traçage de bout en bout et journal d’audit inaltérable ».
- **Diagnostic** : un chaînage d'empreintes et une signature rendent les altérations détectables (inviolabilité apparente, au sens de tamper-evident). Ils ne rendent pas le journal impossible à modifier : l'opérateur qui détient la clé peut réécrire toute la chaîne si elle n'est pas ancrée à l'extérieur. Le terme surpromet.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « journal d'audit à altération détectable », à aligner sur la formulation du § 10.3.
- **Confiance** : déduit. Le mécanisme exact du § 10.3 relève du chunk 15.

### [02-29] [MINEUR] Renvois dans le désordre
- **Axe** : C
- **Localisation** : § 2.4, p. 20 : « (section 13.3 et section 13.1) ».
- **Diagnostic** : l'ordre est inversé (13.1 Verrouillage, 13.3 Clauses).
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « (sections 13.1 et 13.3) ».
- **Confiance** : vérifié dans le texte.

### [02-30] [MINEUR] « Le choix d'un protocole n'est plus un pari sur un éditeur » : une thèse surévaluée
- **Axe** : B
- **Localisation** : § 2.2, p. 17 : « Pour l’entreprise, le choix d’un protocole n’est plus un pari sur un éditeur. »
- **Diagnostic** : une fondation neutre change la propriété du projet, non son orientation technique. Celle-ci reste pilotée par des éditeurs (le comité directeur technique d'A2A réunit des entreprises, voir le H.4 n° 1), et la cadence des révisions de MCP impose des migrations (EXIG-MCP-22). Le risque passe du pari sur un éditeur à une dépendance envers le rythme du consortium.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « n'est plus un pari sur un seul éditeur; il reste une dépendance envers le calendrier de la fondation, que le catalogue absorbe ».
- **Confiance** : déduit.

### [02-31] [MINEUR] « Énoncé vérifiable en revue d'architecture ou en test » : une affirmation trop universelle
- **Axe** : B
- **Localisation** : § 1.4, p. 13 : « un énoncé vérifiable en revue d’architecture ou en test ».
- **Diagnostic** : certaines exigences portent sur une absence ou une exhaustivité, qu'aucun test ne peut démontrer. Ainsi, l'EXIG-GOV-07 (« inventorier tout agent ») n'est vérifiable que par une borne inférieure, au moyen du rapprochement de l'EXIG-GOV-10, et la règle centrale « rien ne contourne la passerelle » ne se vérifie que par l'absence de contre-exemple.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : dire que chaque exigence porte une méthode de vérification, avec ses limites, par exemple « vérifiée par rapprochement mensuel; l'exhaustivité n'est pas démontrable ».
- **Confiance** : déduit.

### [02-32] [MINEUR] Anachronisme au tableau 5
- **Axe** : C
- **Localisation** : tableau 5, ligne du 29 juillet 2025, p. 17 : « hors de l’Agentic AI Foundation (AAIF) ».
- **Diagnostic** : l'AAIF est créée le 9 décembre 2025 (même tableau). La colonne « Portée » mêle l'état d'octobre 2026 à celui de la date du jalon.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : « (toujours hors de l'AAIF au 27 octobre 2026) », ou supprimer la mention, que la ligne du 12 octobre 2026 couvre déjà.
- **Confiance** : vérifié dans le texte.

## Points forts
- Le texte distingue rigoureusement le fait externe du « choix du cadre », et l'encadré « ATTENTION » refuse de tirer une exigence chiffrée de prévisions d'analystes.
- La chronologie du tableau 5 est cohérente : 3 projets fondateurs, plus agentgateway, A2A et Agent Router, plus 4 = 10 projets de l'AAIF. La numérotation EXIG est intacte : 287 blocs, sans trou, dans l'ordre de l'annexe D (vérifié par script).
- Les limites de la vérification sont avouées (p. 15), et le tableau 6 relie chaque enjeu à une réponse localisée.

## Questions pour l'audit bibliographique
1. p. 16, [16] Menlo Ventures : les 37 G$ US comprennent-ils les API de modèles, donc l'inférence ? Quel est le périmètre (États-Unis ou monde) et quelle est la taille de l'échantillon ?
2. p. 16, [18] IBM 2025 : quelle est la population du 13 % et du « une sur cinq » (organisations ayant subi une violation) ? p. 16, [19] : édition 2026, 4,99 M$ US et hausse de 12 % (4,44 × 1,12 ≈ 4,97).
3. p. 16, [14] : le libellé exact est-il « 10 000+ active public servers » ? [15] : la Linux Foundation emploie-t-elle « Azure AI Foundry » ou « Microsoft Foundry » ?
4. p. 16, [10] State of FinOps 2026 : 1 192 répondants et 98 %. [11] CyberArk : 2 600 répondants, 20 pays, Canada inclus, 68 %; la source est un communiqué reproduit par Silicon UK (source secondaire).
5. p. 16, [17] : contexte exact des multiplicateurs 4× et 15×.
6. p. 17, [28] : date de publication du Top 10 agentique de l'OWASP (9 ou 10 décembre 2025). [29, 30] : A2A 1.0.0 du 12 mars 2026 et 1.0.1 du 28 mai 2026. [31, 32] : entrée d'agentgateway à l'AAIF le 4 juin 2026. [36] : Agent Router le 9 septembre 2026. [38] : quatre projets le 22 octobre 2026.
7. p. 17, [5, 35] : approbation du conseil le 4 août (non vérifiée, déjà consigné en H.4 n° 2). p. 17, [34] : 12 mois et 90 jours dans la politique de cycle de vie de MCP 2026-07-28.
8. p. 18, [40, 41] : AP2 a-t-il été « confié à la FIDO Alliance » ? Qui porte l'UCP ? Existe-t-il un groupe de travail de l'AAIF sur le commerce agentique ?
9. p. 19, [46] : Agent 365 en disponibilité générale le 1er mai 2026 et synchronisation en préversion. [47] : ServiceNow, 5 mai 2026. [52] : Gartner, document 8214461, « résumé public, août 2026 » (la référence ne porte pas de mois).
10. p. 20, [48] : création automatique de l'Entra Agent ID depuis juillet 2026, non désactivable. [53-55] : crédits Copilot, crédits Flex et « Agentic Work Units ».
11. p. 20, [58] : règlement (UE) 2026/1744 du 8 juillet 2026. La date du 2 décembre 2027 est-elle fixe ou une date butoir assortie d'un déclenchement anticipé ?
12. p. 20, [8] : E-23 parle-t-elle d'un inventaire des modèles « à risque non négligeable », ou de tous les modèles ?
13. p. 21, [59] : la fiche de Standards Norway contient-elle la définition de « AI agent » ? Sinon, quelle source appuie le texte ? [76] : IMDA, version 1.5, et section 1.1.3.

audit_02.md : 32 constats (0 BLOQUANT, 6 MAJEUR, 26 MINEUR)
