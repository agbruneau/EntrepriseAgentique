"""Corrections de la relecture du 3 novembre 2026, appliquées au corps extrait.

Le corps de la Revue n'a pas de source éditable : il est relu dans l'édition d'origine
(construire_pdf.py, ORIGINE). Comme les errata du 29 octobre, les corrections de la
relecture du 3 novembre sont faites à leur place, et consignées au tableau d'errata de
l'annexe (actualisation-2026-11.html, « Relecture du 3 novembre 2026 »).

Chaque correction remplace un passage qui doit figurer une fois exactement dans le corps
extrait : un passage absent ou ambigu arrête la composition au lieu de passer en silence.
"""
import re

NBSP = ' '

# (passage d'origine, passage corrigé), dans l'ordre du document
CORRECTIONS = [
    # 2.1 : les pièces à DOI sont citées aux fronts des processus et de la gouvernance,
    # non à la couche transactionnelle; règle de numérotation des normes
    ('sans laquelle le front transactionnel n’aurait pas de point d’appui.',
     'sans laquelle les fronts des processus d’affaires et de la gouvernance, où elles sont citées, '
     'n’auraient pas de point d’appui. Elles reçoivent un numéro parce qu’elles sont discutées comme '
     'pièces ; les normes que le texte invoque seulement comme référentiel — la RFC 8693 de l’IETF pour '
     'l’échange de jetons, le modèle PROV du W3C — sont nommées en ligne, sans entrée.'),
    # 2.1 : [43] et [47] désormais engagées en 9.3
    ('vingt-trois de ses cinquante pièces y sont engagées une à une, vingt-sept ne le sont pas',
     'vingt-cinq de ses cinquante pièces y sont engagées une à une, vingt-cinq ne le sont pas'),
    # 2.2 : règle de partage des commentaires, rendue déterministe
    ('une acceptation ou une présentation annoncée compte, une soumission annoncée ne compte pas —',
     'une acceptation ou une présentation annoncée compte, une soumission annoncée ne compte pas, et un '
     'nom de conférence ou d’atelier porté seul, sans mention de soumission ni d’évaluation en cours, '
     'vaut annonce d’acceptation —'),
    # tableau 2 : [180] est instruite aussi au front multi-agents
    ('<td>Systèmes multi-agents</td><td>[88-101], [187]</td>',
     '<td>Systèmes multi-agents</td><td>[88-101], [187] (et [180], rattachée à l’essaim)</td>'),
    # 5.1 : la séparation par capacités a déjà sa mesure hors du lot
    ('convertir la donnée non fiable en types de portée et de contenu bornés [74].</p>',
     'convertir la donnée non fiable en types de portée et de contenu bornés [74]. Hors du lot, l’idée '
     'a déjà sa mesure : CaMeL (Debenedetti <em>et al.</em>, arXiv:2503.18813, 2025) sépare flux de '
     'contrôle et flux de données par capacités et résout 77 % des tâches d’AgentDojo (Debenedetti '
     '<em>et al.</em>, NeurIPS 2024) avec une sécurité prouvable, contre 84 % sans défense, selon le '
     'résumé de sa version courante au 3 novembre 2026.</p>'),
    # 5.2
    ('revendication adossée à des études de cas non dénombrées, donc auto-évaluation et non évaluation adverse.',
     'revendication adossée à des études de cas non dénombrées, donc auto-évaluation et non évaluation '
     'adverse, quand le coût d’utilité de la séparation par capacités est chiffré ailleurs, à sept points '
     'de tâches résolues sur AgentDojo pour CaMeL (5.1).'),
    # 6.1 : [78] instruite à son front; antériorité du primitif atténuant
    ('capacités bornées par époque se fermant à l’achèvement de la tâche [87]. Le socle proposait déjà '
     'des jetons de capacité liés à l’invocation [16].',
     'capacités bornées par époque se fermant à l’achèvement de la tâche [87]. Une formalisation borne '
     'ce que la chaîne transmet de responsabilité : la délégation à deux niveaux répartit la '
     'responsabilité le long d’une chaîne à plusieurs sauts sous un plafond par agent, avec monotonie '
     'de la sûreté et convergence de la politique interne — trois résultats prouvés, la validation '
     'empirique étant annoncée pour une révision ultérieure [78]. <em>Prépublication d’un auteur unique, '
     'non révisée par les pairs : aucune mesure.</em> Le socle proposait déjà des jetons de capacité '
     'liés à l’invocation [16]. Le primitif est d’ailleurs antérieur aux agents : les Macaroons '
     '(Birgisson <em>et al.</em>, NDSS 2014) chaînent des réserves qui ne peuvent qu’atténuer '
     'l’autorité, chaque détenteur pouvant en ajouter sans l’émetteur, et Biscuit en donne une forme à '
     'clé publique, vérifiable hors ligne. Ce qui converge ici est l’adaptation d’un primitif établi aux '
     'protocoles d’agents, non son invention.'),
    # 6.1 : régime de [179]
    ('<em>Rapport d’expérience de trois auteurs : aucune mesure,',
     '<em>Prépublication non révisée par les pairs, rapport d’expérience de trois auteurs : aucune mesure,'),
    # 7.1
    ('la supervision d’exécution en récupère −29,68 % de jetons sans perte de succès sur GAIA [99].',
     'la supervision d’exécution réduit la dépense de jetons de 29,68 % sans perte de succès sur GAIA [99].'),
    # 7.2 : tableau 4, reste de l'erratum 3 du 29 octobre
    ('onze évaluent une construction de leurs auteurs et quatre annoncent un comité de lecture ; les '
     'quatre évaluations indépendantes contre ligne de base forte concluent toutes au non-avantage.',
     'onze évaluent une construction de leurs auteurs et quatre annoncent un comité de lecture ; les '
     'quatre pièces contre ligne de base forte concluent toutes au non-avantage, dont trois évaluent une '
     'architecture de tiers, [92] évaluant aussi son propre cadre et comptant des deux côtés.'),
    ('<td>Non-avantage</td><td>architecture de tiers</td>',
     '<td>Non-avantage</td><td>architecture de tiers ; des auteurs pour [92]</td>'),
    ('quand la correction bootstrap n’est qu’en O(n^−1/2).',
     'quand la correction bootstrap n’est qu’en O(n<sup>−1/2</sup>).'),
    # 8.1
    ('cache ainsi −64,3 points de dégât et +60,7 points de compensation',
     'cache ainsi 64,3 points de dégât et 60,7 points de compensation'),
    ('le prix de l’auditabilité se chiffre à son tour, <strong>8,3 ms',
     'le prix de l’auditabilité se chiffre à son tour : <strong>8,3 ms'),
    # 8.3
    ('sur-bloque massivement', 'surbloque massivement'),
    # 9.3 : [43] et [47]; portée de la lacune de responsabilité
    ('symétriquement, les deux pièces AP2 ignorent x402 [116], [117].',
     'symétriquement, les deux pièces AP2 ignorent x402 [116], [117], que le socle soumet pourtant à deux '
     'analyses d’attaque [43], [47].'),
    ('<p>Première lacune : aucune pièce ne traite la responsabilité d’une transaction non autorisée.',
     '<p>Première lacune : aucune pièce du corpus ne traite la responsabilité d’une transaction non autorisée.'),
    ('une pile assurantielle qui présuppose résolue l’allocation de responsabilité qu’elle ne traite pas [45].',
     'une pile assurantielle qui présuppose résolue l’allocation de responsabilité qu’elle ne traite pas '
     '[45]. La doctrine juridique des paiements — mandats électroniques, régimes de la DSP2 ou du '
     'règlement E américain — se publie en revues de droit, hors du périmètre d’arXiv : la lacune est '
     'celle du corpus, non celle du droit.'),
    # 10.1 : [136]; chiffre de [127] révisé
    ('la gouvernance des agents en processus [32].</p>',
     'la gouvernance des agents en processus [32]. La seule pièce du front attestée en revue mesure '
     'autre chose : la compétence des modèles de langue à produire un modèle de processus, non '
     'l’exécution d’un agent [136].</p>'),
    ('à moins de 6 % de surcoût [127].',
     'à moins de 6 % de surcoût dans la version citée, de 5,2 à 6,6 % depuis sa v3 du 31 août 2026 '
     '(tableau 10) [127].'),
    # 10.2 : [134] révisée
    ('des portes d’approbation humaine des invariants applicables [134]',
     'des portes d’approbation humaine des invariants applicables [134], doté depuis sa v3 d’une preuve '
     'et d’une mesure (tableau 10),'),
    # 10.3 : portée de la requête; conformité imposée et vérification binaire
    ('pas l’exécution d’un agent contre un modèle métier.</p>',
     'pas l’exécution d’un agent contre un modèle métier. La requête est un indicateur, non une preuve '
     'd’absence : la gestion des processus publie surtout hors d’arXiv, et nomme aussi la chose '
     'alignement de trace ou conformité d’exécution. Deux frontières bornent la lacune. Un contrôleur '
     'formel qui pilote l’agent — le graphe DCR de [137], les invariants d’approbation de [134] — '
     'impose la conformité par construction, <em>a priori</em> ; ce qui manque est le contrôle <em>a '
     'posteriori</em> d’une trace d’agent peu contrainte contre un modèle prescrit. Et la vérification '
     'de trace contre une spécification TLA+ ou LTL [171], [172] rend une acceptation binaire, non la '
     '<em>fitness</em> et la précision de la discipline.</p>'),
    # 11.2 : renvoi
    ('<em>La mise en garde de cette revue tient donc toujours :',
     '<em>La mise en garde de méthode de cette revue (3.1, 17) tient donc toujours :'),
    # 12 : registres vérifiables
    ('Ce front compte quatre mesures, dont une seule arbitrée, trois propositions d’architecture, trois '
     'positions, et aucune simulation.',
     'Ce front compte quatre mesures, dont une seule arbitrée — [151], [152], [154], [158] —, trois '
     'propositions d’architecture — [149], [150], [156] —, trois positions — [153], [155], [157] —, et '
     'aucune simulation.'),
    # 13 : erratum 1 du 1er novembre, appliqué à sa place
    ('Aucune de ses seize pièces n’est publiée en comité de lecture —',
     'Aucune de ses seize pièces n’atteste en notice une publication en comité de lecture —'),
    ('ne porte aucun signe de revue [180].</p>',
     'ne porte aucun signe de revue [180]. Crossref établit depuis trois publications, [164], [171] et '
     '[172] (annexe de novembre).</p>'),
    # 13.1 : [160] révisée
    ('+10,5 points sur SWE-bench Verified à coût par tâche réduit de moitié [160]',
     '+10,5 points sur SWE-bench Verified à coût par tâche réduit de moitié dans la version citée, '
     'chiffres changés à la v3 du 4 octobre 2026 (tableau 10) [160]'),
    ('compromet la multi-agents à 80 %', 'compromet le système multi-agents à 80 %'),
    ('tombe de 68-75 % à 6-13 %', 'tombe de 68–75 % à 6–13 %'),
    # 14.1
    ('une attaque compromettant la multi-agents à 80 %', 'une attaque compromettant le système multi-agents à 80 %'),
    # 14.3 : dénominateurs
    ('les pièces entrées à la reprise du 15 août n’y sont pas comptées, et la répartition par front, '
     'elle, les compte.</em>',
     'les pièces entrées à la reprise du 15 août n’y sont pas comptées, ni dans les fractions par front '
     'ci-dessus, quand la répartition du tableau 2, elle, les compte.</em>'),
    # tableau 6
    ('idempotent / réversible /compensable / irréversible', 'idempotent / réversible / compensable / irréversible'),
    # tableau 7 : sécurité
    ('<td>[74] sous attaque adaptative [71], coût d’utilité publié</td>',
     '<td>[74] sous attaque adaptative [71], coût d’utilité publié comme l’est celui de CaMeL sur AgentDojo</td>'),
    # 15 : numéros doublés
    ('<h3>15.1 1. « ', '<h3>15.1 « '),
    ('<h3>15.2 2. « ', '<h3>15.2 « '),
    ('<h3>15.3 3. « ', '<h3>15.3 « '),
    # 15.3 : [112] n'est attestée qu'en commentaire; publiée hors notice
    ('La seule pièce arbitrée du front étend la provenance W3C aux flux agentiques',
     'La pièce du front bâtie sur la provenance du W3C — acceptation annoncée au seul champ de '
     'commentaire, publication à eScience 2025 établie hors notice (annexe de novembre) — l’étend aux '
     'flux agentiques'),
    # références : en-tête
    ('nomment quatre entrées ainsi qualifiées dont une base de littérature arbitrée établit la publication.</em></p>',
     'nomment quatre entrées ainsi qualifiées dont une base de littérature arbitrée établit la publication. '
     'Le champ de commentaire est cité dans ses 55 premiers caractères, la coupure marquée « […] ». Les bancs '
     'que plusieurs pièces emploient sans y être discutés — AgentDojo, SWE-bench et sa sélection Verified '
     '(Jimenez <em>et al.</em>, ICLR 2024) — sont nommés comme instruments, sans entrée, comme les normes '
     'et les primitifs invoqués en référentiel.</em></p>'),
]

# Entrées de la bibliographie dont le champ de commentaire est coupé à 55 caractères
# (55 ou moins après retrait de l'espace final), vérifiées contre les notices le 3 novembre
# 2026; [131] fait exactement 55 caractères et n'est pas coupée.
COMMENTAIRES_COUPES = {7, 8, 32, 33, 61, 66, 79, 99, 103, 112, 113, 133, 135, 137, 145, 155, 156, 172, 183}


def corriger(s):
    for ancien, nouveau in CORRECTIONS:
        n = s.count(ancien)
        assert n == 1, f'correction : passage trouvé {n} fois : {ancien[:80]}'
        s = s.replace(ancien, nouveau)
    # appels groupés : séparés par une virgule, comme dans le reste du texte
    s = re.sub(r'(\[\d+\]) (?=\[\d+\])', r'\1, ', s)
    # pas de « % » rejeté en début de ligne
    s = re.sub(r'(?<=\d) %', NBSP + '%', s)
    # commentaires coupés : la coupure est marquée
    debut = s.index('<h2>Références</h2>')
    fin = s.index('</ol>', debut)
    entrees = s[debut:fin].split('<li>')
    for n in COMMENTAIRES_COUPES:
        e, k = re.subn(r'(<em>Comments</em> \(« .*?)( »\))', r'\1 […]\2', entrees[n], count=1)
        assert k == 1, f'commentaire de [{n}] introuvable'
        entrees[n] = e
    return s[:debut] + '<li>'.join(entrees) + s[fin:]
