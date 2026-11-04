# chunk_01 — pages PDF 1 à 12 (sur 283)



---
## [Page PDF 1]

CADRE DE RÉFÉRENCE D’ARCHITECTURE D’ENTREPRISE
Interopérabilité et Orchestration en 
Entreprise Agentique
Architecture normative, standards d’interopérabilité, patrons d’orchestration, 
autonomie et supervision humaine, identité et sécurité, observabilité et FinOps, 
gouvernance et conformité pour concevoir, déployer et superviser des agents d’IA à 
l’échelle de l’organisation.
André-Guy Bruneau M.Sc. IT · Version 1.1 · 28 octobre 2026
Titre
Interopérabilité et Orchestration en Entreprise Agentique — cadre de référence d’architecture 
d’entreprise
Identifiant normatif
CRE-IA-2026-01
Version et date
1.1 — 28 octobre 2026
Statut
Version finale consolidée, soumise à l’approbation du comité d’architecture et des risques agen­
tiques
Auteur
André-Guy Bruneau M.Sc. IT
Propriétaire
Architecture d’entreprise, au nom du comité d’architecture et des risques agentiques
Cycle de révision
Cadre : chaque semestre. Catalogue des protocoles et versions de référence : chaque trimestre. 
Révision extraordinaire après tout incident agentique grave ou changement réglementaire majeur.
Public
Direction TI, architectes d’entreprise et de solutions, équipes de plateforme et d’intégration, 
équipes produit, sécurité de l’information, gestion des risques et conformité, protection des rensei­
gnements personnels, affaires juridiques, FinOps, approvisionnement, audit interne, responsables 
métier
Classification
Usage interne
État des sources
Faits, versions et dates vérifiés aux 27 et 28 octobre 2026 contre des sources primaires ou, à défaut, 
secondaires reconnues (annexe F)
Actualisation
1er novembre 2026, annexe H (informative)


---
## [Page PDF 2]

CRE-IA-2026-01 · Cadre de référence
Historique des versions
Historique des versions
Version
Date
Nature des changements
0.1
27 oct. 2026
Ébauche pour discussion : structure en treize sections, principes, architecture en 
couches, échelle d’autonomie, liste de contrôle et gabarit de fiche d’agent.
0.2
27 oct. 2026
Ébauche enrichie : règles d’usage de MCP et d’A2A, paliers de risque des outils, 
extensions CloudEvents, évaluation en trois paliers, exemples de contrats.
Ébauche « produc­
tion »
27 oct. 2026
Ébauche parallèle : architecture en plans, exigences identifiées, contrats normatifs, 
grille d’homologation.
Recherche documen­
taire
27 oct. 2026
Synthèse de l’état de l’art en 2026 appuyée sur 121 références.
1.0
27 oct. 2026
Version finale consolidée : fusion des quatre documents, validation de chacune 
des 121 références et vérification des affirmations contre des sources primaires, 
unification des échelles (niveaux N0 à N4, paliers P0 à P3), corrections factuelles 
et mise à jour aux versions courantes des standards, ajout des volets mémoire, 
défense contre l’injection, approvisionnement et conformité canadienne, 28 sché­
mas explicatifs. Audit final du 28 octobre 2026 : réouverture et contrôle de 
chacune des références citées, revue de cohérence interne, factuelle et juridique 
de tous les chapitres, et intégration des corrections retenues (annexe F).
1.1
28 oct. 2026
Feuille de route 2027-2030 : calage sur le calendrier 2027-2030; migration MCP 
avancée dans la phase Plateforme et datée au jalon 2; validation initiale des 
agents visés par E-23 avant le 1er mai 2027; jalon J2a de conformité au RIA 
avant le 2 décembre 2027; jalons J4 et J5 pour la phase Mise à l’échelle; N3 
entre domaines conditionné au passage par la passerelle; cibles chiffrées des 
indicateurs fixées au jalon 3; marge pour les périodes de congés; deux risques 
ajoutés. Plafond d’autonomie par classe ramené à une seule source normative 
(EXIG-CON-02) et article 65.2 de la Loi sur l’accès ajouté aux critères de la classe 
élevée. Modifications corrélatives : sommaire, figure 1, sections 1.1, 3.1, 4.1 et 
14.2, EXIG-AUT-02, annexe F.
Méthode et avertissements
MÉTHODE D’ÉLABORATION ET DE VALIDATION
Cette version consolide quatre documents de travail. Chacune des 121 références de la recherche documen­
taire a été ouverte lorsque la page était accessible (108 sur 121), qualifiée selon sa crédibilité et confrontée aux 
affirmations qui la citaient; onze vérifications thématiques ont ensuite confronté les affirmations des quatre 
documents aux textes primaires : spécifications (Model Context Protocol, Agent2Agent, OpenTelemetry, 
CloudEvents, RFC de l’Internet Engineering Task Force), lois et règlements (Loi 25, règlement européen 
sur l’IA), normes (National Institute of Standards and Technology, ISO/IEC) et publications officielles des 
éditeurs. Seules des sources de catégorie A (primaires ou officielles) ou B (secondaires reconnues) sont citées. 
Le bilan détaillé et les principales corrections figurent à l’annexe F.
AVERTISSEMENTS
Les versions, dates et chiffres reflètent l’état des sources au 27 octobre 2026; les versions applicables 
sont fixées au catalogue d’entreprise, révisé chaque trimestre. Les produits commerciaux sont cités à titre 
d’exemples non limitatifs. Les obligations légales résumées ici en expriment l’intention : leur application à 
un cas précis relève des affaires juridiques.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 2 sur 283


---
## [Page PDF 3]

Table des matières
Historique des versions ............................................................................................................ ⁠2
Méthode et avertissements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠2
Sommaire exécutif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠7
Partie I — Fondements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠10
1 Objet, portée et mode d’emploi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠11
2 Contexte et enjeux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠15
3 Concepts et définitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠20
4 Principes directeurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠25
Partie II — Architecture, interopérabilité et orchestration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠31
5 Architecture de référence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠32
6 Interopérabilité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠45
7 Orchestration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠86
8 Autonomie et supervision humaine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠103
Partie III — Confiance et exploitation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠117
9 Identité, sécurité et confiance zéro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠118
10 Observabilité, évaluation et FinOps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠145
Partie IV — Gouvernance, conformité et mise en œuvre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠159
11 Gouvernance et cycle de vie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠160
12 Risques, conformité et réglementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠170
13 Approvisionnement et clauses contractuelles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠189
14 Modèle de maturité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠196
15 Feuille de route et indicateurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠200
Annexes — Outils d’application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠208
A Grille d’homologation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠209
B Gabarit de fiche d’agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠212
C Exemples de contrats ......................................................................................................... ⁠215
D Registre des exigences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠224
E Glossaire ........................................................................................................................ ⁠231
F Validation des sources et des ébauches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠241
G Références . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠250
H Actualisation de novembre 2026 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ⁠275
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 3 sur 283


---
## [Page PDF 4]

Liste des tableaux
Tableau 1 — Portée du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Tableau 2 — Parcours de lecture par rôle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Tableau 3 — Degrés d’obligation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Tableau 4 — Identifiants des principes et préfixes des exigences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Tableau 5 — Chronologie vérifiée de la consolidation des standards agentiques (novembre 2024 à octobre 2026) . . . . . . 17
Tableau 6 — Huit enjeux, leurs symptômes et la réponse du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Tableau 7 — Définitions normatives du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Tableau 8 — Agents interactifs et agents ambiants : conséquences de conception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Tableau 9 — Mise en œuvre des principes directeurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
Tableau 10 — Tensions fréquentes entre principes et arbitrage retenu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
Tableau 11 — Apport des plans transversaux à chaque couche . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
Tableau 12 — Correspondance des blocs de construction d’architecture (ABB) et des blocs de construction de solution 
(SBB) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
Tableau 13 — Types de mémoire des agents et contrôles applicables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Tableau 14 — Niveaux d’interopérabilité et exigences minimales pour une intégration d’agent . . . . . . . . . . . . . . . . . . . . 46
Tableau 15 — Catalogue des protocoles et standards (état au 27 octobre 2026) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Tableau 16 — Matrice de sélection des protocoles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
Tableau 17 — Principaux changements de la révision MCP 2026-07-28 et effet pour l’entreprise . . . . . . . . . . . . . . . . . . . 57
Tableau 18 — Correspondance entre l’OWASP MCP Top 10 (bêta) et les exigences du cadre . . . . . . . . . . . . . . . . . . . . . . 66
Tableau 19 — Champs de la carte d’agent A2A 1.0 et règles du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
Tableau 20 — Attributs d’extension CloudEvents exigés par le cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
Tableau 21 — Garanties d’un bus Kafka et responsabilités de la conception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Tableau 22 — Contenu minimal des contrats, par type d’interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Tableau 23 — Principaux composants d’AGNTCY et statut au catalogue (état au 27 octobre 2026) . . . . . . . . . . . . . . . . . . 84
Tableau 24 — Huit patrons d’orchestration autorisés et variante encadrée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
Tableau 25 — Critères comparés des principaux patrons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
Tableau 26 — Anti-patrons d’orchestration proscrits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
Tableau 27 — Cadriciels, moteurs et plateformes d’orchestration (exemples non limitatifs, état au 27 octobre 2026) . . . 101
Tableau 28 — Niveaux d’autonomie : rôles, paliers permis et contrôles minimaux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Tableau 29 — Correspondance entre l’échelle du cadre et les autres échelles d’autonomie . . . . . . . . . . . . . . . . . . . . . . . 106
Tableau 30 — Quatre critères pour fixer le niveau d’autonomie sous le plafond de la classe . . . . . . . . . . . . . . . . . . . . . . 107
Tableau 31 — Paliers de risque des outils . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
Tableau 32 — Trois patrons d’interaction avec un agent ambiant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Tableau 33 — Composants logiques de la confiance zéro et leur réalisation pour les agents . . . . . . . . . . . . . . . . . . . . . . 118
Tableau 34 — Risques de l’OWASP Non-Human Identities Top 10 (2025) et réponse du cadre . . . . . . . . . . . . . . . . . . . . 121
Tableau 35 — Profil OAuth exigé pour les agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Tableau 36 — Mécanismes d’identité en normalisation : état au 27 octobre 2026 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Tableau 37 — Référentiels de menaces retenus par le cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Tableau 38 — Top 10 OWASP des applications agentiques et contrôles du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Tableau 39 — Patrons de conception résistants à l’injection et usage recommandé . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
Tableau 40 — Technologies d’isolation du code généré . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Tableau 41 — Attributs de trace exigés et niveau dans la convention OpenTelemetry v1.41.0 . . . . . . . . . . . . . . . . . . . . . 147
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 4 sur 283


---
## [Page PDF 5]

Tableau 42 — Familles d’objectifs de niveau de service d’un agent (cibles proposées par le cadre) . . . . . . . . . . . . . . . . . 152
Tableau 43 — Rôles de la gouvernance agentique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Tableau 44 — Matrice RACI du cycle de vie d’un agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Tableau 45 — Répartition des responsabilités dans le modèle en étoile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
Tableau 46 — Classes de risque des agents : critères, plafond d’autonomie et contrôles minimaux . . . . . . . . . . . . . . . . . 171
Tableau 47 — Articles de la Loi sur le privé qui touchent les agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
Tableau 48 — Textes fédéraux et sectoriels canadiens : statut au 27 octobre 2026 et effet sur les agents . . . . . . . . . . . . 178
Tableau 49 — Articles du règlement européen sur l’IA et réponse du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
Tableau 50 — Matrice de correspondance : NIST AI RMF, ISO/IEC 42001, Loi 25, RIA et artefacts du cadre . . . . . . . . . . . 184
Tableau 51 — Délais de notification applicables aux incidents agentiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
Tableau 52 — Volets de l’évaluation d’impact unifiée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
Tableau 53 — Où se loge le verrouillage (état au 27 octobre 2026) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Tableau 54 — Grille d’évaluation des fournisseurs de solutions agentiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
Tableau 55 — Niveaux de maturité par dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
Tableau 56 — Preuves attendues par niveau de maturité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Tableau 57 — Correspondance indicative entre niveaux de maturité, ISO/IEC 42001 et NIST AI RMF . . . . . . . . . . . . . . . . 199
Tableau 58 — Phases de mise en œuvre, livrables et autonomie autorisée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Tableau 59 — Calage indicatif, mois 0 au 1er décembre 2026 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
Tableau 60 — Plan des 90 premiers jours (phase Fondations) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
Tableau 61 — Indicateurs de mise en œuvre et cibles proposées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
Tableau 62 — Risques de mise en œuvre, signes avant-coureurs et parades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Tableau 63 — Champs de la fiche d’agent et étape où ils deviennent exigibles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Tableau 64 — Exemples de contrats, références et exigences illustrées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
Tableau 65 — Glossaire des termes et des sigles du cadre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Tableau 66 — Catégories de crédibilité des sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Tableau 67 — Verdicts sur les 427 liens affirmation-source de la recherche documentaire . . . . . . . . . . . . . . . . . . . . . . . 242
Tableau 68 — Principales corrections factuelles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
Tableau 69 — Registre de validation des références de la recherche documentaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
Tableau 70 — Dépendances datées du cadre, rouvertes le 1er novembre 2026 sur leur source primaire . . . . . . . . . . . . . 275
Tableau 71 — Reports de la Note AMF IA au cadre (annexe D de la note), en attente de décision du comité . . . . . . . . . 280
Tableau 72 — Errata et incohérences de la version 1.1, établis le 1er novembre 2026 . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
Liste des figures
Figure 1 — Le cadre en une page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Figure 2 — Du maillage N × M aux contrats communs N + M . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Figure 3 — Architecture de référence : six couches et trois plans transversaux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
Figure 4 — Quatre types de mémoire et contrôles d’écriture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Figure 5 — Quatre niveaux d’interopérabilité appliqués aux agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
Figure 6 — Carte des interactions de l’agent et protocoles retenus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Figure 7 — MCP 2026-07-28 derrière la passerelle d’agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
Figure 8 — Cycle de vie d’une tâche A2A 1.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Figure 9 — Délégation A2A avec appel MCP et approbation humaine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
Figure 10 — Chorégraphie événementielle et compteur de sauts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 5 sur 283


---
## [Page PDF 6]

Figure 11 — Huit patrons d’orchestration autorisés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
Figure 12 — Arbre de décision du patron d’orchestration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
Figure 13 — Saga : transactions locales, pivot et compensations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
Figure 14 — Échelle d’autonomie N0 à N4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
Figure 15 — Contrôle exigé selon la classe de l’agent et le palier de l’outil . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Figure 16 — Approbation humaine signée, liée à l’action exacte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
Figure 17 — Délégation par échange de jetons et droits effectifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
Figure 18 — Contrôles appliqués par la passerelle d’agents à chaque appel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
Figure 19 — Défense contre l’injection : éviter la triade létale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Figure 20 — Niveaux d’isolation pour le code généré . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Figure 21 — Une trace distribuée de bout en bout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
Figure 22 — Évaluation en trois paliers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
Figure 23 — Enveloppe budgétaire d’une tâche . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
Figure 24 — Modèle opérationnel en étoile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
Figure 25 — Cycle de vie d’un agent et points de contrôle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
Figure 26 — Réponse à un incident agentique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
Figure 27 — Modèle de maturité en cinq niveaux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
Figure 28 — Feuille de route : quatre phases et leurs jalons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 6 sur 283


---
## [Page PDF 7]

CRE-IA-2026-01 · Cadre de référence
Sommaire exécutif
Sommaire exécutif
Les agents d’IA ne se contentent plus de répondre : ils lisent des systèmes, prennent des décisions et agissent. 
Ce cadre fixe les règles communes qui permettent de les brancher aux systèmes de l’entreprise, de les faire 
collaborer et de les orchestrer de façon sûre, traçable, réversible et économiquement maîtrisée, quel que soit 
le fournisseur. Il est normatif : les chapitres 5 à 13 énoncent des exigences identifiées, vérifiables en revue 
d’architecture ou en test.
Des agents branchés, collaboratifs et orchestrés
de façon sûre, traçable, réversible et économiquement maîtrisée
12 principes directeurs (PRIN-01 à PRIN-12)
standards ouverts · contrat avant code · moindre privilège et moindre agence · autonomie proportionnée au risque · réversibilité · simplicité d’abord
Interopérabilité
MCP 2026-07-28
A2A 1.0
CloudEvents, AsyncAPI
OpenAPI, catalogue
4 niveaux (EIF)
chapitre 6
Orchestration
8 patrons autorisés
agent unique d’abord
exécution durable
sagas, idempotence
dégradation maîtrisée
chapitre 7
Autonomie
niveaux N0 à N4
paliers d’outils P0 à P3
approbation signée
anti-approbation
machinale
chapitre 8
Identité et sécurité
confiance zéro
délégation RFC 8693
passerelle d’agents
OWASP ASI, injection
bacs à sable
chapitre 9
Observabilité
et FinOps
OpenTelemetry GenAI
audit inaltérable
évaluation 3 paliers
coût par tâche
chapitre 10
Architecture de référence : six couches et trois plans transversaux (chapitre 5)
canaux · orchestration · agents · médiation · outils · systèmes d’enregistrement — identité, observabilité, gouvernance
Gouvernance et cycle de vie (chapitre 11)
registre · RACI · modèle en étoile · homologation
Risques et conformité (chapitres 12 et 13)
Loi 25 · BSIF · RIA · NIST AI RMF · ISO/IEC 42001 · contrats
Mise en œuvre : maturité en 5 niveaux, feuille de route en 4 phases, calée sur 2027-2030, indicateurs (chapitres 14 et 15)
annexes : grille d’homologation, fiche d’agent, contrats types, registre des exigences, glossaire, validation des sources
Figure 1 — Le cadre en une page. Le toit énonce la finalité; les principes s’appliquent à toutes les décisions; les cinq piliers portent les 
règles techniques; l’architecture de référence, la gouvernance et la conformité en sont les fondations; la feuille de route en organise le 
déploiement.
Pourquoi maintenant
40 %
des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026, contre moins de 5 % en 
2025 (prévision Gartner, août 2025)
> 40 %
des projets d’IA agentique seront annulés d’ici la fin de 2027 : coûts, valeur incertaine, contrôles inadéquats 
(prévision Gartner, juin 2025)
13 %
des organisations estiment avoir la bonne gouvernance de leurs agents (Gartner, avril 2026)
> 150 000
agents en usage, en moyenne, par entreprise du Fortune 500 d’ici 2028, contre moins de 15 en 2025 (prévision 
Gartner, avril 2026)
Les agents se multiplient plus vite que les règles pour les relier[1, 2]. Sans cadre commun, chaque équipe recrée 
ses connecteurs, ses accès et ses contrôles; les annulations annoncées par Gartner tiennent aux coûts, à une 
valeur d’affaires incertaine et à des contrôles de risque inadéquats, la maturité encore limitée des modèles 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 7 sur 283


---
## [Page PDF 8]

CRE-IA-2026-01 · Cadre de référence
Sommaire exécutif
s’y ajoutant[3]. Les standards, eux, se sont consolidés aux couches agent-outil et agent-agent. Le Model 
Context Protocol (MCP) et le protocole Agent2Agent (A2A) relèvent désormais tous deux de l’Agentic AI 
Foundation, fondation neutre de la Linux Foundation[4, 5]. Selon l’analyse du cadre (section 2.4), le risque de 
verrouillage s’est déplacé des protocoles vers les plateformes : c’est là que le cadre concentre ses exigences.
Les dix décisions structurantes
Dix décisions résument le cadre; chacune renvoie au chapitre qui la détaille.
1. Deux protocoles pivots, versions épinglées. MCP (révision 2026-07-28) relie un agent à ses outils et 
à ses données; A2A (version 1.0) relie un agent à un autre agent; CloudEvents et AsyncAPI portent les 
échanges asynchrones. Les API existantes sont exposées par adaptateurs, jamais réécrites. Les versions 
applicables sont fixées au catalogue, révisé chaque trimestre (chapitre 6).
2. Rien ne contourne la passerelle ni le catalogue. En environnement serveur, tout appel d’un agent 
vers un outil MCP ou vers une donnée ou un agent d’un autre domaine traverse la passerelle d’agents, 
qui authentifie, autorise, applique les garde-fous, limite les coûts, injecte les secrets et journalise. Un 
outil absent du catalogue est injoignable (chapitre 5, chapitre 9).
3. La simplicité d’abord. Un flux déterministe ou un agent unique bien outillé est le choix par défaut, 
et l’on n’ajoute de la complexité que si elle améliore les résultats de façon démontrée[6]; le cadre en tire 
ses propres règles : le multiagent n’est autorisé que sur preuve mesurée de gain, parmi huit patrons 
autorisés et avec deux niveaux de délégation au plus (chapitre 7).
4. Une échelle d’autonomie unique. Les niveaux N0 à N4 plafonnent ce qu’un agent peut faire seul 
selon la classe de risque; l’autonomie non bornée (NX) est interdite. Les outils sont classés P0 à P3 au 
catalogue; la règle la plus stricte l’emporte, et toute action critique, externe ou irréversible (P3) exige 
une approbation humaine signée et liée à l’action exacte (chapitre 8).
5. Une identité propre à chaque agent, des droits délégués et de courte durée. Aucun compte 
partagé ni clé statique; quand un agent agit pour une personne, il reçoit un jeton délégué (échange 
de jetons, RFC 8693) qui identifie à la fois la personne et l’agent, restreint à une seule ressource cible 
(audience unique), et dont la portée ne s’élargit jamais d’un saut à l’autre (chapitre 9).
6. Présomption d’injection. Tout contenu reçu est une donnée, jamais une instruction. Dès qu’un agent 
a lu du contenu non fiable, ses capacités d’envoi vers l’extérieur lui sont retirées de façon déterministe; 
le code qu’il génère s’exécute dans un bac à sable isolé, réseau fermé par défaut (chapitre 9).
7. Réversibilité par conception. L’état est enregistré de façon durable hors du modèle à chaque tran­
sition; chaque écriture porte une clé d’idempotence; les transactions qui touchent plusieurs systèmes 
suivent le patron saga avec compensations; un coupe-circuit global est testé chaque trimestre (chapitre 
7).
8. On ne gouverne que ce qu’on voit. Traçage OpenTelemetry de bout en bout (conventions GenAI 
épinglées), journal d’audit inaltérable, évaluation en trois paliers, enveloppe budgétaire par tâche et 
coût par tâche réussie (chapitre 10).
9. Une personne nommée répond de chaque agent. Registre d’entreprise obligatoire, cycle de vie à 
points de contrôle, modèle opérationnel en étoile et comité d’architecture et des risques agentiques 
(chapitre 11).
10. Conformité dès la conception. Loi 25 (évaluation des facteurs relatifs à la vie privée, décisions auto­
matisées, communications hors Québec, incidents), ligne directrice E-23 du Bureau du surintendant 
des institutions financières (BSIF, pour les institutions financières fédérales) et règlement européen 
sur l’IA (selon son champ d’application), ainsi que les référentiels volontaires NIST AI RMF et ISO/IEC 
42001, sont intégrés aux exigences et à une matrice de correspondance unique (chapitre 12)[7, 8].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 8 sur 283


---
## [Page PDF 9]

CRE-IA-2026-01 · Cadre de référence
Sommaire exécutif
Par où commencer
La mise en œuvre suit quatre phases séparées par trois jalons, vise le niveau 3 de maturité, « Défini », en 
18 mois, puis le niveau 4 et la certification ISO/IEC 42001 aux jalons 4 et 5 (chapitre 14, chapitre 15). Les 
90 premiers jours établissent les fondations : inventaire de tous les agents et serveurs MCP, propriétaire 
nommé pour chacun, fin des clés partagées, passerelle de modèles, traçage pilote, classement des risques 
et évaluations de vie privée, coupe-circuit testé. Aucun agent ne passe en production sans franchir la grille 
d’homologation de l’annexe A.
CE QUI A CHANGÉ PAR RAPPORT AUX ÉBAUCHES
La vérification a confirmé le fond technique des ébauches, mais a imposé plusieurs corrections  : 
versions de protocoles mises à jour (MCP sans état, A2A 1.0), trois échelles d’autonomie incompatibles 
remplacées par une seule, chiffres de marché réattribués à leur véritable source ou retirés, obligations 
de la Loi 25 rattachées aux bons articles, allégations commerciales retirées des exigences. L’annexe F en 
donne le détail.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 9 sur 283


---
## [Page PDF 10]

CRE-IA-2026-01 · Cadre de référence
Partie I — Fondements
Pourquoi un cadre commun, ce qu’il couvre, le vocabulaire partagé et les principes qui tranchent les 
décisions d’architecture.
1 · Objet, portée et mode d’emploi
2 · Contexte et enjeux
3 · Concepts et définitions
4 · Principes directeurs
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 10 sur 283


---
## [Page PDF 11]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
1 Objet, portée et mode d’emploi
Ce chapitre dit ce que le cadre règle, à quels systèmes il s’applique et à qui il s’adresse. Il explique comment 
lire une exigence, comment le document est organisé et comment il évolue. Il présente enfin la méthode qui 
a servi à l’établir et à vérifier ses faits.
1.1 Objet
Le cadre CRE-IA-2026-01 fixe les règles communes qui permettent aux agents d’IA de l’entreprise de se 
brancher aux systèmes, de collaborer entre eux et d’être orchestrés de façon sûre, traçable, réversible et 
économiquement maîtrisée, quel que soit le fournisseur. La présente version 1.1, datée du 28 octobre 2026, 
est soumise à l’approbation du comité d’architecture et des risques agentiques. Le cadre poursuit quatre 
objectifs :
• donner à toutes les équipes un vocabulaire commun (chapitre 3);
• fixer les protocoles retenus, les patrons d’orchestration autorisés et les niveaux d’autonomie permis 
(chapitres 5 à 8);
• encadrer l’identité, la sécurité, l’observabilité, les coûts, la gouvernance et la conformité des agents 
(chapitres 9 à 13);
• offrir une trajectoire de maturité mesurable et une grille d’homologation applicable à chaque projet 
(chapitres 14 et 15, annexe A).
Le cadre est normatif et neutre à l’égard des fournisseurs. Il règle ce qui doit rester sous le contrôle de 
l’entreprise, quelle que soit la plateforme : contrats d’interface, identités et délégations, passage obligé par la 
passerelle d’agents, traces et journal d’audit, registre, plafonds d’autonomie et de coûts. Il ne choisit aucun 
produit : ceux qu’il cite sont des exemples non limitatifs, à l’état du 27 octobre 2026. Il ne tient pas lieu d’avis 
juridique (chapitre 12).
1.2 Portée
Cette section délimite les systèmes visés. Le critère est fonctionnel : ce qui compte n’est pas l’étiquette 
commerciale d’un système, mais sa capacité à appeler des outils ou à agir sur des systèmes et des données 
de l’entreprise.
Tableau 1 — Portée du cadre
Catégorie
Dans la portée
Hors portée
Agents internes
Tout agent bâti à l’interne, en pilote ou en produc­
tion, qui lit ou modifie des systèmes ou des données 
de l’entreprise
Assistant conversationnel sans outil ni capacité 
d’action, régi par la politique d’usage de l’IA
Agents achetés
Agents intégrés aux logiciels-services (software as a 
service, SaaS) et aux progiciels, dès que l’entreprise 
ou une équipe métier les active
Fonction dite « agentique » qui n’appelle au­
cun outil et n’agit sur rien
Agents de tiers
Agents de partenaires, de fournisseurs ou de clients 
qui échangent avec les agents ou les systèmes de 
l’entreprise
Fonctionnement interne de ces agents : le 
cadre en régit les interfaces, les identités et les 
contrats
Outils et données
Serveurs MCP internes ou externes, outils, API, événe­
ments et sources de données exposés aux agents
Systèmes d’enregistrement eux-mêmes, que le 
cadre n’oblige pas à modifier
Plateformes
Plateformes et moteurs d’orchestration, passerelles 
d’agents et de modèles, registres et catalogues
Choix des fournisseurs de modèles, qui re­
lève de l’architecture d’entreprise et de 
l’approvisionnement
Modèles et automati­
sation
Usage des modèles par les agents; flux déterministe 
qui appelle un agent ou qui est appelé par lui
Entraînement et ajustement fin des modèles; 
automatisation robotisée des processus (RPA) 
sans composante agentique
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 11 sur 283


---
## [Page PDF 12]

CRE-IA-2026-01 · Cadre de référence
1 Objet, portée et mode d’emploi
Trois règles tranchent les cas limites. Un assistant qui reçoit un premier outil, même en lecture seule, entre 
dans la portée dès ce moment. À l’inverse, une fonction qu’un éditeur qualifie d’agentique n’y entre que si 
elle appelle des outils ou agit : Gartner observait d’ailleurs, en juin 2025, que de nombreux produits existants 
étaient simplement rebaptisés « agentiques »[3]. En cas de doute, le système est traité comme visé et inscrit 
au registre (section 11.4).
1.3 Public cible et usages par rôle
Le cadre s’adresse à toutes les fonctions qui conçoivent, exploitent, financent ou contrôlent des agents. 
Personne n’a besoin de tout lire : le tableau 2 indique, pour chaque rôle, par où commencer.
Tableau 2 — Parcours de lecture par rôle
Rôle
À lire en priorité
Direction TI et comité d’architecture et des risques agentiques
Sommaire, chapitres 2, 4, 14 et 15
Architectes d’entreprise et de solutions
Chapitres 3 à 8, annexe A
Équipes de plateforme et d’intégration
Chapitres 5, 6, 9 et 10, annexe C
Équipes produit qui bâtissent des agents
Chapitres 3, 7, 8 et 10, annexes A à C
Sécurité de l’information
Chapitres 8 et 9, section 12.8
Risques, conformité, affaires juridiques et protection des rensei­
gnements personnels (RP)
Chapitres 11 et 12, section 8.8
FinOps
Sections 10.5 et 10.6, chapitre 13
Responsables métier, parrains d’agents
Sommaire, chapitres 3, 8 et 11, annexe B
Approvisionnement
Chapitre 13, section 6.3
Audit interne
Annexes A et D, sections 11.4 et 12.6
Appliquer le cadre à un projet
1. Vérifier la portée et inscrire le système au registre dès la conception (annexe B).
2. Classer le risque (section 12.1), fixer le niveau d’autonomie sous le plafond de la classe (section 8.1) et 
déterminer les évaluations d’impact requises (section 12.9).
3. Retenir l’option la plus simple qui suffit, puis le patron d’orchestration (section 7.3).
4. Choisir les protocoles (section 6.3) et publier les contrats au catalogue d’entreprise (section 6.8).
5. Appliquer les exigences pertinentes (annexe D); justifier par écrit tout écart à une recommandation 
(niveau DEVRAIT) et obtenir une dérogation pour tout écart à une obligation (niveau DOIT) (section 
11.6).
6. Remplir la grille d’homologation (annexe A) avant toute mise en production.
1.4 Force normative
Cette section explique comment lire une exigence. Le cadre emploie trois degrés d’obligation, inspirés des 
mots-clés de la RFC 2119 de l’Internet Engineering Task Force (IETF) et mis en évidence dans le texte.
Tableau 3 — Degrés d’obligation
Expression
Sens
Écart admis
doit, ne doit pas
Obligation
Aucun, sauf dérogation écrite approuvée par le comité (ou, pour un agent de 
classe faible, par l’architecture d’entreprise sur délégation du comité), limitée dans 
le temps et assortie de mesures compensatoires (section 11.6). Certaines obligations 
n’admettent aucune dérogation (section 4.3 et EXIG-GOV-17).
devrait, ne de­
vrait pas
Recommandation
Admis s’il est justifié par écrit dans la fiche d’agent ou la décision d’architecture; la 
revue d’architecture contrôle la justification.
peut
Option
Sans objet.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 12 sur 283
