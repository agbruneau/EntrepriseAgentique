# chunk_15 — pages PDF 141 à 152 (sur 283)



---
## [Page PDF 141]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
approbation humaine pour toute exécution qui demande des privilèges ou des destinations réseau 
supplémentaires. Pendant l’exécution, une surveillance DOIT détecter les comportements anormaux 
(processus inattendus, connexions refusées, volumes d’écriture inhabituels).
Pourquoi : séparer génération et exécution empêche qu’un code piégé s’exécute du seul fait que le modèle l’a écrit[28].
EXEMPLE DE MISE EN ŒUVRE SUR KUBERNETES
Dans Kubernetes, l’objet RuntimeClass, stable depuis la version 1.20 (API node.k8s.io/v1), permet de 
choisir pod par pod une configuration d’exécution plus isolée, au prix d’un surcoût[373]. Le sous-projet 
kubernetes-sigs/agent-sandbox (SIG Apps) orchestre des bacs à sable d’agents au-dessus de gVisor ou 
de Kata Containers, avec les ressources Sandbox, SandboxTemplate, SandboxWarmPool et SandboxClaim 
(API v1beta1)[137]. Une réserve préchauffée réduit la latence; chaque bac à sable qu’on en tire reste 
dédié à une seule tâche ou à une seule session, conformément à EXIG-SEC-09. Ces composants sont des 
exemples, non des exigences.
9.8 Chaîne d’approvisionnement agentique
Un agent assemble des composants qu’il n’a pas écrits : modèles, serveurs MCP, agents distants, compé­
tences (skills), gabarits d’invites, bibliothèques et cadriciels. Chacun peut être compromis à la source ou 
modifié après son approbation. Cette section fixe les règles de provenance, d’intégrité et de risque de tiers. 
Les mécanismes de version et de catalogue sont décrits à la section 6.8, et les contrôles propres au protocole 
MCP à la section 6.5.
Des menaces documentées
Invariant Labs a décrit le 1er avril 2025 l’empoisonnement d’outil (tool poisoning), soit des instructions 
malveillantes cachées dans la description d’un outil, et la substitution après approbation (rug pull), soit la 
modification de cette description une fois l’outil approuvé[220]. La fiche de sécurité MCP de l’OWASP reprend 
ces attaques, étend l’empoisonnement aux schémas et aux valeurs de retour, et décrit aussi l’ombrage 
(shadowing) : la description d’un serveur malveillant modifie l’usage des outils d’un autre serveur[221]. Le 
MCP Top 10, encore en bêta, classe l’empoisonnement d’outil en MCP03, la chaîne d’approvisionnement 
en MCP04 et les serveurs MCP fantômes en MCP09[222]. Pour les compétences, l’AST10 recense notamment 
les compétences malveillantes (AST01), la compromission de la chaîne d’approvisionnement (AST02) et la 
dérive des mises à jour (AST07)[374]. Hou et ses coauteurs proposent enfin d’analyser un serveur MCP selon 
les quatre phases de son cycle de vie (création, déploiement, exploitation, maintenance), avec 16 scénarios 
de menace répartis entre quatre types d’attaquants[224].
EXEMPLE
Un serveur MCP de conversion de devises est approuvé en mars. En juin, son éditeur publie une nouvelle 
description qui demande au modèle de joindre « pour vérification » le contenu de la conversation à 
chaque appel. Sans épinglage, l’agent suit la nouvelle consigne dès le lendemain; avec EXIG-SEC-18, la 
passerelle constate que l’empreinte a changé et suspend l’outil jusqu’à une nouvelle revue.
EXIG-SEC-18 · DOIT
Provenance approuvée et intégrité vérifiée à l’exécution
Un agent DOIT invoquer uniquement des serveurs MCP, agents distants, compétences et modèles 
inscrits au catalogue d’entreprise après revue de leur définition complète (nom, titre, description, 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 141 sur 283


---
## [Page PDF 142]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
icônes, schémas d’entrée et de sortie, annotations et _meta). À chaque tools/list (EXIG-MCP-20) et 
avant chaque exécution, la passerelle d’agents DOIT vérifier que la définition présentée correspond 
à l’empreinte épinglée au catalogue et, en cas d’écart, retirer et suspendre le composant jusqu’à une 
nouvelle approbation.
Pourquoi : l’épinglage par empreinte, revérifié avant exécution, neutralise la substitution après approbation, et la 
revue de la définition complète à l’inscription réduit le risque d’empoisonnement d’outil[221].
Signature et nomenclature
La spécification A2A permet de signer une carte d’agent en JWS après canonisation JCS (RFC 8785), le 
champ signatures étant exclu du contenu signé; les clients devraient vérifier au moins une signature avant 
de faire confiance à une carte, et une clé expirée ou révoquée ne doit pas servir à la vérification[68]. Le cœur 
de MCP n’exige pas de signature des messages[221] : l’intégrité d’un serveur MCP repose donc sur l’épinglage 
par empreinte et sur la signature des artefacts déployés.
EXIG-SEC-19 · DOIT
Signature des cartes d’agent et des artefacts
Toute carte d’agent inscrite au catalogue d’entreprise et rattachée au registre DOIT être signée, et 
la passerelle comme les clients DOIVENT vérifier au moins une signature valide, faite avec une clé 
ni expirée ni révoquée, avant de faire confiance à la carte. Les artefacts déployés (images de conte­
neurs, paquets de serveurs MCP, compétences) DEVRAIENT être signés et leur signature vérifiée au 
déploiement.
Pourquoi : la spécification A2A se borne à recommander la vérification d’au moins une signature; le cadre la rend 
obligatoire (choix du cadre), car sans signature un agent malveillant peut publier une carte qui imite un agent 
légitime[68].
EXIG-SEC-20 · DOIT
Nomenclature de chaque version d’agent
Chaque version d’un agent de risque modéré ou élevé DOIT être accompagnée d’une nomenclature 
tenue au registre  : bibliothèques et cadriciels (nomenclature logicielle, SBOM), modèles, gabarits 
d’invites système, serveurs MCP, agents distants et compétences, chacun avec sa version et son 
empreinte.
Pourquoi : lorsqu’une faille est annoncée dans un composant, la nomenclature permet de savoir sans délai quels 
agents l’utilisent (choix du cadre).
Isoler les fournisseurs d’outils les uns des autres
EXIG-SEC-21 · DOIT
Chaque serveur, un domaine de sécurité distinct
La passerelle DOIT traiter chaque serveur MCP et chaque agent distant comme un domaine de sécurité 
indépendant et non fiable : noms d’outils pleinement qualifiés par un espace de noms propre au serveur, 
interdiction qu’un serveur référence ou modifie les outils d’un autre, et surveillance des flux de données 
entre serveurs. Le trafic vers un serveur MCP ou un agent absent du catalogue ou du registre DOIT 
être bloqué et signalé à la sécurité.
Pourquoi : l’OWASP recommande cet isolement par une passerelle contre l’ombrage, la vérification des noms de 
paquets contre le typosquattage et, contre les outils typosquattés, des noms pleinement qualifiés avec versions 
épinglées (ASI02); les serveurs fantômes échappent sinon à tout contrôle[28, 221, 222].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 142 sur 283


---
## [Page PDF 143]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Risque de tiers
Le NIST AI RMF consacre la catégorie GOVERN 6 aux risques venant des logiciels, des données et des 
autres éléments de la chaîne d’approvisionnement de tiers : GOVERN 6.1 vise les politiques sur ces risques, 
y compris la propriété intellectuelle, et GOVERN 6.2 les processus de contingence en cas de défaillance ou 
d’incident d’un système de tiers jugé à haut risque; les serveurs MCP et les agents externes en relèvent[74]. 
Le règlement européen sur l’IA (RIA), tel que modifié par le règlement (UE) 2026/1744, exige en outre du 
fournisseur d’un système à haut risque un accord écrit avec les tiers qui fournissent un système d’IA, un 
modèle d’IA, des outils, services, composants ou processus utilisés ou intégrés dans le système, sauf pour les 
tiers qui rendent publics, sous licence libre et ouverte, des outils, services, processus ou composants autres 
que des modèles d’IA à usage général (art. 25(4))[61, 375].
EXIG-SEC-22 · DOIT
Évaluation des tiers et plan de contingence
Avant son inscription au catalogue, tout serveur MCP, agent ou modèle fourni par un tiers DOIT faire 
l’objet d’une évaluation de sécurité proportionnée au palier de ses outils. Tout composant de tiers utilisé 
par un agent de risque élevé DOIT disposer d’un plan de contingence (désactivation, solution de repli, 
avis aux consommateurs). Lorsqu’un composant est intégré à un système à haut risque au sens du RIA, 
un accord écrit DOIT être conclu avec le tiers (chapitre 13).
Pourquoi : la sécurité d’un agent ne dépasse pas celle du moins sûr de ses fournisseurs; GOVERN 6 en fait une 
pratique de gestion attendue (le NIST AI RMF est un cadre volontaire) et l’article 25(4) du RIA une obligation d’accord 
écrit pour le fournisseur d’un système à haut risque[74, 375].
9.9 Assurance : tests et équipe rouge
Les contrôles des sections précédentes ne valent que s’ils résistent à une attaque réelle. Cette section 
fixe les essais exigés avant la mise en production et pendant l’exploitation; elle ajoute un volet adverse à 
l’évaluation continue de la qualité (section 10.4). Les lignes directrices conjointes du NCSC britannique, de 
l’agence américaine CISA (Cybersecurity and Infrastructure Security Agency) et de leurs partenaires font 
de la sécurité une exigence de base aux quatre phases du cycle de vie : la conception, le développement, 
le déploiement ainsi que l’exploitation et la maintenance[376]. Le guide de l’OWASP sur la sécurisation des 
applications agentiques (version 1.0 du 27 juillet 2025) fournit aux équipes de développement les recom­
mandations techniques correspondantes[377].
Équipe rouge avant la production
Une équipe rouge (red team) attaque l’agent comme le ferait un adversaire. L’OWASP recommande des 
tests périodiques qui simulent le détournement d’objectif et vérifient l’efficacité du retour arrière (ASI01)[28]. 
MITRE ATLAS fournit le vocabulaire commun de ces scénarios et intègre des techniques propres aux agents, 
comme AML.T0110 AI Agent Tool Poisoning, AML.T0124 Autonomous Attack Orchestration et AML.T0133 
Discover AI Agent Runtime Capabilities[352].
EXIG-SEC-23 · DOIT
Exercice d’équipe rouge propre aux agents
Tout agent de classe de risque modérée ou élevée DOIT subir, avant sa mise en production puis 
au moins une fois par année (choix du cadre), un exercice d’équipe rouge propre aux agents, mené 
par une équipe indépendante de l’équipe de développement. Les scénarios couvrent au minimum le 
détournement d’objectif par contenu non fiable, l’exfiltration de données, l’empoisonnement d’outil et 
de mémoire et l’abus de délégation; chacun est rattaché à un risque ASI et, s’il y a lieu, à une technique 
MITRE ATLAS. Un constat de gravité critique non corrigé DOIT bloquer la mise en production.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 143 sur 283


---
## [Page PDF 144]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Pourquoi : choix du cadre, selon lequel seul un adversaire qui cherche activement révèle les combinaisons que 
l’équipe de conception n’a pas imaginées; l’OWASP recommande des tests périodiques de détournement d’objectif 
(ASI01)[28].
Essais automatisés à chaque version
AgentDojo est un environnement d’évaluation des attaques et défenses par injection qui comprend 97 tâches 
réalistes et 629 cas de test de sécurité[378]. Il montre qu’on peut mesurer la résistance à l’injection de façon 
reproductible; on peut donc l’intégrer à la chaîne d’intégration et de déploiement continus comme n’importe 
quel test de régression.
EXIG-SEC-24 · DOIT
Suite d’attaques dans la chaîne d’intégration
La chaîne d’intégration et de déploiement DOIT exécuter, à chaque nouvelle version d’un agent 
(modèle, invite système, outil ou palier modifié), une suite d’attaques automatisées rédigées en français 
et en anglais, par exemple des scénarios dérivés d’AgentDojo, et bloquer le déploiement si le taux de 
réussite des attaques dépasse le seuil fixé à la fiche de l’agent.
Pourquoi : un changement de modèle ou d’invite peut affaiblir silencieusement la résistance d’un agent; seule une 
mesure à chaque version détecte cette régression.
EXIG-SEC-25 · DOIT
Vérification des contrôles déterministes
Les essais DOIVENT démontrer, par des cas négatifs, que : la passerelle retire les outils d’envoi après la 
lecture d’un contenu non fiable (EXIG-SEC-06); un jeton d’approbation altéré, rejoué ou lié à d’autres 
arguments est refusé; un bac à sable ne peut joindre ni une destination hors liste, ni le DNS, ni le service 
de métadonnées; une définition d’outil modifiée est bloquée (EXIG-SEC-18).
Pourquoi : ces contrôles sont binaires; un test qui échoue révèle une faille certaine, alors qu’un test d’injection réussi 
ne mesure qu’une probabilité.
Exercices de compromission et de coupe-circuit
Le règlement européen sur l’IA exige que les personnes chargées de la supervision puissent interrompre 
un système à haut risque au moyen d’un bouton d’arrêt ou d’une procédure analogue qui l’amène à un 
état sûr (art. 14(4)e))[290], et le NIST AI RMF (MANAGE 2.4) demande des mécanismes et des responsabilités 
pour désactiver un système qui s’écarte de l’usage prévu[99]. Au Québec, l’Énoncé de principes pour une 
utilisation responsable de l’IA par les organismes publics demande aux organismes publics, à son principe 
11, des mécanismes de validation, d’intervention humaine ou d’arrêt, particulièrement pour les systèmes 
dotés d’autonomie comme l’IA agentique, et cite en illustration des mécanismes d’arrêt d’urgence[379]. La 
propagation du coupe-circuit (kill switch) par la passerelle est décrite à la section 9.4.
EXIG-SEC-26 · DOIT
Exercice trimestriel de compromission d’agent
Au moins une fois par trimestre (choix du cadre), la plateforme DOIT exercer le scénario d’un agent 
compromis : arrêt par le coupe-circuit, révocation de ses identités et de ses jetons, mise en quarantaine 
et préservation des preuves. Le délai réel de révocation DOIT être mesuré et comparé à la cible de 15 
minutes du tableau 61; tout dépassement DOIT ouvrir une action corrective. Cet exercice PEUT se 
combiner à l’essai trimestriel du coupe-circuit prévu à la section 7.8.
Pourquoi : un mécanisme d’arrêt jamais exercé n’est qu’une hypothèse; seul l’exercice prouve qu’il fonctionne et 
dans quel délai.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 144 sur 283


---
## [Page PDF 145]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
À RETENIR
Lorsque le risque résiduel reste intolérable malgré ces contrôles, la bonne réponse n’est pas un filtre de 
plus, mais un flux déterministe (N0) ou un agent consultatif (N1). Le NCSC l’énonce sans détour : si le 
risque résiduel est intolérable, un modèle de langage n’est peut-être pas la bonne solution[98].
10 Observabilité, évaluation et FinOps
On ne gouverne que ce qu’on voit. Ce chapitre impose une trace OpenTelemetry de bout en bout, reliée 
par un même contexte W3C du canal jusqu’à l’outil, et un journal d’audit inaltérable, distinct de cette 
trace. Il organise l’évaluation continue en trois paliers, du contrat vérifié à chaque modification jusqu’à 
l’échantillonnage de la production. Il donne enfin à chaque tâche une enveloppe budgétaire et à chaque 
agent un coût par tâche réussie, imputé à un centre de coûts.
10.1 Traçage de bout en bout
Cette section fixe la manière dont chaque exécution d’agent produit une trace unique, faite d’étapes 
chronométrées (spans), qui relie la demande d’origine à chaque appel de modèle, d’outil et d’agent.
Un mécanisme stable, des conventions mouvantes
OpenTelemetry fournit un mécanisme de collecte (API et protocole OTLP, de l’anglais OpenTelemetry Pro­
tocol) et des conventions sémantiques qui nomment les attributs. Le mécanisme est stable; les conventions de 
l’IA générative (gen_ai.*) sont toutes au niveau Development, qui admet ruptures et retraits[188, 380]. Depuis 
la v1.42.0 (12 juin 2026), elles vivent dans le dépôt dédié semantic-conventions-genai [180, 381]. Ce dépôt n’a 
publié aucune version étiquetée : la dernière version publiée qui les contient comme conventions en vigueur 
est la v1.41.1 de semantic-conventions (correctif du 11 mai 2026 de la v1.41.0 du 28 avril 2026), les versions 
suivantes les déclarant obsolètes (v1.42.0, 12 juin 2026); la branche principale du nouveau dépôt remplace 
déjà gen_ai.usage.cache_creation.input_tokens par gen_ai.usage.cache_write.input_tokens et re­
structure les métriques de jetons[119, 181, 380, 381, 382, 383, 384]. Le cadre impose donc le mécanisme, épingle 
une version des conventions et lit les données par une couche de correspondance. L’épinglage ne dicte 
toutefois pas ce que les bibliothèques d’instrumentation émettent  : la convention demande que les 
instrumentations existantes ne changent pas par défaut la version GenAI qu’elles produisent (v1.36.0 ou 
antérieure) et qu’elles prévoient la variable d’environnement OTEL_SEMCONV_STABILITY_OPT_IN, dont la 
valeur gen_ai_latest_experimental fait émettre la dernière version expérimentale prise en charge par 
l’instrumentation, et non une version précise[119]. L’instrumentation Python d’OpenAI, par exemple, reste 
sans ce réglage aux conventions v1.30.0[385]. Le catalogue consigne donc, pour chaque composant, la version 
réellement émise et le réglage de cette variable.
EXIG-OBS-01 · DOIT
OpenTelemetry obligatoire, conventions épinglées
Tout composant d’une exécution d’agent (canal, orchestrateur, passerelles, agent, serveur MCP, 
consommateur d’événements) DOIT émettre traces et métriques par OpenTelemetry, en OTLP, vers 
le collecteur de la plateforme, selon la version des conventions GenAI épinglée au catalogue (v1.41.0, 
jusqu’à l’homologation d’une version étiquetée du dépôt dédié). Tableaux de bord, alertes et calculs de 
coûts lisent les données par une couche de correspondance versionnée; un changement de version des 
conventions se gère comme un changement de contrat (section 6.8).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 145 sur 283


---
## [Page PDF 146]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Pourquoi : au niveau Development, des ruptures sont admises et un signal peut être retiré, sans garantie de dépré­
ciation préalable[188]; sans épinglage, un tableau de bord se vide en silence.
Propagation du contexte
W3C Trace Context est une Recommandation du W3C (version du 23 novembre 2021). L’en-tête 
traceparent de version 00 compte 55 caractères; un identifiant entièrement nul est invalide, la version ff 
est interdite, et tracestate compte au plus 32 membres[103].
En-tête traceparent (exemple canonique de la spécification)
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             └┘ └──── identifiant de trace ─────┘ └─ span parent ─┘ └┘
           version        (32 hex)                   (16 hex)     indicateurs
Ce contexte voyage dans les en-têtes HTTP, dans les clés traceparent, tracestate et baggage que MCP 
2026-07-28 réserve dans _meta [162] (EXIG-MCP-16), dans les appels A2A (EXIG-A2A-13) et dans l’extension 
CloudEvents Distributed Tracing (EXIG-EVT-04). Un composant poursuit la trace d’une requête entrante si 
son traceparent est valide et, selon le choix du cadre, vient d’une source de confiance; à une frontière de 
confiance, il peut la redémarrer, ce que la spécification prévoit pour écarter une surface d’attaque par déni 
de service et limiter l’exposition d’information[103]. Enfin, traceparent identifie une trace, pas une demande 
métier.
EXIG-OBS-02 · DOIT
Contexte validé, poursuivi ou redémarré aux frontières
Les passerelles d’agents et de modèles DOIVENT valider le contexte reçu (longueurs, identifiants non 
nuls, version admise) et remplacer tout en-tête invalide par une nouvelle trace. Un composant interne 
DOIT poursuivre la trace d’un autre composant interne; un contexte venu de l’extérieur (partenaire, 
agent tiers, point de rappel HTTP) DOIT être remplacé par une nouvelle trace qui le conserve comme 
lien de span (choix du cadre).
Pourquoi : une trace coupée ne se reconstitue plus, et une trace imposée de l’extérieur peut brouiller une enquête.
EXIG-OBS-03 · DOIT
Identifiants métier portés à part
Chaque span DOIT porter l’identifiant de tâche attribué par l’orchestrateur et, pour un appel A2A, 
le taskId et le contextId. Une déduplication ou une clé d’idempotence NE DOIT PAS se fonder sur 
traceparent.
Pourquoi : une trace peut être redémarrée à une frontière, alors qu’une tâche garde son identité de bout en bout 
(section 7.6).
Hiérarchie des spans
Les conventions nomment chaque span (figure 21) : invoke_workflow {gen_ai.workflow.name} (INTER­
NAL) pour un flux multiagent; invoke_agent {gen_ai.agent.name}, de type CLIENT pour un agent 
distant et INTERNAL dans le même processus; execute_tool {gen_ai.tool.name} (INTERNAL) pour 
un outil; {gen_ai.operation.name} {gen_ai.request.model} pour une inférence[119, 120]. En v1.41.0, 
gen_ai.operation.name admet chat, create_agent, embeddings, execute_tool, generate_content, 
invoke_agent, invoke_workflow, retrieval et text_completion  : aucune valeur «  handoff  » 
n’existe, et un transfert entre agents se trace par invoke_agent. Les appels MCP ont leur propre 
convention  : spans {mcp.method.name} {cible}, attribut requis mcp.method.name, histogrammes 
mcp.client.operation.duration et mcp.server.operation.duration [386]. A2A n’en a pas en v1.41.0 (le 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 146 sur 283


---
## [Page PDF 147]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
dépôt dédié en définit une, non publiée, au niveau Development[241]) et se trace par invoke_agent (section 
6.6).
SPANS (CONVENTIONS OPENTELEMETRY GENAI ET MCP)
traceparent 00-4bf92f3577b34da6a3ce929d0e0e4736-…-01
invoke_workflow traitement-dossier
chat modele-compact
(routage)
invoke_agent agent-risque-credit
CLIENT · A2A
invoke_agent agent-risque-credit
INTERNAL
chat modele-raisonnement
execute_tool lire_dossier
tools/call lire_dossier
MCP CLIENT
chat modele-raisonnement
attente d’approbation (INPUT_REQUIRED)
execute_tool enregistrer_decision
chat modele-compact
(réponse)
Événement gen_ai.evaluation.result rattaché au span
0 s
≈ 40 s
Attributs portés
gen_ai.operation.name
gen_ai.agent.name
gen_ai.agent.version
gen_ai.provider.name
gen_ai.request.model
gen_ai.response.model
gen_ai.usage.input_tokens
gen_ai.usage.output_tokens
gen_ai.usage.cache_read
.input_tokens
gen_ai.tool.name
gen_ai.tool.call.id
mcp.method.name
error.type
Attributs d’entreprise sous
préfixe DNS inversé :
ca.entreprise.cost_center
Figure 21 — Une trace distribuée de bout en bout. Une seule trace relie le flux, le routage, la délégation A2A, les inférences de l’agent 
appelé, l’appel MCP, l’attente d’approbation et l’écriture finale; le résultat d’évaluation s’attache au span évalué. À droite, les attributs 
portés, dont un attribut d’entreprise sous préfixe DNS inversé. Source : cadre CRE-IA-2026-01, d’après les conventions OpenTelemetry 
GenAI et MCP (v1.41.0).
EXIG-OBS-04 · DOIT
Hiérarchie de spans normalisée
Chaque exécution DOIT produire la hiérarchie de la version épinglée : invoke_workflow pour un flux 
multiagent, invoke_agent par agent appelé, un span par inférence, execute_tool par appel d’outil avec 
le span MCP CLIENT correspondant. Attentes d’approbation, compensations et refus de la passerelle 
y figurent comme spans ou événements. Toute valeur de gen_ai.operation.name hors convention est 
inscrite au catalogue comme extension.
Pourquoi : une hiérarchie commune se lit avec les mêmes requêtes, quel que soit le cadriciel.
Attributs et métriques
Sur un span d’inférence, la convention ne requiert que gen_ai.operation.name et gen_ai.provider.name 
[119]. Le cadre rend obligatoires, par une politique plus stricte que la convention, les attributs dont 
dépendent l’audit, le diagnostic et l’imputation (tableau 41). Deux pièges de nommage : la version d’agent 
s’écrit gen_ai.agent.version, avec un point (ajoutée en v1.40.0)[180], et gen_ai.provider.name remplace 
gen_ai.system depuis la v1.37.0[387].
Tableau 41 — Attributs de trace exigés et niveau dans la convention OpenTelemetry v1.41.0
Catégorie
Attribut
Niveau dans la 
convention
Exigence du cadre
Opération
gen_ai.operation.name
Requis
Obligatoire
Fournisseur
gen_ai.provider.name
Requis (inférence, 
plongements, créa­
tion et invocation 
d’agent)
Obligatoire
Modèle
gen_ai.request.model; gen_ai.response.model
Conditionnel; re­
commandé
Obligatoires : alias 
demandé et modèle 
servi
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 147 sur 283


---
## [Page PDF 148]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Catégorie
Attribut
Niveau dans la 
convention
Exigence du cadre
Jetons
gen_ai.usage.input_tokens (cache compris); 
gen_ai.usage.output_tokens
Recommandés
Obligatoires
Cache
gen_ai.usage.cache_read.input_tokens; 
gen_ai.usage.cache_creation.input_tokens
Recommandés; le 
second devient 
cache_write dans la 
branche non pu­
bliée
Obligatoires si le 
fournisseur les ren­
voie
Fin de généra­
tion
gen_ai.response.finish_reasons
Recommandé
Obligatoire
Agent
gen_ai.agent.id, .name, .version
Conditionnels
Obligatoires; identi­
fiant du registre
Outil
gen_ai.tool.name; gen_ai.tool.call.id
Requis sur 
execute_tool; re­
commandé
Obligatoires
MCP
mcp.method.name
Requis
Obligatoire
Erreur
error.type
Conditionnel
Obligatoire en cas 
d’erreur
Entreprise
ca.entreprise.cost_center, 
ca.entreprise.task_id, ca.entreprise.autonomy_level, 
ca.entreprise.approval.approver
Hors convention
Obligatoires; appro­
bateur sous pseudo­
nyme
Sources : conventions OpenTelemetry GenAI et MCP v1.41.0[119, 386]; dernière colonne : choix du cadre.
Pour les métriques, la v1.41.0 définit les histogrammes 
gen_ai.client.operation.duration 
(secondes, requis) et 
gen_ai.client.token.usage (jetons, recommandé)[388]; la branche non 
publiée 
remplace 
l’histogramme 
gen_ai.client.token.usage 
(v1.41.0) 
par 
des 
compteurs 
gen_ai.client.inference.usage.* et des histogrammes gen_ai.client.inference.operation.*, et 
scinde gen_ai.client.operation.duration pour l’inférence[388, 389], migration qu’absorbera la couche de 
correspondance.
EXIG-OBS-05 · DOIT
Attributs et métriques exigés
Chaque span DOIT porter, parmi les attributs que le tableau 41 rend obligatoires, ceux qui s’appliquent 
à son type (inférence, agent, flux, outil, appel MCP), et chaque composant DOIT exposer les métriques 
de durée et de jetons de la version épinglée. Un composant qui ne les produit pas NE DOIT PAS être 
homologué; un attribut obligatoire manquant en production DOIT déclencher une alerte.
Pourquoi : sans modèle servi, version d’agent ni jetons, on ne relie pas une régression à un déploiement et l’on 
n’impute aucun coût.
EXIG-OBS-06 · DOIT
Attributs d’entreprise sous préfixe DNS inversé
Les attributs propres à l’entreprise DOIVENT porter le préfixe de son domaine inversé (p. ex. 
ca.entreprise.cost_center), en minuscules et en snake_case, et être inscrits au catalogue; les préfixes 
enterprise. et otel. sont interdits. Une personne, approbateur compris, n’y figure que sous un 
identifiant pseudonyme.
Pourquoi : OpenTelemetry recommande ce préfixe contre les collisions et réserve otel.* [390]; l’identifiant d’un 
approbateur est un renseignement personnel, et un identifiant pseudonyme le demeure (section 12.2).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 148 sur 283


---
## [Page PDF 149]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Statut des versions : voir la section 10.1. 10.2 Contenu des invites et des réponses
Cette section règle le cas le plus délicat de la télémétrie : le texte des invites, des réponses et des arguments 
d’outils, utile au diagnostic mais souvent chargé de renseignements personnels (RP).
Contrairement à une idée répandue, la convention n’exclut pas ce contenu des spans. Depuis 
la v1.37.0 (la v1.38.0 pour les arguments et résultats d’outils), elle le place dans des attri­
buts «  Opt-In  » (gen_ai.input.messages, gen_ai.output.messages, gen_ai.system_instructions 
et, depuis la v1.38.0, gen_ai.tool.call.arguments et gen_ai.tool.call.result, entre autres), que 
les instrumentations ne devraient pas capturer par défaut[119, 387, 391]. La branche non publiée 
nomme désormais, dans la convention, la variable OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT 
(NO_CONTENT par défaut, SPAN_ONLY, EVENT_ONLY ou SPAN_AND_EVENT)[392]; dans la v1.41.0, la variable 
OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT n’est pas une convention, mais un réglage 
des bibliothèques Python[385]. La convention prévoit trois modes  : ne rien enregistrer (défaut), 
enregistrer le contenu en attributs, ou le stocker à l’extérieur en ne plaçant sur le span qu’une 
référence, dont le format n’est pas normalisé dans la v1.41.0 (la branche non publiée définit des attri­
buts gen_ai.input.messages_ref, gen_ai.output.messages_ref, gen_ai.system_instructions_ref et 
gen_ai.tool.definitions_ref, qui portent un URI absolu[380])[119]. Le cadre retient le premier mode en 
production et le troisième pour le débogage.
Le processeur redaction du Collector OpenTelemetry supprime les attributs absents d’une liste 
d’autorisation (vide, elle supprime tout), masque les valeurs selon des expressions régulières et peut les 
hacher, les variantes HMAC (code d’authentification de message par hachage) étant recommandées pour 
les données à faible entropie; sa stabilité est Beta pour les traces, mais Alpha pour les métriques et les 
journaux[141]. Quant au bagage (baggage), W3C Baggage n’est qu’une recommandation candidate, qui avertit 
de ne pas transporter d’information confidentielle au-delà d’une frontière de confiance[393].
À RETENIR
Les métadonnées se tracent toujours; le contenu, jamais par défaut. Pour comprendre une défaillance, 
on consulte le texte exact dans un dépôt chiffré, à accès restreint et de courte durée, par une référence 
placée sur le span.
EXIG-OBS-07 · NE DOIT PAS
Aucun contenu dans la télémétrie de production
En production, les spans, événements et journaux de télémétrie NE DOIVENT PAS contenir le texte 
des invites, des réponses ou des instructions système, ni les arguments ou résultats d’outils, ni les autres 
contenus que la convention soumet à la capture de contenu (requêtes de recherche, variables d’invite, 
mémoire de l’agent). Cette interdiction est une politique du cadre, plus stricte que la désactivation par 
défaut que prévoit la convention.
Pourquoi : la télémétrie est copiée vers plusieurs systèmes et lue par de nombreuses équipes; le contenu y exposerait 
des RP hors de toute finalité déclarée (section 12.2).
EXIG-OBS-08 · DOIT
Contenu de débogage hors trace et de courte durée
La capture du contenu pour un diagnostic DOIT être activée par une décision documentée (agent, 
motif, période bornée, accord du responsable technique et, si des RP sont en cause, du responsable 
de la protection des renseignements personnels), passer par le caviardage, être stockée dans un dépôt 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 149 sur 283


---
## [Page PDF 150]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
chiffré dont chaque accès est journalisé, et n’apparaître sur le span que par une référence. Le contenu 
est détruit après 14 jours au plus (choix du cadre).
Pourquoi : le mode par référence sépare la trace, largement partagée, du contenu, réservé à quelques personnes.
EXIG-OBS-09 · DOIT
Caviardage à la sortie du périmètre
Toute télémétrie qui quitte la plateforme DOIT traverser un collecteur qui applique une liste 
d’autorisation fermée d’attributs, masque les motifs de RP et de secrets et remplace les identifiants à 
faible entropie par un HMAC à clé gérée par l’entreprise. Les règles de masquage DOIVENT être testées 
en français et en anglais à chaque modification.
Pourquoi : avec une liste fermée par défaut, ce qu’on a oublié de classer ne sort pas[141].
EXIG-OBS-10 · NE DOIT PAS
Aucun renseignement personnel dans le bagage
Le bagage W3C et tracestate NE DOIVENT PAS contenir de RP, de secrets ni de données confiden­
tielles; seuls y figurent des identifiants techniques, comme le centre de coûts. La passerelle DOIT retirer 
tout membre du bagage absent de la liste inscrite au catalogue.
Pourquoi : un système qui reçoit le bagage devrait le transmettre à ses requêtes sortantes, de sorte que ses clés et 
ses valeurs peuvent atteindre d’autres systèmes[393].
10.3 Journal d’audit
Cette section fixe le journal d’audit, qui répond à une autre question que la trace : non pas « que s’est-il 
passé techniquement? », mais « qui a fait quoi, au nom de qui, sous quelle autorité? ».
Une trace est technique, souvent échantillonnée et conservée selon la fiche de l’agent (section 12.2). Le 
journal d’audit est exhaustif pour les actions à effet, inaltérable et signé. Le règlement européen sur l’IA exige 
que les systèmes à haut risque permettent techniquement l’enregistrement automatique des événements 
pendant toute leur durée de vie (art. 12) et que le déployeur conserve les journaux sous son contrôle pendant 
au moins six mois, sauf disposition contraire du droit de l’Union ou du droit national (art. 26(6)); pour 
l’annexe III, ces obligations s’appliquent à compter du 2 décembre 2027, selon le calendrier que modifie le 
règlement (UE) 2026/1744 (art. 113, tel que modifié par le règlement (UE) 2026/1744)[58, 61, 94, 394]. L’article 
12 n’impose ni signature ni format : l’enregistrement signé à cinq éléments est un choix du cadre, au-delà 
du minimum légal. ISO/IEC 42001 prévoit aussi l’enregistrement des journaux d’événements (annexe A, 
A.6.2.8)[395].
Les cinq éléments sont : (1) le mandant, sous pseudonyme; (2) l’agent, avec son identifiant au registre, 
sa version et celle de son invite système; (3) l’action, soit l’outil, la version de sa définition, l’empreinte 
SHA-256 des arguments et l’issue; (4) le modèle servi et sa version; (5) l’autorité, soit le jeton d’approbation 
(section 8.5), soit la règle qui permettait d’agir sans approbation. S’y ajoutent l’horodatage et les identifiants 
de corrélation : trace, tâche, taskId et contextId A2A[68], clé d’idempotence. L’enregistrement est canonisé 
selon la RFC 8785 (JCS), qui rend reproductibles le hachage et la signature de données JSON[236]; l’exemple 
complet figure à l’annexe C.
Enregistrement d’audit à cinq éléments (extrait, avant canonisation)
{
  "horodatage":  "2026-10-27T14:03:12.418Z",
  "correlation": { "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "tache": "tache-7f3c2a",
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 150 sur 283


---
## [Page PDF 151]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
                   "a2a_task_id": "…", "a2a_context_id": "…", "cle_idempotence": "…" },
  "mandant":   { "type": "user", "pseudonyme": "u-5d1e…" },
  "agent":     { "id": "agent-risque-credit", "version": "2.3.0", "invite_systeme": "sha256:…" },
  "action":    { "outil": "erp_enregistrer_decision", "definition": "1.4.1",
                 "arguments_sha256": "…", "issue": "succes" },
  "modele":    { "fournisseur": "…", "servi": "…", "version": "…" },
  "autorite":  { "approbation_jti": "…", "approbateur": "a-91c0…" },
  "precedent_sha256": "…",
  "signature": "<signature du service d’audit>"
}
EXIG-OBS-11 · DOIT
Journal d’audit distinct et exhaustif
Chaque action à effet (outil P2 ou P3), chaque approbation ou refus d’approbation, chaque refus de la 
passerelle (EXIG-IAM-18) et chaque arrêt par coupe-circuit DOIT produire un enregistrement d’audit, 
sans échantillonnage. Le journal DOIT être tenu dans un magasin distinct des traces, sous d’autres 
droits d’accès; aucune équipe qui exploite un agent n’a le droit d’y modifier ni d’y supprimer un 
enregistrement.
Pourquoi : une trace peut être échantillonnée ou purgée par l’exploitation; une preuve ne le peut pas.
EXIG-OBS-12 · DOIT
Enregistrement à cinq éléments, canonisé et signé
Chaque enregistrement DOIT contenir les cinq éléments et les identifiants de corrélation, être canonisé 
selon la RFC 8785, porter l’empreinte de l’enregistrement précédent du même flux et être signé par 
une clé du service d’audit, hors de portée des agents. Les arguments d’outil n’y figurent que par leur 
empreinte SHA-256, calculée sur leur forme canonisée; lorsqu’une approbation a eu lieu, l’empreinte 
d’approbation h (outil ‖ arguments canonisés, section 8.5) y figure aussi.
Pourquoi : choix du cadre; la canonisation de la RFC 8785[236] rend l’empreinte reproductible, de sorte que l’empreinte 
d’approbation, recalculée par la passerelle avant l’exécution, prouve que l’action exécutée est celle qui a été 
approuvée, et le chaînage rend toute suppression détectable.
EXIG-OBS-13 · DOIT
Inaltérabilité et conservation
Le journal d’audit DOIT être tenu en ajout seul, sur un stockage qui interdit modification et effacement 
avant échéance, et son intégrité DOIT être vérifiée automatiquement chaque jour. Il est conservé au 
moins 24 mois, davantage si le calendrier de conservation, un régime sectoriel ou une enquête l’exige, 
puis détruit ou anonymisé à l’échéance (EXIG-CON-10); la règle de conservation des décisions touchant 
une personne s’applique aussi (section 12.2). La table qui relie pseudonymes et personnes est gardée à 
part, sous le contrôle du responsable de la protection des renseignements personnels.
Pourquoi : un journal réinscriptible ne prouve rien; la durée de 24 mois et la vérification quotidienne, choix du cadre, 
dépassent les six mois du RIA pour couvrir une découverte tardive d’un incident.
10.4 Évaluation continue
Cette section fixe la manière dont l’entreprise prouve qu’un agent fait ce qu’on attend de lui, avant et 
pendant son exploitation. Un code HTTP 200 ne dit rien de la justesse d’une réponse : la qualité se mesure, 
en trois paliers (figure 22). Le volet adverse relève de la section 9.9, et la comparaison avec un agent unique, 
de la section 7.1.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 151 sur 283


---
## [Page PDF 152]

CRE-IA-2026-01 · Cadre de référence
10 Observabilité, évaluation et FinOps
Palier 3
Production, en continu
échantillon 5–10 %
Palier 2 — Trajectoires
préproduction, jeu de référence
50 à 200 scénarios, cas adverses
Palier 1 — Contrats déterministes
à chaque modification : schémas MCP, cartes
d’agent, outils simulés, règles de passerelle
Mesure en production
100 % des traces en erreur, relance ou refus
d’approbation; juges automatisés hors du chemin
critique et revue humaine; détection de dérive
Mesure de trajectoire
bons outils, bon ordre, bons arguments;
ancrage factuel dans les résultats d’outils;
respect des garde-fous et du budget
Mesure déterministe
tests de contrat et d’instantané du catalogue;
tests d’injection de fautes des sagas;
tests des politiques de la passerelle
Tout changement de modèle, d’invite, d’outil ou de version de protocole relance les paliers 1 et 2.
Figure 22 — Évaluation en trois paliers. Le palier 1 vérifie les contrats à chaque modification, le palier 2 mesure les trajectoires sur un 
jeu de référence en préproduction, le palier 3 échantillonne la production. Tout changement de modèle, d’invite, d’outil ou de version 
de protocole relance les deux premiers. Source : cadre CRE-IA-2026-01.
Palier 1 : contrats. Sans aucun modèle, il valide les schémas MCP et les cartes d’agent, teste les outils 
contre des doublures, vérifie les politiques de la passerelle (EXIG-IAM-21) et rejoue l’injection de fautes des 
sagas (EXIG-ORC-20). Les validateurs appliquent MCP 2026-07-28 : la spécification interdit de déréférencer 
automatiquement un $ref réseau et recommande de rejeter une référence externe non résolue et de borner 
la profondeur de validation[162]. La conformité passe par a2a-tck, dont les échecs aux tests de niveau MUST 
(obligatoire) sont bloquants[243], et, à titre informatif tant que le cadre officiel de conformité MCP se déclare 
instable, par ses tests (section 6.8).
Palier 2 : trajectoires. Sur un jeu de référence de 50 à 200 scénarios (fourchette du cadre), qui comprend cas 
nominaux, cas limites et tentatives d’injection en français et en anglais, on mesure la justesse de la trajectoire 
(bons outils, bon ordre, bons arguments), l’ancrage factuel dans les résultats d’outils et le respect des garde-
fous et du budget. Le cadre ne présume pas qu’un modèle rende la même sortie à entrées identiques : chaque 
scénario se répète. Évaluer un agent peut avoir des effets réels : l’article qui présente Magentic-One décrit 
AutoGenBench, dont les contrôles de répétition et d’isolation sont importants dès que les actions d’agents 
ont des effets de bord[279].
Palier 3  : production. On évalue de 5 à 10  % des traces (fourchette du cadre), plus toutes 
celles qui ont subi une erreur, une relance, un plafond atteint ou un refus d’approbation, par 
des juges automatisés hors du chemin critique et par une revue humaine. Anthropic décrit 
un juge qui rend, en un seul appel, un score de 0,0 à 1,0 et un verdict de réussite ou 
d’échec[17]. Le résultat se consigne dans l’événement gen_ai.evaluation.result (Development)  : 
gen_ai.evaluation.name (requis), gen_ai.evaluation.score.value, gen_ai.evaluation.score.label 
(p. ex. pass) et gen_ai.evaluation.explanation (texte libre, soumis à l’EXIG-OBS-07 : en production, il 
ne reproduit ni invite ni réponse), et devrait être rattaché au span évalué[396]. Les défaillances multiagents 
se classent selon la taxonomie MAST (Multi-Agent System Failure Taxonomy) (section 7.9), et les entrées du 
bus peuvent être rejouées en isolement pour éprouver une nouvelle version (EXIG-EVT-10).
Tableau 42 — Familles d’objectifs de niveau de service d’un agent (cibles proposées par le cadre)
Famille
Indicateurs
Cible proposée
Fiabilité technique
Succès des appels MCP et A2A; latence par étape au 95e 
centile
Plus de 99,5 % de succès; latence fixée au 
contrat
Efficacité
Tâches achevées sans erreur; étapes par tâche; appels 
d’outils invalides
Moins de 1 % d’appels invalides
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 152 sur 283
