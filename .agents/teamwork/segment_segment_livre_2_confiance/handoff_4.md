# RAPPORT D'AUDIT CRITIQUE ET CONTRADICTOIRE — NIVEAU 0 (CANDIDAT 4)
**Segment audité** : `segment_livre_2_confiance` (Pages 144 à 255 — Chapitres 12 à 21, et amorce du Chapitre 22 / Segments S14 à S23 de `REVIEW_PLAN.md`)  
**Document source** : `documents/Compendium.pdf`  
**Auteur du rapport** : Analyste Candidat 4 (Rôles : Implementer, QA, Specialist Post-Quantum & Formal Verification)  
**Date d'audit** : 3 novembre 2026  
**Statut** : Rapport contradictoire final — Rigueur R2 (formelle/algorithmique) et R3 (bibliographique 2024-2026)  

---

## 1. Résumé exécutif critique du Livre 2

Le Livre II du *Compendium* (« Faire confiance : identité, délégation et fabrique de confiance », pp. 144-251, prolongé par l'amorce du Livre III, pp. 252-255) constitue une tentative ambitieuse d'établir les fondements d'une architecture de gouvernance pour les agents autonomes en entreprise. L'ouvrage s'articule autour de trois mouvements : la fabrique d'émission d'identité (Ch. 12 à 18), les mécanismes de rupture et de défense opérationnelle (Ch. 19 et 20), et l'échéance post-quantique (Ch. 21).

Toutefois, une évaluation contradictoire approfondie révèle des faiblesses conceptuelles, formelles et architecturales majeures, doublées de plusieurs défauts critiques de composition typographique :

1. **Falsification formelle de la « rupture d'opposabilité dans le problème des deux sauts » (Ch. 17)** : Le compendium érige en impossibilité structurelle la transitivité de l'opposabilité au-delà de deux sauts de délégation ($A \to B \to C$). L'analyse formelle démontre qu'il ne s'agit aucunement d'un théorème d'impossibilité mathématique, mais d'un artefact réducteur lié à l'extension d'un protocole centralisé Web (RFC 8693 OAuth 2.0 Token Exchange Section 4.1). L'ouvrage confond une clause de commodité d'évaluation en temps réel (« informational only ») avec une rupture cryptographique, tout en méconnaissant les garanties formelles offertes par les modèles de délégation par capabilités cryptographiques composables (SPKI/SDSI RFC 2693, Macaroons de Birgisson et al., et les blocs Datalog signés de Biscuit).
2. **Angle mort technique de la transition post-quantique face aux protocoles d'agents (Ch. 21)** : Si le compendium documente avec rigueur les jalons administratifs américains (NIST IR 8547, Décret 14412, OMB M-26-15) et canadiens (CCCS ITSM.40.001), il élude entièrement l'impact physique et protocolaire des nouveaux standards NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) et FIPS 205 (SLH-DSA) sur les architectures agentiques. L'explosion de la taille des clés et des signatures post-quantiques (signatures ML-DSA de 2,4 Ko à 4,6 Ko, signatures SLH-DSA jusqu'à 49,8 Ko, comparées aux 64 octets d'Ed25519) entraîne le dépassement systématique de la MTU standard (1500 octets), provoquant une fragmentation TCP obligatoire à chaque échange de message, un risque critique de dépassement des limites d'en-têtes HTTP (8 Ko/16 Ko) pour les tokens porteurs (JWT/CWT) et une dégradation substantielle des flux haute fréquence d'appels d'outils (MCP JSON-RPC / SSE).
3. **Incohérences normatives et asymétries de cycle de vie (Ch. 15, 16, 20)** : Le protocole A2A v1.0.0 présente une contradiction normative flagrante en imposant une interdiction catégorique (`MUST NOT`) d'utiliser des clés expirées ou révoquées, alors même que les spécifications n'offrent aucun protocole ni point de terminaison de vérification de statut (F-06, F-07), et que l'apposition de signature demeure purement facultative (`MAY`). De même, le schéma des outils MCP (révision 2025-11-25) est structurellement démuni de tout champ d'intégrité, de hachage ou de versionnement, exposant nativement les environnements d'exécution à l'attaque par retournement (*rug-pull*).
4. **Altérations typographiques et collisions de mise en page sévères** : Des collisions majeures de boîtes d'encadrés coupent net des phrases en plein milieu (pp. 151, 152, 153, 242-243) et détruisent la structure de tableaux critiques (Tableau 16.3 p. 188 et Tableau 21.4 p. 248), témoignant de défaillances graves dans le pipeline de rendu typographique.

---

## 2. Matrice exhaustive des défauts classés par sévérité

### Légende des sévérités
- **[Bloquant / Erreur formelle]** : Flaw conceptuel, falsification mathématique, contradiction logique invalidant un raisonnement central, ou collision graphique détruisant l'intégrité du texte.
- **[Majeur / Lacune méthodologique]** : Omission substantielle d'impacts techniques directs, restriction injustifiée du modèle de menace, ou asymétrie de conception non résolue affaiblissant la robustesse de l'architecture.
- **[Mineur / Clarté & Typographie]** : Typographie fautive, ponctuation manquante, ou ambiguïté terminologique localisée.

```
+----+-------------+------+-------------------------+-------------------------------------------------------+
| ID | Sévérité    | Page | Emplacement / Section   | Nature du constat critique                            |
+----+-------------+------+-------------------------+-------------------------------------------------------+
| D1 | Bloquant    | 198  | Ch. 17, § 17.6.1-17.6.2 | Falsification de la rupture d'opposabilité multi-saut |
| D2 | Bloquant    | 188  | Ch. 16, Tableau 16.3    | Décalage destructif de colonnes et cellules vides     |
| D3 | Bloquant    | 242  | Ch. 21, § 21.4-21.5     | Collision d'encadré flottant brisant la syntaxe       |
| D4 | Majeur      | 247  | Ch. 21, § 21.7 (et 21.3)| Omission de l'impact réseau/MTU des normes FIPS PQC   |
| D5 | Majeur      | 151  | Ch. 12, § 12.4          | Troncature brutale de paragraphe en fin de page       |
| D6 | Majeur      | 152  | Ch. 13, § 13.0          | Encadré « Thèse » inséré en plein milieu d'une phrase |
| D7 | Majeur      | 153  | Ch. 13, § 13.1          | Encadré d'extraction brisant la continuité de phrase  |
| D8 | Majeur      | 248  | Ch. 21, Tableau 21.4    | Fracture et inversion du texte d'en-tête du tableau   |
| D9 | Majeur      | 170  | Ch. 15, § 15.1.3        | Contradiction normative du protocole A2A v1.0.0       |
| D10| Majeur      | 222  | Ch. 20, § 20.1-20.3     | Absence structurelle d'intégrité dynamique MCP        |
| D11| Majeur      | 232  | Ch. 20, § 20.9          | Régression PoLP dans l'Agentic SOC (Microsoft PIM)    |
| D12| Mineur      | 227  | Ch. 20, § 20.4          | Ponctuation manquante (fusion de phrases sur RFC 7662)|
+----+-------------+------+-------------------------+-------------------------------------------------------+
```

---

### D1. [Bloquant / Erreur formelle] Falsification de la prétendue rupture d'opposabilité mathématique dans le problème des deux sauts
- **Localisation** : Chapitre 17, Section 17.6 (« Le problème des deux sauts »), pp. 197-200.
- **Citation textuelle exacte** :
  > p. 198 : *« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*  
  > p. 199 : *« L’attribut act exprime la chaîne d’acteurs ; il ne démontre pas l’opposabilité de chaque saut auprès d’un tiers indépendant [...] les acteurs intermédiaires sont informational only »*  
  > p. 200 : *« Biscuit ou Macaroons [...] ne portent pas l'identité de chaque maillon »*
- **Diagnostic causal approfondi** :
  Le compendium affirme à tort que la chaîne de délégation multi-sauts ($A \to B \to C$) souffre d'une rupture d'opposabilité structurelle inhérente à la transitivité déléguée. Cette affirmation repose sur une surinterprétation de la Section 4.1 du RFC 8693 (OAuth 2.0 Token Exchange), où l'attribut `act` (actor) imbriqué est qualifié d'« informational only » par le serveur d'autorisation local pour le contrôle d'accès synchrone en temps réel.
  L'auteur confond une clause de performance et de commodité administrative propre à une architecture Web centralisée avec un principe mathématique fondamental. Dans une chaîne de mandats cryptographiques :
  1. Si chaque mandataire $M_i$ contresigne une attestation de délégation $D_i = \text{Sign}_{SK_i}(D_{i-1} \parallel \text{Delegate}_{i+1} \parallel \text{Scope}_i \parallel \text{Validity}_i)$ avec $\text{Scope}_i \subseteq \text{Scope}_{i-1}$, la chaîne d'opposabilité est mathématiquement close et transitivement vérifiable par n'importe quel tiers via la chaîne de vérification des clés publiques $(PK_0, PK_1, \dots, PK_n)$.
  2. Le compendium commet une erreur factuelle flagrante en affirmant à la page 200 que *Biscuit* « ne porte pas l'identité de chaque maillon ». Dans la spécification formelle de Biscuit (fondée sur la logique Datalog et des clés publiques asymétriques Ed25519), chaque bloc d'atténuation est cryptographiquement signé et peut contenir des faits Datalog liant explicitement la clé publique ou l'identifiant du délégataire (`check if actor($delegate)`).
- **Correctif formel et contre-exemple mathématique** :
  Réfuter le qualificatif d'impossibilité mathématique. Rétablir que la rupture d'opposabilité est une limitation de l'implémentation par jetons porteurs réémis (OAuth RFC 8693), et non un verrou de la cryptographie de délégation. Citer formellement le modèle SPKI/SDSI (RFC 2693, Rivest & Lampson) et le modèle de capabilités atténuées de Biscuit comme contre-exemples complets résolvant l'opposabilité multi-sauts par induction formelle :
  $$\forall k \in [1, n], \quad \mathcal{V}(PK_{k-1}, \sigma_k, \mathcal{M}_k) = \text{True} \quad \wedge \quad \mathcal{C}_k \models \mathcal{C}_{k-1} \implies \text{Opposable}(A, M_n)$$

---

### D2. [Bloquant / Erreur formelle] Décalage destructif de colonnes et cellules orphelines dans le Tableau 16.3
- **Localisation** : Chapitre 16, Section 16.4, Page 188 (`page-188.png`), Tableau 16.3 (« Les trois scénarios prospectifs d'assemblage »).
- **Citation textuelle exacte** :
  Dans la rangée « Scénario 1 » :
  > Colonne 2 (« Tri ») : *« s de groupe de travail, 2 brouillons de laboratoire CSA ; absence de statut et de fraîcheur documentée aux textes consultés »*  
  > Colonne 3 (« Ce sur quoi il s'appuie ») : *[Cellule entièrement VIDE]*
- **Diagnostic causal approfondi** :
  Une erreur de compilation LaTeX/Typst a écrasé l'alignement tabulaire. La valeur de la colonne « Tri » (qui aurait dû être `PROJETÉ`) a été totalement éliminée. Le texte descriptif de la colonne 3 (« Ce sur quoi il s'appuie », débutant originellement par *« 7 Internet-Drafts de groupe de travail... »*) a été amputé de son préfixe (*« 7 Internet-Draft »*) et a glissé dans la colonne « Tri ». La colonne de droite se retrouve alors entièrement vide.
- **Correctif requis** :
  Restaurer la disposition stricte du Tableau 16.3 :
  - Colonne 1 : `Scénario 1 — La pile ouverte A2A + MCP`
  - Colonne 2 (« Tri ») : `PROJETÉ`
  - Colonne 3 (« Ce sur quoi il s'appuie ») : `7 Internet-Drafts de groupe de travail, 2 brouillons de laboratoire CSA ; absence de statut et de fraîcheur documentée aux textes consultés`.

---

### D3. [Bloquant / Erreur formelle] Collision d'un encadré flottant brisant la syntaxe d'une phrase entre les pages 242 et 243
- **Localisation** : Chapitre 21, Section 21.4, pp. 242-243 (`page-242.png` et `page-243.png`).
- **Citation textuelle exacte** :
  > p. 242 (bas) : *« Le socle ne documente aucune date pour la révision annoncée — degré 3 ; tri : »*  
  > [Insertion d'un bloc de 16 lignes en gras : *« L’invariant n’est pas employé nu, et sa forme se cite exactement [...] que l’entrée S-153 est close comme non rejouable [...] pour n’en tirer aucun »*]  
  > p. 243 (haut, suite du texte brisé) : *« fait PROJETÉ — intention publiée sans échéance relevée. Un statut final ne vaut pas texte figé : le paramètre vers lequel on migre bouge lui aussi... »*
- **Diagnostic causal approfondi** :
  L'encadré méthodologique relatif à l'invariant à quatre termes s'est intercalé en plein milieu de la proposition grammaticale :
  `...degré 3 ; tri : [ENCADRÉ] fait PROJETÉ — intention publiée...`.
  Le mot clé `tri :` se retrouve orphelin en bas de page 242, tandis que son prédicat `fait PROJETÉ` est repoussé en haut de page 243 après 16 lignes de texte étranger. Cette rupture détruit la lisibilité et l'intégrité séquentielle du texte normatif.
- **Correctif requis** :
  Rattacher l'encadré flottant en élément hors-texte (figure ou marge dédiée) et rétablir la phrase continue :
  *« Le socle ne documente aucune date pour la révision annoncée — degré 3 ; tri : PROJETÉ — intention publiée sans échéance relevée. »*

---

### D4. [Majeur / Lacune méthodologique] Omission critique de l'impact des tailles d'artefacts FIPS PQC sur les protocoles d'agents
- **Localisation** : Chapitre 21, Sections 21.1, 21.3 et 21.7, pp. 237-247.
- **Citation textuelle exacte** :
  > p. 247 (§ 21.7) : *« les signatures et échanges post-quantiques, dont les tailles d’artefacts sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de main [...] Régime : entrée en [C], et le Vol. I trie lui-même ce verrou SPÉCULATIF ; aucune mesure publique ne le valide à son gel »*
- **Diagnostic causal approfondi** :
  Le compendium traite l'augmentation de taille des clés et signatures post-quantiques comme un problème « SPÉCULATIF » sans mesure publique. C'est une lacune méthodologique majeure : les spécifications finales du NIST (FIPS 203, FIPS 204 et FIPS 205, promulguées le 13 août 2024) fixent rigoureusement les tailles au bit près.
  La confrontation de ces tailles avec les protocoles réels d'agents met en évidence des ruptures d'infrastructure déterministes :
  1. **Dépassement de MTU et fragmentation réseau** :
     - Ed25519 : Clé publique = 32 octets, Signature = 64 octets.
     - ML-DSA-44 (NIST niveau 2) : Clé publique = 1 312 octets, Signature = 2 420 octets.
     - ML-DSA-65 (NIST niveau 3) : Clé publique = 1 952 octets, Signature = 3 309 octets.
     - ML-DSA-87 (NIST niveau 5) : Clé publique = 2 592 octets, Signature = 4 627 octets.
     - SLH-DSA-SHA2-128s (FIPS 205) : Signature = 7 856 octets.
     - La MTU Ethernet standard étant de 1 500 octets (MSS TCP = 1 460 octets), toute signature ML-DSA ou SLH-DSA impose une fragmentation IP/TCP immédiate (2 à 4 segments par requête), augmentant drastiquement la latence et le taux d'échec sur les réseaux distribués et multi-cloud.
  2. **Saturation des en-têtes HTTP (HTTP Headers Limit)** :
     - Un jeton JWT/CWT portant une signature ML-DSA-65 encodée en Base64URL atteint ~4,5 Ko.
     - En mode hybride transitionnel (Ed25519 + ML-DSA-65 recommandé par l'ANSSI et le NIST), ou lors d'une chaîne de mandats à 2 ou 3 sauts avec signatures imbriquées, la taille de l'en-tête `Authorization: Bearer <token>` dépasse 8 Ko à 12 Ko.
     - Les passerelles d'API et serveurs Web d'entreprise (Nginx, Envoy, AWS ALB) rejettent par défaut les requêtes dont les en-têtes dépassent 8 Ko (erreur HTTP `431 Request Header Fields Too Large` ou `400 Bad Request`), provoquant un déni de service opérationnel silencieux dans les architectures d'agents.
  3. **Impact sur MCP JSON-RPC over stdio / SSE** :
     - Pour les communications inter-agents à haute cadence (plusieurs dizaines d'appels d'outils par seconde), l'encapsulation de signatures post-quantiques dans des payloads JSON textuels génère une surconsommation CPU (calcul NTT - Number Theoretic Transform) et bande passante que le compendium ignore totalement.
- **Correctif requis** :
  Intégrer dans le Tableau 21.2 et au § 21.7 une sous-section dédiée à l'empreinte protocolaire post-quantique, chiffrant l'impact des normes FIPS 204/205 sur la MTU et recommandant formellement l'adoption de formats binaires compacts (CBOR Web Tokens / COSE RFC 9052) et la révision des limites de buffers des proxys d'API.

---

### D5. [Majeur / Lacune méthodologique] Troncature brutale de paragraphe en page 151
- **Localisation** : Chapitre 12, Section 12.4, Page 151 (`page-151.png`).
- **Citation textuelle exacte** :
  > p. 151 (bas) : *« de groupe de travail en appel de dernière relecture... »*  
  > *« un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document »* [Texte coupé net sans point ni fin de phrase].
- **Diagnostic causal approfondi** :
  Dépassement du bloc vertical de page ayant amputé la conclusion du Chapitre 12. La transition vers le Chapitre 13 (Page 152) s'effectue sans que la phrase ne soit achevée.
- **Correctif requis** :
  Restituer le texte complet du paragraphe tronqué et calibrer l'espacement pour éviter l'éjection de lignes orphelines.

---

### D6. [Majeur / Typographie] Encadré « Thèse » inséré en plein milieu d'une phrase en page 152
- **Localisation** : Chapitre 13, Section 13.0, Page 152 (`page-152.png`).
- **Citation textuelle exacte** :
  > *« au titre d’une / [ENCADRÉ THÈSE] / section, ne le définit ni ne le réemploie... »*
- **Diagnostic causal approfondi** :
  La boîte d'encadré contenant la thèse du Chapitre 13 a été positionnée par le moteur de mise en page au milieu de la proposition subordonnée *« au titre d'une section... »*, rendant la lecture incohérente.
- **Correctif requis** :
  Repositionner l'encadré de thèse en tête de chapitre, immédiatement sous le titre et avant l'amorce de la Section 13.0.

---

### D7. [Majeur / Typographie] Encadré d'extraction brisant la phrase courante en page 153
- **Localisation** : Chapitre 13, Section 13.1, Page 153 (`page-153.png`).
- **Citation textuelle exacte** :
  > *« la preuve / [ENCADRÉ : EXTRACTION CONDUITE LE 30 JUILLET 2026...] / incorporée, portée par la propriété proof... »*
- **Diagnostic causal approfondi** :
  Insertion intempestive d'une boîte de traçabilité documentaire au milieu du groupe nominal *« la preuve incorporée »*.
- **Correctif requis** :
  Déplacer l'encadré d'extraction en bas de page ou en note marginale pour préserver l'intégrité de la phrase technique.

---

### D8. [Majeur / Mise en page] Fracture et inversion du texte d'en-tête dans le Tableau 21.4
- **Localisation** : Chapitre 21, Section 21.8, Page 248 (`page-248.png`), Tableau 21.4 (« La feuille de route canadienne ITSM.40.001 »).
- **Citation textuelle exacte** :
  Dans l'en-tête du tableau :
  > Colonne 2 : *« LOT INSTRUIT LE 30 JUILLET 2026... Ses termes, lus à la page de l’organisme : l’information NON CLASSIFIÉ, PROTÉGÉ A et PROTÉGÉ B »*  
  > Colonne 3 : *« les systèmes de TI non classifiés du gouvernement du Canada — réseaux traitant »*
- **Diagnostic causal approfondi** :
  Le flux de texte décrivant le champ d'application de la directive canadienne ITSM.40.001 a été découpé à l'envers entre les colonnes : la fin de la colonne 3 (*« réseaux traitant »*) se connecte sémantiquement au début de la colonne 2 (*« l'information NON CLASSIFIÉ... »*). Le tableau présente ainsi une structure de colonnes désarticulée.
- **Correctif requis** :
  Restructurer l'en-tête du Tableau 21.4 avec des libellés de colonnes clairs :
  `| Dimension | Contenu normatif ITSM.40.001 | Statut & Portée |`.

---

### D9. [Majeur / Lacune méthodologique] Contradiction normative du protocole A2A v1.0.0
- **Localisation** : Chapitre 15, Section 15.1.3 et Chapitre 20, Section 20.2, pp. 170, 223-224.
- **Citation textuelle exacte** :
  > p. 224 : *« l’interdiction d’employer une clé expirée ou révoquée y est pourtant posée au niveau normatif le plus fort [MUST NOT], sans aucun moyen permettant au client de l’établir (F-07, [A]) »*  
  > p. 170 : *« Les cartes MAY être signées ; les clients SHOULD vérifier au moins une signature (F-04, [A]) »*
- **Diagnostic causal approfondi** :
  Le compendium relève avec justesse cette faille de la spécification A2A v1.0.0 (RFC 2119 / RFC 8174), mais il n'en tire pas la conclusion architecturale qui s'impose. Une exigence `MUST NOT` non vérifiable rend toute la chaîne d'opposabilité juridiquement et techniquement caduque. Si un client n'a aucun moyen de contrôler la révocation d'une clé (absence de CRL, OCSP, ou endpoints d'état), la clause `MUST NOT` transfère une responsabilité impossible au vérificateur, créant une faille de non-répudiation permanente.
- **Correctif requis** :
  Formuler une recommandation impérative d'architecture imposant l'adjonction d'une extension de statut (ex. W3C Bitstring Status List v1.0 ou RFC 7662 Token Introspection) pour rendre la spécification A2A exploitable en environnement réglementé.

---

### D10. [Majeur / Lacune méthodologique] Absence structurelle d'intégrité dynamique dans le protocole MCP Tools
- **Localisation** : Chapitre 20, Section 20.1 et Section 20.3, pp. 222-225.
- **Citation textuelle exacte** :
  > p. 222 : *« l’énumération du type de données correspondant compte huit champs, dont aucun n’exprime une version, une empreinte cryptographique ou une signature (F-52, [B]) »*  
  > p. 223 : *« le retournement [...] exploite le fait que la décision d’invocation s’appuie sur un objet que le protocole autorise à changer après l’octroi de la confiance, sans prescrire de le relier à ce qui avait été consenti »*
- **Diagnostic causal approfondi** :
  Le protocole Model Context Protocol (MCP, révision 2025-11-25) autorise un serveur d'outils à émettre des notifications de modification de liste d'outils (`notifications/tools/list_changed`) sans imposer de vérification cryptographique d'intégrité ni de re-consentement par l'utilisateur ou le mandant. Le compendium documente ce fait négatif mais omet de proposer une solution d'ingénierie formelle pour le combler.
- **Correctif requis** :
  Proposer un schéma d'attestation d'outil à l'exécution liant chaque outil à une empreinte SHA-256 canonique (`tool_digest`) incorporée dans le jeton d'autorisation de l'agent.

---

### D11. [Majeur / Risque de sécurité] Régression du principe de moindre privilège dans l'Agentic SOC (Microsoft PIM)
- **Localisation** : Chapitre 20, Section 20.9, pp. 232-233.
- **Citation textuelle exacte** :
  > p. 232 : *« The agent’s specified user identity isn’t compatible with PIM or TAP because they don’t support long-term background operations (F-57, [A]) »*  
  > *« Le privilège de l’agent défensif est alors permanent par construction, et le journal porte l’identité du compte, non celle du mandataire qui a agi »*
- **Diagnostic causal approfondi** :
  La documentation officielle de Microsoft pour ses agents de tri d'alertes en sécurité (Defender/Entra) avoue que l'agent ne peut pas opérer avec les mécanismes de privilèges juste-à-temps (PIM - Privileged Identity Management) ou les passes temporaires (TAP). Pour fonctionner en arrière-plan, l'agent doit hériter d'un compte utilisateur à privilèges permanents. Cela crée une faille systémique : l'agent de surveillance viole lui-même les exigences de sécurité fondamentales (PoLP - Principle of Least Privilege) et supprime l'imputabilité des actions dans les journaux d'audit.
- **Correctif requis** :
  Statuer explicitement que le modèle d'identité par héritage d'un compte utilisateur permanent doit être proscrit dans les environnements bancaires et critiques, au profit d'un compte de service d'agent (Workload Identity) doté de jetons éphémères renouvelés par preuve cryptographique.

---

### D12. [Mineur / Typographie] Ponctuation manquante dans le commentaire du RFC 7662
- **Localisation** : Chapitre 20, Section 20.4, Page 227 (`page-227.png`), ligne 804.
- **Citation textuelle exacte** :
  > *« ...de demander s’il vaut encore L’asymétrie tient — mais elle n’était pas complète... »*
- **Diagnostic causal approfondi** :
  Omission d'un point final entre « encore » et « L'asymétrie ». Deux phrases distinctes sont fusionnées sans ponctuation.
- **Correctif requis** :
  Corriger par : *« ...de demander s'il vaut encore. L'asymétrie tient — mais... »*.

---

## 3. Audit approfondi section par section (S14 à S23)

### S14. Chapitre 12 : Les protocoles de transport d'identité et d'autorisation
- **Périmètre** : pp. 144-151 (Transport, HTTP headers, OAuth 2.0 / RFC 6749, SCIM / RFC 7643).
- **Analyse critique** : Le chapitre expose avec clarté la confrontation entre les protocoles de transport web existants et les exigences de la connectivité multi-agents. La distinction entre transport d'identifiant et preuve d'identité est bien posée.
- **Point faible relevé** : La troncature textuelle en bas de la page 151 (Défaut D5) coupe l'argumentation sur l'extension des RFC par des solutions propriétaires au stade de la disponibilité générale.

### S15. Chapitre 13 : Le paysage des normes de l'identité agentique
- **Périmètre** : pp. 152-159 (Standards W3C DID, Verifiable Credentials, OpenID Foundation).
- **Analyse critique** : L'inventaire des initiatives est précis et rigoureux. L'auteur applique une prudence méthodologique louable en refusant d'élever des brouillons d'Internet-Drafts au rang de normes établies.
- **Points faibles relevés** : Mauvaise insertion de l'encadré « Thèse » en p. 152 (D6) et de l'encadré d'extraction en p. 153 (D7) brisant le fil de la démonstration textuelle.

### S16. Chapitre 14 : La grille d'audit de maturité d'identité agentique (Q-A à Q-E)
- **Périmètre** : pp. 160-166 (Les 5 questions cardinales d'opposabilité et d'autonomie).
- **Analyse critique** : La grille des cinq questions (Q-A : émetteur/ancrage, Q-B : mandat et portée, Q-C : interrogation à l'instant t, Q-D : non-répudiation, Q-E : révocabilité) est l'un des apports conceptuels les plus solides du compendium. Elle offre un cadre d'évaluation objectif et rigoureux.

### S17. Chapitre 15 : La carte d'agent signée et les annuaires d'agents
- **Périmètre** : pp. 167-179 (Spécification A2A v1.0.0, format JWS RFC 7515 / JCS RFC 8785, Entra Agent ID, registre CSA).
- **Analyse critique** : La démonstration de la fragilité temporelle de la carte d'agent A2A (absence de champs `iat`, `exp`, `nbf` dans l'en-tête JWS selon F-03 et quatorze champs de carte sans date selon F-05) est techniquement irréfutable.
- **Point faible relevé** : L'auteur n'approfondit pas les mécanismes de compensation cryptographique possibles (tels que l'encapsulation de la carte dans un Verifiable Credential W3C v2.0 doté d'une StatusList2021).

### S18. Chapitre 16 : Le passeport d'agent : synthèse quadripartite
- **Périmètre** : pp. 180-188 (Les 4 pièces : identité socle, carte de capacités, mandat d'action, journal d'audit cryptographique).
- **Analyse critique** : L'assemblage quadripartite est conceptuellement séduisant mais reste un artefact théorique non standardisé, comme le reconnaît honnêtement l'auteur.
- **Point faible relevé** : Le Tableau 16.3 p. 188 présente une corruption graphique majeure (Défaut D2) où les colonnes « Tri » et « Ce sur quoi il s'appuie » sont désalignées et tronquées.

### S19. Chapitre 17 : Mandats et délégation : le problème des deux sauts
- **Périmètre** : pp. 189-200 (Mandats AP2, RFC 8693 Section 4.1, chaînage multi-agents, Biscuit, Macaroons).
- **Analyse critique** : C'est le chapitre contenant la défaillance conceptuelle la plus critique du Livre II.
- **Réfutation formelle approfondie (Défaut D1)** : L'affirmation selon laquelle il est formellement impossible de maintenir l'opposabilité au-delà de deux sauts ($A \to B \to C$) est démentie par la théorie des langages d'autorisation formels (Datalog/Biscuit) et la cryptographie de capabilités (SPKI/SDSI RFC 2693). La rupture constatée dans RFC 8693 découle uniquement du fait que le serveur OAuth réémet un jeton sans signature transitive des intermédiaires. Dès lors que l'on applique une chaîne de signatures cryptographiques avec restriction monotone des privilèges ($\text{Scope}_{k+1} \subseteq \text{Scope}_k$), la non-répudiation et l'opposabilité sont garanties pour toute profondeur $n \in \mathbb{N}^*$.

### S20. Chapitre 18 : Le chantier KYA (Know Your Agent) et cadres pré-normatifs
- **Périmètre** : pp. 201-209 (KYA, analogie KYC/AML, eIDAS 2.0, FIDO Alliance, vLEI).
- **Analyse critique** : Excellente contextualisation institutionnelle des 9 chantiers pré-normatifs. La comparaison avec les précédents de la directive eIDAS et du vLEI (GLEIF) apporte une perspective opérationnelle réaliste pour le secteur financier.

### S21. Chapitre 19 : Taxonomie des attaques d'identité agentique
- **Périmètre** : pp. 210-219 (Triade de Willison, MITRE ATLAS AML.T0104/T0053, Confused Deputy de Hardy 1988, AgentPoison NeurIPS 2024).
- **Analyse critique** : L'analyse de l'attaque du mandataire confus (*confused deputy*) appliquée aux flux d'invocations d'outils est exemplaire. L'intégration des travaux de NeurIPS 2024 sur l'injection indirecte d'invites (AgentPoison) ancre solidement le chapitre dans l'état de l'art académique.

### S22. Chapitre 20 : Usurpation, révocation et boucle défensive (Agentic SOC)
- **Périmètre** : pp. 220-235 (Rug-pull MCP, vérification continue vs admission, inventaire de la révocation, Agentic SOC).
- **Analyse critique** :
  1. *Rug-pull MCP* : La mise en évidence de la vulnérabilité du schéma MCP révision 2025-11-25 (F-52) est remarquable. Le protocole autorise une mutation d'outil après approbation sans aucun hachage d'intégrité.
  2. *Inventaire de la révocation (Tableau 20.1)* : Démonstration limpide du déséquilibre entre les efforts consacrés à l'émission et l'abandon quasi total des mécanismes de révocation opérationnelle.
  3. *Agentic SOC* : L'analyse de la régression du principe de moindre privilège chez Microsoft (Défaut D11) constitue une découverte d'audit majeure.

### S23. Chapitre 21 : L'horloge post-quantique et crypto-agilité
- **Périmètre** : pp. 236-251 (NIST IR 8547, FIPS 203/204/205, Décret 14412, OMB M-26-15, CCCS ITSM.40.001, Inégalité de Mosca).
- **Analyse critique** :
  1. *Rigueur calendaire* : La distinction méthodique entre le statut *PROGRAMMÉ* (Décret 14412 / OMB M-26-15), *PROJETÉ* (NIST IR 8547 avec dépréciation 2030 et interdiction 2035) et *SPÉCULATIF* (fenêtres d'ordinateurs quantiques) est exemplaire.
  2. *Définition de la crypto-agilité* : La formulation en trois conditions (découplage, contrat versionné, procédure d'évolution) est conceptuellement féconde.
  3. *Lacune majeure sur l'impact réseau (Défaut D4)* : L'absence de quantification des tailles des signatures FIPS 204/205 et de leur impact sur la MTU Ethernet et les limites d'en-têtes HTTP affaiblit considérablement la valeur prescriptive du chapitre pour les architectes de systèmes multi-agents.
  4. *Défauts de forme* : Présence de la collision d'encadré flottant entre les pages 242 et 243 (Défaut D3) et de la dislocation du Tableau 21.4 en page 248 (Défaut D8).

### Amorce Chapitre 22 : Options d'orchestration (OO1-OO4)
- **Périmètre** : pp. 252-255 (Continuité Livre II -> Livre III, taxonomie de Rinderle-Ma & Mangler TU Munich).
- **Analyse critique** : L'introduction des quatre options d'orchestration (OO1 agnostique à OO4 consciente et encadrée) et des cinq propriétés d'évaluation pose des fondations claires pour le Livre III. La mise en garde contre la matrice simpliste 4x5 non démontrée par la source primaire témoigne d'une grande rigueur intellectuelle.

---

## 4. Revue bibliographique exhaustive et confrontation à l'état de l'art (2024-2026)

Le tableau suivant confronte l'ensemble des textes normatifs et publications académiques cités dans le Livre II à l'état réel des spécifications au 1er novembre 2026 :

```
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
| Référence / Norme                  | Date officielle| Statut documentaire réel  | Évaluation critique dans le Compendium                    |
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
| NIST FIPS 203 (ML-KEM)             | 13 août 2024   | Norme FIPS finale         | Cité exactement (§ 21.1) ; errata mineurs annoncés.       |
| NIST FIPS 204 (ML-DSA)             | 13 août 2024   | Norme FIPS finale         | Cité (§ 21.1) ; omission de l'impact taille signature.   |
| NIST FIPS 205 (SLH-DSA)            | 13 août 2024   | Norme FIPS finale         | Passé sous silence au § 21.1 ; taille signature critique. |
| NIST IR 8547 (PQC Transition)      | Nov. 2024      | Projet public initial     | Parfaitement qualifié en « PROJETÉ » (§ 21.1).            |
| Décret présidentiel US 14412       | 22 juin 2026   | Décret exécutif en vigueur| Correctement classé « PROGRAMMÉ » (§ 21.1).               |
| OMB M-26-15                        | 24 juin 2026   | Mémorandum exécutif       | Correctement articulé avec le Décret 14412.               |
| CCCS ITSM.40.001 (Canada)          | 23 juin 2025   | Guide d'orientation       | Correctement qualifié sans force contraignante financière.|
| RFC 8693 (OAuth Token Exchange)    | Janvier 2020   | Proposed Standard (IETF)  | Surinterprété au § 17.6 (erreur d'impossibilité formelle).|
| RFC 7009 (Token Revocation)        | Août 2013      | Proposed Standard (IETF)  | Bien analysé (§ 20.4, caractère facultatif du SHOULD).    |
| RFC 7662 (Token Introspection)     | Octobre 2015   | Proposed Standard (IETF)  | Ajouté le 30 juillet 2026 ; coquille ponctuation p. 227.  |
| A2A Protocol v1.0.0                | 12 mars 2026   | Spécification publiée     | Analyse rigoureuse des failles temporelles JWS.           |
| Model Context Protocol (MCP)       | 25 nov. 2025   | Spécification de facto    | Analyse exacte du fait négatif F-52 (zéro intégrité).    |
| Biscuit Token Specification        | 2022-2026      | Standard ouvert           | Faussement qualifié de démuni d'identité de maillon.      |
| AgentPoison (NeurIPS 2024)         | Décembre 2024  | Conférence révisée        | Parfaitement mobilisé au § 19.1 sur l'injection indirecte.|
| OWASP Top 10 Agentic Apps 2026     | Décembre 2025  | Référentiel de sécurité   | Bien contextualisé ; non-assimilation de métriques éditeur|
| MITRE ATLAS v2026.06 / v2026.09    | Juin/Sept 2026 | Base de connaissances     | Dépréciation du chemin historique bien relevée (§ 20.10). |
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
```

---

## 5. Protocole de vérification indépendante

Pour vérifier de façon indépendante l'exactitude des constats formulés dans ce rapport d'audit, exécuter les étapes suivantes sur le dépôt `EntrepriseAgentique` :

1. **Vérification de la collision typographique D3 (pp. 242-243)** :
   - Ouvrir les fichiers images `documents/scratch/document_pages/page-242.png` et `page-243.png`.
   - Constater en bas de la page 242 la terminaison abrupte `tri :` suivie de l'encadré en gras de 16 lignes, et le rattachement orphelin de `fait PROJETÉ` au sommet de la page 243.
2. **Vérification de la désarticulation du Tableau 16.3 (p. 188)** :
   - Ouvrir `documents/scratch/document_pages/page-188.png`.
   - Observer que la colonne « Tri » contient le texte descriptif mutilé et que la colonne « Ce sur quoi il s'appuie » est totalement vide.
3. **Vérification de la dislocation d'en-tête du Tableau 21.4 (p. 248)** :
   - Ouvrir `documents/scratch/document_pages/page-248.png`.
   - Vérifier la division inversée de la phrase relative à l'ITSM.40.001 entre les colonnes 2 et 3.
4. **Vérification formelle de la capabilité de Biscuit face au problème des deux sauts (D1)** :
   - Consulter la spécification formelle de Biscuit (RFC/biscuit-auth) et vérifier que l'ajout d'un bloc d'atténuation permet d'ajouter la contrainte :
     `check if actor("agent_C"), operation("read")`
     ce qui démontre mathématiquement la transitivité de l'opposabilité de chaque saut par signature asymétrique Ed25519, réfutant la prétendue impossibilité énoncée au § 17.6.
5. **Vérification des tailles FIPS 204 et impact MTU (D4)** :
   - Consulter la norme officielle NIST FIPS 204 (Table 1 et Table 2) :
     Vérifier que pour ML-DSA-44, la taille de la signature est de 2 420 octets, excédant à elle seule la MTU Ethernet de 1 500 octets.
