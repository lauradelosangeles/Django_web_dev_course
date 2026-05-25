from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recurso, Mensaje
from .forms import ContactoForm

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
desc_card_recursos = "Materiales y herramientas disponibles en la base de datos de recursos."
desc_card_contacto = "¿Tienes preguntas? Escríbeme directamente y te responderé a la brevedad."

stat_lbl_anos        = "Años de experiencia"
stat_lbl_estudiantes = "Estudiantes formados"
stat_lbl_materias    = "Materias activas"
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
        'desc_card_contacto': desc_card_contacto,
    }))


def acerca(request):
    return render(request, 'hub/acerca.html', _ctx())


def recursos_view(request):
    return render(request, 'hub/recursos.html', _ctx({'recursos': Recurso.objects.all()}))


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(
                request,
                f'¡Gracias, {form.cleaned_data["nombre"]}! Tu mensaje fue recibido. Te responderé pronto.',
            )
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ContactoForm()
    return render(request, 'hub/contacto.html', _ctx({'form': form}))
