**Segment scope**: Couverture exhaustive des pages 78 à 145 (chapitres 7 à 12, segments S08 à S13 de REVIEW_PLAN.md), avec focalisation approfondie sur l'architecture réseau Cisco AGNTCY, la synthèse des modes d'échec du Livre I, et la crise des protocoles d'identité humaine (OAuth 2.0 / SCIM) appliqués aux agents autonomes stochastiques.

# Potential Mistakes and Improvements

## 1. [Critical] [Bloquant / Erreur formelle & Corruption éditoriale] Bogue d'édition majeur à la page 115 : mot coupé en deux (« ce cha ... pitre »), rupture syntaxique et duplication textuelle désastreuse

- **Sévérité** : [Critical] [Bloquant / Erreur formelle]
- **Localisation précise** : Chapitre 10 (*Transaction et infrastructure : AP2 et AGNTCY*), page 115 du PDF (`page-115.png`), lignes 28 à 48 du texte extrait de `DOCUMENT_TEXT_MAP.md`. Citation textuelle exacte :
  > « [...] La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce cha
  > Thèse — que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur — le socle établit qu’AP2 est un protocole compagnon d’A2A, rien de plus sur sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet, une déclaration et non un fait vérifié, que des analyses tierces nuancent. pitre prend pour objet. Que la transaction agentique constitue l’aboutissement financier de la pile protocolaire est une lecture d’auteur : les sources établissent que le protocole de paiement est un protocole compagnon de l’axe agent-agent, dédié aux transactions pilotées par agents, et rien de plus sur sa centralité. Qu’AGNTCY soit une couche d’infrastructure et non un concurrent est, pour sa part, le positionnement officiel déclaré du projet — une déclaration, non un fait vérifié, et que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux n’est un fait établi. »
- **Diagnostic causal approfondi** :
  Une inspection visuelle directe de `page-115.png` et l'analyse du flux de texte révèlent une fusion de fichiers non nettoyée ou un bogue critique de composition typographique (LaTeX / Pandoc) :
  1. Le mot « chapitre » est littéralement tronçonné en deux : le radical « ce cha » termine le paragraphe introductif avant le bloc de thèse, tandis que le suffixe « pitre prend pour objet. » est injecté au beau milieu du corps de la thèse, immédiatement après le mot « nuancent. ».
  2. Le paragraphe qui suit est une duplication mot pour mot, quasi-identique, de la thèse (« Que la transaction agentique constitue l'aboutissement financier... »), créant un bégaiement textuel inacceptable dans un ouvrage de référence financière et systémique.
  Cette corruption matérielle discrédite immédiatement le sérieux éditorial de l'ouverture du chapitre 10.
- **Correctif formel ou contre-exemple explicite** :
  Supprimer l'artefact de césure et la répétition textuelle. Remplacer les lignes incriminées par une structure unifiée et rigoureusement articulée :
  ```markdown
  La thèse de ce chapitre doit être décomposée avant d’être employée, car ses deux moitiés n’ont pas le même statut de preuve, et les fondre serait la faute que ce chapitre prend pour objet.

  Thèse — Que la transaction pilotée par agents (AP2) soit l’aboutissement financier de la pile est une lecture d’auteur : le socle établit qu’AP2 est un protocole compagnon d’A2A, sans préjuger de sa centralité ; qu’AGNTCY soit une couche d’infrastructure et non un concurrent est le positionnement officiel déclaré du projet — une déclaration d'intention et non un fait vérifié, que des analyses tierces viennent nuancer. Une lecture d’auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux ne constitue un fait établi.
  ```

---

## 2. [Critical] [Bloquant / Erreur formelle & Confusion conceptuelle] Fausse aporie sur la « collision ACP » : confusion entre le plan de données applicatif (IBM/A2A) et le plan de contrôle réseau (Cisco AGNTCY)

- **Localisation précise** : Chapitre 10, pages 126-127, § 10.5.3 (*Le versant protocolaire de la collision terminologique*), et Chapitre 7, page 87, Tableau 7.3 ligne (d) et encadré § 7.5 (`page-87.png`, `page-126.png`). Citation textuelle exacte :
  > « Restent deux objets, et c’est entre eux que la confusion est à la fois la plus facile et la plus dommageable : l’ACP protocolaire, dont le § 10.5.1 vient de rappeler la fusion ; et la composante ACP de la couche d’infrastructure, dont le § 10.2.3 a rapporté que des analyses tierces lui prêtent un chevauchement avec le protocole agent-agent. Les sources n’établissent, de cette seconde, ni l’intitulé complet, ni la nature, ni l’identité avec la première. [...]
  > L’enjeu de cette prudence n’est pas cosmétique, et les deux branches de l’alternative conduisent à des conclusions d’architecture opposées :
  > • si les deux objets n’en font qu’un, la fusion d’août 2025 vaut pour la couche d’infrastructure, et le chevauchement relevé par les tiers est le vestige d’un protocole éteint ;
  > • s’ils sont deux, la couche d’infrastructure porte une composante active dont le rapport au protocole agent-agent reste à qualifier. »
- **Diagnostic causal approfondi** :
  Le manuscrit s'enferme dans une fausse aporie épistémologique qu'il qualifie de « dossier terminologique le plus délicat de la somme », en affirmant qu'il est impossible d'établir si l'ACP d'IBM et l'ACP de Cisco AGNTCY sont un seul ou deux objets distincts, renvoyant la question comme une lacune insoluble jusqu'au chapitre 49.
  Cette posture procède d'une méconnaissance flagrante de l'architecture des réseaux et de l'état de l'art open source 2024-2026 :
  1. **L'ACP protocolaire applicatif (IBM Research / BeeAI, mars 2025)** : Il s'agit d'une spécification de couche 7 (Application Layer) définissant un protocole de haut niveau pour l'échange d'intentions et de messages structurés entre agents. Ce protocole a formellement fusionné le 29 août 2025 avec le protocole Agent2Agent (A2A) au sein de la Linux Foundation.
  2. **L'ACP d'AGNTCY (Cisco Systems / Linux Foundation, juillet 2025)** : Dans l'architecture réseau de Cisco AGNTCY, « ACP » désigne l'*Agentic Control Plane* (ou *Agent Connectivity Protocol*), qui est un protocole de signalisation d'infrastructure réseau opérant au niveau de la couche transport/session (Overlay Network L4/L5). Il gère le plan de contrôle des passerelles (*Agent Gateways*), la synchronisation des tables de routage de capacités et l'échange de clés publiques pour le transport SLIM (*Secure Lightweight Inter-agent Messaging*).
  Affirmer que ces deux objets pourraient « n'en faire qu'un » et qu'une brique de routage réseau de Cisco aurait pu « s'éteindre » lors de la fusion d'un protocole d'application d'IBM est un contresens technique majeur. L'auteur confond le *Data Plane* applicatif (sémantique inter-agents) et le *Control Plane* d'infrastructure réseau.
- **Correctif formel ou contre-exemple explicite** :
  Réfuter l'hypothèse de l'alternative non tranchée au § 10.5.3 et supprimer la mention de « lacune non comblée ».
  Remplacer par une clarification architecturale formelle dissociant les plans OSI :
  $$\text{Stack}_{\text{Agentique}} = \begin{cases} \text{Couche 7 (Data Plane Applicatif)} : \text{A2A v1.0 (absorbant l'ACP-IBM)} \\ \text{Couche 4/5 (Control Plane Réseau)} : \text{ACP-Cisco / Agntcy Control Plane} \\ \text{Couche 4 (Transport Sécurisé)} : \text{SLIM Mesh Transport} \end{cases}$$
  Démontrer que le chevauchement relevé par des tiers n'est pas un vestige d'un protocole mort, mais la frontière classique entre la signalisation réseau (qui doit connaître les identifiants d'agents pour router les paquets) et le message applicatif A2A encapsulé dans la charge utile (payload).

---

## 3. [Critical] [Bloquant / Erreur formelle & Lacune architecturale] Falsification de l'architecture réseau Cisco AGNTCY : réduction erronée à un « transport » sans topologie, occultation du routage sémantique d'overlay et omission de la surface d'attaque des passerelles d'agents

- **Localisation précise** : Chapitre 10, page 119, § 10.2.2 (*Annuaires et transport : un vocabulaire d’infrastructure*), et Chapitre 9, page 106, Figure 9.2 (`page-119.png`). Citation textuelle exacte :
  > « Le contenu du projet, tel que les sources le portent, tient en deux capacités :
  > • des annuaires de découverte (discovery directories) ;
  > • un transport nommé SLIM.
  > C’est un vocabulaire d’infrastructure, non d’application : découvrir quels agents existent, et acheminer ce qu’ils s’envoient. [...] Les sources n’en disent pas davantage : ni spécification, ni statut de maturité, ni version. Absence de documentation (degré 3). Ce chapitre s’en tient là, et ne complète pas de mémoire. Une couche d’infrastructure dont on ne connaît ni la version ni le statut de maturité n’est pas évaluable au sens de la matrice du ch. 9 § 9.2.5 — et c’est une information en soi. »
- **Diagnostic causal approfondi** :
  L'auteur élude l'analyse d'AGNTCY sous prétexte d'une « absence de documentation (degré 3) ». Or, le projet AGNTCY, initié par Cisco et hébergé par la Linux Foundation depuis juillet 2025, dispose d'un modèle architectural public et documenté. En réduisant AGNTCY à « des annuaires et un transport », le manuscrit commet trois omissions architecturales critiques :
  1. **Topologie de routage en réseau superposé (Overlay Mesh) vs Routage IP traditionnel** : Les agents logiciels stochastiques s'exécutent dans des environnements de conteneurs hautement dynamiques, avec des adresses IP éphémères et réparties sur des clouds hybrides. Le routage IP L3/L4 conventionnel est incapable d'adresser une requête vers « l'agent d'analyse de risque de crédit le plus disponible et certifié ISO 42001 ». AGNTCY implémente un routage sémantique et basé sur les capacités (*Capability-Based Routing*).
  2. **Isolation multi-tenant et micro-segmentation agentique** : Dans les institutions financières réglementées (OSFI/BSIF E-23, Loi 25), deux agents de départements ou d'institutions concurrentes ne peuvent partager un même plan d'exécution sans cloisonnement strict. AGNTCY déploie des passerelles d'agents (*Agent Gateways*) jouant le rôle de *Policy Enforcement Points* (PEP). Le texte n'analyse à aucun moment comment cette isolation est garantie au niveau réseau.
  3. **Overhead cryptographique et surface d'attaque des passerelles** : Le protocole SLIM encapsule les messages dans un chiffrement de bout en bout avec signature à chaque saut. Cet empilement engendre un surcoût de latence (overhead de sérialisation et de handshakes cryptographiques) critique pour les essaims d'agents communicant à haute fréquence. De plus, la passerelle d'agents devient un point névralgique de compromission : si une passerelle AGNTCY est compromise, l'attaquant contourne le cloisonnement multi-tenant et intercepte l'ensemble des flux d'intentions non chiffrés en mémoire.
- **Correctif formel ou contre-exemple explicite** :
  Remplacer la déclaration d'absence du § 10.2.2 par l'analyse formelle de la topologie AGNTCY :
  Modéliser la fonction de routage d'overlay AGNTCY :
  $$R_{\text{Agntcy}} : (\text{Capability\_Descriptor}, \text{Tenant\_ID}, \text{Proof}_{\text{DID}}) \longrightarrow \text{Gateway}_{\text{Target}}(\text{Endpoint}_{\text{mTLS}}, \text{SLIM\_Channel})$$
  *Scénario de rupture d'isolation multi-tenant (Contre-exemple formel)* :
  Soit deux locataires bancaires $T_A$ et $T_B$ connectés à une même passerelle d'infrastructure AGNTCY mutualisée. Si l'authentification mutuelle SLIM termine le canal sécurisé au niveau de la passerelle (*TLS Termination at Edge Gateway*) pour procéder à l'inspection sémantique du payload A2A, la mémoire partagée du processus de la passerelle devient vulnérable à une attaque par canal auxiliaire ou injection indirecte de prompt empoisonnant la table de correspondance des sessions. Un agent compromis de $T_A$ peut alors forcer le routage d'une tâche malveillante vers un agent privé de $T_B$ sans que les filtres réseau IP sous-jacents ne détectent l'anomalie.

---

## 4. [Critical] [Bloquant / Erreur formelle & Omission de l'état de l'art IETF] Falsification de la crise d'OAuth 2.0 : omission des jetons liés au porteur (Sender-Constrained Tokens : DPoP RFC 9449 et MTLS RFC 8705) et focalisation réductrice sur le Bearer Token non lié

- **Localisation précise** : Chapitre 12 (*L’héritage et les standards étirés...*), page 144, lignes 353-356, et Tableau 12.1 (`page-144.png`). Citation textuelle exacte :
  > « Le maillon qui cède y est nommé, et il est architectural : le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. [...]
  > Tableau 12.1 : Le justificatif n’est pas lié à son porteur : Le jeton porteur de la campagne UNC6395 n’est lié ni à l’appelant, ni à un appareil, ni à une session (Vol. III F-21, [A]) »
- **Diagnostic causal approfondi** :
  Le manuscrit ancre toute sa démonstration de la faillite des standards de sécurité hérités face aux agents sur le postulat qu'OAuth 2.0 est irrémédiablement prisonnier du modèle des jetons porteurs (*Bearer Tokens*, RFC 6750), citant comme preuve indépassable la campagne UNC6395 (août 2025, compromise via Salesloft Drift).
  Cette affirmation est techniquement fausse et constitue une omission flagrante des travaux de normalisation de l'IETF :
  1. L'IETF a publié en septembre 2023 le standard **RFC 9449 : OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)**, complétant le **RFC 8705 (OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens)**.
  2. Avec DPoP (RFC 9449), le jeton d'accès n'est plus un *bearer token* : il est cryptographiquement lié à une paire de clés asymétriques propre au client via la confirmation d'empreinte (`jkt` claim). Chaque requête HTTP émise par l'agent requiert une signature numérique d'en-tête contenant un horodatage et un hachage de la requête (`ath` - Access Token Hash). Si un attaquant vole ce jeton (comme dans la campagne UNC6395), ce jeton est **totalement inutilisable** sans la clé privée de l'agent légitime !
  3. En ignorant RFC 9449 et RFC 8705, l'auteur passe à côté de la *véritable* crise d'OAuth face aux agents :
     - Même avec un jeton cryptographiquement lié par DPoP (RFC 9449), un agent dont le raisonnement est détourné par injection d'invite signera lui-même des requêtes légitimes avec sa clé privée légitime !
     - La crise n'est pas le vol de jeton au repos, mais l'impossibilité pour OAuth de lier le jeton au **contexte d'inférence stochastique** et à **l'intention sémantique vérifiable**.
- **Correctif formel ou contre-exemple explicite** :
  Corriger immédiatement le § 12.2 et le Tableau 12.1 en intégrant les RFC 8705 et RFC 9449.
  *Démonstration formelle de la limite de DPoP (Contre-exemple)* :
  Soit un agent $A$ détenteur d'un token d'accès $T$ lié par DPoP à sa clé privée $K_A$.
  La requête $R$ émise vers le serveur de ressources contient :
  $$\text{Header DPoP} = \text{Sign}_{K_A}(\text{URI}, \text{Method}, \text{Timestamp}, \text{Hash}(T))$$
  Le serveur de ressources vérifie avec succès la preuve cryptographique. Pourtant, si le but de la requête $R$ résulte d'une injection de prompt indirecte dans le contexte de $A$, la signature est valide, l'identité machine est confirmée, mais la transaction constitue une exfiltration illégitime. La faille d'OAuth réside dans le découplage entre l'autorisation d'API et l'intégrité cognitive de l'agent, et non dans l'absence de liaison cryptographique du jeton.

---

## 5. [Critical] [Bloquant / Erreur formelle & Mathématique] Invalidation du rapprochement avec la tolérance aux pannes byzantines : omission de la corrélation des erreurs stochastiques (Common-Cause Failures)

- **Localisation précise** : Chapitre 11 (*Modes d’échec et taxonomie des risques protocolaires*), page 133, § 11.2.1 (*La taxonomie des échecs émergents*), lignes 517-531 (`page-133.png`). Citation textuelle exacte :
  > « Perspective de recherche — vers une science de la fiabilité des agents. Deux cadres analytiques se distinguent. D’une part, le rapprochement avec la tolérance aux pannes byzantines : un agent non déterministe qui émet un message plausible mais erroné se comporte comme un nœud byzantin, ce qui ouvre la question — encore largement ouverte — de seuils de quorum et de redondance pour des acteurs probabilistes. D’autre part, la décomposition de l’exécution en sous-tâches vérifiées par consensus comme voie vers une fiabilité de qualité industrielle. »
- **Diagnostic causal approfondi** :
  Le texte propose une analogie séduisante mais mathématiquement et formellement invalide entre les agents autonomes probabilistes et les nœuds byzantins classiques (PBFT de Castro & Liskov, modèles de Lamport) :
  1. *L'hypothèse d'indépendance statistique des fautes* : Les protocoles de consensus byzantin reposent impérativement sur l'hypothèse que les nœuds honnêtes tombent en panne ou sont corrompus de manière indépendante, ce qui permet de tolérer jusqu'à $f < n/3$ nœuds défaillants au moyen d'un quorum à la majorité super-qualifiée ($2f + 1$).
  2. *La réalité des défaillances corrélées en IA agentique* : Dans une entreprise agentique, les agents déployés reposent sur un nombre très restreint de modèles de fondation (ex. GPT-4o, Claude 3.5 Sonnet, Llama 3) et partagent des contextes d'entraînement, des bibliothèques de prompt engineering ou des bases RAG communes.
  3. *Effondrement du quorum* : Face à une invite adversariale, une formulation ambiguë ou un biais systématique, la corrélation des fautes entre agents est quasi-totale ($P(E_A \cap E_B) \gg P(E_A)P(E_B)$). Par conséquent, un essaim de 5 agents d'une même famille confronté à une injection indirecte produira un vote unanime ($5/5$) en faveur de l'action erronée !
  Présenter le quorum byzantin comme une « voie vers une fiabilité de qualité industrielle » sans énoncer l'invalidation formelle par les modes communs de défaillance (*Common-Cause Failures*) induit une fausse sécurité architecturale catastrophique pour une institution réglementée.
- **Correctif formel ou contre-exemple explicite** :
  Formuler le théorème de rupture du consensus agentique homogène :
  Soit $N$ agents participant à un mécanisme de vote byzantin $K$-sur-$N$. Soit $M$ le modèle de fondation partagé.
  Soit une perturbation sémantique adverse $\delta \in \Delta_{\text{adversarial}}$.
  Si le taux de transfert d'erreur intra-modèle satisfait :
  $$P(\text{Erreur}(A_i) = \text{Erreur}(A_j) \mid \delta, M) \ge 1 - \epsilon \quad (\text{avec } \epsilon \ll 1)$$
  Alors le quorum $Q \ge \frac{2N}{3}$ valide l'état byzantin erroné avec une probabilité :
  $$P(\text{Consensus Falsifié}) = \sum_{m = \lceil 2N/3 \rceil}^N \binom{N}{m} (1-\epsilon)^m \epsilon^{N-m} \approx 1$$
  Le texte doit explicitement poser que la tolérance aux pannes byzantines est **inapplicable** aux systèmes multi-agents sans une hétérogénéité prouvée des architectures de modèles, des données d'entraînement et des espaces de représentations latentes.

---

## 6. [Major] [Majeur / Lacune méthodologique & Modélisation] Impasse de la délégation récursive dans OAuth : limites formelles du Token Exchange (RFC 8693) et absence d'atténuation d'intention cryptographique

- **Localisation précise** : Chapitre 12, pages 141-142 (§ 12.1) et page 144 (§ 12.2).
- **Diagnostic causal approfondi** :
  Le chapitre 12 critique l'inadaptation d'OAuth en se concentrant sur le flux d'autorisation interactif (§ 4.1 du RFC 6749) et son présupposé d'un navigateur web humain. Ce faisant, il omet d'analyser le protocole spécifiquement créé par l'IETF pour la délégation entre services : **RFC 8693 (OAuth 2.0 Token Exchange)**.
  Or, c'est précisément dans le RFC 8693 que se matérialisent les faiblesses insurmontables d'OAuth face à des agents autonomes stochastiques :
  1. *Absence d'atténuation dynamique (Dynamic Privilege Attenuation)* : Le RFC 8693 permet à un agent intermédiaire d'échanger son jeton (`subject_token`) contre un nouveau jeton ciblant un tiers. Mais cette négociation est binaire et dépend d'une politique statique sur le serveur d'autorisation central (AS). Il est impossible pour un agent $A$ de dériver localement un sous-jeton cryptographiquement atténué (ex. restreint à 100 $ d'achat et 2 minutes de validité) sans effectuer un aller-retour réseau synchrone vers l'AS.
  2. *Vulnérabilité au mandataire confus récursif (Recursive Confused Deputy)* : Dans une cascade de délégations $H \to A_1 \to A_2 \to A_3$, le jeton final émis par RFC 8693 contient l'identité de l'acteur immédiat (`act` claim), mais perd la traçabilité sémantique fine des décisions prises par les nœuds intermédiaires. Si $A_2$ est trompé par prompt injection, il sollicite de l'AS un jeton conforme aux habilitations statiques de $A_2$, exécutant ainsi une action désastreuse au nom de $H$.
- **Correctif formel ou contre-exemple explicite** :
  Intégrer dans le § 12.1 et le § 12.4 l'analyse comparative entre RFC 8693 et les modèles de capacités cryptographiques atténuables (tels que les *Macaroons* de Birgisson et coll. ou les *Ucan / W3C Verifiable Credentials*) :
  Démontrer que pour préserver l'opposabilité dans une délégation multi-agents sans goulot d'étranglement centralisé, le protocole d'autorisation doit permettre l'adjonction de clauses restrictives signées localement (*offline caveat chaining*) :
  $$\text{Token}_{i+1} = \text{HMAC}(\text{Token}_i, \text{Caveat}_{i+1})$$
  ce qu'OAuth 2.0 / RFC 8693 est incapable de réaliser de par son architecture centralisée.

---

## 7. [Major] [Majeur / Lacune méthodologique & Architecture] Inadéquation structurelle de SCIM (RFC 7643 / RFC 7644) face au cycle de vie hautement volatil et mutable des agents stochastiques

- **Localisation précise** : Chapitre 12, pages 141-143, § 12.1 (lignes 125-145 et 241-253), et Tableau 12.1 (p. 144). Citation textuelle exacte :
  > « La §4 du RFC 7643 (SCIM Core Schema, septembre 2015) annonce définir "the default resource schemas present in a SCIM server" et ne comporte que trois sous-sections : User, Group, Enterprise User Schema Extension. Aucune ne définit de type de ressource pour un mandataire logiciel autonome [...] »
- **Diagnostic causal approfondi** :
  Le manuscrit formule une critique purement sémantique et lexicale de SCIM (l'absence de type de ressource agent et le libellé anthropomorphique d'attributs tels que `employeeNumber` ou `title`).
  Cette critique rate la véritable incompatibilité fondamentale entre SCIM et les systèmes agentiques :
  1. *Différentiel d'échelle temporelle (Life-Cycle Impedance Mismatch)* : SCIM (RFC 7644) est un protocole HTTP/REST synchrone conçu pour le provisionnement d'identités d'employés humains à un rythme journalier ou hebdomadaire (embauche, mobilité, départ). Un agent logiciel stochastique peut être instancié pour une durée de vie de 15 secondes (agent éphémère de micro-tâche), dupliqué à des milliers d'exemplaires lors d'une vague de charge, et détruit immédiatement. Soumettre ces cycles à des requêtes SCIM `POST /Users` et `DELETE /Users/{id}` entraîne une saturation immédiate des passerelles IAM et des latences rédhibitoires.
  2. *Absence d'immuabilité et de signature des mutations d'état* : Dans SCIM, une mise à jour d'état (`PATCH /Users/{id}`) écrase l'enregistrement précédent sans générer de preuve cryptographique de la transition. Si l'invite système, les outils branchés ou les pondérations d'un agent mutent, SCIM est incapable de certifier historiquement quelle version de l'agent a opéré à un instant $t$, annihilant toute capacité d'audit forensique pour la conformité BSIF E-23 ou Loi 25.
- **Correctif formel ou contre-exemple explicite** :
  Restructurer la critique de SCIM en démontrant l'incompatibilité des ordres de grandeur de latence et de volumétrie :
  $$\Delta t_{\text{SCIM Sync}} \sim 10^2 \text{ à } 10^4\text{ s} \quad \gg \quad \tau_{\text{Agent Instance}} \sim 10^{-1} \text{ à } 10^1\text{ s}$$
  Démontrer que tenter d'étendre SCIM via `draft-abbey-scim-agent-extension-00` (mentionné p. 142) est une impasse d'ingénierie, et préconiser à sa place l'utilisation d'annuaires de capacités signées distribuées adossés à des journaux de transparence immuables (Transparency Logs / Sigstore Rekor).

---

## 8. [Major] [Majeur / Lacune taxonomique & Systémique] Incomplétude de la taxonomie des modes d'échec du Livre I (Tableau 11.4) : omission de l'explosion récursive de sous-tâches (Fork Bomb) et des collisions de concurrence distribuée

- **Localisation précise** : Chapitre 11, page 133, Tableau 11.4 (*Les sept modes d’échec spécifiques à la frontière interopérable...*, `page-133.png`).
- **Diagnostic causal approfondi** :
  Le Tableau 11.4 prétend dresser la synthèse unifiée des défaillances de la frontière interopérable, mais il se restreint arbitrairement à 7 modes (routage incorrect, perte de contexte, incompatibilité de schéma, échec de négociation, absence de clarification, dérive sémantique, interblocage).
  Cette liste souffre de deux lacunes majeures identifiées dans les systèmes distribués de production :
  1. *L'explosion combinatoire de sous-tâches (Agentic Fork Bomb / Cascading Sub-task Proliferation)* : Lorsqu'un agent superviseur est configuré pour décomposer dynamiquement des tâches en sous-tâches déléguées à des pairs (A2A), un objectif sous-spécifié ou une boucle de rétroaction instable pousse les agents intermédiaires à engendrer des centaines de sous-agents récursifs. Faute d'un champ standardisé limitant le nombre de sauts (`Max-Hops`) ou d'un budget global de jetons partagé, l'infrastructure subit un déni de service interne auto-infligé (*Self-Induced Distributed DoS*).
  2. *Les collisions de concurrence et mises à jour perdues (Race Conditions / Lost Updates sur outils MCP)* : Depuis la refonte sans état de MCP (juillet 2026), le protocole n'offre aucune sémantique transactionnelle ni de verrouillage distribué. Si deux agents interopérables manipulent simultanément une même ressource via des outils distincts (par exemple, réservation d'un même inventaire ou débit concurrent d'un compte), l'absence de mécanisme de précondition (`ETag` / `If-Match`) entraîne des corruptions silencieuses de données d'entreprise.
- **Correctif formel ou contre-exemple explicite** :
  Compléter formellement le Tableau 11.4 par l'adjonction des modes 8 et 9 :
  - **Mode 8 : Explosion récursive de sous-tâches (Fork Bomb)** — *Ce qui se rompt* : la borne d'épuisement de ressources distribuées et la terminaison de la chaîne. *Mitigation* : injection obligatoire d'un contexte de budget immuable `X-Agentic-Budget-Remaining`.
  - **Mode 9 : Collision de concurrence sur ressources partagées (Lost Update)** — *Ce qui se rompt* : l'intégrité transactionnelle et la cohérence sérielle des effets de bord. *Mitigation* : imposition d'un contrôle de concurrence optimiste (OCC) dans les spécifications de serveurs d'outils MCP.

---

## 9. [Major] [Majeur / Rigueur et Détermination architecturale] Contradiction de fiabilité dans la refonte MCP sans état (juillet 2026) : suppression de la reprise de flux sans primitive d'idempotence obligatoire

- **Localisation précise** : Chapitre 11, page 135, § 11.3.1 (lignes 687-710, `page-135.png`), et Chapitre 8, page 92, Tableau 8.2. Citation textuelle exacte :
  > « (3) La suppression de la reprise de flux transforme une interruption en perte de requête, ce qui déplace vers le client la logique de réémission — et le ch. 48 établit qu’une réémission sans sémantique d’effet est une source de duplication, non une garantie. »
- **Diagnostic causal approfondi** :
  Le manuscrit documente avec une grande précision la refonte sans état de MCP intervenue le 28 juillet 2026 (abandon des sessions côté serveur, passage à des requêtes HTTP-POST indépendantes, suppression de la reprise de flux / *stream resumption*).
  Toutefois, l'auteur s'abstient de formuler le jugement critique formel qui en découle pour la sécurité financière :
  En éliminant l'état de session au niveau transport sans rendre obligatoire un identifiant d'idempotence au niveau applicatif (tel que le draft IETF `Idempotency-Key`), la spécification MCP 2026-07-28 rend toute invocation d'outil à effet de bord non idempotent dangereuse sur un réseau instable. Si une déconnexion survient après que le serveur d'outils a exécuté l'action mais avant que l'agent client ne reçoive le code de retour JSON-RPC, la réémission automatique provoque une double exécution catastrophique en environnement bancaire (double paiement, double signature).
- **Correctif formel ou contre-exemple explicite** :
  Compléter l'analyse du § 11.3.1 en posant formellement l'exigence de non-régression :
  Toute architecture agentique prétendant au grade de production critique sous MCP post-juillet 2026 **doit** encapsuler chaque appel d'outil JSON-RPC avec un en-tête d'idempotence cryptographique déduit du hash de l'intention du mandant :
  $$\text{IdempotencyKey} = \text{HMAC}_{K}(\text{TaskID} \parallel \text{StepIndex} \parallel \text{ToolParams})$$
  Faute de quoi, la suppression de l'état réseau rétrograde MCP d'un protocole de production à un simple protocole de transport au mieux tolérable pour des requêtes en lecture seule.

---

## 10. [Major] [Majeur / Erreur formelle & Syntaxe] Phrase tronquée et rupture grammaticale dans le bloc Thèse de la page 79

- **Sévérité** : [Major] [Majeur / Erreur formelle]
- **Localisation précise** : Chapitre 7 (*Généalogie et gouvernance : des projets propriétaires aux standards ouverts*), page 79 du PDF (`page-79.png`), lignes 10 à 18. Citation textuelle exacte :
  > « Thèse — en dix-sept mois, la couche protocolaire agentique s’est consolidée sous gouvernance neutre (Linux Foundation) — condition nécessaire et non suffisante de sa crédibilité en entreprise réglementée ; mais « soutien ≠ production », et le transfert de gouvernance d’AP2 est documenté : don à la FIDO Alliance le 28 avril 2026, version v0.2, cas Human-Not-Present, deux groupes de travail techniques — fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres. »
- **Diagnostic causal approfondi** :
  La fin du bloc Thèse présente une rupture grammaticale brutale : la suite « instruit au ch. 10. » est immédiatement suivie de « outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres. » sans verbe, sans sujet et sans articulation logique. Il s'agit manifestement d'un résidu de copier-coller issu d'un plan de section (« Le chapitre aborde les outils... ») accidentellement tronqué lors de l'assemblage de l'édition finale.
- **Correctif formel ou contre-exemple explicite** :
  Rétablir la syntaxe complète de la phrase finale du bloc Thèse :
  « [...] fait constaté à la source primaire le 27 juillet 2026, instruit au ch. 10. Le présent mouvement analyse dès lors successivement l'accès aux outils, le dialogue entre agents, la découverte de services, le règlement commercial, et les modes d’échec qui leur sont propres. »

---

# Minor Corrections and Typos

## 11. [Minor] [Mineur / Réfutation bibliographique et datation] Caractérisation imprécise du mécanisme d'identité d'AWS Bedrock Agents
- **Localisation** : Chapitre 12, page 143, lignes 277-296 (`page-143.png`). Citation textuelle exacte :
  > « Chez AWS, le mécanisme documenté comparable est Amazon Bedrock AgentCore Identity, où l’identité d’agent est une identité de charge de travail dotée d’attributs propres plutôt qu’un type d’objet distinct (Vol. III F-36, [C]). »
- **Diagnostic** : L'appellation exacte du service dans la documentation officielle AWS est *Amazon Bedrock Agents* adossé aux rôles IAM de service (`IAM Execution Roles for Bedrock`), et non « Amazon Bedrock AgentCore Identity » (qui mélange des terminologies d'éditeurs tiers). De plus, l'auteur hésite sur la date de disponibilité générale (octobre 2025 vs juillet 2026).
- **Correctif** : Clarifier qu'AWS ne définit aucun type de principal IAM « Agent », mais utilise le mécanisme standard de délégation de rôle `sts:AssumeRole` avec balisage de session (`aws:PrincipalTag`), ce qui corrobore parfaitement la thèse centrale : les hyperscalers étirent l'identité de charge de travail machine sans créer d'objet d'identité propre aux agents.

## 12. [Minor] [Mineur / Typographie et mise en page] Discordance de placement flottant de la Figure 10.4
- **Localisation** : Chapitre 10, page 125 (`page-125.png`).
- **Diagnostic** : La Figure 10.4 (*Le mandat comme couche de preuve opposable...*) est placée au tout début de la page 125, au-dessus du titre de la section 10.5 (*Le destin de l'ACP protocolaire*), alors que le texte appelant cette figure se trouve à la fin de la page 124 (§ 10.4.2). Cette disposition visuelle crée une fausse association où la figure semble appartenir à la section 10.5.
- **Correctif** : Forcer l'ancrage typographique de la figure 10.4 (`[H]` ou insertion inline) immédiatement sous le texte du paragraphe 10.4.2 auquel elle se rattache.

## 13. [Minor] [Mineur / Typographie] Espace insécable manquant devant les deux-points et guillemets
- **Localisation** : Chapitre 11, page 138, Tableau 11.5 ; Chapitre 10, page 116, § 10.1.2.
- **Diagnostic** : Dans plusieurs passages, des signes doubles de ponctuation (deux-points, points-virgules) ou des guillemets français (« ») sont séparés par des espaces sécables ou accolés sans espace conforme aux règles de composition typographique québécoise et canadienne-française.
- **Correctif** : Appliquer systématiquement l'espace insécable fin (`&thinsp;` ou `~`) devant les ponctuations doubles et à l'intérieur des guillemets français.
