
# Módulo 2: Django — Tu Primera Aplicación Web Dinámica

## Diapositiva 1: ¿Qué es Django? El Patrón MTV
- **Conceptos:**
  - **Model** → gestiona los datos (base de datos)
  - **Template** → lo que el usuario ve (HTML)
  - **View** → la lógica que conecta ambos (Python)
  - Flujo: Navegador → URL → View → Template → Respuesta HTML
- **Fragmento de Código Recomendado:**
```
Petición del navegador
         ↓
    urls.py  →  ¿Qué view maneja esta ruta?
         ↓
    views.py →  Ejecuta la lógica Python
         ↓
  template.html → Renderiza el HTML final
         ↓
    Respuesta al navegador
```

---

## Diapositiva 2: Configurar el Entorno — Instalación Limpia
- **Conceptos:**
  - Entorno virtual → aísla las dependencias del proyecto del sistema global
  - `pip install` instala los paquetes listados en `requirements.txt`
  - `django-admin startproject` crea la estructura base
- **Fragmento de Código Recomendado:**
```bash
# 1. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux

# 2. Instalar Django
pip install Django==4.2.9

# 3. Crear proyecto y aplicación
django-admin startproject hub_docente .
python manage.py startapp hub
```

---

## Diapositiva 3: Anatomía del Proyecto Django
- **Conceptos:**
  - `manage.py` → el comando de control (runserver, migrate, etc.)
  - `hub_docente/settings.py` → configuración global del proyecto
  - `hub_docente/urls.py` → enrutador principal (delega a las apps)
  - `hub/` → la aplicación con la lógica de negocio
- **Fragmento de Código Recomendado:**
```
hub_docente/        ← Proyecto Django
├── manage.py
├── hub_docente/
│   ├── settings.py ← Configuración global
│   ├── urls.py     ← Rutas del proyecto
│   └── wsgi.py
└── hub/            ← Tu aplicación
    ├── views.py    ← Lógica (lo que construimos hoy)
    └── urls.py     ← Rutas de la app
```

---

## Diapositiva 4: Tu Primera Vista — `HttpResponse`
- **Conceptos:**
  - Una **view** es simplemente una función Python que recibe `request` y retorna una respuesta
  - `HttpResponse` devuelve cualquier texto plano o HTML como respuesta
  - Las variables f-string inyectan datos dinámicos directamente en el HTML
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
from django.http import HttpResponse

nombre_docente = "Prof. González Silva"
materia        = "Matemáticas"

def inicio(request):
    return HttpResponse(f"""
        <h1>{nombre_docente}</h1>
        <p>Docente de {materia}</p>
    """)
```

---

## Diapositiva 5: Conectar la Vista — Configurar las URLs
- **Conceptos:**
  - `path('', view, name='nombre')` → mapea una URL a una función view
  - El proyecto delega a la app con `include('hub.urls')`
  - `name=` permite referenciar la URL desde plantillas sin escribir rutas a mano
- **Fragmento de Código Recomendado:**
```python
# hub/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',        views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
]

# hub_docente/urls.py
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hub.urls')),  # delega a la app
]
```

---

## Diapositiva 6: Registrar la App y Verificar en el Navegador
- **Conceptos:**
  - Toda app nueva debe declararse en `INSTALLED_APPS` en `settings.py`
  - `python manage.py runserver` lanza el servidor de desarrollo en `127.0.0.1:8000`
  - El servidor recarga automáticamente al guardar cambios en el código
- **Fragmento de Código Recomendado:**
```python
# hub_docente/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... apps de Django
    'hub',   # ← registrar nuestra aplicación aquí
]

# Terminal:
# python manage.py runserver
# → Abre http://127.0.0.1:8000/
```

---

## Diapositiva 7: Agregar Bootstrap via CDN — Sin Instalar Nada
- **Conceptos:**
  - CDN → el navegador descarga Bootstrap desde un servidor externo
  - La `<link>` del CSS va en `<head>`, el `<script>` del JS va antes del cierre de `</body>`
  - Con `defer` el JS se carga sin bloquear el renderizado de la página
- **Fragmento de Código Recomendado:**
```python
# hub/views.py — CDN como variable para reutilizar
_CDN = """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
          defer></script>
"""

def inicio(request):
    return HttpResponse(f"""
    <head>{_CDN}</head>
    <body>
      <div class="container py-5">
        <h1 class="display-4">{nombre_docente}</h1>
      </div>
    </body>""")
```
