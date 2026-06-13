# Módulo 4: Modelos y Base de Datos — Datos que Persisten

---

## Diapositiva 1: ¿Por Qué Modelos? De Lista Estática a Base de Datos
- **Conceptos:**
  - Lista hardcodeada en `views.py` → hay que editar código para agregar un recurso
  - Con modelos → el docente agrega recursos desde el panel de administración sin tocar código
  - Django ORM traduce clases Python a tablas SQL automáticamente
- **Fragmento de Código Recomendado:**
```python
# ❌ ANTES (Semana 3): datos estáticos en el código
recursos_lista = [
    {"titulo": "Khan Academy", "url": "https://es.khanacademy.org"},
]

# ✅ AHORA (Semana 4): datos en la base de datos
from .models import Recurso

def recursos_view(request):
    return render(request, 'hub/recursos.html',
                  _ctx({'recursos': Recurso.objects.all()}))
```

---

## Diapositiva 2: Definir un Modelo — Python como Esquema de BD
- **Conceptos:**
  - Cada clase que hereda de `models.Model` → una tabla en la base de datos
  - Cada atributo → una columna con su tipo de dato
  - `auto_now_add=True` → Django guarda la fecha/hora de creación automáticamente
- **Fragmento de Código Recomendado:**
```python
# hub/models.py
from django.db import models

class Recurso(models.Model):
    titulo      = models.CharField(max_length=200)  # texto corto
    url         = models.URLField()                  # valida que sea una URL
    descripcion = models.TextField(blank=True)       # texto largo, opcional
    creado      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']  # más recientes primero

    def __str__(self):
        return self.titulo  # texto en el panel de admin
```

---

## Diapositiva 3: Migraciones — Control de Versiones para tu Base de Datos
- **Conceptos:**
  - **Migración** = archivo que describe qué cambió en los modelos
  - `makemigrations` → detecta cambios y genera el archivo de migración
  - `migrate` → aplica los cambios a la base de datos real
- **Fragmento de Código Recomendado:**
```bash
# Paso 1: Django detecta cambios en models.py y genera el archivo
python manage.py makemigrations
# → Crea: hub/migrations/0001_initial.py

# Paso 2: Django aplica el archivo → crea las tablas en SQLite
python manage.py migrate
# → Applying hub.0001_initial... OK

# Regla de oro:
# Cada vez que cambias models.py → makemigrations + migrate
```

---

## Diapositiva 4: El Panel de Administración de Django — CRUD Gratis
- **Conceptos:**
  - `admin.site.register(Modelo)` → aparece en `/admin/` con Create/Read/Update/Delete
  - `python manage.py createsuperuser` → crea el usuario administrador
  - El admin es funcional desde el primer día; los docentes lo usan para gestionar recursos
- **Fragmento de Código Recomendado:**
```python
# hub/admin.py
from django.contrib import admin
from .models import Recurso, Mensaje

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'url', 'creado')
    search_fields = ('titulo',)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'correo', 'recibido', 'leido')
    list_filter   = ('leido',)
```

---

## Diapositiva 5: El ORM de Django — Consultas sin Escribir SQL
- **Conceptos:**
  - `Recurso.objects.all()` → `SELECT * FROM recurso ORDER BY -creado`
  - `Recurso.objects.filter(...)` → `WHERE`
  - `Recurso.objects.create(...)` → `INSERT INTO`
  - El ORM es seguro contra inyección SQL por defecto
- **Fragmento de Código Recomendado:**
```python
# hub/views.py
from .models import Recurso

def recursos_view(request):
    # Equivale a: SELECT * FROM hub_recurso ORDER BY creado DESC
    todos = Recurso.objects.all()

    # Equivale a: SELECT * FROM hub_recurso WHERE titulo LIKE '%Khan%'
    # busqueda = Recurso.objects.filter(titulo__icontains='Khan')

    return render(request, 'hub/recursos.html', _ctx({'recursos': todos}))
```

---

## Diapositiva 6: Renderizar Datos de BD en la Plantilla
- **Conceptos:**
  - El queryset de Django es iterable en el template igual que una lista Python
  - `{{ forloop.counter }}` numera los ítems automáticamente
  - `{% if recurso.descripcion %}` evita mostrar espacio vacío si el campo es opcional
- **Fragmento de Código Recomendado:**
```html
<!-- templates/hub/recursos.html -->
{% if recursos %}
  <div class="row g-4">
  {% for recurso in recursos %}
    <div class="col-md-4">
      <div class="rec-card">
        <span class="rec-num">{{ forloop.counter }}</span>
        <a href="{{ recurso.url }}" target="_blank">{{ recurso.titulo }}</a>
        {% if recurso.descripcion %}
          <p class="rec-desc">{{ recurso.descripcion }}</p>
        {% endif %}
      </div>
    </div>
  {% endfor %}
  </div>
{% else %}
  <p>Aún no hay recursos disponibles.</p>
{% endif %}
```

---

## Diapositiva 7: Segundo Modelo — `Mensaje` y Campos Especiales
- **Conceptos:**
  - Un mismo `models.py` puede tener múltiples modelos → múltiples tablas
  - `EmailField` valida automáticamente el formato del correo
  - `BooleanField(default=False)` → útil para estados (leído/no leído)
  - `__str__` controla el texto que aparece en el panel de administración
- **Fragmento de Código Recomendado:**
```python
# hub/models.py
class Mensaje(models.Model):
    nombre   = models.CharField(max_length=100)
    correo   = models.EmailField()           # valida formato de email
    mensaje  = models.TextField()
    recibido = models.DateTimeField(auto_now_add=True)
    leido    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-recibido']

    def __str__(self):
        return f"{self.nombre} — {self.recibido.strftime('%d/%m/%Y')}"
```

---

## Diapositiva 8: Demo en Vivo — `models.py`, Migraciones y Admin
- **Conceptos:**
  - Archivo de referencia: `semana_4/demo/finalizado/hub/models.py` y `views.py`
  - La sesión recorre el flujo completo: definir modelo → migrar → registrar en admin → agregar datos → verlos en `/recursos/`
  - La diferencia clave respecto a Semana 3: `Recurso.objects.all()` reemplaza la lista estática
- **Fragmento de Código Recomendado:**
```
Flujo completo de la demo:

1. models.py         → class Recurso(models.Model): ...
                        class Mensaje(models.Model): ...
2. Terminal          → python manage.py makemigrations
                        python manage.py migrate
                        python manage.py createsuperuser
3. admin.py          → @admin.register(Recurso)
4. Navegador         → http://127.0.0.1:8000/admin/
                        Agrega 3 recursos desde el panel
5. views.py          → Recurso.objects.all()
6. Navegador         → http://127.0.0.1:8000/recursos/
                        Los recursos aparecen en la página ✓
```

---

## Diapositiva 9: Trabajo en Clase — Tu Base de Datos en Acción (20 min)
- **Conceptos:**
  - Archivo de trabajo: `semana_4/ejercicio_clase/plantilla/hub/views.py`
  - La vista `recursos_view()` ya consulta la BD — el ejercicio es **ejecutar el flujo** completo
  - **Ejercicio 2:** Correr migraciones en la terminal integrada de VS Code
  - **Ejercicio 3:** Agregar 3 recursos reales de tu materia desde el panel `/admin/`
- **Fragmento de Código Recomendado:**
```bash
# EJERCICIO 2 — Corre los siguientes comandos en la terminal:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# → Ingresa usuario, email y contraseña cuando los pida

python manage.py runserver
# → Ve a http://127.0.0.1:8000/admin/ e inicia sesión
# → En "Recursos" agrega 3 recursos reales para tu materia

# EJERCICIO 3 — Verifica el resultado:
# → Ve a http://127.0.0.1:8000/recursos/
# → ¿Aparecen tus recursos cargados desde el admin?
```

---

## Diapositiva 10: Tarea y Entregables
- **Conceptos:**
  - Archivo de tarea: `semana_4/tarea/plantilla_tarea/hub/views.py`
  - **Tarea 3 (nueva):** Registrar los modelos en `admin.py` con `list_display` útil — esto no estaba en el ejercicio de clase
  - **Tarea 4:** Agregar 5 recursos (2 más que en clase) desde el admin
- **Fragmento de Código Recomendado:**
```python
# TAREA 3 — Completa hub/admin.py
from django.contrib import admin
from .models import Recurso, Mensaje

# Registra Recurso con list_display que muestre titulo, url y creado
# Registra Mensaje con list_display que muestre nombre, correo y leido

# ──────────────────────────────────────────────────
# ENTREGA:
#   • admin.py completado con @admin.register(Recurso) y Mensaje
#   • Captura de pantalla del admin con tus 5 recursos cargados
#   • /recursos/ mostrando los datos reales en el navegador

# CRITERIO:
#   admin.py registra Recurso con list_display útil
#   (titulo, url, creado como mínimo)
```
