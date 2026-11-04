# RAPPORT DÉFINITIF D'AUDIT D'UNITÉ (RSA NIVEAU 2 — RACINE)
# LIVRE II : « FAIRE CONFIANCE — IDENTITÉ NON HUMAINE ET DÉLÉGATION VÉRIFIABLE »

---

## 1. Titre et Métadonnées de l'audit

- **Document audité** : `documents/Compendium.pdf` (*Interopérabilité et Orchestration en Entreprise Agentique*, André-Guy Bruneau M.Sc. IT, Édition Novembre 2026, 663 pages).
- **Segment audité** : `segment_livre_2_confiance` — Livre II : *Faire confiance : Identité non humaine et délégation vérifiable* (Chapitres 12 à 21, pp. 144 à 251) et amorce de transition vers le Livre III (Chapitre 22, pp. 252 à 255).
- **Couverture du plan de revue** : Segments S14 à S23 de `REVIEW_PLAN.md` (Pages 144 à 255).
- **Rôle de l'auditeur** : Final Review Aggregator (Niveau 2 — Racine de l'arbre d'arbitrage RSA [4, 2, 1]).
- **Entrées synthétisées** :
  - Revue évoluée Niveau 1_1 : `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_2_confiance\review_l1_1.md` (synthèse contradictoire {R1, R2}).
  - Revue évoluée Niveau 1_2 : `c:\Github\EntrepriseAgentique\.agents\teamwork\group_livre_2_confiance\review_l1_2.md` (synthèse contradictoire {R3, R4}).
  - Rapports sources Niveau 0 consultés pour vérification probatoire : `handoff_1.md` à `handoff_4.md`.
  - Artefacts de référence : `DOCUMENT_TEXT_MAP.md` (lignes 11656 à 22660) et épreuves graphiques haute définition `page-144.png` à `page-255.png` dans `documents/scratch/document_pages/`.
- **Date de clôture d'audit** : 3 novembre 2026.
- **Référentiel méthodologique** : Audit contradictoire exhaustif combinant l'axe R2 (Rigueur formelle, algorithmique et théorique) et l'axe R3 (Confrontation bibliographique et état de l'art normatif 2024-2026), sous les critères de conformité prudentielle canadienne (BSIF / OSFI E-23, AMF, Loi 25 QC art. 12.1).

---

## 2. Verdict exécutif d'audit du Livre 2

Le Livre II du *Compendium* constitue la clé de voûte sécuritaire, cryptographique et réglementaire de l'ouvrage. Situé à la charnière entre l'inventaire des protocoles d'interaction (Livre I) et les mécanismes d'orchestration déterministe sous contraintes financières (Livre III), il entreprend de fonder la pile d'identité non humaine (*Machine/Agent Identity*) et de délégation vérifiable indispensable à l'opposabilité juridique des agents autonomes.

### 2.1 Contribution fondamentale annoncée vs Réalité technique et formelle
L'auteur pose un diagnostic salutaire et d'une lucidité remarquable : le déploiement d'agents autonomes en entreprise régulée est impossible sans résoudre le triple défi de la non-répudiation des actes machines, de la traçabilité des chaînes de délégation et de la résistance post-quantique. La posture épistémique de l'auteur — matérialisée par la catégorisation stricte des sources en faits vérifiés [A], faits négatifs établis [B], et degrés d'absence 1 à 3 [C] — constitue un rempart méthodologique exemplaire contre le sensationnalisme technologique et le marketing des éditeurs de logiciels.

Cependant, l'audit approfondi de Niveau 2 met en évidence un **décalage structurel profond entre l'ambition théorique annoncée et la démonstration formelle effective du texte** :
1. **La falsification formelle du « problème des deux sauts » (Ch. 17)** : Le plan directeur annonçait une démonstration mathématique prouvant la rupture inéluctable d'opposabilité dès le second saut de délégation ($A \to B \to C$). Or, le manuscrit ne contient aucun formalisme logique, aucune dérivation mathématique et aucun calcul de probabilité. L'auteur concède lui-même à la page 198 qu'« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict ». Pire, le traitement de la RFC 8693 (*OAuth Token Exchange*) cumule une erreur factuelle (ignorer la spécification des *Nested 'act' claims* à la section 4.4) et une impasse normative (la section 4.1 interdisant formellement l'usage de la revendication `act` pour les décisions de contrôle d'accès). À l'inverse de la thèse du texte, la littérature cryptographique (Macaroons sous PRF, Biscuit sous Datalog) démontre que l'opposabilité transitive est mathématiquement préservable pour tout saut $n \ge 1$ sous le modèle d'infalsifiabilité existentielle (EUF-CMA).
2. **La fragilité critique de l'Agent Card A2A et l'illusion du « Passeport d'agent » (Ch. 15-16)** : Présentée comme le socle d'un « passeport d'agent » conditionnant l'entrée dans le maillage (« Rien n'entre au maillage sans lui », p. 180), l'Agent Card (A2A v1.0.0 de Google / Linux Foundation) est en réalité un simple descripteur fonctionnel d'outils dépourvu de paramètres d'expiration (`iat`, `exp`, `nbf`), sans magasin de clés de confiance prescrit, sans protocole de révocation et dont la signature n'est qu'optionnelle (`MAY`). Ériger une exigence d'exploitation bloquante sur un objet virtuel non standardisé crée une aporie opérationnelle immédiate.
3. **L'angle mort physique et réseau de la cryptographie post-quantique (Ch. 21)** : L'auteur traite avec rigueur l'approbation des normes NIST FIPS 203 et 204 au 13 août 2024, mais omet totalement la norme finale FIPS 205 (SLH-DSA). Surtout, le texte qualifie de « spéculatif sans mesure » le surcoût volumétrique des signatures post-quantiques. Or, les tailles normatives de ML-DSA (2 420 à 4 627 octets, soit 38x à 75x la taille d'Ed25519) et de SLH-DSA (7 856 à 29 792 octets) dépassent instantanément la MTU Ethernet standard (1 500 octets) et saturent les plafonds par défaut des en-têtes HTTP (8 Ko), déclenchant des erreurs fatales `HTTP 431 Request Header Fields Too Large` sur les passerelles d'API d'entreprise.
4. **La dislocation matérielle de la composition typographique (Ch. 12, 13, 16, 21)** : L'inspection directe des épreuves de rendu haute résolution révèle des défaillances de compilation destructives : dislocation complète du Tableau 16.3 (p. 188), collision d'un encadré flottant de 16 lignes fracturant la syntaxe d'une phrase entre les pages 242 et 243, inversion textuelle dans le Tableau 21.4 (p. 248), troncature nette en fin de page 151, et injection d'encadrés pleine largeur au milieu de groupes nominaux (pp. 152, 153).

### 2.2 Diagnostic d'opposabilité juridique et cryptographique
Sur le plan du droit financier québécois et canadien :
- **Loi 25 (Québec, art. 12.1)** : L'absence de prise en compte des protocoles de divulgation sélective (*Selective Disclosure* - SD-JWT VC RFC 9542 et W3C BBS Cryptosuite v1.0) dans le chapitre 13 prive l'architecture de la capacité de satisfaire au principe de minimisation des renseignements personnels.
- **Lignes directrices BSIF / OSFI E-21 et E-23** : Les défaillances opérationnelles documentées dans l'Agentic SOC (Ch. 20) — notamment le contournement des contrôles d'accès temporaires (PIM / TAP) par l'attribution de comptes de service permanents à privilèges élevés dans Microsoft Defender — violent directement les exigences de saine gestion du risque opérationnel et d'imputabilité individuelle des transactions bancaires.
- **Directive CCCS ITSM.40.001** : L'auteur établit avec exactitude que ce guide fédéral ne s'applique pas d'office au secteur financier sous juridiction provinciale ou fédérale privée, mais la présentation disloquée du Tableau 21.4 entretient une ambiguïté qu'il convient de dissiper formellement.

---

## 3. Matrice unifiée et exhaustive des défauts (DEF-L2-01 à DEF-L2-25)

Les défauts identifiés à travers l'arbre RSA sont classés selon les trois niveaux de sévérité stricts de la méthode :
- **Bloquant** : Erreur formelle, théorique, normative ou vice de composition détruisant la cohérence ou la validité d'une démonstration majeure.
- **Majeur** : Faille d'architecture, omission technologique critique, lacune algorithmique ou angle mort de sécurité affaiblissant l'ouvrage sans invalider l'ensemble du corpus.
- **Mineur** : Incohérence locale, ambiguïté de formulation, défaillance graphique mineure ou coquille typographique.

### 3.1 Tableau synoptique de la matrice unifiée

| ID Normalisé | Sévérité | Chapitre | Page(s) | Nature résumée du défaut | Statut RSA |
|---|---|---|---|---|---|
| **DEF-L2-01** | **Bloquant** | Ch. 17 | 196–200 | Falsification formelle du théorème des deux sauts, aveu p. 198, double erreur sur RFC 8693 (§4.1/§4.4) et assertion erronée sur Biscuit | Unifié {L1_1, L1_2} |
| **DEF-L2-02** | **Bloquant** | Ch. 17 | 193 | Collision d'identifiants dans la Figure 17.2 (`F-29` attribué à tort à l'Agent Card) | Unifié {L1_1, L1_2} |
| **DEF-L2-03** | **Bloquant** | Ch. 16 | 188 | Dislocation destructive du Tableau 16.3 (colonne vide, texte de description glissé dans la colonne « Tri ») | Retenu {L1_2} |
| **DEF-L2-04** | **Bloquant** | Ch. 21 | 242–243 | Collision d'un encadré flottant de 16 lignes fracturant la syntaxe d'une phrase entre `tri :` (p. 242) et `fait PROJETÉ` (p. 243) | Retenu {L1_2} |
| **DEF-L2-05** | **Bloquant** | Ch. 12 | 151 | Troncature textuelle critique sous le Tableau 12.3 (« un document » coupé net sans ponctuation) | Unifié {L1_1, L1_2} |
| **DEF-L2-06** | **Bloquant** | Ch. 13 | 152–153 | Débordement d'encadrés pleine largeur (« Thèse » et « EXTRACTION ») fracturant des groupes syntaxiques actifs | Unifié {L1_1, L1_2} |
| **DEF-L2-07** | **Majeur** | Ch. 15–16 | 167–188 | Faille structurelle de l'Agent Card A2A v1.0.0 (absence de fraîcheur et de révocation) et chimère du « Passeport d'agent » | Unifié {L1_1, L1_2} |
| **DEF-L2-08** | **Majeur** | Ch. 15, 20 | 170, 223–224 | Paradoxe normatif d'interdiction `MUST NOT` sans mécanisme de vérification d'état dans A2A v1.0.0 | Retenu {L1_2} |
| **DEF-L2-09** | **Majeur** | Ch. 13 | 153–157 | Schisme d'interopérabilité au sein de W3C VC v2.0 et omission des preuves à divulgation sélective (SD-JWT VC / BBS+) | Unifié {L1_1, L1_2} |
| **DEF-L2-10** | **Majeur** | Ch. 12 | 144–150 | Biais réducteur sur OAuth 2.0 (omission de DPoP RFC 9449 et mTLS RFC 8705) et caducité du draft SCIM CSA | Unifié {L1_1, L1_2} |
| **DEF-L2-11** | **Majeur** | Ch. 19 | 210–222 | Méconnaissance de la sécurité par capabilités (Hardy 1988) et illusion du confinement cognitif face à la Triade Létale | Unifié {L1_1, L1_2} |
| **DEF-L2-12** | **Majeur** | Ch. 20 | 222–225 | Absence de condensat d'intégrité et risque de *Rug-Pull* / *Tool-Squatting* dans MCP (`tools/list_changed`) | Retenu {L1_2} |
| **DEF-L2-13** | **Majeur** | Ch. 20 | 230–235 | Régression du principe de moindre privilège (PoLP) et rupture d'imputabilité PIM/TAP dans l'Agentic SOC | Unifié {L1_1, L1_2} |
| **DEF-L2-14** | **Majeur** | Ch. 20 | 228–235 | Vacuité algorithmique de la boucle défensive du SOC (absence de métriques sur graphes d'exécution et protocole d'expulsion) | Retenu {L1_2} |
| **DEF-L2-15** | **Majeur** | Ch. 18 | 201–210 | Absence de spécification procédurale d'un protocole déterministe d'admission KYA en cinq phases | Retenu {L1_2} |
| **DEF-L2-16** | **Majeur** | Ch. 21 | 236–248 | Omission de FIPS 205 (SLH-DSA), cécité sur la fragmentation MTU (1500o) et saturation d'en-têtes HTTP 431 | Unifié {L1_1, L1_2} |
| **DEF-L2-17** | **Majeur** | Ch. 21 | 242–245 | Verrou normatif de l'absence d'identifiants IANA pour les algorithmes PQC dans JOSE (RFC 7515) et COSE (RFC 9052) | Retenu {L1_2} |
| **DEF-L2-18** | **Majeur** | Ch. 21 | 248 | Fracture et inversion de colonnes dans le Tableau 21.4 (ITSM.40.001) avec colonne 3 déserte sur les données | Retenu {L1_2} |
| **DEF-L2-19** | **Mineur** | Ch. 12 | 147 | Troncature graphique dans la colonne gauche de la Figure 12.4 (« pour » coupé net) | Retenu {L1_2} |
| **DEF-L2-20** | **Mineur** | Ch. 12 | 148 | Glitch rédactionnel et contradiction interne sur la date de publication (absence affirmée puis date collée) | Retenu {L1_1} |
| **DEF-L2-21** | **Mineur** | Ch. 14 | 162–164 | Discordance typologique et saut d'indexation : Figure 14.1 formatée en tableau vs Tableau 14.2 | Retenu {L1_2} |
| **DEF-L2-22** | **Mineur** | Ch. 14, 22 | 166, 253 | Flottement terminologique entre les échelles d'autonomie (4 paliers, 6 niveaux) et la taxonomie OO1–OO4 | Unifié {L1_1, L1_2} |
| **DEF-L2-23** | **Mineur** | Ch. 20 | 227 | Ponctuation manquante fusionnant deux phrases distinctes à propos de la RFC 7662 | Retenu {L1_2} |
| **DEF-L2-24** | **Mineur** | Ch. 19, 20 | 212, 222, 226 | Maintien de mentions de balayage gelé et « rejeu non fait » sur la révision MCP du 28 juillet 2026 et draft AGNTCY | Retenu {L1_2} |
| **DEF-L2-25** | **Mineur** | Ch. 21 | 248–249 | Ambiguïté de portée sur l'application de la directive CCCS ITSM.40.001 aux banques sous égide BSIF/AMF | Retenu {L1_1} |

---

### 3.2 Fiches détaillées des 25 défauts

#### DEF-L2-01 [Bloquant / Erreur formelle, théorique et normative]
- **Localisation** : Chapitre 17, Section 17.6 (« Le problème des deux sauts »), pp. 196 à 200.
- **Citations textuelles exactes** :
  - Page 197 : *« Ce que ce texte prévoit ou tait de la composition de plusieurs délégations successives n’est pas documenté par le socle — degré 3. Il ne s’ensuit ni qu’une telle composition soit prévue, ni qu’elle ne le soit pas. »*
  - Page 198 : *« Le terme "limites démontrées" mérite d'être borné avant d'écrire quoi que ce soit : aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
  - Page 198 (Tableau 17.2) : *« La composition sur plus d'un saut : absence de documentation, degré 3 »*.
  - Page 199 : *« L’attribut act exprime la chaîne d’acteurs ; il ne démontre pas l’opposabilité de chaque saut auprès d’un tiers indépendant [...] les acteurs intermédiaires sont informational only »*.
  - Page 200 : *« Macaroons et Biscuit atténuent une portée, ils ne portent pas l'identité de chaque maillon que le § 17.6.1 déclare perdue »*.
- **Diagnostic causal approfondi** :
  1. *Absence totale de démonstration mathématique* : Le plan de révision annonçait un « théorème des deux sauts démontrant mathématiquement la rupture d'opposabilité dans les délégations récursives $A \to B \to C$ ». Or, le texte n'articule aucun formalisme mathématique, aucune logique d'autorisation (ABLP, SecPAL, logique BAN) et aucun calcul stochastique. L'auteur concède lui-même ce vide à la page 198.
  2. *Erreur factuelle sur la RFC 8693 §4.4* : L'auteur qualifie la composition sur plus d'un saut d'« absence de documentation, degré 3 » dans le standard IETF Token Exchange. C'est faux : la section 4.4 de la RFC 8693 spécifie expressément les *Nested 'act' Claims*, définissant le schéma JSON récursif permettant à une chaîne d'acteurs de propager la délégation sur $N$ sauts. L'auteur a confondu une lacune de sa propre grille d'extraction avec une carence de la norme internationale.
  3. *Incompatibilité normative de la RFC 8693 §4.1 pour l'opposabilité* : Bien que la RFC 8693 permette la syntaxe multi-sauts, sa clause normative §4.1 détruit toute prétention d'opposabilité en disposant expressément : *« The "act" (actor) claim [...] is informational only and MUST NOT be used for access control decisions »*. Le destinataire final $C$ ou le serveur de ressources a l'interdiction formelle de fonder son autorisation sur cette chaîne.
  4. *Fausseté de l'hypothèse de rupture intrinsèque à $N=2$* : La rupture d'opposabilité n'est pas une loi mathématique universelle de la délégation. Dans les algèbres de capabilités cryptographiques (Abadi et al., *A Calculus for Access Control in Distributed Systems* ; Miller et al.), une délégation est une réduction monotone de droits transitivement signée.
  5. *Erreur factuelle sur Biscuit (p. 200)* : L'affirmation selon laquelle *Biscuit* « ne porte pas l'identité de chaque maillon » est factuellement fausse. Dans Biscuit, chaque bloc d'atténuation successif est signé cryptographiquement par le délégataire sortant et peut incorporer des faits Datalog liant sans ambiguïté l'identité et la clé publique du maillon délégué suivant :
     $$\text{check if actor}(\text{"agent\_C"}), \text{operation}(\text{"read"})$$
- **Contre-exemple formel et Correctif rigoureux** :
  Réfuter l'affirmation d'impossibilité structurelle. Énoncer que l'opposabilité se conserve mathématiquement par transitivité sous le modèle standard d'infalsifiabilité existentielle face aux attaques à message choisi (EUF-CMA).
  *Démonstration* : Soit une chaîne de délégation à $n$ sauts $\Delta_n = (D_1, \dots, D_n)$ liant le mandant $A_0$ à l'agent final $A_n$ :
  $$D_k = \text{Sign}_{SK_{k-1}}(A_k \parallel \text{Scope}_k \parallel T_k \parallel H(D_{k-1})) \quad \text{avec} \quad \text{Scope}_k \subseteq \text{Scope}_{k-1}$$
  Un vérificateur indépendant $V$ confronté à $\Delta_n$ vérifie par induction :
  $$\forall k \in [1, n], \quad \text{Verify}_{PK_{k-1}}(D_k) = \text{True} \quad \wedge \quad \text{Scope}_k \subseteq \text{Scope}_{k-1} \quad \wedge \quad t \in \bigcap_{i=1}^n T_i$$
  Sous l'hypothèse de sécurité de la signature sous-jacente, l'avantage de forger un maillon frauduleux est borné par :
  $$\text{Adv}_{\text{Forge}}(\Delta_n) \le \sum_{k=1}^n \text{Adv}_{\text{EUF-CMA}}(A_{k-1}) \le n \cdot \text{negl}(\lambda)$$
  **Correctif** : Requalifier le problème des deux sauts en « défi d'impédance protocolaire et de révocation en cascade en entreprise ». Remplacer la fausse assertion d'absence sur la RFC 8693 par l'analyse de sa section 4.4, tout en démontrant pourquoi la clause §4.1 invalide son usage en contrôle d'accès strict. Citer les architectures Biscuit / Macaroons comme solutions formellement prouvées.

#### DEF-L2-02 [Bloquant / Erreur matérielle d'attribution et collision d'identifiants]
- **Localisation** : Chapitre 17, Page 193 (Figure 17.2, vérifiée sur `page-193.png`).
- **Citation textuelle exacte** :
  Figure 17.2, Boîte 3 : *« 3 Carte d'agent | Porte l'identité, non la chaîne. | F-29, [A] »*.
- **Diagnostic causal approfondi** :
  Collision directe d'identifiants de source. Dans tout l'ouvrage (pp. 147, 151, 192, 198), la fiche `F-29` désigne exclusivement le projet IETF OAuth sur les *Transaction Tokens* (`draft-ietf-oauth-transaction-tokens`, révision -09 du 6 juillet 2026, propagation de contexte). La Carte d'agent (Agent Card A2A de Google / Linux Foundation) est indexée sous les fiches `F-01` à `F-07`. L'attribution de `F-29` à la boîte « Carte d'agent » est une coquille matérielle d'auteur qui désoriente le lecteur et fausse l'index de traçabilité.
- **Correctif formel** :
  Modifier la boîte 3 de la Figure 17.2 : soit remplacer l'intitulé par « Jeton de transaction (propagation de contexte) » en conservant `F-29, [A]`, soit remplacer la référence par `F-04 / F-07, [A]` en conservant l'intitulé « Carte d'agent ».

#### DEF-L2-03 [Bloquant / Bris de composition typographique critique]
- **Localisation** : Chapitre 16, Section 16.4, Page 188 (`page-188.png`), Tableau 16.3 (« Trois scénarios de normalisation du passeport d’agent... »).
- **Citation textuelle exacte** :
  Dans la rangée `1 — extension d'un texte de l'IETF` :
  - Colonne « Tri » : *« s de groupe de travail, aucun publié en RFC, aucune date annoncée (F-85)... »*
  - Colonne « Ce sur quoi il s'appuie » : *[Cellule entièrement VIDE — vide de blanc pur]*
- **Diagnostic causal approfondi** :
  Une erreur d'alignement dans le moteur de composition LaTeX/typographique a supprimé la valeur de la colonne « Tri » (qui devait porter la mention `PROJETÉ`), amputé les premiers mots de la description de la colonne 3 (*« 7 Internet-Draft »* tronqué en *« s »*), et injecté tout le texte descriptif de la colonne 3 à l'intérieur de la colonne « Tri ». La colonne 3 se retrouve totalement déserte, détruisant la cohérence de la table.
- **Correctif requis** :
  Restaurer la disposition tabulaire rigoureuse :
  - Colonne 1 (Scénario) : `1 — extension d’un texte de l’IETF`
  - Colonne 2 (Tri) : `PROJETÉ`
  - Colonne 3 (Ce sur quoi il s’appuie) : `7 Internet-Drafts de groupe de travail, aucun publié en RFC, aucune date annoncée (F-85) — huit au 23 octobre 2026, dont un adopté sur les agents d’IA ; intermédiaires d’IA rangés parmi les charges déléguées (F-86) ; appel de dernière relecture sur la propagation de contexte (F-29)`
  - Colonne 4 (Ce qui le réfuterait) : `l’adoption d’un document couvrant l’assemblage des quatre pièces, ou au contraire l’expiration de la série sans reprise`

#### DEF-L2-04 [Bloquant / Bris de composition typographique critique]
- **Localisation** : Chapitre 21, Section 21.4, pp. 242-243 (`page-242.png` et `page-243.png`).
- **Citation textuelle exacte** :
  - p. 242 (bas) : *« Le socle ne documente aucune date pour la révision annoncée — degré 3 ; tri : »*
  - [Insertion brutale d'un encadré de 16 lignes en gras : *« L’invariant n’est pas employé nu, et sa forme se cite exactement [...] pour n’en tirer aucun »*]
  - p. 243 (haut) : *« fait PROJETÉ — intention publiée sans échéance relevée. Un statut final ne vaut pas texte figé : le paramètre vers lequel on migre bouge lui aussi... »*
- **Diagnostic causal approfondi** :
  Le bloc de mise en relief de l'invariant à quatre termes s'est intercalé au milieu de la séquence grammaticale :
  `...degré 3 ; tri : [ENCADRÉ] fait PROJETÉ — intention publiée...`.
  Le mot-clé `tri :` se retrouve orphelin en pied de page 242, et son prédicat syntaxique `fait PROJETÉ` est repoussé au sommet de la page 243 après 16 lignes de texte étranger. Cette rupture détruit la structure logique du paragraphe d'analyse des avis d'errata NIST.
- **Correctif requis** :
  Rattacher l'encadré flottant comme élément hors-texte (marge ou encadré en tête de section) et rétablir la phrase continue dans le flux principal :
  *« Le socle ne documente aucune date pour la révision annoncée — degré 3 ; tri : PROJETÉ — intention publiée sans échéance relevée. Un statut final ne vaut pas texte figé... »*

#### DEF-L2-05 [Bloquant / Bris de composition typographique critique]
- **Localisation** : Chapitre 12, Page 151 (sous le Tableau 12.3, vérifié sur `page-151.png` et `DOCUMENT_TEXT_MAP.md` lignes 12720–12734).
- **Citation textuelle exacte** :
  Page 151 : *« ...rien de son texte n’est établi. de groupe de travail en appel de dernière relecture propose un mécanisme de propagation du contexte (Vol. III F-29)... »* puis *« L’ordre des faits est donc celui-ci, et il est daté du 21 juillet 2026 : un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document »* [interruption brutale, suivi du saut de paragraphe] *« Ce qui manque à cet inventaire n’est pas une pièce... »*.
- **Diagnostic causal approfondi** :
  Un débordement d'environnement flottant lors de la compilation a fragmenté le texte en deux endroits de la page 151 :
  1. La fin de la phrase sur OIDC s'interrompt et enchaîne directement sans majuscule ni transition sur un fragment orphelin (« de groupe de travail en appel... »).
  2. La phrase de conclusion de la section sous le Tableau 12.3 est tronquée net après le mot « document », privant le lecteur de la formulation de synthèse du chapitre 12.
- **Correctif formel** :
  Ajuster les ressorts verticaux du gabarit de mise en page autour du Tableau 12.3 et rétablir le segment textuel complet :
  *« ...un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document de groupe de travail en appel de dernière relecture propose un mécanisme de propagation du contexte (Vol. III F-29) ; et une spécification de laboratoire demeure un document d'orientation informel sans portée normative. »*

#### DEF-L2-06 [Bloquant / Bris de composition typographique critique]
- **Localisation** : Chapitre 13, Pages 152 et 153 (vérifié sur `page-152.png` et `page-153.png`).
- **Citations textuelles exactes** :
  - Page 152 : *« ...le Vol. I, qui porte le terme au titre d’une »* [Encart Thèse intercalé] *« section, ne le définit ni ne le réemploie dans le corps de celle-ci... »*.
  - Page 153 : *« La Recommandation en admet deux familles, non une : la preuve »* [Encart pleine largeur d'extraction intercalé] *« incorporée, portée par la propriété proof... »*.
- **Diagnostic causal approfondi** :
  Les blocs flottants « Thèse » et « EXTRACTION CONDUITE LE 30 JUILLET 2026 » ne disposent pas de séparateurs de paragraphe stricts (`\par` ou ancrage inline `[H]`). Le compilateur a injecté les blocs au milieu exact de liaisons grammaticales (entre l'article indéfini « une » et le substantif « section » à la p. 152 ; entre le substantif « preuve » et son adjectif « incorporée » à la p. 153).
- **Correctif formel** :
  Forcer les ruptures de paragraphes en amont et en aval de chaque encadré méthodologique et repositionner l'ancrage des boîtes d'extraction pour préserver l'intégrité de la syntaxe linéaire.

#### DEF-L2-07 [Majeur / Architecture de sécurité & Chimère normative]
- **Localisation** : Chapitres 15 et 16, Pages 167 à 188 (§15.1, §15.2, §16.1, Figure 15.1, Tableau 15.1).
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
  - *Couche Découverte* : l'Agent Card A2A cantonnée au rôle d'annuaire technique d'outils ;
  - *Couche Authentification* : un jeton d'instance éphémère lié cryptographiquement par clé asymétrique (SPIFFE SVID ou certificat mTLS RFC 8705) ;
  - *Couche Autorisation / Mandat* : une attestation de mandat éphémère à divulgation sélective (SD-JWT VC ou token Biscuit) portant explicitement l'identité juridique du mandant et une durée de vie strictement bornée ($\Delta t \le 1\text{ h}$).

#### DEF-L2-08 [Majeur / Contradiction normative interne A2A]
- **Localisation** : Chapitre 15, Section 15.1.3 et Chapitre 20, Section 20.2, pp. 170, 223–224.
- **Citations textuelles exactes** :
  - Page 224 : *« l’interdiction d’employer une clé expirée ou révoquée y est pourtant posée au niveau normatif le plus fort [MUST NOT], sans aucun moyen permettant au client de l’établir (F-07, [A]) »*.
  - Page 170 : *« Les cartes MAY être signées ; les clients SHOULD vérifier au moins une signature (F-04, [A]) »*.
- **Diagnostic causal approfondi** :
  Le standard A2A v1.0.0 crée une impossibilité juridique et technique : il impose une interdiction absolue (`MUST NOT`) d'utiliser une clé expirée ou révoquée, tout en omettant de définir le moindre point de terminaison ou protocole de contrôle d'état (absence de liste de révocation, de point d'introspection ou d'annuaire OCSP). L'apposition même de la signature étant purement facultative (`MAY`), la chaîne d'opposabilité s'effondre en pratique.
- **Correctif requis** :
  Formuler une exigence d'extension d'architecture imposant l'adjonction d'un mécanisme de vérification d'état cryptographique (ex. profil W3C Bitstring Status List v1.0 ou RFC 7662) pour conditionner l'admission d'une Agent Card dans un domaine financier.

#### DEF-L2-09 [Majeur / Interopérabilité décentralisée & Protection des données]
- **Localisation** : Chapitre 13, Pages 153 à 157 (§13.2, Tableau 13.1).
- **Citation textuelle exacte** :
  Page 153 : *« Deux familles de preuve pour un même modèle de données signifient que deux implémentations conformes peuvent être mutuellement illisibles : c'est, transposé au niveau du justificatif, exactement le constat de conformité ≠ interopérabilité... »*.
- **Diagnostic causal approfondi** :
  La Recommandation W3C VC v2.0 (15 mai 2025) institutionnalise deux formats mutuellement incompatibles :
  - *Data Integrity Proofs* en JSON-LD (canonicalisation de graphes RDF RFC 8785 / RDFC-2022 et cryptosuites `eddsa-rdfc-2022`) ;
  - *Enveloping Proofs* en jetons plats sérialisés (IETF JOSE/COSE / SD-JWT).
  En outre, le Compendium omet d'analyser l'apport critique des spécifications de divulgation sélective (*Selective Disclosure* - SD-JWT VC RFC 9542 et W3C BBS Cryptosuite v1.0). Sans ces mécanismes, un agent ne peut pas restreindre la preuve de son mandat aux seules données strictement nécessaires à l'acte, violant frontalement le principe de minimisation de l'article 12.1 de la Loi 25 québécoise.
- **Correctif formel** :
  Spécifier une exigence de profilage d'application (*Application Profile*) imposant le format SD-JWT-VC (RFC 9542) pour les échanges inter-domaines et documenter formellement l'impossibilité d'une interopérabilité décentralisée universelle sans restriction de profil.

#### DEF-L2-10 [Majeur / Biais d'analyse protocolaire IAM]
- **Localisation** : Chapitre 12, Pages 144 à 150 (§12.1 à §12.3).
- **Citation textuelle exacte** :
  Page 144 : *« ...le jeton porteur (bearer token) n’est lié ni à l’appelant, ni à un appareil, ni à une session — quiconque le détient est l’intégration. »*
- **Diagnostic causal approfondi** :
  Le réquisitoire contre OAuth 2.0 repose sur un biais réducteur : assimiler l'architecture OAuth au seul profil de jeton porteur impersonnel (RFC 6750). L'auteur passe sous silence les standards ratifiés de *Proof-of-Possession* de l'IETF :
  - RFC 8705 (2020) : liaison mTLS de jetons d'accès aux certificats clients ;
  - RFC 9449 (2023) : DPoP (*Demonstrating Proof-of-Possession*), qui neutralise le vol et le rejeu de jetons en liant cryptographiquement chaque requête HTTP à une paire de clés asymétriques éphémères générées par le client.
  Toutefois, même sous DPoP, OAuth 2.0 reste inadapté aux agents autonomes car il ne modélise pas la subjectivité juridique d'un mandataire autonome. Sur le plan de SCIM 2.0 (RFC 7643/7644), le projet de registre de la Cloud Security Alliance reposait sur `draft-abbey-scim-agent-extension-00`, devenu caduc le 19 avril 2026.
- **Correctif formel** :
  Intégrer RFC 9449 (DPoP) comme contre-mesure d'ingénierie immédiate face au rejeu de jetons, et démontrer que l'alternative architecturale d'avenir réside dans la RFC 9635 (GNAP - *Grant Negotiation and Authorization Protocol*, octobre 2024), conçue dès l'origine pour les interactions asynchrones sans navigateur avec négociation dynamique de droits cryptographiquement liés.

#### DEF-L2-11 [Majeur / Sécurité théorique & Ingénierie des privilèges]
- **Localisation** : Chapitre 19, Pages 210 à 222 (§19.2, §19.3) et Chapitre 20 (§20.1).
- **Citation textuelle exacte** :
  Page 214 : *« Le problème du confused deputy identifié par Hardy en 1988 resurgit avec les agents : l'agent dispose de privilèges légitimes sur des outils, mais son planificateur interne est manipulé par une injection indirecte provenant d'un contenu externe non fiable »*.
  Page 216 : *« Norm Hardy (1988), The Confused Deputy (or why capabilities might have been invented)... nomme le patron dont toute cette taxonomie est une réinstanciation... »*.
- **Diagnostic causal approfondi** :
  1. *Méconnaissance du modèle de capabilités* : L'auteur cite l'article historique de Hardy (1988) comme un argument d'autorité terminologique, sans intégrer la thèse technique centrale de l'article : la faille du *Confused Deputy* provient structurellement de la dissociation entre la désignation de la ressource et l'autorité d'y accéder (inhérente aux listes de contrôle d'accès ACL et aux rôles RBAC). En restant cantonné au paradigme de l'identité et des listes de privilèges, le Compendium ne résout pas la confusion de délégué pour les agents autonomes.
  2. *Illusion du confinement cognitif probabiliste* : Le texte formalise avec exactitude la « triade létale » de Simon Willison :
     $$(\text{AccèsDonnéesPrivées}) \wedge (\text{IngestionContenuNonFiable}) \wedge (\text{CanalExfiltration}) \implies \text{Compromission}$$
     Cependant, les sections 19.3 et 20.1 suggèrent des remèdes probabilistes (filtrage de prompts par guardrails LLM, classificateurs d'intention). Comme l'ont démontré Simon Willison, Perez et al., et les travaux sur AgentPoison (NeurIPS 2024), **aucun filtre textuel sémantique ne peut offrir de garantie mathématique contre l'injection indirecte**. Traiter une défaillance de contrôle d'accès par un modèle stochastique est une hérésie de sécurité.
- **Correctif formel** :
  Substituer la perspective ACL par le paradigme des **Object-Capabilities** : une référence d'outil doit être un triplet cryptographique indivisible :
  $$\mathcal{C} = \langle \text{URI}_{\text{outil}}, \text{AttenuatedPermissions}, \text{ProofOfPossession} \rangle$$
  Imposer le principe du *cloisonnement architectural déterministe* : briser physiquement la triade au niveau du plan d'exécution :
  - *Règle de révocation dynamique de canal* : dès lors qu'un agent ingère un contenu externe non vérifié (courriel, scraping, document non signé), la plateforme d'orchestration révoque immédiatement tous ses canaux réseau sortants non déterministes.
  - *Architecture Dual-Agent avec sas typé* : l'agent d'ingestion non fiable est cantonné dans une sandbox hermétique ; l'agent exécuteur privilégié ne reçoit que des structures de données strictement typées et validées par un schéma déterministe (Protobuf / JSON Schema strict).

#### DEF-L2-12 [Majeur / Sécurité des protocoles d'outils / MCP]
- **Localisation** : Chapitre 20, Sections 20.1 et 20.3, pp. 222 à 225.
- **Citations textuelles exactes** :
  - Page 222 : *« l’énumération du type de données correspondant compte huit champs, dont aucun n’exprime une version, une empreinte cryptographique ou une signature (F-52, [B]) »*.
  - Page 223 : *« le retournement [...] exploite le fait que la décision d’invocation s’appuie sur un objet que le protocole autorise à changer après l’octroi de la confiance, sans prescrire de le relier à ce qui avait été consenti »*.
- **Diagnostic causal approfondi** :
  Le protocole MCP (révision 2025-11-25) autorise un serveur d'outils à notifier dynamiquement une modification de sa liste de primitives via `notifications/tools/list_changed` sans exiger le moindre condensat cryptographique (`tool_digest`) ni signature. Un outil consenti au démarrage peut être substitué par une charge malveillante (*tool-squatting / rug-pull*) sans rupture protocolaire.
- **Correctif requis** :
  Définir une extension d'intégrité liant chaque primitive d'outil à une empreinte canonique immuable :
  $$\mathcal{H}_{\text{tool}} = \text{SHA-256}(\text{JCS}(\text{name} \parallel \text{description} \parallel \text{inputSchema}))$$
  Cette empreinte doit être scellée dans le jeton d'autorisation de l'agent appelant à l'instant de consentement.

#### DEF-L2-13 [Majeur / Sécurité opérationnelle & Gouvernance]
- **Localisation** : Chapitre 20, Section 20.9, pp. 230 à 235.
- **Citations textuelles exactes** :
  - Page 232 : *« The agent’s specified user identity isn’t compatible with PIM or TAP because they don’t support long-term background operations (F-57, [A]) »*.
  - Page 233 : *« Déployer des agents de défense en leur attribuant des comptes utilisateurs pour leur permettre d'agir sur le SI [...] crée une dérive d'imputabilité où les mécanismes de PIM (Privileged Identity Management) et de TAP (Temporary Access Pass) échouent »*.
- **Diagnostic causal approfondi** :
  Dans les architectures de SOC automatisé (Microsoft Copilot for Security, Defender), l'incapacité d'intégrer des identités d'agents pures pousse les équipes d'exploitation à doter les agents de comptes d'utilisateurs humains avec privilèges élevés permanents. Cette pratique induit :
  - L'incompatibilité avec le PIM : le PIM exigeant une approbation humaine MFA interactive, les administrateurs mettent en place des passes permanents (TAP), détruisant le principe du moindre privilège (PoLP) ;
  - L'opacité médico-légale : les journaux d'audit attribuent les modifications d'infrastructure au compte de service sans trace opposable de l'empreinte d'invite ou de l'état du modèle ;
  - La violation des exigences de gouvernance prudentielle (BSIF E-23 et article 12.1 de la Loi 25).
- **Correctif formel** :
  Proscrire l'usage de comptes utilisateurs permanents pour les agents d'arrière-plan. Prescrire une architecture fondée sur des identités de charge de travail (*Workload Identity Federation*) associées à des jetons d'accès éphémères (durée $\le 15$ minutes) renouvelés sous attestation cryptographique de code d'enclave, et régis par un patron de *Double Commande Déterministe (Dual-Control FSM / OO4)*.

#### DEF-L2-14 [Majeur / Lacune algorithmique défensive]
- **Localisation** : Chapitre 20, Sections 20.7 à 20.10, pp. 228 à 235.
- **Citations textuelles exactes** :
  - Page 231 : *« Ce rapport reprend par ailleurs des métriques auto-déclarées d’éditeur, dont le présent chapitre ne reprend aucune »*.
  - Page 233 : *« Lecture de l’auteur — ce qu’il n’établit pas : qu’un centre d’opérations agentique se range en "gouvernable" ou "ingouvernable"... »*.
- **Diagnostic causal approfondi** :
  Alors que le chapitre promet le traitement de la boucle défensive, il se borne à un constat passif d'exposition symétrique à la triade de Willison et à une critique des fiches commerciales d'éditeurs (Microsoft, Google Cloud, CrowdStrike). Il n'articule aucune métrique formelle, aucun algorithme de détection d'anomalies sur les graphes de raisonnement (*reasoning graphs*), et aucun protocole d'isolation ou d'expulsion de sous-graphes compromis.
- **Correctif formel requis** :
  Formaliser les primitives opérationnelles de la boucle défensive :
  1. *Métrique de dérive de raisonnement* : Calcul de la distance d'édition de graphe d'exécution par rapport à un profil d'étalonnage nominal :
     $$\mathcal{D}(G_t, G_{\text{ref}}) = \frac{\text{GraphEditDist}(G_t, G_{\text{ref}})}{|V_t| + |E_t|}$$
  2. *Détection d'anomalies* : Détection des bifurcations anormales de flux d'appels d'outils via plongement temporel de graphe (Temporal Graph Neural Networks / GNN).
  3. *Protocole d'expulsion déterministe* : Révocation cryptographique immédiate de la session d'agent au PEP (*Policy Enforcement Point*), blocage de la paire de clés éphémères au niveau de la passerelle de maillage, et mise en quarantaine des artefacts mémoriels contaminés.

#### DEF-L2-15 [Majeur / Gouvernance inter-domaines & Spécification manquante]
- **Localisation** : Chapitre 18, Sections 18.1 à 18.6, pp. 201 à 210.
- **Citation textuelle exacte** :
  Page 202 : *« Le KYA transpose la logique du KYC — vérifier avant d’admettre — sans l’infrastructure institutionnelle qui rend le KYC possible... »*.
- **Diagnostic causal approfondi** :
  Après avoir dressé l'inventaire pertinent de 9 chantiers pré-normatifs disparates (DIF, Akamai, W3C, AGNTCY, OpenID), l'ouvrage n'articule aucune séquence algorithmique permettant à une passerelle d'entreprise d'exécuter la vérification d'un agent tiers lors de sa demande d'admission.
- **Correctif procédural requis** :
  Définir la machine à états d'admission KYA en 5 phases séquentielles :
  1. *Présentation* : Réception de l'Agent Card signée et des accréditations vérifiables W3C VC 2.0.
  2. *Résolution d'identité* : Résolution décentralisée du DID de l'agent et extraction de sa clé publique racine.
  3. *Contrôle de fraîcheur d'état* : Interrogation synchrone d'une liste de révocation cryptographique (W3C Bitstring Status List v1.0).
  4. *Vérification d'intégrité de charge* : Validation des attestations d'enclave sécurisée (TEE / vLEI).
  5. *Émission d'autorité locale* : Octroi d'un jeton de session éphémère ($T_{\text{exp}} \le 1\text{ h}$) lié à une clé de preuve de possession DPoP (RFC 9449).

#### DEF-L2-16 [Majeur / Architecture réseau & Cryptographie post-quantique]
- **Localisation** : Chapitre 21, Sections 21.1, 21.3 et 21.7, pp. 236 à 248.
- **Citations textuelles exactes** :
  - Page 237 : *« FIPS 203 (ML-KEM, encapsulation de clé) et FIPS 204 (ML-DSA, signature) sont des normes finales, publiées le 13 août 2024 »*.
  - Page 247 (§ 21.7) : *« les signatures et échanges post-quantiques, dont les tailles d’artefacts sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de main [...] Régime : entrée en [C], et le Vol. I trie lui-même ce verrou SPÉCULATIF ; aucune mesure publique ne le valide à son gel »*.
- **Diagnostic causal approfondi** :
  1. *Omission de FIPS 205* : FIPS 205 (SLH-DSA, ex-SPHINCS+) est le standard de signature post-quantique sans réseau euclidien (reposant uniquement sur les fonctions de hachage) promulgué par le NIST le même jour (13 août 2024). C'est le standard de repli universel indispensable en cas de percée cryptanalytique sur les réseaux euclidiens (Module-LWE / ML-DSA).
  2. *Déni de mesure sur les tailles d'artefacts* : L'auteur traite l'explosion volumétrique comme un verrou « spéculatif sans mesure publique ». Or, les spécifications finales du NIST fixent exactement ces grandeurs :
     - Ed25519 classique : Clé publique = 32 octets, Signature = 64 octets.
     - ML-DSA-44 (NIST Niveau 2) : Clé publique = 1 312 octets, Signature = 2 420 octets (multiplication par **38,8**).
     - ML-DSA-65 (NIST Niveau 3) : Clé publique = 1 952 octets, Signature = 3 309 octets.
     - ML-DSA-87 (NIST Niveau 5) : Clé publique = 2 592 octets, Signature = 4 627 octets (multiplication par **75**).
     - SLH-DSA-SHA2-128s (FIPS 205) : Clé publique = 32 octets, Signature = 7 856 octets.
     - SLH-DSA-SHA2-256s (FIPS 205) : Clé publique = 64 octets, Signature = 29 792 octets.
  3. *Rupture d'infrastructure réseau et HTTP* :
     - *Dépassement de MTU* : La MTU Ethernet standard étant de 1 500 octets (MSS TCP = 1 460 octets), toute signature ML-DSA-44 ou SLH-DSA force une fragmentation IP/TCP immédiate (2 à 21 segments par signature), dégradant la latence et la fiabilité des RPC multi-agents.
     - *Saturation des en-têtes HTTP (HTTP 431)* : Un jeton JWT/JWS encapsulant une signature ML-DSA-65 encodée en Base64URL atteint ~4,5 Ko. Dès qu'une chaîne de délégation compte deux ou trois signatures imbriquées, ou en mode hybride (Ed25519 + ML-DSA), l'en-tête `Authorization: Bearer <token>` dépasse 8 Ko à 14 Ko. Or, les passerelles d'API et proxys d'entreprise (ALB AWS, Envoy, Nginx) rejettent par défaut les requêtes excédant 8 Ko via l'erreur fatale `HTTP 431 Request Header Fields Too Large`.
- **Correctif formel et prescription d'ingénierie** :
  Intégrer formellement FIPS 205 dans le corps du texte. Modéliser l'impact volumétrique et prescrire les deux architectures de remédiation nécessaires :
  - *Découplage de transport* : Ne plus transmettre les signatures complètes dans les en-têtes de requêtes synchrones, mais des identifiants d'artefacts déréférençables hors bande via un cache d'attestations vérifié.
  - *Compactage binaire* : Remplacer l'encodage textuel JSON/Base64 par des conteneurs binaires compacts CBOR Web Tokens (CWT) et signatures COSE (RFC 9052 / RFC 9053).
  - *Architecture hybride en couches* : Sécuriser la couche transport (L4) via TLS 1.3 post-quantique (échange de clés ML-KEM-768 selon FIPS 203), tout en conservant au niveau applicatif (L7) des jetons de session signés avec des clés symétriques éphémères dérivées (HMAC-SHA256 ou KMAC), réservant les signatures asymétriques lourdes ML-DSA aux seuls mandats maîtres à longue durée de vie (NIST SP 800-227 / `draft-ietf-lamps-pq-composite-sigs`).

#### DEF-L2-17 [Majeur / Standardisation cryptographique]
- **Localisation** : Chapitre 21, Section 21.5, pp. 242 à 245.
- **Citation textuelle exacte** :
  Page 244 : *« La carte signée dispose d’un point où l’algorithme est déclaré, et ce point est obligatoire (F-03)... »*.
- **Diagnostic causal approfondi** :
  L'auteur affirme que l'Agent Card A2A est crypto-agile au motif que le champ `alg` de l'en-tête JWS (RFC 7515) permet de déclarer un nouvel algorithme. Cette assertion ignore le verrou normatif déterminant : au registre officiel de l'IANA pour JOSE et COSE, **aucun identifiant standard d'algorithme n'est ratifié pour ML-DSA ou SLH-DSA**. Les travaux IETF correspondants (`draft-ietf-cose-dilithium`, etc.) demeurent à l'état de brouillons non ratifiés. Dès lors, toute implémentation post-quantique d'une Agent Card reste confinée à des accords bilatéraux propriétaires non interopérables.
- **Correctif normatif requis** :
  Relever explicitement l'absence d'identifiants IANA ratifiés comme un verrou bloquant l'interopérabilité PQC industrielle des Agent Cards.

#### DEF-L2-18 [Majeur / Bris de composition tabulaire]
- **Localisation** : Chapitre 21, Section 21.8, Page 248 (`page-248.png`), Tableau 21.4 (« La feuille de route canadienne ITSM.40.001 »).
- **Citation textuelle exacte** :
  Dans l'en-tête du tableau :
  - Colonne 2 : *« LOT INSTRUIT LE 30 JUILLET 2026... Ses termes, lus à la page de l’organisme : l’information NON CLASSIFIÉ, PROTÉGÉ A et PROTÉGÉ B »*
  - Colonne 3 : *« les systèmes de TI non classifiés du gouvernement du Canada — réseaux traitant »*
  Et pour toutes les lignes suivantes du tableau, la Colonne 3 est entièrement vide.
- **Diagnostic causal approfondi** :
  Le flux de texte décrivant le périmètre ITSM.40.001 a été inversé entre les colonnes : la fin de phrase en colonne 3 (*« réseaux traitant »*) précède sémantiquement la proposition de la colonne 2 (*« l'information NON CLASSIFIÉ... »*). De plus, l'absence de contenu dans la colonne 3 sur les 4 lignes de données confirme une dislocation de la grille tabulaire.
- **Correctif requis** :
  Restructurer le tableau en deux colonnes explicites : `| Dimension réglementaire ITSM.40.001 | Contenu & Statut d'application |`.

#### DEF-L2-19 [Mineur / Rendu graphique tronqué]
- **Localisation** : Chapitre 12, Page 147 (`page-147.png`), Figure 12.4.
- **Citation textuelle exacte** :
  Dans la colonne gauche (« L'agent comme client ») :
  *« « Une application qui demande des ressources protégées pour »* [Texte coupé net sans suite].
- **Diagnostic causal approfondi** :
  La définition de « client » extraite de la RFC 6749 Section 1.1 a été coupée par la boîte de rendu graphique au mot « pour ».
- **Correctif requis** :
  Rétablir la définition intégrale de la RFC 6749 : *« Une application qui demande des ressources protégées pour le compte du détenteur de ressource et avec son autorisation. »*

#### DEF-L2-20 [Mineur / Glitch rédactionnel et contradiction interne]
- **Localisation** : Chapitre 12, Page 148 (§12.5).
- **Citation textuelle exacte** :
  Page 148 : *« Le chapitre n'écrit donc aucune date de publication pour cette révision. Parue le 28 juillet 2026 (2026-07-28). »*.
- **Diagnostic causal approfondi** :
  Collision de mise à jour lors de l'intégration des notes d'actualisation : la première phrase affirme ne pas donner de date de publication, puis la seconde colle immédiatement la date entre parenthèses.
- **Correctif formel** :
  Harmoniser la phrase : *« La date de publication a été confirmée le 28 juillet 2026 lors de la révision d'actualisation de la source. »*

#### DEF-L2-21 [Mineur / Discordance typologique et saut d'indexation]
- **Localisation** : Chapitre 14, Sections 14.1 et 14.2, pp. 162 à 164 (`page-162.png` et `page-164.png`).
- **Citation textuelle exacte** :
  - Page 162 : *« Figure 14.1 — La grille des cinq questions, et ce que chacune exige d’un mécanisme »*.
  - Page 164 : *« Tableau 14.2 — Application-témoin de la grille à trois mécanismes... »*.
- **Diagnostic causal approfondi** :
  L'encadré de la page 162 est structuré sous forme de tableau comparatif mais est étiqueté « Figure 14.1 ». Le tableau suivant en page 164 est nommé « Tableau 14.2 », ce qui supprime le « Tableau 14.1 » de la séquence des tableaux.
- **Correctif requis** :
  Renommer « Figure 14.1 » en « Tableau 14.1 » pour assurer la continuité de numérotation.

#### DEF-L2-22 [Mineur / Flottement terminologique des échelles d'autonomie]
- **Localisation** : Chapitre 14, Page 166 et Chapitre 22, Page 253.
- **Citation textuelle exacte** :
  Page 166 : *« Trois échelles homonymes coexistent au Vol. I, et seuls le cardinal et la numérotation les discriminent »*.
- **Diagnostic causal approfondi** :
  L'ouvrage renvoie la désambiguïsation formelle des niveaux d'autonomie au chapitre 43, créant une zone de flottement sémantique entre l'échelle opérationnelle à 4 paliers, l'échelle à 6 niveaux du Vol. I et la taxonomie d'orchestration OO1–OO4 du Ch. 22.
- **Correctif formel** :
  Insérer un tableau récapitulatif synoptique au §14.4 alignant immédiatement les trois échelles.

#### DEF-L2-23 [Mineur / Ponctuation manquante fusionnant deux phrases]
- **Localisation** : Chapitre 20, Section 20.4, Page 227 (`page-227.png`), 3e paragraphe.
- **Citation textuelle exacte** :
  *« ...elle permet à celui qui reçoit un jeton de demander s’il vaut encore L’asymétrie tient — mais elle n’était pas complète... »*.
- **Diagnostic causal approfondi** :
  Omission du point final entre « encore » et « L'asymétrie », fusionnant deux propositions distinctes.
- **Correctif requis** :
  Corriger par : *« ...de demander s'il vaut encore. L'asymétrie tient — mais elle n'était pas complète... »*.

#### DEF-L2-24 [Mineur / Rigueur documentaire et clauses de gel]
- **Localisation** : Chapitre 19, Page 212, et Chapitre 20, Pages 222 et 226.
- **Citation textuelle exacte** :
  - Page 212 & 222 : *« Publiée le 28 juillet 2026 (2026-07-28, constat du 23 octobre) ; rejeu non fait : cette section et la rangée "Jeton — MCP" du § 20.4 restent bornées à la révision 2025-11-25 »*.
  - Page 226 : *« Internet-Draft draft-mp-agntcy-ads, de soumission individuelle ; balayage sur la révision -01, supplantée par la -02 du 6 juillet 2026, non rebalayée »*.
- **Diagnostic causal approfondi** :
  Pour un ouvrage compilé fin octobre 2026, maintenir l'analyse de sécurité sur une révision vieille de neuf mois en déclarant le rejeu non fait affaiblit l'actualité de l'audit. La révision draft-mp-agntcy-ads-02 était disponible plusieurs semaines avant la date de gel documentaire du 27 juillet 2026.
- **Correctif requis** :
  Intégrer les apports stabilisés de la révision MCP du 28 juillet 2026 et valider le balayage sur la version draft-mp-agntcy-ads-02.

#### DEF-L2-25 [Mineur / Ambiguïté de portée réglementaire canadienne]
- **Localisation** : Chapitre 21, Pages 248-249 (§21.8, Tableau 21.4).
- **Citation textuelle exacte** :
  Page 248 : *« ITSM.40.001 vise le gouvernement fédéral, non les banques ni les assureurs : une institution qui s'en réclamerait comme d'une échéance applicable lirait, encore une fois, le plafond d'un autre »*.
- **Diagnostic causal approfondi** :
  Bien que l'avertissement textuel soit limpide, la disposition du Tableau 21.4 mettant en exergue les jalons 2031 et 2035 peut prêter à confusion pour un directeur de la conformité bancaire canadienne. Le BSIF / OSFI n'a émis qu'un bulletin d'orientation en mars 2026 et l'AMF n'a fixé aucune date butoir contraignante.
- **Correctif formel** :
  Ajouter une note explicite rappelant que le secteur financier canadien sous réglementation BSIF/AMF demeure régi par la gestion générale du risque opérationnel (BSIF E-21 / E-23) sans calendrier quantique coercitif distinct.

---

## 4. Analyse critique approfondie par chapitre et composant architectural

### 4.1 Ch. 12 (pp. 144–151) : L'héritage d'un demi-siècle et les standards IAM étirés
- **Inadaptation structurelle d'OAuth 2.0 (RFC 6749)** :
  L'auteur démontre avec brio l'aporie fondamentale qui frappe l'application d'OAuth 2.0 aux agents autonomes. Dans la RFC 6749, l'agent ne peut être ni un simple `client` (car le consentement interactif via `user-agent` est impossible lors de tâches d'arrière-plan sans présence humaine — *Human-Not-Present*), ni un `resource owner`. S'il recourt au flux `client_credentials` (§4.4), il agit sous une identité machine statique partagée, créant l'écart d'attribution (*attribution gap*) documenté par l'OWASP (ASI03).
- **Biais réducteur sur les jetons porteurs et omission de DPoP / mTLS** :
  Le réquisitoire contre OAuth 2.0 pèche toutefois par excès de simplification en assimilant l'ensemble de la norme au seul *bearer token* impersonnel de la RFC 6750. L'auteur omet les standards ratifiés de preuve de possession de l'IETF :
  - *RFC 8705 (mTLS)* : liaison cryptographique de jetons d'accès aux certificats clients X.509 ;
  - *RFC 9449 (DPoP - Demonstrating Proof-of-Possession)* : liaison cryptographique de chaque requête HTTP à une paire de clés asymétriques éphémères du client, éliminant radicalement le risque de vol et de rejeu de jetons illustré par l'incident Salesforce UNC6395 d'août 2025.
- **Caducité de SCIM 2.0 pour les agents** :
  L'analyse de SCIM 2.0 (RFC 7643/7644) prouve rigoureusement l'absence de ressource d'agent dans la spécification canonique. Le projet d'extension de la Cloud Security Alliance (`draft-abbey-scim-agent-extension-00`) est devenu caduc le 19 avril 2026 sans être reconduit.
- **Bris de rendu** : Troncature textuelle nette en pied de page 151 (DEF-L2-05) et coupure dans la Figure 12.4 (DEF-L2-19).

### 4.2 Ch. 13 (pp. 152–160) : Identifiants décentralisés (DID) et Verifiable Credentials v2.0
- **Lucidité sur le terrain financier et did:web** :
  L'auteur confirme avec probité qu'aucune grande institution financière n'exploite de DID en production (degré 3 d'absence, p. 158). Sa critique de la méthode `did:web` est magistrale : en liant la résolution d'identité à un nom de domaine DNS et à un certificat TLS périmétrique, `did:web` réintroduit l'autorité centralisée qu'il prétendait abolir.
- **Le schisme d'interopérabilité de W3C VC v2.0** :
  La Recommandation W3C du 15 mai 2025 a institutionnalisé une fracture interne majeure entre deux familles de preuves mutuellement incompatibles :
  1. *Data Integrity Proofs* en JSON-LD (canonicalisation de graphes RDF RDFC-2022 et cryptosuites `eddsa-rdfc-2022`) ;
  2. *Enveloping Proofs* en jetons plats sérialisés (IETF JOSE/COSE / SD-JWT).
  Deux agents conformes à la recommandation W3C VC v2.0 ne peuvent pas interopérer si l'un traite du RDF canonique et l'autre des jetons JSON enveloppés.
- **L'omission de la divulgation sélective (SD-JWT VC / BBS+)** :
  L'auteur n'aborde pas les accréditations vérifiables à divulgation sélective (SD-JWT VC RFC 9542 et cryptosuite W3C BBS v1.0). C'est une lacune réglementaire majeure : sans divulgation sélective, l'agent ne peut pas expurger les données superflues d'un mandat, violant frontalement le principe de minimisation de l'article 12.1 de la Loi 25 québécoise.
- **Bris de rendu** : Collisions d'encadrés pleine largeur fracturant la syntaxe grammaticale aux pages 152 et 153 (DEF-L2-06).

### 4.3 Ch. 14 (pp. 160–167) : Grille d'évaluation de la confiance et les 5 questions
- **Puissance méthodologique de la grille Q-A à Q-E** :
  La matrice d'interrogation systématique (Q-A : *Qui es-tu ?*, Q-B : *Qui t'a créé ?*, Q-C : *Pour qui agis-tu ?*, Q-D : *Que peux-tu faire ?*, Q-E : *Qui en répond ?*) est l'une des contributions doctrinales les plus robustes de l'ouvrage pour les comités d'architecture bancaire. L'application-témoin du Tableau 14.2 prouve qu'aucun mécanisme contemporain n'honore les cinq questions.
- **Limites heuristiques et alignement d'autonomie** :
  La grille demeure un outil descriptif sans formalisation mathématique d'invariants. Par ailleurs, la coexistence de trois échelles d'autonomie (4 paliers, 6 niveaux Vol. I et la taxonomie OO1-OO4) introduit un flottement terminologique qu'il convient de stabiliser (DEF-L2-22).

### 4.4 Ch. 15-16 (pp. 167–188) : L'Agent Card A2A et la chimère du « Passeport d'agent »
- **La fragilité critique de l'Agent Card A2A v1.0.0** :
  L'Agent Card (Linux Foundation / Google) canonicalisée par RFC 8785 (JCS) et signée par RFC 7515 (JWS) est intrinsèquement inapte à servir de passeport de sécurité :
  - Absence totale de champs temporels de fraîcheur (`iat`, `exp`, `nbf`) : une carte compromise demeure valide indéfiniment ;
  - Caractère facultatif de la sécurité : la signature est un `MAY`, la vérification un `SHOULD` ;
  - Absence de tout protocole de contrôle d'état et de magasin de clés de confiance prescrit.
- **La chimère du Passeport d'agent virtuel** :
  L'auteur formalise le passeport d'agent comme un artefact virtuel quadripartite (carte signée, registre gouverné, chaîne de mandat, attestations de conformité). Il énonce la thèse capitale : *« l'assemblage n'est pas une somme »*. Cependant, formuler l'impératif catégorique « Rien n'entre au maillage sans lui » (p. 180) paralyse tout déploiement en 2026, car cet objet n'existe dans aucun standard international ratifié.
- **Bris de rendu** : Dislocation destructrice du Tableau 16.3 à la page 188 (DEF-L2-03).

### 4.5 Ch. 17 (pp. 188–201) : Chaîne de mandat et falsification formelle des deux sauts
- **Réfutation du « théorème des deux sauts »** :
  L'affirmation d'une impossibilité mathématique de préserver l'opposabilité au-delà de deux sauts ($A \to B \to C$) est l'erreur formelle la plus grave du Livre II.
  1. L'aveu de la page 198 concède l'absence de toute démonstration mathématique.
  2. La section 4.4 de la RFC 8693 spécifie explicitement les *Nested 'act' Claims*, contredisant l'assertion d'absence au degré 3 de la page 197.
  3. La clause §4.1 de la RFC 8693 interdit formellement d'utiliser la revendication `act` pour les décisions d'autorisation, privant le Token Exchange de toute portée probatoire en contrôle d'accès strict.
  4. L'affirmation selon laquelle Biscuit ne lie pas l'identité des maillons est fausse (DEF-L2-01).
- **Théorie des capabilités cryptographiques** :
  Sous le modèle standard EUF-CMA, les algèbres de capabilités (Macaroons sous PRF, Biscuit sous Datalog) démontrent mathématiquement qu'une chaîne de délégations à atténuation monotone préserve l'opposabilité, la non-répudiation et l'imputabilité pour tout saut $n \ge 1$.
- **Erreur matérielle dans la Figure 17.2** : Boîte 3 étiquetée « Carte d'agent » associée à la référence `F-29, [A]` des Transaction Tokens (DEF-L2-02).

### 4.6 Ch. 18-19 (pp. 201–222) : KYA, taxonomie des attaques et la Triade Létale
- **Lucidité sur le KYA et l'agent mutable** :
  L'auteur démontre avec pertinence que le KYC bancaire repose sur l'état civil régalien et le droit pénal. Vouloir créer un KYA purement algorithmique sans fédération préalable est une illusion. L'analyse de l'agent mutable à mémoire épisodique (rendant caduque l'authentification par empreinte binaire statique) est visionnaire.
- **Taxonomie des attaques agentiques** :
  La classification des menaces (ATK-01 Rug-Pull, ATK-02 Confused Deputy, ATK-03 EchoLeak CVE-2025-32711) s'aligne rigoureusement sur MITRE ATLAS et l'OWASP Top 10 for Agentic AI 2026.
- **L'impasse du modèle de Hardy (1988) et l'illusion cognitive** :
  L'auteur cite Norm Hardy (1988) sans adopter la solution des Object-Capabilities qu'il formalise. Face à la Triade Létale de Simon Willison, le recours à des filtres de prompts probabilistes est inopérant : seule une rupture déterministe au niveau de la passerelle d'exécution (révocation immédiate des canaux réseau lors de l'ingestion de contenu non fiable, architecture Dual-Agent étanche) offre une garantie formelle de sécurité (DEF-L2-11).

### 4.7 Ch. 20 (pp. 222–236) : Boucle défensive, MCP Rug-Pull et l'Agentic SOC
- **La faille de Rug-Pull dans MCP** :
  L'auteur met au jour une vulnérabilité protocolaire majeure : le schéma MCP `tools/list` ne comporte aucun champ de hachage ou de signature, autorisant un serveur d'outils à notifier dynamiquement une modification malveillante via `tools/list_changed` sans rompre la conformité (DEF-L2-12).
- **Régression de sécurité dans l'Agentic SOC** :
  Dans Microsoft Defender, l'incompatibilité de l'agent avec PIM/TAP impose l'octroi d'un compte de service permanent à hauts privilèges, violant le principe de moindre privilège (PoLP) et supprimant l'imputabilité individuelle dans les journaux d'audit (DEF-L2-13).
- **Vacuité algorithmique de la boucle défensive** :
  Le chapitre dresse un constat d'impuissance sans proposer de métriques formelles sur les graphes de raisonnement (distance d'édition de graphe, temporal GNN) ni de protocole d'expulsion déterministe (DEF-L2-14).

### 4.8 Ch. 21 (pp. 236–252) : L'horloge post-quantique et les contraintes réseau
- **Rigueur chronologique et risque Harvest Now, Forge Later** :
  L'auteur distingue parfaitement la ratification finale des normes NIST (FIPS 203 et 204 au 13 août 2024) du statut consultatif du projet NIST IR 8547. Il souligne avec force que le risque immédiat pour les artefacts signés d'agents est la falsification rétroactive de mandats (*Harvest Now, Forge Later*).
- **Cécité sur les contraintes physiques PQC et omission de FIPS 205** :
  L'omission de FIPS 205 (SLH-DSA) et le refus de chiffrer l'impact volumétrique constituent une lacune technique majeure. L'explosion de taille des signatures (ML-DSA-44 à 2 420 octets, SLH-DSA à 7 856 octets) provoque une fragmentation systématique de la MTU Ethernet (1 500 octets) et entraîne des rejets immédiats `HTTP 431 Request Header Fields Too Large` sur les passerelles d'API dès que des signatures sont imbriquées dans des jetons d'autorisation (DEF-L2-16).
- **Verrou normatif IANA** : Absence totale d'identifiants ratifiés pour les algorithmes PQC dans les registres IANA pour JOSE et COSE (DEF-L2-17).
- **Bris de rendu** : Collision d'un encadré de 16 lignes fracturant une phrase entre les pages 242 et 243 (DEF-L2-04) et dislocation du Tableau 21.4 (DEF-L2-18).

### 4.9 Ch. 22 partiel (pp. 252–255) : Charnière vers le Livre III et taxonomie OO1-OO4
- **Articulation théorique avec l'orchestration déterministe** :
  L'introduction de la taxonomie OO1-OO4 de la TU Munich (Rinderle-Ma & Mangler, 30 juin 2026) permet d'isoler la discontinuité critique **OO2 $\to$ OO3**. Au niveau OO3/OO4, l'inversion de contrôle au profit d'un moteur d'exécution déterministe (machines à états finis, réseaux de Petri) devient la condition impérative de conformité réglementaire pour le secteur financier.

---

## 5. Confrontation bibliographique et état de l'art (2024–2026)

Le tableau ci-dessous confronte systématiquement l'ensemble des textes normatifs et articles scientifiques mobilisés dans le Livre II à l'état réel de l'art à date de novembre 2026 :

| Référence / Texte normatif | Date officielle | Statut documentaire réel | Évaluation critique dans le Compendium | Verdict Niveau 2 (Arbitrage Racine RSA) |
|---|---|---|---|---|
| **RFC 6749 & RFC 6750 (OAuth 2.0)** | Octobre 2012 | Internet Standard (IETF) | Analysé sous l'angle du jeton porteur impersonnel et du flux interactif humain. | **Biais réducteur** : Omet RFC 8705 (mTLS) et RFC 9449 (DPoP), qui éliminent le jeton porteur non lié. |
| **RFC 8693 (OAuth Token Exchange)** | Janvier 2020 | Proposed Standard (IETF) | Jugé inapte au multi-saut (« non documenté, degré 3 »). | **Double erreur formelle** : La §4.4 spécifie le multi-saut (*Nested 'act'*), mais la §4.1 interdit formellement d'utiliser `act` pour l'autorisation. |
| **`draft-ietf-oauth-transaction-tokens`** | Juillet 2026 | Internet-Draft actif (rév. -09) | Borné à un domaine de confiance unique (*« within a single trust domain »*). | **100% Conforme** : Analyse rigoureuse de la frontière administrative de propagation de contexte. |
| **RFC 7643 & 7644 (SCIM 2.0)** | Septembre 2015 | Proposed Standard (IETF) | Absence de ressource d'agent dans la spécification de base. | **Conforme mais incomplet** : Ignore l'extension de schéma (§3.3). Projet CSA expiré le 19 avril 2026. |
| **W3C VC Data Model v2.0** | 15 mai 2025 | W3C Recommendation | Cité avec exactitude quant à sa date et ses 4 propriétés obligatoires. | **Sous-estimation du schisme** : La fracture entre Data Integrity (RDF) et Enveloping (JOSE/COSE) empêche l'interopérabilité directe. |
| **W3C DID Core v1.0 & v1.1 CR** | Mars 2026 | Rec. (v1.0) / Cand. Rec. (v1.1) | Seule la clé `id` est impérative ; résolution hors périmètre. | **100% Conforme** : Diagnostic lucide sur la dépendance périmétrique de `did:web` (DNS/TLS). |
| **A2A v1.0.0 (Google / Linux Foundation)** | 12 mars 2026 | Spécification de consortium | Agent Card signée via JCS (RFC 8785) et JWS (RFC 7515). | **Insuffisant** : Ne dénonce pas assez l'absence de timestamps (`exp`), la signature optionnelle (`MAY`) et l'absence de révocation. |
| **RFC 9635 (GNAP)** | Octobre 2024 | Proposed Standard (IETF) | Mentionné brièvement p. 199. | **Sous-exploité** : Représente le véritable successeur d'OAuth pour les agents asynchrones avec Proof-of-Possession. |
| **Macaroons (Birgisson et al., NDSS 2014)** | Février 2014 | Conférence évaluée par pairs | Cité p. 199 mais faussement jugé inapte à préserver l'identité. | **Réfutation mathématique** : Fournit la preuve formelle de la délégation en cascade opposable sous PRF. |
| **Biscuit Tokens (Geal et al., 2021-2026)** | 2022-2026 | Standard industriel ouvert | Déclaré à tort inapte à lier l'identité des maillons (p. 200). | **Erreur factuelle** : Chaque bloc Datalog peut lier cryptographiquement la clé publique du maillon suivant sous EUF-CMA. |
| **NIST FIPS 203 (ML-KEM)** | 13 août 2024 | FIPS officiel final | Ratifié le 13 août 2024 ; avis d'errata bien documenté. | **100% Conforme** : Analyse chronologique exemplaire. |
| **NIST FIPS 204 (ML-DSA)** | 13 août 2024 | FIPS officiel final | Ratifié le 13 août 2024 ; signatures post-quantiques. | **Lacune physique** : Omission de l'impact volumétrique des clés (1,3 Ko) et signatures (2,4 Ko) sur la MTU et HTTP. |
| **NIST FIPS 205 (SLH-DSA)** | 13 août 2024 | FIPS officiel final | Standard de signature sans réseau (Hash-based). | **OMISSION TOTALE** : Standard de repli indispensable en cas de percée cryptanalytique sur les réseaux euclidiens. |
| **NIST IR 8547 (PQC Transition)** | Novembre 2024 | Initial Public Draft | Dépréciation 2030, retrait 2035. Non contraignant en droit privé. | **100% Conforme** : Analyse exacte du statut pré-normatif. |
| **CCCS ITSM.40.001 (Canada)** | 23 juin 2025 | Guide du gouvernement fédéral | Jalons 2031 (prioritaire) et 2035 (général) restreints au fédéral. | **Conforme mais défiguré** : Analyse juridique exacte, mais table disloquée dans le Tableau 21.4. |
| **Norm Hardy (1988) — Confused Deputy** | Octobre 1988 | Article fondateur | Cité pour illustrer l'usurpation de mandat par injection indirecte. | **Incomplet** : Réduit à un label sans intégrer la solution par Object-Capabilities formalisée dans l'article. |
| **Simon Willison — Triade Létale** | 2023-2025 | Littérature de sécurité IA | Données privées $\cap$ Contenu non fiable $\cap$ Canal de sortie. | **100% Conforme** : Formulation exacte de l'espace de vulnérabilité agentique. |
| **AgentPoison (NeurIPS 2024)** | Décembre 2024 | Conférence révisée par pairs | Mentionné pour réfuter les défenses cognitives probabilistes. | **100% Conforme** : Valide l'impératif du cloisonnement architectural déterministe. |
| **Taxonomie OO1-OO4 (TU Munich)** | 30 juin 2026 | Prépublication universitaire | Découpage des options d'orchestration agentique. | **100% Conforme** : Prudence méthodologique exemplaire quant au statut de préprint. |

---

## 6. Recommandations concrètes de remédiation pour l'auteur

Pour hisser le Livre II au niveau d'une référence doctrinale et technique incontestable devant les régulateurs prudentiels et les directions de sécurité, l'auteur doit appliquer les six chantiers de remédiation suivants :

1. **Reconstruction formelle du Chapitre 17 (La chaîne de mandat)** :
   - *Réfuter la thèse d'un théorème d'impossibilité des deux sauts* : requalifier le problème en « défi d'impédance protocolaire et de révocation en cascade en entreprise ».
   - *Corriger l'analyse de la RFC 8693* : citer explicitement la section 4.4 (*Nested 'act' claims*) pour corriger la fausse assertion d'absence de documentation au degré 3, tout en démontrant pourquoi la section 4.1 disqualifie le Token Exchange pour les décisions d'autorisation opposable.
   - *Intégrer les formalismes par capabilités* : intégrer la preuve de délégation par induction sous EUF-CMA et corriger l'affirmation factuellement fausse sur Biscuit (qui lie parfaitement l'identité des maillons via des faits Datalog signés).
   - *Corriger la Figure 17.2* : remplacer la référence `F-29` de la boîte « Carte d'agent » par `F-04 / F-07`.

2. **Recompilation et assainissement typographique immédiats** :
   - *Restaurer le Tableau 16.3 (p. 188)* : réaligner les colonnes pour réintégrer la mention `PROJETÉ` dans la colonne « Tri » et restituer la description complète dans la colonne « Ce sur quoi il s'appuie ».
   - *Débloquer l'encadré flottant des pp. 242-243* : extraire les 16 lignes en gras du flux syntaxique pour reconnecter le mot-clé `tri :` à son prédicat `fait PROJETÉ`.
   - *Réparer le Tableau 21.4 (p. 248)* : fusionner et réaligner les colonnes 2 et 3 pour supprimer les cellules vides et rétablir la syntaxe continue de la directive ITSM.40.001.
   - *Supprimer les coupures et encadrés intrusifs (pp. 151, 152, 153, 147)* : forcer des sauts de paragraphe propres avant et après chaque encadré méthodologique et restituer la fin de phrase tronquée au bas de la page 151.

3. **Refonte architecturale de la sécurité face au Confused Deputy et à la Triade Létale (Ch. 19-20)** :
   - *Abandonner les parades cognitives probabilistes* : stipuler explicitement qu'aucun filtre de prompt ou classificateur LLM ne fournit de garantie de sécurité contre l'injection indirecte.
   - *Adopter le modèle des Object-Capabilities (Hardy 1988)* : lier chaque invocation d'outil à un triplet indivisible $\langle \text{URI}, \text{Scope}, \text{ProofOfPossession} \rangle$.
   - *Prescrire le cloisonnement architectural déterministe* : imposer la règle de révocation dynamique de canal réseau dès l'ingestion d'un flux non fiable, et isoler les agents d'ingestion dans une architecture Dual-Agent étanche.
   - *Sécuriser MCP face au Rug-Pull* : imposer une empreinte canonique immuable $\mathcal{H}_{\text{tool}} = \text{SHA-256}(\text{JCS}(\text{name} \parallel \text{description} \parallel \text{inputSchema}))$ scellée lors de l'octroi d'autorisation.

4. **Remédiation de l'Agentic SOC (Ch. 20)** :
   - *Interdire les comptes permanents hautement privilégiés* : proscrire la dérive constatée dans Microsoft Defender consistant à bypasser PIM/TAP pour des opérations d'arrière-plan.
   - *Prescrire des jetons éphémères attestés* : imposer des jetons de charge de travail liés à des enclaves sécurisées (durée $\le 15$ min) et régis par une machine à états de double commande déterministe (Dual-Control FSM / OO4).
   - *Intégrer des métriques d'exécution formelles* : documenter le calcul de la distance d'édition de graphe d'exécution ($\mathcal{D}(G_t, G_{\text{ref}})$) et la détection d'anomalies de graphes de raisonnement par réseaux temporels.

5. **Complétude et ingénierie de la transition Post-Quantique (Ch. 21)** :
   - *Intégrer FIPS 205 (SLH-DSA)* : présenter la signature à base de hachage comme l'algorithme de repli indispensable en cas de faille sur les réseaux euclidiens de ML-DSA.
   - *Chiffrer l'impact volumétrique et prescrire des solutions réseau* : documenter l'asymétrie de taille (2,4 à 4,6 Ko pour ML-DSA, jusqu'à 29,8 Ko pour SLH-DSA), la fragmentation systématique de la MTU Ethernet (1 500 octets) et le risque de rejet `HTTP 431`.
   - *Prescrire le découplage hors bande et les formats binaires* : remplacer les signatures complètes dans les en-têtes synchrones par des identifiants d'artefacts vérifiables dans un cache, et adopter les jetons binaires CBOR / COSE (RFC 9052).
   - *Relever le verrou IANA* : souligner l'absence d'identifiants ratifiés pour PQC dans JOSE/COSE comme un obstacle à l'interopérabilité des Agent Cards.

6. **Spécification procédurale d'admission KYA (Ch. 18)** :
   - Remplacer le catalogue descriptif de chantiers pré-normatifs par la machine à états finis déterministe en cinq phases (Présentation $\to$ Résolution DID $\to$ Fraîcheur d'état synchrone $\to$ Vérification d'enclave TEE/vLEI $\to$ Émission de jeton de session DPoP $\le 1\text{ h}$).

---

## 7. Protocole de vérification indépendante et audit reproductible

Tout auditeur indépendant peut vérifier l'exactitude des constats du présent rapport d'unité par les étapes suivantes :

1. **Contrôle de l'absence de preuve et falsification des deux sauts (DEF-L2-01)** :
   - Ouvrir `DOCUMENT_TEXT_MAP.md` aux lignes 17098–17105 (page 198 du PDF) : constater textuellement l'aveu *« aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
   - Consulter la RFC 8693 Section 4.4 : vérifier la présence des *Nested 'act' Claims*.
   - Consulter la RFC 8693 Section 4.1 : vérifier la mention formelle *« MUST NOT be used for access control decisions »*.
   - Consulter la spécification de Biscuit (`biscuit-auth`) : vérifier qu'un bloc d'atténuation signé permet de lier sans équivoque la clé publique du maillon suivant.
2. **Contrôle visuel des bris de composition typographique** :
   - Ouvrir `page-188.png` : observer la dislocation du Tableau 16.3 avec colonne vide et texte glissé (DEF-L2-03).
   - Ouvrir `page-242.png` et `page-243.png` : observer la coupure `tri :` suivie de l'encadré de 16 lignes et la reprise déconnectée `fait PROJETÉ` (DEF-L2-04).
   - Ouvrir `page-248.png` : observer l'inversion d'en-tête et les cellules vides de la colonne 3 du Tableau 21.4 (DEF-L2-18).
   - Ouvrir `page-151.png` : constater la troncature nette *« ; un document »* sous le Tableau 12.3 (DEF-L2-05).
   - Ouvrir `page-152.png` et `page-153.png` : observer l'injection intrusive des encadrés fracturant les liaisons syntaxiques (DEF-L2-06).
   - Ouvrir `page-193.png` : constater la mention erronée `F-29, [A]` dans la boîte 3 de la Figure 17.2 (DEF-L2-02).
   - Ouvrir `page-147.png` : constater la troncature *« pour »* dans la Figure 12.4 (DEF-L2-19).
3. **Contrôle des dimensions cryptographiques PQC (DEF-L2-16)** :
   - Consulter le standard NIST FIPS 204 (Tableaux 1 et 2) : vérifier que la clé publique de ML-DSA-44 mesure 1 312 octets et sa signature 2 420 octets (taille totale 3 732 octets, soit 38,8x celle d'Ed25519 à 96 octets).
   - Consulter le standard NIST FIPS 205 (Tableau 1) : vérifier que la signature de SLH-DSA-SHA2-128s mesure 7 856 octets.
   - Calculer la taille d'un jeton JWT à deux signatures ML-DSA : $> 2 \times 2\,420 \times 1{,}33 \approx 6{,}4$ Ko, approchant ou dépassant le seuil de 8 Ko par défaut des passerelles HTTP.

---
*Rapport définitif d'unité de Niveau 2 approuvé et scellé pour le segment Livre II du Compendium le 3 novembre 2026 par le Final Review Aggregator (Racine RSA).*
