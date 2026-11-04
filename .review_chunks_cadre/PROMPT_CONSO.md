# Consigne — consolidation d'une tranche de la revue du Cadre CRE-IA-2026-01 (Phase 4a)

ultrathink. Tu es méta-réviseur : tu ne relis pas tout le document, tu croises les rapports bruts d'une tranche pour en tirer une matrice dédoublonnée, contre-vérifiée et classée. Rédige en français canadien (termes techniques et identifiants en anglais).

## Entrées
- `C:\Github\EntrepriseAgentique\REVIEW_PLAN_CADRE.md`.
- Les rapports bruts de ta tranche, `C:\Github\EntrepriseAgentique\.review_chunks_cadre\audit_XX.md` (liste dans ta tâche), et `audit_lit.md` s'il existe (vérification bibliographique, qui prime sur les suppositions des rapports bruts).
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\full.txt` (texte intégral, 283 pages) : pour contre-vérifier un constat par Grep. Ne le lis pas en entier.

## Travail
1. **Dédoublonner** : les chunks se recouvrent de 2 pages et plusieurs réviseurs ont vu les mêmes défauts transversaux (passerelle et appels intradomaine, compensation bloquée par coupe-circuit ou mode fermé, usage unique du jeton d'approbation contre réessai idempotent, contenu interdit en télémétrie contre évaluation et preuve, troncature du chaînage d'audit, etc.). Fusionne-les en un seul défaut, qui liste tous les identifiants de constats d'origine.
2. **Contre-vérifier** chaque BLOQUANT et chaque MAJEUR dans `full.txt` : la citation existe-t-elle, la contradiction est-elle réelle, le texte ne la règle-t-il pas ailleurs? Rétrograde ou écarte (avec la raison) ce qui ne tient pas. Ne garde BLOQUANT que ce qui rend une exigence fausse, contradictoire, inapplicable ou dangereuse.
3. **Dérives inter-chapitres** : signale les dérives de notation, de chiffres, de dates et de versions entre ta tranche et le reste du document.
4. **Correctif** : pour chaque défaut, un correctif rédactionnel précis (quoi changer, où, dans quels termes), cohérent avec les autres correctifs de la tranche. Quand un défaut transversal exige un arbitrage de conception (par exemple : la passerelle couvre-t-elle l'intradomaine? une compensation passe-t-elle le coupe-circuit?), propose l'arbitrage dans la section dédiée.

## Sortie
Écris (Write) `C:\Github\EntrepriseAgentique\.review_chunks_cadre\conso_N.md` (N donné dans ta tâche); ne modifie aucun autre fichier.

```
# Consolidation tranche N — <sections>, pages A-B
## Synthèse (10 lignes au plus)
## Matrice des défauts
### [N.01] [BLOQUANT - Erreur formelle/architecturale] Titre
- Constats d'origine : 04-03, 06-01, …
- Localisation exacte : chapitre/section, page, citation (≤ 30 mots)
- Diagnostic par premiers principes :
- Contre-exemple explicite :
- Correctif proposé :
(puis tous les MAJEUR - Lacune méthodologique/omission, puis tous les MINEUR - Dérive de notation/clarté; les mineurs peuvent être groupés par thème si chacun garde sa localisation et son correctif)
## Arbitrages transversaux proposés (défauts qui touchent d'autres tranches : la décision à prendre, l'option recommandée, les sections touchées)
## Constats écartés à la contre-vérification (identifiant, raison)
```
Rapporte tout ce qui survit à la contre-vérification, mineurs compris : ne filtre pas par gravité.

Termine par : `conso_N.md : D défauts (b BLOQUANT, m MAJEUR, n MINEUR), E constats écartés`.
