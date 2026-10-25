from django.http import JsonResponse

from .models import Tarea


def lista_tareas(request):
    """Devuelve el listado de tareas registradas en formato JSON."""
    datos = list(Tarea.objects.values('id', 'titulo', 'completada'))
    return JsonResponse({'total': len(datos), 'tareas': datos})
