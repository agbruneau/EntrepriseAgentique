import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\ch49_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = ['rice', 'décidab', 'indécidab', 'halting', 'arrêt', 'calculab', 'gödel', 'turing', 'formel', 'théorème', 'épistém']
for kw in keywords:
    matches = [m.start() for m in re.finditer(kw, text, re.IGNORECASE)]
    print(f'Keyword "{kw}": {len(matches)} occurrences')
    for pos in matches[:4]:
        snippet = text[max(0, pos-100):min(len(text), pos+150)].replace('\n', ' ')
        print(f'   ... {snippet} ...')
