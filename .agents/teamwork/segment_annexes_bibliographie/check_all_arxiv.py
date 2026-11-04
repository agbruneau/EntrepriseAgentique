import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

arxiv_dict = {}

for idx, e in enumerate(entries, 1):
    m_page = re.search(r'\(p\.(\d+)\)', e)
    page_num = int(m_page.group(1)) if m_page else 0
    
    # find all arXiv matches
    matches = re.findall(r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)', e, re.IGNORECASE)
    for m in matches:
        if m not in arxiv_dict:
            arxiv_dict[m] = []
        arxiv_dict[m].append((idx, page_num, e))

print(f"Total unique arXiv IDs in Annexe I.1: {len(arxiv_dict)}")

# Let's inspect arXiv IDs with strange years or formats
suspicious_arxiv = []
for aid in arxiv_dict:
    # check year (first two digits)
    yr = int(aid[:2])
    mo = int(aid[2:4])
    if yr > 26 or (yr == 26 and mo > 11):
        suspicious_arxiv.append((aid, "Future date after Nov 2026", arxiv_dict[aid]))
    elif mo < 1 or mo > 12:
        suspicious_arxiv.append((aid, "Invalid month", arxiv_dict[aid]))

print(f"Suspicious arXiv IDs: {len(suspicious_arxiv)}")
for aid, reason, occ in suspicious_arxiv:
    print(f"  {aid}: {reason} -> {[o[0] for o in occ]}")

# Also check duplicates (arXiv cited multiple times under different entries)
duplicates = {k: v for k, v in arxiv_dict.items() if len(v) > 1}
print(f"arXiv IDs cited multiple times: {len(duplicates)}")
for aid, occ in list(duplicates.items())[:15]:
    print(f"  arXiv:{aid} cited in entries: {[o[0] for o in occ]}")
