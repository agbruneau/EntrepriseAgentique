import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

for idx, e in enumerate(entries, 1):
    # Check for truncated DOIs
    if re.search(r'10\.\d{4,9}/[^\s]*[-_]$', e) or re.search(r'10\.\d{4,9}/[^\s]*[-_]\s', e) or '10.1007/978-' in e or 'NIST.SP.800-' in e or 'RFC9901' in e:
        print(f"Entry [{idx}] (p.{re.search(r'\(p\.(\d+)\)', e).group(1)}):")
        print(f"  {e}\n")
