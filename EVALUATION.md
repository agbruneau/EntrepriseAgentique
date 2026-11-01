# Évaluation académique du corpus « Interopérabilité et Orchestration en Entreprise Agentique »

| | |
|---|---|
| Objet | Les six livrables du dépôt (1 138 pages, environ 663 000 mots) et leur chaîne de composition, état au commit `70fd758` |
| Auteur évalué | André-Guy Bruneau, M.Sc. IT |
| Évaluateur | Claude Opus 5.5 (Anthropic), à la demande de l'auteur |
| Date | 31 octobre 2026 |
| Niveau de référence | Cycles supérieurs : maîtrise de recherche ou doctorat professionnel en TI |
| Note globale | **79 / 100** — accepté avec corrections modérées |

## Verdict

Le corpus relève des cycles supérieurs par sa rigueur épistémique, qui dépasse ce qu'on attend d'un mémoire de maîtrise. Chaque énoncé y est daté, rattaché à un régime de preuve et borné par ce qu'il n'établit pas. Les erreurs sont corrigées en public plutôt qu'effacées. Tous les contrôles d'exactitude menés pour cette évaluation concordent avec le texte (section 5). La Revue de littérature et la Note AMF IA sont les pièces les plus abouties. La Revue y ajoute une thèse originale : la littérature du champ ne porte, à sa notice, presque aucune attestation d'arbitrage.

Trois faiblesses plafonnent la note. Le corpus n'apporte aucune donnée empirique propre et son Cadre n'a été validé ni sur le terrain ni par un expert humain externe. Une part importante de ses renvois vise des documents absents du dépôt, surtout dans le Compendium. Enfin, la prose est dense et chargée de méta-commentaire sur sa propre fabrication, ce qui la rend peu accessible aux publics qu'elle vise.

## 1. Méthode de l'évaluation et ses limites

**Couverture.** Le corpus dépasse ce qu'un évaluateur peut lire en entier dans une seule séance. Le tableau dit ce qui a été lu en profondeur et ce qui n'a été que contrôlé.

| Document | Pages | Lu en profondeur | Contrôlé sur le texte intégral |
|---|---|---|---|
| NiveauMaturité | 5 | Intégral | — |
| Revue de littérature | 48 | Résumé, § 1 à 5, § 14 à 18, annexes, échantillon de références (environ 60 %) | Recomptes arithmétiques |
| Veille technologique | 109 | Résumé, § 1-2, § 8.4, § 10, § 14, extraits d'annexes (environ 15 %) | Table des matières, recherches ciblées |
| Note AMF IA | 39 | Sommaire exécutif, partie I (environ 25 %) | Table des matières, décomptes |
| Cadre de référence | 277 | Méthode, début du ch. 8, échantillon d'exigences, annexe F (environ 5 %) | Décompte des 272 exigences |
| Compendium | 660 | Table des matières, début du ch. 22 (moins de 2 %) | Décompte des marqueurs de production et d'épistémie |

**Contrôles.** Trois sortes de contrôles ont été menées :
- des recomptes arithmétiques sur les totaux publiés;
- six faits datés vérifiés sur le Web;
- neuf notices arXiv confrontées de mémoire, sans consultation en ligne.

Le texte a été extrait par `pdftotext`; les tableaux en sortent déstructurés, et leur lecture est donc moins sûre que celle de la prose.

**Limites.** Quatre réserves bornent la portée de ce rapport :
- Les notes du Cadre et du Compendium reposent sur un échantillon. Un chapitre non lu peut contenir des défauts ou des qualités que ce rapport ne voit pas.
- L'évaluateur appartient à la famille de modèles qui a servi à produire une partie du corpus (Veille, § 2.1 : « agents LLM (Claude, Anthropic) »). Ce lien expose à des angles morts partagés. Une évaluation par un jury humain reste nécessaire.
- Aucune expertise juridique n'est engagée ici : la justesse des qualifications réglementaires n'est pas évaluée.
- L'absence de divulgation de l'IA dans le Cadre et le Compendium est une inférence tirée de recherches par mots-clés, non d'une lecture intégrale.

## 2. Grille de notation

| Critère | Poids | Note | Justification |
|---|---|---|---|
| Pertinence et originalité de la contribution | 15 | 13 | Objet très actuel, ancrage canadien et québécois rare. La thèse sur le régime de preuve (Revue) et l'instruction de la ligne directrice de l'AMF sont originales. Les taxonomies, elles, sont empruntées (EIF, LCIM, OO1-OO4 d'une source unique). |
| Rigueur méthodologique | 20 | 16 | Régimes de preuve, gels datés, passes de contrôle inverses : un niveau exceptionnel. Restent une revue non systématique à juge unique, des agents de vérification non caractérisés, aucune revue humaine externe et aucune validation empirique du Cadre. |
| Exactitude et appareil de citation | 15 | 13 | Tous les contrôles concordent (section 5). Mais une large part des renvois du Compendium est invérifiable, et la catégorie A du Cadre est trop permissive. |
| Analyse critique et synthèse | 15 | 13 | Désaccords nommés, avec l'expérience qui les arbitrerait (Revue, tableau 7), énoncés de la Veille mis à l'épreuve, autoréfutations publiées. L'appareil critique écrase parfois la synthèse. |
| Cohérence du corpus | 10 | 7 | Le décompte des 272 exigences est cohérent d'un document à l'autre, et le README relie les échelles. En revanche, plusieurs échelles ne se superposent pas, quatre dates de gel coexistent, la Veille (§ 13) décrit un Compendium obsolète et les reports proposés par la Note ne sont pas appliqués. |
| Clarté, style et accessibilité | 10 | 6 | Le français est précis et le vocabulaire maîtrisé. Mais la densité est extrême, les corrections sont narrées dans le corps du texte et le Compendium laisse voir ses artefacts de production. |
| Applicabilité professionnelle | 10 | 8 | Exigences testables à points d'application nommés; profil AMF avec calendrier. Mais rien n'est encore approuvé ni mis à l'essai, et le volume freine l'adoption. |
| Reproductibilité, transparence et éthique | 5 | 3 | Les limites sont très bien déclarées. En revanche, les sources amont sont absentes, la divulgation de l'IA est inégale et le dépôt public n'a pas de licence. |
| **Total** | **100** | **79** | |

Équivalence indicative : B+ à A-, selon le barème de l'établissement.

## 3. Appréciation par document

Les notes de cette section sont indicatives; seule la grille de la section 2 fait foi.

### 3.1 NiveauMaturité (5 p.) — 70

**Forces.** Le document est d'une clarté pédagogique remarquable. Chaque palier tient en une question, une explication « en clair », un mode de défaillance et un exemple concret. L'heuristique de diagnostic (« la panne est toujours au palier qu'on croyait acquis ») est utile en pratique.

**Faiblesses.**
- Le titre annonce une échelle de maturité, mais le document décrit une pile de couches : aucun critère ne dit quand un palier est atteint.
- Le découpage en six paliers n'est pas justifié face à l'EIF (quatre couches) et au LCIM (sept niveaux). Une note de bas de page ne suffit pas.
- Le palier 6 rompt la logique de pile, et le document le reconnaît (« changement de nature ») sans en tirer la conséquence.
- Le document ne cite aucune source.
- Les sections « chez nous » supposent une organisation que le document ne nomme pas.

### 3.2 Veille technologique (109 p.) — 84

**Forces.**
- Le dispositif de recherche est explicite : 106 agents, 531 requêtes, vote de réfutation à deux sur trois. Quinze passes de vérification sont consignées (tableau 1), sous un régime fort ou faible déclaré.
- La prospective sépare ce qui est programmé, ce qui est projeté et ce qui est spéculatif (§ 12) : une hygiène épistémique exemplaire.
- Six énoncés porteurs de l'édition précédente sont réfutés en dix jours, et le document le dit (§ 14).
- L'analyse canadienne est originale : quinze croisements entre protocoles et textes canadiens, aucun lien documenté par source primaire (§ 8.4).
- La lecture du règlement européen est plus fine que certaines sources secondaires consultées pour ce rapport. Elle distingue l'application de l'article 50 au 2 août 2026 du seul délai de grâce de l'article 111(4).

**Faiblesses.**
- Le résumé surévalue la méthode : il annonce que « chaque affirmation » est soumise à contradiction, alors que le § 2.1 fait couvrir une partie du corpus par un régime faible, sans ronde adverse.
- Le décompte de quatorze contributions gonfle l'apport.
- Les corrections signalées par « ✎ » dans le corps alourdissent la lecture.
- L'appui sur les volumes compagnons du même auteur est circulaire; le document le déclare au § 10.
- Les énoncés sur l'AMF y restent au conditionnel, alors que la Note AMF a depuis atteint la source primaire.

### 3.3 Revue de littérature (48 p.) — 88

**Forces.** C'est la meilleure pièce du corpus.
- Sa question est double, et la seconde partie, le régime de preuve, commande la première.
- Le corpus est réparti en trois régimes de preuve (tableau 1 : 12, 32 et 145 pièces sur 189).
- Une passe de contrôle inverse sur DBLP, Crossref et OpenAlex borne le biais dans les deux sens (§ 17). Une revue qui cherche à réfuter son propre résultat central, c'est rare.
- Le tableau 7 associe à chacun des dix désaccords l'expérience qui le trancherait, et le § 16 en tire un programme de recherche testable.
- Les reprises du 15 août et du 29 octobre documentent la péremption du corpus : sept résumés ont changé, et la pièce [71] ne porte plus le chiffre décisif que la revue lui attribuait.
- Tous les totaux recomptés sont exacts.

**Faiblesses.**
- La revue interroge arXiv seul, avec un juge unique et sans double codage. Elle le déclare, mais son résultat principal (77 % sans signe de revue) devient ainsi en partie un artefact de sa source, ce qu'elle admet elle-même.
- Le critère de la notice sous-déclare l'arbitrage. De mémoire de l'évaluateur, à confirmer, GAIA [23] a paru à ICLR 2024 et [48] à NeurIPS 2025, et les deux sont classés sans revue. Le plafond de 145 est donc probablement lâche.
- Les « agents indépendants » de la passe neuve (§ 2.1) ne sont caractérisés ni par leur nature, ni par leur consigne, ni par leur fiabilité mesurée.
- Le décompte du § 14.3 n'a pas été refait après la reprise.
- Le § 15 date la Veille au 8 août, alors que celle-ci est gelée au 15 août.

### 3.4 Cadre de référence (277 p.) — 82

**Forces.**
- Les 272 exigences uniques sont rédigées au registre DOIT / NE DOIT PAS et sont vérifiables. Chacune est rattachée à un point d'application nommé : passerelle, registre ou fiche d'agent.
- Les échelles sont unifiées : autonomie N0 à N4, paliers de risque P0 à P3.
- Certaines exigences traduisent directement un résultat de la littérature. Ainsi, EXIG-ORC-02 exige une preuve mesurée avant d'adopter une architecture multi-agents.
- L'annexe F publie des statistiques de validation peu flatteuses : 61 références sur 121 étaient de catégorie C, et 302 liens affirmation-source sur 427 exigeaient correction. Ce niveau d'honnêteté est rare.
- Les faits techniques contrôlés sont exacts (section 5).

**Faiblesses.**
- La catégorie A admet la documentation d'un éditeur sur son propre produit et les communiqués d'analystes comme « appui de toute exigence et de tout fait » (tableau 66). Or une source primaire de l'allégation n'est pas une preuve du fait : une prévision de Gartner atteste ce que Gartner prévoit, non ce qui arrivera.
- Le document passe de la v0.1 à la v1.1 en deux jours (27-28 oct. 2026), et 1 409 affirmations sont auditées en une journée. Un tel rythme suppose une forte automatisation, que le document ne divulgue pas. Il ne dit pas non plus qui ou quoi est le « second examinateur indépendant ».
- Le Cadre n'a été validé ni par un pilote, ni par une étude de cas, ni par un panel d'experts, et il n'est pas encore approuvé.
- Il est couplé à des versions courantes de spécifications, ce qui l'expose à une obsolescence rapide; le catalogue trimestriel l'atténue.

### 3.5 Note AMF IA (39 p.) — 87

**Forces.** C'est un modèle d'analyse réglementaire appliquée.
- L'unité d'extraction est définie, et chaque attente reçoit un identifiant stable. La Note donne deux granularités : 41 regroupements et 65 à 72 énoncés.
- Une échelle à quatre marqueurs (Confirmé, Probable, Hypothèse, À vérifier) qualifie chaque énoncé.
- Ce que la Note ne peut pas établir est dit explicitement (§ 2.5).
- Les écarts sont expliqués par la structure du Cadre, non comme des oublis.
- La Note relève aussi les points où le Cadre va plus loin que l'AMF.
- L'accès à la source primaire est documenté, y compris le refus HTTP 403 contourné par une session de navigateur.
- La Note comble une lacune que trois autres documents du corpus désignaient : c'est la preuve que le corpus sait se corriger.

**Faiblesses.**
- Les correspondances restent le jugement d'un lecteur unique, revu par des relectures assistées par IA, sans relecture par la conformité ni par les affaires juridiques. La Note le déclare elle-même.
- Les lignes directrices connexes de l'AMF ne sont pas lues; celle sur le risque de modèle ne l'est qu'en partie.
- Les reports proposés aux autres documents (annexe D) n'y sont pas appliqués.
- La Note entière, de la v0.1 à la v1.0, a été produite en un jour.

### 3.6 Compendium (660 p.) — 68

**Forces.**
- L'ambition est encyclopédique et cohérente : cinq livres, cinquante chapitres, horizon 2024-2032.
- La thèse unificatrice tient en cinq termes : contrat protocolaire, identité et délégation, contrôle de finalité, mesure en exploitation, provenance.
- Le marquage épistémique est systématique : environ 339 « Lecture de l'auteur » et 181 « Ce que le socle établit ».
- Les réserves de source viennent d'emblée : le ch. 22 annonce que la taxonomie OO1-OO4 repose sur une seule prépublication.

**Faiblesses.**
- Le volume a été rédigé hors des portes de qualité (README).
- Des artefacts de production restent dans le texte destiné au lecteur : « TOC » (187 occurrences), « PRD » (102), « balayage » (136), décisions D-n (59), et des phrases comme « TOC v0.30, deux thèses examinées, zéro écart ».
- 1 773 renvois aux volumes I à III, absents du dépôt, et 1 181 mentions de fiches F-xx rendent une large part du texte invérifiable; neuf liens de fichier sont morts.
- Le volume reprend largement des contenus de la Veille et du Cadre.
- Depuis la recomposition, le texte des 118 figures est en image et n'est plus sélectionnable, ce qui nuit à l'accessibilité.
- Le caractère « publiable » est décrété (décision D-20) plutôt que démontré.

## 4. Constats transversaux

### Forces

1. **Une épistémologie appliquée de haut niveau.** Gels datés, régimes de preuve nommés, partage entre ce qu'une pièce établit et ce qu'elle n'établit pas : le corpus applique à lui-même les exigences qu'il formule pour le champ.
2. **Une autocorrection publique.** Errata, reprises datées et résultats réfutés sont publiés plutôt que corrigés en silence.
3. **Une exactitude vérifiée.** Aucun des contrôles menés n'a trouvé d'erreur factuelle ni arithmétique.
4. **Un ancrage réglementaire canadien et québécois** que la littérature internationale ne traite presque pas (E-23, Loi 25, AMF, ACVM, Paiements Canada).
5. **Une chaîne de composition contrôlée.** Chaque script refuse d'écrire son PDF si un mot de la source y manque.

### Faiblesses

1. **La lisibilité.** La densité, les longues phrases et le récit des corrections dans le corps du texte servent la traçabilité, mais desservent le comité, les décideurs et les praticiens visés.
2. **Aucune contribution empirique propre.** Le corpus n'apporte ni étude de cas, ni mesure de déploiement, ni entretien; le démonstrateur Borealis-Go a été retiré. Au niveau doctoral, c'est la principale lacune.
3. **Aucune validation humaine externe.** La vérification repose sur des agents d'IA dont la fiabilité n'est pas mesurée (par exemple par un accord inter-juges avec un humain). La divulgation de l'IA est inégale : explicite dans la Veille et la Note AMF, introuvable dans le Cadre et le Compendium.
4. **Une vérifiabilité limitée.** Une part importante des renvois vise des documents absents, et l'autocitation entre volumes compte, de l'aveu même de la Veille (§ 10), pour un seul témoignage.
5. **Une fragmentation temporelle et d'échelles.** Les documents sont gelés au 27 juillet, au 15 août, au 27-28 octobre et au 31 octobre 2026. Une dizaine d'échelles ne se superposent pas, et le README doit avertir qu'« un rang ne se cite pas d'une échelle à l'autre ».
6. **Un statut de diffusion incohérent.** Le Cadre et la Note portent la classification « Usage interne », mais ils sont publiés dans un dépôt GitHub public, sans licence.
7. **Une reproductibilité partielle.** Les sources amont sont absentes : quatre PDF se recomposent à partir de PDF, et la chaîne n'a ni tests ni intégration continue.

## 5. Vérifications effectuées

| Énoncé du corpus | Contrôle | Résultat |
|---|---|---|
| Ligne directrice IA de l'AMF : couverture « mars 2026 », page Web « avril 2026 », prise d'effet le 1er mai 2027 (Note AMF) | Blakes : publication le 7 avril 2026, prise d'effet le 1er mai 2027 | Concordant |
| Le 1er mai 2027 tombe un samedi (Note AMF, sommaire) | Calcul calendaire | Exact |
| Révision MCP 2026-07-28, méthode `server/discover`, cache à TTL et portée (Cadre, EXIG-MCP-02 et 03) | modelcontextprotocol.io | Concordant |
| E-23 : version finale du 11 sept. 2025, entrée en vigueur le 1er mai 2027 (Veille, § 8.4) | BSIF | Concordant |
| WIMSE adopte AIMS le 15 sept. 2026, document informationnel, sans protocole neuf (Revue, annexe) | Datatracker de l'IETF | Concordant (date d'adoption confirmée par une source secondaire) |
| Règlement (UE) 2026/1744 : haut risque reporté au 2 déc. 2027 (annexe III) et au 2 août 2028 (annexe I), publié au JO le 24 juillet (Veille, § 8.1) | Sources secondaires concordantes | Concordant, non vu sur EUR-Lex |
| Neuf notices arXiv de la Revue ([1], [2], [18], [19], [23], [48], [88], [109], [110]) | Mémoire de l'évaluateur, sans consultation en ligne | Identifiants, titres et premiers auteurs concordants |
| 272 exigences du Cadre (Note AMF, README) | Décompte des identifiants EXIG uniques | 272, exact |
| Revue : 12 + 32 + 145 = 189; dépôts 5 + 13 + 52 + 119 = 189; versions 103 + 52 + 24 + 10 = 189; fronts = 139; 50 + 139 + 3 = 192; 67 / 123 = 54 % | Recompte | Exact |
| Note AMF : 5 + 27 + 9 = 41 attentes; familles 12 + 6 + 5 + 9 + 9 = 41 | Recompte | Exact |
| Cadre, annexe F : 125 + 214 + 55 + 14 + 19 = 427 liens; 427 − 125 = 302; 88 + 33 = 121 références | Recompte | Exact |

## 6. Recommandations

### Requises avant toute diffusion académique ou adoption organisationnelle

1. Faire relire le Cadre et la Note AMF par au moins un expert humain du domaine et par la conformité. Les deux documents le posent eux-mêmes comme préalable.
2. Divulguer de façon uniforme, dans chaque document, le rôle de l'IA : rédaction, recherche, vérification, et part de la validation humaine.
3. Purger le Compendium de ses artefacts de production (TOC, PRD, D-n, balayages), ou les reléguer dans une annexe de méthode. Pour les volumes I à III, deux voies : les verser au dépôt, ou retirer les énoncés qui ne reposent que sur eux.
4. Aligner le résumé de la Veille sur sa méthode réelle, avec ses deux régimes.
5. Ajouter une licence et un fichier `CITATION.cff`, et réconcilier la classification « Usage interne » avec la publication.

### Souhaitables

6. Valider le Cadre sur le terrain : pilote sur un ou deux agents, étude de cas ou consultation Delphi d'experts, avec mesure du taux de conformité aux exigences.
7. Étendre à tout le corpus de la Revue la passe DBLP, Crossref et OpenReview, pour resserrer le plafond de 145.
8. Caractériser les agents de vérification (modèle, consigne, taux d'accord avec un vérificateur humain sur un échantillon).
9. Séparer les errata du corps du texte et ouvrir chaque chapitre long par un résumé de quelques lignes.
10. Scinder la catégorie A du Cadre en deux : source primaire du fait, source primaire de l'allégation.
11. Pour NiveauMaturité, choisir entre deux voies : le renommer en modèle de couches, ou ajouter des critères d'atteinte par palier.
12. Verser les sources amont (Typst, HTML) et ajouter un test de la chaîne de composition.

## 7. Conclusion

Ce corpus démontre une maîtrise rare de la preuve dans un champ qui en manque : il dit à chaque pas ce qu'il sait, depuis quand, et jusqu'où. Sa valeur scientifique est aujourd'hui bornée moins par des erreurs, puisqu'aucune n'a été trouvée, que par ce qui lui manque : une validation humaine et empirique, des sources complètes et une forme lisible pour ses destinataires. Les corrections requises sont surtout éditoriales et procédurales. Faites, et assorties d'une validation empirique du Cadre, elles placeraient le corpus nettement au-dessus de 85.

## Suivi des recommandations

L'évaluation porte sur l'état du commit `70fd758`; ses constats ne sont pas réécrits.

- **Recommandation 3, premier volet (31 oct. 2026).** Les traces de production du Compendium sont retirées de son texte (README, « Composition des PDF »). Les renvois aux volumes I à III restent.
- **Recommandation 5, en partie (31 oct. 2026).** Une licence a été ajoutée : CC BY 4.0 pour les documents, MIT pour le code. Restent le fichier `CITATION.cff` et la classification « Usage interne ».

## Sources consultées pour les vérifications

- [Blakes — L'AMF publie sa ligne directrice sur l'utilisation de l'intelligence artificielle](https://www.blakes.com/fr-ca/perspectives/l-amf-publie-sa-ligne-directrice-sur-l-utilisation-de-l-intelligence-artificielle-ce-que-les-insti/)
- [Model Context Protocol — spécification 2026-07-28, `server/discover`](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)
- [BSIF — Ligne directrice E-23, gestion du risque de modèle (2027)](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027)
- [IETF Datatracker — draft-ietf-wimse-aims](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-aims)
- [donneespersonnelles.fr — Omnibus numérique IA](https://donneespersonnelles.fr/omnibus-numerique-ia)
- [Journal du Net — EU AI Act, le calendrier reporté](https://www.journaldunet.com/intelligence-artificielle/1550335-eu-ai-act-le-calendrier-report)
