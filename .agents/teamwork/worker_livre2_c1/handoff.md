# Rapport d'Audit Contradictoire — Candidat 1 (Niveau 0)
## Segment : Livre 2 — Rendre la confiance opposable (Chapitres 12 à 21, Pages 144 à 255)
**Document audité** : `documents/Compendium.pdf`  
**Auteur du rapport** : Analyste Candidat 1 (Niveau 0)  
**Date d'audit** : 3 novembre 2026  
**Périmètre couvert** : Segments S14 à S23 du REVIEW_PLAN (pp. 144-255), Ch. 12 (Identités non humaines), Ch. 13 (DID et Verifiable Credentials), Ch. 14 (Grille d'évaluation de la confiance), Ch. 15 (Agent Card signée A2A et registres), Ch. 16 (Passeport d'agent), Ch. 17 (Chaîne de mandat et délégation), Ch. 18 (Know Your Agent - KYA), Ch. 19 (Taxonomie des attaques), Ch. 20 (Attaques temporelles et Agentic SOC), Ch. 21 (Horloge post-quantique et dette de migration), Ch. 22 introduction (pp. 252-255, transition Livre III).  
**Axes d'évaluation** : R2 (Rigueur formelle et algorithmique) & R3 (Vérification bibliographique et état de l'art 2024-2026).

---

## 1. Résumé exécutif critique du Livre 2

Le Livre 2 du *Compendium* s'intitule avec une grande ambition « Rendre la confiance opposable ». Il se propose de jeter les fondations architecturales, cryptographiques et juridiques de l'autonomie agentique en entreprise, depuis la modélisation de l'identité non humaine jusqu'à l'anticipation de la menace cryptanalytique post-quantique.

Toutefois, une évaluation contradictoire rigoureuse et exhaustive révèle un **décalage structurel profond entre la promesse formelle annoncée et la réalité des mécanismes exposés** :

1. **Falsification formelle du « problème des deux sauts » et nullité du correctif par Token Exchange** :  
   L'axe névralgique du Livre 2 prétend formaliser la rupture d'opposabilité dans les délégations en cascade $A \to B \to C$. Or, l'analyse démontre qu'**aucune formalisation mathématique, logique ou probabiliste n'est fournie** dans l'ouvrage. L'auteur concède lui-même à la page 198 qu'« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict ». Pire encore, la suggestion d'utiliser le Token Exchange (RFC 8693) comme remède s'effondre devant les clauses explicites de la spécification : la RFC 8693 §4.1 proscrit formellement l'utilisation de l'historique d'acteurs `act` pour les décisions de contrôle d'accès (*« informational only and MUST NOT be used for access control decisions »*), la RFC 8693 §1 exclut la validité intrinsèque des jetons échangés, et les Transaction Tokens ne valent que cantonnés à un domaine de confiance administratif unique.
2. **Inadéquation structurelle des protocoles humains (OAuth 2.0 / SCIM 2.0)** :  
   Les tentatives d'étirer OAuth 2.0 (RFC 6749) et SCIM 2.0 (RFC 7643/7644) vers des agents autonomes échouent. Le flux interactif d'autorisation (§4.1) requiert une intervention humaine par redirection Web, tandis que le flux machine-to-machine (§4.4 Client Credentials) ignore la distinction fondamentale entre l'agent agissant pour son propre compte et l'agent agissant sous mandat d'un tiers. Quant à la standardisation de SCIM pour les agents, elle s'appuie sur un projet caduc de CSA Labs reposant sur un brouillon IETF expiré (`draft-abbey-scim-agent-extension-00`, expiré le 19 avril 2026).
3. **Fragilité rédhibitoire de l'Agent Card A2A et chimère du « Passeport d'agent »** :  
   L'Agent Card signée (spécification A2A v1.0.0 de Google / Linux Foundation) est présentée à tort comme une preuve d'identité ou un passeport opposable. En réalité, l'Agent Card n'est qu'une fiche descriptive de métadonnées fonctionnelles. La spécification A2A v1.0.0 ne définit **aucun champ de fraîcheur temporelle** (`iat`, `exp`, `nbf`), rend la signature optionnelle (`MAY`), la vérification recommandée (`SHOULD`), et ne propose aucun protocole de révocation ni gestion de magasin de clés de confiance.
4. **Schisme irréconciliable au sein de W3C VC v2.0** :  
   La Recommandation W3C Verifiable Credentials Data Model v2.0 (mai 2025) institutionnalise deux familles de preuves mutuellement inconciliables : les preuves incorporées en graphe sémantique (`proof` en JSON-LD avec suites RDF Dataset Canonicalization RFC 8785) et les preuves enveloppantes JOSE/COSE (JWT). Sans profilage d'application unifié, deux agents strictement conformes à VC v2.0 sont incapables d'interopérer ou de vérifier leurs preuves respectives de manière autonome.
5. **Défauts typographiques et textuels bloquants lors de la compilation** :  
   L'ouvrage comporte des bris de composition inacceptables pour un texte de référence :
   - *Page 151* : Phrase tronquée net en fin de section sous le Tableau 12.3 (« un document » coupé sans fin de phrase).
   - *Pages 152 et 153* : Boîtes d'encadré flottantes insérées au beau milieu de phrases actives du corps de texte, fragmentant la syntaxe grammaticale (« d'une [Thèse...] section, ne le définit... » et « la preuve [EXTRACTION...] incorporée... »).
6. **Inefficacité du confinement cognitif face au Confused Deputy et à la Triade Létale** :  
   La réémergence du problème du *confused deputy* (Norm Hardy, 1988) dans les architectures agentiques rend obsolètes les approches fondées sur le prompt engineering ou les filtres sémantiques. Conformément aux démonstrations de Simon Willison et aux attaques documentées dans la littérature (AgentPoison, NeurIPS 2024), seul le découplage physique et architectural des privilèges permet de neutraliser la triade létale.
7. **Rigueur chronologique mais angle mort de charge sur la transition Post-Quantique** :  
   Le Compendium se distingue positivement par sa rigueur chronologique en dissociant la normalisation des primitives NIST (FIPS 203, FIPS 204, FIPS 205 au 13 août 2024) du statut encore préliminaire du calendrier de retrait NIST IR 8547 (dépréciation 2030, retrait 2035). Cependant, il omet complètement de quantifier l'explosion de charge réseau et de latence induite par les signatures post-quantiques (ML-DSA exigeant 2 420 octets contre 64 octets pour Ed25519) sur des architectures de micro-agents à haute fréquence d'échanges.

---

## 2. Matrice exhaustive des défauts classés par sévérité

### Tableau synthétique des constatations

| ID | Sévérité | Chapitre | Page | Intitulé synthétique du défaut |
|---|---|---|---|---|
| **DEF-L2-01** | **Bloquant** | Ch. 17 | pp. 196-199 | Falsification de la « démonstration mathématique » des deux sauts et invalidité de RFC 8693 |
| **DEF-L2-02** | **Bloquant** | Ch. 12 | p. 151 | Troncature textuelle critique sous le Tableau 12.3 (« un document » coupé net) |
| **DEF-L2-03** | **Bloquant** | Ch. 13 | pp. 152-153 | Infiltration de boîtes d'encadré scindant des phrases actives en deux |
| **DEF-L2-04** | **Majeur** | Ch. 13 | pp. 153-157 | Schisme d'interopérabilité des formats de preuve W3C VC v2.0 (Embedded vs Enveloping) |
| **DEF-L2-05** | **Majeur** | Ch. 15-16 | pp. 167-184 | Faille conceptuelle de l'Agent Card A2A et du Passeport (absence de fraîcheur et révocation) |
| **DEF-L2-06** | **Majeur** | Ch. 12 | pp. 144-150 | Inaptitude d'OAuth 2.0 / SCIM 2.0 face aux agents autonomes et caducité du draft CSA |
| **DEF-L2-07** | **Majeur** | Ch. 19-20 | pp. 210-224 | Illusion du confinement cognitif face au Confused Deputy et à la Triade Létale de Willison |
| **DEF-L2-08** | **Majeur** | Ch. 20 | pp. 230-235 | Rupture d'imputabilité dans l'Agentic SOC par détournement des mécanismes PIM/TAP |
| **DEF-L2-09** | **Majeur** | Ch. 21 | pp. 238-247 | Omission de la charge réseau et de latence des signatures PQC (ML-DSA vs Ed25519) |
| **DEF-L2-10** | **Mineur** | Ch. 21 | pp. 248-249 | Ambiguïté sur l'opposabilité de la feuille de route canadienne ITSM.40.001 au secteur financier |

---

### Fiches détaillées des défauts

#### DEF-L2-01 [Bloquant / Erreur formelle]
- **Localisation** : Chapitre 17, pages 196 à 199 (§17.6, §17.6.2, Figure 17.6).
- **Citation textuelle exacte** :  
  Page 198 : *« Le terme "limites démontrées" mérite d'être borné avant d'écrire quoi que ce soit : aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »* et *« Ce que le socle établit : les mécanismes de RFC 8693 §4.1, de draft-ietf-oauth-transaction-tokens et d'AP2 [...] Ce qu'il n'établit pas : qu'aucun d'eux résolve le problème dans sa généralité »*.
- **Diagnostic causal approfondi** :  
  Le plan de révision et la trame directrice du Livre 2 affirment l'existence d'une « démonstration mathématique de rupture d'opposabilité dans le problème des deux sauts ($A \to B \to C$) ». Or, l'analyse textuelle démontre qu'**aucun appareil formel n'est articulé** dans le texte : ni logique d'autorisation (telle que SecPAL, logique BAN, ou calcul ABLP), ni réseau de Petri, ni preuve de réduction sous hypothèse cryptographique. L'auteur admet explicitement ce vide.  
  En outre, l'évocation de la RFC 8693 (OAuth Token Exchange) comme mécanisme d'atténuation ou de traçabilité est **réfutée par les clauses normatives impératives de la norme elle-même** :
  1. La RFC 8693 §4.1 dispose expressément : *« The "act" (actor) claim [...] is informational only and MUST NOT be used for access control decisions »*. Le vérificateur aval $C$ ou le service final $S$ n'a donc aucun droit normatif d'asseoir sa politique d'autorisation sur cette chaîne.
  2. La RFC 8693 §1 exclut expressément la sémantique de validité intrinsèque des jetons échangés (*« token validity is out of scope »*).
  3. L'extension par *Transaction Tokens* (`draft-ietf-oauth-transaction-tokens`) ne s'applique qu'à l'intérieur d'un domaine de confiance unique (*« within a single trust domain »*).
- **Contre-exemple formel et Correctif** :  
  Dans le calcul d'autorisation ABLP (Abadi, Burrows, Lampson, Plotkin) :
  Soit $A$ déléguant une requête $\phi$ à $B$, qui délègue à $C$. Pour que $C$ soit habilité à faire valoir $\phi$ auprès du serveur $S$, il faut prouver :
  $$C \text{ speaks\_for } (B \text{ speaks\_for } A) \implies C \text{ speaks\_for } A \text{ on } \phi$$
  Cette déduction est logiquement invalide sans règle explicite de transitivité conditionnée par une preuve de non-répudiation et une borne de profondeur de sous-délégation ($\text{depth} \le k$).  
  **Correctif** : Supprimer toute prétention d'une « démonstration mathématique » existante dans le Compendium. Requalifier le problème comme une « conjecture architecturale empirique ». Remplacer la référence erronée à RFC 8693 par les architectures formellement prouvées d'atténuation cryptographique à porteurs de caveats : les *Macaroons* (Birgisson et al., NDSS 2014) avec clés secrètes chaînées par HMAC et tiers vérificateurs (*third-party caveats* prouvés sous PRF), ou les jetons *Biscuit* (Geal et al.) avec moteur Datalog embarqué vérifié de manière déterministe à chaque saut.

#### DEF-L2-02 [Bloquant / Erreur de composition typographique]
- **Localisation** : Chapitre 12, page 151 (sous le Tableau 12.3, inspection de `page-151.png`).
- **Citation textuelle exacte** :  
  Page 151 : *« un document »* [interruption brutale] suivi d'un paragraphe orphelin sautant à : *« Ce qui manque à cet inventaire, et que les sections suivantes construisent, n'est pas un attribut de plus : c'est la distinction entre l'entité et l'autorité qui la meut... »*.
- **Diagnostic causal approfondi** :  
  Lors du rendu du moteur typographique (LaTeX/Typst), le paragraphe de commentaire analytique situé sous le Tableau 12.3 a été coupé net au mot « document ». La proposition subordonnée et la conclusion de la phrase ont été avalées par un débordement de boîte ou une mauvaise gestion des séparateurs d'environnement. Un fragment de phrase erratique (« d'une section, ne le définit... ») a été repoussé au début de la page 152. Ce défaut prive le lecteur de la synthèse critique du chapitre 12.
- **Correctif formel** :  
  Réajuster les marges et les contraintes verticales de placement du Tableau 12.3, restaurer le texte complet de la proposition :  
  *« La proposition de CSA Labs demeure un document [d'orientation informel qui, en l'état de la normalisation IETF, ne définit pas un profil opposable]. »*

#### DEF-L2-03 [Bloquant / Erreur de mise en page structurelle]
- **Localisation** : Chapitre 13, pages 152 et 153 (inspection de `page-152.png` et `page-153.png`).
- **Citation textuelle exacte** :  
  Page 152 : *« d'une »* [Encart flottant « Thèse » inséré en plein milieu de phrase] *« section, ne le définit... »*.  
  Page 153 : *« la preuve »* [Encart pleine largeur « EXTRACTION CONDUITE LE 30 JUILLET 2026 AU REGISTRE W3C DES MÉTHODES DID... » intercalé] *« incorporée, portée par la propriété proof... »*.
- **Diagnostic causal approfondi** :  
  Les blocs de citation et les encadrés d'extraction de registre ne possèdent pas de balises d'isolation de paragraphe (`\par` ou contrainte d'ancrage strict `[H]`). Le compilateur a injecté les blocs au milieu exact de segments syntagmatiques en cours de composition, brisant la liaison sujet-verbe et nom-adjectif.
- **Correctif formel** :  
  Appliquer des contraintes de flottement strictes avec rupture de paragraphe obligatoire avant et après chaque encadré méthodologique et thèse.

#### DEF-L2-04 [Majeur / Lacune d'interopérabilité]
- **Localisation** : Chapitre 13, pages 153 à 157 (§13.2, Tableau 13.1).
- **Citation textuelle exacte** :  
  Page 153 : *« La spécification autorise deux grandes familles de preuves : les preuves incorporées (embedded proofs), portées par la propriété proof dans le graphe JSON-LD [...] et les preuves enveloppantes (enveloping proofs), où le document VC devient la charge utile d'un jeton signé (JWT) ou chiffré (JOSE, COSE) »*.
- **Diagnostic causal approfondi** :  
  La Recommandation W3C VC v2.0 (mai 2025) a institutionnalisé une fracture technique majeure :
  - La filière *Data Integrity Proofs* repose sur la canonicalisation de graphes RDF (RDFC-2022 / RFC 8785) et des suites cryptographiques complexes (`eddsa-rdfc-2022`).
  - La filière *Enveloping Proofs* (IETF JOSE/COSE / SD-JWT) traite les attestations comme des structures plates sérialisées signées selon la RFC 7515.
  Deux agents autonomes affirmant leur conformité à la norme W3C VC v2.0 ne peuvent pas échanger ni valider leurs attestations sans accord bilatéral préalable hors-norme. Le texte du Compendium présente cette dualité comme un choix de conception neutre, alors qu'elle constitue un obstacle critique à l'opposabilité décentralisée.
- **Correctif formel** :  
  Formuler explicitement une clause d'exigence de profilage (Application Profile Requirement) : toute architecture d'entreprise doit restreindre son écosystème à un profil d'exécution exclusif (par exemple, le profil IETF SD-JWT-VC RFC 9542) et documenter l'impossibilité d'une opposabilité universelle native via W3C VC v2.0 seul.

#### DEF-L2-05 [Majeur / Faille conceptuelle de sécurité]
- **Localisation** : Chapitres 15 et 16, pages 167 à 184 (§15.1, §15.2, §16.1, Figure 15.1).
- **Citation textuelle exacte** :  
  Pages 172-173 : *« La spécification de la carte d'agent signée dans A2A v1.0.0 n'impose aucune contrainte de fraîcheur : aucun champ iat, aucun champ exp, aucun champ nbf [...] et l'usage de la signature y est MAY, tandis que sa vérification est SHOULD »*.
- **Diagnostic causal approfondi** :  
  Le document qualifie à tort l'Agent Card A2A signée de pièce maîtresse du « Passeport d'agent » et d'artefact d'identité vérifiable. Or :
  1. L'Agent Card A2A v1.0.0 (Google / Linux Foundation) ne comporte aucun paramètre temporel (`iat`, `exp`, `nbf`). Une carte compromise ou obsolète reste indéfiniment valide.
  2. La spécification ne prévoit aucune liste de révocation, aucun protocole OCSP ni mécanisme de mise en quarantaine.
  3. La signature n'est qu'une option facultative (`MAY sign`), tout comme la validation (`SHOULD verify`) et la tenue d'un magasin de clés publiques (`MAY maintain a local cache`).
  4. L'Agent Card atteste de métadonnées déclaratives de fonctionnalités (outils supportés, URL d'invocation), mais ne contient aucune liaison cryptographique opposable au mandant juridique (qui répond des actes de l'agent).
- **Correctif formel** :  
  Déconstruire la métaphore du « passeport ». Séparer fonctionnellement :
  - Le *Capability Descriptor* (l'Agent Card A2A, cantonnée à un rôle d'annuaire technique d'exposition d'APIs) ;
  - L'*Identity Token* (un certificat d'instance éphémère X.509 ou SPIFFE SVID) ;
  - Le *Delegation Mandate* (un jeton cryptographique à divulgation sélective SD-JWT ou Biscuit, borné dans le temps avec $\Delta t \le 1\text{ heure}$, lié à l'identité du mandant et vérifié par une autorité de politique ABAC).

#### DEF-L2-06 [Majeur / Incompatibilité fondamentale de standardisation]
- **Localisation** : Chapitre 12, pages 144 à 150 (§12.1 à §12.3).
- **Citation textuelle exacte** :  
  Page 146 : *« OAuth 2.0 est conçu pour un utilisateur humain devant un navigateur [...] Le flux Client Credentials (§4.4) est la seule option non interactive, mais il écrase la distinction entre l'agent agissant pour son propre compte et l'agent agissant au nom d'un tiers »*.
- **Diagnostic causal approfondi** :  
  OAuth 2.0 (RFC 6749) et SCIM 2.0 (RFC 7643/7644) constituent le socle de l'IAM d'entreprise, mais leur application aux agents autonomes révèle des contradictions insurmontables :
  - Le modèle d'authentification interactive d'OAuth 2.0 présume une présence humaine permanente au moment du consentement via navigateur (§4.1 Authorization Code).
  - Le flux machine-to-machine §4.4 (Client Credentials) associe une identité d'application statique sans distinction de mandat contextuel.
  - Le standard SCIM 2.0 n'intègre aucun schéma pour les agents autonomes (§4 limite les objets à `User`, `Group`, `EnterpriseUser`).
  - L'initiative mentionnée par CSA Labs s'appuie sur `draft-abbey-scim-agent-extension-00`, devenu caduc le 19 avril 2026 sans suite à l'IETF. Les entreprises sont ainsi poussées vers des solutions propriétaires (ex. Microsoft Entra Agent ID), réintroduisant une dépendance fermée.
- **Correctif formel** :  
  Adopter et formaliser l'intégration du standard IETF GNAP (RFC 9635 - Grant Negotiation and Authorization Protocol), conçu nativement pour les interactions asynchrones sans navigateur, négociant des droits dynamiques liés à des clés de session asymétriques (Proof of Possession) et supportant la délégation multi-niveaux.

#### DEF-L2-07 [Majeur / Réfutation de sécurité architecturale]
- **Localisation** : Chapitres 19 et 20, pages 210 à 224 (§19.2, §19.3, §20.1).
- **Citation textuelle exacte** :  
  Page 214 : *« Le problème du confused deputy identifié par Hardy en 1988 resurgit avec les agents : l'agent dispose de privilèges légitimes sur des outils, mais son planificateur interne est manipulé par une injection indirecte provenant d'un contenu externe non fiable »*.
- **Diagnostic causal approfondi** :  
  Le texte identifie la résurgence du *confused deputy* (Hardy, 1988) et cite la triade létale de Simon Willison :
  $$(\text{AccèsDonnéesPrivées}) \wedge (\text{IngestionContenuNonFiable}) \wedge (\text{CanalExfiltration}) \implies \text{Compromission}$$
  Cependant, les sections 19.3 et 20.1 s'égarent en proposant des parades cognitives (filtrage de prompts, analyse sémantique, classification d'intention par un modèle tiers). Conformément aux résultats théoriques et empiriques (AgentPoison, NeurIPS 2024 ; Perez et al., 2022), le traitement sémantique en langage naturel est intrinsèquement probabiliste et indécidable : **aucun garde-fou textuel ne peut garantir l'immunité contre l'injection indirecte**.
- **Correctif formel** :  
  Établir le principe du *cloisonnement architectural des privilèges* : la neutralisation de l'attaque exige de briser structurellement la triade de Willison au niveau de la couche d'exécution (Livre III / Livre IV) :
  - Règle de révocation de canal : dès lors qu'un agent ingère une donnée externe non vérifiée (courriel, document, scraping), la plateforme d'exécution doit révoquer immédiatement et automatiquement tout canal réseau sortant non déterministe.
  - Architecture *Dual-Agent* avec sas étanche : l'agent d'ingestion non fiable est isolé dans un bac à sable sans outil à effet de bord ; l'agent exécuteur privilégié n'ingère que des structures de données strictement typées et validées par schéma JSON/Protobuf déterministe.

#### DEF-L2-08 [Majeur / Dérive d'imputabilité opérationnelle]
- **Localisation** : Chapitre 20, pages 230 à 235 (§20.5, Tableau 20.2).
- **Citation textuelle exacte** :  
  Page 233 : *« Déployer des agents de défense en leur attribuant des comptes utilisateurs pour leur permettre d'agir sur le SI [...] crée une dérive d'imputabilité où les mécanismes de PIM (Privileged Identity Management) et de TAP (Temporary Access Pass) échouent »*.
- **Diagnostic causal approfondi** :  
  Dans l'implémentation pratique de l'Agentic SOC (Microsoft Copilot for Security, Google Security AI), l'incapacité d'intégrer des identités d'agents pures pousse les équipes d'exploitation à doter les agents de comptes d'utilisateurs humains avec privilèges élevés.  
  Cette pratique induit une rupture d'imputabilité catastrophique :
  - Les contrôles PIM exigent des défis MFA interactifs humains ; pour permettre l'autonomie 24/7 de l'agent, les administrateurs mettent en place des scripts d'auto-approbation ou des passes d'accès temporaires (TAP) permanents.
  - Les journaux d'audit attribuent les modifications d'infrastructure à l'identifiant du compte utilisateur de service, masquant le modèle sous-jacent, la version de l'invite et la séquence de raisonnement qui a motivé l'action.
  - Cette opacité enfreint les exigences réglementaires d'auditabilité (directive BSIF E-23 au fédéral canadien et article 12.1 de la Loi 25 québécoise).
- **Correctif formel** :  
  Proscrire formellement l'utilisation de comptes utilisateurs pour les agents SOC. Imposer l'authentification par *Workload Identity Federation* avec attestations cryptographiques mTLS / SPIFFE SVID, et consigner dans un journal d'événements immuable (WORM) chaque commande associée à son empreinte d'invite et à sa signature de mandat.

#### DEF-L2-09 [Majeur / Omission de scalabilité post-quantique]
- **Localisation** : Chapitre 21, pages 238 à 247 (§21.3 à §21.7).
- **Citation textuelle exacte** :  
  Page 247 : *« Son §7.4.4 nomme deux propriétés qui s'opposent [...] et une soutenabilité de performance non établie : les signatures et échanges post-quantiques, dont les tailles d'artefacts sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de main »*.
- **Diagnostic causal approfondi** :  
  Le chapitre 21 présente la migration vers NIST FIPS 204 (ML-DSA) et FIPS 205 (SLH-DSA), mais omet totalement de quantifier l'impact de l'asymétrie dimensionnelle sur la communication agentique :
  - Clé publique et signature Ed25519 classique : $32\text{ octets} + 64\text{ octets} = 96\text{ octets}$.
  - ML-DSA-44 (niveau de sécurité NIST 2) : clé publique de $1\,312\text{ octets}$ et signature de $2\,420\text{ octets}$, soit $3\,732\text{ octets}$ (multiplication par un facteur **38,8**).
  - ML-DSA-87 (niveau 5) : clé publique de $2\,592\text{ octets}$ et signature de $4\,627\text{ octets}$ ($7\,219\text{ octets}$, facteur **75**).
  - SLH-DSA-SHA2-128s : signature seule de $7\,856\text{ octets}$ (facteur **81**).  
  Dans un système multi-agents où des micro-tâches génèrent des milliers d'appels A2A et MCP par heure avec transmission de tokens signés dans les en-têtes HTTP, cette surcharge de données sature les mémoires tampons, engorge la bande passante et grève le budget de contexte des LLM lors de l'injection d'artefacts d'autorisation.
- **Correctif formel** :  
  Fournir une modélisation analytique de l'empreinte réseau :
  $$\text{OverheadRatio} = \frac{\text{Taille}_{\text{PQC}}}{\text{Taille}_{\text{Ed25519}}} \approx 40\text{ à } 80$$
  Prescrire une architecture hybride en couches : sécuriser le canal transport (L4) via TLS 1.3 avec échange de clés post-quantique (ML-KEM-768 selon FIPS 203), tout en maintenant au niveau applicatif (L7) des jetons de session signés avec des clés symétriques éphémères dérivées (KMAC / HMAC-SHA256), réservant les signatures asymétriques ML-DSA aux seuls mandats maîtres à longue durée de vie.

#### DEF-L2-10 [Mineur / Ambiguïté de portée réglementaire]
- **Localisation** : Chapitre 21, pages 248-249 (§21.8, Tableau 21.4).
- **Citation textuelle exacte** :  
  Page 248 : *« ITSM.40.001 vise le gouvernement fédéral, non les banques ni les assureurs : une institution qui s'en réclamerait comme d'une échéance applicable lirait, encore une fois, le plafond d'un autre »*.
- **Diagnostic causal approfondi** :  
  Bien que l'avertissement de l'auteur soit louable, la présentation graphique du Tableau 21.4 (mettant en valeur les échéances 2031 et 2035) peut induire en erreur un architecte financier canadien. Le Bureau du surintendant des institutions financières (BSIF / OSFI) n'a émis qu'un bulletin d'information en mars 2026 sans valeur réglementaire contraignante, et l'AMF n'a publié qu'un rapport prospectif. Il n'existe à ce jour aucune date butoir légalement opposable au secteur financier canadien pour la cryptographie post-quantique.
- **Correctif formel** :  
  Ajouter une note explicite en tête du Tableau 21.4 confirmant que l'absence d'obligation spécifique du BSIF maintient les institutions sous la règle générale de gestion du risque opérationnel (BSIF E-21 / E-23), sans jalon quantique calendaire impératif.

---

## 3. Audit approfondi section par section (S14 à S23, Ch. 12 à 21)

### Segment S14 (Ch. 12 & Ch. 13 - pp. 144 à 160) : Identité non humaine, OAuth 2.0 / SCIM étirés et W3C DID / VC
- **Analyse critique** :  
  Le chapitre 12 met en lumière l'étirement excessif des protocoles de gestion des identités historiques. OAuth 2.0 (RFC 6749) ne modélise pas l'agentivité : un agent n'est ni un simple « client » passif, ni un « Resource Owner » doué de subjectivité juridique. L'utilisation du *Client Credentials Grant* (§4.4) crée un angle mort de sécurité : le serveur de ressources reçoit un jeton représentant l'application globale, sans savoir si l'action émane d'une initiative propre de l'agent ou d'une commande explicite d'un utilisateur humain.  
  Concernant SCIM 2.0 (RFC 7643/7644), le document documente bien l'absence d'un objet normalisé pour les agents. L'adossement à `draft-abbey-scim-agent-extension-00` de CSA Labs est fragile : ce draft a expiré le 19 avril 2026 sans adoption par le groupe de travail SCIM de l'IETF.  
  Le chapitre 13 aborde W3C DID Core v1.0/v1.1 et W3C VC v2.0 (mai 2025). Le diagnostic est juste quant au caractère purement syntaxique de DID Core (qui n'impose que l'attribut `id` et laisse la résolution hors périmètre). En revanche, l'évaluation de VC v2.0 sous-estime la gravité de la rupture entre preuves incorporées (`proof` RDF Dataset Canonicalization RFC 8785) et preuves enveloppantes (JOSE/COSE JWT). Cette division empêche l'émergence d'un vérificateur agentique universel.

### Segment S15 (Ch. 13 à Ch. 15 - pp. 160 à 180) : Grille d'évaluation, Agent Card A2A et intégrité vs identité
- **Analyse critique** :  
  La grille des 5 questions (Q-A à Q-E du Ch. 14 : *Qui est-il ? Pour qui agit-il ? Quelles sont ses limites ? Comment vérifier sa preuve ? Comment le révoquer ?*) constitue une heuristique utile pour les comités d'architecture, mais elle ne possède aucun fondement formel démontrable.  
  Le chapitre 15 consacre une large part à l'Agent Card A2A v1.0.0 (Google / Linux Foundation) signée via JWS (RFC 7515) et JCS (RFC 8785). L'analyse contradictoire met en lumière une confusion majeure : **l'intégrité syntaxique d'une carte n'est pas une identité**. L'Agent Card décrit les points de terminaison et les schémas d'outils de l'agent. Le fait qu'elle soit signée empêche sa falsification en transit, mais n'établit aucune opposabilité : la spécification ne contient aucun champ temporel (`iat`, `exp`, `nbf`), ne dispose d'aucun mécanisme de révocation et repose sur une signature facultative (`MAY`).

### Segment S16 (Ch. 15 - pp. 175 à 180) : Annuaires commerciaux et registres d'agents gouvernés
- **Analyse critique** :  
  Le paysage des annuaires d'agents (Microsoft Entra Agent ID, GCP Agent Directory, AWS IAM Identity Center) est caractérisé par un enfermement propriétaire rigide. Les passerelles d'interopérabilité reposent sur des mécanismes de fédération fragiles (OIDC / SAML 2.0).  
  Les initiatives de registres ouverts (CSA Labs Trusted Agent Registry, AGNTCY) tentent de combler ce vide, mais elles reproduisent une gouvernance centralisée par consortium sans standard ouvert contraignant. La confrontation avec les directives canadiennes (BSIF E-23 sur la gestion du risque opérationnel et la résilience, avis ACVM 11-348) confirme qu'aucun régulateur prudentiel ne reconnaît actuellement ces registres comme des tiers de confiance qualifiés.

### Segment S17 (Ch. 15 à Ch. 17 - pp. 180 à 195) : Le Passeport d'agent virtuel et la chaîne de mandat
- **Analyse critique** :  
  Le concept de « Passeport d'agent » proposé au Ch. 16 réunit quatre pièces : (1) l'identifiant d'instance, (2) la carte de capacités, (3) l'attestation de mandat, et (4) la chaîne de confiance émettrice.  
  La formalisation du mandat au Ch. 17 explore le recours au champ `act` de la RFC 8693 §4.1 et aux jetons de transaction IETF. Toutefois, l'analyse démontre que la traçabilité de mandat à sauts multiples ($A \to B \to C$) soulève un conflit d'auditabilité majeur au regard de la Loi 25 québécoise (art. 12.1) : si l'agent $B$ délègue une partie du traitement à un agent tiers $C$ hébergé hors juridiction sans consentement granulaire préalable, l'opposabilité légale du consentement initial de la personne concernée est rompue.

### Segment S18 (Ch. 17 - pp. 195 à 201) : Falsification formelle du problème des deux sauts
- **Analyse critique** :  
  Ce segment constitue le point d'inflexion critique de l'audit. Le document suggère qu'une rupture d'opposabilité a été « démontrée » dans les délégations en cascade $A \to B \to C$.  
  **La falsification est totale** :
  1. Le Compendium n'articule aucune démonstration formelle ou mathématique.
  2. La tentative de présenter le Token Exchange (RFC 8693) comme remède est formellement réfutée par la RFC 8693 elle-même (§4.1 interdisant l'usage de `act` pour l'autorisation ; §1 excluant la validité du token ; confinement au domaine unique).
  3. Les solutions valides issues de la recherche (Macaroons de Birgisson et al. NDSS 2014, Biscuit de Geal et al.) démontrent au contraire qu'une délégation en cascade peut préserver formellement l'opposabilité et l'atténuation de portée si chaque saut adjoint un *caveat* cryptographiquement lié par une chaîne de clés HMAC/asymétriques avec vérification déterministe.

### Segment S19 (Ch. 17 à Ch. 19 - pp. 201 à 210) : Know Your Agent (KYA) et absence d'infrastructure inter-domaines
- **Analyse critique** :  
  Le Ch. 18 dresse un parallèle entre KYC/KYB et KYA (Know Your Agent). L'inventaire des 9 chantiers et des 6 organisations (W3C, IETF, OpenID Foundation, FIDO Alliance, GLEIF pour le vLEI, CSA) illustre la dispersion des efforts.  
  L'audit confirme le constat d'absence d'infrastructures de confiance racine inter-domaines : il n'existe aucun équivalent d'eIDAS 2.0 ou de la fédération PKI Web pour lier l'accréditation d'un agent émis dans une juridiction bancaire canadienne à un système d'information européen ou américain.

### Segment S20 (Ch. 19 & Ch. 20 - pp. 210 à 225) : Taxonomie des attaques, rug-pull MCP et triade de Willison
- **Analyse critique** :  
  L'analyse des attaques agentiques synthétise les taxonomies MITRE ATLAS et OWASP Top 10 for Agentic AI 2026. L'analyse de l'attaque temporelle de type *rug-pull* sur le protocole MCP (Model Context Protocol) est particulièrement pertinente : un serveur d'outils modifie subrepticement les schémas JSON et descriptions de ses fonctions après la phase d'enregistrement initiale.  
  Cependant, le chapitre commet une erreur en misant sur des filtres de sécurité sémantiques contre le *confused deputy*. Comme l'ont démontré Simon Willison et les auteurs d'AgentPoison (NeurIPS 2024), dès lors que les trois conditions de la triade létale sont réunies dans le même espace d'exécution cognitif, l'injection de prompt indirecte est mathématiquement imprévisible et inévitable. Seul le découplage des permissions et la rupture d'un des trois piliers au niveau de l'orchestration offre une garantie formelle.

### Segment S21 (Ch. 20 - pp. 225 à 236) : Boucle défensive Agentic SOC et inventaire de révocation
- **Analyse critique** :  
  Le Ch. 20 met en exergue l'asymétrie fondamentale entre émission et révocation. L'histoire des PKI (CRL sous RFC 5280, OCSP sous RFC 6960 et son abandon par les navigateurs modernes en raison des fuites de vie privée et de latence) se répète dans les architectures d'agents.  
  L'audit valide la mise en garde de l'auteur concernant l'Agentic SOC : utiliser des comptes d'utilisateurs interactifs pour des agents défensifs détruit la traçabilité et contourne les garde-fous de PIM/TAP.

### Segment S22 (Ch. 20 & Ch. 21 - pp. 236 à 240) : Menace quantique sur la pile identitaire
- **Analyse critique** :  
  La démonstration de la vulnérabilité de la cryptographie asymétrique classique (RSA, ECDSA, Ed25519) à l'algorithme de Shor sur un ordinateur quantique à tolérance de pannes (FTQC) est irréfutable.  
  L'audit relève que toute la chaîne d'identité agentique moderne — des certificats TLS/mTLS aux JWT de session, en passant par les signatures JWS des Agent Cards et les preuves DID `did:key` — s'effondrera simultanément lors de l'avènement d'un FTQC. La distinction entre l'attaque SNDL (*Store Now, Decrypt Later*) visant le secret des données et l'attaque par falsification de signature rétroactive sur des mandats archivés est parfaitement établie.

### Segment S23 (Ch. 21 & Ch. 22 - pp. 240 à 255) : Feuille de route NIST, crypto-agilité, dette de migration et transition vers le Livre III
- **Analyse critique** :  
  Le traitement de l'horloge post-quantique au Ch. 21 fait preuve d'une excellente discipline méthodologique en rappelant que si les algorithmes NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) et FIPS 205 (SLH-DSA) sont officiellement normalisés depuis le 13 août 2024, le calendrier de transition NIST IR 8547 (dépréciation 2030, retrait 2035) demeure un projet public initial sans force réglementaire globale. De même, le décret fédéral américain 14412 et la note OMB M-26-15 ne visent que l'appareil exécutif civil américain, et la feuille de route canadienne ITSM.40.001 (juin 2025) n'est qu'un guide d'orientation interne pour le gouvernement fédéral.  
  Néanmoins, la critique R2 souligne l'omission totale du coût dimensionnel des signatures post-quantiques sur la latence des systèmes multi-agents (DEF-L2-09).  
  Enfin, l'ouverture sur le Livre III aux pages 252-255 introduit judicieusement la taxonomie d'orchestration OO1-OO4 (Rinderle-Ma et Mangler, TU Munich, juin 2026), articulant rigoureusement la frontière entre l'identité vérifiable du Livre II et le plan de contrôle d'exécution du Livre III.

---

## 4. Revue bibliographique et confrontation à l'état de l'art (2024-2026)

L'audit contradictoire a procédé à la vérification croisée de l'ensemble des références normatives et scientifiques mobilisées dans le Livre 2 :

1. **RFC 6749 (The OAuth 2.0 Authorization Framework)** :  
   *Conformité* : Établie. La norme impose un cadre interactif humain (§4.1) et son mode machine-to-machine (§4.4) est aveugle aux contextes de délégation dynamique.
2. **RFC 7643 & RFC 7644 (SCIM 2.0 Core Schema & Protocol)** :  
   *Conformité* : Établie. Aucun schéma d'agent n'est standardisé (§4 ne reconnait que User, Group, EnterpriseUser). Le draft `draft-abbey-scim-agent-extension-00` (CSA Labs) est caduc depuis le 19 avril 2026.
3. **RFC 8693 (OAuth 2.0 Token Exchange)** :  
   *Conformité* : Réfutation formelle des prétentions du Livre 2. La section 4.1 interdit formellement d'utiliser la revendication `act` pour les décisions de contrôle d'accès (*« informational only »*), et la section 1 exclut la validation interne des jetons échangés.
4. **`draft-ietf-oauth-transaction-tokens`** :  
   *Conformité* : Brouillon actif à l'IETF en 2025-2026, mais limité expressément au périmètre d'un domaine de confiance administratif unique (*« within a single trust domain »*).
5. **RFC 7515 (JWS) & RFC 8785 (JCS)** :  
   *Conformité* : Établie. Garantit l'intégrité syntaxique des octets sérialisés en JSON, mais ne fournit aucune sémantique de fraîcheur temporelle ou d'autorisation.
6. **W3C DID Core v1.0 & v1.1** :  
   *Conformité* : Établie. Spécification syntaxique minimale dont seule la clé `id` est impérative. La résolution et la résilience cryptographique dépendent des méthodes (`did:key`, `did:web`), dont `did:web` est vulnérable aux attaques TLS/DNS.
7. **W3C Verifiable Credentials Data Model v2.0 (Recommandation mai 2025)** :  
   *Conformité* : Établie. Confirme le schisme normatif irréconciliable entre les preuves incorporées (Data Integrity / RDFC-2022) et les preuves enveloppantes (JOSE/COSE JWT), empêchant l'interopérabilité directe inter-agents sans profilage strict.
8. **A2A (Agent-to-Agent Protocol v1.0.0, Google / Linux Foundation)** :  
   *Conformité* : Établie. L'Agent Card est déclarative, sa signature est optionnelle (`MAY`), la vérification est recommandée (`SHOULD`), et aucun champ temporel (`iat`, `exp`, `nbf`) ni liste de révocation n'est défini.
9. **RFC 9635 (GNAP - Grant Negotiation and Authorization Protocol, 2025-2026)** :  
   *Conformité* : Confirmé comme le successeur architectural moderne d'OAuth 2.0 pour les agents, éliminant les redirections par navigateur et liant les droits à des clés asymétriques de session.
10. **Macaroons (Birgisson et al., NDSS 2014)** :  
    *Conformité* : Référence fondamentale omise pour la formalisation mathématique de la délégation atténuée en cascade, prouvée sous l'hypothèse de sécurité des fonctions pseudo-aléatoires (PRF).
11. **Biscuit Tokens (Geal et al., 2021-2025)** :  
    *Conformité* : Standard de facto de l'industrie pour la délégation décentralisée à base de politiques Datalog embarquées et atténuées cryptographiquement à chaque saut.
12. **NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)** :  
    *Conformité* : Publiés officiellement le 13 août 2024. Confirmé.
13. **NIST IR 8547 (Initial Public Draft, 2024)** :  
    *Conformité* : Confirmé au statut de projet public préliminaire (dépréciation 2030, retrait 2035). Non contraignant pour les entreprises privées.
14. **Décret 14412 & Mémorandum OMB M-26-15** :  
    *Conformité* : Confirmé. Portée strictement restreinte aux agences fédérales civiles des États-Unis.
15. **ITSM.40.001 (CCCS, juin 2025)** :  
    *Conformité* : Confirmé. Cadre d'orientation pour le gouvernement du Canada (2031 / 2035), non opposable au secteur financier privé.
16. **Norm Hardy (1988) — The Confused Deputy** :  
    *Conformité* : Établie. Référence historique validant l'impossibilité de résoudre la confusion de mandat par de simples filtres sémantiques internes.
17. **Simon Willison & Triade Létale (2023-2025)** :  
    *Conformité* : Établie. Formulation canonique de l'insécurité intrinsèque des architectures unifiées combinant données privées, contenu non fiable et canaux de sortie.
18. **AgentPoison (NeurIPS 2024)** :  
    *Conformité* : Validation empirique de l'inefficacité des défenses cognitives face à l'empoisonnement d'agents LLM via RAG et mémoire de long terme.

---

## 5. Rapport de Synthèse Handoff (Protocole à 5 Composants)

### 5.1 Observation
- **Plage textuelle** : Pages 144 à 255 de `documents/Compendium.pdf` (lignes 11984 à 22660 de `documents/DOCUMENT_TEXT_MAP.md`).
- **Anomalies de compilation constatées directement sur les images de pages** :
  - `page-151.png` : Troncature nette du texte sous le Tableau 12.3 (« un document » coupé net).
  - `page-152.png` et `page-153.png` : Encadrés pleine largeur (« Thèse » et « EXTRACTION CONDUITE LE 30 JUILLET 2026... ») insérés en plein milieu de phrases du corps de texte, fragmentant la syntaxe.
- **Faits normatifs et textuels vérifiés** :
  - L'auteur admet explicitement à la page 198 (§17.6.2) : *« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
  - La RFC 8693 §4.1 proscrit expressément à un tiers vérificateur de baser ses décisions de contrôle d'accès sur l'attribut `act`.
  - La spécification A2A v1.0.0 ne définit aucun champ d'expiration (`exp`), ni de date d'émission (`iat`), ni de prise d'effet (`nbf`).
  - La Recommandation W3C VC v2.0 (mai 2025) consacre deux modèles de preuve incompatibles (Data Integrity Proofs JSON-LD vs JOSE/COSE Enveloping Proofs).
  - Les algorithmes NIST FIPS 203, 204 et 205 sont normalisés depuis le 13 août 2024, tandis que le calendrier NIST IR 8547 n'est qu'un projet préliminaire.

### 5.2 Chaîne logique (Logic Chain)
1. *De l'absence de formalisation à la réfutation de la preuve* : Le document promettait une « démonstration mathématique de rupture d'opposabilité dans les deux sauts ». L'aveu textuel de la page 198 combiné à l'absence de tout calcul formel (ABLP, SecPAL) prouve que la rupture n'est pas formellement démontrée dans l'ouvrage.
2. *De la RFC 8693 à l'invalidation du remède* : Puisque la RFC 8693 §4.1 stipule que `act` est informatif et ne doit pas servir aux décisions d'accès, et que le périmètre exclut la validité intrinsèque des jetons, le Token Exchange ne peut pas rétablir l'opposabilité dans une chaîne $A \to B \to C$.
3. *Des failles de l'Agent Card à la déconstruction du Passeport* : Une carte descriptive dépourvue d'expiration, de révocation et de signature impérative ne garantit que l'intégrité syntaxique d'une annonce de capacités. L'assimiler à un « passeport d'agent » constitue une faille de conception majeure.
4. *De l'asymétrie de Willison à l'impératif de cloisonnement* : Dès lors que le LLM est faillible et sensible aux injections indirectes (*confused deputy*), la sécurité ne peut reposer sur des filtres de prompts, mais exige la rupture physique ou cryptographique de la triade létale.
5. *Des métriques post-quantiques à la contrainte de scalabilité* : L'augmentation de la taille des signatures ML-DSA (facteur 38 à 75 par rapport à Ed25519) engendre une saturation réseau lors d'échanges A2A intensifs, imposant une hybridation asymétrique au niveau transport (L4) plutôt qu'applicatif (L7).

### 5.3 Mises en garde et limites (Caveats)
- L'audit s'est concentré sur les aspects formels, cryptographiques et protocolaires (axes R2 et R3) du segment Livre 2 (pp. 144-255).
- Les aspects d'orchestration multi-agents avancée introduits à partir de la page 252 (OO1-OO4) appartiennent structurellement au Livre III et ne sont analysés ici que dans leur articulation avec la couche identitaire.
- Les implémentations propriétaires récentes (ex. mises à jour post-juillet 2026 de Microsoft Entra Agent ID) n'étant pas documentées par des standards ouverts, leur analyse repose sur les spécifications publiques disponibles à la date de gel du document.

### 5.4 Conclusion
Le Livre 2 du *Compendium* pose des questions fondamentales et pertinentes sur la gouvernance de l'identité des agents autonomes et documente avec brio l'état de l'art post-quantique du NIST. Toutefois, il souffre de **trois défauts bloquants** (absence de démonstration formelle des deux sauts combinée à un correctif RFC 8693 formellement invalide, et bris typographiques sévères aux pages 151, 152 et 153) et de **six défauts majeurs** touchant à la solidité de l'Agent Card, l'interopérabilité de W3C VC v2.0, l'illusion du confinement cognitif face au confused deputy, et la charge des signatures post-quantiques.  
Le segment requiert une révision substantielle pour aligner ses prétentions formelles avec les spécifications normatives réelles de l'IETF et du W3C.

### 5.5 Méthode de vérification indépendante (Verification Method)
Pour vérifier de manière indépendante les constats de cet audit :
1. *Vérification textuelle* :
   - Consulter la page 198 de `documents/DOCUMENT_TEXT_MAP.md` (lignes 17850-17950) pour constater l'aveu explicite d'absence de démonstration.
   - Consulter la page 151 (lignes 12560-12590) pour observer la troncature textuelle sous le Tableau 12.3.
2. *Vérification visuelle* :
   - Ouvrir `documents/scratch/document_pages/page-151.png`, `page-152.png` et `page-153.png` pour confirmer les coupures de phrases par les encadrés flottants.
3. *Vérification normative* :
   - Consulter la RFC 8693 §4.1 (site de l'IETF) pour vérifier l'interdiction de baser le contrôle d'accès sur `act`.
   - Consulter la spécification A2A v1.0.0 pour vérifier l'absence des champs temporels `iat`, `exp` et `nbf`.
   - Consulter le standard W3C VC v2.0 §5 pour confirmer la coexistence incompatible des preuves Data Integrity et JOSE/COSE.
   - Consulter NIST FIPS 204 (Tableau 1 et Tableau 2) pour vérifier les tailles de clés et signatures de ML-DSA-44 et ML-DSA-87.
