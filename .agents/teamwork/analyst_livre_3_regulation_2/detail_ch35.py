with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_35.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Let's find each subsection 35.1 to 35.9
sections = re.findall(r"(35\.\d+(?:\.\d+)?\s+[^\n]+)", text)
print("Found subsections in Ch 35:")
for s in sections:
    print(" -", s)

def get_sub(title_start):
    pattern = rf"({re.escape(title_start)}.*?)(?=\n35\.\d+|\n## \[Page \d+\]\s+Compendium 36|\Z)"
    m = re.search(pattern, text, re.DOTALL)
    if m:
        return m.group(1)
    return "NOT FOUND"

for s in sections:
    content = get_sub(s)
    print(f"\n==================== {s} ====================")
    print(content[:1500])
