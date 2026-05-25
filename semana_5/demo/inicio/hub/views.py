from django.shortcuts import render
from .models import Recurso

nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."


def inicio(request):
    return render(request, 'hub/inicio.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'frase_mision': frase_mision,
    })


def acerca(request):
    return render(request, 'hub/acerca.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'anos_experiencia': anos_experiencia,
        'frase_mision': frase_mision,
    })


def recursos_view(request):
    recursos = Recurso.objects.all()
    return render(request, 'hub/recursos.html', {
        'nombre_docente': nombre_docente,
        'recursos': recursos,
    })

