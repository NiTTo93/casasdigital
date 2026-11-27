"""servicios.html: sección 'Automatización y captación de clientes' —
3 tarjetas .card sin CSS, cada una en su propio .two-col -> un grid .services__grid con 3 tarjetas .service."""
import re

p = 'servicios.html'
h = open(p, encoding='utf-8').read()

NEW = '''<section class="section" style="padding-top:0">
<div class="container">
  <p class="section__tag">Más allá del SEO</p>
  <h2 class="section__title" style="margin-bottom:36px">Automatización y captación de clientes</h2>
  <p style="color:var(--gray);max-width:760px;line-height:1.8;margin:-16px 0 32px">Cuando la web ya trae visitas, el siguiente paso es que nada se quede sin respuesta. Estos tres servicios se integran con el SEO o funcionan por separado.</p>
  <div class="services__grid">
    <div class="service">
      <div class="service__icon">⚙️</div>
      <h3>Automatizaciones</h3>
      <p>Formularios que saltan en tu móvil, informes automáticos y tareas que se hacen solas.</p>
      <div class="service__price">Desde 150€</div>
      <a href="automatizaciones-empresas.html" class="btn btn--outline" style="margin-top:20px;padding:10px 20px;font-size:.875rem">Ver más →</a>
    </div>
    <div class="service">
      <div class="service__icon">🤖</div>
      <h3>Agente IA 24/7</h3>
      <p>Un asistente de IA que atiende el teléfono y WhatsApp de tu negocio siempre, incluso fuera de horario.</p>
      <div class="service__price">Montado desde 450€</div>
      <a href="agente-ia-telefono.html" class="btn btn--outline" style="margin-top:20px;padding:10px 20px;font-size:.875rem">Ver más →</a>
    </div>
    <div class="service">
      <div class="service__icon">🎯</div>
      <h3>Captación de leads</h3>
      <p>Landing de conversión + aviso instantáneo al móvil + campañas locales. Leads exclusivos, sin permanencia.</p>
      <div class="service__price">Según volumen</div>
      <a href="captacion-leads.html" class="btn btn--outline" style="margin-top:20px;padding:10px 20px;font-size:.875rem">Ver más →</a>
    </div>
  </div>
</div>
</section>
'''

# Localizar: <div class="container">…Más allá del SEO…</div> + los 3 <div class="two-col">…</div> que siguen
start = h.index('<div class="container"><p class="section__tag">Más allá del SEO')
end_marker = '<a href="captacion-leads.html" class="btn btn--primary">Ver servicio →</a>\n</div></div>\n'
end = h.index(end_marker, start) + len(end_marker)
assert h[start:end].count('class="card"') == 3, h[start:end].count('class="card"')
h = h[:start] + NEW + h[end:]
open(p, 'w', encoding='utf-8').write(h)
print('sección reconstruida · .card restantes:', h.count('class="card"'), '· two-col en servicios:', h.count('class="two-col"'))
