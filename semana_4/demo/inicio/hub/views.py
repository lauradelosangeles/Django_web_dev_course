from django.shortcuts import render

nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."

recursos_lista = [
    {"titulo": "Khan Academy",  "url": "https://es.khanacademy.org",               "descripcion": "Ejercicios y videos gratuitos"},
    {"titulo": "Desmos",        "url": "https://www.desmos.com/scientific?lang=es", "descripcion": "Calculadora gráfica interactiva"},
    {"titulo": "GeoGebra",      "url": "https://www.geogebra.org",                 "descripcion": "Geometría dinámica"},
]


def inicio(request):
    return render(request, 'hub/inicio.html', {'nombre_docente': nombre_docente, 'materia': materia, 'institucion': institucion, 'frase_mision': frase_mision})


def acerca(request):
    return render(request, 'hub/acerca.html', {'nombre_docente': nombre_docente, 'materia': materia, 'institucion': institucion, 'anos_experiencia': anos_experiencia, 'frase_mision': frase_mision})


def recursos_view(request):
    return render(request, 'hub/recursos.html', {'nombre_docente': nombre_docente, 'recursos': recursos_lista})


# EN CLASE: reemplazaremos recursos_lista por Recurso.objects.all()
