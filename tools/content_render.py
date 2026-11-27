# -*- coding: utf-8 -*-
"""Fase 3 · Renderizado de las secciones nuevas (HTML con las clases existentes del template)."""

def h3(t): return f'<h3 style="font-size:1.1rem;margin:28px 0 10px">{t}</h3>'
def p(t, last=False): return f'<p style="color:var(--gray);line-height:1.8;margin-bottom:{0 if last else 8}px">{t}</p>'

def section_light(tag, title, inner):
    return f'''<section class="section">
<div class="container">
  <p class="section__tag">{tag}</p>
  <h2 class="section__title">{title}</h2>
  {inner}
</div>
</section>'''

def section_dark(tag, title, inner):
    return f'''<section class="section section--dark">
<div class="container">
  <p class="section__tag">{tag}</p>
  <h2 class="section__title">{title}</h2>
  {inner}
</div>
</section>'''

def case_block(cs):
    return f'''<div class="two-col">
  <div>
    <p style="color:var(--gray);line-height:1.8;margin-bottom:16px"><strong style="color:#fff">{cs['domain']}</strong>. {cs['before']}</p>
    <p style="color:var(--gray);line-height:1.8;margin-bottom:16px">{cs['after']}</p>
    <p style="color:var(--gray);line-height:1.8">{cs['lesson']}</p>
  </div>
  <div>
    <div class="result"><div class="result__header"><span class="result__domain">{cs['domain']}</span><span class="result__badge result__badge--live">● Posicionando</span></div><div class="result__desc">Web propia que gestiono · <a href="{cs['url']}" target="_blank" rel="noopener">ver web</a></div></div>
    <p style="color:var(--gray);font-size:.95rem;line-height:1.7;margin-top:20px">Los números vienen de Search Console, no de herramientas de pago. En la auditoría te los enseño en pantalla.</p>
  </div>
</div>'''

def list_block(items):
    out = []
    for i, (t, b) in enumerate(items, 1):
        out.append(f'<div class="step"><div class="step__num">{i}</div><div class="step__body"><h3>{t}</h3><p>{b}</p></div></div>')
    return '<div class="steps">' + "".join(out) + '</div>'

def conclusion_block(txt):
    return f'<div class="article-tip" style="margin-top:28px"><p style="color:var(--gray);line-height:1.8;margin:0">{txt}</p></div>'

def table(headers, rows, cls="price-table"):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    trs = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'

def check_list(items):
    return '<ul class="check-list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def faq_items(faqs):
    return "\n".join(f'<div class="faq__item"><div class="faq__q">{q}</div><div class="faq__a">{a}</div></div>' for q, a in faqs)
