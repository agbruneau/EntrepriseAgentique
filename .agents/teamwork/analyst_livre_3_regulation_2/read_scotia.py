with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\chapters\ch_35.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos1 = text.find("35.2 Scotiabank : le volume")
pos2 = text.find("35.3 RBC : la structure", pos1)
print(text[pos1:pos2])
