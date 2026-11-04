import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

print(f"Loaded {len(entries)} entries")

# Check each entry for:
# - author format
# - date format
# - cross references 'cf. §...'
# - strange URLs or DOIs

cf_missing = []
for idx, e in enumerate(entries, 846):
    if 'cf.' not in e and '§' not in e:
        cf_missing.append((idx, e))

print(f"Entries without internal cross-reference (cf. §): {len(cf_missing)}")
for idx, e in cf_missing[:10]:
    print(f"[{idx}]: {e[:90]}...")
