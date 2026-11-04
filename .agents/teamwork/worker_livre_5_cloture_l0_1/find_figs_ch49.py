with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\ch49_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
figs = re.findall(r'Figure 49\.[0-9]+[^\n]+', text)
for fig in figs:
    pos = text.find(fig)
    page = text[:pos].count('=== PAGE ') + 544
    print(f'Page {page}: {fig}')
