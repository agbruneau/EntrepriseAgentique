# chunk_21 — pages PDF 201 à 212 (sur 283)



---
## [Page PDF 201]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
croître sans que les risques croissent au même rythme (choix du cadre). Les jalons 4 et 5 donnent à la phase 
Mise à l’échelle des critères de progression : le niveau 4, puis la certification ISO/IEC 42001, que le modèle 
de maturité place à ce niveau (figure 27).
Tableau 58 — Phases de mise en œuvre, livrables et autonomie autorisée
Phase
Livrables principaux
Autonomie autorisée
Jalon de sortie
Fondations mois 0 à 3
Comité mandaté; inventaire et registre, 
agents fantômes compris; propriétaire mé­
tier nommé pour chaque agent; fin des clés 
d’API partagées entre agents (remplacées 
par un secret propre par agent au coffre 
sous dérogation transitoire en attendant les 
identités de charge de travail de la phase 
Plateforme); passerelle de modèles, qui met 
fin aux appels directs aux fournisseurs; tra­
çage pilote; catalogue initial des protocoles, 
chaque serveur MCP antérieur y étant inscrit 
avec sa date de migration (EXIG-MCP-22); 
premier classement des risques; EFVP lan­
cées; choix des blocs de solution; coupe-cir­
cuit testé.
N0 et N1 seulement : 
pour les agents, lec­
ture et recommanda­
tion (N1), outils P0 
et P1, aucun effet en 
écriture; les flux dé­
terministes (N0) res­
tent régis par leurs 
contrôles habituels.
Jalon 1 : registre com­
plet, comité en fonction.
Plateforme mois 3 à 9
Passerelle d’agents ouverte aux outils P0 et 
P1, puis P2; catalogue d’entreprise MCP et 
A2A; migration des serveurs et clients MCP 
en production vers la révision de référence, 
au plus tard le 28 juillet 2027 (EXIG-MCP-22); 
identité par agent et jetons délégués; tra­
çage OpenTelemetry de bout en bout et 
journal d’audit; moteur d’exécution durable; 
approbation humaine signée; classement 
des risques et cycle de vie appliqués à tout 
nouvel agent; transparence envers les per­
sonnes, notamment pour les décisions visées 
par l’article 12.1 de la Loi sur le privé; pour 
une institution financière fédérale, validation 
initiale des agents et des modèles inscrits 
à l’inventaire E-23 avant le 1er mai 2027 
(EXIG-CON-12); premiers pilotes.
N2; premiers N3 bor­
nés au sein d’un 
même domaine, sur 
décision du comité, 
pour des agents de 
classe faible ou modé­
rée.
Jalon 2 : pilotes homolo­
gués selon l’annexe A; ni­
veau 2 de maturité atteint 
sur les cinq dimensions; 
chaque serveur et client 
MCP en production sur 
une révision antérieure a 
une date de migration 
au plus tard le 28 juillet 
2027, et aucun ne reste 
en production après cette 
date.
Industrialisation mois 9 à 
18
Migration des autres intégrations existantes 
au catalogue; toutes les interactions interdo­
maines par la passerelle; évaluation continue 
dans la chaîne d’intégration et de livraison 
continues (CI/CD); enveloppes budgétaires 
et imputation par centre de coûts; flux 
multiagents, sagas et compensation; bacs à 
sable pour le code généré; équipe rouge 
régulière; base de preuves de conformité 
unifiée.
N3 entre domaines, 
dans la limite du pla­
fond de chaque classe 
de risque, pour un 
agent dont tous les 
appels interdomaines 
passent par la passe­
relle d’agents.
Jalon 2a (organisations 
assujetties au RIA) : au 
plus tard le 1er novembre 
2027, voir l’encadré ci-
dessous. Jalon 3 : niveau 
3 de maturité sur les cinq 
dimensions; cibles chif­
frées des indicateurs ar­
rêtées pour J4 (section 
15.3).
Mise à l’échelle mois 18 et 
plus
Chorégraphie événementielle élargie (Clou­
dEvents, AsyncAPI); agents de partenaires; 
routage adaptatif des modèles; détection de 
dérive en continu; système de management 
de l’IA opéré, audit interne, puis audit de 
certification ISO/IEC 42001; revue du cadre.
N4 sur un domaine 
d’exploitation certifié, 
pour des agents de 
classe faible, sur déci­
sion du comité.
Jalon 4, vers le 
mois 36 : niveau 4 
sur les cinq dimen­
sions; quatre trimestres 
consécutifs d’indicateurs 
conformes aux cibles 
chiffrées; audit interne du 
SMIA réalisé et audit de 
certification lancé. Jalon 
5, vers le mois 48 : 
certificat ISO/IEC 42001 
obtenu; niveau 5 visé 
en interopérabilité et en 
gouvernance; feuille de 
route suivante adoptée. 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 201 sur 283


---
## [Page PDF 202]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
Phase
Livrables principaux
Autonomie autorisée
Jalon de sortie
Ensuite : revue annuelle 
de maturité.
Règles de progression
• Une phase ne doit pas être ouverte (livrables mis en production, autonomie accrue) avant que le comité 
ait constaté, sur preuves, le jalon qui la précède. Les travaux préparatoires de la phase suivante peuvent 
commencer plus tôt, mais aucune hausse d’autonomie n’est permise avant le jalon.
• Le plafond de la phase se combine avec le plafond de la classe de risque (section 8.1) : le plus strict 
s’applique. Un agent de classe élevée reste plafonné à N2, même en phase Mise à l’échelle; un agent de 
classe faible ne dépasse pas N1 tant que le jalon 1 n’est pas franchi.
• Un agent N3 qui agit entre domaines ne doit le faire que par la passerelle d’agents, même avant que 
la couverture interdomaines atteigne 100  % au jalon 3. Tant qu’un appel interdomaines d’un agent 
contourne la passerelle, les actions de cet agent hors de son domaine sont plafonnées à N2.
• Un agent existant dont le niveau dépasse le plafond de la phase doit être ramené sous ce plafond, par le 
retrait de ses outils en écriture ou, dès la phase Plateforme, par l’approbation de chacune de ses actions 
(N2), ou faire l’objet d’une dérogation limitée dans le temps (section 11.6).
• Les travaux qui découlent d’une échéance externe (J2a, la migration MCP exigée par EXIG-MCP-22 et la 
validation initiale E-23) sont datés par cette échéance, non par la durée des phases. Allonger une phase 
après l’évaluation initiale ne les reporte pas : ils passent alors en tête de la phase en cours, même s’ils 
appartiennent à la phase suivante, et le jalon qui précède ne les bloque pas.
• Le comité peut réordonner les travaux d’une phase selon les priorités métier. Il ne doit pas retirer un 
critère de jalon sans réviser le cadre (section 1.6).
ATTENTION
Trois échéances externes resserrent le calendrier. La ligne directrice E-23 du BSIF, en vigueur le 1er mai 
2027 et applicable aux institutions financières fédérales, exige un inventaire d’entreprise des modèles 
à risque non négligeable, y compris ceux des fournisseurs[8]; le cadre y ajoute l’état de validation 
(EXIG-CON-12) : l’inventaire est complet au jalon 1, et la validation initiale des agents visés se fait au 
début de la phase Plateforme. Les serveurs et clients MCP en production doivent avoir migré vers la 
révision de référence au plus tard le 28 juillet 2027 (EXIG-MCP-22), avant la fin de la phase Plateforme. 
Le règlement (UE) 2024/1689, modifié par le règlement (UE) 2026/1744, rend applicables à compter du 
2 décembre 2027 les obligations visant les systèmes à haut risque de l’annexe III (au 2 août 2028 pour 
ceux de l’annexe I)[57, 58]; pour une organisation assujettie qui adopte le cadre à l’automne 2026, cette 
date tombe entre les jalons 2 et 3. Les obligations déjà en vigueur, comme les articles 3.3, 12.1 et 17 de 
la Loi sur le privé, ne suivent pas le rythme des phases et ne souffrent aucune dérogation (section 11.6).
JALON 2A — CONFORMITÉ AU RIA, ANNEXE III
Pour une organisation assujettie au RIA (section 12.4), le comité constate au plus tard le 1er novembre 
2027, sur preuves :
• la liste des agents qui relèvent de l’annexe III, avec l’applicabilité consignée selon l’usage des sorties 
dans l’Union (EXIG-CON-13);
• pour chacun, la revue de requalification en fournisseur faite (EXIG-CON-15) et, si l’organisation est 
fournisseur, les obligations du fournisseur en place (section 12.4);
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 202 sur 283


---
## [Page PDF 203]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
• pour chacun, les obligations du déployeur en place (EXIG-CON-16), dont une conservation des 
journaux configurée pour au moins six mois;
• les preuves versées à la fiche de chaque agent, sans attendre la base de preuves unifiée de la phase 
Industrialisation.
À compter du 2 décembre 2027, les sorties d’un agent visé qui ne satisfait pas à ces critères ne doivent 
pas être utilisées dans l’Union. J2a n’ouvre aucune phase et n’accorde aucune autonomie.
Calage sur le calendrier 2027-2030
Le tableau 59 cale la feuille de route sur une adoption du cadre à l’automne 2026 : évaluation de maturité 
initiale en novembre 2026, ouverture de la phase Fondations le 1er décembre 2026 (mois 0). Un autre point 
de départ décale toutes les dates, sauf celles qui découlent d’une échéance externe. L’entreprise refait ce 
calage après l’évaluation initiale.
Tableau 59 — Calage indicatif, mois 0 au 1er décembre 2026
Période
Phase ou jalon
Échéances externes à tenir
Déc. 2026 – mi-mars 2027
Fondations, congés des 
fêtes compris
—
Mi-mars 2027
J1
Expiration de l’ébauche OAuth 2.1 −16 le 7 mars 2027 (à ins­
crire au catalogue; la référence normative reste OAuth 2.0)
Mi-mars – fin sept. 2027
Plateforme, vacances de la 
construction comprises
E-23 le 1er mai 2027; migration MCP le 28 juillet 2027, à 
terminer avant les vacances de la construction (deux dernières 
semaines de juillet)
Début oct. 2027
J2
—
1er nov. 2027 au plus tard
J2a
RIA, annexe III, le 2 décembre 2027
Oct. 2027 – juin 2028
Industrialisation
—
Début juill. 2028
J3
RIA, annexe I, le 2 août 2028
Juill. 2028 – 2030
Mise à l’échelle
Examen formel du NIST AI RMF au plus tard en 2028 (révision 
extraordinaire du cadre, section 1.6)
Déc. 2029
J4
—
Déc. 2030
J5
—
Une phase de six mois ou moins qui chevauche une période de congés collectifs (fêtes de fin d’année, 
vacances de la construction) s’allonge de la durée de cette période, environ deux semaines chacune; le 
tableau 59 en tient compte. Les durées des phases plus longues et les échéances de J4 et J5 incluent déjà les 
congés. Les échéances externes ne bougent pas : la validation initiale E-23 reste exigible le 1er mai 2027, et 
la migration MCP le 28 juillet 2027.
15.2 Les 90 premiers jours
Les 90 premiers jours forment la phase Fondations. Ils ne servent pas à construire de nouveaux agents, mais 
à rendre visibles et gouvernables ceux qui existent, puis à ouvrir une voie approuvée assez simple pour que 
personne n’ait intérêt à la contourner. L’inventaire répond aussi à la sous-catégorie GOVERN 1.6 du NIST 
AI RMF, qui demande des mécanismes d’inventaire des systèmes d’IA[74]. Ces 13 semaines sont des semaines 
travaillées : une période de congés collectifs s’y ajoute (section 15.1).
Tableau 60 — Plan des 90 premiers jours (phase Fondations)
Semaines
Travaux
Livrable vérifiable
Responsable
1 et 2
Mandater le comité et nommer ses membres; associer le respon­
sable de la protection des renseignements personnels (art. 3.1 de 
Mandat du comité; 
inventaire brut
Architecture 
d’entreprise, sécurité
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 203 sur 283


---
## [Page PDF 204]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
Semaines
Travaux
Livrable vérifiable
Responsable
la Loi sur le privé, modifiée par la Loi 25)[56]; lancer l’inventaire 
des agents internes, des logiciels-services à agents intégrés, des 
serveurs MCP, des assistants dotés d’outils et des agents de par­
tenaires, y compris les agents fantômes repérés dans les journaux 
réseau, les consentements OAuth et les consoles des logiciels-
services.
3 et 4
Ouvrir une fiche par agent (champs de l’étape Proposition, an­
nexe B); nommer un propriétaire métier pour chacun; recenser les 
clés d’API et les comptes de service utilisés par des agents. Pour 
une institution financière fédérale, marquer à la fiche les agents 
et les modèles qui relèvent de l’inventaire E-23.
Registre initial; liste 
des agents sans pro­
priétaire; inventaire 
des secrets
Propriétaires métier, 
équipe plateforme
5 et 6
Mettre en service la passerelle de modèles et y basculer tous les 
appels aux fournisseurs; remplacer chaque clé partagée par un 
secret propre à l’agent, conservé au coffre et injecté à l’exécution, 
en attendant les identités de charge de travail de la phase Plate­
forme; ce secret transitoire s’inscrit comme dérogation bornée 
dans le temps (EXIG-IAM-05, section 11.6). La fuite de secrets, les 
secrets de longue durée et la réutilisation d’une même identité 
figurent au Top 10 OWASP des identités non humaines[91].
Aucun appel direct 
à un fournisseur 
de modèles; aucune 
clé partagée entre 
agents
Équipe plateforme, 
sécurité
7 et 8
Instrumenter deux ou trois agents représentatifs avec OpenTele­
metry (version épinglée des conventions GenAI, section 10.1), 
centre de coûts compris; publier le catalogue initial des proto­
coles (section 6.3) et y inscrire les premiers outils avec leur palier 
P0 à P3; inscrire chaque serveur et client MCP antérieur à la 
révision de référence avec sa date de migration, au plus tard le 
28 juillet 2027 (EXIG-MCP-22).
Traces de bout en 
bout, du canal au 
modèle; catalogue 
initial publié; plan de 
migration MCP
Équipe plate­
forme, architecture 
d’entreprise
9 et 10
Classer chaque agent inventorié (faible, modéré, élevé) et fixer 
son plafond d’autonomie; repérer les agents qui traitent des RP 
ou les communiquent hors du Québec et lancer leurs EFVP, 
exigées par les articles 3.3 et 17 de la Loi sur le privé[413]; repérer 
les agents qui relèvent de l’annexe III du RIA; ramener sous le 
plafond de phase les agents qui le dépassent.
Classe et plafond 
inscrits pour tous les 
agents; EFVP plani­
fiées ou en cours; 
liste des agents visés 
par l’annexe III
Risques et conformi­
té, responsable de 
la protection des RP, 
propriétaires
11
Choisir les blocs de solution de la phase Plateforme (passerelle 
d’agents, moteur d’exécution durable, registre) avec la grille de 
la section 13.4; documenter le coupe-circuit, externe à l’agent[353], 
puis l’exercer sur un agent réel en mesurant le délai de révoca­
tion.
Décision de pla­
teforme; rapport 
d’exercice du coupe-
circuit
Architecture 
d’entreprise, équipe 
plateforme, sécurité
12 et 13
Mesurer la valeur de référence des indicateurs (tableau 61); tenir 
la revue du jalon 1; arrêter le plan de la phase Plateforme et 
choisir les pilotes, en plaçant en tête la migration MCP et, s’il y 
a lieu, la validation initiale E-23; recaler le tableau 59 sur la date 
réelle du jalon 1.
Procès-verbal du ja­
lon 1; tableau de 
bord de référence; 
calendrier recalé
Comité, architecture 
d’entreprise
À RETENIR
Bloquer les agents sans offrir d’autre voie pousse les employés vers l’IA fantôme (shadow AI), constate 
Gartner (avril 2026)[2]. Dès la sixième semaine, la passerelle de modèles et une inscription rapide au 
registre offrent une voie approuvée plus simple que le contournement.
15.3 Indicateurs
Les indicateurs servent à constater les jalons et à piloter l’autonomie sur des mesures. Ils obéissent à cinq 
règles du cadre :
• chaque indicateur doit être calculé à partir du registre, des passerelles, des traces et du journal d’audit 
ou, pour les exercices et les incidents, d’enregistrements horodatés, et non déclaré par les équipes;
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 204 sur 283


---
## [Page PDF 205]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
• la valeur de référence est mesurée au jalon 1; les indicateurs sont ensuite présentés chaque trimestre au 
comité, par agent, par domaine et pour l’entreprise;
• les cibles du tableau 61 sont des choix du cadre; le comité peut les ajuster par écrit, avec justification, 
sauf celles qui reprennent une exigence (registre, secrets, passerelles, traçabilité, EFVP), qui ne s’écartent 
que par dérogation (section 11.6);
• à la revue du jalon 3, le comité remplace par une valeur chiffrée chaque cible exprimée comme une 
tendance (« en baisse », « en hausse »), à partir des séries trimestrielles disponibles; ces valeurs sont les 
cibles que le jalon 4 vérifie;
• chaque indicateur a un responsable de mesure nommé parmi les rôles de la section 11.1.
Tableau 61 — Indicateurs de mise en œuvre et cibles proposées
Indicateur
Définition
Cible proposée
Fréquence
Couverture du re­
gistre
Part des agents actifs, déclarés ou découverts, 
qui ont une fiche à jour au registre
100 %
Mensuelle
Agents sans secret 
partagé
Part des agents qui s’authentifient avec un justi­
ficatif qui leur est propre, sans clé partagée ni 
compte d’une personne
100 % au jalon 1
Mensuelle
Couverture des pas­
serelles
Part des appels de modèles, et des appels inter­
domaines d’outils et d’agents, qui passent par la 
passerelle de modèles ou d’agents
Modèles : 100 % au jalon 1; 
interdomaines : 100 % au ja­
lon 3, et 100 % dès le jalon 2 
pour les agents N3
Mensuelle
Conformité au cata­
logue
Part des intégrations d’agents qui utilisent un 
protocole et une version inscrits au catalogue
100 % des nouveaux agents; 
serveurs et clients MCP en 
production : 100 % sur la révi­
sion de référence au 28 juillet 
2027; 100 % des agents exis­
tants au jalon 3
Trimestrielle
Traçabilité
Part des actions à effet (P2 et P3) rattachées à 
une trace complète, à leur mandant et à une 
entrée du journal d’audit
100 %
Mensuelle
Couverture de 
l’évaluation
Part des agents en production dont le jeu de ré­
férence s’exécute dans la chaîne CI/CD et atteint 
ses seuils (section 10.4)
100 %
Trimestrielle
Réussite des tâches
Tâches réussies sans intervention humaine im­
prévue, sur le total des tâches, par agent
Seuil fixé au contrat d’agent
Mensuelle
Escalade humaine
Part des tâches renvoyées à une personne
Fourchette fixée au contrat 
d’agent; tout écart s’analyse
Mensuelle
Approbation sans 
modification
Par approbateur et par file : part des demandes 
approuvées telles quelles, avec le temps de ré­
ponse médian
Seuil d’alerte fixé par cas 
d’usage; tout écart marqué 
par rapport à la norme 
s’analyse
Mensuelle
Incidents agentiques
Nombre d’incidents par gravité, avec les délais 
de détection et de confinement
Aucun incident grave; délais 
en baisse, puis valeur chiffrée 
au jalon 3
Trimestrielle
Délai de révocation 
en exercice
Temps écoulé entre la décision d’arrêter un 
agent et le refus de son dernier appel, dans 
tous les systèmes, mesuré lors d’un exercice du 
coupe-circuit
15 minutes au plus, puis en 
baisse; valeur chiffrée au jalon 
3
Trimestrielle
Délai d’intégration
Temps nécessaire pour brancher à un agent un 
outil déjà inscrit au catalogue
En baisse d’un trimestre à 
l’autre, puis valeur chiffrée au 
jalon 3
Trimestrielle
Réutilisation
Nombre moyen d’agents consommateurs par 
outil du catalogue
En hausse, puis valeur chiffrée 
au jalon 3
Trimestrielle
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 205 sur 283


---
## [Page PDF 206]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
Indicateur
Définition
Cible proposée
Fréquence
Coût par tâche réus­
sie
Coût total imputé (inférence, outils, quote-part 
de la plateforme) divisé par le nombre de tâches 
réussies, en dollars canadiens
Inférieur au coût du processus 
de référence sans agent; écart 
chiffré au jalon 3
Mensuelle
EFVP à jour
Part des agents traitant des RP dont l’EFVP 
couvre la version en production
100 %
Trimestrielle
La cible proposée de 15 minutes pour la révocation est un choix du cadre, que l’entreprise ajuste en fixant 
son propre délai maximal (EXIG-IAM-20) : elle correspond à la durée de vie cible des jetons délégués 
(section 9.3), qui borne l’exposition résiduelle si un système en aval accepte encore un jeton déjà émis. Elle 
concrétise la sous-catégorie MANAGE 2.4 du NIST AI RMF, qui demande des mécanismes pour désengager 
ou désactiver un système dont le comportement s’écarte de l’usage prévu[74]. Le coût par tâche réussie est 
d’abord présenté en refacturation indicative (showback), modèle que recommande la FinOps Foundation[407]; 
le passage à la refacturation réelle relève du comité (EXIG-FIN-09).
ATTENTION
Un indicateur ne se lit jamais seul. Un taux d’escalade très bas peut signifier qu’un agent tranche des cas 
qu’il devrait renvoyer. Un taux élevé d’approbation sans modification, joint à des temps de réponse très 
courts, peut signaler une approbation machinale : l’Infocomm Media Development Authority (IMDA) 
de Singapour recommande de surveiller ces deux signaux[76]. Une cible déclenche une analyse; elle ne 
sert pas à récompenser une équipe.
15.4 Facteurs de succès et risques de mise en œuvre
Les données publiques invitent à la prudence : selon Gartner (juin 2025), plus de 40 % des projets d’IA 
agentique seront annulés d’ici la fin de 2027 en raison de coûts croissants, d’une valeur d’affaires incertaine 
ou de contrôles des risques inadéquats[3]. Les facteurs suivants visent directement ces trois causes.
Facteurs de succès
1. Un parrainage de direction et un comité qui décide. Un comité seulement consultatif ne peut ni 
constater les jalons ni accorder les dérogations.
2. La plateforme avant la multiplication des agents. Gartner (avril 2026) estime qu’une entreprise 
moyenne du Fortune 500 aura plus de 150 000 agents en usage d’ici 2028, contre moins de 15 en 2025[2]. 
Cet ordre de grandeur prospectif[467] laisse prévoir qu’un contrôle agent par agent ne tiendra pas : 
passerelles, catalogue et gabarits doivent précéder la croissance.
3. Une gouvernance proportionnée. Selon Gartner (mai 2026), appliquer la même gouvernance à tous 
les agents mènera à des échecs, et 40 % des entreprises rétrograderont ou désactiveront des agents 
autonomes d’ici 2027 à cause de lacunes révélées seulement après des incidents en production[95]. Le 
cadre gradue donc les contrôles selon le niveau d’autonomie et le palier d’outil (section 8.4).
4. Commencer simple. Anthropic recommande la solution la plus simple possible[6]; une architecture 
multiagent consomme habituellement de 3 à 10 fois plus de jetons qu’un agent unique[275]. Les premiers 
pilotes retiennent un flux déterministe ou un agent unique outillé.
5. Mesurer la valeur dès le pilote. Chaque pilote compare son coût par tâche réussie à celui du processus 
de référence; un pilote qui ne fait pas mieux s’arrête ou se redéfinit.
6. Concevoir la supervision au lieu de la présumer. Le biais d’automatisation touche les novices 
comme les experts et ne se prévient pas par la seule formation[314]. Les files d’approbation, les seuils et 
les indicateurs de la section 8.7 font partie des livrables de la phase Plateforme.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 206 sur 283


---
## [Page PDF 207]

CRE-IA-2026-01 · Cadre de référence
15 Feuille de route et indicateurs
Risques et parades
Tableau 62 — Risques de mise en œuvre, signes avant-coureurs et parades
Risque
Signe avant-coureur
Parade prévue par le cadre
Abandon faute de 
valeur démontrée
Pilotes sans processus de référence ni coût par 
tâche
Indicateur de valeur obligatoire à la fiche; arrêt 
des pilotes non concluants
Plateforme centrale 
devenue goulot
Délai d’intégration en hausse; contournements
Modèle en étoile et libre-service par gabarits (sec­
tion 11.3)
Prolifération et IA 
fantôme
Agents découverts hors registre; consentements 
OAuth inconnus
Inventaire continu; voie approuvée simple; désac­
tivation des agents sans fiche
Gouvernance uni­
forme
Mêmes contrôles pour un agent N1 et un agent N3; 
files d’approbation saturées
Contrôles gradués par niveau et par palier (section 
8.4)
Approbation machi­
nale
Taux élevé d’approbation sans modification; temps 
de réponse très courts
Files priorisées par risque, regroupement, rotation 
des approbateurs (section 8.7)
Instabilité des stan­
dards
Nouvelle révision de MCP; conventions GenAI 
d’OpenTelemetry encore au niveau Development
Versions épinglées au catalogue; révision trimes­
trielle (section 11.7)
Migration MCP man­
quée
Serveurs ou clients MCP antérieurs encore en pro­
duction à trois mois de l’échéance du 28 juillet 2027; 
serveurs sans date de migration au catalogue
Plan de migration dès la phase Fondations; migra­
tion en tête de la phase Plateforme; critère du 
jalon 2 (EXIG-MCP-22)
Phase Plateforme al­
longée
Livrables de la phase en retard sur le calendrier 
recalé; jalon 2 qui glisse au-delà d’octobre 2027
Travaux datés par leur échéance externe (règles 
de progression); travaux réglementaires en tête de 
phase; réordonnancement par le comité
Verrouillage par une 
plateforme
Extensions propriétaires; données ou mémoires non 
exportables
Clauses contractuelles du chapitre 13
Dérive des coûts
Coût par tâche en hausse; boucles qui atteignent 
leurs plafonds
Enveloppes budgétaires et routage frugal (section 
10.6)
Échéance réglemen­
taire manquée
Agent à haut risque dont la mise en service est 
prévue à compter du 2 décembre 2027; EFVP non 
commencée; inventaire E-23 sans état de validation 
à l’approche du 1er mai 2027
Jalon J2a; validation initiale E-23 en phase Pla­
teforme; priorité dans chaque phase; évaluation 
d’impact unifiée (section 12.9)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 207 sur 283


---
## [Page PDF 208]

CRE-IA-2026-01 · Cadre de référence
Annexes — Outils d’application
Grille d’homologation, gabarit de fiche d’agent, exemples de contrats, registre des exigences, glossaire, 
validation des sources et des ébauches, références.
A · Grille d’homologation
B · Gabarit de fiche d’agent
C · Exemples de contrats
D · Registre des exigences
E · Glossaire
F · Validation des sources et des ébauches
G · Références
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 208 sur 283


---
## [Page PDF 209]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
A Grille d’homologation
Cette grille se remplit pour chaque agent et chaque serveur MCP avant le point de contrôle « homologa­
tion » du cycle de vie, puis à chaque réévaluation. Elle reprend, sous forme vérifiable, les exigences qui 
conditionnent la mise en production; chaque point renvoie aux exigences qui le fondent. Une même grille 
sert à l’équipe du domaine, à la plateforme, à la sécurité et au comité.
A.1 Mode d’emploi
1. Qui remplit. Le responsable technique de l’agent remplit la grille et joint les preuves; l’équipe plate­
forme et la sécurité vérifient; l’autorité désignée par la matrice RACI approuve (section 11.2). Pour un 
agent de classe élevée ou de niveau N4, le comité approuve.
2. Réponses admises. « Conforme » avec preuve (lien vers l’artefact au registre), « Sans objet » avec 
justification, ou « Non conforme ». Un point non conforme exige une dérogation écrite, bornée dans 
le temps et assortie de mesures compensatoires (section 11.6). Un écart à une exigence formulée avec 
DEVRAIT (par exemple EXIG-IAM-15 et −19) se justifie par écrit à la fiche, sans dérogation (section 1.4).
3. Points non dérogeables. Les points marqués non dérogeable ne peuvent faire l’objet d’aucune déro­
gation : un « Non conforme » bloque la mise en production (EXIG-GOV-17).
4. Conservation. La grille remplie, ses preuves et la décision d’homologation sont versées à la fiche de 
l’agent au registre (annexe B) et conservées avec son historique.
Légende de l’applicabilité : Tous s’applique à tout agent; Si … s’applique seulement dans le cas indiqué.
A.2 Gouvernance, registre et classement
• Tous non dérogeable Fiche complète au registre : identifiant, version, parrain (propriétaire métier) et 
responsable technique nommés, équipe de garde, finalité, mandants autorisés. — EXIG-GOV-01, -07, -08
• Tous Séparation des fonctions respectée  : la personne qui prépare une décision du cycle de vie 
(construction, évaluation) n’est pas celle qui l’approuve. — EXIG-GOV-03, -04
• Tous Classe de risque attribuée et approuvée avant l’inscription, avec les critères retenus (rayon 
d’impact, réversibilité, délai de détection, observabilité). — EXIG-CON-01, EXIG-AUT-06
• Tous non dérogeable Niveau d’autonomie déclaré (N0 à N4), dans le plafond de la classe de risque; 
aucun comportement NX. — EXIG-AUT-01, -02, -03, EXIG-CON-02
• Si N3 ou N4 Domaine d’exploitation (ODD) documenté, comportement de repli et conditions d’arrêt 
déclarés; homologation du niveau (l’évaluation assistée de Feng et al. est recommandée, non exigée). — 
EXIG-AUT-04, -05
• Tous Patron d’orchestration déclaré et justifié; configuration la plus simple démontrée suffisante, ou 
preuve mesurée du gain multiagent. — EXIG-ORC-01, -02, -03
• Tous Déclencheurs de réévaluation inscrits à la fiche (changement de modèle, d’invite système, d’outil 
ou de palier d’outil, de version majeure de contrat ou de protocole, de population visée, de finalité ou de 
catégorie de données; incident grave ou dérive détectée). — EXIG-GOV-12, EXIG-CON-03
A.3 Interopérabilité et contrats
• Tous Revue d’interopérabilité aux quatre niveaux (juridique, organisationnel, sémantique, tech­
nique) consignée; vocabulaire et schémas d’entreprise utilisés. — EXIG-INT-01, -02, -03
• Tous Protocoles du catalogue seulement, à la version de référence; choix justifié par la matrice de 
sélection. — EXIG-INT-04, -06, -07, -10
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 209 sur 283


---
## [Page PDF 210]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
• Si outils MCP Serveurs MCP derrière la passerelle, autorisation obligatoire, portées minimales, aucun 
passage de jeton, transport conforme à l’environnement. — EXIG-MCP-01, -08, -09, -10, -11
• Si outils MCP Contrats d’outils orientés tâche (pas de miroir CRUD), nommage et résultats conformes, 
annotations traitées comme de simples indices, empreinte des définitions épinglée. — EXIG-MCP-06, -07, 
-14, -20
• Si outils MCP Contrôles propres à MCP : concordance en-têtes et corps, traitement de _meta, état 
explicite protégé, aucune donnée sensible en en-tête. — EXIG-MCP-15 à -18
• Si invocable par A2A Carte d’agent A2A 1.0 publiée, signée, inscrite au registre, sans champ hors 
norme; compétences internes réservées à la carte étendue. — EXIG-A2A-02 à -06
• Si invocable par A2A Tâches A2A : version annoncée, liaisons standard, authentification à chaque 
requête, autorisation par compétence, notifications push durcies, trousse de compatibilité réussie. — 
EXIG-A2A-07 à -14
• Si événements Événements CloudEvents complets, contrat AsyncAPI au catalogue, attributs de gou­
vernance vérifiés, compteur de sauts appliqué, aucune donnée personnelle dans les attributs, autorisation 
fondée sur l’identité authentifiée auprès du courtier. — EXIG-EVT-02 à -07
• Si événements Consommateurs idempotents, ordre garanti par la clé de partition lorsque requis, 
conservation des entrées pour rejeu isolé. — EXIG-EVT-08, -09, -10
A.4 Orchestration et réversibilité
• Si écriture, plusieurs étapes ou attente Exécution durable : état persisté après chaque transition, reprise 
sans double effet, magasin de points de contrôle protégé. — EXIG-ARC-05, -06, EXIG-ORC-11, -12, -13
• Si écritures Clé d’idempotence sur toute écriture, vérifiée par le service visé. — EXIG-ORC-21, -22
• Si écritures multisystèmes Saga : compensation déclarée au catalogue pour chaque étape, journal de 
compensation tenu avant l’action, compensations idempotentes, escalade après deux échecs, isolation 
sémantique. — EXIG-ORC-15 à -19
• Si saga Quatre tests d’injection de fautes réussis dans la chaîne d’intégration (échec à chaque étape, 
plantage entre journal et action, double compensation, double échec de compensation). — EXIG-ORC-20
• Tous Plafonds d’exécution (étapes, appels d’outils, jetons, coût, délai), résilience et modèle de repli 
testés. — EXIG-ORC-26, -27
• Si multiagent Délégation limitée à deux niveaux, contexte transmis minimal et structuré, retour validé 
avant réutilisation, filtrage de sécurité dans chaque agent. — EXIG-ORC-04, -23, -24, -25
• Tous Coupe-circuit opérationnel pour l’agent et inclus dans l’exercice trimestriel; délai de révocation 
mesuré. — EXIG-ORC-28, EXIG-IAM-20
A.5 Autonomie et supervision humaine
• Tous Paliers des outils (P0 à P3) attribués au catalogue après revue, jamais déduits des annotations du 
serveur; contrôle calculé à chaque appel; échec en mode fermé. — EXIG-AUT-08, -10, -11
• Tous non dérogeable Aucune action P3 sans approbation humaine, par jeton signé lié à l’action 
exacte; aucune approbation tirée de la conversation de l’agent. — EXIG-AUT-09, -12, -13
• Si approbations Approbateurs habilités et formés; écran d’approbation fidèle à l’action; boîte de récep­
tion persistante; charge d’approbation maîtrisée et qualité de la supervision mesurée. — EXIG-AUT-15, 
-16, -19, -20, -21
• Si agent ambiant Réautorisation périodique et effets placés après le point d’approbation. — EXIG-
AUT-17, -18
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 210 sur 283


---
## [Page PDF 211]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
• Si décision sur une personne Décisions automatisées (art. 12.1 de la Loi sur le privé) : avis au plus 
tard au moment de la décision, explication des principaux facteurs, révision humaine significative, 
conservation des éléments de décision. — EXIG-AUT-22, -23, EXIG-CON-07, -08, -09
A.6 Identité, sécurité et confiance zéro
• Tous Identité propre, cryptographique, émise par la plateforme, non partagée; aucun secret statique; 
justificatifs hors de portée du modèle. — EXIG-IAM-03 à -06
• Si agit pour une personne non dérogeable Délégation explicite par échange de jetons; aucune usurpa­
tion; portée jamais élargie; jeton à audience unique; aucun relais de jeton. — EXIG-IAM-08 à -12
• Tous Profil OAuth de l’entreprise appliqué, jetons contraints à l’émetteur et de courte durée; agents 
autonomes avec identifiants du client et portées par outil. — EXIG-IAM-13 à -16
• Tous Passerelle d’agents en coupure de tout appel EXIG-ARC-01, -08, -11, -12, EXIG-IAM-17, -18, -19, -
21 interdomaine, passerelle de modèles pour tout appel de modèle (aucun appel direct à un fournisseur), 
échec en mode fermé, secrets aval injectés par la passerelle, politiques en code versionnées et testées.
• Tous Modèle de menaces établi (analyse simplifiée pour la classe faible) et matrice de traçabilité 
menaces-contrôles (OWASP ASI) à jour. — EXIG-SEC-01, -02
• Tous Défense contre l’injection : présomption d’injection, règle de deux par session, retrait détermi­
niste des capacités d’exfiltration, patron de conception pour la classe élevée. — EXIG-SEC-03 à -07
• Si code généré Bac à sable conforme (technologie d’isolation, éphémère, réseau refusé par défaut, 
métadonnées infonuagiques bloquées, secrets injectés hors du bac à sable, délais à trois niveaux, journal 
externe, porte de validation). — EXIG-SEC-08 à -17
• Tous Chaîne d’approvisionnement : provenance approuvée, signatures vérifiées, nomenclature de 
version, chaque serveur traité comme un domaine distinct, tiers évalués. — EXIG-SEC-18 à -22
• Si classe modérée ou élevée Équipe rouge propre aux agents et suite d’attaques intégrée à la chaîne 
d’intégration; contrôles déterministes vérifiés. — EXIG-SEC-23, -24, -25
A.7 Observabilité, évaluation et coûts
• Tous Traçage de bout en bout : contexte W3C propagé dans HTTP, MCP, A2A et les événements; 
conventions GenAI à la version épinglée; attributs d’entreprise sous préfixe de domaine inversé. — EXIG-
OBS-01 à -06
• Tous Contenu des invites et réponses non capturé par défaut; toute capture exceptionnelle filtrée, 
chiffrée et à conservation courte. — EXIG-OBS-07 à -10
• Tous Journal d’audit distinct des traces, exhaustif pour chaque action à effet et chaque approbation; 
enregistrement à cinq éléments canonisé et signé; inaltérabilité vérifiée. — EXIG-OBS-11, -12, -13
• Tous Évaluation : paliers franchis et relancés à chaque changement, jeu de référence versionné compre­
nant des cas adverses et réussi aux seuils du contrat, évaluations répétées et isolées, échantillonnage de 
la production planifié, objectifs de niveau de service fixés. — EXIG-EVA-01 à -06
• Tous Coûts : enveloppe appliquée à chaque étape, quotas et plafond mensuel par agent, plus petit 
modèle suffisant, préfixe d’invite stable, imputation par centre de coûts, coût par tâche réussie comparé 
au processus sans agent, hypothèses de prix datées; lots asynchrones recommandés (EXIG-FIN-08) et 
table de conversion des unités SaaS si plateforme SaaS (EXIG-FIN-03). — EXIG-FIN-01 à -10
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 211 sur 283


---
## [Page PDF 212]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
A.8 Données, vie privée et conformité
• Si renseignements personnels EFVP terminée avant le passage en pilote, responsable de la protection des 
renseignements personnels consulté dès le début du projet, finalités vérifiées avant toute réutilisation. 
— EXIG-CON-04, -06
• Si traitement hors Québec Lieux de traitement cartographiés (modèles, outils, mémoires) avec EFVP 
et entente écrite pour toute communication hors Québec. — EXIG-CON-05
• Tous Mémoires et traces : durées de vie fixées, contrôles avant toute écriture en mémoire longue, aucun 
historique brut comme mémoire, magasins isolés. — EXIG-ARC-22 à -25, EXIG-CON-10
• Tous Régimes applicables inscrits à la fiche (Loi 25, LPRPDE, BSIF E-23, RIA); aucun usage interdit; 
obligations du déployeur respectées pour la classe élevée. — EXIG-CON-11 à -16
• Tous Transparence : divulgation de l’interaction avec un agent et identification des contenus produits; 
vérification humaine de tout contenu juridique. — EXIG-CON-19, -20, -22
• Tous Incidents : procédure en cinq temps connue de l’équipe de garde, registre des incidents de confi­
dentialité, règle de notification la plus exigeante. — EXIG-CON-23, -24, -25
• Si classe élevée Évaluation d’impact unifiée (EFVP, analyse d’impact algorithmique, analyse d’impact 
sur les droits fondamentaux au besoin). — EXIG-CON-26
• Si acquis d’un fournisseur Grille d’évaluation fournisseur remplie et clauses contractuelles norma­
tives intégrées au contrat. — EXIG-APP-07 à -17
B Gabarit de fiche d’agent
La fiche d’agent est l’entrée du registre d’entreprise décrite à la section 11.4. Ce gabarit fixe son contenu 
minimal et l’étape du cycle de vie où chaque champ devient exigible. Il est normatif par son contenu, pas 
par sa forme : tout outil de registre convient s’il conserve ces champs et leur historique.
Règles d’utilisation
• Ouverture et complétude. La fiche s’ouvre à l’étape Proposition et se complète au fil du cycle de vie 
(section 11.5). Elle est complète lorsque tous les champs exigés à l’étape Pilote sont remplis, ce que vérifie 
le point de contrôle qui clôt l’étape Construction et évaluation; avant cela, l’agent n’obtient aucun jeton 
d’exécution en production.
• Source de vérité. Les valeurs qui commandent un contrôle (palier d’outil, seuil, plafond, portées, niveau 
d’autonomie) DOIVENT être lues par la passerelle dans le registre et le catalogue, jamais dans ce que 
l’agent déclare de lui-même ni dans les annotations d’un serveur MCP (section 8.3).
• Réévaluation. Tout changement de modèle ou de version de modèle, d’instructions système, d’outil ou 
de palier d’outil, de version majeure d’un contrat ou d’un protocole, de population visée, de finalité ou de 
catégorie de données, ainsi que tout incident grave ou toute dérive détectée, déclenche une réévaluation 
de la classe de risque et du niveau d’autonomie (EXIG-GOV-12). Le niveau d’autonomie fonctionne 
comme le « certificat d’autonomie » de Feng et al., qui se renouvelle à chaque changement de l’agent ou 
de son environnement[83]. S’il y a des RP, l’EFVP est mise à jour, comme le recommande le guide de la 
CAI lorsqu’un projet change[413].
• Attestation. Le propriétaire métier atteste périodiquement que l’agent est encore requis et que sa fiche 
est exacte. Le cadre exige l’attestation au moins tous les 12 mois, et tous les 6 mois pour la classe élevée 
(EXIG-GOV-13); à titre d’exemple, les bonnes pratiques de Microsoft Entra Agent ID prévoient que le 
parrain atteste tous les 6 à 12 mois que chaque agent est encore requis[92]. Un agent dont l’attestation est 
échue doit passer à l’état « suspendu » (EXIG-GOV-09).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 212 sur 283
