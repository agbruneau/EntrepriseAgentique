# chunk_12 — pages PDF 111 à 122 (sur 283)



---
## [Page PDF 111]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
Agent
prépare l’action P3
Passerelle d’agents
point d’application
Service d’approbation
adossé au fournisseur d’identité
Approbateur
personne habilitée
1
appel d’outil P3 sans jeton
2
calcule l’empreinte et crée la demande
h = SHA-256(outil ‖ arguments canoniques)
3
présente l’action exacte, ses
paramètres et son effet attendu
4
approuve (authentification forte)
5
jeton d’approbation signé, à usage unique
{ h, approbateur, tâche, exp }
6
rejoue l’appel avec le jeton
7
vérifie la signature, l’expiration, l’usage unique et
recalcule h : toute modification des arguments
invalide l’approbation → exécution, puis audit
N’est jamais une approbation
• un « oui » écrit dans la
conversation de l’agent
• un résumé rédigé par l’agent
• une approbation donnée pour
d’autres arguments
Figure 16 — Approbation humaine signée, liée à l’action exacte. La passerelle intercepte l’appel P3, calcule l’empreinte de l’action 
et la fait approuver par une personne habilitée; le jeton signé ne vaut que pour cette empreinte, une seule fois et pendant 15 minutes 
au plus. Source : CRE-IA-2026-01.
L’empreinte se calcule ainsi : h = SHA-256(identifiant de l’outil ‖ arguments canonisés), où l’identifiant de 
l’outil est pleinement qualifié (serveur, nom et version épinglée). La canonisation suit la RFC 8785 (JSON 
Canonicalization Scheme), une RFC informative de la filière indépendante, non endossée par l’IETF, mais 
stable[308]; A2A 1.0 l’emploie déjà pour signer les cartes d’agent[68]. Sans canonisation, deux sérialisations du 
même objet JSON donneraient deux empreintes. Si l’agent, ou une injection, change un seul argument après 
l’approbation, l’empreinte recalculée par la passerelle ne correspond plus et l’appel est refusé. Un exemple 
de jeton figure à l’annexe C.
La formule est un choix de conception du cadre, pas une norme. Elle met en œuvre l’approbation explicite 
par action à fort impact que recommande l’OWASP (ASI02)[28] et s’appuie sur trois éléments normalisés : 
OpenID Connect CIBA (Client-Initiated Backchannel Authentication) pour l’approbation hors bande, la RFC 
9396 pour décrire l’action et la RFC 8785 pour la canonisation.
EXIG-AUT-12 · DOIT
Jeton d’approbation lié à l’action exacte
Toute approbation exigée par la figure 15 DOIT produire un jeton signé par le service d’approbation 
adossé au fournisseur d’identité, contenant au minimum : l’empreinte h (SHA-256 de l’identifiant plei­
nement qualifié de l’outil, suivi des arguments canonisés selon la RFC 8785), l’identifiant pseudonymisé 
de l’approbateur, les identifiants de la tâche et de l’agent, une date d’expiration et un identifiant à usage 
unique. Avant l’exécution, la passerelle DOIT vérifier la signature, l’expiration et l’usage unique, puis 
recalculer h; toute différence annule l’approbation. Le jeton DOIT expirer au plus 15 minutes après sa 
signature.
Pourquoi : un lien cryptographique entre la décision humaine et l’action exécutée détecte toute modification des 
arguments après l’approbation; ce mécanisme et la durée de validité sont des choix du cadre.
EXIG-AUT-13 · NE DOIT PAS
Ce qui n’est jamais une approbation
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 111 sur 283


---
## [Page PDF 112]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
La passerelle NE DOIT PAS accepter comme approbation un message d’acquiescement dans la 
conversation de l’agent, un résumé ou une justification rédigés par l’agent, une confirmation locale 
dans l’interface de l’agent, ni une approbation donnée pour d’autres arguments, une autre tâche ou un 
autre agent.
Pourquoi : le brouillon de groupe de travail WIMSE AIMS précise qu’une confirmation locale dans l’interface ne 
suffit pas comme autorisation[309].
EXIG-AUT-14 · DEVRAIT
Approbation hors bande normalisée
L’approbation d’un appel P3, ou celle que requiert un agent sans interface, DEVRAIT passer par 
OpenID Connect CIBA  : le service d’approbation lance une demande d’authentification dorsale, 
l’approbateur confirme sur son propre appareil, et un binding_message court, affiché sur les 
deux appareils, rattache la demande à l’action. L’action DEVRAIT être décrite par le paramètre 
authorization_details de la RFC 9396 lorsqu’elle comporte des paramètres que les portées ne peuvent 
exprimer, comme un montant ou un destinataire.
Pourquoi : CIBA Core 1.0 est une spécification finale de l’OpenID Foundation qui découple l’appareil de l’agent de 
celui de l’approbateur[310]; le brouillon WIMSE AIMS cite CIBA en exemple d’autorisation par palier, tout en notant 
ses limites en cours d’exécution, et le livre blanc de l’OpenID Foundation propose CIBA pour l’approbation humaine 
des agents[93, 311]; la RFC 9396 exprime les autorisations fines que scope ne peut exprimer[312].
EXIG-AUT-15 · DOIT
Approbateurs habilités et formés
Chaque combinaison de classe et de palier soumise à approbation DOIT avoir une liste d’approbateurs 
habilités, inscrite au registre. L’approbateur DOIT s’authentifier par authentification forte (au moins 
deux facteurs), posséder la compétence du domaine et l’autorité de refuser, et avoir été formé aux modes 
de défaillance des agents. Pour un appel P3 d’un agent de classe élevée, deux approbateurs distincts 
DOIVENT approuver, dont au moins un autre que le mandant.
Pourquoi : le RIA confie le contrôle humain des systèmes à haut risque à des personnes ayant la compétence, la 
formation et l’autorité nécessaires (art. 26, par. 2)[94]; l’IMDA demande que les superviseurs connaissent les modes 
de défaillance des agents[76]. Le second approbateur est un choix du cadre.
8.6 Interaction humaine avec les agents ambiants
Un agent ambiant travaille en arrière-plan, déclenché par des événements; la personne n’est pas devant lui 
quand il a besoin d’elle, et l’interaction doit être conçue en conséquence.
LangChain définit les agents ambiants comme des agents qui écoutent un flux d’événements et agissent 
en conséquence, éventuellement sur plusieurs événements à la fois, sans être nécessairement entièrement 
autonomes (section 3.3). Pour les relier aux personnes, son billet de janvier 2025 décrit trois patrons : 
notifier, questionner et réviser[86]. Le schéma de la boîte de réception d’agents (Agent Inbox) y associe 
quatre réponses : accept, edit, response et ignore, activées une à une par les drapeaux allow_accept, 
allow_edit, allow_respond et allow_ignore [313].
Tableau 32 — Trois patrons d’interaction avec un agent ambiant
Patron
Quand l’employer
Ce que fait l’agent
Réponses admises
Notifier
Événement important que la politique in­
terdit à l’agent de traiter (p. ex. un contrat 
reçu pour signature).
Signale sans agir.
Prendre connaissance.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 112 sur 283


---
## [Page PDF 113]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
Patron
Quand l’employer
Ce que fait l’agent
Réponses admises
Questionner
Information manquante ou ambiguë.
Suspend la tâche et pose une 
question ciblée au lieu de deviner.
Répondre.
Réviser
Action soumise à approbation selon la fi­
gure 15.
Place l’action préparée dans la file, 
avec son effet attendu.
Accepter, éditer, ré­
pondre par une rétroac­
tion, ignorer (refus).
Éditer une action revient à approuver une autre action : la passerelle calcule l’empreinte des arguments 
modifiés, et c’est cette version que couvre le jeton. Microsoft recommande aussi de distinguer l’approbation, 
qui fait avancer le flux, de la rétroaction, qui renvoie le travail à l’agent, et de restreindre les points 
d’approbation à des invocations d’outils précises[9]. Les protocoles offrent les mécanismes d’attente : en A2A 
1.0, une tâche passe à l’état TASK_STATE_INPUT_REQUIRED ou TASK_STATE_AUTH_REQUIRED (section 6.6)[68]; 
en MCP, un serveur pose une question par élicitation, sans jamais demander de secret par formulaire[223].
Le « voyage dans le temps » souvent associé à ce patron n’est pas une réponse de la boîte de réception : c’est 
une fonction des points de contrôle de LangGraph, qui permet de rejouer une exécution depuis un point 
antérieur ou de bifurquer après avoir modifié l’état[283]. Il sert au diagnostic et à la correction; rejouer une 
étape réexécute ses effets. Enfin, le dépôt agent-inbox est archivé, en lecture seule, depuis le 20 septembre 
2026[313] : le cadre adopte le patron, pas l’outil.
Un piège d’implémentation mérite attention. Dans LangGraph, interrupt() exige un mécanisme de points 
de contrôle persistant; à la reprise, le nœud interrompu redémarre depuis son début, si bien que le code 
placé avant l’interruption s’exécute de nouveau[82]. Un appel d’écriture placé avant le point d’approbation 
serait donc rejoué.
EXIG-AUT-16 · DOIT
Boîte de réception persistante
Tout agent ambiant de niveau N2 ou plus DOIT acheminer ses interactions humaines par une boîte de 
réception persistante qui met en œuvre les trois patrons du tableau 32. Chaque demande DOIT indiquer 
le patron, la tâche, l’agent, l’effet attendu et une échéance fixée par cas d’usage. Une demande sans 
réponse à l’échéance expire : l’action n’est pas exécutée et la tâche passe à une file d’escalade nommée. 
« Ignorer » vaut refus.
Pourquoi : les patrons de LangChain évitent que l’agent devine (il pose une question plutôt que d’halluciner) ou 
agisse sans validation humaine (révision d’une action avant son exécution)[86]; l’expiration en refus applique l’échec 
en mode fermé de l’EXIG-AUT-11.
EXIG-AUT-17 · DOIT
État persisté et effets après le point d’approbation
L’orchestrateur DOIT conserver l’état de la tâche de façon durable à chaque point d’approbation 
obligatoire, dans un moteur d’exécution durable (section 7.4). Un appel à effet de bord NE DOIT PAS 
précéder le point d’interruption dans la même étape; s’il ne peut pas être déplacé, il DOIT porter une 
clé d’idempotence (section 7.6).
Pourquoi : Microsoft recommande de persister l’état aux points d’approbation obligatoires pour reprendre sans 
rejouer le travail antérieur[9], et LangGraph réexécute le code qui précède une interruption[82].
EXIG-AUT-18 · DOIT
Réautorisation périodique des agents ambiants
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 113 sur 283


---
## [Page PDF 114]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
La délégation qui permet à un agent ambiant de niveau N3 ou N4 d’agir DOIT expirer à une échéance 
inscrite à sa fiche, au plus égale à la période d’attestation par le parrain, soit 12 mois au plus pour un 
agent de classe modérée ou faible (section 11.5 et EXIG-GOV-13). À l’échéance, l’agent s’arrête jusqu’à 
ce qu’une personne habilitée renouvelle la délégation.
Pourquoi : OpenAI recommande des expirations périodiques qui maintiennent l’agent à l’arrêt jusqu’à ce qu’un 
humain le révise et le réautorise[291].
8.7 Éviter l’approbation machinale
Un contrôle humain que personne n’exerce vraiment donne une fausse assurance; le cadre le conçoit et le 
mesure au lieu de le présumer.
Le phénomène est documenté. Parasuraman et Manzey (2010) montrent que le biais d’automatisation 
produit des erreurs d’omission et de commission, touche les novices comme les experts, s’observe aussi 
en équipe et ne disparaît ni avec la formation ni avec les consignes; la complaisance apparaît surtout sous 
charge multitâche[314]. OpenAI note qu’un utilisateur qui doit approuver rapidement beaucoup de décisions 
voit sa capacité à les examiner sérieusement diminuer[291].
Les référentiels en tirent des exigences. Le RIA demande que les personnes chargées du contrôle restent 
conscientes du biais d’automatisation (art. 14, par. 4, al. b)[290]; pour les systèmes à haut risque de l’annexe 
III, ces obligations s’appliquent à compter du 2 décembre 2027, et du 2 août 2028 pour ceux de l’annexe I, 
selon le RIA modifié par le règlement (UE) 2026/1744[58, 315]. L’OWASP décrit la menace T10 « Overwhelming 
Human in the Loop  »  : un attaquant submerge les réviseurs de demandes pour provoquer fatigue et 
approbations précipitées[87]. Le risque ASI09 « Human-Agent Trust Exploitation » vise la surconfiance : 
biais d’automatisation, autorité perçue, explications fabriquées[28].
ATTENTION
Plus d’approbations ne veut pas dire plus de sécurité. Au-delà d’un certain volume, chaque approbation 
devient un clic. Le cadre préfère des approbations moins nombreuses, mieux ciblées et mesurées, et 
automatise ce que la figure 15 classe à faible risque.
EXIG-AUT-19 · DOIT
Écran d’approbation fidèle à l’action
L’écran d’approbation DOIT présenter l’action exacte, ses paramètres, son effet attendu, sa réversibilité 
et sa compensation, la provenance des données qui l’ont motivée (en signalant tout contenu non fiable) 
et un indicateur de risque produit par les règles du catalogue, non par le modèle. La prévisualisation 
NE DOIT PAS avoir d’effet de bord : ni appel réseau, ni changement d’état. Le raisonnement de l’agent 
PEUT être affiché comme information secondaire, mais il NE DOIT PAS tenir lieu de justification 
suffisante.
Pourquoi : l’OWASP (ASI09) recommande un résumé de risque en langage clair plutôt qu’une justification produite 
par le modèle, et la séparation entre prévisualisation et effet[28]; la spécification MCP recommande de montrer à 
l’utilisateur les entrées de l’outil avant l’appel[197].
EXIG-AUT-20 · DOIT
Charge d’approbation maîtrisée
Les files d’approbation DOIVENT être priorisées selon le risque. Les demandes semblables 
PEUVENT être regroupées à l’affichage, mais chaque action conserve son propre jeton d’approbation 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 114 sur 283


---
## [Page PDF 115]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
(EXIG-AUT-09 et EXIG-AUT-12). La fréquence des demandes adressées à chaque approbateur DOIT 
être plafonnée selon un seuil fixé par le comité, et la charge DOIT être répartie entre approbateurs, avec 
rotation. Les actions que la figure 15 classe comme automatiques ne sont pas soumises à approbation.
Pourquoi : contre la menace T10, l’OWASP recommande de prioriser les files de révision par risque, d’automatiser 
les approbations à faible risque, de limiter la fréquence des demandes et de répartir dynamiquement la charge entre 
réviseurs[87]; la rotation est un choix du cadre.
EXIG-AUT-21 · DOIT
Mesure de la qualité de la supervision
La plateforme DOIT produire chaque mois, par approbateur et par cas d’usage : le taux d’approbation 
sans modification, les taux de rejet et de modification, le temps de réponse, les renversements suspects 
(action refusée puis approuvée) et les approbateurs dont le taux d’approbation sans modification ou le 
temps de réponse s’écarte de la médiane du cas d’usage d’un seuil fixé par le comité. Pour les actions 
exécutées sans approbation préalable aux niveaux N3 et N4, une revue humaine a posteriori DOIT 
porter sur un échantillon d’au moins 5 % des actions de classe modérée et 1 % de celles de classe faible 
(choix du cadre). Le comité DOIT fixer ces seuils d’alerte par cas d’usage et examiner les écarts signalés.
Pourquoi : l’IMDA recommande de suivre le taux d’intervention des réviseurs (rejet ou modification des actions 
de l’agent), dont un niveau bas peut signaler une approbation machinale, et le temps de réponse des réviseurs[76]; 
l’OWASP recommande de détecter les renversements suspects[87] et le NIST juge utile de recueillir la fréquence des 
cas où une personne passe outre aux sorties du système, et leurs motifs[99]. Aucune source reconnue ne fixe de seuil 
universel.
8.8 Décisions automatisées et droit à la révision
Quand un agent décide seul à propos d’une personne, la Loi 25 crée des droits précis, et une approbation de 
pure forme ne les fait pas disparaître; la section 12.2 traite l’ensemble des obligations.
L’article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. 
P-39.1, « Loi sur le privé ») vise toute décision fondée exclusivement sur un traitement automatisé de 
renseignements personnels. L’entreprise doit en informer la personne au plus tard au moment où elle lui 
communique la décision. À la demande de la personne, elle l’informe des RP utilisés, des raisons et des 
principaux facteurs et paramètres ayant mené à la décision, ainsi que de son droit de faire rectifier ces 
renseignements. La personne doit pouvoir présenter ses observations à un membre du personnel en mesure 
de réviser la décision[56, 316]. Le défaut d’informer la personne de la décision ou de lui donner l’occasion 
de présenter ses observations, en contravention à l’article 12.1, est expressément un motif de sanction 
administrative pécuniaire (art. 90.1, par. 5°)[56, 317], et les renseignements utilisés pour prendre une décision 
doivent être conservés au moins un an après celle-ci (art. 11)[56]. Pour les organismes publics, la disposition 
équivalente est l’article 65.2 de la Loi sur l’accès aux documents des organismes publics et sur la protection 
des renseignements personnels (RLRQ, c. A-2.1, « Loi sur l’accès »)[318].
Qu’est-ce qui rend une décision « exclusivement » automatisée? Selon l’interprétation gouvernementale 
de l’article 65.2, c’est le cas lorsqu’aucune personne physique n’a exercé de contrôle important  : une 
intervention humaine mineure, sans effet réel sur le résultat, ne fait pas échapper à l’obligation, alors qu’un 
outil d’aide qui fournit des éléments à un employé qui décide lui-même n’est pas visé. Cette interprétation 
précise aussi qu’il n’est pas requis de divulguer l’algorithme : le mot « principaux » limite l’explication aux 
facteurs déterminants[318]. Sous le règlement général sur la protection des données de l’Union européenne 
(RGPD), les lignes directrices WP251rev.01 vont dans le même sens : on ne peut contourner la règle en 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 115 sur 283


---
## [Page PDF 116]

CRE-IA-2026-01 · Cadre de référence
8 Autonomie et supervision humaine
fabriquant une intervention humaine, et le contrôle doit être exercé par une personne qui a l’autorité et la 
compétence de modifier la décision[319].
DROIT APPLICABLE
La Commission d’accès à l’information (CAI) n’a pas publié de critères de l’intervention humaine 
significative pour le secteur privé. Les exigences ci-dessous constituent une interprétation prudente du 
cadre, fondée par analogie sur l’article 65.2 et sur WP251rev.01; leur application à un cas précis relève 
des affaires juridiques.
EXIG-AUT-22 · DOIT
Décisions visées par l’article 12.1
Tout agent qui rend une décision concernant une personne, ou la prépare sans révision humaine 
significative, à partir d’un traitement automatisé de ses RP DOIT être de classe élevée et mettre en 
œuvre : l’avis à la personne au plus tard au moment de la communication de la décision; la production, 
sur demande, des RP utilisés, des raisons et des principaux facteurs et paramètres, établie à partir des 
traces et du journal d’audit; l’indication du droit de rectification; un canal vers un membre du personnel 
en mesure de réviser la décision; la conservation des renseignements utilisés pendant au moins un an 
après la décision.
Pourquoi : obligations de l’article 12.1 et de l’article 11 de la Loi sur le privé (pour un organisme public, l’article 65.2 
de la Loi sur l’accès prévoit des obligations d’information équivalentes)[56]; la traduction des traces en explication 
intelligible est un choix de mise en œuvre du cadre.
EXIG-AUT-23 · DOIT
Révision humaine significative
Une intervention humaine DOIT être traitée comme nominale, et la décision comme exclusivement 
automatisée, sauf si la personne qui intervient a l’autorité de modifier la décision et la compétence 
voulue, accède à toutes les données pertinentes et non à la seule recommandation de l’agent, dispose du 
temps nécessaire, et exerce une influence réelle mesurée par l’EXIG-AUT-21. Le degré d’intervention 
humaine et l’étape où elle a lieu DOIVENT être consignés dans l’EFVP.
Pourquoi : interprétation prudente du cadre, et non règle expresse de la Loi 25; par analogie, une validation de 
pure forme ne retire pas le caractère exclusivement automatisé selon l’interprétation gouvernementale de l’article 
65.2 (secteur public)[318], et WP251rev.01 demande de consigner dans l’analyse d’impact le degré et l’étape de 
l’intervention humaine[319].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 116 sur 283


---
## [Page PDF 117]

CRE-IA-2026-01 · Cadre de référence
Partie III — Confiance et exploitation
Identité, sécurité et confiance zéro; traçage, évaluation continue et maîtrise des coûts.
9 · Identité, sécurité et confiance zéro
10 · Observabilité, évaluation et FinOps
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 117 sur 283


---
## [Page PDF 118]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
9 Identité, sécurité et confiance zéro
Un agent est un programme dont le comportement dépend en partie du contenu qu’il lit : son emplacement 
dans le réseau ne dit rien de ses intentions au moment où il agit. Ce chapitre applique donc la confiance 
zéro aux agents : chacun possède sa propre identité, n’agit pour une personne qu’au moyen d’un jeton 
délégué dont la portée ne peut que diminuer, et chacun de ses appels est décidé, un à un, par le service de 
politiques et appliqué par une passerelle. Les sections 9.1 à 9.4 traitent de l’identité, de la délégation et du 
point d’application des politiques; les sections 9.5 à 9.9 traitent des menaces, de l’injection d’instructions, 
du cloisonnement, de la chaîne d’approvisionnement et de l’assurance.
9.1 La confiance zéro appliquée aux agents
Cette section transpose aux agents le modèle de confiance zéro du NIST et pose la règle centrale du chapitre : 
aucune autorisation ne s’hérite, chaque appel se décide.
La publication NIST SP 800-207 (août 2020) définit la confiance zéro comme l’absence de toute confiance im­
plicite fondée sur l’emplacement réseau. L’authentification et l’autorisation y sont des fonctions distinctes, 
exécutées avant l’accès; l’accès à chaque ressource est accordé par session, au moindre privilège, selon une 
politique dynamique qui tient compte de l’identité, de l’état de l’actif et d’attributs comportementaux[73, 112]. 
La publication SP 800-207A (septembre 2023) déplace la segmentation du réseau vers l’identité des services 
et cite SPIFFE comme infrastructure d’identité applicative[320].
Ce modèle convient particulièrement aux agents. Un agent légitime et correctement authentifié peut 
changer de comportement en cours de tâche : il lui suffit de lire un courriel qui contient des instructions 
cachées. Une autorisation accordée au début de la session ne protège donc pas l’étape suivante. C’est 
pourquoi le cadre va au-delà de l’accès par session décrit par le NIST : il exige une décision à chaque appel 
d’outil ou d’agent (choix du cadre). Le tableau 33 montre où chaque composant logique de la SP 800-207 se 
situe dans l’architecture de référence (chapitre 5).
Tableau 33 — Composants logiques de la confiance zéro et leur réalisation pour les agents
Composant (NIST SP 
800-207)
Rôle selon le NIST
Réalisation dans le cadre
Moteur de politique (PE)
Décide d’accorder, de refuser ou de 
révoquer l’accès à une ressource.
Service de politiques : évalue l’identité de l’agent, le man­
dant, les droits effectifs, le palier de l’outil, le niveau 
d’autonomie et l’état de la tâche.
Administrateur de poli­
tique (PA)
Établit ou coupe le chemin de com­
munication entre le sujet et la res­
source.
Fournisseur d’identité (émission et révocation des jetons dé­
légués) et plan de contrôle des passerelles (distribution des 
politiques, coupe-circuit).
Point d’application de po­
litique (PEP)
Ouvre, surveille et termine les 
connexions.
Passerelle d’agents pour les appels vers les outils et les 
agents; passerelle de modèles pour les appels vers les mo­
dèles.
Sources de données 
(CDM, gestion des iden­
tités, journaux, SIEM, ren­
seignements sur les me­
naces)
Alimentent le moteur de politique 
en informations sur l’état de l’actif, 
le sujet et l’activité.
Registre des agents, catalogue (paliers, versions épinglées), 
signaux de risque partagés, budget consommé, contenu non 
fiable déjà lu.
Source : d’après NIST SP 800-207[73]; colonne de droite : choix du cadre.
EXIG-IAM-01 · NE DOIT PAS
Aucune confiance implicite
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 118 sur 283


---
## [Page PDF 119]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
L’accès d’un agent à un outil, à une ressource ou à un autre agent NE DOIT PAS être accordé du 
seul fait de son emplacement réseau, de sa plateforme d’hébergement ou de son appartenance au 
même orchestrateur ou au même domaine. Toute communication entre composants est mutuellement 
authentifiée et chiffrée, y compris à l’intérieur d’un réseau privé.
Pourquoi : la SP 800-207 exclut toute confiance implicite fondée sur l’emplacement réseau[73]; un agent détourné se 
trouve, par définition, déjà à l’intérieur.
EXIG-IAM-02 · DOIT
Une décision à chaque appel
Chaque appel d’un agent vers un outil, une ressource ou un autre agent DOIT être authentifié et 
autorisé individuellement. Le point d’application applique la décision du service de politiques, rendue 
d’après l’identité de l’agent, le mandant, le palier de l’outil, le niveau d’autonomie, l’état de la tâche 
et les signaux de risque. Aucune autorisation n’est héritée d’un appel précédent ni d’une session, et 
l’agent ne participe jamais à la décision sur ses propres droits.
Pourquoi  : l’état d’une tâche agentique change d’un appel à l’autre (contenu non fiable lu, budget consommé, 
approbation expirée); une décision prise une fois par session ne le verrait pas. Exigence propre au cadre, plus stricte 
que l’accès par session de la SP 800-207.
EXEMPLE
Un agent de soutien lit, à l’étape 3 de sa tâche, un courriel externe. À l’étape 4, il tente d’appeler l’outil 
d’envoi de courriels. Parce que la décision est prise à chaque appel, la passerelle sait que la session a 
consommé du contenu non fiable et refuse l’envoi sans approbation humaine (section 9.6). Une autori­
sation accordée à l’ouverture de la session l’aurait laissé passer.
9.2 Identité non humaine des agents
Cette section fixe ce qu’est l’identité d’un agent, comment elle est émise et comment elle prend fin. Le 
principe est simple : on ne peut ni auditer, ni restreindre, ni révoquer ce qu’on ne peut pas désigner.
Un agent n’est ni une personne, ni un compte de service partagé (section 3.4). Microsoft déconseille 
d’attribuer aux agents un compte d’utilisateur ordinaire ou un principal de service traditionnel et a créé, 
avec Microsoft Entra Agent ID, un type d’identité propre aux agents[90]. Les bonnes pratiques de ce produit 
prescrivent une identité unique par instance d’agent et le moindre privilège[92]. Le brouillon de groupe de 
travail IETF WIMSE « AI Identity Management System » (AIMS, draft-ietf-wimse-aims-00, 15 septembre 
2026) exige de son côté un seul identifiant de charge de travail par agent (qui peut être un SPIFFE ID), 
des justificatifs liés cryptographiquement et à expiration explicite, et interdit au grand modèle de langage 
d’accéder aux justificatifs de l’agent[93].
Émettre l’identité
SPIFFE et SPIRE sont des projets diplômés de la Cloud Native Computing Foundation (annonce du 20 
septembre 2022; niveau « Graduated » atteint le 23 août 2022 pour SPIFFE et le 22 août 2022 pour SPIRE selon 
leurs pages de projet) [116, 117, 321]. Un SPIFFE ID prend la forme spiffe://domaine-de-confiance/chemin. 
Le justificatif correspondant, le SVID, existe en deux formats, X.509-SVID et JWT-SVID, tous deux délivrés 
par la Workload API sans secret préalable; l’X.509-SVID est renouvelé automatiquement, tandis que le 
JWT-SVID, de courte durée, est redemandé au besoin; SPIFFE recommande l’X.509-SVID lorsque c’est 
possible, car un JWT-SVID peut être rejoué[322]. La fédération d’identité OpenID Connect (OIDC) des 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 119 sur 283


---
## [Page PDF 120]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
fournisseurs infonuagiques (identités gérées) offre une solution équivalente pour les agents hébergés sur 
une seule plateforme.
Le brouillon WIMSE « Workload Identity Practices » (draft-ietf-wimse-workload-identity-practices-07, version 
du 22 septembre 2026, soumis le 30 juin 2026 au groupe de pilotage de l’ingénierie Internet (IESG)) recom­
mande des justificatifs émis par la plateforme, de courte durée et ne dépassant pas la vie de l’instance, une 
audience distincte par cible, la preuve de possession, l’abandon des variables d’environnement lorsque la 
plateforme offre mieux et l’invalidation à la fin de la charge de travail[323]. Ces deux brouillons WIMSE ne 
sont pas des RFC; le cadre s’en sert comme références de conception.
Microsoft Entra Agent ID illustre une mise en œuvre commerciale, parmi d’autres. Une identité d’agent n’y 
a pas de justificatifs propres : elle obtient ses jetons par un gabarit (agent identity blueprint) qui porte les 
justificatifs et les politiques d’accès conditionnel héritées par toutes ses identités; désactiver le gabarit bloque 
toutes ces identités. Chaque agent a un parrain (sponsor), responsable métier, et un propriétaire, responsable 
technique[90]. Depuis juillet 2026, Copilot Studio crée automatiquement une telle identité pour chaque 
nouvel agent[48]. Le service est offert à tous les clients Entra, mais l’extension aux agents des fonctions de 
sécurité (accès conditionnel, protection des identités) requiert une licence Microsoft Agent 365[324].
EXIG-IAM-03 · DOIT
Identité propre, distincte et non partagée
Chaque agent inscrit au registre DOIT disposer de sa propre identité non humaine, rattachée à sa fiche 
(section 11.4) et à un parrain nommé. Une identité distincte par instance est exigée lorsque des instances 
servent des mandants, des locataires ou des environnements différents, ou lorsqu’il faut pouvoir en 
révoquer une seule. Une identité d’agent n’est jamais partagée entre agents ni utilisée par une personne, 
et un agent n’utilise jamais le compte d’une personne.
Pourquoi : l’OWASP classe la réutilisation d’identités non humaines (NHI9) et leur usage par des humains (NHI10) 
parmi les dix risques principaux[91]; sans identité propre, ni l’audit ni la révocation ne peuvent viser un agent précis.
EXIG-IAM-04 · DOIT
Justificatif cryptographique émis par la plateforme
L’identité d’un agent DOIT reposer sur un justificatif cryptographique émis par la plateforme, de courte 
durée, renouvelé automatiquement et valide au plus pour la vie de l’instance : X.509-SVID (à privilégier) 
ou JWT-SVID SPIFFE, ou identité fédérée OIDC du fournisseur infonuagique. Les justificatifs sont isolés 
par environnement (développement, essai, production).
Pourquoi : un justificatif émis par la plateforme est de courte durée, se renouvelle seul, cesse d’être valide avec 
l’instance et n’exige aucun secret déployé avec la charge de travail; c’est la voie que décrivent SPIFFE et les pratiques 
WIMSE[322, 323].
EXIG-IAM-05 · NE DOIT PAS
Aucun secret statique partagé
Un agent NE DOIT PAS s’authentifier au moyen d’une clé d’API statique, d’un mot de passe ou d’un 
secret client de longue durée partagé. Aucun secret ne figure dans le code, les définitions d’agents, les 
invites, les fichiers de configuration versionnés ni, lorsque la plateforme offre un mécanisme d’émission, 
dans les variables d’environnement. Un secret résiduel imposé par un système patrimonial est conservé 
dans un coffre, renouvelé automatiquement et inscrit comme dérogation (section 11.6).
Pourquoi : le brouillon AIMS qualifie les clés d’API statiques d’antipatron[93] et l’OWASP range la fuite de secrets 
(NHI2) et les secrets de longue durée (NHI7) parmi les risques majeurs[91].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 120 sur 283


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
