import re

with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_31.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Length of Ch 31:", len(text))
lines = text.split("\n")
sections = [l for l in lines if re.match(r"^31\.\d+", l.strip())]
print("Sections in Ch 31:")
for s in sections:
    print("  ", s)
