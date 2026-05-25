# ============================================================
# SEMANA 1 — FINALIZADO: Clase Docente completa
# Ejecutar: python docente.py
# ============================================================


class Docente:
    """Representa a un docente con su información pública."""

    # __init__ se ejecuta automáticamente al crear un objeto.
    # 'self' es la referencia al objeto que se está creando.
    def __init__(self, nombre, materia, institucion, anos_experiencia, materias=None):
        self.nombre           = nombre            # atributo de instancia
        self.materia          = materia
        self.institucion      = institucion
        self.anos_experiencia = anos_experiencia
        self.materias         = materias or []    # lista de asignaturas que dicta

    # Un método es una función que "pertenece" al objeto.
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        print(f"Enseño {self.materia} en {self.institucion}.")
        print(f"Tengo {self.anos_experiencia} años de experiencia.")

    # Imprime cada materia numerada — anticipa {% for materia in materias %} en Django.
    def describir_materias(self):
        if not self.materias:
            print("Aún no hay materias registradas.")
            return
        print(f"Materias de {self.nombre}:")
        for i, m in enumerate(self.materias, start=1):
            print(f"  {i}. {m}")

    # Bonus: genera el bloque <header> de perfil.html con los datos del docente.
    # Anticipa lo que Django hace automáticamente: <h1>{{ docente.nombre }}</h1>
    def generar_html(self):
        return (
            f"<header>\n"
            f"    <h1>{self.nombre}</h1>\n"
            f"    <p>Docente de {self.materia} · {self.institucion}</p>\n"
            f"</header>"
        )


# ── Uso: un objeto por docente, sin duplicar código ─────────
docente_1 = Docente(
    "Prof. González Silva", "Matemáticas", "Colegio Dolores Sucre", 10,
    materias=["Álgebra — 8° grado", "Geometría — 9° grado", "Precálculo — 10° grado"],
)
docente_2 = Docente(
    "Prof. Rodríguez", "Historia", "Colegio Dolores Sucre", 5,
    materias=["Historia Universal — 10° grado", "Historia de América — 11° grado"],
)

docente_1.presentarse()
print()
docente_1.describir_materias()
print()
docente_2.presentarse()

# ── Puente hacia Django (Semanas 2–5) ────────────────────────────────────
# AHORA (Python puro)                     → DJANGO (Semanas 2–5)
# ─────────────────────────────────────────────────────────────────────────
# class Docente:                          → class Docente(models.Model):      [S4]
#     self.nombre = nombre                →     nombre = models.CharField(...)
#     self.materia = materia              →     materia = models.CharField(...)
#     self.anos_experiencia = anos        →     anos_experiencia = models.IntegerField()
#     self.materias = ["Álgebra", ...]    →     (modelo Materia con ForeignKey)
#
# docente_1.presentarse()                 → return render(request,             [S2]
#                                               'hub/inicio.html',
#                                               {'docente': docente_1})
#
# docente_1.describir_materias()          → {% for materia in materias %}      [S3]
#                                               <article>{{ materia }}</article>
#                                           {% endfor %}
#
# Docente("García", ...)                  → Docente.objects.get(id=1)          [S4]
#
# (sin formulario hoy)                    → ContactoForm + {% csrf_token %}     [S5]
