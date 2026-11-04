import re
import sys

def load_pages():
    with open(r'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md', 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    matches = list(re.finditer(r'##\s*\[Page\s*(\d+)\][^\n]*\n', text))
    pages = {}
    for i, m in enumerate(matches):
        p_num = int(m.group(1))
        start_idx = m.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        pages[p_num] = text[start_idx:end_idx]
    return pages

if __name__ == '__main__':
    pages = load_pages()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'get':
            p = int(sys.argv[2])
            print(f"=== PAGE {p} ===")
            print(pages.get(p, 'Not found'))
        elif sys.argv[1] == 'range':
            p_start = int(sys.argv[2])
            p_end = int(sys.argv[3])
            for p in range(p_start, p_end + 1):
                print(f"=== PAGE {p} ===")
                print(pages.get(p, ''))
        elif sys.argv[1] == 'search':
            query = sys.argv[2]
            p_start = int(sys.argv[3]) if len(sys.argv) > 3 else 140
            p_end = int(sys.argv[4]) if len(sys.argv) > 4 else 255
            for p in range(p_start, p_end + 1):
                content = pages.get(p, '')
                if query.lower() in content.lower():
                    print(f"Found in Page {p}:")
                    for line in content.split('\n'):
                        if query.lower() in line.lower():
                            print(f"  {line[:120]}")
