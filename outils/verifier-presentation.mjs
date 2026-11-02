// Vérifie la mise en page de Presentation_Haute_Direction.html dans Edge ou Chrome sans interface.
//
// Pour chaque diapositive : débordement horizontal, cartes qui débordent, blocs qui se
// chevauchent (ou qui empiètent sur le pied de page) et plus petite taille de texte.
//
// Usage : node outils/verifier-presentation.mjs [largeur] [hauteur] [options]
//   options : print          mise en page d'impression (média print émulé)
//             block          bloque Google Fonts (cas hors ligne, police de repli)
//             pdf=sortie.pdf écrit aussi le PDF A4 paysage
//   Navigateur : variable d'environnement NAVIGATEUR, sinon Edge puis Chrome aux emplacements usuels.
//
// Code de sortie : 0 si tout est conforme, 1 sinon.
import { spawn } from 'node:child_process';
import { existsSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const [W = 1366, H = 768] = args.filter((a) => /^\d+$/.test(a)).map(Number);
const PRINT = args.includes('print');
const BLOCK = args.includes('block');
const PDF = (args.find((a) => a.startsWith('pdf=')) || '').slice(4);
const PORT = 9200 + Math.floor(Math.random() * 700);

const page = pathToFileURL(fileURLToPath(new URL('../Presentation_Haute_Direction.html', import.meta.url))).href;
const browser = [
  process.env.NAVIGATEUR,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/microsoft-edge',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => p && existsSync(p));
if (!browser) { console.error('Aucun navigateur Chromium trouvé : définir NAVIGATEUR.'); process.exit(2); }

const proc = spawn(browser, [
  '--headless=new', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'verif-pres-'))}`, 'about:blank',
]);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const quit = (code) => { try { proc.kill(); } catch {} process.exit(code); };
setTimeout(() => { console.error('Délai dépassé'); quit(2); }, 100000);

let tabs;
for (let i = 0; i < 40 && !tabs?.length; i++) {
  try { tabs = await (await fetch(`http://127.0.0.1:${PORT}/json`)).json(); } catch { await sleep(250); }
}
const ws = new WebSocket(tabs.find((t) => t.type === 'page').webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0;
const pending = {};
ws.onmessage = (e) => { const m = JSON.parse(e.data); pending[m.id]?.(m); };
const send = (method, params = {}) =>
  new Promise((r) => { pending[++id] = r; ws.send(JSON.stringify({ id, method, params })); })
    .then((m) => { if (m.error) throw new Error(`${method} : ${m.error.message}`); return m.result; });
const ev = async (expression) => (await send('Runtime.evaluate', { expression, returnByValue: true })).result.value;

await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 780 });
if (BLOCK) {
  await send('Network.enable');
  await send('Network.setBlockedURLs', { urls: ['*fonts.googleapis.com*', '*fonts.gstatic.com*'] });
}
await send('Page.navigate', { url: page });
await sleep(2500);
if (PRINT) { await send('Emulation.setEmulatedMedia', { media: 'print' }); await sleep(400); }

const fonts = await ev(`[...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight))].join(', ') || 'aucune (repli système)'`);
console.log(`${W}×${H} · ${PRINT ? 'impression' : 'écran'} · polices web : ${fonts}`);

const probe = (i) => `(() => {
  const s = document.querySelectorAll('.slide')[${i}];
  const deep = (e) => Math.max(e.getBoundingClientRect().bottom, ...[...e.querySelectorAll('*')].map((c) => c.getBoundingClientRect().bottom));
  const issues = [];
  if (s.scrollWidth > s.clientWidth + 1) issues.push('débordement horizontal ' + (s.scrollWidth - s.clientWidth) + ' px');
  const blocks = [...s.querySelector('.slide-body').children, s.querySelector('.slide-foot')];
  for (let k = 0; k < blocks.length - 1; k++) {
    const ov = deep(blocks[k]) - blocks[k + 1].getBoundingClientRect().top;
    if (ov > 1) issues.push(blocks[k].className.split(' ')[0] + ' chevauche ' + blocks[k + 1].className.split(' ')[0] + ' de ' + Math.round(ov) + ' px');
  }
  const out = deep(blocks[blocks.length - 1]) - s.getBoundingClientRect().bottom;
  if (out > 1) issues.push('pied de page hors diapositive de ' + Math.round(out) + ' px');
  s.querySelectorAll('.card,.dec-box,.res-card,.phase-card,.kpi,.stat-box,.doc-tile,.tier-row,.arch-layer,.callout,.hero-main')
    .forEach((b) => { if (b.scrollHeight > b.clientHeight + 1) issues.push(b.className.split(' ')[0] + ' déborde de ' + (b.scrollHeight - b.clientHeight) + ' px'); });
  let min = Infinity;
  s.querySelectorAll('*').forEach((el) => {
    if ([...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) min = Math.min(min, parseFloat(getComputedStyle(el).fontSize));
  });
  return { min: min.toFixed(1), issues };
})()`;

let failures = 0;
for (let i = 0; i < 12; i++) {
  if (!PRINT) { await ev(`document.querySelectorAll('.dot')[${i}].click()`); await sleep(450); }
  const { min, issues } = await ev(probe(i));
  if (issues.length) failures++;
  console.log(`${String(i + 1).padStart(2, '0')}  texte min ${min} px  ${issues.join(' · ') || 'OK'}`);
}

if (PDF) {
  await send('Emulation.setEmulatedMedia', { media: '' });
  const { data } = await send('Page.printToPDF', { preferCSSPageSize: true, printBackground: true });
  writeFileSync(PDF, Buffer.from(data, 'base64'));
  console.log(`PDF écrit : ${PDF}`);
}
console.log(failures ? `${failures} diapositive(s) en défaut` : 'Tout est conforme');
quit(failures ? 1 : 0);
