# Consigne — audit bibliographique et état de l'art du Cadre CRE-IA-2026-01

ultrathink. Tu es le vérificateur bibliographique indépendant de la revue contradictoire du Cadre de référence CRE-IA-2026-01 (cadre normatif d'architecture d'entreprise pour l'IA agentique, v1.1 du 28 octobre 2026, actualisé le 1er novembre 2026; date de la revue : 3 novembre 2026). Rédige en français canadien.

## Entrées
- `C:\Github\EntrepriseAgentique\REVIEW_PLAN_CADRE.md` : structure, versions et dates épinglées, thèses T1-T8.
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\questions_lit.md` : les faits externes que les réviseurs des chunks n'ont pas pu vérifier, avec page et numéro de constat.
- `C:\Github\EntrepriseAgentique\.review_chunks_cadre\full.txt` : texte intégral (283 pages); annexe G (références [1]-[473], p. 250-275) et références de l'annexe H ([474]+). Cherche-y par Grep; ne le lis pas en entier.

## Méthode
Utilise WebSearch (charge-le avec ToolSearch `select:WebSearch,WebFetch` s'il est différé) et WebFetch sur des sources primaires : spécifications (modelcontextprotocol.io et son dépôt GitHub, a2a-protocol.org et a2aproject/A2A, opentelemetry.io et semantic-conventions, cloudevents.io), registre de l'IETF (datatracker), textes juridiques (EUR-Lex, LégisQuébec, BSIF/OSFI), NIST, ISO, OWASP, articles scientifiques (arXiv, actes de NeurIPS, ICML, ICLR, AISTATS, STOC, SOSP, OSDI, USENIX Security, CCS, IEEE S&P, NDSS). Une page inaccessible est déclarée « non vérifié », jamais « confirmé ». Une source C (blogue, agrégateur) ne tranche rien.

Priorités, dans l'ordre, tant que le budget le permet (environ 60 à 90 recherches) :
1. Les faits dont dépend une exigence, une échéance ou un plafond (versions MCP 2026-07-28 et A2A 1.0/1.0.1, dates du RIA et du règlement (UE) 2026/1744, E-23 au 1er mai 2027, Loi 25 art. 12.1, 17, 3.3 et Loi sur l'accès art. 65.2, RFC 8693/8707/8785/9068/9396, OAuth 2.1, OpenTelemetry GenAI v1.41.0, CloudEvents, AAIF).
2. Les chiffres cités comme données probantes (CaMeL 77 % contre 84 % sur AgentDojo; Agent Security Bench 84,30 %; prévisions Gartner du 26 mai 2026; MAST; Anthropic multiagent 15×; Firecracker; etc.).
3. Les autres questions de `questions_lit.md`.

## État de l'art à confronter (au-delà des questions)
Cherche les travaux fondateurs ou récents (jusqu'en 2026) que le cadre omet et qui précèdent, nuancent ou invalident ses choix, notamment :
- défense par conception contre l'injection : CaMeL, FIDES / contrôle de flux d'information pour agents, Dual LLM, « Design Patterns for Securing LLM Agents against Prompt Injections » (2025), Progent, et les attaques adaptatives qui contournent les défenses (« The Attacker Moves Second », 2025);
- sagas et transactions longues : Garcia-Molina et Salem (SIGMOD 1987), sémantique de compensation, exécution durable (Temporal), idempotence et exactement-une-fois de bout en bout (Saltzer-Reed-Clark, end-to-end argument);
- délégation et capacités : Macaroons (NDSS 2014), Biscuit, adjoint confus (Hardy 1988), capacités à atténuation, travaux 2025-2026 sur l'autorisation des agents (OAuth pour agents, brouillons IETF sur l'identité d'agent);
- évaluation et fiabilité des systèmes multiagents : MAST (« Why Do Multi-Agent LLM Systems Fail? »), travaux montrant qu'un agent unique bien outillé égale ou bat le multiagent;
- supervision humaine : biais d'automatisation, approbation machinale (Parasuraman et Manzey 2010), niveaux d'automatisation (Parasuraman, Sheridan, Wickens 2000), « levels of autonomy for AI agents » (Feng, McDonald, Zhang 2025);
- journaux d'audit inviolables : Schneier-Kelsey (1999), Crosby-Wallach (USENIX Security 2009), Certificate Transparency (RFC 6962/9162) — utiles pour la troncature du chaînage.

## Sortie
Écris `C:\Github\EntrepriseAgentique\.review_chunks_cadre\audit_lit.md` (Write), et ne modifie aucun autre fichier :

```
# Audit bibliographique et état de l'art
## Synthèse (verdict sur la fiabilité des sources du cadre, en 8 lignes au plus)
## 1. Vérification des faits externes
| # | Page | Constat(s) | Affirmation du cadre | Verdict (confirmé / inexact / obsolète / non vérifié) | Ce que dit la source primaire | Source (URL, date de consultation) | Correctif proposé |
## 2. Citations inexactes, obsolètes ou déformées (références [n] de l'annexe G)
(une entrée par référence fautive : [n], défaut, preuve, correctif)
## 3. Travaux omis qui précèdent, nuancent ou invalident les choix du cadre
(une entrée par travail : référence complète vérifiée, lieu de publication, section du cadre touchée, effet : précède / nuance / invalide, correctif proposé)
## 4. Questions laissées sans réponse et ce qui les trancherait
```
Chaque verdict cite sa source. N'invente aucune référence : un travail dont tu n'as pas trouvé la notice n'apparaît pas.

Termine par la ligne : `audit_lit.md : N faits vérifiés (c confirmés, i inexacts, o obsolètes, n non vérifiés), M travaux omis`.
