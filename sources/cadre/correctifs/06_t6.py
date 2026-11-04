"""Correctifs de la revue du 3 novembre 2026 — tranche : annexes B à G (corps.html).

L'annexe H (sections H.1 à H.5) est corrigée directement dans actualisation-2026-11.html;
ses correctifs sont consignés dans JOURNAL sous « Annexe H, … ». Les lignes du registre de
l'annexe D ne sont pas touchées : 99_registre.py les régénère.
Les empreintes des annexes B et C ont été recalculées (SHA-256 de la canonisation RFC 8785).
"""
NBSP = ' '

CORRECTIONS = [
    # [6.05] statut normatif de B fondé sur le renvoi de GOV-07 (A-23)
    ('Il est normatif par son contenu, pas par sa forme\xa0: tout outil de registre convient s’il conserve ces champs et leur historique.</p>',
     'Il est normatif par son contenu, pas par sa forme, parce que l’EXIG-GOV-07 y renvoie (section 1.4)\xa0: tout outil de registre convient s’il conserve ces champs et leur historique.</p>',
     ['22-07', '23-09']),
    # jalon (A-27); pilote = mise en production (A-25); existant inventorié (A-26)
    ('ce que vérifie le point de contrôle qui clôt l’étape Construction et évaluation; avant cela, l’agent n’obtient aucun jeton d’exécution en production.</li>',
     'ce que vérifie le jalon qui clôt l’étape Construction et évaluation; avant cela, l’agent n’obtient aucun jeton d’exécution en production, et un pilote sur données réelles est une mise en production (section 11.5). Un agent déjà en exploitation à l’adoption du cadre reçoit une fiche minimale (champs de l’étape Proposition) sous la mesure transitoire de l’EXIG-GOV-21.</li>',
     ['A-25', 'A-26', 'A-27']),
    # [6.05, 6.06, 6.01] règle portée par GOV-07, AUT-08 et AUT-24; préséance du catalogue; grandeur mesurée
    ('<li><strong>Source de vérité.</strong> Les valeurs qui commandent un contrôle (palier d’outil, seuil, plafond, portées, niveau d’autonomie) DOIVENT être lues par la passerelle dans le registre et le catalogue, jamais dans ce que l’agent déclare de lui-même ni dans les annotations d’un serveur MCP (section 8.3).</li>',
     '<li><strong>Source de vérité.</strong> Les valeurs qui commandent un contrôle (palier d’outil, seuil, plafond, portées, niveau d’autonomie) sont lues par la passerelle dans le registre et le catalogue, jamais dans ce que l’agent déclare de lui-même ni dans les annotations d’un serveur MCP (EXIG-GOV-07, EXIG-AUT-08, section 8.3). Le palier et le seuil d’un outil sont tenus au seul catalogue\xa0: la fiche ne peut fixer qu’un seuil plus strict, et la passerelle signale tout écart de palier entre la fiche et le catalogue comme un incident de réconciliation. La grandeur qu’un seuil mesure est calculée par la passerelle ou fournie par le système visé, jamais déclarée par l’agent (EXIG-AUT-24).</li>',
     ['22-07', '22-08', '22-01']),
    # [6.08, 6.32] renvoi à GOV-12 (A-24); analogie Feng nuancée
    ('<li><strong>Réévaluation.</strong> Tout changement de modèle ou de version de modèle, d’instructions système, d’outil ou de palier d’outil, de version majeure d’un contrat ou d’un protocole, de population visée, de finalité ou de catégorie de données, ainsi que tout incident grave ou toute dérive détectée, déclenche une réévaluation de la classe de risque et du niveau d’autonomie (EXIG-GOV-12). Le niveau d’autonomie fonctionne comme le «\xa0certificat d’autonomie\xa0» de Feng et al., qui se renouvelle à chaque changement de l’agent ou de son environnement<strong><sup>[83]</sup></strong>.',
     '<li><strong>Réévaluation.</strong> Tout changement visé par l’EXIG-GOV-12, qui tient seule la liste des déclencheurs, entraîne une réévaluation de la classe de risque et du niveau d’autonomie avant la mise en service. Le niveau d’autonomie fonctionne comme un certificat interne qui se renouvelle à chaque changement de l’agent ou de son environnement, sans l’indépendance du tiers qui délivre le «\xa0certificat d’autonomie\xa0» de Feng et al.<strong><sup>[83]</sup></strong>.',
     ['23-10', '22-09', '22-11']),
    # A-34
    ('<li><strong>Attestation.</strong> Le propriétaire métier atteste périodiquement',
     '<li><strong>Attestation.</strong> Le parrain atteste périodiquement',
     ['A-34']),
    # [6.39] renvois; A-03
    ('(EXIG-GOV-07, EXIG-FIN-07)</td><td>Proposition (modèles et invite\xa0: Conception)</td>',
     '(EXIG-INT-15, EXIG-GOV-12); pour un agent intégré à un logiciel-service, actions qu’il y exécute, mécanisme d’arrêt propre et mécanisme d’approbation du fournisseur (EXIG-ARC-26)</td><td>Proposition (modèles et invite\xa0: Conception)</td>',
     ['22-29', 'A-03']),
    # [6.06] A-09, A-17
    ('palier P0 à P3 attribué au catalogue, seuil, effet déclaré, clé d’idempotence pour les outils à effet, contrat AsyncAPI pour les événements</td>',
     'palier P0 à P3 et seuil tels qu’inscrits au catalogue (la fiche ne fixe qu’un seuil plus strict, EXIG-AUT-24), effet déclaré, clé d’idempotence et mode de vérification pour les outils à effet (EXIG-ORC-22), compensation et son palier (EXIG-ORC-17), étiquette de fiabilité de chaque source de contexte (EXIG-SEC-03), contrat AsyncAPI pour les événements</td>',
     ['22-08', 'A-09', 'A-17']),
    # A-06
    ('<td>Compensation de chaque étape à effet; étape pivot;',
     '<td>Compensation de chaque étape à effet et identité de compensation de l’orchestrateur (EXIG-ORC-31); étape pivot;',
     ['A-06']),
    # A-18
    ('emplacement du journal d’audit;',
     'emplacement du journal d’audit et, pour une décision visée par l’article 12.1, du dossier de décision (EXIG-OBS-14);',
     ['A-18']),
    # [6.34]
    ('<td>État (proposé, conception, construction, pilote, production, suspendu, retiré);',
     '<td>État (proposé, conception, construction, pilote, production, suspendu, retiré), énumération commune au registre et au catalogue (annexe C, C.2);',
     ['22-12']),
    # [6.33, 6.38]
    ('Les noms de champs sont un choix du cadre; seules comptent leur présence et leur cohérence avec le gabarit.</p>',
     'Les noms de champs sont un choix du cadre; seules comptent leur présence et leur cohérence avec le gabarit. Les personnes y sont désignées par un identifiant fictif, et les empreintes sont abrégées par «\xa0…\xa0».</p>',
     ['22-10', '22-16']),
    # [6.06, 6.07, 6.08, 6.33, 6.37, 6.38, 6.40] fiche d’exemple
    ('<pre><code>{\n  "agent_id": "agt-fin-rapprochement",\n  "name": "Agent de rapprochement des factures fournisseurs",\n  "version": "2.3.0",\n  "lifecycle_state": "production",\n  "owners": {\n    "business_sponsor": "Directrice, comptes fournisseurs",\n    "technical_lead": "Responsable technique, plateforme Finances",\n    "on_call_team": "garde-finances",\n    "cost_center": "CC-4120"\n  },\n  "purpose": "Apparier factures, bons de commande et réceptions; préparer les paiements.",\n  "excluded_uses": ["modifier les coordonnées bancaires d\'un fournisseur"],\n  "principals": ["role:analyste-comptes-fournisseurs", "agent:agt-fin-orchestrateur"],\n  "orchestration_pattern": "agent-unique-outille",\n  "risk_class": "modere",\n  "autonomy": {\n    "ceiling": "N3",\n    "approved_by": "Directrice, comptes fournisseurs",\n    "approved_on": "2027-03-15",\n    "odd_ref": "ODD-FIN-007",\n    "renew_on": ["model_change", "new_write_tool", "target_population_change"]\n  },\n  "regulatory": {"eu_ai_act_high_risk": false, "automated_decision_art_12_1": false},\n  "tools": [\n    {"ref": "erp.factures.lire@1.4.0", "digest": "sha256:9f2c41d0", "tier": "P1"},\n    {"ref": "erp.factures.apparier@2.0.1", "digest": "sha256:51ab07e3", "tier": "P2",\n     "threshold_cad": 5000, "compensation": "erp.factures.desapparier", "idempotency_key": true},\n    {"ref": "tresorerie.paiements.emettre@1.1.0", "digest": "sha256:c07d9b12", "tier": "P3",\n     "approval": "signed_out_of_band"}\n  ],\n  "data": {"classification": "confidentiel", "personal_information": true,\n           "processing_locations": ["Québec"]},\n  "identity": {"workload_id": "spiffe://entreprise.example/agents/agt-fin-rapprochement",\n               "access_mode": "token_exchange_rfc8693", "token_ttl_s": 900},\n  "budget_per_task": {"max_tokens": 50000, "max_cost_cad": 0.75,\n                      "max_tool_calls": 15, "timeout_s": 60, "max_wall_clock_s": 28800,\n                      "max_iterations": 8},\n  "evaluation": {"reference_set": 120, "adversarial_cases": 25,\n                 "last_run": "2027-03-10", "result": "pass"},\n  "observability": {"service_name": "agt-fin-rapprochement",\n                    "genai_semconv": "1.41.0", "content_capture": false},\n  "compliance": {"efvp_ref": "EFVP-2027-014", "efvp_date": "2027-02-28"},\n  "next_review": "2027-09-15",\n  "exceptions": []\n}</code></pre>',
     '<pre><code>{\n  "agent_id": "agt-fin-rapprochement",\n  "name": "Agent de rapprochement des factures fournisseurs",\n  "version": "2.3.0",\n  "lifecycle_state": "production",\n  "owners": {\n    "business_sponsor": "emp-004417",\n    "technical_lead": "emp-007762",\n    "on_call_team": "garde-finances",\n    "cost_center": "CC-4120"\n  },\n  "purpose": "Apparier factures, bons de commande et réceptions; préparer les paiements.",\n  "excluded_uses": ["modifier les coordonnées bancaires d\'un fournisseur"],\n  "principals": ["role:analyste-comptes-fournisseurs", "agent:agt-fin-orchestrateur"],\n  "triggers": ["schedule:rapprochement-nocturne"],\n  "orchestration_pattern": "agent-unique-outille",\n  "risk_class": "moderee",\n  "autonomy": {\n    "ceiling": "N3",\n    "requested_by": "emp-004417",\n    "approved_by": "emp-002318",\n    "approved_on": "2027-03-15",\n    "odd_ref": "ODD-FIN-007",\n    "renew_on": "EXIG-GOV-12"\n  },\n  "regulatory": {"eu_ai_act_high_risk": false, "automated_decision_art_12_1": false},\n  "tools": [\n    {"ref": "erp.factures.lire@1.4.0", "digest": "sha256:9f2c41d0…", "tier": "P1"},\n    {"ref": "erp.factures.apparier@2.0.1", "digest": "sha256:51ab07e3…", "tier": "P2",\n     "compensation": "erp.factures.desapparier@2.0.1", "idempotency_key": true},\n    {"ref": "tresorerie.paiements.emettre@1.1.0", "digest": "sha256:c07d9b12…", "tier": "P3",\n     "approval": "signed_out_of_band", "idempotency_key": true, "pivot": true, "compensation": null}\n  ],\n  "data": {"classification": "confidentiel", "personal_information": true,\n           "processing_locations": ["Québec"]},\n  "identity": {"workload_id": "spiffe://ent.ca/agt-fin-rapprochement",\n               "access_modes": {"principals": "token_exchange_rfc8693", "triggers": "client_credentials"},\n               "token_ttl_s": 900},\n  "budget_per_task": {"max_tokens": 50000, "max_cost_cad": 0.75,\n                      "max_tool_calls": 15, "timeout_s": 60, "max_wall_clock_s": 28800,\n                      "max_iterations": 8},\n  "evaluation": {"reference_set": 120, "adversarial_cases": 25,\n                 "last_run": "2027-03-10", "result": "pass"},\n  "observability": {"service_name": "agt-fin-rapprochement",\n                    "genai_semconv_reference": "1.41.0", "genai_semconv_emitted": "1.41.0",\n                    "otel_semconv_stability_opt_in": "gen_ai_latest_experimental",\n                    "content_capture": false},\n  "compliance": {"efvp_ref": "EFVP-2027-014", "efvp_date": "2027-02-28"},\n  "next_review": "2027-09-15",\n  "exceptions": []\n}</code></pre>',
     ['22-06', '22-08', '22-09', '22-10', '22-15', '22-16', '22-17', 'A-24', 'A-29']),
    # [6.07, 6.35, 6.37] lecture
    ('<p>Lecture\xa0: l’agent apparie seul les factures sous 5\u202f000\xa0$, au-delà de quoi la passerelle exige une approbation; l’émission d’un paiement, de palier P3, exige toujours une approbation signée hors bande. Les valeurs de l’enveloppe budgétaire sont illustratives et se calibrent par mesure (section 10.6).</p>',
     '<p>Lecture\xa0: l’agent apparie seul les factures jusqu’à 5\u202f000\xa0$ inclusivement, seuil inscrit au catalogue pour l’outil d’appariement, que la fiche ne reprend pas; au-delà, le contrôle calculé (EXIG-AUT-10) exige une approbation. Les paliers recopiés dans la fiche servent à la lecture\xa0: le catalogue fait foi. L’émission d’un paiement, de palier P3, exige toujours une approbation signée hors bande; c’est l’étape pivot, sans compensation, et elle porte une clé d’idempotence vérifiée par la trésorerie. Les tâches lancées par une personne ou par l’orchestrateur passent par l’échange de jetons, et le rapprochement nocturne, déclenché par planification, emploie l’identité propre de l’agent (section 9.3). <code>renew_on</code> renvoie à l’EXIG-GOV-12 au lieu d’en recopier la liste. Le niveau N3 est demandé par le parrain et approuvé par une autre personne. Les conventions OpenTelemetry sont consignées par version de référence, version émise et réglage d’adhésion (EXIG-OBS-01). Les valeurs de l’enveloppe budgétaire sont illustratives et se calibrent par mesure (section 10.6).</p>',
     ['22-06', '22-08', '22-13', '22-15', 'A-29']),
    # [6.05] A-23
    ('Ils sont normatifs par leur forme, pas par leurs valeurs\xa0: un contrat réel reprend leur structure et leurs champs, avec ses propres noms, schémas et seuils.',
     'Ces exemples sont informatifs (section 1.4). Leur structure devient normative là où une exigence y renvoie expressément\xa0: C.1 et C.2 par l’EXIG-ORC-22 et l’EXIG-MCP-20, C.6 par l’EXIG-AUT-12, C.8 par l’EXIG-OBS-12; un contrat réel reprend alors leur structure et leurs champs, avec ses propres noms, schémas et seuils.',
     ['22-07', '23-09']),
    # [6.40, 6.49]
    ('<li><strong>Valeurs fictives.</strong> Les noms, domaines (<code>ent.ca</code>), identifiants et montants sont fictifs.</li>',
     '<li><strong>Valeurs fictives.</strong> Les noms, domaines (<code>ent.ca</code>), identifiants et montants sont fictifs. Un seul domaine fictif, <code>ent.ca</code>, sert partout, et son inverse, <code>ca.ent</code>, préfixe les types d’événements. Les montants des arguments d’outil sont des entiers en cents, ce qui ne laisse aucune place à une lecture divergente des nombres (EXIG-AUT-12).</li>',
     ['22-17', '23-13', '22-26']),
    # [6.56] entrées des hachages explicitées
    ('sont de véritables condensés SHA-256, calculés sur les valeurs montrées (forme canonique RFC 8785 pour les objets JSON)\xa0: on peut les recalculer.',
     'sont de véritables condensés SHA-256, calculés sur les valeurs montrées (forme canonique RFC 8785 pour les objets JSON)\xa0: on peut les recalculer. La description de C.1, coupée pour la lecture, se canonise en une seule ligne, chaque coupure valant une espace; la clé d’idempotence est l’empreinte de la canonisation du tableau <code>["idem-v1", task_id, step_id]</code> (section 7.6), et h celle de l’objet {outil, version, definition_digest, agent_id, task_id, arguments} (section 8.5).',
     ['23-15', '24-08']),
    # [6.03]
    ('crée un bon de commande de 12\xa0480\xa0$, soit au-delà du seuil d’approbation de 5\xa0000\xa0$ fixé au catalogue pour cet outil.',
     'crée un bon de commande de 12\u202f480\xa0$, soit au-delà du seuil d’approbation de 5\u202f000\xa0$ par tâche fixé au catalogue pour cet outil et mesuré sur le total calculé des lignes.',
     ['22-02']),
    # tableau 64
    ('<td>EXIG-AUT-08, EXIG-MCP-14, EXIG-MCP-20, EXIG-ORC-22; section 6.8</td>',
     '<td>EXIG-AUT-08, EXIG-AUT-24, EXIG-MCP-14, EXIG-MCP-20, EXIG-ORC-17, EXIG-ORC-22; section 6.8</td>',
     ['A-13']),
    # tableau 64
    ('<td>EXIG-EVT-02, EXIG-EVT-04 à EXIG-EVT-06, EXIG-EVT-09</td>',
     '<td>EXIG-EVT-02, EXIG-EVT-04 à EXIG-EVT-06, EXIG-EVT-09, EXIG-EVT-11</td>',
     ['A-02']),
    # tableau 64
    ('<td>EXIG-AUT-12 à EXIG-AUT-14</td>',
     '<td>EXIG-AUT-09, EXIG-AUT-12 à EXIG-AUT-15, EXIG-AUT-19</td>',
     ['A-12']),
    # [6.57] IAM-11 retirée de C.8
    ('<td>EXIG-OBS-11, EXIG-OBS-12, EXIG-AUT-10, EXIG-IAM-11, EXIG-IAM-21; section 10.3</td>',
     '<td>EXIG-OBS-11 à EXIG-OBS-13, EXIG-AUT-10, EXIG-AUT-15, EXIG-IAM-21; section 10.3</td>',
     ['23-22']),
    # [6.01, 6.49, 6.53] C.1 : montant retiré des arguments, cents, état soumis défini
    ('<pre><code>{\n  "name": "approvisionnement_creer_bon_commande",\n  "title": "Créer un bon de commande (ERP)",\n  "description": "Crée dans l\'ERP un bon de commande, à l\'état brouillon ou soumis, pour un fournisseur\nhomologué et un centre de coûts valide. Une relance avec la même clé d\'idempotence ne crée pas de second bon.\nNe modifie ni n\'annule un bon existant.",\n  "inputSchema": {\n    "type": "object",\n    "properties": {\n      "idempotency_key": { "type": "string", "pattern": "^[0-9a-f]{64}$" },\n      "fournisseur_id": { "type": "string", "pattern": "^SUP-[0-9]{6}$" },\n      "centre_cout": { "type": "string", "pattern": "^CC-[0-9]{4}$", "x-mcp-header": "Cost-Center" },\n      "statut_demande": { "type": "string", "enum": ["brouillon", "soumis"], "default": "brouillon" },\n      "montant_total_cad": { "type": "number", "exclusiveMinimum": 0 },\n      "lignes": {\n        "type": "array",\n        "minItems": 1,\n        "maxItems": 100,\n        "items": {\n          "type": "object",\n          "properties": {\n            "sku": { "type": "string", "pattern": "^PRD-[0-9]{5}$" },\n            "quantite": { "type": "integer", "minimum": 1 },\n            "prix_unitaire_cad": { "type": "number", "minimum": 0 }\n          },\n          "required": ["sku", "quantite", "prix_unitaire_cad"],\n          "additionalProperties": false\n        }\n      }\n    },\n    "required": ["idempotency_key", "fournisseur_id", "centre_cout", "montant_total_cad", "lignes"],\n    "additionalProperties": false\n  },\n  "outputSchema": {\n    "type": "object",\n    "properties": {\n      "bon_commande_id": { "type": "string", "pattern": "^BC-[0-9]{4}-[0-9]{6}$" },\n      "statut": { "type": "string", "enum": ["brouillon", "soumis"] },\n      "montant_total_cad": { "type": "number" },\n      "rejeu": { "type": "boolean", "description": "Vrai si la clé était déjà traitée." }\n    },\n    "required": ["bon_commande_id", "statut", "montant_total_cad", "rejeu"],\n    "additionalProperties": false\n  },\n  "annotations": {\n    "readOnlyHint": false,\n    "destructiveHint": false,\n    "idempotentHint": true,\n    "openWorldHint": false\n  }\n}</code></pre>',
     '<pre><code>{\n  "name": "approvisionnement_creer_bon_commande",\n  "title": "Créer un bon de commande (ERP)",\n  "description": "Crée dans l\'ERP un bon de commande, à l\'état brouillon ou soumis, pour un fournisseur\nhomologué et un centre de coûts valide. Le statut soumis transmet le bon au circuit d\'approbation interne de l\'ERP,\nsans envoi au fournisseur. Le serveur calcule le montant total à partir des lignes; les prix sont en cents.\nUne relance avec la même clé d\'idempotence ne crée pas de second bon. Ne modifie ni n\'annule un bon existant.",\n  "inputSchema": {\n    "type": "object",\n    "properties": {\n      "idempotency_key": { "type": "string", "pattern": "^[0-9a-f]{64}$" },\n      "fournisseur_id": { "type": "string", "pattern": "^SUP-[0-9]{6}$" },\n      "centre_cout": { "type": "string", "pattern": "^CC-[0-9]{4}$", "x-mcp-header": "Cost-Center" },\n      "statut_demande": { "type": "string", "enum": ["brouillon", "soumis"], "default": "brouillon" },\n      "lignes": {\n        "type": "array",\n        "minItems": 1,\n        "maxItems": 100,\n        "items": {\n          "type": "object",\n          "properties": {\n            "sku": { "type": "string", "pattern": "^PRD-[0-9]{5}$" },\n            "quantite": { "type": "integer", "minimum": 1, "maximum": 100000 },\n            "prix_unitaire_cents": { "type": "integer", "minimum": 0, "maximum": 100000000 }\n          },\n          "required": ["sku", "quantite", "prix_unitaire_cents"],\n          "additionalProperties": false\n        }\n      }\n    },\n    "required": ["idempotency_key", "fournisseur_id", "centre_cout", "lignes"],\n    "additionalProperties": false\n  },\n  "outputSchema": {\n    "type": "object",\n    "properties": {\n      "bon_commande_id": { "type": "string", "pattern": "^BC-[0-9]{4}-[0-9]{6}$" },\n      "statut": { "type": "string", "enum": ["brouillon", "soumis"] },\n      "montant_total_cents": { "type": "integer", "minimum": 0 },\n      "rejeu": { "type": "boolean", "description": "Vrai si la clé était déjà traitée." }\n    },\n    "required": ["bon_commande_id", "statut", "montant_total_cents", "rejeu"],\n    "additionalProperties": false\n  },\n  "annotations": {\n    "readOnlyHint": false,\n    "destructiveHint": false,\n    "idempotentHint": true,\n    "openWorldHint": false\n  }\n}</code></pre>',
     ['22-01', '22-26', '22-05']),
    # [6.01, 6.49]
    ('Le motif du champ <code>idempotency_key</code> correspond à la dérivation de la section 7.6, et seul <code>centre_cout</code> porte',
     'Le motif du champ <code>idempotency_key</code> correspond à la dérivation de la section 7.6. Le montant total n’est pas un argument\xa0: le serveur le calcule à partir des lignes et le renvoie, et la passerelle calcule la même grandeur pour le seuil (EXIG-AUT-24); les prix sont des entiers en cents, bornés par le schéma. Seul <code>centre_cout</code> porte',
     ['22-01', '22-26']),
    # A-08 : champ compensation au catalogue
    ('signale une erreur métier par un résultat marqué <code>isError: true</code> (EXIG-MCP-07).</p>',
     'signale une erreur métier par un résultat marqué <code>isError: true</code> (EXIG-MCP-07). La compensation de l’outil et son palier figurent à son entrée de catalogue (C.2), la définition C.1 ne portant que des champs du schéma MCP.</p>',
     ['A-08']),
    # [6.01, 6.03, 6.35, 6.50, 6.34] C.2
    ('<pre><code>{\n  "ref": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",\n  "tool_name": "approvisionnement_creer_bon_commande",\n  "contract_version": "1.4.0",\n  "definition_digest": "sha256:3182dbf3bec38e95fffa2b16ae58217e0cc09251bfbe026b5939c25729f99e1e",\n  "server": {\n    "id": "mcp-approvisionnement",\n    "endpoint": "https://passerelle-agents.ent.ca/mcp/approvisionnement",\n    "mcp_revision": "2026-07-28",\n    "extensions_allowed": []\n  },\n  "lifecycle_state": "active",\n  "tier": "P2",\n  "approval_threshold": { "argument": "montant_total_cad", "max_without_approval_cad": 5000 },\n  "compensation": "mcp-approvisionnement/approvisionnement_annuler_bon_commande@1.2.0",\n  "idempotency": { "argument": "idempotency_key", "checked_by_server": true, "on_conflict": "reject" },\n  "oauth_scope": "approvisionnement.bons-commande.creer",\n  "header_projection": { "centre_cout": "Mcp-Param-Cost-Center" },\n  "data_classification_max": "confidentiel",\n  "personal_information": false,\n  "owner": "Direction Approvisionnement",\n  "on_call_team": "garde-plateforme-erp",\n  "known_consumers": ["agt-achats-indirects"],\n  "reviewed_by": ["proprietaire-outil", "securite"],\n  "approved_on": "2026-10-06",\n  "next_review": "2027-04-06"\n}</code></pre>',
     '<pre><code>{\n  "ref": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",\n  "tool_name": "approvisionnement_creer_bon_commande",\n  "contract_version": "1.4.0",\n  "definition_digest": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",\n  "server": {\n    "id": "mcp-approvisionnement",\n    "endpoint": "https://passerelle-agents.ent.ca/mcp/approvisionnement",\n    "mcp_revision": "2026-07-28",\n    "extensions_allowed": []\n  },\n  "lifecycle_state": "production",\n  "tier": "P2",\n  "approval_thresholds": [\n    { "measure": "sum(lignes[].quantite * lignes[].prix_unitaire_cents)", "computed_by": "gateway",\n      "unit": "cents_cad", "scope": "task", "window": "task",\n      "max_without_approval": 500000, "inclusive": true },\n    { "measure": "sum(lignes[].quantite * lignes[].prix_unitaire_cents)", "computed_by": "gateway",\n      "unit": "cents_cad", "scope": "counterparty:fournisseur_id", "window_s": 86400,\n      "max_without_approval": 2000000, "inclusive": true }\n  ],\n  "compensation": { "ref": "mcp-approvisionnement/approvisionnement_annuler_bon_commande@1.2.0", "tier": "P2" },\n  "idempotency": { "argument": "idempotency_key", "mode": "native", "checked_by_server": true,\n                   "on_conflict": "reject", "on_in_progress": "refuse", "on_duplicate": "replay_result",\n                   "key_retention_s": 864000 },\n  "oauth_scope": "approvisionnement.bons-commande.creer",\n  "header_projection": { "centre_cout": "Mcp-Param-Cost-Center" },\n  "data_classification_max": "confidentiel",\n  "personal_information": false,\n  "owner": "Direction Approvisionnement",\n  "on_call_team": "garde-plateforme-erp",\n  "known_consumers": ["agt-achats-indirects"],\n  "reviewed_by": ["responsable-outil", "securite"],\n  "approved_on": "2026-10-06",\n  "next_review": "2027-04-06"\n}</code></pre>',
     ['22-01', '22-02', '22-13', '22-27', '22-12']),
    # A-34
    ('Lecture\xa0: cette entrée porte le palier, le seuil, la compensation, la portée, le propriétaire et l’équipe de garde de l’outil, attribués après revue par son propriétaire et par la sécurité;',
     'Lecture\xa0: cette entrée porte le palier, les seuils, la compensation et son palier, la portée, la direction responsable et l’équipe de garde de l’outil, attribués après revue par son responsable et par la sécurité;',
     ['A-34']),
    # [6.01, 6.03, 6.35, 6.50, 6.34]
    ('Avec ce palier P2 et ce seuil, un agent de classe modérée déclaré N3 peut créer seul un bon de 5\xa0000\xa0$ ou moins; au-delà, la règle de la section 8.4 impose le jeton d’approbation de l’exemple C.6. L’idempotence déclarée ici, vérifiée par le serveur, fait office de garantie, alors que l’annotation <code>idempotentHint</code> n’en est qu’un indice (EXIG-ORC-22).</p>',
     'Chaque seuil mesure une grandeur que la passerelle calcule à partir des lignes canonisées, jamais un montant déclaré par l’agent, et déclare son unité, sa portée et sa fenêtre; la borne est inclusive, et les compteurs de la tâche et du fournisseur sont tenus par la passerelle (EXIG-AUT-24). Avec ce palier P2 et ces seuils, un agent de classe modérée déclaré N3 peut créer seul des bons totalisant 5\u202f000\xa0$ ou moins dans une tâche, et 20\u202f000\xa0$ ou moins par fournisseur sur 24 heures; au-delà, le contrôle calculé (EXIG-AUT-10) impose le jeton d’approbation de l’exemple C.6. La compensation est elle-même un outil inscrit avec son palier (EXIG-ORC-17). L’idempotence est native, vérifiée par l’ERP; l’entrée déclare les trois comportements de l’EXIG-ORC-22 et la durée de conservation des clés, qui couvre la durée de vie maximale de la tâche durable, la fenêtre de reprise et le délai de réconciliation, alors que l’annotation <code>idempotentHint</code> n’est qu’un indice. <code>lifecycle_state</code> reprend l’énumération du tableau 63.</p>',
     ['22-01', '22-02', '22-13', '22-27', '22-12']),
    # alignement sur EXIG-A2A-02 (t2)
    ('L’exemple montre la carte publiée au registre par l’agent spécialiste',
     'L’exemple montre la carte de référence, inscrite au catalogue et servie par la passerelle, de l’agent spécialiste',
     ['A-20']),
    # [6.43]
    ('règles de présence des champs de la spécification (section 8.4.1) appliquées;',
     'règles de présence des champs de la spécification (section 8.4 de la spécification A2A 1.0) appliquées;',
     ['22-20']),
    # [6.52] A-33
    ('et tout client vérifie cette signature avant de se fier à la carte (EXIG-A2A-03).',
     'et tout client vérifie cette signature avant de se fier à la carte (EXIG-A2A-03). La clé se résout par <code>kid</code> dans le jeu de clés épinglé au catalogue, et <code>jku</code> n’est suivi que s’il concorde exactement avec l’URL inscrite pour cet émetteur, ce qui écarte la falsification de requêtes côté serveur contre laquelle la RFC 8725 met en garde (section 3.10).',
     ['22-04']),
    # alignement sur EXIG-A2A-06 (t2)
    ('ils sont déclarés comme extension de données facultative,',
     'ils sont déclarés comme extension de données facultative, qui ne figure que dans une carte servie aux seuls clients authentifiés (carte de référence d’un agent interne, ou carte étendue d’un agent exposé, EXIG-A2A-06),',
     ['A-20']),
    # [6.44, 6.45]
    ('et <code>version</code>, en SemVer, dont dérive l’<code>ETag</code> servi avec la carte, permet de revalider les copies en cache (EXIG-A2A-04).</p>',
     'et l’<code>ETag</code> servi avec la carte, dérivé du hachage de la représentation servie, signatures comprises, permet de revalider les copies en cache, alors que <code>version</code>, en SemVer, signale la compatibilité (EXIG-A2A-04). L’agent étant de classe élevée, ses appelants présentent un jeton lié par mTLS ou DPoP (EXIG-IAM-14); l’exemple, réduit au schéma OpenID Connect, ne montre pas le schéma mTLS qu’un contrat réel y combinerait dans <code>securityRequirements</code>.</p>',
     ['22-21', '22-22']),
    # [6.40]
    ('"type": "ca.entreprise.logistique.alerte.rupture.v1",\n  "subject": "MTL-02/PRD-99210",',
     '"type": "ca.ent.logistique.alerte.rupture.v1",\n  "subject": "MTL-02/PRD-99210",',
     ['22-17']),
    # [6.48, 6.42] A-02
    ('Un agent qui réagit à cette alerte publie un nouvel événement dont <code>xagenthopcount</code> vaut 2 et qui recopie <code>xagentorigin</code> et <code>xagentmaxhops</code>; un événement dont le compteur atteint 4 n’est pas traité et part en file de lettres mortes (EXIG-EVT-06).',
     'Quand un agent qui réagit à cette alerte publie un nouvel événement, l’intercepteur de publication pose <code>xagenthopcount</code> à 2 et recopie <code>xagentorigin</code> et <code>xagentmaxhops</code>, sans se fier aux valeurs du producteur (EXIG-EVT-11); un événement dont le compteur atteint 4 n’est pas traité et part en file de lettres mortes (EXIG-EVT-06). Le compteur borne la profondeur d’une chaîne, non sa diffusion\xa0: le courtier applique aussi un plafond de largeur, en événements par trace (EXIG-EVT-11). La correspondance entre l’échelle de classification interne (C.2) et les valeurs de <code>dataclassification</code> est inscrite au catalogue.',
     ['22-25', '22-19', 'A-02']),
    # [6.47]
    ('les alertes d’un même article dans un même entrepôt restent dans l’ordre (EXIG-EVT-09)',
     'les alertes d’un même article dans un même entrepôt restent dans l’ordre, pourvu que le nombre de partitions soit figé au contrat et que le producteur soit idempotent ou n’ait qu’une requête en vol (EXIG-EVT-09)',
     ['22-24']),
    # [6.04]
    ('L’exemple complète l’extrait de la section 9.3\xa0: le jeton que présente l’agent d’analyse des dépenses, appelé par l’orchestrateur, au serveur MCP des finances, au nom d’Alice.</p>\n<p><strong>Jeton délégué après deux sauts, décodé (signature omise)</strong></p>',
     'L’exemple complète l’extrait de la section 9.3\xa0: les deux jetons qui portent, au nom d’Alice, l’appel de l’agent d’analyse des dépenses, appelé par l’orchestrateur, vers le serveur MCP des finances. La passerelle d’agents termine TLS\xa0: l’agent lui présente le jeton 1; elle le vérifie, puis obtient par échange le jeton 2, qu’elle présente au serveur (section 6.5).</p>\n<p><strong>Jetons délégués après deux sauts, décodés (signatures omises)</strong></p>',
     ['22-03']),
    # [6.04, 6.51] deux jetons
    ('<pre><code>En-tête\n{ "typ": "at+jwt", "alg": "ES256", "kid": "idp-2026-10" }\nCharge utile\n{\n  "iss": "https://idp.ent.ca",\n  "sub": "alice",\n  "aud": "https://mcp-finance.ent.ca",\n  "client_id": "agent-analyse-depenses",\n  "scope": "finance:read",\n  "act": {\n    "sub": "spiffe://ent.ca/agent-analyse-depenses",\n    "act": { "sub": "spiffe://ent.ca/agent-orch" }\n  },\n  "cnf": { "x5t#S256": "vzF5VHuU_5wCN7LdQZOXTK3y7aNQCqM5M-yosaTb6aw" },\n  "iat": 1793084700,\n  "exp": 1793085600,\n  "jti": "9f1c2d7e-5a41-4c3b-8e06-b2f94a1d7c55"\n}</code></pre>',
     '<pre><code>Jeton 1, présenté par l\'agent à la passerelle\nEn-tête\n{ "typ": "at+jwt", "alg": "ES256", "kid": "idp-2026-10" }\nCharge utile\n{\n  "iss": "https://idp.ent.ca",\n  "sub": "alice",\n  "aud": "https://passerelle-agents.ent.ca",\n  "client_id": "agent-analyse-depenses",\n  "scope": "finance:read",\n  "authorization_details": [{ "type": "lecture_depenses", "periode": "2026-T3" }],\n  "act": {\n    "sub": "spiffe://ent.ca/agent-analyse-depenses",\n    "act": { "sub": "spiffe://ent.ca/agent-orch" }\n  },\n  "cnf": { "x5t#S256": "vzF5VHuU_5wCN7LdQZOXTK3y7aNQCqM5M-yosaTb6aw" },\n  "iat": 1793084700,\n  "exp": 1793085600,\n  "jti": "9f1c2d7e-5a41-4c3b-8e06-b2f94a1d7c55"\n}\nJeton 2, obtenu par la passerelle et présenté au serveur MCP des finances (même en-tête)\nCharge utile\n{\n  "iss": "https://idp.ent.ca",\n  "sub": "alice",\n  "aud": "https://mcp-finance.ent.ca",\n  "client_id": "passerelle-agents",\n  "scope": "finance:read",\n  "authorization_details": [{ "type": "lecture_depenses", "periode": "2026-T3" }],\n  "act": {\n    "sub": "spiffe://ent.ca/agent-analyse-depenses",\n    "act": { "sub": "spiffe://ent.ca/agent-orch" }\n  },\n  "cnf": { "x5t#S256": "q8Lr2Wd0cJmE4sTnV7yHbA1fKpXzG3uN9oRiD5eC6wM" },\n  "iat": 1793084712,\n  "exp": 1793085600,\n  "jti": "3b7e90a1-6c2d-4f58-9a14-d0e8b5c2f716"\n}</code></pre>',
     ['22-03', '22-28', 'A-16']),
    # [6.04, 6.51, 6.17] lecture
    ('<p>Lecture\xa0: le jeton suit le profil JWT de la RFC 9068, avec l’en-tête <code>typ</code> <code>at+jwt</code> et les revendications <code>iss</code>, <code>exp</code>, <code>aud</code>, <code>sub</code>, <code>client_id</code>, <code>iat</code> et <code>jti</code> <strong><sup>[72]</sup></strong>. Alice reste le sujet; l’<code>act</code> externe désigne l’acteur courant, l’agent d’analyse des dépenses, et l’<code>act</code> imbriqué l’orchestrateur, acteur antérieur que le serveur consigne sans s’en servir pour décider (EXIG-IAM-08, EXIG-IAM-11)<strong><sup>[70]</sup></strong>. L’audience unique, la portée réduite à <code>finance:read</code> et la durée de vie de 900 secondes appliquent les exigences EXIG-IAM-10, EXIG-IAM-11 et EXIG-IAM-15. <code>cnf</code> lie le jeton à l’empreinte du certificat X.509-SVID de l’agent\xa0: volé, il ne sert à rien sans la clé privée correspondante (EXIG-IAM-14)<strong><sup>[328]</sup></strong>.</p>',
     '<p>Lecture\xa0: les deux jetons suivent le profil JWT de la RFC 9068, avec l’en-tête <code>typ</code> <code>at+jwt</code> et les revendications <code>iss</code>, <code>exp</code>, <code>aud</code>, <code>sub</code>, <code>client_id</code>, <code>iat</code> et <code>jti</code> <strong><sup>[72]</sup></strong>. Alice reste le sujet des deux; l’<code>act</code> externe désigne l’acteur courant, l’agent d’analyse des dépenses, et l’<code>act</code> imbriqué l’orchestrateur, acteur antérieur que le serveur consigne sans s’en servir pour décider (EXIG-IAM-08, EXIG-IAM-11)<strong><sup>[70]</sup></strong>. Le jeton 1 a pour audience la passerelle, et son <code>cnf</code> le lie à l’empreinte du certificat X.509-SVID de l’agent\xa0: la passerelle vérifie cette liaison sur la connexion mTLS de l’agent (EXIG-IAM-14)<strong><sup>[328]</sup></strong>. Le jeton 2, que la passerelle obtient par échange, la désigne comme client et lui est lié; l’échange n’ajoute aucun niveau d’<code>act</code>, et le serveur n’accepte que la passerelle, par mTLS. Son expiration ne dépasse pas celle du jeton 1\xa0: aucun échange ne prolonge la délégation (EXIG-IAM-08). L’audience unique, la portée réduite à <code>finance:read</code>, la portée de la tâche portée par <code>authorization_details</code> (dépenses du troisième trimestre) et la durée de vie de 900 secondes appliquent les exigences EXIG-IAM-10, EXIG-IAM-11 et EXIG-IAM-15, et le serveur de ressources applique en outre les droits d’Alice d’après <code>sub</code>. Volé, aucun des deux jetons ne sert sans la clé privée de son titulaire.</p>',
     ['22-03', '22-28', '24-03']),
    # [6.10, 6.11, 6.13, 6.14, 6.56] C.6 recalculé
    ('<pre><code>  h          : 9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d\nEn-tête\n{ "typ": "approbation+jwt", "alg": "ES256", "kid": "approbation-2026-10" }\nCharge utile\n{\n  "iss": "https://approbation.ent.ca",\n  "aud": "https://passerelle-agents.ent.ca",\n  "sub": "apb-5e19c2",\n  "iat": 1793093040,\n  "exp": 1793093940,\n  "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",\n  "task_id": "tache-7f3c2a",\n  "agent_id": "agt-achats-indirects@1.2.0",\n  "action_sha256": "9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d",\n  "authorization_details": [\n    {\n      "type": "https://ent.ca/types/action-agent",\n      "locations": ["https://passerelle-agents.ent.ca/mcp/approvisionnement"],\n      "actions": ["tools/call"],\n      "identifier": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",\n      "fournisseur_id": "SUP-004512",\n      "montant_total_cad": 12480,\n      "centre_cout": "CC-4410"\n    }\n  ]\n}</code></pre>',
     '<pre><code>Objet haché (canonisé selon la RFC 8785, présenté coupé)\n  outil      : mcp-approvisionnement/approvisionnement_creer_bon_commande\n  version    : 1.4.0\n  definition : sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6\n  agent_id   : agt-achats-indirects@1.2.0\n  task_id    : tache-7f3c2a\n  arguments  : {"centre_cout":"CC-4410","fournisseur_id":"SUP-004512",\n                "idempotency_key":"80351869ca990c86c8c6a314a7ac23d80b509a03f9a11dd173d2f1112c10eca7",\n                "lignes":[{"prix_unitaire_cents":24960,"quantite":40,"sku":"PRD-10442"},\n                          {"prix_unitaire_cents":20800,"quantite":12,"sku":"PRD-20817"}],\n                "statut_demande":"soumis"}\n  h          : 92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81\n  grandeur   : 1248000 cents, somme des lignes calculée par la passerelle (seuil de la tâche : 500000)\nEn-tête\n{ "typ": "approbation+jwt", "alg": "ES256", "kid": "approbation-2026-10" }\nCharge utile\n{\n  "iss": "https://approbation.ent.ca",\n  "aud": "https://passerelle-agents.ent.ca",\n  "sub": "apb-5e19c2",\n  "approbateur_role": "tiers",\n  "iat": 1793093040,\n  "exp": 1793093940,\n  "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",\n  "task_id": "tache-7f3c2a",\n  "agent_id": "agt-achats-indirects@1.2.0",\n  "action_sha256": "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81",\n  "authorization_details": [\n    {\n      "type": "https://ent.ca/types/action-agent",\n      "locations": ["https://passerelle-agents.ent.ca/mcp/approvisionnement"],\n      "actions": ["tools/call"],\n      "identifier": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",\n      "fournisseur_id": "SUP-004512",\n      "centre_cout": "CC-4410",\n      "statut_demande": "soumis",\n      "lignes": [{ "sku": "PRD-10442", "quantite": 40, "prix_unitaire_cents": 24960 },\n                 { "sku": "PRD-20817", "quantite": 12, "prix_unitaire_cents": 20800 }],\n      "grandeur_seuil": { "valeur": 1248000, "unite": "cents_cad", "portee": "task" }\n    }\n  ]\n}</code></pre>',
     ['23-03', '23-04', '23-06', '23-07', '23-15', '22-01', 'A-11']),
    # bloc « Action soumise » de C.6 égaré sous C.7 (constat de relecture)
    ('<h3>C.7 Enveloppe budgétaire de tâche</h3>\n<pre><code>Action soumise\n  outil      : mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0\n  arguments  : {"centre_cout":"CC-4410","fournisseur_id":"SUP-004512",\n                "idempotency_key":"ce887a26e391ba96cd8c85603dd7b97beb97abffe5db0e610f2b6a8bca237edf",\n                "lignes":[{"prix_unitaire_cad":249.6,"quantite":40,"sku":"PRD-10442"},\n                          {"prix_unitaire_cad":208,"quantite":12,"sku":"PRD-20817"}],\n                "montant_total_cad":12480,"statut_demande":"soumis"}</code></pre>\n',
     '<h3>C.7 Enveloppe budgétaire de tâche</h3>\n',
     ['A-11']),
    # [6.10, 6.11, 6.13, 6.14, 6.56] lecture
    ('<p>Lecture\xa0: h est le SHA-256 de l’identifiant pleinement qualifié de l’outil (serveur, nom, version épinglée), immédiatement suivi des arguments canonisés selon la RFC 8785, dont les clés sont triées et les nombres normalisés (12\xa0480,00 devient <code>12480</code>)<strong><sup>[236]</sup></strong>. Le jeton contient le minimum exigé par l’EXIG-AUT-12\xa0: l’empreinte (<code>action_sha256</code>), l’approbateur pseudonymisé (<code>sub</code>), la tâche, l’agent, une expiration à 15 minutes et un identifiant à usage unique (<code>jti</code>); <code>authorization_details</code> décrit l’action selon la RFC 9396 pour l’écran d’approbation et l’audit, sans remplacer l’empreinte<strong><sup>[312]</sup></strong>. Un <code>typ</code> distinct de <code>at+jwt</code>, choix du cadre, empêche de faire passer ce jeton pour un jeton d’accès, ou l’inverse. La passerelle vérifie la signature, l’expiration et l’usage unique, puis recalcule h sur l’appel reçu et refuse tout écart; ici, l’approbation est obtenue par CIBA sur l’appareil de l’approbateur (EXIG-AUT-14), et seul un tel jeton vaut approbation, jamais un acquiescement dans la conversation (EXIG-AUT-13)<strong><sup>[310]</sup></strong>.</p>',
     '<p>Lecture\xa0: h est le SHA-256 de la canonisation selon la RFC 8785 de l’objet {outil, version, definition_digest, agent_id, task_id, arguments}, où l’outil est désigné par son identifiant pleinement qualifié (serveur et nom) et les arguments incluent la clé d’idempotence (section 8.5)<strong><sup>[236]</sup></strong>; la canonisation trie les clés, et les montants, entiers en cents, ne laissent aucune place à une lecture divergente des nombres. La passerelle rejette tout argument non conforme à I-JSON et transmet au serveur exactement la forme hachée (EXIG-AUT-12). Le jeton contient le minimum exigé par l’EXIG-AUT-12\xa0: l’émetteur et l’audience, l’empreinte (<code>action_sha256</code>), l’approbateur sous pseudonyme stable (<code>sub</code>) et son rôle (tiers, et non le mandant), la tâche, l’agent, une expiration à 15 minutes et son identifiant (<code>jti</code>). <code>authorization_details</code> et l’écran d’approbation sont produits par la passerelle à partir des arguments canonisés, avec la grandeur calculée du seuil, jamais d’un texte de l’agent (EXIG-AUT-19); leur emploi dans un jeton d’approbation est un profil du cadre, la RFC 9396 ne définissant cette revendication que pour les jetons d’accès<strong><sup>[312]</sup></strong>. Un <code>typ</code> distinct de <code>at+jwt</code>, choix du cadre, empêche de faire passer ce jeton pour un jeton d’accès, ou l’inverse. Le jeton est remis à la passerelle, qui le conserve et ne le transmet ni à l’agent ni à son modèle; elle vérifie la signature, l’émetteur, l’audience, l’expiration, la concordance de l’agent et de la tâche avec l’appelant authentifié et le nombre d’approbateurs qu’exige le contrôle calculé, puis recalcule h sur l’appel reçu et refuse tout écart. Le jeton couvre une seule opération\xa0: un réessai de la même opération avant l’expiration est relayé, et l’ERP le déduplique par la clé. Un appel qui exige deux approbateurs (EXIG-AUT-15) reçoit deux jetons distincts sur le même h. La demande porte aussi l’empreinte de la compensation déclarée, approuvée avec l’étape (EXIG-AUT-12), que l’exemple ne montre pas. Ici, l’approbation est obtenue hors bande, par CIBA sur l’appareil de l’approbatrice (EXIG-AUT-09, EXIG-AUT-14), et seul un tel jeton vaut approbation, jamais un acquiescement dans la conversation (EXIG-AUT-13)<strong><sup>[310]</sup></strong>.</p>',
     ['23-03', '23-04', '23-06', '23-07', '23-15', '24-08']),
    # A-34
    ('"notified": "proprietaire"',
     '"notified": "parrain"',
     ['A-34']),
    # [6.36]
    ('Lecture\xa0: l’enveloppe reprend les plafonds de la fiche d’agent (annexe B)\xa0:',
     'Lecture\xa0: l’enveloppe reprend des plafonds de même valeur que la fiche type de l’annexe B, qui décrit un autre agent\xa0:',
     ['22-14', '23-14']),
    # A-06
    ('le seuil d’alerte de 80\xa0% a déjà prévenu le propriétaire, et l’atteinte d’un plafond arrêtera la tâche en état sûr pour l’escalader, sans jamais la déclarer réussie (EXIG-FIN-04).',
     'le seuil d’alerte de 80\xa0% a déjà prévenu le parrain, et l’atteinte d’un plafond arrêtera la tâche vers l’avant, en état sûr, pour l’escalader, sans jamais la déclarer réussie (EXIG-FIN-04). Les compensations des étapes déjà exécutées restent possibles\xa0: elles s’exécutent sous l’identité de compensation de l’orchestrateur, sur une réserve de budget tenue hors de cette enveloppe (EXIG-ORC-31).',
     ['A-06', 'A-34']),
    # [6.09]
    ('<p>L’exemple montre l’enregistrement que la passerelle verse au journal d’audit après l’exécution de l’action approuvée en C.6 (section 10.3).</p>',
     '<p>L’exemple montre l’enregistrement d’issue que la passerelle verse au journal d’audit après l’exécution de l’action approuvée en C.6; un enregistrement d’intention, chaîné dans le même flux, l’a précédé avant le relais de l’appel (section 10.3).</p>',
     ['23-02', '24-14']),
    # [6.09, 6.11-6.14, 6.54, 6.55] C.8
    ('<pre><code>{\n  "empreinte": "sha256:689f1e007503a391dd58d4bdc148cbccde6c2c5a5f1578472244307110180588",\n  "enregistrement": {\n    "action": {\n      "arguments_sha256": "cff55d8aafbb562bfb6b27ca6cec7cf38a1dfe3ee48b2410dcf1f3a04a5bdc2b",\n      "definition": "1.4.0",\n      "issue": "succes",\n      "outil": "mcp-approvisionnement/approvisionnement_creer_bon_commande",\n      "palier": "P2",\n      "reference_resultat": "BC-2026-118734"\n    },\n    "agent": {\n      "id": "agt-achats-indirects",\n      "identite": "spiffe://ent.ca/agt-achats-indirects",\n      "invite_systeme": "sha256:41d07c…",\n      "version": "1.2.0"\n    },\n    "autorite": {\n      "approbateur": "apb-5e19c2",\n      "approbation_jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",\n      "classe_risque": "moderee",\n      "controle": "approbation_requise_au_dela_du_seuil",\n      "empreinte_approbation": "9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d",\n      "niveau_autonomie": "N3",\n      "version_politique": "politiques-passerelle@2026.10.3"\n    },\n    "correlation": {\n      "cle_idempotence": "ce887a26e391ba96cd8c85603dd7b97beb97abffe5db0e610f2b6a8bca237edf",\n      "etape": "etape-03/creer-bon-commande",\n      "span_id": "b7ad6b7169203331",\n      "tache": "tache-7f3c2a",\n      "trace_id": "0af7651916cd43dd8448eb211c80319c"\n    },\n    "horodatage": "2026-10-27T09:26:03.412Z",\n    "mandant": {\n      "jeton_delegue_jti": "4e8b2c71-0d93-4a6f-9b15-7c2e8f40a6d3",\n      "pseudonyme": "u-58c1d7",\n      "type": "user"\n    },\n    "modele": {\n      "fournisseur": "…",\n      "servi": "modele-raisonnement",\n      "version": "2026-08-14"\n    },\n    "precedent_sha256": "sha256:ee710bdb80fd80be1bce7ad8f07964c8a0dea08c5fb81f39289b26666ab4524a",\n    "sequence": 48213\n  },\n  "signature": { "alg": "ES256", "kid": "journal-audit-2026-10", "valeur": "…" }\n}</code></pre>',
     '<pre><code>{\n  "empreinte": "sha256:689f1e007503a391dd58d4bdc148cbccde6c2c5a5f1578472244307110180588",\n  "enregistrement": {\n    "action": {\n      "arguments_sha256": "c808b36a44b197cd96fe679fd662241bf32c459f4480bbc67e5693d20ad3259f",\n      "definition": "1.4.0",\n      "definition_sha256": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",\n      "issue": "succes",\n      "outil": "mcp-approvisionnement/approvisionnement_creer_bon_commande",\n      "palier": "P2",\n      "reference_resultat": "BC-2026-118734"\n    },\n    "agent": {\n      "id": "agt-achats-indirects",\n      "identite": "spiffe://ent.ca/agt-achats-indirects",\n      "invite_systeme": "sha256:41d07c…",\n      "version": "1.2.0"\n    },\n    "autorite": {\n      "approbations": [\n        { "approbateur": "apb-5e19c2", "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28", "role": "tiers" }\n      ],\n      "classe_risque": "moderee",\n      "controle": "approbation_requise_au_dela_du_seuil",\n      "empreinte_approbation": "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81",\n      "grandeur_seuil": 1248000,\n      "niveau_autonomie": "N3",\n      "version_politique": "politiques-passerelle@2026.10.3"\n    },\n    "correlation": {\n      "cle_idempotence": "80351869ca990c86c8c6a314a7ac23d80b509a03f9a11dd173d2f1112c10eca7",\n      "etape": "etape-03/creer-bon-commande#1",\n      "span_id": "b7ad6b7169203331",\n      "tache": "tache-7f3c2a",\n      "trace_id": "0af7651916cd43dd8448eb211c80319c"\n    },\n    "flux": "passerelle-agents-03",\n    "horodatage": "2026-10-27T09:26:03.412Z",\n    "intention_sequence": 48212,\n    "mandant": {\n      "jeton_delegue_jti": "4e8b2c71-0d93-4a6f-9b15-7c2e8f40a6d3",\n      "pseudonyme": "u-58c1d7",\n      "type": "user"\n    },\n    "modele": {\n      "fournisseur": "…",\n      "servi": "modele-compact",\n      "version": "2026-08-14"\n    },\n    "nature": "issue",\n    "precedent_sha256": "sha256:ee710bdb80fd80be1bce7ad8f07964c8a0dea08c5fb81f39289b26666ab4524a",\n    "sequence": 48213\n  },\n  "signature": { "alg": "ES256", "kid": "journal-audit-2026-10", "valeur": "…" }\n}</code></pre>',
     ['23-02', '23-04', '23-05', '23-06', '23-07', '23-08', '23-12']),
    # [6.09, 6.11, 6.12, 6.13, 6.55, 6.21] lecture; recommandation OWASP non vérifiée retirée (lit. 61)
    ('<p>Lecture\xa0: <code>enregistrement</code> reprend les cinq éléments exigés par l’EXIG-OBS-12 (section 10.3)\xa0: le mandant sous pseudonyme (<code>mandant</code>), l’agent avec sa version, son identité et l’empreinte de son invite système (<code>agent</code>), l’action avec l’outil, la version de sa définition, l’empreinte des arguments et l’issue (<code>action</code>), le modèle servi (<code>modele</code>) et l’autorité qui permettait d’agir (<code>autorite</code>\xa0: politique appliquée, contrôle, niveau d’autonomie et jeton d’approbation, selon les EXIG-IAM-21 et EXIG-AUT-10); <code>correlation</code> le relie à la tâche, à l’étape, à la clé d’idempotence et à la trace. Il ne recopie pas les arguments, et le résultat n’y figure que par sa référence\xa0: <code>empreinte_approbation</code> reprend l’empreinte h du jeton C.6, calculée sur l’identifiant qualifié de l’outil (serveur, nom, version épinglée) et sur les arguments canonisés; la passerelle l’a recalculée avant l’exécution, ce qui prouve que l’action exécutée est bien celle qui a été approuvée. <code>empreinte</code> est le SHA-256 de <code>enregistrement</code> canonisé selon la RFC 8785, signé par le service d’audit, et <code>precedent_sha256</code> chaîne chaque enregistrement au précédent, de sorte qu’une suppression ou une modification se détecte, conformément à la recommandation de l’OWASP de tenir des journaux d’audit immuables et signés<strong><sup>[28, 236]</sup></strong>. Ce format et sa signature, choix du cadre, vont au-delà du minimum légal\xa0: pour un système à haut risque (obligations applicables à compter du 2 décembre 2027 pour l’annexe III et du 2 août 2028 pour l’annexe I), le RIA exige que le système permette l’enregistrement automatique des événements, sans en fixer le format (art. 12), et que le déployeur conserve les journaux, dans la mesure où ils sont sous son contrôle, pendant une durée adaptée à la destination du système et d’au moins six mois, sauf disposition contraire du droit de l’Union ou du droit national (art. 26, par. 6)<strong><sup>[94, 394]</sup></strong>.</p>',
     '<p>Lecture\xa0: <code>enregistrement</code> reprend les cinq éléments exigés par l’EXIG-OBS-12 (section 10.3)\xa0: le mandant sous pseudonyme (<code>mandant</code>), l’agent avec sa version, son identité et l’empreinte de son invite système (<code>agent</code>), l’action avec l’outil, la version et l’empreinte de sa définition, l’empreinte des arguments et l’issue (<code>action</code>), le modèle servi (<code>modele</code>) et l’autorité qui permettait d’agir (<code>autorite</code>\xa0: politique appliquée, contrôle, grandeur calculée du seuil, niveau d’autonomie et liste des approbations, chacune avec son jeton et le rôle de l’approbateur, selon les EXIG-IAM-21, EXIG-AUT-10 et EXIG-AUT-15); <code>correlation</code> le relie à la tâche, à l’étape, à la clé d’idempotence et à la trace, et les champs A2A de l’extrait de la section 10.3 sont omis, faute de délégation. Avant de relayer l’appel, la passerelle a écrit l’enregistrement d’intention de séquence 48212, que celui-ci référence (<code>intention_sequence</code>); une intention sans issue est traitée comme un incident (EXIG-OBS-11, EXIG-OBS-13). L’enregistrement ne recopie pas les arguments, et le résultat n’y figure que par sa référence. <code>arguments_sha256</code> est ici une empreinte simple, qu’on peut recalculer; comme la clé d’idempotence se déduit de la tâche et de l’étape, consignées en clair, l’empreinte des arguments d’un outil à faible entropie est salée ou remplacée par un HMAC sous une clé du service d’audit (EXIG-OBS-12). <code>empreinte_approbation</code> reprend l’empreinte h du jeton C.6; la passerelle l’a recalculée avant de relayer l’appel, ce qui atteste que les octets transmis sont ceux qui ont été approuvés, et non que l’effet est celui qui était attendu. Le rôle consigné (tiers) atteste que l’approbatrice n’est pas le mandant, ce que le service d’approbation vérifie à l’émission. <code>empreinte</code> est le SHA-256 de <code>enregistrement</code> canonisé selon la RFC 8785, signé par le service d’audit, et <code>precedent_sha256</code> chaîne chaque enregistrement au précédent du même flux (<code>flux</code>, inscrit au registre des flux)\xa0: une suppression ou une modification internes se détectent, mais la troncature de la queue et la réécriture par le détenteur de la clé ne se détectent que par les points de contrôle de la tête du flux, publiés hors du domaine d’administration du service d’audit (EXIG-OBS-12)<strong><sup>[236]</sup></strong>. Ce format, sa signature et son ancrage, choix du cadre, vont au-delà du minimum légal\xa0: pour un système à haut risque (obligations applicables à compter du 2 décembre 2027 pour l’annexe III et du 2 août 2028 pour l’annexe I, selon le règlement (UE) 2026/1744<strong><sup>[57, 58]</sup></strong>), le RIA exige que le système permette l’enregistrement automatique des événements, sans en fixer le format (art. 12), et que le déployeur conserve les journaux, dans la mesure où ils sont sous son contrôle, pendant une durée adaptée à la destination du système et d’au moins six mois, sauf disposition contraire du droit de l’Union ou du droit national (art. 26, par. 6)<strong><sup>[61, 447]</sup></strong>.</p>',
     ['23-02', '23-04', '23-05', '23-06', '23-12', '26-02', '27-03', '28-35']),
    # [6.61]
    ('toutes les exigences normatives du cadre avec leur force (DOIT, DEVRAIT, PEUT).',
     'toutes les exigences normatives du cadre avec la force de leur bloc (DOIT, NE DOIT PAS, DEVRAIT). Les principes PRIN-01 à PRIN-12 et les tableaux auxquels une exigence renvoie expressément sont aussi normatifs (section 1.4), mais ne figurent pas au registre.',
     ['23-20']),
    # [6.63, 6.16]
    ('Tout contenu qui ne provient ni du mandant authentifié ni de la configuration approuvée de l’agent\xa0: pages Web, courriels, documents téléversés, champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, messages et cartes d’autres agents. Il est traité comme une donnée, jamais comme une instruction; sa lecture entraîne le retrait des outils d’envoi externe et des outils P3 pour le reste de la session. Voir la section 9.6.',
     'Tout contenu autre que la demande saisie par le mandant authentifié et la configuration approuvée de l’agent\xa0: pages Web, courriels, documents et pièces jointes, même téléversés par le mandant, champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, index de récupération, événements, messages, tâches et cartes d’autres agents. Toute source de contexte non inscrite au catalogue avec son étiquette de fiabilité est non fiable (EXIG-SEC-03). Il est traité comme une donnée, jamais comme une instruction. Sa consommation, repérée par le marquage du catalogue, marque la session, et l’étiquette suit toute donnée qui en dérive; elle entraîne, pour le reste de la session, le retrait des outils d’envoi (y compris la requête en texte libre d’un outil de recherche publique) et des outils P3, et la règle de deux s’applique à toute écriture P2 (EXIG-SEC-04, EXIG-SEC-06). Une action retirée ne s’exécute qu’avec une approbation liée à l’action exacte. Voir la section 9.6.',
     ['24-01', '24-05', '24-02', 'A-17']),
    # [6.63]
    ('La «\xa0règle de deux\xa0» de Meta en tire une règle de session\xa0: au plus deux des trois propriétés sans supervision<strong><sup>[307]</sup></strong>. Voir la section 9.6.',
     'La «\xa0règle de deux\xa0» de Meta en tire une règle de session\xa0: sans supervision, au plus deux de trois propriétés, soit [A] traiter des entrées non fiables, [B] accéder à des systèmes sensibles ou à des données privées, [C] modifier un état ou communiquer vers l’extérieur<strong><sup>[307]</sup></strong>. Le cadre l’évalue sur la session composée, à travers délégations, mémoire et événements, et la passerelle l’applique à l’exécution (EXIG-SEC-04). Voir la section 9.6.',
     ['24-01', '24-05', 'A-17']),
    # [6.17, 6.51]
    ('Sa portée ne dépasse jamais les droits effectifs, soit droits du mandant ∩ portée de l’agent ∩ portée de la tâche (choix du cadre), intersection appliquée par le serveur d’autorisation à chaque échange. Voir la section 9.3 et l’annexe C.',
     'Sa portée ne dépasse jamais les droits effectifs, soit droits du mandant ∩ portée de l’agent ∩ portée de la tâche (choix du cadre)\xa0: le serveur d’autorisation borne la portée à chaque échange, la portée de la tâche figurant dans <code>authorization_details</code>, et le serveur de ressources applique à chaque appel les droits du mandant d’après <code>sub</code>. Son expiration ne dépasse jamais celle du jeton reçu, si bien qu’aucun échange ne prolonge une délégation. Il se distingue du mandat d’un agent ambiant. Voir la section 9.3 et l’annexe C.',
     ['24-03', '22-28', 'A-16']),
    # [6.69]
    ('Personne, application ou agent au nom duquel une tâche est exécutée; pour un déclencheur système, identité du service et de son propriétaire nommé.',
     'Personne ou application au nom de laquelle une tâche est exécutée; pour un déclencheur système, identité du service et de son responsable nommé. Le mandant d’une chaîne est toujours l’entité d’origine\xa0: un agent intermédiaire n’y apparaît que comme acteur (<code>act</code>).',
     ['24-13', 'A-34']),
    # [6.70, 6.09]
    ('Mandataire inverse placé devant tous les serveurs MCP et tous les pairs A2A, pour le trafic entrant comme sortant, qui sert de point d’application des politiques. À chaque appel, elle authentifie l’agent et le mandant, vérifie le catalogue, autorise, applique les garde-fous, vérifie l’approbation, limite le budget, injecte les justificatifs en aval, filtre la sortie, puis trace et journalise.',
     'Mandataire placé sur tout le trafic MCP et A2A et sur toute action P2 ou P3, quel que soit le domaine (EXIG-ARC-01), inverse en entrée et de sortie en sortie, qui sert de point d’application des politiques; ses instances, y compris au plus près de l’agent <em>(sidecar)</em>, partagent la politique, le registre des <code>jti</code> et le journal d’audit. À chaque appel, elle authentifie l’agent et le mandant, vérifie le catalogue, autorise, applique les garde-fous, vérifie l’approbation, limite le budget, injecte les justificatifs en aval et filtre la sortie; elle trace l’appel et, pour un appel P2 ou P3, journalise l’intention avant de le relayer et l’issue ensuite.',
     ['24-14', 'A-01', 'A-19']),
    # [6.56]
    ('et pour lier une approbation à l’action exacte\xa0: h = SHA-256(identifiant de l’outil ‖ arguments canonisés). Voir les sections 6.8 et 8.5.',
     'et pour lier une approbation à l’action exacte\xa0: h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments})), où l’outil est désigné par son identifiant pleinement qualifié (serveur et nom). h atteste que les octets transmis sont ceux qui ont été approuvés, non que l’effet est celui qui était attendu. Voir les sections 6.8 et 8.5.',
     ['23-15', '24-08', 'A-11']),
    # [6.65]
    ('qui comprend les systèmes à haut risque du RIA et les décisions visées par l’article 12.1 de la Loi sur le privé;',
     'qui comprend les systèmes à haut risque du RIA et les décisions visées par l’article 12.1 de la Loi sur le privé ou par l’article 65.2 de la Loi sur l’accès;',
     ['24-06']),
    # A-24 : source unique des plafonds
    ('N4 pour la classe faible, sur décision du comité. Voir les sections 8.1 et 12.1.',
     'N4 pour la classe faible, sur décision du comité (EXIG-CON-02). Voir les sections 8.1 et 12.1.',
     ['A-24']),
    # [6.66]
    ('Le cadre exige qu’elle soit déclarée au catalogue, idempotente, journalisée avant l’action qu’elle couvre et déclenchée seulement après l’épuisement des réessais. Voir la section 7.5.',
     'Le cadre exige qu’elle soit inscrite au catalogue comme un outil, avec son palier, idempotente et journalisée avant l’action qu’elle couvre; elle est déclenchée lorsque la progression devient impossible (réessais épuisés ou erreur non transitoire) et s’exécute sous l’identité de compensation de l’orchestrateur, que les arrêts de l’agent n’atteignent pas (EXIG-ORC-31). Une étape dont l’issue est inconnue n’est compensée qu’après la clôture de l’opération chez le système visé ou une issue définitive (EXIG-ORC-16). Voir la section 7.5.',
     ['24-07', 'A-06', 'A-07', 'A-08']),
    # [6.67]
    ('Plafond déclaré au registre, de N0 à N4, qui fixe le rôle de la personne et ce que l’agent peut faire sans approbation\xa0: N0 automatisation déterministe, sans modèle; N1 consultatif, sans écriture; N2 exécution approuvée (HITL); N3 autonomie bornée et supervisée (HOTL); N4 autonomie étendue sous ODD certifié.',
     'Niveau déclaré au registre, de N1 à N4, borné par le plafond de la classe de risque (EXIG-CON-02), qui fixe le rôle de la personne et ce que l’agent peut faire sans approbation\xa0: N1 consultatif, sans écriture; N2 exécution approuvée (HITL); N3 autonomie bornée et supervisée (HOTL); N4 autonomie étendue sous ODD certifié, qui couvre les tâches déclenchées sans demande d’une personne (événement, horaire), origine que la passerelle lit pour appliquer le niveau inscrit. N0 qualifie un flux déterministe, où aucun choix d’action n’est laissé à un modèle\xa0: c’est un repère hors de la portée agentique, non un niveau d’agent.',
     ['24-11', 'A-27']),
    # [6.71]
    ('en trois paliers\xa0: tests de contrats,',
     'en trois étages (E1 à E3)\xa0: tests de contrats,',
     ['24-15', 'A-27']),
    # A-24
    ('Elle est relancée à chaque changement de modèle, d’invite système ou d’outil, et ses résultats conditionnent l’homologation.',
     'Elle est relancée à chaque changement visé par l’EXIG-GOV-12, et ses résultats conditionnent l’homologation.',
     ['A-24']),
    # [6.72]
    ('et avant toute communication de RP hors du Québec, autres provinces comprises (art. 17)<strong><sup>[160]</sup></strong>.',
     'et avant toute communication de RP hors du Québec, autres provinces comprises (art. 17)<strong><sup>[160]</sup></strong>; pour un organisme public, l’article 63.5 de la Loi sur l’accès prévoit l’évaluation des projets de système d’information.',
     ['24-16']),
    # [6.72]
    ('Selon l’interprétation gouvernementale de l’article 65.2 (organismes publics), une intervention humaine mineure ne retire pas ce caractère;',
     'Selon l’interprétation gouvernementale de l’article 65.2 (organismes publics), une intervention humaine mineure ne retire pas ce caractère<strong><sup>[318]</sup></strong>;',
     ['24-16']),
    # [6.73]
    ('Le cadre exige, pour toute écriture P2 ou P3, une clé d’idempotence dérivée des identifiants de la tâche et de l’étape, réutilisée à chaque réessai et vérifiée par le service visé;',
     'Le cadre exige, pour toute écriture P2 ou P3, une clé d’idempotence dérivée de l’identifiant de la tâche racine et de celui de l’étape, réutilisée à chaque réessai et vérifiée par le système qui produit l’effet, ou par un adaptateur doté d’un registre de clés durable (EXIG-ORC-22); le service rejette une clé déjà vue avec des arguments différents, une étape replanifiée reçoit un nouvel identifiant, et la conservation des clés couvre toute la fenêtre de rejeu;',
     ['24-17', 'A-09']),
    # [6.74] vérifié contre le tableau du § 9.1
    ('Dans le cadre, la passerelle d’agents et la passerelle de modèles sont des PEP, et le service de politiques tient le rôle de PE. Voir la section 9.1.',
     'Dans le cadre, la passerelle d’agents et la passerelle de modèles sont des PEP, le service de politiques tient le rôle de PE, et le fournisseur d’identité et le plan de contrôle des passerelles tiennent celui de PA. Voir la section 9.1.',
     ['24-18']),
    # [6.75]
    ('Règle du cadre\xa0: une cible aux entrées et aux sorties définies est un outil, même si elle emploie un modèle en interne.',
     'Règle du cadre\xa0: une cible est un agent si elle choisit elle-même, au moyen d’un modèle, les actions qu’elle exécute; sinon c’est un outil, même si elle emploie un modèle en interne, conserve l’état d’une tâche ou demande une précision (Tasks, élicitation MCP).',
     ['24-19', 'A-20']),
    # [6.58]
    ('avec leur version de référence et l’un de quatre statuts\xa0: Adopter (usage par défaut), Évaluer (pilotes encadrés), Surveiller (veille, hors production) ou Contenir (existant toléré derrière un adaptateur, sans nouvel usage). Le comité le révise au moins chaque trimestre.',
     'avec leur version de référence et l’un de cinq statuts\xa0: Adopter (usage par défaut, seul statut admis pour un nouvel usage en production), Évaluer (pilotes encadrés), Surveiller (veille, hors production), Contenir (existant toléré derrière un adaptateur jusqu’à l’échéance de son plan de sortie, sans nouvel usage) ou Suspendu (service arrêté par la passerelle pour un motif de sécurité). L’architecture d’entreprise le révise au moins chaque trimestre et soumet la révision à l’approbation du comité (EXIG-GOV-18).',
     ['23-17', '24-10', '28-27', 'A-21', 'A-22']),
    # [6.68]
    ('Aucune dérogation n’est possible pour le niveau NX, une action P3 sans approbation humaine, l’usurpation d’identité, un agent sans fiche ni parrain, le dépassement du plafond d’autonomie ou une obligation légale.',
     'Aucune dérogation n’est possible sur les points de l’EXIG-GOV-17, qui en tient la liste, notamment le niveau NX, une action P3 sans approbation humaine hors bande, l’usurpation d’identité, un agent sans fiche au registre ou sans parrain nommé, le dépassement du plafond d’autonomie, la réunion des trois propriétés de la triade létale, l’absence de journal d’audit et toute obligation légale.',
     ['24-12', 'A-24']),
    # [6.87]; N4 (A-27, t1)
    ('(définition de LangChain)<strong><sup>[86]</sup></strong>.',
     '(définition du cadre, inspirée de LangChain)<strong><sup>[86]</sup></strong>. Un agent ambiant qui exécute seul des écritures relève du niveau N4 (section 8.1).',
     ['26-05', 'A-27']),
    # A-05
    ('Son délai de bout en bout est mesuré lors d’un exercice au moins trimestriel (choix du cadre). Voir les sections 7.8 et 9.4.',
     'Il arrête l’agent vers l’avant et ne vise pas le canal de compensation (EXIG-ORC-31). Son délai de bout en bout, de la décision d’arrêt au refus du dernier appel dans tous les systèmes, a une cible fixée par l’entreprise (EXIG-IAM-20) et se mesure lors de l’exercice trimestriel de l’EXIG-SEC-26 (choix du cadre). Voir les sections 7.8 et 9.4.',
     ['A-05', 'A-06']),
    # A-04, A-06
    ('La passerelle d’agents n’ouvre jamais le passage par défaut, et l’orchestrateur suspend la tâche dans un état reprenable. Voir les sections 8.4 et 9.4.',
     'La passerelle d’agents n’ouvre jamais le passage par défaut, et l’orchestrateur suspend la tâche dans un état reprenable. L’échec se fait vers l’avant\xa0: les compensations des étapes exécutées passent par le canal de compensation (EXIG-ORC-31), et une politique en cache vaut décision valide tant qu’elle n’est pas échue (EXIG-IAM-22). Voir les sections 8.4 et 9.4.',
     ['A-04', 'A-06']),
    # A-19
    ('Enregistrement inaltérable et signé, distinct des traces,',
     'Enregistrement chaîné, signé et ancré hors du domaine d’administration du service d’audit, distinct des traces,',
     ['A-19']),
    # A-10, A-12, A-15
    ('qui contient au minimum l’empreinte de l’action approuvée, l’identifiant pseudonymisé de l’approbateur, les identifiants de la tâche et de l’agent, une date d’expiration et un identifiant à usage unique. La passerelle recalcule l’empreinte avant l’exécution; le cadre en limite la validité à 15\xa0minutes.',
     'qui contient au minimum l’émetteur, l’audience, l’empreinte de l’action approuvée, le pseudonyme de l’approbateur et son rôle (mandant ou tiers), les identifiants de la tâche et de l’agent, une date d’expiration et un identifiant de jeton. Il est remis à la passerelle, qui le conserve hors du contexte du modèle, et couvre une seule opération, réessais compris; une double approbation se fait par deux jetons sur la même empreinte. La passerelle recalcule l’empreinte avant l’exécution; le cadre en limite la validité à 15\xa0minutes.',
     ['A-10', 'A-12', 'A-15']),
    # A-27
    ('C’est le patron par défaut du cadre. Voir les sections 3.2 et 7.2.',
     'C’est le patron par défaut du cadre. Un flux sans choix d’action laissé à un modèle relève de N0; un flux assisté par IA est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle. Voir les sections 3.2 et 7.2.',
     ['A-27']),
    # A-20
    ('sous un niveau d’autonomie déclaré<strong><sup>[84]</sup></strong>.',
     'sous un niveau d’autonomie déclaré<strong><sup>[84]</sup></strong>; il choisit lui-même, au moyen d’un modèle, les actions qu’il exécute, ce qui le distingue d’un outil.',
     ['A-20']),
    # A-27
    ('P2 écriture réversible ou compensable, avec approbation au-delà d’un seuil; P3 action critique, externe ou irréversible, jamais exécutée seule par un agent.',
     'P2 écriture réversible, ou compensable vers un état métier équivalent avec un impact borné, avec approbation au-delà d’un seuil; P3 action critique, externe ou irréversible, même si une compensation est déclarée, jamais exécutée seule par un agent.',
     ['A-27']),
    # A-27
    ('(2) Porte du cycle de vie d’un agent, de la proposition au retrait, dont le franchissement est consigné au registre avec ses preuves.',
     '(2) Jalon du cycle de vie d’un agent, de la proposition au retrait, dont le franchissement est consigné au registre avec ses preuves; pour éviter l’homonymie, le cadre dit «\xa0jalon\xa0» en ce sens.',
     ['A-27']),
    # A-34
    ('sa compensation et son propriétaire.',
     'sa compensation et son responsable.',
     ['A-34']),
    # A-12
    ('Dans le cadre, elle prend la forme d’un jeton d’approbation signé, lié à l’action exacte et vérifié par la passerelle d’agents.',
     'Dans le cadre, elle prend la forme d’un jeton d’approbation signé, lié à l’action exacte et vérifié par la passerelle d’agents; pour un appel P3, elle est hors bande.',
     ['A-12']),
    # nouvelle entrée, alignée sur le tableau 7 (t1)
    ('<tr><td><strong>Équipe rouge</strong>',
     '<tr><td><strong>Environnement serveur</strong></td><td><em>server environment</em></td><td>Tout environnement d’exécution autre qu’un poste de développement individuel sans justificatif de production\xa0: développement partagé, préproduction et production, mais aussi poste de travail, navigateur, mobile ou périphérie dès qu’un agent y agit sur des systèmes ou des données de l’entreprise. Le passage par la passerelle y est obligatoire (EXIG-ARC-01). Voir la section 3.1.</td></tr><tr><td><strong>Équipe rouge</strong>',
     ['A-01']),
    # nouvelle entrée
    ('<tr><td><strong>Humain dans la boucle</strong>',
     '<tr><td><strong>Hors bande</strong></td><td><em>out-of-band</em></td><td>Se dit d’une approbation donnée sur un appareil et dans une session distincts de ceux de l’agent, avec une authentification forte résistante à l’hameçonnage; une confirmation locale dans l’interface de l’agent ne suffit pas. Le cadre l’exige pour tout appel P3 (EXIG-AUT-09) et recommande CIBA (EXIG-AUT-14). Voir la section 8.5.</td></tr><tr><td><strong>Humain dans la boucle</strong>',
     ['A-12']),
    # nouvelle entrée
    ('<tr><td><strong>MCP</strong> (Model Context Protocol)',
     '<tr><td><strong>Mandat</strong></td><td><em>standing mandate</em></td><td>Consentement de longue durée, inscrit au serveur d’autorisation, par lequel un mandant autorise un agent ambiant à agir pour lui. Tant que le mandat est valide et le mandant actif, le serveur d’autorisation émet à la demande de l’agent des jetons d’au plus 15 minutes, dont le sujet est le mandant et l’acteur l’agent. Il se distingue du jeton délégué, de courte durée. Voir les sections 8.6 et 9.3.</td></tr><tr><td><strong>MCP</strong> (Model Context Protocol)',
     ['A-16']),
    # [6.15] nouvelle entrée
    ('<tr><td><strong>Plan transversal</strong>',
     '<tr><td><strong>Plan de contrôle</strong></td><td><em>control plane</em></td><td>Services qui distribuent aux instances de la passerelle les politiques, les entrées du catalogue et les états du registre; avec le fournisseur d’identité, il tient le rôle d’administrateur de politiques (section 9.1). Sa panne n’ouvre aucun passage\xa0: la dernière politique distribuée vaut jusqu’à son échéance, puis seuls les appels P0 passent, et la liste de suspension voyage par un canal signé qui en est indépendant (EXIG-IAM-22). Voir la section 9.4.</td></tr><tr><td><strong>Plan transversal</strong>',
     ['23-11', 'A-04']),
    # [6.15, 6.16] nouvelles entrées
    ('<tr><td><strong>SPIFFE</strong>, <strong>SPIRE</strong>',
     '<tr><td><strong>Service de politiques</strong></td><td><em>policy service</em></td><td>Composant qui évalue les politiques d’autorisation et rend la décision qu’applique la passerelle (rôle de PE au sens de la confiance zéro); il fait partie du plan de contrôle. S’il est injoignable, la dernière politique distribuée vaut service disponible tant qu’elle n’est pas échue; échue, seuls les appels P0 passent (EXIG-AUT-11, EXIG-IAM-22). Voir les sections 8.4 et 9.4.</td></tr><tr><td><strong>Session</strong></td><td><em>session</em></td><td>Au sens des EXIG-SEC-04 et EXIG-SEC-06\xa0: la tâche racine et tout ce qui en dérive (sous-tâches, délégations A2A, reprises depuis un point de contrôle, événements publiés au titre de la tâche). Son état (contenu non fiable consommé, données sensibles consultées) est tenu par la passerelle dans un magasin à cohérence forte; un état illisible impose le refus. Un contexte vierge exclut tout rechargement de mémoire, de point de contrôle ou d’artefact étiqueté postérieur à la contamination. Voir les sections 3.1 et 9.6.</td></tr><tr><td><strong>SPIFFE</strong>, <strong>SPIRE</strong>',
     ['23-11', '24-02', 'A-04', 'A-17']),
    # [6.18]
    ('Elle permet à tout lecteur de retracer l’origine d’un fait et le degré de confiance qu’on peut lui accorder.</p>',
     'Elle permet de retracer l’origine des faits de la version 1.0 et le degré de confiance qu’on peut leur accorder; ses limites sont dites en F.1 et à la légende du tableau 69.</p>',
     ['25-01', '25-02', '25-03']),
    # [6.18, 6.22] A-31
    ('Après l’intégration de ces corrections, l’annexe G compte 473 références, toutes citées dans le corps du cadre.',
     'Après l’intégration de ces corrections, l’annexe G compte 473 entrées, toutes citées dans le corps du cadre, dont 25 doublons signalés dans leur entrée («\xa0Même source que [n]\xa0»), soit 448 sources distinctes\xa0: le contrôle d’identité n’a pas fusionné les entrées doubles. Les passes ne portent pas sur la même population (121 références, puis 428 à l’audit final, puis 473 entrées à l’annexe G); l’écart de 45 entrées entre l’audit final et l’annexe G n’est pas ventilé, et le relevé lien par lien des affirmations et des sources n’est pas publié.',
     ['25-02', '25-03', '27-01', '26-03', '24-09', '25-09', '28-31']),
    # [6.20] A-31
    ('<td>Jamais cité; remplacé par une source A ou B, ou fait retiré.</td>',
     '<td>Jamais cité à l’appui d’un fait ou d’une exigence; remplacé par une source A ou B, ou fait retiré. Un argument d’éditeur peut être nommé comme tel dans le texte, sans appel d’appui; une entrée de l’annexe G de cette catégorie y est signalée.</td>',
     ['26-01', '27-02', '26-04', '27-11']),
    # [6.81]
    ('aligné sur le profil OAuth 2.1<strong><sup>[176, 209]</sup></strong>.</td>',
     'aligné sur le profil OAuth 2.1<strong><sup>[175, 176, 209]</sup></strong>.</td>',
     ['25-12']),
    # [6.81] lit. 40
    ('A2A annoncé comme projet de l’AAIF le 17 août 2026 (billet du projet du 27 août 2026)<strong><sup>[5, 29, 472]</sup></strong>.',
     'A2A annoncé comme projet de l’AAIF le 17 août 2026 (billet de la fondation), puis accepté au stade «\xa0Growth\xa0» (billet du projet du 27 août 2026)<strong><sup>[5, 29, 35, 472]</sup></strong>.',
     ['25-12']),
    # [6.82] lit. 52 et 53
    ('<td>+80,9\xa0% (Finance-Agent), −39\xa0% à −70\xa0% (PlanCraft), amplification des erreurs de 17,2× sans vérification centrale;',
     '<td>Selon le billet de Google, +80,9\xa0% (Finance-Agent), −39\xa0% à −70\xa0% (PlanCraft) et amplification des erreurs de 17,2× sans vérification centrale; la version 3 de l’article (260 configurations) donne une plage de +80,8\xa0% à −70,0\xa0%<strong><sup>[274]</sup></strong>;',
     ['25-13']),
    # [6.76] lit. 54
    ('moins de 5 Mio par microVM, démarrage sous 125 ms<strong><sup>[363]</sup></strong>.</td>',
     'moins de 5 Mo par microVM, démarrage sous 125 ms, selon l’article de 2020<strong><sup>[363]</sup></strong>; le site du projet en décrit davantage, les versions récentes ajoutant notamment vsock (section 9.7).</td>',
     ['25-04']),
    # [6.83]
    ('conservé cinq ans selon le règlement',
     'conservé au moins cinq ans selon le règlement',
     ['25-14']),
    # [6.84] lettre de l’art. 17, aligné sur le glossaire
    (', y compris, selon l’interprétation du cadre, les autres provinces',
     ', y compris les autres provinces',
     ['25-15']),
    # [6.81]
    ('les seuils deviennent des paramètres internes approuvés par le comité<strong><sup>[76, 83]</sup></strong>.',
     'les seuils deviennent des paramètres internes approuvés par le comité<strong><sup>[75, 76, 83, 95]</sup></strong>.',
     ['25-12']),
    # [6.19] A-07 : n’est plus présenté comme corrigé selon l’ancienne règle
    ('<td>Une étape à l’état incertain est traitée comme possiblement exécutée; sa compensation, idempotente, doit pouvoir s’exécuter sans risque<strong><sup>[286]</sup></strong>.</td>',
     '<td>Une étape à l’état incertain n’est ni compensée ni replanifiée à l’aveugle\xa0: l’orchestrateur clôt d’abord l’opération chez le système visé (annulation ou révocation de la clé d’idempotence, de sorte qu’une arrivée tardive soit rejetée) ou l’interroge jusqu’à une issue définitive; à défaut, l’étape passe en réconciliation différée, confiée à une personne (EXIG-ORC-16)<strong><sup>[286]</sup></strong>.</td>',
     ['25-05']),
    # [6.85]
    ('issue de CoALA, qui la reprend de l’architecture Soar<strong><sup>[100]</sup></strong>.',
     'issue de CoALA, qui s’inspire de l’architecture Soar et de la psychologie cognitive<strong><sup>[100]</sup></strong>.',
     ['25-16']),
    # [6.18, 6.78, 6.79]
    ('Décision\xa0: <em>conservée</em> = source A ou B citée là où elle appuie un fait; <em>remplacée</em> = remplacée par une source primaire; <em>retirée</em> = sans valeur probante pour le cadre.</p>',
     'Décision, à l’état de la version 1.0\xa0: <em>conservée</em> = source A ou B admissible, citée si elle figure à l’annexe G; <em>remplacée</em> = remplacée par une source primaire, plus récente ou plus spécifique; <em>retirée</em> = sans valeur probante pour le cadre ou hors sujet. Le registre ne renvoie pas aux numéros de l’annexe G, et cinq sources remplacées ou retirées y ont été réintroduites à l’audit final (lignes 7, 16, 36, 41 et 52). Le symbole ✗ réunit les affirmations non appuyées et contredites, que le tableau 67 distingue. Pour une page bloquée ou payante, la catégorie repose sur l’éditeur, et le verdict sur le résumé public.</p>',
     ['25-01', '25-07', '25-08']),
    # [6.18] tableau 69, ligne 7
    ('<tr><td>7</td><td>Governing AI Agents Across Multiple Platforms TrueFoundry</td><td><strong>B</strong></td><td>accessible</td><td>✓2 ◐8 ✗3</td><td>remplacée</td></tr>',
     '<tr><td>7</td><td>Governing AI Agents Across Multiple Platforms TrueFoundry</td><td><strong>B</strong></td><td>accessible</td><td>✓2 ◐8 ✗3</td><td>remplacée; réintroduite à l’audit final ([44])</td></tr>',
     ['25-01']),
    # [6.18] tableau 69, ligne 16
    ('<tr><td>16</td><td>[Project Proposal] AGNTCY #57 (dépôt aaif/project-proposals) GitHub</td><td><strong>A</strong></td><td>accessible</td><td>✓5 ◐6</td><td>remplacée</td></tr>',
     '<tr><td>16</td><td>[Project Proposal] AGNTCY #57 (dépôt aaif/project-proposals) GitHub</td><td><strong>A</strong></td><td>accessible</td><td>✓5 ◐6</td><td>remplacée; réintroduite à l’audit final ([37])</td></tr>',
     ['25-01']),
    # [6.18] tableau 69, ligne 36
    ('<tr><td>36</td><td>Implement 3 Layers of Oversight for Scaled Agentic AI Architectures (titre non vérifié) Gartner</td><td><strong>A</strong></td><td>bloquée</td><td>?1</td><td>retirée</td></tr>',
     '<tr><td>36</td><td>Implement 3 Layers of Oversight for Scaled Agentic AI Architectures (titre non vérifié) Gartner</td><td><strong>A</strong></td><td>bloquée</td><td>?1</td><td>retirée; réintroduite à l’audit final ([52])</td></tr>',
     ['25-01']),
    # [6.18] tableau 69, ligne 41
    ('<tr><td>41</td><td>Levels of Autonomy for AI Agents arXiv</td><td><strong>A</strong></td><td>bloquée</td><td>✓1</td><td>remplacée</td></tr>',
     '<tr><td>41</td><td>Levels of Autonomy for AI Agents arXiv</td><td><strong>A</strong></td><td>bloquée</td><td>✓1</td><td>remplacée; réintroduite à l’audit final ([83])</td></tr>',
     ['25-01']),
    # [6.18] tableau 69, ligne 52
    ('<tr><td>52</td><td>TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems arXiv</td><td><strong>A</strong></td><td>accessible</td><td>◐1</td><td>remplacée</td></tr>',
     '<tr><td>52</td><td>TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems arXiv</td><td><strong>A</strong></td><td>accessible</td><td>◐1</td><td>remplacée; réintroduite à l’audit final ([454])</td></tr>',
     ['25-01']),
    # [6.77, 6.22, 6.20]
    ('Toutes sont de catégorie A (primaires ou officielles) ou B (secondaires reconnues) et ont été consultées ou vérifiées au 27 octobre 2026.',
     'Elles relèvent en principe des catégories A (primaires ou officielles) ou B (secondaires reconnues) du tableau 66; une entrée qui ne l’est pas y est signalée. État des sources au 27 octobre 2026; vérifications des 27 et 28 octobre 2026. La liste compte 473 entrées, dont 25 doublons signalés («\xa0Même source que [n]\xa0»); les numéros ne sont jamais réattribués.',
     ['25-06', '27-01', '26-01', '26-03']),
    # [11] [6.80]
    (' <a href="https://www.silicon.co.uk/press-release/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security"><code>https://www.silicon.co.uk/press-release/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security</code></a></li>',
     ' Reproduction de presse du communiqué; le rapport d’origine n’a pas été relu. <a href="https://www.silicon.co.uk/press-release/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security"><code>https://www.silicon.co.uk/press-release/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security</code></a></li>',
     ['25-11']),
    # [44] [6.20]
    (' <a href="https://www.truefoundry.com/blog/cross-platform-ai-agent-governance"><code>https://www.truefoundry.com/blog/cross-platform-ai-agent-governance</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://www.truefoundry.com/blog/cross-platform-ai-agent-governance"><code>https://www.truefoundry.com/blog/cross-platform-ai-agent-governance</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [45] [6.20]
    (' <a href="https://blogs.mulesoft.com/agentic-perspectives/a-framework-for-architecting-agent-control-plane"><code>https://blogs.mulesoft.com/agentic-perspectives/a-framework-for-architecting-agent-control-plane</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://blogs.mulesoft.com/agentic-perspectives/a-framework-for-architecting-agent-control-plane"><code>https://blogs.mulesoft.com/agentic-perspectives/a-framework-for-architecting-agent-control-plane</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [58] lit. 22
    (' <a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj"><code>https://eur-lex.europa.eu/eli/reg/2026/1744/oj</code></a></li>',
     ' Texte non relu au Journal officiel lors de la revue du 3 novembre 2026 (EUR-Lex inaccessible); les dates d’application sont citées d’après [57]. <a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj"><code>https://eur-lex.europa.eu/eli/reg/2026/1744/oj</code></a></li>',
     ['A-31']),
    # [62] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/3"><code>https://artificialintelligenceact.eu/article/3</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/3"><code>https://artificialintelligenceact.eu/article/3</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [65] [6.22] doublon
    (' <a href="https://www.anthropic.com/research/building-effective-agents"><code>https://www.anthropic.com/research/building-effective-agents</code></a></li>',
     ' Même source que [6]. <a href="https://www.anthropic.com/research/building-effective-agents"><code>https://www.anthropic.com/research/building-effective-agents</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [68] [6.90]
    (' <a href="https://a2a-protocol.org/latest/specification"><code>https://a2a-protocol.org/latest/specification</code></a></li>',
     ' Adresse « latest », qui suit la dernière version publiée; page consultée le 27 octobre 2026. <a href="https://a2a-protocol.org/latest/specification"><code>https://a2a-protocol.org/latest/specification</code></a></li>',
     ['26-08', '27-07', '27-10']),
    # [70] [6.22] doublon
    (' <a href="https://www.rfc-editor.org/rfc/rfc8693.html"><code>https://www.rfc-editor.org/rfc/rfc8693.html</code></a></li>',
     ' Même source que [69]. <a href="https://www.rfc-editor.org/rfc/rfc8693.html"><code>https://www.rfc-editor.org/rfc/rfc8693.html</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [76] lit. 78
    (' <a href="https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf"><code>https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf</code></a></li>',
     ' Version 1.5 publiée le 20 mai 2026. <a href="https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf"><code>https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf</code></a></li>',
     ['A-31']),
    # [87] lit. 60
    (' <a href="https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations"><code>https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations</code></a></li>',
     ' La page pointée présente la version 1.0 du 17 février 2025; la version 1.1 reste à vérifier dans le document. <a href="https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations"><code>https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations</code></a></li>',
     ['A-31']),
    # [93] lit. 62
    (' <a href="https://www.ietf.org/archive/id/draft-ietf-wimse-aims-00.html"><code>https://www.ietf.org/archive/id/draft-ietf-wimse-aims-00.html</code></a></li>',
     ' Révision −01 publiée le 2 novembre 2026; le contenu cité est celui de la −00. <a href="https://www.ietf.org/archive/id/draft-ietf-wimse-aims-00.html"><code>https://www.ietf.org/archive/id/draft-ietf-wimse-aims-00.html</code></a></li>',
     ['A-31']),
    # [94] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/26"><code>https://artificialintelligenceact.eu/article/26</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/26"><code>https://artificialintelligenceact.eu/article/26</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [99] [6.22] doublon
    (' <a href="https://doi.org/10.6028/NIST.AI.100-1"><code>https://doi.org/10.6028/NIST.AI.100-1</code></a></li>',
     ' Même source que [74]. <a href="https://doi.org/10.6028/NIST.AI.100-1"><code>https://doi.org/10.6028/NIST.AI.100-1</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [101] lit. 46
    (' <a href="https://arxiv.org/abs/2503.18813"><code>https://arxiv.org/abs/2503.18813</code></a></li>',
     ' Chiffres cités d’après la version v2 (24 juin 2025). <a href="https://arxiv.org/abs/2503.18813"><code>https://arxiv.org/abs/2503.18813</code></a></li>',
     ['A-31']),
    # [112] [6.22] doublon
    (' <a href="https://csrc.nist.gov/pubs/sp/800/207/final"><code>https://csrc.nist.gov/pubs/sp/800/207/final</code></a></li>',
     ' Même source que [73]. <a href="https://csrc.nist.gov/pubs/sp/800/207/final"><code>https://csrc.nist.gov/pubs/sp/800/207/final</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [118] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/rfc8693"><code>https://datatracker.ietf.org/doc/rfc8693</code></a></li>',
     ' Même source que [69]. <a href="https://datatracker.ietf.org/doc/rfc8693"><code>https://datatracker.ietf.org/doc/rfc8693</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [176] lit. 29
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1</code></a></li>',
     ' Révision −17 publiée le 31 octobre 2026, qui expire le 4 mai 2027 ([481]). <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1</code></a></li>',
     ['A-31']),
    # [177] lit. 67
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant</code></a></li>',
     ' Révision −06 publiée le 31 octobre 2026 ([482]). <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant</code></a></li>',
     ['A-31']),
    # [218] [6.22] doublon
    (' <a href="https://raw.githubusercontent.com/modelcontextprotocol/ext-auth/main/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx"><code>https://raw.githubusercontent.com/modelcontextprotocol/ext-auth/main/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx</code></a></li>',
     ' Même source que [178]. <a href="https://raw.githubusercontent.com/modelcontextprotocol/ext-auth/main/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx"><code>https://raw.githubusercontent.com/modelcontextprotocol/ext-auth/main/specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [219] [6.22, 6.90]
    (' <a href="https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md"><code>https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md</code></a></li>',
     ' Même source que [386], lue sur la branche principale du dépôt dédié; [386], à une étiquette, fait foi. <a href="https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md"><code>https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md</code></a></li>',
     ['26-08', '27-07', '27-10']),
    # [231] [6.90]
    (' <a href="https://a2a-protocol.org/latest/sdk"><code>https://a2a-protocol.org/latest/sdk</code></a></li>',
     ' Adresse « latest », qui suit la dernière version publiée; page consultée le 27 octobre 2026. <a href="https://a2a-protocol.org/latest/sdk"><code>https://a2a-protocol.org/latest/sdk</code></a></li>',
     ['26-08', '27-07', '27-10']),
    # [237] [6.90]
    (' <a href="https://a2a-protocol.org/latest/topics/agent-discovery"><code>https://a2a-protocol.org/latest/topics/agent-discovery</code></a></li>',
     ' Adresse « latest », qui suit la dernière version publiée; page consultée le 27 octobre 2026. <a href="https://a2a-protocol.org/latest/topics/agent-discovery"><code>https://a2a-protocol.org/latest/topics/agent-discovery</code></a></li>',
     ['26-08', '27-07', '27-10']),
    # [238] [6.90]
    (' <a href="https://a2a-protocol.org/latest/topics/extensions"><code>https://a2a-protocol.org/latest/topics/extensions</code></a></li>',
     ' Adresse « latest », qui suit la dernière version publiée; page consultée le 27 octobre 2026. <a href="https://a2a-protocol.org/latest/topics/extensions"><code>https://a2a-protocol.org/latest/topics/extensions</code></a></li>',
     ['26-08', '27-07', '27-10']),
    # [240] [6.22] doublon
    (' <a href="https://a2a-protocol.org/latest/whats-new-v1"><code>https://a2a-protocol.org/latest/whats-new-v1</code></a></li>',
     ' Même source que [235]. <a href="https://a2a-protocol.org/latest/whats-new-v1"><code>https://a2a-protocol.org/latest/whats-new-v1</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [246] [6.20]
    (' <a href="https://kai-waehner.de/about"><code>https://kai-waehner.de/about</code></a></li>',
     ' Page de présentation de l’auteur (catégorie C au sens du tableau 66), sans valeur d’appui. <a href="https://kai-waehner.de/about"><code>https://kai-waehner.de/about</code></a></li>',
     ['26-04']),
    # [248] [6.22] doublon
    (' <a href="https://github.com/cloudevents/spec/blob/ce@v1.0.2/cloudevents/spec.md"><code>https://github.com/cloudevents/spec/blob/ce@v1.0.2/cloudevents/spec.md</code></a></li>',
     ' Même source que [173]. <a href="https://github.com/cloudevents/spec/blob/ce@v1.0.2/cloudevents/spec.md"><code>https://github.com/cloudevents/spec/blob/ce@v1.0.2/cloudevents/spec.md</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [262] [6.20]
    (' <a href="https://www.confluent.io/blog/autonomous-agentic-event-driven-systems-architecture"><code>https://www.confluent.io/blog/autonomous-agentic-event-driven-systems-architecture</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://www.confluent.io/blog/autonomous-agentic-event-driven-systems-architecture"><code>https://www.confluent.io/blog/autonomous-agentic-event-driven-systems-architecture</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [276] [6.20]
    (' <a href="https://cognition.com/blog/dont-build-multi-agents"><code>https://cognition.com/blog/dont-build-multi-agents</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://cognition.com/blog/dont-build-multi-agents"><code>https://cognition.com/blog/dont-build-multi-agents</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [277] [6.20]
    (' <a href="https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems"><code>https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems"><code>https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [287] lit. 72
    (' <a href="https://www.vldb.org/pvldb/vol18/p4874-chang.pdf"><code>https://www.vldb.org/pvldb/vol18/p4874-chang.pdf</code></a></li>',
     ' doi:10.14778/3750601.3750611. <a href="https://www.vldb.org/pvldb/vol18/p4874-chang.pdf"><code>https://www.vldb.org/pvldb/vol18/p4874-chang.pdf</code></a></li>',
     ['A-31']),
    # [288] [6.22] doublon
    (' <a href="https://arxiv.org/abs/2503.11951"><code>https://arxiv.org/abs/2503.11951</code></a></li>',
     ' Même source que [287]. <a href="https://arxiv.org/abs/2503.11951"><code>https://arxiv.org/abs/2503.11951</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [289] [6.20]
    (' <a href="https://cognition.com/blog/multi-agents-working"><code>https://cognition.com/blog/multi-agents-working</code></a></li>',
     ' Argument d’éditeur (catégorie C au sens du tableau 66), cité comme tel, jamais à l’appui d’une exigence. <a href="https://cognition.com/blog/multi-agents-working"><code>https://cognition.com/blog/multi-agents-working</code></a></li>',
     ['26-01', '26-04', '27-02', '27-11']),
    # [290] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/14"><code>https://artificialintelligenceact.eu/article/14</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/14"><code>https://artificialintelligenceact.eu/article/14</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [292] lit. 48
    (' <a href="https://arxiv.org/abs/2503.13657"><code>https://arxiv.org/abs/2503.13657</code></a></li>',
     ' Version citée : v3 (26 octobre 2025). <a href="https://arxiv.org/abs/2503.13657"><code>https://arxiv.org/abs/2503.13657</code></a></li>',
     ['A-31']),
    # [304] révision non vérifiée
    (' <a href="https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles"><code>https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles</code></a></li>',
     ' La révision J3016_202609 que désignent le titre d’origine et l’adresse n’a pas été vérifiée à la source; le cadre ne s’appuie que sur la taxonomie des niveaux et sur la notion de domaine de conception opérationnel. <a href="https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles"><code>https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles</code></a></li>',
     ['11-29']),
    # [308] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/rfc8785"><code>https://datatracker.ietf.org/doc/rfc8785</code></a></li>',
     ' Même source que [236]. <a href="https://datatracker.ietf.org/doc/rfc8785"><code>https://datatracker.ietf.org/doc/rfc8785</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [309] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-aims"><code>https://datatracker.ietf.org/doc/draft-ietf-wimse-aims</code></a></li>',
     ' Même source que [93]. <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-aims"><code>https://datatracker.ietf.org/doc/draft-ietf-wimse-aims</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [318] lit. 28
    (' <a href="https://www.quebec.ca/gouvernement/travailler-gouvernement/normes-gouvernance-pratiques-internes/protection-des-renseignements-personnels/technologie-et-droit-a-la-protection-des-renseignements-personnels/decision-traitement-automatise"><code>https://www.quebec.ca/gouvernement/travailler-gouvernement/normes-gouvernance-pratiques-internes/protection-des-renseignements-personnels/technologie-et-droit-a-la-protection-des-renseignements-personnels/decision-traitement-automatise</code></a></li>',
     ' Page mise à jour le 20 octobre 2025. <a href="https://www.quebec.ca/gouvernement/travailler-gouvernement/normes-gouvernance-pratiques-internes/protection-des-renseignements-personnels/technologie-et-droit-a-la-protection-des-renseignements-personnels/decision-traitement-automatise"><code>https://www.quebec.ca/gouvernement/travailler-gouvernement/normes-gouvernance-pratiques-internes/protection-des-renseignements-personnels/technologie-et-droit-a-la-protection-des-renseignements-personnels/decision-traitement-automatise</code></a></li>',
     ['A-31']),
    # [323] lit. 68
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices"><code>https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices</code></a></li>',
     ' Révision −08 publiée le 30 octobre 2026; dernier appel de l’IETF jusqu’au 13 novembre 2026 ([484]). <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices"><code>https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices</code></a></li>',
     ['A-31']),
    # [327] [6.22] doublon
    (' <a href="https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html"><code>https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html</code></a></li>',
     ' Même source que [176]. <a href="https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html"><code>https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [329] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/rfc9207"><code>https://datatracker.ietf.org/doc/rfc9207</code></a></li>',
     ' Même source que [212]. <a href="https://datatracker.ietf.org/doc/rfc9207"><code>https://datatracker.ietf.org/doc/rfc9207</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [330] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/rfc9728"><code>https://datatracker.ietf.org/doc/rfc9728</code></a></li>',
     ' Même source que [211]. <a href="https://datatracker.ietf.org/doc/rfc9728"><code>https://datatracker.ietf.org/doc/rfc9728</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [332] [6.22] doublon
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens</code></a></li>',
     ' Même source que [179]. <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [334] lit. 69
    (' <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth</code></a></li>',
     ' Révision −03 publiée le 2 novembre 2026. <a href="https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth"><code>https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth</code></a></li>',
     ['A-31']),
    # [348] [6.22] doublon
    (' <a href="https://genai.owasp.org/llm-top-10"><code>https://genai.owasp.org/llm-top-10</code></a></li>',
     ' Même source que [347]. <a href="https://genai.owasp.org/llm-top-10"><code>https://genai.owasp.org/llm-top-10</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [349] [6.22] doublon
    (' <a href="https://owasp.org/www-project-non-human-identities-top-10/2025/top-10-2025"><code>https://owasp.org/www-project-non-human-identities-top-10/2025/top-10-2025</code></a></li>',
     ' Même source que [91]. <a href="https://owasp.org/www-project-non-human-identities-top-10/2025/top-10-2025"><code>https://owasp.org/www-project-non-human-identities-top-10/2025/top-10-2025</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [361] [6.22] doublon
    (' <a href="https://gvisor.dev/docs/architecture_guide/performance"><code>https://gvisor.dev/docs/architecture_guide/performance</code></a></li>',
     ' Même source que [134]. <a href="https://gvisor.dev/docs/architecture_guide/performance"><code>https://gvisor.dev/docs/architecture_guide/performance</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [363] [6.22] doublon
    (' <a href="https://www.usenix.org/system/files/nsdi20-paper-agache.pdf"><code>https://www.usenix.org/system/files/nsdi20-paper-agache.pdf</code></a></li>',
     ' Même source que [360]. <a href="https://www.usenix.org/system/files/nsdi20-paper-agache.pdf"><code>https://www.usenix.org/system/files/nsdi20-paper-agache.pdf</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [368] [6.22] doublon
    (' <a href="https://gvisor.dev/docs/user_guide/gpu"><code>https://gvisor.dev/docs/user_guide/gpu</code></a></li>',
     ' Même source que [134]. <a href="https://gvisor.dev/docs/user_guide/gpu"><code>https://gvisor.dev/docs/user_guide/gpu</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [375] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/25"><code>https://artificialintelligenceact.eu/article/25</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/25"><code>https://artificialintelligenceact.eu/article/25</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [394] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/12"><code>https://artificialintelligenceact.eu/article/12</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/12"><code>https://artificialintelligenceact.eu/article/12</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [431] [6.97]
    (' <a href="https://www.parl.ca/DocumentViewer/en/45-1/bill/C-36/first-reading"><code>https://www.parl.ca/DocumentViewer/en/45-1/bill/C-36/first-reading</code></a></li>',
     ' Texte du projet de loi en première lecture; [430] en donne le statut. <a href="https://www.parl.ca/DocumentViewer/en/45-1/bill/C-36/first-reading"><code>https://www.parl.ca/DocumentViewer/en/45-1/bill/C-36/first-reading</code></a></li>',
     ['27-04', '28-31', '29-10']),
    # [444] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/9"><code>https://artificialintelligenceact.eu/article/9</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/9"><code>https://artificialintelligenceact.eu/article/9</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [445] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/13"><code>https://artificialintelligenceact.eu/article/13</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/13"><code>https://artificialintelligenceact.eu/article/13</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [446] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/72"><code>https://artificialintelligenceact.eu/article/72</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/72"><code>https://artificialintelligenceact.eu/article/72</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [450] [6.22] doublon
    (' <a href="https://online.standard.no/en/isoiec-42001-2023-4"><code>https://online.standard.no/en/isoiec-42001-2023-4</code></a></li>',
     ' Même source que [395]. <a href="https://online.standard.no/en/isoiec-42001-2023-4"><code>https://online.standard.no/en/isoiec-42001-2023-4</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [459] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/73"><code>https://artificialintelligenceact.eu/article/73</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/73"><code>https://artificialintelligenceact.eu/article/73</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [461] [6.21]
    (' <a href="https://artificialintelligenceact.eu/article/27"><code>https://artificialintelligenceact.eu/article/27</code></a></li>',
     ' Site non officiel (agrégateur, catégorie C au sens du tableau 66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a href="https://artificialintelligenceact.eu/article/27"><code>https://artificialintelligenceact.eu/article/27</code></a></li>',
     ['23-16', '26-02', '27-03', '28-35']),
    # [466] [6.22] doublon
    (' <a href="https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf"><code>https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf</code></a></li>',
     ' Même source que [311]. <a href="https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf"><code>https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [468] [6.22] doublon
    (' <a href="https://kafka.apache.org/intro"><code>https://kafka.apache.org/intro</code></a></li>',
     ' Même source que [257]. <a href="https://kafka.apache.org/intro"><code>https://kafka.apache.org/intro</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [470] [6.22] doublon
    (' <a href="https://owasp.org/www-project-non-human-identities-top-10/2025"><code>https://owasp.org/www-project-non-human-identities-top-10/2025</code></a></li>',
     ' Même source que [91]. <a href="https://owasp.org/www-project-non-human-identities-top-10/2025"><code>https://owasp.org/www-project-non-human-identities-top-10/2025</code></a></li>',
     ['24-09', '25-09', '26-03', '27-01']),
    # [6.89] lit. 82
    ('<li><strong><code>[6]</code></strong> Anthropic (Erik S. et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note de l’éditeur :',
     '<li><strong><code>[6]</code></strong> Anthropic (Erik S. [Schluntz] et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note du cadre :',
     ['26-07']),
    # [6.89]
    ('<li><strong><code>[65]</code></strong> Anthropic (Erik S. et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note de l’éditeur :',
     '<li><strong><code>[65]</code></strong> Anthropic (Erik S. [Schluntz] et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note du cadre :',
     ['26-07']),
    # [6.92] lit. 29
    ('(Internet-Draft, version remplacée par la -16)',
     '(Internet-Draft; remplacée par la −16 du 3 septembre 2026, puis par la −17 du 31 octobre 2026)',
     ['26-10']),
    # [6.98]
    ('<li><strong><code>[353]</code></strong> Gouvernement du Canada (2026). Guide on the Use of Agentic Artificial Intelligence. <a href="https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-agentic-artificial-antelligence.html"><code>https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-agentic-artificial-antelligence.html</code></a></li>',
     '<li><strong><code>[353]</code></strong> Gouvernement du Canada (2026). Guide on the Use of Agentic Artificial Intelligence. <a href="https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-agentic-artificial-intelligence.html"><code>https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-agentic-artificial-intelligence.html</code></a></li>',
     ['27-05']),
    # [6.100]
    (' Google Research. https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ (article : arXiv:2512.08296). <a href',
     ' Google Research. Article associé : [274]. <a href',
     ['27-08']),
    # révision non vérifiée (t3)
    ('<li><strong><code>[304]</code></strong> SAE International (2026). J3016_202609 – Taxonomy',
     '<li><strong><code>[304]</code></strong> SAE International. J3016 – Taxonomy',
     ['11-29']),
    # [6.88]
    ('<li><strong><code>[451]</code></strong> ISO/IEC (2025). ISO/IEC 42006:2025 — Exigences pour les organismes procédant à l’audit et à la certification des systèmes de management de l’IA. ISO. <a href="https://online.standard.no/en/isoiec-42006-2025"><code>https://online.standard.no/en/isoiec-42006-2025</code></a></li>',
     '<li><strong><code>[451]</code></strong> ISO/IEC (2025). ISO/IEC 42006:2025 — Exigences pour les organismes procédant à l’audit et à la certification des systèmes de management de l’IA. ISO (fiche catalogue, Standards Norway). <a href="https://online.standard.no/en/isoiec-42006-2025"><code>https://online.standard.no/en/isoiec-42006-2025</code></a></li>',
     ['26-06', '28-33']),
    # [6.88]
    ('<li><strong><code>[452]</code></strong> ISO/IEC (2025). ISO/IEC 42005:2025 — Technologies de l’information — Intelligence artificielle — Évaluation de l’impact des systèmes d’IA. ISO. <a href="https://online.standard.no/en/isoiec-42005-2025"><code>https://online.standard.no/en/isoiec-42005-2025</code></a></li>',
     '<li><strong><code>[452]</code></strong> ISO/IEC (2025). ISO/IEC 42005:2025 — Technologies de l’information — Intelligence artificielle — Évaluation de l’impact des systèmes d’IA. ISO (fiche catalogue, Standards Norway). <a href="https://online.standard.no/en/isoiec-42005-2025"><code>https://online.standard.no/en/isoiec-42005-2025</code></a></li>',
     ['26-06', '28-33']),
    # [6.88]
    ('<li><strong><code>[453]</code></strong> ISO/IEC (2023). ISO/IEC 23894:2023 — Technologies de l’information — Intelligence artificielle — Recommandations relatives au management du risque. ISO. <a href="https://online.standard.no/en/isoiec-23894-2023"><code>https://online.standard.no/en/isoiec-23894-2023</code></a></li>',
     '<li><strong><code>[453]</code></strong> ISO/IEC (2023). ISO/IEC 23894:2023 — Technologies de l’information — Intelligence artificielle — Recommandations relatives au management du risque. ISO (fiche catalogue, Standards Norway). <a href="https://online.standard.no/en/isoiec-23894-2023"><code>https://online.standard.no/en/isoiec-23894-2023</code></a></li>',
     ['26-06', '28-33']),
]

JOURNAL = [
    # (localisation, correctif en une phrase, constats)
    ('Annexe B, introduction', 'Statut normatif de la fiche fondé sur le renvoi de l’EXIG-GOV-07 (section 1.4).', ['22-07', '23-09']),
    ('Annexe B, règles d’utilisation', 'Règle « Source de vérité » ramenée à un renvoi (EXIG-GOV-07, EXIG-AUT-08, EXIG-AUT-24), sans DOIT hors bloc; palier et seuil tenus au seul catalogue, seuil de fiche seulement plus strict, écart de palier traité comme incident de réconciliation; grandeur mesurée jamais déclarée par l’agent.', ['22-07', '22-08', '22-01']),
    ('Annexe B, règles d’utilisation', 'Réévaluation : renvoi à l’EXIG-GOV-12, seule liste des déclencheurs, avant la mise en service; analogie de Feng et al. ramenée à un certificat interne, sans l’indépendance du tiers.', ['23-10', '22-09', '22-11']),
    ('Annexe B, règles d’utilisation', '« Jalon » au lieu de « point de contrôle »; pilote sur données réelles traité comme une mise en production; fiche minimale de l’existant inventorié (EXIG-GOV-21); « parrain » au lieu de « propriétaire métier » pour l’attestation.', ['A-25', 'A-26', 'A-27', 'A-34']),
    ('Annexe B, tableau 63', 'Renvois de l’invite système corrigés (EXIG-INT-15, EXIG-GOV-12); régime des agents intégrés aux logiciels-services (EXIG-ARC-26); palier et seuil lus au catalogue, mode d’idempotence, palier de la compensation et étiquette de fiabilité des sources de contexte; identité de compensation; dossier de décision; énumération d’états commune au registre et au catalogue.', ['22-29', '22-08', '22-12', 'A-03', 'A-06', 'A-09', 'A-17', 'A-18']),
    ('Annexe B, exemple de fiche', 'Personnes désignées par des identifiants fictifs, niveau demandé par le parrain et approuvé par une autre personne; seuil retiré de la fiche; clé d’idempotence et étape pivot pour le paiement P3; renew_on renvoyant à l’EXIG-GOV-12; modes d’accès par mandant et par déclencheur planifié; empreintes marquées comme abrégées; domaine ent.ca et classe « moderee » harmonisés avec l’annexe C; conventions OpenTelemetry consignées par version de référence, version émise et réglage d’adhésion (A-29).', ['22-06', '22-08', '22-09', '22-10', '22-15', '22-16', '22-17', '22-13', 'A-24', 'A-29']),
    ('Annexe B, exemple de fiche', 'Non retenu en l’état : épinglage de la v1.41.1 (A-29 retient la ligne v1.41, v1.41.0 restant la dernière version étiquetée vérifiée, lit. 35); la fiche garde 1.41.0.', ['26-09']),
    ('Annexe C, introduction et conventions', 'Exemples déclarés informatifs, leur structure devenant normative par renvoi exprès (C.1 et C.2 : EXIG-ORC-22, EXIG-MCP-20; C.6 : EXIG-AUT-12; C.8 : EXIG-OBS-12); un domaine fictif et son préfixe inverse; montants en cents; entrées des hachages explicitées (description réunie en une ligne, clé JCS, objet de h).', ['22-07', '23-09', '22-17', '23-13', '22-26', '23-15', '24-08']),
    ('Annexe C, tableau 64', 'Exigences illustrées complétées (EXIG-AUT-24, EXIG-ORC-17, EXIG-EVT-11, EXIG-AUT-09, EXIG-AUT-15, EXIG-AUT-19, EXIG-OBS-13); EXIG-IAM-11 retirée de la ligne C.8.', ['23-22', 'A-13', 'A-12', 'A-02']),
    ('Annexe C, C.1', 'Montant total retiré des arguments (calculé par le serveur et renvoyé en sortie, la passerelle calculant la même grandeur pour le seuil); prix en entiers de cents bornés; état « soumis » défini (circuit d’approbation interne, sans envoi au fournisseur); definition_digest recalculé (sha256:e8c1ccd7…).', ['22-01', '22-26', '22-05']),
    ('Annexe C, C.1 (lecture)', 'Compensation et palier situés à l’entrée de catalogue C.2, C.1 ne portant que des champs MCP. À signaler à t3 : l’EXIG-ORC-17 renvoie au champ compensation « (annexe C, C.1) », qui figure en C.2.', ['A-08']),
    ('Annexe C, C.2', 'Seuils exprimés par une grandeur calculée par la passerelle (somme des lignes), avec unité, portée (tâche, fournisseur sur 24 h), fenêtre et borne inclusive; compensation avec son palier; idempotence native avec les trois comportements de l’EXIG-ORC-22 et la durée de conservation des clés; état « production »; lecture réécrite.', ['22-01', '22-02', '22-13', '22-27', '22-12', 'A-13', 'A-34']),
    ('Annexe C, C.3', 'Carte de référence servie par la passerelle; extension de gouvernance limitée aux cartes servies aux clients authentifiés (EXIG-A2A-06); renvoi à la section 8.4 de la spécification A2A 1.0; résolution par kid au jeu de clés épinglé et jku suivi seulement s’il concorde avec l’URL inscrite (RFC 8725, § 3.10, citée sans appel, faute d’entrée en G); ETag dérivé du hachage de la carte servie, signatures comprises; liaison du jeton exigée pour la classe élevée.', ['22-04', '22-20', '22-21', '22-22', 'A-20', 'A-33']),
    ('Annexe C, C.3', 'Non retenu : la décision « inscrite » du scénario du § 6.6 relève de la tranche du § 6.6; C.3 (« recommande ») est cohérente.', ['22-23']),
    ('Annexe C, C.4', 'Type préfixé ca.ent.*; compteur posé par l’intercepteur de publication (EXIG-EVT-11); profondeur et plafond de largeur distingués; correspondance de classification inscrite au catalogue (valeurs de l’extension non énumérées, faute de vérification); conditions de l’ordre Kafka (partitions figées, producteur idempotent ou une requête en vol).', ['22-17', '22-19', '22-24', '22-25', 'A-02']),
    ('Annexe C, C.5', 'Deux jetons montrés : jeton 1 de l’agent à la passerelle (aud passerelle, cnf agent), jeton 2 de la passerelle au serveur (client_id passerelle, cnf passerelle, act inchangé, exp au plus celle du jeton 1), portée de la tâche dans authorization_details, comme l’extrait du § 9.3 (t4).', ['22-03', '22-28', '24-03', 'A-16']),
    ('Annexe C, C.5', 'Non retenu : grammaire unique des portées OAuth; finance:read est gardé pour concorder avec l’extrait du § 9.3 et le tableau 35, hors tranche.', ['22-18']),
    ('Annexe C, C.6', 'Objet haché montré et h recalculé selon l’EXIG-AUT-12 (canonisation de {outil, version, definition_digest, agent_id, task_id, arguments}), clé d’idempotence recalculée (JCS de ["idem-v1", task_id, step_id]); rôle de l’approbateur; authorization_details produit par la passerelle avec tous les champs significatifs et la grandeur calculée; lecture : I-JSON, vérifications de la passerelle, jeton conservé par la passerelle, une opération par jeton, double approbation par deux jetons, compensation approuvée avec l’étape, hors bande, profil du cadre pour la RFC 9396.', ['23-03', '23-04', '23-06', '23-07', '23-15', '24-08', '22-01', 'A-10', 'A-11', 'A-12', 'A-15']),
    ('Annexe C, C.6 et C.7', 'Bloc « Action soumise » de C.6, égaré sous le titre de C.7 (aussi dans le PDF), replacé dans C.6 (constat de relecture à l’implémentation).', ['A-11']),
    ('Annexe C, C.7', 'Plafonds « de même valeur que la fiche type » (autre agent); arrêt vers l’avant, compensations sous l’identité de compensation et sur une réserve hors enveloppe (EXIG-ORC-31); « parrain » au lieu de « propriétaire ».', ['22-14', '23-14', 'A-06', 'A-34']),
    ('Annexe C, C.8', 'Enregistrement d’issue précédé d’un enregistrement d’intention référencé; flux nommé; definition_sha256 ajouté (aligné sur l’extrait du § 10.3, t4); liste approbations avec jti et rôle; grandeur calculée du seuil; modèle compact à l’étape de création; valeurs recalculées; lecture : h atteste les octets transmis, chaînage interne contre troncature détectée par les points de contrôle externes, empreinte simple d’arguments à saler pour un outil à faible entropie, champs A2A omis.', ['23-02', '23-04', '23-05', '23-06', '23-07', '23-08', '23-12', '24-14', 'A-19']),
    ('Annexe C, C.8 (lecture)', 'Recommandation OWASP « journaux immuables et signés » retirée (non vérifiée, lit. 61); dates du RIA appuyées sur [57, 58] et obligations sur [61, 447] au lieu de l’agrégateur FLI [94, 394].', ['26-02', '27-03', '28-35']),
    ('Annexe C, C.8', 'Empreinte de l’enregistrement maintenue fictive, comme le déclarent les conventions (valeurs élidées).', ['23-15']),
    ('Annexe D, introduction', 'Forces annoncées conformes aux blocs (DOIT, NE DOIT PAS, DEVRAIT); PRIN et tableaux visés signalés comme normatifs hors registre. Lignes du registre non touchées (synchronisées par l’orchestrateur).', ['23-20']),
    ('Annexe D, registre', 'Non retenu ici : titres et forces des lignes (accord des titres, forces mixtes), redondances entre exigences et responsable de la révision trimestrielle relèvent des blocs du corps (A-20, A-22, A-24) et de la synchronisation du registre par l’orchestrateur; exception subject_token de l’EXIG-MCP-11 : tranche du § 6.5; colonnes supplémentaires (section, mesure ISO/IEC 42001) non ajoutées.', ['23-17', '23-18', '23-19', '23-21', '24-10', '28-27']),
    ('Annexe E, Contenu non fiable et Triade létale', 'Définitions alignées sur les EXIG-SEC-03, 04 et 06 (sources inscrites, pièces jointes du mandant, propagation de l’étiquette, outils d’envoi, règle de deux et approbation liée à l’action; propriétés [A], [B], [C] de Meta, session composée).', ['24-01', '24-05', 'A-17']),
    ('Annexe E, nouvelles entrées', 'Entrées « Session » et « Environnement serveur » (alignées sur le tableau 7, t1), « Hors bande », « Mandat », « Plan de contrôle » et « Service de politiques » ajoutées à leur place alphabétique.', ['24-02', '23-11', 'A-01', 'A-04', 'A-12', 'A-16', 'A-17']),
    ('Annexe E, Jeton délégué, Mandant, Mandat', 'Intersection répartie entre serveur d’autorisation (portées, tâche dans authorization_details) et serveur de ressources (droits du sub); expiration bornée par le jeton reçu; mandant toujours l’entité d’origine; mandat d’agent ambiant nommé à part.', ['24-03', '24-13', '22-28', 'A-16']),
    ('Annexe E, Passerelle d’agents', 'Mandataire sur tout le trafic MCP et A2A et toute action P2-P3, inverse en entrée et de sortie en sortie; instances partagées; intention journalisée avant le relais, issue après.', ['24-14', 'A-01', 'A-19']),
    ('Annexe E, Empreinte et Jeton d’approbation', 'h redéfini comme la canonisation d’un objet (aligné sur l’EXIG-AUT-12, t3) et portée de ce qu’il atteste; jeton : émetteur, audience, rôle de l’approbateur, conservé par la passerelle, une opération, double approbation par deux jetons.', ['23-15', '24-08', 'A-10', 'A-11', 'A-12', 'A-15']),
    ('Annexe E, Classe de risque', 'Article 65.2 de la Loi sur l’accès ajouté; plafonds rattachés à l’EXIG-CON-02.', ['24-06', 'A-24']),
    ('Annexe E, Compensation', 'Déclenchement quand la progression devient impossible (réessais épuisés ou erreur non transitoire); outil avec palier; identité de compensation; étape incertaine compensée seulement après clôture ou issue définitive.', ['24-07', 'A-06', 'A-07', 'A-08']),
    ('Annexe E, Niveau d’autonomie, Flux déterministe, Agent ambiant, Palier d’outil, Point de contrôle', 'Niveau borné par la classe (EXIG-CON-02); N0 qualifie un flux, non un agent; N4 couvre les tâches déclenchées sans demande d’une personne, et l’agent ambiant qui écrit seul relève de N4 (alignement sur t1); flux assisté inscrit avec son niveau; P2 et P3 disjoints par l’effet; « jalon » au sens (2).', ['24-11', 'A-27']),
    ('Annexe E, Évaluation continue', 'Trois étages E1 à E3 (plus de « paliers » d’évaluation dans les annexes B à G); relance sur tout changement visé par l’EXIG-GOV-12.', ['24-15', 'A-27', 'A-24']),
    ('Annexe E, EFVP et Décision fondée exclusivement…', 'Article 63.5 de la Loi sur l’accès ajouté pour les organismes publics; interprétation gouvernementale appuyée sur [318].', ['24-16']),
    ('Annexe E, Idempotence', 'Clé dérivée de la tâche racine, vérifiée par le système qui produit l’effet ou un adaptateur à registre durable; rejet d’une clé réutilisée avec d’autres arguments; conservation couvrant la fenêtre de rejeu.', ['24-17', 'A-09']),
    ('Annexe E, PEP', 'Rôle de PA attribué au fournisseur d’identité et au plan de contrôle, d’après le tableau du § 9.1 (vérifié).', ['24-18']),
    ('Annexe E, Outil et Agent', 'Critère agent/outil de l’A-20 : choix des actions au moyen d’un modèle; état de tâche et élicitation n’en font pas un agent.', ['24-19', 'A-20']),
    ('Annexe E, Catalogue des protocoles et Catalogue d’entreprise', 'Cinq statuts, dont Suspendu (A-21); Contenir jusqu’à l’échéance du plan de sortie; révision par l’architecture d’entreprise, approbation par le comité (EXIG-GOV-18); « responsable » au lieu de « propriétaire ».', ['23-17', '24-10', '28-27', 'A-21', 'A-22', 'A-34']),
    ('Annexe E, Dérogation', 'Renvoi à l’EXIG-GOV-17, qui tient la liste; agent sans fiche au registre ou sans parrain nommé; liste enrichie (hors bande P3, triade létale, journal d’audit).', ['24-12', 'A-24']),
    ('Annexe E, Agent ambiant', 'Définition présentée comme choix du cadre inspiré de LangChain; date de [86] non ajoutée (jour non vérifié).', ['26-05']),
    ('Annexe E, Coupe-circuit, Échec en mode fermé, Journal d’audit, Approbation humaine', 'Arrêt vers l’avant sans toucher le canal de compensation, cible de l’EXIG-IAM-20 et exercice de l’EXIG-SEC-26; politique en cache valide jusqu’à échéance; journal « chaîné, signé et ancré » au lieu d’« inaltérable »; approbation P3 hors bande.', ['A-04', 'A-05', 'A-06', 'A-12', 'A-19']),
    ('Annexe E, Délégation (MAJEUR transversal)', 'Volet du corps (§ 9.3, EXIG-IAM-10, PRIN-03 à trois termes) laissé aux tranches t1 et t4; le glossaire suit leur règle.', ['24-03', '24-04']),
    ('Annexe F, introduction et F.1', 'Portée du registre limitée à la version 1.0; 473 entrées dont 25 doublons signalés (448 sources distinctes); populations de chaque passe (121, 428, 473) et écart non ventilé déclarés; relevé lien par lien non publié.', ['25-01', '25-02', '25-03', '27-01', '26-03']),
    ('Annexe F, tableau 66', 'Catégorie C : jamais à l’appui d’un fait ou d’une exigence; argument d’éditeur nommé comme tel, sans appel; entrées de G signalées.', ['26-01', '27-02', 'A-31']),
    ('Annexe F, tableau 68', 'Nos 1, 7 et 30 : références [175], [35], [75] et [95] ajoutées; no 16 : billet de Google distingué de la v3 de l’article [274]; no 17 : 5 Mo, article de 2020 et renvoi au § 9.7; no 21 : « au moins cinq ans »; no 24 : réserve d’interprétation retirée (lettre de l’art. 17); no 31 : étape incertaine traitée selon l’A-07, n’est plus présentée comme corrigée par l’ancienne règle; no 32 : CoALA inspirée de Soar et de la psychologie cognitive.', ['25-12', '25-13', '25-04', '25-14', '25-15', '25-05', '25-16']),
    ('Annexe F, F.4 et tableau 69', 'Légende : décisions à l’état de la version 1.0, définitions des décisions étendues aux sources A, ✗ signalé comme réunissant deux verdicts, catégories des pages non lues qualifiées; lignes 7, 16, 36, 41 et 52 marquées « réintroduite à l’audit final » avec leur numéro en G.', ['25-01', '25-07', '25-08']),
    ('Annexe F, tableau 69 et F.2', 'Non retenu (borne de faisabilité : un tableau se corrige cellule par cellule) : colonnes « no G » et « décision à l’audit final », catégorie de chaque entrée de G, symbole distinct pour « contredite », recalcul de F.2 et publication du registre lien par lien; à traiter par script dans une révision.', ['25-01', '25-02', '25-03', 'A-31']),
    ('Annexe G, introduction', 'État des sources au 27 octobre et vérifications des 27 et 28 octobre; catégories A ou B « en principe », exceptions signalées; 473 entrées dont 25 doublons, numéros jamais réattribués.', ['25-06', '27-01', '26-01', '28-24']),
    ('Annexe G, doublons', '25 entrées annotées « Même source que [m] » : [65]→[6], [70] et [118]→[69], [112]→[73], [308]→[236], [363]→[360], [330]→[211], [248]→[173], [99]→[74], [218]→[178], [240]→[235], [329]→[212], [288]→[287], [348]→[347], [327]→[176], [332]→[179], [309]→[93], [349] et [470]→[91], [466]→[311], [450]→[395], [361] et [368]→[134], [468]→[257], [219]→[386]. Les paires [30]/[229]/[472], [36]/[106], [350]/[374], [28]/[345] et [273]/[274] sont des documents distincts : non annotées.', ['27-01', '26-03', '24-09', '25-09', '28-31', '27-07', '27-10']),
    ('Annexe G, sources de catégorie C', 'Entrées du site FLI ([62], [94], [290], [375], [394], [444]-[446], [459], [461]) annotées comme source secondaire non officielle, renvoyant à [61]; blogues de positionnement ([44], [45], [262], [276], [277], [289]) et page [246] annotés comme arguments d’éditeur. Les appels du corps relèvent des tranches t1 à t5 (t5 les a remplacés par [61] et [412]).', ['26-01', '26-02', '26-04', '27-02', '27-03', '27-11', '28-35', '23-16']),
    ('Annexe G, versions et dates', 'Révisions ultérieures signalées pour [176] (−17), [177] (−06), [93] (−01), [323] (−08, dernier appel), [334] (−03); [210] : −16 puis −17; versions arXiv de [101] (v2) et [292] (v3); dates de [76] et [318]; DOI de [287]; [58] non relu au JO; [87] : la page présente la v1.0; pages « latest » de [68], [231], [237], [238] datées de consultation.', ['26-10', '26-08', '27-07', '27-10', 'A-31']),
    ('Annexe G, entrées ponctuelles', '[6] et [65] : « Note du cadre » et nom complété entre crochets (forme publiée gardée, lit. 82); [11] : reproduction de presse signalée; [273] : entrée mal formée corrigée; [353] : coquille d’URL corrigée; [431] distinguée de [430]; [451]-[453] : revendeur Standards Norway nommé; [304] : révision J3016_202609 signalée comme non vérifiée (t3 l’a retirée du corps).', ['26-07', '25-11', '27-08', '27-05', '27-04', '28-31', '29-10', '26-06', '28-33', '11-29']),
    ('Annexe G, non retenus', 'Non retenus faute de fait établi ou hors tranche : gabarit unique appliqué par script (6.86); date de [86]; URL et titres de [52], [142], [228], [299]; [19] sans date; [462] (issue ou demande de tirage : non vérifié); [427] (art. 10.1 et 10.3, de mémoire); [242] (date de disponibilité générale à vérifier); [189] et [30] pour la v0.1, [17] pour les 1 000 à 2 000 jetons, [305] et l’attribution de [275]/[276] (appels du corps, autres tranches); « Note de l’éditeur » de [113] et [116] (absente du texte); accord « consultée »/« consulté » de [116] et [232] (justifié par le nom accordé); dates SPIFFE et SPIRE confirmées (lit. 64).', ['25-10', '26-15', '27-09', '28-32', '29-16', '26-05', '26-11', '26-12', '27-15', '28-34', '27-06', '27-13', '26-14', '27-12', '27-14', '26-07', '26-13']),
    ('Annexe G, Firecracker', 'Constat 6.76 traité au tableau 68 et par l’annotation du doublon [363]; requalification du reproche « six périphériques virtio » non faite (liste de 2020 non vérifiée).', ['25-04']),
    ('Annexe H, divulgation et H.1', 'Régime de l’annexe : constats et propositions sans effet sur le corps, errata corrigeant le corps; règle de divergence remplacée par trois natures d’écart (erratum prioritaire à toute date, omission à la date de l’état des sources, nouveauté); « devra » ramené à « pourrait ».', ['28-01', '28-02']),
    ('Annexe H, divulgation et H.1', 'Régime de vérification décrit sans contradiction (relevé individuel, échantillon contre-vérifié de taille non consignée, deux lignes en vérification partielle, absence de capture ou d’empreinte); date de consultation des références de H déclarée.', ['28-03', '28-32']),
    ('Annexe H, H.1 et tableau 70', 'Dates de référence : état des sources au 27 octobre 2026, vérifications des 27 et 28 octobre; en-tête du tableau 70 corrigé.', ['25-06', '28-24']),
    ('Annexe H, H.2, H.4 et tableau 72', 'Catégorie « omission à la date de l’état des sources » énoncée (H.1) et appliquée : HTTP+SSE, a2a-tck alpha et EN 18286 versés en H.4; autres faits antérieurs au 27 octobre qualifiés. La ligne no 4 du tableau 72 proposée par la revue n’est pas ajoutée : le fait est une omission et non un erratum, et figure en H.4.', ['28-04', '29-03']),
    ('Annexe H, tableau 70, H.2 et tableau 72 (no 3)', 'Signal MCP : date annoncée, non survenue; EXIG-GOV-18 et non EXIG-INT-23 pour MCP au statut Adopter, déclenchement seulement en cas de changement incompatible ou de dépréciation; « aucun des trois signaux » n’est survenu.', ['28-06', '29-04', '29-05', '28-12']),
    ('Annexe H, tableau 70 et H.2 (extensions)', 'Stade Beta et application de l’EXIG-GOV-19 extension par extension soumis au comité, sans réinterprétation par l’annexe; « devrait » au lieu de « doit »; quota de l’EXIG-MCP-04 à viser sur la primitive tâche si Tasks rejoint le protocole de base.', ['28-07', '28-08']),
    ('Annexe H, tableau 70 (a2a-tck)', 'Réserve rattachée aux EXIG-INT-09 et EXIG-GOV-19, à une étiquette épinglée, et constat versé en H.4 comme omission.', ['28-09', '28-23']),
    ('Annexe H, tableau 70 et H.5 (EN 18286)', 'Présomption de conformité à l’art. 17 présentée comme à vérifier (art. 40 consolidé, décision 2026/2274, affaires juridiques); contradiction avec H.5 levée (« pourrait porter une exigence »).', ['28-10', '29-12']),
    ('Annexe H, H.3 et tableau 71', 'Reports 2, 3, 7, 8 et 9 reconnus comme touchant la structure normative; report 8 déclaré inapplicable en l’état (circularité), avec la voie de l’A-25; report 9 rattaché aussi au § 4.3; report 1 visant l’alinéa « Trois conséquences pratiques », référence manquante signalée; report 5 complété des tableaux 58 et 59; report 7 : « 287 lignes dans la version 1.1, 299 après ajout »; EXIG-AMF-05 et -07 dites identifiants de la Note AMF IA.', ['29-11', '28-21', '28-22', '28-19', '28-20', 'A-25', 'A-30']),
    ('Annexe H, H.2 (MCP)', 'Retrait accéléré pour risque de sécurité actif (au moins 90 jours) mentionné.', ['28-11']),
    ('Annexe H, tableau 72 (no 1) et tableau 70', 'Erratum no 1 étendu au § 13.1; libellé « comité directeur technique de neuf sièges »; § 13.1 ajouté à la ligne A2A du tableau 70.', ['29-01', '28-13', '29-02']),
    ('Annexe H, tableau 72 (no 2) et H.5', 'Date du 4 août traitée comme écart de citation prouvé (retirer ou rattacher à une source); H.5 : « non étayée par les sources citées ».', ['29-06', '28-15', '29-13']),
    ('Annexe H, tableau 72', 'Titre et statut de chaque ligne (erratum prouvé, écart de citation, écart entre livrables); colonne « Où » du no 2 complétée des § 6.9 et 13.1; appels [5, 35] et [35, 130] distingués.', ['28-14', '29-08', '29-07']),
    ('Annexe H, H.4 (art. 50(2))', 'Précision requalifiée : la section 12.4 omet la transition que la section 12.7 énonce déjà [57, 457]; tableau 70 : « rappel ». Date non relue au règlement 2026/1744.', ['28-16', '29-09']),
    ('Annexe H, tableau 70 (OAuth 2.1)', 'Tableau aligné sur la prose : un brouillon actif n’a pas d’échéance, la ligne pouvant sortir du tableau 59.', ['28-17']),
    ('Annexe H, tableau 70 (WIMSE)', 'Exigences adossées à AIMS complétées (EXIG-IAM-14, EXIG-MCP-21, EXIG-AUT-13, EXIG-AUT-14, EXIG-SEC-13); brouillon de révocation classé hors WIMSE.', ['28-18']),
    ('Annexe H, renvois', '« Le tableau 70, 71, 72 » au lieu de « Le 70 », etc.', ['28-25', '29-15']),
    ('Annexe H, H.2', 'J2a présenté comme jalon du cadre qui précède les échéances réglementaires.', ['28-26']),
    ('Annexe H, tableau 70 (ATLAS)', '« déclencherait » au lieu de « déclenche »; option de revue trimestrielle signalée au comité (cadence mensuelle déduite).', ['28-28']),
    ('Annexe H, tableau 70 (OpenTelemetry)', 'Registre nommé : dépôt semantic-conventions-genai, fichier et commit 244465e, d’après [485].', ['28-29']),
    ('Annexe H, H.2', 'Annonce de la prose réécrite : elle développe les raisonnements que le tableau résume.', ['28-30']),
    ('Annexe H, H.5', 'Liste « non rouverts » étendue à toute source du corps absente du tableau 70; IR 8547 : vérification longue étendue aux jetons d’approbation et aux cartes signées, point d’agilité cryptographique suggéré.', ['29-14', '29-19', 'A-19']),
    ('Annexe H, H.4 et références', 'C-36 : LEGISinfo [492] et Veille [493] distingués; [493] : numéros de la Veille préfixés.', ['27-04', '28-31', '29-10', '29-18']),
    ('Annexe H, références', 'Non retenu : une URL par objet pour [483], [486] et [492] (adresses individuelles non relevées par l’annexe, non vérifiables ici).', ['29-17']),
    ('Annexe H, identité documentaire', 'Non retenu dans H.1-H.5 : numéro de version et ligne d’historique relèvent de l’orchestrateur (version 1.2, section H.6); « huit annexes » au § 1.5 relève de t1.', ['28-05']),
    ('Annexe H, H.3 (report 7)', 'Non retenu : constat d’audit_28 selon lequel l’annexe D compterait 272 exigences, faux (il omet les 15 EXIG-A2A); c’est H.3 qui est corrigée.', ['audit_28, note finale']),
    ('Constats de la tranche 6 portant sur le corps', 'Volets du corps traités par les tranches qui les possèdent, selon les arbitrages : INT-05 et A2A-01 (A-20, t1 et t2), AUT-10 et AUT-24 (A-13, t3), IAM-11 et IAM-10 (A-16, t4), OBS-11 à 13 (A-19, t4), AUT-11, IAM-18 et IAM-22 (A-04), AUT-15 (A-12, t3), GOV-12, AUT-05 et CON-03 (A-24), SEC-04 et SEC-06 (A-17), ORC-16 (A-07, t3), INT-19, GOV-18, GOV-19 et INT-23 (A-22), CON-01 (A-25), § 1.4 (A-23); les annexes y renvoient désormais.', ['23-01', '22-01', '22-02', '22-03', '23-02', '23-03', '23-05', '23-06', '23-10', '23-11', '24-02', '25-05', '28-06', '28-07', '28-09', '29-11']),
]
