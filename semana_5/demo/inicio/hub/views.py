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


# ════════════════════════════════════════════════════════════
#  ENGLISH VIEWS  (/en/*)
# ════════════════════════════════════════════════════════════

def inicio_en(request):
    return render(request, 'hub/en/inicio.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'materia': 'Mathematics',
        'institucion': 'School Piquero',
        'frase_mision': 'Every student can master mathematics with the right guidance.',
    })


def about_en(request):
    return render(request, 'hub/en/acerca.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'materia': 'Mathematics',
        'institucion': 'School Piquero',
        'correo': 'prof.gonzalezsilva@school.edu',
        'anos_experiencia': anos_experiencia,
        'frase_mision': 'Every student can master mathematics with the right guidance.',
    })


def resources_en(request):
    from .models import Recurso
    return render(request, 'hub/en/recursos.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'recursos': Recurso.objects.all(),
    })

