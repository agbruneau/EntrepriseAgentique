# Audit chunk_13 — pages 121-132

## Synthèse
Le chunk couvre la fin de la § 9.2 (tableau 34, en recouvrement), la § 9.3 (délégation RFC 8693, intersection des droits, profil OAuth, EXIG-IAM-08 à IAM-16, tableaux 35-36), la § 9.4 (passerelle, figure 18, EXIG-IAM-17 à IAM-21) et le début de la § 9.5 (tableaux 37-38, en recouvrement). Les faits sur les RFC sont exacts dans l'ensemble, et le texte distingue bien l'exigence externe du choix du cadre. En revanche, la chaîne de délégation n'est pas fermée formellement (thèse T6) et la passerelle reste fragile face aux pannes (thèse T2). Les trois défauts les plus graves :
(1) la « portée de la tâche » n'a aucune représentation dans le jeton : l'exemple d'Alice (« et rien d'autre ») est faux [13-01];
(2) le non-élargissement ne borne que la portée, ni la durée ni la reliure du subject_token : un agent peut prolonger indéfiniment la délégation d'un mandant [13-03];
(3) le coupe-circuit dépend du plan de contrôle et de la durée de vie des jetons : une panne du plan de contrôle ou un système sans CAEP le rend inopérant [13-13, 13-17].

## Constats

### [13-01] [MAJEUR] La « portée de la tâche » n'est pas représentable; l'exemple d'Alice affirme une propriété que le jeton n'a pas
- **Axe** : A
- **Localisation** : § 9.3, p. 124 : « Le jeton délégué permet donc de lire les dépenses du troisième trimestre de l'unité d'Alice, et rien d'autre. » Voir aussi l'EXIG-IAM-10 : « portée nécessaire à la tâche ».
- **Diagnostic** : le jeton émis (figure 17, C.5) ne porte que `scope: finance:read`, `sub: alice` et `aud`. Rien n'y exprime « troisième trimestre ». La restriction à l'unité d'Alice vient du serveur cible (filtrage par ligne fondé sur `sub`, étape 6), pas de l'intersection calculée au serveur d'autorisation. Les trois « ensembles » de la figure 17 ne sont pas de même nature : les droits d'Alice portent sur des données, les portées sur des permissions OAuth. Leur intersection n'est donc pas définie. L'EXIG-IAM-10 confie au serveur d'autorisation le calcul d'un terme (« portée nécessaire à la tâche ») qu'aucune entrée normalisée ne lui transmet : en pratique, ce terme se réduit à la portée que l'agent demande lui-même. Le texte affirme aussi que l'intersection « s'applique au serveur d'autorisation » (p. 124), alors que la figure 17 la répartit entre la passerelle (étape 5, « droits effectifs ») et la cible (étape 6).
- **Contre-exemple** : un agent compromis par injection, détenteur de `finance:read`, demande à la cible les dépenses de toute l'année ou des trimestres antérieurs de l'unité d'Alice. Le jeton est valide, Alice a ces droits : l'accès réussit, malgré la promesse « rien d'autre ».
- **Correctif proposé** : porter la portée de la tâche dans `authorization_details` (RFC 9396, déjà retenue en § 8.5 pour les approbations) ou dans un Transaction Token. Désigner explicitement qui fait respecter chaque terme : le serveur d'autorisation pour agent ∩ tâche, la cible pour les droits du mandant via `sub`. Corriger l'exemple, ou y ajouter un `authorization_details` qui borne la période.
- **Confiance** : vérifié dans le texte (figure 17, C.5 p. 220, EXIG-IAM-10).

### [13-02] [MAJEUR] Non-élargissement et audience unique : la portée en aval n'est pas définie quand l'audience change
- **Axe** : A
- **Localisation** : EXIG-IAM-10, p. 124 : « Une portée ne s'élargit jamais d'un saut à l'autre. » EXIG-IAM-11 : « DOIT viser une seule ressource ». EXIG-IAM-08 : « subject_token égal […] au jeton délégué reçu ».
- **Diagnostic** : au premier saut, l'orchestrateur présente au sous-agent un jeton dont `aud` désigne le sous-agent (EXIG-IAM-11). Au second saut, le sous-agent échange ce jeton contre un jeton `aud=mcp-finance`, `scope=finance:read`. Soit le jeton du premier saut contenait déjà `finance:read`, une portée étrangère à son audience que rien ne prescrit; soit `finance:read` est absente du subject_token, et le second saut « élargit » la portée au sens littéral de l'EXIG-IAM-10. Le cadre ne dit ni comment comparer des portées d'audiences différentes, ni qui, au premier saut, inscrit `may_act` pour autoriser le sous-agent.
- **Contre-exemple** : un serveur d'autorisation conforme à la lettre refuse le second saut de l'exemple C.5, faute de `finance:read` dans le subject_token. Un serveur permissif accepte toute portée que permet le registre de l'agent, et la propriété « jamais élargie » devient invérifiable.
- **Correctif proposé** : fixer la règle : le jeton remis à un agent intermédiaire porte la liste des portées en aval autorisées (`authorization_details` ou portée en aval explicite), et chaque échange émet au plus l'intersection de cette liste, du registre et de la tâche. Exiger `may_act` ou une politique équivalente nommant l'acteur suivant dès l'émission.
- **Confiance** : déduit.

### [13-03] [MAJEUR] Aucun plafond de durée ni reliure du subject_token : délégation perpétuable par échanges successifs
- **Axe** : A
- **Localisation** : EXIG-IAM-08, p. 124 (« subject_token égal au jeton du mandant ou au jeton délégué reçu »); EXIG-IAM-10; EXIG-IAM-15 (DEVRAIT).
- **Diagnostic** : seule la portée est bornée d'un saut à l'autre. Rien n'impose `exp(jeton émis) ≤ exp(subject_token)`, ni une borne à partir de l'authentification initiale du mandant (`auth_time`). Rien n'impose non plus que le serveur d'autorisation vérifie que le subject_token visait bien l'acteur demandeur (`aud` = acteur) et qu'il est lié à sa clé (`cnf`). La RFC 8693 laisse tout cela à la politique du serveur.
- **Contre-exemple** : un orchestrateur échange, toutes les 14 minutes, son jeton délégué encore valide contre un nouveau jeton de 15 minutes. La délégation d'Alice, née d'une session de quelques minutes, se prolonge pendant toute la vie de l'agent, à son insu. Autre cas : un agent B inscrit, qui dispose d'un `may_act` large pour Alice, échange un jeton délégué destiné à l'agent A qu'il a obtenu par une trace ou un pair malveillant.
- **Correctif proposé** : ajouter à l'EXIG-IAM-08 ou à l'EXIG-IAM-10 : (a) `exp` émis ≤ `exp` du subject_token; (b) une durée maximale de chaîne depuis l'authentification du mandant; (c) un rejet de tout subject_token dont `aud` ne désigne pas l'acteur ou dont le `cnf` ne correspond pas à l'actor_token ou au certificat client.
- **Confiance** : déduit (RFC 8693 lue de mémoire : elle ne contraint pas `exp`).

### [13-04] [MAJEUR] Profondeur d'`act` et intermédiaires non agents (serveur MCP vers système cible, passerelle)
- **Axe** : A
- **Localisation** : EXIG-IAM-08, p. 124 (« la profondeur d'imbrication de act ne dépasse pas deux niveaux (EXIG-ORC-04) »); EXIG-IAM-12 (« il obtient un nouveau jeton pour chaque audience »); figure 17, boîte « Serveur MCP finance et système cible ».
- **Diagnostic** : la figure 17 réunit le serveur MCP et le système cible dans une même boîte. Or, si la cible est un ERP distinct, l'EXIG-IAM-12 interdit au serveur MCP de lui relayer le jeton : il doit l'échanger. Dans le scénario C.5, la chaîne compte déjà deux niveaux. Si le serveur d'autorisation ajoute un `act` pour le serveur MCP, il obtient trois niveaux et refuse l'échange (EXIG-ORC-04). S'il n'en ajoute pas, la piste d'audit perd un intermédiaire. Le cadre ne dit pas si les serveurs MCP, la passerelle (injection, EXIG-IAM-19) ou les adaptateurs comptent dans la profondeur.
- **Contre-exemple** : la délégation légitime « orchestrateur → exécutant → serveur MCP → ERP » est refusée par un serveur d'autorisation conforme, ou passe sans trace de l'intermédiaire.
- **Correctif proposé** : préciser que la limite de l'EXIG-ORC-04 compte les agents seulement (par exemple les `act.sub` de type SPIFFE d'agent inscrits au registre), et qu'un intermédiaire non agent est consigné dans un attribut distinct ou dans l'audit sans entrer dans le compte. Scinder la boîte de la figure 17.
- **Confiance** : déduit.

### [13-05] [MAJEUR] L'autorisation incrémentale contredit le non-élargissement en chaîne et n'a pas d'approbateur défini
- **Axe** : A
- **Localisation** : § 9.3, p. 124 (« l'agent démarre avec peu de droits et en obtient davantage par une demande traçable »); EXIG-IAM-10 (« Une portée manquante s'obtient par une demande incrémentale explicite, journalisée et limitée en nombre de tentatives »).
- **Diagnostic** : l'autorisation incrémentale de MCP est une nouvelle autorisation par l'utilisateur. Le cadre ne dit pas qui l'accorde au deuxième saut (le mandant, par CIBA? le parrain?), ni pour un agent autonome (EXIG-IAM-16), qui n'a pas de mandant. Accordée au deuxième saut, elle produit précisément un jeton plus large que le subject_token, ce que la même exigence interdit. Le « nombre limité » n'est pas chiffré, ce qui rend l'exigence non testable.
- **Contre-exemple** : un sous-agent reçoit `403 insufficient_scope`. Il ne peut pas élargir sans violer l'EXIG-IAM-10. Il ne peut pas non plus remonter la chaîne, puisqu'aucun mécanisme n'est décrit. Soit la tâche échoue, soit une implémentation ad hoc demande la portée au serveur d'autorisation hors de toute chaîne.
- **Correctif proposé** : préciser que la demande incrémentale remonte au mandant (CIBA, § 8.5) et réémet la chaîne depuis le premier saut. Pour un agent autonome, elle passe par une modification revue du registre, jamais à l'exécution. Fixer un plafond de tentatives par défaut.
- **Confiance** : déduit; mécanisme MCP 2026-07-28 à vérifier.

### [13-06] [MAJEUR] L'adjoint confus entre agents autonomes n'est pas couvert
- **Axe** : A
- **Localisation** : EXIG-IAM-08 (« Lorsqu'un agent agit pour une personne »); EXIG-IAM-16, p. 127 (« DOIT utiliser l'octroi par identifiants du client avec son propre principal »).
- **Diagnostic** : la parade contre l'adjoint confus (droits calculés à partir de l'appelant et de l'acteur) ne s'applique que s'il y a un mandant humain. Dans une chaîne d'agents autonomes (orchestrateur nocturne vers sous-agent vers outil), chaque agent s'authentifie sous son propre principal : la cible ne voit que le sous-agent et ignore l'orchestrateur à l'origine de la demande. Les patrons multiagents du chapitre 7 sont pourtant permis aux agents de fond.
- **Contre-exemple** : un orchestrateur de rapprochement, limité à P1, demande par A2A à un sous-agent doté d'un droit P2 (écriture comptable) d'exécuter une écriture. Le sous-agent agit sous ses propres droits : l'orchestrateur obtient indirectement un droit qu'il n'a pas, ce qui est la définition même de l'adjoint confus (p. 122).
- **Correctif proposé** : étendre l'EXIG-IAM-08 aux chaînes sans personne : l'orchestrateur autonome tient lieu de mandant (`sub` = principal de l'agent initiateur, `act` = agent courant), et l'intersection s'applique de la même façon.
- **Confiance** : vérifié dans le texte (portée des EXIG-IAM-08 et IAM-16).

### [13-07] [MAJEUR] Agents ambiants : aucun mécanisme pour obtenir le jeton d'un mandant absent pendant 12 mois
- **Axe** : A
- **Localisation** : EXIG-IAM-15, p. 126 (« La délégation de longue durée d'un agent ambiant est régie par l'EXIG-AUT-18 »); EXIG-AUT-18, p. 114 (échéance de « 12 mois au plus »); EXIG-IAM-08 (subject_token = jeton du mandant).
- **Diagnostic** : un agent ambiant N3 ou N4 qui agit pour une personne doit, à chaque saut, présenter un subject_token du mandant. Pendant 12 mois, ce jeton ne peut provenir que d'un jeton de rafraîchissement hors ligne, ou d'une autre preuve de la personne gardée par l'environnement d'exécution, donc d'un secret de longue durée de la personne. C'est exactement le risque NHI7 que visent l'EXIG-IAM-05 et l'EXIG-IAM-15. Le cadre ne nomme ni l'octroi, ni le stockage, ni la révocation de cette preuve. L'EXIG-AUT-18 fixe une échéance, pas un mécanisme.
- **Contre-exemple** : une équipe conserve le jeton de rafraîchissement d'Alice dans le coffre de l'agent pour satisfaire l'EXIG-IAM-08. Sa fuite donne 12 mois d'accès au nom d'Alice, et le retrait d'Alice de l'entreprise ne révoque pas cette délégation, faute de règle qui l'y rattache.
- **Correctif proposé** : désigner le mécanisme : délégation enregistrée au serveur d'autorisation (consentement persistant, ID-JAG ou équivalent) et échange à partir de l'identité de l'agent plus une référence de délégation; aucun jeton de personne stocké. Ajouter la révocation de la délégation au départ ou au changement de rôle du mandant.
- **Confiance** : déduit.

### [13-08] [MAJEUR] EXIG-IAM-11 sans clause de variante : le fournisseur cité en exemple n'émet pas le profil RFC 9068, et l'OBO ne porte pas d'`act` imbriqué
- **Axe** : A / B
- **Localisation** : EXIG-IAM-11, p. 124 (« suivre le profil JWT de la RFC 9068 (typ at+jwt; iss, exp, aud, sub, client_id, iat et jti présents) »); EXIG-IAM-08 (« Une variante de fournisseur est admise si son profil […] démontre le même résultat »); p. 122 (flux OBO d'Entra).
- **Diagnostic** : à ma connaissance, les jetons d'accès Entra v2 portent `typ: JWT`, `azp` ou `appid` plutôt que `client_id`, et `uti` plutôt que `jti`. Le flux OBO n'imbrique pas d'`act` : seul le dernier intermédiaire figure dans le jeton. L'EXIG-IAM-08 admet une variante, mais l'EXIG-IAM-11 n'en admet aucune. Et la profondeur de l'EXIG-ORC-04, vérifiée « par l'imbrication de la réclamation act », ne peut pas se vérifier sur un jeton OBO. « Démontre le même résultat » n'a pas de critère d'essai.
- **Contre-exemple** : une entreprise sur Entra (fournisseur que cite le cadre aux p. 121, 122 et 126) ne peut se conformer ni à l'EXIG-IAM-11, ni à l'EXIG-ORC-04 en chaîne.
- **Correctif proposé** : énumérer les propriétés du « même résultat » : audience unique, identifiant unique du jeton, client identifiable, chaîne d'acteurs complète (sinon délégation limitée à un saut). Accorder la même clause de variante à l'EXIG-IAM-11, ou exiger une passerelle de réémission conforme à la RFC 9068.
- **Confiance** : à vérifier (documentation Entra des revendications des jetons d'accès et du flux OBO).

### [13-09] [MINEUR] EXIG-IAM-11 restreint la décision à « sub et l'acteur courant seulement », ce qui exclut scope, aud et cnf
- **Axe** : A / C
- **Localisation** : EXIG-IAM-11, p. 125 : « fonde sa décision sur sub et sur l'acteur courant seulement ».
- **Diagnostic** : la RFC 8693, que la p. 122 restitue correctement, parle des « attributs de premier niveau et [de] l'acteur courant ». La lettre de l'EXIG-IAM-11 interdit de fonder la décision sur `scope`, ce qui contredit l'EXIG-IAM-10 et l'étape 5 de la figure 17.
- **Contre-exemple** : une ressource qui ignore `scope` est conforme à la lettre de l'EXIG-IAM-11.
- **Correctif proposé** : remplacer par « sur les revendications de premier niveau et l'acteur courant seulement, jamais sur les acteurs antérieurs ».
- **Confiance** : vérifié dans le texte.

### [13-10] [MAJEUR] La liaison mTLS ou DPoP ne traverse pas une passerelle qui termine TLS
- **Axe** : A / B
- **Localisation** : tableau 35, p. 125 (« la ressource rejette la requête si le certificat diffère »); EXIG-IAM-14; § 9.4 (« La passerelle agit en mandataire inverse »).
- **Diagnostic** : pour inspecter, filtrer et injecter (contrôles 4, 7 et 8), la passerelle doit terminer TLS. Le serveur MCP voit alors le certificat de la passerelle, pas celui de l'agent : soit il rejette tout (tableau 35), soit il ne vérifie plus la liaison, et le jeton redevient porteur sur le segment passerelle → serveur. Pour DPoP, si la passerelle réécrit l'URL, la valeur `htu` de la preuve ne correspond plus. Le cadre ne désigne ni le point de vérification de la liaison ni la protection du segment aval.
- **Contre-exemple** : un attaquant présent dans le domaine du serveur MCP rejoue un jeton capturé derrière la passerelle : aucun contrôle de `cnf` n'a lieu.
- **Correctif proposé** : préciser que la passerelle vérifie `cnf` et que le serveur n'accepte que la passerelle, par mTLS du maillage. Ou alors exiger une réémission par la passerelle (nouveau jeton lié à sa propre identité, avec `act`), en tenant compte de l'effet sur la profondeur [13-04].
- **Confiance** : déduit.

### [13-11] [MAJEUR] EXIG-IAM-17 se lit comme une exemption intradomaine qui contredit l'EXIG-ARC-01 et l'EXIG-MCP-01
- **Axe** : C / A
- **Localisation** : EXIG-IAM-17, p. 129 : « tout appel d'un agent vers un serveur MCP, vers un autre agent ou vers une ressource qui franchit une frontière de domaine DOIT passer par la passerelle […] À l'intérieur d'un domaine, la décision par appel (EXIG-IAM-02) est appliquée par le serveur de ressources ».
- **Diagnostic** : la proposition relative peut qualifier les trois compléments ou le dernier seulement. La phrase « À l'intérieur d'un domaine » est générale. L'EXIG-ARC-01 (p. 33) impose au contraire la passerelle pour tout appel MCP ou A2A, même intradomaine, et l'EXIG-MCP-01 ajoute « Un hôte ne se connecte jamais directement à un serveur de domaine ». De plus, l'accès direct d'un agent aux données de son propre domaine échappe alors aux contrôles 5 (jeton d'approbation) et 8 (filtrage), même pour une écriture P2 ou P3.
- **Contre-exemple** : un auditeur lit l'EXIG-IAM-17 au sens large et accepte un appel MCP intradomaine direct, sans vérification du catalogue ni du jeton d'approbation.
- **Correctif proposé** : réécrire : « tout appel vers un serveur MCP ou un pair A2A, et tout accès à une ressource d'un autre domaine ». Préciser que toute écriture P2 ou P3 intradomaine passe par un outil MCP derrière la passerelle.
- **Confiance** : vérifié dans le texte (EXIG-ARC-01, EXIG-MCP-01).

### [13-12] [MAJEUR] Force normative de l'injection des justificatifs : DOIT par l'EXIG-IAM-17, DEVRAIT par l'EXIG-IAM-19, facultative selon l'EXIG-IAM-06
- **Axe** : C / A
- **Localisation** : EXIG-IAM-17 (« applique au minimum les neuf contrôles de la figure 18 », dont le contrôle 7 « Injecter les secrets hors de l'agent »); EXIG-IAM-19 · DEVRAIT; EXIG-IAM-06 (« Les jetons sont manipulés par le code d'exécution de l'agent ou injectés par la passerelle »).
- **Diagnostic** : l'EXIG-IAM-17 rend le contrôle 7 obligatoire. L'EXIG-IAM-19 le recommande seulement. L'EXIG-IAM-06 et l'EXIG-IAM-08, où l'agent fait lui-même l'échange, supposent que l'environnement d'exécution détienne le jeton délégué. Par ailleurs, le bloc DEVRAIT de l'EXIG-IAM-19 contient un DOIT (bac à sable, secret patrimonial), et l'annexe D le classe DEVRAIT (p. 229) : une liste de contrôle tirée de l'annexe D perd l'obligation.
- **Contre-exemple** : une passerelle qui relaie le jeton délégué obtenu par l'agent, sans rien injecter, est conforme à l'EXIG-IAM-19 et non conforme à l'EXIG-IAM-17.
- **Correctif proposé** : dans la figure 18 et l'EXIG-IAM-17, faire du contrôle 7 un contrôle « lorsque applicable (EXIG-IAM-19, EXIG-SEC-14) ». Scinder l'EXIG-IAM-19 en un DEVRAIT et un DOIT distincts, et mettre l'annexe D à jour.
- **Confiance** : vérifié dans le texte.

### [13-13] [MAJEUR] Repli sur la « dernière politique distribuée » sans borne de fraîcheur : le coupe-circuit est inopérant pendant une panne du plan de contrôle
- **Axe** : A / B
- **Localisation** : EXIG-IAM-18, p. 129 : « Si le plan de contrôle est indisponible, elle continue d'appliquer la dernière politique distribuée. » Tableau 33 (p. 118) : le plan de contrôle assure « distribution des politiques, coupe-circuit ».
- **Diagnostic** : le coupe-circuit passe par le plan de contrôle. Pendant une panne de ce dernier, une suspension ne parvient à aucune passerelle, et l'agent visé continue d'agir sous l'ancienne politique, sans limite de durée. L'état dynamique utilisé par les contrôles 5 et 6 (budget consommé, jetons d'approbation à usage unique, révocations) n'est pas une « politique » : rien ne dit si la passerelle refuse ou laisse passer quand elle ne peut plus le lire. La porte 3 de MuleSoft, adoptée comme critère, consacre ce comportement.
- **Contre-exemple** : un agent compromis et une indisponibilité du plan de contrôle (panne, ou déni de service provoqué) coïncident. L'équipe actionne le coupe-circuit, mais les passerelles ne reçoivent rien. Seule la désactivation au fournisseur d'identité agit, et seulement à l'expiration des jetons [13-17].
- **Correctif proposé** : fixer une durée maximale de validité de la politique en cache, après quoi la passerelle refuse tout sauf P0. Prévoir un canal de coupe-circuit indépendant du plan de contrôle (liste de suspension poussée ou interrogée localement, signée). Dire que l'état indisponible pour les budgets et les jetons d'approbation impose le refus. Journaliser le mode dégradé et la version de la politique en cache (EXIG-IAM-21).
- **Confiance** : vérifié dans le texte (tableau 33, EXIG-IAM-18); scénario déduit.

### [13-14] [MAJEUR] La même panne donne deux issues pour un appel P3 : EXIG-IAM-18 contre EXIG-AUT-11
- **Axe** : A
- **Localisation** : EXIG-IAM-18 (dernière politique distribuée); EXIG-AUT-11, p. 109 : « Si le service d'approbation, le catalogue ou le service de politiques est indisponible […] la passerelle DOIT refuser tout appel P3 ».
- **Diagnostic** : le cadre ne dit pas si un catalogue ou des politiques mis en cache par la passerelle comptent comme « disponibles ». Si oui, l'EXIG-AUT-11 ne joue jamais tant que le cache existe. Si non, l'EXIG-IAM-18 ne sert à rien pour P2 et P3. Le service de politiques (PE) est-il local à la passerelle ou central? Le tableau 33 ne le précise pas.
- **Contre-exemple** : le plan de contrôle et le catalogue central tombent, la passerelle conserve un cache valide. Une équipe autorise un P3 approuvé (EXIG-IAM-18), l'autre le refuse (EXIG-AUT-11) : les deux s'estiment conformes.
- **Correctif proposé** : définir la disponibilité (cache non expiré au sens de [13-13] = disponible) et poser un ordre explicite : en mode dégradé, P3 et P2 au-delà du seuil sont refusés.
- **Confiance** : vérifié dans le texte; interprétation déduite.

### [13-15] [MAJEUR] Passerelle obligatoire et mode fermé, mais aucune exigence de disponibilité ni de redondance
- **Axe** : B
- **Localisation** : EXIG-IAM-17 (passage obligatoire) et EXIG-IAM-18 (« elle n'ouvre jamais le passage par défaut »), p. 129.
- **Diagnostic** : l'association « chemin unique obligatoire et échec fermé » fait de la passerelle un point unique de défaillance de toute l'activité agentique. Le document ne contient aucune occurrence de « haute disponibilité » ni d'objectif de disponibilité de la passerelle. « Point unique de défaillance » n'y apparaît qu'aux p. 94 et 99, à propos des sagas et des agents. Le Pourquoi de l'EXIG-IAM-17 présente le point unique comme une vertu sans en traiter le coût (thèse T2).
- **Contre-exemple** : une mise à jour de politique défectueuse (EXIG-IAM-21), déployée sur toutes les passerelles, refuse tous les appels. Tous les agents s'arrêtent, files humaines comprises si elles passent aussi par la passerelle.
- **Correctif proposé** : ajouter une exigence : instances redondantes par zone, objectif de disponibilité inscrit et mesuré, déploiement progressif des politiques avec retour arrière automatique, essai de panne dans l'exercice trimestriel.
- **Confiance** : vérifié dans le texte (recherche dans full.txt).

### [13-16] [MAJEUR] Figure 18 : l'audit n'est produit qu'au retour, donc une action exécutée sans réponse n'est pas auditée
- **Axe** : A
- **Localisation** : figure 18, p. 128 (« RETOUR : […] 9 · Tracer et journaliser »; « Un refus à n'importe quelle étape arrête l'appel »).
- **Diagnostic** : à l'aller, la figure ne fait aucun enregistrement, sauf en cas de refus. Si l'outil exécute une action P3 et que la réponse se perd (délai dépassé, plantage de la passerelle), aucun enregistrement n'existe, ce qui contredit l'EXIG-OBS-11 (« Chaque action à effet […] DOIT produire un enregistrement »). De plus, au retour, un « refus » du filtre (8) n'« arrête » rien : l'effet a déjà eu lieu.
- **Contre-exemple** : un virement P3 approuvé est exécuté par l'ERP, la passerelle redémarre avant l'étape 9. Le journal ne montre ni l'action ni l'approbation consommée. L'agent réessaie avec la même clé d'idempotence, ce qui empêche le doublon, mais l'audit reste vide.
- **Correctif proposé** : écrire un enregistrement d'intention (empreinte, approbation, décision) avant de transmettre l'appel, puis un enregistrement de résultat ou d'issue inconnue (« outcome unknown »). Corriger la légende : au retour, le filtre masque et ne peut pas annuler.
- **Confiance** : déduit (figure 18 et EXIG-OBS-11, p. 150).

### [13-17] [MAJEUR] La portée réelle du coupe-circuit dépend de la durée de vie des jetons; la compensation invoquée par l'EXIG-IAM-15 ne tient pas
- **Axe** : A
- **Localisation** : EXIG-IAM-20, p. 130 (« diffuse la révocation […] aux systèmes raccordés qui les prennent en charge »); EXIG-IAM-15 (« l'écart est compensé par […] la révocation en quasi temps réel (EXIG-IAM-20) »); p. 126 (CAE « jusqu'à 28 heures »).
- **Diagnostic** : un jeton JWT autoporteur (RFC 9068) reste accepté par toute ressource qui ne prend pas en charge SSF et CAEP et qui ne reçoit pas l'appel par la passerelle (appel intradomaine, [13-11]), jusqu'à son `exp`. Chez Entra, ce peut être 60 à 90 minutes, ou 28 heures avec CAE, CAE ne protégeant que les ressources qui le prennent en charge. La compensation de l'EXIG-IAM-15 est donc nulle précisément là où la durée dépasse la cible. Le « délai maximal de bout en bout » n'est rattaché ni à la durée des jetons ni à la liste des systèmes non raccordés.
- **Contre-exemple** : un agent est suspendu à 10 h 00. Son jeton CAE de 28 heures reste valide jusqu'au lendemain auprès d'une API interne sans CAEP, appelée directement dans le domaine.
- **Correctif proposé** : exiger que, pour tout système sans SSF ni CAEP, la durée des jetons soit au plus égale au délai maximal du coupe-circuit, ou que ce système ne soit joignable que par la passerelle. Inclure ces systèmes dans l'exercice trimestriel.
- **Confiance** : vérifié dans le texte; comportement CAE à vérifier.

### [13-18] [MAJEUR] Le coupe-circuit désactive l'identité de l'agent et bloque du même coup les compensations des sagas en cours
- **Axe** : A
- **Localisation** : EXIG-IAM-20 (« suspend un agent […] sur toutes les passerelles, désactive l'identité de l'agent auprès du fournisseur d'identité »); EXIG-ORC-28, p. 99 (« laisse les sagas en cours dans un état connu, suspendues ou compensées »).
- **Diagnostic** : si les compensations (outils P2) sont appelées sous l'identité de l'agent suspendu, la passerelle et le fournisseur d'identité les refusent, et la saga reste à moitié exécutée. Le cadre ne désigne aucune identité ni aucun canal de compensation qui survive à la suspension.
- **Contre-exemple** : un agent d'achats est arrêté entre la réservation de stock et le paiement. La compensation « libérer le stock » est refusée (agent suspendu) et le stock reste bloqué.
- **Correctif proposé** : préciser que les compensations sont exécutées par le moteur d'exécution durable, sous sa propre identité et avec une politique de compensation seule, non visée par la suspension de l'agent, et que l'exercice trimestriel le vérifie.
- **Confiance** : déduit.

### [13-19] [MINEUR] Le coupe-circuit fait l'objet de deux exigences voisines, aux sources numérotées différemment
- **Axe** : C
- **Localisation** : EXIG-IAM-20, p. 130 (sources [74] et [61]); EXIG-ORC-28, p. 99 (mêmes sources RIA art. 14(4)e) et NIST MANAGE 2.4, citées [99, 290]).
- **Diagnostic** : les deux exigences se recouvrent (exercice trimestriel, délai mesuré) sans se renvoyer l'une à l'autre. Les mêmes sources y portent des numéros différents.
- **Correctif proposé** : renvoi croisé entre l'EXIG-IAM-20 et l'EXIG-ORC-28, et une seule référence par source.
- **Confiance** : vérifié dans le texte.

### [13-20] [MINEUR] Une phrase sans verbe principal (SSF et CAEP)
- **Axe** : C
- **Localisation** : p. 130 : « Pour propager une révocation au-delà de la passerelle, les spécifications finales OpenID Shared Signals Framework 1.0, qui fournit le cadre de diffusion, et CAEP 1.0 (29 août 2025), qui définit […] ».
- **Correctif proposé** : « …, le cadre s'appuie sur les spécifications finales… ».
- **Confiance** : vérifié dans le texte.

### [13-21] [MINEUR] Contrôle 5 : la figure, la liste et la définition de N2 divergent
- **Axe** : C
- **Localisation** : figure 18 (« (P3, P2 > seuil) »); liste p. 128 (« ou à chaque action pour un agent de niveau N2 »); définition de N2 (p. 21 : « chaque action en écriture attend une approbation »).
- **Diagnostic** : la figure omet le cas N2. La liste dit « chaque action », ce qui inclut les lectures P0 et P1, alors que N2 ne vise que les écritures. L'EXIG-IAM-17 rend la figure normative.
- **Correctif proposé** : « P3; P2 au-delà du seuil; toute écriture pour un agent N2 », dans la figure comme dans la liste.
- **Confiance** : vérifié dans le texte.

### [13-22] [MINEUR] Le contrôle de débit et de budget vient après des garde-fous coûteux
- **Axe** : B
- **Localisation** : figure 18 : 4 « Garde-fous d'entrée (schéma, injection) » avant 6 « Débit, quotas et budget ».
- **Diagnostic** : la détection d'injection repose souvent sur un classifieur. Une boucle d'agent (ASI08) consomme donc la capacité des garde-fous avant d'être freinée par le quota. La pratique courante limite le débit tôt, juste après l'authentification.
- **Correctif proposé** : séparer la limitation de débit (après 1) de la vérification du budget de tâche (avant 7), ou justifier l'ordre.
- **Confiance** : déduit.

### [13-23] [MINEUR] Un refus typé renseigne un agent compromis sur la politique
- **Axe** : B
- **Localisation** : EXIG-IAM-18 : « Tout refus renvoie à l'agent un code d'erreur typé (p. ex. portée insuffisante, approbation requise, budget épuisé, agent suspendu) ».
- **Diagnostic** : un agent sous injection peut sonder les actions et distinguer « approbation requise » de « portée insuffisante », et cibler ensuite l'approbateur (ASI09). Le compromis n'est pas discuté.
- **Correctif proposé** : limiter les codes à quelques familles utiles à l'escalade; le détail reste à l'audit. Surveiller les rafales de refus (signal de risque de l'EXIG-IAM-02).
- **Confiance** : déduit.

### [13-24] [MINEUR] L'encadré sur la latence est répété trois fois, avec des écarts, et néglige le coût des garde-fous
- **Axe** : C / B
- **Localisation** : encadré ATTENTION, p. 130-131; même contenu en § 5 (p. 37) et § 13.2 (p. 192).
- **Diagnostic** : trois versions presque identiques, mais seule celle du chapitre 9 précise « avec 512 connexions » et seul le § 13.2 ajoute que l'inspection agentique n'était peut-être pas active. Les chiffres cités portent sur le relais, alors que les contrôles 4 et 8 (classifieurs) dominent probablement la latence ajoutée.
- **Correctif proposé** : garder une seule version (§ 13.2, EXIG-APP-04), renvoyer à elle ailleurs, et mentionner explicitement la latence des garde-fous.
- **Confiance** : vérifié dans le texte (redondance); coût des classifieurs déduit.

### [13-25] [MINEUR] Les « sept portes » d'un éditeur sont retenues comme critères d'acceptation, hors de tout bloc normatif
- **Axe** : B / C
- **Localisation** : p. 129 : « Le cadre retient ces sept portes comme critères d'acceptation d'une passerelle d'agents (choix du cadre). » Repris p. 191.
- **Diagnostic** : selon le § 1.4, seuls les blocs EXIG obligent : cette phrase n'a donc aucune force, alors qu'elle se présente comme un critère. La source est le billet d'un éditeur de passerelles. Les portes 4 (réutiliser la gouvernance d'API) et 5 (coûts centralisés) avantagent son produit, et la porte 3 consacre le repli critiqué en [13-13].
- **Correctif proposé** : soit en faire une exigence APP, avec reformulation neutre et critère d'essai, soit la présenter comme grille informative.
- **Confiance** : vérifié dans le texte.

### [13-26] [MINEUR] Paramètres de la RFC 8693 : l'obligation de subject_token_type est omise
- **Axe** : A
- **Localisation** : p. 122 : « subject_token (le jeton du mandant) est obligatoire; actor_token […] et requested_token_type sont facultatifs ».
- **Diagnostic** : la RFC 8693 (§ 2.1) rend aussi obligatoires `subject_token_type` et `grant_type` (`urn:ietf:params:oauth:grant-type:token-exchange`). Le résumé est incomplet, et l'EXIG-IAM-08 s'y appuie.
- **Correctif proposé** : ajouter ces deux paramètres.
- **Confiance** : certain d'après ma connaissance de la RFC; à confirmer par l'audit bibliographique.

### [13-27] [MINEUR] L'EXIG-IAM-09 interdit de « réutiliser le jeton » d'une personne, alors que l'EXIG-IAM-08 exige de le présenter
- **Axe** : C
- **Localisation** : EXIG-IAM-09 : « aucun agent ne réutilise le jeton, la session ou le mot de passe d'une personne »; EXIG-IAM-08 : « subject_token égal au jeton du mandant ».
- **Diagnostic** : à la lettre, présenter le jeton d'Alice au serveur d'autorisation est une réutilisation. Seule l'EXIG-IAM-12 prévoit cette exception.
- **Correctif proposé** : « ne le présente à aucun service autre que le serveur d'autorisation, à titre de subject_token (EXIG-IAM-12) ».
- **Confiance** : vérifié dans le texte.

### [13-28] [MINEUR] Le jeton de la figure 17 ne respecte pas l'EXIG-IAM-11, et « SVID » est ambigu
- **Axe** : C
- **Localisation** : figure 17, p. 123 (revendications sub, act, aud, scope, exp, cnf; « actor_token = SVID de l'agent »).
- **Diagnostic** : `typ`, `iss`, `client_id`, `iat` et `jti`, qu'exige l'EXIG-IAM-11, manquent, sans mention « extrait ». Le texte de la p. 123 précise que l'actor_token est un JWT-SVID, pas un X.509-SVID. La figure dit seulement « SVID ».
- **Correctif proposé** : marquer « extrait » et écrire « JWT-SVID ».
- **Confiance** : vérifié dans le texte.

### [13-29] [MINEUR] Profil OAuth : écarts sur PKCE, sur les acteurs visés et sur le décompte « deux points »
- **Axe** : A / C
- **Localisation** : tableau 35 (« PKCE pour les clients publics »); EXIG-IAM-13 (« PKCE avec S256 », sans restriction; « émission et validation du paramètre iss »); Pourquoi : « plus strict que la RFC 9700 sur deux points ».
- **Diagnostic** : (a) le tableau limite PKCE aux clients publics, l'exigence l'étend à tous. (b) La validation de `iss` (RFC 9207) incombe au client OAuth (hôte ou agent), qui n'est pas visé par l'EXIG-IAM-13 (fournisseur, passerelle, serveurs). (c) Le cadre est aussi plus strict que la RFC 9700 sur PKCE pour les clients confidentiels (RECOMMENDED dans la RFC) et sur RFC 9207 et 9728, qu'elle n'impose pas : il y a plus de deux points.
- **Correctif proposé** : harmoniser le tableau et l'exigence, ajouter les clients aux sujets de l'exigence, corriger le décompte.
- **Confiance** : vérifié dans le texte; contenu de la RFC 9700 d'après ma connaissance.

### [13-30] [MINEUR] Liaison des jetons P1 seulement recommandée
- **Axe** : B
- **Localisation** : EXIG-IAM-14 : « Tout jeton qui donne accès à un outil P2 ou P3 […] DOIT être lié […] Pour les autres jetons, la liaison DEVRAIT ».
- **Diagnostic** : un jeton P1 (fiche de paie, dossier client, tableau 31) volé permet une exfiltration de renseignements personnels, donc un incident au sens de la Loi 25. Le risque ne se limite pas à l'écriture. Note : les jetons sont liés à un serveur, pas à un outil; « accès à un outil P2 » vise donc tout serveur qui expose un outil P2, ce qui mérite d'être écrit.
- **Correctif proposé** : DOIT aussi pour P1 sensible, ou justifier l'exclusion.
- **Confiance** : déduit.

### [13-31] [MINEUR] « n'emprunte jamais l'identité d'une personne pour élargir ses droits »
- **Axe** : C
- **Localisation** : EXIG-IAM-16, p. 127.
- **Diagnostic** : le complément de but laisse entendre qu'un emprunt sans élargissement serait admis, ce que l'EXIG-IAM-09 interdit sans condition.
- **Correctif proposé** : « n'emprunte jamais l'identité d'une personne (EXIG-IAM-09) ».
- **Confiance** : vérifié dans le texte.

### [13-32] [MINEUR] Références en double pour une même source
- **Axe** : C
- **Localisation** : [176] et [327] (draft-ietf-oauth-v2-1-16, p. 125); [179] et [332] (Transaction Tokens −11, p. 126-127); [91] et [349] (OWASP NHI Top 10, p. 121 et 131); [347] et [348] (OWASP LLM Top 10 2025, p. 131); [69], [70] et [118] (RFC 8693).
- **Diagnostic** : ces doublons gonflent le décompte des références (thèse T8) et compliquent la vérification.
- **Correctif proposé** : fusionner, en citant la section dans le corps (« RFC 8693, § 4.1 [70] »).
- **Confiance** : vérifié dans le texte (annexe G).

### [13-33] [MINEUR] « en attente du rapport » traduit mal l'état IETF
- **Axe** : C
- **Localisation** : tableau 36, Transaction Tokens : « consensus du groupe atteint, en attente du rapport ».
- **Diagnostic** : l'état IETF est « WG Consensus: Waiting for Write-Up » (réf. [483]), c'est-à-dire la fiche du responsable du document (shepherd write-up), pas un « rapport ».
- **Correctif proposé** : « en attente de la fiche du responsable (shepherd write-up) ».
- **Confiance** : vérifié dans le texte ([483]).

### [13-34] [MINEUR] (couture p. 121 et p. 129) Tableau 34 : NHI3 rattaché à l'EXIG-IAM-17 de façon peu probante
- **Axe** : C
- **Localisation** : tableau 34 : « NHI3 Identités de tiers vulnérables […] EXIG-IAM-17; chaîne d'approvisionnement ».
- **Diagnostic** : l'EXIG-IAM-17 régit les appels des agents de l'entreprise. Elle ne couvre pas les accès qu'un fournisseur détient sur les systèmes de l'entreprise (octrois OAuth de tiers, comptes de service), qui sont l'objet de NHI3.
- **Correctif proposé** : renvoyer d'abord aux clauses (§ 13.3) et à un inventaire des octrois de tiers; garder l'EXIG-IAM-17 en second.
- **Confiance** : déduit.

### [13-35] [MINEUR] (couture p. 132 et § 9.3-9.4) Tableau 38 : renvois imprécis pour ASI10 et incomplets pour ASI03
- **Axe** : C
- **Localisation** : ASI10 : « Surveillance, plafonds et coupe-circuit (section 9.4) »; ASI03 : « EXIG-IAM-08 à EXIG-IAM-12 ».
- **Diagnostic** : la § 9.4 contient le coupe-circuit et le budget, mais les plafonds relèvent de l'EXIG-ORC-26 (§ 7.8) et la surveillance du chapitre 10. Pour ASI03, le mécanisme « réutilise un jeton » trouve sa parade directe dans l'EXIG-IAM-14 (liaison) et l'EXIG-IAM-15 (durée), qui ne sont pas citées.
- **Correctif proposé** : ASI10 : EXIG-ORC-26, EXIG-IAM-20, § 10.4. ASI03 : EXIG-IAM-08 à EXIG-IAM-16.
- **Confiance** : vérifié dans le texte.

## Points forts
Restitution exacte de la sémantique d'`act` (acteur courant ou antérieur), de `may_act` et de la distinction entre délégation et usurpation (RFC 8693), ainsi que des profils RFC 8705, 9449, 9728 et 9207. La frontière entre exigence externe et choix du cadre est tenue partout (EXIG-IAM-10, 13, 14, 15, 18, 21). Le texte refuse avec honnêteté de chiffrer une durée de vie normative et une latence non mesurées.

## Questions pour l'audit bibliographique
- p. 124 : MCP 2026-07-28, autorisation : 403 `insufficient_scope`, autorisation incrémentale et plafond de tentatives [209].
- p. 124-125 : revendications des jetons d'accès Entra v2 (`typ`, `client_id` ou `azp`, `jti` ou `uti`) et absence d'`act` imbriqué dans l'OBO [326] (trancherait [13-08]).
- p. 125 : MCP 2026-07-28 exige-t-il que le client valide `iss` (RFC 9207)?
- p. 125 : draft-ietf-oauth-v2-1-16 du 3 septembre 2026, expirant le 7 mars 2027 [176, 327] (arithmétique cohérente à 185 jours).
- p. 126 : durées Entra (60 à 90 min, minimum 10 min, CAE jusqu'à 28 h) [331]; formule « quelques minutes ou moins » dans Transaction Tokens −11, § 6 [179].
- p. 126 et 127 : extensions MCP « OAuth Client Credentials » et « Enterprise-Managed Authorization » stables depuis la révision 2026-07-28 [217, 218]; ID-JAG −04 du 21 mai 2026 [177].
- p. 127 : états IETF de identity-chaining −17 (file de l'éditeur des RFC), spiffe-client-auth −02 (15 juin 2026), draft-oauth-ai-agents-on-behalf-of-user −02 (26 août 2025, expiré le 27 février 2026) [333-335].
- p. 127 : NCCoE, document de réflexion de février 2026; synthèse du 29 septembre 2026, « plus de 600 répondants », cas d'usage DevSecOps [337, 338].
- p. 128 : couverture d'Azure API Management (outils MCP seulement; A2A en JSON-RPC seulement) [108, 109]; Kong AI A2A Proxy, Gateway 3.14+, édition Enterprise, sans gestion d'état [111]; appartenance d'agentgateway et d'Agent Router à l'AAIF [36, 130, 339]; Omni Gateway, ancien Flex Gateway [341].
- p. 129 : documentation Vercel Sandbox (dépendance à SNI, terminaison TLS, règle générique) [342].
- p. 130 : disponibilité générale de Microsoft Agent 365 le 1er mai 2026 et actions de cycle de vie « à venir » [46]; date de finalisation de SSF 1.0 et CAEP 1.0 (29 août 2025?) et liste des événements CAEP [343, 344].
- p. 130-131 : chiffres d'agentgateway (500 000 req/s, 512 connexions, P99 < 0,2 ms à 30 000 req/s) [142]; FAQ et banc d'essai TrueFoundry [143, 144].
- p. 131 : date de publication du Top 10 agentique de l'OWASP (9 décembre 2025) [345]; T16 et T17 dans la v1.1 de « Threats and Mitigations » [87]; LLM Top 10 2026 (août 2026, agentivité excessive en LLM03) [346]; chiffres de MITRE ATLAS 2026.09 [352].

audit_13.md : 35 constats (0 BLOQUANT, 17 MAJEUR, 18 MINEUR)
