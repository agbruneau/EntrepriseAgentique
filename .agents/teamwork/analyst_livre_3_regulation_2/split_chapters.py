import re
import os

segment_file = r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\segment_text_309_420.txt"
with open(segment_file, "r", encoding="utf-8") as f:
    text = f.read()

# Chapters: 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
# Also include 26 end (p. 309-310)
chap_patterns = [
    (26, r"26 · Le vide fédéral"),
    (27, r"27 · Québec : la ligne directrice IA de l’AMF et l’article 12.1 de la Loi 25"),
    (28, r"28 · Valeurs mobilières : l’avis ACVM 11-348"),
    (29, r"29 · Le pont : des contraintes réglementaires aux frames déterministes"),
    (30, r"30 · Le maillage réglementaire international et la normalisation institutionnelle"),
    (31, r"31 · Le vertical financier : pourquoi l’agentique y est durcie"),
    (32, r"32 · Le cadre des services bancaires axés sur le consommateur"),
    (33, r"33 · ISO 20022 : Lynx accompli, RTR visé"),
    (34, r"34 · Les sous-domaines financiers : banque, assurance, patrimoine"),
    (35, r"35 · Études de cas : la production agentique canadienne \(2025-2026\)"),
    (36, r"36 · Prospective : AP2 sur les rails canadiens \?"),
    (37, r"Livre IV — Appliquer, exploiter, produire et")
]

# Find start index of each chapter
indices = []
for num, pat in chap_patterns:
    m = re.search(pat, text)
    if m:
        indices.append((num, m.start()))
        print(f"Chapter {num} found at char {m.start()}")
    else:
        print(f"Chapter {num} NOT found")

out_dir = r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters"
os.makedirs(out_dir, exist_ok=True)

for i in range(len(indices) - 1):
    c_num, start = indices[i]
    next_c_num, end = indices[i+1]
    c_text = text[start:end]
    fname = os.path.join(out_dir, f"ch_{c_num}.txt")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(c_text)
    print(f"Wrote ch_{c_num}.txt ({len(c_text)} chars)")
