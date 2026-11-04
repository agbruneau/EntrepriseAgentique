# Audit chunk_18 — pages 171-182

## Synthèse
Le chunk couvre la fin du § 12.1 (tableau 46, EXIG-CON-01 à 03), tout le § 12.2 (Loi 25, tableau 47, EXIG-CON-04 à 10), le § 12.3 (tableau 48, EXIG-CON-11 et 12), le § 12.4 (RIA, tableau 49, EXIG-CON-13 à 16) et le début du § 12.5. La restitution du droit québécois est précise et bien sourcée, et la séparation entre obligation légale et choix du cadre est rigoureuse. Ce qui pèche, c'est le raccord avec l'architecture des chapitres 9 et 10. Les trois défauts les plus graves :
1. Aucun magasin ne peut conserver les « RP en entrée » d'une décision pendant un an. Les traces n'ont pas le droit de contenir ce contenu (EXIG-OBS-07) et le journal d'audit n'en garde que l'empreinte (EXIG-OBS-12) ([18-01]).
2. La classe dépend du caractère « exclusivement automatisé » de la décision, qui dépend à son tour du niveau que la classe plafonne : la classification peut osciller sans point fixe ([18-02]).
3. Les contrôles de localisation et de finalité sont confiés à des passerelles qui ne voient pas les flux visés ([18-04], [18-05]).

## Constats

### [18-01] [BLOQUANT] Conservation d'un an des « RP en entrée » sans magasin possible
- **Axe** : A
- **Localisation** : § 12.2, EXIG-CON-09, p. 177 : « L’exportation de traces techniques est un moyen; la personne reçoit une transcription écrite et intelligible. » L'énoncé exige de conserver les « RP en entrée, versions de l’agent, du modèle et des outils, facteurs retenus et approbations ».
- **Diagnostic** : EXIG-CON-09 désigne les traces comme moyen de conserver les RP en entrée. Or EXIG-OBS-07 (p. 150) interdit en production tout contenu d'invite, de réponse et d'argument d'outil dans la télémétrie. EXIG-OBS-08 limite la capture de débogage à une « période bornée », dans un dépôt « de courte durée ». EXIG-OBS-12 ne garde les arguments d'outil que sous forme d'empreinte SHA-256. Aucune des trois sources de preuve du cadre ne peut donc restituer pendant un an les RP utilisés pour décider (art. 11). Le même défaut touche EXIG-AUT-22 (p. 116), qui exige de produire les « RP utilisés » « à partir des traces et du journal d’audit ». Telles qu'elles sont rédigées, ces deux exigences DOIT sont inexécutables par les moyens qu'elles désignent.
- **Contre-exemple** : un client demande, onze mois après un refus de crédit rendu par l'agent, les RP utilisés (art. 12.1). Le span ne contient que des métadonnées, l'audit ne contient que h(arguments) et le dépôt de débogage est purgé. L'entreprise ne peut pas répondre, et le défaut d'information est un motif de sanction administrative pécuniaire (art. 90.1).
- **Correctif proposé** : créer un « dossier de décision » distinct des traces et du journal d'audit. Il serait chiffré, à accès restreint, conservé au moins un an et relié à l'audit par l'empreinte (h(contenu) dans l'audit, contenu dans le dossier). Il faut aussi retirer « l'exportation de traces techniques est un moyen » et réécrire la clause « établie à partir des traces et du journal d’audit » d'EXIG-AUT-22. Enfin, il faut prévoir une exception explicite dans EXIG-OBS-07 et EXIG-OBS-08.
- **Confiance** : vérifié dans le texte (EXIG-CON-09, EXIG-AUT-22, EXIG-OBS-07, EXIG-OBS-08, EXIG-OBS-12 lus dans full.txt).

### [18-02] [MAJEUR] Classification circulaire : la classe dépend de la supervision qu'elle plafonne
- **Axe** : A
- **Localisation** : § 12.1, EXEMPLE, p. 172 : « Si cet avis est communiqué au client sans examen réel par un employé, il s’agit d’une décision fondée exclusivement sur un traitement automatisé ». Le critère se trouve au tableau 46 (classe élevée) et la définition de l'intervention significative aux p. 176 (EXIG-CON-08) et 116 (EXIG-AUT-22 et 23).
- **Diagnostic** : le critère « décision fondée exclusivement sur un traitement automatisé » n'est pas une propriété intrinsèque de l'agent. Il dépend du niveau d'autonomie et de la qualité de l'approbation, c'est-à-dire de ce que la classe sert à plafonner (EXIG-CON-02). De plus, EXIG-AUT-23 mesure l'« influence réelle » par EXIG-AUT-21, donc a posteriori. EXIG-CON-01 exige pourtant la classe avant l'inscription. La fonction classe = f(niveau) et niveau ≤ plafond(classe) n'a pas toujours de point fixe.
- **Contre-exemple** : un agent attribue un palier de fidélité à des clients, effet non « important », sans RP sensibles.
  - À N2 avec révision significative, la décision n'est pas exclusivement automatisée : classe modérée, plafond N3.
  - À N3, il n'y a plus d'approbation : décision exclusivement automatisée, donc classe élevée (tableau 46, EXIG-AUT-22) et plafond N2.
  - Retour à la première étape : la classe oscille. Avant la mise en service, aucune mesure d'EXIG-AUT-21 n'existe pour trancher.
- **Correctif proposé** : évaluer ce critère au niveau d'autonomie *demandé* et au pire cas de supervision. Par exemple : « l'agent rendrait, au niveau demandé, une décision exclusivement automatisée ». Il faut aussi préciser qu'une classe une fois élevée ne redescend pas tant que les mesures d'EXIG-AUT-21 n'ont pas établi une révision significative. C'est à concilier avec le report no 8 du tableau 71 (H.3), qui ajoute le « niveau d’autonomie demandé » aux critères sans résoudre la circularité.
- **Confiance** : déduit (raisonnement formel sur le texte).

### [18-03] [MAJEUR] Deux tests divergents de l'approbation nominale (EXIG-CON-08 et EXIG-AUT-23)
- **Axe** : C
- **Localisation** : § 12.2, EXIG-CON-08, p. 176 : « si l’approbateur ne dispose pas de l’une ou l’autre de ces conditions : l’information sur la décision et ses facteurs, le temps nécessaire […], l’autorité de la modifier ».
- **Diagnostic** : les deux exigences ne posent pas les mêmes conditions.
  - EXIG-CON-08 en retient trois : information, temps, autorité.
  - EXIG-AUT-23 (p. 116), vers laquelle elle renvoie, en exige cinq : autorité, compétence, accès à *toutes* les données pertinentes « et non à la seule recommandation de l’agent », temps, et influence réelle mesurée (EXIG-AUT-21).

  Le « À défaut d’une seule d’entre elles » d'EXIG-CON-08 laisse croire que les trois conditions suffisent. Un vérificateur qui suit la grille d'EXIG-CON-08 accepte donc une approbation qu'EXIG-AUT-23 tient pour nominale. Dernier point : le suivi du « taux d’approbation sans modification » est rédigé comme une conséquence du défaut (« À défaut […], et le taux […] est suivi »). Or il devrait être permanent, puisque c'est lui qui alimente EXIG-AUT-21.
- **Contre-exemple** : un approbateur compétent en apparence, disposant du temps voulu et de l'autorité, ne voit que la recommandation et les « facteurs » produits par l'agent. Il approuve à 99,8 %. EXIG-CON-08 est satisfaite; EXIG-AUT-23 ne l'est pas (accès limité, influence nulle).
- **Correctif proposé** : faire d'EXIG-CON-08 un simple renvoi aux cinq conditions d'EXIG-AUT-23 (source unique, comme pour les plafonds dans EXIG-CON-02). Sortir aussi le suivi par approbateur de la proposition conditionnelle.
- **Confiance** : vérifié dans le texte.

### [18-04] [MAJEUR] EXIG-CON-05 confie à la passerelle de modèles un contrôle qu'elle ne peut pas exercer
- **Axe** : B
- **Localisation** : § 12.2, EXIG-CON-05, p. 175 : « la passerelle de modèles DOIT refuser toute route qui n’est pas couverte. »
- **Diagnostic** : l'exigence cartographie quatre types de destinations (modèle, serveur MCP, agent délégataire, magasin de mémoire ou de traces). Elle ne confie pourtant le refus qu'à la passerelle de modèles, qui ne voit que les appels d'inférence (EXIG-ARC, p. 33 : « Tout appel d’inférence DOIT passer par la passerelle de modèles »). Les appels MCP et A2A traversent la passerelle d'agents, et les écritures en mémoire passent par le plan mémoire. Par ailleurs, une « route couverte » se définit par rapport à un flux *de RP*. La passerelle doit donc savoir, requête par requête, si la charge contient des RP, ce que rien ne lui permet de déterminer de façon fiable. Enfin, les points de terminaison « globaux » ou d'inférence interrégionale de certains fournisseurs déplacent le traitement sans que la route déclarée change.
- **Contre-exemple** : un agent délègue par A2A à un agent partenaire hébergé en Virginie, ou écrit un résumé de dossier client dans un index vectoriel en Ontario. Aucune de ces deux routes ne passe par la passerelle de modèles.
- **Correctif proposé** :
  - étendre le refus à la passerelle d'agents (MCP, A2A) et au plan mémoire;
  - raisonner par route déclarée et non par contenu : toute route vers l'extérieur du Québec est refusée si l'agent est autorisé à traiter des RP et que la route n'est pas couverte;
  - exiger contractuellement l'épinglage régional, sans inférence interrégionale (lien avec la clause 5 du § 13.3).
- **Confiance** : vérifié dans le texte (portée de la passerelle de modèles); déduit pour les points de terminaison globaux.

### [18-05] [MAJEUR] Contrôle de finalité placé hors du chemin des usages secondaires
- **Axe** : B
- **Localisation** : § 12.2, EXIG-CON-06, p. 175 : « Les données DOIVENT porter une étiquette de finalité que le service de politiques de la passerelle d’agents (section 9.4) DOIT vérifier avant toute transmission vers un usage secondaire. »
- **Diagnostic** : les usages secondaires typiques ne transitent pas par la passerelle d'agents, point d'application des appels d'outils et des délégations (§ 9.4) : extraction de traces ou de conversations vers un lac de données, constitution d'un corpus d'ajustement fin, analyses. Le contrôle technique censé empêcher la « réutilisation de bonne foi » ne voit donc pas le flux à contrôler. L'exigence est vérifiable en revue, mais pas efficace en exploitation.
- **Contre-exemple** : une équipe de science des données exporte, par l'API du dépôt de mémoires, six mois de conversations pour ajuster un modèle. L'étiquette de finalité existe, mais aucun point d'application ne la lit.
- **Correctif proposé** : placer le contrôle aux points de sortie des magasins (API d'export des dépôts de traces, de mémoire et de conversations; pipelines d'entraînement), sous forme d'une politique de données appliquée par la plateforme de données. Garder la passerelle d'agents pour les seuls flux agentiques.
- **Confiance** : déduit (architecture du § 9.4 lue).

### [18-06] [MAJEUR] La mesure compensatoire au CLOUD Act ne protège pas les données traitées par inférence
- **Axe** : A
- **Localisation** : § 12.2, p. 175 : « Le cadre retient comme mesures compensatoires le chiffrement à clés gérées par l’entreprise et, pour les RP sensibles, le recours à des fournisseurs sous compétence canadienne. »
- **Diagnostic** : un modèle hébergé doit voir les données en clair pour produire l'inférence. Le chiffrement au repos à clés gérées par le client protège les données stockées, mais pas les invites, les contextes ou les sorties en cours de traitement chez le fournisseur, ni les journaux qu'il conserve. Si la clé réside dans le service de gestion de clés du fournisseur (BYOK), celui-ci peut aussi être contraint de l'utiliser. Seules des clés tenues hors du fournisseur (HYOK, ou gestion externe des clés) ou du calcul confidentiel attesté réduisent réellement l'exposition. Pour les RP non sensibles, la mesure retenue donne une assurance trompeuse dans l'EFVP. Deuxième point, mineur : la formule « oblige […] à préserver et à divulguer les données en leur possession » omet que l'obligation naît d'une réquisition légale (18 U.S.C. § 2713 vise le respect des obligations de préservation ou de divulgation découlant d'une procédure). La même formulation figure à la clause 5 (§ 13.3, p. 192).
- **Contre-exemple** : un agent envoie un dossier de réclamation à un modèle hébergé par un fournisseur américain dans une région canadienne, avec chiffrement BYOK. Une ordonnance vise les journaux d'invites conservés 30 jours par le fournisseur pour la détection d'abus. Le chiffrement n'y change rien.
- **Correctif proposé** : préciser le modèle de clés (gestion externe, hors de portée du fournisseur). Exiger contractuellement une conservation nulle des invites et des sorties chez le fournisseur. Mentionner le calcul confidentiel comme option. Enfin, ajouter « sur réquisition légale » à la description du CLOUD Act.
- **Confiance** : déduit (fonctionnement de l'inférence); à vérifier par l'audit bibliographique pour le libellé exact de 18 U.S.C. § 2713.

### [18-07] [MAJEUR] Droit de rectification et de suppression (art. 28) absent, sans propagation aux mémoires et index
- **Axe** : A
- **Localisation** : § 12.2, tableau 47 (p. 173-174), qui n'a aucune ligne pour l'art. 28; EXIG-CON-07, p. 176 : « indiquer le droit de rectification »; EXIG-CON-10, p. 177.
- **Diagnostic** : le cadre renvoie trois fois au droit de rectification (p. 176, EXIG-CON-07, DROIT APPLICABLE), mais ni le tableau 47 ni aucune exigence ne traite l'art. 28 (rectification et suppression; l'art. 28.1, désindexation, n'est pas cité non plus; recherche dans full.txt sans résultat). Pour un agent, c'est le point le plus délicat. Un RP rectifié ou supprimé subsiste dans la mémoire épisodique et sémantique, dans les plongements (traités comme des RP, p. 177), dans les instantanés de mémoire gelés (EXIG-CON-23) et dans les sauvegardes. Les index ANN (par exemple HNSW) se contentent souvent de marquer l'élément comme supprimé jusqu'au compactage. EXIG-CON-10 ne règle que l'échéance de conservation, pas la suppression ponctuelle sur demande.
- **Contre-exemple** : une personne fait rectifier son revenu. L'agent continue de récupérer l'ancien revenu dans sa mémoire sémantique et fonde une nouvelle décision sur un RP inexact, en contravention de l'art. 11 (exactitude au moment de la décision).
- **Correctif proposé** : ajouter une ligne « 28 et 28.1 » au tableau 47 et une exigence de propagation. Une demande de rectification ou de suppression doit atteindre, dans le délai de l'art. 32, chaque mémoire, index et cache inscrits à la fiche, avec suppression physique vérifiable (compactage ou reconstruction de l'index). Il faut aussi prévoir le cas des données sous gel (EXIG-CON-23).
- **Confiance** : vérifié dans le texte (absence); déduit pour les mécanismes d'index; contenu de l'art. 28 à vérifier par l'audit bibliographique.

### [18-08] [MAJEUR] Les poids ajustés sur des RP échappent au cycle de vie
- **Axe** : A
- **Localisation** : § 12.2, EXIG-CON-06, p. 175 : « notamment l’entraînement ou l’ajustement fin de modèles »; EXIG-CON-10, p. 177 : « Chaque magasin de mémoire, index vectoriel et dépôt de traces d’un agent DOIT avoir une durée de conservation ».
- **Diagnostic** : EXIG-CON-06 et le tableau 47 (art. 14) admettent l'entraînement ou l'ajustement fin sur des conversations, avec un consentement distinct. Mais le § 5.5 (p. 42) déclare « l’ajustement des modèles […] hors de la portée du cadre ». EXIG-CON-10 ne couvre ni les poids ni les adaptateurs (LoRA), alors qu'un modèle ajusté peut mémoriser et régurgiter des RP. Le cadre traite pourtant les plongements comme des RP (p. 177) : il les inclut, mais en exclut un artefact au moins aussi riche. Rien ne règle non plus le retrait du consentement (art. 8 ou 9 de la loi, à vérifier) après l'entraînement.
- **Contre-exemple** : un modèle est ajusté en 2026 sur des conversations consenties. En 2027, une personne retire son consentement. Les conversations sont détruites selon EXIG-CON-10, mais le modèle ajusté, inscrit nulle part comme magasin de RP, reste en production indéfiniment.
- **Correctif proposé** : soit interdire l'ajustement fin sur des RP (cohérent avec le § 5.5), soit inscrire les modèles ajustés comme « magasins dérivés » soumis à EXIG-CON-10. Dans ce second cas, il faut une durée de vie, un réentraînement ou une destruction à l'échéance ou au retrait du consentement, et un test d'extraction en équipe rouge.
- **Confiance** : vérifié dans le texte (portée); déduit pour la mémorisation.

### [18-09] [MAJEUR] Le tableau 49 mêle obligations du fournisseur et du déployeur et omet celles du fournisseur requalifié
- **Axe** : A
- **Localisation** : § 12.4, tableau 49, p. 181. La ligne 9 répond « Classe de risque et réévaluations (EXIG-CON-01, EXIG-CON-03); cycle de vie (section 11.5). » EXIG-CON-13 (p. 181-182) soumet l'agent « aux exigences du tableau 49 dès son homologation »; EXIG-CON-15 (p. 182) dit : « elle DOIT conclure des accords écrits avec les tiers ».
- **Diagnostic** : les art. 9, 12 (conception de la journalisation), 13, 15, 72 et 73 sont des obligations du *fournisseur*. L'entreprise déployeuse, qui « l’utilise sous sa propre autorité » (art. 3(4), p. 180), n'y est tenue que si elle devient fournisseur (art. 25). Le tableau ne distingue pas ces rôles. EXIG-CON-13, qui renvoie au tableau en bloc, ne dit pas lesquelles s'appliquent à un simple déployeur. À l'inverse, quand EXIG-CON-15 conclut à la requalification, elle n'exige que les accords écrits (art. 25(4)). Les obligations propres au fournisseur sont absentes : système de gestion de la qualité (art. 17), documentation technique (art. 11), évaluation de la conformité (art. 43), déclaration UE et marquage CE (art. 47-48), enregistrement dans la base de l'UE (art. 49), obligations générales (art. 16). Ce sont pourtant les plus lourdes.
- **Contre-exemple** : une orchestration affecte un modèle d'IA à usage général à la présélection de candidats (annexe III, emploi). La revue d'EXIG-CON-15 conclut que l'entreprise devient fournisseur. Elle conclut les accords de l'art. 25(4) et se croit conforme, sans évaluation de conformité, sans marquage CE et sans enregistrement.
- **Correctif proposé** : ajouter une colonne « rôle » (fournisseur ou déployeur) au tableau 49 et les lignes 11, 16, 17, 43, 47-49. EXIG-CON-15 doit renvoyer à l'ensemble des obligations du fournisseur en cas de requalification.
- **Confiance** : vérifié dans le texte; contenu des articles d'après mes connaissances du RIA (sûr pour l'attribution au fournisseur des art. 9, 11, 16, 17, 43, 49 et 72).

### [18-10] [MAJEUR] Droit à l'explication de l'art. 86 du RIA absent
- **Axe** : A
- **Localisation** : § 12.4, tableau 49 (p. 181) et EXIG-CON-16 (p. 182) : « les personnes visées par une décision prise ou assistée par le système. » À comparer avec EXIG-CON-07 (p. 176) et EXIG-CON-21.
- **Diagnostic** : l'art. 86 donne à toute personne visée par une décision fondée sur la sortie d'un système de l'annexe III, et produisant des effets juridiques ou importants, le droit d'obtenir du déployeur une explication claire du rôle du système et des principaux éléments de la décision. C'est l'analogue européen de l'art. 12.1, mais il couvre les décisions *assistées*. Aucune occurrence de « article 86 » ou « art. 86 » n'apparaît dans le document. Le cadre construit l'explicabilité pour « couvrir les deux régimes » (Loi 25 et C-36, p. 179) sans nommer le régime européen en vigueur pour ses agents à haut risque. Par ailleurs, l'art. 4 (maîtrise de l'IA, applicable depuis le 2 février 2025) n'apparaît pas non plus dans le tableau 49. Sa portée aurait été modifiée par l'omnibus : à vérifier.
- **Contre-exemple** : un agent de tarification d'assurance vie, dont les sorties servent à une filiale française, recommande une surprime qu'un employé approuve de façon significative. L'art. 12.1 ne s'applique pas (révision humaine réelle); l'art. 86 s'applique. Ni EXIG-CON-07 ni le tableau 49 ne le prévoient.
- **Correctif proposé** : ajouter une ligne 86 au tableau 49, avec un renvoi à EXIG-CON-21, qui couvre déjà les décisions partiellement automatisées. Vérifier l'état de l'art. 4 après le règlement (UE) 2026/1744.
- **Confiance** : vérifié dans le texte (absence); contenu de l'art. 86 d'après mes connaissances (sûr); état de l'art. 4 à vérifier.

### [18-11] [MAJEUR] Loi concernant la cybersécurité (ancien C-8) : effet direct probable sur les banques, non retenu
- **Axe** : A
- **Localisation** : § 12.3, p. 179 : « Leur effet sur les fournisseurs de télécommunications et d’infonuagique utilisés par les agents est suivi par le processus de la section 11.7. » Voir aussi EXIG-CON-11 (p. 179) et EXIG-CON-25 (p. 187 : « Loi 25, LPRPDE, BSIF, RIA »).
- **Diagnostic** : d'après mes connaissances du projet C-26, dont C-8 est la reprise, la partie 2 (Loi sur la protection des cybersystèmes essentiels) vise directement les exploitants désignés de services critiques. Ceux-ci comprennent les systèmes bancaires et les systèmes de compensation et de règlement, avec un programme de cybersécurité obligatoire et la déclaration des incidents dans des délais courts (72 heures dans C-26). Le texte présente la loi comme une affaire de fournisseurs de télécommunications et d'infonuagique, alors qu'une banque fédérale qui exploite des agents serait elle-même assujettie. Il en résulte un régime de notification omis dans EXIG-CON-25 et dans la liste d'EXIG-CON-11. L'infonuagique ne figurait pas, à ma connaissance, parmi les services critiques de C-26.
- **Contre-exemple** : une banque désignée subit un incident agentique touchant un cybersystème essentiel. Son plan applique la « règle la plus exigeante » entre la Loi 25, la LPRPDE, le BSIF et le RIA, et omet la déclaration au Centre de la sécurité des télécommunications.
- **Correctif proposé** : vérifier le texte sanctionné (L.C. 2026, ch. 9). Si la partie 2 est conservée, ajouter la loi aux régimes d'EXIG-CON-11 et d'EXIG-CON-25 et au tableau 51 pour les exploitants désignés. Corriger aussi « fournisseurs […] d’infonuagique ».
- **Confiance** : à vérifier (source externe : texte de L.C. 2026, ch. 9, annexe 1 des services critiques; l'annexe H, H.5, indique que la fiche LEGISinfo n'a pas pu être relue).

### [18-12] [MINEUR] Renvoi au § 11.7, qui ne contient aucun processus de veille réglementaire
- **Axe** : C
- **Localisation** : § 12.3, p. 179 : « est suivi par le processus de la section 11.7. »
- **Diagnostic** : le § 11.7 (Gouvernance des standards) régit le catalogue des *protocoles et standards*. EXIG-GOV-20 y nomme les organismes à suivre (AAIF, IETF, OpenTelemetry, W3C, NIST, OWASP), sans aucun législateur ni régulateur. Aucune occurrence de « veille réglementaire » ou « veille juridique » n'apparaît dans le document. Le chapitre 12 cite pourtant de nombreux textes en mouvement : C-36, C-22, le rapport quinquennal de la CAI, l'omnibus et l'AMF.
- **Contre-exemple** : C-22 est adopté en 2027; aucun rôle désigné n'en évalue l'effet sur les fournisseurs.
- **Correctif proposé** : étendre EXIG-GOV-20 à une veille réglementaire (CAI, BSIF, AMF, LEGISinfo, Commission européenne) confiée à l'équipe risques et conformité, ou corriger le renvoi.
- **Confiance** : vérifié dans le texte.

### [18-13] [MINEUR] Trois listes divergentes de déclencheurs de réévaluation
- **Axe** : C
- **Localisation** : EXIG-CON-03, p. 172 (« modèle ou de fournisseur, d’outil ou de palier d’outil, de catégorie de données, de finalité, de population visée ou de lieu de traitement »); figure 25, p. 166 (« modèle, d’invite, d’outil, de protocole ou de population visée »); EXIG-CON-12, p. 180 : « Un changement de modèle, de fournisseur ou de données d’entrée déclenche la revue prévue par E-23. »
- **Diagnostic** : trois ensembles différents pour un même concept. L'invite et le protocole ne figurent pas dans EXIG-CON-03; la finalité, le lieu et le fournisseur ne figurent pas dans la figure 25. Quant aux « données d'entrée » d'EXIG-CON-12, elles sont ambiguës. Pour un agent à récupération, les données d'entrée changent à chaque requête : lues littéralement, elles imposeraient une revue indépendante permanente.
- **Contre-exemple** : un changement d'invite système modifie le comportement décisionnel. La figure 25 renvoie l'agent en conception, mais EXIG-CON-03 ne réévalue ni la classe ni l'EFVP.
- **Correctif proposé** : une liste unique dans EXIG-CON-03, reprise par renvoi. Remplacer « données d’entrée » par « sources ou catégories de données d’entrée ».
- **Confiance** : vérifié dans le texte.

### [18-14] [MINEUR] « Consentement à l'inférence » contraire à l'exception de l'art. 12 citée deux lignes plus haut
- **Axe** : C
- **Localisation** : § 12.2, p. 175 : « le cadre à séparer le consentement à l’inférence (rendre le service demandé) de celui à l’entraînement »; tableau 47, ligne 14.
- **Diagnostic** : le même paragraphe énumère « fourniture d’un service demandé » parmi les exceptions qui dispensent du consentement. Rendre le service demandé est d'ailleurs la fin de la collecte. Exiger un consentement pour l'inférence revient à fonder le service principal sur une base retirable, et à créer un flux de consentement que la loi n'exige pas.
- **Contre-exemple** : un client retire son « consentement à l'inférence ». L'entreprise ne peut plus rendre le service, alors que la loi l'y autorise.
- **Correctif proposé** : formuler « la fin principale (inférence nécessaire au service demandé) et toute fin secondaire (entraînement, ajustement) sont distinguées; seule la seconde exige un consentement distinct ou une exception documentée ».
- **Confiance** : vérifié dans le texte; interprétation juridique déduite.

### [18-15] [MINEUR] L'EFVP du tableau 46 est rattachée à la classe, celle d'EXIG-CON-04 aux RP
- **Axe** : C
- **Localisation** : tableau 46, p. 171 : « EFVP si l’agent traite des RP » (modérée), EFVP inconditionnelle (élevée), rien pour la classe faible; EXIG-CON-04, p. 174.
- **Diagnostic** : l'obligation légale (art. 3.3, EXIG-CON-04) dépend de la présence de RP, pas de la classe. Le tableau impose une EFVP à un agent de classe élevée sans RP (action financière irréversible sur données d'entreprise), où elle n'a pas d'objet. Il l'omet pour la classe faible, dont le critère « données publiques ou internes non confidentielles » n'exclut pas tout RP (annuaire interne, par exemple).
- **Contre-exemple** : un agent de classe faible qui lit l'annuaire du personnel n'a, selon le tableau 46, qu'une autoévaluation; EXIG-CON-04 exige une EFVP.
- **Correctif proposé** : écrire « EFVP si l'agent traite des RP (EXIG-CON-04) » dans les trois classes, et l'évaluation d'impact unifiée pour la classe élevée.
- **Confiance** : vérifié dans le texte.

### [18-16] [MINEUR] Le tableau 47 (art. 3.3) renvoie à EXIG-CON-04 pour les changements, qui relèvent d'EXIG-CON-03
- **Axe** : C
- **Localisation** : tableau 47, p. 173 : « Tout nouvel agent, et tout changement de modèle ou d’outils touchant des RP (EXIG-CON-04). »
- **Diagnostic** : EXIG-CON-04 vise les « projet[s] d’acquisition, de développement ou de refonte » et ne mentionne pas les changements de modèle ou d'outils. C'est EXIG-CON-03 qui déclenche la mise à jour de l'EFVP à chaque changement.
- **Correctif proposé** : « (EXIG-CON-03 et EXIG-CON-04) ».
- **Confiance** : vérifié dans le texte.

### [18-17] [MINEUR] EXIG-CON-10 ne réserve qu'un seul délai légal de conservation
- **Axe** : C
- **Localisation** : EXIG-CON-10, p. 177 : « sous réserve des délais de conservation prévus par la loi (EXIG-CON-09) et du gel des preuves d’un incident (EXIG-CON-23) ».
- **Diagnostic** : la parenthèse assimile les délais légaux au seul art. 11 (EXIG-CON-09). D'autres minimums s'appliquent aux mêmes dépôts : les journaux du déployeur, au moins six mois (art. 26(6) du RIA, EXIG-CON-16); le registre des atteintes de la LPRPDE, 24 mois (tableau 48); le registre des incidents, cinq ans (EXIG-CON-24); l'audit, 24 mois (EXIG-OBS-13). Les conservations pour litige (*legal hold*) ne sont pas non plus réservées.
- **Contre-exemple** : la fiche fixe à 90 jours la durée des traces d'un agent à haut risque visé par le RIA. La purge automatique d'EXIG-CON-10 détruit des journaux que l'art. 26(6) oblige à garder six mois.
- **Correctif proposé** : « sous réserve de tout délai minimal légal, réglementaire ou du cadre applicable (EXIG-CON-09, EXIG-CON-16, EXIG-CON-24, EXIG-OBS-13) et de toute conservation pour litige ou incident ».
- **Confiance** : vérifié dans le texte.

### [18-18] [MINEUR] « Le cadre exige davantage » ne vaut que pour le journal d'audit
- **Axe** : C
- **Localisation** : EXIG-CON-16, p. 182 : « conserver les journaux sous son contrôle au moins six mois (le cadre exige davantage, section 10.3) ».
- **Diagnostic** : le tableau 49 (art. 12) fait répondre aux journaux du RIA à la fois par les traces (§ 10.1) et par l'audit (§ 10.3). Seul l'audit a un minimum de 24 mois (EXIG-OBS-13). La durée des traces est fixée par la fiche selon la finalité (EXIG-CON-10, p. 177) et peut descendre sous six mois. L'affirmation est donc vraie pour une partie seulement des journaux visés par l'art. 12. Ce constat est à lire avec [18-17].
- **Correctif proposé** : fixer un plancher de six mois pour les traces de tout agent à haut risque au sens du RIA, ou préciser que seul l'audit répond à l'art. 26(6).
- **Confiance** : vérifié dans le texte.

### [18-19] [MINEUR] EXIG-CON-10 n'énumère pas l'état durable ni les journaux d'événements
- **Axe** : C
- **Localisation** : § 12.2, p. 177 : « Pour un agent, la règle vise la mémoire épisodique et sémantique (section 5.5), les index vectoriels et les traces. »
- **Diagnostic** : le § 5.5 définit quatre types de mémoire. La mémoire de travail y est « persisté[e] hors du modèle à chaque transition (points de contrôle du moteur durable) ». Les historiques d'exécution durable, les journaux de saga et les sujets d'événements (§ 6.7, 7.4-7.5) contiennent les charges utiles, donc des RP. EXIG-CON-10 ne vise que la mémoire, les index et les traces.
- **Correctif proposé** : ajouter « historiques d'exécution durable, journaux de saga et sujets d'événements » à l'énumération d'EXIG-CON-10.
- **Confiance** : vérifié dans le texte (§ 5.5); déduit pour le contenu des historiques.

### [18-20] [MINEUR] « Classe élevée d'office » ignore la dérogation de l'art. 6(3) sans la déclarer choix du cadre
- **Axe** : A
- **Localisation** : tableau 49, p. 181 : « Classe élevée d’office (EXIG-CON-01 et EXIG-CON-13). » Voir aussi EXIG-CON-13 (p. 181-182) et le § 12.4 (p. 180).
- **Diagnostic** : l'art. 6(3) exclut du haut risque un système de l'annexe III qui n'exécute qu'une tâche procédurale étroite, améliore une activité humaine déjà achevée, détecte des écarts sans remplacer l'évaluation humaine ou effectue une tâche préparatoire, sauf en cas de profilage. Le cadre classe pourtant tout usage de l'annexe III en classe élevée. C'est défendable, mais le texte ne le présente pas comme un « choix du cadre », alors qu'il le fait ailleurs avec soin. Par ailleurs, le § 12.4 décrit l'annexe III sans mentionner l'exclusion de la détection de fraude au point 5(b).
- **Correctif proposé** : ajouter « (choix du cadre : la dérogation de l'art. 6(3) n'est pas utilisée) » ou prévoir une procédure documentée d'application de l'art. 6(3) (avec l'obligation de documentation de l'art. 6(4)).
- **Confiance** : vérifié dans le texte; contenu de l'art. 6(3) d'après mes connaissances (sûr).

### [18-21] [MINEUR] « Membre du personnel nommément désigné » : point unique de défaillance
- **Axe** : B
- **Localisation** : EXIG-CON-07, p. 176 : « offrir un canal pour présenter des observations à un membre du personnel nommément désigné et en mesure de réviser la décision ».
- **Diagnostic** : la loi exige « un membre du personnel en mesure de réviser », pas une personne nommée. Une désignation nominative, combinée au délai de 30 jours, crée un point unique de défaillance (absence, départ). À l'échelle (milliers de décisions de préqualification), elle crée aussi un goulot. Le texte ne dit pas si un rôle ou une file suffit.
- **Correctif proposé** : « un rôle désigné, doté d'au moins un titulaire et d'un suppléant, avec capacité dimensionnée selon le volume de décisions ».
- **Confiance** : déduit.

### [18-22] [MINEUR] Redondance entre EXIG-AUT-22 et EXIG-CON-07, 09 et 21
- **Axe** : C
- **Localisation** : EXIG-CON-07 et EXIG-CON-09, p. 176-177 (« Avis et explication des décisions automatisées »), et EXIG-AUT-22, p. 116.
- **Diagnostic** : EXIG-AUT-22 impose déjà l'avis, l'explication, la rectification, le canal de révision et la conservation d'un an. EXIG-CON-07 et 09 reprennent ces obligations avec des écarts : désignation nominative et délai de 30 jours d'un côté, explication « établie à partir des traces » de l'autre. EXIG-CON-21 en reprend une partie. Ces quatre sources pour une même obligation risquent de diverger à la prochaine révision, comme c'est déjà le cas en [18-03].
- **Correctif proposé** : faire d'une exigence la source unique (EXIG-CON-07) et réduire les autres à des renvois, comme EXIG-CON-02 l'a fait pour les plafonds.
- **Confiance** : vérifié dans le texte.

### [18-23] [MINEUR] Doublement des amendes en récidive attribué à l'art. 91
- **Axe** : C
- **Localisation** : § 12.2, p. 178 : « Les infractions pénales (art. 91) entraînent une amende […]; les amendes sont portées au double en cas de récidive. »
- **Diagnostic** : d'après mes connaissances, le doublement en récidive figure à l'art. 92.1 de la Loi sur le privé, non à l'art. 91. Le tableau 47 ne cite que « 90.1 et suiv., 91, 93.1 ».
- **Correctif proposé** : « (art. 91 et 92.1) ».
- **Confiance** : à vérifier (texte consolidé de la Loi sur le privé).

### [18-24] [MINEUR] Points déjà consignés à l'annexe H
- **Axe** : C
- **Localisation** : tableau 48, p. 178 : « Déposé le 15 juin 2026; deuxième lecture; non en vigueur »; § 12.4, p. 180 : « l’application générale, dont les obligations de transparence de l’article 50, depuis le 2 août 2026 »; EXIG-CON-11, p. 179 (liste des régimes sans l'AMF); EXIG-CON-12 (titre).
- **Diagnostic** :
  - « deuxième lecture » pour C-36 : déjà consigné en H.4, comme précision (« à l'étape de la deuxième lecture »);
  - transition de l'art. 50(2) au 2 décembre 2026 : déjà consigné en H.4, comme précision;
  - absence de l'AMF dans EXIG-CON-11 et titre d'EXIG-CON-12 : déjà proposés par les reports nos 1 à 3 du tableau 71 (H.3), en attente.

  À noter : le texte reconnaît lui-même (p. 179) que les institutions de compétence québécoise intègrent les attentes de l'AMF à leur registre de conformité, mais EXIG-CON-11 ne les liste pas.
- **Correctif proposé** : appliquer H.4 et trancher les reports nos 1 à 3 de H.3.
- **Confiance** : vérifié dans le texte.

## Points forts
- La séparation rigoureuse entre obligation légale et « choix du cadre » (délai de 30 jours, analyse des biais, inclusion de l'Ontario, plongements traités comme des RP) rend chaque exigence défendable devant un juriste.
- L'interprétation de l'intervention humaine significative (p. 176) relie correctement l'art. 12.1 à la mécanique N2, et le RIA est cadré par l'art. 2(1)(c) plutôt que par une « présence en Europe » vague.
- Les sanctions, les dates de la Loi 25 et la portée de l'art. 17 sont exactes d'après mes connaissances.

## Questions pour l'audit bibliographique
- p. 173 : dates d'entrée en vigueur de la Loi 25, dont les « dispositions accessoires » du 22 septembre 2021 [7, 56].
- p. 174 : guide EFVP de la CAI, « version 3.1, avril 2024 », et citations « améliorer un modèle d’intelligence artificielle » et « rendre une décision automatisée » [413].
- p. 175 : cadre fédéral de souveraineté numérique (novembre 2025) et affirmation qu'aucun cas documenté d'accès étranger n'a été relevé [418]; libellé de 18 U.S.C. § 2713 [417].
- p. 176 : art. 90.1, par. 5°, comme motif visant l'art. 12.1 [56, 317].
- p. 177 : position de la CAI sur l'impossibilité d'anonymiser les données génétiques, biométriques et de géolocalisation [420]; IA-RI-2025-003-OP, en vigueur le 5 décembre 2025, et son contenu [421]; Énoncé de principes (édition 2025), 12 principes, principe 11 sur l'IA agentique [379], et caractère contraignant de l'Énoncé pour les organismes publics (p. 178).
- p. 178 : Énoncé de politique de souveraineté numérique (février 2026) [422]; outils gouvernementaux [423]; absence de sanction de la CAI liée aux décisions automatisées [424]; rapport quinquennal de la CAI du 11 juin 2026 et ses 74 recommandations [425]; récidive à l'art. 92.1 ([18-23]).
- p. 178 : C-36, dépôt le 15 juin 2026, art. 62, 63, 113 et 114, plafond de 10 M$ ou 3 % [430, 431]; Directive sur la prise de décisions automatisée, champ « après le 1er avril 2020 » et EIA à 65 et 41 questions [432, 433].
- p. 179 : Guide fédéral sur l'IA agentique (2026) [353]; avis du BSIF sur les incidents « en vigueur depuis le 13 août 2021 » [434]; Ligne directrice IA de l'AMF (avril 2026, en vigueur le 1er mai 2027), non relue selon H.5; Loi concernant la cybersécurité (L.C. 2026, ch. 9, sanctionnée le 15 juin 2026), en particulier la présence des systèmes bancaires parmi les services critiques ([18-11]) [439]; état de C-22 au Sénat [440].
- p. 180 : règlement (UE) 2026/1744 du 8 juillet 2026 (numéro, date, entrée en vigueur le 27 juillet 2026), reports au 2 décembre 2027 et au 2 août 2028, nouvelles interdictions au 2 décembre 2026, bac à sable au 2 août 2027 (cités en partie à [57] plutôt qu'au texte; H.5 : EUR-Lex non relu) [57, 58, 443]; sort de l'art. 4 (maîtrise de l'IA) après l'omnibus ([18-10]).
- p. 182 : NIST AI RMF « en cours de révision » dans le cadre du plan d'action américain [99, 448].
