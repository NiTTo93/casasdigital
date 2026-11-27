# PLAN BATMAN — Casas Digital top 1 en SEO + Diseño Web en los 6 municipios de la Bahía de Cádiz

> Fecha: 27-nov-2026 · Repo: /root/casasdigital-repo · Estado: PLAN (sin ejecutar)
> Marcas: ✅ VERIFICADO (GSC/live 27-nov) · 🔍 DEDUCIDO · ❓ CONFIRMAR (Juan)

## 0. Diagnóstico — lo que dicen los datos (✅ GSC 90d, 25-ago → 24-nov)

| Métrica | Valor | Lectura |
|---|---|---|
| Impresiones 90d | 551 | 427 (77%) llevan nombre de municipio → la demanda YA existe |
| Clicks 90d | ~10 | Casi nada convierte porque no salimos en página 1 |
| "agencia seo cadiz" | pos 85.8 · 21 imp | Cae en consultoria-seo.html — esa página NO dice "agencia" |
| "agencia seo jerez" | pos 91.8 · 21 imp | Cae en seo-jerez.html (1.227 palabras, sin año, sin "agencia") |
| "seo cadiz" / "seo en cadiz" | pos 79 / 80 | Cae en consultoria-seo.html |
| "seo chiclana" | pos 48 · 23 imp | seo-chiclana.html (1.830 palabras) — la ciudad que mejor está |
| "consultor seo cadiz" | pos 25 (home) · 44-59 (consultoria) | La home es la página más fuerte (pos 1 marca, pos 8.5 clínicas) |
| "diseño web X" | pos 55-97 · ~15 imp | Solo existe diseno-web-seo.html genérica |
| San Fernando / Puerto Real | 0 páginas | No existimos para 2 de los 6 municipios |
| Brand "casas digital" | pos 8 · 1 imp | Marca débil — nadie busca Casas Digital todavía |

**Conclusión:** el site está indexado y Google lo PROBA en todas las ciudades, pero lo sitúa en pos 45-92 porque (a) las páginas de ciudad son finas (1.230 palabras vs 2.500-3.000 de las que sí posicionan), (b) no dicen "agencia", (c) no cubren "diseño web + ciudad", (d) faltan 2 municipios, (e) cero señal de entidad local (sin LocalBusiness schema, sin dateModified, FAQPage solo en 3 de 33 páginas).

## 1. Objetivo y secuencia realista

Top 1 en TODO no llega en 60 días — los competidores llevan 10+ años con dominios asentados. La secuencia que sí gana:

| Fase | Meses | Objetivo medible (GSC) |
|---|---|---|
| 1 Base técnica + 12 money pages | Sem 1-3 | Las 12 URLs indexadas; "seo san fernando" y "seo puerto real" en top 20 (competencia casi nula 🔍) |
| 2 Contenido local + enlaces internos | Sem 3-8 | Top 10 en Chiclana · El Puerto · San Fernando · Puerto Real para "seo X" y "diseño web X"; top 20 Cádiz/Jerez |
| 3 Autoridad local (citas, prensa, GBP) | Sem 6-12 | Top 3 en los 4 municipios pequeños; top 5 Cádiz y Jerez en "agencia seo X" |
| 4 Blindaje | Mes 4+ | Top 1-3 Cádiz/Jerez; brand "casas digital" pos 1 con sitelinks |

## 2. Arquitectura objetivo (12 money pages + 2 hubs)

| URL | Kw principal | Kw secundarias | Estado |
|---|---|---|---|
| index.html | Agencia SEO y diseño web Bahía de Cádiz | agencia seo cadiz · diseño web cadiz | Re-angle title ✏️ |
| seo-bahia-cadiz.html (hub) | SEO Bahía de Cádiz | marketing digital bahía · posicionamiento web cádiz | NUEVO |
| diseno-web-bahia-cadiz.html (hub) | Diseño web Bahía de Cádiz | crear página web cádiz · páginas web cádiz | NUEVO (o reconvertir diseno-web-seo.html) |
| seo-cadiz.html | Agencia SEO en Cádiz | consultor seo cadiz · posicionamiento web cadiz | Ampliar ✏️ |
| seo-jerez.html | Agencia SEO en Jerez | consultor seo jerez · posicionamiento web jerez | Ampliar ✏️ |
| seo-chiclana.html | Agencia SEO en Chiclana | marketing digital chiclana · consultoria seo chiclana | Ampliar ✏️ |
| seo-puerto-santa-maria.html | Agencia SEO en El Puerto de Santa María | seo el puerto · posicionamiento web el puerto | Ampliar ✏️ |
| seo-san-fernando.html | Agencia SEO en San Fernando | consultor seo san fernando | NUEVO |
| seo-puerto-real.html | Agencia SEO en Puerto Real | consultor seo puerto real | NUEVO |
| diseno-web-cadiz.html … ×6 | Diseño web en [ciudad] | crear página web · diseño páginas web · kit digital [ciudad] | 6 NUEVAS |
| consultoria-seo.html | Consultoría SEO (sin geo) | qué es · precio · cómo funciona | Re-angle (quitar "Cádiz" del title) |
| seo-local.html / google-business-profile.html / auditoria-seo.html | (servicios, sin geo) | — | Mantener; donantes de enlaces |

**Regla anti-canibalización:** cada municipio tiene UNA página de SEO y UNA de diseño web. Los servicios genéricos (consultoría, SEO local, auditoría, GBP) no llevan "Cádiz" en el title — la geo la llevan las páginas de ciudad. La home solo pelea "agencia seo cadiz" + "diseño web cadiz" a nivel bahía.

## 3. Fase 1 — Base técnica (1 sesión, antes de cualquier contenido)

1. **LocalBusiness/ProfessionalService JSON-LD** en TODAS las páginas (bloque compartido): nombre Casas Digital, Juan Casas, teléfono ❓, address Cádiz ❓, `areaServed` con los 6 municipios (City + sameAs Wikipedia), `priceRange`, `sameAs` (LinkedIn, GBP ❓), `hasOfferCatalog` con los 12 servicios.
2. **dateModified** en todas las páginas + `lastmod` real en sitemap (hoy: 0 dateModified, lastmod solo 2 fechas).
3. **FAQPage schema** en las 12 money pages + 6 servicios (hoy 3 de 33). Preguntas = queries literales de GSC ("cuánto cuesta el seo", "cuánto cobra un consultor seo", "contratar seo precio" → ya aparecen en GSC pos 21-77).
4. **Title/H1 de las 4 páginas de ciudad existentes** → formato `Agencia SEO en [Ciudad] — Posicionamiento Web 2027 | Casas Digital` (kw exacta delante + año, formato ya validado en notarías/auditoría).
5. **Breadcrumbs** Home › SEO Bahía de Cádiz › SEO en [ciudad] con BreadcrumbList schema.
6. Checklist structural sweep (skill receta-optimizacion-kw): canonicals, logo→`/`, CSS versionado, IndexNow.

## 4. Fase 2 — Las 12 money pages (plantilla única, 2.500-3.000 palabras)

Estructura obligatoria de cada página de ciudad:
- H1 exacto + lead con el municipio, la bahía y el año.
- **Prueba local verificable**: "Webs que ya posiciono en [municipio]" — enlaces OUTBOUND a las webs de la flota que ranquean en esa ciudad (Chiclana · Puerto Real · El Puerto · SF · Jerez). Salida solamente, sin recíprocos (regla anti-PBN). ✅ E-E-A-T real que ninguna agencia de la bahía puede copiar.
- **Qué pasa cuando buscas "[sector] en [ciudad]"**: 3-4 ejemplos de SERP local con captura de Juan ❓ (quién sale, por qué: GBP + reseñas + web lenta).
- **Kit Digital / web de 3.000€**: sección honesta "por qué tu web del Kit Digital no te trae clientes" — sin nombres de agencias (ver Riesgos).
- Tabla de precios "desde" ❓ (Juan fija: SEO local / diseño web / auditoría 150€ puerta ya en uso).
- Infografía generada "Cómo posicionamos tu web en [ciudad] en 5 pasos" (generador SVG→PNG de la skill, paleta dark #4f7df9) + `<ol>` espejo.
- 4-6 FAQs con schema (precio, plazo, cobertura, "¿trabajas con mi sector?", "¿ya tengo web del Kit Digital?").
- Bloque "También en [municipios vecinos]" — 3 enlaces hermanos con contexto geográfico.
- CTA: WhatsApp + formulario (ya conectado a Telegram 💻) + campo oculto `ciudad` para saber qué página convierte.

## 5. Fase 3 — Contenido de apoyo (24 posts en 8 semanas · 3/semana, tanda validada)

| Clúster | Posts | Enlace a money page |
|---|---|---|
| Por municipio (6 × 2) | "Cómo aparecer en Google Maps en [ciudad]" · "Cuánto cuesta una página web en [ciudad] 2027" | diseno-web-[ciudad] / seo-[ciudad] con ancla exacta |
| Batman / auditoría pública (4) | "9 fallos de seguridad que vemos en webs WordPress de la Bahía" · "Por qué tu web del Kit Digital no vende" · "Auditoría SEO gratis: qué miramos en 24h" · "SEO local vs SEO nacional: qué necesita tu negocio de Cádiz" | auditoria-seo + seo-bahia hub |
| Sectores × geo (4) | "SEO para clínicas dentales en Jerez" · "SEO para notarías en Cádiz" · "SEO para inmobiliarias en Chiclana/El Puerto" · "SEO para abogados en San Fernando/Puerto Real" | sector page + ciudad (ancla "SEO para notarías en Cádiz") |
| Confiancia/precio (4) | "Cuánto cobra un consultor SEO en Cádiz (precios reales 2027)" (ya existe, re-escribir con datos de la bahía) · "Consultor SEO vs agencia SEO: qué conviene en Cádiz" · "Cuánto tarda el SEO en dar resultados" · "Qué es el Kit Digital y quién lo puede pedir aún" ❓ verificar estado del programa | consultoria-seo + ciudad |
| Marca (2) | "Quién está detrás de Casas Digital" · "Casos: de 0 a top 3 en [municipio] en X semanas" (con GSC real) | home |

## 6. Interlinking (el que mueve posiciones — receta probada ×6)

- **Home** → 12 money pages en grid de 6 ciudades × 2 servicios (hoy solo 4 enlaces a ciudades). Anclas exactas: "Agencia SEO en San Fernando", "Diseño web en Jerez".
- **Hubs bahía** → sus 6 ciudades (ancla exacta) + posts del clúster.
- **Páginas de sector** (abogados, notarías, joyerías, clínicas, inmobiliarias, restaurantes) → 2-3 ciudades cada una con ancla sector+ciudad. Estas páginas son las que ya están en pos 1-9: son las donantes fuertes.
- **Ciudad ↔ ciudad**: vecinos (Cádiz↔San Fernando↔Puerto Real · Chiclana↔El Puerto · Jerez↔Puerto Real) en el bloque "También en".
- **Cada money page recibe mínimo 5 enlaces exactos** desde: home, hub, 2 sectores, 2 posts. Verificación con `grep -oE '<a href="seo-san-fernando.html"[^>]*>[^<]*</a>'` en toda la web.

## 7. Off-site — autoridad local (no volumen, RELEVANCIA local)

1. **GBP Casas Digital** ❓ (no aparece en dashboard): verificar que existe; categorías "Consultor de marketing en Internet" + "Diseñador de sitios web"; área de servicio = 6 municipios (SAB, dirección oculta si no atiende en oficina); servicios listados por ciudad; posts semanales con el post del clúster; Q&A sembrado ("¿Hacéis SEO en Jerez?").
2. **Citas NAP** (citador propio ✅): mismos datos en 40-60 directorios, priorizando los locales de la bahía (Cámaras de Comercio de Cádiz/Jerez, asociaciones de autónomos, directorios municipales).
3. **Estudio de datos "Estado del SEO de las webs de la Bahía de Cádiz 2027"**: auditar 100-150 webs de negocios locales con tooling propio (PageSpeed API · WordPress versión · schema · SSL · móvil). Estadística agregada, SIN nombres. Pitch a prensa local 🔍 (La Voz, Diario de Cádiz, Jerez Información) + colegios profesionales. Es el contenido que ninguna agencia puede replicar y el que más enlaces locales da.
4. **Colegios profesionales** (notarios, abogados, dentistas Cádiz): charla "visibilidad digital para despachos" → enlace desde el colegio + autoridad temática YMYL que ya estás atacando con las páginas de sector.
5. **Enlaces sectoriales ES** moderados (blogs de marketing, guest posts) con anclas variadas "agencia SEO Cádiz" / "Casas Digital" / brand desnudo. ❓ presupuesto.

## 8. "Robarles sus keywords de marca" — lectura honesta 🔍

- Las búsquedas de marca de agencias locales de Jerez/El Puerto/Cádiz son de volumen muy bajo (decenas/mes) y Google casi siempre pone su propia web + GBP arriba. Una página "Alternativas a [Agencia]" tiene riesgo legal (marca/difamación) y poco retorno. **Recomendación: no hacerla.**
- El robo real está en SUS CLIENTES: cada página "SEO para [sector] en [ciudad]" que sale top 1 se muestra al cliente de esa agencia cuando busca a su proveedor o su sector. El flujo de rescate (auditoría 150€, ya montado) es el canal. Más el contenido "tu web del Kit Digital no vende" capturando a los que ya pagaron los 3.000€.
- Opcional legal: páginas "[ciudad] marketing digital" / "agencias SEO en Cádiz: cómo elegir" que listan criterios objetivos sin nombrar (capturan quien compara agencias).

## 9. Medición

- Script GSC semanal (ya montado): por clúster de ciudad → impresiones · clicks · mejor posición de las 12 kw objetivo. Escalera de la sección 1.
- Juan valida SERPs desde su máquina (la del VPS no replica Google).
- Ahrefs ❓: export de volúmenes 6 ciudades × 8 kw (seo · agencia seo · consultor seo · diseño web · crear página web · marketing digital · posicionamiento web · kit digital) = 48 filas → priorizar las 4 primeras páginas.

## 10. Decisiones que necesito de Juan ❓

1. **"Agencia SEO"**: en memoria consta "NO atacar agencia seo cádiz" (posicionamiento como consultor). Pero es la kw con más impresiones de la bahía (83+ imp/90d en GSC). Propuesta: las páginas de ciudad dicen "Agencia SEO en X — Juan Casas, consultor" (cubre ambas intenciones). ¿OK?
2. **GBP**: ¿existe perfil de Google Business de Casas Digital? Si no, es prioridad 0 esta semana.
3. **Precios diseño web** para la tabla "desde" y la sección Kit Digital.
4. **Dirección/teléfono** para el LocalBusiness schema y las citas NAP.
5. **Capturas de SERP local** por municipio desde su móvil (con ubicación) para la sección "qué pasa cuando buscas X en Y".

## 11. Riesgos

- **Canibalización consultoria-seo ↔ seo-cadiz ↔ home**: se resuelve con la regla de la sección 2 (geo solo en páginas de ciudad) y re-angle de consultoria-seo.
- **Defamación**: nunca nombrar agencias competidoras en contenido negativo. Solo datos agregados.
- **Anti-PBN**: enlaces a la flota solo OUTBOUND desde casasdigital, nunca recíprocos.
- **Kit Digital**: verificar estado del programa antes de publicar contenido dependiente.
- **Expectativas**: top 1 Cádiz/Jerez es mes 4-6, no semana 3. Los 4 municipios pequeños son la victoria rápida que da casos para los grandes.

## 12. Archivos

- Modificar: index.html · seo-cadiz/jerez/chiclana/puerto-santa-maria.html · consultoria-seo.html · diseno-web-seo.html · 6 sector pages · sitemap.xml · style.css (cards ciudades)
- Crear: seo-bahia-cadiz.html · diseno-web-bahia-cadiz.html · seo-san-fernando.html · seo-puerto-real.html · diseno-web-{cadiz,jerez,chiclana,puerto-santa-maria,san-fernando,puerto-real}.html · blog/ (24) · img/infografia-[ciudad].png ×6
- Verificación tras cada tanda: 1 script (titles live · canonical · FAQ schema · enlaces exactos por página · ET.parse sitemap) + `python3 /root/indexnow.py casasdigital.es`
