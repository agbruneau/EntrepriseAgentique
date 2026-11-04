import re

text_map_path = r"C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md"

with open(text_map_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

pages = {}
current_page = None
page_pattern = re.compile(r"^## \[Page (\d+)\] \(`(page-\d+\.png)`\)")

for idx, line in enumerate(lines):
    m = page_pattern.match(line.strip())
    if m:
        p_num = int(m.group(1))
        pages[p_num] = {
            "file": m.group(2),
            "line_start": idx + 1,
            "text": []
        }
        current_page = p_num
    elif current_page is not None:
        pages[current_page]["text"].append(line)

print(f"Total pages indexed: {len(pages)}")

# Print pages from 309 to 420
for p in range(309, 421):
    if p in pages:
        first_few = [l.strip() for l in pages[p]["text"][:6] if l.strip()]
        title_summary = " // ".join(first_few[:3])
        print(f"Page {p} (line {pages[p]['line_start']}): {title_summary[:120]}")
