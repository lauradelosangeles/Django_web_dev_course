# ============================================================
# SEMANA 1 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa las variables con tu información
# EJERCICIO 2 → Agrega el método presentarse() a la clase
# ============================================================


# ── EJERCICIO 1: Completa las variables ─────────────────────
nombre      = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia     = ""    # Tu materia. Ej: "Ciencias Naturales"
institucion = ""    # Tu institución
anos        = 0     # Años de experiencia
materias    = []    # Lista de asignaturas. Ej: ["Biología — 9° grado", "Química — 10°"]


# ── La clase ya tiene __init__ — solo falta presentarse() ───
class Docente:

    def __init__(self, nombre, materia, institucion, anos_experiencia, materias=None):
        self.nombre           = nombre
        self.materia          = materia
        self.institucion      = institucion
        self.anos_experiencia = anos_experiencia
        self.materias         = materias or []    # ← en S3: {% for m in materias %}

    # ============================================================
    # EJERCICIO 2 — Agrega el método presentarse()
    #
    # El método debe imprimir:
    #   "Hola, soy [nombre]."
    #   "Enseño [materia] en [institucion]."
    #   "Tengo [años] años de experiencia."
    #
    # Prompt Cursor (Ctrl+K):
    #   "Agrega un método presentarse(self) a esta clase
    #    que imprima tres líneas con los atributos del docente."
    # ============================================================

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        print(f"Enseño {self.materia} en {self.institucion}.")
        print(f"Tengo {self.anos_experiencia} años de experiencia.")


# Prueba tu clase con tus datos reales
mi_docente = Docente(
    nombre=nombre,
    materia=materia,
    institucion=institucion,
    anos_experiencia=anos,
    materias=materias,
)

mi_docente.presentarse()


# ── Puente hacia Django (Semanas 2–5) ───────────────────────────────────
# AHORA (Python puro):                    PRÓXIMA SEMANA Y SIGUIENTES:
# ─────────────────────────────────────────────────────────────────────────
# mi_docente = Docente("García", ...)  →  [S2] Django + URLs: /perfil/, /acerca/
# mi_docente.presentarse()             →  [S2] return render(request, 'perfil.html',
#                                                    {'docente': mi_docente})
# self.materias = ["Álgebra", ...]     →  [S3] {% for materia in materias %}
#                                                <article>{{ materia }}</article>
#                                            {% endfor %}
# class Docente:                       →  [S4] class Docente(models.Model):
#     self.nombre = nombre             →           nombre = models.CharField(...)
#
# Django inyecta en el HTML: <h1>{{ docente.nombre }}</h1>
