import re

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

print(f"Loaded {len(entries)} entries from pp. 638-651")

arxiv_pattern = re.compile(r'arXiv:(\d{4}\.\d{4,5})', re.IGNORECASE)
doi_pattern = re.compile(r'(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)')
url_pattern = re.compile(r'https?://[^\s]+')

report_lines = []

for idx, e in enumerate(entries):
    arxiv_matches = arxiv_pattern.findall(e)
    doi_matches = doi_pattern.findall(e)
    url_matches = url_pattern.findall(e)
    
    # check year
    years = re.findall(r'\((\d{4}(?:-\d{4})?)\)', e)
    
    # check if contains institution
    insts = [i for i in ['BSIF', 'OSFI', 'AMF', 'NIST', 'Banque du Canada', 'Bank of Canada', 'BIS', 'BRI', 'FSB', 'SEC', 'ACVM', 'CSA', 'Treasury', 'Federal Reserve', 'SWIFT', 'W3C', 'ISO', 'Gartner', 'WEF', 'OECD', 'OCDE'] if i.lower() in e.lower()]
    
    report_lines.append({
        'raw': e,
        'arxiv': arxiv_matches,
        'doi': doi_matches,
        'urls': url_matches,
        'years': years,
        'insts': insts
    })

print(f"Entries with arXiv: {sum(1 for r in report_lines if r['arxiv'])}")
print(f"Entries with DOI: {sum(1 for r in report_lines if r['doi'])}")
print(f"Entries with URLs: {sum(1 for r in report_lines if r['urls'])}")
print(f"Entries with Institutions: {sum(1 for r in report_lines if r['insts'])}")

# Let's list all arXiv IDs to test
all_arxiv = []
for r in report_lines:
    for a in r['arxiv']:
        all_arxiv.append((a, r['raw'][:100]))

print(f"Total arXiv papers to check: {len(all_arxiv)}")
for a, snippet in all_arxiv[:20]:
    print(f"  {a}: {snippet}...")
