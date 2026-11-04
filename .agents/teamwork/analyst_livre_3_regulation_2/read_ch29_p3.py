with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_29.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

m = re.search(r"29\.4\.1.*", text, re.DOTALL)
if m:
    print(m.group(0))
