# Semana 4: Diseño de Bases de Datos, Modelos y Panel de Administración

> El ORM de Django traduce clases Python en tablas SQLite.
> El Panel de Admin genera una interfaz web para gestionar recursos y mensajes sin escribir formularios extra.

## Objetivo de Aprendizaje

Al finalizar esta semana podrás **definir modelos Django** que representan tablas de base de datos, registrarlos en el Panel de Administración y consultar datos desde las vistas usando el ORM de Django.

---

## El concepto

Hasta ahora los datos desaparecían al reiniciar el servidor. **SQLite** guarda todo en `db.sqlite3` sin instalar otro programa. Defines clases en `models.py` (`Recurso`, `Mensaje`); Django crea tablas y consultas con `objects.all()` o `objects.filter()`.

**Analogía:** el modelo es el encabezado de la planilla; una migración es imprimir una versión nueva con columnas actualizadas; el admin es un formulario conectado a la base de datos.

## En el Hub Personal del Docente

- **`Recurso`:** título, URL, descripción y fecha — lo que muestra `/recursos/`.
- **`Mensaje`:** contactos recibidos (se usarán con formulario POST en semana 5).

Las vistas dejan las listas fijas y leen `Recurso.objects.all()` desde la base de datos.

---

## Actividades de la semana

| Actividad | Carpeta | Tema | Descripción |
|-----------|---------|------|-------------|
| **Demo** | `demo/inicio/` → `demo/finalizado/` | Modelos, migraciones y Panel Admin | Partes de la semana 3 (plantillas listas) con `models.py` vacío. En vivo defines `Recurso` y `Mensaje`, ejecutas `makemigrations` + `migrate`, creas superusuario, registras modelos en `admin.py` y conectas `recursos_view()` al ORM. |
| **Actividad en clase** | `ejercicio_clase/plantilla/` | Modelo `Recurso` y datos reales | Personalizas el Hub, defines el modelo `Recurso` en `models.py`, corres migraciones, cargas al menos 3 recursos desde `/admin/` y verificas que `/recursos/` los muestra. Entrega: captura del admin + página funcionando. |
| **Tarea** | `tarea/plantilla_tarea/` | Modelo `Mensaje` | `Recurso` ya está definido; creas el modelo `Mensaje` desde cero, lo registras en el admin, migras la BD y cargas 5 recursos reales de tu materia. Refuerzas el flujo completo modelo → admin → vista. |
| **Diseño del modelo de datos** | `diseno/` | Modelo E/R e historias de usuario | Antes de programar, documentas las tablas `Recurso` y `Mensaje` en `modelo_datos.md` (campos, tipos, claves) y escribes 3 historias de usuario en `historias_usuario.md` para que cada funcionalidad esté centrada en las necesidades del docente. |
| **Prueba unitaria** | `demo/finalizado/hub/tests.py` | TDD básico con TestCase | Ejecutas `python manage.py test` en `semana_4/demo/finalizado/` y verificas que las 2 pruebas pasan: creación de un `Recurso` y que `__str__` devuelve el título. El archivo de tarea incluye un TODO para que el docente escriba el test de `Mensaje`. |

---

## Fuente de Verdad de Cada Archivo

| Archivo | Responsabilidad |
|---------|----------------|
| `hub/models.py` | **Archivo principal esta semana**: tablas como clases Python |
| `hub/admin.py` | Registra modelos en `/admin/` |
| `hub/migrations/` | Generados con `makemigrations` |
| `hub/views.py` | Consulta la BD con el ORM |

---

## Modelos del curso (referencia)

```python
class Recurso(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    recibido = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
```

---

## Teoría

| Concepto | Qué hace | Analogía docente |
|----------|----------|------------------|
| Campo (`CharField`, etc.) | Tipo de columna | Formato de celda en planilla |
| Migración | Aplica cambios del modelo a la BD | Nueva versión impresa de la planilla |
| QuerySet | Registros devueltos por una consulta | Filas que cumplen un criterio |
| `objects.all()` | Todos los registros | “Toda la planilla” |
| `objects.filter(...)` | Registros filtrados | “Solo 3er año” |

### ORM vs. SQL manual

| SQL manual | ORM Django |
|------------|------------|
| `CREATE TABLE ...` | `class Mensaje(models.Model):` |
| `INSERT INTO ...` | `Mensaje.objects.create(...)` |
| `SELECT * FROM ...` | `Mensaje.objects.all()` |

### Sintaxis esencial

| Comando / código | Cuándo usarlo |
|------------------|---------------|
| `python manage.py makemigrations` | Tras cambiar `models.py` |
| `python manage.py migrate` | Siempre después de `makemigrations` |
| `python manage.py createsuperuser` | Una vez, para entrar a `/admin/` |
| `@admin.register(Modelo)` | Mostrar modelo en el panel |

---

## Comandos Clave

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Panel: http://127.0.0.1:8000/admin/
```

---

## Errores comunes

1. **Olvidar migrar** — sin `makemigrations` + `migrate`, la BD no tiene las tablas nuevas.
2. **`no such table`** — ejecuta `migrate` en proyectos recién clonados.
3. **Modelo invisible en admin** — falta registrarlo en `admin.py`.
4. **Lista vacía en la vista** — crea registros de prueba en `/admin/` antes de probar plantillas.

---

## Glosario

- **ORM:** traduce Python ↔ tablas sin escribir SQL a mano.
- **Migración:** script que actualiza la estructura de la BD.
- **QuerySet:** conjunto de objetos devueltos por una consulta.

---

## Siguiente semana

El admin gestiona datos por dentro; falta que el visitante envíe mensajes desde el formulario público de contacto (POST + CSRF) y publicar el Hub en PythonAnywhere.

---

## Prompts de Cursor AI para Esta Semana

**Prompt 1 — Crear un modelo:**
> "Crea un modelo Django llamado `Recurso` en models.py con los campos: titulo (CharField, máximo 200 caracteres), url (URLField), descripcion (TextField, puede estar vacío) y creado (DateTimeField con auto_now_add=True). Agrega Meta con ordering por '-creado' y un __str__ que devuelva el título."

**Prompt 2 — Registrar en el admin:**
> "En admin.py, registra el modelo Recurso usando @admin.register. Configura ModelAdmin con titulo, url y creado en list_display, y búsqueda por titulo."

**Prompt 3 — Usar el ORM en la vista:**
> "Modifica recursos_view en views.py para usar Recurso.objects.all() en lugar de una lista fija."

**Prompt 4 — Filtrar en el admin:**
> "En MensajeAdmin, agrega list_filter por 'leido' y list_editable = ['leido'] para marcar mensajes como leídos desde la lista."

**Prompt 5 — Prueba unitaria con TestCase:**
> "Crea un test de Django que verifique que al crear un Recurso, objects.count() aumenta en 1 y que str(recurso) devuelve su título."
