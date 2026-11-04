# Original User Request

## Initial Request — 2026-11-03T22:19:31Z

Use a very large team of agents. Exécute un Deep Paper Review exhaustif et contradictoire sur `documents/Compendium.pdf` selon un pipeline strict en 4 phases. Configure tous les sous-agents d'analyse avec un budget de raisonnement maximal (thinking = max).

Integrity mode: development

## Requirements

### R1. Cartographie et segmentation (Phase 1)
- Extraire la structure complète, la table des matières, les théorèmes et axiomes centraux et la taxonomie de `documents/Compendium.pdf`.
- Découper logiquement le manuscrit en segments de 10 à 15 pages avec un recouvrement de 2 pages entre segments adjacents pour préserver le contexte des preuves et des transitions.
- Consigner ce plan de partitionnement et la table des symboles et définitions globales dans `REVIEW_PLAN.md`.

### R2. Audit formel et systémique en essaim (Phase 2)
Chaque sous-agent audite son segment assigné sans complaisance selon trois axes causaux :
- Rigueur formelle et algorithmique : falsifier les démonstrations mathématiques, vérifier les bornes de complexité, les invariants d'état, les hypothèses de concurrence/distribution et la validité des équations. Signaler tout saut logique ou postulat implicite non démontré.
- Solidité architecturale et empirique : évaluer la méthodologie, la reproductibilité des bancs d'essai, les cas limites omis (modes de défaillance, contention, passage à l'échelle) et la validité des compromis annoncés.
- Clarté et densité structurelle : identifier les redondances, les contradictions internes au segment et les passages sous-spécifiés.

### R3. Vérification bibliographique et état de l'art (Phase 3)
Utiliser la recherche web pour confronter les affirmations clés et la bibliographie de `documents/Compendium.pdf` à la littérature scientifique et industrielle récente (jusqu'en 2026) :
- Identifier les travaux fondateurs ou récents omis (conférences majeures telles que STOC, ICML, NeurIPS, ICLR, AISTATS, SOSP, OSDI ou standards actuels).
- Vérifier qu'aucune référence citée n'est déformée, obsolète ou contredite par des résultats postérieurs.

### R4. Cohérence inter-chapitres et méta-synthèse (Phase 4)
Croiser les rapports des phases 2 et 3 avec `REVIEW_PLAN.md` pour détecter les dérives de notation, les définitions contradictoires d'un chapitre à l'autre et les dépendances circulaires. Produire le livrable final dans `./DEEP_REVIEW_COMPENDIUM.md` comprenant :
1. Verdict exécutif et évaluation de la contribution fondamentale.
2. Matrice des défauts classés par sévérité (Bloquant/Erreur formelle, Majeur/Lacune méthodologique, Mineur/Clarté) avec localisation exacte (chapitre, page, citation exacte), diagnostic causal et correctif ou contre-exemple explicite.
3. Liste des références manquantes et des expériences ou preuves complémentaires requises.

## Acceptance Criteria

### Plan de revue (`REVIEW_PLAN.md`)
- [ ] Le fichier `REVIEW_PLAN.md` est généré à la racine.
- [ ] Le fichier contient la table des matières complète et la structure globale de `documents/Compendium.pdf`.
- [ ] Le manuscrit est découpé en segments de 10 à 15 pages avec un chevauchement exact de 2 pages entre segments consécutifs.
- [ ] Le fichier contient une table exhaustive des symboles, axiomes et définitions globales.

### Rapport d'audit approfondi (`./DEEP_REVIEW_COMPENDIUM.md`)
- [ ] Le fichier `./DEEP_REVIEW_COMPENDIUM.md` est produit et structuré selon les sections exigées.
- [ ] Section 1 : Comprend un verdict exécutif clair et l'évaluation critique de la contribution fondamentale du document.
- [ ] Section 2 : Contient la matrice complète des défauts répertoriés lors de l'audit, catégorisés par sévérité (Bloquant/Erreur formelle, Majeur/Lacune méthodologique, Mineur/Clarté).
- [ ] Chaque entrée de la matrice des défauts comporte sa localisation précise (chapitre, numéro de page, citation textuelle exacte), son diagnostic causal et un correctif formel ou un contre-exemple explicite.
- [ ] Section 3 : Dresse la liste exhaustive des références bibliographiques omises ou déformées (confrontées à la littérature jusqu'en 2026), ainsi que les expériences ou preuves complémentaires requises.
