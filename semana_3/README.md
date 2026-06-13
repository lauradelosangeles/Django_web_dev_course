# Semana 3: Plantillas Dinámicas y Herencia

> Una plantilla Django es HTML con espacios en blanco que el servidor rellena con datos reales.
> La herencia (`base.html`) evita copiar el menú en cada página del Hub.

## Objetivo de Aprendizaje

Al finalizar esta semana podrás **separar el HTML de Python** usando el motor de plantillas de Django, pasar datos del servidor a la plantilla con un contexto, y reutilizar la estructura base con herencia de plantillas.

---

## El concepto

`{{ variable }}` inserta datos; `{% for %}`, `{% if %}` y `{% block %}` añaden lógica de presentación. `{% extends "base.html" %}` hace que cada página herede navbar y pie de página: un cambio en la base actualiza todo el sitio.

**Analogía:** la plantilla base es la hoja membretada del colegio; cada página solo completa la sección de contenido.

## En el Hub Personal del Docente

Creas `templates/base.html` con Bootstrap 5 y páginas `hub/inicio.html`, `acerca.html` y `recursos.html` que heredan de la base. Las vistas pasan de `HttpResponse` a `render(request, plantilla, contexto)`.

---

## Actividades de la semana

| Actividad | Carpeta | Tema | Descripción |
|-----------|---------|------|-------------|
| **Demo** | `demo/inicio/` → `demo/finalizado/` | `render()` y herencia de plantillas | El inicio conserva vistas con `HttpResponse` y `base.html` vacío. En vivo refactorizas a `render()`, construyes `templates/base.html` (Bootstrap, navbar) e `hub/inicio.html` con `{% extends %}`. El finalizado tiene tres páginas con plantillas y contexto. |
| **Actividad en clase** | `ejercicio_clase/plantilla/` | Vistas `acerca()` y `recursos_view()` | Personalizas datos del docente. `inicio()` ya usa `render()`. Conviertes `acerca()` a plantilla y creas `recursos_view()` que pasa `recursos_lista` a `hub/recursos.html`. Criterio: las 3 URLs usan plantillas, sin `HttpResponse`. |
| **Tarea** | `tarea/plantilla_tarea/` | Página de recursos propia | Completas variables, revisas `inicio()` y `acerca()` dadas, armas una lista de al menos 3 recursos reales de tu materia y completas `recursos_view()` + plantilla. Criterio: las 3 URLs muestran tu contenido. |
| **Diseño previo** | `diseno/` | Requisitos y wireframe | Antes de programar, rellenas la tabla de requisitos funcionales y no funcionales (`requisitos.md`), bocetas la pantalla `/recursos/` en papel o herramienta digital (`wireframe_recursos.md`) y te autoevalúas con la rúbrica de usabilidad y accesibilidad (`rubrica_usabilidad.md`). |

---

## Fuente de Verdad de Cada Archivo

| Archivo | Responsabilidad |
|---------|----------------|
| `hub/views.py` | Usa `render()` para combinar vista + plantilla + contexto |
| `templates/base.html` | Estructura compartida: nav, footer, bloques Bootstrap |
| `templates/hub/inicio.html` | Hereda de base, rellena `{% block contenido %}` |
| `templates/hub/acerca.html` | Hereda de base, muestra datos del docente |
| `templates/hub/recursos.html` | Hereda de base, itera sobre lista de recursos |
| `static/css/estilos.css` | Estilos personalizados adicionales a Bootstrap |

---

## Teoría

| Concepto | Qué hace | Analogía docente |
|----------|----------|------------------|
| `{{ variable }}` | Muestra un valor del contexto | Espacio en blanco de una circular |
| `{% block %}` | Zona que las hijas reemplazan | Sección “observaciones” del informe |
| `{% extends %}` | Hereda otra plantilla | Informe con formato oficial |
| **Contexto** | Diccionario vista → plantilla | Sobre con datos para rellenar |
| `render()` | Combina solicitud, plantilla y contexto | Imprimir la circular ya completada |

### Sintaxis esencial

| Sintaxis | Uso |
|----------|-----|
| `{% block nombre %}{% endblock %}` | Define zona rellenable |
| `{% extends "base.html" %}` | Primera línea de plantillas hijas |
| `{% for item in lista %}` | Bucle sobre lista Python |
| `{% if condicion %}` | Condicional |
| `{% url 'nombre_ruta' %}` | URL por nombre de ruta |
| `{% load static %}` / `{% static '...' %}` | Archivos CSS e imágenes |

---

## De HttpResponse a render()

```python
# ANTES (Semana 2)
def inicio(request):
    return HttpResponse(f"<h1>{nombre_docente}</h1>")

# AHORA (Semana 3)
def inicio(request):
    contexto = {'nombre_docente': nombre_docente, 'materia': materia}
    return render(request, 'hub/inicio.html', contexto)
```

---

## Herencia de Plantillas

```
templates/
├── base.html              ← nav, footer, <head>, Bootstrap
└── hub/
    ├── inicio.html        ← {% extends "base.html" %}
    ├── acerca.html
    └── recursos.html      ← {% for recurso in recursos %}
```

---

## Errores comunes

1. **`TemplateDoesNotExist`** — ruta incorrecta en `render()` o carpeta `templates/` mal ubicada (`templates/hub/...`).
2. **Variable vacía en pantalla** — typo en `{{ nombre }}` vs clave del contexto (Django no avisa).
3. **Falta `{% endfor %}` o `{% endif %}`** — cada bloque necesita cierre explícito.
4. **`{% extends %}` no es la primera línea** — debe ir antes de cualquier HTML.

---

## Glosario

- **Plantilla / motor de plantillas:** HTML + marcadores que Django convierte en página final.
- **Contexto:** diccionario de datos disponibles en la plantilla.
- **CDN:** servidor externo (p. ej. Bootstrap 5) sin descargar archivos al proyecto.

---

## Siguiente semana

Los recursos viven en listas fijas dentro del código. La semana 4 los guarda en SQLite y permite gestionarlos desde `/admin/` sin tocar Python.

---

## Prompts de Cursor AI para Esta Semana

**Prompt 1 — Refactorizar a render():**
> "Convierte esta vista Django que usa HttpResponse a una que use render(). Crea el archivo de plantilla correspondiente en templates/hub/ con el mismo HTML, pero usando variables de plantilla Django como {{ nombre_docente }} en lugar de f-strings de Python."

**Prompt 2 — Crear base.html con Bootstrap:**
> "Crea un archivo templates/base.html para un hub de docente. Incluye Bootstrap 5 desde CDN, una barra de navegación con enlaces a Inicio, Acerca y Recursos, y un {% block contenido %}{% endblock %}. El navbar debe mostrar {{ nombre_docente }} como marca."

**Prompt 3 — Plantilla con bucle for:**
> "Crea templates/hub/recursos.html que herede de base.html. Debe mostrar una lista de recursos usando {% for recurso in recursos %}. Cada recurso tiene 'titulo', 'url' y 'descripcion'. Muéstralos como tarjetas Bootstrap con el título como enlace."

**Prompt 4 — Condicional en plantilla:**
> "En recursos.html, agrega un {% if recursos %}...{% else %}...{% endif %} que muestre '¡Aún no hay recursos disponibles!' cuando la lista esté vacía."

**Prompt 5 — Revisión de accesibilidad:**
> "Revisa este HTML y dime qué mejoras de accesibilidad necesita (alt, roles ARIA, contraste, jerarquía de encabezados) para cumplir buenas prácticas."
