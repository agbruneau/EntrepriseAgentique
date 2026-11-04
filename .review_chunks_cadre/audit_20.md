# Audit chunk_20 — pages 191-202

## Synthèse
Le chunk couvre la fin du § 13.2 (EXIG-APP-03 à -06), les dix clauses contractuelles (EXIG-APP-07 à -16), la grille du tableau 54 (EXIG-APP-17), le modèle de maturité (ch. 14) et le début de la feuille de route (§ 15.1, fig. 28, tableau 58). Les faits juridiques et les correspondances NIST et ISO sont soignés et le plus souvent exacts. Les défauts se concentrent sur la logique des règles. Les trois plus graves :
1. La grille du tableau 54 contredit les exigences qu'elle applique : la note 2 est « démontrée par le fournisseur », l'« échec » n'est pas défini et le statut éliminatoire ne suit pas les clauses DOIT.
2. La révocation par le fournisseur en 24 h (EXIG-APP-16) contredit le coupe-circuit immédiat (EXIG-APP-06) et la cible de 15 min (EXIG-IAM-20).
3. La feuille de route n'étend jamais la passerelle d'agents au palier P3, alors que l'approbation signée repose sur l'interception de l'appel P3 par la passerelle.

## Constats

### [20-01] [MAJEUR] Échelle de notation du tableau 54 incompatible avec EXIG-APP-03/-04; « échec » non défini
- **Axe** : A
- **Localisation** : § 13.4, p. 195-196 (couture avec p. 192) : « 2, démontré par le fournisseur; 3, démontré par un essai reproductible de l'entreprise »; « seuil d'admissibilité à 2,0, sans aucun échec à un critère éliminatoire ».
- **Diagnostic** : EXIG-APP-03 (DOIT) exige des essais reproductibles dans l'environnement de l'entreprise. EXIG-APP-04 interdit qu'une valeur du fournisseur serve de « critère de notation ». La grille accorde pourtant 2 à une démonstration du fournisseur, ce qui suffit à atteindre le seuil. Le texte ne dit pas non plus ce qu'est un « échec » à un critère éliminatoire : une note de 0, une note inférieure à 2 ou une note inférieure à 3. La décision d'écarter une offre (EXIG-APP-17) est donc indécidable.
- **Contre-exemple** : un fournisseur obtient 2 partout, sur la seule foi de ses démonstrations, sans rapport a2a-tck exécuté chez l'entreprise. Son score est 2,0, aucun 0 n'apparaît, et il est admissible malgré la violation d'EXIG-APP-03. La ligne « Performance mesurée » peut aussi recevoir 2 sur une démonstration du fournisseur, contre l'esprit d'EXIG-APP-04.
- **Correctif proposé** : définir l'échec éliminatoire comme une note inférieure à 3 pour les critères qu'une EXIG DOIT rattache à un essai de l'entreprise (interopérabilité, performance), et inférieure à 2 ailleurs. Plafonner à 1 la note d'un critère non vérifié par l'entreprise lorsque l'exigence impose un essai.
- **Confiance** : vérifié dans le texte.

### [20-02] [MAJEUR] Statut « éliminatoire » incohérent avec les clauses DOIT
- **Axe** : A / C
- **Localisation** : tableau 54, p. 196 : « Sécurité et chaîne d'approvisionnement … 15 Non »; « Réversibilité … 10 Non »; preuve « Clauses 3 à 6 acceptées ».
- **Diagnostic** : le § 13.3 présente les dix clauses comme des « exigences minimales » DOIT. Or la grille n'élimine que le refus des clauses 3 à 6 (ligne « Données »), et seulement au travers d'autres lignes pour les clauses 1, 2 et 10. Le refus de la clause 7 (audit, équipe rouge) ou de la clause 8 (réversibilité) ne fait que baisser le score. Le chapitre est pourtant fondé sur le risque de verrouillage (T1). De plus, « Coûts et FinOps » (poids 5) est éliminatoire, mais « Sécurité » (poids 15) ne l'est pas, sans justification.
- **Contre-exemple** : une offre qui refuse le droit d'audit et la restitution des mémoires obtient 0 sur ces deux lignes et 3 ailleurs. Son score vaut (75 × 3) / 100 = 2,25 : l'offre est admise sans dérogation, contre EXIG-APP-13 et EXIG-APP-14.
- **Correctif proposé** : rendre éliminatoire le refus de toute clause DOIT (ou exiger une dérogation, § 11.6), et rendre éliminatoires « Sécurité » et « Réversibilité », ou motiver qu'elles ne le soient pas.
- **Confiance** : vérifié dans le texte.

### [20-03] [MAJEUR] Critères éliminatoires inapplicables à une partie du périmètre d'acquisition
- **Axe** : B
- **Localisation** : tableau 54, p. 196 : « MCP 2026-07-28 et A2A 1.0 natifs … Oui ». Le périmètre du ch. 13 (p. 189) inclut « un service de modèles, … une passerelle, un serveur MCP ».
- **Diagnostic** : EXIG-APP-07 conditionne A2A à « toute délégation entre agents », mais EXIG-APP-03 et la ligne éliminatoire l'imposent sans condition. Un service de modèles ou un serveur MCP n'a pas de carte d'agent. Il ne peut pas produire de rapport a2a-tck et se trouve éliminé d'office. De même, l'« export FOCUS d'un mois de pilote », lui aussi éliminatoire, n'a pas de sens pour un serveur MCP libre et gratuit.
- **Contre-exemple** : l'acquisition d'un serveur MCP de connecteur ERP échoue au critère « Interopérabilité » faute d'A2A. Il faut une dérogation pour chaque acquisition de ce type.
- **Correctif proposé** : ajouter une colonne « applicable à » (plateforme, agent, service de modèles, passerelle, serveur MCP) et admettre « sans objet » avec justification, comme à l'annexe A.
- **Confiance** : vérifié dans le texte.

### [20-04] [MINEUR] Renvoi erroné : « plafonds par agent (EXIG-APP-05) »
- **Axe** : C
- **Localisation** : tableau 54, ligne « Coûts et FinOps », p. 196.
- **Diagnostic** : EXIG-APP-05 (p. 192) traite d'OTLP, de W3C Trace Context et de FOCUS. Elle ne mentionne aucun plafond. Les plafonds par agent relèvent d'EXIG-FIN-03 (« Unités SaaS converties et plafonnées ») et d'EXIG-FIN-05 (« Quotas et plafond mensuel par agent »).
- **Contre-exemple** : l'évaluateur qui suit le renvoi ne trouve pas le critère à noter.
- **Correctif proposé** : écrire « (EXIG-APP-05, EXIG-FIN-03, -05) ».
- **Confiance** : vérifié dans le texte.

### [20-05] [MINEUR] Rééquilibrage des poids : cas limites non traités
- **Axe** : A
- **Localisation** : § 13.4, p. 195 : « pour un agent de classe de risque élevée, le comité peut les rééquilibrer d'au plus 5 points par critère ».
- **Diagnostic** : les critères de poids 5 (« Coûts et FinOps », éliminatoire, et « Performance ») peuvent tomber à 0. Un critère de poids nul resterait-il éliminatoire? Par ailleurs, une acquisition vise souvent une plateforme qui porte des agents de plusieurs classes. Or la règle est formulée « pour un agent ».
- **Contre-exemple** : une plateforme destinée à des agents de classes faible et élevée : quelle pondération appliquer?
- **Correctif proposé** : fixer un poids plancher, par exemple 5, pour les critères éliminatoires, et rattacher le rééquilibrage à la classe la plus élevée des agents visés par l'acquisition.
- **Confiance** : vérifié dans le texte.

### [20-06] [MINEUR] « Trace de bout en bout » éliminatoire contre une exigence limitée aux sauts contrôlés
- **Axe** : A / B
- **Localisation** : p. 192 : EXIG-APP-05, « sur chaque saut qu'elle contrôle ». Tableau 54, p. 196 : « Trace de bout en bout produite pendant l'essai », critère éliminatoire.
- **Diagnostic** : un fournisseur conforme à EXIG-APP-05 peut s'appuyer sur des outils hébergés qu'il ne contrôle pas. C'est l'exemple de Microsoft Agent Framework (p. 191). Il ne produit alors pas de trace de bout en bout et se fait éliminer, bien qu'il respecte l'exigence.
- **Contre-exemple** : l'appel à un outil MCP hébergé par un tiers rompt la trace, et l'offre est écartée.
- **Correctif proposé** : aligner le critère et l'exigence : soit trace complète sur les sauts contrôlés et liste des ruptures, soit propagation exigée sur tous les sauts.
- **Confiance** : vérifié dans le texte.

### [20-07] [MAJEUR] Révocation par le fournisseur en 24 h contre coupe-circuit immédiat et cible de 15 min
- **Axe** : A
- **Localisation** : EXIG-APP-16, p. 195 : « à la fin du contrat ou à la suspension d'un agent, la révocation par le fournisseur, dans un délai fixé (cible du cadre : 24 heures) ». À comparer avec EXIG-APP-06, p. 192 : « sans attendre une intervention du fournisseur », et avec § 15.3 et EXIG-IAM-20 : « La cible proposée de 15 minutes pour la révocation ».
- **Diagnostic** : à la suspension, les jetons, consentements OAuth et webhooks détenus par le fournisseur restent valides jusqu'à 24 h. Le coupe-circuit de l'entreprise ne couvre que les systèmes qui prennent en charge CAEP. La clause confond aussi suspension (réversible) et révocation (définitive) : révoquer toutes les identités à chaque suspension rend celle-ci irréversible. Enfin, l'« essai de révocation chronométré » du tableau 54 et le « délai de révocation … sous la cible » du tableau 55 (niveau 4) ne disent pas laquelle des deux cibles s'applique.
- **Contre-exemple** : un agent compromis est suspendu. Pendant 24 h, un webhook côté fournisseur continue de déclencher des actions et un consentement OAuth donne encore accès à la messagerie.
- **Correctif proposé** : à la suspension, exiger l'invalidation côté fournisseur dans le délai d'EXIG-IAM-20 (cible de 15 min), réceptrice CAEP comprise. Garder 24 h pour la seule révocation de fin de contrat. Désigner la cible dans les tableaux 54 et 55.
- **Confiance** : vérifié dans le texte.

### [20-08] [MINEUR] Révocation en 24 h à la fin du contrat contre transition de six mois
- **Axe** : A
- **Localisation** : EXIG-APP-16, p. 195 (« à la fin du contrat ») et EXIG-APP-14, p. 195 (« assistance pendant une période de transition (cible du cadre : six mois) »).
- **Diagnostic** : si la transition suit l'échéance, la révocation de toutes les identités en 24 h empêche d'exploiter les agents pendant la sortie.
- **Contre-exemple** : une migration progressive vers un nouveau fournisseur devient impossible au lendemain de l'échéance.
- **Correctif proposé** : faire courir le délai d'EXIG-APP-16 à compter de la fin de la période de transition, sauf en cas de résiliation pour faute ou d'incident.
- **Confiance** : déduit.

### [20-09] [MAJEUR] Obligations de conservation et de destruction contradictoires
- **Axe** : A
- **Localisation** : les clauses en conflit sont les suivantes :
  - EXIG-APP-09, p. 193 : « conserver ces renseignements au moins un an après la décision (art. 11) »;
  - EXIG-APP-10, p. 194 : « en interdire la conservation après son échéance »;
  - EXIG-APP-12, p. 194 : « préserver les preuves »;
  - EXIG-APP-14, p. 195 : « puis qu'il détruise les données ».
- **Diagnostic** : l'obligation de l'art. 11 incombe à l'entreprise, mais la clause 3 la fait porter par le fournisseur (« le fournisseur DOIT … conserver »). Si le contrat prend fin moins d'un an après une décision, le fournisseur doit à la fois conserver et détruire. De même, un incident en cours d'enquête à l'échéance oppose la préservation des preuves à la destruction attestée. Aucune règle de préséance ni de gel juridique (legal hold) n'est prévue.
- **Contre-exemple** : une décision est rendue le 1er mars et le contrat prend fin le 30 juin. EXIG-APP-09 impose de conserver jusqu'au 1er mars suivant, tandis qu'EXIG-APP-10 et EXIG-APP-14 imposent de détruire après la transition.
- **Correctif proposé** : transférer l'obligation de l'art. 11 à l'entreprise par la restitution d'EXIG-APP-14, puis autoriser la destruction. Prévoir une suspension de la destruction pendant une enquête ou un litige.
- **Confiance** : vérifié dans le texte (pour la portée de l'art. 11 : à vérifier).

### [20-10] [MINEUR] La clause 3 omet la révision humaine de l'art. 12.1 et le délai propre au fournisseur
- **Axe** : A
- **Localisation** : EXIG-APP-09, p. 193 : « fournir de quoi l'informer … et permettre de répondre aux demandes d'accès dans les 30 jours (art. 32) ».
- **Diagnostic** :
  - L'art. 12.1 accorde aussi le droit de présenter ses observations à un membre du personnel en mesure de réviser la décision. L'annexe A (A.5) l'exige, mais la clause ne demande pas au fournisseur de quoi reprendre ou neutraliser une décision.
  - Le fournisseur n'a aucun délai propre : s'il met 30 jours, l'entreprise ne peut plus respecter les siens.
- **Contre-exemple** : la demande d'accès arrive le jour 1 et l'export du fournisseur le jour 29. Il ne reste qu'un jour pour la réponse.
- **Correctif proposé** : ajouter le soutien à la révision et un délai de fourniture, par exemple 10 jours.
- **Confiance** : vérifié dans le texte; contenu de l'art. 12.1 à vérifier.

### [20-11] [MINEUR] Art. 17 : « interprétation » superflue et EFVP préalable omise
- **Axe** : A
- **Localisation** : EXIG-APP-11, p. 194 : « ce que le cadre interprète comme incluant une autre province ».
- **Diagnostic** : d'après mes connaissances, l'art. 17 vise toute communication « à l'extérieur du Québec », ce qui inclut les autres provinces par le texte lui-même. Présenter ce point comme une interprétation affaiblit l'obligation. La clause omet aussi que l'art. 17 subordonne la communication à une EFVP préalable, que seul le « Pourquoi » évoque.
- **Contre-exemple** : un fournisseur conteste la clause en la présentant comme un simple choix du cadre.
- **Correctif proposé** : supprimer l'incise et ajouter « après une EFVP concluant à une protection adéquate ».
- **Confiance** : à vérifier (texte de l'art. 17).

### [20-12] [MINEUR] Clause 6 : destinataire et objet de l'art. 18.3 imprécis
- **Axe** : A
- **Localisation** : EXIG-APP-12, p. 194 : « aviser l'entreprise sans délai ».
- **Diagnostic** : selon mes connaissances, l'art. 18.3 impose d'aviser la personne responsable de la protection des renseignements personnels de toute violation « ou tentative de violation » des obligations de confidentialité. La clause ne nomme ni ce destinataire ni les tentatives.
- **Contre-exemple** : une tentative d'exfiltration bloquée n'est pas notifiée, parce qu'elle ne « touche » pas les données.
- **Correctif proposé** : écrire « aviser sans délai le responsable de la protection des renseignements personnels de l'entreprise de toute violation ou tentative de violation ».
- **Confiance** : à vérifier (libellé de l'art. 18.3).

### [20-13] [MINEUR] Clause 7 : préavis de changement de modèle non vérifiable
- **Axe** : B
- **Localisation** : EXIG-APP-13, p. 194 : « un préavis écrit avant tout changement de modèle qui modifie le comportement d'un agent ».
- **Diagnostic** : le fournisseur juge seul si le comportement change, et aucun délai n'est fixé, contrairement aux clauses 5, 8 et 10. Le critère n'est ni testable ni opposable.
- **Contre-exemple** : une mise à jour silencieuse d'un alias de modèle est jugée « sans effet » par le fournisseur.
- **Correctif proposé** : exiger un préavis pour tout changement de version de modèle, avec une cible chiffrée, et réserver l'exception aux correctifs de sécurité urgents notifiés a posteriori.
- **Confiance** : vérifié dans le texte.

### [20-14] [MINEUR] Clause 9 : « chaque tiers » sans l'exemption des logiciels libres
- **Axe** : A
- **Localisation** : EXIG-APP-15, p. 195 : « le contrat avec chaque tiers … DOIT constituer l'accord écrit exigé par l'article 25(4) ».
- **Diagnostic** : l'exemption des composants sous licence libre et ouverte n'apparaît que dans le « Pourquoi ». Pour un composant libre, il n'existe souvent aucun contrat, et la DOIT est alors insatisfaisable. Les fournisseurs de modèles à usage général, eux non exemptés, n'offrent souvent que des conditions standard : la faisabilité n'est pas discutée.
- **Contre-exemple** : une bibliothèque libre intégrée à un agent relevant de l'annexe III bloque l'homologation.
- **Correctif proposé** : intégrer l'exemption au corps de l'exigence et prévoir une voie de repli (dérogation, documentation au titre de l'art. 53) pour les modèles à usage général.
- **Confiance** : vérifié dans le texte; portée de l'art. 25(4) à vérifier.

### [20-15] [MINEUR] Clause 1 : période de dépréciation A2A peut-être inexistante
- **Axe** : A
- **Localisation** : EXIG-APP-07, p. 193 : « maintenir une version de protocole dépréciée au moins pendant la période prévue par la spécification ».
- **Diagnostic** : la p. 191 chiffre la période pour MCP (12 mois ou 90 jours), pas pour A2A. Si A2A 1.0 ne fixe aucune durée, la clause est vide.
- **Contre-exemple** : un fournisseur retire A2A 0.3 du jour au lendemain en invoquant l'absence de période.
- **Correctif proposé** : fixer une cible du cadre, par exemple 12 mois, à défaut de période dans la spécification.
- **Confiance** : à vérifier (source externe).

### [20-16] [MINEUR] Clause 2 : « chaîne des acteurs » et portée des `act` imbriqués
- **Axe** : A
- **Localisation** : EXIG-APP-08, p. 193 : « dont la revendication act conserve la chaîne des acteurs »; « Pourquoi : sans chaîne de délégation, la passerelle ne peut pas appliquer l'intersection des droits ».
- **Diagnostic** : selon mes connaissances, la RFC 8693 (§ 4.1) déclare les acteurs antérieurs imbriqués « informational only » et exclus des décisions d'accès. Une intersection calculée sur toute la chaîne irait donc au-delà de la RFC. Si l'intersection ne porte que sur `sub` et l'`act` extérieur, le mot « chaîne » induit en erreur.
- **Contre-exemple** : une passerelle conforme à la RFC ignore un acteur intermédiaire aux droits réduits, et l'intersection attendue n'est pas appliquée.
- **Correctif proposé** : préciser que l'intersection porte sur `sub` et l'`act` extérieur, et que la chaîne imbriquée sert à l'audit; ou définir une règle propre au cadre, en la nommant comme telle.
- **Confiance** : à vérifier (RFC 8693, § 4.1).

### [20-17] [MINEUR] Clause 8 : liste de restitution incomplète
- **Axe** : A
- **Localisation** : EXIG-APP-14, p. 195. La liste énumère les mémoires, les graphes, les définitions, la configuration, les journaux et les traces.
- **Diagnostic** : la clause 4 cite comme données de l'entreprise les « plongements vectoriels ». La clause 8 omet aussi les index vectoriels, les jeux d'évaluation et les artefacts d'ajustement autorisés par écrit, ainsi que les jetons et les preuves d'approbation signés (§ 8.5).
- **Contre-exemple** : à la sortie, l'entreprise perd les jeux d'évaluation qui conditionnent l'homologation des agents migrés.
- **Correctif proposé** : compléter la liste.
- **Confiance** : vérifié dans le texte.

### [20-18] [MAJEUR] Critères de maturité non reproductibles
- **Axe** : B
- **Localisation** : § 14.2, p. 198 : « deux évaluateurs qui examinent les mêmes preuves aboutissent au même niveau ». Tableau 55 : « Premiers serveurs MCP », « équipe rouge régulière », « réutilisation mesurée ». P. 197 : « elles visent surtout les nouveaux agents et les pilotes ». Échantillonnage : « un échantillon d'agents de chaque classe ».
- **Diagnostic** : plusieurs critères sont non quantifiés. « Premiers » peut vouloir dire un seul serveur, « régulière » n'a pas de fréquence, « surtout » n'a pas de seuil. La taille de l'échantillon n'est pas fixée. La règle par défaut, « à défaut pour tous les agents en production », contredit aussi la portée « surtout les pilotes » du niveau 2. L'objectif de reproductibilité affirmé n'est donc pas atteignable.
- **Contre-exemple** : un évaluateur cote 2 en interopérabilité avec un serveur MCP; un autre cote 1 parce que les agents en production n'ont ni contrat ni épinglage.
- **Correctif proposé** : chiffrer chaque critère (seuil, fréquence, périmètre explicite) et fixer une règle d'échantillonnage, par exemple tous les agents de classe élevée et au moins 20 % des autres.
- **Confiance** : vérifié dans le texte.

### [20-19] [MINEUR] Cumul des niveaux et critères négatifs du niveau 1
- **Axe** : A
- **Localisation** : § 14.1, p. 196 (« les niveaux sont cumulatifs ») et § 14.2, p. 198 (« ses critères, et ceux du niveau inférieur, sont satisfaits »). Tableau 55, niveau 1 : « Clés d'API et comptes de service partagés ».
- **Diagnostic** : les « critères » du niveau 1 décrivent des carences. Lue à la lettre, la règle de cumul exige de « satisfaire » le partage de clés pour atteindre le niveau 2, qui l'interdit.
- **Contre-exemple** : la lecture littérale rend tout niveau 2 inatteignable.
- **Correctif proposé** : déclarer le niveau 1 comme niveau plancher, sans critères.
- **Confiance** : vérifié dans le texte.

### [20-20] [MAJEUR] Le recul de maturité ne retire pas l'autonomie déjà accordée
- **Axe** : A
- **Localisation** : § 14.2, p. 198 : « le recul d'une dimension est soumis au comité, qui peut reporter les hausses d'autonomie prévues ». P. 199 : « font de la maturité une condition de l'autonomie ». P. 198 : « Après le jalon 3, l'entreprise refait l'évaluation chaque année ».
- **Diagnostic** : si la maturité conditionne l'autonomie, la condition doit tenir en permanence, pas seulement au franchissement du jalon. Or le texte ne prévoit qu'un report facultatif des hausses, jamais le retour des agents sous le plafond correspondant. Avec une évaluation annuelle, un recul peut rester ignoré jusqu'à 12 mois.
- **Contre-exemple** : après le jalon 2, une équipe réintroduit une clé partagée, ce qui ramène la dimension identité au niveau 1. Les agents N3 interdomaines continuent d'opérer, et le comité peut ne rien décider.
- **Correctif proposé** : exiger que tout recul sous le niveau du dernier jalon ramène les agents concernés au plafond de la phase correspondante, sauf dérogation bornée, et qu'un indicateur continu (tableau 61) déclenche la réévaluation.
- **Confiance** : vérifié dans le texte.

### [20-21] [MAJEUR] Les dimensions de maturité ne couvrent ni l'autonomie et la supervision ni l'approvisionnement
- **Axe** : B
- **Localisation** : § 14.1, p. 196 : « Les cinq dimensions reprennent les piliers du cadre ». Le chapitre 8 (autonomie, approbation) et le chapitre 13 n'y figurent pas, et le tableau 55 ne mentionne ni approbation, ni agents ambiants, ni réversibilité contractuelle.
- **Diagnostic** : la maturité conditionne les hausses d'autonomie (p. 199), mais aucun critère ne mesure les contrôles dont ces hausses dépendent : approbation signée (T5), approbation machinale (§ 8.7), délégation de longue durée des agents ambiants. La réversibilité envers les fournisseurs (T1) n'est pas mesurée non plus.
- **Contre-exemple** : une entreprise atteint le niveau 3 sur les cinq dimensions sans que ses approbateurs soient formés ni que le taux d'approbation machinale soit suivi. Elle peut alors ouvrir N4 après le jalon 3.
- **Correctif proposé** : ajouter une dimension « Autonomie et supervision », ou intégrer ces critères à l'orchestration et à la gouvernance, et ajouter la réversibilité contractuelle à la gouvernance.
- **Confiance** : vérifié dans le texte.

### [20-22] [MINEUR] Autoévaluation annuelle « guidée par l'annexe A »
- **Axe** : C
- **Localisation** : § 14.2, p. 198 : « par autoévaluation guidée par l'annexe A »; « une déclaration d'équipe n'est pas une preuve ».
- **Diagnostic** : l'annexe A est une grille d'homologation par agent (p. 209). Elle ne contient pas les critères d'entreprise du tableau 55 (comité, catalogue, indicateurs trimestriels). Par ailleurs, une autoévaluation est en tension avec l'exclusion des déclarations d'équipe. Le texte ne dit pas non plus si les jalons J4 et J5 sont constatés sur autoévaluation.
- **Contre-exemple** : l'annexe A ne permet pas de coter la gouvernance au niveau 4.
- **Correctif proposé** : renvoyer aux tableaux 55 et 56, et exiger une évaluation conduite par l'architecture d'entreprise pour J4 et J5.
- **Confiance** : vérifié dans le texte.

### [20-23] [MINEUR] Évaluation initiale circulaire
- **Axe** : B
- **Localisation** : § 14.2, p. 198 : « Une première évaluation précède la phase Fondations et calibre les durées ». Les preuves admises sont tirées « du registre, des passerelles, des traces ».
- **Diagnostic** : avant la phase Fondations, le registre et les passerelles n'existent pas encore : l'évaluation donne 1 par construction. La p. 200 admet d'ailleurs que les agents non inventoriés se découvrent pendant les Fondations, donc après le calibrage.
- **Contre-exemple** : l'évaluation initiale ne peut pas prévoir les « dizaines d'agents non inventoriés » qui allongeront la phase.
- **Correctif proposé** : admettre, pour l'évaluation initiale seulement, une découverte outillée (journaux d'identité et de facturation, analyse du trafic sortant) et recalibrer au jalon 1.
- **Confiance** : vérifié dans le texte.

### [20-24] [MINEUR] Certification ISO/IEC 42001 placée tantôt au niveau 4, tantôt au niveau 5
- **Axe** : C
- **Localisation** : la figure 27 (p. 197) place « ISO/IEC 42001 » sous le niveau 4. La p. 201 parle de « la certification ISO/IEC 42001, que le modèle de maturité place à ce niveau (figure 27) », soit le niveau 4. En revanche, le tableau 56 (p. 199) range au niveau 5 un « certificat ISO/IEC 42001 », et le tableau 57 (p. 200) une « certification par tierce partie ». La p. 199 situe la « préparation » au niveau 4.
- **Diagnostic** : le niveau de la certification elle-même varie d'un endroit à l'autre.
- **Contre-exemple** : J5 (certificat) mesure-t-il le niveau 4 ou le niveau 5?
- **Correctif proposé** : écrire partout « préparation (niveau 4), certification (niveau 5) », et corriger la figure 27 et la p. 201.
- **Confiance** : vérifié dans le texte.

### [20-25] [MINEUR] Déclaration d'applicabilité : niveau 4 dans le texte, mais article 6.1.3 au niveau 3
- **Axe** : C
- **Localisation** : p. 199 : « La déclaration d'applicabilité … est un livrable de ce niveau » (niveau 4). Tableau 57, niveau 3 : « (6.1.2 à 6.1.4 …) ».
- **Diagnostic** : selon mes connaissances, c'est l'article 6.1.3 d'ISO/IEC 42001 (traitement des risques) qui exige la déclaration d'applicabilité. Le tableau 57 range cet article au niveau 3 et le texte la place au niveau 4.
- **Contre-exemple** : un évaluateur exige la déclaration d'applicabilité dès le niveau 3, selon le tableau 57.
- **Correctif proposé** : soit ne retenir que 6.1.2 et 6.1.4 au niveau 3, soit placer la déclaration d'applicabilité au niveau 3.
- **Confiance** : à vérifier (ISO/IEC 42001, art. 6.1.3).

### [20-26] [MAJEUR] La passerelle d'agents n'est jamais étendue au palier P3
- **Axe** : A
- **Localisation** : figure 28, p. 200 : « Pass. d'agents (P0, P1 puis P2) »; tableau 58, p. 201 : « Passerelle d'agents ouverte aux outils P0 et P1, puis P2 ». À comparer avec la figure 16 (§ 8.5) : « La passerelle intercepte l'appel P3, calcule l'empreinte de l'action ».
- **Diagnostic** : la vérification de l'approbation signée liée à l'action exacte suppose que la passerelle voie l'appel P3. Aucune phase ne l'ouvre au palier P3, alors que N2, qui peut déclencher du P3 après approbation, est permis dès la phase Plateforme. Ou bien les appels P3 passent hors de la passerelle, ce qui contredit T2, ou bien ils sont impossibles jusqu'à une date non précisée.
- **Contre-exemple** : en phase Plateforme, un agent N2 de paiement demande une action P3. Soit l'approbation est vérifiée ailleurs que dans la passerelle, sans empreinte calculée, soit l'action est bloquée sans que la feuille de route le dise.
- **Correctif proposé** : écrire « P0, P1, puis P2 et P3 (approbation signée) » dans la phase Plateforme, ou interdire explicitement le palier P3 jusqu'à un jalon nommé.
- **Confiance** : vérifié dans le texte.

### [20-27] [MINEUR] Plafond de phase relevé avant la mise en service des contrôles
- **Axe** : A
- **Localisation** : p. 200 : « l'autonomie accordée aux agents n'augmente qu'une fois ces contrôles en service ». Tableau 58 : en phase Plateforme, « N2 » est permis alors que l'« approbation humaine signée », le « moteur d'exécution durable » et la passerelle P2 sont des livrables de cette même phase.
- **Diagnostic** : le plafond N2 s'ouvre au jalon 1, avant ses propres contrôles. En pratique, la contrainte vient de l'homologation par agent (annexe A), pas du plafond de phase, mais le texte ne le dit pas.
- **Contre-exemple** : un lecteur conclut que N2 est permis au mois 3, sans approbation signée en service.
- **Correctif proposé** : préciser que le plafond de phase est une condition nécessaire, et que la hausse effective exige l'homologation (annexe A), donc des contrôles en service.
- **Confiance** : déduit.

### [20-28] [MAJEUR] Des obligations légales déjà en vigueur sont planifiées comme livrables de phase
- **Axe** : C / A
- **Localisation** : figure 28, p. 200 : « EFVP en cours » (Fondations) et « Art. 12.1, validation E-23 » (Plateforme). Tableau 58, p. 201 : « transparence envers les personnes, notamment pour les décisions visées par l'article 12.1 ». À comparer avec la p. 202 : « Les obligations déjà en vigueur, comme les articles 3.3, 12.1 et 17 … ne suivent pas le rythme des phases et ne souffrent aucune dérogation ».
- **Diagnostic** : la feuille de route laisse jusqu'à 9 mois pour se conformer à l'art. 12.1. La règle de progression 4 (p. 202) permet en outre une dérogation bornée pour un agent existant. Les deux contredisent l'interdiction de déroger aux obligations en vigueur. Les agents N0 ou existants qui rendent des décisions entièrement automatisées ne sont pas visés par le plafond N1 des Fondations.
- **Contre-exemple** : un flux N0 existant de refus de crédit automatisé reste sans avis au titre de l'art. 12.1 jusqu'au mois 9, en conformité apparente avec la feuille de route.
- **Correctif proposé** : sortir les art. 3.3, 12.1 et 17 des lignes de phase, inscrire « conformité immédiate des agents existants » en tête des Fondations, et exclure ces obligations de la règle de progression 4.
- **Confiance** : vérifié dans le texte.

### [20-29] [MINEUR] Condition N3 interdomaines : par agent (p. 199) ou par action (p. 202)
- **Axe** : C
- **Localisation** : p. 199 : « pour un agent dont tous les appels interdomaines passent déjà par la passerelle »; p. 202 : « les actions de cet agent hors de son domaine sont plafonnées à N2 ».
- **Diagnostic** : selon la p. 199, l'agent entier perd N3 dès qu'un de ses appels contourne la passerelle. Selon la p. 202, il garde N3 dans son domaine et seules ses actions externes sont plafonnées. L'annexe A (A.6, « Tous ») exige de son côté la passerelle pour tout appel interdomaines.
- **Contre-exemple** : un agent qui contourne la passerelle pour un seul appel est N2 selon la p. 199, et N3 dans son domaine selon la p. 202.
- **Correctif proposé** : unifier sur une seule règle et l'aligner sur l'annexe A.
- **Confiance** : vérifié dans le texte.

### [20-30] [MINEUR] « Domaine d'exploitation certifié » ambigu
- **Axe** : C
- **Localisation** : p. 199 et tableau 58 : « domaine d'exploitation certifié »; figure 28 : « N4 sur périmètre certifié ».
- **Diagnostic** : dans les mêmes pages, « certifié » désigne aussi la certification ISO/IEC 42001 (J5). Le lecteur peut croire que N4 attend le certificat (mois 48), alors qu'il est ouvert dès le jalon 3.
- **Contre-exemple** : un comité reporte N4 jusqu'à J5.
- **Correctif proposé** : écrire « ODD homologué par le comité (§ 8.1) » ou renvoyer explicitement à la définition.
- **Confiance** : déduit.

### [20-31] [MINEUR] La chorégraphie est comptée dans deux dimensions
- **Axe** : C
- **Localisation** : tableau 55. Le niveau 4 en interopérabilité comprend la « chorégraphie CloudEvents et AsyncAPI », et le niveau 5 en orchestration la « Chorégraphie interdomaines ».
- **Diagnostic** : la même capacité est cotée dans deux dimensions, à des niveaux différents. Comme le niveau global est un minimum, cette double prise en compte pèse deux fois.
- **Contre-exemple** : l'absence de chorégraphie bloque à la fois l'interopérabilité au niveau 4 et l'orchestration au niveau 5.
- **Correctif proposé** : réserver le format et le contrat (CloudEvents, AsyncAPI) à l'interopérabilité, et le patron d'exécution à l'orchestration.
- **Confiance** : vérifié dans le texte.

## Points forts
- Clauses juridiques précises et prudentes : la distinction entre choix du cadre et loi est explicite (art. 12.1, 18.3, 3.5), et l'absence de responsabilité « conjointe » est rappelée.
- Correspondances NIST AI RMF et ISO/IEC 42001 justes dans l'ensemble (GOVERN 1.6, 1.7 et 6.1, MANAGE 2.4, MEASURE 2.4 et 3.1; A.6.2.6, A.6.2.8, A.10). La distinction entre maturité de l'entreprise et autonomie d'un agent est bien posée.
- Les échéances externes sont datées indépendamment des phases (p. 202), ce qui protège contre l'allongement d'une phase.

## Questions pour l'audit bibliographique
- p. 195 et 202 : le règlement (UE) 2026/1744 modifie-t-il bien l'art. 25(4) et fixe-t-il le 2 décembre 2027 (annexe III) et le 2 août 2028 (annexe I)? Le texte EUR-Lex n'a pas été rouvert (H.5).
- p. 194 : l'avis du BSIF sur les incidents fixe-t-il un point de départ au délai de 24 h (constat, détermination de la gravité)? C'est ce que conteste « sans fixer le point de départ ».
- p. 193 : A2A 1.0 prévoit-il une période minimale de maintien des versions dépréciées (EXIG-APP-07)?
- p. 193 : RFC 8693, § 4.1, statut des revendications `act` imbriquées (« informational only »?).
- p. 199 : ISO/IEC 42001:2023, l'art. 6.1.3 exige-t-il la déclaration d'applicabilité? Les intitulés A.5, A.6.2.6, A.6.2.8 et A.10 sont-ils exacts? ISO/IEC 42006:2025 est-elle bien publiée?
- p. 193-194 : libellés des art. 11, 12.1, 17, 18.3 et 32 de la Loi sur le privé (conservation d'un an, droit d'observation, « extérieur du Québec », « tentative de violation », 30 jours).
- p. 194 : document fédéral [418] (stockage au Canada et compétence étrangère, aucun cas documenté) : titre et date.
- p. 198 : Feng, McDonald et Zhang [83] et Morris et al. [302] soutiennent-ils l'autonomie comme décision de conception et un niveau de déploiement inférieur au maximum possible?
- p. 199 : intitulés NIST AI RMF de MAP 3.5, MEASURE 2.7 et MANAGE 4.1, et absence de gabarit de profil (« does not prescribe profile templates »).
