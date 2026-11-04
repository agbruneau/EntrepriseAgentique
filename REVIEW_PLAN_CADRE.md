# Plan de revue — Cadre de référence CRE-IA-2026-01

**Document audité** : `documents/Cadre de Référence.pdf` — *Interopérabilité et Orchestration en Entreprise Agentique*, cadre de référence d'architecture d'entreprise CRE-IA-2026-01, version 1.1 (28 octobre 2026), actualisation du 1er novembre 2026 (annexe H). Auteur : André-Guy Bruneau, M.Sc. IT. Composé en Typst 0.15.1. **283 pages.**
**Date de la revue** : 3 novembre 2026. La pagination imprimée (« Page X sur 283 ») coïncide avec la pagination PDF.
**Nature du document** : cadre *normatif* d'entreprise (principes, exigences DOIT/DEVRAIT/PEUT, tableaux, contrats d'exemple), pas un article de recherche. Il ne contient ni théorème ni banc d'essai propre : les « axiomes » sont les principes PRIN-01 à PRIN-12, les « invariants » sont les règles de combinaison des échelles et les exigences EXIG-*. L'axe « falsification formelle » s'applique donc à la cohérence logique de ces règles, aux propriétés techniques revendiquées (idempotence, saga, délégation OAuth, chaînage d'audit, machines à états A2A, concurrence), à l'exactitude des faits sur les spécifications et les lois, et aux chiffres cités.

---

## 1. Structure

| Partie | Chapitres | Pages |
|---|---|---|
| Liminaires | Historique des versions, Méthode et avertissements, Sommaire exécutif (10 décisions structurantes) | 1-9 |
| I — Fondements | 1 Objet, portée, mode d'emploi; 2 Contexte et enjeux; 3 Concepts et définitions; 4 Principes directeurs | 10-30 |
| II — Architecture, interopérabilité, orchestration | 5 Architecture de référence; 6 Interopérabilité (MCP, A2A, événements, contrats, veille); 7 Orchestration; 8 Autonomie et supervision humaine | 31-116 |
| III — Confiance et exploitation | 9 Identité, sécurité, confiance zéro; 10 Observabilité, évaluation, FinOps | 117-158 |
| IV — Gouvernance, conformité, mise en œuvre | 11 Gouvernance et cycle de vie; 12 Risques, conformité, réglementation; 13 Approvisionnement; 14 Maturité; 15 Feuille de route | 159-207 |
| Annexes | A Grille d'homologation; B Fiche d'agent; C Exemples de contrats (C.1-C.8); D Registre des exigences; E Glossaire; F Validation des sources; G Références [1]-[473]; H Actualisation de novembre 2026 (réf. [474]+) | 208-283 |

### Sections principales (page de début)
- **Ch. 1** (11) : 1.1 Objet · 1.2 Portée · 1.3 Public · 1.4 Force normative (13) · 1.5 Identifiants (13) · 1.6 Révision · 1.7 Méthode (14)
- **Ch. 2** (15) : 2.1 Adoption 2026 · 2.2 Consolidation des standards (17) · 2.3 Huit enjeux (18) · 2.4 Pourquoi maintenant (19)
- **Ch. 3** (20) : 3.1 Définitions normatives, tableau 7 (20-23) · 3.2 Flux ou agent (23) · 3.3 Interactifs / ambiants (24) · 3.4 Ce qu'un agent n'est pas (24)
- **Ch. 4** (25) : 4.1 Douze principes · 4.2 Tableau 9 (28) · 4.3 Préséance et tableau 10 (29)
- **Ch. 5** (32) : 5.1 Vue d'ensemble, règle centrale · 5.2 Six couches (34-37) · 5.3 Plans transversaux (38) · 5.4 Blocs (39) · 5.5 Mémoire (41) · 5.6 Parcours de bout en bout (44)
- **Ch. 6** (45) : 6.1 Quatre niveaux d'interopérabilité · 6.2 Carte (48) · 6.3 Catalogue des protocoles (49) · 6.4 Matrice (52) · 6.5 MCP 2026-07-28 (53-66) · 6.6 A2A 1.0 (67-75) · 6.7 Événementiel / CloudEvents (75-80) · 6.8 Contrats, SemVer, catalogue (81-83) · 6.9 Émergents, AAIF, AGNTCY, paiements (84-85)
- **Ch. 7** (86) : 7.1 Données probantes · 7.2 Huit patrons autorisés (87) · 7.3 Choix (91) · 7.4 Exécution durable (93) · 7.5 Saga (94) · 7.6 Idempotence (97) · 7.7 Contexte inter-agents (98) · 7.8 Résilience (99) · 7.9 Anti-patrons (100) · 7.10 Cadriciels (101)
- **Ch. 8** (103) : 8.1 N0-N4 (tableau 28) · 8.2 Critères (107) · 8.3 P0-P3 (tableau 31, 108) · 8.4 Combinaison (109) · 8.5 Approbation vérifiable (110) · 8.6 Agents ambiants (112) · 8.7 Approbation machinale (114) · 8.8 Décisions automatisées (115)
- **Ch. 9** (118) : 9.1 Confiance zéro · 9.2 Identité non humaine (119) · 9.3 Délégation RFC 8693, intersection des droits (122-127) · 9.4 Passerelle d'agents (127-130) · 9.5 Menaces, OWASP Top 10 agentique (131) · 9.6 Injection, triade létale, 4 niveaux (133-136) · 9.7 Bacs à sable, 4 verrous (136-140) · 9.8 Chaîne d'approvisionnement (141) · 9.9 Équipe rouge (143)
- **Ch. 10** (145) : 10.1 OpenTelemetry, conventions GenAI v1.41.0 · 10.2 Contenu des invites (149) · 10.3 Journal d'audit (150) · 10.4 Évaluation continue, trois paliers (151) · 10.5 Économie de l'inférence (154) · 10.6 Coûts (155)
- **Ch. 11** (160) : Rôles · RACI (162) · Étoile (162) · Registre (164) · Cycle de vie (166) · Dérogations (168) · Gouvernance des standards (169)
- **Ch. 12** (170) : 12.1 Classes de risque, tableau 46 (171) · 12.2 Loi 25 (172-178) · 12.3 Fédéral, E-23 (178) · 12.4 RIA, règlement (UE) 2026/1744 (180) · 12.5 NIST AI RMF, ISO/IEC 42001 (182) · 12.6 Correspondance (184) · 12.7 Transparence (185) · 12.8 Incidents (186) · 12.9 Évaluation d'impact unifiée (188)
- **Ch. 13** (189) : verrouillage · critères · clauses (192) · grille, tableau 54 (195)
- **Ch. 14** (196) : 5 niveaux × 5 dimensions, niveau global = dimension la plus faible · cotation (198) · lien ISO/NIST (199)
- **Ch. 15** (200) : 4 phases (0-3, 3-9, 9-18, 18+ mois), jalons J1, J2, J2a, J3, J4, J5 · 90 jours (203) · indicateurs (204) · risques (206)
- **Annexes** : A (209) · B (212) · C (215-224) · D (224-230) · E (231-241) · F (241-250) · G (250-275) · H (275-283; H.4 errata, p. 281)

## 2. Taxonomie et notations

### Identifiants normatifs (§ 1.5, tableau 4)
- **PRIN-01 à PRIN-12** : principes (ch. 4). Seuls les blocs EXIG (ch. 5-13), les PRIN et les tableaux expressément visés sont normatifs.
- **EXIG-XXX-NN**, numérotation continue par préfixe, jamais réattribuée. Décompte extrait du texte (aucun trou) : ARC 25 · INT 23 · MCP 22 · A2A 15 · EVT 10 · ORC 30 · AUT 23 · IAM 21 · SEC 26 · OBS 13 · EVA 6 · FIN 10 · GOV 20 · CON 26 · APP 17 = **287 exigences**. L'annexe H mentionne aussi `EXIG-AMF-05` et `EXIG-AMF-07` (reports proposés par la Note AMF IA), préfixe absent du tableau 4.
- Forces : DOIT, NE DOIT PAS, DEVRAIT, PEUT. Distinction « exigence externe » (« la spécification exige ») / « choix du cadre ».
- Sources : catégories A (primaire), B (secondaire reconnue), C (jamais citée). Références [n] → annexe G.
- À vérifier : § 1.5 annonce « sept annexes, de A à G », alors que le document contient une annexe H.

### Échelles et axes (à ne jamais confondre, § 3.1)
1. **Classe de risque de l'agent** (tableau 46, § 12.1) : faible, modérée, élevée; la plus élevée dont un critère est rempli, jamais une moyenne.
2. **Niveau d'autonomie** N0 (déterministe, sans modèle), N1 (consultatif, P0-P1), N2 (exécution approuvée, HITL), N3 (autonomie bornée sous seuils et ODD, HOTL), N4 (autodéclenchement, ODD certifié, décision du comité), **NX interdit**.
3. **Palier d'outil** P0 (lecture publique), P1 (lecture interne ou sensible), P2 (écriture réversible ou compensable), P3 (critique, externe ou irréversible : jamais exécuté seul). Écriture sans compensation déclarée ⇒ P3; outil à effets multiples ⇒ palier le plus élevé; palier tiré du catalogue, jamais des annotations (EXIG-AUT-08).
4. **Topologie** (ch. 7) : flux déterministe, agent unique, multiagent (8 patrons autorisés, délégation sur 2 niveaux au plus, multiagent seulement sur gain mesuré).
- **Plafonds (EXIG-CON-02, source unique depuis la v1.1)** : élevée → N2; modérée → N3; faible → N3, N4 sur décision du comité. Règle la plus stricte entre classe, niveau et palier (§ 8.4, matrice classe × palier).
- **Règle d'or EXIG-AUT-07** : rayon élevé + réversibilité faible + détection lente ⇒ jamais au-delà de N2.
- **Maturité** (ch. 14) : 1 Initial, 2 Reproductible, 3 Défini, 4 Géré, 5 Optimisé; 5 dimensions; niveau global = minimum. Cible : niveau 3 en 18 mois.
- **Feuille de route** : Fondations (0-3, N0-N1) → J1 → Plateforme (3-9, N2 et premiers N3 intradomaine) → J2 → Industrialisation (9-18, N3 interdomaine par la passerelle) → J3 → Mise à l'échelle (18+, N4). J2a (RIA annexe III) au plus tard le 1er novembre 2027; J4 maturité 4; J5 ISO/IEC 42001.

### Versions et dates épinglées (dérives inter-chapitres possibles)
MCP révision **2026-07-28** (migration au plus tard le 28 juillet 2027, EXIG-MCP-22) · A2A **1.0** (carte à `/.well-known/agent-card.json`; v1.0.1 du 28 mai 2026; machine à 8 états + `UNSPECIFIED`) · OpenTelemetry, conventions GenAI **v1.41.0** (Development) · CloudEvents, AsyncAPI · OAuth : RFC 8693 (échange de jetons), RFC 8785 (JCS) pour l'audit chaîné SHA-256 · AAIF (Linux Foundation) : MCP depuis décembre 2025, A2A depuis août 2026 · Loi 25 (L.Q. 2021, c. 25) : 22 sept. 2023 / 22 sept. 2024; art. 12.1 Loi sur le privé; art. 65.2 Loi sur l'accès · RIA (UE) 2024/1689 : application générale le 2 août 2026; annexe III au 2 décembre 2027 et annexe I au 2 août 2028 (règlement (UE) 2026/1744) · BSIF **E-23** en vigueur le 1er mai 2027 · NIST AI RMF 1.0, NIST AI 100-2 E2025, ISO/IEC 42001:2023, ISO/IEC 22989:2022 · OWASP Top 10 agentique (ASI01-ASI10), OWASP NHI Top 10 2025, menace T10.
État des sources : 27-28 octobre 2026 (corps); 1er novembre 2026 (annexe H, informative, qui consigne elle-même des errata au tableau 72).

## 3. « Axiomes » et thèses centrales

**Douze principes** (ordre de préséance, § 4.3 : 1. droit et contrats; 2. PRIN-03 à 07, 10, 12; 3. PRIN-01, 02, 08, 09, 11) :
PRIN-01 standards ouverts avant intégrations propriétaires · PRIN-02 contrat avant code · PRIN-03 identité propre, moindre privilège, moindre agence (droits effectifs = intersection mandant ∩ agent) · PRIN-04 autonomie proportionnée au risque · PRIN-05 réversibilité par conception (P3 jamais seul) · PRIN-06 traçabilité et imputabilité économique · PRIN-07 défiance envers le contenu reçu · PRIN-08 déterminisme autour du modèle, simplicité d'abord · PRIN-09 découplage des fournisseurs · PRIN-10 humain imputable · PRIN-11 découplage raisonnement, action, mémoire · PRIN-12 dégradation maîtrisée, échec en mode fermé.

**Thèses à mettre à l'épreuve**
- T1 : le risque de verrouillage s'est déplacé des protocoles vers les plateformes (§ 2.4, 13.1).
- T2 : la passerelle d'agents, point unique d'application des politiques, suffit (rien ne la contourne; un outil hors catalogue est injoignable) — question de point de défaillance unique, de latence, de neutralité au transport, du mode stdio local.
- T3 : idempotence + exécution durable + saga = « ne jamais refaire une action terminée » (§ 7.4-7.6) — isolation entre sagas concurrentes, compensations non commutatives, fenêtres de rejeu.
- T4 : le retrait déterministe des capacités d'envoi après lecture de contenu non fiable neutralise la triade létale (§ 9.6) — canaux latéraux, persistance en mémoire, propagation inter-agents.
- T5 : l'approbation humaine signée et liée à l'action exacte (empreinte d'arguments canonisés) est vérifiable et ne dégénère pas en approbation machinale (§ 8.5, 8.7, C.6).
- T6 : la délégation par échange de jetons à audience unique, sans élargissement de portée d'un saut à l'autre, reste sûre en chaîne multi-agents (§ 9.3).
- T7 : la classification par la plus haute classe + plafonds + règle la plus stricte forme un treillis cohérent, sans cas indécidable ni contradiction avec les jalons de la feuille de route.
- T8 : la méthode de validation des sources (121 réf., 427 liens; audit final : 428 réf., 1 409 affirmations; annexe G : 473 réf.) est fiable et reproductible.

## 4. Découpage pour l'audit (12 pages, recouvrement de 2)

| Chunk | Pages | Contenu |
|---|---|---|
| 01 | 1-12 | Liminaires, sommaire exécutif, § 1.1-1.3 |
| 02 | 11-22 | Ch. 1, ch. 2, § 3.1 |
| 03 | 21-32 | § 3.1-3.4, ch. 4, début ch. 5 |
| 04 | 31-42 | § 5.1-5.5 |
| 05 | 41-52 | § 5.5-5.6, § 6.1-6.3 |
| 06 | 51-62 | § 6.4, § 6.5 MCP (première partie) |
| 07 | 61-72 | Fin § 6.5, § 6.6 A2A |
| 08 | 71-82 | Fin § 6.6, § 6.7 événementiel, § 6.8 |
| 09 | 81-92 | § 6.8-6.9, § 7.1-7.3 |
| 10 | 91-102 | § 7.3-7.10 (état, saga, idempotence, résilience) |
| 11 | 101-112 | § 7.10, § 8.1-8.5 |
| 12 | 111-122 | § 8.5-8.8, § 9.1-9.2 |
| 13 | 121-132 | § 9.3-9.5 (délégation, passerelle) |
| 14 | 131-142 | § 9.5-9.8 (injection, bacs à sable) |
| 15 | 141-152 | § 9.8-9.9, § 10.1-10.4 |
| 16 | 151-162 | § 10.4-10.6, § 11.1-11.2 |
| 17 | 161-172 | § 11.2-11.7, § 12.1 |
| 18 | 171-182 | § 12.1-12.5 (Loi 25, E-23, RIA) |
| 19 | 181-192 | § 12.5-12.9, § 13.1-13.2 |
| 20 | 191-202 | § 13.2-13.4, ch. 14, § 15.1 |
| 21 | 201-212 | § 15.1-15.4, annexe A |
| 22 | 211-222 | Fin A, annexe B, § C.1-C.5 |
| 23 | 221-232 | § C.6-C.8, annexe D, début E |
| 24 | 231-242 | Annexe E, § F.1-F.2 |
| 25 | 241-252 | Annexe F, début G |
| 26 | 251-262 | Annexe G (références) |
| 27 | 261-272 | Annexe G (références) |
| 28 | 271-282 | Fin G, annexe H |
| 29 | 281-283 | Fin H (errata, références de l'actualisation) |

Chaque rapport `audit_XX.md` cite page et passage exacts, et ne signale dans les pages de recouvrement que ce qui n'apparaît pas déjà dans le chunk voisin, sauf constat inter-pages.
