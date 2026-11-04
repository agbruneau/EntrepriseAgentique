# Handoff Report — Analyste 1 Niveau 0 (Segment Livre I Protocoles, pp. 78-145)

**Agent** : Analyste 1 Niveau 0 (`worker_protocoles_0_1`)  
**Mission** : Audit contradictoire exhaustif du segment `segment_livre_1_protocoles` (pp. 78 à 145, chapitres 7 à 11 et chapitre 12 pp. 140-145).  
**Date** : 2026-11-03T22:50:00Z  

---

## 1. Observation
- **Corpus examiné** :
  - `DOCUMENT_TEXT_MAP.md` (lignes 6386 à 12186) couvrant l'intégralité des pages 78 à 145 du compendium *Interopérabilité et Orchestration en Entreprise Agentique*.
  - Images de pages inspectées via `view_file` dans `documents/scratch/document_pages/` : `page-78.png` à `page-145.png` (validation visuelle approfondie des diagrammes, tableaux et encadrés doctrinaux, notamment Figures 7.3, 7.5, 8.2, 8.4, 8.6, 9.2, 9.5, 10.1, 10.4, 11.1, 11.4 et Tableaux 7.1, 7.2, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.3, 11.2, 11.3, 11.4, 11.5, 11.6, 12.1, 12.2, 12.3).
- **Faits protocolaires et citations relevées** :
  1. *MCP Transport sans état* (Ch. 8, p. 92) : « un flux de réponse interrompu perd la requête en vol, que le client doit réémettre sous un identifiant neuf. »
  2. *MCP Roots & Confinement* (Ch. 8, p. 91) : « les racines et l'échantillonnage passent à l'état déprécié... la spécification recommandant de leur substituer, respectivement, le passage des répertoires par paramètres d'outil ou URI de ressource ».
  3. *MCP stdio* (Ch. 8, p. 92) : Transport stdio qualifié de sous-processus local avec cycle de vie partagé, sans prescription sur le cadrage de trames NDJSON et l'étanchéité `stdout`/`stderr`.
  4. *MCP Gestion d'erreurs* (Ch. 8, p. 94) : Omission de la distinction formelle entre erreur protocolaire JSON-RPC 2.0 (`error`) et erreur métier d'exécution encapsulée (`isError: true` dans `result`).
  5. *AP2 Chaîne de mandats* (Ch. 10, pp. 118, 120) : Spécification des mandats Intent/Cart/Payment sans mécanisme de réservation atomique ni contrôle de concurrence optimiste face aux sous-agents parallèles.
  6. *Taxonomie des risques & HITL* (Ch. 11, pp. 130-134) : Analyse de l'injection indirecte et du tool poisoning sans formaliser la vulnérabilité de confusion d'interface lors de l'approbation humaine (Confused Deputy HITL).
  7. *A2A v1.0 Agent Card signée* (Ch. 8, p. 97) : Absence de liaison cryptographique de session temps réel (Proof-of-Possession / DPoP RFC 9449 ou mTLS RFC 8705), laissant la porte ouverte aux attaques par rejeu de profil.

---

## 2. Logic Chain
1. **Du transport sans état au risque de double exécution** : Si le transport élimine l'état de session et que la règle de reprise consiste à réémettre sous un `id` JSON-RPC incrémenté, alors toute méthode `tools/call` à effet de bord interrompue après exécution serveur mais avant acquittement client sera réexécutée. En l'absence de clé d'idempotence obligatoire dans la charge utile JSON-RPC 2.0, l'opération n'est pas idempotente, causant un préjudice financier direct.
2. **De la dépréciation des roots au Path Traversal** : Si l'hôte délègue la spécification du répertoire cible aux arguments d'outils générés par le LLM au lieu d'une liste de racines négociée à l'initialisation, une injection indirecte de prompt forçant l'émission d'un chemin arbitraire (ex: clés SSH ou répertoires système) sera exécutée par le serveur local sans opposition d'un garde-fou hôte au niveau applicatif.
3. **De la pollution de stdout au déni de service IPC** : Si des bibliothèques tierces émettent des journaux ou avertissements non sollicités sur `stdout`, le parseur NDJSON du client MCP interprète ces chaînes comme des trames JSON corrompues, déclenchant l'erreur fatale `-32700` et provoquant la fermeture du sous-processus serveur.
4. **De la confusion d'erreurs à la rupture de la boucle agentique** : Si les serveurs MCP retournent des erreurs JSON-RPC formelles (`error`) au lieu de succès contenant `isError: true`, les clients hôtes lèvent des exceptions système bloquantes au lieu de transmettre le message d'erreur au contexte du modèle pour réévaluation et correction stochastique.
5. **De la concurrence AP2 au dépassement budgétaire** : Si un Intent Mandate autorise un plafond budgétaire sans registre de sérialisation atomique, deux sous-agents opérant en parallèle peuvent générer deux Cart Mandates valides individuellement mais dont la somme excède le plafond autorisé, entraînant un dépassement financier lors du règlement simultané.
6. **De la statique des Agent Cards à l'usurpation d'identité** : Une signature sur un fichier JSON statique prouve l'intégrité de la déclaration, non la légitimité du porteur de la connexion TCP/TLS. Sans mécanisme de preuve de possession (DPoP), une Agent Card interceptée peut être rejouée par un agent malveillant.

---

## 3. Caveats
- L'audit s'est appuyé sur les spécifications officielles MCP publiées par Anthropic (2024-2026), les brouillons de l'IETF (RFC 6749, RFC 7643, RFC 8693, RFC 9207, RFC 9421, RFC 9449, drafts WIMSE) et les annonces de la Linux Foundation pour A2A et AP2.
- La révision MCP du 2026-07-28 mentionnée dans le texte comme "revalidation du 30 juillet 2026" présente un statut hybride dans le manuscrit (considérée comme non acquise au gel du 27 juillet mais instruite en profondeur) ; l'audit a pris en compte sa substance technique telle qu'exposée par l'auteur.
- Aucun test d'intrusion physique sur les serveurs MCP d'éditeurs tiers n'a été réalisé ; la démonstration repose sur l'analyse formelle des protocoles de transport et des machines à états distribuées.

---

## 4. Conclusion
Le segment protocoles (pp. 78 à 145) présente une solidité conceptuelle et documentaire remarquable quant à la traçabilité des sources et à la rigueur épistémique de non-généralisation.
Toutefois, sous l'angle de l'ingénierie protocolaire pure et de la sécurité formelle des systèmes distribués, le texte comporte **trois anomalies bloquantes** (rupture d'idempotence sur HTTP sans état, suppression du confinement de sécurité par dépréciation des roots MCP, vulnérabilité de framing sur stdio) et **quatre failles majeures** (confusion du typage d'erreurs JSON-RPC, concurrence non atomique d'AP2, angle mort HITL face à l'injection transitive, et absence de Proof-of-Possession pour les Agent Cards).
Ces constats doivent être intégrés pour blinder le compendium avant publication finale.

---

## 5. Verification Method
1. **Inspection des citations et localisations** :
   - Vérifier dans `documents/DOCUMENT_TEXT_MAP.md` les lignes 6478 à 12186.
   - Vérifier visuellement les planches PNG correspondantes dans `documents/scratch/document_pages/` (`page-91.png`, `page-92.png`, `page-93.png`, `page-94.png`, `page-118.png`, `page-131.png`).
2. **Vérification normative externe** :
   - Spécification officielle MCP (Model Context Protocol Specification, sections *Transports*, *Tools*, *Roots*).
   - Spécification JSON-RPC 2.0 (RFC / JSON-RPC Specification, sections 5.1 *Error object* et codes d'erreur réservés).
   - IETF RFC 9449 (OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer - DPoP).
   - W3C Verifiable Credentials Data Model v2.0.
