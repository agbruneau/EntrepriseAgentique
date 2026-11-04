with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_28.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Length of Ch 28:", len(text))
print(text[:3000])
print("\n---\n")
print(text[3000:7000])
