with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\annexes_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = p.split(' ===')[0]
    lines = [l for l in p.split('\n') if l.strip()]
    print(f'*** PAGE {p_num} (lines: {len(lines)}) ***')
    print('\n'.join(lines[:6]))
    print('...\n')
