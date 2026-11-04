import sys
import re

with open(r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Split by page
pages = text.split('## [Page ')
page_dict = {}
for p in pages[1:]:
    p_num = int(p.split(']')[0])
    p_content = p.split('\n', 1)[1] if '\n' in p else ''
    page_dict[p_num] = p_content

# Let's inspect page 584
print("=== PAGE 584 ===")
print(page_dict[584][:1500])

# Let's inspect page 585
print("=== PAGE 585 ===")
print(page_dict[585][:1500])

# Let's inspect page 651 (Annexe I.2)
print("=== PAGE 651 ===")
print(page_dict[651])

# Let's inspect page 652
print("=== PAGE 652 ===")
print(page_dict[652][:1500])
