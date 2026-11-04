# Consigne d'implémentation — correctifs de la revue du Cadre CRE-IA-2026-01

ultrathink. Tu implémentes, dans une tranche du document, les correctifs issus de la revue contradictoire. Rédige en français canadien, dans le registre exact du Cadre (phrases courtes, « Le cadre fixe », « choix du cadre », DOIT/DEVRAIT/PEUT en gras, termes techniques et identifiants en anglais). Régime production : chaque correctif doit être juste, vérifiable et ne rien casser.

## Entrées
1. `C:\Github\EntrepriseAgentique\REVIEW_PLAN_CADRE.md` (notations, échelles).
2. Le rapport consolidé `C:\Github\EntrepriseAgentique\DEEP_REVIEW_CADRE_REFERENCE.md` : lis la matrice des défauts pour ta tranche et les constats transversaux qui la touchent. Les arbitrages transversaux qui y sont tranchés (section « Arbitrages transversaux ») s'imposent à toi : applique-les tels quels dans ta tranche.
3. Les rapports bruts de ta tranche (listés dans ta tâche) dans `C:\Github\EntrepriseAgentique\.review_chunks_cadre\audit_XX.md`, et `audit_lit.md` pour les faits externes.
4. Le corps HTML à corriger : `C:\Github\EntrepriseAgentique\.review_chunks_cadre\corps.html` (lecture seule; c'est le texte exact sur lequel s'appliquent les remplacements). Cherche-y avec Grep; lis-en seulement les zones utiles.

## Ce que tu produis
Un seul fichier : `C:\Github\EntrepriseAgentique\sources\cadre\correctifs\NN_tranche.py` (nom donné dans ta tâche). Ne modifie aucun autre fichier.

```python
"""Correctifs de la revue du 3 novembre 2026 — tranche : <sections>."""
NBSP = '\xa0'
CORRECTIONS = [
    # [constats] explication courte
    ('passage exact du corps.html', 'passage corrigé', ['04-03', '06-01']),
]
JOURNAL = [
    # (localisation, correctif en une phrase, constats)
    ('§ 5.2, EXIG-ARC-01', 'Portée précisée : …', ['04-01', '06-01']),
]
```

## Règles des remplacements
- Le passage d'origine est copié **à l'octet près** depuis `corps.html` (balises, `\xa0` insécables, apostrophes typographiques ’, guillemets « », tirets —). Il doit y figurer **une seule fois** : allonge-le jusqu'à ce qu'il soit unique. Les passages de ta tranche ne chevauchent pas ceux d'une autre tranche : reste dans tes sections.
- Ne touche jamais : le texte des figures (images vectorielles, intouchables; tu peux corriger leur `<figcaption>` ou le texte qui les commente), les identifiants existants (EXIG-XXX-NN, PRIN-NN, numéros de tableaux, de figures et de références [n]), l'ordre des tableaux. Garde la structure HTML des blocs (`<div id="exig-…">`, `<div id="pourquoi-…">`, `<table>`, `<caption>`).
- Une exigence corrigée garde son identifiant. Une exigence nouvelle n'est créée qu'en dernier recours, au numéro suivant le dernier de son préfixe (vérifie dans corps.html qu'il est libre et que nulle autre tranche ne le prend : seule la tranche qui possède le chapitre du préfixe en crée), avec la même structure HTML que ses voisines; signale-la dans JOURNAL avec la mention « nouvelle exigence » pour que l'annexe D soit mise à jour.
- Pour un fait externe : n'écris que ce qu'établit `audit_lit.md` ou ce dont tu es certain; sinon, retire l'affirmation ou présente-la comme choix du cadre. Les appels de citation existants restent valides; n'en invente pas.
- Un BLOQUANT ou MAJEUR se corrige dans la règle elle-même (énoncé de l'exigence, tableau, définition), pas seulement par une note. Un MINEUR se corrige au plus court.
- Si un constat est faux à la relecture du texte, ou si son correctif contredirait un arbitrage transversal ou une source primaire, ne le corrige pas : consigne-le dans JOURNAL avec la nature « non retenu : <raison> ».
- Tout constat de ta tranche doit apparaître dans JOURNAL (corrigé, ou non retenu avec raison).

## Contrôle obligatoire avant de rendre
Exécute depuis `C:\Github\EntrepriseAgentique\sources\cadre` :
`python corrections.py C:\Github\EntrepriseAgentique\.review_chunks_cadre\corps.html`
La commande applique tous les modules présents. Corrige ton module jusqu'à ce qu'aucune erreur ne mentionne ton fichier (les erreurs d'autres modules ne te regardent pas). Vérifie aussi `python -c "import ast,sys;ast.parse(open(sys.argv[1],encoding='utf8').read())" <ton fichier>`.

Termine ta réponse par une ligne : `NN_tranche.py : X correctifs, Y constats non retenus, Z nouvelles exigences`.

## Propriété des sections (stricte; un passage hors de ta tranche n'est pas à toi)
Repères dans corps.html (titres HTML) :
- **t1** : du début de corps.html jusqu'au titre `<h3>6.4` exclu (Méthode et avertissements, sommaire exécutif, ch. 1 à 5, § 6.1-6.3). Exception : la table « Historique des versions » et le numéro de version appartiennent à l'orchestrateur (n'y touche pas).
- **t2** : de `<h3>6.4` jusqu'à `<h3>7.3` exclu.
- **t3** : de `<h3>7.3` jusqu'au titre de la Partie III exclu (fin du ch. 8).
- **t4** : Partie III (ch. 9 et 10) jusqu'au titre de la Partie IV exclu.
- **t5** : Partie IV (ch. 11 à 15) et l'annexe A, jusqu'à `<h2>B ` exclu.
- **t6** : annexes B à G (de `<h2>B ` à la fin de corps.html), et l'annexe H, dont la source est `C:\Github\EntrepriseAgentique\sources\cadre\actualisation-2026-11.html` (t6 seul peut la modifier, directement avec Edit, sections H.1 à H.5 seulement).
Un arbitrage qui touche plusieurs tranches : chacune applique la part située dans ses sections. Les nouveaux identifiants sont ceux du tableau « Nouveaux identifiants » (2.0.1) : crée seulement ceux dont le préfixe relève de tes sections (ARC-26 : t1; EVT-11 : t2; ORC-31, AUT-24 : t3; IAM-22, OBS-14, EVA-07 : t4; GOV-21, APP-18 : t5). t6 ajoute ces 9 lignes à l'annexe D, à leur place dans l'ordre du document, et met à jour tout décompte de l'annexe D.

## Bornes de faisabilité (priment sur la synthèse)
- Les numéros de références [n] ne changent jamais : un doublon de l'annexe G est annoté dans son entrée (« Même source que [m]. »), sans renumérotation; les décomptes (473 références) sont corrigés en texte (« 473 entrées, dont k doublons signalés »).
- Le texte des figures (schémas vectoriels) est intouchable : corrige la légende ou le texte voisin, et signale l'écart résiduel dans JOURNAL (« figure non modifiable : … »).
- Ne change pas le titre court d'une exigence existante : l'annexe D le reprend mot pour mot. Si c'est indispensable, note-le dans JOURNAL avec la mention « titre modifié : <nouveau titre> ».
- Une exigence devenue renvoi garde son bloc, son identifiant et son titre; son énoncé devient « Voir l'EXIG-… » avec la règle résiduelle s'il y en a une.
- Un tableau se corrige cellule par cellule : ne réécris pas un tableau entier.
- Pour l'annexe H : corrige ce qui est faux dans H.1-H.5, sans réécrire l'annexe. L'orchestrateur ajoutera une section H.6 et la ligne d'historique de la version 1.2.
