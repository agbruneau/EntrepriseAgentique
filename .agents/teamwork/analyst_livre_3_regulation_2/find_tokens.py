with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_35.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

for m in re.finditer(r"(?:[0-9]+[,\.][0-9]+\s+milliards|milliards\s+de\s+jetons)", text, re.IGNORECASE):
    pos = m.start()
    print("--- MATCH ---")
    print(text[max(0, pos-150):min(len(text), pos+250)].replace("\n", " "))
