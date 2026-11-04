import re

with open(r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\segment_text_309_420.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = re.split(r"(## \[Page \d+\] \(`page-\d+\.png`\))", text)

def get_page(num):
    target = f"## [Page {num}] (`page-{num}.png`)"
    for i, part in enumerate(pages):
        if target in part:
            return pages[i+1] if i+1 < len(pages) else ""
    return ""

print("=== CHAPITRE 27 (Pages 311 - 322) ===")
for p in range(311, 323):
    content = get_page(p)
    print(f"--- PAGE {p} ---")
    lines = [l for l in content.split("\n") if l.strip()]
    for l in lines[:15]:
        print(l)
    print(f"... ({len(lines)} lines total)")
