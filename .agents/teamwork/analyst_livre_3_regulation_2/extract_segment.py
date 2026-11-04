import re

text_map_path = r"C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md"
out_path = r"c:\Github\EntrepriseAgentique\.agents\teamwork\analyst_livre_3_regulation_2\segment_text_309_420.txt"

with open(text_map_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

recording = False
extracted = []

for line in lines:
    if "## [Page 309]" in line:
        recording = True
    if "## [Page 421]" in line:
        recording = False
        break
    if recording:
        extracted.append(line)

with open(out_path, "w", encoding="utf-8") as f:
    f.writelines(extracted)

print(f"Extracted {len(extracted)} lines into {out_path}")
