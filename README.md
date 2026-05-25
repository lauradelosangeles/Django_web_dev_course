# Desarrollo Web con Python y Django — Hub Personal del Docente

Curso de 5 semanas para docentes. Cada semana construyes una pieza del **Hub Personal del Docente**: un sitio web real donde compartes recursos con tus estudiantes, recibes mensajes y administras todo desde el Panel de Administración de Django.

---

## ¿Qué Vas a Construir?

Una aplicación web con Django que incluye:
- Página de inicio donde te presentas y describes tus cursos
- Página de recursos con enlaces y materiales para estudiantes
- Formulario de contacto para recibir mensajes
- Panel de administración para gestionar todo el contenido

---

## Herramientas del Curso

| Herramienta | Uso en el curso |
|-------------|----------------|
| **Python 3.10+** | Lenguaje base |
| **Django 4.2** | Framework web completo con patrón MVT |
| **SQLite** | Base de datos integrada en Django |
| **Bootstrap 5** | Diseño profesional sin escribir CSS desde cero |
| **Cursor AI** | Editor con IA para escribir y entender código |

---

## Estructura del Curso por Semana

| Semana | Tema | Habilidad principal |
|--------|------|---------------------|
| Semana 1 | HTML y Python | Entender la web y las bases del lenguaje |
| Semana 2 | Django y Rutas | Instalar Django y crear tu primer servidor |
| Semana 3 | Plantillas Dinámicas | Separar HTML de Python con el motor de plantillas |
| Semana 4 | Modelos y Admin | Guardar datos y administrarlos visualmente |
| Semana 5 | Formularios y Despliegue | Recibir mensajes y publicar el sitio en internet |

---

## Anatomía de Cada Semana

```
semana_X/
├── README.md                  ← Objetivos, conceptos y prompts para Cursor
├── demo/
│   ├── inicio/                ← Código al INICIO de la clase (el profesor parte de aquí)
│   └── finalizado/            ← Código TERMINADO después de la demo en vivo
├── ejercicio_clase/
│   └── plantilla/             ← Plantilla con guías [Ctrl+K] para el ejercicio en clase
└── tarea/
    └── plantilla_tarea/       ← Punto de partida para el trabajo en casa
```

---

## Actividades por semana

Cada semana sigue el mismo esquema: **Demo** (profesor en vivo, `demo/inicio` → `demo/finalizado`), **Actividad en clase** (`ejercicio_clase/plantilla/`) y **Tarea** (`tarea/plantilla_tarea/`). Detalle completo en el `README.md` de cada semana.

| Semana | Actividad | Tema | Descripción |
|--------|-----------|------|-------------|
| **1** | Demo | HTML y clase `Docente` | Construcción en vivo de `perfil.html` y `docente.py` desde HTML vacío. |
| **1** | Actividad en clase | `presentarse()` | Completar `ejercicio.html` y método `presentarse()` en la clase `Docente`. |
| **1** | Tarea | Docente ampliado | Método `describir_materias()`, segunda instancia y entrega `tarea.py` + `tarea.html`. |
| **2** | Demo | Django y rutas | Vistas `inicio()` y `acerca()` con `HttpResponse` y servidor local. |
| **2** | Actividad en clase | Vista `acerca()` | Crear la página Acerca con ruta propia (inicio ya dado). |
| **2** | Tarea | Tercera ruta | Añadir una vista y URL adicional a elección del docente. |
| **3** | Demo | Plantillas y `render()` | `base.html` con Bootstrap, herencia y refactor desde `HttpResponse`. |
| **3** | Actividad en clase | Plantillas dinámicas | Convertir `acerca()` y crear `recursos_view()` con contexto. |
| **3** | Tarea | Recursos propios | Lista de recursos reales y página `/recursos/` completa. |
| **4** | Demo | Modelos y admin | `Recurso`, `Mensaje`, migraciones y Panel de Administración. |
| **4** | Actividad en clase | Modelo `Recurso` | Definir modelo, migrar y cargar 3 recursos desde `/admin/`. |
| **4** | Tarea | Modelo `Mensaje` | Definir `Mensaje`, registrar en admin y cargar 5 recursos. |
| **5** | Demo | POST, CSRF y `.env` | Formulario de contacto, validación y configuración de producción. |
| **5** | Actividad en clase | Vista `contacto()` | Completar guardado de mensajes con `ContactoForm`. |
| **5** | Tarea | PythonAnywhere | Publicar el Hub con URL pública en internet. |

---

## Instalación Rápida

```bash
# 1. Instalar Python 3.10+ desde python.org
# 2. Instalar dependencias del curso
pip install -r requirements.txt
# 3. Para semanas 2-5, navegar a la carpeta del proyecto y ejecutar:
python manage.py runserver
# 4. Abrir el navegador en: http://127.0.0.1:8000
```

---

## Guía de Despliegue en PythonAnywhere

### Requisitos previos
- Cuenta gratuita en [pythonanywhere.com](https://www.pythonanywhere.com)
- El proyecto subido al servidor (ver opciones abajo)
- Usuario de ejemplo: `tuusuario` → URL final: `tuusuario.pythonanywhere.com`

---

### Paso 1 — Subir el proyecto al servidor

**Opción A — Desde GitHub (recomendada)**

En la consola **Bash** de PythonAnywhere:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
```

**Opción B — Subida manual**

Pestaña **Files** → crear carpetas → subir cada archivo individualmente.

> ⚠️ Nunca subas `.env` ni `db.sqlite3` — se crean directamente en el servidor.

---

### Paso 2 — Instalar dependencias

```bash
cd /home/tuusuario/tu-repo/semana_5/demo/finalizado
pip3.10 install --user -r requirements.txt
```

---

### Paso 3 — Crear el archivo `.env`

```bash
cp .env.ejemplo .env
nano .env
```

Contenido del `.env` con tus valores reales:

```env
SECRET_KEY=pegar-aqui-la-clave-generada-con-python
DEBUG=False
ALLOWED_HOSTS=tuusuario.pythonanywhere.com,localhost,127.0.0.1
```

Para generar la `SECRET_KEY`:
```bash
python3.10 -c "import secrets; print(secrets.token_hex(32))"
```

Guardar en nano: `Ctrl+O` → `Enter` → `Ctrl+X`

---

### Paso 4 — Crear la base de datos

```bash
# Crear los archivos de migración de la app hub
python3.10 manage.py makemigrations hub

# Aplicar todas las migraciones (crea las tablas en db.sqlite3)
python3.10 manage.py migrate

# Crear el superusuario para /admin/
python3.10 manage.py createsuperuser
```

---

### Paso 5 — Recolectar archivos estáticos

```bash
python3.10 manage.py collectstatic --noinput
```

Los archivos CSS/JS quedan en la carpeta `staticfiles/`.

---

### Paso 6 — Configurar el Web App

1. Pestaña **Web** → **Add a new web app**
2. Seleccionar **Manual configuration** → **Python 3.10**
3. En la sección **Code**, apuntar el campo **Source code** a:
   ```
   /home/tuusuario/tu-repo/semana_5/demo/finalizado
   ```

---

### Paso 7 — Configurar el archivo WSGI

Clic en el link del archivo WSGI (`/var/www/tuusuario_pythonanywhere_com_wsgi.py`) y reemplazar **todo** el contenido con:

```python
import sys
import os
from dotenv import load_dotenv

path = '/home/tuusuario/tu-repo/semana_5/demo/finalizado'
if path not in sys.path:
    sys.path.insert(0, path)

# Ruta absoluta al .env — necesario porque uWSGI no arranca desde la carpeta del proyecto
load_dotenv(os.path.join(path, '.env'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'hub_docente.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

> ⚠️ **Importante:** el `path` debe apuntar a la carpeta que **contiene** la carpeta `hub_docente/` (donde está `manage.py`), no a `hub_docente/` misma.

---

### Paso 8 — Configurar archivos estáticos

En la pestaña **Web** → sección **Static files**:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/tuusuario/tu-repo/semana_5/demo/finalizado/staticfiles` |

---

### Paso 9 — Recargar y probar

Clic en el botón **Reload** → abrir `tuusuario.pythonanywhere.com` en el navegador.

---

### Dónde ver los logs

| Log | Contenido |
|-----|-----------|
| **Server log** | Arranques y reinicios de uWSGI |
| **Error log** | Errores de Python/Django — **aquí está el error real** |
| **Access log** | Peticiones HTTP recibidas |

En Bash:
```bash
tail -50 /var/log/tuusuario.pythonanywhere.com.error.log
```

---

## Errores Comunes en el Despliegue

### ❌ Error 1: `ModuleNotFoundError: No module named 'hub_docente'`

**Síntoma en el error log:**
```
ModuleNotFoundError: No module named 'hub_docente'
File "/var/www/tuusuario_pythonanywhere_com_wsgi.py", line 11, in <module>
    application = get_wsgi_application()
```

**Causa A — El `path` en el WSGI apunta a la carpeta incorrecta:**
```python
# ❌ Incorrecto — apunta DENTRO del paquete
path = '/home/tuusuario/repo/semana_5/demo/finalizado/hub_docente'

# ✅ Correcto — apunta donde está manage.py
path = '/home/tuusuario/repo/semana_5/demo/finalizado'
```

**Causa B — Falta la línea `application` al final del WSGI:**
```python
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()   # ← esta línea no debe faltar
```

**Solución:** Editar el archivo WSGI en la interfaz web de PythonAnywhere, corregir el `path` y verificar que `application = get_wsgi_application()` está presente. Luego hacer **Reload**.

---

### ❌ Error 2: `DisallowedHost` — Invalid HTTP_HOST header

**Síntoma en el error log:**
```
django.core.exceptions.DisallowedHost: Invalid HTTP_HOST header:
'tuusuario.pythonanywhere.com'. You may need to add
'tuusuario.pythonanywhere.com' to ALLOWED_HOSTS.
```

**Causa A — El `.env` tiene el placeholder sin reemplazar:**
```env
# ❌ Sin cambiar
ALLOWED_HOSTS=tunombre.pythonanywhere.com,localhost,127.0.0.1

# ✅ Con el usuario real
ALLOWED_HOSTS=tuusuario.pythonanywhere.com,localhost,127.0.0.1
```

**Causa B — `load_dotenv()` no encuentra el `.env` bajo uWSGI:**

uWSGI arranca desde `/home/tuusuario/`, no desde la carpeta del proyecto. `load_dotenv()` sin argumentos busca el `.env` en el directorio de trabajo actual y no lo encuentra.

**Solución:** Usar ruta absoluta en el WSGI (ya incluida en la plantilla del Paso 7):
```python
load_dotenv(os.path.join(path, '.env'))
```

---

### ❌ Error 3: `OperationalError: no such table: hub_recurso`

**Síntoma en el error log:**
```
django.db.utils.OperationalError: no such table: hub_recurso
```

**Causa:** La base de datos existe pero no tiene las tablas de la app `hub` porque `migrate` no se ejecutó en el servidor, o los archivos de migración no existían.

**Solución:**
```bash
cd /home/tuusuario/tu-repo/semana_5/demo/finalizado

# Si los archivos de migración no existen aún:
python3.10 manage.py makemigrations hub

# Crear las tablas:
python3.10 manage.py migrate
```

> El archivo `db.sqlite3` local **no se sube a git** — la base de datos del servidor empieza vacía y debe inicializarse con `migrate`.

---

### ❌ Error 4: `migrate` no crea las tablas de `hub`

**Síntoma en la consola:**
```
Running migrations:
  No migrations to apply.
  Your models in app(s): 'hub' have changes that are not yet reflected
  in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then
  re-run 'manage.py migrate' to apply them.
```

**Causa:** La carpeta `hub/migrations/` solo tiene `__init__.py` — nunca se generaron los archivos de migración de la app.

**Solución:**
```bash
python3.10 manage.py makemigrations hub
python3.10 manage.py migrate
```

---

### ❌ Error 5: CSS no carga en producción

**Síntoma:** La página carga pero sin estilos.

**Causa:** Con `DEBUG=False`, Django no sirve archivos estáticos. Hay que configurarlos en PythonAnywhere.

**Solución:**
```bash
python3.10 manage.py collectstatic --noinput
```
Y configurar en **Web → Static files**:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/tuusuario/tu-repo/semana_5/demo/finalizado/staticfiles` |

---

### ❌ Error 6: Error 403 en el formulario de contacto

**Síntoma:** El formulario lanza error 403 al enviarse.

**Causa:** Falta `{% csrf_token %}` dentro del `<form method="post">`.

**Solución:** Agregar en la plantilla:
```html
<form method="post">
    {% csrf_token %}
    ...
</form>
```

