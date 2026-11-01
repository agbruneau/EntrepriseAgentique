# Interopérabilité et Orchestration en Entreprise Agentique

Corpus documentaire d'André-Guy Bruneau, M.Sc. IT, sur la conception, le déploiement et la supervision d'agents d'IA fondés sur les grands modèles de langue en entreprise, avec un accent sur les services financiers réglementés au Canada.

## Structure du dépôt

```
documents/          Les six livrables en PDF
sources/commun/     Chaîne de composition commune : extracteur de PDF balisé, gabarit Typst, filtre pandoc, contrôles
sources/<document>/ Script de composition de chaque livrable (note-amf, revue, veille, cadre, compendium, niveau-maturite)
                    et son annexe « Actualisation de novembre 2026 » (actualisation-2026-11.html)
sources/annexes/    Sources Typst des annexes « Reprise du 29 octobre 2026 » (Veille et Revue)
LICENSE             Licence des documents (CC BY 4.0); sources/LICENSE : licence du code (MIT)
```

Les documents dont le corpus dépend sans être versés ici sont listés à la section [Documents absents du dépôt](#documents-absents-du-dépôt).

## Livrables

Chaque livrable porte depuis le 1er novembre 2026 une annexe datée « Actualisation de novembre 2026 » (voir [Actualisation de novembre 2026](#actualisation-de-novembre-2026)). Le corps de chaque document reste gelé à sa date.

| Document | Nature | Pages | Date |
|---|---|---|---|
| [NiveauMaturité](documents/NiveauMaturit%C3%A9.pdf) | Pile d'interopérabilité en six paliers, propre à ce document : technico-syntaxique, sémantique, chorégraphique, politique, juridique, agentique. | 6 | Version 1.0, compilée le 29 oct. 2026; actualisation du 1er nov. 2026 en dernière page |
| [Veille technologique](documents/Veille%20Technologique.pdf) | État de l'art en entreprise : protocoles MCP, A2A et ANP, gouvernance, adoption, sécurité, sept couches implicites. | 123 | Faits gelés au 15 août 2026; reprise du 29 oct. 2026 et actualisation du 1er nov. 2026 en annexe |
| [Revue de littérature](documents/Revue%20de%20litt%C3%A9rature.pdf) | Revue de la littérature académique (192 pièces, dont 189 sur arXiv) sur dix fronts; confronte trois énoncés de la veille. L'actualisation de novembre y ajoute une passe neuve de 40 pièces, lues au résumé et non versées au corpus. | 74 | Faits gelés au 15 août 2026; notices reprises le 29 oct. 2026, actualisation du 1er nov. 2026 en annexe |
| [Cadre de référence](documents/Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) | Cadre normatif d'architecture d'entreprise (CRE-IA-2026-01, v1.1, soumis à l'approbation du comité) : standards, patrons d'orchestration, autonomie et supervision humaine, identité, observabilité, FinOps, conformité. | 283 | 28 oct. 2026 (v1.1); actualisation informative du 1er nov. 2026 (annexe H) |
| [Note AMF IA](documents/Note%20AMF%20IA.pdf) | Note d'instruction et profil d'application québécois du cadre (CRE-IA-2026-01-QC, v1.0, version finale pour publication) : ligne directrice de l'AMF sur l'utilisation de l'IA instruite attente par attente (41 attentes), correspondance avec les 272 exigences du cadre, 12 exigences EXIG-AMF, articulation avec la gestion du risque de modèle et recalage du jalon J-AMF au 1er mai 2027. | 44 | 31 oct. 2026 (v1.0); actualisation du 1er nov. 2026 (annexe H) |
| [Compendium](documents/Compendium.pdf) | Somme en cinq livres et cinquante chapitres : Coopérer, Faire confiance, Encadrer, Appliquer/exploiter, Livrer et clore (horizon 2024-2032). | 663 | Gel au 27 juill. 2026, compilé le 24 oct. 2026 (édition de nov. 2026); actualisation du 1er nov. 2026 (annexe N) |

## Statut et limites

- Le **Cadre de référence** (v1.1) est une version finale soumise à l'approbation du comité; il n'est pas encore approuvé.
- La **Note AMF IA** (v1.0) est une version finale pour publication, non encore soumise au comité. Ses états de correspondance ont été revus par quatre relectures assistées par IA; une relecture par la conformité et l'audit interne reste un préalable à l'adoption de ses exigences EXIG-AMF (§ 13.2, point 1). Les reports qu'elle propose au Cadre, au Compendium et à la Veille (annexe D) ne sont pas appliqués à leur corps; les annexes de novembre les présentent (Cadre, H.3; Compendium, N.3; Veille, errata).
- Le **Compendium** a été rédigé hors des portes de qualité, sans relecture adversariale. Ses dettes de vérification ont été instruites le 29 oct. 2026 (journal `VERIFICATIONS.md`, retiré du dépôt au commit `d47db0f` et consultable dans l'historique git). Les traces de sa production (plan de rédaction, décisions d'auteur, garde-fous, portes, remontées, lots de travail) ont été retirées du texte le 31 oct. 2026 (voir [Composition des PDF](#composition-des-pdf)). Ses renvois aux volumes I à III visent des documents absents du dépôt (voir ci-dessous).
- La **Veille** (§ 13) décrit une version antérieure du Compendium, en douze livres; une note datée sous le Tableau 16 le signale, et la structure en vigueur est celle du Compendium livré.
- Les cinq PDF ont été corrigés le 29 oct. 2026 selon `PLAN.md`, par retouche directe faute de sources amont dans ce dépôt; `PLAN.md` et le contrôle `verifier.py` ont été retirés au commit `d47db0f` et restent dans l'historique git. Ces corrections sont dans les PDF d'origine (commit `d28324a`), dont la recomposition du 31 oct. 2026 extrait le texte (voir [Composition des PDF](#composition-des-pdf)).
- La **Veille** et la **Revue** ont été révisées le même jour, en après-midi : errata corrigés à leur place quand ils tenaient dans la ligne, puis une annexe « Reprise du 29 octobre 2026 » ajoutée à chacune (Veille : énoncés datés rouverts sur source primaire, onze errata, références [343] à [371]; Revue : 189 notices arXiv reprises, régimes de preuve recomptés, quatre errata). Le corps reste gelé au 15 août 2026; l'annexe fait foi pour le 29 octobre. Ces ajouts sont repris dans les PDF recomposés; les sources amont, absentes, ne les ont pas reçus.
- Les six livrables ont reçu le 1er nov. 2026 une annexe « Actualisation de novembre 2026 », relevée par des agents LLM (Claude, Anthropic) et contre-vérifiée par échantillon, mais **non relue par l'auteur** (voir [Actualisation de novembre 2026](#actualisation-de-novembre-2026)). Le corps de chaque document n'est pas réécrit; chaque annexe fait foi pour le 1er novembre.
- Les échelles diffèrent d'un document à l'autre (voir ci-dessous). Un rang ne se cite pas d'une échelle à l'autre.
- La typographie de la ponctuation haute n'est pas harmonisée : NiveauMaturité met une espace insécable avant `?`, le Cadre n'en met généralement pas, les autres documents varient.

## Actualisation de novembre 2026

Le 1er nov. 2026, chaque livrable a reçu une annexe datée. La Revue et la Veille ont été actualisées en priorité. Les faits ont été relevés ce jour-là sur source primaire : dépôts de code lus par étiquette et par commit, registre de l'IETF, API d'arXiv et de Crossref, pages des organismes et des régulateurs. Le régime est celui de la reprise du 29 octobre : contre-vérification individuelle, sans ronde adverse.

Chaque annexe déclare ce qui n'a pas pu être vérifié. Le site de l'AMF, notamment, refuse l'outillage automatisé (HTTP 403); un état inconnu n'y est jamais donné pour « inchangé ». Les relevés ont été conduits par des sous-agents LLM. Un échantillon en a été contre-vérifié à la source : les 40 pièces de la passe de la Revue, les 36 DOI de sa passe de contrôle, et des étiquettes git, états IETF et pages web de la Veille, du Cadre et de la Note AMF.

| Document | Annexe | Contenu |
|---|---|---|
| Revue de littérature | « Actualisation de novembre 2026 », tableaux 12 à 17, réf. [193] à [242] | Voir le détail ci-dessous. |
| Veille technologique | « Actualisation de novembre 2026 », tableaux 27 à 30, réf. [372] à [430] | Voir le détail ci-dessous. |
| Cadre de référence | H, informative, tableaux 70 à 72, réf. [474] à [495] | Dépendances datées des exigences rouvertes, avec la conséquence pour le comité (OAuth 2.1 −17, calendrier MCP, stades des extensions, a2a-tck, MITRE ATLAS, RIA). Neuf reports de la Note AMF IA présentés sans être appliqués. Erratum : le comité directeur technique d'A2A compte neuf sièges depuis le 20 oct. 2026 (§ 6.6). Aucune exigence n'est modifiée. |
| Note AMF IA | H, tableaux H.1 à H.3 | Faits datés rouverts et points ouverts du § 13.2, dont aucun n'est fermé. Errata : l'art. 12.1 de la loi sur le secteur privé est édicté par l'art. 110 de L.Q. 2021, c. 25, et entre en vigueur par son art. 175, non par ses art. 102 et 165(3); titre officiel d'E-23. La version 1.0 n'est pas modifiée. |
| Compendium | N, tableaux N.1 et N.2, réf. [AN-1] à [AN-27] | Protocole de revalidation du ch. 50 appliqué aux quatorze événements du tableau 50.1 : deux survenus, un à moitié, dix non survenus, un non revalidé. Quatre reports de la Note AMF IA. Aucune entrée du socle n'est amendée. |
| NiveauMaturité | Dernière page | Ancrages datés des paliers 2, 5 et 6 au 1er novembre (ISO 20022 et rail temps réel, Loi 25, E-23, ligne directrice IA de l'AMF, A2A et MCP). Aucun palier ne change. |

Détail de la Revue :

- Les 189 notices arXiv sont reprises : aucune révision depuis le 29 octobre, et les mêmes régimes (16 attestées, 34 auto-déclarées, 139 sans signe).
- La passe de contrôle sur Crossref est refaite : 36 pièces sans attestation en notice ont une version publiée, dont 22 « sans signe ».
- Une passe neuve couvre les dépôts du 14 août au 29 octobre 2026 : 40 pièces, quatre par front, lues au résumé et non versées au corpus. Les trois énoncés de la veille sont rouverts.
- Quatre errata, dont le rendu « MSR “26 » de l'édition du 31 octobre.

Détail de la Veille :

- Chaque ligne du tableau 25 est rouverte. `draft-chen-oauth-agent-revocation` est relancé le 30 octobre; OAuth 2.1 passe en −17; le registre MCP passe en v1.8.7; la norme EN 18286 est attestée en source primaire.
- Les sept objets non rouverts le 29 octobre le sont : plateformes, OWASP, CSA, MPP, Cloudflare, FIDO, W3C, analystes, incident de juillet 2026.
- Errata :
  - date de la ligne directrice IA de l'AMF;
  - passage d'A2A sous l'AAIF, établi en source primaire dès août, de sorte que le Cadre (réf. [5]) avait raison;
  - entrée en vigueur des règles du RTR;
  - quatre énoncés du corps déjà inexacts au 15 août.

## Documents absents du dépôt

Le corpus s'appuie sur des documents qui ne sont pas versés ici. Leur absence n'empêche pas la lecture, mais elle empêche de vérifier une partie des citations et de recompiler les PDF depuis leurs sources.

| Document | Qui y renvoie | Conséquence de l'absence |
|---|---|---|
| Sources amont des PDF : Typst 0.15.1 pour la Veille, la Revue et le Compendium; HTML imprimé par Chrome pour le Cadre et NiveauMaturité (d'après les métadonnées des PDF) | Les cinq livrables | Recompilation depuis la source impossible. Les PDF se recomposent à partir de leur édition d'origine (voir [Composition des PDF](#composition-des-pdf)); NiveauMaturité, depuis sa source HTML de l'historique git (commit `4457a54`), corrections du 29 oct. 2026 reportées. |
| Vol. I — *Interopérabilité agentique* (7 ch.) | Compendium (373 renvois); Veille § 4.12 et § 13 | Renvois invérifiables depuis ce dépôt. |
| Vol. II — *L'autonomie encadrée* (24 ch.) et son socle coté (46 entrées) | Compendium (542 renvois); Veille § 8.4 et § 13 | Faits repris du socle invérifiables depuis ce dépôt. |
| Vol. III — *L'entreprise agentique* et ses fiches F-xx et H-xx | Compendium (858 renvois, dont 123 fiches distinctes citées comme sources); Veille § 7.6 et § 13 | Énoncés appuyés sur une fiche invérifiables depuis ce dépôt. |
| Démonstrateur Borealis-Go (Vol. I) | Veille § 4.12 | Retiré de son dépôt le 25 juill. 2026 (Veille § 13.2), rejouable dans le seul historique git de ce dépôt-là. |
| Fichiers de travail : `PRD/PRD.md` (dont les décisions d'auteur D-n, § 15), `PRD/socle-consolide.md`, `PRD/TOC.md`, `PRD/gel-2026-07-27.md`, `PRD/gel-2026-07-28-volet-residuel.md`, `annexe-references.md` | Compendium d'origine (commit `d28324a`) : 9 liens de fichier (p. 152, 154, 279, 280, 353 et 940) et renvois aux décisions D-n, retirés de l'édition recomposée | La teneur des décisions D-18 et D-21, qui fixent le périmètre du dépôt à cinq livrables, n'est pas consultable. |

Au 15 août 2026, la Veille (§ 13.8) décrit les volumes III et IV comme diffusés à leur seul auteur, faute de relecteur distinct; le Vol. IV est depuis versé ici comme Compendium (décision D-21). L'absence des volumes I à III peut donc être voulue.

## Sources des annexes

Les annexes du 29 octobre de la Veille et de la Revue se recompilent séparément avec Typst 0.15.1; `tpl.typ` porte la mise en page commune. Les PDF produits sont ignorés par git.

```bash
typst compile sources/annexes/veille_annexe.typ
```

```bash
typst compile sources/annexes/revue_annexe.typ
```

Les annexes de l'actualisation de novembre sont en HTML, une par livrable : `sources/<document>/actualisation-2026-11.html`. Chaque script les compose après le corps, avec les mêmes contrôles mot à mot. Leurs tableaux et leurs références continuent les suites du document. Le Cadre et la Note AMF prennent l'annexe H; le Compendium, l'annexe N, avec les tableaux N.1… et les références [AN-1]…. Pour modifier une annexe, éditer son fichier HTML puis relancer le script du document.

## Composition des PDF

Depuis le 31 oct. 2026, les six PDF partagent une même mise en page : format lettre, texte justifié avec césure française (Libertinus Serif), titres et tableaux en Segoe UI, couverture avec fiche, table des matières, en-tête courant du chapitre, pied « Page X sur N ». La chaîne commune est dans `sources/commun/` : `extraire.py` convertit un PDF balisé en HTML structuré, `composer.py` passe ce HTML par pandoc (`filtre.lua`) et Typst 0.15.1 (`gabarit.typ`). Chaque script refuse d'écrire son PDF si un mot de la source y manque; ceux qui partent d'un PDF contrôlent aussi la complétude de l'extraction.

Outillage requis : Python 3 avec PyMuPDF, pandoc 3.9 et Typst 0.15.1. Un pandoc plus ancien ne convient pas : la 3.1 écrit `#blockquote`, que Typst ne connaît pas (NiveauMaturité échoue), et pagine autrement la Veille et la Note AMF. Sans Segoe UI (police de Windows), le gabarit se replie sur Selawik, police libre que Microsoft publie comme substitut de Segoe UI (licence SIL OFL 1.1). Il faut la fournir à Typst par `TYPST_FONT_PATHS`. Selawik n'a pas d'italique : les intertitres en italique sans empattement sortent alors en romain. Les six PDF de l'actualisation du 1er nov. 2026 ont été recomposés sous Linux, donc en Selawik. La Veille, la Revue, la Note AMF et NiveauMaturité gardent la pagination de leur corps. Le Cadre et le Compendium, plus chargés de tableaux, raccourcissent de une à deux pages, car Selawik est un peu plus étroite que Segoe UI Variable.

Sources de chaque livrable :

- **Note AMF IA** : `sources/note-amf/note-amf-ia.html`, export HTML de sa source Claude Docs ([lien](https://claude.ai/artifact/RBLR169KURVcsLrP1NE6PS), accès réservé à l'auteur). Après une modification de la source, réexporter le HTML par-dessus ce fichier; si les dates du calendrier du § 12 changent, les reporter dans `calendrier.typ`.
- **Veille, Revue, Cadre, Compendium** : leur PDF d'origine, lu dans git au commit `d28324a` (aucune source amont dans le dépôt). Le script ne lit jamais le PDF recomposé.
- **Compendium**, en plus : `retraits.py` retire du texte extrait les traces de production, avant composition. Des règles ôtent environ 440 renvois de pure forme (« (R-13 du Vol. III) », « (décision 15 du TOC) », « au sens de R-14 du Vol. III »). Ensuite, 879 substitutions comptées (`retraits.json`) réécrivent 732 phrases et en retirent 104. Le script s'arrête si une substitution ne trouve pas son nombre d'occurrences attendu, ou si une trace de la liste de contrôle subsiste.
- **NiveauMaturité** : sa source HTML au commit `4457a54`, avec les corrections du 29 oct. 2026 reportées par le script; texte contrôlé contre le PDF d'origine.

```bash
python sources/<document>/construire_pdf.py
```

Limites de la recomposition :

- Les renvois internes (« tableau 31 », « section 6.8 ») sont du texte, non des liens; les URL restent des liens.
- Jusqu'au 1er nov. 2026, l'apostrophe en tête d'une année élidée (« MSR ’26 », « NSDI ’20 ») sortait en guillemet ouvrant (« MSR “26 ») : deux fois dans le Cadre, neuf dans le Compendium, deux dans la Revue (tableau 8, réf. [59]). `filtre.lua` la passe désormais en caractère littéral.
- Les schémas du Cadre (28, repris en vectoriel) et les figures du Compendium (118, en images à 200 dpi) gardent le style de l'original; le texte des figures du Compendium n'est plus sélectionnable.
- Les pastilles de l'annexe A du Cadre deviennent du texte et ses cases à cocher disparaissent.
- Dans le Compendium, l'ordre du texte de quelques cellules retouchées à la main (p. 736, 803, 905 et 940 de l'original; tableau 47.2) reste approximatif.
- Le retrait des traces du Compendium épargne ce qui qualifie une affirmation pour le lecteur : régimes [A]/[B]/[C], socle et relève, degrés d'absence, cotes F-xx, H-xx et S-xxx, renvois aux volumes I à III. Il ne touche pas les figures, dont le texte est en image. Les phrases réécrites l'ont été sans relecture humaine; l'édition d'origine reste au commit `d28324a`.

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
3. **Cadre de référence** pour les exigences applicables (et **Note AMF IA** pour son profil d'application québécois).
4. **Compendium** pour l'approfondissement.

## Licence

- Documents (`documents/`, annexes) : [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). Réutilisation et adaptation libres, avec attribution à l'auteur.
- Code de composition (`sources/`) : [licence MIT](sources/LICENSE).

## Auteur

André-Guy Bruneau — agbruneau@gmail.com
