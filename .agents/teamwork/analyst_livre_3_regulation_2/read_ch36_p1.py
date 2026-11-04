with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_36.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

def print_section(sec_id, max_chars=4000):
    m = re.search(rf"({sec_id}\s+[^\n]+)(.*?)(?=\n36\.\d+|\Z)", text, re.DOTALL)
    if m:
        title = m.group(1)
        body = m.group(2)
        print(f"=== {title} ===")
        print(body[:max_chars])
        print(f"\n[... Total chars: {len(body)}]\n")
    else:
        print(f"Section {sec_id} not found")

print_section("36.1")
print_section("36.2")
print_section("36.3")
print_section("36.4")
