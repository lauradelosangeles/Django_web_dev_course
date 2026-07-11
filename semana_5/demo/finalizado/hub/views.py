from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recurso, Mensaje
from .forms import ContactoForm, ContactoFormEN

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = "Prof. Laura Herrera"
iniciales        = "LH"
materia          = "Programación estructurada"
institucion      = "Unidad Educativa Fiscal Dolores Sucre"
anos_experiencia = "25"
num_estudiantes  = "320"
num_materias     = "3"
correo           = "angeles.herrera@docentes.edu.ec"
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


# ════════════════════════════════════════════════════════════
#  ENGLISH VIEWS  (/en/*)
# ════════════════════════════════════════════════════════════

def _ctx_en(extra=None):
    """Context helper with English content and stat labels."""
    base = {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'iniciales': iniciales,
        'materia': 'Mathematics',
        'institucion': 'School Piquero',
        'anos_experiencia': anos_experiencia,
        'num_estudiantes': num_estudiantes,
        'num_materias': num_materias,
        'correo': 'prof.gonzalezsilva@school.edu',
        'frase_mision': 'Every student can master mathematics with the right guidance.',
        'icono_materia': icono_materia,
        'stat_lbl_anos': 'Years of Experience',
        'stat_lbl_estudiantes': 'Students Taught',
        'stat_lbl_materias': 'Active Subjects',
    }
    if extra:
        base.update(extra)
    return base


def inicio_en(request):
    return render(request, 'hub/en/inicio.html', _ctx_en({
        'desc_card_sobre_mi': f'My background, teaching philosophy and {anos_experiencia} years educating students in Mathematics.',
        'desc_card_materias': f'Active groups this semester with materials and activities at School Piquero.',
        'desc_card_recursos': 'Materials and tools available in the resources database.',
        'desc_card_contacto': 'Have questions? Write to me directly and I will reply shortly.',
    }))


def about_en(request):
    return render(request, 'hub/en/acerca.html', _ctx_en())


def resources_en(request):
    return render(request, 'hub/en/recursos.html', _ctx_en({'recursos': Recurso.objects.all()}))


def contact_en(request):
    if request.method == 'POST':
        form = ContactoFormEN(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(
                request,
                f'Thank you, {form.cleaned_data["nombre"]}! Your message was received. I will get back to you soon.',
            )
            return redirect('contacto_en')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ContactoFormEN()
    return render(request, 'hub/en/contacto.html', _ctx_en({'form': form}))
