# chunk_16 — pages PDF 151 à 162 (sur 283)



---
## [Page PDF 151]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
                   "a2a_task_id": "…", "a2a_context_id": "…", "cle_idempotence": "…" },
  "mandant":   { "type": "user", "pseudonyme": "u-5d1e…" },
  "agent":     { "id": "agent-risque-credit", "version": "2.3.0", "invite_systeme": "sha256:…" },
  "action":    { "outil": "erp_enregistrer_decision", "definition": "1.4.1",
                 "arguments_sha256": "…", "issue": "succes" },
  "modele":    { "fournisseur": "…", "servi": "…", "version": "…" },
  "autorite":  { "approbation_jti": "…", "approbateur": "a-91c0…" },
  "precedent_sha256": "…",
  "signature": "<signature du service d’audit>"
}
EXIG-OBS-11 · DOIT
Journal d’audit distinct et exhaustif
Chaque action à effet (outil P2 ou P3), chaque approbation ou refus d’approbation, chaque refus de la 
passerelle (EXIG-IAM-18) et chaque arrêt par coupe-circuit DOIT produire un enregistrement d’audit, 
sans échantillonnage. Le journal DOIT être tenu dans un magasin distinct des traces, sous d’autres 
droits d’accès; aucune équipe qui exploite un agent n’a le droit d’y modifier ni d’y supprimer un 
enregistrement.
Pourquoi : une trace peut être échantillonnée ou purgée par l’exploitation; une preuve ne le peut pas.
EXIG-OBS-12 · DOIT
Enregistrement à cinq éléments, canonisé et signé
Chaque enregistrement DOIT contenir les cinq éléments et les identifiants de corrélation, être canonisé 
selon la RFC 8785, porter l’empreinte de l’enregistrement précédent du même flux et être signé par 
une clé du service d’audit, hors de portée des agents. Les arguments d’outil n’y figurent que par leur 
empreinte SHA-256, calculée sur leur forme canonisée; lorsqu’une approbation a eu lieu, l’empreinte 
d’approbation h (outil ‖ arguments canonisés, section 8.5) y figure aussi.
Pourquoi : choix du cadre; la canonisation de la RFC 8785[236] rend l’empreinte reproductible, de sorte que l’empreinte 
d’approbation, recalculée par la passerelle avant l’exécution, prouve que l’action exécutée est celle qui a été 
approuvée, et le chaînage rend toute suppression détectable.
EXIG-OBS-13 · DOIT
Inaltérabilité et conservation
Le journal d’audit DOIT être tenu en ajout seul, sur un stockage qui interdit modification et effacement 
avant échéance, et son intégrité DOIT être vérifiée automatiquement chaque jour. Il est conservé au 
moins 24 mois, davantage si le calendrier de conservation, un régime sectoriel ou une enquête l’exige, 
puis détruit ou anonymisé à l’échéance (EXIG-CON-10); la règle de conservation des décisions touchant 
une personne s’applique aussi (section 12.2). La table qui relie pseudonymes et personnes est gardée à 
part, sous le contrôle du responsable de la protection des renseignements personnels.
Pourquoi : un journal réinscriptible ne prouve rien; la durée de 24 mois et la vérification quotidienne, choix du cadre, 
dépassent les six mois du RIA pour couvrir une découverte tardive d’un incident.
10.4 Évaluation continue
Cette section fixe la manière dont l’entreprise prouve qu’un agent fait ce qu’on attend de lui, avant et 
pendant son exploitation. Un code HTTP 200 ne dit rien de la justesse d’une réponse : la qualité se mesure, 
en trois paliers (figure 22). Le volet adverse relève de la section 9.9, et la comparaison avec un agent unique, 
de la section 7.1.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 151 sur 283


---
## [Page PDF 152]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Palier 3
Production, en continu
échantillon 5–10 %
Palier 2 — Trajectoires
préproduction, jeu de référence
50 à 200 scénarios, cas adverses
Palier 1 — Contrats déterministes
à chaque modification : schémas MCP, cartes
d’agent, outils simulés, règles de passerelle
Mesure en production
100 % des traces en erreur, relance ou refus
d’approbation; juges automatisés hors du chemin
critique et revue humaine; détection de dérive
Mesure de trajectoire
bons outils, bon ordre, bons arguments;
ancrage factuel dans les résultats d’outils;
respect des garde-fous et du budget
Mesure déterministe
tests de contrat et d’instantané du catalogue;
tests d’injection de fautes des sagas;
tests des politiques de la passerelle
Tout changement de modèle, d’invite, d’outil ou de version de protocole relance les paliers 1 et 2.
Figure 22 — Évaluation en trois paliers. Le palier 1 vérifie les contrats à chaque modification, le palier 2 mesure les trajectoires sur un 
jeu de référence en préproduction, le palier 3 échantillonne la production. Tout changement de modèle, d’invite, d’outil ou de version 
de protocole relance les deux premiers. Source : cadre CRE-IA-2026-01.
Palier 1 : contrats. Sans aucun modèle, il valide les schémas MCP et les cartes d’agent, teste les outils 
contre des doublures, vérifie les politiques de la passerelle (EXIG-IAM-21) et rejoue l’injection de fautes des 
sagas (EXIG-ORC-20). Les validateurs appliquent MCP 2026-07-28 : la spécification interdit de déréférencer 
automatiquement un $ref réseau et recommande de rejeter une référence externe non résolue et de borner 
la profondeur de validation[162]. La conformité passe par a2a-tck, dont les échecs aux tests de niveau MUST 
(obligatoire) sont bloquants[243], et, à titre informatif tant que le cadre officiel de conformité MCP se déclare 
instable, par ses tests (section 6.8).
Palier 2 : trajectoires. Sur un jeu de référence de 50 à 200 scénarios (fourchette du cadre), qui comprend cas 
nominaux, cas limites et tentatives d’injection en français et en anglais, on mesure la justesse de la trajectoire 
(bons outils, bon ordre, bons arguments), l’ancrage factuel dans les résultats d’outils et le respect des garde-
fous et du budget. Le cadre ne présume pas qu’un modèle rende la même sortie à entrées identiques : chaque 
scénario se répète. Évaluer un agent peut avoir des effets réels : l’article qui présente Magentic-One décrit 
AutoGenBench, dont les contrôles de répétition et d’isolation sont importants dès que les actions d’agents 
ont des effets de bord[279].
Palier 3  : production. On évalue de 5 à 10  % des traces (fourchette du cadre), plus toutes 
celles qui ont subi une erreur, une relance, un plafond atteint ou un refus d’approbation, par 
des juges automatisés hors du chemin critique et par une revue humaine. Anthropic décrit 
un juge qui rend, en un seul appel, un score de 0,0 à 1,0 et un verdict de réussite ou 
d’échec[17]. Le résultat se consigne dans l’événement gen_ai.evaluation.result (Development)  : 
gen_ai.evaluation.name (requis), gen_ai.evaluation.score.value, gen_ai.evaluation.score.label 
(p. ex. pass) et gen_ai.evaluation.explanation (texte libre, soumis à l’EXIG-OBS-07 : en production, il 
ne reproduit ni invite ni réponse), et devrait être rattaché au span évalué[396]. Les défaillances multiagents 
se classent selon la taxonomie MAST (Multi-Agent System Failure Taxonomy) (section 7.9), et les entrées du 
bus peuvent être rejouées en isolement pour éprouver une nouvelle version (EXIG-EVT-10).
Tableau 42 — Familles d’objectifs de niveau de service d’un agent (cibles proposées par le cadre)
Famille
Indicateurs
Cible proposée
Fiabilité technique
Succès des appels MCP et A2A; latence par étape au 95e 
centile
Plus de 99,5 % de succès; latence fixée au 
contrat
Efficacité
Tâches achevées sans erreur; étapes par tâche; appels 
d’outils invalides
Moins de 1 % d’appels invalides
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 152 sur 283


---
## [Page PDF 153]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Famille
Indicateurs
Cible proposée
Qualité et sécurité
Réponses non ancrées sur échantillon; violations de garde-
fous; approbations sans modification (section 8.7)
Moins de 0,5 % de réponses non ancrées; 
aucune violation d’un garde-fou bloquant
Économie unitaire
Coût moyen et au 99e centile par tâche réussie, en dollars 
canadiens
Sous le coût du processus de référence sans 
agent
Cibles : choix du cadre, à calibrer agent par agent au contrat.
EXIG-EVA-01 · DOIT
Paliers franchis et relancés à chaque changement
Tout agent DOIT franchir les paliers 1 et 2 avant sa mise en production et rester soumis au palier 3 en 
exploitation. Tout changement de modèle, y compris derrière un même alias (EXIG-ARC-09), d’invite 
système, d’outil, de palier d’outil ou de version de protocole relance les paliers d’évaluation 1 et 2. Les 
tests du palier 1 DOIVENT s’exécuter en intégration continue et bloquer le déploiement en cas d’échec.
Pourquoi : le comportement d’un agent change sans que son code change; seule une mesure relancée détecte la 
régression.
EXIG-EVA-02 · DOIT
Jeu de référence tenu et versionné
Chaque agent DOIT disposer d’un jeu de référence de 50 à 200 scénarios, versionné avec lui, couvrant 
ses compétences, des cas limites et des tentatives d’injection en français et en anglais. Toute défaillance 
confirmée en production y ajoute un scénario. Les seuils de trajectoire, d’ancrage et de garde-fous 
figurent au contrat; un seuil manqué bloque la mise en production.
Pourquoi : un jeu nourri par les défaillances réelles empêche qu’une erreur corrigée revienne.
EXIG-EVA-03 · DOIT
Évaluations répétées et isolées
Les évaluations du palier 2 et les rejeux DOIVENT s’exécuter en environnement isolé, outils à effet 
remplacés par des doublures. Chaque scénario DOIT s’exécuter au moins trois fois (choix du cadre); on 
retient le taux de réussite et sa dispersion.
Pourquoi : une évaluation qui touche des systèmes réels en répète les effets, et une exécution unique ne dit rien de 
la variabilité[279].
EXIG-EVA-04 · DOIT
Échantillonnage de la production
L’évaluation en production DOIT porter sur un échantillon aléatoire de 5 à 10  % des traces et 
sur toutes les traces marquées d’une erreur, d’une relance, d’un plafond atteint ou d’un refus 
d’approbation. Elle s’exécute hors du chemin critique, et chaque résultat est consigné par un événement 
gen_ai.evaluation.result rattaché au span évalué.
Pourquoi : l’événement normalisé relie chaque score à son exécution (rattachement au span évalué ou, à défaut, par 
gen_ai.response.id); le ciblage des traces atypiques (erreur, relance, plafond, refus) est un choix du cadre[396].
EXIG-EVA-05 · DOIT
Juge automatisé encadré
Un juge à base de modèle DOIT être distinct du modèle ou de l’invite qu’il évalue, appliquer une grille 
versionnée et être calibré contre des évaluations humaines, avec un taux d’accord revu chaque trimestre. 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 153 sur 283


---
## [Page PDF 154]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Ses verdicts alimentent indicateurs et alertes; ils NE DOIVENT PAS autoriser ni bloquer une action 
en production.
Pourquoi : un juge partage les faiblesses des modèles qu’il évalue; il mesure, il ne gouverne pas.
EXIG-EVA-06 · DOIT
Objectifs de niveau de service et réaction aux écarts
Chaque agent en production DOIT déclarer à son contrat des objectifs pour les quatre familles du 
tableau 42; un système multiagent DOIT en outre classer ses défaillances selon la taxonomie MAST. 
Un objectif manqué pendant deux périodes consécutives (choix du cadre) déclenche une revue par 
le parrain et le responsable technique, qui corrigent, réduisent le niveau d’autonomie ou suspendent 
l’agent (section 11.5).
Pourquoi : un objectif sans conséquence prévue ne gouverne rien.
10.5 Économie de l’inférence
Cette section donne les repères économiques vérifiés qui fondent les règles de maîtrise des coûts. Les chiffres 
des fournisseurs y sont des grilles ou des allégations datées, jamais des exigences.
Des prix qui baissent, des volumes qui montent. Presque tous les praticiens FinOps sondés gèrent 
désormais des dépenses d’IA (section 2.1); le State of FinOps 2026 cite parmi leurs défis la visibilité sur des 
modèles de prix hétérogènes, la répartition des coûts et la mesure du rendement[10]. Selon l’AI Index 2025 de 
Stanford (l’édition 2026 est parue depuis; le chiffre n’a pas été revérifié dans celle-ci), le coût d’inférence d’un 
système de niveau GPT-3.5 a baissé de plus de 280 fois entre novembre 2022 et octobre 2024, soit un coût à 
capacité constante, non une baisse générale du prix du jeton[397]. Epoch AI (mars 2025) mesure une baisse 
de 9 à 900 fois par an selon le seuil visé, les baisses les plus rapides ayant été observées au cours de l’année 
précédant la publication et leur persistance étant incertaine[398]. En sens inverse, un agent consomme bien 
plus de jetons qu’une conversation (section 7.1), et les définitions d’outils pèsent à chaque appel : selon 
Anthropic, 58 outils MCP occupent environ 55 000 jetons avant le premier message (mesure de novembre 
2025, antérieure au segmenteur des modèles Claude 4.7 et suivants)[205].
Une facture qui dépend de la configuration. En octobre 2026, la grille d’Anthropic affiche, par million 
de jetons, 0,10 $ US en entrée et 0,50 $ US en sortie pour Claude Haiku 5.5 (invites d’au plus 100 000 jetons, 
lectures et écritures de cache comprises; au-delà, 0,50 $ US en entrée et 2,50 $ US en sortie), contre 10 $ US et 
50 $ US pour Claude Fable 5.1, soit un facteur 100. S’y cumulent le rabais des lots, les multiplicateurs du cache 
et une majoration de 10 % pour l’inférence restreinte aux États-Unis comme pour les points de terminaison 
régionaux des plateformes partenaires; le segmenteur (tokenizer) des modèles Claude 4.7 et suivants produit 
en outre environ 30 % plus de jetons pour un même texte que le segmenteur précédent (celui de Claude 
Sonnet 4.6 et des modèles antérieurs), l’écart variant selon le contenu[399]. On compare donc des modèles au 
coût par tâche réussie, après normalisation, et un choix de résidence dicté par une EFVP (section 12.2) entre 
au modèle de coût; la zone « us » de l’API d’Anthropic n’est pas une résidence canadienne, et aucune zone 
canadienne n’y est offerte[400].
Des leviers documentés. Le traitement asynchrone par lots coûte 50 % de moins chez Anthropic comme 
chez OpenAI, avec une fenêtre de traitement de 24 heures[88, 89]. Le cache d’invites récompense un préfixe 
stable : chez Anthropic, le préfixe suit l’ordre outils, système, messages, toute modification d’une définition 
d’outil invalide le cache entier, et une lecture en cache coûte au plus 0,1 fois le prix d’entrée (0,05 fois pour 
Claude Opus 5.5 et Sonnet 5.5, 0,025 fois pour Claude Fable 5.1), mais une écriture coûte 1,25 fois (durée 
de vie de 5 minutes, par défaut) ou 2 fois (1 heure) ce prix[401]; chez OpenAI, le cache s’active dès 1 024 
jetons pour GPT-5.6 et les suivants, et OpenAI recommande de placer le contenu stable avant le contenu 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 154 sur 283


---
## [Page PDF 155]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
dynamique[402]. Enfin, NVIDIA Research et Georgia Tech estiment que servir un petit modèle de 7 milliards 
de paramètres coûte de 10 à 30 fois moins, en latence, en énergie et en calcul, qu’un modèle de 70 à 175 
milliards, et que de 40 à 70 % des requêtes de leurs études de cas pourraient lui être confiées[403]. C’est un 
coût de calcul, non un prix facturé, et l’équivalence de qualité reste une thèse que seule une mesure tranche.
ATTENTION
Les pourcentages d’économie par levier qui circulent dans la littérature commerciale (routage, élagage 
du contexte, cache sémantique, plafonds) n’ont, pour la plupart, aucune source vérifiable. Le cadre n’en 
reprend aucun : chaque levier se juge à l’économie mesurée sur la charge de l’entreprise.
Des unités propres aux plateformes SaaS. En octobre 2026, Microsoft Copilot Studio facture en Copilot 
Credits (par exemple 5 par action d’agent avec le moteur standard, et 10 par 1 000 jetons pour un modèle 
de raisonnement); au-delà de 125 % de la capacité prépayée du locataire, les agents personnalisés sont 
désactivés, sauf si la facturation à l’usage absorbe le dépassement, et un plafond mensuel peut être fixé 
par agent[53]. Salesforce Agentforce propose notamment des crédits à 0,005 $ US, soit environ 0,10 $ US par 
action standard, à titre indicatif[55]. Ces unités ne se comparent pas sans conversion.
EXIG-FIN-01 · DOIT
Comparaison au coût par tâche réussie
Le choix ou le changement d’un modèle, d’un fournisseur ou d’une plateforme DOIT reposer sur le 
coût par tâche réussie mesuré sur le jeu de référence (section 10.4), et non sur le prix du jeton. Le 
modèle de coût intègre les modificateurs de prix (lots, cache, résidence), la normalisation des jetons 
d’un segmenteur à l’autre et, pour un modèle hébergé par l’entreprise, l’hébergement, l’exploitation 
et l’évaluation.
Pourquoi : un même texte ne donne pas le même nombre de jetons d’un modèle à l’autre[399], et le coût de calcul 
d’un petit modèle n’est pas son coût total[403].
EXIG-FIN-02 · DOIT
Hypothèses de prix datées et révisées
Les prévisions budgétaires DOIVENT reposer sur des hypothèses de prix datées, révisées chaque 
trimestre avec le catalogue, sans extrapoler les baisses passées. Les exigences et les contrats d’agent NE 
DOIVENT PAS inscrire le prix d’un modèle : les fiches renvoient aux grilles des fournisseurs.
Pourquoi : les grilles changent souvent, et la persistance des baisses observées est incertaine[398].
EXIG-FIN-03 · DOIT
Unités SaaS converties et plafonnées
Pour tout agent exploité sur une plateforme SaaS, l’équipe FinOps DOIT tenir une table de conversion 
entre les unités de l’éditeur (crédits, actions, conversations) et le coût par tâche réussie, et configurer 
les plafonds offerts, comme un plafond mensuel par agent. Un dépassement qui désactive des agents 
DOIT être traité comme un risque de continuité, avec seuil d’alerte et responsable nommé.
Pourquoi : sans conversion, construire et acheter ne se comparent pas, et un dépassement de capacité peut arrêter 
des agents[53].
10.6 Maîtrise des coûts
Cette section transforme ces repères en mécanismes de maîtrise des coûts, de l’enveloppe de la tâche 
jusqu’au calcul du coût par tâche réussie.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 155 sur 283


---
## [Page PDF 156]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Enveloppe budgétaire et quotas
Chaque demande reçoit à son entrée une enveloppe de jetons, de coût, d’appels d’outils et de délai (figure 
23). Le Generative AI Lens d’AWS Well-Architected Framework recommande de telles conditions d’arrêt 
(délais d’expiration, limites de jetons) pour rendre prévisible le coût maximal d’un agent, et juge le risque 
élevé en leur absence[404]. Les plafonds se déclarent à la fiche (EXIG-ORC-26) et voyagent avec chaque 
appel (EXIG-ARC-02); les valeurs de la figure sont illustratives. Aucune norme ne fixe les seuils : le cadre 
alerte à 80 % et arrête à 100 %. À la passerelle de modèles, les quotas s’appliquent par période; la politique 
llm-token-limit d’Azure API Management, par exemple, limite les jetons par minute et par quota sur 
une période d’une heure à un an, mais compte séparément par passerelle, estime les jetons en diffusion 
en continu, et sa limite peut être dépassée temporairement par des requêtes concurrentes[107]. Un quota de 
passerelle est donc une borne approximative; l’enveloppe, une borne logique.
ENVELOPPE ATTRIBUÉE À LA DEMANDE (EXEMPLE)
Jetons
41 200 / 50 000
Coût
0,52 $ / 0,75 $
Appels d’outils
9 / 15
Délai
38 s / 60 s
CONSOMMATION DES JETONS PAR ÉTAPE
1
2 · planification
3
4 · arbitrage
5
6
80 % : alerte au propriétaire
100 % : arrêt
propre et escalade
Modèle compact : triage, extraction, routage, appel d’outil simple
Modèle de raisonnement : planification complexe, arbitrage, ambiguïté critique
La passerelle de modèles et l’orchestrateur
décrémentent l’enveloppe à chaque étape;
le coût est imputé au centre de coûts de la trace.
Figure 23 — Enveloppe budgétaire d’une tâche. L’enveloppe se décrémente à chaque étape; à 80 % d’un plafond, le propriétaire 
est alerté; à 100 %, l’exécution s’arrête proprement et passe en escalade. Les étapes simples vont au modèle compact, la planification 
au modèle de raisonnement. Source : cadre CRE-IA-2026-01; valeurs illustratives.
EXIG-FIN-04 · DOIT
Enveloppe appliquée à chaque étape
La passerelle de modèles et l’orchestrateur DOIVENT décrémenter l’enveloppe à chaque appel de 
modèle et d’outil, alerter le propriétaire dès qu’un plafond atteint 80 % et, à 100 %, arrêter l’exécution en 
état sûr et la passer en escalade, avec un refus typé « budget épuisé » (EXIG-IAM-18). Un orchestrateur 
qui délègue attribue à l’exécutant une part de l’enveloppe restante, jamais une enveloppe neuve.
Pourquoi : les conditions d’arrêt bornent le coût maximal[404], et une enveloppe recréée à chaque délégation rendrait 
le plafond inopérant; les seuils de 80 et 100 % sont des choix du cadre.
EXIG-FIN-05 · DOIT
Quotas et plafond mensuel par agent
Chaque agent DOIT disposer, à la passerelle de modèles, d’un quota de jetons par minute et d’un plafond 
mensuel de coût inscrits à sa fiche (annexe B), avec une marge déclarée pour les dépassements possibles 
en concurrence. À son plafond mensuel, l’agent est suspendu ou ramené à son modèle de repli, selon 
sa fiche, et le parrain en est avisé.
Pourquoi : un agent ambiant s’exécute sans demande humaine, et la limite d’une passerelle peut être dépassée 
temporairement[107].
Routage frugal, préfixe stable et lots
Le Centre d’architecture Azure demande d’attribuer à chaque agent un modèle proportionné à sa tâche, 
en notant que classification, extraction et mise en forme peuvent souvent se confier à de petits modèles 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 156 sur 283


---
## [Page PDF 157]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
sans baisse de la qualité globale, et de mesurer les jetons par agent et par exécution[9]. Le Generative AI 
Lens retient trois principes : choisir le modèle et le mode d’inférence selon le besoin réel, contrôler la 
longueur des invites et des réponses, borner les flux[405]. Les modèles de raisonnement se réservent d’abord 
à la planification complexe, à l’arbitrage entre contraintes et aux ambiguïtés critiques; tout autre emploi se 
justifie par une mesure (EXIG-FIN-06).
Pour profiter du cache, une invite va du plus stable au plus variable  : outils, instructions système, 
documents récurrents, puis demande. Les serveurs MCP internes listent leurs outils dans un ordre déter­
ministe (EXIG-MCP-03), et un outil chargé à la demande s’ajoute après le point de rupture du cache 
(section 6.5). Le taux de succès du cache se lit en rapportant gen_ai.usage.cache_read.input_tokens à 
gen_ai.usage.input_tokens, que la convention demande (SHOULD) d’établir en y incluant les jetons servis 
depuis le cache; l’API d’Anthropic rapporte toutefois ses lectures en cache à part, et le dénominateur se 
vérifie donc par fournisseur[119].
EXIG-FIN-06 · DOIT
Plus petit modèle suffisant
Chaque étape d’un agent DOIT être servie par le plus petit modèle homologué qui atteint, pour cette 
étape, les seuils du jeu de référence. L’emploi d’un modèle de raisonnement se justifie à la fiche par 
une mesure; la passerelle applique la correspondance entre étape et modèle, de préférence par alias 
logique (EXIG-ARC-09).
Pourquoi : l’écart de prix atteint un facteur 100 chez un même fournisseur (Claude Fable 5.1 contre Claude Haiku 5.5, 
pour des invites d’au plus 100 000 jetons; facteur 20 au-delà)[399]; c’est le levier le plus direct, pourvu que la qualité 
soit démontrée.
EXIG-FIN-07 · DOIT
Préfixe stable et cache mesuré
Les invites DOIVENT être assemblées en préfixe stable (outils, instructions système, contenus récur­
rents) suivi du contenu variable. Une définition d’outil ou une invite système DOIT se modifier par 
une version déployée, jamais à la volée. Le taux de lecture en cache est suivi par agent, et une baisse 
marquée ouvre une analyse.
Pourquoi : modifier une définition d’outil invalide tout le cache[401], et OpenAI recommande de placer le contenu 
stable en tête[402].
EXIG-FIN-08 · DEVRAIT
Lots asynchrones pour les charges non urgentes
Les charges non urgentes des agents ambiants, des évaluations et des traitements périodiques 
DEVRAIENT passer par les API par lots lorsque leur délai, jusqu’à 24 heures, est acceptable. 
L’orchestrateur consigne l’identifiant du lot à son point de contrôle pour en reprendre les résultats 
(section 7.4).
Pourquoi : le traitement par lots coûte 50 % de moins chez les fournisseurs vérifiés[88, 89].
Imputation et économie unitaire
Le cadre FinOps définit le périmètre de dépenses (Scope) comme un segment de dépenses aligné sur des 
constructions d’affaires (produit, centre de coûts, environnement) et cite la dépense d’IA agentique en 
exemple[406]. Le guide FinOps for AI (mis à jour le 17 février 2026) recommande de mettre en place un 
modèle de refacturation indicative (showback) et une stratégie d’étiquetage, et relève l’absence de cadres 
généralement admis pour répartir les coûts entre charges multiagents[407]. FOCUS 1.4 (FinOps Open Cost 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 157 sur 283


---
## [Page PDF 158]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
and Usage Specification) normalise les données de facturation (coûts, catégorie de service, quantité et unité 
consommées, étiquettes), avec une catégorie « AI and Machine Learning », mais sans colonne native de 
jetons ni indicateur par agent[408, 409]; la version 1.5 est traitée au chapitre 13. Les indicateurs par agent se 
calculent donc en joignant coûts FOCUS, télémétrie gen_ai.* et résultats métier. Le cadre en définit trois :
• Coût par tâche réussie : coût total imputé à l’agent (inférence, outils, quote-part de la plateforme) 
divisé par le nombre de tâches réussies selon son contrat, en dollars canadiens.
• Jetons par agent et par exécution : ventilés en entrée, sortie, lecture et écriture en cache et, s’il y a 
lieu, raisonnement, chaque catégorie se facturant à un tarif différent.
• Ratio jetons/résultat : jetons par tâche réussie; sa hausse à qualité égale signale une dérive (contexte 
qui enfle, boucle, cache rompu).
EXIG-FIN-09 · DOIT
Imputation par centre de coûts
Chaque span DOIT porter le centre de coûts imputé (ca.entreprise.cost_center), tiré du référentiel 
financier et identique à l’étiquette des données de facturation. La dépense agentique est suivie comme 
un périmètre de dépenses FinOps (Scope) distinct, avec ses responsables. L’imputation commence par 
la refacturation indicative; la refacturation réelle suit, sur décision du comité, une fois les indicateurs 
stabilisés.
Pourquoi : la FinOps Foundation recommande la refacturation indicative pour l’IA[407]; une étiquette commune rend 
la jointure possible.
EXIG-FIN-10 · DOIT
Indicateurs d’économie unitaire publiés
L’équipe FinOps DOIT calculer chaque mois, pour chaque agent en production, les trois indicateurs ci-
dessus, à partir des données FOCUS exigées des fournisseurs (chapitre 13), de la télémétrie de la version 
épinglée et des résultats métier, et les transmettre au parrain et les inscrire au registre. Un agent dont 
le coût par tâche réussie dépasse celui du processus de référence deux mois de suite (choix du cadre) 
passe en revue de valeur (section 11.5).
Pourquoi : FOCUS normalise les données de facturation, non la performance des agents[410]; seul le croisement des 
coûts, des jetons et des résultats dit si un agent crée de la valeur.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 158 sur 283


---
## [Page PDF 159]

CRE-IA-2026-01 · Cadre de référence
Partie IV — Gouvernance, conformité et mise 
en œuvre
Qui décide et répond de quoi, quelles obligations s’appliquent, comment acheter, mesurer la maturité et 
déployer le cadre.
11 · Gouvernance et cycle de vie
12 · Risques, conformité et réglementation
13 · Approvisionnement et clauses contractuelles
14 · Modèle de maturité
15 · Feuille de route et indicateurs
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 159 sur 283


---
## [Page PDF 160]

CRE-IA-2026-01 · Cadre de référence
11 Gouvernance et cycle de vie
11 Gouvernance et cycle de vie
Un agent qui agit au nom de l’entreprise relève d’une personne nommée, figure au registre et suit un 
parcours balisé, de sa proposition à son retrait. Ce chapitre répartit les rôles, fixe la matrice RACI et le 
modèle opérationnel en étoile, puis définit le registre d’entreprise des agents et des serveurs MCP, les points 
de contrôle du cycle de vie et le régime des dérogations. Il précise enfin comment le cadre admet, révise et 
retire les standards de son catalogue.
À RETENIR
Trois règles structurent ce chapitre : une personne nommée répond de chaque agent; sans fiche complète 
au registre, aucun justificatif de production; tout changement significatif rouvre l’évaluation. Les rôles, 
la matrice RACI, les points de contrôle et les dérogations organisent l’application de ces trois règles.
11.1 Rôles et responsabilités
Cette section nomme les rôles que le cadre mobilise et ce que chacun doit livrer (tableau 43). Le principe est 
simple : un agent ne répond pas de ses actes (section 3.4); une personne identifiable en répond, et chaque 
décision du cycle de vie revient à un rôle précis.
Les référentiels convergent sur ce point. Le NIST AI RMF demande que les rôles et responsabilités liés aux 
risques de l’IA soient documentés (GOVERN 2.1) et que l’intensité de la gestion des risques suive la tolérance 
au risque de l’organisation (GOVERN 1.3)[74]. ISO/IEC 42001 traite des rôles à l’article 5.3 et de l’organisation 
interne à la mesure A.3 de son annexe A[395]. Au Québec, la Loi sur la protection des renseignements 
personnels dans le secteur privé (RLRQ, c. P-39.1, ci-après « Loi sur le privé »), modifiée par la Loi 25, confie 
la fonction de responsable de la protection des renseignements personnels (RPRP) à la personne ayant la 
plus haute autorité, qui peut la déléguer par écrit; la Loi exige aussi des politiques de gouvernance qui 
précisent les rôles et responsabilités tout au long du cycle de vie des renseignements (art. 3.1 et 3.2)[56]. Les 
organismes publics appliquent les dispositions équivalentes de la Loi sur l’accès, notamment les articles 63.3 
(règles de gouvernance) et 63.5 (EFVP)[56].
Microsoft Entra Agent ID distingue, pour chaque agent, un parrain (sponsor), qui porte la responsabilité 
métier, et un propriétaire, qui l’administre techniquement[90]. Le cadre reprend cette distinction sans 
dépendre du produit : le propriétaire métier joue le rôle de parrain, le responsable technique celui de 
propriétaire au sens d’Entra.
Tableau 43 — Rôles de la gouvernance agentique
Rôle
Responsabilités principales
Fondement ou remarque
Propriétaire métier 
(parrain)
Répond de la finalité, des résultats et des effets de l’agent; demande 
son niveau d’autonomie; finance l’agent; atteste périodiquement qu’il 
est encore requis.
Une personne, jamais une 
équipe ni un fournisseur.
Responsable tech­
nique
Conçoit, construit, teste et exploite l’agent; tient à jour sa fiche, son 
contrat et sa carte d’agent; dirige l’équipe de garde.
Ne peut homologuer son 
propre agent (EXIG-GOV-03).
Équipe plateforme
Opère les passerelles, le registre, le catalogue, le traçage, l’outillage 
d’évaluation, les gabarits et le coupe-circuit global.
Centre du modèle en étoile 
(section 11.3).
Architecture 
d’entreprise
Tient le cadre et le catalogue des protocoles; conduit les revues 
d’architecture; instruit les dérogations.
Gouvernance des standards 
(section 11.7).
Sécurité 
de l’information
Modèle de menaces; politique des identités et des paliers d’outils; 
tests d’abus et équipe rouge; réponse aux incidents de sécurité.
Chapitre 9.
Risques et conformité
Classe le risque des agents; vérifie la conformité réglementaire; suit les 
dérogations et les risques résiduels.
Chapitre 12.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 160 sur 283


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
