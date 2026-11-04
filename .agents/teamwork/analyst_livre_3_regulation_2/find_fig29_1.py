with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_29.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

m = re.search(r"Figure 29\.1.*?(?=\n\n|\Z)", text)
if m:
    print(m.group(0))

lines = text.split("\n")
for idx, l in enumerate(lines):
    if "Figure 29.1" in l or "Tableau 29.1" in l:
        print(f"L{idx}: {l}")
        for j in range(max(0, idx-5), min(len(lines), idx+15)):
            print(f"  {lines[j]}")
