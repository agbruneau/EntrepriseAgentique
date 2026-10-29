# Plan d'exécution des corrections — Entreprise Agentique (`PLAN.md`)

Ce plan structure la résolution exhaustive des constats relevés lors de l'audit des six fichiers du dépôt ([README.md](README.md), [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf), [Veille Technologique.pdf](Veille%20Technologique.pdf), [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf), [Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf](Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) et [Compendium.pdf](Compendium.pdf)).

**Validation du 29 octobre 2026.** Chaque constat a été confronté aux PDF du dépôt : extraction PyMuPDF sur texte normalisé (césures recollées, `U+00AD` retirés, lignes fusionnées), recalcul des condensés de l'Annexe C du Cadre, lecture de `NiveauMaturité.html` (commit `4457a54`). Les constats faux ont été corrigés ou retirés. Les décomptes sont ceux de [verifier.py](verifier.py) (contrôle P6).

**État d'exécution (29 oct. 2026) — `verifier.py` : 19 contrôles réussis sur 27.**

- **Fait dans ce dépôt** :
  - **P4** au complet. `NiveauMaturité.pdf` a été recompilé (Chrome sans interface) à partir de `NiveauMaturité.html` (`4457a54`). Modifications de la source :
    - `&shy;` → `-`, commentaire CSS et `aria-label` compris;
    - `<meta name="author">`;
    - mention `André-Guy Bruneau · Octobre 2026 · Version 1.0` dans l'en-tête de la p. 1;
    - `@page { size: 281mm 158mm; margin: 0 }`, format 16:9 de l'édition publiée, au lieu de l'A4 avec marges de la source;
    - `.slide[aria-current="true"] { animation: none }` à l'impression, faute de quoi la p. 1 sortait vide (opacité 0 de l'animation d'entrée).

    Métadonnées et 7 signets injectés avec `pymupdf`. L'espace insécable avant `?` est conservée (P5.4.2).
  - **P5.4.1** et volet métadonnée de **P2.3** : `author = André-Guy Bruneau` posé dans les cinq PDF (sauvegarde incrémentale, contenu intact), `subject` du Compendium renseigné. À reporter dans les sources amont, sinon la prochaine compilation fera régresser le contrôle.
  - **P5.2**, **P5.3.3**, **P5.4.2** : table de correspondance des échelles, date et version de NiveauMaturité, et absence de convention pour `?`, consignées dans le [README.md](README.md).
- **Bloqué : sources amont absentes** de ce poste et de GitHub (Typst du Compendium, de la Veille et de la Revue; HTML du Cadre) : P1 (tout), P2.2, P2.3 (texte des p. 1–2), P3 (tout), P5.1, P5.3.1, P5.3.2. Le chantier P1.2 exige en outre des re-vérifications en source primaire (ch. 35, 40, 44, 47) qui relèvent de l'auteur.

**Pagination.** `Compendium.pdf` : folios imprimés (folio = page du PDF − 14). Autres documents : pages du PDF.

---

## 0. Prérequis d'architecture documentaire

Ce dépôt ne contient que les PDF compilés et [README.md](README.md). L'exécution s'articule donc sur deux environnements :

1. **Environnement source (dépôt de rédaction amont)** :
   - Sources Typst (`Typst 0.15.1` d'après les métadonnées) de `Compendium.pdf`, `Veille Technologique.pdf` et `Revue de littérature.pdf`, incluant les scripts `build/assemble-bibliographie.py`, `check-compendium.py` et `PRD/check-sieges.py` (cités par le Compendium, absents de ce dépôt).
   - Source HTML/CSS (rendu Chromium) de `Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf`.
   - Source `NiveauMaturité.html` de `NiveauMaturité.pdf`, récupérable dans ce dépôt par `git show 4457a54:NiveauMaturité.html` (dernière version versionnée; concorde avec le PDF du 29 oct. 2026 sur les questions des paliers et l'encadré de la p. 1).
2. **Environnement de publication (ce dépôt)** :
   - Réception des 5 PDF recompilés, mise à jour de [README.md](README.md) et exécution du script de vérification finale avant `git push origin main`.

---

## Vue synoptique des chantiers et priorités

| Priorité | Chantier | Livrable(s) cible(s) | Volume d'anomalies traitées |
| :---: | :--- | :--- | :--- |
| **P1** | Assainissement éditorial et bibliographique du Compendium | [Compendium.pdf](Compendium.pdf) | 50 bandeaux de chantier, 26 `☐`, 148 `☑`, 483 `⚠`, 116 `CA-IV-`, 64 notes infiltrées en Annexe I.1, 15 notes « hors du rendu », doublons bibliographiques, erreur CRR3 `2024/1619`, renvois à des annexes non rédigées, en-têtes tronqués |
| **P2** | Corrections formelles du Cadre de référence | [Cadre de Référence](Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) | Coupures de lignes JSON (Annexe C), accent de l'auteur (`André-Guy Bruneau`); condensés `SHA-256` vérifiés exacts (aucune action) |
| **P3** | Nettoyage de la Veille technologique et de la Revue de littérature | [Veille Technologique.pdf](Veille%20Technologique.pdf), [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf) | 140 `et al..`, 19 `☑`, 193 `⚠` (184 + 9), § 13 anachronique (Tableaux 15 et 16), page 145 veuve, première ligne du Résumé p. 1 |
| **P4** | Mise à niveau des métadonnées, signets et typographie | [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf) | Attribution auteur/date/version, signets PDF (`TOC`), `&shy;` de `Technico-Syntaxique`, espace avant `?` |
| **P5** | Harmonisation transversale et parcours de lecture | Tous les fichiers + [README.md](README.md) | Mention des « huit livrables », table de correspondance des échelles, date de la ligne directrice AMF, renvoi OpenTelemetry GenAI, métadonnée `author`, dates du `README.md` |
| **P6** | Validation automatisée de non-régression | Pipeline de vérification | Contrôle binaire de 100 % des critères d'acceptation sur les 5 PDF finaux |

---

## Chantier P1 — Assainissement de `Compendium.pdf` (Critique & Majeur)

### P1.1 Purge des bandeaux d'échafaudage en tête des 50 chapitres
- **Constat** : Les 50 chapitres affichent sous leur titre un bandeau interne de gestion de projet (`TOC.md v0.23` à `v0.30`, `CA-IV-11 et CA-IV-13 insatisfaites`, `G-4 à G-6 ouvertes`, `aucun vote adversarial`, `rédigé hors portes le 27 juillet 2026 et malgré la remontée bloquante R-IV-01`, `au compte des huit (D-21)`). 90 des 116 occurrences de `CA-IV-` s'y trouvent.
- **Action** :
  - Désactiver l'affichage du bloc de métadonnées de chantier dans le gabarit Typst des chapitres ou retirer ces sous-titres des 50 fichiers sources.
  - Conserver uniquement, si souhaité pour la traçabilité éditoriale, une notice méthodologique unifiée en début d'ouvrage (pages liminaires).

### P1.2 Résolution des 26 dettes ouvertes (`☐`) et retrait des marqueurs internes (`☑`, `⚠`)
- **Constat** : Le volume contient **26 cases `☐`** (ch. 21 : 2; ch. 35 : 6; ch. 40 : 4; ch. 44 : 3; ch. 50 : 4; ch. 25, 27, 33, 38, 42, 47 et 49 : 1 chacun), **148 cases `☑`**, **483 symboles `⚠`** (dont 468 dans l'Annexe I) et **26 mentions `CA-IV-`** hors des bandeaux.
- **Action** :
  1. Traiter sur le fond les dettes de vérification signalées par les 26 `☐`, en particulier :
     - **Ch. 35 (p. 626, 627, 630, 634, 636, 637)** : six entrées « non ré-établies » à la re-datation du 28 juillet 2026; les re-dater en source primaire ou retirer les affirmations qu'elles portent.
     - **Ch. 40 (p. 722, 726, 727)** : entrées non établies, dont deux ont pour source des fichiers du Vol. I retirés du dépôt le 22 juillet 2026; les sourcer autrement ou les retirer.
     - **Ch. 44 (p. 783, 789, 797)** : conduire la re-vérification du mécanisme d'extension (Specialization + stéréotype + Profiles) sur le document normatif d'**ArchiMate 4** (The Open Group, C260, 27 avril 2026), version de référence du chapitre, puis retirer les encadrés d'aveu de non-lecture.
     - **Ch. 47 (p. 845)** : payer le jalon `J-IV-7` (confronter la cinquième horloge du § 47.8.1 au texte des ch. 37 à 40) ou retirer le paragraphe qui expose cette dette.
  2. Supprimer du rendu final toutes les cases `☐` et `☑`, les marqueurs `⚠` et les 26 mentions `CA-IV-` résiduelles.

### P1.3 Résolution des annexes absentes et des renvois internes cassés
- **Constat** : Le volume passe du Chapitre 50 (p. 915) à la `Liste des références` (p. 916, 159 entrées `S-001` à `S-159`), puis à l'`Annexe I` (p. 926), *« neuvième et dernière »* annexe du plan. Le texte renvoie pourtant aux Annexes B à H (aucun renvoi à une Annexe A), jusque dans la table des matières (`45.4 Correspondance réglementaire : le tableau B.3 développé`) :
  - l'Annexe B est la base de 159 entrées (« l'Annexe B existe et compte 159 entrées », p. 886), rendue sous le titre `Liste des références` sans en porter le nom;
  - les Annexes D et G sont abandonnées (« elle n'est pas rédigée et ne le sera pas », décision 26 du TOC, 2 sept. 2026; p. 577 et 745), l'Annexe H est dite non rédigée (p. 811);
  - plusieurs renvois visent l'« Annexe C du TOC », annexe du plan de travail `TOC.md`, et non du Compendium.

  Le texte cite en outre des fichiers absents du dépôt (`PRD/check-sieges.py`, `check-compendium.py`, `build/assemble-bibliographie.py`, `PRD/socle-consolide.md`, `TOC.md`, `audit-references.md`) et porte **15 notes de bas de page** « Renvoi à la note de statut de la pièce, hors du rendu » (p. 91 à 914, dont celles des `§ 47.13`, p. 845, et `§ 50.5`, p. 914).
- **Action** :
  - **Option A (recommandée)** : titrer la `Liste des références` comme l'Annexe B qu'elle est, garder l'`Annexe I` comme annexe finale sous un titre qui ne la dit plus « neuvième », et remplacer tout renvoi aux annexes non rédigées (C, D à H), y compris au titre du `§ 45.4`, par un renvoi direct aux chapitres ou tableaux existants du Compendium et du Cadre de référence; retirer ou requalifier les renvois à l'« Annexe C du TOC ».
  - **Option B** : rédiger les annexes encore citées comme existantes ou à venir (C, E, F, H) et purger les renvois aux annexes abandonnées (D, G).
  - Supprimer toutes les mentions de scripts/fichiers internes du dépôt amont et les 15 notes « hors du rendu ».

### P1.4 Nettoyage et dédoublonnage de l'Annexe I.1 (`build/assemble-bibliographie.py`)
- **Constat** :
  - **64 notes** ont été aspirées comme entrées bibliographiques et triées de A à Y. Règle de détection (`is_note` de [verifier.py](verifier.py)) : un « : » hors parenthèses avant le premier « (année). », ou aucun « (année). ». Elle signale aussi l'entrée `LangChain (The LangChain Team) ; version originale : Martin, L. (2025)`, vraie référence dont le champ auteur est à normaliser :
    - une dizaine de consignes et statistiques de méthode (`Anti-hype`, `Doublons fusionnés`, `Entrée générique`, `Entrées uniques`, `Les ressources marquées`, `Marquer le statut`, `Pour les textes`, `Privilégier les sources`, `Ressources vivantes`, `Tous les chiffres`, `Verdicts d'origine`);
    - une cinquantaine de notes d'errata de la forme « Référence : correction » (p. ex. `AI Act 2024/1689 : date d'adoption 13.6.2024 ajoutée…`, `SEC S7-12-23 : retiré le 12.6.2025…`, `Y201 : Case Study publiée en 2020…`).
  - **Erreur factuelle (p. 970)** : le règlement **CRR III** est cité sous `Règlement (UE) 2024/1619` et `http://data.europa.eu/eli/reg/2024/1619/oj`; `2024/1619` est le numéro de la directive **CRD VI** (ELI `dir/2024/1619`, entrée distincte p. 969), et CRR III est le `Règlement (UE) 2024/1623` (déjà présent p. 969).
  - **Doublons multiples non fusionnés** : `arXiv:0908.0191` (3×), `arXiv:2312.00326` (2×), `arXiv:2501.07913` (2×), `Règlement (UE) 2024/1689` (4 entrées consécutives p. 969, plus la note d'errata `AI Act` p. 928), `DORA 2022/2554` (3×), `MiCA 2023/1114` (3×), `eIDAS 2 2024/1183` (2×), `PLD 2024/2853` (2×), `RFC 6749` (2×), `RFC 8693` (2×), `RFC 8707` (2×), `RFC 9728` (2×), `SPIFFE` (3×), ligne directrice IA de l'AMF (2×, p. 929 et 931), `Rao & Georgeff 1995` (2×), `Tolk & Muguira 2003` (2×), `Wooldridge 2009` (2×), `Yan 2025` (2×). Les décomptes RFC de l'audit initial (6749 : 3×, 8693 : 4×, 8707 : 3×, 9421 : 3×) comptaient des entrées qui citent la RFC sans en être la notice (p. ex. le brouillon OAuth 2.1, Okta XAA, Visa TAP); `RFC 9421` n'a qu'une notice.
  - **Artefacts résiduels** : **101** mentions `⚠ à re-vérifier à la rédaction` et **41** mentions `(contexte non cité)` (texte normalisé; une recherche brute sur l'extraction en manque une vingtaine, coupées par les césures). Aucun double point `..` dans le rendu actuel.
- **Action** :
  1. Dans `build/assemble-bibliographie.py`, ajouter un filtre d'exclusion rejetant les consignes (préfixes ci-dessus) **et** les notes d'errata (règle `is_note` ci-dessus); normaliser le champ auteur de l'entrée LangChain; contrôler le résultat avec [verifier.py](verifier.py).
  2. Corriger à la source l'entrée `2024/1619 (CRR3)` → `2024/1623 (CRR3)` et la fusionner avec l'entrée existante; conserver l'entrée `Directive (UE) 2024/1619 (CRD VI)`.
  3. Renforcer la clé de dédoublonnage dans `build/assemble-bibliographie.py` :
     - Normalisation par identifiant canonique prioritaire : `arXiv:XXXX.XXXXX` (sans numéro de version `vN`), `RFC NNNN`, `ELI/CELEX` européen (`reg/YYYY/NNNN`, `dir/YYYY/NNNN`), `DOI` en minuscules.
     - Normalisation de la clé `(auteur, année, titre)` après suppression des accents, de la casse, des sous-titres après `:` / `—` et de la ponctuation.
     - Agrégation propre de la liste des chapitres citants `[Ch. X, Ch. Y]` lors de la fusion.
  4. Purger les suffixes `— ⚠ à re-vérifier à la rédaction` et `(contexte non cité)`, en vérifiant que la purge ne laisse ni `..` ni ponctuation finale orpheline.
  5. Les compteurs du tableau récapitulatif (p. 927 : `1154` entrées uniques, `109` doublons fondus) sont déjà produits par le script et concordent avec les 1154 entrées actuelles; vérifier qu'ils suivent la purge et la fusion.

### P1.5 Correction de la troncature des en-têtes courants
- **Constat** : Les titres de chapitres longs sont coupés au milieu d'un mot dans l'en-tête courant (p. ex. `1 · L'interopérabilité comme problème d'intégration d'entrepri…`, `47 · L'artefact livré : provenance des composants et mise en se…`).
- **Action** : Dans le gabarit Typst (`header`), définir un titre court par chapitre ou tronquer au dernier espace avant la limite de caractères plutôt qu'à un indice fixe de caractères.

---

## Chantier P2 — Corrections de `Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf` (Moyen & Mineur)

### P2.1 Condensés `SHA-256` de l'Annexe C : constat invalidé, aucune action
- **Constat initial** : C.6 et C.7 afficheraient `9f86d081…0f00a08` (`SHA-256` de `"test"`), à remplacer par `b29360aa…ef1c9a6`.
- **Vérification** : la v1.1 (28 oct. 2026) ne contient plus `9f86d081…`. C.6 (p. 235–236) est le jeton d'approbation : `h = 9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d`, soit `SHA-256(identifiant de l'outil ‖ arguments canonisés RFC 8785)`, recalculé exact et repris dans `action_sha256` (C.6) et `empreinte_approbation` (C.8). C.7 (p. 236–237) est l'enveloppe budgétaire et ne porte aucun condensé. `definition_digest` (C.2), `idempotency_key` (`SHA-256("tache-7f3c2a|etape-03/creer-bon-commande")`) et `arguments_sha256` (C.8) se recalculent aussi exactement; les autres empreintes sont déclarées fictives (p. 230). La valeur `b29360aa…` ne correspond à aucun objet du document : l'insérer créerait l'erreur.
- **Action** : aucune. Le contrôle P6 recalcule ces condensés.

### P2.2 Préservation de l'intégrité des littéraux JSON en Annexe C (p. 230–239)
- **Constat** : Des chaînes JSON canonisées et des identifiants (`"SUP-\n004512"`, `"PRD-\n20817"`, p. 236) sont coupés par des retours à la ligne dans le rendu PDF.
- **Action** : Ajuster la feuille de style CSS des blocs de code de l'Annexe C (taille de police légèrement réduite ou coupure autorisée uniquement entre propriétés JSON hors littéraux de chaîne, et bloc JCS de C.6 sur une ligne continue ou avec indication explicite d'échappement d'affichage).

### P2.3 Correction de l'accent sur le prénom de l'auteur
- **Constat** : Écrit `Andre-Guy Bruneau` en page 1, en page 2 (Fiche du document) et dans la métadonnée PDF `author`.
- **Action** : Remplacer par `André-Guy Bruneau` aux trois endroits avant recompilation.

---

## Chantier P3 — Nettoyage de `Veille Technologique.pdf` et `Revue de littérature.pdf` (Moyen & Mineur)

### P3.1 Mise à jour et nettoyage de `Veille Technologique.pdf`
- **Constats** :
  1. La section 13 (§ 13.1 à 13.5, Tableau 15 p. 81 et Tableau 16 p. 82) décrit l'état du 18–19 juillet 2026 : Vol. III et IV à « zéro chapitre », Compendium v0.4 en **douze livres**; une notice bibliographique de la p. 122 parle d'un « omnibus de 54 chapitres et 12 livres ». La p. 83 (§ 13.8 : Vol. III rédigé depuis le 22 juillet, Vol. IV arrêté le 29 juillet) et le `Compendium.pdf` réel (**5 livres et 50 chapitres**) le contredisent.
  2. Le texte et la bibliographie contiennent **19 cases `☑`** et **184 symboles `⚠`**.
  3. La page finale 145 (foliotée 144) est une veuve de 2 lignes (fin de la référence `[342]`).
  4. Le seul `..` du document (réf. 187, p. 117) est le chemin relatif `../common/durable-task-code-constraints` d'une URL : à conserver.
- **Actions** :
  - Mettre à jour les Tableaux 15 et 16, les § 13.1–13.5 et la notice de la p. 122 pour refléter l'architecture finale du Compendium (5 livres, 50 chapitres) et l'état complété des volumes.
  - Supprimer les 19 annotations `☑ ...` et les 184 symboles `⚠` du texte et de la bibliographie.
  - Ajuster les paramètres d'espacement de la bibliographie dans Typst pour faire tenir la fin de la référence `[342]` sur la page 144 (143 foliotée), supprimant la page 145 veuve.

### P3.2 Correction bibliographique et typographique de `Revue de littérature.pdf`
- **Constats** :
  1. **140 occurrences de `et al..`** dans la bibliographie (p. 41–59); aucun autre double point.
  2. **9 symboles `⚠`** résiduels.
  3. La première ligne du Résumé (p. 1), ouverte par le titre en ligne « Résumé », est justifiée avec des espaces très étirées, `l'interopérabilité` ne tenant pas sur la ligne; l'extraction texte la restitue à raison d'un mot par ligne.
- **Actions** :
  - Dans la fonction de formatage des auteurs du gabarit Typst, tester `if not authors.ends-with(".")` avant d'ajouter le point séparateur afin d'obtenir `et al.` avec un seul point sur les 140 entrées.
  - Retirer les 9 symboles `⚠`.
  - Corriger la première ligne du Résumé (césure de `l'interopérabilité`, reformulation ou justification à gauche de ce paragraphe).

---

## Chantier P4 — Mise à niveau de `NiveauMaturité.pdf` (Moyen & Mineur)

- **Constats** :
  1. Aucune mention de l'auteur, de la date ni de la version dans le document ni dans les métadonnées PDF (`author: ""`).
  2. Aucun signet PDF (`toc_entries: 0`).
  3. Séquence `U+00AD` (`SOFT HYPHEN`) + `U+2010` dans `Technico­‐Syntaxique` aux pages 1 et 2. La source porte `Technico&shy;Syntaxique` (deux occurrences), coupure voulue selon le commentaire CSS de `.level-grid` (colonne de 11,5 em); le `U+2010` est le trait que Chromium affiche à la coupure.
  4. Espace insécable (`&nbsp;`) avant `?` : 12 occurrences, sur les 7 pages, uniforme dans le document. Le reste du corpus n'a pas de convention unique : espace dominante dans le Compendium (185 contre 13), collé dans le Cadre (49 contre 5), mixte dans la Veille et la Revue.
  5. `⚠ Échelle propre à ce document.` (p. 1) est un avertissement de contenu voulu, non un marqueur de chantier.
- **Actions** :
  1. Restaurer `NiveauMaturité.html` depuis le commit `4457a54` dans l'espace de build.
  2. Remplacer les deux `&shy;` par le trait d'union ASCII `-` (`Technico-Syntaxique`); vérifier au rendu que le titre de palier ne chevauche pas la question, sinon élargir la colonne de `.level-grid`.
  3. Appliquer la convention d'espace avant `?` retenue en P5.4 (rien à faire si l'espace insécable est conservée).
  4. Ajouter la mention `André-Guy Bruneau · Octobre 2026 · Version 1.0` sur la page 1 et la balise `<meta name="author" content="André-Guy Bruneau">`.
  5. Exporter le PDF et injecter avec `pymupdf` les métadonnées complètes (`title`, `author`, `subject`) ainsi que la table des matières PDF (7 entrées de signets : *Vue d'ensemble* + *Paliers 1 à 6*, une par page).
  6. Conserver le `⚠` de la p. 1 (exclu du contrôle P6) ou le remplacer par une mention textuelle.

---

## Chantier P5 — Harmonisation transversale et mise à jour de `README.md` (Majeur, Moyen & Mineur)

### P5.1 Résolution de l'écart sur les « huit livrables du dépôt »
- **Constat** : `Compendium.pdf` (p. 2 et les 50 bandeaux, « au compte des huit (D-21) ») parle des « huit livrables du dépôt » alors que ce dépôt en compte cinq.
- **Action** :
  - Mettre à jour la note liminaire de `Compendium.pdf` (p. 2) pour nommer les **cinq livrables publiés dans ce dépôt** (ou verser les trois volumes manquants si leur publication est souhaitée).

### P5.2 Table de correspondance des échelles de maturité, d'interopérabilité et d'autonomie
- **Constat** : Les documents utilisent des échelles distinctes sans table de passage :
  - `NiveauMaturité` : 6 paliers (technico-syntaxique, sémantique, chorégraphique, politique, juridique, agentique).
  - `Cadre de Référence` : 4 couches de l'EIF, non numérotées (juridique, organisationnelle, sémantique, technique), et gouvernance transversale (§ 6.1); autonomie N0–N4 (ch. 8); maturité en 5 niveaux (ch. 14).
  - `Compendium` : pile canonique en 4 niveaux (1 technique, 2 syntaxique, 3 sémantique, 4 organisationnel), étendue par le LCIM à 7 niveaux de 0 à 6 (§ 1.1.2); options d'orchestration OO1–OO4 (ch. 22); trois échelles d'autonomie héritées du Vol. I (§ 4.1.4).
- **Action** : Ajouter dans [README.md](README.md) une section **Correspondance des échelles du corpus**, par thème et non par rang (le README pose déjà qu'« un rang ne se cite pas d'une échelle à l'autre ») :

  | Palier (`NiveauMaturité`) | `Cadre de Référence` | `Compendium` |
  | :--- | :--- | :--- |
  | 1 Technico-syntaxique | Couche technique (§ 6.1) | Niveaux 1 technique et 2 syntaxique (§ 1.1.2); MCP et A2A (ch. 8) |
  | 2 Sémantique | Couche sémantique (§ 6.1) | Niveau 3 sémantique et LCIM (§ 1.1.2); ch. 2 |
  | 3 Chorégraphique | Couche organisationnelle (§ 6.1); orchestration (ch. 7) | Niveau 4 organisationnel (§ 1.1.2); OO1–OO4 (ch. 22) |
  | 4 Politique | Gouvernance de l'interopérabilité (§ 6.1); gouvernance et cycle de vie (ch. 11) | Gouvernance de l'interopérabilité (ch. 3); PEP/PDP (ch. 37) |
  | 5 Juridique | Couche juridique (§ 6.1); risques, conformité et réglementation (ch. 12) | Cadre réglementaire (ch. 25 à 30) |
  | 6 Agentique | Autonomie N0–N4 (ch. 8); maturité 1–5 (ch. 14) | Niveaux d'autonomie (§ 4.1.4) |

### P5.3 Alignement des faits techniques et réglementaires transversaux
1. **Ligne directrice sur l'utilisation de l'IA de l'AMF (Québec)** :
   - **État** : `Cadre de Référence` § 12.3 (p. 189) : *« version de mars 2026 »*; Annexe I.1 du `Compendium` : *« Version finale publiée 7.4.2026 »* (p. 929) et *« version finale 7 avr. 2026 »* (p. 931, doublon); `Veille` § 4.11.5 (p. 38) : *« finale le 7 avril 2026 »*, date que la Veille rétracte elle-même au § 13.6 (p. 83 : non reconfirmée, divergence « signalée, non uniformisée »). `S-113` (`Compendium` p. 922) constate que ni le 30 mars ni le 7 avril 2026 ne figure sur les pages de l'AMF, qui affichent « Avril 2026 » (FR) et « Updated on April 24, 2026 » (EN).
   - **Action** : aligner le `Cadre` (p. 189), le `Compendium` (p. 929 et 931, fusionnées) et la `Veille` (§ 4.11.5 et ses reprises) sur ce que la source primaire affiche : page de l'AMF datée « Avril 2026 » / « Updated on April 24, 2026 », aucune date de publication au jour près attestée, entrée en vigueur le 1er mai 2027.
2. **Conventions sémantiques GenAI d'OpenTelemetry** :
   - **État** : le `Cadre de Référence` l'explique déjà au § 10.1 (p. 154) : la `v1.41.1` (11 mai 2026, correctif de la `v1.41.0` du 28 avril) est la dernière version de `semantic-conventions` où les conventions GenAI sont en vigueur; la `v1.42.0` (12 juin 2026) les déclare obsolètes au profit du dépôt `semantic-conventions-genai`, sans version étiquetée. Le § 13.2 (p. 202) et `S-120` du `Compendium` concordent. Le Tableau 41 (p. 156) cite la `v1.41.0` sans ce rappel.
   - **Action (mineure)** : ajouter sous le Tableau 41 un renvoi au § 10.1.
3. **Dates dans [README.md](README.md)** :
   - Elles concordent aujourd'hui avec les PDF (Veille et Revue : faits gelés au 15 août 2026, compilés le 15 sept.; Cadre : 28 oct.; NiveauMaturité : 29 oct.; Compendium : compilé le 24 oct.). Harmoniser la colonne `Date` avec la couverture et les métadonnées des 5 PDF recompilés.

### P5.4 Métadonnée `author` et convention typographique
1. **Métadonnée `author`** : `Andre-Guy Bruneau` (Cadre, cf. P2.3), vide (NiveauMaturité, cf. P4), `André-Guy Bruneau, M.Sc. IT` (Compendium), `André-Guy Bruneau, M.Sc. IT · agbruneau@gmail.com · 15 août 2026` (Veille, Revue). Fixer `André-Guy Bruneau` dans les cinq documents (Typst : `set document(author: ...)`), condition du contrôle P6. Renseigner le `subject` du Compendium, vide.
2. **Espace avant `?`** : choisir une convention pour le corpus (constat P4.4) et l'appliquer aux cinq documents, ou consigner dans le README qu'il n'y en a pas.

---

## Chantier P6 — Grille de vérification automatisée (Gate de sortie)

Avant tout commit des nouveaux PDF dans ce dépôt, exécuter le script [verifier.py](verifier.py) (`pymupdf`), qui vérifie que **toutes** les assertions suivantes passent à `True` et sort en erreur sinon :

```bash
python verifier.py
```

Les recherches de chaînes portent sur le texte normalisé (césures recollées, `U+00AD` retirés, lignes fusionnées); sans normalisation, les césures masquent des occurrences. **Référence initiale au 29 oct. 2026 : 13 contrôles réussis sur 27; 19 après les corrections faisables dans ce dépôt.**

- [ ] **Présence et intégrité** : Les 5 PDF et [README.md](README.md) s'ouvrent sans erreur; tous les liens internes des 5 PDF pointent vers des pages valides (`broken_internal_links == 0`). Les destinations nommées UTF-8 de Typst, que PyMuPDF lit en Latin-1, sont résolues par l'arbre des noms (vrai aujourd'hui pour les 5 PDF).
- [ ] **Métadonnées et signets** : Pour chacun des 5 PDF, `metadata["author"] == "André-Guy Bruneau"` (cf. P5.4), `metadata["title"] != ""` et `len(doc.get_toc()) > 0`.
- [ ] **Absence de marqueurs de chantier** : `0` occurrence de `☐`, `☑`, `⚠` (hormis l'avertissement voulu de `NiveauMaturité.pdf` p. 1), `CA-IV-`, `R-IV-01`, `hors du rendu` et `à re-vérifier à la rédaction` dans les 5 PDF.
- [ ] **Hygiène typographique et Unicode** : `0` occurrence de `­` dans [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf) (dans les PDF Typst, `U+00AD` marque les césures de fin de ligne — 3 171 dans le Compendium, 107 dans la Veille, 37 dans la Revue — et reste légitime), `0` occurrence de `et al..` dans [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf), et aucune page de fin veuve de moins de 5 lignes dans [Veille Technologique.pdf](Veille%20Technologique.pdf).
- [ ] **Exactitude normative et cryptographique du Cadre de référence** :
  - 272 exigences dans le corps == 272 exigences à l'Annexe D; 473 références citées == 473 références à l'Annexe G (vrai pour la v1.1).
  - Condensés recalculés à partir des valeurs affichées et égaux à celles-ci : `h` (C.6, repris dans `action_sha256` et `empreinte_approbation` en C.8) == `SHA-256(identifiant de l'outil ‖ JCS(arguments))`, `definition_digest` (C.2), `idempotency_key` et `arguments_sha256` (C.8); `0` occurrence de `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`.
- [ ] **Intégrité bibliographique du Compendium** :
  - `0` note méthodologique ou d'errata infiltrée dans l'Annexe I.1 (règle de P1.4).
  - `0` doublon d'identifiant principal dans l'Annexe I.1 : `Règlement`/`Directive (UE)` en tête de titre, RFC publiée par l'IETF (`IETF RFC NNNN`), `arXiv` sans version. Une entrée qui en cite une autre (p. ex. le RTS 2018/389 qui renvoie à PSD2 2015/2366) n'est pas un doublon.
  - Règlement CRR III associé exclusivement à `2024/1623` (et non `2024/1619`).
  - Concordance exacte entre le nombre réel d'entrées de l'Annexe I.1 et le total affiché au tableau récapitulatif de l'annexe.
