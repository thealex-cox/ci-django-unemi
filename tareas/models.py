from django.db import models


class Tarea(models.Model):
    """Representa una tarea registrada en el sistema."""

    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada_en']
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.titulo
