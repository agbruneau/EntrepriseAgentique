# Consigne d'audit d'un chunk — revue contradictoire du Cadre de référence CRE-IA-2026-01

ultrathink. Tu es un réviseur indépendant, exigeant et sans complaisance. Rédige en français canadien (termes techniques et identifiants en anglais).

## Entrées
1. Lis d'abord `C:\Github\EntrepriseAgentique\REVIEW_PLAN_CADRE.md` (structure, notations, échelles, versions épinglées, thèses T1-T8).
2. Lis intégralement ton chunk assigné (texte extrait du PDF, pages marquées `[Page PDF n]`; pagination imprimée = pagination PDF). Les tableaux et figures sont aplatis par l'extraction : reconstitue-les avec prudence et ne signale pas un défaut de mise en page qui ne serait qu'un artefact d'extraction.
3. Pour confirmer ou réfuter une contradiction avec un autre chapitre, tu PEUX chercher (Grep) dans `C:\Github\EntrepriseAgentique\.review_chunks_cadre\full.txt` (texte complet, 283 pages). Ne lis pas d'autres fichiers du dépôt. Pas de recherche Web : un fait externe que tu ne peux vérifier se signale « à vérifier par l'audit bibliographique », avec ce qui trancherait.

## Nature du document
Cadre normatif d'entreprise (principes PRIN, exigences EXIG DOIT/DEVRAIT/PEUT), pas un article scientifique. Transpose les trois axes :

**A. Falsification formelle et algorithmique** — cohérence logique des règles et des échelles (classe × niveau N × palier P, plafonds, préséance, règle la plus stricte) : cherche les cas indécidables, les combinaisons non couvertes, les règles qui se contredisent. Vérifie les propriétés techniques revendiquées : idempotence, exécution durable, saga et compensations (concurrence, isolation, ordre, échec de compensation), machines à états (A2A), délégation OAuth et échange de jetons (élargissement de portée, audience, confused deputy), chaînage d'audit et canonisation, signatures d'approbation (TOCTOU, rejeu), propagation de contexte, bornes et seuils chiffrés (cohérence arithmétique, unités). Signale tout postulat implicite, saut logique, cas limite non traité. Exactitude des affirmations sur les spécifications (MCP, A2A, OpenTelemetry, CloudEvents, RFC) et les lois (Loi 25, RIA, E-23) : signale ce qui te semble faux ou douteux d'après tes connaissances, en distinguant ce dont tu es sûr de ce que tu supposes.

**B. Robustesse systémique et empirique** — validité des données probantes invoquées (chiffres d'analystes, études, bancs d'essai cités : population, date, généralisation abusive), modes de défaillance sous contention et à l'échelle (passerelle comme point unique de défaillance, latence, saturation des approbateurs, tempêtes d'événements, pannes de fournisseur), testabilité réelle des exigences (« vérifiable en revue ou en test » : l'est-elle?), faisabilité opérationnelle et coût des contrôles, compromis architecturaux non justifiés.

**C. Densité et cohérence locale** — contradictions internes, redondances, définitions circulaires ou sous-spécifiées, termes employés avant définition, dérives de notation (identifiants, versions, dates, chiffres) entre ce chunk et le reste du document, renvois erronés (section, tableau, exigence inexistants ou mal ciblés).

L'annexe H (tableau 72, p. 281) consigne déjà des errata : si tu retrouves l'un d'eux, marque-le « déjà consigné en H.4 » plutôt que comme nouveau.

## Sortie
Écris (Write) ton rapport dans `C:\Github\EntrepriseAgentique\.review_chunks_cadre\audit_XX.md` (XX = numéro de ton chunk). Ne modifie aucun autre fichier.

Structure :
```
# Audit chunk_XX — pages A-B
## Synthèse (5 lignes max : ce que couvre le chunk, qualité globale, les 3 défauts les plus graves)
## Constats
### [XX-01] [BLOQUANT|MAJEUR|MINEUR] Titre court
- **Axe** : A | B | C
- **Localisation** : chapitre/section, page, citation exacte (≤ 30 mots, entre guillemets)
- **Diagnostic** (premiers principes) :
- **Contre-exemple ou scénario de défaillance** explicite :
- **Correctif proposé** :
- **Confiance** : vérifié dans le texte | déduit | à vérifier (source externe)
## Points forts (3 lignes max)
## Questions pour l'audit bibliographique (faits externes à vérifier, avec page)
```
Barème : BLOQUANT = erreur formelle ou architecturale qui rend une exigence fausse, contradictoire, inapplicable ou dangereuse; MAJEUR = lacune méthodologique, omission importante, fait externe probablement faux; MINEUR = dérive de notation, clarté, renvoi, redondance. Rapporte chaque constat, y compris les mineurs : ne filtre pas. N'invente rien : chaque constat cite le texte. Dans les pages de recouvrement (2 premières et 2 dernières), ne rapporte que ce qui exige les deux côtés de la couture.

Termine ta réponse finale par une seule ligne : `audit_XX.md : N constats (b BLOQUANT, m MAJEUR, n MINEUR)`.
