import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

print(f"Total entries: {len(entries)}")

for idx, e in enumerate(entries, 846):
    # check for obvious syntax/formatting flaws
    # 1. Missing space after period
    bad_punct = re.findall(r'\.[A-Z]', e)
    # 2. Broken URLs (containing spaces or line breaks)
    has_space_in_url = re.findall(r'https?://[^\s]+\s+[^\s]+', e)
    # 3. Trailing punctuation in identifiers
    bad_doi = re.findall(r'DOI\s+10\.\d{4,9}/[^\s]+[\),;]', e)
    
    # check duplicates of authors
    m_author = re.match(r'^(?:\[\d+\]\s*\([^\)]+\):\s*)?([^(\d]+)\s*\((20\d\d)', e)
    
    anomalies = []
    if bad_punct:
        anomalies.append(f"Missing space after period: {bad_punct}")
    if bad_doi:
        anomalies.append(f"Malformed DOI trailing char: {bad_doi}")
    if ' — cf.' not in e and '— cf.' not in e and not e.endswith('.'):
        anomalies.append("Does not end with period or cf.")
        
    if anomalies:
        print(f"Entry [{idx}]: {anomalies}")
        print(f"   {e[:120]}...\n")
