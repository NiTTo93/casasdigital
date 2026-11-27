# -*- coding: utf-8 -*-
"""Auditoría UX + crawlabilidad + semántica + interlinking de casasdigital.es (local)."""
import re, glob, os, json, sys
from collections import Counter, defaultdict

pages = sorted(glob.glob('*.html') + glob.glob('blog/*.html'))
R = {}
def body(h): return re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', '', h, flags=re.S)
def txt(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()

print("=" * 70); print("1. SEMÁNTICA DE HEADINGS (H1 único, jerarquía, saltos)"); print("=" * 70)
for p in pages:
    b = body(open(p, encoding='utf-8').read())
    hs = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', b, re.S)
    h1 = [txt(t) for g, t in hs if g == 'h1']; h2 = [txt(t) for g, t in hs if g == 'h2']
    h3 = sum(1 for g, _ in hs if g == 'h3')
    # saltos de nivel (h2 -> h4 sin h3)
    lv = [int(g[1]) for g, _ in hs]; jumps = sum(1 for i in range(1, len(lv)) if lv[i] - lv[i-1] > 1)
    flag = []
    if len(h1) != 1: flag.append(f"H1x{len(h1)}")
    if jumps: flag.append(f"saltos={jumps}")
    if h3 == 0 and len(h2) >= 6: flag.append("sin H3")
    print(f"{p:45s} H1={len(h1)} H2={len(h2):2d} H3={h3:2d} {' | '.join(flag)}")
    if p in ('index.html', 'servicios.html', 'seo-cadiz.html', 'diseno-web-cadiz.html', 'blog/index.html', 'blog/como-aparecer-google-maps-cadiz.html'):
        for g, t in hs:
            if g in ('h1', 'h2'): print(f"      {g}: {txt(t)[:90]}")

print(); print("=" * 70); print("2. INTERLINKING (enlaces internos por página, huérfanas, más enlazadas)"); print("=" * 70)
out = {}; inn = Counter(); anchors_to = defaultdict(list)
for p in pages:
    b = body(open(p, encoding='utf-8').read())
    b = re.sub(r'<nav.*?</nav>|<footer.*?</footer>', '', b, flags=re.S)  # solo cuerpo
    links = set()
    for href in re.findall(r'<a[^>]+href="([^"]+)"', b):
        if href.startswith(('http', 'mailto:', 'tel:', '#')) or href in ('', '/'): continue
        h2 = href.split('#')[0].split('?')[0]
        tgt = os.path.normpath(os.path.join(os.path.dirname(p), h2))
        if h2.endswith('/') or (not os.path.splitext(h2)[1] and os.path.isdir(tgt)): tgt = os.path.join(tgt, 'index.html')
        if os.path.exists(tgt):
            links.add(tgt); inn[tgt] += 1
            for m in re.finditer(r'<a[^>]+href="' + re.escape(href) + r'"[^>]*>(.*?)</a>', b, re.S):
                anchors_to[tgt].append(txt(m.group(1)))
    out[p] = links
for p in pages:
    if inn[p] <= 1: print(f"  HUÉRFANA/casi: {p}  (recibe {inn[p]} enlaces de cuerpo)")
print("\n  Enlaces de cuerpo que salen de cada página (menos de 3 = débil):")
for p in pages:
    if len(out[p]) < 3 and not p.startswith('blog/'): print(f"  {len(out[p])} → {p}")
print("\n  Top 12 páginas más enlazadas desde el cuerpo:")
for p, n in inn.most_common(12): print(f"  {n:3d} ← {p}")
print("\n  Anclas hacia diseño web (¿genéricas?) para las 6 ciudades + hub:")
for tgt in ['diseno-web-bahia-cadiz.html'] + [f'diseno-web-{c}.html' for c in ['cadiz', 'jerez', 'san-fernando', 'chiclana', 'puerto-real', 'puerto-santa-maria']]:
    a = Counter(anchors_to.get(tgt, [])); print(f"  {tgt:32s} {dict(a.most_common(4))}")
print("\n  Anclas hacia SEO ciudades:")
for tgt in [f'seo-{c}.html' for c in ['cadiz', 'jerez', 'san-fernando', 'chiclana', 'puerto-real', 'puerto-santa-maria']]:
    a = Counter(anchors_to.get(tgt, [])); print(f"  {tgt:32s} {dict(a.most_common(3))}")

print(); print("=" * 70); print("3. CRAWLEABILIDAD (robots, canonical, noindex, sitemap vs disco, hreflang/og)"); print("=" * 70)
sm = set(re.findall(r'<loc>([^<]+)</loc>', open('sitemap.xml', encoding='utf-8').read()))
sm_paths = {u.replace('https://casasdigital.es/', '') or 'index.html' for u in sm}
disk = set(pages) | {'blog/index.html'}
print("  robots.txt:", open('robots.txt').read().replace('\n', ' | ')[:200])
for p in pages:
    h = open(p, encoding='utf-8').read(); b = body(h)
    can = re.search(r'rel="canonical" href="([^"]+)"', b); can = can.group(1) if can else None
    ni = 'noindex' in b; base = 'https://casasdigital.es/'
    expected = base + ('' if p == 'index.html' else p)
    flag = []
    if ni: flag.append("NOINDEX")
    if can and can.rstrip('/') != expected.rstrip('/'): flag.append(f"canonical={can}")
    if not can: flag.append("SIN canonical")
    key = p if p != 'blog/index.html' else 'blog/'
    if key not in sm_paths and p not in sm_paths and (p.rstrip('index.html') or '') not in sm_paths and (p[:-5] if p.endswith('index.html') else p) not in sm_paths and p not in sm_paths:
        # tolerancia: sitemap usa .html para todo, blog/ para el índice
        if not (p == 'blog/index.html' and 'blog/' in sm_paths): flag.append("NO en sitemap")
    if flag and not ni: print(f"  {p:45s} {' | '.join(flag)}")
    if ni: print(f"  {p:45s} NOINDEX (correcto si es gracias/privacidad-result)")
print("  URLs en sitemap que NO existen en disco:", [u for u in sm if u.replace(base, '').replace('blog/', 'blog/index.html') not in disk and u.rstrip('/') != base] or "ninguna")

print(); print("=" * 70); print("4. UX / MÓVIL (nav, hamburguesa, CTA, tap targets, tablas, imágenes sin alt, contraste básico)"); print("=" * 70)
css = open('css/style.css', encoding='utf-8').read()
print("  @media en CSS:", Counter(re.findall(r'@media\s*\(([^)]+)\)', css)).most_common(6))
print("  .nav__links tiene regla móvil?:", bool(re.search(r'@media[^{]*\{[^@]*\.nav__links', css)))
print("  hamburguesa JS bind:", "hamburger" in open('js/main.js', encoding='utf-8').read() if os.path.exists('js/main.js') else 'sin js/main.js')
h = open('index.html', encoding='utf-8').read()
print("  nav HTML en index:", len(re.findall(r'<a[^>]+href="[^"]*"[^>]*>', re.search(r'<nav.*?</nav>', h, re.S).group(0))), "enlaces")
for p in pages:
    b = body(open(p, encoding='utf-8').read())
    imgs = re.findall(r'<img[^>]+>', b); noalt = [i for i in imgs if 'alt=' not in i]
    lazy = sum(1 for i in imgs if 'loading="lazy"' not in i)
    wh = sum(1 for i in imgs if not re.search(r'width=', i))
    tables = b.count('<table')
    if noalt or (lazy and imgs) or (wh and imgs) or tables:
        print(f"  {p:45s} img={len(imgs)} sinAlt={len(noalt)} sinLazy={lazy} sinWidth={wh} tablas={tables}")
cta = Counter()
for p in pages:
    b = body(open(p, encoding='utf-8').read()); b = re.sub(r'<nav.*?</nav>|<footer.*?</footer>', '', b, flags=re.S)
    for t in re.findall(r'<a[^>]+class="[^"]*btn[^"]*"[^>]*>(.*?)</a>', b, re.S): cta[txt(t)] += 1
print("\n  Textos de botones CTA (consistencia):", cta.most_common(10))
print("  tel:/wa.me en cuerpo:", sum(1 for p in pages if re.search(r'href="(tel:|https://wa\.me)', re.sub(r'<nav.*?</nav>|<footer.*?</footer>', '', body(open(p, encoding='utf-8').read()), flags=re.S))), "páginas")
