# Audit chunk_28 — pages 271-282

## Synthèse
Le chunk couvre la fin de l'annexe G (réf. [403]-[473]) puis l'annexe H (H.1 à H.5, tableaux 70-72, début des références [474]+). Le recoupement avec le corps est en grande partie exact : sections, exigences, dates et calculs vérifiés (28 septembre 2027 et 30 mars 2027 sont bien les derniers mardis; les expirations de −16, −17 et SPIFFE −02 respectent 185 jours; l'annexe D compte bien 272 exigences). Les trois défauts les plus graves :
1. Le régime « informatif » ne tient pas : l'annexe consigne des errata qui restent faux dans le corps, prescrit (« doit »), interprète des critères normatifs, et sa règle « le corps vaut pour le 27 octobre » est contredite par son propre erratum.
2. Le régime de vérification se contredit : « contre-vérification individuelle » d'un côté, seulement « un échantillon » contre-vérifié de l'autre, plus des lectures passées par un résumeur ou relayées.
3. Le critère qui trie les faits entre H.2 (dépassé depuis) et H.4 (erratum) est appliqué de façon incohérente : au moins sept faits « nouveaux » sont antérieurs au 27 octobre, ce qui fragilise aussi l'« état des sources » du corps.

## Constats

### [28-01] MAJEUR Régime informatif contredit par des errata non reportés et un contenu prescriptif
- **Axe** : C
- **Localisation** : H.1, p. 275, « Cette annexe est informative. Elle ne modifie aucune exigence, aucun tableau ni aucune échéance »; tableau 70, p. 276, « Le catalogue doit porter le stade de chaque extension (EXIG-INT-09) »; p. 278, « la version 2026.10 la déclenche dès l'approbation du cadre »; H.2, p. 280, « il ne s'applique plus à MCP en bloc, mais extension par extension ».
- **Diagnostic** : un erratum corrige par nature un texte. Le placer dans une annexe qui « ne modifie » rien laisse le corps faux. La section 6.6 (et la section 13.1, voir 28-13) continue d'affirmer « huit entreprises ». Par ailleurs, l'annexe emploie le registre normatif (« doit », « déclenche ») et réinterprète la portée de l'EXIG-GOV-19 (extension par extension), ce qui est un acte d'interprétation normative. Or la section 1.4 ne reconnaît la force normative qu'aux blocs EXIG, aux PRIN et aux tableaux visés. Le lecteur ne sait pas si ces phrases l'obligent.
- **Contre-exemple** : un architecte qui applique la section 6.6 en revue d'appel d'offres reprend « huit entreprises », car le corps fait foi pour les exigences. Un autre, qui lit H.2, refuse Tasks en production faute de « réserve inscrite » au titre de l'EXIG-GOV-19. Les deux lectures sont défendables.
- **Correctif proposé** : séparer deux régimes. Un errata normatif, daté et approuvé, appliqué au corps sous un numéro 1.1.1 avec un relevé des modifications. Puis des constats et propositions informatifs, rédigés au conditionnel (« le comité pourrait… »). Remplacer « doit » et « déclenche » par « appellerait ».
- **Confiance** : vérifié dans le texte

### [28-02] MAJEUR La règle de divergence corps/annexe est fausse pour les errata
- **Axe** : A
- **Localisation** : H.1, p. 275, « Là où l'annexe et le corps divergent, le corps vaut pour le 27 octobre 2026, l'annexe pour le 1er novembre »; tableau 72, n° 1, p. 281, « Bloomberg y a été ajouté le 20 octobre 2026, avant l'état des sources du cadre (27 octobre) ».
- **Diagnostic** : la règle suppose que toute divergence vient d'un changement survenu après le 27 octobre. L'erratum n° 1 établit le contraire : le corps était déjà faux au 27 octobre. La règle déclare donc valide, à sa date, un énoncé que l'annexe prouve faux à cette même date. Elle ne dit pas non plus quel texte appliquer après le 1er novembre, alors que c'est la seule question utile à un lecteur qui agit aujourd'hui. Le renvoi au catalogue ne vaut que pour les versions.
- **Contre-exemple** : la composition du comité directeur d'A2A, au 27 octobre, est neuf sièges selon [479]. Selon la règle de H.1, le corps (huit) « vaut » pour cette date.
- **Correctif proposé** : « En cas de divergence, l'erratum (H.4) prime sur le corps à toute date; un constat de H.2 décrit l'état au 1er novembre sans modifier le corps tant que le comité n'a pas statué; pour les versions, le catalogue fait foi. »
- **Confiance** : vérifié dans le texte

### [28-03] MAJEUR Régime de vérification contradictoire et non reproductible
- **Axe** : B
- **Localisation** : divulgation, p. 275, « un échantillon en a été contre-vérifié à la source par l'agent qui a assemblé l'annexe »; régime déclaré, p. 275, « contre-vérification individuelle sur source primaire »; tableau 70, ligne AAIF/AGNTCY, p. 277, « page lue par un outil de lecture Web, qui la résume »; ligne AMF, p. 279, « Dernier état lu : 31 octobre 2026 […] [491] ».
- **Diagnostic** :
  - Les deux phrases s'excluent : soit chaque fait a été contre-vérifié, soit seulement un échantillon. Ni la taille de l'échantillon ni les faits qu'il couvre ne sont donnés.
  - Les deux passes sont faites par des agents LLM, sans relecture humaine déclarée.
  - Une lecture par un résumeur n'est pas une lecture de source primaire. Le statut « New » de la proposition n° 57, qui fonde le verdict « Signal non survenu », vient de ce résumé.
  - L'état « Prise d'effet : 1er mai 2027 » de l'AMF vient de la Note AMF IA, un livrable frère : c'est un relais secondaire.
  - « Preuve » est annoncée, mais aucune capture ni empreinte n'est conservée. Pour les pages mouvantes, l'annexe admet elle-même qu'un état antérieur « n'est pas vérifiable ici » (tableau 72, n° 2).
- **Contre-exemple** : si le résumeur a omis un commentaire de décision sur la proposition n° 57, le signal AGNTCY de l'EXIG-INT-23 est déclaré non survenu à tort, et la révision extraordinaire n'a pas lieu.
- **Correctif proposé** : préciser la règle (vérification individuelle par l'agent de relevé, échantillon de N faits contre-vérifié par un second agent, liste jointe). Classer « vérifié partiellement » les lectures par résumeur et les relais. Archiver chaque page lue (Wayback, capture, SHA-256) et référencer l'archive.
- **Confiance** : vérifié dans le texte

### [28-04] MAJEUR Critère H.2 / H.4 appliqué de façon incohérente; plusieurs « nouveautés » précèdent l'état des sources
- **Axe** : C
- **Localisation** : H.4, p. 281, « Un énoncé exact à sa date, mais dépassé depuis, relève du 70, non d'un erratum »; tableau 70, p. 276-279.
- **Diagnostic** : selon ce critère, n'entre au tableau 70 que ce qui a changé après le 27 octobre. Or l'annexe y range, ou en H.5, des faits antérieurs :
  - SEP-2596 finale le 3 juin 2026;
  - SEP-3398 acceptée le 14 octobre;
  - EN 18286 au JO le 14 octobre;
  - déclaration du BSIF du 15 octobre;
  - étiquette alpha3 d'a2a-tck le 20 octobre;
  - deuxième lecture de C-22 au Sénat le 22 octobre;
  - NIST IR 8547 finale le 27 octobre.

  Ce ne sont ni des énoncés dépassés depuis, ni des errata au sens de H.4. Ce sont des omissions à la date de l'état des sources, catégorie que l'annexe ne nomme pas. Seul Bloomberg, au 20 octobre, est traité en erratum, ce qui rend le tri arbitraire. Conséquence systémique : la mention de couverture « Faits, versions et dates vérifiés aux 27 et 28 octobre 2026 » n'est pas tenue pour ces sources.
- **Contre-exemple** : la ligne HTTP+SSE dit « L'échéance n'est plus indéterminée », alors que rien n'a changé depuis le 3 juin. Le tableau 70 présente comme une actualisation ce qui est une lacune du corps.
- **Correctif proposé** : ajouter à H.4 une catégorie « omission à la date » et y verser ces sept faits. Ou bien restreindre la mention de couverture du corps aux faits effectivement rouverts (annexe F).
- **Confiance** : vérifié dans le texte (dates tirées de l'annexe elle-même)

### [28-05] MAJEUR Identité documentaire : deux artefacts distincts portent « Version 1.1 »
- **Axe** : C
- **Localisation** : pied de chaque page, « Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026 »; page de titre, « Actualisation 1er novembre 2026, annexe H (informative) »; § 1.5, p. 13, « Sept annexes, de A à G »; § 1.6, p. 14, « Chaque révision porte un numéro de version et une date, et s'accompagne d'un relevé des modifications ».
- **Diagnostic** : l'ajout de l'annexe H a modifié la page de titre, la table des matières, les pieds de page et le décompte des annexes, sans nouvelle entrée à l'historique des versions (p. 2) et sans changement de numéro. Le § 1.5 reste à sept annexes. Le § 1.6 exige un numéro et un relevé pour chaque révision. Une approbation par le comité « de la version 1.1 » ne désigne donc pas un texte unique.
- **Contre-exemple** : deux membres du comité votent sur deux PDF « 1.1 », l'un avec l'annexe H et 283 pages, l'autre sans.
- **Correctif proposé** : numéroter 1.1.1 (ou 1.1-H), ajouter la ligne d'historique, corriger le § 1.5 (« huit annexes, de A à H; l'annexe H est informative »).
- **Confiance** : vérifié dans le texte

### [28-06] MAJEUR Signal « révision de MCP » : déclaré survenu alors qu'il est seulement daté, et hors du champ de l'EXIG-INT-23
- **Axe** : A
- **Localisation** : tableau 70, p. 275, « Le signal "révision de MCP" de l'EXIG-INT-23 a désormais une date : le 30 mars 2027 »; H.2, p. 280, « seul celui de MCP est survenu »; tableau 72, n° 3, « Inscrire au catalogue le signal comme survenu ».
- **Diagnostic** :
  - Le § 6.9 nomme le signal « une révision de MCP ». Une révision prévue le 30 mars 2027, et encore « subject to confirmation », n'est pas survenue. Déclarer le signal « survenu » déclenche, selon l'EXIG-INT-23, une révision extraordinaire immédiate pour un événement futur et incertain.
  - L'EXIG-INT-23 ne vise que les entrées « au statut Évaluer ou Surveiller » (p. 86). MCP 2026-07-28 est au statut Adopter (tableau 15), dont la révision extraordinaire relève de l'EXIG-GOV-18 (« version majeure ou dépréciation »).
  - L'annexe applique donc le mauvais mécanisme à l'entrée, sur un fait qui ne l'a pas encore déclenché. Le défaut existe déjà au § 6.9, qui mêle ce signal à ceux d'entrées Évaluer ou Surveiller.
- **Contre-exemple** : MCP repousse sa publication de mars 2027 à septembre 2027 par le « transition calendar ». Le catalogue garde alors un signal « survenu » sans révision, et l'éventuelle révision extraordinaire faite en novembre 2026 n'avait pas d'objet.
- **Correctif proposé** : distinguer « annonce de date » (révision trimestrielle, EXIG-INT-08) et « publication de la révision » (révision extraordinaire, EXIG-GOV-18). Au § 6.9, rattacher le signal MCP aux extensions au statut Évaluer, ou le retirer de la liste des signaux de l'EXIG-INT-23.
- **Confiance** : vérifié dans le texte

### [28-07] MAJEUR Stades d'extension : cas indécidable dans l'EXIG-GOV-19 et énumération fermée de l'EXIG-INT-09
- **Axe** : A
- **Localisation** : tableau 70, p. 276, « Tasks, au stade Beta […] ne satisfait au troisième critère de l'EXIG-GOV-19 qu'avec une réserve inscrite »; EXIG-GOV-19, p. 170, « statut final ou stable […]; un brouillon ou un composant de niveau expérimental n'est admis qu'avec une réserve ».
- **Diagnostic** :
  - Le critère connaît deux pôles, « final ou stable » et « brouillon ou expérimental ». Le stade Beta de SEP-3392 n'est ni l'un ni l'autre : l'assimiler à l'expérimental est une décision, pas une lecture.
  - L'EXIG-GOV-19 régit l'admission d'un « standard » au statut Adopter, alors que les extensions sont filtrées par l'EXIG-MCP-04 (inscription au catalogue) et l'EXIG-INT-06. L'extension du critère aux extensions n'est écrite nulle part.
  - L'EXIG-INT-09 énumère des statuts fermés (« norme, recommandation, brouillon de groupe de travail, brouillon individuel, préversion ou projet hébergé ») sans les stades Experimental, Beta ou Stable. Le « doit » de l'annexe suppose donc une modification de l'EXIG-INT-09.
- **Contre-exemple** : Tasks (Beta) est actif en production sous l'entrée MCP Adopter (tableau 15). Est-ce conforme? L'EXIG-INT-06 dit oui si l'entrée est Adopter, l'annexe dit non sans réserve : la question est indécidable.
- **Correctif proposé** : à la révision, compléter le troisième critère de l'EXIG-GOV-19 (« Beta : admis avec réserve »), déclarer qu'il s'applique à chaque extension, et ajouter les stades d'extension à l'énumération de l'EXIG-INT-09.
- **Confiance** : vérifié dans le texte

### [28-08] MAJEUR La promotion de Tasks au protocole de base ferait disparaître les contrôles de l'EXIG-MCP-04
- **Axe** : B
- **Localisation** : tableau 70, p. 276, « "MCP Tasks Beta, to Core" »; EXIG-MCP-04, p. 58, « Pour l'extension Tasks, la passerelle impose un quota de tâches actives par mandant et une durée de vie maximale ».
- **Diagnostic** : le quota et la durée de vie sont rattachés au statut d'extension (« Une extension MCP DOIT figurer au catalogue… »). Si Tasks entre dans le protocole de base à une révision future, il n'est plus une extension : la liste d'autorisation et le quota de l'EXIG-MCP-04 ne s'appliquent plus littéralement. Le risque de déni de service par tâches asynchrones, cité par le cadre lui-même [203], revient alors sans contrôle. L'annexe relève la destination « Core » sans en tirer cette conséquence.
- **Contre-exemple** : après migration vers la révision qui intègre Tasks au protocole de base, un serveur ouvre des milliers de tâches par mandant. Aucune exigence n'impose plus de quota.
- **Correctif proposé** : rattacher le quota et la durée de vie à la primitive tâche (`tasks/*`), quel que soit son statut d'extension ou de protocole de base, et le noter au tableau 70.
- **Confiance** : déduit

### [28-09] MAJEUR a2a-tck : une barrière bloquante repose sur une suite alpha, en asymétrie avec la suite MCP jugée informative
- **Axe** : B
- **Localisation** : tableau 70, ligne a2a-tck, p. 277, « L'exigence bloquante repose sur une trousse dont la ligne 1.0 est étiquetée alpha »; EXIG-INT-19, p. 84, « consignés à titre informatif tant que ce cadre demeure en préversion 0.x ».
- **Diagnostic** : l'EXIG-INT-19 et l'EXIG-A2A-14 rendent bloquants les tests MUST d'a2a-tck, alors que la même exigence rend informatifs les résultats MCP parce qu'ils sont en préversion. La ligne 1.0 d'a2a-tck était alpha dès le 20 octobre, avant l'état des sources. L'incohérence existait donc dans la v1.1 : elle relève de H.4, pas du tableau 70 (voir 28-04). Un résultat d'une suite alpha peut changer entre deux étiquettes, de sorte qu'une homologation n'est pas reproductible.
- **Contre-exemple** : un agent réussit les tests MUST d'alpha3 et est homologué. Alpha4 reclasse un test en MUST : l'agent en production devient non conforme sans avoir changé.
- **Correctif proposé** : verser le constat en H.4. Proposer au comité soit d'épingler une étiquette précise d'a2a-tck au catalogue (EXIG-INT-07) avec une réserve (EXIG-GOV-19), soit d'aligner sur le régime MCP.
- **Confiance** : vérifié dans le texte

### [28-10] MAJEUR EN 18286 : présomption de conformité à l'article 17 douteuse, et contradiction avec H.5
- **Axe** : A
- **Localisation** : tableau 70, p. 279, « EN 18286 donne présomption de conformité à l'article 17 pour l'organisation requalifiée fournisseur (EXIG-CON-15, J2a) »; H.5, p. 282, « Quatre sources datées ne portent ici aucune exigence ».
- **Diagnostic** :
  - D'après mes connaissances, l'article 40(1) du RIA attache la présomption aux exigences de la section 2 du chapitre III (art. 8 à 15), « dans la mesure où » la norme les couvre. L'article 17 (système de gestion de la qualité) est en section 3. La présomption alléguée est donc douteuse, sauf si le règlement (UE) 2026/1744 ou la décision 2026/2274 a modifié ce point. Or l'annexe déclare n'avoir pu lire le texte de 2026/1744 (H.5).
  - Le tableau 70 rattache EN 18286 à l'EXIG-CON-15 et à J2a, puis H.5 la range parmi les sources qui « ne portent aucune exigence ».
- **Contre-exemple** : une organisation requalifiée fournisseur s'appuie sur EN 18286 pour présumer sa conformité à l'article 17, alors que la présomption ne vise peut-être que les articles 8 à 15. Elle aurait alors un dossier de conformité incomplet au jalon J2a.
- **Correctif proposé** : faire vérifier par les affaires juridiques l'article 40(1) et l'acte d'exécution 2026/2274. Écrire « norme harmonisée à l'appui de l'article 17 » tant que la présomption n'est pas établie, et harmoniser H.5 avec le tableau 70.
- **Confiance** : à vérifier (source externe : texte consolidé de l'article 40 et décision d'exécution (UE) 2026/2274)

### [28-11] MINEUR Le retrait accéléré de 90 jours est ignoré dans l'analyse du calendrier MCP
- **Axe** : A
- **Localisation** : H.2, p. 279, « Roots, Sampling, la journalisation protocolaire et le DCR ne pourront l'être, si le calendrier est tenu, qu'à la publication de septembre 2027 ».
- **Diagnostic** : le tableau 17 (p. 57) rapporte que SEP-2596 permet, « en cas de retrait accéléré exceptionnel », un retrait après 90 jours. L'affirmation « ne pourront l'être qu'à » omet cette voie : la publication de mars 2027 pourrait les retirer par exception.
- **Contre-exemple** : une faille dans Sampling déclenche un retrait accéléré à la révision de mars 2027. La « marge » de l'échéance du 28 juillet 2027 disparaît pour qui adopte cette révision.
- **Correctif proposé** : « sauf retrait accéléré exceptionnel (90 jours, SEP-2596) ».
- **Confiance** : vérifié dans le texte (tableau 17); application déduite

### [28-12] MINEUR L'inférence « mars 2027 ⇒ révision extraordinaire » repose sur un postulat implicite
- **Axe** : A
- **Localisation** : H.2, p. 279, « L'identifiant d'une révision MCP date son dernier changement incompatible (section 6.5) : celle de mars 2027 appellera donc la révision extraordinaire de l'EXIG-GOV-18 ».
- **Diagnostic** : la conclusion suppose que la publication prévue contiendra un changement incompatible. Avec un calendrier fixe, une publication pourrait ne comporter que des ajouts compatibles. Dans ce cas, l'EXIG-GOV-18 (« version majeure ou une dépréciation ») ne se déclenche pas.
- **Correctif proposé** : « si elle comporte un changement incompatible ou une dépréciation ».
- **Confiance** : déduit

### [28-13] MINEUR Erratum n° 1 incomplet : « huit entreprises » figure aussi en 13.1
- **Axe** : C
- **Localisation** : tableau 72, n° 1, p. 281, « Où : Section 6.6 »; § 13.1, p. 190, « son comité directeur technique réunit huit entreprises concurrentes : AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow[29] ».
- **Diagnostic** : la même erreur figure en 13.1, que l'erratum ne vise pas. La colonne « Sections » de la ligne « A2A, gouvernance » du tableau 70 omet aussi 13.1, qui reprend l'hébergement par l'AAIF (p. 189).
- **Correctif proposé** : ajouter « § 13.1 » à l'erratum n° 1 et à la ligne du tableau 70.
- **Confiance** : vérifié dans le texte

### [28-14] MINEUR Tableau 72 : deux lignes sur trois enfreignent son propre critère d'admission
- **Axe** : C
- **Localisation** : H.4, p. 281, « Le 72 ne retient que ce qu'une source primaire établit »; n° 2, « Ce que le site affichait le 29 octobre n'est pas vérifiable ici »; n° 3, « ce n'est pas un erratum ».
- **Diagnostic** : le n° 2 n'est pas établi, puisque l'annexe le dit invérifiable, et son traitement renvoie l'écart à la Veille, autre livrable. Le n° 3 est déclaré non-erratum. Le titre (« Errata et incohérences de la version 1.1 ») couvre donc des écarts entre livrables, ce qui dilue la valeur probante du tableau.
- **Correctif proposé** : déplacer les nos 2 et 3 dans une rubrique « Écarts entre livrables (Veille) », hors du tableau 72.
- **Confiance** : vérifié dans le texte

### [28-15] MINEUR Date du 4 août : un défaut de citation présenté comme simple « non vérifiée »
- **Axe** : C
- **Localisation** : tableau 72, n° 2, p. 281, « La mention "approbation du conseil d'administration le 4 août" (tableau 5) ne figure dans aucun des deux billets : non vérifiée »; tableau 5, p. 17, « (approbation du conseil d'administration le 4 août)[5, 35] ».
- **Diagnostic** : le fait est attribué à [5] et [35], qui ne le contiennent pas. Au regard du § 1.4 (« un fait externe porte sa source »), c'est un erratum de citation établi, quelle que soit la véracité de la date. Le même alinéa dit pourtant « son énoncé est confirmé ».
- **Correctif proposé** : inscrire en H.4 l'erratum « source manquante pour le 4 août; retirer la date ou citer la source ».
- **Confiance** : vérifié dans le texte

### [28-16] MINEUR Transition de l'article 50(2) classée « précision » sans vérification du texte
- **Axe** : C
- **Localisation** : H.4, p. 281, « sous réserve de la transition de l'article 50(2) au 2 décembre 2026 […]; l'état de la page au 27 octobre n'a pas été vérifié ».
- **Diagnostic** : si la transition provient du règlement (UE) 2026/1744, en vigueur depuis le 27 juillet selon le § 12.4, alors l'énoncé du corps (« article 50 depuis le 2 août 2026 ») était incomplet à sa date, donc un erratum. L'annexe n'a pu lire ni la page au 27 octobre, ni le texte de 2026/1744 (H.5). Conclure « pas un erratum » contredit sa propre règle (« un état inconnu n'est pas "inchangé" »). L'impact est faible, puisque l'EXIG-CON-20 va au-delà de l'article 50.
- **Correctif proposé** : classer « indéterminé, à trancher sur le texte de 2026/1744 ».
- **Confiance** : vérifié dans le texte

### [28-17] MINEUR OAuth 2.1 : le tableau et la prose recommandent deux traitements différents
- **Axe** : C
- **Localisation** : tableau 70, p. 277, « l'expiration passe en phase Plateforme et se déplace à chaque version »; H.2, p. 279, « Le comité pourra retirer cette ligne des échéances externes plutôt que d'y substituer le 4 mai 2027 ».
- **Diagnostic** : le tableau suggère de déplacer l'échéance, la prose de la retirer. C'est la prose qui est cohérente avec son argument : un brouillon actif n'a pas d'échéance.
- **Correctif proposé** : aligner le tableau sur la prose.
- **Confiance** : vérifié dans le texte

### [28-18] MINEUR Ligne WIMSE : liste d'exigences incomplète et catégorie approximative
- **Axe** : C
- **Localisation** : tableau 70, p. 278, « EXIG-IAM-03 à EXIG-IAM-07, EXIG-IAM-12 »; « draft-chen-oauth-agent-revocation relancé en −01 ».
- **Diagnostic** : AIMS sert aussi de justification aux EXIG-MCP-21 (p. 66), EXIG-AUT-13 et EXIG-AUT-14 (p. 113-114), EXIG-IAM-14 (p. 126) et EXIG-SEC-13 (p. 140). La conclusion « Aucune exigence touchée » est juste aujourd'hui, mais la table de dépendances, outil des révisions futures, est incomplète. De plus, un brouillon OAuth de révocation est rangé sous « Brouillons individuels de délégation » (WIMSE).
- **Correctif proposé** : compléter la liste et classer la révocation à part.
- **Confiance** : vérifié dans le texte

### [28-19] MINEUR Report n° 1 : mauvais alinéa visé; fait AMF du corps sans source
- **Axe** : C
- **Localisation** : tableau 71, n° 1, p. 280, « Dernier alinéa de la section 12.3, après le tableau 48 »; § 12.3, p. 179, « (version d'avril 2026, en vigueur le 1er mai 2027), que le présent cadre ne reprend pas ».
- **Diagnostic** : la mention AMF est dans l'alinéa « Trois conséquences pratiques », suivi de l'alinéa « La veille porte aussi… » puis des EXIG-CON-11 et CON-12 : ce n'est pas le dernier alinéa. Cette mention datée ne porte aucun appel de référence, contrairement au § 1.4. La ligne AMF du tableau 70 la reprend sans relever l'absence de source.
- **Correctif proposé** : viser « l'alinéa "Trois conséquences pratiques" » et signaler la référence manquante.
- **Confiance** : vérifié dans le texte

### [28-20] MINEUR Report n° 5 : le tableau 60 ne couvre pas la période de J1 au 1er mai 2027
- **Axe** : C
- **Localisation** : tableau 71, n° 5, p. 280, « Plan des 90 premiers jours (section 15.2) : travaux des semaines 1 à 13 et de J1 au 1er mai 2027 ».
- **Diagnostic** : le tableau 60 se limite aux semaines 1 à 13 (phase Fondations). Les travaux de J1 au 1er mai 2027 tombent dans la phase Plateforme (tableaux 58 et 59). La colonne « Ce qu'il toucherait » omet ces tableaux.
- **Correctif proposé** : ajouter « tableaux 58 et 59 (phase Plateforme) ».
- **Confiance** : vérifié dans le texte

### [28-21] MINEUR Report n° 9 vise un alinéa non normatif; « seul le report 7 touche la structure » est contestable
- **Axe** : A
- **Localisation** : tableau 71, n° 9, p. 280, « Premier alinéa de la section 1.6 »; H.3, p. 281, « Le report 7 est le seul qui toucherait la structure normative du cadre ».
- **Diagnostic** : selon le § 1.4, seuls les blocs EXIG des chapitres 5 à 13, les PRIN et les tableaux visés obligent. Le § 1.6 (« la plus stricte s'applique ») est donc informatif : y loger une règle entre deux régimes réglementaires la priverait de force normative. Sa vraie place est le § 4.3 ou une EXIG-CON. Par ailleurs, les reports 2 (énoncé de l'EXIG-CON-11), 3 (titre de l'EXIG-CON-12) et 8 (critères du tableau 46, normatif par renvoi de l'EXIG-CON-01) modifient eux aussi des éléments normatifs.
- **Correctif proposé** : signaler pour le n° 9 la question de force normative. Remplacer « structure normative » par « appareil d'identifiants », ou lister les reports qui modifient un texte normatif.
- **Confiance** : vérifié dans le texte

### [28-22] MINEUR Report n° 8 : la circularité classe/niveau devrait être un préalable bloquant
- **Axe** : A
- **Localisation** : tableau 71, n° 8, p. 280, « Le critère "niveau d'autonomie demandé" est à concilier avec la section 12.1, qui sépare classe et niveau et fait de la classe le plafond du niveau ».
- **Diagnostic** : l'annexe voit le conflit mais le minimise (« à concilier »). Si la classe dépend du niveau demandé et que le niveau est plafonné par la classe, la définition est circulaire. Exemple : demander N3 fait passer l'agent en classe élevée, plafonnée à N2. Le niveau retenu (N2) ne justifie plus la classe élevée, d'où une règle sans point fixe garanti.
- **Correctif proposé** : qualifier ce report d'« inapplicable en l'état », et suggérer « autonomie maximale envisagée » comme critère de classe, évalué une fois, avant le plafonnement.
- **Confiance** : déduit

### [28-23] MINEUR Ligne a2a-tck : la réserve relève de l'EXIG-GOV-19, pas de l'EXIG-INT-09
- **Axe** : C
- **Localisation** : tableau 70, p. 277, « inscrit au catalogue avec une réserve (EXIG-INT-09) ».
- **Diagnostic** : l'EXIG-INT-09 impose le statut exact. La notion de « réserve inscrite » est définie à l'EXIG-GOV-19.
- **Correctif proposé** : « (EXIG-INT-09, EXIG-GOV-19) ».
- **Confiance** : vérifié dans le texte

### [28-24] MINEUR Dérive de date de référence (27 ou 28 octobre)
- **Axe** : C
- **Localisation** : en-tête du tableau 70, « Au 28 octobre 2026 (texte du cadre) »; H.1, « le corps vaut pour le 27 octobre 2026 »; tableau 72, « l'état des sources du cadre (27 octobre) ».
- **Diagnostic** : l'annexe emploie deux dates pour la même référence. C'est significatif pour ATLAS 2026.10, daté du 28 octobre.
- **Correctif proposé** : fixer une seule date, ou dire « 27-28 octobre » partout.
- **Confiance** : vérifié dans le texte

### [28-25] MINEUR Renvois sans le mot « tableau »
- **Axe** : C
- **Localisation** : p. 275, « Le 70 reprend »; p. 280, « Le 71 les présente »; p. 281, « Le 72 ne retient ».
- **Diagnostic** : le supplément de renvoi Typst manque probablement. À confirmer sur le PDF : un artefact d'extraction est peu probable, puisque « Tableau 70 — » est extrait normalement.
- **Correctif proposé** : « Le tableau 70… ».
- **Confiance** : vérifié dans le texte extrait

### [28-26] MINEUR J2a rangé parmi les « échéances réglementaires »
- **Axe** : C
- **Localisation** : H.2, p. 280, « Les échéances réglementaires du cadre — E-23 au 1er mai 2027, J2a au 1er novembre 2027, annexe III […] ».
- **Diagnostic** : J2a est un jalon interne, choix du cadre, calé un mois avant l'échéance réglementaire du 2 décembre 2027. Le ranger parmi les échéances réglementaires brouille la distinction « exigence externe / choix du cadre » posée au § 1.4.
- **Correctif proposé** : « les échéances réglementaires […] et le jalon J2a qui les précède ».
- **Confiance** : vérifié dans le texte

### [28-27] MINEUR Double exigence de révision trimestrielle, avec deux acteurs différents
- **Axe** : C
- **Localisation** : H.1, p. 275, « révision trimestrielle du catalogue (EXIG-INT-08, EXIG-GOV-18) ».
- **Diagnostic** : l'EXIG-INT-08 fait réviser le catalogue par « Le comité », l'EXIG-GOV-18 par « L'architecture d'entreprise » avec soumission au comité. L'annexe s'appuie sur les deux sans relever le doublon ni l'écart de responsabilité. Le constat porte sur le corps, et l'annexe le propage.
- **Correctif proposé** : à la révision, une seule exigence ou un renvoi explicite (INT-08 = décision, GOV-18 = préparation).
- **Confiance** : vérifié dans le texte

### [28-28] MINEUR EXIG-SEC-02 : « à chaque nouvelle version » d'ATLAS implique une cadence mensuelle
- **Axe** : B
- **Localisation** : tableau 70, p. 278, « la version 2026.10 la déclenche dès l'approbation du cadre ».
- **Diagnostic** : ATLAS a publié 2026.09 le 14 septembre, puis 2026.10 le 28 octobre. Une mise à jour complète de la matrice à chaque publication coûte cher et n'est guère vérifiable. L'annexe relève le déclenchement, pas la cadence.
- **Correctif proposé** : signaler au comité une option « revue à la révision trimestrielle, sauf nouvelle technique propre aux agents ».
- **Confiance** : déduit

### [28-29] MINEUR Ligne OpenTelemetry : registre non précisé
- **Axe** : C
- **Localisation** : tableau 70, p. 278, « registre : 85 attributs gen_ai.*, tous Development ».
- **Diagnostic** : on ne sait pas s'il s'agit du registre de v1.44.0 (central, où le corps dit les attributs GenAI déclarés obsolètes depuis v1.42.0, p. 146) ou de la branche principale du dépôt dédié. Le chiffre n'est pas interprétable sans cette précision.
- **Correctif proposé** : nommer le registre et sa révision (commit).
- **Confiance** : vérifié dans le texte

### [28-30] MINEUR Prose de H.2 redondante avec le tableau 70
- **Axe** : C
- **Localisation** : p. 275, « La prose qui suit ne retient que ce qu'il ne dit pas »; p. 279-280.
- **Diagnostic** : la prose répète les trois octrois d'OAuth 2.1, les dates de SEP-3398 et SEP-2596, les stades des extensions et les signaux non survenus, déjà présents au tableau. L'annonce n'est pas tenue.
- **Correctif proposé** : réduire la prose aux raisonnements (expiration ≠ échéance, conséquences GOV-18 et GOV-19), ou retirer l'annonce.
- **Confiance** : vérifié dans le texte

### [28-31] MINEUR Références redondantes ou à double titre
- **Axe** : C
- **Localisation** : [472] p. 275, « Release v1.0.1 (dépôt a2aproject/A2A) »; [30] (Releases v0.3.0, v1.0.0, v1.0.1); [478] p. 282 (étiquettes v1.0.1 et v1.1.0-rc); [430] p. 272, « Loi visant à protéger la vie privée et les données des consommateurs »; [431], « Loi sur la protection de la vie privée et des données des consommateurs ».
- **Diagnostic** : trois références couvrent la publication v1.0.1. C-36 porte deux titres, sans qu'on dise lequel est le titre abrégé.
- **Correctif proposé** : fusionner [472] dans [30]. Pour C-36, indiquer « titre intégral / titre abrégé ».
- **Confiance** : vérifié dans le texte

### [28-32] MINEUR Formats de date hétérogènes dans l'annexe G
- **Axe** : C
- **Localisation** : [439] p. 273, « (2026-06-15) »; [456] p. 274, « (2026, 7 avril) »; [455], « (20 octobre 2026) »; [467], « (2026, 30 avril) ».
- **Diagnostic** : trois formats de date coexistent (ISO, « année, jour mois », « jour mois année »). L'annexe H emploie un quatrième gabarit.
- **Correctif proposé** : un seul gabarit bibliographique.
- **Confiance** : vérifié dans le texte

### [28-33] MINEUR Éditeur « ISO » avec des adresses de Standards Norway
- **Axe** : C
- **Localisation** : [451]-[453] p. 273-274, « ISO. https://online.standard.no/… ».
- **Diagnostic** : [450] nomme correctement Standards Norway. [451] à [453] attribuent à l'ISO des fiches d'un revendeur national.
- **Correctif proposé** : « fiche catalogue, Standards Norway », comme pour [450], ou une adresse iso.org.
- **Confiance** : vérifié dans le texte

### [28-34] MINEUR [462] : « demande de tirage » avec une adresse d'issue
- **Axe** : C
- **Localisation** : [462] p. 274, « (demande de tirage nº 3696). GitHub […] /issues/3696 ».
- **Diagnostic** : le type annoncé ne correspond pas à l'adresse donnée.
- **Correctif proposé** : vérifier s'il s'agit d'une issue ou d'une PR et corriger le type ou l'adresse.
- **Confiance** : à vérifier (source externe)

### [28-35] MINEUR Articles du RIA cités tantôt par la Commission, tantôt par le Future of Life Institute
- **Axe** : C
- **Localisation** : [441], [442], [447], [457] (AI Act Service Desk) contre [444]-[446], [459], [461], p. 273-274 (« Future of Life Institute (2026) »).
- **Diagnostic** : pour un texte de loi, la source primaire (EUR-Lex ou Service Desk) existe. Le FLI est une source secondaire, admissible en catégorie B, mais le mélange n'est pas justifié.
- **Correctif proposé** : citer les articles 9, 13, 27, 72 et 73 sur le Service Desk ou EUR-Lex.
- **Confiance** : vérifié dans le texte

## Points forts
- Recoupements exacts dans l'ensemble : sections et exigences ciblées, calculs de dates (derniers mardis, expirations à 185 jours, 3 juin + 3 mois), 272 lignes à l'annexe D.
- Discipline de l'incertitude : pages inaccessibles déclarées « non vérifiées », « inconnu, non "inchangé" », collision de numérotation [474] repérée d'avance.
- Bonne analyse de fond : une expiration de brouillon n'est pas une échéance, et une suite de tests bloquante ne peut pas reposer sur une alpha.

## Questions pour l'audit bibliographique
- p. 279 : la décision d'exécution (UE) 2026/2274 du 12 octobre 2026 (JO L du 14 octobre) publie-t-elle EN 18286, et l'article 40(1), dans sa version modifiée par 2026/1744, couvre-t-il l'article 17? (voir 28-10)
- p. 278 : « Article 50(2) transition » au 2 décembre 2026 : l'origine est-elle 2026/1744 ou un acte ultérieur? Pour quels systèmes? (voir 28-16)
- p. 276 : SEP-3392, les stades Experimental/Beta/Stable et « MCP Tasks Beta, to Core » sur la page Extensions Overview [169].
- p. 275 : texte de SEP-3398 (« last Tuesday of March and September », report au 30 mars 2027) et contenu du « transition calendar ».
- p. 276 : SEP-2596 « Final » par la PR n° 2856 du 3 juin 2026; règle des trois mois pour HTTP+SSE dans le registre des dépréciations.
- p. 277 : GOVERNANCE.md d'A2A, « nine seats », commit 98279d6 du 20 octobre 2026 (Bloomberg).
- p. 277 : étiquettes a2a-tck 1.0.0.alpha3 et 0.3.0.beta6 (20 octobre 2026).
- p. 277 : draft-ietf-oauth-v2-1-17 (31 octobre 2026, « Obsoletes: 6749, 6750 (if approved) »); ID-JAG −05 et −06.
- p. 278 : draft-ietf-wimse-workload-identity-practices-08 et dernier appel de l'IETF jusqu'au 13 novembre 2026.
- p. 278 : MITRE ATLAS 2026.10 (28 octobre 2026) : 129 techniques, 92 sous-techniques, 44 mesures, 77 études de cas.
- p. 274 : [455] renommage de COSAiS en « Control Overlays for Super Intelligence Systems » le 20 octobre 2026 (intitulé inhabituel, à confirmer sur la page CSRC).
- p. 274 : [460] Règlement sur les incidents de confidentialité : décret 1761-2022 et date de G.O.Q. du 14 décembre 2022. Le règlement était, à ma connaissance, en vigueur dès le 22 septembre 2022 : la date de publication paraît tardive.
- p. 282 : NIST IR 8547 « finale depuis le 27 octobre 2026 » [494]; déclaration du BSIF du 15 octobre 2026 [495].
- p. 281 : [492] est-il LEGISinfo ou la Veille? (« ce que dit aussi la Veille [492] »; à recouper avec le chunk 29).

Note hors document : le décompte des blocs EXIG du corps donne 272 exigences (APP 17, ARC 25, AUT 23, CON 26, EVA 6, EVT 10, FIN 10, GOV 20, IAM 21, INT 23, MCP 22, OBS 13, ORC 30, SEC 26), ce qui confirme le « 272 lignes » de l'annexe H. Le total de 287 de REVIEW_PLAN_CADRE.md est erroné.

audit_28.md : 35 constats (0 BLOQUANT, 10 MAJEUR, 25 MINEUR)
