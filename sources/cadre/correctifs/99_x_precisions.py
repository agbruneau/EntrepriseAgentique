"""Précisions qui lèvent les ambiguïtés relevées par des constats d'abord écartés (orchestrateur).

Ces constats avaient été jugés faux ou réglés ailleurs : le texte était exact, mais un réviseur
attentif s'y était mépris, ou la cause était corrigée sous un autre numéro. Les précisions
ci-dessous ferment la lecture qui avait mené au constat.
"""
NBSP = '\xa0'

CORRECTIONS = [
    # 06-18 : date de la révision MCP et version candidate
    ('l’identifiant AAAA-MM-JJ correspond au dernier changement incompatible.',
     'l’identifiant AAAA-MM-JJ correspond, selon la page Versioning de la spécification, au dernier changement '
     'incompatible qu’introduit la révision : c’est la date de sa publication, non celle du gel de sa version '
     'candidate.', ['06-18']),
    # 08-15 : un agent qui republie est un nouveau producteur (conventions de messagerie d'OpenTelemetry)
    ('un agent qui publie un nouvel événement en réaction y <strong>DOIT</strong> recopier le <code>traceparent</code> '
     'de l’événement reçu (ou, s’il ouvre la chaîne, celui de la trace qu’il ouvre),',
     'un agent qui publie un nouvel événement en réaction y <strong>DOIT</strong> porter un <code>traceparent</code> '
     'de la même trace que l’événement reçu, dont le span parent est son propre span de publication, et relier son '
     'span de traitement à l’événement reçu par un lien de span, pour que la trace garde l’arbre causal (ou, s’il '
     'ouvre la chaîne, le <code>traceparent</code> de la trace qu’il ouvre),', ['08-15']),
    # 09-18 : signaux des entrées au statut Adopter
    ('L’apparition du signal <strong>DOIT</strong> entraîner une révision extraordinaire de l’entrée, sans attendre '
     'l’échéance trimestrielle.</p>',
     'L’apparition du signal <strong>DOIT</strong> entraîner une révision extraordinaire de l’entrée, sans attendre '
     'l’échéance trimestrielle. Pour une entrée au statut Adopter ou Contenir, une nouvelle révision, une '
     'dépréciation ou une version stable relève de l’EXIG-GOV-18, qui en fixe la révision extraordinaire.</p>',
     ['09-18']),
    # 09-27 : plusieurs systèmes d'enregistrement en parallèle
    ('Une branche de garde-fou <strong>DOIT</strong> rendre son verdict avant la fusion; une expiration vaut refus '
     '(PRIN-12).</p>',
     'Une branche de garde-fou <strong>DOIT</strong> rendre son verdict avant la fusion; une expiration vaut refus '
     '(PRIN-12). S’il faut écrire dans plusieurs systèmes d’enregistrement, un seul composant écrit dans chacun, sous '
     'une saga (section 7.5).</p>', ['09-27']),
    # 10-41 : intitulé de la troisième catégorie de MAST
    ('conception du système, désalignement entre agents et vérification des tâches.',
     'conception du système, désalignement entre agents, et vérification et terminaison des tâches.', ['10-41']),
    # 21-29 : deux ordres de grandeur, deux sources
    ('une architecture multiagent consomme habituellement de 3 à 10 fois plus de jetons qu’un agent '
     'unique<strong><sup>[275]</sup></strong>.',
     'une architecture multiagent consomme de 3 à 10 fois plus de jetons qu’un agent unique selon '
     '[275]<strong><sup>[275]</sup></strong>, et environ 3,75 fois selon les mesures d’Anthropic (environ 15 fois une '
     'conversation contre environ 4 fois pour un agent)<strong><sup>[17]</sup></strong>.', ['21-29']),
    # 18-24 : C-36 et transition de l'article 50(2), reportés de l'annexe H dans le corps
    ('Déposé le 15 juin 2026; deuxième lecture; non en vigueur',
     'Déposé et lu une première fois le 15 juin 2026; à l’étape de la deuxième lecture; non en vigueur', ['18-24']),
    ('dont les obligations de transparence de l’article 50, depuis le 2 août 2026<strong><sup>[57]</sup></strong>.',
     'dont les obligations de transparence de l’article 50, depuis le 2 août 2026, avec une transition au 2 décembre '
     '2026 pour le marquage de l’article 50(2) des systèmes génératifs mis sur le marché avant le 2 août '
     '2026<strong><sup>[57]</sup></strong>.', ['18-24']),
    ('lignes directrices et avis du BSIF, directive fédérale,',
     'lignes directrices et avis du BSIF, lignes directrices de l’AMF pour une institution de compétence québécoise, '
     'directive fédérale,', ['18-24']),
]

JOURNAL = [
    ('§ 6.5, versionnage de MCP', 'Date de la révision précisée : celle de sa publication, qui porte le dernier '
     'changement incompatible, non celle du gel de la version candidate.', ['06-18']),
    ('§ 6.7, EXIG-EVT-04', 'Un agent qui republie porte un traceparent de la même trace dont le span parent est son '
     'span de publication, et relie son traitement à l’événement reçu par un lien de span.', ['08-15']),
    ('§ 6.9, EXIG-INT-23', 'Signaux des entrées Adopter ou Contenir renvoyés à l’EXIG-GOV-18.', ['09-18']),
    ('§ 7.2, EXIG-ORC-07', 'Écriture dans plusieurs systèmes d’enregistrement : un écrivain par système, sous saga.',
     ['09-27']),
    ('§ 7.9, MAST', 'Troisième catégorie nommée « vérification et terminaison des tâches ».', ['10-41']),
    ('§ 15.4, facteurs de succès', 'Les deux ordres de grandeur du coût en jetons du multiagent attribués chacun à sa '
     'source ([275] et [17]).', ['21-29']),
    ('Tableau 48, § 12.4, EXIG-CON-11', 'Étape de C-36, transition de l’article 50(2) et lignes directrices de l’AMF '
     'reportées de l’annexe H dans le corps.', ['18-24']),
]
