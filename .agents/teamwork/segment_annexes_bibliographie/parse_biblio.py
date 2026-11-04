import re

with open(r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('## [Page ')
page_dict = {}
for p in pages[1:]:
    p_num = int(p.split(']')[0])
    p_content = p.split('\n', 1)[1] if '\n' in p else ''
    page_dict[p_num] = p_content

# In Annexe I.1 (pp. 586-651)
# Entries usually start with "• " or letter headings like "A", "B", etc.
# Let's extract entries across pages 586 to 651.

entries = []
current_entry = None

for p_num in range(586, 652):
    lines = page_dict[p_num].split('\n')
    for line in lines:
        stripped = line.strip()
        # Check if line is header or footer
        if "Compendium I.1" in stripped or "Gel au 27 juillet" in stripped or stripped.startswith("Page ") or "sur 663" in stripped:
            continue
        if stripped.startswith("I.2 —"):
            break
        if stripped.startswith("• "):
            if current_entry:
                entries.append(current_entry)
            current_entry = {'page': p_num, 'text': stripped[2:]}
        elif current_entry:
            if stripped:
                current_entry['text'] += " " + stripped

if current_entry:
    entries.append(current_entry)

print(f"Total entries found in Annexe I.1: {len(entries)}")

# Let's write all entries to a file with their index
with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'w', encoding='utf-8') as f_out:
    for idx, e in enumerate(entries, 1):
        f_out.write(f"[{idx}] (p.{e['page']}): {e['text']}\n\n")

print(f"Entries written to entries_index.txt. First entry: {entries[0]['text'][:80]}...")
print(f"Last entry: {entries[-1]['text'][:80]}...")
print(f"Entry 351: {entries[350]['text'][:80]} (page {entries[350]['page']})...")
