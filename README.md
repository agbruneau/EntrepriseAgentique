# Interopérabilité et Orchestration en Entreprise Agentique

**Présentation en ligne : [agbruneau.github.io/EntrepriseAgentique/Presentation.html](https://agbruneau.github.io/EntrepriseAgentique/Presentation.html)**

## Résumé

Le corpus traite de la conception, intégration, gouvernance et supervision d'agents d'intelligence artificielle fondés sur les grands modèles de langue en contexte d'entreprise, plus particulièrement au sein des services financiers réglementés au Canada. Il s'inscrit dans le champ de l'ingénierie des systèmes, envisagée sous l'angle de l'architecture d'entreprise et de l'interopérabilité. L'entreprise agentique y est appréhendée comme un ensemble de systèmes hétérogènes et distribués, conçus et exploités de manière indépendante, qu'il convient de faire interopérer. Le corpus en examine l'architecture de référence, les exigences, le cycle de vie, la vérification et la conformité. L'orchestration y est rattachée à l'intégration d'entreprise et à la gestion des processus d'affaires : coordination de traitements distribués, exécution durable et chorégraphie. L'agentique ressortit quant à elle à l'intelligence artificielle, et plus précisément aux systèmes multiagents. Le corpus en approfondit l'interopérabilité protocolaire, l'identité, la délégation et l'autonomie encadrée, le tout documenté dans six livrables :

- **Échelle de maturité** de l'interopérabilité en six paliers (NiveauMaturité);
- **Veille technologique** sur les protocoles, les normes et l'adoption en entreprise;
- **Revue de littérature** académique de 192 pièces, répartie sur dix fronts;
- **Cadre de référence** normatif d'architecture d'entreprise (CRE-IA-2026-01, 296 exigences en version 1.2);
- **Note d'instruction** de la ligne directrice de l'Autorité des marchés financiers (AMF) sur l'utilisation de l'intelligence artificielle, qui en dérive un profil d'application québécois du cadre;
- **Compendium** de synthèse en cinq livres et cinquante chapitres.

## Livrables

Chaque livrable porte depuis le 1er novembre 2026 une annexe datée « Actualisation de novembre 2026 », placée en fin de document (colonne Date). Le corps de chaque document reste gelé à sa date; l'annexe fait foi pour la date qu'elle porte.

| Document                                                                | Nature                                                                                                                                                                                                                                                                                                                                                                                             | Pages | Date                                                                                                               |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| [NiveauMaturité](documents/NiveauMaturit%C3%A9.pdf)                     | Pile d'interopérabilité en six paliers, propre à ce document : technico-syntaxique, sémantique, chorégraphique, politique, juridique, agentique.                                                                                                                                                                                                                                              | 6     | Version 1.0, compilée le 29 oct. 2026; actualisation du 1er nov. 2026 en dernière page                           |
| [Veille technologique](<documents/Veille%20Technologique.pdf>)           | État de l'art en entreprise : protocoles MCP, A2A et ANP, gouvernance, adoption, sécurité, sept couches implicites.                                                                                                                                                                                                                                                                             | 126   | Faits gelés au 15 août 2026; reprise du 29 oct. 2026, actualisation du 1er nov. 2026 et relecture du 3 nov. 2026 en annexe |
| [Revue de littérature](<documents/Revue%20de%20litt%C3%A9rature.pdf>)   | Revue de la littérature académique (192 pièces, dont 189 sur arXiv) sur dix fronts; confronte trois énoncés de la veille. L'actualisation de novembre y ajoute une passe neuve de 40 pièces, lues au résumé et non versées au corpus.                                                                                                                                                     | 78    | Faits gelés au 15 août 2026; notices reprises le 29 oct. 2026, actualisation du 1er nov. 2026 et relecture du 3 nov. 2026 en annexe |
| [Cadre de référence](<documents/Cadre%20de%20R%C3%A9f%C3%A9rence.pdf>) | Cadre normatif d'architecture d'entreprise (CRE-IA-2026-01, v1.2, soumis à l'approbation du comité) : standards, patrons d'orchestration, autonomie et supervision humaine, identité, observabilité, FinOps, conformité. La v1.2 applique les correctifs de la revue contradictoire du 3 nov. 2026 ([rapport](DEEP_REVIEW_CADRE_REFERENCE.md), registre en annexe H.6).                                                                                                                                                                      | 372   | 3 nov. 2026 (v1.2); actualisation informative du 1er nov. 2026 et correctifs de la revue du 3 nov. 2026 (annexe H)                                         |
| [Note AMF IA](<documents/Note%20AMF%20IA.pdf>)                           | Note d'instruction et profil d'application québécois du cadre (CRE-IA-2026-01-QC, v1.0, version finale pour publication) : ligne directrice de l'AMF sur l'utilisation de l'IA instruite attente par attente (41 attentes), correspondance avec les exigences du cadre (272 des 287 de la v1.1 relues; erratum H.3 no 3), 12 exigences EXIG-AMF, articulation avec la gestion du risque de modèle et recalage du jalon J-AMF au 1er mai 2027. | 44    | 31 oct. 2026 (v1.0); actualisation du 1er nov. 2026 (annexe H)                                                     |
| [Compendium](documents/Compendium.pdf)                                   | Somme en cinq livres et cinquante chapitres : Coopérer, Faire confiance, Encadrer, Appliquer/exploiter, Livrer et clore (horizon 2024-2032).                                                                                                                                                                                                                                                      | 699   | Gel au 27 juill. 2026, compilé le 24 oct. 2026 (édition de nov. 2026); actualisation du 1er nov. 2026 et relecture du 3 nov. 2026 (annexes J et N) |

## Présentation

Synthèse en onze diapositives pour la haute direction, publiée sur GitHub Pages : **[agbruneau.github.io/EntrepriseAgentique/Presentation.html](https://agbruneau.github.io/EntrepriseAgentique/Presentation.html)** (source : [Presentation.html](Presentation.html)).

- Diapos 1 à 10 : thèse, paradoxe adoption / assurance, échelle de maturité, protocoles, architecture de référence, dix décisions, vue d'ensemble du Cadre (§ 5.1, figure 3), autonomie, conformité AMF, pilotage.
- Diapo 11 (annexe) : les six livrables en PDF, chacun ouvert dans un nouvel onglet pour lecture dans le navigateur.
- Navigation : flèches, 1 à 9 et 0 pour un accès direct, S pour le sommaire, F pour le plein écran, Maj+P pour le PDF A4 paysage.
- Vérification de la mise en page (Edge ou Chrome sans interface) : `node outils/verifier-presentation.mjs [largeur] [hauteur] [print]`.

## Ordre de lecture suggéré

Le tableau des livrables suit cet ordre.

1. **NiveauMaturité** pour la vue d'ensemble; son échelle en six paliers lui est propre.
2. **Veille technologique** pour l'état de l'art en entreprise, puis **Revue de littérature**, qui confronte trois de ses énoncés à la littérature académique.
3. **Cadre de référence** pour les exigences applicables, puis **Note AMF IA**, qui en dérive le profil d'application québécois.
4. **Compendium** pour l'approfondissement. Son corps, gelé au 27 juillet 2026, est le plus ancien du corpus : le lire avec son annexe N, qui en revalide les échéances et présente les reports proposés par la Note AMF IA.

## Structure du dépôt

- `documents/` : les six livrables en PDF, seuls fichiers de référence.
- `sources/` : chaîne de recomposition des PDF (Python, pandoc 3, Typst 0.15.1) et annexes d'actualisation en HTML, un dossier par livrable, plus `commun/` (chaîne partagée) et `annexes/` (annexes Typst de la reprise du 29 octobre 2026, Veille et Revue); `python sources/<livrable>/construire_pdf.py` recompose un livrable et contrôle que tout le texte source se retrouve dans le PDF. Polices requises : voir l'en-tête de `sources/commun/composer.py`.
- `outils/verifier-presentation.mjs` : vérification de la mise en page de la présentation.
- `Presentation.html` : la présentation, page autonome (figure intégrée, polices Google Fonts).

## Licence

- Documents (`documents/`, annexes, `Presentation.html`) : [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). Réutilisation et adaptation libres, avec attribution à l'auteur.
- Code de composition (`sources/`) : [licence MIT](sources/LICENSE).

## Auteur

André-Guy Bruneau M.Sc. IT — agbruneau@gmail.com
