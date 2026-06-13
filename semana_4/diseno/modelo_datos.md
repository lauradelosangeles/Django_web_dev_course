# Diseño del Modelo de Datos — Semana 4

> Antes de ejecutar `makemigrations`, define en papel (o aquí) qué tablas necesitas
> y qué columnas tendrá cada una. Este documento es la referencia que justifica cada
> campo en `models.py`.

---

## Tabla: `hub_recurso` (modelo `Recurso`)

| Campo | Tipo de dato Django | Clave | Notas |
|-------|---------------------|-------|-------|
| `id` | `BigAutoField` (automático) | PK | Django lo genera; no se escribe en `models.py` |
| `titulo` | `CharField(max_length=200)` | — | Nombre del recurso educativo |
| `url` | `URLField()` | — | Dirección web; Django valida el formato |
| `descripcion` | `TextField(blank=True)` | — | Texto largo, opcional |
| `creado` | `DateTimeField(auto_now_add=True)` | — | Fecha/hora de creación, automática |

---

## Tabla: `hub_mensaje` (modelo `Mensaje`)

| Campo | Tipo de dato Django | Clave | Notas |
|-------|---------------------|-------|-------|
| `id` | `BigAutoField` (automático) | PK | Django lo genera |
| `nombre` | `CharField(max_length=100)` | — | Nombre del remitente |
| `correo` | `EmailField()` | — | Django valida el formato de correo |
| `mensaje` | `TextField()` | — | Texto del mensaje; obligatorio |
| `recibido` | `DateTimeField(auto_now_add=True)` | — | Fecha/hora de recepción, automática |
| `leido` | `BooleanField(default=False)` | — | El docente lo marca como leído en el admin |

---

## Relación entre tablas

En esta versión del Hub, `Recurso` y `Mensaje` son independientes — no hay clave
foránea entre ellos.

**Relación futura (opcional):**  
Si en el futuro un docente quiere adjuntar un recurso específico a un mensaje, se
podría agregar un campo `ForeignKey`:

```
Mensaje ──< Recurso
(un mensaje puede referenciar un recurso)
```

Esto se implementaría con:
```python
recurso = models.ForeignKey(Recurso, null=True, blank=True, on_delete=models.SET_NULL)
```

---

## Diagrama E/R (dibuja aquí o adjunta imagen)

```
┌─────────────────────┐         ┌──────────────────────┐
│       RECURSO       │         │       MENSAJE        │
├─────────────────────┤         ├──────────────────────┤
│ PK  id              │         │ PK  id               │
│     titulo          │         │     nombre           │
│     url             │         │     correo           │
│     descripcion     │         │     mensaje          │
│     creado          │         │     recibido         │
└─────────────────────┘         │     leido            │
                                └──────────────────────┘
```

> **Instrucción:** Dibuja este diagrama en papel o en draw.io/Excalidraw y guarda
> la imagen como `diagrama_er.png` en esta misma carpeta.

---

## Flujo completo

```
models.py  →  makemigrations  →  migrate  →  admin.py  →  /admin/  →  vista ORM
```

Cada vez que cambies `models.py`, debes repetir los dos comandos de migración.
