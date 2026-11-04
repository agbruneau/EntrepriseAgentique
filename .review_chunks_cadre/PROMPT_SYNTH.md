# Consigne — méta-audit croisé et synthèse finale (Phase 4b)

ultrathink. Tu es le méta-réviseur final de la revue contradictoire du Cadre de référence CRE-IA-2026-01 (283 pages, 287 exigences). Rédige en français canadien, sans complaisance, avec la sobriété d'un rapport de comité de lecture.

## Entrées
- `C:\Github\EntrepriseAgentique\REVIEW_PLAN_CADRE.md` (structure, notations, thèses T1-T8).
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\digest.md` : pour chacune des six tranches consolidées, la synthèse, la liste des défauts BLOQUANT et MAJEUR (titre, constats, localisation), les arbitrages transversaux proposés et les constats écartés.
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\conso_1.md` à `conso_6.md` : la matrice détaillée de chaque tranche. Consulte-les (Grep, lecture ciblée) pour vérifier un défaut que tu cites; ne les lis pas en entier.
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\audit_lit.md` : vérification bibliographique et état de l'art.
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\full.txt` : texte intégral, pour trancher un point par Grep.

## Travail
1. **Croiser** les tranches : repère les défauts transversaux que plusieurs tranches ont vus séparément (même cause, sections différentes), les dérives de notation, de chiffres, de dates et de versions entre chapitres, et les contradictions entre arbitrages proposés par des tranches différentes.
2. **Trancher les arbitrages transversaux** : pour chaque décision de conception que les tranches ont proposée (portée de la passerelle et intradomaine; agents intégrés aux logiciels-services; compensations face au coupe-circuit, au mode fermé et aux plafonds; usage unique du jeton d'approbation et réessai idempotent; canonisation et différentiel d'analyse JSON; propagation du marquage de contenu non fiable et règle de deux à l'échelle du système; contenu interdit en télémétrie contre preuve, évaluation, art. 11 Loi 25 et avis d'incident; ancrage externe du chaînage d'audit; statut « Contenir »; force normative du catalogue, des tableaux et des méta-règles; régime transitoire de la feuille de route; décompte 287 exigences; etc.), retiens **une** option, formulée comme une règle rédigeable, et liste les sections et exigences à modifier. Ces arbitrages seront appliqués tels quels par six implémenteurs indépendants : ils doivent être précis, cohérents entre eux et compatibles avec les sources primaires d'`audit_lit.md`.
3. **Évaluer** la contribution sans complaisance.

## Sortie
Écris (Write) `C:\Github\EntrepriseAgentique\.review_chunks_cadre\synth.md`, et ne modifie aucun autre fichier. Ce texte formera le début de `DEEP_REVIEW_CADRE_REFERENCE.md`; la matrice détaillée des six tranches y sera ajoutée mécaniquement à la suite (section 2), ne la recopie pas.

```
# Revue approfondie et contradictoire — Cadre de référence CRE-IA-2026-01
(métadonnées : document, version, date de la revue, méthode en 4 phases en 5 lignes, décompte des constats bruts et des défauts consolidés par gravité)
## 1. Verdict exécutif
### 1.1 Thèse centrale du cadre
### 1.2 Évaluation de la contribution (forces réelles, faiblesses structurelles, verdict sur T1-T8 une par une)
### 1.3 Verdict (acceptable en l'état / après révisions majeures / à refondre) et conditions
## 2. Matrice des défauts
### 2.0 Défauts transversaux et dérives inter-chapitres
(chaque défaut transversal : [BLOQUANT|MAJEUR|MINEUR - …], défauts de tranche fusionnés (ex. 1.01, 3.04, 4.07), localisations, diagnostic par premiers principes, contre-exemple, correctif)
### 2.0.1 Arbitrages transversaux retenus
(A-01, A-02… : décision, règle rédigée, sections et exigences touchées, défauts résolus)
## 3. État de l'art manquant et preuves exigées
### 3.1 Travaux omis (d'après audit_lit.md : référence, effet, section touchée)
### 3.2 Citations inexactes ou obsolètes à corriger (renvoi à audit_lit.md)
### 3.3 Preuves, essais et expérimentations additionnels exigés (ce que le cadre doit démontrer ou faire mesurer pour que ses exigences soient tenables : bancs d'essai de la passerelle sous contention, essais de compensation sous coupe-circuit, essais d'injection adaptative, etc.)
```

Termine par la ligne : `synth.md : T défauts transversaux, A arbitrages retenus`.
