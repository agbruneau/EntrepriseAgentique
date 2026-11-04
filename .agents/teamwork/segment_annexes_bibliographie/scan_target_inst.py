with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\institutional_entries.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
print(f"Total institutional entries: {len(entries)}")

targets = ['bsif', 'osfi', 'amf', 'nist', 'banque du canada', 'bank of canada', 'bis', 'bri']

for idx, e in enumerate(entries):
    for t in targets:
        if t in e.lower():
            # print match
            lines = e.split('\n')
            first_line = lines[0]
            print(f"Target '{t}': {first_line[:100]} | full: {e}")
            print("-" * 60)
            break
