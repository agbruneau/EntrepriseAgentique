import re
from difflib import SequenceMatcher

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

# Clean titles and URLs
def get_clean_title(entry):
    # remove index, page, author, year
    text_clean = re.sub(r'^\[\d+\]\s*\([^\)]+\):\s*', '', entry)
    m = re.search(r'\(\d{4}(?:-\d{4})?\)\.\s*([^.]+)', text_clean)
    if m:
        return m.group(1).strip().lower()
    return text_clean[:50].strip().lower()

def get_urls(entry):
    return re.findall(r'https?://[^\s]+', entry)

url_map = {}
for idx, e in enumerate(entries, 1):
    urls = get_urls(e)
    for u in urls:
        # normalize url
        u_norm = u.replace('www.', '').replace('\u200b', '').rstrip('/.-')
        if u_norm not in url_map:
            url_map[u_norm] = []
        url_map[u_norm].append(idx)

duplicate_urls = {k: v for k, v in url_map.items() if len(v) > 1}

print(f"Total duplicate URLs found: {len(duplicate_urls)}")
for u, idxs in list(duplicate_urls.items())[:20]:
    print(f"URL: {u}")
    print(f"  Entries: {idxs}")
    for i in idxs:
        print(f"    [{i}]: {entries[i-1][:100]}...")
