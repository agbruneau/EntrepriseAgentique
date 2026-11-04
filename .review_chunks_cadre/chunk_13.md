# chunk_13 — pages PDF 121 à 132 (sur 283)



---
## [Page PDF 121]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
EXIG-IAM-06 · NE DOIT PAS
Justificatifs hors de portée du modèle
Le modèle NE DOIT PAS avoir accès aux justificatifs de l’agent : aucun jeton, certificat ni secret n’entre 
dans le contexte du modèle, dans la mémoire de l’agent, dans les arguments d’un outil ou dans les traces. 
Les jetons sont manipulés par le code d’exécution de l’agent ou injectés par la passerelle (EXIG-IAM-19).
Pourquoi : le brouillon AIMS l’interdit[93]; un modèle qui voit un jeton peut être amené, par injection d’instructions, 
à le divulguer.
Retirer et révoquer
Une identité oubliée reste une porte ouverte. Le livre blanc de l’OpenID Foundation sur l’identité des agents 
(annoncé le 7 octobre 2025) recommande un retrait formel des agents, par exemple une opération DELETE 
du protocole SCIM (System for Cross-domain Identity Management) propagée aux systèmes raccordés[311, 325]. 
Le NIST AI RMF prévoit des processus de déclassement sécuritaire des systèmes d’IA (GOVERN 1.7), dont 
le cadre fait découler la révocation des identifiants[74]. Microsoft recommande que les parrains attestent 
tous les 6 à 12 mois que chaque agent est encore requis et que les agents orphelins soient revus chaque 
trimestre[92].
EXIG-IAM-07 · DOIT
Révocation au retrait et revues périodiques
Le retrait d’un agent DOIT révoquer son identité, ses justificatifs, ses jetons actifs et ses délégations, 
dans un délai maximal fixé par l’entreprise et mesuré en exercice, puis propager la suppression aux 
systèmes raccordés. Le parrain atteste au moins tous les 12 mois (tous les 6 mois pour un agent de classe 
de risque élevée) que l’agent est encore requis. Une revue trimestrielle détecte les agents orphelins (sans 
parrain, sans fiche à jour ou inactifs), qui sont désactivés (section 11.5).
Pourquoi : le retrait inadéquat est le premier risque du classement OWASP (NHI1)[91]. Les périodicités sont des choix 
du cadre, inscrits dans la plage recommandée par Microsoft.
Le tableau 34 rattache chacun des dix risques de l’OWASP Non-Human Identities Top 10 (2025) aux 
exigences de ce chapitre. La correspondance avec le Top 10 des applications agentiques (ASI) est traitée à 
la section 9.5.
Tableau 34 — Risques de l’OWASP Non-Human Identities Top 10 (2025) et réponse du cadre
Risque OWASP
Ce qui se passe
Réponse du cadre
NHI1 Retrait inadéquat (Improper Offboar­
ding)
L’agent retiré garde des accès valides.
EXIG-IAM-07; cycle de vie (sec­
tion 11.5)
NHI2 Fuite de secrets (Secret Leakage)
Une clé apparaît dans le code, une trace ou 
une réponse du modèle.
EXIG-IAM-05, EXIG-IAM-06, 
EXIG-IAM-19
NHI3 Identités de tiers vulnérables (Vulne­
rable Third-Party NHI)
Un fournisseur détient des accès étendus et 
mal protégés.
EXIG-IAM-17; 
chaîne d’approvisionnement (sec­
tion 9.8); clauses (section 13.3)
NHI4 Authentification non sécurisée (Inse­
cure Authentication)
Octrois obsolètes, secrets partagés, absence 
de preuve de possession.
EXIG-IAM-04, EXIG-IAM-13, 
EXIG-IAM-14
NHI5 Identités surprivilégiées (Overprivile­
ged NHI)
L’agent possède plus de droits que ses 
tâches n’en exigent.
EXIG-IAM-10, EXIG-IAM-16
NHI6 Configurations infonuagiques non sé­
curisées (Insecure Cloud Deployment Confi­
gurations)
Justificatifs exposés par la configuration du 
déploiement.
EXIG-IAM-04 (identité fédérée); 
cloisonnement (section 9.7)
NHI7 Secrets de longue durée (Long-Lived 
Secrets)
Un secret volé reste exploitable des mois du­
rant.
EXIG-IAM-04, EXIG-IAM-05, 
EXIG-IAM-15
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 121 sur 283


---
## [Page PDF 122]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Risque OWASP
Ce qui se passe
Réponse du cadre
NHI8 Isolation des environnements (Environ­
ment Isolation)
Le même justificatif sert en essai et en pro­
duction.
EXIG-IAM-04 (isolation par envi­
ronnement)
NHI9 Réutilisation d’identités (NHI Reuse)
Plusieurs agents partagent une identité; 
l’audit devient ambigu.
EXIG-IAM-03, EXIG-IAM-16
NHI10 Usage humain d’identités non hu­
maines (Human Use of NHI)
Une personne se sert de l’identité d’un agent 
pour agir.
EXIG-IAM-03
Source : liste et intitulés de l’OWASP[91]; traduction et correspondance : cadre.
9.3 Délégation : agir au nom d’une personne
Cette section règle le cas le plus fréquent et le plus délicat : un agent qui agit pour une personne. L’objectif 
est double : que chaque système appelé sache à la fois qui demande et qui agit, et que l’agent ne puisse 
jamais faire plus que ce que la personne pourrait faire elle-même.
Le risque visé porte un nom : l’adjoint confus (confused deputy). Un agent doté de droits étendus exécute la 
demande d’une personne qui en a moins et lui procure ainsi, indirectement, ce qu’elle n’aurait pas pu obtenir 
seule. La spécification MCP le signale explicitement pour les mandataires MCP[208]. La parade consiste à 
faire porter par chaque appel l’identité du mandant et celle de l’agent, puis à calculer les droits à partir 
des deux.
Échange de jetons et chaîne d’acteurs
La norme de référence est l’échange de jetons OAuth 2.0 (RFC 8693, janvier 2020). Dans 
la requête, subject_token (le jeton du mandant) est obligatoire; actor_token (le justificatif de 
l’agent) et requested_token_type sont facultatifs, actor_token_type devenant obligatoire en présence 
d’actor_token. La revendication may_act exprime qu’une partie est autorisée à agir pour une autre; le 
serveur d’autorisation peut s’en servir pour accepter ou refuser une délégation[70].
Dans le jeton émis, la revendication act est un objet JSON, et non une simple chaîne. Des act imbriqués 
représentent une chaîne  : l’act le plus externe désigne l’acteur courant, les act imbriqués les acteurs 
antérieurs. La RFC précise que seuls les attributs de premier niveau et l’acteur courant servent aux décisions 
d’accès; les acteurs antérieurs sont informatifs. Elle laisse aussi l’émission d’act à la discrétion du serveur 
d’autorisation : c’est donc le cadre qui l’exige[70].
La RFC distingue la délégation, où l’acteur conserve une identité distincte et agit pour le mandant, de 
l’usurpation (impersonation), où l’acteur devient indiscernable du mandant[69]. Le livre blanc de l’OpenID 
Foundation recommande de remplacer l’usurpation par une autorité déléguée explicite, dans des jetons qui 
identifient à la fois l’utilisateur et l’agent, et d’atténuer la portée à chaque saut[311]. Le système cible exécute 
donc la requête au nom de la personne, l’agent restant identifié comme acteur courant.
« On-Behalf-Of » (OBO) désigne un patron de délégation, pas une norme. Le flux OBO de Microsoft Entra, 
par exemple, ne repose pas sur la RFC 8693, mais sur l’octroi urn:ietf:params:oauth:grant-type:jwt-bearer 
avec requested_token_use=on_behalf_of [326]. Le cadre exige donc un résultat (jeton délégué, audience 
restreinte, portée réduite, mandant et acteur identifiables) et nomme la RFC 8693 comme référence; chaque 
variante de fournisseur est profilée au catalogue.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 122 sur 283


---
## [Page PDF 123]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Alice
utilisatrice (mandante)
Agent orchestrateur
identité SPIFFE propre
Fournisseur d’identité
serveur d’autorisation
Passerelle d’agents
point d’application
Serveur MCP finance
et système cible
1
demande + jeton d’Alice
2
échange de jetons (RFC 8693)
subject_token = jeton d’Alice
actor_token = SVID de l’agent
resource = mcp-finance
3
jeton délégué signé, durée courte
4
appel d’outil MCP + jeton délégué + traceparent
5
vérifie signature,
audience, portée,
droits effectifs
6
exécution sous l’identité d’Alice
filtrage par ligne
Revendications du jeton délégué (étape 3)
{ "sub": "alice",
"act": { "sub": "spiffe://ent.ca/agent-orch" },
"aud": "https://mcp-finance.ent.ca",
"scope": "finance:read",
"exp": 1793085600, "cnf": { … } }
sub = mandant humain · act = agent qui agit (imbriqué à chaque saut)
aud = un seul serveur · cnf = jeton lié à une clé (mTLS ou DPoP)
Droits effectifs = intersection des trois ensembles
Droits
d’Alice
Portée de
l’agent
Portée de la tâche
∩
Chaque saut conserve
ou réduit la portée;
jamais il ne l’élargit.
Figure 17 — Délégation par échange de jetons et droits effectifs. L’orchestrateur échange le jeton d’Alice contre un jeton délégué 
à audience unique (étapes 2 et 3), que la passerelle vérifie avant l’appel (étape 5); le serveur cible agit au nom d’Alice, l’agent 
restant identifié comme acteur courant (étape 6). Les droits effectifs ne dépassent jamais l’intersection des trois ensembles. Source : 
CRE-IA-2026-01, d’après la RFC 8693 et la RFC 9068.
La figure 17 illustre le premier échange. Lorsqu’un sous-agent appelé par A2A doit à son tour appeler un 
outil, il refait un échange : son subject_token est le jeton délégué reçu, son actor_token est son propre 
JWT-SVID (un X.509-SVID sert plutôt à l’authentification mTLS du client, la RFC 8693 ne définissant aucun 
type de jeton pour un certificat). Le jeton obtenu conserve le mandant et ajoute un niveau d’act, comme 
dans l’extrait suivant (l’exemple complet figure à l’annexe C).
Jeton délégué après deux sauts (extrait)
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
  "cnf": { "x5t#S256": "…" },
  "iat": 1793084700, "exp": 1793085600, "jti": "9f1c…"
}
EXIG-IAM-08 · DOIT
Délégation explicite par échange de jetons
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 123 sur 283


---
## [Page PDF 124]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Lorsqu’un agent agit pour une personne, il DOIT obtenir, à chaque saut, un jeton délégué par échange 
de jetons conforme à la RFC 8693 : subject_token égal au jeton du mandant ou au jeton délégué reçu, 
actor_token égal au justificatif de l’agent. Le jeton émis porte sub (le mandant) et act (l’agent courant), 
avec un act imbriqué par acteur antérieur. Avant d’émettre, le serveur d’autorisation DOIT vérifier 
que l’agent est autorisé à agir pour ce mandant (may_act ou politique équivalente) et que la profondeur 
d’imbrication de act ne dépasse pas deux niveaux (EXIG-ORC-04). Une variante de fournisseur est 
admise si son profil, inscrit au catalogue, démontre le même résultat.
Pourquoi : la RFC 8693 rend act facultatif[70]; le cadre l’exige pour que chaque appel désigne à la fois la personne 
et l’agent.
EXIG-IAM-09 · NE DOIT PAS
Interdiction de l’usurpation
Un agent NE DOIT PAS usurper l’identité d’une personne : aucun jeton ne présente l’agent comme 
s’il était le mandant, et aucun agent ne réutilise le jeton, la session ou le mot de passe d’une personne.
Pourquoi : un appel usurpé efface l’agent de la piste d’audit et lui donne tous les droits de la personne[69, 311].
Droits effectifs : une intersection, jamais une addition
Microsoft définit la permission effective d’une application déléguée comme l’intersection de ce que 
l’utilisateur peut faire et de ce que l’application est autorisée à faire[96]. Le cadre y ajoute un troisième terme, 
la portée de la tâche (choix du cadre) : droits effectifs = droits du mandant ∩ portée de l’agent ∩ portée de 
la tâche. Exemple : Alice peut lire et approuver les factures de son unité; l’agent d’analyse ne détient que 
finance:read; la tâche porte sur les dépenses du troisième trimestre. Le jeton délégué permet donc de lire 
les dépenses du troisième trimestre de l’unité d’Alice, et rien d’autre.
Comme la RFC 8693 interdit de fonder une décision d’accès sur les acteurs antérieurs, cette intersection ne 
peut pas être recalculée par le serveur de ressources à partir des act imbriqués : elle s’applique au serveur 
d’autorisation, à chaque échange[70]. Lorsqu’une portée manque, MCP prévoit que le serveur réponde 403 
avec error="insufficient_scope" et que le client demande une autorisation incrémentale, avec un nombre 
limité de tentatives[209] : l’agent démarre avec peu de droits et en obtient davantage par une demande 
traçable.
EXIG-IAM-10 · DOIT
Portée jamais élargie
À chaque échange, le serveur d’autorisation DOIT émettre une portée au plus égale à l’intersection 
des droits du mandant, de la portée accordée à l’agent au registre et de la portée nécessaire à la tâche. 
Une portée ne s’élargit jamais d’un saut à l’autre. Une portée manquante s’obtient par une demande 
incrémentale explicite, journalisée et limitée en nombre de tentatives, jamais par un jeton plus large 
obtenu d’avance.
Pourquoi : l’atténuation de la portée à chaque saut est recommandée par l’OpenID Foundation[311]; la formule à trois 
termes est un choix du cadre.
EXIG-IAM-11 · DOIT
Jeton à audience unique, validé par la cible
Tout jeton d’accès présenté par un agent à un outil, à une ressource ou à un autre agent DOIT viser 
une seule ressource (paramètre resource de la RFC 8707 ou audience de la RFC 8693) et suivre le profil 
JWT de la RFC 9068 (typ at+jwt; iss, exp, aud, sub, client_id, iat et jti présents). Le serveur de 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 124 sur 283


---
## [Page PDF 125]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
ressources rejette tout jeton dont aud ne le désigne pas, fonde sa décision sur sub et sur l’acteur courant 
seulement, et journalise les deux; les acteurs antérieurs servent à l’audit.
Pourquoi : un jeton à audience unique ne vaut rien ailleurs s’il est volé[71, 72]; la RFC 9068 ne définit pas act, qui 
relève de la RFC 8693.
EXIG-IAM-12 · NE DOIT PAS
Aucun relais de jeton
Un agent, un outil ou un serveur MCP NE DOIT PAS transmettre tel quel à un autre service un jeton 
qu’il a reçu (token passthrough), sauf au serveur d’autorisation, à titre de subject_token d’un échange 
de jetons (EXIG-IAM-08); il obtient un nouveau jeton pour chaque audience.
Pourquoi : la spécification d’autorisation MCP l’interdit, le brouillon AIMS le qualifie d’antipatron[93, 209].
Profil OAuth de l’entreprise
Au 27 octobre 2026, OAuth 2.1 n’est pas une RFC : c’est un Internet-Draft actif du groupe de travail OAuth 
(draft-ietf-oauth-v2-1-16, septembre 2026, expirant le 7 mars 2027)[176]. La référence normative est donc 
OAuth 2.0 conforme à la RFC 9700 (BCP 240, janvier 2025), alignée sur le profil OAuth 2.1 en cours de 
normalisation[175]. Le tableau 35 précise ce que cela signifie pour les agents.
Tableau 35 — Profil OAuth exigé pour les agents
Exigence
Référence
Application aux agents
Pratiques de sécurité 
courantes
RFC 9700, BCP 240[175]
Octroi implicite à éviter, octroi par mot de passe interdit, 
PKCE pour les clients publics, comparaison exacte des URI 
de redirection, jetons restreints en audience et en privi­
lèges, authentification asymétrique des clients (mTLS ou 
private_key_jwt).
Alignement sur OAuth 2.1
Brouillon draft-ietf-oauth-v2-1-16 
[327]
Le brouillon ne définit que trois octrois : code 
d’autorisation avec PKCE, jeton de rafraîchissement, identi­
fiants du client. Un agent n’utilise que ceux-là, plus les 
octrois d’extension retenus par le cadre (RFC 8693, RFC 
7523). Aucun jeton dans l’URI.
Authentification mTLS et 
jetons liés au certificat
RFC 8705[328]
Jeton lié par cnf « x5t#S256 »; la ressource rejette la 
requête si le certificat diffère. Profil par défaut dans le 
maillage de services, avec des X.509-SVID (ligne directrice 
du cadre).
Preuve de possession 
(DPoP)
RFC 9449[213]
Preuve JWT dpop+jwt liée à htm, htu, iat, jti et ath; jeton 
lié par cnf.jkt; nonce possible. Profil des agents hors 
maillage : poste de travail, navigateur, mobile, périphérie.
Identification de 
l’émetteur
RFC 9207[329]
Paramètre iss dans la réponse d’autorisation contre la 
confusion de serveurs. MCP 2026-07-28 exige que le client 
le valide; le cadre exige que le fournisseur d’identité 
l’émette.
Métadonnées de res­
source protégée
RFC 9728[330]
Document /.well-known/oauth-protected-resource dont la 
valeur resource correspond exactement à l’identifiant de la 
ressource. Publié par chaque serveur MCP et chaque API 
exposée aux agents.
Indicateur de ressource
RFC 8707[71]
Paramètre resource dans les requêtes d’autorisation et de 
jeton; MCP exige l’URI canonique du serveur[209].
Jeton d’accès JWT
RFC 9068[72]
Format des jetons délégués; act s’ajoute selon la RFC 8693.
EXIG-IAM-13 · DOIT
Profil OAuth de l’entreprise
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 125 sur 283


---
## [Page PDF 126]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Le fournisseur d’identité, la passerelle d’agents et les serveurs exposés aux agents DOIVENT appliquer 
le profil du tableau 35 : pratiques de la RFC 9700, aucun octroi implicite ni octroi par mot de passe, 
PKCE avec S256, comparaison exacte des URI de redirection, authentification asymétrique des clients 
confidentiels, émission et validation du paramètre iss (RFC 9207) et publication des métadonnées de 
ressource protégée (RFC 9728).
Pourquoi : la RFC 9700 est la référence de sécurité OAuth en vigueur, alors qu’OAuth 2.1 reste un brouillon[175, 176]. 
Le cadre est plus strict que la RFC 9700 sur deux points : celle-ci déconseille l’octroi implicite (NE DEVRAIT PAS) 
et ne fait que recommander l’authentification asymétrique des clients (choix du cadre).
EXIG-IAM-14 · DOIT
Jetons liés à l’expéditeur
Tout jeton qui donne accès à un outil P2 ou P3, ou qui est détenu par un agent de classe de risque 
élevée, DOIT être lié à l’expéditeur (sender-constrained) : mTLS (RFC 8705) dans le maillage de services, 
de préférence avec un X.509-SVID, ou DPoP (RFC 9449) hors du maillage. Pour les autres jetons, la 
liaison DEVRAIT être appliquée. Les jetons de rafraîchissement des clients publics DOIVENT être 
liés à l’expéditeur ou à usage unique.
Pourquoi : un jeton porteur volé est utilisable par quiconque le détient. La RFC 9700 recommande la liaison du jeton 
à l’expéditeur (DEVRAIT)[175]; le cadre la rend obligatoire pour les paliers P2 et P3 et pour les agents de classe de 
risque élevée. La répartition mTLS/DPoP est une ligne directrice du cadre.
Aucune norme IETF, OpenID ou NIST ne fixe de durée de vie chiffrée : la RFC 9700, le brouillon OAuth 2.1, 
MCP (qui le recommande, SHOULD) et le brouillon AIMS ne demandent que des jetons « de courte durée ». 
Le brouillon Transaction Tokens évoque des durées « de l’ordre de quelques minutes ou moins »[179]. Chez 
Microsoft Entra, la durée par défaut est de 60 à 90 minutes, une politique configurable ne peut descendre 
sous 10 minutes, et l’évaluation continue de l’accès (CAE) peut la prolonger jusqu’à 28 heures en échange 
d’une révocation en quasi temps réel[331]. Le cadre fixe donc une cible plutôt qu’un absolu.
EXIG-IAM-15 · DEVRAIT
Durée de vie courte des jetons
Un jeton d’accès d’agent DEVRAIT expirer en 15 minutes ou moins lorsque le fournisseur d’identité 
le permet. Lorsque la durée minimale du fournisseur est plus longue, l’écart est compensé par la liaison 
du jeton à l’expéditeur (EXIG-IAM-14) et par la révocation en quasi temps réel (EXIG-IAM-20). La 
délégation de longue durée d’un agent ambiant est régie par l’EXIG-AUT-18 (échéance inscrite à la 
fiche, renouvelée par une personne habilitée).
Pourquoi : la cible de 15 minutes est un choix du cadre; OpenAI cite, parmi les moyens de borner l’action des agents, 
des expirations périodiques jusqu’à ce qu’un humain révise et réautorise l’agent[291].
Agents autonomes et approbations hors bande
Un agent qui n’agit pour personne (traitement de fond, surveillance, rapprochement nocturne) n’a pas 
de mandant à représenter. Microsoft Entra Agent ID prescrit alors le flux par identifiants du client (client 
credentials), et le flux OBO pour les agents interactifs[92]. MCP publie, depuis la révision 2026-07-28, une 
extension stable « OAuth Client Credentials » pour ce cas[217]. Lorsqu’un agent sans interface doit obtenir 
la confirmation d’une personne, il passe par une approbation hors bande (CIBA), décrite à la section 8.5.
EXIG-IAM-16 · DOIT
Agents autonomes : identifiants du client et portées par outil
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 126 sur 283


---
## [Page PDF 127]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Un agent qui n’agit pour aucune personne DOIT utiliser l’octroi par identifiants du client avec son 
propre principal, authentifié par un justificatif cryptographique (EXIG-IAM-04), et des portées mini­
males définies outil par outil. Il ne partage jamais un jeton avec un autre agent et n’emprunte jamais 
l’identité d’une personne pour élargir ses droits.
Pourquoi : l’OWASP classe les identités surprivilégiées (NHI5) et la réutilisation d’identités (NHI9) parmi les risques 
principaux[91].
Mécanismes en cours de normalisation
Plusieurs mécanismes utiles aux agents ne sont pas encore des normes publiées. Le tableau 36 en donne l’état 
au 27 octobre 2026 et la cote retenue; il précise, pour l’identité, le catalogue des protocoles de la section 6.3.
Tableau 36 — Mécanismes d’identité en normalisation : état au 27 octobre 2026
Mécanisme
État
Usage visé
Cote
OAuth 2.1
Brouillon de groupe de tra­
vail, version −16 (septembre 
2026)[176]
Profil de référence, via la RFC 9700
Adopter avec 
réserve
ID-JAG et extension MCP 
« Enterprise-Managed Authori­
zation »
Brouillon −04 (21 mai 2026); 
extension MCP stable depuis 
2026-07-28[177, 218]
Le fournisseur d’identité de l’entreprise 
décide, par politique, à quels serveurs 
MCP un employé accède, sans consente­
ment par serveur (ID-JAG par RFC 8693, 
puis jeton d’accès par RFC 7523)
Évaluer
Transaction Tokens
Brouillon −11 (juillet 2026), 
consensus du groupe atteint, 
en attente du rapport[179, 
332]
Propager l’identité et le contexte 
d’autorisation dans un domaine; jeton ja­
mais accepté hors de son domaine, jamais 
plus large que le jeton remplacé
Évaluer
Identity and Authorization Chai­
ning Across Domains
Brouillon −17 dans la file de 
l’éditeur des RFC[333]
Appels d’agents entre domaines de 
confiance (filiales, partenaires); à citer 
comme RFC dès sa publication
Évaluer
Authentification de client OAuth 
par SPIFFE
Brouillon de groupe de tra­
vail −02 (15 juin 2026) [334]
SVID comme justificatif de client au lieu 
d’un secret partagé; d’ici là, SVID en 
actor_token, mTLS ou private_key_jwt
Évaluer
« OAuth 2.0 Extension: 
On-Behalf-Of User Authoriza­
tion for AI Agents »
Brouillon individuel, version 
−02 (26 août 2025), expiré 
le 27 février 2026, non adop­
té[335]
Paramètre requested_actor et consente­
ment nommant l’agent; ce n’est pas une 
spécification de l’IETF
Surveiller
Brouillons individuels WIMSE 
sur la délégation entre agents
Non adoptés par le groupe 
de travail[336]
Chaînes de délégation entre agents et 
entre organisations
Surveiller
À RETENIR
Les pratiques d’identité des agents ne sont pas stabilisées. Le centre d’excellence en cybersécurité du 
NIST (NCCoE, National Cybersecurity Center of Excellence) a publié en février 2026 un document de 
réflexion sur l’identité et l’autorisation des agents logiciels et d’IA, puis, le 29 septembre 2026, la syn­
thèse des commentaires de plus de 600 répondants et l’annonce d’un premier cas d’usage DevSecOps[337, 
338]. Le cadre exige donc des résultats (identité propre, délégation explicite, portée décroissante, audience 
unique) plutôt qu’un produit, et réexamine ces cotes à chaque révision du catalogue (section 11.7).
9.4 La passerelle d’agents, point d’application des politiques
Cette section précise le rôle de la passerelle d’agents : c’est le point d’application de la confiance zéro, celui 
où se vérifient, appel par appel, l’identité, la délégation, le catalogue, l’approbation et le budget.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 127 sur 283


---
## [Page PDF 128]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
La passerelle agit en mandataire inverse devant les serveurs MCP et les pairs A2A (section 5.2). Les décisions 
viennent du service de politiques; la passerelle les applique et en garde la trace. Ce rôle est réalisable 
avec des produits documentés, cités ici à titre d’exemples non limitatifs  : Azure API Management[108], 
Amazon Bedrock AgentCore Gateway[110], Kong AI Gateway[132], les projets agentgateway et Agent Router 
de l’AAIF[36, 130, 339] et MuleSoft Agent Fabric[138], avec sa passerelle Omni Gateway (anciennement Flex 
Gateway)[138, 340, 341]. Leur couverture varie : Azure API Management ne gère que les outils MCP, et non les 
ressources ni les invites[108], et seulement les agents A2A en JSON-RPC[109]; le mandataire A2A de Kong 
(greffon AI A2A Proxy de Kong Gateway 3.14 et plus, édition Enterprise) relaie le trafic sans gérer l’état 
des tâches[111]; cet état reste, selon le cadre, du ressort de l’agent ou de l’orchestrateur. La correspondance 
complète des blocs de solution figure à la section 5.4.
ALLER : CHAQUE APPEL AGENT → OUTIL OU AGENT → AGENT
Agent
appelant
1
Authentifier
l’agent et
le mandant
2
Contrôler
l’inscription
et la version
3
Autoriser
(droits effectifs,
palier, politique)
4
Garde-fous
d’entrée (schéma,
injection)
5
Vérifier le jeton
d’approbation
(P3, P2 > seuil)
6
Débit, quotas
et budget
de la tâche
7
Injecter les
secrets hors
de l’agent
Outil MCP
ou pair A2A
(inscrit au catalogue)
RETOUR : RÉSULTAT DE L’OUTIL
Agent
appelant
9 · Tracer et journaliser
span OpenTelemetry, enregistrement
d’audit (mandant, agent, outil, décision)
8 · Filtrer la sortie
masquage des renseignements personnels et des secrets,
balisage « contenu non fiable » avant le contexte du modèle
Résultat
structuré
Coupe-circuit central
Suspendre un agent, un outil ou un serveur MCP en une seule action, appliquée par toutes les passerelles;
tout refus renvoie un code d’erreur typé à l’agent et produit un événement d’audit. Testé au moins une fois par trimestre.
Figure 18 — Contrôles appliqués par la passerelle d’agents à chaque appel. À l’aller, sept contrôles s’appliquent dans l’ordre avant 
que l’appel n’atteigne l’outil ou le pair; au retour, la sortie est filtrée, puis tracée et journalisée. Un refus à n’importe quelle étape arrête 
l’appel; le coupe-circuit agit sur toutes les passerelles à la fois. Source : CRE-IA-2026-01.
Fonctions obligatoires
Les neuf contrôles de la figure 18 renvoient chacun à une partie du cadre :
1. Authentifier l’agent (SVID, mTLS) et le mandant (jeton délégué) : section 9.2 et section 9.3.
2. Contrôler l’inscription de l’agent, de l’outil ou du pair au catalogue, ainsi que la version et l’empreinte 
épinglées : section 6.8.
3. Autoriser d’après les droits effectifs, le palier de l’outil, le niveau d’autonomie et les attributs : section 
8.4.
4. Appliquer les garde-fous d’entrée : schéma des arguments, cohérence des en-têtes MCP, détection 
d’injection : section 6.5 et section 9.6.
5. Vérifier le jeton d’approbation lorsque la classe de l’agent et le palier l’exigent (P3; P2 au-delà du 
seuil, ou à chaque action pour un agent de niveau N2) : section 8.5.
6. Limiter le débit, les quotas et le budget de la tâche : section 10.6.
7. Injecter les justificatifs en aval, hors de l’agent (modèle sans clés, ci-dessous).
8. Filtrer la sortie : masquage des renseignements personnels et des secrets, balisage du contenu non 
fiable : section 9.6.
9. Tracer et journaliser : span OpenTelemetry et enregistrement d’audit : section 10.1 et section 10.3.
EXIG-IAM-17 · DOIT
Passage obligatoire par la passerelle d’agents
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 128 sur 283


---
## [Page PDF 129]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Dans tout environnement serveur, tout appel d’un agent vers un serveur MCP, vers un autre agent 
ou vers une ressource qui franchit une frontière de domaine DOIT passer par la passerelle d’agents 
(EXIG-ARC-01, EXIG-MCP-01), qui applique au minimum les neuf contrôles de la figure 18. Un outil, 
un serveur MCP ou un agent absent du catalogue, ou dont la version ou l’empreinte diffère de celle qui 
est épinglée, est bloqué. À l’intérieur d’un domaine, la décision par appel (EXIG-IAM-02) est appliquée 
par le serveur de ressources et par l’authentification mutuelle du maillage de services.
Pourquoi : un point d’application unique est le seul endroit où une politique s’applique de la même façon quel que 
soit le cadriciel ou la plateforme de l’agent appelant.
EXIG-IAM-18 · DOIT
Échec en mode fermé et refus typé
La passerelle DOIT refuser tout appel pour lequel elle ne peut pas obtenir ou évaluer une décision de 
politique valide; elle n’ouvre jamais le passage par défaut. Si le plan de contrôle est indisponible, elle 
continue d’appliquer la dernière politique distribuée. Tout refus renvoie à l’agent un code d’erreur typé 
(p. ex. portée insuffisante, approbation requise, budget épuisé, agent suspendu) et produit un événement 
d’audit.
Pourquoi : une passerelle ouverte par défaut transforme toute panne en brèche; un refus typé permet à l’agent 
d’escalader vers un humain plutôt que de réessayer à l’aveugle. Choix du cadre.
Neutralité au niveau du transport
Des éditeurs de passerelles, dont TrueFoundry et MuleSoft, soutiennent que la gouvernance native de chaque 
plateforme s’arrête à sa frontière : une règle définie dans un écosystème ne s’applique pas à un agent d’un 
autre[44, 45]. Il s’agit d’un argument d’architecture plutôt que d’un constat mesuré, mais il justifie de placer 
l’application des politiques au niveau du transport. MuleSoft (billet du 12 août 2026) propose sept portes de 
conception, chacune assortie d’un critère de réussite ou d’échec : (1) application neutre des politiques au 
niveau du transport HTTP, quel que soit le fournisseur ou le cadriciel; (2) politique attachée à l’actif (agent, 
serveur MCP, modèle, API); (3) application partout, avec maintien de la dernière politique distribuée en cas 
de panne du plan de contrôle; (4) réutilisation de la gouvernance d’API existante; (5) gouvernance centralisée 
des coûts et des jetons; (6) portabilité des environnements d’exécution sans refonte de la gouvernance; 
(7) propagation vérifiée de l’identité humaine déléguée[45]. Le cadre retient ces sept portes comme critères 
d’acceptation d’une passerelle d’agents (choix du cadre).
Modèle « sans clés »
Dans le modèle « sans clés », l’agent ne détient aucun justificatif pour les systèmes en aval : la passerelle ou 
un mandataire de sortie les ajoute à la requête après la décision de politique. Amazon Bedrock AgentCore 
Gateway documente ainsi une authentification entrante et sortante avec injection d’identifiants propre à 
chaque outil[110]. Selon la documentation de Vercel Sandbox, le patron a des limites lorsqu’il s’applique au 
trafic sortant d’un bac à sable : il dépend de l’indication du nom de serveur TLS (SNI) et exige la terminaison 
TLS par le mandataire, et une règle générique laisse passer sans transformation le trafic dont le domaine 
n’est pas détecté[342] (section 9.7).
EXIG-IAM-19 · DEVRAIT
Justificatifs en aval injectés par la passerelle
Les justificatifs nécessaires pour appeler un système en aval DEVRAIENT être injectés par la passerelle 
ou par un mandataire de sortie après la décision de politique (et DOIVENT l’être lorsqu’un code 
s’exécute en bac à sable selon l’EXIG-SEC-14 ou lorsqu’un secret résiduel de système patrimonial 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 129 sur 283


---
## [Page PDF 130]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
est employé sous dérogation selon l’EXIG-IAM-05), de sorte que le modèle n’y ait jamais accès 
(EXIG-IAM-06). L’injection ne vise qu’une liste fermée de destinations, sans règle générique.
Pourquoi : un justificatif que l’agent ne voit jamais ne peut ni fuir par une réponse du modèle ni être réutilisé hors 
de la politique.
Coupe-circuit
Le NIST AI RMF demande des mécanismes et des responsabilités pour supplanter, désengager ou désactiver 
un système dont les résultats s’écartent de l’usage prévu (MANAGE 2.4)[74], et le règlement européen sur 
l’IA prévoit, pour les systèmes à haut risque, la possibilité d’interrompre le système de façon sécuritaire (art. 
14(4)e))[61]. OpenAI recommande une interruption gracieuse, ciblée (révoquer une catégorie d’actions) ou 
générale[291]. Les plans de contrôle d’éditeurs n’y suffisent pas encore : Microsoft Agent 365, en disponibilité 
générale depuis le 1er mai 2026, tient un registre et permet de bloquer les agents non gérés, mais les actions de 
cycle de vie sur des agents infonuagiques tiers sont annoncées comme à venir[46]. Pour propager une révo­
cation au-delà de la passerelle, les spécifications finales OpenID Shared Signals Framework 1.0, qui fournit 
le cadre de diffusion, et CAEP 1.0 (29 août 2025), qui définit notamment les événements session-revoked, 
token-claims-change et credential-change [343, 344].
EXIG-IAM-20 · DOIT
Coupe-circuit propagé et mesuré
La plateforme DOIT offrir un coupe-circuit qui, en une seule action, suspend un agent, un outil, un 
serveur MCP ou une catégorie d’actions sur toutes les passerelles, désactive l’identité de l’agent auprès 
du fournisseur d’identité et diffuse la révocation, au moyen du Shared Signals Framework et de CAEP, 
aux systèmes raccordés qui les prennent en charge. Le délai maximal de bout en bout est fixé par 
l’entreprise et mesuré lors d’un exercice au moins trimestriel (section 7.8).
Pourquoi : un arrêt qui n’atteint qu’une plateforme laisse l’agent agir ailleurs. Aucune source vérifiable ne chiffre le 
gain d’un coupe-circuit; le cadre exige donc un délai mesuré plutôt qu’une promesse.
Politique en code et performance
Les passerelles du marché expriment leurs politiques dans des langages déclaratifs : agentgateway applique 
un contrôle d’accès par moteur de politiques CEL (Common Expression Language)[339], et AgentCore Policy 
applique des règles déterministes compatibles avec Cedar, qui interceptent chaque appel d’outil avant son 
exécution[102]. Une politique décide qui peut faire quoi : elle se gère comme du code de production.
EXIG-IAM-21 · DOIT
Politique en code, versionnée et testée
Les politiques appliquées par la passerelle DOIVENT être exprimées en code dans un langage décla­
ratif, versionnées, revues par une seconde personne, testées par des cas positifs et négatifs avant tout 
déploiement, puis distribuées par un pipeline. Chaque décision journalisée mentionne la version de la 
politique appliquée.
Pourquoi : sans version de politique dans le journal, l’audit ne peut pas reconstituer la règle qui a autorisé une action. 
Choix du cadre.
ATTENTION
Le cadre ne fixe aucune cible de latence chiffrée pour la passerelle, faute de mesure indépendante. Les 
chiffres publiés sont des allégations de fournisseurs, parfois contradictoires. L’équipe d’agentgateway 
déclare environ 500 000 requêtes par seconde avec 512 connexions et une latence P99 inférieure à 0,2 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 130 sur 283


---
## [Page PDF 131]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
ms à 30 000 requêtes par seconde, sans préciser le type de trafic ni le matériel[142]. TrueFoundry indique 
« typiquement moins de 5 ms » dans sa FAQ, mais son propre banc d’essai montre de +7 à +12 ms (1 
vCPU, 200 à 370 requêtes par seconde, selon le niveau de traçage)[143, 144]. Seule compte la latence ajoutée 
(P50 et P99) mesurée dans les conditions de l’entreprise, politiques et traçage activés; la section 13.2 en 
fait un critère d’évaluation des fournisseurs.
9.5 Menaces propres aux agents
Cette section fixe le référentiel de menaces que toute équipe applique à un agent et relie chaque menace 
aux contrôles du cadre. Un agent diffère d’une application classique sur deux points : il lit du texte qui peut 
contenir des instructions, et il agit par des outils. Une phrase piégée dans un courriel peut donc devenir une 
action réelle, comme un envoi, un paiement ou une suppression.
Référentiels retenus
Le cadre ne crée pas sa propre taxonomie. Il s’appuie sur des référentiels publics et entretenus, chacun avec 
un rôle précis (tableau 37). Le Top 10 de l’OWASP (Open Worldwide Application Security Project) pour 
les applications agentiques, publié le 9 décembre 2025 par l’OWASP GenAI Security Project, en constitue 
la base[345].
Tableau 37 — Référentiels de menaces retenus par le cadre
Référentiel
Éditeur, date et statut
Usage dans le cadre
OWASP Top 10 for 
Agentic Applications 
2026 (ASI01 à ASI10)
OWASP GenAI Security Project, décembre 2025, licence CC 
BY-SA 4.0[28]
Obligatoire Base de la modélisation des 
menaces des agents de classe de risque 
modérée ou élevée (EXIG-SEC-01).
OWASP Agentic AI – 
Threats and Mitiga­
tions (T1 à T17)
v1.0 du 17 février 2025 (T1 à T15); v1.1 de décembre 2025, 
qui ajoute T16, abus des protocoles inter-agents, et T17, 
compromission de la chaîne d’approvisionnement[87]
Recommandé Taxonomie détaillée 
pour l’analyse et les tests.
OWASP Top 10 for 
LLM Applications 2026
Édition 2026 parue en août 2026; l’agentivité excessive 
passe de LLM06 à LLM03[346]. L’édition 2025, publiée le 17 
novembre 2024 (LLM01 Prompt Injection à LLM10 Unboun­
ded Consumption), reste celle à laquelle renvoie la table de 
correspondance du Top 10 agentique (ASI) [347, 348]
Recommandé Risques propres au mo­
dèle lui-même.
OWASP Non-Human 
Identities Top 10 
(2025)
NHI1 Improper Offboarding à NHI10 Human Use of NHI[349]
Recommandé Identités des agents 
(section 9.2).
OWASP MCP Top 10
Édition 2025, en phase bêta (MCP01 à MCP10)[222]
Recommandé Tests d’abus des serveurs 
MCP (section 6.5).
OWASP Agentic Skills 
Top 10 (AST10)
Projet distinct au stade « Incubator », version affichée 
1.0-2026[350]
Surveiller Référence émergente sur les 
compétences d’agents, non une norme.
CSA MAESTRO
Cloud Security Alliance, 6 février 2025; sept couches, des 
modèles de fondation à l’écosystème d’agents[351]
Recommandé Structurer l’analyse 
couche par couche.
MITRE ATLAS
Version 2026.09 du 14 septembre 2026 : 16 tactiques, 120 
techniques, 88 sous-techniques, 40 mesures d’atténuation et 
73 études de cas[352]
Recommandé Scénarios d’équipe 
rouge et règles de détection.
NIST AI 100-2 E2025
NIST, version finale du 24 mars 2025[97]
Recommandé Vocabulaire des attaques 
et principe de présomption d’injection.
EXIG-SEC-01 · DOIT
Modélisation des menaces avant la production
Tout agent de classe de risque modérée ou élevée DOIT faire l’objet, avant sa mise en production, d’une 
modélisation des menaces documentée qui examine chacun des risques ASI01 à ASI10 et consigne, pour 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 131 sur 283


---
## [Page PDF 132]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
chacun, les contrôles retenus ou la justification de son exclusion. La modélisation DOIT être révisée à 
chaque changement de modèle, d’outil, de palier d’outil ou de niveau d’autonomie. Un agent de risque 
faible DEVRAIT faire l’objet d’une analyse simplifiée sur la même base.
Pourquoi : examiner systématiquement les dix risques du référentiel public évite les angles morts propres aux agents.
Les dix risques du Top 10 agentique
Le tableau 38 reprend les intitulés officiels de l’OWASP[28], les explique en une phrase et renvoie aux 
contrôles du cadre qui y répondent. La colonne « Mécanisme » est une synthèse du cadre, non une citation.
Tableau 38 — Top 10 OWASP des applications agentiques et contrôles du cadre
Code
Risque (titre officiel traduit)
Mécanisme
Contrôles du cadre
ASI01
Détournement de l’objectif de 
l’agent (Agent Goal Hijack)
Un contenu non fiable (page web, 
courriel, sortie d’outil) réoriente les 
objectifs ou le plan de l’agent.
EXIG-SEC-03 à EXIG-SEC-07; approbation 
humaine de toute modification des objec­
tifs (EXIG-AUT-03, section 8.1).
ASI02
Mésusage et exploitation des 
outils (Tool Misuse and Exploi­
tation)
L’agent enchaîne des outils légitimes 
de façon dangereuse ou leur passe des 
arguments malveillants.
Paliers P0 à P3 (section 8.3); validation des 
arguments par la passerelle (section 9.4); 
EXIG-SEC-18 et EXIG-SEC-21.
ASI03
Abus d’identité et de privi­
lèges (Identity and Privilege 
Abuse)
L’agent dispose de droits excessifs, 
réutilise un jeton ou agit au-delà du 
mandat de son mandant.
Identité propre (EXIG-IAM-03 à 
EXIG-IAM-06, section 9.2); jeton délégué 
à audience unique et portée réduite à 
chaque saut (EXIG-IAM-08 à EXIG-IAM-12, 
section 9.3).
ASI04
Vulnérabilités de la chaîne 
d’approvisionnement agen­
tique (Agentic Supply Chain 
Vulnerabilities)
Un serveur MCP, un agent, une com­
pétence ou un modèle de tiers est 
compromis à la source ou modifié 
après approbation.
EXIG-SEC-18 à EXIG-SEC-22; catalogue et 
versions (section 6.8).
ASI05
Exécution de code inattendue 
(Unexpected Code Execution, 
RCE)
L’agent génère ou déclenche du code 
qui s’exécute avec les droits de son 
environnement.
EXIG-SEC-08 à EXIG-SEC-17.
ASI06
Empoisonnement de la mé­
moire et du contexte (Memory 
& Context Poisoning)
Une information fausse ou piégée, 
écrite en mémoire ou dans le contexte, 
oriente les décisions suivantes.
Contrôles d’écriture en mémoire (section 
5.5); mémoire traitée comme contenu non 
fiable (EXIG-SEC-03).
ASI07
Communication inter-agents 
non sécurisée (Insecure 
Inter-Agent Communication)
Un agent usurpe l’identité d’un pair, 
ou un message est intercepté ou altéré 
entre agents.
Authentification à chaque requête (section 
6.6); cartes signées (EXIG-SEC-19); mes­
sages d’agents non fiables (EXIG-SEC-03).
ASI08
Défaillances en cascade (Cas­
cading Failures)
Une erreur ou une boucle se propage 
d’agent en agent plus vite qu’un hu­
main ne peut réagir.
Compteur de sauts (EXIG-EVT-06, section 
6.7); compensation (section 7.5); délais, 
disjoncteurs et plafonds (EXIG-ORC-26 et 
EXIG-ORC-27, section 7.8).
ASI09
Exploitation de la confiance 
humain-agent (Human-Agent 
Trust Exploitation)
L’agent obtient une approbation par 
une justification trompeuse ou par la 
saturation des approbateurs.
Approbation liée à l’action exacte 
(EXIG-AUT-12, section 8.5); prévention de 
l’approbation machinale (EXIG-AUT-19 et 
EXIG-AUT-20, section 8.7).
ASI10
Agents dévoyés (Rogue 
Agents)
Un agent s’écarte durablement de son 
mandat tout en paraissant légitime.
Surveillance, plafonds et coupe-circuit 
(section 9.4); EXIG-SEC-26; journal d’audit 
signé (section 10.3).
Le document de l’OWASP fournit sa propre table de correspondance entre chaque risque ASI, le Top 10 LLM 
2025, les menaces T1 à T17 et les risques fondamentaux de l’AI Vulnerability Scoring System (AIVSS)[28]. Le 
cadre l’emploie telle quelle plutôt que de recréer des regroupements approximatifs. Ainsi, ASI01 correspond 
à LLM01:2025 (injection d’invite) et à LLM06:2025 (agentivité excessive, devenue LLM03 dans l’édition 2026)
[28, 346, 348], et ASI09 s’arrime à la menace T10, saturation de l’humain dans la boucle[28, 87]. De même, les 
risques d’identités non humaines se répartissent entre plusieurs risques ASI plutôt que de se rattacher à 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 132 sur 283
