with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_35.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

def print_section(sec_id, max_chars=3500):
    m = re.search(rf"({sec_id}\s+[^\n]+)(.*?)(?=\n35\.\d+|\Z)", text, re.DOTALL)
    if m:
        title = m.group(1)
        body = m.group(2)
        print(f"=== {title} ===")
        print(body[:max_chars])
        print(f"\n[... Total chars: {len(body)}]\n")
    else:
        print(f"Section {sec_id} not found")

for s in ["35.1", "35.2", "35.3", "35.4", "35.5", "35.6", "35.7", "35.8"]:
    print_section(s)
