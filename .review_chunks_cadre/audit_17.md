# Audit chunk_17 — pages 161-172

## Synthèse
Le chunk couvre la fin des rôles et la matrice RACI (§ 11.1-11.2), le modèle en étoile (§ 11.3), le registre (§ 11.4), le cycle de vie (§ 11.5), les dérogations (§ 11.6), la gouvernance des standards (§ 11.7) et le début du § 12.1 (classes de risque). Le texte est dense et bien sourcé, mais la machine de gouvernance (états, points de contrôle, décideurs) est sous-spécifiée. Les trois défauts les plus graves :
1. Le tableau 44 donne « A, R » à une même personne pour des décisions que l'EXIG-GOV-03 et l'annexe A interdisent de cumuler.
2. Le statut « Contenir » (usage existant toléré) contredit l'EXIG-GOV-20 et l'EXIG-INT-06.
3. La suspension, à la passerelle, d'une identité « suspendue » bloque aussi les compensations des sagas en cours, et elle ne touche pas les agents intégrés aux logiciels-services.

## Constats

### [17-01] [BLOQUANT] La matrice RACI viole la séparation des fonctions qu'elle prétend servir
- **Axe** : A
- **Localisation** : § 11.1, p. 161, EXIG-GOV-03 : « Une même personne NE DOIT PAS à la fois préparer et approuver une décision du cycle de vie d'un agent »; tableau 44, p. 162 : « Concevoir, construire et évaluer » → RT « A, R »; « Attester périodiquement l'agent » → PM « A, R »; EXIG-GOV-11, p. 167 : « le décideur désigné par tableau 44 ».
- **Diagnostic** : l'EXIG-GOV-04 exige de nommer les personnes qui tiennent les rôles R et A. Sur deux lignes, le tableau 44 attribue les deux rôles au même rôle nominatif, donc à la même personne. Or le point de contrôle de l'étape 3 (« Seuils d'évaluation atteints », figure 25) est une décision du cycle de vie, et l'annexe A (A.2) cite expressément l'évaluation : « la personne qui prépare une décision du cycle de vie (construction, évaluation) n'est pas celle qui l'approuve ». Le responsable technique évalue donc son propre agent puis déclare les seuils atteints. Même problème pour le point de contrôle de l'étape 5 : le parrain prépare et approuve seul l'attestation (« A, R »), y compris pour la classe élevée, dont la « Revue semestrielle » (tableau 46) se réduit à cette auto-attestation, sans regard indépendant.
- **Contre-exemple** : un RT pressé par l'échéance abaisse un seuil du jeu d'évaluation, constate qu'il est « atteint » et consigne lui-même le passage (EXIG-GOV-11). La fiche est conforme au tableau 44, mais non conforme à l'EXIG-GOV-03 et à l'annexe A. Les deux lectures sont normatives et contradictoires.
- **Correctif proposé** : scinder la ligne en « Concevoir et construire » (RT A, R) et « Valider l'atteinte des seuils d'évaluation » (A = PM ou RC, R = RT). Pour l'attestation, mettre PM en R et une fonction indépendante en A (RC, ou CO pour la classe élevée), ou bien exclure expressément l'attestation du champ de l'EXIG-GOV-03, avec justification.
- **Confiance** : vérifié dans le texte.

### [17-02] [BLOQUANT] Le statut « Contenir » est inapplicable sous l'EXIG-GOV-20 et l'EXIG-INT-06
- **Axe** : A / C
- **Localisation** : § 11.7, p. 169 : « « Contenir » tolère l'existant, interdit tout nouvel usage et exige un plan de sortie »; EXIG-GOV-20, p. 170 : « Un standard ou un projet NE DOIT PAS être utilisé, même en pilote avec des données réelles, s'il ne figure pas au catalogue au statut « Évaluer » ou « Adopter » ».
- **Diagnostic** : un standard au statut « Contenir » n'est ni « Évaluer » ni « Adopter ». L'EXIG-GOV-20 en interdit donc tout usage, alors que la définition du statut (et le tableau 15, p. 49 : « Tolérés derrière un adaptateur ») en tolère l'usage existant en production. L'EXIG-INT-06 (p. 50) aggrave la contradiction : « DOIT figurer au catalogue avec le statut Adopter pour être employé en production ». Le statut est soit lettre morte, soit une violation permanente. Accessoirement, « même en pilote avec des données réelles » laisse ambigu l'usage « Surveiller » (essais hors production sans données réelles) : est-il interdit lui aussi?
- **Contre-exemple** : un format propre à un fournisseur, classé « Contenir » au tableau 15, sert en production derrière un adaptateur. Un auditeur qui applique l'EXIG-GOV-20 doit exiger l'arrêt immédiat, ce qui rend caduc le plan de sortie daté qu'exige le statut.
- **Correctif proposé** : reformuler l'EXIG-GOV-20 : « … NE DOIT PAS être utilisé avec des données réelles s'il ne figure pas au catalogue au statut Évaluer ou Adopter, ou, pour un usage existant, au statut Contenir avec un plan de sortie daté ». Ajouter la même exception à l'EXIG-INT-06 et préciser que « Surveiller » permet les essais sans données réelles.
- **Confiance** : vérifié dans le texte.

### [17-03] [MAJEUR] L'EXIG-GOV-11 renvoie à un décideur que le tableau 44 ne désigne pas
- **Axe** : C / A
- **Localisation** : EXIG-GOV-11, p. 167 : « Chaque passage est consigné au registre avec la date, le décideur désigné par tableau 44 et les preuves »; figure 25, p. 166.
- **Diagnostic** : les six points de contrôle de la figure 25 ne correspondent pas aux activités du tableau 44. « Revue d'architecture et de sécurité » (étape 2) n'a aucune ligne : est-ce AE, SÉC, ou les deux (deux « A », interdits par l'EXIG-GOV-04)? « Seuils d'évaluation atteints » relève de la ligne fusionnée « Concevoir, construire et évaluer » (voir 17-01). « Preuve de révocation » n'a pas de décideur propre (la ligne « Retirer l'agent » donne A au PM, qui n'opère pas la révocation). Pour ces points, l'exigence de consigner « le décideur désigné » ne peut pas être satisfaite de façon déterministe.
- **Contre-exemple** : la revue d'architecture et de sécurité d'un agent modéré est consignée avec AE comme décideur dans un domaine et avec SÉC dans un autre. Les deux fiches sont « conformes », et l'audit ne peut rien comparer.
- **Correctif proposé** : ajouter au tableau 44 une ligne par point de contrôle de la figure 25 (ou une colonne « point de contrôle » qui renvoie à l'activité), chacune avec un seul A.
- **Confiance** : vérifié dans le texte.

### [17-04] [MAJEUR] Classe de risque « avant l'inscription », alors que le cycle de vie inscrit d'abord et classe ensuite
- **Axe** : C / A
- **Localisation** : EXIG-CON-01, p. 172 : « Chaque agent DOIT recevoir une classe de risque […] avant son inscription au registre (section 11.4) »; § 11.5, p. 166, étape 1 : « fiche créée à l'état « proposé », avec une première estimation de la classe de risque »; étape 2 : « L'équipe propose la classe de risque, que la fonction risques et conformité tranche ».
- **Diagnostic** : le cycle de vie crée la fiche (inscription) à l'étape 1 et ne tranche la classe qu'à l'étape 2; le tableau 44 place d'ailleurs « Inscrire l'agent au registre » avant « Classer le risque ». L'EXIG-CON-01 (et l'annexe A, A.2 : « Classe de risque attribuée et approuvée avant l'inscription ») impose l'ordre inverse. Comme la décision de classement doit elle-même être consignée au registre (EXIG-GOV-11, EXIG-CON-01 : « consignée dans la fiche d'agent »), l'exigence est circulaire : on ne peut pas consigner dans une fiche qui n'existe pas encore.
- **Contre-exemple** : une proposition inscrite à l'état « proposé » avec une classe « estimée » est non conforme à l'EXIG-CON-01 dès sa création; à l'inverse, une classe tranchée hors registre n'a aucune trace auditable.
- **Correctif proposé** : dans l'EXIG-CON-01, remplacer « avant son inscription au registre » par « avant la sortie de l'état « en conception » » (ou « avant la revue d'architecture et de sécurité »), et aligner l'annexe A.
- **Confiance** : vérifié dans le texte.

### [17-05] [MAJEUR] Le délai de grâce de 30 jours pour un rôle A vacant contredit les EXIG-GOV-04 et EXIG-GOV-08
- **Axe** : A
- **Localisation** : EXIG-GOV-09, p. 165 : « dont un rôle A est vacant depuis plus de 30 jours, DOIT passer à l'état « suspendu » »; EXIG-GOV-04, p. 162 : « une fiche dont un rôle A est vacant est incomplète »; EXIG-GOV-08, p. 165 : « NE DOIT PAS recevoir de justificatif valide en production tant que sa fiche n'est pas complète ».
- **Diagnostic** : dès la vacance, la fiche est incomplète (EXIG-GOV-04). Or les justificatifs d'agent sont « de courte durée » et renouvelés au besoin (ch. 9, p. ~120, EXIG-IAM : « justificatif cryptographique émis par la plateforme, de courte durée »). Chaque renouvellement est une « réception » que l'EXIG-GOV-08 interdit. La suspension est donc de fait immédiate, et le délai de 30 jours de l'EXIG-GOV-09 est inopérant. De plus, l'annexe A tient la « Fiche complète au registre » pour « non dérogeable » : l'exploitation pendant 30 jours avec une fiche incomplète n'est permise que par le cadre lui-même, ce qui affaiblit la non-dérogeabilité.
- **Contre-exemple** : le parrain quitte l'entreprise un vendredi. Lundi, le SVID ou le jeton expire et doit être renouvelé, mais la fiche est incomplète, donc l'émission est refusée (EXIG-GOV-08). L'agent tombe sans préavis, alors que l'EXIG-GOV-09 promettait 30 jours.
- **Correctif proposé** : choisir explicitement. Soit l'EXIG-GOV-08 vise « complète à l'approbation initiale », et une vacance survenue ensuite relève de l'EXIG-GOV-09 (délai de grâce avec intérim nommé obligatoire); soit on supprime le délai de 30 jours. Exiger dans tous les cas un suppléant nommé pour chaque rôle A dans la fiche.
- **Confiance** : déduit (combinaison de trois exigences vérifiées dans le texte).

### [17-06] [MAJEUR] L'EXIG-GOV-08 ne fait refuser que deux états sur sept à la passerelle
- **Axe** : A
- **Localisation** : EXIG-GOV-08, p. 165 : « La passerelle d'agents DOIT refuser tout appel d'une identité absente du registre ou à l'état « suspendu » ».
- **Diagnostic** : le refus à la passerelle ne vise que l'absence et l'état « suspendu ». Les états « proposé », « en conception », « en construction » et surtout « retiré » ne sont pas couverts. Le contrôle repose alors sur la seule non-émission ou révocation des justificatifs, qui se propage « dans le délai maximal fixé par l'entreprise » (EXIG-GOV-14, EXIG-IAM-07), donc pas instantanément. Pendant cette fenêtre, un agent « retiré » dont le jeton reste valide passe la passerelle. Rien n'est dit non plus des identités de serveurs MCP visées par la première phrase : seule la « passerelle d'agents » est tenue de refuser.
- **Contre-exemple** : un agent est retiré à 10 h et le délai de révocation mesuré est de 15 min. À 10 h 05, son jeton encore valide est accepté, puisque la fiche n'est ni absente ni « suspendue ».
- **Correctif proposé** : formuler en liste blanche : « La passerelle DOIT refuser tout appel d'une identité dont la fiche n'est pas à l'état « pilote » ou « production » », et appliquer la règle à toutes les passerelles (modèles, agents, MCP).
- **Confiance** : vérifié dans le texte.

### [17-07] [MAJEUR] La suspension, brutale et sans exception, bloque les compensations des sagas en cours
- **Axe** : A / B
- **Localisation** : EXIG-GOV-08, p. 165 : « refuser tout appel d'une identité […] à l'état « suspendu » »; EXIG-GOV-09, p. 165 (attestation échue ⇒ « suspendu »); EXIG-GOV-16, p. 168 (dérogation échue ⇒ « suspendu »); § 11.5, p. 167 : « La suspension […] est immédiate et réversible ».
- **Diagnostic** : l'EXIG-ORC-28 (§ 7.8) exige que l'arrêt laisse « les sagas en cours dans un état connu, suspendues ou compensées selon la procédure ». Or si la passerelle refuse tout appel de l'identité suspendue, les appels de compensation émis sous cette identité sont refusés aussi (thèse T3). Le cadre fait en outre déclencher la même suspension immédiate par des causes administratives (attestation échue, dérogation échue, rôle vacant), sans préavis aux consommateurs, alors que le retrait planifié exige 60 jours de préavis (EXIG-GOV-14). Une négligence de calendrier produit donc l'effet d'un coupe-circuit de sécurité.
- **Contre-exemple** : un agent P2 réserve un stock, puis débite un compte. L'attestation expire à minuit entre les deux étapes. La compensation (« libérer la réservation ») est refusée par la passerelle : le stock reste bloqué jusqu'à intervention manuelle, et les agents consommateurs échouent sans avis.
- **Correctif proposé** : distinguer deux modes. Une suspension de sécurité (coupe-circuit, immédiate) et une suspension administrative (blocage des nouvelles tâches seulement, avec avis aux consommateurs), toutes deux avec une liste blanche de compensations autorisées sous une identité ou une portée dédiée, journalisée. Exiger un avertissement préalable (comme les 30 jours de l'EXIG-GOV-16) pour l'échéance d'attestation.
- **Confiance** : déduit.

### [17-08] [MAJEUR] Suspension et quarantaine sont sans prise sur les agents intégrés aux logiciels-services
- **Axe** : B / A
- **Localisation** : EXIG-GOV-07, p. 165 : « qu'il soit développé à l'interne, intégré à un logiciel-service ou exploité par un partenaire »; ATTENTION, p. 165 : « la suspension d'un agent s'applique à la passerelle d'agents, pas seulement dans la console de son éditeur »; EXIG-GOV-10, p. 166 : « placer en quarantaine tout agent découvert hors registre ».
- **Diagnostic** : un agent intégré à un logiciel-service agit le plus souvent sur les données de ce service, à l'intérieur de la plateforme de l'éditeur, sans traverser la passerelle de l'entreprise. Les justificatifs sont souvent émis par l'éditeur, pas par la plateforme de l'entreprise. Ni le refus à la passerelle (EXIG-GOV-08) ni la non-émission de justificatifs ne l'arrêtent; l'ATTENTION reconnaît d'ailleurs que les actions de cycle de vie sur les agents tiers sont « annoncées comme à venir ». Les agents « découverts hors registre » par l'EXIG-GOV-10 sont précisément ceux qui ont échappé à la passerelle, puisque celle-ci refuse les identités absentes. La « quarantaine » n'a alors aucun mécanisme défini (thèse T2).
- **Contre-exemple** : un agent Copilot créé par un employé (identité Entra Agent ID automatique, p. 166) lit et modifie des documents SharePoint. Il est découvert au rapprochement mensuel, mais aucune passerelle n'est sur son chemin : la « quarantaine » se réduit à une demande à la console de l'éditeur, ce que l'ATTENTION juge insuffisant.
- **Correctif proposé** : exiger, pour chaque agent intégré à un logiciel-service, un mécanisme d'arrêt documenté et testé (désactivation dans le fournisseur d'identité, CAEP ou SSF, contrat), consigné dans la fiche (EXIG-IAM-20), et définir la quarantaine comme un ensemble d'actions concrètes par type de source.
- **Confiance** : déduit.

### [17-09] [MAJEUR] Le registre, consulté « à chaque appel », est un point unique de défaillance non spécifié
- **Axe** : B
- **Localisation** : § 11.4, p. 164 : « ce qui permet à la passerelle de vérifier à chaque appel l'état de la fiche et la version épinglée du contrat ».
- **Diagnostic** : la consultation synchrone du registre à chaque appel place le registre sur le chemin critique de tous les agents. Aucune exigence du chunk (ni, d'après une recherche de « registre » près de « indisponib » ou de « cache » dans le texte complet, ailleurs) ne fixe sa disponibilité, sa latence, son mode de réplication ou une politique de cache. Avec l'échec en mode fermé (PRIN-12), une panne du registre arrête tout le parc; avec un cache, la suspension n'est plus « immédiate » mais bornée par le TTL, que rien ne fixe.
- **Contre-exemple** : une migration de la base du registre provoque 20 min d'indisponibilité. Toutes les passerelles refusent tous les appels, y compris les compensations (voir 17-07). Ou bien un cache de 10 min est introduit pour la latence, et un agent suspendu continue d'agir 10 min.
- **Correctif proposé** : exiger un objectif de disponibilité du registre au moins égal à celui de la passerelle, une copie en lecture locale aux passerelles avec un TTL maximal inscrit et mesuré dans l'exercice de coupe-circuit (EXIG-ORC-28, EXIG-IAM-20), et un comportement défini en cas de registre injoignable.
- **Confiance** : déduit (absence vérifiée par recherche lexicale, non exhaustive).

### [17-10] [MAJEUR] L'exception « Si le changement ne peut attendre » contredit la règle « avant leur mise en production »
- **Axe** : A
- **Localisation** : EXIG-GOV-12, p. 167 : « DOIVENT déclencher une réévaluation […] avant leur mise en production » puis « Si le changement ne peut attendre, l'agent fonctionne au niveau d'autonomie inférieur jusqu'à la fin de la réévaluation ».
- **Diagnostic** : la seconde phrase autorise la mise en production avant réévaluation, ce que la première interdit et que l'EXIG-CON-03 (p. 172 : « avant la mise en production du changement ») interdit aussi, sans exception. L'exception n'a ni décideur, ni critère d'urgence, ni durée maximale. Elle peut aussi heurter une obligation légale non dérogeable (EXIG-GOV-17) : l'ajout d'une « nouvelle catégorie de données, notamment de RP » est une refonte qui exige une EFVP terminée (art. 3.3 de la Loi sur le privé; EXIG-CON-04). Abaisser l'autonomie d'un cran n'y supplée pas. Enfin, si le changement fait monter la classe (p. ex. de modérée à élevée), « le niveau inférieur » (N3 → N2) est fortuitement conforme, mais une classe faible en N4 qui devient élevée tomberait à N3, au-dessus du plafond N2.
- **Contre-exemple** : un agent faible en N4 se voit ajouter des RP sensibles « en urgence ». Sous l'exception, il passe en production en N3, sans EFVP et au-dessus du plafond de sa nouvelle classe élevée (N2).
- **Correctif proposé** : restreindre l'exception aux changements imposés de l'extérieur (retrait d'un modèle par le fournisseur, correctif de sécurité), sur décision nommée (RC ou CO), pour une durée bornée. L'exclure pour tout changement qui touche les RP ou la classe, et fixer le niveau d'exploitation au minimum de « niveau inférieur » et du plafond de la classe réévaluée provisoirement.
- **Confiance** : vérifié dans le texte (contradiction); déduit (scénario).

### [17-11] [MAJEUR] L'exemple de changement de modèle suppose que le fournisseur garde l'ancienne version, et confond qualité et autonomie
- **Axe** : B
- **Localisation** : EXEMPLE, p. 167 : « Si les seuils ne sont pas atteints, l'agent reste sur l'ancienne version, ou redescend à N2 le temps de corriger ».
- **Diagnostic** : 1) Rester sur la version épinglée suppose que le fournisseur la maintient; quand elle est retirée à une date imposée, l'option disparaît, et le cas n'est pas traité (aucun lien avec le repli homologué du § 7.8 ni avec les clauses de préavis du ch. 13). 2) Un échec aux seuils d'évaluation (qualité, sécurité) n'est pas corrigé en baissant l'autonomie : en N2, les mêmes erreurs sont présentées aux approbateurs, ce qui nourrit l'approbation machinale (§ 8.7). 3) Le Pourquoi invoque l'E-23, qui « déclenche une revue indépendante », mais l'exemple ne comporte aucune revue indépendante : RC confirme la classe, puis le parrain approuve. Le Pourquoi de l'EXIG-AUT-05 décrit l'E-23 autrement (« définissent des critères de modification importante »).
- **Contre-exemple** : le fournisseur retire la version épinglée le 1er mars, et la nouvelle échoue au jeu d'évaluation. L'agent ne peut ni rester ni « redescendre » utilement : seul le repli ou la suspension reste possible, et le texte n'en dit rien.
- **Correctif proposé** : compléter l'exemple avec le cas du retrait imposé (repli homologué ou suspension planifiée) et remplacer « redescend à N2 » par une condition (seulement si l'échec est compensé par l'approbation humaine). Harmoniser la description de l'E-23 entre l'EXIG-GOV-12 et l'EXIG-AUT-05, et prévoir la revue indépendante pour les institutions assujetties.
- **Confiance** : vérifié dans le texte (points 2 et 3); à vérifier (source externe) pour le libellé exact de l'E-23 sur la revue indépendante.

### [17-12] [MAJEUR] Le pilote reçoit des justificatifs de production sans que l'équipe rouge ni l'homologation soient des conditions d'entrée
- **Axe** : A / C
- **Localisation** : § 11.4, p. 164 : « Seuls les états « pilote » et « production » permettent d'obtenir des justificatifs d'exécution en production »; § 11.5, p. 166, étape 3 : « Point de contrôle : seuils d'évaluation atteints (section 10.4), fiche complète et, s'il y a des RP, EFVP terminée »; étape 4 : « homologation selon la grille d'homologation (annexe A) ».
- **Diagnostic** : le pilote s'exécute en production, avec des justificatifs de production et des données réelles, mais l'homologation n'intervient qu'à sa sortie. L'équipe rouge est exigée « avant sa mise en production » (EXIG-SEC-23; tableau 46, p. 171 : « équipe rouge avant production »), et l'homologation du niveau aussi (EXIG-AUT-05 : « homologué avant la mise en production »). Le texte ne dit pas si l'entrée en pilote est une « mise en production ». Selon la lecture, un agent de classe élevée peut traiter des données réelles en pilote sans exercice d'équipe rouge, ou bien l'homologation de fin de pilote arrive trop tard. Le point de contrôle de l'étape 3 ne mentionne pas l'équipe rouge.
- **Contre-exemple** : un agent de préqualification de prêts (classe élevée, p. 172) entre en pilote auprès de vrais clients sur la foi des seuils d'évaluation et de l'EFVP; l'exercice d'équipe rouge est planifié « avant production », c'est-à-dire après le pilote.
- **Correctif proposé** : définir « mise en production » comme l'entrée à l'état « pilote » pour l'application des EXIG-SEC-23, EXIG-AUT-05 et EXIG-CON-26, ou ajouter l'équipe rouge (classes modérée et élevée) et une homologation provisoire au point de contrôle de l'étape 3.
- **Confiance** : vérifié dans le texte (ambiguïté); déduit (scénario).

### [17-13] [MAJEUR] La liste des exigences non dérogeables omet les contrôles contre les dommages qu'elle invoque
- **Axe** : A / B
- **Localisation** : EXIG-GOV-17, p. 169 : « ces règles protègent contre des dommages irréversibles »; p. 172 : « un agent en lecture seule qui consulte des dossiers médicaux reste de classe élevée, parce qu'une fuite ne se répare pas ».
- **Diagnostic** : l'exfiltration de données est l'exemple même du dommage irréversible selon le cadre, mais les contrôles qui la préviennent restent dérogeables : retrait déterministe des capacités d'envoi après lecture de contenu non fiable (triade létale, § 9.6), journal d'audit chaîné (§ 10.3), échec en mode fermé (PRIN-12). Seuls figurent NX, P3 sans approbation, usurpation, absence de fiche ou de parrain, et dépassement de plafond. La justification énoncée ne correspond donc pas à la liste.
- **Contre-exemple** : un domaine obtient une dérogation de six mois, renouvelable, à la règle de la triade létale pour un agent modéré qui lit des courriels externes et peut envoyer des messages : l'exfiltration de RP devient possible sous un régime « conforme ».
- **Correctif proposé** : ajouter à l'EXIG-GOV-17 (et au § 4.3 et à l'annexe A) au moins la règle de la triade létale et l'existence du journal d'audit, ou réécrire le Pourquoi pour dire que la liste est minimale et que le reste relève du jugement du comité.
- **Confiance** : déduit.

### [17-14] [MAJEUR] La révision extraordinaire ne vise que les standards « Adopter » et ne tient pas les fenêtres de 90 jours
- **Axe** : B / A
- **Localisation** : EXIG-GOV-18, p. 169 : « Une révision extraordinaire DOIT avoir lieu dès qu'un standard au statut « Adopter » publie une version majeure ou une dépréciation; un correctif de sécurité PEUT aussi la justifier ».
- **Diagnostic** : 1) Les standards « Contenir » (en production par définition) et « Évaluer » (pilotes avec données réelles, EXIG-GOV-20) n'ont aucun déclencheur extraordinaire. 2) La fenêtre de retrait accéléré de MCP (90 jours, p. 169) est égale à la période de révision ordinaire (trimestre) : une dépréciation annoncée juste après une révision peut expirer avant la suivante si elle touche un standard non « Adopter », ou un correctif de sécurité, laissé à « PEUT ». 3) Pour les conventions GenAI d'OpenTelemetry, classées « Adopter » au tableau 15 et qui « peuvent changer sans processus de dépréciation » (p. 169), la règle « échéance [qui] précède la fin de la fenêtre de dépréciation annoncée » est indéfinie : il n'y a pas de fenêtre.
- **Contre-exemple** : une extension au statut « Évaluer » (p. ex. Enterprise-Managed Authorization) est retirée en accéléré pour une faille active. Aucune révision extraordinaire n'est exigée, et les pilotes avec données réelles continuent sur une fonctionnalité vulnérable jusqu'à la révision trimestrielle.
- **Correctif proposé** : étendre le déclencheur à tout statut autre que « Surveiller », rendre obligatoire (DOIT) la révision sur avis de sécurité, et prévoir pour les composants sans politique de dépréciation une règle propre (épinglage plus test de non-régression à chaque version).
- **Confiance** : vérifié dans le texte.

### [17-15] [MAJEUR] Les critères d'admission de l'EXIG-GOV-19 ne sont pas satisfaits par des entrées « Adopter » du catalogue
- **Axe** : A / C
- **Localisation** : EXIG-GOV-19, p. 169-170 : « spécification publique, versionnée et assortie d'une politique de compatibilité et de dépréciation »; « un brouillon ou un composant de niveau expérimental n'est admis qu'avec une réserve inscrite au catalogue ».
- **Diagnostic** : la réserve ne lève que le critère 3 (statut final). Or les conventions GenAI d'OpenTelemetry, « Adopter » au tableau 15, sont décrites p. 169 comme pouvant « changer sans processus de dépréciation » : elles échouent au critère 1, que la réserve ne couvre pas. OAuth 2.1 (Internet-Draft, « Adopter » avec réserve) n'a pas non plus de politique de dépréciation propre. La réserve vide en pratique le critère 3 de sa force, puisque tout brouillon peut être « Adopter ». Enfin, les RFC de l'IETF n'ont pas de « politique de compatibilité et de dépréciation » au sens d'un registre de fonctionnalités : une lecture littérale du critère 1 exclurait la RFC 8693.
- **Contre-exemple** : un auditeur applique l'EXIG-GOV-19 au tableau 15 et doit déclasser les conventions GenAI, socle de tout le ch. 10.
- **Correctif proposé** : faire porter explicitement la réserve sur les critères 1 et 3, définir ce qui tient lieu de politique de dépréciation pour une RFC (mécanisme « obsoletes/updates ») et exiger, pour tout « Adopter avec réserve », une date de réexamen.
- **Confiance** : vérifié dans le texte; déduit pour l'interprétation des RFC.

### [17-16] [MAJEUR] Le comité est un goulot d'étranglement sans délai de décision ni fréquence fixée
- **Axe** : B
- **Localisation** : p. 161 : « Approuve les agents de classe élevée et tout niveau N4; accorde les dérogations; approuve le catalogue des protocoles; révise le cadre chaque semestre »; EXIG-GOV-02, p. 161 (fréquence laissée au mandat); EXIG-GOV-14, p. 168 : « retrait anticipé pour un motif de sécurité, décidé par le comité »; § 11.3, p. 163 : « Tout centraliser crée un goulot d'étranglement ».
- **Diagnostic** : le comité est A pour toutes les homologations de classe élevée, tout N4, toutes les dérogations (sauf la délégation pour la classe faible), tous les renouvellements, tout changement de statut au catalogue (y compris en révision extraordinaire), les retraits anticipés de sécurité et la déclaration de tolérance au risque (EXIG-CON-17). Aucune exigence ne fixe de délai de décision, de quorum minimal ou de procédure d'urgence. Le cadre recrée ainsi pour la gouvernance le goulot qu'il reproche à la centralisation technique.
- **Contre-exemple** : une faille active impose le retrait d'un standard en moins de 90 jours et le retrait anticipé de trois agents. Le comité, mensuel, ne se réunit pas à temps : les agents restent « suspendus » sans décision (seule voie compatible avec l'EXIG-GOV-14), et les migrations ne sont pas approuvées.
- **Correctif proposé** : exiger dans le mandat (EXIG-GOV-02) une procédure d'urgence (décision par un sous-comité ou par le président, ratifiée a posteriori) et des délais de décision par type de dossier, mesurés comme indicateurs.
- **Confiance** : déduit.

### [17-17] [MINEUR] « Franchir dans l'ordre les six points de contrôle » ne prévoit ni abandon, ni retour en arrière, ni suspension
- **Axe** : A
- **Localisation** : EXIG-GOV-11, p. 167 : « Un agent DOIT franchir dans l'ordre les six points de contrôle de figure 25 ».
- **Diagnostic** : lu littéralement, un projet abandonné à l'état « proposé » doit passer l'évaluation et l'homologation avant son « retrait ». La réévaluation (EXIG-GOV-12) renvoie aux étapes 2 à 4, ce qui fait revenir en arrière. Le point de contrôle de l'étape 5 est récurrent, pas franchi une fois. Les transitions vers et depuis « suspendu » ne sont rattachées à aucun point de contrôle.
- **Contre-exemple** : un cas d'usage est refusé à la revue d'architecture : il ne peut pas être conformément « retiré ».
- **Correctif proposé** : remplacer la clause par un diagramme d'états avec des transitions autorisées (dont l'abandon de tout état vers « retiré », et « suspendu » ↔ état antérieur), chacune avec sa preuve.
- **Confiance** : vérifié dans le texte.

### [17-18] [MINEUR] Cinq listes divergentes de déclencheurs de réévaluation
- **Axe** : C / B
- **Localisation** : EXIG-GOV-12, p. 167 (« modification de l'invite système », « ajout d'un outil ou passage d'un outil à un palier supérieur »); EXIG-CON-03, p. 172 (« d'outil ou de palier d'outil »); figure 25, p. 166 (« Changement de modèle, d'invite, d'outil, de protocole ou de population visée »); EXIG-AUT-05 (« hors correction purement typographique », « d'outil en écriture »); annexe A, A.2.
- **Diagnostic** : les listes diffèrent sur des points matériels. Seule l'EXIG-AUT-05 exclut les corrections typographiques d'invite. Le retrait d'un outil ou la baisse de palier déclenche l'EXIG-CON-03 mais pas l'EXIG-GOV-12. L'ODD et la dérive figurent dans l'EXIG-GOV-12 mais pas dans l'EXIG-CON-03. Sans exclusion, toute retouche d'invite relance la réévaluation complète de la classe et du niveau, d'un coût disproportionné.
- **Contre-exemple** : une coquille corrigée dans l'invite est exemptée par l'EXIG-AUT-05 mais déclenche l'EXIG-GOV-12.
- **Correctif proposé** : désigner une liste unique (comme l'EXIG-CON-02 pour les plafonds) à laquelle les autres renvoient.
- **Confiance** : vérifié dans le texte.

### [17-19] [MINEUR] Pilote « un niveau sous la cible » : texte conditionnel et non normatif, figure inconditionnelle
- **Axe** : C / B
- **Localisation** : § 11.5, p. 166 : « Le pilote d'un agent qui vise N3 ou N4 devrait s'exécuter au niveau immédiatement inférieur »; figure 25 : « un niveau sous la cible ».
- **Diagnostic** : le « devrait » en minuscules, hors d'un bloc EXIG, n'a pas de force normative (§ 1.4). La figure l'étend à tous les niveaux, alors que le texte le limite à N3 et N4. Si la règle est suivie, le niveau cible n'est jamais observé avant l'homologation, qui pourtant homologue ce niveau.
- **Correctif proposé** : en faire une EXIG DEVRAIT limitée à N3 et N4, aligner la figure et prévoir une phase de pilote finale au niveau cible sous surveillance renforcée.
- **Confiance** : vérifié dans le texte.

### [17-20] [MINEUR] Trois formulations divergentes des points non dérogeables, et un « ni » ambigu
- **Axe** : C
- **Localisation** : EXIG-GOV-17, p. 169 : « l'exploitation d'un agent sans fiche au registre ni parrain nommé »; § 4.3, p. 30 : « la mise en production d'un agent sans personne nommée qui en répond »; annexe A : « Fiche complète au registre » et « Aucune action P3 sans approbation humaine, par jeton signé lié à l'action » marqués non dérogeables.
- **Diagnostic** : « sans X ni Y » se lit « ni X ni Y ». Un agent qui a une fiche mais pas de parrain n'est donc pas visé à la lettre. L'annexe A est plus stricte (fiche « complète », « jeton signé ») que l'EXIG-GOV-17, à laquelle elle renvoie pourtant.
- **Correctif proposé** : « sans fiche complète au registre ou sans parrain nommé », et aligner les trois listes sur l'EXIG-GOV-17 comme source unique.
- **Confiance** : vérifié dans le texte.

### [17-21] [MINEUR] La procédure de dérogation ne couvre pas les dérogations qui ne visent pas un agent
- **Axe** : A / C
- **Localisation** : EXIG-GOV-05, p. 164 : « exploiter de passerelle, de registre ou de catalogue parallèle sans dérogation (section 11.6) »; EXIG-GOV-15, p. 168 : « demandée par écrit par le parrain »; contenu minimal : « le ou les agents concernés ».
- **Diagnostic** : une dérogation à l'EXIG-GOV-05 vise un domaine ou un composant (passerelle parallèle), sans agent ni parrain désigné. Elle n'a donc ni demandeur habilité ni fiche où la rendre « visible ». Le § 4.3 (p. 30 : « jamais une catégorie entière ») est en tension avec « le ou les agents ».
- **Correctif proposé** : prévoir un demandeur pour les composants (propriétaire du composant ou responsable de domaine) et l'inscription de la dérogation à la fiche du composant.
- **Confiance** : vérifié dans le texte.

### [17-22] [MINEUR] La délégation à l'architecture d'entreprise crée un second « A » et un cumul instruction-décision
- **Axe** : C / A
- **Localisation** : tableau 44, p. 162 : « Accorder une dérogation » → AE « R », CO « A »; EXIG-GOV-15, p. 168 : « Le comité PEUT déléguer à l'architecture d'entreprise les dérogations qui visent un agent de classe faible ».
- **Diagnostic** : en délégation, AE devient A tout en étant R (instruction), ce que le tableau ne montre pas (EXIG-GOV-04 : un seul A). L'exigence se contente d'une personne différente au sein de la même fonction. Hors délégation, l'AE, membre du comité (EXIG-GOV-02), instruit puis participe à la décision : aucune récusation n'est prévue (EXIG-GOV-03).
- **Correctif proposé** : ajouter au tableau 44 une note de délégation et une règle de récusation dans le mandat du comité.
- **Confiance** : vérifié dans le texte.

### [17-23] [MINEUR] Rôles du comité et de la fonction sécurité, risques et gouvernance incohérents entre tableaux et exigences
- **Axe** : C
- **Localisation** : tableau 44, p. 162 : « Retirer l'agent » → CO « — »; EXIG-GOV-14, p. 168 : « retrait anticipé pour un motif de sécurité, décidé par le comité »; tableau 45, p. 163 : sécurité, risques et gouvernance « C : vérifie la complétude; peut déclencher le coupe-circuit ».
- **Diagnostic** : le comité est « non concerné » par une activité dont il est décideur dans un cas. Déclencher le coupe-circuit est une action (R), pas une consultation (C).
- **Correctif proposé** : CO « A (retrait anticipé) » dans le tableau 44; dans le tableau 45, « R : déclenche le coupe-circuit ».
- **Confiance** : vérifié dans le texte.

### [17-24] [MINEUR] Justification circulaire du délai de 60 jours
- **Axe** : C
- **Localisation** : EXIG-GOV-14, p. 168 : « Le préavis de 60 jours est un choix du cadre, aligné sur la coexistence des versions (section 6.8) »; EXIG-INT-14 (p. 82) : « il concorde avec le préavis de retrait d'un agent (section 11.5) ».
- **Diagnostic** : chaque délai se justifie par l'autre; aucun ne repose sur une base indépendante (temps de migration mesuré, contrat).
- **Correctif proposé** : énoncer une fois le fondement (« choix du cadre, fondé sur … ») et faire renvoyer l'autre exigence à celle-là.
- **Confiance** : vérifié dans le texte.

### [17-25] [MINEUR] Redondance EXIG-GOV-13, EXIG-IAM-07 et EXIG-GOV-09
- **Axe** : C
- **Localisation** : EXIG-GOV-13, p. 167 (attestation à 12 et 6 mois, revue trimestrielle, « désactiver ceux qui ne sont pas régularisés (EXIG-IAM-07) »).
- **Diagnostic** : l'EXIG-IAM-07 énonce déjà les mêmes périodicités et la même revue trimestrielle. L'EXIG-GOV-09 fait suspendre automatiquement à l'échéance, alors que la revue trimestrielle « désactive ». Trois sources pour un même contrôle, avec deux sanctions (« suspendu » ou « désactivé ») et deux délais (échéance ou trimestre) : le risque de dérive que la v1.1 a corrigé pour les plafonds réapparaît ici.
- **Correctif proposé** : faire de l'EXIG-GOV-13 la source unique, l'EXIG-IAM-07 n'y renvoyant que pour la révocation.
- **Confiance** : vérifié dans le texte.

### [17-26] [MINEUR] « Quarantaine » et « désactivé » hors des sept états; transitions non définies
- **Axe** : C
- **Localisation** : § 11.4, p. 164 : « La fiche passe par sept états »; EXIG-GOV-10, p. 166 : « placer en quarantaine »; EXIG-GOV-13 : « désactiver ».
- **Diagnostic** : un agent découvert hors registre n'a pas de fiche, donc pas d'état. La « quarantaine » n'est pas un état et ses effets ne sont pas définis. « Désactivé » se confond-il avec « suspendu »? La sortie de « suspendu » (vers quel état?) n'est pas précisée.
- **Correctif proposé** : définir la quarantaine (fiche minimale créée d'office à l'état « suspendu », par exemple) et l'équivalence « désactivé = suspendu ».
- **Confiance** : vérifié dans le texte.

### [17-27] [MINEUR] Pourquoi de l'EXIG-GOV-13 : « borne la plus stricte » et « choix du cadre » se contredisent
- **Axe** : C
- **Localisation** : p. 167 : « le cadre retient la borne la plus stricte pour la classe élevée, et les périodicités de 12 mois, de 6 mois et d'un trimestre sont des choix du cadre ».
- **Diagnostic** : les trois valeurs reprennent les bornes et la cadence de la recommandation de Microsoft citée dans la même phrase; les qualifier de « choix du cadre » brouille la distinction entre exigence externe et choix du cadre (§ 1.4). L'EXIG-IAM-07 le formule mieux : « inscrits dans la plage recommandée par Microsoft ».
- **Correctif proposé** : reprendre la formulation de l'EXIG-IAM-07.
- **Confiance** : vérifié dans le texte.

### [17-28] [MINEUR] Qui révise le catalogue : le comité ou l'architecture d'entreprise?
- **Axe** : C
- **Localisation** : EXIG-GOV-18, p. 169 : « L'architecture d'entreprise DOIT réviser le catalogue des protocoles au moins chaque trimestre et soumettre les changements de statut à l'approbation du comité ».
- **Diagnostic** : le § 6.3 (p. 50) dit « Le comité révise le catalogue chaque trimestre ». Le tableau 44 (AE R, CO A) et l'EXIG-GOV-18 sont cohérents entre eux, mais pas avec le § 6.3.
- **Correctif proposé** : au § 6.3, « L'architecture d'entreprise révise le catalogue chaque trimestre et le comité approuve les changements de statut ».
- **Confiance** : vérifié dans le texte.

### [17-29] [MINEUR] Motif du retrait accéléré de MCP : « risque de sécurité actif » ici, « exceptionnel » ailleurs
- **Axe** : C
- **Localisation** : § 11.7, p. 169 : « ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité actif ».
- **Diagnostic** : les § 2.2 (p. 17), 6.5 (tableau, p. ~57) et 13 (p. ~193) disent « retrait accéléré exceptionnel », sans motif. Les deux énoncés ne sont pas équivalents, puisque le second admet d'autres motifs que la sécurité.
- **Correctif proposé** : aligner sur le libellé exact de la SEP-2596.
- **Confiance** : vérifié dans le texte (divergence); à vérifier (source externe) pour le libellé correct.

### [17-30] [MINEUR] Renvois sans article : « de tableau 44 », « de figure 25 », « par tableau 44 »
- **Axe** : C
- **Localisation** : EXIG-GOV-11, p. 167 : « les six points de contrôle de figure 25 », « le décideur désigné par tableau 44 »; EXIG-GOV-04, p. 162 : « Chaque activité de tableau 44 ».
- **Diagnostic** : artefact probable de génération des renvois (Typst); en français, il faut « de la figure 25 », « par le tableau 44 », « du tableau 44 ».
- **Correctif proposé** : corriger le gabarit de renvoi.
- **Confiance** : vérifié dans le texte.

### [17-31] [MINEUR] La liste minimale des organismes suivis omet des émetteurs de standards normatifs du cadre; « projet » n'est pas défini
- **Axe** : C
- **Localisation** : EXIG-GOV-20, p. 170 : « au minimum l'AAIF […], l'IETF […], OpenTelemetry, le W3C, le NIST […] et l'OWASP GenAI Security Project »; « Un standard ou un projet NE DOIT PAS être utilisé ».
- **Diagnostic** : la liste omet l'OpenID Foundation (SSF, CAEP, CIBA, mobilisés par l'EXIG-IAM-20 et le Pourquoi de l'EXIG-GOV-14), la CNCF (CloudEvents, SPIFFE), l'OpenAPI Initiative et AsyncAPI, tous émetteurs d'entrées « Adopter ». « Projet » pourrait viser toute bibliothèque libre, ce qui étendrait le catalogue des protocoles à des cadriciels régis ailleurs (EXIG-ORC).
- **Correctif proposé** : compléter la liste et remplacer « projet » par « protocole, standard ou extension », comme dans l'EXIG-INT-06.
- **Confiance** : vérifié dans le texte.

### [17-32] [MINEUR] « Certificat d'autonomie » interne sans indépendance ni mode de lecture sûr
- **Axe** : A
- **Localisation** : § 11.4, p. 164 : « un plafond lisible par les autres agents et par la passerelle, valable pour une configuration donnée ».
- **Diagnostic** : le texte reconnaît que Feng et coll. font délivrer le certificat par un tiers; l'adaptation interne perd cette indépendance sans compensation énoncée. La lecture « par les autres agents » n'est pas spécifiée : si un agent lit le niveau déclaré dans la carte de l'agent pair plutôt qu'au registre, il fait confiance à une déclaration non vérifiée (PRIN-07).
- **Correctif proposé** : préciser que seul le registre, interrogé par la passerelle, fait foi, et que la carte d'agent n'en est qu'une copie informative.
- **Confiance** : déduit.

### [17-33] [MINEUR] Deux « catalogues » désignés par le même mot
- **Axe** : C
- **Localisation** : EXIG-GOV-05, p. 164 : « le registre, le catalogue, la chaîne de traçage »; § 11.4, p. 164 : « le catalogue d'entreprise (section 6.8) »; § 11.7 : « catalogue des protocoles et standards (section 6.3) ».
- **Diagnostic** : le catalogue d'entreprise (contrats) et le catalogue des protocoles (statuts) sont distincts, mais « le catalogue » nu, dans l'EXIG-GOV-05, le tableau 45 et la figure 24, ne permet pas de savoir lequel est visé.
- **Correctif proposé** : qualifier systématiquement le terme (« catalogue d'entreprise » ou « catalogue des protocoles »).
- **Confiance** : vérifié dans le texte.

### [17-34] [MINEUR] La paraphrase de la règle centrale ajoute un « hors domaine » restrictif
- **Axe** : C
- **Localisation** : Pourquoi de l'EXIG-GOV-05, p. 164 : « rien n'atteigne un outil, une donnée ou un agent hors domaine sans la passerelle et le catalogue (section 5.1) ».
- **Diagnostic** : l'EXIG-ARC-01 vise « tout appel d'un agent vers un outil, une ressource ou une invite MCP, vers une donnée d'un autre domaine ou vers un autre agent ». Le qualificatif de domaine ne porte que sur les données. La paraphrase peut se lire comme exemptant les appels d'outils intradomaine.
- **Correctif proposé** : « rien n'atteigne un outil, un agent ou une donnée d'un autre domaine sans … ».
- **Confiance** : vérifié dans le texte.

### [17-35] [MINEUR] Renvoi au § 8.1 pour le plafond d'autonomie, dont l'EXIG-CON-02 est la source unique
- **Axe** : C
- **Localisation** : § 11.5, p. 166 : « sous le plafond de cette classe (section 8.1) »; EXIG-GOV-17, p. 169 : « le dépassement du plafond d'autonomie de la classe de risque (section 8.1) ».
- **Diagnostic** : depuis la v1.1, l'EXIG-CON-02 (§ 12.1) fait foi, et le § 8.1 n'y renvoie que par relais (p. 106 : « EXIG-CON-02 pour la classe de risque de l'agent »).
- **Correctif proposé** : renvoyer à l'« EXIG-CON-02 (section 12.1) ».
- **Confiance** : vérifié dans le texte.

## Points forts
Liaison explicite entre l'état du registre et l'émission des justificatifs (inventaire transformé en contrôle d'accès). Dérogations bornées, compensées et à renouvellement unique. Signalement systématique des « choix du cadre ».
Distinction claire entre le registre d'entreprise et le registre officiel MCP, entre suspension et retrait, et entre classe, niveau et palier.

## Questions pour l'audit bibliographique
- p. 164 : le registre officiel MCP est-il toujours « en préversion » au 27 octobre 2026, et sa documentation dit-elle ne pas prendre en charge les serveurs privés et recommander des sous-registres d'entreprise [25, 43]? (Lancement en préversion le 8 septembre 2025 : conforme à ce que je sais.)
- p. 164 : E-23 du BSIF, « en vigueur le 1er mai 2027 », exige-t-elle un inventaire couvrant les modèles des fournisseurs et une cote de risque qui module la gouvernance [8]? Le texte de l'E-23 dit-il « revue indépendante » sur modification (p. 167), ou seulement « critères de modification importante » (EXIG-AUT-05)?
- p. 165 : Microsoft Agent 365 en disponibilité générale le 1er mai 2026, synchronisation avec Bedrock et Google Cloud en préversion publique à cette date [46]; Amazon Bedrock AgentCore Registry (fonctions décrites) [102]; Azure API Center comme registre MCP privé [108]; annonce ServiceNow du 5 mai 2026 (30 intégrations, coupe-circuit) [47].
- p. 166 : Copilot Studio crée-t-il automatiquement une identité Entra Agent ID pour chaque nouvel agent depuis juillet 2026 [48]?
- p. 167 : dans Entra Agent ID, la désactivation d'un « agent identity blueprint » bloque-t-elle toutes les identités dérivées [92]? La recommandation Microsoft « 6 à 12 mois » et « chaque trimestre » est-elle exacte [92]?
- p. 164 et 167 : Feng, McDonald et Zhang (niveaux d'autonomie, « certificat d'autonomie » délivré par un tiers et renouvelé à chaque changement) [83] : conforme à ce que je sais, à confirmer.
- p. 168 : le livre blanc de l'OpenID Foundation recommande-t-il un retrait propagé par SCIM DELETE [311]? Les événements CAEP cités [344] (CAEP 1.0 final du 29 août 2025)?
- p. 169 : politique de cycle de vie MCP (SEP-2596) : douze mois, ou 90 jours en retrait accéléré, « pour un risque de sécurité actif » ou « exceptionnel » [34, 196]? OAuth 2.1 toujours Internet-Draft (draft-16, septembre 2026) [176]? Conventions GenAI d'OpenTelemetry toujours au niveau Development [181, 188]?
- p. 169 : Cadre européen d'interopérabilité sur la gestion du changement [157].
- p. 170 : processus d'admission de l'AAIF (étapes énumérées) [42, 263]; « huit groupes de travail » de l'AAIF [40]; lancement par le CAISI de l'AI Agent Standards Initiative le 17 février 2026 [411]; synthèse du NCCoE du 29 septembre 2026 (« plus de 600 intervenants ») [338], que l'annexe H.5 dit non rouverte; brouillons WIMSE sur la délégation [336].
- p. 165-167 : NIST AI RMF GOVERN 1.6, 1.7, 6.1, 6.2 et MANAGE 2.4 [74] : libellés conformes à ce que je sais; OWASP NHI Top 10, NHI1 = Improper Offboarding [91] : conforme.

audit_17.md : 35 constats (2 BLOQUANT, 14 MAJEUR, 19 MINEUR)
