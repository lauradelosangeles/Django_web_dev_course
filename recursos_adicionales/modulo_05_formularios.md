# Módulo 5: Formularios Django — El Usuario Habla con el Servidor

---

## Diapositiva 1: El Ciclo de Vida de un Formulario — GET vs. POST
- **Conceptos:**
  - **GET** → el usuario llega a la página por primera vez → mostrar formulario vacío
  - **POST** → el usuario envía el formulario → procesar y guardar datos
  - La misma vista maneja los dos casos con un `if request.method == 'POST'`
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
def contacto(request):
    if request.method == 'POST':
        # Procesar datos enviados
        form = ContactoForm(request.POST)
        ...
    else:
        # GET: mostrar formulario vacío
        form = ContactoForm()

    return render(request, 'hub/contacto.html', _ctx({'form': form}))
```

---

## Diapositiva 2: Crear un Formulario — La Clase `forms.Form`
- **Conceptos:**
  - `forms.Form` define los campos y sus validaciones en Python
  - `widget=` controla cómo se renderiza el campo en HTML
  - `attrs={'class': 'form-control'}` inyecta clases CSS de Bootstrap automáticamente
- **Fragmento de Código Recomendado:**
```python
# hub/forms.py
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Tu nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre completo'
        }),
    )
    correo  = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    )
```

---

## Diapositiva 3: Protección CSRF — La Defensa Invisible
- **Conceptos:**
  - **CSRF** = Cross-Site Request Forgery → ataque en el que otra web envía formularios en tu nombre
  - `{% csrf_token %}` genera un token secreto único por sesión
  - Django rechaza automáticamente cualquier POST sin el token válido
- **Fragmento de Código Recomendado:**
```html
<!-- templates/hub/contacto.html -->
<form method="POST" novalidate>
  {% csrf_token %}   {# ← obligatorio en TODO formulario POST #}

  {% for field in form %}
  <div class="mb-4">
    <label for="{{ field.id_for_label }}" class="form-label">
      {{ field.label }}
    </label>
    {{ field }}   {# renderiza el <input> con sus attrs de Bootstrap #}
    {% if field.errors %}
      <div style="color:#e53e3e; font-size:.8rem; margin-top:.35rem;">
        {% for error in field.errors %}{{ error }}{% endfor %}
      </div>
    {% endif %}
  </div>
  {% endfor %}

  <button type="submit">Enviar mensaje →</button>
</form>
```

---

## Diapositiva 4: Validación y Datos Limpios — `is_valid()` y `cleaned_data`
- **Conceptos:**
  - `form.is_valid()` → ejecuta todas las validaciones (campos requeridos, formato email, etc.)
  - `form.cleaned_data` → diccionario con los datos **ya validados y saneados**
  - Si el formulario es inválido, se devuelve al usuario con los errores visibles
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # cleaned_data: datos seguros y validados
            nombre  = form.cleaned_data['nombre']
            correo  = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            # ... guardar en BD
        else:
            # Django re-renderiza el form con errores por campo
            pass
```

---

## Diapositiva 5: Guardar en la BD y Redirigir — El Patrón PRG
- **Conceptos:**
  - **PRG** = Post/Redirect/Get → evita que recargar la página reenvíe el formulario
  - `Mensaje.objects.create(...)` → inserta el registro en la base de datos
  - `redirect('nombre_url')` → 302 al cliente para que haga un GET limpio
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
from django.shortcuts import render, redirect
from .models import Mensaje

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre  = form.cleaned_data['nombre'],
                correo  = form.cleaned_data['correo'],
                mensaje = form.cleaned_data['mensaje'],
            )
            return redirect('contacto')  # ← Patrón PRG
    else:
        form = ContactoForm()
    return render(request, 'hub/contacto.html', _ctx({'form': form}))
```

---

## Diapositiva 6: Mensajes Flash — Feedback Inmediato al Usuario
- **Conceptos:**
  - `messages.success(request, texto)` → almacena un mensaje en la sesión del usuario
  - Se consume automáticamente en la siguiente petición (desaparece al recargar)
  - `{% for message in messages %}` lo renderiza en cualquier plantilla
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
from django.contrib import messages

if form.is_valid():
    Mensaje.objects.create(...)
    messages.success(
        request,
        f'¡Gracias, {form.cleaned_data["nombre"]}! Tu mensaje fue recibido.',
    )
    return redirect('contacto')
else:
    messages.error(request, 'Por favor corrige los errores del formulario.')
```
```html
<!-- base.html — mostrar mensajes en todas las páginas -->
{% for message in messages %}
  <div class="alert alert-{{ message.tags }}">{{ message }}</div>
{% endfor %}
```

---

## Diapositiva 7: Internacionalización — Una App, Dos Idiomas
- **Conceptos:**
  - Mismo patrón MTV, pero con contextos y plantillas distintas por idioma
  - Una función helper `_ctx_en()` redefine las etiquetas en inglés
  - Las rutas `/en/` en `urls.py` apuntan a vistas espejo en inglés
- **Fragmento de Código Recomendado:**
```python
# hub/urls.py — rutas en español e inglés
urlpatterns = [
    path('',            views.inicio,      name='inicio'),
    path('contacto/',   views.contacto,    name='contacto'),
    # — English —
    path('en/',         views.inicio_en,   name='inicio_en'),
    path('en/contact/', views.contact_en,  name='contacto_en'),
]

# hub/views.py — contexto independiente para inglés
def _ctx_en(extra=None):
    base = {
        'nombre_docente':       'Teacher Gonzalez Silva',
        'stat_lbl_anos':        'Years of Experience',
        'stat_lbl_estudiantes': 'Students Taught',
    }
    if extra: base.update(extra)
    return base
```

---

## Diapositiva 8: Demo en Vivo — El Formulario Completo en Acción
- **Conceptos:**
  - Archivo de referencia: `semana_5/demo/finalizado/hub/views.py` y `forms.py`
  - La sesión muestra el flujo completo: formulario vacío → POST → validación → guardado → mensaje → redirect
  - Se verifica en `/admin/ → Mensajes` que el mensaje efectivamente quedó guardado en la BD
- **Fragmento de Código Recomendado:**
```
Flujo completo de la demo:

1. forms.py      → class ContactoForm(forms.Form): nombre, correo, mensaje
2. views.py      → def contacto(request):
                       GET  → ContactoForm() vacío → render
                       POST → ContactoForm(request.POST)
                              is_valid() → Mensaje.objects.create(...)
                              messages.success(...) → redirect('contacto')
3. contacto.html → <form method="POST">{% csrf_token %}...
4. base.html     → {% for message in messages %}...{% endfor %}
5. /admin/       → Mensajes → confirma que el mensaje quedó guardado ✓
```

---

## Diapositiva 9: Trabajo en Clase — Completa la Vista `contacto()` (20 min)
- **Conceptos:**
  - Archivo de trabajo: `semana_5/ejercicio_clase/plantilla/hub/views.py`
  - **Ejercicio 1:** Completa la zona de personalización
  - **Ejercicio 2:** Implementa la vista `contacto()` completa usando el prompt de IA
- **Fragmento de Código Recomendado:**
```python
# EJERCICIO 2 — Usa Ctrl+K en Cursor con este prompt:
# "Crea la vista contacto() que maneje GET y POST.
#  En GET: instancia ContactoForm vacío y renderiza
#  'hub/contacto.html' con el formulario en el contexto.
#  En POST: valida el formulario; si es válido, crea un
#  Mensaje con los datos limpios, agrega messages.success
#  y redirige a 'contacto'. Si no es válido, re-renderiza
#  con el formulario y sus errores."

def contacto(request):
    # COMPLETA AQUÍ ↓
    pass

# Verifica el resultado:
# 1. Ve a http://127.0.0.1:8000/contacto/
# 2. Envía un mensaje de prueba
# 3. ¿Aparece el mensaje de confirmación?
# 4. Ve a /admin/ → Mensajes y confirma que se guardó
```

---

## Diapositiva 10: Tarea y Entregables — ¡A Producción!
- **Conceptos:**
  - Archivo de tarea: `semana_5/tarea/plantilla_tarea/hub/views.py`
  - **Tareas 1–3:** La vista `contacto()` ya está dada — personalizarla y ejecutarla
  - **Tarea 4 (el gran hito):** Desplegar el hub completo en **PythonAnywhere** y compartir la URL pública
- **Fragmento de Código Recomendado:**
```
TAREA 1 → Completa la zona de personalización con tu info real
TAREA 2 → Lee y ejecuta la vista contacto() ya dada
TAREA 3 → Personaliza el mensaje de éxito con tu nombre:
            messages.success(request,
              '¡Gracias, [tu nombre]! Tu mensaje fue enviado.')

TAREA 4 → Sigue el README.md para desplegar en PythonAnywhere:
            1. Crea cuenta gratuita en pythonanywhere.com
            2. Sube tu proyecto (Git o archivo .zip)
            3. Configura el Web App desde el panel de PA
            4. Configura ALLOWED_HOSTS y SECRET_KEY
            5. Colecta archivos estáticos: collectstatic

──────────────────────────────────────────────────
ENTREGA:  URL pública de tu hub en PythonAnywhere
          Ejemplo: tuusuario.pythonanywhere.com

CRITERIO: El sitio carga en producción con tu
          información real y el formulario funciona
```
