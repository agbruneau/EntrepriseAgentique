"""Recompose le Cadre de référence CRE-IA-2026-01 à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, imprimée par Chrome, lue dans git au commit
        ORIGINE, recomposée dans documents/Cadre de Référence.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt : le PDF fait foi. sources/commun/extraire.py
relit son balisage, sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - balisage de Chrome : en-tête courant (y ≈ 33) et pied (y ≈ 750) écartés par les
    marges; le pied, rangé sous le H1 du chapitre suivant, rend ces H1 « multipages »;
  - page de titre et fiche du document (p. 1-2) : couverture et fiche du gabarit;
    l'historique des versions et la méthode restent en préambule;
  - table des matières, listes des tableaux et des figures (p. 5-10) : régénérées;
    les listes d'origine servent à contrôler les légendes et donnent le titre court
    des figures;
  - titres : parties (H1 « Fondements »…) au niveau 1, chapitres et annexes (H1) au
    niveau 2, puis H2 -> 3, H3 -> 4, H4 -> 5;
  - schémas (28 Figure) : recadrés en PDF vectoriel depuis la page d'origine et
    intégrés tels quels (texte compris), légende reprise;
  - légendes « Tableau N — … » (paragraphes en gras avant le tableau) : remises en
    légende; numéros gardés en toutes lettres, sans numérotation de Typst;
  - blocs d'exigence (EXIG-XXX-NN) et encadrés (À RETENIR, ATTENTION…) : regroupés
    selon le rectangle de fond qui les contient dans l'original, puis stylés;
  - blocs de code (NonStruct en chasse fixe) : <pre>, ligne visuelle par ligne
    (retours de Chrome gardés, corps réduit pour que la plus longue tienne);
  - code en ligne : pastilles de Chrome lues sans leur marge interne (extracteur
    commun, pastilles=True); renvois d'exigences de la grille d'homologation (lus en
    exposant) remis en fin d'item;
  - Typst (schemas.typ) : code en ligne long coupé seulement après « / » ou « - »;
  - « André-Guy » : le « é » est un span à part, suivi d'un blanc.

Contrôles : complétude de l'extraction (écarts connus listés), recadrage sans perte
du texte des schémas, retouches du script sans perte, contrôle mot à mot de
composer(), numéros des tableaux et des figures conformes aux listes d'origine.

Actualisation du 1er novembre 2026 : annexe H, informative, rédigée en HTML dans ce dossier
(actualisation-2026-11.html) et composée après l'annexe G; ses tableaux et ses références
continuent les suites du document (tableau 70, référence 474). Elle ne modifie aucune exigence.

Revue contradictoire du 3 novembre 2026 : ses correctifs du corps sont faits à leur place
par corrections.py, sur le corps recomposé (corps()), et consignés à l'annexe H (section
« Revue contradictoire du 3 novembre 2026 »). Les mots qu'un correctif retire sont
soustraits du contrôle « sans perte »; le contrôle de composer() porte sur le texte corrigé.
"""
import atexit, collections, html, pathlib, re, shutil, subprocess, sys, tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as C
from composer import ACTUALISATION, AUTEUR, DOCUMENTS, actualisation, chaine_typst, composer, mots
from extraire import MONO, Extracteur, cadre, controler_extraction, texte_controle, vers_html, zones_ecartees
from corrections import corriger
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Cadre de Référence.pdf'
# Édition d'origine (Chrome, 28 oct. 2026) : le PDF recomposé ne doit pas servir de
# source à son tour. Elle porte, au commit ORIGINE, le nom long du document (renommé
# le 31 oct. 2026).
ORIGINE = 'd28324a'
NOM_ORIGINE = 'Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf'
OUT = pathlib.Path(args[1]) if len(args) > 1 else SORTIE
if args:
    SRC = pathlib.Path(args[0])
else:
    SRC = pathlib.Path(tempfile.mkdtemp()) / 'origine.pdf'
    atexit.register(shutil.rmtree, SRC.parent, True)
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{NOM_ORIGINE}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

MARGES = (50, 50)          # en-tête courant à y ≈ 33-42, pied à y ≈ 750; texte entre 57 et 728
PAGES_TDM = range(4, 10)   # p. 5 à 10 : table des matières, listes des figures et des tableaux
PREAMBULE = ('Fiche du document', 'Historique des versions', 'Méthode et avertissements')
PARTIES = ('Fondements', 'Architecture, interopérabilité et orchestration', 'Confiance et exploitation',
           'Gouvernance, conformité et mise en œuvre', 'Outils d’application')
LARGEUR = 468              # justification du gabarit (pt)
EXIG = re.compile(r'EXIG-[A-Z0-9]{3}-\d{2}')
RETIRES = []               # textes d'origine remplacés par corrections.py
# Libellés des schémas corrigés par la revue du 3 novembre 2026 : {figure : [(span d'origine,
# libellé corrigé, 'c' centré | 'g' aligné à gauche)]}. Les écarts de structure (flèches,
# branches, ordre des étapes) restent corrigés par la légende (annexe H, section H.6).
LIBELLES = {
    1: [('audit inaltérable', 'audit chaîné et ancré', 'c'),
        ('évaluation 3 paliers', 'évaluation en 3 étages', 'c'),
        ('Risques et conformité (chapitres 12 et 13)', 'Risques, conformité et approvisionnement (chapitres 12 et 13)', 'c'),
        ('Loi 25 · BSIF · RIA · NIST AI RMF · ISO/IEC 42001 · contrats',
         'Loi 25 · BSIF E-23 · RIA · NIST AI RMF · ISO/IEC 42001 · contrats', 'c'),
        ('annexes : grille d’homologation, fiche d’agent, contrats types, registre des exigences, glossaire, '
         'validation des sources',
         'annexes : grille d’homologation, fiche d’agent, contrats types, registre des exigences, glossaire, '
         'validation des sources, références, actualisation', 'c', {'l': 440})],
    2: [('4 + 5 = 9 contrats réutilisables, une politique', '4 + 5 = 9 contrats réutilisables, un point d’application', 'c')],
    3: [('• Journal d’audit inaltérable', '• Journal d’audit chaîné et ancré', 'g'),
        ('• Évaluation continue (3 paliers)', '• Évaluation continue (3 étages)', 'g'),
        # portée de la passerelle (A-01) et placement des mémoires (tableau 13)
        ('Interdit : un agent n’atteint jamais un système ou un outil hors domaine sans passer par la passerelle '
         'et le catalogue',
         'Interdit : un agent n’atteint jamais un système ou un outil sans passer par la passerelle et le '
         'catalogue, hors fonction locale P0-P1 (EXIG-ARC-01)', 'g', {'l': 430}),
        ('Mémoire épisodique', 'Mémoire de travail', 'c'),
        ('Ressources, index,', 'Ressources, mémoires', 'c'),
        ('graphes de connaissances', 'épisodique et sémantique', 'c')],
    4: [('Validation et provenance de la source · isolation par locataire et par serveur MCP · expiration · '
         'instantanés restaurables',
         'Validation et provenance de la source · isolation par mandant ou par locataire (tableau 13) · expiration · '
         'instantanés restaurables', 'g'),
        ('Interdits : état conservé en mémoire de processus · transcriptions brutes comme mémoire longue · '
         'magasin partagé entre serveurs non isolés',
         'Interdits : état qui n’existe qu’en mémoire de processus · transcriptions brutes comme mémoire longue · '
         'magasin partagé entre serveurs non isolés', 'g')],
    13: [('Débiter le client', 'Préautoriser le paiement', 'c'), ('non reprenable', 'compensable (P2)', 'c')],
    22: [('Palier 3', 'Étage E3', 'c'), ('Palier 2 — Trajectoires', 'Étage E2 — Trajectoires', 'c'),
         ('Palier 1 — Contrats déterministes', 'Étage E1 — Contrats déterministes', 'c'),
         ('50 à 200 scénarios, cas adverses', '50 scénarios au moins, cas adverses', 'c'),
         ('Tout changement de modèle, d’invite, d’outil ou de version de protocole relance les paliers 1 et 2.',
          'Tout changement de modèle, d’invite, d’outil ou de version de protocole relance les étages E1 et E2.', 'c')],
    25: [('bornés, un niveau', 'bornés, du niveau', 'c'), ('sous la cible', 'inférieur au visé', 'c'),
         ('POINTS DE CONTRÔLE', 'JALONS DU CYCLE DE VIE', 'g')],
    28: [('Pass. d’agents (P0, P1 puis P2)', 'Pass. d’agents (P0 à P3)', 'g'),
         ('Art. 12.1, validation E-23', 'Art. 12.1, inventaire E-23', 'g')],
}
# Écarts que la légende corrigeait encore (« figure non modifiable » des modules 01 à 06) : libellés,
# lignes ajoutées et tracés corrigés dans le dessin (editer_libelles), aux couleurs des schémas.
MARINE, VERT, ROUGE = (0.0549, 0.1647, 0.2784), (0.1686, 0.4784, 0.2941), (0.6588, 0.1961, 0.2431)
BLANC, GRILLE = (1, 1, 1), (0.8902, 0.9098, 0.9373)
LIBELLES.update({
    # 05-19, 05-12 : tableau 14 et EXIG-INT-03; OAuth 2.0 profilé par la RFC 9700
    5: [('Finalité et base légale de chaque flux de renseignements personnels; EFVP; entente écrite',
         'Finalité et fondement de chaque flux de renseignements personnels; EFVP lorsque la loi l’exige,', 'g',
         {'l': 300}),
        ('pour toute communication hors Québec; clauses contractuelles pour les agents de tiers',
         'notamment hors Québec; entente écrite et clauses contractuelles avec chaque tiers', 'g', {'l': 300}),
        ('Protocoles du catalogue (MCP, A2A, CloudEvents, OpenAPI), TLS 1.3, authentification',
         'Protocoles du catalogue (MCP, A2A, CloudEvents, OpenAPI), TLS 1.3 (1.2 en plancher), authentification',
         'g', {'l': 300}),
        ('normalisée (OAuth 2.x), contexte de trace W3C propagé à chaque appel',
         'normalisée (OAuth 2.0, RFC 9700), contexte de trace W3C propagé à chaque appel', 'g', {'l': 300})],
    # 05-12, 05-13 : OAuth 2.0 (RFC 9700); Surveiller (hors production) et Contenir (tableau 15)
    6: [('OAuth 2.x, échange de jetons (RFC 8693),', 'OAuth 2.0 (RFC 9700), échange de jetons (RFC 8693),', 'g',
         {'l': 142}),
        ('À surveiller (pilotes seulement)', 'À surveiller ou à contenir', 'g'),
        ('Protocoles de commerce et de paiement', 'Commerce et paiements agentiques :', 'g'),
        ('agentiques; formats propriétaires', 'veille hors production; formats propres', 'g', {'l': 112}),
        ('contenus derrière un adaptateur', 'à un fournisseur, derrière un adaptateur', 'g', {'l': 112})],
    # 06-02, 06-17, 06-32 : client par point d'accès, jeton destiné à la passerelle, EMA au statut Évaluer;
    # les lignes de la requête, en IBM Plex Mono, sont réécrites ensemble en IBM Plex Sans
    7: [('Un client par serveur;', 'Un client par point d’accès;', 'g'),
        ('POST /mcp · MCP-Protocol-Version: 2026-07-28 · Mcp-Method: tools/call · Mcp-Name: erp_creer_bon',
         'POST /mcp · MCP-Protocol-Version: 2026-07-28 · Mcp-Method: tools/call · Mcp-Name: erp_creer_bon', 'g'),
        ('Authorization: Bearer <jeton émis pour ce serveur>',
         'Authorization: Bearer <jeton émis pour ce point d’accès de la passerelle>', 'g', {'l': 310}),
        ('{"method":"tools/call","params":{"name":"erp_creer_bon","arguments":{…},',
         '{"method":"tools/call","params":{"name":"erp_creer_bon","arguments":{…},', 'g'),
        ('"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","traceparent":"00-…"}}}',
         '"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","traceparent":"00-…"}}}', 'g'),
        ('', 'EMA : statut Évaluer, pilotes seulement (section 6.3)', 'g',
         {'comme': 'Extensions (activation explicite) :', 'dx': 5.9, 'dy': 18.8, 'corps': 5.3, 'couleur': 0x5a6678})],
    # 07-29, 08-01, 08-08, 08-09 : découverte au catalogue, étape 7 en flux continu, jeton remis à la
    # passerelle (flèche prolongée jusqu'à elle), référence non secrète, rôles distincts
    9: [('Utilisateur', 'Personnes', 'c'),
        ('et approbateur', 'utilisateur, approbateur', 'c', {'l': 62}),
        ('Registre', 'Catalogue', 'c'),
        ('rect', (88.0, 243.2, 171.4, 249.2), BLANC, None, 0),
        ('fleche', (87.4, 246.3), (341.1, 246.3), VERT, 0.8164, MARINE),
        ('jeton d’approbation signé', 'approbation signée :', 'g'),
        ('', 'jeton remis à la passerelle, qui le conserve', 'g', {'comme': 'jeton d’approbation signé', 'dx': 82.4}),
        ('SendMessage (même taskId) + approbation', 'SendStreamingMessage (même taskId) + réf. d’approbation', 'g',
         {'l': 150}),
        ('+ clé d’idempotence', '+ même clé, réf. d’approbation', 'g', {'l': 74})],
    # 08-18 : le plafond N laisse traiter N − 1 événements; l'agent N reçoit le saut 3 et republie le 4
    10: [('reçoit saut 4/4', 'reçoit 3/4, republie 4/4', 'c', {'l': 72}),
         ('+ alerte d’observabilité', 'saut 4/4 non traité', 'c'),
         ('boucle interrompue', '+ alerte d’observabilité', 'c')],
    # 09-25 : évaluateur, modèle ou invite distincts; itération = cycle de production et d'évaluation
    11: [('≤', '', 'c'),
         ('3 itérations', '≤ 3 itérations (production + évaluation)', 'c', {'dx': -1.8, 'l': 112}),
         ('(compilateur, règles), critique sur', '(compilateur, règles), puis modèle ou', 'g', {'l': 106}),
         ('un modèle distinct; puis escalade.', 'invite distincts; escalade au plafond.', 'g', {'l': 106})],
    # 09-23 : question orthogonale sur la chorégraphie, agent unique avant routage, feuilles de la chaîne
    # séquentielle et du clavardage de groupe; les deux cases de droite échangent libellés et couleurs
    12: [('Déclenchement par une', 'Des domaines faiblement couplés', 'c', {'l': 86}),
         ('personne ou un événement?', 'réagissent-ils au même fait?', 'c', {'l': 86}),
         ('personne', 'NON', 'c', {'couleur': 0xa8323e}),
         ('événement', 'OUI', 'c', {'couleur': 0x2b7a4b}),
         ('étapes agentiques bornées', 'ou chaîne séquentielle', 'c'),
         ('Un spécialiste unique suffit', 'Un agent unique bien outillé,', 'c', {'l': 95}),
         ('après qualification?', 'contexte non saturé, suffit-il?', 'c', {'l': 95}),
         ('Un agent unique, outils bien', 'Un spécialiste unique suffit', 'c', {'dy': 4.1}),
         ('décrits, contexte non saturé,', 'après qualification?', 'c', {'dy': 4.1}),
         ('suffit-il?', '', 'c'),
         ('repeindre', (444.4, 379.5, 558.7, 409.2), (0.3569, 0.2941, 0.6039)),
         ('repeindre', (444.4, 474.5, 558.7, 504.2), (0.0902, 0.2902, 0.4863)),
         ('Routage et transfert', 'Agent unique', 'c'),
         ('l’agent de tête se retire', 'recherche d’outils si nécessaire', 'c'),
         ('Agent unique', 'Routage et transfert', 'c'),
         ('recherche d’outils si nécessaire', 'l’agent de tête se retire', 'c'),
         ('2 niveaux au plus · parallèle si possible', 'ou clavardage de groupe si débat requis', 'c')],
    # 11-19 : contrôles alignés sur le tableau 28
    14: [('accès circonscrit, DLP,', 'accès circonscrit, journalisation,', 'c', {'l': 86}),
         ('P2 et P3 après', 'P2 après approbation signée;', 'c', {'l': 86}),
         ('approbation signée', 'P3 après approbation hors bande', 'c', {'l': 86}),
         ('revue par échantillon', 'retour arrière rapide', 'c'),
         ('retour arrière rapide', 'arrêts testés, réautorisation', 'c', {'l': 86})],
    # 11-06, 11-20 : cellules en complément du tableau 31, P2 harmonisé, revue a posteriori, cumul
    15: [('jeton délégué, masquage', 'contrôles du palier (tableau 31)', 'c', {'l': 92}),
         ('repeindre', (251.4, 465.5, 350.9, 501.2), (0.8980, 0.9569, 0.9176)),
         ('Automatique + audit', 'Automatique', 'c', {'pres': (301, 478), 'couleur': 0x2b7a4b}),
         ('jeton délégué, filtrage par ligne', 'contrôles du palier (tableau 31)', 'c', {'l': 92}),
         ('repeindre', (353.8, 425.5, 453.3, 461.1), (1.0, 0.9490, 0.8627)),
         ('Autonome sous seuil', 'Approbation au-delà', 'c', {'couleur': 0xb86e00}),
         ('idempotence, compensation', 'du seuil métier déclaré', 'c'),
         ('Audit + revue', 'Revue a posteriori', 'c'),
         ('finalité vérifiée, minimisation', 'échantillon : finalité, minimisation', 'c', {'l': 92}),
         ('La règle la plus stricte l’emporte. Le palier d’un outil est inscrit au catalogue; la passerelle ne se '
          'fie pas aux annotations déclarées par le serveur.',
          'Les contrôles se cumulent; l’approbation la plus stricte l’emporte (EXIG-AUT-10). Le palier d’un outil '
          'est inscrit au catalogue; la passerelle ne se fie pas aux annotations déclarées par le serveur.', 'g',
          {'l': 500})],
    # 12-01, 12-02, 12-08 : appel soumis à approbation (EXIG-AUT-10), jeton remis à la passerelle (flèche
    # raccourcie), champs du jeton, rejeu avec la clé d'idempotence et la référence de la demande
    16: [('prépare l’action P3', 'prépare l’action', 'c'),
         ('appel d’outil P3 sans jeton', 'appel soumis à approbation, sans jeton', 'g', {'l': 112}),
         ('rect', (103.4, 216.3, 238.7, 223.0), BLANC, None, 0),
         ('fleche', (384.3, 219.6), (241.8, 219.6), VERT, 0.8907),
         ('{ h, approbateur, tâche, exp }', '{ h, agent, approbateur, rôle, jti, tâche, exp }', 'd', {'l': 122}),
         ('rejoue l’appel avec le jeton', 'rejoue : même clé, réf. de la demande', 'g', {'l': 112}),
         ('vérifie la signature, l’expiration, l’usage unique et',
          'apparie le jeton qu’elle conserve, vérifie signature, expiration', 'g', {'l': 200}),
         ('recalcule h : toute modification des arguments',
          'et usage unique, recalcule h : toute modification des arguments', 'g', {'l': 200})],
    # 4.55, 4.06 (A-16) : second jeton de la passerelle, deux audiences, extrait, JWT-SVID
    17: [('et système cible', 'système cible : autre audience', 'c', {'l': 74}),
         ('exécution sous l’identité d’Alice', 'second jeton, au nom d’Alice', 'g'),
         ('subject_token = jeton d’Alice', 'subject_token = jeton d’Alice', 'g'),
         ('actor_token = SVID de l’agent', 'actor_token = JWT-SVID de l’agent', 'g'),
         ('resource = mcp-finance', 'resource = mcp-finance', 'g'),
         ('Revendications du jeton délégué (étape 3)', 'Revendications du jeton délégué (étape 3, extrait)', 'g')],
    # 4.10, 4.11, 4.14, 4.61, 4.62 : cnf, contrôle 5 calculé, débit dès l'authentification, injection
    # conditionnelle, intention écrite avant le relais, filtre sans effet sur l'action
    18: [('le mandant', 'le mandant (cnf)', 'c', {'l': 44}),
         ('(P3, P2 > seuil)', '(P3, P2 > seuil, N2)', 'c', {'l': 44}),
         ('Débit, quotas', 'Débit (dès 1),', 'c', {'l': 44}),
         ('et budget', 'quotas, budget', 'c', {'l': 44}),
         ('secrets hors', 'secrets si prévu,', 'c', {'l': 44}),
         ('de l’agent', 'hors de l’agent', 'c', {'l': 44}),
         ('', 'Appel P2 ou P3 : l’enregistrement d’intention est écrit avant le relais (EXIG-OBS-11); celui de '
          'l’issue, au retour.', 'g', {'comme': 'Authentifier', 'dx': -7.7, 'dy': 28.6, 'couleur': 0x5a6678,
                                      'l': 400}),
         ('masquage des renseignements personnels et des secrets,',
          'masquage des RP et des secrets, sans annuler un effet déjà produit;', 'c', {'l': 195}),
         ('span OpenTelemetry, enregistrement', 'span OpenTelemetry, audit de l’issue', 'c'),
         ('d’audit (mandant, agent, outil, décision)', '(mandant, agent, outil, décision)', 'c')],
    # 4.69 : EXIG-SEC-04
    19: [('[B] accède à des données sensibles', '[B] accède à des données ou systèmes sensibles', 'g', {'l': 114}),
         ('Les trois à la fois : supervision humaine', 'Les trois à la fois : approbation de l’action', 'g',
          {'l': 124}),
         ('ou nouveau contexte vierge obligatoires.', 'exacte ou nouveau contexte vierge obligatoire.', 'g',
          {'l': 124})],
    # 4.36 : attente d'approbation en deux événements reliés par un lien de span, et non en span ouvert
    21: [('rect', (324.8, 192.0, 365.1, 201.9), BLANC, None, 0),
         ('ligne', (336.0, 191.5), (336.0, 202.4), GRILLE, 0.7422),
         ('ligne', (331.4, 196.95), (358.4, 196.95), ROUGE, 0.6, '[1.2 1.2] 0'),
         ('rond', (328.6, 196.95), 2.6, ROUGE),
         ('rond', (361.2, 196.95), 2.6, ROUGE),
         ('attente d’approbation (INPUT_REQUIRED)', 'attente d’approbation : deux événements, lien de span', 'g',
          {'l': 150}),
         # 4.27, A-01 : l'écriture finale est un outil MCP, avec son span MCP CLIENT
         ('', 'MCP CLIENT', 'g', {'comme': 'MCP CLIENT', 'dx': 25.5, 'dy': 39.9}),
         ('ca.entreprise.cost_center', 'ca.ent.cost_center', 'g')],
    # 4.48, A-34 : cinq dimensions de l'EXIG-ORC-26 (rangée « Étapes » ajoutée), état tenu par la
    # passerelle de modèles, alerte au responsable technique
    23: [('copier', (388.0, 189.4, 499.3, 198.3), (0, -32.8)),
         ('copier', (388.0, 173.0, 454.8, 182.0), (0, -16.4)),
         ('', 'Étapes', 'g', {'comme': 'Délai', 'dy': -32.8}),
         ('', '6 / 10', 'd', {'comme': '38 s / 60 s', 'dy': -32.8}),
         ('80 % : alerte au propriétaire', '80 % : alerte au responsable technique', 'd', {'l': 125}),
         ('La passerelle de modèles et l’orchestrateur', 'La passerelle de modèles tient l’enveloppe', 'g'),
         ('décrémentent l’enveloppe à chaque étape;', 'et la décrémente à chaque étape;', 'g')],
    # 5.30, 5.85, 5.87, 5.09 (A-06, A-18, A-27) : contention sans destruction, gel étendu, qualification et
    # avis en parallèle de la préservation, sagas compensées et réparation métier, étages d'évaluation
    26: [('révocation de ses jetons', 'jetons et accès révoqués;', 'c'),
         ('et de ses accès', 'bacs à sable conservés', 'c', {'l': 70}),
         ('Gel des traces, du journal', 'Gel des traces, de l’audit,', 'c', {'l': 95}),
         ('d’audit et des instantanés', 'de la mémoire, des bacs à sable,', 'c', {'l': 95}),
         ('de mémoire', 'des tâches A2A, des approbations;', 'c', {'l': 95}),
         ('', 'purges suspendues', 'c', {'comme': 'de mémoire', 'dy': 8.2, 'l': 95}),
         ('rect', (215.3, 215.6, 291.6, 222.0), BLANC, None, 0),
         ('ligne', (217.3, 218.8), (290.5, 218.8), MARINE, 0.8907, '[2 2] 0'),
         ('', 'en parallèle', 'c', {'comme': 'Préserver', 'dx': 51.7, 'dy': -28.5, 'police': 'IBMPlexSans-Regular',
                                   'corps': 5.8, 'couleur': 0x5a6678}),
         ('Compensations des actions', 'Sagas en cours compensées;', 'c'),
         ('exécutées; correctif; relance', 'actions terminées réparées', 'c'),
         ('des paliers d’évaluation', 'par le métier; correctif;', 'c'),
         ('', 'relance des étages d’évaluation', 'c', {'comme': 'des paliers d’évaluation', 'dy': 8.2, 'l': 90})],
})
FICHE_12 = {'Version et date': '1.2 — 3 novembre 2026',
            'État des sources': 'Faits, versions et dates vérifiés aux 27 et 28 octobre 2026 contre des sources '
                                'primaires ou, à défaut, secondaires reconnues (annexe F); faits repris par la '
                                'revue contradictoire du 3 novembre 2026 vérifiés à cette date (annexe H, '
                                'section H.6)'}

# Écarts connus du contrôle de complétude (les en-têtes de tableau répétés, absorbés par
# l'extracteur, en sont soustraits) : « André » (p. 1 et 2) est composé de deux spans
# séparés par un blanc; le PDF se lit « Andr » + « é », l'extraction donne « André ».
ECARTS_CONNUS = {'andr': 2, 'é': 2}


def niveau(n, texte):
    t = re.sub(r'\s+', ' ', texte).strip()
    if n == 1:
        return 1 if t in PARTIES else 2
    if n == 2 and t in PREAMBULE:
        return 2
    return n + 1


class Cadre(Extracteur):
    """Extracteur commun, plus trois traitements propres au balisage de Chrome : schémas
    (Figure) rendus en image, blocs de code, regroupement des encadrés."""

    def __init__(self, pdf, **params):
        super().__init__(pdf, **params)
        self.cadres = {}            # clé de Figure intérieure -> (page, Rect de structure)
        self.schemas = []           # [(clé intérieure, page, Rect)], dans l'ordre du texte
        self.fonds = {}             # page -> rectangles de fond pleins, larges

    def lire_page(self, page):
        def marcher(b, chemin):
            if b['type'] != 2:
                return
            cle = chemin + (b['index'],)
            enfants = [c for c in b.get('blocks', []) if c['type'] == 2]
            if b.get('raw') == 'Figure' and not any(c.get('raw') == 'Figure' for c in enfants):
                assert cle not in self.cadres, f'figure sur deux pages : {cle}'
                self.cadres[cle] = (page.number, pymupdf.Rect(b['bbox']))
            for c in b.get('blocks', []):
                marcher(c, cle)
        for b in page.get_text('dict', flags=pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            marcher(b, ())
        self.fonds[page.number] = [it['rect'] for it in page.get_drawings()
                                   if it.get('fill') and it['rect'].width > 300 and it['rect'].height > 15]
        return super().lire_page(page)

    # les lignes d'un schéma sont éparses : le recasement les disperserait
    def recaser(self):
        figs = self.feuilles & set(self.cadres)
        self.feuilles -= figs
        super().recaser()
        self.feuilles |= figs

    def code(self, cle):
        """Bloc en chasse fixe sur plusieurs lignes : texte ligne à ligne, blancs de tête
        gardés (Chrome les conserve, pre-wrap)."""
        runs = [r for r in self.runs_de(cle) if r.texte.strip()]
        if not runs or not all(MONO.search(r.police) for r in runs):
            return None
        lignes = self.lignes_visuelles(self.runs_de(cle))
        if len(lignes) < 2:
            return None
        texte = '\n'.join(''.join(r.texte for r in l).rstrip() for l in lignes)
        return '<pre><code>' + html.escape(texte, quote=False) + '</code></pre>'

    def rendre(self, cle, legende=None):
        n = self.noeuds[cle]
        interieures = [c for c in n.enfants if c in self.cadres]
        if n.role == 'Figure' and interieures:
            autres = [c for c in n.enfants if c not in interieures and self.noeuds[c].role != 'Caption'
                      and self.runs_de(c)]
            assert len(interieures) == 1 and not autres, f'figure inattendue : {cle}'
            cap = next(c for c in n.enfants if self.noeuds[c].role == 'Caption')
            p, r = self.cadres[interieures[0]]
            self.schemas.append((interieures[0], p, r))
            k = len(self.schemas)
            return (f'<figure><img src="schema-{k:02}.pdf"><figcaption>{self.en_ligne_html(cap)}'
                    '</figcaption></figure>')
        if cle in self.feuilles and n.role not in ('TD', 'TH', 'LI', 'LBody', 'Caption') \
                and not re.fullmatch(r'H\d?', n.role):
            h = self.code(cle)
            if h:
                return h
        return super().rendre(cle, legende)

    def rendre_suite(self, enfants, legende=None):
        out = super().rendre_suite(enfants, legende)
        if out and self.noeuds[out[0][0]].parent in self.racines:
            out = self.encadrer(out)
        return out

    def fond(self, cle):
        """Rectangle de fond (page, Rect) qui contient le début d'un bloc, s'il y en a un."""
        runs = [r for r in self.runs_de(cle) if r.texte.strip()]
        if not runs:
            return None
        r0 = min(runs, key=lambda r: (r.page, r.bbox[1], r.bbox[0]))
        x, y = (r0.bbox[0] + r0.bbox[2]) / 2, (r0.bbox[1] + r0.bbox[3]) / 2
        dedans = [f for f in self.fonds.get(r0.page, ()) if f.x0 <= x <= f.x1 and f.y0 <= y <= f.y1]
        return (r0.page, min(dedans, key=lambda f: f.width * f.height)) if dedans else None

    def encadrer(self, out):
        """Blocs consécutifs posés sur un même fond -> un <div> (exigence ou encadré).
        Un fond coupé par un saut de page continue en tête de la page suivante."""
        groupes = []
        for cle, h in out:
            f = None if re.match(r'<(table|figure|h\d|pre)', h) else self.fond(cle)
            g = groupes[-1] if groupes else None
            # une exigence ouvre toujours son propre groupe (deux exigences voisines
            # de part et d'autre d'un saut de page ne se fondent pas)
            neuve = EXIG.match(re.sub(r'<[^>]+>', '', h).strip())
            if f and g and g[0] and not neuve and not g[2]:
                (p0, r0), (p1, r1) = g[0], f
                meme = p0 == p1 and r0 == r1
                suite = p1 == p0 + 1 and r0.y1 > 792 - MARGES[1] - 30 and r1.y0 < MARGES[0] + 30
                if meme or suite:
                    g[0] = f
                    g[1].append((cle, h))
                    continue
            groupes.append([f, [(cle, h)], bool(neuve)])
        res = []
        for f, items, _ in groupes:
            if not f:
                res += items
                continue
            corps = '\n'.join(h for _, h in items)
            texte = re.sub(r'<[^>]+>', '', corps)
            genre = 'exig' if EXIG.match(texte.strip()) else 'encadre'
            if genre == 'exig':
                corps = re.sub(r'<p>(Pourquoi\s:.*?)</p>', lambda m: f'<div id="pourquoi-{len(res)}"><p>{m.group(1)}</p></div>',
                               corps, flags=re.S)
            res.append((items[0][0], f'<div id="{genre}-{len(res)}">\n{corps}\n</div>'))
        return res


# polices des schémas sans fichier disponible : IBM Plex Mono et Bold, Segoe UI et Consolas
# (flèches, symboles) se réécrivent en IBM Plex Sans Regular ou SemiBold
POLICE_DE_REMPLACEMENT = {'IBMPlexMono-Regular': 'IBMPlexSans-Regular', 'IBMPlexSans-Bold': 'IBMPlexSans-SemiBold',
                          'SegoeUI': 'IBMPlexSans-Regular', 'SegoeUI-Semibold': 'IBMPlexSans-SemiBold',
                          'Consolas': 'IBMPlexSans-Regular'}
FORMES = ('rect', 'ligne', 'fleche', 'rond', 'repeindre', 'copier')


def police_plex(nom):
    """Fichier d'IBM Plex Sans pour un span des schémas, cherché dans TYPST_FONT_PATHS."""
    import os
    nom = POLICE_DE_REMPLACEMENT.get(nom, nom)
    fichier = {'IBMPlexSans-Regular': 'IBMPlexSans-Regular.ttf', 'IBMPlexSans-SemiBold': 'IBMPlexSans-SemiBold.ttf'}[nom]
    for d in os.environ.get('TYPST_FONT_PATHS', '').split(os.pathsep):
        for f in pathlib.Path(d).rglob(fichier) if d else ():
            return str(f)
    sys.exit(f'police {fichier} introuvable dans TYPST_FONT_PATHS (libellés corrigés des schémas)')


def libelles(editions):
    """Couples (libellé d'origine, libellé corrigé) d'une liste d'éditions, formes exclues."""
    return [(e[0], e[1]) for e in editions if e[0] not in FORMES]


def editer_libelles(pg, r, editions):
    """Corrige un schéma dans son dessin même (revue du 3 novembre 2026). Les éditions
    s'appliquent sur la page d'origine, en points de cette page :
      (ancien, nouveau, aligne[, options]) : libellé d'une ligne. Le span d'origine est caviardé
        (texte seul, tracés gardés) puis réécrit dans sa police, sur sa ligne de base, centré
        sur l'ancien (« c »), aligné à sa gauche (« g ») ou à sa droite (« d »), réduit au besoin
        pour ne pas dépasser la largeur permise. nouveau vide : libellé retiré. ancien vide :
        ligne ajoutée, posée d'après le span modèle d'options['comme'] (police, corps, couleur,
        position), qui reste en place. Options : pres (x, y) pour choisir parmi des spans
        identiques, l (largeur maximale), dx et dy (décalage), police, corps, couleur (0xRRGGBB);
      ('rect', Rect, fond, trait, epaisseur) : rectangle peint (masque d'une flèche, par exemple);
      ('ligne', p0, p1, couleur, epaisseur[, tirets]) et ('fleche', p0, p1, couleur, epaisseur) :
        segment, et pointe pleine en p1 pour la flèche;
      ('rond', centre, rayon, fond) : pastille;
      ('repeindre', Rect, fond) : le tracé plein de ce rectangle, redessiné dans un autre fond;
      ('copier', Rect, (dx, dy)) : le tracé plein de ce rectangle, recopié décalé.
    Les formes se peignent par-dessus le dessin d'origine, les libellés par-dessus les formes;
    aucun texte d'origine ne doit rester sous une forme pleine."""
    spans = [s for b in pg.get_text('dict', clip=r)['blocks'] for l in b.get('lines', []) for s in l['spans']]
    traces = pg.get_drawings()

    def span(texte, pres=None):
        trouves = [s for s in spans if s['text'].strip() == texte]
        if pres and trouves:
            trouves = [min(trouves, key=lambda s: abs((s['bbox'][0] + s['bbox'][2]) / 2 - pres[0])
                           + abs((s['bbox'][1] + s['bbox'][3]) / 2 - pres[1]))]
        assert len(trouves) == 1, f'libellé de schéma trouvé {len(trouves)} fois : {texte}'
        return trouves[0]

    def trace(rect):
        trouves = [t for t in traces if t.get('fill') and all(abs(a - b) < 0.3 for a, b in zip(t['rect'], rect))]
        assert trouves, f'tracé plein introuvable : {rect}'
        return trouves[0]

    poses, formes, caviardes = [], [], []
    for e in editions:
        if e[0] in FORMES:
            formes.append(e)
            continue
        ancien, nouveau, aligne = e[:3]
        o = e[3] if len(e) > 3 else {}
        if ancien:
            s = span(ancien, o.get('pres'))
            b = pymupdf.Rect(s['bbox'])
            marge = s['size'] * 0.2
            pg.add_redact_annot(pymupdf.Rect(b.x0, b.y0 + marge, b.x1, b.y1 - marge), fill=False)
            caviardes.append(id(s))
        else:
            s = span(o['comme'], o.get('pres'))
        if nouveau:
            poses.append((s, nouveau, aligne, o, bool(ancien)))
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)

    pleins = []
    for f in formes:
        sh = pg.new_shape()
        if f[0] == 'rect':
            _, rect, fond, trait, ep = f
            sh.draw_rect(pymupdf.Rect(rect))
            sh.finish(fill=fond, color=trait, width=ep or 0)
            if fond:
                pleins.append(pymupdf.Rect(rect))
        elif f[0] in ('ligne', 'fleche'):
            p0, p1, couleur, ep = (pymupdf.Point(f[1]), pymupdf.Point(f[2]), f[3], f[4])
            if f[0] == 'fleche':
                # pointe des schémas d'origine : 5,4 pt de long et de large, de la couleur du trait
                # ou de celle que donne le sixième élément
                u = (p1 - p0) / abs(p1 - p0)
                base = p1 - u * 5.4
                n = pymupdf.Point(-u.y, u.x) * 2.7
                sh.draw_line(p0, base)
                sh.finish(color=couleur, width=ep)
                sh.draw_polyline([p1, base + n, base - n, p1])
                sh.finish(fill=f[5] if len(f) > 5 else couleur, color=None, closePath=True)
            else:
                sh.draw_line(p0, p1)
                sh.finish(color=couleur, width=ep, dashes=f[5] if len(f) > 5 else None)
        elif f[0] == 'rond':
            sh.draw_circle(pymupdf.Point(f[1]), f[2])
            sh.finish(fill=f[3], color=None)
        elif f[0] in ('repeindre', 'copier'):
            t = trace(f[1])
            dx, dy = f[2] if f[0] == 'copier' else (0, 0)
            d = pymupdf.Point(dx, dy)
            for it in t['items']:
                if it[0] == 'l':
                    sh.draw_line(it[1] + d, it[2] + d)
                elif it[0] == 'c':
                    sh.draw_bezier(it[1] + d, it[2] + d, it[3] + d, it[4] + d)
                elif it[0] == 're':
                    sh.draw_rect(it[1] + d)
                else:
                    raise AssertionError(f'élément de tracé non géré : {it[0]}')
            sh.finish(fill=f[2] if f[0] == 'repeindre' else t['fill'], color=None, closePath=True)
            pleins.append(pymupdf.Rect(t['rect']) + (dx, dy, dx, dy))
        sh.commit()
    for s in spans:
        if id(s) in caviardes or not s['text'].strip():
            continue
        b = pymupdf.Rect(s['bbox'])
        c = pymupdf.Point((b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2)
        assert not any(c in p for p in pleins), f'texte d’origine masqué par une forme : {s["text"]}'

    for i, (s, nouveau, aligne, o, remplace) in enumerate(poses):
        fichier = police_plex(o.get('police', s['font']))
        police = pymupdf.Font(fontfile=fichier)
        b = pymupdf.Rect(s['bbox'])
        largeur_max = o.get('l', b.width * (1.45 if aligne == 'c' else 1.6))
        taille = o.get('corps', s['size'])
        l = police.text_length(nouveau, fontsize=taille)
        if l > largeur_max:
            taille *= largeur_max / l
            l = largeur_max
        x = {'c': (b.x0 + b.x1) / 2 - l / 2, 'g': b.x0, 'd': b.x1 - l}[aligne] + o.get('dx', 0)
        c = o.get('couleur', s['color'])
        couleur = ((c >> 16 & 255) / 255, (c >> 8 & 255) / 255, (c & 255) / 255)
        nom = f'plex{i}'
        pg.insert_font(fontname=nom, fontfile=fichier)
        pg.insert_text((x, s['origin'][1] + o.get('dy', 0)), nouveau, fontname=nom, fontsize=taille, color=couleur)


def recadrer(src, p, rect, dest, runs_rect, editions=()):
    """Schéma de la page p, recadré (texte et tracés hors cadre retirés), réduit au
    besoin à la justification du gabarit; editions : libellés corrigés (LIBELLES)."""
    r = pymupdf.Rect(rect)
    if runs_rect:
        r |= runs_rect
    # les tracés débordent parfois du rectangle de structure (figure 15) : on prend
    # ceux qui le chevauchent, sauf un fond plus grand que la figure elle-même, puis,
    # de proche en proche, ceux qui chevauchent le cadre agrandi (figure 3 : le chemin
    # interdit, à gauche des couches, et son symbole d'interdiction)
    while True:
        avant = pymupdf.Rect(r)
        coeur = r + (2, 2, -2, -2)
        for it in src[p].get_drawings():
            d = it['rect']
            if d.intersects(coeur) and d.get_area() < 1.5 * r.get_area():
                r |= d
        if r == avant:
            break
    r = (r + (-4, -4, 4, 4)) & src[p].rect
    tmp = pymupdf.open()
    tmp.insert_pdf(src, from_page=p, to_page=p)
    pg = tmp[0]
    if editions:
        editer_libelles(pg, r, editions)
    W, H = pg.rect.width, pg.rect.height
    for z in ((0, 0, W, r.y0), (0, r.y1, W, H), (0, r.y0, r.x0, r.y1), (r.x1, r.y0, W, r.y1)):
        pg.add_redact_annot(pymupdf.Rect(z))
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE, graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
    s = min(1, (LARGEUR - 6) / r.width)
    out = pymupdf.open()
    page = out.new_page(width=r.width * s, height=r.height * s)
    page.show_pdf_page(page.rect, tmp, 0, clip=r)
    out.save(dest, garbage=4, deflate=True)
    return ' '.join(w[4] for w in pymupdf.open(dest)[0].get_text('words'))


def couverture(pdf):
    """Page de titre : surtitre (espacé), titre (31 pt), sous-titre (12 pt)."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    surtitre = 'Cadre de référence d’architecture d’entreprise'
    espace = next(t for s, t in lignes if s == 9)
    assert re.sub(r'\s', '', espace).lower() == re.sub(r'\s', '', surtitre).lower(), espace
    titre = ' '.join(t for s, t in lignes if s == 31)
    sous_titre = ' '.join(t for s, t in lignes if s == 12)
    return dict(surtitre=surtitre, titre=titre, sous_titre=sous_titre)


def listes_origine(blocs):
    """Entrées « Tableau N — titre » et « Figure N — titre » des listes d'origine (p. 9-10)."""
    t = html.unescape(re.sub(r'<[^>]+>', '\n', '\n'.join(b.html for b in blocs if b.page in PAGES_TDM)))
    lire = lambda genre: [(int(n), re.sub(r'\s+', ' ', x).strip()) for n, x in
                          re.findall(rf'^{genre}\s(\d+)\s—\s(.+?)\s+\d+\s*$', t, flags=re.M)]
    return lire('Tableau'), lire('Figure')


def corps(blocs, tableaux, figures):
    h = [b.html for b in blocs if b.page not in PAGES_TDM and b.page > 0]
    # p. 2 : la fiche du document passe sur la couverture
    s = '\n'.join(h)
    m = re.match(r'<h2>Fiche du document</h2>\s*(<table>.*?</table>)\s*', s, re.S)
    assert m, s[:200]
    fiche, s = m.group(1), s[m.end():]
    s = s.replace('André -Guy', 'André-Guy')
    fiche = fiche.replace('André -Guy', 'André-Guy')
    # légendes de tableaux : paragraphe en gras juste avant le tableau
    s, k = re.subn(r'<p><strong>(Tableau\xa0?\s?\d+ — [^<]*)</strong></p>\s*<table>',
                   lambda m: f'<table><caption>{m.group(1)}</caption>', s)
    legendes = [(int(n), re.sub(r'\s+', ' ', html.unescape(t)).strip())
                for n, t in re.findall(r'<caption>Tableau\s(\d+) — ([^<]*)</caption>', s)]
    assert [n for n, _ in legendes] == list(range(1, len(legendes) + 1)), legendes
    assert legendes == tableaux, set(legendes) ^ set(tableaux)
    # légendes de figures : « Figure N — titre court. Explication… »
    caps = [html.unescape(re.sub(r'<[^>]+>', '', c)).replace('\xa0', ' ')
            for c in re.findall(r'<figcaption>(.*?)</figcaption>', s, re.S)]
    assert len(caps) == len(figures) and all(c.startswith(f'Figure {n} — {t}') for c, (n, t) in zip(caps, figures)), \
        [(c[:50], t) for c, (n, t) in zip(caps, figures) if not c.startswith(f'Figure {n} — {t}')]
    # parties : « PARTIE I » espacé + H1 -> un titre de niveau 1; le chapitre suivant
    # commence sur une page neuve
    def partie(m):
        libelle = re.sub(r'\s', '', m.group(1))
        libelle = 'Annexes' if libelle == 'ANNEXES' else 'Partie ' + libelle[len('PARTIE'):]
        return f'<h1>{libelle} — {m.group(2)}</h1>'
    s, np = re.subn(r'<p><strong>((?:P ?A ?R ?T ?I ?E [IVX ]+?)|(?:A ?N ?N ?E ?X ?E ?S))</strong></p>\s*<h1>([^<]*)</h1>',
                    partie, s)
    assert np == len(PARTIES), np
    s = re.sub(r'(<h1>.*?</h1>.*?)(?=<h2>)', r'\1<div data-typst="pagebreak(weak: true)"></div>\n', s, flags=re.S)
    # exigences : identifiant et degré d'obligation sur une ligne
    s, nx = re.subn(r'(<div id="exig-\d+">\n)<p><strong><code>(EXIG-[A-Z0-9]{3}-\d{2})</code></strong></p>\n'
                    r'<p><strong>((?:NE )?(?:DOIT|DEVRAIT|PEUT)(?: PAS)?)</strong></p>',
                    r'\1<p><strong><code>\2</code> · \3</strong></p>', s)
    assert nx == s.count('<div id="exig-'), (nx, s.count('<div id="exig-'))
    # dates « 27 oct. 2026 » insécables (colonne Date de l'historique)
    s = re.sub(r'(\d{1,2}) ([a-zéû]{3,5}\.) (\d{4})', '\\1\xa0\\2\xa0\\3', s)
    # espace ordinaire collée à une insécable (lien voisin d'un « : ») : une seule
    morceaux = re.split(r'(<pre\b.*?</pre>)', s, flags=re.S)
    s = ''.join(m if i % 2 else re.sub(r' ?\xa0 ?', '\xa0', m) for i, m in enumerate(morceaux))
    # grille d'homologation (annexe A) : les renvois d'exigences, alignés à droite sur la
    # première ligne de l'item, sont lus comme un exposant en milieu de phrase; ils
    # passent en fin d'item
    def renvoi(m):
        r = re.search(r'\s*<code><sup>([^<]*)</sup></code>\s*', m.group(1))
        return f'<li>{m.group(1)[:r.start()]} {m.group(1)[r.end():]} — <code>{r.group(1)}</code></li>'
    s, nr = re.subn(r'<li>((?:(?!</li>).)*<code><sup>(?:(?!</li>).)*)</li>', renvoi, s, flags=re.S)
    assert nr == 49 and '<code><sup>' not in s, nr
    # références : en drapeau (longues URL)
    i = s.index('<h2>G Références</h2>') + len('<h2>G Références</h2>')
    s = s[:i] + '\n<div id="references">\n' + s[i:] + '\n</div>'
    # revue contradictoire du 3 novembre 2026 : correctifs faits à leur place
    s, RETIRES[:] = corriger(s)
    if HTML:
        HTML.with_suffix('.corps.html').write_text(s, encoding='utf8')
    debut = s.index('<h2>Méthode et avertissements</h2>')
    fin = s.index('<h2>', debut + 1)
    return fiche, s[:fin], s[fin:]


def main():
    e = Cadre(SRC, niveaux=niveau, marges=MARGES, pastilles=True)
    blocs = e.extraire()
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    src = pymupdf.open(SRC)

    # schémas : recadrés depuis l'original, texte compris
    travail = pathlib.Path(tempfile.mkdtemp())
    atexit.register(shutil.rmtree, travail, True)
    extras, texte_schemas = [], []
    for k, (cle, p, r) in enumerate(e.schemas, 1):
        runs = [x.bbox for x in e.runs_de(cle) if x.page == p]
        f = travail / f'schema-{k:02}.pdf'
        texte_schemas.append(recadrer(src, p, r, f, pymupdf.Rect(cadre(runs)) if runs else None,
                                      LIBELLES.get(k, ())))
        extras.append(f)
    schemas_mots = mots(' '.join(texte_schemas))
    figures_mots = collections.Counter()
    for cle, _, _ in e.schemas:
        figures_mots += mots(' '.join(x.texte for x in e.runs_de(cle)))
    # le recadrage garde tout le texte balisé du schéma, hors libellés corrigés, dont les
    # nouveaux doivent figurer dans le schéma
    perdu = figures_mots - schemas_mots - mots(' '.join(a for ed in LIBELLES.values() for a, _ in libelles(ed)))
    absents = mots(' '.join(n for ed in LIBELLES.values() for _, n in libelles(ed))) - schemas_mots
    if absents:
        sys.exit(f'libellés corrigés absents des schémas : {dict(absents)}')
    if perdu:
        sys.exit(f'recadrage des schémas incomplet : {dict(perdu)}')

    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) se retrouve dans l'extraction ou dans un schéma, aux écarts connus près
    ecarter = zones_ecartees(SRC) + [(i, src[i].rect) for i in PAGES_TDM]
    manque, surplus = controler_extraction(SRC, brut, marges=MARGES, ecarter=ecarter)
    manque -= figures_mots
    inexplique = manque - collections.Counter(ECARTS_CONNUS)
    if inexplique:
        sys.exit(f'extraction incomplète : {dict(inexplique.most_common(40))}')
    print(f'extraction : {len(blocs)} blocs, {len(e.schemas)} schémas; écarts connus seulement'
          f' ({sum(manque.values())} mots)')

    p = couverture(SRC)
    tableaux, figures = listes_origine(blocs)
    assert len(tableaux) == 69 and len(figures) == len(e.schemas) == 28, (len(tableaux), len(figures))
    fiche_html, preambule, texte = corps(blocs, tableaux, figures)
    rangs = re.findall(r'<tr><th>(?:<strong>)?(.*?)(?:</strong>)?</th><td>(.*?)</td></tr>', fiche_html)
    assert len(rangs) == 10, rangs
    # l'auteur porte son titre (forme commune à tous les livrables)
    assert [b for a, b in rangs if 'Auteur' in a] == ['André-Guy Bruneau'], rangs
    rangs = [(a, html.escape(AUTEUR) if 'Auteur' in a else b) for a, b in rangs]
    # révision 1.2 (revue contradictoire du 3 novembre 2026) : la fiche porte la version
    # courante; les valeurs d'origine remplacées sont soustraites du contrôle sans perte
    for champ, valeur in FICHE_12.items():
        rangs = [(a, (RETIRES.append(b), valeur)[1] if re.sub(r'<[^>]+>', '', a) == champ else b) for a, b in rangs]
    fiche = ('<div class="fiche"><table><tbody>' +
             ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rangs) +
             f'<tr><td>Actualisation</td><td>{ACTUALISATION}, annexe H (informative)</td></tr>'
             '</tbody></table></div>')
    annexe, refs_annexe = actualisation(ICI)
    annexe += section_h6()
    champs = {html.unescape(a): html.unescape(re.sub(r'<[^>]+>', '', b)) for a, b in rangs}
    version, date = champs['Version et date'].split(' — ')

    (travail / 'schemas.typ').write_text(SCHEMAS_TYP.replace('%FIGURES%', ', '.join(
        chaine_typst(C.typographie(f'>Figure {n} — {t}<')[1:-1]) for n, t in figures)), encoding='utf8')
    extras.append(travail / 'schemas.typ')
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#import "schemas.typ": *
#set document(title: {chaine_typst(p['titre'])},
  description: "Cadre de référence d’architecture d’entreprise {champs['Identifiant normatif']}, version {version}, {date}.",
  keywords: ("IA agentique", "interopérabilité", "orchestration", "MCP", "A2A", "OAuth", "OpenTelemetry", "Loi 25", "gouvernance"))
#show: note.with(titre-court: "{champs['Identifiant normatif']} · Cadre de référence",
  pied: [Version {version} · {date} · actualisation du {ACTUALISATION}])
#show: regles
#couverture(surtitre: {typo(p['surtitre'])}, titre: text(hyphenate: false, {typo(p['titre'])}),
  sous-titre: text(hyphenate: false, {typo(p['sous_titre'])}), auteur: {chaine_typst(AUTEUR)}, date: [Version {version} · {date}],
  fiche: include "fiche.typ")
#include "preambule.typ"
#sommaire()
#listes()
#include "corps.typ"
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    source = ' '.join(texte_controle(t) for t in (p['surtitre'], p['titre'], p['sous_titre'], fiche, preambule, texte,
                                                  annexe, refs_annexe))
    source += ' ' + ' '.join(texte_schemas)
    if HTML:
        HTML.with_suffix('.schemas.txt').write_text('\n'.join(texte_schemas), encoding='utf8')
        HTML.with_suffix('.source.txt').write_text(source, encoding='utf8')
    # les retouches du script ne perdent rien : tout mot de l'extraction (hors table des
    # matières, couverture) se retrouve dans la source composée
    perte = mots(texte_controle(vers_html([b for b in blocs if b.page not in PAGES_TDM and b.page > 0]))) - mots(source)
    # libellés de partie réécrits (« PA R T I E I V », « A N N E X E S »)
    perte -= mots('PA R T I E I V X A N N E X E S ' * 5)
    perte -= mots('Fiche du document')   # titre de la p. 2 : la fiche passe sur la couverture
    perte -= mots(texte_controle(' '.join(RETIRES)))   # mots retirés par les correctifs (corrections.py)
    assert not perte, perte
    composer({'fiche': fiche, 'preambule': preambule, 'corps': texte, 'actualisation': annexe,
              'references-actualisation': refs_annexe}, main_typ, OUT, source, extras=extras)
    verifier_numeros(OUT, tableaux, figures)


def section_h6():
    """Annexe H, section H.6 : registre des correctifs de la revue du 3 novembre 2026,
    tiré du JOURNAL de chaque module de correctifs (corrections.py)."""
    from corrections import journal
    e = html.escape
    from corrections import modules
    suivi_m = dict(modules()).get('99_w_suivi')
    SUIVI, FAUX = (suivi_m.SUIVI, suivi_m.FAUX) if suivi_m else ({}, set())
    lignes = list(journal())
    non = lambda l: l[1].lower().startswith('non retenu')
    ids = lambda l: [c for c in (l[2] if len(l) > 2 else []) if not c.startswith('A-') and c != 'lissage']
    retenus, ecartes = [], []
    for i, l in enumerate(lignes):
        if not non(l):
            retenus.append(l)
            continue
        # un constat laissé « non retenu » à une étape, puis corrigé par un module ultérieur ou par
        # un arbitrage, passe au tableau 73 avec l'endroit de sa correction; seul un constat
        # démontré faux reste au tableau 74
        plus_tard = {c for x in lignes[i + 1:] if not non(x) for c in ids(x)}
        cs = ids(l)
        if cs and not any(c in FAUX for c in cs) and all(c in plus_tard or c in SUIVI for c in cs):
            ou = sorted({SUIVI[c] for c in cs if c in SUIVI})
            retenus.append((l[0], 'Corrigé à une étape ultérieure : ' + ('; '.join(ou) if ou else 'voir les lignes '
                            'suivantes du tableau') + '. Motif de l’étape initiale : ' + l[1], l[2]))
        else:
            assert any(c in FAUX for c in cs), f'constat non retenu sans correctif ni preuve de fausseté : {l}'
            ecartes.append(l)
    def rangee(l):
        loc, nature, constats = l[0], l[1], l[2] if len(l) > 2 else []
        return f'<tr><td>{e(loc)}</td><td>{e(nature)}</td><td>{e(", ".join(constats))}</td></tr>'
    def tableau(n, titre, ls):
        return (f'<table>\n<caption>Tableau {n} — {titre}</caption>\n'
                '<thead><tr><th>Où</th><th>Correctif</th><th>Constats</th></tr></thead>\n<tbody>\n'
                + '\n'.join(rangee(l) for l in ls) + '\n</tbody>\n</table>\n')
    return (
        '\n<h3>H.6 Revue contradictoire du 3 novembre 2026 : correctifs appliqués</h3>\n'
        '<p>Contrairement aux sections H.1 à H.5, cette section consigne des modifications du corps. '
        'Le 3 novembre 2026, une revue contradictoire a audité les 283 pages de la version 1.1 en 29 tranches '
        'de douze pages qui se recouvrent, consolidé environ 860 constats en 623 défauts (14 bloquants, 216 '
        'majeurs, 393 mineurs), vérifié 83 faits externes à leur source primaire et retenu 34 arbitrages '
        'transversaux. Ses correctifs sont faits à leur place dans la version 1.2; l’historique des versions '
        'les résume. Les identifiants existants sont conservés; neuf exigences sont ajoutées (296 au total). '
        'Les schémas, recadrés de l’édition d’origine, sont corrigés dans le dessin même (libellés réécrits dans '
        'leur police, cases, traits et flèches redessinés) pour les figures 1 à 7, 9 à 19, 21 à 23, 25, 26 et 28; '
        'les mentions « figure non modifiable » du tableau 73 renvoient à l’état antérieur à ces corrections.</p>\n'
        f'<p>Le tableau 73 liste les {len(retenus)} correctifs, dans l’ordre du document; les numéros de '
        'constats renvoient au rapport de la revue (tranche-numéro). Tout constat de la revue y figure, y compris '
        'ceux qu’une étape a d’abord laissés et qu’une étape ultérieure, une précision ou un arbitrage a corrigés; '
        'un constat dont la prémisse était fausse y figure avec le correctif du défaut réel qu’il signalait. '
        'Une seule mesure demandée n’a pu être prise : le symbole distinct pour « contredite » au tableau 69 '
        'suppose un verdict par référence que les ébauches n’ont pas conservé (seuls les totaux du tableau 67 '
        'subsistent); la légende du tableau 69 le dit.</p>\n'
        + tableau(73, 'Correctifs de la revue contradictoire du 3 novembre 2026, appliqués dans la version 1.2', retenus)
        + (tableau(74, 'Constats de la revue du 3 novembre 2026 démontrés faux, sans correctif', ecartes)
           if ecartes else ''))


def verifier_numeros(pdf, tableaux, figures):
    """Les légendes du PDF composé portent les numéros d'origine, dans l'ordre."""
    t = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf)).replace('­', ''))
    for genre, liste in (('Tableau', tableaux), ('Figure', figures)):
        for n, titre in liste:
            assert t.count(f'{genre} {n} — {titre}') >= 2, f'{genre} {n} introuvable (légende et liste)'
    print(f'numérotation : {len(tableaux)} tableaux et {len(figures)} figures, légendes et listes conformes')


SCHEMAS_TYP = r'''// Règles propres au Cadre de référence, appliquées après #show: note.
#import "gabarit.typ": *
#let titres-figures = (%FIGURES%,)

#let regles(body) = {
  // numéros des tableaux et figures : ceux de l'original, en toutes lettres
  set figure(numbering: none)
  show figure.where(kind: table): set figure.caption(position: top)
  show figure.caption.where(position: top): it => block(sticky: true, it)
  show figure.where(kind: image): set block(above: 14pt, below: 16pt)
  // identifiants en chasse fixe (EXIG-AUT-09, tools/call) : insécables. Une URL (texte
  // d'un lien, que Typst coupe à n'importe quel signe) ou un long nom : coupé seulement
  // après « / » ou « - », chaque morceau insécable.
  show raw.where(block: false): it => {
    if it.text.len() <= 40 { return if it.text.contains(" ") { it } else { box(it) } }
    let morceaux = it.text.matches(regex("[^/-]+[/-]*|[/-]+")).map(m => m.text)
    if morceaux.len() <= 1 { return it }
    morceaux.map(m => raw(m)).join(sym.zws)
  }
  // blocs de code : lignes de Chrome gardées; 6,8 pt pour que la plus longue (109
  // signes) tienne sur la justification
  show raw.where(block: true): it => block(width: 100%, fill: zebre, inset: 7pt, radius: 2pt,
    stroke: 0.4pt + filet, text(size: 6.8pt, it))
  // exigences et encadrés : <div id="exig-N"> et <div id="encadre-N"> de l'extraction
  show block: it => {
    if not it.has("label") { return it }
    let l = str(it.label)
    if l.starts-with("exig-") {
      set par(spacing: 0.6em)
      block(width: 100%, breakable: true, above: 12pt, below: 12pt, inset: (left: 11pt, right: 8pt, y: 7pt),
        stroke: (left: 2.5pt + accent, top: 0.4pt + filet, bottom: 0.4pt + filet, right: 0.4pt + filet), it.body)
    } else if l == "references" {
      set par(justify: false)
      it.body
    } else if l.starts-with("encadre-") {
      block(width: 100%, breakable: true, above: 12pt, below: 12pt, inset: 9pt, radius: 2pt,
        fill: accent-pale, it.body)
    } else if l.starts-with("pourquoi-") {
      set text(size: 9.6pt, fill: gris)
      it.body
    } else { it }
  }
  body
}

// Listes des tableaux et des figures, régénérées (titres courts des figures : ceux de
// la liste d'origine).
#let entree(titre, loc) = {
  set par(justify: false, hanging-indent: 1.2em)
  link(loc, titre)
  h(4pt)
  box(width: 1fr, repeat(gap: 3pt)[.])
  h(2pt)
  link(loc, str(counter(page).at(loc).first()))
  linebreak()
}
#let listes() = page(header: none, {
  set text(font: sans, size: 8.6pt)
  for (titre, corps) in (
    ([Liste des tableaux], context {
      for f in query(figure.where(kind: table)).filter(f => f.caption != none) {
        entree(f.caption.body, f.location())
      }
    }),
    ([Liste des figures], context {
      let fs = query(figure.where(kind: image))
      assert(fs.len() == titres-figures.len(), message: "figures : " + str(fs.len()))
      for (f, t) in fs.zip(titres-figures) { entree(t, f.location()) }
    }),
  ) {
    v(24pt, weak: true)
    text(size: 18pt, weight: "semibold", fill: accent, titre)
    v(4pt)
    line(length: 100%, stroke: 0.6pt + filet)
    v(8pt)
    corps
  }
})
'''

if __name__ == '__main__':
    main()
