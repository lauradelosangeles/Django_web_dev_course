# Guía de Docente — Demo Semana 2
**Duración objetivo:** 10–15 minutos  
**Carpetas:** `demo/inicio/` (punto de partida) · `demo/finalizado/` (referencia)

---

## Antes de comenzar la clase

- [ ] Abrir `demo/finalizado/` en el servidor: `python manage.py runserver`
- [ ] Abrir `demo/inicio/hub/views.py` en el editor (pantalla compartida)
- [ ] Tener el browser listo en `http://127.0.0.1:8000`

---

## Mapa de tiempo

| Bloque | Duración | Qué hacer |
|--------|----------|-----------|
| 1 | 2 min | Mostrar el resultado final |
| 2 | 1 min | Recorrer la estructura del proyecto |
| 3 | 5–7 min | Escribir las views en `inicio/` |
| 4 | 1 min | Revisar las URLs |
| 5 | 1–2 min | Correr el servidor y navegar |

---

## Bloque 1 — Mostrar el resultado (2 min)

Abrir el browser en `http://127.0.0.1:8000` con el proyecto `finalizado/` corriendo.

**Di esto:**
> "Esto es lo que vamos a construir hoy: un hub personal de docente hecho 100% con Python y Django. Dos páginas: la de inicio y la de perfil. Todo el HTML sale desde Python — sin archivos HTML separados todavía."

Navegar en vivo:
1. Página de inicio → señalar el nombre, la materia, las estadísticas
2. Click en "Acerca de mí" → señalar las tarjetas de información
3. "¿Cómo lo hicimos? Vamos al código."

---

## Bloque 2 — Estructura del proyecto (1 min)

Mostrar en el explorador de archivos:

```
demo/inicio/
├── manage.py           ← CLI de Django
├── hub/                ← nuestra aplicación
│   ├── views.py        ← AQUÍ ESCRIBIMOS HOY
│   └── urls.py         ← ya está configurado
└── hub_docente/        ← configuración del proyecto
    ├── settings.py
    └── urls.py
```

**Di esto:**
> "El proyecto tiene dos partes: `hub_docente` es la configuración general, `hub` es nuestra app. Hoy solo tocamos `views.py` — Django ya sabe cómo llegar ahí."

---

## Bloque 3 — Escribir las views (5–7 min)

Abrir `demo/inicio/hub/views.py`. El archivo ya tiene:

```python
from django.http import HttpResponse

nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"

# AQUÍ CONSTRUIMOS EN CLASE
```

### Paso 3a — La función `inicio()` (3 min)

**Di esto:**
> "Una view en Django es simplemente una función de Python. Recibe el `request` del navegador y devuelve una respuesta. Empecemos con la página de inicio."

Escribir en vivo:

```python
def inicio(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{nombre_docente}</title></head>
    <body>
        <h1>Bienvenidos al hub de {nombre_docente}</h1>
        <p>Docente de {materia} en {institucion}</p>
        <p>Años de experiencia: {anos_experiencia}</p>
        <a href="/acerca/">Ver mi perfil</a>
    </body>
    </html>
    """)
```

**Puntos clave a señalar mientras escribes:**
- `HttpResponse(...)` → "Django necesita que devolvamos una respuesta HTTP"
- `f"""..."""` → "El f-string nos permite meter variables de Python dentro del HTML"
- `{nombre_docente}` → "Las llaves conectan nuestras variables con el HTML"

### Paso 3b — La función `acerca()` (2 min)

**Di esto:**
> "La segunda página sigue el mismo patrón exacto: función → HttpResponse → HTML con f-string."

Escribir en vivo:

```python
def acerca(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Acerca — {nombre_docente}</title></head>
    <body>
        <h1>{nombre_docente}</h1>
        <p><strong>Materia:</strong> {materia}</p>
        <p><strong>Institución:</strong> {institucion}</p>
        <p><strong>Experiencia:</strong> {anos_experiencia} años</p>
        <a href="/">← Volver</a>
    </body>
    </html>
    """)
```

**Pregunta al grupo:**
> "¿Alguien nota qué cambió entre `inicio()` y `acerca()`? — Solo el HTML adentro. La estructura es idéntica."

---

## Bloque 4 — Revisar las URLs (1 min)

Abrir `demo/inicio/hub/urls.py` (ya está escrito — solo explicar, no editar):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('',        views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
]
```

**Di esto:**
> "Las URLs ya están conectadas. `path('', views.inicio)` dice: cuando alguien entra a `/`, llama a la función `inicio`. `path('acerca/', views.acerca)` dice: cuando entra a `/acerca/`, llama a `acerca`. Eso es todo el enrutamiento."

Mostrar también `hub_docente/urls.py` brevemente:
> "Y este archivo le dice a Django: para todo lo que empiece con vacío, busca en las URLs de `hub`. Así se conectan los dos niveles."

---

## Bloque 5 — Correr el servidor (1–2 min)

En la terminal, desde `demo/inicio/`:

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000` y navegar entre las dos páginas.

**Di esto:**
> "¿Ven? Django toma nuestra función de Python, la conecta a una URL, y la ejecuta cada vez que el navegador hace una petición. Eso es el corazón de Django: request entra → view procesa → response sale."

**Pregunta de cierre:**
> "Si quiero agregar una tercera página, ¿qué necesito hacer? — Exacto: una función nueva en `views.py` y un `path()` nuevo en `urls.py`. Eso es todo."

---

## Resumen del concepto central

```
Navegador  →  URL  →  urls.py  →  views.py (función)  →  HttpResponse  →  Navegador
```

Las variables al inicio del archivo (`nombre_docente`, `materia`, etc.) son la zona de personalización — en la práctica los estudiantes las cambian primero para ver el efecto inmediato.

---

## Si te sobra tiempo (opcional)

Mostrar el `finalizado/` y señalar cómo el mismo patrón escala:
- Las mismas funciones `inicio()` y `acerca()`
- Solo más HTML y CSS dentro del f-string
- Las variables de personalización hacen que todo cambie de un lugar

> "La arquitectura no cambió — solo el diseño. Eso es lo que les pido que recuerden."
