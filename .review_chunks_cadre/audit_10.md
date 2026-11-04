# Audit chunk_10 — pages 91-102

## Synthèse
Le chunk couvre la fin du § 7.3 (choix du patron, EXIG-ORC-09-10), l'exécution durable (§ 7.4, ORC-11-14), la saga (§ 7.5, ORC-15-20), l'idempotence (§ 7.6, ORC-21-22), le contexte inter-agents (§ 7.7, ORC-23-25), la résilience (§ 7.8, ORC-26-28), les anti-patrons (§ 7.9, ORC-29) et le début du § 7.10 (ORC-30). L'ensemble est bien sourcé, honnête sur les « choix du cadre » et techniquement au-dessus de la moyenne, mais la thèse T3 (« ne jamais refaire une action terminée ») ne tient pas telle qu'elle est écrite. Les trois défauts les plus graves : (1) la compensation d'une étape à l'issue incertaine peut précéder l'effet tardif de l'original (ORC-16 est fausse sans mécanisme de clôture); (2) le coupe-circuit d'ORC-28 bloque « toute nouvelle étape » tout en exigeant des sagas « compensées », et IAM-20 révoque les identités qui serviraient à compenser; (3) les compensations et les réessais P3 entrent en collision avec l'approbation à usage unique de 15 minutes (AUT-09, AUT-12), et la figure 13 place un débit (P3) avant le pivot, à rebours d'ORC-15.

## Constats

### [10-01] [BLOQUANT] Compensation d'une étape incertaine : course avec l'original encore en vol
- **Axe** : A
- **Localisation** : § 7.5, EXIG-ORC-16, p. 96 : « Une étape dont l'issue est inconnue est traitée comme possiblement exécutée : sa compensation est déclenchée et reste sans effet si l'action n'a pas eu lieu. » Voir aussi la règle 2, p. 95.
- **Diagnostic** (premiers principes) : « issue inconnue » (délai expiré, plantage) ne veut pas dire « action terminée ou jamais commencée ». La requête d'origine peut encore être en file ou en traitement chez le service visé. Une compensation conditionnelle (« rembourser la transaction X si elle a été débitée ») évalue sa condition à l'instant t; si l'original s'exécute à t + ε, la compensation, déjà passée et sans effet, ne se rejoue pas. Le schéma est un TOCTOU classique. La garantie « reste sans effet si l'action n'a pas eu lieu » est exacte, mais elle ne couvre pas « aura lieu ». S'y ajoute une tension avec PRIN-12 (« En cas de doute, le système échoue en mode fermé : il s'arrête ou escalade plutôt que d'agir ») : ORC-16 fait au contraire agir automatiquement dans le doute.
- **Contre-exemple ou scénario de défaillance** : T3 « Débiter le client » expire au bout de 30 s; la passerelle de paiement traite la requête à 45 s. À 31 s, l'orchestrateur lance C3 « rembourser si débité » : rien n'est trouvé, donc aucun effet, et C3 est marquée faite. À 45 s, le débit passe. Le client est débité, la saga se croit compensée et aucune alerte ne part.
- **Correctif proposé** : avant de compenser une étape incertaine, exiger sa résolution : (a) relancer la requête d'origine avec la même clé d'idempotence jusqu'à obtenir un résultat définitif (succès mémorisé, 422 ou absence de traitement attestée), le 409 « en cours » valant attente et non feu vert; ou (b) poser côté service une pierre tombale sur la clé (annulation de la clé), qui garantit qu'un original tardif sera rejeté. Ajouter à ORC-22 : « le service DOIT permettre d'interroger ou de révoquer une clé ». Préciser le rapport avec PRIN-12.
- **Confiance** : déduit (raisonnement sur le texte; aucune sémantique de clôture n'est exigée nulle part dans le chunk)

### [10-02] [BLOQUANT] Coupe-circuit : « bloque toute nouvelle étape » contre sagas « compensées »
- **Axe** : A
- **Localisation** : § 7.8, EXIG-ORC-28, p. 100 : « L'arrêt bloque toute nouvelle étape, conserve l'état pour analyse et laisse les sagas en cours dans un état connu, suspendues ou compensées selon la procédure. »
- **Diagnostic** (premiers principes) : une compensation est une étape (elle est journalisée comme telle par ORC-16 et exécutée par l'orchestrateur). Si l'arrêt bloque toute nouvelle étape, aucune saga ne peut être « compensée » après l'arrêt. Le texte s'aggrave avec EXIG-IAM-20 (p. 130), qui, « en une seule action », « désactive l'identité de l'agent auprès du fournisseur d'identité et diffuse la révocation » : l'orchestrateur perd aussi les jetons nécessaires pour appeler les outils de remboursement ou de libération. Le cas d'une saga arrêtée entre le pivot et ses étapes réessayables n'est pas traité : le pivot est irréversible, les étapes en aval sont bloquées, et l'« état connu » est en fait incohérent.
- **Contre-exemple ou scénario de défaillance** : un incident d'injection déclenche le coupe-circuit global pendant que 200 sagas ont réservé du stock (T2) sans encore débiter. Toutes restent figées : le stock reste réservé, les verrous sémantiques (ORC-19) persistent et aucune compensation n'est permise. Si l'équipe lève l'arrêt pour compenser, elle réactive aussi l'agent compromis.
- **Correctif proposé** : distinguer un arrêt « vers l'avant » (aucune nouvelle étape métier) d'un canal de compensation exécuté sous une identité distincte de service de compensation, non révoquée par le coupe-circuit et limitée aux outils de compensation déclarés au catalogue. Exiger que, pour les sagas passées au pivot, les étapes réessayables puissent se terminer ou passent en file humaine. Aligner IAM-20 sur ce point.
- **Confiance** : vérifié dans le texte (ORC-28 p. 100, IAM-20 p. 130)

### [10-03] [MAJEUR] La figure 13 place un débit (P3) avant le pivot et avant l'approbation
- **Axe** : C (et A)
- **Localisation** : § 7.5, figure 13, p. 95 : « T3 ✗ échec Débiter le client non reprenable […] T4 · pivot Confirmation officielle irréversible · approbation »; « Le pivot T4 n'est atteint qu'après succès de T1 à T3. »
- **Diagnostic** (premiers principes) : le tableau 31 (p. 108) classe le « Virement » en P3, et l'annexe B (p. 215) écrit que « l'émission d'un paiement, de palier P3, exige toujours une approbation signée hors bande ». EXIG-ORC-15 (p. 96) exige que « toute étape de palier P3 […] se place au pivot ou après, une fois […] l'approbation humaine obtenue ». La figure de référence montre exactement l'inverse : un prélèvement financier externe exécuté avant le pivot et avant toute approbation. Le lecteur apprend donc le mauvais patron. Si l'auteur voulait un débit P2 (compensable par remboursement), la figure contredit le tableau 31.
- **Contre-exemple ou scénario de défaillance** : une équipe calque sa saga sur la figure. Le client est débité sans approbation, et le remboursement C3 (lui-même P3, voir 10-05) dépend d'une approbation qui n'arrivera pas à temps.
- **Correctif proposé** : faire du débit le pivot (ou le placer après une autorisation de paiement sans capture, compensable par annulation de l'autorisation, qui serait alors P2), et déplacer l'approbation avant cette étape. Ajouter au texte la règle de classement d'une préautorisation.
- **Confiance** : vérifié dans le texte (p. 95, 96, 108, 215)

### [10-04] [MAJEUR] Étapes postérieures au pivot : rien n'exige qu'elles réussissent à terme
- **Axe** : A
- **Localisation** : EXIG-ORC-15, p. 96 : « toute étape de palier P3 (action critique, externe ou irréversible) se place au pivot ou après »; principe p. 95 : « les transactions réessayables, idempotentes, qui la suivent jusqu'au terme ».
- **Diagnostic** (premiers principes) : la théorie de la saga (pivot de Microsoft et de Richardson) ne tient que si chaque étape postérieure au pivot réussit à terme par réessai. ORC-15 autorise au contraire plusieurs étapes P3 au pivot « ou après », sans exiger qu'elles soient réessayables jusqu'au succès. Après le pivot, un échec non transitoire n'a ni compensation (le pivot est irréversible) ni règle d'escalade : ORC-17 et ORC-18 ne visent que les compensations. Une ambiguïté s'y ajoute : « l'approbation humaine obtenue », au singulier, peut se lire comme une approbation par saga, alors qu'EXIG-AUT-09 exige une approbation « propre à cet appel » pour chaque P3.
- **Contre-exemple ou scénario de défaillance** : pivot = virement émis (P3); étape suivante = avis officiel au client (P3), refusé définitivement (adresse invalide). Le virement ne se défait pas, l'avis ne part pas, et aucune exigence ne dit quoi faire.
- **Correctif proposé** : exiger qu'une saga n'ait qu'un pivot; que toute étape postérieure soit idempotente, réessayable sans limite métier ou dotée d'une voie humaine nommée; et que chaque P3 reçoive sa propre approbation (renvoi explicite à AUT-09 et AUT-12). Ajouter un test « échec définitif après le pivot » à ORC-20.
- **Confiance** : vérifié dans le texte (absence de règle); théorie du pivot : déduit de la source [67] citée

### [10-05] [MAJEUR] Palier et approbation des compensations non définis
- **Axe** : A
- **Localisation** : EXIG-ORC-17, p. 96 : « Chaque compensation DOIT être idempotente et définie en termes métier (remboursement, avis rectificatif, libération de stock) »; règle 3, p. 95 : « on envoie un rectificatif ».
- **Diagnostic** (premiers principes) : un remboursement est un virement et un avis rectificatif est une « communication externe officielle » : deux exemples P3 du tableau 31 (p. 108). EXIG-AUT-09 interdit tout P3 sans approbation préalable propre à l'appel, et AUT-12 limite le jeton à 15 minutes et à un seul usage. Soit les compensations P3 échappent à l'approbation, et c'est une brèche dans PRIN-05; soit elles l'exigent, et ORC-16 (compensation « déclenchée » automatiquement) et ORC-18 (seuil de deux échecs) deviennent inapplicables pendant un incident où les approbateurs sont saturés.
- **Contre-exemple ou scénario de défaillance** : une panne de l'ERP déclenche 500 compensations « remboursement ». Chacune attend une approbation hors bande de 15 minutes au plus; les approbateurs ne suivent pas, les jetons expirent, ORC-18 compte des « échecs » et la file humaine déborde.
- **Correctif proposé** : déclarer au catalogue le palier de chaque outil de compensation; permettre une approbation préalable de la compensation, liée à l'empreinte de l'action d'origine et donnée au moment de l'approbation de la saga; ou classer explicitement la compensation exacte d'une action approuvée comme exemptée, sous plafond de montant.
- **Confiance** : vérifié dans le texte (p. 95-96, 108-111)

### [10-06] [MAJEUR] Dépendances et ordre des compensations : présupposés, jamais déclarés
- **Axe** : A
- **Localisation** : EXIG-ORC-18, p. 96 : « poursuivre les compensations qui n'en dépendent pas »; figure 13, p. 95 : « COMPENSATIONS (ORDRE INVERSE, IDEMPOTENTES) » et « compenser de k−1 à 1 »; règle 3 : « ne suit pas toujours l'ordre inverse exact et peut parfois s'exécuter en parallèle ».
- **Diagnostic** (premiers principes) : ORC-18 n'est applicable que si un graphe de dépendances entre compensations existe. Aucune exigence (ORC-15, ORC-16, catalogue § 6.8) n'oblige à le déclarer, et la figure impose l'ordre inverse que le texte relativise ensuite. Sans graphe, l'orchestrateur ne peut pas décider de manière déterministe quelles compensations « n'en dépendent pas ». Une suite de compensations ordonnée de k−1 à 1 n'est par ailleurs pas commutative en général (libérer le stock avant d'annuler un transport qui réserve ce stock).
- **Contre-exemple ou scénario de défaillance** : C2 (libérer le stock) échoue deux fois; C1 (annuler le transport) dépend-elle de C2? Rien ne le dit. Un orchestrateur exécute C1, un autre s'abstient : le comportement varie selon la mise en œuvre.
- **Correctif proposé** : exiger dans la définition de la saga un ordre de compensation déclaré (ordre inverse par défaut) et les dépendances explicites entre compensations, vérifiés par ORC-20.
- **Confiance** : vérifié dans le texte

### [10-07] [MAJEUR] La saga d'une chorégraphie n'a pas d'orchestrateur, or ORC-16 et ORC-18 en exigent un
- **Axe** : A
- **Localisation** : EXIG-ORC-08, p. 91 : « Une chorégraphie événementielle […] DOIT avoir un propriétaire de bout en bout […], une saga explicite (section 7.5) »; ORC-16, p. 96 : « l'orchestrateur DOIT consigner »; ORC-18 : « l'orchestrateur DOIT cesser de la relancer ».
- **Diagnostic** (premiers principes) : par définition, une chorégraphie n'a pas d'orchestrateur. Or le journal tenu avant l'action, le traitement de l'incertain et l'escalade après deux échecs sont tous attribués à « l'orchestrateur ». Un propriétaire inscrit au registre n'est pas un composant d'exécution. La figure 12 (p. 91) oriente vers la chorégraphie tout déclenchement par événement, ce qui rend le cas fréquent. Le constat exige les deux côtés de la couture (p. 91 et p. 96).
- **Contre-exemple ou scénario de défaillance** : trois consommateurs Kafka exécutent T1-T3 par réaction. T3 échoue : qui tient le journal corrélé, qui décide que l'issue est incertaine, qui compte les deux échecs de C2? Personne.
- **Correctif proposé** : soit exiger qu'une chorégraphie à effets multisystèmes ait un coordinateur de saga (orchestration de la seule saga), soit réécrire ORC-16 à ORC-18 en termes de « composant responsable de la saga » et préciser leur transposition à la chorégraphie (journal par participant, événements de compensation, moniteur de saga).
- **Confiance** : vérifié dans le texte

### [10-08] [MAJEUR] Verrou sémantique sans bail ni portée sur les écrivains hors saga
- **Axe** : B
- **Localisation** : § 7.5, p. 96 : « posent d'abord un verrou sémantique « réservation en attente », visible des autres sagas »; EXIG-ORC-19, p. 97 : « Lorsque plusieurs sagas ou agents peuvent modifier les mêmes enregistrements ».
- **Diagnostic** (premiers principes) : un verrou sémantique ne protège que contre les écrivains qui le respectent. Les humains dans l'ERP, les traitements en lot et les intégrations historiques l'ignorent, et ORC-19 ne les vise pas. Aucune exigence ne fixe non plus de durée ou de bail du verrou ni de propriétaire. Or ORC-18 envoie la saga en file humaine pour une durée indéterminée, ORC-28 la suspend, et LangGraph attend « sans limite » (p. 93). Le verrou devient un blocage durable.
- **Contre-exemple ou scénario de défaillance** : une saga réserve le dernier stock puis passe en file humaine un vendredi. Le verrou « réservation en attente » bloque toutes les ventes jusqu'au lundi, pendant que le module de vente au comptoir, hors saga, vend quand même l'article.
- **Correctif proposé** : élargir ORC-19 à tout écrivain du système d'enregistrement (anomalies documentées aussi pour les écrivains hors agent); exiger pour chaque verrou sémantique une échéance, un propriétaire et une procédure de libération en cas de suspension ou d'escalade.
- **Confiance** : déduit

### [10-09] [MAJEUR] Les quatre tests d'ORC-20 omettent le cas le plus dangereux
- **Axe** : B
- **Localisation** : EXIG-ORC-20, p. 97 : « échec forcé de chaque étape Tk […]; plantage entre l'écriture au journal et l'action; double exécution de chaque compensation; double échec d'une compensation ».
- **Diagnostic** (premiers principes) : le plantage entre le journal et l'action ne produit qu'une étape non exécutée, le cas facile. Le cas qui justifie la règle 2 (« Traiter l'incertain comme exécuté ») est le plantage ou le délai expiré après l'action et avant la consignation du résultat, et il n'est pas testé. Ne sont pas testés non plus : la course avec un original tardif (10-01), deux sagas concurrentes sur le même enregistrement (ORC-19), l'échec après le pivot (10-04), l'arrêt par coupe-circuit en pleine saga (10-02) et le plantage pendant une compensation. Les doublures ne reproduisent pas le comportement réel d'idempotence du service visé, que seul ce service connaît (Pourquoi d'ORC-22).
- **Contre-exemple ou scénario de défaillance** : une saga réussit les quatre tests. En production, un délai expiré sur un débit réussi déclenche une compensation pendant qu'un réessai double le débit : ce chemin n'avait jamais été exercé.
- **Correctif proposé** : ajouter au minimum les tests « effet réalisé, résultat perdu », « original tardif après compensation », « sagas concurrentes », « échec après le pivot » et « arrêt en cours de saga »; exiger un test de contrat d'idempotence contre l'environnement d'essai réel du service.
- **Confiance** : vérifié dans le texte

### [10-10] [MAJEUR] Un plafond atteint en cours de saga interdit la compensation qu'il rend nécessaire
- **Axe** : A
- **Localisation** : EXIG-ORC-26, p. 100 : « L'atteinte d'un plafond DOIT arrêter la boucle en état sûr et déclencher l'escalade prévue ».
- **Diagnostic** (premiers principes) : en pleine saga, le seul « état sûr » s'obtient par compensation, qui consomme des appels d'outils, de la durée et parfois des jetons. Si le plafond d'appels d'outils ou de coût est atteint, la compensation dépasse le plafond, et aucune réserve n'est prévue. Le plafond de « durée totale » ne précise pas s'il inclut l'attente humaine : ORC-11 et § 7.4 envisagent une attente d'approbation de trois jours, et LangGraph attend « sans limite ». Les réessais (ORC-27) comptent-ils dans le plafond? Non précisé (voir 10-19).
- **Contre-exemple ou scénario de défaillance** : plafond de 10 appels d'outils atteint après T1 à T3. L'arrêt « en état sûr » laisserait T1 et T2 non compensées; les compenser porte le total à 12, au-delà du plafond.
- **Correctif proposé** : réserver un budget de compensation distinct, non soumis au plafond d'exécution; préciser que la durée totale exclut (ou inclut, avec valeur distincte) l'attente humaine; préciser le décompte des réessais.
- **Confiance** : déduit

### [10-11] [MAJEUR] Aucune durée de conservation des clés d'idempotence
- **Axe** : A
- **Localisation** : EXIG-ORC-22, p. 98 : « un doublon ne produit aucun effet supplémentaire; une clé réutilisée avec des arguments différents est rejetée ».
- **Diagnostic** (premiers principes) : la déduplication n'est garantie que pendant la durée de conservation des clés par le service. Le brouillon IETF cité prévoit une expiration des clés : à confirmer par l'audit bibliographique, mais toute mise en œuvre réelle purge les clés. Les exécutions du cadre peuvent durer des jours (approbation de trois jours, interrupt() « sans limite », Temporal « sans limite de durée », Step Functions jusqu'à un an, p. 102). Un réessai, une reprise ou une compensation postérieure à la purge réexécute l'effet.
- **Contre-exemple ou scénario de défaillance** : le service garde les clés 24 heures. Une saga reprend 72 heures après une approbation et rejoue T2 avec la même clé : la clé a été purgée, le stock est réservé deux fois.
- **Correctif proposé** : exiger que la conservation déclarée de la clé au catalogue soit supérieure ou égale à la durée maximale d'une exécution (plafond ORC-26) augmentée de la fenêtre de compensation, et que l'orchestrateur refuse de reprendre une étape au-delà de cette fenêtre sans résolution explicite.
- **Confiance** : déduit; expiration prévue par le brouillon : à vérifier (source externe)

### [10-12] [MAJEUR] La sémantique de step_id ne couvre ni les boucles, ni la replanification après issue incertaine, ni les bifurcations
- **Axe** : A
- **Localisation** : § 7.6, p. 97 : « étape replanifiée avec d'autres valeurs → nouveau step_id, donc nouvelle clé »; ORC-21, p. 98 : « Une étape replanifiée avec d'autres arguments reçoit un nouvel identifiant d'étape, donc une nouvelle clé. »
- **Diagnostic** (premiers principes) : trois trous. (1) Les itérations légitimes (boucle évaluateur-optimiseur à trois itérations, LoopAgent) : si step_id n'inclut pas l'indice d'itération, la deuxième exécution voulue est absorbée comme doublon ou rejetée en 422. (2) La replanification après une issue incertaine : l'ancienne étape a peut-être produit son effet, la nouvelle clé en produit un second, et rien n'exige de compenser ou de résoudre l'ancienne avant de replanifier. (3) Le « voyage dans le temps » de LangGraph (p. 94) bifurque avec les mêmes task_id et step_id : la branche corrigée est soit dédupliquée à tort, soit rejetée.
- **Contre-exemple ou scénario de défaillance** : « réserver 10 unités » expire (issue incertaine); le planificateur replanifie « réserver 12 unités » sous un nouveau step_id. Résultat : 22 unités réservées, ou 10 réservées et jamais libérées.
- **Correctif proposé** : définir step_id comme (chemin dans le plan, indice d'itération, numéro de bifurcation); interdire la replanification d'une étape incertaine avant sa résolution (10-01); traiter une bifurcation comme une nouvelle tâche (nouveau task_id) ou un nouvel espace de clés.
- **Confiance** : déduit

### [10-13] [MAJEUR] Déduplication « par son adaptateur » contre le Pourquoi « seul le système visé sait »
- **Axe** : A
- **Localisation** : EXIG-ORC-22, p. 98 : « DOIT vérifier la clé côté serveur, directement ou par son adaptateur »; Pourquoi : « seul le système visé sait si l'effet a déjà eu lieu ».
- **Diagnostic** (premiers principes) : un adaptateur qui enregistre la clé puis appelle un système non idempotent n'est pas atomique avec l'effet. S'il plante entre l'appel et l'enregistrement du résultat, il ne sait pas si l'effet a eu lieu, exactement ce que le Pourquoi reconnaît. L'option « par son adaptateur » réintroduit donc le problème qu'elle prétend résoudre, sauf si l'adaptateur écrit dans la même transaction que le système visé.
- **Contre-exemple ou scénario de défaillance** : l'adaptateur MCP d'un ERP enregistre la clé K « en cours », appelle l'API de l'ERP, qui crée la commande, puis plante. Au réessai, K est « en cours » : 409 sans fin, ou purge de K et seconde commande.
- **Correctif proposé** : n'admettre l'adaptateur que s'il écrit la clé dans la même transaction que l'effet, ou s'il peut interroger le système visé par une référence externe portée par l'effet (numéro de commande dérivé de la clé); sinon, classer l'outil P3 (non idempotent).
- **Confiance** : déduit

### [10-14] [MAJEUR] Réessai d'un appel P3 contre un jeton d'approbation à usage unique de 15 minutes
- **Axe** : A
- **Localisation** : ORC-21, p. 98 : « une clé d'idempotence […] réutilisée telle quelle à chaque réessai »; ORC-12, p. 94 : « dans une étape réessayable »; contre EXIG-AUT-12, p. 111 : « vérifier la signature, l'expiration et l'usage unique […]. Le jeton DOIT expirer au plus 15 minutes ».
- **Diagnostic** (premiers principes) : la passerelle consomme le jeton d'approbation au premier essai. Si cet essai expire (issue incertaine), le réessai avec la même clé d'idempotence est refusé par la passerelle (jeton déjà utilisé) avant même d'atteindre le service, qui seul pourrait dire « déjà fait ». Après une reprise sur panne de plus de 15 minutes, le jeton est expiré. Le cadre ne dit pas si le réessai d'un P3 exige une nouvelle approbation; s'il l'exige, l'approbateur reçoit deux demandes pour la même action, un terreau d'approbation machinale (§ 8.7). Conserver le jeton dans le point de contrôle pour la reprise le place aussi dans un magasin d'état, ce qui heurte l'esprit d'IAM-06.
- **Contre-exemple ou scénario de défaillance** : le virement approuvé expire côté réseau; le réessai est rejeté pour « jti déjà consommé ». La saga traite l'issue comme incertaine et compense par un remboursement d'un virement peut-être émis, compensation elle-même P3 (10-05).
- **Correctif proposé** : faire porter l'usage unique par le couple (jti, clé d'idempotence) : un réessai de la même clé et de la même empreinte h reste admis pendant la fenêtre, et le service répond par son résultat mémorisé. Décrire explicitement le réessai P3 dans ORC-21 et AUT-12.
- **Confiance** : vérifié dans le texte (p. 98, 111); conséquence : déduit

### [10-15] [MAJEUR] ORC-12 : « sinon, déplacé après le point de pause » ne règle pas le réessai
- **Axe** : A
- **Localisation** : EXIG-ORC-12, p. 94 : « Tout effet de bord placé avant un point de pause ou dans une étape réessayable DOIT être idempotent; sinon, il DOIT être déplacé après le point de pause. »
- **Diagnostic** (premiers principes) : déplacer un effet après un point de pause règle la réexécution du nœud interrompu (LangGraph), mais pas celle d'une étape réessayable (activité Temporal), qui reste réessayable où qu'elle se trouve. Le code placé après un interrupt() se réexécute lui aussi si le nœud échoue ensuite ou si le nœud contient plusieurs interrupt(). L'échappatoire contredit aussi ORC-21 et ORC-22, qui exigent une clé pour toute écriture P2 ou P3 sans alternative.
- **Contre-exemple ou scénario de défaillance** : un envoi de notification non idempotent est placé après l'interrupt(); une erreur réseau plus loin dans le même nœud provoque un réessai du nœud, et la notification part deux fois.
- **Correctif proposé** : « Tout effet de bord DOIT être idempotent ou isolé dans une étape journalisée exécutée au plus une fois; l'emplacement par rapport au point de pause ne dispense pas de cette règle. »
- **Confiance** : déduit (comportement LangGraph décrit p. 93 par le cadre lui-même)

### [10-16] [MAJEUR] La granularité « après chaque transition » dépasse celle des cadriciels présentés comme conformes
- **Axe** : A
- **Localisation** : EXIG-ORC-11, p. 94 : « persiste l'état après chaque transition (appel de modèle, appel d'outil, décision, réponse humaine) »; § 7.4, p. 93 : Microsoft Agent Framework « crée un point de contrôle à la fin de chaque étape de calcul du flux ».
- **Diagnostic** (premiers principes) : LangGraph et Microsoft Agent Framework persistent par super-étape ou par nœud, pas par appel de modèle ou d'outil à l'intérieur d'un nœud ou d'un exécuteur d'agent. Un exécuteur d'agent qui enchaîne plusieurs appels de modèle et d'outils dans une seule étape ne satisfait pas ORC-11 sans redécoupage. Le tableau 27 (p. 101-102) présente pourtant ces produits comme des atouts au regard du cadre, sans signaler l'écart.
- **Contre-exemple ou scénario de défaillance** : un exécuteur d'agent MAF effectue cinq appels d'outils dans une super-étape et plante au quatrième. La reprise rejoue les cinq; les trois écritures déjà faites ne sont protégées que par les clés d'idempotence, et les lectures coûteuses sont refaites.
- **Correctif proposé** : soit exiger qu'un appel non déterministe soit son propre nœud ou sa propre activité (renvoi à ORC-12), soit réécrire ORC-11 en « après chaque étape journalisée », et l'indiquer dans les « Points d'attention » du tableau 27.
- **Confiance** : déduit (granularité de MAF : celle que le cadre décrit p. 93; LangGraph : à vérifier dans la documentation)

### [10-17] [MAJEUR] ORC-11 sans proportionnalité : tout flux de plus d'une étape exige un moteur durable
- **Axe** : B
- **Localisation** : EXIG-ORC-11, p. 94 : « Tout flux de plus d'une étape, ou susceptible d'attendre une approbation, DOIT s'exécuter sur un moteur d'exécution durable ».
- **Diagnostic** (premiers principes) : un agent N1 en lecture P0-P1 qui fait deux appels d'outil pour répondre à une question est un « flux de plus d'une étape ». Il devrait persister son état après chaque appel de modèle, ce qui ajoute latence, coût et RP stockés (ORC-13) pour un gain nul : relancer depuis le début ne produit aucun double effet. L'exigence ignore le palier (P0-P1 sans effet), la classe et la durée, contrairement à PRIN-08 (« simplicité d'abord »).
- **Contre-exemple ou scénario de défaillance** : un assistant de recherche documentaire interne, 300 ms par tour, doit écrire dans PostgreSQL après chaque appel de modèle; la latence et le volume de RP persistés augmentent sans réduire aucun risque.
- **Correctif proposé** : limiter le DOIT aux flux qui comportent au moins une étape P2 ou P3, une attente humaine, ou une durée supérieure à un seuil déclaré; DEVRAIT ailleurs.
- **Confiance** : vérifié dans le texte

### [10-18] [MAJEUR] ORC-14 : une version ancienne maintenue sans borne, même vulnérable
- **Axe** : B
- **Localisation** : EXIG-ORC-14, p. 94 : « DEVRAIT laisser chaque exécution en cours se terminer sur la version avec laquelle elle a commencé ».
- **Diagnostic** (premiers principes) : le texte ne prévoit ni durée maximale de cohabitation des versions, ni exception de sécurité (correctif d'injection, vulnérabilité d'un outil), ni le cas d'un modèle retiré par le fournisseur en cours d'exécution, ni l'articulation avec le retrait ou la suspension (§ 11.5) et avec le coupe-circuit. Avec des attentes « sans limite » (p. 93), l'entreprise doit maintenir des versions déployées pendant des semaines.
- **Contre-exemple ou scénario de défaillance** : une version 2.3.0 vulnérable à une injection est corrigée en 2.3.1; 40 exécutions en attente d'approbation reprennent sur la 2.3.0 et exécutent l'action injectée.
- **Correctif proposé** : borner la cohabitation des versions (plafond de durée ORC-26); prévoir que le retrait de sécurité d'une version force la suspension ou la migration testée des exécutions en cours.
- **Confiance** : déduit

### [10-19] [MAJEUR] Réessais : ni gigue, ni budget global, ni borne de tentatives, ni décompte dans les plafonds
- **Axe** : B
- **Localisation** : EXIG-ORC-27, p. 100 : « des réessais à temporisation exponentielle (exponential backoff) limités aux erreurs transitoires et un disjoncteur »; p. 93 : « Temporal réessaie les activités en échec[79] ».
- **Diagnostic** (premiers principes) : (1) Sans gigue (jitter), les clients se resynchronisent après une panne du fournisseur et créent une tempête de réessais. (2) Les réessais s'empilent par couche (SDK du modèle, passerelle de modèles, activité Temporal, passerelle d'agents, sous-agent) : k couches de n essais donnent nᵏ appels. (3) La politique de réessai par défaut des activités Temporal est, sauf erreur de ma part, sans limite de tentatives; chaque tentative d'une activité « invocation d'agent » consomme des jetons. (4) ORC-26 ne dit pas si les réessais comptent dans les plafonds.
- **Contre-exemple ou scénario de défaillance** : panne de 10 minutes du fournisseur de modèle. Trois couches de cinq réessais donnent 125 appels par requête, synchronisés à chaque palier de temporisation; à la reprise, le pic de facturation et la saturation du quota empêchent le retour à la normale.
- **Correctif proposé** : exiger la gigue, une seule couche propriétaire des réessais par dépendance (les autres à zéro), un nombre de tentatives borné et déclaré, un budget de réessai global et le décompte des réessais dans les plafonds d'ORC-26.
- **Confiance** : déduit; politique Temporal par défaut : à vérifier (source externe)

### [10-20] [MAJEUR] Le jeton délégué dans le message de délégation contre EXIG-IAM-06
- **Axe** : C (et A)
- **Localisation** : EXIG-ORC-23, p. 99 : « DOIT transmettre un message structuré limité au sous-objectif, […] au jeton délégué du mandant (section 9.3) »; exemple p. 98 : « "jeton_delegue": "<jeton délégué du mandant, audience = agent-credit>" ».
- **Diagnostic** (premiers principes) : EXIG-IAM-06 (p. 121) écrit que « aucun jeton, certificat ni secret n'entre dans le contexte du modèle, dans la mémoire de l'agent, dans les arguments d'un outil ou dans les traces ». Placer le jeton dans le corps du message de délégation l'expose dès que l'exécutant est un agent utilisé comme outil (le message devient des arguments d'outil, p. 102), dès que le message entre dans le contexte du modèle exécutant, et dès qu'il est persisté dans un point de contrôle (ORC-13 : « y compris les messages en attente ») ou dans le journal d'ORC-16 (« ses arguments »). Le « contenu logique indépendant du protocole » ne dit pas où le jeton voyage réellement.
- **Contre-exemple ou scénario de défaillance** : l'orchestrateur appelle l'agent de crédit comme outil (OpenAI Agents SDK); le message, jeton compris, se retrouve dans le contexte du modèle de l'exécutant, puis dans le point de contrôle PostgreSQL et la trace. Une injection dans un état financier fait recopier le jeton dans la sortie.
- **Correctif proposé** : retirer le jeton du message logique; exiger qu'il voyage dans l'en-tête d'authentification du transport (A2A, MCP), injecté et retiré par le code d'exécution ou la passerelle, et qu'il soit exclu des points de contrôle et des journaux. Corriger l'exemple.
- **Confiance** : vérifié dans le texte (p. 98-99, 121)

### [10-21] [MAJEUR] Le message de délégation, limité par une liste fermée, exclut les identifiants qu'exige ORC-21
- **Axe** : A
- **Localisation** : EXIG-ORC-23, p. 99 : « limité au sous-objectif, aux critères d'acceptation, aux paramètres requis, aux références d'artefacts, au jeton délégué […], au contexte de trace […], au budget restant et au schéma de retour »; ORC-21, p. 98 : « dérivée de l'identifiant de la tâche et de celui de l'étape ».
- **Diagnostic** (premiers principes) : l'exécutant doit dériver des clés d'idempotence stables d'un réessai à l'autre de la délégation. Il ne reçoit pourtant ni task_id ni step_id ni clé parente, et le traceparent change de span-id à chaque essai. Si l'orchestrateur réessaie la délégation, l'exécutant génère de nouvelles clés et double ses écritures. La liste fermée (« limité au ») omet aussi le palier maximal autorisé et le niveau d'autonomie, que l'exécutant ne peut alors pas appliquer de lui-même (la portée du jeton peut en tenir lieu, mais rien ne le dit).
- **Contre-exemple ou scénario de défaillance** : délégation « réserver le stock » à un sous-agent; la réponse se perd et l'orchestrateur réessaie. Le sous-agent attribue un nouveau task_id, donc de nouvelles clés, et réserve deux fois.
- **Correctif proposé** : ajouter à la liste d'ORC-23 l'identifiant de la tâche parente et de l'étape de délégation (ou une clé d'idempotence de délégation dont l'exécutant dérive les siennes), stables d'un réessai à l'autre, ainsi que le plafond de palier.
- **Confiance** : vérifié dans le texte (liste fermée); conséquence : déduit

### [10-22] [MAJEUR] Contexte minimal en DOIT contre découpage par frontières de contexte en DEVRAIT
- **Axe** : C
- **Localisation** : EXIG-ORC-10, p. 93, Pourquoi : « un transfert qui ne passe que des messages, sans la trace complète, fait perdre des décisions implicites »; ORC-23, p. 99 : « L'historique brut complet NE DOIT PAS être transmis »; § 7.7, p. 98 : « Le contexte minimal convient donc surtout aux tâches de lecture; une tâche à fortes dépendances reste à un seul agent ».
- **Diagnostic** (premiers principes) : la protection contre la perte de décisions implicites (ne pas scinder une tâche couplée) n'est qu'un DEVRAIT (ORC-10), et la nuance « surtout aux tâches de lecture » n'apparaît dans aucune exigence. L'interdiction de transmettre l'historique est en revanche un DOIT universel. Le cadre peut donc exiger la scission (ORC-09) puis interdire le contexte qui rendrait la scission sûre. Le Pourquoi d'ORC-10 justifie d'ailleurs l'inverse de ce qu'exige ORC-23.
- **Contre-exemple ou scénario de défaillance** : une tâche de rédaction et de mise à jour couplée est répartie entre deux agents, en écart au seul DEVRAIT d'ORC-10. ORC-23 empêche de transmettre les décisions de l'orchestrateur, et l'exécutant écrit des valeurs contradictoires, comme le décrit Cognition [276].
- **Correctif proposé** : promouvoir en DOIT la règle « une tâche d'écriture à fortes dépendances reste à un seul agent », ou admettre dans ORC-23 la transmission d'un registre structuré des décisions prises (sans l'historique brut).
- **Confiance** : vérifié dans le texte

### [10-23] [MAJEUR] Journal de compensation : arguments en clair, en ajout seul, sans conservation ni lien avec le journal d'audit
- **Axe** : B (et C)
- **Localisation** : EXIG-ORC-16, p. 96 : « consigner dans un journal durable, en ajout seul et corrélé à la trace, l'étape, ses arguments, sa clé d'idempotence et la compensation ».
- **Diagnostic** (premiers principes) : ce second journal en ajout seul stocke des arguments en clair, qui contiennent souvent des RP (montant et identifiant du client). EXIG-OBS-12 (p. 151) écrit au contraire que « les arguments d'outil n'y figurent que par leur empreinte SHA-256 » dans le journal d'audit, et ORC-13 impose chiffrement, accès restreint et élagage aux points de contrôle. ORC-16 n'impose rien de tel : ni chiffrement, ni droits d'accès, ni durée de conservation, ni destruction (EXIG-CON-10), et il ne précise pas s'il se confond avec le journal d'audit (OBS-11) ou avec l'historique du moteur (Temporal). Un journal en ajout seul se prête mal à la destruction à l'échéance qu'exige la Loi 25.
- **Contre-exemple ou scénario de défaillance** : un journal en ajout seul de 24 mois contient numéros de client, montants et adresses en clair, hors du calendrier de conservation, que l'équipe d'exploitation lit sans les contrôles du journal d'audit.
- **Correctif proposé** : soumettre le journal de compensation aux contrôles d'ORC-13 (accès, chiffrement, conservation, élagage à la clôture de la saga plus un délai), et préciser son rapport avec OBS-11 et avec l'historique du moteur durable (lequel tient lieu de l'autre).
- **Confiance** : vérifié dans le texte (p. 96, 151)

### [10-24] [MAJEUR] ORC-30 ne fait pas démontrer les capacités propres au chapitre 7
- **Axe** : C
- **Localisation** : EXIG-ORC-30, p. 102 : « la persistance durable des points de contrôle et la reprise après panne; la pause pour approbation humaine sans perte d'état; l'émission de traces OpenTelemetry […]; la prise en charge de MCP et d'A2A […]; l'export ».
- **Diagnostic** (premiers principes) : la preuve de concept omet les capacités que le chapitre rend obligatoires et que les produits ne fournissent pas tous : propagation d'une clé d'idempotence stable (ORC-21), compensation et escalade de saga (ORC-15 à 18), plafonds par exécution (ORC-26), coupe-circuit ciblé et global (ORC-28), cohabitation des versions (ORC-14), granularité de persistance d'ORC-11 (10-16). Un produit peut donc être inscrit au catalogue puis se révéler incapable de satisfaire ORC-26 ou ORC-28. Ce constat exige les deux côtés de la couture (p. 94-100 et p. 102).
- **Contre-exemple ou scénario de défaillance** : une plateforme SaaS réussit la preuve de concept d'ORC-30, mais n'offre ni plafond de coût par exécution ni arrêt ciblé d'un outil; l'écart n'apparaît qu'à l'homologation de l'agent.
- **Correctif proposé** : ajouter à ORC-30 la démonstration des plafonds, du coupe-circuit, de la propagation de la clé d'idempotence et des compensations, ou renvoyer explicitement aux tests d'ORC-20.
- **Confiance** : vérifié dans le texte

### [10-25] [MINEUR] Clé dérivée : entropie de l'exemple et séparateur ambigu
- **Axe** : A
- **Localisation** : § 7.6, p. 97 : « task_id = "tache-7f3c2a" » et « cle = hex( SHA-256( task_id + "|" + step_id ) ) ».
- **Diagnostic** (premiers principes) : le hachage n'ajoute aucune entropie. Avec un task_id de 6 caractères hexadécimaux (24 bits), comme dans l'exemple, la clé est devinable, alors que le brouillon met en garde contre les clés à faible entropie (le texte le rappelle). Une clé prévisible permet à un tiers de préempter une clé (422 ou 409 opposés à la requête légitime) si le service ne cloisonne pas les clés par client. La concaténation avec « | » est ambiguë si un identifiant contient « | » : ("a|b","c") et ("a","b|c") donnent la même clé. Le cadre emploie ailleurs la RFC 8785 pour les empreintes (OBS-12), mais pas ici.
- **Contre-exemple ou scénario de défaillance** : deux couples distincts (task_id, step_id) produisent la même clé; la seconde écriture est rejetée en 422 ou absorbée comme doublon.
- **Correctif proposé** : exiger un task_id aléatoire d'au moins 122 bits (UUIDv4) et un encodage non ambigu (préfixes de longueur ou tableau JSON canonisé RFC 8785); exiger le cloisonnement des clés par client côté service.
- **Confiance** : vérifié dans le texte (exemple); risque : déduit

### [10-26] [MINEUR] « Logique de coordination déterministe » non définie
- **Axe** : C
- **Localisation** : EXIG-ORC-12, p. 94 : « La logique de coordination DOIT rester déterministe ».
- **Diagnostic** (premiers principes) : dans les patrons agent unique et orchestrateur-exécutants, c'est le modèle qui choisit l'étape suivante. Le texte ne précise pas qu'il faut entendre « déterministe à résultats journalisés égaux », c'est-à-dire le déterminisme de rejeu de Temporal. LangGraph, fondé sur des points de contrôle plutôt que sur le rejeu, n'a pas cette contrainte. Lu à la lettre, ORC-12 interdirait les patrons autorisés du § 7.2.
- **Contre-exemple ou scénario de défaillance** : un réviseur refuse un orchestrateur qui laisse le modèle choisir l'exécutant suivant, au motif que la coordination n'est pas déterministe.
- **Correctif proposé** : « déterministe une fois relus les résultats journalisés des appels non déterministes ».
- **Confiance** : vérifié dans le texte

### [10-27] [MINEUR] Magasin en mémoire limité au « poste de développement » : l'intégration continue est exclue
- **Axe** : B
- **Localisation** : EXIG-ORC-11, p. 94 : « Un magasin en mémoire NE DOIT PAS être utilisé hors du poste de développement. »
- **Diagnostic** (premiers principes) : la formule interdit InMemorySaver en intégration continue, dans les environnements éphémères d'essai et pour les doublures d'ORC-20, des usages légitimes et sans risque. L'intention est « hors production ».
- **Contre-exemple ou scénario de défaillance** : une chaîne d'intégration continue qui exécute les tests d'ORC-20 avec un magasin en mémoire est non conforme.
- **Correctif proposé** : « NE DOIT PAS être utilisé en production ni dans un environnement qui traite des données réelles ».
- **Confiance** : vérifié dans le texte

### [10-28] [MINEUR] ORC-13 : attribution contradictoire et cas des états modifiés à dessein
- **Axe** : C
- **Localisation** : EXIG-ORC-13, p. 94, Pourquoi : « (constat du cadre, non tiré de la source)[105] »; corps : « NE DOIT PAS charger de point de contrôle d'origine non vérifiée ».
- **Diagnostic** (premiers principes) : appeler [105] pour un énoncé déclaré « non tiré de la source » brouille la traçabilité : la partie sourcée n'est pas distinguée de la partie propre au cadre. Par ailleurs, le voyage dans le temps (p. 94) prévoit de « bifurquer après correction de l'état » : un état modifié par une personne est par construction d'une origine autre que l'orchestrateur, et le texte ne dit pas comment il devient « vérifié » (signature de l'opérateur, journal).
- **Contre-exemple ou scénario de défaillance** : un opérateur corrige l'état par update_state; le contrôle d'intégrité échoue et l'orchestrateur refuse la reprise, ou l'équipe désactive le contrôle.
- **Correctif proposé** : séparer la phrase sourcée de la phrase du cadre; exiger que toute modification manuelle d'état soit re-signée par le service et journalisée en audit.
- **Confiance** : vérifié dans le texte

### [10-29] [MINEUR] Temporal « sans limite de durée » : limites d'historique et de charge utile passées sous silence
- **Axe** : B
- **Localisation** : § 7.4, p. 93 : « Temporal garantit qu'une exécution de flux se poursuit jusqu'à son terme, sans limite de durée imposée »; tableau 27, p. 102.
- **Diagnostic** (premiers principes) : sans limite de durée, mais un historique d'événements borné (de l'ordre de 50 000 événements ou 50 Mo, d'après mes connaissances) et une charge utile bornée (de l'ordre de 2 Mo). Les invocations d'agent journalisées comme activités (p. 93) stockent invites et réponses dans l'historique : une longue boucle agentique ou un gros contexte atteint ces limites et exige Continue-As-New ou des références à des artefacts.
- **Contre-exemple ou scénario de défaillance** : un agent documentaire renvoie une synthèse de 3 Mo comme résultat d'activité; le flux échoue.
- **Correctif proposé** : mentionner ces limites dans les « Points d'attention » de Temporal et exiger le passage par référence (magasin d'artefacts, ORC-24) pour les résultats volumineux.
- **Confiance** : à vérifier (source externe : documentation Temporal, « Limits »)

### [10-30] [MINEUR] ORC-16 « avant chaque étape » vise aussi les lectures
- **Axe** : C
- **Localisation** : EXIG-ORC-16, p. 96 : « Avant chaque étape, l'orchestrateur DOIT consigner […] la compensation à exécuter. »
- **Diagnostic** (premiers principes) : une étape de lecture (P0, P1) n'a ni clé d'idempotence (ORC-21 ne vise que P2 et P3) ni compensation. Le libellé impose une écriture de journal vide à chaque lecture.
- **Contre-exemple ou scénario de défaillance** : un vérificateur juge non conforme une saga qui ne journalise pas ses lectures.
- **Correctif proposé** : « Avant chaque étape d'écriture (P2 ou P3) ».
- **Confiance** : vérifié dans le texte

### [10-31] [MINEUR] ORC-18 : l'unité de décompte de « deux échecs » est ambiguë
- **Axe** : C
- **Localisation** : EXIG-ORC-18, p. 96 : « Lorsqu'une même compensation échoue deux fois de suite (erreur non transitoire ou politique de réessai épuisée) ».
- **Diagnostic** (premiers principes) : un « échec » est-il une tentative ou l'épuisement d'une politique de réessai? Dans le second cas, deux échecs valent 2 × n tentatives; dans le cas d'une erreur non transitoire, relancer une seconde fois est inutile (Temporal, cité, recommande de poursuivre et d'alerter dès l'erreur non réessayable). La figure 13 (« 2 échecs d'une compensation ») ne tranche pas.
- **Contre-exemple ou scénario de défaillance** : deux équipes mettent en œuvre ORC-18 avec des décomptes différents (2 tentatives contre 10); ORC-20 (« double échec ») est réussi dans les deux cas.
- **Correctif proposé** : « une erreur non transitoire, ou deux épuisements successifs de la politique de réessai déclarée ».
- **Confiance** : vérifié dans le texte

### [10-32] [MINEUR] ORC-09 : décompte des outils, « chevauchement » et critère de décision indéfinis
- **Axe** : B
- **Localisation** : EXIG-ORC-09, p. 93 : « Dès qu'un agent dépasse 15 outils […], ou dès que des outils se chevauchent, l'équipe DOIT mesurer la précision de sélection ».
- **Diagnostic** (premiers principes) : (1) Compte-t-on les outils au catalogue de l'agent ou ceux chargés au début du tour? Avec le chargement à la demande que l'exigence recommande, la réponse change. (2) « se chevauchent » n'est pas défini : presque tout jeu d'outils se chevauche en partie, et l'exigence devient universelle. (3) Aucun seuil de précision ne dit quand la consolidation a « réussi » et quand scinder devient justifié. La « plage de 15 à 20 » est construite par le cadre à partir de sources qui disent « moins de 20 » et « plus de 15 avec succès » (p. 92).
- **Contre-exemple ou scénario de défaillance** : un agent à 40 outils chargés à la demande (3 visibles par tour) est-il au-delà du seuil? Deux revues répondent différemment.
- **Correctif proposé** : compter les outils « disponibles au début d'un tour »; définir le chevauchement (p. ex. descriptions dont la confusion est mesurée sur le jeu d'évaluation); fixer un seuil de précision déclaré à la fiche.
- **Confiance** : vérifié dans le texte

### [10-33] [MINEUR] Le champ « echeance » contient une durée (« PT10M »)
- **Axe** : C
- **Localisation** : § 7.7, p. 98 : « "echeance": "PT10M" ».
- **Diagnostic** (premiers principes) : une échéance est un instant; PT10M est une durée ISO 8601 dont le point de départ n'est pas défini (émission, réception ou sortie de file). Une durée relative propagée d'un saut à l'autre s'allonge à chaque file d'attente.
- **Contre-exemple ou scénario de défaillance** : le message attend 8 minutes en file; l'exécutant croit disposer de 10 minutes alors qu'il n'en reste que 2 au budget de l'orchestrateur.
- **Correctif proposé** : « "echeance": "2026-10-27T14:13:12Z" » (instant absolu), ou renommer le champ « duree_max » et en préciser l'origine.
- **Confiance** : vérifié dans le texte

### [10-34] [MINEUR] ORC-25 : filtrer « selon les droits du mandant » n'est pas testable pour les contenus dérivés
- **Axe** : B
- **Localisation** : EXIG-ORC-25, p. 99 : « Chaque agent DOIT filtrer ses résultats selon les droits du mandant, de sorte qu'aucune donnée inaccessible à ce mandant ne remonte ».
- **Diagnostic** (premiers principes) : le filtrage se vérifie pour des enregistrements, pas pour une synthèse rédigée par le modèle qui intègre une inférence tirée d'une donnée inaccessible. Si les droits effectifs sont déjà l'intersection mandant ∩ agent (PRIN-03), la donnée inaccessible n'aurait jamais dû être lue; le risque réel vient des données lues sous les droits propres de l'agent, cas que l'exigence ne nomme pas.
- **Contre-exemple ou scénario de défaillance** : l'agent de sanctions, qui « obéit à d'autres droits d'accès » (p. 92), renvoie « client à risque élevé » : est-ce une donnée inaccessible au mandant? Le test ne peut pas trancher.
- **Correctif proposé** : rattacher l'exigence à l'intersection des droits (9.3) pour les lectures et définir, pour les agents à frontière de sécurité distincte, le contrat de sortie autorisé (schéma de retour à champs déclassifiés).
- **Confiance** : déduit

### [10-35] [MINEUR] ORC-27 : le disjoncteur obligatoire n'est pas signalé comme choix du cadre
- **Axe** : C
- **Localisation** : EXIG-ORC-27, p. 100, Pourquoi : « Microsoft […] recommande d'envisager des disjoncteurs; la temporisation exponentielle et la limitation aux erreurs transitoires sont des choix du cadre ».
- **Diagnostic** (premiers principes) : la source recommande d'« envisager » un disjoncteur; le corps en fait un DOIT pour chaque dépendance. Le passage d'« envisager » à « exiger » est lui aussi un choix du cadre, mais le Pourquoi ne le signale pas, contrairement à la règle de distinction (§ 1.4). PRIN-12 (p. 27) le rend obligatoire, ce qu'il suffirait de citer.
- **Contre-exemple ou scénario de défaillance** : sans objet (traçabilité).
- **Correctif proposé** : ajouter « le disjoncteur obligatoire est un choix du cadre (PRIN-12) ».
- **Confiance** : vérifié dans le texte

### [10-36] [MINEUR] File humaine « recevant le contexte complet » contre minimisation
- **Axe** : C
- **Localisation** : EXIG-ORC-27, p. 100 : « file humaine nommée recevant le contexte complet ».
- **Diagnostic** (premiers principes) : ORC-23 justifie le contexte minimal par « l'exposition des données », et la Loi 25 impose la minimisation. Le repli humain reçoit au contraire le contexte complet, invites et RP comprises, sans restriction d'accès ni de durée.
- **Contre-exemple ou scénario de défaillance** : une file de soutien partagée reçoit l'historique complet de dossiers de crédit.
- **Correctif proposé** : « le contexte nécessaire à la reprise, sous les droits du mandant ».
- **Confiance** : vérifié dans le texte

### [10-37] [MINEUR] ORC-28 : délai mesuré sans cible, redondant avec IAM-20; lieu de l'exercice non précisé
- **Axe** : C (et B)
- **Localisation** : EXIG-ORC-28, p. 100 : « Un exercice d'arrêt DOIT avoir lieu au moins une fois par trimestre et son délai mesuré DOIT être consigné. »
- **Diagnostic** (premiers principes) : ORC-28 ne fixe aucun critère de réussite, alors qu'IAM-20 (p. 130) exige un « délai maximal de bout en bout […] fixé par l'entreprise et mesuré lors d'un exercice au moins trimestriel ». Les deux exigences se recouvrent sans se renvoyer l'une à l'autre au même degré. ORC-28 ne dit pas non plus si l'exercice du coupe-circuit global a lieu en production : arrêter tous les agents chaque trimestre a un coût d'exploitation, et l'exercer en préproduction ne prouve pas la propagation réelle.
- **Contre-exemple ou scénario de défaillance** : un exercice consigne un délai de 40 minutes : conforme à ORC-28, non conforme à IAM-20 si la cible est de 5 minutes.
- **Correctif proposé** : renvoyer à la cible d'IAM-20 et préciser le périmètre de l'exercice (ciblé en production, global en préproduction représentative, par exemple).
- **Confiance** : vérifié dans le texte

### [10-38] [MINEUR] ORC-29 rend obligatoire, par le tableau 26, un DEVRAIT (ORC-10)
- **Axe** : C
- **Localisation** : EXIG-ORC-29, p. 101 : « Une conception NE DOIT PAS présenter l'un des anti-patrons du tableau 26 »; tableau 26, p. 100 : « Agents sans spécialisation réelle, découpés par type de travail » → « (EXIG-ORC-10) ».
- **Diagnostic** (premiers principes) : ORC-10 est un DEVRAIT, mais son contraire devient un anti-patron interdit sans dérogation. La force normative d'ORC-10 est donc en pratique DOIT, et la lecture de 1.4 s'en trouve brouillée.
- **Contre-exemple ou scénario de défaillance** : une équipe s'écarte d'ORC-10, ce qu'un DEVRAIT permet sur justification, et se voit exiger une dérogation formelle (§ 11.6) par ORC-29.
- **Correctif proposé** : promouvoir ORC-10 en DOIT, ou retirer cet anti-patron du tableau 26 (le garder comme avertissement).
- **Confiance** : vérifié dans le texte

### [10-39] [MINEUR] Le « correctif exigé » du tableau 26 cite des éléments absents d'ORC-05
- **Axe** : C
- **Localisation** : tableau 26, p. 101 : « Critères concrets, tests négatifs, suite complète (EXIG-ORC-05) ».
- **Diagnostic** (premiers principes) : EXIG-ORC-05 (p. 90) exige des critères vérifiables, des vérifications déterministes préalables, un évaluateur distinct et trois itérations au plus, mais ni « tests négatifs » ni « suite complète ». Le tableau, rendu normatif par ORC-29, ajoute des obligations qui n'existent dans aucun bloc EXIG.
- **Contre-exemple ou scénario de défaillance** : une revue d'architecture refuse un agent pour absence de tests négatifs en s'appuyant sur ORC-05, qui ne les exige pas.
- **Correctif proposé** : ajouter ces éléments à ORC-05, ou corriger la cellule.
- **Confiance** : vérifié dans le texte (full.txt, p. 90)

### [10-40] [MINEUR] Figure 13 : libellé « non reprenable » et ordre « de k−1 à 1 »
- **Axe** : C
- **Localisation** : figure 13, p. 95 : « T3 ✗ échec Débiter le client non reprenable »; « échec définitif → compenser de k−1 à 1 ».
- **Diagnostic** (premiers principes) : « non reprenable » n'est défini nulle part : non réessayable, non compensable ou non reprise après plantage? Les trois sortes d'étapes du texte (compensable, pivot, réessayable) n'emploient pas ce terme. « De k−1 à 1 » ne vaut que pour un échec définitif connu. Pour une étape incertaine (règle 2), il faut compenser de k à 1, ce que la note sous la figure dit en passant (« C3 n'est exécutée que si son effet est incertain ») sans corriger la formule. Voir aussi 10-06 pour l'ordre.
- **Contre-exemple ou scénario de défaillance** : un lecteur applique « k−1 à 1 » à un délai expiré et omet C3.
- **Correctif proposé** : remplacer « non reprenable » par la sorte d'étape du texte; écrire « compenser de k−1 à 1 (de k à 1 si l'issue de Tk est incertaine) ».
- **Confiance** : vérifié dans le texte

### [10-41] [MINEUR] MAST : intitulé de la troisième catégorie abrégé
- **Axe** : C
- **Localisation** : § 7.9, p. 100 : « trois catégories : conception du système, désalignement entre agents et vérification des tâches ».
- **Diagnostic** (premiers principes) : d'après mes connaissances, la troisième catégorie de MAST s'intitule « Task Verification and Termination ». L'arrêt prématuré et la terminaison font partie de la catégorie, et c'est précisément l'anti-patron « victoire prématurée » du tableau 26.
- **Contre-exemple ou scénario de défaillance** : sans objet (exactitude de la citation).
- **Correctif proposé** : « vérification et terminaison des tâches ».
- **Confiance** : à vérifier (source externe [292])

## Points forts
Distinction rigoureuse entre source et « choix du cadre » (seuils de deux échecs, trimestre, 15 outils), honnêteté sur les chiffres déclarés par les fournisseurs (p. 92) et sur la non-reproductibilité du rejeu (p. 94).
Mécanique saga solide dans ses fondements : journal tenu avant l'action, traitement de l'incertain, compensation en termes métier, isolation sémantique avec les six contre-mesures de Microsoft.
Les sémantiques de livraison (Kafka, A2A push, Step Functions Standard et Express) et les annotations MCP sont correctement présentées comme ne garantissant pas l'unicité.

## Questions pour l'audit bibliographique
- p. 97 : existence et date de draft-ietf-httpapi-idempotency-key-header-08 (« 22 octobre 2026 »); codes 409 et 422; recommandation d'UUID; politique d'expiration des clés (utile à 10-11) [78].
- p. 97 : A2A 1.0, notifications push : « au moins une tentative de livraison (reprises facultatives, doublons possibles) » [68].
- p. 93 et 102 : politique de réessai par défaut des activités Temporal (nombre de tentatives illimité?) [79]; limites d'historique et de charge utile [80, 81] (10-19, 10-29).
- p. 95 : recommandation Temporal d'inscrire la compensation avant l'activité et de poursuivre après une erreur non réessayable [286].
- p. 96 : Microsoft, patron Saga : trois anomalies et six contre-mesures, mauvaise adéquation aux dépendances cycliques [67].
- p. 96 : SagaLLM, Chang et Geng, PVLDB 2025 : lieu et année exacts de publication [287, 288].
- p. 94 : Microsoft Agent Framework, magasins Python à liste blanche de types à la désérialisation; granularité des points de contrôle [105].
- p. 94 : LangGraph, voyage dans le temps (réexécution des nœuds suivants) [283]; persistance par super-étape [124].
- p. 94 : Anthropic, déploiements « arc-en-ciel » [17].
- p. 98 : Cognition (Yan, 22 avril 2026), nuance « écritures à fil unique » [289].
- p. 98 : Anthropic, synthèses de sous-agents « souvent de 1 000 à 2 000 jetons » [17, 149].
- p. 99-100 : RIA art. 14(4)e) (arrêt sûr) [290]; NIST AI RMF MANAGE 2.4 [99]; OpenAI, interruption ciblée ou générale [291].
- p. 100 : MAST : « plus de 1 600 traces », « sept cadriciels », 14 modes, intitulés des trois catégories [292].
- p. 92-93 (couture) : Anthropic, recherche d'outils : -85 % de jetons; 49 → 74 % (Opus 4) et 79,5 → 88,1 % (Opus 4.5) [205]; OpenAI « moins de 20 fonctions » [115].
