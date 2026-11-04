with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_32.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

m = re.search(r"32\.1.*?(?=32\.4|\Z)", text, re.DOTALL)
if m:
    print(m.group(0))
