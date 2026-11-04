# RAPPORT D'AUDIT CRITIQUE ET ÉVOLUÉ (RSA NIVEAU 1 — ARBITRAGE L1_2)
# LIVRE II : « FAIRE CONFIANCE — IDENTITÉ NON HUMAINE ET DÉLÉGATION VÉRIFIABLE »

**Document audité** : `documents/Compendium.pdf`  
**Segment audité** : Livre II — *Faire confiance : Identité non humaine et délégation vérifiable* (Ch. 12 à 21, pp. 144 à 251) et amorce de transition vers le Livre III (Ch. 22, pp. 252 à 255 / Segments S14 à S23 de `REVIEW_PLAN.md`).  
**Auteur de la synthèse évoluée** : Review Aggregator 2 (RSA Niveau 1)  
**Candidats de Niveau 0 arbitrés** : Candidat 3 (`handoff_3.md`) et Candidat 4 (`handoff_4.md`)  
**Date d'arbitrage** : 3 novembre 2026  
**Référentiel méthodologique** : Axes R2 (Rigueur formelle, algorithmique et théorique) et R3 (Confrontation bibliographique et état de l'art normatif 2024-2026).  

---

## 1. Résumé Exécutif d'Évaluation du Livre 2

Le Livre II du *Compendium* constitue la clé de voûte sécuritaire, cryptographique et protocolaire de l'ouvrage. Situé entre l'exposition des protocoles d'interaction (Livre I) et l'encadrement réglementaire financier déterministe (Livre III), il entreprend de formaliser la pile d'identité non humaine (*Machine/Agent Identity*) et de délégation vérifiable indispensable au déploiement d'agents autonomes en environnement bancaire régulé.

### 1.1 Apports conceptuels majeurs et posture épistémique
L'arbitrage confirme la haute valeur méthodologique de plusieurs constructions de l'auteur :
1. **Une discipline documentaire rigoureuse** : Le système formalisé des « degrés d'absence » (degré 1 : fait négatif vérifié par balayage exhaustif ; degré 2 : fait négatif établi par réserve expresse de la source ; degré 3 : absence de documentation dans le corpus) confère à l'ouvrage une probité intellectuelle rare, immunisée contre les annonces sensationnalistes d'éditeurs et les interpolations statistiques non étayées.
2. **La grille des cinq questions (Q-A à Q-E, Ch. 14)** : Cette matrice d'interrogation systématique (*Qui es-tu ? Qui t'a créé ? Pour qui agis-tu ? Que peux-tu faire ? Qui en répond ?*) fournit un outil d'audit d'une remarquable puissance analytique. Appliquée aux mécanismes actuels (carte d'agent, annuaires commerciaux, registres ouverts), elle démontre avec rigueur qu'aucun mécanisme contemporain n'honore simultanément les cinq exigences.
3. **La déconstruction du « Passeport d'agent » (Ch. 16)** : En qualifiant sans détour le passeport d'agent d'« objet de synthèse » n'existant dans aucune spécification ratifiée de 2026, l'auteur évite l'écueil de la réification prématurée et prouve que l'assemblage quadripartite (carte signée, registre, mandat, attestations de conformité) n'est pas une simple addition mécanique.
4. **La caractérisation fine de la dette cryptographique post-quantique (Ch. 21)** : L'auteur met en lumière la nature asymétrique de la menace quantique sur l'identité : le risque premier pour les artefacts signés (cartes, attestations) n'est pas le déchiffrement rétroactif (*Harvest Now, Decrypt Later*), mais la **rupture rétroactive de non-répudiation et la falsification d'antériorité** (*Harvest Now, Forge Later*), anéantissant la force probante des pistes d'audit patrimoniales.

---

### 1.2 Faiblesses critiques, vices formels et défauts de composition
En dépit de ces qualités, la confrontation contradictoire approfondie des candidats 3 et 4 et la vérification directe sur les artefacts de rendu graphique (`page-144.png` à `page-255.png`) révèlent des failles majeures réparties en trois ordres :

1. **Erreur formelle et falsification théorique (Bloquant)** :
   - **Falsification de la « rupture d'opposabilité à deux sauts » (Ch. 17)** : L'affirmation centrale selon laquelle une chaîne de délégation $A \to B \to C$ perd structurellement son opposabilité dès le second saut procède d'une confusion catégorielle majeure. L'auteur a érigé une règle procédurale locale d'autorisation *stateless* (la clause de la RFC 8693 Section 4.1 qualifiant les acteurs intermédiaires imbriqués d'« informational only ») en impossibilité mathématique universelle. Sous le modèle standard d'infalsifiabilité existentielle (EUF-CMA), l'opposabilité se conserve formellement pour toute profondeur finie $n \ge 2$ via des chaînes de signatures asymétriques, des accréditations vérifiables W3C v2.0 chaînées ou des capabilités à atténuation monotone (Macaroons de Google/NDSS 2014, Biscuit tokens sous Datalog). De plus, l'affirmation de la page 200 selon laquelle Biscuit ne lie pas l'identité de chaque maillon est factuellement fausse.
2. **Défauts de rendu typographique destructifs (Bloquants et Majeurs)** :
   - **Dislocation du Tableau 16.3 (p. 188)** : La compilation a provoqué un décalage horizontal des colonnes, amputant le texte descriptif qui glisse dans la colonne « Tri », tandis que la colonne « Ce sur quoi il s'appuie » se retrouve totalement vide.
   - **Collision d'encadré flottant (pp. 242-243)** : Un encadré méthodologique de 16 lignes en gras a été injecté au milieu d'une phrase, séparant le mot-clé `tri :` (bas de page 242) de son prédicat `fait PROJETÉ` (haut de page 243).
   - **Inversion d'en-tête et colonnes orphelines dans le Tableau 21.4 (p. 248)** : Le texte relatif à la directive canadienne ITSM.40.001 est disloqué et inversé entre les colonnes 2 et 3, laissant la colonne 3 vide sur toutes les lignes de données.
   - **Collisions et troncatures textuelles en cascade (pp. 147, 151, 152, 153)** : Troncatures nettes de paragraphes en fin de page 151, insertion d'encadrés de thèse ou d'extraction en plein milieu de propositions grammaticales (pp. 152, 153), et troncature graphique d'une définition RFC dans la Figure 12.4 (p. 147).
3. **Angles morts d'architecture, de sécurité et d'ingénierie post-quantique (Majeurs)** :
   - **Cécité sur les contraintes physiques PQC (Ch. 21)** : L'ouvrage omet la norme finale FIPS 205 (SLH-DSA) et qualifie de « spéculatif sans mesure » le surcoût volumétrique des signatures PQC. Or, les tailles normatives de ML-DSA (2,4 à 4,6 Ko) et SLH-DSA (7,8 à 49,8 Ko) excèdent immédiatement la MTU Ethernet standard (1 500 octets), imposant une fragmentation TCP systématique, et saturent les limites des en-têtes HTTP (`Authorization: Bearer`), déclenchant des rejets fatals HTTP 431 par les passerelles réseau d'entreprise (ALB, Nginx, Envoy).
   - **Impasse de standardisation IANA pour JOSE/COSE (Ch. 21)** : L'affirmation de crypto-agilité de l'Agent Card via le paramètre `alg` ignore qu'aucun identifiant d'algorithme PQC n'est ratifié par l'IANA pour JWS/COSE à mi-2026.
   - **Vacuité algorithmique et régression de sécurité dans l'Agentic SOC (Ch. 20)** : Le chapitre défensif n'articule aucune métrique formelle de dérive de raisonnement, aucun algorithme de détection sur les graphes d'exécution, et aucun protocole d'isolation/expulsion de sous-graphes compromis. En pratique, l'architecture d'agent défensif analysée (Microsoft Defender) viole frontalement le principe de moindre privilège (PoLP) en imposant un compte permanent sans PIM ni TAP.
   - **Omission de la sécurité par capabilités (Object-Capabilities, Ch. 19)** : En citant Hardy (1988) uniquement comme un précurseur terminologique du *Confused Deputy* sans adopter le modèle des capabilités non forgeables qu'il préconise, l'ouvrage s'enferme dans les apories insolubles des contrôles d'accès par listes (ACL/RBAC).
   - **Absence de protocole formel d'admission KYA (Ch. 18)** : L'ouvrage dresse l'inventaire de 9 chantiers hétérogènes sans formaliser la machine à états finis en cinq phases requise pour l'admission d'un agent tiers au périmètre d'entreprise.

---

## 2. Protocole d'Arbitrage RSA et Évolution Critique

L'arbitrage de Niveau 1 confronte rigoureusement les constats des Candidats 3 et 4 pour forger une revue évoluée de niveau supérieur.

### 2.1 Accords forts corroborés
Les deux analystes convergent sur les constats techniques suivants :
- **Réfutation mathématique de l'impossibilité des deux sauts** : Unanimité sur le fait que la RFC 8693 Section 4.1 ne constitue pas un théorème d'impossibilité et que les modèles par capabilités (Biscuit, Macaroons) garantissent l'opposabilité transitive sous EUF-CMA.
- **Impact volumétrique PQC sur les couches réseau et transport** : Accord sur l'impact critique de la taille des signatures ML-DSA/SLH-DSA sur la MTU Ethernet et le franchissement du plafond de 8 Ko des en-têtes HTTP.
- **Faille structurelle de l'Agentic SOC** : Corroboration du constat de symétrie attaque/défense et de la compromission de l'imputabilité par l'usage de comptes de service statiques permanents.
- **Vulnérabilité MCP Rug-Pull** : Corroboration de l'absence totale de champ d'intégrité (hash/digest) dans le schéma MCP `tools/list` (F-52) face aux mutations dynamiques via `notifications/tools/list_changed`.
- **Contradiction normative A2A** : Corroboration de l'incohérence entre l'interdiction `MUST NOT` d'utiliser des clés révoquées et l'absence complète de point de contrôle de statut (F-07).

### 2.2 Réconciliation des divergences et arbitrages
1. **Sévérité du surcoût PQC (DEF-L2-02 vs D4)** :
   - *Candidat 3* classe le défaut en Bloquant en se focalisant sur l'omission de FIPS 205 et l'incompatibilité HTTP 431.
   - *Candidat 4* le classe en Majeur en ciblant la fragmentation MTU et la dégradation de bande passante MCP.
   - *Arbitrage RSA L1* : Requalification en **Défaut Majeur de Conception d'Architecture Réseau**. Ce n'est pas une impossibilité mathématique (le chiffrement fonctionne), mais un vice d'architecture physique qui paralyse l'infrastructure d'entreprise en production sans découplage par référence déréférençable ou adoption de formats binaires COSE/CBOR.
2. **Défaillances de rendu typographique** :
   - Le Candidat 4 a conduit un balayage visuel minutieux des images de pages, mettant au jour les dislocations critiques du Tableau 16.3 (p. 188), de l'encadré flottant des pp. 242-243, et du Tableau 21.4 (p. 248), ainsi que les ruptures syntaxiques des pages 151, 152 et 153.
   - Le Candidat 3 s'est principalement concentré sur la Figure 12.4 (p. 147) et l'indexation du Tableau 14.2 (p. 164).
   - *Arbitrage RSA L1* : Intégration unifiée de toutes les défaillances graphiques vérifiées. Les dislocations qui brisent la syntaxe logique d'une thèse ou détruisent la substance d'un tableau comparatif sont classées au niveau **Bloquant de composition**, car elles altèrent directement la transmissibilité et la validité du texte.
3. **Apports théoriques complémentaires intégrés** :
   - Intégration de la formalisation du **modèle de capabilités (Hardy 1988)** du Candidat 3 comme contre-mesure structurelle au *Confused Deputy* dans MCP.
   - Intégration de la **spécification procédurale d'admission KYA en 5 phases** issue de l'analyse du Candidat 3.
   - Intégration de la découverte du Candidat 3 relative au **verrou normatif IANA pour les algorithmes PQC dans JOSE/COSE**.
   - Intégration de la réfutation par le Candidat 4 de l'affirmation erronée de la page 200 sur Biscuit.

---

## 3. Matrice Consolidée des Défauts (Bloquant, Majeur, Mineur)

```
+-------------+-----------------------------+----------+---------+-----------------------------------------------------------+
| ID          | Sévérité                    | Chapitre | Page(s) | Nature du défaut consolidé                                |
+-------------+-----------------------------+----------+---------+-----------------------------------------------------------+
| DEF-RSA2-01 | Bloquant (Erreur formelle)  | Ch. 17   | 197-200 | Falsification de l'opposabilité dans les deux sauts       |
| DEF-RSA2-02 | Bloquant (Composition PDF)  | Ch. 16   | 188     | Dislocation destructive du Tableau 16.3 (cellule vide)    |
| DEF-RSA2-03 | Bloquant (Composition PDF)  | Ch. 21   | 242-243 | Collision d'encadré flottant brisant la syntaxe de phrase |
| DEF-RSA2-04 | Majeur (Architecture PQC)   | Ch. 21   | 236-248 | Omission FIPS 205 et impact physique MTU / HTTP 431       |
| DEF-RSA2-05 | Majeur (Composition PDF)    | Ch. 12   | 151     | Troncature abrupte de paragraphe en fin de page           |
| DEF-RSA2-06 | Majeur (Composition PDF)    | Ch. 13   | 152     | Encadré « Thèse » fracturant le corps d'une phrase        |
| DEF-RSA2-07 | Majeur (Composition PDF)    | Ch. 13   | 153     | Encadré d'extraction inséré dans un groupe nominal        |
| DEF-RSA2-08 | Majeur (Composition PDF)    | Ch. 21   | 248     | Fracture et inversion de texte dans le Tableau 21.4       |
| DEF-RSA2-09 | Majeur (Contradiction Norm) | Ch. 15   | 170,224 | Paradoxe MUST NOT sans vérification de statut A2A v1.0    |
| DEF-RSA2-10 | Majeur (Sécurité API)       | Ch. 20   | 222-225 | Absence de hachage d'intégrité et rug-pull dans MCP Tools |
| DEF-RSA2-11 | Majeur (Sécurité Opérat.)   | Ch. 20   | 232-233 | Régression PoLP dans l'Agentic SOC (comptes permanents)   |
| DEF-RSA2-12 | Majeur (Lacune Algorithme)  | Ch. 20   | 228-235 | Vacuité algorithmique de détection sur reasoning graphs   |
| DEF-RSA2-13 | Majeur (Théorie Sécurité)   | Ch. 19   | 216-217 | Méconnaissance de la sécurité par capabilités (Hardy 1988)|
| DEF-RSA2-14 | Majeur (Spécif. Manquante)  | Ch. 18   | 201-209 | Absence de machine d'états d'admission KYA déterministe   |
| DEF-RSA2-15 | Majeur (Standardisation)    | Ch. 21   | 242-245 | Absence de ratification IANA pour PQC dans JOSE/COSE      |
| DEF-RSA2-16 | Mineur (Graphique)          | Ch. 12   | 147     | Troncature textuelle dans la Figure 12.4 (« pour »)       |
| DEF-RSA2-17 | Mineur (Cohérence Index)    | Ch. 14   | 162-164 | Saut d'indexation (Figure 14.1 vs Tableau 14.2)           |
| DEF-RSA2-18 | Mineur (Typographie)        | Ch. 20   | 227     | Ponctuation manquante fusionnant deux phrases (RFC 7662)  |
| DEF-RSA2-19 | Mineur (Obsolescence)       | Ch. 19-20| 212, 222 | Révision MCP 2026-07-28 laissée en « rejeu non fait »     |
| DEF-RSA2-20 | Mineur (Rigueur Corpus)     | Ch. 20   | 226     | Balayage maintenu sur draft AGNTCY -01 au lieu de -02     |
+-------------+-----------------------------+----------+---------+-----------------------------------------------------------+
```

---

### DEF-RSA2-01. [Bloquant / Erreur formelle] Falsification de la prétendue rupture d'opposabilité mathématique dans le problème des deux sauts
- **Localisation** : Chapitre 17, Section 17.6 (« Le problème des deux sauts »), pp. 197-200.
- **Citations textuelles exactes** :
  - p. 198 : *« Ce qui manque au second saut n’est donc pas un détail que la spécification aurait négligé, c’est ce qu’elle a délibérément placé hors de sa portée... la perte ne se produit pas à un rang numéroté, mais au premier changement de régime... "deux sauts" nomme le premier cas de figure où ce changement devient inévitable... aucune des trois pistes n'a fait l'objet d'une démonstration au sens strict »*.
  - p. 199 : *« L’attribut act exprime la chaîne d’acteurs ; il ne démontre pas l’opposabilité de chaque saut auprès d’un tiers indépendant [...] les acteurs intermédiaires sont informational only »*.
  - p. 200 : *« Macaroons et Biscuit atténuent une portée, ils ne portent pas l'identité de chaque maillon que le § 17.6.1 déclare perdue »*.
- **Diagnostic causal approfondi** :
  L'auteur confond une contrainte d'implémentation opérationnelle locale d'une RFC spécifique (RFC 8693 OAuth 2.0 Token Exchange Section 4.1) avec un théorème d'impossibilité mathématique.
  1. La RFC 8693 prescrit que pour un serveur de ressources local *stateless*, l'élément `act` imbriqué est informatif afin d'éviter que le serveur ne prenne des décisions d'autorisation synchrones complexes sur l'ensemble de l'historique amont. Cela n'interdit en aucun cas à un vérificateur global ou à une autorité d'audit d'établir la non-répudiation et l'opposabilité probatoire complète de la chaîne.
  2. L'affirmation selon laquelle *Biscuit* « ne porte pas l'identité de chaque maillon » est **factuellement et mathématiquement fausse**. Dans la spécification formelle de Biscuit (fondée sur la logique Datalog et des signatures asymétriques à clé publique Ed25519), chaque bloc d'atténuation successif est signé cryptographiquement par le délégataire sortant et peut incorporer des faits Datalog liant sans ambiguïté l'identité et la clé publique du maillon délégué suivant :
     $$\text{check if actor}(\text{"agent\_C"}), \text{operation}(\text{"read"})$$
- **Correctif formel et contre-exemple mathématique** :
  Réfuter l'affirmation d'impossibilité structurelle. Énoncer que l'opposabilité se conserve mathématiquement par transitivité sous le modèle standard d'infalsifiabilité existentielle face aux attaques à message choisi (EUF-CMA).
  *Démonstration* : Soit une chaîne de délégation à $n$ sauts $\Delta_n = (D_1, \dots, D_n)$ liant le mandant $A_0$ à l'agent final $A_n$ :
  $$D_k = \text{Sign}_{SK_{k-1}}(A_k \parallel \text{Scope}_k \parallel T_k \parallel H(D_{k-1})) \quad \text{avec} \quad \text{Scope}_k \subseteq \text{Scope}_{k-1}$$
  Un vérificateur indépendant $V$ confronté à $\Delta_n$ vérifie par induction :
  $$\forall k \in [1, n], \quad \text{Verify}_{PK_{k-1}}(D_k) = \text{True} \quad \wedge \quad \text{Scope}_k \subseteq \text{Scope}_{k-1} \quad \wedge \quad t \in \bigcap_{i=1}^n T_i$$
  Sous l'hypothèse de sécurité de la signature sous-jacente, l'avantage de forger un maillon frauduleux est borné par :
  $$\text{Adv}_{\text{Forge}}(\Delta_n) \le \sum_{k=1}^n \text{Adv}_{\text{EUF-CMA}}(A_{k-1}) \le n \cdot \text{negl}(\lambda)$$
  Citer SPKI/SDSI (RFC 2693), Macaroons (Birgisson et al., NDSS 2014) et Biscuit comme contre-exemples de référence prouvant l'opposabilité multi-sauts sans retour au mandant d'origine.

---

### DEF-RSA2-02. [Bloquant / Erreur de composition] Décalage destructif de colonnes et cellules orphelines dans le Tableau 16.3
- **Localisation** : Chapitre 16, Section 16.4, Page 188 (`page-188.png`), Tableau 16.3 (« Trois scénarios de normalisation du passeport d’agent... »).
- **Citation textuelle exacte** :
  Dans la rangée `1 — extension d'un texte de l'IETF` :
  - Colonne « Tri » : *« s de groupe de travail, aucun publié en RFC, aucune date annoncée (F-85)... »*
  - Colonne « Ce sur quoi il s'appuie » : *[Cellule entièrement VIDE — vide de blanc pur]*
- **Diagnostic causal approfondi** :
  Une erreur d'alignement dans le moteur de composition a supprimé la valeur de la colonne « Tri » (qui devait porter la mention `PROJETÉ`), amputé les premiers mots de la description de la colonne 3 (*« 7 Internet-Draft »* tronqué en *« s »*), et injecté tout le texte descriptif de la colonne 3 à l'intérieur de la colonne « Tri ». La colonne 3 se retrouve totalement déserte, détruisant la cohérence de la table.
- **Correctif requis** :
  Restaurer la disposition tabulaire rigoureuse :
  - **Colonne 1 (Scénario)** : `1 — extension d’un texte de l’IETF`
  - **Colonne 2 (Tri)** : `PROJETÉ`
  - **Colonne 3 (Ce sur quoi il s’appuie)** : `7 Internet-Drafts de groupe de travail, aucun publié en RFC, aucune date annoncée (F-85) — huit au 23 octobre 2026, dont un adopté sur les agents d’IA ; intermédiaires d’IA rangés parmi les charges déléguées (F-86) ; appel de dernière relecture sur la propagation de contexte (F-29)`
  - **Colonne 4 (Ce qui le réfuterait)** : `l’adoption d’un document couvrant l’assemblage des quatre pièces, ou au contraire l’expiration de la série sans reprise`

---

### DEF-RSA2-03. [Bloquant / Erreur de composition] Collision d'un encadré flottant brisant la syntaxe d'une phrase entre les pages 242 et 243
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

---

### DEF-RSA2-04. [Majeur / Architecture Réseau & PQC] Omission critique de FIPS 205 (SLH-DSA) et cécité sur l'impact volumétrique des signatures PQC
- **Localisation** : Chapitre 21, Sections 21.1, 21.3 et 21.7, pp. 237-247.
- **Citation textuelle exacte** :
  - p. 237 : *« FIPS 203 (ML-KEM, encapsulation de clé) et FIPS 204 (ML-DSA, signature) sont des normes finales, publiées le 13 août 2024 »*.
  - p. 247 (§ 21.7) : *« les signatures et échanges post-quantiques, dont les tailles d’artefacts sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de main [...] Régime : entrée en [C], et le Vol. I trie lui-même ce verrou SPÉCULATIF ; aucune mesure publique ne le valide à son gel »*.
- **Diagnostic causal approfondi** :
  1. **Omission de FIPS 205** : FIPS 205 (SLH-DSA, ex-SPHINCS+) est le standard de signature post-quantique sans réseau euclidien (reposant uniquement sur les fonctions de hachage) promulgué par le NIST le même jour (13 août 2024). C'est le standard de repli universel indispensable en cas de percée cryptanalytique sur les réseaux euclidiens (Module-LWE / ML-DSA).
  2. **Déni de mesure sur les tailles d'artefacts** : L'auteur traite l'explosion volumétrique comme un verrou « spéculatif sans mesure publique ». Or, les spécifications finales du NIST fixent exactement ces grandeurs :
     - Ed25519 classique : Clé publique = 32 octets, Signature = 64 octets.
     - ML-DSA-44 (NIST Niveau 2) : Clé publique = 1 312 octets, Signature = 2 420 octets.
     - ML-DSA-65 (NIST Niveau 3) : Clé publique = 1 952 octets, Signature = 3 309 octets.
     - ML-DSA-87 (NIST Niveau 5) : Clé publique = 2 592 octets, Signature = 4 627 octets.
     - SLH-DSA-SHA2-128s (FIPS 205) : Clé publique = 32 octets, Signature = 7 856 octets.
     - SLH-DSA-SHA2-256s (FIPS 205) : Clé publique = 64 octets, Signature = 29 792 octets.
  3. **Rupture d'infrastructure réseau et HTTP** :
     - *Dépassement de MTU* : La MTU Ethernet standard étant de 1 500 octets (MSS TCP = 1 460 octets), toute signature ML-DSA-44 ou SLH-DSA force une fragmentation IP/TCP immédiate (2 à 21 segments par signature), dégradant la latence et la fiabilité des RPC multi-agents.
     - *Saturation des en-têtes HTTP (HTTP 431)* : Un jeton JWT/JWS encapsulant une signature ML-DSA-65 encodée en Base64URL atteint ~4,5 Ko. Dès qu'une chaîne de délégation compte deux ou trois signatures imbriquées, ou en mode hybride (Ed25519 + ML-DSA), l'en-tête `Authorization: Bearer <token>` dépasse 8 Ko à 14 Ko. Or, les passerelles d'API et proxys d'entreprise (ALB AWS, Envoy, Nginx) rejettent par défaut les requêtes excédant 8 Ko via l'erreur fatale `HTTP 431 Request Header Fields Too Large`.
- **Correctif formel et prescription d'ingénierie** :
  Intégrer formellement FIPS 205 dans le corps du texte. Modéliser l'impact volumétrique et prescrire les deux architectures de remédiation nécessaires :
  - **Découplage de transport** : Ne plus transmettre les signatures complètes dans les en-têtes de requêtes synchrones, mais des identifiants d'artefacts déréférençables hors bande via un cache d'attestations vérifié.
  - **Compactage binaire** : Remplacer l'encodage textuel JSON/Base64 par des conteneurs binaires compacts CBOR Web Tokens (CWT) et signatures COSE (RFC 9052 / RFC 9053).

---

### DEF-RSA2-05. [Majeur / Erreur de composition] Troncature abrupte de paragraphe en pied de page 151
- **Localisation** : Chapitre 12, Section 12.4, Page 151 (`page-151.png`).
- **Citation textuelle exacte** :
  - p. 151 : *« L’ordre des faits est donc celui-ci, et il est daté du 21 juillet 2026 : un produit en disponibilité générale étend des RFC (Vol. III H-02 ; F-33) ; un document »* [Texte coupé net sans point final ni suite].
- **Diagnostic causal approfondi** :
  Dépassement de la grille verticale de mise en page ayant tronqué la phrase de conclusion du paragraphe. La transition vers le paragraphe suivant (*« Ce qui manque à cet inventaire... »*) s'effectue sur une phrase inachevée.
- **Correctif requis** :
  Restituer la fin de la proposition tronquée (précisant la nature du document en question) et rétablir la ponctuation finale.

---

### DEF-RSA2-06. [Majeur / Erreur de composition] Encadré « Thèse » inséré en plein milieu d'une phrase en page 152
- **Localisation** : Chapitre 13, Section 13.0, Page 152 (`page-152.png`).
- **Citation textuelle exacte** :
  - p. 152 : *« au titre d’une / [ENCADRÉ THÈSE] / section, ne le définit ni ne le réemploie dans le corps de celle-ci... »*
- **Diagnostic causal approfondi** :
  La boîte de texte flottante contenant la thèse du Chapitre 13 a été injectée au milieu de la proposition subordonnée *« au titre d'une section... »*, provoquant une rupture syntaxique grossière.
- **Correctif requis** :
  Repositionner l'encadré de thèse en tête de chapitre, sous le titre principal et avant le premier paragraphe de la section 13.0.

---

### DEF-RSA2-07. [Majeur / Erreur de composition] Encadré d'extraction inséré dans un groupe nominal en page 153
- **Localisation** : Chapitre 13, Section 13.1, Page 153 (`page-153.png`).
- **Citation textuelle exacte** :
  - p. 153 : *« La Recommandation en admet deux familles, non une : la preuve / [ENCADRÉ EXTRACTION CONDUITE LE 30 JUILLET 2026...] / incorporée, portée par la propriété proof... »*
- **Diagnostic causal approfondi** :
  L'encadré de traçabilité documentaire a été positionné entre le nom *« la preuve »* et son adjectif *« incorporée »*, brisant le syntagme nominal de définition technique.
- **Correctif requis** :
  Déplacer l'encadré d'extraction en bas de page ou en note marginale pour préserver l'intégrité de la phrase technique.

---

### DEF-RSA2-08. [Majeur / Erreur de composition] Fracture et inversion de texte dans le Tableau 21.4
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

---

### DEF-RSA2-09. [Majeur / Contradiction Normative] Paradoxe de l'interdiction MUST NOT sans vérification de statut dans A2A v1.0.0
- **Localisation** : Chapitre 15, Section 15.1.3 et Chapitre 20, Section 20.2, pp. 170, 223-224.
- **Citations textuelles exactes** :
  - p. 224 : *« l’interdiction d’employer une clé expirée ou révoquée y est pourtant posée au niveau normatif le plus fort [MUST NOT], sans aucun moyen permettant au client de l’établir (F-07, [A]) »*.
  - p. 170 : *« Les cartes MAY être signées ; les clients SHOULD vérifier au moins une signature (F-04, [A]) »*.
- **Diagnostic causal approfondi** :
  Le standard A2A v1.0.0 crée une impossibilité juridique et technique : il impose une interdiction absolue (`MUST NOT`) d'utiliser une clé expirée ou révoquée, tout en omettant de définir le moindre point de terminaison ou protocole de contrôle d'état (absence de liste de révocation, de point d'introspection ou d'annuaire OCSP). L'apposition même de la signature étant purement facultative (`MAY`), la chaîne d'opposabilité s'effondre en pratique.
- **Correctif requis** :
  Formuler une exigence d'extension d'architecture imposant l'adjonction d'un mécanisme de vérification d'état cryptographique (ex. profil W3C Bitstring Status List v1.0 ou RFC 7662) pour conditionner l'admission d'une Agent Card dans un domaine financier.

---

### DEF-RSA2-10. [Majeur / Sécurité des API] Absence de hachage d'intégrité et risque de Rug-Pull dans Model Context Protocol (MCP)
- **Localisation** : Chapitre 20, Sections 20.1 et 20.3, pp. 222-225.
- **Citations textuelles exactes** :
  - p. 222 : *« l’énumération du type de données correspondant compte huit champs, dont aucun n’exprime une version, une empreinte cryptographique ou une signature (F-52, [B]) »*.
  - p. 223 : *« le retournement [...] exploite le fait que la décision d’invocation s’appuie sur un objet que le protocole autorise à changer après l’octroi de la confiance, sans prescrire de le relier à ce qui avait été consenti »*.
- **Diagnostic causal approfondi** :
  Le protocole MCP (révision 2025-11-25) autorise un serveur d'outils à notifier dynamiquement une modification de sa liste de primitives via `notifications/tools/list_changed` sans exiger le moindre condensat cryptographique (`tool_digest`) ni signature. Un outil consenti au démarrage peut être substitué par une charge malveillante (*tool-squatting / rug-pull*) sans rupture protocolaire.
- **Correctif requis** :
  Définir une extension d'intégrité liant chaque primitive d'outil à une empreinte canonique immuable :
  $$\mathcal{H}_{\text{tool}} = \text{SHA-256}(\text{JCS}(\text{name} \parallel \text{description} \parallel \text{inputSchema}))$$
  Cette empreinte doit être scellée dans le jeton d'autorisation de l'agent appelant à l'instant de consentement.

---

### DEF-RSA2-11. [Majeur / Sécurité Opérationnelle] Régression du principe de moindre privilège (PoLP) dans l'Agentic SOC
- **Localisation** : Chapitre 20, Section 20.9, pp. 232-233.
- **Citations textuelles exactes** :
  - p. 232 : *« The agent’s specified user identity isn’t compatible with PIM or TAP because they don’t support long-term background operations (F-57, [A]) »*.
  - *« Le privilège de l’agent défensif est alors permanent par construction, et le journal porte l’identité du compte, non celle du mandataire qui a agi »*.
- **Diagnostic causal approfondi** :
  L'implémentation officielle de Microsoft Defender pour l'agent de tri d'alertes avoue que l'agent ne peut pas opérer avec les mécanismes de privilèges juste-à-temps (PIM - *Privileged Identity Management*) ou les passes d'accès temporaires (TAP). Pour assurer son exécution en arrière-plan, l'agent doit hériter d'un compte utilisateur doté de privilèges permanents. Cette conception viole frontalement le principe de moindre privilège (PoLP), supprime l'imputabilité individuelle dans les journaux d'audit et expose l'infrastructure défensive à un détournement de privilèges majeurs en cas d'injection indirecte.
- **Correctif requis** :
  Proscrire l'usage de comptes utilisateurs permanents pour les agents d'arrière-plan. Prescrire une architecture fondée sur des identités de charge de travail (*Workload Identity Federation*) associées à des jetons d'accès éphémères (durée $\le 15$ minutes) renouvelés sous attestation cryptographique de code d'enclave.

---

### DEF-RSA2-12. [Majeur / Lacune Algorithmique] Vacuité algorithmique de la détection et du confinement dans l'Agentic SOC
- **Localisation** : Chapitre 20, Sections 20.7 à 20.10, pp. 228-235.
- **Citations textuelles exactes** :
  - p. 231 : *« Ce rapport reprend par ailleurs des métriques auto-déclarées d’éditeur, dont le présent chapitre ne reprend aucune »*.
  - p. 233 : *« Lecture de l’auteur — ce qu’il n’établit pas : qu’un centre d’opérations agentique se range en "gouvernable" ou "ingouvernable"... »*.
- **Diagnostic causal approfondi** :
  Alors que le chapitre promet le traitement de la boucle défensive, il se borne à un constat passif d'exposition symétrique à la triade de Willison et à une critique des fiches commerciales d'éditeurs (Microsoft, Google Cloud, CrowdStrike). Il n'articule aucune métrique formelle, aucun algorithme de détection d'anomalies sur les graphes de raisonnement (*reasoning graphs*), et aucun protocole d'isolation ou d'expulsion de sous-graphes compromis.
- **Correctif formel requis** :
  Formaliser les primitives opérationnelles de la boucle défensive :
  1. *Métrique de dérive de raisonnement* : Calcul de la distance d'édition de graphe d'exécution par rapport à un profil d'étalonnage nominal :
     $$\mathcal{D}(G_t, G_{\text{ref}}) = \frac{\text{GraphEditDist}(G_t, G_{\text{ref}})}{|V_t| + |E_t|}$$
  2. *Détection d'anomalies* : Détection des bifurcations anormales de flux d'appels d'outils via plongement temporel de graphe (Temporal Graph Neural Networks / GNN).
  3. *Protocole d'expulsion déterministe* : Révocation cryptographique immédiate de la session d'agent au PEP (*Policy Enforcement Point*), blocage de la paire de clés éphémères au niveau de la passerelle de maillage, et mise en quarantaine des artefacts mémoriels contaminés.

---

### DEF-RSA2-13. [Majeur / Théorie de la Sécurité] Méconnaissance de la solution par capabilités (Hardy 1988) face au délégué confus
- **Localisation** : Chapitre 19, Section 19.3, pp. 216-217.
- **Citation textuelle exacte** :
  - p. 216 : *« Norm Hardy (1988), The Confused Deputy (or why capabilities might have been invented)... nomme le patron dont toute cette taxonomie est une réinstanciation... »*.
- **Diagnostic causal approfondi** :
  L'auteur cite l'article historique de Hardy (1988) comme un simple argument d'autorité terminologique, sans intégrer la thèse technique centrale de l'article : la faille du *Confused Deputy* provient structurellement de la dissociation entre la désignation de la ressource et l'autorité d'y accéder (inhérente aux listes de contrôle d'accès ACL et aux rôles RBAC). En restant cantonné au paradigme de l'identité et des listes de privilèges, le Compendium ne résout pas la confusion de délégué pour les agents autonomes.
- **Correctif conceptuel requis** :
  Substituer la perspective ACL par le paradigme des **Object-Capabilities** : une référence d'outil doit être un triplet cryptographique indivisible :
  $$\mathcal{C} = \langle \text{URI}_{\text{outil}}, \text{AttenuatedPermissions}, \text{ProofOfPossession} \rangle$$
  L'agent mandataire ne détient aucun droit autonome global ; il ne peut agir que dans la stricte limite de la capabilité non forgeable qui lui a été expressément transmise par son mandant.

---

### DEF-RSA2-14. [Majeur / Spécification Manquante] Absence de spécification procédurale d'un protocole d'admission KYA déterministe
- **Localisation** : Chapitre 18, Sections 18.1 à 18.6, pp. 201-209.
- **Citation textuelle exacte** :
  - p. 202 : *« Le KYA transpose la logique du KYC — vérifier avant d’admettre — sans l’infrastructure institutionnelle qui rend le KYC possible... »*.
- **Diagnostic causal approfondi** :
  Après avoir dressé l'inventaire pertinent de 9 chantiers pré-normatifs disparates (DIF, Akamai, W3C, AGNTCY, OpenID), l'ouvrage n'articule aucune séquence algorithmique permettant à une passerelle d'entreprise d'exécuter la vérification d'un agent tiers lors de sa demande d'admission.
- **Correctif procédural requis** :
  Définir la machine à états d'admission KYA en 5 phases séquentielles :
  1. *Présentation* : Réception de l'Agent Card signée et des accréditations vérifiables W3C VC 2.0.
  2. *Résolution d'identité* : Résolution décentralisée du DID de l'agent et extraction de sa clé publique racine.
  3. *Contrôle de fraîcheur d'état* : Interrogation synchrone d'une liste de révocation cryptographique (W3C Bitstring Status List v1.0).
  4. *Vérification d'intégrité de charge* : Validation des attestations d'enclave sécurisée (TEE / vLEI).
  5. *Émission d'autorité locale* : Octroi d'un jeton de session éphémère ($T_{\text{exp}} \le 1\text{ h}$) lié à une clé de preuve de possession DPoP (RFC 9449).

---

### DEF-RSA2-15. [Majeur / Standardisation Cryptographique] Verrou normatif de l'absence de ratification IANA pour les algorithmes PQC dans JOSE/COSE
- **Localisation** : Chapitre 21, Section 21.5, pp. 242-245.
- **Citation textuelle exacte** :
  - p. 244 : *« La carte signée dispose d’un point où l’algorithme est déclaré, et ce point est obligatoire (F-03)... »*.
- **Diagnostic causal approfondi** :
  L'auteur affirme que l'Agent Card A2A est crypto-agile au motif que le champ `alg` de l'en-tête JWS (RFC 7515) permet de déclarer un nouvel algorithme. Cette assertion ignore le verrou normatif déterminant : au registre officiel de l'IANA pour JOSE et COSE, **aucun identifiant standard d'algorithme n'est ratifié pour ML-DSA ou SLH-DSA**. Les travaux IETF correspondants (`draft-ietf-cose-dilithium`, etc.) demeurent à l'état de brouillons non ratifiés. Dès lors, toute implémentation post-quantique d'une Agent Card reste confinée à des accords bilatéraux propriétaires non interopérables.
- **Correctif normatif requis** :
  Relever explicitement l'absence d'identifiants IANA ratifiés comme un verrou bloquant l'interopérabilité PQC industrielle des Agent Cards.

---

### DEF-RSA2-16. [Mineur / Rendu Graphique] Troncature textuelle dans la Figure 12.4
- **Localisation** : Chapitre 12, Page 147 (`page-147.png`), Figure 12.4.
- **Citation textuelle exacte** :
  Dans la colonne gauche (« L'agent comme client ») :
  *« « Une application qui demande des ressources protégées pour »* [Texte coupé net sans suite].
- **Diagnostic causal approfondi** :
  La définition de « client » extraite de la RFC 6749 Section 1.1 a été coupée par la boîte de rendu graphique au mot « pour ».
- **Correctif requis** :
  Rétablir la définition intégrale de la RFC 6749 : *« Une application qui demande des ressources protégées pour le compte du détenteur de ressource et avec son autorisation. »*

---

### DEF-RSA2-17. [Mineur / Cohérence Éditoriale] Discordance typologique et saut d'indexation Figure 14.1 / Tableau 14.2
- **Localisation** : Chapitre 14, Sections 14.1 et 14.2, pp. 162-164 (`page-162.png` et `page-164.png`).
- **Citation textuelle exacte** :
  - p. 162 : *« Figure 14.1 — La grille des cinq questions, et ce que chacune exige d’un mécanisme »*.
  - p. 164 : *« Tableau 14.2 — Application-témoin de la grille à trois mécanismes... »*.
- **Diagnostic causal approfondi** :
  L'encadré de la page 162 est structuré sous forme de tableau comparatif mais est étiqueté « Figure 14.1 ». Le tableau suivant en page 164 est nommé « Tableau 14.2 », ce qui supprime le « Tableau 14.1 » de la séquence des tableaux.
- **Correctif requis** :
  Renommer « Figure 14.1 » en « Tableau 14.1 » pour assurer la continuité de numérotation.

---

### DEF-RSA2-18. [Mineur / Typographie] Ponctuation manquante fusionnant deux phrases au sujet de la RFC 7662
- **Localisation** : Chapitre 20, Section 20.4, Page 227 (`page-227.png`), 3e paragraphe.
- **Citation textuelle exacte** :
  *« ...elle permet à celui qui reçoit un jeton de demander s’il vaut encore L’asymétrie tient — mais elle n’était pas complète... »*.
- **Diagnostic causal approfondi** :
  Omission du point final entre « encore » et « L'asymétrie », fusionnant deux propositions distinctes.
- **Correctif requis** :
  Corriger par : *« ...de demander s'il vaut encore. L'asymétrie tient — mais elle n'était pas complète... »*.

---

### DEF-RSA2-19. [Mineur / Obsolescence Documentaire] Maintien de la clause « rejeu non fait » sur la révision MCP 2026-07-28
- **Localisation** : Chapitre 19, p. 212 et Chapitre 20, p. 222.
- **Citation textuelle exacte** :
  *« Publiée le 28 juillet 2026 (2026-07-28, constat du 23 octobre) ; rejeu non fait : cette section et la rangée "Jeton — MCP" du § 20.4 restent bornées à la révision 2025-11-25 »*.
- **Diagnostic causal approfondi** :
  Pour un ouvrage finalisé et compilé fin octobre 2026, maintenir l'analyse de sécurité sur une révision vieille de neuf mois en déclarant le rejeu non fait affaiblit l'actualité de l'audit.
- **Correctif requis** :
  Intégrer les apports stabilisés de la révision MCP du 28 juillet 2026 (refonte de la gestion d'état et profils d'autorisation).

---

### DEF-RSA2-20. [Mineur / Rigueur de Corpus] Maintien d'un balayage sur draft AGNTCY obsolète
- **Localisation** : Chapitre 20, Section 20.4, p. 226.
- **Citation textuelle exacte** :
  *« Internet-Draft draft-mp-agntcy-ads, de soumission individuelle ; balayage sur la révision -01, supplantée par la -02 du 6 juillet 2026, non rebalayée »*.
- **Diagnostic causal approfondi** :
  La révision -02 était disponible plusieurs semaines avant la date de gel documentaire du 27 juillet 2026.
- **Correctif requis** :
  Valider le balayage sur la version draft-mp-agntcy-ads-02 pour confirmer la persistance de l'absence de primitives de révocation dans l'annuaire ADS.

---

## 4. Analyse Critique Approfondie par Chapitre (Ch. 12 à 21 + amorce Ch. 22)

### S14 : L'héritage étiré et l'identité décentralisée (Ch. 12 & Ch. 13, pp. 144-159)
- **Crise de la pile IAM pré-agentique (OAuth 2.0 & SCIM)** :
  Le chapitre 12 démontre rigoureusement l'aporie fondamentale qui frappe l'adaptation des protocoles web historiques. Dans la RFC 6749, l'agent autonome ne peut être ni un simple `client` (car il requiert alors un consentement interactif via `user-agent` incompatible avec les tâches autonomes *Human-Not-Present*), ni un `resource owner`. S'il utilise le flux `client_credentials` (§4.4), il opère sous une identité de service statique, créant l'écart d'attribution (*attribution gap*) identifié par l'OWASP (ASI03). Quant à SCIM 2.0 (RFC 7643), l'absence de schéma pour mandataires autonomes est solidement établie au degré 1.
- **Limites institutionnelles de W3C VC 2.0 et DID v1.0/v1.1 (Ch. 13)** :
  L'auteur confronte judicieusement le statut de Recommandation W3C du Verifiable Credentials Data Model v2.0 (mai 2025) à son absence d'adoption en production bancaire. La cryptographie existe (Data Integrity, SD-JWT-VC), mais la fédération de gouvernance fait défaut, à l'exception du vLEI (GLEIF).
- **Défaillances matérielles** : Troncatures et collisions de mise en page (Défauts DEF-RSA2-05, DEF-RSA2-06, DEF-RSA2-07, DEF-RSA2-16).

### S15 & S16 : La grille des cinq questions, Agent Card A2A et annuaires d'agents (Ch. 14 & Ch. 15, pp. 160-179)
- **Puissance analytique de la grille Q-A à Q-E (Ch. 14)** :
  L'application-témoin (Tableau 14.2) montre que sur 15 cellules évaluées, aucun mécanisme contemporain ne répond aux cinq exigences (8 réponses partielles, 7 silences complets). L'auteur prouve que le défaut de réponse à Q-A (*Qui es-tu ?*) prive de fondement Q-D (*Que peux-tu faire ?*) et Q-E (*Qui en répond ?*).
- **Fragilité temporelle de l'Agent Card A2A v1.0.0 (Ch. 15)** :
  L'audit technique du format JWS sous JCS (RFC 8785) démontre la précarité de l'artefact : signature facultative (`MAY`), absence de champs temporels (`iat`, `exp`, `nbf`) dans l'en-tête protégé, ancrage de confiance renvoyé hors protocole et contradiction sur les clés expirées (DEF-RSA2-09).
- **Fracture architecturale des annuaires commerciaux (Entra Agent ID)** :
  L'analyse met au jour le cloisonnement étanche entre les identités d'agent et les comptes utilisateurs dans Entra Agent ID, autorisant des fuites de périmètre où un agent contourne les contrôles contextuels appliqués aux humains.

### S17 : Le Passeport d'agent : anatomie d'un artefact virtuel (Ch. 16, pp. 180-188)
- **Déconstruction lucide de la synthèse quadripartite** :
  L'auteur formalise le passeport comme une construction d'auteur intégrant la carte d'agent, le registre gouverné, la chaîne de mandat et les attestations réglementaires. Il formule une thèse capitale : *« l'assemblage n'est pas une somme »*. Aucune des composantes ne supplée aux carences de l'autre.
- **Défaillance matérielle** : La dislocation du Tableau 16.3 en page 188 (DEF-RSA2-02) compromet gravement la lisibilité de cette démonstration.

### S18 : La chaîne de mandat et réfutation du problème des deux sauts (Ch. 17, pp. 189-200)
- **Réfutation de la rupture d'opposabilité** :
  L'affirmation d'une impossibilité mathématique de préserver l'opposabilité au-delà de deux sauts constitue l'erreur formelle majeure du Livre II (DEF-RSA2-01). L'opposabilité est mathématiquement préservée sous EUF-CMA dès lors que chaque délégation lie cryptographiquement l'identité du délégué et restreint les prérogatives de manière monotone.
- **Pertinence de l'analyse du biais d'automatisation (§17.4-17.5)** :
  L'auteur expose avec acuité l'angle mort de l'article 12.1 de la Loi 25 québécoise et de la ligne directrice BSIF E-23 : ces textes exigent une révision humaine sans jamais spécifier le format probatoire de cette supervision, générant le phénomène de « tamponnage machinal ».

### S19 & S20 : KYA, taxonomie des attaques et Rug-Pull MCP (Ch. 18, 19 & 20, pp. 201-227)
- **Taxonomie des attaques (Ch. 19)** :
  L'alignement avec MITRE ATLAS (AML.T0104, AML.T0053), la campagne UNC6395 (vol de jetons porteurs), l'injection indirecte d'invites (AgentPoison NeurIPS 2024) et la triade de Willison est remarquable. Cependant, l'impasse sur le modèle de capabilités de Hardy (DEF-RSA2-13) laisse le problème du *Confused Deputy* sans remédiation architecturale.
- **Le Rug-Pull MCP (Ch. 20)** :
  La découverte de l'absence de tout condensat d'intégrité dans le schéma MCP `tools/list` (DEF-RSA2-10) face à la notification `list_changed` constitue un apport critique majeur.
- **Inventaire de la révocation (Tableau 20.1)** :
  Démonstration limpide de l'abandon de la fraîcheur d'état en production, corroborée par l'abandon d'OCSP par Let's Encrypt le 6 août 2025.

### S21 : L'Agentic SOC : promesse vs réalité (Ch. 20, pp. 228-235)
- **Exposition symétrique et régression de sécurité** :
  L'auteur démontre que les agents défensifs ingèrent des données hautement non fiables (courriels de phishing, logs bruts) et s'exposent directement à l'injection indirecte. L'aveu de Microsoft concernant l'incompatibilité avec PIM/TAP (DEF-RSA2-11) détruit le principe de moindre privilège. Néanmoins, l'absence d'algorithmes de détection sur reasoning graphs (DEF-RSA2-12) laisse la boucle défensive sans contenu opérationnel.

### S22 & S23 : Horloge post-quantique, crypto-agilité et orchestration OO1-OO4 (Ch. 21 & Ch. 22, pp. 236-255)
- **Rigueur chronologique NIST et risque Harvest Now, Forge Later** :
  La clarification des jalons (NIST IR 8547, Décret US 14412, OMB M-26-15, ITSM.40.001) et du risque de falsification rétroactive des signatures d'identité est exemplaire.
- **Failles d'ingénierie et de rendu** :
  L'omission de FIPS 205 et des impacts MTU/HTTP 431 (DEF-RSA2-04), l'impasse IANA JOSE/COSE (DEF-RSA2-15), la collision de l'encadré flottant des pp. 242-243 (DEF-RSA2-03) et la dislocation du Tableau 21.4 (DEF-RSA2-08) affaiblissent l'analyse.
- **Transition vers le Livre III (Ch. 22, pp. 252-255)** :
  L'introduction de la taxonomie OO1-OO4 (TU Munich, Rinderle-Ma & Mangler 2026) isole parfaitement la discontinuité critique **OO2 $\to$ OO3**, où l'inversion de contrôle au profit d'un moteur déterministe devient la condition *sine qua non* d'admissibilité réglementaire en finance.

---

## 5. Synthèse Bibliographique et Conformité à l'État de l'Art (2024-2026)

Le tableau ci-dessous confronte les affirmations et références du Livre II à l'état réel des normes et publications à date de novembre 2026 :

```
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
| Référence / Texte normatif         | Date officielle| Statut documentaire réel  | Évaluation critique dans le Compendium                    |
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
| NIST FIPS 203 (ML-KEM)             | 13 août 2024   | Norme FIPS finale         | Cité exactement (§ 21.1) ; avis d'errata bien documenté.  |
| NIST FIPS 204 (ML-DSA)             | 13 août 2024   | Norme FIPS finale         | Cité (§ 21.1) ; omission de l'impact taille signature.   |
| NIST FIPS 205 (SLH-DSA)            | 13 août 2024   | Norme FIPS finale         | OMISSION TOTALE dans le corps du Ch. 21.                  |
| NIST IR 8547 (PQC Transition)      | Nov. 2024      | Projet public initial     | Parfaitement qualifié en « PROJETÉ » (§ 21.1).            |
| Décret présidentiel US 14412       | 22 juin 2026   | Décret exécutif en vigueur| Correctement qualifié « PROGRAMMÉ » (§ 21.1).             |
| Mémorandum exécutif OMB M-26-15    | 24 juin 2026   | Directive fédérale active | Articulé avec exactitude sur les échéances 2030/2031.     |
| CCCS ITSM.40.001 (Canada)          | 23 juin 2025   | Guide d'orientation       | Bien analysé ; défiguré par dislocation du Tableau 21.4.  |
| RFC 8693 (OAuth Token Exchange)    | Janvier 2020   | Proposed Standard (IETF)  | Surinterprété au § 17.6 (erreur d'impossibilité formelle).|
| RFC 9635 (GNAP)                    | Octobre 2024   | Proposed Standard (IETF)  | Mentionné brièvement p. 199 ; non exploité en contre-ex.  |
| RFC 9449 (DPoP)                    | Septembre 2023 | Proposed Standard (IETF)  | Négligé face à la vulnérabilité des jetons porteurs.      |
| RFC 7662 (Token Introspection)     | Octobre 2015   | Proposed Standard (IETF)  | Ajouté le 30 juillet 2026 ; coquille ponctuation p. 227.  |
| W3C Verifiable Credentials v2.0    | 15 mai 2025    | W3C Recommendation        | Parfaitement identifié ; lacune d'implémentation bancaire |
| W3C Decentralized Identifiers v1.1 | 5 mars 2026    | Candidate Recommendation  | Bien instruit (§ 13.1) ; fait négatif de méthode validé.  |
| Linux Foundation A2A v1.0.0        | 12 mars 2026   | Spécification publiée     | Analyse rigoureuse des faiblesses JWS/JCS.                |
| Model Context Protocol (MCP)       | 25 nov. 2025   | Spécification de facto    | Analyse remarquable de F-52 ; obsolescence du rejeu.      |
| Biscuit Token Specification        | 2022-2026      | Standard ouvert           | Faussement déclaré démuni d'identité de maillon (p. 200). |
| Macaroons (Birgisson et al.)       | NDSS 2014      | Conférence à comité       | Bien mobilisé p. 199 ; preuve d'opposabilité multi-sauts. |
| Norm Hardy (Confused Deputy)       | 1988           | Article fondateur         | Réduit à un label ; modèle capabilités éludé (§ 19.3).   |
| OWASP Top 10 Agentic Apps 2026     | Décembre 2025  | Référentiel de sécurité   | Catégorie ASI03 parfaitement corroborée.                  |
| MITRE ATLAS v2026.06 / v2026.09    | Juin/Sept 2026 | Base de connaissances     | Techniques AML.T0104 et AML.T0053 rigoureusement citées. |
| AgentPoison (NeurIPS 2024)         | Décembre 2024  | Conférence révisée        | Modèle d'empoisonnement RAG parfaitement exploité (§ 19.1) |
| TU Munich (Rinderle-Ma & Mangler)   | 30 juin 2026   | Prépublication académique | Taxonomie OO1-OO4 exploitée avec une grande rigueur.       |
+------------------------------------+----------------+---------------------------+-----------------------------------------------------------+
```

---

## 6. Protocole de Vérification Indépendante et Audit Reproductible

Pour auditer et vérifier de façon reproductible les constats du présent rapport :

1. **Vérification de la fausseté de l'impossibilité des deux sauts (DEF-RSA2-01)** :
   - Consulter la spécification officielle de Biscuit (`biscuit-auth`) : vérifier qu'un token Biscuit permet d'ajouter un bloc Datalog signé avec une clé Ed25519 contenant la clause d'autorité :
     `check if actor("agent_C"), operation("read")`
   - Ce mécanisme démontre formellement la non-répudiation et l'opposabilité de chaque maillon intermédiaire, réfutant l'affirmation de la page 200.
2. **Vérification de la dislocation du Tableau 16.3 (DEF-RSA2-02)** :
   - Inspecter l'image `documents/scratch/document_pages/page-188.png`.
   - Constater que la colonne « Tri » contient le texte tronqué débutant par *« s de groupe de travail... »* et que la colonne « Ce sur quoi il s'appuie » est totalement vide de blanc.
3. **Vérification de la collision flottante des pages 242-243 (DEF-RSA2-03)** :
   - Inspecter `documents/scratch/document_pages/page-242.png` et `page-243.png`.
   - Observer en pied de page 242 la rupture `tri :` suivie de l'encadré en gras de 16 lignes, et la reprise déconnectée `fait PROJETÉ` en tête de page 243.
4. **Vérification de la taille des artefacts PQC et fragmentation réseau (DEF-RSA2-04)** :
   - Consulter la norme NIST FIPS 204 (Tableaux 1 et 2) : vérifier que la signature ML-DSA-44 mesure 2 420 octets, excédant la MTU Ethernet de 1 500 octets.
   - Consulter la norme NIST FIPS 205 (Tableau 1) : vérifier que la signature SLH-DSA-SHA2-128s mesure 7 856 octets.
   - Calculer la taille d'un jeton HTTP portant 3 signatures imbriquées ML-DSA : $> 3 \times 2\,420 \times 1{,}33 \approx 9{,}6$ Ko, provoquant l'erreur HTTP 431 sur passerelle Nginx/Envoy standard (seuil à 8 Ko).
5. **Vérification des ruptures de paragraphes et d'encadrés (DEF-RSA2-05, DEF-RSA2-06, DEF-RSA2-07, DEF-RSA2-08, DEF-RSA2-16)** :
   - Inspecter `page-151.png` : fin de paragraphe tronquée net à *« ; un document »*.
   - Inspecter `page-152.png` : encadré inséré entre *« au titre d'une »* et *« section »*.
   - Inspecter `page-153.png` : encadré inséré entre *« la preuve »* et *« incorporée »*.
   - Inspecter `page-248.png` : en-tête déstructuré et colonne 3 vide sur toutes les données.
   - Inspecter `page-147.png` : colonne gauche de Figure 12.4 tronquée au mot *« pour »*.

---
*Rapport d'audit contradictoire évolué L1_2 finalisé le 3 novembre 2026 par Review Aggregator 2.*
