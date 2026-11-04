# chunk_23 — pages PDF 221 à 232 (sur 283)



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


---
## [Page PDF 223]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
C.8 Enregistrement d’audit
L’exemple montre l’enregistrement que la passerelle verse au journal d’audit après l’exécution de l’action 
approuvée en C.6 (section 10.3).
Enregistrement d’audit canonisé (clés dans l’ordre RFC 8785, présentées indentées)
{
  "empreinte": "sha256:689f1e007503a391dd58d4bdc148cbccde6c2c5a5f1578472244307110180588",
  "enregistrement": {
    "action": {
      "arguments_sha256": "cff55d8aafbb562bfb6b27ca6cec7cf38a1dfe3ee48b2410dcf1f3a04a5bdc2b",
      "definition": "1.4.0",
      "issue": "succes",
      "outil": "mcp-approvisionnement/approvisionnement_creer_bon_commande",
      "palier": "P2",
      "reference_resultat": "BC-2026-118734"
    },
    "agent": {
      "id": "agt-achats-indirects",
      "identite": "spiffe://ent.ca/agt-achats-indirects",
      "invite_systeme": "sha256:41d07c…",
      "version": "1.2.0"
    },
    "autorite": {
      "approbateur": "apb-5e19c2",
      "approbation_jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
      "classe_risque": "moderee",
      "controle": "approbation_requise_au_dela_du_seuil",
      "empreinte_approbation": "9a2c0a8c4394ceb424c47d73d17bb417439d26a488e4d93c4834d481f5dc7e9d",
      "niveau_autonomie": "N3",
      "version_politique": "politiques-passerelle@2026.10.3"
    },
    "correlation": {
      "cle_idempotence": "ce887a26e391ba96cd8c85603dd7b97beb97abffe5db0e610f2b6a8bca237edf",
      "etape": "etape-03/creer-bon-commande",
      "span_id": "b7ad6b7169203331",
      "tache": "tache-7f3c2a",
      "trace_id": "0af7651916cd43dd8448eb211c80319c"
    },
    "horodatage": "2026-10-27T09:26:03.412Z",
    "mandant": {
      "jeton_delegue_jti": "4e8b2c71-0d93-4a6f-9b15-7c2e8f40a6d3",
      "pseudonyme": "u-58c1d7",
      "type": "user"
    },
    "modele": {
      "fournisseur": "…",
      "servi": "modele-raisonnement",
      "version": "2026-08-14"
    },
    "precedent_sha256": "sha256:ee710bdb80fd80be1bce7ad8f07964c8a0dea08c5fb81f39289b26666ab4524a",
    "sequence": 48213
  },
  "signature": { "alg": "ES256", "kid": "journal-audit-2026-10", "valeur": "…" }
}
Lecture : enregistrement reprend les cinq éléments exigés par l’EXIG-OBS-12 (section 10.3) : le mandant 
sous pseudonyme (mandant), l’agent avec sa version, son identité et l’empreinte de son invite système 
(agent), l’action avec l’outil, la version de sa définition, l’empreinte des arguments et l’issue (action), le 
modèle servi (modele) et l’autorité qui permettait d’agir (autorite : politique appliquée, contrôle, niveau 
d’autonomie et jeton d’approbation, selon les EXIG-IAM-21 et EXIG-AUT-10); correlation le relie à la 
tâche, à l’étape, à la clé d’idempotence et à la trace. Il ne recopie pas les arguments, et le résultat n’y figure 
que par sa référence : empreinte_approbation reprend l’empreinte h du jeton C.6, calculée sur l’identifiant 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 223 sur 283


---
## [Page PDF 224]

CRE-IA-2026-01 · Cadre de référence
C Exemples de contrats
qualifié de l’outil (serveur, nom, version épinglée) et sur les arguments canonisés; la passerelle l’a recalculée 
avant l’exécution, ce qui prouve que l’action exécutée est bien celle qui a été approuvée. empreinte est le 
SHA-256 de enregistrement canonisé selon la RFC 8785, signé par le service d’audit, et precedent_sha256 
chaîne chaque enregistrement au précédent, de sorte qu’une suppression ou une modification se détecte, 
conformément à la recommandation de l’OWASP de tenir des journaux d’audit immuables et signés[28, 236]. 
Ce format et sa signature, choix du cadre, vont au-delà du minimum légal : pour un système à haut risque 
(obligations applicables à compter du 2 décembre 2027 pour l’annexe III et du 2 août 2028 pour l’annexe I), 
le RIA exige que le système permette l’enregistrement automatique des événements, sans en fixer le format 
(art. 12), et que le déployeur conserve les journaux, dans la mesure où ils sont sous son contrôle, pendant 
une durée adaptée à la destination du système et d’au moins six mois, sauf disposition contraire du droit de 
l’Union ou du droit national (art. 26, par. 6)[94, 394].
D Registre des exigences
Ce registre récapitule, dans l’ordre du document, toutes les exigences normatives du cadre avec leur 
force (DOIT, DEVRAIT, PEUT). Chaque identifiant renvoie à l’exigence complète, avec son énoncé et sa 
justification. Le registre sert de base aux revues d’architecture, à la grille d’homologation (annexe A) et à la 
déclaration d’applicabilité ISO/IEC 42001.
Identifiant
Force
Exigence
EXIG-ARC-01
DOIT
Passage obligatoire par la passerelle et le catalogue
EXIG-ARC-02
DOIT
Mandant, trace et plafonds dans chaque appel
EXIG-ARC-03
NE DOIT PAS
Aucune logique d’agent dans les canaux
EXIG-ARC-04
DOIT
Mandant établi et trace ouverte à l’entrée
EXIG-ARC-05
DOIT
Exécution durable des tâches à effets
EXIG-ARC-06
DOIT
Points de contrôle protégés comme des données de production
EXIG-ARC-07
NE DOIT PAS
Le routage n’accorde aucun droit
EXIG-ARC-08
DOIT
Passerelle de modèles obligatoire
EXIG-ARC-09
DEVRAIT
Modèles désignés par un alias logique
EXIG-ARC-10
DOIT
Code généré exécuté en bac à sable
EXIG-ARC-11
DOIT
Passerelle d’agents dans les deux sens
EXIG-ARC-12
DOIT
Liste d’autorisation tirée du catalogue
EXIG-ARC-13
DOIT
Aucun contournement par le bus d’événements
EXIG-ARC-14
DOIT
Exposition sans réécriture des services
EXIG-ARC-15
DEVRAIT
Outils conçus pour la tâche
EXIG-ARC-16
DOIT
Résultats filtrés selon les droits du mandant
EXIG-ARC-17
DOIT
Écriture par les interfaces qui appliquent les règles métier
EXIG-ARC-18
DEVRAIT
Écritures corrélées et idempotentes
EXIG-ARC-19
DOIT
Services transversaux mutualisés
EXIG-ARC-20
DOIT
Correspondance ABB-SBB documentée
EXIG-ARC-21
DOIT
SBB exposés par les standards retenus
EXIG-ARC-22
NE DOIT PAS
Pas d’historique brut comme mémoire
EXIG-ARC-23
DOIT
Contrôles avant toute écriture en mémoire longue
EXIG-ARC-24
DOIT
Mémoire procédurale gérée comme du code
EXIG-ARC-25
NE DOIT PAS
Aucun magasin de mémoire partagé sans isolation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 224 sur 283


---
## [Page PDF 225]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-INT-01
DOIT
Revue d’interopérabilité à quatre niveaux
EXIG-INT-02
DOIT
Vocabulaire et schémas d’entreprise
EXIG-INT-03
DOIT
Accord d’interopérabilité et gestion du changement
EXIG-INT-04
DOIT
Protocole désigné par type d’interaction
EXIG-INT-05
DEVRAIT
Agent pair invoqué par A2A, pas déguisé en outil
EXIG-INT-06
DOIT
Statut au catalogue avant tout usage en production
EXIG-INT-07
DOIT
Version de référence fixée au catalogue
EXIG-INT-08
DOIT
Révision trimestrielle du catalogue des protocoles
EXIG-INT-09
NE DOIT PAS
Statut normatif exact
EXIG-INT-10
DOIT
Choix de protocole justifié par la matrice
EXIG-INT-11
DEVRAIT
Diffusion d’un changement d’état par événement
EXIG-MCP-01
DOIT
Exposition des capacités par MCP, derrière la passerelle
EXIG-MCP-02
DOIT
Révision de référence vérifiée par la découverte
EXIG-MCP-03
DOIT
Listes stables et cache conforme à cacheScope
EXIG-MCP-04
DOIT
Extensions activées sur liste d’autorisation
EXIG-MCP-05
DEVRAIT
Choix de la primitive selon le besoin
EXIG-MCP-06
NE DOIT PAS
Aucun miroir CRUD des API
EXIG-MCP-07
DOIT
Conventions de nommage et de résultat des outils
EXIG-MCP-08
DOIT
Transport selon l’environnement
EXIG-MCP-09
DOIT
Autorisation obligatoire et conforme à la spécification
EXIG-MCP-10
DOIT
Portées minimales et élévation progressive
EXIG-MCP-11
NE DOIT PAS
Interdiction du passage de jeton
EXIG-MCP-12
DOIT
Enregistrement des clients MCP
EXIG-MCP-13
DOIT
Consentement par client des mandataires MCP
EXIG-MCP-14
DOIT
Annotations et métadonnées déclarées : de simples indices
EXIG-MCP-15
DOIT
Concordance des en-têtes et du corps
EXIG-MCP-16
DOIT
Traitement du champ _meta
EXIG-MCP-17
DOIT
État explicite protégé
EXIG-MCP-18
NE DOIT PAS
Aucune donnée sensible en en-tête
EXIG-MCP-19
DOIT
Schémas, URL et icônes : des entrées non fiables
EXIG-MCP-20
DOIT
Empreintes des définitions et isolement des serveurs
EXIG-MCP-21
NE DOIT PAS
Élicitation : ni secret ni approbation déguisée
EXIG-MCP-22
DOIT
Migration bornée et abandon des fonctions dépréciées
EXIG-A2A-01
DOIT
A2A 1.0 pour toute délégation entre agents
EXIG-A2A-02
DOIT
Carte publiée et inscrite au registre
EXIG-A2A-03
DOIT
Carte signée et vérifiée
EXIG-A2A-04
DOIT
Version de carte et revalidation du cache
EXIG-A2A-05
NE DOIT PAS
Aucun champ hors norme dans la carte
EXIG-A2A-06
DOIT
Compétences internes dans la carte étendue
EXIG-A2A-07
DOIT
Suivi des tâches longues
EXIG-A2A-08
DOIT
Version annoncée et liaisons standard
EXIG-A2A-09
DOIT
Transport chiffré et authentification à chaque requête
EXIG-A2A-10
DOIT
Autorisation par compétence et par locataire
EXIG-A2A-11
NE DOIT PAS
Flux OAuth retirés
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 225 sur 283


---
## [Page PDF 226]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-A2A-12
DOIT
Notifications push durcies
EXIG-A2A-13
DOIT
Traçage et corrélation des tâches
EXIG-A2A-14
DOIT
Compatibilité vérifiée avant inscription
EXIG-A2A-15
DEVRAIT
Migration bornée depuis la version 0.3
EXIG-EVT-01
DEVRAIT
Recours au bus pour l’asynchrone
EXIG-EVT-02
DOIT
Enveloppe CloudEvents complète
EXIG-EVT-03
DOIT
Contrat AsyncAPI au catalogue
EXIG-EVT-04
DOIT
Attributs de gouvernance présents et vérifiés
EXIG-EVT-05
NE DOIT PAS
Aucun renseignement personnel dans les attributs
EXIG-EVT-06
DOIT
Compteur de sauts et coupure des boucles
EXIG-EVT-07
DOIT
Autorisation fondée sur l’identité, pas sur les attributs
EXIG-EVT-08
DOIT
Effets réels protégés par l’idempotence
EXIG-EVT-09
DOIT
Ordre garanti par la clé de partition
EXIG-EVT-10
DOIT
Conservation des entrées et rejeu isolé
EXIG-INT-12
DOIT
Contrat complet avant l’inscription
EXIG-INT-13
DOIT
Versionnage sémantique des contrats
EXIG-INT-14
DOIT
Coexistence d’au moins 60 jours
EXIG-INT-15
DOIT
Dépendances épinglées par version et empreinte
EXIG-INT-16
DOIT
Nouvelle approbation à toute modification
EXIG-INT-17
DOIT
Catalogue unique, source de la découverte
EXIG-INT-18
DOIT
Consommateurs connus avant tout retrait
EXIG-INT-19
DOIT
Détection automatique des ruptures
EXIG-INT-20
NE DOIT PAS
Qualification « AAIF » vérifiée
EXIG-INT-21
DOIT
Pilotes AGNTCY subordonnés au catalogue
EXIG-INT-22
DOIT
Paiements initiés par un agent
EXIG-INT-23
DOIT
Signal de révision inscrit au catalogue
EXIG-ORC-01
DOIT
Configuration la plus simple justifiée
EXIG-ORC-02
DOIT
Preuve mesurée avant le multiagent
EXIG-ORC-03
DOIT
Patron déclaré au registre
EXIG-ORC-04
NE DOIT PAS
Délégation limitée à deux niveaux
EXIG-ORC-05
DOIT
Boucle évaluateur-optimiseur bornée
EXIG-ORC-06
DOIT
Clavardage de groupe encadré
EXIG-ORC-07
DOIT
Fusion déclarée et écrivain unique en parallèle
EXIG-ORC-08
DOIT
Chorégraphie sous propriétaire et saga
EXIG-ORC-09
DOIT
Surcharge d’outils traitée avant de scinder
EXIG-ORC-10
DEVRAIT
Découpage par frontières de contexte
EXIG-ORC-11
DOIT
Persistance après chaque transition
EXIG-ORC-12
DOIT
Reprise sans double effet
EXIG-ORC-13
DOIT
Magasin de points de contrôle protégé
EXIG-ORC-14
DEVRAIT
Déploiement sans interruption des exécutions longues
EXIG-ORC-15
DOIT
Saga pour toute écriture multisystème
EXIG-ORC-16
DOIT
Journal de compensation tenu avant l’action
EXIG-ORC-17
DOIT
Compensations idempotentes et métier, après réessais
EXIG-ORC-18
DOIT
Escalade après deux échecs d’une compensation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 226 sur 283


---
## [Page PDF 227]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-ORC-19
DOIT
Isolation sémantique des sagas concurrentes
EXIG-ORC-20
DOIT
Quatre tests d’injection de fautes
EXIG-ORC-21
DOIT
Clé d’idempotence sur toute écriture
EXIG-ORC-22
DOIT
Vérification de la clé par le service visé
EXIG-ORC-23
DOIT
Contexte de délégation minimal et structuré
EXIG-ORC-24
DOIT
Retour validé avant toute réutilisation
EXIG-ORC-25
DOIT
Filtrage de sécurité dans chaque agent
EXIG-ORC-26
DOIT
Plafonds sur toute exécution
EXIG-ORC-27
DOIT
Mécanismes de résilience et repli testé
EXIG-ORC-28
DOIT
Coupe-circuit exercé chaque trimestre
EXIG-ORC-29
NE DOIT PAS
Aucun anti-patron sans dérogation
EXIG-ORC-30
DOIT
Capacités démontrées avant l’inscription d’un produit
EXIG-AUT-01
DOIT
Niveau d’autonomie déclaré et appliqué
EXIG-AUT-02
DOIT
Plafond selon la classe de risque
EXIG-AUT-03
NE DOIT PAS
Autonomie non bornée interdite (NX)
EXIG-AUT-04
DOIT
Domaine de conception opérationnel (ODD), repli et arrêts pour N3 et N4
EXIG-AUT-05
DOIT
Homologation et réévaluation du niveau
EXIG-AUT-06
DOIT
Classement fondé sur les permissions effectives
EXIG-AUT-07
NE DOIT PAS
Règle d’or : pas d’exécution autonome du risque cumulé
EXIG-AUT-08
DOIT
Palier attribué au catalogue après revue
EXIG-AUT-09
NE DOIT PAS
Aucun outil P3 exécuté seul
EXIG-AUT-10
DOIT
Contrôle calculé à chaque appel
EXIG-AUT-11
DOIT
Échec en mode fermé
EXIG-AUT-12
DOIT
Jeton d’approbation lié à l’action exacte
EXIG-AUT-13
NE DOIT PAS
Ce qui n’est jamais une approbation
EXIG-AUT-14
DEVRAIT
Approbation hors bande normalisée
EXIG-AUT-15
DOIT
Approbateurs habilités et formés
EXIG-AUT-16
DOIT
Boîte de réception persistante
EXIG-AUT-17
DOIT
État persisté et effets après le point d’approbation
EXIG-AUT-18
DOIT
Réautorisation périodique des agents ambiants
EXIG-AUT-19
DOIT
Écran d’approbation fidèle à l’action
EXIG-AUT-20
DOIT
Charge d’approbation maîtrisée
EXIG-AUT-21
DOIT
Mesure de la qualité de la supervision
EXIG-AUT-22
DOIT
Décisions visées par l’article 12.1
EXIG-AUT-23
DOIT
Révision humaine significative
EXIG-IAM-01
NE DOIT PAS
Aucune confiance implicite
EXIG-IAM-02
DOIT
Une décision à chaque appel
EXIG-IAM-03
DOIT
Identité propre, distincte et non partagée
EXIG-IAM-04
DOIT
Justificatif cryptographique émis par la plateforme
EXIG-IAM-05
NE DOIT PAS
Aucun secret statique partagé
EXIG-IAM-06
NE DOIT PAS
Justificatifs hors de portée du modèle
EXIG-IAM-07
DOIT
Révocation au retrait et revues périodiques
EXIG-IAM-08
DOIT
Délégation explicite par échange de jetons
EXIG-IAM-09
NE DOIT PAS
Interdiction de l’usurpation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 227 sur 283


---
## [Page PDF 228]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-IAM-10
DOIT
Portée jamais élargie
EXIG-IAM-11
DOIT
Jeton à audience unique, validé par la cible
EXIG-IAM-12
NE DOIT PAS
Aucun relais de jeton
EXIG-IAM-13
DOIT
Profil OAuth de l’entreprise
EXIG-IAM-14
DOIT
Jetons liés à l’expéditeur
EXIG-IAM-15
DEVRAIT
Durée de vie courte des jetons
EXIG-IAM-16
DOIT
Agents autonomes : identifiants du client et portées par outil
EXIG-IAM-17
DOIT
Passage obligatoire par la passerelle d’agents
EXIG-IAM-18
DOIT
Échec en mode fermé et refus typé
EXIG-IAM-19
DEVRAIT
Justificatifs en aval injectés par la passerelle
EXIG-IAM-20
DOIT
Coupe-circuit propagé et mesuré
EXIG-IAM-21
DOIT
Politique en code, versionnée et testée
EXIG-SEC-01
DOIT
Modélisation des menaces avant la production
EXIG-SEC-02
DOIT
Matrice de traçabilité des menaces
EXIG-SEC-03
DOIT
Présomption d’injection
EXIG-SEC-04
DOIT
Règle de deux par session
EXIG-SEC-05
NE DOIT PAS
Détection jamais seule
EXIG-SEC-06
DOIT
Retrait déterministe des capacités d’exfiltration
EXIG-SEC-07
DOIT
Patron de conception pour les agents de risque élevé
EXIG-SEC-08
DOIT
Technologie d’isolation du code non fiable
EXIG-SEC-09
DOIT
Bac à sable éphémère et minimal
EXIG-SEC-10
DOIT
Charges qui exigent un GPU
EXIG-SEC-11
DEVRAIT
Performance mesurée sur la charge réelle
EXIG-SEC-12
DOIT
Sortie réseau refusée par défaut
EXIG-SEC-13
DOIT
Service de métadonnées infonuagiques
EXIG-SEC-14
NE DOIT PAS
Secrets injectés par le mandataire de sortie
EXIG-SEC-15
DOIT
Délais à trois niveaux
EXIG-SEC-16
DOIT
Journal d’exécution tenu hors du bac à sable
EXIG-SEC-17
DOIT
Porte de validation du code généré
EXIG-SEC-18
DOIT
Provenance approuvée et intégrité vérifiée à l’exécution
EXIG-SEC-19
DOIT
Signature des cartes d’agent et des artefacts
EXIG-SEC-20
DOIT
Nomenclature de chaque version d’agent
EXIG-SEC-21
DOIT
Chaque serveur, un domaine de sécurité distinct
EXIG-SEC-22
DOIT
Évaluation des tiers et plan de contingence
EXIG-SEC-23
DOIT
Exercice d’équipe rouge propre aux agents
EXIG-SEC-24
DOIT
Suite d’attaques dans la chaîne d’intégration
EXIG-SEC-25
DOIT
Vérification des contrôles déterministes
EXIG-SEC-26
DOIT
Exercice trimestriel de compromission d’agent
EXIG-OBS-01
DOIT
OpenTelemetry obligatoire, conventions épinglées
EXIG-OBS-02
DOIT
Contexte validé, poursuivi ou redémarré aux frontières
EXIG-OBS-03
DOIT
Identifiants métier portés à part
EXIG-OBS-04
DOIT
Hiérarchie de spans normalisée
EXIG-OBS-05
DOIT
Attributs et métriques exigés
EXIG-OBS-06
DOIT
Attributs d’entreprise sous préfixe DNS inversé
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 228 sur 283


---
## [Page PDF 229]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-OBS-07
NE DOIT PAS
Aucun contenu dans la télémétrie de production
EXIG-OBS-08
DOIT
Contenu de débogage hors trace et de courte durée
EXIG-OBS-09
DOIT
Caviardage à la sortie du périmètre
EXIG-OBS-10
NE DOIT PAS
Aucun renseignement personnel dans le bagage
EXIG-OBS-11
DOIT
Journal d’audit distinct et exhaustif
EXIG-OBS-12
DOIT
Enregistrement à cinq éléments, canonisé et signé
EXIG-OBS-13
DOIT
Inaltérabilité et conservation
EXIG-EVA-01
DOIT
Paliers franchis et relancés à chaque changement
EXIG-EVA-02
DOIT
Jeu de référence tenu et versionné
EXIG-EVA-03
DOIT
Évaluations répétées et isolées
EXIG-EVA-04
DOIT
Échantillonnage de la production
EXIG-EVA-05
DOIT
Juge automatisé encadré
EXIG-EVA-06
DOIT
Objectifs de niveau de service et réaction aux écarts
EXIG-FIN-01
DOIT
Comparaison au coût par tâche réussie
EXIG-FIN-02
DOIT
Hypothèses de prix datées et révisées
EXIG-FIN-03
DOIT
Unités SaaS converties et plafonnées
EXIG-FIN-04
DOIT
Enveloppe appliquée à chaque étape
EXIG-FIN-05
DOIT
Quotas et plafond mensuel par agent
EXIG-FIN-06
DOIT
Plus petit modèle suffisant
EXIG-FIN-07
DOIT
Préfixe stable et cache mesuré
EXIG-FIN-08
DEVRAIT
Lots asynchrones pour les charges non urgentes
EXIG-FIN-09
DOIT
Imputation par centre de coûts
EXIG-FIN-10
DOIT
Indicateurs d’économie unitaire publiés
EXIG-GOV-01
DOIT
Responsables nommés pour chaque agent
EXIG-GOV-02
DOIT
Comité d’architecture et des risques agentiques
EXIG-GOV-03
NE DOIT PAS
Séparation des fonctions
EXIG-GOV-04
DOIT
Un seul A, des personnes nommées
EXIG-GOV-05
DOIT
Socle commun obligatoire
EXIG-GOV-06
DEVRAIT
Conformité par construction
EXIG-GOV-07
DOIT
Inventaire complet
EXIG-GOV-08
NE DOIT PAS
Sans fiche, aucun justificatif
EXIG-GOV-09
DOIT
Fiche à jour ou agent suspendu
EXIG-GOV-10
DOIT
Détection des agents hors registre
EXIG-GOV-11
DOIT
Points de contrôle consignés
EXIG-GOV-12
DOIT
Réévaluation sur changement significatif
EXIG-GOV-13
DOIT
Attestation périodique du parrain
EXIG-GOV-14
DOIT
Retrait vérifiable
EXIG-GOV-15
DOIT
Demande et décision écrites
EXIG-GOV-16
DOIT
Durée bornée
EXIG-GOV-17
NE DOIT PAS
Exigences non dérogeables
EXIG-GOV-18
DOIT
Révision trimestrielle du catalogue
EXIG-GOV-19
DOIT
Critères d’admission d’un standard
EXIG-GOV-20
DOIT
Veille désignée et usage encadré
EXIG-CON-01
DOIT
Classe de risque attribuée avant l’inscription
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 229 sur 283


---
## [Page PDF 230]

CRE-IA-2026-01 · Cadre de référence
D Registre des exigences
Identifiant
Force
Exigence
EXIG-CON-02
DOIT
Plafond d’autonomie par classe
EXIG-CON-03
DOIT
Réévaluation à chaque changement significatif
EXIG-CON-04
DOIT
EFVP avant tout projet d’agent impliquant des RP
EXIG-CON-05
DOIT
Cartographie des lieux de traitement
EXIG-CON-06
DOIT
Finalité vérifiée avant toute réutilisation
EXIG-CON-07
DOIT
Avis et explication des décisions automatisées
EXIG-CON-08
NE DOIT PAS
Aucune approbation nominale
EXIG-CON-09
DOIT
Conservation des éléments de décision
EXIG-CON-10
DOIT
Durée de vie des mémoires et des traces
EXIG-CON-11
DOIT
Régimes applicables inscrits à la fiche
EXIG-CON-12
DOIT
Arrimage à E-23 pour les institutions financières fédérales
EXIG-CON-13
DOIT
Applicabilité du RIA déterminée par l’usage des sorties
EXIG-CON-14
NE DOIT PAS
Aucun usage interdit
EXIG-CON-15
DOIT
Revue de requalification en fournisseur
EXIG-CON-16
DOIT
Obligations du déployeur d’un agent à haut risque
EXIG-CON-17
DOIT
Déclaration de tolérance au risque
EXIG-CON-18
DOIT
Base de preuves unique
EXIG-CON-19
DOIT
Divulgation de l’interaction avec un agent
EXIG-CON-20
DOIT
Identification des contenus produits par un agent
EXIG-CON-21
DOIT
Explication intelligible et canal de révision
EXIG-CON-22
DOIT
Vérification humaine du contenu juridique
EXIG-CON-23
DOIT
Réponse en cinq temps et gel des preuves
EXIG-CON-24
DOIT
Registre et avis des incidents de confidentialité
EXIG-CON-25
DOIT
Règle la plus exigeante entre régimes de notification
EXIG-CON-26
DOIT
Évaluation d’impact unifiée par agent de classe élevée
EXIG-APP-01
DOIT
Analyse de réversibilité avant tout engagement
EXIG-APP-02
NE DOIT PAS
Aucune dépendance à une extension non approuvée
EXIG-APP-03
DOIT
Preuves de conformité protocolaire
EXIG-APP-04
DOIT
Mesures de performance reproductibles
EXIG-APP-05
DOIT
Télémétrie et données de coûts ouvertes
EXIG-APP-06
DOIT
Identité et arrêt sous le contrôle de l’entreprise
EXIG-APP-07
DOIT
Clause 1 — Interopérabilité ouverte et portabilité des cartes
EXIG-APP-08
DOIT
Clause 2 — Conformité MCP et délégation d’identité
EXIG-APP-09
DOIT
Clause 3 — Télémétrie exportable et explicabilité
EXIG-APP-10
DOIT
Clause 4 — Usage limité au mandat et interdiction d’entraînement
EXIG-APP-11
DOIT
Clause 5 — Résidence, transferts et lois étrangères
EXIG-APP-12
DOIT
Clause 6 — Notification d’incident
EXIG-APP-13
DOIT
Clause 7 — Audit, sécurité et transparence des changements
EXIG-APP-14
DOIT
Clause 8 — Réversibilité et sortie
EXIG-APP-15
DOIT
Clause 9 — Accord écrit au sens de l’article 25(4) du RIA
EXIG-APP-16
DOIT
Clause 10 — Révocation des identités non humaines
EXIG-APP-17
DOIT
Application de la grille
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 230 sur 283


---
## [Page PDF 231]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
E Glossaire
Ce glossaire réunit, par ordre alphabétique, les termes et les sigles du cadre, avec leur équivalent anglais 
d’usage courant et une définition brève qui renvoie à la section où chacun est traité. Les définitions 
reprennent le sens que le document donne à chaque terme; lorsqu’un terme vient d’une norme ou d’un texte 
de loi, la source est indiquée, et ce que le cadre y ajoute est signalé comme un choix du cadre. En cas d’écart 
entre une définition abrégée et le corps du document, le corps du document prévaut.
Conventions
• Classement. Les entrées suivent l’ordre alphabétique du terme français, sans tenir compte des accents, 
des apostrophes ni du contenu des parenthèses. Un sigle d’usage courant suit le terme entre parenthèses; 
les sigles et les noms propres sans équivalent français (par exemple A2A, AAIF, CIBA, CloudEvents, 
FinOps, MCP, OAuth, OBO, OpenTelemetry, SPIFFE) sont classés tels quels.
• Typographie. L’équivalent anglais figure en italique. Les noms de champs, de méthodes, d’en-têtes et 
d’attributs sont en police à chasse fixe.
• Force normative. Le glossaire ne crée aucune exigence. Les mots doit, devrait et peut gardent le sens 
fixé à la section 1.4, et les définitions normatives des termes de base figurent à la section 3.1.
Tableau 65 — Glossaire des termes et des sigles du cadre
Terme (sigle)
Équivalent anglais
Définition
A2A (protocole 
Agent2Agent)
Agent2Agent (A2A) protocol
Protocole ouvert d’intégration horizontale qui relie un agent à un 
autre agent autonome, potentiellement opaque, qui raisonne et 
conserve un état sur plusieurs tours. Projet de l’AAIF, annoncé publi­
quement le 17 août 2026, il est retenu par le cadre dans sa version 
de protocole 1.0, avec trois liaisons standard (JSON-RPC, gRPC, 
HTTP+JSON) et l’en-tête A2A-Version à chaque requête[5, 68]. Voir la 
section 6.6.
AAIF
Agentic AI Foundation
Fonds dirigé de la Linux Foundation, créé le 9 décembre 2025 et 
cofondé par Anthropic, Block et OpenAI, qui héberge des projets 
agentiques sous gouvernance neutre, dont MCP, A2A, agentgateway 
et Agent Router; il en compte dix au 22 octobre 2026[4, 130, 193]. Un 
projet n’est un « standard AAIF » qu’une fois son admission approu­
vée et annoncée. Voir la section 6.9.
Agent
AI agent
Selon ISO/IEC 22989:2022 (3.1.1), entité automatisée qui perçoit son 
environnement, y réagit et agit pour atteindre ses buts[59]. Dans le 
cadre : système logiciel qui poursuit un objectif en dirigeant lui-
même sa boucle « raisonner, agir, observer » (ReAct) au moyen d’un 
modèle, d’outils et d’un état, sous un niveau d’autonomie déclaré[84]. 
Un agent n’est ni une personne, ni un compte d’utilisateur, ni un 
principal de service partagé; une personne nommée en répond. Voir 
les sections 3.1 et 3.4.
Agent ambiant
ambient agent
Agent qui écoute un flux d’événements et agit en conséquence, 
éventuellement sur plusieurs événements à la fois, sans être néces­
sairement entièrement autonome (définition de LangChain)[86]. Il tra­
vaille en arrière-plan, à la différence d’un agent interactif, sollicité par 
une personne qui attend sa réponse, et rejoint les personnes par une 
boîte de réception persistante (notifier, questionner, réviser). Voir les 
sections 3.3 et 8.6.
Analyse d’impact sur 
les droits fondamen­
taux (AIDF)
fundamental rights impact 
assessment (FRIA)
Analyse que l’article 27 du RIA exige de certains déployeurs de sys­
tèmes à haut risque avant la première utilisation; elle peut renvoyer 
aux sections pertinentes de l’analyse d’impact relative à la protection 
des données (AIPD) du Règlement général sur la protection des 
données (RGPD) ou en intégrer des parties[58, 61]. Le cadre l’intègre à 
l’évaluation d’impact unifiée de chaque agent de classe élevée. Voir 
la section 12.9.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 231 sur 283


---
## [Page PDF 232]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Annotation d’outil
tool annotation
Métadonnée qu’un serveur MCP déclare sur un outil : un titre (title) 
et quatre indices (readOnlyHint, destructiveHint, idempotentHint, 
openWorldHint). La spécification demande aux clients de tenir les 
annotations pour non fiables, sauf si elles proviennent de serveurs 
de confiance[197]. Le palier, le seuil et la compensation d’un outil se 
lisent au catalogue d’entreprise, jamais dans ses annotations. Voir la 
section 6.5.
Approbation humaine
human approval
Décision explicite d’une personne habilitée qui autorise une action 
précise avant son exécution. Dans le cadre, elle prend la forme d’un 
jeton d’approbation signé, lié à l’action exacte et vérifié par la passe­
relle d’agents. Un acquiescement dans la conversation, un résumé 
rédigé par l’agent ou une confirmation locale dans son interface n’en 
sont jamais une. Voir la section 8.5.
Approbation machinale
rubber-stamping
Approbation donnée sans examen réel, sous l’effet du volume, de 
la fatigue ou du biais d’automatisation, soit la tendance à se fier 
excessivement à une sortie automatisée. L’OWASP (Open Worldwide 
Application Security Project) range la saturation délibérée des appro­
bateurs parmi les menaces (T10, Overwhelming Human in the Loop)
[87]. Le cadre la prévient par des files priorisées selon le risque et par 
la mesure du taux d’approbation sans modification. Voir la section 
8.7.
AsyncAPI
AsyncAPI
Spécification ouverte qui décrit de façon lisible par machine les 
canaux, les opérations d’envoi (send) ou de réception (receive) et les 
messages d’une application asynchrone. Le cadre retient la version 
3.x (3.0.0 du 5 décembre 2023; 3.1.0 du 31 janvier 2026, version 
mineure sans rupture) pour le contrat de chaque sujet du bus 
d’événements[174, 249]. Voir la section 6.7.
Bac à sable
sandbox
Environnement d’exécution isolé, éphémère et sans privilèges où 
s’exécute le code qu’un agent génère ou reçoit d’une source non 
fiable : microVM (Firecracker, Kata Containers), gVisor ou WebAs­
sembly (WASI), jamais un conteneur à noyau partagé (choix du 
cadre). Il démarre sans accès réseau, ne contient aucun secret, ap­
plique des délais à trois niveaux et est journalisé de l’extérieur. Voir 
la section 9.7.
Bloc de construction 
d’architecture (ABB) et 
de solution (SBB)
architecture building block; 
solution building block
Notions de TOGAF : l’ABB capture les exigences d’architecture et 
oriente le développement des SBB; le SBB est le produit ou le com­
posant qui met en œuvre la fonction et dépend du fournisseur[121]. 
Dans le cadre, la passerelle d’agents est un ABB neutre et durable; le 
produit qui la réalise est un SBB remplaçable. Voir la section 5.4.
Bus d’événements
event bus; event broker
Courtier qui transporte des événements entre producteurs et 
consommateurs qui s’ignorent, par exemple Apache Kafka. Il dé­
couple les échanges dans le temps, admet plusieurs abonnés et 
permet le rejeu des entrées, mais Kafka livre par défaut « au moins 
une fois »[140] : un effet réel n’est protégé que par l’idempotence du 
consommateur et du système cible. Voir la section 6.7.
Cadriciel
framework; agent framework
Bibliothèque logicielle qui structure la logique d’un agent ou d’une 
orchestration, par exemple LangGraph, Microsoft Agent Framework, 
Google ADK ou OpenAI Agents SDK. Le cadre le traite comme 
un bloc de solution remplaçable : entre agents, seuls les contrats 
publiés font foi. Voir la section 7.10.
Carte d’agent
Agent Card
Document JSON par lequel un agent A2A déclare son identité, 
ses compétences, ses interfaces et ses exigences de sécurité. En 
A2A 1.0, elle compte huit champs obligatoires (name, description, 
supportedInterfaces, version, capabilities, defaultInputModes, 
defaultOutputModes, skills), et un agent exposé la publie à 
/.well-known/agent-card.json [68]. Le cadre exige qu’elle soit signée 
(JWS sur la carte canonisée JCS), versionnée selon SemVer et inscrite 
au registre. Voir la section 6.6 et l’annexe C.
Catalogue d’entreprise
enterprise catalog
Source unique de ce qu’un agent peut joindre : outils, serveurs MCP, 
cartes d’agent et contrats d’événements, chacun avec sa version et 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 232 sur 283
