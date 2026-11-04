"""Correctifs de la revue du 3 novembre 2026 — tranche : Partie III (chapitres 9 et 10)."""
import re

NBSP = '\xa0'


def fr(t):
    """Typographie du corps : insécables avant « : % $ » et après « », séparateur des milliers."""
    t = re.sub(r' (?=[:%$»])', NBSP, t)
    t = t.replace('« ', '«' + NBSP).replace('$ US', '$' + NBSP + 'US')
    t = re.sub(r'(?<=\d) (?=\d{3}(?!\d))', ' ', t)
    return t


_C = [
    # ---------------------------------------------------------------- § 9.1
    # [3.78] IAM-01 : communication réseau, force explicite, stdio local renvoyé à MCP-08
    ('Toute communication entre composants est mutuellement authentifiée et chiffrée, y compris à l’intérieur d’un réseau privé.</p>',
     'Toute communication réseau entre composants <strong>DOIT</strong> être mutuellement authentifiée et chiffrée (mTLS ou équivalent), y compris à l’intérieur d’un réseau privé; le transport stdio local relève de l’EXIG-MCP-08.</p>',
     ['3.78']),
    # [3.76, 3.41] IAM-02 : appels de modèle; état de tâche cohérent entre instances
    ('<p>Chaque appel d’un agent vers un outil, une ressource ou un autre agent <strong>DOIT</strong> être authentifié et autorisé individuellement. Le point d’application applique la décision',
     '<p>Chaque appel d’un agent vers un outil, une ressource, un modèle ou un autre agent <strong>DOIT</strong> être authentifié et autorisé individuellement. Le point d’application (passerelle d’agents ou, pour un appel de modèle, passerelle de modèles) applique la décision',
     ['3.76']),
    ('l’état de la tâche et les signaux de risque. Aucune autorisation n’est héritée',
     'l’état de la tâche et les signaux de risque. L’état de la tâche (contenu non fiable consommé, données sensibles consultées, budget, compteurs) est tenu dans un magasin à cohérence forte, partagé par toutes les instances du point d’application; un état illisible ou indisponible impose le refus (EXIG-IAM-18, EXIG-IAM-22). Aucune autorisation n’est héritée',
     ['3.41', 'A-17']),
    # [3.77] exemple : une écriture P2 sous le seuil, que seule la décision par appel arrête
    ('À l’étape 4, il tente d’appeler l’outil d’envoi de courriels. Parce que la décision est prise à chaque appel, la passerelle sait que la session a consommé du contenu non fiable et refuse l’envoi sans approbation humaine (section 9.6).',
     'À l’étape 4, il tente d’écrire une note dans le dossier du client, une écriture P2 sous le seuil qu’il exécute seul d’ordinaire. Parce que la décision est prise à chaque appel, la passerelle sait que la session a consommé du contenu non fiable et soumet cette écriture à une approbation humaine de l’action exacte (EXIG-SEC-04, section 9.6).',
     ['3.77']),
    # ---------------------------------------------------------------- § 9.2
    # [A-31] brouillons WIMSE réépinglés
    ('(AIMS, <code>draft-ietf-wimse-aims-00</code>, 15 septembre 2026)',
     '(AIMS, <code>draft-ietf-wimse-aims-00</code>, 15 septembre 2026; une révision -01 a paru le 2 novembre 2026, et les passages cités ici sont ceux de la -00)',
     ['A-31']),
    ('soumis le 30 juin 2026 au groupe de pilotage de l’ingénierie Internet (IESG))',
     'soumis le 30 juin 2026 au groupe de pilotage de l’ingénierie Internet (IESG); la révision -08 du 30 octobre 2026 est en dernier appel IETF jusqu’au 13 novembre 2026)',
     ['A-31']),
    # [3.80, A-34] gabarit Entra : justificatif partagé; rôles d’Entra
    ('désactiver le gabarit bloque toutes ces identités. Chaque agent a un parrain <em>(sponsor)</em>, responsable métier, et un propriétaire, responsable technique<strong><sup>[90]</sup></strong>.',
     'désactiver le gabarit bloque toutes ces identités, ce qui en fait un justificatif partagé que l’EXIG-IAM-04 encadre. Chaque agent a un parrain <em>(sponsor)</em>, responsable métier, et un propriétaire <em>(owner)</em>, responsable technique<strong><sup>[90]</sup></strong>; un gestionnaire <em>(manager)</em> s’y ajoute pour l’agent qui dispose d’un compte d’utilisateur.',
     ['3.80', 'A-34']),
    # [3.79, 3.80] IAM-04 : JWT-SVID réémis; justificatif commun d’une plateforme
    ('de courte durée, renouvelé automatiquement et valide au plus pour la vie de l’instance : X.509-SVID (à privilégier) ou JWT-SVID SPIFFE, ou identité fédérée OIDC du fournisseur infonuagique. Les justificatifs sont isolés par environnement (développement, essai, production).</p>',
     'de courte durée, renouvelé automatiquement ou réémis à la demande par la plateforme, et valide au plus pour la vie de l’instance : X.509-SVID (à privilégier) ou JWT-SVID SPIFFE, ou identité fédérée OIDC du fournisseur infonuagique. Les justificatifs sont isolés par environnement (développement, essai, production). Lorsqu’une plateforme émet les jetons de plusieurs identités à partir d’un justificatif commun (p. ex. le gabarit de Microsoft Entra Agent ID), ce justificatif <strong>DOIT</strong> être fédéré ou géré par la plateforme, sans secret client (EXIG-IAM-05), et le profil de la plateforme inscrit au catalogue définit ce que vaut l’instance au sens de la présente exigence.</p>',
     ['3.79', '3.80']),
    ('un justificatif émis par la plateforme est de courte durée, se renouvelle seul,',
     'un justificatif émis par la plateforme est de courte durée, se renouvelle ou se réémet sans intervention,',
     ['3.79']),
    # [3.18, A-15] IAM-06 : circulation des jetons
    ('dans les arguments d’un outil ou dans les traces. Les jetons sont manipulés par le code d’exécution de l’agent ou injectés par la passerelle (EXIG-IAM-19).</p>',
     'dans les arguments d’un outil, dans un message logique, dans un point de contrôle, dans le journal de compensation ou dans les traces. Jetons délégués et jetons d’approbation circulent dans les en-têtes d’authentification du transport; ils sont injectés et retirés par le code d’exécution de l’agent ou par la passerelle (EXIG-IAM-19). Le jeton d’approbation est conservé par la passerelle, qui ne le remet ni à l’agent ni à son modèle (EXIG-AUT-12); un message de délégation porte une référence de délégation, non le jeton (EXIG-ORC-23).</p>',
     ['3.18', 'A-15']),
    # [3.81, 3.02, A-05, A-06] IAM-07 : orphelins renvoyés à GOV-13; compensations
    ('puis propager la suppression aux systèmes raccordés. Le parrain atteste au moins tous les 12 mois (tous les 6 mois pour un agent de classe de risque élevée) que l’agent est encore requis. Une revue trimestrielle détecte les agents orphelins (sans parrain, sans fiche à jour ou inactifs), qui sont désactivés (section 11.5).</p>',
     'puis propager la suppression aux systèmes raccordés. Les compensations des sagas en cours de l’agent retiré s’exécutent sous l’identité de compensation (EXIG-ORC-31), que ce retrait ne révoque pas. L’attestation du parrain et la revue des agents orphelins suivent l’EXIG-GOV-13; la désactivation qui en résulte révoque l’identité et les justificatifs selon la présente exigence.</p>',
     ['3.81', '3.02', 'A-05', 'A-06']),
    ('Les périodicités sont des choix du cadre, inscrits dans la plage recommandée par Microsoft.</p>',
     'Les périodicités sont celles de l’EXIG-GOV-13.</p>',
     ['3.81']),
    # [3.82, 4.66] tableau 34, NHI3 : couverture partielle déclarée
    ('<td>EXIG-IAM-17; chaîne d’approvisionnement (section 9.8); clauses (section 13.3)</td>',
     '<td>Couverture partielle : clauses (section 13.3) et chaîne d’approvisionnement (section 9.8); EXIG-IAM-17 pour les appels sortants. Aucun inventaire des octrois accordés à des tiers n’est encore exigé.</td>',
     ['3.82', '4.66']),
    # ---------------------------------------------------------------- § 9.3
    # [4.53] paramètres obligatoires de la RFC 8693
    ('Dans la requête, <code>subject_token</code> (le jeton du mandant) est obligatoire;',
     'Dans la requête, <code>grant_type</code> (<code>urn:ietf:params:oauth:grant-type:token-exchange</code>), <code>subject_token</code> (le jeton du mandant) et <code>subject_token_type</code> sont obligatoires;',
     ['4.53']),
    # [4.55, 4.06, A-16] légende de la figure 17 (figure non modifiable)
    ('Les droits effectifs ne dépassent jamais l’intersection des trois ensembles. Source : CRE-IA-2026-01, d’après la RFC 8693 et la RFC 9068.</figcaption>',
     'Les droits effectifs ne dépassent jamais l’intersection des trois ensembles. Le schéma simplifie trois points que le texte précise : après vérification, la passerelle obtient pour le serveur un jeton qui la désigne comme client, sans ajouter de niveau d’<code>act</code> (EXIG-IAM-14); le serveur MCP et le système cible, réunis dans une même boîte, sont deux audiences distinctes (EXIG-IAM-12); le jeton représenté est un extrait, et « SVID » y désigne le JWT-SVID présenté comme <code>actor_token</code>. Source : CRE-IA-2026-01, d’après la RFC 8693 et la RFC 9068.</figcaption>',
     ['4.55', '4.06', 'A-16']),
    # [A-16, 4.03, 4.10] chaîne à travers la passerelle; extrait du second jeton
    ('Le jeton obtenu conserve le mandant et ajoute un niveau d’<code>act</code>, comme dans l’extrait suivant (l’exemple complet figure à l’annexe C).</p>\n'
     '<p><strong>Jeton délégué après deux sauts (extrait)</strong></p>\n'
     '<pre><code>{\n'
     '  "iss": "https://idp.ent.ca",\n'
     '  "sub": "alice",\n'
     '  "aud": "https://mcp-finance.ent.ca",\n'
     '  "client_id": "agent-analyse-depenses",\n'
     '  "scope": "finance:read",\n',
     'Le jeton obtenu conserve le mandant et ajoute un niveau d’<code>act</code>. L’agent le présente à la passerelle (<code>aud</code> désignant la passerelle, <code>cnf</code> lié à l’agent); la passerelle vérifie la liaison, puis obtient pour le serveur un jeton qui la désigne comme client et lui est lié, sans ajouter de niveau d’<code>act</code> (EXIG-IAM-14). L’extrait suivant montre ce second jeton; la portée de la tâche y figure dans <code>authorization_details</code> (EXIG-IAM-10), et l’exemple complet figure à l’annexe C.</p>\n'
     '<p><strong>Jeton délégué après deux sauts, remis par la passerelle au serveur (extrait)</strong></p>\n'
     '<pre><code>{\n'
     '  "iss": "https://idp.ent.ca",\n'
     '  "sub": "alice",\n'
     '  "aud": "https://mcp-finance.ent.ca",\n'
     '  "client_id": "passerelle-agents",\n'
     '  "scope": "finance:read",\n'
     '  "authorization_details": [{ "type": "lecture_depenses", "periode": "2026-T3" }],\n',
     ['A-16', '4.03', '4.10']),
    # [4.05, 4.06, 4.09, A-16] IAM-08 : durée, liaison du subject_token, profondeur, variante
    ('Le jeton émis porte <code>sub</code> (le mandant) et <code>act</code> (l’agent courant), avec un <code>act</code> imbriqué par acteur antérieur. Avant d’émettre, le serveur d’autorisation <strong>DOIT</strong> vérifier que l’agent est autorisé à agir pour ce mandant (<code>may_act</code> ou politique équivalente) et que la profondeur d’imbrication de <code>act</code> ne dépasse pas deux niveaux (EXIG-ORC-04). Une variante de fournisseur est admise si son profil, inscrit au catalogue, démontre le même résultat.</p>',
     'Le jeton émis porte <code>sub</code> (le mandant, toujours l’entité d’origine) et <code>act</code> (l’agent courant), avec un <code>act</code> imbriqué par acteur antérieur. Avant d’émettre, le serveur d’autorisation <strong>DOIT</strong> vérifier que l’agent est autorisé à agir pour ce mandant (<code>may_act</code> ou politique équivalente) et que la profondeur d’imbrication de <code>act</code> ne dépasse pas deux niveaux (EXIG-ORC-04); il refuse l’échange qui l’excède. La profondeur ne compte que les agents inscrits au registre : la passerelle qui refait l’échange vers le serveur (EXIG-IAM-14) et un serveur MCP qui obtient un jeton pour son propre système cible (EXIG-IAM-12) n’y ajoutent aucun niveau et sont consignés à l’audit. Le serveur d’autorisation <strong>DOIT</strong> en outre : (a) émettre un <code>exp</code> au plus égal à celui du <code>subject_token</code>, de sorte qu’aucun échange ne prolonge une délégation; (b) refuser tout échange au-delà de la durée maximale de chaîne inscrite à la fiche, comptée depuis l’authentification du mandant (<code>auth_time</code>); (c) rejeter tout <code>subject_token</code> dont <code>aud</code> ne désigne pas l’acteur demandeur, ou dont la liaison (<code>cnf</code>) ne désigne ni cet acteur ni la passerelle. Une variante de fournisseur est admise si son profil, inscrit au catalogue, démontre le même résultat : audience unique, identifiant unique du jeton, client identifiable, mandant et chaîne d’acteurs complète; à défaut de chaîne, la délégation est limitée à un saut, ou le jeton est réémis par une passerelle conforme à la RFC 9068.</p>',
     ['4.05', '4.06', '4.09', 'A-16']),
    # [4.54] IAM-09 : la présentation au serveur d’autorisation reste permise
    ('aucun agent ne réutilise le jeton, la session ou le mot de passe d’une personne.</p>',
     'aucun agent ne présente le jeton d’une personne à un service autre que le serveur d’autorisation, à titre de <code>subject_token</code> (EXIG-IAM-12), ni ne réutilise sa session ou son mot de passe.</p>',
     ['4.54']),
    # [4.03, A-16] exemple d’Alice : la portée de la tâche représentée dans le jeton
    ('la tâche porte sur les dépenses du troisième trimestre. Le jeton délégué permet donc de lire les dépenses du troisième trimestre de l’unité d’Alice, et rien d’autre.</p>',
     'la tâche porte sur les dépenses du troisième trimestre, que le jeton délégué porte dans <code>authorization_details</code>. Le serveur d’autorisation borne la portée (agent et tâche), et le serveur de ressources applique les droits d’Alice d’après <code>sub</code> : le jeton délégué permet donc de lire les dépenses du troisième trimestre de l’unité d’Alice, et rien d’autre. Sans cette représentation de la tâche, il permettrait de lire toutes les dépenses de l’unité.</p>',
     ['4.03', 'A-16']),
    ('à partir des <code>act</code> imbriqués : elle s’applique au serveur d’autorisation, à chaque échange<strong><sup>[70]</sup></strong>.',
     'à partir des <code>act</code> imbriqués : le serveur d’autorisation borne les portées à chaque échange, et le serveur de ressources applique à chaque appel les droits du mandant désigné par <code>sub</code><strong><sup>[70]</sup></strong>.',
     ['4.03', 'A-16']),
    ('l’agent démarre avec peu de droits et en obtient davantage par une demande traçable.</p>',
     'l’agent démarre avec peu de droits et en obtient davantage par une demande traçable, qui, dans une chaîne, remonte au mandant (EXIG-IAM-10).</p>',
     ['4.04']),
    # [4.03, 4.04, A-16] IAM-10 : représentation de la tâche, changement d’audience, demande incrémentale
    ('de la portée accordée à l’agent au registre et de la portée nécessaire à la tâche. Une portée ne s’élargit jamais d’un saut à l’autre. Une portée manquante s’obtient par une demande incrémentale explicite, journalisée et limitée en nombre de tentatives, jamais par un jeton plus large obtenu d’avance.</p>',
     'de la portée accordée à l’agent au registre et de la portée nécessaire à la tâche; le serveur de ressources applique, à chaque appel, les droits du mandant d’après <code>sub</code>. La portée de la tâche <strong>DOIT</strong> être représentée dans le jeton, par <code>authorization_details</code> (RFC 9396) ou par une portée paramétrée inscrite au catalogue, et appliquée par la cible. Le mandant d’une chaîne est toujours l’entité d’origine; un agent intermédiaire n’apparaît que comme <code>act</code>. Une portée ne s’élargit jamais d’un saut à l’autre : le jeton remis à un agent intermédiaire porte les portées en aval autorisées pour la tâche, chaque échange émet au plus l’intersection de cette liste, du registre et de la tâche, et changer d’audience sans élargir la liste est permis. Une portée absente de la liste s’obtient par une demande incrémentale remontée au mandant, approuvée par lui (section 8.5) et journalisée, qui réémet la chaîne depuis le premier saut; pour un agent autonome, par une modification revue du registre, jamais à l’exécution. Les tentatives sont plafonnées à trois par tâche, sauf valeur plus stricte à la fiche. Aucun jeton plus large n’est obtenu d’avance.</p>',
     ['4.03', '4.04', 'A-16']),
    ('la formule à trois termes est un choix du cadre.</p>',
     'la formule à trois termes, sa répartition entre serveur d’autorisation et serveur de ressources et le plafond de tentatives sont des choix du cadre. Le cadre a écarté les capacités atténuables (macarons), faute de révocation, d’audience et d’audit centralisés.</p>',
     ['4.04', 'A-16']),
    # [4.09, 4.52, A-16] IAM-11 : variante admise; revendications de premier niveau
    ('<code>iat</code> et <code>jti</code> présents). Le serveur de ressources rejette tout jeton dont <code>aud</code> ne le désigne pas, fonde sa décision sur <code>sub</code> et sur l’acteur courant seulement, et journalise les deux; les acteurs antérieurs servent à l’audit.</p>',
     '<code>iat</code> et <code>jti</code> présents); une variante de fournisseur est admise aux conditions de l’EXIG-IAM-08. Le serveur de ressources rejette tout jeton dont <code>aud</code> ne le désigne pas, fonde sa décision sur les revendications de premier niveau (dont <code>sub</code>, <code>scope</code>, <code>aud</code> et <code>cnf</code>) et sur l’acteur courant seulement, jamais sur les acteurs antérieurs, et journalise le mandant et l’acteur courant; les acteurs antérieurs servent à l’audit. Derrière la passerelle, le jeton présenté au serveur est celui que la passerelle obtient pour lui (EXIG-IAM-14).</p>',
     ['4.09', '4.52', 'A-16']),
    # [4.99 e, A-31] OAuth 2.1 réépinglé
    ('(<code>draft-ietf-oauth-v2-1-16</code>, septembre 2026, expirant le 7 mars 2027)<strong><sup>[176]</sup></strong>.',
     '(<code>draft-ietf-oauth-v2-1-16</code>, septembre 2026, expirant le 7 mars 2027; la révision -17 du 31 octobre 2026, qui expire le 4 mai 2027, l’a remplacée depuis)<strong><sup>[176]</sup></strong>.',
     ['4.99', 'A-31']),
    # [4.56] tableau 35 : PKCE pour tous les clients
    ('PKCE pour les clients publics,',
     'PKCE pour tous les clients (choix du cadre, EXIG-IAM-13),',
     ['4.56']),
    ('<td>Brouillon <code>draft-ietf-oauth-v2-1-16</code> <strong>[327]</strong></td>',
     '<td>Brouillon <code>draft-ietf-oauth-v2-1-16</code> (-17 depuis le 31 octobre 2026) <strong>[327]</strong></td>',
     ['4.99', 'A-31']),
    # [4.10] tableau 35 : liaison derrière une passerelle qui termine TLS
    ('la ressource rejette la requête si le certificat diffère.',
     'la ressource rejette la requête si le certificat diffère; derrière une passerelle qui termine TLS, la liaison se vérifie à la passerelle (EXIG-IAM-14).',
     ['4.10']),
    # [4.56] IAM-13 : sujets de l’exigence; décompte des points plus stricts
    ('<p>Le fournisseur d’identité, la passerelle d’agents et les serveurs exposés aux agents <strong>DOIVENT</strong> appliquer le profil du tableau 35',
     '<p>Le fournisseur d’identité, la passerelle d’agents, les clients OAuth (hôtes et agents) et les serveurs exposés aux agents <strong>DOIVENT</strong> appliquer, chacun pour son rôle, le profil du tableau 35',
     ['4.56']),
    ('Le cadre est plus strict que la RFC 9700 sur deux points : celle-ci déconseille l’octroi implicite (NE DEVRAIT PAS) et ne fait que recommander l’authentification asymétrique des clients (choix du cadre).</p>',
     'Le cadre est plus strict que la RFC 9700 sur plusieurs points, dont ces trois choix du cadre : celle-ci déconseille l’octroi implicite (NE DEVRAIT PAS) et ne fait que recommander PKCE pour les clients confidentiels et l’authentification asymétrique des clients.</p>',
     ['4.56']),
    # [4.10, 4.57, A-16] IAM-14 : périmètre P1 sensible; liaison à travers la passerelle
    ('<p>Tout jeton qui donne accès à un outil P2 ou P3, ou qui est détenu par un agent de classe de risque élevée, <strong>DOIT</strong> être lié',
     '<p>Tout jeton qui donne accès à un serveur exposant un outil P2 ou P3, ou un outil P1 portant sur des RP ou des données classifiées, ou qui est détenu par un agent de classe de risque élevée, <strong>DOIT</strong> être lié',
     ['4.57']),
    ('ou DPoP (RFC 9449) hors du maillage. Pour les autres jetons,',
     'ou DPoP (RFC 9449) hors du maillage. Derrière une passerelle qui termine TLS, la liaison se vérifie à la passerelle : l’agent lui présente un jeton dont <code>aud</code> désigne la passerelle et <code>cnf</code> l’agent; la passerelle vérifie <code>cnf</code>, puis obtient par échange un jeton pour le serveur (<code>aud</code> égal au serveur, <code>client_id</code> et <code>cnf</code> désignant la passerelle, <code>act</code> égal à l’agent, acteurs antérieurs imbriqués), et le serveur <strong>DOIT</strong> n’accepter que la passerelle, par mTLS. Cet échange n’ajoute aucun niveau de profondeur (EXIG-IAM-08). Pour les autres jetons,',
     ['4.10', 'A-16']),
    # [4.08, 4.15, A-05, A-16] IAM-15 : borne liée au coupe-circuit; mandat d’agent ambiant
    ('<p><strong><code>EXIG-IAM-15</code> · DEVRAIT</strong></p>',
     '<p><strong><code>EXIG-IAM-15</code> · DOIT</strong></p>',
     ['4.15', 'A-05']),
    ('La délégation de longue durée d’un agent ambiant est régie par l’EXIG-AUT-18 (échéance inscrite à la fiche, renouvelée par une personne habilitée).</p>',
     'Un jeton destiné à un système qui ne prend en charge ni SSF ni CAEP <strong>DOIT</strong> avoir une durée de vie au plus égale à la cible du coupe-circuit (EXIG-IAM-20), ou ce système <strong>DOIT</strong> n’être joignable que par la passerelle. La délégation de longue durée d’un agent ambiant <strong>DOIT</strong> être un consentement inscrit au serveur d’autorisation : celui-ci émet, à la demande de l’agent authentifié, des jetons d’au plus 15 minutes, ou de la durée minimale du fournisseur si elle est plus longue (<code>sub</code> égal au mandant, <code>act</code> égal à l’agent), tant que le mandat est valide et que le mandant est actif; l’agent ne stocke aucun jeton de la personne, jeton de rafraîchissement compris. Le mandat est révoqué automatiquement au départ ou au changement de rôle du mandant, et son échéance suit l’EXIG-AUT-18 (inscrite à la fiche, renouvelée par une personne habilitée).</p>',
     ['4.08', '4.15', 'A-05', 'A-16']),
    ('<div id="pourquoi-813"><p>Pourquoi : la cible de 15 minutes est un choix du cadre;',
     '<div id="pourquoi-813"><p>Pourquoi : la cible de 15 minutes est un choix du cadre; un jeton émis vers un système sans SSF ni CAEP reste valide jusqu’à son expiration, d’où la borne liée au coupe-circuit;',
     ['4.15']),
    # [4.07, 4.58] IAM-16 : chaîne d’agents autonomes; renvoi à IAM-09
    ('Il ne partage jamais un jeton avec un autre agent et n’emprunte jamais l’identité d’une personne pour élargir ses droits.</p>',
     'Il ne partage jamais un jeton avec un autre agent et n’emprunte jamais l’identité d’une personne (EXIG-IAM-09). Lorsqu’un agent autonome délègue à un autre agent, l’agent initiateur tient lieu de mandant : l’échange de l’EXIG-IAM-08 s’applique avec <code>sub</code> égal au principal de l’initiateur et <code>act</code> égal à l’agent courant, et l’intersection de l’EXIG-IAM-10 porte sur les droits de l’initiateur.</p>',
     ['4.07', '4.58']),
    # [4.59, 4.99 e, A-31] tableau 36 : révisions postérieures et état IETF
    ('<td>Brouillon de groupe de travail, version -16 (septembre 2026)<strong><sup>[176]</sup></strong></td>',
     '<td>Brouillon de groupe de travail, version -16 (septembre 2026); version -17 du 31 octobre 2026 depuis<strong><sup>[176]</sup></strong></td>',
     ['4.99', 'A-31']),
    ('<td>Brouillon -04 (21 mai 2026); extension MCP stable depuis 2026-07-28',
     '<td>Brouillon -04 (21 mai 2026), -06 du 31 octobre 2026 depuis; extension MCP stable depuis 2026-07-28',
     ['4.99', 'A-31']),
    ('consensus du groupe atteint, en attente du rapport',
     'consensus du groupe atteint, en attente de la fiche de synthèse du responsable du document <em>(write-up)</em>',
     ['4.59']),
    ('<td>Brouillon de groupe de travail -02 (15 juin 2026) <strong>[334]</strong></td>',
     '<td>Brouillon de groupe de travail -02 (15 juin 2026), -03 du 2 novembre 2026 depuis <strong>[334]</strong></td>',
     ['A-31']),
    # ---------------------------------------------------------------- § 9.4
    # [A-01, A-02] la passerelle parmi les points d’application
    ('Les décisions viennent du service de politiques; la passerelle les applique et en garde la trace.',
     'Les décisions viennent du service de politiques; la passerelle les applique et en garde la trace. Elle n’est pas le seul point d’application : la passerelle de modèles régit l’inférence et le courtier d’événements la publication et la consommation (EXIG-EVT-11); toute action P2 ou P3 passe toutefois par elle (EXIG-IAM-17).',
     ['A-01', 'A-02']),
    # [4.11, 4.14, 4.61, A-19] légende de la figure 18 (figure non modifiable)
    ('Un refus à n’importe quelle étape arrête l’appel; le coupe-circuit agit sur toutes les passerelles à la fois. Source : CRE-IA-2026-01.</figcaption>',
     'Un refus à n’importe quelle étape arrête l’appel; le coupe-circuit agit sur toutes les passerelles à la fois. Le schéma simplifie trois points que la liste ci-dessous précise : pour un appel P2 ou P3, l’enregistrement d’intention est écrit avant le relais (EXIG-OBS-11), et non au seul retour; le contrôle 5 vise aussi toute écriture d’un agent de niveau N2; le contrôle 7 ne s’applique que lorsqu’une injection est prévue (EXIG-IAM-19). Au retour, le filtre masque la sortie; il n’annule pas un effet déjà produit. Source : CRE-IA-2026-01.</figcaption>',
     ['4.11', '4.14', '4.61', 'A-19']),
    # [4.10] contrôle 1 : liaison du jeton
    ('<li><strong>Authentifier</strong> l’agent (SVID, mTLS) et le mandant (jeton délégué) : section 9.2 et section 9.3.</li>',
     '<li><strong>Authentifier</strong> l’agent (SVID, mTLS) et le mandant (jeton délégué), et vérifier la liaison du jeton (<code>cnf</code>) : section 9.2 et section 9.3.</li>',
     ['4.10']),
    # [4.61, A-10, A-14] contrôle 5 : contrôle calculé; écriture N2
    ('<li><strong>Vérifier le jeton d’approbation</strong> lorsque la classe de l’agent et le palier l’exigent (P3; P2 au-delà du seuil, ou à chaque action pour un agent de niveau N2) : section 8.5.</li>',
     '<li><strong>Vérifier le jeton d’approbation</strong> lorsque le contrôle calculé selon l’EXIG-AUT-10 l’exige (P3; P2 au-delà du seuil; toute écriture d’un agent de niveau N2) : section 8.5. La passerelle conserve le jeton, qui couvre une opération (EXIG-AUT-12).</li>',
     ['4.61', 'A-10', 'A-14']),
    # [4.62] contrôle 6 : ordre justifié
    ('<li><strong>Limiter</strong> le débit, les quotas et le budget de la tâche : section 10.6.</li>',
     '<li><strong>Limiter</strong> le débit, les quotas et le budget de la tâche : section 10.6. La limitation de débit par appelant s’applique dès l’authentification, avant les garde-fous coûteux; le budget se vérifie avant le relais.</li>',
     ['4.62']),
    # [4.11, A-16] contrôle 7 : conditionnel
    ('<li><strong>Injecter les justificatifs</strong> en aval, hors de l’agent (modèle sans clés, ci-dessous).</li>',
     '<li><strong>Injecter les justificatifs</strong> en aval, hors de l’agent, lorsque l’injection est prévue (EXIG-IAM-19, EXIG-SEC-14), et obtenir le jeton destiné au serveur (EXIG-IAM-14) : modèle sans clés, ci-dessous.</li>',
     ['4.11', 'A-16']),
    # [4.14, A-19] contrôle 9 : intention avant l’effet
    ('<li><strong>Tracer et journaliser</strong> : span OpenTelemetry et enregistrement d’audit : section 10.1 et section 10.3.</li>',
     '<li><strong>Tracer et journaliser</strong> : span OpenTelemetry et enregistrement d’audit : section 10.1 et section 10.3. Pour un appel P2 ou P3, l’enregistrement d’intention est écrit avant le relais, et l’enregistrement d’issue au retour (EXIG-OBS-11).</li>',
     ['4.14', 'A-19']),
    # [4.60, 3.28, A-01] IAM-17 : portée unique de la passerelle
    ('<p>Dans tout environnement serveur, tout appel d’un agent vers un serveur MCP, vers un autre agent ou vers une ressource qui franchit une frontière de domaine <strong>DOIT</strong> passer par la passerelle d’agents (EXIG-ARC-01, EXIG-MCP-01), qui applique au minimum les neuf contrôles de la figure 18. Un outil, un serveur MCP ou un agent absent du catalogue, ou dont la version ou l’empreinte diffère de celle qui est épinglée, est bloqué. À l’intérieur d’un domaine, la décision par appel (EXIG-IAM-02) est appliquée par le serveur de ressources et par l’authentification mutuelle du maillage de services.</p>',
     '<p>Dans tout environnement autre qu’un poste de développement individuel sans justificatif de production, tout appel d’un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, tout accès à une ressource d’un autre domaine et toute action de palier P2 ou P3 <strong>DOIVENT</strong> passer par la passerelle d’agents (EXIG-ARC-01, EXIG-MCP-01), qui applique au minimum les neuf contrôles de la figure 18, chacun lorsqu’il s’applique. Une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Un outil, un serveur MCP ou un agent absent du catalogue, ou dont la version ou l’empreinte diffère de celle qui est épinglée, est bloqué. Seule une fonction locale de palier P0 ou P1, exécutée dans l’unité de déploiement de l’agent, sur les données de son propre domaine et inscrite au catalogue avec son palier, peut s’en dispenser : la décision par appel (EXIG-IAM-02) y est appliquée par le serveur de ressources et par l’authentification mutuelle du maillage de services. Une instance de la passerelle peut être déployée au plus près de l’agent <em>(sidecar)</em>, à condition de partager la politique, le registre des <code>jti</code> et le journal d’audit des autres instances.</p>',
     ['4.60', '3.28', '4.11', 'A-01']),
    # [4.12, 4.63, 3.29, A-04, A-06] IAM-18 : cache borné; refus typé par familles; compensations
    ('<p>La passerelle <strong>DOIT</strong> refuser tout appel pour lequel elle ne peut pas obtenir ou évaluer une décision de politique valide; elle n’ouvre jamais le passage par défaut. Si le plan de contrôle est indisponible, elle continue d’appliquer la dernière politique distribuée. Tout refus renvoie à l’agent un code d’erreur typé (p. ex. portée insuffisante, approbation requise, budget épuisé, agent suspendu) et produit un événement d’audit.</p>',
     '<p>La passerelle <strong>DOIT</strong> refuser tout appel pour lequel elle ne peut pas obtenir ou évaluer une décision de politique valide; elle n’ouvre jamais le passage par défaut. Si le plan de contrôle est indisponible, elle continue d’appliquer la dernière politique distribuée, tant que celle-ci n’est pas échue (EXIG-IAM-22); le mode dégradé et la version de politique appliquée sont journalisés. Tout refus renvoie à l’agent un code d’erreur typé, choisi parmi quelques familles utiles à l’escalade (p. ex. portée insuffisante, approbation requise, budget épuisé, agent suspendu), et produit un événement d’audit qui en porte le détail; une rafale de refus est un signal de risque (EXIG-IAM-02). Le refus en mode fermé vise les appels vers l’avant : les compensations déclarées passent par le canal de compensation (EXIG-ORC-31).</p>',
     ['4.12', '4.63', '3.29', 'A-04', 'A-06']),
    # [4.64, A-04] sept portes : grille informative; porte 3 bornée
    ('Le cadre retient ces sept portes comme critères d’acceptation d’une passerelle d’agents (choix du cadre).</p>',
     'Le cadre retient ces sept portes comme grille informative d’évaluation d’une passerelle d’agents, et non comme critères normatifs : les critères d’acceptation sont les exigences du présent chapitre. La troisième porte ne vaut que dans la limite de l’EXIG-IAM-22 : une politique distribuée ne s’applique que pendant sa durée de validité.</p>',
     ['4.64', 'A-04']),
    # [4.11] IAM-19 : la force affichée est celle du cas obligatoire
    ('<p><strong><code>EXIG-IAM-19</code> · DEVRAIT</strong></p>',
     '<p><strong><code>EXIG-IAM-19</code> · DOIT</strong></p>',
     ['4.11']),
    ('<p>Les justificatifs nécessaires pour appeler un système en aval <strong>DEVRAIENT</strong> être injectés par la passerelle ou par un mandataire de sortie après la décision de politique (et <strong>DOIVENT</strong> l’être lorsqu’un code s’exécute en bac à sable selon l’EXIG-SEC-14 ou lorsqu’un secret résiduel de système patrimonial est employé sous dérogation selon l’EXIG-IAM-05), de sorte que le modèle n’y ait jamais accès (EXIG-IAM-06).',
     '<p>Les justificatifs nécessaires pour appeler un système en aval <strong>DOIVENT</strong> être injectés par la passerelle ou par un mandataire de sortie, après la décision de politique, lorsqu’un code s’exécute en bac à sable (EXIG-SEC-14) ou lorsqu’un secret résiduel de système patrimonial est employé sous dérogation (EXIG-IAM-05); dans les autres cas, ils <strong>DEVRAIENT</strong> l’être. Dans tous les cas, le modèle n’y a jamais accès (EXIG-IAM-06).',
     ['4.11']),
    # [4.65] phrase sans verbe principal
    ('Pour propager une révocation au-delà de la passerelle, les spécifications finales OpenID Shared Signals Framework 1.0,',
     'Pour propager une révocation au-delà de la passerelle, le cadre s’appuie sur les spécifications finales OpenID Shared Signals Framework 1.0,',
     ['4.65']),
    # [4.15, 4.16, 4.99 a-b, 3.54, A-04, A-05, A-06] IAM-20 : source unique du coupe-circuit
    ('<p>La plateforme <strong>DOIT</strong> offrir un coupe-circuit qui, en une seule action, suspend un agent, un outil, un serveur MCP ou une catégorie d’actions sur toutes les passerelles, désactive l’identité de l’agent auprès du fournisseur d’identité et diffuse la révocation, au moyen du Shared Signals Framework et de CAEP, aux systèmes raccordés qui les prennent en charge. Le délai maximal de bout en bout est fixé par l’entreprise et mesuré lors d’un exercice au moins trimestriel (section 7.8).</p>',
     '<p>La plateforme <strong>DOIT</strong> offrir un coupe-circuit qui, en une seule action, suspend un agent, un outil, un serveur MCP ou une catégorie d’actions sur toutes les instances de la passerelle, par le canal de suspension de l’EXIG-IAM-22, désactive l’identité de l’agent auprès du fournisseur d’identité et diffuse la révocation, au moyen du Shared Signals Framework et de CAEP, aux systèmes raccordés qui les prennent en charge. Le coupe-circuit arrête l’agent vers l’avant : il refuse tout nouvel appel sous son identité. Il ne vise pas le canal de compensation (EXIG-ORC-31), sauf décision distincte. Les systèmes raccordés sans SSF ni CAEP sont inscrits au catalogue, et la durée de vie des jetons qui leur sont destinés est bornée selon l’EXIG-IAM-15. Le délai mesuré va de la décision d’arrêt au refus du dernier appel dans tous les systèmes, durée de vie résiduelle des jetons émis comprise (tableau 61). La cible est fixée par l’entreprise, proposée à 15 minutes; elle est mesurée à l’exercice trimestriel de l’EXIG-SEC-26, seul exercice du coupe-circuit.</p>',
     ['4.15', '4.16', '4.99', '3.54', 'A-04', 'A-05', 'A-06']),
    ('le cadre exige donc un délai mesuré plutôt qu’une promesse.</p>',
     'le cadre exige donc un délai mesuré plutôt qu’une promesse. Un jeton autoporteur reste accepté jusqu’à son expiration par un système qui ne reçoit ni SSF ni CAEP, d’où la borne de l’EXIG-IAM-15; arrêter l’agent ne doit pas empêcher de compenser ce qu’il a commencé (EXIG-ORC-31).</p>',
     ['4.15', '4.16']),
    # [4.99 c] encadré sur la latence : latence des garde-fous
    ('Seule compte la latence ajoutée (P50 et P99) mesurée dans les conditions de l’entreprise, politiques et traçage activés; la section 13.2 en fait un critère d’évaluation des fournisseurs.</p>\n</div>\n<h3>9.5 Menaces propres aux agents</h3>',
     'Seule compte la latence ajoutée (P50 et P99) mesurée dans les conditions de l’entreprise, politiques, garde-fous d’entrée et de sortie (contrôles 4 et 8) et traçage activés; la section 13.2 en fait un critère d’évaluation des fournisseurs.</p>\n</div>\n'
     # [4.12, 4.13, A-04] nouvelle exigence EXIG-IAM-22
     '<h4>Disponibilité et mode dégradé</h4>\n'
     '<div id="exig-iam-22">\n'
     '<p><strong><code>EXIG-IAM-22</code> · DOIT</strong></p>\n'
     '<p><strong>Disponibilité et validité de la politique en cache</strong></p>\n'
     '<p>La passerelle d’agents, le registre, le catalogue, le service de politiques, le service d’approbation, le registre des <code>jti</code> et le service d’audit <strong>DOIVENT</strong> avoir un objectif de disponibilité fixé par l’entreprise, inscrit au catalogue et mesuré, ainsi qu’une redondance qui le tient (instances redondantes par zone pour la passerelle). Les politiques se déploient progressivement, avec retour arrière automatique. Chaque politique distribuée porte une durée de validité inscrite au catalogue : tant qu’elle n’est pas échue, elle vaut service disponible au sens de l’EXIG-AUT-11; échue, la passerelle ne laisse passer que les appels P0. Un état dynamique illisible (marquage de la session, compteurs, budget, registre des <code>jti</code>, état de la fiche) impose le refus de l’appel qui en dépend. La liste de suspension (agents, outils, versions) <strong>DOIT</strong> être poussée par un canal signé indépendant du plan de contrôle et appliquée même quand celui-ci est indisponible. La panne d’une instance de la passerelle est jouée à l’exercice de l’EXIG-SEC-26.</p>\n'
     '<div id="pourquoi-iam-22"><p>Pourquoi : un passage obligé qui échoue fermé est un point unique de défaillance pour toute l’activité agentique; une politique en cache sans âge maximal fige le coupe-circuit et le retrait d’outil pendant une panne du plan de contrôle, et donne deux issues au même appel P3 selon qu’on tient le cache pour disponible ou non. Les objectifs et les durées sont fixés par l’entreprise (choix du cadre).</p></div>\n'
     '</div>\n'
     '<h3>9.5 Menaces propres aux agents</h3>',
     ['4.99', '4.12', '4.13', 'A-04']),
    # ---------------------------------------------------------------- § 9.5
    # [4.71] correspondance NHI vers ASI non vérifiée : retirée
    ('De même, les risques d’identités non humaines se répartissent entre plusieurs risques ASI plutôt que de se rattacher à ASI03 seul : NHI1 (retrait inadéquat) relève d’ASI04, NHI2 (fuite de secrets) d’ASI02 et d’ASI06, et NHI4 (authentification non sécurisée) d’ASI03 et d’ASI07<strong><sup>[28,</sup> 349]</strong>.</p>',
     'Le cadre n’établit pas, en revanche, de correspondance propre entre le Top 10 des identités non humaines et les risques ASI : ces risques sont traités par les exigences de la section 9.2 (tableau 34).</p>',
     ['4.71']),
    # [4.99 f, A-24] SEC-01 et SEC-02 : déclencheurs renvoyés à GOV-12
    ('La modélisation <strong>DOIT</strong> être révisée à chaque changement de modèle, d’outil, de palier d’outil ou de niveau d’autonomie.',
     'La modélisation <strong>DOIT</strong> être révisée avant la mise en service de tout changement visé par l’EXIG-GOV-12, qui tient la liste unique des déclencheurs de réévaluation.',
     ['4.99', 'A-24']),
    ('La matrice <strong>DOIT</strong> être mise à jour à chaque nouvelle version du Top 10 agentique ou d’ATLAS.</p>',
     'La matrice <strong>DOIT</strong> être mise à jour à chaque nouvelle version du Top 10 agentique ou des menaces T1 à T17, à chaque révision du cadre et, pour MITRE ATLAS, dont les versions se succèdent rapidement, au moins tous les six mois (EXIG-GOV-12).</p>',
     ['4.99', 'A-24']),
    # [4.66] tableau 38 : renvois précisés
    ('(EXIG-IAM-08 à EXIG-IAM-12, section 9.3)',
     '(EXIG-IAM-08 à EXIG-IAM-16, section 9.3)',
     ['4.66']),
    ('<td>Surveillance, plafonds et coupe-circuit (section 9.4); EXIG-SEC-26; journal d’audit signé (section 10.3).</td>',
     '<td>Plafonds et disjoncteurs (EXIG-ORC-26, section 7.8); coupe-circuit (EXIG-IAM-20) et son exercice (EXIG-SEC-26); évaluation continue (section 10.4); journal d’audit signé (section 10.3).</td>',
     ['4.66']),
    # ---------------------------------------------------------------- § 9.6
    # [4.01, 4.19, 4.72, A-17] SEC-03 : toute source étiquetée; frontière du mandant
    ('<p>Tout contenu qui ne provient ni du mandant authentifié ni de la configuration approuvée de l’agent <strong>DOIT</strong> être traité comme non fiable : pages web, courriels, documents téléversés (y compris par le mandant), champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, messages et cartes d’autres agents. Le catalogue d’entreprise <strong>DOIT</strong> marquer chaque outil dont la sortie peut contenir du contenu de tiers, afin que la passerelle d’agents sache, sans se fier au modèle, qu’une session a consommé un tel contenu.</p>',
     '<p>Toute source de contexte (outil, mémoire, index de récupération, déclencheur, téléversement, message ou tâche A2A entrant, événement) <strong>DOIT</strong> être inscrite au catalogue avec son étiquette de fiabilité; une source non inscrite est non fiable. Seules la demande saisie par le mandant authentifié pour sa tâche et la configuration approuvée de l’agent sont fiables. Tout autre contenu <strong>DOIT</strong> être traité comme non fiable, quel que soit son canal, même s’il vient du mandant : pages web, courriels, pièces jointes et documents (téléversés, collés ou cités), champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, messages et tâches d’autres agents, ainsi que les cartes d’agents et les définitions d’outils, hors des champs revus et épinglés au catalogue (EXIG-SEC-18). Faute de pouvoir distinguer un texte de tiers collé dans la demande, la fiche d’un agent qui réunit [B] et [C] déclare comment ses saisies libres sont étiquetées; à défaut, elles sont non fiables. Tout canal d’entrée de contexte passe par la passerelle ou lui signale son étiquette, afin que la passerelle sache, sans se fier au modèle, qu’une session a consommé un tel contenu.</p>',
     ['4.01', '4.19', '4.72', 'A-17']),
    # [4.69] légende de la figure 19 (figure non modifiable)
    ('Source : cadre CRE-IA-2026-01, d’après Willison (2025), Meta (2025) et Beurer-Kellner et al. (2025).</figcaption>',
     'Le schéma abrège deux points que l’EXIG-SEC-04 précise : la « supervision humaine » y est l’approbation de l’action exacte, et [B] y vise les données et les systèmes sensibles, en lecture comme en écriture. Source : cadre CRE-IA-2026-01, d’après Willison (2025), Meta (2025) et Beurer-Kellner et al. (2025).</figcaption>',
     ['4.69']),
    # [4.67, 4.01] exemple : retrait de l’exécution autonome; délégation à un autre agent
    ('Avec les règles ci-dessous, la passerelle retire l’outil d’envoi dès la lecture du courriel : l’agent prépare sa réponse en brouillon, et l’envoi n’a lieu qu’après une approbation humaine qui montre le destinataire et le contenu exacts.</p>',
     'Avec les règles ci-dessous, la passerelle retire l’outil d’envoi de l’exécution autonome dès la lecture du courriel : l’agent prépare sa réponse, et l’envoi n’a lieu qu’après une approbation humaine qui montre le destinataire et le contenu exacts. Le même retrait vaut si l’agent confie l’envoi à un autre agent : le message qu’il lui transmet porte l’étiquette de contamination (EXIG-SEC-04).</p>',
     ['4.67', '4.01']),
    # [4.01, 4.17, 4.18, 4.21, A-17] SEC-04 : session composée, [B] élargi, contexte vierge, charge d’approbation
    ('<p>La fiche de chaque agent <strong>DOIT</strong> déclarer lesquelles des trois propriétés il réunit dans une même session : [A] il traite du contenu non fiable; [B] il accède à des données sensibles ou à des outils P1; [C] il modifie un état ou communique vers l’extérieur (outils P2, P3 ou envoi externe). Un agent qui réunit les trois <strong>NE DOIT PAS</strong> exécuter d’action [C] sans approbation humaine liée à l’action exacte (section 8.5), sauf s’il repart d’un contexte vierge exempt du contenu non fiable.</p>\n'
     '<div id="pourquoi-865"><p>Pourquoi : c’est la réunion des trois propriétés qui rend l’exfiltration possible; en retirer une seule suffit à rompre la chaîne<strong><sup>[307, 354]</sup></strong>.</p></div>',
     '<p>La fiche de chaque agent <strong>DOIT</strong> déclarer lesquelles des trois propriétés il réunit dans une même session : [A] il traite du contenu non fiable; [B] il accède, en lecture ou en écriture, à des données ou à des systèmes sensibles (outils P1 portant sur de telles données, ou P2 sur un système sensible); [C] il modifie un état ou communique vers l’extérieur (outils P2, P3 ou envoi externe, y compris vers un autre agent). La règle de deux s’évalue sur la session composée : la session est la tâche racine et tout ce qui en dérive (sous-tâches, délégations A2A, reprises depuis un point de contrôle, événements publiés au titre de la tâche), et son état (contenu non fiable consommé, données sensibles consultées) est tenu par la passerelle dans un magasin à cohérence forte; un état illisible impose le refus. Toute donnée produite par une session marquée (artefact, entrée de mémoire, message ou tâche A2A, événement) porte l’étiquette, et la consommer marque la session du consommateur; une donnée sensible reçue d’un pair confère [B]. La fiche déclare les propriétés; la passerelle applique la règle à l’exécution. Une session qui réunit les trois <strong>NE DOIT PAS</strong> exécuter d’action [C] sans approbation humaine liée à l’action exacte (section 8.5), sauf si l’agent repart d’un contexte vierge. Un contexte vierge exclut tout rechargement de mémoire, de point de contrôle ou d’artefact étiqueté postérieur à la contamination, et ne reçoit du contexte contaminé que des sorties contraintes (énumération, champs validés par schéma, références symboliques : tableau 39); toute autre sortie hérite de l’étiquette. Après une lecture non fiable, les écritures P2 restent soumises aux seuils de volume de l’EXIG-AUT-10, avec un plafond par session inscrit à la fiche. La fiche <strong>DOIT</strong> estimer le volume d’approbations qu’entraîne la règle et nommer la capacité qui l’absorbe (EXIG-AUT-20); au-delà, l’agent est reconçu selon un patron du tableau 39.</p>\n'
     '<div id="pourquoi-865"><p>Pourquoi : c’est la réunion des trois propriétés, dans le flux d’information d’une session et non chez un agent isolé, qui rend l’exfiltration possible; en retirer une seule suffit à rompre la chaîne pour la session composée<strong><sup>[307, 354]</sup></strong>. Le suivi des étiquettes le long du flux applique le principe du contrôle de flux d’information (choix du cadre).</p></div>',
     ['4.01', '4.17', '4.18', '4.21', 'A-17']),
    # [4.68] SEC-05 : critère d’acceptation
    ('et le résultat consigné à la fiche de l’agent.</p>',
     'et le résultat consigné à la fiche de l’agent et comparé au seuil de l’EXIG-SEC-24.</p>',
     ['4.68']),
    # [4.67, 4.01] « Retirer » : étiquettes des sources; retrait de l’exécution autonome
    ('La passerelle sait, grâce au marquage du catalogue, qu’une session vient de consommer du contenu non fiable; elle restreint alors les outils offerts à l’agent pour le reste de la session. Le modèle n’a rien à décider : l’outil d’envoi n’est tout simplement plus disponible.</p>',
     'La passerelle sait, grâce à l’étiquette de chaque source de contexte (EXIG-SEC-03), qu’une session vient de consommer du contenu non fiable; elle retire alors de l’exécution autonome, pour le reste de la session, les outils qui permettent d’exfiltrer. Le modèle n’a rien à décider : l’outil d’envoi ne s’exécute plus sans une approbation humaine de l’action exacte.</p>',
     ['4.67', '4.01']),
    # [4.01, 4.20, 4.67, A-17] SEC-06 : outil d’envoi défini; canaux fermés; liste toujours appliquée
    ('<p>Dès qu’une session a consommé du contenu non fiable, la passerelle d’agents <strong>DOIT</strong> retirer à l’agent, pour le reste de la session, les outils d’envoi vers l’extérieur et les outils P3, et refuser toute requête sortante vers une destination absente de la liste d’autorisation. Une action ainsi retirée ne s’exécute qu’avec une approbation humaine liée à l’action exacte. Le retrait est appliqué par la passerelle à partir du marquage du catalogue, jamais par une consigne donnée au modèle.</p>',
     '<p>Dès qu’une session (EXIG-SEC-04) a consommé du contenu non fiable, la passerelle d’agents <strong>DOIT</strong> retirer de l’exécution autonome, pour le reste de la session, les outils d’envoi et les outils P3 : chaque appel de ces outils exige alors une approbation humaine liée à l’action exacte. Est un outil d’envoi tout outil dont un argument peut atteindre une destination hors de la frontière de confiance de la session, autres agents compris, y compris la requête en texte libre d’un outil de recherche publique P0 ou d’un outil de lecture d’URL. Après contamination, les arguments libres des outils de lecture sont contraints (valeurs énumérées, absence de RP détectés), et les écritures P2 vers des champs visibles de tiers sont soumises à approbation. La passerelle <strong>DOIT</strong> refuser en tout temps toute requête sortante vers une destination absente de la liste d’autorisation. Le retrait est appliqué par la passerelle à partir des étiquettes des sources (EXIG-SEC-03), jamais par une consigne donnée au modèle.</p>',
     ['4.01', '4.20', '4.67', 'A-17']),
    # [4.22] tableau 39 : plan puis exécution ne fige pas les arguments
    ('ce contenu ne peut plus ajouter d’action.</td>',
     'ce contenu ne peut plus ajouter d’action, mais il peut encore influencer les arguments des actions prévues.</td>',
     ['4.22']),
    # [4.70] CaMeL : version citée, portée de la mesure et de la garantie
    ('contre 84 % pour un système non défendu<strong><sup>[101]</sup></strong>. Le coût en utilité est réel, mais quantifié (7 points de pourcentage sur AgentDojo) : c’est le prix d’une garantie plutôt que d’une probabilité.</p>',
     'contre 84 % pour un système non défendu, selon la version v2 de l’article<strong><sup>[101]</sup></strong>. Le coût en utilité est réel, mais il n’est mesuré que sur ce banc d’essai (7 points de pourcentage) : c’est le prix d’une garantie plutôt que d’une probabilité, garantie bornée aux flux de contrôle et de données, hors canaux auxiliaires.</p>',
     ['4.70']),
    # [4.22] SEC-07 : confinement des arguments pour la classe élevée
    ('autre que la minimisation du contexte, consigné à la fiche de l’agent (annexe B) et vérifié en revue de conception. Un agent de risque modéré dans la même situation <strong>DEVRAIT</strong> en appliquer un.</p>\n'
     '<div id="pourquoi-879"><p>Pourquoi : ces patrons empêchent par construction le contenu non fiable de choisir les actions, ce qu’aucun filtre ne garantit<strong><sup>[357]</sup></strong>.</p></div>',
     'autre que la minimisation du contexte, consigné à la fiche de l’agent (annexe B) et vérifié en revue de conception. Le patron retenu <strong>DOIT</strong> aussi confiner les données (sélecteur d’actions, map-reduce à sortie contrainte, double modèle, code puis exécution avec suivi des flux); à défaut, les arguments sensibles issus de contenu non fiable (bénéficiaire, compte, destinataire) <strong>DOIVENT</strong> être validés contre une source de référence. Un agent de risque modéré dans la même situation <strong>DEVRAIT</strong> en appliquer un.</p>\n'
     '<div id="pourquoi-879"><p>Pourquoi : ces patrons empêchent par construction le contenu non fiable de choisir les actions, ce qu’aucun filtre ne garantit; seuls certains confinent aussi les arguments, que leurs auteurs décrivent comme encore influençables sous le patron plan puis exécution<strong><sup>[357]</sup></strong>.</p></div>',
     ['4.22']),
    # [A-11] « Approuver » : empreinte de l’action exacte, jeton conservé
    ('un jeton signé, lié à l’empreinte de l’outil et de ses arguments, que la passerelle vérifie avant l’exécution (section 8.5).',
     'un jeton signé, lié à l’empreinte de l’action exacte (outil, définition, appelant et arguments), que la passerelle conserve et vérifie avant l’exécution (section 8.5).',
     ['A-11', 'A-10']),
    # ---------------------------------------------------------------- § 9.7
    # [4.23] noyau partagé : conteneur interdit, microVM par défaut
    ('Le cadre va plus loin, par choix : il interdit le noyau partagé pour tout code non fiable, parce qu’un agent',
     'Le cadre va plus loin, par choix : il interdit le conteneur à noyau partagé pour tout code non fiable et retient par défaut un noyau invité dédié (microVM), parce qu’un agent',
     ['4.23']),
    ('<p>Tout code généré par un agent, ou reçu d’une source non fiable, <strong>DOIT</strong> s’exécuter dans une microVM (Firecracker, Kata Containers), sous gVisor ou, s’il est compilé en WebAssembly, dans un environnement WASI sans autorité ambiante. Il <strong>NE DOIT PAS</strong> s’exécuter dans un conteneur à noyau partagé, dans le processus de l’agent ni sur l’hôte de la passerelle.</p>\n'
     '<div id="pourquoi-891"><p>Pourquoi : la frontière doit résister à une faille du noyau, puisque l’attaquant choisit le code exécuté; ce choix du cadre est plus strict que la recommandation de l’OWASP.</p></div>',
     '<p>Tout code généré par un agent, ou reçu d’une source non fiable, <strong>DOIT</strong> s’exécuter dans une microVM (Firecracker, Kata Containers), option par défaut, ou, sur justification consignée à la fiche, sous gVisor ou, s’il est compilé en WebAssembly, dans un environnement WASI sans autorité ambiante, l’environnement d’exécution Wasm tournant alors dans un processus distinct de l’agent, lui-même confiné. Il <strong>NE DOIT PAS</strong> s’exécuter dans un conteneur à noyau partagé, dans le processus de l’agent ni sur l’hôte de la passerelle.</p>\n'
     '<div id="pourquoi-891"><p>Pourquoi : l’attaquant choisit le code exécuté; seule la microVM interpose un noyau invité qui résiste à une faille du noyau de l’hôte, gVisor et WASI en réduisant la surface. Ce choix du cadre est plus strict que la recommandation de l’OWASP.</p></div>',
     ['4.23']),
    # [4.73] SEC-09 : réutilisation, instantanés, gel des preuves
    ('<p>Chaque bac à sable <strong>DOIT</strong> être créé pour une seule tâche ou une seule session, puis détruit, sans jamais être réutilisé pour un autre mandant;',
     '<p>Chaque bac à sable <strong>DOIT</strong> être créé pour une seule tâche ou une seule session, puis détruit à sa fin, sauf gel des preuves (EXIG-CON-23), sans jamais être réutilisé; un bac à sable restauré depuis un instantané régénère son entropie et ses identifiants;',
     ['4.73', 'A-18']),
    # [4.79] SEC-10 : délai de correctif, GPU en passage direct, garantie affaiblie
    ('<p>Un bac à sable qui exige un GPU <strong>DOIT</strong> faire l’objet d’une analyse de risque propre, approuvée par la sécurité, et l’hôte <strong>DOIT</strong> maintenir ses pilotes à jour.',
     '<p>Un bac à sable qui exige un GPU <strong>DOIT</strong> faire l’objet d’une analyse de risque propre, approuvée par la sécurité, qui accepte nommément l’affaiblissement de la garantie de l’EXIG-SEC-08, et l’hôte <strong>DOIT</strong> appliquer les correctifs de sécurité de ses pilotes dans le délai de la politique de correctifs de l’entreprise. En passage direct d’un GPU à une microVM, l’analyse vérifie l’isolement par l’IOMMU et la remise à zéro de la mémoire du GPU entre deux bacs à sable.',
     ['4.79']),
    # [4.24, 4.74, A-33] SEC-12 : règle de sortie réseau unique
    ('<p>Un bac à sable <strong>DOIT</strong> démarrer sans aucun accès réseau sortant, résolution DNS comprise. Chaque destination nécessaire <strong>DOIT</strong> être inscrite nommément à une liste d’autorisation tenue à la fiche de l’agent, sans règle générique; le trafic <strong>DOIT</strong> passer par un mandataire de sortie qui refuse le HTTP en clair et qui termine TLS pour les domaines où il injecte une authentification (EXIG-SEC-14). Les plages privées et lien-local, dont 169.254.0.0/16 et leurs équivalents IPv6 (<code>fc00::/7</code>, <code>fe80::/10</code>), <strong>DOIVENT</strong> être bloquées, à l’exception de l’adresse du mandataire de sortie.</p>',
     '<p>Un bac à sable <strong>DOIT</strong> refuser par défaut tout accès réseau sortant, résolution DNS comprise. Chaque destination nécessaire <strong>DOIT</strong> être inscrite nommément à une liste d’autorisation tenue à la fiche de l’agent, sans règle générique; cette liste est la même que celle de l’EXIG-SEC-06. Le trafic <strong>DOIT</strong> passer par un mandataire de sortie qui refuse le HTTP en clair et qui termine TLS pour toute destination ou, à défaut, vérifie la concordance du SNI, de l’en-tête <code>Host</code> et du certificat, ce qui refuse le <em>domain fronting</em>; pour un service multilocataire, la liste restreint aussi la méthode, le préfixe d’URL ou l’identifiant de locataire. Toute connexion sortante initiée à partir d’une donnée externe (URL, <code>jku</code>, icône, notification push, redirection), du bac à sable comme d’un client MCP ou A2A (EXIG-MCP-12, EXIG-MCP-19, EXIG-A2A-12), <strong>DOIT</strong> viser une destination de la liste, être résolue une fois puis connectée à l’adresse résolue, vérifiée avant la connexion hors des plages des registres IANA d’adresses à usage spécial (IPv4 et IPv6, dont <code>127.0.0.0/8</code>, <code>10.0.0.0/8</code>, <code>100.64.0.0/10</code>, <code>169.254.0.0/16</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>, <code>::1</code>, <code>fc00::/7</code>, <code>fe80::/10</code>, <code>::ffff:0:0/96</code> et <code>64:ff9b::/96</code>), après normalisation; chaque redirection est revalidée selon la même règle, avec un plafond de redirections. Seule l’adresse du mandataire de sortie échappe à ce blocage. Une cible interne légitime est atteinte par une entrée de catalogue, jamais par une URL fournie.</p>',
     ['4.24', '4.74', 'A-33']),
    ('<div id="pourquoi-899"><p>Pourquoi : une sortie fermée par défaut limite l’exfiltration de données même lorsque le code exécuté n’est pas fiable<strong><sup>[208, 342]</sup></strong>.</p></div>',
     '<div id="pourquoi-899"><p>Pourquoi : une sortie fermée par défaut limite l’exfiltration de données même lorsque le code exécuté n’est pas fiable<strong><sup>[208, 342]</sup></strong>; une adresse vérifiée puis connectée telle quelle écarte la réassociation DNS, et la RFC 8725 (§ 3.10) met en garde contre le suivi aveugle de <code>jku</code>. Le cadre réunit ici la règle de sortie que d’autres exigences appliquent (choix du cadre).</p></div>',
     ['A-33']),
    # [4.75] SEC-13 : limite de sauts exigée, non présumée
    ('<strong>DOIT</strong> en outre être configuré pour n’accepter qu’IMDSv2.</p>',
     '<strong>DOIT</strong> en outre être configuré pour n’accepter qu’IMDSv2, avec une limite de sauts de la réponse <code>PUT</code> égale à 1 sur les hôtes de bacs à sable.</p>',
     ['4.75']),
    ('est présent et limite par défaut les sauts IP à un, ce qui protège contre',
     'est présent et permet de limiter à un les sauts IP de sa réponse, que l’exigence impose au lieu de s’en remettre à une valeur par défaut; ces mesures protègent contre',
     ['4.75']),
    # [4.25, 4.76, A-33] SEC-14 : jeton éphémère borné; protocoles autres que HTTP
    ('le mandataire de sortie, situé hors du bac à sable, <strong>DOIT</strong> ajouter l’authentification après vérification de la destination; lorsque le code appelle des outils,',
     'le mandataire de sortie, situé hors du bac à sable, <strong>DOIT</strong> ajouter un jeton éphémère obtenu par échange de jetons (audience unique, portée minimale, durée au plus égale à la vie du bac à sable) après vérification de la destination, de la méthode et du chemin; tout appel qui produit un effet P2 ou P3 passe par la passerelle et ses paliers. Pour un protocole que le mandataire ne peut pas courtier, un mandataire de protocole inscrit au catalogue tient ce rôle; à défaut, un identifiant éphémère de portée minimale, émis pour ce seul bac à sable et révoqué à sa destruction, est admis sur dérogation (section 11.6). Lorsque le code appelle des outils,',
     ['4.25', '4.76']),
    ('<div id="pourquoi-903"><p>Pourquoi : le code compromis ne peut ni lire ni réutiliser un justificatif qu’il ne détient pas<strong><sup>[93, 342]</sup></strong>.</p></div>',
     '<div id="pourquoi-903"><p>Pourquoi : le code compromis ne peut ni lire ni exfiltrer un justificatif qu’il ne détient pas<strong><sup>[93, 342]</sup></strong>; comme il peut encore s’en servir par le mandataire, cet usage reste borné par la portée, la méthode et le chemin autorisés.</p></div>',
     ['4.25']),
    # [4.78] SEC-15 : boucle de tâche, attente d’approbation, borne la plus courte
    ('par boucle de tâche (20 minutes par défaut) et pour sa durée de vie totale (destruction dès la fin de la tâche et, au plus tard, après 60 minutes par défaut). Ces valeurs sont des choix du cadre; toute valeur supérieure <strong>DOIT</strong> être justifiée à la fiche de l’agent.</p>',
     'par boucle de tâche, soit le temps d’exécution actif de la tâche dans le bac à sable (20 minutes par défaut), et pour sa durée de vie totale (destruction dès la fin de la tâche et, au plus tard, après 60 minutes par défaut). Ces valeurs sont des choix du cadre; toute valeur supérieure <strong>DOIT</strong> être justifiée à la fiche de l’agent. Une attente d’approbation suspend l’exécution, qui reprend par exécution durable dans un nouveau bac à sable. Lorsque la fiche, l’EXIG-ORC-26 et la présente exigence fixent des bornes différentes, la plus courte s’applique.</p>',
     ['4.78']),
    # [4.26] SEC-16 : ce qui s’observe de l’extérieur, agent d’invité, minimisation
    ('<p>Chaque commande exécutée, chaque écriture de fichier et chaque requête réseau d’un bac à sable <strong>DOIVENT</strong> être consignées par un composant situé hors du bac à sable, dans un journal inaltérable rattaché à la trace de la tâche (section 10.3).</p>',
     '<p>Chaque requête réseau d’un bac à sable <strong>DOIT</strong> être consignée par le mandataire de sortie, hors du bac à sable, dans un journal inaltérable rattaché à la trace de la tâche (section 10.3). Les commandes exécutées et les écritures de fichiers <strong>DOIVENT</strong> être consignées par un composant hors du bac à sable lorsque la technologie le permet (appels système sous gVisor, différence du disque à la destruction); sinon, par un agent placé dans l’invité, sur une racine en lecture seule, qui transmet chaque événement sans délai hors du bac à sable. Le journal est minimisé (aucun secret, RP caviardés) et conservé selon l’EXIG-CON-10.</p>',
     ['4.26']),
    # [4.27, 4.77] SEC-17 : aucune approbation à l’exécution hors fiche; porte d’appoint
    ('<p>Le code généré <strong>DOIT</strong> franchir une porte de validation avant exécution : analyse statique, refus des constructions d’évaluation dynamique (<code>eval</code> et équivalents) dans les agents en production, et approbation humaine pour toute exécution qui demande des privilèges ou des destinations réseau supplémentaires. Pendant l’exécution, une surveillance <strong>DOIT</strong> détecter les comportements anormaux (processus inattendus, connexions refusées, volumes d’écriture inhabituels).</p>',
     '<p>Le code généré <strong>DOIT</strong> franchir une porte de validation avant exécution : analyse statique fondée sur une liste d’autorisation de modules et de constructions, et refus des constructions d’évaluation dynamique (<code>eval</code> et équivalents) dans les agents en production. Cette porte est une mesure d’appoint; le bac à sable reste le contrôle principal. Une exécution qui demande des privilèges ou des destinations réseau absents de la fiche est refusée; leur ajout passe par une modification de la fiche approuvée au registre. Pendant l’exécution, une surveillance <strong>DOIT</strong> détecter au minimum les processus inattendus, les connexions refusées et les volumes d’écriture inhabituels, et alerter la sécurité.</p>',
     ['4.27', '4.77']),
    # ---------------------------------------------------------------- § 9.8
    # [4.28, 4.29, 4.80, A-21] SEC-18 : empreinte par type de composant; granularité de la suspension
    ('(nom, titre, description, icônes, schémas d’entrée et de sortie, annotations et <code>_meta</code>). À chaque <code>tools/list</code> (EXIG-MCP-20) et avant chaque exécution, la passerelle d’agents <strong>DOIT</strong> vérifier que la définition présentée correspond à l’empreinte épinglée au catalogue et, en cas d’écart, retirer et suspendre le composant jusqu’à une nouvelle approbation.</p>\n'
     '<div id="pourquoi-918"><p>Pourquoi : l’épinglage par empreinte, revérifié avant exécution, neutralise la substitution après approbation, et la revue de la définition complète à l’inscription réduit le risque d’empoisonnement d’outil<strong><sup>[221]</sup></strong>.</p></div>',
     '(pour un outil MCP : nom, titre, description, icônes, schémas d’entrée et de sortie, annotations et <code>_meta</code>). À chaque <code>tools/list</code> (EXIG-MCP-20) et avant chaque exécution, la passerelle d’agents <strong>DOIT</strong> vérifier que la définition présentée correspond à l’empreinte épinglée au catalogue. L’empreinte est, pour un outil MCP, le SHA-256 de sa définition canonisée selon la RFC 8785; pour une carte A2A, celui de son contenu signé canonisé; pour une compétence ou un paquet, celui de l’archive. Pour un modèle hébergé, l’identifiant de version servi (<code>gen_ai.response.model</code> ou date d’instantané) en tient lieu, et son changement déclenche une réévaluation (EXIG-GOV-12). En cas d’écart, la passerelle retire et suspend l’outil dont l’empreinte diffère, ou le serveur entier si l’écart touche ses instructions, plusieurs outils ou l’empreinte du serveur, jusqu’à une nouvelle approbation.</p>\n'
     '<div id="pourquoi-918"><p>Pourquoi : l’épinglage par empreinte, revérifié avant exécution, neutralise la substitution de définition après approbation, et la revue de la définition complète à l’inscription réduit le risque d’empoisonnement d’outil<strong><sup>[221]</sup></strong>. Il ne couvre ni le comportement du serveur ni ses valeurs de retour, qui restent du contenu non fiable (EXIG-SEC-03, EXIG-SEC-06).</p></div>',
     ['4.28', '4.29', '4.80', 'A-21']),
    # [4.29] serveurs distants de tiers : risque résiduel nommé
    ('l’intégrité d’un serveur MCP repose donc sur l’épinglage par empreinte et sur la signature des artefacts déployés.</p>',
     'l’intégrité de la définition d’un serveur MCP repose donc sur l’épinglage par empreinte et, pour un serveur que l’entreprise déploie, sur la signature de ses artefacts. Un serveur distant de tiers n’offre que l’épinglage de sa définition : son comportement relève des clauses du chapitre 13, et le risque résiduel est consigné à la fiche.</p>',
     ['4.29']),
    # [4.30] SEC-19 : ancre de confiance de la clé
    ('vérifier au moins une signature valide, faite avec une clé ni expirée ni révoquée, avant de faire confiance à la carte.',
     'vérifier au moins une signature valide, faite avec une clé inscrite au catalogue pour cet éditeur ou publiée par le domaine de l’agent avec une liaison <code>kid</code>/<code>jku</code> vérifiée (EXIG-SEC-12), ni expirée ni révoquée, avant de faire confiance à la carte.',
     ['4.30']),
    ('car sans signature un agent malveillant peut publier une carte qui imite un agent légitime<strong><sup>[68]</sup></strong>.</p>',
     'car sans signature un agent malveillant peut publier une carte qui imite un agent légitime<strong><sup>[68]</sup></strong>; une signature ne prouve toutefois l’éditeur que si la clé lui est liée, puisqu’un imitateur peut signer avec sa propre clé valide.</p>',
     ['4.30']),
    # [4.32] SEC-20 : agents N3-N4 et exposés au contenu non fiable
    ('<p>Chaque version d’un agent de risque modéré ou élevé <strong>DOIT</strong>',
     '<p>Chaque version d’un agent de risque modéré ou élevé, de niveau N3 ou N4, ou qui consomme du contenu non fiable, <strong>DOIT</strong>',
     ['4.32']),
    # [4.81] SEC-21 : catalogue ou registre selon le composant
    ('Le trafic vers un serveur MCP ou un agent absent du catalogue ou du registre <strong>DOIT</strong>',
     'Le trafic vers tout serveur MCP ou agent distant absent du catalogue, et vers tout agent interne absent du registre, <strong>DOIT</strong>',
     ['4.81']),
    # [4.31, 4.82] SEC-22 : proportionnalité définie; exception de l’art. 25(4)
    ('faire l’objet d’une évaluation de sécurité proportionnée au palier de ses outils.',
     'faire l’objet d’une évaluation de sécurité proportionnée au palier le plus élevé des outils qu’il expose ou, pour un modèle ou un agent, à la classe de risque la plus élevée des agents qui l’utilisent.',
     ['4.82']),
    ('Lorsqu’un composant est intégré à un système à haut risque au sens du RIA, un accord écrit <strong>DOIT</strong> être conclu avec le tiers (chapitre 13).</p>',
     'Lorsque l’entreprise est fournisseur d’un système à haut risque au sens du RIA, un accord écrit <strong>DOIT</strong> être conclu avec le tiers qui fournit un composant intégré à ce système (art. 25(4), chapitre 13), sauf pour un composant autre qu’un modèle d’IA à usage général publié sous licence libre et ouverte, qui fait alors l’objet d’une évaluation renforcée et d’un plan de contingence (choix du cadre).</p>',
     ['4.31']),
    # ---------------------------------------------------------------- § 9.9
    # [4.32, 4.33, A-25, A-32] SEC-23 : sujets élargis, pilote, échelle de gravité, agent en production
    ('<p>Tout agent de classe de risque modérée ou élevée <strong>DOIT</strong> subir, avant sa mise en production puis au moins une fois par année (choix du cadre),',
     '<p>Tout agent de classe de risque modérée ou élevée, tout agent de niveau N3 ou N4 et tout agent qui consomme du contenu non fiable <strong>DOIT</strong> subir, avant sa mise en production (l’entrée en pilote sur données réelles en est une) puis au moins une fois par année (choix du cadre),',
     ['4.32', 'A-25']),
    ('Un constat de gravité critique non corrigé <strong>DOIT</strong> bloquer la mise en production.</p>',
     'La gravité des constats se cote sur une échelle à quatre degrés (faible, moyenne, élevée, critique) inscrite au catalogue; est critique un constat qui permet, sans autre faille, une action P3 non approuvée, une exfiltration de RP ou un contournement de la passerelle (choix du cadre). Un constat de gravité critique non corrigé <strong>DOIT</strong> bloquer la mise en production; en production, il <strong>DOIT</strong> entraîner sous 5 jours ouvrables (choix du cadre) la suspension ciblée de l’agent ou une dérogation (section 11.6).</p>',
     ['4.33']),
    # [4.34, 4.83, 4.99 f, A-24, A-32] SEC-24 : déclencheurs, seuil indépendant, règle statistique
    ('<p>La chaîne d’intégration et de déploiement <strong>DOIT</strong> exécuter, à chaque nouvelle version d’un agent (modèle, invite système, outil ou palier modifié), une suite d’attaques automatisées rédigées en français et en anglais, par exemple des scénarios dérivés d’AgentDojo, et bloquer le déploiement si le taux de réussite des attaques dépasse le seuil fixé à la fiche de l’agent.</p>',
     '<p>La chaîne d’intégration et de déploiement <strong>DOIT</strong> exécuter, à chaque nouvelle version d’un agent (tout changement visé par l’EXIG-GOV-12), une suite d’attaques automatisées rédigées en français et en anglais, par exemple des scénarios dérivés d’AgentDojo, attaques adaptatives comprises, et bloquer le déploiement si le taux de réussite des attaques dépasse le seuil. Le seuil est fixé par la fonction risques et conformité, sous un plafond par classe, et non par l’équipe qui déploie; il se décide selon la règle de l’EXIG-EVA-03. Une part de la suite est renouvelée chaque trimestre. Cette suite est la composante adverse de l’étage E2 d’évaluation (section 10.4), avec un seul seuil.</p>',
     ['4.34', '4.83', '4.99', 'A-24', 'A-32']),
    # [4.01, 4.05, 4.29, 4.30, 4.84, A-10] SEC-25 : cas négatifs complétés
    ('<p>Les essais <strong>DOIVENT</strong> démontrer, par des cas négatifs, que : la passerelle retire les outils d’envoi après la lecture d’un contenu non fiable (EXIG-SEC-06); un jeton d’approbation altéré, rejoué ou lié à d’autres arguments est refusé; un bac à sable ne peut joindre ni une destination hors liste, ni le DNS, ni le service de métadonnées; une définition d’outil modifiée est bloquée (EXIG-SEC-18).</p>',
     '<p>Les essais <strong>DOIVENT</strong> démontrer, par des cas négatifs, que : la passerelle retire de l’exécution autonome les outils d’envoi après la lecture d’un contenu non fiable (EXIG-SEC-06), y compris quand le contenu arrive par un autre agent (l’un lit, l’autre envoie) ou par une entrée de mémoire empoisonnée; un jeton d’approbation altéré, présenté avec une autre empreinte ou lié à d’autres arguments est refusé, alors que la présentation répétée de la même opération est relayée sans nouvelle approbation (EXIG-AUT-12); une carte non signée ou signée d’une clé non inscrite, un serveur hors catalogue, un élargissement de portée, une audience erronée et un échange qui prolonge une délégation sont refusés; un bac à sable ne peut joindre ni une destination hors liste, ni le DNS, ni le service de métadonnées, ni une plage à usage spécial, IPv6 comprise; une définition d’outil modifiée est bloquée (EXIG-SEC-18), et une valeur de retour piégée reste traitée comme non fiable; la passerelle refuse en mode fermé quand une dépendance est indisponible.</p>',
     ['4.01', '4.05', '4.29', '4.30', '4.84', 'A-10']),
    # [4.15, 4.16, 4.99 a-b, A-05, A-06] SEC-26 : exercice unique, mesure, compensations
    ('<p>Au moins une fois par trimestre (choix du cadre), la plateforme <strong>DOIT</strong> exercer le scénario d’un agent compromis : arrêt par le coupe-circuit, révocation de ses identités et de ses jetons, mise en quarantaine et préservation des preuves. Le délai réel de révocation <strong>DOIT</strong> être mesuré et comparé à la cible de 15 minutes du tableau 61; tout dépassement <strong>DOIT</strong> ouvrir une action corrective. Cet exercice <strong>PEUT</strong> se combiner à l’essai trimestriel du coupe-circuit prévu à la section 7.8.</p>',
     '<p>Au moins une fois par trimestre (choix du cadre), la plateforme <strong>DOIT</strong> exercer le scénario d’un agent compromis : arrêt par le coupe-circuit, révocation de ses identités et de ses jetons, mise en quarantaine, préservation des preuves, poursuite des compensations des sagas en cours par le canal de compensation (EXIG-ORC-31) et panne d’une instance de la passerelle (EXIG-IAM-22). L’exercice se fait en production sur un agent témoin, avec une rotation qui couvre chaque classe de risque et les systèmes raccordés sans SSF ni CAEP. Le délai mesuré est celui de l’EXIG-IAM-20 (refus du dernier appel dans tous les systèmes, durée de vie résiduelle des jetons comprise); il <strong>DOIT</strong> être comparé à la cible fixée par l’entreprise (proposée à 15 minutes au tableau 61), et tout dépassement <strong>DOIT</strong> ouvrir une action corrective. Cet exercice est le seul exercice du coupe-circuit : l’EXIG-ORC-28 et l’EXIG-IAM-20 y renvoient.</p>',
     ['4.15', '4.16', '4.99', 'A-05', 'A-06']),
    # ---------------------------------------------------------------- § 10.1
    # [A-19, A-27] chapeau du chapitre 10
    ('un journal d’audit inaltérable, distinct de cette trace. Il organise l’évaluation continue en trois paliers,',
     'un journal d’audit chaîné et ancré, distinct de cette trace. Il organise l’évaluation continue en trois étages (E1 à E3),',
     ['A-19', 'A-27']),
    # [4.02, A-29] conformité mesurée après correspondance
    ('Le cadre impose donc le mécanisme, épingle une version des conventions et lit les données par une couche de correspondance.',
     'Le cadre impose donc le mécanisme, épingle une version de référence des conventions et y ramène, par une couche de correspondance au collecteur, ce que chaque composant émet.',
     ['4.02', 'A-29']),
    # [4.02, 4.35, 4.99 d, A-02, A-29] OBS-01
    ('<p>Tout composant d’une exécution d’agent (canal, orchestrateur, passerelles, agent, serveur MCP, consommateur d’événements) <strong>DOIT</strong> émettre traces et métriques par OpenTelemetry, en OTLP, vers le collecteur de la plateforme, selon la version des conventions GenAI épinglée au catalogue (v1.41.0, jusqu’à l’homologation d’une version étiquetée du dépôt dédié). Tableaux de bord, alertes et calculs de coûts lisent les données par une couche de correspondance versionnée; un changement de version des conventions se gère comme un changement de contrat (section 6.8).</p>',
     '<p>Tout composant d’une exécution d’agent exploité par l’entreprise (canal, orchestrateur, passerelles, courtier d’événements, agent, serveur MCP, consommateur d’événements) <strong>DOIT</strong> émettre traces et métriques par OpenTelemetry, en OTLP, vers le collecteur de la plateforme, selon une version des conventions GenAI consignée au catalogue pour ce composant (version émise et réglage d’<code>OTEL_SEMCONV_STABILITY_OPT_IN</code>). Une couche de correspondance versionnée du collecteur la ramène à la version de référence épinglée au catalogue, la ligne v1.41 (v1.41.0; correctif v1.41.1 admis après vérification qu’il ne modifie pas les attributs <code>gen_ai.*</code>), jusqu’à l’homologation d’une version étiquetée du dépôt dédié. Tableaux de bord, alertes et calculs de coûts lisent les données après correspondance; un changement de version des conventions se gère comme un changement de contrat (section 6.8). Un composant de tiers qui n’émet pas vers le collecteur de l’entreprise est couvert par les spans CLIENT et les métriques de la passerelle, et par une clause contractuelle d’export de télémétrie (chapitre 13).</p>',
     ['4.02', '4.35', '4.99', 'A-02', 'A-29']),
    # [4.85] OBS-02 : composant interne défini
    ('Un composant interne <strong>DOIT</strong> poursuivre la trace d’un autre composant interne;',
     'Un composant interne, c’est-à-dire authentifié par une identité de charge de travail inscrite au registre, <strong>DOIT</strong> poursuivre la trace d’un autre composant interne;',
     ['4.85']),
    # [4.36] légende de la figure 21 (figure non modifiable)
    ('l’attente d’approbation et l’écriture finale; le résultat d’évaluation s’attache au span évalué.',
     'l’attente d’approbation (que l’EXIG-OBS-04 représente par deux événements, et non par un span ouvert pendant l’attente) et l’écriture finale; le résultat d’évaluation s’attache au span évalué.',
     ['4.36']),
    # [4.36, 4.86] OBS-04 : attente d’approbation par événements; span MCP pour un outil MCP
    ('<code>execute_tool</code> par appel d’outil avec le span MCP CLIENT correspondant. Attentes d’approbation, compensations et refus de la passerelle y figurent comme spans ou événements.',
     '<code>execute_tool</code> par appel d’outil et, pour un outil MCP, le span MCP CLIENT correspondant. Compensations et refus de la passerelle y figurent comme spans ou événements. Une attente d’approbation <strong>DOIT</strong> se représenter par un événement d’ouverture et un événement de fermeture, et non par un span ouvert pendant l’attente; la reprise ouvre un nouveau span, relié au précédent par un lien de span.',
     ['4.36', '4.86']),
    # [4.02, 4.40, A-29] OBS-05 : à la sortie du collecteur; échantillonnage en queue
    ('<p>Chaque span <strong>DOIT</strong> porter, parmi les attributs que le tableau 41 rend obligatoires, ceux qui s’appliquent à son type (inférence, agent, flux, outil, appel MCP), et chaque composant <strong>DOIT</strong> exposer les métriques de durée et de jetons de la version épinglée. Un composant qui ne les produit pas <strong>NE DOIT PAS</strong> être homologué; un attribut obligatoire manquant en production <strong>DOIT</strong> déclencher une alerte.</p>',
     '<p>Chaque span <strong>DOIT</strong> porter, à la sortie du collecteur, après correspondance, parmi les attributs que le tableau 41 rend obligatoires, ceux qui s’appliquent à son type (inférence, agent, flux, outil, appel MCP), et chaque composant <strong>DOIT</strong> exposer, après correspondance, les métriques de durée et de jetons de la version de référence. Un composant qui ne les produit pas, même après correspondance, <strong>NE DOIT PAS</strong> être homologué; un attribut obligatoire manquant en production <strong>DOIT</strong> déclencher une alerte, mesurée avant échantillonnage. L’échantillonnage des traces <strong>DOIT</strong> conserver toutes les traces marquées (erreur, relance, plafond atteint, refus d’approbation), par un échantillonnage en queue au collecteur avec répartition par <code>trace_id</code>.</p>',
     ['4.02', '4.40', 'A-29']),
    # [4.87] tableau 41 : l’approbateur sort des spans
    ('<code>ca.entreprise.autonomy_level</code>, <code>ca.entreprise.approval.approver</code></td><td>Hors convention</td><td>Obligatoires; approbateur sous pseudonyme</td>',
     '<code>ca.entreprise.autonomy_level</code>, <code>ca.entreprise.approval.jti</code></td><td>Hors convention</td><td>Obligatoires; l’approbateur ne figure qu’au journal d’audit, joint par l’identifiant du jeton d’approbation</td>',
     ['4.87']),
    ('Une personne, approbateur compris, n’y figure que sous un identifiant pseudonyme.</p>',
     'Une personne n’y figure que sous un identifiant pseudonyme, et l’approbateur n’y figure pas : il est consigné au seul journal d’audit (section 10.3).</p>',
     ['4.87']),
    # ---------------------------------------------------------------- § 10.2
    # [A-18, 4.41] autres magasins du contenu
    ('Le cadre retient le premier mode en production et le troisième pour le débogage.</p>',
     'Le cadre retient le premier mode en production et le troisième pour le débogage. Les autres usages du contenu ont leur propre magasin, hors de la télémétrie : le dossier de décision (EXIG-OBS-14) et le dépôt d’évaluation (EXIG-EVA-07).</p>',
     ['4.41', 'A-18']),
    ('par une référence placée sur le span.</p>',
     'par une référence placée sur le span. Pour évaluer la qualité ou justifier une décision, on passe par les magasins qui leur sont propres (EXIG-EVA-07, EXIG-OBS-14), jamais par la télémétrie.</p>',
     ['4.41', 'A-18']),
    # [4.37, A-18] OBS-07 : exceptions, statuts, noms de spans; renvoi aux autres régimes
    ('ni les autres contenus que la convention soumet à la capture de contenu (requêtes de recherche, variables d’invite, mémoire de l’agent). Cette interdiction',
     'ni les autres contenus que la convention soumet à la capture de contenu (requêtes de recherche, variables d’invite, mémoire de l’agent), ni les messages et traces d’exception, descriptions de statut, noms de spans et membres du bagage qui en recopient. Les autres régimes du contenu relèvent des EXIG-OBS-08 (débogage), EXIG-OBS-14 (dossier de décision), EXIG-EVA-07 (évaluation) et EXIG-CON-23 (incident). Cette interdiction',
     ['4.37', 'A-18']),
    # [4.88, A-18] OBS-08 : attribut de référence; gel des preuves; usages exclus
    ('et n’apparaître sur le span que par une référence. Le contenu est détruit après 14 jours au plus (choix du cadre).</p>',
     'et n’apparaître sur le span que par une référence (attribut <code>ca.entreprise.content_ref</code>, en attendant les attributs <code>*_ref</code> de la convention). Le contenu est détruit après 14 jours au plus (choix du cadre), sauf gel des preuves (EXIG-CON-23). Une capture de débogage ne sert ni à l’évaluation de production (EXIG-EVA-07) ni au dossier de décision (EXIG-OBS-14).</p>',
     ['4.88', 'A-18']),
    # [4.89, 4.37] OBS-09 : essai par signal; exceptions caviardées
    ('Les règles de masquage <strong>DOIVENT</strong> être testées en français et en anglais à chaque modification.</p>',
     'Le collecteur tronque ou caviarde les messages d’exception et les descriptions de statut. Les règles de masquage <strong>DOIVENT</strong> être testées en français et en anglais à chaque modification, par un essai de non-fuite propre à chaque type de signal (traces, métriques, journaux); là où le processeur <code>redaction</code>, Alpha pour les métriques et les journaux, ne couvre pas un champ, une autre transformation du collecteur (processeur <code>transform</code>) en tient lieu.</p>',
     ['4.89', '4.37']),
    # [4.90] OBS-10 : filtre au collecteur et aux SDK; tracestate aux frontières
    ('La passerelle <strong>DOIT</strong> retirer tout membre du bagage absent de la liste inscrite au catalogue.</p>',
     'La passerelle, le collecteur et les SDK (par un propagateur filtrant) <strong>DOIVENT</strong> retirer tout membre du bagage absent de la liste inscrite au catalogue. À une frontière de confiance, <code>tracestate</code> suit la règle de l’EXIG-OBS-02 : les membres reçus de l’extérieur ne sont pas propagés vers l’intérieur.</p>',
     ['4.90']),
    # ---------------------------------------------------------------- § 10.3
    # [4.38, A-19] portée et nature du journal
    ('Le journal d’audit est exhaustif pour les actions à effet, inaltérable et signé.',
     'Le journal d’audit est exhaustif pour les actions à effet et les lectures de données sensibles, chaîné, ancré hors de son domaine d’administration et signé.',
     ['4.38', 'A-19']),
    # [4.91, A-11, A-12] cinq éléments
    ('(3) l’<strong>action</strong>, soit l’outil, la version de sa définition, l’empreinte SHA-256 des arguments et l’issue;',
     '(3) l’<strong>action</strong>, soit l’outil, la version et l’empreinte de sa définition (EXIG-SEC-18), l’empreinte des arguments et l’issue;',
     ['4.91', 'A-11']),
    ('soit le jeton d’approbation (section 8.5), soit la règle qui permettait d’agir sans approbation. S’y ajoutent l’horodatage et les identifiants de corrélation',
     'soit le ou les jetons d’approbation (section 8.5), soit la règle qui permettait d’agir sans approbation, avec le contrôle appliqué et la version de la politique. S’y ajoutent l’horodatage, le numéro de séquence et l’empreinte de l’enregistrement précédent du même flux (EXIG-OBS-12), ainsi que les identifiants de corrélation',
     ['4.91', 'A-12', 'A-19']),
    # [4.91] extrait aligné sur l’annexe C.8
    ('<pre><code>{\n'
     '  "horodatage":  "2026-10-27T14:03:12.418Z",\n'
     '  "correlation": { "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "tache": "tache-7f3c2a",\n'
     '                   "a2a_task_id": "…", "a2a_context_id": "…", "cle_idempotence": "…" },\n'
     '  "mandant":   { "type": "user", "pseudonyme": "u-5d1e…" },\n'
     '  "agent":     { "id": "agent-risque-credit", "version": "2.3.0", "invite_systeme": "sha256:…" },\n'
     '  "action":    { "outil": "erp_enregistrer_decision", "definition": "1.4.1",\n'
     '                 "arguments_sha256": "…", "issue": "succes" },\n'
     '  "modele":    { "fournisseur": "…", "servi": "…", "version": "…" },\n'
     '  "autorite":  { "approbation_jti": "…", "approbateur": "a-91c0…" },\n'
     '  "precedent_sha256": "…",\n'
     '  "signature": "&lt;signature du service d’audit&gt;"\n'
     '}</code></pre>',
     '<pre><code>{\n'
     '  "empreinte": "sha256:…",\n'
     '  "enregistrement": {\n'
     '    "action":      { "outil": "erp_enregistrer_decision", "definition": "1.4.1",\n'
     '                     "definition_sha256": "sha256:…", "arguments_sha256": "…", "issue": "succes" },\n'
     '    "agent":       { "id": "agent-risque-credit", "version": "2.3.0", "invite_systeme": "sha256:…" },\n'
     '    "autorite":    { "approbation_jti": "…", "approbateur": "a-91c0…", "controle": "…",\n'
     '                     "empreinte_approbation": "…", "version_politique": "…" },\n'
     '    "correlation": { "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "tache": "tache-7f3c2a",\n'
     '                     "a2a_task_id": "…", "a2a_context_id": "…", "cle_idempotence": "…" },\n'
     '    "horodatage":  "2026-10-27T14:03:12.418Z",\n'
     '    "mandant":     { "type": "user", "pseudonyme": "u-5d1e…" },\n'
     '    "modele":      { "fournisseur": "…", "servi": "…", "version": "…" },\n'
     '    "precedent_sha256": "sha256:…",\n'
     '    "sequence":    1207\n'
     '  },\n'
     '  "signature": { "alg": "ES256", "kid": "…", "valeur": "…" }\n'
     '}</code></pre>',
     ['4.91']),
    # [4.14, 4.38, A-10, A-19] OBS-11 : intention avant l’effet; lectures P1 sensibles; dépendance d’AUT-11
    ('<p>Chaque action à effet (outil P2 ou P3), chaque approbation ou refus d’approbation, chaque refus de la passerelle (EXIG-IAM-18) et chaque arrêt par coupe-circuit <strong>DOIT</strong> produire un enregistrement d’audit, sans échantillonnage.',
     '<p>Avant de relayer un appel P2 ou P3, la passerelle <strong>DOIT</strong> écrire un enregistrement d’intention chaîné (empreinte h, jeton d’approbation, décision); l’enregistrement d’issue suit, ou constate une issue inconnue. Chaque action à effet (outil P2 ou P3), chaque appel P1 portant sur des RP ou des données classifiées (au besoin agrégé par tâche), chaque approbation ou refus d’approbation, chaque refus de la passerelle (EXIG-IAM-18) et chaque arrêt par coupe-circuit <strong>DOIT</strong> produire un enregistrement d’audit, sans échantillonnage. Le service d’audit fait partie des dépendances de l’EXIG-AUT-11 : s’il est indisponible, les appels P2 et P3 sont refusés.',
     ['4.14', '4.38', 'A-10', 'A-19']),
    # [4.39, 4.92, A-11, A-19] OBS-12 : flux, ancrage externe, empreinte, h redéfini
    ('<p>Chaque enregistrement <strong>DOIT</strong> contenir les cinq éléments et les identifiants de corrélation, être canonisé selon la RFC 8785, porter l’empreinte de l’enregistrement précédent du même flux et être signé par une clé du service d’audit, hors de portée des agents. Les arguments d’outil n’y figurent que par leur empreinte SHA-256, calculée sur leur forme canonisée; lorsqu’une approbation a eu lieu, l’empreinte d’approbation h (outil ‖ arguments canonisés, section 8.5) y figure aussi.</p>\n'
     '<div id="pourquoi-983"><p>Pourquoi : choix du cadre; la canonisation de la RFC 8785<strong><sup>[236]</sup></strong> rend l’empreinte reproductible, de sorte que l’empreinte d’approbation, recalculée par la passerelle avant l’exécution, prouve que l’action exécutée est celle qui a été approuvée, et le chaînage rend toute suppression détectable.</p></div>',
     '<p>Chaque enregistrement <strong>DOIT</strong> contenir les cinq éléments et les identifiants de corrélation, être canonisé selon la RFC 8785, porter son numéro de séquence et l’empreinte de l’enregistrement précédent du même flux, et être signé par une clé du service d’audit, hors de portée des agents. L’empreinte d’un enregistrement est le SHA-256 de sa forme canonisée, signature exclue, comme à l’annexe C.8. Un flux est la séquence numérotée d’une instance d’écriture, inscrite à un registre des flux. Au moins toutes les heures, un point de contrôle signé et daté de la tête de chaque flux (numéro de séquence, empreinte) <strong>DOIT</strong> être publié hors du domaine d’administration du service d’audit (témoin, registre de transparence sur le modèle de la RFC 9162, ou stockage WORM sous une autre administration), et la cohérence est vérifiée par une fonction indépendante. Les arguments d’outil n’y figurent que par leur empreinte SHA-256, calculée sur leur forme canonisée; pour des arguments à faible entropie, cette empreinte est salée ou remplacée par un HMAC sous une clé du service d’audit. Lorsqu’une approbation a eu lieu, l’empreinte d’approbation h (empreinte de l’action approuvée, EXIG-AUT-12) y figure aussi.</p>\n'
     '<div id="pourquoi-983"><p>Pourquoi : choix du cadre; la canonisation de la RFC 8785<strong><sup>[236]</sup></strong> rend l’empreinte reproductible, de sorte que l’empreinte d’approbation, recalculée par la passerelle avant l’exécution, atteste que les octets transmis sont ceux qui ont été approuvés, non que l’effet est celui qui était attendu. Le chaînage détecte la modification ou la suppression interne; la troncature et la réécriture par le détenteur de la clé ne se détectent que par les points de contrôle externes.</p></div>',
     ['4.39', '4.92', 'A-11', 'A-19']),
    # [4.39, A-19] OBS-13 : vérification contre les points de contrôle; purge par segments
    ('et son intégrité <strong>DOIT</strong> être vérifiée automatiquement chaque jour. Il est conservé au moins 24 mois, davantage si le calendrier de conservation, un régime sectoriel ou une enquête l’exige, puis détruit ou anonymisé à l’échéance (EXIG-CON-10);',
     'et son intégrité <strong>DOIT</strong> être vérifiée automatiquement chaque jour, contre les derniers points de contrôle publiés (EXIG-OBS-12). Il est conservé au moins 24 mois, davantage si le calendrier de conservation, un régime sectoriel ou une enquête l’exige (EXIG-CON-10), puis purgé à l’échéance, sauf gel des preuves (EXIG-CON-23), par segments entiers clos par un point de reprise signé; l’anonymisation se fait par destruction des lignes correspondantes de la table des pseudonymes, jamais par réécriture d’un enregistrement, et les clés de vérification sont conservées toute la durée de rétention;',
     ['4.39', 'A-19']),
    # [A-18] nouvelle exigence EXIG-OBS-14 (dossier de décision)
    ('<h3>10.4 Évaluation continue</h3>',
     '<div id="exig-obs-14">\n'
     '<p><strong><code>EXIG-OBS-14</code> · DOIT</strong></p>\n'
     '<p><strong>Dossier de décision</strong></p>\n'
     '<p>Pour toute décision visée par l’art. 12.1 de la Loi sur le privé ou par l’art. 65.2 de la Loi sur l’accès, l’agent <strong>DOIT</strong> verser à un dossier de décision chiffré, sous le contrôle du responsable de la protection des renseignements personnels, les RP en entrée, les versions de l’agent, du modèle et des outils, les facteurs retenus et les approbations. Le dossier est distinct de la télémétrie et du journal d’audit, auquel il est relié par empreinte; chaque accès y est journalisé. Il est conservé au moins un an après la décision (EXIG-CON-09), puis détruit, sauf gel des preuves (EXIG-CON-23). Les facteurs consignés sont ceux du processus déterministe, jamais le raisonnement affiché du modèle.</p>\n'
     '<div id="pourquoi-obs-14"><p>Pourquoi : l’EXIG-CON-09 exige de conserver ces éléments pour répondre aux demandes de la personne, alors que la télémétrie ne porte aucun contenu et que l’audit ne garde que des empreintes; sans magasin désigné, l’obligation ne peut pas être exécutée. Le magasin unique et ses droits sont un choix du cadre.</p></div>\n'
     '</div>\n'
     '<h3>10.4 Évaluation continue</h3>',
     ['4.41', 'A-18']),
    # ---------------------------------------------------------------- § 10.4
    # [A-27, 4.99 f, 4.93] figure 22 : étages, déclencheurs, plafond atteint (figure non modifiable)
    ('la qualité se mesure, en trois paliers (figure 22).',
     'la qualité se mesure, en trois étages, E1 à E3 (figure 22, qui les nomme « paliers »).',
     ['A-27']),
    ('Tout changement de modèle, d’invite, d’outil ou de version de protocole relance les deux premiers. Source : cadre CRE-IA-2026-01.</figcaption>',
     'Tout changement visé par l’EXIG-GOV-12 relance les deux premiers avant la mise en service. Le texte nomme ces paliers « étages » (E1 à E3), et l’étage E3 évalue aussi toutes les traces qui ont atteint un plafond (EXIG-EVA-04). Source : cadre CRE-IA-2026-01.</figcaption>',
     ['4.99', '4.93', '4.42', 'A-24', 'A-27']),
    ('<p><strong>Palier 1 : contrats.</strong>',
     '<p><strong>Étage E1 : contrats.</strong>',
     ['A-27']),
    ('rejoue l’injection de fautes des sagas (EXIG-ORC-20).',
     'rejoue l’injection de fautes des sagas (EXIG-ORC-20), y compris la suspension de l’agent et l’épuisement de son enveloppe en cours de saga.',
     ['4.16']),
    ('<p><strong>Palier 2 : trajectoires.</strong> Sur un jeu de référence de 50 à 200 scénarios (fourchette du cadre),',
     '<p><strong>Étage E2 : trajectoires.</strong> Sur un jeu de référence d’au moins 50 scénarios (200 à titre indicatif, choix du cadre),',
     ['A-27', '4.43']),
    ('<p><strong>Palier 3 : production.</strong> On évalue de 5 à 10 % des traces (fourchette du cadre), plus toutes celles',
     '<p><strong>Étage E3 : production.</strong> On évalue un échantillon aléatoire d’au moins 5 % des exécutions (10 % recommandé, choix du cadre), plus toutes les traces',
     ['A-27', '4.93']),
    # [4.95, 4.46, A-32] tableau 42 : cibles précisées
    ('<td>Succès des appels MCP et A2A; latence par étape au 95<sup>e</sup> centile</td>',
     '<td>Succès des appels MCP et A2A, refus de politique exclus; latence par étape au 95<sup>e</sup> centile</td>',
     ['4.95']),
    ('<td>Réponses non ancrées sur échantillon; violations de garde-fous; approbations sans modification (section 8.7)</td><td>Moins de 0,5 % de réponses non ancrées; aucune violation d’un garde-fou bloquant</td>',
     '<td>Réponses non ancrées sur échantillon; violations de garde-fous (contournement effectif, non tentative bloquée); approbations sans modification (section 8.7)</td><td>Moins de 0,5 % de réponses non ancrées, démontré selon l’EXIG-EVA-03; aucune violation d’un garde-fou bloquant; approbations sans modification sous le seuil d’alerte de l’EXIG-AUT-21</td>',
     ['4.95', 'A-32']),
    ('<td>Coût moyen et au 99<sup>e</sup> centile par tâche réussie, en dollars canadiens</td><td>Sous le coût du processus de référence sans agent</td>',
     '<td>Coût total moyen et au 99<sup>e</sup> centile par tâche réussie, en dollars canadiens (section 10.6)</td><td>Coût moyen sous le coût du processus de référence sans agent ou, à défaut de processus de référence, sous la valeur attendue inscrite à la fiche</td>',
     ['4.95', '4.46']),
    # [4.42, A-24, A-27] EVA-01 : réévaluation avant la mise en service; alias
    ('<p>Tout agent <strong>DOIT</strong> franchir les paliers 1 et 2 avant sa mise en production et rester soumis au palier 3 en exploitation. Tout changement de modèle, y compris derrière un même alias (EXIG-ARC-09), d’invite système, d’outil, de palier d’outil ou de version de protocole relance les paliers d’évaluation 1 et 2. Les tests du palier 1 <strong>DOIVENT</strong>',
     '<p>Tout agent <strong>DOIT</strong> franchir les étages E1 et E2 avant sa mise en production et rester soumis à l’étage E3 en exploitation. Tout changement visé par l’EXIG-GOV-12, dont tout changement du modèle servi, y compris derrière un même alias (EXIG-ARC-09), <strong>DOIT</strong> franchir de nouveau les étages E1 et E2 avant de servir en production; la passerelle de modèles <strong>NE DOIT PAS</strong> résoudre un alias vers une cible qui ne les a pas franchis, ni vers un alias flottant du fournisseur (p. ex. « -latest ») : elle vise une version épinglée. Les tests de l’étage E1 <strong>DOIVENT</strong>',
     ['4.42', '4.99', 'A-24', 'A-27']),
    # [4.43, A-18, A-32] EVA-02 : jeu non plafonné, réservé, alimenté par le dépôt d’évaluation
    ('<p>Chaque agent <strong>DOIT</strong> disposer d’un jeu de référence de 50 à 200 scénarios, versionné avec lui, couvrant ses compétences, des cas limites et des tentatives d’injection en français et en anglais. Toute défaillance confirmée en production y ajoute un scénario. Les seuils de trajectoire, d’ancrage et de garde-fous figurent au contrat; un seuil manqué bloque la mise en production.</p>',
     '<p>Chaque agent <strong>DOIT</strong> disposer d’un jeu de référence d’au moins 50 scénarios (200 à titre indicatif), versionné avec lui, stratifié par compétence, couvrant ses compétences, des cas limites et des tentatives d’injection en français et en anglais, avec un sous-ensemble réservé, non communiqué à l’équipe qui construit l’agent. Toute défaillance confirmée en production y ajoute un scénario, reconstitué à partir du dépôt d’évaluation (EXIG-EVA-07), à un registre de régression non plafonné; une consolidation versionnée garde au moins un scénario par mode de défaillance. Les seuils de trajectoire, d’ancrage et de garde-fous figurent au contrat et se décident selon la règle de l’EXIG-EVA-03; un seuil manqué bloque la mise en production.</p>',
     ['4.43', 'A-18', 'A-32']),
    # [4.34, A-32] EVA-03 : règle de décision statistique
    ('<p>Les évaluations du palier 2 et les rejeux <strong>DOIVENT</strong> s’exécuter en environnement isolé, outils à effet remplacés par des doublures. Chaque scénario <strong>DOIT</strong> s’exécuter au moins trois fois (choix du cadre); on retient le taux de réussite et sa dispersion.</p>',
     '<p>Les évaluations de l’étage E2 et les rejeux <strong>DOIVENT</strong> s’exécuter en environnement isolé, outils à effet remplacés par des doublures. Chaque scénario <strong>DOIT</strong> s’exécuter au moins trois fois (choix du cadre); on retient le taux de réussite et sa dispersion. Toute porte (EXIG-SEC-24, EXIG-EVA-02, EXIG-EVA-04, tableau 42) et toute comparaison (EXIG-ORC-02) <strong>DOIT</strong> déclarer la taille d’échantillon, la statistique, l’intervalle de confiance et la règle de décision. Un taux cible p n’est démontré que si la borne supérieure de l’intervalle de confiance à 95 % (p. ex. de Wilson) est inférieure à p, ce qui exige au moins 3/p essais indépendants sans échec; les répétitions d’un même scénario ne sont pas indépendantes.</p>',
     ['4.34', 'A-32', 'A-27']),
    # [4.40, 4.41, 4.34, 4.93, A-18] EVA-04 : unité, plancher, calcul des taux, source du contenu
    ('<p>L’évaluation en production <strong>DOIT</strong> porter sur un échantillon aléatoire de 5 à 10 % des traces et sur toutes les traces marquées d’une erreur, d’une relance, d’un plafond atteint ou d’un refus d’approbation. Elle s’exécute hors du chemin critique, et chaque résultat est consigné par un événement <code>gen_ai.evaluation.result</code> rattaché au span évalué.</p>\n'
     '<div id="pourquoi-997"><p>Pourquoi : l’événement normalisé relie chaque score à son exécution (rattachement au span évalué ou, à défaut, par <code>gen_ai.response.id</code>); le ciblage des traces atypiques (erreur, relance, plafond, refus) est un choix du cadre<strong><sup>[396]</sup></strong>.</p></div>',
     '<p>L’évaluation en production <strong>DOIT</strong> porter sur un échantillon aléatoire d’au moins 5 % des exécutions (10 % recommandé; davantage pour la classe élevée), avec une taille minimale absolue par période inscrite au contrat, et sur toutes les traces marquées d’une erreur, d’une relance, d’un plafond atteint ou d’un refus d’approbation, conservées selon l’EXIG-OBS-05. Les taux se calculent sur la seule strate aléatoire, ou par pondération inverse; un agent à faible volume agrège plusieurs périodes. Le contenu évalué provient du dépôt d’évaluation (EXIG-EVA-07). Elle s’exécute hors du chemin critique, et chaque résultat est consigné par un événement <code>gen_ai.evaluation.result</code> rattaché au span évalué ou, à défaut, corrélé par <code>gen_ai.response.id</code>.</p>\n'
     '<div id="pourquoi-997"><p>Pourquoi : l’événement normalisé relie chaque score à son exécution; le ciblage des traces atypiques (erreur, relance, plafond, refus) et la règle de calcul des taux sont des choix du cadre<strong><sup>[396]</sup></strong>.</p></div>',
     ['4.40', '4.41', '4.34', '4.93', 'A-18', 'A-32']),
    # [4.44, 4.94] EVA-05 : juge d’un autre modèle; critère d’échec de la calibration
    ('<p>Un juge à base de modèle <strong>DOIT</strong> être distinct du modèle ou de l’invite qu’il évalue, appliquer une grille versionnée et être calibré contre des évaluations humaines, avec un taux d’accord revu chaque trimestre.',
     '<p>Un juge à base de modèle <strong>DOIT</strong> être distinct du modèle évalué, de préférence d’une autre famille ou d’un autre fournisseur, et avoir sa propre invite; à défaut d’un autre modèle, l’accord avec les évaluations humaines est mesuré dans cette configuration même. Il applique une grille versionnée et est calibré contre des évaluations humaines, sur un échantillon dont la taille figure au contrat, avec un taux d’accord revu chaque trimestre; un juge dont l’accord tombe sous le seuil du contrat (p. ex. kappa de Cohen inférieur à 0,6) n’alimente plus les indicateurs de l’EXIG-EVA-06.',
     ['4.44', '4.94']),
    # [4.45, 4.99 h] EVA-06 : période définie; escalade; renvoi à FIN-10
    ('Un objectif manqué pendant deux périodes consécutives (choix du cadre) déclenche une revue par le parrain et le responsable technique, qui corrigent, réduisent le niveau d’autonomie ou suspendent l’agent (section 11.5).</p>',
     'Un objectif manqué pendant deux mois civils consécutifs (choix du cadre) déclenche une revue par le parrain et le responsable technique, la fonction risques et conformité consultée, qui corrigent, réduisent le niveau d’autonomie ou suspendent l’agent (section 11.5); pour un agent de classe élevée ou de niveau N4, le comité en décide. Après trois mois sans retour sous la cible, l’autonomie est réduite d’un niveau et le comité est saisi. Pour l’économie unitaire, l’EXIG-FIN-10 s’applique.</p>',
     ['4.45', '4.99']),
    # [4.41, A-18] nouvelle exigence EXIG-EVA-07 (dépôt d’évaluation)
    ('<h3>10.5 Économie de l’inférence</h3>',
     '<div id="exig-eva-07">\n'
     '<p><strong><code>EXIG-EVA-07</code> · DOIT</strong></p>\n'
     '<p><strong>Dépôt d’évaluation</strong></p>\n'
     '<p>Le contenu nécessaire à l’évaluation de production (invite, résultats d’outils, réponse) <strong>DOIT</strong> être versé à un dépôt d’évaluation distinct de la télémétrie : échantillon caviardé et chiffré, finalité « évaluation de la qualité » déclarée à l’EFVP (section 12.2), rétention bornée à la fiche (30 jours par défaut, choix du cadre), accès journalisé et réservé à l’équipe d’évaluation, aux juges et aux réviseurs habilités, rattachement au span par référence. C’est la seule source du contenu évalué au titre de l’EXIG-EVA-04 et des scénarios ajoutés au titre de l’EXIG-EVA-02, qui en sont reconstitués puis anonymisés. Un juge asynchrone qui évalue le contenu en mémoire, sans le persister, est admis sans dépôt.</p>\n'
     '<div id="pourquoi-eva-07"><p>Pourquoi : juger l’ancrage ou la justesse d’une réponse exige son contenu, que la télémétrie ne porte pas (EXIG-OBS-07) et que la capture de débogage ne doit pas fournir en permanence (EXIG-OBS-08); un dépôt propre, à finalité déclarée, encadre cet usage (choix du cadre).</p></div>\n'
     '</div>\n'
     '<h3>10.5 Économie de l’inférence</h3>',
     ['4.41', 'A-18']),
    # ---------------------------------------------------------------- § 10.5
    # [4.99 j, A-28] résidence
    ('la zone « us » de l’API d’Anthropic n’est pas une résidence canadienne, et aucune zone canadienne n’y est offerte',
     'la zone « us » de l’API d’Anthropic n’est ni québécoise ni canadienne, et aucune zone canadienne n’y est offerte; toute zone hors du Québec relève de l’art. 17 (section 12.2)',
     ['4.99', 'A-28']),
    # [4.46, 4.96 a] FIN-01 : indicateur de sélection; segmenteurs et ratio
    ('<strong>DOIT</strong> reposer sur le coût par tâche réussie mesuré sur le jeu de référence (section 10.4), et non sur le prix du jeton. Le modèle de coût intègre les modificateurs de prix (lots, cache, résidence), la normalisation des jetons d’un segmenteur à l’autre et,',
     '<strong>DOIT</strong> reposer sur le coût d’inférence par tâche réussie mesuré sur le jeu de référence (section 10.4), pondéré par la distribution de production et augmenté du coût estimé des outils réels, et non sur le prix du jeton; le suivi en production (EXIG-FIN-10) emploie le coût total. Le modèle de coût intègre les modificateurs de prix (lots, cache, résidence), la normalisation des jetons d’un segmenteur à l’autre, qui vaut aussi pour le ratio jetons/résultat, dont la ligne de base est réinitialisée à chaque changement de modèle, et,',
     ['4.46', '4.96']),
    # [4.96 b] FIN-02 : table de prix versionnée
    ('sans extrapoler les baisses passées. Les exigences',
     'sans extrapoler les baisses passées. La passerelle de modèles <strong>DOIT</strong> tenir une table de prix versionnée et datée, avec une règle de conversion en dollars canadiens (source et date du taux). Les exigences',
     ['4.96']),
    # ---------------------------------------------------------------- § 10.6
    # [4.48, 4.99 k] enveloppe : dimensions, état tenu en un point
    ('<p>Chaque demande reçoit à son entrée une enveloppe de jetons, de coût, d’appels d’outils et de délai (figure 23).',
     '<p>Chaque tâche reçoit à son entrée une enveloppe aux dimensions de l’EXIG-ORC-26 : étapes ou itérations, appels d’outils, jetons, coût et durée totale (figure 23); pour un agent ambiant, la tâche naît de l’événement déclencheur.',
     ['4.48', '4.99']),
    ('Les plafonds se déclarent à la fiche (EXIG-ORC-26) et voyagent avec chaque appel (EXIG-ARC-02);',
     'Les plafonds se déclarent à la fiche (EXIG-ORC-26) et voyagent avec chaque appel (EXIG-ARC-02) à titre d’information, l’état qui fait foi étant tenu par la passerelle de modèles (EXIG-FIN-04);',
     ['4.48']),
    ('Un quota de passerelle est donc une borne approximative; l’enveloppe, une borne logique.</p>',
     'Un quota de passerelle est donc une borne approximative; l’enveloppe, tenue en un seul point avec réservation avant chaque appel, une borne logique.</p>',
     ['4.48']),
    # [4.99 i, 4.99 k, A-34] légende de la figure 23 (figure non modifiable)
    ('à 80 % d’un plafond, le propriétaire est alerté;',
     'à 80 % d’un plafond, le responsable technique est alerté;',
     ['4.99', 'A-34']),
    ('Les étapes simples vont au modèle compact, la planification au modèle de raisonnement. Source : cadre CRE-IA-2026-01; valeurs illustratives.</figcaption>',
     'Les étapes simples vont au modèle compact, la planification au modèle de raisonnement. Le schéma omet le plafond d’étapes ou d’itérations de l’EXIG-ORC-26, et l’alerte qu’il attribue au « propriétaire » va au responsable technique. Source : cadre CRE-IA-2026-01; valeurs illustratives.</figcaption>',
     ['4.99', 'A-34']),
    # [4.48, 4.16, 4.99 i, A-06, A-34] FIN-04 : détenteur unique, réservation, compensations
    ('<p>La passerelle de modèles et l’orchestrateur <strong>DOIVENT</strong> décrémenter l’enveloppe à chaque appel de modèle et d’outil, alerter le propriétaire dès qu’un plafond atteint 80 % et, à 100 %, arrêter l’exécution en état sûr et la passer en escalade, avec un refus typé « budget épuisé » (EXIG-IAM-18). Un orchestrateur qui délègue attribue à l’exécutant une part de l’enveloppe restante, jamais une enveloppe neuve.</p>\n'
     '<div id="pourquoi-1015"><p>Pourquoi : les conditions d’arrêt bornent le coût maximal<strong><sup>[404]</sup></strong>, et une enveloppe recréée à chaque délégation rendrait le plafond inopérant; les seuils de 80 et 100 % sont des choix du cadre.</p></div>',
     '<p>La passerelle de modèles <strong>DOIT</strong> être seule détentrice de l’état de l’enveloppe, côté serveur, indexé par l’identifiant de tâche; l’orchestrateur et la passerelle d’agents lui déclarent les appels d’outils. Chaque appel réserve atomiquement son coût maximal possible avant exécution, puis ajuste au coût réel; chaque part attribuée à un exécutant est débitée du parent dès son attribution. La passerelle alerte le responsable technique dès qu’un plafond atteint 80 % et, à 100 %, arrête l’exécution vers l’avant en état sûr et la passe en escalade, avec un refus typé « budget épuisé » (EXIG-IAM-18); les compensations des sagas en cours consomment la réserve du canal de compensation (EXIG-ORC-31), hors de l’enveloppe. Un orchestrateur qui délègue attribue à l’exécutant une part de l’enveloppe restante, jamais une enveloppe neuve; un partenaire externe est borné par un plafond contractuel.</p>\n'
     '<div id="pourquoi-1015"><p>Pourquoi : les conditions d’arrêt bornent le coût maximal<strong><sup>[404]</sup></strong>, et une enveloppe recréée à chaque délégation rendrait le plafond inopérant; un état tenu en un seul point, avec réservation, empêche que des sous-agents parallèles consomment chacun le même reste. Les seuils de 80 et 100 % sont des choix du cadre.</p></div>',
     ['4.48', '4.16', '4.99', 'A-06', 'A-34']),
    # [4.49, A-06] FIN-05 : alerte préalable; tâches en cours; plafond du repli
    ('À son plafond mensuel, l’agent est suspendu ou ramené à son modèle de repli, selon sa fiche, et le parrain en est avisé.</p>',
     'Le parrain est alerté à 80 % du plafond mensuel. À 100 %, les nouvelles tâches sont refusées, ou l’agent est ramené à son modèle de repli, selon sa fiche, et le parrain en est avisé; les tâches en cours se terminent ou se compensent (EXIG-ORC-31). Le modèle de repli dispose d’un plafond propre inscrit à la fiche, et le traitement de continuité de l’EXIG-FIN-03 s’applique.</p>',
     ['4.49', 'A-06']),
    # [4.96 c] un seul nom pour l’indicateur de cache
    ('Le taux de succès du cache se lit en rapportant',
     'La part des jetons d’entrée lus en cache se lit en rapportant',
     ['4.96']),
    # [4.47] FIN-06 : critère du coût par tâche réussie
    ('<p>Chaque étape d’un agent <strong>DOIT</strong> être servie par le plus petit modèle homologué qui atteint, pour cette étape, les seuils du jeu de référence.',
     '<p>La configuration modèle par étape retenue pour un agent <strong>DOIT</strong> atteindre les seuils d’agent du jeu de référence au plus faible coût par tâche réussie mesuré (EXIG-FIN-01), parmi les modèles homologués; un modèle plus petit qui échoue plus souvent peut coûter davantage par tâche réussie.',
     ['4.47']),
    # [4.96 b] rapport de prix illustratif
    ('<div id="pourquoi-1020"><p>Pourquoi : l’écart de prix atteint un facteur 100 chez un même fournisseur (Claude Fable 5.1 contre Claude Haiku 5.5, pour des invites d’au plus 100 000 jetons; facteur 20 au-delà)',
     '<div id="pourquoi-1020"><p>Pourquoi : dans la grille d’octobre 2026, à titre illustratif, l’écart de prix atteint un facteur 100 chez un même fournisseur (Claude Fable 5.1 contre Claude Haiku 5.5, pour des invites d’au plus 100 000 jetons; facteur 20 au-delà, si le prix de Claude Fable 5.1 ne varie pas avec la longueur de l’invite)',
     ['4.96']),
    # [4.96 c-d] FIN-07 : outils chargés à la demande; indicateur et seuil
    ('<strong>DOIT</strong> se modifier par une version déployée, jamais à la volée. Le taux de lecture en cache est suivi par agent, et une baisse marquée ouvre une analyse.</p>',
     '<strong>DOIT</strong> se modifier par une version déployée; l’ajout en fin de préfixe d’un outil versionné au catalogue est permis, et une définition modifiée reçue à l’exécution est refusée par la passerelle (EXIG-MCP-20). La part des jetons d’entrée lus en cache est suivie par agent, selon une formule tenue par fournisseur, et une baisse de plus de 20 points sur 7 jours (choix du cadre) ouvre une analyse.</p>',
     ['4.96']),
    # [4.46] coût total
    ('<li><strong>Coût par tâche réussie</strong> : coût total imputé à l’agent (inférence, outils, quote-part de la plateforme) divisé',
     '<li><strong>Coût par tâche réussie</strong> : coût total imputé à l’agent (inférence, outils, quote-part de la plateforme, évaluation par les juges et revue humaine, temps d’approbation et de garde imputé) divisé',
     ['4.46']),
    # [4.50, 4.51] FIN-09 : propagation et répartition du centre de coûts
    ('tiré du référentiel financier et identique à l’étiquette des données de facturation. La dépense agentique est suivie comme un périmètre de dépenses FinOps <em>(Scope)</em> distinct, avec ses responsables.',
     'tiré du référentiel financier et identique à l’étiquette des données de facturation. Le centre de coûts du mandant ou de la tâche d’origine se propage par le bagage (EXIG-OBS-10), et un service appelé ne le remplace pas; un service partagé déclare une clé de répartition. Lorsque les données de facturation d’un fournisseur ne descendent pas sous le compte ou la clé d’API, l’entreprise ouvre une clé ou un espace de travail par centre de coûts, ou répartit la facture d’après la télémétrie. La dépense agentique est suivie comme un périmètre de dépenses FinOps <em>(Scope)</em> distinct, dont l’équipe FinOps et les parrains sont responsables.',
     ['4.50', '4.51']),
    # [4.99 h, 4.51] FIN-10 : revue de valeur définie
    ('deux mois de suite (choix du cadre) passe en revue de valeur (section 11.5).</p>',
     'deux mois de suite (choix du cadre) passe en revue de valeur : le parrain, le responsable technique et l’équipe FinOps décident, devant la fonction risques et conformité, de maintenir, de reconcevoir ou de retirer l’agent, et la décision est consignée au registre (section 11.5).</p>',
     ['4.99', '4.51']),
]

# Passages d’origine qui contiennent une espace ordinaire avant « : » (exceptions à fr())
_BRUT = [
    # titre de section : note de renvoi fondue dans le titre (édition d’origine)
    ('<h3>Statut des versions : voir la section 10.1. 10.2 Contenu des invites et des réponses</h3>\n'
     '<p>Cette section règle le cas le plus délicat de la télémétrie : le texte des invites, des réponses et des arguments d’outils, utile au diagnostic mais souvent chargé de renseignements personnels (RP).</p>',
     '<h3>10.2 Contenu des invites et des réponses</h3>\n'
     '<p>Cette section règle le cas le plus délicat de la télémétrie : le texte des invites, des réponses et des arguments d’outils, utile au diagnostic mais souvent chargé de renseignements personnels (RP). Le statut des versions des conventions citées est celui de la section 10.1.</p>',
     []),
]


def _brut(ancien):
    """fr() sauf sur l’espace ordinaire du titre fautif."""
    tete, _, reste = ancien.partition('\n')
    return tete + '\n' + fr(reste)


CORRECTIONS = [(fr(a), fr(n), c) for a, n, c in _C] + [(_brut(a), fr(n), c) for a, n, c in _BRUT]

JOURNAL = [
    # § 9.1
    ('§ 9.1, EXIG-IAM-01', 'Force rendue explicite (DOIT) et portée limitée à la communication réseau; le transport stdio local renvoie à l’EXIG-MCP-08.', ['3.78']),
    ('§ 9.1, EXIG-IAM-02', 'Les appels de modèle entrent dans la décision par appel; l’état de la tâche est tenu dans un magasin à cohérence forte partagé par les instances, et un état illisible impose le refus.', ['3.76', '3.41', 'A-17']),
    ('§ 9.1, EXEMPLE de l’EXIG-IAM-02', 'Exemple remplacé par une écriture P2 sous le seuil, que seule la décision par appel soumet à approbation après une lecture non fiable.', ['3.77']),
    # § 9.2
    ('§ 9.2, brouillons WIMSE', 'Révisions postérieures signalées : AIMS -01 du 2 novembre 2026 (passages cités tirés de la -00), Workload Identity Practices -08 en dernier appel IETF.', ['A-31']),
    ('§ 9.2, Microsoft Entra Agent ID', 'Gabarit qualifié de justificatif partagé encadré par l’EXIG-IAM-04; rôles owner et manager mentionnés.', ['3.80', 'A-34']),
    ('§ 9.2, EXIG-IAM-04', 'Réémission à la demande admise (JWT-SVID); un justificatif commun à plusieurs identités doit être fédéré ou géré, sans secret client, et le profil de plateforme définit l’instance.', ['3.79', '3.80']),
    ('§ 9.2, EXIG-IAM-06', 'Circulation des jetons fixée : en-têtes du transport, jamais dans un message logique, un point de contrôle, le journal de compensation ni une trace; jeton d’approbation conservé par la passerelle.', ['3.18', 'A-15']),
    ('§ 9.2, EXIG-IAM-07', 'Attestation et agents orphelins renvoyés à l’EXIG-GOV-13 (source unique); le retrait ne révoque pas l’identité de compensation (EXIG-ORC-31).', ['3.81', '3.02', 'A-05', 'A-06']),
    ('§ 9.2, tableau 34, NHI3', 'Couverture déclarée partielle; absence d’inventaire des octrois accordés aux tiers signalée.', ['3.82', '4.66']),
    # § 9.3
    ('§ 9.3, résumé de la RFC 8693', 'grant_type et subject_token_type ajoutés aux paramètres obligatoires.', ['4.53']),
    ('§ 9.3, figure 17 (légende)', 'Figure non modifiable : la légende précise le second jeton obtenu par la passerelle, la distinction serveur MCP / système cible et la nature d’extrait du jeton (« SVID » = JWT-SVID en actor_token).', ['4.55', '4.06', 'A-16']),
    ('§ 9.3, extrait du jeton après deux sauts', 'Extrait remplacé par le jeton que la passerelle obtient pour le serveur (client_id de la passerelle), avec la portée de la tâche dans authorization_details; chaîne agent → passerelle → serveur décrite.', ['A-16', '4.03', '4.10']),
    ('§ 9.3, EXIG-IAM-08', 'Le serveur d’autorisation borne exp au subject_token, impose une durée maximale de chaîne et vérifie aud et cnf du subject_token; la profondeur ne compte que les agents; variante de fournisseur définie par le « même résultat ».', ['4.05', '4.06', '4.09', 'A-16']),
    ('§ 9.3, EXIG-IAM-09', 'L’interdiction vise la présentation du jeton d’une personne à un service autre que le serveur d’autorisation.', ['4.54']),
    ('§ 9.3, droits effectifs (exemple d’Alice)', 'La portée de la tâche est portée par authorization_details; serveur d’autorisation et serveur de ressources se répartissent l’intersection; demande incrémentale remontée au mandant.', ['4.03', '4.04', 'A-16']),
    ('§ 9.3, EXIG-IAM-10', 'Portée de la tâche obligatoirement représentée dans le jeton; non-élargissement défini par la liste des portées en aval, changement d’audience permis; demande incrémentale approuvée par le mandant, réémission de la chaîne, plafond de trois tentatives; macarons écartés.', ['4.03', '4.04', 'A-16']),
    ('§ 9.3, EXIG-IAM-11', 'Variante de fournisseur admise comme à l’EXIG-IAM-08; décision fondée sur les revendications de premier niveau et l’acteur courant; jeton présenté au serveur obtenu par la passerelle.', ['4.09', '4.52', 'A-16']),
    ('§ 9.3, profil OAuth et tableaux 35 et 36', 'OAuth 2.1 -17, ID-JAG -06 et SPIFFE client auth -03 signalés comme révisions postérieures; PKCE exigé de tous les clients; état IETF des Transaction Tokens traduit « en attente de la fiche de synthèse »; liaison mTLS vérifiée à la passerelle.', ['4.99', '4.56', '4.59', '4.10', 'A-31']),
    ('§ 9.3, EXIG-IAM-13', 'Clients OAuth (hôtes et agents) ajoutés aux sujets; décompte « deux points » remplacé par trois choix du cadre nommés.', ['4.56']),
    ('§ 9.3, EXIG-IAM-14', 'Liaison obligatoire étendue aux outils P1 sur RP; vérification de cnf à la passerelle qui termine TLS, réémission d’un jeton lié à la passerelle, serveur n’acceptant que la passerelle par mTLS.', ['4.10', '4.57', 'A-16']),
    ('§ 9.3, EXIG-IAM-15', 'Force modifiée : DOIT (annexe D à mettre à jour). Durée des jetons bornée par la cible du coupe-circuit pour les systèmes sans SSF ni CAEP; mandat d’agent ambiant inscrit au serveur d’autorisation, sans jeton de personne stocké, révoqué au départ du mandant.', ['4.08', '4.15', 'A-05', 'A-16']),
    ('§ 9.3, EXIG-IAM-16', 'Chaîne d’agents autonomes : l’initiateur tient lieu de mandant; renvoi à l’EXIG-IAM-09.', ['4.07', '4.58']),
    # § 9.4
    ('§ 9.4, introduction', 'Les trois points d’application (passerelle d’agents, passerelle de modèles, courtier d’événements) sont nommés.', ['A-01', 'A-02']),
    ('§ 9.4, figure 18 (légende) et liste des contrôles', 'Figure non modifiable : la légende et la liste précisent l’intention d’audit écrite avant le relais, le contrôle 5 calculé selon l’EXIG-AUT-10 (écritures N2 comprises), le contrôle 7 conditionnel, la vérification de cnf, l’ordre de la limitation de débit et le filtre de retour sans effet sur l’action.', ['4.11', '4.14', '4.61', '4.62', '4.10', 'A-10', 'A-14', 'A-19']),
    ('§ 9.4, EXIG-IAM-17', 'Portée unique : tout appel MCP et A2A quel que soit le domaine, tout accès interdomaine et toute action P2 ou P3; seule une fonction locale P0-P1 s’en dispense; instance en sidecar admise.', ['4.60', '3.28', '4.11', 'A-01']),
    ('§ 9.4, EXIG-IAM-18', 'Politique en cache valable tant qu’elle n’est pas échue; refus typés par familles, détail à l’audit, rafale de refus comme signal de risque; compensations par le canal de compensation.', ['4.12', '4.63', '3.29', 'A-04', 'A-06']),
    ('§ 9.4, sept portes', 'Présentées comme grille informative, non comme critères normatifs; troisième porte bornée par l’EXIG-IAM-22.', ['4.64', 'A-04']),
    ('§ 9.4, EXIG-IAM-19', 'Force modifiée : DOIT (annexe D à mettre à jour); le cas obligatoire est énoncé en tête et le cas général reste un DEVRAIT. L’exigence n’est pas scindée, faute d’identifiant attribué.', ['4.11']),
    ('§ 9.4, coupe-circuit', 'Phrase sans verbe principal corrigée (SSF et CAEP).', ['4.65']),
    ('§ 9.4, EXIG-IAM-20', 'Source unique du coupe-circuit : arrêt vers l’avant par le canal de suspension, compensation hors de portée, systèmes sans SSF ni CAEP inscrits et bornés, délai mesuré jusqu’au dernier refus, cible proposée à 15 minutes, exercice unique à l’EXIG-SEC-26.', ['4.15', '4.16', '4.99', '3.54', 'A-04', 'A-05', 'A-06']),
    ('§ 9.4, encadré sur la latence', 'La latence des garde-fous (contrôles 4 et 8) entre dans la mesure.', ['4.99']),
    ('§ 9.4, EXIG-IAM-22', 'Nouvelle exigence : objectif de disponibilité et redondance des composants obligatoires, durée de validité des politiques en cache (P0 seul une fois échue), refus sur état dynamique illisible, liste de suspension par canal signé indépendant.', ['4.12', '4.13', 'A-04']),
    # § 9.5
    ('§ 9.5, correspondance NHI vers ASI', 'Correspondance non vérifiée à la source retirée; renvoi au tableau 34.', ['4.71']),
    ('§ 9.5, EXIG-SEC-01 et EXIG-SEC-02', 'Déclencheurs de révision renvoyés à l’EXIG-GOV-12; matrice mise à jour pour T1-T17, à chaque révision du cadre et au moins tous les six mois pour ATLAS.', ['4.99', 'A-24']),
    ('§ 9.5, tableau 38', 'Renvois d’ASI03 (EXIG-IAM-08 à 16) et d’ASI10 (EXIG-ORC-26, EXIG-IAM-20, section 10.4) précisés.', ['4.66']),
    # § 9.6
    ('§ 9.6, EXIG-SEC-03', 'Toute source de contexte inscrite avec son étiquette (non inscrite = non fiable); seule la demande saisie par le mandant est fiable; cartes et définitions traitées de la même façon; étiquetage des saisies libres déclaré.', ['4.01', '4.19', '4.72', 'A-17']),
    ('§ 9.6, figure 19 (légende)', 'Figure non modifiable : la légende aligne « supervision humaine » et [B] sur l’EXIG-SEC-04.', ['4.69']),
    ('§ 9.6, EXIG-SEC-04', 'Règle de deux évaluée sur la session composée (tâche racine et dérivées), étiquettes propagées avec les données, [B] étendu à l’écriture et aux données reçues d’un pair, contexte vierge défini, plafond des écritures P2, charge d’approbation estimée.', ['4.01', '4.17', '4.18', '4.21', 'A-17']),
    ('§ 9.6, EXIG-SEC-05', 'Critère d’acceptation ajouté (seuil de l’EXIG-SEC-24).', ['4.68']),
    ('§ 9.6, EXIG-SEC-05 et EXIG-SEC-14 (en-têtes)', 'Non retenu en partie : l’en-tête garde la force principale, selon la convention du document; seul le critère d’acceptation de l’EXIG-SEC-05 est ajouté.', ['4.68']),
    ('§ 9.6, « Retirer », exemple et EXIG-SEC-06', 'Retrait défini comme retrait de l’exécution autonome (chaque appel exige une approbation); outil d’envoi défini, autres agents et recherche P0 compris; arguments de lecture contraints; liste d’autorisation appliquée en tout temps.', ['4.01', '4.20', '4.67', 'A-17']),
    ('§ 9.6, tableau 39 et EXIG-SEC-07', 'Limite du plan puis exécution sur les arguments signalée; pour la classe élevée, confinement des données ou validation des arguments sensibles exigé.', ['4.22']),
    ('§ 9.6, CaMeL', 'Version v2 de l’article citée; coût limité au banc d’essai; garantie bornée aux flux de contrôle et de données.', ['4.70']),
    ('§ 9.6, « Approuver »', 'Empreinte de l’action exacte (outil, définition, appelant, arguments) et jeton conservé par la passerelle.', ['A-10', 'A-11']),
    # § 9.7
    ('§ 9.7, choix de l’isolation et EXIG-SEC-08', 'MicroVM par défaut, gVisor et WASI sur justification, Wasm hors du processus de l’agent; le Pourquoi ne prête plus à gVisor et WASI la résistance à une faille du noyau.', ['4.23']),
    ('§ 9.7, EXIG-SEC-09', 'Aucune réutilisation; régénération de l’entropie après restauration d’instantané; réserve du gel des preuves.', ['4.73', 'A-18']),
    ('§ 9.7, EXIG-SEC-10', 'Délai de correctif des pilotes, passage direct de GPU (IOMMU, remise à zéro) et acceptation nommée de la garantie affaiblie.', ['4.79']),
    ('§ 9.7, EXIG-SEC-12', 'Règle de sortie réseau unique : refus par défaut, liste unique avec l’EXIG-SEC-06, refus du domain fronting, services multilocataires restreints, résolution unique et plages IANA à usage spécial, redirections revalidées, cibles internes par le catalogue.', ['4.24', '4.74', 'A-33']),
    ('§ 9.7, EXIG-SEC-13', 'Limite de sauts IMDSv2 exigée au lieu d’être présumée par défaut.', ['4.75']),
    ('§ 9.7, EXIG-SEC-14', 'Jeton éphémère borné (audience, portée, durée), vérification de la méthode et du chemin, P2-P3 par la passerelle; repli pour les protocoles autres que HTTP; Pourquoi rectifié.', ['4.25', '4.76']),
    ('§ 9.7, EXIG-SEC-15', 'Boucle de tâche définie; attente d’approbation hors bac à sable; la plus courte des bornes s’applique.', ['4.78']),
    ('§ 9.7, EXIG-SEC-16', 'Distinction entre observation externe et agent d’invité en lecture seule; minimisation et conservation.', ['4.26']),
    ('§ 9.7, EXIG-SEC-17', 'Aucune approbation à l’exécution de privilèges ou de destinations hors fiche; porte d’appoint fondée sur une liste d’autorisation; critères de surveillance minimaux.', ['4.27', '4.77']),
    # § 9.8
    ('§ 9.8, EXIG-SEC-18', 'Empreinte définie par type de composant (RFC 8785 pour un outil MCP), version servie pour un modèle hébergé; suspension de l’outil ou du serveur entier selon l’écart; limite de l’épinglage (comportement, valeurs de retour) dite.', ['4.28', '4.29', '4.80', 'A-21']),
    ('§ 9.8, signature et nomenclature', 'Intégrité limitée à la définition; risque résiduel des serveurs distants de tiers nommé.', ['4.29']),
    ('§ 9.8, EXIG-SEC-19', 'Clé liée à l’éditeur (catalogue ou kid/jku vérifiés).', ['4.30']),
    ('§ 9.8, EXIG-SEC-20 et EXIG-SEC-23', 'Agents N3-N4 et agents exposés au contenu non fiable soumis à la nomenclature et à l’équipe rouge.', ['4.32']),
    ('§ 9.8, EXIG-SEC-21', 'Catalogue pour les serveurs et agents distants, registre pour les agents internes.', ['4.81']),
    ('§ 9.8, EXIG-SEC-22', 'Proportionnalité définie pour les modèles et agents; accord écrit limité au fournisseur d’un système à haut risque, avec l’exception de l’art. 25(4).', ['4.31', '4.82']),
    # § 9.9
    ('§ 9.9, EXIG-SEC-23', 'Pilote sur données réelles traité comme mise en production; échelle de gravité définie; constat critique en production : suspension ciblée ou dérogation sous 5 jours ouvrables.', ['4.33', 'A-25', 'A-32']),
    ('§ 9.9, EXIG-SEC-24', 'Déclencheurs de l’EXIG-GOV-12; seuil fixé par la fonction risques et conformité, décidé selon l’EXIG-EVA-03; attaques adaptatives; suite renouvelée; composante adverse de l’étage E2.', ['4.34', '4.83', '4.99', 'A-24', 'A-32']),
    ('§ 9.9, EXIG-SEC-25', 'Cas négatifs ajoutés : décomposition multiagent, mémoire empoisonnée, représentation de la même opération, carte et clés, portée et audience, prolongation de délégation, plages IPv6, valeur de retour piégée, mode fermé.', ['4.01', '4.05', '4.29', '4.30', '4.84', 'A-10']),
    ('§ 9.9, EXIG-SEC-26', 'Exercice unique du coupe-circuit, en production sur un agent témoin, avec compensations et panne de passerelle; délai mesuré selon l’EXIG-IAM-20 et comparé à la cible fixée par l’entreprise.', ['4.15', '4.16', '4.99', 'A-05', 'A-06']),
    ('§ 9.4 et § 9.9, appels de citation du RIA et de MANAGE 2.4', 'Non retenu en partie : les appels [61]/[290] et [74]/[99] sont conservés, les numéros de références étant intouchables; les doublons relèvent de l’annexe G.', ['4.99']),
    # § 10.1
    ('Chapitre 10, chapeau', 'Journal « chaîné et ancré » au lieu d’« inaltérable »; étages d’évaluation E1 à E3.', ['A-19', 'A-27']),
    ('§ 10.1, EXIG-OBS-01', 'Conformité mesurée à la sortie du collecteur, après correspondance vers la ligne v1.41 (v1.41.0, correctif v1.41.1 admis après vérification); version émise consignée par composant; composants de tiers couverts par la passerelle et par contrat; courtier ajouté.', ['4.02', '4.35', '4.99', 'A-02', 'A-29']),
    ('§ 10.1, EXIG-OBS-02', 'Composant interne défini par son identité de charge de travail inscrite au registre.', ['4.85']),
    ('§ 10.1, figure 21 (légende) et EXIG-OBS-04', 'Figure non modifiable : attente d’approbation représentée par deux événements reliés par un lien de span; span MCP CLIENT pour les seuls outils MCP.', ['4.36', '4.86']),
    ('§ 10.1, EXIG-OBS-05', 'Attributs exigés après correspondance; alerte mesurée avant échantillonnage; échantillonnage en queue qui conserve toutes les traces marquées.', ['4.02', '4.40', 'A-29']),
    ('§ 10.1, tableau 41 et EXIG-OBS-06', 'Approbateur retiré des spans (identifiant du jeton d’approbation comme clé de jonction), consigné au seul journal d’audit.', ['4.87']),
    # § 10.2
    ('§ 10.2, titre', 'Titre rétabli : la note « Statut des versions : voir la section 10.1 », fondue dans le titre de l’édition d’origine, passe dans le paragraphe d’ouverture.', []),
    ('§ 10.2, modes, À RETENIR et EXIG-OBS-07', 'Interdit étendu aux messages d’exception, descriptions de statut, noms de spans et bagage; renvoi aux magasins propres (débogage, dossier de décision, évaluation, incident).', ['4.37', '4.41', 'A-18']),
    ('§ 10.2, EXIG-OBS-08', 'Attribut de référence nommé; réserve du gel des preuves; capture exclue de l’évaluation et du dossier de décision.', ['4.88', 'A-18']),
    ('§ 10.2, EXIG-OBS-09', 'Exceptions caviardées; essai de non-fuite par type de signal; solution de rechange au processeur redaction en Alpha.', ['4.89', '4.37']),
    ('§ 10.2, EXIG-OBS-10', 'Filtre du bagage étendu au collecteur et aux SDK; traitement de tracestate aux frontières.', ['4.90']),
    # § 10.3
    ('§ 10.3, présentation du journal et cinq éléments', 'Lectures sensibles couvertes; journal chaîné et ancré; empreinte de la définition, contrôle, version de politique, séquence et précédent.', ['4.38', '4.91', 'A-11', 'A-12', 'A-19']),
    ('§ 10.3, extrait d’enregistrement', 'Extrait aligné sur l’annexe C.8 : enveloppe empreinte / enregistrement / signature, séquence, empreinte de la définition, empreinte d’approbation, contrôle et version de politique.', ['4.91']),
    ('§ 10.3, EXIG-OBS-11', 'Enregistrement d’intention avant le relais d’un P2 ou P3; lectures P1 de RP auditées; service d’audit ajouté aux dépendances de l’EXIG-AUT-11.', ['4.14', '4.38', 'A-10', 'A-19']),
    ('§ 10.3, EXIG-OBS-12', 'Flux défini, points de contrôle horaires publiés hors du domaine d’administration, empreinte d’enregistrement définie, arguments à faible entropie salés ou par HMAC, h renvoyé à l’EXIG-AUT-12; Pourquoi rectifié (troncature, portée de h).', ['4.39', '4.92', 'A-11', 'A-19']),
    ('§ 10.3, EXIG-OBS-13', 'Vérification contre les points de contrôle; purge par segments clos, anonymisation par la table des pseudonymes, clés de vérification conservées, réserve du gel.', ['4.39', 'A-19']),
    ('§ 10.3, EXIG-OBS-14', 'Nouvelle exigence : dossier de décision chiffré pour les décisions visées par l’art. 12.1 de la Loi sur le privé ou l’art. 65.2 de la Loi sur l’accès, relié à l’audit par empreinte, conservé au moins un an.', ['4.41', 'A-18']),
    # § 10.4
    ('§ 10.4, figure 22 (légende) et paliers d’évaluation', 'Figure non modifiable : « paliers » d’évaluation renommés « étages E1 à E3 » dans le texte; déclencheurs renvoyés à l’EXIG-GOV-12; « plafond atteint » ajouté en légende; titre de l’EXIG-EVA-01 conservé (annexe D).', ['A-27', '4.93', '4.99', 'A-24']),
    ('§ 10.4, étage E1', 'Injection de fautes « suspension ou épuisement en cours de saga » ajoutée.', ['4.16']),
    ('§ 10.4, tableau 42', 'Refus de politique exclus du succès technique; violation définie; règle statistique; seuil des approbations sans modification; coût total et valeur attendue à défaut de processus de référence.', ['4.95', '4.46', 'A-32']),
    ('§ 10.4, EXIG-EVA-01', 'Réévaluation avant la mise en service; la passerelle ne résout pas un alias vers une cible non évaluée ni vers un alias flottant du fournisseur.', ['4.42', '4.99', 'A-24']),
    ('§ 10.4, EXIG-EVA-02', 'Jeu d’au moins 50 scénarios, stratifié, avec sous-ensemble réservé et registre de régression non plafonné, alimenté par le dépôt d’évaluation.', ['4.43', 'A-18', 'A-32']),
    ('§ 10.4, EXIG-EVA-03', 'Règle de décision statistique pour toute porte et toute comparaison (borne supérieure à 95 %, au moins 3/p essais indépendants).', ['4.34', 'A-32']),
    ('§ 10.4, EXIG-EVA-04', 'Échantillon d’au moins 5 % des exécutions avec plancher absolu; taux sur la strate aléatoire; contenu tiré du dépôt d’évaluation; repli de rattachement par gen_ai.response.id dans l’énoncé.', ['4.40', '4.41', '4.34', '4.93', 'A-18', 'A-32']),
    ('§ 10.4, EXIG-EVA-05', 'Juge d’un autre modèle de préférence, accord mesuré à défaut; seuil d’accord au contrat, en deçà duquel le juge n’alimente plus les indicateurs.', ['4.44', '4.94']),
    ('§ 10.4, EXIG-EVA-06', 'Période définie (mois civil); fonction risques et conformité consultée, comité pour la classe élevée et N4, escalade après trois mois; renvoi à l’EXIG-FIN-10 pour l’économie unitaire.', ['4.45', '4.99']),
    ('§ 10.4, EXIG-EVA-07', 'Nouvelle exigence : dépôt d’évaluation caviardé, chiffré, à finalité déclarée et rétention bornée, seule source du contenu évalué et des scénarios tirés de la production.', ['4.41', 'A-18']),
    # § 10.5-10.6
    ('§ 10.5, résidence', 'Zone hors du Québec renvoyée à l’art. 17.', ['4.99', 'A-28']),
    ('§ 10.5, EXIG-FIN-01 et EXIG-FIN-02', 'Indicateur de sélection pondéré et distinct du coût total suivi en production; normalisation étendue au ratio jetons/résultat; table de prix versionnée et datée.', ['4.46', '4.96']),
    ('§ 10.6, enveloppe et figure 23 (légende)', 'Figure non modifiable : cinq dimensions de l’EXIG-ORC-26, état tenu par la passerelle de modèles, alerte au responsable technique et non au « propriétaire ».', ['4.48', '4.99', 'A-34']),
    ('§ 10.6, EXIG-FIN-04', 'Détenteur unique de l’enveloppe, réservation atomique, parts débitées au parent, compensations hors enveloppe, plafond contractuel des partenaires; « propriétaire » remplacé.', ['4.48', '4.16', '4.99', 'A-06', 'A-34']),
    ('§ 10.6, EXIG-FIN-05', 'Alerte à 80 % du plafond mensuel; nouvelles tâches refusées à 100 %, tâches en cours terminées ou compensées; plafond propre du modèle de repli.', ['4.49', 'A-06']),
    ('§ 10.6, EXIG-FIN-06', 'Critère du coût par tâche réussie au lieu du « plus petit modèle » par étape (titre conservé); rapport de prix marqué illustratif et conditionnel.', ['4.47', '4.96']),
    ('§ 10.6, EXIG-FIN-07 et indicateur de cache', 'Un seul nom d’indicateur, formule par fournisseur, seuil chiffré; ajout d’outils versionnés en fin de préfixe permis.', ['4.96']),
    ('§ 10.6, indicateurs et EXIG-FIN-09', 'Coût total élargi (évaluation, approbation, garde); centre de coûts propagé et réparti pour les services partagés.', ['4.46', '4.50']),
    ('§ 10.6, EXIG-FIN-09 et EXIG-FIN-10', 'Équipe FinOps désignée comme responsable du périmètre et participante de la revue de valeur, désormais définie; son ajout aux tableaux 43 et 44 relève des § 11.1-11.2.', ['4.51', '4.99', 'A-34']),
    # hors tranche ou non retenus
    ('§ 9.4, encadré sur la latence (unification)', 'Non retenu dans cette tranche : l’encadré de la section 9.4, seul à préciser les 512 connexions, est conservé; sa fusion avec les versions des sections 5.4 et 13.2 relève des tranches qui les portent.', ['4.99']),
    ('§ 6.7, EXIG-EVT-10 (rétention des traces)', 'Non retenu dans cette tranche : le renvoi de l’EXIG-EVT-10 relève du chapitre 6; le § 10.3 renvoie déjà à la fiche.', ['4.99']),
    ('Annexe G, doublons de références', 'Non retenu dans cette tranche : le dédoublonnage relève de l’annexe G.', ['4.99']),
    ('Tableau 61, couverture des passerelles', 'Non retenu dans cette tranche : l’indicateur relève du chapitre 15; la portée qu’il doit compter est fixée par l’EXIG-IAM-17 corrigée.', ['4.99']),
]
