# RAPPORT D'AGRÉGATION ET D'ÉVOLUTION CONTRADICTOIRE — NIVEAU 1 / AGRÉGATEUR 2
## Segment : `segment_livre_1_protocoles` (Pages 78 à 145 — Chapitres 7 à 12)
### Candidats audités : Candidat 3 (`handoff_3.md`) et Candidat 4 (`handoff_4.md`)
**Date d'évaluation** : 2026-11-03  
**Auteur** : Agrégateur de Revue 2 (Niveau 1 — `worker_protocoles_1_2`)  
**Périmètre couvert** : Livre I (Chapitres 7 à 11) et Livre II (Chapitre 12), pp. 78 à 145 : Standards ouverts (MCP, A2A), Découverte et registres, Protocoles transactionnels (AP2, AGNTCY, x402, MPP), Modes d'échec et taxonomie des risques protocolaires, et Identités non humaines étirées (OAuth 2.0, OIDC, SCIM, SPIFFE).

---

# TABLEAU DE CONVERGENCE ET ARBITRAGE CONTRADICTOIRE (NIVEAU 0 $\to$ NIVEAU 1)

| Thématique / Constat d'audit | Position Candidat 3 | Position Candidat 4 | Arbitrage et Évolution (Niveau 1) |
| :--- | :--- | :--- | :--- |
| **Bogue d'édition majeur à la page 115** | [Minor] Traité comme coquille de composition. | [Critical] Traité comme corruption matérielle bloquante. | **Arbitré [Critical] (Bloquant éditorial)** : Mot « chapitre » tronçonné en deux (« ce cha ... pitre ») et duplication textuelle mot à mot de la thèse. Inadmissible dans un compendium financier de référence. |
| **Aporie sur l'homonymie « ACP » (IBM vs Cisco)** | [Minor] Simple ambiguïté terminologique. | [Critical] Fausse aporie épistémologique et confusion de couches OSI. | **Arbitré [Critical] (Erreur formelle)** : Confusion inacceptable entre le Data Plane applicatif L7 (IBM BeeAI / A2A) et le Control Plane réseau L4/L5 (Cisco AGNTCY / SLIM). L'abstention de l'auteur est injustifiée. |
| **Absence de formalisme transactionnel dans AP2** | [Critical] Démonstration formelle (PACELC, ACID, Saga, absence de compensation). | Non traité directement (focalisé sur OAuth/AGNTCY). | **Arbitré [Critical] (Erreur formelle majeure)** : Intégration prioritaire de la preuve du Candidat 3. AP2 n'est pas un protocole transactionnel mais une simple chaîne statique d'attestations W3C VC sans atomicité. |
| **Rupture de la non-répudiation (AP2 vs Prompt Injection)** | [Critical] Contradiction p. 123 vs p. 124 ; anéantissement du contrôle exclusif. | [Critical] Mentionné via DPoP et intégrité cognitive. | **Arbitré [Critical] (Erreur formelle juridique et cryptographique)** : Incompatibilité formelle avec le droit de la preuve électronique (LCCJTI art. 28, eIDAS art. 26). La signature d'un agent injecté ne prouve aucun consentement du mandant. |
| **Idempotence financière et réémission MCP sans état** | [Critical] Risque de double débit financier par perte de stream. | [Major] Suppression de reprise de flux sans Idempotency-Key. | **Arbitré [Critical] (Bloquant architectural)** : Convergence unanime. Renvoi désinvolte au ch. 48 inadmissible face à une couche de paiement HTTP/JSON-RPC sans état. |
| **Crise d'OAuth 2.0 face aux agents (DPoP RFC 9449)** | Non traité (focalisé sur AP2/MCP). | [Critical] Omission des RFC 9449 / 8705 ; méprise sur la racine de la crise. | **Arbitré [Critical] (Erreur formelle et omission de l'état de l'art IETF)** : Démontre que le problème d'OAuth n'est pas le Bearer Token (résolu par DPoP), mais le découplage entre autorisation d'API et intégrité cognitive de l'agent. |
| **Tolérance aux pannes byzantines (PBFT p. 133)** | Non traité. | [Critical] Invalidation mathématique par les pannes en mode commun. | **Arbitré [Critical] (Erreur formelle mathématique)** : Violation de l'hypothèse d'indépendance statistique des nœuds dans les LLM partageant des fondations et des contextes communs. |
| **Architecture réseau Cisco AGNTCY** | Non traité. | [Critical] Réduction erronée à un transport ; omission du routage d'overlay. | **Arbitré [Major] (Lacune architecturale)** : Qualification rigoureuse de la topologie réseau, de la micro-segmentation multi-tenant (BSIF E-23) et de la surface d'attaque des passerelles. |
| **Inadéquation de SCIM (RFC 7643 / 7644)** | Non traité. | [Major] Incompatibilité d'échelle temporelle ($\Delta t$) et absence d'immuabilité. | **Arbitré [Major] (Lacune méthodologique)** : Dépasse la critique lexicale de l'auteur en prouvant l'incompatibilité des rythmes d'instanciation des agents éphémères. |
| **Limites de la délégation OAuth (RFC 8693)** | Non traité. | [Major] Token Exchange centralisé vs capacités atténuables hors-ligne. | **Arbitré [Major] (Lacune méthodologique)** : Analyse comparative avec Macaroons / UCAN et vulnérabilité au mandataire confus récursif. |
| **Articulation AP2 avec ISO 20022 (Lynx / RTR)** | [Major] Incompatibilité avec les rails bancaires d'entreprise. | Non traité. | **Arbitré [Major] (Lacune d'intégration financière)** : L'abandon en « degré 3 » d'ISO 20022 (`pain.001`, `pacs.008`) rend la pile inapplicable en finance canadienne réglementée. |
| **Concurrence multi-agents et interblocages** | [Major] Absence de verrous distribués et de Wait-For Graph. | [Major] Omission des Fork Bombs et des courses budgétaires. | **Arbitré [Major] (Lacune taxonomique et algorithmique)** : Consolidation des deux critiques sur les défaillances de concurrence du Tableau 11.4. |
| **Insécurité des poignées d'état (State Handles) MCP** | [Major] Jetons d'état dans le prompt sans schéma AEAD scellé. | Non traité directement. | **Arbitré [Major] (Vulnérabilité protocolaire)** : Risque de falsification d'état et d'attaque par rejeu via injection indirecte. |
| **Accidents d'édition textuelle à la page 79** | Non traité. | [Major] Rupture grammaticale dans le bloc Thèse. | **Arbitré [Major] (Erreur formelle de composition)** : Découverte additionnelle au Niveau 1 d'une seconde coupure nette dans le paragraphe suivant (« le contrat entre un agent et ses »). |

---

# I. CONSTATS BLOQUANTS / ERREURS FORMELLES & THÉORIQUES [CRITICAL]

## 1. [Critical] [Bloquant éditorial & Corruption textuelle] Bogue de composition typographique à la page 115 : mot coupé (« ce cha ... pitre »), rupture syntaxique et duplication textuelle de la thèse
- **Sévérité** : [Critical] [Bloquant / Erreur formelle d'édition]
- **Localisation précise** : Chapitre 10 (*Transaction et infrastructure : AP2 et AGNTCY*), page 115 du PDF (`page-115.png`), lignes 9484 à 9507 de `DOCUMENT_TEXT_MAP.md`. Citation textuelle exacte :
  > « [...] La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce cha
  > Thèse — que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur — le socle établit qu’AP2 est un protocole compagnon d’A2A, rien de plus sur sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet, une déclaration et non un fait vérifié, que des analyses tierces nuancent. pitre prend pour objet. Que la transaction agentique constitue l’aboutissement financier de la pile protocolaire est une lecture d’auteur : les sources établissent que le protocole de paiement est un protocole compagnon de l’axe agent-agent, dédié aux transactions pilotées par agents, et rien de plus sur sa centralité. Qu’AGNTCY soit une couche d’infrastructure et non un concurrent est, pour sa part, le positionnement officiel déclaré du projet — une déclaration, non un fait vérifié, et que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux n’est un fait établi. »
- **Diagnostic causal approfondi** :
  L'inspection directe de la page 115 démontre un accident de composition logicielle (LaTeX/Pandoc) survenu lors de l'insertion de la boîte flottante de thèse :
  1. *Scission morphologique d'un mot* : Le mot « chapitre » est tronçonné en deux fragments étanches : le radical « ce cha » termine la ligne précédant l'encadré, tandis que le suffixe « pitre prend pour objet. » est réinjecté au beau milieu du paragraphe suivant, immédiatement après le mot « nuancent. ».
  2. *Bégaiement textuel intégral* : Le paragraphe succédant immédiatement à la boîte de thèse reprend quasi mot pour mot le contenu même de la thèse (« Que la transaction agentique constitue l'aboutissement financier... »), créant une redondance tautologique et désastreuse dans l'ouverture d'un chapitre pivot de la somme.
- **Correctif formel** :
  Restructurer l'entrée du chapitre 10 en supprimant la duplication et en ressoudant la phrase introductive :
  ```markdown
  La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce chapitre prend pour objet.

  Thèse — Que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur : le socle établit qu’AP2 est un protocole compagnon d’A2A, sans préjuger de sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet — une déclaration d'intention et non un fait vérifié, que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux ne constitue un fait établi.
  ```

---

## 2. [Critical] [Bloquant / Erreur formelle & Confusion de couches] Fausse aporie sur la collision terminologique « ACP » : confusion entre le Data Plane applicatif L7 (IBM BeeAI / A2A) et le Control Plane réseau L4/L5 (Cisco AGNTCY)
- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 10, pages 126-127, § 10.5.3 (*Le versant protocolaire de la collision terminologique*), et Chapitre 7, page 87, Tableau 7.3 ligne (d) et encadré § 7.5 (`page-87.png`, `page-126.png`, `page-127.png`). Citation textuelle exacte :
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
- **Correctif formel** :
  Réfuter l'alternative d'indécidabilité du § 10.5.3. Clarifier l'étagement des responsabilités selon le modèle des plans réseau :
  $$\text{Architecture Globale} = \begin{cases} \mathbf{Plan\ Applicatif\ (Couche\ 7)} : & \text{A2A v1.0 (absorbant l'ACP-IBM pour le transport des charges utiles d'intention)} \\ \mathbf{Plan\ de\ Contr\hat{o}le\ R\acute{e}seau\ (Couche\ 5)} : & \text{ACP-Cisco AGNTCY (signalisation, routage de passerelles et annuaires)} \\ \mathbf{Plan\ de\ Donn\acute{e}es\ R\acute{e}seau\ (Couche\ 4)} : & \text{SLIM Mesh (chiffrement et transport point-à-point)} \end{cases}$$

---

## 3. [Critical] [Bloquant / Erreur formelle & Théorie transactionnelle] Absence de formalisme transactionnel distribué (ACID vs BASE) et impossibilité de l'atomicité dans AP2 sans modèle Saga et transactions compensatoires
- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 10, page 116, § 10.1.1 (lignes 9540-9545) :
  > « AP2 s’attache à ce qui se passe lorsque la tâche déléguée engage un paiement. Ce n’est pas un protocole concurrent ; c’est un protocole qui prend le relais au point où la délégation cesse d’être réversible » ;
  et page 118, § 10.1.4 (lignes 9746-9772) :
  > « Il porte la chaîne de mandats — Intent Mandate, Cart Mandate, Payment Mandate — matérialisés comme attestations vérifiables signées au sens de la recommandation du consortium du web [...] Le contrat de consentement est découplé du contrat de mouvement de fonds » ;
  et Figure 10.4 page 125.
- **Diagnostic causal approfondi** :
  Le manuscrit qualifie abusivement AP2 de protocole de transaction tout en le réduisant à une suite d'attestations vérifiables W3C statiques. En informatique des systèmes répartis (théorème CAP/PACELC et standards transactionnels ISO/IEC 10026) :
  1. *Une chaîne de jetons signés ne constitue pas une transaction* : Une autorisation cryptographique statique n'assure aucune cohérence d'état dynamique face aux partitions réseau, aux pannes de nœuds ou aux rejets d'exécution.
  2. *Violation de l'Atomicité ($A$ de ACID) :* Si le `Payment Mandate` est exécuté sur le réseau financier (débit bancaire effectif), mais que le commerçant ou l'agent subit un crash avant la livraison du bien ou l'émission du reçu, le système demeure dans un état non atomique incohérent (débit sans contrepartie).
  3. *Fausse affirmation d'irréversibilité :* Le paiement financier réel n'est jamais instantanément irréversible (présence de pré-autorisations, autorisations avec capture différée, règlements nets différés, et mécanismes de rétrofacturation / chargebacks). En l'absence de formalisation d'un patron Saga distribué orchestré (avec définition formelle des transactions compensatoires $C_i$ annulant les transactions directes $T_i$), AP2 est formellement inapte au traitement transactionnel bancaire d'entreprise.
- **Contre-exemple explicite et correctif formel** :
  *Scénario d'échec :* Un agent de voyage d'entreprise réserve un trajet combiné avion (900 $) + hôtel (300 $). Le paiement du vol est validé via AP2. Lors de l'appel pour l'hôtel, l'API renvoie un code HTTP 503 (chambres épuisées). Si la politique d'entreprise impose l'annulation globale, aucun mécanisme d'AP2 ne coordonne la compensation financière, laissant les fonds prélevés et le système dans un état orphelin corrompu.
  *Correctif formel :*
  Requalifier AP2 comme protocole de *mandat et d'autorisation*, et définir explicitement l'automate d'exécution Saga :
  $$\text{Transaction Global } G = (T_1, T_2, \dots, T_n) \quad \text{avec le vecteur de compensation } (C_n, \dots, C_1)$$
  où chaque mandat de paiement (`Payment Mandate`) porte un `Global-Transaction-ID` et est obligatoirement assorti d'une spécification de mandat d'annulation (`Void Mandate`) et de remboursement (`Reversal Mandate`).

---

## 4. [Critical] [Bloquant / Erreur formelle juridique & Cryptographique] Rupture de la non-répudiation juridique dans AP2 face à l'injection d'invites due à la perte du contrôle exclusif du mandant
- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 10, page 120 (Tableau 10.1) ; page 123, § 10.3.4 (lignes 10220-10234) :
  > « Debi et coll., Whispers of Wealth, 2026 [...] montre que la signature des mandats ne neutralise pas l’amont : un agent dont l’intention est détournée signera un mandat malveillant parfaitement valide. Le verrou n’est pas la vérifiabilité cryptographique du mandat — elle fonctionne — mais l’intégrité du raisonnement qui le produit » ;
  et pages 124-125, § 10.4.2 (lignes 10280-10293) :
  > « La réponse architecturale : le mandat comme couche de preuve opposable. La chaîne intention -> panier -> paiement du § 10.1.4, signée et horodatée, fournit l’élément probant qui rattache une transaction contestée à un consentement antérieur du mandant ».
- **Diagnostic causal approfondi** :
  Il existe une contradiction interne flagrante entre la démonstration de la page 123 et la conclusion de la page 124 :
  - À la page 123, l'auteur admet qu'un agent manipulé par injection indirecte apposera une signature cryptographique valide sur un mandat malveillant spoliant l'utilisateur.
  - Aux pages 124-125, il prétend néanmoins que cette même chaîne signée constitue la « preuve opposable » rattachant la transaction au consentement du mandant et assurant la non-répudiation.
  Or, en droit de la preuve électronique (Loi concernant le cadre juridique des technologies de l'information - LCCJTI art. 28 au Québec, PIPEDA/LPRPDE au Canada fédéral, et Règlement eIDAS art. 26 en Europe), la force probante et la non-répudiation reposent sur une condition préalable d'ordre public : **le signataire doit conserver le contrôle exclusif de son moyen de création de signature**.
  Dès lors qu'une clé de signature est déléguée à un processus stochastique autonome soumis à des interférences contextuelles, le contrôle exclusif est anéanti. Devant un tribunal, la signature du mandat prouve uniquement l'exécution d'un calcul, jamais l'intégrité du consentement de l'humain.
- **Correctif formel** :
  Supprimer l'affirmation selon laquelle la chaîne signée AP2 résout l'opposabilité et la non-répudiation. Établir une démarcation stricte :
  1. *Transactions sous présence humaine (Human-Present) :* Signature du hachage de commande (`CartHash`) via WebAuthn/Passkeys (FIDO2) exécutée au sein d'une enclave matérielle sécurisée (Secure Enclave / TPM), garantissant le contrôle exclusif.
  2. *Transactions autonomes déléguées (Human-Not-Present) :* Exclusion expresse du principe de non-répudiation opposable au débiteur ; bascule obligatoire vers un régime contractuel de responsabilité objective, de dépôts fiduciaires sous séquestre (*escrow*), de plafonds d'autorisation stricts et d'assurance contre le risque d'ingérence algorithmique.

---

## 5. [Critical] [Bloquant / Erreur formelle d'architecture] Absence de mécanisme d'idempotence et risque de double débit lors des réémissions sur transport MCP sans état
- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 8, page 92 (Tableau 8.2) ; Chapitre 11, page 135, § 11.3.1 (lignes 11296-11303) :
  > « (3) La suppression de la reprise de flux transforme une interruption en perte de requête, ce qui déplace vers le client la logique de réémission — et le ch. 48 établit qu’une réémission sans sémantique d’effet est une source de duplication, non une garantie » ;
  et Chapitre 10, pp. 115-127 (absence totale de standard d'idempotence dans AP2 et MPP).
- **Diagnostic causal approfondi** :
  La refonte de MCP du 28 juillet 2026 supprime le suivi de session et la reprise de flux (*stream resumption*). Tout timeout réseau contraint l'agent client à réémettre l'appel d'outil sous un identifiant neuf.
  Simultanément, le Chapitre 10 introduit les protocoles de paiement agentique (AP2, MPP) au-dessus de cette couche sans standardiser de clé d'idempotence financière.
  Si une requête de règlement financier subit une rupture de liaison après que le serveur ou la passerelle bancaire a procédé au débit, mais avant la réception du code JSON-RPC de confirmation :
  1. L'agent client interprète le timeout comme un échec de transmission et réémet l'ordre avec un nouvel identifiant d'appel.
  2. Faute d'en-tête d'idempotence partagé, le serveur financier traite la requête comme une transaction nouvelle.
  3. L'utilisateur subit un double débit financier incontrôlé.
  Renvoyer le traitement de cette vulnérabilité au chapitre 48 constitue une faute de conception majeure dans les chapitres posant les fondations protocolaires de paiement.
- **Correctif formel** :
  Spécifier impérativement au cœur des chapitres 8 et 10 un en-tête d'idempotence cryptographique déterministe pour tout appel d'outil ou mandat à effet de bord :
  $$K_{\text{idempotence}} = \text{Base64}\Big(\text{HMAC-SHA256}\big(K_{\text{mandat}},\, \text{IntentID} \parallel \text{CartHash} \parallel \text{Nonce}_{\text{séquence}}\big)\Big)$$
  Imposer la mise en cache côté serveur des résultats d'exécution transactionnelle indexés sur $K_{\text{idempotence}}$ pendant une durée minimale contractuelle (ex. 24 à 48 heures).

---

## 6. [Critical] [Bloquant / Erreur formelle & Omission de l'état de l'art IETF] Falsification de la crise d'OAuth 2.0 : omission des jetons liés au porteur (DPoP RFC 9449 et MTLS RFC 8705) et méprise sur la racine de la crise
- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 12 (*L’héritage et les standards étirés...*), page 144, lignes 12008-12011, et Tableau 12.1 (lignes 12042-12048, `page-144.png`). Citation textuelle exacte :
  > « Le maillon qui cède y est nommé, et il est architectural : le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. [...]
  > Tableau 12.1 : Le justificatif n’est pas lié à son porteur : Le jeton porteur de la campagne UNC6395 n’est lié ni à l’appelant, ni à un appareil, ni à une session (Vol. III F-21, [A]) »
- **Diagnostic causal approfondi** :
  Le manuscrit fait reposer l'ensemble de sa démonstration de la faillite d'OAuth face aux agents sur la vulnérabilité du *Bearer Token* (RFC 6750), en prenant pour preuve l'incident UNC6395 (compromission d'août 2025 via des jetons d'intégration Salesforce).
  Cette analyse est doublement fautive :
  1. *Omission de l'état de l'art IETF :* L'IETF a précisément résolu la non-liaison des jetons porteurs en publiant le standard **RFC 9449 (DPoP - Demonstrating Proof-of-Possession at the Application Layer)** en septembre 2023 et le **RFC 8705 (Certificate-Bound Access Tokens via MTLS)**. Avec DPoP, le jeton d'accès est cryptographiquement lié à la paire de clés asymétriques du client. Le vol du jeton au repos (comme dans l'affaire UNC6395) est totalement inopérant pour un attaquant ne possédant pas la clé privée de l'agent.
  2. *Méprise sur la vulnérabilité intrinsèque des agents :* En focalisant la critique sur le jeton non lié, l'auteur masque la véritable impasse d'OAuth 2.0 : même en présence de jetons parfaitement liés par DPoP (RFC 9449), un agent autonome dont le raisonnement est manipulé par injection d'invite générera lui-même des preuves DPoP valides pour accomplir des actes malveillants. La faillite d'OAuth ne réside pas dans l'absence de liaison cryptographique au porteur, mais dans l'incapacité d'OAuth à lier l'autorisation à **l'intégrité cognitive du modèle et au contexte sémantique d'inférence**.
- **Correctif formel** :
  Réécrire le § 12.2 et le Tableau 12.1 pour intégrer les RFC 8705 et 9449. Démontrer formellement les limites de DPoP face au détournement cognitif :
  $$\text{DPoP Proof} = \text{Sign}_{K_{\text{Agent}}}\big(\text{HTTP-Method} \parallel \text{URI} \parallel \text{Timestamp} \parallel \text{Hash}(T_{\text{access}})\big)$$
  Établir que la signature est mathématiquement irréprochable alors même que la décision d'appel résulte d'un empoisonnement de contexte, prouvant que l'autorisation machine classique ignore l'état de santé mental de l'agent appelant.

---

## 7. [Critical] [Bloquant / Erreur formelle mathématique] Invalidation du rapprochement avec la tolérance aux pannes byzantines : omission de la corrélation des erreurs stochastiques (Common-Cause Failures)
- **Sévérité** : [Critical] [Bloquant / Erreur formelle mathématique]
- **Localisation précise** : Chapitre 11 (*Modes d’échec et taxonomie des risques protocolaires*), page 133, § 11.2.1 (lignes 11108-11118, `page-133.png`). Citation textuelle exacte :
  > « Perspective de recherche — vers une science de la fiabilité des agents. Deux cadres analytiques se distinguent. D’une part, le rapprochement avec la tolérance aux pannes byzantines : un agent non déterministe qui émet un message plausible mais erroné se comporte comme un nœud byzantin, ce qui ouvre la question — encore largement ouverte — de seuils de quorum et de redondance pour des acteurs probabilistes. D’autre part, la décomposition de l’exécution en sous-tâches vérifiées par consensus comme voie vers une fiabilité de qualité industrielle. »
- **Diagnostic causal approfondi** :
  L'analogie proposée entre agents autonomes probabilistes et nœuds byzantins classiques (modèles de Lamport, PBFT de Castro & Liskov) est mathématiquement fausse en raison d'une violation flagrante de leurs hypothèses de base :
  1. *L'axiome d'indépendance statistique des défaillances :* Les algorithmes de consensus byzantin garantissent la sûreté ($Safety$) et la vivacité ($Liveness$) sous réserve que la probabilité de défaillance des nœuds soit indépendante, permettant à un quorum super-majoritaire de $Q \ge 2f + 1$ (avec $n \ge 3f + 1$) d'isoler les nœuds corrompus.
  2. *Défaillances en mode commun dans les systèmes agentiques (Common-Cause Failures) :* En pratique d'entreprise, les agents s'appuient sur un ensemble très restreint de modèles de fondation (ex. Claude 3.5, GPT-4o, Llama 3) et partagent des données de contexte (RAG), des invites système ou des représentations latentes similaires.
  3. *Effondrement du vote par consensus :* Face à un prompt trompeur, une perturbation sémantique adverse ou un biais de raisonnement, les agents d'une même classe de modèles partagent le même mode d'échec ($P(E_i \cap E_j) \gg P(E_i)P(E_j)$). Un ensemble de $N$ agents votera ainsi unanimement pour l'état erroné, réduisant le prétendu quorum byzantin à une illusion d'intégrité.
- **Correctif formel** :
  Poser formellement les limites mathématiques du consensus agentique homogène :
  Soit $N$ agents et un modèle de base partagé $M$. En présence d'un stimulus adverse $\delta$, la probabilité de consensus erroné tend vers 1 dès lors que le taux de transfert d'erreur intra-modèle est élevé :
  $$P(\text{Consensus Falsifié}) = \sum_{m = \lceil 2N/3 \rceil}^N \binom{N}{m} (1-\epsilon)^m \epsilon^{N-m} \xrightarrow[\epsilon \to 0]{} 1$$
  Mentionner explicitement que la tolérance aux pannes byzantines est formellement inapplicable aux essaims d'agents sans une diversité prouvée des architectures de modèles, des jeux de données d'apprentissage et des mécanismes d'inférence.

---

# II. CONSTATS MAJEURS / LACUNES MÉTHODOLOGIQUES, ARCHITECTURALES ET ALGORITHMIQUES [MAJOR]

## 8. [Major] [Majeur / Lacune architecturale] Réduction erronée de l'architecture Cisco AGNTCY : occultation du routage d'overlay sémantique (Capability-Based Routing) et omission de l'isolation multi-tenant (BSIF E-23 / Loi 25)
- **Sévérité** : [Major] [Majeur / Lacune architecturale]
- **Localisation précise** : Chapitre 10, page 119, § 10.2.2 (lignes 9830-9851) :
  > « Le contenu du projet, tel que les sources le portent, tient en deux capacités : des annuaires de découverte (discovery directories) ; un transport nommé SLIM. [...] Les sources n’en disent pas davantage : ni spécification, ni statut de maturité, ni version. Absence de documentation (degré 3). Ce chapitre s’en tient là, et ne complète pas de mémoire. »
- **Diagnostic causal approfondi** :
  Le manuscrit se réfugie sous l'étiquette commode d'« absence de documentation (degré 3) » pour éluder l'analyse architecturale du projet open source AGNTCY (Cisco / Linux Foundation), pourtant documenté publiquement. Ce faisant, il passe sous silence trois exigences fondamentales de l'ingénierie des réseaux d'entreprise :
  1. *Routage en réseau superposé (Overlay Mesh) vs Routage IP traditionnel :* Les agents s'exécutent dans des conteneurs éphémères aux adresses IP changeantes. AGNTCY implémente un routage sémantique fondé sur les descripteurs de capacités déclarés (*Capability-Based Routing*), découplé des sous-réseaux IP sous-jacents.
  2. *Cloisonnement multi-tenant et micro-segmentation agentique :* Dans les institutions financières réglementées (directives BSIF E-23, Loi 25), des agents appartenant à des juridictions ou départements distincts ne peuvent communiquer en clair. AGNTCY positionne des passerelles d'agents (*Agent Gateways*) opérant comme des points de contrôle d'accès réseau (*Policy Enforcement Points* - PEP).
  3. *Overhead cryptographique et vulnérabilité des passerelles :* Le protocole SLIM superpose du chiffrement de bout en bout avec vérification des signatures à chaque nœud relais, induisant un surcoût de latence critique pour les flux conversationnels d'agents. De plus, la passerelle constitue un point de défaillance unique : sa compromission expose les charges utiles non chiffrées en mémoire partagée.
- **Correctif formel** :
  Supprimer la déclaration de carence documentaire et formaliser la matrice de routage de passerelle d'infrastructure AGNTCY :
  $$R_{\text{AGNTCY}} : \big(\text{CapabilityDescriptor},\, \text{TenantID},\, \text{Proof}_{\text{DID}}\big) \longrightarrow \text{Gateway}_{\text{Target}}\big(\text{Endpoint}_{\text{mTLS}},\, \text{SLIM-Channel}\big)$$

---

## 9. [Major] [Majeur / Lacune méthodologique] Impasse de la délégation récursive dans OAuth : limites formelles du Token Exchange (RFC 8693) et omission des capacités cryptographiques atténuables hors-ligne
- **Sévérité** : [Major] [Majeur / Lacune méthodologique]
- **Localisation précise** : Chapitre 12, pages 141-144, § 12.1 et § 12.2.
- **Diagnostic causal approfondi** :
  Le chapitre 12 critique l'inadaptation d'OAuth aux agents en centrant son réquisitoire sur le flux interactif (§ 4.1 du RFC 6749) et l'absence d'humain devant l'écran, omettant d'instruire le standard spécifiquement conçu par l'IETF pour la délégation inter-services : le **RFC 8693 (OAuth 2.0 Token Exchange)**.
  Or, c'est précisément dans le RFC 8693 que se révèlent les limites structurelles d'OAuth face aux systèmes multi-agents :
  1. *Centralisation et latence synchrone :* Tout échange de jeton (`subject_token` $\to$ nouveau jeton) requiert un aller-retour réseau synchrone vers le serveur d'autorisation central (AS). Dans une chaîne de délégation récursive multi-sauts ($A_1 \to A_2 \to \dots \to A_n$), ce goulot d'étranglement paralyse les performances.
  2. *Impossibilité d'atténuation cryptographique locale :* Le RFC 8693 ne permet pas à un agent intermédiaire d'atténuer lui-même les privilèges d'un jeton (ex. restreindre le montant autorisé ou réduire la fenêtre temporelle) sans solliciter l'AS.
  3. *Vulnérabilité au mandataire confus récursif (Recursive Confused Deputy) :* La traçabilité de l'intention initiale est perdue au fil des réémissions de jetons intermédiaires.
- **Correctif formel** :
  Intégrer une analyse comparative opposant le RFC 8693 aux architectures de capacités cryptographiques atténuables hors-ligne (*Macaroons* de Birgisson et coll., *UCAN* / *W3C Verifiable Credentials*) :
  $$\text{Capabilité}_{i+1} = \text{HMAC}\big(\text{Capabilité}_i,\, \text{Restriction}_{i+1}\big)$$
  démontrant que les architectures d'agents autonomes requièrent des jetons auto-atténuables localement sans dépendance synchrone à un serveur central.

---

## 10. [Major] [Majeur / Lacune méthodologique] Incompatibilité structurelle et temporelle de SCIM (RFC 7643 / RFC 7644) face au cycle de vie hautement volatil et non tracé des agents stochastiques
- **Sévérité** : [Major] [Majeur / Lacune méthodologique]
- **Localisation précise** : Chapitre 12, pages 141-143, § 12.1 (lignes 11904-11922) et Tableau 12.1 (p. 144). Citation textuelle exacte :
  > « La §4 du RFC 7643 ne définit aucun type de ressource pour un mandataire logiciel autonome [...] la spécification de registre d’agents de CSA Labs du 27 mars 2026 s’y ancre néanmoins, via une extension IETF expirée [...] »
- **Diagnostic causal approfondi** :
  L'auteur formule une critique purement lexicale et sémantique de SCIM (l'absence de ressource « Agent » et le vocabulaire orienté ressources humaines comme `employeeNumber`).
  Cette critique passe à côté du véritable obstacle d'ingénierie qui rend SCIM inapplicable aux agents :
  1. *Incompatibilité des ordres de grandeur temporels :* SCIM (RFC 7644) est un protocole HTTP/REST synchrone taillé pour des mouvements d'identités humaines (embauche, rotation, départ) sur des échelles de jours ou d'heures ($\Delta t \sim 10^3 \text{ à } 10^5\text{ s}$). Les agents autonomes de traitement de tâches sont instanciés de façon éphémère pour des durées de vie de quelques secondes ($\tau \sim 10^{-1} \text{ à } 10^1\text{ s}$) et peuvent être répliqués par milliers. Gérer ce cycle de vie par des requêtes SCIM `POST /Users` et `DELETE /Users/{id}` entraîne l'effondrement immédiat des annuaires d'entreprise.
  2. *Absence d'immuabilité et d'auditabilité forensique :* Une mutation d'état dans SCIM (`PATCH`) écrase les attributs précédents sans consigner de preuve d'état signée. Or, la traçabilité réglementaire (BSIF E-23) exige de certifier avec précision quelle version du modèle, quel prompt système et quelles autorisations étaient en vigueur lors de l'exécution d'une transaction financière à un instant $t$.
- **Correctif formel** :
  Rejeter les propositions d'extension artificielle de SCIM (ex. `draft-abbey-scim-agent-extension`) pour la gestion des cycles de vie d'agents. Préconiser des architectures d'annuaires de capacités adossées à des journaux de transparence immuables et cryptographiquement vérifiables (*Transparency Logs* / Sigstore Rekor).

---

## 11. [Major] [Majeur / Lacune d'intégration financière] Incompatibilité et absence totale d'articulation entre AP2 et les standards de messagerie financière réglementée (ISO 20022 : pain.001, pacs.008, camt.056)
- **Sévérité** : [Major] [Majeur / Lacune d'intégration financière]
- **Localisation précise** : Chapitre 10, page 118, § 10.1.4 (lignes 9774-9782) :
  > « L’articulation du protocole de paiement avec les rails de paiement nationaux d’un marché donné — le cas canadien est celui que le Vol. II instruit — n’est documentée par aucune source de son socle : absence de documentation (degré 3) [...] La somme héritera cette lacune telle quelle » ;
  et pp. 121-124 (focalisation exclusive sur les cartes et micro-paiements crypto x402/MPP).
- **Diagnostic causal approfondi** :
  L'ouvrage annonce en sous-titre le déploiement d'agents « en services financiers réglementés (2024-2032) ». Or, dans l'infrastructure bancaire moderne d'entreprise (au Canada avec Lynx et le Real-Time Rail RTR de Paiements Canada, aux États-Unis avec FedNow, et en Europe avec SEPA Instant), le standard normatif pivot obligatoire est **ISO 20022**.
  Le manuscrit abandonne toute articulation entre AP2 et ISO 20022 en invoquant un « degré 3 » :
  - Aucun mapping formel des mandats AP2 (`Payment Mandate`) vers les messages d'initiation de virement ISO 20022 `pain.001.001.12` ;
  - Aucun schéma de transport des identifiants cryptographiques d'agents (DIDs ou clés publiques) au sein des blocs d'identification des parties débitrices (`Dbtr/Id/OrgId/Othr/Id`) dans les messages interbancaires `pacs.008` ;
  - Aucun traitement des retours, rejets et annulations de paiements via les formats de notification `pacs.002` et `camt.056`.
  Ignorer ISO 20022 rend la pile AP2 totalement inopérante pour une institution financière régie par les normes du BSIF.
- **Correctif formel** :
  Insérer une spécification prescriptive de passerelle d'interopérabilité `AP2-to-ISO20022` :
  1. *Traduction du mandat :* Encapsulation du `Payment Mandate` signé dans le bloc documentaire de transport `SupplementaryData` (`Envlp`) d'un message `pain.001` ;
  2. *Identification d'agent :* Enregistrement du DID de l'agent mandataire dans la balise `Dbtr/PrvtId/Othr/Id` sous le scheme identifier `DID` ;
  3. *Gestion du cycle de vie :* Liaison des notifications d'exécution interbancaire `pacs.002` aux événements de clôture de tâche dans le cycle A2A.

---

## 12. [Major] [Majeur / Lacune taxonomique et algorithmique] Incomplétude de la taxonomie des modes d'échec (Tableau 11.4) : omission de l'explosion récursive de sous-tâches (Fork Bomb) et absence d'algorithmes de détection d'interblocage (Wait-For Graph)
- **Sévérité** : [Major] [Majeur / Lacune taxonomique et algorithmique]
- **Localisation précise** : Chapitre 11, page 133, Tableau 11.4 (*Les sept modes d’échec spécifiques...*, `page-133.png`) et § 11.2.1.
- **Diagnostic causal approfondi** :
  Le Tableau 11.4 prétend établir la taxonomie exhaustive des échecs à la frontière interopérable, mais il présente des lacunes critiques :
  1. *Omission de l'explosion récursive de sous-tâches (Agentic Fork Bomb / Cascading Sub-task Proliferation) :* Lorsqu'un superviseur décompose des missions en sous-tâches déléguées à des pairs via A2A, une formulation sous-spécifiée pousse les sous-agents à engendrer récursivement des dizaines de descendants. Faute d'un compteur de sauts standardisé (`Max-Hops`) et d'un budget global de jetons partagé, l'infrastructure subit un déni de service interne auto-induit (*Self-Inflicted DoS*).
  2. *Traitement purement déclaratif de l'interblocage (Deadlock) :* Le tableau cite « l'interblocage de délégation — agents s'attendant mutuellement » comme étant « propre à cette section ». Or, le texte du chapitre ne fournit aucun modèle formel d'attente (absence de graphe d'attente *Wait-For Graph* - WFG), aucune vérification des conditions de Coffman, et aucun algorithme de prévention ou de rupture (pas d'estampilles de Lamport, pas de politiques Wound-Wait / Wait-Die).
  3. *Usage métaphorique du mot « verrou » :* Le terme « verrou » est utilisé 7 fois dans les chapitres 10 et 11 comme figure de style (« verrou du domaine », « verrou opérationnel »), sans jamais désigner un véritable mécanisme de synchronisation distribuée (*Distributed Lock Manager* via Raft ou Redis Redlock).
- **Correctif formel** :
  Compléter le Tableau 11.4 en intégrant :
  - **Mode 8 : Explosion récursive de sous-tâches (Fork Bomb)** — Rupture : borne d'épuisement de ressources distribuées. *Mitigation* : en-tête contextuel immuable `X-Agentic-Hop-Limit` décrémenté à chaque délégation et budget de calcul global plafonné.
  - Formaliser la détection d'interblocage multi-agents par la construction dynamique d'un graphe orienté d'attente $G = (V, E)$ où un cycle $A_1 \to A_2 \to \dots \to A_1$ déclenche l'interruption préemptive de la tâche la plus récente selon un ordonnancement d'estampilles temporelles strict (*Wait-Die Policy*).

---

## 13. [Major] [Majeur / Sécurité protocolaire] Insécurité de l'état applicatif dans MCP révisé (2026-07-28) : exposition de jetons d'état opaques dans le canal de prompt non fiable sans schéma AEAD
- **Sévérité** : [Major] [Majeur / Sécurité protocolaire]
- **Localisation précise** : Chapitre 8, page 92, Tableau 8.2 ; et Chapitre 11, page 135, § 11.3.1 (lignes 11286-11290). Citation textuelle exacte :
  > « [...] l’état applicatif migre vers des poignées frappées par le serveur et transmises comme arguments d’outil ordinaires, c’est-à-dire dans le canal même que le § 11.1 décrit comme non fiable. »
- **Diagnostic causal approfondi** :
  L'auteur observe pertinemment que la refonte de MCP sans état reporte la conservation d'état vers des « poignées d'outils » (*state handles*) réinjectées dans les arguments de prompt par le modèle.
  Toutefois, le manuscrit omet de formuler les exigences de durcissement cryptographique indispensables :
  1. *Falsification d'état (State Tampering) :* Si la poignée d'état n'est pas scellée et authentifiée cryptographiquement côté serveur, une injection indirecte dans le prompt peut amener le LLM à altérer les paramètres portés par la poignée (ex. identifiant d'entité, niveau de privilège).
  2. *Rejeu et confusion de contexte :* En l'absence d'horodatage strict et d'un nonce lié à l'instance, une poignée d'état valide interceptée peut être rejouée dans une session d'agent distincte.
- **Correctif formel** :
  Imposer dans les prescriptions d'architecture que toute poignée d'état transitant par un agent sur un transport sans état utilise impérativement le chiffrement authentifié avec données associées (AEAD) :
  $$\text{StateHandle} = \text{ChaCha20-Poly1305}_{K_{\text{serveur}}}\big(\text{Payload d'état}\big) \parallel \text{Tag d'authentification}$$
  garantissant qu'aucune manipulation par le LLM ou injection adverse ne puisse corrompre l'état de session conservé côté serveur.

---

## 14. [Major] [Majeur / Erreur formelle de composition] Ruptures textuelles et phrases tronquées à la page 79 (bloc Thèse et paragraphe introductif § 7.0)
- **Sévérité** : [Major] [Majeur / Erreur formelle de composition]
- **Localisation précise** : Chapitre 7 (*Généalogie et gouvernance...*), page 79 du PDF (`page-79.png`), lignes 6496-6508 de `DOCUMENT_TEXT_MAP.md`. Citation textuelle exacte :
  > « [...] fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.
  > Le second mouvement du Livre s’ouvre ici. Les ch. 1 à 3 ont posé le socle pré-agentique ; les ch. 4 à 6, l’ingénierie de l’agent. Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses
  > La proposition directrice tient en un déplacement, et il vaut d’être énoncé avec précision [...] »
- **Diagnostic causal approfondi** :
  L'inspection de la page 79 révèle deux ruptures syntaxiques majeures de composition :
  1. *Fin de bloc Thèse corrompue :* La mention « instruit au ch. 10. » est immédiatement concaténée avec « outils, le dialogue entre agents... » sans transition, verbe ni articulation grammaticale.
  2. *Paragraphe suivant tronqué net :* La phrase se termine abruptement sur « — le contrat entre un agent et ses » sans aucun nom ni complément d'objet, avant de sauter directement à l'alinéa suivant (« La proposition directrice... »).
- **Correctif formel** :
  Rétablir la syntaxe complète des deux passages corrompus :
  1. Pour la fin du bloc Thèse : « [...] fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. Le présent mouvement analyse dès lors successivement l'accès aux outils, le dialogue entre agents, la découverte de services, le règlement commercial, et les modes d’échec qui leur sont propres. »
  2. Pour le paragraphe suivant : « Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses pairs ainsi que son environnement d'outils. »

---

# III. CONSTATS MINEURS / CLARTÉ TERMINOLOGIQUE ET MISE EN PAGE [MINOR]

## 15. [Minor] [Mineur / Rigueur documentaire] Désignation imprécise du mécanisme d'identité d'AWS Bedrock
- **Localisation** : Chapitre 12, page 143, lignes 11932-11936 (`page-143.png`). Citation :
  > « Chez AWS, le mécanisme documenté comparable est Amazon Bedrock AgentCore Identity, où l’identité d’agent est une identité de charge de travail dotée d’attributs propres plutôt qu’un type d’objet distinct [...] »
- **Diagnostic** : L'appellation commerciale exacte d'AWS est *Amazon Bedrock Agents* associé aux rôles IAM de service (`IAM Execution Roles`), le libellé « Amazon Bedrock AgentCore Identity » résultant d'un amalgame terminologique d'éditeurs tiers.
- **Correctif** : Rectifier la désignation en précisant qu'AWS ne définit pas d'objet d'identité dédié aux agents, mais réutilise le mécanisme de délégation `sts:AssumeRole` avec balises de session (`aws:PrincipalTag`), ce qui corrobore la thèse de l'étirement des identités de charge de travail existantes.

---

## 16. [Minor] [Mineur / Mise en page] Déplacement typographique discordant de la Figure 10.4
- **Localisation** : Chapitre 10, page 125 (`page-125.png`).
- **Diagnostic** : La Figure 10.4 (*Le mandat comme couche de preuve opposable...*) est intercalée en tête de la page 125, au-dessus du titre de la section 10.5 (*Le destin de l'ACP protocolaire*), alors qu'elle illustre le texte de la section 10.4.2 située au bas de la page 124. Cette disposition crée une fausse association thématique avec l'ACP.
- **Correctif** : Forcer l'ancrage typographique de la figure immédiatement sous le paragraphe 10.4.2 auquel elle se rattache conceptuellement.

---

## 17. [Minor] [Mineur / Typographie québécoise et canadienne-française] Espaces insécables manquants devant la ponctuation double
- **Localisation** : Chapitre 10, page 116, § 10.1.2 ; Chapitre 11, page 138, Tableau 11.5.
- **Diagnostic** : Des signes de ponctuation doubles (deux-points, points-virgules) et des guillemets français (« ») ne comportent pas d'espace insécable fin, provoquant des retours à la ligne orphelins.
- **Correctif** : Appliquer systématiquement l'espace insécable (`&thinsp;` ou `~`) conformément aux normes de composition du français canadien et québécois.

---

# CONCLUSION DE L'AGRÉGATEUR 2

L'audit contradictoire consolidé des candidats 3 et 4 met en évidence une contradiction fondamentale du compendium sur le segment des protocoles (pp. 78-145) :
1. **Sur le plan éditorial et de la composition** : Le segment souffre de bogues matériels inacceptables pour un ouvrage de cette ambition, dont le tronçonnement du mot « chapitre » et le bégaiement textuel à la page 115, ainsi que des coupures de phrases nettes à la page 79.
2. **Sur le plan conceptuel et protocolaire** : L'ouvrage s'enferme dans une fausse aporie sur le sigle « ACP », confondant le Data Plane applicatif L7 (IBM/A2A) et le Control Plane réseau L4/L5 (Cisco AGNTCY).
3. **Sur le plan financier et distribué** : AP2 est qualifié à tort de protocole transactionnel. En réalité, il s'agit d'une chaîne statique d'attestations W3C dépourvue de garanties d'atomicité (ACID/BASE), de protocole Saga, de clé d'idempotence sur transport MCP sans état, et de passerelle vers la messagerie financière réglementée ISO 20022.
4. **Sur le plan juridique et de la sécurité** : La promesse de non-répudiation d'AP2 est juridiquement caduque, car l'injection d'invites anéantit le contrôle exclusif du mandant sur la signature de l'agent. De même, l'analyse d'OAuth 2.0 ignore les jetons liés au porteur (DPoP RFC 9449) et l'analogie avec les pannes byzantines s'effondre mathématiquement face aux défaillances corrélées en mode commun des modèles de fondation.
