# Consigne commune — derniers correctifs du Cadre CRE-IA-2026-01, version 1.2

ultrathink. Le Cadre a été corrigé en version 1.2 par des modules de remplacement (`C:\Github\EntrepriseAgentique\sources\cadre\correctifs\*.py`, appliqués dans l'ordre alphabétique par `corrections.py`). Il reste des correctifs de l'audit non implémentés; tu en traites un lot (dans ta tâche). Rédige en français canadien, dans le registre du Cadre. Régime production.

## Entrées
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\corps_corrige.html` : le corps APRÈS tous les modules existants (lecture seule). Tes passages d'origine se copient d'ici, à l'octet près (insécables `\xa0`, apostrophes ’, « »).
- `C:\Github\EntrepriseAgentique\DEEP_REVIEW_CADRE_REFERENCE.md` (matrices et arbitrages A-01 à A-34, qui font foi), `C:\Github\EntrepriseAgentique\.review_chunks_cadre\conso_N.md`, `audit_XX.md`, `audit_lit.md`.
- Les JOURNAL des modules existants disent ce qui a été fait et pourquoi un constat n'a pas été retenu.

## Module à produire
Un fichier `C:\Github\EntrepriseAgentique\sources\cadre\correctifs\<nom donné>.py`, au format des autres : `CORRECTIONS = [(ancien, nouveau, constats)]`, `JOURNAL = [(localisation, correctif, constats)]`. Chaque `ancien` figure une seule fois dans corps_corrige.html. Ne touche jamais : identifiants EXIG/PRIN, numéros de tableaux, figures et références [n], lignes du registre de l'annexe D (régénérées par script), titres courts des exigences. Un tableau se modifie par remplacements exacts (une colonne ajoutée = chaque rangée remplacée, en-tête compris). Ne modifie aucun autre fichier, sauf mention contraire dans ta tâche.

## Contrôle obligatoire
Depuis `C:\Github\EntrepriseAgentique\sources\cadre` : `python corrections.py C:\Github\EntrepriseAgentique\.review_chunks_cadre\corps.html` doit finir sans erreur visant ton module (d'autres agents écrivent des modules en parallèle sur d'autres zones : ignore leurs erreurs). Tout constat de ton lot figure dans ton JOURNAL : corrigé, ou « non retenu : <raison démontrée> » seulement s'il est faux (preuve à l'appui) — l'impossibilité ou la lourdeur ne sont pas des raisons.

Termine par : `<module> : N correctifs, M non retenus (raisons)`.
