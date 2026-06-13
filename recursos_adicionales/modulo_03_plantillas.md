# Módulo 3: Plantillas Django — Separando HTML de Python

---

## Diapositiva 1: El Problema — HTML dentro de Python
- **Conceptos:**
  - `HttpResponse` con HTML largo es imposible de mantener
  - Un diseñador no puede editar HTML si está enterrado en código Python
  - Las plantillas separan **responsabilidades**: Python maneja lógica, HTML maneja presentación
- **Fragmento de Código Recomendado:**
```python
# ❌ ANTES (Semana 2): inmanejable con páginas reales
def inicio(request):
    return HttpResponse(f"""<!DOCTYPE html><html>...(200 líneas de HTML)...</html>""")

# ✅ AHORA (Semana 3): limpio y separado
def inicio(request):
    return render(request, 'hub/inicio.html', {'nombre': 'Prof. González'})
```

---

## Diapositiva 2: La Función `render()` y el Contexto
- **Conceptos:**
  - `render(request, 'plantilla.html', contexto)` → los tres argumentos clave
  - El **contexto** es un diccionario: las claves se convierten en variables de plantilla
  - `_ctx()` es un helper que centraliza las variables compartidas entre todas las vistas
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
from django.shortcuts import render

def _ctx(extra=None):
    base = {
        'nombre_docente': "Prof. González Silva",
        'materia':        "Matemáticas",
        'correo':         "prof@colegio.edu",
    }
    if extra:
        base.update(extra)  # agrega variables adicionales
    return base

def acerca(request):
    return render(request, 'hub/acerca.html', _ctx())
```

---

## Diapositiva 3: La Plantilla Base — Herencia de Templates
- **Conceptos:**
  - `base.html` define el esqueleto (navbar, footer, CSS) **una sola vez**
  - `{% block content %}{% endblock %}` → marca el espacio que cada página rellena
  - DRY: *Don't Repeat Yourself* — si el navbar cambia, lo cambias en un solo archivo
- **Fragmento de Código Recomendado:**
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
  <title>{% block title %}Hub Docente{% endblock %}</title>
  <!-- CSS y Bootstrap aquí -->
</head>
<body>

  <nav>...</nav>

  {% block content %}
  {# Cada página hija rellena este espacio #}
  {% endblock %}

  <footer>...</footer>
</body>
</html>
```

---

## Diapositiva 4: Páginas Hijas — `{% extends %}` y `{% block %}`
- **Conceptos:**
  - `{% extends "base.html" %}` → la primera línea de TODA página hija
  - Solo se escribe el contenido **único** de esa página dentro del `{% block %}`
  - Todo lo que está fuera de un `{% block %}` en una hija es **ignorado**
- **Fragmento de Código Recomendado:**
```html
<!-- templates/hub/acerca.html -->
{% extends "base.html" %}

{% block title %}Acerca — {{ nombre_docente }}{% endblock %}

{% block content %}
<header class="ph">
  <h1>{{ nombre_docente }}</h1>
  <p>Docente de {{ materia }} · {{ institucion }}</p>
</header>
{% endblock %}
```

---

## Diapositiva 5: Variables de Plantilla `{{ }}` y Lógica Condicional
- **Conceptos:**
  - `{{ variable }}` → imprime el valor de la clave del contexto
  - Las variables pueden encadenarse: `{{ docente.nombre }}`
  - El navbar activo usa lógica condicional dentro del HTML con `{% if %}`
- **Fragmento de Código Recomendado:**
```html
<!-- templates/base.html — Navbar con enlace activo dinámico -->
<nav class="nb py-2">
  <a href="{% url 'inicio' %}" class="nb-brand">{{ nombre_docente }}</a>
  <div>
    <a href="{% url 'inicio' %}"
       class="nb-link {% if request.resolver_match.url_name == 'inicio' %}active{% endif %}">
       Inicio
    </a>
    <a href="{% url 'acerca' %}"
       class="nb-link {% if request.resolver_match.url_name == 'acerca' %}active{% endif %}">
       Acerca
    </a>
  </div>
</nav>
```

---

## Diapositiva 6: La Etiqueta `{% url %}` — Links que No Se Rompen
- **Conceptos:**
  - `{% url 'nombre_de_url' %}` → Django calcula la ruta exacta automáticamente
  - Si cambias `/acerca/` a `/sobre-mi/` en `urls.py`, los links se actualizan solos
  - El `name=` en `urls.py` es el identificador que usa `{% url %}`
- **Fragmento de Código Recomendado:**
```python
# hub/urls.py — el name= es lo que usamos en {% url %}
urlpatterns = [
    path('',          views.inicio,        name='inicio'),
    path('acerca/',   views.acerca,        name='acerca'),
    path('recursos/', views.recursos_view, name='recursos'),
]
```
```html
<!-- En la plantilla: nunca escribas /acerca/ directamente -->
<a href="{% url 'acerca' %}">Ver mi perfil</a>
<a href="{% url 'recursos' %}">Recursos</a>
```

---

## Diapositiva 7: Pasar Listas al Template — `{% for %}` y `{% if %}`
- **Conceptos:**
  - Una lista de diccionarios en el contexto se itera con `{% for item in lista %}`
  - `{% if lista %}` verifica que la lista no esté vacía antes de renderizarla
  - `{{ forloop.counter }}` es una variable mágica que cuenta las iteraciones
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
recursos_lista = [
    {"titulo": "Khan Academy", "url": "https://es.khanacademy.org"},
    {"titulo": "Desmos",       "url": "https://www.desmos.com"},
]
def recursos_view(request):
    return render(request, 'hub/recursos.html', _ctx({'recursos': recursos_lista}))
```
```html
{% for recurso in recursos %}
  <div class="rec-card">
    <span class="rec-num">{{ forloop.counter }}</span>
    <a href="{{ recurso.url }}">{{ recurso.titulo }}</a>
  </div>
{% endfor %}
```

---

## Diapositiva 8: Demo en Vivo — De `HttpResponse` a `render()`
- **Conceptos:**
  - Archivo de referencia: `semana_3/demo/finalizado/hub/views.py` + `templates/`
  - La sesión migra las vistas existentes de Semana 2 → elimina el HTML del Python
  - Se muestra la carpeta `templates/` con `base.html` y las tres páginas hijas
- **Fragmento de Código Recomendado:**
```
templates/
├── base.html              ← navbar + footer + CSS compartido
└── hub/
    ├── inicio.html        ← {% extends "base.html" %}
    ├── acerca.html        ← {% extends "base.html" %}
    └── recursos.html      ← {% extends "base.html" %}
                              {% for recurso in recursos %}...{% endfor %}

hub/views.py
  inicio()        → render(request, 'hub/inicio.html', _ctx({...}))
  acerca()        → render(request, 'hub/acerca.html', _ctx())
  recursos_view() → render(request, 'hub/recursos.html', _ctx({'recursos': lista}))
```

---

## Diapositiva 9: Trabajo en Clase — Migrar a Templates (20 min)
- **Conceptos:**
  - Archivo de trabajo: `semana_3/ejercicio_clase/plantilla/hub/views.py`
  - La vista `inicio()` ya usa `render()` — úsala como modelo para los demás ejercicios
  - **Ejercicio 2 y 3:** Usa `Ctrl+K` en Cursor para que la IA complete las vistas
- **Fragmento de Código Recomendado:**
```python
# EJERCICIO 1 — Completa la zona de personalización
nombre_docente = ""    # → "Prof. Ramírez"
recursos_lista = [
    # {"titulo": "...", "url": "https://...", "descripcion": "..."},
]

# EJERCICIO 2 — Convierte acerca() a render()
# Prompt Cursor (Ctrl+K):
# "Convierte esta vista a render(). Crea el contexto con
#  nombre_docente, materia, institucion y anos_experiencia.
#  La plantilla a usar es 'hub/acerca.html'."
def acerca(request):
    pass  # ← COMPLETA AQUÍ

# EJERCICIO 3 — Crea recursos_view() con render()
# Prompt: "Crea la vista recursos_view que use render() con
# 'hub/recursos.html' y pase recursos_lista bajo 'recursos'."
```

---

## Diapositiva 10: Tarea y Entregables
- **Conceptos:**
  - Archivo de tarea: `semana_3/tarea/plantilla_tarea/hub/views.py`
  - Las vistas `inicio()` y `acerca()` están dadas; **Tarea 3** es completar `recursos_view()`
  - Hay que agregar al menos **3 recursos reales** de la materia propia en `recursos_lista`
- **Fragmento de Código Recomendado:**
```python
# TAREA 3 — Completa esta vista
recursos_lista = [
    # Agrega al menos 3 recursos reales de tu materia
    # {"titulo": "Nombre del sitio", "url": "https://...", "descripcion": "Para qué sirve"},
]

def recursos_view(request):
    # Prompt Cursor (Ctrl+K):
    # "Completa esta vista para que use render() con la
    #  plantilla 'hub/recursos.html' y pase recursos_lista
    #  bajo la clave 'recursos' y nombre_docente en el contexto."
    pass

# ──────────────────────────────────────────────────
# ENTREGA:  views.py + templates/hub/recursos.html completados
# CRITERIO: Las 3 URLs muestran tu contenido real
#           (inicio, acerca y recursos con tus datos)
```
