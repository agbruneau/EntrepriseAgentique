# Audit chunk_16 — pages 151-162

## Synthèse
Le chunk couvre la fin du § 10.3 (recouvrement), le § 10.4 (évaluation en trois paliers, EXIG-EVA-01 à 06), les § 10.5-10.6 (économie de l'inférence, EXIG-FIN-01 à 10), l'intercalaire de la partie IV et les § 11.1-11.2 (rôles, RACI, recouvrement à partir de la p. 161). Le texte est dense, bien sourcé et honnête sur ses choix. Ses règles se tiennent toutefois mal entre elles et avec le reste du cadre. Les trois défauts les plus graves : (1) l'évaluation continue du palier 3 et l'alimentation du jeu de référence exigent le contenu des invites et réponses de production, que l'EXIG-OBS-07 interdit et que l'EXIG-OBS-08 n'autorise que ponctuellement; (2) l'enveloppe budgétaire, appliquée en mode fermé, peut bloquer les compensations qu'elle est censée laisser en « état sûr », et son intégrité comme sa cohérence en concurrence ne sont pas spécifiées; (3) les critères de sélection de modèle (EXIG-FIN-01 et EXIG-FIN-06) divergent et reposent sur des seuils « par étape » qui n'existent nulle part.

## Constats

### [16-01] [BLOQUANT] L'évaluation de production et l'enrichissement du jeu de référence n'ont aucune voie conforme d'accès au contenu
- **Axe** : A
- **Localisation** : § 10.4, EXIG-EVA-04, p. 153 : « L'évaluation en production DOIT porter sur un échantillon aléatoire de 5 à 10 % des traces »; EXIG-EVA-02, p. 153 : « Toute défaillance confirmée en production y ajoute un scénario ». Tableau 42, p. 153 : « Réponses non ancrées sur échantillon ».
- **Diagnostic** : juger l'ancrage factuel ou la justesse d'une réponse (des juges automatisés « hors du chemin critique », plus une revue humaine) exige l'invite, les résultats d'outils et la réponse. Or l'EXIG-OBS-07 (p. 149) interdit ce contenu dans toute la télémétrie de production. L'EXIG-OBS-08 n'admet une capture que « pour un diagnostic », sur décision documentée, pour une « période bornée », avec destruction après 14 jours au plus. Une évaluation continue sur 5 à 10 % des traces n'est pas un diagnostic borné. Le cadre ne définit aucun autre magasin de contenu pour l'évaluation : rétention, droits d'accès, caviardage, finalité au sens de la Loi 25 et EFVP restent muets. Même chose pour reconstituer un scénario à partir d'une défaillance de production (EVA-02), puisque l'entrée fautive n'a pas été conservée.
- **Contre-exemple ou scénario de défaillance** : un agent de classe modérée traite des RP. Pour respecter EVA-04, l'équipe ouvre une capture de contenu permanente « pour diagnostic ». Elle viole alors la borne temporelle et la finalité de l'EXIG-OBS-08. Si elle respecte OBS-07 et OBS-08, le palier 3 ne peut produire que des scores sur métadonnées, et la cible « moins de 0,5 % de réponses non ancrées » devient invérifiable.
- **Correctif proposé** : créer une exigence EXIG-EVA (ou OBS) dédiée à un « dépôt d'évaluation » : contenu caviardé, accès journalisé, rétention bornée (p. ex. 30 à 90 jours), finalité « évaluation de la qualité » déclarée dans l'EFVP, accès réservé aux juges et aux réviseurs habilités, rattachement au span par référence comme dans OBS-08. Ajouter un renvoi croisé dans OBS-07 et OBS-08. Préciser qu'un scénario EVA-02 tiré de la production est reconstitué à partir de ce dépôt, puis anonymisé.
- **Confiance** : déduit (texte des EXIG-OBS-07, OBS-08, EVA-02 et EVA-04 vérifié; l'absence d'un autre magasin de contenu a été vérifiée par recherche dans full.txt).

### [16-02] [MAJEUR] La réévaluation suit le changement de modèle au lieu de le précéder, ce qui contredit l'EXIG-GOV-12
- **Axe** : A
- **Localisation** : EXIG-EVA-01, p. 153 : « Tout changement de modèle, y compris derrière un même alias (EXIG-ARC-09), […] relance les paliers d'évaluation 1 et 2 ».
- **Diagnostic** : l'EVA-01 dit que le changement « relance » les paliers, sans exiger que la relance précède la mise en service. Seuls les tests du palier 1 bloquent un *déploiement* en intégration continue. Or un changement derrière un alias passe par la configuration de la passerelle, pas par un déploiement de l'agent. L'EXIG-ARC-09, à laquelle EVA-01 renvoie, écrit d'ailleurs « suivi d'une réévaluation » (après coup). À l'inverse, l'EXIG-GOV-12 (p. 167) exige la réévaluation « avant leur mise en production ». Le cadre contient donc deux ordres incompatibles, et l'EVA-01 renvoie à celui qui est permissif. Le texte ne traite pas non plus les alias côté fournisseur, comme un « -latest » qui change sans préavis.
- **Contre-exemple ou scénario de défaillance** : l'équipe plateforme repointe l'alias `modele-compact` vers une nouvelle version un vendredi soir. Aucun pipeline CI ne tourne. Le palier 2 se « relance » le lundi; entre-temps, l'agent N3 a servi deux jours sur un modèle non évalué, sans enfreindre la lettre de l'EVA-01.
- **Correctif proposé** : dans l'EVA-01, écrire « … DOIT franchir de nouveau les paliers 1 et 2 **avant** que le changement ne serve en production; la passerelle NE DOIT PAS résoudre un alias vers une cible qui n'a pas franchi ces paliers ». Corriger l'EXIG-ARC-09 dans le même sens et interdire les alias flottants du fournisseur, en exigeant une version épinglée.
- **Confiance** : vérifié dans le texte (EVA-01, ARC-09 l. 1968-1972, GOV-12 l. 10579-10588).

### [16-03] [MINEUR] Quatre listes de déclencheurs de réévaluation qui divergent
- **Axe** : C
- **Localisation** : figure 22, p. 152 : « Tout changement de modèle, d'invite, d'outil ou de version de protocole relance les paliers 1 et 2 »; EXIG-EVA-01, p. 153 (ajoute le « palier d'outil » et l'alias); figure 25 et EXIG-GOV-12, p. 166-167 (ajoutent population visée, ODD, catégorie de données, fournisseur, lieu de traitement).
- **Diagnostic** : une nouvelle population visée ou une nouvelle catégorie de RP déclenche la réévaluation de la classe (GOV-12), mais pas la relance du palier 2 (EVA-01), alors que c'est précisément le jeu de référence qui devrait changer. Aucune liste ne mentionne non plus les changements de corpus de récupération ou de mémoire, ni ceux de la grille ou du modèle du juge (EVA-05).
- **Contre-exemple ou scénario de défaillance** : un agent étendu de la clientèle francophone à toute la clientèle canadienne repasse la revue de classe sans que son jeu de référence soit enrichi ni rejoué.
- **Correctif proposé** : tenir une seule liste normative de déclencheurs, par exemple dans GOV-12, et y renvoyer depuis EVA-01 et les figures 22 et 25. Y ajouter les corpus de récupération, la mémoire et le juge.
- **Confiance** : vérifié dans le texte.

### [16-04] [MAJEUR] Le jeu de référence est borné à 200 scénarios mais croît sans fin
- **Axe** : A
- **Localisation** : EXIG-EVA-02, p. 153 : « Chaque agent DOIT disposer d'un jeu de référence de 50 à 200 scénarios […] Toute défaillance confirmée en production y ajoute un scénario. »
- **Diagnostic** : les deux phrases sont des obligations. La seconde rend le jeu monotone croissant; la première lui impose un maximum. Après un nombre suffisant de défaillances confirmées, l'agent ne peut plus satisfaire les deux à la fois. Rien ne prévoit le retrait, la fusion ou la rotation des scénarios.
- **Contre-exemple ou scénario de défaillance** : un agent part de 190 scénarios et connaît 15 défaillances confirmées en un trimestre. Il atteint 205 scénarios et devient non conforme, ou bien on supprime des cas de régression, ce qui détruit la raison d'être de la règle : « empêche qu'une erreur corrigée revienne ».
- **Correctif proposé** : faire de 50 un minimum et de 200 une taille indicative. Distinguer un « noyau » stable d'un « registre de régression » non plafonné, ou bien prévoir une règle de consolidation versionnée qui conserve au moins un scénario par mode de défaillance.
- **Confiance** : vérifié dans le texte.

### [16-05] [MAJEUR] Les seuils chiffrés n'ont pas la puissance statistique pour être vérifiés
- **Axe** : B
- **Localisation** : EXIG-EVA-03, p. 153 : « Chaque scénario DOIT s'exécuter au moins trois fois […] on retient le taux de réussite et sa dispersion »; tableau 42 : « Moins de 0,5 % de réponses non ancrées »; EXIG-EVA-04 (échantillon de 5 à 10 %, « et sur toutes les traces marquées »).
- **Diagnostic** : (a) En préproduction, 50 scénarios exécutés 3 fois donnent 150 exécutions corrélées. Une seule faute vaut alors 0,67 %. Pour montrer un taux inférieur à 0,5 % à 95 % de confiance sans aucune faute, la « règle de trois » demande environ 600 essais indépendants. (b) Une dispersion estimée sur 3 répétitions est très instable. (c) En production, l'échantillon mêle un tirage aléatoire et 100 % des traces atypiques. Un taux brut calculé « sur échantillon » est donc biaisé vers le haut, faute de pondération par strate. (d) Pour un agent à faible volume, comme un agent ambiant mensuel, 5 % donnent un échantillon quasi nul. Le cadre fixe des seuils DOIT et un blocage de mise en production (EVA-02) sans règle de décision statistique.
- **Contre-exemple ou scénario de défaillance** : un agent traite 400 tâches par mois. L'échantillon aléatoire compte 20 traces, auxquelles s'ajoutent 30 traces en erreur. Deux réponses non ancrées parmi ces 50 donnent 4 %, ce qui déclenche à tort l'EVA-06. Inversement, zéro faute sur 20 ne prouve rien sous 0,5 %.
- **Correctif proposé** : exiger que les seuils s'expriment avec un intervalle de confiance, par exemple une borne supérieure à 95 %. Calculer les taux de production sur la seule strate aléatoire, ou par pondération inverse. Fixer une taille minimale absolue d'échantillon, p. ex. max(5 %, n_min). Prévoir le cas des agents à faible volume, avec une agrégation sur plusieurs périodes. Envisager un indicateur pass^k plutôt qu'une moyenne sur 3 essais.
- **Confiance** : déduit (arithmétique vérifiée).

### [16-06] [MINEUR] Un DOIT « de 5 à 10 % » interdit d'échantillonner davantage
- **Axe** : A
- **Localisation** : EXIG-EVA-04, p. 153 : « DOIT porter sur un échantillon aléatoire de 5 à 10 % des traces ».
- **Diagnostic** : la borne supérieure est normative. Un agent de classe élevée évalué à 100 %, ou à 20 %, serait non conforme. La règle ne dit pas non plus si le pourcentage porte sur les traces conservées ou sur les exécutions. Si le traçage est lui-même échantillonné à la tête (head sampling), 5 % des traces conservées peuvent ne représenter que 0,5 % des exécutions. Enfin, « toutes les traces marquées d'une erreur » suppose un échantillonnage de queue (tail sampling) qui conserve toutes les erreurs, ce que le chunk n'exige pas.
- **Correctif proposé** : écrire « au moins 5 % des exécutions (10 % recommandé; davantage pour la classe élevée) » et exiger que l'échantillonnage du traçage conserve toutes les traces marquées.
- **Confiance** : vérifié dans le texte (portée de l'échantillonnage des traces : déduit).

### [16-07] [MINEUR] L'exigence et sa justification divergent sur le rattachement de l'événement d'évaluation
- **Axe** : C
- **Localisation** : EXIG-EVA-04, p. 153 : « chaque résultat est consigné par un événement gen_ai.evaluation.result rattaché au span évalué » contre « Pourquoi : […] rattachement au span évalué ou, à défaut, par gen_ai.response.id »; p. 152 : « et devrait être rattaché au span évalué ».
- **Diagnostic** : le corps impose le rattachement au span; le « Pourquoi » admet un repli par `gen_ai.response.id`; le texte de la p. 152 le présente comme un « devrait ». Un auditeur ne sait pas si le repli est conforme.
- **Correctif proposé** : intégrer le repli au corps de l'exigence (« rattaché au span évalué ou, à défaut, corrélé par gen_ai.response.id ») ou le retirer du « Pourquoi ».
- **Confiance** : vérifié dans le texte.

### [16-08] [MINEUR] La figure 22 omet le « plafond atteint » parmi les traces évaluées à 100 %
- **Axe** : C
- **Localisation** : figure 22, p. 152 : « 100 % des traces en erreur, relance ou refus d'approbation », contre texte p. 152 et EXIG-EVA-04, p. 153 : « d'une erreur, d'une relance, d'un plafond atteint ou d'un refus d'approbation ».
- **Diagnostic** : la figure, qui sert de résumé, omet une catégorie normative. Le constat est à la couture : figure en p. 152, exigence en p. 153.
- **Correctif proposé** : ajouter « plafond atteint » à la figure 22.
- **Confiance** : vérifié dans le texte.

### [16-09] [MAJEUR] Un juge « distinct du modèle **ou** de l'invite » peut être le même modèle
- **Axe** : A
- **Localisation** : EXIG-EVA-05, p. 153 : « Un juge à base de modèle DOIT être distinct du modèle ou de l'invite qu'il évalue ».
- **Diagnostic** : la disjonction est satisfaite par le même modèle muni d'une autre invite. Or la justification même de l'exigence, « un juge partage les faiblesses des modèles qu'il évalue », vise ce cas. Le biais d'auto-préférence d'un juge envers ses propres sorties est un phénomène connu.
- **Contre-exemple ou scénario de défaillance** : l'agent et son juge tournent sur `modele-compact`, avec deux invites différentes. Le juge partage les hallucinations de l'agent, mesure un ancrage excellent, et la cible du tableau 42 est « atteinte ».
- **Correctif proposé** : écrire « distinct du modèle évalué (autre famille ou autre fournisseur de préférence) **et** de son invite ». À défaut, exiger que l'accord avec les évaluations humaines soit mesuré spécifiquement dans la configuration « même modèle ».
- **Confiance** : vérifié dans le texte (biais d'auto-préférence : connaissance générale, à vérifier par l'audit bibliographique si on veut le citer).

### [16-10] [MINEUR] La calibration du juge n'a pas de critère d'échec
- **Axe** : B
- **Localisation** : EXIG-EVA-05, p. 153 : « être calibré contre des évaluations humaines, avec un taux d'accord revu chaque trimestre ».
- **Diagnostic** : on « revoit » le taux d'accord, mais aucun seuil minimal, aucune mesure (accord brut, kappa) et aucune conséquence ne sont fixés. L'exigence n'est donc pas vérifiable en revue : n'importe quel taux est conforme.
- **Correctif proposé** : fixer au contrat un seuil d'accord minimal, p. ex. kappa de Cohen ≥ 0,6, avec une taille d'échantillon humaine. Prévoir qu'un juge sous ce seuil ne peut plus alimenter les indicateurs de l'EVA-06.
- **Confiance** : vérifié dans le texte.

### [16-11] [MAJEUR] La réaction aux écarts est confiée aux intéressés, sur une période non définie
- **Axe** : B
- **Localisation** : EXIG-EVA-06, p. 154 : « Un objectif manqué pendant deux périodes consécutives (choix du cadre) déclenche une revue par le parrain et le responsable technique, qui corrigent, réduisent le niveau d'autonomie ou suspendent l'agent ».
- **Diagnostic** : (a) La « période » n'est définie nulle part (jour, semaine, mois?). La règle n'est donc ni testable ni comparable d'un agent à l'autre. (b) Les deux seuls réviseurs sont ceux qui ont intérêt à maintenir l'agent. La p. 162 pose pourtant le principe inverse pour la classe de risque : « celui qui souhaite déployer l'agent propose la classe, une fonction indépendante la tranche ». (c) Pour un agent de classe élevée ou N4, la règle de la p. 162 fait du comité le « A » du niveau d'autonomie, alors qu'ici le parrain et le responsable technique décident seuls. Le comité n'est même pas informé. (d) L'option « corrigent » ne prévoit ni délai ni escalade si l'écart persiste.
- **Contre-exemple ou scénario de défaillance** : un agent de classe élevée manque sa cible d'ancrage pendant six mois. À chaque revue, le parrain et le responsable technique « corrigent » l'invite. Aucune fonction indépendante n'est saisie et le comité n'en sait rien.
- **Correctif proposé** : définir la période, par exemple le mois civil, ou la renvoyer au contrat de manière obligatoire. Ajouter la fonction risques et conformité comme « C », et le comité comme « A » pour la classe élevée ou N4. Après N périodes sans retour sous la cible, imposer la réduction d'autonomie et l'escalade au comité.
- **Confiance** : vérifié dans le texte (couture p. 154 / p. 162).

### [16-12] [MINEUR] Deux déclencheurs pour le même écart économique, et une « revue de valeur » introuvable
- **Axe** : C
- **Localisation** : EXIG-FIN-10, p. 158 : « dépasse celui du processus de référence deux mois de suite (choix du cadre) passe en revue de valeur (section 11.5) »; EXIG-EVA-06, p. 154 (même famille « Économie unitaire », « deux périodes consécutives »).
- **Diagnostic** : le même dépassement déclenche deux procédures : une revue par le parrain et le responsable technique (EVA-06) et une « revue de valeur » (FIN-10), avec des périodes qui peuvent différer. Le terme « revue de valeur » n'apparaît qu'en FIN-10. Le § 11.5 (p. 166-168) ne le définit pas : il traite des points de contrôle, de la réévaluation et de l'attestation. Le renvoi est donc mal ciblé.
- **Correctif proposé** : fusionner les deux déclencheurs, l'EVA-06 renvoyant à l'EXIG-FIN-10 pour l'économie unitaire. Définir la revue de valeur, avec ses participants, ses issues possibles et sa consignation, dans le § 11.5, ou corriger le renvoi.
- **Confiance** : vérifié dans le texte (recherche de « revue de valeur » dans full.txt : une seule occurrence).

### [16-13] [MINEUR] Les cibles du tableau 42 sont ambiguës
- **Axe** : C
- **Localisation** : tableau 42, p. 152-153 : « Coût moyen et au 99e centile par tâche réussie […] Sous le coût du processus de référence sans agent »; « Plus de 99,5 % de succès »; « approbations sans modification (section 8.7) »; « aucune violation d'un garde-fou bloquant ».
- **Diagnostic** : (a) Le tableau ne dit pas si la cible économique porte sur la moyenne ou sur le 99e centile. Si elle porte sur le 99e centile, elle est presque toujours manquée; si elle porte sur la moyenne, le 99e centile n'a pas de cible. (b) « Succès » d'un appel MCP ou A2A : un refus typé de la passerelle (EXIG-IAM-18), ou une tâche A2A à l'état `rejected`, est-il un échec? Si oui, durcir les politiques dégrade l'objectif de niveau de service. (c) L'indicateur « approbations sans modification » n'a pas de cible, alors que l'EVA-06 exige des objectifs pour chaque famille; le § 8.7 (l. 7347) emploie un écart à la médiane fixé par le comité. (d) Un garde-fou « bloquant » ne peut, par définition, être « violé » que s'il a échoué : il faut dire si l'on compte les tentatives bloquées ou les contournements. (e) Le « processus de référence » n'existe pas pour une capacité nouvelle; le § 15 le reconnaît comme un risque (l. 13438), sans règle de repli ici.
- **Correctif proposé** : préciser la statistique visée pour chaque cible. Exclure explicitement les refus de politique du taux d'échec technique. Renvoyer au seuil du § 8.7 pour les approbations. Définir « violation ». Prévoir une cible de remplacement (valeur attendue à la fiche) faute de processus de référence.
- **Confiance** : vérifié dans le texte.

### [16-14] [MAJEUR] Un même nom, « coût par tâche réussie », pour deux mesures différentes
- **Axe** : B
- **Localisation** : EXIG-FIN-01, p. 155 : « DOIT reposer sur le coût par tâche réussie mesuré sur le jeu de référence (section 10.4) »; définition, p. 158 : « coût total imputé à l'agent (inférence, outils, quote-part de la plateforme) divisé par le nombre de tâches réussies selon son contrat ».
- **Diagnostic** : sur le jeu de référence, les outils à effet sont des doublures (EVA-03). Le coût réel des outils (API facturées, crédits SaaS par action) et la quote-part de la plateforme en sont absents. La composition du jeu, chargée de cas limites et de tentatives d'injection, n'est pas représentative de la charge de production : le coût moyen par tâche y est biaisé. La définition de la p. 158 est, elle, une mesure comptable de production. Le choix d'un modèle ou d'une plateforme repose donc sur un indicateur qui n'est pas celui qu'on suit ensuite (FIN-10).
- **Contre-exemple ou scénario de défaillance** : la plateforme A gagne sur le jeu de référence, où les outils sont gratuits. En production, elle consomme deux fois plus d'actions SaaS facturées que la plateforme B, et son coût réel par tâche est supérieur.
- **Correctif proposé** : distinguer un « coût d'inférence par tâche réussie (jeu de référence, pondéré par la distribution de production) » pour la sélection, et un « coût total par tâche réussie (production) » pour le suivi. Exiger d'ajouter le coût estimé des outils réels au premier.
- **Confiance** : vérifié dans le texte.

### [16-15] [MAJEUR] Le périmètre de coût exclut le travail humain, ce qui biaise la comparaison avec le processus sans agent
- **Axe** : B
- **Localisation** : p. 158 : « coût total imputé à l'agent (inférence, outils, quote-part de la plateforme) »; EXIG-FIN-01, p. 155 : « pour un modèle hébergé par l'entreprise, l'hébergement, l'exploitation et l'évaluation ».
- **Diagnostic** : le processus de référence est, par construction, du travail humain. Le coût de l'agent omet le temps des approbateurs (N2 et approbations P3), la revue humaine du palier 3, l'équipe de garde, et le coût des évaluations et des juges (palier 3) pour un modèle non hébergé. La comparaison prescrite (tableau 42, FIN-10) favorise donc systématiquement l'agent. Les périmètres divergent en outre entre FIN-01, qui inclut l'évaluation pour un modèle hébergé seulement, et la définition de la p. 158, qui ne la mentionne pas.
- **Contre-exemple ou scénario de défaillance** : un agent N2 coûte 0,40 $ d'inférence par tâche, mais chaque tâche exige 4 minutes d'un approbateur à 60 $/h, soit 4 $. Il est déclaré « sous le coût du processus de référence » (3 $) alors qu'il coûte 4,40 $.
- **Correctif proposé** : définir un seul périmètre complet : inférence, outils, plateforme, évaluation (juges et revue humaine), temps d'approbation et de garde imputé. Appliquer ce périmètre dans FIN-01, FIN-10 et le tableau 42.
- **Confiance** : déduit.

### [16-16] [MINEUR] La normalisation des segmenteurs est exigée là où elle est inutile et omise là où elle compte
- **Axe** : A
- **Localisation** : EXIG-FIN-01, p. 155 : « la normalisation des jetons d'un segmenteur à l'autre »; p. 158 : « Ratio jetons/résultat : […] sa hausse à qualité égale signale une dérive ».
- **Diagnostic** : un coût par tâche exprimé en dollars ne dépend pas du segmenteur : la différence de comptage est déjà dans la facture. La normalisation est en revanche indispensable au ratio jetons/résultat. Un passage à un segmenteur qui produit « environ 30 % plus de jetons » (p. 154) fait monter ce ratio sans aucune dérive, ce qui produit une fausse alerte.
- **Correctif proposé** : déplacer l'obligation de normalisation vers le ratio jetons/résultat et les prévisions budgétaires (FIN-02). Réinitialiser la ligne de base du ratio à chaque changement de modèle.
- **Confiance** : déduit.

### [16-17] [MAJEUR] « Plus petit modèle suffisant » : des seuils par étape qui n'existent pas, et un critère qui contredit l'EXIG-FIN-01
- **Axe** : A
- **Localisation** : EXIG-FIN-06, p. 157 : « Chaque étape d'un agent DOIT être servie par le plus petit modèle homologué qui atteint, pour cette étape, les seuils du jeu de référence. »
- **Diagnostic** : (a) L'EVA-02 place au contrat des seuils *par agent* (trajectoire, ancrage, garde-fous); aucun seuil *par étape* n'est défini. L'exigence est donc inapplicable telle quelle. (b) « Plus petit » n'a pas d'ordre défini : le nombre de paramètres des modèles propriétaires n'est pas publié, et « plus petit » ne veut pas forcément dire « moins cher ». (c) Les étapes ne sont pas indépendantes. Un modèle moins capable à l'étape 2 modifie les entrées de l'étape 3, si bien que l'optimum étape par étape n'atteint pas forcément le seuil global. (d) L'EXIG-FIN-01 retient le coût *par tâche réussie* : un plus petit modèle, plus souvent en échec ou en relance, peut coûter plus cher par tâche réussie. Les deux DOIT peuvent désigner des modèles différents. (e) Le coût d'évaluation est combinatoire : m modèles × s étapes × jusqu'à 200 scénarios × 3 essais.
- **Contre-exemple ou scénario de défaillance** : à l'étape « extraction », le modèle compact atteint 92 % et le modèle moyen 97 %. Le compact « atteint le seuil » fixé à 90 % et l'EXIG-FIN-06 l'impose. Les 5 points d'erreurs se propagent : le taux de succès global tombe sous le seuil d'agent, et le coût par tâche réussie dépasse celui du modèle moyen.
- **Correctif proposé** : remplacer par « la configuration modèle-par-étape retenue DOIT atteindre les seuils d'agent du jeu de référence au plus faible coût par tâche réussie (EXIG-FIN-01) mesuré ». Le modèle de raisonnement reste justifié par une mesure. Définir l'ordre de comparaison par le coût, pas par la taille.
- **Confiance** : vérifié dans le texte (conséquences : déduit).

### [16-18] [MINEUR] Prix interdits dans les exigences mais nécessaires à leur application; devise non traitée
- **Axe** : C
- **Localisation** : EXIG-FIN-02, p. 155 : « Les exigences et les contrats d'agent NE DOIVENT PAS inscrire le prix d'un modèle »; EXIG-FIN-06, Pourquoi, p. 157 : « l'écart de prix atteint un facteur 100 […] facteur 20 au-delà »; figure 23 : « 0,52 $ / 0,75 $ ».
- **Diagnostic** : (a) Le « Pourquoi » d'une exigence inscrit justement un rapport de prix daté, qui sera périmé à la prochaine révision des grilles, le risque que FIN-02 veut éviter. (b) Pour décrémenter l'enveloppe en coût (FIN-04), la passerelle a besoin d'une table de prix. Le cadre ne dit pas où elle vit, qui la tient ni comment elle se date. (c) Les grilles sont en $ US; l'enveloppe et les indicateurs sont en $ CA (p. 158, C.7 `max_cost_cad`). Ni la source ni la date du taux de change ne sont fixées. (d) « contrats d'agent » contre « fiches » : la distinction n'est pas claire (la fiche « renvoie aux grilles »), pas plus que « révisées chaque trimestre avec le catalogue » (lequel?).
- **Correctif proposé** : retirer le chiffre du « Pourquoi » de FIN-06 ou le marquer « illustratif, daté d'octobre 2026 ». Exiger une table de prix versionnée et datée à la passerelle de modèles, révisée en même temps que les hypothèses de FIN-02, avec une règle de conversion en $ CA. Nommer le catalogue visé.
- **Confiance** : vérifié dans le texte.

### [16-19] [MAJEUR] L'enveloppe, présentée comme une « borne logique », n'est spécifiée ni en cohérence, ni en concurrence, ni en intégrité
- **Axe** : A
- **Localisation** : § 10.6, p. 156 : « Un quota de passerelle est donc une borne approximative; l'enveloppe, une borne logique. »; EXIG-FIN-04 : « La passerelle de modèles et l'orchestrateur DOIVENT décrémenter l'enveloppe à chaque appel ».
- **Diagnostic** : (a) Il y a deux décrémenteurs, la passerelle et l'orchestrateur, sans autorité désignée : double comptage ou divergence des compteurs. (b) Le coût d'un appel de modèle n'est connu qu'après la réponse. Sans réservation préalable (`max_tokens` ≤ reste), un appel peut dépasser 100 %. (c) Des sous-agents ou des appels d'outils parallèles qui décrémentent le même reste ont exactement la course que le texte reproche au quota APIM. Le partage « une part de l'enveloppe restante » n'est sûr que si la part est *réservée* (débitée du parent à l'attribution), ce qui n'est pas dit. (d) Les « plafonds restants » voyagent dans l'appel (EXIG-ARC-02); C.7 les montre en clair et sans signature. Un agent compromis ou bogué peut annoncer un reste neuf à l'aval. (e) Une délégation A2A à un partenaire externe n'honore pas l'enveloppe. (f) « Chaque demande reçoit à son entrée une enveloppe » : un agent ambiant déclenché par événement n'a pas de demande.
- **Contre-exemple ou scénario de défaillance** : un orchestrateur lance 4 sous-agents en parallèle, chacun avec « une part de l'enveloppe restante » calculée sur le même reste de 10 000 jetons. Chacun reçoit 10 000 jetons, soit 40 000 consommables pour une borne déclarée à 10 000.
- **Correctif proposé** : faire de la passerelle de modèles le seul détenteur de l'état de l'enveloppe, côté serveur et indexé par `task_id`. Imposer la réservation atomique (débit au moment de l'attribution d'une part et avant chaque appel, à hauteur du maximum possible, puis ajustement). Faire transporter dans les appels une référence d'enveloppe intègre plutôt que des montants. Traiter le partenaire externe par plafond contractuel, et définir l'unité « demande » pour les agents ambiants (événement déclencheur).
- **Confiance** : déduit (absence de spécification vérifiée par recherche sur « enveloppe » dans full.txt).

### [16-20] [MAJEUR] Un budget épuisé, appliqué en mode fermé, peut bloquer les compensations
- **Axe** : A
- **Localisation** : EXIG-FIN-04, p. 156 : « à 100 %, arrêter l'exécution en état sûr et la passer en escalade, avec un refus typé « budget épuisé » (EXIG-IAM-18) ».
- **Diagnostic** : l'enveloppe se décrémente « à chaque appel de modèle et d'outil » et la passerelle refuse en mode fermé (IAM-18). Une saga arrêtée en cours de route doit compenser les étapes déjà réalisées, et chaque compensation est un appel d'outil, parfois précédé d'un appel de modèle. Rien n'exempte les compensations de l'enveloppe ni ne leur réserve de budget. L'« état sûr » requis par FIN-04 et ORC-26 peut donc être inatteignable, en contradiction avec PRIN-05 (réversibilité) et PRIN-12. La recherche de « compensation » associée à « plafond » ou « budget » dans full.txt ne donne rien.
- **Contre-exemple ou scénario de défaillance** : une saga de 5 étapes réserve un stock à l'étape 1, crée un bon de commande à l'étape 2, puis épuise son budget de jetons à l'étape 3. La passerelle refuse « budget épuisé » à l'appel `annuler_reservation`. La saga reste à moitié exécutée, exactement ce que la p. 12 (l. 1538) déclare inacceptable.
- **Correctif proposé** : exiger une réserve de compensation, calculée à la conception, que l'arrêt à 100 % ne consomme pas. À défaut, déclarer les compensations hors enveloppe, exécutées par le moteur d'exécution durable sous un plafond distinct et journalisées. Ajouter un test d'injection de fautes « épuisement du budget en cours de saga » au palier 1 (EXIG-ORC-20).
- **Confiance** : déduit (textes de FIN-04, IAM-18 et ORC-26 vérifiés).

### [16-21] [MAJEUR] La suspension au plafond mensuel ignore les exécutions en cours, et le modèle de repli n'est pas borné
- **Axe** : B
- **Localisation** : EXIG-FIN-05, p. 156 : « À son plafond mensuel, l'agent est suspendu ou ramené à son modèle de repli, selon sa fiche, et le parrain en est avisé. »; EXIG-FIN-03, p. 155 : « Un dépassement qui désactive des agents DOIT être traité comme un risque de continuité ».
- **Diagnostic** : (a) Le cadre traite comme un risque de continuité la désactivation imposée par un éditeur SaaS, à 125 % de la capacité prépayée de Copilot Studio. Il s'impose pourtant la même coupure en interne, sans le même traitement : aucun seuil d'alerte mensuel (l'alerte à 80 % de FIN-04 vise l'enveloppe d'une tâche) et aucun sort défini pour les sagas en vol. (b) « Ramené à son modèle de repli » : le repli consomme encore, sans plafond déclaré, si bien que le plafond mensuel n'en est plus un. (c) Le parrain n'est avisé qu'au plafond, pas avant.
- **Contre-exemple ou scénario de défaillance** : le 28 du mois, un agent de rapprochement atteint son plafond au milieu de 300 sagas ouvertes. Si la suspension est immédiate, ces sagas sont abandonnées sans compensation. Si l'agent passe au repli, la consommation continue sans limite jusqu'au 1er.
- **Correctif proposé** : alerter à 80 % du plafond mensuel; à 100 %, refuser les nouvelles tâches mais laisser terminer ou compenser les tâches en vol sous la réserve de [16-20]; fixer un plafond propre au repli; appliquer à FIN-05 le traitement de continuité de FIN-03.
- **Confiance** : vérifié dans le texte (conséquences : déduit).

### [16-22] [MINEUR] « Taux de succès » contre « taux de lecture » du cache, et une « baisse marquée » non définie
- **Axe** : C
- **Localisation** : p. 157 : « Le taux de succès du cache se lit en rapportant gen_ai.usage.cache_read.input_tokens à gen_ai.usage.input_tokens »; EXIG-FIN-07 : « Le taux de lecture en cache est suivi par agent, et une baisse marquée ouvre une analyse. »
- **Diagnostic** : le rapport décrit la part des jetons d'entrée servis depuis le cache, pas un taux de succès (hit rate) par requête; le texte emploie deux noms pour le même indicateur. « Baisse marquée » n'a pas de seuil : l'exigence n'est pas vérifiable. Comme le note le texte, le dénominateur varie selon le fournisseur, donc une comparaison inter-fournisseurs du taux est trompeuse sans normalisation.
- **Correctif proposé** : nommer un seul indicateur (« part des jetons d'entrée lus en cache »), donner la formule par fournisseur, et fixer un seuil relatif, p. ex. une baisse de plus de 20 points sur 7 jours.
- **Confiance** : vérifié dans le texte.

### [16-23] [MINEUR] « Jamais à la volée » contre le chargement d'outils à la demande et `list_changed`
- **Axe** : C
- **Localisation** : EXIG-FIN-07, p. 157 : « Une définition d'outil ou une invite système DOIT se modifier par une version déployée, jamais à la volée. »; p. 157 : « un outil chargé à la demande s'ajoute après le point de rupture du cache ».
- **Diagnostic** : le chargement à la demande modifie l'ensemble d'outils au cours d'une session, et un serveur MCP tiers peut changer ses définitions et l'annoncer par notification. L'exigence ne distingue pas « modifier une définition » (interdit) et « ajouter dynamiquement une définition déjà versionnée » (permis). Elle ne dit pas non plus comment la passerelle traite une définition tierce changée à chaud.
- **Correctif proposé** : préciser que l'ajout d'outils versionnés au catalogue est permis en fin de préfixe, et qu'une modification de définition reçue à l'exécution est refusée par la passerelle ou traitée comme un nouveau déploiement (renvoi aux exigences MCP de catalogue et d'instantané).
- **Confiance** : vérifié dans le texte (comportement MCP : d'après mes connaissances de la spécification).

### [16-24] [MAJEUR] L'imputation suppose un centre de coûts unique par span et des factures plus fines qu'elles ne le sont
- **Axe** : B
- **Localisation** : EXIG-FIN-09, p. 158 : « Chaque span DOIT porter le centre de coûts imputé (ca.entreprise.cost_center), tiré du référentiel financier et identique à l'étiquette des données de facturation. »
- **Diagnostic** : (a) Un span de la passerelle, d'un serveur MCP partagé ou d'un agent d'un autre domaine appelé par A2A sert plusieurs centres de coûts. Le texte cite lui-même la FinOps Foundation sur « l'absence de cadres généralement admis pour répartir les coûts entre charges multiagents », mais impose une valeur unique sans règle : celle du demandeur, celle du propriétaire ou une clé de répartition? (b) Les données FOCUS des fournisseurs d'inférence sont agrégées par compte, espace de travail ou clé, pas par requête. L'« étiquette » n'est identique à celle des spans que si l'entreprise crée une clé ou un espace par centre de coûts, ce que l'exigence ne dit pas. La « jointure » n'est alors possible qu'au niveau agrégé.
- **Contre-exemple ou scénario de défaillance** : l'agent conformité du domaine B, appelé par 6 domaines, porte le centre de coûts de B. Toute sa dépense est imputée à B, et le coût par tâche réussie des 6 agents appelants est sous-estimé.
- **Correctif proposé** : définir la règle : le centre de coûts du mandant ou de la tâche d'origine se propage (bagage, OBS-10), et le service appelé ne le remplace pas. Pour les services partagés, prévoir une clé de répartition déclarée. Exiger une clé ou un espace de travail fournisseur par centre de coûts, ou une répartition par télémétrie, pour rendre la jointure possible.
- **Confiance** : déduit (granularité des données FOCUS des fournisseurs : à vérifier par l'audit bibliographique).

### [16-25] [MAJEUR] L'équipe FinOps porte des DOIT mais n'existe ni au tableau 43 ni à la RACI
- **Axe** : C
- **Localisation** : EXIG-FIN-03, p. 155 : « l'équipe FinOps DOIT tenir une table de conversion »; EXIG-FIN-10, p. 158 : « L'équipe FinOps DOIT calculer chaque mois »; tableau 43, p. 160-161 (rôles) et tableau 44, p. 162 (aucune colonne ni activité FinOps). EXIG-FIN-09 : « sur décision du comité ».
- **Diagnostic** : un rôle titulaire d'obligations normatives est absent de la liste des rôles. Aucune activité de coût (fixer le plafond mensuel, tenir la table de conversion, décider du passage à la refacturation réelle, conduire la revue de valeur) n'a de « A » dans la matrice, ce qui prive l'EXIG-GOV-04 (« un et un seul rôle A ») de prise sur toute la chaîne de maîtrise des coûts. Le mandat du comité (tableau 43, justification de GOV-02) ne comprend pas non plus la décision de refacturation que l'EXIG-FIN-09 lui confie.
- **Correctif proposé** : ajouter « Équipe FinOps » au tableau 43 et une colonne FIN au tableau 44, avec au moins les activités « Fixer quotas et plafond mensuel », « Calculer et publier l'économie unitaire » et « Conduire la revue de valeur ». Ajouter la décision de refacturation au mandat du comité.
- **Confiance** : vérifié dans le texte.

### [16-26] [MAJEUR] Le parrain demande lui-même le niveau d'autonomie et l'homologation qu'il approuve
- **Axe** : A
- **Localisation** : tableau 43, p. 160 : « Propriétaire métier (parrain) […] demande son niveau d'autonomie »; tableau 44, p. 162 : « Fixer le niveau d'autonomie » (A = PM) et « Homologuer la mise en production » (A = PM); EXIG-GOV-03, p. 161 : « Une même personne NE DOIT PAS à la fois préparer et approuver une décision du cycle de vie ».
- **Diagnostic** : pour les classes faible et modérée, la même personne demande le niveau d'autonomie (tableau 43) puis l'approuve (tableau 44). Elle approuve aussi l'homologation d'un agent dont elle porte la demande et le financement. L'EXIG-GOV-03 n'est appliquée qu'au responsable technique, alors que sa formulation générale couvre aussi le parrain. Le cadre applique ailleurs l'argument d'indépendance (« celui qui souhaite déployer l'agent propose la classe, une fonction indépendante la tranche », p. 162), mais pas ici. Le plafond par classe (EXIG-CON-02) limite le risque, sans supprimer l'autocontrôle jusqu'à N3.
- **Contre-exemple ou scénario de défaillance** : un parrain de classe modérée demande N3, l'approuve comme « A », puis homologue lui-même la mise en production. Aucune fonction indépendante n'a dit oui.
- **Correctif proposé** : faire de la fonction risques et conformité, ou de l'architecture d'entreprise, le « A » pour le niveau d'autonomie et l'homologation des classes faible et modérée; le parrain reste « R » (il demande). À défaut, reformuler GOV-03 pour en limiter explicitement la portée.
- **Confiance** : vérifié dans le texte (couture p. 160 / p. 161-162; le reste du tableau 44 relève du chunk 17).

### [16-27] [MINEUR] « Propriétaire » désigne deux rôles différents
- **Axe** : C
- **Localisation** : EXIG-FIN-04, p. 156 : « alerter le propriétaire dès qu'un plafond atteint 80 % »; figure 23 : « 80 % : alerte au propriétaire »; p. 160 : « le propriétaire métier joue le rôle de parrain, le responsable technique celui de propriétaire au sens d'Entra ».
- **Diagnostic** : après la p. 160, « propriétaire » seul peut désigner le propriétaire métier (le parrain) ou le responsable technique (le propriétaire au sens d'Entra). Le destinataire de l'alerte FIN-04 est donc indéterminé. FIN-05 et FIN-10 disent, eux, « parrain ».
- **Correctif proposé** : remplacer « propriétaire » par « responsable technique » ou « parrain » dans FIN-04, la figure 23 et C.7 (`"notified": "proprietaire"`), et proscrire « propriétaire » seul dans le cadre.
- **Confiance** : vérifié dans le texte.

### [16-28] [MINEUR] Le « facteur 20 au-delà » suppose un prix constant de Fable 5.1 au-delà de 100 000 jetons
- **Axe** : C
- **Localisation** : p. 154 : « au-delà, 0,50 $ US en entrée et 2,50 $ US en sortie […] contre 10 $ US et 50 $ US pour Claude Fable 5.1 »; EXIG-FIN-06 : « facteur 20 au-delà ».
- **Diagnostic** : l'arithmétique est juste (10/0,50 = 50/2,50 = 20) seulement si Fable 5.1 n'a pas de majoration pour contexte long. Le texte ne le dit pas.
- **Correctif proposé** : préciser « Fable 5.1 sans majoration au-delà de 100 000 jetons, selon la grille d'octobre 2026 », ou corriger le facteur.
- **Confiance** : à vérifier (source externe [399]).

### [16-29] [MINEUR] « Résidence canadienne » contredit la lecture que le cadre fait de l'art. 17
- **Axe** : C
- **Localisation** : p. 154 : « la zone « us » de l'API d'Anthropic n'est pas une résidence canadienne, et aucune zone canadienne n'y est offerte ».
- **Diagnostic** : le cadre interprète l'art. 17 de la Loi sur le privé comme visant toute communication hors du Québec, « autres provinces comprises » (l. 12266, 15871). Présenter la résidence canadienne comme le critère pertinent laisse croire qu'une zone canadienne dispenserait de l'EFVP de l'art. 17, ce que le cadre lui-même exclut.
- **Correctif proposé** : écrire « … n'est ni une résidence québécoise ni canadienne; toute zone hors du Québec relève de l'art. 17 (section 12.2) ».
- **Confiance** : vérifié dans le texte.

### [16-30] [MINEUR] Le régime public est cité sans son pendant au RPRP ni le comité obligatoire
- **Axe** : A
- **Localisation** : p. 160 : « Les organismes publics appliquent les dispositions équivalentes de la Loi sur l'accès, notamment les articles 63.3 (règles de gouvernance) et 63.5 (EFVP) ».
- **Diagnostic** : d'après mes connaissances, la Loi sur l'accès confie la fonction de responsable à la personne ayant la plus haute autorité (art. 8) et impose aux organismes publics un comité sur l'accès à l'information et la protection des RP (art. 8.1). Ce comité est un acteur de gouvernance absent des tableaux 43 et 44. Pour un organisme public, la RACI est donc incomplète.
- **Correctif proposé** : citer les art. 8 et 8.1, et ajouter « comité AIPRP (organismes publics) » comme « C » des activités EFVP et incidents.
- **Confiance** : à vérifier (source externe : texte consolidé de la Loi sur l'accès, art. 8 et 8.1).

### [16-31] [MINEUR] Les dimensions de l'enveloppe dérivent entre le § 10.6, l'EXIG-ORC-26 et C.7
- **Axe** : C
- **Localisation** : p. 156 : « une enveloppe de jetons, de coût, d'appels d'outils et de délai »; EXIG-ORC-26 : « étapes ou itérations, appels d'outils, jetons, coût et durée totale »; C.7 : `max_iterations`, `timeout_s`, `max_wall_clock_s`, « Chaque étape incrémente consumed ».
- **Diagnostic** : le § 10.6 et la figure 23 omettent les itérations. Leur « Délai » (38 s / 60 s) correspond au temps actif (`timeout_s`) et non à la « durée totale » d'ORC-26 (`max_wall_clock_s`, 28 800 s). Le § 10.6 parle de « décrémenter » l'enveloppe, C.7 d'« incrémenter consumed ». Sans gravité, mais un implémenteur ne sait pas quelle liste est normative.
- **Correctif proposé** : aligner la figure 23 et le § 10.6 sur la liste d'ORC-26 (cinq dimensions, en distinguant temps actif et durée totale), et unifier le vocabulaire (reste ou consommé).
- **Confiance** : vérifié dans le texte.

## Points forts
Datation et réserves systématiques des chiffres de fournisseurs (édition de l'AI Index non revérifiée, segmenteur, persistance incertaine des baisses), et refus explicite des pourcentages d'économie sans source. Bonne séparation entre ce que la source établit et le « choix du cadre ». Le juge qui « mesure, il ne gouverne pas » (EVA-05) et l'enveloppe non recréée à la délégation (FIN-04) sont des choix sains.

## Questions pour l'audit bibliographique
- p. 154 [399] : grille d'Anthropic d'octobre 2026 : Haiku 5.5 à 0,10 / 0,50 $ US (≤ 100 000 jetons) et 0,50 / 2,50 $ US au-delà; Fable 5.1 à 10 / 50 $ US, avec ou sans majoration au-delà de 100 000 jetons; segmenteur des modèles 4.7 et suivants donnant « environ 30 % » de jetons en plus; majoration de 10 % pour l'inférence restreinte aux États-Unis et pour les points de terminaison régionaux des partenaires.
- p. 154 [401] : multiplicateurs de lecture en cache de 0,05 (Opus 5.5, Sonnet 5.5) et 0,025 (Fable 5.1); écriture à 1,25 (5 min) et à 2 (1 h).
- p. 154 [402] : seuil de 1 024 jetons « pour GPT-5.6 et les suivants ». Le même seuil s'appliquait déjà aux modèles antérieurs depuis 2024 : la formulation laisse-t-elle croire à tort à une nouveauté?
- p. 154 [400] : absence de zone canadienne dans la résidence des données de l'API d'Anthropic, et prise en charge éventuelle de la restriction géographique pour les lots (FIN-08).
- p. 154 [397] : le chiffre « plus de 280 fois » (AI Index 2025) est-il repris, révisé ou contredit dans l'édition 2026?
- p. 154 [205] : 58 outils pour environ 55 000 jetons (billet du 24 novembre 2025).
- p. 155 [403] : Belcak et coll. (2025) est un article de position; les « 40 à 70 % » sont-ils des estimations des auteurs sur trois études de cas (MetaGPT, Open Operator, Cradle) plutôt que des mesures?
- p. 155 [53] : Copilot Studio : 5 crédits par action d'agent, 10 crédits par 1 000 jetons pour un modèle de raisonnement, désactivation des agents personnalisés au-delà de 125 % de la capacité prépayée.
- p. 155 [55] : Agentforce : crédit à 0,005 $ US, environ 0,10 $ US par action standard.
- p. 156 [404] et p. 157 [405] : niveau de risque « élevé » de GENCOST05-BP01; le Generative AI Lens retient-il bien « trois principes », ou cinq pratiques (GENCOST01 à 05)?
- p. 156 [107] : comportement de `llm-token-limit` (compteurs par passerelle ou région, estimation en diffusion, dépassement en concurrence).
- p. 157 [119] : la convention v1.41.0 demande-t-elle (SHOULD) que `gen_ai.usage.input_tokens` inclue les jetons servis depuis le cache, et nomme-t-elle l'attribut `gen_ai.usage.cache_read.input_tokens`?
- p. 157 [9] : le Centre d'architecture Azure recommande-t-il explicitement un modèle proportionné par agent et la mesure des jetons par agent et par exécution?
- p. 158 [408, 409] : FOCUS 1.4 sans colonne native de jetons : la colonne ConsumedUnit ne peut-elle pas porter des « tokens »? Granularité des exports FOCUS des fournisseurs d'inférence (par clé, par espace, par requête).
- p. 160 [56] : Loi sur l'accès, art. 8 et 8.1 (responsable et comité obligatoire), en complément des art. 63.3 et 63.5.
- p. 160 [90] : Entra Agent ID distingue-t-il aussi un rôle « manager » en plus du sponsor et de l'owner?

audit_16.md : 31 constats (1 BLOQUANT, 14 MAJEUR, 16 MINEUR)
