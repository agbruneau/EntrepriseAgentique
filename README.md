# Interopérabilité et Orchestration en Entreprise Agentique

Corpus documentaire d'André-Guy Bruneau, M.Sc. IT, sur la conception, le déploiement et la supervision d'agents d'IA fondés sur les grands modèles de langue en entreprise, avec un accent sur les services financiers réglementés au Canada.

## Structure du dépôt

```
documents/          Les cinq livrables en PDF
sources/annexes/    Sources Typst des annexes « Reprise du 29 octobre 2026 » (Veille et Revue)
```

Les documents dont le corpus dépend sans être versés ici sont listés à la section [Documents absents du dépôt](#documents-absents-du-dépôt).

## Livrables

| Document | Nature | Pages | Date |
|---|---|---|---|
| [NiveauMaturité](documents/NiveauMaturit%C3%A9.pdf) | Pile d'interopérabilité en six paliers, propre à ce document : technico-syntaxique, sémantique, chorégraphique, politique, juridique, agentique. | 7 | Version 1.0, compilée le 29 oct. 2026 |
| [Veille technologique](documents/Veille%20Technologique.pdf) | État de l'art en entreprise : protocoles MCP, A2A et ANP, gouvernance, adoption, sécurité, sept couches implicites. | 152 | Faits gelés au 15 août 2026; reprise datée du 29 oct. 2026 en annexe |
| [Revue de littérature](documents/Revue%20de%20litt%C3%A9rature.pdf) | Revue de la littérature académique (192 pièces, dont 189 sur arXiv) sur dix fronts; confronte trois énoncés de la veille. | 64 | Faits gelés au 15 août 2026; notices reprises le 29 oct. 2026 en annexe |
| [Cadre de référence](documents/Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) | Cadre normatif d'architecture d'entreprise (CRE-IA-2026-01, v1.1, soumis à l'approbation du comité) : standards, patrons d'orchestration, autonomie et supervision humaine, identité, observabilité, FinOps, conformité. | 294 | 28 oct. 2026 |
| [Compendium](documents/Compendium.pdf) | Somme en cinq livres et cinquante chapitres : Coopérer, Faire confiance, Encadrer, Appliquer/exploiter, Livrer et clore (horizon 2024-2032). | 1000 | Gel au 27 juill. 2026, compilé le 24 oct. 2026 (édition de nov. 2026) |

## Statut et limites

- Le **Cadre de référence** (v1.1) est une version finale soumise à l'approbation du comité; il n'est pas encore approuvé.
- Le **Compendium** a été rédigé hors des portes de qualité, sans relecture adversariale. Ses dettes de vérification ont été instruites le 29 oct. 2026 (journal `VERIFICATIONS.md`, retiré du dépôt au commit `d47db0f` et consultable dans l'historique git). Ses renvois aux volumes I à III et ses liens de fichier visent des documents absents du dépôt (voir ci-dessous).
- La **Veille** (§ 13) décrit une version antérieure du Compendium, en douze livres; une note datée sous le Tableau 16 le signale, et la structure en vigueur est celle du Compendium livré.
- Les cinq PDF ont été corrigés le 29 oct. 2026 selon `PLAN.md`, par retouche directe faute de sources amont dans ce dépôt; `PLAN.md` et le contrôle `verifier.py` ont été retirés au commit `d47db0f` et restent dans l'historique git. Les sources doivent recevoir les mêmes corrections avant toute recompilation.
- La **Veille** et la **Revue** ont été révisées le même jour, en après-midi : errata corrigés à leur place quand ils tenaient dans la ligne, puis une annexe « Reprise du 29 octobre 2026 » ajoutée à chacune (Veille : énoncés datés rouverts sur source primaire, onze errata, références [343] à [371]; Revue : 189 notices arXiv reprises, régimes de preuve recomptés, quatre errata). Le corps reste gelé au 15 août 2026; l'annexe fait foi pour le 29 octobre. Ces ajouts sont à reporter dans les sources amont.
- Les échelles diffèrent d'un document à l'autre (voir ci-dessous). Un rang ne se cite pas d'une échelle à l'autre.
- La typographie de la ponctuation haute n'est pas harmonisée : NiveauMaturité met une espace insécable avant `?`, le Cadre n'en met généralement pas, les autres documents varient.

## Documents absents du dépôt

Le corpus s'appuie sur des documents qui ne sont pas versés ici. Leur absence n'empêche pas la lecture, mais elle empêche de vérifier une partie des citations et de recompiler les PDF.

| Document | Qui y renvoie | Conséquence de l'absence |
|---|---|---|
| Sources amont des PDF : Typst 0.15.1 pour la Veille, la Revue et le Compendium; HTML imprimé par Chrome pour le Cadre et NiveauMaturité (d'après les métadonnées des PDF) | Les cinq livrables | Recompilation impossible. Seule la source HTML de NiveauMaturité subsiste, dans l'historique git (commit `4457a54`), dans un état antérieur aux corrections du 29 oct. 2026. |
| Vol. I — *Interopérabilité agentique* (7 ch.) | Compendium (373 renvois); Veille § 4.12 et § 13 | Renvois invérifiables depuis ce dépôt. |
| Vol. II — *L'autonomie encadrée* (24 ch.) et son socle coté (46 entrées) | Compendium (542 renvois); Veille § 8.4 et § 13 | Faits repris du socle invérifiables depuis ce dépôt. |
| Vol. III — *L'entreprise agentique* et ses fiches F-xx et H-xx | Compendium (858 renvois, dont 123 fiches distinctes citées comme sources); Veille § 7.6 et § 13 | Énoncés appuyés sur une fiche invérifiables depuis ce dépôt. |
| Démonstrateur Borealis-Go (Vol. I) | Veille § 4.12 | Retiré de son dépôt le 25 juill. 2026 (Veille § 13.2), rejouable dans le seul historique git de ce dépôt-là. |
| Fichiers de travail : `PRD/PRD.md` (dont les décisions d'auteur D-n, § 15), `PRD/socle-consolide.md`, `PRD/TOC.md`, `PRD/gel-2026-07-27.md`, `PRD/gel-2026-07-28-volet-residuel.md`, `annexe-references.md` | Compendium : 9 liens de fichier (p. 152, 154, 279, 280, 353 et 940) et renvois aux décisions D-n | Liens morts. La teneur des décisions D-18 et D-21, qui fixent le périmètre du dépôt à cinq livrables, n'est pas consultable. |

Au 15 août 2026, la Veille (§ 13.8) décrit les volumes III et IV comme diffusés à leur seul auteur, faute de relecteur distinct; le Vol. IV est depuis versé ici comme Compendium (décision D-21). L'absence des volumes I à III peut donc être voulue.

## Sources des annexes

Les annexes de la Veille et de la Revue se recompilent séparément avec Typst 0.15.1; `tpl.typ` porte la mise en page commune. Les PDF produits sont ignorés par git.

```bash
typst compile sources/annexes/veille_annexe.typ
```

```bash
typst compile sources/annexes/revue_annexe.typ
```

## Correspondance des échelles du corpus

Les échelles du corpus ne se superposent pas rang pour rang. Le tableau les relie par thème, à partir des paliers de NiveauMaturité.

- **NiveauMaturité** : six paliers.
- **Cadre de référence** : quatre couches de l'EIF, non numérotées, et une gouvernance transversale (§ 6.1); autonomie N0 à N4 (ch. 8); maturité en cinq niveaux (ch. 14).
- **Compendium** : pile canonique en quatre niveaux (1 technique, 2 syntaxique, 3 sémantique, 4 organisationnel), étendue par le LCIM à sept niveaux numérotés de 0 à 6 (§ 1.1.2); options d'orchestration OO1 à OO4 (ch. 22); trois échelles d'autonomie héritées du Vol. I (§ 4.1.4).

| Palier (NiveauMaturité) | Cadre de référence | Compendium |
|---|---|---|
| 1 Technico-syntaxique | Couche technique (§ 6.1) | Niveaux 1 technique et 2 syntaxique (§ 1.1.2); MCP et A2A (ch. 8) |
| 2 Sémantique | Couche sémantique (§ 6.1) | Niveau 3 sémantique et LCIM (§ 1.1.2); ch. 2 |
| 3 Chorégraphique | Couche organisationnelle (§ 6.1); orchestration (ch. 7) | Niveau 4 organisationnel (§ 1.1.2); OO1 à OO4 (ch. 22) |
| 4 Politique | Gouvernance de l'interopérabilité (§ 6.1); gouvernance et cycle de vie (ch. 11) | Gouvernance de l'interopérabilité (ch. 3); PEP/PDP (ch. 37) |
| 5 Juridique | Couche juridique (§ 6.1); risques, conformité et réglementation (ch. 12) | Cadre réglementaire (ch. 25 à 30) |
| 6 Agentique | Autonomie N0 à N4 (ch. 8); maturité en cinq niveaux (ch. 14) | Niveaux d'autonomie (§ 4.1.4) |

## Ordre de lecture suggéré

L'ordre du tableau des livrables suit cet ordre de lecture.

1. **NiveauMaturité** pour la vue d'ensemble, à lire avec son échelle propre.
2. **Veille technologique** puis **Revue de littérature** pour l'état des connaissances.
3. **Cadre de référence** pour les exigences applicables.
4. **Compendium** pour l'approfondissement.

## Auteur

André-Guy Bruneau — agbruneau@gmail.com
