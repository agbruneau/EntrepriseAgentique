import re

with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_33.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Length of Ch 33:", len(text))
lines = text.split("\n")
sections = [l for l in lines if re.match(r"^33\.\d+", l.strip())]
print("Sections in Ch 33:")
for s in sections:
    print("  ", s)

print("\n--- First 3000 chars ---")
print(text[:3000])
