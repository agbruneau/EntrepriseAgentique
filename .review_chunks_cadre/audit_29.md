# Audit chunk_29 — pages 281-283

## Synthèse
Le chunk couvre la fin de H.3 (une phrase de couture), le tableau 72 (errata H.4) et ses trois « précisions », H.5 (ce qui n'a pas été rouvert) et les références [474]-[495]. Les dates et l'arithmétique se vérifient : 30 mars 2027 et 28 septembre 2027 tombent bien un dernier mardi, l'expiration à 185 jours de l'ébauche −17 tombe le 4 mai 2027, et la SEP-2596 finale le 3 juin plus trois mois donne le 3 septembre 2026. Les défauts portent plutôt sur la complétude et la cohérence des errata. Les trois plus graves :
- l'erratum 1 corrige le § 6.6 mais oublie le § 13.1, qui dit encore « huit entreprises »;
- le traitement de l'erratum 3 inscrit comme « survenu » un signal qui n'a pas eu lieu, et le rattache à une exigence (EXIG-INT-23) qui ne vise pas MCP;
- le critère « erratum ou précision » est appliqué de façon inégale (Bloomberg contre HTTP+SSE). S'y ajoute une phrase de couture qui minimise le report 8, lequel rend circulaire la règle classe × niveau.

## Constats

### [29-01] [MAJEUR] Erratum 1 incomplet : le § 13.1 garde « huit entreprises »
- **Axe** : C
- **Localisation** : tableau 72, no 1, p. 281 : « Section 6.6, « Rôle, historique et gouvernance » »; le corps, § 13.1, p. 190 : « son comité directeur technique réunit huit entreprises concurrentes : AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow[29] ».
- **Diagnostic** : la recherche Grep de « huit entreprises » et de « comité directeur » ne trouve que deux occurrences dans le corps : p. 67 (§ 6.6) et p. 190 (§ 13.1). L'erratum ne localise que la première. La ligne « A2A, gouvernance » du tableau 70 (p. 277) n'énumère pas non plus le § 13.1 (« sommaire, 2.2 (tableau 5), 6.6, 6.9, annexe F »).
- **Contre-exemple** : une fois l'erratum appliqué, le § 6.6 dit « neuf entreprises » et le § 13.1, chapitre d'approvisionnement qui fonde sur ce décompte l'argument « le risque … est donc faible », dit « huit ». Le document se contredit après correction.
- **Correctif proposé** : étendre la colonne « Où » à « sections 6.6 et 13.1 » et appliquer le même libellé de remplacement aux deux endroits. Ajouter 13.1 à la ligne correspondante du tableau 70.
- **Confiance** : vérifié dans le texte.

### [29-02] [MINEUR] « nine seats » traduit par « neuf entreprises »
- **Axe** : A
- **Localisation** : tableau 72, no 1 : « Le fichier de gouvernance du projet compte « nine seats » … Lire « neuf entreprises » »; réf. [479], p. 282.
- **Diagnostic** : le nombre de sièges statutaires d'un comité ne dit pas combien sont occupés ni par combien d'entités distinctes. Le correctif passe de « nine seats » à « neuf entreprises » sans citer la liste des membres. Le corps compte en outre « IBM Research », une division, parmi les « entreprises ».
- **Contre-exemple** : si GOVERNANCE.md prévoit neuf sièges dont un est vacant ou partagé, le correctif « neuf entreprises » serait lui-même un erratum.
- **Correctif proposé** : citer la liste nominative des membres (section « Members » de GOVERNANCE.md au commit 98279d6), ou écrire « un comité de neuf sièges, dont Bloomberg depuis le 20 octobre 2026 ».
- **Confiance** : déduit; à vérifier sur la source externe.

### [29-03] [MAJEUR] Critère « erratum ou précision » appliqué de façon inégale (Bloomberg contre HTTP+SSE)
- **Axe** : A, C
- **Localisation** : p. 281 : « Un énoncé exact à sa date, mais dépassé depuis, relève du 70, non d'un erratum », puis « Le retrait de HTTP+SSE « trois mois après que la SEP-2596 atteint l'état final » … reproduit fidèlement le registre … mais l'échéance était déjà calculable au 27 octobre (H.2) »; le corps, p. 57 (tableau 17) et p. 67 (« Pourquoi » de l'EXIG-MCP-22).
- **Diagnostic** : l'erratum 1 est retenu parce qu'un fait primaire antérieur à l'état des sources (le 20 octobre) rendait faux un énoncé du corps. Pour HTTP+SSE, le fait primaire est encore plus ancien : la SEP-2596 est finale depuis le 3 juin 2026 ([475]), avant même la publication de la révision 2026-07-28. Pourtant le corps présente encore l'échéance comme une condition à venir, et le « Pourquoi » de l'EXIG-MCP-22 affirme que « l'échéance retenue … évite qu'une révision future ne rompe des intégrations en production ». Selon le critère du préambule, cet énoncé n'est pas « exact à sa date, mais dépassé depuis » : il était déjà dépassé à sa date. Le classer comme simple « précision » contredit le traitement de l'erratum 1. La seule différence est la fidélité littérale au registre, critère qui n'est énoncé nulle part.
- **Contre-exemple** : H.2 (p. 276 et p. 279) établit que HTTP+SSE « peut disparaître dès la révision de mars 2027 », soit quatre mois avant l'échéance de migration du 28 juillet 2027. Un lecteur du corps seul croit que le 28 juillet 2027 protège toutes les fonctions dépréciées. Ce n'est pas le cas pour un client passé à la révision de mars 2027 face à un serveur antérieur qui n'offre que HTTP+SSE.
- **Correctif proposé** : ajouter au tableau 72 une ligne no 4 (incohérence) visant le tableau 17 et le « Pourquoi » de l'EXIG-MCP-22, avec ce libellé : « admissible au retrait depuis le 3 septembre 2026 (SEP-2596 finale le 3 juin 2026) ». Énoncer dans le préambule le critère qui distingue un erratum d'une précision.
- **Confiance** : vérifié dans le texte (dates internes). L'interprétation du déclencheur du registre est à vérifier par l'audit bibliographique (question 3).

### [29-04] [MAJEUR] Erratum 3 : un signal inscrit « comme survenu » alors qu'il n'a pas eu lieu
- **Axe** : A
- **Localisation** : tableau 72, no 3, colonne « Traitement proposé » : « Inscrire au catalogue le signal comme survenu, avec la date du 30 mars 2027 (H.2) »; à comparer avec H.2, p. 275 : « a désormais une date : le 30 mars 2027, sous réserve du calendrier de transition ».
- **Diagnostic** : le signal défini au § 6.9 (p. 85) est « une révision de MCP ». Ce qui est survenu, c'est l'annonce d'une date de révision, non la révision elle-même. L'EXIG-INT-23 dispose que « L'apparition du signal DOIT entraîner une révision extraordinaire de l'entrée ». Inscrire le signal comme survenu déclenche donc une révision extraordinaire sans objet, près de cinq mois avant la publication. Le traitement abandonne en outre la réserve « subject to confirmation in the transition calendar » que H.2 et la réf. [474] conservent.
- **Contre-exemple** : si le calendrier de transition repousse la publication au-delà du 30 mars 2027, le catalogue porte un signal « survenu » daté d'un événement qui n'a pas eu lieu, et la révision extraordinaire a été tenue sur une spécification inexistante.
- **Correctif proposé** : « Inscrire au catalogue la date annoncée de la prochaine révision (30 mars 2027, sous réserve du calendrier de transition [474]); le signal surviendra à la publication. »
- **Confiance** : vérifié dans le texte.

### [29-05] [MINEUR] Erratum 3 et H.2 : EXIG-INT-23 ou EXIG-GOV-18?
- **Axe** : C
- **Localisation** : tableau 72, no 3 : « Sections 6.5 et 6.9 (signaux de l'EXIG-INT-23) »; tableau 70, p. 275 : « Le signal « révision de MCP » de l'EXIG-INT-23 »; H.2, p. 279 : « celle de mars 2027 appellera donc la révision extraordinaire de l'EXIG-GOV-18 ».
- **Diagnostic** : l'EXIG-INT-23 (p. 86) ne vise que les entrées « au statut Évaluer ou Surveiller ». Or MCP 2026-07-28 est au statut Adopter (tableau 15, p. 50). Pour un standard Adopter, la révision extraordinaire relève de l'EXIG-GOV-18 (p. 169), comme le dit correctement H.2 à la p. 279. L'annexe rattache donc le même événement à deux exigences dont les champs d'application s'excluent. Le défaut d'origine est au § 6.9, qui range « une révision de MCP » parmi les signaux de veille.
- **Contre-exemple** : un vérificateur qui applique l'EXIG-INT-23 à la lettre conclut qu'aucun signal ne peut être inscrit pour MCP, puisque l'entrée n'est ni au statut Évaluer ni au statut Surveiller.
- **Correctif proposé** : dans le tableau 72 (no 3) et le tableau 70, viser l'EXIG-GOV-18. Au § 6.9, préciser que la révision de MCP est un signal au sens de l'EXIG-GOV-18 et non de l'EXIG-INT-23. Ce dernier point est peut-être déjà relevé par l'audit du chunk 09.
- **Confiance** : vérifié dans le texte.

### [29-06] [MAJEUR] Erratum 2 : une affirmation non étayée par ses sources, déclarée « aucun erratum »
- **Axe** : C (et méthode, thèse T8)
- **Localisation** : tableau 72, no 2 : « Aucun erratum au cadre … La mention « approbation du conseil d'administration le 4 août » (tableau 5) ne figure dans aucun des deux billets : non vérifiée »; tableau 5, p. 17 : « (approbation du conseil d'administration le 4 août)[5, 35] », dans un tableau intitulé « Chronologie vérifiée ».
- **Diagnostic** : l'annexe établit, sur les sources primaires elles-mêmes, que les références citées ([5] et [35]) ne contiennent pas l'affirmation. C'est un défaut de citation prouvé, qui entre exactement dans le critère du tableau 72 (« ce qu'une source primaire établit »). Le qualifier de simple « non vérifié » et conclure qu'il n'y a « aucun erratum au cadre » contredit à la fois ce critère et le titre « Chronologie vérifiée ». Aucun traitement n'est proposé.
- **Contre-exemple** : un lecteur qui remonte aux sources [5] et [35] pour vérifier la date du 4 août ne la trouve pas. La méthode de validation des sources (annexe F) se trouve prise en défaut sur un tableau présenté comme vérifié.
- **Correctif proposé** : traiter le point comme un erratum de citation. Retirer la parenthèse ou la rattacher à une source qui la contient (une décision du conseil de l'AAIF ou la proposition d'admission, si elle existe), et le dire dans la colonne « Traitement proposé ».
- **Confiance** : vérifié dans le texte. L'existence d'une source pour le 4 août est à vérifier (question 1).

### [29-07] [MINEUR] Erratum 2 : localisation et attribution incomplètes
- **Axe** : C
- **Localisation** : tableau 72, no 2, colonne « Où » : « Sommaire, tableau 5, sections 2.2 et 6.6, tableau 68 (no 7); [5], [35] »; colonne « Constat » : « la fondation compte A2A parmi ses projets [5, 35, 130] ».
- **Diagnostic** : la même affirmation figure au § 13.1, p. 189 (« est devenu un projet hébergé de l'AAIF le 17 août 2026[5, 35] »), et au § 6.9, p. 84 (« l'AAIF héberge dix projets : … A2A »). Aucun de ces deux endroits n'est listé, alors que le tableau 70 (p. 277) mentionne bien le § 6.9. Par ailleurs, [5] est le billet du projet A2A et non une source de la fondation.
- **Contre-exemple** : quand l'écart sera levé dans la Veille, une mise à jour qui suivrait la colonne « Où » laisserait de côté les § 6.9 et 13.1.
- **Correctif proposé** : ajouter les sections 6.9 et 13.1 à la colonne « Où », et écrire « [35, 130] » pour ce que compte la fondation.
- **Confiance** : vérifié dans le texte.

### [29-08] [MINEUR] « Errata et incohérences prouvés » : la ligne 2 n'est pas prouvée, deux lignes sur trois ne sont pas des errata
- **Axe** : C
- **Localisation** : titre de H.4 et préambule « Le 72 ne retient que ce qu'une source primaire établit »; ligne no 2 : « Ce que le site affichait le 29 octobre n'est pas vérifiable ici ».
- **Diagnostic** : la ligne 2 reconnaît que l'état du site au 29 octobre est invérifiable. L'incohérence avec la Veille n'est donc pas établie : il se peut que le site ait changé entre le 29 octobre et le 1er novembre. Les lignes 2 et 3 concluent chacune « aucun erratum » ou « ce n'est pas un erratum ». Le tableau ne contient donc qu'un erratum, le no 1, malgré son titre.
- **Contre-exemple** : sans objet. Le défaut est de qualification, non de fond.
- **Correctif proposé** : renommer la section en « Errata et écarts entre livrables » et ajouter une colonne « Statut » (erratum prouvé, écart prouvé, écart non tranché), la ligne 2 relevant du dernier.
- **Confiance** : vérifié dans le texte.

### [29-09] [MINEUR] Précision sur l'article 50 : le corps contenait déjà la transition
- **Axe** : C
- **Localisation** : p. 281 : « sous réserve de la transition de l'article 50(2) au 2 décembre 2026 que la Commission affiche au 1er novembre [57]; l'état de la page au 27 octobre n'a pas été vérifié »; le corps, § 12.7, p. 185 : « un délai transitoire jusqu'au 2 décembre 2026 vise le marquage des systèmes déjà sur le marché avant le 2 août 2026[57, 457] ».
- **Diagnostic** : le corps, daté du 27 octobre, cite déjà [57] pour cette transition. La réserve « non vérifié » est donc sans objet : le corps atteste que l'information était connue à la date de l'état des sources. Le vrai défaut est interne au corps : le § 12.4 (p. 180) omet la transition que le § 12.7 énonce. H.2 (p. 278) la présente aussi à tort comme nouvelle (« Au 2 décembre 2026 s'ajoute »).
- **Contre-exemple** : un lecteur de H.4 croit à une lacune du corps qui n'existe pas, et manque l'écart réel entre le § 12.4 et le § 12.7.
- **Correctif proposé** : « le § 12.4 omet la transition de l'article 50(2) au 2 décembre 2026, que le § 12.7 énonce déjà [57, 457] : renvoi à ajouter au § 12.4 ». Corriger « s'ajoute » au tableau 70.
- **Confiance** : vérifié dans le texte. La date du 2 décembre 2026 est à vérifier (question 4).

### [29-10] [MINEUR] Précision C-36 : réinterprétation au lieu d'une correction, et citation mal rattachée
- **Axe** : C
- **Localisation** : p. 281 : « « Deuxième lecture » (tableau 48) se lit « à l'étape de la deuxième lecture » … ce que dit aussi la Veille [492] »; tableau 48, p. 178 : « Déposé le 15 juin 2026; deuxième lecture; non en vigueur ».
- **Diagnostic** : dans une suite d'étapes franchies (« déposé…; deuxième lecture; »), « deuxième lecture » se lit comme un événement accompli. L'annexe établit le contraire (dernière étape franchie : la première lecture), mais ne propose aucun nouveau libellé : l'ambiguïté reste dans le corps. Par ailleurs, la réf. [492] renvoie à LEGISinfo, pas à la Veille (qui est la réf. [493]) : la formule « la Veille [492] » attribue la citation à la mauvaise source.
- **Contre-exemple** : un juriste qui lit le tableau 48 conclut que C-36 a passé la deuxième lecture, donc qu'il a été adopté en principe, ce qui est faux au 1er novembre.
- **Correctif proposé** : remplacer la cellule par « Déposé et lu une première fois le 15 juin 2026; à l'étape de la deuxième lecture; non en vigueur », et écrire « ce que dit aussi la Veille [493]; statut LEGISinfo [492] ».
- **Confiance** : vérifié dans le texte.

### [29-11] [MAJEUR] Couture H.3/H.4 : « Le report 7 est le seul qui toucherait la structure normative » est faux (le report 8 rend circulaire la règle classe × niveau)
- **Axe** : A
- **Localisation** : p. 281 : « Le report 7 est le seul qui toucherait la structure normative du cadre; les autres en complètent le contenu »; tableau 71, no 8, p. 280 : « Ajouter aux critères de classe … le niveau d'autonomie demandé … à concilier avec la section 12.1, qui sépare classe et niveau et fait de la classe le plafond du niveau (EXIG-CON-02) ».
- **Diagnostic** : le report 8 modifie les critères de classification (tableau 46, EXIG-CON-01), ce qui est de la structure normative au même titre que le report 7. Il introduit surtout une dépendance circulaire : la classe dépendrait du niveau demandé, alors que le niveau est plafonné par la classe. La règle n'a plus de point fixe garanti. Le report 9 touche lui aussi la règle de préséance du § 1.6.
- **Contre-exemple** : supposons un critère « N3 demandé ⇒ classe élevée ». Un agent qui demande N3 devient de classe élevée, donc plafonné à N2. Redemandé en N2, il redevient de classe modérée, plafonnée à N3, et peut donc redemander N3. Le résultat dépend de l'ordre d'évaluation : c'est un cas indécidable au sens de la thèse T7.
- **Correctif proposé** : « Les reports 7, 8 et 9 toucheraient la structure normative (préfixe et registre; critères de classe; règle de préséance); le report 8 exige au préalable de rompre la circularité entre classe et niveau, par exemple en évaluant la classe sans le critère d'autonomie, puis en refusant tout niveau demandé au-delà du plafond. »
- **Confiance** : vérifié dans le texte (circularité déduite des règles citées).

### [29-12] [MINEUR] EN 18286 : « hors du cadre » en H.5, rattachée à des exigences en H.2
- **Axe** : C
- **Localisation** : H.5, p. 282 : « Hors du cadre. Quatre sources datées ne portent ici aucune exigence … EN 18286 »; tableau 70, p. 278-279 : « EN 18286 donne présomption de conformité à l'article 17 pour l'organisation requalifiée fournisseur (EXIG-CON-15, J2a); le cadre ne la cite pas »; préambule de H.2 : « dépendances datées qui portent une exigence ».
- **Diagnostic** : la même source est rangée à la fois parmi les dépendances qui portent une exigence (tableau 70) et parmi les sources qui n'en portent aucune (H.5).
- **Contre-exemple** : le comité ne sait pas si EN 18286 appelle une décision au titre de l'EXIG-CON-15 ou un simple signalement.
- **Correctif proposé** : en H.5, écrire « ne portent aucune exigence du cadre actuel; EN 18286 pourrait en porter une au titre de l'EXIG-CON-15 (tableau 70) », ou retirer la ligne du tableau 70.
- **Confiance** : vérifié dans le texte.

### [29-13] [MINEUR] H.5 « Non vérifiés » mélange deux états différents
- **Axe** : C
- **Localisation** : H.5, p. 281 : « Non vérifiés le 1er novembre 2026. La page … (HTTP 403); … la date d'approbation du 4 août citée au tableau 5 ».
- **Diagnostic** : les trois premiers éléments sont des sources inaccessibles. Pour le quatrième, les sources ont été lues et l'affirmation n'y figure pas (constat no 2 du tableau 72) : elle n'est pas « non vérifiée » mais « non étayée par ses sources ». Voir [29-06].
- **Contre-exemple** : sans objet. Le défaut est de qualification.
- **Correctif proposé** : déplacer le 4 août vers une mention « non étayé par les sources citées » rattachée à l'erratum proposé en [29-06].
- **Confiance** : vérifié dans le texte.

### [29-14] [MINEUR] Liste « Non rouverts » non déclarée exhaustive, avec des sources datées qui manquent
- **Axe** : B, C
- **Localisation** : H.5, p. 281-282 : « Non rouverts. La Loi 25 … les chiffres d'analystes. Leur état au 1er novembre 2026 est inconnu, non « inchangé » ».
- **Diagnostic** : la recherche Grep sur l'annexe H (à partir de la ligne 18930 de full.txt) ne trouve ni OWASP NHI Top 10 2025, ni NIST AI 100-2 E2025, ni ISO/IEC 17021-1, ni les RFC 8693 et 8785. Ces sources ne figurent ni au tableau 70 ni en H.5. Comme la liste ne se déclare pas exhaustive, leur état est ambigu, alors que la règle de H.1 veut justement qu'un état inconnu soit déclaré tel.
- **Contre-exemple** : un lecteur infère que l'OWASP NHI Top 10 a été rouvert et trouvé inchangé, ce qui n'a pas été fait.
- **Correctif proposé** : ajouter « et toute source du corps absente du tableau 70 », ou compléter la liste.
- **Confiance** : vérifié dans le texte.

### [29-15] [MINEUR] Le mot « tableau » manque dans les renvois de l'annexe H
- **Axe** : C
- **Localisation** : p. 281 : « Le 72 ne retient que … relève du 70 »; même tournure en p. 275 (« Le 70 reprend ») et p. 280 (« Le 71 les présente »).
- **Diagnostic** : le corps écrit « Le tableau 6 présente » (p. 18). L'annexe H omet systématiquement le mot « tableau », sans doute à cause d'un renvoi Typst sans supplément (déduction). Comme l'omission est régulière, ce n'est probablement pas un artefact d'extraction.
- **Contre-exemple** : « relève du 70 » est inintelligible hors contexte.
- **Correctif proposé** : écrire « Le tableau 72 », « du tableau 70 », « Le tableau 71 », et vérifier le supplément des renvois dans la source Typst.
- **Confiance** : vérifié dans le texte (cause déduite).

### [29-16] [MINEUR] Références [474]-[495] : format différent de l'annexe G
- **Axe** : C
- **Localisation** : p. 282-283, par exemple « [474] Model Context Protocol. « SEP-3398: Release Cycle Updates », statut Accepted … Consulté le 1er novembre 2026 »; à comparer avec l'annexe G : « [195] Soria Parra, D. et Delimarsky, D. (2026). The New MCP Roadmap. Model Context Protocol Blog. https://… ».
- **Diagnostic** : l'annexe G suit le format « Auteur (date). Titre. Éditeur. URL », sans date de consultation. L'annexe H met le titre entre guillemets, ajoute le statut et la date de consultation, et date dans le corps de la notice. Les deux formats coexistent dans une même numérotation continue.
- **Contre-exemple** : sans objet. Le défaut est de présentation.
- **Correctif proposé** : unifier les formats, ou déclarer en H.1 le format propre à l'annexe (justifié par l'horodatage des relevés).
- **Confiance** : vérifié dans le texte.

### [29-17] [MINEUR] Références peu reproductibles : [483], [486] et [492]
- **Axe** : B, C
- **Localisation** : [483], p. 283 : « https://datatracker.ietf.org/api/v1/doc/document/ »; [486] : « OAI/Arazzo-Specification …, asyncapi/spec (v3.1.0), cloudevents/spec (v1.0.2) … https://github.com/OAI/Arazzo-Specification/tags »; [492] : « Projets de loi C-36 et C-22 … https://www.parl.ca/legisinfo/en/bill/45-1/c-36/json ».
- **Diagnostic** : [483] renvoie à la racine d'une API et non aux dix ébauches citées. [486] regroupe trois dépôts sous l'URL d'un seul. [492] cite C-22 sans donner son URL. Un relevé d'état daté n'est reproductible que si chaque objet a son adresse.
- **Contre-exemple** : un auditeur ne peut pas retrouver l'état « RFC Ed Queue » de draft-ietf-oauth-identity-chaining-17 à partir de l'URL fournie.
- **Correctif proposé** : une URL par objet (pages datatracker de chaque ébauche, étiquettes des dépôts asyncapi/spec et cloudevents/spec, fiche JSON de C-22).
- **Confiance** : vérifié dans le texte.

### [29-18] [MINEUR] [493] et l'erratum 3 utilisent des numéros de la Veille qui existent aussi dans le cadre
- **Axe** : C
- **Localisation** : [493], p. 283 : « annexe « Reprise du 29 octobre 2026 » (tableau 25 et références [343] et [350]) »; erratum 3 : « l'annexe du 29 octobre de la Veille (tableau 25) ».
- **Diagnostic** : dans le cadre, [343] est l'OpenID Shared Signals Framework et [350] l'OWASP AST10 (cité au tableau 70 sous « [222, 350] »). Le tableau 25 du cadre porte sur les patrons. Les mêmes numéros désignent ici des objets de la Veille, sans préfixe qui les distingue.
- **Contre-exemple** : un lecteur qui suit [350] tombe sur l'OWASP AST10 au lieu de la source de la Veille.
- **Correctif proposé** : préfixer les numéros externes, par exemple « Veille, tableau 25; Veille, réf. [343] et [350] ».
- **Confiance** : vérifié dans le texte.

### [29-19] [MINEUR] H.5, NIST IR 8547 : ce qui est signé ne se limite pas au journal d'audit
- **Axe** : B
- **Localisation** : H.5, p. 282 : « la conservation longue des enregistrements d'audit signés (EXIG-OBS-12, EXIG-OBS-13) est le point où le comité pourrait vouloir examiner la première ».
- **Diagnostic** : d'autres objets à vérifier longtemps sont signés en ES256 : les jetons d'approbation (« approbation+jwt », ES256, annexe C, p. 221), dont l'empreinte figure au journal pour la non-répudiation, et les cartes d'agent signées en JWS (EXIG-A2A-10). Aucune exigence n'impose d'agilité cryptographique. L'EXIG-OBS-13 prévoit « au moins 24 mois, davantage si … un régime sectoriel … l'exige », ce qui peut dépasser l'horizon de dépréciation d'ECDSA.
- **Contre-exemple** : une conservation de dix ans imposée par un régime sectoriel, avec des approbations signées en 2027, devrait encore être vérifiable après la date où ECDSA P-256 ne sera plus admis. Le journal seul ne suffit pas à prouver l'approbation.
- **Correctif proposé** : étendre la mention aux approbations (§ 8.5, C.6) et aux cartes signées, et suggérer au comité un point « agilité cryptographique et re-scellement » (horodatage ou contre-signature périodique).
- **Confiance** : déduit. Les dates de dépréciation dans la version finale de l'IR 8547 sont à vérifier (question 6).

## Points forts
- Vérifications arithmétiques exactes : 30 mars 2027 et 28 septembre 2027 sont bien des derniers mardis, l'expiration à 185 jours de la −17 donne le 4 mai 2027, et la SEP-2596 plus trois mois donne le 3 septembre 2026.
- La discipline « inconnu, non « inchangé » » et la séparation entre « non vérifiés », « non rouverts » et « hors du cadre » sont saines, malgré les écarts relevés en [29-13] et [29-14].
- Les vérifications négatives de H.5 tiennent : IR 8547, le Real-Time Rail et toute norme harmonisée sont effectivement absents du corps, et aucune exigence ne fixe d'algorithme de signature.

## Questions pour l'audit bibliographique
1. p. 281 (no 2) : existe-t-il une source primaire de l'AAIF (procès-verbal, annonce, proposition d'admission) datant au 4 août 2026 l'approbation de l'admission d'A2A par le conseil? À défaut, l'erratum de citation proposé en [29-06] s'impose.
2. p. 281 (no 1) et [479] : GOVERNANCE.md d'a2aproject/A2A au commit 98279d6 nomme-t-il neuf membres distincts, ou seulement neuf sièges?
3. p. 281 (précisions) et [475] : le déclencheur du registre des dépréciations MCP (« three months after SEP-2596 reaches Final ») vise-t-il bien le statut Final de la SEP, posé par la PR no 2856 le 3 juin 2026? Le fait que la révision du 28 juillet reprenne cette condition au futur suggère une autre lecture possible.
4. p. 281 et [57] : la date de fin de la transition de l'article 50(2) est-elle le 2 décembre 2026 dans le texte adopté du règlement (UE) 2026/1744? Je crois me souvenir que la proposition d'omnibus de la Commission prévoyait le 2 février 2027, ce qui reste à confirmer sur EUR-Lex.
5. p. 282 et [489, 490] : EN 18286:2026 et la décision d'exécution (UE) 2026/2274 (JO L du 14 octobre 2026) existent-elles, et la norme porte-t-elle bien sur l'article 17 (système de management de la qualité)?
6. p. 282 et [494] : date et contenu de la version finale de NIST IR 8547, notamment le calendrier de dépréciation et de retrait d'ECDSA P-256.
7. p. 282 et [495] : déclaration du BSIF du 15 octobre 2026 sur les « Sound Practices » du FSB (existence, date, mention d'E-23).
8. p. 282-283 et [474], [476], [481]-[484] : dates et statuts des SEP-3398 (acceptée le 14 octobre, fusionnée le 27 octobre) et SEP-3392 (Final, fusionnée le 29 octobre), de draft-ietf-oauth-v2-1-17 (31 octobre), de l'ID-JAG −05 et −06, de transaction-tokens-11 et identity-chaining-17 (RFC Ed Queue), et de la Last Call de workload-identity-practices-08 jusqu'au 13 novembre.

audit_29.md : 19 constats (0 BLOQUANT, 6 MAJEUR, 13 MINEUR)
