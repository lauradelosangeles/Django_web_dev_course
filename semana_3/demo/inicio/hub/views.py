from django.http import HttpResponse

nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."


def inicio(request):
    return HttpResponse(f"<h1>{nombre_docente}</h1><p>{materia} · {institucion}</p>")


def acerca(request):
    return HttpResponse(f"<h1>Acerca de {nombre_docente}</h1><p>{anos_experiencia} años de experiencia</p>")


def recursos_view(request):
    return HttpResponse("<h1>Recursos</h1><p>Aquí irán los recursos...</p>")
