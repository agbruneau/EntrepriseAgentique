import os

text_map_path = r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md'

with open(text_map_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

pages = {}
cur_p = None
cur_lines = []
start_idx = 0

for idx, line in enumerate(lines):
    if line.startswith('## [Page '):
        if cur_p is not None:
            pages[cur_p] = (start_idx, cur_lines)
        p_num = int(line.split(']')[0].replace('## [Page ', '').strip())
        cur_p = p_num
        start_idx = idx
        cur_lines = [line]
    else:
        if cur_p is not None:
            cur_lines.append(line)
if cur_p is not None:
    pages[cur_p] = (start_idx, cur_lines)

print(f"Total pages: {len(pages)}")

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_protocoles_0_3\pages_summary.txt', 'w', encoding='utf-8') as out:
    for p in range(78, 146):
        if p in pages:
            non_empty = [l.strip() for l in pages[p][1] if l.strip() and not l.startswith('##') and not l.startswith('---') and not l.startswith('Gel au')]
            snippet = " | ".join(non_empty[:3])
            out.write(f"Page {p} (line {pages[p][0]}): {snippet}\n")

print("Summary written.")
