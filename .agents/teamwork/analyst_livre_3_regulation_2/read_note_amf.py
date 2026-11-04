import fitz

doc = fitz.open(r"c:\Github\EntrepriseAgentique\documents\Note AMF IA.pdf")
print("Pages in Note AMF IA.pdf:", len(doc))
for i in range(min(5, len(doc))):
    print(f"--- PAGE {i+1} ---")
    print(doc[i].get_text()[:1000])
