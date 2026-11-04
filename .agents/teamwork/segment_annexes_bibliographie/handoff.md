# Rapport de Handoff — Segment Annexes et Bibliographie (Candidat 1)

## 1. Observation
- **Périmètre inspecté** : Pages 584 à 663 de `documents/Compendium.pdf`, avec l'amont immédiat de l'Annexe B (pp. 578-584), inspectées via les images haute résolution `documents/scratch/document_pages/page-578.png` à `page-663.png` et le texte complet de `documents/DOCUMENT_TEXT_MAP.md` (lignes 52578 à 60932).
- **Faits primaires de l'Annexe B (pp. 578-584)** : 159 entrées ($S\text{-}001$ à $S\text{-}159$), découpées en Vol. II (46 entrées), Vol. III (96 entrées), Vol. I (17 entrées). La numérotation des faits sources présente des sauts documentés : Vol. II omet F-12, F-13, F-14 ; Vol. III exclut F-92 et F-96 de l'Annexe B mais les cite verbatim dans le corps du manuscrit aux chapitres 38, 39 et 40. La table d'héritage $H\text{-}01$ à $H\text{-}33$ omet $H\text{-}13$ et $H\text{-}16$, tandis que $H\text{-}15$ est cité 6 fois bien qu'exclu du socle consolidé.
- **Anomalie visuelle et arithmétique de la page 585** : La table de synthèse de dédoublonnage de l'Annexe I présente deux cellules vides (« Doublons fondus » et « Entrées uniques »). Les valeurs ont débordé de la grille sous la forme d'une puce orpheline textuelle `• 134 1065`. L'arithmétique $1\,263 - 134 = 1\,129 \neq 1\,065$ est incohérente.
- **Vérification empirique des entrées 1 à 150 (pp. 586-596)** : 100 % des articles académiques et standards vérifiés par `search_web` existent réellement (aucun article inventé par LLM). Cependant, au moins 17 paires/triplets de doublons stricts non fondus subsistent dans les 150 premières notices (ex. Anthropic 2024 MCP consécutif p. 588, Courtney ANS v2 consécutif p. 599, Aim Labs EchoLeak en triplon p. 587, Aldasoro BIS 1194 consécutif p. 587).
- **Régime de l'Annexe I.2 (p. 651)** : L'auteur admet que l'Annexe I ne réunit pas trois bibliographies mais une seule (Vol. I), les volumes sources II et III ne portant aucune bibliographie résoluble.
- **Actualisation réglementaire (Annexe N, pp. 652-663)** : Revalidation rigoureuse du NIST IR 8547 Final (27 oct. 2026), de l'A2A v1.1.0-rc (29 oct. 2026), de la SEP-3398 (MCP), du gel de C-36, du report d'application de l'EU AI Act et des 4 reports de la Note AMF IA (CRE-IA-2026-01-QC).

## 2. Logic Chain
1. Les observations visuelles de `page-585.png` démontrent un bogue de compilation du tableau récapitulatif (débordement de boîte) et une incohérence numérique ($1\,263 - 198 = 1\,065$, le chiffre 134 étant erroné ou résiduel).
2. L'inspection des entrées 1 à 150 de l'Annexe I.1 et les recherches Web confirment que la méthode de dédoublonnage annoncée (fusion par DOI/arXiv/URL ou signature textuelle) a échoué à éliminer des doublons triviaux partageant des URLs strictement identiques.
3. La comparaison entre l'Annexe B et le corps du texte (ch. 38, 39, 40) démontre l'existence de citations fantômes pour les faits exclus F-92 et F-96, ainsi que pour la thèse non admise au socle H-15.
4. L'aveu de l'Annexe I.2 établit une asymétrie probatoire : 89,3 % des faits vérifiés du socle (Volumes II et III) ne bénéficient d'aucun identifiant résoluble dans la bibliographie générale, ce qui affaiblit leur opposabilité réglementaire.
5. Les constats de l'Annexe N confirment la solidité du suivi des faits jusqu'au 1er novembre 2026, mais laissent le corps du texte en état de désynchronisation assumée.

## 3. Caveats
- Les monographies sources des Volumes I, II et III n'étant pas versées au dépôt de révision, les contextes initiaux de formulation des faits F-xx et H-xx ont été reconstitués à partir des seuls énoncés présents dans le Compendium (Vol. IV) et des notes de bas de page.
- Le balayage web s'est concentré de manière exhaustive sur les entrées 1 à 150 de l'Annexe I.1 ; les entrées 151 à 1 065 ont fait l'objet de sondages par échantillonnage.

## 4. Conclusion
Le segment `segment_annexes_bibliographie` (pp. 584-663) est validé sous condition de révisions majeures :
- Corriger le tableau de la page 585 (cellules vides et puce orpheline).
- Purger les 17 doublons identifiés dans l'Annexe I.1.
- Statuer sur les citations fantômes F-92, F-96 et H-15.
- Intégrer les travaux fondamentaux omis (SOSP PagedAttention/vLLM, SGLang RadixAttention, StruQ prompt injection, ERC-4337).
Le rapport exhaustif complet est consigné dans `c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\handoff_1.md`.

## 5. Verification Method
- **Inspection visuelle** : `view_file` sur `documents/scratch/document_pages/page-585.png` (constat direct du tableau tronqué et de la puce `• 134 1065`).
- **Inspection textuelle** : `view_file` sur `documents/DOCUMENT_TEXT_MAP.md` aux lignes 53177-53260 (p. 585) et 53261-54500 (doublons de l'Annexe I.1).
- **Vérification Web indépendante** : Exécuter des requêtes sur les DOIs et identifiants arXiv cités (ex. `10.1145/800213.806523`, `arXiv:2602.11327`, `arXiv:2407.15909`).
