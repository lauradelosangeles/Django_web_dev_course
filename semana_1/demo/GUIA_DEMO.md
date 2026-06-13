# Guía de Demo — Semana 1
**`inicio/docente.py` → `finalizado/docente.py`**
Tiempo: 15–20 minutos.

---

## Preparación previa

- Cursor abierto en `inicio/docente.py`
- `inicio/perfil.html` abierto en el navegador
- Terminal lista en la carpeta `inicio/`

---

## PASO 1 — El problema (2 min)

Señala las variables sueltas al inicio del archivo:

```python
nombre      = "Prof. González Silva"
materia     = "Matemáticas"
institucion = "Colegio Simón Bolívar"
experiencia = 10
```

> "Esto funciona para un docente. ¿Para diez? Copiamos y pegamos diez veces. Si el colegio cambia de nombre, lo buscamos en diez lugares. Una clase resuelve eso."

---

## PASO 2 — Completar `__init__` en vivo (6 min)

El método ya existe con `pass`. Reemplázalo:

```python
def __init__(self, nombre, materia, institucion, anos_experiencia, materias=None):
    self.nombre           = nombre
    self.materia          = materia
    self.institucion      = institucion
    self.anos_experiencia = anos_experiencia
    self.materias         = materias or []
```

**Explica mientras escribes — una sola frase por línea:**
- `self.nombre = nombre` → el dato de entrada se guarda como dato del objeto
- `materias or []` → si no pasan lista, usamos lista vacía en lugar de `None`

---

## PASO 3 — Completar `presentarse` en vivo (3 min)

```python
def presentarse(self):
    print(f"Hola, soy {self.nombre}.")
    print(f"Enseño {self.materia} en {self.institucion}.")
    print(f"Tengo {self.anos_experiencia} años de experiencia.")
```

> "Un método es una función que usa los datos del objeto. `self` es cómo accede a ellos."

---

## PASO 4 — Descomentar y ejecutar (3 min)

Descomenta el bloque de uso al final del archivo:

```python
docente_1 = Docente(
    "Prof. González Silva", "Matemáticas", "C. Simón Bolívar", 10,
    materias=["Álgebra — 8° grado", "Geometría — 9°", "Precálculo — 10°"],
)
docente_2 = Docente("Prof. Rodríguez", "Historia", "Liceo Central", 5)
docente_1.presentarse()
docente_2.presentarse()
```

En la terminal:
```
python docente.py
```

> "Dos objetos del mismo molde, con datos distintos. Sin duplicar código."

---

## PASO 5 — Puente hacia Django (2 min)

Cambia al navegador con `perfil.html`. Señala el nombre en el hero.

> "Ese nombre está escrito a mano en el HTML. En Django, vendría de la base de datos y aparecería así:"

Muestra el comentario que ya está en el HTML:
```html
<!-- En Django: <h1>{{ nombre_docente }}</h1> -->
```

> "La clase `Docente` que acabamos de construir se convierte en un modelo Django. En lugar de `print(self.nombre)`, Django inyecta ese dato directo en la página. Eso es lo que veremos en las próximas semanas."

---

## Si sobra tiempo (~3 min)

Agrega `describir_materias()` en vivo y llámalo con `docente_1`:

```python
def describir_materias(self):
    if not self.materias:
        print("Aún no hay materias registradas.")
        return
    print(f"Materias de {self.nombre}:")
    for i, m in enumerate(self.materias, start=1):
        print(f"  {i}. {m}")
```

> "Anticipa el `{% for materia in materias %}` que escribiremos en Semana 3."

---

## Errores frecuentes

| Síntoma | Causa | Solución rápida |
|---|---|---|
| `TypeError: missing argument` | Falta un parámetro requerido | Leer el error — Python dice exactamente cuál |
| `AttributeError` con `None` | Faltó el `or []` en materias | Agregar `or []` en `__init__` |
| `IndentationError` | Mezcla de tabs y espacios | Cursor → View → Render Whitespace |
