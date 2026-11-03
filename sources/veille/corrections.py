"""Corrections de la relecture du 3 novembre 2026, appliquées au corps extrait.

Le corps de la Veille n'a pas de source éditable : il est relu dans l'édition d'origine
(construire_pdf.py, ORIGINE). Les errata du 29 octobre n'y corrigeaient que ce qui
tenait dans la ligne, le PDF étant retouché sur place; la recomposition lève cette
contrainte. Les corrections de la relecture du 3 novembre sont donc faites à leur
place, errata du 29 octobre laissés à l'annexe compris, et consignées au tableau
d'errata de l'annexe de novembre (actualisation-2026-11.html, « Relecture du
3 novembre 2026 »). Chaque correction s'appuie sur un fait que le document établit
déjà, au corps ou dans ses annexes.

Chaque correction remplace un passage qui doit figurer exactement le nombre de fois
indiqué (une, par défaut) : un passage absent ou ambigu arrête la composition.
"""
import re

ZWSP = '​'

# (passage d'origine, passage corrigé[, occurrences]), dans l'ordre du document
CORRECTIONS = [
    # mots-clés : MPP, ajouté à la section 4.8 le 15 août
    ('paiements agentiques ; AP2 ; x402 ;', 'paiements agentiques ; AP2 ; x402 ; MPP ;'),
    # sommaire, constat 2 (erratum 5 du 29 octobre, appliqué en entier)
    ('plus de 950 serveurs au répertoire [270] ; décompte <em>total</em> sans source primaire.',
     'plus de 950 serveurs au répertoire [270] ; décompte <em>total</em> établi par recomptage du '
     'registre officiel, 21 767 enregistrements au 15 août (6.3).'),
    # sommaire, constat 6 (erratum 8 du 29 octobre)
    ('il n’impose qu’information et observations devant un employé habilité à réviser :',
     'il impose information, observations devant un employé habilité à réviser et, sur demande, '
     'communication des raisons et des principaux facteurs et paramètres de la décision (8.4) :'),
    # sommaire, constat 10 (erratum 10 du 29 octobre)
    ('<p>10. Le corpus compagnon compte quatre volumes, dont deux ne sont pas écrits. Deux volumes rédigés '
     'fournissent des faits (4.12, 8.4) ; deux ne sont que des cadrages — zéro chapitre — et ne prêtent que '
     'des instruments, marqués comme constructions d’auteur.',
     '<p>10. Le corpus compagnon compte quatre volumes. Deux fournissent des faits (4.12, 8.4) ; les deux '
     'autres, cadrages sans chapitre aux passes de juillet, sont rédigés depuis, le 22 et le 29 juillet, mais '
     'à diffusion bornée à leur auteur (13.8), et ne prêtent que des instruments, marqués comme '
     'constructions d’auteur.'),
    # 1, QR4 : la septième couche
    ('sémantique, de confiance, orchestration —,', 'sémantique, de confiance, orchestration, exploitation —,'),
    # 1.1, contribution 7 : MPP; l'inactivité est celle d'AP2
    ('AP2, x402, ACP et UCP répliquent le fossé identité-autorisation ; aucun vocabulaire de capacités '
     'partagé (OASF bornée à son écosystème) ; x402 est allé plus loin qu’AP2, à la Linux Foundation [282], '
     'sans commit depuis le 29 avril 2026 ;',
     'AP2, x402, MPP, ACP et UCP répliquent le fossé identité-autorisation ; aucun vocabulaire de capacités '
     'partagé (OASF bornée à son écosystème) ; x402 est allé plus loin qu’AP2, à la Linux Foundation [282], '
     'quand le dépôt d’AP2 est sans commit depuis le 29 avril 2026 ; MPP, sans fondation, est le second '
     'règlement par HTTP 402 (4.8) ;'),
    # 1.2 : la section 4.14
    ('implémentation de référence (4.12), exploitation (4.13),',
     'implémentation de référence (4.12), exploitation (4.13), orchestration des agents (4.14),'),
    # guide de lecture : la section 4.14
    ('orchestration, 4.11.6 ;', 'orchestration des processus, 4.11.6, et des agents, 4.14 ;'),
    # 2.2 : la prose suit le tableau 1
    ('Trois passes seulement — 2, 7 et 13 juillet — soumettent tout leur lot à la ronde adverse ; ailleurs, '
     'elle ne couvre que les énoncés les plus exposés, et les trois passes de veille n’en ont aucune. Les faits '
     'ne pèsent donc pas tous le même poids : les sections 4.6 à 4.13 en sont le haut,',
     'Deux passes seulement — 2 et 15 juillet — soumettent tout leur lot à la ronde adverse ; ailleurs — 7, 12 '
     'et 13 juillet, intégrale du 18 — elle ne couvre que les énoncés les plus exposés, et les quatre passes '
     'de veille, de l’édition d’août au 15 août, n’en ont aucune, pas plus que celle du 23 juillet. La colonne '
     '« Énoncés » compte des énoncés, sauf aux 12 et 18 juillet, où elle compte des agents. Les faits ne '
     'pèsent donc pas tous le même poids : les sections 4.10 et 4.11 en sont le haut, les sections 4.6, 4.8, '
     '4.9 et 4.13, vérifiées en partie individuellement, viennent ensuite, la 4.12 porte le régime de son '
     'corpus compagnon,'),
    # 4.1
    ('prise de contrôle de namespace d’organisation', 'prise de contrôle d’espace de nommage d’organisation'),
    # 4.3 : ANP 1.1, antérieure au gel (annexe du 29 octobre)
    ('le livre blanc reste en version unique [15].',
     'le livre blanc reste en version unique [15], quoique le dépôt canonique ait publié une version ANP 1.1 '
     'le 27 juin 2026 (annexe du 29 octobre, [351]).'),
    # tableau 3
    ('révision 2026-07-28 en <em>release candidate</em> [97])',
     'révision 2026-07-28 en <em>release candidate</em> au 12 juillet, normative depuis le 28 juillet [97])'),
    ('<td>livre blanc + brouillons W3C CG [15, 16]</td>',
     '<td>livre blanc + brouillons W3C CG [15, 16] ; ANP 1.1 au dépôt, 27 juin 2026 [351]</td>'),
    ('communauté ANP /incubation W3C (CG)', 'communauté ANP / incubation W3C (CG)'),
    # 4.5, cadrage : les sept couches
    ('de confiance, portant l’identité et l’autorisation que présupposent leurs cadres OAuth (§4.10).</p>',
     'de confiance, portant l’identité et l’autorisation que présupposent leurs cadres OAuth (§4.10). '
     'L’événementiel (§4.6), le plan de contrôle (§4.7), l’orchestration des processus (§4.11) et '
     'l’exploitation (§4.13) complètent les sept couches ; la sous-section 4.12 est une épreuve par le code, '
     'non une couche.</p>'),
    # 4.8 : citation de [284] (annexe de novembre)
    ('seule la réservation de <em>handle</em> est ouverte, le reste restant « in the coming months » [284].',
     'seule la réservation de <em>handle</em> est ouverte, le reste annoncé pour plus tard [284].'),
    ('<em>Et le protocole le plus adopté de la sous-couche règlement n’a migré nulle part</em> : MPP n’a ni '
     'fondation, ni gouvernance neutre, ni version numérotée.',
     '<em>Et le protocole le plus adopté de la sous-couche règlement n’a migré nulle part</em> : MPP n’a ni '
     'fondation, ni gouvernance neutre, ni version numérotée ; son noyau est pourtant déposé à l’IETF depuis '
     'le 19 juin 2026, en soumission individuelle sans filière (annexe de novembre).'),
    # 4.9
    ('Existe-t-il ? Par examen direct des spécifications : non.',
     'Existe-t-il ? Par examen direct des spécifications des trois protocoles structurants : non.'),
    ('le billet primaire ne nomme ni AGNTCY ni OASF, et n’a reçu au 15 août 2026 ni nouvelle version,',
     'le billet primaire ne nomme ni AGNTCY ni OASF, et la spécification n’a reçu au 15 août 2026 ni nouvelle version,'),
    # 4.10 : DMSC n'est pas un groupe de travail (annexe du 29 octobre, [359])
    ('Mais trois BoF agentiques ont été approuvées en juin 2026, et deux groupes en sont issus : '
     '<strong>DAWN</strong> (découverte d’agents, de charges de travail et d’entités nommées) et '
     '<strong>DMSC</strong> (collaboration multi-agents sécurisée dynamique) [159]. <em>Au 15 août 2026, '
     'ces deux groupes portent',
     'Mais trois BoF agentiques ont été approuvées en juin 2026 : <strong>DAWN</strong> (découverte '
     'd’agents, de charges de travail et d’entités nommées) en est issu comme groupe de travail, et '
     '<strong>DMSC</strong> (collaboration multi-agents sécurisée dynamique), que cette édition donnait '
     'pour charté, figure au registre à l’état « BoF concluded » le 8 octobre (annexe du 29 octobre, [359]) '
     '[159]. <em>Au 15 août 2026, ces deux enceintes portent'),
    ('<em>DAWN et DMSC, chartés en juin, portent vingt-sept brouillons et n’en ont adopté aucun</em> [159]',
     '<em>DAWN, charté en juin, et DMSC, resté BoF, portent vingt-sept brouillons et n’en ont adopté aucun</em> [159]'),
    ('les deux groupes agentiques chartés en juin n’ont toujours rien adopté.',
     'ni DAWN, charté en juin, ni DMSC n’ont toujours rien adopté.'),
    # tableau 6
    ('<td>Google Agent Identity — identité SPIFFE par agent, GA le 22 avril 2026 [153]</td>',
     '<td>Google Agent Identity — identité SPIFFE par agent, GA le 22 avril 2026 ; Agent Identity API et '
     '<em>auth manager</em> en préversion [153]</td>'),
    # tableau 8 : la garantie de Zeebe n'est pas attestée
    ('<td><em>exactly-once</em> (état) — portée non énoncée par la page citée [183] ;',
     '<td>garantie non énoncée par la page citée [183] — l’<em>exactly-once</em> d’état lui était prêté sans source ;'),
    ('pré-version', 'préversion', 4),
    # 4.11.3 : pourquoi le décompte ne se fixe pas
    ('<em>Le décompte d’implémentations ne se laisse pas fixer : huit produits portent des résultats publiés, '
     'trois n’en portent aucun.</em>',
     '<em>Le décompte d’implémentations ne se laisse pas fixer : huit produits portent des résultats publiés, '
     'trois n’en portent aucun, et le nombre dépend de ce que l’on compte pour une implémentation (tableau 20).</em>'),
    # 4.11.5 : article 12.1, énoncé entier et partage des deux stades
    ('L’article 12.1 de la loi 25 québécoise', 'L’article 12.1 de la Loi 25 québécoise'),
    ('et n’impose alors que trois choses : informer au moment de la décision, permettre des observations '
     'devant un membre du personnel <em>en mesure de réviser</em>, communiquer sur demande les renseignements '
     'et les principaux facteurs [212].',
     'et impose alors d’informer la personne au moment de la décision, de lui permettre de présenter ses '
     'observations à un membre du personnel <em>en mesure de réviser</em> la décision, et de lui communiquer '
     'sur demande les renseignements utilisés, les raisons et les principaux facteurs et paramètres ayant '
     'mené à la décision, ainsi que son droit de rectification [212].'),
    ('Maintenir un humain en mesure de réviser sort la décision du champ de l’article ; sinon, information et '
     'voie de recours — tâche utilisateur de BPMN ou confirmation de CUA (4.11.2), table DMN (4.11.3).',
     'Une intervention humaine dans la décision même — tâche utilisateur de BPMN ou confirmation de CUA '
     '(4.11.2) — la sort du champ de l’article ; le membre du personnel en mesure de réviser après coup ne '
     'l’en sort pas : il est le recours que l’article impose, avec l’information et la restitution des '
     'facteurs et paramètres, que porte une table DMN (4.11.3).'),
    # 4.12 : ce qui reste rejouable
    ('Une implémentation de référence qu’on ne peut plus ouvrir ne porte plus le même régime de preuve.</p>',
     'Une implémentation de référence qu’on ne peut plus ouvrir ne porte plus le même régime de preuve. '
     'Restent rejouables sur les dépôts publics les comportements des SDK amont — SDK Go de MCP v1.6.1, '
     'a2a-go v2.3.1 — ; les défauts propres au démonstrateur ne se vérifient plus.</p>'),
    # 4.13.1
    ('dans chacun des deux fichiers candidats [228].',
     'dans chacun des deux fichiers candidats, <code>gen-ai-agent-spans.md</code> et <code>gen-ai-spans.md</code> [228].'),
    # tableau 10
    ('<td>[233], [287], [330]</td>', '<td>[233], [286], [287], [330]</td>'),
    ('<strong>aucune fusionnée ni fermée</strong>', '<strong>aucune résolue ni fermée</strong>'),
    ('(QO 24)', '(question ouverte 24)'),
    # 4.14 : le registre de Google précède celui d'AWS
    ('le premier catalogue gouverné d’agents relève d’un exploitant, non de la couche commune, et il n’est '
     'toujours pas général.',
     'ce catalogue gouverné d’agents, venu après l’Agent Registry de Google, général depuis le 18 juin 2026 '
     '(tableau 12), relève d’un exploitant, non de la couche commune, et il n’est toujours pas général.'),
    ('(QO 25)', '(question ouverte 25)'),
    ('Chacune des sept couches orthogonales des sections 4.6 à 4.13 dispose',
     'Chacune des sept couches orthogonales des sections 4.6 à 4.11 et 4.13 — la 4.12 est une épreuve, non '
     'une couche — dispose'),
    # 5
    ('Le tableau 6.5 porte les statuts', 'Le tableau 11 porte les statuts'),
    ('AARP et COAZ — autorisation des appels d’outils MCP — en brouillons le 15 juin 2026 [79] ;',
     'AARP et COAZ — autorisation des appels d’outils MCP — en brouillons le 15 juin 2026 [79], dont le '
     'texte en vigueur est au dépôt du groupe [327] ;'),
    # 5.5 et 9.1 : a2a-tck, tronc immobile et dépôt actif (erratum 9 du 29 octobre)
    ('<code>a2a-tck</code> (Apache-2.0, mai 2025), sans une fusion depuis le 29 juin 2026 [264],',
     '<code>a2a-tck</code> (Apache-2.0, mai 2025), sans une fusion depuis le 29 juin 2026 mais six demandes '
     'de tirage ouvertes en août [264],'),
    # 6.5
    ('« portée par » l’agentique [82] [275].', '« portée par » l’agentique [82, 275].'),
    # 7.1 : OWASP (annexe de novembre)
    ('n’a rien publié depuis juin 2026, et aucun relevé d’incidents ne succède à celui du 14 avril [71, 109].',
     'n’a rien publié depuis juin 2026 à l’index de l’initiative, et aucun relevé d’incidents n’y succède à '
     'celui du 14 avril [71, 109] ; le projet GenAI d’OWASP date pourtant du 8 juillet un relevé du deuxième '
     'trimestre (annexe de novembre).'),
    # 7.1 et 8.4 : l'incident de juillet, d'après les primaires du 26 août (annexe de novembre)
    ('par une faille zéro-jour dans un logiciel de registre de paquets exposé sur l’internet,',
     'par des failles zéro-jour d’une instance interne de registre de paquets, devenue leur voie vers '
     'l’internet (rapport technique du 26 août, annexe de novembre),', 2),
    ('elle a été fabriquée (8.4).</p>',
     'elle a été fabriquée (8.4) — selon l’avis de la CSA ; l’enquête indépendante publiée depuis estime à '
     'environ 7 % les transcriptions falsifiées, à petite échelle, et n’a vu aucune altération réussie des '
     'journaux (annexe de novembre).</p>'),
    # 7.2
    ('l’Agent Identity API demeure en préversion depuis le 15 juin 2026 [107, 153]',
     'l’Agent Identity API demeure en préversion depuis le 18 juin 2026 [107, 153]'),
    # 7.3
    ('passé au groupe DAWN, chartré en juin,', 'passé au groupe DAWN, charté en juin,'),
    # 7.8
    ('Entrées de registre : retrait par l’exploitant', '<strong>Entrées de registre</strong> : retrait par l’exploitant'),
    ('Attestations vérifiables : mécanisme de statut spécifié', '<strong>Attestations vérifiables</strong> : mécanisme de statut spécifié'),
    # 8 : pictogrammes de correction
    ('✎ <em>Correction d’un énoncé de l’édition précédente</em>', '<em>Correction d’un énoncé de l’édition précédente</em>', 2),
    ('✎ <em>Correction</em> :', '<em>Correction</em> :'),
    ('✎ Mais il n’impose pas seulement', 'Mais il n’impose pas seulement'),
    ('[341], texte canadien primaire qui, lui, nomme', '[341], texte primaire cosigné par le Canada qui, lui, nomme'),
    # 8.3
    ('COAZ projette déjà, en brouillon, chaque appel d’outil MCP sur un point AuthZEN [149] ;',
     'COAZ projette déjà, en brouillon, chaque appel d’outil MCP sur un point AuthZEN [149, 327] ;'),
    # 8.4 : AMF, état du PDF (annexe de novembre, erratum 1, témoignage hors passe)
    ('La date de la version finale de la ligne directrice IA de l’AMF diverge — 30 mars 2026 au socle [218], '
     'contre le 7 avril ici [210] —',
     'La date de la version finale de la ligne directrice IA de l’AMF diverge — 30 mars 2026 au socle [218], '
     'contre le 7 avril ici [210] ; le PDF, lu depuis hors passe, porte « Mars 2026 » et une modification du '
     '30 mars, pour une publication en avril (annexe de novembre, erratum 1) —'),
    ('l’incident de juillet 2026 en fournit la preuve par des artefacts de journaux hallucinés (7.1) [337]',
     'l’incident de juillet 2026 en fournit un indice par des artefacts de journaux hallucinés (7.1) [337], '
     'que l’enquête indépendante ramène à des transcriptions falsifiées, sans journal altéré'),
    # 9.1
    ('kit d’A2A figé depuis juin 2026 [264]', 'kit d’A2A au tronc immobile depuis le 29 juin 2026, au dépôt actif [264]'),
    # 9.5 : MPP
    ('<strong>ni AP2, ni UCP, ni ACP</strong> [285] : souscrire à tout n’empêche pas les tiers de trancher.',
     '<strong>ni AP2, ni UCP, ni ACP</strong> [285], et documente MPP depuis le 5 août [309] : souscrire à '
     'tout n’empêche pas les tiers de trancher, entre mandats sinon entre règlements (4.8).'),
    # 9.6 : réserve de source sur l'AMF
    ('les instruments d’E-23, de l’AMF, de l’art. 12.1 et de DORA [172]',
     'les instruments d’E-23, de l’AMF — sous la réserve de source de la section 8.4 —, de l’art. 12.1 et de DORA [172]'),
    # 10 : AI Act consolidé (erratum 11 du 29 octobre)
    ('Aucune version consolidée de l’AI Act intégrant le règlement (UE) 2026/1744 n’est disponible non plus.',
     'La version consolidée de l’AI Act intégrant le règlement (UE) 2026/1744 est publiée (8.1, [254]), mais '
     'l’outillage automatisé n’en a reçu que des réponses vides.'),
    ('ses constats restent exacts et datés, mais un renvoi exact vers un fichier absent reste exact ; il cesse '
     'd’être opposable.',
     'ses constats restent exacts et datés, mais un renvoi vers un fichier absent, s’il reste exact, cesse '
     'd’être opposable.'),
    # 11, questions 15 et 25
    ('Deux implémentations d’A2A convergeront-elles sans suite de conformité, une canonicalisation libre ayant '
     'rompu l’interopérabilité (4.12 [217]) ?',
     'Deux implémentations d’A2A convergeront-elles tant que les vecteurs de canonicalisation RFC 8785 restent '
     'en demande ouverte au kit de conformité, une canonicalisation libre ayant rompu l’interopérabilité '
     '(4.12, [217]) ?'),
    ('L’orchestration hors de la couche commune ? Un format', 'L’orchestration hors de la couche commune. Un format'),
    # 12
    ('ligne directrice IA de l’AMF, finale [210] — date du 7 avril non reconfirmée en source primaire '
     '(section 13.6) ; Camunda 8.9 (MCP GA, connecteurs A2A alpha) [170]',
     'ligne directrice IA de l’AMF, finale en avril 2026, document daté de mars [210] — le 7 avril ne se '
     'cite qu’avec sa source secondaire (annexe de novembre, erratum 1) ; Camunda 8.9, 14 avril (connecteur '
     'MCP sorti de l’arbre alpha, sans disponibilité générale énoncée ; connecteurs A2A alpha) [170]'),
    # 12.1 et 10 : RTR (annexe de novembre, erratum 3)
    ('celle du règlement d’exploitation reste sous attribution secondaire [257].',
     'celle du règlement d’exploitation et des règles, tenue ici sous attribution secondaire [257], est '
     'confirmée par un communiqué de Paiements Canada du 30 juin 2026 (annexe de novembre, erratum 3).'),
    ('deux énoncés y sont sous attribution : l’entrée en vigueur du règlement d’exploitation du RTR,',
     'deux énoncés y sont sous attribution : l’entrée en vigueur du règlement d’exploitation du RTR, confirmée '
     'depuis (annexe de novembre, erratum 3),'),
    ('(2030-2032 [171])', '(2030-2032, [171])'),
    ('mais l’IETF a refusé la BoF sur la délégation en mai 2026 [159].',
     'mais l’IETF a refusé la BoF sur la délégation en mai 2026, et DAWN, seul groupe agentique charté en '
     'juin, n’a rien adopté au 15 août [159].'),
    # 13 : état de juillet, dit comme tel
    ('<h3>13.1 Quatre volumes, deux états de rédaction</h3>',
     '<h3>13.1 Quatre volumes, deux états de rédaction</h3>\n<p><em>Les sections 13.1 à 13.5 et les tableaux '
     '15 et 16 décrivent le corpus à son état des 18 et 19 juillet 2026, celui des passes de juillet. Les '
     'volumes III et IV ont été rédigés depuis, le 22 et le 29 juillet, le Vol. IV arrêté en cinq livres et '
     'cinquante chapitres ; leur régime de citation tient, pour un autre motif : la diffusion bornée à leur '
     'auteur (13.8).</em></p>'),
    (' <em>Note du 29 octobre 2026. Les tableaux 15 et 16 et les sections 13.1 à 13.5 décrivent l’état du '
     '18–19 juillet 2026 Le Compendium livré compte cinq livres et cinquante chapitres, et les volumes III et '
     'IV sont rédigés (13.8).</em></td>', '</td>'),
    ('<em>programmé / projeté /spéculatif</em>', '<em>programmé / projeté / spéculatif</em>'),
    ('et n’impose alors qu’information de la personne et possibilité d’observations devant un employé '
     '<strong>en mesure de réviser</strong> — il borne l’absence totale d’humain, sans prescrire aucun degré '
     'd’autonomie (8.2, 9.6).',
     'et impose alors information de la personne, possibilité d’observations devant un employé '
     '<strong>en mesure de réviser</strong> et, sur demande, communication des raisons et des principaux '
     'facteurs et paramètres de la décision — il borne l’absence totale d’humain, sans prescrire aucun degré '
     'd’autonomie (8.4, 9.6).'),
    # tableau 18
    ('<td>confirmation avant effet ; refus remédiable (4.10)</td>',
     '<td>confirmation avant effet ; refus remédiable (4.11.2, 4.11.3, 4.11.5)</td>'),
    # tableau 19
    ('Même défaut que la ligne suivante, trouvé par le même moyen.', 'Même défaut que la ligne précédente, trouvé par le même moyen.'),
    ('state=all&amp;sort=updated', 'state=all&amp;' + ZWSP + 'sort=updated', None),
    # tableau 20 : l'issue ne décrit pas l'édition publiée
    ('<td>légendes redescendues après le tableau, dans tous les artefacts</td>',
     '<td>légendes redescendues après le tableau dans les artefacts de la passe ; l’édition publiée les place '
     'pourtant avant (relecture du 3 novembre 2026)</td>'),
    # tableaux 22 et 24 : 217 et 219 comptés deux fois
    ('<tr><td>Orchestration des processus</td><td>167, 169, 173, 174, 175, 181, 188, 189, 190, 203, 214, 217, '
     '219, 224, 226, 230, 231, 232, 287</td><td>dix-neuf numéros pour <strong>dix-sept références déclarées</strong> '
     '— l’écart n’est pas résolu</td>',
     '<tr><td>Orchestration des processus et exploitation (4.11, 4.13)</td><td>167, 169, 173, 174, 175, 181, '
     '188, 189, 190, 203, 214, 224, 226, 230, 231, 232, 287</td><td><strong>dix-sept</strong>, 217 et 219 '
     'étant comptées à la ligne précédente</td>'),
    ('dix-sept à dix-neuf références de faible volatilité', 'dix-sept références de faible volatilité'),
    # références
    ('Communiqué, 26 août 2025. https://my.idc.com/getdoc.jsp?containerId=prUS53765225',
     'Communiqué, 26 août 2025 — même pièce que [275], qui en porte la réserve de lecture. '
     'https://my.idc.com/getdoc.jsp?containerId=prUS53765225'),
    ('; exposition des flots RPA, agents, flots API et processus BPMN Maestro comme outils MCP)',
     '; l’énumération des flots RPA, agents, flots API et processus BPMN Maestro exposés comme outils MCP ne '
     'se lit pas dans la note : 4.11.2)'),
    ('dix produits aux résultats publiés, dont', 'huit produits aux résultats publiés et trois sans résultat, '
     'décompte non fixé (tableau 20), dont'),
    ('le reste annoncé « in the coming months ».', 'le reste annoncé pour plus tard.'),
    (' ( <em>adresse relevée le 17 août 2026', ' (<em>adresse relevée le 17 août 2026', 3),
    ('<li><p>Amazon Web Services. Annonces du 6 août 2026 —',
     '<li><p>Amazon Web Services. Annonces du 6 août 2026 (adresses exactes : [394], annexe de novembre, pour '
     'les instances ; [333] pour la préversion du registre) —'),
    ('; chaque cas d’usage d’un modèle sous-jacent capturé et évalué séparément)',
     '; inventaire des usages approuvés — l’évaluation séparée de chaque cas d’usage ne s’y lit pas en ces '
     'termes, 4.11.5)'),
    # tableau 12 : AWS et Google (sections 4.14, 7.2; annexe de novembre)
    ('<td>Gateway MCP et Agent Registry <strong>GA le 13 octobre 2025</strong> ;',
     '<td>Gateway MCP <strong>GA le 13 octobre 2025</strong> ; Agent Registry en préversion depuis le 9 avril '
     '2026, relancé le 6 août, non général au 15 août (4.14) ;'),
    ('type de calcul <em>Instances</em> du <em>Runtime</em> annoncé le 6 août 2026 — aucune entrée n’en énonce '
     'la disponibilité générale</td>',
     'type de calcul <em>Instances</em> du <em>Runtime</em> en disponibilité générale le 6 août 2026 [290]</td>'),
    ('Agent Registry (agents et serveurs MCP), Agent Gateway et serveur MCP distant <strong>GA le 18 juin 2026</strong>',
     'Agent Registry (agents et serveurs MCP) et Agent Gateway <strong>GA le 18 juin 2026</strong>, serveur MCP '
     'distant GA dès le lancement du 22 avril (annexe de novembre)'),
    # 8.5 : la rétractation de 4.11.5 sur E-23
    ('E-23 exige que chaque cas d’usage d’un modèle soit capturé et évalué séparément,',
     'E-23 exige un inventaire des usages approuvés de chaque modèle (4.11.5),'),
]


def corriger(s):
    for c in CORRECTIONS:
        ancien, nouveau, *n = c
        attendu = n[0] if n else 1
        k = s.count(ancien)
        assert k > 0 if attendu is None else k == attendu, f'correction : passage trouvé {k} fois : {ancien[:80]}'
        s = s.replace(ancien, nouveau)
    return s
