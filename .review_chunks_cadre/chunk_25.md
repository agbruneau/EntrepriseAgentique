# chunk_25 — pages PDF 241 à 252 (sur 283)



---
## [Page PDF 241]

CRE-IA-2026-01 · Cadre de référence
E Glossaire
Terme (sigle)
Équivalent anglais
Définition
Système 
d’enregistrement
system of record
Système qui fait foi pour une donnée de l’entreprise : ERP, CRM, 
système de dossiers, entrepôt de données, logiciel-service. Un agent 
n’y écrit que par une interface qui applique les contrôles métier de 
ce système, jamais par un accès direct aux tables. Voir la section 5.2.
Système d’IA
AI system
Selon l’article 3(1) du RIA, système automatisé conçu pour fonc­
tionner à différents niveaux d’autonomie, qui peut faire preuve 
d’adaptabilité après son déploiement et qui déduit, à partir des 
entrées qu’il reçoit, la manière de générer des sorties (prédictions, 
contenus, recommandations ou décisions) pouvant influencer des 
environnements physiques ou virtuels[61]. Le cadre considère tout 
agent comme un système d’IA. Voir la section 12.4.
Tâche (A2A)
task
Unité de travail A2A créée par l’agent serveur, qui lui attribue 
son identifiant (taskId); contextId regroupe les tâches et les 
messages d’une même interaction. Une tâche suit une machine 
à huit états de cycle de vie (l’énumération compte neuf va­
leurs avec TASK_STATE_UNSPECIFIED), dont deux états interrompus 
(INPUT_REQUIRED, AUTH_REQUIRED) et quatre états terminaux, et produit 
des artefacts composés de parties (Part)[68]. Voir la section 6.6.
Traçage
distributed tracing
Reconstitution de bout en bout du chemin d’une demande au 
moyen de traces OpenTelemetry, faites de spans reliés par un même 
contexte W3C Trace Context (en-tête traceparent), défini pour HTTP; 
le cadre exige de le propager aussi dans le champ _meta de MCP, 
dans A2A et dans l’extension CloudEvents Distributed Tracing[103, 162, 
253]. Le traceparent n’est pas un identifiant métier, et la trace ne 
remplace pas le journal d’audit. Voir la section 10.1.
Transfert
handoff
Cession explicite du contrôle d’une session, avec son contexte utile, 
d’un agent source vers un agent cible mieux qualifié; l’agent source 
se retire. Le transfert vise une liste fermée de destinataires et porte le 
mandant, pas tout l’historique. Voir la section 7.2.
Triade létale
lethal trifecta
Combinaison, nommée par Simon Willison, de l’accès à des données 
privées, de l’exposition à du contenu non fiable et de la capacité de 
communiquer vers l’extérieur, qui rend l’exfiltration possible[354]. La 
« règle de deux » de Meta en tire une règle de session : au plus deux 
des trois propriétés sans supervision[307]. Voir la section 9.6.
F Validation des sources et des ébauches
Cette annexe rend compte de la vérification qui fonde la version 1.0 : comment les 121 références de la 
recherche documentaire ont été validées, ce que la vérification a révélé, et quelles affirmations des ébauches 
ont été corrigées ou retirées. Elle permet à tout lecteur de retracer l’origine d’un fait et le degré de confiance 
qu’on peut lui accorder.
F.1 Méthode
La vérification s’est déroulée en trois passes, les 27 et 28 octobre 2026.
1. Validation référence par référence. Chacune des 121 références de la recherche documentaire a fait 
l’objet d’une tentative d’ouverture; pour les 13 pages bloquées, payantes ou redirigées, on s’est limité 
au résumé public ou à une source primaire. On a consigné son accessibilité, son éditeur, sa date et sa 
catégorie de crédibilité, puis confronté chaque affirmation qui la citait au contenu réel de la page (427 
liens affirmation-source au total). Lorsqu’une page n’appuyait pas une affirmation, une source primaire 
a été recherchée pour la confirmer ou la réfuter.
2. Vérification thématique. Onze vérifications ont confronté les affirmations des quatre ébauches aux 
textes primaires  : MCP; A2A et protocoles connexes; plateformes et fondations; identité; sécurité; 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 241 sur 283


---
## [Page PDF 242]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
observabilité, contrats et événements; orchestration; autonomie; droit québécois et canadien; référen­
tiels internationaux; économie et données de marché. Elles ont aussi recueilli les faits complémentaires 
intégrés au cadre.
3. Audit final. Le 28 octobre 2026, chacune des 428 références alors citées dans le corps du cadre a été 
rouverte à sa source et confrontée, affirmation par affirmation, aux passages qui s’y appuient (1 409 
affirmations examinées). L’identité de chaque référence (auteurs, titre, date, éditeur), sa catégorie et 
son statut à cette date ont été contrôlés, et les écarts les plus graves ont été recontrôlés par un second 
examinateur indépendant, qui a réfuté plusieurs reclassements proposés. En parallèle, tous les chapitres 
et annexes ont été relus pour la cohérence interne, l’exactitude factuelle et juridique, la formulation des 
exigences et la langue. Les corrections retenues ont été intégrées au texte; 49 sources ont été ajoutées au 
registre, et le texte des exigences, les échelles et les renvois ont été harmonisés. Après l’intégration de 
ces corrections, l’annexe G compte 473 références, toutes citées dans le corps du cadre. Les arbitrages 
d’architecture et de gouvernance relevés lors de cet audit ont également été tranchés et intégrés à la 
présente version.
Tableau 66 — Catégories de crédibilité des sources
Catégorie
Définition
Usage dans le cadre
A
Source primaire ou officielle : organismes de normalisation et leurs dépôts 
(IETF, W3C, ISO, NIST, OWASP, CNCF, OpenTelemetry, Linux Foundation et 
sites des projets), textes législatifs et organismes de réglementation, docu­
mentation officielle d’un éditeur sur son propre produit, articles scientifiques 
d’auteurs identifiables, communiqués des firmes d’analystes.
Appui de toute exigence et de 
tout fait.
B
Source secondaire reconnue : grande presse spécialisée, cabinets juridiques, 
experts reconnus.
Appui d’un fait de contexte, 
jamais seul pour une exigence.
C
Blogue de positionnement, agrégateur, site inconnu ou contenu généré en 
série.
Jamais cité; remplacé par une 
source A ou B, ou fait retiré.
F.2 Bilan chiffré
Les décomptes ci-dessous portent sur les 121 références et sur les 427 liens affirmation-source de la recherche 
documentaire.
121
références validées une à une, dont 108 accessibles et 13 bloquées, payantes ou redirigées
61
références de catégorie C (50 %), dont 33 présentant les marques d’un contenu généré en série
88
références remplacées (71) ou retirées (17); 33 conservées comme sources A ou B
705
sources admissibles (A ou B) recensées pour la version finale, dont 632 de catégorie A (primaires ou 
officielles); 49 ont été ajoutées lors de l’audit final
Tableau 67 — Verdicts sur les 427 liens affirmation-source de la recherche documentaire
Verdict
Nombre
Part
Signification
Appuyée
125
29 %
La source citée confirme l’affirmation telle qu’écrite.
Partiellement ap­
puyée
214
50 %
Le fond est juste, mais un détail (date, chiffre, version, portée) diffère : l’énoncé a 
été corrigé.
Non appuyée
55
13 %
La source ne contient pas l’affirmation : source primaire trouvée ou fait retiré.
Contredite
14
3 %
La source ou une source primaire dit le contraire : fait corrigé.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 242 sur 283


---
## [Page PDF 243]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
Verdict
Nombre
Part
Signification
Invérifiable
19
4 %
Aucune source crédible trouvée : fait retiré ou présenté comme choix interne du 
cadre.
À RETENIR
Le fond technique des ébauches était solide, mais plus de sept affirmations sur dix (302 sur 427) 
exigeaient une correction de détail, une meilleure source ou un retrait. Les erreurs récurrentes : versions 
de protocoles dépassées, chiffres de marché attribués à la mauvaise firme, obligations légales mal ratta­
chées à un article, allégations commerciales présentées comme des normes et seuils chiffrés sans source.
F.3 Principales corrections apportées aux ébauches
Le tableau suivant recense les corrections les plus importantes. Les sources indiquées appuient la version 
retenue.
Tableau 68 — Principales corrections factuelles
#
Affirmation des ébauches
Version retenue dans le cadre
1
MCP 2026-07-28 « impose » OAuth 2.1, 
norme publiée.
L’autorisation est facultative dans MCP; le cadre la rend obligatoire. OAuth 2.1 
reste un Internet-Draft de l’IETF; on exige OAuth 2.0 selon la RFC 9700, aligné 
sur le profil OAuth 2.1[176, 209].
2
Champs x-enterprise-* dans les annota­
tions d’un outil MCP.
Hors du schéma (cinq propriétés seulement, dont quatre indices non fiables). 
Le palier, le seuil d’approbation et la compensation sont inscrits au catalogue 
d’entreprise (choix du cadre, non prescrit par le schéma MCP) [201].
3
La passerelle doit supprimer tout champ 
_meta.
La version du protocole et les capacités du client y sont obligatoires, et 
traceparent, tracestate et baggage y sont réservés au contexte de trace; on 
conserve ces clés, on filtre les clés non reconnues et on ne fonde aucune auto­
risation sur _meta [162].
4
Quatre vecteurs d’attaque selon Akamai; 
rejet 400/403 en cas d’écart d’en-têtes.
L’analyse d’Akamai décrit cinq zones de risque; la concordance en-têtes/corps 
est déjà exigée par la spécification (HTTP 400, erreur −32020) [190, 203].
5
MCP exige des jetons liés (mTLS ou 
DPoP) de 5 à 15 minutes.
MCP utilise des jetons porteurs[209]; la liaison à l’émetteur et la durée courte 
sont une politique du cadre fondée sur les RFC 8705[328] et 9449[213].
6
Carte d’agent à /.well-known/agent.json, 
champs url et authentication, méthode 
tasks/sendSubscribe.
Formes antérieures à la version 1.0. A2A 1.0 : agent-card.json, 
supportedInterfaces, securitySchemes, SendStreamingMessage, états 
TASK_STATE_* [68].
7
Spécification A2A « gelée » le 12 mars 
2026.
Version 1.0.0 publiée le 12 mars 2026, correctif 1.0.1 le 28 mai 2026 (release 
GitHub du projet); A2A annoncé comme projet de l’AAIF le 17 août 2026 (billet 
du projet du 27 août 2026)[5, 29, 472].
8
AGNTCY fait partie de la pile de l’AAIF; 
SLIM est résistant au quantique.
AGNTCY est un projet de la Linux Foundation dont la candidature à l’AAIF est 
ouverte; la proposition qualifie SLIM de « quantum-safe » sans nommer de 
suite MLS post-quantique (SLIM met en œuvre MLS, RFC 9420), de sorte que 
son caractère post-quantique n’est pas démontré[37, 269].
9
Copilot Studio : MCP en disponibilité gé­
nérale visée en octobre 2026.
MCP est en disponibilité générale dans Copilot Studio depuis le 29 mai 
2025[300].
10
Une passerelle ajoute moins de 5 ms; 
le coupe-circuit confine « en millise­
condes ».
Allégations commerciales divergentes (TrueFoundry : « typiquement » moins 
de 5 ms dans sa FAQ, +7 à +12 ms à son propre banc d’essai); aucun seuil 
chiffré n’est retenu sans mesure interne (P50/P99, politiques actives)[143, 144].
11
Délégation limitée à un niveau et sept 
sous-agents : règles générales.
Contraintes du produit Agentforce; la profondeur maximale de deux niveaux 
est un choix du cadre[49].
12
Attribut gen_ai.agent_version; opération 
handoff; contenu jamais dans les attributs 
de span.
Nom exact gen_ai.agent.version (ajouté en v1.40.0); aucune valeur handoff 
dans gen_ai.operation.name (v1.41.0); contenu en attributs facultatifs (opt-in) 
depuis la version 1.37.0; conventions au niveau « Development », à épingler[119, 
180].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 243 sur 283


---
## [Page PDF 244]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
#
Affirmation des ébauches
Version retenue dans le cadre
13
Indicateurs d’agent « au format FOCUS ».
FOCUS normalise les données de facturation (version 1.4); aucune de ses co­
lonnes ne porte d’indicateur par agent, que l’organisation calcule par jointure 
avec sa propre télémétrie[410, 463].
14
Le traitement exactement une fois de 
Kafka empêche les doubles paiements.
La garantie vaut entre sujets Kafka; pour tout effet externe, le système cible 
doit coopérer, par exemple au moyen d’une clé d’idempotence qu’il vérifie[140].
15
Un bus d’événements réduit la latence de 
coordination de 70 à 90 %.
Chiffre sans source primaire : retiré; seul l’avantage qualitatif de l’abonnement 
sur l’interrogation est retenu[262].
16
Multiagent : +81 % et −70 % (Google), 3 
à 10 fois plus de jetons.
+80,9 % (Finance-Agent), −39 % à −70 % (PlanCraft), amplification des erreurs 
de 17,2× sans vérification centrale; 3 à 10× par rapport à l’agent unique et 
environ 15× par rapport à une conversation sont deux mesures distinctes[17, 
273, 275].
17
Firecracker : environ 100 000 lignes, six 
périphériques virtio.
Environ 50 000 lignes de Rust (2020), quatre types de périphériques émulés 
(réseau et bloc virtio, port série, contrôleur de clavier i8042 partiel), moins de 5 
Mio par microVM, démarrage sous 125 ms[363].
18
gVisor impose un surcoût d’E/S de 10 à 
30 %.
Aucune fourchette publiée; le coût dépend des appels système : mesurer sur la 
charge réelle[361].
19
Taux de réussite de 84 % du détourne­
ment d’objectif.
Chiffre d’un banc d’essai précis (Agent Security Bench, 84,30 %), cité seulement 
dans ce contexte[359].
20
Les identités non humaines dépassent les 
humaines de 20 contre 1.
Enquête de fournisseur la mieux documentée : 82 identités machines par 
humain (CyberArk, 2025); chaque organisation mesure son propre ratio[11].
21
Loi 25 : avis à la CAI en 72 heures (art. 3.2 
ou 3.5).
Avis « avec diligence » en cas de risque de préjudice sérieux (art. 3.5 de la Loi 
sur le privé); registre (art. 3.8) conservé cinq ans selon le règlement; 72 heures 
n’est qu’une cible interne[56, 460].
22
Décisions automatisées au secteur pu­
blic : article 63.1.
Article 65.2 de la Loi sur l’accès[318]; l’article 63.1 porte sur les mesures de 
sécurité[56].
23
Amendes pénales de 1 000 à 10 000 $ 
pour une personne; amendes de plus de 
500 000 $ déjà prononcées; sanction de 
5 000 $ en vertu de la Loi 25.
De 5 000 à 100 000 $ pour une personne physique (art. 91 de la Loi sur le 
privé); aucune amende de plus de 500 000 $ n’est confirmée; les 5 000 $ visent 
une décision de la Cour supérieure (art. 342 C.p.c.) sur des citations inventées 
par l’IA[458].
24
Article 17 : « analyse d’impact relative au 
transfert »; protection « équivalente ».
EFVP et entente écrite; critère de protection « adéquate »; « hors Québec » 
s’entend de tout lieu extérieur au Québec, y compris, selon l’interprétation du 
cadre, les autres provinces[416].
25
Règlement européen : haut risque appli­
cable le 2 août 2026; s’applique dès 
qu’un agent « touche » des utilisateurs 
de l’UE.
Échéances reportées par le règlement (UE) 2026/1744 (annexe III : 2 décembre 
2027; annexe I : 2 août 2028); critère de l’article 2 : utilisation des sorties dans 
l’Union[58, 61].
26
NIST MANAGE 3.1 et 3.2 couvrent 
le coupe-circuit; MEASURE 2.7 la sur­
veillance des hallucinations.
Coupe-circuit : MANAGE 2.4; déclassement : GOVERN 1.7; MEASURE 2.7 porte 
sur la sécurité et la résilience; la surveillance en production relève de MEASURE 
2.4[74].
27
« Seulement 13 % ont la gouvernance 
adéquate » attribué à McKinsey; 150 000 
agents par entreprise attribués à un 
blogue.
Les deux chiffres proviennent de Gartner (communiqué du 28 avril 2026)[2].
28
Les dépenses d’IA des entreprises ont 
bondi de 320 %.
Chiffre sans source, qui semble provenir d’une lecture erronée du facteur 3,2 
(environ +220 %) : 37 G$ US en 2025 contre 11,5 G$ US en 2024 (Menlo 
Ventures, 9 décembre 2025)[16].
29
Petits modèles 10 à 30 fois moins coû­
teux (arXiv 2506.02142); Phi-3.5 « 98 % 
de calcul en moins ».
Référence exacte : arXiv 2506.02153 (coût de calcul, non prix facturé); le 
« 98 % » est introuvable et retiré[403, 473].
30
Trois échelles d’autonomie incompatibles 
(L0–L5, N0–N4, L0–L4) et seuils chiffrés 
(60 s, 5 min, 1 h).
Échelle unique N0 à N4 et niveau NX interdit, fondée sur Feng et al., Gartner, 
AWS et l’IMDA (Infocomm Media Development Authority, Singapour); les 
seuils deviennent des paramètres internes approuvés par le comité[76, 83].
31
Saga : un plantage entre la journalisation 
et l’action ne déclenche aucune compen­
sation.
Une étape à l’état incertain est traitée comme possiblement exécutée; sa com­
pensation, idempotente, doit pouvoir s’exécuter sans risque[286].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 244 sur 283


---
## [Page PDF 245]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
#
Affirmation des ébauches
Version retenue dans le cadre
32
Mémoire à quatre niveaux « inspirée de 
Tulving ».
Taxonomie à quatre types (travail, épisodique, sémantique, procédurale) issue 
de CoALA, qui la reprend de l’architecture Soar[100].
F.4 Registre des 121 références de la recherche documentaire
Légende des verdicts : ✓ appuyée · ◐ partiellement appuyée · ✗ non appuyée ou contredite · ? invérifiable · — 
aucune affirmation associée à la référence. La colonne n reprend le numéro de la référence dans la recherche 
documentaire. Décision : conservée = source A ou B citée là où elle appuie un fait; remplacée = remplacée 
par une source primaire; retirée = sans valeur probante pour le cadre.
Tableau 69 — Registre de validation des références de la recherche documentaire
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
1
Enterprise Agentic AI Architecture Design Guidance 
(Part 1) Architecture & Governance Magazine
B
accessible
✓5 ◐10 ✗3
conservée
2
Enterprise Agentic AI Reference Architecture (2026) 
Triotech Systems
C
accessible
✓2 ◐2
retirée
3
A Framework for Architecting Agent Control Plane 
MuleSoft
B
accessible
✓3 ◐3 ✗3
conservée
4
Microsoft Copilot Studio vs. Salesforce Agentforce: 
Which AI Agent Platform is Better for Enterprises? 
Artic Consulting
C
accessible
◐4
remplacée
5
Agentic AI Architecture Framework for Enterprises: 
The Complete 2026 Design and Governance Guide 
NextAgile
C
accessible
◐4 ✗1 ?9
remplacée
6
AI FinOps Explained: AI Cost Optimization Guide for 
2026 AvePoint
C
accessible
✓1 ◐5 ✗2
remplacée
7
Governing AI Agents Across Multiple Platforms 
TrueFoundry
B
accessible
✓2 ◐8 ✗3
remplacée
8
Designing agentgateway: A Unified 
High-Performance Gateway for AI and API Traffic 
agentgateway.dev
A
accessible
✓1 ◐2
conservée
9
Agent Communication Protocol (ACP) Explained: 
What It Is and Why It Matters Boldare
C
accessible
✓1 ◐6
remplacée
10
What the Linux Foundation and AAIF Mean for MCP 
and Agentic AI Blck Alpaca
C
accessible
✓1 ◐3 ✗2
remplacée
11
The next generation of MCP Cloudflare
B
accessible
✓12 ◐6 ✗2
remplacée
12
Specification - Model Context Protocol (MCP) 
ModelContextProtocol.Info
C
accessible
✓1
remplacée
13
Architecture overview (documentation MCP, révision 
2026-07-28) Model Context Protocol
A
accessible
✓5 ◐1
conservée
14
#17: What is A2A and why is it – still! – underappre­
ciated? Turing Post
B
accessible
✓2 ◐1
remplacée
15
All About the A2A Protocol, Now Part of the Agentic 
AI Foundation rohitghumare.com
C
accessible
✓10 ◐6 ✗3 ?1
remplacée
16
[Project Proposal] AGNTCY #57 (dépôt aaif/project-
proposals) GitHub
A
accessible
✓5 ◐6
remplacée
17
AGNTCY: the open standard set to structure the In­
ternet of Agents Splunk
B
accessible
✓2 ◐2
remplacée
18
Autonomous Agentic Event-Driven Systems Archi­
tecture Confluent
A
accessible
✓4 ◐6
conservée
19
Event-Driven Architecture for AI Agents (Patterns 
and Benefits) Atlan
C
accessible
◐3
remplacée
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 245 sur 283


---
## [Page PDF 246]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
20
The 6 Levels of AI Autonomy (2026): A Practical Fra­
mework Agentys
C
accessible
◐8 ✗10
remplacée
21
AI Agent Risk Assessment: What Organizations 
Need to Evaluate Global AI Certification Council
C
accessible
✓2 ◐5 ✗4
remplacée
22
When to use multi-agent systems (and when not to) 
Anthropic
A
accessible
✓6 ◐8 ✗1
conservée
23
Single-Agent vs Multi-Agent AI: When to Scale Your 
Dev Workflow Augment Code
C
accessible
✓1
remplacée
24
The Saga Pattern for Multi-Agent Transactions: 
Compensating Actions RedLineSoft
C
accessible
✓11 ◐2 ✗1
remplacée
25
AI Agent Orchestration Frameworks: A 2026 Guide 
Levelop
C
accessible
✓2 ◐8 ✗2
remplacée
26
OWASP Top 10 for Agentic Applications (2026) — 
fiche de cadre Modulos (MFF-14) Modulos AG
B
accessible
✓7 ◐5 ✗2
remplacée
27
Authentication for AI Agents: OAuth Patterns for 
Non-Human Identity guptadeepak.com
B
accessible
✓2 ◐6 ✗2
remplacée
28
ISO 42001 vs NIST AI RMF: Which Do You Need in 
2026? Fruggr
C
accessible
◐3
remplacée
29
How to sandbox AI agents in 2026: MicroVMs, gVi­
sor & isolation strategies Northflank
B
accessible
✓1 ◐5 ✗1
remplacée
30
Conformité à l’IA et à la Loi 25 du Québec : le guide 
complet 2026 Augure
C
accessible
◐11 ✗9 ?1
remplacée
31
Enterprise Architecture 2030: Navigating Agentic AI 
Scenarios Gartner
A
payante
✓1
conservée
32
The best AI agent frameworks in 2026 LangChain
B
accessible
◐4 ✗2
remplacée
33
Best Agentic AI Platforms for Enterprise Operations 
(2026 Guide) Shadow Inc.
C
accessible
✓1 ◐1 ✗2
remplacée
34
Multi-Agent AI News - Week of May 19-25, 2026 - 
Enterprise Orchestration Platforms Suprmind
C
accessible
◐2 ✗1 ?1
remplacée
35
Agentic Integration with SAP, ServiceNow, and Sa­
lesforce Microsoft Community Hub
B
accessible
—
retirée
36
Implement 3 Layers of Oversight for Scaled Agentic 
AI Architectures (titre non vérifié) Gartner
A
bloquée
?1
retirée
37
AI Agent Sandbox: How to Safely Run Autonomous 
Agents in 2026 Firecrawl
B
accessible
✓3 ◐1
conservée
38
MCP (Model Context Protocol) in 2026: the com­
plete guide for engineering teams Jacar Systems
C
accessible
✓2 ◐3 ✗1
remplacée
39
Multi-Agent Orchestration Patterns: A Production 
Guide (2026) explainx.ai
C
accessible
✓2 ◐5 ✗1
remplacée
40
Agentforce Interoperability Guide (The Architect’s 
Guide to Agentforce Interoperability) Salesforce
A
accessible
◐2
conservée
41
Levels of Autonomy for AI Agents arXiv
A
bloquée
✓1
remplacée
42
The Five Working Levels of AI Agent Autonomy, and 
How to Choose Among Them The Inteq Group
C
accessible
✓1 ◐1
remplacée
43
Building Blocks (TOGAF 9.1, Partie IV, chapitre 37) 
QualiWare Center of Excellence
B
accessible
◐1
remplacée
44
Architecture Building Blocks (ABBs) vs Solution Buil­
ding Blocks (SBBs) Boldo
C
accessible
—
remplacée
45
SAP Enterprise Architects’ Guide: Using TOGAF® 
ABBs and SBBs to Deliver Successful SAP S/4HANA 
Implementations Insight Arc
C
accessible
—
retirée
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 246 sur 283


---
## [Page PDF 247]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
46
Ambient Agents and the New Agent Inbox ft. Harri­
son Chase Inference by Sequoia
B
accessible
◐7
remplacée
47
Introducing ambient agents LangChain
A
accessible
✓2 ◐2
conservée
48
Confluent: The Real-Time Backbone for Agentic Sys­
tems Confluent
A
accessible
◐2
conservée
49
Best Code Execution Sandboxes for AI Agents in 
2026 E2B
A
accessible
✓1
conservée
50
MCP Is Growing Up: The 2026 Roadmap Takes 
Shape Obot AI
B
accessible
✓1 ◐1
remplacée
51
5 Best Code Execution Sandboxes for AI Agents 
Blaxel
C
accessible
—
retirée
52
TRiSM for Agentic AI: A Review of Trust, Risk, 
and Security Management in LLM-based Agentic 
Multi-Agent Systems arXiv
A
accessible
◐1
remplacée
53
AI Agent Protocols: MCP, A2A, ACP, and the Interop 
Stack AIPrompt20
C
accessible
✓1
remplacée
54
The AI Agent Memory Architecture Deep Dive: 
Building Agents That Remember Across Sessions, 
Devices, and Tools AI Magicx
C
accessible
✓1 ◐4 ✗1
remplacée
55
GraphRAG, AI Agents, and Memory: How Graph 
Databases Power the Next Wave of AI in 2026 Fal­
korDB
B
accessible
◐3
remplacée
56
Agent Memory Architectures: Vector vs Graph vs 
Episodic Digital Applied
C
accessible
—
retirée
57
New in Confluent Intelligence: A2A, Multivariate 
Anomaly Detection, Vector Search for Cosmos DB, 
Amazon S3 Vectors, and More Confluent
A
accessible
◐1
conservée
58
Cheap Tokens, Expensive Agents: The 2026 Infe­
rence Economics Reckoning Socradata
C
accessible
◐2 ✗1 ?1
remplacée
59
OpenTelemetry GenAI Semantic Conventions: A 
Practical Guide OpenObserve
C
accessible
◐4 ✗3
remplacée
60
Agent Memory Systems: How AI Agents Remember, 
Learn, and Stay Coherent Across Time Tresslers 
Group
C
accessible
◐1
remplacée
61
Avoid Governance Mismatch: Classify AI Agents by 
Autonomy Level Gartner
A
bloquée
✓1 ◐1
conservée
62
From autonomous cars to autonomous agents: the 
five levels of AI agent autonomy (titre non confirmé) 
MIT Media Lab
B
bloquée
?3
remplacée
63
The 5 Levels of Agentic AI (And Why Most Busi­
nesses Need Less Autonomy Than They Think) (titre 
non confirmé) Medium
C
bloquée
—
retirée
64
The 5 Levels of AI Agent Autonomy: From Copilot to 
Fully Autonomous (And Where to Start) Pickaxe
C
accessible
◐1
remplacée
65
The Six Levels of Agentic Behavior Vellum
C
accessible
—
retirée
66
The Top Agentic AI Security Threats You Need to 
Know in 2026 Lasso Security
B
accessible
◐1
remplacée
67
Ambient agents explained: Applications, architec­
ture, and building with ZBrain ZBrain
C
accessible
—
retirée
68
LIVE: Ambient Agents and the New Agent Inbox ft. 
Harrison Chase Sequoia Capital
B
accessible
✓2
conservée
69
UX for Agents, Part 2: Ambient LangChain
B
accessible
—
conservée
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 247 sur 283


---
## [Page PDF 248]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
70
Why Google’s Agent2Agent Protocol Needs Apache 
Kafka Medium
B
bloquée
—
remplacée
71
MCP (Model Context Protocol) for Business: The 
USB-C of AI Agents and Why It Changes Your Stack 
in 2026 NAXIA
C
accessible
—
retirée
72
The New MCP Specification: What Security Teams 
Must Prepare For Akamai Security Research
B
accessible
✓4 ◐3
conservée
73
Agent Card Explained: A2A Protocol, JSON & Use 
Cases AI Growth Agent
C
accessible
✓2 ◐2 ✗1
remplacée
74
Agent communication protocols: A2A vs ACP vs 
MCP (2026) crystl
C
accessible
—
retirée
75
What’s New in A2A Protocol v1.0 A2A Project
A
accessible
—
conservée
76
A2A v1.0: a builder’s guide, part 2 - migration, secu­
rity, and production Agentic AI Foundation
A
accessible
—
conservée
77
A2A Agent Card: Structure, Discovery, and Signing 
Agent2Agent.Info
C
redirigée
✓1
remplacée
78
A2A v1.0 Agent Card Specification Explorer A2A Re­
gistry
C
accessible
—
remplacée
79
AGNTCY Documentation AGNTCY
A
accessible
—
conservée
80
Beyond Context Sharing: A Unified Agent Commu­
nication Protocol (ACP) for Secure, Federated, and 
Autonomous Agent-to-Agent (A2A) Orchestration 
arXiv
A
accessible
—
retirée
81
Four Design Patterns for Event-Driven, Multi-Agent 
Systems Confluent
A
accessible
✓1 ◐1
conservée
82
MCP vs. REST/HTTP API vs. Kafka: The Architect’s 
Guide to Agentic AI Integration kai-waehner.de
B
accessible
✓2 ◐5 ✗1
conservée
83
Building effective agents Anthropic
A
accessible
◐1
conservée
84
Single Agent vs Multi-Agent: When to Build a 
Multi-Agent System (titre non confirmé : page inac­
cessible) Towards Data Science
B
bloquée
—
remplacée
85
How to Decide When to Use a Single Agent vs a 
Multi-Agent Team MindStudio
C
accessible
✓1
remplacée
86
Multi-Agent AI Orchestration: A CTO’s 2026 Guide 
KGT Solutions
C
accessible
✓1 ?1
remplacée
87
Top Agent Frameworks To Use in 2026: A Compari­
son Splunk
C
accessible
✓2 ◐2
remplacée
88
How and when to build multi-agent systems Lang­
Chain
B
accessible
—
conservée
89
Top 9 AI Agent Frameworks in 2026 (titre de la 
bibliographie; page non lue) Medium
C
bloquée
—
retirée
90
Conformité Loi 25 – Microsoft, hébergé au Canada 
(io4 Technologies) io4 Technologies
C
accessible
✓1 ◐1
remplacée
91
Salesforce Agentforce vs Microsoft Copilot Studio: 
2026 Comparison Smartbridge LLC
C
accessible
—
retirée
92
AI Agent Memory Architectures: From Context Win­
dows to Persistent Knowledge Zylos Research
C
accessible
—
retirée
93
Memory Systems for AI Agents: Practical Implemen­
tations (2025-2026) GitHub Gist
C
accessible
—
retirée
94
SYNAPSE: Empowering LLM Agents with 
Episodic-Semantic Memory via Spreading Activation 
arXiv
A
accessible
—
conservée
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 248 sur 283


---
## [Page PDF 249]

CRE-IA-2026-01 · Cadre de référence
F Validation des sources et des ébauches
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
95
Architecture – Solo Enterprise for agentgateway 
docs Solo.io
A
accessible
—
remplacée
96
OAuth 2.0 Token Exchange: When One Token Isn’t 
the Token You Need (titre non confirmé) Medium
C
bloquée
?1
remplacée
97
OAuth’s On-Behalf-Of flow for AI agents WorkOS
B
accessible
◐2
remplacée
98
OAuth 2.0 Extension: On-Behalf-Of User Authoriza­
tion for AI Agents (brouillon −01) IETF
A
accessible
◐1
remplacée
99
On-Behalf-Of Token Exchange Auth0
A
accessible
—
conservée
100
OAuth 2.0 Extension: On-Behalf-Of User Authoriza­
tion for AI Agents (brouillon −00) IETF
A
accessible
◐1
remplacée
101
AI Agent Code Execution Sandboxes: Isolation from 
Containers to MicroVMs (titre non confirmé) Me­
dium
C
bloquée
—
remplacée
102
OWASP Top 10 for Agentic Applications 2026: Key 
Takeaways & How to Take Action Teleport
B
accessible
—
remplacée
103
OWASP Non-Human Identities Top 10 OWASP 
Foundation
A
accessible
—
conservée
104
OWASP Agentic Skills Top 10 OWASP Foundation
A
accessible
—
conservée
105
OWASP GenAI Security Project Releases Top 10 
Risks and Mitigations for Agentic AI Security 
OWASP GenAI Security Project
A
accessible
—
conservée
106
AI TRiSM: Understanding Gartner’s View on Agentic 
AI Trust Sweet Security
C
accessible
◐1 ✗1
remplacée
107
OpenTelemetry GenAI Semantic Conventions: 
What’s Stable Praesidia
C
accessible
—
remplacée
108
Semantic Conventions for GenAI agent and frame­
work spans OpenTelemetry
A
accessible
—
conservée
109
Loi 25 et IA au Québec : guide PME 2026 (« Loi 25 et 
IA. Les gestes qui comptent. ») Margence inc.
C
accessible
◐1
remplacée
110
Conseil et formation IA — conformité Loi 25 et IA 
responsable au Québec | DictIA DictIA Inc.
C
accessible
✓1 ✗2
remplacée
111
Principaux changements aux lois sur la protection 
des renseignements personnels Commission d’accès 
à l’information du Québec
A
accessible
—
conservée
112
Décisions automatisées et Loi 25 : préparer 
l’information et la révision humaine extensio.ai
C
accessible
◐1
remplacée
113
Mesures applicables lors de l’utilisation de 
l’intelligence artificielle générative (indication 
d’application IA-RI-2025-003-OP) Gouvernement du 
Québec
A
accessible
—
conservée
114
AI Governance in 2026: A Practical Framework for 
NIST AI RMF, EU AI Act, and ISO 42001 Enterprise 
Architecture Blog
C
accessible
—
remplacée
115
NIST AI RMF Continuous Monitoring 2026 Bitsight
C
bloquée
—
remplacée
116
NIST AI RMF: 8-Step Implementation Guide Neural­
Trust
C
accessible
—
remplacée
117
A Guide to AI TRiSM: Trust, Risk, and Security Mana­
gement Palo Alto Networks
B
accessible
—
conservée
118
NIST AI RMF Implementation: A Clear 8-Step Plan 
for 2026 Governance Docs LLC
C
accessible
—
remplacée
119
AI FinOps Became a Real Discipline in 2026. Here’s 
What It Requires. Larridin
C
accessible
—
retirée
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 249 sur 283


---
## [Page PDF 250]

CRE-IA-2026-01 · Cadre de référence
G Références
n
Source (titre réel, éditeur)
Cat.
Accès
Affirmations
Décision
120
AI FinOps 2026: The Definitive Guide to Costs and 
Value Compresr
C
accessible
◐2 ✗1
remplacée
121
FinOps for AI: How to Control LLM Token Spend 
Before It Controls Your Budget Varcio
C
accessible
—
remplacée
G Références
Liste des sources citées, numérotées dans l’ordre de leur première citation. Toutes sont de catégorie A 
(primaires ou officielles) ou B (secondaires reconnues) et ont été consultées ou vérifiées au 27 octobre 
2026. Les versions des spécifications évoluant rapidement, le catalogue d’entreprise fait foi pour les 
versions applicables.
• [1] Gartner (2025, 26 août). Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI 
Agents by 2026, Up from Less Than 5% in 2025 [communiqué]. Gartner. https://www.gartner.com/en/
newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-
ai-agents-by-2026-up-from-less-than-5-percent-in-2025
• [2] Gartner (2026, 28 avril). Gartner Identifies Six Steps to Manage AI Agent Sprawl [commu­
niqué]. Gartner. https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-
to-manage-artificial-intelligence-agent-sprawl
• [3] Gartner (2025, 25 juin). Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled 
by End of 2027 [communiqué]. Gartner. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-
gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
• [4] Linux Foundation (9 décembre 2025). Linux Foundation Announces the Formation of the Agentic 
AI Foundation (AAIF), Anchored by New Project Contributions Including Model Context Protocol 
(MCP), goose and AGENTS.md. Linux Foundation. https://www.linuxfoundation.org/press/linux-foundation-
announces-the-formation-of-the-agentic-ai-foundation
• [5] A2A Project (27 août 2026). A New Chapter for A2A: Joining the Agentic AI Foundation. https://
a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation
• [6] Anthropic (Erik S. et Zhang, B.) (19 décembre 2024). Building effective agents. Anthropic. Note 
de l’éditeur : l’outillage décrit a changé depuis décembre 2024; les principes cités demeurent. https://
www.anthropic.com/engineering/building-effective-agents
• [7] Commission d’accès à l’information du Québec (s. d.). Principaux changements aux lois sur 
la protection des renseignements personnels. CAI. https://www.cai.gouv.qc.ca/protection-renseignements-
personnels/sujets-et-domaines-dinteret/principaux-changements-loi-25
• [8] Bureau du surintendant des institutions financières (2025). Ligne directrice E-23 – Gestion du 
risque de modélisation (2027). BSIF. https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-
23-model-risk-management-2027
• [9] Microsoft (2026). AI agent orchestration patterns. Azure Architecture Center. https://
learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
• [10] FinOps Foundation (2026). State of FinOps 2026. Linux Foundation. https://data.finops.org/
• [11] CyberArk (23 avril 2025). Machine Identities Outnumber Humans by More Than 80 to 1: New Re­
port Exposes the Exponential Threats of Fragmented Identity Security [communiqué]. Business Wire 
(reproduit par Silicon UK). https://www.silicon.co.uk/press-release/machine-identities-outnumber-humans-by-
more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 250 sur 283


---
## [Page PDF 251]

CRE-IA-2026-01 · Cadre de référence
G Références
• [12] McKinsey & Company (2025, 5 novembre). The state of AI in 2025: Agents, innovation, and 
transformation. QuantumBlack, AI by McKinsey. https://www.mckinsey.com/capabilities/quantumblack/our-
insights/the-state-of-ai
• [13] Shaw, F. X. (2025, 19 mai). Microsoft Build 2025: The age of AI agents and building the 
open agentic web. Microsoft. https://blogs.microsoft.com/blog/2025/05/19/microsoft-build-2025-the-age-of-
ai-agents-and-building-the-open-agentic-web
• [14] Soria Parra, D. (2025). MCP joins the Agentic AI Foundation. Model Context Protocol Blog. 
https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation
• [15] Linux Foundation (2026). A2A Protocol Surpasses 150 Organizations, Lands in Ma­
jor Cloud Platforms, and Sees Enterprise Production Use in First Year. Communiqué, 
9 avril 2026. https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-
cloud-platforms-and-sees-enterprise-production-use-in-first-year
• [16] Menlo Ventures (2025, 9 décembre). 2025: The State of Generative AI in the Enterprise. Menlo 
Ventures. https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise
• [17] Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. et Ford, D. (2025, 13 juin). How we built our 
multi-agent research system. Anthropic. https://www.anthropic.com/engineering/multi-agent-research-system
• [18] IBM (2025, 30 juillet). IBM Report: 13% Of Organizations Reported Breaches Of AI Models Or 
Applications, 97% Of Which Reported Lacking Proper AI Access Controls [communiqué; Cost of a 
Data Breach Report 2025, Ponemon Institute]. IBM. https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-
organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-
controls
• [19] IBM et Ponemon Institute (2026). Cost of a Data Breach Report 2026. IBM. 
https://www.ibm.com/reports/data-breach
• [20] Anthropic (25 novembre 2024). Introducing the Model Context Protocol. Anthropic. https://
www.anthropic.com/news/model-context-protocol
• [21] Google (9 avril 2025). Announcing the Agent2Agent Protocol (A2A). Google for Developers Blog. 
https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability
• [22] Linux Foundation (23 juin 2025). Linux Foundation Launches the Agent2Agent Pro­
tocol Project to Enable Secure, Intelligent Communication Between AI Agents. Linux Foun­
dation. https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-
enable-secure-intelligent-communication-between-ai-agents
• [23] Linux Foundation (29 juillet 2025). Linux Foundation Welcomes the AGNTCY Project 
to Standardize Open Multi-Agent System Infrastructure and Break Down AI Agent Silos. 
https://www.linuxfoundation.org/press/linux-foundation-welcomes-the-agntcy-project-to-standardize-open-multi-
agent-system-infrastructure-and-break-down-ai-agent-silos
• [24] LF AI & Data Foundation (29 août 2025). ACP Joins Forces with A2A. https://lfaidata.foundation/
communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data
• [25] Soria Parra, D., Jones, A., Antanavicius, T., Padilla, T. et Chu, T. (2025). Introducing the MCP 
Registry. Model Context Protocol Blog. https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-
preview
• [26] Google Cloud (16 septembre 2025). Powering AI commerce with the new Agent Payments Proto­
col (AP2). Google Cloud Blog. https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-
to-payments-ap2-protocol
• [27] Stripe (29 septembre 2025). Stripe powers Instant Checkout in ChatGPT and releases Agentic 
Commerce Protocol co-developed with OpenAI. Stripe. https://stripe.com/newsroom/news/stripe-openai-
instant-checkout
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 251 sur 283


---
## [Page PDF 252]

CRE-IA-2026-01 · Cadre de référence
G Références
• [28] OWASP GenAI Security Project (2025). OWASP Top 10 for Agentic Applications for 2026. 
OWASP Foundation. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
• [29] A2A Project (12 mars 2026). A2A Protocol Ships v1.0: Production-Ready Standard for 
Agent-to-Agent Communication. https://a2a-protocol.org/latest/blog/2026/03/12/a2a-protocol-ships-v10-
production-ready-standard-for-agent-to-agent-communication
• [30] A2A Project (2025-2026). Releases (v0.3.0, v1.0.0, v1.0.1). GitHub a2aproject/A2A. https://
github.com/a2aproject/A2A/releases
• [31] Agentic AI Foundation (2026). agentgateway Joins AAIF as an Open Gateway for Agentic 
AI Infrastructure. AAIF, 4 juin 2026. https://aaif.io/blog/agentgateway-joins-aaif-as-an-open-gateway-for-
agentic-ai-infrastructure
• [32] Linux Foundation (2025). Linux Foundation Welcomes agentgateway Project to Accelerate 
AI Agent Adoption While Maintaining Security, Observability and Governance. Communiqué, 25 
août 2025. https://linuxfoundation.org/press/linux-foundation-welcomes-agentgateway-project-to-accelerate-
ai-agent-adoption-while-maintaining-security-observability-and-governance
• [33] Soria Parra, D. et Delimarsky, D. (2026). The 2026-07-28 Specification. Model Context Protocol 
Blog. https://blog.modelcontextprotocol.io/posts/2026-07-28
• [34] Model Context Protocol (2026). Versioning. https://modelcontextprotocol.io/specification/versioning
• [35] Agentic AI Foundation (2026). A2A joins AAIF’s open agentic stack. AAIF, 17 août 2026. 
https://aaif.io/blog/a2a-joins-aaif
• [36] Agentic AI Foundation (9 septembre 2026). Envoy AI Gateway becomes Agent Router and joins 
AAIF. Agentic AI Foundation (AAIF). https://aaif.io/blog/agent-router-joins-aaif
• [37] Cisco (Parello, J.) (12 octobre 2026). [Project Proposal] AGNTCY, issue no 57. GitHub, aaif/
project-proposals (Agentic AI Foundation). https://github.com/aaif/project-proposals/issues/57
• [38] Linux Foundation (2026). Agentic AI Foundation Announces Four New Projects: Agent 
Skills, Open Responses, OpenEnv, and OpenSandbox. Communiqué, 22 octobre 2026. https://
www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-
openenv-and-opensandbox
• [39] A2A Project (s. d.). A2A and MCP. https://a2a-protocol.org/latest/topics/a2a-and-mcp
• [40] Agentic AI Foundation (s. d.). Home (section « Working groups that matter »). Agentic AI Foun­
dation (AAIF). https://aaif.io/
• [41] Parikh, S. (28 avril 2026). We’re donating Agent Payments Protocol to the FIDO Alliance to sup­
port the future of secure, agentic payments. Google. https://blog.google/products-and-platforms/platforms/
google-pay/agent-payments-protocol-fido-alliance
• [42] Agentic AI Foundation (2026). Project Proposals (processus d’admission). GitHub. https://
github.com/aaif/project-proposals
• [43] Model Context Protocol (2026). The MCP Registry. https://modelcontextprotocol.io/registry/about
• [44] TrueFoundry (2026). Governing AI Agents Across Multiple Platforms. https://www.truefoundry.com/
blog/cross-platform-ai-agent-governance
• [45] Dhimate, Y. (2026). A Framework for Architecting Agent Control Plane. MuleSoft Blog, 12 août 
2026. https://blogs.mulesoft.com/agentic-perspectives/a-framework-for-architecting-agent-control-plane
• [46] Shah, N., Lefferts, R. et Roszak, J. (2026). Microsoft Agent 365, now generally available, expands 
capabilities and integrations. Microsoft Security Blog, 1er mai 2026. https://www.microsoft.com/en-us/
security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations
• [47] ServiceNow (2026). ServiceNow expands AI Control Tower to discover, observe, govern, secure, 
and measure AI deployed across any system in the enterprise. Communiqué, 5 mai 2026. https://
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 252 sur 283
