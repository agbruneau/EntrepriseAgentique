import re

with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_27.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Length:", len(text))
lines = text.split("\n")
sections = [l for l in lines if re.match(r"^27\.\d+", l.strip())]
print("Sections in Ch 27:")
for s in sections:
    print("  ", s)
