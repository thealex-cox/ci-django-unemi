from django.test import TestCase
from django.urls import reverse

from .models import Tarea


class TareaModelTest(TestCase):
    """Pruebas unitarias del modelo Tarea."""

    def test_crear_tarea_por_defecto_no_esta_completada(self):
        tarea = Tarea.objects.create(titulo='Configurar GitHub Actions')
        self.assertEqual(str(tarea), 'Configurar GitHub Actions')
        self.assertFalse(tarea.completada)

    def test_marcar_tarea_como_completada(self):
        tarea = Tarea.objects.create(titulo='Instalar dependencias')
        tarea.completada = True
        tarea.save()
        self.assertTrue(Tarea.objects.get(pk=tarea.pk).completada)


class TareaVistaTest(TestCase):
    """Pruebas de integracion de la vista lista_tareas."""

    def test_la_vista_responde_200(self):
        respuesta = self.client.get(reverse('lista_tareas'))
        self.assertEqual(respuesta.status_code, 200)

    def test_la_vista_devuelve_las_tareas_registradas(self):
        Tarea.objects.create(titulo='Tarea de prueba CI')
        respuesta = self.client.get(reverse('lista_tareas'))
        self.assertContains(respuesta, 'Tarea de prueba CI')
