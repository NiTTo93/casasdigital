"""Reconstruye el bloque 'Zonas de trabajo' de servicios/sectores/6 sectores:
lista plana (clase footer) -> grid de tarjetas .service (icono + H3 ancla exacta + contexto)."""
import re, glob

CITIES = [  # slug, nombre, emoji, (línea SEO, línea DW)
    ('cadiz', 'Cádiz', '📍', 'Capital y zona centro: la competencia más dura de la provincia.', 'Webs corporativas en la capital.'),
    ('jerez', 'Jerez', '🍷', 'El municipio más poblado: volumen de búsqueda y competencia altísima.', 'Webs para negocios jerezanos.'),
    ('san-fernando', 'San Fernando', '🌊', 'Búsqueda local muy cerrada: el mapa decide casi todo.', 'Webs para la Isla.'),
    ('chiclana', 'Chiclana', '🏖', 'Turismo y residentes: dos públicos con búsquedas distintas.', 'Webs en Chiclana y la costa.'),
    ('puerto-real', 'Puerto Real', '⛵', 'Poco competencia orgánica: se posiciona rápido con contenido.', 'Webs en Puerto Real y la Bahía.'),
    ('puerto-santa-maria', 'El Puerto de Santa María', '🚢', 'Puerto y playas: estacionalidad que conviene captar todo el año.', 'Webs en El Puerto.'),
]
HUB_SEO = ('bahia-cadiz', 'Toda la Bahía de Cádiz', '🗺', 'Visión conjunta de los seis municipios y cómo ataco cada zona.')

# Orden de los enlaces tal y como aparecen hoy (para reemplazar el bloque exacto)
SEO_SEQ = ['bahia-cadiz', 'cadiz', 'jerez', 'san-fernando', 'chiclana', 'puerto-real', 'puerto-santa-maria']
DW_SEQ = ['bahia-cadiz', 'cadiz', 'jerez', 'san-fernando', 'chiclana', 'puerto-real', 'puerto-santa-maria']

LABEL_SEO = {'bahia-cadiz': 'Agencia SEO en la Bahía de Cádiz', 'cadiz': 'Agencia SEO en Cádiz', 'jerez': 'Agencia SEO en Jerez',
             'san-fernando': 'Agencia SEO en San Fernando', 'chiclana': 'Agencia SEO en Chiclana', 'puerto-real': 'Agencia SEO en Puerto Real',
             'puerto-santa-maria': 'Agencia SEO en El Puerto de Santa María'}
LABEL_DW = {'bahia-cadiz': 'Diseño web en la Bahía de Cádiz', 'cadiz': 'Diseño web Cádiz', 'jerez': 'Diseño web Jerez',
            'san-fernando': 'Diseño web San Fernando', 'chiclana': 'Diseño web Chiclana', 'puerto-real': 'Diseño web Puerto Real',
            'puerto-santa-maria': 'Diseño web El Puerto de Santa María'}


def card(kind, slug, sub):
    name = LABEL_SEO[slug] if kind == 'seo' else LABEL_DW[slug]
    href = f'{kind}-{slug}.html'
    emoji = next((c[2] for c in CITIES if c[0] == slug), HUB_SEO[2])
    return (f'    <div class="service"><div class="service__icon">{emoji}</div>'
            f'<h3><a href="{href}">{name}</a></h3><p>{sub}</p></div>\n')


def seo_grid(with_hub=True, extra=''):
    out = '  <div class="services__grid">\n'
    for slug, name, emoji, seo_line, _ in CITIES:
        out += card('seo', slug, seo_line)
    if with_hub:
        out += card('seo', 'bahia-cadiz', HUB_SEO[3])
    out += '  </div>\n'
    return out + extra


def dw_grid():
    out = '  <div class="services__grid">\n'
    for slug, name, emoji, _, dw_line in CITIES:
        out += card('diseno-web', slug, dw_line)
    out += card('diseno-web', 'bahia-cadiz', 'Hub con los seis municipios y la comparativa Kit Digital.')
    out += '  </div>\n'
    return out


def link_list(prefix, seq, labels):
    items = ''.join(f'    <a href="{prefix}-{s}.html">{labels[s]}</a>\n' for s in seq)
    return f'  <div class="footer__zones-links" style="margin-bottom:12px">\n{items}  </div>\n'


def fix(p, has_dw):
    h = open(p, encoding='utf-8').read()
    body_end = h.find('<footer')
    pat = re.compile(r'  <div class="footer__zones-links" style="margin-bottom:12px">.*?</div>\n', re.S)
    replaced = []
    def sub(m):
        block = m.group(0)
        if replaced and not has_dw or len(replaced) >= 2:
            return block
        first = re.search(r'href="([^"]+)"', block).group(1)
        if first.startswith('seo-'):
            replaced.append('seo'); return seo_grid(with_hub=True)
        if first.startswith('diseno-web-'):
            replaced.append('dw'); return dw_grid()
        return block
    h2 = pat.sub(sub, h, count=0)
    assert 'seo' in replaced, (p, replaced)
    if has_dw: assert 'dw' in replaced, (p, replaced)
    assert h2.count('footer__zones-links" style="margin-bottom') == 0, p
    open(p, 'w', encoding='utf-8').write(h2)
    print(f"{p}: grid tarjetas {'SEO+DW' if has_dw else 'SEO'}")


for p in ['servicios.html', 'sectores.html']:
    fix(p, True)
for s in ['abogados', 'joyerias', 'notarias', 'inmobiliarias', 'clinicas-dentales', 'restaurantes']:
    fix(f'seo-{s}.html', False)
