# -*- coding: utf-8 -*-
"""Fase 3 · Diseño web pages · lo que veo al auditar webs de cada ciudad."""

DW_AUDIT = {
    "cadiz": dict(
        intro="Audito webs de negocios de Cádiz capital casi cada semana. Esto es lo que encuentro, una y otra vez:",
        items=[
            "Webs de agencias de fuera que usan la misma plantilla para Cádiz que para Huelva, con el nombre de la ciudad cambiado.",
            "Formularios que «envían» pero no avisan: el cliente rellena, le sale el mensaje de gracias, y el negocio se enterne una semana después.",
            "Casco histórico: webs de comercio y hostelería sin fotos propias, sin horarios actualizados y sin una sola página por servicio.",
            "Empresas de Zona Franca y polígonos industriales con sliders que no cargan en móvil o con vídeos de portada de 20 MB.",
            "Sitios con HTTPS a medias (aviso en el navegador) y versiones http y https duplicadas en Google.",
        ],
        conclusion="Casi todas estas webs se pueden arreglar sin rehacerlas. Lo que no se puede arreglar es el tiempo perdido mientras no posicionan.",
    ),
    "jerez": dict(
        intro="En Jerez el patrón se repite: webs bonitas que no venden. Esto es lo que encuentro al auditarlas:",
        items=[
            "Webs de plantilla con un slider en portada que tarda 6 segundos en cargar en 4G; el usuario se va antes de ver el título.",
            "Textos escritos para el dueño, no para el cliente: «30 años de experiencia», «calidad garantizada», sin una sola búsqueda real cubierta.",
            "Webs bilingües mal montadas: la versión inglesa indexada como principal y la española como duplicada.",
            "Restaurantes y bodegas con la carta en PDF que Google no lee, y sin página de reservas que funcione en móvil.",
            "Negocios con el dominio registrado a nombre de la agencia anterior, no del dueño. Cuando cambian de proveedor, pierden el dominio.",
        ],
        conclusion="En Jerez la buena noticia es que casi nadie está haciendo las cosas bien. Arreglar cuatro cosas básicas ya te pone por delante del 80 % de tu competencia.",
    ),
    "san-fernando": dict(
        intro="San Fernando es el municipio donde veo más webs de Kit Digital abandonadas. Esto es lo que encuentro al auditarlas:",
        items=[
            "Webs del Kit Digital entregadas hace 2-3 años y sin tocar desde entonces: plugins desactualizados, formulario roto y cero SEO.",
            "Negocios de la Calle Real y Bahía Sur con GBP sin trabajar: la ficha existe pero no tiene categorías correctas, fotos ni servicios.",
            "Clínicas y despachos con webs «de corporación» que no dicen en qué calle están ni a qué municipio sirven.",
            "Webs sin una sola página por servicio: todo en la home, así Google no puede posicionar nada por separado.",
            "Teléfonos y horarios que no coinciden entre la web, Maps y las redes sociales. Google penaliza la inconsistencia en SEO local.",
        ],
        conclusion="En San Fernando el Kit Digital fue un buen punto de partida, pero casi nadie ha hecho trabajar esa web después. Ahí está la oportunidad.",
    ),
    "chiclana": dict(
        intro="Chiclana tiene la particularidad de tener dos mercados (ciudad y costa), y las webs de la zona suelen olvidar el segundo. Esto es lo que encuentro:",
        items=[
            "Webs de negocios de La Barrosa y Sancti Petri que no mencionan la zona en ninguna página: pierden todas las búsquedas de playa.",
            "Restaurantes y chiringuitos con la carta en PDF y sin página de reservas que funcione en móvil.",
            "Webs del Kit Digital con plantilla compartida con otros 200 negocios de Andalucía, sin una línea de texto propio.",
            "Inmobiliarias con buscador de propiedades que Google no puede leer (filtros en JavaScript sin renderizado).",
            "Negocios con dos fichas de Google Maps duplicadas (una la creó la agencia anterior) y ninguna trabajada.",
        ],
        conclusion="En Chiclana, el que trabaja las dos zonas (ciudad y costa) se lleva un mercado que los demás están dejando libre.",
    ),
    "puerto-real": dict(
        intro="Puerto Real es un mercado pequeño con webs muy parecidas entre sí. Esto es lo que encuentro:",
        items=[
            "Negocios sin web propia: solo ficha de Maps y Facebook. Para Google no existen fuera del pack local.",
            "Webs de agencias locales hechas entre 2015 y 2018, sin adaptar a móvil y con textos que no han cambiado desde entonces.",
            "Negocios del Casco Antiguo y de Rio San Pedro sin una página que diga dónde están y a qué zona sirven.",
            "Servicios orientados a la universidad y al PEN sin contenido para esa audiencia concreta.",
            "Webs con el dominio registrado a nombre del técnico que la hizo, no del dueño del negocio.",
        ],
        conclusion="En Puerto Real una web hecha hoy, con SEO desde el principio, te pone por delante del 90 % de tu competencia en cuestión de semanas.",
    ),
    "puerto-santa-maria": dict(
        intro="En El Puerto conviven los negocios de todo el año y los de temporada, y las webs reflejan esa confusión. Esto es lo que encuentro:",
        items=[
            "Webs «de temporada» que solo hablan del verano y no dicen nada del resto del año: pierden 9 meses de búsquedas de proximidad.",
            "Restaurantes y bodegas con la carta en PDF, sin reservas online y sin fotos propias.",
            "Webs del Kit Digital con plantilla compartida con otros 200 negocios de Andalucía.",
            "Negocios de Valdelagrana y El Trocadero con GBP sin trabajar, o con fichas de temporada que nadie actualiza.",
            "Webs con la versión móvil rota: botones que no funcionan y texto que se sale del borde.",
        ],
        conclusion="En El Puerto la diferencia la marca quien piensa en todo el año y en todas las zonas. La web tiene que vender también en noviembre.",
    ),
}
