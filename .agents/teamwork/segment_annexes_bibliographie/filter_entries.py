import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    content = f.read()

entries = content.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

print(f"Total entries: {len(entries)}")

institutions = ['BSIF', 'OSFI', 'AMF', 'NIST', 'Banque du Canada', 'Bank of Canada', 'BRI', 'BIS', 'FSB', 'SEC', 'ACVM', 'CSA', 'CIRO', 'OCRCVM', 'Federal Reserve', 'EBA', 'ESMA', 'ECB', 'BCE']

inst_entries = []
y2024_2026_entries = []
p638_651_entries = []

for idx, e in enumerate(entries, 1):
    # check page
    m_page = re.search(r'\(p\.(\d+)\)', e)
    page_num = int(m_page.group(1)) if m_page else 0
    
    # check year
    has_recent = any(y in e for y in ['(2024)', '(2025)', '(2026)', '2024', '2025', '2026'])
    
    # check institution
    has_inst = any(inst.lower() in e.lower() for inst in institutions)
    
    if has_inst:
        inst_entries.append((idx, page_num, e))
    if has_recent:
        y2024_2026_entries.append((idx, page_num, e))
    if page_num >= 638:
        p638_651_entries.append((idx, page_num, e))

print(f"Total institution entries found: {len(inst_entries)}")
print(f"Total 2024-2026 entries found: {len(y2024_2026_entries)}")
print(f"Total entries in pp. 638-651: {len(p638_651_entries)}")

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\institutional_entries.txt', 'w', encoding='utf-8') as f:
    for idx, p, e in inst_entries:
        f.write(f"[{idx}] (p.{p}): {e}\n\n")

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'w', encoding='utf-8') as f:
    for idx, p, e in p638_651_entries:
        f.write(f"[{idx}] (p.{p}): {e}\n\n")
