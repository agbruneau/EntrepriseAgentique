# Audit chunk_12 — pages 111-122

## Synthèse
Le chunk couvre la fin de § 8.5 (jeton d'approbation, EXIG-AUT-12 à 15), § 8.6-8.8 (agents ambiants, approbation machinale, décisions automatisées, EXIG-AUT-16 à 23), la page de partie III et § 9.1-9.2 (confiance zéro, identité non humaine, EXIG-IAM-01 à 07, tableaux 33-34), plus l'amorce de § 9.3. Le texte est dense, sourcé et distingue bien norme externe et choix du cadre; les faits sur CIBA, RFC 8785/9396/8693, SP 800-207, SPIFFE et l'art. 12.1 me semblent exacts. Défauts les plus graves : (1) l'EXIG-AUT-20 soustrait à l'approbation les cellules « automatiques » de la figure 15, ce qui contredit la règle du plus strict de l'EXIG-AUT-10; (2) le jeton d'approbation (EXIG-AUT-12) ne couvre que les approbations « exigées par la figure 15 », ne dit pas comment l'usage unique coexiste avec les réessais idempotents et ne sait pas représenter le double approbateur exigé par l'EXIG-AUT-15; (3) la qualification « exclusivement automatisée » (EXIG-AUT-23) dépend d'une mesure mensuelle a posteriori, inutilisable au moment où l'avis de l'art. 12.1 est dû. Note : les pages 111-112 sont en recouvrement des deux côtés (chunks 11 et 12); j'y rapporte les constats qui mettent en jeu les pages 113-116 ou les annexes C et D.

## Constats

### [12-01] [BLOQUANT] L'EXIG-AUT-20 exempte d'approbation ce que l'EXIG-AUT-10 peut y soumettre
- **Axe** : A
- **Localisation** : § 8.7, EXIG-AUT-20, p. 115 : « Les actions que la figure 15 classe comme automatiques ne sont pas soumises à approbation. »
- **Diagnostic** : L'EXIG-AUT-10 (p. 110) retient le contrôle le plus strict entre la cellule de la figure 15, le niveau d'autonomie et les déclencheurs (comportement atypique, dépassement de seuil, cumul de la règle de deux). La légende de la figure 15 précise que ces éléments peuvent rendre le contrôle « plus strict, jamais plus souple ». L'EXIG-AUT-20 ne met en jeu que la cellule et pose une exemption absolue, dans un bloc DOIT. Les deux exigences se contredisent dès qu'un déclencheur vise une cellule « Automatique ».
- **Contre-exemple** : Un agent faible, N3, fait une lecture P1 (cellule « Automatique ») hors de son périmètre habituel, ce qui est un déclencheur « comportement atypique » de l'EXIG-AUT-10. Selon l'EXIG-AUT-10, la lecture exige une approbation. Selon l'EXIG-AUT-20, elle « n'est pas soumise à approbation ». Une passerelle qui suit la lettre de l'EXIG-AUT-20 laisse passer un accès anormal.
- **Correctif proposé** : Remplacer la phrase par : « Les actions dont le contrôle calculé selon l'EXIG-AUT-10 est automatique ne sont pas soumises à approbation. »
- **Confiance** : vérifié dans le texte (p. 109-110 et 115)

### [12-02] [MAJEUR] Jeton et liste d'approbateurs limités aux approbations « exigées par la figure 15 »
- **Axe** : A
- **Localisation** : EXIG-AUT-12, p. 111 : « Toute approbation exigée par la figure 15 DOIT produire un jeton signé par le service d'approbation »; EXIG-AUT-15, p. 112 : « Chaque combinaison de classe et de palier soumise à approbation DOIT avoir une liste d'approbateurs ».
- **Diagnostic** : Deux sources d'approbation ne viennent pas de la cellule : le niveau N2 (§ 8.4 : « le niveau prime alors sur la cellule ») et les déclencheurs de l'EXIG-AUT-10. Pour ces approbations, rien n'oblige à émettre un jeton lié à l'empreinte. De même, aucune liste d'approbateurs n'est exigée pour une combinaison classe × palier dont la cellule n'est pas « soumise à approbation ».
- **Contre-exemple** : Un agent modéré déclaré N2 fait une écriture P2 sous le seuil (cellule « Autonome sous seuil »). Le niveau impose une approbation, mais l'EXIG-AUT-12 ne s'applique pas à la lettre : une confirmation sans jeton reste conforme. Et comme la combinaison modérée × P2 n'est pas « soumise à approbation » d'après la cellule, aucune liste d'approbateurs n'existe. La demande ne peut alors être acheminée à personne : blocage, ou approbateur improvisé.
- **Correctif proposé** : Dans l'EXIG-AUT-12 et l'EXIG-AUT-15, remplacer « exigée par la figure 15 » par « exigée par le contrôle calculé selon l'EXIG-AUT-10 », et définir les listes d'approbateurs par classe × palier × motif (cellule, niveau, déclencheur).
- **Confiance** : vérifié dans le texte

### [12-03] [MAJEUR] Liste de vérification du jeton incomplète (habilitation de l'approbateur, émetteur, audience)
- **Axe** : A
- **Localisation** : EXIG-AUT-12, p. 111 : « Avant l'exécution, la passerelle DOIT vérifier la signature, l'expiration et l'usage unique, puis recalculer h; toute différence annule l'approbation. »
- **Diagnostic** : C'est la seule liste de contrôles vérifiable en test, et il lui manque quatre points. (a) Que le `sub` du jeton figure dans la liste d'approbateurs habilités pour la combinaison visée (EXIG-AUT-15) : personne n'est chargé de le vérifier. (b) Que l'agent et la tâche du jeton correspondent à l'appelant : l'EXIG-AUT-13 l'impose sous forme négative, mais h ne contient ni l'agent ni la tâche. (c) `iss` et `aud`, absents du contenu minimal, alors que l'exemple C.6 (p. 221) les porte. (d) Le nombre d'approbateurs requis (voir 12-11).
- **Contre-exemple** : Un employé non habilité, mais connu du fournisseur d'identité, approuve par CIBA un appel P3. Le jeton est bien signé par le service d'approbation, l'empreinte concorde et le jeton n'a pas servi : la passerelle exécute. La liste de l'EXIG-AUT-15 est alors décorative.
- **Correctif proposé** : Ajouter à l'EXIG-AUT-12 : `iss` et `aud` (la passerelle) obligatoires; l'agent et la tâche doivent égaler ceux de l'appelant; l'approbateur doit être habilité au registre au moment de la signature; le nombre d'approbations distinctes doit être celui que le contrôle exige.
- **Confiance** : vérifié dans le texte (p. 111-112, 221)

### [12-04] [MAJEUR] « Usage unique » non défini face aux réessais idempotents, à la réplication et à l'expiration
- **Axe** : A / B
- **Localisation** : EXIG-AUT-12, p. 111 : « une date d'expiration et un identifiant à usage unique »; la figure 16 indique qu'à l'étape 6, l'agent « rejoue l'appel avec le jeton ».
- **Diagnostic** : L'exécution durable réessaie avec la même clé d'idempotence (§ 7.6, p. 93-97). Trois points restent ouverts. (1) Le moment où le `jti` est consommé : avant l'appel aval, il bloque le réessai légitime; après, il laisse une fenêtre de rejeu concurrent (TOCTOU). (2) Avec plusieurs instances de passerelle, l'usage unique exige un registre de `jti` partagé et cohérent, et rien n'est dit de son comportement en cas de partition. (3) Un réessai qui survient après les 15 minutes force une nouvelle approbation d'une action peut-être déjà exécutée.
- **Contre-exemple** : L'appel P3 approuvé expire en délai d'attente côté aval, sans qu'on sache s'il a abouti. L'orchestrateur réessaie avec la même clé d'idempotence et le même jeton, et la passerelle refuse : jeton déjà utilisé. L'approbateur doit approuver de nouveau une action peut-être exécutée, ce qui nourrit l'approbation machinale (§ 8.7). Si la passerelle ne consomme le `jti` qu'après succès, deux répliques acceptent en parallèle le même jeton. Le doublon n'est alors évité que si l'aval vérifie la clé.
- **Correctif proposé** : Lier atomiquement `jti`, h et clé d'idempotence : un même triplet peut être présenté de nouveau jusqu'à `exp` pour un réessai, tout autre usage est refusé. Le registre de `jti` est partagé, à écriture conditionnelle, et refuse en mode fermé en cas de partition. Expliciter le cas du réessai après `exp`.
- **Confiance** : déduit

### [12-05] [MAJEUR] La canonisation RFC 8785 ne protège pas contre la divergence d'analyse JSON entre passerelle et serveur
- **Axe** : A
- **Localisation** : § 8.5, p. 111 : « La canonisation suit la RFC 8785 (JSON Canonicalization Scheme) »; « Sans canonisation, deux sérialisations du même objet JSON donneraient deux empreintes. »
- **Diagnostic** : JCS suppose des données I-JSON (clés uniques, nombres IEEE 754 double). Le cadre ne dit ni que la passerelle refuse les entrées qui ne sont pas I-JSON, ni qu'elle transmet au serveur les octets canonisés qui ont servi au calcul de h. Si elle relaie les octets d'origine, l'empreinte porte sur l'interprétation de la passerelle, pas sur celle du serveur qui exécute.
- **Contre-exemple** : L'agent envoie `{"montant_total_cad":100,"montant_total_cad":100000}`. L'analyseur de la passerelle garde la première clé et affiche, canonise et fait approuver 100. Le serveur MCP garde la dernière et exécute 100 000. Même chose pour un entier au-delà de 2^53, arrondi par la passerelle mais lu exactement par le serveur.
- **Correctif proposé** : L'EXIG-AUT-12 DOIT exiger le rejet de toute entrée qui n'est pas I-JSON (clés dupliquées, nombres non représentables) et la transmission au serveur de la forme canonique dont h est tiré. Recommander des montants en chaîne ou en unités mineures entières.
- **Confiance** : déduit (comportement de JCS et des analyseurs : connaissance générale)

### [12-06] [MINEUR] Concaténation sans séparateur dans le calcul de h
- **Axe** : A
- **Localisation** : p. 111 : « h = SHA-256(identifiant de l'outil ‖ arguments canonisés) »; l'exemple C.6 précise « immédiatement suivi des arguments ».
- **Diagnostic** : Sans séparateur ni préfixe de longueur, l'encodage n'est pas injectif en général. Le risque est faible ici, puisque les arguments canonisés commencent par `{` et que la grammaire de l'identifiant l'exclut probablement, mais rien ne l'écrit.
- **Contre-exemple** : Si un jour une version épinglée pouvait contenir `{`, deux couples (outil, arguments) distincts produiraient le même flux d'octets.
- **Correctif proposé** : Fixer la grammaire de l'identifiant (sans `{`), ou hacher un objet JCS `{"outil":…,"arguments":…}`, ou ajouter un séparateur de domaine.
- **Confiance** : déduit

### [12-07] [MINEUR] Le jeton remis à l'agent pour qu'il « rejoue l'appel » contre l'EXIG-IAM-06
- **Axe** : C
- **Localisation** : figure 16, p. 111 : « rejoue l'appel avec le jeton »; EXIG-IAM-06, p. 121 : « aucun jeton, certificat ni secret n'entre dans le contexte du modèle, dans la mémoire de l'agent, dans les arguments d'un outil ».
- **Diagnostic** : Le parcours ne dit pas par où transite le jeton. S'il passe par l'agent, il ne doit entrer ni dans le contexte ni dans les arguments, sinon h change, mais seulement dans le code d'exécution. Rien ne l'écrit à la section 8.5.
- **Contre-exemple** : Une mise en œuvre naïve renvoie le jeton au modèle dans le résultat de l'outil (« approbation requise, jeton : … ») pour qu'il rappelle l'outil, ce qui viole l'EXIG-IAM-06.
- **Correctif proposé** : Préciser que la passerelle conserve le jeton et rattache la reprise à la demande, ou que le jeton circule en en-tête par le code d'exécution, hors du contexte du modèle.
- **Confiance** : vérifié dans le texte

### [12-08] [MINEUR] La figure 16 restreint le parcours aux appels P3
- **Axe** : C
- **Localisation** : légende de la figure 16, p. 111 : « La passerelle intercepte l'appel P3 ».
- **Diagnostic** : L'exemple de référence C.6 (p. 221, voir aussi p. 216) applique ce parcours à un outil P2 au-delà du seuil. La figure laisse croire que le parcours est propre au P3.
- **Contre-exemple** : Un lecteur qui conçoit la passerelle à partir de la figure ne prévoit pas l'interception des appels P2 au-delà du seuil.
- **Correctif proposé** : Écrire « l'appel soumis à approbation (P3, ou P2 au-delà du seuil, ou selon l'EXIG-AUT-10) ».
- **Confiance** : vérifié dans le texte

### [12-09] [MINEUR] Le `binding_message` de CIBA ne lie pas la demande à l'action, surtout sans interface
- **Axe** : A
- **Localisation** : EXIG-AUT-14, p. 112 : « un binding_message court, affiché sur les deux appareils, rattache la demande à l'action ».
- **Diagnostic** : Dans CIBA, le `binding_message` sert à ce que l'utilisateur constate que les deux appareils parlent de la même transaction. C'est un lien entre appareils, pas un lien cryptographique à l'action, rôle que tient h. Pour un agent sans interface, que l'exigence vise expressément, aucun appareil de consommation n'affiche ce message, et le lien entre appareils ne veut alors rien dire.
- **Contre-exemple** : Agent ambiant sans interface : le message n'apparaît que sur le téléphone de l'approbateur et ne se compare à rien.
- **Correctif proposé** : Dire que le `binding_message` aide l'approbateur à reconnaître la demande (référence courte dérivée de h ou de la tâche) et que le lien à l'action repose sur h.
- **Confiance** : à vérifier (CIBA Core 1.0, § 7.1, définition de `binding_message`)

### [12-10] [MINEUR] Approbation hors bande : DOIT au tableau 46, DEVRAIT à l'EXIG-AUT-14
- **Axe** : C
- **Localisation** : EXIG-AUT-14, p. 112 : « DEVRAIT passer par OpenID Connect CIBA »; tableau 46, p. 171, classe élevée : « P3 toujours soumis à une approbation hors bande ».
- **Diagnostic** : Le tableau 46 est normatif par renvoi de l'EXIG-CON-02. Pour la classe élevée, le caractère hors bande y est obligatoire, alors que l'EXIG-AUT-14 le fait recommandé pour tout P3. Ce n'est pas une contradiction stricte (CIBA n'est qu'un moyen), mais la force normative diverge sans que le texte le dise.
- **Contre-exemple** : Un agent élevé dont l'approbation P3 se fait dans une console Web sur le même poste respecte l'EXIG-AUT-14 (DEVRAIT non suivi, avec justification), mais pas le tableau 46.
- **Correctif proposé** : Ajouter à l'EXIG-AUT-14 : « DOIT pour un agent de classe élevée (tableau 46) ».
- **Confiance** : vérifié dans le texte

### [12-11] [MAJEUR] Double approbation exigée, mais ni le jeton ni l'audit ne savent la porter
- **Axe** : A
- **Localisation** : EXIG-AUT-15, p. 112 : « Pour un appel P3 d'un agent de classe élevée, deux approbateurs distincts DOIVENT approuver, dont au moins un autre que le mandant. »; EXIG-AUT-12 : « l'identifiant pseudonymisé de l'approbateur ».
- **Diagnostic** : Le contenu minimal du jeton ne prévoit qu'un approbateur. L'enregistrement d'audit C.8 (p. 223) n'a qu'un champ `approbateur` et un `approbation_jti`. Le texte ne dit pas s'il faut deux jetons (chacun à usage unique, donc lequel consomme-t-on?), un jeton cosigné, ou un ordre et une indépendance des deux approbations. Si l'action est éditée entre les deux, les deux approbations portent sur des empreintes différentes.
- **Contre-exemple** : La passerelle reçoit un seul jeton valide, signé par le premier approbateur, avec la bonne empreinte. Les contrôles de l'EXIG-AUT-12 passent tous, et l'appel P3 de classe élevée s'exécute avec une seule approbation.
- **Correctif proposé** : Définir un jeton à approbations multiples (liste `approbateurs[]`, chacune sur le même h, distinctes et habilitées) ou deux jetons liés par la même tâche et le même h, et exiger que la passerelle vérifie le nombre requis. Adapter C.6 et C.8.
- **Confiance** : vérifié dans le texte (p. 111-112, 221-223)

### [12-12] [MINEUR] Clause « au moins un autre que le mandant » vide de sens
- **Axe** : A
- **Localisation** : EXIG-AUT-15, p. 112 (même citation que 12-11).
- **Diagnostic** : Deux approbateurs distincts ne peuvent pas être tous deux le mandant; la clause est donc toujours vraie et n'ajoute rien. L'intention probable est la séparation des fonctions : un approbateur indépendant du mandant, de sa ligne hiérarchique, du parrain et du propriétaire de l'agent.
- **Contre-exemple** : Le mandant et son subordonné direct approuvent un virement P3 : la règle est respectée, mais l'indépendance est nulle.
- **Correctif proposé** : « dont au moins un indépendant du mandant, de sa ligne hiérarchique et du parrain de l'agent ».
- **Confiance** : vérifié dans le texte

### [12-13] [MAJEUR] Approbateurs « inscrits et formés » : guère applicable aux agents interactifs au service de nombreux mandants
- **Axe** : B
- **Localisation** : EXIG-AUT-15, p. 112 : « L'approbateur DOIT s'authentifier par authentification forte (au moins deux facteurs), posséder la compétence du domaine et l'autorité de refuser, et avoir été formé aux modes de défaillance des agents. »
- **Diagnostic** : La figure 15 range l'« envoi » en P3, et l'EXIG-AUT-09 interdit tout P3 sans approbation. Pour un assistant interactif, l'approbateur naturel est le mandant, qui confirme sur son appareil par CIBA. Or l'EXIG-AUT-15 exige qu'il figure sur une liste du registre et ait été formé. Le cadre n'estime ni la taille de cette population ni le coût de la formation, et ne prévoit rien pour les mandants externes (clients) qu'on ne peut pas former.
- **Contre-exemple** : Un assistant de courriel déployé à 10 000 employés : chaque envoi est P3. Soit les 10 000 employés sont inscrits et formés, soit chaque envoi passe par un approbateur central, qui sature aussitôt (voir 12-22). Pour un agent au service de clients, la règle est inapplicable telle quelle.
- **Correctif proposé** : Distinguer l'approbation par le mandant de sa propre action (authentification forte et écran fidèle, sans formation de fond) de l'approbation par un tiers habilité (risque élevé, effet sur autrui). Ou bien reclasser certains envois internes en P2 compensable. Dimensionner le bassin d'approbateurs.
- **Confiance** : déduit

### [12-14] [MAJEUR] L'édition d'une action ne déclenche pas le recalcul du contrôle exigé
- **Axe** : A
- **Localisation** : § 8.6, p. 113 : « Éditer une action revient à approuver une autre action : la passerelle calcule l'empreinte des arguments modifiés, et c'est cette version que couvre le jeton. »
- **Diagnostic** : La nouvelle action peut changer de contrôle exigé (seuil franchi, autre destinataire, passage au double approbateur) et d'indicateur de risque (EXIG-AUT-19). Le texte se contente de recalculer h. L'approbateur qui édite devient aussi l'auteur de l'action qu'il approuve, ce qui contourne le principe des quatre yeux.
- **Contre-exemple** : Un bon de commande de 4 000 $, sous le seuil de 5 000 $ et soumis à approbation à cause d'un déclencheur, est porté par l'approbateur à 9 000 $ pendant l'édition. La passerelle recalcule h et émet le jeton, mais ne réévalue pas le seuil : la seconde approbation, ou la règle du dépassement de seuil, n'est jamais appliquée.
- **Correctif proposé** : Toute édition DOIT repasser par l'EXIG-AUT-10, avec le nouvel indicateur de risque. Si le contrôle recalculé est plus strict, ou s'il exige deux approbateurs, l'éditeur ne peut pas être le seul approbateur.
- **Confiance** : déduit

### [12-15] [MINEUR] Le patron « Notifier » ne se prête pas aux champs obligatoires de l'EXIG-AUT-16
- **Axe** : C
- **Localisation** : EXIG-AUT-16, p. 113 : « Chaque demande DOIT indiquer le patron, la tâche, l'agent, l'effet attendu et une échéance fixée par cas d'usage. »; tableau 32 (Notifier) : « Signale sans agir. »
- **Diagnostic** : Une notification n'a pas d'« effet attendu ». Le texte dit qu'une demande sans réponse fait passer « la tâche » en escalade, mais il n'y a pas d'action à refuser. Le sens de l'expiration pour « Notifier » et « Questionner » n'est pas défini.
- **Contre-exemple** : Une notification « contrat reçu » non lue à l'échéance : faut-il escalader? Et quel effet attendu inscrire?
- **Correctif proposé** : Préciser les champs requis par patron et l'issue de l'expiration pour chacun.
- **Confiance** : vérifié dans le texte

### [12-16] [MINEUR] EXIG-AUT-17 : un NE DOIT PAS assorti d'une échappatoire, et une redite de la règle d'idempotence
- **Axe** : A / C
- **Localisation** : EXIG-AUT-17, p. 113 : « Un appel à effet de bord NE DOIT PAS précéder le point d'interruption dans la même étape; s'il ne peut pas être déplacé, il DOIT porter une clé d'idempotence ».
- **Diagnostic** : (a) Une interdiction qui tombe dès que l'appel « ne peut pas être déplacé » est en fait un DEVRAIT; aucun critère ne dit qui juge l'impossibilité. (b) L'exigence d'idempotence du § 7.6 (p. 93-97 : « Chaque appel d'outil en écriture (P2 ou P3) DOIT porter une clé d'idempotence dérivée de l'identifiant de la tâche et de celui de l'étape ») couvre déjà les écritures, ce qui rend la clause redondante pour elles. Elle ne couvre pas les effets de bord qui ne sont pas des écritures P2/P3 : notification, publication d'événement, appel de modèle facturé. (c) Il faut rappeler que la clé doit être dérivée de façon déterministe : une clé générée dans le nœud (UUID aléatoire) change à chaque redémarrage du nœud.
- **Contre-exemple** : Le nœud LangGraph génère `uuid4()` puis écrit avant `interrupt()`. À la reprise, le nœud repart du début, génère une autre clé et l'écriture est dupliquée.
- **Correctif proposé** : Reformuler en DOIT (effet après l'interruption) et faire de l'exception une dérogation consignée. Renvoyer à la clé déterministe du § 7.6 et étendre la règle aux effets de bord autres que P2/P3.
- **Confiance** : vérifié dans le texte (p. 113 et § 7.6)

### [12-17] [MINEUR] LangGraph : un `checkpointer` est exigé, pas nécessairement persistant
- **Axe** : A
- **Localisation** : p. 113 : « Dans LangGraph, interrupt() exige un mécanisme de points de contrôle persistant ».
- **Diagnostic** : À ma connaissance, `interrupt()` exige un `checkpointer`, qui peut être en mémoire (`InMemorySaver`). La persistance est une exigence de production, celle que pose l'EXIG-AUT-17, pas une contrainte de l'API.
- **Contre-exemple** : Un prototype avec `InMemorySaver` interrompt et reprend correctement, mais perd l'état au redémarrage du processus.
- **Correctif proposé** : « exige un mécanisme de points de contrôle (checkpointer), qui doit être persistant en production ».
- **Confiance** : à vérifier (documentation LangGraph sur `interrupt`, réf. [82])

### [12-18] [MAJEUR] L'arrêt à l'échéance, la révocation au retrait et le coupe-circuit bloquent les compensations en cours
- **Axe** : A / B
- **Localisation** : EXIG-AUT-18, p. 114 : « À l'échéance, l'agent s'arrête jusqu'à ce qu'une personne habilitée renouvelle la délégation. »; EXIG-IAM-07, p. 121 : le retrait « DOIT révoquer son identité, ses justificatifs, ses jetons actifs et ses délégations ».
- **Diagnostic** : Une saga interrompue par l'expiration de la délégation, la révocation ou le coupe-circuit (EXIG-IAM-20) n'a plus d'identité ni de délégation pour exécuter ses compensations (§ 7.5). Le cadre ne dit pas sous quelle autorité les compensations s'exécutent après un arrêt. Une recherche dans le texte complet ne trouve aucune règle qui relie compensation et suspension ou révocation (T3).
- **Contre-exemple** : Un agent ambiant N3 a débité un compte (étape 1) et doit créditer un autre compte (étape 2). La délégation expire entre les deux, l'étape 2 échoue et la compensation (recréditer) est refusée par la passerelle faute de délégation valide : l'état incohérent persiste jusqu'au renouvellement.
- **Correctif proposé** : Prévoir un état « drainage » : plus de nouvelles tâches avant l'échéance (marge au moins égale à la durée maximale d'une saga) et une autorité de compensation distincte, limitée aux outils de compensation déclarés, qui survit à l'arrêt et au coupe-circuit.
- **Confiance** : déduit (absence vérifiée par recherche dans full.txt)

### [12-19] [MINEUR] « Délégation » désigne à la fois un mandat de 12 mois et un jeton de 15 minutes
- **Axe** : C
- **Localisation** : EXIG-AUT-18, p. 114 : « La délégation qui permet à un agent ambiant de niveau N3 ou N4 d'agir DOIT expirer à une échéance inscrite à sa fiche ».
- **Diagnostic** : Au § 9.3, la délégation est l'échange de jetons RFC 8693 (EXIG-IAM-08), avec des jetons de 15 minutes ou moins (EXIG-IAM-15). Ici, c'est un mandat permanent dont l'échéance va jusqu'à 12 mois. L'EXIG-IAM-15 renvoie à l'EXIG-AUT-18 pour la « délégation de longue durée », mais le terme n'est défini nulle part dans ce sens.
- **Contre-exemple** : Un auditeur lit « délégation de 12 mois » comme un jeton délégué de 12 mois, contraire à l'EXIG-IAM-15.
- **Correctif proposé** : Introduire « mandat d'agent ambiant » (ou « autorisation permanente ») et réserver « délégation » à l'échange de jetons.
- **Confiance** : vérifié dans le texte

### [12-20] [MAJEUR] L'écran d'approbation n'est pas tenu de montrer tout ce que couvre l'empreinte
- **Axe** : A
- **Localisation** : EXIG-AUT-19, p. 114 : « L'écran d'approbation DOIT présenter l'action exacte, ses paramètres, son effet attendu ».
- **Diagnostic** : Le cadre ne dit pas que l'écran est produit à partir des arguments canonisés hachés. L'exemple C.6 (p. 221) indique que `authorization_details` sert « pour l'écran d'approbation et l'audit ». Or ce bloc ne reprend ni `lignes` (SKU, quantités, prix) ni `statut_demande`, présents dans les arguments hachés (p. 221-222). L'approbateur approuve donc une empreinte dont il n'a pas vu tout le contenu. La propriété « ce que l'on voit est ce que l'on signe », au cœur de la thèse T5, n'est pas garantie.
- **Contre-exemple** : Une injection fait remplacer un SKU par un article non autorisé, au même total. L'écran tiré de `authorization_details` affiche fournisseur, total et centre de coût, tous corrects. L'approbateur approuve et h concorde, puisque l'action approuvée est bien l'action piégée.
- **Correctif proposé** : L'écran DOIT être une fonction totale et déterministe des arguments canonisés (tous les champs, ou les champs omis listés au catalogue comme non significatifs). `authorization_details` DOIT être dérivé des arguments, et non fourni à côté.
- **Confiance** : vérifié dans le texte (p. 114, 221-222)

### [12-21] [MINEUR] « Ce que la figure 15 classe à faible risque » : la figure ne classe pas de risque
- **Axe** : C
- **Localisation** : ATTENTION, p. 114 : « automatise ce que la figure 15 classe à faible risque ».
- **Diagnostic** : La figure 15 donne des contrôles (« Automatique »), pas des niveaux de risque. L'expression se confond avec la « classe faible », un autre axe que § 3.1 interdit de confondre.
- **Contre-exemple** : Un lecteur comprend « automatise les agents de classe faible ».
- **Correctif proposé** : « automatise ce dont le contrôle calculé (EXIG-AUT-10) est automatique ».
- **Confiance** : vérifié dans le texte

### [12-22] [MAJEUR] Fréquence plafonnée par approbateur : la saturation n'est pas traitée
- **Axe** : B
- **Localisation** : EXIG-AUT-20, p. 115 : « La fréquence des demandes adressées à chaque approbateur DOIT être plafonnée selon un seuil fixé par le comité ».
- **Diagnostic** : Un plafond par approbateur et un bassin fini donnent une capacité totale finie. Le texte ne dit pas ce qui arrive aux demandes au-delà : file d'attente, refus, ou suspension de la tâche selon l'EXIG-AUT-11? L'expiration en refus n'est prévue que pour les agents ambiants (EXIG-AUT-16). Rien n'exige de dimensionner le bassin selon le volume prévu. Sous la menace T10, la priorisation par risque permet à un attaquant d'affamer les demandes légitimes en inondant la file de demandes à risque élevé.
- **Contre-exemple** : Une campagne d'injection fait produire 5 000 demandes P3 par heure. Avec 10 approbateurs plafonnés à 30 demandes par heure, la capacité est de 300 : toutes les demandes légitimes de moindre priorité expirent ou attendent sans fin, ce qui revient à un déni de service.
- **Correctif proposé** : Exiger un dimensionnement (volume prévu × marge) au registre; un plafond de demandes par agent et par tâche, en plus du plafond par approbateur; une issue définie au dépassement (suspension et coupe-circuit automatique de l'agent émetteur au-delà d'un seuil).
- **Confiance** : déduit

### [12-23] [MAJEUR] Échantillonnage a posteriori à proportion fixe : coût non borné et puissance statistique nulle
- **Axe** : B
- **Localisation** : EXIG-AUT-21, p. 115 : « une revue humaine a posteriori DOIT porter sur un échantillon d'au moins 5 % des actions de classe modérée et 1 % de celles de classe faible ».
- **Diagnostic** : (a) L'unité « action » n'est pas définie (appel d'outil, tâche, écriture seulement?). (b) Une proportion fixe donne, à fort volume, une charge humaine énorme qui concurrence les approbations (EXIG-AUT-20). À faible volume, l'échantillon est trop petit pour détecter quoi que ce soit. (c) Si un cas d'usage n'a qu'un ou deux approbateurs, l'écart à la médiane ne détecte rien. Aucun objectif de détection, par exemple un taux d'erreur à détecter avec une confiance donnée, ne fonde les pourcentages, ce que la note « choix du cadre » reconnaît sans le justifier.
- **Contre-exemple** : Un agent modéré qui fait 2 millions d'appels P2 par mois impose 100 000 revues mensuelles. Un agent faible qui fait 80 actions par mois en impose une seule.
- **Correctif proposé** : Définir l'unité (action à effet). Remplacer la proportion par un échantillon stratifié par risque, avec un minimum absolu et un plafond, calculé pour détecter un taux d'anomalie cible avec une confiance fixée par le comité. Exiger au moins trois approbateurs, ou une référence entre cas d'usage, pour la comparaison à la médiane.
- **Confiance** : déduit

### [12-24] [MAJEUR] Révision « significative » jugée par une mesure mensuelle a posteriori, alors que l'avis est dû au moment de la décision
- **Axe** : A
- **Localisation** : EXIG-AUT-23, p. 116 : « exerce une influence réelle mesurée par l'EXIG-AUT-21 ».
- **Diagnostic** : L'EXIG-AUT-21 produit des indicateurs mensuels agrégés par approbateur. La qualification « exclusivement automatisée » d'une décision donnée en dépend, alors que l'avis de l'art. 12.1 (EXIG-AUT-22, EXIG-CON-07) est dû « au plus tard au moment de la communication de la décision ». Au moment de décider, l'obligation est donc indécidable. Les autres critères (« compétence voulue », « temps nécessaire ») n'ont pas de mesure : l'exigence n'est pas « vérifiable en revue ou en test » (§ 1.5). Le cas « mesure non encore disponible » (premier mois, nouvel approbateur) n'est pas couvert non plus.
- **Contre-exemple** : Un nouveau cas d'usage N2 au premier mois : aucune mesure de l'EXIG-AUT-21 n'existe. Faut-il envoyer l'avis de l'art. 12.1? Si, au mois 2, la mesure révèle une approbation machinale, les décisions du mois 1 étaient exclusivement automatisées et sans avis, motif de sanction (art. 90.1).
- **Correctif proposé** : Qualifier la décision a priori, par cas d'usage, dans l'EFVP, avec un défaut prudent (« exclusivement automatisée » tant que la preuve contraire n'est pas consignée). Utiliser l'EXIG-AUT-21 comme contrôle a posteriori qui déclenche la requalification et, au besoin, des avis rétroactifs. Donner des critères mesurables : temps minimal d'examen, accès aux données sources consigné.
- **Confiance** : vérifié dans le texte (raisonnement déduit)

### [12-25] [MAJEUR] EXIG-AUT-22/23 et EXIG-CON-07/08/09 : obligations légales en double, au contenu divergent
- **Axe** : C
- **Localisation** : EXIG-AUT-23, p. 116 (cinq conditions : autorité, compétence, accès à toutes les données, temps, influence mesurée); EXIG-CON-08, p. 176 : « l'information sur la décision et ses facteurs, le temps nécessaire pour l'examiner, l'autorité de la modifier ou de l'annuler ».
- **Diagnostic** : Deux paires d'exigences normatives encadrent la même obligation légale, sans être identiques. L'EXIG-AUT-23 pose cinq conditions, l'EXIG-CON-08 trois. L'EXIG-CON-07 ajoute « importance relative » des facteurs, un membre du personnel « nommément désigné » et un délai de 30 jours, absents de l'EXIG-AUT-22. L'EXIG-CON-09 conserve aussi les versions et les approbations, l'EXIG-AUT-22 seulement « les renseignements utilisés ». Ce n'est pas une contradiction stricte, puisque l'EXIG-CON-08 ne pose que des conditions nécessaires, mais un auditeur qui part du chapitre 8 omet trois obligations du chapitre 12. Comme la sanction est pécuniaire, la redondance coûte cher.
- **Contre-exemple** : Une équipe met en œuvre l'EXIG-AUT-22 à la lettre : un canal générique, sans personne désignée ni délai, ne satisfait pas l'EXIG-CON-07.
- **Correctif proposé** : Garder une seule source normative (EXIG-CON-07 à 09). Réduire l'EXIG-AUT-22 à « DOIT être de classe élevée et satisfaire aux EXIG-CON-07 à CON-09 », et aligner les conditions de l'EXIG-AUT-23 et de l'EXIG-CON-08, ou faire renvoyer l'une à l'autre.
- **Confiance** : vérifié dans le texte (p. 116, 176-177)

### [12-26] [MINEUR] Portée ambiguë de l'EXIG-AUT-22, plus large que le critère du tableau 46
- **Axe** : C
- **Localisation** : EXIG-AUT-22, p. 116 : « Tout agent qui rend une décision concernant une personne, ou la prépare sans révision humaine significative, à partir d'un traitement automatisé de ses RP DOIT être de classe élevée ».
- **Diagnostic** : Deux lectures sont possibles : « sans révision humaine significative » qualifie seulement « prépare », ou bien les deux verbes. Dans la première lecture, tout agent qui « rend » une décision, même révisée, est de classe élevée et doit donner l'avis de l'art. 12.1, ce qui va au-delà du tableau 46 (« décision fondée exclusivement sur un traitement automatisé »). Comme la classe élevée plafonne à N2 et que chaque action y est approuvée, « rendre » seul une décision n'est possible que si l'approbation est nominale. Le texte gagnerait à l'écrire.
- **Contre-exemple** : Un agent N2 rédige une décision de crédit qu'un analyste révise vraiment. Selon la lecture retenue, l'avis de l'art. 12.1 est dû ou non.
- **Correctif proposé** : « Tout agent dont les décisions concernant une personne sont, au sens de l'EXIG-AUT-23, fondées exclusivement sur un traitement automatisé de ses RP… », en concordance avec le tableau 46.
- **Confiance** : vérifié dans le texte (p. 116, 171)

### [12-27] [MINEUR] L'EXIG-IAM-02 omet les appels aux modèles, que le tableau 33 place sous un point d'application
- **Axe** : C
- **Localisation** : EXIG-IAM-02, p. 119 : « Chaque appel d'un agent vers un outil, une ressource ou un autre agent DOIT être authentifié et autorisé individuellement. »; tableau 33, PEP : « passerelle de modèles pour les appels vers les modèles ».
- **Diagnostic** : Le tableau fait de la passerelle de modèles un PEP, mais l'exigence de décision par appel ne vise pas les modèles. Cela compte pour le budget et les données sensibles envoyées à un modèle externe.
- **Contre-exemple** : Un agent envoie à un modèle externe un contexte chargé de RP sensibles, sans décision par appel exigée.
- **Correctif proposé** : Ajouter « ou un modèle » à l'EXIG-IAM-02, ou expliquer pourquoi les appels aux modèles relèvent d'une autre exigence.
- **Confiance** : vérifié dans le texte

### [12-28] [MAJEUR] Décision par appel selon l'état de la tâche : course possible entre répliques de passerelle
- **Axe** : A / B
- **Localisation** : EXIG-IAM-02, p. 119 : décision « rendue d'après l'identité de l'agent, le mandant, le palier de l'outil, le niveau d'autonomie, l'état de la tâche et les signaux de risque »; EXEMPLE : « la passerelle sait que la session a consommé du contenu non fiable ».
- **Diagnostic** : La garantie suppose que le marquage « contenu non fiable lu » et le budget consommé soient visibles, de façon cohérente, de toute instance qui décide de l'appel suivant. Le cadre ne fixe ni où cet état est tenu, ni sa cohérence (lecture de sa propre écriture par tâche), ni le refus en mode fermé si l'état est indisponible. La même lacune concerne les appels parallèles d'un modèle (thèse T4).
- **Contre-exemple** : La réponse de lecture du courriel externe traverse la réplique A, dont le marquage met 200 ms à se propager. L'appel d'envoi, émis aussitôt après, arrive à la réplique B, qui voit une tâche « propre » et laisse passer.
- **Correctif proposé** : Exiger que l'état de la tâche pris en compte par la politique soit tenu dans un magasin à cohérence forte par tâche, ou que les appels d'une même tâche aillent toujours à la même instance. Si l'état est indisponible ou périmé, appliquer l'EXIG-IAM-18 (refus).
- **Confiance** : déduit

### [12-29] [MINEUR] L'exemple de l'EXIG-IAM-02 illustre mal la décision par appel
- **Axe** : C
- **Localisation** : EXEMPLE, p. 119 : « il tente d'appeler l'outil d'envoi de courriels » … « Une autorisation accordée à l'ouverture de la session l'aurait laissé passer. »
- **Diagnostic** : La figure 15 classe l'« envoi » en P3, et l'EXIG-AUT-09 impose une approbation à chaque appel P3, quel que soit l'état de la session. L'envoi aurait donc été bloqué même avec une autorisation de session : l'exemple ne montre pas l'apport de la décision par appel.
- **Contre-exemple** : Sans contenu non fiable lu, le même envoi exige aussi une approbation.
- **Correctif proposé** : Prendre un outil P2 interne (p. ex. écriture dans un dossier client), autorisé seul sous le seuil, qui ne bascule en approbation qu'à cause du contenu non fiable (règle de deux).
- **Confiance** : vérifié dans le texte (p. 109, 119)

### [12-30] [MINEUR] « Toute communication… mutuellement authentifiée et chiffrée » contre stdio local; force normative implicite
- **Axe** : A / C
- **Localisation** : EXIG-IAM-01, p. 119 : « Toute communication entre composants est mutuellement authentifiée et chiffrée, y compris à l'intérieur d'un réseau privé. »
- **Diagnostic** : Le cadre permet MCP en stdio sur un poste de développement (EXIG-MCP-08, p. 53 et suivantes), un transport sans authentification mutuelle ni chiffrement au sens réseau. La phrase est en plus à l'indicatif dans un bloc NE DOIT PAS : sa force normative est implicite.
- **Contre-exemple** : Un serveur MCP stdio local, conforme à l'EXIG-MCP-08, contrevient à la lettre de l'EXIG-IAM-01.
- **Correctif proposé** : « Toute communication réseau entre composants DOIT être… (mTLS); les communications locales par stdio relèvent de l'EXIG-MCP-08. »
- **Confiance** : vérifié dans le texte

### [12-31] [MINEUR] « Renouvelé automatiquement » ne convient pas au JWT-SVID
- **Axe** : C
- **Localisation** : EXIG-IAM-04, p. 120 : « de courte durée, renouvelé automatiquement et valide au plus pour la vie de l'instance »; p. 119 : « le JWT-SVID, de courte durée, est redemandé au besoin ».
- **Diagnostic** : Le texte distingue lui-même le renouvellement automatique (X.509-SVID) de la demande au besoin (JWT-SVID), puis exige les deux propriétés de chacune des options.
- **Contre-exemple** : Un vérificateur strict déclare non conforme tout JWT-SVID.
- **Correctif proposé** : « renouvelé automatiquement ou réémis à la demande par la plateforme ».
- **Confiance** : vérifié dans le texte

### [12-32] [MINEUR] Le gabarit Entra Agent ID n'est pas confronté aux EXIG-IAM-03 à 05
- **Axe** : B
- **Localisation** : p. 120 : « elle obtient ses jetons par un gabarit (agent identity blueprint) qui porte les justificatifs et les politiques d'accès conditionnel héritées par toutes ses identités ».
- **Diagnostic** : Le cadre présente cette mise en œuvre sans la confronter à ses propres exigences. Les justificatifs du gabarit sont partagés par toutes les identités qui en dépendent (NHI9) et peuvent être un secret client de longue durée (EXIG-IAM-05). La notion de « vie de l'instance » (EXIG-IAM-04) n'a pas d'équivalent évident sur une plateforme SaaS. La conformité semble possible (justificatif fédéré, identité gérée), mais n'est pas démontrée.
- **Contre-exemple** : Un gabarit doté d'un secret client de deux ans : toutes les identités d'agent qui en dépendent reposent sur un secret statique partagé.
- **Correctif proposé** : Ajouter au catalogue un profil par plateforme qui exige des justificatifs de gabarit fédérés ou gérés, sans secret, et définit l'« instance ».
- **Confiance** : à vérifier (documentation Microsoft Entra Agent ID, réf. [90])

### [12-33] [MINEUR] Orphelins : EXIG-IAM-07 et EXIG-GOV-13 ne disent pas la même chose
- **Axe** : C
- **Localisation** : EXIG-IAM-07, p. 121 : « Une revue trimestrielle détecte les agents orphelins (sans parrain, sans fiche à jour ou inactifs), qui sont désactivés »; EXIG-GOV-13 (p. 167 environ) : « désactiver ceux qui ne sont pas régularisés ».
- **Diagnostic** : L'EXIG-IAM-07 désactive sans condition, l'EXIG-GOV-13 laisse un délai de régularisation. L'objet de l'attestation diffère aussi : « encore requis » à l'EXIG-IAM-07, mais finalité, mandants, portées, classe et niveau à l'EXIG-GOV-13. La section 11.3 prévoit en outre une suspension après 30 jours de rôle vacant.
- **Contre-exemple** : Un agent sans parrain depuis 10 jours est-il désactivé (IAM-07) ou en régularisation (GOV-13, 30 jours)?
- **Correctif proposé** : Faire renvoyer l'EXIG-IAM-07 à l'EXIG-GOV-13 pour la revue et l'attestation, et ne garder que la révocation technique.
- **Confiance** : vérifié dans le texte

### [12-34] [MINEUR] NHI3 rattaché à l'EXIG-IAM-17 : correspondance faible
- **Axe** : C
- **Localisation** : tableau 34, p. 121 : NHI3 → « EXIG-IAM-17; chaîne d'approvisionnement (section 9.8); clauses (section 13.3) ».
- **Diagnostic** : NHI3 vise les identités non humaines que détiennent des tiers : applications OAuth et intégrations de fournisseurs qui accèdent à vos systèmes. L'EXIG-IAM-17 (passage obligatoire par la passerelle d'agents) ne régit que les appels de vos agents, pas les accès entrants des fournisseurs. Aucune exigence nommée ne prévoit l'inventaire et la revue des octrois accordés à des tiers.
- **Contre-exemple** : Une intégration SaaS tierce dotée d'un octroi OAuth étendu sur la messagerie n'est touchée par aucune exigence du tableau.
- **Correctif proposé** : Rattacher NHI3 à une exigence d'inventaire et de revue des identités et octrois de tiers (§ 9.8 ou § 13.3), ou le déclarer partiellement couvert.
- **Confiance** : déduit (portée de NHI3 d'après mes connaissances de l'OWASP NHI Top 10)

## Points forts
La liaison cryptographique de l'approbation à l'action exacte (h, usage unique, expiration, `typ` distinct d'`at+jwt` en C.6), complétée par la liste explicite de ce qui n'est jamais une approbation, est un mécanisme solide et testable dans son principe.
Le texte distingue avec soin l'exigence externe du choix du cadre (seuils de 5 % et 1 %, second approbateur, rotation, analogie avec l'art. 65.2) et signale ses limites (« Aucune source reconnue ne fixe de seuil universel »).
Le tableau 33 transpose la SP 800-207 sans la trahir, et le passage de la décision par session à la décision par appel est justifié de façon convaincante pour des agents dont le comportement change en cours de tâche.

## Questions pour l'audit bibliographique
- p. 111 : A2A 1.0 emploie-t-il la RFC 8785 pour signer les cartes d'agent (signatures JWS d'AgentCard)? Trancher dans la spécification A2A 1.0 (a2a.proto et section sur les signatures), réf. [68].
- p. 112 : le brouillon WIMSE AIMS (draft-ietf-wimse-aims-00, 15 sept. 2026) dit-il qu'une confirmation locale dans l'interface ne suffit pas comme autorisation, et cite-t-il CIBA avec ses limites en cours d'exécution? Réf. [93], [309].
- p. 112 : RIA, art. 26, par. 2 (compétence, formation, autorité des personnes chargées du contrôle humain) : numérotation à confirmer dans le texte consolidé, réf. [94].
- p. 113 : dépôt `langchain-ai/agent-inbox` archivé en lecture seule depuis le 20 septembre 2026? Réf. [313]. Le billet LangChain sur les agents ambiants date-t-il de janvier 2025 et contient-il les trois patrons? Réf. [86].
- p. 113 : la recommandation de Microsoft de distinguer approbation et rétroaction et de persister l'état aux points d'approbation est-elle bien dans [9]?
- p. 114 : RIA modifié par le règlement (UE) 2026/1744 : application de l'art. 14 au 2 décembre 2027 (annexe III) et au 2 août 2028 (annexe I). L'annexe H.5 reconnaît que le texte n'a pas pu être relu sur EUR-Lex. Réf. [58], [315].
- p. 114 : OpenAI [291] recommande-t-il des expirations périodiques qui gardent l'agent à l'arrêt jusqu'à réautorisation? Contrôler la formulation exacte.
- p. 114 : OWASP T10 « Overwhelming Human in the Loop » [87]; ASI09 « Human-Agent Trust Exploitation » [28] et sa recommandation d'un résumé de risque en langage clair plutôt qu'une justification produite par le modèle (p. 114, Pourquoi de l'EXIG-AUT-19).
- p. 115 : Loi sur le privé, art. 90.1, par. 5° : le défaut visé par l'art. 12.1 y figure-t-il bien comme motif de sanction administrative pécuniaire? Réf. [56], [317].
- p. 115-116 : source de l'« interprétation gouvernementale » de l'art. 65.2 [318] : existence, date, et mention du mot « principaux »; absence de critères publiés par la CAI pour le secteur privé (encadré DROIT APPLICABLE, p. 116).
- p. 119 : dates de passage au niveau Graduated de SPIFFE (23 août 2022) et de SPIRE (22 août 2022) contre l'annonce de la CNCF du 20 septembre 2022, réf. [116], [117], [321]. L'annexe H.5 indique que SPIFFE et SPIRE n'ont pas été relus.
- p. 120 : draft-ietf-wimse-workload-identity-practices-07 du 22 sept. 2026, soumis à l'IESG le 30 juin 2026 : une version -07 postérieure à la soumission est plausible, mais à confirmer sur le Datatracker, réf. [323].
- p. 120 : création automatique d'une identité Entra Agent ID par Copilot Studio depuis juillet 2026 [48]; licence Microsoft Agent 365 requise pour l'accès conditionnel et la protection des identités [324].
- p. 121 : périodicité d'attestation de 6 à 12 mois et revue trimestrielle des orphelins recommandées par Microsoft [92]; livre blanc de l'OpenID Foundation annoncé le 7 octobre 2025, avec recommandation SCIM DELETE [311], [325].
