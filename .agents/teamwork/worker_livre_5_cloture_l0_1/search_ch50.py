import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\ch50_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

terms = ['décommission', 'recertif', 'fin de vie', 'drain', 'clé', 'session', 'mémoire', 'révoc', 'cycle de vie', 'obsolesc']
for t in terms:
    m = list(re.finditer(t, text, re.IGNORECASE))
    print(f'Term "{t}": {len(m)} matches')
    for match in m[:3]:
        pos = match.start()
        print('   ', text[max(0, pos-60):min(len(text), pos+80)].replace('\n', ' '))
