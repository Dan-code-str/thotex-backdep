from django.urls import path
from .views import EmpleadoLista, EmpleadoDetalle

urlpatterns = [
    path('empleados', EmpleadoLista.as_view(), name='empleados'),
    path('empleados/<int:pk>', EmpleadoDetalle.as_view(), name='empleado'), 
]