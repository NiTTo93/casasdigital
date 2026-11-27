# -*- coding: utf-8 -*-
"""Generador de páginas de ciudad (SEO + Diseño web) y hubs — casasdigital.es
  python3 tools/gen_city_pages.py seo   -> 6 seo-<ciudad>.html
  python3 tools/gen_city_pages.py dw    -> 6 diseno-web-<ciudad>.html
  python3 tools/gen_city_pages.py hubs  -> seo-bahia-cadiz.html + diseno-web-bahia-cadiz.html
Reutiliza head/nav/footer de seo-chiclana.html (ya con schema Fase 1) y sustituye el cuerpo.
"""
import re, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from city_data import CITIES, FLEET, SITE, WA, TODAY, YEAR, kw_seo, kw_dw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
ORDER = ["cadiz", "jerez", "san-fernando", "chiclana", "puerto-real", "puerto-santa-maria"]
SEO_LABEL = {"cadiz": "SEO Cádiz", "jerez": "SEO Jerez", "san-fernando": "SEO San Fernando", "chiclana": "SEO Chiclana",
             "puerto-real": "SEO Puerto Real", "puerto-santa-maria": "SEO El Puerto de Santa María"}
DW_LABEL = {"cadiz": "Diseño web Cádiz", "jerez": "Diseño web Jerez", "san-fernando": "Diseño web San Fernando", "chiclana": "Diseño web Chiclana",
            "puerto-real": "Diseño web Puerto Real", "puerto-santa-maria": "Diseño web El Puerto de Santa María"}

def shell(title, desc, canonical_path, body, faqs, trail, h1_for_breadcrumb=None):
    """devuelve HTML completo a partir del template de seo-chiclana (head/nav/footer con schema)."""
    tpl = open("seo-chiclana.html", encoding="utf-8").read()
    # head: title/desc/canonical
    head_end = tpl.index("</head>")
    head = tpl[:head_end]
    head = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", head, count=1)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', head, count=1)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{SITE}{canonical_path}">', head, count=1)
    # quitar FAQPage schema anterior (lo regeneramos) y ProfessionalService/Breadcrumb antiguo
    head = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>\s*', '', head, flags=re.S)
    head = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "BreadcrumbList".*?</script>\s*', '', head, flags=re.S)
    # nuevo breadcrumb schema
    items = ",\n".join(f'    {{"@type": "ListItem", "position": {i}, "name": "{n}", "item": "{u}"}}' for i, (n, u) in enumerate(trail, 1))
    bc = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n' + items + "\n  ]\n}\n</script>"
    # FAQPage schema
    fq = ""
    if faqs:
        ents = ",\n".join(
            f'    {{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}'
            for q, a in faqs)
        fq = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n' + ents + "\n  ]\n}\n</script>"
    head = head + fq + "\n" + bc + "\n"
    # nav + footer: del template
    nav = re.search(r"<nav.*?</nav>", tpl, re.S).group(0)
    footer = re.search(r"<footer.*?</footer>", tpl, re.S).group(0)
    script = re.search(r"<script>\s*const nav=.*?</script>", tpl, re.S).group(0)
    return head + "</head>\n<body>\n" + nav + "\n" + body + "\n" + footer + "\n" + script + "\n</body>\n</html>\n"

def breadcrumb(trail):
    parts = ['<a href="/">Inicio</a>']
    for n, u in trail[1:-1]:
        parts.append(f'<a href="{u.replace(SITE, "")}">{n}</a>')
    parts.append(trail[-1][0])
    return '<div class="breadcrumb">' + " › ".join(parts) + '</div>'


def faq_block(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        out.append(f'<div class="faq__item"><div class="faq__q">{q}</div><div class="faq__a">{a}</div></div>')
    out.append("</div>")
    return "\n".join(out)

def fleet_block(keys):
    cards = "\n".join(
        f'<div class="result"><div class="result__header"><span class="result__domain">{FLEET[k][0]}</span>'
        f'<span class="result__badge result__badge--live">● Posicionando</span></div>'
        f'<div class="result__desc">{FLEET[k][2]} · <a href="{FLEET[k][1]}" target="_blank" rel="noopener">{k}</a></div></div>'
        for k in keys)
    return f'<div class="results__grid">{cards}</div>'

def neighbors_block(slug, kind):
    c = CITIES[slug]
    lab = SEO_LABEL if kind == "seo" else DW_LABEL
    fn = (lambda s: f"seo-{s}.html") if kind == "seo" else (lambda s: f"diseno-web-{s}.html")
    links = " · ".join(f'<a href="{fn(n)}">{lab[n]}</a>' for n in c["neighbors"])
    return f'<p style="color:var(--gray);font-size:.95rem">También trabajo en la bahía: {links} · <a href="{kind if kind=="seo" else "diseno-web"}-bahia-cadiz.html">{"SEO" if kind=="seo" else "Diseño web"} Bahía de Cádiz</a>.</p>'

# ------------------------------------------------------------------ SEO pages
def seo_body(slug):
    c = CITIES[slug]; k = kw_seo(slug)
    trail = [("Inicio", SITE), ("Servicios", SITE + "servicios.html"), (k["h1"].replace("Agencia SEO en ", "SEO "), SITE + f"seo-{slug}.html")]
    faqs = [
        (f"¿Cuánto cuesta contratar una agencia SEO en {c['short']}?",
         f"Depende del punto de partida y del sector. La auditoría inicial es gratuita; el SEO mensual para un negocio local de {c['short']} suele moverse entre 150 y 400 € al mes, y el diseño web desde 300 €. Antes de pedirte nada te enseño los resultados de otras webs de la bahía que ya están en página 1."),
        (f"¿En cuánto tiempo se ven resultados de SEO en {c['short']}?",
         f"En municipios de la bahía como {c['short']}, con competencia media o baja, las primeras posiciones en búsquedas de cola larga suelen aparecer entre la semana 4 y la 8; las keywords principales («agencia seo», «clínica dental», «fontanero» + ciudad) tardan de 3 a 6 meses. Te paso un seguimiento mensual con las posiciones reales de Search Console."),
        (f"¿Ya tengo web del Kit Digital. ¿Sirve para hacer SEO en {c['short']}?",
         "Sí, casi siempre. La web del Kit Digital no suele ser el problema: el problema es que nadie la ha tocado desde que se entregó. WordPress desactualizado, formularios que no avisan, HTTPS a medias y cero contenido local. Auditarla y arreglarla cuesta mucho menos que rehacerla."),
        (f"¿Trabajas con negocios de cualquier sector en {c['short']}?",
         f"Sí, aunque donde más experiencia tengo es en servicios locales (reformas, climatización, plagas, electricidad), despachos profesionales (abogados, notarías), clínicas dentales y hostelería. Si tu sector es muy especializado, te lo digo en la auditoría antes de empezar."),
        (f"¿Haces SEO solo en {c['short']} o en toda la bahía?",
         "Trabajo en los seis municipios de la bahía: Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María. Para cada uno tengo una página propia porque la búsqueda local cambia de una ciudad a otra, y para Google no es lo mismo."),
    ]
    sectors = "\n".join(f"<li>{s}</li>" for s in c["sectors"])
    angles = "\n".join(f'<h3 style="font-size:1.1rem;margin:28px 0 10px">{t}</h3>\n<p style="color:var(--gray);line-height:1.8;margin-bottom:8px">{b}</p>' for t, b in c["angles"])
    return f'''<section class="page-hero" style="padding-top: 120px;">
<div class="container">
  {breadcrumb(trail)}
  <div class="page-hero__tag">{k['tag']}</div>
  <h1>{k['h1']}</h1>
  <p class="page-hero__sub">Cuando alguien en {c['short']} busca lo que vendes, Google decide en el móvil y en el pack de Maps quién aparece. Trabajo el SEO de {c['name']} con la base técnica, el Google Business Profile y el contenido local que la mayoría de webs de la zona no tiene. Auditoría gratis y precios claros, desde 300 €.</p>
  <div class="hero__btns">
    <a href="contacto.html" class="btn btn--primary">Solicitar auditoría gratis →</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp</a>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">SEO local en {c['name']}</p>
  <h2 class="section__title">{c['pop']}. Un mercado que se busca por nombre de ciudad.</h2>
  <div class="two-col">
    <div>
      <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">Cuando alguien en {c['short']} busca un servicio, Google no muestra «lo mejor de la provincia»: muestra lo que entiende que está en {c['short']}. Eso significa que la web tiene que decir el nombre de la ciudad, el barrio, la zona y el teléfono local, y que el Google Business Profile tiene que decir lo mismo. La mayoría de webs de la zona no lo hacen.</p>
      <p style="color:var(--gray);line-height:1.8">Trabajo el SEO de {c['short']} en tres capas: primero la base técnica y el GBP (lo que decide el pack local), después el contenido que responde a las búsquedas reales de {c['short']}, y por último la autoridad local: citas, reseñas y menciones en medios de la bahía. Sin las tres, el SEO no se sostiene.</p>
      <h3 style="font-size:1.1rem;margin:24px 0 10px">Sectores con más demanda de SEO en {c['short']}</h3>
      <ul class="check-list">{sectors}</ul>
    </div>
    <div>
      <h3 style="font-size:1.1rem;margin-bottom:12px">Webs que ya posicionan en la bahía</h3>
      <p style="color:var(--gray);font-size:.95rem;line-height:1.7;margin-bottom:16px">No vendo humo: estas son webs propias que gestiono y que ya están en página 1 por búsquedas locales de la zona. El mismo método, aplicado a tu negocio.</p>
      {fleet_block(c['fleet_keys'])}
    </div>
  </div>
</div>
</section>

<section class="section">
<div class="container">
  <p class="section__tag">Qué cambia el juego en {c['short']}</p>
  <h2 class="section__title">Tres cosas que ninguna agencia de la bahía te va a contar sobre el SEO en {c['short']}</h2>
  {angles}
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Precios claros</p>
  <h2 class="section__title">Cuánto cuesta el SEO en {c['short']}</h2>
  <div class="two-col">
    <div>
      <table class="price-table">
        <tr><th>Servicio</th><th>Desde</th><th>Qué incluye</th></tr>
        <tr><td>Auditoría SEO</td><td>Gratis</td><td>Análisis de tu web y tu GBP, lista de fallos priorizados y plan a 90 días</td></tr>
        <tr><td>SEO local mensual</td><td>150 €/mes</td><td>GBP, contenido local, enlaces internos, seguimiento mensual de posiciones</td></tr>
        <tr><td>Diseño web + SEO</td><td>300 €</td><td>Web rápida, optimizada para búsquedas de {c['short']}, sin dominio ni hosting</td></tr>
        <tr><td>Automatización / Agente IA</td><td>150 € / 450 €</td><td>Formularios que avisan al móvil, informes automáticos, agente de teléfono 24/7</td></tr>
      </table>
    </div>
    <div>
      <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">Los precios son «desde» porque dependen del número de URLs, de la competencia del sector en {c['short']} y del punto de partida de la web. La auditoría es gratuita y sin compromiso: te digo lo que hay antes de que decidas si seguimos.</p>
      <p style="color:var(--gray);line-height:1.8">Si ya tienes web del Kit Digital, en la mayoría de los casos se aprovecha: se arregla lo que falla y se le añade el SEO que nunca tuvo. Rehacer desde cero solo tiene sentido cuando la web no se puede actualizar.</p>
      <a href="contacto.html" class="btn btn--primary" style="margin-top:12px">Pide tu auditoría gratis →</a>
    </div>
  </div>
</div>
</section>

<section class="section">
<div class="container">
  <p class="section__tag">Cómo trabajo</p>
  <h2 class="section__title">De la auditoría a la primera página en 5 pasos</h2>
  <div class="steps">
    <div class="step"><div class="step__num">1</div><div class="step__body"><h3>Auditoría sin coste</h3><p>Reviso tu web, tu Google Business Profile y a qué te enfrentas en {c['short']}. Te lo explico en una llamada de 20 minutos, con capturas.</p></div></div>
    <div class="step"><div class="step__num">2</div><div class="step__body"><h3>Plan a 90 días</h3><p>Lista priorizada: qué arreglar primero, qué contenido crear y qué palabras atacar en {c['short']} según volumen y competencia reales.</p></div></div>
    <div class="step"><div class="step__num">3</div><div class="step__body"><h3>Base técnica y GBP</h3><p>Velocidad, móvil, schema, canonicals, formulario que avisa al móvil y Google Business Profile actualizado con el nombre de la ciudad.</p></div></div>
    <div class="step"><div class="step__num">4</div><div class="step__body"><h3>Contenido local</h3><p>Páginas por servicio y por zona de {c['short']}, con casos reales de la bahía. Texto que responde a lo que la gente de {c['short']} escribe en Google.</p></div></div>
    <div class="step"><div class="step__num">5</div><div class="step__body"><h3>Seguimiento y escalado</h3><p>Posiciones y llamadas cada mes. Lo que funciona en {c['short']} se replica en los municipios vecinos cuando tiene sentido para el negocio.</p></div></div>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Preguntas frecuentes</p>
  <h2 class="section__title">Dudas habituales antes de contratar SEO en {c['short']}</h2>
  {faq_block(faqs)}
  <div style="margin-top:36px">{neighbors_block(slug, 'seo')}</div>
</div>
</section>

<section class="cta">
<div class="container">
  <h2>¿Tu negocio en {c['short']} no aparece en Google?</h2>
  <p>Auditoría gratuita de tu web y tu Google Business Profile. Te enseño qué falla y qué resultados tienen otras webs de la bahía.</p>
  <div class="cta__btns">
    <a href="contacto.html" class="btn btn--primary">Solicitar auditoría gratis →</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp directo</a>
  </div>
</div>
</section>''', faqs, trail

# ------------------------------------------------------------------ Diseño web pages
def dw_body(slug):
    c = CITIES[slug]; k = kw_dw(slug)
    trail = [("Inicio", SITE), ("Servicios", SITE + "servicios.html"), (k["h1"].replace("Diseño web en ", "Diseño web "), SITE + f"diseno-web-{slug}.html")]
    faqs = [
        (f"¿Cuánto cuesta una página web en {c['short']}?",
         f"Desde 300 €, sin dominio ni hosting (que suelen rondar los 40-60 € al año entre ambos). El precio final depende del número de páginas, de si hay formulario, reserva, catálogo o varias secciones. Te paso presupuesto cerrado antes de empezar, sin sorpresas."),
        ("¿La web del Kit Digital me sirve o tengo que hacerla nueva?",
         "En muchos casos sirve como base. El problema no es la web en sí, sino que se entregó sin SEO, sin velocidad y sin nadie que la mantenga. Se puede arreglar y poner a trabajar; rehacerla solo tiene sentido si está hecha con una herramienta cerrada que no permite tocar nada."),
        ("¿En cuánto tiempo está lista la web?",
         "Una web de 5-6 páginas suele estar lista en 2-3 semanas desde que tengo los textos y las fotos. Antes de publicarla la paso por velocidad, móvil, schema y canonicals, y la doy de alta en Search Console y Bing."),
        ("¿La web aparecerá en Google por sí sola?",
         "No. Publicar una web es el 20 %; el otro 80 % es SEO: contenido por servicio y por ciudad, Google Business Profile, citas locales y enlaces. Por eso todas las webs que hago ya salen con la base SEO montada, y el mantenimiento mensual es opcional pero recomendable."),
        (f"¿Trabajas con negocios de {c['short']} que ya tienen web?",
         f"Sí. Lo más habitual es que lleguen con una web del Kit Digital o de una agencia anterior que no posiciona. La reviso, te digo qué aprovecho y qué rehago, y te paso presupuesto por separado."),
    ]
    angles = "\n".join(f'<h3 style="font-size:1.1rem;margin:28px 0 10px">{t}</h3>\n<p style="color:var(--gray);line-height:1.8;margin-bottom:8px">{b}</p>' for t, b in c["angles"])
    return f'''<section class="page-hero" style="padding-top: 120px;">
<div class="container">
  {breadcrumb(trail)}
  <div class="page-hero__tag">{k['tag']}</div>
  <h1>{k['h1']}</h1>
  <p class="page-hero__sub">Páginas web rápidas, claras y preparadas para que Google te encuentre cuando alguien en {c['short']} busca lo que vendes. Desde 300 €, sin dominio ni hosting, y con la base SEO incluida desde el primer día.</p>
  <div class="hero__btns">
    <a href="contacto.html" class="btn btn--primary">Pedir presupuesto →</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp</a>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Diseño web en {c['name']}</p>
  <h2 class="section__title">Una web que no posiciona es un folleto caro.</h2>
  <div class="two-col">
    <div>
      <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">En {c['short']} casi todos los negocios tienen ya una web. El problema es que la mayoría son folletos: bonitos, con fotos de archivo y un formulario que nadie ve. No aparecen en Google porque nadie hizo SEO, no porque Google sea injusto.</p>
      <p style="color:var(--gray);line-height:1.8">Yo hago webs con un objetivo: que te encuentren. Cada página está escrita para una búsqueda concreta de {c['short']}, con velocidad de carga alta en móvil, schema, canonicals y un formulario que avisa al móvil en el momento. Y después, si quieres, sigo con el SEO mes a mes.</p>
      <h3 style="font-size:1.1rem;margin:24px 0 10px">Qué incluye una web de Casas Digital</h3>
      <ul class="check-list">
        <li>Diseño a medida, adaptado a móvil, sin plantillas de 50 €</li>
        <li>Textos orientados a las búsquedas reales de {c['short']}</li>
        <li>Velocidad y Core Web Vitals en verde desde el primer día</li>
        <li>Schema LocalBusiness, FAQ y servicios; canonicals y sitemap</li>
        <li>Formulario conectado a tu móvil (aviso instantáneo, sin plugins de terceros)</li></li>
        <li>Alta en Google Search Console, Bing e IndexNow</li>
      </ul>
    </div>
    <div>
      <div class="price-box">
        <div class="price-box__label">Página web desde</div>
        <div class="price-box__amount">300 €</div>
        <div class="price-box__note">Sin dominio ni hosting · Presupuesto cerrado antes de empezar</div>
      </div>
      <p style="color:var(--gray);font-size:.95rem;line-height:1.7;margin-top:20px">Las webs que hago para la bahía están publicadas en mi portafolio de resultados. Todas comparten una cosa: cargan rápido y salen en Google por búsquedas de su ciudad.</p>
      <a href="index.html#resultados" class="btn btn--outline" style="margin-top:12px">Ver resultados →</a>
    </div>
  </div>
</div>
</section>

<section class="section">
<div class="container">
  <p class="section__tag">Por qué en {c['short']} la mayoría de webs no venden</p>
  <h2 class="section__title">Lo que veo al auditar webs de negocios de {c['short']}</h2>
  {angles}
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Precios</p>
  <h2 class="section__title">Cuánto cuesta una web en {c['short']}</h2>
  <div class="two-col">
    <div>
      <table class="price-table">
        <tr><th>Tipo de web</th><th>Desde</th><th>Ideal para</th></tr>
        <tr><td>Landing de 1 página</td><td>300 €</td><td>Un servicio principal, campana de captación, lanzamiento</td></tr>
        <tr><td>Web de 5-6 páginas</td><td>600 €</td><td>Negocio local con varios servicios, quieres posicionar en {c['short']}</td></tr>
        <tr><td>Web + SEO mensual</td><td>600 € + 150 €/mes</td><td>Quieres que la web trabaje sola y te traiga llamadas cada mes</td></tr>
        <tr><td>Reparación web Kit Digital</td><td>300 €</td><td>Ya tienes web, pero está abandonada y no posiciona</td></tr>
      </table>
    </div>
    <div>
      <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">Todos los precios son «desde», sin dominio ni hosting. El presupuesto se cierra antes de empezar y no cambia salvo que tú cambies el alcance.</p>
      <p style="color:var(--gray);line-height:1.8">Si vienes de una web del Kit Digital, en la mayoría de los casos la aprovechamos: se arregla lo que falla y se le añade el SEO que nunca tuvo.</p>
      <a href="contacto.html" class="btn btn--primary" style="margin-top:12px">Pide presupuesto →</a>
    </div>
  </div>
</div>
</section>

<section class="section">
<div class="container">
  <p class="section__tag">Proceso</p>
  <h2 class="section__title">De la idea a la web publicada en 5 pasos</h2>
  <div class="steps">
    <div class="step"><div class="step__num">1</div><div class="step__body"><h3>Hablamos de tu negocio</h3><p>Qué vendes, a quién en {c['short']}, qué te diferencia. Sin tecnicismos.</p></div></div>
    <div class="step"><div class="step__num">2</div><div class="step__body"><h3>Presupuesto cerrado</h3><p>Número de páginas, secciones y precio final por escrito. Sin sorpresas.</p></div></div>
    <div class="step"><div class="step__num">3</div><div class="step__body"><h3>Textos y diseño</h3><p>Escribo los textos orientados a las búsquedas de {c['short']} y diseño la web a medida.</p></div></div>
    <div class="step"><div class="step__num">4</div><div class="step__body"><h3>Base SEO y pruebas</h3><p>Velocidad, móvil, schema, canonicals y formulario que avisa al móvil.</p></div></div>
    <div class="step"><div class="step__num">5</div><div class="step__body"><h3>Publicación y alta</h3><p>Search Console, Bing, IndexNow. Tu web empieza a posicionarse desde el día uno.</p></div></div>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Preguntas frecuentes</p>
  <h2 class="section__title">Dudas habituales sobre diseño web en {c['short']}</h2>
  {faq_block(faqs)}
  <div style="margin-top:36px">{neighbors_block(slug, 'dw')}</div>
</div>
</section>

<section class="cta">
<div class="container">
  <h2>¿Quieres una web que te traiga clientes en {c['short']}?</h2>
  <p>Presupuesto cerrado, sin dominio ni hosting obligatorio, y con la base SEO incluida desde el primer día.</p>
  <div class="cta__btns">
    <a href="contacto.html" class="btn btn--primary">Pedir presupuesto →</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp directo</a>
  </div>
</div>
</section>''', faqs, trail

# ------------------------------------------------------------------ Hubs
def hub_body(kind):
    is_seo = kind == "seo"
    title = "Agencia SEO en la Bahía de Cádiz — SEO Local en 6 municipios | Casas Digital" if is_seo else "Diseño web en la Bahía de Cádiz — Webs que posicionan, desde 300€ | Casas Digital"
    desc = ("Agencia SEO en la Bahía de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María. SEO local, GBP y diseño web. Auditoría gratis."
            if is_seo else "Diseño web en la Bahía de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María. Webs rápidas con SEO local, desde 300€.")
    h1 = "Agencia SEO en la Bahía de Cádiz" if is_seo else "Diseño web en la Bahía de Cádiz"
    tag = "SEO Local · Bahía de Cádiz" if is_seo else "Diseño web · Bahía de Cádiz"
    path = f"{kind}-bahia-cadiz.html" if is_seo else "diseno-web-bahia-cadiz.html"
    trail = [("Inicio", SITE), ("Servicios", SITE + "servicios.html"), (h1, SITE + path)]
    lab = SEO_LABEL if is_seo else DW_LABEL
    fn = (lambda s: f"seo-{s}.html") if is_seo else (lambda s: f"diseno-web-{s}.html")
    cards = "\n".join(
        f'<div class="service"><div class="service__icon">{"📍" if is_seo else "🖥"}</div><h3><a href="{fn(s)}">{lab[s]}</a></h3>'
        f'<p>{CITIES[s]["pop"]}. {"SEO local, GBP y contenido por ciudad." if is_seo else "Webs rápidas con base SEO local, desde 300 €."}</p>'
        f'<div class="service__price">{CITIES[s]["name"]}</div></div>' for s in ORDER)
    faqs = [
        ("¿Cuál es la diferencia entre hacer SEO en Cádiz, Jerez o Chiclana?",
         "La intención y la competencia. En Cádiz capital y Jerez hay más volumen y más agencias; en San Fernando, Puerto Real, Chiclana y El Puerto hay menos volumen pero muchas menos webs trabajadas, y por eso se llega antes al top 3. La estrategia cambia por ciudad, el método es el mismo."),
        ("¿Cubres toda la bahía o solo la capital?",
         "Los seis municipios: Cádiz, Jerez de la Frontera, San Fernando, Chiclana de la Frontera, Puerto Real y El Puerto de Santa María. Cada uno tiene su propia página porque Google trata cada ciudad como una búsqueda distinta."),
        ("¿Cuánto cuesta el SEO local en la bahía?",
         "La auditoría es gratuita. El SEO mensual va desde 150 €/mes y el diseño web desde 300 €. El precio final depende del sector, de la competencia en tu ciudad y del punto de partida de tu web."),
    ] if is_seo else [
        ("¿Cuánto cuesta una web en la bahía de Cádiz?",
         "Desde 300 € una landing, desde 600 € una web de 5-6 páginas. Sin dominio ni hosting. Presupuesto cerrado antes de empezar."),
        ("¿Hacéis webs para negocios de cualquier municipio?",
         "Sí: Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María. Cada web lleva el nombre de la ciudad y las zonas donde trabaja el negocio, porque eso es lo que Google necesita para mostrarla en búsquedas locales."),
        ("¿La web incluye SEO?",
         "Incluye la base: velocidad, móvil, schema, canonicals, textos orientados a las búsquedas de tu ciudad y alta en Search Console. El SEO mensual (contenido, GBP, enlaces) es opcional y se contrata aparte."),
    ]
    body = f'''<section class="page-hero" style="padding-top: 120px;">
<div class="container">
  {breadcrumb(trail)}
  <div class="page-hero__tag">{tag}</div>
  <h1>{h1}</h1>
  <p class="page-hero__sub">{"Una agencia para los seis municipios de la bahía. SEO local pensado para cómo busca la gente en Cádiz, Jerez, San Fernando, Chiclana, Puerto Real y El Puerto de Santa María, no una plantilla de ciudad genérica." if is_seo else "Webs rápidas y preparadas para Google en los seis municipios de la bahía. Desde 300 €, sin dominio ni hosting, con la base SEO de tu ciudad incluida."}</p>
  <div class="hero__btns">
    <a href="contacto.html" class="btn btn--primary">{"Solicitar auditoría gratis →" if is_seo else "Pedir presupuesto →"}</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp</a>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Seis municipios, seis búsquedas distintas</p>
  <h2 class="section__title">Elige tu ciudad</h2>
  <div class="services__grid" style="margin-top:24px">{cards}</div>
</div>
</section>

<section class="section">
<div class="container">
  <p class="section__tag">{"Cómo trabajo el SEO local" if is_seo else "Qué incluye la web"}</p>
  <h2 class="section__title">{"Lo mismo que ya funciona en la bahía" if is_seo else "Una web no es un folleto: es la mitad de tu marketing"}</h2>
  <div class="two-col">
    <div>
      <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">{"El SEO local en la bahía se decide en el pack de Google Maps y en el móvil. Primero arreglamos la base: Google Business Profile, nombre de la ciudad en la web, velocidad y formulario. Después el contenido que responde a lo que la gente de cada municipio escribe en Google, y por último la autoridad local: citas, reseñas y menciones en medios de la zona." if is_seo else "Todas las webs que hago salen con la base SEO montada: textos por servicio y por ciudad, velocidad alta en móvil, schema, canonicals y sitemap. Publicar es el primer paso; el SEO mensual es lo que hace que la web te traiga llamadas cada mes."}</p>
      <p style="color:var(--gray);line-height:1.8">{"No vendo humo. Estas webs son propias, las gestiono y ya están en página 1 por búsquedas de la bahía. El mismo método, aplicado a tu negocio." if is_seo else "Si ya tienes web del Kit Digital, en la mayoría de los casos se aprovecha: se arregla lo que falla y se le añade el SEO que nunca tuvo."}</p>
    </div>
    <div>
      {"<h3 style='font-size:1.1rem;margin-bottom:12px'>Webs que ya posicionan</h3>" + fleet_block(["reformassanfernando.com", "controlplagaspuertosantamaria.es", "aireacondicionadojerez.es"]) if is_seo else '<div class="price-box"><div class="price-box__label">Página web desde</div><div class="price-box__amount">300 €</div><div class="price-box__note">Sin dominio ni hosting · Presupuesto cerrado</div></div>'}
    </div>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <p class="section__tag">Preguntas frecuentes</p>
  <h2 class="section__title">Dudas habituales</h2>
  {faq_block(faqs)}
</div>
</section>

<section class="cta">
<div class="container">
  <h2>{"¿Tu negocio no aparece en Google en tu municipio?" if is_seo else "¿Quieres una web que posicione en tu municipio?"}</h2>
  <p>{"Auditoría gratuita de tu web y tu Google Business Profile. Te enseño qué falla y qué resultados tienen otras webs de la bahía." if is_seo else "Presupuesto cerrado, sin dominio ni hosting, con la base SEO de tu ciudad incluida."}</p>
  <div class="cta__btns">
    <a href="contacto.html" class="btn btn--primary">{"Solicitar auditoría gratis →" if is_seo else "Pedir presupuesto →"}</a>
    <a href="{WA}" class="btn btn--outline" target="_blank">💬 WhatsApp directo</a>
  </div>
</div>
</section>'''
    return body, faqs, trail, title, desc, path

def write(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "seo"
    made = []
    if mode == "seo":
        for s in ORDER:
            body, faqs, trail = seo_body(s); k = kw_seo(s)
            write(f"seo-{s}.html", shell(k["title"], k["desc"], f"seo-{s}.html", body, faqs, trail)); made.append(f"seo-{s}.html")
    elif mode == "dw":
        for s in ORDER:
            body, faqs, trail = dw_body(s); k = kw_dw(s)
            write(f"diseno-web-{s}.html", shell(k["title"], k["desc"], f"diseno-web-{s}.html", body, faqs, trail)); made.append(f"diseno-web-{s}.html")
    elif mode == "hubs":
        for kind in ("seo", "dw"):
            body, faqs, trail, title, desc, path = hub_body(kind)
            write(path, shell(title, desc, path, body, faqs, trail)); made.append(path)
    print("generadas:", made)
