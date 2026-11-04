import re
import os

text_map_path = r"C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md"

with open(text_map_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split by pages
page_chunks = re.split(r"## \[Page (\d+)\] \(`page-\d+\.png`\)", text)

pages = {}
for i in range(1, len(page_chunks), 2):
    p_num = int(page_chunks[i])
    p_content = page_chunks[i+1]
    pages[p_num] = p_content

out_dir = r"c:\Github\EntrepriseAgentique\.agents\teamwork\segment_livre_4_application\analyst_4\extracted_chapters"
os.makedirs(out_dir, exist_ok=True)

chapters_def = [
    ("ch36_p419", 419, 419, "Prospective AP2"),
    ("ch37_mesh_pep_pdp", 420, 435, "Maillage d'agents, PEP/PDP et Zero Trust"),
    ("ch38_observabilite", 436, 445, "Observabilité agentique et OpenTelemetry"),
    ("ch39_cycle_vie_derive", 446, 455, "Cycle de vie opérationnel, dérive et incidents"),
    ("ch40_indicateurs_finops", 456, 466, "AgentOps et FinOps des agents"),
    ("ch41_fabrique_agents", 467, 473, "Fabrique d'agents, certification et réémission"),
    ("ch42_matrice_protocoles_reglements", 474, 481, "Matrice protocoles x réglementations"),
    ("ch43_archi_reference_7couches", 482, 494, "Architecture de référence unifiée par couches"),
    ("ch44_archimate", 495, 506, "Formalisation ArchiMate"),
    ("ch45_blueprint_borealis_ibm", 507, 519, "Blueprint instancié et cycle de vie"),
    ("ch46_roadmap_mai2027", 520, 526, "Instrumentation et feuille de route mai 2027"),
    ("ch47_artefact_livre_debut", 527, 530, "Artefact livré, provenance et mise en service")
]

for name, start_p, end_p, desc in chapters_def:
    chap_text = []
    for p in range(start_p, end_p + 1):
        if p in pages:
            chap_text.append(f"\n\n==================== PAGE {p} ====================\n\n")
            chap_text.append(pages[p])
    
    file_path = os.path.join(out_dir, f"{name}.txt")
    with open(file_path, "w", encoding="utf-8") as f_out:
        f_out.write("".join(chap_text))
    print(f"Wrote {name}.txt ({len(''.join(chap_text))} chars, pages {start_p}-{end_p})")

