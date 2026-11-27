"""index.html — optimización E-E-A-T para la kw 'consultor seo cadiz'.
H1 exacto, bloque persona (vivo en Cádiz / sin permanencia / precios), FAQ visible + FAQPage schema,
Person schema enlazada al ProfessionalService. Idempotente: se puede relanzar."""
import re, json

P = 'index.html'
h = open(P, encoding='utf-8').read()
orig = h

# ---------- 1. H1 + hero ----------
H1_OLD = '<h1>Hago que tu negocio aparezca <em>primero en Google</em></h1>'
H1_NEW = '<h1>Consultor SEO en <em>Cádiz</em></h1>'
SUB_OLD = re.search(r'<p class="hero__sub">.*?</p>', h, re.S).group(0)
SUB_NEW = ('<p class="hero__sub">Soy Juan Casas, consultor SEO en Cádiz. Hago que negocios de servicios aparezcan primeros en Google '
           'cuando alguien en la provincia busca lo que ofrecen. No vendo humo: te enseño los resultados antes de pedirte nada.</p>')
h = h.replace(H1_OLD, H1_NEW).replace(SUB_OLD, SUB_NEW)

# foto hero: width/height + tagline local bajo la foto
h = h.replace('<img src="img/juan1.jpg" alt="Juan Casas — Consultor SEO en Cádiz" style="width:220px;',
              '<img src="img/juan1.jpg" alt="Juan Casas — Consultor SEO en Cádiz" width="220" height="220" style="width:220px;')
h = h.replace('<div class="hero__stats">',
              '<div style="font-size:.9rem;color:#cbd5e1;text-align:center">Vivo en Cádiz · Reunión presencial en la bahía · Trato directo</div>\n    <div class="hero__stats">', 1)

# ---------- 2. Sobre mí ----------
ABOUT_OLD = re.search(r'<div class="about__text">\s*<p>Llevo 8 años.*?</div>', h, re.S).group(0)
ABOUT_NEW = '''<div class="about__text">
    <p>Soy Juan Casas y llevo 8 años dedicándome al SEO. Empecé con webs de afiliación y ecommerce, y desde hace años me centro en el <strong>SEO local</strong>: que negocios de servicios aparezcan los primeros cuando alguien de Cádiz, Jerez, San Fernando, Chiclana, El Puerto o Puerto Real busca lo que ofrecen.</p>
    <p><strong>Vivo en Cádiz</strong> y trabajo con negocios de toda la provincia. Podemos vernos en persona en Cádiz, Jerez, San Fernando, Chiclana, El Puerto o Puerto Real, o por videollamada si lo prefieres. No soy una agencia con 50 empleados ni un comercial que te llama cada semana: <strong>hablas directamente conmigo</strong>, yo ejecuto y te explico todo lo que hago y por qué.</p>
    <p><strong>Sin permanencia.</strong> Trabajamos mes a mes: sigues conmigo por los resultados, no porque un contrato te obligue. Y sabes lo que cuesta desde el primer día: auditoría desde 150 €, SEO mensual desde 250 €/mes, web desde 300 €.</p>
    <p>Trabajo con reformas, climatización, cerrajeros, limpieza, electricistas, fontaneros, clínicas, despachos y cualquier profesional que necesite que le encuentren en Google. Si ese es tu caso, podemos hablar.</p>
  </div>'''
h = h.replace(ABOUT_OLD, ABOUT_NEW)

# ---------- 3. FAQ visible ----------
FAQ_ANCHOR = '<section class="cta">'
FAQ_HTML = '''<section class="section" id="preguntas-frecuentes">
<div class="container">
  <p class="section__tag">Preguntas frecuentes</p>
  <h2 class="section__title">Lo que me preguntan los negocios de Cádiz antes de empezar</h2>
  <div class="faq">
    <div class="faq__item"><h3>¿Qué hace un consultor SEO en Cádiz?</h3><p>Analizo tu web, tu Google Business Profile y tu competencia, decido qué búsquedas te traen clientes y trabajo la parte técnica, el contenido y la autoridad de tu marca para que aparezcas el primero cuando alguien de Cádiz busca lo que vendes. Te enseño cada mes con datos cómo evoluciona.</p></div>
    <div class="faq__item"><h3>¿Cuánto cuesta un consultor SEO en Cádiz?</h3><p>La auditoría inicial cuesta desde 150 € (pago único, con videollamada incluida). El SEO mensual sale desde 250 €/mes según el sector, la competencia y los objetivos. Si necesitas web, desde 300 €. Sabes el precio antes de empezar, sin letra pequeña.</p></div>
    <div class="faq__item"><h3>¿Cuánto tarda en notarse el posicionamiento SEO?</h3><p>Las primeras mejoras suelen verse entre el tercer y el sexto mes; en búsquedas locales poco competidas antes, y en sectores muy disputados hace falta más tiempo. Desde el primer mes te enseño con datos cómo evoluciona tu web.</p></div>
    <div class="faq__item"><h3>¿Hay permanencia?</h3><p>No. Trabajamos mes a mes, sin contratos de permanencia ni penalizaciones. Prefiero que sigas conmigo por los resultados, no porque un contrato te obligue.</p></div>
    <div class="faq__item"><h3>¿Trabajas solo con empresas de Cádiz?</h3><p>Me centro en negocios de servicios de la provincia de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, El Puerto de Santa María y Puerto Real. Vivir aquí me permite reunirme contigo en persona y conocer el mercado local, que no es lo mismo que posicionar en Madrid o Barcelona.</p></div>
    <div class="faq__item"><h3>¿Necesito una web nueva para posicionarme?</h3><p>No siempre. Muchas webs mejoran con ajustes técnicos y de contenido. Si tu web es muy lenta o no convierte visitas en clientes, te lo digo claramente y podemos hacerla nueva con el SEO pensado desde el principio, desde 300 €.</p></div>
    <div class="faq__item"><h3>¿Cómo empezamos?</h3><p>Con una auditoría: reviso tu web, tu ficha de Google y tu competencia y te entrego un informe con las acciones exactas a hacer. Desde ahí decides si quieres que lo ejecute yo o lo aplica tu equipo. <a href="contacto.html" style="color:#5eead4;font-weight:700">Pide tu auditoría gratis →</a></p></div>
  </div>
</div>
</section>

'''
assert FAQ_ANCHOR in h, 'ancla FAQ no encontrada'
h = re.sub(r'<section class="section" id="preguntas-frecuentes">.*?</section>\n\n', '', h, flags=re.S)
h = h.replace(FAQ_ANCHOR, FAQ_HTML + FAQ_ANCHOR, 1)

# ---------- 4. Schema ----------
FAQS = [
    ('¿Qué hace un consultor SEO en Cádiz?', 'Analizo tu web, tu Google Business Profile y tu competencia, decido qué búsquedas te traen clientes y trabajo la parte técnica, el contenido y la autoridad de tu marca para que aparezcas el primero cuando alguien de Cádiz busca lo que vendes. Te enseño cada mes con datos cómo evoluciona.'),
    ('¿Cuánto cuesta un consultor SEO en Cádiz?', 'La auditoría inicial cuesta desde 150 € (pago único, con videollamada incluida). El SEO mensual sale desde 250 €/mes según el sector, la competencia y los objetivos. Si necesitas web, desde 300 €. Sabes el precio antes de empezar, sin letra pequeña.'),
    ('¿Cuánto tarda en notarse el posicionamiento SEO?', 'Las primeras mejoras suelen verse entre el tercer y el sexto mes; en búsquedas locales poco competidas antes, y en sectores muy disputados hace falta más tiempo. Desde el primer mes te enseño con datos cómo evoluciona tu web.'),
    ('¿Hay permanencia?', 'No. Trabajamos mes a mes, sin contratos de permanencia ni penalizaciones. Prefiero que sigas conmigo por los resultados, no porque un contrato te obligue.'),
    ('¿Trabajas solo con empresas de Cádiz?', 'Me centro en negocios de servicios de la provincia de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, El Puerto de Santa María y Puerto Real. Vivir aquí me permite reunirme contigo en persona y conocer el mercado local, que no es lo mismo que posicionar en Madrid o Barcelona.'),
    ('¿Necesito una web nueva para posicionarme?', 'No siempre. Muchas webs mejoran con ajustes técnicos y de contenido. Si tu web es muy lenta o no convierte visitas en clientes, te lo digo claramente y podemos hacerla nueva con el SEO pensado desde el principio, desde 300 €.'),
    ('¿Cómo empezamos?', 'Con una auditoría: reviso tu web, tu ficha de Google y tu competencia y te entrego un informe con las acciones exactas a hacer. Desde ahí decides si quieres que lo ejecute yo o lo aplica tu equipo.'),
]
PERSON = {
    '@type': 'Person', '@id': 'https://casasdigital.es/#juan-casas',
    'name': 'Juan Casas', 'jobTitle': 'Consultor SEO',
    'description': 'Consultor SEO local y diseño web en Cádiz. 8 años de experiencia posicionando negocios de servicios en la provincia de Cádiz.',
    'url': 'https://casasdigital.es/#sobre-mi', 'image': 'https://casasdigital.es/img/juan1.jpg',
    'email': 'mailto:jj.casascecilia@gmail.com',
    'sameAs': ['https://www.linkedin.com/in/juanjesuscasas/'],
    'homeLocation': {'@type': 'City', 'name': 'Cádiz', 'sameAs': 'https://es.wikipedia.org/wiki/C%C3%A1diz'},
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Cádiz', 'addressRegion': 'Andalucía', 'addressCountry': 'ES'},
    'knowsAbout': ['SEO local', 'SEO técnico', 'Google Business Profile', 'Posicionamiento web', 'Diseño web', 'Contenido SEO', 'Linkbuilding', 'Schema markup'],
    'worksFor': {'@id': 'https://casasdigital.es/#organization'},
}
# ---------- 4. Schema (solo el 1er bloque JSON-LD: ProfessionalService) ----------
FAQS = [
    ('¿Qué hace un consultor SEO en Cádiz?', 'Analizo tu web, tu Google Business Profile y tu competencia, decido qué búsquedas te traen clientes y trabajo la parte técnica, el contenido y la autoridad de tu marca para que aparezcas el primero cuando alguien de Cádiz busca lo que vendes. Te enseño cada mes con datos cómo evoluciona.'),
    ('¿Cuánto cuesta un consultor SEO en Cádiz?', 'La auditoría inicial cuesta desde 150 € (pago único, con videollamada incluida). El SEO mensual sale desde 250 €/mes según el sector, la competencia y los objetivos. Si necesitas web, desde 300 €. Sabes el precio antes de empezar, sin letra pequeña.'),
    ('¿Cuánto tarda en notarse el posicionamiento SEO?', 'Las primeras mejoras suelen verse entre el tercer y el sexto mes; en búsquedas locales poco competidas antes, y en sectores muy disputados hace falta más tiempo. Desde el primer mes te enseño con datos cómo evoluciona tu web.'),
    ('¿Hay permanencia?', 'No. Trabajamos mes a mes, sin contratos de permanencia ni penalizaciones. Prefiero que sigas conmigo por los resultados, no porque un contrato te obligue.'),
    ('¿Trabajas solo con empresas de Cádiz?', 'Me centro en negocios de servicios de la provincia de Cádiz: Cádiz, Jerez, San Fernando, Chiclana, El Puerto de Santa María y Puerto Real. Vivir aquí me permite reunirme contigo en persona y conocer el mercado local, que no es lo mismo que posicionar en Madrid o Barcelona.'),
    ('¿Necesito una web nueva para posicionarme?', 'No siempre. Muchas webs mejoran con ajustes técnicos y de contenido. Si tu web es muy lenta o no convierte visitas en clientes, te lo digo claramente y podemos hacerla nueva con el SEO pensado desde el principio, desde 300 €.'),
    ('¿Cómo empezamos?', 'Con una auditoría: reviso tu web, tu ficha de Google y tu competencia y te entrego un informe con las acciones exactas a hacer. Desde ahí decides si quieres que lo ejecute yo o lo aplica tu equipo.'),
]
PERSON = {
    '@type': 'Person', '@id': 'https://casasdigital.es/#juan-casas',
    'name': 'Juan Casas', 'jobTitle': 'Consultor SEO',
    'description': 'Consultor SEO local y diseño web en Cádiz. 8 años de experiencia posicionando negocios de servicios en la provincia de Cádiz.',
    'url': 'https://casasdigital.es/#sobre-mi', 'image': 'https://casasdigital.es/img/juan1.jpg',
    'email': 'mailto:jj.casascecilia@gmail.com',
    'sameAs': ['https://www.linkedin.com/in/juanjesuscasas/'],
    'homeLocation': {'@type': 'City', 'name': 'Cádiz', 'sameAs': 'https://es.wikipedia.org/wiki/C%C3%A1diz'},
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Cádiz', 'addressRegion': 'Andalucía', 'addressCountry': 'ES'},
    'knowsAbout': ['SEO local', 'SEO técnico', 'Google Business Profile', 'Posicionamiento web', 'Diseño web', 'Contenido SEO', 'Linkbuilding', 'Schema markup'],
    'worksFor': {'@id': 'https://casasdigital.es/#organization'},
}
blocks = list(re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', h, re.S))
assert blocks and '"ProfessionalService"' in blocks[0].group(1), 'bloque ProfessionalService no encontrado'
org = json.loads(blocks[0].group(1))
org['@id'] = 'https://casasdigital.es/#organization'
org['founder'] = {'@id': 'https://casasdigital.es/#juan-casas'}
org['employee'] = {'@id': 'https://casasdigital.es/#juan-casas'}
graph = [org, PERSON, {
    '@type': 'FAQPage', '@id': 'https://casasdigital.es/#faq',
    'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQS],
}]
NEW_SCHEMA = '<script type="application/ld+json">' + json.dumps(graph, ensure_ascii=False, separators=(',', ':')) + '</script>'
b0 = blocks[0]
h = h[:b0.start()] + NEW_SCHEMA + h[b0.end():]

# ---------- 5. Meta description ----------
h = re.sub(r'<meta name="description" content="[^"]*"',
           '<meta name="description" content="Consultor SEO en Cádiz. SEO local para negocios de servicios de la provincia: auditoría desde 150 €, SEO mensual desde 250 €, sin permanencia. Soy Juan Casas, trabajas directamente conmigo. Pide tu auditoría gratis."', h, count=1)
# title: kw primero, nombre al final (la marca apenas tiene búsquedas propias)
h = re.sub(r'<title>[^<]*</title>', '<title>Consultor SEO en Cádiz — Juan Casas | Casas Digital</title>', h, count=1)

open(P, 'w', encoding='utf-8').write(h)
print('OK index.html — H1:', re.search(r'<h1>(.*?)</h1>', h, re.S).group(1), '| FAQ visibles:', h.count('faq__item'), '| schema Person:', '"@type":"Person"' in h, '| FAQPage:', '"FAQPage"' in h, '| palabras:', len(re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S)).split()))
