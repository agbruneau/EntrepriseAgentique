**Segment scope**: Pages 584 à 663 (Annexes B [clôture pp. 583-585], Annexe I [I.1 pp. 585-651, I.2 p. 651], Annexe N [pp. 652-663], segments S54 à S60 du plan de revue).

# Rapport d'Audit Unitaire Définitif — Segment Annexes et Bibliographie (Niveau 2, Racine RSA)

**Ouvrage examiné** : *Interopérabilité et Orchestration en Entreprise Agentique* (Édition Novembre 2026, 663 pages).  
**Auteur de l'ouvrage** : André-Guy Bruneau M.Sc. IT.  
**Auditeur racine** : Agrégateur Final de Revue (Niveau 2, Racine RSA).  
**Synthèses de Niveau 1 réconciliées** : 
- *Agrégateur A1* (`aggregator_1.md`, 44,4 Ko — synthèse contradictoire C1 et C3).
- *Agrégateur A2* (`aggregator_2.md`, 28,4 Ko — synthèse contradictoire C2 et C4).  
**Régime d'évaluation** : Production — Rigueur mathématique, vérification formelle sur sources primaires, preuve matérielle in-text et opposabilité prudentielle/réglementaire.  
**Date d'évaluation** : Novembre 2026.

---

# 1. Résumé exécutif et verdict global

## 1.1 Objet et rôle architectural du segment terminal
Le segment final du Compendium (pages 584 à 663, ancré dès la clôture de l'Annexe B à la page 578) constitue la clé de voûte de l'appareil critique, de la traçabilité des faits et de la force probatoire de l'ensemble de l'ouvrage :
- **L'Annexe B (pp. 578-585)** récapitule le *socle de référence* composé de 159 faits primaires codifiés ($S\text{-}001$ à $S\text{-}159$) issus des trois tomes initiaux : Volume II (46 faits, $S\text{-}001$ à $S\text{-}046$), Volume III (96 faits, $S\text{-}047$ à $S\text{-}142$) et Volume I (17 faits, $S\text{-}143$ à $S\text{-}159$). Chaque fait s'accompagne d'un niveau de preuve formalisé ([A] vote adversarial à trois juges, [B] source primaire ouverte sans vote complet, [C] repérage non extrait) et d'un degré d'absence documenté.
- **L'Annexe I (pp. 585-651)** présente la *« Bibliographie générale consolidée »* de l'œuvre. La sous-section I.1 (pp. 586-651) regroupe alphabétiquement 1 065 notices de publications, tandis que la sous-section I.2 (p. 651) formule la clause méthodologique régissant la non-reprise des références issues des Volumes II et III.
- **L'Annexe N (pp. 652-663)** met en œuvre le protocole d'actualisation temporelle arrêté au 1ᵉʳ novembre 2026, confrontant les 14 événements du tableau 50.1 aux mutations factuelles observées, répercutant l'instruction de la *Note AMF IA* (CRE-IA-2026-01-QC du 31 octobre 2026) et publiant le registre des éléments non revalidés adossé aux sources primaires [AN-1] à [AN-27].

## 1.2 Bilan des points forts de l'appareil documentaire
L'audit contradictoire de Niveau 2 met en lumière des qualités méthodologiques et empiriques de premier ordre, qui démarquent nettement le Compendium des publications généralistes en intelligence artificielle :
1. **Exactitude absolue des sources de l'Annexe N [AN-1 à AN-27]** : Le balayage exhaustif des 27 sources primaires confirme leur entière authenticité au 1ᵉʳ novembre 2026. La publication de la version finale officielle du NIST IR 8547 le 27 octobre 2026 (`DOI:10.6028/NIST.IR.8547`), l'état du projet de loi fédéral canadien C-36 (succédant à C-27/AIDA, déposé le 15 juin 2026 en 45ᵉ législature), le calendrier IETF OAuth 2.1 (`draft-ietf-oauth-v2-1-17` du 31 octobre 2026), le passage en Last Call de WIMSE (`draft-ietf-wimse-workload-identity-practices-08` le 30 octobre 2026) et l'étiquetage `v1.1.0-rc` d'A2A le 29 octobre 2026 à 12 h 05 UTC sont rigoureusement exacts.
2. **Absence totale d'hallucinations de références scientifiques** : Contrairement aux dérives fréquentes des synthèses générées par modèle de langage, aucune notice bibliographique de l'Annexe I.1 n'est fabriquée. L'échantillonnage de plus de 200 références de pointe 2024-2026 (Anbiaee et al. sur la modélisation des menaces MCP/A2A, Bhardwaj sur les contrats comportementaux d'agents, Cemri et al. sur les défaillances multi-agents à NeurIPS 2025, Chen et al. sur la délégation post-quantique AITH, DeepSeek-R1 dans *Nature*, l'incident EchoLeak CVE-2025-32711) a été intégralement vérifié auprès des registres arXiv, CrossRef, DOI et IETF.
3. **Transparence épistémique exemplaire sur les blocages d'accès** : L'auteur documente avec franchise les limites opérationnelles de ses sondes automatisées : refus HTTP 403 (pare-feu applicatif WAF) opposés par les portails de l'Autorité des marchés financiers (AMF) et de la FIDO Alliance le 1ᵉʳ novembre 2026, statut HTTP 202 non résolu sur EUR-Lex, et nécessité d'un arbitrage interactif manuel.

## 1.3 Synthèse des cinq défaillances structurelles majeures
En dépit de ces qualités d'enquête remarquables, le segment terminal est grevé de cinq vices structurels majeurs qui détruisent sa portée probatoire :
1. **Non-rejouabilité et circularité des axiomes théoriques cardinaux (Annexe B, p. 584)** : La totalité des 17 faits du Volume I ($S\text{-}143$ à $S\text{-}159$) sont dégradés au niveau [C] et transitent par des synthèses internes du Volume III. Plus grave encore, les principes architecturaux les plus fondamentaux de l'ouvrage — l'invariant transversal à quatre termes ($S\text{-}153$), l'impossibilité de la chaîne d'opposabilité au-delà de deux sauts de délégation ($S\text{-}154$), le plan de contrôle obligatoire ($S\text{-}156$) et le cas fil rouge ($S\text{-}158$) — portent textuellement la mention *« Citation non rejouable »* ou *« Cible supprimée »*. Des théorèmes centraux du livre reposent ainsi sur des sources déclarées impossibles à reproduire.
2. **Falsification méthodologique et non-consolidation de l'Annexe I.2 (p. 651)** : L'intitulé « Bibliographie générale consolidée » est trompeur. L'Annexe I.2 confesse que le dépouillement des Volumes II et III ne livre **zéro adresse primaire résoluble**. Sur les 159 faits du socle, **142 faits (89,3 %)** — couvrant l'identité d'agent, les passeports cryptographiques, la ligne directrice BSIF E-23, la conformité à la Loi 25 québécoise et la responsabilité civile — sont totalement privés de notice bibliographique pérenne (DOI, URL canonique, pagination).
3. **Troncature du protocole de péremption du Ch. 50 au geste 1 en Annexe N (p. 652)** : L'Annexe N applique uniquement le geste 1 (constater à la source primaire) et renonce expressément aux gestes 2 (amender l'Annexe B) et 3 (reprendre les chapitres dépendants). Ce blocage méthodologique engendre une désynchronisation doctrinale permanente : le corps de l'ouvrage maintient des affirmations périmées ou contredites (Ch. 8/S-002 sur A2A, Ch. 21 sur NIST IR 8547 Final, Ch. 27/42 sur la ligne directrice AMF, Ch. 30 sur l'obligation de marquage synthétique de l'AI Act en août 2026 plutôt qu'en décembre 2026, Ch. 32 sur le transfert de supervision de la CDBA à la Banque du Canada, Ch. 44 sur ArchiMate 4 vs 3.2).
4. **Échec patent du dédoublonnage et rupture arithmétique de la page 585** : Alors que l'introduction p. 585 proclame un dédoublonnage systématique par identifiant et signature textuelle, la table de synthèse est graphiquement brisée (cellules vides et puce orpheline `• 134 1065`) et mathématiquement incohérente ($1\,263 - 134 = 1\,129 \neq 1\,065$, déficit inexpliqué de 64 entrées). De plus, l'Annexe I.1 héberge une prolifération de triplicatas (OAuth 2.1, EchoLeak), de quadruplicatas (IETF WIMSE) et plus de 50 paires de doublons textuels stricts non fondus.
5. **Pollution éditoriale par fuite de directives internes et corruption d'URL par `\ufffe`** : L'assemblage final a laissé échapper dans les notices bibliographiques distribuées au public 8 fragments manifestes de notes de régie, consignes d'enquête et commentaires d'auteur non purgés (Wang/Tolk LCIM p. 646, OSFI/BSIF p. 630, OpenID p. 640, Finastra p. 605, Dun Yuan p. 650, EBA p. 602, Sparx Systems p. 640, OpenAI Morgan Stanley p. 628). Par ailleurs, le moteur de composition typographique a injecté le caractère Unicode de césure fantôme `\ufffe` dans une dizaine d'adresses Web de l'Annexe N, rompant les hyperliens lors du copier-coller.

## 1.4 Verdict global : RÉSERVE MAJEURE AVEC VICES BLOQUANTS D'OPPOSABILITÉ
Le Compendium constitue une œuvre d'une envergure conceptuelle remarquable et d'une lucidité rare. Néanmoins, en régime Production, **le segment terminal ne peut être certifié en l'état pour une exploitation en environnement prudentiel, juridique ou bancaire**. L'inaccessibilité des sources de 89,3 % du socle, l'aveu de non-rejouabilité des théorèmes pivots et la désynchronisation textuelle entre les chapitres et les annexes privent l'ouvrage du statut de preuve opposable formelle.

---

# 2. Évaluation détaillée Axe R2 : Appareil critique, cohérence et actualisation

## 2.1 Clôture de l'Annexe B (pp. 578-585, segment S54)
L'Annexe B consigne les 159 faits de référence ($S\text{-}001$ à $S\text{-}159$) qui forment le socle probatoire du Compendium :
- **Cardinalités par tome source** :
  - Volume II (*L'autonomie encadrée*) : 46 faits ($S\text{-}001$ à $S\text{-}046$).
  - Volume III (*L'entreprise agentique*) : 96 faits ($S\text{-}047$ à $S\text{-}142$).
  - Volume I (*Interopérabilité agentique*) : 17 faits ($S\text{-}143$ à $S\text{-}159$).
  - Total : $46 + 96 + 17 = 159$ faits. La continuité de la numérotation globale est respectée.

### 2.1.1 Dégradation épistémologique et circularité du Volume I ($S\text{-}143$ à $S\text{-}159$)
La vérification de la page 584 (lignes 53134 à 53202 de `DOCUMENT_TEXT_MAP.md`) révèle une rupture critique :
1. **Asymétrie de classement** : Alors que les faits des Volumes II et III comportent des entrées de niveau [A] (preuves vérifiées contradictoirement) et [B] (sources primaires ouvertes), **100 % des faits du Volume I ($S\text{-}143$ à $S\text{-}159$) sont dégradés au niveau [C]** (sources prospectives ou repérages internes non extraits).
2. **Transit systématique par le Volume III** : Aucune de ces 17 entrées ne possède d'ancrage direct et autonome ; elles sont toutes introduites via une clause d'héritage intermédiaire du Volume III (« par Vol. III H-xx §7.3 »).
3. **Aveu de non-rejouabilité sur les énoncés doctrinaux majeurs** :
   Les piliers théoriques sur lesquels s'appuie l'architecture de solutions de l'ouvrage sont officiellement marqués comme non rejouables :
   - **$S\text{-}153$ (p. 584, l. 53176-53178)** :  
     *« • S-153 — L'invariant à quatre termes. [C] — Vol. I, Synthèse §10.3, par Vol. III H-27 §7.3. Citation non rejouable. »*
   - **$S\text{-}154$ (p. 584, l. 53180-53182)** :  
     *« • S-154 — La délégation au-delà de deux sauts. [C] — Vol. I, Synthèse §11.5, par Vol. III H-28 §7.3. Citation non rejouable. »*
   - **$S\text{-}156$ (p. 584, l. 53188-53190)** :  
     *« • S-156 — Le plan de contrôle obligatoire. [C] — Vol. I, Synthèse §10.2, par Vol. III H-30 §7.3. Citation non rejouable. »*
   - **$S\text{-}158$ (p. 584, l. 53196-53198)** :  
     *« • S-158 — Le cas fil rouge. [C] — Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3, par Vol. III H-32 §7.3. Fait négatif non rejouable (cible supprimée). »*

**Diagnostic causal et impact juridique** :  
L'invariant transversal à quatre termes (*Découplage, Contrat, Évolution, Exploitation*, Ch. 1, p. 6) et la thèse de la rupture d'opposabilité dans la délégation au-delà de deux sauts ($A \to B \to C$, Ch. 17, pp. 189-195) sont présentés au lecteur comme des théorèmes démontrés et universels. Or, dans l'appareil critique officiel, ils se réduisent à des renvois circulaires vers des textes internes non versés au dépôt public et assortis de la mention « Citation non rejouable ». En audit légal et en droit de la preuve, une telle citation est frappée de nullité probatoire.

### 2.1.2 Citations fantômes in-text et exclusion de faits ($F\text{-}92$ et $F\text{-}96$)
L'analyse comparative entre l'Annexe B et le corps de l'ouvrage met au jour une divergence matérielle irréfutable :
- Dans l'Annexe B (pp. 583-584, lignes 53102-53128), la liste des faits du Volume III passe de $S\text{-}137$ (`Vol. III F-91 §7.11`) directement à $S\text{-}138$ (`Vol. III F-93 §7.11`). Le fait **`F-92` a été exclu du socle consolidé**. De même, $S\text{-}140$ (`Vol. III F-95 §7.11`) est immédiatement suivi de $S\text{-}141$ (`Vol. III F-97 §7.11`). Le fait **`F-96` a été exclu du socle consolidé**.
- **Preuve matérielle in-text** : Bien qu'exclus du socle pour « vote dû, non conduit », `Vol. III F-92` et `Vol. III F-96` continuent d'être cités et mobilisés dans le corps du livre comme arguments d'autorité technique aux chapitres 38, 39 et 40 :
  - *Ch. 39, p. 447 et p. 449* : *« ...ne référence qu’un nom d’agent lisible par un humain et un identifiant de modèle de requête (Vol. III F-92, [B, degré 1] ; ⚖ vote dû, non conduit). »* (présent 6 fois dans le corpus).
  - *Ch. 40, p. 463* : *« ...portant sur un ensemble d’agents (Vol. III F-96, [B, degré 1] ; ⚖ vote dû, non conduit). Fait négatif de degré 1... »* (présent 10 fois dans le corpus).
Cette discordance prouve que les faits ont été élagués de l'Annexe B lors d'une passe de clôture tardive sans que les renvois du texte principal n'aient été purgés.

### 2.1.3 Anomalies de la table d'héritage H et des faits F du Volume II
- **Volume II** : L'entrée $S\text{-}011$ renvoie à `Vol. II F-11 §7.4`, et $S\text{-}012$ saute directement à `Vol. II F-15 §7.6`. Les faits `F-12`, `F-13` et `F-14` (concernant la signature agent-agent v1.0.0 et la taxonomie des attaques MITRE AML) sont omis de l'Annexe B sans explication méthodologique, tout en étant cités dans le texte des chapitres 12 et 20. De plus, $S\text{-}021$ recourt à une numérotation non standardisée `Vol. II F-23b §7.5`.
- **Table d'héritage H** : Les identifiants $H\text{-}13$ et $H\text{-}16$ sont absents. L'identifiant $H\text{-}15$ est formellement défini au Ch. 43 (§ 43.3) comme une « construction d'auteur du Vol. II... n'entre pas au socle ». Pourtant, $H\text{-}15$ est cité à 7 reprises dans les chapitres d'architecture pour étayer des choix de conception.

---

## 2.2 Régime de non-consolidation de l'Annexe I.2 (p. 651, segment S59)
À la sous-section I.2, l'auteur expose les motifs de l'absence des sources des tomes II et III :
> *« ...les socles des Vol. II et III ne portent PAS leurs sources sous une forme reprenable. Le dépouillement des deux volumes rendait, le 30 juillet 2026, une seule adresse pour l’ensemble des deux volumes ; il n’en rend plus aucune à l'audit du 19 octobre 2026 ; leurs entrées F-xx citent leurs sources en prose et par leur nom — « lautorite.qc.ca », « Norton Rose Fulbright », « rapport annuel Desjardins 2025 » —, jamais par un identifiant résoluble. [...] La consolidation est structurellement asymétrique : le Vol. I fournit une bibliographie parce qu’il en tient une ; les deux autres n’en fournissent aucune parce qu’ils n’en tiennent pas. »* (lignes 59262 à 59278).

### 2.2.1 Réfutation formelle de l'argumentation d'auteur
1. **Tromperie sur l'intitulé de l'annexe** : L'en-tête général porte le titre formel *« Annexe I — Bibliographie générale consolidée »*. Présenter 66 pages de notices tout en excluant les sources de deux tomes sur trois constitue une asymétrie documentaire inacceptable.
2. **Effondrement de la vérifiabilité des livres réglementaires et prudentiels** :
   - Le Volume I (protocoles d'interopérabilité technique) bénéficie de 1 065 notices avec DOI, liens arXiv et références académiques.
   - Les Volumes II et III (qui traitent de la responsabilité civile, du mandat, de l'identité des agents, de la conformité prudentielle BSIF E-23, de la Loi 25 québécoise, des avis ACVM et des retours d'expérience bancaires) sont totalement dépourvus de références résolubles.
   - **Bilan arithmétique accablant** : Sur les 159 faits du socle, **142 faits (89,3 %)** ne disposent d'aucune adresse vérifiable dans l'Annexe I.
3. **Contradiction interne avec la doctrine d'opposabilité** : Tout au long des Livres II et V, l'auteur affirme que la traçabilité intégrale et l'auditabilité algorithmique sont des exigences non négociables. Tolérer que 9 faits de socle sur 10 ne puissent être vérifiés par un auditeur externe viole frontalement ce principe directeur. L'affirmation selon laquelle « une entrée [A] dont la source est nommée en prose reste une entrée [A] » est épistémologiquement insoutenable en audit réglementaire : la valeur d'une preuve dépend de sa reproductibilité immédiate.

---

## 2.3 Actualisation de clôture de l'Annexe N (pp. 652-663, segment S60)

### 2.3.1 Troncature du protocole de péremption du chapitre 50
Le paragraphe N.1 (p. 652, lignes 59334 à 59343) formule la décision suivante :
> *« Le § 50.3 prescrit trois gestes, dans cet ordre : constater le fait à sa source primaire et le consigner dans un rapport daté; amender l’entrée du socle (annexe B); reprendre ensuite les chapitres qui en dépendent. L’annexe accomplit le premier et s’arrête là : elle n’amende aucune entrée S-nnn et ne reprend aucun chapitre. Elle nomme les entrées et les chapitres que la reprise toucherait, de sorte qu’aucun chapitre ne soit corrigé avant son socle. »*

Cette décision engendre une scission textuelle à l'intérieur du volume :
- L'Annexe N relève avec une grande précision que certains faits sont modifiés ou périmés au 1ᵉʳ novembre 2026.
- En omettant les gestes 2 et 3, le Compendium publie un corps de texte devenu erroné ou obsolète, obligeant le lecteur à maintenir un registre mental d'amendements non fusionnés (*unmerged pull request*).

### 2.3.2 Désynchronisations doctrinales directes entre chapitres et annexes
1. **Évolution du protocole A2A (Ch. 8 / S-002 vs Annexe N.2/N.4)** :
   Le corps du texte (Ch. 8 et fait $S\text{-}002$) affirme qu'au 29 octobre 2026, aucun mouvement n'a eu lieu sur A2A. L'Annexe N ([AN-6], p. 662) consigne pourtant que l'étiquette `v1.1.0-rc` a été publiée le 29 octobre 2026 à 12 h 05 UTC sur le dépôt officiel. Le chapitre 8 n'a pas été révisé.
2. **Transition post-quantique du NIST (Ch. 21 vs Annexe N.2 [AN-14])** :
   Le Chapitre 21 (pp. 236-251) traite le rapport NIST IR 8547 comme un projet de travail préliminaire non arrêté. L'Annexe N ([AN-14], p. 662) consigne la parution de la version finale officielle le 27 octobre 2026, actant l'interdiction de tout algorithme à clé publique vulnérable au quantique après 2035. Le chapitre 21 n'a pas été mis à jour.
3. **Ligne directrice IA de l'AMF (Ch. 27 et 42 vs Annexe N.1 [AN-1])** :
   Le Chapitre 27 (§ 27.1, § 27.3) et le Chapitre 42 (§ 42.3.1) qualifient la réglementation québécoise de l'AMF de « vide de socle » non instruit. L'Annexe N.1 incorpore pourtant les conclusions de la *Note AMF IA* du 31 octobre 2026 (CRE-IA-2026-01-QC) détaillant les 41 attentes de l'autorité financière. Les chapitres 27 et 42 n'ont pas été synchronisés.
4. **Obligation de marquage synthétique de l'AI Act (Ch. 30 vs Annexe N.4 [AN-25])** :
   Le Chapitre 30 (pp. 335-349) annonce que les obligations de marquage des contenus synthétiques entreront en vigueur le 2 décembre 2026. L'Annexe N.4 (p. 661 et [AN-25]) note que la Commission européenne applique les règles de transparence dès août 2026 (conformément à l'Article 50 du Règlement sur l'IA). Cette divergence expose une organisation à un risque sérieux de non-conformité juridique.
5. **Supervision de l'Open Banking canadien (Ch. 32 vs Notice [749] p. 631)** :
   La Notice [749] de l'Annexe I.1 consigne avec exactitude que la *Loi sur la banque axée sur le consommateur* (CDBA, 2026 ch. 3, art. 246, sanctionnée le 26 mars 2026) a confié la supervision du système à la **Banque du Canada**. Le Chapitre 32 (p. 367) et la Table des symboles (p. 184) maintiennent de façon obsolète que cette autorité est l'**Agence de la consommation en matière financière du Canada (FCAC/ACFC)**.
6. **Métamodèle d'architecture ArchiMate (Ch. 43-44 vs Notices [920]-[921] p. 642)** :
   Les notices bibliographiques 920 et 921 enregistrent la publication d'ArchiMate 4 (C260) par The Open Group le 27 avril 2026, spécifiant qu'elle remplace ArchiMate 3.2 (C226) et abandonne le découpage rigide en couches au profit de domaines pairs. Pourtant, l'intégralité des modélisations formelles du Livre IV (Ch. 43 et 44) est adossée au modèle à 7 couches d'ArchiMate 3.2.

### 2.3.3 Disponibilité des dépôts et inopposabilité formelle (p. 661)
À la page 661 (lignes 60766-60768 de `DOCUMENT_TEXT_MAP.md`), l'Annexe N concède que les sources des Volumes I à III demeurent « absentes du dépôt » :
> *« • Les autres entrées à sensibilité temporelle du socle que cette annexe ne nomme pas, et les renvois aux volumes I à III, absents du dépôt. »*

Cette rétention des dépôts sources empêche tout auditeur externe de rejouer la chaîne de dérivation reliant les données brutes aux énoncés finaux.

---

# 3. Vérification bibliographique et état de l'art Axe R3

## 3.1 Bilan de la vérification croisée des sources
L'audit croisé confirme l'authenticité matérielle des textes légaux, réglementaires et académiques récents cités dans le Volume I :
- *Textes normatifs et juridiques* : Décret présidentiel américain EO 14412 du 22 juin 2026 sur la cryptographie post-quantique (Notice [923], p. 642) ; loi américaine GENIUS Act PL 119-27 du 18 juillet 2025 sur les stablecoins (Notice [944], p. 644) ; standard IETF RFC 9901 sur SD-JWT (`DOI:10.17487/RFC9901`, Notice [297], p. 604).
- *Articles scientifiques 2024-2026* : Anbiaee et al. (`arXiv:2602.11327`) sur la modélisation des menaces MCP/A2A ; Bhardwaj (`arXiv:2602.22302`) sur les contrats comportementaux ; Cemri et al. (`arXiv:2503.13657`, NeurIPS 2025) sur les défaillances multi-agents ; Chen et al. (`arXiv:2604.07695`) sur le protocole AITH ; DeepSeek-R1 (`Nature` vol. 645, 2025) ; Sun & Evans (`arXiv:2603.02451`) sur l'attestation composable ; Tibebu & Shemtaga (`arXiv:2604.07778`) sur l'horizon de responsabilité.

## 3.2 Bogue de mise en page et incohérence arithmétique de la page 585
À la page 585 (lignes 53264 à 53275 et image `page-585.png`), le tableau récapitulatif du dédoublonnage de l'Annexe I présente une rupture flagrante :
```text
Mesure                                                      Valeur
Entrées relevées aux sept bibliographies du Vol. I          1263
Doublons fondus par identifiant normalisé                   [cellule vide]
Entrées uniques de la présente annexe                       [cellule vide]
Adresses primaires reprises des socles des Vol. II et III   0
• 134 1065
```
1. **Éjection typographique** : Les cellules correspondant aux doublons et aux entrées uniques sont vides ; les entiers `134` et `1065` ont été expulsés hors de la table sous la forme d'une puce orpheline textuelle `• 134 1065`.
2. **Incohérence mathématique** : Si 1 263 entrées brutes ont été collectées et que 134 doublons ont été fondus, le total d'entrées uniques doit être égal à :
   $$1\,263 - 134 = 1\,129 \neq 1\,065$$
   Il existe un déficit inexpliqué de **64 entrées** ($1\,129 - 1\,065 = 64$) éliminées sans traçabilité. Inversement, si le nombre d'entrées uniques de l'Annexe I.1 est bien de 1 065, le nombre réel de doublons éliminés est de :
   $$1\,263 - 1\,065 = 198 \neq 134$$

## 3.3 Faillite empirique du dédoublonnage en Annexe I.1
Alors que la page 585 prétend qu'un dédoublonnage par identifiant ou signature a été appliqué, l'inspection automatisée et visuelle du corpus de 1 066 notices révèle un échec complet de l'algorithme de déduplication, qui n'a éliminé que les chaînes d'URL strictement identiques au caractère près :
1. **Triplicatas consécutifs documentés** :
   - *IETF OAuth 2.1* (pp. 610-611, lignes 55558-55580) : Trois notices consécutives pour la spécification `draft-ietf-oauth-v2-1-15` (variations mineures dans le libellé des éditeurs : « Hardt, D. (ed.) », « Hardt, D. ; Parecki, A. (Eds.) »).
   - *Aim Security / EchoLeak CVE-2025-32711* (p. 587, lignes 28449-28459) : Trois notices contiguës pour la même vulnérabilité d'injection prompt dans Microsoft 365 Copilot (Aim Labs divulgation, Aim Labs prépublication arXiv, Aim Security avis de sécurité).
2. **Quadruplicata IETF WIMSE (p. 613, lignes 55796-55815)** :
   Quatre notices pour l'architecture `draft-ietf-wimse-arch-07`, dont deux notices strictement identiques au mot près (`IETF WIMSE Working Group — Salowey, J. et al.`).
3. **Plus de 50 paires de doublons textuels stricts non fondus** :
   - *Anthropic MCP* (p. 588, lignes 28520 et 28522) : Double citation consécutive du billet de lancement du 25 novembre 2024.
   - *Aldasoro et al. BIS WP 1194* (p. 587, lignes 28468 et 28471) : Même document de travail de la BRI sur les banques et l'IA.
   - *Courtney et al. ANS v2* (p. 599, lignes 29046 et 29049) : Même brouillon IETF du 13 avril 2026.
   - *Temporal Platform Documentation* (p. 641, lignes 58354 et 58356) : Double entrée consécutive.
   - *NIST AI RMF 1.0 (NIST AI 100-1)* (p. 627, lignes 57072 et 57076) et *NIST GenAI Profile (AI 600-1)* (p. 627, lignes 57082 et 57086) : Doublons sous deux graphies différentes (« NIST » vs « NIST, U.S. Dept. of Commerce »).
   - *OWASP Top 10 for Agentic Applications* (pp. 630-631, lignes 57390 et 57414) : Double notice consécutive.
   - *Willison Lethal Trifecta* (p. 647, lignes 58894 et 58898) : Même billet du 16 juin 2025.
   - *World Economic Forum Future of Jobs* (p. 647, lignes 58932 et 58938) : Même rapport.
   - *Doublons distants avec graphies divergentes* : W3C VCDM 2.0 cité sous `Sporny et al.` (p. 640) et sous `W3C VC WG` (p. 646) ; Trulioo KYA (Notices [935] et [936], p. 643) ; Federal Reserve SR 11-7 (sous `Board of Governors` p. 593 et sous `Federal Reserve` p. 604).

## 3.4 Inventaire exhaustif des directives internes de rédaction non purgées
L'assemblage semi-automatisé a laissé subsister au sein des notices bibliographiques finales 8 fragments manifestes de consignes de rédaction, notes d'arbitrage et directives de relecture destinées à l'auteur :
1. **Notice [980] — Wang, Tolk, Wang (p. 646, lignes 58814-58816)** :  
   `...cf. §6.10 (ancrage primaire ; à conserver ici uniquement pour la transposition LCIM → plateaux/agents, sinon renvoi ch. 1-5)`  
   *Preuve* : Directive d'arbitrage de l'auteur sur la conservation de la notice LCIM imprimée verbatim dans le texte public.
2. **Notice [729] — OSFI/BSIF (p. 630, lignes 57358-57360)** :  
   `OSFI/BSIF (2023/2024). Lignes directrices B-10 (Third-Party Risk Management) et B-13 (Technology and Cyber Risk Management). Voir §2.5 ci-dessus. — cf. §5.6, §5.11`  
   *Preuve* : « Voir §2.5 ci-dessus » résulte d'un copier-coller brut d'une note de bas de page de chapitre.
3. **Notice [880] — South et al. / OpenID Foundation (p. 640, lignes 58238-58240)** :  
   `...[Whitepaper OpenID et sa prépublication arXiv sont le même document ; entrée unique, cf. cat. 4 fusionnée ici.]`  
   *Preuve* : Note de régie de compilation interne insérée entre crochets.
4. **Notice Finastra (p. 605, lignes 55068-55072)** :  
   `...Raison de l’écart : URL non confirmée par recherche, slug ne correspondant pas exactement au titre annoncé, page Viewpoints non datée et susceptible de changer. À sur le site Finastra et à citer avec date de consultation avant tout usage en §5.7/§5.11.`  
   *Preuve* : Mémo d'investigation non résolu contenant la formulation tronquée « À sur le site Finastra ».
5. **Notice Yuan, Dun et al. (p. 650, lignes 59158-59160)** :  
   `arXiv:2604.02369. [Prépublication : fixer le numéro de version arXiv au moment de citer.]`  
   *Preuve* : Consigne technique de gel de version arXiv oubliée entre crochets.
6. **Notice Sparx Systems (p. 640, ligne 58244)** :  
   `...IA conversationnelle via tiers, ex. Kernaro AI, à dater`  
   *Preuve* : Directive de vérification temporelle « à dater » intégrée dans la notice.
7. **Notice EBA (p. 602, ligne 54782)** :  
   `...consultation close 8.10.2025 ; version finale à confirmer`  
   *Preuve* : Consigne de veille juridique « version finale à confirmer » imprimée dans le texte distribué.
8. **Notice OpenAI / Morgan Stanley (p. 628, ligne 57196)** :  
   `...— cf. §5.10, §5.11, §5.12.2 à revérifier`  
   *Preuve* : Annotation éditoriale « à revérifier » non purgée.

## 3.5 Analyse du bogue de césure Unicode `\ufffe` et corruption d'URL
1. **Caractère parasite `\ufffe` dans l'Annexe N (pp. 662-663)** :  
   Lors de la coupure de fin de ligne dans les URL de l'Annexe N, le moteur de composition typographique a inséré le caractère Unicode `\ufffe` (non-caractère / marque d'inversion d'octet) :
   - `[AN-11]` : `https://datatracker.ietf.org/wg/wimse/documents/` (coupure sur `docu\ufffements`).
   - `[AN-14]` : `https://csrc.nist.gov/pubs/ir/8547/final` (coupure sur `oc\ufffetobre`).
   - `[AN-15]` : `...guideline-e\ufffe23-model-risk-management-2027` (tiret d'URL transformé en `\ufffe`).
   - `[AN-23]` : `https://datatracker.ietf.org/doc/draft\ufffeietf-oauth-v2-1/`.
   - `[AN-24]` : `draft-chen-oauth\ufffeagent-revocation` et `draft-sweeney-wimse-credential-delegation`.
   - `[AN-25]` : `regulatory\ufffeframework-ai`.
   - `[AN-27]` : `dé\ufffemocratie à l’ère numérique` dans l'URL du PDF de la CAI Québec.  
   Ce caractère brise la résolution hypertexte lors d'un copier-coller dans un navigateur Web ou un script d'audit automatisé.
2. **Espaces parasites dans l'Annexe I.1** :  
   De multiples URL et DOI de l'Annexe I comportent des espaces blancs injectés après le point ou le tiret : `https://www. consumerfinance.gov/` (p. 595), `https://www. osfi-bsif.gc.ca/` (p. 630), `https://docs. pactflow.io/` (p. 639), `https://docs. temporal.io/` (p. 641), `DOI 10.6028/NIST.SP.800- 207A` (p. 595).

---

# 4. Matrice complète des défauts classés par sévérité

| ID Défaut | Sévérité | Localisation exacte | Description & Citation textuelle | Diagnostic causal | Correctif explicite ou contre-exemple formel |
|---|---|---|---|---|---|
| **DEF-ANNEX-01** | **Bloquant** | Annexe B, p. 584, entrées S-153, S-154, S-156, S-158 (lignes 53176-53198) | *« S-153 — L'invariant à quatre termes... Citation non rejouable »* ; *« S-154 — La délégation au-delà de deux sauts... Citation non rejouable »* ; *« S-156 — Le plan de contrôle obligatoire... Citation non rejouable »* ; *« S-158 — Le cas fil rouge... Fait négatif non rejouable (cible supprimée) »*. | Les principes architecturaux et théoriques pivots du Compendium sont adossés à des synthèses internes privées du Volume III déclarées impossibles à reproduire. | Remplacer ces renvois auto-référentiels par des démonstrations mathématiques formelles publiées en annexe ouverte et des références scientifiques indépendantes (RFC 8693, Chen et al. AITH 2026). |
| **DEF-ANNEX-02** | **Bloquant** | Annexe I.2, p. 651 (lignes 59260-59300) | *« ...les socles des Vol. II et III ne portent PAS leurs sources sous une forme reprenable [...] La consolidation est structurellement asymétrique : le Vol. I fournit une bibliographie parce qu’il en tient une ; les deux autres n’en fournissent aucune... »*. | Rupture d'opposabilité prudentielle : 89,3 % des faits du socle ($S\text{-}001$ à $S\text{-}142$, couvrant la responsabilité, l'identité d'agent et BSIF E-23) sont privés d'adresses résolubles (DOI/URL). | Rétro-annoter les sources primaires des 142 faits des Volumes II et III et publier une véritable sous-section consolidée intégrant leurs identifiants pérennes. |
| **DEF-ANNEX-03** | **Bloquant** | Annexe N, p. 652 (§ N.1, lignes 59334-59343) | *« Le § 50.3 prescrit trois gestes, dans cet ordre : constater [...] amender [...] reprendre [...]. L’annexe accomplit le premier et s’arrête là : elle n’amende aucune entrée S-nnn et ne reprend aucun chapitre. »*. | Troncature volontaire du protocole de péremption laissant coexister dans le même volume un corps de texte obsolète contredit par son annexe de clôture. | Exécuter formellement les gestes 2 et 3 : créer les fiches amendées dans l'Annexe B et insérer les papillons ou renvois de mise à jour dans les chapitres touchés (Ch. 8, 21, 27, 30, 32, 42, 44). |
| **DEF-ANNEX-04** | **Bloquant** | Livre III, Ch. 30 (pp. 335-349) vs Annexe N.4 (p. 661 et [AN-25] p. 663) | Le Ch. 30 fixe l'obligation de marquage des contenus synthétiques au **2 décembre 2026**, contredit par l'Annexe N.4 rappelant que la Commission européenne applique l'obligation de transparence dès **août 2026** (Art. 50 AI Act). | Mauvaise interprétation du calendrier échelonné de l'AI Act dans le Livre III non corrigée lors de la rédaction de l'Annexe N. Risque de non-conformité légale sévère. | Aligner immédiatement le Chapitre 30 sur l'Article 50 du Règlement européen sur l'IA en fixant l'échéance de conformité à août 2026. |
| **DEF-ANNEX-05** | **Majeur** | Annexe I, p. 585 (lignes 53264-53275) et image `page-585.png` | **Tableau tronqué et puce orpheline** : Cellules vides pour « Doublons fondus » et « Entrées uniques » ; puce isolée `• 134 1065`. Arithmétique fausse : $1\,263 - 134 = 1\,129 \neq 1\,065$ (écart inexpliqué de 64 entrées). | Débordement de boîte lors de la composition typographique éjectant les entiers hors du tableau ; formule de calcul inexacte ($1263 - 1065 = 198 \neq 134$). | Réinsérer `198` dans la cellule « Doublons fondus », `1065` dans « Entrées uniques », et supprimer la ligne orpheline `• 134 1065`. |
| **DEF-ANNEX-06** | **Majeur** | Annexe B, pp. 583-584 vs Livre IV, Ch. 38, 39, 40 (pp. 438, 447, 449, 463) | **Citations fantômes in-text** : `Vol. III F-92` et `Vol. III F-96` sont sautés et exclus de l'Annexe B, mais cités à 16 reprises dans le texte comme arguments d'autorité technique (`Vol. III F-92, [B, degré 1] ; ⚖ vote dû, non conduit`). | Élagage tardif de faits en Annexe B sans nettoyage correspondant des renvois in-text dans les chapitres d'AgentOps. | Réintégrer formellement F-92 et F-96 dans l'Annexe B (portant le Vol. III à 98 faits) ou purger leurs citations d'autorité aux chapitres 38 à 40. |
| **DEF-ANNEX-07** | **Majeur** | Annexe I.1, pp. 587, 588, 599, 610-613, 627, 630-631, 641, 647 | **Échec patent du dédoublonnage** : Triplicatas (OAuth 2.1 pp. 610-611, EchoLeak p. 587) ; quadruplicata IETF WIMSE (p. 613) ; plus de 50 paires de doublons stricts contigus (Anthropic MCP, Courtney ANS v2, NIST AI RMF, etc.). | Algorithme de déduplication primaire comparant uniquement les URL identiques au caractère près sans analyse sémantique des titres ni des variantes d'auteurs. | Réexécuter un script de dédoublonnage sémantique flou (distance de Levenshtein < 0,1 sur titre et auteurs normalisés) et actualiser le compteur d'entrées uniques. |
| **DEF-ANNEX-08** | **Majeur** | Annexe I.1, p. 602, 605, 628, 630, 640, 646, 650 | **Fuite de directives internes de travail** : *« (ancrage primaire ; à conserver ici uniquement pour...) »* (p. 646) ; *« Voir §2.5 ci-dessus »* (p. 630) ; *« [Whitepaper OpenID... entrée unique] »* (p. 640) ; *« À sur le site Finastra »* (p. 605) ; *« [fixer le numéro de version] »* (p. 650) ; *« à revérifier »* (p. 628). | Assemblage semi-automatisé n'ayant pas filtré les consignes éditoriales entre crochets, parenthèses ou fragments collés depuis les notes de chapitres. | Effectuer une passe de nettoyage éditorial systématique par expressions régulières pour supprimer toutes les directives internes des notices bibliographiques. |
| **DEF-ANNEX-09** | **Majeur** | Annexe I.1, p. 631 (Notice [749]) vs Livre III, Ch. 32 (p. 367) et Table des symboles (p. 184) | **Contradiction réglementaire sur la supervision de l'Open Banking (CDBA)** : La Notice [749] consigne le transfert à la Banque du Canada sous la CDBA 2026 ch. 3, alors que le Ch. 32 maintient la FCAC. | Absence de relecture transversale entre les notices ajoutées en 2026 et le corps doctrinal du Livre III. | Aligner le Chapitre 32 et la table des symboles sur la Notice [749] en désignant la Banque du Canada comme autorité de supervision de la CDBA. |
| **DEF-ANNEX-10** | **Majeur** | Annexe I.1, p. 642 (Notices [920]-[921]) vs Livre IV, Ch. 43 et 44 (pp. 495-506) | **Obsolescence du métamodèle architectural formel** : Les notices 920-921 actent la publication d'ArchiMate 4 (C260, avril 2026) supprimant les couches, tandis que le Ch. 44 repose sur les 7 couches rigides d'ArchiMate 3.2. | Introduction d'ArchiMate 4 en bibliographie sans mise à niveau des diagrammes et chapitres d'architecture d'entreprise. | Ajouter une note de cadrage au Ch. 44 documentant la transition vers ArchiMate 4 et justifiant le maintien transitoire du métamodèle 3.2. |
| **DEF-ANNEX-11** | **Majeur** | Annexe N, p. 661 (lignes 60766-60768) | **Inopposabilité formelle par rétention des volumes sources** : *« et les renvois aux volumes I à III, absents du dépôt. »*. | Choix de diffusion restreinte conservant les monographies sources I, II et III hors de la portée des relecteurs externes et du public. | Verser les fichiers sources ou des extraits d'audit vérifiables des Volumes I, II et III dans un répertoire public d'archive du dépôt Git. |
| **DEF-ANNEX-12** | **Majeur** | Annexe I.1, p. 640 (Notices [892] et [893]) | **Collision lexicale et duplication contradictoire sur Stripe MPP** : *« [892] Merchant Payments Protocol »* vs *« [893] Machine Payments Protocol »*. | Erreur lexicale d'attribution combinée à une duplication de notice sur le protocole Stripe/Tempo. | Supprimer la notice erronée [892] et consolider les données dans la notice [893] sous l'intitulé officiel *Machine Payments Protocol*. |
| **DEF-ANNEX-13** | **Majeur** | Annexe N.4, p. 661 (lignes 60750-60778) et Ch. 50 (§ 50.2) | **Angle mort structurel sur les runtimes et abandon de la frise prudentielle § 49.1** : La couche d'exécution (runtimes Wasm, conteneurs) est exclue de la revalidation, et les 8 jalons prudentiels 2026-2028 sont laissés non instruits. | Définition trop restrictive du périmètre de revalidation du Tableau 50.1 ayant exclu les composants logiciels et le balayage prudentiel. | Ajouter une ligne dédiée aux environnements d'exécution dans le Tableau 50.1 et conduire le balayage documentaire des échéances de Bâle III et du BSIF. |
| **DEF-ANNEX-14** | **Mineur** | Annexe N, pp. 662-663 ([AN-7, 8, 11, 14, 15, 23, 24, 25, 27]) | **Corruption des hyperliens par césure Unicode `\ufffe`** : Ex. `draft\ufffeietf-oauth-v2-1`, `guideline-e\ufffe23`, `dé\ufffemocratie`. | Insertion automatique du caractère non imprimable `\ufffe` par le moteur typographique lors des césures d'URL. | Recompiler le document avec une règle désactivant les césures automatiques au sein des blocs d'URL et d'identifiants pérennes. |
| **DEF-ANNEX-15** | **Mineur** | Annexe I.1, p. 631 (Notice Tempo) et p. 651 (Notice [1064] Zinnia) | **Troncation mécanique sur la préposition orpheline « à »** : *« ...cf. §5.9, §5.11, §5.12.2 à »* (l. 59250) et *« ...cf. §5.7, §5.13 à »* (l. 57452). | Coupure de fin de chaîne lors de l'extraction des renvois internes sous Typst/LaTeX. | Compléter les références de paragraphes manquantes ou supprimer la préposition orpheline « à ». |
| **DEF-ANNEX-16** | **Mineur** | Annexe I.1, pp. 639-650 (Notices [876], [877], [921], [1006], [1048], [1054]) | **Absence d'espace après le point fermant de l'année** : `(2026).The`, `(2026).TraderBench`, `(2024).A Multimodal`, `(2026).Workload`. | Concaténation textuelle défectueuse sans séparateur d'espace lors du formatage automatique des notices. | Insérer un espace standard entre le point de fermeture de l'année et le premier mot du titre. |
| **DEF-ANNEX-17** | **Mineur** | Annexe B, p. 584, entrée S-158 (lignes 53196-53198) | **Coquille syntaxique et concaténation brute** : *« Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 »*. | Concaténation de deux champs de métadonnées avec duplication du terme « Annexe B ». | Nettoyer la chaîne pour lire : *« Vol. I, Monographie, Annexe B ; Architecture de solutions §7.4.3 »*. |
| **DEF-ANNEX-18** | **Mineur** | Annexe N.4, p. 661 (lignes 60770-60774) | **Brouillons IETF au statut « Replaced » non actualisés** : Maintien de références obsolètes (`draft-meunier-web-bot-auth-architecture-05`, `draft-mozleywilliams-dnsop-bandaid-00`). | Inscription verbatim des notices de l'Annexe I sans actualisation vers les spécifications qui leur ont succédé à l'IETF. | Mettre à jour les notices avec les identifiants actifs ayant remplacé ces brouillons au registre IETF. |

---

# 5. Liste consolidée des travaux fondamentaux et standards omis jusqu'en 2026

L'analyse épistémologique du Compendium révèle un paradoxe structural : l'ouvrage fait preuve d'une hyper-spécialisation sur les prépublications arXiv de 2024-2026 et les spécifications industrielles émergentes, mais souffre d'un vide presque total concernant la littérature fondatrice évaluée par les pairs dans les grandes conférences d'informatique théorique, de systèmes distribués et de sécurité (STOC, FOCS, SOSP, OSDI, ACM CCS, IEEE S&P).

Pour conférer au Compendium l'assise académique et prudentielle indispensable à un traité d'entreprise de 663 pages, les vingt travaux majeurs suivants doivent être intégrés :

### 5.1 Systèmes distribués, consensus et cohérence d'état (SOSP / OSDI / CIDR / CACM)
1. **Lamport, Leslie (1978 & 1998)** :
   - *Time, Clocks, and the Ordering of Events in a Distributed System*. *Communications of the ACM*, 21(7), pp. 558-565.
   - *The Part-Time Parliament (Paxos)*. *ACM Transactions on Computer Systems*, 16(2), pp. 133-169.
   - *Impact & Justification* : Fondement universel de l'ordonnancement d'événements stochastiques et de la cohérence de mémoire distribuée entre agents asynchrones (indispensable aux Ch. 6, 10 et 48).
2. **Castro, Miguel & Liskov, Barbara (1999)** :
   - *Practical Byzantine Fault Tolerance (PBFT)*. In *Proc. of the 3rd USENIX OSDI '99*, pp. 173-186.
   - *Impact & Justification* : Socle théorique obligatoire pour régir la tolérance aux pannes byzantines dans les essaims d'agents et neutraliser les agents corrompus ou compromis (Ch. 6 et Ch. 20).
3. **Ongaro, Diego & Ousterhout, John (2014)** :
   - *In Search of an Understandable Consensus Algorithm (Raft)*. In *Proc. of USENIX ATC '14*, pp. 305-319.
   - *Impact & Justification* : Algorithme de consensus pratique universellement utilisé pour assurer la réplication d'état des registres d'agents et des orchestrateurs.
4. **Corbett, James C. et al. (2012)** :
   - *Spanner: Google’s Globally-Distributed Database*. In *Proc. of OSDI '12* / *ACM TOCS*, 31(3), pp. 8:1-8:22.
   - *Impact & Justification* : Référence canonique sur les horloges synchronisées (TrueTime) et les transactions distribuées cohérentes, incontournable pour confronter le paradigme Saga exposé au Ch. 48.
5. **Helland, Pat & Campbell, Dave (2009)** :
   - *Building on Quicksand*. In *Proc. of the 4th Biennial CIDR '09*.
   - *Impact & Justification* : Démonstration séminale de l'impossibilité des transactions ACID traditionnelles dans les systèmes autonomes hautement distribués et justification formelle des mécanismes de compensation.

### 5.2 Sécurité formelle, moniteurs de référence et identité de production (TISSEC / CCS / CNCF)
6. **Schneider, Fred B. (2000)** :
   - *Enforceable Security Policies*. *ACM Transactions on Information and System Security (TISSEC)*, 3(1), pp. 30-50.
   - *Impact & Justification* : **Omission théorique la plus grave du Livre II**. Fred Schneider démontre mathématiquement la frontière exacte de ce qu'un moniteur de référence peut appliquer à l'exécution (propriétés de sûreté / *safety*) et ce qui est indécidable (propriétés de vivacité / *liveness*). Cette distinction est essentielle pour valider ou réfuter formellement le « Théorème de Décidabilité des Politiques » formulé au Ch. 48.
7. **Birgisson, Arnar ; Politz, Joe Gibbs ; Erlingsson, Úlfar et al. (2014)** :
   - *Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud*. In *Proc. of ACM CCS '14*, pp. 304-319.
   - *Impact & Justification* : Modèle cryptographique fondateur de l'atténuation de jetons sans état et de la délégation décentralisée à preuve contextuelle (au cœur des protocoles examinés aux Ch. 12 à 17).
8. **CNCF / SPIFFE Project (2020-2026)** :
   - *Secure Production Identity Framework for Everyone (SPIFFE) & SPIFFE Runtime Environment (SPIRE) Specification*. Standard gradué CNCF.
   - *Impact & Justification* : **Standard industriel de référence mondial** déployé en production pour l'identité cryptographique non-humaine et l'attestation dynamique de charges de travail (X.509 SVID). Alors que le Compendium cite abondamment le projet émergent IETF WIMSE (4 notices p. 613), l'omission totale de SPIFFE/SPIRE en bibliographie affaiblit la crédibilité industrielle de l'ouvrage.

### 5.3 Régulation prudentielle financière et résilience opérationnelle
9. **BSIF / OSFI — Ligne directrice E-21 sur la résilience opérationnelle (Août 2024)** :
   - Bureau du surintendant des institutions financières (2024). *Ligne directrice E-21 : Gestion du risque opérationnel et résilience opérationnelle*. Ottawa : BSIF (version finale publiée le 22 août 2024).
   - *Impact & Justification* : **Omission réglementaire canadienne la plus critique de l'ouvrage**. Le Compendium analyse B-10 (Tiers), B-13 (Cyber/TI) et E-23 (Risque de modèle). Or, le BSIF a conçu la ligne directrice E-21 comme le pivot obligeant les institutions financières à définir des « tolérances aux perturbations » critiques. Le déploiement d'agents autonomes en environnement bancaire (Ch. 31 à 35) tombe directement sous le champ d'application d'E-21.
10. **OICV / IOSCO — Rapport sur l'intelligence artificielle sur les marchés de capitaux (2024-2025)** :
    - International Organization of Securities Commissions (2024/2025). *Artificial Intelligence in Capital Markets: Governance, Integrity and Conduct Risks*. Madrid : IOSCO.
    - *Impact & Justification* : Organisme normatif mondial dont l'ACVM est membre. Complément indispensable pour encadrer les agents de négociation et de conseil automatisé (Ch. 28 et Ch. 34).
11. **Banque des règlements internationaux (BRI / BIS) (2024)** :
    - *Artificial intelligence and the financial system: revolution or evolution?* BIS Annual Economic Report 2024, Chapitre III, Bâle.
    - *Impact & Justification* : Rapport macro-prudentiel mondial sur les risques d'instabilité financière induits par les décisions algorithmiques corrélées.
12. **Banque du Canada (2025)** :
    - *Macrofinancial Implications of Generative AI in the Canadian Financial Ecosystem*. Bank of Canada Staff Analytical Note, Ottawa.
    - *Impact & Justification* : Analyse de la banque centrale du pays d'ancrage principal du Compendium sur les canaux de transmission des risques d'IA.

### 5.4 Runtimes d'inférence, gestion de mémoire et architectures d'exécution (SOSP / NeurIPS / FAST)
13. **Kwon, Woosuk ; Li, Zhuohan ; Zhuang, Siyuan et al. (2023)** :
    - *Efficient Memory Management for Large Language Model Serving with PagedAttention*. In *Proc. of the 29th ACM SOSP '23*, pp. 611-626. DOI: `10.1145/3600006.3613165`.
    - *Impact & Justification* : Bien que la notice produit *vLLM (2026)* figure à la p. 638, l'article fondateur de SOSP 2023 est omis. PagedAttention constitue le socle algorithmique indispensable pour gérer la mémoire KV-cache dans les systèmes multi-agents concurrents.
14. **Zheng, Lianmin ; Yin, Liangsheng ; Xie, Zhiqiang et al. (2024)** :
    - *SGLang: Efficient Execution of Structured Language Model Programs*. In *NeurIPS 2024* / arXiv:2312.07104.
    - *Impact & Justification* : SGLang a introduit *RadixAttention* (réutilisation du KV-cache sur les arbres de prompts partagés), devenu le standard de l'industrie en 2025-2026 pour optimiser l'exécution des graphes d'agents chaînés.
15. **Qin, Y. et al. (2025)** :
    - *Mooncake: A KVCache-Centric Disaggregated Architecture for LLM Serving*. In *USENIX FAST '25* / arXiv:2407.00079.
    - *Impact & Justification* : Architecture désagrégée séparant le calcul et la mémoire KV-cache pour le traitement d'agents à très grande échelle.

### 5.5 Sécurité agentique offensive/défensive, logique et théorie des jeux (USENIX Security / NeurIPS / FOCS)
16. **Cohen, Stav ; Bitton, Ron ; Nassi, Ben (2024)** :
    - *Here Comes The AI Worm: Unleashing Zero-Click Worms that Target GenAI-Powered Applications (Morris II)*. arXiv:2403.02817.
    - *Impact & Justification* : Première démonstration d'un ver informatique zéro-clic s'autorépliquant entre agents connectés via RAG. Lacune majeure du Chapitre 11 sur les risques protocolaires.
17. **Chen, Z. ; Xiang, Z. ; Xiao, C. ; Song, D. ; Li, B. (2024)** :
    - *AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases*. In *NeurIPS 2024* / arXiv:2407.12784.
    - *Impact & Justification* : Référence à NeurIPS 2024 établissant la première attaque par porte dérobée sans réentraînement ciblant la mémoire épisodique des agents RAG avec un taux d'efficacité supérieur à 80 %.
18. **Chen, S. ; Piet, J. ; Sitawarin, C. ; Wagner, D. (2025)** :
    - *StruQ: Defending Against Prompt Injection with Structured Queries*. In *Proc. of 34th USENIX Security Symposium (USENIX Security '25)*.
    - *Impact & Justification* : Solution architecturale de pointe isolant le canal de contrôle du canal de données face aux injections de prompts indirectes (Ch. 11 et 19).
19. **Alur, Rajeev ; Henzinger, Thomas A. ; Kupferman, Orna (1997/2002)** :
    - *Alternating-time Temporal Logic (ATL)*. In *Proc. of 38th FOCS '97* / *Journal of the ACM*, 49(5), pp. 672-713.
    - *Impact & Justification* : Logique temporelle formelle standard permettant de vérifier mathématiquement les propriétés stratégiques et les capacités de coalitions d'agents autonomes.
20. **Nisan, Noam ; Roughgarden, Tim ; Tardos, Éva ; Vazirani, Vijay (2007)** :
    - *Algorithmic Game Theory*. Cambridge University Press.
    - *Impact & Justification* : Traité de référence nécessaire pour formaliser les mécanismes d'incitation, les topologies de marché d'agents et la prévention des collusions stochastiques (Ch. 6).

---

# 6. Recommandations prioritaires pour la méta-synthèse globale (`DEEP_REVIEW_COMPENDIUM.md`)

Pour le document de synthèse générale de l'audit de l'œuvre, six recommandations d'action doivent être retenues :

1. **Lever les vices bloquants d'opposabilité de l'Annexe B** :
   Imposer la révision de la page 584 pour éliminer les mentions « Citation non rejouable » sur les faits pivots $S\text{-}153$, $S\text{-}154$ et $S\text{-}156$, en publiant des preuves formelles autonomes en annexe mathématique ou en adossant ces énoncés à la littérature ouverte.
2. **Résoudre l'asymétrie documentaire de l'Annexe I.2** :
   Proscrire le statut de « Bibliographie générale consolidée » tant que les 142 faits de socle issus des Volumes II et III demeurent privés d'identifiants résolubles. Exiger une passe d'annotation rétroactive dotant chaque fait de son URL canonique ou référence légale précise.
3. **Exécuter les gestes 2 et 3 de péremption du Chapitre 50** :
   Mettre un terme à la désynchronisation entre le corps du livre et l'Annexe N. Les chapitres 8, 21, 27, 30, 32 et 44 doivent être formellement actualisés pour s'aligner sur les constats de clôture au 1ᵉʳ novembre 2026.
4. **Assainir la chaîne pré-presse et de compilation** :
   - Réparer la table tronquée de la page 585 en réintégrant `198` doublons fondus et `1065` entrées uniques, et supprimer la puce orpheline `• 134 1065`.
   - Exécuter un script de dédoublonnage sémantique flou pour fusionner les triplicatas, quadruplicatas et 50+ doublons de l'Annexe I.1.
   - Purger l'intégralité des 8 directives de travail et mémos internes polluant les notices bibliographiques.
   - Désactiver la césure automatique sur les blocs d'URL pour éliminer le caractère parasite `\ufffe` et supprimer les espaces parasites.
5. **Combler le vide académique par l'incorporation des 20 références fondamentales** :
   Intégrer les travaux séminales en systèmes distribués (Lamport, PBFT, Raft), en sécurité formelle (Fred Schneider sur les moniteurs de référence, Macaroons), en régulation prudentielle canadienne (BSIF Ligne directrice E-21 sur la résilience opérationnelle) et en standards industriels de production (CNCF SPIFFE/SPIRE).
6. **Ouvrir les dépôts d'archives des monographies sources** :
   Verser les fichiers sources ou les registres d'audit complets des Volumes I, II et III dans le dépôt public pour satisfaire aux exigences d'auditabilité et de non-répudiation revendiquées par le Compendium.

---

# 7. Corrections mineures et typographiques (Minor Corrections and Typos)

1. **Annexe B, p. 584, l. 53196 (S-158)** : Nettoyer la duplication textuelle *« Vol. I, Monographie § Annexe B et Annexe B — Architecture de solutions §7.4.3 »* en supprimant la répétition du segment « Annexe B ».
2. **Annexe I.1, p. 651, Notice [1064] Zinnia (l. 59250)** : Supprimer la préposition orpheline « à » ou insérer le numéro de sous-section manquant : *« ...cf. §5.9, §5.11, §5.12.2 à »*.
3. **Annexe I.1, p. 631, Notice Paradigm / Stripe Tempo (l. 57452)** : Même anomalie : corriger *« ...cf. §5.7, §5.13 à »*.
4. **Annexe I.1, notices diverses (pp. 639-650)** : Restaurer l'espace normalisé manquant entre le point fermant de l'année et le titre du document : corriger `(2026).The`, `(2026).TraderBench`, `(2024).A Multimodal`, `(2026).Workload`.
5. **Annexe I.1, p. 595, 630, 639, 641** : Supprimer les espaces parasites insérés au milieu des adresses : `consumerfinance.gov`, `osfi-bsif.gc.ca`, `docs.pactflow.io`, `docs.temporal.io`, `NIST.SP.800-207A`.
6. **Annexe N, pp. 662-663** : Remplacer l'ensemble des occurrences du caractère de césure fantôme `\ufffe` dans les URL par un tiret standard ou une chaîne continue sans rupture.
7. **Annexe I.1, Notice [892] p. 640** : Supprimer l'entrée erronée « Merchant Payments Protocol » générée par confusion lexicale avec la Notice [893] « Machine Payments Protocol ».
