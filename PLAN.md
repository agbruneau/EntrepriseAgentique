# Plan d'exécution des corrections — Entreprise Agentique (`PLAN.md`)

Ce plan structure la résolution exhaustive des constats relevés lors de l'audit des six fichiers du dépôt ([README.md](README.md), [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf), [Veille Technologique.pdf](Veille%20Technologique.pdf), [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf), [Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf](Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) et [Compendium.pdf](Compendium.pdf)).

---

## 0. Prérequis d'architecture documentaire

Ce dépôt ne contient que les PDF compilés et [README.md](README.md). L'exécution s'articule donc sur deux environnements :

1. **Environnement source (dépôt de rédaction amont)** :
   - Sources Typst (`Typst 0.14.2` / `0.15.1`) de `Compendium.pdf`, `Veille Technologique.pdf` et `Revue de littérature.pdf`, incluant les scripts `build/assemble-bibliographie.py`, `check-compendium.py` et `PRD/check-sieges.py`.
   - Source HTML/CSS (rendu Chromium) de `Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf`.
   - Source `NiveauMaturité.html` de `NiveauMaturité.pdf` (récupérable directement dans ce dépôt via `git show 4457a54:NiveauMaturité.html`).
2. **Environnement de publication (ce dépôt)** :
   - Réception des 5 PDF recompilés, mise à jour de [README.md](README.md) et exécution du script de vérification finale avant `git push origin main`.

---

## Vue synoptique des chantiers et priorités

| Priorité | Chantier | Livrable(s) cible(s) | Volume d'anomalies traitées |
| :---: | :--- | :--- | :--- |
| **P1** | Assainissement éditorial et bibliographique du Compendium | [Compendium.pdf](Compendium.pdf) | 50 bandeaux d'audit, 26 `☐`, 148 `☑`, 483 `⚠`, 58 notes infiltrées en Annexe I.1, doublons bibliographiques, erreur CRR3 `2024/1619`, Annexes A–H absentes, en-têtes tronqués |
| **P2** | Corrections cryptographiques et formelles du Cadre de référence | [Cadre de Référence](Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) | Condensé `SHA-256` erroné (C.6/C.7), coupures de lignes JSON (Annexe C), accent de l'auteur (`André-Guy Bruneau`) |
| **P3** | Nettoyage de la Veille technologique et de la Revue de littérature | [Veille Technologique.pdf](Veille%20Technologique.pdf), [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf) | 140 `et al..` + 3 `..`, 19 `☑`, 193 `⚠`, § 13 anachronique (Tableaux 15 et 16), page 145 veuve, justification du résumé p. 1 |
| **P4** | Mise à niveau des métadonnées, signets et typographie | [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf) | Attribution auteur/date/version, signets PDF (`TOC`), retrait de `U+00AD`, ponctuation `?` |
| **P5** | Harmonisation transversale et parcours de lecture | Tous les fichiers + [README.md](README.md) | Mention des « 8 livrables », table de correspondance des échelles de maturité, date de la ligne directrice AMF, version OpenTelemetry GenAI (`v1.41.0` vs `v1.42.0`), dates du `README.md` |
| **P6** | Validation automatisée de non-régression | Pipeline de vérification | Contrôle binaire de 100 % des critères d'acceptation sur les 5 PDF finaux |

---

## Chantier P1 — Assainissement de `Compendium.pdf` (Critique & Majeur)

### P1.1 Purge des bandeaux d'échafaudage en tête des 50 chapitres
- **Constat** : Les 50 chapitres affichent sous leur titre un bandeau interne de gestion de projet (`TOC.md v0.23` à `v0.30`, `CA-IV-11 et CA-IV-13 insatisfaites`, `G-4 à G-6 ouvertes`, `aucun vote adversarial`, `rédigé hors portes le 27 juillet 2026 et malgré la remontée bloquante R-IV-01`).
- **Action** :
  - Désactiver l'affichage du bloc de métadonnées de chantier dans le gabarit Typst des chapitres ou retirer ces sous-titres des 50 fichiers sources.
  - Conserver uniquement, si souhaité pour la traçabilité éditoriale, une notice méthodologique unifiée en début d'ouvrage (pages liminaires).

### P1.2 Résolution des 26 dettes ouvertes (`☐`) et retrait des marqueurs internes (`☑`, `⚠`)
- **Constat** : Le corps du texte contient **26 cases `☐`** non résolues, **148 cases `☑`** et **483 symboles `⚠`**.
- **Action** :
  1. Traiter sur le fond les dettes de vérification signalées par les 26 `☐`, en particulier :
     - **Ch. 16 (p. 283)** : acquitter la vérification primaire du jalon `J-IV-7` et retirer le bloc de statut interne.
     - **Ch. 35 (p. 628, 632)** : trancher et figer la datation des sources signalées « non ré-établies » au 28 juillet 2026.
     - **Ch. 44 (p. 784)** : vérifier les éléments cités de la spécification **ArchiMate 3.2** auprès de la norme primaire de The Open Group, puis retirer l'encadré d'aveu de non-lecture primaire.
     - **Ch. 47 (p. 846)** : résoudre les marqueurs `⚠` hérités du Volume I et supprimer le paragraphe sur la dette `J-IV-7`.
  2. Supprimer du rendu final toutes les cases `☐` et `☑` ainsi que les marqueurs de travail `⚠`.

### P1.3 Résolution des Annexes A à H et des renvois internes cassés
- **Constat** : Le volume passe du Chapitre 50 (p. 915) à la `Liste des références` (p. 916), puis à l'`Annexe I` (p. 926), qualifiée de *« neuvième et dernière »*, alors que les Annexes A à H sont absentes du PDF mais citées dans les chapitres et la table des matières (`45.4 Correspondance réglementaire : le tableau B.3 développé`). En outre, le texte cite des fichiers absents du dépôt (`PRD/check-sieges.py`, `check-compendium.py`, `build/assemble-bibliographie.py`, `PRD/socle-consolide.md`, `TOC.md`, `audit-references.md`) et des sections « hors du rendu » (`§ 47.13` p. 846, `§ 50.5` p. 904).
- **Action** :
  - **Option A (recommandée)** : Renommer l'`Annexe I` en `Annexe A — Bibliographie générale consolidée` (ou `Annexe unique`), remplacer dans les 50 chapitres et au titre `§ 45.4` tout renvoi aux Annexes A–H par un renvoi direct aux chapitres ou tableaux existants du Compendium et du Cadre de référence.
  - **Option B** : Rédiger et inclure effectivement les annexes maintenues (A et B) et purger toute référence aux six annexes annulées (C à H).
  - Supprimer toutes les mentions de scripts/fichiers internes du dépôt amont et les notes de bas de page pointant vers des sections « hors du rendu » (`§ 47.13`, `§ 50.5`).

### P1.4 Nettoyage et dédoublonnage de l'Annexe I.1 (`build/assemble-bibliographie.py`)
- **Constat** :
  - **58 notes méthodologiques et consignes de prompt** du Volume I ont été aspirées comme entrées bibliographiques et triées de A à V.
  - **Erreur factuelle (p. 970)** : le règlement **CRR III** est cité sous `Règlement (UE) 2024/1619` et `http://data.europa.eu/eli/reg/2024/1619/oj` (identifiant de la directive **CRD VI**) au lieu de `Règlement (UE) 2024/1623` (déjà présent à la p. 969).
  - **Doublons multiples non fusionnés** : `arXiv:0908.0191` (3×), `arXiv:2312.00326` (2×), `arXiv:2501.07913` (2×), `Règlement (UE) 2024/1689` (5× dont 4 consécutives p. 969 et 1 sous *AI Act* p. 928), `DORA 2022/2554` (3×), `MiCA 2023/1114` (3×), `RFC 6749` (3×), `RFC 8693` (4×), `RFC 8707` (3×), `RFC 9421` (3×), `SPIFFE` (3×), `Rao & Georgeff 1995` (2×), `Tolk & Muguira 2003` (2×), `Wooldridge 2009` (2×), `Yan 2025` (2×).
  - **Artefacts résiduels** : **80** mentions `⚠ à re-vérifier à la rédaction`, **39** mentions `(contexte non cité)` et **33** doubles points `..`.
- **Action** :
  1. Dans `build/assemble-bibliographie.py`, ajouter un filtre d'exclusion rejetant les lignes de métadonnées/consignes des fichiers sources (préfixes `Anti-hype`, `Doublons fusionnés`, `Entrées uniques`, `Les ressources marquées`, `Marquer le statut`, `Pour les textes`, `Privilégier les sources`, `Ressources vivantes`, `Tous les chiffres`, `Verdicts d'origine`, statistique par catégorie, etc.).
  2. Corriger à la source l'entrée `2024/1619 (CRR3)` → `2024/1623 (CRR3)` (ou la convertir en entrée distincte pour la `Directive (UE) 2024/1619 (CRD VI)` si le chapitre source cite CRD VI).
  3. Renforcer la clé de dédoublonnage dans `build/assemble-bibliographie.py` :
     - Normalisation par identifiant canonique prioritaire : `arXiv:XXXX.XXXXX` (sans numéro de version `vN`), `RFC NNNN`, `ELI/CELEX` européen (`reg/YYYY/NNNN`, `dir/YYYY/NNNN`), `DOI` en minuscules.
     - Normalisation de la clé `(auteur, année, titre)` après suppression des accents, de la casse, des sous-titres après `:` / `—` et de la ponctuation.
     - Agrégation propre de la liste des chapitres citants `[Ch. X, Ch. Y]` lors de la fusion.
  4. Purger les suffixes `— ⚠ à re-vérifier à la rédaction` et `(contexte non cité)`, et normaliser la ponctuation finale pour éliminer les 33 `..`.
  5. Mettre à jour automatiquement le compteur d'entrées uniques du tableau récapitulatif de la page 927 (actuellement fixé à `1154`).

### P1.5 Correction de la troncature des en-têtes courants
- **Constat** : Les titres de chapitres longs sont coupés au milieu d'un mot dans l'en-tête courant (p. ex. `1 · L'interopérabilité comme problème d'intégration d'entrepri…`).
- **Action** : Dans le gabarit Typst (`header`), définir un titre court par chapitre ou tronquer au dernier espace avant la limite de caractères plutôt qu'à un indice fixe de caractères.

---

## Chantier P2 — Corrections de `Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf` (Moyen & Mineur)

### P2.1 Correction du condensé `SHA-256` en Annexe C.6 et C.7 (p. 236–237)
- **Constat** : L'Annexe C.6 affiche `h = 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08` (qui est le `SHA-256` de la chaîne `"test"`) comme résultat du hachage `SHA-256` de l'objet JSON canonisé RFC 8785, et reprend cette valeur dans le champ `"action_sha256"` en C.7 (p. 237).
- **Action** :
  - Remplacer en C.6 (p. 236) et en C.7 (p. 237) `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08` par le véritable condensé `SHA-256` de la chaîne UTF-8 canonisée :
    ```text
    b29360aa7cb71ee087ffef4d78b57857bd5379074b897734a88304f27ef1c9a6
    ```
  - Vérifier ou annoter comme illustratifs les condensés de C.2 (`definition_digest`) et C.8 (`arguments_sha256`, `empreinte`).

### P2.2 Préservation de l'intégrité des littéraux JSON en Annexe C (p. 230–239)
- **Constat** : Des chaînes JSON canonisées et des identifiants (`"SUP-\n004512"`, `"PRD-\n20817"`) sont coupés par des retours à la ligne dans le rendu PDF.
- **Action** : Ajuster la feuille de style CSS des blocs de code de l'Annexe C (taille de police légèrement réduite ou coupure autorisée uniquement entre propriétés JSON hors littéraux de chaîne, et bloc JCS de C.6 sur une ligne continue ou avec indication explicite d'échappement d'affichage).

### P2.3 Correction de l'accent sur le prénom de l'auteur
- **Constat** : Écrit `Andre-Guy Bruneau` en page 1, en page 2 (Fiche du document) et dans la métadonnée PDF `author`.
- **Action** : Remplacer par `André-Guy Bruneau` aux trois endroits avant recompilation.

---

## Chantier P3 — Nettoyage de `Veille Technologique.pdf` et `Revue de littérature.pdf` (Moyen & Mineur)

### P3.1 Mise à jour et nettoyage de `Veille Technologique.pdf`
- **Constats** :
  1. La section 13 (§ 13.1 à 13.5, Tableau 15 p. 81 et Tableau 16 p. 82) décrit un état du 18–19 juillet 2026 où les Vol. III et IV ont « zéro chapitre » et où le Compendium comporte **12 livres et 54 chapitres**, contredit à la page 83 (§ 13.8–13.9) et par le `Compendium.pdf` réel (**5 livres et 50 chapitres**).
  2. Le texte et la bibliographie contiennent **19 cases `☑`** et **184 symboles `⚠`**.
  3. La page finale 145 (foliotée 144) est une veuve de 2 lignes.
  4. La référence `[275]` comporte un double point `..`.
- **Actions** :
  - Mettre à jour les Tableaux 15 et 16 et les § 13.1–13.5 pour refléter l'architecture finale du Compendium (5 livres, 50 chapitres) et l'état complété des volumes.
  - Supprimer les 19 annotations `☑ ...` et les 184 symboles `⚠` du texte et de la bibliographie.
  - Retirer le point surnuméraire de la référence `[275]`.
  - Ajuster les paramètres d'espacement de la bibliographie dans Typst pour faire tenir la fin de la référence `[342]` sur la page 144 (143 foliotée), supprimant la page 145 veuve.

### P3.2 Correction bibliographique et typographique de `Revue de littérature.pdf`
- **Constats** :
  1. **140 occurrences de `et al..`** (et 2 doubles points en fin de titre) dans la bibliographie (p. 43–60).
  2. **9 symboles `⚠`** résiduels.
  3. Les sept premiers mots du Résumé (p. 1 : `Cette revue examine la littérature académique sur`) sont extraits à raison d'un mot par ligne à cause de la justification sur colonne étroite.
- **Actions** :
  - Dans la fonction de formatage des auteurs du gabarit Typst, tester `if not authors.ends-with(".")` avant d'ajouter le point séparateur afin d'obtenir `et al.` avec un seul point sur les 140 entrées (et nettoyer les 2 titres terminés par un point).
  - Retirer les 9 symboles `⚠`.
  - Ajuster la mise en page de l'encadré du Résumé en page 1 pour éviter l'étirement d'un mot par ligne.

---

## Chantier P4 — Mise à niveau de `NiveauMaturité.pdf` (Moyen & Mineur)

- **Constats** :
  1. Aucune mention de l'auteur, de la date ni de la version dans le document ni dans les métadonnées PDF (`author: ""`).
  2. Aucun signet PDF (`toc_entries: 0`).
  3. Séquence `U+00AD` (`SOFT HYPHEN`) + `U+2010` dans `Technico\u00ad‐Syntaxique` aux pages 1 et 2.
  4. Espace avant `?` aux pages 5 et 6 (`Qui a le droit de faire quoi ?`, `Qui répond de quoi ?`), contrairement au reste du corpus québécois.
- **Actions** :
  1. Restaurer `NiveauMaturité.html` depuis le commit `4457a54` dans l'espace de build.
  2. Remplacer toute occurrence de `\u00ad` et `\u2010` par le trait d'union ASCII `-` (`Technico-Syntaxique`).
  3. Retirer l'espace avant `?` aux pages 5 et 6.
  4. Ajouter la mention `André-Guy Bruneau · Octobre 2026 · Version 1.0` sur la page 1 et dans les balises `<meta name="author" content="André-Guy Bruneau">`.
  5. Exporter le PDF et injecter avec `pymupdf` les métadonnées complètes (`title`, `author`, `subject`) ainsi que la table des matières PDF (7 entrées de signets : *Vue d'ensemble* + *Paliers 1 à 6*).

---

## Chantier P5 — Harmonisation transversale et mise à jour de `README.md` (Majeur, Moyen & Mineur)

### P5.1 Résolution de l'écart sur les « huit livrables du dépôt »
- **Constat** : `Compendium.pdf` (p. 2 et bandeaux) parle des « huit livrables du dépôt » alors que ce dépôt en compte cinq.
- **Action** :
  - Mettre à jour la note liminaire de `Compendium.pdf` (p. 2) pour nommer les **cinq livrables publiés dans ce dépôt** (ou verser les trois volumes manquants si leur publication est souhaitée).

### P5.2 Table de correspondance des échelles de maturité, d'interopérabilité et d'autonomie
- **Constat** : Les documents utilisent des échelles distinctes sans table de passage (6 paliers dans `NiveauMaturité.pdf`, 4 niveaux EIF + 5 niveaux de maturité organisationnelle + autonomie N0–N4 dans le `Cadre de Référence`, pile à 7 niveaux + LCIM L0–L6 + options OO1–OO4 dans le `Compendium`).
- **Action** : Ajouter dans [README.md](README.md) une section **Correspondance des échelles du corpus** reliant explicitement :
  - **Interopérabilité technique et syntaxique** : Palier 1 (`NiveauMaturité`) ↔ Niveau 1 Technique (`Cadre` § 6.1) ↔ Niveaux 1–2 Technique & Syntaxique (`Compendium` ch. 1).
  - **Interopérabilité sémantique** : Palier 2 (`NiveauMaturité`) ↔ Niveau 2 Sémantique (`Cadre` § 6.1) ↔ Niveau 3 Sémantique (`Compendium`).
  - **Orchestration / Chorégraphie** : Palier 3 (`NiveauMaturité`) ↔ Niveau 3 Organisationnelle (`Cadre` § 6.1, ch. 7) ↔ Niveau 4 Pragmatique/Chorégraphique & OO1–OO4 (`Compendium` ch. 22).
  - **Politique & Sécurité (PEP/PDP)** : Palier 4 (`NiveauMaturité`) ↔ Plan transversal A (`Cadre` ch. 9) ↔ Niveau 5 Politique (`Compendium`).
  - **Juridique & Réglementaire** : Palier 5 (`NiveauMaturité`) ↔ Niveau 4 Juridique (`Cadre` § 6.1, ch. 12) ↔ Niveau 6 Juridique (`Compendium`).
  - **Autonomie & Gouvernance agentique** : Palier 6 (`NiveauMaturité`) ↔ Échelle d'autonomie N0–N4 (`Cadre` ch. 8) et Modèle de maturité 1–5 (`Cadre` ch. 14) ↔ Niveau 7 Agentique (`Compendium` ch. 43).

### P5.3 Alignement des faits techniques et réglementaires transversaux
1. **Ligne directrice sur l'utilisation de l'IA de l'AMF (Québec)** :
   - Harmoniser le `Cadre de Référence` (§ 12.3, p. 189 : *« version de mars 2026 »*) et l'Annexe I.1 du `Compendium` (p. 929, 931 : *« version finale publiée 7.4.2026 »*) sur la formulation vérifiée de la `Veille` (§ 13.6) et de `S-113` (*« publiée au printemps 2026 — affichée "Avril 2026" / mise à jour le 24 avril 2026 sur le site de l'AMF —, en vigueur le 1er mai 2027 »*).
2. **Conventions sémantiques GenAI d'OpenTelemetry** :
   - Dans le `Cadre de Référence`, préciser au Tableau 41 (p. 156) que la `v1.41.0` est épinglée comme dernière version de `semantic-conventions` avant la dépréciation de la `v1.42.0` (12 juin 2026) et le transfert vers le dépôt `semantic-conventions-genai` (décrit en § 13.2, p. 202 et dans `Compendium` `S-120`).
3. **Dates dans [README.md](README.md)** :
   - Harmoniser la colonne `Date` du tableau des livrables dans [README.md](README.md) avec les dates figurant sur la couverture et dans les métadonnées des 5 PDF recompilés.

---

## Chantier P6 — Grille de vérification automatisée (Gate de sortie)

Avant tout commit des nouveaux PDF dans ce dépôt, exécuter un script Python (`pymupdf`) vérifiant que **toutes** les assertions suivantes passent à `True` :

- [ ] **Présence et intégrité** : Les 5 PDF et [README.md](README.md) s'ouvrent sans erreur; tous les liens internes des 5 PDF pointent vers des pages valides (`broken_internal_links == 0`).
- [ ] **Métadonnées et signets** : Pour chacun des 5 PDF, `metadata["author"] == "André-Guy Bruneau"`, `metadata["title"] != ""` et `len(doc.get_toc()) > 0`.
- [ ] **Absence de marqueurs de chantier** : `0` occurrence de `☐`, `0` occurrence de `☑`, `0` occurrence de `⚠`, `0` occurrence de `CA-IV-`, `0` occurrence de `R-IV-01`, `0` occurrence de `hors du rendu` et `0` occurrence de `à re-vérifier à la rédaction` dans les 5 PDF.
- [ ] **Hygiène typographique et Unicode** : `0` occurrence de `\u00ad` (`SOFT HYPHEN`), `0` occurrence de `et al..` dans [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf), et aucune page de fin veuve de moins de 5 lignes dans [Veille Technologique.pdf](Veille%20Technologique.pdf).
- [ ] **Exactitude normative et cryptographique du Cadre de référence** :
  - 272 exigences dans le corps == 272 exigences à l'Annexe D; 473 références citées == 473 références à l'Annexe G.
  - Présence du condensé exact `b29360aa7cb71ee087ffef4d78b57857bd5379074b897734a88304f27ef1c9a6` en Annexe C.6 et C.7, et `0` occurrence de `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`.
- [ ] **Intégrité bibliographique du Compendium** :
  - `0` note méthodologique infiltrée dans l'Annexe I.1.
  - `0` doublon d'identifiant `arXiv`, `RFC` ou `Règlement (UE)` dans l'Annexe I.1.
  - Règlement CRR III associé exclusivement à `2024/1623` (et non `2024/1619`).
  - Concordance exacte entre le nombre réel d'entrées de l'Annexe I.1 et le total affiché au tableau récapitulatif de l'annexe.
