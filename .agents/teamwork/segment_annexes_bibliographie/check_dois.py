import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

doi_dict = {}

for idx, e in enumerate(entries, 1):
    m_page = re.search(r'\(p\.(\d+)\)', e)
    page_num = int(m_page.group(1)) if m_page else 0
    
    # DOI regex
    matches = re.findall(r'10\.\d{4,9}/[^\s,;]+', e)
    for m in matches:
        m_clean = m.rstrip('.')
        if m_clean not in doi_dict:
            doi_dict[m_clean] = []
        doi_dict[m_clean].append((idx, page_num, e))

print(f"Total unique DOIs in Annexe I.1: {len(doi_dict)}")
for d in list(doi_dict.keys())[:25]:
    print(f"  {d}")
