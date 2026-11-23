# 🔍 REGISTRO DE CAZA DE FALLOS — Bahía de Cádiz (23-nov-2026)

## ✅ FALLO GORDO (urgencia → rescate 500€)
**AC PUERTO (El Puerto)** — 991 URLs de casino en el sitemap,
vivas (200), riesgo de desindexación. PDF: AVISO-ACPUERTO.pdf.
ESTADO: llamadas hechas, "te llamamos" — seguimiento martes 11:00

## 🟡 FALLOS MEDIOS (pitch auditoría 150€)
**Pérez-Alberni (Cádiz)** — sin sitemap.xml + sin analytics
**Mateo López (Cádiz+SF)** — sin sitemap.xml (añadido al speech)
**Autoescuela Villar (SF)** — title "Inicio" vacío de SEO
**Suraña (SF)** — WP 5.1 (7 años sin actualizar) → argumento
de seguridad para el nurture de diciembre

## ❌ DESCARTADOS (verificados sin fallos)
Tamayo (robots bien currado) · El Bosque · Fuentes Méndez ·
Cleardent · Abogados AGA

## 📌 LECCIONES
1. Los "cialis/slot" de los primeros checks eran falsos positivos
   (especialistas, wpml-ls-slot-4) — SIEMPRE verificar contexto
   exacto antes de contactar
2. Los dominios escritos de memoria sin verificar dan 000 —
   solo auditar dominios confirmados en fuentes reales
3. El hacked content de casino es RARO en la Bahía (1 de ~20
   webs auditadas) — por eso el lead AC Puerto vale oro: el
   rescate no tiene competencia posible

# 🚨 CAZA AMPLIADA (23-nov ~19:30) — 2 NUEVOS LEADS DE RESCATE

## 1 · BUCALCLINIC (Cádiz/Sevilla) — HACKED CONFIRMADO (verificado a fondo 23-nov noche)
- bucalclinic.com — clínica dental con centros en Cádiz, Sevilla y Ceuta
- Dominio desde 2011 (IONOS) — negocio real con años de rodaje
- **SPAM FARMACÉUTICO OCULTO CONFIRMADO** (verificado con render):
  el texto "sildenafil precio" está en el DOM con font 36px,
  opacity 1... PERO dentro de un contenedor con
  `position:absolute; left:-15609px` = FUERA DE PANTALLA
  (técnica cloaking: invisible para humanos, visible para Google)
  Prueba para mostrarles: ver código fuente → Ctrl+F "sildenafil"
- SOLO la home está infectada (el resto de las 13 páginas limpias)
- ❌ CORRECCIONES (falsos positivos míos, verificados):
  · el "teléfono 999999999" NO EXISTE (eran valores CSS z-index
    y headers rate-limit — precipitación al interpretar regex)
  · el SSL está BIEN (https 200 válido + http redirige 301;
    mi "sin SSL" venía del sitemap interno con URLs http viejas)
  · "cialis" era falso positivo (espeCIALIStas) y "dose" del
    aviso legal también (incluyénDOSE, limitánDOSE — español!)
- ⚠️ menores: sin meta description · sitemap interno con URLs http
- VEREDICTO REAL: hacked content oculto grave ante Google, SOLO
  en la home, limpiable rápido. Pitch: cloaking farmacéutico +
  demo del código fuente delante de ellos

## 2 · ODONTO AVENIDA (Chiclana) — BOMBA DE RELÓJERÍA ⏳
- odontoavenida.com — clínica dental centro de Chiclana
- **WordPress 4.8 (de 2017 — 9 AÑOS sin actualizar)**
- 🚨 **REV SLIDER instalado** — el plugin con MÁS vulnerabilidades
  críticas de la historia de WP (el vector del hackeo masivo 2015-2018)
- Plugins heredados: timetable, sitepress multilingual
- Sitemap OK (200) pero la web es un blanco perfecto para lo mismo
  que le pasó a AC Puerto y Bucalclinic
- VEREDICTO: no está hackeada TODAVÍA — el pitch es preventivo:
  "su vecina de Cádiz acaba de ser hackeada con menos señales de
  riesgo que usted. Actualizar + blindar ANTES de que pase"

## PRIORIZACIÓN DE CONTACTO (todos los rescates):
1. BUCALCLINIC — urgencia máxima (teléfono falso YA les cuesta pacientes)
2. AC PUERTO — seguimiento de la llamada pendiente
3. ODONTO AVENIDA — preventivo con caso real de la zona

---
## 📅 LOG BUCALCLINIC (23-nov noche)
CONTACTADO por Juan. Pendiente respuesta.
PLAN DE SEGUIMIENTO:
- Si no contestan en 48h → 1 follow-up corto por el mismo canal:
  "¿Pudo ver lo del código fuente? La prueba se hace en 10
  segundos — le enseño dónde está el texto oculto cuando quiera,
  sin compromiso"
- SI PIDEN PRUEBA → mandar captura del código fuente con el
  "sildenafil precio" resaltado + la explicación de left:-15609px
  en lenguaje llano (el PDF de AC Puerto sirve de plantilla —
  hacer versión Bucalclinic de 1 página si piden presupuesto)
- OFERTA RECOMENDADA: limpieza 300-400€ (1 sola página infectada)
  + 95€/mes mantenimiento (vigilancia = lo que habría detectado
  esto hace meses)
LECCIÓN DEL PROCESO (para próximos pitches): siempre verificar
con render + contexto antes de afirmar fallos. El pitch de
Bucalclinic es sólido SOLO con el dato del cloaking (que es
real y demostrable con el código fuente).
