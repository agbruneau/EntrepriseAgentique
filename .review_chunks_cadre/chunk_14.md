# chunk_14 — pages PDF 131 à 142 (sur 283)



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


---
## [Page PDF 133]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
ASI03 seul : NHI1 (retrait inadéquat) relève d’ASI04, NHI2 (fuite de secrets) d’ASI02 et d’ASI06, et NHI4 
(authentification non sécurisée) d’ASI03 et d’ASI07[28, 349].
EXIG-SEC-02 · DOIT
Matrice de traçabilité des menaces
L’équipe de sécurité DOIT tenir une matrice qui relie chaque risque ASI, chaque menace T1 à T17 
pertinente et chaque technique MITRE ATLAS retenue aux exigences du cadre et aux tests qui les 
vérifient, en s’appuyant sur les correspondances officielles de l’OWASP. La matrice DOIT être mise à 
jour à chaque nouvelle version du Top 10 agentique ou d’ATLAS.
Pourquoi : une menace sans contrôle ni test associé n’est pas maîtrisée; la matrice rend ces écarts visibles en revue.
9.6 Se défendre contre l’injection d’instructions
L’injection d’instructions (prompt injection) est la menace centrale des agents : un texte placé par un tiers 
dans une page web, un document, une réponse d’outil ou un message d’agent est interprété comme une 
consigne. Cette section pose le principe de présomption d’injection, puis échelonne les contrôles du plus 
faible au plus fort.
Présumer l’injection
Le NIST classe l’injection d’invite indirecte (NISTAML.015) dans sa taxonomie des attaques et recommande 
de concevoir les systèmes en présumant que l’injection est possible dès qu’un modèle reçoit des entrées non 
fiables[97]. Le Centre national de cybersécurité du Royaume-Uni (NCSC) explique pourquoi, en décembre 
2025 : contrairement à une base de données, un modèle de langage ne sépare pas intrinsèquement les 
données des instructions. Le risque se gère donc comme un risque résiduel, par une conception déterministe 
qui limite ce que le système peut faire, et non par des listes de refus faciles à contourner[98]. Le guide du 
gouvernement du Canada sur l’IA agentique demande lui aussi de traiter le texte externe ou fourni par 
l’utilisateur comme des données à analyser, non comme des instructions à suivre[353].
EXIG-SEC-03 · DOIT
Présomption d’injection
Tout contenu qui ne provient ni du mandant authentifié ni de la configuration approuvée de l’agent 
DOIT être traité comme non fiable  : pages web, courriels, documents téléversés (y compris par 
le mandant), champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, 
messages et cartes d’autres agents. Le catalogue d’entreprise DOIT marquer chaque outil dont la sortie 
peut contenir du contenu de tiers, afin que la passerelle d’agents sache, sans se fier au modèle, qu’une 
session a consommé un tel contenu.
Pourquoi : un modèle ne distingue pas de façon fiable une donnée d’une consigne; les protections doivent donc 
reposer surtout sur des garde-fous déterministes, tenus hors du modèle, qui limitent ce que le système peut faire[98].
Éviter la triade létale
Simon Willison a nommé « triade létale » la combinaison de trois propriétés : accès à des données privées, 
exposition à du contenu non fiable et capacité de communiquer vers l’extérieur. Un agent qui les réunit peut 
être amené à exfiltrer des données, et la seule protection sûre consiste à éviter la combinaison[354]. Meta en a 
tiré, le 31 octobre 2025, une règle opérationnelle, la « règle de deux » : dans une même session, un agent ne 
devrait pas réunir plus de deux des propriétés [A] traiter des entrées non fiables, [B] accéder à des systèmes 
sensibles ou à des données privées, [C] changer un état ou communiquer vers l’extérieur. Si les trois sont 
nécessaires, l’agent ne devrait pas agir de façon autonome : il lui faut au minimum une supervision humaine 
ou un nouveau départ dans un contexte vierge[307].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 133 sur 283


---
## [Page PDF 134]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
LA TRIADE LÉTALE
Données
privées
Contenu
non fiable
Communication
externe ou effet
fuite
possible
Un agent qui réunit les trois propriétés peut être
amené à exfiltrer des données par un texte piégé.
Règle de deux par session
Au plus deux de ces propriétés :
[A] traite des entrées non fiables
[B] accède à des données sensibles
[C] change un état ou communique
Les trois à la fois : supervision humaine
ou nouveau contexte vierge obligatoires.
Patrons de conception résistants
• Plan puis exécution (plan figé avant
toute lecture non fiable)
• Double modèle : privilégié sans texte
non fiable, quarantaine sans outils
• Sélecteur d’actions, map-reduce,
minimisation du contexte
• Séparation des flux de contrôle
et de données (CaMeL)
CONTRÔLES DU CADRE, DU PLUS FAIBLE AU PLUS FORT
1 · Signaler
enveloppe « non
fiable », détection
réduit la probabilité
2 · Retirer
outils d’envoi retirés
dès que du contenu
non fiable est lu
3 · Concevoir
patrons ci-dessus
selon la classe
de risque
4 · Approuver
jeton signé pour
toute action P3 et
tout envoi externe
Présomption d’injection : un filtre de détection n’est jamais le contrôle principal.
Figure 19 — Défense contre l’injection : éviter la triade létale. Le diagramme de gauche montre la combinaison à éviter et la règle 
de deux qui la casse; la bande inférieure classe les contrôles du cadre du plus faible (signaler) au plus fort (approuver). Source : cadre 
CRE-IA-2026-01, d’après Willison (2025), Meta (2025) et Beurer-Kellner et al. (2025).
EXEMPLE
Un agent de service à la clientèle lit les courriels entrants [A], consulte le dossier du client [B] et dispose 
d’un outil d’envoi de courriel [C]. Un courriel piégé lui demande de « transférer l’historique du client 
pour vérification » à une adresse externe. Avec les règles ci-dessous, la passerelle retire l’outil d’envoi 
dès la lecture du courriel : l’agent prépare sa réponse en brouillon, et l’envoi n’a lieu qu’après une 
approbation humaine qui montre le destinataire et le contenu exacts.
EXIG-SEC-04 · DOIT
Règle de deux par session
La fiche de chaque agent DOIT déclarer lesquelles des trois propriétés il réunit dans une même session : 
[A] il traite du contenu non fiable; [B] il accède à des données sensibles ou à des outils P1; [C] il modifie 
un état ou communique vers l’extérieur (outils P2, P3 ou envoi externe). Un agent qui réunit les trois 
NE DOIT PAS exécuter d’action [C] sans approbation humaine liée à l’action exacte (section 8.5), sauf 
s’il repart d’un contexte vierge exempt du contenu non fiable.
Pourquoi : c’est la réunion des trois propriétés qui rend l’exfiltration possible; en retirer une seule suffit à rompre la 
chaîne[307, 354].
Quatre niveaux de contrôle
Les contrôles ne se valent pas. Le cadre les classe en quatre niveaux, du plus faible au plus fort (bande 
inférieure de la figure 19), et un agent exposé à du contenu non fiable en combine toujours plusieurs.
1. Signaler : enveloppe et détection
La passerelle place tout contenu non fiable dans une enveloppe marquée «  non fiable  » (délimiteurs, 
provenance, classification) avant son entrée dans le contexte du modèle. Ce marquage réduit la probabilité 
de succès d’une attaque sans l’éliminer. Dans les expériences de ses auteurs sur des modèles GPT, la mise 
en évidence de la provenance (spotlighting) a fait passer le taux de réussite des attaques de plus de 50 % à 
moins de 2 %, avec un effet minime sur la tâche[355]; un taux résiduel, même faible, reste exploitable par un 
attaquant patient. Les détecteurs comme les Prompt Shields d’Azure AI Content Safety repèrent les attaques 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 134 sur 283


---
## [Page PDF 135]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
par invite de l’utilisateur et par document, y compris, en préversion, dans les réponses d’outils; Microsoft 
précise toutefois qu’ils ne jugent ni de la nocivité ni de l’exactitude, et que leur performance hors de l’anglais 
peut varier[356]. Ces produits sont des exemples, non des exigences.
EXIG-SEC-05 · NE DOIT PAS
Détection jamais seule
Le marquage et la détection d’injection NE DOIVENT PAS constituer le seul contrôle d’un agent 
exposé à du contenu non fiable. Avant la mise en production, leur efficacité DOIT être mesurée sur un 
jeu d’attaques rédigées en français et en anglais, et le résultat consigné à la fiche de l’agent.
Pourquoi : un filtre se contourne par reformulation, et un détecteur surtout évalué en anglais peut laisser passer une 
attaque rédigée en français[98, 356].
2. Retirer : capacités d’envoi retirées après une lecture non fiable
Un contrôle déterministe efficace consiste à retirer la capacité d’exfiltrer au moment où le risque apparaît. 
La passerelle sait, grâce au marquage du catalogue, qu’une session vient de consommer du contenu non 
fiable; elle restreint alors les outils offerts à l’agent pour le reste de la session. Le modèle n’a rien à décider : 
l’outil d’envoi n’est tout simplement plus disponible.
EXIG-SEC-06 · DOIT
Retrait déterministe des capacités d’exfiltration
Dès qu’une session a consommé du contenu non fiable, la passerelle d’agents DOIT retirer à l’agent, 
pour le reste de la session, les outils d’envoi vers l’extérieur et les outils P3, et refuser toute requête 
sortante vers une destination absente de la liste d’autorisation. Une action ainsi retirée ne s’exécute 
qu’avec une approbation humaine liée à l’action exacte. Le retrait est appliqué par la passerelle à partir 
du marquage du catalogue, jamais par une consigne donnée au modèle.
Pourquoi : le retrait de la capacité d’exfiltration est appliqué par la passerelle et ne dépend pas du comportement du 
modèle, alors que l’injection d’instructions ne se détecte pas de façon fiable; le marquage seul réduit le risque sans 
l’éliminer (raisonnement du cadre)[307, 354].
3. Concevoir : patrons résistants à l’injection
Beurer-Kellner et ses coauteurs (2025) proposent six patrons de conception qui offrent une résistance 
démontrable à l’injection. Leur principe commun : une fois le contenu non fiable ingéré, l’agent est contraint 
de sorte que ce contenu ne puisse déclencher aucune action conséquente[357]. Le tableau 39 les résume et 
indique l’usage que le cadre en recommande.
Tableau 39 — Patrons de conception résistants à l’injection et usage recommandé
Patron
Principe
Usage recommandé par le 
cadre
Sélecteur 
d’actions (Action-Selector)
Le modèle traduit la demande en une action choisie dans 
une liste fixe; le résultat de l’action ne revient pas au 
modèle.
Routage, assistants de com­
mande à faible variété.
Plan puis exécution 
(Plan-Then-Execute)
Le plan d’appels d’outils est figé avant toute lecture de 
contenu non fiable; ce contenu ne peut plus ajouter 
d’action.
Flux répétitifs : tri de cour­
riels, préparation de rap­
ports.
Map-reduce de modèles (LLM 
Map-Reduce)
Chaque document non fiable est traité par une instance 
isolée qui renvoie une sortie contrainte (catégorie, champ 
validé par schéma); l’agrégation ne voit que ces sorties.
Traitement en lot de docu­
ments de tiers : factures, CV, 
pages web.
Double modèle (Dual LLM)
Un modèle privilégié, doté d’outils, ne voit jamais le texte 
non fiable; un modèle en quarantaine, sans outils, le traite; 
un contrôleur logiciel ne transmet que des références sym­
boliques[358].
Assistants qui lisent des 
courriels ou des documents 
de tiers.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 135 sur 283


---
## [Page PDF 136]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Patron
Principe
Usage recommandé par le 
cadre
Code puis exécution 
(Code-Then-Execute)
Le modèle écrit un programme qui appelle les outils; le 
programme, exécuté en bac à sable, traite le contenu non 
fiable par des appels isolés.
Agents de risque élevé qui 
exigent des garanties dé­
montrables.
Minimisation du contexte 
(Context-Minimization)
Les éléments devenus inutiles, comme la requête initiale 
une fois convertie en requête structurée, sont retirés du 
contexte avant les étapes suivantes.
Mesure complémentaire, 
combinable avec les autres 
patrons.
CaMeL, proposé par Google DeepMind et l’ETH Zurich en mars 2025, pousse le patron «  code puis 
exécution » jusqu’à extraire les flux de contrôle et de données de la seule requête de confiance, de sorte 
que des données non fiables ne puissent jamais modifier le déroulement du programme. Sur le banc d’essai 
AgentDojo, il résout 77 % des tâches avec une sécurité démontrable, contre 84 % pour un système non 
défendu[101]. Le coût en utilité est réel, mais quantifié (7 points de pourcentage sur AgentDojo) : c’est le prix 
d’une garantie plutôt que d’une probabilité.
EXIG-SEC-07 · DOIT
Patron de conception pour les agents de risque élevé
Un agent de classe de risque élevée exposé à du contenu non fiable DOIT appliquer au moins un des 
patrons du tableau 39 autre que la minimisation du contexte, consigné à la fiche de l’agent (annexe B) 
et vérifié en revue de conception. Un agent de risque modéré dans la même situation DEVRAIT en 
appliquer un.
Pourquoi : ces patrons empêchent par construction le contenu non fiable de choisir les actions, ce qu’aucun filtre ne 
garantit[357].
4. Approuver : la personne voit l’action exacte
Pour toute action P3 et tout envoi externe après une lecture non fiable, le dernier rempart est l’approbation 
humaine vérifiable : un jeton signé, lié à l’empreinte de l’outil et de ses arguments, que la passerelle vérifie 
avant l’exécution (section 8.5). Un « oui » écrit dans la conversation de l’agent n’est jamais une approbation, 
puisqu’une injection peut l’imiter.
ATTENTION
Les « taux de réussite des attaques » cités sans contexte induisent en erreur. Le chiffre de 84,30 % 
provient de l’Agent Security Bench (ICLR 2025) : c’est le taux moyen de réussite d’attaque le plus élevé 
observé sur un banc d’essai couvrant les injections dans l’invite système, l’invite de l’utilisateur, les 
outils et la mémoire, où les défenses évaluées se sont révélées d’efficacité limitée[359]. Il décrit un banc 
d’essai, non la probabilité de compromission d’un système réel; le cadre exige de mesurer ses propres 
agents (section 9.9).
9.7 Cloisonnement de l’exécution du code
Cette section fixe où et comment s’exécute le code qu’un agent génère ou reçoit. Un appel d’outil prédéfini 
a des effets connus d’avance; un script généré peut tout faire. Il suffit d’un fichier CSV piégé, soumis pour 
analyse, pour qu’un agent écrive un script qui lit des secrets et les envoie à l’extérieur. Le cloisonnement 
vise à ce que, même dans ce cas, le script ne trouve rien à voler et aucun chemin pour sortir.
Choisir la technologie d’isolation
Toutes les technologies ne placent pas la frontière d’isolation au même endroit (figure 20). Un conteneur 
Linux standard isole par espaces de noms, cgroups et filtres seccomp-bpf, mais tous les conteneurs d’un hôte 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 136 sur 283


---
## [Page PDF 137]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
partagent un noyau unique, ce qui impose un compromis entre sécurité et compatibilité[360]. Pour le code 
généré, l’OWASP recommande des conteneurs en bac à sable aux limites strictes (ASI05)[28]. Le cadre va plus 
loin, par choix : il interdit le noyau partagé pour tout code non fiable, parce qu’un agent peut produire, à la 
demande d’un attaquant, exactement le code qui exploite une faille du noyau.
Conteneur standard
Code généré par l’agent
Espaces de noms, cgroups
Noyau de l’hôte
PARTAGÉ
Matériel
Interdit pour code non fiable
gVisor
Code généré par l’agent
Noyau applicatif en espace
utilisateur (Sentry)
Noyau de l’hôte
appels système filtrés
(seccomp)
Matériel
Admis · GPU avec réserves
MicroVM (Firecracker, Kata)
Code généré par l’agent
Noyau invité dédié
VMM minimal + jailer
Noyau hôte + KVM
Matériel (virtualisation)
Option par défaut
WebAssembly (WASI)
Module compilé en Wasm
Environnement sans autorité
ambiante (capacités)
Processus hôte
et noyau
Matériel
Admis pour greffons Wasm
frontière d’isolation principale
QUATRE VERROUS OBLIGATOIRES, QUELLE QUE SOIT LA TECHNOLOGIE
Réseau fermé par défaut
liste d’autorisation explicite,
DNS restreint, métadonnées
infonuagiques bloquées
Secrets hors du bac à sable
injectés par le mandataire
de sortie; jamais lisibles
par le code de l’agent
Délais à trois niveaux
par appel d’outil, par boucle
de tâche, par durée de vie
du bac à sable; éphémère
Journalisation immuable
commandes, écritures de
fichiers et requêtes réseau
consignées hors du bac à sable
Figure 20 — Niveaux d’isolation pour le code généré. Chaque colonne situe la frontière d’isolation principale d’une technologie, 
du noyau partagé (interdit) à la microVM (option par défaut); la bande inférieure rappelle les quatre verrous exigés quelle que soit la 
technologie. Source : cadre CRE-IA-2026-01, d’après Agache et al. (2020), la documentation de gVisor et de WASI, et l’OWASP (ASI05).
Tableau 40 — Technologies d’isolation du code généré
Technologie
Principe
Frontière d’isolation
Coût et contraintes
Usage recom­
mandé
Conteneur à 
noyau partagé
Espaces de noms, cgroups 
et seccomp-bpf sur le noyau 
de l’hôte.
Noyau de l’hôte, par­
tagé par tous les 
conteneurs.
Faible coût, compatibilité 
maximale.
Interdit pour le 
code non fiable 
(choix du cadre).
gVisor
Noyau applicatif en espace 
utilisateur (le Sentry, écrit en 
Go) qui traite lui-même les 
appels système; accès aux 
fichiers délégué au proces­
sus Gofer[134].
Sentry, sous filtre sec­
comp restrictif.
Aucun surcoût sur l’exécution 
brute; surcoût important pour 
les charges riches en pe­
tits appels système ou 
en nombreuses opérations 
sur le système de fichiers; 
compatibilité partielle, gVisor 
n’implémentant qu’un sous-
ensemble de l’interface Li­
nux[361, 362].
Admis ; option 
pour les GPU, 
avec réserves.
MicroVM Firecra­
cker
Moniteur de machines vir­
tuelles en Rust sur KVM; 
chaque microVM a son 
propre noyau invité[133].
Virtualisation maté­
rielle, plus le jailer.
Moins de 5 Mio de sur­
coût mémoire et démarrage 
en moins de 125 ms avec le 
noyau minimal du projet[363].
Par défaut
Kata Containers
Machines virtuelles lé­
gères intégrées à l’outillage 
de conteneurs, avec QE­
MU, Cloud Hypervisor 
ou Firecracker; projet de 
l’OpenInfra Foundation[135].
Virtualisation maté­
rielle.
Surcoût d’une machine vir­
tuelle; compatible avec Kuber­
netes.
Par défaut sur 
plateforme Ku­
bernetes.
WebAssembly 
(WASI)
Sécurité par capacités : le 
module démarre sans auto­
Environnement 
d’exécution Wasm.
Format binaire compact et ra­
pide à charger, mais le code 
doit être compilé en Wasm[364]; 
Admis pour gref­
fons et fonctions 
compilés.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 137 sur 283


---
## [Page PDF 138]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Technologie
Principe
Frontière d’isolation
Coût et contraintes
Usage recom­
mandé
rité ambiante et ne fait que 
ce que l’hôte lui accorde[136].
risques résiduels : déborde­
ments dans la mémoire li­
néaire, canaux auxiliaires tem­
porels[365].
Les chiffres publiés par les concepteurs de Firecracker datent de 2020 : environ 50 000 lignes de Rust, soit 96 % 
de moins que QEMU, qui dépassait alors 1,4 million de lignes[360]. Selon son site, Firecracker n’émule que cinq 
périphériques (virtio-net, virtio-block, virtio-vsock, une console série et un contrôleur de clavier minimal), 
sans BIOS d’après l’article de 2020; les versions récentes ajoutent toutefois d’autres périphériques (entropie 
virtio-rng depuis la 1.4, virtio-pmem et virtio-mem depuis la 1.14) et un transport PCI facultatif (depuis la 
1.13), de sorte que la surface exposée dépend de la version et de la configuration déployées[133]. Son jailer 
ajoute une seconde ligne de défense : chroot, espaces de noms PID et réseau, abandon des privilèges et profil 
seccomp-bpf limité à 24 appels système et 30 ioctl[363]. Les temps de reprise annoncés par les fournisseurs 
de bacs à sable gérés, par exemple moins de 25 ms chez Blaxel ou environ une seconde chez E2B, sont des 
allégations commerciales mesurées dans leurs propres conditions[366, 367].
EXIG-SEC-08 · DOIT
Technologie d’isolation du code non fiable
Tout code généré par un agent, ou reçu d’une source non fiable, DOIT s’exécuter dans une microVM 
(Firecracker, Kata Containers), sous gVisor ou, s’il est compilé en WebAssembly, dans un environnement 
WASI sans autorité ambiante. Il NE DOIT PAS s’exécuter dans un conteneur à noyau partagé, dans le 
processus de l’agent ni sur l’hôte de la passerelle.
Pourquoi : la frontière doit résister à une faille du noyau, puisque l’attaquant choisit le code exécuté; ce choix du 
cadre est plus strict que la recommandation de l’OWASP.
EXIG-SEC-09 · DOIT
Bac à sable éphémère et minimal
Chaque bac à sable DOIT être créé pour une seule tâche ou une seule session, puis détruit, sans jamais 
être réutilisé pour un autre mandant; s’exécuter sans privilèges root; n’avoir aucun montage du système 
de fichiers de l’hôte; et appliquer des quotas de processeur, de mémoire, de disque et de processus.
Pourquoi : un environnement jetable, isolé par session et sans privilèges empêche qu’une compromission persiste 
ou atteigne la session d’un autre utilisateur[28].
EXIG-SEC-10 · DOIT
Charges qui exigent un GPU
Un bac à sable qui exige un GPU DOIT faire l’objet d’une analyse de risque propre, approuvée par la 
sécurité, et l’hôte DOIT maintenir ses pilotes à jour. Sous gVisor, l’analyse tient compte du fait que 
nvproxy relaie les appels ioctl au pilote NVIDIA de l’hôte et ne valide pas les tampons d’accès direct 
à la mémoire (DMA).
Pourquoi : gVisor prend en charge certains GPU NVIDIA (T4, A100, A10G, L4, H100), mais sa documentation 
reconnaît qu’il protège beaucoup moins bien contre les failles du pilote lui-même[368]; chez Modal, par exemple, les 
bacs à sable GPU ne sont offerts qu’avec gVisor[369].
EXIG-SEC-11 · DEVRAIT
Performance mesurée sur la charge réelle
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 138 sur 283


---
## [Page PDF 139]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
Les objectifs de latence et de coût des bacs à sable DEVRAIENT être fixés à partir de mesures faites sur 
la charge réelle de l’entreprise, et non à partir de chiffres de fournisseurs ou de pourcentages génériques.
Pourquoi : le coût de gVisor dépend du profil d’appels système et de la plateforme, et le temps de démarrage publié 
par Firecracker (moins de 125 ms) est mesuré dans des conditions précises (console série désactivée, noyau et système 
de fichiers racine minimaux)[133, 361, 370].
Quatre verrous obligatoires
Quelle que soit la technologie, quatre verrous s’appliquent (bande inférieure de la figure 20). Les trois 
premiers ferment les issues d’un code malveillant : sortir par le réseau, voler un secret, durer. Le quatrième 
garantit qu’on saura ce qui s’est passé.
Verrou 1 : réseau fermé par défaut
L’OWASP recommande des bacs à sable d’exécution dotés de listes d’autorisation sortantes qui refusent 
toute destination non approuvée (ASI02)[28]. Pour les clients MCP qui récupèrent des URL d’autorisation 
OAuth, la spécification MCP recommande (SHOULD) de bloquer les plages privées et lien-local, dont 
169.254.0.0/16 qui inclut les services de métadonnées d’AWS, de Google Cloud et d’Azure, et invite les 
exploitants à envisager un mandataire de sortie[208]. Le filtrage par nom de domaine a des limites documen­
tées : fondé sur l’indication du nom de serveur (SNI) du protocole TLS, il ne filtre pas le HTTP en clair et 
n’empêche pas par défaut le domain fronting; une politique fondée sur des plages IP laisse la résolution DNS 
ouverte, ce qui permet d’exfiltrer des données par le DNS[342].
EXIG-SEC-12 · DOIT
Sortie réseau refusée par défaut
Un bac à sable DOIT démarrer sans aucun accès réseau sortant, résolution DNS comprise. Chaque 
destination nécessaire DOIT être inscrite nommément à une liste d’autorisation tenue à la fiche de 
l’agent, sans règle générique; le trafic DOIT passer par un mandataire de sortie qui refuse le HTTP en 
clair et qui termine TLS pour les domaines où il injecte une authentification (EXIG-SEC-14). Les plages 
privées et lien-local, dont 169.254.0.0/16 et leurs équivalents IPv6 (fc00::/7, fe80::/10), DOIVENT 
être bloquées, à l’exception de l’adresse du mandataire de sortie.
Pourquoi : une sortie fermée par défaut limite l’exfiltration de données même lorsque le code exécuté n’est pas 
fiable[208, 342].
EXIG-SEC-13 · DOIT
Service de métadonnées infonuagiques
Sur toute plateforme, le service de métadonnées de l’hôte DOIT être inaccessible depuis les bacs à 
sable. Sur AWS, tout hôte qui exécute des agents ou des bacs à sable DOIT en outre être configuré pour 
n’accepter qu’IMDSv2.
Pourquoi  : IMDSv2 exige un jeton de session obtenu par une requête PUT, refuse d’en émettre si l’en-tête 
X-Forwarded-For est présent et limite par défaut les sauts IP à un, ce qui protège contre la plupart des attaques par 
falsification de requêtes côté serveur (SSRF)[371, 372].
Verrou 2 : secrets hors du bac à sable
Un secret absent ne peut pas être volé. Dans le patron de courtage d’identifiants, le mandataire de sortie 
ajoute l’en-tête d’authentification aux requêtes sortantes, de sorte que le secret n’entre jamais dans le bac 
à sable. Ce patron a ses limites : il dépend du SNI et exige que le mandataire termine TLS, et une règle 
générique « * » laisse passer sans transformation le trafic dont le domaine n’est pas détectable[342]. Le 
brouillon WIMSE AIMS interdit par ailleurs au modèle d’accéder aux justificatifs de l’agent[93]. Enfin, pour 
l’appel d’outils programmatique, les bonnes pratiques MCP prévoient un code sans accès réseau direct, un 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 139 sur 283


---
## [Page PDF 140]

CRE-IA-2026-01 · Cadre de référence
9 Identité, sécurité et confiance zéro
hôte courtier qui détient les identifiants et applique à chaque appel la même politique d’approbation qu’à 
un appel direct, et des résultats d’un serveur traités comme non fiables pour un autre[204].
EXIG-SEC-14 · NE DOIT PAS
Secrets injectés par le mandataire de sortie
Un secret (clé, jeton, mot de passe, certificat) NE DOIT PAS se trouver dans le bac à sable, ses 
variables d’environnement, ses fichiers ou le contexte du modèle. Lorsque le code appelle un service, 
le mandataire de sortie, situé hors du bac à sable, DOIT ajouter l’authentification après vérification 
de la destination; lorsque le code appelle des outils, l’hôte courtier DOIT appliquer à chaque appel les 
mêmes contrôles d’autorisation et d’approbation qu’à un appel direct de l’agent.
Pourquoi : le code compromis ne peut ni lire ni réutiliser un justificatif qu’il ne détient pas[93, 342].
Verrou 3 : délais à trois niveaux
Aucune norme ne fixe ces délais. L’OWASP recommande des plafonds d’usage (coût, débit, jetons)[28], et les 
fournisseurs imposent leurs propres durées maximales, par exemple cinq minutes par défaut chez Modal[369]. 
Le cadre fixe donc des valeurs par défaut, ajustables à la fiche de l’agent.
EXIG-SEC-15 · DOIT
Délais à trois niveaux
Chaque bac à sable DOIT appliquer trois délais maximaux : par appel d’outil ou exécution de script 
(30 secondes par défaut), par boucle de tâche (20 minutes par défaut) et pour sa durée de vie totale 
(destruction dès la fin de la tâche et, au plus tard, après 60 minutes par défaut). Ces valeurs sont des 
choix du cadre; toute valeur supérieure DOIT être justifiée à la fiche de l’agent.
Pourquoi : un délai borne la durée d’une exfiltration lente, d’un minage de cryptomonnaie ou d’une boucle, même 
lorsque les autres contrôles ont échoué.
Verrou 4 : journalisation immuable
EXIG-SEC-16 · DOIT
Journal d’exécution tenu hors du bac à sable
Chaque commande exécutée, chaque écriture de fichier et chaque requête réseau d’un bac à sable 
DOIVENT être consignées par un composant situé hors du bac à sable, dans un journal inaltérable 
rattaché à la trace de la tâche (section 10.3).
Pourquoi : l’OWASP demande de journaliser toute génération et exécution de code (ASI05) et de tenir des journaux 
complets, immuables et signés des actions des agents (ASI10)[28]; un journal tenu dans le bac à sable pourrait être 
effacé par le code qu’il surveille.
Séparer la génération de l’exécution
Le bac à sable limite les dégâts; il ne dispense pas de vérifier ce qu’on exécute. L’OWASP recommande, 
pour ASI05, d’interdire eval dans les agents en production, d’exiger des interpréteurs sûrs et le suivi de 
contamination du code généré, de ne jamais exécuter en root, d’isoler les environnements par session, de 
séparer génération et exécution par des portes de validation, d’analyser le code avant exécution et de le 
surveiller pendant, et d’exiger une approbation humaine pour les exécutions à privilèges élevés[28].
EXIG-SEC-17 · DOIT
Porte de validation du code généré
Le code généré DOIT franchir une porte de validation avant exécution  : analyse statique, refus 
des constructions d’évaluation dynamique (eval et équivalents) dans les agents en production, et 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 140 sur 283


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
