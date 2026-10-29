# Interopérabilité et Orchestration en Entreprise Agentique

Corpus documentaire d'André-Guy Bruneau, M.Sc. IT, sur la conception, le déploiement et la supervision d'agents d'IA fondés sur les grands modèles de langue en entreprise, avec un accent sur les services financiers réglementés au Canada.

## Documents

| Document | Nature | Date |
|---|---|---|
| [Veille Technologique.pdf](Veille%20Technologique.pdf) | État de l'art en entreprise : protocoles MCP, A2A et ANP, gouvernance, adoption, sécurité, sept couches implicites. | Faits gelés au 15 août 2026 |
| [Revue de littérature.pdf](Revue%20de%20litt%C3%A9rature.pdf) | Revue de la littérature académique (192 pièces, surtout arXiv) sur dix fronts; confronte trois énoncés de la veille. | Faits gelés au 15 août 2026 |
| [Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf](Cadre%20de%20R%C3%A9f%C3%A9rence%20-%20Interop%C3%A9rabilit%C3%A9%20et%20Orchestration%20en%20Entreprise%20Agentique.pdf) | Cadre normatif d'architecture d'entreprise (CRE-IA-2026-01, v1.1, soumis à l'approbation du comité) : standards, patrons d'orchestration, autonomie et supervision humaine, identité, observabilité, FinOps, conformité. | 28 oct. 2026 |
| [NiveauMaturité.pdf](NiveauMaturit%C3%A9.pdf) | Pile d'interopérabilité en six paliers, propre à ce document : technico-syntaxique, sémantique, chorégraphique, politique, juridique, agentique. | Version 1.0, compilée le 29 oct. 2026 |
| [Compendium.pdf](Compendium.pdf) | Somme en cinq livres et cinquante chapitres : Coopérer, Faire confiance, Encadrer, Appliquer/exploiter, Livrer et clore (horizon 2024-2032). | Gel au 27 juill. 2026, compilé le 24 oct. 2026 (édition de nov. 2026) |

## Statut et limites

- Le **Cadre de référence** (v1.1) est une version finale soumise à l'approbation du comité; il n'est pas encore approuvé.
- Le **Compendium** porte en tête de chaque chapitre son statut de rédaction : chapitres rédigés hors des portes de qualité, sans relecture adversariale. Ses renvois aux volumes I à III et aux fichiers de travail (`TOC.md`, `PRD`) visent des documents absents de ce dépôt.
- La **Veille** (§ 13) décrit une version antérieure du Compendium, en douze livres; la structure en vigueur est celle du Compendium livré.
- Les échelles diffèrent d'un document à l'autre (voir ci-dessous). Un rang ne se cite pas d'une échelle à l'autre.
- La typographie de la ponctuation haute n'est pas harmonisée : NiveauMaturité met une espace insécable avant `?`, le Cadre n'en met généralement pas, les autres documents varient.

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

1. **NiveauMaturité** pour la vue d'ensemble, à lire avec son échelle propre.
2. **Veille technologique** puis **Revue de littérature** pour l'état des connaissances.
3. **Cadre de référence** pour les exigences applicables.
4. **Compendium** pour l'approfondissement.

## Auteur

André-Guy Bruneau — agbruneau@gmail.com
