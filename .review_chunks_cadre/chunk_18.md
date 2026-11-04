# chunk_18 — pages PDF 171 à 182 (sur 283)



---
## [Page PDF 171]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Le principe est simple : on ne bâtit pas un programme de conformité par texte de loi. Chaque agent reçoit 
une classe de risque, et cette classe déclenche un ensemble de contrôles dont les preuves (traces, journal 
d’audit, évaluations d’impact, résultats d’évaluation) servent à la fois à la Loi 25, au règlement européen et 
aux référentiels volontaires. Les seuils, délais internes et fréquences de revue propres au cadre sont signalés 
comme tels.
12.1 Classes de risque des agents
La classe de risque mesure ce qui arrive si l’agent se trompe; elle détermine l’intensité de la gouvernance 
qui s’applique à lui.
Trois notions coexistent et ne se confondent pas. Le niveau d’autonomie (N0 à N4, section 8.1) dit jusqu’où 
l’agent agit sans approbation. Le palier d’outil (P0 à P3, section 8.3) dit ce que fait chaque outil. La classe 
de risque dit quelles conséquences un agent peut produire sur des personnes, sur l’entreprise ou sur des 
tiers. La classe fixe le plafond du niveau d’autonomie, et la règle la plus stricte entre classe, niveau et palier 
l’emporte (section 8.4).
Cette gradation répond à un constat partagé. Selon Gartner (communiqué du 26 mai 2026), appliquer une 
gouvernance uniforme à tous les agents mènera à des échecs; l’analyste recommande une gouvernance 
proportionnelle[95]. Le cadre de gouvernance de l’IA agentique de l’Infocomm Media Development Authority 
(IMDA, Singapour) désigne la portée des actions de l’agent, leur réversibilité et son niveau d’autonomie 
comme déterminants du risque[76]. La ligne directrice E-23 du BSIF suit la même logique pour les modèles : 
une cote de risque détermine l’intensité de la gouvernance, la fréquence des examens et l’autorité 
d’approbation[8]. Les quatre critères d’analyse du cadre (rayon d’impact, réversibilité, délai de détection et 
de récupération, observabilité reconstructive) sont décrits à la section 8.2.
Tableau 46 — Classes de risque des agents : critères, plafond d’autonomie et contrôles minimaux
Classe
Critères (un seul suffit)
Plafond 
d’autonomie
Contrôles minimaux
Revue
Élevée
Décision à effet important sur une per­
sonne (crédit, emploi, assurance, accès 
à un service essentiel); décision fondée 
exclusivement sur un traitement automa­
tisé de RP (art. 12.1 de la Loi sur le privé; 
art. 65.2 de la Loi sur l’accès pour les or­
ganismes publics); système à haut risque 
au sens du règlement européen sur l’IA; 
action financière, juridique ou irréversible 
au-delà des seuils déclarés; renseigne­
ments personnels sensibles
N2
EFVP et évaluation d’impact 
unifiée (section 12.9); 
équipe rouge avant pro­
duction (section 9.9); ho­
mologation par le comi­
té d’architecture et des 
risques agentiques; P3 tou­
jours soumis à une appro­
bation hors bande
Semestrielle
Modérée
RP non sensibles ou données confiden­
tielles; actions P2 réversibles ou compen­
sables en production; échanges avec des 
partenaires, des clients ou le public
N3, avec des 
seuils plus bas et 
une revue a pos­
teriori renforcée
EFVP si l’agent traite des 
RP; revue de sécurité; 
exercice d’équipe rouge 
avant production puis an­
nuel (EXIG-SEC-23); évalua­
tion continue (section 10.4)
Annuelle
Faible
Données publiques ou internes non 
confidentielles; lecture seule ou actions 
internes réversibles; aucun effet sur une 
personne
N3; N4 sur déci­
sion du comité
Autoévaluation documen­
tée; évaluation continue; 
inscription au registre
Annuelle
Plafonds repris d’EXIG-CON-02, qui fait foi. Choix du cadre. Les fréquences de revue sont des valeurs par 
défaut que la déclaration de tolérance au risque peut resserrer (EXIG-CON-17).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 171 sur 283


---
## [Page PDF 172]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Un seul critère suffit : la classe retenue est la plus élevée dont un critère est rempli, jamais une moyenne. 
Les conséquences ne se compensent pas : un agent en lecture seule qui consulte des dossiers médicaux reste 
de classe élevée, parce qu’une fuite ne se répare pas.
EXEMPLE
Un agent de préqualification de prêts personnels lit des données et produit un avis « admissible » ou 
« non admissible ». Si cet avis est communiqué au client sans examen réel par un employé, il s’agit d’une 
décision fondée exclusivement sur un traitement automatisé : l’agent est de classe élevée et plafonné à 
N2, alors que tous ses outils sont de palier P1. À l’inverse, un agent qui reclasse des billets d’assistance 
internes en écriture réversible (P2), sans RP, relève de la classe modérée et peut atteindre N3 sous des 
seuils déclarés.
EXIG-CON-01 · DOIT
Classe de risque attribuée avant l’inscription
Chaque agent DOIT recevoir une classe de risque (faible, modérée ou élevée) selon le tableau 46 avant 
son inscription au registre (section 11.4). La classe retenue est la plus élevée dont au moins un critère est 
rempli; la justification est consignée dans la fiche d’agent et validée par l’équipe risques et conformité.
Pourquoi : une moyenne des critères masquerait la conséquence la plus grave, qui seule commande les contrôles.
EXIG-CON-02 · DOIT
Plafond d’autonomie par classe
Le niveau d’autonomie déclaré au registre DOIT respecter le plafond de la classe : N2 pour la classe 
élevée, N3 pour les classes modérée et faible. N4 n’est permis qu’à un agent de classe faible, sur décision 
consignée du comité d’architecture et des risques agentiques. Un agent NE DOIT PAS opérer au niveau 
NX, quelle que soit sa classe.
Pourquoi : les plafonds par classe sont un choix du cadre; pour les systèmes à haut risque, le règlement européen exige 
des mesures de supervision humaine proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation 
(art. 14(3))[412].
EXIG-CON-03 · DOIT
Réévaluation à chaque changement significatif
La classe de risque DOIT être réévaluée, avant la mise en production du changement, lors de tout 
changement de modèle ou de fournisseur, d’outil ou de palier d’outil, de catégorie de données, de finalité, 
de population visée ou de lieu de traitement. La même réévaluation déclenche la mise à jour de l’EFVP 
et de l’évaluation d’impact unifiée (EXIG-CON-26).
Pourquoi : le guide de la Commission d’accès à l’information (CAI) demande de mettre à jour une EFVP lorsque le 
projet change, et E-23 fait des modifications d’un modèle et de ses données un déclencheur de revue indépendante[8, 
413].
12.2 Loi 25 et droit québécois
Cette section traduit en exigences les obligations québécoises qui touchent directement les agents : évalua­
tion préalable, communication hors Québec, consentement, décisions automatisées, conservation, secteur 
public et sanctions.
La Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (L.Q. 
2021, c. 25, « Loi 25 ») a été sanctionnée le 22 septembre 2021. Elle est entrée en vigueur par étapes : le 22 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 172 sur 283


---
## [Page PDF 173]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
septembre 2022 pour le responsable de la protection des renseignements personnels (RPRP) et les incidents 
de confidentialité[56], le 22 septembre 2023 pour l’essentiel[56], et le 22 septembre 2024 pour le droit à la 
portabilité (quelques dispositions accessoires l’étant dès le 22 septembre 2021)[7, 56]. Elle modifie la Loi sur la 
protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1, « Loi sur le privé ») et la Loi 
sur l’accès aux documents des organismes publics et sur la protection des renseignements personnels (RLRQ, c. 
A-2.1, « Loi sur l’accès »). Sauf mention contraire, les articles cités sont ceux de la Loi sur le privé.
Un point de départ s’impose : l’entreprise demeure responsable des RP qu’elle détient, même lorsqu’un 
fournisseur de modèles, de plateforme d’agents ou de serveur MCP les conserve ou les traite pour elle (art. 
1 et 3.1)[56]; selon la CAI, elle conserve aussi ses obligations en cas d’incident[414]. La loi ne connaît pas de 
responsabilité « conjointe » : le fournisseur est un mandataire lié par un contrat écrit (art. 18.3)[56].
Tableau 47 — Articles de la Loi sur le privé qui touchent les agents
Article
Obligation (résumé)
Application aux agents (interprétation 
du cadre)
3.1
La personne ayant la plus haute autorité exerce la fonction de 
responsable de la protection des RP, délégable par écrit; titre et coor­
données publiés sur le site Web.
Le responsable est consulté sur chaque 
agent qui traite des RP et participe à 
l’homologation des agents de classe éle­
vée (section 11.1).
3.2
Politiques et pratiques de gouvernance (conservation, destruction, 
rôles, plaintes) approuvées par le responsable; information publiée en 
termes simples et clairs.
Les règles de conservation des traces et 
des mémoires d’agents font partie de ces 
politiques.
3.3
EFVP pour tout projet d’acquisition, de développement ou de refonte 
d’un système d’information ou de prestation électronique de services 
impliquant des RP; responsable consulté dès le début; portabilité 
permise.
Tout nouvel agent, et tout changement 
de modèle ou d’outils touchant des RP 
(EXIG-CON-04).
3.5 à 3.8
Incidents de confidentialité : mesures pour diminuer le risque; avis 
« avec diligence » à la CAI et aux personnes en cas de risque de 
préjudice sérieux; registre de tous les incidents.
Réponse aux incidents agentiques (section 
12.8).
8.1
Informer au préalable du recours à une technologie permettant 
d’identifier, de localiser ou de profiler une personne, et des moyens 
d’activer ces fonctions.
Un agent qui évalue le rendement au 
travail, la situation économique, la santé, 
les préférences ou le comportement d’une 
personne fait du profilage.
9.1
Produit ou service technologique offert au public et doté de para­
mètres de confidentialité : plus haut niveau de confidentialité par 
défaut.
Mémoire persistante, partage de conver­
sations et personnalisation désactivés par 
défaut dans les agents offerts au public.
11
RP à jour et exacts au moment d’une décision; conservés au moins un 
an après celle-ci.
Conservation des éléments de décision 
(EXIG-CON-09).
12
Utilisation limitée aux fins de la collecte, sauf consentement (exprès 
s’il est sensible) ou exception prévue; la prospection commerciale ou 
philanthropique n’est pas une fin compatible.
Aucune réutilisation de conversations ou 
de traces à d’autres fins sans base légale 
documentée (EXIG-CON-06).
12.1
Décision fondée exclusivement sur un traitement automatisé : infor­
mer, expliquer sur demande, permettre la rectification et des obser­
vations à un membre du personnel en mesure de réviser la décision.
EXIG-CON-07, EXIG-CON-08 et 
EXIG-CON-21.
14
Consentement manifeste, libre, éclairé, donné à des fins spécifiques 
et demandé pour chacune d’elles, en termes simples et clairs; présen­
té distinctement s’il est demandé par écrit.
Consentements séparés pour l’inférence et 
pour l’entraînement de modèles.
17
Avant toute communication hors Québec : EFVP tenant compte de 
la sensibilité, de la finalité, des mesures de protection et du régime 
juridique de l’État de destination; protection adéquate; entente écrite.
Tout modèle, serveur MCP, agent déléga­
taire ou magasin de mémoire situé hors 
Québec (EXIG-CON-05).
18.3
Mandat ou contrat de service écrit : mesures de confidentialité, usage 
limité au mandat, aucune conservation après l’expiration, avis sans 
délai de toute violation, droit de vérification.
Clauses fournisseurs (section 13.3), dont 
l’interdiction d’entraîner des modèles sur 
les données confiées.
23
Destruction ou anonymisation une fois les fins accomplies, selon 
le Règlement sur l’anonymisation; un renseignement dépersonnalisé 
demeure un RP.
Cycle de vie des mémoires et des index 
vectoriels (EXIG-CON-10).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 173 sur 283


---
## [Page PDF 174]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Article
Obligation (résumé)
Application aux agents (interprétation 
du cadre)
27 et 32
Accès et copie; transcription écrite et intelligible; depuis le 22 sep­
tembre 2024, portabilité des renseignements informatisés recueillis 
auprès de la personne; réponse écrite au plus tard dans les 30 jours.
Les inférences produites par un agent sont 
visées par le droit d’accès, mais pas par la 
portabilité.
90.1 et 
suiv., 91, 
93.1
Sanctions administratives pécuniaires, infractions pénales, dom­
mages-intérêts punitifs.
Voir « Sanctions et recours » ci-dessous.
Source des obligations : L.Q. 2021, c. 25[56]. La colonne de droite est une interprétation du cadre.
Évaluation des facteurs relatifs à la vie privée
L’EFVP est obligatoire dans deux situations qui visent directement les agents : tout projet d’acquisition, de 
développement ou de refonte d’un système d’information ou de prestation électronique de services impli­
quant des RP (art. 3.3), et toute communication de RP à l’extérieur du Québec (art. 17)[413]. Elle ne vise donc 
pas « tout système » en exploitation, mais tout projet qui en crée ou en modifie un. La loi exige qu’elle soit 
proportionnée à la sensibilité, à la finalité, à la quantité, à la répartition et au support des renseignements, 
sans prescrire de forme ni de signature[56]. Le guide de la CAI (version 3.1, avril 2024) est recommandé : il 
prévoit une évaluation de la conformité, une analyse des risques avec stratégies d’atténuation, un inventaire 
et un « parcours » des renseignements, puis une réévaluation de la nécessité et de la proportionnalité; il cite 
« améliorer un modèle d’intelligence artificielle » et « rendre une décision automatisée » parmi les finalités 
à examiner[413].
Pour un agent, le parcours des renseignements est plus long que pour une application classique : invite, 
contexte récupéré, appels d’outils MCP, délégations A2A, mémoire, traces. L’EFVP du cadre inventorie donc 
les RP outil par outil et délégation par délégation. La loi n’exige pas d’évaluer les biais dans l’EFVP; le cadre 
l’exige pour tout agent qui décide ou recommande à l’égard d’une personne, dans le prolongement de la 
recommandation de la CAI (dès 2020) d’imposer, pour les systèmes de décision automatisée, une EFVP et 
une analyse d’impact algorithmique couvrant tous les droits fondamentaux, et de celle du gouvernement 
du Québec pour les décisions automatisées[318, 415].
EXIG-CON-04 · DOIT
EFVP avant tout projet d’agent impliquant des RP
Tout projet d’acquisition, de développement ou de refonte d’un agent impliquant des RP DOIT faire 
l’objet d’une EFVP terminée avant le passage en pilote. Le responsable de la protection des RP DOIT 
être consulté dès le début du projet. L’EFVP DOIT inventorier les RP par outil, par délégation et par 
mémoire, et DOIT comprendre une analyse des biais lorsque l’agent décide ou recommande à l’égard 
d’une personne (exigence propre au cadre).
Pourquoi : article 3.3 de la Loi sur le privé, qui ne prescrit pas le contenu de l’EFVP; l’analyse des biais est une 
exigence propre au cadre, appuyée par les orientations de la CAI (discrimination parmi les conséquences à évaluer; 
analyse d’impact algorithmique recommandée au législateur), non une obligation légale[56, 413, 415].
Communication hors Québec et lois étrangères
Confier à un fournisseur situé hors Québec la tâche d’utiliser ou de conserver des RP pour le compte de 
l’entreprise, par exemple en appelant l’API d’un modèle hébergé ailleurs, relève de l’article 17. L’entreprise 
réalise d’abord une EFVP qui tient compte de la sensibilité des renseignements, de la finalité, des mesures 
de protection, y compris contractuelles, et du régime juridique de l’État de destination. La communication 
est permise si les renseignements bénéficient d’une protection adéquate, et elle fait l’objet d’une entente 
écrite[56, 416]. Le texte de l’article 17 vise toute communication à l’extérieur du Québec et ne distingue pas 
les provinces; le cadre l’interprète donc comme incluant l’Ontario : un index vectoriel hébergé dans une 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 174 sur 283


---
## [Page PDF 175]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
région infonuagique en Ontario déclenche l’article 17 au même titre qu’un hébergement aux États-Unis 
(interprétation du cadre)[56, 416].
La résidence des données ne règle pas tout. Le CLOUD Act américain (2018) oblige les fournisseurs assujettis 
au droit américain à préserver et à divulguer les données en leur possession, sous leur garde ou sous 
leur contrôle, qu’elles soient situées aux États-Unis ou à l’étranger[417]. Le cadre fédéral de souveraineté 
numérique (novembre 2025) constate que le stockage au Canada ne place pas à lui seul les données hors de 
la compétence de tribunaux étrangers, tout en notant que le gouvernement du Canada n’a relevé aucun cas 
documenté de gouvernement étranger cherchant à accéder aux données d’entreprises canadiennes détenues 
par des fournisseurs[418]. Le risque est donc réel, mais à pondérer dans l’EFVP. Le cadre retient comme 
mesures compensatoires le chiffrement à clés gérées par l’entreprise et, pour les RP sensibles, le recours à 
des fournisseurs sous compétence canadienne.
EXIG-CON-05 · DOIT
Cartographie des lieux de traitement
La fiche de chaque agent DOIT indiquer le lieu de traitement (province ou pays, et fournisseur) de 
chaque modèle appelé, serveur MCP, agent délégataire et magasin de mémoire ou de traces. Tout flux 
de RP vers l’extérieur du Québec, y compris vers une autre province, DOIT être couvert par une EFVP 
au sens de l’article 17 et par une entente écrite avant sa mise en service; la passerelle de modèles DOIT 
refuser toute route qui n’est pas couverte.
Pourquoi : l’article 17 vise toute communication « à l’extérieur du Québec », que le cadre interprète comme incluant 
les autres provinces, et un routage dynamique entre modèles peut créer un transfert que personne n’a décidé[56, 416].
Consentement et finalités
Un RP ne peut servir qu’aux fins pour lesquelles il a été recueilli, sauf consentement (exprès s’il est sensible) 
ou exception prévue par la loi : fins compatibles ayant un lien pertinent et direct avec les fins initiales, 
bénéfice manifeste de la personne, prévention de la fraude, fourniture d’un service demandé, recherche 
ou statistiques avec des renseignements dépersonnalisés. La prospection commerciale ou philanthropique 
n’est jamais une fin compatible (art. 12)[56]. Le consentement doit être manifeste, libre, éclairé et donné à des 
fins spécifiques; il est demandé pour chacune de ces fins, en termes simples et clairs (art. 14)[56, 419]. La loi 
n’emploie pas la notion de consentement « groupé », mais l’exigence d’un consentement par finalité conduit 
le cadre à séparer le consentement à l’inférence (rendre le service demandé) de celui à l’entraînement ou à 
l’ajustement fin de modèles.
EXIG-CON-06 · DOIT
Finalité vérifiée avant toute réutilisation
Toute réutilisation de conversations, de traces, de mémoires ou de sorties d’agents à une autre fin que 
celle de la collecte, notamment l’entraînement ou l’ajustement fin de modèles, DOIT reposer sur un 
consentement distinct ou sur une exception légale documentée. Les données DOIVENT porter une 
étiquette de finalité que le service de politiques de la passerelle d’agents (section 9.4) DOIT vérifier 
avant toute transmission vers un usage secondaire.
Pourquoi : articles 12 et 14 de la Loi sur le privé; un contrôle technique empêche qu’une équipe réutilise de bonne 
foi des traces pour une fin non couverte.
Décisions fondées exclusivement sur un traitement automatisé
L’article 12.1 s’applique lorsqu’une décision concernant une personne est fondée exclusivement sur un 
traitement automatisé de ses RP. L’entreprise doit l’en informer au plus tard au moment où elle l’informe 
de la décision. À sa demande, elle doit aussi l’informer des RP utilisés, des raisons et des principaux facteurs 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 175 sur 283


---
## [Page PDF 176]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
et paramètres ayant mené à la décision, ainsi que de son droit de faire rectifier ces renseignements. La 
personne doit avoir l’occasion de présenter ses observations à un membre du personnel en mesure de 
réviser la décision[56]. Le défaut d’informer la personne ou de lui permettre de présenter ses observations 
est expressément un motif de sanction administrative pécuniaire (art. 90.1, par. 5°)[56, 317].
Quand une décision est-elle « exclusivement » automatisée? Selon l’interprétation du gouvernement du 
Québec pour l’article 65.2 de la Loi sur l’accès, rédigé comme l’article 12.1 et que le cadre transpose par 
analogie à ce dernier, c’est le cas lorsqu’aucune personne physique n’a exercé un contrôle important. Une 
intervention humaine mineure, sans effet réel sur le résultat, ne fait pas échapper à l’obligation; en revanche, 
un outil d’aide à la décision qui fournit des éléments à un employé qui décide lui-même n’est pas visé[318]. 
Pour un agent de niveau N2, la conséquence est concrète : un bouton « Approuver » cliqué sans information, 
sans temps et sans autorité réelle ne transforme pas la décision de l’agent en décision humaine. Le même 
document précise qu’il n’est pas requis de divulguer l’algorithme : le mot « principaux » limite l’explication 
aux facteurs déterminants et à leur importance relative, ce qui protège les renseignements industriels et 
commerciaux.
DROIT APPLICABLE
Article 12.1 de la Loi sur le privé (article 65.2 de la Loi sur l’accès pour les organismes publics) : avis au 
plus tard au moment de la décision; sur demande, RP utilisés, raisons, principaux facteurs et paramètres, 
droit de rectification; observations à un membre du personnel en mesure de réviser. L’article 12.1 ne fixe 
aucun délai de réponse : le délai de 30 jours de l’article 32 vise les demandes d’accès et de rectification. 
Les RP utilisés pour décider sont conservés au moins un an après la décision (art. 11)[56].
EXIG-CON-07 · DOIT
Avis et explication des décisions automatisées
Pour toute décision concernant une personne fondée exclusivement sur le traitement automatisé de ses 
RP par un agent, le système DOIT : informer la personne au plus tard au moment où la décision lui 
est communiquée; pouvoir produire sur demande les RP utilisés, les raisons et les principaux facteurs 
et paramètres de la décision avec leur importance relative; indiquer le droit de rectification; offrir un 
canal pour présenter des observations à un membre du personnel nommément désigné et en mesure 
de réviser la décision. Le délai de réponse à ces observations DOIT être d’au plus 30 jours (choix du 
cadre; l’article 12.1 ne fixe aucun délai).
Pourquoi : article 12.1; le défaut constitue un motif de sanction administrative pécuniaire[56, 317].
EXIG-CON-08 · NE DOIT PAS
Aucune approbation nominale
Une approbation humaine NE DOIT PAS être considérée comme retirant le caractère exclusivement 
automatisé d’une décision si l’approbateur ne dispose pas de l’une ou l’autre de ces conditions  : 
l’information sur la décision et ses facteurs, le temps nécessaire pour l’examiner, l’autorité de la 
modifier ou de l’annuler (voir aussi EXIG-AUT-23). À défaut d’une seule d’entre elles, les obligations 
de l’EXIG-CON-07 s’appliquent, et le taux d’approbation sans modification est suivi par approbateur 
(section 8.7).
Pourquoi : selon l’interprétation gouvernementale, une intervention humaine mineure, sans effet réel sur le résultat, 
ne fait pas échapper à l’obligation[318].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 176 sur 283


---
## [Page PDF 177]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
EXIG-CON-09 · DOIT
Conservation des éléments de décision
Les éléments de toute décision d’agent touchant une personne DOIVENT être conservés au moins 
un an après la décision, sous une forme qui permet de répondre aux demandes prévues aux articles 
12.1 et 27 : RP en entrée, versions de l’agent, du modèle et des outils, facteurs retenus et approbations. 
L’exportation de traces techniques est un moyen; la personne reçoit une transcription écrite et intel­
ligible.
Pourquoi : l’article 11 exige de conserver au moins un an les RP utilisés pour décider; la conservation des versions 
et des facteurs va au-delà du minimum légal pour rendre l’explication possible[56].
Conservation, mémoire et destruction
Une fois les fins accomplies, l’entreprise doit détruire le renseignement ou l’anonymiser pour des fins sé­
rieuses et légitimes, selon les critères du Règlement sur l’anonymisation des renseignements personnels (art. 
23); un renseignement dépersonnalisé, notion définie à l’article 12, demeure un renseignement personnel. La 
CAI estime en outre que certaines données, dont les données génétiques, biométriques et de géolocalisation, 
ne peuvent être adéquatement anonymisées[56, 420]. Pour un agent, la règle vise la mémoire épisodique et 
sémantique (section 5.5), les index vectoriels et les traces. Un plongement vectoriel (embedding) calculé à 
partir d’un RP n’est pas anonyme du seul fait qu’il est illisible pour un humain : le cadre le traite comme 
un RP.
EXIG-CON-10 · DOIT
Durée de vie des mémoires et des traces
Chaque magasin de mémoire, index vectoriel et dépôt de traces d’un agent DOIT avoir une durée de 
conservation liée à sa finalité, inscrite dans la fiche d’agent et appliquée automatiquement. À l’échéance, 
sous réserve des délais de conservation prévus par la loi (EXIG-CON-09) et du gel des preuves d’un 
incident (EXIG-CON-23), les données DOIVENT être détruites ou anonymisées selon le règlement; les 
plongements calculés à partir de RP suivent le même régime que les RP d’origine.
Pourquoi : article 23 de la Loi sur le privé; une mémoire sans échéance accumule des RP au-delà de leur finalité.
Secteur public québécois
Les organismes publics appliquent les dispositions équivalentes de la Loi sur l’accès : décisions fondées 
exclusivement sur un traitement automatisé (art. 65.2), EFVP (art. 63.5), règles de gouvernance (art. 63.3), 
incidents de confidentialité (art. 63.8 à 63.11) et communication hors Québec (art. 70.1); l’article 63.1 porte 
sur les mesures de sécurité[56, 318]. Trois textes gouvernementaux s’y ajoutent :
• l’indication d’application IA-RI-2025-003-OP sur l’IA générative, en vigueur le 5 décembre 2025, exige 
notamment une EFVP dès la conception de tout système d’IA générative, même sans RP apparent, la clas­
sification préalable des données numériques gouvernementales, des essais de fiabilité, une supervision 
humaine proportionnée à l’autonomie, l’interdiction d’entrer des renseignements confidentiels dans un 
système d’IA générative public et, pour les données confidentielles, la préférence pour des fournisseurs 
québécois ou canadiens hébergés au Québec ou au Canada[421];
• l’Énoncé de principes pour une utilisation responsable de l’IA par les organismes publics (édition 2025) 
compte 12 principes; le principe 11 vise expressément l’IA agentique et exige des mécanismes permettant 
la validation, l’intervention humaine ou l’arrêt des actions du système, par exemple des validations avant 
certaines actions critiques et des mécanismes d’arrêt d’urgence[379];
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 177 sur 283


---
## [Page PDF 178]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
• l’Énoncé de politique de souveraineté numérique et d’approvisionnement en TI (février 2026) oriente 
l’État vers l’hébergement souverain, des centres de données sous juridiction québécoise et le logiciel 
libre[422].
L’indication d’application et l’Énoncé de principes lient les organismes publics; l’énoncé de politique de 
souveraineté numérique énonce une orientation de l’État. Pour les entreprises privées, le cadre les retient 
comme référence de bonne pratique. Le gouvernement met aussi à la disposition des organismes des outils 
officiels : analyse des décisions automatisées, modèle de registre des incidents, analyse du régime juridique 
d’une communication hors Québec et schéma de décision sur l’EFVP[423]. Ils constituent de bons points de 
départ pour les gabarits du cadre.
Sanctions et recours
La CAI peut imposer une sanction administrative pécuniaire d’au plus 50 000 $ à une personne physique et, 
à une entreprise, d’au plus 10 000 000 $ ou 2 % du chiffre d’affaires mondial de l’exercice précédent, selon 
le montant le plus élevé (art. 90.12)[56]; un engagement accepté par la CAI et respecté écarte la sanction[317]. 
Les infractions pénales (art. 91) entraînent une amende de 5 000 $ à 100 000 $ pour une personne physique 
et, pour une entreprise, de 15 000 $ à 25 000 000 $ ou 4 % du chiffre d’affaires mondial, selon le montant 
le plus élevé; les amendes sont portées au double en cas de récidive. Une atteinte illicite intentionnelle ou 
résultant d’une faute lourde donne en outre droit à des dommages-intérêts punitifs d’au moins 1 000 $ (art. 
93.1)[56]. La page des sanctions de la CAI et son rapport annuel 2024-2025 ne font état d’aucune sanction liée 
aux décisions automatisées : le risque tient aux plafonds légaux, non à des précédents[424].
Le droit évolue. Dans son rapport quinquennal déposé le 11 juin 2026, la CAI formule 74 recommandations, 
dont une meilleure prise en compte des inférences algorithmiques et une meilleure définition du processus 
d’EFVP[425]. Le cadre traite dès maintenant les inférences produites par les agents comme des RP à gouverner.
12.3 Cadre fédéral et sectoriel canadien
Cette section situe les obligations fédérales et sectorielles qui s’ajoutent au droit québécois, et distingue ce 
qui est en vigueur de ce qui n’est encore qu’un projet.
Tableau 48 — Textes fédéraux et sectoriels canadiens : statut au 27 octobre 2026 et effet sur les agents
Texte
Statut
Ce qu’il implique pour les agents
LPRPDE (Loi sur la protection 
des renseignements personnels 
et les documents électroniques)
En vigueur
Atteinte présentant un risque réel de préjudice grave : déclaration 
au Commissariat et avis aux personnes « dès que possible » 
(LPRPDE, par. 10.1(2) et (6)); toutes les atteintes sont consignées, 
registre conservé 24 mois[426, 427].
Projet de loi C-27, dont la Loi 
sur l’intelligence artificielle et 
les données (LIAD)
Resté à l’étape du comité 
à la fin de la session, le 
6 janvier 2025; mort au 
Feuilleton à la proroga­
tion[428, 429]
Aucune obligation : la LIAD n’existe pas.
Projet de loi C-36, Loi sur la 
protection de la vie privée et 
des données des consomma­
teurs
Déposé le 15 juin 2026; 
deuxième lecture; non en 
vigueur[430]
Viserait tout système décisionnel automatisé qui appuie ou rem­
place le jugement humain; lorsqu’il sert à faire des prédictions, 
des recommandations ou des décisions pouvant avoir un effet 
juridique ou un effet important semblable : usage décrit dans 
l’information rendue publique (art. 62), explication sur demande 
et observations écrites à un employé pouvant réviser (art. 63). Les 
sanctions administratives (art. 113 et 114) ne visent que certaines 
dispositions, dont l’art. 62(1) mais pas l’art. 63; le plafond est le 
plus élevé de 10 M$ et de 3 % des revenus mondiaux bruts[431].
Directive sur la prise de déci­
sions automatisée du Secréta­
riat du Conseil du Trésor du 
Canada (SCT) et évaluation de 
l’incidence algorithmique (EIA)
S’applique à 
l’administration fédérale
Systèmes développés ou acquis après le 1er avril 2020 qui 
remplacent ou appuient le jugement humain dans des déci­
sions administratives; EIA obligatoire (65 questions de risque, 41 
d’atténuation, niveaux d’incidence I à IV), faite au début de la 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 178 sur 283


---
## [Page PDF 179]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Texte
Statut
Ce qu’il implique pour les agents
conception, mise à jour avant la production, résultats publiés[432, 
433].
Guide sur l’utilisation de l’IA 
agentique (gouvernement du 
Canada, 2026)
Orientation pour 
l’administration fédérale
Autonomie bornée, lecture seule par défaut, points de contrôle 
humains pour les actions qui modifient l’état des systèmes, pro­
priétaire humain désigné, identifiant unique par agent, journalisa­
tion dans un système que l’agent ne peut modifier, coupe-circuit 
externe, texte externe traité comme des données[353].
Ligne directrice E-23 du BSIF, 
Gestion du risque de modèle
Publiée le 11 septembre 
2025; en vigueur le 1er 
mai 2027 pour les ins­
titutions financières fédé­
rales[8]
« Modèle » inclut les méthodes d’IA et d’apprentissage automa­
tique (la prise de décision autonome relève des principes de 
surveillance); inventaire d’entreprise des modèles à risque non né­
gligeable, y compris ceux des fournisseurs, cote de risque, revue 
indépendante, surveillance de la dérive.
Avis du BSIF sur le signalement 
des incidents liés à la technolo­
gie et à la cybersécurité
En vigueur depuis le 13 
août 2021[434]
Signalement écrit au BSIF dans les 24 heures, ou plus tôt si pos­
sible.
Ligne directrice B-13 du BSIF, 
Gestion des risques liés à la 
technologie et au cyberrisque
Publiée en juillet 2022 
(lettre du BSIF du 13 
juillet 2022); en vigueur 
depuis le 1er janvier 
2024[435, 436]
Gestion des identités et des accès fondée sur le risque (authen­
tification multifacteur, accès privilégiés, moindre privilège, attesta­
tion périodique, surveillance des comptes de service); journalisa­
tion continue et centralisée; incidents d’origine tierce visés.
Code de conduite volontaire 
sur l’IA générative avancée (In­
novation, Sciences et Dévelop­
pement économique Canada, 
ISDE)
Septembre 2023; volon­
taire[437]
Six résultats : responsabilisation, sécurité, justice et équité, trans­
parence, surveillance humaine, validité et robustesse.
Principes des commissaires à la 
protection de la vie privée pour 
une IA générative responsable
7 décembre 2023, cosi­
gnés par la CAI[438]
Neuf principes; menaces propres à l’IA (injection, inversion de 
modèle, débridage); mécanisme de contestation avec révision hu­
maine pour les décisions assistées par l’IA.
Trois conséquences pratiques en découlent. D’abord, une institution financière fédérale devrait traiter 
chaque agent comme un compte de service privilégié, dans l’esprit de B-13 : identité propre, accès minimal, 
surveillance (section 9.2). Ensuite, le projet C-36 viserait aussi les décisions partiellement automatisées; le 
cadre conçoit donc l’explicabilité des agents pour couvrir les deux régimes, sans attendre l’adoption du 
projet (EXIG-CON-21). Enfin, le guide fédéral sur l’IA agentique converge avec les exigences des chapitres 8 
à 10. Les institutions financières de compétence québécoise intègrent en outre à leur registre de conformité 
les attentes de l’Autorité des marchés financiers (AMF) en matière d’IA, énoncées dans sa Ligne directrice 
sur l’utilisation de l’intelligence artificielle (version d’avril 2026, en vigueur le 1er mai 2027), que le présent 
cadre ne reprend pas.
La veille porte aussi sur deux textes connexes : la Loi concernant la cybersécurité (ancien projet de loi C-8), 
sanctionnée le 15 juin 2026 (L.C. 2026, ch. 9), et le projet de loi C-22 sur l’accès légal, à l’étude au Sénat en 
octobre 2026[439, 440]. Leur effet sur les fournisseurs de télécommunications et d’infonuagique utilisés par les 
agents est suivi par le processus de la section 11.7.
EXIG-CON-11 · DOIT
Régimes applicables inscrits à la fiche
La fiche de chaque agent DOIT énumérer les régimes juridiques et sectoriels qui s’appliquent à lui (Loi 
sur le privé ou Loi sur l’accès, LPRPDE, règlement européen sur l’IA, lignes directrices du BSIF, directive 
fédérale, textes gouvernementaux québécois) et, pour chacun, les obligations retenues et l’exigence 
du cadre qui y répond. L’équipe risques et conformité valide cette liste à l’homologation et à chaque 
réévaluation (EXIG-CON-03).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 179 sur 283


---
## [Page PDF 180]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Pourquoi : un même agent peut relever de plusieurs régimes dont les seuils et les délais diffèrent; seule une liste 
explicite permet d’appliquer le plus exigeant.
EXIG-CON-12 · DOIT
Arrimage à E-23 pour les institutions financières fédérales
Une institution financière fédérale DOIT, au plus tard le 1er mai 2027, inscrire chaque agent et chaque 
modèle qu’il utilise, y compris ceux des fournisseurs, à l’inventaire des modèles attendu par la ligne 
directrice E-23 (le cadre étend l’inscription à chaque agent et à chaque modèle utilisé), avec propriétaire, 
cote de risque, version et état de validation. Un changement de modèle, de fournisseur ou de données 
d’entrée déclenche la revue prévue par E-23.
Pourquoi : E-23 inclut les méthodes d’IA et d’apprentissage automatique dans sa définition de modèle, traite de la 
prise de décision autonome dans ses principes de surveillance et exige un inventaire d’entreprise[8].
12.4 Règlement européen sur l’IA
Cette section indique quand le règlement (UE) 2024/1689 (RIA) s’applique à une entreprise canadienne et 
ce qu’il exige d’un agent à haut risque.
Portée : l’utilisation des sorties dans l’Union
Le RIA ne s’applique pas parce qu’une entreprise « opère en Europe ». Selon l’article 2(1), il vise notamment 
les fournisseurs qui mettent un système d’IA sur le marché ou en service dans l’Union, où qu’ils soient 
établis, les déployeurs établis ou situés dans l’Union, ainsi que les fournisseurs et déployeurs établis dans 
un pays tiers lorsque les sorties produites par le système sont utilisées dans l’Union[61, 441]. Un agent exploité 
à Montréal dont les recommandations servent à une filiale européenne peut donc être visé. Le RIA définit 
le système d’IA comme un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, 
qui déduit des entrées qu’il reçoit la manière de générer des sorties pouvant influencer des environnements 
physiques ou virtuels (art. 3(1)); le déployeur est celui qui l’utilise sous sa propre autorité (art. 3(4))[62]. Le 
cadre considère tout agent comme un système d’IA au sens de cette définition.
Les systèmes à haut risque relèvent de l’article 6 et des annexes I et III. L’annexe III couvre huit domaines : 
biométrie; infrastructures critiques; éducation et formation; emploi et gestion des travailleurs; accès aux 
services essentiels privés et publics, dont l’évaluation de la solvabilité et la tarification en assurance vie 
et maladie; répression; migration, asile et contrôle des frontières; administration de la justice et processus 
démocratiques[442].
Calendrier modifié par le règlement (UE) 2026/1744
Le RIA est entré en vigueur le 1er août 2024. Les pratiques interdites s’appliquent depuis le 2 février 2025, 
les règles sur les modèles d’IA à usage général depuis le 2 août 2025, et l’application générale, dont les 
obligations de transparence de l’article 50, depuis le 2 août 2026[57]. Le règlement (UE) 2026/1744 du 8 juillet 
2026, dit « omnibus numérique sur l’IA », en vigueur depuis le 27 juillet 2026, a reporté les obligations du 
haut risque : au 2 décembre 2027 pour les systèmes de l’annexe III et au 2 août 2028 pour ceux de l’annexe 
I (produits réglementés)[58, 443]. Il ajoute des interdictions applicables le 2 décembre 2026 (hypertrucages 
sexuels non consentis, matériel d’abus pédosexuel) et prévoit au moins un bac à sable réglementaire de l’IA 
opérationnel dans chaque État membre au 2 août 2027[57].
ATTENTION
Un report n’est pas un moratoire. Le règlement (UE) 2026/1744 ne suspend ni les pratiques interdites 
ni les obligations des modèles d’IA à usage général[443]. Surtout, les journaux et la documentation d’un 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 180 sur 283


---
## [Page PDF 181]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
agent ne se reconstituent pas après coup : un agent conçu en 2026 sans eux ne sera pas conforme en 
décembre 2027.
Tableau 49 — Articles du règlement européen sur l’IA et réponse du cadre
Article
Exigence (résumé)
Réponse du cadre
2
Portée : fournisseurs et déployeurs, y compris hors Union lorsque 
les sorties y sont utilisées.
Applicabilité consignée dans la fiche 
(EXIG-CON-13).
6, annexes I 
et III
Classification des systèmes à haut risque.
Classe élevée d’office (EXIG-CON-01 et 
EXIG-CON-13).
9
Système de gestion des risques continu et itératif sur tout le cycle 
de vie.
Classe de risque et réévaluations 
(EXIG-CON-01, EXIG-CON-03); cycle de vie 
(section 11.5).
12
Enregistrement automatique des événements pendant toute la du­
rée de vie.
Traçage (section 10.1) et journal d’audit (sec­
tion 10.3); la signature et l’enregistrement à 
cinq éléments sont des choix du cadre, au-
delà du minimum légal.
13
Transparence et notice d’utilisation destinées aux déployeurs.
Fiche d’agent (annexe B) et carte d’agent re­
mises aux équipes qui déploient l’agent.
14
Supervision humaine effective : comprendre le système, rester 
conscient du biais d’automatisation, ignorer ou inverser une sortie, 
interrompre le système et le mettre dans un état sûr.
Approbation vérifiable (section 8.5), lutte 
contre l’approbation machinale (section 8.7), 
coupe-circuit (section 7.8).
15
Exactitude, robustesse et cybersécurité.
Évaluation continue (section 10.4) et sécurité 
(chapitre 9).
25
Un déployeur devient fournisseur s’il appose son nom, modifie 
substantiellement le système ou en change la destination; accord 
écrit avec les tiers fournisseurs de composants intégrés (25(4)), 
sauf pour les outils, services et composants rendus publics sous 
licence libre et ouverte, hors modèles d’IA à usage général.
Revue de requalification (EXIG-CON-15); 
clauses fournisseurs (section 13.3).
26
Obligations du déployeur : notice, supervision compétente, don­
nées d’entrée pertinentes, surveillance et suspension, journaux 
conservés au moins six mois, information des travailleurs et des 
personnes visées.
EXIG-CON-16.
27
Analyse d’impact sur les droits fondamentaux (AIDF) avant la pre­
mière utilisation, pour certains déployeurs.
Évaluation d’impact unifiée (section 12.9).
50
Informer les personnes qu’elles interagissent avec un système d’IA; 
marquer les contenus synthétiques.
EXIG-CON-19 et EXIG-CON-20.
72
Surveillance après commercialisation pendant toute la durée de 
vie, y compris l’interaction avec d’autres systèmes d’IA.
Traces des délégations A2A et analyse des 
chaînes multiagents dans le plan de sur­
veillance.
73
Signalement des incidents graves aux autorités de surveillance du 
marché.
Réponse aux incidents (section 12.8).
Sources : règlement (UE) 2024/1689, tel que modifié par le règlement (UE) 2026/1744 (EUR-Lex), et, pour la 
lecture article par article, les pages des articles 9, 13 et 72 du site non officiel du Future of Life Institute[58, 
61, 444, 445, 446].
EXIG-CON-13 · DOIT
Applicabilité du RIA déterminée par l’usage des sorties
La fiche de chaque agent DOIT indiquer si ses sorties sont, ou sont prévues pour être, utilisées dans 
l’Union européenne (destinataires, filiales ou clients qui s’y trouvent), et si son usage relève d’un 
domaine de l’annexe III. Un agent dont les sorties sont utilisées dans l’Union pour un usage de l’annexe 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 181 sur 283


---
## [Page PDF 182]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
III DOIT être classé en classe élevée et soumis aux exigences du tableau 49 dès son homologation, sans 
attendre le 2 décembre 2027.
Pourquoi : pour un fournisseur ou un déployeur établi hors de l’Union, le critère de l’article 2(1)(c) est l’utilisation des 
sorties dans l’Union; les preuves exigées ne se constituent qu’en cours d’exploitation (raisonnement du cadre)[441].
EXIG-CON-14 · NE DOIT PAS
Aucun usage interdit
Un agent NE DOIT PAS être homologué pour une pratique interdite par le RIA, quel que soit le lieu 
d’utilisation de ses sorties (choix du cadre). Le registre tient la liste de ces pratiques, mise à jour selon 
le règlement (UE) 2026/1744, et la revue d’homologation vérifie la finalité de l’agent contre cette liste.
Pourquoi : les interdictions s’appliquent depuis le 2 février 2025, de nouvelles s’ajoutent le 2 décembre 2026, et le 
report du haut risque ne les touche pas[57, 443].
EXIG-CON-15 · DOIT
Revue de requalification en fournisseur
Toute orchestration qui affecte un modèle, un agent ou un système d’IA à usage général à un usage 
de l’annexe III, qui modifie substantiellement un système à haut risque ou qui y appose le nom de 
l’entreprise DOIT déclencher, avant l’homologation, une revue de requalification en fournisseur au 
sens de l’article 25(1). Si l’entreprise devient fournisseur, elle DOIT conclure des accords écrits avec les 
tiers qui fournissent des outils, services, composants ou modèles intégrés au système (art. 25(4)).
Pourquoi  : la composition d’agents peut, à elle seule, changer la destination d’un composant et faire basculer 
l’entreprise dans le rôle de fournisseur[375].
EXIG-CON-16 · DOIT
Obligations du déployeur d’un agent à haut risque
Pour un agent à haut risque au sens du RIA, l’entreprise DOIT : confier la supervision humaine à des 
personnes compétentes, formées et dotées de l’autorité nécessaire; veiller à la pertinence des données 
d’entrée qu’elle contrôle; surveiller le fonctionnement et suspendre l’usage en cas de risque; conserver 
les journaux sous son contrôle au moins six mois (le cadre exige davantage, section 10.3); informer les 
travailleurs concernés avant une mise en service en milieu de travail et les personnes visées par une 
décision prise ou assistée par le système.
Pourquoi : article 26 du RIA, applicable aux systèmes de l’annexe III à compter du 2 décembre 2027[57, 447].
12.5 NIST AI RMF, ISO/IEC 42001 et normes associées
Cette section situe les référentiels volontaires et certifiables qui structurent la gestion des risques de l’IA et 
retient les sous-catégories et mesures les plus utiles aux agents.
NIST AI RMF 1.0 et profil IA générative
Le NIST AI RMF 1.0 (NIST AI 100-1), publié le 26 janvier 2023, s’articule autour de quatre fonctions : Gou­
verner (GOVERN), fonction transversale, Cartographier (MAP), Mesurer (MEASURE) et Gérer (MANAGE). 
Il est d’application volontaire; le NIST indique qu’il est en cours de révision dans le cadre du plan d’action 
américain sur l’IA, sans calendrier publié pour la version révisée, le document prévoyant lui-même un 
examen formel au plus tard en 2028[99, 448]. Il compte 72 sous-catégories (GOVERN 1.1 à 6.2, MAP 1.1 à 5.2, 
MEASURE 1.1 à 4.3, MANAGE 1.1 à 4.3) et définit sept caractéristiques d’une IA digne de confiance : valide 
et fiable; sûre; sécurisée et résiliente; responsable et transparente; explicable et interprétable; respectueuse 
de la vie privée; équitable, avec gestion des biais nuisibles[74]. Le profil IA générative (NIST AI 600-1, 26 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 182 sur 283
