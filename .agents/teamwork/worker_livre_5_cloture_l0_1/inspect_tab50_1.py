with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\ch50_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Tableau 50.1')
pos_end = text.find('50.3 Le protocole de revalidation')
print(text[pos:pos+4000])
