import re

text_map_path = r"C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md"

with open(text_map_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

pages = {}
current_page = None
current_content = []

for line in lines:
    m = re.match(r"^## \[Page (\d+)\]", line)
    if m:
        if current_page is not None:
            pages[current_page] = "".join(current_content)
        current_page = int(m.group(1))
        current_content = [line]
    else:
        if current_page is not None:
            current_content.append(line)

if current_page is not None:
    pages[current_page] = "".join(current_content)

print(f"Total pages indexed: {len(pages)}")

# Range 419 to 530
assigned_pages = {p: pages[p] for p in range(419, 531) if p in pages}
print(f"Assigned pages found: {len(assigned_pages)}")

# Detect chapters and titles
chapters = []
for p in range(419, 531):
    content = assigned_pages.get(p, "")
    for line in content.splitlines():
        line_str = line.strip()
        if re.match(r"^Compendium \d+", line_str) or re.match(r"^\d+\s*·\s*", line_str) or re.match(r"^Livre IV", line_str):
            chapters.append((p, line_str))

print("\n--- Structure detected ---")
seen = set()
for p, title in chapters:
    if title not in seen:
        print(f"Page {p}: {title}")
        seen.add(title)
