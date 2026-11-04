# Audit chunk_09 — pages 81-92

## Synthèse
Le chunk couvre la fin du § 6.8 (SemVer, épinglage, catalogue, tests de compatibilité), le § 6.9 (AAIF, AGNTCY, paiements, signaux de veille) et les § 7.1-7.3 (données probantes, huit patrons, arbre de décision). Il est dense et bien sourcé, mais ses mécanismes de versionnage tiennent mal ensemble une fois combinés avec l'épinglage exact et les serveurs de tiers. Les trois défauts les plus graves : (1) l'EXIG-INT-18 interdit le retrait anticipé que l'EXIG-INT-14 autorise pour un motif de sécurité; (2) l'EXIG-ORC-04 fait vérifier par la passerelle la profondeur des `act` imbriqués, ce que le § 9.3 du cadre lui-même, citant la RFC 8693, interdit comme base d'une décision d'accès; (3) l'arbre de la figure 12 envoie tout déclenchement par événement vers la chorégraphie, le patron le moins prévisible, à l'encontre de la règle « le plus simple d'abord ».

## Constats

### [09-01] [BLOQUANT] Retrait anticipé pour motif de sécurité : l'EXIG-INT-14 l'autorise, l'EXIG-INT-18 l'interdit
- **Axe** : C (et A)
- **Localisation** : § 6.8, EXIG-INT-14 (p. 82) : « Seul un motif de sécurité, sur décision du comité, justifie un retrait anticipé »; EXIG-INT-18 (p. 83) : « Une version n'est retirée qu'à l'échéance annoncée, jamais avant la fin de la coexistence de l'EXIG-INT-14 ».
- **Diagnostic** : l'EXIG-INT-18 est absolue (« jamais ») et ne reprend pas l'exception de l'EXIG-INT-14. Les deux DOIT se contredisent. Dans le cas le plus important, une version vulnérable, l'exigence la plus stricte (INT-18) l'emporte selon la règle de préséance du cadre, et la version doit alors rester servie. L'EXIG-GOV-14 (p. 168) ajoute une troisième formulation, « précédé d'une suspension (EXIG-INT-14) », alors que l'EXIG-INT-14 ne parle pas de suspension.
- **Contre-exemple** : une version 2.x d'un outil P2 se révèle exploitable (empoisonnement de description) 10 jours après la publication de 3.0. Le comité décide le retrait, mais l'EXIG-INT-18 l'interdit avant le jour 60, et la passerelle doit continuer de servir 2.x (EXIG-INT-17 : « dépréciées non échues »).
- **Correctif proposé** : dans l'EXIG-INT-18, ajouter « sauf retrait anticipé pour motif de sécurité (EXIG-INT-14) ». Dans l'EXIG-INT-14, introduire l'état « suspendue » (retrait immédiat de la passerelle, puis retrait définitif) que l'EXIG-GOV-14 présuppose, et l'ajouter aux quatre états du catalogue (p. 83).
- **Confiance** : vérifié dans le texte.

### [09-02] [BLOQUANT] L'EXIG-ORC-04 fait fonder un rejet par la passerelle sur les acteurs antérieurs, contrairement au § 9.3 et à la RFC 8693
- **Axe** : A
- **Localisation** : § 7.2, EXIG-ORC-04 (p. 90) : « la passerelle d'agents DOIVENT vérifier la profondeur par l'imbrication de la réclamation act du jeton délégué et rejeter toute délégation excédentaire ».
- **Diagnostic** : le § 9.3 (p. 124) dit « la RFC 8693 interdit de fonder une décision d'accès sur les acteurs antérieurs », et l'EXIG-IAM-11 (p. 125) dit que le consommateur « fonde sa décision sur sub et sur l'acteur courant seulement ». Les `act` imbriqués sont « informational only » (RFC 8693 § 4.1, d'après mes connaissances). Rejeter un jeton selon la profondeur de son imbrication, c'est précisément une décision d'accès fondée sur les acteurs antérieurs. Le contrôle conforme est celui que fait le serveur d'autorisation au moment de l'échange (EXIG-IAM-08). Trois cas de contournement s'y ajoutent : (a) l'EXIG-IAM-08 ne s'applique que « lorsqu'un agent agit pour une personne », donc une chaîne d'agents ambiants ne produit pas d'`act` imbriqué; (b) le patron 5 admet un « appel interne » (tableau 24), sans échange de jetons; (c) on ne sait pas si un transfert du patron 3, où le routeur « se retire », compte comme un niveau.
- **Contre-exemple** : routeur → spécialiste (transfert par échange de jetons) → exécutant. On a trois `act` imbriqués, la chaîne est rejetée, alors que le routeur s'est retiré. À l'inverse, un exécutant ambiant qui appelle un troisième agent avec son propre jeton de service franchit la limite sans aucune imbrication. Dans un cas comme dans l'autre, la règle ne tient pas.
- **Correctif proposé** : confier la vérification de profondeur au seul serveur d'autorisation. Pour les chaînes sans mandant humain, exiger aussi l'échange de jetons, avec l'agent initiateur comme `sub`. Préciser que le transfert remplace l'acteur et n'ajoute pas de niveau. Interdire la délégation par appel interne au-delà d'un niveau, ou la tracer par un attribut de profondeur signé. Au passage, aligner le « Pourquoi » de l'EXIG-APP-08 (p. 191), qui fait appliquer l'intersection par la passerelle à partir de la chaîne `act`, contrairement au § 9.3.
- **Confiance** : contradiction interne vérifiée dans le texte; la lecture de la RFC 8693 § 4.1 est déduite de mes connaissances, à confirmer par l'audit bibliographique.

### [09-03] [MAJEUR] L'épinglage exact rend inopérant le versionnage mineur et correctif
- **Axe** : A
- **Localisation** : EXIG-INT-15 (p. 82-83) : « NE DOIT PAS désigner une version flottante (« dernière », plage de versions) »; EXIG-INT-14 : « la version majeure précédente DOIT rester disponible au moins 60 jours »; EXIG-INT-19 : « la version active précédente ».
- **Diagnostic** : chaque consommateur épingle une version exacte et son empreinte. Or la coexistence n'est garantie que pour la majeure précédente, et l'EXIG-INT-19 suppose une seule version active à la fois. Rien ne dit ce qu'il advient d'une version 1.2.3 quand 1.3.0 (reformulation de description, donc mineure) est activée. Un serveur MCP ne sert qu'une définition à la fois, et l'EXIG-MCP-20 suspend tout outil dont l'empreinte diffère de l'épinglage. Chaque version mineure casse donc tous les consommateurs, sans préavis. Le « Pourquoi » de l'EXIG-INT-13 (« dit au consommateur s'il peut migrer sans risque ») perd son objet.
- **Contre-exemple** : un fournisseur corrige une faute dans une description, publiée en 1.3.0. Les 40 agents épinglés sur 1.2.3 voient l'outil retiré de leur `tools/list` jusqu'à ce que 40 fiches soient modifiées, revues et tracées.
- **Correctif proposé** : définir le sort des versions mineures et correctives : coexistence, ou migration des épinglages en lot par le propriétaire du contrat, avec un avis. Ou bien permettre d'épingler une empreinte par version mineure tout en autorisant la passerelle à servir plusieurs versions actives. Dire explicitement si plusieurs versions mineures peuvent être « actives ».
- **Confiance** : déduit de la combinaison INT-14, INT-15, INT-19 et MCP-20 (textes vérifiés).

### [09-04] [MAJEUR] Coexistence, approbation préalable et tests avant activation ne s'appliquent pas aux serveurs de tiers
- **Axe** : B
- **Localisation** : EXIG-INT-16 (p. 83) : « avant d'être servie aux agents, y compris pour les serveurs et agents de tiers »; EXIG-INT-14; EXIG-INT-19 : « La chaîne d'intégration DOIT ».
- **Diagnostic** : l'entreprise ne contrôle ni le calendrier de publication d'un serveur distant de tiers, ni le maintien de son ancienne version, ni sa chaîne d'intégration. Pour un tiers, les EXIG-INT-14 et INT-19 sont donc inapplicables. Quant à l'EXIG-INT-16, elle ne peut se réaliser que par une suspension (EXIG-MCP-20, SEC-18) : toute modification d'un tiers coupe le service en mode fermé. Le compromis disponibilité contre sécurité n'est ni nommé ni outillé (environnement de préproduction du fournisseur, préavis contractuel de changement de définition, mise en cache de l'ancienne version).
- **Contre-exemple** : un fournisseur SaaS ajoute un paramètre optionnel un vendredi soir. Tous les agents qui dépendent de l'outil perdent la capacité jusqu'à la revue de l'EXIG-INT-16. La coexistence de 60 jours, que l'EXIG-INT-14 rend obligatoire, ne peut pas être respectée.
- **Correctif proposé** : prévoir un régime distinct pour les tiers : clause contractuelle de préavis et de point d'accès de préversion (à relier aux clauses du ch. 13), version tenue au catalogue par l'entreprise, test différentiel à l'entrée du catalogue à la place de la chaîne d'intégration, et procédure accélérée de revue avec un délai cible.
- **Confiance** : déduit.

### [09-05] [MAJEUR] L'empreinte garantit la définition, non le comportement : la promesse de l'épinglage est surévaluée
- **Axe** : A
- **Localisation** : p. 82 : « l'empreinte prouve ce que l'agent reçoit »; « Pourquoi » de l'EXIG-INT-15 (p. 83) : « sans épinglage, un fournisseur peut changer le comportement d'un agent à l'insu de son propriétaire ».
- **Diagnostic** : l'empreinte porte sur la définition canonisée (RFC 8785), pas sur l'implémentation du serveur. Le niveau « correctif » est d'ailleurs défini comme une correction qui ne change pas la définition, donc ni l'empreinte. Un fournisseur malveillant ou compromis peut changer le comportement d'un outil sans toucher à sa définition, et l'épinglage ne le voit pas. Le « Pourquoi » de l'EXIG-INT-15, et celui de l'EXIG-SEC-18 (« neutralise la substitution après approbation »), laissent croire le contraire. Le rug pull « par l'implémentation » n'est pas couvert.
- **Contre-exemple** : la définition de `crm_update_contact` reste identique, mais le serveur se met à copier chaque appel vers un tiers. L'empreinte reste valide.
- **Correctif proposé** : écrire « l'empreinte prouve la définition reçue » et renvoyer, pour le comportement, à la signature des artefacts déployés, à la provenance (§ 9.8) et au contrôle des sorties réseau.
- **Confiance** : vérifié dans le texte (portée de l'empreinte); le scénario est déduit.

### [09-06] [MINEUR] Trois énumérations différentes de la « définition publiée »
- **Axe** : C
- **Localisation** : EXIG-INT-13 (p. 82) : « (nom, description, schémas, annotations, compétences) »; EXIG-MCP-20 (p. 63) : « nom, titre, description, icônes, schémas d'entrée et de sortie, annotations et _meta ».
- **Diagnostic** : un changement de titre, d'icône ou de `_meta` modifie l'empreinte (MCP-20), ce qui suspend l'outil et exige une nouvelle approbation (INT-16). L'EXIG-INT-13 ne l'oblige pourtant pas à une version mineure, et la définition de « correctif » devient ambiguë. Pour une carte A2A, rien ne dit si l'empreinte exclut le champ `signatures`, comme le fait la signature JWS (p. 142). Une rotation de clé changerait alors l'empreinte. L'EXIG-INT-19 ne bloque, enfin, que l'incompatibilité sans version majeure, et non un changement d'empreinte publié comme correctif.
- **Contre-exemple** : un fournisseur publie en correctif 1.2.4 un `_meta` modifié. L'outil est suspendu à la passerelle, alors que rien dans l'EXIG-INT-19 n'a bloqué la publication.
- **Correctif proposé** : définir une seule fois le périmètre canonisé, par type d'interface (avec `signatures` exclu pour les cartes), le citer dans INT-13, INT-16 et MCP-20, et ajouter à l'EXIG-INT-19 « empreinte modifiée sans incrément au moins mineur ⇒ blocage ».
- **Confiance** : vérifié dans le texte.

### [09-07] [MINEUR] Unité de versionnage ambiguë : l'outil ou le serveur
- **Axe** : C
- **Localisation** : tableau 22 (p. 81) : pour l'« Outil MCP », « Version et empreinte »; EXIG-INT-15 : « pour chaque outil, ressource, invite »; EXIG-INT-17 (p. 83) : « chaque version de contrat (schéma, serveur MCP, carte d'agent A2A, sujet AsyncAPI) ».
- **Diagnostic** : le tableau 22 et l'EXIG-INT-15 versionnent l'outil, alors que l'EXIG-INT-17 versionne le serveur. On ne sait pas si l'ajout d'un outil à un serveur incrémente le serveur, ni si une modification d'un outil incrémente ses voisins.
- **Correctif proposé** : fixer l'unité (outil, ressource ou invite), et le serveur comme simple agrégat d'entrées.
- **Confiance** : vérifié dans le texte.

### [09-08] [MAJEUR] Des « consommateurs non déclarés » ne devraient pas exister si la passerelle applique l'épinglage
- **Axe** : B
- **Localisation** : EXIG-INT-18 (p. 83) : « rapprochés chaque mois des appels observés par la passerelle »; « les traces servent à repérer, avant l'échéance, les appels de consommateurs non déclarés ».
- **Diagnostic** : selon les EXIG-INT-15, INT-17, MCP-20 et SEC-18, la passerelle connaît l'identité de l'agent appelant, sa fiche et ses épinglages. Si un consommateur non déclaré peut appeler une version, c'est que la passerelle n'applique pas la liste des consommateurs, ce qui contredit la thèse T2 (point unique d'application). Le rapprochement mensuel ne laisse, de plus, que deux occasions de détection dans la fenêtre de 60 jours.
- **Contre-exemple** : un agent appelle un outil sans l'avoir déclaré. Il est détecté au jour 45, et l'échéance du jour 60 le casse quand même.
- **Correctif proposé** : faire refuser par la passerelle, en temps réel, tout appel d'une version absente de la fiche de l'appelant. Ramener le rapprochement à un contrôle de cohérence, et le rendre continu pendant la fenêtre de dépréciation.
- **Confiance** : déduit.

### [09-09] [MINEUR] Renvoi erroné : l'EXIG-APP-08 au lieu de l'EXIG-APP-03
- **Axe** : C
- **Localisation** : EXIG-INT-19 (p. 84) : « (ou d'une suite équivalente approuvée par l'architecture d'entreprise, EXIG-APP-08) ».
- **Diagnostic** : l'EXIG-APP-08 (p. 191) est la clause contractuelle sur la conformité MCP et la délégation. C'est l'EXIG-APP-03 (p. 190) qui prévoit « une suite équivalente approuvée par l'architecture d'entreprise ».
- **Correctif proposé** : remplacer le renvoi par l'EXIG-APP-03.
- **Confiance** : vérifié dans le texte.

### [09-10] [MINEUR] Portée de l'a2a-tck différente entre l'EXIG-INT-19 et l'EXIG-A2A-14; trousse 1.0 en alpha
- **Axe** : C
- **Localisation** : EXIG-INT-19 : « la nouvelle version DOIT réussir [...] pour un agent A2A, les tests MUST d'a2a-tck »; EXIG-A2A-14 : « à chaque nouvelle version mineure ou majeure ».
- **Diagnostic** : l'EXIG-INT-19 vise toute nouvelle version, correctifs compris, alors que l'EXIG-A2A-14 ne vise que les versions mineures et majeures. Les tests a2a-tck sont bloquants, et ceux de MCP informatifs au motif que la suite est « en préversion 0.x ». Or la ligne 1.0 de l'a2a-tck est elle-même étiquetée alpha : déjà relevé à l'annexe H (tableau des dépendances, ligne a2a-tck, p. 277), mais pas en H.4.
- **Correctif proposé** : aligner les deux portées et appliquer le même critère de maturité aux deux suites.
- **Confiance** : vérifié dans le texte.

### [09-11] [MINEUR] « Tests de contrat de ses consommateurs connus » : mal défini quand le consommateur est un modèle
- **Axe** : B
- **Localisation** : EXIG-INT-19 : « la nouvelle version DOIT réussir les tests de contrat de ses consommateurs connus ».
- **Diagnostic** : quand les consommateurs sont des agents, aucun artefact de test de contrat piloté par le consommateur n'est défini (ni à l'annexe B, ni au tableau 22). On ne voit donc pas comment l'exigence se vérifie.
- **Correctif proposé** : définir le test (jeu d'évaluation de l'agent consommateur rejoué en environnement isolé contre la nouvelle version, § 10.4) et son seuil de réussite.
- **Confiance** : déduit.

### [09-12] [MINEUR] La coexistence des types d'événements n'est pas réglée
- **Axe** : B
- **Localisation** : tableau 22 : pour le sujet d'événement, « Contrat AsyncAPI 3.x et type versionné »; EXIG-INT-14.
- **Diagnostic** : un changement incompatible crée un nouveau type (`.v2`, EXIG-EVT-03). Une coexistence de 60 jours suppose alors une double publication v1 et v2, que rien n'encadre. Un consommateur abonné aux deux pendant sa migration traiterait deux fois le même fait, faute d'une clé d'idempotence commune aux deux types.
- **Correctif proposé** : exiger, pendant la coexistence, un identifiant de fait commun (`id` ou clé métier) et une déduplication côté consommateur.
- **Confiance** : déduit.

### [09-13] [MINEUR] EXIG-INT-20 : lue à la lettre, la règle interdit de qualifier de « standard » tout projet extérieur à l'AAIF
- **Axe** : C
- **Localisation** : p. 84 : « NE DOIT PAS qualifier un projet de standard ou de projet de l'AAIF s'il ne figure pas à la liste des projets publiée par la fondation ».
- **Diagnostic** : prise littéralement, la règle interdit d'appeler « standard » CloudEvents, OpenAPI ou une RFC. Elle laisse aussi entendre que figurer à la liste suffit pour être un standard, ce que dément la phrase suivante (« ne dispense d'aucun critère »).
- **Correctif proposé** : écrire « NE DOIT PAS qualifier un projet de “projet de l'AAIF” ni de “standard de l'AAIF” s'il... ».
- **Confiance** : vérifié dans le texte.

### [09-14] [MINEUR] Le tableau 15 renvoie au § 6.9 pour une règle qui n'y figure pas
- **Axe** : C
- **Localisation** : tableau 15 (p. 50), ligne AGNTCY : « aucune dépendance de production sans décision du comité (6.9) ».
- **Diagnostic** : le § 6.9 (EXIG-INT-21) traite des pilotes subordonnés au catalogue et des propriétés alléguées. Aucune exigence n'y porte sur une décision du comité pour une dépendance de production.
- **Correctif proposé** : ajouter cette règle à l'EXIG-INT-21, ou corriger le renvoi.
- **Confiance** : vérifié dans le texte.

### [09-15] [MAJEUR] EXIG-INT-22 : paiement en l'absence de l'utilisateur contradictoire et indéfini pour les agents ambiants
- **Axe** : A
- **Localisation** : p. 85 : « n'être exécuté qu'avec une approbation humaine signée, liée à l'action exacte »; « Le paiement en l'absence de l'utilisateur NE DOIT PAS être autorisé tant qu'aucun protocole qui l'encadre n'a le statut Adopter ».
- **Diagnostic** : la première phrase exige, sans exception, une approbation humaine liée à l'action exacte. La clause « tant que » laisse pourtant entendre qu'une fois un protocole au statut Adopter (AP2 et ses mandats d'intention, liés à des contraintes et non à l'action exacte), le paiement en l'absence de l'utilisateur deviendrait admissible, ce que la première phrase continue d'interdire. On ne sait pas non plus qui est « l'utilisateur ». Pour un agent ambiant (§ 8.6), sans mandant présent, tout paiement est-il « en l'absence de l'utilisateur », donc interdit même si un approbateur des comptes fournisseurs signe ?
- **Contre-exemple** : un agent ambiant d'approvisionnement prépare un paiement de facture, et le responsable des comptes fournisseurs le signe. Selon la première phrase, c'est conforme; selon la seconde, c'est interdit.
- **Correctif proposé** : définir « absence de l'utilisateur » (aucune approbation humaine propre à la transaction) et préciser que l'approbateur peut être distinct du mandant. Dire si l'adoption future d'un protocole pourrait, ou non, assouplir la première phrase.
- **Confiance** : vérifié dans le texte.

### [09-16] [MAJEUR] EXIG-INT-22 : jetons de paiement sans usage unique ni échéance, preuve d'intention sans signataire défini
- **Axe** : A
- **Localisation** : p. 85 : « il ne manipule que des jetons émis hors de lui, limités à un bénéficiaire et à un montant »; « une preuve d'intention signée ».
- **Diagnostic** : un jeton limité au bénéficiaire et au montant, mais réutilisable et sans échéance, permet de rejouer le paiement (double débit lors d'une reprise, EXIG-ORC-12). Le jeton partagé de l'ACP, que le texte prend pour modèle, est aussi borné dans le temps (d'après mes connaissances, à vérifier). Le signataire de la « preuve d'intention » n'est pas désigné : une signature de l'agent ne prouve pas l'intention humaine. La règle ne dit pas non plus en quoi un tel jeton n'est pas lui-même un « justificatif de paiement » que l'agent transmet.
- **Contre-exemple** : à la suite d'une expiration de délai, l'orchestrateur réessaie l'étape. Le même jeton est présenté deux fois au marchand, et l'exigence n'impose pas d'usage unique.
- **Correctif proposé** : exiger des jetons à usage unique, à courte échéance, liés à l'empreinte de l'approbation (§ 8.5) et à la clé d'idempotence. Préciser que la preuve d'intention est l'approbation signée de l'humain, et définir « justificatif de paiement ».
- **Confiance** : vérifié dans le texte pour le libellé; la portée temporelle du jeton ACP est à vérifier (source externe).

### [09-17] [MINEUR] « Trois protocoles se partagent le commerce agentique » : affirmation probablement incomplète
- **Axe** : B
- **Localisation** : p. 85 : « Trois protocoles se partagent le commerce agentique, sans convergence ».
- **Diagnostic** : d'après mes connaissances, d'autres initiatives existaient dès 2025 : Visa Trusted Agent Protocol / Intelligent Commerce, Mastercard Agent Pay, x402 de Coinbase. L'exhaustivité affirmée est douteuse.
- **Correctif proposé** : écrire « Trois protocoles principaux », ou ajouter les autres au catalogue (statut Surveiller).
- **Confiance** : à vérifier (source externe).

### [09-18] [MINEUR] L'EXIG-INT-23 ne couvre pas les entrées au statut Adopter, que visent pourtant ses propres signaux
- **Axe** : C
- **Localisation** : EXIG-INT-23 (p. 86) : « Chaque entrée du catalogue des protocoles au statut Évaluer ou Surveiller DOIT indiquer le signal »; signaux (p. 85) : « une révision de MCP ».
- **Diagnostic** : MCP, et vraisemblablement les conventions OpenTelemetry, sont au statut Adopter, et ne sont donc pas soumis à l'EXIG-INT-23. Or ce sont deux des trois signaux cités. Que la feuille de route de MCP ne donne pas de date est déjà consigné en H.4 (no 3, incohérence avec la Veille, non un erratum). Le défaut de portée, lui, n'y est pas.
- **Correctif proposé** : étendre l'exigence aux entrées Adopter (signaux de nouvelle révision, de dépréciation, de version stable).
- **Confiance** : vérifié dans le texte (statut des conventions OpenTelemetry déduit).

### [09-19] [MINEUR] « Première version étiquetée des conventions GenAI » : formule ambiguë
- **Axe** : C
- **Localisation** : p. 85 : « la première version étiquetée des conventions GenAI d'OpenTelemetry[181] ».
- **Diagnostic** : le § 10.1 (p. 145) précise que ces conventions ont paru dans des versions étiquetées de `semantic-conventions` (v1.41.0, v1.41.1), et que c'est le dépôt dédié `semantic-conventions-genai` qui n'en a pas encore. Lue seule, la formule est inexacte.
- **Correctif proposé** : écrire « la première version étiquetée du dépôt dédié semantic-conventions-genai (§ 10.1) ».
- **Confiance** : vérifié dans le texte.

### [09-20] [MAJEUR] EXIG-ORC-02 : critère d'acceptation incommensurable, sans protocole statistique, et tolérant une régression de qualité
- **Axe** : B
- **Localisation** : p. 87 : « Elle n'est retenue que si le gain de qualité ou de délai couvre le surcoût mesuré ».
- **Diagnostic** : on y compare des grandeurs de nature différente (points de taux de réussite ou secondes, contre des dollars) sans fonction de valeur déclarée. L'exigence ne fixe ni taille d'échantillon, ni répétitions, ni intervalle de confiance, alors que les évaluations de modèles sont bruitées. Le « ou » permet en outre de retenir une topologie plus rapide mais moins fiable. Telle quelle, l'exigence ne se vérifie pas de façon reproductible en revue.
- **Contre-exemple** : sur 30 tâches, la topologie multiagent réussit 2 tâches de moins, mais répond 40 % plus vite. Le « gain de délai » la qualifie.
- **Correctif proposé** : exiger la non-régression du taux de réussite (borne inférieure de l'intervalle de confiance), une valeur monétaire déclarée par tâche réussie, et un nombre minimal d'exécutions et de répétitions, renvoyés au § 10.4.
- **Confiance** : vérifié dans le texte.

### [09-21] [MINEUR] EXIG-ORC-01 : liste des « options plus simples » circulaire pour l'agent unique et ordre différent de celui de la figure 12
- **Axe** : C
- **Localisation** : p. 87 : « pourquoi les options plus simples (code ou règle métier, appel direct au modèle, flux déterministe, agent unique outillé) ne répondent pas ».
- **Diagnostic** : prise à la lettre, la liste oblige un agent unique outillé à justifier pourquoi un agent unique outillé ne suffit pas. Elle place aussi l'appel direct avant le flux déterministe, alors que la figure 12 fusionne « règle » et « appel direct » à la première question.
- **Correctif proposé** : écrire « les options plus simples que le patron retenu, dans l'ordre de la figure 12 ».
- **Confiance** : vérifié dans le texte.

### [09-22] [MAJEUR] Délégation descendante : l'autonomie et la classe peuvent être « blanchies » par l'exécutant
- **Axe** : A
- **Localisation** : § 7.2 (p. 89) : « Un orchestrateur plafonné à N3 peut ainsi déléguer à un exécutant plafonné à N1, et chaque action reste soumise à la règle la plus stricte entre le niveau de l'agent qui agit et le palier ».
- **Diagnostic** : la règle ne considère que l'agent qui agit, comme l'EXIG-AUT-10 (p. 110). Le cas inverse n'est pas traité : un orchestrateur N1, ou de classe élevée (plafond N2), qui délègue à un exécutant N3 de classe modérée obtient des écritures P2 autonomes que lui-même ne pourrait pas faire. L'intersection des droits (§ 9.3) borne les portées OAuth, pas le niveau d'autonomie ni le contrôle de la figure 15. La phrase omet aussi la classe, que le § 8.4 inclut (« classe, niveau, palier »).
- **Contre-exemple** : un agent consultatif N1, de classe élevée, délègue « mets à jour les 20 dossiers » à un exécutant N3 de classe modérée. Sous le seuil, l'exécutant agit seul (figure 15, Modéré × P2).
- **Correctif proposé** : écrire que le contrôle applicable est le plus strict de la chaîne (niveau et classe minimaux entre l'initiateur et l'agent qui agit), transmis dans le jeton délégué ou dans le contexte de la tâche, et vérifié par la passerelle.
- **Confiance** : déduit, après vérification des § 8.4 et 9.3.

### [09-23] [MAJEUR] Figure 12 : l'événement mène à la chorégraphie, le routage passe avant l'agent unique, et deux patrons sont inatteignables
- **Axe** : A (et C)
- **Localisation** : figure 12 (p. 91) : « Déclenchement par une personne ou un événement? événement → Chorégraphie événementielle »; « la première réponse qui conclut fixe le patron ».
- **Diagnostic** : (a) le mode de déclenchement n'est pas un critère de topologie. Le tableau 24 réserve la chorégraphie aux « Processus interdomaines faiblement couplés, gros volumes ». L'arbre impose donc le patron le moins prévisible (tableau 25 : « Moyenne, émergente ») à tout agent ambiant à étapes non prédéfinies, ce qui contredit l'EXIG-ORC-01 et la règle « part toujours de l'option la plus simple ». (b) Le routage, qui comprend un routeur et plusieurs spécialistes, est retenu avant même qu'on se demande si un agent unique suffit, ce qui contourne l'esprit de l'EXIG-ORC-02. (c) Aucune feuille ne mène à la « Chaîne séquentielle » ni au « Clavardage de groupe », pourtant autorisés (tableau 24, EXIG-ORC-06).
- **Contre-exemple** : un agent qui surveille une boîte de réception et résume chaque courriel reçu (déclenchement par événement, étapes simples) aboutit à « Chorégraphie », avec saga et propriétaire de bout en bout (EXIG-ORC-08), alors qu'un agent unique suffisait.
- **Correctif proposé** : faire du déclenchement une question orthogonale (« plusieurs domaines faiblement couplés réagissent-ils au même fait? »), placer « agent unique » avant « routage », et ajouter des feuilles pour la chaîne séquentielle et le clavardage de groupe.
- **Confiance** : vérifié dans le texte (figure reconstituée depuis l'extraction).

### [09-24] [MAJEUR] Saga en chorégraphie : les exigences du § 7.5 supposent un orchestrateur, et le compteur de sauts peut bloquer les compensations
- **Axe** : A
- **Localisation** : tableau 24 (p. 89) : « saga dès que des effets touchent plusieurs systèmes d'enregistrement »; EXIG-ORC-08 (p. 91) : « une saga explicite (section 7.5) et les contrôles d'enveloppe de la section 6.7 ».
- **Diagnostic** : les EXIG-ORC-16 et ORC-18 (p. 95) attribuent le journal de compensation et l'escalade à « l'orchestrateur », qui par définition n'existe pas en chorégraphie (« sans chef d'orchestre »). La chorégraphie ne peut donc pas satisfaire au § 7.5 tel qu'il est rédigé. Le compteur de sauts (EXIG-EVT-06, plafond par défaut de 4) s'applique en outre aux événements publiés « en réaction », donc aux événements de compensation, et une saga qui échoue près du plafond ne peut plus se compenser.
- **Contre-exemple** : les étapes aux sauts 1 à 3 écrivent, et l'étape au saut 4 est rejetée en lettres mortes. Les événements de compensation publiés en réaction portent un compteur supérieur ou égal à 4 : rejetés à leur tour, ils laissent la saga à moitié appliquée, sans orchestrateur pour l'escalader.
- **Correctif proposé** : désigner, pour toute chorégraphie à effets, un composant propriétaire de la saga (journal et escalade), ou imposer une saga orchestrée. Exclure les événements de compensation du plafond, ou leur réserver une marge.
- **Confiance** : déduit, après vérification du § 6.7 et des EXIG-ORC-16 et ORC-18.

### [09-25] [MINEUR] Évaluateur-optimiseur : « modèle distinct » dans la figure, « modèle ou invite » dans l'exigence; décompte des itérations ambigu
- **Axe** : C
- **Localisation** : figure 11 (p. 88) : « critique sur un modèle distinct »; EXIG-ORC-05 (p. 90) : « à un modèle ou à une invite distincts de ceux du producteur »; « trois itérations au plus ».
- **Diagnostic** : la figure exige un modèle distinct, alors que l'exigence se contente d'une invite distincte. On ne sait pas non plus si la production initiale compte comme une itération (trois productions, ou une production et trois révisions).
- **Correctif proposé** : aligner la figure sur l'exigence, ou l'inverse, et définir l'itération comme un cycle production et évaluation.
- **Confiance** : vérifié dans le texte.

### [09-26] [MINEUR] Clavardage de groupe : trois agents en tout, ou trois plus le gestionnaire
- **Axe** : C
- **Localisation** : tableau 24 (p. 89) : « Trois agents au plus »; EXIG-ORC-06 (p. 91) : « trois agents participants au plus, sous un gestionnaire (hors décompte des trois participants) ».
- **Diagnostic** : le tableau et la figure ne précisent pas que le gestionnaire est hors décompte. Si la recommandation de Microsoft compte le gestionnaire, l'EXIG-ORC-06 l'excède (quatre agents).
- **Correctif proposé** : harmoniser le tableau 24, et vérifier le mode de décompte de la source [9].
- **Confiance** : texte vérifié; le décompte de Microsoft est à vérifier (source externe).

### [09-27] [MINEUR] Parallélisation : garde-fou concurrent non bloquant, et sens de « un seul composant » en combinaison
- **Axe** : A
- **Localisation** : tableau 24 (p. 89) : « garde-fou exécuté en parallèle de la tâche »; EXIG-ORC-07 (p. 91) : « un seul composant DOIT écrire le résultat final ».
- **Diagnostic** : la règle de fusion (« déterministe, vote ou arbitrage ») ne dit pas que l'écrivain doit attendre le verdict du garde-fou, ni ce qu'il fait si ce dernier expire (mode fermé, PRIN-12). Combinée au patron 5 (« parallèle si possible », figure 12), elle laisse aussi ouverte la question de savoir si des exécutants parallèles peuvent chacun écrire dans leur propre système d'enregistrement.
- **Correctif proposé** : faire du verdict des branches de garde-fou une condition bloquante de la fusion, avec refus en cas d'expiration, et préciser « un seul écrivain par système d'enregistrement, sous saga s'il y en a plusieurs ».
- **Confiance** : déduit.

### [09-28] [MINEUR] Données probantes : la profondeur de délégation n'est pas mesurée, et des chiffres sont tirés du billet plutôt que de la version 3
- **Axe** : B
- **Localisation** : « Pourquoi » de l'EXIG-ORC-04 (p. 90) : « sans validation centrale, amplifie les erreurs[273] »; § 7.1 : 17,2 fois et 4,4 fois tirés du billet [273], alors que la version 3 [274] donne d'autres agrégats.
- **Diagnostic** : la mesure de Google compare des architectures indépendantes et centralisées, et non des profondeurs de délégation. Elle n'étaye pas la limite de deux niveaux (le texte le reconnaît : « indirectement »). On ne sait pas si les chiffres 17,2 et 4,4 tiennent dans la version 3.
- **Correctif proposé** : citer les chiffres de la version 3, ou dire qu'ils proviennent de la version du billet.
- **Confiance** : à vérifier (source externe).

### [09-29] [MINEUR] Périmètre flou de « topologie à plusieurs agents » dans l'EXIG-ORC-02
- **Axe** : C
- **Localisation** : EXIG-ORC-02 : « Une topologie à plusieurs agents DOIT être comparée [...] à une base de référence à agent unique ».
- **Diagnostic** : on ne sait pas si un routeur non agentique, ou un évaluateur qui n'est qu'« une invite distincte » (EXIG-ORC-05), font du système un multiagent soumis à la preuve mesurée.
- **Correctif proposé** : renvoyer à la définition d'agent du tableau 7 et énumérer les patrons soumis à l'EXIG-ORC-02.
- **Confiance** : vérifié dans le texte.

### [09-30] [MINEUR] SemVer : reformulation de description mineure, ou changement de sens majeur
- **Axe** : A
- **Localisation** : p. 82 : « mineur : ajout compatible et toute reformulation d'une description » / « majeur : [...] changement de sens à format constant ».
- **Diagnostic** : la description étant une consigne pour le modèle (« Pourquoi » de l'EXIG-INT-16), une reformulation peut en changer le sens (« ne supprime pas » retiré). La règle le permet en lisant « mineure » comme un plancher (EXIG-INT-13 : « au moins mineure »), mais la liste à puces se lit comme une classification définitive.
- **Correctif proposé** : écrire « mineur : reformulation qui ne change pas le sens, établie par la revue sémantique (EXIG-INT-16) ».
- **Confiance** : vérifié dans le texte.

### [09-31] [MINEUR] Date de la prochaine révision de MCP (signal de l'EXIG-INT-23) — déjà consigné en H.4
- **Axe** : C
- **Localisation** : p. 85 : « une révision de MCP, dont la feuille de route du 22 août 2026 ne donne pas la date[195] ».
- **Diagnostic** : déjà consigné en H.4 (tableau 72, no 3) comme incohérence entre livrables : la SEP-3398 a été versée le 27 octobre et la date du 30 mars 2027 est à inscrire comme signal survenu.
- **Correctif proposé** : celui du tableau 72.
- **Confiance** : vérifié dans le texte.

## Points forts
Le § 6.9 distingue avec rigueur hébergement, candidature et maturité (EXIG-INT-20, 21), et la chronologie de l'AAIF concorde avec le tableau 5 (dix projets). Le § 7.1 qualifie honnêtement ses sources (évaluation interne, résultats déclarés par le fournisseur, contrainte de produit), et les chiffres d'Anthropic (90,2 %, 4 fois et 15 fois, 80 % de la variance) concordent avec ce que j'en connais. La séparation entre contrat publié et entrée de catalogue (tableau 22) est saine.

## Questions pour l'audit bibliographique
- p. 90 : RFC 8693 § 4.1 : les `act` imbriqués sont-ils « informational only » et exclus des décisions d'accès ? (tranche 09-02)
- p. 82 : la définition `Tool` de MCP 2026-07-28 est-elle bien sans champ de version [197], et le champ `version` d'une carte A2A est-il de format libre [68] ? Une extension A2A incompatible exige-t-elle une nouvelle URI [238] ?
- p. 82 : l'OWASP [221] recommande-t-il l'épinglage par empreinte et un nouveau consentement à chaque modification ?
- p. 83 : le cycle Active, Deprecated, Removed de MCP [34]; registre officiel toujours en préversion [43].
- p. 84 : état de la suite de conformité MCP (0.2.0-alpha) [225, 226]; AAIF à dix projets au 22 octobre 2026 [38, 130]; processus d'admission [42, 263].
- p. 84 : AGNTCY à la Linux Foundation le 29 juillet 2025 [23]; proposition no 57 du 12 octobre 2026 et 81 organisations [37]; OASF inspiré d'OCSF, ADS sur OCI, SLIM sur gRPC et MLS RFC 9420, Agent Badges [264-270]; brouillons IETF individuels [271, 272].
- p. 85 : ACP en bêta, portée du jeton partagé (marchand, montant, échéance ?) [183, 27]; AP2 0.2 et Human Not Present, don à la FIDO Alliance le 28 avril 2026 [26, 41]; UCP de janvier 2026 [184]; existence d'autres protocoles (Visa TAP, Mastercard Agent Pay, x402).
- p. 86 : Google Research, billet du 28 janvier 2026 (180 configurations; +80,9 %; −39 à −70 %; 17,2 fois et 4,4 fois) [273] et version 3 du 8 avril 2026 (260 configurations; +80,8 % à −70,0 %) [274]; auteurs « Kim, Liu et coll. ».
- p. 86 : article d'Anthropic du 23 janvier 2026, surcoût de 3 à 10 fois, trois cas justifiant le multiagent, « victoire prématurée » [275].
- p. 87 : Cognition [276], LangChain [277], Centre d'architecture Azure (niveaux de complexité, trois motifs) [9].
- p. 89 : Agentforce, un seul niveau de délégation multiorganisation [49]; Magentic-One dans Microsoft Agent Framework [278, 279].
- p. 90 : « Mind Viruses », Papadopoulos et coll., août 2026 [280]; recommandation de Microsoft de limiter le clavardage de groupe à trois agents, gestionnaire compris ou non [9].
- p. 92 : OpenAI, moins de 20 fonctions [115] et 15 ou 10 outils [66]; Anthropic, de 30 à 50 outils [281]; recherche d'outils (−85 %; 49 → 74 %; 79,5 → 88,1 %) [205].
