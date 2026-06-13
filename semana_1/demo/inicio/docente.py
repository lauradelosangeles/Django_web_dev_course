# ============================================================
# SEMANA 1 — INICIO: De variables sueltas a una clase
# Ejecutar: python docente.py
# ============================================================
    

# ════════════════════════════════════════════════════════════
# PROBLEMA: datos sueltos, sin estructura
# ════════════════════════════════════════════════════════════
nombre      = "Prof. González Silva"
materia     = "Matemáticas"
institucion = "Colegio Simón Bolívar"
experiencia = 10

# ¿Y si necesitamos un segundo docente? → duplicamos todo. ❌


# ════════════════════════════════════════════════════════════
# SOLUCIÓN: una clase agrupa datos + comportamiento
# ════════════════════════════════════════════════════════════

class Docente:
    """Representa a un docente con su información pública."""
    # TODO EN VIVO ① — el profesor escribe el cuerpo de __init__:
    #   self.nombre           = nombre
    #   self.materia          = materia
    #   self.institucion      = institucion
    #   self.años_experiencia = años_experiencia
    #   self.materias         = materias or []   ← lista de asignaturas
    def __init__(self, nombre, materia, institucion, años_experiencia, materias=None):
        self.nombre = nombre
        self.materia = materia
        self.institucion = institucion
        self.anos_experiencia = años_experiencia
        self.materias = materias or []
        pass

    # TODO EN VIVO ② — el profesor escribe el cuerpo de presentarse:
    #   print(f"Hola, soy {self.nombre}.")
    #   print(f"Enseño {self.materia} en {self.institucion}.")
    #   print(f"Tengo {self.anos_experiencia} años de experiencia.")
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        print(f"Enseño {self.materia} en {self.institucion}.")
        print(f"Tengo {self.anos_experiencia} años de experiencia.")

# ── Uso (descomentar al terminar __init__ y presentarse) ────
# docente_1 = Docente(
#     "Prof. González Silva", "Matemáticas", "C. Simón Bolívar", 10,
#     materias=["Álgebra — 8° grado", "Geometría — 9°", "Precálculo — 10°"],
# )
# docente_2 = Docente("Prof. Rodríguez", "Historia", "Liceo Central", 5)
# docente_1.presentarse()
# docente_2.presentarse()

docente_1 = Docente(
     "Prof. González Silva", "Matemáticas", "C. Dolores Sucre", 10,
     materias=["Álgebra — 8° grado", "Geometría — 9°", "Precálculo — 10°"],
 )
docente_2 = Docente("Prof. Rodríguez", "Historia", "Liceo Central", 5)

print(nombre)
print(materia)
print(institucion)
print(experiencia)
#print(f"Hola Mundo, me llamo {nombre}")
#docente_1.presentarse()
docente_2.presentarse()