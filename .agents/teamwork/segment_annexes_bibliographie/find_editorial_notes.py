import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')

editorial_patterns = [
    r'à conserver', r'à supprimer', r'à vérifier', r'fusionn',
    r'renvoi ch\.', r'voir §', r'non rejouable', r'cible supprimée',
    r'dépouillement'
]

matches_found = []
for idx, e in enumerate(entries, 1):
    for pat in editorial_patterns:
        if re.search(pat, e, re.IGNORECASE):
            matches_found.append((idx, pat, e))
            break

print(f"Total entries with editorial artifacts: {len(matches_found)}")
for idx, pat, e in matches_found:
    print(f"[{idx}] (pat '{pat}'):\n  {e}\n")
