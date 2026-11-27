#!/usr/bin/env python3
"""Fase 1 técnica site-wide casasdigital.es — 27-nov-2026
1. ProfessionalService JSON-LD con areaServed (6 municipios bahía) en todas las páginas
2. dateModified (meta + schema) en todas
3. BreadcrumbList schema (según breadcrumb visible)
4. Footer 'Zonas' → 6 ciudades SEO + 6 diseño web (exact anchors)
5. CSS version bump
Idempotente: si ya existe ProfessionalService, lo reemplaza; si ya hay footer nuevo, no duplica.
"""
import re, glob, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
TODAY = "2026-11-27"
OLD_CSS, NEW_CSS = "style.css?v=20261121c", "style.css?v=20261127a"
SITE = "https://casasdigital.es/"

CITIES = [  # slug, nombre, wikipedia
    ("cadiz", "Cádiz", "https://es.wikipedia.org/wiki/C%C3%A1diz"),
    ("jerez", "Jerez de la Frontera", "https://es.wikipedia.org/wiki/Jerez_de_la_Frontera"),
    ("san-fernando", "San Fernando", "https://es.wikipedia.org/wiki/San_Fernando_(Espa%C3%B1a)"),
    ("chiclana", "Chiclana de la Frontera", "https://es.wikipedia.org/wiki/Chiclana_de_la_Frontera"),
    ("puerto-real", "Puerto Real", "https://es.wikipedia.org/wiki/Puerto_Real"),
    ("puerto-santa-maria", "El Puerto de Santa María", "https://es.wikipedia.org/wiki/El_Puerto_de_Santa_Mar%C3%ADa"),
]

def slug_url(p):
    return SITE if p == "index.html" else SITE + p

def localbiz(p):
    area = ",\n".join(f'    {{"@type": "City", "name": "{n}", "sameAs": "{w}"}}' for _, n, w in CITIES)
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "{SITE}#org",
  "name": "Casas Digital",
  "alternateName": "Juan Casas — Consultor SEO Cádiz",
  "description": "Agencia SEO y diseño web en la Bahía de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María. SEO local, diseño web desde 300€, auditorías SEO, Google Business Profile y automatizaciones para empresas.",
  "url": "{SITE}",
  "telephone": "+34610304263",
  "email": "hola@casasdigital.es",
  "priceRange": "300€ - 1500€",
  "image": "{SITE}img/juan1.jpg",
  "founder": {{"@type": "Person", "name": "Juan Casas", "jobTitle": "Consultor SEO", "url": "{SITE}"}},
  "address": {{"@type": "PostalAddress", "addressLocality": "Cádiz", "addressRegion": "Andalucía", "addressCountry": "ES"}},
  "areaServed": [
{area}
  ],
  "serviceType": ["SEO local", "Diseño web", "Auditoría SEO", "Google Business Profile", "Consultoría SEO", "Automatizaciones"],
  "sameAs": ["https://www.linkedin.com/in/juanjesuscasas/"],
  "makesOffer": [
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Diseño web SEO", "url": "{SITE}diseno-web-seo.html"}}}},
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "SEO local mensual", "url": "{SITE}seo-local.html"}}}},
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Auditoría SEO", "url": "{SITE}auditoria-seo.html"}}}},
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Google Business Profile", "url": "{SITE}google-business-profile.html"}}}}
  ]
}}
</script>'''

FOOTER_ZONAS = '''<div class="footer__zones">
    <span class="footer__zones-title">Agencia SEO en la Bahía de Cádiz</span>
    <div class="footer__zones-links">
      <a href="seo-cadiz.html">SEO Cádiz</a>
      <a href="seo-jerez.html">SEO Jerez</a>
      <a href="seo-san-fernando.html">SEO San Fernando</a>
      <a href="seo-chiclana.html">SEO Chiclana</a>
      <a href="seo-puerto-real.html">SEO Puerto Real</a>
      <a href="seo-puerto-santa-maria.html">SEO El Puerto de Santa María</a>
      <a href="seo-bahia-cadiz.html">SEO Bahía de Cádiz</a>
    </div>
  </div>
  <div class="footer__zones">
    <span class="footer__zones-title">Diseño web en la Bahía de Cádiz</span>
    <div class="footer__zones-links">
      <a href="diseno-web-cadiz.html">Diseño web Cádiz</a>
      <a href="diseno-web-jerez.html">Diseño web Jerez</a>
      <a href="diseno-web-san-fernando.html">Diseño web San Fernando</a>
      <a href="diseno-web-chiclana.html">Diseño web Chiclana</a>
      <a href="diseno-web-puerto-real.html">Diseño web Puerto Real El Puerto</a>
      <a href="diseno-web-puerto-santa-maria.html">Diseño web El Puerto de Santa María</a>
      <a href="diseno-web-bahia-cadiz.html">Diseño web Bahía de Cádiz</a>
    </div>
  </div>'''

def breadcrumb_schema(trail):  # trail = [(name, url), ...]
    items = []
    for i, (name, url) in enumerate(trail, 1):
        items.append(f'    {{"@type": "ListItem", "position": {i}, "name": "{name}", "item": "{url}"}}')
    return '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n' + ",\n".join(items) + "\n  ]\n}\n</script>"

def trail_from_html(html, page_path):
    """Breadcrumb visible -> [(name,url)]. Home 'Inicio' -> SITE."""
    m = re.search(r'<div class="breadcrumb">(.*?)</div>', html, re.S)
    if not m:
        return [("Inicio", SITE)]
    trail = []
    for href, txt in re.findall(r'<a href="([^"]+)">([^<]+)</a>', m.group(1)):
        if href.startswith("/"):
            url = SITE + href[1:]
        elif href.startswith("http"):
            url = href
        else:
            url = SITE + href.split("#")[0]
        trail.append((txt.strip(), url))
    # último nivel = texto sin enlace
    last = re.sub(r'<[^>]+>', '', m.group(1)).split('›')[-1].strip()
    if last:
        trail.append((last, slug_url(page_path)))
    return trail or [("Inicio", SITE)]

def process(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html
    # CSS bump
    html = html.replace(OLD_CSS, NEW_CSS)
    # quitar schema viejo si existiera (idempotencia)
    html = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "ProfessionalService".*?</script>\s*', '', html, flags=re.S)
    html = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "BreadcrumbList".*?</script>\s*', '', html, flags=re.S)
    # insertar ProfessionalService + BreadcrumbList antes de </head>
    trail = trail_from_html(html, path)
    block = localbiz(path) + "\n" + breadcrumb_schema(trail) + "\n"
    html = html.replace("</head>", block + "</head>", 1)
    # dateModified meta
    if 'name="article:modified_time"' not in html:
        html = html.replace('<meta name="robots" content="index,follow">',
                            f'<meta name="robots" content="index,follow">\n<meta property="article:modified_time" content="{TODAY}">', 1)
    # footer zonas (idempotente: solo si no está ya la nueva versión)
    if 'Agencia SEO en la Bahía de Cádiz</span>' not in html:
        m = re.search(r'<div class="footer__zones">\s*<span class="footer__zones-title">Zonas</span>.*?</div>\s*</div>', html, re.S)
        if m:
            html = html[:m.start()] + FOOTER_ZONAS + html[m.end():]
        else:
            # sin footer zonas: insertar antes del <p> de copyright
            m2 = re.search(r'(<footer class="footer">.*?)(\s*<p>&copy;)', html, re.S)
            if m2:
                html = html[:m2.start(2)] + "\n  " + FOOTER_ZONAS + "\n  " + html[m2.start(2):]
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return html != orig

if __name__ == "__main__":
    pages = sorted(glob.glob("*.html") + glob.glob("blog/*.html"))
    pages = [p for p in pages if p != "index.html"]  # index: schema propio (Person+FAQPage) -> tools/optimize_home_eeat.py
    changed = 0
    for p in pages:
        if p in ("contacto-gracias.html",):
            continue
        if process(p):
            changed += 1
    print(f"procesadas {len(pages)} · modificadas {changed}")
    # verificación
    ok_lb = ok_bc = ok_dm = ok_fz = 0
    for p in pages:
        h = open(p, encoding="utf-8").read()
        ok_lb += '"@type": "ProfessionalService"' in h
        ok_bc += '"@type": "BreadcrumbList"' in h
        ok_dm += 'article:modified_time" content="2026-11-27' in h
        ok_fz += 'Agencia SEO en la Bahía de Cádiz</span>' in h
    print(f"ProfessionalService {ok_lb}/{len(pages)} · Breadcrumb {ok_bc}/{len(pages)} · dateModified {ok_dm}/{len(pages)} · footerZonas {ok_fz}/{len(pages)}")

