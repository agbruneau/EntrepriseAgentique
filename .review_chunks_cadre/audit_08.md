# Audit chunk_08 — pages 71-82

## Synthèse
Le chunk couvre la fin du § 6.6 (A2A 1.0 : suivi des tâches, liaisons, sécurité, figure 9, migration), tout le § 6.7 (CloudEvents, AsyncAPI, extensions de gouvernance, compteur de sauts, garanties Kafka) et le début du § 6.8 (contrats, SemVer, coexistence, épinglage). Les faits sont précis et sourcés, et le texte sépare bien « exigence externe » et « choix du cadre ». En revanche, la gouvernance événementielle tient mal à l'échelle d'un système. Les trois défauts les plus graves : (1) le bus d'événements contourne la passerelle, l'intersection des droits et la limite de délégation [08-20]; (2) le compteur de sauts ne borne ni les boucles qui passent par un système non agentique (l'exemple même du texte) ni l'amplification par diffusion [08-16, 08-17]; (3) le jeton d'approbation à usage unique entre en conflit avec le réessai idempotent de l'écriture P3 de la figure 9 [08-08].
Pages de recouvrement : pour les p. 71-72 et 81-82, seuls les constats qui exigent l'autre côté de la couture sont retenus.

## Constats

### [08-01] [MAJEUR] La figure 9 enfreint EXIG-A2A-07 et la justification vaut aussi contre le flux SSE
- **Axe** : A
- **Localisation** : § 6.6, EXIG-A2A-07 (p. 71); figure 9, étapes 3 et 7 (p. 74). « le client DOIT la suivre par flux en continu (SendStreamingMessage) ou par notification push » ; étape 7 : « SendMessage (même taskId) + approbation ».
- **Diagnostic** : selon la p. 71, SendMessage « attend que la tâche atteigne un état terminal ou interrompu ». Or l'étape 7 relance par un SendMessage bloquant une tâche qui va ensuite écrire dans l'ERP (étapes 8-9), donc une tâche dont la durée n'est pas bornée, et c'est le patron même que l'exigence proscrit. La justification (« une connexion bloquante longue se heurte aux délais des intermédiaires réseau ») s'applique aussi au flux SSE ouvert à l'étape 3 : c'est une connexion HTTP longue, exposée aux délais d'inactivité des mandataires, et l'attente d'une approbation humaine peut durer des heures. Enfin, « durée attendue » n'est pas mesurable : qui l'estime, et sur quelle base?
- **Contre-exemple** : l'approbateur répond en 40 minutes. Le répartiteur de charge coupe le flux SSE après 60 s d'inactivité, et le client doit appeler SubscribeToTask, ce qui est interdit « pour le suivi courant ». L'étape 7 bloque ensuite la connexion pendant l'écriture ERP.
- **Correctif proposé** : à l'étape 7, employer SendStreamingMessage, ou SendMessage avec `returnImmediately: true` puis le flux ou la notification push. Exiger des battements de cœur ou une durée maximale de flux, et permettre explicitement la reprise par SubscribeToTask après un état interrompu. Faire déclarer au catalogue, par compétence, la durée attendue (p95 mesuré).
- **Confiance** : vérifié dans le texte (incohérence); déduit (comportement des intermédiaires).

### [08-02] [MAJEUR] EXIG-A2A-08 et EXIG-A2A-15 se contredisent, et la règle de refus a des trous
- **Axe** : A, C
- **Localisation** : EXIG-A2A-08 (p. 72) « Tout client A2A DOIT envoyer A2A-Version à chaque requête »; EXIG-A2A-15 (p. 75) « Passé cette date, la passerelle DOIT refuser les requêtes sans en-tête A2A-Version »; p. 71 « Un en-tête vide est interprété comme la version 0.3 … ou le paramètre de requête équivalent ».
- **Diagnostic** : (a) un client 0.3, que la double publication de l'EXIG-A2A-15 sert justement à tolérer, n'envoie pas l'en-tête et enfreint donc l'EXIG-A2A-08 (DOIT, sans délai) pendant toute la période de coexistence. (b) Après le retrait, la règle ne refuse que les requêtes « sans en-tête ». Elle laisse passer un en-tête vide, que la spécification lit comme 0.3, et un en-tête explicite « 0.3 ». À l'inverse, elle refuse un client 1.0 conforme qui passe la version par le paramètre de requête que la spécification admet. (c) Un DOIT est imbriqué dans un bloc DEVRAIT : si l'agent ne fait pas de double publication, aucune date de retrait n'existe et le DOIT ne se déclenche jamais.
- **Contre-exemple** : après la date de retrait, `A2A-Version: 0.3` ou `A2A-Version:` (vide) passe, alors que `?A2A-Version=1.0` est rejeté.
- **Correctif proposé** : à l'EXIG-A2A-08, ajouter « sauf client 0.3 pendant la période de l'EXIG-A2A-15 ». Dans l'EXIG-A2A-15, remplacer la règle de refus par « refuser toute requête dont la version effective (en-tête ou paramètre; absent ou vide valant 0.3) n'est pas prise en charge ». Sortir la règle de la passerelle dans une exigence DOIT distincte.
- **Confiance** : vérifié dans le texte.

### [08-03] [MAJEUR] L'autorisation par compétence n'est pas applicable par la passerelle
- **Axe** : A, B
- **Localisation** : EXIG-A2A-10 (p. 73) « Chaque compétence publiée DOIT être associée à une portée OAuth dédiée … un jeton valide pour analyser un dossier ne doit pas permettre d'accorder un prêt ».
- **Diagnostic** : SendMessage adresse un agent, pas une compétence. À ma connaissance, aucun champ normalisé d'un message A2A 1.0 ne désigne l'AgentSkill visée : c'est l'agent serveur, donc le modèle, qui décide quelle compétence il exécute. Une portée par compétence ne peut donc être vérifiée ni par la passerelle (en amont) ni de façon déterministe par le serveur, à moins que le routage vers la compétence soit lui-même déterministe. La phrase sur le locataire est aussi ambiguë : « sans jamais le déduire du seul contenu de la requête », alors que le tenant demandé est précisément dans la requête.
- **Contre-exemple** : un jeton portant la seule portée `analyse-dossier` envoie « analyse puis accorde le prêt ». La passerelle voit un SendMessage valide vers l'agent crédit, et le modèle invoque la compétence d'octroi.
- **Correctif proposé** : exiger un identifiant de compétence porté par une métadonnée ou une extension approuvée (EXIG-A2A-05), vérifié par la passerelle contre la portée, et un routage déterministe côté serveur vers la compétence déclarée. À défaut, une compétence par point de terminaison ou par agent. Reformuler la phrase sur le locataire : « le tenant demandé DOIT figurer parmi les locataires autorisés par le jeton ».
- **Confiance** : déduit; à vérifier dans a2a.proto, qui tranche sur l'absence d'un champ de compétence dans Message ou SendMessageRequest.

### [08-04] [MINEUR] EXIG-A2A-11 : flux Device Code sans garde-fou, méthode d'authentification du client non précisée, force mal étiquetée
- **Axe** : B, C
- **Localisation** : EXIG-A2A-11 (p. 73), « NE DOIT PAS » … « Ils DOIVENT utiliser … (ou le Device Code pour un appareil sans navigateur) … les justificatifs client pour un agent qui agit en son nom propre ».
- **Diagnostic** : (a) Le flux Device Code (RFC 8628) est le vecteur connu de l'hameçonnage par code d'appareil. Il est admis ici sans condition (liste d'applications autorisées, durée courte, accès conditionnel). (b) « Justificatifs client » n'exclut pas le `client_secret`, alors que le PRIN-03 interdit le secret partagé et que le § 9 retient SVID, mTLS ou private_key_jwt. (c) Le bloc est étiqueté NE DOIT PAS mais porte trois DOIVENT.
- **Contre-exemple** : un agent interne en client_credentials avec `client_secret` statique respecte la lettre de l'EXIG-A2A-11 et enfreint le PRIN-03.
- **Correctif proposé** : « justificatifs client authentifiés par mTLS, private_key_jwt ou SVID, jamais par secret partagé »; restreindre le Device Code aux clients inscrits au catalogue, avec accès conditionnel; étiqueter le bloc DOIT.
- **Confiance** : vérifié dans le texte; déduit (risque d'hameçonnage).

### [08-05] [MINEUR] Références en double ou incohérentes pour un même fait A2A 1.0
- **Axe** : C
- **Localisation** : p. 72 « retire les flux OAuth implicite et par mot de passe … [30] »; EXIG-A2A-11 (p. 73) « A2A 1.0 a retiré ces flux[240] »; p. 75 « … SendStreamingMessage [235] ».
- **Diagnostic** : [235] (« What's New in A2A Protocol v1.0 », github.com/a2aproject) et [240] (« What's New in A2A Protocol v1.0 », a2a-protocol.org) désignent le même document sous deux URL. Le même retrait est appuyé tantôt sur [30] (page des versions publiées), tantôt sur [240].
- **Correctif proposé** : fusionner [235] et [240]; citer une seule source pour le retrait des flux.
- **Confiance** : vérifié dans le texte (annexe G).

### [08-06] [MAJEUR] EXIG-A2A-12 bloque les récepteurs internes et omet des vecteurs SSRF que le cadre traite ailleurs
- **Axe** : A, B
- **Localisation** : EXIG-A2A-12 (p. 73) « valider l'URL de webhook contre la SSRF … après résolution DNS (plages privées, boucle locale et lien-local refusées) »; p. 72, liste IPv4 de la spécification.
- **Diagnostic** : (a) Dans l'entreprise, les orchestrateurs clients résident en général sur des adresses RFC 1918. Refuser les plages privées interdit donc les notifications push internes, alors que l'EXIG-A2A-07 impose le flux ou le push. (b) Vérifier après résolution n'empêche pas le rebinding DNS si la connexion résout l'adresse une seconde fois (TOCTOU). Rien n'est dit des redirections HTTP, de l'IPv6 (::1, fc00::/7, fe80::/10, ::ffff:10.0.0.1), de 0.0.0.0 ni de 100.64.0.0/10, alors que l'exigence CIMD du § 6.5 (p. 62) impose de « ne pas suivre les redirections, bloquer les adresses à usage spécial ». (c) L'EXIG-A2A-09 fait passer « tout échange A2A » par la passerelle, mais ne dit pas si l'appel sortant du webhook la traverse. (d) Les reprises ne sont bornées ni en nombre ni en durée.
- **Contre-exemple** : `cb.attaquant.example` résout vers 203.0.113.5 au contrôle, puis vers 169.254.169.254 à la connexion; ou bien il répond 302 vers `http://[::ffff:a9fe:a9fe]/`.
- **Correctif proposé** : épingler l'adresse résolue pour la connexion; refuser les redirections; appliquer la liste IANA des adresses à usage spécial en IPv4 et en IPv6; faire sortir les webhooks par la passerelle d'agents (égress contrôlé), avec une liste d'autorisation des récepteurs internes inscrits au catalogue; borner les reprises (p. ex. 5 essais ou 24 h).
- **Confiance** : vérifié dans le texte; déduit (vecteurs SSRF).

### [08-07] [MINEUR] EXIG-A2A-13 propage traceparent vers les agents tiers sans règle de sortie
- **Axe** : B
- **Localisation** : EXIG-A2A-13 (p. 73) « Chaque appel A2A DOIT propager l'en-tête W3C traceparent ».
- **Diagnostic** : l'EXIG-OBS-02 (p. 146) ne traite que le contexte entrant (redémarré à la frontière). Envoyer l'identifiant de trace interne à un agent tiers expose de l'information et laisse ce tiers corréler les appels de l'entreprise, ce que la spécification W3C range parmi ses considérations de confidentialité.
- **Correctif proposé** : « vers un agent hors périmètre, la passerelle DOIT ouvrir une nouvelle trace et relier l'interne par un lien de span ».
- **Confiance** : déduit.

### [08-08] [MAJEUR] Figure 9, étape 8 : le jeton d'approbation à usage unique et le réessai idempotent sont incompatibles
- **Axe** : A
- **Localisation** : figure 9, étape 8 (p. 74) « appelle l'outil d'écriture de l'ERP avec le jeton d'approbation et une clé d'idempotence (section 7.6) »; EXIG-AUT-12 (p. 111) : jeton à usage unique, h = outil + arguments canonisés, expiration de 15 minutes; EXIG-ORC-21 (p. 98) : la clé voyage dans l'en-tête Idempotency-Key ou dans un champ du contrat.
- **Diagnostic** : (a) Si la clé est un champ du contrat, elle entre dans h et doit être connue dès l'étape 5. Or l'étape 5 ne mentionne qu'« outil, arguments, montant », et l'étape 8 semble l'ajouter après coup, ce qui donne un h différent et un refus. Si la clé passe par l'en-tête, elle sort de h et l'approbation ne la lie pas. (b) Si l'appel ERP expire sans réponse (issue inconnue), la passerelle a déjà consommé le jeton. Le réessai idempotent, qui est justement le moyen sûr de lever le doute, est alors refusé : il faut une nouvelle approbation humaine, sinon l'écriture reste dans un état indéterminé.
- **Contre-exemple** : le premier essai atteint l'ERP, la réponse se perd, le réessai avec la même clé est rejeté (« jeton déjà utilisé ») et la tâche passe à FAILED alors que l'écriture a eu lieu.
- **Correctif proposé** : fixer la clé d'idempotence avant l'approbation et l'inclure dans h; définir l'usage unique comme « une seule clé d'idempotence par jeton », ce qui admet les réessais de la même clé jusqu'à l'expiration, avec une vérification côté ERP (EXIG-ORC-22).
- **Confiance** : déduit, à partir du texte des p. 74, 98 et 111.

### [08-09] [MINEUR] Figure 9 : annulation non atomique, tâche orpheline, rôle d'approbateur confondu avec l'utilisateur
- **Axe** : B
- **Localisation** : p. 74 « Si l'approbateur refuse ou si le délai d'approbation expire, l'orchestrateur annule la tâche (CancelTask) et aucune écriture n'a lieu »; couloir « Utilisateur et approbateur ».
- **Diagnostic** : (a) Dans A2A, CancelTask est une demande que l'agent peut refuser (TaskNotCancelableError). Si une approbation tardive arrive pendant que l'annulation est en cours, l'écriture peut déjà être partie, et « aucune écriture » n'est garantie que par le jeton, pas par l'annulation. (b) Si l'orchestrateur tombe, la tâche reste à INPUT_REQUIRED indéfiniment : aucun délai côté serveur. (c) Le couloir unique « Utilisateur et approbateur » laisse croire que le demandeur peut s'approuver lui-même. La séparation des fonctions du § 11 vise le cycle de vie, pas les actions P3.
- **Correctif proposé** : faire expirer côté serveur les états interrompus; écrire « aucune écriture sans jeton valide »; distinguer les couloirs, ou préciser si un demandeur peut approuver sa propre demande P3.
- **Confiance** : déduit.

### [08-10] [MAJEUR] La conformité a2a-tck n'est revérifiée qu'au changement de carte
- **Axe** : B
- **Localisation** : EXIG-A2A-14 (p. 75) « avant son inscription au registre et à chaque nouvelle version mineure ou majeure de sa carte »; p. 82, correctif : « correction qui ne change ni la définition publiée ni le comportement attendu ».
- **Diagnostic** : la trousse vérifie l'implémentation, pas la carte. Une mise à jour de SDK ou du code serveur (que la p. 75 rend probable pour le SDK JavaScript, en disponibilité générale tardive) ne change ni la carte ni sa version majeure ou mineure, et échappe donc au test. La justification (« la conformité se prouve par un test reproductible ») n'est pas tenue.
- **Correctif proposé** : rejouer les tests MUST dans la chaîne d'intégration à chaque déploiement de l'agent (l'interface en ligne de commande citée p. 75 s'y prête), en plus des changements de carte.
- **Confiance** : déduit.

### [08-11] [MINEUR] L'argument topologique ne distingue pas le bus de l'architecture du cadre
- **Axe** : B
- **Localisation** : § 6.7 (p. 75) « relier N agents deux à deux exige jusqu'à N(N−1)/2 liaisons, alors que N agents reliés à un courtier n'en exigent que N ».
- **Diagnostic** : l'arithmétique est juste, mais le cadre fait déjà passer tout appel A2A et MCP par la passerelle (EXIG-A2A-09), ce qui donne aussi N connexions. Le gain de connexions n'est donc pas un argument du bus face à A2A dans ce cadre; seul le découplage logique, que le texte mentionne ensuite, en est un.
- **Correctif proposé** : comparer à la topologie en étoile de la passerelle, ou retirer l'argument.
- **Confiance** : vérifié dans le texte.

### [08-12] [MINEUR] datacontenttype et dataschema sont obligatoires sur un événement qui n'a pas de data
- **Axe** : A, C
- **Localisation** : EXIG-EVT-02 (p. 76) « porter … time, datacontenttype et dataschema »; EXIG-EVT-05 (p. 78) « l'événement ne transmet qu'une référence (dataref), sans data ».
- **Diagnostic** : dans CloudEvents, datacontenttype et dataschema décrivent `data`. L'événement « sans data » que prescrit l'EXIG-EVT-05 doit pourtant les porter, sans aucune sémantique. En mode binaire Kafka, datacontenttype devient de plus l'en-tête content-type qui sert à détecter le mode (p. 76). Par ailleurs, l'EXIG-EVT-02 vise aussi tout événement « consommé » par un agent, y compris ceux d'un ERP existant que l'entreprise ne contrôle pas, ce qui suppose des adaptateurs que le texte ne prévoit pas.
- **Correctif proposé** : « datacontenttype et dataschema DOIVENT être présents dès que data l'est; pour un événement par référence, dataschema décrit la ressource visée par dataref ». Prévoir un adaptateur de mise en conformité pour les producteurs non agentiques.
- **Confiance** : vérifié dans le texte; sémantique CloudEvents d'après mes connaissances.

### [08-13] [MINEUR] Le préfixe de type ne correspond pas au domaine de l'entreprise
- **Axe** : C
- **Localisation** : EXIG-EVT-02 (p. 76) « par exemple ca.entreprise.logistique.alerte.rupture.v1 ».
- **Diagnostic** : l'exemple de l'annexe C.4 emploie `source: https://agents.ent.ca/...` et `catalogue.ent.ca`. Le domaine inversé de ent.ca est `ca.ent`, pas `ca.entreprise`, alors que la règle exige un nom « en domaine inversé ».
- **Correctif proposé** : unifier le domaine fictif (`ca.ent.…` ou `entreprise.ca`).
- **Confiance** : vérifié dans le texte (p. 76, 219-220).

### [08-14] [MAJEUR] « Événement d'agent » est indécidable pour le consommateur
- **Axe** : A
- **Localisation** : EXIG-EVT-04 (p. 78) « Un consommateur DOIT refuser un événement d'agent qui en est dépourvu ».
- **Diagnostic** : le seul marqueur d'un événement d'agent, xagentorigin, fait partie des attributs dont l'absence doit déclencher le refus. Un événement d'agent privé de tous ses attributs ressemble à un événement de système non agentique et passe. La règle ne se déclenche que si l'événement est en partie conforme.
- **Contre-exemple** : un agent mal configuré publie sans aucune extension; le consommateur le traite comme un événement de l'ERP et ne le dirige pas vers les lettres mortes.
- **Correctif proposé** : déterminer la nature « agent » par l'identité authentifiée du producteur auprès du courtier (EXIG-EVT-07, liste des producteurs au catalogue), et faire rejeter par le courtier, à la publication, l'événement d'un producteur agent qui ne porte pas les attributs.
- **Confiance** : vérifié dans le texte.

### [08-15] [MAJEUR] La recopie de traceparent contredit les conventions OpenTelemetry citées et l'EXIG-OBS-02
- **Axe** : A, C
- **Localisation** : EXIG-EVT-04 (p. 78) « un agent qui publie un nouvel événement en réaction y DOIT recopier le traceparent de l'événement reçu »; p. 77 : les conventions de messagerie « recommandent que le producteur injecte le contexte de création dans le message ».
- **Diagnostic** : l'agent qui republie est un nouveau producteur. Selon OpenTelemetry, il injecte son propre contexte (même trace, span parent = son span de création). En recopiant le traceparent reçu, le cadre fait pointer chaque événement de la chaîne vers le span du premier émetteur, et l'arbre causal (quel agent a produit quel événement) disparaît de la trace. Par ailleurs, l'EXIG-OBS-02 impose de remplacer un contexte invalide ou venu de l'extérieur, alors que l'EXIG-EVT-04 interdit à tout intermédiaire de modifier traceparent et exige de recopier celui de l'événement reçu, même s'il provient d'un partenaire.
- **Contre-exemple** : avec trois republications, les quatre événements portent le même span parent, et l'enquête ne sait plus si Approvisionnement réagissait à Planification ou au Détecteur.
- **Correctif proposé** : « conserver l'identifiant de trace et remplacer le span parent par celui du span de publication de l'agent; relier le span de traitement à l'événement reçu par un lien de span »; aligner l'EXIG-EVT-04 sur l'EXIG-OBS-02 pour les événements d'origine externe.
- **Confiance** : déduit (lecture des conventions telles que le cadre les rapporte p. 77, et de l'EXIG-OBS-02, p. 146).

### [08-16] [MAJEUR] Le compteur de sauts ne coupe pas la boucle prise en exemple
- **Axe** : A, B
- **Localisation** : p. 78 « la planification révise une prévision, l'approvisionnement ajuste une commande, ce qui déclenche une nouvelle révision »; EXIG-EVT-06 (p. 79) « (un composant qui n'applique pas la règle, ou qui n'est pas un agent, rompt la chaîne causale) ».
- **Diagnostic** : « ajuster une commande » est une écriture dans l'ERP (p. 75, « réaction aux changements d'état d'un ERP »). L'ERP publie alors son propre événement, sans compteur, et l'agent suivant se croit « premier agent » et repart à 1. La boucle-type du texte traverse donc justement le composant qui rompt la chaîne : la règle reste vraie sur le papier, mais ne protège pas du cas qui la motive. De même, un agent qui publie plus tard, à partir de sa mémoire, ou sur un autre sujet, peut remettre le compteur à 1. Enfin, rien ne dit que le compteur est géré par du code déterministe (SDK ou intercepteur du courtier) plutôt que par l'agent, alors que le texte promet une coupure « sans dépendre du jugement d'un modèle ».
- **Contre-exemple** : Planification → événement (1) → Approvisionnement modifie la commande dans l'ERP → `erp.commande.modifiee` (sans compteur) → Planification (1) → … sans fin.
- **Correctif proposé** : propager le compteur et xagentorigin par la boîte d'envoi (outbox) des systèmes adaptés; ajouter un second coupe-boucle, indépendant des attributs (débit par entité et par identifiant de trace, budget de coût par chaîne, EXIG-FIN); faire gérer le compteur par l'intercepteur de publication de la plateforme.
- **Confiance** : vérifié dans le texte (limite reconnue, portée non tirée); déduit (scénario).

### [08-17] [MAJEUR] Le compteur borne la profondeur, pas la largeur
- **Axe** : B
- **Localisation** : EXIG-EVT-06 (p. 79) « borne la longueur de toute chaîne d'événements »; figure 10 « → lettres mortes + alerte ».
- **Diagnostic** : avec un plafond de 4 et k abonnés qui republient chacun, une chaîne produit jusqu'à 1 + k + k² + k³ événements, chacun consommant des jetons et pouvant produire des effets, et k³ événements atteignent les lettres mortes, chacun avec son alerte. La tempête est bornée, mais de façon exponentielle, et elle se double d'une tempête d'alertes. Le titre « Prévention des tempêtes » promet plus que la règle.
- **Contre-exemple** : k = 10 donne 1 111 événements et 1 000 alertes pour une seule alerte de rupture de stock.
- **Correctif proposé** : plafonner aussi le nombre d'événements par identifiant de trace ou par xagentorigin dans une fenêtre de temps (au courtier ou à la passerelle); regrouper les alertes de lettres mortes par chaîne.
- **Confiance** : déduit (arithmétique).

### [08-18] [MINEUR] Sémantique du plafond : décalage d'un cran dans la figure 10, cas d'agrégation non défini
- **Axe** : A, C
- **Localisation** : figure 10 (p. 79) « Approvisionnement consomme, republie saut 3/4 … Agent N reçoit saut 4/4 »; tableau 20 (p. 77-78) « l'événement dont le compteur atteint ce plafond n'est pas traité »; EXIG-EVT-06 « xagentorigin à son identifiant ».
- **Diagnostic** : (a) Si Approvisionnement publie le saut 3, l'agent N reçoit 3, ce qui est inférieur à 4 : il traite. Pour qu'il « reçoive 4/4 », il faut une publication de plus, absente de la figure. (b) Avec la règle « ≥ », la 4ᵉ publication est produite puis jamais traitée : un « plafond de 4 sauts » autorise en fait 3 traitements, et le contrôle au consommateur gaspille une publication que le producteur aurait pu refuser. (c) Un agent qui publie en réaction à plusieurs événements (agrégation) n'a aucune règle de compteur (max + 1?) ni d'origine. (d) L'EXIG-EVT-06 omet la version, que le tableau 20 exige dans xagentorigin.
- **Correctif proposé** : corriger la figure; définir « au plus N publications traitées »; faire vérifier le compteur aussi par le producteur; « compteur = max des compteurs reçus + 1 » pour l'agrégation; « identifiant et version ».
- **Confiance** : vérifié dans le texte.

### [08-19] [MAJEUR] Le plafond recopié depuis le premier événement ignore le plafond de chaque sujet
- **Axe** : A, C
- **Localisation** : EXIG-EVT-06 (p. 79) « recopier les deux autres valeurs sans les modifier »; tableau 22 (p. 81), sujet d'événement : « plafond de sauts » à l'entrée de catalogue; tableau 20 : « plafond de sauts fixé au contrat du flux ».
- **Diagnostic** : une chaîne traverse plusieurs sujets, dont chacun a son propre plafond au catalogue (tableau 22). Comme la valeur du premier sujet est recopiée, le plafond d'un sujet aval plus strict n'est jamais appliqué, ce qui contredit la règle « la plus stricte » du cadre. Le lieu du plafond flotte aussi entre le « contrat du flux » (AsyncAPI, tableau 20 et EXIG-EVT-06) et l'« entrée de catalogue » (tableau 22, que l'EXIG-EVT-03 présente comme distincte du contrat), et « flux » n'est défini ni comme sujet ni comme chaîne.
- **Contre-exemple** : le sujet A (plafond 4) alimente le sujet B (plafond 2, car ses effets sont P2). Un événement à 3 sur B est traité, puisque 3 < 4.
- **Correctif proposé** : à chaque publication, xagentmaxhops = min(valeur reçue, plafond du sujet cible); loger le plafond à un seul endroit; définir « flux ».
- **Confiance** : vérifié dans le texte.

### [08-20] [BLOQUANT] Le bus d'événements contourne la passerelle, l'intersection des droits et la limite de délégation
- **Axe** : A, B
- **Localisation** : EXIG-EVT-07 (p. 79) « Une décision d'autorisation NE DOIT PAS se fonder sur authtype, authid »; EXIG-EVT-01 (p. 76); sommaire, décision 2 : « Rien ne contourne la passerelle ni le catalogue … tout appel d'un agent vers … un agent d'un autre domaine traverse la passerelle ».
- **Diagnostic** : à juste titre, l'EXIG-EVT-07 fait de l'initiateur une donnée informative. Mais le consommateur agit alors sous sa propre identité : pour toute chorégraphie (patron autorisé, que l'EXIG-EVT-01 recommande pour l'asynchrone), l'intersection mandant ∩ agent du PRIN-03 disparaît. La limite de délégation à deux niveaux (EXIG-ORC-04, vérifiée par l'imbrication `act` à l'échange de jetons) ne s'applique pas non plus, puisque l'événement ne porte aucun jeton. Rien dans le chunk, ni ailleurs d'après une recherche dans le texte complet, ne fait passer le courtier par la passerelle. Le bus offre donc une voie sanctionnée pour joindre un agent d'un autre domaine sans passer par la passerelle, contre la décision 2. On a là un adjoint confus (confused deputy) par construction.
- **Contre-exemple** : un utilisateur sans droit d'écriture sur les commandes demande à un agent de publier « révision de prévision ». L'agent Approvisionnement, qui a des droits d'écriture propres, modifie la commande. Le journal indique un authid informatif; aucun contrôle n'a croisé les droits de l'utilisateur.
- **Correctif proposé** : (a) un événement qui peut déclencher un effet P2 ou P3 au nom d'une personne DOIT référencer une délégation vérifiable (jeton ou attestation signée par le serveur d'autorisation, échangée par le consommateur à la RFC 8693), sinon le consommateur agit seulement dans les limites d'un mandat de service inscrit au catalogue pour ce sujet; (b) compter les sauts d'événements dans la profondeur de délégation, ou justifier l'écart; (c) dire explicitement si le courtier est un point d'application de politique équivalent à la passerelle, et corriger la décision 2 en conséquence.
- **Confiance** : vérifié dans le texte (p. 79, sommaire, EXIG-ORC-04); recherche dans full.txt sans lien courtier-passerelle.

### [08-21] [MINEUR] La clé de partition « sans renseignement personnel » contredit l'EXIG-EVT-05
- **Axe** : C
- **Localisation** : EXIG-EVT-09 (p. 80) « (dossier, commande, session), la clé de partition DOIT être l'identifiant technique de cette entité, sans renseignement personnel »; EXIG-EVT-05 : un pseudonyme « demeure un renseignement personnel ».
- **Diagnostic** : l'identifiant d'un dossier de crédit ou d'une session rattachée à une personne est un pseudonyme, donc un RP selon l'EXIG-EVT-05 elle-même. L'exigence est impossible à satisfaire pour deux des trois exemples. La clé Kafka est en outre répliquée, journalisée et conservée un an (EXIG-EVT-10).
- **Correctif proposé** : « sans RP direct; un identifiant pseudonyme est admis et traité comme un RP (conservation, accès) ».
- **Confiance** : vérifié dans le texte.

### [08-22] [MINEUR] Ordre : des conditions sont omises, et l'exigence est propre à un produit
- **Axe** : B, C
- **Localisation** : EXIG-EVT-09 (p. 80-81); p. 79 « un autre courtier se juge sur les mêmes questions ».
- **Diagnostic** : l'ordre par clé est aussi rompu par l'ajout de partitions (le hachage de la clé change de partition), par le traitement concurrent dans un consommateur (appels de modèle en parallèle), par les sujets de réessai et les lettres mortes, et par un relais de boîte d'envoi à plusieurs instances. Aucune de ces conditions n'est traitée. Le DOIT impose en outre un mécanisme de la liaison Kafka (« Key Mapper »), sans équivalent pour un autre courtier.
- **Correctif proposé** : ajouter « nombre de partitions figé pendant la vie du sujet, traitement séquentiel par clé, relais ordonné »; formuler le DOIT de façon indépendante du courtier (« la clé native du courtier DOIT égaler partitionkey »).
- **Confiance** : déduit (fonctionnement de Kafka).

### [08-23] [MINEUR] Le producteur idempotent ne couvre pas tous les doublons nés des reprises
- **Axe** : A
- **Localisation** : tableau 21 (p. 79) « le producteur idempotent (depuis 0.11.0.0) évite les doublons dans le journal lors des reprises ».
- **Diagnostic** : la déduplication repose sur l'identifiant de producteur et le numéro de séquence par partition, valables pour une session de producteur. Le redémarrage du producteur ou du relais de la boîte d'envoi crée un nouvel identifiant, et un renvoi produit alors un doublon (sauf `transactional.id`). L'énoncé surestime la garantie, et c'est justement le cas de la boîte d'envoi.
- **Correctif proposé** : « évite les doublons dus aux réessais internes d'une même session de producteur ».
- **Confiance** : connaissance de KIP-98 (sûr pour l'essentiel); à confirmer par [140] ou [256].

### [08-24] [MAJEUR] Pour un consommateur d'événements, la règle de dérivation de la clé d'idempotence produit des doubles effets
- **Axe** : A
- **Localisation** : EXIG-EVT-08 (p. 80) « transmet au système cible une clé d'idempotence que ce dernier vérifie (section 7.6) »; EXIG-ORC-21 (p. 98) « dérivée de l'identifiant de la tâche et de celui de l'étape ».
- **Diagnostic** : lorsqu'un événement est relivré après la panne d'un consommateur (effet produit, déduplication non encore inscrite), le consommateur ouvre une nouvelle tâche, donc un nouvel identifiant de tâche et une nouvelle clé, et le système cible accepte le doublon. La déduplication sur (source, id) ne protège pas, parce que l'effet et l'inscription de déduplication ne sont pas atomiques. Aucune fenêtre de conservation de la déduplication n'est fixée non plus, alors que les sujets conservent jusqu'à un an.
- **Contre-exemple** : paiement émis, plantage avant la validation du décalage, relivraison, nouvelle tâche, nouvelle clé, second paiement : le scénario même que l'EXIG-EVT-08 prétend exclure.
- **Correctif proposé** : pour un traitement déclenché par un événement, « clé = H(source, id, étape) »; conserver l'état de déduplication au moins aussi longtemps que la rétention du sujet.
- **Confiance** : déduit (combinaison des p. 80 et 98).

### [08-25] [MINEUR] EXIG-EVT-10 : « tout rejeu », sujet partagé, renvoi au ch. 10, effacement
- **Axe** : B, C
- **Localisation** : EXIG-EVT-10 (p. 81) « Tout rejeu DOIT s'exécuter dans un environnement isolé »; « sans excéder la rétention des traces et journaux d'audit fixée au chapitre 10 ».
- **Diagnostic** : (a) La reprise d'un groupe de consommateurs depuis un décalage antérieur (après une panne ou un correctif) est un rejeu en production que la lettre de la règle interdit; « rejeu » doit être défini. (b) Un sujet qui alimente plusieurs agents, à fenêtres d'enquête différentes, n'a pas de règle (le maximum, présumément). (c) Le ch. 10 ne fixe que la conservation du journal d'audit (24 mois, EXIG-OBS-13). Celle des traces relève de la fiche (EXIG-CON-10, ch. 12), et le renvoi est donc partiellement faux. (d) Un journal Kafka immuable ne permet pas de détruire un RP avant l'échéance du sujet (art. 23 de la Loi sur le privé), et ni l'effacement par destruction de clé (crypto-shredding) ni le compactage ne sont prévus.
- **Correctif proposé** : définir « rejeu d'audit ou d'évaluation »; prendre la fenêtre maximale des agents abonnés; corriger le renvoi (EXIG-OBS-13, EXIG-CON-10); prévoir le chiffrement par sujet ou par personne, avec destruction de la clé.
- **Confiance** : vérifié dans le texte (p. 81, 146-147, 172-178).

### [08-26] [MINEUR] Le tableau 22 est en retrait sur l'EXIG-EVT-03 et ne lui sert donc pas de minimum fiable
- **Axe** : C
- **Localisation** : tableau 22 (p. 81), sujet d'événement : « Producteurs et consommateurs autorisés; classification; plafond de sauts »; EXIG-EVT-03 (p. 76) : l'entrée précise « le propriétaire, la classification et les producteurs et consommateurs autorisés »; EXIG-INT-12 : le tableau 22 est le minimum bloquant.
- **Diagnostic** : le propriétaire, exigé par l'EXIG-EVT-03, manque au tableau 22, comme pour les ressources, les invites, les agents et les API. Un sujet sans propriétaire satisfait donc le contrôle bloquant de l'EXIG-INT-12. La clé de partition, que l'EXIG-EVT-03 met dans le contrat, n'y figure pas non plus.
- **Correctif proposé** : ajouter « propriétaire et équipe de garde » à chaque ligne, et « clé de partition » à la ligne des sujets.
- **Confiance** : vérifié dans le texte.

### [08-27] [MAJEUR] Aucun mécanisme ne permet la coexistence de 60 jours pour un outil MCP ou une carte A2A
- **Axe** : A, B
- **Localisation** : EXIG-INT-14 (p. 82) « la version majeure précédente DOIT rester disponible au moins 60 jours »; p. 82 « la définition d'un outil MCP ne comporte aucun champ de version ».
- **Diagnostic** : un serveur MCP expose une seule définition par nom d'outil, et une carte A2A se publie à une URI bien connue unique avec un seul champ version. Faire coexister deux versions majeures exige un nom suffixé (lui-même un changement majeur selon le § 6.8, « élément renommé »), un second serveur ou un second point de terminaison. Le cadre ne choisit pas, alors qu'il le fait pour les événements (« un nouveau type versionné », EXIG-EVT-03) et pour A2A 0.3/1.0 (double interface, EXIG-A2A-15). L'exigence est donc inapplicable telle quelle pour deux des cinq types d'interfaces du tableau 22.
- **Correctif proposé** : convention imposée (p. ex. `domaine.outil_v2` pour MCP, une entrée `supportedInterfaces` par version majeure pour A2A) et routage par la passerelle selon la dépendance épinglée (EXIG-INT-15).
- **Confiance** : vérifié dans le texte; déduit (contraintes MCP et A2A).

### [08-28] [MINEUR] SemVer : « toute reformulation » mineure, sens du correctif face à l'épinglage
- **Axe** : A
- **Localisation** : p. 82 « mineur : ajout compatible et toute reformulation d'une description »; « correctif : correction qui ne change ni la définition publiée »; « Il dépend d'une version identifiée par son numéro et par son empreinte ».
- **Diagnostic** : (a) Pour un outil MCP, la description est une instruction au modèle. Une reformulation peut changer le sens, ce qui est majeur selon la puce précédente : « toute » crée un conflit que seule l'EXIG-INT-13 tranche, par renvoi. (b) Un correctif laisse l'empreinte inchangée : si l'épinglage exige l'égalité du numéro, chaque correctif oblige à réapprouver tous les consommateurs sans changement de définition; s'il ne vérifie que l'empreinte, le numéro épinglé ne sert à rien. La règle n'est pas fixée.
- **Correctif proposé** : « reformulation sans changement de sens »; « l'épinglage porte sur MAJEUR.MINEUR et sur l'empreinte; le correctif est libre ».
- **Confiance** : vérifié dans le texte.

### [08-29] [MINEUR] L'empreinte des sujets et des contrats AsyncAPI n'est vérifiée à l'exécution par personne
- **Axe** : B
- **Localisation** : p. 82 « la passerelle vérifie l'empreinte à l'exécution (EXIG-MCP-20, EXIG-SEC-18) »; EXIG-INT-15 « pour chaque … sujet d'événement, la version épinglée et l'empreinte approuvée ».
- **Diagnostic** : l'EXIG-MCP-20 ne vise que les définitions d'outils. Les événements passent par le courtier, pas par la passerelle (voir 08-20), et rien ne vérifie que le dataschema reçu correspond à l'empreinte épinglée. Un contrat AsyncAPI, souvent écrit en YAML, doit aussi être converti en JSON avant la canonisation RFC 8785, une étape que le cadre ne précise pas.
- **Correctif proposé** : faire vérifier par le consommateur (registre de schémas) que le `dataschema` reçu figure parmi ceux qu'il a épinglés; définir la forme canonique (JSON issu du YAML) d'un contrat AsyncAPI.
- **Confiance** : déduit.

### [08-30] [MINEUR] Format d'appel de références incohérent
- **Axe** : C
- **Localisation** : p. 77 « Distributed Tracing, Partitioning, Sampling et Sequence[251][187] ».
- **Diagnostic** : partout ailleurs, la forme groupée est « [29, 68] ».
- **Correctif proposé** : « [187, 251] ».
- **Confiance** : vérifié dans le texte.

### [08-31] [MINEUR] La file de lettres mortes reçoit des données que le consommateur n'avait pas le droit de traiter
- **Axe** : B
- **Localisation** : EXIG-EVT-04 (p. 78) « rejeter l'événement dont il ne peut respecter les exigences … et le diriger vers la file de lettres mortes ».
- **Diagnostic** : une file de lettres mortes commune reçoit des événements de classification arbitraire, y compris celle que le consommateur ne savait pas protéger. Ses lecteurs (exploitation) accèdent alors à des données `restricted`, et aucune classification ni aucun contrôle d'accès ne sont exigés pour cette file.
- **Correctif proposé** : file de lettres mortes par sujet, héritant de la classification maximale du sujet et de ses listes de contrôle d'accès; inscription au catalogue.
- **Confiance** : déduit.

### [08-32] [MINEUR] « Key Mapper » à activer explicitement : fait externe douteux
- **Axe** : A
- **Localisation** : p. 76 « un « Key Mapper » facultatif, à activer explicitement »; EXIG-EVT-09 (p. 81) « car la liaison reprend par défaut la clé fournie par l'utilisateur[250] ».
- **Diagnostic** : de mémoire, la liaison Kafka 1.0.2 dit que chaque implémentation « SHOULD provide a default Key Mapper » qui recopie partitionkey dans la clé. Si c'est exact, « à activer explicitement » et « par défaut la clé fournie par l'utilisateur » déforment la source (comportement d'un SDK précis présenté comme comportement de la liaison).
- **Correctif proposé** : citer le passage exact de [250] et distinguer la liaison du comportement des SDK.
- **Confiance** : à vérifier (source externe : § 3.1 « Key Mapping » de kafka-protocol-binding.md, balise ce@v1.0.2).

## Points forts
Les faits normatifs sont soigneusement séparés des choix du cadre (en-tête absent ou vide, « au moins une fois », préfixe x, pseudonyme toujours tenu pour un RP).
Le refus de promettre la reproduction des décisions au rejeu, et celui de s'appuyer sur la sémantique « exactement une fois » de Kafka pour un effet externe, sont justes et rares dans ce genre de cadre.
La figure 9 rend concrète la combinaison A2A, MCP et approbation signée, avec un refus explicite du « oui » conversationnel.

## Questions pour l'audit bibliographique
- p. 71 : A2A 1.0, nom exact et sémantique de `returnImmediately`; UnsupportedOperationError pour un message envoyé à une tâche terminale; ListTasks qui omet les artefacts par défaut [68].
- p. 71 : en A2A 1.0, un message A2A ou SendMessageRequest a-t-il un champ désignant l'AgentSkill (décisif pour 08-03)? Le flux SSE se ferme-t-il à l'entrée d'un état interrompu [68]?
- p. 71-72 : en-tête vide ⇒ 0.3; paramètre de requête équivalent; TLS 1.3 « recommandé »; liste SSRF et délai de 10 à 30 s pour les notifications push [68, 161].
- p. 72 : A2A 1.0 ajoute-t-il un flux Device Code et un indicateur PKCE [30, 240]?
- p. 73 : existence et statut du dépôt `open-telemetry/semantic-conventions-genai` et de sa convention A2A (Development, non étiquetée) [241].
- p. 75 : SDK JavaScript en disponibilité générale le 22 juillet 2026 [242]; niveaux MUST/SHOULD/MAY d'a2a-tck [243]; interface en ligne de commande présentée le 1er octobre 2026, versions dès le 9 septembre [244, 245].
- p. 75-76 : qualité de Kai Waehner, « conseiller indépendant » (anciennement Field CTO chez Confluent?) [167, 246].
- p. 76 : CloudEvents 1.0.2 (février 2022) et statut Graduated de la CNCF le 25 janvier 2024 [173, 247, 248]; AsyncAPI 3.1.0 publiée le 31 janvier 2026 [249].
- p. 76, 81 : comportement par défaut du « Key Mapper » dans la liaison Kafka 1.0.2 [250] (08-32).
- p. 77 : Auth Context, Data Classification et Expiry Time absentes de la 1.0.2 [251]; valeurs et définitions d'authtype (notamment `user`, `system`) [252]; obligation de rejet et d'intégrité par les intermédiaires dans Data Classification [255]; règle multi-sauts de Distributed Tracing [253].
- p. 77 : conventions OpenTelemetry de messagerie, liens par défaut et parenté admise pour un message unique [254].
- p. 79-80 : ordre limité au lot pour les files coopératives (KIP-932) [258]; Kafka 4.0 du 18 mars 2025, sens de « généralise » le protocole de rééquilibrage (KIP-848 : disponibilité générale ou valeur par défaut côté client?) [259]; files coopératives prêtes pour la production en 4.2.0 (17 février 2026) et files de lettres mortes en 4.4.0 (22 octobre 2026) [260, 261]; propos de Confluent sur le rejeu déterministe [262].
- p. 81 : sens de [238] (une nouvelle URI pour tout changement incompatible d'une extension A2A); OWASP sur l'épinglage par empreinte et le nouveau consentement [221].

audit_08.md : 32 constats (1 BLOQUANT, 13 MAJEUR, 18 MINEUR)
