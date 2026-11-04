"""digest : condensé des consolidations pour la synthèse; final : assemble DEEP_REVIEW_CADRE_REFERENCE.md."""
import pathlib, re, sys

ICI = pathlib.Path(__file__).resolve().parent
TRANCHES = {1: 'Liminaires, ch. 1-5, § 6.1-6.3 (p. 1-52)', 2: '§ 6.4-7.3 (p. 51-92)',
            3: '§ 7.3-8.8 (p. 91-122)', 4: 'Ch. 9-10, § 11.1-11.2 (p. 121-162)',
            5: 'Ch. 11-15, annexe A (p. 161-212)', 6: 'Annexes B-H (p. 211-283)'}


def sections(t):
    """Découpe en sections de niveau 2 : {titre: texte}."""
    parts = re.split(r'^## ', t, flags=re.M)
    return {p.split('\n', 1)[0].strip(): p.split('\n', 1)[1] if '\n' in p else '' for p in parts[1:]}


def digest():
    out = ['# Condensé des six consolidations\n']
    for n in TRANCHES:
        t = (ICI / f'conso_{n}.md').read_text(encoding='utf8')
        s = sections(t)
        out.append(f'\n# Tranche {n} — {TRANCHES[n]}\n')
        for titre, corps in s.items():
            if titre.startswith('Synthèse') or titre.startswith('Arbitrages') or titre.startswith('Constats écartés'):
                out.append(f'## {titre}\n{corps.strip()}\n')
        mat = next((c for k, c in s.items() if k.startswith('Matrice')), '')
        out.append('## Défauts BLOQUANT et MAJEUR (titre, constats, localisation)\n')
        for bloc in re.split(r'^### ', mat, flags=re.M)[1:]:
            tete = bloc.split('\n', 1)[0]
            if 'BLOQUANT' in tete or 'MAJEUR' in tete:
                const = re.search(r'Constats d.origine\s*:?\**\s*:?\s*(.*)', bloc)
                loc = re.search(r'Localisation[^:]*:\**\s*:?\s*(.*)', bloc)
                out.append(f'- **{tete.strip()}** — constats : {const.group(1).strip() if const else "?"}'
                           f' — {loc.group(1).strip()[:300] if loc else ""}')
        out.append(f'\nMineurs : {sum(1 for b in re.split(r"^### ", mat, flags=re.M)[1:] if "MINEUR" in b.split(chr(10),1)[0])} entrées.\n')
    (ICI / 'digest.md').write_text('\n'.join(out), encoding='utf8')
    print('digest.md', (ICI / 'digest.md').stat().st_size)


def final():
    synth = (ICI / 'synth.md').read_text(encoding='utf8')
    i = synth.index('\n## 3.')
    tete, queue = synth[:i], synth[i:]
    blocs = []
    for n in TRANCHES:
        t = (ICI / f'conso_{n}.md').read_text(encoding='utf8')
        s = sections(t)
        mat = next((c for k, c in s.items() if k.startswith('Matrice')), '')
        ecartes = next((c for k, c in s.items() if k.startswith('Constats écartés')), '')
        mat = re.sub(r'^### ', '#### ', mat, flags=re.M)
        blocs.append(f'\n### 2.{n} Tranche {n} — {TRANCHES[n]}\n{mat.strip()}\n')
        if ecartes.strip():
            blocs.append(f'\n#### Constats écartés à la contre-vérification (tranche {n})\n{ecartes.strip()}\n')
    doc = tete.rstrip() + '\n' + ''.join(blocs) + queue
    sortie = ICI.parent / 'DEEP_REVIEW_CADRE_REFERENCE.md'
    sortie.write_text(doc, encoding='utf8')
    print(sortie, len(doc))


if __name__ == '__main__':
    {'digest': digest, 'final': final}[sys.argv[1]]()
