import re

with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\segment_text_309_420.txt", "r", encoding="utf-8") as f:
    text = f.read()

keywords = ["automate", "DFA", "état puits", "etats puits", "états-puits", "machine à états", "déterministe", "transitions", "complétude", "théorème", "lemme", "démonstration", "formel"]

for kw in keywords:
    matches = list(re.finditer(rf"\b{kw}\w*", text, re.IGNORECASE))
    print(f"Keyword '{kw}': {len(matches)} occurrences")
    for m in matches[:5]:
        start = max(0, m.start() - 60)
        end = min(len(text), m.end() + 60)
        snippet = text[start:end].replace("\n", " ")
        print(f"   [{m.start()}] ...{snippet}...")
