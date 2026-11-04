# Audit chunk_22 — pages 211-222

## Synthèse
Le chunk couvre la fin de la grille d'homologation (A.6-A.8), l'annexe B (règles, tableau 63, fiche JSON d'exemple) et les exemples C.1 à C.5 (outil MCP, entrée de catalogue, carte A2A, CloudEvents, jeton délégué), avec l'amorce de C.6-C.7. Qualité élevée : j'ai recalculé `definition_digest` (C.2), `h` (C.6) et la clé d'idempotence (C.7, = SHA-256 de `tache-7f3c2a|etape-03/creer-bon-commande`) : tous exacts; l'en-tête JWS de C.3 et les horodatages concordent. Les trois défauts les plus graves : (1) le seuil d'approbation repose sur `montant_total_cad`, un argument redondant que l'agent fixe lui-même et que rien ne rattache aux lignes; (2) le format de seuil, évalué appel par appel, ne bloque pas le fractionnement et ne sait pas exprimer le seuil « par tâche » de la section 8.4; (3) C.5 contredit le modèle d'audience et de liaison mTLS de la passerelle (section 6.5).

## Constats

### [22-01] [BLOQUANT] Seuil d'approbation calculé sur un montant déclaré par l'agent, sans lien avec les lignes
- **Axe** : A
- **Localisation** : C.1 (p. 216-217) et C.2 (p. 218), « "approval_threshold": { "argument": "montant_total_cad", "max_without_approval_cad": 5000 } »; C.1 : « "montant_total_cad": { "type": "number", "exclusiveMinimum": 0 } »
- **Diagnostic** : la passerelle compare le seuil à un argument (`montant_total_cad`) qui reprend une information déjà portée par `lignes` (quantité × prix unitaire). Le schéma ne peut pas imposer l'égalité, et ni la description de l'outil, ni l'entrée de catalogue, ni EXIG-ORC-22 ou EXIG-AUT-10 n'obligent le serveur à recalculer le total et à refuser un écart. Le contrôle repose donc sur une valeur contrôlée par l'agent, donc par une injection éventuelle. Le texte rend ces exemples « normatifs par leur forme » (p. 215) : on encourage ainsi la reproduction de ce défaut dans les contrats réels.
- **Contre-exemple** : un agent compromis appelle l'outil avec `montant_total_cad: 4900` et les deux lignes de C.7 (9 984 $ + 2 496 $ = 12 480 $). La passerelle juge l'appel sous le seuil et ne demande aucune approbation. Si l'ERP calcule le total à partir des lignes, comme il le fait d'ordinaire, il crée un bon soumis de 12 480 $ sans approbation, et le journal consigne 4 900 $.
- **Correctif proposé** : soit retirer `montant_total_cad` des entrées (le serveur le calcule et le renvoie dans `outputSchema`), soit exiger que la passerelle, ou le serveur avant tout effet, recalcule le total à partir des lignes et rejette tout écart. Ajouter à EXIG-AUT-10 une règle générale : un seuil se calcule sur une valeur dérivée de l'effet, jamais sur un argument redondant.
- **Confiance** : vérifié dans le texte (aucune règle de cohérence); scénario déduit.

### [22-02] [MAJEUR] Seuil évalué appel par appel : fractionnement possible, et le seuil « par tâche » de la section 8.4 n'est pas exprimable
- **Axe** : A
- **Localisation** : C.2 (p. 218), « un agent de classe modérée déclaré N3 peut créer seul un bon de 5 000 $ ou moins »; cf. section 8.4 (p. 109), « le seuil déclaré de l'outil est de 25 par tâche »
- **Diagnostic** : `approval_threshold` porte sur un seul argument d'un seul appel. Il n'a ni fenêtre, ni agrégat par tâche, par fournisseur ou par période. L'exemple même de la section 8.4 (25 factures « par tâche ») ne peut donc pas s'écrire dans le format de catalogue qui sert de modèle. Aucune exigence ne traite le fractionnement (recherche de « fraction », « cumul », « scind » dans tout le texte : rien sur les seuils).
- **Contre-exemple** : l'agent émet trois bons de 4 160 $ au même fournisseur `SUP-004512` dans la même tâche, chacun avec un `step_id` distinct, donc une clé d'idempotence distincte (section 7.6). Chaque appel passe sous le seuil et le total atteint 12 480 $ sans approbation.
- **Correctif proposé** : enrichir `approval_threshold` d'une portée d'agrégation (`per_call`, `per_task`, `per_counterparty_per_day`), tenue à jour par la passerelle comme l'enveloppe budgétaire de C.7. Ajouter un déclencheur « cumul sous le seuil » aux déclencheurs d'EXIG-AUT-10.
- **Confiance** : vérifié dans le texte.

### [22-03] [MAJEUR] Jeton délégué de C.5 incompatible avec le modèle de passerelle de la section 6.5 (audience et liaison mTLS)
- **Axe** : A
- **Localisation** : C.5 (p. 220-221), « "aud": "https://mcp-finance.ent.ca" » et « cnf lie le jeton à l'empreinte du certificat X.509-SVID de l'agent »; section 6.5 (p. 56), « l'URI canonique annoncée aux clients est la sienne; elle obtient ensuite, pour le serveur de domaine, un jeton distinct »
- **Diagnostic** : selon la section 6.5, l'agent s'adresse à l'URI de la passerelle, comme dans C.2 (`endpoint` sous `passerelle-agents.ent.ca`), et la passerelle obtient un second jeton pour le serveur. Deux cas sont possibles, et C.5 contredit chacun d'eux. (a) C.5 est le jeton que l'agent présente : son `aud` devrait alors désigner la passerelle, pas `mcp-finance.ent.ca`. (b) C.5 est le jeton que reçoit le serveur : il a alors été obtenu par la passerelle, et `cnf` devrait lier le certificat de la passerelle (le TLS se termine à la passerelle, donc le serveur ne peut pas vérifier la possession de la clé de l'agent), `client_id` et l'`act` courant devraient désigner la passerelle. La lecture présente pourtant C.5 comme le jeton que « présente l'agent […] au serveur MCP ». La figure 17 (p. 123) a le même défaut.
- **Contre-exemple** : avec le TLS terminé à la passerelle, le serveur MCP reçoit un jeton dont `x5t#S256` désigne le certificat de l'agent, alors que la connexion entrante présente celui de la passerelle. Soit il rejette tout appel légitime, soit il désactive la vérification `cnf`, et EXIG-IAM-14 devient lettre morte. S'il accepte ce jeton, c'est qu'il y a eu relais de jeton (EXIG-IAM-12).
- **Correctif proposé** : montrer les deux jetons, agent → passerelle (aud = URI de la passerelle, cnf = agent) et passerelle → serveur (aud = serveur, cnf = passerelle, act courant = passerelle ou agent selon la règle retenue), ou bien déclarer explicitement la passerelle transparente au TLS. Préciser en EXIG-IAM-11 qui figure dans `act` lorsque la passerelle refait l'échange.
- **Confiance** : vérifié dans le texte (contradiction 6.5 / C.5); conséquence mTLS déduite.

### [22-04] [MAJEUR] En-tête `jku` de la carte signée sans ancre de confiance épinglée
- **Axe** : A
- **Localisation** : C.3 (p. 219), en-tête décodé `{"alg":"ES256","typ":"JOSE","kid":"cartes-agents-2026-10","jku":"https://cles.ent.ca/a2a/jwks.json"}`; lecture : « le jeu de clés publiques de l'entreprise (jku), et tout client vérifie cette signature avant de se fier à la carte »
- **Diagnostic** : le paramètre `jku` est fourni par le signataire. Un client qui va chercher la clé à l'URL indiquée par la signature vérifie seulement que la carte est cohérente avec elle-même, pas qu'elle est authentique : c'est le piège classique de la vérification JWS, contre lequel met en garde la RFC 8725, BCP JWT (section à confirmer). EXIG-A2A-03 évoque « une clé dont le catalogue consigne la confiance » pour les tiers, mais ni cette exigence ni la lecture n'interdisent de suivre `jku`, et elles n'exigent pas de le confronter à une liste blanche.
- **Contre-exemple** : un attaquant publie une carte `risque-credit` modifiée (URL d'interface vers son serveur), signée avec sa propre clé, avec `jku: https://attaquant.example/jwks.json`. Un client qui suit `jku` la juge valide et détourne les tâches (ASI07).
- **Correctif proposé** : dans EXIG-A2A-03, résoudre la clé par `kid` dans un jeu de clés épinglé au catalogue; ignorer `jku` ou ne l'accepter qu'en concordance exacte avec une URL inscrite au catalogue pour cet émetteur. Le dire dans la lecture de C.3.
- **Confiance** : vérifié dans le texte (en-tête décodé); bonne pratique JOSE d'après mes connaissances, numéro de section de la RFC 8725 à vérifier.

### [22-05] [MAJEUR] Palier P2 de l'outil de création de bon soumis : un effet externe et des effets multiples non traités
- **Axe** : A
- **Localisation** : C.1 (p. 216), « Crée dans l'ERP un bon de commande, à l'état brouillon ou soumis »; C.2 (p. 218), « "tier": "P2" »; compensation `approvisionnement_annuler_bon_commande`
- **Diagnostic** : P3 couvre ce qui est « critique, externe ou irréversible », et un outil à effets multiples prend le palier le plus élevé (section 8.3). L'outil a deux effets : un brouillon, réversible, et un bon « soumis ». Si la soumission transmet le bon au fournisseur, ce qui est courant dans un ERP, l'effet est externe et l'annulation n'est qu'une compensation partielle (contrat éventuellement formé, communication déjà partie). L'exemple ne dit pas ce que fait « soumis », et le classement P2 repose sur ce postulat implicite.
- **Contre-exemple** : dans un ERP où « soumis » déclenche l'envoi EDI au fournisseur, un agent N3 crée seul un bon soumis de 4 990 $. L'annulation envoyée ensuite ne défait pas l'expédition déjà lancée.
- **Correctif proposé** : préciser dans la description et au catalogue que « soumis » reste interne (circuit d'approbation de l'ERP), ou scinder en deux outils (créer un brouillon en P2, soumettre en P3), ou classer l'outil P3 en vertu de la règle des effets multiples.
- **Confiance** : déduit (l'effet de « soumis » n'est pas décrit).

### [22-06] [MAJEUR] Fiche d'exemple : l'outil de paiement P3 n'a pas de clé d'idempotence
- **Axe** : A / C
- **Localisation** : annexe B, exemple (p. 215), « {"ref": "tresorerie.paiements.emettre@1.1.0", "digest": "sha256:c07d9b12", "tier": "P3", "approval": "signed_out_of_band"} »
- **Diagnostic** : EXIG-ORC-21 et EXIG-ORC-22 exigent une clé d'idempotence vérifiée par le serveur pour tout outil P2 ou P3, et le tableau 63 exige à l'étape Conception une « clé d'idempotence pour les outils à effet ». L'exemple l'indique pour l'outil P2 (`"idempotency_key": true`) mais pas pour l'émission de paiement, l'outil même où le doublon coûte le plus cher (section 7.6 : « débiter un client deux fois »). La mention « extrait » n'explique pas qu'on ait gardé le champ pour P2 et retiré pour P3.
- **Contre-exemple** : un lecteur prend la fiche pour modèle. Après un délai expiré, l'orchestrateur relance l'émission, et l'approbation signée est encore valide pendant 15 minutes. Sans clé côté trésorerie, le paiement part deux fois. Le `jti` à usage unique du jeton d'approbation bloque le second passage par la passerelle seulement si celle-ci a consigné le premier usage avant la coupure.
- **Correctif proposé** : ajouter `"idempotency_key": true` (et l'étape pivot) à l'entrée P3, ou retirer ce champ de toutes les entrées et le renvoyer au catalogue.
- **Confiance** : vérifié dans le texte.

### [22-07] [MAJEUR] Statut normatif des annexes B et C contradictoire avec la section 1.4 et l'annexe H
- **Axe** : C
- **Localisation** : B (p. 212), « Il est normatif par son contenu, pas par sa forme » et « DOIVENT être lues par la passerelle dans le registre »; C (p. 215), « Ils sont normatifs par leur forme, pas par leurs valeurs »; section 1.4 (p. 13), « le reste du texte, les exemples et les figures sont informatifs »; H.5 (p. 282), « les exemples de l'annexe C signent en ES256, à titre informatif »
- **Diagnostic** : la section 1.4 limite l'obligation aux blocs EXIG, aux PRIN et aux tableaux auxquels une exigence renvoie expressément. L'annexe B peut s'appuyer sur EXIG-GOV-07 (« fiche conforme à l'annexe B »). L'annexe C, elle, n'est visée par aucune exigence : tous les renvois relevés sont du type « exemple complet à l'annexe C ». Elle se dit pourtant normative par sa forme, et H.5 la tient pour informative. Le « DOIVENT » de la règle « Source de vérité » se trouve aussi hors de tout bloc EXIG.
- **Contre-exemple** : en homologation, un contrat d'outil qui s'écarte de la structure de C.2 (pas de `header_projection`, par exemple) est conforme d'après la section 1.4 et non conforme d'après l'annexe C. Le résultat dépend du lecteur.
- **Correctif proposé** : déclarer C informative, en renvoyant au tableau 22 et aux EXIG pour les champs obligatoires, ou créer une exigence qui rende obligatoires les structures C.2, C.6 et C.8. Transformer la règle « Source de vérité » en EXIG, ou renvoyer à EXIG-AUT-08 et EXIG-MCP-14.
- **Confiance** : vérifié dans le texte.

### [22-08] [MAJEUR] Seuil et palier inscrits deux fois (fiche et catalogue) sans règle de préséance
- **Axe** : A
- **Localisation** : B (p. 212), « DOIVENT être lues par la passerelle dans le registre et le catalogue »; exemple (p. 215), « "tier": "P2", "threshold_cad": 5000 »; C.2 (p. 218), `approval_threshold` au catalogue
- **Diagnostic** : la fiche (registre) et l'entrée de catalogue portent chacune un palier et un seuil pour le même outil. La règle dit de lire « dans le registre et le catalogue » sans dire lequel prévaut en cas d'écart. La règle « la plus stricte » de la section 8.4 vise la classe, le niveau et le palier, pas deux copies d'une même valeur. De plus, le `threshold_cad` de la fiche ne précise pas l'argument mesuré, contrairement à C.2.
- **Contre-exemple** : la sécurité relève le palier de l'outil d'appariement à P3 au catalogue, et la fiche, pas encore réévaluée, indique toujours P2. Une passerelle qui lit la fiche laisse passer l'appel seul. Une autre qui lit le catalogue le bloque. Le comportement dépend de l'implémentation.
- **Correctif proposé** : palier et seuil d'outil uniquement au catalogue (la fiche n'en conserve qu'une copie, vérifiée par réconciliation); un seuil propre à l'agent est permis seulement s'il est plus strict, et la passerelle applique le minimum. L'écrire dans la règle « Source de vérité ».
- **Confiance** : vérifié dans le texte; scénario déduit.

### [22-09] [MINEUR] La liste « Réévaluation » de l'annexe B s'écarte d'EXIG-GOV-12, et l'exemple `renew_on` l'appauvrit encore
- **Axe** : C
- **Localisation** : B (p. 212), « Tout changement de modèle ou de version de modèle, d'instructions système, d'outil ou de palier d'outil, de version majeure d'un contrat »; exemple (p. 215), « "renew_on": ["model_change", "new_write_tool", "target_population_change"] »
- **Diagnostic** : EXIG-GOV-12 (p. 167) compte en plus le changement d'ODD et le changement de fournisseur ou de lieu de traitement, que la paraphrase de B omet. B écrit aussi « tout changement d'outil » là où GOV-12 dit « ajout d'un outil ou passage à un palier supérieur ». La paraphrase est à la fois plus large et plus étroite que l'exigence. L'exemple ne retient que trois déclencheurs, et `new_write_tool` est plus étroit que l'« ajout d'un outil » de GOV-12.
- **Contre-exemple** : l'agent déplace son modèle vers une région hors Québec. Ce déclencheur, essentiel au regard de l'article 17, ne figure ni dans B ni dans `renew_on`.
- **Correctif proposé** : remplacer la liste de B par un renvoi à EXIG-GOV-12, et ajuster `renew_on` à l'énumération de cette exigence.
- **Confiance** : vérifié dans le texte.

### [22-10] [MINEUR] L'exemple désigne des fonctions là où le gabarit exige des personnes nommées
- **Axe** : C
- **Localisation** : tableau 63 (p. 213), « Personne nommée qui répond des effets de l'agent » et « Plafond N0 à N4 approuvé, par qui (personne nommée) »; exemple (p. 215), « "business_sponsor": "Directrice, comptes fournisseurs" », « "approved_by": "Directrice, comptes fournisseurs" »
- **Diagnostic** : l'exemple ne respecte pas son propre gabarit. Si l'on veut éviter des RP d'employés dans l'exemple, il faut le dire, par exemple avec un identifiant d'employé fictif.
- **Correctif proposé** : `"business_sponsor": "emp-004417"` (fictif), ou une note expliquant le choix.
- **Confiance** : vérifié dans le texte.

### [22-11] [MINEUR] Analogie du « certificat d'autonomie » sans sa propriété essentielle (délivrance par un tiers)
- **Axe** : B
- **Localisation** : B (p. 212), « Le niveau d'autonomie fonctionne comme le « certificat d'autonomie » de Feng et al., qui se renouvelle à chaque changement »
- **Diagnostic** : la section 11.4 (p. 164) précise que Feng, McDonald et Zhang font délivrer ce certificat par un tiers. Or le tableau 44 fait du propriétaire métier l'autorité (A) qui fixe le niveau d'autonomie, et l'exemple montre la parraine approuvant le plafond de son propre agent. L'analogie invoquée en appui perd l'indépendance qui lui donne sa valeur.
- **Correctif proposé** : écrire « comme un certificat interne, sans l'indépendance du tiers prévu par Feng et al. », ou donner la fonction risques et conformité comme approbatrice du plafond N3 et N4.
- **Confiance** : vérifié dans le texte (B, 11.4, tableau 44); la teneur exacte de [83] est à vérifier.

### [22-12] [MINEUR] Libellés d'états divergents entre les sections 11.4, le tableau 63 et les exemples
- **Axe** : C
- **Localisation** : tableau 63 (p. 214), « État (proposé, conception, construction, pilote, production, suspendu, retiré) »; section 11.4 (p. 164), « « en conception », « en construction » »; C.2 (p. 218), « "lifecycle_state": "active" »
- **Diagnostic** : la section 11.4 énumère sept états normatifs (en lien avec EXIG-GOV-08), et le tableau 63 les nomme autrement. L'état « active » d'un outil au catalogue n'est défini nulle part.
- **Correctif proposé** : aligner les libellés et donner, pour les deux registres, l'énumération des valeurs lisibles par machine.
- **Confiance** : vérifié dans le texte (recherche d'« active » et d'« actif » sans définition d'état).

### [22-13] [MINEUR] Borne du seuil à 5 000 $ ambiguë
- **Axe** : C
- **Localisation** : B (p. 215), « l'agent apparie seul les factures sous 5 000 $, au-delà de quoi la passerelle exige une approbation »; C.2 (p. 218), « peut créer seul un bon de 5 000 $ ou moins »
- **Diagnostic** : « sous » (strict) et « ou moins » (large) ne disent pas la même chose, et le cas d'une facture d'exactement 5 000 $ n'est réglé ni dans B ni par la sémantique de `max_without_approval_cad`.
- **Correctif proposé** : fixer la sémantique (inclusive) dans la définition du champ et écrire « 5 000 $ ou moins » partout.
- **Confiance** : vérifié dans le texte.

### [22-14] [MINEUR] L'enveloppe C.7 « reprend les plafonds de la fiche d'agent (annexe B) », qui est celle d'un autre agent
- **Axe** : C
- **Localisation** : C.7 (p. 222), « l'enveloppe reprend les plafonds de la fiche d'agent (annexe B) »; la fiche B porte `"agent_id": "agt-fin-rapprochement"` (p. 215), alors que C.7 porte sur `agt-achats-indirects@1.2.0`
- **Diagnostic** : les valeurs (50 000, 0,75, 15, 8, 60, 28 800) sont identiques, mais elles appartiennent à deux agents distincts. Le renvoi laisse croire que la fiche B est celle du scénario commun, ce qui est un constat de couture entre les pages 215 et 222.
- **Correctif proposé** : « reprend les plafonds inscrits à la fiche de l'agent (gabarit de l'annexe B) », ou aligner la fiche d'exemple sur `agt-achats-indirects`.
- **Confiance** : vérifié dans le texte.

### [22-15] [MINEUR] L'agent de rapprochement de l'exemple emploie l'échange de jetons, alors que le cadre cite le rapprochement comme cas des identifiants du client
- **Axe** : C
- **Localisation** : exemple B (p. 215), « "access_mode": "token_exchange_rfc8693" »; section 9.3 (p. 126), « Un agent qui n'agit pour personne (traitement de fond, surveillance, rapprochement nocturne) »
- **Diagnostic** : les mandants de l'exemple incluent un rôle humain et l'orchestrateur, donc l'agent peut être interactif. Mais il porte un délai total de 8 h et un nom qui correspond au cas type d'EXIG-IAM-16. La fiche n'a qu'un seul `access_mode` pour deux modes d'invocation possibles.
- **Correctif proposé** : permettre un `access_mode` par mandant ou déclencheur (échange de jetons pour `role:`, identifiants du client pour les déclencheurs planifiés), comme le laisse entendre le champ « Autorisations » du tableau 63.
- **Confiance** : déduit.

### [22-16] [MINEUR] Empreintes tronquées à 8 caractères hexadécimaux dans l'exemple de fiche
- **Axe** : C
- **Localisation** : exemple B (p. 215), « "digest": "sha256:9f2c41d0" »
- **Diagnostic** : EXIG-INT-15 exige l'empreinte approuvée, et l'annexe C insiste pour que ses empreintes soient de vrais SHA-256 de 64 caractères. Une empreinte de 32 bits, reprise telle quelle, autoriserait des collisions faciles à fabriquer.
- **Correctif proposé** : écrire l'empreinte complète, ou noter « abrégée » avec « … » comme le font les conventions de l'annexe C.
- **Confiance** : vérifié dans le texte.

### [22-17] [MINEUR] Domaines fictifs et préfixe en domaine inversé incohérents
- **Axe** : C
- **Localisation** : B (p. 215), « spiffe://entreprise.example/agents/… »; C (p. 215), « domaines (ent.ca) »; C.4 (p. 219), « "type": "ca.entreprise.logistique.alerte.rupture.v1" »
- **Diagnostic** : la fiche B et l'annexe C n'utilisent pas le même domaine (`entreprise.example`, `ent.ca`), et C.5 emploie `spiffe://ent.ca`. Le préfixe inversé `ca.entreprise`, utilisé aussi pour les attributs OpenTelemetry (section 10.1), ne correspond à aucun des deux : l'inverse de `ent.ca` est `ca.ent`.
- **Correctif proposé** : un seul domaine fictif (`ent.ca`) et un préfixe `ca.ent.*`, ou `entreprise.ca` partout.
- **Confiance** : vérifié dans le texte.

### [22-18] [MINEUR] Trois conventions de nommage des portées OAuth
- **Axe** : C
- **Localisation** : C.2 (p. 218), « approvisionnement.bons-commande.creer »; C.3 (p. 219), « agents.risque-credit » et « risque-credit.analyser »; C.5 (p. 220), « finance:read »
- **Diagnostic** : on trouve des points ou un deux-points, une ressource en tête ou en queue, du français ou de l'anglais. EXIG-IAM-16 exige des « portées par outil », et la comparaison d'intersection (EXIG-IAM-10) suppose une grammaire de portées stable.
- **Correctif proposé** : fixer une grammaire au profil OAuth (tableau 35), p. ex. `<domaine>.<ressource>.<action>`, et l'appliquer aux cinq exemples.
- **Confiance** : vérifié dans le texte.

### [22-19] [MINEUR] Vocabulaire de classification : « internal » (CloudEvents) et « confidentiel » (fiche, catalogue) sans correspondance
- **Axe** : C
- **Localisation** : C.4 (p. 220), « "dataclassification": "internal" »; C.2 (p. 218), « "data_classification_max": "confidentiel" »
- **Diagnostic** : EXIG-EVT-04 oblige le consommateur à rejeter une valeur qu'il ne reconnaît pas. Sans table de correspondance entre l'échelle interne en français et les valeurs de l'extension Data Classification, un agent qui recopie la classification de sa fiche dans l'événement fait rejeter ce dernier.
- **Correctif proposé** : ajouter au tableau 20, ou à C.4, la correspondance échelle interne ↔ valeurs de l'extension.
- **Confiance** : vérifié dans le texte; les valeurs admises par l'extension sont à vérifier.

### [22-20] [MINEUR] Renvoi « section 8.4.1 » ambigu
- **Axe** : C
- **Localisation** : C.3 (p. 219), « règles de présence des champs de la spécification (section 8.4.1) appliquées »
- **Diagnostic** : partout ailleurs, « section X.Y » désigne une section du cadre. La section 8.4 du cadre (combinaison classe × palier) n'a pas de sous-section 8.4.1. Il s'agit vraisemblablement de la section de la spécification A2A.
- **Correctif proposé** : « (spécification A2A 1.0, section 8.4.1)[68] ».
- **Confiance** : vérifié dans le texte (aucune section 8.4.1 dans le cadre); numéro dans A2A à vérifier.

### [22-21] [MINEUR] ETag dérivé de la seule version : risque de copies périmées lors d'une rotation de clé
- **Axe** : B
- **Localisation** : C.3 (p. 219), « version, en SemVer, dont dérive l'ETag servi avec la carte, permet de revalider les copies en cache (EXIG-A2A-04) »
- **Diagnostic** : la signature est exclue du contenu canonisé. Une rotation de la clé `kid` change donc la carte servie sans forcément changer `version`. Le guide cité (p. 70) admet aussi un ETag « dérivé […] d'un hachage », plus robuste.
- **Contre-exemple** : la clé `cartes-agents-2026-10` est révoquée, puis la carte est re-signée sans changer de version. Les clients revalident, reçoivent 304 et gardent la carte signée par la clé révoquée, qu'EXIG-A2A-03 les oblige à rejeter : l'agent devient injoignable jusqu'à l'expiration du cache.
- **Correctif proposé** : dériver l'ETag de l'empreinte de la carte servie, signatures comprises, ou imposer un incrément de version à toute nouvelle signature.
- **Confiance** : déduit.

### [22-22] [MINEUR] La carte ne déclare pas la liaison du jeton à l'expéditeur
- **Axe** : A
- **Localisation** : C.3 (p. 219), `securitySchemes` limité à `openIdConnectSecurityScheme`
- **Diagnostic** : l'agent est de classe élevée, et EXIG-IAM-14 exige mTLS ou DPoP pour les jetons détenus par un agent de cette classe. La carte, qui sert à la découverte, n'annonce pas cette exigence (A2A prévoit un schéma mTLS). Un client conforme à la carte présente un jeton porteur.
- **Correctif proposé** : ajouter un schéma `mtlsSecurityScheme`, ou l'équivalent dans A2A 1.0, combiné à OIDC dans `securityRequirements`.
- **Confiance** : déduit; nom exact du schéma A2A à vérifier.

### [22-23] [MINEUR] L'agent de crédit « n'accorde ni ne refuse » mais inscrit une décision dans l'ERP (section 6.6)
- **Axe** : C
- **Localisation** : C.3 (p. 218), « recommande une décision motivée. N'accorde ni ne refuse aucun crédit. »; section 6.6 (p. 74), « Prêt à inscrire sa décision […] 8. L'agent crédit appelle l'outil d'écriture de l'ERP »
- **Diagnostic** : la carte présente un agent qui recommande, et le scénario dont elle relève le montre en train d'écrire une décision. La différence pèse sur la qualification (décision automatisée ou non, art. 12.1, ou au regard du RIA si des personnes physiques sont visées).
- **Correctif proposé** : dans la section 6.6, écrire « inscrire sa recommandation », ou décrire la compétence d'écriture dans la carte.
- **Confiance** : vérifié dans le texte.

### [22-24] [MINEUR] Ordre Kafka présenté comme acquis sans ses conditions
- **Axe** : B
- **Localisation** : C.4 (p. 220), « comme Kafka écrit les messages de même clé dans la même partition et en conserve l'ordre, les alertes d'un même article dans un même entrepôt restent dans l'ordre »
- **Diagnostic** : la garantie suppose un partitionneur par hachage de clé, un nombre de partitions constant et des reprises du producteur qui ne réordonnent pas les messages (idempotence activée ou une seule requête en vol). Un ajout de partitions réaffecte les clés, et les messages en transit peuvent alors se dépasser.
- **Correctif proposé** : écrire ces conditions en EXIG-EVT-09 (nombre de partitions figé au contrat, producteur idempotent) et nuancer la lecture.
- **Confiance** : déduit (connaissance de Kafka); état actuel de [468] à vérifier.

### [22-25] [MINEUR] Le compteur de sauts borne la profondeur, pas la diffusion
- **Axe** : B
- **Localisation** : C.4 (p. 220), « un événement dont le compteur atteint 4 n'est pas traité et part en file de lettres mortes (EXIG-EVT-06) »
- **Diagnostic** : avec `xagentmaxhops = 4`, il y a trois niveaux de réaction. Si chaque événement intéresse k agents (la section 6.7 cite la planification et l'approvisionnement pour une même alerte), une alerte produit jusqu'à k + k² + k³ événements, chacun avec son coût en jetons. La tempête est bornée en profondeur, pas en volume.
- **Correctif proposé** : ajouter au contrat AsyncAPI un plafond de diffusion ou de débit par `xagentorigin` et par trace, appliqué par le bus.
- **Confiance** : déduit (défaut hérité de la section 6.7).

### [22-26] [MINEUR] Montants en nombres JSON binaires
- **Axe** : B
- **Localisation** : C.1 (p. 216-217), « "montant_total_cad": { "type": "number" […] "prix_unitaire_cad": { "type": "number", "minimum": 0 } »
- **Diagnostic** : `number` correspond à un flottant IEEE 754 chez la plupart des clients. Un contrôle de cohérence total = Σ quantité × prix, recommandé en 22-01, échoue ou passe selon l'arrondi (p. ex. 0,1 × 3). L'empreinte RFC 8785 reste stable, mais l'égalité métier ne l'est pas.
- **Correctif proposé** : montants en cents (`integer`), ou en chaîne décimale avec `pattern`, et règle de tolérance déclarée.
- **Confiance** : déduit.

### [22-27] [MINEUR] Déclaration d'idempotence au catalogue incomplète au regard d'EXIG-ORC-22
- **Axe** : A
- **Localisation** : C.2 (p. 218), « "idempotency": { "argument": "idempotency_key", "checked_by_server": true, "on_conflict": "reject" } »
- **Diagnostic** : EXIG-ORC-22 exige trois comportements (doublon sans effet, arguments différents rejetés, original en cours refusé) et précise : « Ce comportement est déclaré dans l'entrée de catalogue ». L'entrée n'en déclare qu'un, et ne dit pas combien de temps le serveur conserve les clés. Au-delà de cette durée, une relance tardive (`max_wall_clock_s` de 8 h en C.7) recrée un bon.
- **Correctif proposé** : ajouter `on_in_progress: "refuse"` et `key_retention_s` (au moins `max_wall_clock_s` de la tâche).
- **Confiance** : vérifié dans le texte.

### [22-28] [MINEUR] Aucune règle ne borne l'expiration d'un jeton dérivé par celle du jeton reçu
- **Axe** : A
- **Localisation** : C.5 (p. 220), « "iat": 1793084700, "exp": 1793085600 » (même `exp` que le jeton du premier saut, figure 17, p. 123)
- **Diagnostic** : dans l'exemple, l'`exp` du jeton après deux sauts est égal à celui du jeton reçu, ce qui est correct. Mais EXIG-IAM-10 interdit seulement l'élargissement de la portée, pas celui de la durée. Une chaîne d'échanges successifs, chacun émis pour 15 minutes, prolongerait donc la délégation au-delà du jeton du mandant. Je n'ai trouvé aucune règle sur ce point dans le texte complet.
- **Correctif proposé** : dans EXIG-IAM-10, ajouter « exp du jeton émis ≤ exp du subject_token ».
- **Confiance** : vérifié par recherche (absence); risque déduit.

### [22-29] [MINEUR] Renvois approximatifs du tableau 63 pour l'empreinte de l'invite système
- **Axe** : C
- **Localisation** : tableau 63 (p. 213), « version et empreinte de l'invite sys­tème (EXIG-GOV-07, EXIG-FIN-07) »
- **Diagnostic** : EXIG-GOV-07 exige les modèles et leurs versions, et EXIG-FIN-07 porte sur le « préfixe stable et cache mesuré ». Ni l'une ni l'autre n'impose une version et une empreinte de l'invite système. EXIG-INT-15 (qui couvre les « invites » parmi les dépendances) serait plus juste.
- **Correctif proposé** : renvoyer à EXIG-INT-15 (et à EXIG-GOV-12 pour le déclencheur).
- **Confiance** : vérifié dans le registre (titres de l'annexe D); énoncé complet de FIN-07 non relu.

## Points forts
Les empreintes de l'annexe C sont réellement reproductibles : `definition_digest`, `h` et la clé d'idempotence se recalculent exactement à partir des valeurs montrées. La chaîne C.1 → C.2 → C.6 → C.7 est cohérente : version @1.4.0, arithmétique 9 984 + 2 496 = 12 480, horodatages (approbation à 9 h 24, état à 9 h 25 UTC). Le tableau 63, qui associe à chaque champ l'étape où il devient exigible, transforme le registre en contrôle vérifiable (EXIG-GOV-08).

## Questions pour l'audit bibliographique
- p. 212 : Feng, McDonald et Zhang [83] décrivent-ils un « certificat d'autonomie » renouvelé « à chaque changement de l'agent ou de son environnement », et délivré par un tiers?
- p. 212 : les bonnes pratiques de Microsoft Entra Agent ID [92] prévoient-elles une attestation par le parrain tous les 6 à 12 mois?
- p. 212 : le guide d'EFVP de la CAI [413] recommande-t-il la mise à jour de l'EFVP lorsqu'un projet change?
- p. 216-217 : la révision MCP 2026-07-28 définit-elle `x-mcp-header` dans `inputSchema` et l'en-tête `Mcp-Param-<Nom>`? JSON Schema 2020-12 y est-il le dialecte par défaut?
- p. 219 : A2A 1.0 (a2a.proto) compte-t-il exactement huit champs obligatoires dans `AgentCard`? Les noms `supportedInterfaces`, `protocolBinding`, `extendedAgentCard`, `securityRequirements` (`schemes`/`list`) et le schéma mTLS sont-ils exacts? À quelle section de la spécification renvoie « 8.4.1 »?
- p. 219 : la RFC 8725 met-elle en garde contre le suivi de `jku`/`x5u`, et à quelle section?
- p. 220 : l'extension CloudEvents Data Classification admet-elle la valeur `internal`, et quelles autres? `service_account` est-il une valeur d'`authtype` de l'extension Auth Context?
- p. 220 : la liaison Kafka de CloudEvents 1.0.2 [250] décrit-elle le « Key Mapper » comme facultatif, et exclut-elle `datacontenttype` des en-têtes `ce_` au profit de `content-type`?
- p. 221 : la RFC 9068 exige-t-elle exactement `iss`, `exp`, `aud`, `sub`, `client_id`, `iat` et `jti`, et la RFC 8693 réserve-t-elle les `act` imbriqués à l'information (je le crois, avec une confiance élevée)?

audit_22.md : 29 constats (1 BLOQUANT, 7 MAJEUR, 21 MINEUR)
