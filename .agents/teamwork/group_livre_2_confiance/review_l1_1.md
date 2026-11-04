# Revue Critique Évoluée (Niveau 1 - RSA) — Livre II : Faire Confiance (Ch. 12 à 21 & Ch. 22 partiel, pp. 144–255)

**Document audité** : `documents/Compendium.pdf` (*Interopérabilité et Orchestration en Entreprise Agentique*, André-Guy Bruneau M.Sc. IT, Édition Novembre 2026, 663 pages)  
**Segment audité** : `segment_livre_2_confiance` (Segments S14 à S23 du plan de revue, pages 144 à 255)  
**Auteur de la synthèse** : Review Aggregator 1 (Niveau 1 de l'arbre RSA)  
**Candidats de Niveau 0 audités** : Candidat 1 (`handoff_1.md`) et Candidat 2 (`handoff_2.md`)  
**Date d'arbitrage** : 3 novembre 2026  
**Statut du livrable** : Rapport d'arbitrage et d'évolution critique consolidé (Niveau 1 final)

---

## 1. Résumé exécutif d'évaluation du Livre 2

Le Livre II du *Compendium*, intitulé *« Faire confiance : Identité non humaine et délégation vérifiable »* (ch. 12 à 21, complété aux pages 252-255 par l'introduction du Livre III, ch. 22), constitue la clé de voûte de l'ouvrage sur les plans sécuritaire, cryptographique et réglementaire. Sa thèse centrale affirme que le déploiement d'agents autonomes en entreprise régulée (notamment sous la juridiction du BSIF, de l'AMF et de la Loi 25 au Québec) est irrecevable sans une identité non humaine opposable, une chaîne de délégation vérifiable et une trajectoire de migration post-quantique chiffrée.

L'arbitrage contradictoire de Niveau 1 (combinant les rapports indépendants des Candidats 1 et 2, vérifiés contre `DOCUMENT_TEXT_MAP.md` et les épreuves typographiques `page-144.png` à `page-255.png`) salue la rigueur documentaire de l'auteur sur la classification épistémique des sources (distinction rigide entre faits vérifiés, faits négatifs établis et absences de documentation de degrés 1 à 3). Cependant, l'évaluation de Niveau 1 révèle un **décalage structurel profond entre l'ambition formelle affichée et les démonstrations réelles de l'ouvrage**, matérialisé par cinq failles systémiques :

1. **Falsification formelle du « problème des deux sauts » et double erreur sur la RFC 8693 (Ch. 17)** :  
   Alors que le plan directeur (`REVIEW_PLAN.md`) promettait une « démonstration mathématique de rupture d'opposabilité dans les délégations récursives $A \to B \to C$ », le texte du Compendium ne contient **aucune démonstration formelle, aucun calcul logique et aucune formule mathématique**. L'auteur concède lui-même à la page 198 qu'« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict ».  
   Pire encore, le traitement de la RFC 8693 (*OAuth 2.0 Token Exchange*) cumule deux erreurs critiques :
   - *Une erreur factuelle directe* (p. 197 et Tableau 17.2, p. 198) : l'auteur qualifie la composition sur plus d'un saut d'« absence de documentation, degré 3 », ignorant que la section 4.4 de la RFC 8693 standardise explicitement les *Nested 'act' Claims* pour les délégations multi-sauts.
   - *Une illusion d'opposabilité* : le recours au Token Exchange comme mécanisme de contrôle d'accès est proscrit par la RFC 8693 §4.1 elle-même, qui stipule impérativement que la revendication `act` est purement informative et ne doit pas servir aux décisions d'accès (*« informational only and MUST NOT be used for access control decisions »*).  
   À l'inverse des assertions du texte, la théorie des capabilités cryptographiques (Macaroons sous PRF, tokens Biscuit sous Datalog) démontre que l'opposabilité peut être mathématiquement préservée pour tout saut $n \ge 1$. La rupture constatée en entreprise n'est donc pas un théorème mathématique, mais un artefact opérationnel causé par le recours à des *bearer tokens* déconnectés et l'absence de révocation synchrone.

2. **Défauts typographiques et textuels bloquants lors de la compilation (Ch. 12 et 13, pp. 151–153)** :  
   L'inspection visuelle haute résolution confirme trois bris de composition inacceptables pour un texte de référence :
   - *Page 151* : Phrase tronquée net sous le Tableau 12.3 (« un document » coupé net sans point final, précédé d'un paragraphe orphelin commençant sans majuscule : « de groupe de travail en appel... »).
   - *Pages 152 et 153* : Deux encadrés pleine largeur (« Thèse » et « EXTRACTION CONDUITE LE 30 JUILLET 2026... ») ont été injectés au milieu exact de phrases actives du corps de texte, fragmentant la syntaxe grammaticale (« d'une [Thèse...] section, ne le définit... » et « la preuve [EXTRACTION...] incorporée... »).

3. **Collision d'identifiants et erreur matérielle d'attribution dans la Figure 17.2 (p. 193)** :  
   Dans le schéma pivot du chapitre 17 modélisant les rangs de la chaîne de mandat, la boîte 3 (« Carte d'agent ») est associée à la référence `F-29, [A]`. Or, dans l'ensemble du Compendium (pp. 147, 192, 198), `F-29` désigne exclusivement le brouillon IETF sur les *Transaction Tokens* (propagation de contexte), tandis que la Carte d'agent relève des entrées `F-01` à `F-07`.

4. **Fragilité rédhibitoire de l'Agent Card A2A et chimère du « Passeport d'agent » (Ch. 15 et 16)** :  
   L'Agent Card (A2A v1.0.0 de Google / Linux Foundation) est présentée à tort comme l'ancrage d'un « passeport d'agent ». En réalité, il s'agit d'un simple descripteur fonctionnel de capacités (points de terminaison d'outils) dépourvu de tout champ de validité temporelle (`iat`, `exp`, `nbf`), sans protocole de révocation ni magasin de clés de confiance prescrit, et dont la signature n'est qu'optionnelle (`MAY`). Ériger la règle « Rien n'entre au maillage sans lui » (p. 180) pour un objet virtuel non standardisé crée une aporie d'exploitation insoluble.

5. **Angle mort de charge réseau sur la transition Post-Quantique FIPS 204 (Ch. 21)** :  
   Bien que l'auteur fasse preuve d'une grande lucidité sur le statut réglementaire des normes NIST (FIPS 203, 204 et 205 ratifiés le 13 août 2024 ; calendrier NIST IR 8547 non contraignant pour les banques canadiennes), il omet totalement de quantifier l'impact dimensionnel des signatures post-quantiques sur la communication agentique : ML-DSA-44 requiert 2 420 octets (contre 64 octets pour Ed25519, soit un facteur d'accroissement de 38x), provoquant la saturation des mémoires tampons d'API Gateway et du contexte LLM lors d'échanges intensifs A2A / MCP.

---

## 2. Matrice consolidée des défauts classés par sévérité

### 2.1 Tableau synoptique unifié

| ID Défaut | Sévérité | Chapitre | Page | Intitulé synthétique du défaut | Candidats d'origine |
|---|---|---|---|---|---|
| **DEF-L2-01** | **Bloquant** | Ch. 17 | pp. 196–199 | Falsification formelle du théorème des deux sauts et double erreur normative sur RFC 8693 (§4.1 et §4.4) | Corroboré (C1 DEF-01 / C2 DEF-01, DEF-03) |
| **DEF-L2-02** | **Bloquant** | Ch. 12 | p. 151 | Troncature textuelle critique sous le Tableau 12.3 (« un document » coupé net) | Retenu (C1 DEF-L2-02, vérifié visuellement) |
| **DEF-L2-03** | **Bloquant** | Ch. 13 | pp. 152–153 | Débordement d'encadrés pleine largeur fragmentant des phrases actives du corps de texte | Retenu (C1 DEF-L2-03, vérifié visuellement) |
| **DEF-L2-04** | **Bloquant** | Ch. 17 | p. 193 | Collision d'identifiants et erreur matérielle d'attribution dans la Figure 17.2 (`F-29` attribué à l'Agent Card) | Retenu (C2 DEF-02, vérifié visuellement) |
| **DEF-L2-05** | **Majeur** | Ch. 15–16 | pp. 167–184 | Faille structurelle de l'Agent Card A2A v1.0.0 (absence de fraîcheur et révocation) et chimère du « Passeport » | Corroboré (C1 DEF-L2-05 / C2 S15, S17) |
| **DEF-L2-06** | **Majeur** | Ch. 13 | pp. 153–157 | Schisme d'interopérabilité au sein de W3C VC v2.0 et omission des preuves à divulgation sélective (SD-JWT VC / BBS+) | Corroboré (C1 DEF-L2-04 / C2 DEF-06) |
| **DEF-L2-07** | **Majeur** | Ch. 12 | pp. 144–150 | Biais réducteur sur OAuth 2.0 (omission de DPoP RFC 9449 et mTLS RFC 8705) et caducité du draft SCIM CSA | Corroboré (C1 DEF-L2-06 / C2 DEF-04, DEF-05) |
| **DEF-L2-08** | **Majeur** | Ch. 19–20 | pp. 210–224 | Illusion du confinement cognitif face au *Confused Deputy* et à la Triade Létale de Willison | Corroboré (C1 DEF-L2-07 / C2 S20) |
| **DEF-L2-09** | **Majeur** | Ch. 20 | pp. 230–235 | Rupture d'imputabilité dans l'Agentic SOC par contournement des contrôles PIM/TAP | Corroboré (C1 DEF-L2-08 / C2 DEF-08) |
| **DEF-L2-10** | **Majeur** | Ch. 21 | pp. 238–248 | Omission de la charge volumétrique et de la latence des signatures PQC FIPS 204 (ML-DSA vs Ed25519) | Corroboré (C1 DEF-L2-09 / C2 DEF-07) |
| **DEF-L2-11** | **Mineur** | Ch. 12 | p. 148 | Glitch rédactionnel et contradiction interne sur la date de révision (affirmation d'absence suivie de la date) | Retenu (C2 DEF-09) |
| **DEF-L2-12** | **Mineur** | Ch. 21 | pp. 248–249 | Ambiguïté de portée sur l'opposabilité de la directive canadienne ITSM.40.001 au secteur financier | Retenu (C1 DEF-L2-10) |
| **DEF-L2-13** | **Mineur** | Ch. 14 & 22 | p. 166 & p. 253 | Flottement terminologique et risque de confusion entre les 3 échelles d'autonomie et OO1-OO4 | Retenu (C2 DEF-10) |

---

### 2.2 Fiches détaillées des défauts

#### DEF-L2-01 [Bloquant / Erreur formelle, théorique et normative]
- **Localisation** : Chapitre 17, pages 196 à 199 (§17.6, §17.6.1, §17.6.2, Figure 17.6, Tableau 17.2).
- **Citations textuelles exactes** :  
  - Page 197 : *« Ce que ce texte prévoit ou tait de la composition de plusieurs délégations successives n’est pas documenté par le socle — degré 3. Il ne s’ensuit ni qu’une telle composition soit prévue, ni qu’elle ne le soit pas. »*
  - Page 198 : *« Le terme "limites démontrées" mérite d'être borné avant d'écrire quoi que ce soit : aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
  - Page 198 (Tableau 17.2) : *« La composition sur plus d'un saut : absence de documentation, degré 3 »*.
- **Diagnostic causal approfondi** :  
  1. *Absence intégrale de preuve formelle* : Le plan de révision annonçait un résultat théorique majeur : un « théorème des deux sauts démontrant mathématiquement la rupture d'opposabilité dans les délégations récursives $A \to B \to C$ ». Or, le texte n'articule aucun formalisme mathématique, aucune logique d'autorisation formelle (ABLP, SecPAL, logique BAN) et aucun modèle stochastique. L'auteur concède lui-même ce vide.
  2. *Erreur factuelle sur la RFC 8693 §4.4* : L'auteur affirme qu'il s'agit d'une « absence de documentation, degré 3 » dans le standard IETF Token Exchange. C'est faux : la section 4.4 de la RFC 8693 spécifie expressément les *Nested 'act' Claims*, définissant le schéma JSON récursif permettant à une chaîne d'acteurs de propager la délégation sur $N$ sauts. L'auteur a confondu une omission de sa fiche de lecture interne `F-47` avec une carence de la norme internationale.
  3. *Incompatibilité normative de la RFC 8693 §4.1 pour l'opposabilité* : Bien que la RFC 8693 permette la syntaxe multi-sauts, sa clause normative §4.1 détruit toute prétention d'opposabilité en disposant expressément : *« The "act" (actor) claim [...] is informational only and MUST NOT be used for access control decisions »*. Le destinataire final $C$ ou le serveur de ressources $S$ a l'interdiction de fonder son autorisation sur cette chaîne.
  4. *Fausseté de l'hypothèse de rupture intrinsèque à $N=2$* : La rupture d'opposabilité n'est pas une loi mathématique universelle de la délégation. Dans les algèbres de capabilités cryptographiques (Abadi et al., *A Calculus for Access Control in Distributed Systems* ; Miller et al.), une délégation est une réduction de droits transitivement signée.
- **Contre-exemple formel et Correctif** :  
  Soit une chaîne de capabilités cryptographiques à base de *Macaroons* (Birgisson et al., NDSS 2014) ou de tokens *Biscuit* (Geal et al.) avec moteur Datalog embarqué.  
  Le mandant racine $M$ émet le jeton initial :
  $$T_0 = (id_M, \text{scope}_0, \sigma_0) \quad \text{avec} \quad \sigma_0 = \text{HMAC}(k_M, id_M \parallel \text{scope}_0)$$
  L'agent $A_1$ délègue à $A_2$ en adjoignant une atténuation $\text{caveat}_1$ et dérive la signature :
  $$T_1 = (T_0, id_{A_1}, \text{caveat}_1, \sigma_1) \quad \text{avec} \quad \sigma_1 = \text{HMAC}(\sigma_0, id_{A_1} \parallel \text{caveat}_1)$$
  Par induction, pour tout saut $n \ge 1$ :
  $$T_n = (T_{n-1}, id_{A_n}, \text{caveat}_n, \sigma_n) \quad \text{avec} \quad \sigma_n = \text{HMAC}(\sigma_{n-1}, id_{A_n} \parallel \text{caveat}_n)$$
  Sous l'hypothèse de sécurité des fonctions pseudo-aléatoires (PRF) et de non-falsifiabilité des signatures (EUF-CMA), l'opposabilité et l'atténuation sont préservées pour tout $n \in \mathbb{N}^*$.  
  **Correctif** : Requalifier le problème des deux sauts en « défi d'impédance protocolaire et de révocation en cascade en entreprise ». Remplacer la fausse assertion d'absence sur la RFC 8693 par l'analyse de sa section 4.4, tout en démontrant pourquoi la clause §4.1 invalide son usage en contrôle d'accès strict. Citer les architectures Biscuit / Macaroons comme solutions formellement prouvées.

#### DEF-L2-02 [Bloquant / Erreur de composition typographique]
- **Localisation** : Chapitre 12, page 151 (sous le Tableau 12.3, vérifié sur `page-151.png` et `DOCUMENT_TEXT_MAP.md` lignes 12720–12734).
- **Citation textuelle exacte** :  
  Page 151 : *« ...rien de son texte n’est établi. de groupe de travail en appel de dernière relecture propose un mécanisme de propagation du contexte (Vol. III F-29)... »* puis *« L’ordre des faits est donc celui-ci, et il est daté du 21 juillet 2026 : un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document »* [interruption brutale, suivi du saut de paragraphe] *« Ce qui manque à cet inventaire n’est pas une pièce... »*.
- **Diagnostic causal approfondi** :  
  Un débordement d'environnement flottant lors de la compilation a fragmenté le texte en deux endroits de la page 151 :
  1. La fin de la phrase sur OIDC s'interrompt et enchaîne directement sans majuscule ni transition sur un fragment orphelin (« de groupe de travail en appel... »).
  2. La phrase de conclusion de la section sous le Tableau 12.3 est tronquée net après le mot « document », privant le lecteur de la formulation de synthèse du chapitre 12.
- **Correctif formel** :  
  Ajuster les ressorts verticaux du gabarit de mise en page autour du Tableau 12.3 et rétablir le segment textuel complet :  
  *« ...un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document de groupe de travail en appel de dernière relecture propose un mécanisme de propagation du contexte (Vol. III F-29) ; et une spécification de laboratoire demeure un document d'orientation informel sans portée normative. »*

#### DEF-L2-03 [Bloquant / Erreur de mise en page structurelle]
- **Localisation** : Chapitre 13, pages 152 et 153 (vérifié sur `page-152.png` et `page-153.png`).
- **Citations textuelles exactes** :  
  - Page 152 : *« ...le Vol. I, qui porte le terme au titre d’une »* [Encart Thèse intercalé] *« section, ne le définit ni ne le réemploie dans le corps de celle-ci... »*.
  - Page 153 : *« La Recommandation en admet deux familles, non une : la preuve »* [Encart pleine largeur d'extraction intercalé] *« incorporée, portée par la propriété proof... »*.
- **Diagnostic causal approfondi** :  
  Les blocs flottants « Thèse » et « EXTRACTION CONDUITE LE 30 JUILLET 2026 » ne disposent pas de séparateurs de paragraphe stricts (`\par` ou ancrage inline `[H]`). Le compilateur a injecté les blocs au milieu exact de liaisons grammaticales (entre l'article indéfini « une » et le substantif « section » à la p. 152 ; entre le substantif « preuve » et son adjectif « incorporée » à la p. 153).
- **Correctif formel** :  
  Forcer les ruptures de paragraphes en amont et en aval de chaque encadré méthodologique et repositionner l'ancrage des boîtes d'extraction pour préserver l'intégrité de la syntaxe linéaire.

#### DEF-L2-04 [Bloquant / Erreur matérielle d'attribution]
- **Localisation** : Chapitre 17, page 193 (Figure 17.2, vérifiée sur `page-193.png`).
- **Citation textuelle exacte** :  
  Figure 17.2, Boîte 3 : *« 3 Carte d'agent | Porte l'identité, non la chaîne. | F-29, [A] »*.
- **Diagnostic causal approfondi** :  
  Collision directe d'identifiants de source. Dans tout l'ouvrage (p. 147, 151, 192, 198), la fiche `F-29` désigne le projet IETF OAuth sur les *Transaction Tokens* (`draft-ietf-oauth-transaction-tokens`, révision -09 du 6 juillet 2026, propagation de contexte). La Carte d'agent (Agent Card A2A de Google / Linux Foundation) est indexée sous les fiches `F-01` à `F-07`. L'attribution de `F-29` à la boîte « Carte d'agent » est une coquille matérielle d'auteur qui désoriente le lecteur et fausse l'index de traçabilité.
- **Correctif formel** :  
  Modifier la boîte 3 de la Figure 17.2 : soit remplacer l'intitulé par « Jeton de transaction (propagation de contexte) » en conservant `F-29, [A]`, soit remplacer la référence par `F-04 / F-07, [A]` en conservant l'intitulé « Carte d'agent ».

#### DEF-L2-05 [Majeur / Faille structurelle d'architecture de sécurité]
- **Localisation** : Chapitres 15 et 16, pages 167 à 184 (§15.1, §15.2, §16.1, Figure 15.1, Tableau 15.1).
- **Citation textuelle exacte** :  
  Pages 172-173 : *« La spécification de la carte d'agent signée dans A2A v1.0.0 n'impose aucune contrainte de fraîcheur : aucun champ iat, aucun champ exp, aucun champ nbf [...] et l'usage de la signature y est MAY, tandis que sa vérification est SHOULD »*.
- **Diagnostic causal approfondi** :  
  L'ouvrage érige l'Agent Card signée A2A en pivot du « Passeport d'agent » tout en affirmant péremptoirement : « Rien n'entre au maillage sans lui » (p. 180). Or, les faiblesses intrinsèques de la spécification A2A v1.0.0 rendent cette prescription inapplicable et dangereuse :
  1. Absence totale de bornes temporelles (`iat`, `exp`, `nbf`) : une carte compromise ou révoquée reste syntaxiquement valide indéfiniment.
  2. Caractère facultatif de la sécurité : la signature est un `MAY`, la vérification un `SHOULD`, et la gestion d'un magasin de clés locales un `MAY`.
  3. Absence de protocole de révocation : aucun équivalent de CRL ou OCSP n'est défini.
  4. Confusion entre descripteur de capacités et identité légale : l'Agent Card ne lie aucunement l'agent à la personne morale responsable juridique des transactions.
- **Correctif formel** :  
  Découpler explicitement la pile en trois couches autonomes :
  - Couche Découverte : l'Agent Card A2A cantonnée au rôle d'annuaire technique d'outils ;
  - Couche Authentification : un jeton d'instance éphémère lié cryptographiquement par clé asymétrique (SPIFFE SVID ou certificat mTLS RFC 8705) ;
  - Couche Autorisation / Mandat : une attestation de mandat éphémère à divulgation sélective (SD-JWT VC ou token Biscuit) portant explicitement l'identité juridique du mandant et une durée de vie strictement bornée ($\Delta t \le 1\text{ h}$).

#### DEF-L2-06 [Majeur / Lacune d'interopérabilité et de minimisation]
- **Localisation** : Chapitre 13, pages 153 à 157 (§13.2, Tableau 13.1).
- **Citation textuelle exacte** :  
  Page 153 : *« Deux familles de preuve pour un même modèle de données signifient que deux implémentations conformes peuvent être mutuellement illisibles : c'est, transposé au niveau du justificatif, exactement le constat de conformité ≠ interopérabilité... »*.
- **Diagnostic causal approfondi** :  
  La Recommandation W3C VC v2.0 (15 mai 2025) institutionnalise deux formats mutuellement incompatibles :
  - *Data Integrity Proofs* en JSON-LD (canonicalisation de graphes RDF RFC 8785 / RDFC-2022 et cryptosuites `eddsa-rdfc-2022`) ;
  - *Enveloping Proofs* en jetons plats sérialisés (IETF JOSE/COSE / SD-JWT).  
  En outre, le Compendium omet d'analyser l'apport critique des spécifications de divulgation sélective (*Selective Disclosure* - SD-JWT VC RFC 9542 et W3C BBS Cryptosuite v1.0). Sans ces mécanismes, un agent ne peut pas restreindre la preuve de son mandat aux seules données strictement nécessaires à l'acte, violant frontalement le principe de minimisation de l'article 12.1 de la Loi 25 québécoise.
- **Correctif formel** :  
  Spécifier une exigence de profilage d'application (*Application Profile*) imposant le format SD-JWT-VC (RFC 9542) pour les échanges inter-domaines et documenter formellement l'impossibilité d'une interopérabilité décentralisée universelle sans restriction de profil.

#### DEF-L2-07 [Majeur / Biais d'analyse protocolaire]
- **Localisation** : Chapitre 12, pages 144 à 150 (§12.1 à §12.3).
- **Citation textuelle exacte** :  
  Page 144 : *« ...le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. »*
- **Diagnostic causal approfondi** :  
  Le réquisitoire contre OAuth 2.0 repose sur un biais réducteur : assimiler l'architecture OAuth au seul profil de jeton porteur impersonnel (RFC 6750). L'auteur passe sous silence les standards ratifiés de *Proof-of-Possession* de l'IETF :
  - RFC 8705 (2020) : liaison mTLS de jetons d'accès aux certificats clients ;
  - RFC 9449 (2023) : DPoP (*Demonstrating Proof-of-Possession*), qui neutralise le vol et le rejeu de jetons en liant cryptographiquement chaque requête HTTP à une paire de clés asymétriques éphémères générées par le client.  
  Toutefois, même sous DPoP, OAuth 2.0 reste inadapté aux agents autonomes car il ne modélise pas la subjectivité juridique d'un mandataire autonome. Sur le plan de SCIM 2.0 (RFC 7643/7644), le projet de registre de la Cloud Security Alliance reposait sur `draft-abbey-scim-agent-extension-00`, devenu caduc le 19 avril 2026.
- **Correctif formel** :  
  Intégrer RFC 9449 (DPoP) comme contre-mesure d'ingénierie immédiate face au rejeu de jetons, et démontrer que l'alternative architecturale d'avenir réside dans la RFC 9635 (GNAP - *Grant Negotiation and Authorization Protocol*, octobre 2024), conçue dès l'origine pour les interactions asynchrones sans navigateur avec négociation dynamique de droits cryptographiquement liés.

#### DEF-L2-08 [Majeur / Insuffisance de sécurité architecturale face au Confused Deputy]
- **Localisation** : Chapitres 19 et 20, pages 210 à 224 (§19.2, §19.3, §20.1).
- **Citation textuelle exacte** :  
  Page 214 : *« Le problème du confused deputy identifié par Hardy en 1988 resurgit avec les agents : l'agent dispose de privilèges légitimes sur des outils, mais son planificateur interne est manipulé par une injection indirecte provenant d'un contenu externe non fiable »*.
- **Diagnostic causal approfondi** :  
  Le texte formalise avec exactitude la « triade létale » de Simon Willison :
  $$(\text{AccèsDonnéesPrivées}) \wedge (\text{IngestionContenuNonFiable}) \wedge (\text{CanalExfiltration}) \implies \text{Compromission}$$
  Cependant, les sections 19.3 et 20.1 suggèrent des remèdes probabilistes (filtrage de prompts par LLM guardrails, classificateurs d'intention). Comme l'ont démontré Simon Willison, Perez et al., et les travaux sur AgentPoison (NeurIPS 2024), **aucun filtre textuel sémantique ne peut offrir de garantie mathématique contre l'injection indirecte**. Traiter une défaillance de contrôle d'accès par un modèle stochastique est une hérésie de sécurité.
- **Correctif formel** :  
  Imposer le principe du *cloisonnement architectural déterministe* : briser physiquement la triade au niveau du plan d'exécution :
  - *Règle de révocation dynamique de canal* : dès lors qu'un agent ingère un contenu externe non vérifié (courriel, scraping, document non signé), la plateforme d'orchestration révoque immédiatement tous ses canaux réseau sortants non déterministes.
  - *Architecture Dual-Agent avec sas typé* : l'agent d'ingestion non fiable est cantonné dans une sandbox hermétique ; l'agent exécuteur privilégié ne reçoit que des structures de données strictement typées et validées par un schéma déterministe (Protobuf / JSON Schema strict).

#### DEF-L2-09 [Majeur / Aporie opérationnelle de l'Agentic SOC]
- **Localisation** : Chapitre 20, pages 230 à 235 (§20.5, §20.9, Tableau 20.2).
- **Citation textuelle exacte** :  
  Page 233 : *« Déployer des agents de défense en leur attribuant des comptes utilisateurs pour leur permettre d'agir sur le SI [...] crée une dérive d'imputabilité où les mécanismes de PIM (Privileged Identity Management) et de TAP (Temporary Access Pass) échouent »*.
- **Diagnostic causal approfondi** :  
  Dans les architectures de SOC automatisé (Microsoft Copilot for Security, Google Security AI), l'incapacité d'intégrer des identités d'agents pures pousse les équipes d'exploitation à doter les agents de comptes d'utilisateurs humains avec privilèges élevés. Cette pratique induit :
  - L'incompatibilité avec le PIM : le PIM exigeant une approbation humaine MFA interactive, les administrateurs mettent en place des auto-approbations ou des passes permanents (TAP), détruisant le principe du moindre privilège ;
  - L'opacité médico-légale : les journaux d'audit attribuent les modifications d'infrastructure au compte de service sans trace opposable de l'empreinte d'invite ou de l'état du modèle ;
  - La violation des exigences de gouvernance prudentielle (BSIF E-23 et article 12.1 de la Loi 25).
- **Correctif formel** :  
  Spécifier un patron de *Double Commande Déterministe (Dual-Control FSM / OO4)* : tout ordre de remédiation infrastructurelle émis par un agent du SOC doit être contresigné cryptographiquement par un PDP (*Policy Decision Point*) formel appliquant des invariants immuables, avec journalisation WORM de l'arbre d'inférence.

#### DEF-L2-10 [Majeur / Angle mort volumétrique de la cryptographie post-quantique]
- **Localisation** : Chapitre 21, pages 238 à 248 (§21.3 à §21.7, Tableau 21.3).
- **Citation textuelle exacte** :  
  Page 247 : *« ...et une soutenabilité de performance non établie : les signatures et échanges post-quantiques, dont les tailles d'artefacts sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de main »*.
- **Diagnostic causal approfondi** :  
  L'auteur évoque la crypto-agilité comme un simple paramètre de version dans les en-têtes JSON, sans chiffrer l'asymétrie volumétrique des signatures post-quantiques normalisées par le NIST (FIPS 204) :
  - Clé publique et signature Ed25519 classique : $32\text{ o} + 64\text{ o} = 96\text{ octets}$.
  - ML-DSA-44 (niveau de sécurité NIST 2) : clé publique de $1\,312\text{ octets}$ et signature de $2\,420\text{ octets}$, soit $3\,732\text{ octets}$ (multiplication par **38,8**).
  - ML-DSA-87 (niveau 5) : clé publique de $2\,592\text{ octets}$ et signature de $4\,627\text{ octets}$, soit $7\,219\text{ octets}$ (multiplication par **75**).  
  Dans des architectures multi-agents générant des milliers d'appels A2A et MCP par minute, ce gonflement provoque un dépassement systématique des tampons d'en-têtes HTTP des passerelles d'API (souvent plafonnés à 8 Ko), un engorgement de bande passante et une surconsommation critique de fenêtres de contexte LLM lorsque les jetons sont injectés dans les prompts d'orchestration.
- **Correctif formel** :  
  Fournir une modélisation analytique du surcoût réseau :
  $$\text{OverheadRatio} = \frac{\text{Taille}_{\text{PQC}}}{\text{Taille}_{\text{Ed25519}}} \approx 38\text{ à } 75$$
  Prescrire une architecture hybride en couches : sécuriser la couche transport (L4) via TLS 1.3 post-quantique (échange de clés ML-KEM-768 selon FIPS 203), tout en conservant au niveau applicatif (L7) des jetons de session signés avec des clés symétriques éphémères dérivées (HMAC-SHA256 ou KMAC), réservant les signatures asymétriques lourdes ML-DSA aux seuls mandats maîtres à longue durée de vie. Utiliser les signatures composites hybrides (NIST SP 800-227 / `draft-ietf-lamps-pq-composite-sigs`).

#### DEF-L2-11 [Mineur / Glitch rédactionnel et contradiction interne]
- **Localisation** : Chapitre 12, page 148 (§12.5).
- **Citation textuelle exacte** :  
  Page 148 : *« Le chapitre n'écrit donc aucune date de publication pour cette révision. Parue le 28 juillet 2026 (2026-07-28). »*.
- **Diagnostic causal approfondi** :  
  Collision de mise à jour lors de l'intégration des notes d'actualisation : la première phrase affirme ne pas donner de date de publication, puis la seconde colle immédiatement la date entre parenthèses.
- **Correctif formel** :  
  Harmoniser la phrase : *« La date de publication a été confirmée le 28 juillet 2026 lors de la révision d'actualisation de la source. »*

#### DEF-L2-12 [Mineur / Ambiguïté de portée réglementaire canadienne]
- **Localisation** : Chapitre 21, pages 248-249 (§21.8, Tableau 21.4).
- **Citation textuelle exacte** :  
  Page 248 : *« ITSM.40.001 vise le gouvernement fédéral, non les banques ni les assureurs : une institution qui s'en réclamerait comme d'une échéance applicable lirait, encore une fois, le plafond d'un autre »*.
- **Diagnostic causal approfondi** :  
  Bien que l'avertissement textuel soit limpide, la disposition du Tableau 21.4 mettant en exergue les jalons 2031 et 2035 peut prêter à confusion pour un directeur de la conformité bancaire canadienne. Le BSIF / OSFI n'a émis qu'un bulletin d'orientation en mars 2026 et l'AMF n'a fixé aucune date butoir contraignante.
- **Correctif formel** :  
  Ajouter une note de bas de tableau explicite rappelant que le secteur financier canadien sous réglementation BSIF/AMF demeure régi par la gestion générale du risque opérationnel (BSIF E-21 / E-23) sans calendrier quantique coercitif distinct.

#### DEF-L2-13 [Mineur / Flottement terminologique des échelles d'autonomie]
- **Localisation** : Chapitres 14 et 22, page 166 et page 253.
- **Citation textuelle exacte** :  
  Page 166 : *« Trois échelles homonymes coexistent au Vol. I, et seuls le cardinal et la numérotation les discriminent »*.
- **Diagnostic causal approfondi** :  
  L'ouvrage renvoie la désambiguïsation formelle des niveaux d'autonomie au chapitre 43, créant une zone de flottement sémantique entre l'échelle opérationnelle à 4 paliers, l'échelle à 6 niveaux du Vol. I et la taxonomie d'orchestration OO1–OO4 du ch. 22.
- **Correctif formel** :  
  Insérer un tableau récapitulatif synoptique au §14.4 alignant immédiatement les trois échelles.

---

## 3. Analyse critique approfondie section par section (Ch. 12 à 21 & Ch. 22 partiel)

### 3.1 Ch. 12 (pp. 144–151) : L'héritage d'un demi-siècle et les standards IAM étirés
- **Points forts** : La déconstruction historique est remarquable. L'auteur démontre avec pertinence que les agents n'arrivent pas sur une page blanche, mais héritent d'un demi-siècle de dette technique d'identités machines (comptes de service, certificats X.509, clés d'API). L'analyse de l'incident UNC6395 (août 2025 sur Salesforce) démontre concrètement la vulnérabilité des jetons d'accès statiques.
- **Insuffisances et faiblesses** : Le chapitre commet une erreur de perspective en assimilant OAuth 2.0 au seul *bearer token* impersonnel de la RFC 6750, sans mentionner que les standards RFC 8705 (mTLS) et RFC 9449 (DPoP) lient cryptographiquement les jetons à des clés privées de clients. Par ailleurs, la critique de SCIM 2.0 (RFC 7643) méconnaît le mécanisme d'extension de schéma (§3.3) utilisé par les solutions de pointe (Microsoft Entra Agent ID).
- **Incident typographique** : La page 151 subit une troncature nette sous le Tableau 12.3 (« un document » coupé net, DEF-L2-02).

### 3.2 Ch. 13 (pp. 152–160) : L'identité décentralisée (W3C VC v2.0, DID v1.1)
- **Points forts** : L'observation selon laquelle aucune grande institution financière n'exploite de DID en production (degré 3 d'absence, p. 158) est parfaitement exacte. La critique de `did:web` (qui réintroduit une dépendance totale au DNS et à la PKI Web périmétrique, annulant la souveraineté décentralisée) est d'une grande lucidité.
- **Insuffisances et faiblesses** : Le chapitre passe sous silence le schisme opérationnel de W3C VC v2.0 (Recommandation du 15 mai 2025) : la fracture irréconciliable entre *Data Integrity Proofs* (graphes RDF RDFC-2022) et *Enveloping Proofs* (JOSE/COSE) empêche tout échange direct sans profilage préalable (DEF-L2-06). De plus, l'omission de la divulgation sélective (SD-JWT VC et BBS+) prive l'ouvrage de la solution technique clé pour la conformité à l'article 12.1 de la Loi 25.
- **Incident typographique** : Débordement d'encadrés flottants aux pages 152 et 153 fragmentant des phrases actives du corps de texte (DEF-L2-03).

### 3.3 Ch. 14 (pp. 160–167) : La grille d'évaluation de la confiance et les 5 questions
- **Points forts** : La grille des 5 questions transversales (Q-A : *Qui es-tu ?*, Q-B : *Qui t'a créé ?*, Q-C : *Pour qui agis-tu ?*, Q-D : *Que peux-tu faire ?*, Q-E : *Qui en répond ?*) constitue l'une des contributions méthodologiques les plus robustes de l'ouvrage pour les comités d'architecture d'entreprise.
- **Insuffisances et faiblesses** : La grille demeure une heuristique sans appareil de vérification formelle. Le lien avec les échelles d'autonomie souffre d'un flottement terminologique (DEF-L2-13).

### 3.4 Ch. 15 (pp. 167–180) : L'Agent Card signée A2A et les registres gouvernés
- **Points forts** : L'analyse de l'Agent Card A2A v1.0.0 (Google / Linux Foundation) canonicalisée par RFC 8785 (JCS) et signée par RFC 7515 (JWS) est méticuleuse. La question épistémique posée (« qui signe les signataires ? ») démonte le mythe de la confiance autonome sans racine PKI d'entreprise. L'inventaire des registres commerciaux (Entra Agent ID, GCP Agent Directory) illustre le risque d'enfermement propriétaire.
- **Insuffisances et faiblesses** : L'auteur ne dénonce pas assez vigoureusement les failles de sécurité de la spécification A2A v1.0.0 : absence de timestamps (`exp`, `iat`), signature facultative (`MAY`), absence de magasin de clés de confiance et absence totale de révocation (DEF-L2-05).

### 3.5 Ch. 16 (pp. 180–188) : Le Passeport d'agent virtuel
- **Points forts** : Le passeport d'agent est explicitement qualifié d'« objet de synthèse virtuel » assemblant quatre composantes (carte signée, inscription au registre, chaîne de mandat, attestations). L'auteur évite l'écueil d'en faire une norme existante.
- **Insuffisances et faiblesses** : Formuler l'impératif catégorique « Rien n'entre au maillage sans lui » (p. 180) paralyse tout déploiement en 2026, car cet objet n'existe dans aucun standard international. Le tableau des substituts provisoires (Tableau 16.2) reste un colmatage hétéroclite sans opposabilité réglementaire.

### 3.6 Ch. 17 (pp. 188–201) : La chaîne de mandat et la réfutation des deux sauts
- **Points forts** : L'accent mis sur la distinction fondamentale entre identité (qui est l'agent) et mandat (pour qui il agit) est capital. L'introduction du protocole de paiement AP2 (v0.2.0, SD-JWT) et l'analyse des mandats sans présence humaine (*Human Not Present*) sont à la pointe de l'actualité.
- **Insuffisances et faiblesses** : C'est le maillon le plus faible du Livre II. Falsification formelle du prétendu théorème mathématique des deux sauts (DEF-L2-01), double erreur d'analyse sur la RFC 8693 (§4.1 et §4.4), et erreur matérielle d'attribution dans la Figure 17.2 associant l'Agent Card à la fiche `F-29` des Transaction Tokens (DEF-L2-04).

### 3.7 Ch. 18 (pp. 201–210) : Know Your Agent (KYA) et le vide inter-domaines
- **Points forts** : Le parallèle entre KYC et KYA est d'une grande lucidité sociologique et juridique : le KYC fonctionne grâce à l'état civil régalien, aux passeports biométriques et au droit pénal. Vouloir créer un KYA purement algorithmique sans fédération juridique préalable est une illusion. L'analyse de l'agent mutable à mémoire épisodique (remettant en cause l'identité par empreinte SHA-256 du code source) est visionnaire.
- **Insuffisances et faiblesses** : L'inventaire du Tableau 18.1 (9 chantiers dans 6 organisations, 0 texte ratifié) dresse un constat d'impuissance sans proposer de patron de fédération bilatérale transitoire pour les institutions financières.

### 3.8 Ch. 19 (pp. 210–222) : Taxonomie des attaques et la Triade Létale
- **Points forts** : La typologie des attaques agentiques (ATK-01 Confused Deputy, ATK-02 Rug-pull MCP, ATK-03 EchoLeak CVE-2025-32711) est parfaitement conforme aux référentiels MITRE ATLAS et OWASP Top 10 for Agentic AI 2026. L'explication de l'attaque temporelle par *rug-pull* sur un serveur d'outils MCP est remarquable.
- **Insuffisances et faiblesses** : L'orientation vers des parades cognitives (guardrails de prompt) pour contrer la triade létale de Willison est une erreur de sécurité majeure. L'injection indirecte étant indécidable au niveau du LLM, seule une rupture physique ou cryptographique des flux au niveau du moteur d'exécution offre une garantie formelle (DEF-L2-08).

### 3.9 Ch. 20 (pp. 222–236) : Boucle défensive, révocation et Agentic SOC
- **Points forts** : La mise en lumière de l'asymétrie fondamentale entre émission et révocation est magistrale. L'historique des échecs des CRL et d'OCSP (RFC 5280, RFC 6960) illustre la difficulté intrinsèque d'une révocation distribuée synchrone.
- **Insuffisances et faiblesses** : Le constat de l'impasse de l'Agentic SOC (recours à des comptes de service hautement privilégiés contournant PIM/TAP) n'est assorti d'aucun patron de remédiation déterministe (DEF-L2-09).

### 3.10 Ch. 21 (pp. 236–252) : L'horloge post-quantique et les standards NIST
- **Points forts** : Rigueur chronologique exemplaire dissociant la ratification définitive des algorithmes NIST (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA au 13 août 2024) du caractère préliminaire du calendrier NIST IR 8547. L'analyse démontrant que la directive canadienne ITSM.40.001 ne s'impose pas d'office aux banques privées est juridiquement irréprochable.
- **Insuffisances et faiblesses** : Omission critique de l'impact volumétrique des signatures post-quantiques (ML-DSA) sur les micro-échanges agentiques à haute fréquence et absence de prescriptions sur les conteneurs hybrides composites (DEF-L2-10).

### 3.11 Ch. 22 partiel (pp. 252–255) : Articulation avec l'orchestration déterministe
- **Points forts** : L'introduction de la taxonomie OO1-OO4 de la TU Munich (Rinderle-Ma et Mangler, 30 juin 2026) articule avec une grande netteté la frontière entre la couche d'identité du Livre II et la couche de contrôle d'exécution du Livre III.
- **Insuffisances et faiblesses** : Le statut de préprint non revu par les pairs de cette taxonomie doit être rappelé avec force pour éviter de lui prêter une valeur normative équivalente à une norme ISO/IEEE.

---

## 4. Synthèse bibliographique et conformité à l'état de l'art (2024–2026)

Le tableau ci-dessous confronte systématiquement l'ensemble des références mobilisées dans le Livre II aux textes normatifs et scientifiques en vigueur :

| Référence / Standard | Statut officiel (2024–2026) | Évaluation critique dans le Compendium | Verdict Niveau 1 (Arbitrage RSA) |
|---|---|---|---|
| **RFC 6749 & RFC 6750 (OAuth 2.0)** | Standard IETF (Internet Standard) | Analysé sous l'angle du bearer token et du flux interactif humain. | **Biais réducteur** : Omet RFC 8705 (mTLS) et RFC 9449 (DPoP), qui éliminent le bearer token non lié. |
| **RFC 8693 (OAuth Token Exchange)** | Proposed Standard (RFC) | Jugé inapte au multi-saut (« non documenté, degré 3 »). | **Erreur factuelle et normative** : La section 4.4 spécifie le multi-saut (*Nested 'act'*), mais la §4.1 interdit formellement d'utiliser `act` pour l'autorisation. |
| **`draft-ietf-oauth-transaction-tokens`** | Internet-Draft actif (rév. -09 / -17) | Borné à un domaine de confiance unique (*« within a single trust domain »*). | **100% Conforme** : Analyse rigoureuse de la frontière administrative de propagation de contexte. |
| **RFC 7643 & 7644 (SCIM 2.0)** | Standard IETF | Absence de ressource d'agent dans la §4. | **Conforme mais partiel** : Ignore la possibilité d'extension par URI de schéma (§3.3). Draft CSA expiré le 19 avril 2026. |
| **W3C VC Data Model v2.0** | W3C Recommendation (15 mai 2025) | Cité avec exactitude quant à sa date et ses 4 propriétés obligatoires. | **Sous-estimation du schisme** : La rupture entre Data Integrity (RDF) et Enveloping (JOSE/COSE) empêche l'interopérabilité directe. |
| **W3C DID Core v1.0 & v1.1 CR** | Rec. (v1.0) / Candidate Rec. (v1.1, mars 2026) | Seule la clé `id` est impérative ; résolution hors périmètre. | **100% Conforme** : Diagnostic lucide sur la dépendance périmétrique de `did:web` (DNS/TLS). |
| **A2A v1.0.0 (Google / Linux Foundation)** | Spécification de consortium (2025-2026) | Agent Card signée via JCS (RFC 8785) et JWS (RFC 7515). | **Insuffisant** : Ne souligne pas assez l'absence de champs de fraîcheur (`exp`), la signature optionnelle (`MAY`) et l'absence de révocation. |
| **RFC 9635 (GNAP)** | Proposed Standard (RFC, octobre 2024) | Cité au 30 juillet 2026 (p. 199). | **Sous-exploité** : Représente le véritable successeur d'OAuth pour les agents asynchrones avec Proof-of-Possession. |
| **Macaroons (Birgisson et al., NDSS 2014)** | Littérature académique majeure | Totalement omis dans le Compendium. | **Omission fondamentale** : Fournit la preuve formelle de la délégation en cascade opposable sous PRF. |
| **Biscuit Tokens (Geal et al., 2021-2025)** | Standard industriel ouvert | Totalement omis dans le Compendium. | **Omission fondamentale** : Atténuation cryptographique multi-sauts avec Datalog embarqué et vérification déterministe. |
| **NIST FIPS 203, 204, 205** | FIPS officiels (13 août 2024) | ML-KEM, ML-DSA, SLH-DSA approuvés le 13 août 2024. | **100% Conforme** : Rigueur chronologique irréprochable. |
| **NIST IR 8547** | Initial Public Draft (2024) | Dépréciation 2030, retrait 2035. Non contraignant en droit privé. | **100% Conforme** : Analyse exacte du statut pré-normatif. |
| **CCCS ITSM.40.001** | Guide du gouvernement canadien (juin 2025) | Jalons 2031 (prioritaire) et 2035 (général) restreints au fédéral. | **100% Conforme** : Bonne distinction entre gouvernement fédéral et secteur financier privé. |
| **Norm Hardy (1988) — Confused Deputy** | Littérature académique historique | Cité pour illustrer l'usurpation de mandat par injection indirecte. | **100% Conforme** : Référence canonique incontestable. |
| **Simon Willison — Triade Létale** | Littérature de sécurité IA (2023-2025) | Données privées $\cap$ Contenu non fiable $\cap$ Canal de sortie. | **100% Conforme** : Formulation exacte de l'espace de vulnérabilité agentique. |
| **AgentPoison (NeurIPS 2024)** | Conférence évaluée par les pairs | Mentionné pour réfuter les défenses cognitives probabilistes. | **100% Conforme** : Valide l'impératif du cloisonnement architectural déterministe. |
| **Taxonomie OO1-OO4 (TU Munich, juin 2026)** | Preprint universitaire (Rinderle-Ma & Mangler) | Découpage des options d'orchestration agentique. | **100% Conforme** : Prudence méthodologique exemplaire quant au statut de préprint. |

---

## 5. Rapport d'arbitrage RSA (Protocole à 5 Composants)

### 5.1 Observation
- **Examen direct des sources** : Balayage complet des pages 144 à 255 de `documents/Compendium.pdf` et confrontation textuelle aux lignes 11656 à 22660 de `DOCUMENT_TEXT_MAP.md`.
- **Anomalies visuelles vérifiées sur épreuves haute définition** :
  - `page-151.png` : Troncature nette du texte sous le Tableau 12.3 (« un document » coupé net).
  - `page-152.png` et `page-153.png` : Encadrés flottants pleine largeur (« Thèse » et « EXTRACTION CONDUITE LE 30 JUILLET 2026... ») injectés au milieu exact de phrases actives.
  - `page-193.png` : Erreur matérielle dans la Figure 17.2 associant l'étiquette « Carte d'agent » à la référence `F-29` (Transaction Tokens).
- **Vérification normative** :
  - Page 198 : L'auteur concède qu'« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict ».
  - RFC 8693 §4.4 : Présence formelle des *Nested 'act' Claims* contredisant l'assertion d'absence de documentation au degré 3 de la page 197.
  - RFC 8693 §4.1 : Interdiction impérative d'utiliser la revendication `act` pour les décisions de contrôle d'accès.
  - A2A v1.0.0 : Absence complète de paramètres d'expiration temporelle (`exp`, `iat`, `nbf`) et signature optionnelle (`MAY`).
  - NIST FIPS 204 : ML-DSA-44 requiert 2 420 octets de signature, soit 38x la taille d'Ed25519 (64 octets).

### 5.2 Logic Chain (Chaîne logique de déduction)
1. Le Compendium et son plan de revue promettaient une démonstration mathématique de rupture d'opposabilité au deuxième saut ($A \to B \to C$) et suggéraient le recours au Token Exchange (RFC 8693) pour tracer le mandat.
2. L'aveu textuel de la page 198 et l'absence totale d'équations prouvent l'inexistence de toute démonstration mathématique dans l'ouvrage.
3. L'affirmation selon laquelle le multi-saut n'est pas documenté dans la RFC 8693 est fausse (RFC 8693 §4.4).
4. Néanmoins, la RFC 8693 §4.1 proscrivant l'usage de `act` pour le contrôle d'accès, le Token Exchange ne peut en aucun cas conférer d'opposabilité à une délégation multi-sauts.
5. À l'opposé, les algèbres de capabilités cryptographiques (Macaroons, Biscuit) démontrent mathématiquement qu'une chaîne de signatures asymétriques à atténuation ordonnée préserve l'opposabilité et l'imputabilité pour tout saut $n \ge 1$.
6. Par conséquent, la rupture d'opposabilité n'est pas une loi mathématique universelle, mais un défaut d'implémentation opérationnelle (usage de bearer tokens impersonnels, conversion en frontière de domaine vers des protocoles non typés, et faillite de la révocation synchrone).
7. Les trois bris typographiques majeurs aux pages 151, 152 et 153 et la coquille d'attribution de la Figure 17.2 dégradent gravement la crédibilité de l'ouvrage et imposent une recompilation immédiate du segment.

### 5.3 Caveats (Mises en garde et limites de l'audit)
- L'audit contradictoire s'est concentré sur les axes R2 (Rigueur formelle et algorithmique) et R3 (Confrontation bibliographique 2024-2026) du segment Livre 2 (pp. 144-255).
- Les mécanismes d'orchestration avancés introduits à la fin du segment (OO1-OO4, pp. 252-255) préfigurent le Livre III et n'ont été examinés que dans leur articulation avec la couche identitaire.
- Les solutions commerciales émergentes postérieures à juillet 2026 (mises à jour de Microsoft Entra Agent ID, AWS Bedrock Agentic IAM) n'étant pas régies par des RFC ouverts, leur analyse repose sur les spécifications stables disponibles au gel documentaire.

### 5.4 Conclusion d'arbitrage
Le Livre II du *Compendium* est un traité d'ingénierie et de gouvernance d'une valeur doctrinale remarquable, qui pose les bonnes questions et déconstruit salutairement les illusions de sécurité commerciale. Cependant, pour prétendre au statut de référence opposable devant les régulateurs prudentiels (BSIF, AMF) et les directions de la sécurité (CISO), le texte doit impérativement être purgé de :
- Ses **quatre défauts bloquants** : la prétention injustifiée à un théorème mathématique des deux sauts, la double erreur sur la RFC 8693 (§4.1 et §4.4), la collision d'identifiants dans la Figure 17.2, et les coupures typographiques des pages 151, 152 et 153 ;
- Ses **six défauts majeurs** : la dépendance naïve envers l'Agent Card A2A et le passeport d'agent virtuel, le schisme non profilé de W3C VC v2.0, l'omission de DPoP (RFC 9449) et GNAP (RFC 9635), le recours erroné à des filtres cognitifs contre le Confused Deputy, l'impasse d'imputabilité de l'Agentic SOC, et l'omission de la surcharge réseau post-quantique de ML-DSA.

### 5.5 Verification Method (Procédure de vérification indépendante)
Pour vérifier de manière indépendante et reproductible les constats de cette revue de Niveau 1 :
1. **Contrôle visuel des anomalies typographiques et de la Figure 17.2** :
   - Ouvrir `documents/scratch/document_pages/page-151.png` et observer la coupure sous le Tableau 12.3 (« un document » coupé net).
   - Ouvrir `documents/scratch/document_pages/page-152.png` et `page-153.png` pour constater l'insertion intrusive des encadrés pleine largeur brisant la syntaxe grammaticale.
   - Ouvrir `documents/scratch/document_pages/page-193.png` pour constater la mention `F-29, [A]` dans la boîte 3 (« Carte d'agent ») de la Figure 17.2.
2. **Contrôle textuel de l'aveu formel** :
   - Consulter la page 198 de `DOCUMENT_TEXT_MAP.md` (lignes 17098 à 17105) pour lire textuellement : *« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
3. **Contrôle normatif de la RFC 8693** :
   - Consulter la RFC 8693 §4.4 sur le dépôt de l'IETF pour vérifier la spécification des *Nested 'act' Claims*.
   - Consulter la RFC 8693 §4.1 pour vérifier l'interdiction d'utiliser `act` pour les décisions de contrôle d'accès.
4. **Contrôle post-quantique FIPS 204** :
   - Consulter le standard NIST FIPS 204 (Tableau 1 et Tableau 2) pour vérifier les dimensions de clés ($1\,312\text{ o}$) et signatures ($2\,420\text{ o}$) pour ML-DSA-44.
