with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_35.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

def print_exact_section(header, next_header):
    pos1 = text.find(header)
    pos2 = text.find(next_header, pos1) if next_header else len(text)
    print(f"=== {header} ===")
    print(text[pos1:pos2])

print_exact_section("35.1 TD : la pré-adjudication", "35.2 Scotiabank : le volume")
print_exact_section("35.2 Scotiabank : le volume", "35.3 RBC : la structure")
print_exact_section("35.4 Manuvie : l’environnement", "35.5 Desjardins : la stratégie")
print_exact_section("35.8.1 BMO", "35.8.2 Sun Life")
