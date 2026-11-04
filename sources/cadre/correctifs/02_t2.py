"""Correctifs de la revue du 3 novembre 2026 — tranche : § 6.4 à 6.9 (MCP, A2A, événementiel, contrats, veille) et § 7.1-7.2."""
NBSP = '\xa0'


def T(s):
    """Typographie du corps : insécable avant le deux-points et le pour-cent, et dans les guillemets."""
    return (s.replace(' :', NBSP + ':').replace(' %', NBSP + '%')
             .replace('« ', '«' + NBSP).replace(' »', NBSP + '»'))


def C(ancien, nouveau, constats):
    return (T(ancien), T(nouveau), constats)


CORRECTIONS = [
    # ---------------------------------------------------------------- § 6.4
    # [2.54, 2.53] Tasks au stade Beta; interrogation à l'intervalle annoncé, avec plancher
    C('<td>MCP avec l’extension officielle Tasks, si elle est inscrite au catalogue<strong><sup>[191]</sup></strong></td><td>Asynchrone, par interrogation</td>',
      '<td>MCP avec l’extension officielle Tasks (stade Beta), si elle est inscrite au catalogue<strong><sup>[191]</sup></strong></td><td>Asynchrone, par interrogation à l’intervalle annoncé par le serveur, avec un plancher inscrit au catalogue et un quota de tâches par mandant (EXIG-MCP-04)</td>',
      ['06-12', '06-33']),
    # [2.37] adaptateur de composition orienté tâche
    C('<td>Contrat OpenAPI exposé en outils MCP par un adaptateur</td>',
      '<td>Contrat OpenAPI exposé en outils MCP par un adaptateur de composition orienté tâche (EXIG-MCP-06)</td>',
      ['06-08']),
    # [2.13] A-21 : le flux SSE structuré est un patron interne au statut Adopter
    C('<td>AG-UI (Évaluer) ou flux SSE structuré</td>',
      '<td>Flux SSE structuré produit par l’orchestrateur, à schéma d’événements versionné au catalogue d’entreprise (patron interne, statut Adopter, section 6.3); AG-UI en pilote seulement (statut Évaluer)</td>',
      ['06-11']),
    # [2.36] questions non exclusives, qui préparent la soumission d'EXIG-INT-10; A-20 pour la question 3
    C('<p>Lorsqu’un cas ne figure pas dans la matrice, quatre questions, posées dans l’ordre, mènent au bon choix :</p>',
      '<p>Lorsqu’un cas ne figure pas dans la matrice, quatre questions qualifient chaque liaison et préparent la soumission exigée par l’EXIG-INT-10. Elles ne sont pas exclusives : une même cible peut relever de MCP pour ses outils et du bus pour ses changements d’état, si bien que la quatrième question se pose pour toute liaison.</p>',
      ['06-09', '06-31']),
    C('<li>La cible raisonne-t-elle, garde-t-elle un état, peut-elle demander une précision ou une autorisation? Si oui, A2A;',
      '<li>La cible choisit-elle elle-même, au moyen d’un modèle, les actions qu’elle exécute? Si oui, c’est un agent, et A2A (EXIG-A2A-01); une cible qui conserve l’état d’une tâche ou demande une précision sans choisir ses actions reste un outil (MCP, extension Tasks, élicitation);',
      ['06-09']),
    # [2.65] l'argument du nombre de liaisons ne distingue pas le bus de la passerelle
    C('<p>La quatrième question a une base arithmétique simple : relier N agents deux à deux exige jusqu’à N(N−1)/2 intégrations, contre N connexions vers un courtier. Le bus réduit le nombre de liaisons, pas la gouvernance des sujets, des schémas et des contrats, qui reste entière.</p>',
      '<p>La quatrième question repose sur le découplage logique, non sur le décompte des liaisons : relier N agents deux à deux exige jusqu’à N(N−1)/2 intégrations, mais la passerelle d’agents forme déjà une étoile à N connexions. Le bus apporte ce que la passerelle n’offre pas : le découplage dans le temps, des abonnés que l’émetteur ignore et le rejeu. La gouvernance des sujets, des schémas et des contrats reste entière.</p>',
      ['08-11']),

    # ---------------------------------------------------------------- § 6.5
    # [2.96] date de la prochaine révision MCP (SEP-3398), omission antérieure au 27 octobre
    C('La feuille de route publiée le 22 août 2026 n’annonce aucune date pour la prochaine révision.',
      'La feuille de route publiée le 22 août 2026 n’annonce aucune date pour la prochaine révision; la SEP-3398, acceptée le 14 octobre 2026 et versée au dépôt le 27 octobre, fixe deux publications par an et la reporte au 30 mars 2027, sous réserve du calendrier de transition (annexe H).',
      ['06-34']),
    # [2.01] A-01 : exception de la fonction locale P0-P1; outils hébergés par le fournisseur de modèles
    C('<p>Tout outil, toute ressource et toute invite mis à la disposition d’un agent <strong>DOIVENT</strong> l’être par un serveur MCP inscrit au catalogue d’entreprise et, dans tout environnement serveur, publié derrière la passerelle d’agents (sur un poste de développement, l’exécution locale par <code>stdio</code> obéit à l’EXIG-MCP-08).',
      '<p>Tout outil, toute ressource et toute invite mis à la disposition d’un agent <strong>DOIVENT</strong> l’être par un serveur MCP inscrit au catalogue d’entreprise et, dans tout environnement autre qu’un poste de développement individuel sans justificatif de production, publié derrière la passerelle d’agents, vers une version et une empreinte approuvées (sur ce poste, le serveur local obéit à l’EXIG-MCP-08). Seule en est dispensée la fonction locale de palier P0 ou P1 de l’EXIG-ARC-01, exécutée dans l’unité de déploiement de l’agent, sur les données de son propre domaine et inscrite au catalogue avec son palier; une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Un outil hébergé par le fournisseur de modèles n’est admis qu’au palier P0.',
      ['06-01']),
    # [2.45] server/discover réservé aux serveurs 2026-07-28; vérification périodique des tiers
    C('la passerelle la vérifie par <code>server/discover</code>, en contournant son propre cache (le résultat porte <code>ttlMs</code> et <code>cacheScope</code>), à l’homologation et à chaque déploiement, et refuse',
      'la passerelle la vérifie par <code>server/discover</code> pour un serveur 2026-07-28, et par la réponse à <code>initialize</code> pour un serveur antérieur inscrit avec sa date de migration (EXIG-MCP-22), en contournant son propre cache (le résultat porte <code>ttlMs</code> et <code>cacheScope</code>), à l’homologation, à chaque déploiement et, pour un serveur de tiers, périodiquement, au plus tard à l’échéance de <code>ttlMs</code>, et refuse',
      ['06-15']),
    # [2.50] l'identifiant non nul n'est pas une nouveauté de 2026-07-28; [2.07] un client par point d'accès
    C('En 2026-07-28, l’identifiant d’une requête ne peut pas être nul et tout résultat porte un champ <code>resultType</code> <strong><sup>[162]</sup></strong>.</p>',
      'Comme depuis la révision 2024-11-05, l’identifiant d’une requête ne peut pas être nul; en 2026-07-28, tout résultat porte en outre un champ <code>resultType</code> <strong><sup>[162]</sup></strong>.</p>',
      ['06-19']),
    # [2.15, 2.07] préfixage par l'identifiant de serveur au catalogue; un point d'accès virtuel est un serveur pour l'hôte
    C('Dans ce second cas, elle préfixe les noms d’outils par un identifiant de serveur : la spécification',
      'Pour l’hôte, un point d’accès virtuel est un serveur : il y crée un seul client. Dans tous les cas, elle préfixe les noms d’outils par l’identifiant de leur serveur au catalogue (EXIG-MCP-20) : la spécification',
      ['06-16', '06-17']),
    # [2.07, 2.54] légende de la figure 7 : client par point d'accès; EMA au statut Évaluer
    C('L’hôte crée un client par serveur; chaque requête, autonome et sans session, traverse la passerelle,',
      'L’hôte crée un client par point d’accès MCP (serveur publié ou point d’accès virtuel); chaque requête, autonome et sans session, traverse la passerelle,',
      ['06-17']),
    C('une requête complète porte aussi les capacités du client dans <code>_meta</code>. Source',
      'une requête complète porte aussi les capacités du client dans <code>_meta</code>. L’extension d’autorisation EMA qui y figure est au statut Évaluer : pilotes seulement (section 6.3). Le jeton présenté à la passerelle lui est destiné; elle en obtient un second pour le serveur de domaine (section 9.3). Source',
      ['06-02', '06-32']),
    # [2.07] A-16 : jeton à l'audience de la passerelle, second jeton pour le serveur de domaine
    C('Authorization: Bearer &lt;jeton émis pour ce serveur seulement&gt;',
      'Authorization: Bearer &lt;jeton émis pour ce point d’accès de la passerelle&gt;',
      ['06-02']),
    C('Le jeton n’est valable que pour ce serveur (EXIG-MCP-11).',
      'Le jeton n’est valable que pour ce point d’accès de la passerelle (EXIG-MCP-11), qui obtient pour le serveur de domaine un second jeton par échange de jetons (section 9.3).',
      ['06-02']),
    # [2.44] sessions persistantes : pendant la coexistence, les serveurs antérieurs en gardent
    C('<td>Plus de répartiteurs de charge à sessions persistantes <em>(sticky sessions)</em> ni de magasin de sessions partagé.',
      '<td>À terme, après la migration (EXIG-MCP-22), plus de répartiteurs de charge à sessions persistantes <em>(sticky sessions)</em> ni de magasin de sessions partagé; pendant la coexistence, l’affinité ou le magasin de sessions est limité aux serveurs antérieurs inscrits, dont les <code>Mcp-Session-Id</code> suivent les règles de l’EXIG-MCP-17.',
      ['06-14', '07-22']),
    # [2.05] A-10 : la relance MRTR garde la clé, compte pour une opération, ne consomme pas le jeton
    C('le <code>requestState</code> devient une entrée non fiable à protéger (EXIG-MCP-17).</td>',
      'le <code>requestState</code> devient une entrée non fiable à protéger (EXIG-MCP-17). La relance garde la clé d’idempotence et compte pour une seule opération au budget et à l’audit; un passage soldé par <code>input_required</code> ne consomme pas le jeton d’approbation (section 8.5).</td>',
      ['06-05', '07-06']),
    # [2.09] cache « private » : contexte d'autorisation, non jeton
    C('un cache « private » n’est jamais partagé entre jetons (EXIG-MCP-03).',
      'un cache « private » n’est jamais partagé entre contextes d’autorisation (EXIG-MCP-03).',
      ['06-04']),
    # A-22 et lit. 4 : retrait accéléré pour un risque de sécurité actif, non « exceptionnel »
    C('ou au moins 90 jours en cas de retrait accéléré exceptionnel',
      'ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée)',
      ['A-22', 'lit. 4']),
    # [2.48] fondement des retraits immédiats; [2.96] échéance calculable de HTTP+SSE
    C('<code>ping</code>, <code>logging/setLevel</code> et <code>notifications/roots/list_changed</code> sont retirés. Le retrait',
      '<code>ping</code>, <code>logging/setLevel</code> et <code>notifications/roots/list_changed</code> sont retirés directement, comme conséquences du passage sans état (SEP-2575) : la politique de cycle de vie, adoptée dans la même révision, ne vise pas ces retraits, et la journalisation protocolaire dépréciée n’a plus de réglage de niveau. Le retrait',
      ['06-20']),
    C('celui du transport HTTP+SSE, trois mois après que la SEP-2596 atteint l’état final)<strong><sup>[168, 196]</sup></strong>.</td>',
      'celui du transport HTTP+SSE, trois mois après que la SEP-2596 atteint l’état final, soit dès le début de septembre 2026, cette SEP étant finale depuis le 3 juin 2026 : annexe H)<strong><sup>[168, 196]</sup></strong>.</td>',
      ['06-34']),
    # [2.09, 2.51] EXIG-MCP-03 : contexte d'autorisation défini, invalidation, absence de cacheScope, ordre de la liste agrégée
    C('Les serveurs MCP internes <strong>DOIVENT</strong> renvoyer leurs outils dans un ordre déterministe, identique d’une requête à l’autre tant que l’ensemble ne change pas. La passerelle <strong>DOIT</strong> respecter <code>ttlMs</code> et <code>cacheScope</code> : sa clé de cache inclut la méthode et les paramètres de la requête (curseur, URI) et, pour une réponse « private », le contexte d’autorisation;',
      'Les serveurs MCP internes <strong>DOIVENT</strong> renvoyer leurs outils dans un ordre déterministe, identique d’une requête à l’autre tant que l’ensemble ne change pas; la passerelle qui agrège plusieurs serveurs fusionne leurs listes par identifiant de serveur, puis par nom, et conserve un ordre stable après filtrage. La passerelle <strong>DOIT</strong> respecter <code>ttlMs</code> et <code>cacheScope</code> : sa clé de cache inclut la méthode et les paramètres de la requête (curseur, URI) et, pour une réponse « private », le contexte d’autorisation, soit l’émetteur, le sujet, le client, l’audience et l’ensemble exact des portées du jeton;',
      ['06-04', '06-22']),
    C('le résultat d’une relance MRTR (<code>inputResponses</code> ou <code>requestState</code>) ne sont jamais mis en cache.</p>',
      'le résultat d’une relance MRTR (<code>inputResponses</code> ou <code>requestState</code>) ne sont jamais mis en cache. La passerelle <strong>DOIT</strong> évaluer la politique avant tout service depuis le cache, ne rien mettre en cache en l’absence de <code>cacheScope</code>, invalider les entrées d’un contexte à la révocation ou à la suspension de l’agent et à tout changement de portées et, à chaque rétablissement de <code>subscriptions/listen</code>, invalider les entrées du serveur et relire ses listes.</p>',
      ['06-04', '06-21']),
    # [2.06 c, 2.10] EXIG-MCP-04 : clé à la création de toute tâche; gabarits ui:// épinglés, CSP du catalogue
    C('Pour l’extension Tasks, la passerelle impose un quota de tâches actives par mandant et une durée de vie maximale. Pour MCP Apps, chaque gabarit <code>ui://</code> est revu avant l’homologation, servi sous une politique de sécurité du contenu restrictive, et le contenu généré qu’il affiche est encodé.</p>',
      'Pour l’extension Tasks, la passerelle impose un quota de tâches actives par mandant et une durée de vie maximale, et toute requête qui crée une tâche porte une clé d’idempotence, quel que soit le palier, afin qu’une panne survenue avant la consignation du <code>taskId</code> ne laisse pas de tâche orpheline (section 7.6). Pour MCP Apps, chaque gabarit <code>ui://</code> est revu avant l’homologation, l’empreinte de son contenu est épinglée au catalogue et vérifiée à chaque <code>resources/read</code> (un écart suspend le gabarit), et le contenu généré qu’il affiche est encodé; l’hôte applique la politique de sécurité du contenu et les permissions inscrites au catalogue, jamais celles de <code>_meta.ui</code>, que le serveur déclare.</p>',
      ['06-13', '06-06']),
    # [2.08] la ressource est déclarée sans effet par le serveur et classée au catalogue
    C('<code>crm://comptes/9482/sommaire</code> se lit sans effet sur le système et se met en cache selon <code>ttlMs</code>.',
      '<code>crm://comptes/9482/sommaire</code> est déclarée sans effet par le serveur, classée au catalogue comme une lecture (palier P0 ou P1) et se met en cache selon <code>ttlMs</code>.',
      ['06-03']),
    # [2.37] adaptateurs de composition qui valident les règles métier
    C('des adaptateurs déclaratifs traduisent les opérations OpenAPI pertinentes en outils orientés tâche (section 5.2).',
      'des adaptateurs de composition traduisent les opérations OpenAPI pertinentes en outils orientés tâche, qui valident les règles métier (section 5.2 et EXIG-MCP-06).',
      ['06-08']),
    # [2.08] EXIG-MCP-05 : palier des ressources, contrôles appliqués à resources/read, hôte sans lecture de ressources
    C('<p>La lecture d’une entité connue <strong>DEVRAIT</strong> être exposée comme ressource adressée par URI; une recherche, un calcul ou une écriture, comme outil; une procédure normalisée de domaine, comme invite versionnée et revue au même titre que du code.</p>',
      '<p>La lecture d’une entité connue <strong>DEVRAIT</strong> être exposée comme ressource adressée par URI; une recherche, un calcul ou une écriture, comme outil; une procédure normalisée de domaine, comme invite versionnée et revue au même titre que du code. Une ressource ou un gabarit de ressource reçoit au catalogue un palier P0 ou P1, comme un outil de lecture : la passerelle <strong>DOIT</strong> appliquer à <code>resources/read</code> les contrôles de ce palier, le masquage et le balisage du contenu non fiable (section 9.6). Lorsque l’hôte n’offre pas au modèle la lecture de ressources, un outil de lecture adossé à la ressource la remplace.</p>',
      ['06-03', '06-30']),
    C('Pourquoi : la ressource se lit sans effet et se met en cache;',
      'Pourquoi : la ressource, déclarée sans effet par le serveur et classée au catalogue, se met en cache, mais une lecture sensible reste une lecture sensible; la spécification laisse en outre à l’application hôte le choix des ressources qu’elle fournit au modèle;',
      ['06-03', '06-30']),
    # [2.37] EXIG-MCP-06 : critère de revue vérifiable
    C('Il expose des outils qui accomplissent des tâches métier complètes et valident eux-mêmes leurs paramètres.</p>',
      'Il expose des outils qui accomplissent des tâches métier complètes et valident eux-mêmes leurs paramètres. Critère de revue : aucun outil d’écriture dont le contrat se réduit à une opération unique de l’API, sans validation métier.</p>',
      ['06-08']),
    # [2.15, 2.52] EXIG-MCP-07 : longueur réservée au préfixe; résultat d'erreur; une seule forme transmise au modèle
    C('porter un nom de 1 à 128 caractères ASCII (lettres, chiffres, <code>_</code>, <code>-</code>, <code>.</code>) préfixé par leur domaine;',
      'porter un nom de 1 à 96 caractères ASCII (lettres, chiffres, <code>_</code>, <code>-</code>, <code>.</code>) préfixé par leur domaine, la marge jusqu’aux 128 caractères de la spécification étant réservée au préfixe de serveur que pose la passerelle (EXIG-MCP-20);',
      ['06-16']),
    C('puis renvoyer un <code>structuredContent</code> conforme, accompagné du même JSON sérialisé dans un bloc texte.</p>',
      'puis renvoyer un <code>structuredContent</code> conforme, accompagné du même JSON sérialisé dans un bloc texte. Un outil qui renvoie aussi des erreurs structurées les décrit dans son <code>outputSchema</code> (union du succès et de l’erreur), et l’hôte ne transmet au modèle qu’une des deux formes du résultat.</p>',
      ['06-23']),
    # [2.87] réassociation DNS
    C('pour contrer le détournement DNS,',
      'pour contrer les attaques par réassociation DNS <em>(DNS rebinding)</em>,',
      ['06-24']),
    # [2.11, 2.88] A-01 : EXIG-MCP-08, serveur local en Streamable HTTP encadré; TLS
    C('<p>Dans tout environnement serveur (développement partagé, préproduction, production), un serveur MCP <strong>DOIT</strong> être exposé par Streamable HTTP, chiffré par TLS 1.3 (TLS 1.2 toléré comme plancher, versions antérieures désactivées), derrière la passerelle d’agents. Le transport stdio n’est permis que sur le poste d’un développeur, pour un serveur installé depuis le catalogue et exécuté dans un bac à sable aux privilèges minimaux; l’hôte affiche la commande complète avant l’installation et exige une approbation explicite.</p>',
      '<p>Dans tout environnement autre qu’un poste de développement individuel sans justificatif de production (développement partagé, préproduction, production), un serveur MCP <strong>DOIT</strong> être exposé par Streamable HTTP, derrière la passerelle d’agents, sur TLS : TLS 1.3 négocié lorsque le pair le permet, TLS 1.2 au minimum, versions antérieures désactivées. Sur un tel poste, et là seulement, un serveur local est permis, installé depuis le catalogue et exécuté dans un bac à sable aux privilèges minimaux; l’hôte affiche la commande complète avant l’installation et exige une approbation explicite. Ce serveur local emploie stdio ou, en Streamable HTTP, <strong>DOIT</strong> n’écouter que sur l’adresse de bouclage, valider l’en-tête <code>Origin</code> et exiger une authentification.</p>',
      ['06-07', '06-25']),
    # [2.87] parenthèse en double; lit. 29 : la -17 a paru le 31 octobre
    C('fondée sur le brouillon OAuth 2.1 dans sa version -13 (la version -16 est la plus récente au 27 octobre 2026; voir la section 6.3), que la spécification MCP cite encore (la version -16 est la plus récente au 27 octobre 2026; voir la section 6.3)',
      'fondée sur le brouillon OAuth 2.1 dans sa version -13, que la spécification MCP cite encore (la version -16 était la plus récente au 27 octobre 2026, et la -17 a paru le 31 octobre 2026; voir la section 6.3)',
      ['06-26', 'lit. 29']),
    # [2.87, 2.89] DPoP au profil d'autorisation MCP; jetons liés à l'expéditeur
    C('et la finalisation de DPoP ne figure qu’à sa feuille de route<strong><sup>[195, 209]</sup></strong>. Les jetons contraints à l’émetteur (RFC 9449 ou RFC 8705)',
      'et l’intégration de DPoP (RFC 9449) au profil d’autorisation MCP ne figure qu’à sa feuille de route<strong><sup>[195, 209]</sup></strong>. Les jetons liés à l’expéditeur <em>(sender-constrained)</em> (RFC 9449 ou RFC 8705)',
      ['06-27', '06-28']),
    # [2.11, 2.12, 2.07] EXIG-MCP-09 : plus d'exemption implicite du poste pour HTTP; iss; portées en mode agrégé
    C('<p>Tout serveur MCP accessible ailleurs que sur un poste de développement <strong>DOIT</strong> exiger une autorisation OAuth conforme à la spécification MCP 2026-07-28 : métadonnées de ressource protégée (RFC 9728), indicateur de ressource (RFC 8707) portant l’URI canonique, vérification de l’audience à chaque requête et jeton transmis uniquement par l’en-tête <code>Authorization</code>.',
      '<p>Tout serveur MCP, hormis un serveur local en stdio sur un poste de développement (EXIG-MCP-08), <strong>DOIT</strong> exiger une autorisation OAuth conforme à la spécification MCP 2026-07-28 : métadonnées de ressource protégée (RFC 9728), indicateur de ressource (RFC 8707) portant l’URI canonique, vérification de l’audience à chaque requête et jeton transmis uniquement par l’en-tête <code>Authorization</code>. Chaque serveur publié séparément a sa propre URI canonique; en mode agrégé, les portées sont préfixées par l’identifiant du serveur au catalogue, et la passerelle vérifie que chaque appel vise un serveur couvert par les portées du jeton.',
      ['06-07', '06-17']),
    C('et valider <code>iss</code> (RFC 9207) avant d’échanger le code d’autorisation.',
      'et, avant d’échanger le code d’autorisation, valider <code>iss</code> (RFC 9207) s’il est présent, rejeter la réponse qui en est dépourvue alors que les métadonnées du serveur d’autorisation annoncent son support et, face à un serveur d’autorisation qui ne l’annonce pas, employer une <code>redirect_uri</code> distincte par serveur d’autorisation et vérifier l’émetteur attendu pour la transaction (RFC 9700).',
      ['06-10']),
    # [2.18] A-33 : renvoi à la règle unique de sortie réseau; la règle CIMD sur les redirections, plus stricte, demeure
    C('<strong>DOIT</strong> refuser l’authentification par secret partagé, ne pas suivre les redirections, bloquer les adresses à usage spécial et borner la taille du document lu.</p>',
      '<strong>DOIT</strong> refuser l’authentification par secret partagé, ne suivre aucune redirection (règle du brouillon CIMD, plus stricte que l’EXIG-SEC-12), appliquer pour le reste la règle de sortie réseau de l’EXIG-SEC-12 et borner la taille du document lu.</p>',
      ['07-08']),
    # [2.08, 2.55] EXIG-MCP-14 : gabarits de ressource; concordance définie
    C('lire le palier de risque, le seuil d’approbation et l’outil de compensation d’un outil dans son entrée au catalogue, jamais dans ses annotations ni dans son <code>_meta</code>. Les serveurs internes <strong>DOIVENT</strong> néanmoins déclarer leurs annotations, qui <strong>DOIVENT</strong> concorder avec la classification du catalogue; un écart <strong>DOIT</strong> bloquer l’homologation.',
      'lire le palier de risque, le seuil d’approbation et l’outil de compensation d’un outil ou d’un gabarit de ressource dans son entrée au catalogue, jamais dans ses annotations ni dans son <code>_meta</code>. Les serveurs internes <strong>DOIVENT</strong> néanmoins déclarer leurs annotations, qui <strong>DOIVENT</strong> concorder avec la classification du catalogue : <code>readOnlyHint</code> vrai pour un outil P0 ou P1 et faux pour un outil P2 ou P3; <code>idempotentHint</code> vrai seulement si une clé d’idempotence est déclarée au catalogue. Un écart <strong>DOIT</strong> bloquer l’homologation; les autres indices relèvent de la revue.',
      ['06-03', '07-16']),
    # [2.44, 2.95] sessions : à terme seulement; formulation de l'analyse d'Akamai
    C('<p>Le passage au protocole sans état supprime le détournement d’identifiant de session, mais déplace le risque',
      '<p>À terme, après la migration (EXIG-MCP-22), le passage au protocole sans état supprime le détournement d’identifiant de session, que les serveurs antérieurs gardent pendant la coexistence, mais il déplace le risque',
      ['06-14']),
    C('L’analyse de la version candidate publiée par Akamai le 25 juin 2026 relève notamment',
      'L’analyse, publiée par Akamai le 25 juin 2026, de la version candidate relève notamment',
      ['07-23']),
    # [2.38] EXIG-MCP-15 : en-têtes obligatoires selon la révision inscrite au catalogue
    C('et rejeter toute divergence ou tout en-tête obligatoire absent par HTTP 400 et l’erreur -32020.',
      'et rejeter par HTTP 400 et l’erreur -32020 toute divergence, ainsi que l’absence de tout en-tête obligatoire selon la révision inscrite au catalogue pour le serveur visé, et non selon celle que déclare l’appelant.',
      ['07-04']),
    # [2.43] EXIG-MCP-16 : baggage filtré, clés admises tenues au catalogue
    C('<strong>DOIVENT</strong> conserver les clés réservées de <code>_meta</code> (protocole, capacités du client, contexte de trace), ignorer ou filtrer les clés non reconnues et ne fonder',
      '<strong>DOIVENT</strong> conserver les clés réservées de <code>_meta</code> (protocole, capacités du client, <code>traceparent</code> et <code>tracestate</code>), filtrer <code>baggage</code> par liste d’autorisation à chaque frontière de confiance, retirer toute clé absente de la liste des clés admises que le catalogue tient pour chaque serveur et ne fonder',
      ['07-17']),
    # [2.39, 2.05] A-10 : EXIG-MCP-17, clé non ambiguë, entropie, usage unique défini et partagé entre répliques
    C('liés côté serveur à l’utilisateur authentifié (clé de la forme <code>utilisateur:identifiant</code>, l’utilisateur étant tiré du jeton vérifié); la possession',
      'd’au moins 128 bits d’entropie, liés côté serveur à l’utilisateur authentifié (clé formée de l’émetteur et du sujet du jeton vérifié, <code>iss</code> et <code>sub</code>, et de l’identifiant, sérialisée sans ambiguïté); la possession',
      ['07-05']),
    C('en protéger l’intégrité par HMAC ou par chiffrement authentifié (AEAD), y inclure le mandant, une courte durée de vie et l’empreinte de la requête d’origine, et en garantir l’usage unique lorsque l’étape l’exige.</p>',
      'en protéger l’intégrité par HMAC ou par chiffrement authentifié (AEAD), sous une clé propre au serveur, y inclure le mandant, l’identifiant du serveur et de l’outil, une courte durée de vie et l’empreinte de la requête d’origine. Toute étape qui porte une approbation ou une écriture P2 ou P3 est à usage unique : le serveur tient un registre des états consommés, partagé par toutes ses répliques et conservé pendant la durée de vie de l’état, et une relance qui présente le même <code>requestState</code> pour la même requête renvoie le résultat mémorisé, sans nouvel effet.</p>',
      ['06-05', '07-05', '08-08']),
    # [2.16] EXIG-MCP-18 : contrôle à l'exécution, y compris pour les tiers
    C('les schémas d’outils <strong>DOIVENT</strong> être analysés en intégration continue pour le vérifier.</p>',
      'la passerelle et les hôtes <strong>DOIVENT</strong> écarter de <code>tools/list</code> tout outil dont une propriété marquée <code>x-mcp-header</code> n’est pas inscrite au catalogue comme projection autorisée, ce qui couvre les serveurs de tiers; pour les serveurs internes, l’analyse des schémas en intégration continue complète ce contrôle.</p>',
      ['07-11']),
    # [2.17, 2.18] A-33 : EXIG-MCP-19, règle de sortie réseau unique; icônes matricielles, SVG rendu en image matricielle ou refusé
    C('lors de la découverte OAuth, n’accepter que HTTPS, bloquer les plages d’adresses privées, de bouclage et lien-local, valider chaque redirection et passer par un mandataire de sortie;',
      'lors de la découverte OAuth, n’accepter que HTTPS et appliquer la règle de sortie réseau de l’EXIG-SEC-12, un serveur d’autorisation interne légitime étant atteint par son entrée de catalogue, jamais par une URL fournie;',
      ['07-08', '08-06']),
    C('n’accepter une icône qu’en <code>https</code> ou <code>data:</code>, de même origine que le serveur, récupérée sans identifiants et dont le type est validé par signature binaire.</p>',
      'n’accepter qu’une icône matricielle (PNG, WebP ou JPEG) dont le type est validé par signature binaire, en <code>https</code>, de même origine que le serveur et récupérée sans identifiants, ou en <code>data:</code>; une icône SVG, format textuel qu’aucune signature binaire ne qualifie, est rendue en image matricielle avant tout affichage, ou refusée.</p>',
      ['07-07']),
    # [2.14] l'empreinte vérifie la définition, pas le comportement
    C('L’épinglage au catalogue est réglé à la section 6.8; l’exigence suivante en assure l’application à l’exécution.</p>',
      'L’épinglage au catalogue est réglé à la section 6.8; l’exigence suivante en vérifie la définition à l’exécution. Le comportement du serveur, que la définition ne transporte pas, relève de la signature des artefacts déployés et de la provenance (section 9.8), du contrôle des sorties réseau et des tests de contrat.</p>',
      ['07-09']),
    # [2.14, 2.15, 2.56, 2.77] A-21 : EXIG-MCP-20, canonisation, périmètre unique, préfixage, granularité de la suspension
    C('<p>À l’homologation, à chaque <code>tools/list</code> et avant l’exécution (EXIG-SEC-18), la passerelle <strong>DOIT</strong> calculer l’empreinte de chaque définition d’outil complète (nom, titre, description, icônes, schémas d’entrée et de sortie, annotations et <code>_meta</code>) et la comparer à l’empreinte épinglée au catalogue; un outil dont l’empreinte diffère est retiré de la liste remise à l’agent et suspendu jusqu’à une nouvelle approbation. La passerelle <strong>DOIT</strong> traiter chaque serveur comme un domaine de sécurité distinct : aucun serveur ne référence ni ne modifie les outils d’un autre, et la sortie de tout outil est une donnée non fiable (section 9.6).</p>',
      '<p>À l’homologation, à chaque <code>tools/list</code> et avant l’exécution, la passerelle <strong>DOIT</strong> calculer l’empreinte de chaque définition d’outil, soit le SHA-256 de sa canonisation RFC 8785 sur le périmètre de la définition publiée fixé par l’EXIG-INT-13 (icônes hachées par leur contenu, champs volatils de <code>_meta</code> inscrits au catalogue exclus), et la comparer à l’empreinte épinglée au catalogue; un outil dont l’empreinte diffère est retiré de la liste remise à l’agent et suspendu jusqu’à une nouvelle approbation, et la version entière du serveur l’est au-delà d’un nombre d’écarts inscrit au catalogue (l’EXIG-SEC-18 fait foi pour la suspension). Cette empreinte atteste la définition reçue, non le comportement du serveur. La passerelle <strong>DOIT</strong> traiter chaque serveur comme un domaine de sécurité distinct : elle préfixe tout outil remis à l’agent par l’identifiant de son serveur au catalogue, au moyen d’un séparateur admis dans les noms d’outils mais interdit dans ces identifiants, refuse toute collision de noms et réécrit de façon cohérente le corps et l’en-tête <code>Mcp-Name</code>; le catalogue indexe palier et empreinte sur le couple (serveur, nom d’origine); la revue d’homologation recherche dans les descriptions toute mention d’outils ou de serveurs tiers; la sortie de tout outil est une donnée non fiable (section 9.6).</p>',
      ['07-09', '07-10', '07-24', '09-05', '09-06']),
    # [2.58] A-14 : EXIG-MCP-21, renvoi au contrôle calculé; élicitation qui demande un secret
    C('pour une action qui en exige une (palier P3; palier P2 au-delà du seuil déclaré; toute écriture d’un agent de niveau N2) : seule compte l’approbation signée, liée à l’action exacte, décrite à la section 8.5.</p>',
      'pour une action qui en exige une (toute action pour laquelle le contrôle calculé selon l’EXIG-AUT-10 exige une approbation) : seule compte l’approbation signée, liée à l’action exacte, décrite à la section 8.5. L’hôte <strong>DOIT</strong> avertir l’utilisateur, ou refuser la demande, lorsqu’une élicitation en mode formulaire comporte un champ de format <code>password</code> ou dont le nom évoque un secret.</p>',
      ['07-20']),
    # [2.57] tableau 18 : correspondances corrigées et portée de la correspondance
    C('Le tableau 18 la met en correspondance avec les exigences du cadre; cette correspondance est une interprétation interne.',
      'Le tableau 18 la met en correspondance avec les exigences du cadre; cette correspondance est une interprétation interne, qui nomme les exigences qui traitent chaque risque sans prétendre le couvrir entièrement.',
      ['07-25']),
    C('<td>MCP03 Empoisonnement d’outil</td><td>EXIG-MCP-14, EXIG-MCP-20</td>',
      '<td>MCP03 Empoisonnement d’outil</td><td>EXIG-MCP-14, EXIG-MCP-20, EXIG-SEC-18</td>',
      ['07-25']),
    C('<td>EXIG-MCP-02, EXIG-MCP-20; section 9.8</td>',
      '<td>EXIG-MCP-20, EXIG-SEC-18; section 9.8</td>',
      ['07-25']),
    C('<td>MCP08 Absence d’audit et de télémétrie</td><td>EXIG-MCP-10, EXIG-MCP-16; chapitre 10</td>',
      '<td>MCP08 Absence d’audit et de télémétrie</td><td>EXIG-MCP-10; EXIG-OBS-01 et section 10.3 (journal d’audit)</td>',
      ['07-25']),
    # [2.38] pas de repli vers initialize pour un serveur inscrit en 2026-07-28
    C('avant de revenir à <code>initialize</code>; sur stdio,',
      'avant de revenir à <code>initialize</code>; un client de l’entreprise ne revient jamais à <code>initialize</code> pour un serveur inscrit au catalogue en 2026-07-28, et la sonde ne sert qu’à l’inventaire et au développement. Sur stdio,',
      ['07-21']),
    # A-22 : régime unique des suites de conformité (étape 6 de la migration)
    C('ses résultats complètent les tests internes sans les remplacer<strong><sup>[225, 226]</sup></strong>.</li>',
      'il suit le régime des suites de conformité de l’EXIG-INT-19 et complète les tests internes sans les remplacer<strong><sup>[225, 226]</sup></strong>.</li>',
      ['08-10', '09-10']),
    # [2.19, 2.46, 2.47, 2.96] A-23, A-26 : EXIG-MCP-22
    C('<p>La passerelle <strong>DOIT</strong> accepter les deux générations de MCP pendant une période de coexistence bornée, chaque serveur antérieur étant inscrit au catalogue avec sa date de migration. Tous les serveurs et clients en production <strong>DOIVENT</strong> avoir migré vers la révision 2026-07-28 au plus tard le 28 juillet 2027, et un nouveau développement <strong>NE DOIT PAS</strong> s’appuyer sur une fonction dépréciée (Roots, Sampling, journalisation protocolaire, DCR, transport HTTP+SSE). Pendant la transition, les clients traitent -32002 (serveurs antérieurs) et -32602 comme « ressource introuvable » en réponse à <code>resources/read</code> seulement.</p>',
      '<p>Pendant une période de coexistence bornée, la passerelle <strong>DOIT</strong> accepter la génération antérieure de MCP pour les seuls serveurs inscrits au catalogue avec une date de migration, et la refuser pour tout autre. Tous les serveurs et clients en production <strong>DOIVENT</strong> avoir migré vers la révision épinglée au catalogue (valeur initiale : 2026-07-28) au plus tard le 28 juillet 2027, échéance du cadre qui ne change que par une révision (section 1.6). Un nouveau développement <strong>NE DOIT PAS</strong> s’appuyer sur une fonction dépréciée (Roots, Sampling, journalisation protocolaire, DCR, transport HTTP+SSE), et toute intégration en production <strong>DOIT</strong> avoir cessé de les employer à la même échéance. Pendant la transition, un client traite -32002 (serveurs antérieurs) comme « ressource introuvable » en réponse à <code>resources/read</code>; il ne traite -32602 ainsi que si <code>error.data</code> le désigne comme tel, sinon comme une erreur de paramètres, et journalise tout -32602 avec l’identifiant de trace.</p>',
      ['07-03', '07-18', '07-19']),
    C('(le transport HTTP+SSE obéit à une échéance distincte : trois mois après que la SEP-2596 atteint l’état final)<strong><sup>[196]</sup></strong>; l’échéance retenue, choix du cadre, évite qu’une révision future ne rompe des intégrations en production.',
      '(le transport HTTP+SSE obéit à une échéance distincte : trois mois après que la SEP-2596 atteint l’état final, soit dès le début de septembre 2026, cette SEP étant finale depuis le 3 juin 2026, annexe H)<strong><sup>[196]</sup></strong>. L’échéance retenue, choix du cadre, vise à la fois le changement de génération et l’abandon des fonctions dépréciées, deux opérations distinctes : migrer vers 2026-07-28 ne retire pas Sampling d’une intégration. Elle précède la première révision qui pourrait retirer ces fonctions, celle de la fin de septembre 2027 si le calendrier de la SEP-3398 est tenu (annexe H).',
      ['07-03', '07-33']),

    # ---------------------------------------------------------------- § 6.6
    # [2.96] erratum : comité directeur technique de neuf sièges
    C('un comité directeur technique de huit entreprises (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow; composition annoncée le 12 mars 2026) le pilote<strong><sup>[29]</sup></strong>,',
      'un comité directeur technique de neuf sièges le pilote : les huit entreprises de la composition annoncée le 12 mars 2026 (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow)<strong><sup>[29]</sup></strong>, et Bloomberg depuis le 20 octobre 2026 (erratum, annexe H),',
      ['07-32']),
    # [2.59] A-20, A-23 : EXIG-A2A-01, délégation hors processus; critère agent/outil; version épinglée
    C('<p>Toute interaction par laquelle un agent délègue une tâche à un agent d’un autre domaine, d’un autre cadriciel ou d’un tiers <strong>DOIT</strong> utiliser A2A, version de protocole 1.0 (sauf pendant la coexistence bornée de l’EXIG-A2A-15). Un protocole agent-agent propriétaire <strong>DOIT</strong> être contenu derrière un adaptateur, conformément au catalogue (section 6.3). Les transferts entre sous-agents d’un même orchestrateur, dans un même processus, n’y sont pas tenus.</p>',
      '<p>Toute délégation à un agent d’un autre domaine, d’un autre cadriciel, d’un tiers ou d’un autre processus <strong>DOIT</strong> utiliser A2A, dans la version de protocole épinglée au catalogue (valeur initiale : 1.0), sauf pendant la coexistence bornée de l’EXIG-A2A-15. Un protocole agent-agent propriétaire <strong>DOIT</strong> être contenu derrière un adaptateur, conformément au catalogue (section 6.3). Seuls les transferts entre sous-agents d’un même orchestrateur, dans un même processus, en sont exemptés (EXIG-INT-05). Une cible est un agent si elle choisit elle-même, au moyen d’un modèle, les actions qu’elle exécute; sinon c’est un outil, même si elle conserve l’état d’une tâche ou demande une précision (extension Tasks, élicitation MCP).</p>',
      ['07-26']),
    # [2.60] URI bien connue unique par nom d'hôte
    C('Un agent exposé la publie à <code>https://{domaine}/.well-known/agent-card.json</code>;',
      'Un agent exposé la publie à <code>https://{domaine}/.well-known/agent-card.json</code>, URI unique par nom d’hôte : chaque agent exposé reçoit donc son propre nom d’hôte (p. ex. <code>risque-credit.agents.ent.ca</code>), à défaut de quoi le champ <code>tenant</code> distingue les agents d’un même point de terminaison;',
      ['07-28']),
    # [2.20, 2.40] tableau 19 : cartes de façade; ETag dérivé du hachage
    C('<td>Adresses de la passerelle d’agents, jamais l’adresse directe de l’agent.</td>',
      '<td>Adresses de la passerelle d’agents, jamais l’adresse directe de l’agent (cartes des agents de l’entreprise et cartes de façade des agents de tiers, EXIG-A2A-02).</td>',
      ['07-01', '07-27']),
    C('incrémentée à chaque changement publié; sert d’<code>ETag</code>.</td>',
      'incrémentée à chaque changement publié; l’<code>ETag</code> dérive du hachage de la représentation servie (EXIG-A2A-04).</td>',
      ['07-12']),
    C('<td>Obligatoires; renvoient au fournisseur d’identité de l’entreprise.</td>',
      '<td>Obligatoires; renvoient au fournisseur d’identité de l’entreprise (pour une carte de façade, celui qu’emploie la passerelle).</td>',
      ['07-01']),
    # [2.21] la découverte passe par le catalogue, auquel renvoie le registre
    C('Dans l’entreprise, le registre (section 11.4) est la source de découverte autorisée.',
      'Dans l’entreprise, la découverte passe par le catalogue d’entreprise, auquel renvoie la fiche de l’agent au registre (section 11.4; EXIG-INT-17).',
      ['07-29']),
    # [2.62] extension de gouvernance dans la carte étendue seulement
    C('Si un pair doit les lire, ils se déclarent comme extension de données dans <code>capabilities.extensions</code>.',
      'Si un pair doit les lire, ils se déclarent comme extension de données dans les <code>capabilities.extensions</code> de la carte étendue seulement, jamais dans la carte publique (EXIG-A2A-06).',
      ['07-31']),
    # [2.20, 2.21] EXIG-A2A-02 : carte de référence d'un agent interne; carte d'origine et carte de façade d'un tiers
    C('<p>Tout agent invocable par d’autres agents <strong>DOIT</strong> publier une carte conforme à A2A\xa01.0, l’inscrire au catalogue d’entreprise (et la rattacher à sa fiche au registre, section 11.4) et déclarer dans <code>supportedInterfaces</code> les adresses de la passerelle d’agents. Un agent exposé hors de l’entreprise <strong>DOIT</strong> aussi publier sa carte à l’URI bien connue; un agent interne ne la publie pas.</p>',
      '<p>Tout agent invocable par d’autres agents <strong>DOIT</strong> publier une carte conforme à A2A\xa01.0, l’inscrire au catalogue d’entreprise (et la rattacher à sa fiche au registre, section 11.4) et déclarer dans <code>supportedInterfaces</code> les adresses de la passerelle d’agents. Un agent exposé hors de l’entreprise <strong>DOIT</strong> aussi publier sa carte à l’URI bien connue; un agent interne ne la publie pas : la carte inscrite au catalogue est sa carte de référence, servie par la passerelle, et la fiche du registre y renvoie. Pour un agent de tiers, le catalogue conserve la carte d’origine, signée par le tiers et vérifiée à l’homologation, avec son empreinte; la passerelle sert aux agents de l’entreprise une carte de façade, qui porte ses propres adresses, est signée par une clé de l’entreprise et référence l’empreinte de la carte d’origine. Aucun client de l’entreprise ne suit les <code>supportedInterfaces</code> d’une carte d’origine.</p>',
      ['07-01', '07-14', '07-27', '07-29']),
    # [2.20, 2.21, 2.41] EXIG-A2A-03 : clé de façade, carte étendue, jku et kid, rejeu d'une ancienne carte
    C('avec une clé de l’émetteur de la carte (clé gérée par l’entreprise pour ses propres agents; pour un agent de tiers, clé dont le catalogue consigne la confiance). La passerelle d’agents et les clients <strong>DOIVENT</strong> rejeter une carte sans signature valide ou signée par une clé expirée ou révoquée.',
      'avec une clé de l’émetteur de la carte (clé gérée par l’entreprise pour ses propres agents et pour les cartes de façade; pour la carte d’origine d’un agent de tiers, clé dont le catalogue consigne la confiance). La règle vaut aussi pour la carte étendue. La passerelle d’agents et les clients <strong>DOIVENT</strong> rejeter une carte sans signature valide ou signée par une clé expirée ou révoquée, rejeter un <code>jku</code> ou un <code>kid</code> absent du catalogue et refuser une carte de version inférieure à la dernière qu’ils ont vue. Pour les clients externes, l’entreprise publie son jeu de clés (JWKS) sur son domaine principal.',
      ['07-01', '07-13', '07-14']),
    # [2.40, 2.21] EXIG-A2A-04 : ETag fort dérivé du hachage, signatures comprises; serveur désigné
    C('Le serveur <strong>DOIT</strong> fournir un <code>ETag</code> dérivé de cette version et un <code>Cache-Control</code>;',
      'Le serveur qui sert la carte (l’URI bien connue pour un agent exposé, la passerelle pour une carte de référence ou de façade) <strong>DOIT</strong> fournir un <code>ETag</code> fort, dérivé du hachage de la représentation servie, signatures comprises, et un <code>Cache-Control</code>; une nouvelle signature est un changement publié;',
      ['07-12', '07-14']),
    C('Pourquoi : un incrément fiable est le signal sur lequel le cadre fonde l’invalidation des copies en cache des clients (le guide de découverte admet aussi un ETag dérivé d’un hachage).',
      'Pourquoi : le hachage change dès qu’un octet de la carte change, signatures comprises, ce qu’un numéro de version ne garantit pas; un 304 ne peut donc pas prolonger une carte signée par une clé révoquée (le guide de découverte admet un ETag dérivé d’un hachage). SemVer reste le signal de compatibilité (section 6.8).',
      ['07-12']),
    # [2.21, 2.62] EXIG-A2A-06 : visée des seuls agents exposés; gouvernance en carte étendue
    C('<p>Les compétences réservées à des consommateurs internes <strong>DOIVENT</strong> être publiées dans la carte étendue, servie par <code>GetExtendedAgentCard</code> après authentification et contrôle des permissions. La carte publique se limite aux compétences destinées aux appelants externes.</p>',
      '<p>Pour un agent exposé hors de l’entreprise, les compétences réservées à des consommateurs internes <strong>DOIVENT</strong> être publiées dans la carte étendue, servie par <code>GetExtendedAgentCard</code> après authentification et contrôle des permissions, et la carte publique se limite aux compétences destinées aux appelants externes. La carte d’un agent interne, servie aux seuls clients authentifiés (EXIG-A2A-02), porte toutes ses compétences. L’extension de gouvernance ne figure que dans la carte étendue.</p>',
      ['07-14', '07-31']),
    # [2.06 a] lit. 17 : déduplication par messageId facultative dans la spécification
    C('le client ne pouvant pas en imposer un pour une nouvelle tâche; <code>contextId</code> regroupe',
      'le client ne pouvant pas en imposer un pour une nouvelle tâche (un réessai de <code>SendMessage</code> peut donc créer une seconde tâche, d’où la règle de l’EXIG-A2A-07); <code>contextId</code> regroupe',
      ['07-02']),
    # [2.23, 2.06 a, 2.61] EXIG-A2A-07
    C('<p>Lorsque la durée attendue d’une tâche dépasse 5 secondes (seuil fixé par le cadre), le client <strong>DOIT</strong> la suivre par flux en continu (<code>SendStreamingMessage</code>) ou par notification push. L’interrogation par <code>GetTask</code> et la reprise par <code>SubscribeToTask</code> <strong>PEUVENT</strong> servir à rétablir le suivi après une coupure, mais <strong>NE DOIVENT PAS</strong> servir au suivi courant.</p>',
      '<p>Lorsque la durée attendue d’une tâche, déclarée par compétence au catalogue (95<sup>e</sup> centile mesuré), dépasse 5 secondes (seuil fixé par le cadre), le client <strong>DOIT</strong> la suivre par flux en continu (<code>SendStreamingMessage</code>) ou par notification push, y compris pour le message qui relance une tâche interrompue; un flux ouvert porte des battements de cœur. L’interrogation par <code>GetTask</code> <strong>PEUT</strong> servir à rétablir le suivi après une coupure, mais <strong>NE DOIT PAS</strong> servir au suivi courant; la reprise par <code>SubscribeToTask</code> est permise après une coupure ou un état interrompu. Avant de réessayer un envoi dont la réponse s’est perdue, le client <strong>DOIT</strong> rechercher une tâche existante par <code>contextId</code> et par identifiant de message (<code>messageId</code>), et l’agent serveur <strong>DOIT</strong> rattacher à la tâche existante un message déjà reçu. Un délai maximal, inscrit au catalogue, borne les états <code>INPUT_REQUIRED</code> et <code>AUTH_REQUIRED</code>; à son terme, le serveur clôt la tâche dans un état terminal.</p>',
      ['08-01', '07-02', '07-30']),
    C('Pourquoi : une connexion bloquante longue se heurte aux délais des intermédiaires réseau, et une boucle d’interrogation consomme sans rien apprendre; la spécification laisse ce choix au client, d’où cette règle interne.',
      'Pourquoi : une connexion bloquante longue se heurte aux délais des intermédiaires réseau, et une boucle d’interrogation consomme sans rien apprendre; la spécification laisse ce choix au client, d’où cette règle interne. La spécification permet à l’agent de détecter un message en double par son <code>messageId</code> sans l’y obliger<strong><sup>[68]</sup></strong>; le cadre l’impose, pour que la clé d’idempotence de l’agent appelé reste stable d’un essai à l’autre (section 7.6).',
      ['07-02']),
    # [2.22] EXIG-A2A-08 : le client 0.3 de la coexistence
    C('<p>Tout client A2A <strong>DOIT</strong> envoyer <code>A2A-Version</code> à chaque requête.',
      '<p>Tout client A2A <strong>DOIT</strong> envoyer <code>A2A-Version</code> à chaque requête, sauf un client 0.3 pendant la période de l’EXIG-A2A-15.',
      ['07-15']),
    # [2.88] TLS; A-17 : un message A2A reçu est une source de contexte étiquetée
    C('<p>Tout échange A2A <strong>DOIT</strong> utiliser TLS 1.3 par défaut, TLS 1.2 étant le plancher toléré (versions antérieures désactivées), avec validation des certificats,',
      '<p>Tout échange A2A <strong>DOIT</strong> négocier TLS 1.3 lorsque le pair le permet, TLS 1.2 au minimum, versions antérieures désactivées, avec validation des certificats,',
      ['06-25']),
    C('valider ses paramètres et borner la taille des messages et des fichiers.</p>',
      'valider ses paramètres et borner la taille des messages et des fichiers. Un message ou une tâche A2A reçu est une source de contexte au sens de l’EXIG-SEC-03 et porte les étiquettes de la session qui l’a produit (EXIG-SEC-04).</p>',
      ['A-17']),
    # [2.24] EXIG-A2A-10 : compétence désignée et vérifiable; locataire autorisé par le jeton
    C('L’appelant <strong>DOIT</strong> présenter un jeton délégué dont l’audience est l’agent appelé (section 9.3). Lorsqu’un point de terminaison sert plusieurs locataires, la passerelle <strong>DOIT</strong> vérifier que le <code>tenant</code> demandé correspond aux droits du jeton, sans jamais le déduire du seul contenu de la requête.</p>',
      'L’appelant <strong>DOIT</strong> présenter un jeton délégué dont l’audience est l’agent appelé (section 9.3). Comme un message A2A s’adresse à l’agent, la compétence visée <strong>DOIT</strong> être désignée par une métadonnée d’une extension approuvée (EXIG-A2A-05), que la passerelle vérifie contre la portée du jeton, et l’agent serveur <strong>DOIT</strong> router de façon déterministe vers cette seule compétence; à défaut, chaque compétence a son propre point de terminaison. Lorsqu’un point de terminaison sert plusieurs locataires, la passerelle <strong>DOIT</strong> vérifier que le <code>tenant</code> demandé figure parmi les locataires que le jeton autorise.</p>',
      ['08-03']),
    # [2.63] EXIG-A2A-11 : Device Code encadré; justificatifs client sans secret partagé; [2.91] source unique du retrait
    C('(ou le Device Code pour un appareil sans navigateur) quand une personne s’authentifie, les justificatifs client pour un agent qui agit en son nom propre',
      '(ou le Device Code pour un appareil sans navigateur, réservé aux clients inscrits au catalogue, sous accès conditionnel et avec une durée de code courte) quand une personne s’authentifie, les justificatifs client, authentifiés par mTLS, <code>private_key_jwt</code> ou SVID et jamais par secret partagé, pour un agent qui agit en son nom propre',
      ['08-04']),
    C('Pourquoi : A2A 1.0 a retiré ces flux<strong><sup>[240]</sup></strong>,',
      'Pourquoi : A2A 1.0 a retiré ces flux<strong><sup>[30]</sup></strong>,',
      ['08-05']),
    # [2.18] A-33 : EXIG-A2A-12, règle de sortie réseau; récepteurs internes par le catalogue; reprises bornées
    C('<strong>DOIT</strong> valider l’URL de webhook contre la SSRF à l’enregistrement et à chaque livraison, après résolution DNS (plages privées, boucle locale et lien-local refusées), appliquer un délai d’expiration compris entre 10 et 30 secondes et des reprises à repli exponentiel.',
      '<strong>DOIT</strong> appliquer à l’URL de webhook, à l’enregistrement et à chaque livraison, la règle de sortie réseau de l’EXIG-SEC-12, sortir par la passerelle d’agents ou par le mandataire de sortie, appliquer un délai d’expiration compris entre 10 et 30 secondes et des reprises à repli exponentiel, bornées en nombre et en durée au catalogue. Un récepteur interne légitime, comme un orchestrateur de l’entreprise, est atteint par son entrée de catalogue, jamais par l’URL fournie.',
      ['07-08', '08-06']),
    # [2.43] EXIG-A2A-13 : nouvelle trace vers un agent hors périmètre
    C('par un span <code>invoke_agent</code> de type CLIENT. Le journal d’audit',
      'par un span <code>invoke_agent</code> de type CLIENT. Vers un agent hors du périmètre de confiance, la passerelle ouvre une nouvelle trace reliée par un lien de span et filtre <code>baggage</code> par liste d’autorisation (EXIG-OBS-02). Le journal d’audit',
      ['08-07']),
    # [2.64, 2.23] légende de la figure 9 : écart résiduel de la figure
    C('et l’écriture n’a lieu qu’avec un jeton d’approbation lié à l’action exacte. Source',
      'et l’écriture n’a lieu qu’avec un jeton d’approbation lié à l’action exacte. Le texte qui suit fait foi là où la figure diffère : l’étape 7 emploie <code>SendStreamingMessage</code>, le jeton d’approbation reste à la passerelle, et l’utilisateur et l’approbateur, réunis dans un même couloir, sont deux rôles distincts. Source',
      ['08-01', '08-09']),
    # [2.21] étape 2 : le catalogue
    C('<li>L’orchestrateur cherche au registre la compétence « risque de crédit »,',
      '<li>L’orchestrateur cherche au catalogue d’entreprise la compétence « risque de crédit »,',
      ['07-29']),
    # [2.05] A-10, A-15 : étapes 5 à 8
    C('l’action exacte à approuver : outil, arguments, montant.</li>',
      'l’action exacte à approuver : outil, arguments (clé d’idempotence comprise), montant.</li>',
      ['08-08']),
    C('l’approbation produit un jeton signé lié à l’empreinte de l’action (section 8.5).</li>\n<li>L’orchestrateur envoie un nouveau message rattaché au même <code>taskId</code>, qui transmet le jeton d’approbation.</li>\n<li>L’agent crédit appelle l’outil d’écriture de l’ERP avec le jeton d’approbation et une clé d’idempotence (section 7.6); la passerelle vérifie que le jeton correspond exactement à cet appel avant de le relayer.</li>',
      'l’approbation produit un jeton signé lié à l’empreinte de l’action, remis à la passerelle qui le conserve; l’orchestrateur ne reçoit que la référence de la demande, une donnée non secrète (section 8.5).</li>\n<li>L’orchestrateur envoie par <code>SendStreamingMessage</code> un nouveau message rattaché au même <code>taskId</code>, qui transmet la référence de la demande d’approbation.</li>\n<li>L’agent crédit appelle l’outil d’écriture de l’ERP avec la même clé d’idempotence et la référence de la demande (section 7.6); la passerelle y apparie le jeton qu’elle conserve, vérifie qu’il correspond exactement à cet appel et à cet appelant, puis relaie l’appel.</li>',
      ['06-05', '08-01', '08-08']),
    # [2.64] annulation : aucune écriture sans jeton valide; expiration côté serveur; auto-approbation
    C('l’orchestrateur annule la tâche (<code>CancelTask</code>) et aucune écriture n’a lieu.',
      'l’orchestrateur annule la tâche (<code>CancelTask</code>), et aucune écriture n’a lieu sans jeton d’approbation valide; un état interrompu qui n’est pas annulé expire côté serveur (EXIG-A2A-07). Le demandeur peut confirmer lui-même l’action, sauf pour un appel P3 d’un agent de classe élevée, qui exige deux approbateurs distincts dont au moins un n’est pas le mandant (section 8.5).',
      ['08-09']),
    # [2.25] A-22 : EXIG-A2A-14, à chaque déploiement; trousse épinglée; régime alpha
    C('avant son inscription au registre et à chaque nouvelle version mineure ou majeure de sa carte.',
      'avant son inscription au registre, à chaque déploiement de l’agent (code ou SDK compris) et à chaque nouvelle version de sa carte, avec une version d’<code>a2a-tck</code> épinglée à une étiquette au catalogue. Tant que la ligne visée de la trousse est alpha, seuls bloquent les tests MUST restés stables pendant deux versions de la trousse; les autres résultats sont consignés.',
      ['08-10']),
    # [2.22] EXIG-A2A-15 : DOIT, date absolue, version effective; degré modifié
    C('<p><strong><code>EXIG-A2A-15</code> · DEVRAIT</strong></p>',
      '<p><strong><code>EXIG-A2A-15</code> · DOIT</strong></p>',
      ['08-02']),
    C('<p>Un agent encore en 0.3 <strong>DEVRAIT</strong> migrer par double publication : sa carte annonce une interface 1.0 et une interface 0.3, cette dernière portant une date de retrait inscrite au catalogue, au plus six mois après l’ouverture de l’interface 1.0 (choix du cadre). Passé cette date, la passerelle <strong>DOIT</strong> refuser les requêtes sans en-tête <code>A2A-Version</code>.</p>',
      '<p>Un agent encore en 0.3 <strong>DOIT</strong> migrer par double publication : sa carte annonce une interface 1.0 et une interface 0.3, cette dernière portant une date de retrait absolue inscrite au catalogue, au plus six mois après l’approbation du cadre ou, si elle est postérieure, après l’inscription de l’agent (choix du cadre). Passé cette date, la passerelle <strong>DOIT</strong> refuser toute requête dont la version effective (en-tête <code>A2A-Version</code> ou paramètre de requête, une valeur absente ou vide valant 0.3) n’est pas prise en charge par l’interface inscrite au catalogue.</p>',
      ['07-15', '08-02']),

    # ---------------------------------------------------------------- § 6.7
    # [2.65] argument de topologie
    C('<p>S’y ajoute un argument de topologie : relier N agents deux à deux exige jusqu’à N(N−1)/2 liaisons, alors que N agents reliés à un courtier n’en exigent que N. Le gain porte sur le nombre de connexions; les sujets, les schémas et les contrats restent à gouverner.',
      '<p>L’argument du nombre de liaisons (N(N−1)/2 liaisons deux à deux, contre N vers un courtier) ne distingue pas le bus de la passerelle d’agents, qui forme déjà une étoile à N connexions; l’apport propre du bus est le découplage logique décrit ci-dessus. Les sujets, les schémas et les contrats restent à gouverner.',
      ['08-11']),
    # A-02 : le bus n'est pas un chemin hors des points d'application
    C('Le choix suit la matrice de la section 6.4 et le patron de chorégraphie de la section 7.2.</p>',
      'Le choix suit la matrice de la section 6.4 et le patron de chorégraphie de la section 7.2. Le bus n’est pas un chemin hors des points d’application : le courtier en est un (EXIG-EVT-11).</p>',
      ['08-20']),
    # [2.66, 2.92] EXIG-EVT-02 : attributs de données dès que data est présent; domaine fictif; adaptateur
    C('<code>time</code>, <code>datacontenttype</code> et <code>dataschema</code> (exigence du cadre). Le <code>type</code>',
      '<code>time</code> et, dès que l’événement porte <code>data</code>, <code>datacontenttype</code> et <code>dataschema</code> (exigence du cadre; pour un événement par référence, <code>dataschema</code> décrit la ressource que vise <code>dataref</code>). Un événement d’un système existant que consomme un agent passe par un adaptateur de mise en conformité. Le <code>type</code>',
      ['08-12']),
    C('<code>ca.entreprise.logistique.alerte.rupture.v1</code>',
      '<code>ca.ent.logistique.alerte.rupture.v1</code>',
      ['08-13']),
    # [2.91] format d'appel
    C('Sampling et Sequence<strong><sup>[251][187]</sup></strong>,',
      'Sampling et Sequence<strong><sup>[187, 251]</sup></strong>,',
      ['08-30']),
    # [2.67, 2.28] A-02 : tableau 20, attributs posés par l'intercepteur; plafond au catalogue du sujet
    C('<td>Obligatoire sur tout événement publié par un agent</td>',
      '<td>Obligatoire sur tout événement publié par un agent; posé par l’intercepteur de publication (EXIG-EVT-11)</td>',
      ['08-16']),
    C('<td>Obligatoire; augmenté de 1 à chaque republication</td>',
      '<td>Obligatoire; posé par l’intercepteur de publication : 1 de plus que le plus grand compteur reçu</td>',
      ['08-18']),
    C('plafond de sauts fixé au contrat du flux; l’événement dont le compteur atteint ce plafond n’est pas traité</td><td>Obligatoire; 4 par défaut; recopié sans modification</td>',
      'plafond de sauts inscrit à l’entrée de catalogue du sujet; l’événement dont le compteur atteint ce plafond n’est pas traité, si bien qu’un plafond N laisse traiter N − 1 événements de la chaîne</td><td>Obligatoire; 4 par défaut; minimum de la valeur reçue et du plafond du sujet de publication</td>',
      ['08-18', '08-19']),
    # [2.26, 2.43, 2.74] A-02 : EXIG-EVT-04
    C('<p>Tout événement publié par un agent <strong>DOIT</strong> porter les attributs obligatoires du tableau 20. Un consommateur <strong>DOIT</strong> refuser un événement d’agent qui en est dépourvu et le diriger vers la file de lettres mortes <em>(dead-letter queue)</em>.',
      '<p>Tout événement publié par un agent <strong>DOIT</strong> porter les attributs obligatoires du tableau 20. Est un événement d’agent tout événement publié sous une identité d’agent inscrite au registre : le courtier ou l’intercepteur de publication <strong>DOIT</strong> rejeter à la publication l’événement d’un tel producteur qui ne les porte pas (EXIG-EVT-11). Un consommateur <strong>DOIT</strong> en outre refuser un événement d’agent qui en est dépourvu et le diriger vers la file de lettres mortes <em>(dead-letter queue)</em> du sujet, inscrite au catalogue, qui hérite de la classification maximale du sujet et de ses listes de contrôle d’accès.',
      ['08-14', '08-31']),
    C('(ou, s’il ouvre la chaîne, celui de la trace qu’il ouvre) (section 10.1).</p>',
      '(ou, s’il ouvre la chaîne, celui de la trace qu’il ouvre), sauf pour un événement d’origine externe, régi par l’EXIG-OBS-02 (section 10.1).</p>',
      ['08-15']),
    # [2.27] la boucle-type traverse l'ERP; plafond de largeur
    C('Le compteur de sauts coupe cette boucle de façon déterministe, sans dépendre du jugement d’un modèle (figure 10).',
      'Le compteur de sauts, posé par l’intercepteur de publication et non par l’agent, coupe cette boucle de façon déterministe, sans dépendre du jugement d’un modèle (figure 10), à condition que le système d’enregistrement modifié propage les attributs : ajuster une commande est une écriture à l’ERP, qui publie son propre événement. Un plafond de largeur, tenu par le courtier par identifiant de trace, borne en outre les chaînes qui se ramifient : sans lui, k abonnés qui republient chacun produisent jusqu’à 1 + k + k² + k³ événements en quatre sauts.',
      ['08-16', '08-17']),
    # [2.27, 2.28, 2.35, 2.67] A-02, A-06 : EXIG-EVT-06
    C('<p>Le premier agent qui publie dans une chaîne <strong>DOIT</strong> fixer <code>xagenthopcount</code> à 1, <code>xagentorigin</code> à son identifiant et <code>xagentmaxhops</code> à la valeur du contrat du flux (4 par défaut). Tout agent qui publie en réaction à un événement reçu <strong>DOIT</strong> augmenter le compteur de 1 et recopier les deux autres valeurs sans les modifier. Un agent qui reçoit un événement dont <code>xagenthopcount</code> atteint ou dépasse <code>xagentmaxhops</code> <strong>DOIT</strong> s’abstenir de le traiter, le diriger vers la file de lettres mortes et lever une alerte. Le plafond d’un flux ne se relève que par une modification revue de son contrat.</p>',
      '<p>L’intercepteur de publication de la plateforme, et non l’agent, <strong>DOIT</strong> poser les attributs de chaîne (EXIG-EVT-11). Pour le premier événement d’une chaîne : <code>xagenthopcount</code> à 1, <code>xagentorigin</code> à l’identifiant et à la version de l’agent, <code>xagentmaxhops</code> au plafond inscrit à l’entrée de catalogue du sujet (4 par défaut). Pour un événement publié en réaction : <code>xagenthopcount</code> à 1 de plus que le plus grand compteur reçu, <code>xagentorigin</code> recopié, <code>xagentmaxhops</code> au minimum de la valeur reçue et du plafond du sujet de publication. Un système d’enregistrement adapté qui publie à la suite d’une écriture d’agent propage ces attributs par sa boîte d’envoi. Un consommateur qui reçoit un événement dont <code>xagenthopcount</code> atteint ou dépasse <code>xagentmaxhops</code> <strong>DOIT</strong> s’abstenir de le traiter, le diriger vers la file de lettres mortes et lever une alerte, regroupée par chaîne. Le courtier <strong>DOIT</strong> en outre plafonner le nombre d’événements par identifiant de trace dans une fenêtre de temps inscrite au catalogue. Un événement de compensation, déclaré comme tel au contrat du sujet et publié sous l’identité de compensation (EXIG-ORC-31), n’est pas soumis au plafond de sauts; il reste soumis à l’autorisation et à un budget propre. Le plafond d’un sujet ne se relève que par une modification revue de son entrée de catalogue.</p>',
      ['08-16', '08-17', '08-18', '08-19', '09-24']),
    C('Pourquoi : une règle locale, appliquée par chaque consommateur, borne la longueur de toute chaîne d’événements qui ne traverse que des consommateurs conformes (un composant qui n’applique pas la règle, ou qui n’est pas un agent, rompt la chaîne causale).',
      'Pourquoi : posés à la publication, hors de l’agent, les attributs bornent la chaîne sans dépendre du jugement d’un modèle; le minimum des plafonds fait prévaloir le sujet le plus strict, et le plafond par trace borne les chaînes ramifiées, que le compteur seul ne borne pas. Un système qui ne propage pas les attributs rompt encore la chaîne causale : le plafond par trace reste alors la seule borne. Une saga qui échoue près du plafond doit pouvoir se compenser.',
      ['08-16', '08-17', '09-24']),
    # [2.70] tableau 21 : le producteur idempotent ne couvre pas un redémarrage
    C('le producteur idempotent (depuis 0.11.0.0) évite les doublons dans le journal lors des reprises<strong><sup>[140]</sup></strong>',
      'le producteur idempotent (depuis 0.11.0.0) évite les doublons dus aux réessais internes d’une même session de producteur; un redémarrage du producteur ou du relais exige <code>transactional.id</code> ou la déduplication par le consommateur<strong><sup>[140]</sup></strong>',
      ['08-23']),
    # [2.06 b] A-09 : EXIG-EVT-08, rétention et atomicité de la déduplication; clé dérivée de l'événement
    C('et transmet au système cible une clé d’idempotence que ce dernier vérifie (section 7.6).',
      'et transmet au système cible une clé d’idempotence que ce dernier vérifie (section 7.6). Cette clé dérive du couple (<code>source</code>, <code>id</code>) de l’événement déclencheur, jamais de l’identifiant d’une tâche ouverte par le consommateur; l’état de déduplication est conservé au moins pendant la rétention du sujet et mis à jour dans la même transaction que l’effet, ou complété par une requête d’état qui constate l’effet.',
      ['08-24']),
    # [2.68, 2.69] EXIG-EVT-09 : pseudonyme admis; clé native; conditions de l'ordre
    C('sans renseignement personnel (EXIG-EVT-05), porté par <code>partitionkey</code> et précisé au contrat AsyncAPI. Le producteur <strong>DOIT</strong> aussi copier cette valeur dans la clé du message Kafka, au moyen d’un « Key Mapper » à activer explicitement, car la liaison reprend par défaut la clé fournie par l’utilisateur<strong><sup>[250]</sup></strong>.',
      'sans renseignement personnel direct (EXIG-EVT-05; un identifiant pseudonyme est admis et traité comme un renseignement personnel, pour la conservation comme pour l’accès), porté par <code>partitionkey</code> et précisé au contrat AsyncAPI. La clé native du courtier <strong>DOIT</strong> égaler <code>partitionkey</code> : sur Kafka, le producteur la fixe lui-même ou active le « Key Mapper » facultatif de la liaison, qui reprend par défaut la clé fournie par l’utilisateur<strong><sup>[250]</sup></strong>. L’ordre suppose en outre un nombre de partitions figé pendant la vie du sujet, un traitement séquentiel par clé chez le consommateur et un relais de boîte d’envoi ordonné.',
      ['08-21', '08-22', '08-32']),
    # [2.71] EXIG-EVT-10 : rejeu d'audit ou d'évaluation; renvois; sujet partagé; effacement
    C('sans excéder la rétention des traces et journaux d’audit fixée au chapitre 10), dans la limite du calendrier de conservation applicable aux RP. Tout rejeu <strong>DOIT</strong> s’exécuter',
      'sans excéder la rétention fixée par l’EXIG-OBS-13 pour le journal d’audit et par l’EXIG-CON-10 pour les traces), dans la limite du calendrier de conservation applicable aux RP; un sujet qui alimente plusieurs agents retient la plus longue de leurs fenêtres, et l’effacement des RP d’un sujet conservé se fait par chiffrement par personne ou par sujet, puis destruction de la clé. Tout rejeu d’audit ou d’évaluation <strong>DOIT</strong> s’exécuter',
      ['08-25']),
    C('jamais à répéter des actions en production.</p>',
      'jamais à répéter des actions en production. La reprise opérationnelle d’un groupe de consommateurs après une panne n’est pas un rejeu au sens de cette exigence : l’EXIG-EVT-08 la régit.</p>',
      ['08-25']),
    # [2.02, 2.26, 2.27, 2.28, 2.73] A-02 : nouvelle exigence EXIG-EVT-11, le courtier point d'application
    C('<div id="pourquoi-514"><p>Pourquoi : rejouer des entrées contre des outils réels répéterait leurs effets, et un modèle peut décider autrement la seconde fois.</p></div>\n</div>',
      '<div id="pourquoi-514"><p>Pourquoi : rejouer des entrées contre des outils réels répéterait leurs effets, et un modèle peut décider autrement la seconde fois.</p></div>\n</div>\n'
      '<p>Le bus ne porte aucun jeton, et l’initiateur qu’indiquent <code>authtype</code> et <code>authid</code> est informatif (EXIG-EVT-07) : sans point d’application au courtier, un consommateur agirait sous sa seule identité, hors de l’intersection des droits (PRIN-03) et de la limite de délégation. L’exigence qui suit fait du courtier un point d’application au même titre que la passerelle; elle ne le substitue pas à la passerelle pour l’effet.</p>\n'
      '<div id="exig-515">\n'
      '<p><strong><code>EXIG-EVT-11</code> · DOIT</strong></p>\n'
      '<p><strong>Courtier d’événements, point d’application</strong></p>\n'
      '<p>Le courtier et l’intercepteur de publication de la plateforme <strong>DOIVENT</strong>, pour la publication et la consommation : authentifier le producteur; appliquer les listes de contrôle d’accès par sujet (EXIG-EVT-07); poser eux-mêmes les attributs de gouvernance (identité de l’agent producteur, référence de délégation, compteur et plafond de sauts de l’EXIG-EVT-06, étiquettes de contamination et de sensibilité de la session productrice, EXIG-SEC-04); refuser un événement dont le <code>dataschema</code> ne figure pas parmi les schémas épinglés pour le sujet, et rejeter à la publication l’événement d’un agent qui ne porte pas les attributs du tableau 20. Est un événement d’agent tout événement publié sous une identité d’agent inscrite au registre. Le plafond de sauts appliqué est le minimum du plafond du premier sujet et de celui de chaque sujet traversé, et un plafond de largeur (événements par identifiant de trace, dans une fenêtre inscrite au catalogue) s’y ajoute. Toute action P2 ou P3 qu’un consommateur exécute à la suite d’un événement <strong>DOIT</strong> passer par la passerelle d’agents, sous la délégation que référence l’événement, échangée selon la RFC 8693 (EXIG-IAM-08), ou, à défaut, sous un mandat de service inscrit au catalogue pour ce sujet et pour ce consommateur; un tel saut compte dans la profondeur de délégation de l’EXIG-ORC-04.</p>\n'
      '<div id="pourquoi-515"><p>Pourquoi : un point d’application des politiques n’a de valeur que si tout chemin vers un effet le traverse; la chorégraphie, que l’EXIG-EVT-01 recommande, en serait sinon un contournement sanctionné, et l’empreinte des schémas épinglés (EXIG-INT-15) ne serait vérifiée par personne à l’exécution.</p></div>\n'
      '</div>',
      ['08-20', '08-29', '08-14', '08-16', '08-19']),

    # ---------------------------------------------------------------- § 6.8
    # A-13 : seuil déclaré selon l'EXIG-AUT-24; [2.08, 2.10, 2.72] tableau 22
    C('<td>Version et empreinte; palier P0 à P3 et seuil (section 8.3);',
      '<td>Version et empreinte; palier P0 à P3 et seuil, avec sa grandeur, son unité, sa portée et sa fenêtre (section 8.3, EXIG-AUT-24);',
      ['A-13']),
    C('<td>Ressource adressée par URI; invite nommée et décrite</td><td>Version et empreinte; classification</td>',
      '<td>Ressource adressée par URI; invite nommée et décrite</td><td>Version et empreinte (pour un gabarit <code>ui://</code>, empreinte de son contenu); palier P0 ou P1 d’une ressource (EXIG-MCP-05); classification; propriétaire et équipe de garde</td>',
      ['06-03', '06-06', '08-26']),
    C('<td>Version et empreinte; portée OAuth par compétence; renvoi à la fiche du registre</td>',
      '<td>Version et empreinte; portée OAuth par compétence et durée attendue par compétence (EXIG-A2A-07); renvoi à la fiche du registre; pour un agent de tiers, carte d’origine et son empreinte (EXIG-A2A-02)</td>',
      ['07-01', '08-01']),
    C('<td>Contrat AsyncAPI 3.x et <code>type</code> versionné (section 6.7)</td><td>Producteurs et consommateurs autorisés; classification; plafond de sauts</td>',
      '<td>Contrat AsyncAPI 3.x, avec la clé de partition, et <code>type</code> versionné (section 6.7)</td><td>Producteurs et consommateurs autorisés; classification; plafond de sauts et plafond par trace (EXIG-EVT-06); file de lettres mortes; propriétaire et équipe de garde</td>',
      ['08-19', '08-26', '08-31']),
    # [2.76] mineur : reformulation sans changement de sens
    C('<li><strong>mineur</strong> : ajout compatible et toute reformulation d’une description;</li>',
      '<li><strong>mineur</strong> : ajout compatible et reformulation d’une description sans changement de sens, établie par la revue sémantique (EXIG-INT-16);</li>',
      ['08-28', '09-30']),
    # [2.77, 2.78] EXIG-INT-13 : périmètre unique de la définition publiée, unité de version
    C('au moins mineure pour toute modification de la définition publiée (nom, description, schémas, annotations, compétences), majeure pour tout changement incompatible, y compris de sens. Pour un agent A2A, c’est le champ <code>version</code> de sa carte (EXIG-A2A-04).</p>',
      'au moins mineure pour toute modification de la définition publiée, majeure pour tout changement incompatible, y compris de sens. Pour un agent A2A, c’est le champ <code>version</code> de sa carte (EXIG-A2A-04). L’unité de version est l’outil, la ressource, l’invite, la carte d’agent ou le sujet; un serveur MCP n’est qu’un agrégat d’entrées. La définition publiée, que canonise l’empreinte (EXIG-INT-15, EXIG-INT-16, EXIG-MCP-20), comprend : pour un outil MCP, le nom, le titre, la description, les icônes, les schémas d’entrée et de sortie, les annotations et <code>_meta</code>, hors champs volatils inscrits au catalogue; pour une ressource ou une invite, son URI ou son nom, sa description et, pour un gabarit <code>ui://</code>, son contenu; pour une carte A2A, la carte canonisée sans le champ <code>signatures</code>; pour un sujet, le contrat AsyncAPI converti en JSON.</p>',
      ['09-06', '09-07']),
    # [2.03, 2.29, 2.75] A-21 : EXIG-INT-14, suspension; service multiversion; coexistence des types d'événements
    C('Seul un motif de sécurité, sur décision du comité, justifie un retrait anticipé.</p>',
      'Seul un motif de sécurité justifie un retrait anticipé : sur décision du comité, la version visée passe d’abord à l’état « suspendue », et la passerelle cesse immédiatement de la servir (EXIG-GOV-14); le comité fixe ensuite la date de retrait. Pendant la coexistence, la passerelle sert la version majeure précédente sous un nom d’outil suffixé par sa version majeure (p. ex. <code>domaine_outil_v2</code>) pour MCP, et sous une entrée <code>supportedInterfaces</code> par version majeure pour A2A, et elle route selon la dépendance épinglée de l’appelant; deux types d’événements coexistants (v1 et v2) portent un même identifiant de fait (<code>id</code> ou clé métier), et le consommateur abonné aux deux déduplique. Un contrat de tiers relève de l’EXIG-INT-16.</p>',
      ['09-01', '09-03', '08-27', '09-12']),
    # [2.14, 2.73] l'empreinte prouve la définition; contrats AsyncAPI; vérification des schémas d'événements
    C('Le numéro dit ce que le fournisseur affirme; l’empreinte prouve ce que l’agent reçoit. La fiche d’agent consigne ces dépendances (annexe B), et la passerelle vérifie l’empreinte à l’exécution (EXIG-MCP-20, EXIG-SEC-18).',
      'Le numéro dit ce que le fournisseur affirme; l’empreinte prouve la définition que l’agent reçoit, non le comportement du serveur, qui relève de la signature des artefacts déployés et de la provenance (section 9.8), du contrôle des sorties réseau et des tests de contrat. L’empreinte d’un contrat AsyncAPI porte sur sa conversion en JSON, canonisée de la même façon. La fiche d’agent consigne ces dépendances (annexe B); la passerelle vérifie l’empreinte à l’exécution (EXIG-MCP-20, EXIG-SEC-18) et, pour un événement, le courtier et le registre de schémas du consommateur vérifient que le <code>dataschema</code> reçu figure parmi les schémas épinglés (EXIG-EVT-11).',
      ['09-05', '08-29']),
    # [2.29, 2.14] EXIG-INT-15 : grain de l'épinglage, migration des mineures
    C('changer de version est une modification de la fiche, revue et tracée.</p>',
      'changer de version est une modification de la fiche, revue et tracée. L’épinglage porte sur MAJEUR.MINEUR et sur l’empreinte; un correctif, qui ne change pas l’empreinte, se suit sans modifier la fiche. À l’activation d’une version mineure, le propriétaire du contrat migre en lot les épinglages après avis aux consommateurs, ou la passerelle sert la mineure précédente pendant une fenêtre de migration inscrite au catalogue; au plus deux versions mineures d’une même majeure sont actives à la fois (choix du cadre).</p>',
      ['08-27', '09-03']),
    C('Pourquoi : sans épinglage, un fournisseur peut changer le comportement d’un agent à l’insu de son propriétaire.',
      'Pourquoi : sans épinglage, un fournisseur peut changer la définition que lit l’agent à l’insu de son parrain; l’épinglage ne prouve pas pour autant le comportement du fournisseur, qui relève de la section 9.8.',
      ['09-05']),
    # [2.30] EXIG-INT-16 : régime des tiers
    C('y compris pour les serveurs et agents de tiers. La revue confirme aussi le palier attribué.</p>',
      'y compris pour les serveurs et agents de tiers. La revue confirme aussi le palier attribué. Pour un tiers, dont l’entreprise ne contrôle ni le calendrier ni la chaîne d’intégration : la version est tenue au catalogue par l’entreprise; le contrat prévoit un préavis de changement de définition et un point d’accès de préversion (chapitre 13); un test différentiel à l’entrée du catalogue remplace la chaîne d’intégration de l’EXIG-INT-19; une revue accélérée vise un délai cible inscrit au catalogue. Hors préavis, la modification suspend l’outil ou l’agent jusqu’à la revue (EXIG-MCP-20) : ce mode fermé est le comportement assumé, la coexistence de l’EXIG-INT-14 étant alors impossible.</p>',
      ['09-04']),
    # [2.03] A-21 : état « suspendue »
    C('Chaque version de contrat est « en revue », « active », « dépréciée » (avec sa date de retrait) ou « retirée »,',
      'Chaque version de contrat est « en revue », « active », « dépréciée » (avec sa date de retrait), « suspendue » (motif de sécurité, EXIG-INT-14) ou « retirée »,',
      ['09-01']),
    # [2.03, 2.78] EXIG-INT-17 : unité de version; versions suspendues non servies
    C('qui recense chaque version de contrat (schéma, serveur MCP, carte d’agent A2A, sujet AsyncAPI)',
      'qui recense chaque version de contrat (outil, ressource ou invite MCP, regroupés par serveur, carte d’agent A2A, sujet AsyncAPI)',
      ['09-07']),
    C('la passerelle ne sert que les versions actives et les versions dépréciées non échues.</p>',
      'la passerelle ne sert que les versions actives et les versions dépréciées non échues, jamais une version suspendue ou retirée.</p>',
      ['09-01']),
    # [2.03, 2.42] A-21 : EXIG-INT-18, exception de sécurité; consommateurs non déclarés bloqués
    C('Une version n’est retirée qu’à l’échéance annoncée, jamais avant la fin de la coexistence de l’EXIG-INT-14, et après avis à ses consommateurs connus; les traces servent à repérer, avant l’échéance, les appels de consommateurs non déclarés.</p>',
      'Une version n’est retirée qu’à l’échéance annoncée, jamais avant la fin de la coexistence de l’EXIG-INT-14 sauf suspension de sécurité (EXIG-INT-14, EXIG-GOV-14), et après avis à ses consommateurs connus. La passerelle refuse tout appel d’une version absente de la fiche de l’appelant (EXIG-IAM-17); le rapprochement avec les appels observés est un contrôle de cohérence, rendu continu pendant la fenêtre de dépréciation.</p>',
      ['09-01', '09-08']),
    C('Pourquoi : les traces révèlent les consommateurs non déclarés avant que le retrait ne les brise.',
      'Pourquoi : le rapprochement révèle les écarts entre les fiches et les appels avant que le retrait ne brise un consommateur.',
      ['09-08']),
    # [2.25] A-22, A-27 : régime commun des suites; « étage » au lieu de « palier »
    C('<code>a2a-tck</code>, dont les tests MUST sont bloquants (EXIG-A2A-14)<strong><sup>[243]</sup></strong>, et le cadre officiel de tests de conformité MCP, encore en versions 0.x (préversion 0.2.0-alpha en cours)<strong><sup>[225, 226]</sup></strong>. Ces tests forment le premier palier de l’évaluation continue (section 10.4).</p>',
      '<code>a2a-tck</code> (EXIG-A2A-14)<strong><sup>[243]</sup></strong> et le cadre officiel de tests de conformité MCP, encore en versions 0.x (préversion 0.2.0-alpha en cours)<strong><sup>[225, 226]</sup></strong>. Les deux suites suivent un même régime (EXIG-INT-19). Ces tests forment le premier étage de l’évaluation continue (section 10.4).</p>',
      ['08-10', '09-10']),
    # [2.25, 2.77, 2.79, 2.93] A-22 : EXIG-INT-19
    C('<p>La chaîne d’intégration <strong>DOIT</strong> comparer chaque nouvelle version d’un contrat à la version active précédente et bloquer toute publication qui contient un changement incompatible sans incrément majeur. Avant son activation, la nouvelle version <strong>DOIT</strong> réussir les tests de contrat de ses consommateurs connus et, pour un agent A2A, les tests MUST d’<code>a2a-tck</code>; les résultats du cadre officiel de conformité MCP (ou d’une suite équivalente approuvée par l’architecture d’entreprise, EXIG-APP-08) sont consignés à titre informatif tant que ce cadre demeure en préversion 0.x et se déclare instable.</p>',
      '<p>La chaîne d’intégration <strong>DOIT</strong> comparer chaque nouvelle version d’un contrat à la version active précédente et bloquer toute publication qui contient un changement incompatible sans incrément majeur, ou dont l’empreinte change sans incrément au moins mineur. Avant son activation, la nouvelle version <strong>DOIT</strong> réussir le jeu d’évaluation de chaque agent consommateur connu, rejoué en environnement isolé contre elle (section 10.4) avec le seuil de réussite inscrit à sa fiche, et, pour un agent A2A, les tests de l’EXIG-A2A-14. Une suite de conformité (<code>a2a-tck</code>, cadre officiel de conformité MCP ou suite équivalente approuvée par l’architecture d’entreprise, EXIG-APP-03) est épinglée à une étiquette au catalogue; tant que sa ligne est alpha ou en préversion 0.x, ses résultats sont consignés et ne bloquent que sur les tests restés stables pendant deux versions de la suite. Pour un tiers, l’EXIG-INT-16 s’applique.</p>',
      ['08-10', '09-06', '09-09', '09-10', '09-11']),

    # ---------------------------------------------------------------- § 6.9
    # [2.80] EXIG-INT-20 : qualification « de l'AAIF » seulement
    C('<strong>NE DOIT PAS</strong> qualifier un projet de standard ou de projet de l’AAIF s’il ne figure pas',
      '<strong>NE DOIT PAS</strong> qualifier un projet de « projet de l’AAIF » ni de « standard de l’AAIF » s’il ne figure pas',
      ['09-13']),
    # [2.93] EXIG-INT-21 : la règle du tableau 15 sur AGNTCY
    C('<strong>NE DOIT PAS</strong> entrer dans une analyse de risque sans preuve de la configuration effective.</p>',
      '<strong>NE DOIT PAS</strong> entrer dans une analyse de risque sans preuve de la configuration effective. Toute dépendance de production à un composant d’AGNTCY exige une décision du comité.</p>',
      ['09-14']),
    # [2.81] trois protocoles principaux
    C('<p>Trois protocoles se partagent le commerce agentique, sans convergence.',
      '<p>Trois protocoles principaux se disputent le commerce agentique, sans convergence; d’autres initiatives existent, que le catalogue inscrit au statut Surveiller lorsqu’elles touchent l’entreprise.',
      ['09-17']),
    # [2.31] EXIG-INT-22
    C('<strong>DOIT</strong> être classé P3 et n’être exécuté qu’avec une approbation humaine signée, liée à l’action exacte (section 8.5). L’agent <strong>NE DOIT PAS</strong> recevoir ni transmettre de justificatif de paiement; il ne manipule que des jetons émis hors de lui, limités à un bénéficiaire et à un montant. Chaque paiement <strong>DOIT</strong> laisser au journal d’audit une preuve d’intention signée. Le paiement en l’absence de l’utilisateur <strong>NE DOIT PAS</strong> être autorisé tant qu’aucun protocole qui l’encadre n’a le statut Adopter.</p>',
      '<strong>DOIT</strong> être classé P3 et n’être exécuté qu’avec une approbation humaine signée, propre à la transaction et liée à l’action exacte (section 8.5). L’agent <strong>NE DOIT PAS</strong> recevoir ni transmettre de justificatif de paiement; il ne manipule que des jetons émis hors de lui, à usage unique et à courte échéance, limités à un bénéficiaire et à un montant, et liés à l’empreinte de l’approbation et à la clé d’idempotence de l’étape. Chaque paiement <strong>DOIT</strong> laisser au journal d’audit une preuve d’intention signée : l’approbation de la personne habilitée, qui peut être distincte du mandant. Est « en l’absence de l’utilisateur » tout paiement sans approbation humaine propre à la transaction; il <strong>NE DOIT PAS</strong> être autorisé, et l’adoption d’un protocole qui l’encadre ne l’autorise pas sans révision du cadre.</p>',
      ['09-15', '09-16']),
    # [2.94] A-29; [2.96] A-22 : la révision de MCP sort des signaux de l'EXIG-INT-23
    C('une décision de l’AAIF sur AGNTCY, une révision de MCP, dont la feuille de route du 22 août 2026 ne donne pas la date<strong><sup>[195]</sup></strong>, ou la première version étiquetée des conventions GenAI d’OpenTelemetry<strong><sup>[181]</sup></strong>.</p>',
      'une décision de l’AAIF sur AGNTCY ou la première version étiquetée du dépôt dédié semantic-conventions-genai d’OpenTelemetry (section 10.1)<strong><sup>[181]</sup></strong>. Une révision de MCP, standard au statut Adopter, ne relève pas de ces signaux : sa publication déclenche la révision extraordinaire de l’EXIG-GOV-18, et l’annonce de sa date relève de la révision trimestrielle (la SEP-3398 la fixe au 30 mars 2027, sous réserve; section 6.5).</p>',
      ['09-19', '09-31']),

    # ---------------------------------------------------------------- § 7.1
    # [2.86] lit. 53 : chiffres du billet seulement
    C('<li><strong>Erreurs.</strong> Google Research mesure une amplification des erreurs pouvant atteindre 17,2 fois',
      '<li><strong>Erreurs.</strong> Selon le billet de Google Research du 28 janvier 2026, chiffres absents du résumé de la version 3 de l’article, l’amplification des erreurs peut atteindre 17,2 fois',
      ['09-28']),
    # [2.34] (part du § 7.1) EXIG-ORC-01 : options plus simples que le patron retenu
    C('pourquoi les options plus simples (code ou règle métier, appel direct au modèle, flux déterministe, agent unique outillé) ne répondent pas au besoin.',
      'pourquoi les options plus simples que le patron retenu, prises de la plus simple à la plus complexe parmi le code ou la règle métier, l’appel direct au modèle, le flux déterministe et l’agent unique outillé, ne répondent pas au besoin.',
      ['09-21']),
    # [2.32] A-32 : EXIG-ORC-02, règle de décision statistique et périmètre
    C('Elle n’est retenue que si le gain de qualité ou de délai couvre le surcoût mesuré; la comparaison est versée',
      'Elle n’est retenue que si son taux de réussite n’est pas inférieur à celui de la base de référence (borne inférieure de l’intervalle de confiance à 95 % de la différence supérieure à l’opposé d’une marge de non-infériorité déclarée à la fiche) et si son gain, valorisé par une valeur monétaire déclarée par tâche réussie, couvre le surcoût mesuré; la comparaison déclare la taille d’échantillon, le nombre de répétitions, la statistique et la règle de décision (section 10.4). Sont visés les patrons 3 à 7 du tableau 24 et la variante encadrée, dès que plus d’un composant choisit lui-même ses actions au moyen d’un modèle; un routeur sans modèle ou un évaluateur réduit à une invite distincte n’en fait pas un système multiagent. La comparaison est versée',
      ['09-20', '09-29']),

    # ---------------------------------------------------------------- § 7.2
    # [2.83] légende de la figure 11 : évaluateur et itération
    C('les points orangés signalent un contrôle de schéma entre étapes.',
      'les points orangés signalent un contrôle de schéma entre étapes. Pour l’évaluateur-optimiseur, l’évaluateur est un modèle ou une invite distincts de ceux du producteur (EXIG-ORC-05).',
      ['09-25']),
    # A-20 : appel interne réservé aux sous-agents d'un même processus
    C('délègue à des spécialistes (A2A ou appel interne), puis consolide leurs artefacts.',
      'délègue à des spécialistes (A2A, ou appel interne entre sous-agents d’un même processus), puis consolide leurs artefacts.',
      ['A-20']),
    # [2.85] garde-fou parallèle : la fusion attend le verdict
    C('Analyse multisource, vérification croisée, garde-fou exécuté en parallèle de la tâche.',
      'Analyse multisource, vérification croisée, garde-fou exécuté en parallèle de la tâche, dont la fusion attend le verdict (EXIG-ORC-07).',
      ['09-27']),
    # [2.84] gestionnaire hors décompte
    C('<td>Trois agents au plus, plafond de tours; propagation d’idées entre agents.</td>',
      '<td>Trois agents participants au plus, plus un gestionnaire (EXIG-ORC-06), plafond de tours; propagation d’idées entre agents.</td>',
      ['09-26']),
    # [2.33] A-16 : contrôle le plus strict de la chaîne
    C('Un orchestrateur plafonné à N3 peut ainsi déléguer à un exécutant plafonné à N1, et chaque action reste soumise à la règle la plus stricte entre le niveau de l’agent qui agit et le palier de l’outil appelé (section 8.4).</p>',
      'Un orchestrateur plafonné à N3 peut ainsi déléguer à un exécutant plafonné à N1. Chaque action est soumise au contrôle le plus strict de la chaîne : le niveau d’autonomie et la classe les plus contraignants entre l’initiateur et l’agent qui agit, combinés au palier de l’outil appelé (section 8.4). Ces valeurs voyagent dans le contexte de délégation (EXIG-ORC-23) et s’imposent à l’exécutant, et la passerelle les vérifie (EXIG-AUT-10) : un exécutant N3 de classe modérée n’écrit pas seul pour un initiateur N1 ou de classe élevée.</p>',
      ['09-22']),
    # [2.04] A-16 : EXIG-ORC-04, profondeur vérifiée au serveur d'autorisation; [2.86] Pourquoi
    C('Le serveur d’autorisation, lors de l’échange de jetons (EXIG-IAM-08, section 9.3), et la passerelle d’agents <strong>DOIVENT</strong> vérifier la profondeur par l’imbrication de la réclamation <code>act</code> du jeton délégué et rejeter toute délégation excédentaire.</p>',
      'Le serveur d’autorisation <strong>DOIT</strong> vérifier la profondeur lors de chaque échange de jetons (EXIG-IAM-08, section 9.3) et refuser l’échange qui l’excède; la passerelle d’agents ne fonde aucune décision sur les acteurs imbriqués, que la RFC 8693 tient pour informatifs (EXIG-IAM-11). Toute délégation entre agents, même sans mandant humain, passe par un échange de jetons dont le sujet est le mandant d’origine ou, s’il n’y a pas de mandant, l’agent initiateur. Un transfert (patron 3) remplace l’acteur courant sans ajouter de niveau, l’échange que refait la passerelle n’en ajoute pas non plus, et un appel interne entre sous-agents d’un même processus (patron 5) ne délègue pas au-delà. Un saut d’événement qui agit pour une personne compte comme un niveau (EXIG-EVT-11).</p>',
      ['09-02']),
    C('Pourquoi : choix du cadre; la coordination multiagent alourdit la communication',
      'Pourquoi : choix du cadre, que l’étude citée n’étaye qu’indirectement; la coordination multiagent alourdit la communication',
      ['09-28']),
    # [2.83] EXIG-ORC-05 : définition de l'itération
    C('et s’arrêter après trois itérations au plus.',
      'et s’arrêter après trois itérations au plus, une itération étant un cycle de production et d’évaluation.',
      ['09-25']),
    # [2.85] EXIG-ORC-07 : verdict du garde-fou bloquant
    C('un seul composant <strong>DOIT</strong> écrire le résultat final dans un système d’enregistrement.</p>',
      'un seul composant <strong>DOIT</strong> écrire le résultat final dans un système d’enregistrement. Une branche de garde-fou <strong>DOIT</strong> rendre son verdict avant la fusion; une expiration vaut refus (PRIN-12).</p>',
      ['09-27']),
    # [2.35] A-06 : EXIG-ORC-08, coordinateur de saga
    C('<strong>DOIT</strong> avoir un propriétaire de bout en bout inscrit au registre, une saga explicite (section 7.5) et les contrôles d’enveloppe de la section 6.7.</p>',
      '<strong>DOIT</strong> avoir un propriétaire de bout en bout inscrit au registre, une saga explicite (section 7.5) et les contrôles d’enveloppe de la section 6.7. Un coordinateur de saga, composant inscrit au registre, y tient le rôle de l’orchestrateur des EXIG-ORC-16 à 18 (journal de compensation, escalade), et ses compensations passent par le canal de compensation (EXIG-ORC-31); à défaut de coordinateur, la saga est orchestrée.</p>',
      ['09-24']),
]

JOURNAL = [
    # (localisation, correctif en une phrase, constats)
    ('§ 6.4, tableau 16 (Tasks)', 'Extension Tasks marquée Beta; interrogation à l’intervalle annoncé par le serveur, avec plancher et quota par mandant, reconnue pour MCP.', ['06-12', '06-33']),
    ('§ 6.4, questions de choix', 'Questions non exclusives, qui préparent la soumission de l’EXIG-INT-10; question 3 alignée sur le critère agent/outil (choisit ses actions au moyen d’un modèle).', ['06-09', '06-31']),
    ('§ 6.4, tableau 16 et § 6.7', 'L’argument N(N−1)/2 est remplacé par celui du découplage logique, la passerelle formant déjà une étoile.', ['08-11']),
    ('§ 6.4, tableau 16 (interface utilisateur)', 'Flux SSE structuré de l’orchestrateur désigné comme patron interne au statut Adopter; AG-UI limité aux pilotes.', ['06-11']),
    ('§ 6.5, EXIG-MCP-01', 'Exception limitée à la fonction locale P0-P1 de l’EXIG-ARC-01; toute action P2-P3 est un outil MCP derrière la passerelle; outil hébergé par le fournisseur de modèles admis au seul palier P0.', ['06-01']),
    ('§ 6.5, EXIG-MCP-02', 'server/discover réservé aux serveurs 2026-07-28, initialize pour les antérieurs; vérification périodique des serveurs de tiers (date d’approbation du cadre non fixée : elle relève de l’historique).', ['06-15']),
    ('§ 6.5, figure 7 et exemple', 'Jeton émis pour le point d’accès de la passerelle, second jeton pour le serveur de domaine; un client par point d’accès; portées préfixées en mode agrégé (EXIG-MCP-09). Figure non modifiable : sa légende corrige l’écart.', ['06-02', '06-17']),
    ('§ 6.5, figure 7 (légende)', 'EMA signalée au statut Évaluer (pilotes seulement). Figure non modifiable.', ['06-32']),
    ('§ 6.5, EXIG-MCP-05 et EXIG-MCP-14', 'Ressources classées au catalogue (P0 ou P1), contrôles de palier, masquage et balisage appliqués à resources/read; outil de lecture de remplacement pour un hôte sans lecture de ressources.', ['06-03', '06-30']),
    ('§ 6.5, EXIG-MCP-03 et tableau 17', 'Contexte d’autorisation défini (émetteur, sujet, client, audience, portées); invalidation à la révocation, à la suspension, au changement de portées et à la reconnexion; rien en cache sans cacheScope.', ['06-04', '06-21']),
    ('§ 6.5, EXIG-MCP-17, tableau 17, figure 9', 'Usage unique défini (approbation, écriture P2-P3), registre partagé des états consommés, relance qui renvoie le résultat mémorisé; la relance MRTR garde la clé et compte pour une opération; la clé d’idempotence figure dans l’action à approuver (étape 5).', ['06-05', '07-06', '08-08']),
    ('§ 6.5, EXIG-MCP-04', 'Clé d’idempotence à toute création de tâche MCP; empreinte du contenu des gabarits ui:// épinglée et vérifiée; CSP et permissions tirées du catalogue, jamais de _meta.ui.', ['06-13', '06-06']),
    ('§ 6.5, EXIG-MCP-08 et EXIG-MCP-09', 'Serveur local permis sur le seul poste de développement sans justificatif de production; en Streamable HTTP, bouclage, Origin et authentification obligatoires; plus d’exemption implicite d’autorisation pour HTTP.', ['06-07']),
    ('§ 6.5, EXIG-MCP-09', 'iss validé s’il est présent, réponse sans iss rejetée si son support est annoncé, sinon redirect_uri distincte par serveur d’autorisation (RFC 9700).', ['06-10']),
    ('§ 6.5, tableau 17 et sécurité propre à MCP', 'Suppression des sessions présentée comme acquise après la migration seulement; affinité limitée aux serveurs antérieurs inscrits pendant la coexistence.', ['06-14', '07-22']),
    ('§ 6.5, EXIG-MCP-20, EXIG-MCP-07 et § 6.5 (agrégation)', 'Préfixage obligatoire par l’identifiant de serveur, séparateur interdit dans ces identifiants, collisions refusées, réécriture de Mcp-Name, indexation sur (serveur, nom d’origine), revue des mentions d’outils tiers; noms internes limités à 96 caractères.', ['07-10', '06-16']),
    ('§ 6.5, EXIG-MCP-20, § 6.5 et § 6.8', 'Canonisation RFC 8785 et périmètre unique de la définition publiée; l’empreinte atteste la définition, non le comportement, renvoyé à la signature des artefacts, à la provenance et aux tests de contrat.', ['07-09', '09-05']),
    ('§ 6.5, EXIG-MCP-18', 'La passerelle et les hôtes écartent tout outil dont une projection x-mcp-header n’est pas inscrite au catalogue, serveurs de tiers compris.', ['07-11']),
    ('§ 6.5, EXIG-MCP-19', 'Icônes matricielles validées par signature binaire; une icône SVG est rendue en image matricielle ou refusée.', ['07-07']),
    ('§ 6.5-6.6, EXIG-MCP-12, EXIG-MCP-19, EXIG-A2A-12', 'Renvoi à la règle unique de sortie réseau de l’EXIG-SEC-12; cibles internes par le catalogue; règle CIMD sur les redirections gardée comme disposition spéciale; reprises des webhooks bornées.', ['07-08', '08-06']),
    ('§ 6.5, EXIG-MCP-22', 'Abandon des fonctions dépréciées exigé de toute intégration en production au 28 juillet 2027, distinct de la migration; Pourquoi corrigé. Échéance unique du 28 juillet 2027 plutôt que le 30 avril 2027 proposé : selon la SEP-3398, la première révision qui pourrait retirer ces fonctions serait celle de septembre 2027 (annexe H), ce qui laisse la marge voulue.', ['07-03']),
    ('§ 6.5, EXIG-MCP-15 et migration', 'En-têtes obligatoires selon la révision inscrite au catalogue; pas de repli vers initialize pour un serveur inscrit en 2026-07-28.', ['07-04', '07-21']),
    ('§ 6.5, EXIG-MCP-17', 'Clé d’état fondée sur (iss, sub, identifiant) sans ambiguïté, 128 bits d’entropie, identifiants du serveur et de l’outil dans le requestState, clé propre au serveur.', ['07-05']),
    ('§ 6.5, EXIG-MCP-16, EXIG-A2A-13, EXIG-EVT-04', 'traceparent et tracestate conservés, baggage filtré aux frontières, clés _meta admises tenues au catalogue; nouvelle trace vers un agent hors périmètre; événement d’origine externe régi par l’EXIG-OBS-02.', ['07-17', '08-07', '08-15']),
    ('§ 6.5, EXIG-MCP-22', 'Double prise en charge réservée aux serveurs inscrits avec une date de migration; version cible « épinglée au catalogue (valeur initiale : 2026-07-28) »; échéance du cadre modifiable par révision seulement.', ['07-19']),
    ('§ 6.5, EXIG-MCP-22', 'Le code -32602 n’est lu comme « ressource introuvable » que si error.data le désigne; il est journalisé avec la trace.', ['07-18']),
    ('§ 6.5, tableau 17 (dépréciations)', 'Retraits immédiats de ping, logging/setLevel et notifications/roots/list_changed rattachés au passage sans état, hors politique de cycle de vie (lit. 2).', ['06-20']),
    ('§ 6.5, versionnage MCP', 'non retenu : la page Versioning de MCP définit l’identifiant comme la date du dernier changement incompatible; le texte la reproduit fidèlement.', ['06-18']),
    ('§ 6.5, architecture', 'L’identifiant de requête non nul est présenté comme acquis depuis 2024-11-05; seul resultType est nouveau en 2026-07-28.', ['06-19']),
    ('§ 6.5, EXIG-MCP-03', 'Fusion des listes agrégées par serveur puis par nom, ordre stable après filtrage.', ['06-22']),
    ('§ 6.5, EXIG-MCP-07', 'Erreurs structurées décrites dans l’outputSchema (union du succès et de l’erreur), ce qui reste conforme à la spécification; une seule forme du résultat transmise au modèle.', ['06-23']),
    ('§ 6.5, tableau 18', 'EXIG-SEC-18 ajoutée à MCP03 et MCP04, EXIG-MCP-02 retirée de MCP04, MCP08 renvoyé à EXIG-OBS-01 et au § 10.3; la correspondance est dite partielle par nature, sans marquage ligne par ligne.', ['07-25']),
    ('§ 6.5, EXIG-MCP-14', 'Concordance définie : readOnlyHint vrai en P0-P1, faux en P2-P3; idempotentHint vrai seulement avec une clé déclarée.', ['07-16']),
    ('§ 6.5, EXIG-MCP-20', 'Suspension de l’outil, puis de la version du serveur au-delà d’un nombre d’écarts; l’EXIG-SEC-18 fait foi pour la suspension.', ['07-24']),
    ('§ 6.5, EXIG-MCP-21', 'Renvoi au contrôle calculé de l’EXIG-AUT-10; avertissement ou refus d’une élicitation qui demande un secret.', ['07-20']),
    ('§ 6.5, sécurité propre à MCP', 'Formulation de l’analyse d’Akamai désambiguïsée; décompte (six éléments contre cinq zones à l’annexe F) non harmonisé : contenu de [203] non vérifié, annexe F hors tranche.', ['07-23']),
    ('§ 6.5, transport et autorisation', 'Réassociation DNS; parenthèse en double retirée et révision -17 d’OAuth 2.1 signalée (lit. 29); intégration de DPoP au profil MCP; « jetons liés à l’expéditeur » (l’annexe A relève d’une autre tranche).', ['06-24', '06-26', '06-27', '06-28']),
    ('§ 6.5-6.6, EXIG-MCP-08 et EXIG-A2A-09', 'TLS 1.3 négocié lorsque le pair le permet, TLS 1.2 au minimum, versions antérieures désactivées, formulé de même pour MCP et A2A.', ['06-25']),
    ('§ 6.5, tableau 16, EXIG-MCP-06, § 6.5', 'Critère de revue vérifiable pour l’interdiction du miroir CRUD; adaptateur de composition orienté tâche.', ['06-08']),
    ('§ 6.5, tableau 17', 'Retrait accéléré « pour un risque de sécurité actif (avis publié ou exploitation documentée) », et non « exceptionnel » (lit. 4).', ['A-22', 'lit. 4']),
    ('§ 6.5, versionnage et tableau 17; EXIG-MCP-22', 'Précisions de l’annexe H reportées : SEP-3398 (révision au 30 mars 2027, sous réserve); HTTP+SSE admissible au retrait dès le début de septembre 2026, la SEP-2596 étant finale depuis le 3 juin 2026.', ['06-34', '07-33']),
    ('§ 6.6, gouvernance', 'Erratum appliqué : comité directeur technique de neuf sièges, Bloomberg depuis le 20 octobre 2026.', ['07-32']),
    ('§ 6.6, EXIG-A2A-01', 'Délégation hors processus couverte; seuls les sous-agents d’un même processus sont exemptés; critère agent/outil; version épinglée au catalogue (valeur initiale 1.0).', ['07-26']),
    ('§ 6.6, EXIG-A2A-02, EXIG-A2A-03, tableau 19, tableau 22', 'Carte d’origine du tiers conservée au catalogue, carte de façade servie et signée par l’entreprise; aucun client ne suit les adresses d’une carte d’origine.', ['07-01', '07-27']),
    ('§ 6.6, EXIG-A2A-02, EXIG-A2A-04, EXIG-A2A-06, figure 9', 'Carte de référence d’un agent interne au catalogue, servie par la passerelle; EXIG-A2A-06 limitée aux agents exposés; carte étendue signée; découverte au catalogue. L’exemple C.3 relève d’une autre tranche.', ['07-14', '07-29']),
    ('§ 6.6, EXIG-A2A-08 et EXIG-A2A-15', 'Exception du client 0.3; date de retrait absolue comptée depuis l’approbation du cadre ou l’inscription; refus fondé sur la version effective (en-tête ou paramètre, vide valant 0.3). Degré modifié : DOIT (annexe D à mettre à jour).', ['07-15', '08-02']),
    ('§ 6.6, EXIG-A2A-07 et figure 9', 'Relance d’une tâche interrompue en flux continu, battements de cœur, reprise par SubscribeToTask permise, durée attendue déclarée par compétence. Figure non modifiable : sa légende signale l’écart de l’étape 7.', ['08-01']),
    ('§ 6.6, EXIG-A2A-07 et § 6.6', 'Recherche d’une tâche existante par contextId et messageId avant tout réessai, rattachement par le serveur; déduplication présentée comme un choix du cadre (lit. 17).', ['07-02']),
    ('§ 6.6, EXIG-A2A-10', 'Compétence désignée par une extension approuvée, vérifiée par la passerelle, routage déterministe; locataire tiré des locataires autorisés par le jeton.', ['08-03']),
    ('§ 6.6, EXIG-A2A-14, EXIG-INT-19, § 6.8', 'Conformité vérifiée à chaque déploiement et à chaque version de carte; suites épinglées à une étiquette; tant qu’une suite est alpha ou 0.x, seuls bloquent les tests stables pendant deux versions, pour a2a-tck comme pour MCP.', ['08-10', '09-10']),
    ('§ 6.6, EXIG-A2A-04 et tableau 19', 'ETag fort dérivé du hachage de la représentation servie, signatures comprises; une nouvelle signature est un changement publié.', ['07-12']),
    ('§ 6.6, EXIG-A2A-03', 'Rejet d’un jku ou d’un kid absent du catalogue et d’une carte de version inférieure; JWKS publié pour les clients externes.', ['07-13']),
    ('§ 6.6, EXIG-A2A-03 (ancrage)', 'non retenu en partie : l’EXIG-A2A-03 ancre déjà la confiance des clés dans le catalogue; seuls la fraîcheur et l’ancrage des clients externes sont corrigés.', ['07-13']),
    ('§ 6.6, découverte', 'Un nom d’hôte par agent exposé, ou le champ tenant, pour l’URI bien connue.', ['07-28']),
    ('§ 6.6, EXIG-A2A-07', 'Délai maximal des états INPUT_REQUIRED et AUTH_REQUIRED inscrit au catalogue, clôture par le serveur; la table des transitions de la spécification n’est pas reproduite, faute de vérification.', ['07-30']),
    ('§ 6.6, métadonnées de gouvernance et EXIG-A2A-06', 'Extension de gouvernance réservée à la carte étendue; l’exemple C.3 relève d’une autre tranche.', ['07-31']),
    ('§ 6.6, EXIG-A2A-11', 'Device Code réservé aux clients inscrits, sous accès conditionnel; justificatifs client par mTLS, private_key_jwt ou SVID, jamais par secret partagé. Degré NE DOIT PAS inchangé, pour ne pas désaccorder l’annexe D.', ['08-04']),
    ('§ 6.6, figure 9, étapes 5 à 8 et suite', 'Jeton d’approbation conservé par la passerelle, référence non secrète transmise; annulation non atomique corrigée (aucune écriture sans jeton valide), expiration côté serveur, rôles d’utilisateur et d’approbateur distingués, auto-approbation bornée. Figure non modifiable : couloir unique signalé en légende.', ['08-09']),
    ('§ 6.6, EXIG-A2A-11 (Pourquoi)', 'Retrait des flux OAuth appuyé sur une seule source, [30]; le doublon [235]/[240] relève de l’annexe G.', ['08-05']),
    ('§ 6.6, EXIG-A2A-09', 'Message ou tâche A2A reçu traité comme source de contexte étiquetée (EXIG-SEC-03, SEC-04).', ['A-17']),
    ('§ 6.7, EXIG-EVT-11', 'Nouvelle exigence : le courtier et l’intercepteur de publication, points d’application (authentification, listes de contrôle d’accès, attributs posés par eux, schémas épinglés vérifiés, plafonds de sauts et de largeur), et toute action P2-P3 d’un consommateur passée par la passerelle sous délégation référencée ou mandat de service.', ['08-20', '08-29']),
    ('§ 6.7, EXIG-EVT-04 et EXIG-EVT-11', 'La nature « agent » est fixée par l’identité du producteur au registre; rejet à la publication de l’événement d’agent sans attributs.', ['08-14']),
    ('§ 6.7, EXIG-EVT-06 et § 6.7', 'Attributs posés par l’intercepteur, propagation par les systèmes adaptés, plafond par trace au courtier, alertes regroupées; limite de la boucle ERP nommée.', ['08-16', '08-17']),
    ('§ 6.7, EXIG-EVT-06, tableaux 20 et 22', 'Plafond logé à l’entrée de catalogue du sujet et appliqué comme minimum de la valeur reçue et du plafond du sujet.', ['08-19']),
    ('§ 6.7, tableau 20 et EXIG-EVT-06', 'Compteur égal à 1 de plus que le plus grand compteur reçu; sémantique « un plafond N laisse traiter N − 1 événements » écrite; version dans xagentorigin. Figure 10 non modifiable : elle reste conforme à cette sémantique.', ['08-18']),
    ('§ 6.7, EXIG-EVT-06 et § 7.2, EXIG-ORC-08', 'Événement de compensation hors plafond de sauts, sous l’identité de compensation (EXIG-ORC-31); coordinateur de saga inscrit au registre, à défaut saga orchestrée.', ['09-24']),
    ('§ 6.7, EXIG-EVT-08', 'Clé dérivée de (source, id) de l’événement déclencheur; déduplication conservée pendant la rétention du sujet, atomique avec l’effet ou complétée par une requête d’état.', ['08-24']),
    ('§ 6.7, EXIG-EVT-02', 'datacontenttype et dataschema exigés dès que data est présent; événement par référence; adaptateur pour les systèmes existants; domaine fictif ca.ent.', ['08-12', '08-13']),
    ('§ 6.7, EXIG-EVT-09', 'Pseudonyme admis comme clé et traité comme un RP; clé native du courtier égale à partitionkey; conditions de l’ordre énoncées (Key Mapper confirmé facultatif, lit. 38; balise 1.0.2 non relue).', ['08-21', '08-22', '08-32']),
    ('§ 6.7, tableau 21', 'Le producteur idempotent couvre les réessais d’une même session; un redémarrage exige transactional.id ou la déduplication du consommateur.', ['08-23']),
    ('§ 6.7, EXIG-EVT-10', 'Rejeu d’audit ou d’évaluation seulement; fenêtre maximale des agents abonnés; renvois à l’EXIG-OBS-13 et à l’EXIG-CON-10; effacement par destruction de clé.', ['08-25']),
    ('§ 6.7, EXIG-EVT-04 et tableau 22', 'File de lettres mortes par sujet, inscrite au catalogue, qui hérite de la classification et des listes de contrôle d’accès du sujet.', ['08-31']),
    ('§ 6.7, enveloppe', 'Format d’appel [187, 251].', ['08-30']),
    ('§ 6.7, contexte de trace', 'non retenu pour le point principal : le cadre suit l’extension Distributed Tracing, qui laisse le contexte de chaque saut au transport; seul l’écart avec l’EXIG-OBS-02 est corrigé.', ['08-15']),
    ('§ 6.7, EXIG-EVT-01', 'Le bus n’est pas un chemin hors des points d’application.', ['08-20']),
    ('§ 6.8, tableau 22', 'Propriétaire et équipe de garde, clé de partition, palier des ressources, carte d’origine des tiers, plafond par trace et file de lettres mortes ajoutés; seuil déclaré selon l’EXIG-AUT-24.', ['08-26', 'A-13']),
    ('§ 6.8, EXIG-INT-14, EXIG-INT-17, EXIG-INT-18', 'État « suspendue » ajouté : retrait anticipé de sécurité précédé d’une suspension qui fait cesser le service; l’EXIG-INT-18 reprend l’exception.', ['09-01']),
    ('§ 6.8, EXIG-INT-14 et EXIG-INT-15', 'Service multiversion : nom suffixé par la majeure (MCP), une entrée supportedInterfaces par majeure (A2A); épinglage sur MAJEUR.MINEUR et empreinte; migration en lot des mineures; au plus deux mineures actives.', ['08-27', '09-03']),
    ('§ 6.8, EXIG-INT-16', 'Régime des tiers : version tenue par l’entreprise, préavis contractuel, point d’accès de préversion, test différentiel, revue accélérée, suspension assumée hors préavis.', ['09-04']),
    ('§ 6.8, EXIG-INT-13', 'Périmètre unique de la définition publiée par type d’interface; unité de version à l’outil, à la ressource, à l’invite, à la carte ou au sujet.', ['09-06', '09-07']),
    ('§ 6.8, EXIG-INT-18', 'Appel d’une version absente de la fiche refusé; rapprochement continu pendant la dépréciation.', ['09-08']),
    ('§ 6.8, EXIG-INT-19', 'Renvoi corrigé vers l’EXIG-APP-03; jeu d’évaluation de chaque agent consommateur rejoué contre la nouvelle version; empreinte modifiée sans incrément bloquée.', ['09-09', '09-11']),
    ('§ 6.8, coexistence des événements', 'Types v1 et v2 coexistants liés par un même identifiant de fait, déduplication par le consommateur.', ['09-12']),
    ('§ 6.8, versionnage sémantique', 'Mineur : reformulation sans changement de sens, établie par la revue sémantique.', ['08-28', '09-30']),
    ('§ 6.8, épinglage', 'Empreinte d’un contrat AsyncAPI calculée sur sa conversion JSON canonisée; dataschema vérifié par le courtier et le registre de schémas.', ['08-29']),
    ('§ 6.8, tests de compatibilité', '« Premier étage » de l’évaluation continue au lieu de « palier » (homonyme).', ['A-27']),
    ('§ 6.9, EXIG-INT-20', 'Seules les qualifications « projet de l’AAIF » et « standard de l’AAIF » sont visées.', ['09-13']),
    ('§ 6.9, EXIG-INT-21', 'Règle annoncée au tableau 15 ajoutée : toute dépendance de production à AGNTCY exige une décision du comité.', ['09-14']),
    ('§ 6.9, EXIG-INT-22', 'Approbation propre à la transaction; jetons à usage unique, à courte échéance, liés à l’empreinte et à la clé; signataire de la preuve d’intention désigné; « absence de l’utilisateur » définie et interdite sans révision du cadre.', ['09-15', '09-16']),
    ('§ 6.9, commerce agentique', '« Trois protocoles principaux »; les autres initiatives au statut Surveiller au besoin (Visa, Mastercard et x402 non vérifiés, donc non nommés).', ['09-17']),
    ('§ 6.9, EXIG-INT-23', 'non retenu : l’arbitrage A-22 limite l’EXIG-INT-23 aux statuts Évaluer et Surveiller, l’EXIG-GOV-18 portant la révision des standards Adopter.', ['09-18']),
    ('§ 6.9, signaux à suivre', 'Première version étiquetée du dépôt semantic-conventions-genai; la révision de MCP sort des signaux (EXIG-GOV-18), sa date (30 mars 2027, sous réserve) relevant de la révision trimestrielle.', ['09-19', '09-31']),
    ('§ 7.1, EXIG-ORC-01', 'Options plus simples que le patron retenu, de la plus simple à la plus complexe; le réagencement de la figure 12 relève du § 7.3.', ['09-21']),
    ('§ 7.1, EXIG-ORC-02', 'Règle de non-infériorité à 95 %, valeur monétaire déclarée par tâche réussie, taille d’échantillon et répétitions déclarées; patrons visés énumérés selon le critère d’agent.', ['09-20', '09-29']),
    ('§ 7.1, erreurs, et EXIG-ORC-04 (Pourquoi)', '17,2 et 4,4 fois attribués au billet du 28 janvier 2026, absents du résumé de la version 3 (lit. 53); limite de deux niveaux dite choix du cadre appuyé indirectement.', ['09-28']),
    ('§ 7.2, EXIG-ORC-04', 'Profondeur vérifiée par le serveur d’autorisation à l’échange; aucune décision de la passerelle sur les act imbriqués (RFC 8693, § 4.1, lit. 30); délégation sans mandant par échange; transfert et échange de la passerelle sans niveau ajouté; appel interne borné.', ['09-02']),
    ('§ 7.2, patrons et autonomie', 'Contrôle le plus strict de la chaîne (niveau et classe de l’initiateur et de l’agent qui agit), transmis dans le contexte de délégation et vérifié par la passerelle.', ['09-22']),
    ('§ 7.2, figure 11 et EXIG-ORC-05', 'Évaluateur : modèle ou invite distincts; itération définie. Figure non modifiable : sa légende corrige l’écart.', ['09-25']),
    ('§ 7.2, tableau 24 et EXIG-ORC-06', 'Trois participants au plus, plus un gestionnaire (décompte de la source [9] non vérifié).', ['09-26']),
    ('§ 7.2, tableau 24 et EXIG-ORC-07', 'La fusion attend le verdict du garde-fou; une expiration vaut refus.', ['09-27']),
    ('§ 7.2, EXIG-ORC-07', 'non retenu pour le point (b) : l’EXIG-ORC-07 limite déjà les branches à la lecture et à la production d’artefacts.', ['09-27']),
    ('§ 7.2, tableau 24 (patron 5)', 'Appel interne réservé aux sous-agents d’un même processus.', ['A-20']),
]
