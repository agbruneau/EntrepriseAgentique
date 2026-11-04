import os
import json

text_map_path = r"C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md"
page_image_dir = r"C:\Github\EntrepriseAgentique\documents\scratch\document_pages"
total_pages = 663

segments_def = [
    {
        "name": "segment_livre_1_fondements",
        "category": "Methodology",
        "start": 1,
        "end": 79,
        "review_plan_segments": "S01 à S07",
        "instruction": "Auditer le socle pré-agentique et théorique de l'interopérabilité (Ch. 1 à 6). Falsifier la formule de coût d'intégration N(N-1)/2, vérifier les taxonomies LCIM et couplage, examiner la dualité GAV vs LAV en intégration sémantique, et auditer l'architecture de la boucle ReAct face aux erreurs stochastiques des LLMs et à la dérive contextuelle en RAG."
    },
    {
        "name": "segment_livre_1_protocoles",
        "category": "Methodology",
        "start": 78,
        "end": 145,
        "review_plan_segments": "S08 à S13",
        "instruction": "Auditer l'anatomie protocolaire des systèmes agentiques (Ch. 7 à 11). Examiner en profondeur les spécifications MCP (JSON-RPC 2.0, transport SSE/stdio) et A2A, les mécanismes de registres et de découverte dynamique, le protocole de paiement AP2 et l'infrastructure Cisco AGNTCY. Falsifier la taxonomie des risques protocolaires (injection indirecte, collisions de verrous, désynchronisation d'état)."
    },
    {
        "name": "segment_livre_2_confiance",
        "category": "Theory / Math",
        "start": 144,
        "end": 255,
        "review_plan_segments": "S14 à S23",
        "instruction": "Auditer la pile d'identité non humaine et de délégation vérifiable (Ch. 12 à 21). Évaluer les limites d'OAuth 2.0/SCIM, la solidité cryptographique des W3C DID et VC, la structure signée de l'Agent Card et le passeport d'agent. Falsifier la démonstration mathématique de rupture d'opposabilité dans le 'problème des deux sauts' (A->B->C), auditer la taxonomie des attaques (rug-pull, confused deputy), la boucle défensive Agentic SOC, et l'impact de la transition post-quantique NIST (ML-DSA, SLH-DSA)."
    },
    {
        "name": "segment_livre_3_orchestration",
        "category": "Modeling",
        "start": 254,
        "end": 310,
        "review_plan_segments": "S24 à S28",
        "instruction": "Auditer le paradigme APM et la taxonomie d'orchestration OO1-OO4 (Ch. 22 à 26). Démontrer la rigueur formelle de l'autonomie encadrée déterministe (OO4), auditer la comparaison des frameworks d'orchestration (LangGraph, Semantic Kernel, Temporal), analyser les modèles de concurrence et de passage à l'échelle d'entreprise, et examiner la transposition de la ligne directrice BSIF/OSFI E-23 ainsi que l'impact du vide législatif fédéral canadien (C-27/AIDA)."
    },
    {
        "name": "segment_livre_3_regulation",
        "category": "Argument & Analysis",
        "start": 309,
        "end": 420,
        "review_plan_segments": "S29 à S38",
        "instruction": "Auditer l'encadrement réglementaire durci du vertical financier et les études de cas (Ch. 27 à 36). Examiner l'article 12.1 de la Loi 25 québécoise et la Ligne directrice IA de l'AMF, l'avis ACVM 11-348, et évaluer le pont mathématique traduisant les contraintes en automates finis déterministes. Analyser l'intégration ISO 20022 (Lynx, RTR), le cadre FCAC d'open banking, falsifier les retours d'expérience et métriques annoncées dans les études de cas bancaires canadiennes (2025-2026), et évaluer la viabilité d'AP2."
    },
    {
        "name": "segment_livre_4_application",
        "category": "Experiments",
        "start": 419,
        "end": 530,
        "review_plan_segments": "S39 à S48",
        "instruction": "Auditer l'infrastructure d'exploitation, de production et de modélisation (Ch. 37 à 46). Analyser l'architecture Zero Trust AgentMesh (PEP/PDP), la pile d'observabilité OpenTelemetry et la détection de dérive de raisonnement (reasoning drift), les indicateurs FinOps (Coût par tâche CpT), la CI/CD de la fabrique d'agents, la matrice protocoles × réglementations, l'architecture 7 couches, la formalisation ArchiMate 3.2 et le blueprint d'architecture instancié (Boréalis/IBM)."
    },
    {
        "name": "segment_livre_5_cloture",
        "category": "Conclusion",
        "start": 529,
        "end": 585,
        "review_plan_segments": "S49 à S53",
        "instruction": "Auditer la sémantique d'effet, la livraison logicielle et la prospective technologique (Ch. 47 à 50). Falsifier les garanties formelles d'idempotence, de compensation (patron Saga) et de réconciliation d'état distribué. Vérifier la provenance logicielle (SBOM, SLSA), les critères formels de décidabilité des politiques de sécurité et les limites épistémiques (horizon 2027-2032), ainsi que le protocole de péremption et de recertification périodique des agents."
    },
    {
        "name": "segment_annexes_bibliographie",
        "category": "Other",
        "start": 584,
        "end": 663,
        "review_plan_segments": "S54 à S60",
        "instruction": "Auditer l'appareil critique, la bibliographie consolidée et l'actualisation réglementaire (Annexes B, I, N). Vérifier exhaustivement les références bibliographiques citées : détecter les fausses citations, les hallucinations de DOI, les anachronismes ou omissions de la littérature scientifique jusqu'en 2026 (STOC, NeurIPS, SOSP, ICLR, etc.). Auditer l'Annexe N (Note AMF IA, révision du protocole ch. 50 et inventaire des lacunes)."
    }
]

lines = []
lines.append("# Analysis Partition Metadata")
lines.append("")
lines.append(f"input_format: pdf")
lines.append(f"text_map_path: {text_map_path}")
lines.append(f"page_image_dir: {page_image_dir}")
lines.append(f"total_pages: {total_pages}")
lines.append("")
lines.append("## Segments Partitioning")
lines.append("")

for s in segments_def:
    p_imgs = [f"page-{p}.png" for p in range(s["start"], s["end"] + 1)]
    lines.append(f"### Segment: {s['name']}")
    lines.append(f"- **name**: {s['name']}")
    lines.append(f"- **category**: {s['category']}")
    lines.append(f"- **page_ranges**: [[{s['start']}, {s['end']}]]")
    lines.append(f"- **review_plan_mapping**: {s['review_plan_segments']}")
    lines.append(f"- **page_images**: {json.dumps(p_imgs)}")
    lines.append(f"- **context_instruction**: {s['instruction']}")
    lines.append("")

target_file = r"c:\Github\EntrepriseAgentique\.agents\teamwork\document_orchestrator\ANALYSIS_PARTITION.md"
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines).strip() + "\n")

print(f"ANALYSIS_PARTITION.md successfully written to {target_file}")
print(f"Size: {os.path.getsize(target_file)} bytes")
