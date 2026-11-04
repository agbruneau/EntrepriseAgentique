# Audit chunk_05 — pages 41-52

## Synthèse
Couvre la fin du § 5.5 (mémoire : figure 4, tableau 13, EXIG-ARC-22 à 25), le parcours de bout en bout (§ 5.6), le § 6.1 (EIF, tableau 14, EXIG-INT-01 à 03), le § 6.2 (carte, EXIG-INT-04 et 05) et le § 6.3 (catalogue, tableau 15, EXIG-INT-06 à 09). La documentation des sources et des statuts est soignée, mais les règles du catalogue se contredisent entre elles.
Les trois défauts les plus graves :
(1) EXIG-INT-06 interdit en production l'existant que le statut Contenir tolère;
(2) EXIG-INT-04 (DOIT A2A) contredit EXIG-INT-05 (DEVRAIT, avec exception intradomaine), et le critère outil/agent ne permet pas de trancher;
(3) l'affirmation « les trois passent par la passerelle » ne vaut pas pour les événements, qui échappent à EXIG-ARC-01 et à EXIG-SEC-06.

## Constats

### [05-01] [MAJEUR] EXIG-INT-06 interdit en production ce que le statut Contenir tolère
- **Axe** : A
- **Localisation** : § 6.3, p. 49 et p. 51. Définition p. 49 : « Contenir existant toléré derrière un adaptateur, sans nouvel usage, avec un plan de sortie daté ». EXIG-INT-06, p. 51 : « DOIT figurer au catalogue avec le statut Adopter pour être employé en production ».
- **Diagnostic** : la condition d'usage en production d'EXIG-INT-06 est le statut Adopter, et cette condition est nécessaire. Un élément au statut Contenir n'est donc, par définition, pas Adopter. Or le statut Contenir existe pour tolérer un usage *existant*, donc en production. Tableau 15, p. 51, ligne « Formats propres à un fournisseur » : « Tolérés derrière un adaptateur ». EXIG-GOV-18 (§ 11.7) et le texte voisin le redisent : « "Contenir" tolère l'existant ». La phrase finale d'EXIG-INT-06 (« le statut Contenir interdit tout nouvel usage ») ne lève pas la contradiction, puisque la première phrase interdit déjà tout usage.
- **Contre-exemple** : un connecteur propriétaire en production, classé Contenir avec un plan de sortie à 12 mois. Une lecture littérale d'EXIG-INT-06 impose de le couper sur-le-champ. Une lecture de l'intention le maintient. L'auditeur ne peut pas trancher.
- **Correctif proposé** : « … DOIT figurer au catalogue avec le statut Adopter pour tout nouvel usage en production; un usage existant au statut Contenir reste permis jusqu'à l'échéance de son plan de sortie ».
- **Confiance** : vérifié dans le texte.

### [05-02] [MAJEUR] Force contradictoire entre EXIG-INT-04 et EXIG-INT-05 pour la délégation à un agent
- **Axe** : A / C
- **Localisation** : § 6.2, p. 49. EXIG-INT-04 · DOIT : « A2A pour la délégation à un autre agent ». EXIG-INT-05 · DEVRAIT : « L'enveloppe "agent comme outil" reste permise à l'intérieur d'un même agent ou d'un même domaine de confiance ».
- **Diagnostic** : EXIG-INT-04 rend A2A obligatoire pour toute délégation à un autre agent, sans exception. Tout autre protocole relève d'une dérogation (section 11.6). EXIG-INT-05 traite le même cas comme une recommandation (DEVRAIT) et ouvre une exception intradomaine qu'EXIG-INT-04 ne connaît pas. Selon § 1.4, une exigence DOIT l'emporte sur une DEVRAIT, si bien que l'exception d'EXIG-INT-05 est nulle. À l'inverse, si l'exception est voulue, EXIG-INT-04 est trop forte.
- **Contre-exemple** : dans le domaine facturation, un agent de rapprochement est exposé en outil MCP à l'orchestrateur du même domaine. Ce montage est conforme à EXIG-INT-05 et non conforme à EXIG-INT-04, qui exigerait une dérogation.
- **Correctif proposé** : ajouter à EXIG-INT-04 « sous réserve de l'EXIG-INT-05 » ou, mieux, déplacer l'exception intradomaine dans EXIG-INT-04 elle-même. Préciser aussi ce qu'est un « domaine de confiance » (terme non défini ici, distinct du « domaine métier » d'EXIG-INT-03).
- **Confiance** : vérifié dans le texte.

### [05-03] [MAJEUR] Critère outil/agent indécidable : conjonction contre disjonction, et MCP remplit les critères « agent »
- **Axe** : A
- **Localisation** : § 6.2, p. 48 : « Si elle planifie, conserve un état et peut renvoyer une question, c'est un agent ». EXIG-INT-05, p. 49 : « qui planifie, conserve un état ou peut demander une précision ».
- **Diagnostic** : la règle de départage pose une conjonction (« et »), alors que l'exigence pose une disjonction (« ou »). Deux critères ne discriminent pas, de plus. Un serveur MCP peut poser une question par élicitation (§ 6.5, p. 55 et suivantes : « L'élicitation reste le canal par lequel un serveur sollicite une personne »). L'extension Tasks lui donne aussi un état durable à états `input_required` (§ 6.5). Selon EXIG-INT-05, tout outil MCP qui emploie l'élicitation ou Tasks devient ainsi un « agent » à invoquer par A2A. La règle du « modèle employé en interne » n'aide pas, puisqu'elle ne vise que les entrées et sorties.
- **Contre-exemple** : un outil MCP `ouvrir_reclamation` est sans planification. Il conserve un état (tâche Tasks) et demande une précision (élicitation). La règle de la p. 48 le classe outil. EXIG-INT-05 le classe agent. Les deux protocoles imposent des contrôles différents (cycle de vie A2A, carte signée), et le choix change l'homologation.
- **Correctif proposé** : retenir un critère unique et opératoire. Par exemple : « est un agent toute cible qui choisit elle-même la suite de ses actions (planification autonome); l'état et les demandes de précision par élicitation ou Tasks ne suffisent pas ». Aligner ensuite le texte de la p. 48 et EXIG-INT-05.
- **Confiance** : vérifié dans le texte (élicitation et Tasks décrites au § 6.5 du même document).

### [05-04] [MAJEUR] Les événements ne passent pas par la passerelle d'agents, contrairement à ce que l'encadré affirme
- **Axe** : A / B (thèse T2)
- **Localisation** : § 6.2, p. 49, À RETENIR : « Les trois passent par la passerelle d'agents et par le catalogue d'entreprise ». Également p. 48-49 : « l'échange qui sort d'un domaine passe par la passerelle d'agents ».
- **Diagnostic** : EXIG-ARC-01 (§ 5.2) ne vise que les appels vers un outil, une ressource ou une invite MCP, vers une donnée d'un autre domaine ou vers un autre agent. La publication sur le bus n'y figure pas. Dans le texte complet, le § 6.7 (EXIG-EVT-01 à 05) ne fait jamais transiter un événement par la passerelle. Le catalogue (EXIG-EVT-03) et le consommateur (EXIG-EVT-04) portent seuls les contrôles. L'encadré énonce donc une propriété que les exigences ne garantissent pas. Conséquence de sécurité : EXIG-SEC-06 retire « les outils d'envoi vers l'extérieur » par la passerelle après la lecture d'un contenu non fiable. Un producteur Kafka hors passerelle reste alors un canal d'exfiltration que ce retrait ne couvre pas (thèse T4).
- **Contre-exemple** : un agent lit un courriel piégé. La passerelle lui retire l'envoi de courriel. L'agent publie pourtant un CloudEvent sur un sujet consommé par un connecteur sortant vers un partenaire, et l'exfiltration aboutit hors du point d'application des politiques.
- **Correctif proposé** : soit étendre EXIG-ARC-01 aux publications et abonnements d'agents, par un proxy d'événements ou des ACL de courtier pilotées par la même politique, et soumettre la publication au retrait d'EXIG-SEC-06; soit corriger l'encadré : « MCP et A2A passent par la passerelle; l'événement passe par le catalogue et les ACL du courtier ».
- **Confiance** : vérifié dans le texte (aucune mention de la passerelle dans le § 6.7 au sujet de la publication); le scénario d'exfiltration est déduit.

### [05-05] [MAJEUR] Parcours § 5.6 : un seul jeton délégué, « restreint » par la passerelle, contredit le modèle de délégation du chapitre 9
- **Axe** : A / C (thèse T6)
- **Localisation** : § 5.6, p. 44. Étape 3 : « obtient un jeton délégué au nom de la conseillère ». Étape 5 : « la passerelle d'agents, qui vérifie le catalogue, restreint le jeton à l'audience du serveur MCP (paramètre resource, RFC 8707) ».
- **Diagnostic** : la RFC 8707 est un paramètre que le *client* envoie au serveur d'autorisation. Une passerelle ne peut pas « restreindre » l'audience d'un jeton déjà émis. Elle ne peut que le vérifier, ou en obtenir un autre par échange (RFC 8693). Le chapitre 9 le dit lui-même. EXIG-IAM-10 et 11 placent l'intersection et l'audience unique au serveur d'autorisation, « à chaque échange ». La figure 17 dit « jeton délégué à audience unique […] que la passerelle vérifie ». Le parcours suppose de plus un seul jeton obtenu à l'ouverture, alors qu'il vise au moins trois audiences distinctes : le serveur de consultation, le serveur de facturation et l'agent de conformité par A2A. Si la passerelle relayait le jeton reçu, ce serait du token passthrough, que MCP interdit (§ 6.5).
- **Contre-exemple** : un lecteur qui implante le parcours tel qu'écrit obtient à l'étape 3 un jeton à audience « passerelle » ou multi-audience, puis le fait suivre aux serveurs MCP. Il crée exactement le confused deputy que l'EXIG-IAM-11 veut empêcher.
- **Correctif proposé** : à l'étape 3, écrire « obtient le jeton de la conseillère »; aux étapes 5, 6 et 8, écrire « l'orchestrateur (ou la passerelle agissant comme client) obtient par échange de jetons (RFC 8693, paramètre resource RFC 8707) un jeton à audience unique pour ce serveur, que la passerelle vérifie ».
- **Confiance** : vérifié dans le texte (contradiction avec les § 9.3 et 9.4); l'exactitude de la RFC 8707 relève de mes connaissances, avec un degré de certitude élevé.

### [05-06] [MAJEUR] Parcours § 5.6 : suspension pour approbation, durée de vie des jetons et droits du mandant non traités
- **Axe** : A / B (thèse T5)
- **Localisation** : § 5.6, p. 44. Étape 7 : « le moteur suspend la tâche, état persisté, et présente l'action exacte à une approbatrice ». Étape 8 : « Le moteur reprend la tâche. L'appel passe par la passerelle avec le jeton d'approbation ».
- **Diagnostic** : deux postulats restent implicites.
  - Le jeton délégué de l'étape 3 vit 15 minutes ou moins (§ 9.3 : « DEVRAIT expirer en 15 minutes ou moins »). Une attente d'approbation de plusieurs heures l'aura périmé. Le parcours ne dit pas qu'un nouvel échange a lieu à la reprise, ni que les droits de la conseillère sont revérifiés : révocation ou départ entre l'étape 1 et l'étape 8 (TOCTOU sur le mandant).
  - L'approbation (8.5 : `{ h, approbateur, tâche, exp }`) n'ajoute aucun droit, car les droits effectifs sont une intersection (EXIG-IAM-10). L'écriture de 1 200 $ suppose donc que la conseillère détient elle-même le droit d'émettre un avoir de ce montant. Si son plafond métier est de 500 $, comme le seuil le laisse penser, l'ERP refuse après l'approbation, ou alors l'approbation sert de contournement.
- **Contre-exemple** : l'approbatrice approuve à 16 h 50 une demande déposée à 9 h. Le moteur reprend la tâche avec le jeton de 9 h, expiré, et l'appel échoue. Une implantation « robuste » conserverait alors un jeton de longue durée, ce qui contredit le chapitre 9.
- **Correctif proposé** : ajouter à l'étape 8 « à la reprise, le moteur obtient un nouveau jeton délégué par échange, ce qui revérifie les droits actuels du mandant ». Préciser à l'étape 7 que l'approbation est une séparation des tâches et non une élévation de droits. Indiquer enfin que la conseillère détient le droit d'émettre l'avoir, ou que l'écriture se fait au nom de l'approbatrice.
- **Confiance** : déduit (des § 8.5 et 9.3 lus dans full.txt).

### [05-07] [MAJEUR] EXIG-ARC-23 inapplicable à la mémoire sémantique : isolation par mandant et date d'expiration
- **Axe** : A
- **Localisation** : EXIG-ARC-23, p. 43 : « Toute écriture en mémoire épisodique ou sémantique DOIT […] l'isolent par locataire, par mandant et par serveur MCP, lui fixent une date d'expiration ». Tableau 13, p. 42, ligne Sémantique : « Tant que la source est valide », « Mise à jour par les propriétaires des données; filtrage selon le mandant ». Figure 4 : « isolation par locataire et par serveur MCP ».
- **Diagnostic** : la mémoire sémantique contient de la connaissance de domaine partagée : index vectoriels et lexicaux, graphes, documentation. Le tableau 13 la protège par un *filtrage en lecture* selon le mandant (EXIG-ARC-16), non par une isolation des écritures. Il lui donne une durée de vie liée à la validité de la source, non une date fixe. Appliquée à la lettre, EXIG-ARC-23 cloisonne chaque document par employé et lui attribue une échéance arbitraire. Les trois vues se contredisent aussi sur l'isolation par mandant, absente de la figure 4 et présente dans EXIG-ARC-23.
- **Contre-exemple** : la politique de remboursement indexée par le propriétaire des données ne peut pas être « isolée par mandant » sans être dupliquée pour chaque conseillère. Elle ne peut pas non plus recevoir une date d'expiration sans qu'on l'invente.
- **Correctif proposé** : scinder EXIG-ARC-23. Pour l'épisodique : isolation par locataire, mandant et serveur, expiration par entrée (EXIG-CON-10). Pour le sémantique : isolation par locataire et par serveur, filtrage en lecture selon le mandant, expiration liée à la validité de la source. Aligner ensuite la figure 4 et le tableau 13.
- **Confiance** : vérifié dans le texte (la contradiction est démontrée; la gravité est déduite).

### [05-08] [MAJEUR] EXIG-INT-07 bloque l'inscription des serveurs MCP antérieurs que l'EXIG-MCP-22 tolère
- **Axe** : A / C
- **Localisation** : EXIG-INT-07, p. 51 : « une déclaration incompatible avec le catalogue DOIT bloquer l'inscription au registre ». Tableau 15, p. 49, ligne MCP : « révision 2026-07-28 » (aucune coexistence mentionnée). La ligne A2A, p. 50, prévoit en revanche : « interfaces 0.3 seulement en coexistence bornée ».
- **Diagnostic** : EXIG-MCP-22 (§ 6.5) exige que la passerelle accepte « les deux générations de MCP pendant une période de coexistence bornée », jusqu'au 28 juillet 2027, chaque serveur antérieur étant « inscrit au catalogue avec sa date de migration ». Le tableau 15 ne fixe pour MCP que 2026-07-28, et EXIG-INT-07 ne définit pas « incompatible ». Un serveur qui déclare seulement 2025-11-25 est donc incompatible avec le catalogue et bloqué, contrairement à EXIG-MCP-22. L'asymétrie avec la ligne A2A montre un oubli plutôt qu'un choix.
- **Contre-exemple** : au 1er novembre 2026, un serveur MCP de fournisseur encore en 2025-11-25 ne peut pas être inscrit selon EXIG-INT-07. Il doit pourtant l'être selon EXIG-MCP-22.
- **Correctif proposé** : ajouter à la ligne MCP « révisions antérieures (2025-11-25) en coexistence bornée jusqu'au 28 juillet 2027 (EXIG-MCP-22) ». Définir dans EXIG-INT-07 une déclaration compatible : elle inclut la version de référence, ou une version en coexistence assortie d'une date de migration.
- **Confiance** : vérifié dans le texte.

### [05-09] [MAJEUR] EXIG-INT-02 : des schémas « gérés au niveau de l'entreprise » pour des outils de tiers qu'elle ne contrôle pas
- **Axe** : B
- **Localisation** : EXIG-INT-02, p. 47 : « Les données échangées […] entre agents et outils […] DOIVENT être décrites par des schémas JSON Schema 2020-12 versionnés […] Ces schémas DOIVENT être gérés au niveau de l'entreprise, et non par chaque équipe d'agent ».
- **Diagnostic** : le `inputSchema` et l'`outputSchema` d'un serveur MCP de tiers appartiennent à son éditeur : serveur Action Fabric de ServiceNow, plateformes SaaS du tableau 12, p. 41. Il en va de même de la carte d'un agent A2A de partenaire. L'entreprise peut les *inscrire* et les *épingler*, mais non les « gérer » ni les fonder sur son vocabulaire métier. L'exigence est inapplicable à tout le segment SaaS que le cadre recommande pourtant (tableau 12, couches 1 à 3), et il n'est pas possible d'en vérifier le respect en revue.
- **Contre-exemple** : Salesforce Agentforce expose ses outils MCP avec ses propres schémas. Aucune équipe de l'entreprise ne peut les rendre conformes au vocabulaire d'entreprise. L'intégration devient non conforme par construction, ou il faut un adaptateur pour chaque outil.
- **Correctif proposé** : limiter l'obligation aux schémas *produits* par l'entreprise, et exiger pour les schémas de tiers une inscription épinglée (empreinte), plus une correspondance vers le vocabulaire d'entreprise tenue à l'adaptateur ou à la passerelle.
- **Confiance** : déduit.

### [05-10] [MINEUR] AsyncAPI 3.x et JSON Schema 2020-12 : prise en charge de schemaFormat douteuse
- **Axe** : A / B
- **Localisation** : EXIG-INT-02, p. 47 : « dans AsyncAPI 3.x, en déclarant explicitement schemaFormat à JSON Schema 2020-12, le format par défaut étant le Schema Object d'AsyncAPI ».
- **Diagnostic** : de mémoire, le Schema Object d'AsyncAPI 3.0 est un sur-ensemble de JSON Schema *draft-07*. La spécification n'impose aux outils de reconnaître que ce format et JSON Schema draft-07. Les autres valeurs de `schemaFormat` sont facultatives. Si c'est exact, rendre 2020-12 obligatoire sur le bus fait dépendre la validation d'outils qui peuvent l'ignorer, ou la refuser en silence.
- **Contre-exemple** : un générateur ou validateur AsyncAPI ne reconnaît pas `application/schema+json;version=2020-12`, et la validation des événements n'a jamais lieu.
- **Correctif proposé** : vérifier la liste des formats obligatoires d'AsyncAPI 3.1. Si 2020-12 n'en fait pas partie, exiger un test de conformité de la chaîne d'outils (validateur du courtier, générateurs) ou tolérer draft-07 sur le bus.
- **Confiance** : à vérifier (spécification AsyncAPI 3.x, section Multi Format Schema Object).

### [05-11] [MINEUR] Versions « fixées » qui ne le sont pas, malgré EXIG-INT-07
- **Axe** : C
- **Localisation** : tableau 15, p. 50 : « OpenAPI 3.1.x ou 3.2.x », « AsyncAPI 3.x », « version épinglée (v1.41.0 ou première version étiquetée du dépôt semantic-conventions-genai) ». Figure 6, p. 48 : « OpenAPI 3.1 ». EXIG-INT-07, p. 51 : « Le catalogue DOIT fixer, pour chaque standard adopté, la version de référence (… d'AsyncAPI) ».
- **Diagnostic** : « 3.x » et « 3.1.x ou 3.2.x » ne fixent rien. « v1.41.0 ou première version étiquetée » est une disjonction, donc pas un épinglage. EXIG-OBS-01 (§ 10.1) dit pour sa part « v1.41.0, jusqu'à l'homologation d'une version étiquetée », une condition que le tableau 15 omet. Le § 10.1 signale en outre le correctif v1.41.1 (11 mai 2026), dont le tableau 15 ne dit rien. La figure 6 réduit OpenAPI à 3.1.
- **Contre-exemple** : un contrat AsyncAPI 3.1 et un consommateur 3.0 sont tous deux « conformes au catalogue ». Une équipe qui émet les conventions du dépôt genai étiquetées v0.1 se dit conforme, sans homologation.
- **Correctif proposé** : fixer AsyncAPI 3.1.0 (ou 3.0.0) et une version d'OpenAPI de référence (les autres étant tolérées). Reprendre au tableau 15 la formule d'EXIG-OBS-01. Statuer sur v1.41.0 ou v1.41.1. Corriger la figure 6.
- **Confiance** : vérifié dans le texte.

### [05-12] [MINEUR] Le catalogue ne respecte pas sa propre EXIG-INT-09
- **Axe** : C
- **Localisation** : EXIG-INT-09, p. 52 : « Le catalogue indique le statut exact de chaque élément : norme, recommandation, brouillon de groupe de travail, brouillon individuel, préversion ou projet hébergé ». Tableau 15, p. 49-51. Figures 5 et 6 : « OAuth 2.x ».
- **Diagnostic** : le tableau 15 n'a pas de colonne de statut normatif. Ce statut n'apparaît que pour certaines lignes : OAuth 2.1 (Internet-Draft), ID-JAG (brouillon de groupe de travail), W3C Trace Context (Recommandation). Il manque pour MCP, A2A, AsyncAPI, OpenAPI, AG-UI et Transaction Tokens (le nom du brouillon seulement). La ligne CloudEvents adopte les « extensions de gouvernance et compteur de sauts » au statut Adopter. L'encadré de la même page précise pourtant que ces extensions « n'ont aucun statut officiel ». Le lecteur du tableau ne le voit pas, alors qu'EXIG-INT-06 vise aussi les extensions. « OAuth 2.x » dans les figures 5 et 6 confond la norme et le brouillon, ce qu'EXIG-INT-09 proscrit.
- **Contre-exemple** : un acheteur qui reprend la ligne CloudEvents dans un contrat présente comme adoptée une extension sans statut, soit le cas visé par EXIG-INT-09.
- **Correctif proposé** : ajouter au tableau 15 une colonne « Statut normatif ». Mentionner dans la ligne CloudEvents « extensions documentées, sans statut officiel ». Remplacer « OAuth 2.x » par « OAuth 2.0 (RFC 9700), profil OAuth 2.1 (brouillon) ».
- **Confiance** : vérifié dans le texte.

### [05-13] [MINEUR] Figure 6 : « À surveiller (pilotes seulement) » contredit la définition du statut Surveiller
- **Axe** : C
- **Localisation** : figure 6, p. 48 : « À surveiller (pilotes seulement) Protocoles de commerce et de paiement agentiques; formats propriétaires contenus derrière un adaptateur ».
- **Diagnostic** : le statut Surveiller signifie « veille et essais hors production, sans données réelles » (p. 49). Les pilotes relèvent d'Évaluer, et le § 11.7 précise : « NE DOIT PAS être utilisé, même en pilote avec des données réelles ». Les formats propriétaires sont au statut Contenir, non Surveiller (tableau 15, p. 51).
- **Contre-exemple** : sur la foi de la figure, une équipe lance un pilote ACP avec des données réelles, ce que le tableau 15 et le § 11.7 interdisent.
- **Correctif proposé** : bandeau « En veille (hors production) : commerce et paiements agentiques », et bandeau distinct « Contenus : formats propriétaires derrière un adaptateur ».
- **Confiance** : vérifié dans le texte.

### [05-14] [MINEUR] Figure 4 : « les mêmes contrôles d'écriture » pour les trois mémoires longues, alors que la procédurale suit un autre régime
- **Axe** : C
- **Localisation** : légende de la figure 4, p. 42 : « les trois mémoires longues sont persistées hors du modèle, récupérées au besoin et protégées par les mêmes contrôles d'écriture ». EXIG-ARC-23, p. 43 : « en mémoire épisodique ou sémantique ». EXIG-ARC-24 : processus de changement logiciel pour la procédurale.
- **Diagnostic** : la légende applique à la mémoire procédurale les contrôles d'EXIG-ARC-23. Les exigences la placent pourtant sous un régime distinct : revue, version, registre, aucun droit d'écriture de l'agent. Lecture contradictoire entre la figure et le texte normatif.
- **Contre-exemple** : sans objet, il s'agit d'une incohérence rédactionnelle.
- **Correctif proposé** : « les mémoires épisodique et sémantique passent par les contrôles d'écriture; la mémoire procédurale, par le processus de changement logiciel ».
- **Confiance** : vérifié dans le texte.

### [05-15] [MINEUR] EXIG-ARC-22 : borne renvoyée à un champ de fiche absent, interdiction « en entier » non testable
- **Axe** : A / B
- **Localisation** : EXIG-ARC-22, p. 43 : « NE DOIT PAS être réinjecté en entier dans le contexte du modèle […] dans la limite d'une fenêtre de contexte bornée à la fiche de l'agent ».
- **Diagnostic** : la phrase mêle la consolidation persistée et la borne du contexte. Je n'ai trouvé aucun champ « borne de contexte » dans l'annexe B. La grille B ne mentionne que « aucun historique brut comme mémoire ». Dans une conversation de trois tours, l'historique entier *est* l'ensemble des « derniers échanges » que le tableau 13 place légitimement en mémoire de travail. L'interdiction n'a pas de seuil et ne peut donc pas être testée.
- **Contre-exemple** : un agent conversationnel réinjecte ses quatre derniers tours, soit tout l'historique. L'auditeur ne peut pas dire s'il viole EXIG-ARC-22.
- **Correctif proposé** : « au-delà de la borne de contexte déclarée dans la fiche d'agent (champ à ajouter à l'annexe B, en jetons), l'historique DOIT être compacté ou consolidé ».
- **Confiance** : déduit (recherche de « fenêtre de contexte » dans full.txt : deux occurrences seulement, aucune en annexe B).

### [05-16] [MINEUR] « Valident sa source » : critère non défini pour les résumés épisodiques produits par le modèle
- **Axe** : B (thèse T4)
- **Localisation** : EXIG-ARC-23, p. 43 : « valident sa source ». § 5.6, étape 10, p. 45 : « un résumé validé de la résolution entre en mémoire épisodique ».
- **Diagnostic** : pour une entrée épisodique, la « source » est la trajectoire de l'agent. Selon EXIG-SEC-03, cette trajectoire contient des réponses d'outils non fiables. Le texte ne dit ni qui valide ni selon quel critère : humain, règle, second modèle. Le § 5.5 ne renvoie pas non plus à EXIG-SEC-03, qui traite les entrées de mémoire comme du contenu non fiable à la relecture. Ce renvoi est pourtant le contrôle qui ferme le chemin de persistance de l'injection.
- **Contre-exemple** : un champ libre de l'ERP contient une instruction piégée, que le résumé « validé » recopie. À la session suivante, seul le marquage d'EXIG-SEC-03 empêche son effet, et le § 5.5 ne le mentionne pas.
- **Correctif proposé** : définir la validation (schéma du résumé, liste des champs admis, exclusion du texte libre provenant d'outils) et ajouter au § 5.5 « toute entrée de mémoire relue est un contenu non fiable (EXIG-SEC-03) ».
- **Confiance** : vérifié dans le texte (absence de définition et de renvoi); le scénario est déduit.

### [05-17] [MINEUR] Écriture en arrière-plan : contexte du mandant et rétention des transcriptions intermédiaires non traités
- **Axe** : B
- **Localisation** : p. 42-43 : « ou en arrière-plan (sans latence, mais avec une fréquence à choisir) […] Le cadre accepte les deux modes, à condition qu'ils passent par les mêmes contrôles ».
- **Diagnostic** : une consolidation différée doit connaître le mandant pour isoler l'entrée (EXIG-ARC-23), alors que la session et son jeton délégué ont pris fin. Elle exige aussi de conserver la matière brute jusqu'au traitement. La durée et le statut de ce tampon ne sont pas encadrés, ce qui frôle l'anti-patron « Archiver les transcriptions brutes ».
- **Contre-exemple** : un lot nocturne consolide les sessions du jour à partir de transcriptions conservées 24 heures. Le cadre ne dit pas si c'est une « mémoire longue » interdite ni sous quelle identité le lot écrit.
- **Correctif proposé** : borner la rétention du tampon (durée maximale, chiffrement, purge après consolidation) et exiger que l'identité du mandant soit capturée dans le tampon au moment de la session.
- **Confiance** : déduit.

### [05-18] [MINEUR] EXIG-ARC-25 : le « service de mémoire » partagé reste un état mutable partagé
- **Axe** : A
- **Localisation** : EXIG-ARC-25, p. 43 : « le partage passe par des ressources en lecture seule ou par un service de mémoire qui applique les contrôles de l'exigence EXIG-ARC-23 ». Pourquoi : « le Centre d'architecture Azure proscrit le partage d'état mutable entre agents concurrents ».
- **Diagnostic** : les contrôles d'EXIG-ARC-23 portent sur la provenance, l'isolation et l'expiration, non sur la concurrence. Un service de mémoire en écriture pour plusieurs agents reste un état mutable partagé, que la justification invoquée proscrit. Le texte ne prévoit ni contrôle de concurrence (version, verrou optimiste) ni règle de fusion. « Isolés les uns des autres » n'est pas défini : processus, identité, locataire?
- **Contre-exemple** : deux agents concurrents mettent à jour le même fait client par le service de mémoire. La dernière écriture l'emporte, sans détection.
- **Correctif proposé** : exiger dans le service de mémoire une écriture conditionnelle (ETag ou numéro de version) et un journal des écritures. Définir « isolé » (identité de charge de travail et espace de noms distincts).
- **Confiance** : déduit.

### [05-19] [MINEUR] Tableau 14 et figure 5 contre EXIG-INT-03 : portée de l'accord, EFVP et TLS
- **Axe** : C
- **Localisation** : tableau 14, p. 47, ligne Gouvernance intégrée : « Accord d'interopérabilité par intégration ». EXIG-INT-03 : « Toute intégration qui franchit la frontière d'un domaine métier ou de l'entreprise ». Figure 5, p. 46 : « EFVP; entente écrite pour toute communication hors Québec », « TLS 1.3 ». Tableau 14 : « EFVP lorsque la loi l'exige », « TLS 1.2 toléré comme plancher ».
- **Diagnostic** : le tableau rend l'accord obligatoire pour toute intégration, alors que l'exigence le limite aux intégrations qui franchissent une frontière. La figure présente l'EFVP comme systématique et TLS 1.3 comme seul admis, alors que le tableau les conditionne.
- **Contre-exemple** : un outil MCP intradomaine n'a pas d'accord. Il est conforme à EXIG-INT-03 et non conforme au « minimum » du tableau 14.
- **Correctif proposé** : écrire dans le tableau 14 « Accord d'interopérabilité pour toute intégration qui franchit un domaine (EXIG-INT-03) ». Aligner la figure 5 sur le tableau.
- **Confiance** : vérifié dans le texte.

### [05-20] [MINEUR] EXIG-INT-01 : revue à quatre niveaux pour chaque intégration, sans proportionnalité
- **Axe** : B
- **Localisation** : EXIG-INT-01, p. 47 : « Toute intégration d'un agent avec un outil, une ressource, un autre agent ou un flux d'événements DOIT faire l'objet […] d'une revue couvrant les niveaux juridique, organisationnel, sémantique et technique ».
- **Diagnostic** : une revue juridique et organisationnelle pour chaque outil P0 intradomaine (lecture publique) a un coût sans rapport avec le risque. Elle contredit la logique de proportionnalité du cadre (PRIN-04, paliers P0-P3). Sans grille allégée, l'exigence sera contournée par regroupement ou par complaisance.
- **Contre-exemple** : un agent qui ajoute un outil de conversion d'unités P0 doit produire une revue juridique consignée à sa fiche.
- **Correctif proposé** : graduer la revue selon le palier et la frontière franchie. Par exemple : P0 et P1 intradomaine, niveaux sémantique et technique seulement; P2-P3 ou interdomaine, les quatre niveaux.
- **Confiance** : déduit.

### [05-21] [MINEUR] EXIG-INT-04 « chaque interaction » : l'appel d'inférence et le repli SSE n'ont pas d'entrée au catalogue
- **Axe** : A / C
- **Localisation** : EXIG-INT-04, p. 49 : « Chaque interaction d'un agent DOIT emprunter le protocole que le catalogue désigne pour son type […] Tout connecteur propriétaire ou format hors catalogue exige une dérogation ». Tableau 15, ligne AG-UI : « à défaut, flux SSE structuré produit par l'orchestrateur ».
- **Diagnostic** : l'appel d'un agent à la passerelle de modèles (EXIG-ARC-08) est une interaction d'agent. Aucun type ni protocole du tableau 15 ne la couvre (API compatible OpenAI, API de fournisseur). Le « flux SSE structuré » de repli n'a ni contrat ni format au catalogue. Une lecture littérale exige une dérogation pour chaque agent.
- **Contre-exemple** : tout agent conforme à EXIG-ARC-08 serait, selon EXIG-INT-04, en défaut faute de dérogation pour son appel d'inférence.
- **Correctif proposé** : ajouter au tableau 15 une ligne « Agent → passerelle de modèles » (interface d'inférence de l'entreprise, statut Adopter) et définir le format du flux SSE de repli, ou exclure explicitement ces deux interactions de la portée d'EXIG-INT-04.
- **Confiance** : vérifié dans le texte.

### [05-22] [MINEUR] Révision trimestrielle : deux exigences et deux acteurs pour la même obligation
- **Axe** : C
- **Localisation** : p. 51 : « Le comité révise le catalogue chaque trimestre (section 11.7) ». EXIG-INT-08, p. 52 : « Le comité d'architecture et des risques agentiques DOIT réviser le catalogue ». EXIG-GOV-18 (§ 11.7) : « L'architecture d'entreprise DOIT réviser le catalogue […] et soumettre les changements de statut à l'approbation du comité ».
- **Diagnostic** : la même obligation est portée par deux exigences DOIT, avec deux responsables différents (le comité qui révise, contre l'architecture qui révise et le comité qui approuve). Il en résulte une redondance et une ambiguïté de RACI.
- **Contre-exemple** : un audit constate qu'aucune révision n'a eu lieu au trimestre. On ne sait pas qui est en défaut : le comité (EXIG-INT-08) ou l'architecture d'entreprise (EXIG-GOV-18)?
- **Correctif proposé** : garder une seule exigence (EXIG-GOV-18) et transformer EXIG-INT-08 en renvoi, ou aligner les acteurs (architecture : révise; comité : approuve).
- **Confiance** : vérifié dans le texte.

### [05-23] [MINEUR] « Loi sur le privé » redéfinie à plusieurs reprises
- **Axe** : C
- **Localisation** : p. 45 : « RLRQ, c. P-39.1, ci-après « Loi sur le privé » ». Le p. 43 cite déjà l'article 23 sous le nom complet.
- **Diagnostic** : l'abréviation est redéfinie plus loin au moins trois fois : § 8.8 (« P-39.1, « Loi sur le privé » »), § 12.1-12.2 (« ci-après « Loi sur le privé » ») et annexe E. La page 43 emploie le nom long deux pages avant la définition. Il y a redondance et dérive de notation, sans effet sur le sens.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : définir l'abréviation une fois, à la première occurrence (p. 43) ou dans le glossaire, puis l'employer partout.
- **Confiance** : vérifié dans le texte (full.txt).

### [05-24] [MINEUR] Parcours § 5.6 : ordre confirmation/compensation, et délégation conditionnelle dans un flux « déterministe »
- **Axe** : A
- **Localisation** : étape 9, p. 45 : « la conseillère reçoit la confirmation avec la référence d'audit. Si une étape ultérieure échoue sans reprise possible, le moteur exécute la compensation déclarée, ici l'annulation de l'avoir ». Étape 2 : « choisit le flux déterministe »; étape 6 : « Si une vérification relève d'un autre domaine […] l'orchestrateur délègue ».
- **Diagnostic** : après l'étape 8, aucune « étape ultérieure » n'est décrite. Si une compensation survient après la confirmation, la conseillère et le client détiennent une confirmation que le système annule. Le parcours ne dit ni si l'annulation d'un avoir *approuvé par une humaine* exige elle-même approbation ou notification, ni si elle se journalise à part. L'étape 6 laisse aussi entendre qu'un choix conditionnel de délégation se fait dans un flux dit déterministe, sans préciser si c'est le flux ou l'agent qui décide.
- **Contre-exemple** : l'avoir est confirmé au client, puis annulé en silence par compensation, sans trace d'approbation pour l'annulation.
- **Correctif proposé** : placer la confirmation après la dernière étape compensable, ou prévoir une notification de compensation au mandant et à l'approbatrice. Préciser que la branche de l'étape 6 est une branche du flux déclarée au registre.
- **Confiance** : déduit.

### [05-25] [MINEUR] Source d'éditeur pour justifier un choix normatif sur MCP
- **Axe** : B
- **Localisation** : p. 48 : « MCP ne garantit ni la livraison ni la cohérence des données, alors qu'un journal d'événements persistant découple producteurs et consommateurs, comme le souligne l'architecte Kai Waehner[167] ».
- **Diagnostic** : l'auteur cité est un architecte d'un éditeur de plateforme d'événements (Confluent), partie intéressée. L'énoncé est en outre imprécis. MCP est un protocole requête-réponse : la « garantie de livraison » relève du transport et de l'idempotence. Quant à la « cohérence des données », elle n'est pas une propriété qu'on attend d'un protocole d'appel. L'argument tient par les premiers principes (découplage temporel, plusieurs abonnés, rejeu) et n'a pas besoin de cette source.
- **Contre-exemple** : sans objet.
- **Correctif proposé** : reformuler selon les propriétés (« un appel MCP est synchrone et point à point; il n'offre ni rétention, ni rejeu, ni diffusion à plusieurs abonnés ») et classer la source en catégorie B en mentionnant l'affiliation.
- **Confiance** : à vérifier (affiliation de l'auteur de [167] par l'audit bibliographique).

### [05-26] [MINEUR] « Extensions officielles (Tasks, Apps, autorisation …) » : l'autorisation est-elle une extension?
- **Axe** : A
- **Localisation** : tableau 15, p. 49 : « extensions officielles (Tasks, Apps, autorisation; Enterprise-Managed Authorization reste au statut Évaluer), désactivées par défaut dans MCP ».
- **Diagnostic** : dans les révisions de MCP que je connais (jusqu'à 2025-11-25), l'autorisation fait partie de la spécification de base (facultative pour les transports HTTP). Seules certaines variantes (identifiants clients, EMA) sont des extensions. Le § 6.5 du même document décrit l'autorisation 2026-07-28 comme du cœur (RFC 8707, RFC 9207, PKCE) et non comme une extension « désactivée par défaut ». Présenter l'autorisation comme désactivée par défaut pourrait laisser croire qu'un serveur sans autorisation est la configuration normale.
- **Contre-exemple** : une équipe lit « autorisation […] désactivée par défaut » et expose un serveur sans OAuth en attendant son « inscription ».
- **Correctif proposé** : écrire « extensions officielles (Tasks, Apps, extensions d'autorisation telles que les identifiants clients; Enterprise-Managed Authorization au statut Évaluer) ».
- **Confiance** : à vérifier (journal des modifications de la révision 2026-07-28 et dépôt ext-auth).

## Points forts
L'exemple TPS/TVQ est arithmétiquement exact (1 000 × 1,14975 = 1 149,75) et illustre bien le niveau sémantique. L'encadré « Normes, brouillons et préversions » et le refus de fixer un seuil de latence sur la foi des fournisseurs sont exemplaires. Le parcours § 5.6 relie concrètement les exigences des six couches.

## Questions pour l'audit bibliographique
- p. 43 : Anthropic, outil mémoire côté client [152]. Validation des chemins contre la traversée « exigée », recommandations sur la taille et la suppression des mémoires inutilisées : formulation exacte (exige ou recommande).
- p. 43 : CoALA [100] juge-t-il expressément l'écriture procédurale « nettement plus risquée »? Centre d'architecture Azure [9] : proscription du partage d'état mutable entre agents concurrents (patron concurrent).
- p. 45 : nouvel EIF 2017 [157]. Vérifier « 12 principes et 47 recommandations » et l'objet de la recommandation 26 (accords d'interopérabilité dans toutes les couches).
- p. 45 : règlement (UE) 2024/903. Entrée en vigueur le 11 avril 2024; rôle du comité pour une Europe interopérable dans la mise à jour de l'EIF [159].
- p. 47 : AsyncAPI 3.x (3.1.0). Liste des valeurs de `schemaFormat` que les outils doivent obligatoirement reconnaître; JSON Schema 2020-12 en fait-il partie? (voir 05-10)
- p. 47 : MCP [162, 163]. JSON Schema 2020-12 comme dialecte par défaut (depuis 2025-11-25) toujours valide en 2026-07-28.
- p. 48 : AG-UI [164-166]. « 31 types d'événements standard », licence MIT, « partenariat de CopilotKit avec LangChain et CrewAI » (LangGraph?).
- p. 48 : affiliation de Kai Waehner [167] (voir 05-25).
- p. 49 : documentation A2A [161]. Formulation « strongly recommend » d'une solution de gestion d'API pour les serveurs exposés.
- p. 49 : MCP 2026-07-28 [169]. Liste des extensions officielles; statut de l'autorisation (cœur ou extension) (voir 05-26).
- p. 50 : OpenAPI 3.2.1 (10 septembre 2026) [170]; Arazzo 1.1.0 (17 mai 2026) [172] (l'annexe H, réf. [486], confirme l'étiquette 1.1.0, mais pas la date); draft-ietf-oauth-v2-1-16 (septembre 2026) et son expiration le 7 mars 2027 [176]; draft-ietf-oauth-transaction-tokens-11 [179]; statut « brouillon de groupe de travail » d'ID-JAG [177].
- p. 50 : A2A 1.0. En-tête `A2A-Version` obligatoire à chaque requête; dates de 1.0.0 (12 mars 2026) et de 1.0.1 (28 mai 2026) [29, 30].
- p. 51 : AGNTCY « candidat à l'AAIF » (cohérent avec le § 6.9 et le tableau 5 : à confirmer à la source [37, 182]).

audit_05.md : 26 constats (0 BLOQUANT, 9 MAJEUR, 17 MINEUR)
