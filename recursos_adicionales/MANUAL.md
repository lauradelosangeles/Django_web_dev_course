# Manual Técnico y de Usuario — Hub Personal del Docente

> Este manual documenta los requisitos, la instalación, la estructura del proyecto
> y el uso básico del Hub Personal del Docente desarrollado en el curso de 5 semanas
> "Desarrollo Web con Python y Django".

---

## 1. Requisitos del sistema

| Componente | Versión mínima | Notas |
|------------|---------------|-------|
| Python | 3.10 | Descarga desde python.org |
| Django | 4.2 | Se instala con pip |
| SQLite | Incluido en Python | No requiere instalación separada |
| Navegador moderno | Chrome 90+ / Firefox 88+ / Edge 90+ | Para usar la interfaz web |
| Git | 2.30+ | Para control de versiones |

---

## 2. Instalación paso a paso

### 2.1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd curso_django_profesores
```

### 2.2. Navegar a la carpeta de la semana a usar

```bash
# Ejemplo: semana 5 (versión completa)
cd semana_5/demo/finalizado
```

### 2.3. Crear y activar el entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2.4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2.5. Configurar variables de entorno

```bash
# Windows
copy .env.ejemplo .env

# macOS / Linux
cp .env.ejemplo .env
```

Abre `.env` y ajusta los valores:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

> **Importante:** Nunca subas el archivo `.env` al repositorio. Está en `.gitignore`.

### 2.6. Aplicar migraciones y crear superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 2.7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador.

---

## 3. Estructura de carpetas del proyecto

```
semana_5/demo/finalizado/
├── hub/                        ← Aplicación principal Django
│   ├── models.py               ← Modelos Recurso y Mensaje
│   ├── views.py                ← Vistas (inicio, acerca, recursos, contacto)
│   ├── urls.py                 ← Rutas de la app
│   ├── forms.py                ← ContactoForm
│   ├── admin.py                ← Registro en el Panel de Administración
│   └── migrations/             ← Historial de cambios de la BD
├── hub_docente/                ← Configuración del proyecto Django
│   ├── settings.py             ← Ajustes: BD, apps, plantillas, estáticos
│   ├── urls.py                 ← Enrutador principal
│   └── wsgi.py                 ← Entrada para servidor de producción
├── templates/                  ← Plantillas HTML
│   ├── base.html               ← Estructura compartida (nav, footer)
│   └── hub/
│       ├── inicio.html
│       ├── acerca.html
│       ├── recursos.html
│       └── contacto.html
├── static/css/estilos.css      ← Estilos personalizados
├── .env.ejemplo                ← Plantilla de variables de entorno
├── requirements.txt            ← Dependencias del proyecto
└── manage.py                   ← Utilidad de línea de comandos Django
```

---

## 4. Mantenimiento

### Agregar un nuevo recurso educativo

1. Ve a `http://127.0.0.1:8000/admin/`
2. Inicia sesión con el superusuario.
3. Haz clic en **Recursos → Agregar recurso**.
4. Llena título, URL y descripción, luego guarda.
5. El recurso aparece inmediatamente en `/recursos/`.

### Ver mensajes de contacto recibidos

1. Ve a `http://127.0.0.1:8000/admin/hub/mensaje/`
2. Los mensajes no leídos aparecen con `leido = False`.
3. Puedes marcarlos como leídos desde la lista.

### Actualizar dependencias

```bash
pip install --upgrade -r requirements.txt
```

### Respaldar la base de datos

```bash
# Copia manual del archivo SQLite
cp db.sqlite3 db_backup_$(date +%Y%m%d).sqlite3
```

### Preparar para producción (PythonAnywhere)

```bash
python manage.py collectstatic
```

Configura `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ["tuusuario.pythonanywhere.com"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

## 5. Guía de usuario del Hub

### Página de Inicio (`/`)
Muestra la bienvenida con el nombre y materia del docente, y una frase de misión
educativa. Usa los enlaces de la barra de navegación para explorar el sitio.

### Página Acerca (`/acerca/`)
Presenta la presentación del docente: institución, años de experiencia y materia.

### Página Recursos (`/recursos/`)
Lista los materiales educativos publicados por el docente.
- Haz clic en el título de cada recurso para abrir el enlace en una nueva pestaña.
- Los recursos más recientes aparecen primero.

### Formulario de Contacto (`/contacto/`)
Permite enviar un mensaje directo al docente.
1. Llena los campos: nombre, correo electrónico y mensaje.
2. Haz clic en "Enviar mensaje".
3. Si los datos son correctos, aparecerá el mensaje de confirmación "¡Mensaje recibido!".
4. Si hay algún error (p. ej., correo inválido), el campo correspondiente mostrará
   la indicación de corrección.

### Panel de Administración (`/admin/`)
Solo para el docente. Permite gestionar recursos y ver mensajes recibidos.
Requiere las credenciales del superusuario creado durante la instalación.

---

## 6. Solución de problemas frecuentes

| Problema | Causa probable | Solución |
|----------|---------------|----------|
| `no such table` | Migraciones no aplicadas | `python manage.py migrate` |
| Error 403 al enviar formulario | Falta `{% csrf_token %}` en plantilla | Verifica el template de contacto |
| CSS no carga en producción | Falta `collectstatic` | `python manage.py collectstatic` |
| `DisallowedHost` | Dominio no está en `ALLOWED_HOSTS` | Agrega el dominio en `settings.py` |
| `SECRET_KEY` expuesta | `.env` no existe o está en el repositorio | Crea `.env` desde `.env.ejemplo` |
