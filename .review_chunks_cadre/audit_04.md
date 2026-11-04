# Audit chunk_04 — pages 31-42

## Synthèse
Le chunk couvre la page de partie II et le chapitre 5 (§ 5.1 à 5.4, début de 5.5) : règle centrale, six couches, EXIG-ARC-01 à ARC-21, plans transversaux (tableau 11), blocs ABB/SBB (tableau 12), début de la mémoire. La rédaction est dense, sourcée, prudente sur les chiffres de fournisseurs. Les trois défauts les plus graves : (1) les plateformes SaaS à agents intégrés, proposées en SBB, ne peuvent pas satisfaire EXIG-ARC-08/01/11 et aucune voie de dérogation n'est prévue ([04-03]); (2) la passerelle d'agents, rendue obligatoire et fermée par défaut, n'a aucune exigence de disponibilité, et sa panne bloque aussi les compensations ([04-04]); (3) la portée de la règle centrale varie d'un énoncé à l'autre (« hors de son domaine » ou tout appel MCP) ([04-01]).

## Constats

### [04-01] [MAJEUR] Portée de la règle centrale : quatre formulations incompatibles
- **Axe** : C (et A)
- **Localisation** : § 5 intro p. 32 : « aucun agent n'atteint un outil, une donnée ou un autre agent hors de son domaine sans passer par la passerelle »; figure 3 : « un agent n'atteint jamais un système ou un outil hors domaine »; EXIG-ARC-01 p. 33 : « tout appel d'un agent vers un outil, une ressource ou une invite MCP, vers une donnée d'un autre domaine ou vers un autre agent DOIT transiter »; EXIG-ARC-11 p. 36 : « pour le trafic interdomaine comme pour celui qui entre dans l'entreprise ou qui en sort ».
- **Diagnostic** : l'introduction et la figure limitent la règle au trafic hors domaine. ARC-01 l'étend à tout appel MCP, intradomaine compris. ARC-11 énumère le trafic interdomaine, entrant et sortant, sans nommer l'intradomaine. EXIG-IAM-17 (p. 128-129), auquel ARC-01 renvoie, est ambigu par sa syntaxe (« vers un serveur MCP, vers un autre agent ou vers une ressource qui franchit une frontière de domaine ») et confie l'intradomaine au serveur de ressources et au maillage. Comme ARC-01 renvoie à IAM-17 pour une exception, il forme avec lui une définition circulaire du périmètre.
- **Contre-exemple** : un agent appelle un serveur MCP de son propre domaine sans passer par la passerelle, en mTLS de maillage. Selon la figure 3, l'introduction et la dernière phrase d'IAM-17, l'appel est conforme. Selon ARC-01 et EXIG-MCP-01, il ne l'est pas. Deux auditeurs concluent en sens contraires, et l'appel échappe au coupe-circuit et au journal de la passerelle.
- **Correctif proposé** : une seule formulation normative, dans ARC-01, reprise mot pour mot ailleurs. Par exemple : « tout appel MCP ou A2A, intradomaine compris, et tout accès à une donnée d'un autre domaine ». Aligner ensuite la figure 3, l'introduction, ARC-11, IAM-17 et l'encadré À RETENIR de la p. 44.
- **Confiance** : vérifié dans le texte (full.txt, l. 8154-8159).

### [04-02] [MAJEUR] « Environnement serveur » non défini au point d'emploi; postes de travail non couverts
- **Axe** : A
- **Localisation** : EXIG-ARC-01 p. 33 : « Dans tout environnement serveur [...] (seule exception : un serveur MCP local en transport stdio sur un poste de développement, encadré par l'EXIG-MCP-08 ». Voir aussi EXIG-ARC-11, p. 36.
- **Diagnostic** : le terme n'est défini qu'en incise dans EXIG-MCP-08, au § 6.5 (« développement partagé, préproduction, production »). Le cadre reconnaît pourtant des hôtes hors serveur : un « poste de travail » comme hôte MCP (§ 6.5) et un « profil des agents hors maillage : poste de travail, navigateur, mobile, périphérie » (§ 9.3). ARC-01 et ARC-11 ne disent rien de ces hôtes. MCP-01 couvre en partie le cas des appels MCP, mais ni les appels A2A ni l'accès aux données d'un autre domaine depuis un poste.
- **Contre-exemple** : un assistant de bureau sur le poste d'un employé (qui n'est pas un poste de développement) appelle un agent partenaire en A2A. Le cas ne relève ni de l'environnement serveur ni de l'exception stdio : aucune exigence du chapitre 5 n'impose la passerelle.
- **Correctif proposé** : définir le terme au § 5.1 (ou au tableau 7). Remplacer « Dans tout environnement serveur » par « Dans tout environnement autre qu'un poste de développement isolé », et rattacher explicitement les postes de travail, les navigateurs et les appareils mobiles à la règle.
- **Confiance** : vérifié dans le texte (l. 3436, 3740, 7899); l'absence de couverture est déduite.

### [04-03] [BLOQUANT] Plateformes SaaS à agents intégrés : SBB recommandés, mais non conformes à ARC-08, ARC-01, ARC-11 et ARC-03
- **Axe** : A (et B)
- **Localisation** : tableau 12, ligne « Couches 1 à 3 — Plateforme SaaS à agents intégrés » p. 41 (Copilot Studio, Agentforce, ServiceNow); EXIG-ARC-08 p. 35 : « Un agent DOIT n'accéder aux modèles que par cette passerelle, sans détenir de clé de fournisseur de modèles ni appeler un fournisseur directement »; p. 38 : « D'où l'exigence d'un coupe-circuit appliqué à la passerelle, quel que soit l'éditeur ».
- **Diagnostic** : un agent Copilot Studio ou Agentforce appelle les modèles de son éditeur depuis le nuage de celui-ci. Il ne passe pas par la passerelle de modèles de l'entreprise (ARC-08). Ses appels d'outils natifs restent dans la plateforme et n'atteignent pas la passerelle d'agents (ARC-01, ARC-11, coupe-circuit). Sa logique d'agent est configurée dans le canal (ARC-03). EXIG-FIN-03 confirme que le cadre prévoit de tels agents (« Pour tout agent exploité sur une plateforme SaaS »). Or ARC-20 impose de refuser l'homologation tant qu'un ABB nécessaire, ici la passerelle de modèles, n'a pas de SBB. Les exigences sont donc soit inapplicables, soit contradictoires avec le tableau 12 et FIN-03. Aucune dérogation type n'est prévue (Grep « SaaS » à proximité de « passerelle » ou « dérogation » : aucun résultat).
- **Contre-exemple** : l'équipe homologue un agent Copilot Studio inscrit au registre. Appliquées à la lettre, ARC-08 et ARC-20 imposent de le refuser. S'il est accepté, le coupe-circuit « quel que soit l'éditeur » n'a aucune prise sur ses appels d'outils internes à Microsoft.
- **Correctif proposé** : ajouter une exigence propre aux agents SaaS intégrés. Elle énumérerait les contrôles compensatoires (traçage exportable, coupe-circuit natif de l'éditeur testé chaque trimestre, outils d'entreprise exposés seulement par la passerelle, plafonds de l'éditeur selon FIN-03) et imposerait une dérogation type (§ 11.6) pour ARC-08 et ARC-03. Corriger ensuite la phrase de la p. 38.
- **Confiance** : vérifié dans le texte (tableau 12, FIN-03 l. 9818); l'impossibilité technique de router les modèles d'un SaaS par la passerelle de l'entreprise est déduite.

### [04-04] [MAJEUR] La passerelle, point unique de défaillance, n'a aucune exigence de disponibilité
- **Axe** : B
- **Localisation** : EXIG-ARC-01 p. 33 : « un point d'application unique est la condition pour authentifier, autoriser, tracer et couper chaque appel »; EXIG-ARC-11 p. 36 : « réévaluer l'autorisation à chaque appel ».
- **Diagnostic** : ARC-01, ARC-08 et ARC-11 font passer tout le trafic des agents, modèles compris, par deux passerelles. EXIG-IAM-18 les ferme en cas d'échec et ne traite que la panne du plan de contrôle (« dernière politique distribuée »), pas celle du plan de données. Aucune exigence de redondance, d'objectif de disponibilité ni de test de panne n'a été trouvée (Grep « haute disponibilité », « redondan », « point unique de défaillance » : aucune occurrence qui vise la passerelle). Les outils de compensation de la couche 5 passent eux aussi par la passerelle (ARC-01, ARC-12).
- **Scénario de défaillance** : la passerelle d'agents tombe pendant qu'une saga a déjà écrit dans l'ERP. Comme l'échec est fermé, la compensation est refusée. La saga reste à moitié faite jusqu'au retour du service, et tous les agents du parc s'arrêtent en même temps. L'objectif de PRIN-12 (dégradation maîtrisée) n'est pas atteint.
- **Correctif proposé** : ajouter une exigence ARC ou IAM qui fixe un SLO de disponibilité au moins égal à celui des systèmes les plus critiques derrière la passerelle, une redondance active sur plusieurs zones et un exercice de panne chaque trimestre. Elle donnerait aussi une priorité réservée aux compensations (file ou capacité dédiée) et dirait, pour chaque palier, ce qui se dégrade quand le plan de données est indisponible.
- **Confiance** : vérifié dans le texte pour l'absence d'exigence (Grep); le scénario est déduit.

### [04-05] [MAJEUR] « Sans réécriture des services » contre l'idempotence vérifiée par le système visé
- **Axe** : A
- **Localisation** : EXIG-ARC-14 p. 37 : « exposées aux agents par des serveurs MCP ou des adaptateurs placés devant les API en place, sans réécriture des services d'origine »; EXIG-ARC-18 p. 38 : « une référence de trace que le système cible conserve avec l'opération ».
- **Diagnostic** : EXIG-ORC-22 (§ 7.6) permet de vérifier la clé « directement ou par son adaptateur », mais sa justification dit : « seul le système visé sait si l'effet a déjà eu lieu ». Devant une API patrimoniale non idempotente, l'adaptateur ne peut pas savoir si une requête expirée a produit son effet. ARC-14 interdit de modifier le service, et ARC-18 suppose que le système cible conserve une référence qu'il n'a pas de champ pour stocker. Le cas n'a aucune voie conforme.
- **Contre-exemple** : un adaptateur crée un bon de commande dans l'ERP et l'appel expire après 30 s. L'adaptateur ne sait pas si le bon existe. S'il réessaie, il risque un doublon (contraire à ORC-22). S'il ne réessaie pas, la tâche est bloquée. Modifier l'ERP pour qu'il accepte une clé contrevient à ARC-14.
- **Correctif proposé** : changer ARC-14 en « sans réécriture de la logique métier ». Permettre une extension minimale (champ de clé, référence de trace, requête de vérification par clé), ou exiger, pour toute API sans idempotence native, une opération de lecture qui permet de rapprocher l'état avant réessai. À défaut, classer l'outil P3 (approbation humaine à chaque réessai).
- **Confiance** : vérifié dans le texte (ORC-22, l. 6025-6029); le contre-exemple est déduit.

### [04-06] [MAJEUR] Points de contrôle : la provenance vérifiée ne protège pas contre le rejeu d'un état ancien
- **Axe** : A
- **Localisation** : EXIG-ARC-06 p. 35 : « Un orchestrateur DOIT refuser de reprendre une exécution à partir d'un point de contrôle dont la provenance n'est pas vérifiée. »
- **Diagnostic** : ARC-06 et ORC-13 exigent l'intégrité et la provenance, mais pas la fraîcheur. Un point de contrôle authentique mais périmé, par exemple l'état d'avant la consommation d'une approbation ou d'avant une compensation, passe la vérification. Le § 7.4 décrit d'ailleurs le « voyage dans le temps » de LangGraph, qui recharge un point de contrôle antérieur. Rien n'interdit de le faire en production.
- **Contre-exemple** : un opérateur, ou un attaquant qui a accès en écriture au magasin, restaure le point de contrôle signé de l'étape 3, alors que l'étape 5 a déjà compensé l'écriture de l'étape 4. À la reprise, l'étape 4 s'exécute de nouveau. La clé d'idempotence (tâche + étape, ORC-21) est identique : le serveur rejette le doublon s'il a gardé la clé, et l'effet compensé n'est pas refait, ce qui laisse l'état métier incohérent avec le journal de la saga. S'il ne l'a pas gardée, l'effet est refait (voir [04-07]).
- **Correctif proposé** : lier chaque point de contrôle à un numéro de séquence monotone signé, propre à la tâche. Refuser toute reprise depuis un point qui n'est pas le dernier, sauf dans un environnement de rejeu isolé avec doublures, comme le prévoit EXIG-EVT-10 pour les événements.
- **Confiance** : déduit.

### [04-07] [MAJEUR] Durée illimitée des exécutions durables, conservation des clés d'idempotence non bornée
- **Axe** : A (thèse T3)
- **Localisation** : § 5.2, couche 2, p. 34 : « Temporal [...] poursuit une exécution jusqu'à son terme sans limite de temps imposée »; « Les flux Standard d'AWS Step Functions durent jusqu'à un an »; EXIG-ARC-05, attente d'approbation.
- **Diagnostic** : le chapitre retient des moteurs dont les exécutions durent des semaines ou des mois, en attente d'approbation. ORC-21 et ORC-22 exigent une clé d'idempotence vérifiée côté serveur, mais aucune exigence ne fixe combien de temps le service doit la garder (Grep sur la conservation, l'expiration et la fenêtre des clés : aucun résultat). Si le service expire ses clés avant la reprise de la tâche, le réessai produit un double effet.
- **Scénario de défaillance** : une tâche N2 attend une approbation pendant 3 semaines, puis reprend; l'appel P2 d'avant la pause avait expiré sans réponse. Le service visé, comme beaucoup d'API de paiement (à vérifier : la pratique courante est d'environ 24 h), a purgé la clé. Le réessai crée un second paiement.
- **Correctif proposé** : exiger que l'entrée de catalogue d'un outil P2 ou P3 déclare la durée de conservation des clés. L'orchestrateur refuserait de réessayer sans rapprochement quand le délai écoulé dépasse cette durée. Sinon, borner la durée des tâches à effets en suspens.
- **Confiance** : déduit; la durée de conservation chez les fournisseurs est à vérifier.

### [04-08] [MAJEUR] EXIG-ARC-20 : l'ABB « nécessaire » est déclaré par la solution elle-même
- **Axe** : B
- **Localisation** : EXIG-ARC-20 p. 39 : « L'homologation DOIT être refusée tant qu'un ABB de tableau 12 nécessaire à la solution n'a pas de SBB désigné. »
- **Diagnostic** : la solution juge elle-même quels ABB lui sont « nécessaires », alors que le contrôle sert à repérer ce qu'elle omet. L'exemple du « Pourquoi » (« un agent sans passerelle de modèles ») est justement un ABB qu'une équipe peut déclarer non nécessaire. Le contrôle ne vérifie que ce qu'on lui déclare.
- **Contre-exemple** : une équipe soumet un agent N2 en écriture qui ne mentionne ni moteur durable ni passerelle de modèles. Elle les déclare non nécessaires, et ARC-20 est satisfait.
- **Correctif proposé** : ajouter au tableau 12 une colonne « obligatoire si » qui dérive chaque ABB des DOIT (ARC-01, ARC-05 pour toute écriture ou approbation, ARC-08 pour toute inférence, ARC-10 pour tout code généré, ARC-19 pour le plan transversal). Le caractère nécessaire devient alors un critère vérifiable en revue.
- **Confiance** : vérifié dans le texte.

### [04-09] [MAJEUR] Retrait « en une seule opération » contre la dernière politique distribuée
- **Axe** : A (thèse T2)
- **Localisation** : EXIG-ARC-12 p. 36 : « une source unique permet de retirer partout, en une seule opération, un outil compromis ».
- **Diagnostic** : la promesse de retrait immédiat ignore le délai de propagation vers les instances et les caches de la passerelle. EXIG-IAM-18 dit en outre que, si le plan de contrôle est indisponible, la passerelle « continue d'appliquer la dernière politique distribuée ». Pendant une panne du plan de contrôle, un retrait ne peut donc pas se propager. La propagation n'a pas de délai maximal et la politique en cache n'a pas de durée de validité.
- **Scénario de défaillance** : un serveur MCP compromis est retiré du catalogue pendant un incident qui touche aussi le plan de contrôle. Les instances de la passerelle gardent l'ancienne liste d'autorisation, et l'outil reste joignable aussi longtemps que dure la panne.
- **Correctif proposé** : fixer un délai maximal de propagation des retraits, mesuré lors de l'exercice du coupe-circuit. Donner une durée de validité à la politique en cache, après laquelle les appels P2 et P3 sont refusés. Prévoir aussi un coupe-circuit local au plan de données, qui ne dépend pas du plan de contrôle.
- **Confiance** : déduit (IAM-18, l. 8164-8167).

### [04-10] [MINEUR] Step Functions et Temporal : garanties présentées sans leurs limites
- **Axe** : A
- **Localisation** : p. 34 : « Les flux Standard d'AWS Step Functions durent jusqu'à un an avec une sémantique d'exécution exactement une fois, alors que les flux Express [...] sont mieux adaptés aux actions idempotentes ».
- **Diagnostic** : d'après mes connaissances, le « exactement une fois » des flux Standard porte sur l'exécution du flux et ses transitions, pas sur les effets externes des tâches : une tâche configurée avec `Retry` peut répéter son effet. L'opposition suggère que l'idempotence ne concerne que les flux Express. Le paragraphe suivant ne corrige qu'à propos de LangGraph. Pour Temporal, « sans limite de temps » passe sous silence la limite de taille de l'historique, qui impose Continue-As-New pour les exécutions très longues (je le suppose d'après mes connaissances; à vérifier).
- **Correctif proposé** : préciser « exactement une fois au niveau des transitions; les tâches réessayées exigent des effets idempotents (EXIG-ORC-21) ». Mentionner la limite d'historique de Temporal.
- **Confiance** : à vérifier (documentation AWS [104], Temporal [81]).

### [04-11] [MINEUR] Doublons divergents : ARC-05 et ORC-11, ARC-06 et ORC-13
- **Axe** : C (et B)
- **Localisation** : EXIG-ARC-05 p. 34-35 : « Toute tâche qui produit un effet en écriture, attend une approbation humaine ou s'étend sur plus d'un échange »; EXIG-ARC-06 p. 35.
- **Diagnostic** : EXIG-ORC-11 (§ 7.4) fixe la même obligation, mais avec un autre déclencheur (« Tout flux de plus d'une étape, ou susceptible d'attendre une approbation »). Une tâche d'une seule étape en écriture relève d'ARC-05 et pas d'ORC-11. EXIG-ORC-13 ajoute à ARC-06 l'accès réservé à l'identité de l'orchestrateur, ainsi que la conservation et l'élagage. « Échange » n'est pas défini : selon la lecture, un assistant conversationnel N1 de plusieurs tours exige un moteur durable ou en est dispensé. Deux blocs normatifs pour une même obligation, rédigés en termes différents, donneront des audits divergents.
- **Correctif proposé** : faire d'ARC-05 et d'ARC-06 de simples renvois (« selon EXIG-ORC-11 et EXIG-ORC-13 »), ou unifier les déclencheurs (« écriture, approbation ou plus d'une étape ») et le contenu.
- **Confiance** : vérifié dans le texte (l. 5805-5827).

### [04-12] [MINEUR] « Aucun état en mémoire de processus » contre « jamais seulement en mémoire »
- **Axe** : C (couture p. 35 / p. 42)
- **Localisation** : EXIG-ARC-05 p. 35 : « jamais seulement en mémoire de processus »; tableau 13 p. 42 : « aucun état en mémoire de processus (EXIG-ARC-05) »; figure 4 : « Interdits : état conservé en mémoire de processus ».
- **Diagnostic** : la fenêtre de contexte, que le tableau 13 range dans la mémoire de travail, vit forcément en mémoire de processus pendant un appel. La figure 4 et le tableau 13 durcissent ARC-05 en une interdiction impossible à respecter.
- **Correctif proposé** : écrire « aucun état qui n'existe qu'en mémoire de processus » dans la figure 4 et le tableau 13.
- **Confiance** : vérifié dans le texte.

### [04-13] [MINEUR] « Plafonds restants » : double dépense possible dans une délégation parallèle; « jetons » à double sens
- **Axe** : A (et C)
- **Localisation** : EXIG-ARC-02 p. 33 : « le contexte de trace et les plafonds restants de la tâche (jetons, coût, appels d'outils, délai) ».
- **Diagnostic** : pris à la lettre, transmettre le plafond « restant » à chaque branche d'un parallélisme permet à N branches de dépenser chacune la totalité du solde. EXIG-FIN-04 corrige (« une part de l'enveloppe restante »), mais ARC-02 n'y renvoie pas, et EXIG-ORC (l. 6071) dit encore « budget restant ». Dans la même phrase, « jeton » désigne d'abord le jeton OAuth délégué, puis les jetons de modèle.
- **Contre-exemple** : il reste 10 $ à l'orchestrateur, qui délègue en parallèle à 3 agents. Chacun reçoit « 10 $ restants », et la dépense peut atteindre 30 $.
- **Correctif proposé** : écrire « la part allouée des plafonds (EXIG-FIN-04) » et « jetons de modèle ».
- **Confiance** : vérifié dans le texte (FIN-04, l. 9873-9876).

### [04-14] [MINEUR] Droits du mandant seul, au lieu de l'intersection de PRIN-03
- **Axe** : A
- **Localisation** : EXIG-ARC-07 p. 35 : « soumis à l'autorisation de la passerelle selon le mandant et le palier de l'outil »; EXIG-ARC-16 p. 37 : « aucun agent ne reçoive une donnée que le mandant ne pourrait pas consulter lui-même ».
- **Diagnostic** : selon PRIN-03, les droits effectifs sont l'intersection des droits du mandant et de ceux de l'agent. EXIG-IAM-02 ajoute l'identité de l'agent, le niveau d'autonomie, l'état de la tâche et les signaux de risque. Filtrer selon le mandant seul laisse fuir vers l'agent ce que son propre périmètre exclut.
- **Contre-exemple** : la directrice des ressources humaines délègue une tâche à un agent de facturation. L'outil agrégé renvoie des données RH qu'elle peut consulter. ARC-16 est respecté, PRIN-03 ne l'est pas.
- **Correctif proposé** : dans ARC-16, écrire « selon les droits effectifs (intersection du mandant et de l'agent, PRIN-03) », et dans ARC-07 renvoyer aux entrées de décision d'IAM-02.
- **Confiance** : vérifié dans le texte (l. 1444-1450, 7507-7513).

### [04-15] [MINEUR] EXIG-ARC-13 : authentification exigée, autorisation absente
- **Axe** : C
- **Localisation** : EXIG-ARC-13 p. 36-37 : « ses producteurs comme ses consommateurs DOIVENT s'authentifier auprès du bus »; « un simple abonnement suffit à contourner la règle centrale ».
- **Diagnostic** : le « Pourquoi » vise l'abonnement abusif, mais l'exigence n'impose que l'authentification. L'autorisation par sujet tirée du catalogue figure dans EXIG-EVT-07, qu'ARC-13 ne cite pas. Lu seul, ARC-13 accepte qu'un agent authentifié s'abonne à n'importe quel sujet inscrit.
- **Correctif proposé** : ajouter « et être autorisés par sujet selon l'entrée de catalogue (EXIG-EVT-07) ».
- **Confiance** : vérifié dans le texte (l. 4779-4785).

### [04-16] [MINEUR] EXIG-ARC-04 : « poursuivre une trace » sans condition de confiance
- **Axe** : A
- **Localisation** : EXIG-ARC-04 p. 34 : « Il DOIT aussi ouvrir ou poursuivre une trace conforme à W3C Trace Context avant de transmettre la demande ».
- **Diagnostic** : le § 10.1 (l. 9256-9258) ne poursuit une trace que si l'en-tête `traceparent` est valide et vient d'une source de confiance, et prévoit de la redémarrer à une frontière de confiance. ARC-04 permet de poursuivre sans condition la trace d'un webhook externe. Un appelant pourrait alors injecter un identifiant de trace et polluer la corrélation dont dépend l'imputabilité.
- **Correctif proposé** : ajouter « poursuivre une trace entrante seulement si elle vient d'une source de confiance; la redémarrer à une frontière de confiance (section 10.1) ».
- **Confiance** : vérifié dans le texte.

### [04-17] [MINEUR] EXIG-ARC-09 : ordre ambigu entre changement de modèle et réévaluation; alias non épinglé
- **Axe** : A
- **Localisation** : EXIG-ARC-09 p. 35 : « un changement de modèle ou de fournisseur s'effectue par configuration, suivi d'une réévaluation (section 10.4) ».
- **Diagnostic** : « suivi d'une » se lit comme une réévaluation postérieure au changement en production. EXIG-GOV et EXIG-CON (l. 10581, 10864) exigent au contraire la réévaluation « avant la mise en production ». Rien n'oblige non plus l'alias à se résoudre vers une version immuable : un alias de fournisseur flottant (« latest ») change de modèle sans qu'aucune configuration de l'entreprise ne bouge. La l. 9701 (« y compris derrière un même alias ») ne couvre que les changements détectés.
- **Correctif proposé** : écrire « précédé d'une réévaluation ». Exiger que l'alias se résolve vers un instantané daté, épinglé et inscrit au registre.
- **Confiance** : vérifié dans le texte; le risque d'alias flottant est déduit.

### [04-18] [MINEUR] Tableau 12 : exemples de SBB non conformes présentés sans le signaler
- **Axe** : C (et B)
- **Localisation** : tableau 12 p. 40 : « OpenAI Agents SDK (boucle d'agent, MCP, traçage intégré et fournisseurs non OpenAI; A2A et OpenTelemetry non documentés) »; « Azure API Management (outils MCP seulement, agents A2A en JSON-RPC seulement) »; « agents de flux de Google ADK ».
- **Diagnostic** : le tableau mentionne bien les lacunes, mais ne dit pas qu'elles déclenchent EXIG-ARC-21 (dérogation) ou EXIG-ARC-02 (refus d'homologation d'un composant incapable de propager la trace). Il reste aussi à vérifier que les agents de flux de Google ADK, qui ordonnancent les étapes, forment un « moteur d'exécution durable » au sens d'ARC-05 et d'ORC-11 (persistance hors processus après chaque transition).
- **Correctif proposé** : ajouter une colonne ou une note « écarts connus : dérogation requise (ARC-21) ». Vérifier la durabilité d'ADK, ou la déplacer vers la ligne de l'orchestrateur.
- **Confiance** : vérifié dans le texte; les capacités d'ADK sont à vérifier.

### [04-19] [MINEUR] Tableau 12 : références manquantes
- **Axe** : C
- **Localisation** : tableau 12 p. 40-41 : « IBM ContextForge (licence Apache 2.0; modèle de soutien non précisé par le projet) » sans référence (cité [113] à la p. 37); « Azure API Center »; « Agent Registry de MuleSoft Agent Fabric »; « AgentCore Runtime »; « ServiceNow AI Agent Fabric ».
- **Diagnostic** : la plupart des exemples du tableau sont sourcés; ceux-là ne le sont pas, ce qui tranche avec la méthode de l'annexe F.
- **Correctif proposé** : ajouter [113] et les références primaires manquantes.
- **Confiance** : vérifié dans le texte.

### [04-20] [MINEUR] Encadré ATTENTION : triplé, sans même jeu de conditions, et sans critère d'acceptation
- **Axe** : B (et C)
- **Localisation** : fin du § 5.4, p. 41 : « la documentation de TrueFoundry annonce [...] inférieure à 5 ms, alors que son propre banc d'essai (page d'architecture) mesure de 7 à 12 ms ».
- **Diagnostic** : le même constat revient au § 9.4 (l. 8240-8252) et au § 13.2 (l. 12163-12168), avec des détails différents (1 vCPU et 200 à 370 requêtes par seconde ailleurs, absents ici; « 512 connexions » au § 9.4 seulement). « Alors que » présente comme une contradiction deux valeurs prises dans des conditions différentes. Enfin, sans seuil fixé, la mesure exigée (EXIG-APP-04) n'a aucun critère de réussite : l'exigence de mesure est vérifiable, mais l'acceptation de la passerelle ne l'est pas.
- **Correctif proposé** : garder une seule version complète (au § 13.2) et y renvoyer d'ici. Exiger que la fiche ou l'appel d'offres fixe un budget de latence ajoutée (P99) propre à l'entreprise, qui serve de critère d'acceptation.
- **Confiance** : vérifié dans le texte.

### [04-21] [MINEUR] Collisions terminologiques : « palier » et « point de contrôle »
- **Axe** : C
- **Localisation** : figure 3 p. 32 : « Évaluation continue (3 paliers) »; tableau 11 p. 39 : « Palier P0 à P3 »; EXIG-ARC-06 p. 35 : « Points de contrôle protégés ».
- **Diagnostic** : « palier » désigne à la fois le palier d'outil P0-P3, une échelle normative, et le palier d'évaluation 1-3 du § 10.4. « Point de contrôle » désigne à la fois l'état persisté (checkpoint, ARC-05 et ARC-06) et l'étape du cycle de vie (EXIG-GOV-11, figure 25). Le § 3.1 interdit de confondre les échelles; ces homonymes y invitent.
- **Correctif proposé** : renommer en « étages d'évaluation E1-E3 » et « jalons du cycle de vie » (ou « barrières »).
- **Confiance** : vérifié dans le texte (l. 9699, 10571-10573).

### [04-22] [MINEUR] Renvois générés mal accordés
- **Axe** : C
- **Localisation** : EXIG-ARC-20 p. 39 : « les ABB de tableau 12 », « un ABB de tableau 12 »; p. 33 : « Chaque boîte de figure 3 »; p. 42 : « [151]. figure 4 et tableau 13 en présentent l'organisation ».
- **Diagnostic** : il manque l'article et la contraction (« du tableau 12 », « de la figure 3 »), et une phrase commence par une minuscule. Le défaut est systématique et vient du gabarit de renvoi.
- **Correctif proposé** : corriger le gabarit Typst pour produire « du tableau », « de la figure » et une majuscule en début de phrase.
- **Confiance** : vérifié dans le texte.

### [04-23] [MINEUR] « Mandataire inverse » pour une passerelle qui joue dans les deux sens
- **Axe** : C
- **Localisation** : p. 36 : « la passerelle d'agents, mandataire inverse devant les serveurs MCP et les pairs A2A »; EXIG-ARC-11 : « Passerelle d'agents dans les deux sens ».
- **Diagnostic** : le trafic sortant vers un SaaS ou un partenaire passe par un mandataire sortant (forward proxy), pas par un mandataire inverse. Le terme du tableau 12 (« Mandataire inverse ») ne couvre que la moitié d'ARC-11.
- **Correctif proposé** : écrire « mandataire inverse en entrée et mandataire sortant en sortie ».
- **Confiance** : vérifié dans le texte.

### [04-24] [MINEUR] « Équipe plateforme » employée avant d'être définie
- **Axe** : C
- **Localisation** : p. 35 (couche 3) et EXIG-ARC-19 p. 39 : « DOIVENT être fournis par l'équipe plateforme ».
- **Diagnostic** : le terme porte une obligation normative dans ARC-19, mais sa première définition apparaît au chapitre 11 (l. 10037), sans renvoi et sans entrée au tableau 7.
- **Correctif proposé** : ajouter un renvoi (« section 11.1 ») ou une entrée au tableau 7.
- **Confiance** : vérifié dans le texte (Grep : première occurrence l. 1957).

### [04-25] [MINEUR] Placement des mémoires : la figure 3 contredit le § 5.5
- **Axe** : C (couture p. 32 / p. 42)
- **Localisation** : figure 3, couche 2 : « Points de contrôle, mémoire de travail »; couche 3 : « Mémoire épisodique et procédurale »; figure 4 : épisodique « exposée en ressources ou outils MCP »; tableau 13, travail : « Fenêtre de contexte ».
- **Diagnostic** : la figure 3 place la mémoire de travail en couche 2 et l'épisodique en couche 3. Le § 5.5 met la mémoire de travail dans le contexte du modèle (couche 3) et expose l'épisodique comme ressource MCP (couche 5, derrière la passerelle). La mémoire sémantique n'est nommée qu'implicitement en couche 5 (« index, graphes »).
- **Correctif proposé** : aligner la figure 3 sur le tableau 13 : travail en couches 2 et 3, épisodique et sémantique en couche 5, procédurale déployée avec l'agent.
- **Confiance** : vérifié dans le texte.

### [04-26] [MINEUR] Agents ambiants déclenchés par le bus : qui établit le mandant?
- **Axe** : A
- **Localisation** : § 5.2, couche 1, p. 34 : « Un agent ambiant [...] y est raccordé par un déclencheur (par exemple une tâche planifiée qui vérifie périodiquement les nouveaux événements) ».
- **Diagnostic** : la figure 3 place les « événements » en couche 1, et le bus en couche 4. Un agent abonné directement au bus n'a pas de déclencheur de couche 1 au sens d'ARC-04. EXIG-EVT-07 interdit en outre de fonder un droit sur `authid` ou `authclaims`. Le mandant d'une tâche déclenchée par un événement n'est donc fixé nulle part : identité de service et propriétaire? Personne à l'origine de l'événement?
- **Correctif proposé** : préciser dans ARC-04 que le consommateur d'un événement est un déclencheur système, dont le mandant est l'identité du service et son propriétaire, jamais un attribut de l'événement.
- **Confiance** : déduit.

### [04-27] [MINEUR] EXIG-ARC-08 : périmètre de « tout appel d'inférence » et phrase redondante
- **Axe** : A (et C)
- **Localisation** : EXIG-ARC-08 p. 35 : « Tout appel d'inférence DOIT passer par la passerelle de modèles de l'entreprise. Un agent DOIT n'accéder aux modèles que par cette passerelle ».
- **Diagnostic** : la deuxième phrase répète la première. Le périmètre reste flou pour les plongements de l'indexation sémantique, les classifieurs de garde-fous et de DLP embarqués, les juges LLM de l'évaluation et les modèles locaux. Ces appels sont-ils visés? Sans réponse, l'exigence est soit inapplicable (un classifieur embarqué), soit contournable.
- **Correctif proposé** : fusionner les deux phrases et définir « appel d'inférence », en énumérant les exclusions éventuelles (par exemple : modèle embarqué inscrit au registre).
- **Confiance** : vérifié dans le texte.

### [04-28] [MINEUR] EXIG-ARC-01 omet l'empreinte
- **Axe** : C
- **Localisation** : EXIG-ARC-01 p. 33 : « viser un élément inscrit au catalogue d'entreprise à une version approuvée ».
- **Diagnostic** : EXIG-ARC-12 (« leur version et leur empreinte approuvées ») et EXIG-IAM-17 (« dont la version ou l'empreinte diffère ») bloquent aussi sur l'empreinte. ARC-01 ne vise que la version : un serveur republié sous le même numéro de version, avec un contenu différent, le respecterait.
- **Correctif proposé** : écrire « à une version et une empreinte approuvées ».
- **Confiance** : vérifié dans le texte.

## Points forts
- La distinction ABB/SBB (TOGAF, phases A-D puis E) et le principe « des rôles, pas des produits » sont posés rigoureusement et datés (27 octobre 2026).
- La prudence sur les chiffres des fournisseurs (encadré ATTENTION, refus des gains non mesurés) et la séparation entre exigence externe et choix du cadre sont exemplaires.
- Les exigences ARC-07 (le routage n'accorde aucun droit), ARC-16 (filtrage à la source) et ARC-17 (écriture par les interfaces métier) sont justes et vérifiables en revue.

## Questions pour l'audit bibliographique
- p. 34 [104] : AWS Step Functions. Le « exactement une fois » des flux Standard porte-t-il sur l'exécution du flux seulement, effets des tâches réessayées exclus? Durées confirmées : Standard ≤ 1 an, Express ≤ 5 min.
- p. 34 [81] : Temporal, « sans limite de temps imposée ». Quelle est la limite de taille de l'historique qui impose Continue-As-New?
- p. 35 [36, 106] et p. 40 [130] : Envoy AI Gateway, renommé Agent Router, a-t-il rejoint l'AAIF le 9 septembre 2026? p. 40 [31] : agentgateway à l'AAIF le 4 juin 2026?
- p. 35 [107] : nom exact de la politique `llm-token-limit` d'Azure API Management.
- p. 36 [111] : greffon AI A2A Proxy de Kong, version 3.14 et plus, édition AI Gateway Enterprise.
- p. 36 [28] : l'identifiant ASI05 « Unexpected Code Execution » de l'OWASP Top 10 for Agentic Applications 2026.
- p. 37 [9] : le Centre d'architecture Azure demande-t-il le filtrage de sécurité (security trimming) « dans chaque agent »?
- p. 38 [119, 120] : `invoke_workflow` figure-t-il parmi les valeurs de `gen_ai.operation.name` dans la version épinglée (v1.41.0) des conventions GenAI?
- p. 38 [46] : Microsoft Agent 365 est-il en disponibilité générale depuis le 1er mai 2026, avec les actions de cycle de vie sur les agents tiers « à venir »?
- p. 38 [116, 117] : SPIFFE et SPIRE sont-ils des projets diplômés de la CNCF (selon moi, depuis 2022)?
- p. 40 [122] : l'intégration de Temporal avec l'OpenAI Agents SDK est-elle en disponibilité générale depuis le 23 mars 2026? [125] : Microsoft Agent Framework 1.0? [126] : les agents de flux de Google ADK persistent-ils l'état hors processus après chaque transition?
- p. 40 [140] : Kafka garantit-il par défaut une livraison au moins une fois, compte tenu des réglages du producteur idempotent par défaut depuis la 3.0 et du commit automatique côté consommateur?
- p. 41 [48] : A2A est-il en disponibilité générale dans Copilot Studio depuis avril 2026, avec une identité Entra Agent ID pour chaque nouvel agent? [49] : A2A entrant et sortant dans Agentforce?
- p. 41 [143, 144] : les conditions du banc d'essai de TrueFoundry (1 vCPU, de 200 à 370 requêtes par seconde) et de sa FAQ (« typiquement < 5 ms ») sont-elles comparables?
- [04-07] : combien de temps les API de paiement et les ERP courants gardent-ils les clés d'idempotence (par exemple 24 h)?

audit_04.md : 28 constats (1 BLOQUANT, 8 MAJEUR, 19 MINEUR)
