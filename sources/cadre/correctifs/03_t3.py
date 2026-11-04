"""Correctifs de la revue du 3 novembre 2026 — tranche : § 7.3 à 7.10 et chapitre 8."""
import re

NBSP = '\xa0'


def t(s):
    """Typographie du corps : espace insécable avant « : », « % » et « $ », dans les
    guillemets, dans « p. ex. » et entre les tranches de trois chiffres."""
    s = s.replace(' :', NBSP + ':').replace('« ', '«' + NBSP).replace(' »', NBSP + '»')
    s = s.replace(' %', NBSP + '%').replace(' $', NBSP + '$').replace('p. ex.', 'p.' + NBSP + 'ex.')
    s = s.replace('Opus 4', 'Opus' + NBSP + '4')
    return re.sub(r'(?<=\d) (?=\d{3}\b)', NBSP, s)


_C = [
    # ------------------------------------------------------------------ § 7.3
    # [09-23] l'arbre de la figure 12 se lit sous trois règles qui priment sur le dessin
    ('''<p>Le choix du patron suit l’arbre de décision de la figure 12, qui part toujours de l’option la plus simple. Il se documente à la fiche de l’agent et se révise lorsque les mesures de production contredisent l’hypothèse de départ.</p>''',
     '''<p>Le choix du patron suit l’arbre de décision de la figure 12, qui part toujours de l’option la plus simple. Il se documente à la fiche de l’agent et se révise lorsque les mesures de production contredisent l’hypothèse de départ. L’arbre se lit sous trois règles, qui priment sur le dessin de la figure. D’abord, le mode de déclenchement ne choisit pas la topologie : un agent déclenché par un événement suit le même arbre qu’un agent sollicité par une personne, et la chorégraphie n’est retenue que si plusieurs domaines faiblement couplés réagissent au même fait (tableau 24). Ensuite, la question de l’agent unique se pose avant celle du routage, qui suppose un routeur et plusieurs spécialistes. Enfin, deux feuilles absentes du dessin sont admises : la chaîne séquentielle, lorsque les étapes sont connues et que chacune transforme la sortie typée de la précédente, et le clavardage de groupe, lorsqu’un débat contradictoire est requis (EXIG-ORC-06).</p>''',
     ['09-23']),
    ('''Les questions se lisent de haut en bas; la première réponse qui conclut fixe le patron. Les encadrés du bas''',
     '''Les questions se lisent de haut en bas; la première réponse qui conclut fixe le patron, sous les trois règles du texte qui précède : le déclenchement par événement ne mène pas à lui seul à la chorégraphie, l’agent unique se teste avant le routage, et la chaîne séquentielle et le clavardage de groupe restent admis. Les encadrés du bas''',
     ['09-23']),
    # [06-29] chiffre de 85 % nuancé comme au § 6.5
    ('''Selon Anthropic, sa recherche d’outils réduit de 85 % la consommation de jetons de contexte dans son exemple chiffré''',
     '''Selon Anthropic, sa recherche d’outils réduit de 85 % (près de 89 % d’après ses deux chiffres, section 6.5) la consommation de jetons de contexte dans son exemple chiffré''',
     ['06-29']),
    # [10-32] ORC-09 : décompte, chevauchement et critère de décision
    ('''<p>Dès qu’un agent dépasse 15 outils (seuil opérationnel retenu par le cadre dans la plage de 15 à 20 outils), ou dès que des outils se chevauchent, l’équipe <strong>DOIT</strong> mesurer la précision de sélection d’outils sur le jeu d’évaluation, puis essayer''',
     '''<p>Dès qu’un agent dispose de plus de 15 outils au début d’un tour (seuil opérationnel retenu par le cadre dans la plage de 15 à 20 outils), ou dès que le jeu d’évaluation montre des confusions entre outils (chevauchement), l’équipe <strong>DOIT</strong> mesurer la précision de sélection d’outils sur le jeu d’évaluation et la comparer au seuil de précision déclaré à la fiche, puis essayer''',
     ['10-32']),
    # [10-22, 10-38] ORC-10 : la nuance « une tâche à fortes dépendances reste à un seul agent » devient une règle
    ('''une spécialisation d’outils ou une frontière de sécurité, consignés à la fiche.</p>''',
     '''une spécialisation d’outils ou une frontière de sécurité, consignés à la fiche. Une tâche d’écriture à fortes dépendances <strong>DOIT</strong> rester à un seul agent (section 7.7).</p>''',
     ['10-22', '10-38']),

    # ------------------------------------------------------------------ § 7.4
    # [10-29] Temporal : limites d'historique et réessais illimités par défaut (audit_lit, ligne 71)
    ('''Temporal garantit qu’une exécution de flux se poursuit jusqu’à son terme, sans limite de durée imposée, et la reprend après une panne en rejouant son historique d’événements<strong><sup>[81]</sup></strong>.''',
     '''Temporal garantit qu’une exécution de flux se poursuit jusqu’à son terme, sans limite de durée imposée, et la reprend après une panne en rejouant son historique d’événements<strong><sup>[81]</sup></strong>. Cet historique est toutefois borné (51 200 événements ou 50 Mo par exécution, selon la documentation de Temporal) : une exécution longue se poursuit par Continue-As-New, et un résultat volumineux passe par référence (EXIG-ORC-24). Ses activités sont en outre réessayées sans limite par défaut (EXIG-ORC-27).''',
     ['10-29', '10-19']),
    # [10-16, 10-17, 10-27] ORC-11 : proportionnalité, granularité par étape journalisée, magasin en mémoire
    ('''<p>Tout flux de plus d’une étape, ou susceptible d’attendre une approbation, <strong>DOIT</strong> s’exécuter sur un moteur d’exécution durable qui persiste l’état après chaque transition (appel de modèle, appel d’outil, décision, réponse humaine) dans un magasin externe au processus. Un magasin en mémoire <strong>NE DOIT PAS</strong> être utilisé hors du poste de développement.</p>''',
     '''<p>Tout flux qui comporte au moins une étape P2 ou P3, une attente humaine (approbation, question) ou une durée supérieure à un seuil déclaré à la fiche <strong>DOIT</strong> s’exécuter sur un moteur d’exécution durable qui persiste l’état après chaque étape journalisée (appel de modèle, appel d’outil, décision, réponse humaine) dans un magasin externe au processus; chaque appel non déterministe à effet est sa propre étape (EXIG-ORC-12). Les autres flux de plus d’une étape <strong>DEVRAIENT</strong> le faire. Un magasin en mémoire <strong>NE DOIT PAS</strong> être utilisé en production ni dans un environnement qui traite des données réelles.</p>''',
     ['10-16', '10-17', '10-27']),
    # [10-15, 10-26, 12-16] ORC-12 : coordination déterministe définie; tout effet de bord idempotent ou exécuté au plus une fois
    ('''<p>La logique de coordination <strong>DOIT</strong> rester déterministe; chaque appel non déterministe <strong>DOIT</strong> s’exécuter comme une étape journalisée dont le résultat est relu, et non recalculé, à la reprise. Tout effet de bord placé avant un point de pause ou dans une étape réessayable <strong>DOIT</strong> être idempotent; sinon, il <strong>DOIT</strong> être déplacé après le point de pause.</p>''',
     '''<p>La logique de coordination <strong>DOIT</strong> rester déterministe une fois relus les résultats journalisés des appels non déterministes; chaque appel non déterministe <strong>DOIT</strong> s’exécuter comme une étape journalisée dont le résultat est relu, et non recalculé, à la reprise. Tout effet de bord, écriture ou non (notification, événement publié, appel facturé), <strong>DOIT</strong> être idempotent par une clé déterministe (EXIG-ORC-21) ou isolé dans une étape journalisée exécutée au plus une fois. Son emplacement par rapport au point de pause n’en dispense pas : un effet non idempotent ne précède jamais un point de pause et ne se trouve jamais dans une étape réessayable.</p>''',
     ['10-15', '10-26', '12-16']),
    # [10-28] ORC-13 : état modifié à la main; aucun jeton au point de contrôle (A-15)
    ('''conservation et élagage définis. Un orchestrateur <strong>NE DOIT PAS</strong> charger de point de contrôle d’origine non vérifiée.</p>''',
     '''conservation et élagage définis. Un orchestrateur <strong>NE DOIT PAS</strong> charger de point de contrôle d’origine non vérifiée. Toute modification manuelle de l’état (bifurcation après correction) est signée de nouveau par le service d’orchestration et journalisée en audit. Aucun jeton n’y figure (EXIG-IAM-06).</p>''',
     ['10-28']),
    # [10-28] Pourquoi d'ORC-13 : la phrase sourcée est séparée du constat du cadre
    ('''<p>Pourquoi : un point de contrôle contient l’état complet de la tâche, y compris les messages en attente; un point de contrôle altéré permet donc d’en modifier l’état, et ces messages peuvent contenir des RP (constat du cadre, non tiré de la source)<strong><sup>[105]</sup></strong>.</p>''',
     '''<p>Pourquoi : Microsoft désigne le point de contrôle, qui contient l’état complet de la tâche, y compris les messages en attente, comme une frontière de confiance<strong><sup>[105]</sup></strong>. Qu’un point de contrôle altéré permette d’en modifier l’état et que ces messages puissent contenir des RP est un constat du cadre.</p>''',
     ['10-28']),
    # [10-18] ORC-14 : cohabitation bornée, retrait de sécurité
    ('''une migration d’état en cours d’exécution <strong>DEVRAIT</strong> se tester comme un changement de schéma.</p>''',
     '''une migration d’état en cours d’exécution <strong>DEVRAIT</strong> se tester comme un changement de schéma. La cohabitation est bornée par le plafond de durée de l’EXIG-ORC-26. Le retrait d’une version pour un motif de sécurité <strong>DOIT</strong> suspendre les exécutions en cours ou les migrer par une migration testée.</p>''',
     ['10-18']),

    # ------------------------------------------------------------------ § 7.5
    # [10-01] règle 2 : résoudre l'issue incertaine avant de compenser (A-07)
    ('''<li><strong>Traiter l’incertain comme exécuté.</strong> Si l’orchestrateur ignore l’issue d’une étape (délai expiré, plantage entre le journal et la réponse), il la considère comme possiblement exécutée. Sa compensation doit alors pouvoir s’exécuter sans risque même si l’action n’a jamais eu lieu : « rembourser la transaction X si elle a été débitée », et non « rembourser le montant X ».</li>''',
     '''<li><strong>Résoudre l’incertain avant de compenser.</strong> Si l’orchestrateur ignore l’issue d’une étape (délai expiré, plantage entre le journal et la réponse), il la considère comme possiblement exécutée, mais aussi comme possiblement encore en cours chez le système visé : une compensation exécutée trop tôt ne trouve rien, réussit à vide, puis l’original produit son effet. Il clôt donc d’abord l’opération (annulation ou révocation de la clé d’idempotence, qui fait rejeter toute arrivée tardive) ou interroge le système visé par la clé jusqu’à une issue définitive; à défaut, l’étape passe en réconciliation humaine (EXIG-ORC-16). La compensation reste conditionnelle : « rembourser la transaction X si elle a été débitée », et non « rembourser le montant X ».</li>''',
     ['10-01']),
    # [10-03, 10-40] figure 13 : débit P3 avant le pivot, « non reprenable », « de k−1 à 1 » (figure non modifiable)
    ('''Le journal montre que chaque compensation est consignée avant l’action qu’elle couvre. Source : cadre CRE-IA-2026-01, d’après Garcia-Molina et Salem (1987), Microsoft et Temporal.''',
     '''Le journal montre que chaque compensation est consignée avant l’action qu’elle couvre. Le dessin simplifie deux points, que le texte corrige. Un débit externe est P3 et ne peut précéder le pivot (EXIG-ORC-15) : T3 se lit « préautoriser le paiement, sans capture », étape compensable (P2) par l’annulation de la préautorisation, et la capture se fait au pivot, avec son approbation. La compensation porte sur les étapes exécutées : de k−1 à 1 si T<sub>k</sub> a échoué sans effet, de k à 1 si son issue, une fois résolue (EXIG-ORC-16), est un effet réalisé. Source : cadre CRE-IA-2026-01, d’après Garcia-Molina et Salem (1987), Microsoft et Temporal.''',
     ['10-03', '10-40']),
    # [10-04, 10-06, 10-07, 09-24] ORC-15 : pivot unique, après-pivot réessayable, ordre des compensations, coordinateur de saga
    ('''<p>Une tâche qui écrit dans au moins deux systèmes d’enregistrement sans transaction commune <strong>DOIT</strong> être modélisée comme une saga : chaque étape d’écriture P2 référence la compensation déclarée dans son entrée de catalogue (section 6.8), le pivot est identifié, et toute étape de palier P3 (action critique, externe ou irréversible) se place au pivot ou après, une fois les validations critiques réussies et l’approbation humaine obtenue (section 8.5).</p>''',
     '''<p>Une tâche qui écrit dans au moins deux systèmes d’enregistrement sans transaction commune <strong>DOIT</strong> être modélisée comme une saga : chaque étape d’écriture P2 référence la compensation déclarée dans son entrée de catalogue (section 6.8); la définition de la saga déclare l’ordre des compensations (ordre inverse par défaut) et leurs dépendances, selon lesquels s’applique l’EXIG-ORC-18; le pivot, unique, est identifié; toute étape de palier P3 (action critique, externe ou irréversible) se place au pivot ou après, une fois les validations critiques réussies, et reçoit sa propre approbation humaine (EXIG-AUT-09 et EXIG-AUT-12). Les étapes qui suivent le pivot <strong>DOIVENT</strong> être idempotentes et réessayables jusqu’au succès, ou dotées d’une file humaine nommée pour l’échec définitif. En chorégraphie, un coordinateur de saga inscrit au registre tient le rôle de l’orchestrateur des EXIG-ORC-16 à EXIG-ORC-18 et de l’EXIG-ORC-31 (EXIG-ORC-08).</p>''',
     ['10-04', '10-06', '10-07', '09-24']),
    # [10-01, 10-23, 10-30] ORC-16 : écritures seulement, journal protégé et distinct de l'audit, résolution de l'incertain (A-07, A-15, A-18)
    ('''<p>Avant chaque étape, l’orchestrateur <strong>DOIT</strong> consigner dans un journal durable, en ajout seul et corrélé à la trace, l’étape, ses arguments, sa clé d’idempotence et la compensation à exécuter. Une étape dont l’issue est inconnue est traitée comme possiblement exécutée : sa compensation est déclenchée et reste sans effet si l’action n’a pas eu lieu.</p>''',
     '''<p>Avant chaque étape d’écriture (P2 ou P3), l’orchestrateur, ou le coordinateur de saga en chorégraphie, <strong>DOIT</strong> consigner dans un journal durable, en ajout seul et corrélé à la trace, l’étape, la référence de ses arguments, sa clé d’idempotence et la compensation à exécuter. Ce journal ne garde que des références et, chiffrés, les seuls arguments nécessaires à la compensation; il ne contient aucun jeton (EXIG-IAM-06). Il suit les contrôles de l’EXIG-ORC-13 (accès, chiffrement, conservation, élagage au plus tard à la clôture de la saga augmentée d’un délai déclaré); l’historique du moteur durable <strong>PEUT</strong> en tenir lieu. Il est distinct du journal d’audit (EXIG-OBS-11), qui n’en reçoit que des empreintes. Avant de compenser une étape dont l’issue est inconnue, l’orchestrateur <strong>DOIT</strong> soit clôturer l’opération chez le système visé (annulation ou révocation de la clé d’idempotence, de sorte que toute arrivée tardive soit rejetée), soit l’interroger par sa clé jusqu’à une issue définitive, une réponse 409 valant attente et non échec. Si aucune des deux voies n’existe, l’étape passe en réconciliation différée, confiée à une personne (EXIG-ORC-18), et n’est ni compensée ni replanifiée à l’aveugle.</p>''',
     ['10-01', '10-23', '10-30']),
    ('''<div id="pourquoi-629"><p>Pourquoi : un effet peut survenir avant que l’échec ne soit signalé<strong><sup>[286]</sup></strong>.</p></div>''',
     '''<div id="pourquoi-629"><p>Pourquoi : un effet peut survenir avant que l’échec ne soit signalé<strong><sup>[286]</sup></strong>; une compensation qui précède l’effet tardif de l’original réussit à vide et laisse un effet net, d’où la résolution préalable, choix du cadre.</p></div>''',
     ['10-01']),
    # [10-05] ORC-17 : la compensation est un outil à palier propre, approuvée avec l'étape (A-08)
    ('''<p>Chaque compensation <strong>DOIT</strong> être idempotente et définie en termes métier (remboursement, avis rectificatif, libération de stock) avec le propriétaire du système visé. L’orchestrateur réessaie''',
     '''<p>Chaque compensation <strong>DOIT</strong> être idempotente, définie en termes métier (remboursement, avis rectificatif, libération de stock) avec le propriétaire du système visé, et inscrite au catalogue comme un outil, avec son palier, référencé par le champ <code>compensation</code> de l’outil d’origine (annexe C, C.1). La compensation déclarée d’une étape approuvée, bornée au montant et aux bénéficiaires d’origine et liée à la même clé d’idempotence, est approuvée avec l’étape (EXIG-AUT-12); toute autre compensation P3 exige une nouvelle approbation. Par exemple, une préautorisation de paiement annulable est P2, et sa capture est P3. L’orchestrateur réessaie''',
     ['10-05']),
    # [10-31] ORC-18 : unité de décompte; graphe déclaré; coordinateur
    ('''<p>Lorsqu’une même compensation échoue deux fois de suite (erreur non transitoire ou politique de réessai épuisée), l’orchestrateur <strong>DOIT</strong> cesser de la relancer, poursuivre les compensations qui n’en dépendent pas,''',
     '''<p>Lorsqu’une compensation subit une erreur non transitoire, ou épuise deux fois de suite la politique de réessai déclarée, l’orchestrateur, ou le coordinateur de saga en chorégraphie, <strong>DOIT</strong> cesser de la relancer, poursuivre les compensations qui n’en dépendent pas selon le graphe déclaré (EXIG-ORC-15),''',
     ['10-31', '10-06']),
    # [10-08] ORC-19 : écrivains hors saga, échéance et propriétaire du verrou
    ('''<p>Lorsque plusieurs sagas ou agents peuvent modifier les mêmes enregistrements, la conception <strong>DOIT</strong> documenter les anomalies possibles (mises à jour perdues, lectures sales, lectures non répétables) et appliquer au moins une contre-mesure à chacune.</p>''',
     '''<p>Lorsque plusieurs sagas, agents ou autres écrivains du système d’enregistrement (personnes, traitements en lot, intégrations existantes) peuvent modifier les mêmes enregistrements, la conception <strong>DOIT</strong> documenter les anomalies possibles (mises à jour perdues, lectures sales, lectures non répétables) et appliquer au moins une contre-mesure à chacune. Tout verrou sémantique <strong>DOIT</strong> avoir une échéance, un propriétaire et une procédure de libération en cas de suspension ou d’escalade; un écrivain qui ne le respecte pas est traité comme une anomalie à couvrir.</p>''',
     ['10-08']),
    # [10-09] ORC-20 : tests manquants (A-07); titre modifié
    ('''<p><strong>Quatre tests d’injection de fautes</strong></p>
<p>Avant la mise en production, toute saga <strong>DOIT</strong> réussir quatre tests automatisés, exécutés contre des doublures des systèmes d’enregistrement : échec forcé de chaque étape T<sub>k</sub> avec vérification des compensations; plantage entre l’écriture au journal et l’action; double exécution de chaque compensation; double échec d’une compensation avec vérification de l’escalade.</p>''',
     '''<p><strong>Tests d’injection de fautes des sagas</strong></p>
<p>Avant la mise en production, toute saga <strong>DOIT</strong> réussir les tests automatisés suivants, exécutés contre des doublures des systèmes d’enregistrement : échec forcé de chaque étape T<sub>k</sub> avec vérification des compensations et de leur ordre déclaré; plantage entre l’écriture au journal et l’action; effet réalisé et résultat perdu; arrivée tardive de l’original après la décision de compenser; sagas concurrentes sur le même enregistrement; échec définitif après le pivot; double exécution de chaque compensation; double échec d’une compensation avec vérification de l’escalade; plantage pendant une compensation; compensation sous coupe-circuit et pendant une panne de la passerelle (EXIG-ORC-31). Un test de contrat d’idempotence <strong>DOIT</strong> en outre s’exécuter contre l’environnement d’essai du service visé, seul à connaître son comportement réel.</p>''',
     ['10-09']),

    # ------------------------------------------------------------------ § 7.6
    # [10-11, 10-12] texte : opération racine, rétention laissée au serveur par le brouillon (audit_lit, ligne 34)
    ('''<p>Le cadre dérive la clé de l’identifiant de la tâche et de celui de l’étape. Le brouillon IETF''',
     '''<p>Le cadre dérive la clé de l’identifiant de la tâche racine, stable de bout en bout, et de celui de l’étape. Le brouillon IETF''',
     ['10-12']),
    ('''acceptable pourvu que la clé reste unique par opération et que le service la valide avant tout traitement<strong><sup>[78]</sup></strong>.''',
     '''acceptable pourvu que la clé reste unique par opération et que le service la valide avant tout traitement<strong><sup>[78]</sup></strong>. Le brouillon laisse au serveur la durée de conservation des clés; le cadre la borne (EXIG-ORC-22).''',
     ['10-11']),
    # [10-12, 10-25] illustration : itération, étape incertaine, construction par canonisation
    ('''étape replanifiée avec d’autres valeurs → nouveau step_id, donc nouvelle clé</code></pre>''',
     '''étape replanifiée avec d’autres valeurs → nouveau step_id, donc nouvelle clé
étape dont l’issue est incertaine        → aucune replanification avant résolution (EXIG-ORC-16)
nouvelle itération d’une boucle          → indice d’itération dans step_id, donc nouvelle clé</code></pre>''',
     ['10-12']),
    ('''<pre><code>task_id         = "tache-7f3c2a"                      (attribué par l’orchestrateur)
step_id         = "etape-02/reserver-stock"
cle             = hex( SHA-256( task_id + "|" + step_id ) )</code></pre>''',
     '''<pre><code>task_id         = "tache-7f3c2a"              (tâche racine; valeur abrégée, UUIDv4 en production)
step_id         = "etape-02/reserver-stock#1"  (chemin dans le plan, indice d’itération)
cle             = hex( SHA-256( JCS( ["idem-v1", task_id, step_id] ) ) )</code></pre>''',
     ['10-25']),
    # [10-12] ORC-21 : opération racine, itérations, bifurcations, étape incertaine (A-07, A-09)
    ('''<p>Chaque appel d’outil en écriture (P2 ou P3) <strong>DOIT</strong> porter une clé d’idempotence dérivée de l’identifiant de la tâche et de celui de l’étape, réutilisée telle quelle à chaque réessai. Une étape replanifiée avec d’autres arguments reçoit un nouvel identifiant d’étape, donc une nouvelle clé.''',
     '''<p>Chaque appel d’outil en écriture (P2 ou P3) <strong>DOIT</strong> porter une clé d’idempotence dérivée d’un identifiant d’opération racine stable de bout en bout et de l’identifiant de l’étape, réutilisée telle quelle à chaque réessai. L’identifiant racine est celui de la tâche de l’appelant d’origine, propagé dans le message de délégation (EXIG-ORC-23) et, pour un événement, le couple (<code>source</code>, <code>id</code>). L’identifiant d’étape encode le chemin de l’étape dans le plan et l’indice d’itération; une bifurcation par voyage dans le temps reçoit un nouvel espace de clés. La clé est l’empreinte de la canonisation RFC 8785 d’un objet, et non d’une concaténation, et l’identifiant racine est aléatoire (UUIDv4 ou équivalent). Une étape replanifiée avec d’autres arguments reçoit un nouvel identifiant d’étape, donc une nouvelle clé; une étape dont l’issue est incertaine <strong>NE DOIT PAS</strong> être replanifiée avant sa résolution (EXIG-ORC-16).''',
     ['10-12', '10-25']),
    # [10-11, 10-13] ORC-22 : mode de vérification déclaré, adaptateur admis sous condition, rétention bornée (A-09)
    ('''<p>Tout outil P2 ou P3 inscrit au catalogue <strong>DOIT</strong> vérifier la clé côté serveur, directement ou par son adaptateur : un doublon ne produit aucun effet supplémentaire; une clé réutilisée avec des arguments différents est rejetée; une requête dont l’original est encore en cours est refusée sans exécution. Ce comportement''',
     '''<p>Tout outil P2 ou P3 inscrit au catalogue <strong>DOIT</strong> déclarer au catalogue l’argument qui porte sa clé d’idempotence et son mode de vérification : (a) natif, la clé étant vérifiée par le système d’enregistrement; (b) par adaptateur, avec un registre de clés durable mis à jour dans la même transaction que l’effet, ou complété par une requête d’état qui constate l’effet par une référence externe dérivée de la clé. Un outil sans (a) ni (b) est classé P3, n’est jamais réessayé automatiquement, et une issue inconnue y déclenche une réconciliation humaine. La vérification garantit qu’un doublon ne produit aucun effet supplémentaire, qu’une clé réutilisée avec des arguments différents est rejetée et qu’une requête dont l’original est encore en cours est refusée sans exécution. Le service <strong>DOIT</strong> permettre d’interroger l’état d’une clé et <strong>DEVRAIT</strong> permettre de la révoquer; les clés sont cloisonnées par client. Leur durée de conservation, déclarée au catalogue, <strong>DOIT</strong> couvrir la durée de vie maximale de la tâche durable (EXIG-ORC-26), plus la fenêtre de reprise et le délai de réconciliation; une reprise depuis un point de contrôle plus ancien que cette durée est interdite (EXIG-ARC-06). Ce comportement''',
     ['10-11', '10-13']),
    ('''<div id="pourquoi-642"><p>Pourquoi : seul le système visé sait si l’effet a déjà eu lieu<strong><sup>[78]</sup></strong>.</p></div>''',
     '''<div id="pourquoi-642"><p>Pourquoi : seul le système visé sait si l’effet a déjà eu lieu, et le brouillon laisse au serveur la durée de conservation des clés<strong><sup>[78]</sup></strong>; la déduplication ne vaut que pendant cette durée.</p></div>''',
     ['10-11', '10-13']),

    # ------------------------------------------------------------------ § 7.7
    # [10-20, 10-21, 10-33, 12-07] exemple de délégation : référence au lieu du jeton, identifiants de clé, palier, échéance absolue
    ('''  "jeton_delegue": "&lt;jeton délégué du mandant, audience = agent-credit&gt;",''',
     '''  "delegation": "&lt;référence de délégation; jeton délégué en en-tête, hors message&gt;",
  "tache_racine": "tache-7f3c2a", "etape": "etape-04/evaluer-solvabilite#1", "palier_max": "P1",''',
     ['10-20', '10-21', '12-07']),
    ('''"appels_outils": 10, "echeance": "PT10M" },''',
     '''"appels_outils": 10, "echeance": "2026-10-27T14:13:12Z" },''',
     ['10-33']),
    # [10-20, 10-21, 10-22] ORC-23 : jeton en en-tête (A-15), identifiants racine, palier, niveau et classe de la chaîne (A-16)
    ('''<p>Une délégation <strong>DOIT</strong> transmettre un message structuré limité au sous-objectif, aux critères d’acceptation, aux paramètres requis, aux références d’artefacts, au jeton délégué du mandant (section 9.3), au contexte de trace (section 10.1), au budget restant et au schéma de retour attendu. L’historique brut''',
     '''<p>Une délégation <strong>DOIT</strong> transmettre un message structuré limité au sous-objectif, aux critères d’acceptation, aux paramètres requis, aux références d’artefacts, à la référence de délégation (section 9.3), à l’identifiant de la tâche racine et à celui de l’étape qui délègue, dont l’exécutant dérive ses propres clés d’idempotence (EXIG-ORC-21), au palier maximal autorisé, au contexte de trace (section 10.1), au budget restant, au schéma de retour attendu et, pour une tâche fortement couplée, à un registre structuré des décisions prises. Le jeton délégué voyage dans l’en-tête d’authentification du transport (A2A, MCP), injecté par le code d’exécution ou par la passerelle; il <strong>NE DOIT PAS</strong> figurer dans le message, dans un point de contrôle, dans un journal ni dans le contexte du modèle (EXIG-IAM-06). Le niveau d’autonomie et la classe les plus contraignants de la chaîne voyagent dans le contexte de délégation et s’imposent à l’exécutant (EXIG-AUT-10). L’historique brut''',
     ['10-20', '10-21', '10-22']),
    # [10-34] ORC-25 : lecture sous l'intersection des droits; schéma déclassifié pour un agent à frontière distincte; étiquettes (A-17)
    ('''<p>Chaque agent <strong>DOIT</strong> filtrer ses résultats selon les droits du mandant, de sorte qu’aucune donnée inaccessible à ce mandant ne remonte à l’orchestrateur ni à l’utilisateur. Les garde-fous de contenu s’appliquent à l’entrée, aux appels d’outils, aux réponses d’outils et à la sortie finale; le contenu reçu d’un autre agent est traité comme une donnée non fiable (section 9.6).</p>''',
     '''<p>Chaque agent <strong>DOIT</strong> lire sous l’intersection des droits du mandant et de sa propre portée (section 9.3) et filtrer ses résultats selon les droits du mandant, de sorte qu’aucune donnée inaccessible à ce mandant ne remonte à l’orchestrateur ni à l’utilisateur. Un agent qui lit sous ses propres droits, derrière une frontière de sécurité distincte, <strong>DOIT</strong> rendre un schéma de retour dont les champs, déclarés à la fiche, sont accessibles au mandant. Les garde-fous de contenu s’appliquent à l’entrée, aux appels d’outils, aux réponses d’outils et à la sortie finale; le contenu reçu d’un autre agent est traité comme une donnée non fiable et porte les étiquettes de sa session d’origine (section 9.6).</p>''',
     ['10-34']),

    # ------------------------------------------------------------------ § 7.8
    # [10-10, 10-19] ORC-26 : réessais comptés; réserve de compensation hors plafonds (A-06)
    ('''L’atteinte d’un plafond <strong>DOIT</strong> arrêter la boucle en état sûr et déclencher l’escalade prévue; elle <strong>NE DOIT PAS</strong> être rapportée comme un succès.</p>''',
     '''L’atteinte d’un plafond <strong>DOIT</strong> arrêter la boucle en état sûr et déclencher l’escalade prévue; elle <strong>NE DOIT PAS</strong> être rapportée comme un succès. Les réessais comptent dans ces plafonds. L’arrêt au plafond agit vers l’avant : les compensations des étapes exécutées puisent dans une réserve de budget calculée à la conception, hors de ces plafonds (EXIG-ORC-31).</p>''',
     ['10-10', '10-19']),
    # [10-19, 10-35, 10-36] ORC-27 : gigue, borne, couche unique, décompte; contexte nécessaire à la reprise (A-09)
    ('''<strong>DOIT</strong> être protégée par un délai d’expiration, des réessais à temporisation exponentielle <em>(exponential backoff)</em> limités aux erreurs transitoires et un disjoncteur. Les erreurs sont remontées et journalisées, jamais masquées. Le repli prévu (modèle de repli homologué, service dégradé ou file humaine nommée recevant le contexte complet) est testé avant la production.</p>''',
     '''<strong>DOIT</strong> être protégée par un délai d’expiration, par des réessais à temporisation exponentielle avec gigue <em>(exponential backoff with jitter)</em>, limités aux erreurs transitoires, en nombre borné et déclaré (<code>maximumAttempts</code> pour une activité Temporal à effet, dont les tentatives sont illimitées par défaut), portés par une seule couche par dépendance et comptés dans les plafonds de l’EXIG-ORC-26, et par un disjoncteur. Les erreurs sont remontées et journalisées, jamais masquées. Le repli prévu (modèle de repli homologué, service dégradé ou file humaine nommée recevant le contexte nécessaire à la reprise, sous les droits du mandant) est testé avant la production.</p>''',
     ['10-19', '10-36']),
    ('''la temporisation exponentielle et la limitation aux erreurs transitoires sont des choix du cadre<strong><sup>[9]</sup></strong>.</p>''',
     '''la temporisation exponentielle, la gigue, la borne des tentatives, la couche unique, la limitation aux erreurs transitoires et le disjoncteur obligatoire sont des choix du cadre (PRIN-12)<strong><sup>[9]</sup></strong>.</p>''',
     ['10-35', '10-19']),
    # [10-02, 10-37] ORC-28 : arrêt vers l'avant, canal de compensation (A-06), exercice unique et cible (A-05)
    ('''L’arrêt bloque toute nouvelle étape, conserve l’état pour analyse et laisse les sagas en cours dans un état connu, suspendues ou compensées selon la procédure. Un exercice d’arrêt <strong>DOIT</strong> avoir lieu au moins une fois par trimestre et son délai mesuré <strong>DOIT</strong> être consigné.</p>''',
     '''L’arrêt agit vers l’avant : il bloque toute nouvelle étape métier et conserve l’état pour analyse. Les compensations des sagas en cours s’exécutent par le canal de compensation (EXIG-ORC-31), que l’arrêt ne ferme pas sauf décision distincte; une saga passée au pivot termine ses étapes réessayables par ce canal ou passe en file humaine. La suspension de sécurité est immédiate; la suspension administrative bloque les nouvelles tâches après avis préalable. La compensation automatique vise les sagas en cours; la réparation des actions terminées est une décision du propriétaire métier (section 12.8). L’arrêt <strong>DOIT</strong> être exercé au moins une fois par trimestre, dans l’exercice de l’EXIG-SEC-26 : l’arrêt ciblé en production, l’arrêt global dans un environnement représentatif. Le délai mesuré <strong>DOIT</strong> être consigné et comparé à la cible de l’EXIG-IAM-20.</p>''',
     ['10-02', '10-37']),
    ('''<p>Pourquoi : le RIA prévoit l’interruption sûre des systèmes à haut risque (art. 14(4)e)) et le NIST AI RMF, d’usage volontaire, demande des mécanismes pour désactiver un système (MANAGE 2.4), le cadre l’appliquant à tous les agents<strong><sup>[99, 290]</sup></strong>; la fréquence trimestrielle est un choix du cadre.</p></div>
</div>''',
     '''<p>Pourquoi : le RIA prévoit l’interruption sûre des systèmes à haut risque (art. 14(4)e)) et le NIST AI RMF, d’usage volontaire, demande des mécanismes pour désactiver un système (MANAGE 2.4), le cadre l’appliquant à tous les agents<strong><sup>[99, 412]</sup></strong>; la fréquence trimestrielle et l’arrêt vers l’avant sont des choix du cadre.</p></div>
</div>
<div id="exig-orc31">
<p><strong><code>EXIG-ORC-31</code> · DOIT</strong></p>
<p><strong>Canal de compensation</strong></p>
<p>Les compensations <strong>DOIVENT</strong> s’exécuter sous une identité de compensation propre à l’orchestrateur de la saga, ou au coordinateur de saga en chorégraphie, distincte de celle de l’agent et inscrite au registre. Cette identité n’est autorisée qu’aux outils de compensation déclarés au catalogue pour une étape inscrite comme exécutée au journal de compensation de la même tâche (EXIG-ORC-16). Elle passe toujours par la passerelle ou par le courtier d’événements, et chaque appel est audité. Elle n’est touchée ni par le coupe-circuit, ni par la suspension, ni par la révocation de l’agent, ni par l’épuisement de son enveloppe, ni par le plafond de sauts, ni par l’échéance de son mandat. Elle dispose d’une réserve de budget calculée à la conception, hors de l’enveloppe de l’agent. Elle <strong>PEUT</strong> être suspendue par une décision distincte, motivée et journalisée. Si la passerelle est indisponible, la compensation entre dans une file persistée, et l’EXIG-ORC-18 s’applique à l’échéance fixée à la fiche.</p>
<div id="pourquoi-orc31"><p>Pourquoi : chaque arrêt du cadre bloque tout appel de l’identité visée; sans canal distinct, il laisserait à moitié exécutée la saga qu’il interrompt, contre PRIN-12. Choix du cadre.</p></div>
</div>''',
     ['10-02', '10-10', '12-18']),
    ('''<p>Le dernier recours est l’arrêt. Pour les systèmes à haut risque, le règlement européen sur l’IA prévoit la possibilité d’interrompre le système de façon sûre (art. 14(4)e))<strong><sup>[290]</sup></strong>;''',
     '''<p>Le dernier recours est l’arrêt. Pour les systèmes à haut risque, le règlement européen sur l’IA prévoit la possibilité d’interrompre le système de façon sûre (art. 14(4)e))<strong><sup>[412]</sup></strong>;''',
     ['11-31']),

    # ------------------------------------------------------------------ § 7.9
    # [10-39] tableau 26 : la cellule ne cite que ce qu'exige l'EXIG-ORC-05
    ('''<td>Critères concrets, tests négatifs, suite complète (EXIG-ORC-05)</td>''',
     '''<td>Critères vérifiables, vérifications déterministes d’abord, évaluateur distinct (EXIG-ORC-05)</td>''',
     ['10-39']),

    # ------------------------------------------------------------------ § 7.10
    # [10-16] tableau 27 : granularité de persistance de LangGraph et de MAF
    ('''<td>Nœud réexécuté à la reprise; magasin persistant exigé en production<strong><sup>[82, 124]</sup></strong></td>''',
     '''<td>Nœud réexécuté à la reprise; magasin persistant exigé en production<strong><sup>[82, 124]</sup></strong>; granularité de persistance à aligner sur l’EXIG-ORC-11 (un appel à effet par nœud)</td>''',
     ['10-16']),
    ('''<td>Magasin de points de contrôle à protéger comme frontière de confiance<strong><sup>[105]</sup></strong></td>''',
     '''<td>Magasin de points de contrôle à protéger comme frontière de confiance<strong><sup>[105]</sup></strong>; point de contrôle par étape de calcul du flux : granularité à aligner sur l’EXIG-ORC-11</td>''',
     ['10-16']),
    # [10-29, 10-19] tableau 27 : limites de Temporal
    ('''<td>Isoler appels de modèles et d’outils dans des activités (EXIG-ORC-12)</td>''',
     '''<td>Isoler appels de modèles et d’outils dans des activités (EXIG-ORC-12); historique borné : Continue-As-New et passage par référence; <code>maximumAttempts</code> sur les activités à effet (EXIG-ORC-27)</td>''',
     ['10-29', '10-19']),
    # [10-24] ORC-30 : capacités propres au chapitre 7
    ('''la prise en charge de MCP et d’A2A, nativement ou par adaptateur; l’export des définitions de flux et de l’état dans un format documenté.</p>''',
     '''la prise en charge de MCP et d’A2A, nativement ou par adaptateur; l’export des définitions de flux et de l’état dans un format documenté; la propagation d’une clé d’idempotence stable (EXIG-ORC-21); l’exécution des compensations et de l’escalade de saga (tests de l’EXIG-ORC-20); les plafonds par exécution (EXIG-ORC-26); l’arrêt ciblé et global (EXIG-ORC-28).</p>''',
     ['10-24']),

    # ------------------------------------------------------------------ § 8.1
    # [11-32] prévision d'analyste
    ('''<p>Deux constats la fondent.''', '''<p>Deux arguments la fondent.''', ['11-32']),
    ('''la firme prévoit que, d’ici 2027, 40 % des entreprises rétrograderont''',
     '''la firme prévoit, dans un communiqué sans méthode publiée, que, d’ici 2027, 40 % des entreprises rétrograderont''',
     ['11-32']),
    # [11-14] N3 et N4 : l'origine de la tâche les départage (A-27)
    ('''<p>Chaque niveau se définit donc par deux éléments observables : le rôle de la personne et l’étendue de ce que l’agent peut faire sans approbation.''',
     '''<p>Chaque niveau se définit donc par deux éléments : le rôle de la personne et l’étendue de ce que l’agent peut faire sans approbation. Le second s’observe appel par appel. N4 se distingue en outre de N3 par l’origine de la tâche, déclenchée sans demande d’une personne (événement, horaire), que la passerelle lit dans un attribut posé par l’orchestrateur ou par le courtier.''',
     ['11-14']),
    # [11-19] figure 14 contre tableau 28 (figure non modifiable)
    ('''plus l’autonomie croît, plus les contrôles compensatoires s’accumulent. Le niveau NX, hors de l’échelle, est interdit.''',
     '''plus l’autonomie croît, plus les contrôles compensatoires s’accumulent. Le niveau NX, hors de l’échelle, est interdit. En cas d’écart entre la figure et le tableau 28, le tableau fait foi : approbation hors bande des P3 dès N2, retour arrière rapide dès N3; la DLP indiquée en N1 n’est pas un contrôle minimal.''',
     ['11-19']),
    # [11-26] tableau 28, N0 (A-27)
    ('''<td>Aucun modèle : flux codé, règles, RPA, API.</td>''',
     '''<td>Aucun choix d’action laissé à un modèle : le code fixe chaque pas (flux codé, règles, RPA, API); un modèle peut transformer une donnée sans choisir l’action. N0 qualifie un flux, non un agent.</td>''',
     ['11-26']),
    # [11-13] tableau 28, N2 : ce qui distingue l'approbation P2 de l'approbation P3 (A-12)
    ('''<td>P0, P1; P2 et P3 après approbation signée (P3 : hors bande)</td>''',
     '''<td>P0, P1; P2 après approbation signée (service d’approbation, même appareil admis); P3 après approbation signée hors bande (EXIG-AUT-09)</td>''',
     ['11-13']),
    # [11-14] tableau 28, N4 : origine de la tâche (A-27)
    ('''<td>S’autodéclenche sur des événements et opère en continu.</td>''',
     '''<td>Traite des tâches déclenchées sans demande d’une personne (événement, horaire) et opère en continu, dans un ODD certifié. La passerelle lit l’origine de la tâche et refuse une tâche ainsi déclenchée pour un agent qui n’est pas N4.</td>''',
     ['11-14']),
    # [11-26, 11-14] AUT-01 : N1 à N4; contrôle de N4 à l'origine de la tâche
    ('''<p>Chaque agent <strong>DOIT</strong> avoir un niveau d’autonomie N0 à N4 (tableau 28) inscrit au registre''',
     '''<p>Chaque agent <strong>DOIT</strong> avoir un niveau d’autonomie N1 à N4 (tableau 28; N0 qualifie un flux déterministe, non un agent) inscrit au registre''',
     ['11-26']),
    ('''La passerelle d’agents <strong>DOIT</strong> refuser tout appel d’outil qui excède ce plafond.</p>''',
     '''La passerelle d’agents <strong>DOIT</strong> refuser tout appel d’outil qui excède ce plafond, ainsi que toute tâche déclenchée sans demande d’une personne pour un agent qui n’est pas N4, d’après l’attribut d’origine posé par l’orchestrateur ou par le courtier.</p>''',
     ['11-14']),
    # [11-31] RIA, art. 14 : source de la Commission plutôt que l'agrégateur
    ('''au niveau d’autonomie et au contexte d’utilisation (art. 14, par. 3)<strong><sup>[290]</sup></strong>;''',
     '''au niveau d’autonomie et au contexte d’utilisation (art. 14, par. 3)<strong><sup>[412]</sup></strong>;''',
     ['11-31']),
    # [11-29] AUT-04 : repli à la sortie du domaine, niveau 4 de SAE
    ('''<p>Pourquoi : SAE J3016 distingue ses niveaux 3 et 4 par la partie qui assure le repli hors du domaine<strong><sup>[304]</sup></strong>; le RIA prévoit l’arrêt du système dans un état sûr (art. 14, par. 4, al. e)<strong><sup>[290]</sup></strong>''',
     '''<p>Pourquoi : SAE J3016 distingue ses niveaux 3 et 4 par la partie qui assure le repli à la sortie du domaine; le repli assuré par le système, qu’exige la présente exigence, est celui de son niveau 4<strong><sup>[304]</sup></strong>; le RIA prévoit l’arrêt du système dans un état sûr (art. 14, par. 4, al. e)<strong><sup>[412]</sup></strong>''',
     ['11-29', '11-31']),
    # [11-27, 11-15, 11-26] AUT-05 : déclencheurs à l'EXIG-GOV-12 (A-24); ni rétrogradation de masse, ni N0 présumé
    ('''puis réévalué à chaque changement de modèle ou de version de modèle, d’invite système (hors correction purement typographique attestée sans effet sur le jeu d’évaluation), d’outil en écriture, de population visée ou d’ODD. Tant que la réévaluation n’est pas faite, l’agent <strong>DOIT</strong> fonctionner au niveau immédiatement inférieur à son niveau déclaré; un agent de niveau N1 est suspendu ou ramené à un flux déterministe sans autonomie (N0).</p>''',
     '''puis réévalué avant la mise en service de tout changement visé par l’EXIG-GOV-12, qui fait foi pour la liste des déclencheurs (une correction purement typographique de l’invite système, attestée sans effet sur le jeu d’évaluation, n’en est pas un). Tant que la réévaluation n’est pas faite, la version antérieure reste en service; à défaut, l’agent <strong>DOIT</strong> être suspendu, ou remplacé par le flux déterministe de repli s’il existe. Un changement ne permet jamais de fonctionner au-dessus du plafond de classe. La version de modèle servie est épinglée et vérifiée par la passerelle de modèles.</p>''',
     ['11-27', '11-15', '11-26']),
    # [11-28] tableau 29 : Feng et al. indicatif dans les deux phrases; « approbateur » sur exception
    ('''Les correspondances avec Gartner, AWS et Feng et al. reposent sur les sources citées sous le tableau; celles avec Morris et al. et SAE J3016 sont indicatives, car ces échelles mesurent autre chose que le rôle de la personne.''',
     '''Les correspondances avec Gartner et AWS reposent sur les sources citées sous le tableau; celles avec Feng et al., Morris et al. et SAE J3016 sont indicatives, car ces échelles décrivent le rôle de l’utilisateur ou un autre objet que le plafond d’actions sans approbation.''',
     ['11-28']),
    ('''Les libellés L1 à L5 sont ceux de Feng et al.</p>''',
     '''Les libellés L1 à L5 sont ceux de Feng et al.; leur « approbateur » (L4) n’intervient que lorsque l’agent le sollicite, ce qui le rapproche de N3 plutôt que de N2.</p>''',
     ['11-28']),
    # [11-29] tableau 29, N3 : le repli des N3 est celui du niveau 4 de SAE
    ('''<td>Niveau 3 : l’humain reprend la main</td>''',
     '''<td>Niveaux 3 et 4 : une personne supervise, comme au niveau 3, mais le repli est assuré par le système, comme au niveau 4 (EXIG-AUT-04)</td>''',
     ['11-29']),
    # [11-29] SAE : révision non vérifiée (retirée), repli « à la sortie du domaine »
    ('''et non une norme de sécurité; sa révision en vigueur est J3016_202609. Le cadre''',
     '''et non une norme de sécurité. Le cadre''',
     ['11-29']),
    ('''de son niveau 4, où le système assure lui-même le repli dans son domaine;''',
     '''de son niveau 4, où le système assure lui-même le repli à la sortie de son domaine;''',
     ['11-29']),

    # ------------------------------------------------------------------ § 8.2
    # [11-11] tableau 30 : vocabulaire unifié; valeur plafonnante de la détection; AUT-07 cas extrême
    ('''<td>Un rayon large abaisse le niveau ou impose des seuils plus bas.</td>''',
     '''<td>Un rayon élevé abaisse le niveau ou impose des seuils plus bas.</td>''',
     ['11-11']),
    ('''<td>Une détection lente impose un contrôle avant l’action (N2) plutôt qu’après.</td>''',
     '''<td>Une détection lente plafonne à N2 (contrôle avant l’action plutôt qu’après), quels que soient les autres critères; l’EXIG-AUT-07 en est le cas extrême.</td>''',
     ['11-11']),
    ('''Un agent de facturation peut modifier 10 000 comptes par exécution (rayon large).''',
     '''Un agent de facturation peut modifier 10 000 comptes par exécution (rayon élevé).''',
     ['11-11']),
    # [11-18] AUT-06 : les actions accessibles après approbation comptent
    ('''<p>L’évaluation des quatre critères <strong>DOIT</strong> se fonder sur les permissions effectives de l’agent (outils autorisés, portées des jetons, plafonds de volume et de montant), et non sur l’intention déclarée.''',
     '''<p>L’évaluation des quatre critères <strong>DOIT</strong> se fonder sur les permissions effectives de l’agent (outils autorisés, portées des jetons, plafonds de volume et de montant), y compris les actions qui ne lui sont accessibles qu’après approbation, et non sur l’intention déclarée.''',
     ['11-18', '11-17']),
    # [11-31] AUT-06 : communiqué de Gartner (source A) au lieu de l'article de presse
    ('''<p>Pourquoi : Gartner situe la cause de nombreux échecs dans la confusion entre la capacité d’agir et la portée des accès accordés<strong><sup>[305]</sup></strong>;''',
     '''<p>Pourquoi : Gartner situe la cause de nombreux échecs dans la confusion entre la capacité d’agir et la portée des accès accordés<strong><sup>[95]</sup></strong>;''',
     ['11-31']),
    # [11-12] AUT-07 : un seuil non approuvé est réputé atteint (fermeture par défaut)
    ('''<strong>NE DOIT PAS</strong> être autorisé au-delà de N2, quels que soient ses résultats aux bancs d’essai.</p>''',
     '''<strong>NE DOIT PAS</strong> être autorisé au-delà de N2, quels que soient ses résultats aux bancs d’essai. En l’absence de seuil approuvé pour un critère, ce critère est réputé atteint.</p>''',
     ['11-12']),

    # ------------------------------------------------------------------ § 8.3
    # [11-16] tableau 31, P0 : outil dont les arguments quittent l'entreprise (A-17)
    ('''<td>Identité de charge de travail, limitation de débit, journalisation de l’usage.</td>''',
     '''<td>Identité de charge de travail, limitation de débit, journalisation de l’usage. Un outil dont un argument quitte l’entreprise (requête en texte libre vers un moteur de recherche public, par exemple) porte l’attribut « sortie de données » : il compte comme outil d’envoi (EXIG-SEC-06) et comme propriété [C] (EXIG-SEC-04), et ses arguments passent un contrôle DLP.</td>''',
     ['11-16']),
    # [11-08] tableau 31, P2 : nature (A-27) et seuil mesuré (A-13)
    ('''<td>Écriture réversible ou compensable, impact modéré</td>''',
     '''<td>Écriture réversible, ou compensable vers un état métier équivalent, à impact borné; jamais un effet irréversible ou externe</td>''',
     ['11-08']),
    ('''seuil métier au catalogue (p. ex. 5 000 $); approbation au-delà du seuil.</td>''',
     '''seuil métier au catalogue (p. ex. 5 000 $), mesuré sur une grandeur que l’agent ne choisit pas, avec sa portée et sa fenêtre (EXIG-AUT-24); approbation au-delà du seuil.</td>''',
     ['11-08']),
    # [11-01, 11-16, 10-05] AUT-08 : irréversible = P3 (A-27); palier des compensations; schémas P2-P3 (A-11); sortie de données
    ('''Un outil qui combine plusieurs effets prend le palier le plus élevé; un outil d’écriture sans compensation déclarée est classé P3.</p>''',
     '''Un outil qui combine plusieurs effets prend le palier le plus élevé; un outil d’écriture sans compensation déclarée est classé P3. Un effet irréversible ou externe est P3, même si une compensation est déclarée; P2 suppose une écriture réversible, ou compensable vers un état métier équivalent avec un impact borné. Un outil de compensation reçoit son propre palier (EXIG-ORC-17). Dans les schémas des outils P2 et P3, les montants et les identifiants sont des chaînes ou des entiers en unités mineures. Un outil dont un argument peut atteindre une destination hors du périmètre de confiance porte au catalogue l’attribut « sortie de données », indépendant du palier (EXIG-SEC-06).</p>''',
     ['11-01', '12-05', '11-16', '10-05']),
    # [11-13, 11-30] AUT-09 : hors bande en DOIT (A-12); ASI02 au lieu d'ASI09
    ('''<p>Un agent <strong>NE DOIT PAS</strong> exécuter un outil P3 sans une approbation humaine préalable, propre à cet appel, quel que soit son niveau d’autonomie.</p>''',
     '''<p>Un agent <strong>NE DOIT PAS</strong> exécuter un outil P3 sans une approbation humaine préalable, propre à cet appel et obtenue hors bande, c’est-à-dire sur un appareil et dans une session distincts de ceux de l’agent, avec une authentification forte résistante à l’hameçonnage, quel que soit son niveau d’autonomie. La compensation déclarée d’une étape approuvée est couverte par l’approbation de l’étape (EXIG-AUT-12).</p>''',
     ['11-13', '12-10', '10-05']),
    ('''l’OWASP range l’absence de confirmation des actions sensibles parmi les vulnérabilités (ASI09)<strong><sup>[28, 76, 291]</sup></strong>.</p>''',
     '''l’OWASP recommande l’approbation explicite des actions à fort impact (ASI02)<strong><sup>[28, 76, 291]</sup></strong>. Le caractère hors bande est un choix du cadre.</p>''',
     ['11-30', '11-13']),

    # ------------------------------------------------------------------ § 8.4
    # [11-20, 11-06] figure 15 : contrôles du palier en sus, revue a posteriori, cellules P2 (figure non modifiable)
    ('''la cellule donne le contrôle minimal. Le niveau d’autonomie de l’agent et les déclencheurs d’approbation peuvent le rendre plus strict, jamais plus souple.''',
     '''la cellule donne le contrôle minimal, en plus des contrôles obligatoires du palier (tableau 31). « Audit + revue » désigne une revue a posteriori par échantillonnage; les cellules P2 des classes faible et modérée énoncent la même règle (approbation au-delà du seuil déclaré). Le niveau d’autonomie de l’agent et les déclencheurs d’approbation peuvent rendre le contrôle plus strict, jamais plus souple; il se calcule selon l’EXIG-AUT-10.''',
     ['11-20', '11-06']),
    # [11-07] règle de deux : formulation de Meta pour [B] (audit_lit, ligne 55)
    ('''un agent ne devrait pas cumuler l’exposition à des entrées non fiables, l’accès à des données sensibles et la capacité de changer d’état''',
     '''un agent ne devrait pas cumuler l’exposition à des entrées non fiables, l’accès à des systèmes sensibles ou à des données privées et la capacité de changer d’état''',
     ['11-07']),
    # [11-06, 11-07, 11-09] AUT-10 : union des contrôles, ordre des approbations, chaîne de délégation, déclencheur aligné sur SEC-04 (A-14, A-16, A-17)
    ('''<p>Pour chaque appel d’outil, la passerelle d’agents <strong>DOIT</strong> déterminer le contrôle exigé en retenant le plus strict des éléments suivants : la cellule classe × palier de la figure 15, le niveau d’autonomie de l’agent et les déclencheurs d’approbation (comportement atypique, dépassement de seuil, cumul de contenu non fiable, de données sensibles et d’action externe). Elle consigne''',
     '''<p>Pour chaque appel d’outil, la passerelle d’agents, que traversent tout appel MCP et toute action P2 ou P3 (EXIG-ARC-01), <strong>DOIT</strong> déterminer le contrôle exigé. Ce contrôle est l’union des contrôles exigés par la cellule classe × palier de la figure 15, par le niveau d’autonomie et la classe les plus contraignants de la chaîne de délégation (EXIG-ORC-23), par les déclencheurs d’approbation (comportement atypique, seuil de l’EXIG-AUT-24, cumul de la règle de deux au sens de l’EXIG-SEC-04 : contenu non fiable, données sensibles et changement d’état ou communication externe) et par les points non dérogeables (EXIG-GOV-17). Les contrôles techniques (jeton délégué, masquage, filtrage par ligne, audit) se cumulent; aucun n’en remplace un autre. Entre exigences d’approbation, l’ordre est : refus, approbation hors bande à deux approbateurs, approbation hors bande, approbation, exécution automatique avec revue a posteriori, exécution automatique; le plus strict est le premier de cette liste. Elle consigne''',
     ['11-06', '11-07', '11-09']),
    ('''<p>Pourquoi : retenir le plus strict des éléments empêche qu’un agent peu autonome''',
     '''<p>Pourquoi : cumuler les contrôles et retenir l’approbation la plus forte empêche qu’un agent peu autonome''',
     ['11-06']),
    # [11-10] AUT-11 : dépendances, cache non échu, refus selon le contrôle calculé (A-04, A-06, A-19)
    ('''<p>Si le service d’approbation, le catalogue ou le service de politiques est indisponible, ou si aucune politique ne couvre l’action demandée, la passerelle <strong>DOIT</strong> refuser tout appel P3 et tout appel P2 au-delà du seuil, sans préjudice du refus général de tout appel dépourvu de décision de politique valide (EXIG-IAM-18). Dans tous ces cas, l’orchestrateur <strong>DOIT</strong> suspendre la tâche dans un état reprenable.</p>''',
     '''<p>Le service d’approbation, le catalogue, le service de politiques, le registre des jti et le service d’audit sont des dépendances de la passerelle; une politique ou un instantané du catalogue distribués et non échus valent service disponible (EXIG-IAM-22). Si l’une de ces dépendances est indisponible, ou si aucune politique ne couvre l’action demandée, la passerelle <strong>DOIT</strong> refuser tout appel dont le contrôle calculé (EXIG-AUT-10) exige une approbation, donc au moins tout appel P3 et tout appel P2 au-delà du seuil, ainsi que tout appel P2 ou P3 si le service d’audit est indisponible. Une politique ou un instantané échus ne laissent passer que les appels P0. Ces refus sont sans préjudice du refus général de tout appel dépourvu de décision de politique valide (EXIG-IAM-18). Dans tous ces cas, l’orchestrateur <strong>DOIT</strong> suspendre la tâche dans un état reprenable; une compensation refusée pour l’un de ces motifs entre dans la file persistée de l’EXIG-ORC-31.</p>''',
     ['11-10']),
    # [11-08] nouvelle EXIG-AUT-24 (A-13), placée à la fin du § 8.4
    ('''si les superviseurs sont injoignables ou si aucune politique n’existe pour l’action tentée<strong><sup>[76]</sup></strong>.</p></div>
</div>''',
     '''si les superviseurs sont injoignables ou si aucune politique n’existe pour l’action tentée<strong><sup>[76]</sup></strong>.</p></div>
</div>
<div id="exig-aut24">
<p><strong><code>EXIG-AUT-24</code> · DOIT</strong></p>
<p><strong>Grandeur, unité, portée et fenêtre des seuils</strong></p>
<p>Chaque seuil inscrit au catalogue <strong>DOIT</strong> déclarer : une grandeur dérivée de l’effet, calculée par la passerelle à partir des arguments canonisés (la somme des lignes d’une commande, par exemple) ou fournie par le système visé, jamais un argument redondant déclaré par l’agent; son unité; sa portée (appel, tâche, agent, mandant ou contrepartie); sa fenêtre. La passerelle tient les compteurs dans un magasin à cohérence forte, et un compteur illisible impose le refus. La valeur du seuil est fixée au catalogue seulement; la fiche ne peut fixer qu’une valeur plus stricte. Tant que le comité n’a pas approuvé les seuils d’étalonnage de l’EXIG-AUT-07, l’outil est traité comme s’il les dépassait. Des contraintes par argument (bénéficiaires admis, plages de valeurs) <strong>PEUVENT</strong> s’y ajouter au catalogue.</p>
<div id="pourquoi-aut24"><p>Pourquoi : un seuil ne borne l’agent que si la grandeur mesurée échappe à son contrôle; sans portée ni fenêtre, dix appels sous le seuil en font un au-delà. Choix du cadre.</p></div>
</div>''',
     ['11-08']),

    # ------------------------------------------------------------------ § 8.5
    # [11-22, 12-06, 11-01, 12-05] h : canonisation d'un objet; I-JSON; ce que h atteste (A-11)
    ('''<p>L’empreinte se calcule ainsi : h = SHA-256(identifiant de l’outil ‖ arguments canonisés), où l’identifiant de l’outil est pleinement qualifié (serveur, nom et version épinglée).''',
     '''<p>L’empreinte se calcule ainsi : h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments})), c’est-à-dire l’empreinte de la canonisation d’un objet qui réunit l’identifiant pleinement qualifié de l’outil (serveur et nom), sa version épinglée, l’empreinte de sa définition, les identifiants de l’agent et de la tâche, et les arguments; la canonisation d’un objet évite l’ambiguïté d’une concaténation.''',
     ['11-22', '12-06']),
    ('''l’empreinte recalculée par la passerelle ne correspond plus et l’appel est refusé. Un exemple de jeton figure à l’annexe C.</p>''',
     '''l’empreinte recalculée par la passerelle ne correspond plus et l’appel est refusé. Cette propriété suppose que la passerelle rejette tout argument non conforme à I-JSON (RFC 7493 : clés dupliquées, nombres hors de la plage exacte d’un double, chaînes invalides) et transmette au serveur exactement la forme canonique hachée; sinon, deux analyseurs JSON peuvent lire deux actions différentes sous le même h. L’empreinte atteste que les octets transmis sont ceux qui ont été approuvés, et non que l’effet est celui qui était attendu. Un exemple de jeton figure à l’annexe C.</p>''',
     ['11-01', '12-05']),
    ('''la RFC 9396 pour décrire l’action et la RFC 8785 pour la canonisation.</p>''',
     '''la RFC 9396 pour décrire l’action et la RFC 8785 pour la canonisation. L’emploi d’<code>authorization_details</code> dans un jeton d’approbation est un profil du cadre : la RFC 9396 ne le définit que pour les jetons d’accès.</p>''',
     ['11-02']),
    # [12-08, 12-07, 11-23] figure 16 : parcours non limité aux P3; jeton conservé par la passerelle (figure non modifiable)
    ('''La passerelle intercepte l’appel P3, calcule l’empreinte de l’action et la fait approuver par une personne habilitée; le jeton signé ne vaut que pour cette empreinte, une seule fois et pendant 15 minutes au plus.''',
     '''La passerelle intercepte l’appel soumis à approbation selon l’EXIG-AUT-10 (P3, P2 au-delà du seuil, niveau N2 ou déclencheur), calcule l’empreinte de l’action et la fait approuver par une personne habilitée; le jeton signé ne vaut que pour cette empreinte, pour une seule opération et pendant 15 minutes au plus. Le dessin simplifie trois points, que l’EXIG-AUT-12 précise : à l’étape 5, le jeton est remis à la passerelle, qui le conserve, et non à l’agent; à l’étape 6, l’agent rejoue l’appel avec la même clé d’idempotence et la référence de la demande, donnée non secrète; le jeton porte aussi l’agent, l’identifiant jti et le rôle de l’approbateur, et une double approbation se fait par deux jetons sur le même h.''',
     ['12-08', '12-07', '11-23']),
    # [11-01, 11-03, 11-04, 11-05, 11-23, 12-02, 12-03, 12-04, 12-05, 12-11, 10-14, 10-05, 12-14] AUT-12 (A-08, A-10, A-11, A-12, A-14)
    ('''<p>Toute approbation exigée par la figure 15 <strong>DOIT</strong> produire un jeton signé par le service d’approbation adossé au fournisseur d’identité, contenant au minimum : l’empreinte h (SHA-256 de l’identifiant pleinement qualifié de l’outil, suivi des arguments canonisés selon la RFC 8785), l’identifiant pseudonymisé de l’approbateur, les identifiants de la tâche et de l’agent, une date d’expiration et un identifiant à usage unique. Avant l’exécution, la passerelle <strong>DOIT</strong> vérifier la signature, l’expiration et l’usage unique, puis recalculer h; toute différence annule l’approbation. Le jeton <strong>DOIT</strong> expirer au plus 15 minutes après sa signature.</p>''',
     '''<p>Toute approbation exigée par le contrôle calculé selon l’EXIG-AUT-10 <strong>DOIT</strong> produire un jeton signé par le service d’approbation adossé au fournisseur d’identité, contenant au minimum : l’émetteur et l’audience (la passerelle); l’empreinte h, SHA-256 de la canonisation selon la RFC 8785 de l’objet {outil, version, definition_digest, agent_id, task_id, arguments}, dont les arguments incluent la clé d’idempotence; l’identifiant de l’approbateur, pseudonyme stable au sein du service, et son rôle (mandant ou tiers); les identifiants de la tâche et de l’agent; une date d’expiration et un identifiant de jeton (<code>jti</code>). La double approbation se fait par deux jetons sur le même h. La passerelle <strong>DOIT</strong> rejeter tout argument non conforme à I-JSON (RFC 7493) et transmettre au serveur exactement la forme canonique hachée; elle conserve le jeton et ne le remet ni à l’agent ni à son modèle (EXIG-IAM-06). Avant l’exécution, elle <strong>DOIT</strong> vérifier la signature, l’émetteur, l’audience, l’expiration, la concordance de l’agent et de la tâche avec l’appelant authentifié, ainsi que le nombre et la distinction des approbateurs qu’exige le contrôle calculé, puis recalculer h; toute différence annule l’approbation. Le jeton couvre une seule opération : jusqu’à son expiration, la passerelle relaie toute présentation de la même opération (même appelant, même tâche, même h), et le système visé déduplique par la clé (EXIG-ORC-22); toute présentation avec une autre empreinte est refusée comme rejeu; un passage soldé par une demande de précision ou par un refus ne consomme pas le jeton. Après l’expiration, si l’issue est inconnue, la passerelle interroge le système visé par la clé : si l’effet est attesté, aucune nouvelle approbation n’est demandée; sinon, une nouvelle approbation est requise. Le registre des <code>jti</code> est partagé par toutes les instances de la passerelle, à écriture atomique, et fermé en cas d’indisponibilité (EXIG-AUT-11). La demande d’approbation d’une étape P2 ou P3 inclut l’empreinte de sa compensation déclarée, bornée au montant et aux bénéficiaires d’origine et liée à la même clé d’idempotence; cette compensation est approuvée avec l’étape. L’édition d’une action par l’approbateur est une nouvelle action : la passerelle recalcule le contrôle de l’EXIG-AUT-10 et h avant d’émettre le jeton, et celui qui a édité ne peut pas être le seul approbateur d’un appel qui en exige deux. Un outil P3 qui agit sur une ressource modifiable <strong>DEVRAIT</strong> recevoir dans ses arguments approuvés les valeurs résolues qui déterminent l’effet (bénéficiaire, montant) ou une précondition de version (version ou ETag de la ressource) vérifiée à l’exécution; à défaut, la fiche déclare le risque résiduel de modification entre l’approbation et l’exécution. Le jeton <strong>DOIT</strong> expirer au plus 15 minutes après sa signature.</p>''',
     ['11-01', '11-03', '11-04', '11-05', '11-23', '12-02', '12-03', '12-04', '12-05', '12-11', '12-14', '10-14', '10-05']),
    ('''<p>Pourquoi : un lien cryptographique entre la décision humaine et l’action exécutée détecte toute modification des arguments après l’approbation; ce mécanisme et la durée de validité sont des choix du cadre.</p>''',
     '''<p>Pourquoi : un lien cryptographique entre la décision humaine et l’action exécutée détecte toute modification des arguments après l’approbation, pourvu que la passerelle et le serveur lisent les mêmes octets; ce mécanisme, la durée de validité et la règle d’une opération par jeton, qui concilie l’approbation et le réessai idempotent, sont des choix du cadre.</p>''',
     ['11-01', '11-04']),
    # [11-25, 12-09, 12-10] AUT-14 : hors bande des P3 renvoyé à AUT-09; binding_message ramené à son rôle
    ('''<p>L’approbation d’un appel P3, ou celle que requiert un agent sans interface, <strong>DEVRAIT</strong> passer par OpenID Connect CIBA : le service d’approbation lance une demande d’authentification dorsale, l’approbateur confirme sur son propre appareil, et un <code>binding_message</code> court, affiché sur les deux appareils, rattache la demande à l’action.''',
     '''<p>L’approbation hors bande d’un appel P3 (EXIG-AUT-09), ou celle que requiert un agent sans interface, <strong>DEVRAIT</strong> passer par OpenID Connect CIBA : le service d’approbation lance une demande d’authentification dorsale, et l’approbateur confirme sur son propre appareil. Un <code>binding_message</code> court, dérivé de h ou de la tâche, affiché à l’approbateur et, si l’agent a une interface, sur celle-ci, et consigné dans la demande et dans le jeton, aide à reconnaître la demande; le lien à l’action repose sur h (EXIG-AUT-12).''',
     ['11-25', '12-09', '12-10']),
    # [11-31] WIMSE AIMS : un seul numéro pour un même brouillon
    ('''et le livre blanc de l’OpenID Foundation propose CIBA pour l’approbation humaine des agents<strong><sup>[93, 311]</sup></strong>;''',
     '''et le livre blanc de l’OpenID Foundation propose CIBA pour l’approbation humaine des agents<strong><sup>[309, 311]</sup></strong>;''',
     ['11-31']),
    # [11-21, 11-24, 12-02, 12-12, 12-13] AUT-15 : listes selon le contrôle calculé, mandant (A-12), indépendance, authentification résistante à l'hameçonnage
    ('''<p>Chaque combinaison de classe et de palier soumise à approbation <strong>DOIT</strong> avoir une liste d’approbateurs habilités, inscrite au registre. L’approbateur <strong>DOIT</strong> s’authentifier par authentification forte (au moins deux facteurs), posséder la compétence du domaine et l’autorité de refuser, et avoir été formé aux modes de défaillance des agents. Pour un appel P3 d’un agent de classe élevée, deux approbateurs distincts <strong>DOIVENT</strong> approuver, dont au moins un autre que le mandant.</p>''',
     '''<p>Chaque combinaison de classe, de palier et de motif d’approbation (cellule, niveau, déclencheur) pour laquelle le contrôle calculé selon l’EXIG-AUT-10 exige une approbation <strong>DOIT</strong> avoir une liste d’approbateurs habilités, inscrite au registre (EXIG-GOV-04). L’approbation <strong>PEUT</strong> être donnée par le mandant lui-même, comme confirmation de sa propre action, sauf pour un appel P3 d’un agent de classe élevée : deux approbateurs distincts <strong>DOIVENT</strong> alors approuver, dont au moins un qui n’est pas le mandant et ne relève ni de sa ligne hiérarchique ni du parrain de l’agent. Les approbateurs autres que le mandant sont inscrits à la liste; ils <strong>DOIVENT</strong> posséder la compétence du domaine et l’autorité de refuser, et avoir été formés aux modes de défaillance des agents. Tout approbateur <strong>DOIT</strong> s’authentifier par authentification forte (au moins deux facteurs), résistante à l’hameçonnage (FIDO2 ou WebAuthn, par exemple) pour une approbation P3. Le service d’approbation vérifie, avant de signer, que l’approbateur est habilité pour le contrôle visé, et le rôle de chaque approbateur (mandant ou tiers) est consigné à l’audit.</p>''',
     ['11-21', '11-24', '12-02', '12-12', '12-13']),
    ('''<p>Pourquoi : le RIA confie le contrôle humain des systèmes à haut risque à des personnes ayant la compétence, la formation et l’autorité nécessaires (art. 26, par. 2)<strong><sup>[94]</sup></strong>; l’IMDA demande que les superviseurs connaissent les modes de défaillance des agents<strong><sup>[76]</sup></strong>. Le second approbateur est un choix du cadre.</p>''',
     '''<p>Pourquoi : le RIA confie le contrôle humain des systèmes à haut risque à des personnes ayant la compétence, la formation et l’autorité nécessaires (art. 26, par. 2)<strong><sup>[447]</sup></strong>; l’IMDA demande que les superviseurs connaissent les modes de défaillance des agents<strong><sup>[76]</sup></strong>. Le second approbateur, la confirmation par le mandant et la règle d’indépendance sont des choix du cadre.</p>''',
     ['11-31', '12-13']),

    # ------------------------------------------------------------------ § 8.6
    # [12-02] tableau 32 : Réviser selon le contrôle calculé
    ('''<td>Action soumise à approbation selon la figure 15.</td>''',
     '''<td>Action soumise à approbation selon le contrôle calculé (EXIG-AUT-10).</td>''',
     ['12-02']),
    # [12-14] édition : le contrôle est recalculé avant l'émission du jeton
    ('''<p>Éditer une action revient à approuver une autre action : la passerelle calcule l’empreinte des arguments modifiés, et c’est cette version que couvre le jeton.''',
     '''<p>Éditer une action revient à approuver une autre action : l’action éditée repasse par l’EXIG-AUT-10 avant l’émission du jeton, avec un nouvel indicateur de risque, la passerelle calcule l’empreinte des arguments modifiés, et c’est cette version que couvre le jeton (EXIG-AUT-12).''',
     ['12-14']),
    # [12-17] interrupt() : checkpointer exigé, persistant en production
    ('''Dans LangGraph, <code>interrupt()</code> exige un mécanisme de points de contrôle persistant;''',
     '''Dans LangGraph, <code>interrupt()</code> exige un mécanisme de points de contrôle (<em>checkpointer</em>), qui doit être persistant en production;''',
     ['12-17']),
    # [12-15] AUT-16 : champs selon le patron; issue des notifications et des questions
    ('''Chaque demande <strong>DOIT</strong> indiquer le patron, la tâche, l’agent, l’effet attendu et une échéance fixée par cas d’usage. Une demande sans réponse à l’échéance expire : l’action n’est pas exécutée et la tâche passe à une file d’escalade nommée.''',
     '''Chaque demande <strong>DOIT</strong> indiquer le patron, la tâche, l’agent, une échéance fixée par cas d’usage et, pour le patron Réviser, l’effet attendu. Une demande Réviser sans réponse à l’échéance expire : l’action n’est pas exécutée et la tâche passe à une file d’escalade nommée. Une question sans réponse suspend la tâche, puis l’escalade; une notification est escaladée si sa politique l’exige.''',
     ['12-15']),
    # [12-16] AUT-17 : l'échappatoire est retirée; renvoi à ORC-12
    ('''Un appel à effet de bord <strong>NE DOIT PAS</strong> précéder le point d’interruption dans la même étape; s’il ne peut pas être déplacé, il <strong>DOIT</strong> porter une clé d’idempotence (section 7.6).</p>''',
     '''Un appel à effet de bord <strong>NE DOIT PAS</strong> précéder le point d’interruption dans la même étape, et tout effet de bord suit l’EXIG-ORC-12 (clé déterministe, ou étape journalisée exécutée au plus une fois).</p>''',
     ['12-16']),
    # [12-18, 12-19] AUT-18 : mandat d'agent ambiant (A-16), drainage, arrêt sans préjudice des compensations (A-06)
    ('''<p>La délégation qui permet à un agent ambiant de niveau N3 ou N4 d’agir <strong>DOIT</strong> expirer à une échéance inscrite à sa fiche, au plus égale à la période d’attestation par le parrain, soit 12 mois au plus pour un agent de classe modérée ou faible (section 11.5 et EXIG-GOV-13). À l’échéance, l’agent s’arrête jusqu’à ce qu’une personne habilitée renouvelle la délégation.</p>''',
     '''<p>Le mandat d’agent ambiant, consentement inscrit au serveur d’autorisation qui permet à un agent ambiant de niveau N3 ou N4 d’obtenir, à sa demande, des jetons délégués d’au plus 15 minutes au nom du mandant tant que le mandat est valide et que le mandant est actif (section 9.3), <strong>DOIT</strong> expirer à une échéance inscrite à sa fiche, au plus égale à la période d’attestation par le parrain, soit 12 mois au plus pour un agent de classe modérée ou faible (section 11.5 et EXIG-GOV-13). Avant l’échéance, l’agent entre en drainage : il n’accepte plus de nouvelle tâche pendant une marge au moins égale à la durée maximale d’une saga. À l’échéance, l’agent s’arrête vers l’avant, sans préjudice du canal de compensation (EXIG-ORC-31), jusqu’à ce qu’une personne habilitée renouvelle le mandat.</p>''',
     ['12-18', '12-19']),

    # ------------------------------------------------------------------ § 8.7
    # [11-31] RIA : texte de la Commission et règlement modificatif, sans l'agrégateur
    ('''restent conscientes du biais d’automatisation (art. 14, par. 4, al. b)<strong><sup>[290]</sup></strong>;''',
     '''restent conscientes du biais d’automatisation (art. 14, par. 4, al. b)<strong><sup>[412]</sup></strong>;''',
     ['11-31']),
    ('''selon le RIA modifié par le règlement (UE) 2026/1744<strong><sup>[58, 315]</sup></strong>.''',
     '''selon le RIA modifié par le règlement (UE) 2026/1744<strong><sup>[58]</sup></strong>.''',
     ['11-31']),
    # [12-21] ATTENTION : renvoi au contrôle calculé
    ('''et automatise ce que la figure 15 classe à faible risque.</p>''',
     '''et automatise ce dont le contrôle calculé (EXIG-AUT-10) est automatique.</p>''',
     ['12-21']),
    # [11-02, 12-20] AUT-19 : écran dérivé des arguments canonisés (A-11)
    ('''un indicateur de risque produit par les règles du catalogue, non par le modèle. La prévisualisation''',
     '''un indicateur de risque produit par les règles du catalogue, non par le modèle. L’écran et <code>authorization_details</code> sont produits par la passerelle à partir des seuls arguments canonisés que couvre h et du schéma de l’outil inscrit au catalogue, jamais d’un texte fourni par l’agent; l’écran montre tous les champs, sauf ceux que le catalogue déclare non significatifs, ainsi que la grandeur calculée du seuil (EXIG-AUT-24). La prévisualisation''',
     ['11-02', '12-20']),
    # [12-01, 11-15, 12-22] AUT-20 : exemption selon le contrôle calculé; dimensionnement et issue au dépassement (A-12, A-14)
    ('''et la charge <strong>DOIT</strong> être répartie entre approbateurs, avec rotation. Les actions que la figure 15 classe comme automatiques ne sont pas soumises à approbation.</p>''',
     '''et la charge <strong>DOIT</strong> être répartie entre approbateurs, avec rotation. Seules les actions dont le contrôle calculé selon l’EXIG-AUT-10 est automatique échappent à l’approbation. La capacité d’approbation <strong>DOIT</strong> être dimensionnée à la conception et inscrite au registre (volume prévu, y compris la charge que crée l’EXIG-SEC-06, avec une marge); un plafond de demandes par agent et par tâche s’ajoute au plafond par approbateur. Au dépassement, les actions sont mises en file, jamais approuvées par défaut; une demande qui expire vaut refus, et un agent émetteur qui dépasse un seuil déclaré est suspendu par un arrêt ciblé.</p>''',
     ['12-01', '11-15', '12-22']),
    # [12-23] AUT-21 : unité, bornes absolues, règle de décision (A-32); comparaison à la médiane
    ('''Pour les actions exécutées sans approbation préalable aux niveaux N3 et N4, une revue humaine a posteriori <strong>DOIT</strong> porter sur un échantillon d’au moins 5 % des actions de classe modérée et 1 % de celles de classe faible (choix du cadre).''',
     '''Pour les appels d’outils à effet exécutés sans approbation préalable aux niveaux N3 et N4, une revue humaine a posteriori <strong>DOIT</strong> porter sur un échantillon stratifié par risque : 5 % de ces appels pour la classe modérée et 1 % pour la classe faible (choix du cadre), bornés par une taille minimale et une taille maximale absolues par période, que le comité fixe pour détecter un taux d’anomalie cible avec une confiance déclarée (EXIG-EVA-03). La comparaison à la médiane exige au moins trois approbateurs par cas d’usage; à défaut, la référence est prise entre cas d’usage comparables.''',
     ['12-23']),

    # ------------------------------------------------------------------ § 8.8
    # [12-25, 12-26] AUT-22 devient un renvoi à l'EXIG-CON-07 à 09 (A-24)
    ('''<p>Tout agent qui rend une décision concernant une personne, ou la prépare sans révision humaine significative, à partir d’un traitement automatisé de ses RP <strong>DOIT</strong> être de classe élevée et mettre en œuvre : l’avis à la personne au plus tard au moment de la communication de la décision; la production, sur demande, des RP utilisés, des raisons et des principaux facteurs et paramètres, établie à partir des traces et du journal d’audit; l’indication du droit de rectification; un canal vers un membre du personnel en mesure de réviser la décision; la conservation des renseignements utilisés pendant au moins un an après la décision.</p>''',
     '''<p>Voir l’EXIG-CON-07 (obligations envers la personne), l’EXIG-CON-08 (révision humaine significative) et l’EXIG-CON-09 (conservation), qui font foi. Règle résiduelle : tout agent dont les décisions concernant une personne sont fondées exclusivement, au sens de l’EXIG-CON-08, sur un traitement automatisé de ses RP <strong>DOIT</strong> être de classe élevée.</p>''',
     ['12-25', '12-26']),
    ('''<p>Pourquoi : obligations de l’article 12.1 et de l’article 11 de la Loi sur le privé (pour un organisme public, l’article 65.2 de la Loi sur l’accès prévoit des obligations d’information équivalentes)<strong><sup>[56]</sup></strong>; la traduction des traces en explication intelligible est un choix de mise en œuvre du cadre.</p>''',
     '''<p>Pourquoi : obligations de l’article 12.1 et de l’article 11 de la Loi sur le privé (pour un organisme public, l’article 65.2 de la Loi sur l’accès prévoit des obligations d’information équivalentes)<strong><sup>[56]</sup></strong>; une obligation légale n’a qu’une source dans le cadre, le chapitre 12.</p>''',
     ['12-25']),
    # [12-24] AUT-23 devient un renvoi à l'EXIG-CON-08; qualification a priori, mesure a posteriori (A-24)
    ('''<p>Une intervention humaine <strong>DOIT</strong> être traitée comme nominale, et la décision comme exclusivement automatisée, sauf si la personne qui intervient a l’autorité de modifier la décision et la compétence voulue, accède à toutes les données pertinentes et non à la seule recommandation de l’agent, dispose du temps nécessaire, et exerce une influence réelle mesurée par l’EXIG-AUT-21. Le degré d’intervention humaine et l’étape où elle a lieu <strong>DOIVENT</strong> être consignés dans l’EFVP.</p>''',
     '''<p>Voir l’EXIG-CON-08, qui porte le test de révision humaine significative (autorité, compétence, accès à toutes les données pertinentes, temps) et la qualification, faite a priori à l’EFVP et à la fiche, avec un défaut prudent : la décision est réputée exclusivement automatisée tant que la preuve contraire n’y est pas consignée. Règle résiduelle : les indicateurs de l’EXIG-AUT-21 servent de contrôle a posteriori; un écart requalifie la décision et déclenche les avis dus (EXIG-CON-07). Le degré d’intervention humaine et l’étape où elle a lieu <strong>DOIVENT</strong> être consignés dans l’EFVP.</p>''',
     ['12-24', '12-25']),
]

CORRECTIONS = [(t(a), t(b), c) for a, b, c in _C]

JOURNAL = [
    # § 7.3
    ('§ 7.3, figure 12 et texte', 'L’arbre se lit sous trois règles qui priment sur le dessin : le déclenchement par événement ne mène pas à lui seul à la chorégraphie, l’agent unique se teste avant le routage, la chaîne séquentielle et le clavardage de groupe sont des feuilles admises; figure non modifiable : le dessin garde l’ancienne branche « événement → chorégraphie », corrigée par la légende et le texte; le volet EXIG-ORC-01 (09-21) relève du § 7.1.', ['09-23']),
    ('§ 7.3, surcharge d’outils', 'Le chiffre de 85 % est nuancé comme au § 6.5 (près de 89 % d’après les deux chiffres d’Anthropic).', ['06-29']),
    ('§ 7.3, EXIG-ORC-09', 'Décompte des outils au début d’un tour, chevauchement défini par la confusion mesurée, seuil de précision déclaré à la fiche.', ['10-32']),
    ('§ 7.3, EXIG-ORC-10', 'Une tâche d’écriture à fortes dépendances DOIT rester à un seul agent; l’EXIG-ORC-23 admet un registre structuré des décisions prises; la force de l’exigence reste DEVRAIT pour le reste.', ['10-22', '10-38']),
    # § 7.4
    ('§ 7.4, Temporal; tableau 27', 'Limites d’historique de Temporal (51 200 événements ou 50 Mo, Continue-As-New) et réessais d’activités illimités par défaut ajoutés au texte et aux points d’attention.', ['10-29']),
    ('§ 7.4, EXIG-ORC-11', 'Moteur durable exigé pour les flux à effet P2-P3, à attente humaine ou de longue durée, persistance par étape journalisée, magasin en mémoire interdit en production et sur données réelles; granularité de LangGraph et de MAF signalée au tableau 27.', ['10-16', '10-17', '10-27']),
    ('§ 7.4, EXIG-ORC-12', 'Coordination déterministe définie après relecture des résultats journalisés; tout effet de bord est idempotent par clé déterministe ou exécuté au plus une fois, quel que soit son emplacement.', ['10-15', '10-26']),
    ('§ 7.4, EXIG-ORC-13', 'Phrase sourcée séparée du constat du cadre; état modifié à la main signé de nouveau et audité; aucun jeton au point de contrôle.', ['10-28']),
    ('§ 7.4, EXIG-ORC-14', 'Cohabitation bornée par le plafond de durée; retrait de sécurité d’une version : suspension ou migration testée des exécutions en cours.', ['10-18']),
    # § 7.5
    ('§ 7.5, règle 2, EXIG-ORC-16', 'Une étape dont l’issue est inconnue est résolue avant toute compensation (clôture de l’opération ou interrogation par la clé, 409 valant attente); à défaut, réconciliation humaine, sans compensation ni replanification à l’aveugle.', ['10-01']),
    ('§ 7.5, EXIG-ORC-16', 'Journal tenu avant chaque écriture seulement, limité aux références et aux arguments chiffrés nécessaires, sans jeton, soumis aux contrôles de l’EXIG-ORC-13 et distinct du journal d’audit.', ['10-23', '10-30']),
    ('§ 7.5, figure 13', 'Légende : T3 se lit comme une préautorisation P2, la capture P3 se fait au pivot, la compensation va de k−1 à 1 ou de k à 1 selon l’issue résolue de T<sub>k</sub>; figure non modifiable : le dessin montre encore « Débiter le client · non reprenable » avant le pivot.', ['10-03', '10-40']),
    ('§ 7.5, EXIG-ORC-15', 'Pivot unique; étapes postérieures réessayables jusqu’au succès ou dotées d’une file humaine; approbation propre à chaque P3; ordre et dépendances des compensations déclarés; coordinateur de saga inscrit au registre en chorégraphie.', ['10-04', '10-06', '10-07', '09-24']),
    ('§ 7.5, EXIG-ORC-17', 'Chaque compensation est un outil au catalogue, avec son palier; la compensation déclarée d’une étape approuvée est approuvée avec elle; exemple normatif : préautorisation P2, capture P3.', ['10-05']),
    ('§ 7.5, EXIG-ORC-18', 'Décompte précisé (erreur non transitoire, ou politique de réessai épuisée deux fois); compensations poursuivies selon le graphe déclaré; coordinateur de saga en chorégraphie.', ['10-31']),
    ('§ 7.5, EXIG-ORC-19', 'Portée étendue aux écrivains hors saga; échéance, propriétaire et procédure de libération de tout verrou sémantique.', ['10-08']),
    ('§ 7.5, EXIG-ORC-20', 'Tests ajoutés : effet réalisé et résultat perdu, original tardif, sagas concurrentes, échec après le pivot, plantage pendant une compensation, compensation sous coupe-circuit et pendant une panne de la passerelle, test de contrat d’idempotence contre le service réel; titre modifié : Tests d’injection de fautes des sagas.', ['10-09']),
    # § 7.6
    ('§ 7.6, texte et illustration', 'Clé dérivée de la tâche racine, construite par canonisation JCS d’un tableau étiqueté (et non par concaténation), identifiant racine aléatoire en production; itérations et étapes incertaines illustrées; rétention laissée au serveur par le brouillon, bornée par le cadre. La valeur abrégée « tache-7f3c2a » est gardée pour concorder avec C.6.', ['10-25', '10-12', '10-11']),
    ('§ 7.6, EXIG-ORC-21', 'Identifiant d’opération racine propagé par A2A et par les événements, indice d’itération, nouvel espace de clés à la bifurcation, construction canonique, aucune replanification d’une étape incertaine avant sa résolution.', ['10-12', '10-25']),
    ('§ 7.6, EXIG-ORC-22', 'Mode de vérification déclaré (natif, ou adaptateur transactionnel ou à requête d’état), sinon P3 sans réessai automatique; interrogation et révocation des clés; cloisonnement par client; durée de conservation couvrant la vie de la tâche, la reprise et la réconciliation.', ['10-11', '10-13']),
    # § 7.7
    ('§ 7.7, EXIG-ORC-23 et exemple', 'Le message porte une référence de délégation, le jeton voyageant en en-tête, hors message, point de contrôle, journal et contexte du modèle; il porte aussi la tâche racine, l’étape, le palier maximal et, au besoin, le registre des décisions; le niveau et la classe les plus contraignants de la chaîne s’imposent à l’exécutant; l’échéance de l’exemple devient un instant UTC.', ['10-20', '10-21', '12-07', '10-33']),
    ('§ 7.7, EXIG-ORC-25', 'Lecture sous l’intersection des droits; schéma de retour aux champs accessibles au mandant pour un agent à frontière de sécurité distincte; étiquettes de la session d’origine propagées.', ['10-34']),
    # § 7.8
    ('§ 7.8, EXIG-ORC-26', 'Réessais comptés dans les plafonds; l’arrêt au plafond agit vers l’avant, les compensations puisant dans une réserve hors plafonds.', ['10-10']),
    ('§ 7.8, EXIG-ORC-27', 'Gigue, nombre de tentatives borné et déclaré (maximumAttempts pour Temporal), couche unique de réessai, décompte dans les plafonds; disjoncteur obligatoire signalé comme choix du cadre; file humaine limitée au contexte nécessaire à la reprise.', ['10-19', '10-35', '10-36']),
    ('§ 7.8, EXIG-ORC-28', 'L’arrêt agit vers l’avant et laisse ouvert le canal de compensation; suspensions de sécurité et administrative distinguées, compensation automatique et réparation métier distinguées; exercice unique de l’EXIG-SEC-26, arrêt ciblé en production et global en environnement représentatif, délai comparé à la cible de l’EXIG-IAM-20.', ['10-02', '10-37']),
    ('§ 7.8, EXIG-ORC-31', 'Nouvelle exigence (A-06), placée après l’EXIG-ORC-28 : identité de compensation propre à l’orchestrateur ou au coordinateur de saga, limitée aux compensations déclarées d’étapes exécutées, insensible aux arrêts de l’agent, avec réserve de budget et file persistée si la passerelle est indisponible; à ajouter à l’annexe D. Le volet IAM-07 et IAM-20 relève du chapitre 9.', ['10-02', '10-10', '12-18']),
    # § 7.9-7.10
    ('§ 7.9, tableau 26', 'La cellule de l’anti-patron « victoire prématurée » ne cite plus que ce qu’exige l’EXIG-ORC-05.', ['10-39']),
    ('§ 7.9, MAST', 'Non retenu : audit_lit (ligne 48) confirme les trois catégories telles que le texte les nomme; la mention de la v3 de [292] relève de l’annexe G.', ['10-41']),
    ('§ 7.10, EXIG-ORC-30', 'Preuve de concept étendue à la clé d’idempotence stable, aux compensations et à l’escalade de saga, aux plafonds par exécution et à l’arrêt ciblé et global.', ['10-24']),
    # § 8.1
    ('§ 8.1, fondements', 'La prévision de Gartner est présentée comme une prévision sans méthode publiée, et non comme un constat.', ['11-32']),
    ('§ 8.1, tableau 28, EXIG-AUT-01', 'N0 qualifie un flux, non un agent (niveaux d’agent N1 à N4); N4 se distingue de N3 par l’origine de la tâche, que la passerelle lit et contrôle; « deux éléments observables » corrigé. L’alignement du § 3.3 relève du ch. 3.', ['11-14', '11-26']),
    ('§ 8.1, tableau 28, N2', 'L’approbation P2 (service d’approbation, même appareil admis) est distinguée de l’approbation P3 hors bande.', ['11-13']),
    ('§ 8.1, figure 14', 'Légende : le tableau 28 fait foi en cas d’écart; figure non modifiable : le dessin garde la DLP en N1, le retour arrière rapide en N4 et omet le hors bande en N2.', ['11-19']),
    ('§ 8.1, EXIG-AUT-05', 'Déclencheurs de réévaluation renvoyés à l’EXIG-GOV-12 (A-24); réévaluation avant la mise en service, ancienne version maintenue ou agent suspendu plutôt que rétrogradé, flux de repli seulement s’il existe; version de modèle épinglée et vérifiée. Le volet EXIG-CON-03 relève du ch. 12.', ['11-27', '11-15', '11-26']),
    ('§ 8.1, tableau 29 et note', 'Correspondances avec Feng et al. déclarées indicatives dans les deux phrases; l’« approbateur » de Feng n’intervient que sur sollicitation de l’agent.', ['11-28']),
    ('§ 8.1, EXIG-AUT-04, tableau 29, SAE J3016', 'Repli « à la sortie du domaine » aux deux endroits; le repli des N3 est celui du niveau 4 de SAE; la révision J3016_202609, non vérifiée à la source (audit_lit), n’est plus affirmée dans le corps, l’entrée [304] restant à relire.', ['11-29']),
    ('§ 7.8 et ch. 8, appels au RIA et à Gartner', 'Articles 14 et 26 du RIA appuyés sur le Service Desk de la Commission ([412], [447]) au lieu de l’agrégateur FLI; appel [315] retiré au § 8.7; Gartner [95] au lieu de l’article de presse [305]; WIMSE AIMS cité sous [309] seulement. La fusion des entrées doubles relève de l’annexe G.', ['11-31']),
    # § 8.2
    ('§ 8.2, tableau 30, EXIG-AUT-07', 'Vocabulaire unifié (« rayon élevé »); la détection lente plafonne seule à N2, l’EXIG-AUT-07 en étant le cas extrême.', ['11-11']),
    ('§ 8.2, EXIG-AUT-07', 'Un critère sans seuil approuvé est réputé atteint (fermeture par défaut).', ['11-12']),
    ('§ 8.2, EXIG-AUT-06', 'Les actions accessibles après approbation comptent dans le classement. Le volet classe par défaut du tableau 46 relève du ch. 12.', ['11-17', '11-18']),
    # § 8.3
    ('§ 8.3, tableau 31, P0; EXIG-AUT-08', 'Attribut de catalogue « sortie de données », indépendant du palier : l’outil compte comme outil d’envoi (EXIG-SEC-06) et comme [C], avec contrôle DLP des arguments.', ['11-16']),
    ('§ 8.3, tableau 31, P2; EXIG-AUT-08', 'P2 et P3 disjoints par l’effet (irréversible ou externe = P3, A-27); seuil mesuré sur une grandeur que l’agent ne choisit pas, avec portée et fenêtre; palier propre aux compensations; montants et identifiants en chaînes ou en entiers en unités mineures.', ['11-08', '11-01', '10-05']),
    ('§ 8.3, EXIG-AUT-09', 'Approbation des P3 hors bande en DOIT (appareil et session distincts, authentification résistante à l’hameçonnage); compensation déclarée couverte par l’approbation de l’étape; ASI02 au lieu d’ASI09 dans le Pourquoi.', ['11-13', '12-10', '11-30']),
    # § 8.4
    ('§ 8.4, EXIG-AUT-10, figure 15', 'Contrôle défini comme l’union des contrôles (cellule, niveau et classe les plus contraignants de la chaîne, déclencheurs, non-dérogeables) avec un ordre total des approbations; déclencheur de cumul aligné sur l’EXIG-SEC-04; passerelle traversée par tout P2-P3 (EXIG-ARC-01); légende de la figure 15 précisée; figure non modifiable : les cellules gardent leur libellé.', ['11-06', '11-07', '11-09', '11-20']),
    ('§ 8.4, règle de deux', '[B] reprend la formulation de Meta (« systèmes sensibles ou données privées »). La définition de la session relève du glossaire et du § 3.1.', ['11-07']),
    ('§ 8.4, EXIG-AUT-11', 'Dépendances complétées (registre des jti, service d’audit); politique ou instantané non échus valant service disponible, échus ne laissant passer que P0; refus de tout appel soumis à approbation; compensation refusée versée à la file de l’EXIG-ORC-31.', ['11-10']),
    ('§ 8.4, EXIG-AUT-24', 'Nouvelle exigence (A-13), placée après l’EXIG-AUT-11 : grandeur calculée, unité, portée et fenêtre de chaque seuil, compteurs à cohérence forte, valeur fixée au catalogue, traitement comme dépassé avant l’approbation des seuils; à ajouter à l’annexe D. Les volets C.1, C.2 et fiche B relèvent des annexes.', ['11-08']),
    # § 8.5
    ('§ 8.5, texte et EXIG-AUT-12', 'h devient la canonisation d’un objet {outil, version, definition_digest, agent_id, task_id, arguments}; la passerelle rejette l’entrée non I-JSON et transmet la forme hachée; h atteste les octets transmis, non l’effet. Les tests négatifs de l’annexe A et la valeur de h en C.6 relèvent des annexes.', ['11-01', '12-05', '11-22', '12-06']),
    ('§ 8.5, EXIG-AUT-12', 'Liste de vérification complétée (émetteur, audience, concordance de l’agent et de la tâche, nombre et distinction des approbateurs); double approbation par deux jetons sur le même h; rôle de l’approbateur.', ['11-05', '11-23', '12-03', '12-11']),
    ('§ 8.5, EXIG-AUT-12', 'Un jeton couvre une opération : présentations répétées relayées jusqu’à l’expiration, demande de précision ou refus non consommateurs, interrogation par la clé après l’expiration, registre des jti partagé et atomique; jeton conservé par la passerelle, hors du modèle.', ['10-14', '11-04', '12-04', '12-07']),
    ('§ 8.5, EXIG-AUT-12', 'Précondition de version ou valeurs résolues recommandées pour un P3 sur une ressource modifiable, sinon risque résiduel déclaré à la fiche.', ['11-03']),
    ('§ 8.5, EXIG-AUT-12, AUT-15, AUT-20, ATTENTION, tableau 32, figure 16', 'Les renvois à la « figure 15 » deviennent des renvois au contrôle calculé selon l’EXIG-AUT-10; figure non modifiable : le dessin de la figure 16 montre encore un appel « P3 », un jeton remis à l’agent et un jeton sans agent ni jti, que la légende corrige.', ['12-01', '12-02', '12-08', '12-21']),
    ('§ 8.5, texte', 'L’emploi d’authorization_details dans un jeton d’approbation est présenté comme un profil du cadre (audit_lit, ligne 32).', ['11-02']),
    ('§ 8.5, EXIG-AUT-14', 'Le hors bande des P3 est renvoyé à l’EXIG-AUT-09 (DOIT); CIBA reste le moyen recommandé; le binding_message aide à reconnaître la demande, le lien à l’action reposant sur h.', ['11-25', '12-09', '12-10']),
    ('§ 8.5, EXIG-AUT-15', 'Listes par classe, palier et motif selon le contrôle calculé; confirmation par le mandant admise sauf P3 de classe élevée; second approbateur indépendant du mandant, de sa ligne hiérarchique et du parrain; inscription et formation pour les approbateurs autres que le mandant; authentification résistante à l’hameçonnage pour les P3; habilitation vérifiée avant signature.', ['11-21', '12-12', '11-24', '12-13']),
    # § 8.6
    ('§ 8.6, édition, EXIG-AUT-12', 'L’action éditée repasse par l’EXIG-AUT-10 avant l’émission du jeton; l’éditeur ne peut pas être le seul approbateur d’un appel qui en exige deux.', ['12-14']),
    ('§ 8.6, interrupt()', 'Un checkpointer est exigé par l’API; sa persistance est une exigence de production.', ['12-17']),
    ('§ 8.6, EXIG-AUT-16', 'Effet attendu exigé pour le seul patron Réviser; issue à l’échéance définie pour les questions et les notifications.', ['12-15']),
    ('§ 8.6, EXIG-AUT-17', 'L’exception « s’il ne peut pas être déplacé » est retirée; renvoi à l’EXIG-ORC-12.', ['12-16']),
    ('§ 8.6, EXIG-AUT-18', 'Mandat d’agent ambiant distingué de la délégation par échange de jetons; drainage avant l’échéance; arrêt vers l’avant, sans préjudice du canal de compensation. Le glossaire et l’EXIG-IAM-15 relèvent d’autres tranches.', ['12-19', '12-18']),
    # § 8.7
    ('§ 8.7, EXIG-AUT-19', 'Écran et authorization_details produits par la passerelle à partir des seuls arguments canonisés et du schéma du catalogue, tous les champs significatifs montrés avec la grandeur calculée du seuil. La complétion d’authorization_details en C.6 relève de l’annexe C.', ['11-02', '12-20']),
    ('§ 8.7, EXIG-AUT-20', 'Capacité d’approbation dimensionnée et inscrite au registre, plafond par agent et par tâche, mise en file au dépassement, expiration en refus, suspension ciblée de l’émetteur au-delà d’un seuil.', ['11-15', '12-22']),
    ('§ 8.7, EXIG-AUT-21', 'Unité définie (appel à effet), échantillon stratifié borné par des tailles absolues dimensionnées pour un taux cible (A-32); comparaison à la médiane seulement à partir de trois approbateurs.', ['12-23']),
    # § 8.8
    ('§ 8.8, EXIG-AUT-22', 'Devient un renvoi aux EXIG-CON-07 à CON-09 (A-24), avec la règle résiduelle de classe élevée pour les décisions fondées exclusivement sur un traitement automatisé; la portée ambiguë disparaît.', ['12-25', '12-26']),
    ('§ 8.8, EXIG-AUT-23', 'Devient un renvoi à l’EXIG-CON-08 (A-24) : qualification a priori avec défaut prudent, mesure de l’EXIG-AUT-21 comme contrôle a posteriori qui requalifie. L’alignement de l’EXIG-CON-08 relève du ch. 12.', ['12-24', '12-25']),
    ('§ 8.3, tableau 31', 'Non retenu en partie : le reclassement de l’envoi interne en P2 n’est pas fait, l’EXIG-AUT-08 (A-27) classant P3 tout effet externe; le besoin de l’assistant interactif est couvert par la confirmation du mandant (EXIG-AUT-15).', ['12-13']),
]
