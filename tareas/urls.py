from django.urls import path

from .views import lista_tareas

urlpatterns = [
    path('tareas/', lista_tareas, name='lista_tareas'),
]
