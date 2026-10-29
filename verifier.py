"""Contrôle de sortie P6 (PLAN.md) : vérifie les 5 PDF et le README avant publication.

Usage : python verifier.py — code de sortie 0 si tous les contrôles passent, 1 sinon.
Dépendance : pymupdf.
"""
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
PDFS = {
    'Compendium': 'Compendium.pdf',
    'Cadre': 'Cadre de Référence - Interopérabilité et Orchestration en Entreprise Agentique.pdf',
    'Veille': 'Veille Technologique.pdf',
    'Revue': 'Revue de littérature.pdf',
    'NiveauMaturité': 'NiveauMaturité.pdf',
}
AUTHOR = 'André-Guy Bruneau'
MARKERS = ['☐', '☑', '⚠', 'CA-IV-', 'R-IV-01', 'hors du rendu', 'à re-vérifier à la rédaction']
ALLOWED_WARNING = '⚠ Échelle propre à ce document'  # avertissement voulu de NiveauMaturité p. 1 (PLAN P4)
TEST_DIGEST = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'  # SHA-256 de "test"

YEAR = re.compile(r'\([^()]*?(?<!\d)(?:1[89]\d\d|20\d\d)(?!\d)[a-z]?[^()]*?\)\.|\(s\.\s?d\.\)\.')
UE_ID = re.compile(r"(?:Règlement|Directive)(?: délégué| d'exécution)? \(UE\) (?:n° )?(\d{4}/\d+)")
RFC_ID = re.compile(r'\bIETF,? (?:Internet Standard STD \d+, )?RFC ?(\d{3,5})\b')
ARXIV_ID = re.compile(r'(?:arXiv[: ]?|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})', re.I)

results = []


def check(name, ok, detail=''):
    results.append(bool(ok))
    print(f"{'OK   ' if ok else 'ÉCHEC'}  {name}" + (f' — {detail}' if detail else ''))


def norm(text):
    """Texte comparable : césures recollées, U+00AD retirés, blancs réduits à une espace."""
    text = text.replace('\xad\n', '').replace('\xad', '')
    text = re.sub(r'(?<=\S)-\n', '-', text)
    return re.sub(r'\s+', ' ', text)


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def jcs(obj):
    # shortcut: tri par point de code et repr des flottants de Python, conformes à RFC 8785 pour des clés ASCII
    # et des nombres usuels; passer à une implémentation JCS complète si les exemples changent de nature.
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def section(doc, prefix):
    """Pages (1-based, bornes incluses) de la première entrée du sommaire qui commence par prefix."""
    toc = doc.get_toc()
    i = next(i for i, (_, title, _) in enumerate(toc) if title.startswith(prefix))
    level, _, start = toc[i]
    end = next((page - 1 for lvl, _, page in toc[i + 1:] if lvl <= level), doc.page_count)
    return start, end


def page_text(page):
    """Texte de la page dans l'ordre visuel des lignes : un contenu retouché ou déplacé arrive en fin de flux."""
    lines = [(round(l['spans'][0]['origin'][1]), l['bbox'][0], ''.join(s['text'] for s in l['spans']))
             for b in page.get_text('dict')['blocks'] for l in b.get('lines', [])]
    return '\n'.join(t for _, _, t in sorted(lines))


def link_page(link, names):
    """Page cible d'un lien interne; PyMuPDF lit en Latin-1 les noms de destination UTF-8 de Typst, d'où le recodage."""
    if link.get('page') is not None:
        return link['page']
    name = link.get('nameddest', '')
    try:
        name = name.encode('latin-1').decode('utf-8')
    except UnicodeError:
        pass
    return names.get(name, {}).get('page', -1)


def is_note(entry):
    """Note de méthode ou d'errata aspirée dans la bibliographie (PLAN P1.4) :
    un « : » hors parenthèses avant le premier « (année). », ou aucun « (année). »."""
    year = YEAR.search(entry)
    depth = 0
    for i, ch in enumerate(entry[:year.start()] if year else entry):
        depth += (ch == '(') - (ch == ')')
        if depth == 0 and entry.startswith(' : ', i):
            return True
    return year is None


def primary_id(entry):
    """Identifiant propre de l'entrée, et non d'un texte qu'elle cite."""
    year = YEAR.search(entry)
    if year and (m := UE_ID.match(entry[year.end():].lstrip())):
        return f'UE {m.group(1)}'
    if m := RFC_ID.search(entry):
        return f'RFC {m.group(1)}'
    if m := ARXIV_ID.search(entry):
        return f'arXiv:{m.group(1)}'
    return None


def selftest():
    assert norm('sys\xad\ntèmes CA-\nIV-01  a') == 'systèmes CA-IV-01 a'
    assert is_note('SEC S7-12-23 : retiré le 12.6.2025 (Release 33-11377).')
    assert is_note('Anti-hype : les tailles de marché divergentes sont conservées.')
    assert not is_note('Hardt, D. (Ed.) (2012). The OAuth 2.0 Authorization Framework. IETF RFC 6749.')
    assert not is_note('OWASP MCP Top 10 Project (lead : V. Verma Sehgal) (2025). OWASP MCP Top 10.')
    assert not is_note('ASC X12 (s. d.). ASC X12 — Electronic Data Interchange : normes.')
    assert primary_id('Hardt, D. (2012). The OAuth 2.0 Framework. IETF, RFC 6749. DOI 10.17487/RFC6749.') == 'RFC 6749'
    assert primary_id('Okta (2025). Cross App Access (fondée sur token exchange/RFC 8693).') is None
    assert primary_id('Commission européenne (2018). Règlement délégué (UE) 2018/389 — RTS sous PSD2 '
                      '(Directive (UE) 2015/2366).') == 'UE 2018/389'
    assert primary_id('CEN-CENELEC JTC 21 (2021-2026). Work Programme : en appui du Règlement (UE) 2024/1689.') is None
    assert primary_id('Qiang, Z. (2024). Agent-OM. arXiv:2312.00326v3.') == 'arXiv:2312.00326'
    assert sha256('test') == TEST_DIGEST


def check_documents(docs, texts):
    for key, doc in docs.items():
        names = doc.resolve_names()
        broken = sum(1 for page in doc for link in page.get_links()
                     if link['kind'] in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED)
                     and not 0 <= link_page(link, names) < doc.page_count)
        check(f'{key} : liens internes', broken == 0, f'{broken} lien(s) rompu(s)' if broken else '')

        meta, toc = doc.metadata, doc.get_toc()
        problems = [f'author={meta["author"]!r}'] if meta['author'] != AUTHOR else []
        problems += ['title vide'] if not meta['title'] else []
        problems += ['aucun signet'] if not toc else []
        check(f'{key} : métadonnées et signets', not problems, ', '.join(problems))

        text = norm('\n'.join(texts[key]))
        if key == 'NiveauMaturité':
            text = text.replace(ALLOWED_WARNING, '')
        found = {m: text.count(m) for m in MARKERS if m in text}
        check(f'{key} : marqueurs de chantier', not found, ', '.join(f'{m} ×{n}' for m, n in found.items()))


def check_typography(docs, texts):
    soft = '\n'.join(texts['NiveauMaturité']).count('\xad')
    check('NiveauMaturité : U+00AD', soft == 0, f'{soft} occurrence(s)' if soft else '')
    etal = norm('\n'.join(texts['Revue'])).count('et al..')
    check('Revue : « et al.. »', etal == 0, f'{etal} occurrence(s)' if etal else '')
    lines = [l for l in texts['Veille'][-1].splitlines() if l.strip() and not l.strip().isdigit()]
    check('Veille : dernière page non veuve (≥ 5 lignes)', len(lines) >= 5, f'{len(lines)} ligne(s) p. {docs["Veille"].page_count}')


def cadre_digests(annex_c):
    """Écarts entre les condensés affichés à l'Annexe C et leur recalcul (PLAN P2.1)."""
    dec = json.JSONDecoder()

    def json_after(pattern):
        return dec.raw_decode(annex_c, annex_c.index('{', re.search(pattern, annex_c).end()))[0]

    definition = json_after(r'Définition de l.outil')
    record = json_after(r'Enregistrement d.audit canonisé')['enregistrement']
    submitted = re.search(r'outil\s*:\s*(\S+)\s+arguments\s*:\s*', annex_c)
    tool = submitted.group(1)
    args, end = dec.raw_decode(annex_c, submitted.end())
    h = re.compile(r'\s*h\s*:\s*([0-9a-f]{64})').match(annex_c, end).group(1)
    shown_definition = re.search(r'"definition_digest":\s*"sha256:([0-9a-f]{64})"', annex_c).group(1)
    shown_action = re.search(r'"action_sha256":\s*"([0-9a-f]{64})"', annex_c).group(1)

    h_calc = sha256(tool + jcs(args))
    key_calc = sha256(f"{record['correlation']['tache']}|{record['correlation']['etape']}")
    pairs = {
        'h (C.6)': (h, h_calc),
        'action_sha256 (C.6)': (shown_action, h_calc),
        'empreinte_approbation (C.8)': (record['autorite']['empreinte_approbation'], h_calc),
        'definition_digest (C.2)': (shown_definition, sha256(jcs(definition))),
        'idempotency_key (C.6)': (args['idempotency_key'], key_calc),
        'cle_idempotence (C.8)': (record['correlation']['cle_idempotence'], key_calc),
        'arguments_sha256 (C.8)': (record['action']['arguments_sha256'], sha256(jcs(args))),
    }
    return [f'{name} : affiché {shown[:12]}…, recalculé {calc[:12]}…'
            for name, (shown, calc) in pairs.items() if shown != calc]


def check_cadre(doc, pages):
    def text(start, end):
        return '\n'.join(pages[start - 1:end])

    annexes, _ = section(doc, 'Annexes')
    d_start, d_end = section(doc, 'D ')
    g_start, g_end = section(doc, 'G ')

    def requirements(t):
        return {f'EXIG-{a}-{b}' for a, b in re.findall(r'EXIG-\s?([A-Z]+)-\s?(\d+)', norm(t))}
    body, registry = requirements(text(1, annexes - 1)), requirements(text(d_start, d_end))
    check('Cadre : exigences du corps == Annexe D', body == registry,
          f'corps {len(body)}, annexe D {len(registry)}; absentes de D : {sorted(body - registry)[:5]}; '
          f'absentes du corps : {sorted(registry - body)[:5]}' if body != registry else f'{len(body)} exigences')

    numbers = [int(n) for n in re.findall(r'^\[(\d+)\]', text(g_start, g_end), re.M)]
    cited = set()
    for group in re.findall(r'\[(\d+(?:\s*[,–-]\s*\d+)*)\]', norm(text(1, g_start - 1))):
        for part in group.split(','):
            a, _, b = re.sub(r'\s', '', part).replace('–', '-').partition('-')
            cited.update(range(int(a), int(b or a) + 1))
    cited.discard(0)  # « [0] » d'un exemple de code, pas une citation
    refs = set(numbers)
    ok = cited == refs and len(numbers) == len(refs)
    check('Cadre : références citées == Annexe G', ok,
          f'{len(refs)} références' if ok else f'annexe G {len(numbers)} entrées ({len(refs)} numéros), citées {len(cited)}; '
          f'non citées : {sorted(refs - cited)[:5]}; citées absentes : {sorted(cited - refs)[:5]}')

    c_start, c_end = section(doc, 'C ')
    try:
        gaps = cadre_digests(norm(text(c_start, c_end)))
    except (AttributeError, KeyError, StopIteration, ValueError) as exc:
        gaps = [f'Annexe C illisible ({type(exc).__name__} : {exc})']
    check('Cadre : condensés de l\'Annexe C recalculés', not gaps, '; '.join(gaps))
    stale = norm('\n'.join(pages)).count(TEST_DIGEST)
    check('Cadre : condensé de « test » absent', stale == 0, f'{stale} occurrence(s)' if stale else '')


def check_bibliography(doc, pages):
    start, end = section(doc, 'Annexe I')
    annex = norm('\n'.join(pages[start - 1:end]))
    entries = annex.split('• ')[1:]

    notes = [e for e in entries if is_note(e)]
    check('Compendium : notes infiltrées dans l\'Annexe I', not notes,
          f'{len(notes)}, p. ex. « {notes[0][:60]}… »' if notes else '')

    groups = defaultdict(int)
    for entry in entries:
        if key := primary_id(entry):
            groups[key] += 1
    dups = {k: n for k, n in sorted(groups.items()) if n > 1}
    check('Compendium : doublons d\'identifiant (arXiv, RFC, UE)', not dups,
          ', '.join(f'{k} ×{n}' for k, n in dups.items()))

    crr = [e for e in entries if re.search(r'\bCRR ?(?:III|3)\b', e) and '2024/1619' in e]
    check('Compendium : CRR III sous 2024/1623 seulement', not crr, f'{len(crr)} entrée(s) CRR III sous 2024/1619' if crr else '')

    shown = re.search(r'Entrées uniques de la présente annexe (\d+)', annex)
    total = int(shown.group(1)) if shown else None
    check('Compendium : total affiché == entrées réelles', total == len(entries),
          f'affiché {total}, réel {len(entries)}')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    selftest()
    try:
        (ROOT / 'README.md').read_text(encoding='utf-8')
        docs = {key: pymupdf.open(ROOT / name) for key, name in PDFS.items()}
    except Exception as exc:  # fichier absent ou illisible : rien d'autre n'est vérifiable
        check('Présence : 5 PDF et README lisibles', False, str(exc))
        return 1
    check('Présence : 5 PDF et README lisibles', True)
    texts = {key: [page_text(page) for page in doc] for key, doc in docs.items()}

    check_documents(docs, texts)
    check_typography(docs, texts)
    check_cadre(docs['Cadre'], texts['Cadre'])
    check_bibliography(docs['Compendium'], texts['Compendium'])

    print(f'\n{sum(results)}/{len(results)} contrôles réussis')
    return 0 if all(results) else 1


if __name__ == '__main__':
    sys.exit(main())
