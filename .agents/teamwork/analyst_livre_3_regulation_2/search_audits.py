import re

files = [
    r"c:\Github\EntrepriseAgentique\documents\Audit Veille Techno.txt",
    r"c:\Github\EntrepriseAgentique\documents\Audit Revue Littérature.txt"
]

terms = ["11-348", "12.1", "E-23", "C-27", "C-15", "C-69", "Lynx", "RTR", "AP2", "AMF"]

for fpath in files:
    print(f"=== File: {fpath} ===")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    for t in terms:
        matches = [m.start() for m in re.finditer(re.escape(t), content, re.IGNORECASE)]
        print(f"  Term '{t}': {len(matches)} matches")
        for pos in matches[:2]:
            snippet = content[max(0, pos-50):min(len(content), pos+80)].replace("\n", " ")
            print(f"    [{pos}] ...{snippet}...")
