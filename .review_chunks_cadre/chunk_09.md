# chunk_09 — pages PDF 81 à 92 (sur 283)



---
## [Page PDF 81]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
car la liaison reprend par défaut la clé fournie par l’utilisateur[250]. Les files coopératives NE DOIVENT 
PAS servir à un tel flux; elles conviennent aux bassins d’exécutants dont les tâches sont indépendantes.
Pourquoi : Kafka ne garantit l’ordre qu’au sein d’une partition, et une file coopérative ne le garantit qu’à l’intérieur 
d’un lot.
EXIG-EVT-10 · DOIT
Conservation des entrées et rejeu isolé
Les sujets qui alimentent des agents de classe de risque modérée ou élevée DOIVENT conserver leurs 
événements au moins pendant la fenêtre d’enquête inscrite à la fiche de l’agent (au moins 90 jours 
pour la classe modérée et un an pour la classe élevée, sans excéder la rétention des traces et journaux 
d’audit fixée au chapitre 10), dans la limite du calendrier de conservation applicable aux RP. Tout rejeu 
DOIT s’exécuter dans un environnement isolé où les outils à effet sont remplacés par des doublures; 
ses résultats servent à l’audit et à l’évaluation continue (section 10.4), jamais à répéter des actions en 
production.
Pourquoi : rejouer des entrées contre des outils réels répéterait leurs effets, et un modèle peut décider autrement la 
seconde fois.
6.8 Contrats, versionnage et catalogue d’entreprise
Cette section fixe ce que chaque interface offerte à un agent doit déclarer, comment ses versions évoluent 
sans briser ses consommateurs et ce que contient le catalogue d’entreprise.
Ce que chaque contrat déclare
Un contrat a deux faces : ce que le fournisseur publie dans le format du protocole, et ce que l’entreprise fixe 
au catalogue. Comme les annotations MCP sont des indices non fiables (EXIG-MCP-14) et que la carte A2A 
n’admet aucun champ de gouvernance hors norme (EXIG-A2A-05), tout ce qui commande une décision de 
sécurité vit au catalogue (tableau 22; exemples à l’annexe C).
Tableau 22 — Contenu minimal des contrats, par type d’interface
Interface
Contrat publié
Entrée fixée au catalogue
Outil MCP
Nom préfixé par le domaine; description destinée au 
modèle, qui dit ce que fait l’outil et ce qu’il ne fait 
pas; inputSchema et, au besoin, outputSchema en JSON 
Schema 2020-12; clé d’idempotence pour tout outil à 
effet (section 7.6)
Version et empreinte; palier P0 à P3 et seuil 
(section 8.3); compensation de toute écriture P2; 
propriétaire et équipe de garde; classification maxi­
male des données
Ressource et in­
vite MCP
Ressource adressée par URI; invite nommée et décrite
Version et empreinte; classification
Agent A2A
Carte A2A 1.0 signée (section 6.6)
Version et empreinte; portée OAuth par compé­
tence; renvoi à la fiche du registre
Sujet 
d’événement
Contrat AsyncAPI 3.x et type versionné (section 6.7)
Producteurs et consommateurs autorisés; classifi­
cation; plafond de sauts
API existante
Contrat OpenAPI 3.1.x ou 3.2.x; erreurs au format RFC 
9457[171]
Outils MCP qui l’exposent, chacun avec son entrée
EXIG-INT-12 · DOIT
Contrat complet avant l’inscription
Toute interface offerte à un agent DOIT disposer, avant son inscription au catalogue d’entreprise, d’un 
contrat publié et d’une entrée de catalogue qui contiennent au minimum les éléments du tableau 22. 
Un élément manquant bloque l’inscription.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 81 sur 283


---
## [Page PDF 82]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Pourquoi : la passerelle n’applique que des règles écrites; sans palier ni compensation déclarés, l’agent déciderait 
seul de ce qui est sûr.
Versionnage sémantique
La version d’un protocole ne dit rien des contrats publiés sur lui. Or la définition d’un outil MCP ne comporte 
aucun champ de version[197], et le champ version d’une carte A2A est de format libre[68]. Le cadre impose 
donc aux contrats le versionnage sémantique (SemVer), de forme MAJEUR.MINEUR.CORRECTIF, tenu au 
catalogue :
• majeur : tout changement qui peut faire échouer ou tromper un consommateur (élément retiré ou 
renommé, nouveau paramètre obligatoire, valeurs admises restreintes en entrée, valeur ajoutée à une 
énumération de sortie, changement de sens à format constant);
• mineur : ajout compatible et toute reformulation d’une description;
• correctif : correction qui ne change ni la définition publiée ni le comportement attendu.
Le changement de sens est le plus dangereux, car aucun validateur ne le voit : un montant qui passe de hors 
taxes à toutes taxes comprises reste un nombre valide (section 6.1). A2A applique la même logique à ses 
extensions, dont tout changement incompatible exige une nouvelle URI[238].
EXIG-INT-13 · DOIT
Versionnage sémantique des contrats
Tout contrat inscrit au catalogue DOIT porter une version SemVer, incrémentée à chaque publication 
selon les règles ci-dessus : au moins mineure pour toute modification de la définition publiée (nom, 
description, schémas, annotations, compétences), majeure pour tout changement incompatible, y 
compris de sens. Pour un agent A2A, c’est le champ version de sa carte (EXIG-A2A-04).
Pourquoi : un numéro régi par des règles connues dit au consommateur s’il peut migrer sans risque (règle du cadre).
EXIG-INT-14 · DOIT
Coexistence d’au moins 60 jours
À la publication d’une version majeure, la version majeure précédente DOIT rester disponible au moins 
60 jours (choix du cadre), avec une date de retrait inscrite au catalogue dès ce moment et annoncée aux 
consommateurs connus. Seul un motif de sécurité, sur décision du comité, justifie un retrait anticipé.
Pourquoi : un délai connu permet de planifier les migrations; il concorde avec le préavis de retrait d’un agent 
(section 11.5).
Épinglage et approbation des changements
Un consommateur ne suit jamais « la dernière version ». Il dépend d’une version identifiée par son numéro 
et par son empreinte, soit le condensé SHA-256 de la définition canonisée selon la RFC 8785[236]. Le numéro 
dit ce que le fournisseur affirme; l’empreinte prouve ce que l’agent reçoit. La fiche d’agent consigne ces 
dépendances (annexe B), et la passerelle vérifie l’empreinte à l’exécution (EXIG-MCP-20, EXIG-SEC-18). 
L’OWASP recommande d’épingler les définitions par empreinte et de redemander le consentement à chaque 
modification[221].
EXIG-INT-15 · DOIT
Dépendances épinglées par version et empreinte
Chaque agent DOIT déclarer dans sa fiche, pour chaque outil, ressource, invite, agent appelé et sujet 
d’événement, la version épinglée et l’empreinte approuvée. Une dépendance NE DOIT PAS désigner 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 82 sur 283


---
## [Page PDF 83]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
une version flottante (« dernière », plage de versions); changer de version est une modification de la 
fiche, revue et tracée.
Pourquoi : sans épinglage, un fournisseur peut changer le comportement d’un agent à l’insu de son propriétaire.
EXIG-INT-16 · DOIT
Nouvelle approbation à toute modification
Toute modification de la définition publiée d’un outil, d’une ressource, d’une invite ou d’une carte 
d’agent, y compris la reformulation d’une description, DOIT être revue et approuvée de nouveau au 
catalogue avant d’être servie aux agents, y compris pour les serveurs et agents de tiers. La revue 
confirme aussi le palier attribué.
Pourquoi : le modèle lit la description comme une consigne, et la substitution après approbation (rug pull) exploite 
justement un changement présenté comme anodin (section 9.8).
Catalogue d’entreprise
Le catalogue d’entreprise recense tous les contrats joignables par les agents. Le catalogue des protocoles 
(section 6.3) dit quels standards employer; le catalogue d’entreprise, quels contrats existent sur ces standards. 
Le registre (section 11.4) dit qui répond d’un agent et avec quel risque; le catalogue, par quel contrat et dans 
quelle version. Le registre officiel MCP, en préversion, n’en tient jamais lieu[43].
Chaque version de contrat est « en revue », « active », « dépréciée » (avec sa date de retrait) ou « retirée », 
à l’image du cycle Active, Deprecated, Removed que MCP applique à ses propres fonctionnalités[34]. Ces états 
sont distincts de ceux de la fiche d’agent. Sans la liste des consommateurs de chaque version, on découvre 
ceux d’une version retirée par leurs pannes.
EXIG-INT-17 · DOIT
Catalogue unique, source de la découverte
L’entreprise DOIT tenir un seul catalogue d’entreprise, sous une même autorité et articulé avec le 
registre de gouvernance (section 11.4), qui recense chaque version de contrat (schéma, serveur MCP, 
carte d’agent A2A, sujet AsyncAPI) avec son état, son propriétaire, son empreinte et, s’il y a lieu, sa 
date de retrait. La découverte passe par lui, jamais par une adresse configurée à la main; la passerelle 
ne sert que les versions actives et les versions dépréciées non échues.
Pourquoi : deux sources de vérité finissent par diverger.
EXIG-INT-18 · DOIT
Consommateurs connus avant tout retrait
Le catalogue DOIT indiquer les consommateurs connus de chaque version active ou dépréciée, tirés 
des fiches d’agents et rapprochés chaque mois des appels observés par la passerelle (fréquence fixée par 
le cadre). Une version n’est retirée qu’à l’échéance annoncée, jamais avant la fin de la coexistence de 
l’EXIG-INT-14, et après avis à ses consommateurs connus; les traces servent à repérer, avant l’échéance, 
les appels de consommateurs non déclarés.
Pourquoi : les traces révèlent les consommateurs non déclarés avant que le retrait ne les brise.
Tests de compatibilité
Une règle de versionnage ne tient que si une machine la vérifie; seul le changement de sens échappe à la 
comparaison des schémas et relève de la revue sémantique (EXIG-INT-01 et EXIG-INT-16). Les suites de 
conformité complètent les tests internes : a2a-tck, dont les tests MUST sont bloquants (EXIG-A2A-14)[243], 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 83 sur 283


---
## [Page PDF 84]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
et le cadre officiel de tests de conformité MCP, encore en versions 0.x (préversion 0.2.0-alpha en cours)[225, 
226]. Ces tests forment le premier palier de l’évaluation continue (section 10.4).
EXIG-INT-19 · DOIT
Détection automatique des ruptures
La chaîne d’intégration DOIT comparer chaque nouvelle version d’un contrat à la version active précé­
dente et bloquer toute publication qui contient un changement incompatible sans incrément majeur. 
Avant son activation, la nouvelle version DOIT réussir les tests de contrat de ses consommateurs 
connus et, pour un agent A2A, les tests MUST d’a2a-tck; les résultats du cadre officiel de conformité 
MCP (ou d’une suite équivalente approuvée par l’architecture d’entreprise, EXIG-APP-08) sont consi­
gnés à titre informatif tant que ce cadre demeure en préversion 0.x et se déclare instable.
Pourquoi : une règle de compatibilité vérifiée à la main finit par céder sous la pression d’une livraison.
6.9 Protocoles émergents et veille
Cette section situe les travaux qui n’ont pas le statut Adopter (section 6.3) et en encadre l’usage; le processus 
de veille relève de la section 11.7.
Ce que l’AAIF héberge réellement
Au 22 octobre 2026, l’Agentic AI Foundation (AAIF) héberge dix projets  : MCP, goose, AGENTS.md, 
agentgateway, A2A, Agent Router et, annoncés ce jour-là, Agent Skills, Open Responses, OpenEnv et 
OpenSandbox[38, 130]. L’admission suit un processus formel : proposition publique, triage, recommandation 
du comité technique, puis approbation du conseil d’administration, suivie des formalités juridiques et de 
l’intégration technique menées avec la Linux Foundation[42, 263]. Un projet proposé n’est qu’un candidat, et 
l’hébergement garantit une gouvernance neutre, non la maturité d’une spécification.
EXIG-INT-20 · NE DOIT PAS
Qualification « AAIF » vérifiée
Un document d’architecture, un appel d’offres ou un contrat NE DOIT PAS qualifier un projet de 
standard ou de projet de l’AAIF s’il ne figure pas à la liste des projets publiée par la fondation au terme 
d’une admission approuvée; un projet dont la proposition est ouverte est dit « candidat à l’AAIF ». 
L’hébergement par l’AAIF ne dispense d’aucun critère d’admission au statut Adopter (EXIG-GOV-19).
Pourquoi : AGNTCY, souvent présenté comme une composante de l’AAIF, n’en est qu’un candidat[37]; l’erreur fausse 
l’analyse du risque fournisseur.
AGNTCY
AGNTCY, rendu public par Cisco en mars 2025, est un projet de la Linux Foundation depuis le 29 juillet 
2025[23]. Sa proposition à l’AAIF, déposée par Cisco le 12 octobre 2026, fait état de 81 organisations qui 
l’appuient, indique que Cisco fournit l’essentiel des contributions et restait sans décision au 27 octobre 
2026[37]. Le tableau 23 présente ses principaux composants.
Tableau 23 — Principaux composants d’AGNTCY et statut au catalogue (état au 27 octobre 2026)
Composant
Fonction vérifiée
Statut
OASF (Open Agentic 
Schema Framework)
Modèle de données extensible, inspiré d’OCSF (Open Cybersecurity Schema Frame­
work), qui décrit des agents par des enregistrements annotés de compétences et 
de domaines; l’Agent Directory Service (ADS) y convertit des définitions de serveurs 
MCP, des cartes d’agent A2A et des Agent Skills[264, 265]
Évaluer
Agent Directory Ser­
vice (ADS)
Annuaire d’enregistrements OASF stockés comme artefacts OCI (Open Container Ini­
tiative), adressés par leur condensé, signés et vérifiables[266, 267]
Évaluer
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 84 sur 283


---
## [Page PDF 85]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Composant
Fonction vérifiée
Statut
SLIM (Secure 
Low-Latency Interac­
tive Messaging)
Messagerie sur gRPC et HTTP/2, sessions chiffrées de bout en bout par MLS (Messa­
ging Layer Security) (RFC 9420)[268, 269]
Surveiller
Identity
Identifiants d’agents et de serveurs MCP adossés à des justificatifs vérifiables du W3C 
(« Agent Badges »)[270]
Surveiller
Trois précautions s’imposent. Les spécifications d’ADS et de SLIM soumises à l’IETF sont des brouillons 
individuels[271, 272]. La résistance de SLIM à l’ordinateur quantique, parfois avancée, n’est pas étayée : les 
suites cryptographiques initiales de MLS sont classiques[269]. Enfin, la liaison SLIMRPC reste expérimentale 
(EXIG-A2A-08), et la carte d’agent suit le schéma d’A2A, non celui d’OASF.
EXIG-INT-21 · DOIT
Pilotes AGNTCY subordonnés au catalogue
Tout pilote d’OASF ou d’ADS DOIT traiter le catalogue d’entreprise comme source de vérité : les 
enregistrements de l’annuaire en sont dérivés, et aucun agent n’y découvre un outil ou un agent absent 
du catalogue. Une propriété de sécurité alléguée, comme la résistance de SLIM au quantique, NE DOIT 
PAS entrer dans une analyse de risque sans preuve de la configuration effective.
Pourquoi : un annuaire parallèle recréerait deux sources de vérité, et une propriété non démontrée ne protège rien.
Commerce et paiements agentiques
Trois protocoles se partagent le commerce agentique, sans convergence. L’Agentic Commerce Protocol 
d’OpenAI et de Stripe (septembre 2025) demeure en bêta[183]; son jeton de paiement partagé est limité à un 
marchand et au montant d’un panier, et masque les justificatifs de paiement à la plateforme d’IA[27]. AP2 
(Agent Payments Protocol), publié par Google en septembre 2025, étend A2A et MCP par des mandats signés 
qui prouvent l’intention et l’autorisation de l’utilisateur; sa version 0.2 ajoute les paiements en l’absence 
de l’utilisateur (Human Not Present), et Google en a fait don à la FIDO Alliance le 28 avril 2026[26, 41]. UCP 
(Universal Commerce Protocol), annoncé en janvier 2026 par Google en collaboration avec des détaillants et 
des plateformes de commerce, prend en charge REST, MCP et A2A et est compatible avec AP2[184]. Les trois 
restent au statut Surveiller, mais leurs patrons inspirent déjà la règle qui suit.
EXIG-INT-22 · DOIT
Paiements initiés par un agent
Tout paiement, achat ou engagement financier déclenché par un agent, quel que soit le protocole, DOIT 
être classé P3 et n’être exécuté qu’avec une approbation humaine signée, liée à l’action exacte (section 
8.5). L’agent NE DOIT PAS recevoir ni transmettre de justificatif de paiement; il ne manipule que des 
jetons émis hors de lui, limités à un bénéficiaire et à un montant. Chaque paiement DOIT laisser au 
journal d’audit une preuve d’intention signée. Le paiement en l’absence de l’utilisateur NE DOIT PAS 
être autorisé tant qu’aucun protocole qui l’encadre n’a le statut Adopter.
Pourquoi : AP2 fonde l’imputabilité d’un paiement sur des mandats signés, l’Agentic Commerce Protocol limite son 
jeton à un marchand et à un montant; le cadre généralise ces patrons à tout paiement.
Signaux à suivre
La veille n’est vérifiable que si l’on sait ce que l’on attend : une décision de l’AAIF sur AGNTCY, une révision 
de MCP, dont la feuille de route du 22 août 2026 ne donne pas la date[195], ou la première version étiquetée 
des conventions GenAI d’OpenTelemetry[181].
EXIG-INT-23 · DOIT
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 85 sur 283


---
## [Page PDF 86]

CRE-IA-2026-01 · Cadre de référence
6 Interopérabilité
Signal de révision inscrit au catalogue
Chaque entrée du catalogue des protocoles au statut Évaluer ou Surveiller DOIT indiquer le signal 
qui déclenchera le réexamen de son statut et la date de sa dernière vérification. L’apparition du signal 
DOIT entraîner une révision extraordinaire de l’entrée, sans attendre l’échéance trimestrielle.
Pourquoi : l’admission d’un projet à l’AAIF ou la publication d’une RFC ne devrait pas attendre trois mois pour être 
prise en compte.
À RETENIR
Une fondation neutre n’est pas un statut au catalogue, et une annonce n’est pas une norme : un travail 
émergent n’entre en production que par le statut Adopter.
7 Orchestration
L’orchestration décide qui fait quoi, dans quel ordre, avec quel état et quelles garanties en cas d’échec. Ce 
chapitre fixe la règle de départ, soit la configuration la plus simple qui répond au besoin, puis les huit patrons 
autorisés et la façon de choisir parmi eux. Il impose enfin les mécanismes qui rendent une orchestration 
digne de la production : exécution durable, saga et compensation, idempotence, contexte minimal entre 
agents, résilience et coupe-circuit.
7.1 Commencer simple : ce que disent les données probantes
Cette section résume les mesures publiées sur les systèmes multiagents et en tire la règle de départ du cadre : 
un flux déterministe ou un agent unique bien outillé, sauf preuve mesurée du contraire.
Des gains réels, sur des tâches précises
Anthropic rapporte que son système de recherche multiagent, formé d’un agent principal Claude Opus 4 
et de sous-agents Claude Sonnet 4, a surpassé de 90,2 % un agent unique Claude Opus 4 sur son évaluation 
interne de recherche. Le gain est le plus marqué pour les requêtes « en largeur », qui poursuivent plusieurs 
pistes indépendantes à la fois; il s’agit d’une évaluation interne, et non d’un banc d’essai public[17].
L’étude de Google Research « Towards a Science of Scaling Agent Systems » (Kim, Liu et coll.) nuance 
fortement ce résultat. Selon le billet du 28 janvier 2026 (180 configurations, quatre bancs d’essai, cinq 
architectures, trois familles de modèles), l’architecture centralisée gagne 80,9 % sur une tâche parallélisable 
(Finance-Agent), alors que chaque variante multiagent dégrade la performance de 39 à 70 % sur une tâche 
séquentielle (PlanCraft)[273]. La version 3 de l’article (8 avril 2026; 260 configurations, six bancs d’essai) donne 
une plage de +80,8 % à −70,0 % et observe que les gains de la coordination diminuent lorsque l’agent unique 
est déjà performant[274].
Des coûts et des risques qui croissent avec le nombre d’agents
• Jetons. Selon Anthropic, un agent consomme environ 4 fois plus de jetons qu’une conversation, et un 
système multiagent environ 15 fois plus; sur le banc d’essai BrowseComp, le volume de jetons explique à 
lui seul 80 % de la variance de performance[17]. Un article d’Anthropic du 23 janvier 2026 situe le surcoût 
habituel du multiagent entre 3 et 10 fois les jetons d’un agent unique pour une tâche équivalente[275].
• Erreurs. Google Research mesure une amplification des erreurs pouvant atteindre 17,2 fois dans des 
systèmes multiagents indépendants, contre 4,4 fois lorsqu’un orchestrateur central sert de goulot de 
validation[273].
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 86 sur 283


---
## [Page PDF 87]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
• Cohérence. Cognition soutient qu’il faut partager le contexte complet (les traces de l’agent, pas de 
simples messages), car chaque action porte des décisions implicites; des sous-agents mal informés 
prennent des décisions contradictoires. Cette prise de position d’ingénierie recommande par défaut un 
agent linéaire à fil unique[276]. LangChain réconcilie les deux positions : le multiagent convient mieux 
aux tâches de lecture, faciles à paralléliser, qu’aux tâches d’écriture, où des écritures concurrentes se 
contredisent[277].
• Limites d’emploi. Anthropic juge que les tâches où tous les agents doivent partager le même contexte, 
ou qui comportent de nombreuses dépendances, conviennent mal au multiagent, et que le surcoût ne se 
justifie que si la valeur de la tâche le paie[17].
Une consigne convergente des éditeurs
Le Centre d’architecture Azure prescrit le niveau de complexité le plus bas qui répond au besoin de façon 
fiable : appel direct au modèle, puis agent unique doté d’outils, puis orchestration multiagent, seulement si 
l’agent unique échoue pour cause de complexité d’invite, de surcharge d’outils ou d’exigences de sécurité[9]. 
Anthropic recommande la solution la plus simple possible[65] et OpenAI, de maximiser d’abord les capacités 
d’un agent unique[66].
À RETENIR
Le multiagent est un outil de spécialiste, pas une architecture par défaut. Il rapporte surtout sur des 
tâches de lecture parallélisables et à forte valeur; il coûte de 3 à 10 fois plus de jetons et peut dégrader 
les tâches séquentielles. Le cadre exige donc une preuve mesurée avant d’ajouter des agents (PRIN-08).
EXIG-ORC-01 · DOIT
Configuration la plus simple justifiée
Chaque agent ou système d’agents DOIT inscrire à sa fiche (annexe B) pourquoi les options plus simples 
(code ou règle métier, appel direct au modèle, flux déterministe, agent unique outillé) ne répondent pas 
au besoin. La revue d’architecture DOIT refuser un patron dont la justification manque.
Pourquoi : chaque niveau de complexité ajoute coordination, latence et coût[9].
EXIG-ORC-02 · DOIT
Preuve mesurée avant le multiagent
Une topologie à plusieurs agents DOIT être comparée, sur le même jeu d’évaluation (section 10.4), à 
une base de référence à agent unique : taux de réussite, jetons par exécution, latence et coût par tâche 
réussie. Elle n’est retenue que si le gain de qualité ou de délai couvre le surcoût mesuré; la comparaison 
est versée à la fiche de l’agent, avec la grille d’homologation (annexe A).
Pourquoi : les gains publiés dépendent fortement de la tâche et le surcoût en jetons peut atteindre un ordre de 
grandeur[273, 275].
7.2 Patrons autorisés
Le cadre autorise huit patrons, combinables entre eux, et une variante encadrée (voir la figure 11 et le tableau 
24). Un patron décrit la topologie de la coordination; il ne fixe pas le niveau d’autonomie, qui se déclare 
séparément (chapitre 8).
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 87 sur 283


---
## [Page PDF 88]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
1 · Flux déterministe
code
agent
valide
code
Patron par défaut. Le code fixe
le chemin; le modèle traite les
étapes non structurées.
2 · Chaîne séquentielle
étape A
étape B
étape C
Sortie typée de A → entrée de B;
contrôle de schéma entre étapes
(points orangés).
3 · Routage et transfert
routeur
spécialiste 1
spécialiste 2
spécialiste 3
Qualifie l’intention puis cède la
session et le contexte utile;
le routeur se retire.
4 · Parallélisation
répart.
agent
agent
agent
fusion
Sectionnement (sous-tâches
indépendantes) ou vote; règle de
fusion explicite; coût × N.
5 · Orchestrateur et exécutants
orchestrateur
spéc. A
spéc. B
spéc. C
Plan dynamique, délégation A2A,
consolidation des artefacts;
deux niveaux au plus.
6 · Évaluateur-optimiseur
producteur
évaluateur
≤ 3 itérations
Vérificateur déterministe d’abord
(compilateur, règles), critique sur
un modèle distinct; puis escalade.
7 · Chorégraphie événementielle
bus d’événements (CloudEvents)
agent
agent
agent
agent
agent
Pas de chef d’orchestre; compteur
de sauts, trace et saga obligatoires.
8 · Agent unique outillé
raisonner
agir
observer
outil
outil
outil
Boucle ouverte bornée (étapes,
budget, délai); base de référence
avant tout multiagent.
Figure 11 — Huit patrons d’orchestration autorisés. Chaque vignette montre la topologie d’un patron et sa règle principale; les 
points orangés signalent un contrôle de schéma entre étapes. Les patrons se combinent : un flux déterministe peut contenir une étape 
orchestrée, qui publie à son tour un événement. Source : cadre CRE-IA-2026-01, d’après Anthropic (2024) et le Centre d’architecture 
Azure (2026).
Le catalogue s’appuie sur deux références de premier rang. Anthropic distingue les flux de travail, où le 
modèle et les outils suivent des chemins de code prédéfinis (enchaînement d’invites, routage, parallélisation, 
orchestrateur-travailleurs, évaluateur-optimiseur), des agents, où le modèle dirige lui-même son proces­
sus[65]. Le Centre d’architecture Azure décrit cinq orchestrations : séquentielle, concurrente, clavardage de 
groupe, transfert et magnétique[9]; la documentation de Microsoft Agent Framework indique que ce dernier 
patron est conçu à partir de Magentic-One, le système décrit par Fourney et coll.[278, 279]. Le cadre y ajoute la 
chorégraphie événementielle, absente des deux catalogues, et fait du flux déterministe à étapes agentiques 
le patron par défaut.
Tableau 24 — Huit patrons d’orchestration autorisés et variante encadrée
Patron
Fonctionnement
Quand l’utiliser
Point de vigilance
Correspondance
1. Flux déterministe
Un moteur de flux 
fixe l’ordre et les 
embranchements; 
certaines étapes 
appellent un mo­
dèle ou un agent 
borné pour traiter 
l’information non 
structurée.
Processus 
connus, régle­
mentés ou audi­
tés. Patron par 
défaut.
Rigide quand les 
cas varient beau­
coup; chaque étape 
agentique a un 
contrat de sortie vali­
dé.
Ajout du cadre; Anthropic : flux de 
travail.
2. Chaîne séquentielle
Chaque étape 
transforme la sor­
tie typée de la pré­
cédente.
Tâche décom­
posable en 
étapes fixes (ex­
traire, vérifier, 
rédiger).
Erreurs propagées et 
latences cumulées : 
validation de schéma 
et délai par étape.
Azure : séquentiel. Anthropic : en­
chaînement d’invites.
3. Routage et transfert 
(handoff)
Un routeur quali­
fie l’intention, puis 
cède la session et 
le contexte utile à 
un spécialiste dé­
claré; il se retire.
Triage, service 
à la clientèle 
par domaine, la­
tence prioritaire.
Liste fermée de des­
tinataires; le transfert 
porte le mandant, 
pas tout l’historique; 
aucun transfert en 
boucle.
Azure : transfert. Anthropic : rou­
tage. OpenAI : décentralisé.
4. Parallélisation
Un répartiteur 
lance des sous-
Analyse multi­
source, vérifi­
Jetons multipliés par 
le nombre de 
Azure : concurrent. Anthropic : pa­
rallélisation.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 88 sur 283


---
## [Page PDF 89]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Patron
Fonctionnement
Quand l’utiliser
Point de vigilance
Correspondance
tâches indépen­
dantes (section­
nement) ou la 
même tâche plu­
sieurs fois (vote), 
puis fusionne.
cation croisée, 
garde-fou exé­
cuté en parallèle 
de la tâche.
branches, pointes de 
charge; règle de fu­
sion explicite.
5. Orchestrateur et exé­
cutants
Un agent planifie 
dynamiquement, 
délègue à des 
spécialistes (A2A 
ou appel in­
terne), puis conso­
lide leurs artefacts.
Tâches ouvertes 
dont les sous-
tâches ne sont 
pas connues 
d’avance.
Coût et latence éle­
vés; l’orchestrateur 
est un point unique 
de défaillance; deux 
niveaux au plus.
Azure : magnétique (variante). An­
thropic : orchestrateur-travailleurs. 
OpenAI : gestionnaire.
6. Évaluateur-optimiseur
Un producteur 
propose; un éva­
luateur distinct 
juge selon des 
critères explicites 
et renvoie jusqu’à 
l’acceptation.
Qualité véri­
fiable : code, 
rédaction régle­
mentée, confor­
mité.
Trois itérations au 
plus, puis escalade; 
vérificateur qui dé­
clare victoire trop tôt.
Azure : boucle producteur-vérifi­
cateur. Anthropic : évaluateur-op­
timiseur.
7. Chorégraphie événe­
mentielle
Les agents ré­
agissent aux évé­
nements d’un bus 
et publient les 
leurs, sans chef 
d’orchestre.
Processus inter­
domaines fai­
blement cou­
plés, gros vo­
lumes, agents 
ambiants.
Vue d’ensemble diffi­
cile, risque de cycles : 
trace et compteur 
de sauts obliga­
toires; saga dès que 
des effets touchent 
plusieurs systèmes 
d’enregistrement.
Ajout du cadre; saga par choré­
graphie chez Microsoft.
8. Agent unique outillé
Un agent boucle 
seul « raisonner, 
agir, observer » 
avec ses outils, 
sous plafonds.
Requêtes va­
riées dans un 
même domaine; 
base de réfé­
rence avant tout 
multiagent.
Surcharge d’outils, 
contexte qui enfle; 
conditions d’arrêt 
obligatoires.
Azure : agent unique doté d’outils. 
Anthropic : agent.
Variante encadrée : cla­
vardage de groupe et 
débat
Plusieurs agents 
échangent dans 
un fil commun, 
sous un gestion­
naire qui donne la 
parole.
Décisions où un 
contre-examen 
vaut plus que la 
latence.
Trois agents au plus, 
plafond de tours; 
propagation d’idées 
entre agents.
Azure : clavardage de groupe.
Patron et autonomie sont deux dimensions distinctes : un système multiagent peut combiner des agents de 
niveaux différents[83]. Un orchestrateur plafonné à N3 peut ainsi déléguer à un exécutant plafonné à N1, et 
chaque action reste soumise à la règle la plus stricte entre le niveau de l’agent qui agit et le palier de l’outil 
appelé (section 8.4).
Règles propres à certains patrons
Orchestrateur et exécutants. Le cadre limite la délégation à deux niveaux : l’orchestrateur, puis ses 
exécutants. Ce plafond est un choix du cadre, appuyé indirectement par la mesure d’amplification des erreurs 
de Google Research. Salesforce impose une contrainte équivalente, dans un produit précis : l’orchestration 
multiorganisation d’Agentforce n’admet qu’un seul niveau de délégation (agent A vers agent B, jamais A 
vers B vers C), soit deux agents en chaîne comme dans le cadre[49]. Il s’agit d’une contrainte de produit, et 
non d’une règle générale.
Évaluateur-optimiseur. Microsoft exige un plafond d’itérations, des critères d’acceptation clairs et un 
comportement de repli défini, comme l’escalade vers un humain[9]; la valeur de trois itérations est un choix 
du cadre. Anthropic décrit l’écueil de la « victoire prématurée » : un sous-agent vérificateur exécute quelques 
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 89 sur 283


---
## [Page PDF 90]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
tests et déclare le succès. Les parades sont des critères concrets, des vérifications exhaustives et des tests 
négatifs[275].
Clavardage de groupe et débat. Microsoft recommande de limiter le clavardage de groupe à trois agents[9]. 
Une prépublication d’août 2026 (« Mind Viruses », Papadopoulos et coll., Anthropic Fellows Program et 
EPFL) montre que des idées ou des objectifs peuvent se propager d’agent en agent, dans une petite équipe 
d’agents de programmation et dans une chaîne d’agents dont le contexte est effacé entre les sessions. Un bref 
avertissement dans l’invite système y a conféré une immunité « quasi totale », mais la propagation varie 
selon le modèle, les consignes initiales et la topologie, et les auteurs jugent le risque réel mais actuellement 
limité[280]. Le cadre admet cet avertissement comme mesure complémentaire peu coûteuse, jamais comme 
contrôle suffisant.
Parallélisation. Le patron réduit le temps total, au prix de pointes de consommation lorsque plusieurs 
agents appellent les modèles en même temps, et il exige une logique de résolution des conflits[9]. Anthropic 
rapporte que la parallélisation des sous-agents et des appels d’outils a réduit jusqu’à 90 % le temps de 
recherche pour les requêtes complexes[17].
Chorégraphie événementielle. Pour une saga, la chorégraphie évite tout point unique de défaillance, 
mais elle complique le suivi et les tests d’intégration et expose à des dépendances cycliques[67]. Les contrôles 
d’enveloppe (trace, compteur de sauts, file de lettres mortes) relèvent de la section 6.7.
EXIG-ORC-03 · DOIT
Patron déclaré au registre
Chaque système d’agents DOIT déclarer à sa fiche et au registre (section 11.4) le patron retenu parmi 
ceux du tableau 24, ou leur combinaison, accompagné d’un schéma de ses flux. Toute autre topologie 
exige une dérogation (section 11.6).
Pourquoi : un patron connu se revoit, se teste et se compare; une topologie improvisée ne se gouverne pas.
EXIG-ORC-04 · NE DOIT PAS
Délégation limitée à deux niveaux
Une chaîne de délégation NE DOIT PAS dépasser deux niveaux (orchestrateur, puis exécutant) : un 
exécutant ne délègue pas à son tour à un autre agent sans dérogation. Le serveur d’autorisation, lors de 
l’échange de jetons (EXIG-IAM-08, section 9.3), et la passerelle d’agents DOIVENT vérifier la profon­
deur par l’imbrication de la réclamation act du jeton délégué et rejeter toute délégation excédentaire.
Pourquoi : choix du cadre; la coordination multiagent alourdit la communication et, sans validation centrale, amplifie 
les erreurs[273]; l’article mesure en outre un surcoût en jetons et davantage de tours de raisonnement[274].
EXIG-ORC-05 · DOIT
Boucle évaluateur-optimiseur bornée
Une boucle évaluateur-optimiseur DOIT déclarer des critères d’acceptation vérifiables, exécuter 
d’abord les vérifications déterministes disponibles (compilation, tests, moteur de règles), confier 
l’évaluation à un modèle ou à une invite distincts de ceux du producteur et s’arrêter après trois itérations 
au plus. Au plafond, la tâche passe en escalade humaine avec la dernière version et les critiques reçues.
Pourquoi : Microsoft exige un plafond, des critères clairs et un repli défini; la valeur de trois est un choix du cadre[9].
EXIG-ORC-06 · DOIT
Clavardage de groupe encadré
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 90 sur 283


---
## [Page PDF 91]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Le clavardage de groupe ou le débat entre agents DOIT réunir trois agents participants au plus, sous 
un gestionnaire (hors décompte des trois participants) qui attribue la parole, avec un plafond de tours 
et une règle de clôture déclarés. Le maillage libre, où chaque agent sollicite les autres sans plafond, NE 
DOIT PAS être utilisé.
Pourquoi : Microsoft recommande de limiter le clavardage de groupe à trois agents[9], et des idées peuvent se propager 
d’agent en agent[280].
EXIG-ORC-07 · DOIT
Fusion déclarée et écrivain unique en parallèle
Un patron de parallélisation DOIT déclarer avant l’exécution sa règle de fusion (déterministe, vote 
ou arbitrage) et sa limite de concurrence. Les branches DOIVENT se limiter à lire et à produire des 
artefacts; un seul composant DOIT écrire le résultat final dans un système d’enregistrement.
Pourquoi : des écritures concurrentes se contredisent[277].
EXIG-ORC-08 · DOIT
Chorégraphie sous propriétaire et saga
Une chorégraphie événementielle qui produit des effets dans plusieurs systèmes d’enregistrement 
DOIT avoir un propriétaire de bout en bout inscrit au registre, une saga explicite (section 7.5) et les 
contrôles d’enveloppe de la section 6.7.
Pourquoi : sans chef d’orchestre, personne ne voit le processus entier ni ne répond de son issue.
7.3 Choisir le patron
Le choix du patron suit l’arbre de décision de la figure 12, qui part toujours de l’option la plus simple. Il se 
documente à la fiche de l’agent et se révise lorsque les mesures de production contredisent l’hypothèse de 
départ.
Une règle métier ou un
seul appel d’outil suffit?
NON
OUI
Pas d’agent
code, règle ou appel direct
Les étapes sont-elles
connues d’avance?
OUI
Flux déterministe
étapes agentiques bornées
NON
Déclenchement par une
personne ou un événement?
événement
Chorégraphie
événementielle
personne
Un spécialiste unique suffit
après qualification?
OUI
Routage et transfert
l’agent de tête se retire
NON
Un agent unique, outils bien
décrits, contexte non saturé,
suffit-il?
OUI
Agent unique
recherche d’outils si nécessaire
NON
Orchestrateur et exécutants
2 niveaux au plus · parallèle si possible
À combiner avec tout patron
La qualité se vérifie? → boucle évaluateur-optimiseur (≤ 3 itérations).
Sous-tâches indépendantes? → parallélisation (sectionnement ou vote).
Par défaut, retenir l’option la plus simple qui répond au besoin; passer au multiagent seulement sur preuve mesurée de gain.
Figure 12 — Arbre de décision du patron d’orchestration. Les questions se lisent de haut en bas; la première réponse qui conclut 
fixe le patron. Les encadrés du bas s’ajoutent à n’importe quel patron lorsque la qualité se vérifie ou que des sous-tâches sont 
indépendantes. Source : cadre CRE-IA-2026-01, d’après le Centre d’architecture Azure (niveaux de complexité) et Anthropic.
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 91 sur 283


---
## [Page PDF 92]

CRE-IA-2026-01 · Cadre de référence
7 Orchestration
Quand le multiagent se justifie
Anthropic retient trois cas où plusieurs agents surpassent un agent unique : la protection du contexte (une 
sous-tâche produit une exploration volumineuse qui polluerait le contexte principal), la parallélisation 
(des pistes réellement indépendantes) et la spécialisation (des outils ou des consignes incompatibles dans 
un même agent)[275]. Microsoft ajoute les frontières de sécurité distinctes : deux domaines qui ne doivent 
pas partager les mêmes droits justifient deux agents[9]. L’effort doit aussi suivre la complexité : Anthropic 
emploie un agent et de 3 à 10 appels d’outils pour une recherche factuelle simple, de 2 à 4 sous-agents pour 
une comparaison, et davantage pour une recherche complexe[17].
Surcharge d’outils : mesurer avant de scinder
Aucune source ne fixe de seuil unique. OpenAI suggère, à titre indicatif, de viser moins de 20 fonctions 
disponibles au début d’un tour[115] et souligne que le chevauchement compte plus que le nombre : certaines 
mises en œuvre gèrent avec succès plus de 15 outils distincts, d’autres peinent avec moins de 10 outils qui se 
chevauchent[66]. La documentation d’Anthropic situe la dégradation au-delà de 30 à 50 outils disponibles[281]. 
Avant de multiplier les agents, deux leviers moins coûteux existent : consolider les outils en opérations 
orientées tâche, regroupées sous des espaces de noms[114], et charger les définitions d’outils à la demande. 
Selon Anthropic, sa recherche d’outils réduit de 85 % la consommation de jetons de contexte dans son 
exemple chiffré et fait passer la précision, sur ses évaluations internes de MCP, de 49 à 74 % (Opus 4) et de 
79,5 à 88,1 % (Opus 4.5); ce sont des résultats déclarés par le fournisseur[205].
Découper par frontières de contexte
Quand plusieurs agents sont retenus, on découpe selon les frontières de contexte, et non selon le type de 
travail : une fonctionnalité et ses tests restent avec le même agent[275]. Par exemple, dans l’analyse d’un 
dossier de crédit, l’agent qui lit les états financiers calcule aussi les ratios qui en découlent; un agent distinct 
ne se justifie que pour un contexte isolable, comme la vérification des sanctions internationales, qui obéit à 
d’autres droits d’accès.
Tableau 25 — Critères comparés des principaux patrons
Critère
Flux déter­
ministe
Agent 
unique
Routage et 
transfert
Orchestrateur 
et exécutants
Évaluateur-optimiseur
Chorégra­
phie
Prévisibilité et 
auditabilité
Très élevée
Moyenne
Élevée
Moyenne
Élevée sur le résultat
Moyenne, 
émergente
Latence de 
bout en bout
Faible à 
moyenne
Variable selon 
les tours
Faible
Élevée; réduite 
si parallèle
Moyenne à élevée
Asynchrone
Profil de coût 
en jetons (re­
père)
Le plus bas
Environ 4 fois 
une conver­
sation
Cumul étape 
par étape
3 à 10 fois 
l’agent unique; 
pointes si pa­
rallèle
Croît avec les itérations
Croît avec les 
abonnés et 
les sauts
Tolérance à 
l’ambiguïté
Faible
Élevée dans 
un domaine
Moyenne
Très élevée
Moyenne
Moyenne
Ce qui borne la 
dérive
Le code
Plafonds et 
budget
Liste fermée 
de destina­
taires
Deux niveaux, 
budget, délais
Trois itérations
Compteur de 
sauts, lettres 
mortes
Les appréciations qualitatives du tableau 25 sont des repères du cadre. Les seuls ordres de grandeur retenus 
par le cadre sont ceux d’Anthropic (environ 4 fois et 15 fois une conversation; de 3 à 10 fois l’agent unique)
[17, 275] et les profils de Microsoft : coûts cumulés étape par étape pour les patrons séquentiel et de transfert, 
pointes pour le patron concurrent, coût le moins prévisible pour le patron magnétique[9]. Ces repères cèdent 
la place aux mesures de jetons par agent et par exécution dès qu’elles existent (section 10.6).
EXIG-ORC-09 · DOIT
Version 1.1 · 28 octobre 2026 · actualisation du 1er novembre 2026
Page 92 sur 283
