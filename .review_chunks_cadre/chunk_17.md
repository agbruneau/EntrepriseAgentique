# chunk_17 — pages PDF 161 à 172 (sur 283)



---
## [Page PDF 161]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
Rôle
Responsabilités principales
Fondement ou remarque
Responsable de la 
protection des RP 
(RPRP)
Est consulté dès le début de tout projet impliquant des RP; encadre les 
EFVP; approuve les politiques de gouvernance des RP; dirige le traite­
ment des incidents de confidentialité (choix du cadre).
Loi sur le privé, art. 3.1 à 3.3.
Comité d’architecture 
et des risques agen­
tiques
Approuve les agents de classe élevée et tout niveau N4; accorde les 
dérogations; approuve le catalogue des protocoles; révise le cadre 
chaque semestre.
Instance décisionnelle du 
cadre (EXIG-GOV-02).
Approbateurs hu­
mains
Approuvent ou refusent, sur la base de l’action exacte, les actions que 
la section 8.4 soumet à approbation.
Personnes compétentes, for­
mées et dotées de l’autorité 
nécessaire (règlement euro­
péen sur l’IA, ou RIA, art. 26).
Équipe de garde
Surveille l’agent en production, reçoit les escalades, suspend l’agent 
au besoin et applique les procédures d’incident.
Joignable pendant les heures 
d’exploitation déclarées.
L’exigence relative aux approbateurs s’inspire du règlement européen sur l’IA : le déployeur d’un système 
à haut risque confie la supervision humaine à des personnes compétentes, formées et dotées de l’autorité 
nécessaire (art. 26)[61, 94]. Pour les systèmes de l’annexe III, cette obligation s’applique à compter du 2 
décembre 2027 (2 août 2028 pour ceux de l’annexe I, soit les produits réglementés)[58]. Le cadre l’étend à 
tous les agents, quelle que soit leur classe (EXIG-AUT-15).
EXIG-GOV-01 · DOIT
Responsables nommés pour chaque agent
Chaque agent et chaque serveur MCP inscrits au registre DOIVENT avoir un propriétaire métier 
(parrain) et un responsable technique désignés nommément, ainsi qu’une équipe de garde joignable 
pendant les heures d’exploitation déclarées. Pour un agent intégré à un logiciel-service ou exploité par 
un partenaire, le parrain est la personne interne qui répond de son usage et du contrat.
Pourquoi : une responsabilité confiée à « l’équipe » ou au fournisseur n’est exercée par personne; l’OWASP place 
le retrait inadéquat des identités non humaines, typique des agents orphelins, au premier rang de son NHI Top 10 
(NHI1)[91].
EXIG-GOV-02 · DOIT
Comité d’architecture et des risques agentiques
L’entreprise DOIT constituer un comité d’architecture et des risques agentiques doté d’un mandat 
écrit qui précise sa composition (au minimum l’architecture d’entreprise, la sécurité de l’information, 
la fonction risques et conformité, le RPRP ou son délégué, l’équipe plateforme et des représentants des 
domaines métier), son quorum, ses pouvoirs et la fréquence de ses réunions. Ses décisions DOIVENT 
être motivées et consignées au registre.
Pourquoi : les décisions qui engagent l’entreprise (niveau N4, agent de classe élevée, dérogation, catalogue des 
protocoles) exigent une instance qui réunit les expertises et dont les arbitrages laissent une trace vérifiable.
EXIG-GOV-03 · NE DOIT PAS
Séparation des fonctions
Une même personne NE DOIT PAS à la fois préparer et approuver une décision du cycle de vie d’un 
agent : le responsable technique d’un agent n’homologue pas sa mise en production, n’accorde pas une 
dérogation qui le vise et n’approuve pas les actions P3 de cet agent.
Pourquoi : la séparation des fonctions est le contrôle le plus simple contre l’erreur et la complaisance; elle donne 
son sens au « A » de la matrice RACI.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 161 sur 283


---
## [Page PDF 162]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
11.2 Matrice RACI
Cette section attribue chaque activité du cycle de vie à un rôle qui réalise (R), à un seul rôle qui approuve et 
répond (A), aux rôles consultés (C) et aux rôles informés (I). Le tiret signifie « non concerné ». Abréviations 
des colonnes : PM, propriétaire métier (parrain); RT, responsable technique; PL, équipe plateforme; AE, 
architecture d’entreprise; SÉC, sécurité de l’information; RC, risques et conformité; RPRP, responsable de 
la protection des RP; CO, comité d’architecture et des risques agentiques.
Tableau 44 — Matrice RACI du cycle de vie d’un agent
Activité
PM
RT
PL
AE
SÉC
RC
RPRP
CO
Inscrire l’agent au registre
A
R
C
I
I
I
—
—
Classer le risque de l’agent
R
C
—
C
C
A
C
I
Fixer le niveau d’autonomie
A
R
—
C
C
C
—
I
Classer les outils par palier (P0 à P3)
C
R
C
I
A
C
C
—
Concevoir, construire et évaluer
C
A, R
C
C
C
I
I
—
Réaliser l’EFVP
A
R
I
I
C
C
C
—
Homologuer la mise en production (le responsable tech­
nique prépare le dossier, il ne décide pas)
A
R
C
C
C
C
C
I
Exploiter et surveiller
I
A, R
R
—
C
I
—
—
Gérer un incident
I
R
R
I
A
C
C
I
Accorder une dérogation
R
C
I
R
C
C
C
A
Attester périodiquement l’agent
A, R
C
I
—
I
I
—
—
Retirer l’agent
A
R
R
I
C
I
C
—
Réviser le catalogue des protocoles
I
I
C
R
C
C
—
A
Trois règles complètent la matrice. Pour un agent de classe élevée ou visant le niveau N4, le comité devient 
A pour le niveau d’autonomie et l’homologation, et le propriétaire métier devient R. Pour un incident de 
confidentialité, le cadre confie au RPRP le rôle A pour l’évaluation du préjudice, les avis et l’inscription au 
registre des incidents prévus aux articles 3.5 à 3.8 de la Loi sur le privé (section 12.8). Enfin, l’équipe de 
garde exécute, pour le responsable technique, les tâches R de l’exploitation et de la gestion des incidents.
Le classement du risque revient à la fonction risques et conformité plutôt qu’au parrain : celui qui souhaite 
déployer l’agent propose la classe, une fonction indépendante la tranche. De même, la sécurité valide le 
palier d’un outil, parce que ce palier détermine les contrôles exigés (section 8.3).
EXIG-GOV-04 · DOIT
Un seul A, des personnes nommées
Chaque activité de tableau 44 DOIT avoir un et un seul rôle A. La fiche de chaque agent DOIT nommer 
les personnes qui tiennent, pour cet agent, les rôles R et A de la matrice, y compris, pour chaque 
combinaison de classe de risque et de palier d’outil, les approbateurs humains (EXIG-AUT-15); une fiche 
dont un rôle A est vacant est incomplète.
Pourquoi : deux « A » diluent la responsabilité, et une matrice sans noms ne sert à rien le jour d’un incident.
11.3 Modèle opérationnel en étoile
Cette section fixe la répartition du travail entre une plateforme centrale et les domaines métier (figure 24 
et tableau 45). Le cadre retient un modèle en étoile (hub-and-spoke) : la plateforme fournit et opère le socle 
commun; les domaines bâtissent et exploitent leurs agents en libre-service; la sécurité, les risques et la 
gouvernance encadrent les deux.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 162 sur 283


---
## [Page PDF 163]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
Ce choix évite deux échecs connus. Tout centraliser crée un goulot d’étranglement : chaque agent attend une 
équipe qui ne connaît pas le métier. Tout décentraliser multiplie les passerelles, les registres et les façons de 
gérer les identités, donc les failles. Dans le modèle en étoile, un contrôle s’écrit une fois dans la plateforme 
et s’applique partout, tandis que la logique métier reste la propriété des domaines.
Sécurité, risques et gouvernance : politiques, audit, approbations
Plateforme
agentique centrale
passerelles, catalogue,
registre, gabarits,
observabilité, évaluation
Finance
MCP, agents, budget
Ressources humaines
MCP, agents, budget
Service à la clientèle
MCP, agents, budget
Opérations TI
MCP, agents, budget
Approvisionnement
MCP, agents, budget
Ventes
MCP, agents, budget
Plateforme centrale — fournit et opère
Passerelles de modèles et d’agents, bus d’événements,
catalogue et registre, gabarits (SDK, CI/CD, traçage),
outillage d’évaluation, tableaux de bord de coûts,
coupe-circuit global.
Domaines métier — bâtissent et exploitent
Serveurs MCP de domaine et logique des agents,
classement des outils par palier, jeux d’évaluation
métier, budget et imputation, propriétaire nommé
et équipe de garde pour chaque agent.
Sécurité, risques, gouvernance — encadrent
Politiques d’identité, paliers et seuils d’approbation,
tests d’abus et d’intrusion, audit des contrôles,
dérogations; le comité approuve le niveau N4 et
les agents à risque élevé.
Figure 24 — Modèle opérationnel en étoile. La plateforme centrale fournit une seule fois les passerelles, le registre, les gabarits 
et le coupe-circuit; chaque domaine y branche ses serveurs MCP et ses agents; la sécurité, les risques et la gouvernance encadrent 
l’ensemble. Source : CRE-IA-2026-01; les six domaines sont donnés à titre d’exemple.
Tableau 45 — Répartition des responsabilités dans le modèle en étoile
Responsabilité
Plateforme centrale
Domaines métier
Sécurité, risques et gou­
vernance
Passerelles de modèles et d’agents, 
bus d’événements
R, A : conçoit, opère, sécu­
rise
C : consomme en libre-
service
C : audite les contrôles
Registre, catalogue et coupe-circuit 
global
R, A : opère l’outillage
R : tient ses fiches et 
contrats à jour
C : vérifie la complétude; 
peut déclencher le coupe-
circuit
Gabarits d’agents (trousses de déve­
loppement, CI/CD, traçage)
R, A : fournit et maintient
I : instancie
C : valide les contrôles inté­
grés
Serveurs MCP de domaine et logique 
des agents
C : accompagne
R, A : développe, teste, 
exploite
C : impose les tests d’abus
Classement des outils par palier
C : inscrit au catalogue
R : propose
A : valide selon la politique 
des paliers
Jeux d’évaluation métier
C : outille la chaîne 
d’évaluation
R, A : définit les scénarios
C : exige les cas adverses
Politiques d’identité et seuils 
d’approbation
R : applique dans les passe­
relles
C : décrit les cas métier
A : définit
Budget et imputation des coûts
R : mesure et expose les 
coûts
A : maîtrise son budget
I
EXIG-GOV-05 · DOIT
Socle commun obligatoire
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 163 sur 283


---
## [Page PDF 164]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
Les domaines métier DOIVENT utiliser les passerelles, le registre, le catalogue, la chaîne de traçage 
et le coupe-circuit fournis par la plateforme. Un domaine NE DOIT PAS exploiter de passerelle, de 
registre ou de catalogue parallèle sans dérogation (section 11.6).
Pourquoi : un contrôle appliqué en deux endroits finit par diverger; la règle centrale de l’architecture veut que rien 
n’atteigne un outil, une donnée ou un agent hors domaine sans la passerelle et le catalogue (section 5.1).
EXIG-GOV-06 · DEVRAIT
Conformité par construction
La plateforme DEVRAIT fournir des gabarits d’agents qui intègrent par défaut l’identité propre de 
l’agent, la propagation du contexte de trace, les plafonds de coût, de jetons et d’itérations, l’appel aux 
outils par la passerelle et l’inscription au registre, de sorte que le chemin conforme soit aussi le plus 
court pour une équipe de domaine.
Pourquoi : un contrôle livré dans le gabarit coûte une fois; un contrôle exigé en revue coûte à chaque agent et se 
contourne sous la pression des échéances.
11.4 Registre d’entreprise des agents et serveurs MCP
Cette section définit le registre, inventaire faisant autorité de tous les agents et serveurs MCP de l’entreprise. 
On ne gouverne pas ce qu’on ne voit pas : le registre est la condition de tous les autres contrôles.
Le NIST AI RMF, d’application volontaire, prévoit des mécanismes d’inventaire des systèmes d’IA, dotés 
de ressources selon les priorités de risque (GOVERN 1.6)[74]. Pour les institutions financières fédérales, la 
ligne directrice E-23 du BSIF, en vigueur le 1er mai 2027, exige un inventaire d’entreprise des modèles à 
risque non négligeable, y compris ceux des fournisseurs, et une cote de risque qui détermine l’intensité de 
la gouvernance[8]. Le registre du cadre répond à ces deux attentes : il couvre les agents tiers et consigne les 
modèles utilisés.
Contenu et états de la fiche
Chaque agent et chaque serveur MCP a une fiche, dont le gabarit complet figure à l’annexe B. Elle consigne 
au minimum l’identification et la version; le parrain, le responsable technique, l’équipe de garde et les 
approbateurs; la finalité et les mandants autorisés; la classe de risque et le niveau d’autonomie approuvés; 
les outils appelés et leurs paliers; les modèles et leurs versions; les données touchées et la présence de RP; 
l’identité et les portées; les résultats d’évaluation; le budget et les plafonds; l’état de cycle de vie, les dates 
de revue et les dérogations en vigueur. Le niveau d’autonomie inscrit tient lieu, à l’interne, de « certificat 
d’autonomie » tel que le conçoivent Feng, McDonald et Zhang (qui le font délivrer par un tiers) : un plafond 
lisible par les autres agents et par la passerelle, valable pour une configuration donnée[83].
La fiche passe par sept états : « proposé », « en conception », « en construction », « pilote », « production », 
« suspendu » et « retiré ». Seuls les états « pilote » et « production » permettent d’obtenir des justificatifs 
d’exécution en production.
Registre et catalogue
Le registre répond aux questions « qui, quoi, pourquoi et avec quel risque »; le catalogue d’entreprise 
(section 6.8) répond à « par quel contrat et dans quelle version ». Les deux partagent l’identifiant de l’agent 
ou du serveur, ce qui permet à la passerelle de vérifier à chaque appel l’état de la fiche et la version épinglée 
du contrat. Le registre d’entreprise est distinct du registre officiel MCP : celui-ci, en préversion depuis le 8 
septembre 2025, ne contient que des métadonnées de serveurs publics, ne prend pas en charge les serveurs 
privés et recommande aux entreprises d’opérer leur propre sous-registre[25, 43]. Il peut servir de source de 
découverte, jamais de registre d’entreprise.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 164 sur 283


---
## [Page PDF 165]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
Exemples de mise en œuvre
Plusieurs produits couvrent une partie du rôle; ce sont des exemples non limitatifs, à l’état du 27 octobre 
2026. Microsoft Agent 365, en disponibilité générale depuis le 1er mai 2026, offre un registre et des contrôles 
comme le blocage des agents non gérés[46]. Amazon Bedrock AgentCore Registry tient un catalogue 
gouverné d’agents, de serveurs MCP, d’outils et de compétences, avec un flux de publication, de revue et 
d’approbation[102]. Azure API Center sert de registre privé pour découvrir les serveurs MCP d’une organi­
sation[108]. ServiceNow a annoncé le 5 mai 2026 l’extension de son AI Control Tower à la découverte des 
actifs d’IA déployés par 30 nouvelles intégrations et à un coupe-circuit[47].
ATTENTION
Un registre de plateforme voit d’abord les agents de sa propre plateforme. Au 1er mai 2026, la synchro­
nisation du registre d’Agent 365 avec Amazon Bedrock et Google Cloud était en préversion publique, 
et les actions de cycle de vie sur les agents infonuagiques tiers étaient annoncées comme à venir[46]. 
Le registre d’entreprise est donc un rôle d’architecture alimenté par plusieurs sources, et la suspension 
d’un agent s’applique à la passerelle d’agents, pas seulement dans la console de son éditeur.
EXIG-GOV-07 · DOIT
Inventaire complet
Le registre DOIT inventorier tout agent et tout serveur MCP qui agit dans le périmètre de l’entreprise, 
qu’il soit développé à l’interne, intégré à un logiciel-service ou exploité par un partenaire, avec une 
fiche conforme à l’annexe B, y compris les modèles utilisés et leurs versions.
Pourquoi  : le NIST AI RMF range les logiciels, données et composants de tiers parmi les risques à gouverner 
(GOVERN 6.1 et 6.2)[74]; un agent tiers absent du registre échappe à toute revue.
EXIG-GOV-08 · NE DOIT PAS
Sans fiche, aucun justificatif
Une identité d’agent ou de serveur MCP NE DOIT PAS recevoir de justificatif valide en production 
tant que sa fiche n’est pas complète, approuvée et à l’état « pilote » ou « production ». La passerelle 
d’agents DOIT refuser tout appel d’une identité absente du registre ou à l’état « suspendu ».
Pourquoi : lier l’émission des justificatifs à l’état du registre transforme l’inventaire en contrôle d’accès; un agent 
non inscrit ne peut rien faire.
EXIG-GOV-09 · DOIT
Fiche à jour ou agent suspendu
La fiche DOIT être mise à jour avant la mise en œuvre de tout changement qui en modifie le contenu. 
Un agent dont l’attestation périodique est échue, ou dont un rôle A est vacant depuis plus de 30 jours, 
DOIT passer à l’état « suspendu » jusqu’à sa régularisation. Le délai de 30 jours est un choix du cadre.
Pourquoi : une fiche périmée donne une fausse assurance; la suspension rend le coût de la négligence visible pour 
le parrain plutôt que pour la sécurité.
EXIG-GOV-10 · DOIT
Détection des agents hors registre
L’équipe plateforme DOIT, au moins chaque mois, rapprocher le registre de sources indépendantes 
(journaux des passerelles, identités d’agents du fournisseur d’identité, inventaires des logiciels-services, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 165 sur 283


---
## [Page PDF 166]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
facturation des fournisseurs de modèles) et placer en quarantaine tout agent découvert hors registre 
jusqu’à son inscription ou son retrait. La fréquence mensuelle est un choix du cadre.
Pourquoi  : les agents fantômes naissent hors des processus; seul un rapprochement avec ce que les systèmes 
observent réellement les fait apparaître. Certaines plateformes facilitent ce rapprochement : depuis juillet 2026, 
Copilot Studio crée automatiquement une identité Entra Agent ID pour chaque nouvel agent[48].
11.5 Cycle de vie et points de contrôle
Cette section découpe la vie d’un agent en six étapes, chacune fermée par un point de contrôle qui laisse 
une preuve au registre. L’intensité des contrôles suit la classe de risque : un agent de classe faible franchit 
les mêmes portes qu’un agent de classe élevée, avec des preuves plus légères.
1
Proposition
2
Conception
3
Construction
4
Pilote
5
Production
6
Retrait
ÉTAPES
Cas d’usage, valeur
attendue, propriétaire
métier nommé
Classe de risque, niveau
d’autonomie, patron,
contrats, EFVP
Gabarits de plateforme,
jeu de référence,
tests de sécurité
Périmètre et durée
bornés, un niveau
sous la cible
Surveillance, évaluation
continue, gestion
des changements
Révocation des identités,
retrait du catalogue,
archivage, avis
POINTS DE CONTRÔLE
Fiche au registre
état « proposé »
Revue d’architecture
et de sécurité
Seuils d’évaluation
atteints
Homologation
(annexe A)
Revue annuelle
(semestrielle si élevé)
Preuve de
révocation
Changement de modèle, d’invite, d’outil, de protocole ou de population visée → réévaluation
Figure 25 — Cycle de vie d’un agent et points de contrôle. Chaque étape se termine par un point de contrôle consigné au registre; 
en production, un changement significatif renvoie l’agent aux étapes de conception, d’évaluation et de pilote, dans la mesure du 
changement. Source : CRE-IA-2026-01.
1. Proposition. Le parrain décrit le cas d’usage et la valeur attendue. Point de contrôle : fiche créée à 
l’état « proposé », avec une première estimation de la classe de risque.
2. Conception. L’équipe propose la classe de risque, que la fonction risques et conformité tranche 
(tableau 44), puis fixe, sous le plafond de cette classe (section 8.1), le niveau d’autonomie visé, le patron 
d’orchestration (chapitre 7), les contrats et la carte d’agent (section 6.8). S’il y a des RP, l’EFVP commence 
ici : la Loi sur le privé l’exige pour tout projet d’acquisition, de développement ou de refonte d’un 
système d’information impliquant des RP, et le RPRP est consulté dès le début (art. 3.3)[56]. Point de 
contrôle : revue d’architecture et de sécurité.
3. Construction et évaluation. L’agent est bâti sur les gabarits de la plateforme, avec son jeu d’évaluation 
et ses tests de sécurité (section 9.9). Point de contrôle : seuils d’évaluation atteints (section 10.4), fiche 
complète et, s’il y a des RP, EFVP terminée (EXIG-CON-04).
4. Pilote. Périmètre, population et durée sont bornés. Le pilote d’un agent qui vise N3 ou N4 devrait 
s’exécuter au niveau immédiatement inférieur. Point de contrôle  : homologation selon la grille 
d’homologation (annexe A).
5. Production. Surveillance, évaluation continue et gestion des changements. Point de contrôle : attes­
tation périodique du parrain (EXIG-GOV-13), tous les 12 mois, tous les 6 mois pour la classe élevée.
6. Retrait. Révocation des identités, retrait du catalogue, avis aux consommateurs et archivage. Point de 
contrôle : preuve de révocation au registre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 166 sur 283


---
## [Page PDF 167]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
La suspension se distingue du retrait. Elle est immédiate et réversible : c’est le coupe-circuit, que le NIST 
rattache aux mécanismes permettant de supplanter, désengager ou désactiver un système dont le compor­
tement s’écarte de l’usage prévu (MANAGE 2.4)[74]. Le retrait est définitif et planifié. Le délai maximal de 
suspension se fixe et se teste selon la section 7.8 et la section 9.4; dans Microsoft Entra Agent ID, par exemple, 
désactiver le gabarit (agent identity blueprint) bloque d’un coup toutes les identités qui en dérivent[92].
EXIG-GOV-11 · DOIT
Points de contrôle consignés
Un agent DOIT franchir dans l’ordre les six points de contrôle de figure 25. Chaque passage est consigné 
au registre avec la date, le décideur désigné par tableau 44 et les preuves (rapport d’évaluation, EFVP, 
résultats des tests de sécurité, grille d’homologation de l’annexe A).
Pourquoi : une décision sans trace ne peut être ni auditée ni contestée; le registre devient le dossier de preuve 
de l’agent.
EXIG-GOV-12 · DOIT
Réévaluation sur changement significatif
Les changements suivants DOIVENT déclencher une réévaluation de la classe de risque et du niveau 
d’autonomie avant leur mise en production : changement de modèle ou de version de modèle; modifi­
cation de l’invite système; ajout d’un outil ou passage d’un outil à un palier supérieur; nouvelle version 
majeure d’un contrat ou d’un protocole; nouvelle population visée ou nouvelle finalité; modification 
du domaine d’exploitation (ODD); nouvelle catégorie de données, notamment de RP; changement de 
fournisseur ou de lieu de traitement des données; incident grave ou dérive détectée par l’évaluation 
continue. La réévaluation reprend les points de contrôle de conception, d’évaluation et de pilote dans la 
mesure du changement. Si le changement ne peut attendre, l’agent fonctionne au niveau d’autonomie 
inférieur jusqu’à la fin de la réévaluation (EXIG-AUT-05).
Pourquoi : le niveau d’autonomie vaut pour une configuration donnée; Feng, McDonald et Zhang prévoient le 
renouvellement du certificat d’autonomie à chaque changement de l’agent ou de son environnement[83], et la ligne 
directrice E-23 du BSIF déclenche une revue indépendante lors de modifications des modèles ou des données[8].
EXEMPLE
Un agent de rapprochement de factures fournisseurs de classe modérée, homologué au niveau N3, utilise 
un modèle dont le fournisseur annonce une nouvelle version. La passerelle de modèles conserve la 
version épinglée pendant que l’équipe rejoue le jeu d’évaluation sur la nouvelle; la fonction risques 
confirme la classe, puis le parrain approuve la bascule, consignée au registre. Si les seuils ne sont pas 
atteints, l’agent reste sur l’ancienne version, ou redescend à N2 le temps de corriger.
EXIG-GOV-13 · DOIT
Attestation périodique du parrain
Le parrain DOIT attester au registre, au moins tous les 12 mois et tous les 6 mois pour un agent de classe 
élevée, que l’agent est encore requis et que sa finalité, ses mandants, ses portées, sa classe et son niveau 
d’autonomie restent exacts. L’équipe plateforme DOIT revoir chaque trimestre la liste des agents sans 
parrain actif, sans fiche à jour ou inactifs, et désactiver ceux qui ne sont pas régularisés (EXIG-IAM-07).
Pourquoi : Microsoft recommande de faire attester par les parrains, tous les 6 à 12 mois, que chaque agent est encore 
requis, et de revoir chaque trimestre les agents orphelins[92]; le cadre retient la borne la plus stricte pour la classe 
élevée, et les périodicités de 12 mois, de 6 mois et d’un trimestre sont des choix du cadre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 167 sur 283


---
## [Page PDF 168]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
EXIG-GOV-14 · DOIT
Retrait vérifiable
Le retrait d’un agent DOIT comprendre : la révocation de toutes ses identités, justificatifs et jetons, 
propagée aux passerelles et aux fournisseurs dans le délai maximal fixé par l’entreprise (EXIG-IAM-07); 
un avis aux consommateurs connus au moins 60 jours avant la fin du service, sauf retrait anticipé pour 
un motif de sécurité, décidé par le comité et précédé d’une suspension (EXIG-INT-14); le retrait de ses 
entrées au catalogue; l’archivage de ses journaux d’audit et de ses versions selon les durées de conser­
vation applicables; l’archivage ou la destruction de ses mémoires selon la politique de conservation; 
une preuve de révocation inscrite au registre. Le préavis de 60 jours est un choix du cadre, aligné sur la 
coexistence des versions (section 6.8).
Pourquoi : le NIST AI RMF demande des processus de déclassement sécuritaire (GOVERN 1.7)[74], le livre blanc de 
l’OpenID Foundation recommande un retrait formel propagé, par exemple par une opération SCIM DELETE[311], et 
les événements CAEP permettent de diffuser la révocation aux parties concernées[344].
11.6 Dérogations
Cette section encadre les exceptions au cadre. Une dérogation est une exception écrite, temporaire et 
compensée; elle n’est jamais une permission tacite. Sans dérogations, un cadre trop rigide pousse les équipes 
vers des agents fantômes; sans discipline, les dérogations vident le cadre de son contenu.
Une demande de dérogation contient au minimum :
• l’identifiant de chaque exigence visée et le ou les agents concernés;
• la justification : pourquoi la conformité est impossible ou disproportionnée maintenant;
• le risque résiduel et son effet sur la classe de risque;
• les mesures compensatoires, par exemple un niveau d’autonomie abaissé, une approbation humaine 
ajoutée, un plafond de coût réduit ou une surveillance renforcée;
• la durée, la date d’échéance et le plan de retour à la conformité;
• le demandeur, les avis reçus et le décideur.
EXIG-GOV-15 · DOIT
Demande et décision écrites
Toute dérogation DOIT être demandée par écrit par le parrain avec le contenu minimal ci-dessus, 
instruite par l’architecture d’entreprise avec l’avis de la sécurité, de la fonction risques et, s’il y a des RP, 
du RPRP, puis accordée ou refusée par le comité. Le comité PEUT déléguer à l’architecture d’entreprise 
les dérogations qui visent un agent de classe faible, pour 90 jours au plus (choix du cadre), à la condition 
que la décision soit prise par une personne autre que celle qui a instruit la demande. La dérogation est 
inscrite au registre et visible dans la fiche de l’agent.
Pourquoi : une exception accordée oralement ne se retrouve ni à l’audit ni à l’échéance; la délégation pour la classe 
faible évite d’engorger le comité.
EXIG-GOV-16 · DOIT
Durée bornée
Une dérogation DOIT porter une date d’échéance d’au plus six mois. Elle PEUT être renouvelée une 
seule fois, par décision du comité, sur présentation d’un plan de retour à la conformité mis à jour. À 
l’échéance, l’exigence s’applique de nouveau; si l’agent n’y satisfait pas, il passe à l’état « suspendu ». 
Le registre DOIT avertir le parrain 30 jours avant l’échéance. Ces durées sont des choix du cadre.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 168 sur 283


---
## [Page PDF 169]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
Pourquoi : une exception sans échéance devient la règle; une exception qu’on veut renouveler plusieurs fois signale 
plutôt une règle à revoir, ce que tranche la révision semestrielle du cadre (section 1.6).
EXIG-GOV-17 · NE DOIT PAS
Exigences non dérogeables
Une dérogation NE DOIT PAS autoriser un niveau d’autonomie NX; l’exécution d’une action P3 sans 
approbation humaine; l’usurpation d’identité au lieu de la délégation (section 9.3); l’exploitation d’un 
agent sans fiche au registre ni parrain nommé; le dépassement du plafond d’autonomie de la classe de 
risque (section 8.1); ou le manquement à une obligation légale ou réglementaire.
Pourquoi  : ces règles protègent contre des dommages irréversibles ou contre une responsabilité légale que 
l’entreprise ne peut pas écarter par une décision interne.
11.7 Gouvernance des standards
Cette section fixe la façon dont le cadre fait évoluer son catalogue des protocoles et standards (section 6.3). 
Les standards agentiques changent de trimestre en trimestre : sans processus explicite, chaque annonce de 
fournisseur devient une décision d’architecture improvisée.
Le Cadre européen d’interopérabilité rappelle que l’interopérabilité est régulièrement perturbée par les 
changements législatifs, organisationnels et technologiques, et qu’elle exige des procédures de gestion du 
changement[157]. Les exemples récents le confirment. La révision 2026-07-28 de MCP a introduit une poli­
tique de cycle de vie à trois états (Active, Deprecated, Removed) : une fonctionnalité dépréciée reste au moins 
douze mois dans la spécification, ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité 
actif[34, 196]. Les conventions sémantiques GenAI d’OpenTelemetry sont au niveau de stabilité Development 
et peuvent changer sans processus de dépréciation[181, 188]. OAuth 2.1 demeure un Internet-Draft[176].
Chaque statut du catalogue emporte une conséquence de gouvernance. « Adopter » désigne le choix par 
défaut des nouveaux projets. « Évaluer » autorise des pilotes bornés, avec une date de décision. « Surveiller » 
limite le standard à la veille et aux essais hors production, sans données réelles. « Contenir » tolère l’existant, 
interdit tout nouvel usage et exige un plan de sortie.
EXIG-GOV-18 · DOIT
Révision trimestrielle du catalogue
L’architecture d’entreprise DOIT réviser le catalogue des protocoles au moins chaque trimestre et 
soumettre les changements de statut à l’approbation du comité. Chaque changement est daté et motivé; 
une dépréciation ou un retrait s’accompagne d’un plan de migration dont l’échéance précède la fin de 
la fenêtre de dépréciation annoncée par le standard. Une révision extraordinaire DOIT avoir lieu dès 
qu’un standard au statut « Adopter » publie une version majeure ou une dépréciation; un correctif de 
sécurité PEUT aussi la justifier (section 1.6).
Pourquoi : une fenêtre de dépréciation de douze mois ne protège que l’organisation qui la voit venir et planifie sa 
migration dès l’annonce.
EXIG-GOV-19 · DOIT
Critères d’admission d’un standard
Un standard DOIT satisfaire aux six critères suivants, propres au cadre, pour obtenir le statut 
« Adopter » :
• spécification publique, versionnée et assortie d’une politique de compatibilité et de dépréciation;
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 169 sur 283


---
## [Page PDF 170]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
• gouvernance neutre ou multipartite (organisme de normalisation ou fondation), et non celle d’un 
seul fournisseur;
• statut final ou stable (RFC, Recommandation du W3C, version ou révision publiée comme stable); 
un brouillon ou un composant de niveau expérimental n’est admis qu’avec une réserve inscrite au 
catalogue, épinglé à une version précise et adossé à un standard publié ou à un mécanisme stable;
• au moins deux mises en œuvre indépendantes, ou une suite de tests de conformité exécutable dans 
la chaîne d’intégration;
• modèle de sécurité documenté, compatible avec le chapitre 9;
• licence ouverte, sans redevance.
Pourquoi : ces critères écartent les annonces prématurées. L’AAIF, par exemple, n’admet un projet qu’au terme 
d’un processus formel (proposition publique, triage, recommandation du comité technique, approbation du conseil 
d’administration, puis formalités juridiques et intégration technique avec la Linux Foundation); une proposition 
déposée ne suffit pas[42, 263] (section 6.9).
EXIG-GOV-20 · DOIT
Veille désignée et usage encadré
L’architecture d’entreprise DOIT désigner une personne chargée de la veille pour chaque organisme qui 
fait évoluer un standard du catalogue, au minimum l’AAIF (projets et groupes de travail), l’IETF (groupes 
OAuth et WIMSE), OpenTelemetry, le W3C, le NIST (son Center for AI Standards and Innovation, CAISI, 
et son National Cybersecurity Center of Excellence, NCCoE) et l’OWASP GenAI Security Project. Un 
standard ou un projet NE DOIT PAS être utilisé, même en pilote avec des données réelles, s’il ne figure 
pas au catalogue au statut « Évaluer » ou « Adopter ».
Pourquoi : les pratiques d’identité et de sécurité des agents ne sont pas stabilisées. L’AAIF anime huit groupes de 
travail, dont identité et confiance, observabilité et traçabilité, gouvernance et alignement réglementaire[40]; le CAISI 
du NIST a lancé le 17 février 2026 l’AI Agent Standards Initiative[411]; le groupe WIMSE de l’IETF voit se multiplier 
les brouillons individuels sur la délégation entre agents[336].
L’entreprise PEUT participer aux consultations publiques et aux groupes de travail pour faire valoir ses 
besoins; le NCCoE du NIST a, par exemple, publié le 29 septembre 2026 la synthèse des commentaires de plus 
de 600 intervenants sur son document de réflexion consacré à l’identité et à l’autorisation des agents[338]. 
Le cadre lui-même est révisé chaque semestre par le comité : les dérogations accordées, les incidents et 
les résultats de la veille alimentent cette révision, et le chapitre 14 situe ces pratiques dans le modèle de 
maturité.
12 Risques, conformité et réglementation
Ce chapitre relie la classe de risque d’un agent aux obligations qui en découlent. Il traduit en exigences 
vérifiables la Loi 25 et le droit québécois, le cadre fédéral et sectoriel canadien, le règlement européen sur 
l’IA, le NIST AI RMF et ISO/IEC 42001, puis les réunit dans une matrice de correspondance et une base de 
preuves unique. Il fixe enfin la transparence due aux personnes, la réponse aux incidents agentiques et une 
évaluation d’impact unifiée. L’état du droit est celui du 27 octobre 2026.
ATTENTION
Ce chapitre résume l’intention des textes; leur application à un cas précis relève des affaires juridiques.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 170 sur 283


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
