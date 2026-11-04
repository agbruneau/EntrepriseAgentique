# chunk_19 — pages PDF 181 à 192 (sur 283)



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


---
## [Page PDF 183]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
juillet 2024) décrit douze risques propres à l’IA générative ou aggravés par elle; deux touchent directement 
les agents : la configuration humain-IA (biais d’automatisation, dépendance excessive) et l’intégration de la 
chaîne de valeur et des composants (intégration non traçable de composants tiers)[449].
Les sous-catégories suivantes sont les plus directement utiles aux agents[74] :
• GOVERN 1.3 : processus qui déterminent le niveau d’activités de gestion des risques selon la tolérance 
au risque de l’organisation; GOVERN 1.6  : mécanismes d’inventaire des systèmes d’IA, dotés de 
ressources selon les priorités de risque (le registre d’agents); GOVERN 1.7 : déclassement sécuritaire (le 
cadre y rattache la révocation des identifiants);
• GOVERN 6.1 et 6.2 : politiques sur les risques liés aux tiers et contingence en cas de défaillance d’un 
système de tiers jugé à haut risque (serveurs MCP et agents externes);
• MAP 3.5 : processus de supervision humaine définis, évalués et documentés;
• MEASURE 2.4  : surveillance en production du fonctionnement et du comportement du système; 
MEASURE 2.7 : évaluation de la sécurité et de la résilience; MEASURE 3.1 : suivi des risques émergents;
• MANAGE 2.3  : réponse aux risques jusque-là inconnus et reprise; MANAGE 2.4  : mécanismes et 
responsabilités pour supplanter, désengager ou désactiver un système (le coupe-circuit); MANAGE 4.1 : 
plans de surveillance après déploiement couvrant le recours et la neutralisation par un humain (appeal 
and override), l’intervention en cas d’incident, la reprise, la gestion du changement et le déclassement.
ISO/IEC 42001 et normes associées
ISO/IEC 42001:2023 (1re édition, 18 décembre 2023) spécifie les exigences d’un système de management de 
l’IA (SMIA). Elle suit la structure harmonisée des normes de systèmes de management, comme ISO/IEC 
27001 : articles 4 (contexte), 5 (leadership), 6 (planification, dont l’appréciation des risques en 6.1.2, leur 
traitement en 6.1.3 et l’évaluation d’impact des systèmes d’IA en 6.1.4), 7 (support), 8 (fonctionnement), 
9 (évaluation des performances) et 10 (amélioration)[395]. Son annexe A, normative, compte 38 mesures 
réparties en neuf objectifs (A.2 à A.10). Les plus directement applicables aux agents sont A.5 (évaluation 
des impacts des systèmes d’IA), A.6.2.6 (exploitation et surveillance), A.6.2.8 (enregistrement des journaux 
d’événements), A.9 (utilisation responsable et usage prévu) et A.10 (relations avec les tiers et les clients)[395, 
450]. La certification est délivrée par des organismes conformes à ISO/IEC 17021-1 et à ISO/IEC 42006:2025[451].
Trois normes complètent l’ensemble. ISO/IEC 42005:2025 donne des lignes directrices pour évaluer l’impact 
d’un système d’IA sur les personnes et la société, à quels moments du cycle de vie, et pour intégrer cette 
évaluation au SMIA; ISO/IEC 23894:2023 traite de la gestion des risques propres à l’IA; ISO/IEC 22989:2022 
établit la terminologie et définit l’agent d’IA (3.1.1)[59, 452, 453]. Le NIST AI RMF et ISO/IEC 42001 sont complé­
mentaires (appréciation du présent cadre) : le premier est un cadre d’application volontaire, la seconde 
une norme d’exigences certifiable par tierce partie[448, 451]. Une entreprise qui vise la certification tient une 
déclaration d’applicabilité qui rattache les exigences du présent cadre aux mesures de l’annexe A; le lien 
avec le modèle de maturité est traité à la section 14.3.
Ce que ces référentiels ne sont pas
AI TRiSM (AI Trust, Risk and Security Management) est un cadre d’analyste propriétaire de Gartner, non une 
norme : le cadre ne le place pas au même rang que le RIA, ISO/IEC 42001 ou le NIST AI RMF. La littérature 
scientifique l’a adapté aux systèmes multiagents autour de l’explicabilité, du ModelOps, de la sécurité et de 
la confidentialité, chacun sous l’angle de la gouvernance du cycle de vie[454]. De même, aucune publication 
du NIST ne fixe encore de profil d’interopérabilité des agents. L’AI Agent Standards Initiative du Center for 
AI Standards and Innovation (CAISI) du NIST, lancée le 17 février 2026, et le projet de superpositions de 
contrôles SP 800-53 (COSAiS, Control Overlays for Securing AI Systems, renommé COSIS, Control Overlays 
for Super Intelligence Systems, le 20 octobre 2026 selon la page du projet), qui prévoit des cas d’usage « agent 
unique » et « multiagents », relèvent de la veille (section 11.7)[411, 455]. Il en va de même de la note de 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 183 sur 283


---
## [Page PDF 184]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
concept du 7 avril 2026 sur un profil consacré aux infrastructures critiques, document préparatoire non 
contraignant[456].
EXIG-CON-17 · DOIT
Déclaration de tolérance au risque
Le comité d’architecture et des risques agentiques DOIT faire approuver par la direction une déclaration 
de tolérance au risque qui fixe, pour chaque classe, le niveau d’activités de gestion des risques (contrôles, 
fréquence des revues, autorité d’approbation) et les seuils au-delà desquels un agent est suspendu. La 
déclaration DOIT être revue chaque année et après tout incident grave.
Pourquoi : GOVERN 1.3 demande de proportionner la gestion des risques à la tolérance de l’organisation; sans seuils 
écrits, chaque équipe fixe les siens[74].
12.6 Matrice de correspondance
La matrice relie les quatre fonctions du NIST AI RMF aux articles d’ISO/IEC 42001, aux obligations de la Loi 
25 et du RIA, et aux artefacts du cadre qui en font la preuve. Elle constitue une interprétation interne du 
cadre, non une table de correspondance publiée par le NIST ou l’ISO.
Tableau 50 — Matrice de correspondance : NIST AI RMF, ISO/IEC 42001, Loi 25, RIA et artefacts du cadre
Fonction NIST
ISO/IEC 42001
Loi 25 (Loi sur le 
privé)
RIA
Artefacts et contrôles du cadre
Gouverner : GOVERN 
1.1, 1.2, 1.3, 1.6, 1.7, 2.1, 
6.1, 6.2
Art. 4 et 5 
(5.2 politique, 
5.3 rôles); A.2, 
A.3, A.10
Art. 3.1, 3.2, 18.3
Art. 25 et 
26
Déclaration de tolérance au risque 
(EXIG-CON-17); registre avec propriétaire nommé 
(section 11.4); matrice RACI (section 11.2); clauses 
fournisseurs (section 13.3); retrait avec révocation 
des identités (section 11.5)
Cartographier : MAP 
1.1 à 5.2, dont MAP 3.5
Art. 6 (6.1.2 à 
6.1.4); A.5
Art. 3.3, 8.1, 17
Art. 6 et 
annexe III; 
art. 9 et 
27
Classe de risque (EXIG-CON-01); niveau 
d’autonomie et paliers d’outils (chapitre 8); 
lieux de traitement (EXIG-CON-05); évaluation 
d’impact unifiée (EXIG-CON-26)
Mesurer : MEASURE 
2.4, 2.5, 2.7, 3.1
Art. 9 (9.1 à 9.3); 
A.6.2.4, A.6.2.6, 
A.6.2.8, A.7.4
Art. 11, 12.1, 27
Art. 12, 
15, 72
Traçage (section 10.1); journal d’audit (section 
10.3); évaluation continue (section 10.4); taux 
d’approbation sans modification (section 8.7)
Gérer : MANAGE 2.3, 
2.4, 4.1
Art. 8 et 10; A.9
Art. 3.5 à 3.8, 12.1 
(révision), 23
Art. 14, 
26, 73
Coupe-circuit (section 7.8); compensation (sec­
tion 7.5); approbation vérifiable (section 
8.5); réponse aux incidents (EXIG-CON-23 
à EXIG-CON-25); destruction des mémoires 
(EXIG-CON-10)
Interprétation du cadre, établie à partir de NIST AI 100-1 et du catalogue d’ISO/IEC 42001[74, 395].
Deux confusions courantes sont à éviter. L’objectif A.7 d’ISO/IEC 42001 porte sur les données des systèmes 
d’IA (acquisition, qualité, provenance, préparation), et non sur l’évaluation des performances, l’audit interne 
ou la revue de direction, qui relèvent de l’article 9. Les sous-catégories MANAGE 3.1 et 3.2 visent les 
ressources de tiers et les modèles préentraînés; le coupe-circuit relève de MANAGE 2.4 et le déclassement 
sécuritaire de GOVERN 1.7[74].
EXIG-CON-18 · DOIT
Base de preuves unique
Chaque preuve produite par la plateforme ou par les équipes (trace, enregistrement d’audit, EFVP, 
évaluation d’impact, résultat d’évaluation, rapport d’équipe rouge, décision d’homologation) DOIT 
être conservée une seule fois dans un dépôt de preuves, étiquetée avec les exigences du cadre et les 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 184 sur 283


---
## [Page PDF 185]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
dispositions externes auxquelles elle répond selon le tableau 50. L’équipe risques et conformité DOIT 
revoir la matrice chaque année.
Pourquoi : une base unique évite de produire quatre dossiers pour un même contrôle et permet de démontrer, pour 
une demande précise à une date précise, qu’un engagement a été respecté.
12.7 Transparence envers les personnes
Une personne a le droit de savoir qu’elle a affaire à un agent, de reconnaître un contenu produit par un 
agent et de comprendre une décision qui la concerne.
L’article 50 du RIA, applicable depuis le 2 août 2026, oblige les fournisseurs à concevoir les systèmes 
qui interagissent directement avec des personnes de façon qu’elles sachent qu’elles interagissent avec un 
système d’IA, sauf si c’est évident, et à marquer de façon lisible par machine les contenus synthétiques. 
Les déployeurs divulguent les hypertrucages et les textes générés publiés pour informer le public sur des 
questions d’intérêt public, sauf contrôle éditorial humain. L’information est claire et fournie au plus tard 
lors de la première interaction; un délai transitoire jusqu’au 2 décembre 2026 vise le marquage des systèmes 
déjà sur le marché avant le 2 août 2026[57, 457]. Le cadre va un peu plus loin que ce minimum : il informe toute 
personne, même lorsque l’interaction paraît évidente, et identifie tout contenu d’agent diffusé à l’externe.
Au Québec, la transparence passe aussi par l’avis préalable au profilage (art. 8.1), la confidentialité par 
défaut (art. 9.1), l’information des décisions automatisées (art. 12.1) et le droit d’accès à une transcription 
intelligible (art. 27). Les principes des commissaires à la protection de la vie privée demandent un mécanisme 
de contestation avec révision humaine pour les décisions assistées par l’IA, et pas seulement pour celles 
qui sont entièrement automatisées[438]. Le raisonnement affiché par un modèle n’est pas forcément une 
explication fidèle : l’IMDA rappelle qu’il peut ne pas refléter fidèlement les actions de l’agent[76].
EXIG-CON-19 · DOIT
Divulgation de l’interaction avec un agent
Toute personne qui interagit avec un agent, par écrit ou par la voix, DOIT en être informée clairement 
au plus tard lors de la première interaction, même lorsque la nature artificielle de l’interlocuteur paraît 
évidente (choix du cadre). Un agent NE DOIT PAS se présenter comme une personne.
Pourquoi : article 50 du RIA, que le cadre étend à toutes les interactions pour éviter une appréciation au cas par cas 
de ce qui est « évident »[457].
EXIG-CON-20 · DOIT
Identification des contenus produits par un agent
Tout contenu produit ou substantiellement modifié par un agent et diffusé à l’externe (courriel, publi­
cation, document, image, audio) DOIT être identifié comme tel. Lorsque l’entreprise fournit un système 
génératif visé par l’article 50 du RIA, le marquage DOIT en outre être lisible par machine.
Pourquoi : l’article 50 n’impose l’identification que de certains contenus; l’identification de tout contenu diffusé à 
l’externe est un choix du cadre, qui permet aussi de retrouver la trace d’un contenu en cas d’incident ou de plainte.
EXIG-CON-21 · DOIT
Explication intelligible et canal de révision
Chaque avis de décision rendu à l’égard d’une personne avec l’aide d’un agent, que la décision soit 
entièrement ou partiellement automatisée, DOIT indiquer le canal de révision humaine et ses coor­
données. L’explication fournie sur demande présente en langage clair les principaux facteurs et leur 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 185 sur 283


---
## [Page PDF 186]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
importance relative, sans divulguer l’algorithme ni les poids du modèle; le raisonnement affiché par le 
modèle n’en tient jamais lieu.
Pourquoi : l’interprétation gouvernementale limite l’explication aux facteurs déterminants, et couvrir les décisions 
partiellement automatisées anticipe le projet C-36 et les principes des commissaires[318, 431].
EXIG-CON-22 · DOIT
Vérification humaine du contenu juridique
Tout contenu juridique, réglementaire ou contractuel produit par un agent et destiné à un usage externe 
(tribunal, autorité, client, partenaire) DOIT être vérifié avant sa diffusion par une personne compétente, 
qui confirme que chaque source citée existe et appuie l’énoncé.
Pourquoi : dans Specter Aviation c. Laprade (2025 QCCS 3521), la Cour supérieure du Québec a imposé une sanction 
de 5 000 $, en vertu de l’article 342 du Code de procédure civile, pour le dépôt de références inexistantes générées 
par l’IA[458].
12.8 Incidents agentiques
Un incident agentique se gère comme un incident de sécurité, avec deux particularités  : l’agent peut 
continuer d’agir pendant qu’on l’analyse, et ses effets peuvent exiger une compensation métier.
Le cadre définit l’incident agentique comme une action non autorisée, une fuite de données, une décision 
erronée ayant produit un effet, un contournement de garde-fou ou un emballement des coûts imputable à un 
agent. Un incident de confidentialité au sens de la Loi 25 en est un cas particulier, par exemple un connecteur 
MCP trop permissif qui expose le dossier d’un autre client. L’enjeu n’est pas théorique : en 2024-2025, la 
CAI a reçu 514 avis d’incidents de confidentialité, en hausse de 16 %, dont 80 % du secteur privé, et les accès 
non autorisés y dominent (251 avis)[424].
1
Contenir
Coupe-circuit de l’agent;
révocation de ses jetons
et de ses accès
2
Préserver
Gel des traces, du journal
d’audit et des instantanés
de mémoire
3
Évaluer et aviser
Impact et rayon d’atteinte;
incident de confidentialité :
registre, avis à la CAI et aux
personnes si risque de préjudice
sérieux, avec diligence
4
Corriger et compenser
Compensations des actions
exécutées; correctif; relance
des paliers d’évaluation
5
Apprendre
Retour d’expérience sans
blâme; mise à jour des
contrôles et du cadre
Incident agentique : action non autorisée, fuite de données, décision erronée à effet, contournement de garde-fou ou emballement des coûts
Figure 26 — Réponse à un incident agentique. Les cinq temps se lisent de gauche à droite : on contient l’agent avant de chercher 
la cause, on fige les preuves avant de corriger, puis on évalue, on avise, on répare et on apprend. Source : cadre CRE-IA-2026-01.
1. Contenir. L’équipe de garde actionne le coupe-circuit de l’agent à la passerelle, révoque ses jetons et 
ses accès, suspend ses délégations en cours et annule les actions en attente d’approbation (section 7.8).
2. Préserver. Les traces, le journal d’audit, les instantanés de mémoire et les versions exactes de l’agent, 
du modèle, des invites et des définitions d’outils sont figés. Pour un système à haut risque, le RIA 
interdit au fournisseur, dans l’enquête qui suit le signalement d’un incident grave, d’altérer le système 
d’une manière susceptible de nuire à l’évaluation ultérieure des causes avant d’en informer les autorités 
compétentes (art. 73(6)); le déployeur y est soumis lorsqu’il ne peut joindre le fournisseur (art. 26(5))
[94, 459].
3. Évaluer et aviser. Les traces permettent de mesurer le rayon d’atteinte  : personnes, systèmes et 
partenaires touchés. L’équipe qualifie l’incident au regard de chaque régime (incident de confidentialité, 
atteinte au sens de la LPRPDE, incident technologique au sens du BSIF, incident grave au sens du RIA) 
et déclenche les avis du tableau 51.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 186 sur 283


---
## [Page PDF 187]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
4. Corriger et compenser. Les actions exécutées sont compensées selon le patron saga (section 7.5), le 
correctif est appliqué, puis les paliers d’évaluation sont relancés avant toute remise en service; le niveau 
d’autonomie peut être abaissé.
5. Apprendre. Un retour d’expérience sans blâme met à jour les contrôles, les jeux d’évaluation et, au 
besoin, le cadre.
Tableau 51 — Délais de notification applicables aux incidents agentiques
Régime
Déclencheur
Destinataires
Délai
Loi sur le privé, art. 3.5
Incident de confidentialité 
présentant un risque de préju­
dice sérieux
CAI et personnes 
concernées
« Avec diligence »; aucun délai en heures
Loi sur le privé, art. 3.8, 
et Règlement sur les in­
cidents de confidentiali­
té
Tout incident de confidentia­
lité, même sans risque de pré­
judice sérieux
Registre interne, 
transmis à la CAI sur 
demande
Tenu à jour; conservé au moins cinq ans
LPRPDE
Atteinte présentant un risque 
réel de préjudice grave
Commissariat et per­
sonnes concernées
« Dès que possible »; registre de toutes les 
atteintes conservé 24 mois
Avis du BSIF (2021)
Incident lié à la technologie 
ou à la cybersécurité d’une 
institution financière fédérale
BSIF
Par écrit, dans les 24 heures ou plus tôt si 
possible
RIA, art. 73 (fournisseur) 
et art. 26(5) (déployeur : 
informer d’abord le 
fournisseur)
Incident grave impliquant un 
système à haut risque
Autorités de sur­
veillance du marché
Dès l’établissement d’un lien de causalité (ou 
de sa probabilité raisonnable) et, dans tous 
les cas, au plus tard 15 jours après la prise 
de connaissance de l’incident grave par le 
fournisseur ou, le cas échéant, le déployeur; 
10 jours en cas de décès; 2 jours en cas 
d’infraction généralisée ou de perturbation 
grave et irréversible d’une infrastructure cri­
tique
Cadre (cible interne)
Incident de confidentialité 
présentant un risque de préju­
dice sérieux
CAI
Avis initial visé dans les 72 heures suivant la 
prise de connaissance, complété ensuite
Sources : L.Q. 2021, c. 25; Règlement sur les incidents de confidentialité; Commissariat à la protection de la 
vie privée; BSIF; RIA[56, 62, 426, 427, 434, 459, 460]. Le délai de 72 heures est une cible du cadre, non une 
exigence de la Loi 25.
L’avis écrit à la CAI comporte onze éléments, dont l’organisation et son numéro d’entreprise du Québec 
(NEQ), une personne-ressource, les renseignements visés, les circonstances et la cause, la date ou la période 
de l’incident, la date de prise de connaissance, le nombre de personnes touchées (dont les résidents du 
Québec), les motifs du risque de préjudice et les mesures d’atténuation; les compléments sont transmis 
avec diligence[460]. Le cadre fait produire ces champs à partir de la télémétrie des agents, pour que l’avis ne 
dépende pas d’une reconstitution manuelle.
EXIG-CON-23 · DOIT
Réponse en cinq temps et gel des preuves
Le plan de réponse aux incidents de chaque agent DOIT suivre les cinq temps de la figure 26. La 
contention (coupe-circuit et révocation des jetons) DOIT être exécutable par l’équipe de garde sans 
approbation préalable, et le gel des traces, du journal d’audit, des instantanés de mémoire et des versions 
exactes de l’agent, du modèle, des invites et des définitions d’outils précède toute correction.
Pourquoi : sans versions figées, l’analyse des causes devient impossible; MANAGE 2.4 demande des mécanismes et 
des responsabilités clairs pour désactiver un système[74].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 187 sur 283


---
## [Page PDF 188]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
EXIG-CON-24 · DOIT
Registre et avis des incidents de confidentialité
Tout incident de confidentialité impliquant un agent DOIT être inscrit au registre des incidents avec le 
contenu prévu par le Règlement sur les incidents de confidentialité et conservé au moins cinq ans. S’il 
présente un risque de préjudice sérieux, la CAI et les personnes concernées sont avisées avec diligence; 
le cadre fixe une cible interne de 72 heures pour l’avis initial à la CAI, que l’équipe de réponse DEVRAIT 
respecter (choix du cadre).
Pourquoi : articles 3.5 et 3.8 de la Loi sur le privé et articles 7 et 8 du règlement; la loi n’impose aucun délai en heures, 
d’où une cible interne explicite[56, 414, 460].
EXIG-CON-25 · DOIT
Règle la plus exigeante entre régimes de notification
Le plan de réponse DOIT recenser, pour chaque agent, les régimes de notification applicables (Loi 25, 
LPRPDE, BSIF, RIA) et appliquer le plus exigeant : registre unique conservé cinq ans, double analyse 
du « préjudice sérieux » (Québec) et du « risque réel de préjudice grave » (fédéral), délais du tableau 
51. L’événement d’incident produit à partir de la télémétrie comporte les champs de l’avis exigé par le 
règlement québécois.
Pourquoi : une organisation soumise à plusieurs régimes doit pouvoir satisfaire le plus strict sans reconstituer les 
faits sous la pression du délai.
12.9 Évaluation d’impact unifiée
Plutôt que plusieurs analyses rédigées par plusieurs équipes, le cadre exige un seul livrable par agent de 
classe élevée, structuré pour répondre à chaque régime.
Les régimes se recoupent largement. L’EFVP examine les RP et leur parcours. L’analyse d’impact sur les 
droits fondamentaux (AIDF) du RIA est obligatoire avant la première utilisation pour les déployeurs qui sont 
des organismes de droit public, les entités privées qui fournissent des services publics et les déployeurs de 
systèmes d’évaluation de la solvabilité ou de tarification en assurance vie et maladie; elle décrit les processus, 
la durée et la fréquence d’utilisation, les personnes touchées, les risques, les mesures de supervision humaine 
et les mesures prévues si les risques se matérialisent, peut renvoyer aux sections pertinentes de l’analyse 
d’impact relative à la protection des données (AIPD) du règlement général sur la protection des données 
(RGPD, art. 35) ou en intégrer des parties lorsque celle-ci remplit déjà certaines obligations (art. 27(4), tel 
que modifié par le règlement (UE) 2026/1744), et est notifiée à l’autorité de surveillance du marché[58, 61, 461]. 
ISO/IEC 42005:2025 fournit la méthode : quand et comment évaluer l’impact sur les personnes et la société, 
et comment l’intégrer au SMIA[452]. Un seul livrable évite que les mêmes faits soient décrits trois fois, avec 
trois versions différentes.
Tableau 52 — Volets de l’évaluation d’impact unifiée
Volet
Source
Contenu minimal
Obligatoire lorsque
Vie privée (EFVP)
Loi sur le privé, art. 3.3 
et 17; Loi sur l’accès, 
art. 63.5 et 70.1
Inventaire et parcours des RP par outil, dé­
légation et mémoire; conformité; risques et 
atténuation; nécessité et proportionnalité; 
lieux de traitement
Projet impliquant des RP; com­
munication hors Québec
Droits fondamentaux 
(AIDF)
RIA, art. 27
Processus, durée et fréquence d’utilisation; 
personnes touchées; risques; supervision 
humaine; mesures si le risque se matéria­
lise
Déployeurs visés par l’article 27, 
avant la première utilisation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 188 sur 283


---
## [Page PDF 189]

CRE-IA-2026-01 · Cadre de référence
12 Risques, conformité et réglementation
Volet
Source
Contenu minimal
Obligatoire lorsque
Impact algorith­
mique
Recommandation du 
gouvernement du 
Québec; EIA fédérale
Erreurs, discrimination et biais; niveau 
d’incidence
Tout agent qui décide ou recom­
mande à l’égard d’une personne 
(choix du cadre); EIA pour les ins­
titutions fédérales assujetties à la 
directive
Impact sur les per­
sonnes et la société
ISO/IEC 42005; ISO/
IEC 42001, 6.1.4 et A.5
Méthode, moments du cycle de vie, docu­
mentation et intégration au SMIA
Méthode de référence du cadre 
pour tous les volets
Décision sur le 
risque résiduel
Cadre
Classe, niveau d’autonomie, mesures rete­
nues, risque résiduel accepté par le pro­
priétaire métier et par le comité
Avant l’homologation et avant 
tout relèvement du niveau 
d’autonomie
Sources :[318, 413, 432, 452, 461].
EXIG-CON-26 · DOIT
Évaluation d’impact unifiée par agent de classe élevée
Chaque agent de classe élevée DOIT disposer d’une évaluation d’impact unifiée couvrant les volets 
applicables du tableau 52, approuvée par le propriétaire métier et par le comité d’architecture et des 
risques agentiques avant le passage en pilote et avant tout relèvement de son niveau d’autonomie. Elle 
est mise à jour à chaque déclencheur de l’EXIG-CON-03, revue au moins une fois par année (choix du 
cadre) et référencée dans la fiche d’agent (annexe B).
Pourquoi : l’AIDF peut s’appuyer sur l’AIPD (art. 27(4)) et ISO/IEC 42005 fournit une méthode commune; un livrable 
unique garde les faits cohérents entre régimes[452, 461].
À RETENIR
La classe de risque commande tout le reste  : plafond d’autonomie, EFVP et évaluation d’impact, 
fréquence des revues, intensité des tests. Une décision qu’aucun humain n’a réellement examinée reste 
automatisée, quel que soit le bouton cliqué. Les délais légaux de notification diffèrent selon les régimes; 
le cadre applique toujours le plus exigeant et s’appuie sur une base de preuves unique.
13 Approvisionnement et clauses contractuelles
Les protocoles d’interopérabilité relèvent désormais d’une gouvernance neutre; le risque de dépendance 
s’est donc déplacé vers les plateformes, leurs extensions et les données qu’elles accumulent. Ce chapitre 
traduit le cadre en critères d’évaluation des fournisseurs, en dix clauses contractuelles normatives et en une 
grille de notation. Il s’adresse aux acheteurs, aux juristes, aux architectes et au responsable de la protection 
des renseignements personnels qui négocient l’acquisition d’une plateforme d’agents, d’un service de 
modèles, d’une passerelle, d’un serveur MCP ou d’un agent de tiers.
13.1 Où se situe désormais le risque de verrouillage
Cette section localise le risque de dépendance envers un fournisseur (vendor lock-in), afin de concentrer la 
négociation là où il se trouve réellement.
Des protocoles sous gouvernance neutre
Le Model Context Protocol (MCP) a été versé à l’Agentic AI Foundation (AAIF), fondation hébergée par la 
Linux Foundation, dès sa création le 9 décembre 2025; AWS, Google et Microsoft figurent parmi ses membres 
Platine[4]. Le protocole Agent2Agent (A2A) est devenu un projet hébergé de l’AAIF le 17 août 2026[5, 35]; 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 189 sur 283


---
## [Page PDF 190]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
son comité directeur technique réunit huit entreprises concurrentes : AWS, Cisco, Google, IBM Research, 
Microsoft, Salesforce, SAP et ServiceNow[29]. Le risque qu’un protocole du catalogue disparaisse ou passe 
sous le contrôle d’un seul éditeur est donc faible. Un projet n’est toutefois un « standard AAIF » qu’une 
fois son admission approuvée et annoncée[42]; au 27 octobre 2026, la candidature d’AGNTCY demeure sans 
décision[37] (voir section 6.9).
Un risque déplacé vers les plateformes
Un protocole ouvert ne rend pas la plateforme ouverte. Le verrouillage se loge désormais dans cinq endroits, 
résumés au tableau 53. Des éditeurs de passerelles soutiennent en outre que la gouvernance native d’une 
plateforme s’arrête à sa frontière et ne suit pas l’agent qui en sort[44, 45]. C’est un argument d’éditeurs, mais 
il décrit bien le risque que le cadre traite par sa passerelle d’agents et son registre d’entreprise (section 9.4 et 
section 11.4). Les exemples du tableau illustrent des mécanismes; ils ne jugent pas des produits qui évoluent 
rapidement.
Tableau 53 — Où se loge le verrouillage (état au 27 octobre 2026)
Lieu
Manifestation
Exemple documenté
Parade du cadre
Extensions de 
protocole
Une fonction essentielle 
n’existe que par une ex­
tension propre à l’éditeur.
A2A permet de déclarer une extension obligatoire 
(required) dans capabilities.extensions [238]; MCP 
admet des extensions à préfixe DNS inversé, désacti­
vées par défaut[169].
EXIG-APP-02 et 
EXIG-APP-07
Couverture par­
tielle
« Prend en charge MCP » 
ne vise qu’une partie des 
primitives ou des liaisons.
Azure API Management gère les outils MCP, mais ni 
les ressources ni les invites, et les agents A2A en 
JSON-RPC seulement[108, 109]; le greffon AI A2A Proxy 
de Kong Gateway (3.14 et plus, édition AI Gateway 
Enterprise) ne gère pas l’état des tâches[111].
Preuves par essais 
(EXIG-APP-03)
Contraintes de 
produit
Les 
limites d’orchestration du 
produit deviennent celles 
de l’architecture.
Agentforce limite volontairement la délégation entre 
organisations Salesforce à un seul niveau et signale, 
pour Agent Script, une limite actuelle de sept sous-
agents connectés[49].
Logique d’orchestration 
détenue par l’entreprise 
(PRIN-09, chapitre 7)
Plan de contrôle 
et identité
L’inventaire, l’arrêt et 
l’identité des agents dé­
pendent de la console de 
l’éditeur.
Copilot Studio crée d’office une identité Entra Agent 
ID pour chaque nouvel agent depuis juillet 2026[48]; 
les fonctions de sécurité associées exigent une li­
cence Agent 365[324], dont les actions de cycle de vie 
sur des agents infonuagiques tiers sont annoncées 
comme à venir[46].
EXIG-APP-06 et 
EXIG-APP-16
Données, défini­
tions et unités
Mémoires, invites sys­
tème, journaux et uni­
tés de facturation propres 
rendent la sortie coû­
teuse.
Copilot Studio facture en crédits et désactive les 
agents personnalisés au-delà de 125 % de la capaci­
té prépayée[53].
EXIG-APP-05 et 
EXIG-APP-14
À RETENIR
Le protocole est ouvert; il faut négocier l’ouverture là où elle se perd : la couverture réelle du protocole, 
l’identité des agents, leur arrêt, leurs données et leurs définitions doivent rester sous le contrôle de 
l’entreprise.
EXIG-APP-01 · DOIT
Analyse de réversibilité avant tout engagement
Toute acquisition d’une plateforme d’agents, d’un service de modèles, d’une passerelle ou d’un agent 
de tiers DOIT être précédée d’une analyse de réversibilité documentée : composants et extensions 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 190 sur 283


---
## [Page PDF 191]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
propriétaires utilisés, données et définitions à récupérer, formats de restitution, délai et coût estimés de 
sortie. L’architecture d’entreprise DOIT la valider, et l’analyse DOIT être versée au registre.
Pourquoi : le coût de sortie se décide à la signature, pas à la résiliation.
EXIG-APP-02 · NE DOIT PAS
Aucune dépendance à une extension non approuvée
Un agent ou un outil de l’entreprise NE DOIT PAS dépendre d’une extension de protocole propriétaire 
absente du catalogue (section 6.3). Une extension admise DOIT être identifiée par son URI ou son 
préfixe versionné et posséder un comportement de repli documenté; elle NE DOIT PAS être déclarée 
obligatoire envers des clients, sauf dérogation (section 11.6).
Pourquoi : une extension obligatoire recrée, au-dessus d’un protocole ouvert, la dépendance que ce protocole devait 
éliminer.
13.2 Critères d’évaluation des fournisseurs
Cette section fixe ce qu’un fournisseur doit démontrer, et comment. Le principe est simple : une preuve 
reproductible dans l’environnement de l’entreprise l’emporte toujours sur une allégation commerciale.
Interopérabilité protocolaire
La révision courante de MCP est 2026-07-28[34]. Le projet publie un cadre officiel de tests de conformité, 
encore en versions 0.x (0.1.16 sur le tag latest de npm, préversions 0.2.0-alpha en cours)[225, 226] : ses résultats 
sont utiles, mais l’entreprise doit les compléter par ses propres scénarios. Pour A2A 1.0, la trousse officielle 
a2a-tck teste les trois liaisons standard selon les niveaux MUST, SHOULD et MAY, à partir des interfaces 
déclarées dans la carte d’agent[243]. Le fournisseur précise enfin comment il suivra les dépréciations : MCP 
maintient une fonctionnalité dépréciée au moins douze mois, ou au moins 90 jours en cas de retrait accéléré 
exceptionnel, avant de pouvoir la retirer[34, 196].
Observabilité et données de coûts
Les conventions GenAI d’OpenTelemetry sont toutes au niveau de stabilité Development et ont été dépla­
cées en mai 2026 (déclarées obsolètes dans semantic-conventions à la v1.42.0, le 12 juin 2026) vers un dépôt 
dédié qui n’a encore publié aucune version étiquetée[180, 181, 462]. « Compatible OpenTelemetry » ne suffit donc 
pas : le fournisseur déclare la version qu’il émet, et l’entreprise vérifie la propagation du contexte de trace à 
chaque saut. Par exemple, le SDK Python de Microsoft Agent Framework propage le contexte W3C vers les 
serveurs MCP que l’agent ouvre lui-même, mais pas vers les outils MCP hébergés par un fournisseur[295]. 
Pour les coûts, FOCUS (FinOps Open Cost and Usage Specification) 1.4 (ratifiée le 4 juin 2026) normalise 
les données de facturation, sans définir d’indicateurs par agent[408, 463, 464]; FOCUS 1.5, dont la ratification 
est prévue le 3 décembre 2026, prévoit, dans son brouillon de travail, l’identité du modèle et le détail des 
jetons[465]. Le coût par tâche réussie se calcule en joignant ces données à la télémétrie (section 10.6).
Identité, délégation et arrêt
Le cadre exige une identité non humaine distincte par agent (section 9.2); la réutilisation d’identités (NHI9) 
et les secrets de longue durée (NHI7) figurent au Top 10 des identités non humaines de l’OWASP[91]. MCP 
impose un jeton propre à chaque serveur et interdit de relayer un jeton reçu, mais n’exige ni l’échange 
de jetons de la RFC 8693 ni la revendication act [209] : la délégation vérifiable relève donc d’une exigence 
contractuelle distincte (EXIG-APP-08). Les sept portes de conception publiées par MuleSoft pour un plan de 
contrôle d’agents, dont la neutralité de l’application des politiques au niveau du transport et la propagation 
vérifiée de l’identité humaine déléguée, forment une grille complémentaire que le cadre retient comme 
critères d’acceptation d’une passerelle d’agents (section 9.4)[45].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 191 sur 283


---
## [Page PDF 192]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
Performance mesurée, pas annoncée
Les chiffres publiés ne se comparent pas. TrueFoundry indique dans sa documentation une latence ajoutée 
généralement inférieure à 5 ms, alors que son propre banc d’essai montre de +7 à +12 ms sur 1 vCPU, entre 
200 et 370 requêtes par seconde selon le niveau de traçage[143, 144]. L’équipe d’agentgateway déclare environ 
500 000 requêtes par seconde et une latence P99 inférieure à 0,2 ms à 30 000 requêtes par seconde, sans 
préciser le type de trafic ni le matériel[142]. Aucune de ces sources ne précise si l’inspection des politiques 
agentiques était active pendant la mesure.
EXIG-APP-03 · DOIT
Preuves de conformité protocolaire
Le fournisseur DOIT démontrer la prise en charge de MCP 2026-07-28 et d’A2A 1.0 par des essais 
reproductibles dans l’environnement de l’entreprise : rapport a2a-tck sans échec de niveau MUST pour 
chaque liaison déclarée, scénarios de conformité MCP exécutés avec le cadre officiel ou une suite équi­
valente approuvée par l’architecture d’entreprise, et liste explicite des primitives, liaisons et versions 
non prises en charge.
Pourquoi : « prend en charge » couvre souvent une partie seulement du protocole (tableau 53).
EXIG-APP-04 · DOIT
Mesures de performance reproductibles
Toute valeur de latence ajoutée, de débit ou de disponibilité invoquée par un fournisseur DOIT être 
mesurée dans les conditions de l’entreprise, politiques, traçage et journalisation actifs, aux 50e et 99e 
centiles (P50 et P99), avec la méthode, le matériel, le type de trafic et les données brutes. Une valeur 
publiée par le fournisseur NE DOIT PAS servir d’exigence ni de critère de notation.
Pourquoi : les allégations publiques sont incomparables, parfois contradictoires.
EXIG-APP-05 · DOIT
Télémétrie et données de coûts ouvertes
La solution DOIT exporter traces, métriques et journaux par OTLP selon une version déclarée et 
épinglée des conventions GenAI, propager le contexte W3C Trace Context sur chaque saut qu’elle 
contrôle et fournir ses données de facturation au format FOCUS 1.4 ou ultérieur, avec la correspondance 
entre ses unités propres (crédits, messages) et les jetons consommés.
Pourquoi : sans traces ni coûts exportables, l’entreprise ne peut ni auditer ses agents ni comparer ses fournisseurs 
(section 10.1).
EXIG-APP-06 · DOIT
Identité et arrêt sous le contrôle de l’entreprise
La solution DOIT attribuer à chaque agent une identité non humaine distincte, fédérable au fournis­
seur d’identité de l’entreprise et sans clé statique partagée, et permettre à l’entreprise de suspendre 
ou de révoquer un agent, ses jetons et ses sessions depuis ses propres outils, par exemple au moyen 
d’événements CAEP[344], sans attendre une intervention du fournisseur.
Pourquoi : un coupe-circuit qui dépend de la console d’un éditeur n’est pas un coupe-circuit d’entreprise (section 9.4).
13.3 Clauses contractuelles normatives
Les dix clauses suivantes sont des exigences minimales. Elles s’insèrent dans tout contrat d’acquisition ou 
de renouvellement visé par ce chapitre; leur rédaction juridique relève des affaires juridiques. Les délais 
marqués « cible du cadre » sont des choix internes, ajustables par dérogation (section 11.6). Dans ce chapitre, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 192 sur 283
