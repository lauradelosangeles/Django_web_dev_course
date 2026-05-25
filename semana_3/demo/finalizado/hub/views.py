from django.shortcuts import render

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = "Prof. González Silva"
iniciales        = "PG"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"
num_estudiantes  = "320"
num_materias     = "3"
correo           = "prof.garcia@colegio.edu"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."

icono_materia      = "📐"
desc_card_sobre_mi = f"Mi trayectoria, filosofía de enseñanza y {anos_experiencia} años formando estudiantes en {materia}."
desc_card_materias = f"Grupos activos este semestre con materiales y actividades en {institucion}."
desc_card_recursos = "Materiales, ejercicios y sitios de referencia para reforzar el aprendizaje."

stat_lbl_anos        = "Años de experiencia"
stat_lbl_estudiantes = "Estudiantes formados"
stat_lbl_materias    = "Materias activas"

recursos_lista = [
    {"titulo": "Khan Academy",  "url": "https://es.khanacademy.org",               "descripcion": "Lecciones y ejercicios gratuitos de matemáticas y ciencias."},
    {"titulo": "Desmos",        "url": "https://www.desmos.com",                   "descripcion": "Graficadora interactiva para explorar funciones matemáticas."},
    {"titulo": "GeoGebra",      "url": "https://www.geogebra.org",                 "descripcion": "Geometría dinámica, álgebra y calculadora estadística."},
]
# ════════════════════════════════════════════════════════════


def _ctx(extra=None):
    base = {
        'nombre_docente': nombre_docente, 'iniciales': iniciales,
        'materia': materia, 'institucion': institucion,
        'anos_experiencia': anos_experiencia, 'num_estudiantes': num_estudiantes,
        'num_materias': num_materias, 'correo': correo, 'frase_mision': frase_mision,
        'icono_materia': icono_materia,
        'stat_lbl_anos': stat_lbl_anos, 'stat_lbl_estudiantes': stat_lbl_estudiantes,
        'stat_lbl_materias': stat_lbl_materias,
    }
    if extra:
        base.update(extra)
    return base


def inicio(request):
    return render(request, 'hub/inicio.html', _ctx({
        'desc_card_sobre_mi': desc_card_sobre_mi,
        'desc_card_materias': desc_card_materias,
        'desc_card_recursos': desc_card_recursos,
    }))


def acerca(request):
    return render(request, 'hub/acerca.html', _ctx())


def recursos_view(request):
    return render(request, 'hub/recursos.html', _ctx({'recursos': recursos_lista}))
