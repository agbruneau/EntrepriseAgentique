import sys

with open(r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_page = None
page_start = {}
page_lines = {}

for idx, line in enumerate(lines):
    if line.startswith('## [Page '):
        p_num = int(line.split('[Page ')[1].split(']')[0])
        if 584 <= p_num <= 663:
            current_page = p_num
            page_start[p_num] = idx + 1
            page_lines[p_num] = []
        else:
            current_page = None
    elif current_page is not None:
        page_lines[current_page].append(line)

print(f"Total pages loaded: {len(page_start)}")

for p in sorted(page_start.keys()):
    content = "".join(page_lines[p])
    # detect important lines
    first_few = [l.strip() for l in page_lines[p][:5] if l.strip()]
    headings = [l.strip() for l in page_lines[p] if l.strip().startswith(('Annexe', 'I.', 'Régime', 'N.'))]
    print(f"Page {p} (line {page_start[p]}): {first_few[:2]} | Headings: {headings}")
