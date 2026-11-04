# Audit chunk_15 — pages 141-152

## Synthèse
Le chunk couvre la fin du § 9.7, le § 9.8 (chaîne d'approvisionnement, EXIG-SEC-18 à -22), le § 9.9 (équipe rouge, essais, exercices, EXIG-SEC-23 à -26) et le ch. 10 jusqu'au début du § 10.4 (OpenTelemetry, contenu, journal d'audit, EXIG-OBS-01 à -13). Les faits sur les spécifications sont précis et datés, et la plupart des choix du cadre sont étiquetés comme tels. Les trois défauts les plus graves : (1) EXIG-OBS-01/05 exige d'émettre la version épinglée v1.41.0, alors que le texte lui-même dit que les instrumentations n'émettent pas une version précise ([15-01]); (2) le chaînage d'audit ne détecte pas une troncature, et l'anonymisation exigée à l'échéance est incompatible avec un stockage inaltérable et chaîné ([15-27], [15-30]); (3) le palier 3 (juges et revue humaine, 100 % des traces en erreur) est irréalisable sous EXIG-OBS-07/08 et sous un échantillonnage en tête ([15-32], [15-33]).
Recouvrement : pour les p. 141-142 et 151-152, je ne retiens que les constats qui exigent aussi les p. 143-150 (EXIG-SEC-22 à -25, § 10.3).

## Constats

### [15-01] [BLOQUANT] EXIG-OBS-01/05 exige d'émettre une version que le texte déclare impossible à garantir
- **Axe** : A, C
- **Localisation** : § 10.1, p. 145 et 148. Texte : « L'épinglage ne dicte toutefois pas ce que les bibliothèques d'instrumentation émettent »; EXIG-OBS-01 : « DOIT émettre traces et métriques […] selon la version des conventions GenAI épinglée au catalogue (v1.41.0 »; EXIG-OBS-05 : « Un composant qui ne les produit pas NE DOIT PAS être homologué ».
- **Diagnostic** : le paragraphe précédent explique que, par défaut, les instrumentations émettent la v1.36.0 ou antérieure (v1.30.0 pour l'instrumentation Python d'OpenAI), et qu'avec `gen_ai_latest_experimental` elles émettent « la dernière version expérimentale prise en charge […] et non une version précise ». Aucun réglage ne garantit donc la v1.41.0. Or l'exigence normative impose l'émission « selon » la v1.41.0, et EXIG-OBS-05 interdit d'homologuer tout composant qui ne porte pas les attributs du tableau 41. Ces attributs incluent `gen_ai.provider.name` (v1.37.0+) et `gen_ai.agent.version` (v1.40.0+, d'après le texte). La couche de correspondance, présentée comme le remède, n'apparaît dans l'exigence qu'en lecture (« Tableaux de bord […] lisent »), pas comme moyen de conformité à l'émission.
- **Contre-exemple** : un agent instrumenté par opentelemetry-instrumentation-openai, réglage par défaut, émet `gen_ai.system` et pas `gen_ai.provider.name`. EXIG-OBS-05 interdit de l'homologuer. Avec l'opt-in, il peut émettre une version postérieure à v1.41.0 (p. ex. `cache_write` de la branche principale). Il n'est alors toujours pas conforme à « selon la v1.41.0 ». Aucun composant du marché ne satisfait la lettre de l'exigence.
- **Correctif proposé** : reformuler EXIG-OBS-01 ainsi : « émettre une version des conventions consignée au catalogue pour chaque composant (version et réglage `OTEL_SEMCONV_STABILITY_OPT_IN`), ramenée à la v1.41.0 par la couche de correspondance versionnée au collecteur ». Dans EXIG-OBS-05, vérifier les attributs après correspondance (à la sortie du collecteur), pas à l'émission.
- **Confiance** : vérifié dans le texte (contradiction interne); versions d'instrumentation à vérifier (source externe).

### [15-02] [MAJEUR] EXIG-SEC-18 : l'empreinte n'est définie que pour un outil MCP, alors que l'exigence vise aussi modèles, agents et compétences
- **Axe** : A, B
- **Localisation** : § 9.8, p. 141-142 (couture avec EXIG-SEC-25, p. 144) : « serveurs MCP, agents distants, compétences et modèles […] (nom, titre, description, icônes, schémas d'entrée et de sortie, annotations et _meta) ».
- **Diagnostic** : la liste des champs ne s'applique qu'à une définition d'outil MCP. Pour un modèle hébergé chez un fournisseur, la passerelle ne voit qu'un alias (`gen_ai.request.model`). Aucune empreinte n'est observable, et le modèle servi peut changer derrière l'alias. Pour une carte A2A ou une compétence, rien ne dit quels champs entrent dans l'empreinte. Aucune canonisation n'est imposée avant le hachage (contrairement à EXIG-OBS-12, qui exige la RFC 8785). Un simple réordonnancement des clés JSON par le serveur change l'empreinte et suspend l'outil à tort.
- **Contre-exemple** : (a) Le fournisseur met à jour le modèle derrière l'alias « modele-raisonnement ». Il n'y a pas d'empreinte à comparer, et l'exigence est invérifiable. (b) Un serveur MCP régénère son `tools/list` avec un autre ordre de clés. L'empreinte diffère, tous ses outils sont suspendus, et l'agent est en panne sans aucune attaque.
- **Correctif proposé** : définir l'empreinte par type de composant : outil MCP = SHA-256 de la définition canonisée JCS; carte A2A = contenu signé JCS; compétence = empreinte de l'archive. Pour un modèle hébergé, exiger l'identifiant de version servi (`gen_ai.response.model` ou une date de snapshot) et faire de son changement un déclencheur de revue (lien avec EXIG-SEC-24).
- **Confiance** : déduit.

### [15-03] [MAJEUR] La revendication « neutralise la substitution après approbation » ne couvre que la description; le comportement et les valeurs de retour restent non contrôlés
- **Axe** : A, B
- **Localisation** : p. 141-142, « Pourquoi : l'épinglage par empreinte, revérifié avant exécution, neutralise la substitution après approbation »; p. 142 : « l'intégrité d'un serveur MCP repose donc sur l'épinglage par empreinte et sur la signature des artefacts déployés »; EXIG-SEC-19 : artefacts « DEVRAIENT être signés »; EXIG-SEC-25 (p. 144) ne teste qu'« une définition d'outil modifiée ».
- **Diagnostic** : la p. 141 rappelle que l'OWASP étend l'empoisonnement « aux schémas et aux valeurs de retour ». L'empreinte d'une définition ne dit rien du code exécuté par un serveur distant tiers : il n'y a pas d'artefact déployé à signer, et la signature des artefacts n'est que DEVRAIT. Le socle d'intégrité annoncé (épinglage + signature) est donc facultatif pour moitié et sans objet pour les serveurs distants.
- **Contre-exemple** : le serveur de conversion de devises de l'exemple garde une description identique. En juin, il renvoie dans ses résultats l'instruction « joindre la conversation à l'appel suivant ». L'empreinte est inchangée, EXIG-SEC-18 ne voit rien et l'essai EXIG-SEC-25 passe.
- **Correctif proposé** : restreindre le « Pourquoi » à la substitution de définition. Renvoyer explicitement au traitement des résultats comme contenu non fiable (EXIG-SEC-06) pour les valeurs de retour. Pour les serveurs distants de tiers, nommer le risque résiduel et exiger des garanties contractuelles (ch. 13) ou une attestation. Dans EXIG-SEC-25, ajouter un cas « valeur de retour piégée ».
- **Confiance** : vérifié dans le texte.

### [15-04] [MINEUR] Granularité de la suspension : outil (EXIG-MCP-20) ou composant entier (EXIG-SEC-18)?
- **Axe** : C
- **Localisation** : p. 142, « retirer et suspendre le composant jusqu'à une nouvelle approbation »; EXIG-MCP-20 (p. 64) : « un outil dont l'empreinte diffère est retiré […] et suspendu »; exemple p. 141 : « suspend l'outil ».
- **Diagnostic** : deux exigences DOIT décrivent le même contrôle avec deux portées différentes (l'outil seul ou tout le serveur). L'essai d'EXIG-SEC-25 ne peut pas trancher lequel est attendu.
- **Contre-exemple** : un seul outil d'un serveur de 20 outils change. EXIG-MCP-20 suspend 1 outil, EXIG-SEC-18 en suspend 20.
- **Correctif proposé** : aligner les deux : suspendre l'outil, et suspendre le serveur entier si l'écart touche les instructions du serveur ou plusieurs outils (risque d'ombrage).
- **Confiance** : vérifié dans le texte.

### [15-05] [MAJEUR] EXIG-SEC-19 : vérifier « une signature valide » sans ancre de confiance ne prouve rien
- **Axe** : A
- **Localisation** : p. 142, « vérifier au moins une signature valide, faite avec une clé ni expirée ni révoquée, avant de faire confiance à la carte »; Pourquoi : « sans signature un agent malveillant peut publier une carte qui imite un agent légitime ».
- **Diagnostic** : la menace invoquée (imitation) n'est parée que si la clé est liée à l'identité de l'éditeur légitime : clé épinglée au catalogue, JWKS servi par le domaine de l'agent, chaîne X.509. L'exigence ne demande que validité cryptographique et non-révocation. Un imitateur signe sa fausse carte avec sa propre clé, valide et non révoquée.
- **Contre-exemple** : un attaquant publie une carte « agent-paie » signée avec une clé ES256 qu'il a générée la veille. La signature est valide et la clé ni expirée ni révoquée : EXIG-SEC-19 est satisfaite.
- **Correctif proposé** : « signature valide faite avec une clé inscrite au catalogue pour cet éditeur (ou publiée par le domaine de l'agent, avec liaison `kid`/`jku` vérifiée) ». Ajouter ce cas négatif (clé valide mais non inscrite) à EXIG-SEC-25.
- **Confiance** : déduit (portée exacte du mécanisme `jku` de la spécification A2A à vérifier).

### [15-06] [MINEUR] EXIG-SEC-21 : « absent du catalogue ou du registre », disjonction ambiguë
- **Axe** : C
- **Localisation** : p. 142, « Le trafic vers un serveur MCP ou un agent absent du catalogue ou du registre DOIT être bloqué »; couture avec EXIG-SEC-22 (p. 143, « Avant son inscription au catalogue »).
- **Diagnostic** : deux lectures sont possibles. (a) Serveur absent du catalogue / agent absent du registre. (b) Tout composant absent de l'un *ou* de l'autre. Dans la lecture (b), un serveur MCP, qui n'a pas sa place au registre des agents, est toujours bloqué.
- **Correctif proposé** : « tout serveur MCP absent du catalogue et tout agent absent du registre ».
- **Confiance** : vérifié dans le texte.

### [15-07] [MAJEUR] EXIG-SEC-22 : accord écrit exigé sans l'exception de l'art. 25(4) ni distinction de rôle, donc inapplicable aux composants libres
- **Axe** : A, B
- **Localisation** : p. 143. Texte : « sauf pour les tiers qui rendent publics, sous licence libre et ouverte, des outils […] autres que des modèles d'IA à usage général (art. 25(4)) »; EXIG-SEC-22 : « Lorsqu'un composant est intégré à un système à haut risque au sens du RIA, un accord écrit DOIT être conclu avec le tiers ».
- **Diagnostic** : le paragraphe cite l'exception pour le logiciel libre, mais l'exigence ne la reprend pas et n'est pas étiquetée « choix du cadre ». Pour un serveur MCP libre récupéré d'un dépôt public, il n'existe souvent aucune contrepartie avec qui signer : l'exigence est alors inexécutable. Par ailleurs, l'art. 25(4) vise le *fournisseur* du système à haut risque. Si l'entreprise n'est que déployeur, l'obligation légale ne lui incombe pas.
- **Contre-exemple** : un agent de crédit (annexe III) utilise un serveur MCP libre sous licence Apache-2.0, maintenu par des bénévoles. EXIG-SEC-22 exige un accord écrit impossible à obtenir, et l'agent ne peut pas être homologué alors que le RIA ne l'exige pas.
- **Correctif proposé** : reprendre l'exception de l'art. 25(4) et préciser « lorsque l'entreprise est fournisseur ». Pour les composants libres, remplacer l'accord par une évaluation renforcée et un plan de contingence. Si le cadre veut aller au-delà du RIA, l'étiqueter « choix du cadre ».
- **Confiance** : vérifié dans le texte; portée exacte de l'art. 25(4) modifié par le règlement (UE) 2026/1744 à vérifier par l'audit bibliographique.

### [15-08] [MINEUR] EXIG-SEC-22 : « proportionnée au palier de ses outils » n'a pas de sens pour un modèle
- **Axe** : C
- **Localisation** : p. 143, « tout serveur MCP, agent ou modèle fourni par un tiers DOIT faire l'objet d'une évaluation de sécurité proportionnée au palier de ses outils ».
- **Diagnostic** : un modèle n'a pas d'outils ni de palier, et un agent tiers expose des compétences A2A, pas des outils catalogués. L'exigence n'a pas de critère de proportion pour ces deux cas. Il faudrait se fonder sur la classe de risque des agents consommateurs.
- **Correctif proposé** : « proportionnée au palier le plus élevé des outils qu'il expose ou, pour un modèle ou un agent, à la classe de risque la plus élevée des agents qui l'utilisent ».
- **Confiance** : déduit.

### [15-09] [MAJEUR] Les agents de classe faible, seuls admis à N4, échappent à l'équipe rouge et à la nomenclature
- **Axe** : A (treillis T7)
- **Localisation** : EXIG-SEC-23, p. 143 : « Tout agent de classe de risque modérée ou élevée DOIT subir […] un exercice d'équipe rouge »; EXIG-SEC-20, p. 142 : « agent de risque modéré ou élevé »; EXIG-CON-02 : « N4 n'est permis qu'à un agent de classe faible ».
- **Diagnostic** : la condition ne porte que sur la classe et ignore le niveau d'autonomie. Or, d'après EXIG-CON-02, N4 (autodéclenchement, sans humain dans la boucle) n'existe *que* dans la classe faible. L'équipe rouge et la nomenclature exemptent donc précisément les agents les plus autonomes. Un agent faible N3/N4 qui lit du contenu non fiable reste exposé au détournement et à l'exfiltration (triade létale), indépendamment de sa classe d'impact.
- **Contre-exemple** : un agent ambiant N4 de classe faible lit les courriels entrants et classe des billets. Il n'a jamais d'équipe rouge ni de nomenclature. Une faille annoncée dans sa bibliothèque d'analyse ne permet pas de le retrouver (Pourquoi d'EXIG-SEC-20).
- **Correctif proposé** : étendre EXIG-SEC-23 et EXIG-SEC-20 à « toute classe modérée ou élevée, et tout agent de niveau N3 ou N4 ou qui consomme du contenu non fiable ».
- **Confiance** : vérifié dans le texte (EXIG-CON-02 confirmé dans full.txt).

### [15-10] [MAJEUR] EXIG-SEC-23 : échelle « critique » non définie, et rien n'est prévu pour un agent déjà en production
- **Axe** : B
- **Localisation** : p. 143, « Un constat de gravité critique non corrigé DOIT bloquer la mise en production ».
- **Diagnostic** : (a) Aucune échelle de gravité n'est définie pour les constats d'équipe rouge (je n'en trouve pas dans full.txt). Celle des incidents du tableau 61 est différente. (b) L'exercice annuel porte sur un agent *déjà* en production, et pour lui la conséquence d'un constat critique n'est pas définie (suspension? coupe-circuit? délai de correction?). L'exigence n'est contraignante qu'une fois, à la première mise en production.
- **Contre-exemple** : l'exercice annuel révèle une exfiltration par mémoire empoisonnée sur un agent de classe élevée en service. Le texte n'impose ni suspension ni délai, et l'agent continue d'opérer.
- **Correctif proposé** : renvoyer à une échelle nommée (p. ex. celle du § 12.8 ou CVSS adaptée). Ajouter : « en production, un constat critique DOIT entraîner la suspension ciblée (EXIG-ORC-28) ou une dérogation (§ 11.6) sous N jours ».
- **Confiance** : vérifié dans le texte (absence d'échelle : déduit de la recherche dans full.txt).

### [15-11] [MAJEUR] EXIG-SEC-24 : porte de déploiement statistiquement non spécifiée, seuil fixé par l'équipe elle-même, déclencheurs incomplets
- **Axe** : B
- **Localisation** : p. 144, « bloquer le déploiement si le taux de réussite des attaques dépasse le seuil fixé à la fiche de l'agent »; « (modèle, invite système, outil ou palier modifié) ».
- **Diagnostic** :
  1. Le taux de réussite d'une attaque sur un modèle non déterministe est une estimation. Sans nombre de répétitions ni intervalle de confiance, la porte oscille. Le § 10.4 reconnaît que « chaque scénario se répète », mais EXIG-SEC-24 n'en dit rien. Le cadre met lui-même en garde contre les taux « cités sans contexte » (p. 135).
  2. Le seuil est inscrit à la fiche (annexe B, « seuil de réussite maximale »), tenue par l'équipe qui veut déployer. Aucun plafond ni approbateur indépendant n'est prévu.
  3. Une suite figée s'use : les défenses s'ajustent aux attaques connues, sans attaque adaptative.
  4. Les déclencheurs omettent la version de protocole (que mentionne pourtant la figure 22) et le changement silencieux du modèle servi derrière un alias.
- **Contre-exemple** : une suite de 40 attaques, exécutée une fois, donne 2/40 = 5 % pour un seuil de 5 %, et le déploiement passe. Exécutée de nouveau, elle donne 4/40 et le bloque. Le fournisseur remplace ensuite le modèle derrière l'alias, et aucune exécution n'est déclenchée.
- **Correctif proposé** : fixer un nombre minimal de répétitions et une borne supérieure de confiance, p. ex. un intervalle de Wilson à 95 % sous le seuil. Faire approuver le seuil par la sécurité, avec un plafond par classe. Renouveler une part de la suite à chaque trimestre. Aligner les déclencheurs sur la figure 22 et y ajouter le changement de `gen_ai.response.model`.
- **Confiance** : vérifié dans le texte (points 1, 2, 4); déduit (point 3).

### [15-12] [MINEUR] EXIG-SEC-24 et palier 2 : deux portes d'injection sans articulation
- **Axe** : C
- **Localisation** : p. 144 (EXIG-SEC-24) et p. 152 (« tentatives d'injection en français et en anglais » dans le jeu de référence du palier 2).
- **Diagnostic** : les deux mécanismes mesurent la résistance à l'injection à chaque changement, avec des seuils différents (fiche « seuil de réussite maximale » et « seuils d'acceptation »). Le texte ne dit pas si ce sont les mêmes scénarios ni lequel prévaut.
- **Correctif proposé** : déclarer que la suite d'EXIG-SEC-24 est la composante adverse du palier 2 et qu'elle a un seuil unique.
- **Confiance** : vérifié dans le texte.

### [15-13] [MINEUR] EXIG-SEC-25 : la liste des cas négatifs omet des contrôles déterministes du même chapitre
- **Axe** : B
- **Localisation** : p. 144, « Les essais DOIVENT démontrer, par des cas négatifs, que : la passerelle retire […]; un jeton d'approbation altéré […]; un bac à sable […]; une définition d'outil modifiée est bloquée ».
- **Diagnostic** : les contrôles suivants sont aussi binaires et ne sont pas testés : refus d'une carte A2A non signée ou signée par une clé non inscrite (EXIG-SEC-19); blocage d'un serveur hors catalogue (EXIG-SEC-21); refus d'un élargissement de portée ou d'une audience erronée à l'échange de jetons (§ 9.3); blocage des plages privées et IPv6 (EXIG-SEC-12); refus en mode fermé (EXIG-IAM-18). Le « Pourquoi » justifie les tests par leur caractère binaire, ce qui vaut tout autant pour ces contrôles.
- **Correctif proposé** : compléter la liste ou renvoyer à une liste tenue en annexe A.
- **Confiance** : vérifié dans le texte.

### [15-14] [MAJEUR] EXIG-SEC-26 : « délai réel de révocation » sans point d'arrivée défini, structurellement hors cible pour les systèmes sans CAEP
- **Axe** : A, B
- **Localisation** : p. 144, « Le délai réel de révocation DOIT être mesuré et comparé à la cible de 15 minutes du tableau 61 ».
- **Diagnostic** : le texte ne dit pas où s'arrête la mesure : désactivation chez le fournisseur d'identité, dernier refus à la passerelle, ou dernier système raccordé qui cesse d'accepter un jeton déjà émis? EXIG-IAM-20 ne diffuse la révocation qu'« aux systèmes raccordés qui les prennent en charge ». Ailleurs, un jeton autoporté reste valide jusqu'à son expiration, et la durée de 15 minutes n'est que DEVRAIT, « lorsque le fournisseur d'identité le permet ». Le texte ne dit pas non plus si l'exercice se fait en production ou en préproduction (le délai n'est pas représentatif hors production), ni si un seul agent par trimestre suffit pour toute la plateforme.
- **Contre-exemple** : un SaaS tiers accepte des jetons d'une durée de 60 minutes et ne prend pas en charge CAEP. Le délai mesuré à la passerelle est de 2 minutes, conforme, alors que l'agent compromis peut agir dans le SaaS pendant 58 minutes de plus.
- **Correctif proposé** : définir la mesure comme le délai jusqu'au dernier refus effectif sur chaque système raccordé, en incluant la durée de vie résiduelle maximale des jetons émis. Exiger l'exercice en production (sur un agent témoin) et une rotation qui couvre chaque classe de risque.
- **Confiance** : vérifié dans le texte (EXIG-IAM-20 et durée des jetons confirmées dans full.txt).

### [15-15] [MINEUR] Cible de 15 minutes figée dans un DOIT alors qu'EXIG-IAM-20 la laisse à l'entreprise; trois exercices trimestriels qui se recouvrent
- **Axe** : C
- **Localisation** : p. 144, « comparé à la cible de 15 minutes du tableau 61 »; EXIG-IAM-20 : « Le délai maximal de bout en bout est fixé par l'entreprise »; tableau 61 : « cibles proposées », « que l'entreprise ajuste ».
- **Diagnostic** : EXIG-SEC-26 fait d'une cible proposée, que l'entreprise peut ajuster, une référence normative fixe. Par ailleurs, EXIG-ORC-28, EXIG-IAM-20 et EXIG-SEC-26 imposent chacune un exercice trimestriel de coupe-circuit avec mesure du délai. Le « PEUT se combiner » ne règle pas cette redondance.
- **Correctif proposé** : « comparé à la cible fixée par l'entreprise (proposée à 15 minutes au tableau 61) ». Fusionner les trois exigences en un seul exercice, en renvoyant des deux autres vers EXIG-SEC-26.
- **Confiance** : vérifié dans le texte.

### [15-16] [MINEUR] Épinglage de v1.41.0 alors que le texte désigne v1.41.1 comme dernière version en vigueur
- **Axe** : C
- **Localisation** : p. 145, « la dernière version publiée qui les contient comme conventions en vigueur est la v1.41.1 […] »; EXIG-OBS-01 : « (v1.41.0, jusqu'à l'homologation […]) ».
- **Diagnostic** : épingler la version mineure plutôt que son correctif n'est pas justifié. Le lecteur ne sait pas si v1.41.1 est admise (p. ex. sous la règle SemVer du § 6.8).
- **Correctif proposé** : épingler « v1.41.x (correctif v1.41.1 admis) », ou dire pourquoi v1.41.0 est retenue.
- **Confiance** : vérifié dans le texte.

### [15-17] [MAJEUR] EXIG-OBS-01/05 s'appliquent à des composants de tiers hors du contrôle de l'entreprise
- **Axe** : B
- **Localisation** : p. 145, « Tout composant d'une exécution d'agent (canal, orchestrateur, passerelles, agent, serveur MCP, consommateur d'événements) DOIT émettre […] vers le collecteur de la plateforme ».
- **Diagnostic** : un serveur MCP distant d'un éditeur SaaS ou un agent A2A partenaire n'émettra pas d'OTLP vers le collecteur de l'entreprise. EXIG-OBS-02 prévoit d'ailleurs de *redémarrer* la trace à cette frontière. Si on applique EXIG-OBS-05 (« NE DOIT PAS être homologué »), aucun serveur distant de tiers n'est homologable.
- **Contre-exemple** : un serveur MCP CRM hébergé par l'éditeur ne peut pas être homologué, faute de télémétrie émise vers l'entreprise. Si on ne l'exige pas de lui, il faut une dérogation pour chaque fournisseur.
- **Correctif proposé** : limiter l'obligation d'émission aux composants exploités par l'entreprise. Pour les tiers, exiger que la passerelle produise les spans CLIENT et les métriques, et prévoir des clauses contractuelles de télémétrie (ch. 13).
- **Confiance** : déduit.

### [15-18] [MINEUR] EXIG-OBS-02 : critère « interne » non défini, en tension avec la confiance zéro
- **Axe** : A, C
- **Localisation** : p. 146, « Un composant interne DOIT poursuivre la trace d'un autre composant interne »; paragraphe : « vient d'une source de confiance ».
- **Diagnostic** : le ch. 9 refuse la confiance implicite fondée sur la position réseau, mais rien ne dit comment un composant reconnaît que l'appelant est « interne » (identité SPIFFE? mTLS?). Si c'est le réseau qui en décide, cela contredit la confiance zéro.
- **Correctif proposé** : « interne = appelant authentifié par une identité de charge de travail inscrite au registre ».
- **Confiance** : déduit.

### [15-19] [MAJEUR] EXIG-OBS-04 : une attente d'approbation modélisée en span peut durer des heures ou des jours
- **Axe** : B
- **Localisation** : p. 147, « Attentes d'approbation, compensations et refus de la passerelle y figurent comme spans ou événements »; figure 21 : « attente d'approbation (INPUT_REQUIRED) », « ≈ 40 s ».
- **Diagnostic** : en N2, une approbation humaine peut prendre des heures ou des jours. Un span n'est exporté qu'à sa fin. Avec une exécution durable (§ 7.4), le processus qui l'a ouvert peut redémarrer : le span est alors perdu et la trace reste orpheline. Beaucoup de systèmes de stockage écartent aussi les spans très longs ou les traces qui s'étendent sur plusieurs jours. La figure, à environ 40 s, masque ce cas.
- **Contre-exemple** : une demande d'approbation est déposée un vendredi à 17 h et l'orchestrateur est redéployé pendant la fin de semaine. Le span d'attente n'est jamais exporté, et l'enquête ne voit pas l'attente.
- **Correctif proposé** : imposer pour les attentes un événement d'ouverture, un événement de fermeture et la reprise dans une nouvelle trace (ou un nouveau span) liée par un lien de span, plutôt qu'un span long.
- **Confiance** : déduit (comportement des SDK et des systèmes de stockage : à vérifier).

### [15-20] [MINEUR] EXIG-OBS-04 : « le span MCP CLIENT correspondant » pour tout outil
- **Axe** : C
- **Localisation** : p. 147, « execute_tool par appel d'outil avec le span MCP CLIENT correspondant ».
- **Diagnostic** : les outils qui ne passent pas par MCP (fonctions locales, API directes) n'ont pas de span MCP. Pris à la lettre, l'essai de conformité échoue.
- **Correctif proposé** : « et, pour un outil MCP, le span MCP CLIENT correspondant ».
- **Confiance** : vérifié dans le texte.

### [15-21] [MINEUR] Pseudonyme d'approbateur sur chaque span, contre la logique même d'EXIG-OBS-07
- **Axe** : C
- **Localisation** : tableau 41 (p. 148), « ca.entreprise.approval.approver […] Obligatoires; approbateur sous pseudonyme »; EXIG-OBS-06 : « un identifiant pseudonyme le demeure »; Pourquoi d'EXIG-OBS-07 : « la télémétrie est copiée vers plusieurs systèmes et lue par de nombreuses équipes ».
- **Diagnostic** : le cadre reconnaît que le pseudonyme est un RP et que la télémétrie est trop largement diffusée pour accueillir des RP. Il l'y rend pourtant obligatoire, alors que le journal d'audit le porte déjà.
- **Correctif proposé** : retirer l'approbateur des spans, garder `approbation_jti` comme clé de jonction et laisser l'approbateur au seul journal d'audit.
- **Confiance** : vérifié dans le texte.

### [15-22] [MAJEUR] EXIG-OBS-07 omet les messages d'exception, les descriptions de statut et les noms de spans
- **Axe** : B
- **Localisation** : p. 149, « NE DOIVENT PAS contenir le texte des invites, des réponses ou des instructions système, ni les arguments ou résultats d'outils ».
- **Diagnostic** : les fuites de contenu les plus courantes passent par `exception.message`/`exception.stacktrace`, la description du statut de span et les journaux applicatifs d'erreur. Une erreur de validation qui recopie l'argument fautif, ou une erreur du fournisseur qui cite l'invite, en sont des exemples. `error.type` est obligatoire (tableau 41), mais rien n'encadre le texte qui l'accompagne.
- **Contre-exemple** : un outil rejette « numéro d'assurance sociale 123-456-789 invalide » et l'exception est enregistrée sur le span. Un RP se retrouve dans la télémétrie de production sans violer la lettre d'EXIG-OBS-07.
- **Correctif proposé** : étendre l'interdiction aux messages et traces d'exception, aux descriptions de statut et aux noms de spans, et exiger la troncature ou le caviardage de ces champs au collecteur (EXIG-OBS-09).
- **Confiance** : déduit.

### [15-23] [MINEUR] EXIG-OBS-08 : destruction à 14 jours « au plus » sans réserve pour le gel des preuves; attribut de référence absent de la version épinglée
- **Axe** : C
- **Localisation** : p. 150, « Le contenu est détruit après 14 jours au plus »; p. 149 : référence « dont le format n'est pas normalisé dans la v1.41.0 ».
- **Diagnostic** : (a) EXIG-CON-10 réserve le gel des preuves d'incident (EXIG-CON-23), mais EXIG-OBS-08 est absolue : un diagnostic qui révèle un incident oblige à détruire la preuve. (b) Les attributs `*_ref` n'existant pas en v1.41.0, la référence doit être un attribut d'entreprise (EXIG-OBS-06), ce qui n'est pas dit.
- **Correctif proposé** : ajouter « sauf gel des preuves (EXIG-CON-23) ». Nommer l'attribut, p. ex. `ca.entreprise.content_ref`, en attendant les attributs `*_ref` de la convention.
- **Confiance** : vérifié dans le texte.

### [15-24] [MINEUR] EXIG-OBS-09 repose sur un processeur Alpha pour les journaux et métriques, et à la portée incertaine
- **Axe** : B
- **Localisation** : p. 149, « sa stabilité est Beta pour les traces, mais Alpha pour les métriques et les journaux »; EXIG-OBS-09 : « Toute télémétrie qui quitte la plateforme DOIT traverser un collecteur qui applique une liste d'autorisation fermée ».
- **Diagnostic** : le contrôle de sortie obligatoire pour les journaux et métriques repose sur un composant Alpha, sans mention du risque ni d'une solution de rechange. Je ne suis pas sûr que le processeur `redaction` traite les corps de journaux (où les conventions placent le contenu des événements), les attributs de ressource et les noms de spans.
- **Correctif proposé** : exiger un essai de non-fuite par type de signal, et une solution de rechange (p. ex. le processeur `transform`) là où le processeur `redaction` ne couvre pas un champ.
- **Confiance** : à vérifier (source externe : documentation du processeur redaction de opentelemetry-collector-contrib).

### [15-25] [MINEUR] EXIG-OBS-10 : filtrage du bagage limité à la passerelle; tracestate non filtré
- **Axe** : A
- **Localisation** : p. 150, « La passerelle DOIT retirer tout membre du bagage absent de la liste inscrite au catalogue ».
- **Diagnostic** : les appels internes qui ne traversent pas la passerelle (orchestrateur → consommateur d'événements, extension CloudEvents) propagent le bagage sans filtre. `tracestate`, visé par l'interdiction, n'a aucun mécanisme d'application.
- **Correctif proposé** : appliquer la liste au collecteur et aux SDK (propagateur filtrant), et préciser le traitement de `tracestate` aux frontières (EXIG-OBS-02).
- **Confiance** : déduit.

### [15-26] [MAJEUR] EXIG-OBS-11 n'audite pas les lectures P1 de données sensibles
- **Axe** : B
- **Localisation** : p. 151 (couture avec le § 10.3, p. 150), « Chaque action à effet (outil P2 ou P3) […] DOIT produire un enregistrement d'audit, sans échantillonnage ».
- **Diagnostic** : P1 couvre la « lecture interne ou sensible ». La question que pose le § 10.3 (« qui a fait quoi, au nom de qui ») vaut aussi pour la consultation de RP : c'est la première étape d'une exfiltration, et une enquête Loi 25 sur une atteinte doit pouvoir la reconstituer. Ces lectures ne laissent que des traces échantillonnées et purgeables.
- **Contre-exemple** : un agent détourné lit 5 000 dossiers clients (P1) puis exfiltre par un canal approuvé. Le journal d'audit ne montre aucune lecture, et l'étendue de l'atteinte ne peut pas être établie.
- **Correctif proposé** : auditer sans échantillonnage les appels P1 qui portent sur des RP ou des données classifiées, éventuellement sous forme agrégée par tâche.
- **Confiance** : déduit.

### [15-27] [MAJEUR] Chaînage d'audit : la troncature reste indétectable, « même flux » n'est pas défini, l'écriture concurrente n'est pas traitée
- **Axe** : A
- **Localisation** : p. 151, EXIG-OBS-12 : « porter l'empreinte de l'enregistrement précédent du même flux »; Pourquoi : « le chaînage rend toute suppression détectable ».
- **Diagnostic** : une chaîne de hachage détecte une suppression *au milieu*, mais pas la suppression des derniers enregistrements : la chaîne tronquée reste valide. Il faut un ancrage externe (tête signée publiée périodiquement, numéro de séquence vérifié contre un compteur indépendant). La notion de « flux » n'est définie nulle part : par agent, par tâche, par instance du service d'audit? Avec plusieurs écrivains concurrents, une chaîne linéaire impose de tout sérialiser, ce qui crée un goulot et un point unique de défaillance. Sinon, elle bifurque. Enfin, rien ne dit si `signature` est exclue du contenu haché et signé : l'extrait du § 10.3 la place au même niveau que les données, alors que l'annexe C.8 la met à part.
- **Contre-exemple** : un administrateur malveillant du magasin efface les 30 derniers enregistrements avant le scellement WORM du jour. La vérification quotidienne d'EXIG-OBS-13 parcourt une chaîne intacte et ne signale rien.
- **Correctif proposé** : définir le flux (p. ex. une chaîne par partition, avec un numéro de séquence). Publier chaque heure la tête de chaîne signée dans un système indépendant (ou dans un journal de transparence). Préciser que `empreinte` = SHA-256(JCS(enregistrement)), signature exclue, comme en C.8. Corriger le « Pourquoi » : « toute suppression ou modification antérieure à la dernière tête publiée ».
- **Confiance** : vérifié dans le texte (absence de définition de « flux » confirmée dans full.txt); le raisonnement cryptographique est déduit.

### [15-28] [MINEUR] Extrait du § 10.3 incohérent avec l'annexe C.8 et avec EXIG-OBS-12
- **Axe** : C
- **Localisation** : p. 150-151, extrait JSON (`"signature": "<signature du service d'audit>"` au même niveau que les données; `"autorite": { "approbation_jti": "…", "approbateur": "a-91c0…" }`; `"definition": "1.4.1"`).
- **Diagnostic** : (a) La signature est intégrée à l'objet, alors que C.8 la sépare de `enregistrement` et ajoute `empreinte` et `sequence`. (b) EXIG-OBS-12 exige l'empreinte d'approbation h, que l'extrait n'a pas (C.8 l'a : `empreinte_approbation`). (c) L'élément 5 prévoit « soit la règle qui permettait d'agir sans approbation », sans champ dans l'extrait (C.8 : `controle`, `version_politique`). (d) L'action consigne la *version* de la définition, alors qu'EXIG-SEC-18 épingle par *empreinte*. Une substitution sans changement de version n'est donc pas prouvable a posteriori.
- **Correctif proposé** : aligner l'extrait sur C.8 et ajouter `definition_sha256` à l'élément 3.
- **Confiance** : vérifié dans le texte.

### [15-29] [MINEUR] Empreinte SHA-256 nue d'arguments à faible entropie, alors qu'EXIG-OBS-09 exige un HMAC
- **Axe** : A, C
- **Localisation** : p. 151, « Les arguments d'outil n'y figurent que par leur empreinte SHA-256 »; EXIG-OBS-09 : « remplace les identifiants à faible entropie par un HMAC ».
- **Diagnostic** : des arguments comme {numéro de client, montant} s'énumèrent : le SHA-256 nu, conservé 24 mois, est réversible par dictionnaire et reste donc un RP. Le cadre exige un HMAC pour la télémétrie qui sort de la plateforme, mais pas pour le journal, conservé plus longtemps.
- **Correctif proposé** : soit HMAC à clé du service d'audit (h d'approbation recalculable par le même service), soit énoncer explicitement que l'empreinte est un RP pseudonymisé soumis au même régime que la table de correspondance.
- **Confiance** : déduit.

### [15-30] [MAJEUR] EXIG-OBS-13 : « détruit ou anonymisé » sur un stockage en ajout seul et chaîné
- **Axe** : A
- **Localisation** : p. 151, « stockage qui interdit modification et effacement avant échéance […] puis détruit ou anonymisé à l'échéance (EXIG-CON-10) ».
- **Diagnostic** : on ne peut pas anonymiser en place un enregistrement inaltérable, signé et chaîné sans invalider sa signature et toute la chaîne qui suit. Détruire les enregistrements les plus anciens supprime aussi l'origine de la chaîne, et la vérification quotidienne échoue ensuite, à moins qu'un point de reprise signé ne soit prévu.
- **Contre-exemple** : au mois 25, la purge des enregistrements du mois 1 fait échouer la vérification d'intégrité du lendemain. On désactive alors le contrôle ou on bloque la purge.
- **Correctif proposé** : anonymiser par la destruction des lignes de la table de correspondance des pseudonymes (déjà tenue à part), sans toucher aux enregistrements. Prévoir des points de reprise signés (tête de chaîne au début de chaque période) qui permettent de purger par segments entiers.
- **Confiance** : déduit.

### [15-31] [MINEUR] EXIG-EVT-10 renvoie à une rétention des traces « fixée au chapitre 10 » que ce chapitre ne fixe pas
- **Axe** : C
- **Localisation** : EXIG-EVT-10 (§ 6.7) : « sans excéder la rétention des traces et journaux d'audit fixée au chapitre 10 »; § 10.3, p. 150 : « Une trace est […] conservée selon la fiche de l'agent (section 12.2) ».
- **Diagnostic** : le ch. 10 ne fixe que la conservation de l'audit (24 mois) et celle du contenu de débogage (14 jours). Pour les traces, il renvoie à la fiche. Si la fiche fixe 90 jours pour un agent de classe élevée, EXIG-EVT-10 exige à la fois au moins un an et au plus 90 jours.
- **Correctif proposé** : renvoyer à la fiche (annexe B) et imposer que la rétention des traces soit au moins égale à la fenêtre d'enquête d'EXIG-EVT-10.
- **Confiance** : vérifié dans le texte.

### [15-32] [MAJEUR] Palier 3 : « 100 % des traces en erreur » est incompatible avec un échantillonnage en tête, dont le cadre ne dit rien
- **Axe** : B
- **Localisation** : p. 150, « Une trace est technique, souvent échantillonnée »; p. 152 (figure 22) : « 100 % des traces en erreur, relance ou refus d'approbation »; EXIG-OBS-05 : « un attribut obligatoire manquant en production DOIT déclencher une alerte ».
- **Diagnostic** : une décision d'échantillonnage prise en tête, au début de la trace, ne sait pas encore si la trace échouera. Garder 100 % des erreurs exige un échantillonnage en queue au collecteur, avec une mémoire tampon par trace et la contrainte que tous les spans d'une trace aboutissent à la même instance. Cette contrainte de capacité et de routage n'est ni exigée ni chiffrée. De même, l'alerte d'EXIG-OBS-05 ne voit que les traces conservées.
- **Contre-exemple** : avec un échantillonnage en tête de 10 %, 90 % des traces en erreur ne parviennent jamais au palier 3, et l'objectif de 100 % est atteint en apparence sur un sous-ensemble biaisé.
- **Correctif proposé** : exiger un échantillonnage en queue (ou aucun échantillonnage pour les spans d'erreur et de refus). Dimensionner le collecteur en conséquence, avec un équilibrage par `trace_id`. Mesurer les attributs manquants avant l'échantillonnage.
- **Confiance** : déduit.

### [15-33] [MAJEUR] Palier 3 : juges et revue humaine impossibles sous EXIG-OBS-07/08
- **Axe** : A, B
- **Localisation** : EXIG-OBS-07 (p. 149) : « En production, les spans, événements et journaux de télémétrie NE DOIVENT PAS contenir le texte des invites, des réponses »; EXIG-OBS-08 : capture « activée par une décision documentée […] période bornée »; p. 152 : « On évalue de 5 à 10 % des traces […] par des juges automatisés hors du chemin critique et par une revue humaine ».
- **Diagnostic** : un juge qui mesure l'ancrage factuel ou la justesse d'une réponse a besoin du texte de l'invite, de la réponse et des résultats d'outils. Un juge « hors du chemin critique » lit nécessairement une source persistée. Or la trace n'en contient pas (EXIG-OBS-07), et le dépôt de débogage n'est alimenté que ponctuellement, sur décision et pour une période bornée (EXIG-OBS-08). Le texte ne nomme aucune autre source, et une revue humaine des seules métadonnées ne permet pas de juger la qualité.
- **Contre-exemple** : pour se conformer au palier 3, l'équipe active en permanence la capture d'EXIG-OBS-08 « pour diagnostic ». Elle contourne ainsi la décision bornée et les 14 jours deviennent une capture continue, ou bien elle renonce au palier 3.
- **Correctif proposé** : créer une troisième voie explicite : un dépôt d'évaluation où un échantillon de 5 à 10 % est caviardé, chiffré et conservé brièvement, avec une finalité d'évaluation déclarée (Loi 25, section 12.2), un accès restreint aux juges et réviseurs et une référence sur le span. Sinon, exécuter les juges en ligne de façon asynchrone, sur le contenu en mémoire, sans le persister.
- **Confiance** : vérifié dans le texte (absence d'une source de contenu pour le palier 3 : déduit).

## Points forts
Les faits techniques sont précis et datés : en-tête `traceparent` de 55 caractères, 32 membres de `tracestate`, versions des conventions, niveaux Requis/Recommandé du tableau 41, et l'absence de valeur « handoff » corrige une idée reçue.
La séparation entre trace et journal d'audit, l'enregistrement à cinq éléments canonisé JCS et lié à l'empreinte d'approbation h, ainsi que l'interdiction d'une idempotence fondée sur `traceparent` sont solides.
La distinction entre obligation externe et « choix du cadre » est tenue presque partout (NIST d'usage volontaire, art. 12 du RIA sans signature, 24 mois au-delà des six mois de l'art. 26(6)).

## Questions pour l'audit bibliographique
- p. 141 : `kubernetes-sigs/agent-sandbox` relève-t-il de SIG Apps, et ses ressources Sandbox, SandboxTemplate, SandboxWarmPool et SandboxClaim sont-elles en `v1beta1` (et non en `v1alpha1`)? [137]
- p. 141 : la date du 1er avril 2025 du billet d'Invariant Labs sur l'empoisonnement d'outil et la substitution après approbation [220].
- p. 141 : la numérotation du MCP Top 10 de l'OWASP (MCP03 empoisonnement, MCP04 chaîne d'approvisionnement, MCP09 serveurs fantômes) [222] et celle de l'AST10 (AST01, AST02, AST07) [374].
- p. 141 : Hou et coll. décrivent-ils bien quatre phases (création, déploiement, exploitation, maintenance) et 16 scénarios répartis entre quatre types d'attaquants? Une version antérieure de l'article comptait trois phases (création, exploitation, mise à jour). Préciser la version citée [224].
- p. 142 : l'exclusion du champ `signatures` du contenu signé JCS et la règle « au moins une signature » de la spécification A2A 1.0 [68]; le mécanisme de liaison de la clé (`jku`/`kid`) qu'elle prévoit.
- p. 142 : « ASI02 » recommande-t-il bien les noms pleinement qualifiés avec versions épinglées contre le typosquattage [28]?
- p. 143 : la portée de l'art. 25(4) du RIA après le règlement (UE) 2026/1744 [61, 375].
- p. 143 : la date du 27 juillet 2025 du guide de l'OWASP sur la sécurisation des applications agentiques (version 1.0) [377].
- p. 143 : l'existence et l'intitulé des techniques AML.T0110, AML.T0124 et AML.T0133 de MITRE ATLAS [352].
- p. 144 : le principe 11 de l'Énoncé de principes québécois et sa mention de l'IA agentique et des mécanismes d'arrêt d'urgence [379].
- p. 145 : les dates v1.41.0 (28 avril 2026), v1.41.1 (11 mai 2026) et v1.42.0 (12 juin 2026); le déplacement vers `semantic-conventions-genai`; la règle de stabilité « v1.36.0 ou antérieure par défaut »; l'instrumentation Python d'OpenAI à la v1.30.0 [119, 180, 381-385].
- p. 146 : MCP 2026-07-28 réserve-t-il bien `traceparent`, `tracestate` et `baggage` dans `_meta` [162]?
- p. 147-148 : `gen_ai.agent.version` ajouté en v1.40.0 [180]; `gen_ai.provider.name` qui remplace `gen_ai.system` en v1.37.0 [387]; les niveaux du tableau 41 (notamment `gen_ai.agent.*` « Conditionnels »); les valeurs de `gen_ai.operation.name` en v1.41.0, dont `invoke_workflow` [119, 120].
- p. 149 : v1.38.0 pour `gen_ai.tool.call.arguments`/`result` [391]; la variable `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` et ses quatre valeurs sur la branche principale [392]; la stabilité Beta/Alpha du processeur `redaction` et la couverture des corps de journaux [141]; le statut de W3C Baggage (recommandation candidate) [393].
- p. 150 : la date d'application du 2 décembre 2027 pour l'annexe III (art. 113 modifié) [394]; ISO/IEC 42001 A.6.2.8 [395].
- p. 152 : l'énoncé d'AutoGenBench sur la répétition et l'isolation [279]; le juge d'Anthropic qui rend un score de 0,0 à 1,0 et un verdict en un seul appel [17]; les attributs de `gen_ai.evaluation.result` [396].

audit_15.md : 33 constats (1 BLOQUANT, 16 MAJEUR, 16 MINEUR)
