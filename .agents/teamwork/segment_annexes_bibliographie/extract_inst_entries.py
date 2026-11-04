import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

def find_entries_with_keywords(keywords):
    results = []
    for idx, e in enumerate(entries, 1):
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', e, re.IGNORECASE):
                results.append((idx, e))
                break
    return results

print("=== BSIF / OSFI ENTRIES ===")
for idx, e in find_entries_with_keywords(['bsif', 'osfi']):
    print(f"[{idx}]: {e}\n")

print("=== AMF ENTRIES ===")
for idx, e in find_entries_with_keywords(['AMF (Québec)', 'Autorité des marchés financiers', 'lautorite.qc.ca']):
    print(f"[{idx}]: {e}\n")

print("=== BANQUE DU CANADA ENTRIES ===")
for idx, e in find_entries_with_keywords(['Banque du Canada', 'Bank of Canada', 'bankofcanada']):
    print(f"[{idx}]: {e}\n")

print("=== BIS / BRI ENTRIES ===")
for idx, e in find_entries_with_keywords(['Bank for International Settlements', 'bis.org', 'BRI']):
    print(f"[{idx}]: {e}\n")

print("=== NIST ENTRIES ===")
for idx, e in find_entries_with_keywords(['NIST']):
    print(f"[{idx}]: {e}\n")
