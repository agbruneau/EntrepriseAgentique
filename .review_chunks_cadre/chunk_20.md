# chunk_20 — pages PDF 191 à 202 (sur 283)



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


---
## [Page PDF 193]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
« Loi sur le privé » désigne la Loi sur la protection des renseignements personnels dans le secteur privé 
(RLRQ, c. P-39.1).
DROIT APPLICABLE
L’entreprise demeure responsable des renseignements personnels qu’elle confie à un fournisseur, y 
compris en cas d’incident[414]. La Loi sur le privé ne prévoit pas de responsabilité « conjointe » : elle 
impose un contrat écrit qui encadre le mandataire (art. 18.3)[56]. Les clauses donnent à l’entreprise les 
moyens de remplir ses propres obligations (section 12.2).
EXIG-APP-07 · DOIT
Clause 1 — Interopérabilité ouverte et portabilité des cartes
Le contrat DOIT engager le fournisseur à prendre en charge A2A 1.0 en entrée et en sortie pour 
toute délégation entre agents; à publier des cartes d’agent conformes à la spécification A2A, dont le 
fichier a2a.proto est la définition normative, à l’adresse /.well-known/agent-card.json pour les 
agents exposés; à n’exiger aucune extension propriétaire pour déléguer une tâche à un agent tiers ou 
en recevoir une; et à maintenir une version de protocole dépréciée au moins pendant la période prévue 
par la spécification, avec préavis écrit avant son retrait.
Pourquoi : sans A2A 1.0 natif ni extension imposée, l’entreprise change de fournisseur sans réécrire ses délégations; 
le schéma de la carte relève de la spécification A2A, non d’un éditeur ni d’un autre projet[68].
EXIG-APP-08 · DOIT
Clause 2 — Conformité MCP et délégation d’identité
Le contrat DOIT exiger que tout outil ou connecteur exposé par le fournisseur respecte MCP 2026-07-28 
et sa spécification d’autorisation : paramètre resource de la RFC 8707, jeton propre à chaque serveur, 
interdiction de relayer un jeton reçu[71, 209]. Il DOIT exiger en outre, comme engagement distinct de la 
conformité MCP, l’acceptation de jetons délégués émis par échange de jetons (RFC 8693) dont la reven­
dication act conserve la chaîne des acteurs[70]. La prise en charge de l’extension Enterprise-Managed 
Authorization PEUT être valorisée dans la notation de la ligne « Identité et délégation »[178].
Pourquoi : sans chaîne de délégation, la passerelle ne peut pas appliquer l’intersection des droits du mandant et de 
l’agent (section 9.3).
EXIG-APP-09 · DOIT
Clause 3 — Télémétrie exportable et explicabilité
Le contrat DOIT garantir à l’entreprise un accès continu aux traces et aux journaux d’exécution de 
ses agents, y compris la version exacte du modèle, les outils appelés et les approbations. Pour toute 
décision concernant une personne, le fournisseur DOIT fournir de quoi l’informer des renseignements 
personnels utilisés et des raisons, principaux facteurs et paramètres de la décision (art. 12.1, qui vise les 
décisions fondées exclusivement sur un traitement automatisé; l’étendre à toute décision est un choix 
du cadre), conserver ces renseignements au moins un an après la décision (art. 11) et permettre de 
répondre aux demandes d’accès dans les 30 jours (art. 32)[56].
Pourquoi : l’obligation d’expliquer reste à l’entreprise; elle vise les facteurs déterminants, non l’algorithme[318].
EXIG-APP-10 · DOIT
Clause 4 — Usage limité au mandat et interdiction d’entraînement
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 193 sur 283


---
## [Page PDF 194]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
Le contrat DOIT préciser les mesures de confidentialité, limiter l’usage des renseignements à 
l’exécution du mandat et en interdire la conservation après son échéance (art.  18.3)[56]. Il DOIT 
aussi interdire expressément d’utiliser les données de l’entreprise (invites, contextes, sorties, traces, 
mémoires, plongements vectoriels) pour entraîner, ajuster ou évaluer des modèles du fournisseur ou de 
tiers, sauf autorisation écrite distincte.
Pourquoi : la loi ne nomme pas l’entraînement; l’interdiction explicite découle de la limitation au mandat et ferme 
toute ambiguïté.
EXIG-APP-11 · DOIT
Clause 5 — Résidence, transferts et lois étrangères
Le contrat DOIT déclarer chaque lieu de traitement ou de conservation des données de l’entreprise 
(inférence, outils, mémoires, journaux, sous-traitants), prévoir un préavis écrit de tout changement 
(cible du cadre : 90 jours), constituer l’entente écrite exigée par l’article 17 de la Loi sur le privé[56] 
lorsque des renseignements personnels sont communiqués hors du Québec, ce que le cadre interprète 
comme incluant une autre province, ou confiés à un tiers établi hors du Québec pour traitement ou 
conservation, et documenter l’exposition du fournisseur à des lois étrangères d’accès aux données, avec 
les mesures compensatoires retenues, par exemple un chiffrement à clés gérées par l’entreprise[416].
Pourquoi : le Clarifying Lawful Overseas Use of Data Act (CLOUD Act) des États-Unis oblige un fournisseur qui y 
est assujetti à divulguer les données sous sa garde ou son contrôle, où qu’elles soient[417]; le gouvernement fédéral 
reconnaît que le stockage au Canada ne suffit pas à écarter la compétence de tribunaux étrangers, tout en ne relevant 
aucun cas documenté de gouvernement étranger cherchant à accéder aux données d’entreprises canadiennes 
détenues par des fournisseurs[418]. L’EFVP pondère ce risque.
EXIG-APP-12 · DOIT
Clause 6 — Notification d’incident
Le contrat DOIT obliger le fournisseur à aviser l’entreprise sans délai, et au plus tard dans le délai que le 
contrat fixe (cible du cadre : 24 heures après la prise de connaissance par le fournisseur), de tout incident 
touchant ses données, ses identités ou ses agents, y compris une action d’agent non autorisée, une 
injection réussie ou une fuite par un outil; à transmettre les éléments requis pour l’avis à la Commission 
d’accès à l’information (CAI) et pour le registre des incidents; et à préserver les preuves et les versions 
en cause.
Pourquoi : le mandataire doit aviser sans délai de toute violation (art. 18.3), et l’entreprise doit aviser la CAI « avec 
diligence » lorsque l’incident présente un risque de préjudice sérieux (art. 3.5), la loi ne fixant aucun délai en 
heures[56]; la cible de 24 heures reprend l’ordre de grandeur du délai de signalement au BSIF sans suffire à le respecter 
à elle seule : l’avis exige 24 heures ou moins, sans fixer le point de départ, et une institution financière fédérale 
devrait exiger un délai plus court[434] (section 12.8).
EXIG-APP-13 · DOIT
Clause 7 — Audit, sécurité et transparence des changements
Le contrat DOIT accorder à l’entreprise un droit de vérification, l’accès aux résultats des évaluations de 
sécurité et d’équipe rouge des composants agentiques, fondées au minimum sur l’OWASP Top 10 for 
Agentic Applications 2026[28], la liste à jour des modèles, serveurs MCP, agents et sous-traitants intégrés 
avec leurs versions, et un préavis écrit avant tout changement de modèle qui modifie le comportement 
d’un agent de l’entreprise.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 194 sur 283


---
## [Page PDF 195]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
Pourquoi : un changement de modèle ou de fournisseur peut exiger la mise à jour de l’EFVP[413] et, dans les institu­
tions financières fédérales, la revue prévue par la ligne directrice E-23, qui inclut les modèles de fournisseurs[8]; le 
NIST AI RMF demande des politiques sur les risques de tiers (GOVERN 6.1)[74].
EXIG-APP-14 · DOIT
Clause 8 — Réversibilité et sortie
Le contrat DOIT prévoir qu’à l’échéance, à la résiliation ou sur demande, le fournisseur restitue dans 
des formats ouverts, structurés et documentés les mémoires des agents (épisodique, sémantique, procé­
durale), les graphes de connaissances, les définitions d’agents (invites système, cartes, compétences, 
flux, politiques), la configuration des outils, les journaux d’audit et les traces; qu’il prête assistance 
pendant une période de transition (cible du cadre : six mois); puis qu’il détruise les données et l’atteste 
par écrit.
Pourquoi : la mémoire et les définitions forment l’actif que l’entreprise doit garder (section 5.5); la loi exige que le 
contrat prévoie que le mandataire ne conserve pas les renseignements après le mandat[56].
EXIG-APP-15 · DOIT
Clause 9 — Accord écrit au sens de l’article 25(4) du RIA
Lorsque l’entreprise est fournisseur d’un système d’IA à haut risque au sens du règlement européen 
sur l’IA (RIA), ou le devient, notamment en y apposant son nom, en le modifiant substantiellement ou 
en réaffectant un agent à un usage de l’annexe III (art. 25(1)), le contrat avec chaque tiers qui fournit 
un outil, un service, un composant ou un modèle intégré DOIT constituer l’accord écrit exigé par 
l’article 25(4), tel que modifié par le règlement (UE) 2026/1744[58, 61, 375]. Le cadre y exige au minimum la 
documentation technique, l’accès aux journaux, l’accès pour essais et l’assistance en cas d’incident.
Pourquoi : ces obligations visent les systèmes de l’annexe III à compter du 2 décembre 2027 et ceux de l’annexe I à 
compter du 2 août 2028[57]; les outils, services, processus et composants rendus publics sous licence libre et ouverte 
en sont exemptés, sauf s’il s’agit de modèles d’IA à usage général (section 12.4).
EXIG-APP-16 · DOIT
Clause 10 — Révocation des identités non humaines
Le contrat DOIT prévoir, à la fin du contrat ou à la suspension d’un agent, la révocation par le 
fournisseur, dans un délai fixé (cible du cadre  : 24  heures), de toutes les identités non humaines, 
justificatifs, jetons, consentements OAuth, abonnements de notification et webhooks liés à l’entreprise, 
avec attestation écrite. L’entreprise DOIT révoquer de son côté les accès qu’elle a accordés et vérifier 
l’absence d’accès résiduel.
Pourquoi : le retrait inadéquat est le premier risque du Top 10 NHI de l’OWASP (NHI1)[91]; le NIST AI RMF prévoit 
un déclassement sécuritaire (GOVERN 1.7)[74], et le livre blanc de l’OpenID Foundation (section 2.9) recommande 
un retrait formel propagé à tous les systèmes intégrés[466].
13.4 Grille d’évaluation
La grille du tableau 54 rend les offres comparables. Chaque critère reçoit une note de 0 à 3 : 0, absent ou 
non démontré; 1, partiel ou inscrit à une feuille de route datée; 2, démontré par le fournisseur; 3, démontré 
par un essai reproductible de l’entreprise. Le score est la moyenne pondérée des notes. Le cadre fixe le seuil 
d’admissibilité à 2,0, sans aucun échec à un critère éliminatoire. Les pondérations sont indicatives : pour un 
agent de classe de risque élevée, le comité peut les rééquilibrer d’au plus 5 points par critère, en le justifiant, 
la somme des poids demeurant égale à 100.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 195 sur 283


---
## [Page PDF 196]

CRE-IA-2026-01 · Cadre de référence
13 Approvisionnement et clauses contractuelles
Tableau 54 — Grille d’évaluation des fournisseurs de solutions agentiques
Critère
Ce qui est évalué
Preuve attendue
Poids
Éliminatoire
Interopérabilité protocolaire
MCP 2026-07-28 et A2A 1.0 na­
tifs; primitives et liaisons cou­
vertes; extensions
Rapport a2a-tck, résultats 
de conformité MCP, liste 
des écarts
20
Oui
Identité et délégation
Identité par agent, fédération, 
jetons délégués, révocation par 
l’entreprise
Démonstration dans le lo­
cataire de l’entreprise; es­
sai de révocation chrono­
métré
15
Oui
Sécurité et chaîne 
d’approvisionnement
Garde-fous, bacs à sable, inven­
taire versionné des composants, 
équipe rouge
Rapports d’essai; inven­
taire; droit d’audit (clause 
7)
15
Non
Observabilité et audit
OTLP, conventions épinglées, 
propagation du contexte, journal 
d’audit exportable
Trace de bout en bout 
produite pendant l’essai
15
Oui
Données, résidence et confor­
mité
Lieux de traitement, article 17, 
interdiction d’entraînement, ar­
ticle 12.1, incidents
Clauses 3 à 6 acceptées; 
carte des flux pour l’EFVP
15
Oui
Réversibilité
Formats de restitution, assis­
tance, délai de sortie
Essai de restitution sur un 
agent pilote
10
Non
Coûts et FinOps
Données FOCUS, unités 
propres, plafonds par agent 
(EXIG-APP-05)
Export FOCUS d’un mois 
de pilote
5
Oui
Performance mesurée
Latence ajoutée P50 et P99, dé­
bit, disponibilité
Banc d’essai reproduc­
tible de l’entreprise 
(EXIG-APP-04)
5
Non
EXIG-APP-17 · DOIT
Application de la grille
Toute acquisition visée par ce chapitre DOIT être évaluée avec la grille du tableau 54. Une offre qui 
échoue un critère éliminatoire DOIT être écartée, sauf dérogation approuvée (section 11.6). La grille 
remplie et ses preuves DOIVENT être conservées au registre (section 11.4) et réévaluées à chaque 
renouvellement de contrat.
Pourquoi : une grille commune rend les décisions traçables et comparables d’une acquisition à l’autre.
14 Modèle de maturité
Ce chapitre situe l’entreprise sur cinq niveaux de maturité et cinq dimensions, pour mesurer l’écart entre 
ses pratiques et le cadre. Il fixe la méthode d’évaluation, les preuves attendues et le lien entre la maturité, les 
jalons et l’autonomie permise, puis relie le modèle à ISO/IEC 42001 et au NIST AI RMF. Il n’ajoute aucune 
exigence.
14.1 Cinq niveaux et cinq dimensions
Cette section définit l’échelle. Chaque niveau décrit un état observable des pratiques, et les niveaux sont 
cumulatifs : atteindre le niveau 3 suppose de satisfaire aussi aux critères du niveau 2. Les cinq dimensions 
reprennent les piliers du cadre : interopérabilité (chapitre 6), orchestration (chapitre 7), identité et sécurité 
(chapitre 9), observabilité, évaluation et coûts compris (chapitre 10), et gouvernance (chapitre 11 et chapitre 
12).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 196 sur 283


---
## [Page PDF 197]

CRE-IA-2026-01 · Cadre de référence
14 Modèle de maturité
1
Initial
Connecteurs ad hoc, clés
partagées, aucun inventaire
2
Reproductible
Premiers serveurs MCP,
identité par agent, traces
par projet, registre manuel
3
Défini
Catalogue d’entreprise,
passerelle, jetons délégués,
traçage de bout en bout,
cycle de vie à contrôles
4
Géré
Multiagent en production,
sagas, autorisation fine,
évaluation continue, coût
par tâche, ISO/IEC 42001
5
Optimisé
Confiance vérifiable
entre organisations,
autonomie ajustée par les
mesures, revue externe
Cible de la feuille de route : 18 mois
Niveau global = dimension la plus faible
(interopérabilité, orchestration, identité,
observabilité, gouvernance)
Figure 27 — Modèle de maturité en cinq niveaux. Chaque niveau englobe les précédents; la feuille de route vise le niveau 3, « Défini », 
en 18 mois (durée indicative, à calibrer après l’évaluation initiale). Le niveau global de l’entreprise est celui de sa dimension la plus 
faible. Source : CRE-IA-2026-01.
Le passage du niveau 2 au niveau 3 tient d’abord à la portée des pratiques : au niveau 2, à l’exception du 
registre, de l’identité et de la passerelle de modèles, qui couvrent déjà tous les agents, elles visent surtout 
les nouveaux agents et les pilotes; au niveau 3, elles forment la norme unique de tout le portefeuille. Le 
niveau 4 ajoute le pilotage par les mesures; le niveau 5, l’amélioration continue et la confiance étendue aux 
partenaires.
Tableau 55 — Niveaux de maturité par dimension
Niveau
Interopérabilité
Orchestration
Identité et sécurité
Observabilité
Gouvernance
1 — Initial Pra­
tiques improvi­
sées par chaque 
équipe
Connecteurs ad hoc, 
propres à chaque 
projet
Invites et scripts 
isolés; logique mé­
tier confiée au mo­
dèle
Clés d’API et 
comptes de service 
partagés
Journaux locaux; 
coûts inconnus
Aucun inventaire; 
agents fantômes
2 — Reproduc­
tible Pratiques 
établies et répé­
tées
Premiers serveurs 
MCP et cartes 
d’agent au cata­
logue, versions épin­
glées; contrats pour 
les outils des pilotes
Flux déterministes 
à étapes agen­
tiques; patron 
documenté par 
agent; exécution 
durable des pilotes
Identité propre à 
chaque agent, au­
cune clé partagée; 
secrets au coffre; 
passerelle de mo­
dèles; coupe-circuit 
exercé
Traces OpenTele­
metry par projet; 
journal d’audit 
des pilotes; coûts 
suivis par agent
Registre complet, 
tenu en partie 
à la main; par­
rain nommé pour 
chaque agent; 
comité en fonc­
tion; classes de 
risque attribuées
3 — Défini Pra­
tiques normali­
sées pour tout le 
portefeuille
Catalogue 
d’entreprise unique; 
MCP et A2A pour 
tout nouvel agent; in­
tégrations existantes 
migrées
Patrons autorisés 
et gabarits; mo­
teur d’exécution 
durable; compen­
sation définie pour 
chaque étape à 
effet; plafonds 
d’itérations
Passerelle d’agents 
pour tout appel in­
terdomaine; jetons 
délégués; garde-
fous communs; bacs 
à sable; équipe 
rouge régulière
Traçage de bout 
en bout; journal 
d’audit de toute 
action P2 et P3; 
évaluation dans 
la chaîne CI/CD; 
enveloppes bud­
gétaires
Cycle de vie 
à points de 
contrôle pour 
tous les agents; 
aucun justifica­
tif sans fiche 
complète; déro­
gations bornées
4 — Géré Pra­
tiques pilotées 
par les mesures
Systèmes clés expo­
sés au catalogue; ver­
sions gérées; choré­
graphie CloudEvents 
et AsyncAPI; réutilisa­
tion mesurée
Multiagent en pro­
duction là où un 
gain est mesu­
ré; sagas éprou­
vées par injection 
de fautes; routage 
des modèles selon 
les mesures
Autorisation fine par 
politiques en code; 
délai de révocation 
mesuré en exercice, 
sous la cible
Évaluation conti­
nue, production 
comprise; détec­
tion de la dérive; 
coût par tâche 
réussie suivi
Indicateurs tri­
mestriels utilisés 
dans les décisions 
du comité; prépa­
ration à la cer­
tification ISO/IEC 
42001
5 — Opti­
misé Améliora­
tion continue, 
confiance éten­
Interopérabilité avec 
les partenaires; vo­
cabulaire sémantique 
partagé
Chorégraphie in­
terdomaines; auto­
nomie ajustée se­
lon les mesures, à 
Confiance vérifiable 
entre organisations : 
cartes signées, fédé­
Incidents et dé­
rives versés aux 
jeux d’évaluation; 
décisions fondées 
Révision du cadre 
alimentée par les 
incidents, les dé­
rogations et la 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 197 sur 283


---
## [Page PDF 198]

CRE-IA-2026-01 · Cadre de référence
14 Modèle de maturité
Niveau
Interopérabilité
Orchestration
Identité et sécurité
Observabilité
Gouvernance
due aux parte­
naires
la hausse comme à 
la baisse
ration des identités 
et de la délégation
sur la valeur et le 
risque mesurés
veille (section 
11.7); revue ex­
terne
À RETENIR
Un niveau de maturité qualifie l’entreprise; un niveau d’autonomie (N0 à N4, section 8.1) qualifie un 
agent. L’autonomie n’est pas un objectif de maturité : Feng, McDonald et Zhang en font une décision de 
conception, et Morris et al. rappellent que le niveau retenu au déploiement n’a pas à être le maximum 
que permettent les capacités du modèle[83, 302]. Une entreprise au niveau 5 peut garder la plupart de ses 
agents à N1 ou à N2.
14.2 Évaluer sa maturité
Cette section fixe la cotation, le calendrier et les preuves admises. Le but est un résultat reproductible : deux 
évaluateurs qui examinent les mêmes preuves aboutissent au même niveau.
Règles de cotation
• Une dimension atteint un niveau lorsque ses critères, et ceux du niveau inférieur, sont satisfaits dans 
tout le périmètre qu’ils désignent, ou à défaut pour tous les agents en production.
• Le niveau global est celui de la dimension la plus faible. Une entreprise dotée d’un catalogue exemplaire, 
mais dont des agents partagent encore des clés d’API, reste au niveau 1 : un incident emprunte le maillon 
le plus faible.
• Un critère se prouve par des données du registre, des passerelles, des traces et du journal d’audit, comme 
les indicateurs du tableau 61; une déclaration d’équipe n’est pas une preuve. Pour les critères qui ne se 
calculent pas automatiquement, l’évaluateur examine les listes de contrôle de l’annexe A d’un échantillon 
d’agents de chaque classe; tous les agents de classe élevée en font partie.
Calendrier et conduite
Une première évaluation précède la phase Fondations et calibre les durées de la feuille de route (section 15.1). 
Une évaluation a lieu ensuite à chaque jalon : le jalon 2 exige le niveau 2 sur les cinq dimensions, le jalon 
3 le niveau 3 (tableau 58). Après le jalon 3, l’entreprise refait l’évaluation chaque année, par autoévaluation 
guidée par l’annexe A.
L’architecture d’entreprise conduit l’évaluation avec les fonctions qui répondent de chaque dimension; le 
comité en arrête le résultat, comme il constate les jalons. Ce résultat donne le niveau de chaque dimension, 
ses preuves et le plan d’action qui comble les écarts; le recul d’une dimension est soumis au comité, qui 
peut reporter les hausses d’autonomie prévues. Une phase peut livrer des capacités d’un niveau supérieur : 
la phase Industrialisation livre des flux multiagents et des sagas, dont l’exploitation éprouvée (gain mesuré, 
essais par injection de fautes) relève du niveau 4 en orchestration, alors que le jalon 3 ne vérifie que le 
niveau 3.
Preuves attendues
Tableau 56 — Preuves attendues par niveau de maturité
Niveau
Exemples de preuves
2 — Reproductible
Couverture du registre à 100 %; aucun agent sans justificatif propre; tous les appels de modèles par la 
passerelle; catalogue publié; traces des pilotes; rapport d’exercice du coupe-circuit; pilotes homologués 
selon l’annexe A.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 198 sur 283


---
## [Page PDF 199]

CRE-IA-2026-01 · Cadre de référence
14 Modèle de maturité
Niveau
Exemples de preuves
3 — Défini
Conformité au catalogue et couverture des passerelles interdomaines à 100 %, agents existants compris; 
traçabilité de toutes les actions P2 et P3; couverture de l’évaluation à 100 %; points de contrôle consignés 
pour chaque agent (EXIG-GOV-11); rapports d’équipe rouge.
4 — Géré
Séries trimestrielles d’indicateurs et décisions du comité qui s’y appuient; délai de révocation mesuré 
en exercice sous la cible; alertes de dérive traitées; coût par tâche réussie comparé au processus de 
référence; déclaration d’applicabilité et audit interne.
5 — Optimisé
Révisions du cadre motivées par les incidents et les mesures; rapport de revue externe ou certificat ISO/
IEC 42001; ententes avec des partenaires; contributions aux standards ouverts.
ATTENTION
Le modèle mesure l’avancement; il ne suspend aucune exigence. Tout nouvel agent est homologué selon 
l’annexe A, quel que soit le niveau de l’entreprise; les agents existants sont ramenés en conformité selon 
la feuille de route, sous les plafonds de phase ou par dérogation bornée (section 11.6).
Maturité et autonomie permise
Les règles de progression du chapitre 15 font de la maturité une condition de l’autonomie (tableau 58) : 
N2 et les premiers N3 bornés après le jalon 1; N3 entre domaines après le jalon 2, donc au niveau 2 de 
maturité, pour un agent dont tous les appels interdomaines passent déjà par la passerelle d’agents; N4 
après le jalon 3, donc au niveau 3 sur les cinq dimensions, pour un agent de classe faible, sur un domaine 
d’exploitation certifié et sur décision du comité. Le plafond de la classe de risque s’applique en plus, et le 
plus strict l’emporte.
14.3 Lien avec la certification ISO/IEC 42001 et le NIST AI RMF
Cette section situe le modèle par rapport aux deux référentiels présentés à la section 12.5. Le modèle est un 
instrument interne de pilotage, qui ne donne lieu à aucune certification.
Le NIST AI RMF, d’application volontaire, propose des profils temporels : un profil actuel (Current Profile) 
décrit la gestion présente de l’IA, un profil cible (Target Profile) les résultats nécessaires pour atteindre les 
objectifs de gestion des risques. Leur comparaison révèle des écarts que des plans d’action comblent; le NIST 
ne prescrit aucun gabarit de profil[74, 448]. L’évaluation de maturité suit cette logique; pour en tirer un profil 
au sens du NIST, l’entreprise rattache ses critères aux sous-catégories pertinentes, dont celles du tableau 57.
ISO/IEC 42001:2023 est au contraire une norme d’exigences certifiable par tierce partie, par des organismes 
conformes à ISO/IEC 17021-1 et à ISO/IEC 42006:2025[451]. Norme de système de management, elle encadre 
des processus, du contexte de l’organisation (article 4) jusqu’à l’amélioration (article 10)[395]. Le cadre situe 
donc la préparation à la certification au niveau 4, qui ajoute aux processus du niveau 3 une évaluation des 
performances fondée sur des mesures. La déclaration d’applicabilité, qui rattache les exigences du cadre aux 
mesures de l’annexe A de la norme (section 12.5), est un livrable de ce niveau.
Tableau 57 — Correspondance indicative entre niveaux de maturité, ISO/IEC 42001 et NIST AI RMF
Niveau
ISO/IEC 42001:2023
NIST AI RMF 1.0
2 — Reproductible
Politique d’IA (5.2), rôles (5.3); premières appréciations 
des risques (6.1.2)
GOVERN 1.6 (inventaire), 2.1 (rôles); MANAGE 
2.4 (coupe-circuit)
3 — Défini
Planification et fonctionnement appliqués à tous les 
agents (6.1.2 à 6.1.4, article 8); mesures A.5, A.6.2.8 et 
A.10
GOVERN 1.7 (déclassement), 6.1 (tiers); MAP 3.5 
(supervision humaine); MEASURE 2.7 (sécurité et 
résilience)
4 — Géré
Évaluation des performances, audit interne et revue 
de direction (article 9); mesure A.6.2.6 (exploitation et 
surveillance)
MEASURE 2.4 (surveillance en production), 3.1 
(risques émergents); MANAGE 4.1; profils actuel 
et cible comparés
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 199 sur 283


---
## [Page PDF 200]

CRE-IA-2026-01 · Cadre de référence
14 Modèle de maturité
Niveau
ISO/IEC 42001:2023
NIST AI RMF 1.0
5 — Optimisé
Amélioration (article 10); certification par tierce partie
Profils revus à chaque révision du cadre
Interprétation du cadre, établie à partir de NIST AI 100-1 et du catalogue d’ISO/IEC 42001[74, 395].
Le cadre admet une certification ISO/IEC 42001 comme revue externe de la dimension Gouvernance; elle 
n’atteste toutefois pas, à elle seule, les quatre autres : la norme encadre des processus, sans prescrire de 
protocole, de passerelle ni de format de trace. À l’inverse, un niveau élevé de maturité n’établit ni la 
certification ni la conformité à la Loi 25 ou au RIA, qui s’apprécient obligation par obligation (chapitre 12).
15 Feuille de route et indicateurs
Ce chapitre ordonne la mise en œuvre du cadre en quatre phases séparées par trois jalons, auxquels 
s’ajoutent un jalon réglementaire et deux jalons de mise à l’échelle; il la cale sur le calendrier 2027-2030, puis 
détaille les 90 premiers jours. Il fixe les indicateurs qui permettent au comité d’architecture et des risques 
agentiques de constater les progrès sur des mesures plutôt que sur des déclarations. Il se termine par les 
facteurs de succès, puis par les risques de mise en œuvre, chacun assorti de sa parade.
15.1 Quatre phases et leurs jalons
La mise en œuvre progresse par phases : chaque phase installe les contrôles dont la suivante a besoin, et 
l’autonomie accordée aux agents n’augmente qu’une fois ces contrôles en service. C’est la logique d’un 
chantier : on ne monte pas les étages avant d’avoir coulé les fondations.
Fondations
mois 0 à 3
Plateforme
mois 3 à 9
Industrialisation
mois 9 à 18
Mise à l’échelle
mois 18 et plus
Gouvernance
Comité, registre
Classes de risque, cycle de vie
Indicateurs trimestriels, dérogations
Cibles chiffrées, revue annuelle
Passerelles
Pass. modèles
Pass. d’agents (P0, P1 puis P2)
Toutes les interactions interdomaines
Interopérabilité
Inventaire
Catalogue, migration MCP
Migration des autres intégrations
Agents de partenaires
Identité et sécurité
Fin des clés
Identités, jetons délégués
Bacs à sable, équipe rouge régulière
Observabilité, FinOps
Traçage OpenTelemetry
Évaluation continue, coût par tâche
Routage adaptatif
Orchestration
Flux durables, approbation
Multiagent, sagas et compensation
Chorégraphie élargie
Conformité
EFVP en cours
Art. 12.1, validation E-23
Base de preuves; J2a (annexe III)
Certification ISO/IEC 42001
Autonomie autorisée
N0 et N1
N2, premiers N3 bornés
N3 entre domaines, par la passerelle
N4 sur périmètre certifié
Jalon 1
registre complet,
comité en fonction
Jalon 2
pilotes homologués,
maturité 2, MCP daté
Jalon 3
maturité 3 sur les
cinq dimensions
Jalon 2a
RIA, annexe III,
1er nov. 2027
Jalon 4
maturité 4
Jalon 5
certificat
ISO/IEC 42001
Figure 28 — Feuille de route : quatre phases et leurs jalons. Chaque ligne de travail avance d’une phase à l’autre; la dernière ligne 
indique l’autonomie maximale permise pendant la phase. Les losanges marquent les jalons : le comité constate J1, J2 et J3 avant d’ouvrir 
la phase suivante, J2a avant l’échéance réglementaire qu’il vise; J4 et J5 mesurent la progression dans la phase Mise à l’échelle. Source : 
CRE-IA-2026-01 (durées indicatives, à calibrer après l’évaluation de maturité initiale).
Les durées sont indicatives et se calibrent après l’évaluation de maturité initiale (section 14.2) : une organi­
sation qui exploite déjà une passerelle d’API raccourcira la phase Plateforme; celle qui découvre des dizaines 
d’agents non inventoriés allongera la phase Fondations. Le troisième jalon marque l’atteinte du niveau 3 de 
maturité sur les cinq dimensions du chapitre 14, seuil que le cadre retient pour laisser le nombre d’agents 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 200 sur 283


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
