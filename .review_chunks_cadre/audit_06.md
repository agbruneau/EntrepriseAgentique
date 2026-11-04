# Audit chunk_06 — pages 51-62

## Synthèse
Le chunk couvre la fin du catalogue des protocoles (EXIG-INT-06 à 09), la matrice de sélection (tableau 16, EXIG-INT-10 et 11) et la première partie du § 6.5 sur MCP 2026-07-28 (gouvernance, figure 7, tableau 17, cache, extensions, primitives, transport, autorisation, EXIG-MCP-01 à 14). Le texte est dense, bien sourcé, et distingue avec soin ce que la spécification exige de ce que le cadre choisit. Les trois défauts les plus graves :
1. EXIG-MCP-01 (« tout outil » par MCP derrière la passerelle) contredit les exceptions intradomaine d'EXIG-ARC-01 et d'EXIG-IAM-17.
2. L'audience du jeton est ambiguë : la figure 7 parle d'un jeton « émis pour ce serveur », mais l'URI canonique est celle de la passerelle, et l'agrégation derrière un point d'accès virtuel casse l'audience unique.
3. Les ressources MCP échappent aux contrôles de palier et sont mises en cache sous une clé « contexte d'autorisation » non définie, sans invalidation à la révocation.

## Constats

### [06-01] [BLOQUANT] EXIG-MCP-01 contredit les exceptions intradomaine d'EXIG-ARC-01 et d'EXIG-IAM-17
- **Axe** : A
- **Localisation** : § 6.5, EXIG-MCP-01, p. 54 : « Tout outil, toute ressource et toute invite mis à la disposition d'un agent DOIVENT l'être par un serveur MCP inscrit au catalogue d'entreprise ». Comparer avec EXIG-ARC-01, p. 33 : « les appels internes à un même domaine applicatif sans serveur MCP ni pair A2A sont régis par l'EXIG-IAM-17 », et EXIG-IAM-17, p. 129 : « À l'intérieur d'un domaine, la décision par appel (EXIG-IAM-02) est appliquée par le serveur de ressources ».
- **Diagnostic** : trois DOIT décrivent le même périmètre de deux façons. EXIG-MCP-01 n'admet aucun outil hors MCP et interdit toute connexion directe d'un hôte à un serveur de domaine. EXIG-ARC-01 et EXIG-IAM-17, eux, prévoient explicitement des outils intradomaine sans serveur MCP, contrôlés par le serveur de ressources et le maillage. EXIG-MCP-01 ne dit rien non plus des outils en processus (fonctions locales du cadriciel, calculs purs) ni des outils hébergés par le fournisseur de modèles.
- **Contre-exemple** : un agent de facturation appelle en processus une fonction de calcul de taxes de son propre domaine. EXIG-ARC-01 et EXIG-IAM-17 l'autorisent. EXIG-MCP-01 exige pour la même fonction un serveur MCP inscrit au catalogue, publié derrière la passerelle, avec un aller-retour réseau et un échange de jetons. L'homologateur ne peut pas trancher.
- **Correctif proposé** : borner EXIG-MCP-01 aux capacités qui franchissent une frontière de domaine ou qui touchent un système d'enregistrement. Renvoyer explicitement à l'exception d'EXIG-ARC-01 et d'EXIG-IAM-17. Statuer sur les outils en processus et sur ceux hébergés par le fournisseur de modèles (interdits, ou palier P0 seulement).
- **Confiance** : vérifié dans le texte.

### [06-02] [MAJEUR] Audience du jeton à la passerelle : figure 7 ambiguë, agrégation incompatible avec l'audience unique
- **Axe** : A
- **Localisation** : figure 7 et exemple, p. 56 : « Host: passerelle-agents.interne.exemple … Authorization: Bearer <jeton émis pour ce serveur seulement> » et « Le jeton n'est valable que pour ce serveur (EXIG-MCP-11) ». Comparer avec p. 60 (« l'URI canonique annoncée aux clients est la sienne »), p. 55 (« en agréger plusieurs derrière un point d'accès virtuel ») et EXIG-MCP-11, p. 61 (« NE DOIT PAS accepter un jeton qui n'a pas été émis pour lui »).
- **Diagnostic** : le jeton présenté par l'hôte est adressé à la passerelle (`Host`, chemin `/mcp`). S'il est émis pour le serveur de domaine, comme le suggère « ce serveur », la passerelle accepte un jeton qui ne lui est pas destiné, ce qui viole EXIG-MCP-11. S'il est émis pour la passerelle, comme le dit la p. 60, la figure induit en erreur. Dans le cas agrégé, l'URI canonique du point d'accès virtuel couvre plusieurs serveurs de domaine : la promesse « valable pour ce serveur seulement » devient fausse, et seules les portées discriminent les serveurs.
- **Contre-exemple** : la passerelle agrège CRM, ERP et GED sous `https://passerelle-agents.interne.exemple/mcp`. Un jeton (`resource` égale cette URI) obtenu pour lire le CRM est accepté pour un `tools/call` ERP si les portées ne sont pas cloisonnées par serveur. L'audience n'offre alors aucune isolation.
- **Correctif proposé** : écrire dans la figure « jeton émis pour ce point d'accès de la passerelle ». Exiger un point d'accès, donc une URI canonique, par serveur de domaine, ou, à défaut, des portées préfixées par l'identifiant de serveur et vérifiées par la passerelle. Rattacher la règle à EXIG-MCP-09 et EXIG-MCP-11.
- **Confiance** : vérifié dans le texte (incohérence); conséquence déduite.

### [06-03] [MAJEUR] Les ressources échappent aux contrôles de palier, alors qu'EXIG-MCP-05 y déplace les lectures
- **Axe** : A
- **Localisation** : EXIG-MCP-05, Pourquoi, p. 59 : « la ressource se lit sans effet et se met en cache; l'outil porte un contrat d'entrée strict et passe par les contrôles de palier ». Voir aussi p. 58 (« crm://comptes/9482/sommaire se lit sans effet sur le système ») et EXIG-MCP-14, p. 62 (« le palier de risque, le seuil d'approbation et l'outil de compensation d'un outil »).
- **Diagnostic** : l'échelle P0-P3 et EXIG-MCP-14 ne visent que les outils. EXIG-MCP-05 recommande pourtant d'exposer en ressource toute lecture d'entité connue, y compris les lectures sensibles, qui relèveraient de P1 pour un outil. Le texte affirme aussi que la lecture est « sans effet », ce que le serveur seul déclare : c'est la même confiance que le cadre refuse aux annotations. Rien ne dit comment la triade létale (§ 9.6), qui repose sur la lecture de contenu sensible ou non fiable, traite un `resources/read`.
- **Contre-exemple** : un serveur CRM expose `crm://clients/{id}/dossier` (renseignements personnels) en ressource. Aucun palier, aucun seuil d'approbation, aucune marque de « lecture sensible » ne s'applique. La réponse est mise en cache selon `ttlMs`, et la lecture ne déclenche pas le retrait des capacités d'envoi.
- **Correctif proposé** : étendre au catalogue l'attribution d'un palier (P0 ou P1) à chaque gabarit de ressource. Exiger que la passerelle l'applique à `resources/read` comme à `tools/call`, y compris pour le marquage des contenus non fiables (§ 9.6). Retirer « sans effet » ou le présenter comme une déclaration du serveur.
- **Confiance** : déduit (aucune occurrence de palier appliqué aux ressources dans full.txt).

### [06-04] [MAJEUR] Cache « private » : clé non définie, aucune invalidation à la révocation ou à la réduction de portées
- **Axe** : A | B
- **Localisation** : EXIG-MCP-03, p. 58 : « pour une réponse « private », le contexte d'autorisation; une réponse « private » n'est servie qu'à ce même contexte ». Le tableau 17, p. 57, dit plutôt : « un cache « private » n'est jamais partagé entre jetons ».
- **Diagnostic** :
  - Deux définitions s'opposent : clé par jeton, ou clé par « contexte d'autorisation », expression qui n'apparaît nulle part ailleurs dans le document. Une clé par jeton rend le cache inutile avec des jetons courts. Une clé par sujet mélange des jetons de portées différentes (élévation progressive, EXIG-MCP-10, p. 61).
  - Aucune règle ne purge le cache à la révocation, à la suspension d'un agent ou à la fin d'une élévation.
  - Rien ne fixe le comportement face à une réponse sans `ttlMs` ni `cacheScope` (serveurs antérieurs en coexistence, EXIG-MCP-22).
- **Contre-exemple** : un agent obtient par élévation progressive la portée `crm.dossiers.lire` et lit une ressource « private » (`ttlMs` de 10 min). La portée est retirée ou l'agent est suspendu. Pendant 10 min, une requête du même sujet et du même client reçoit encore le contenu depuis le cache. Les contrôles d'accès par primitive ne s'exercent pas, puisque l'appel ne joint pas le serveur.
- **Correctif proposé** : définir le contexte d'autorisation (au minimum sujet, client, audience et ensemble exact de portées). Exiger l'invalidation sur révocation, suspension et changement de portées, et l'évaluation de la politique avant tout service depuis le cache. Par défaut, ne rien mettre en cache en l'absence de `cacheScope`. Aligner le tableau 17 sur la définition retenue.
- **Confiance** : vérifié dans le texte (définitions divergentes; aucune règle d'invalidation dans full.txt); scénario déduit.

### [06-05] [MAJEUR] La relance MRTR n'est pas articulée à l'approbation à usage unique, à l'idempotence ni au décompte des budgets
- **Axe** : A
- **Localisation** : tableau 17, p. 57 : « le client relance la requête d'origine avec les réponses et un requestState opaque. MRTR s'applique à tools/call ».
- **Diagnostic** : avec MRTR, un même `tools/call` d'écriture traverse deux fois la passerelle. Le cadre ne dit pas :
  - si le jeton d'approbation, signé et à usage unique (`jti`, § 8.5), est consommé au premier passage, qui s'est soldé par `input_required` sans effet;
  - si la relance garde la même clé d'idempotence (EXIG-ORC-21);
  - si l'enveloppe, décrémentée « à chaque appel d'outil » (EXIG-FIN-04), et le journal d'audit comptent un ou deux appels.
  EXIG-MCP-03 traite le cache de la relance, rien d'autre.
- **Contre-exemple** : un appel P3 approuvé reçoit `InputRequiredResult` (précision demandée). La passerelle a marqué le `jti` comme consommé. La relance est refusée : l'approbation légitime est perdue, et la nouvelle demande d'approbation alimente l'approbation machinale (§ 8.7). À l'inverse, si le `jti` n'est consommé qu'à l'effet, la passerelle doit savoir si le serveur a agi, ce qu'elle ignore.
- **Correctif proposé** : exiger que la relance MRTR porte la même clé d'idempotence et la même empreinte d'arguments. Le `jti` est consommé seulement sur un résultat final non `input_required`, et lié à l'empreinte de la requête d'origine contenue dans le `requestState` (EXIG-MCP-17). Le journal relie les deux passages sous une même opération, comptée une fois au budget.
- **Confiance** : déduit (aucune mention croisée MRTR, approbation ou idempotence dans full.txt).

### [06-06] [MAJEUR] MCP Apps : la revue des gabarits `ui://` à l'homologation ne protège pas d'un changement ultérieur; la CSP est déclarée par le serveur
- **Axe** : B | A
- **Localisation** : EXIG-MCP-04, p. 58 : « chaque gabarit ui:// est revu avant l'homologation, servi sous une politique de sécurité du contenu restrictive ». Voir aussi p. 58 : « _meta.ui.csp et _meta.ui.permissions encadrent les origines et les permissions ».
- **Diagnostic** : le gabarit est une ressource lue dynamiquement. EXIG-MCP-20 (p. 64) épingle l'empreinte de la définition d'outil, donc l'URI `_meta.ui.resourceUri`, mais pas le contenu HTML servi à cette URI : il y a un écart entre le moment du contrôle et celui de l'usage (TOCTOU). La CSP et les permissions viennent du `_meta` du serveur, alors qu'EXIG-MCP-14 et EXIG-MCP-16 posent que le `_meta` déclaré ne fonde aucune décision de sécurité.
- **Contre-exemple** : après homologation, un serveur compromis sert sous le même `ui://facture/vue` un HTML qui exfiltre par `postMessage` les données affichées, et élargit `_meta.ui.csp` à un domaine externe. L'empreinte de l'outil est inchangée, donc rien ne se déclenche.
- **Correctif proposé** : épingler au catalogue l'empreinte du contenu de chaque gabarit `ui://` et la vérifier à chaque `resources/read`. Imposer, côté hôte, la CSP et les permissions du catalogue, jamais celles du `_meta`.
- **Confiance** : déduit.

### [06-07] [MAJEUR] Serveur MCP local en Streamable HTTP sur un poste de développement : combinaison non couverte
- **Axe** : A
- **Localisation** : EXIG-MCP-08, p. 60 : « Le transport stdio n'est permis que sur le poste d'un développeur ». EXIG-MCP-09, p. 60 : « Tout serveur MCP accessible ailleurs que sur un poste de développement DOIT exiger une autorisation ». Voir aussi p. 59 : « un serveur local devrait n'écouter que sur 127.0.0.1 ».
- **Diagnostic** : EXIG-MCP-08 encadre stdio sur le poste et HTTP en environnement serveur. Le cas d'un serveur HTTP local sur le poste (fréquent : inspecteurs, serveurs SDK) n'est ni permis ni interdit, et EXIG-MCP-09 l'exempte d'autorisation. La validation d'`Origin` et l'écoute sur la boucle locale restent des « devrait » de la spécification, sans exigence du cadre.
- **Contre-exemple** : un développeur lance un serveur ERP de test sur `0.0.0.0:3000`, sans authentification. Une page Web malveillante l'atteint par rebinding DNS, ou un collègue l'atteint par le réseau local, et invoque ses outils avec les identifiants de préproduction du développeur.
- **Correctif proposé** : soit interdire le transport HTTP sur le poste hors passerelle, soit l'encadrer : écoute sur 127.0.0.1 seulement, validation d'`Origin` obligatoire, authentification même locale, serveur installé depuis le catalogue.
- **Confiance** : déduit.

### [06-08] [MAJEUR] « Aucun miroir CRUD » face aux « adaptateurs déclaratifs » OpenAPI : exigence difficilement conciliable et invérifiable
- **Axe** : C | B
- **Localisation** : EXIG-MCP-06, p. 59 : « NE DOIT PAS exposer une API en recopiant une à une ses opérations élémentaires ». Comparer avec le tableau 16, p. 52 (« Contrat OpenAPI exposé en outils MCP par un adaptateur ») et la p. 59 (« des adaptateurs déclaratifs traduisent les opérations OpenAPI pertinentes en outils orientés tâche »).
- **Diagnostic** : un adaptateur déclaratif fait correspondre des opérations à des outils, ce qui revient presque toujours à un rapport un pour un. L'outil exemplaire (« valide en une seule opération le fournisseur, le centre de coûts et les lignes », p. 58) suppose une composition de plusieurs appels, donc de la logique, donc un service, et plus un adaptateur déclaratif. Sans critère, la frontière entre « miroir » et « tâche » est invérifiable en revue : à partir de combien d'opérations recopiées y a-t-il miroir?
- **Contre-exemple** : un adaptateur expose `get_fournisseur`, `get_centre_cout` et `create_bon` à partir de trois opérations OpenAPI. Il est conforme à la ligne du tableau 16 et à la p. 59, et non conforme à EXIG-MCP-06. Deux réviseurs concluront différemment.
- **Correctif proposé** : donner un critère vérifiable (p. ex. aucun outil d'écriture dont le contrat est une opération unique de l'API sans validation métier; ratio d'outils par intention métier). Reconnaître que l'outil orienté tâche exige un adaptateur de composition, et non une simple traduction déclarative, et le dire au tableau 16.
- **Confiance** : déduit.

### [06-09] [MAJEUR] L'ordre des quatre questions de choix contredit EXIG-INT-11
- **Axe** : A
- **Localisation** : § 6.4, p. 53 : « quatre questions, posées dans l'ordre, mènent au bon choix » et « 2. La cible est-elle un outil ou une donnée aux entrées et aux sorties définies? Si oui, MCP. »
- **Diagnostic** : les questions ne s'excluent pas mutuellement, et la première réponse positive l'emporte. Un changement d'état qui intéresse plusieurs consommateurs dont chacun est un système aux entrées et sorties définies reçoit la réponse « MCP » à la question 2, et la question 4 (événement) n'est jamais atteinte. Or EXIG-INT-11 recommande justement l'événement dans ce cas. La question 3, « si oui, A2A », court-circuite de même la question 4 pour une diffusion vers des agents.
- **Contre-exemple** : un agent de commande doit signaler « commande confirmée » à la facturation, à l'entrepôt et au CRM, trois cibles aux contrats définis. L'algorithme donne trois appels MCP; EXIG-INT-11 demande un événement.
- **Correctif proposé** : placer la question sur la multiplicité des consommateurs et le découplage avant les questions 2 et 3, ou indiquer que les questions qualifient chaque liaison et non un choix exclusif.
- **Confiance** : déduit.

### [06-10] [MAJEUR] Validation d'`iss` : DOIT inapplicable face à un serveur d'autorisation tiers qui n'émet pas `iss`
- **Axe** : A
- **Localisation** : EXIG-MCP-09, p. 60 : « valider iss (RFC 9207) avant d'échanger le code d'autorisation ». Le paragraphe précédent dit, lui : « que le client doit valider s'il est présent ».
- **Diagnostic** : l'exigence est absolue pour les clients de l'entreprise, mais seuls les serveurs d'autorisation de l'entreprise sont tenus d'émettre `iss`. Face à un serveur tiers (EXIG-MCP-12 vise des serveurs tiers) qui n'émet pas `iss` et ne l'annonce pas, le client ne peut ni valider ni savoir s'il doit refuser. Si on lit la règle comme « valider s'il est présent », la protection contre la confusion entre serveurs d'autorisation (mix-up) disparaît sans mesure de remplacement, alors qu'un client MCP parle par construction à plusieurs serveurs d'autorisation.
- **Contre-exemple** : un client d'entreprise relié à un serveur MCP SaaS dont le serveur d'autorisation ne prend pas en charge RFC 9207. Soit l'intégration est impossible, sans que le texte dise que c'est voulu, soit elle tourne sans défense contre le mix-up.
- **Correctif proposé** : écrire « valider `iss` s'il est présent, refuser s'il est absent alors qu'il est annoncé ». À défaut d'`iss`, exiger la contre-mesure de la RFC 9700 : une `redirect_uri` distincte par serveur d'autorisation et la vérification de l'émetteur attendu par session. Ou bien interdire explicitement les serveurs d'autorisation tiers sans RFC 9207.
- **Confiance** : déduit.

### [06-11] [MAJEUR] Agent vers interface utilisateur : la seule voie de production n'a aucun statut au catalogue
- **Axe** : C | A
- **Localisation** : catalogue, p. 51 (AG-UI, Évaluer) : « Pilotes; à défaut, flux SSE structuré produit par l'orchestrateur. » Tableau 16, p. 53 : « AG-UI (Évaluer) ou flux SSE structuré ». EXIG-INT-06, p. 51 : « DOIT figurer au catalogue avec le statut Adopter pour être employé en production ».
- **Diagnostic** : AG-UI, au statut Évaluer, est exclu de la production. Le « flux SSE structuré » de repli n'est pas une entrée du catalogue et n'a donc aucun statut. Pris littéralement, il s'agit d'un format propre, qui relèverait de « Contenir », statut qui interdit tout nouvel usage. Aucune interaction agent vers interface ne peut alors entrer en production conformément à EXIG-INT-06.
- **Contre-exemple** : une équipe livre en production un assistant interactif sur un flux SSE dont les événements sont définis par l'orchestrateur. Le réviseur ne trouve aucune entrée Adopter qui le couvre.
- **Correctif proposé** : inscrire au catalogue le flux SSE structuré (schéma d'événements d'entreprise versionné, p. ex. décrit en AsyncAPI) au statut Adopter, comme contrat interne, ou indiquer qu'il relève d'un contrat d'entreprise exempt d'EXIG-INT-06.
- **Confiance** : vérifié dans le texte (absence d'entrée); qualification « Contenir » déduite.

### [06-12] [MINEUR] Interrogation prescrite pour MCP Tasks, interdite pour le suivi courant en A2A
- **Axe** : C
- **Localisation** : tableau 16, p. 52, ligne MCP Tasks : « Asynchrone, par interrogation ». Voir aussi la p. 53, question 3 : « au-delà de 5 secondes … la diffusion en continu ou les notifications push s'imposent », et EXIG-A2A-07, p. 67 (« NE DOIVENT PAS servir au suivi courant », car « une boucle d'interrogation consomme sans rien apprendre »).
- **Diagnostic** : le même argument d'économie, appliqué à A2A, condamne le mode qui est le seul prévu pour les tâches MCP longues. Le cadre ne justifie pas l'écart et ne fixe pour MCP ni seuil ni intervalle d'interrogation minimal.
- **Contre-exemple** : mille tâches MCP actives interrogées chaque seconde par un orchestrateur saturent la passerelle, alors que le même travail en A2A serait refusé en revue.
- **Correctif proposé** : reconnaître que l'extension Tasks est fondée sur l'interrogation. Imposer de respecter l'intervalle annoncé par le serveur et un plancher, et borner le nombre de tâches interrogées par mandant (en lien avec le quota d'EXIG-MCP-04).
- **Confiance** : vérifié dans le texte.

### [06-13] [MINEUR] Tâche MCP : fenêtre de panne entre la création et la consignation du `taskId`
- **Axe** : A
- **Localisation** : p. 58 : « celui-ci consigne le taskId dans son point de contrôle pour reprendre le suivi après une panne (section 7.4) ».
- **Diagnostic** : si l'orchestrateur tombe après l'envoi de la requête qui crée la tâche, mais avant d'avoir consigné le `taskId`, la reprise relance la création. EXIG-ORC-21 impose une clé d'idempotence aux écritures P2 et P3 seulement. Rien n'oblige le serveur à renvoyer le même `taskId` pour une clé répétée, plutôt qu'une erreur de doublon.
- **Contre-exemple** : une extraction P1 de longue durée est créée deux fois après une panne. La tâche orpheline consomme le quota de tâches actives du mandant (EXIG-MCP-04) jusqu'à expiration de sa durée de vie.
- **Correctif proposé** : exiger une clé d'idempotence à toute création de tâche, quel que soit le palier, et la déduplication par le serveur avec renvoi du `taskId` existant.
- **Confiance** : déduit.

### [06-14] [MINEUR] « Plus de sessions persistantes » : faux pendant la coexistence des deux générations
- **Axe** : B
- **Localisation** : tableau 17, p. 57 : « Plus de répartiteurs de charge à sessions persistantes (sticky sessions) ni de magasin de sessions partagé ».
- **Diagnostic** : EXIG-MCP-22 (p. 65) fait accepter les deux générations par la passerelle jusqu'au 28 juillet 2027. Pour joindre un serveur antérieur, il faut une poignée de main `initialize` et une affinité `Mcp-Session-Id`. La passerelle garde donc, pendant au moins neuf mois, l'état de session que le tableau dit disparu.
- **Contre-exemple** : la passerelle, déployée sans affinité sur la foi du tableau 17, répartit les requêtes d'une session antérieure entre deux nœuds. Le second ne connaît pas la session et l'appel échoue.
- **Correctif proposé** : écrire « à terme, après la migration (EXIG-MCP-22) » et exiger, pendant la coexistence, un magasin de sessions ou une affinité limités aux serveurs antérieurs inscrits.
- **Confiance** : déduit.

### [06-15] [MINEUR] EXIG-MCP-02 : vérification par `server/discover` impossible pour les serveurs antérieurs; date d'« approbation du cadre » non fixée
- **Axe** : C | B
- **Localisation** : EXIG-MCP-02, p. 55 : « La révision prise en charge par chaque serveur est inscrite et épinglée au catalogue; la passerelle la vérifie par server/discover ».
- **Diagnostic** :
  - La première phrase ne vise que les serveurs « mis en production après l'approbation du cadre », mais la seconde s'applique à « chaque serveur ». Un serveur antérieur, toléré par EXIG-MCP-22, n'implémente pas `server/discover`; la p. 66 prévoit pour lui la réponse à `initialize`, ce qu'EXIG-MCP-02 ne dit pas.
  - La date d'« approbation du cadre » n'est pas définie : version 1.1, approbation par le comité?
  - La vérification ne se fait qu'« à chaque déploiement », moment que l'entreprise ignore pour un serveur SaaS tiers.
- **Contre-exemple** : à l'homologation d'un serveur 2025-11-25 inscrit avec une date de migration, la passerelle appelle `server/discover`, reçoit une erreur et, par application littérale, refuse le serveur.
- **Correctif proposé** : restreindre la seconde phrase aux serveurs 2026-07-28 et renvoyer, pour les autres, à l'étape 1 de la migration (p. 66). Dater l'approbation. Pour les serveurs tiers, remplacer « à chaque déploiement » par une vérification périodique, au plus tard à l'échéance de `ttlMs`.
- **Confiance** : vérifié dans le texte.

### [06-16] [MINEUR] Préfixage des noms d'outils par la passerelle : longueur, séparateur et double préfixe non réglés
- **Axe** : A | C
- **Localisation** : p. 55 : « elle préfixe les noms d'outils par un identifiant de serveur ». EXIG-MCP-07, p. 59 : « porter un nom de 1 à 128 caractères ASCII (lettres, chiffres, _, -, .) préfixé par leur domaine ».
- **Diagnostic** :
  - Un nom valide de 128 caractères dépasse la limite une fois préfixé par la passerelle.
  - Le séparateur appartient forcément au jeu permis (`_`, `-`, `.`), si bien que le découpage est ambigu lorsque l'identifiant de serveur contient le même caractère.
  - Le nom se retrouve doublement préfixé (serveur, puis domaine).
  - Le texte ne dit pas sous quel nom, d'origine ou réécrit, le catalogue indexe le palier (EXIG-MCP-14) et l'empreinte (EXIG-MCP-20), ni comment `Mcp-Name` est réécrit sans rompre la concordance d'EXIG-MCP-15.
- **Contre-exemple** : avec les serveurs `crm` et `crm_b`, l'outil `crm_b_lister` agrégé est routé de façon ambiguë.
- **Correctif proposé** : réserver une longueur maximale au nom côté serveur (p. ex. 96 caractères), fixer un séparateur interdit dans les identifiants de serveur, indexer le catalogue sur le couple (serveur, nom d'origine) et préciser que la passerelle réécrit corps et en-tête de façon cohérente.
- **Confiance** : déduit.

### [06-17] [MINEUR] « Un client par serveur, connexion dédiée » : formulation périmée face au protocole sans état et à l'agrégation
- **Axe** : C
- **Localisation** : p. 55 : « Il crée un client MCP pour chaque serveur, et chaque client entretient une connexion dédiée ». La figure 7, p. 56, dit : « Un client par serveur ».
- **Diagnostic** : en 2026-07-28, chaque requête est autonome et sans session (p. 56-57), si bien que « connexion dédiée » ne décrit plus rien d'observable. Avec l'agrégation (p. 55), l'hôte n'a qu'un client pour le point d'accès virtuel, qui couvre plusieurs serveurs.
- **Correctif proposé** : écrire « un client par point d'accès MCP (serveur, ou point d'accès virtuel de la passerelle) » et retirer « connexion dédiée », ou la limiter à stdio et aux serveurs antérieurs.
- **Confiance** : déduit (la page d'architecture officielle peut conserver la formule : à vérifier).

### [06-18] [MINEUR] L'identifiant de révision « dernier changement incompatible » ne concorde pas avec la chronologie donnée
- **Axe** : C
- **Localisation** : p. 54 : « l'identifiant AAAA-MM-JJ correspond au dernier changement incompatible » et « après une version candidate verrouillée le 21 mai 2026 et dix semaines de validation ».
- **Diagnostic** : si la version candidate est verrouillée le 21 mai, le dernier changement incompatible lui est antérieur, et pourtant l'identifiant est la date de publication (28 juillet). Soit la règle de versionnage énoncée est inexacte, soit des changements incompatibles sont survenus après le verrouillage. H.2 (p. 279) tire de cette règle une conséquence normative : la révision de mars 2027 déclencherait la révision extraordinaire d'EXIG-GOV-18.
- **Correctif proposé** : formuler « l'identifiant est la date de publication d'une révision qui contient au moins un changement incompatible », si c'est l'usage constaté.
- **Confiance** : à vérifier (source externe : page « Versioning » de la spécification MCP).

### [06-19] [MINEUR] « Identifiant de requête non nul » présenté comme une nouveauté de 2026-07-28
- **Axe** : A
- **Localisation** : p. 55 : « En 2026-07-28, l'identifiant d'une requête ne peut pas être nul ».
- **Diagnostic** : d'après mes connaissances, cette contrainte (« MUST NOT be null », contrairement au JSON-RPC de base) figure déjà dans la révision 2024-11-05. La tournure laisse croire qu'il s'agit d'un changement.
- **Correctif proposé** : écrire « Comme depuis 2024-11-05, l'identifiant ne peut pas être nul; en 2026-07-28, tout résultat porte en outre `resultType` ».
- **Confiance** : à vérifier (source externe : section « Messages » de la révision 2024-11-05). J'en suis raisonnablement sûr.

### [06-20] [MINEUR] Règle de cycle de vie (au moins 12 mois) face aux retraits immédiats de 2026-07-28
- **Axe** : C | A
- **Localisation** : tableau 17, p. 57 : « une fonctionnalité dépréciée reste dans la spécification au moins douze mois ». Sur la même page : « ping, logging/setLevel et notifications/roots/list_changed sont retirés ».
- **Diagnostic** : le tableau ne dit pas si ces trois éléments étaient dépréciés depuis au moins 12 mois, ni si la règle de la SEP-2596 s'applique avant sa propre adoption. `logging/setLevel` est retiré alors que la journalisation protocolaire n'est que dépréciée : un mécanisme maintenu perd sa commande. Le lecteur ne peut pas juger si un retrait sans préavis peut se reproduire, alors que la règle sert de base à l'échéance d'EXIG-MCP-22.
- **Correctif proposé** : préciser le fondement de ces retraits (conséquence du passage sans état, hors règle de cycle de vie) et l'effet du retrait de `setLevel` sur la journalisation dépréciée.
- **Confiance** : à vérifier (source externe : journal des modifications 2026-07-28 et registre des dépréciations).

### [06-21] [MINEUR] Abonnements sans reprise : aucune obligation de resynchronisation après coupure
- **Axe** : B
- **Localisation** : tableau 17, p. 57 : « la reprise de flux par Last-Event-ID est retirée ».
- **Diagnostic** : une notification `list_changed` perdue pendant une coupure laisse la passerelle avec une liste d'outils et un cache périmés. Le recalcul des empreintes à chaque `tools/list` (EXIG-MCP-20) ne se produit alors pas. Le cadre ne prescrit aucune relecture complète à la reconnexion.
- **Correctif proposé** : à chaque rétablissement de `subscriptions/listen`, exiger l'invalidation des entrées de cache du serveur et une nouvelle lecture des listes.
- **Confiance** : déduit.

### [06-22] [MINEUR] L'ordre déterministe est exigé des serveurs, pas de la liste agrégée et filtrée par la passerelle
- **Axe** : A
- **Localisation** : EXIG-MCP-03, p. 58 : « Les serveurs MCP internes DOIVENT renvoyer leurs outils dans un ordre déterministe ».
- **Diagnostic** : l'hôte reçoit la liste fusionnée et filtrée selon les portées (figure 7). L'effet recherché sur le cache d'invites (EXIG-FIN-07) dépend de l'ordre de cette liste-là. Une fusion non déterministe, ou des serveurs tiers sans ordre stable, annulent le bénéfice.
- **Correctif proposé** : étendre l'exigence à la passerelle : fusion par identifiant de serveur, puis par nom, et ordre stable après filtrage.
- **Confiance** : déduit.

### [06-23] [MINEUR] EXIG-MCP-07 : `structuredContent` exigé sans condition, y compris sur une erreur; double sérialisation coûteuse
- **Axe** : A | B
- **Localisation** : EXIG-MCP-07, p. 59 : « renvoyer un structuredContent conforme, accompagné du même JSON sérialisé dans un bloc texte ».
- **Diagnostic** : une erreur métier renvoyée avec `isError: true` ne peut en général pas se conformer à l'`outputSchema` d'un succès, et l'exigence ne prévoit pas ce cas. La copie texte double le volume de résultat si l'hôte transmet les deux au modèle, ce qui contredit la logique d'économie de contexte d'EXIG-MCP-06 et des p. 58-59.
- **Correctif proposé** : exempter les résultats `isError` de la conformité, ou exiger un schéma d'erreur. Recommander à l'hôte de ne transmettre au modèle qu'une des deux formes.
- **Confiance** : déduit.

### [06-24] [MINEUR] « Détournement DNS » au lieu de « rebinding DNS »
- **Axe** : A
- **Localisation** : p. 59 : « valider l'en-tête Origin sur toute connexion entrante pour contrer le détournement DNS ».
- **Diagnostic** : la validation d'`Origin` vise le DNS rebinding (rattachement d'un nom contrôlé par l'attaquant à une adresse locale), pas le détournement (hijacking) de résolution. Les deux menaces appellent des contre-mesures différentes.
- **Correctif proposé** : « contrer les attaques par rebinding DNS (réassociation DNS) ».
- **Confiance** : vérifié dans le texte; terme de la spécification (« DNS rebinding ») d'après mes connaissances.

### [06-25] [MINEUR] Formulation TLS ambiguë dans un DOIT, et divergente de la règle A2A
- **Axe** : C
- **Localisation** : EXIG-MCP-08, p. 60 : « DOIT être exposé par Streamable HTTP, chiffré par TLS 1.3 (TLS 1.2 toléré comme plancher, versions antérieures désactivées) ».
- **Diagnostic** : un serveur limité à TLS 1.2 est-il conforme? Le DOIT dit 1.3, la parenthèse dit 1.2. EXIG-A2A (p. 68) écrit plutôt « TLS 1.3 par défaut, TLS 1.2 étant le plancher toléré ». Le test d'homologation ne peut pas trancher.
- **Correctif proposé** : « DOIT négocier TLS 1.3 lorsque le pair le permet; TLS 1.2 est le minimum; les versions antérieures DOIVENT être désactivées », et la même formule pour A2A.
- **Confiance** : vérifié dans le texte.

### [06-26] [MINEUR] Parenthèse dupliquée
- **Axe** : C
- **Localisation** : p. 60 : « (la version −16 est la plus récente au 27 octobre 2026; voir la section 6.3) », répétée mot pour mot deux fois dans la même phrase.
- **Correctif proposé** : supprimer la seconde occurrence.
- **Confiance** : vérifié dans le texte.

### [06-27] [MINEUR] « La finalisation de DPoP » : formulation trompeuse
- **Axe** : A | C
- **Localisation** : p. 60 : « la finalisation de DPoP ne figure qu'à sa feuille de route ».
- **Diagnostic** : DPoP est une RFC publiée (RFC 9449, citée deux lignes plus bas). Ce qui figure à la feuille de route de MCP, c'est son intégration au profil d'autorisation.
- **Correctif proposé** : « l'intégration de DPoP (RFC 9449) au profil d'autorisation MCP ne figure qu'à sa feuille de route ».
- **Confiance** : vérifié dans le texte.

### [06-28] [MINEUR] « Émetteur » désigne tantôt l'expéditeur (sender), tantôt l'émetteur (issuer)
- **Axe** : C
- **Localisation** : p. 60 : « Les jetons contraints à l'émetteur (RFC 9449 ou RFC 8705) ». Comparer avec la p. 61 (« lié à l'émetteur qui l'a délivré : si l'émetteur change », où il s'agit de l'issuer) et le § 9.3 (« Jetons liés à l'expéditeur », lignes 7938 et 15040 de full.txt).
- **Diagnostic** : les jetons « sender-constrained » sont liés au détenteur qui les présente, pas à leur émetteur. Le même mot, à quelques lignes d'écart, nomme deux rôles OAuth opposés, et le chapitre 9 emploie un autre terme.
- **Correctif proposé** : uniformiser en « jetons liés à l'expéditeur » ; réserver « émetteur » à `iss`. La même correction s'impose à la ligne 13628 de full.txt.
- **Confiance** : vérifié dans le texte.

### [06-29] [MINEUR] Chiffre de 85 % nuancé au § 6.5, repris sans nuance au § 7.3
- **Axe** : C
- **Localisation** : p. 59 : « elle chiffre cette réduction à 85 % (les deux chiffres donnent plutôt près de 89 %) ». Au § 7.3, p. 92 : « sa recherche d'outils réduit de 85 % la consommation de jetons de contexte ».
- **Diagnostic** : le calcul de la p. 59 est exact ((77 000 − 8 700) / 77 000 ≈ 88,7 %), mais le § 7.3 reprend 85 % sans réserve. Le même chiffre est donc présenté de deux façons.
- **Correctif proposé** : harmoniser, soit par la même parenthèse, soit par un renvoi au § 6.5.
- **Confiance** : vérifié dans le texte.

### [06-30] [MINEUR] EXIG-MCP-05 : les ressources sont pilotées par l'application, pas par le modèle
- **Axe** : B
- **Localisation** : EXIG-MCP-05, p. 59 : « La lecture d'une entité connue DEVRAIT être exposée comme ressource adressée par URI ».
- **Diagnostic** : dans MCP, les ressources sont conçues pour être choisies par l'application hôte, alors que les outils sont contrôlés par le modèle. Un agent qui doit décider seul de lire une entité dépend d'un hôte qui expose les ressources au modèle, ce que beaucoup ne font pas. Le compromis, gain de cache contre perte d'autonomie, n'est pas justifié.
- **Correctif proposé** : conditionner la recommandation à un hôte qui offre au modèle la lecture de ressources, ou admettre un outil de lecture adossé à la ressource.
- **Confiance** : à vérifier (section « Resources » de la spécification, formulation « application-driven »).

### [06-31] [MINEUR] EXIG-INT-10 : les lignes du tableau 16 n'ont pas d'identifiant; le rôle des quatre questions est flou
- **Axe** : C | B
- **Localisation** : EXIG-INT-10, p. 53 : « justifié dans la fiche d'agent par renvoi à une ligne du tableau 16 ». Voir aussi la p. 53 : « quatre questions … mènent au bon choix ».
- **Diagnostic** : les lignes ne sont pas numérotées, et un renvoi stable résistera mal aux mises à jour de la matrice qu'EXIG-INT-10 annonce. Les quatre questions semblent dispenser de la matrice, alors qu'EXIG-INT-10 impose de soumettre tout cas absent à l'architecture d'entreprise.
- **Correctif proposé** : numéroter les lignes (M1 à M8) et préciser que les quatre questions ne servent qu'à préparer la soumission.
- **Confiance** : vérifié dans le texte.

### [06-32] [MINEUR] Figure 7 : EMA présentée parmi les extensions du serveur de référence alors qu'elle est au statut Évaluer
- **Axe** : C
- **Localisation** : figure 7, p. 56 : « Extensions (activation explicite) : tasks · apps · auth (EMA) ». Comparer avec le catalogue, p. 49-50, et la p. 62 : « elle figure au statut « Évaluer » du catalogue ».
- **Diagnostic** : la figure décrit l'architecture de production. EXIG-INT-06 limite EMA aux pilotes.
- **Correctif proposé** : annoter « EMA : pilotes seulement (Évaluer) » dans la figure.
- **Confiance** : vérifié dans le texte.

### [06-33] [MINEUR] Stade de l'extension Tasks non indiqué, contrairement à ce qu'exige EXIG-INT-09 (signalé en H.2)
- **Axe** : C
- **Localisation** : p. 52 : « MCP avec l'extension officielle Tasks ». La p. 62 précise pour les extensions d'autorisation : « stables depuis la révision 2026-07-28 ».
- **Diagnostic** : le cadre donne le stade des extensions d'autorisation, mais pas celui de Tasks, qui est Beta d'après H.2 (p. 279). EXIG-INT-09 demande le « statut exact » au catalogue. La lacune est signalée en H.2, pas parmi les errata de H.4.
- **Correctif proposé** : mentionner « Tasks (Beta) » au tableau 16 et au catalogue.
- **Confiance** : vérifié dans le texte.

### [06-34] [MINEUR] Déjà consigné en H.4 : date de la prochaine révision MCP et échéance du retrait de HTTP+SSE
- **Axe** : C
- **Localisation** : p. 54 : « La feuille de route publiée le 22 août 2026 n'annonce aucune date pour la prochaine révision » (H.4, no 3). Tableau 17, p. 57 : « trois mois après que la SEP-2596 atteint l'état final » (H.4, précisions hors errata).
- **Diagnostic** : déjà consigné en H.4. La SEP-2596 est finale depuis le 3 juin 2026, et l'échéance était donc calculable au 27 octobre.
- **Correctif proposé** : appliquer le traitement de H.4 et de H.2.
- **Confiance** : vérifié dans le texte.

## Points forts
- Le texte distingue systématiquement l'exigence de la spécification et le choix du cadre (EXIG-MCP-04, 08 et 09, ainsi que les p. 60 et 62), et nuance ses chiffres (89 % contre 85 %, données « selon les responsables »).
- Le tableau 17 fait une lecture opérationnelle exacte du passage sans état (risque déplacé des sessions vers `requestState` et les en-têtes), avec un renvoi aux exigences correspondantes.
- La défiance envers les annotations et le `_meta` déclarés (EXIG-MCP-02, Pourquoi; EXIG-MCP-14) est cohérente avec PRIN-07.

## Questions pour l'audit bibliographique
- p. 54 : la date d'annonce de MCP (25 novembre 2024), le don à l'AAIF le 9 décembre 2025 et la liste des membres platine au lancement [4, 20, 193].
- p. 54 : les chiffres « environ 10 000 serveurs actifs » et « plus de 97 millions de téléchargements mensuels » [14] (déclarés par le projet, sans mesure indépendante).
- p. 54 : depuis 2026-07-28, une SEP prend-elle la forme d'une demande de tirage, et une extension exige-t-elle une implémentation de référence dans un SDK officiel [168, 169]?
- p. 54 : version candidate verrouillée le 21 mai 2026; prise en charge par les SDK TypeScript, Python, Go et C# à la sortie, Rust en bêta [33, 194]; règle « AAAA-MM-JJ = dernier changement incompatible » (voir 06-18).
- p. 54 : registre MCP lancé en préversion le 8 septembre 2025 et toujours en préversion, sans prise en charge des serveurs privés [25, 43].
- p. 55 : l'identifiant non nul est-il nouveau en 2026-07-28 ou acquis depuis 2024-11-05 (voir 06-19)? Champ `resultType` [162].
- p. 57 : numéros de SEP (2567, 2575, 2243, 2322, 2549, 2663, 2106, 2596) et codes −32020, −32021, −32022; passage de « ressource introuvable » de −32002 à −32602 [162, 168, 190].
- p. 57 : fondement des retraits immédiats de `ping`, `logging/setLevel` et `notifications/roots/list_changed` face à la règle des 12 mois (voir 06-20).
- p. 58 : méthodes et états de l'extension Tasks (`tasks/get`, `tasks/update`, `tasks/cancel`; working, input_required, completed, failed, cancelled) [191]; clés `_meta.ui.*` de MCP Apps [202].
- p. 58 : affirmation d'Akamai sur le déni de service par tâches asynchrones et le XSS stocké par les interfaces générées [203].
- p. 58 : règle des préfixes réservés (« deuxième libellé » `modelcontextprotocol` ou `mcp`) [169].
- p. 59 : seuil « de l'ordre de 1 à 5 % de la fenêtre de contexte » des bonnes pratiques MCP [204]; chiffres de 77 000, 8 700 et 72 000 jetons et base de calcul des 85 % [205].
- p. 59 : HTTP 403 sur un `Origin` invalide et terme « DNS rebinding » [190].
- p. 60 : citation par MCP 2026-07-28 du brouillon OAuth 2.1 −13; `iss` (RFC 9207) « devrait » côté serveur d'autorisation et rejet s'il est absent alors qu'il est annoncé [209, 212].
- p. 61 : CIMD −02 (limite d'environ 5 Ko, interdiction du secret partagé) et référence −00 dans MCP [216]; dépréciation du DCR en 2026-07-28 [168, 215].
- p. 62 : EMA (ID-JAG par RFC 8693, puis RFC 7523) et extension OAuth Client Credentials « stables depuis 2026-07-28 » [217, 218]; valeurs par défaut des annotations et formulation « should never » [197, 201].
