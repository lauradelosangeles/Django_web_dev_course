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
