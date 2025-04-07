from django.urls import path
from .views import lista_empleados, crear_empleado, crear_documento

app_name = 'documents'  # <- Agregamos el namespace acá

urlpatterns = [
    path('', lista_empleados, name='lista_empleados'),
    path('nuevo-empleado/', crear_empleado, name='crear_empleado'),
    path('nuevo-documento/', crear_documento, name='crear_documento'),
]