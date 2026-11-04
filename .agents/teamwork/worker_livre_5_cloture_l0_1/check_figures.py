import os

txt_dir = r'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_livre_5_cloture_l0_1\extracted_text'

figures = [
    (529, 'Figure 47.1'),
    (533, 'Figure 47.4'),
    (540, 'Figure 48.1'),
    (541, 'Figure 48.2'),
    (542, 'Figure 48.3'),
    (547, 'Figure 49.0'),
    (550, 'Figure 49.1'),
    (560, 'Figure 49.11'),
    (574, 'Figure 50.2'),
    (576, 'Figure 50.3'),
    (577, 'Figure 50.4')
]

for p, fig in figures:
    p_file = os.path.join(txt_dir, f'page_{p}.txt')
    if os.path.exists(p_file):
        with open(p_file, 'r', encoding='utf-8') as f:
            c = f.read()
        idx = c.find(fig)
        if idx != -1:
            snippet = c[max(0, idx-50):min(len(c), idx+180)].replace('\n', ' ')
            print(f'P.{p} [{fig}]: {snippet}')
        else:
            print(f'P.{p} [{fig}]: NOT FOUND in page text')
