# -*- coding: utf-8 -*-
"""Fase 3 · Diseño web pages · estructura según sector, errores móviles y FAQ extra."""

DW_STRUCT_INTRO = "No todos los negocios necesitan lo mismo. Esto es lo que recomiendo según lo que vendes en {short}, y por qué:"
DW_STRUCT = [
    ("Negocio de servicios (reformas, plagas, climatización, electricidad)", "6-8 páginas", "Home + una página por servicio + zonas de {short} + contactos. Cada página de servicio se posiciona por separado («reformas de baños {short}», «instalación de aire acondicionado {short}»). Es la estructura que más consultas genera en la bahía."),
    ("Clínica dental, fisioterapia, estética", "6-10 páginas", "Home + una página por tratamiento con precio orientativo y fotos + equipo + reservas. Las búsquedas son por tratamiento («implante dental {short} precio»), no por clínica."),
    ("Despacho profesional (abogado, notaría, gestoría)", "6-8 páginas", "Home + una página por materia + quién soy + blog de preguntas legales. Aquí la confianza lo es todo: biografía, colegiación y casos sin datos personales."),
    ("Restaurante, bar, chiringuito", "4-5 páginas", "Home con carta en HTML (no PDF), reservas, eventos y cómo llegar. El 90 % del tráfico viene de Maps; la web tiene que confirmar lo que Maps promete."),
    ("Comercio con tienda física", "4-6 páginas", "Home + categorías + marcas + horarios y ubicación. Si vendes online, catálogo con fichas que Google pueda leer."),
    ("Inmobiliaria", "8-12 páginas", "Home + páginas por zona de {short} y por tipo de operación + buscador legible por Google + fichas de inmuebles."),
    ("Landing de un solo servicio", "1 página", "Solo si vendes un único servicio o quieres probar un mercado. Desde 300 €. Conviene ampliarla a las 8 semanas si funciona."),
]

DW_MOBILE_TITLE = "Los errores de móvil que están costándote clientes en {short}"
DW_MOBILE_INTRO = "Más del 80 % de las búsquedas de servicio en la bahía se hacen desde el móvil. Estos son los fallos que veo una y otra vez, y que arreglo en cada web:"
DW_MOBILE = [
    ("La web tarda más de 3 segundos en cargar", "En 4G la mayoría de webs de agencias de la zona tardan 6-10 segundos. El usuario vuelve a Google antes de ver tu nombre. Lo arreglo con HTML ligero, imágenes en WebP y sin sliders de portada."),
    ("Botones demasiado pequeños o pegados", "Un botón de «llamar» de 28 píxeles en un móvil con la mano es un botón que no se pulsa. Todos los botones que diseño tienen al menos 48 píxeles y separación suficiente."),
    ("Textos que se salen del borde", "Párrafos y tablas sin adaptar: el usuario tiene que hacer zoom y moverse de lado a lado. Lo verifico en 3 tamaños de pantalla antes de publicar."),
    ("Formularios con 10 campos", "Cada campo extra pierde un 10 % de las consultas. Pido lo mínimo: nombre, teléfono y qué necesitas. El resto, en la primera llamada."),
    ("Sin botón de llamada ni de WhatsApp visible", "En {short} la gente llama o escribe por WhatsApp; no rellena formularios largos. El botón de contacto tiene que estar siempre a un pulgar de distancia."),
    ("Menús que no se abren", "Hamburguesas que no responden, enlaces de navegación que no se ven. En móvil la navegación tiene que ser de un toque, y lo pruebo en iOS y Android."),
]

DW_FAQ_EXTRA = [
    ("¿Puedo ver ejemplos de webs que hayas hecho en la bahía?", "Sí. En la sección de resultados de esta web tienes webs propias que gestiono y que hoy posicionan en sus ciudades. También puedo enseñarte en la auditoría webs de clientes que no son públicas por acuerdo con el negocio."),
    ("¿Qué me necesitas de mi parte para empezar?", "Lo básico: qué vendes, a quién, en qué zonas de {short}, tus precios orientativos y fotos si tienes. El resto lo escribo yo y tú lo revisas."),
    ("¿La web estará en varios idiomas?", "Si te interesa, sí (inglés es lo habitual en la bahía por turismo y residentes extranjeros). Lo hago con URLs separadas por idioma y etiquetas hreflang correctas, no con traductores automáticos dentro de la página."),
    ("¿Puedo añadir un blog después?", "Sí. Recomiendo añadirlo cuando tengas claro que vas a publicar con regularidad: un blog con 3 posts de 2022 da peor imagen que no tener blog. Te lo preparo para que publicar sea escribir y darle a un botón."),
]
