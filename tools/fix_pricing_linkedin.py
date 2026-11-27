"""Precio web unificado (300 € landing · 600 € web 5-6 págs) en home, servicios y diseno-web-seo;
LinkedIn real (juanjesuscasas) en todo el sitio. Idempotente."""
import re, glob

LINKEDIN_OLD = 'https://www.linkedin.com/in/juanjesuscasas/'
LINKEDIN_NEW = 'https://www.linkedin.com/in/juanjesuscasas/'
SCALE = 'Landing 300 € · Web de 5-6 páginas 600 €'

def sub_once(h, old, new, label):
    if old in h:
        return h.replace(old, new, 1)
    if new in h:
        return h  # ya aplicado
    raise SystemExit(f'✗ no encontrado: {label}')

# ---------- index.html ----------
p = 'index.html'; h = open(p, encoding='utf-8').read()
h = sub_once(h,
    '<p>Creo tu web profesional optimizada para SEO desde el primer día. Rápida, responsive, con schema markup y estructura pensada para posicionar en tu zona.</p>\n      <div class="service__price">Desde 600€ · Proyecto</div>',
    f'<p>Creo tu web profesional optimizada para SEO desde el primer día. Rápida, responsive, con schema markup y estructura pensada para posicionar en tu zona.</p>\n      <div class="service__price">Desde 300€</div>\n      <p style="font-size:.85rem;color:var(--gray);margin-top:-10px">{SCALE} · Sin dominio ni hosting</p>',
    'index tarjeta web')
# la FAQ de la home ya dice "desde 300 €": ok. Sobre mí ya dice "web desde 300 €": ok.
open(p, 'w', encoding='utf-8').write(h); print('✓ index.html')

# ---------- servicios.html ----------
p = 'servicios.html'; h = open(p, encoding='utf-8').read()
h = sub_once(h,
    '<div class="service__price">Desde 600€ · Proyecto</div>\n      <a href="diseno-web-seo.html"',
    f'<div class="service__price">Desde 300€</div>\n      <p style="font-size:.85rem;color:var(--gray);margin-top:-10px;margin-bottom:4px">{SCALE} · Sin dominio ni hosting</p>\n      <a href="diseno-web-seo.html"',
    'servicios tarjeta web')
open(p, 'w', encoding='utf-8').write(h); print('✓ servicios.html')

# ---------- diseno-web-seo.html ----------
p = 'diseno-web-seo.html'; h = open(p, encoding='utf-8').read()
h = sub_once(h, 'estructura pensada para posicionar en Google desde el primer día. Desde 600€."',
                'estructura pensada para posicionar en Google desde el primer día. Landing desde 300 €, web de 5-6 páginas desde 600 €."', 'dw-seo meta desc')
h = sub_once(h, 'El punto de partida para una web de negocio local es 600€.',
                'El punto de partida es una landing de una página por 300 €; una web de negocio local de 5-6 páginas, 600 €.', 'dw-seo párrafo precio')
OLD_BOX = re.search(r'<div class="price-box">\s*<div class="price-box__label">Web profesional con SEO integrado</div>\s*<div class="price-box__amount">Desde 600€</div>\s*<div class="price-box__note">.*?</div>\s*</div>', h, re.S)
assert OLD_BOX, 'price-box no encontrado en diseno-web-seo'
NEW_BOX = f'''<div class="price-box">
          <div class="price-box__label">Landing de 1 página · con SEO local</div>
          <div class="price-box__amount">300 €</div>
          <div class="price-box__note">Un servicio principal o una campaña · Sin dominio ni hosting · IVA no incluido</div>
        </div>
        <div class="price-box" style="margin-top:16px">
          <div class="price-box__label">Web de 5-6 páginas · con SEO integrado</div>
          <div class="price-box__amount">600 €</div>
          <div class="price-box__note">Negocio local con varios servicios · Presupuesto cerrado antes de empezar</div>
        </div>
        <p style="font-size:.9rem;color:var(--gray);margin-top:14px">¿Quieres que la web siga trabajando sola? <a href="contacto.html" style="color:#5eead4;font-weight:700">Web + SEO mensual</a>: 600 € + 150 €/mes.</p>'''
h = h[:OLD_BOX.start()] + NEW_BOX + h[OLD_BOX.end():]
open(p, 'w', encoding='utf-8').write(h); print('✓ diseno-web-seo.html')

# ---------- LinkedIn en todo el sitio + scripts ----------
files = sorted(glob.glob('*.html') + glob.glob('blog/*.html') + glob.glob('tools/*.py'))
n = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    if LINKEDIN_OLD in s:
        open(f, 'w', encoding='utf-8').write(s.replace(LINKEDIN_OLD, LINKEDIN_NEW)); n += 1
print(f'✓ LinkedIn actualizado en {n} archivos')
