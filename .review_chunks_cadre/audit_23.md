# Audit chunk_23 — pages 221-232

## Synthèse
Le chunk couvre la fin de l'annexe C (C.6 jeton d'approbation, C.7 enveloppe budgétaire, C.8 enregistrement d'audit), le registre des exigences (annexe D, 287 entrées) et le début du glossaire (annexe E). Qualité élevée : les empreintes h, arguments_sha256 et la clé d'idempotence se recalculent exactement, et le registre concorde à 100 % (force et titre) avec les 287 blocs EXIG du corps. Les trois défauts les plus graves : (1) le registre juxtapose deux exigences contradictoires, EXIG-INT-05 (agent comme outil permis dans un même domaine) et EXIG-A2A-01 (A2A obligatoire pour un autre cadriciel); (2) l'enregistrement d'audit est écrit après l'exécution, et rien ne règle la panne entre l'effet et l'écriture, ni l'interaction entre usage unique du jti, réessai idempotent et expiration à 15 minutes; (3) C.8 affirme que le recalcul de h « prouve » l'action exécutée, alors que h ne lie ni l'appelant ni l'empreinte de définition, et que le format ne permet ni de détecter l'auto-approbation ni de porter deux approbateurs.

## Constats

### [23-01] [BLOQUANT] EXIG-INT-05 et EXIG-A2A-01 se contredisent sur l'agent comme outil
- **Axe** : A
- **Localisation** : annexe D, p. 225 (EXIG-INT-05 « DEVRAIT — Agent pair invoqué par A2A, pas déguisé en outil »; EXIG-A2A-01 « DOIT — A2A 1.0 pour toute délégation entre agents »); corps p. 49 et p. 68. INT-05 : « L'enveloppe "agent comme outil" reste permise à l'intérieur d'un même agent ou d'un même domaine de confiance. » A2A-01 : « délègue une tâche à un agent d'un autre domaine, d'un autre cadriciel ou d'un tiers DOIT utiliser A2A ».
- **Diagnostic** : les deux règles portent sur le même acte et diffèrent par la force comme par le périmètre. Pour un autre domaine, A2A-01 impose (DOIT) ce qu'INT-05 recommande seulement (DEVRAIT, donc dérogeable par simple justification à la fiche, tableau 3). Pour un même domaine de confiance mais un autre cadriciel et un autre processus, INT-05 permet ce qu'A2A-01 interdit. A2A-01 n'exempte que « dans un même processus ».
- **Contre-exemple** : un agent LangGraph du domaine Finances enveloppe un agent Microsoft Agent Framework du même domaine dans un outil MCP. Selon INT-05, c'est conforme; selon A2A-01, c'est non conforme. La revue d'architecture ne peut pas trancher, et le cycle de vie A2A (input-required, auth-required, annulation), dont dépendent l'approbation et l'audit selon INT-05 lui-même, disparaît.
- **Correctif proposé** : aligner les deux exigences sur un même critère. Par exemple : INT-05 en DOIT, avec l'exception d'A2A-01 (« même orchestrateur, même processus »), ou bien l'exception d'A2A-01 étendue à « même domaine de confiance et même cadriciel ». Ajouter un renvoi croisé.
- **Confiance** : vérifié dans le texte

### [23-02] [MAJEUR] Enregistrement d'audit postérieur à l'exécution : exhaustivité non garantie
- **Axe** : A / B
- **Localisation** : C.8, p. 223 : « l'enregistrement que la passerelle verse au journal d'audit après l'exécution de l'action approuvée »; EXIG-OBS-11 (p. 151) exige un enregistrement pour « chaque action à effet [...] sans échantillonnage ».
- **Diagnostic** : l'effet (création de BC-2026-118734) et l'ajout au journal sont deux écritures non atomiques sur deux systèmes. Le cadre ne fixe ni enregistrement d'intention préalable (sur le modèle du journal de compensation « tenu avant l'action » d'EXIG-ORC-16), ni comportement de la passerelle quand le service d'audit est indisponible. Aucune occurrence de « audit » avec « indisponible » dans le document : on ne sait pas si elle doit refuser en mode fermé ou exécuter, puis mettre en tampon.
- **Contre-exemple** : la passerelle relaie tools/call, le serveur crée le bon, puis la passerelle tombe avant l'ajout. Résultat : un effet P2 de 12 480 $ sans enregistrement, et EXIG-OBS-11 est violée sans qu'aucun contrôle ne le détecte, puisque le chaînage ne voit que ce qui a été écrit.
- **Correctif proposé** : exiger un enregistrement « intention » chaîné avant le relais (issue en_cours), puis un enregistrement « issue » qui le référence. La vérification quotidienne d'EXIG-OBS-13 traite toute intention sans issue comme un incident. Fixer en DOIT le comportement de la passerelle si le journal est indisponible (refus des P2 et P3, comme EXIG-AUT-11).
- **Confiance** : vérifié dans le texte (absence de règle); scénario déduit

### [23-03] [MAJEUR] Usage unique du jti, expiration à 15 minutes et réessai idempotent : sémantique indéterminée
- **Axe** : A
- **Localisation** : C.6, p. 221 : « La passerelle vérifie la signature, l'expiration et l'usage unique, puis recalcule h »; C.8, p. 223 : correlation.cle_idempotence, approbation_jti; EXIG-AUT-12 (p. 110), EXIG-ORC-21 (p. 97-98 : clé « réutilisée telle quelle à chaque réessai »).
- **Diagnostic** : la clé d'idempotence fait partie des arguments, donc de h. Un réessai après une panne réseau ou après le cas [23-02] présente le même h et le même jti. Deux lectures sont possibles, et aucune n'est fixée. (a) Le jti est consommé avant le relais : le réessai légitime est refusé (« approbation requise ») pour une action peut-être déjà exécutée, et il faut une nouvelle approbation humaine d'un fait accompli. (b) Le jti est consommé après succès : une panne entre effet et consommation laisse le jti rejouable. L'idempotence côté serveur absorbe l'effet, mais pas l'enregistrement d'audit en double. S'y ajoute l'expiration à 15 minutes : un réessai durable (exécution reprise, EXIG-ORC-12) au-delà de exp (9 h 39 UTC ici) échoue, quelle que soit la lecture. Enfin, rien ne dit que le magasin des jti consommés est partagé entre les instances de la passerelle, ni combien de temps il est conservé.
- **Contre-exemple** : le relais part à 9 h 26 et le serveur crée le bon, mais la réponse se perd. L'orchestrateur reprend à 9 h 41 avec la même clé. Le jeton est expiré ou consommé : refus, tâche suspendue, approbateur sollicité de nouveau pour un bon qui existe déjà (rejeu: true côté serveur).
- **Correctif proposé** : définir l'état du jti comme une machine (réservé → consommé ou libéré), liée à la clé d'idempotence. Un réessai porteur de la même clé et du même h est admis après exp tant que le service visé répond « rejeu », sans nouvel effet. Le magasin des jti doit être partagé, avec une rétention d'au moins exp + fenêtre de réessai.
- **Confiance** : déduit (silence du texte vérifié)

### [23-04] [MAJEUR] « Ce qui prouve que l'action exécutée est bien celle qui a été approuvée » : affirmation trop forte
- **Axe** : A
- **Localisation** : C.8, p. 224 : « la passerelle l'a recalculée avant l'exécution, ce qui prouve que l'action exécutée est bien celle qui a été approuvée »; même formule dans le Pourquoi d'EXIG-OBS-12 (p. 151).
- **Diagnostic** : l'égalité de h prouve seulement que la requête reçue par la passerelle porte le même outil@version et les mêmes arguments que ceux approuvés. Elle ne lie : (a) ni l'appelant, car la vérification énumérée (signature, expiration, usage unique, h) ne compare pas agent_id et task_id du jeton à l'identité SPIFFE et à la tâche de l'appel, et le jeton n'a pas de cnf; (b) ni la définition, car h et le champ action.definition portent « 1.4.0 », pas le definition_digest que le catalogue C.2 tient (sha256:3182…), alors qu'EXIG-MCP-20 pilote l'empreinte de définition; (c) ni ce que le serveur aval a réellement exécuté. De plus, l'attestation provient de la passerelle elle-même.
- **Contre-exemple** : un autre agent, qui a la même portée sur l'outil, obtient le jeton d'approbation, qui transite par le contexte de l'orchestrateur, et soumet l'appel identique. Toutes les vérifications passent, l'audit attribue l'action à cet agent sous l'approbation donnée à agt-achats-indirects, et l'appel légitime est ensuite refusé (jti consommé).
- **Correctif proposé** : ajouter à la vérification DOIT la concordance agent_id/task_id du jeton avec l'appelant authentifié, et lier le jeton à l'appelant (cnf, ou empreinte du jeton délégué). Inclure definition_digest dans h et dans action. Reformuler « prouve » en « établit que la requête relayée est identique à celle approuvée ».
- **Confiance** : vérifié dans le texte (éléments absents); scénario déduit

### [23-05] [MAJEUR] Chaînage : « une suppression ou une modification se détecte » sans ancrage de la tête
- **Axe** : A / B
- **Localisation** : C.8, p. 224 : « precedent_sha256 chaîne chaque enregistrement au précédent, de sorte qu'une suppression ou une modification se détecte »; EXIG-OBS-12 : « l'empreinte de l'enregistrement précédent du même flux ».
- **Diagnostic** : une chaîne de hachage détecte une suppression ou une modification en son milieu, pas la troncature des derniers enregistrements. Elle ne détecte pas non plus la réécriture complète par un détenteur de la clé de signature, ni la disparition d'un flux entier. Le « flux » n'est défini nulle part (aucune occurrence de « flux d'audit »). Une chaîne unique (sequence 48213) sérialise tous les ajouts P2 et P3 de toutes les instances de passerelle : point de contention et de défaillance unique. Des chaînes par instance exigent un registre des flux, sans lequel la suppression d'un flux entier passe inaperçue. EXIG-OBS-13 (stockage en ajout seul) atténue la troncature, mais la vérification quotidienne ne peut pas constater l'absence de la queue sans une tête publiée ailleurs. Le kid mensuel (« journal-audit-2026-10 ») suppose une rotation des clés, mais la conservation des clés de vérification pendant 24 mois n'est pas fixée.
- **Contre-exemple** : un exploitant qui a accès au magasin sous-jacent supprime les enregistrements 48210 à 48213. La chaîne restante est valide, et la vérification quotidienne passe.
- **Correctif proposé** : définir le flux (par instance ou par partition, avec le registre des flux), ancrer périodiquement la tête (séquence et empreinte) hors du magasin, dans un journal de transparence ou un horodatage signé tiers, puis vérifier la continuité contre cet ancrage. Fixer la conservation des clés publiques pour toute la durée de rétention.
- **Confiance** : vérifié dans le texte (absence); propriété cryptographique connue

### [23-06] [MAJEUR] Auto-approbation du mandant non interdite au-delà du seuil P2, et indétectable dans l'audit
- **Axe** : A / B
- **Localisation** : C.8, p. 223 : « "approbateur": "apb-5e19c2" » et « "pseudonyme": "u-58c1d7" »; EXIG-AUT-15 (p. 112) : « Pour un appel P3 d'un agent de classe élevée, deux approbateurs distincts DOIVENT approuver, dont au moins un autre que le mandant ».
- **Diagnostic** : la seule exigence qui sépare l'approbateur du mandant vise P3 en classe élevée. Pour le cas de C.8 (P2 au-delà du seuil, classe modérée), rien n'empêche le mandant d'approuver sa propre commande s'il figure parmi les approbateurs habilités, et le contrôle « approbation_requise_au_dela_du_seuil » devient alors un acquiescement à soi-même. De plus, approbateur et mandant appartiennent à deux espaces de pseudonymes distincts (apb- et u-). On ne peut donc pas vérifier la séparation à partir du journal sans la table de correspondance gardée par le responsable de la protection des RP (EXIG-OBS-13), ce qui rend la séparation des fonctions (EXIG-GOV-03) non automatisable.
- **Contre-exemple** : Alice, acheteuse principale inscrite comme approbatrice de la combinaison modérée × P2, lance la tâche puis approuve sur son propre appareil par CIBA un bon de 12 480 $. Tout est conforme et indiscernable dans l'audit.
- **Correctif proposé** : exiger, pour toute approbation, approbateur ≠ mandant (DOIT), vérifié par la passerelle au moment de l'émission. Consigner dans l'enregistrement un indicateur calculé « approbateur_distinct_du_mandant », ou un pseudonyme commun aux deux rôles.
- **Confiance** : vérifié dans le texte

### [23-07] [MAJEUR] Format d'approbation à un seul approbateur, incompatible avec la double approbation exigée
- **Axe** : A / C
- **Localisation** : C.6, p. 221 (« "sub": "apb-5e19c2" », un seul jti); C.8, p. 223 (autorite.approbateur, approbation_jti : scalaires); annexe C, p. 215 : « Ils sont normatifs par leur forme »; EXIG-AUT-15 (deux approbateurs distincts pour P3 en classe élevée).
- **Diagnostic** : si la forme des exemples est normative, le jeton et l'enregistrement ne peuvent représenter qu'un approbateur. Le cas P3 en classe élevée, avec deux jetons ou un jeton cosigné, n'a pas de forme : la passerelle ne sait pas s'il faut deux jti, deux signatures ou une liste, et l'audit ne peut pas en garder la trace.
- **Contre-exemple** : un paiement P3 d'un agent de classe élevée. Le second approbateur n'a aucun champ prévu dans autorite, et l'enregistrement conforme à C.8 omet une approbation exigée.
- **Correctif proposé** : faire d'autorite.approbations une liste de couples {approbateur, jti, empreinte}, et préciser à la section 8.5 si la double approbation passe par deux jetons distincts sur le même h ou par un jeton multisigné.
- **Confiance** : vérifié dans le texte

### [23-08] [MAJEUR] Modèle de raisonnement servi à une étape non autorisée par l'enveloppe
- **Axe** : C
- **Localisation** : C.7, p. 222 : « "reasoning_steps": ["planification", "arbitrage"] » et « le modèle de raisonnement seulement aux étapes nommées »; C.8, p. 223 : « "etape": "etape-03/creer-bon-commande" » avec « "servi": "modele-raisonnement" ».
- **Diagnostic** : le scénario fil rouge (même tâche, même agent, 41 secondes d'écart) montre l'étape de création du bon servie par le modèle de raisonnement, alors que l'enveloppe le réserve à la planification et à l'arbitrage. L'exemple qui doit illustrer la conformité illustre une violation d'EXIG-FIN-06 (correspondance étape → modèle appliquée par la passerelle).
- **Contre-exemple** : un auditeur qui confronte C.7 et C.8 avec la vérification de routage de la passerelle conclurait à un écart de routage dans l'exemple de référence.
- **Correctif proposé** : mettre « modele-compact » dans C.8, ou nommer l'étape « etape-03/arbitrage » et l'ajouter à reasoning_steps, en expliquant pourquoi une écriture P2 exige du raisonnement.
- **Confiance** : vérifié dans le texte

### [23-09] [MAJEUR] Statut des exemples contradictoire : informatifs (§ 1.4) ou normatifs par la forme (annexe C)?
- **Axe** : C
- **Localisation** : § 1.4, p. 13 : « le reste du texte, les exemples et les figures sont informatifs »; annexe C, p. 215 : « Ils sont normatifs par leur forme, pas par leurs valeurs ».
- **Diagnostic** : les deux énoncés s'excluent. L'enjeu est concret pour ce chunk : si la forme de C.8 est normative, les divergences avec l'extrait de la section 10.3 [23-12] et les conventions incohérentes [23-13] deviennent des contradictions normatives; si elle est informative, l'homologation (annexe A) n'a aucun format de référence pour l'enregistrement d'audit.
- **Contre-exemple** : un fournisseur produit des enregistrements selon la structure de la section 10.3 (signature au même niveau que precedent_sha256, sans enveloppe empreinte/enregistrement). Sous le § 1.4, c'est conforme; sous l'annexe C, non.
- **Correctif proposé** : énoncer au § 1.4 l'exception (« la structure des exemples de l'annexe C est normative lorsqu'une exigence y renvoie »), puis faire renvoyer EXIG-OBS-12 et EXIG-AUT-12 expressément à C.8 et C.6.
- **Confiance** : vérifié dans le texte

### [23-10] [MAJEUR] Trois exigences de réévaluation aux déclencheurs divergents
- **Axe** : C / A
- **Localisation** : annexe D, p. 227, 229, 230 : EXIG-AUT-05 « Homologation et réévaluation du niveau », EXIG-GOV-12 « Réévaluation sur changement significatif », EXIG-CON-03 « Réévaluation à chaque changement significatif »; corps p. 106, 167, 172.
- **Diagnostic** : les listes diffèrent. AUT-05 exclut la « correction purement typographique » de l'invite système, alors que GOV-12 vise toute « modification de l'invite système », sans exception, pour la classe et le niveau. CON-03, qui réévalue la classe, omet l'invite système et la nouvelle version majeure de contrat que GOV-12 retient. GOV-12 ajoute « incident grave ou dérive », que les deux autres ignorent. Le régime transitoire diffère aussi : AUT-05 impose le « niveau immédiatement inférieur », GOV-12 le permet seulement « si le changement ne peut attendre ».
- **Contre-exemple** : une coquille corrigée dans l'invite système. Selon AUT-05, pas de réévaluation du niveau; selon GOV-12, réévaluation obligatoire avant la mise en production. Les deux exigences sont en DOIT.
- **Correctif proposé** : une liste unique des changements significatifs (dans GOV-12), à laquelle AUT-05 et CON-03 renvoient, avec une seule exception typographique et un seul régime transitoire.
- **Confiance** : vérifié dans le texte

### [23-11] [MAJEUR] Politique en cache sans âge maximal, alors que le coupe-circuit dépend de la propagation
- **Axe** : B
- **Localisation** : annexe D, p. 228 (EXIG-IAM-18 « Échec en mode fermé et refus typé », EXIG-IAM-20 « Coupe-circuit propagé et mesuré »); corps p. 129 : « Si le plan de contrôle est indisponible, elle continue d'appliquer la dernière politique distribuée »; EXIG-AUT-11 (p. 110).
- **Diagnostic** : IAM-18 autorise la passerelle à décider indéfiniment sur la dernière politique reçue. IAM-20 exige une suspension « sur toutes les passerelles » en une seule action. Pendant une panne du plan de contrôle, une suspension émise après la dernière distribution n'atteint pas les passerelles, qui continuent d'admettre les appels P0, P1 et P2 sous le seuil de l'agent suspendu. AUT-11 ne bloque que P3 et P2 au-delà du seuil, et seulement si le « service de politiques » (distinct ou non du plan de contrôle : non précisé) est indisponible.
- **Contre-exemple** : l'agent est compromis, le plan de contrôle est en panne et le coupe-circuit est actionné. Les passerelles appliquent la politique d'avant la suspension, et l'agent continue de créer des bons de moins de 5 000 $ (P2 sous le seuil, sans approbation).
- **Correctif proposé** : fixer un âge maximal de la politique en cache (par exemple quelques minutes), au-delà duquel la passerelle passe en refus de toute écriture. Prévoir un canal de suspension indépendant du plan de contrôle, comme la révocation de l'identité auprès du fournisseur d'identité, qui est déjà dans IAM-20. Définir « service de politiques » et « plan de contrôle ».
- **Confiance** : déduit (textes vérifiés; architecture de distribution non décrite)

### [23-12] [MINEUR] Dérives entre l'extrait de la section 10.3 et l'enregistrement C.8
- **Axe** : C
- **Localisation** : C.8, p. 223-224 et § 10.3, p. 150-151. C.8 : « l'agent avec sa version, son identité et l'empreinte de son invite système ». § 10.3 : « sa version et celle de son invite système ».
- **Diagnostic** : (a) version de l'invite (§ 10.3) contre empreinte de l'invite (C.8); (b) § 10.3 place signature et precedent_sha256 au premier niveau, tandis que C.8 enveloppe {empreinte, enregistrement, signature} et met precedent_sha256 dans enregistrement, ce qui donne deux structures à hacher et à signer; (c) les identifiants de corrélation A2A (a2a_task_id, a2a_context_id), annoncés comme constituants, manquent dans C.8 (admissible sans délégation, mais non dit); (d) l'outil est nommé « erp_enregistrer_decision » sans serveur au § 10.3, et « serveur/nom » sans version dans C.8; (e) « art. 26(6) » (§ 10.3) contre « art. 26, par. 6 » (C.8).
- **Contre-exemple** : deux implémentations conformes chacune à un exemple produisent des empreintes incompatibles pour le même événement.
- **Correctif proposé** : aligner l'extrait du § 10.3 sur C.8 (ou le réduire à un renvoi), et préciser que les champs A2A sont omis faute de délégation.
- **Confiance** : vérifié dans le texte

### [23-13] [MINEUR] Conventions de champs et de préfixes de hachage incohérentes dans le scénario
- **Axe** : C
- **Localisation** : C.6-C.8, p. 221-223; annexe B, p. 212-213.
- **Diagnostic** : la même donnée change de nom d'un objet à l'autre : task_id (C.6, C.7) et tache (C.8); idempotency_key et cle_idempotence; cost_center (C.7) et centre_cout (arguments). agent_id « agt-achats-indirects@1.2.0 » (C.6, C.7) devient id + version (C.8). Le catalogue C.2 dit contract_version, C.8 dit definition. La classe s'écrit « moderee » (C.8) et « modere » (annexe B, risk_class). Le préfixe « sha256: » figure sur empreinte, precedent_sha256 et invite_systeme, mais pas sur arguments_sha256, empreinte_approbation ni action_sha256. Le chemin SPIFFE est « spiffe://ent.ca/agt-achats-indirects » ici, mais « spiffe://entreprise.example/agents/agt-… » à l'annexe B, alors que la convention des exemples fixe ent.ca, et C.5 utilise le préfixe « agent- ».
- **Contre-exemple** : une jointure automatique entre l'enveloppe, le jeton et l'audit sur la clé de tâche exige une table de correspondance des noms.
- **Correctif proposé** : un dictionnaire de champs unique pour l'annexe C (une langue, un préfixe de hachage constant, une énumération de classes unique).
- **Confiance** : vérifié dans le texte

### [23-14] [MINEUR] « Fiche d'agent (annexe B) » : la fiche est celle d'un autre agent
- **Axe** : C
- **Localisation** : C.7, p. 222 : « l'enveloppe reprend les plafonds de la fiche d'agent (annexe B) »; annexe B : agent_id « agt-fin-rapprochement », cost_center « CC-4120 ».
- **Diagnostic** : les plafonds sont identiques, mais la fiche décrit un autre agent et un autre centre de coûts. Aucune fiche d'agt-achats-indirects n'existe dans le document, de sorte que la classe « moderee » et le niveau « N3 » consignés en C.8 ne se rattachent à aucune fiche (le seuil de 5 000 $ et le palier P2 se vérifient en revanche au catalogue C.2).
- **Contre-exemple** : un lecteur qui suit le renvoi constate que CC-4120 ≠ CC-4410.
- **Correctif proposé** : écrire « mêmes valeurs que la fiche type de l'annexe B », ou aligner la fiche B sur agt-achats-indirects.
- **Confiance** : vérifié dans le texte

### [23-15] [MINEUR] Reproductibilité inégale des empreintes; dérivation de clé et concaténation non spécifiées
- **Axe** : A
- **Localisation** : C.8, p. 223 : « "empreinte": "sha256:689f1e00…" », avec des valeurs élidées (« "invite_systeme": "sha256:41d07c…" », « "fournisseur": "…" »); C.6, p. 221 : « immédiatement suivi des arguments canonisés ».
- **Diagnostic** : vérifiés par recalcul : h = SHA-256(« mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0 » ‖ JCS(arguments)) = 9a2c0a8c…; arguments_sha256 = cff55d8a…; la clé d'idempotence = SHA-256(« tache-7f3c2a|etape-03/creer-bon-commande »). En revanche, l'empreinte 689f1e00… ne peut pas se recalculer à partir du texte imprimé : avec les « … » littéraux, on obtient 43d95b9e…. Le séparateur « | » de la dérivation de clé n'est écrit nulle part (EXIG-ORC-21 dit seulement « dérivée de »), ce qui gêne l'interopérabilité entre orchestrateurs et reprises. La concaténation de h sans séparateur ni préfixe de longueur n'est non ambiguë que parce qu'un identifiant d'outil ne peut pas contenir « { », hypothèse non énoncée.
- **Contre-exemple** : deux orchestrateurs qui dérivent la clé avec « / » et « | » produisent des clés différentes pour la même étape, et la reprise crée un doublon.
- **Correctif proposé** : signaler l'empreinte C.8 comme illustrative ou donner les valeurs complètes; écrire la dérivation (« SHA-256(task_id ‖ "|" ‖ step_id) »); calculer h sur JCS([identifiant, arguments]) ou énoncer la contrainte sur les caractères de l'identifiant.
- **Confiance** : vérifié (recalcul)

### [23-16] [MINEUR] Dates RIA de C.8 appuyées sur des sources secondaires
- **Axe** : B / C
- **Localisation** : C.8, p. 224 : « obligations applicables à compter du 2 décembre 2027 pour l'annexe III et du 2 août 2028 pour l'annexe I »; appel « [94, 394] ».
- **Diagnostic** : [94] et [394] sont les pages de la Future of Life Institute (artificialintelligenceact.eu) sur les articles 26 et 12, donc des sources secondaires qui ne portent pas nécessairement le report du règlement (UE) 2026/1744. Le § 10.3 cite en plus [58, 61] et le règlement de report, mais pas C.8. L'annexe H.5 indique que le texte de 2026/1744 n'a pas pu être rouvert sur EUR-Lex.
- **Contre-exemple** : sans objet (fait externe).
- **Correctif proposé** : citer en C.8 les mêmes sources primaires que le § 10.3 (texte consolidé et règlement 2026/1744).
- **Confiance** : à vérifier (source externe)

### [23-17] [MINEUR] Révision trimestrielle du catalogue : deux responsables
- **Axe** : C
- **Localisation** : annexe D, p. 225 et 229; EXIG-INT-08 (p. 52) : « Le comité d'architecture et des risques agentiques DOIT réviser le catalogue des protocoles »; EXIG-GOV-18 (p. 169) : « L'architecture d'entreprise DOIT réviser le catalogue des protocoles au moins chaque trimestre et soumettre les changements de statut à l'approbation du comité ».
- **Diagnostic** : même obligation, même périodicité, sujet différent (le comité révise ou l'architecture révise et le comité approuve), ce qui brouille le RACI.
- **Contre-exemple** : un audit de conformité trimestriel ne sait pas qui consigner comme R.
- **Correctif proposé** : garder GOV-18 (architecture R, comité A) et faire d'INT-08 un renvoi.
- **Confiance** : vérifié dans le texte

### [23-18] [MINEUR] EXIG-MCP-11 sans l'exception subject_token d'EXIG-IAM-12
- **Axe** : C
- **Localisation** : annexe D, p. 225 et 228; EXIG-MCP-11 (p. 61) : « NE DOIT PAS [...] retransmettre en aval un jeton reçu »; EXIG-IAM-12 (p. 125) : « sauf au serveur d'autorisation, à titre de subject_token ».
- **Diagnostic** : lue seule, MCP-11 interdit l'échange de jetons qu'elle prescrit elle-même dans la phrase suivante. Le serveur d'autorisation est-il « en aval »? Le texte ne le dit pas.
- **Contre-exemple** : un vérificateur statique qui applique MCP-11 à la lettre signale toute présentation de subject_token.
- **Correctif proposé** : reprendre l'exception d'IAM-12 dans MCP-11, ou fusionner les deux par renvoi.
- **Confiance** : vérifié dans le texte

### [23-19] [MINEUR] Registre : titres qui, accolés à « NE DOIT PAS », inversent le sens; force unique pour des exigences mixtes
- **Axe** : C
- **Localisation** : annexe D : EXIG-SEC-14 « NE DOIT PAS — Secrets injectés par le mandataire de sortie » (p. 228); EXIG-GOV-03 « NE DOIT PAS — Séparation des fonctions », EXIG-GOV-17 « NE DOIT PAS — Exigences non dérogeables » (p. 229); EXIG-INT-09 « NE DOIT PAS — Statut normatif exact » (p. 225); EXIG-INT-20 « NE DOIT PAS — Qualification "AAIF" vérifiée » (p. 226); EXIG-ARC-18 « DEVRAIT — Écritures corrélées et idempotentes » (p. 224).
- **Diagnostic** : le registre se lit comme force + objet. SEC-14 se lit alors « ne doit pas injecter les secrets par le mandataire », soit le contraire du corps, qui impose (DOIT) l'injection par le mandataire et interdit (NE DOIT PAS) les secrets dans le bac à sable. ARC-18 en DEVRAIT laisse croire l'idempotence facultative, alors qu'EXIG-ORC-21 l'impose (ARC-18 ne vise en fait que la référence de trace). Plusieurs exigences mêlent les forces (SEC-14, ORC-04, ORC-26, INT-15, A2A-03, CON-02), et la colonne n'en montre qu'une. Les titres et les forces concordent par ailleurs exactement avec le corps (287 sur 287, vérifié par script).
- **Contre-exemple** : un relecteur de la grille d'homologation, qui ne travaille que sur le registre, coche SEC-14 « conforme » parce qu'aucun secret n'est injecté par le mandataire.
- **Correctif proposé** : formuler les titres de façon neutre ou en accord avec la force (« Aucun secret dans le bac à sable; injection par le mandataire », « Référence de trace sur chaque écriture »), et noter « DOIT / NE DOIT PAS » pour les exigences mixtes.
- **Confiance** : vérifié dans le texte

### [23-20] [MINEUR] Introduction du registre : forces et périmètre inexacts
- **Axe** : C
- **Localisation** : annexe D, p. 224 : « toutes les exigences normatives du cadre avec leur force (DOIT, DEVRAIT, PEUT) »; « sert de base [...] à la déclaration d'applicabilité ISO/IEC 42001 ».
- **Diagnostic** : aucune exigence en PEUT n'existe (vérifié), alors que NE DOIT PAS, employé 35 fois environ, n'est pas annoncé. « Toutes les exigences normatives » omet les PRIN-01 à PRIN-12 et les tableaux visés expressément, normatifs selon le § 1.4 (p. 13). La déclaration d'applicabilité rattache les exigences aux mesures de l'annexe A de la norme (§ 12.5), mais le registre ne comporte ni colonne de rattachement ni renvoi de section ou de page.
- **Contre-exemple** : une grille d'homologation bâtie sur le seul registre ignore PRIN-05 et les tableaux de plafonds visés.
- **Correctif proposé** : corriger la liste des forces, préciser « toutes les exigences EXIG », ajouter les colonnes section et mesure ISO/IEC 42001 (annexe A).
- **Confiance** : vérifié dans le texte

### [23-21] [MINEUR] Redondances non croisées dans le registre
- **Axe** : C
- **Localisation** : annexe D : ARC-06 / ORC-13 (points de contrôle protégés); ORC-28 / IAM-20 (coupe-circuit trimestriel); A2A-03 / SEC-19 (signature des cartes); ARC-01 / ARC-11 / IAM-17 (passage par la passerelle); CON-07 / AUT-22 (décisions automatisées).
- **Diagnostic** : les textes concordent pour l'essentiel (vérifié pour ARC-06/ORC-13 et A2A-03/SEC-19), mais divergent aux marges. CON-07 vise une décision « fondée exclusivement » sur un traitement automatisé, AUT-22 aussi celle qu'un agent « prépare sans révision humaine significative ». Le délai de 30 jours n'est que dans CON-07, la conservation d'un an que dans AUT-22. Le doublonnage multiplie les points de dérive à chaque révision (d'où [23-10], [23-17] et [23-18]).
- **Contre-exemple** : une révision de CON-07 qui n'atteint pas AUT-22 crée deux régimes pour la même décision.
- **Correctif proposé** : désigner une exigence maîtresse par sujet et réduire les autres à un renvoi, comme AUT-02 le fait déjà vers CON-02.
- **Confiance** : vérifié dans le texte

### [23-22] [MINEUR] Table de correspondance de l'annexe C : EXIG-IAM-11 attribuée à C.8
- **Axe** : C
- **Localisation** : tableau d'introduction de l'annexe C, p. 215-216 : « C.8 Enregistrement d'audit [...] EXIG-OBS-11, EXIG-OBS-12, EXIG-AUT-10, EXIG-IAM-11, EXIG-IAM-21 »; la lecture de C.8 (p. 223-224) n'invoque que OBS-12, IAM-21 et AUT-10.
- **Diagnostic** : rien dans C.8 ne met en œuvre l'audience unique (IAM-11). Le renvoi visait probablement IAM-18 (refus typés audités) ou OBS-13.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : remplacer IAM-11 par l'exigence visée, et faire citer OBS-11 dans la lecture de C.8.
- **Confiance** : déduit

## Points forts
- Exemples cryptographiquement exacts : h, arguments_sha256, clé d'idempotence, iat/exp (9 h 24 à 9 h 39 UTC, 900 s) et arithmétique (249,6 × 40 + 208 × 12 = 12 480; 41 200/50 000 = 0,824) se vérifient.
- Le registre concorde parfaitement avec le corps : 287 exigences, aucun trou, forces et titres identiques.
- C.8 distingue rigoureusement le minimum légal (RIA art. 12 et 26) du choix du cadre; l'enregistrement ne porte que des empreintes et des références.

## Questions pour l'audit bibliographique
- p. 224 : OWASP Top 10 for Agentic Applications 2026 [28] recommande-t-il expressément des journaux d'audit « immuables et signés »? Trancher sur le texte de l'entrée concernée.
- p. 224 : dates d'application RIA (annexe III le 2 décembre 2027, annexe I le 2 août 2028) et article 113 modifié par le règlement (UE) 2026/1744 : vérifier sur EUR-Lex, puisque [94] et [394] (Future of Life Institute) ne le portent peut-être pas.
- p. 224 : art. 26, par. 6 du RIA, « au moins six mois [...] durée adaptée à la destination » : vérifier la formulation du texte consolidé.
- p. 221 : RFC 9396, est-il admis d'employer authorization_details dans un JWT qui n'est ni une demande ni un jeton d'accès, avec des champs propres au type (fournisseur_id, montant_total_cad)? Vérifier au § 2 de la RFC (champs propres au type permis).
- p. 221 : CIBA Core 1.0 [310] produit des jetons d'identité ou d'accès, pas un « approbation+jwt ». Vérifier que le cadre présente bien l'émission du jeton d'approbation comme une étape propre au service d'approbation, et que binding_message peut porter h.
- p. 232 : OWASP Agentic AI Threats and Mitigations [87], T10 « Overwhelming Human in the Loop » : vérifier l'intitulé et le numéro.

audit_23.md : 22 constats (1 BLOQUANT, 10 MAJEUR, 11 MINEUR)
