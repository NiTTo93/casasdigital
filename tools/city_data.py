# -*- coding: utf-8 -*-
"""Datos locales de los 6 municipios de la Bahía de Cádiz — casasdigital.es"""

SITE = "https://casasdigital.es/"
WA = "https://wa.me/34610304263"
TODAY = "2026-11-27"
YEAR = "2027"

# Páginas de la flota que YA posicionan (enlaces OUT, nunca recíprocos — regla anti-PBN)
FLEET = {
    "reformassanfernando.com": ("Reformas en San Fernando", "https://reformassanfernando.com", "Página 1-2 en «reformas San Fernando»"),
    "reformaschiclana.es": ("Reformas en Chiclana", "https://reformaschiclana.es", "Top local en Chiclana y La Barrosa"),
    "controlplagaspuertosantamaria.es": ("Control de plagas en El Puerto", "https://controlplagaspuertosantamaria.es", "Top local en El Puerto de Santa María"),
    "controldeplagaspuertoreal.es": ("Control de plagas en Puerto Real", "https://controldeplagaspuertoreal.es", "Top local en Puerto Real"),
    "reformaspuertoreal.es": ("Reformas en Puerto Real", "https://reformaspuertoreal.es", "Top local en Puerto Real"),
    "reformaselpuerto.es": ("Reformas en El Puerto de Santa María", "https://reformaselpuerto.es", "Top local en El Puerto"),
    "controldeplagaschiclana.es": ("Control de plagas en Chiclana", "https://controldeplagaschiclana.es", "Top local en Chiclana"),
    "aireacondicionadojerez.es": ("Aire acondicionado en Jerez", "https://aireacondicionadojerez.es", "24+ consultas en top 24, en indexación"),
    "servielectricjerez.es": ("Electricistas en Jerez", "https://servielectricjerez.es", "Top local en Jerez"),
    "multiservicioschiclana24h.es": ("Multiservicios 24h en Chiclana", "https://multiservicioschiclana24h.es", "Top local en Chiclana"),
    "fumigacionsanfernando.es": ("Fumigación en San Fernando", "https://fumigacionsanfernando.es", "Top local en San Fernando"),
}

CITIES = {
    "cadiz": dict(
        name="Cádiz", short="Cádiz", pop="58.000 en el casco urbano, más de un millón en la bahía",
        fleet_keys=["reformassanfernando.com", "reformaschiclana.es", "controlplagaspuertosantamaria.es"],
        neighbors=["jerez", "san-fernando", "puerto-real"],
        sectors=["Comercio del casco histórico y Mercado Central", "Hostelería y turismo (La Caleta, Semana Santa, Carnaval)",
                 "Despachos profesionales: abogados, notarías, gestorías", "Clínicas dentales y estéticas",
                 "Inmobiliarias y administración de fincas", "Academias, autoescuelas y formación"],
        angles=[
            ("El casco histórico y el pack local de Maps",
             "En Cádiz capital la búsqueda «cercano a mí» la decide el pack local de Google Maps, no la web. Un negocio de la calle Comercio, de la Plaza de las Flores o de Zona Franca necesita primero un Google Business Profile trabajado (categorías correctas, reseñas respondidas, fotos semanales, publicaciones) y después una web que diga exactamente lo mismo. Si el GBP y la web discrepan en nombre, dirección u horarios, Google pierde confianza en ambos."),
            ("Turismo con doble intención",
             "Un restaurante o un alojamiento de Cádiz recibe búsquedas de residentes («desayuno cerca de mí») y de visitantes («dónde comer en Cádiz centro»). Son dos SEO distintos: el primero es puro pack local, el segundo es contenido y autoridad. Hay que decidir cuál paga las facturas en temporada baja y construir la web para esa intención, no para las dos a la vez."),
            ("Las webs del Kit Digital en Cádiz",
             "Muchas empresas gaditanas pagaron su web con el bono Kit Digital y hoy tienen una web «entregada»: WordPress desactualizado, plugins sin tocar desde 2023, formularios que no avisan al móvil y cero trabajo SEO. No hace falta tirarla: hace falta auditarla, actualizarla y ponerla a trabajar. Es el cliente ideal para una auditoría honesta."),
        ],
    ),
    "jerez": dict(
        name="Jerez de la Frontera", short="Jerez", pop="213.000 habitantes, la ciudad más grande de la bahía",
        fleet_keys=["aireacondicionadojerez.es", "servielectricjerez.es", "reformassanfernando.com"],
        neighbors=["cadiz", "puerto-real", "puerto-santa-maria"],
        sectors=["Bodegas y enoturismo", "Escuelas de equitación y turismo ecuestre", "Autoescuelas, academias y formación",
                 "Clínicas dentales, veterinarios y estética", "Despachos de abogados y gestorías", "Comercio del centro y hostelería"],
        angles=[
            ("El mercado más competido de la bahía, y el más descuidado",
             "En Jerez hay más agencias y más inversión en publicidad que en el resto de la bahía junta. Pero casi ninguna de esas agencias posiciona su propia web por sus keywords de servicio en Jerez: se venden pornetwork y por Kit Digital, venden anuncios y redes, no posicionamiento orgánico. Ese hueco entre lo que se vende y lo que se entrega es exactamente donde trabaja una agencia SEO que enseña sus resultados antes de pedir nada."),
            ("Bodegas y enoturismo: un sector con búsqueda internacional",
             "Jerez tiene un activo que ninguna otra ciudad de la bahía tiene: un sector con demanda global. Una bodega con web en castellano e inglés, schema de eventos para visitas y espectáculos, fotos propias y reseñas de visitantes es capaz de salir en «jerez wine tour» o «visita bodega Jerez», búsquedas que ningún competidor local está trabajando bien."),
            ("Webs del Kit Digital en Jerez",
             "Igual que en el resto de la bahía, en Jerez hay cientos de webs entregadas con el bono Kit Digital y abandonadas a su suerte: WordPress obsoleto, formularios con reCAPTCHA que no deja enviar, HTTPS a medias y cero SEO. El negocio cree que «ya tiene web» y lo que tiene es un documento muerto. Auditarla cuesta poco y suele ser el primer paso de todo lo demás."),
        ],
    ),
    "san-fernando": dict(
        name="San Fernando", short="San Fernando", pop="~96.000 habitantes",
        fleet_keys=["reformassanfernando.com", "fumigacionsanfernando.es"],
        neighbors=["cadiz", "puerto-real", "chiclana"],
        sectors=["Comercio y hostelería de la Calle Real", "Empresas del Polígono IPEC y nave industrial",
                 "Clínicas dentales y fisioterapia", "Autoescuelas y formación", "Despachos y gestorías", "Servicios del hogar (reformas, plagas, climatización)"],
        angles=[
            ("La Isla tiene su propia intención de búsqueda",
             "San Fernando no es «Cádiz» para Google: cuando alguien busca «fontanero San Fernando» o «clínica dental San Fernando», Google muestra negocios de la Isla y de los alrededores, no los de la capital. Una web que solo dice «en Cádiz» pierde esas búsquedas. Decir «San Fernando», «Calle Real», «IPEC», «Bahía Sur» en el sitio, en el GBP y en las citas locales es lo que hace que Google entienda dónde está el negocio de verdad."),
            ("Un tejido de negocios de proximidad",
             "La economía de San Fernando es de proximidad: comercio, hostelería, servicios del hogar, despachos. En ese tipo de mercado el 80 % de las decisiones pasa por el pack local de Maps y por el móvil. El trabajo que mueve la aguja es GBP + una web rápida en móvil + reseñas; el contenido largo y la autoridad vienen después."),
            ("Ventaja frente a las agencias de la capital",
             "Casi ninguna agencia de Cádiz o Jerez tiene página propia de San Fernando. Es más fácil posicionar «agencia SEO San Fernando» que «agencia SEO Cádiz» porque simplemente hay menos páginas que compiten. Para los negocios pasa lo mismo en su sector: quien trabaje el nombre de la ciudad en su web y su GBP se lleva un mercado que los de fuera están dejando libre."),
        ],
    ),
    "chiclana": dict(
        name="Chiclana de la Frontera", short="Chiclana", pop="~85.000 habitantes, que se multiplican en verano",
        fleet_keys=["reformaschiclana.es", "controldeplagaschiclana.es", "multiservicioschiclana24h.es"],
        neighbors=["puerto-santa-maria", "san-fernando", "cadiz"],
        sectors=["Turismo y hostelería de La Barrosa y Novo Sancti Petri", "Construcción, reformas e inmobiliarias",
                 "Comercio del centro y urbanizaciones", "Clínicas dentales y estética", "Gestorías y despachos", "Servicios del hogar"],
        angles=[
            ("Dos ciudades en una: Chiclana todo el año y La Barrosa en verano",
             "Chiclana tiene una economía doble. De octubre a mayo manda el negocio local: reformas, gestorías, clínicas, comercio. De junio a septiembre manda La Barrosa y Novo Sancti Petri: hostelería, turismo, chiringuitos, alquiler. Una web que no tiene páginas para las dos estaciones pierde la mitad del año. La estrategia es construir el contenido de temporada con meses de antelación para que Google lo tenga posicionado cuando llegue el verano."),
            ("El mercado inmobiliario y de reformas más activo de la bahía",
             "Chiclana es donde más se construye y se reforma de la zona, y eso se nota en las búsquedas: reformas integrales, cocinas, placas solares, apartamentos en La Barrosa. Es un mercado con presupuesto alto por lead, y por eso mismo el que más sufre la competencia de portales nacionales (Habitaclia, Milanuncios) que se llevan las primeras posiciones. Ganarle a un portal es posible con contenido local real y autoridad de barrio, no con más texto."),
            ("Turismo: competir con las grandes plataformas",
             "En «hotel en Chiclana» o «restaurante La Barrosa» salen Booking, TripAdvisor y ElTenedor. Competir ahí de frente es perder. La vía es la búsqueda de cola larga con intención («apartamento con piscina en La Barrosa», «arroz con pulpo en Chiclana») y la conversión directa sin intermediarios, que es donde el negocio gana margen."),
        ],
    ),
    "puerto-real": dict(
        name="Puerto Real", short="Puerto Real", pop="~42.000 habitantes",
        fleet_keys=["controldeplagaspuertoreal.es", "reformaspuertoreal.es"],
        neighbors=["cadiz", "san-fernando", "jerez"],
        sectors=["Universidad (UCA, Campus de Puerto Real) y formación", "Industria e ingeniería (Airbus, navantas, Astilleros)",
                 "Comercio y hostelería del casco", "Clínicas y servicios de salud", "Servicios del hogar", "Deporte y actividades infantiles"],
        angles=[
            ("Una ciudad con industria y universidad, no solo comercio",
             "Puerto Real no es un municipio puramente residencial: tiene el campus de la UCA, la zona industrial de Las Aletas y Astilleros, y un casco con comercio de proximidad. Eso genera dos tipos de búsqueda muy distintos: la del estudiante y la del profesional que trabaja en la zona (almuerzo, fisioterapia, autoescuela) y la del negocio industrial B2B que busca proveedores. La web tiene que hablar a ambos sin mezclarlos."),
            ("Entre Cádiz y Jerez: la ubicación importa",
             "Puerto Real está a 15 minutos de Cádiz y a 20 de Jerez. Para Google, «clínica dental Puerto Real» es una búsqueda distinta a «clínica dental Cádiz». Muchos negocios de Puerto Real tienen la web hecha por una agencia de la capital y ni siquiera mencionan Puerto Real en la home: le están regalando las búsquedas de su propia ciudad a los de Cádiz."),
            ("Poco volumen, poca competencia",
             "Es un municipio pequeño en búsquedas, pero por eso mismo las primeras posiciones están casi vacías: pocas webs locales trabajadas, muchos GBP abandonados. Para un negocio local es el lugar más barato de la bahía para llegar al top 3 y el mejor sitio para empezar."),
        ],
    ),
    "puerto-santa-maria": dict(
        name="El Puerto de Santa María", short="El Puerto", pop="~88.000 habitantes",
        fleet_keys=["controlplagaspuertosantamaria.es", "reformaselpuerto.es"],
        neighbors=["puerto-real", "jerez", "chiclana"],
        sectors=["Turismo y hostelería (Valdelagrana, Playa de La Puntilla, bodegas)", "Pesca y comercio del puerto",
                 "Clínicas dentales y estética", "Inmobiliarias y reformas", "Despachos y gestorías", "Autoescuelas y formación"],
        angles=[
            ("Turismo, bodegas y playa: tres mercados en una web",
             "El Puerto tiene el casco histórico, el paseo marítimo y Valdelagrana, más las bodegas de fino. Son tres públicos distintos que buscan cosas distintas en momentos distintos del año. La web de un negocio de El Puerto tiene que tener páginas para cada uno y enlazarlas bien entre sí, porque Google decide a qué página mostrar según la intención, no según la home."),
            ("El nombre más difícil de la bahía",
             "«El Puerto de Santa María» es largo, y la gente lo busca de tres formas: «El Puerto», «El Puerto de Santa María» y «Puerto Santa María». Si la web solo usa una, pierde las otras. Título, H1, GBP, descripciones y citas locales tienen que alternar las variantes de forma natural para que Google las asocie todas al mismo negocio."),
            ("Entre Jerez y Cádiz, con identidad propia",
             "El Puerto está a 20 minutos de Jerez y a 30 de Cádiz, pero sus habitantes no buscan en Jerez: buscan en El Puerto. Los negocios locales que solo aparecen por el nombre grande pierden la búsqueda de su propia ciudad. Para una agencia es una ventaja: hay pocas webs de servicios que digan «El Puerto de Santa María» en el título y el contenido."),
        ],
    ),
}

# Plantillas de título/descripción por tipo
def kw_seo(slug):
    c = CITIES[slug]
    return dict(
        title=f"Agencia SEO en {c['short'] if slug!='puerto-santa-maria' else 'El Puerto de Santa María'} — Posicionamiento Web {YEAR} | Casas Digital",
        desc=f"Agencia SEO en {c['name']}: SEO local para negocios de {c['short']}, zona centro y toda la bahía de Cádiz. Auditoría gratis, SEO mensual, Google Business Profile y diseño web desde 300€.",
        h1=f"Agencia SEO en {c['short'] if slug!='puerto-santa-maria' else 'El Puerto de Santa María'}",
        tag=f"SEO Local · {c['name']}",
    )

def kw_dw(slug):
    c = CITIES[slug]
    short = c['short'] if slug != 'puerto-santa-maria' else 'El Puerto de Santa María'
    return dict(
        title=f"Diseño web en {short} — Webs que posicionan en Google, desde 300€ | Casas Digital",
        desc=f"Diseño web en {c['name']}: páginas web rápidas, optimizadas para SEO local en {c['short']} y la bahía de Cádiz. Desde 300€ (sin dominio ni hosting). Pide presupuesto sin compromiso.",
        h1=f"Diseño web en {short}",
        tag=f"Diseño web · {c['name']}",
    )
