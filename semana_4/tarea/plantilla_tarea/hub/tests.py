from django.test import TestCase
from .models import Recurso


class RecursoModelTest(TestCase):
    def test_creacion_recurso(self):
        Recurso.objects.create(
            titulo="Guía de Álgebra",
            url="https://ejemplo.com",
            descripcion="Material de apoyo",
        )
        self.assertEqual(Recurso.objects.count(), 1)

    def test_str_devuelve_titulo(self):
        recurso = Recurso.objects.create(
            titulo="Guía de Álgebra", url="https://ejemplo.com",
        )
        self.assertEqual(str(recurso), "Guía de Álgebra")


# ============================================================
# TODO — Prueba para Mensaje
#
# Cuando hayas definido el modelo Mensaje en models.py,
# agrega aquí una prueba similar:
#
#   from .models import Mensaje
#
#   class MensajeModelTest(TestCase):
#       def test_creacion_mensaje(self):
#           Mensaje.objects.create(
#               nombre="Ana García",
#               correo="ana@ejemplo.com",
#               mensaje="Hola, ¿hay tutoría esta semana?",
#           )
#           self.assertEqual(Mensaje.objects.count(), 1)
#
#       def test_str_devuelve_nombre_y_fecha(self):
#           # El __str__ del modelo devuelve "nombre — DD/MM/AAAA"
#           msg = Mensaje.objects.create(
#               nombre="Ana García",
#               correo="ana@ejemplo.com",
#               mensaje="Hola",
#           )
#           self.assertIn("Ana García", str(msg))
#
# ============================================================
