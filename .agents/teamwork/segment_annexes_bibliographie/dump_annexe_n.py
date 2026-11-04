with open(r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('## [Page ')
page_dict = {}
for p in pages[1:]:
    p_num = int(p.split(']')[0])
    p_content = p.split('\n', 1)[1] if '\n' in p else ''
    page_dict[p_num] = p_content

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\annexe_N_full.txt', 'w', encoding='utf-8') as f_out:
    for p in range(652, 664):
        f_out.write(f"==================== PAGE {p} ====================\n")
        f_out.write(page_dict[p])
        f_out.write("\n\n")

print("Annexe N dumped to annexe_N_full.txt")
