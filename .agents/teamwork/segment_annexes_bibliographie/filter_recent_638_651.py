with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
print(f"Total entries in 638-651: {len(entries)}")

# Let's inspect all entries that cite 2025 or 2026
recent = []
for idx, e in enumerate(entries):
    if '2025' in e or '2026' in e:
        recent.append((idx, e))

print(f"Recent (2025-2026) entries in 638-651: {len(recent)}")

# Print summary of these recent entries
with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\recent_638_651.txt', 'w', encoding='utf-8') as f_out:
    for idx, e in recent:
        f_out.write(f"--- Entry #{idx} ---\n{e}\n\n")

print("Saved recent entries to recent_638_651.txt")
