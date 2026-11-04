# chunk_22 — pages PDF 211 à 222 (sur 283)



---
## [Page PDF 211]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
• Si décision sur une personne Décisions automatisées (art. 12.1 de la Loi sur le privé) : avis au plus 
tard au moment de la décision, explication des principaux facteurs, révision humaine significative, 
conservation des éléments de décision. — EXIG-AUT-22, -23, EXIG-CON-07, -08, -09
A.6 Identité, sécurité et confiance zéro
• Tous Identité propre, cryptographique, émise par la plateforme, non partagée; aucun secret statique; 
justificatifs hors de portée du modèle. — EXIG-IAM-03 à -06
• Si agit pour une personne non dérogeable Délégation explicite par échange de jetons; aucune usurpa­
tion; portée jamais élargie; jeton à audience unique; aucun relais de jeton. — EXIG-IAM-08 à -12
• Tous Profil OAuth de l’entreprise appliqué, jetons contraints à l’émetteur et de courte durée; agents 
autonomes avec identifiants du client et portées par outil. — EXIG-IAM-13 à -16
• Tous Passerelle d’agents en coupure de tout appel EXIG-ARC-01, -08, -11, -12, EXIG-IAM-17, -18, -19, -
21 interdomaine, passerelle de modèles pour tout appel de modèle (aucun appel direct à un fournisseur), 
échec en mode fermé, secrets aval injectés par la passerelle, politiques en code versionnées et testées.
• Tous Modèle de menaces établi (analyse simplifiée pour la classe faible) et matrice de traçabilité 
menaces-contrôles (OWASP ASI) à jour. — EXIG-SEC-01, -02
• Tous Défense contre l’injection : présomption d’injection, règle de deux par session, retrait détermi­
niste des capacités d’exfiltration, patron de conception pour la classe élevée. — EXIG-SEC-03 à -07
• Si code généré Bac à sable conforme (technologie d’isolation, éphémère, réseau refusé par défaut, 
métadonnées infonuagiques bloquées, secrets injectés hors du bac à sable, délais à trois niveaux, journal 
externe, porte de validation). — EXIG-SEC-08 à -17
• Tous Chaîne d’approvisionnement : provenance approuvée, signatures vérifiées, nomenclature de 
version, chaque serveur traité comme un domaine distinct, tiers évalués. — EXIG-SEC-18 à -22
• Si classe modérée ou élevée Équipe rouge propre aux agents et suite d’attaques intégrée à la chaîne 
d’intégration; contrôles déterministes vérifiés. — EXIG-SEC-23, -24, -25
A.7 Observabilité, évaluation et coûts
• Tous Traçage de bout en bout : contexte W3C propagé dans HTTP, MCP, A2A et les événements; 
conventions GenAI à la version épinglée; attributs d’entreprise sous préfixe de domaine inversé. — EXIG-
OBS-01 à -06
• Tous Contenu des invites et réponses non capturé par défaut; toute capture exceptionnelle filtrée, 
chiffrée et à conservation courte. — EXIG-OBS-07 à -10
• Tous Journal d’audit distinct des traces, exhaustif pour chaque action à effet et chaque approbation; 
enregistrement à cinq éléments canonisé et signé; inaltérabilité vérifiée. — EXIG-OBS-11, -12, -13
• Tous Évaluation : paliers franchis et relancés à chaque changement, jeu de référence versionné compre­
nant des cas adverses et réussi aux seuils du contrat, évaluations répétées et isolées, échantillonnage de 
la production planifié, objectifs de niveau de service fixés. — EXIG-EVA-01 à -06
• Tous Coûts : enveloppe appliquée à chaque étape, quotas et plafond mensuel par agent, plus petit 
modèle suffisant, préfixe d’invite stable, imputation par centre de coûts, coût par tâche réussie comparé 
au processus sans agent, hypothèses de prix datées; lots asynchrones recommandés (EXIG-FIN-08) et 
table de conversion des unités SaaS si plateforme SaaS (EXIG-FIN-03). — EXIG-FIN-01 à -10
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 211 sur 283


---
## [Page PDF 212]

CRE-IA-2026-01 · Cadre de référence
A Grille d’homologation
A.8 Données, vie privée et conformité
• Si renseignements personnels EFVP terminée avant le passage en pilote, responsable de la protection des 
renseignements personnels consulté dès le début du projet, finalités vérifiées avant toute réutilisation. 
— EXIG-CON-04, -06
• Si traitement hors Québec Lieux de traitement cartographiés (modèles, outils, mémoires) avec EFVP 
et entente écrite pour toute communication hors Québec. — EXIG-CON-05
• Tous Mémoires et traces : durées de vie fixées, contrôles avant toute écriture en mémoire longue, aucun 
historique brut comme mémoire, magasins isolés. — EXIG-ARC-22 à -25, EXIG-CON-10
• Tous Régimes applicables inscrits à la fiche (Loi 25, LPRPDE, BSIF E-23, RIA); aucun usage interdit; 
obligations du déployeur respectées pour la classe élevée. — EXIG-CON-11 à -16
• Tous Transparence : divulgation de l’interaction avec un agent et identification des contenus produits; 
vérification humaine de tout contenu juridique. — EXIG-CON-19, -20, -22
• Tous Incidents : procédure en cinq temps connue de l’équipe de garde, registre des incidents de confi­
dentialité, règle de notification la plus exigeante. — EXIG-CON-23, -24, -25
• Si classe élevée Évaluation d’impact unifiée (EFVP, analyse d’impact algorithmique, analyse d’impact 
sur les droits fondamentaux au besoin). — EXIG-CON-26
• Si acquis d’un fournisseur Grille d’évaluation fournisseur remplie et clauses contractuelles norma­
tives intégrées au contrat. — EXIG-APP-07 à -17
B Gabarit de fiche d’agent
La fiche d’agent est l’entrée du registre d’entreprise décrite à la section 11.4. Ce gabarit fixe son contenu 
minimal et l’étape du cycle de vie où chaque champ devient exigible. Il est normatif par son contenu, pas 
par sa forme : tout outil de registre convient s’il conserve ces champs et leur historique.
Règles d’utilisation
• Ouverture et complétude. La fiche s’ouvre à l’étape Proposition et se complète au fil du cycle de vie 
(section 11.5). Elle est complète lorsque tous les champs exigés à l’étape Pilote sont remplis, ce que vérifie 
le point de contrôle qui clôt l’étape Construction et évaluation; avant cela, l’agent n’obtient aucun jeton 
d’exécution en production.
• Source de vérité. Les valeurs qui commandent un contrôle (palier d’outil, seuil, plafond, portées, niveau 
d’autonomie) DOIVENT être lues par la passerelle dans le registre et le catalogue, jamais dans ce que 
l’agent déclare de lui-même ni dans les annotations d’un serveur MCP (section 8.3).
• Réévaluation. Tout changement de modèle ou de version de modèle, d’instructions système, d’outil ou 
de palier d’outil, de version majeure d’un contrat ou d’un protocole, de population visée, de finalité ou de 
catégorie de données, ainsi que tout incident grave ou toute dérive détectée, déclenche une réévaluation 
de la classe de risque et du niveau d’autonomie (EXIG-GOV-12). Le niveau d’autonomie fonctionne 
comme le « certificat d’autonomie » de Feng et al., qui se renouvelle à chaque changement de l’agent ou 
de son environnement[83]. S’il y a des RP, l’EFVP est mise à jour, comme le recommande le guide de la 
CAI lorsqu’un projet change[413].
• Attestation. Le propriétaire métier atteste périodiquement que l’agent est encore requis et que sa fiche 
est exacte. Le cadre exige l’attestation au moins tous les 12 mois, et tous les 6 mois pour la classe élevée 
(EXIG-GOV-13); à titre d’exemple, les bonnes pratiques de Microsoft Entra Agent ID prévoient que le 
parrain atteste tous les 6 à 12 mois que chaque agent est encore requis[92]. Un agent dont l’attestation est 
échue doit passer à l’état « suspendu » (EXIG-GOV-09).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 212 sur 283


---
## [Page PDF 213]

CRE-IA-2026-01 · Cadre de référence
B Gabarit de fiche d’agent
• Contenu exclu. La fiche ne contient ni secret ni renseignement personnel de clients. Chaque serveur 
MCP a aussi une fiche au registre, qui reprend les blocs de ce gabarit qui le concernent (identification, 
propriétaires, données et RP, identité et portées, garde-fous, évaluation, observabilité, cycle de vie, 
dérogations); ses outils ont en plus leur propre entrée au catalogue (section 6.8, annexe C).
Champs de la fiche
Tableau 63 — Champs de la fiche d’agent et étape où ils deviennent exigibles
Bloc
Champ
Contenu attendu
Exigé dès
Identification
Identifiant, nom, ver­
sion
Identifiant unique et immuable au registre; nom en lan­
gage clair; version sémantique (SemVer)
Proposition
Type, plateforme et 
modèles
Agent interne, agent intégré à un logiciel-service ou 
agent de partenaire; plateforme d’exécution; environne­
ments; modèles utilisés (principaux et de repli) avec leurs 
versions épinglées; version et empreinte de l’invite sys­
tème (EXIG-GOV-07, EXIG-FIN-07)
Proposition (mo­
dèles et invite : 
Conception)
Carte d’agent
URL et empreinte de la carte d’agent signée, si l’agent est 
invocable par d’autres agents (section 6.6)
Pilote, si appli­
cable
Propriétaires
Propriétaire métier 
(parrain)
Personne nommée qui répond des effets de l’agent; son 
unité; son suppléant
Proposition
Responsable tech­
nique et équipe de 
garde
Personne nommée; équipe joignable pendant les heures 
d’exploitation déclarées et sa file d’incidents
Conception
Centre de coûts
Code imputé à chaque trace (section 10.6)
Conception
Finalité
Tâche et valeur atten­
due
Tâche confiée, en deux phrases; indicateur de valeur; pro­
cessus de référence sans agent et son coût
Proposition
Usages exclus
Ce que l’agent ne doit jamais faire, même à la demande 
d’un mandant
Conception
Mandants et déclen­
cheurs
Invocation
Personnes, rôles ou agents autorisés à l’invoquer; canaux; 
déclencheurs automatiques (événements, planification)
Conception
Orchestration
Patron
Patron retenu (section 7.2) et justification de la confi­
guration la plus simple (avec la comparaison mesurée 
face à un agent unique, EXIG-ORC-02, et les frontières 
de contexte ou de sécurité justifiant le découpage, 
EXIG-ORC-10); protocole retenu pour chaque intégration, 
justifié par la matrice de sélection (section 6.4); résultat 
de la revue d’interopérabilité aux quatre niveaux (section 
6.1); agents appelés; profondeur d’imbrication
Conception
Risque et autonomie
Classe de risque
Faible, modérée ou élevée, avec l’analyse des critères de 
la section 8.2 et l’approbation obtenue
Conception
Niveau d’autonomie
Plafond N0 à N4 approuvé, par qui (personne nommée) 
et à quelle date; domaine d’exploitation documenté pour 
N3 et N4; déclencheurs de renouvellement; échéance de 
réautorisation d’un agent ambiant de niveau N3 ou N4
Conception
Qualification régle­
mentaire
Régimes applicables (Loi sur le privé ou Loi sur l’accès, 
LPRPDE, RIA, BSIF, directive fédérale), chacun avec les 
obligations retenues et l’exigence du cadre qui y répond; 
sorties utilisées ou non dans l’Union européenne; sys­
tème à haut risque au sens du RIA ou non; décision 
fondée exclusivement sur un traitement automatisé (art. 
12.1 de la Loi sur le privé) ou non; modèle visé par la 
ligne directrice E-23 du BSIF, s’il y a lieu
Conception
Outils, agents et évé­
nements
Inventaire des dépen­
dances
Pour chaque outil, ressource, invite, agent appelé ou sujet 
d’événement : référence au catalogue, version épinglée 
et empreinte (EXIG-INT-15), palier P0 à P3 attribué au 
catalogue, seuil, effet déclaré, clé d’idempotence pour les 
outils à effet, contrat AsyncAPI pour les événements
Conception
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 213 sur 283


---
## [Page PDF 214]

CRE-IA-2026-01 · Cadre de référence
B Gabarit de fiche d’agent
Bloc
Champ
Contenu attendu
Exigé dès
Données et RP
Catégories et classifi­
cation
Catégories de données, classification, présence de RP et 
de RP sensibles, finalité de chaque usage
Conception
Localisation et mé­
moire
Lieu de traitement (province ou pays, et fournisseur) de 
chaque modèle, serveur MCP, agent délégataire et maga­
sin de mémoire ou de traces; durées de conservation des 
mémoires, index vectoriels et traces (section 5.5)
Conception
Identité et portées
Identité
Identifiant de charge de travail (p. ex. SPIFFE ID) et type 
de justificatif (section 9.2)
Pilote
Autorisations
Mode d’accès (délégation par échange de jetons ou iden­
tité propre de l’agent); portées et audiences; durée de vie 
des jetons
Pilote
Garde-fous
Contrôles actifs
Contrôles d’entrée (contenu non fiable), de sortie (pré­
vention des fuites de données) et d’action (politiques 
de la passerelle); propriétés réunies parmi contenu non 
fiable, données sensibles et effet ou communication ex­
terne (règle de deux); bac à sable si l’agent exécute du 
code, avec sa liste d’autorisation réseau
Pilote
Évaluation
Jeu de référence et ré­
sultats
Taille du jeu, dont les scénarios adverses; seuils 
d’acceptation et seuil de réussite maximale de la suite 
d’attaques automatisées (EXIG-SEC-24); date, version et 
résultat de la dernière exécution et du dernier exercice 
d’équipe rouge (EXIG-SEC-23)
Pilote
Budget et plafonds
Enveloppe
Plafonds par tâche (jetons, coût, appels d’outils, itéra­
tions, durée d’exécution active et durée totale); quota de 
jetons par minute et plafond mensuel, avec le comporte­
ment à l’atteinte du plafond (suspension ou modèle de 
repli); modèles autorisés et modèle de repli
Pilote
Compensation et es­
calade
Reprise
Compensation de chaque étape à effet; étape pivot; 
file humaine d’escalade; rôles approbateurs et règles 
d’approbation; mode dégradé
Pilote
Observabilité
Traçage et audit
Nom de service; version épinglée et version réellement 
émise des conventions OpenTelemetry GenAI (réglage 
de OTEL_SEMCONV_STABILITY_OPT_IN); capture du conte­
nu (désactivée par défaut); emplacement du journal 
d’audit; fenêtre de conservation des événements d’entrée 
(EXIG-EVT-10); objectifs de niveau de service
Pilote
Conformité
Évaluations d’impact
Référence et date de l’EFVP, y compris celle exigée par 
l’article 17 en cas de communication hors du Québec; 
consultation du responsable de la protection des RP; éva­
luation d’impact unifiée et analyse d’impact sur les droits 
fondamentaux (RIA, art. 27) lorsqu’elle est exigée (section 
12.9)
Pilote, si appli­
cable
Transparence
Mode d’information des personnes; procédure de révi­
sion humaine pour les décisions visées par l’article 12.1
Pilote, si appli­
cable
Cycle de vie
État et revues
État (proposé, conception, construction, pilote, produc­
tion, suspendu, retiré); dates de mise en production, de 
dernière attestation et de prochaine revue; historique des 
versions
Proposition
Dérogations
Dérogations en vi­
gueur
Identifiant, exigence visée, mesures compensatoires, 
échéance et approbateur (section 11.6)
Dès qu’une déro­
gation existe
Exemple de fiche lisible par machine
L’exemple suivant décrit un agent fictif de classe modérée, plafonné à N3. Les noms de champs sont un 
choix du cadre; seules comptent leur présence et leur cohérence avec le gabarit.
Fiche d’agent au registre (JSON, extrait)
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 214 sur 283


---
## [Page PDF 215]

CRE-IA-2026-01 · Cadre de référence
B Gabarit de fiche d’agent
{
  "agent_id": "agt-fin-rapprochement",
  "name": "Agent de rapprochement des factures fournisseurs",
  "version": "2.3.0",
  "lifecycle_state": "production",
  "owners": {
    "business_sponsor": "Directrice, comptes fournisseurs",
    "technical_lead": "Responsable technique, plateforme Finances",
    "on_call_team": "garde-finances",
    "cost_center": "CC-4120"
  },
  "purpose": "Apparier factures, bons de commande et réceptions; préparer les paiements.",
  "excluded_uses": ["modifier les coordonnées bancaires d'un fournisseur"],
  "principals": ["role:analyste-comptes-fournisseurs", "agent:agt-fin-orchestrateur"],
  "orchestration_pattern": "agent-unique-outille",
  "risk_class": "modere",
  "autonomy": {
    "ceiling": "N3",
    "approved_by": "Directrice, comptes fournisseurs",
    "approved_on": "2027-03-15",
    "odd_ref": "ODD-FIN-007",
    "renew_on": ["model_change", "new_write_tool", "target_population_change"]
  },
  "regulatory": {"eu_ai_act_high_risk": false, "automated_decision_art_12_1": false},
  "tools": [
    {"ref": "erp.factures.lire@1.4.0", "digest": "sha256:9f2c41d0", "tier": "P1"},
    {"ref": "erp.factures.apparier@2.0.1", "digest": "sha256:51ab07e3", "tier": "P2",
     "threshold_cad": 5000, "compensation": "erp.factures.desapparier", "idempotency_key": true},
    {"ref": "tresorerie.paiements.emettre@1.1.0", "digest": "sha256:c07d9b12", "tier": "P3",
     "approval": "signed_out_of_band"}
  ],
  "data": {"classification": "confidentiel", "personal_information": true,
           "processing_locations": ["Québec"]},
  "identity": {"workload_id": "spiffe://entreprise.example/agents/agt-fin-rapprochement",
               "access_mode": "token_exchange_rfc8693", "token_ttl_s": 900},
  "budget_per_task": {"max_tokens": 50000, "max_cost_cad": 0.75,
                      "max_tool_calls": 15, "timeout_s": 60, "max_wall_clock_s": 28800,
                      "max_iterations": 8},
  "evaluation": {"reference_set": 120, "adversarial_cases": 25,
                 "last_run": "2027-03-10", "result": "pass"},
  "observability": {"service_name": "agt-fin-rapprochement",
                    "genai_semconv": "1.41.0", "content_capture": false},
  "compliance": {"efvp_ref": "EFVP-2027-014", "efvp_date": "2027-02-28"},
  "next_review": "2027-09-15",
  "exceptions": []
}
Lecture : l’agent apparie seul les factures sous 5 000 $, au-delà de quoi la passerelle exige une approbation; 
l’émission d’un paiement, de palier P3, exige toujours une approbation signée hors bande. Les valeurs de 
l’enveloppe budgétaire sont illustratives et se calibrent par mesure (section 10.6).
C Exemples de contrats
Cette annexe donne huit exemples complets de contrats et d’objets d’échange, conformes, lorsqu’elles 
existent, aux spécifications en vigueur au 27 octobre 2026 et, dans tous les cas, aux exigences du cadre. 
Ils sont normatifs par leur forme, pas par leurs valeurs : un contrat réel reprend leur structure et leurs 
champs, avec ses propres noms, schémas et seuils. Chaque exemple est suivi d’une lecture qui le rattache 
aux exigences qu’il met en œuvre.
Conventions des exemples
• Valeurs fictives. Les noms, domaines (ent.ca), identifiants et montants sont fictifs.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 215 sur 283


---
## [Page PDF 216]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
• Formats normalisés et formats internes. Les exemples C.1, C.3, C.4 et C.5 n’emploient que des 
champs définis par leur spécification ou par les mécanismes d’extension qu’elle prévoit. Les exemples 
C.2, C.6, C.7 et C.8 sont des formats internes : comme à l’annexe B, les noms de champs sont un choix 
du cadre, et seules comptent leur présence et leur cohérence.
• Empreintes vérifiables. Les empreintes definition_digest, idempotency_key, h (reprise dans 
action_sha256 et empreinte_approbation) et arguments_sha256 sont de véritables condensés SHA-256, 
calculés sur les valeurs montrées (forme canonique RFC 8785 pour les objets JSON) : on peut les recalculer. 
Les valeurs qui dépendent d’objets non montrés ou abrégés (empreinte de certificat, enregistrement 
précédent, empreinte de l’invite système, empreinte de l’enregistrement C.8) sont fictives, et les signa­
tures, qu’on ne peut pas reproduire sans la clé privée, sont abrégées par « … ».
• Scénario commun. Les exemples C.1, C.2, C.6, C.7 et C.8 suivent une même tâche  : l’agent 
agt-achats-indirects, de classe de risque modérée et plafonné à N3, crée un bon de commande de 
12 480 $, soit au-delà du seuil d’approbation de 5 000 $ fixé au catalogue pour cet outil.
Tableau 64 — Exemples de contrats, références et exigences illustrées
Exemple
Référence
Exigences et sections illustrées
C.1 Outil MCP
MCP 2026-07-28; JSON Schema 2020-12
EXIG-MCP-07, EXIG-MCP-14, EXIG-MCP-18; 
EXIG-ORC-21
C.2 Entrée de catalogue
Format interne du cadre
EXIG-AUT-08, EXIG-MCP-14, EXIG-MCP-20, 
EXIG-ORC-22; section 6.8
C.3 Carte d’agent
A2A 1.0 (a2a.proto); JWS (RFC 7515); RFC 
8785
EXIG-A2A-02 à EXIG-A2A-06, EXIG-A2A-10
C.4 Événement
CloudEvents 1.0 (1.0.2) et extensions do­
cumentées; W3C Trace Context
EXIG-EVT-02, EXIG-EVT-04 à EXIG-EVT-06, 
EXIG-EVT-09
C.5 Jeton délégué
RFC 9068, RFC 8693, RFC 8705
EXIG-IAM-08, EXIG-IAM-10, EXIG-IAM-11, 
EXIG-IAM-14, EXIG-IAM-15
C.6 Jeton d’approbation 
humaine
Format interne; RFC 8785, RFC 9396, CIBA
EXIG-AUT-12 à EXIG-AUT-14
C.7 Enveloppe budgétaire
Format interne du cadre
EXIG-ORC-26, EXIG-FIN-04; section 10.6
C.8 Enregistrement d’audit
Format interne; RFC 8785
EXIG-OBS-11, EXIG-OBS-12, EXIG-AUT-10, 
EXIG-IAM-11, EXIG-IAM-21; section 10.3
C.1 Outil MCP
L’exemple montre la définition d’un outil d’écriture orienté tâche, telle qu’un serveur MCP la renvoie dans 
tools/list (section 6.5).
Définition de l’outil approvisionnement_creer_bon_commande (MCP 2026-07-28)
{
  "name": "approvisionnement_creer_bon_commande",
  "title": "Créer un bon de commande (ERP)",
  "description": "Crée dans l'ERP un bon de commande, à l'état brouillon ou soumis, pour un fournisseur
homologué et un centre de coûts valide. Une relance avec la même clé d'idempotence ne crée pas de second bon.
Ne modifie ni n'annule un bon existant.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "idempotency_key": { "type": "string", "pattern": "^[0-9a-f]{64}$" },
      "fournisseur_id": { "type": "string", "pattern": "^SUP-[0-9]{6}$" },
      "centre_cout": { "type": "string", "pattern": "^CC-[0-9]{4}$", "x-mcp-header": "Cost-Center" },
      "statut_demande": { "type": "string", "enum": ["brouillon", "soumis"], "default": "brouillon" },
      "montant_total_cad": { "type": "number", "exclusiveMinimum": 0 },
      "lignes": {
        "type": "array",
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 216 sur 283


---
## [Page PDF 217]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
        "minItems": 1,
        "maxItems": 100,
        "items": {
          "type": "object",
          "properties": {
            "sku": { "type": "string", "pattern": "^PRD-[0-9]{5}$" },
            "quantite": { "type": "integer", "minimum": 1 },
            "prix_unitaire_cad": { "type": "number", "minimum": 0 }
          },
          "required": ["sku", "quantite", "prix_unitaire_cad"],
          "additionalProperties": false
        }
      }
    },
    "required": ["idempotency_key", "fournisseur_id", "centre_cout", "montant_total_cad", "lignes"],
    "additionalProperties": false
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "bon_commande_id": { "type": "string", "pattern": "^BC-[0-9]{4}-[0-9]{6}$" },
      "statut": { "type": "string", "enum": ["brouillon", "soumis"] },
      "montant_total_cad": { "type": "number" },
      "rejeu": { "type": "boolean", "description": "Vrai si la clé était déjà traitée." }
    },
    "required": ["bon_commande_id", "statut", "montant_total_cad", "rejeu"],
    "additionalProperties": false
  },
  "annotations": {
    "readOnlyHint": false,
    "destructiveHint": false,
    "idempotentHint": true,
    "openWorldHint": false
  }
}
Lecture  : la définition n’emploie que des champs du schéma MCP 2026-07-28; ses schémas suivent 
JSON Schema 2020-12, dialecte par défaut de la spécification, et additionalProperties: false ferme le 
contrat[162, 197]. Le motif du champ idempotency_key correspond à la dérivation de la section 7.6, et seul 
centre_cout porte x-mcp-header : le client recopie sa valeur dans l’en-tête Mcp-Param-Cost-Center, ce qui 
convient à une donnée non sensible (EXIG-MCP-18). Les annotations, conformes au schéma, ne décident de 
rien : elles doivent seulement concorder avec le palier inscrit au catalogue (EXIG-MCP-14). L’outil renvoie 
un structuredContent conforme à outputSchema, accompagné du même JSON dans un bloc texte, et signale 
une erreur métier par un résultat marqué isError: true (EXIG-MCP-07).
C.2 Entrée de catalogue de l’outil
L’exemple montre où vit la gouvernance de l’outil C.1 : dans le catalogue d’entreprise, et non dans le serveur 
(section 6.8).
Entrée du catalogue d’entreprise pour l’outil C.1 (format interne)
{
  "ref": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",
  "tool_name": "approvisionnement_creer_bon_commande",
  "contract_version": "1.4.0",
  "definition_digest": "sha256:3182dbf3bec38e95fffa2b16ae58217e0cc09251bfbe026b5939c25729f99e1e",
  "server": {
    "id": "mcp-approvisionnement",
    "endpoint": "https://passerelle-agents.ent.ca/mcp/approvisionnement",
    "mcp_revision": "2026-07-28",
    "extensions_allowed": []
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 217 sur 283


---
## [Page PDF 218]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
  },
  "lifecycle_state": "active",
  "tier": "P2",
  "approval_threshold": { "argument": "montant_total_cad", "max_without_approval_cad": 5000 },
  "compensation": "mcp-approvisionnement/approvisionnement_annuler_bon_commande@1.2.0",
  "idempotency": { "argument": "idempotency_key", "checked_by_server": true, "on_conflict": "reject" },
  "oauth_scope": "approvisionnement.bons-commande.creer",
  "header_projection": { "centre_cout": "Mcp-Param-Cost-Center" },
  "data_classification_max": "confidentiel",
  "personal_information": false,
  "owner": "Direction Approvisionnement",
  "on_call_team": "garde-plateforme-erp",
  "known_consumers": ["agt-achats-indirects"],
  "reviewed_by": ["proprietaire-outil", "securite"],
  "approved_on": "2026-10-06",
  "next_review": "2027-04-06"
}
Lecture : cette entrée porte le palier, le seuil, la compensation, la portée, le propriétaire et l’équipe de 
garde de l’outil, attribués après revue par son propriétaire et par la sécurité; la passerelle les lit ici, jamais 
dans les annotations (EXIG-AUT-08, EXIG-MCP-14). definition_digest est le SHA-256 de la définition 
C.1 canonisée selon la RFC 8785 : à chaque tools/list, la passerelle recalcule l’empreinte et retire l’outil 
au moindre écart, description comprise, jusqu’à une nouvelle approbation (EXIG-MCP-20)[221, 236]. Avec ce 
palier P2 et ce seuil, un agent de classe modérée déclaré N3 peut créer seul un bon de 5 000 $ ou moins; 
au-delà, la règle de la section 8.4 impose le jeton d’approbation de l’exemple C.6. L’idempotence déclarée 
ici, vérifiée par le serveur, fait office de garantie, alors que l’annotation idempotentHint n’en est qu’un 
indice (EXIG-ORC-22).
C.3 Carte d’agent A2A
L’exemple montre la carte publiée au registre par l’agent spécialiste du scénario de délégation de la section 
6.6.
Carte d’agent A2A 1.0 signée de l’agent d’évaluation du risque de crédit
{
  "name": "Agent d'évaluation du risque de crédit",
  "description": "Analyse un dossier de crédit commercial selon la politique CR-12 et recommande une décision
motivée. N'accorde ni ne refuse aucun crédit.",
  "supportedInterfaces": [
    {
      "url": "https://passerelle-agents.ent.ca/a2a/risque-credit",
      "protocolBinding": "JSONRPC",
      "protocolVersion": "1.0"
    }
  ],
  "provider": {
    "organization": "Direction Gestion des risques",
    "url": "https://intranet.ent.ca/risque-credit"
  },
  "version": "2.3.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": true,
    "extendedAgentCard": true,
    "extensions": [
      {
        "uri": "https://ent.ca/a2a/extensions/gouvernance/v1",
        "description": "Copie en lecture seule de données du registre : niveau d'autonomie et classe de
risque.",
        "required": false,
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 218 sur 283


---
## [Page PDF 219]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
        "params": { "niveau_autonomie": "N2", "classe_risque": "elevee" }
      }
    ]
  },
  "securitySchemes": {
    "idp-entreprise": {
      "openIdConnectSecurityScheme": { "openIdConnectUrl": "https://idp.ent.ca/.well-known/openid-
configuration" }
    }
  },
  "securityRequirements": [{ "schemes": { "idp-entreprise": { "list": ["agents.risque-credit"] } } }],
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["application/json", "text/markdown"],
  "skills": [
    {
      "id": "analyse-dossier-commercial",
      "name": "Analyse prudentielle d'un dossier de crédit commercial",
      "description": "Évalue la solvabilité d'une entreprise cliente, vérifie les garanties et produit une
recommandation motivée avec les ratios calculés.",
      "tags": ["credit", "risque", "conformite"],
      "examples": ["Analyser le dossier 8841 selon la politique CR-12"],
      "securityRequirements": [{ "schemes": { "idp-entreprise": { "list": ["risque-credit.analyser"] } } }]
    }
  ],
  "signatures": [
    {
      "protected":
"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpPU0UiLCJraWQiOiJjYXJ0ZXMtYWdlbnRzLTIwMjYtMTAiLCJqa3UiOiJodHRwczovL2NsZXMuZW50
LmNhL2EyYS9qd2tzLmpzb24ifQ",
      "signature": "Wm3k…"
    }
  ]
}
Lecture : la carte contient les huit champs obligatoires d’A2A 1.0, ses adresses sont celles de la passerelle 
d’agents, et la compétence porte sa propre portée OAuth dans securityRequirements (EXIG-A2A-02, 
EXIG-A2A-10)[68, 192]. La signature est un JWS calculé sur la carte canonisée selon la RFC 8785, champ 
signatures exclu et règles de présence des champs de la spécification (section 8.4.1) appliquées; son en-tête 
protégé, encodé en base64url, désigne le type JOSE (typ), l’algorithme ES256, la clé (kid) et le jeu de clés 
publiques de l’entreprise (jku), et tout client vérifie cette signature avant de se fier à la carte (EXIG-A2A-03). 
Le niveau d’autonomie et la classe de risque ne forment pas un champ de premier niveau  : ils sont 
déclarés comme extension de données facultative, dont l’URI versionnée figure au registre des extensions 
approuvées, et la fiche du registre fait foi en cas d’écart (EXIG-A2A-05)[238]. extendedAgentCard annonce 
une carte étendue, servie après authentification, qui ajoute les compétences réservées aux appelants internes 
(EXIG-A2A-06), et version, en SemVer, dont dérive l’ETag servi avec la carte, permet de revalider les copies 
en cache (EXIG-A2A-04).
C.4 Événement CloudEvents
L’exemple montre la première alerte d’une chorégraphie, publiée par un agent détecteur sur le bus 
d’événements (section 6.7).
Événement CloudEvents 1.0 avec les extensions exigées par le cadre (représentation JSON)
{
  "specversion": "1.0",
  "id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "source": "https://agents.ent.ca/logistique/detecteur-rupture-stock",
  "type": "ca.entreprise.logistique.alerte.rupture.v1",
  "subject": "MTL-02/PRD-99210",
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 219 sur 283


---
## [Page PDF 220]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
  "time": "2026-10-27T09:15:00Z",
  "datacontenttype": "application/json",
  "dataschema": "https://catalogue.ent.ca/schemas/logistique/alerte-rupture/1.0.0",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "authtype": "service_account",
  "authid": "ordonnanceur-inventaire-quotidien",
  "dataclassification": "internal",
  "partitionkey": "MTL-02/PRD-99210",
  "xagentorigin": "agt-detecteur-rupture@1.3.0",
  "xagenthopcount": 1,
  "xagentmaxhops": 4,
  "xcostcenter": "CC-8100",
  "data": {
    "entrepot_id": "MTL-02",
    "sku": "PRD-99210",
    "stock_actuel": 12,
    "seuil_critique": 50,
    "horizon_epuisement_heures": 18
  }
}
Lecture : l’événement porte les quatre attributs requis par CloudEvents, les attributs time, datacontenttype 
et dataschema exigés par le cadre, et un type versionné en domaine inversé (EXIG-EVT-02)[248]. traceparent 
(Distributed Tracing), authtype et authid (Auth Context), dataclassification (Data Classification) et 
partitionkey (Partitioning) sont des extensions documentées, alors que xagentorigin, xagenthopcount, 
xagentmaxhops et xcostcenter sont propres au cadre (EXIG-EVT-04); aucun attribut ne contient de rensei­
gnement personnel (EXIG-EVT-05)[187, 252, 255]. Un agent qui réagit à cette alerte publie un nouvel événement 
dont xagenthopcount vaut 2 et qui recopie xagentorigin et xagentmaxhops; un événement dont le compteur 
atteint 4 n’est pas traité et part en file de lettres mortes (EXIG-EVT-06). Sur Kafka, le mode binaire retenu 
par défaut place les attributs (sauf datacontenttype, porté par l’en-tête content-type) dans des en-têtes 
préfixés ce_ et data dans la valeur; une fois le « Key Mapper » de la liaison activé (mécanisme facultatif), 
partitionkey est recopié dans la clé du message et, comme Kafka écrit les messages de même clé dans la 
même partition et en conserve l’ordre, les alertes d’un même article dans un même entrepôt restent dans 
l’ordre (EXIG-EVT-09)[250, 468].
C.5 Jeton délégué
L’exemple complète l’extrait de la section 9.3 : le jeton que présente l’agent d’analyse des dépenses, appelé 
par l’orchestrateur, au serveur MCP des finances, au nom d’Alice.
Jeton délégué après deux sauts, décodé (signature omise)
En-tête
{ "typ": "at+jwt", "alg": "ES256", "kid": "idp-2026-10" }
Charge utile
{
  "iss": "https://idp.ent.ca",
  "sub": "alice",
  "aud": "https://mcp-finance.ent.ca",
  "client_id": "agent-analyse-depenses",
  "scope": "finance:read",
  "act": {
    "sub": "spiffe://ent.ca/agent-analyse-depenses",
    "act": { "sub": "spiffe://ent.ca/agent-orch" }
  },
  "cnf": { "x5t#S256": "vzF5VHuU_5wCN7LdQZOXTK3y7aNQCqM5M-yosaTb6aw" },
  "iat": 1793084700,
  "exp": 1793085600,
  "jti": "9f1c2d7e-5a41-4c3b-8e06-b2f94a1d7c55"
}
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 220 sur 283


---
## [Page PDF 221]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
Lecture : le jeton suit le profil JWT de la RFC 9068, avec l’en-tête typ at+jwt et les revendications iss, 
exp, aud, sub, client_id, iat et jti [72]. Alice reste le sujet; l’act externe désigne l’acteur courant, l’agent 
d’analyse des dépenses, et l’act imbriqué l’orchestrateur, acteur antérieur que le serveur consigne sans s’en 
servir pour décider (EXIG-IAM-08, EXIG-IAM-11)[70]. L’audience unique, la portée réduite à finance:read 
et la durée de vie de 900 secondes appliquent les exigences EXIG-IAM-10, EXIG-IAM-11 et EXIG-IAM-15. 
cnf lie le jeton à l’empreinte du certificat X.509-SVID de l’agent : volé, il ne sert à rien sans la clé privée 
correspondante (EXIG-IAM-14)[328].
C.6 Jeton d’approbation humaine
L’exemple montre l’action soumise à l’approbateur, le calcul de son empreinte et le jeton signé qui en résulte 
(section 8.5).
Action soumise, empreinte h et jeton d’approbation décodé (signature omise)
  h          : 9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d
En-tête
{ "typ": "approbation+jwt", "alg": "ES256", "kid": "approbation-2026-10" }
Charge utile
{
  "iss": "https://approbation.ent.ca",
  "aud": "https://passerelle-agents.ent.ca",
  "sub": "apb-5e19c2",
  "iat": 1793093040,
  "exp": 1793093940,
  "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
  "task_id": "tache-7f3c2a",
  "agent_id": "agt-achats-indirects@1.2.0",
  "action_sha256": "9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d",
  "authorization_details": [
    {
      "type": "https://ent.ca/types/action-agent",
      "locations": ["https://passerelle-agents.ent.ca/mcp/approvisionnement"],
      "actions": ["tools/call"],
      "identifier": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",
      "fournisseur_id": "SUP-004512",
      "montant_total_cad": 12480,
      "centre_cout": "CC-4410"
    }
  ]
}
Lecture : h est le SHA-256 de l’identifiant pleinement qualifié de l’outil (serveur, nom, version épinglée), 
immédiatement suivi des arguments canonisés selon la RFC 8785, dont les clés sont triées et les nombres 
normalisés (12  480,00 devient 12480)[236]. Le jeton contient le minimum exigé par l’EXIG-AUT-12  : 
l’empreinte (action_sha256), l’approbateur pseudonymisé (sub), la tâche, l’agent, une expiration à 15 
minutes et un identifiant à usage unique (jti); authorization_details décrit l’action selon la RFC 9396 
pour l’écran d’approbation et l’audit, sans remplacer l’empreinte[312]. Un typ distinct de at+jwt, choix du 
cadre, empêche de faire passer ce jeton pour un jeton d’accès, ou l’inverse. La passerelle vérifie la signature, 
l’expiration et l’usage unique, puis recalcule h sur l’appel reçu et refuse tout écart; ici, l’approbation est 
obtenue par CIBA sur l’appareil de l’approbateur (EXIG-AUT-14), et seul un tel jeton vaut approbation, 
jamais un acquiescement dans la conversation (EXIG-AUT-13)[310].
C.7 Enveloppe budgétaire de tâche
Action soumise
  outil      : mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0
  arguments  : {"centre_cout":"CC-4410","fournisseur_id":"SUP-004512",
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 221 sur 283


---
## [Page PDF 222]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
                "idempotency_key":"ce887a26e391ba96cd8c85603dd7b97beb97abffe5db0e610f2b6a8bca237edf",
                "lignes":[{"prix_unitaire_cad":249.6,"quantite":40,"sku":"PRD-10442"},
                          {"prix_unitaire_cad":208,"quantite":12,"sku":"PRD-20817"}],
                "montant_total_cad":12480,"statut_demande":"soumis"}
L’exemple montre l’enveloppe attribuée à la tâche du scénario, telle que la passerelle de modèles et 
l’orchestrateur la tiennent à jour (section 10.6).
Enveloppe budgétaire de la tâche tache-7f3c2a, état à 9 h 25 UTC (format interne)
{
  "task_id": "tache-7f3c2a",
  "agent_id": "agt-achats-indirects@1.2.0",
  "cost_center": "CC-4410",
  "issued_at": "2026-10-27T09:02:11Z",
  "limits": {
    "max_tokens": 50000,
    "max_cost_cad": 0.75,
    "max_tool_calls": 15,
    "max_iterations": 8,
    "timeout_s": 60,
    "max_wall_clock_s": 28800
  },
  "alert_ratio": 0.8,
  "on_exhaustion": { "action": "stop_and_escalate", "queue": "file-achats-exceptions" },
  "models": {
    "default": "modele-compact",
    "reasoning": "modele-raisonnement",
    "reasoning_steps": ["planification", "arbitrage"],
    "fallback": "modele-compact-repli"
  },
  "consumed": {
    "as_of": "2026-10-27T09:25:41Z",
    "tokens": 41200,
    "cost_cad": 0.52,
    "tool_calls": 9,
    "iterations": 5,
    "active_s": 38
  },
  "alerts": [
    {
      "metric": "tokens",
      "ratio": 0.824,
      "at": "2026-10-27T09:25:41Z",
      "notified": "proprietaire"
    }
  ],
  "delegations": []
}
Lecture : l’enveloppe reprend les plafonds de la fiche d’agent (annexe B) : jetons, coût, appels d’outils, 
itérations et temps d’exécution active (timeout_s); max_wall_clock_s borne en outre la durée totale, attente 
d’approbation comprise (EXIG-ORC-26). Chaque étape incrémente consumed : à 82,4 % des jetons, le seuil 
d’alerte de 80 % a déjà prévenu le propriétaire, et l’atteinte d’un plafond arrêtera la tâche en état sûr pour 
l’escalader, sans jamais la déclarer réussie (EXIG-FIN-04). Le modèle compact sert par défaut, le modèle de 
raisonnement seulement aux étapes nommées, et tout le coût s’impute au centre de coûts de la tâche. Une 
délégation à un exécutant recevrait une part de l’enveloppe restante, inscrite dans delegations, et jamais 
une enveloppe neuve (section 7.7); les valeurs sont illustratives et se calibrent par mesure.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 222 sur 283
