**Segment scope**: Pages 78 à 145 (Livre I, Chapitres 7 à 11 et Livre II, Chapitre 12 — Couche protocolaire, découverte, transactions AP2/AGNTCY, modes d'échec et identités étirées).

# RAPPORT D'UNITÉ DÉFINITIF DE NIVEAU 2 : SEGMENT DES PROTOCOLES
## Consolidation racine et réconciliation contradictoire (Chapitres 7 à 12, pp. 78-145)

---

# 1. Verdict Exécutif de Segment

Le segment consacré à la couche protocolaire agentique (pp. 78 à 145, couvrant les chapitres 7 à 11 du Livre I ainsi que l'ancrage identitaire du chapitre 12 du Livre II) aborde le nœud névralgique de l'ouvrage : le passage de l'intégration logicielle déterministe classique à la négociation dynamique d'intentions et de transactions autonomes entre systèmes d'intelligence artificielle.

### Évaluation globale et niveau de maturité
Sur le plan de l'intention architecturale, le segment pose des jalons conceptuels remarquables. L'auteur saisit avec acuité l'impératif de neutralité de gouvernance (transition vers la Linux Foundation), caractérise avec pertinence l'illusion du « port universel » de MCP, et documente avec lucidité l'asymétrie structurelle entre l'axe agent-outil (asymétrique, client-serveur) et l'axe agent-agent (symétrique, pair-à-pair).

Toutefois, l'audit contradictoire approfondi de Niveau 2 révèle que ce segment souffre d'un contraste saisissant entre une grande sophistication théorique apparente et des défaillances fondamentales de modélisation en systèmes distribués, en cryptographie appliquée, en ingénierie financière et en rigueur éditoriale :
1. **Ruptures matérielles de composition et de texte** : Le segment est entaché de bogues de composition inacceptables dans un compendium de référence, notamment à la page 115 (mot « chapitre » tronçonné en « ce cha ... pitre », suivi d'un bégaiement textuel de la thèse entière) et à la page 79 (deux ruptures syntaxiques brutales et phrases tronquées net).
2. **Fausses apories et confusions de couches réseau (OSI)** : L'auteur érige une collision homonymique industrielle ordinaire sur l'acronyme « ACP » en un abîme épistémologique prétendument insoluble, en confondant le *Data Plane* applicatif L7 (IBM BeeAI / A2A) et le *Control Plane* réseau d'infrastructure L4/L5 (Cisco AGNTCY / SLIM).
3. **Falsification de la réduction combinatoire et imprudence transactionnelle sur MCP** : L'affirmation selon laquelle MCP ramène la complexité d'intégration de $O(N \times M)$ à $O(N + M)$ est formellement fausse au niveau sémantique/pragmatique face à l'hétérogénéité des modèles de fondation. De plus, la qualification du transport MCP révisé comme « cœur sans état » déployable derrière un simple tourniquet (*round-robin*) est contredite par l'usage de poignées d'état (*handles*) pour les requêtes multi-tours (MRTR), tandis que la suppression de la reprise de flux sans clé d'idempotence financière ouvre une brèche critique de double débit transactionnel.
4. **Impasse transactionnelle et juridique d'AP2** : Présenté abusivement comme un protocole transactionnel financier, AP2 ne constitue qu'une chaîne statique d'attestations W3C vérifiables sans aucune garantie d'atomicité (ACID), sans modèle Saga compensatoire, et sans aucune prise en compte de la concurrence (verrous distribués, double dépense budgétaire). Pire encore, l'affirmation selon laquelle cette chaîne signée confère une « preuve opposable » assurant la non-répudiation est juridiquement et cryptographiquement caduque : l'injection indirecte d'invite anéantit le contrôle exclusif du mandant sur sa signature (LCCJTI art. 28, eIDAS art. 26).
5. **Omissions de l'état de l'art normatif (IETF, ISO) et hallucinations juridiques** : L'analyse d'OAuth 2.0 ignore le standard majeur RFC 9449 (DPoP), accusant à tort le jeton porteur (*bearer token*) d'être la cause racine d'une crise qui réside en réalité dans l'intégrité cognitive de l'agent. Le texte invoque un prétendu « règlement (UE) 2026/1744 » inexistant pour reporter l'AI Act à 2028, ignore ISO 20022 (`pain.001`, `pacs.008`) indispensable aux rails bancaires d'entreprise (Lynx, RTR), et dénature la tolérance aux pannes byzantines (PBFT) en l'appliquant aveuglément à des agents stochastiques sujets à des défaillances corrélées en mode commun (*Common-Cause Failures*).

En l'état, la couche protocolaire ne peut être déployée en environnement financier réglementé sans une refonte en profondeur des chapitres 7 à 12.

---

# Potential Mistakes and Improvements

Cette section rassemble l'ensemble des défauts critiques et majeurs validés sur pièces, classés par sévérité décroissante.

---

## 2.1 Défauts Bloquants et Erreurs Formelles [Critical / Blocking]

### DEF-PROT-01 [Bloquant / Erreur formelle d'édition] Bogue de composition typographique à la page 115 : mot tronçonné (« ce cha ... pitre »), rupture syntaxique et duplication textuelle de la thèse
- **Sévérité** : Bloquant / Erreur formelle d'édition.
- **Localisation précise** : Chapitre 10 (*Transaction et infrastructure : AP2 et AGNTCY*), page 115 du PDF (`page-115.png`), lignes 9484 à 9507 de `DOCUMENT_TEXT_MAP.md`.
- **Citation textuelle exacte** :
  > « [...] La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce cha
  > Thèse — que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur — le socle établit qu’AP2 est un protocole compagnon d’A2A, rien de plus sur sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet, une déclaration et non un fait vérifié, que des analyses tierces nuancent. pitre prend pour objet. Que la transaction agentique constitue l’aboutissement financier de la pile protocolaire est une lecture d’auteur : les sources établissent que le protocole de paiement est un protocole compagnon de l’axe agent-agent, dédié aux transactions pilotées par agents, et rien de plus sur sa centralité. Qu’AGNTCY soit une couche d’infrastructure et non un concurrent est, pour sa part, le positionnement officiel déclaré du projet — une déclaration, non un fait vérifié, et que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux n’est un fait établi. »
- **Diagnostic causal approfondi** :
  L'inspection directe de la page 115 démontre un accident de composition logicielle (moteur Pandoc/LaTeX) survenu lors de l'insertion d'un bloc flottant d'encadré de thèse :
  1. *Scission morphologique d'un lexème pivot* : Le mot « chapitre » est tronçonné en deux fragments étanches : le radical « ce cha » termine la ligne précédant l'encadré, tandis que le suffixe « pitre prend pour objet. » est réinjecté de façon aberrante au beau milieu de la phrase suivant l'encadré, immédiatement après le mot « nuancent. ».
  2. *Bégaiement textuel intégral* : Le paragraphe succédant immédiatement à la boîte de thèse reprend quasi mot pour mot le contenu même de la boîte de thèse (« Que la transaction agentique constitue l'aboutissement financier... »), créant une redondance tautologique dégradante dans l'ouverture d'un chapitre fondamental de la somme.
- **Correctif formel direct** :
  Restructurer l'entrée du chapitre 10 en supprimant la duplication et en ressoudant la phrase introductive :
  ```markdown
  La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce chapitre prend pour objet.

  Thèse — Que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur : le socle établit qu’AP2 est un protocole compagnon d’A2A, sans préjuger de sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet — une déclaration d'intention et non un fait vérifié, que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux ne constitue un fait établi.
  ```

---

### DEF-PROT-02 [Bloquant / Erreur formelle & Confusion de couches] Fausse aporie sur la collision terminologique « ACP » : confusion entre le Data Plane applicatif L7 (IBM BeeAI / A2A) et le Control Plane réseau L4/L5 (Cisco AGNTCY)
- **Sévérité** : Bloquant / Erreur formelle de modélisation réseau.
- **Localisation précise** : Chapitre 10, pages 126-127, § 10.5.3 (*Le versant protocolaire de la collision terminologique*), et Chapitre 7, page 87, Tableau 7.3 ligne (d) et encadré § 7.5 (`page-87.png`, `page-126.png`, `page-127.png`).
- **Citation textuelle exacte** :
  > « Restent deux objets, et c’est entre eux que la confusion est à la fois la plus facile et la plus dommageable : l’ACP protocolaire, dont le § 10.5.1 vient de rappeler la fusion ; et la composante ACP de la couche d’infrastructure, dont le § 10.2.3 a rapporté que des analyses tierces lui prêtent un chevauchement avec le protocole agent-agent. Les sources n’établissent, de cette seconde, ni l’intitulé complet, ni la nature, ni l’identité avec la première. [...]
  > L’enjeu de cette prudence n’est pas cosmétique, et les deux branches de l’alternative conduisent à des conclusions d’architecture opposées :
  > • si les deux objets n’en font qu’un, la fusion d’août 2025 vaut pour la couche d’infrastructure, et le chevauchement relevé par les tiers est le vestige d’un protocole éteint ;
  > • s’ils sont deux, la couche d’infrastructure porte une composante active dont le rapport au protocole agent-agent reste à qualifier.
  > Les sources ne tranchent pas, et aucune inférence n’est proposée ici. Un ouvrage qui trancherait gagnerait en fluidité ce qu’il perdrait en droit d’être cru. La question est ouverte au registre des lacunes du Vol. II, et la somme la portera telle quelle jusqu’au ch. 49... »
- **Diagnostic causal approfondi** :
  L'auteur érige une simple homonymie industrielle en un abîme épistémologique (« le dossier le plus délicat de la somme »), en posant une alternative insoluble qui témoigne d'une confusion entre les couches du modèle OSI :
  1. *L'ACP d'IBM Research / BeeAI (mars 2025)* est strictement un **protocole de niveau application (Couche 7 OSI / Data Plane)** définissant des schémas d'échange sémantique et d'intentions entre agents. Il a formellement fusionné le 29 août 2025 avec le protocole Agent2Agent (A2A) au sein de la Linux Foundation.
  2. *L'ACP de Cisco AGNTCY (juillet 2025)* désigne l'**Agentic Control Plane (Couche 4/5 OSI / Control Plane Réseau)**. C'est une brique de signalisation d'infrastructure réseau gérant l'interconnexion de passerelles (*Agent Gateways*), la propagation des tables de routage sémantiques et la négociation des canaux sécurisés du maillage SLIM (*Secure Lightweight Inter-agent Messaging*).
  Prétendre que ces deux entités pourraient « n'en faire qu'un » et qu'une brique de signalisation réseau de Cisco aurait pu « s'éteindre » à cause d'une fusion applicative d'IBM est un contresens architectural total. L'abstention de l'auteur nuit gravement à la crédibilité technique de l'ouvrage.
- **Correctif formel direct** :
  Réfuter l'alternative d'indécidabilité du § 10.5.3. Clarifier l'étagement des responsabilités selon le modèle des plans réseau :
  $$\text{Architecture Globale} = \begin{cases} \mathbf{Plan\ Applicatif\ (Couche\ 7)} : & \text{A2A v1.0 (absorbant l'ACP-IBM pour le transport des charges utiles d'intention)} \\ \mathbf{Plan\ de\ Contr\hat{o}le\ R\acute{e}seau\ (Couche\ 5)} : & \text{ACP-Cisco AGNTCY (signalisation, routage de passerelles et annuaires)} \\ \mathbf{Plan\ de\ Donn\acute{e}es\ R\acute{e}seau\ (Couche\ 4)} : & \text{SLIM Mesh (chiffrement et transport point-à-point)} \end{cases}$$

---

### DEF-PROT-03 [Bloquant / Erreur formelle - Axe R3] Citation réglementaire erronée d'un prétendu « règl. (UE) 2026/1744 » et calendrier contradictoire de l'AI Act
- **Sévérité** : Bloquant / Erreur formelle (Axe R3 — Intégrité des sources juridiques et normatives).
- **Localisation précise** : Chapitre 10, page 124, lignes 10296-10303 de `DOCUMENT_TEXT_MAP.md` (vérifié sur `page-124.png`), en contradiction avec les pages 30520, 34016, 60352 et 60726.
- **Citation textuelle exacte** :
  > « Sur le plan réglementaire, le règlement européen sur l’intelligence artificielle — Règlement (UE) 2024/1689, nommé ici parce qu’un instrument repris se désigne par son identifiant — encadre notamment les modèles à usage général, dont les obligations s’appliquent depuis août 2025, la mise en conformité générale se poursuivant jusqu’au 2 août 2027 (2028 pour le haut risque, règl. (UE) 2026/1744). »
- **Diagnostic causal approfondi** :
  Ce passage contient une anomalie juridique majeure doublée d'une incohérence interne flagrante dans l'ouvrage :
  1. *Acte inexistant dans EUR-Lex* : Le texte normatif désigné comme « règl. (UE) 2026/1744 » n'existe pas dans le Journal officiel de l'Union européenne régissant l'intelligence artificielle. Le cadre juridique exclusif est le **Règlement (UE) 2024/1689** du 13 juin 2024. L'auteur concède d'ailleurs lui-même en annexe (p. 60726, ligne 60728) : « EUR-Lex répond HTTP 202 sans contenu; la date de publication du règlement (UE) 2026/1744 n'a pas été relue. »
  2. *Contradiction interne sur les dates d'échéance* : La page 124 annonce une échéance à « 2028 pour le haut risque », tandis que le chapitre 30 (p. 30520) et le chapitre 34 (p. 34016) affirment péremptoirement que l'échéance opposable est reportée au « 2 décembre 2027 ».
  3. *Calendrier officiel de l'art. 111 du Règlement (UE) 2024/1689* :
     - 2 février 2025 : Pratiques interdites (art. 5) ;
     - 2 août 2025 : Modèles d'IA à usage général (GPAI, Chapitre V) ;
     - 2 août 2026 : Entrée en application générale, incluant les systèmes à haut risque de l'**Annexe III** ;
     - 2 août 2027 : Systèmes à haut risque relevant des législations d'harmonisation de l'UE préexistantes (**Annexe I**).
  Aucun report à 2028 n'est prévu pour l'Annexe III.
- **Correctif formel direct** :
  Purger impérativement toute mention du prétendu `règl. (UE) 2026/1744` et harmoniser le calendrier d'application :
  > « ...la mise en conformité des modèles d’IA à usage général (GPAI) s’appliquant depuis le 2 août 2025, l'entrée en application générale des systèmes à haut risque de l'Annexe III intervenant au 2 août 2026, et celle des systèmes régis par les législations d'harmonisation sectorielles de l'Annexe I au 2 août 2027, conformément à l'article 111 du Règlement (UE) 2024/1689. »

---

### DEF-PROT-04 [Bloquant / Erreur formelle & Modélisation transactionnelle] Absence de formalisme transactionnel réparti (ACID/BASE) et impossibilité d'atomicité dans AP2 sans patron Saga compensatoire
- **Sévérité** : Bloquant / Erreur formelle en théorie des systèmes répartis.
- **Localisation précise** : Chapitre 10, page 116 (§ 10.1.1, lignes 9540-9545) ; page 118 (§ 10.1.4, lignes 9746-9772) ; et Figure 10.4 page 125 (`page-116.png`, `page-118.png`, `page-125.png`).
- **Citation textuelle exacte** :
  > « AP2 s’attache à ce qui se passe lorsque la tâche déléguée engage un paiement. Ce n’est pas un protocole concurrent ; c’est un protocole qui prend le relais au point où la délégation cesse d’être réversible » ;
  > « Il porte la chaîne de mandats — Intent Mandate, Cart Mandate, Payment Mandate — matérialisés comme attestations vérifiables signées au sens de la recommandation du consortium du web [...] Le contrat de consentement est découplé du contrat de mouvement de fonds ».
- **Diagnostic causal approfondi** :
  Le manuscrit qualifie abusivement AP2 de « protocole de transaction » alors qu'il ne s'agit que d'un format d'échange d'attestations vérifiables statiques (W3C Verifiable Credentials) :
  1. *Une chaîne de jetons signés ne constitue pas une transaction répartie* : Une autorisation cryptographique statique n'offre aucune garantie de consistance dynamique face aux partitions réseau, aux pannes partielles de passerelles marchandes ou aux refus de compensation interbancaire.
  2. *Violation de l'Atomicité ($A$ de ACID) :* Si le `Payment Mandate` est capturé sur le réseau financier (débit bancaire effectif), mais que le marchand ou l'agent subit un crash avant la validation du panier ou la délivrance de la marchandise, le système demeure dans un état non atomique incohérent (débit financier sans contrepartie d'actif).
  3. *Fausse allégation d'irréversibilité instantanée :* Les rails bancaires réels fonctionnent avec des pré-autorisations, des autorisations avec capture différée, des compensations nettes différées et des régimes de rétrofacturation (*chargebacks*). En l'absence de formalisation d'un patron Saga distribué orchestré (avec définition mathématique des transactions compensatoires $C_i$ annulant les transactions directes $T_i$), AP2 est formellement inapte au traitement transactionnel financier d'entreprise.
- **Contre-exemple explicite et correctif formel** :
  *Contre-exemple :* Réservation multi-agents avion (900 $) + hôtel (300 $). Le paiement du vol est validé via AP2. Lors de l'appel pour l'hôtel, l'API renvoie un code HTTP 503 (chambres épuisées). Si la politique d'entreprise impose l'annulation du voyage global, aucun mécanisme d'AP2 ne coordonne la compensation financière, laissant les fonds débités et le système dans un état orphelin corrompu.
  *Correctif formel :*
  Requalifier AP2 comme protocole de *mandat et d'autorisation*, et définir explicitement l'automate d'exécution Saga :
  $$\text{Transaction Globale } G = (T_1, T_2, \dots, T_n) \quad \text{avec le vecteur de compensation } (C_n, \dots, C_1)$$
  où chaque mandat de paiement (`Payment Mandate`) porte un `Global-Transaction-ID` et est obligatoirement assorti d'une spécification de mandat d'annulation (`Void Mandate`) et de remboursement (`Reversal Mandate`).

---

### DEF-PROT-05 [Bloquant / Erreur formelle juridique & Cryptographique] Rupture de la non-répudiation juridique dans AP2 face à l'injection d'invites par anéantissement du contrôle exclusif du mandant
- **Sévérité** : Bloquant / Erreur formelle juridique et cryptographique.
- **Localisation précise** : Chapitre 10, page 120 (Tableau 10.1) ; page 123 (§ 10.3.4, lignes 10220-10234) ; et pages 124-125 (§ 10.4.2, lignes 10280-10293, `page-123.png`, `page-124.png`).
- **Citation textuelle exacte** :
  > « Debi et coll., Whispers of Wealth, 2026 [...] montre que la signature des mandats ne neutralise pas l’amont : un agent dont l’intention est détournée signera un mandat malveillant parfaitement valide. Le verrou n’est pas la vérifiabilité cryptographique du mandat — elle fonctionne — mais l’intégrité du raisonnement qui le produit » ;
  > « La réponse architecturale : le mandat comme couche de preuve opposable. La chaîne intention -> panier -> paiement du § 10.1.4, signée et horodatée, fournit l’élément probant qui rattache une transaction contestée à un consentement antérieur du mandant ».
- **Diagnostic causal approfondi** :
  Il existe une contradiction interne flagrante entre la démonstration de la page 123 et la conclusion de la page 124 :
  - À la page 123, l'auteur concède qu'un agent manipulé par injection indirecte apposera une signature cryptographique valide sur un mandat malveillant spoliant l'utilisateur.
  - Aux pages 124-125, il prétend néanmoins que cette même chaîne signée constitue la « preuve opposable » rattachant la transaction au consentement du mandant et assurant la non-répudiation.
  Or, en droit de la preuve électronique (Loi concernant le cadre juridique des technologies de l'information - LCCJTI art. 28 au Québec, LPRPDE/PIPEDA au Canada fédéral, et Règlement eIDAS art. 26 en Europe), la force probante et la non-répudiation reposent sur une condition préalable d'ordre public : **le signataire doit conserver le contrôle exclusif de son moyen de création de signature**.
  Dès lors qu'une clé de signature est déléguée à un processus stochastique autonome soumis à des interférences contextuelles, le contrôle exclusif est détruit. Devant un tribunal, la signature du mandat prouve uniquement l'exécution d'un calcul stochastique, jamais l'intégrité du consentement de l'humain.
- **Correctif formel direct** :
  Supprimer l'affirmation selon laquelle la chaîne signée AP2 résout l'opposabilité et la non-répudiation. Établir une démarcation stricte :
  1. *Transactions sous présence humaine (Human-Present) :* Signature du hachage de commande (`CartHash`) via WebAuthn/Passkeys (FIDO2) exécutée au sein d'une enclave matérielle sécurisée (Secure Enclave / TPM), garantissant le contrôle exclusif de l'humain.
  2. *Transactions autonomes déléguées (Human-Not-Present) :* Exclusion expresse du principe de non-répudiation opposable au débiteur ; bascule obligatoire vers un régime contractuel de responsabilité objective, de dépôts fiduciaires sous séquestre (*escrow*), de plafonds d'autorisation stricts et d'assurance contre le risque d'ingérence algorithmique.

---

### DEF-PROT-06 [Bloquant / Erreur formelle d'architecture] Rupture d'idempotence et invalidation du routage à tourniquet sous transport MCP révisé sans état
- **Sévérité** : Bloquant / Erreur formelle d'architecture de systèmes distribués.
- **Localisation précise** : Chapitre 8, page 92, Tableau 8.2 et lignes 7502-7518 (vérifié sur `page-92.png`) ; et Chapitre 11, page 135 (§ 11.3.1, lignes 11296-11303).
- **Citation textuelle exacte** :
  > « Cœur sans état (ratifié le 28 juill. 2026) : suppression de la poignée de main, de l’identifiant de session et de la reprise de flux. Couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet. »
  > « (1) Les sessions de protocole et l’en-tête qui les portait disparaissent... l’état qu’un serveur doit conserver d’un appel à l’autre passe par des poignées explicites, frappées par le serveur et transmises comme arguments d’outil ordinaires. »
  > « (3) Le découplage se paie, et le prix n’était pas au tableau : la reprise de flux et la retransmission de messages sont retirées — un flux de réponse interrompu perd la requête en vol, que le client doit réémettre sous un identifiant neuf. »
- **Diagnostic causal approfondi** :
  Ce passage cumule deux failles distribuées rédhibitoires :
  1. *Rupture d'idempotence et double exécution destructrice* : Prescrire qu'en cas d'interruption réseau du flux de réponse, le client « doit réémettre sous un identifiant neuf » viole frontalement la théorie de la distribution transactionnelle. Si la requête `tools/call` est une opération modifiant l'état (virement bancaire, ordre boursier, modification d'infrastructure cloud) et que la coupure intervient après l'exécution locale par le serveur mais avant la réception de la réponse HTTP, l'émission d'une requête avec un nouvel `id` JSON-RPC déclenche une réexécution aveugle non dédupliquée, JSON-RPC 2.0 ne comportant aucune clé d'idempotence native. Renvoyer cette question au chapitre 48 constitue une esquive inadmissible.
  2. *Contradiction du répartiteur à tourniquet (Round-Robin Routing)* : Affirmer qu'il n'y a « aucun couplage résiduel » et qu'un serveur est « déployable derrière un répartiteur à tourniquet » est directement démenti par la phrase précédente : les requêtes à tours multiples (MRTR) utilisent des « poignées explicites frappées par le serveur ». Si le tour 1 génère un handle en mémoire sur l'instance $S_1$ et que le tour 2 est routé par le tourniquet vers l'instance $S_2$, l'appel échoue immédiatement par poignée invalide (`Unknown Handle`), à moins d'imposer une affinité de session (*sticky session*) ou un magasin d'état distribué partagé (Redis/DB), deux contraintes qui contredisent expressément l'absence de tout couplage résiduel.
- **Correctif formel et contre-exemple explicite** :
  *Scénario de rupture :* Virement bancaire de 100 000 $ émis sous `id: 501`. Le serveur MCP débite le compte, mais le réseau s'effondre avant la sérialisation SSE de la réponse. Le client MCP réémet la même charge sous `id: 502`. Le serveur sans état exécute à nouveau l'outil. 200 000 $ sont débités.
  *Formulation corrigée du Tableau 8.2 et du texte* :
  > Remplacer « Couplage résiduel : aucun — serveur déployable derrière un répartiteur à tourniquet » par :
  > « Découplage du transport HTTP. En revanche, pour les requêtes multi-tours (MRTR), un couplage d'état applicatif subsiste : le déploiement horizontal derrière un tourniquet exige soit un magasin d'état partagé entre instances de serveurs, soit des jetons d'état autonomes signés côté client (schéma AEAD). De plus, la suppression de la reprise de transport interdit la réémission aveugle des méthodes à effet de bord : le protocole d'application doit obligatoirement encapsuler une clé d'idempotence déterministe (`Idempotency-Key` HMAC) et un cache de déduplication côté serveur. »

---

### DEF-PROT-07 [Bloquant / Erreur formelle de modélisation] Falsification combinatoire du coût d'intégration $N \times M \to N + M$ de MCP face aux modèles stochastiques
- **Sévérité** : Bloquant / Erreur formelle de modélisation.
- **Localisation précise** : Chapitre 8, page 90 (texte et Figure 8.1), lignes 7340-7346 (`page-90.png`).
- **Citation textuelle exacte** :
  > « faire dialoguer N agents avec M outils sans standard impose N×M intégrations point-à-point ; une couche de contrat partagée ramène ce coût à N+M. C’est exactement le geste du modèle de données canonique (ch. 1 § 1.6.1), transposé à l’axe agent-outil — et il vaut d’être reconnu comme tel plutôt que présenté comme une nouveauté. »
- **Diagnostic causal approfondi** :
  Cette affirmation transpose sans discernement un théorème d'intégration logicielle déterministe (où un schéma canonique XML/JSON et un protocole RPC éliminent les adaptateurs logiciels de $O(N \times M)$ à $O(N + M)$) à une architecture pilotée par des modèles d'inférence probabilistes hétérogènes.
  Dans le protocole MCP, un outil n'est pas sélectionné par un compilateur mais par la boucle cognitive d'un grand modèle de langage lisant sa description en langage naturel (`description`, p. 111). Or, chaque famille de modèles ($N$ modèles : Claude 3.5, GPT-4o, Gemini 1.5, Llama 3.3, Mistral Large) possède des sensibilités de prompt, des fenêtres contextuelles et des heuristiques de *function calling* dissemblables :
  - L'interopérabilité technique de transport est bien en $O(N + M)$ ;
  - En revanche, l'interopérabilité sémantique et pragmatique (LCIM niveaux 3 et 4) impose une calibration, une réécriture de prompts, une validation empirique de sélection et un banc de test unitaire pour chaque paire $(\text{Agent}_i, \text{Outil}_j)$.
  Décréter que le coût global d'intégration est ramené à $N + M$ occulte la composante de coût dominante de l'ingénierie agentique, qui demeure combinatoire en $O(N \times M)$ en l'absence d'une sémantique formellement prouvable.
- **Correctif formel direct** :
  > « La standardisation syntaxique du transport et des schémas JSON-RPC opérée par MCP ramène la plomberie d'interconnexion technique de $O(N \times M)$ à $O(N + M)$. En revanche, au niveau pragmatique du LCIM, l'interprétation des descriptions textuelles d'outils par des modèles probabilistes hétérogènes réintroduit une charge d'ajustement et d'évaluation combinatoire : l'assurance que $N$ modèles distincts sélectionnent et paramètrent correctement $M$ outils sans dérive sémantique ne s'obtient pas en $N+M$ sans une ontologie de capacités formellement vérifiable. »

---

### DEF-PROT-08 [Bloquant / Faille de sécurité architecturale] Évasion de confinement (Path Traversal) induite par la dépréciation des racines (`roots`) MCP au profit d'arguments d'outils
- **Sévérité** : Bloquant / Faille de sécurité architecturale.
- **Localisation précise** : Chapitre 8, page 91, § 8.1.2, lignes 7420-7426 (`page-91.png`).
- **Citation textuelle exacte** :
  > « (1) les racines et l’échantillonnage passent à l’état déprécié — avec la journalisation —, la spécification recommandant de leur substituer, respectivement, le passage des répertoires par paramètres d’outil ou URI de ressource... »
- **Diagnostic causal approfondi** :
  Dans l'architecture de sécurité de MCP, la primitive `roots` permettait à l'application hôte (le client) d'imposer au serveur un périmètre inviolable de répertoires autorisés sur le système de fichiers, établissant une frontière de bac à sable (*sandbox boundary*) au niveau du protocole.
  Le compendium rapporte sans aucune réserve critique la recommandation de déprécier les racines au profit du passage des répertoires comme arguments d'outils. Or, dans un système agentique, les arguments d'outils sont générés de manière stochastique par le modèle de fondation. Si l'hôte délègue la délimitation du périmètre aux arguments fournis par le modèle, une injection de prompt indirecte (provenant d'un document externe non fiable analysé par l'agent) peut contraindre le modèle à émettre un chemin hors périmètre (`C:\Windows\System32`, `~/.ssh/id_rsa`, `/etc/passwd` ou `../../sensitive_data`).
  Substituer la négociation descendante de `roots` par des paramètres d'outils détruit le principe fondamental de médiation complète (*Complete Mediation*) et transfère la sécurité à un composant intrinsèquement faillible (l'inférence probabiliste).
- **Correctif formel direct** :
  Ajouter au § 8.1.2 un encadré de sécurité impératif :
  > « Avertissement architectural : le passage de répertoires en paramètres d'outils ne constitue en aucun cas une alternative sécurisée aux racines (`roots`). Dès lors que la frontière `roots` est dépréciée au niveau protocolaire, l'infrastructure d'entreprise doit impérativement réintroduire un confinement physique au niveau de l'OS (namespaces Linux, chroot, conteneurisation éphémère ou sandboxing gVisor), interdisant au serveur d'accéder à des chemins situés hors du périmètre alloué, indépendamment des arguments générés par le LLM. »

---

### DEF-PROT-09 [Bloquant / Erreur formelle mathématique - Axe R2] Incompatibilité théorique de la tolérance aux pannes byzantines (BFT) classique appliquée aux agents probabilistes
- **Sévérité** : Bloquant / Erreur formelle de modélisation algorithmique (Axe R2).
- **Localisation précise** : Chapitre 11, page 133, § 11.2.1, lignes 11110-11118 (`page-133.png`).
- **Citation textuelle exacte** :
  > « Perspective de recherche — vers une science de la fiabilité des agents. Deux cadres analytiques se distinguent. D’une part, le rapprochement avec la tolérance aux pannes byzantines : un agent non déterministe qui émet un message plausible mais erroné se comporte comme un nœud byzantin, ce qui ouvre la question — encore largement ouverte — de seuils de quorum et de redondance pour des acteurs probabilistes. D’autre part, la décomposition de l’exécution en sous-tâches vérifiées par consensus comme voie vers une fiabilité de qualité industrielle. »
- **Diagnostic causal approfondi** :
  L'assimilation directe d'un agent LLM à un nœud byzantin dans un algorithme de consensus distribué classique (PBFT de Castro & Liskov, Raft byzantin) repose sur une triple incompatibilité mathématique :
  1. *Absence d'égalité bit-à-bit des sorties :* Dans les protocoles BFT classiques, la validation est un prédicat booléen strict $V(m) \in \{\text{true}, \text{false}\}$ et deux nœuds honnêtes exécutant le même automate déterministe produisent une égalité binaire stricte de leurs condensats cryptographiques ($H(m_1) = H(m_2)$). Pour des agents LLM probabilistes (même à température $T=0$), deux agents non défaillants ne génèrent **jamais de sorties textuelles identiques bit-à-bit** ($H(m_1) \neq H(m_2)$ presque sûrement), rendant le calcul de quorum sur signatures de hachages impossible.
  2. *Violation de l'axiome d'indépendance des pannes (Common-Cause Failures) :* BFT repose sur l'indépendance statistique des défaillances. Or, les agents d'entreprise partagent un petit nombre de modèles de fondation (Claude, GPT, Llama) et des contextes d'invites similaires. Face à une perturbation adverse ou un prompt complexe, ils partagent les mêmes modes d'échec ($P(E_i \cap E_j) \gg P(E_i)P(E_j)$). Un consensus super-majoritaire de modèles homogènes convergera ainsi unanimement vers l'erreur.
  3. *Régression infinie de l'arbitre :* L'application d'un quorum exige un arbitre sémantique. Si cet arbitre est un LLM, il est sujet aux mêmes pannes stochastiques.
- **Correctif formel direct** :
  Poser formellement les limites mathématiques du consensus agentique homogène :
  $$P(\text{Consensus Falsifié}) = \sum_{m = \lceil 2N/3 \rceil}^N \binom{N}{m} (1-\epsilon)^m \epsilon^{N-m} \xrightarrow[\epsilon \to 0]{} 1$$
  Stipuler que la tolérance aux pannes pour agents probabilistes exige d'abandonner le consensus binaire de transport au profit d'un **consensus sur invariants logiques formels** : projection des réponses stochastiques en prédicats typés vérifiables par des solveurs SMT ou des automates déterministes, combinée à une stricte hétérogénéité des modèles de fondation.

---

### DEF-PROT-10 [Bloquant / Erreur formelle & Omission normative IETF] Falsification de la crise d'OAuth 2.0 : omission des jetons liés au porteur (DPoP RFC 9449, MTLS RFC 8705) et méprise sur la racine de la crise
- **Sévérité** : Bloquant / Erreur formelle et omission de l'état de l'art IETF.
- **Localisation précise** : Chapitre 12 (*L’héritage et les standards étirés...*), page 144, lignes 12008-12011, et Tableau 12.1 (lignes 12042-12048, `page-144.png`).
- **Citation textuelle exacte** :
  > « Le maillon qui cède y est nommé, et il est architectural : le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. [...]
  > Tableau 12.1 : Le justificatif n’est pas lié à son porteur : Le jeton porteur de la campagne UNC6395 n’est lié ni à l’appelant, ni à un appareil, ni à une session (Vol. III F-21, [A]) »
- **Diagnostic causal approfondi** :
  Le manuscrit fait reposer l'ensemble de sa démonstration de la faillite d'OAuth face aux agents sur la vulnérabilité intrinsèque du jeton porteur (*Bearer Token*, RFC 6750), en prenant pour preuve l'incident UNC6395 (compromission de jetons d'intégration Salesforce).
  Cette analyse est doublement fautive :
  1. *Omission de l'état de l'art IETF :* L'IETF a précisément neutralisé la non-liaison des jetons porteurs en publiant le standard **RFC 9449 (DPoP - Demonstrating Proof-of-Possession at the Application Layer)** en septembre 2023 et le **RFC 8705 (Certificate-Bound Access Tokens via MTLS)**. Avec DPoP, le jeton d'accès est cryptographiquement lié à la paire de clés asymétriques du client. Le vol du jeton au repos (comme dans UNC6395) est totalement inopérant sans la clé privée de l'agent.
  2. *Méprise sur la vulnérabilité intrinsèque des agents :* En focalisant la critique sur le jeton non lié, l'auteur masque la véritable impasse d'OAuth 2.0 : même en présence de jetons parfaitement liés par DPoP (RFC 9449), un agent autonome dont le raisonnement est manipulé par injection d'invite générera lui-même des preuves DPoP valides pour accomplir des actes malveillants. La faillite d'OAuth ne réside pas dans l'absence de liaison cryptographique au porteur, mais dans l'incapacité d'OAuth à lier l'autorisation à **l'intégrité cognitive du modèle et au contexte sémantique d'inférence**.
- **Correctif formel direct** :
  Réécrire le § 12.2 et le Tableau 12.1 pour intégrer les RFC 8705 et 9449. Démontrer formellement les limites de DPoP face au détournement cognitif :
  $$\text{DPoP Proof} = \text{Sign}_{K_{\text{Agent}}}\big(\text{HTTP-Method} \parallel \text{URI} \parallel \text{Timestamp} \parallel \text{Hash}(T_{\text{access}})\big)$$
  Établir que la signature est mathématiquement irréprochable alors même que la décision d'appel résulte d'un empoisonnement de contexte, prouvant que l'autorisation machine classique ignore l'état d'intégrité cognitive de l'agent appelant.

---

## 2.2 Défauts Majeurs et Lacunes Méthodologiques [Major]

### DEF-PROT-11 [Majeur / Intégrité transactionnelle] Absence de modélisation de la concurrence, des collisions de verrous et de la double dépense budgétaire sous AP2
- **Sévérité** : Majeur / Lacune de modélisation d'intégrité transactionnelle (exigée par `REVIEW_PLAN.md`, segment S12).
- **Localisation précise** : Chapitre 10, pages 115-118 (§ 10.1) et page 123 (§ 10.3.4).
- **Diagnostic causal approfondi** :
  Le Chapitre 10 décrit l'enchaînement des mandats d'AP2 (`Intent Mandate` $\to$ `Cart Mandate` $\to$ `Payment Mandate`) sous forme d'attestations vérifiables signées W3C. Cependant, le modèle élude totalement la modélisation de la concurrence distribuée lors de sous-délégations parallèles :
  1. *Double allocation budgétaire (Budget Depletion / Double-Spend)* : Si un mandant humain confie à un orchestrateur un Intent Mandate avec un plafond de 5 000 $, et que l'orchestrateur mandate en parallèle deux sous-agents spécialisés (ex: hébergement et licences logicielles), chaque sous-agent peut négocier un panier de 3 500 $ et 2 500 $. Les deux paniers respectent individuellement la limite de 5 000 $. En l'absence d'un protocole de réservation atomique (Distributed Lock Manager, Two-Phase Commit ou jeton CAS), la présentation simultanée des deux Cart Mandates aux rails de règlement engage 6 000 $, violant la contrainte budgétaire du mandant.
  2. *Expiration et collisions de verrous d'inventaire* : La latence d'inférence des agents LLM (5 à 30 secondes) engendre des collisions systématiques avec les verrous transactionnels courts des API marchandes.
- **Correctif formel direct** :
  Intégrer au § 10.1.4 et au § 10.4 la modélisation formelle d'un schéma de réservation temporaire (`Commit-Hold Scheme`) :
  > « L'Intent Mandate doit être géré via un schéma de réservation temporaire auprès du compte émetteur. Chaque Cart Mandate doit poser un verrou logique sur une fraction de l'enveloppe budgétaire avant de pouvoir être transformé en Payment Mandate, tout échec aval déclenchant une transaction de compensation libérant le solde réservé. »

---

### DEF-PROT-12 [Majeur / Rigueur cryptographique] Vulnérabilité d'usurpation de l'Agent Card statique A2A et carence de Preuve de Possession
- **Sévérité** : Majeur / Lacune de sécurité cryptographique et d'alignement normatif IETF.
- **Localisation précise** : Chapitre 8, page 97, § 8.4.2 (`page-97.png`) et Chapitre 12, page 144, lignes 12002-12020.
- **Diagnostic causal approfondi** :
  Le compendium salue la signature des Agent Cards dans A2A v1.0. Mais une carte signée est un document statique accessible publiquement (`/.well-known/agent.json`). Le compendium omet de signaler la vulnérabilité d'usurpation par rejeu (*Impersonation / Credential Replay*) : la simple détention d'une carte signée ne prouve nullement que l'entité qui émet la requête réseau est le titulaire de la clé privée associée au domaine déclaré.
- **Correctif formel direct** :
  Imposer au protocole A2A un profil de Preuve de Possession (RFC 9449 DPoP ou RFC 9421 HTTP Message Signatures) :
  > « L'Agent Card signée partage la faiblesse du modèle porteur (Bearer) : quiconque l'intercepte peut s'en prévaloir. Pour garantir l'attribution non répudiable, l'architecture d'entreprise doit impérativement astreindre les protocoles A2A et MCP à une preuve de possession au niveau applicatif (DPoP RFC 9449 ou signatures HTTP RFC 9421). Chaque message doit comporter une preuve cryptographique éphémère signée par la clé privée du demandeur, neutralisant toute tentative de rejeu hors bande. »

---

### DEF-PROT-13 [Majeur / Systèmes distribués] Absence de consensus distribué dans A2A et fausse équivalence d'interaction (MCP Tasks vs A2A Tasks)
- **Sévérité** : Majeur / Lacune de modélisation en systèmes distribués.
- **Localisation précise** : Chapitre 8, pages 96-98 (§ 8.4) et Chapitre 9, page 101 (§ 8.6.2 & § 8.6.3).
- **Diagnostic causal approfondi** :
  1. *Absence de consensus et d'idempotence dans le cycle de vie des tâches A2A* : Le protocole A2A définit un automate d'états de tâche (`submitted`, `in-progress`, `requires-input`, `completed`, `canceled`). Cependant, en cas de partition réseau entre agents autonomes inter-entreprises, A2A ne propose aucune horloge logique vectorielle, aucun identifiant d'idempotence native, ni aucun protocole de réconciliation pour traiter les transitions concurrentes (ex: l'agent mandant émet `cancel` pendant que le délégataire exécute `complete`).
  2. *Fausse équivalence entre MCP Tasks et A2A Tasks* : Qualifier les tâches asynchrones de MCP d'« empiètement sur le terrain de la délégation d'A2A » (p. 101) repose sur une confusion informatique entre deux patrons de calcul :
     - **MCP Tasks** est un modèle **RPC asynchrone asymétrique (client-serveur)** : l'hôte garde le contrôle total de l'orchestration et surveille un job passif d'arrière-plan.
     - **A2A Tasks** est un modèle de **délégation d'acteur autonome pair-à-pair** : l'agent délégataire dispose de sa propre boucle cognitive, d'un raisonnement opaque, et d'un pouvoir d'arbitrage sur l'atteinte du but.
- **Correctif formel direct** :
  Restituer la frontière conceptuelle exacte au § 8.6.2 : MCP Tasks relève du calcul différé (*deferred batch job*), tandis qu'A2A relève de la négociation d'objectifs entre pairs autonomes. Documenter l'absence de primitives de consensus distribué dans A2A comme une limite majeure pour les échanges contractuels inter-organisations.

---

### DEF-PROT-14 [Majeur / Ingénierie protocolaire] Cadrage d'E/S (I/O Framing) et corruption du parseur JSON-RPC 2.0 sur le transport stdio de MCP
- **Sévérité** : Majeur / Erreur d'ingénierie protocolaire.
- **Localisation précise** : Chapitre 8, page 92, Tableau 8.2 et § 8.1.3 (`page-92.png`).
- **Diagnostic causal approfondi** :
  L'analyse du transport d'entrée-sortie standard (stdio) présente ce mode comme un couplage fort de cycle de vie partagé, mais omet l'élément de robustesse le plus critique : l'étanchéité du cadrage de trame (*Frame Delimitation*) en NDJSON (Newline Delimited JSON).
  Dans les runtimes d'exécution de serveurs MCP (Python, Node.js, Go), de multiples bibliothèques tierces (drivers DB, CUDA, PyTorch) écrivent spontanément des messages de log, bannières ou warnings directement sur `stdout`. Or, sur le transport stdio, `stdout` est le canal exclusif de multiplexage des trames JSON-RPC. L'émission d'un seul octet non JSON ou d'un saut de ligne intempestif corrompt immédiatement l'état du parseur de l'hôte (`Parse Error -32700`), provoquant la rupture immédiate de la communication IPC ou un blocage en lecture.
- **Correctif formel direct** :
  Ajouter au § 8.1.3 la règle d'isolation industrielle :
  > « Sanctuarisation absolue de stdout : le transport stdio impose une discipline d'E/S stricte. Le descripteur `stdout` est réservé exclusivement aux trames JSON-RPC délimitées par `\n`. Toute journalisation, diagnostic ou trace doit obligatoirement être déroutée vers `stderr`. Tout manquement à cette séparation entraîne la désynchronisation irréversible du parseur de l'hôte. »

---

### DEF-PROT-15 [Majeur / Modélisation des erreurs] Confusion entre erreurs protocolaires JSON-RPC et erreurs fonctionnelles d'outils (`isError: true`)
- **Sévérité** : Majeur / Lacune d'architecture logicielle.
- **Localisation précise** : Chapitre 8, page 93, § 8.1.4 et page 94, § 8.2.3.
- **Diagnostic causal approfondi** :
  Le texte traite de la sémantique des résultats mais omet la dichotomie essentielle de la spécification MCP relative au traitement des erreurs :
  1. Une erreur de bas niveau protocolaire (syntaxe JSON invalide, méthode RPC inexistante) doit générer un objet d'erreur standard JSON-RPC 2.0 (`{"error": {"code": -32601, ...}}`), ce qui signale une défaillance de tuyauterie et interrompt le dialogue.
  2. En revanche, un échec fonctionnel d'exécution d'un outil (paramètre invalide, ressource non trouvée, solde insuffisant) ne DOIT PAS renvoyer une erreur JSON-RPC. Il doit être retourné sous la forme d'un objet de succès (`result`) contenant le fanion `isError: true` et un contenu textuel explicatif.
  Cette dissociation est cruciale : renvoyer `isError: true` dans le `result` permet d'injecter la cause de l'échec directement dans la fenêtre de contexte du LLM, activant sa capacité d'auto-correction cognitive (*self-healing loop*), alors qu'une erreur JSON-RPC protocolaire disjoncte le runtime client.
- **Correctif formel direct** :
  Insérer la clarification dans le § 8.2.3 pour guider correctement l'implémentation des serveurs MCP d'entreprise.

---

### DEF-PROT-16 [Majeur / Sécurité cognitive] Faille du Human-In-The-Loop par opacité sémantique face à l'injection indirecte transitive
- **Sévérité** : Majeur / Vulnérabilité de conception de sécurité.
- **Localisation précise** : Chapitre 11, pages 130-131 (§ 11.1.3) et page 134 (§ 11.2.2).
- **Diagnostic causal approfondi** :
  Le texte analyse l'injection indirecte et positionne l'approbation humaine (*Human-in-the-Loop*, HITL) comme mesure d'atténuation. Toutefois, il ignore la vulnérabilité du « mandataire confus induit par l'interface » (*HITL Blind Approval*) :
  Lorsqu'un agent est manipulé par injection indirecte, il génère un appel d'outil malveillant dont la charge nuisible est masquée au sein d'arguments techniques complexes, volumineux ou obfusqués. Les interfaces d'approbation humaine actuelles se bornant à afficher les paramètres bruts, l'opérateur humain valide l'action sans en comprendre les implications réelles, légitimant l'attaque.
- **Correctif formel direct** :
  Stipuler au § 11.4 qu'un contrôle HITL n'est efficace que s'il est précédé d'un moteur déterministe de projection d'impact (*Impact Projection Engine*) traduisant les paramètres techniques en effets de bord métiers explicites, indépendamment de toute synthèse formulée par le LLM potentiellement compromis.

---

### DEF-PROT-17 [Majeur / Systèmes distribués] Omission du théorème CAP, des fenêtres de latence de révocation et des attaques Sybil dans les registres distribués
- **Sévérité** : Majeur / Lacune d'analyse des systèmes distribués (Axe R2).
- **Localisation précise** : Chapitre 9, pages 104-105, § 9.1.4 et § 9.1.5.
- **Diagnostic causal approfondi** :
  Le Chapitre 9 vante les annuaires distribués d'agents basés sur des tables de hachage distribuées (DHT) et réseaux fédérés pair-à-pair, en préconisant la « révocation coordonnée ». Cependant, l'analyse ignore les théorèmes distribués fondamentaux (CAP / PACELC) :
  1. Une DHT fonctionne en consistance éventuelle : la propagation d'une révocation d'Agent Card ou de clé compromise prend un temps $\Delta t_{\text{prop}}$. Durant cette fenêtre, un agent délégataire continue de transiger avec un nœud révoqué en toute bonne foi.
  2. Les registres DHT ouverts sans mécanisme de preuve de travail ou barrière de caution économique (*slashing / stake*) sont vulnérables aux attaques Sybil et à l'empoisonnement de routage des capacités d'agents.
- **Correctif formel direct** :
  Compléter le § 9.1.5 en précisant que pour les flux financiers d'entreprise, la découverte sur DHT à consistance éventuelle est impropre ; l'architecture doit s'appuyer sur des registres à consistance forte adossés à des journaux de transparence immuables (*Transparency Logs*).

---

### DEF-PROT-18 [Majeur / Méthodologie critique] Biais d'évaluation asymétrique entre MCP et A2A par confusion entre absence de CVE et sûreté
- **Sévérité** : Majeur / Biais d'évaluation méthodologique.
- **Localisation précise** : Chapitre 11, page 132 (§ 11.1.4) et page 138 (Tableau 11.5).
- **Diagnostic causal approfondi** :
  L'ouvrage applique une grille de lecture asymétrique injustifiée : le protocole MCP est décortiqué à l'aide de nombreuses CVE (CVE-2025-6514, CVE-2025-49596, exposition de serveurs non authentifiés), tandis que le protocole A2A est exonéré d'analyse de menaces sous prétexte qu'« aucune attaque propre au protocole agent-agent n'est au corpus ».
  Cette absence de CVE résulte uniquement du stade de déploiement en atelier fermé d'A2A. Les vecteurs d'attaque sur la communication inter-agents (déni de service par bouclage de tâches récursives, injection dans le contexte partagé multi-tours, falsification de l'Agent Card par empoisonnement DNS) sont formellement documentés dans la recherche contemporaine (AgentDojo, OWASP Agentic).
- **Correctif formel direct** :
  Compléter la cinquième ligne du Tableau 11.5 en y inscrivant les menaces théoriques formellement identifiées sur la délégation inter-agents.

---

### DEF-PROT-19 [Majeur / Architecture de l'ouvrage] Surqualification disproportionnée du projet AGNTCY au Chapitre 10
- **Sévérité** : Majeur / Déséquilibre structurel de composition.
- **Localisation précise** : Chapitre 10, page 115 (titre) et pages 118-120 (§ 10.2).
- **Diagnostic causal approfondi** :
  Le projet d'infrastructure AGNTCY est promu dans le titre même du Chapitre 10 à parité avec AP2, MCP et A2A. Pourtant, le texte concède aux pages 119-120 qu'il s'agit d'une coquille documentaire vide dans le corpus analysé : ni spécification publique analysable, ni version stable, ni implémentation open-source examinée, et incapacité à expliciter sa propre composante ACP (renvoyée au Ch. 49).
- **Correctif formel direct** :
  Rétrograder AGNTCY au rang d'illustration industrielle exploratoire au sein du § 9.2, et rebaptiser le Chapitre 10 : « 10 · Transaction et infrastructure : AP2 et les couches d'acheminement agentique ».

---

### DEF-PROT-20 [Majeur / Lacune architecturale] Réduction erronée de Cisco AGNTCY : occultation du routage d'overlay sémantique et de l'isolation multi-tenant (BSIF E-23 / Loi 25)
- **Sévérité** : Majeur / Lacune architecturale.
- **Localisation précise** : Chapitre 10, page 119, § 10.2.2 (lignes 9830-9851).
- **Diagnostic causal approfondi** :
  Le manuscrit se réfugie sous l'étiquette commode d'« absence de documentation (degré 3) » pour éluder l'analyse architecturale du projet open source AGNTCY (Cisco / Linux Foundation) :
  1. *Routage en réseau superposé (Overlay Mesh)* : Les agents s'exécutent dans des conteneurs éphémères aux adresses IP changeantes. AGNTCY implémente un routage sémantique fondé sur les descripteurs de capacités déclarés (*Capability-Based Routing*), découplé des sous-réseaux IP sous-jacents.
  2. *Cloisonnement multi-tenant et micro-segmentation agentique* : Dans les institutions financières réglementées (directives BSIF E-23, Loi 25), des agents appartenant à des juridictions ou départements distincts ne peuvent communiquer en clair. AGNTCY positionne des passerelles d'agents (*Agent Gateways*) opérant comme des points de contrôle d'accès réseau (*Policy Enforcement Points* - PEP).
  3. *Overhead cryptographique et point de défaillance unique* : Le protocole SLIM superpose du chiffrement de bout en bout avec vérification des signatures à chaque nœud relais, induisant un surcoût de latence critique. De plus, la passerelle constitue un point de défaillance unique : sa compromission expose les charges utiles non chiffrées en mémoire partagée.
- **Correctif formel direct** :
  Supprimer la déclaration de carence documentaire et formaliser la matrice de routage de passerelle d'infrastructure AGNTCY :
  $$R_{\text{AGNTCY}} : \big(\text{CapabilityDescriptor},\, \text{TenantID},\, \text{Proof}_{\text{DID}}\big) \longrightarrow \text{Gateway}_{\text{Target}}\big(\text{Endpoint}_{\text{mTLS}},\, \text{SLIM-Channel}\big)$$

---

### DEF-PROT-21 [Majeur / Lacune méthodologique] Impasse de la délégation récursive dans OAuth : limites formelles du Token Exchange (RFC 8693) et omission des capacités cryptographiques atténuables hors-ligne
- **Sévérité** : Majeur / Lacune méthodologique.
- **Localisation précise** : Chapitre 12, pages 141-144, § 12.1 et § 12.2.
- **Diagnostic causal approfondi** :
  Le chapitre 12 critique l'inadaptation d'OAuth aux agents en centrant son réquisitoire sur le flux interactif (§ 4.1 du RFC 6749) et l'absence d'humain devant l'écran, omettant d'instruire le standard spécifiquement conçu par l'IETF pour la délégation inter-services : le **RFC 8693 (OAuth 2.0 Token Exchange)**.
  Or, c'est précisément dans le RFC 8693 que se révèlent les limites structurelles d'OAuth face aux systèmes multi-agents :
  1. *Centralisation et latence synchrone* : Tout échange de jeton (`subject_token` $\to$ nouveau jeton) requiert un aller-retour réseau synchrone vers le serveur d'autorisation central (AS). Dans une chaîne de délégation récursive multi-sauts ($A_1 \to A_2 \to \dots \to A_n$), ce goulot d'étranglement paralyse les performances.
  2. *Impossibilité d'atténuation cryptographique locale* : Le RFC 8693 ne permet pas à un agent intermédiaire d'atténuer lui-même les privilèges d'un jeton sans solliciter l'AS.
  3. *Vulnérabilité au mandataire confus récursif (Recursive Confused Deputy)* : La traçabilité de l'intention initiale est perdue au fil des réémissions de jetons intermédiaires.
- **Correctif formel direct** :
  Intégrer une analyse comparative opposant le RFC 8693 aux architectures de capacités cryptographiques atténuables hors-ligne (*Macaroons*, *UCAN* / *W3C Verifiable Credentials*) :
  $$\text{Capabilité}_{i+1} = \text{HMAC}\big(\text{Capabilité}_i,\, \text{Restriction}_{i+1}\big)$$
  démontrant que les architectures d'agents autonomes requièrent des jetons auto-atténuables localement sans dépendance synchrone à un serveur central.

---

### DEF-PROT-22 [Majeur / Lacune méthodologique] Incompatibilité structurelle et temporelle de SCIM (RFC 7643 / RFC 7644) face au cycle de vie hautement volatil et non tracé des agents stochastiques
- **Sévérité** : Majeur / Lacune méthodologique.
- **Localisation précise** : Chapitre 12, pages 141-143, § 12.1 (lignes 11904-11922) et Tableau 12.1 (p. 144).
- **Diagnostic causal approfondi** :
  L'auteur formule une critique purement lexicale et sémantique de SCIM (l'absence de ressource « Agent » et le vocabulaire orienté ressources humaines comme `employeeNumber`). Cette critique passe à côté du véritable obstacle d'ingénierie :
  1. *Incompatibilité des ordres de grandeur temporels* : SCIM (RFC 7644) est un protocole HTTP/REST synchrone taillé pour des mouvements d'identités humaines sur des échelles de jours ou d'heures ($\Delta t \sim 10^3 \text{ à } 10^5\text{ s}$). Les agents autonomes de traitement de tâches sont instanciés de façon éphémère pour des durées de vie de quelques secondes ($\tau \sim 10^{-1} \text{ à } 10^1\text{ s}$) et peuvent être répliqués par milliers. Gérer ce cycle de vie par des requêtes SCIM `POST /Users` et `DELETE /Users/{id}` entraîne l'effondrement immédiat des annuaires d'entreprise.
  2. *Absence d'immuabilité et d'auditabilité forensique* : Une mutation d'état dans SCIM (`PATCH`) écrase les attributs précédents sans consigner de preuve d'état signée. Or, la traçabilité réglementaire (BSIF E-23) exige de certifier avec précision quelle version du modèle, quel prompt système et quelles autorisations étaient en vigueur lors de l'exécution d'une transaction financière à un instant $t$.
- **Correctif formel direct** :
  Rejeter les propositions d'extension artificielle de SCIM pour la gestion des cycles de vie d'agents. Préconiser des architectures d'annuaires de capacités adossées à des journaux de transparence immuables et cryptographiquement vérifiables (*Transparency Logs* / Sigstore Rekor).

---

### DEF-PROT-23 [Majeur / Lacune d'intégration financière] Incompatibilité et absence totale d'articulation entre AP2 et les standards de messagerie financière réglementée (ISO 20022 : pain.001, pacs.008, camt.056)
- **Sévérité** : Majeur / Lacune d'intégration financière.
- **Localisation précise** : Chapitre 10, page 118, § 10.1.4 (lignes 9774-9782) et pp. 121-124.
- **Diagnostic causal approfondi** :
  L'ouvrage annonce en sous-titre le déploiement d'agents « en services financiers réglementés (2024-2032) ». Or, dans l'infrastructure bancaire moderne d'entreprise (au Canada avec Lynx et le Real-Time Rail RTR de Paiements Canada, aux États-Unis avec FedNow, et en Europe avec SEPA Instant), le standard normatif pivot obligatoire est **ISO 20022**.
  Le manuscrit abandonne toute articulation entre AP2 et ISO 20022 en invoquant un « degré 3 » d'absence de documentation :
  - Aucun mapping formel des mandats AP2 (`Payment Mandate`) vers les messages d'initiation de virement ISO 20022 `pain.001.001.12` ;
  - Aucun schéma de transport des identifiants cryptographiques d'agents (DIDs ou clés publiques) au sein des blocs d'identification des parties débitrices (`Dbtr/Id/OrgId/Othr/Id`) dans les messages interbancaires `pacs.008` ;
  - Aucun traitement des retours, rejets et annulations de paiements via les formats de notification `pacs.002` et `camt.056`.
  Ignorer ISO 20022 rend la pile AP2 totalement inopérante pour une institution financière régie par les normes du BSIF.
- **Correctif formel direct** :
  Insérer une spécification prescriptive de passerelle d'interopérabilité `AP2-to-ISO20022` :
  1. *Traduction du mandat* : Encapsulation du `Payment Mandate` signé dans le bloc documentaire de transport `SupplementaryData` (`Envlp`) d'un message `pain.001` ;
  2. *Identification d'agent* : Enregistrement du DID de l'agent mandataire dans la balise `Dbtr/PrvtId/Othr/Id` sous le scheme identifier `DID` ;
  3. *Gestion du cycle de vie* : Liaison des notifications d'exécution interbancaire `pacs.002` aux événements de clôture de tâche dans le cycle A2A.

---

### DEF-PROT-24 [Majeur / Lacune taxonomique et algorithmique] Incomplétude de la taxonomie des modes d'échec (Tableau 11.4) : omission de l'explosion récursive de sous-tâches (Fork Bomb) et absence d'algorithmes de détection d'interblocage (Wait-For Graph)
- **Sévérité** : Majeur / Lacune taxonomique et algorithmique.
- **Localisation précise** : Chapitre 11, page 133, Tableau 11.4 (`page-133.png`) et § 11.2.1.
- **Diagnostic causal approfondi** :
  Le Tableau 11.4 prétend établir la taxonomie exhaustive des échecs à la frontière interopérable, mais il présente des lacunes critiques :
  1. *Omission de l'explosion récursive de sous-tâches (Agentic Fork Bomb / Cascading Sub-task Proliferation)* : Lorsqu'un superviseur décompose des missions en sous-tâches déléguées à des pairs via A2A, une formulation sous-spécifiée pousse les sous-agents à engendrer récursivement des dizaines de descendants. Faute d'un compteur de sauts standardisé (`Max-Hops`) et d'un budget global de jetons partagé, l'infrastructure subit un déni de service interne auto-induit (*Self-Inflicted DoS*).
  2. *Traitement purement déclaratif de l'interblocage (Deadlock)* : Le tableau cite « l'interblocage de délégation — agents s'attendant mutuellement » comme étant « propre à cette section ». Or, le texte du chapitre ne fournit aucun modèle formel d'attente (absence de graphe d'attente *Wait-For Graph* - WFG), aucune vérification des conditions de Coffman, et aucun algorithme de prévention ou de rupture (pas d'estampilles de Lamport, pas de politiques Wound-Wait / Wait-Die).
  3. *Usage métaphorique du mot « verrou »* : Le terme « verrou » est utilisé 7 fois dans les chapitres 10 et 11 comme figure de style (« verrou du domaine », « verrou opérationnel »), sans jamais désigner un véritable mécanisme de synchronisation distribuée (*Distributed Lock Manager* via Raft ou Redis Redlock).
- **Correctif formel direct** :
  Compléter le Tableau 11.4 en intégrant :
  - **Mode 8 : Explosion récursive de sous-tâches (Fork Bomb)** — Rupture : borne d'épuisement de ressources distribuées. *Mitigation* : en-tête contextuel immuable `X-Agentic-Hop-Limit` décrémenté à chaque délégation et budget de calcul global plafonné.
  - Formaliser la détection d'interblocage multi-agents par la construction dynamique d'un graphe orienté d'attente $G = (V, E)$ où un cycle $A_1 \to A_2 \to \dots \to A_1$ déclenche l'interruption préemptive de la tâche la plus récente selon un ordonnancement d'estampilles temporelles strict (*Wait-Die Policy*).

---

### DEF-PROT-25 [Majeur / Sécurité protocolaire] Insécurité de l'état applicatif dans MCP révisé : exposition de jetons d'état opaques dans le canal de prompt non fiable sans schéma AEAD
- **Sévérité** : Majeur / Sécurité protocolaire.
- **Localisation précise** : Chapitre 8, page 92, Tableau 8.2 ; et Chapitre 11, page 135, § 11.3.1 (lignes 11286-11290).
- **Citation textuelle exacte** :
  > « [...] l’état applicatif migre vers des poignées frappées par le serveur et transmises comme arguments d’outil ordinaires, c’est-à-dire dans le canal même que le § 11.1 décrit comme non fiable. »
- **Diagnostic causal approfondi** :
  L'auteur observe pertinemment que la refonte de MCP sans état reporte la conservation d'état vers des « poignées d'outils » (*state handles*) réinjectées dans les arguments de prompt par le modèle.
  Toutefois, le manuscrit omet de formuler les exigences de durcissement cryptographique indispensables :
  1. *Falsification d'état (State Tampering)* : Si la poignée d'état n'est pas scellée et authentifiée cryptographiquement côté serveur, une injection indirecte dans le prompt peut amener le LLM à altérer les paramètres portés par la poignée (ex. identifiant d'entité, niveau de privilège).
  2. *Rejeu et confusion de contexte* : En l'absence d'horodatage strict et d'un nonce lié à l'instance, une poignée d'état valide interceptée peut être rejouée dans une session d'agent distincte.
- **Correctif formel direct** :
  Imposer dans les prescriptions d'architecture que toute poignée d'état transitant par un agent sur un transport sans état utilise impérativement le chiffrement authentifié avec données associées (AEAD) :
  $$\text{StateHandle} = \text{ChaCha20-Poly1305}_{K_{\text{serveur}}}\big(\text{Payload d'état}\big) \parallel \text{Tag d'authentification}$$
  garantissant qu'aucune manipulation par le LLM ou injection adverse ne puisse corrompre l'état de session conservé côté serveur.

---

### DEF-PROT-26 [Majeur / Erreur formelle de composition] Ruptures textuelles et phrases tronquées net à la page 79 (bloc Thèse et paragraphe introductif § 7.0)
- **Sévérité** : Majeur / Erreur formelle de composition.
- **Localisation précise** : Chapitre 7 (*Généalogie et gouvernance...*), page 79 du PDF (`page-79.png`), lignes 6496-6508 de `DOCUMENT_TEXT_MAP.md`.
- **Citation textuelle exacte** :
  > « [...] fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.
  > Le second mouvement du Livre s’ouvre ici. Les ch. 1 à 3 ont posé le socle pré-agentique ; les ch. 4 à 6, l’ingénierie de l’agent. Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses
  > La proposition directrice tient en un déplacement, et il vaut d’être énoncé avec précision [...] »
- **Diagnostic causal approfondi** :
  L'inspection de la page 79 révèle deux ruptures syntaxiques majeures de composition :
  1. *Fin de bloc Thèse corrompue* : La mention « instruit au ch. 10. » est immédiatement concaténée avec « outils, le dialogue entre agents... » sans transition, verbe ni articulation grammaticale.
  2. *Paragraphe suivant tronqué net* : La phrase se termine abruptement sur « — le contrat entre un agent et ses » sans aucun nom ni complément d'objet, avant de sauter directement à l'alinéa suivant (« La proposition directrice... »).
- **Correctif formel direct** :
  Rétablir la syntaxe complète des deux passages corrompus :
  1. Pour la fin du bloc Thèse : « [...] fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. Le présent mouvement analyse dès lors successivement l'accès aux outils, le dialogue entre agents, la découverte de services, le règlement commercial, et les modes d’échec qui leur sont propres. »
  2. Pour le paragraphe suivant : « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses pairs ainsi que son environnement d'outils. »

---

# Minor Corrections and Typos

Cette section répertorie l'ensemble des anomalies éditoriales, coquilles typographiques et imprécisions de vocabulaire relevées dans le segment.

### MIN-PROT-01 Fragment de texte orphelin au Chapitre 8 (p. 95)
- **Localisation** : Page 95, lignes 7790-7793 de `DOCUMENT_TEXT_MAP.md` (`page-95.png`).
- **Citation** : `« Revalidation du 30 juillet 2026 : la réserve ci-dessus a été validée par l’événement, et c’est le seul endroit de la somme où cela se produit. La révision »`
- **Diagnostic** : Deux mots orphelins terminent la ligne immédiatement au-dessus de la Figure 8.2 sans verbe ni ponctuation.
- **Correctif** : Supprimer le fragment `« La révision »` ou compléter la phrase avant la légende de la figure.

### MIN-PROT-02 Incohérence de maturité d'A2A v1.0 entre le Tableau 9.3 et le corps du texte
- **Localisation** : Page 107 (Tableau 9.3) vs pages 97, 100 et 114.
- **Diagnostic** : Le Tableau 9.3 qualifie A2A de « production ; version 1.0 stable », alors que la page 97 énumère quatre lacunes ouvertes non closes, que la page 100 concède une négociation purement implicite et que la page 114 admet l'absence de banc inter-fournisseurs.
- **Correctif** : Remplacer dans le tableau par : « production émergente / standard de fait sous réserve de validation inter-fournisseurs ».

### MIN-PROT-03 Troncature non explicitée du modèle formel LCIM (p. 80, Tableau 7.1)
- **Localisation** : Page 80, Tableau 7.1 et § 7.1.2.
- **Diagnostic** : Le compendium applique le modèle LCIM de Tolk & Muguira (2003) sur 5 niveaux (0 à 4), omettant les niveaux 5 et 6 (dynamique et conceptuel) sans préciser qu'il s'agit d'une adaptation compactée.
- **Correctif** : Expliciter en note infrapaginale que les niveaux 5 et 6 sont fusionnés au niveau pragmatique dans l'adaptation agentique.

### MIN-PROT-04 Précision terminologique sur les SVID SPIFFE (p. 141 vs p. 143)
- **Localisation** : Page 141 et page 143.
- **Diagnostic** : Le texte emploie indifféremment SVID et certificat X.509 sans rappeler qu'un SVID SPIFFE se décline soit en `X509-SVID`, soit en `JWT-SVID`.
- **Correctif** : Préciser `X509-SVID` à la page 143.

### MIN-PROT-05 Normalisation du genre de RFC 9207 (p. 94)
- **Localisation** : Chapitre 8, page 94, § 8.2.3.
- **Diagnostic** : Le texte mentionne « la RFC 9207 », alors que la norme terminologique de l'ouvrage utilise le masculin (« le RFC »), comme aux pages 144 et 146 (« le RFC 6749 », « le RFC 7643 »).
- **Correctif** : Remplacer par « le RFC 9207 ».

### MIN-PROT-06 Désignation imprécise du mécanisme d'identité d'AWS Bedrock (p. 143)
- **Localisation** : Chapitre 12, page 143, lignes 11932-11936 (`page-143.png`).
- **Citation** : `« Chez AWS, le mécanisme documenté comparable est Amazon Bedrock AgentCore Identity... »`
- **Diagnostic** : L'appellation commerciale officielle d'AWS est *Amazon Bedrock Agents* associé aux rôles IAM d'exécution (`IAM Execution Roles`), le terme « AgentCore Identity » provenant d'un amalgame d'éditeurs tiers.
- **Correctif** : Rectifier la désignation en précisant qu'AWS ne définit pas d'objet d'identité dédié, mais réutilise `sts:AssumeRole` avec balises de session (`aws:PrincipalTag`).

### MIN-PROT-07 Déplacement typographique discordant de la Figure 10.4 (p. 125)
- **Localisation** : Chapitre 10, page 125 (`page-125.png`).
- **Diagnostic** : La Figure 10.4 (*Le mandat comme couche de preuve opposable...*) est positionnée en tête de la page 125, au-dessus du titre de la section 10.5 (*Le destin de l'ACP protocolaire*), alors qu'elle illustre la section 10.4.2 située au bas de la page 124.
- **Correctif** : Forcer l'ancrage typographique de la figure immédiatement sous le texte du § 10.4.2.

### MIN-PROT-08 Espaces insécables manquants devant la ponctuation double
- **Localisation** : Chapitre 10, page 116 (§ 10.1.2) ; Chapitre 11, page 138 (Tableau 11.5).
- **Diagnostic** : Des signes de ponctuation doubles (deux-points, points-virgules) et des guillemets français (« ») ne comportent pas d'espace insécable fin, provoquant des retours à la ligne orphelins.
- **Correctif** : Appliquer systématiquement l'espace insécable conformément aux règles de composition du français canadien et québécois.

---

# 3. Inventaire Critique Bibliographique et État de l'Art 2026 (Axe R3)

L'audit de l'axe R3 impose de rectifier les hallucinations et lacunes normatives relevées dans le segment afin de sceller la conformité de l'ouvrage à l'état de l'art technologique et juridique de 2026.

```
+----------------------------------------------------------------------------------------------------------+
|                                    ÉTAT DE L'ART NORMATIF RÉCONCILIÉ 2026                                |
+------------------------------------+---------------------------------------------------------------------+
| Référence défaillante du texte     | Rectification normative et standard de référence 2026              |
+------------------------------------+---------------------------------------------------------------------+
| Prétendu « règl. (UE) 2026/1744 »   | Règlement (UE) 2024/1689 (AI Act) : application GPAI août 2025,     |
| (p. 124, 30520, 34016, 60726)      | Annexe III août 2026, Annexe I août 2027 (art. 111).                 |
+------------------------------------+---------------------------------------------------------------------+
| Jetons porteurs OAuth 2.0 (p. 144) | RFC 9449 OAuth 2.0 DPoP (Demonstrating Proof-of-Possession)         |
| (affaire Salesforce UNC6395)       | et RFC 8705 (MTLS Bound Tokens). Découplage intégrité cognitive.     |
+------------------------------------+---------------------------------------------------------------------+
| Aporie ACP IBM vs Cisco (p. 126)   | Séparation stricte des couches OSI :                                |
|                                    | - A2A v1.0 (Linux Foundation) = Data Plane applicatif L7            |
|                                    | - Cisco AGNTCY / SLIM = Control Plane L5 & Transport L4              |
+------------------------------------+---------------------------------------------------------------------+
| Absence doc. rails bancaires AP2   | ISO 20022 Financial Services Messaging :                           |
| (p. 118, « degré 3 »)              | - pain.001.001.12 (Credit Transfer Initiation avec mandats)        |
|                                    | - pacs.008.001.10 (FI to FI Customer Credit Transfer)               |
|                                    | - camt.056 / pacs.002 (Reversals & Payment Status Notifications)    |
|                                    | - Rails canadiens : Lynx (Gros montants) et RTR (Temps réel)        |
+------------------------------------+---------------------------------------------------------------------+
| Délégation OAuth interactive       | RFC 8693 (OAuth 2.0 Token Exchange) comparé aux                    |
| (RFC 6749 §4.1, p. 141)            | Capacités cryptographiques atténuées hors-ligne (Macaroons / UCAN)  |
+------------------------------------+---------------------------------------------------------------------+
| SCIM pour agents (RFC 7643/7644)   | Rejet de SCIM face aux agents éphémères ;                           |
| (p. 141, CSA Labs 2026)            | Adoption de Transparency Logs immuables (Sigstore Rekor)           |
+------------------------------------+---------------------------------------------------------------------+
| MCP révisé « sans état » (p. 92)   | Spécification MCP 2026-07-28 :                                      |
|                                    | - Idempotency-Key obligatoire sur toute méthode à effet de bord     |
|                                    | - State Handles chiffrés en ChaCha20-Poly1305 (AEAD)                |
|                                    | - Sanctuarisation absolue de stdout pour le cadrage NDJSON          |
+------------------------------------+---------------------------------------------------------------------+
| Consensus byzantin PBFT (p. 133)   | Cadre BFT stochastique : consensus sur invariants logiques formels  |
|                                    | vérifiables par solveurs SMT, sous hétérogénéité prouvée des LLM.   |
+------------------------------------+---------------------------------------------------------------------+
```

---

# 4. Recommandations Impératives de Réécriture pour les Chapitres 7 à 11

Pour conférer à la somme la rigueur indispensable à un compendium d'ingénierie financière de haut vol, les réécritures suivantes doivent être exécutées sans délai :

1. **Chapitre 7 : Réparation textuelle et ancrage formel**
   - Rétablir immédiatement la phrase tronquée de la thèse et de l'introduction à la page 79.
   - Insérer une note au § 7.1.2 explicitant la troncature du modèle LCIM de Tolk & Muguira à 5 niveaux pour les besoins de l'architecture agentique.

2. **Chapitre 8 : MCP et A2A — Rigueur transactionnelle et sécurité**
   - Reformuler la proposition combinatoire de la page 90 : distinguer explicitement la réduction syntaxique $O(N+M)$ du coût d'adaptation pragmatique $O(N \times M)$ face à des modèles de fondation hétérogènes.
   - Corriger le Tableau 8.2 et le § 8.1.3 : supprimer l'affirmation d'un « déploiement à tourniquet sans couplage résiduel », imposer la spécification d'un en-tête d'idempotence (`Idempotency-Key`) pour tout appel d'outil modifiant l'état, et édicter la règle d'isolation absolue de `stdout` sur transport stdio.
   - Intégrer un encadré de sécurité au § 8.1.2 condamnant la dépréciation des racines (`roots`) comme vecteur d'évasion de bac à sable (*Path Traversal*) sans confinement physique au niveau de l'OS.
   - Distinguer au § 8.2.3 les erreurs de protocole JSON-RPC des erreurs fonctionnelles retournées avec `isError: true`.

3. **Chapitre 9 : Registres et découverte — Cohérence des états distribués**
   - Compléter l'analyse des annuaires distribués (DHT) au § 9.1.5 par les limites du théorème CAP et la modélisation des fenêtres de vulnérabilité lors de la révocation de clés.
   - Harmoniser la maturité déclarée d'A2A v1.0 dans le Tableau 9.3 avec les réserves formulées dans le corps du texte.

4. **Chapitre 10 : Transactions et AP2 — Refonte structurelle**
   - Corriger immédiatement le bogue de composition de la page 115 (ressouder « ce chapitre prend pour objet » et supprimer la duplication textuelle).
   - Réfuter l'aporie ACP du § 10.5.3 en établissant la séparation nette entre le Data Plane applicatif L7 (A2A) et le Control Plane réseau L4/L5 (Cisco AGNTCY).
   - Requalifier AP2 comme protocole de mandat et non de transaction, et formaliser le patron Saga distribué compensatoire indispensable aux opérations financières.
   - Réfuter la promesse de non-répudiation des pages 124-125 face à l'injection d'invite, en rappelant les exigences légales de contrôle exclusif du mandant (LCCJTI art. 28, eIDAS art. 26).
   - Purger la citation fictive du « règl. (UE) 2026/1744 » à la page 124 et aligner le calendrier sur l'art. 111 du Règlement (UE) 2024/1689.
   - Remplacer l'aveu de « degré 3 » d'absence de documentation financière par une spécification prescriptive de passerelle vers la messagerie ISO 20022 (`pain.001`, `pacs.008`) pour les rails bancaires d'entreprise.

5. **Chapitre 11 : Modes d'échec et consensus distribué**
   - Compléter la taxonomie du Tableau 11.4 par le mode 8 : l'explosion récursive de sous-tâches (*Agentic Fork Bomb*) avec mitigation par compteur immuable de sauts (`X-Agentic-Hop-Limit`).
   - Remplacer l'usage métaphorique de l'interblocage par un modèle algorithmique fondé sur le graphe d'attente (*Wait-For Graph*) et les politiques de rupture temporelle (*Wait-Die*).
   - Rectifier l'analogie BFT de la page 133 en démontrant l'incompatibilité de PBFT classique face aux sorties non identiques bit-à-bit et aux pannes corrélées en mode commun des modèles de fondation.

6. **Chapitre 12 : Identités étirées et autorisation**
   - Réécrire le § 12.2 et le Tableau 12.1 pour intégrer les normes IETF de preuve de possession RFC 9449 (DPoP) et RFC 8705 (MTLS), en démontrant que la crise d'OAuth face aux agents découle de l'absence de vérification de l'intégrité cognitive du modèle et non d'une faiblesse du jeton porteur.
   - Instruire le standard RFC 8693 (Token Exchange) et documenter ses limites face aux capacités atténuées hors-ligne (Macaroons / UCAN).
   - Démontrer l'inadéquation temporelle ($\Delta t$) de SCIM face au cycle de vie volatil des agents stochastiques.
