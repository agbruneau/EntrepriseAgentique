# Audit chunk_03 — pages 21-32

## Synthèse
Le chunk couvre la fin du tableau 7 et les deux échelles (§ 3.1), flux ou agent (§ 3.2), interactifs ou ambiants (§ 3.3), ce qu'un agent n'est pas (§ 3.4), les douze principes, le tableau 9, la préséance, le tableau 10 et les dérogations (ch. 4), puis l'ouverture du ch. 5. La rédaction est dense et les sources sont bien attribuées, mais les règles de combinaison ont des trous formels.
Les trois défauts les plus graves :
1. L'arbitrage « fonction locale » et l'exception intradomaine d'EXIG-ARC-01 laissent sans vérificateur l'approbation P3, pourtant non dérogeable (03-08).
2. La frontière N3/N4 est indécidable pour un agent ambiant, ce qui permet de contourner la décision du comité (03-02).
3. La définition de la compensation rend P2 et P3 non disjoints (03-03).

## Constats

### [03-01] [MAJEUR] Le patron par défaut du cadre n'a pas de niveau d'autonomie, et N0 contredit la définition d'agent
- **Axe** : A
- **Localisation** : § 3.1-3.2, p. 22-23 : « N0 Automatisation déterministe : aucun modèle » et « Flux de travail assisté par IA. […] C'est le patron par défaut du cadre. » Voir aussi « Appel direct au modèle » (p. 23) et la définition d'Agent (p. 21) : « au moyen d'un modèle ».
- **Diagnostic** : l'échelle N0-N4 s'applique « partout » (p. 22), et EXIG-AUT-01 exige que « Chaque agent DOI[ve] avoir un niveau d'autonomie N0 à N4 ». Deux problèmes :
  - Par définition, un agent utilise un modèle et N0 n'en a aucun : N0 ne peut donc pas être le niveau d'un agent.
  - Le flux assisté par IA et l'appel direct au modèle utilisent un modèle sans être des agents. Ils ne sont pas N0 (il y a un modèle) et ne sont pas clairement N1-N4 (ce ne sont pas des agents). Pourtant, le ch. 9 (p. 145) assimile « un flux déterministe (N0) », alors que le tableau 7 range sous « flux déterministe » les flux qui appellent un modèle.
- **Contre-exemple** : un flux codé fait classer un courriel par le modèle, puis le code crée un billet (P2). Il n'est pas N0 (un modèle est appelé). S'il est N1, il n'a pas le droit d'écrire. S'il est N2, chaque écriture exige une approbation. S'il est N3, il faut un ODD. Aucune règle ne tranche, et la passerelle ne peut pas appliquer EXIG-AUT-10.
- **Correctif proposé** :
  - Définir N0 comme « aucun choix laissé au modèle » plutôt que « aucun modèle ».
  - Ou bien, créer une règle explicite : un flux assisté par IA hérite du niveau qui correspond à ses écritures déclenchées par une sortie de modèle (sans approbation, cela équivaut à N3).
  - Dans EXIG-AUT-01, remplacer « N0 à N4 » par « N1 à N4 » pour les agents.
- **Confiance** : vérifié dans le texte (contradiction); déduit (scénario).

### [03-02] [MAJEUR] Frontière N3/N4 indécidable pour un agent ambiant, ce qui contourne la décision du comité
- **Axe** : A
- **Localisation** : § 3.3, p. 24 : « Un agent ambiant peut […] agir seul sous seuils (N3); seul le niveau N4 combine le déclenchement sur événements, l'exécution continue et l'absence de la personne ». Définition de N4, p. 23.
- **Diagnostic** : selon le tableau 28, N4 a les mêmes paliers permis que N3 (« Comme N3; P3 toujours approuvé »). Seuls le déclenchement autonome et l'« exécution continue » le distinguent, et ce dernier critère n'est défini nulle part. Or un agent ambiant N3 se déclenche déjà sur des événements et agit seul sous seuils. Cette distinction n'est pas observable, alors qu'elle décide de la licéité : N4 n'est permis qu'à la classe faible, sur décision du comité (EXIG-CON-02).
- **Contre-exemple** : un agent de classe modérée consomme un flux Kafka 24 h sur 24 et ferme seul des billets en double (P2 sous seuil). Déclaré N3 « ambiant », il est conforme. C'est pourtant exactement le comportement de l'exemple N4 du tableau 28 (« sur alerte […] jour et nuit »). L'équipe évite ainsi la décision du comité et l'exigence d'un ODD certifié.
- **Correctif proposé** : définir N4 par un critère observable, par exemple « aucune personne n'est désignée pour traiter les escalades dans un délai borné pendant la plage d'exploitation » ou « le déclencheur n'est pas une demande d'un mandant humain ». À défaut, classer en N4 tout agent qui s'autodéclenche et agit en écriture sans personne de garde. Ajouter ce critère au tableau 30.
- **Confiance** : vérifié dans le texte.

### [03-03] [MAJEUR] La définition de la compensation rend P2 et P3 non disjoints
- **Axe** : A
- **Localisation** : p. 22, Compensation : « Elle ne rétablit pas forcément l'état initial ». Paliers, p. 23 : « P2 écriture réversible; P3 action critique, externe ou irréversible ». Définition de N3, p. 22 : « actions P2 réversibles ou compensables ».
- **Diagnostic** : P2 couvre les écritures « réversibles ou compensables » (N3, tableau 31), et P3 couvre les écritures « irréversibles ». Puisque le cadre admet qu'une compensation ne rétablit pas l'état initial, une action compensable peut être irréversible : elle tombe à la fois en P2 et en P3. EXIG-AUT-08 ne tranche pas ce cas. Sa règle du « palier le plus élevé » vise un outil « qui combine plusieurs effets », pas un effet unique qui a deux propriétés. Sa règle « sans compensation déclarée → P3 » pousse même vers P2 dès qu'une compensation est déclarée.
- **Contre-exemple** : une écriture comptable interne, compensée par une contre-passation, reste irréversible puisque l'écriture d'origine demeure au grand livre. Un autre exemple : l'envoi d'un avis interne, compensé par un « avis rectificatif » (exemple d'EXIG-ORC-17). Classé P2, l'outil est exécuté seul par un agent N3, alors que l'invariant non dérogeable « P3 jamais seul » visait précisément l'irréversible.
- **Correctif proposé** : rendre les paliers disjoints par une règle de préséance explicite, par exemple « irréversible ou externe ⇒ P3, même s'il existe une compensation ». Redéfinir P2 comme « réversible, ou compensable avec un état final équivalent et un impact borné ». Inscrire cette règle dans EXIG-AUT-08.
- **Confiance** : vérifié dans le texte (définitions); déduit (exemples).

### [03-04] [MAJEUR] L'intersection des droits à deux termes n'est pas compositionnelle dans une chaîne de délégation
- **Axe** : A
- **Localisation** : PRIN-03, p. 26 : « les droits effectifs d'un agent délégué ne dépassent jamais l'intersection des droits du mandant et de ceux de l'agent ». Définition de Délégation, p. 21 : « envoi d'une tâche à un autre agent, sans plus de droits que n'en a le mandant ».
- **Diagnostic** : dans une chaîne M → A → B, la règle donne à B les droits M ∩ B, qui peuvent dépasser les droits de A. A peut alors obtenir, par B, plus que ce qu'il pouvait faire lui-même : c'est une élévation par un « adjoint confus » (confused deputy). La définition de Délégation, qui ne borne que par le mandant, est plus faible que celle du Jeton délégué (« sa portée ne s'élargit jamais d'un saut à l'autre »). Le cadre énonce donc deux invariants différents. Par ailleurs, le serveur d'autorisation ne peut calculer l'intersection que sur des portées (scope). Les droits fins (ligne, document, ReBAC) ne sont connus que du serveur de ressources, donc « le serveur d'autorisation l'applique à chaque échange » est inexact pour ces droits.
- **Contre-exemple** : M, gestionnaire, peut tout lire. A, agent de tri, ne peut lire que les billets. B, agent RH, peut lire la paie. A délègue à B « au nom de M ». B lit la paie (M ∩ B), puis renvoie le résultat à A, qui n'y avait pas droit.
- **Correctif proposé** : énoncer l'invariant sous la forme droits(Bₖ) ⊆ M ∩ A₁ ∩ … ∩ Aₖ, en cohérence avec le jeton délégué. Préciser que l'intersection des portées se fait au serveur d'autorisation, et que celle des droits fins se fait au serveur de ressources, qui évalue la chaîne `act` complète. Aligner la définition de Délégation (p. 21).
- **Confiance** : vérifié dans le texte (formulation); déduit (scénario). À recouper avec le § 9.3 (chunk 13).

### [03-05] [MAJEUR] La borne « jamais supérieurs à ceux de son mandant » est vide pour un agent autonome ou ambiant
- **Axe** : A
- **Localisation** : PRIN-03, p. 26 : « Ses droits sont minimaux, de courte durée et jamais supérieurs à ceux de son mandant ». Définition de Mandant, p. 21 : « Personne, application ou agent ».
- **Diagnostic** : pour un agent qui s'autodéclenche (N4, ambiant), le mandant est l'« identité de l'agent autonome et de son propriétaire » (EXIG-ARC-02) ou l'« identité du service » (EXIG-ARC-04). Si le mandant est l'agent lui-même, la borne devient réflexive (droits(A) ⊆ droits(A)). Si c'est le propriétaire, l'agent hérite potentiellement des droits étendus d'un gestionnaire. Dans les deux cas, PRIN-03 ne borne plus rien. La définition de Mandant, qui inclut « agent », autorise cette circularité.
- **Contre-exemple** : un agent ambiant de qualité des données, dont le propriétaire est un directeur des données, reçoit les droits du directeur sur tous les entrepôts. PRIN-03 est formellement respecté.
- **Correctif proposé** : pour un mandant non humain, borner les droits par une liste d'autorisations approuvée au registre, indépendante des droits du propriétaire. Interdire qu'un agent soit son propre mandant.
- **Confiance** : vérifié dans le texte (définitions); déduit (conséquence).

### [03-06] [MAJEUR] La règle de départage « à rang égal » est indécidable
- **Axe** : A
- **Localisation** : § 4.3, p. 29 : « À rang égal, on retient l'option la plus simple qui respecte les deux principes en présence ».
- **Diagnostic** : il n'y a conflit que si aucune option ne satisfait les deux principes. La règle présuppose donc l'existence de l'objet dont l'absence définit le conflit. Elle ne départage rien dans un vrai conflit. Le rang 2 réunit sept principes sans ordre interne (PRIN-03 à 07, 10, 12), et le tableau 10 n'illustre qu'un seul conflit intrarang (PRIN-05 et PRIN-10).
- **Contre-exemple** : PRIN-12 (s'arrêter en cas de doute) s'oppose à PRIN-05 (compenser une saga à moitié exécutée) pendant une panne du service d'approbation, comme en 03-11. Aucune option ne respecte les deux, et la règle ne dit rien.
- **Correctif proposé** : remplacer la règle par « à rang égal, retenir l'option qui minimise l'effet irréversible; à défaut, escalader au comité », ou fixer un ordre total à l'intérieur du rang 2.
- **Confiance** : vérifié dans le texte.

### [03-07] [MAJEUR] Les engagements contractuels de rang 1 entrent en conflit avec les interdits non dérogeables
- **Axe** : A
- **Localisation** : § 4.3, p. 29 : « Le droit applicable et les engagements contractuels, qu'aucun principe ne peut écarter ». Encadré, p. 30 : « Une dérogation ne peut pas non plus écarter une obligation légale ».
- **Diagnostic** : le droit et les contrats sont placés au même rang, au-dessus des principes de protection. Or les contrats sont signés par l'entreprise elle-même. Une clause d'un fournisseur ou d'un client (par exemple un compte de service partagé imposé, ou l'exécution automatique d'un ordre au-delà d'un seuil) primerait donc sur PRIN-03 ou PRIN-05. EXIG-GOV-17, lui, ne connaît que l'obligation légale. Pour un contrat qui exige un point non dérogeable, l'ordre de préséance et l'encadré donnent des réponses opposées. Le § 1.6 (p. 13) répète « les engagements contractuels priment toujours ».
- **Contre-exemple** : un contrat de SaaS impose que l'agent du fournisseur agisse sous le compte d'un employé désigné. Selon le § 4.3, le contrat l'emporte; selon EXIG-GOV-17, l'usurpation est interdite sans dérogation possible.
- **Correctif proposé** : retirer « engagements contractuels » du rang 1, ou le subordonner aux points d'EXIG-GOV-17. Ajouter au ch. 13 l'interdiction de signer une clause contraire à ces points.
- **Confiance** : vérifié dans le texte.

### [03-08] [BLOQUANT] Exception intradomaine : personne ne vérifie l'approbation d'une action P3, pourtant non dérogeable
- **Axe** : A
- **Localisation** : tableau 10, p. 29 : « PRIN-01 vise les échanges qui franchissent une frontière de domaine; à l'intérieur, une fonction locale suffit. » Règle centrale, p. 32 : « aucun agent n'atteint un outil […] hors de son domaine sans passer par la passerelle ».
- **Diagnostic** :
  - EXIG-ARC-01 renvoie les appels intradomaines « sans serveur MCP ni pair A2A » à EXIG-IAM-17, selon lequel la décision par appel est alors appliquée « par le serveur de ressources et par l'authentification mutuelle du maillage de services ».
  - Or le calcul du contrôle (classe × palier × niveau × déclencheurs, EXIG-AUT-10), le refus au-delà du plafond (EXIG-AUT-01) et la vérification du jeton d'approbation (EXIG-AUT-12) sont confiés exclusivement à la passerelle.
  - Une fonction locale d'écriture P3 n'a ni passerelle ni serveur de ressources distinct.
  
  Aucun composant normatif ne vérifie donc l'approbation d'une action P3 intradomaine, alors qu'EXIG-AUT-09 et EXIG-GOV-17 la rendent non dérogeable. PRIN-06 n'a pas non plus de point de journalisation garanti.
- **Contre-exemple** : un agent de facturation appelle une fonction locale `emettre_virement` dans sa propre unité de déploiement, ce qu'autorise l'arbitrage du tableau 10. La passerelle ne voit jamais l'appel. Après une injection, l'agent exécute un virement sans approbation, et rien dans le cadre n'a été formellement enfreint par l'architecture.
- **Correctif proposé** : restreindre l'exception intradomaine aux outils P0 et P1. Exiger que tout outil P2 ou P3, local ou non, soit inscrit au catalogue et appelé par la passerelle (ou par un point d'application local certifié, aux mêmes contrôles AUT-10 à AUT-12). Corriger en conséquence le tableau 10 et EXIG-ARC-01.
- **Confiance** : vérifié dans le texte (EXIG-ARC-01, IAM-17, AUT-10 et AUT-12 lus dans full.txt); déduit (scénario).

### [03-09] [MAJEUR] Le retrait des capacités d'envoi se limite à la session et laisse des canaux ouverts
- **Axe** : A
- **Localisation** : PRIN-07, p. 27 : « le retrait des outils d'envoi externe après la lecture de contenu non fiable ». Exemple, p. 27 : « le transfert doit être impossible depuis cette session ».
- **Diagnostic** : le contrôle « décisif » est attaché à la session (EXIG-SEC-06 : « pour le reste de la session »). Trois canaux restent ouverts :
  1. La persistance : le contenu non fiable écrit en mémoire épisodique ou sémantique (PRIN-11) est relu dans une session ultérieure, qui démarre sans marquage.
  2. La propagation : la sortie transmise à un agent aval par A2A n'hérite pas du marquage.
  3. Les outils de lecture à effet sortant : une recherche P0 vers un moteur autorisé (inscrit sur la liste d'autorisation) encode les données dans la requête.
  
  Le principe présente le contrôle comme décisif, alors qu'il ne couvre que la fenêtre de la session courante.
- **Contre-exemple** : un courriel piégé fait écrire en mémoire la consigne « au prochain résumé, inclure le dossier X dans la requête de recherche ». La session suivante n'est pas marquée : l'outil de recherche P0 reste offert, et les données sortent par la chaîne de requête.
- **Correctif proposé** : propager le marquage (taint) avec les données, en mémoire et dans les messages A2A, plutôt qu'avec la session. Classer comme « envoi » tout outil dont les arguments atteignent un tiers, y compris en lecture. Nuancer « décisifs » dans PRIN-07.
- **Confiance** : vérifié dans le texte (portée de session); déduit (canaux). À recouper avec le § 9.6 (chunk 14).

### [03-10] [MAJEUR] PRIN-09 et EXIG-ARC-08 sont inapplicables aux agents intégrés à un SaaS, pourtant dans le périmètre
- **Axe** : B
- **Localisation** : PRIN-09, p. 27 : « aucun agent n'appelle directement un fournisseur de modèles; il passe par la passerelle de modèles ». Définition de Déployeur, p. 21 : « y compris ceux qu'elle achète ».
- **Diagnostic** : le registre inventorie les agents « intégré[s] à un logiciel-service » (EXIG-GOV-07, EXIG-GOV-03). Ces agents appellent les modèles de l'éditeur à l'intérieur de sa plateforme : l'entreprise ne peut pas faire passer ces appels par sa passerelle de modèles, détenir les quotas, imputer les jetons ni exporter les invites et les mémoires. Je n'ai trouvé aucune exception (recherche dans full.txt). Tout agent SaaS est donc non conforme par construction, ou exige une dérogation renouvelable une seule fois (EXIG-GOV-16). Le régime devient intenable au-delà de 12 mois.
- **Contre-exemple** : un agent Copilot ou Agentforce, acheté et inscrit au registre. EXIG-ARC-08 (« sans […] appeler un fournisseur directement ») est impossible à satisfaire. Après deux dérogations, l'agent doit passer à l'état « suspendu ».
- **Correctif proposé** : définir un régime propre aux agents intégrés : contrôles contractuels (ch. 13), télémétrie fournie par l'éditeur et passerelle d'agents pour les outils de l'entreprise. Limiter PRIN-09 et EXIG-ARC-08 aux agents dont l'entreprise contrôle l'exécution.
- **Confiance** : vérifié dans le texte (absence d'exception dans les passages trouvés); déduit (impossibilité technique).

### [03-11] [MAJEUR] L'échec en mode fermé bloque les compensations : la passerelle est un point unique de défaillance pour la reprise
- **Axe** : B
- **Localisation** : PRIN-12, p. 28 : « En cas de doute, le système échoue en mode fermé : il s'arrête ou escalade plutôt que d'agir ». Règle centrale, p. 32. Exemple de « Concevoir pour durer », p. 28 : « jamais rester à moitié exécuté ».
- **Diagnostic** : les outils de compensation (couche 5, fig. 3) passent par la passerelle. EXIG-AUT-11 refuse « tout appel P2 au-delà du seuil » si le service d'approbation ou de politiques est indisponible. Une compensation massive au-delà du seuil, ou toute compensation pendant une panne de la passerelle, est donc refusée. Le mode fermé, sûr pour une action nouvelle, devient dangereux pour une action de retour : il fige l'état incohérent que PRIN-12 dit vouloir éviter. EXIG-IAM-18 couvre la panne du plan de contrôle, pas celle de la passerelle elle-même.
- **Contre-exemple** : une saga débite 300 comptes, puis le crédit échoue. La compensation (300 remboursements, au-delà du seuil de 25 par tâche) doit être approuvée, mais le service d'approbation est en panne. Les clients restent débités pendant toute la panne.
- **Correctif proposé** : distinguer les actions nouvelles (mode fermé) des compensations déclarées au catalogue, qui seraient pré-autorisées et exemptes du seuil dans une fenêtre bornée. Exiger une haute disponibilité de la passerelle, avec un objectif chiffré, et un chemin de compensation de secours journalisé.
- **Confiance** : vérifié dans le texte (EXIG-AUT-11); déduit (scénario).

### [03-12] [MAJEUR] La règle d'or EXIG-AUT-07 reste dérogeable
- **Axe** : A
- **Localisation** : encadré « SANS DÉROGATION POSSIBLE », p. 30 : « ni pour le dépassement du plafond d'autonomie de la classe de risque (EXIG-GOV-17) ».
- **Diagnostic** : EXIG-AUT-07 (rayon élevé + réversibilité faible + détection lente ⇒ jamais au-delà de N2) n'est ni dans l'encadré ni dans EXIG-GOV-17. Un agent qui remplit ces critères n'est pas nécessairement de classe élevée : les critères du tableau 46 ne retiennent ni le rayon ni la détection. Son plafond de classe peut donc être N3, et le dépasser par dérogation n'est pas interdit. Pourtant, EXIG-GOV-17 justifie la liste par la protection « contre des dommages irréversibles », qui est précisément l'objet de la règle d'or.
- **Contre-exemple** : un agent interne de purge de données, sans RP ni effet financier, est de classe modérée (plafond N3). Il supprime 10 000 enregistrements par exécution, la réversibilité est faible et les écarts ne sont détectés qu'au mois suivant. Une dérogation de six mois l'autorise en N3, contre la règle d'or.
- **Correctif proposé** : ajouter EXIG-AUT-07 à EXIG-GOV-17 et à l'encadré, ou faire du cumul de ces critères un critère de la classe élevée au tableau 46.
- **Confiance** : vérifié dans le texte.

### [03-13] [MINEUR] La définition de P2 au § 3.1 est plus étroite que celle du tableau 31 et de N3
- **Axe** : C
- **Localisation** : p. 23 : « P2 écriture réversible ». À comparer avec N3, p. 22 (« actions P2 réversibles ou compensables ») et avec le tableau 31 (« Écriture réversible ou compensable, impact modéré »).
- **Diagnostic** : la définition qui « fait foi » (§ 3.1) omet « ou compensable » et « impact modéré ». N3 qualifie ensuite P2 de « réversibles ou compensables », ce qui laisse entendre qu'il existe des P2 qui ne le sont pas.
- **Contre-exemple** : un lecteur qui s'en tient au § 3.1 classe en P3 une réservation compensable.
- **Correctif proposé** : reprendre au § 3.1 le libellé du tableau 31, et supprimer le qualificatif redondant dans N3.
- **Confiance** : vérifié dans le texte.

### [03-14] [MINEUR] Les étiquettes « sur la boucle » et « hors de la boucle » sont contredites par l'approbation préalable d'une action P3
- **Axe** : C
- **Localisation** : N3, p. 22 : « une action P3 exige une approbation hors bande (humain sur la boucle) ». N4, p. 23 : « l'humain est hors de la boucle d'exécution […] une action P3 est toujours approuvée ». Définitions, p. 22 : HOTL « sans approbation préalable »; hors de la boucle : « aucune intervention pendant l'exécution ».
- **Diagnostic** : approuver une action P3 avant son exécution, c'est être dans la boucle (HITL) pour cette action. Les étiquettes contredisent les définitions qu'elles invoquent.
- **Contre-exemple** : un auditeur conclut qu'en N4 aucune personne ne doit intervenir pendant l'exécution, ce qui est incompatible avec EXIG-AUT-09.
- **Correctif proposé** : écrire « HOTL, sauf pour les actions P3, approuvées une à une (HITL) ».
- **Confiance** : vérifié dans le texte.

### [03-15] [MINEUR] La préséance (§ 4.3), le devoir de l'architecte (§ 4.2) et les « définitions normatives » sont hors du périmètre normatif du § 1.4
- **Axe** : C
- **Localisation** : § 4.3, p. 29 : « Choix du cadre : en cas de conflit, l'ordre de préséance suivant s'applique ». § 4.2, p. 29 : « l'architecte doit consigner dans la décision d'architecture le raisonnement ».
- **Diagnostic** : selon le § 1.4 (p. 13), seuls les blocs EXIG, les PRIN et les tableaux auxquels une exigence renvoie « créent une obligation normative ». L'ordre de préséance, le devoir de l'architecte et le tableau 7 (« Définitions normatives », « font foi », p. 20) ne sont repris dans aucun bloc EXIG trouvé. Ils sont donc informatifs, alors que le tableau 3 renvoie à la « section 4.3 » pour les points non dérogeables.
- **Contre-exemple** : en revue, une équipe refuse l'ordre de préséance comme texte informatif, et rien ne l'y oblige.
- **Correctif proposé** : élever la préséance et le devoir de l'architecte au rang d'EXIG-GOV, ou étendre la liste du § 1.4 au § 4.3 et au tableau 7.
- **Confiance** : vérifié dans le texte.

### [03-16] [MINEUR] Tableau 9 : la famille EXIG-EVA n'est rattachée à aucun principe, et PRIN-02 omet EXIG-EVT
- **Axe** : C
- **Localisation** : tableau 9, p. 28-29.
- **Diagnostic** : les 15 familles du tableau 4 n'apparaissent pas toutes. EXIG-EVA (6 exigences, § 10.4) est absente de la colonne « Exigences ». PRIN-02 vise explicitement le « contrat d'événement » (p. 25), mais ne cite ni le § 6.7 ni EXIG-EVT.
- **Contre-exemple** : une revue par principe, faite à partir du tableau 9, ne contrôle jamais l'évaluation continue.
- **Correctif proposé** : rattacher EXIG-EVA à PRIN-06 ou à PRIN-12 (preuve : jeu de référence, objectifs de niveau de service). Ajouter « 6.7, EXIG-EVT » à PRIN-02.
- **Confiance** : vérifié dans le texte.

### [03-17] [MINEUR] La liste non dérogeable de la p. 30 dérive d'EXIG-GOV-17
- **Axe** : C
- **Localisation** : p. 30 : « pour la mise en production d'un agent sans personne nommée qui en répond » et « l'exécution par un agent seul d'une action de palier P3 ».
- **Diagnostic** : EXIG-GOV-17 vise « l'exploitation d'un agent sans fiche au registre ni parrain nommé », ce qui est plus large dans le temps (après la mise en production) et ajoute la fiche, et « l'exécution d'une action P3 sans approbation humaine ». L'encadré omet aussi la condition d'EXIG-GOV-15 pour la délégation à l'architecture d'entreprise : la décision doit être prise par une personne autre que l'instructeur.
- **Contre-exemple** : un agent mis en production avec un parrain, puis laissé sans parrain après un départ, n'est pas couvert par l'encadré, mais l'est par EXIG-GOV-17.
- **Correctif proposé** : reprendre mot pour mot le libellé d'EXIG-GOV-17 dans l'encadré, ou n'y garder qu'un renvoi.
- **Confiance** : vérifié dans le texte.

### [03-18] [MINEUR] L'objet de la dérogation (principe ou exigence) et son effet sur un composant sont mal définis
- **Axe** : C
- **Localisation** : p. 30 : « Un écart à un principe doit faire l'objet d'une dérogation écrite » et « Une dérogation vise un agent ou un composant précis […] sinon l'écart est corrigé ou l'agent passe à l'état « suspendu » ».
- **Diagnostic** : EXIG-GOV-15 exige « l'identifiant de chaque exigence visée », et EXIG-GOV-16 dit qu'« à l'échéance, l'exigence s'applique de nouveau ». Un écart à un principe sans exigence correspondante n'a pas d'identifiant. Pour une dérogation qui vise un composant (un connecteur propriétaire, par exemple), le texte ne dit pas quel agent passe à « suspendu » : tous ceux qui l'utilisent?
- **Contre-exemple** : une dérogation à PRIN-01 pour un connecteur partagé par 12 agents arrive à échéance, et rien ne dit lesquels de ces agents sont suspendus.
- **Correctif proposé** : écrire « écart à un principe ou à une exigence DOIT » et prévoir l'identifiant PRIN-xx dans la demande. Préciser l'effet de l'échéance sur un composant : retrait du catalogue et suspension des agents qui en dépendent.
- **Confiance** : vérifié dans le texte.

### [03-19] [MINEUR] Tableau 10, ligne « PRIN-07 et utilité » : l'arbitrage ne couvre que la classe élevée et sort du mécanisme de préséance
- **Axe** : A
- **Localisation** : p. 29 : « La classe de risque tranche : pour la classe de risque élevé, on accepte la perte d'utilité. »
- **Diagnostic** : l'« utilité » n'est pas un principe, et la préséance du § 4.3 ne s'y applique donc pas. Le tableau ne dit rien des classes modérée et faible, alors qu'EXIG-SEC-07 n'impose un patron de conception qu'à la classe élevée. Accessoirement, « risque élevé » devrait être « risque élevée » ou « classe élevée », selon la notation du tableau 46.
- **Contre-exemple** : pour un agent de classe modérée exposé à du contenu non fiable, la défense par conception est-elle exigible? Aucune réponse.
- **Correctif proposé** : énoncer la règle pour les trois classes, ou renvoyer explicitement à EXIG-SEC-07.
- **Confiance** : vérifié dans le texte.

### [03-20] [MINEUR] Le tableau 8 laisse entendre qu'une approbation dans la session est valide, contrairement à EXIG-AUT-13
- **Axe** : C
- **Localisation** : tableau 8, p. 24, « Interaction humaine » de l'agent interactif : « Dans la session; une action P3 reste approuvée hors bande ».
- **Diagnostic** : par contraste, le texte suggère que les approbations P2 (en N2) se donnent « dans la session ». Or EXIG-AUT-13 exclut l'acquiescement dans la conversation et la « confirmation locale dans l'interface de l'agent ». Le même tableau désigne d'ailleurs ce risque comme dominant.
- **Contre-exemple** : une équipe implémente l'approbation P2 en N2 par un bouton « Oui » dans le clavardage de l'agent.
- **Correctif proposé** : écrire « Dans la session, par un jeton d'approbation signé émis hors de l'interface de l'agent (EXIG-AUT-12 et -13); P3 hors bande ».
- **Confiance** : vérifié dans le texte.

### [03-21] [MINEUR] Le mot « palier » désigne deux choses
- **Axe** : C
- **Localisation** : p. 22 : « Palier d'outil — Risque propre à un outil, de P0 à P3 ». Figure 3, p. 32 : « Évaluation continue (3 paliers) ».
- **Diagnostic** : le terme défini au § 3.1 est réemployé pour les paliers d'évaluation 1 à 3 (EXIG-EVA-01 : « franchir les paliers 1 et 2 »). Le risque de confusion est réel, puisque les deux échelles ont des numéros voisins.
- **Contre-exemple** : « palier 2 » peut se lire comme P2 (écriture réversible) ou comme le palier d'évaluation 2.
- **Correctif proposé** : renommer les paliers d'évaluation (« étapes » ou « niveaux d'évaluation E1-E3 »).
- **Confiance** : vérifié dans le texte.

### [03-22] [MINEUR] PRIN-04 dit le niveau « fixé par la classe », ce qui contredit EXIG-AUT-01 et -02
- **Axe** : C
- **Localisation** : PRIN-04, p. 26 : « un plafond déclaré au registre et fixé par la classe de risque de l'agent ».
- **Diagnostic** : la classe fixe le plafond du plafond. Le niveau déclaré est « le plus bas qui permet d'atteindre l'objectif » (EXIG-AUT-01), et il est évalué selon les critères du tableau 30 et d'EXIG-AUT-07 (EXIG-AUT-02), pas seulement selon la classe.
- **Contre-exemple** : lu à la lettre, un agent de classe modérée est N3, même si N1 suffit.
- **Correctif proposé** : écrire « borné par le plafond de la classe de risque et par les critères du tableau 30 ».
- **Confiance** : vérifié dans le texte.

### [03-23] [MINEUR] CaMeL : les chiffres 77 % et 84 % sont datés de « mars 2025 » sans version épinglée
- **Axe** : B
- **Localisation** : tableau 10, p. 29 : « CaMeL (Debenedetti et coll., mars 2025) accomplit 77 % des tâches avec une sécurité démontrable, contre 84 % ». Référence [101] : arXiv:2503.18813, sans version.
- **Diagnostic** : de mémoire, la v1 de mars 2025 annonçait 67 %, et 77 % provient d'une révision ultérieure. Je ne l'ai pas vérifié. La date ne correspondrait alors pas au chiffre. Par ailleurs, la « sécurité démontrable » porte sur les flux de données et de contrôle, pas sur les canaux latéraux, que les auteurs excluent.
- **Contre-exemple** : un lecteur qui ouvre la v1 trouve 67 %.
- **Correctif proposé** : épingler la version arXiv (vN, date) et nuancer la portée de la preuve.
- **Confiance** : à vérifier (source externe).

### [03-24] [MINEUR] Le résumé des résultats de ReAct est sélectif
- **Axe** : B
- **Localisation** : § 3.2, p. 23 : « ce qui a réduit les hallucinations par rapport à la chaîne de pensée seule et amélioré le taux de réussite sur les tâches interactives ».
- **Diagnostic** : de mémoire, sur HotpotQA, ReAct seul était moins exact que la chaîne de pensée. La réduction des hallucinations ressort de l'analyse des échecs, et le meilleur résultat venait de la combinaison ReAct + CoT-SC. L'énoncé suggère une supériorité générale.
- **Contre-exemple** : sans objet (fait externe).
- **Correctif proposé** : ajouter « au prix d'une exactitude parfois moindre sur les tâches de connaissance (HotpotQA) ».
- **Confiance** : à vérifier (source externe : Yao et al. 2023, tableaux 1 et 2).

### [03-25] [MINEUR] « Chaque instance la sienne au besoin » n'est pas vérifiable
- **Axe** : B
- **Localisation** : § 3.4, p. 24 : « Chaque agent a sa propre identité, et chaque instance la sienne au besoin[92]. »
- **Diagnostic** : « au besoin » ne précise pas le critère (instances concurrentes, mandants distincts, révocation séparée). La règle n'est donc pas vérifiable en revue.
- **Contre-exemple** : 50 réplicas d'un agent partagent une identité, puis l'une d'elles est compromise et ne peut pas être révoquée seule.
- **Correctif proposé** : fixer le critère (par exemple : identité d'instance obligatoire dès que des instances servent des mandants différents ou doivent être révocables séparément) et renvoyer à l'EXIG-IAM correspondante.
- **Confiance** : vérifié dans le texte.

### [03-26] [MINEUR] Le texte de loi (RIA, art. 26) est cité par une source secondaire, et l'applicabilité n'est pas précisée
- **Axe** : C
- **Localisation** : § 3.4, p. 24 : « le RIA oblige le déployeur d'un système à haut risque à confier la supervision humaine à des personnes compétentes[94] ».
- **Diagnostic** : [94] est le site du Future of Life Institute, alors que le règlement lui-même est disponible ([61]). Le présent « oblige » omet que, selon le cadre lui-même, les obligations de l'annexe III s'appliquent au 2 décembre 2027 (règlement (UE) 2026/1744).
- **Contre-exemple** : sans objet.
- **Correctif proposé** : citer l'art. 26(2) d'après [61] et ajouter « à compter de la date d'application des obligations relatives aux systèmes à haut risque (section 12.4) ».
- **Confiance** : vérifié dans le texte (références); à vérifier (dates d'application).

### [03-27] [MINEUR] Tableau 10, PRIN-06 et RP : « exclu par défaut » sous-énonce EXIG-OBS-07
- **Axe** : C
- **Localisation** : p. 29 : « le contenu est exclu par défaut, activé sur décision documentée et conservé hors des traces ».
- **Diagnostic** : EXIG-OBS-07 n'établit pas une valeur par défaut. C'est une interdiction en production (« NE DOIVENT PAS contenir »), et la capture ponctuelle relève d'EXIG-OBS-08, hors trace. « Par défaut » et « activé » laissent croire que le contenu pourrait être activé dans les traces.
- **Contre-exemple** : une équipe active la capture de contenu de la convention GenAI dans les spans de production « sur décision documentée ».
- **Correctif proposé** : écrire « le contenu est interdit dans la télémétrie de production (EXIG-OBS-07); une capture de diagnostic, bornée et documentée, est stockée hors des traces (EXIG-OBS-08) ».
- **Confiance** : vérifié dans le texte.

### [03-28] [MINEUR] Deux listes de principes protecteurs presque identiques
- **Axe** : C
- **Localisation** : p. 25 : « (PRIN-03 à PRIN-06, PRIN-10 et PRIN-12) ». § 4.3, p. 29 : « PRIN-03 à PRIN-07, PRIN-10 et PRIN-12 ».
- **Diagnostic** : les deux listes ne diffèrent que par PRIN-07. L'écart est sans doute voulu (les trois questions ne portent pas sur l'injection), mais rien ne l'explique, et le lecteur peut croire à une coquille.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : aligner les deux listes, ou dire pourquoi PRIN-07 est exclu des trois questions.
- **Confiance** : vérifié dans le texte.

## Points forts
- Les quatre axes (classe, niveau, palier, topologie) sont nettement distingués, et le texte sépare partout le choix du cadre de l'exigence externe.
- L'exécution durable est explicitement distinguée de l'idempotence (p. 22), et les garde-fous probabilistes ne sont jamais présentés comme suffisants.
- Le tableau 10 expose de vraies tensions avec un arbitrage chiffré et sourcé, au lieu de prétendre que les principes ne se contredisent jamais.

## Questions pour l'audit bibliographique
- p. 23, [83] : le « certificat d'autonomie » figure-t-il bien dans Feng, McDonald et Zhang, arXiv:2506.12469 v2?
- p. 23, [84] : ReAct : réduction des hallucinations par rapport à CoT et exactitude sur HotpotQA (voir 03-24).
- p. 24, [88, 89] : au 27 octobre 2026, le rabais par lots est-il de 50 % avec une fenêtre de 24 h, chez Anthropic comme chez OpenAI?
- p. 24, [87] : T10 correspond-elle à « Overwhelming Human in the Loop » dans la v1.1 des Threats and Mitigations de l'OWASP?
- p. 24, [91] : NHI9 (réutilisation) et NHI10 (usage humain d'une NHI) dans l'OWASP NHI Top 10 2025.
- p. 24, [93] : draft-ietf-wimse-aims-00 est-il adopté par le groupe de travail WIMSE? Le titre est-il bien « AI Identity Management System »? Le brouillon qualifie-t-il les clés d'API statiques d'antipatron?
- p. 24-25, [90, 92] : Microsoft déconseille-t-il les principaux de service traditionnels pour les agents? Entra Agent ID distingue-t-il « sponsor » et « owner »?
- p. 24, [94] : texte de l'art. 26(2) du RIA, et date d'application aux systèmes de l'annexe III.
- p. 25, [4, 35] : AAIF a-t-elle accueilli MCP en décembre 2025 et A2A le 17 août 2026? A2A était sous gouvernance neutre de la Linux Foundation dès juin 2025.
- p. 26, [95] : communiqué Gartner du 26 mai 2026 sur la « confusion » entre capacité d'agir et portée des accès.
- p. 27, [97, 98] : NIST AI 100-2 E2025 (concevoir dans l'hypothèse d'une injection) et billet du NCSC (pas de séparation intrinsèque entre données et instructions).
- p. 28, [99] : libellé de GOVERN 3.2 du NIST AI RMF.
- p. 28, [76] : les quatre dimensions du cadre agentique de l'IMDA, et son § 1.1.3 (p. 22).
- p. 28, [100] : CoALA juge-t-elle l'écriture en mémoire procédurale plus risquée?
- p. 29, [101] : version arXiv de CaMeL qui donne 77 % et 84 % (voir 03-23).
