from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', ClienteLista.as_view(), name='clientes'),
    path('clientes/<int:pk>/', ClienteDetalle.as_view(), name='cliente_detalle'),
    path('proveedores/', ProveedorLista.as_view(), name='proveedores'),
    path('proveedores/<int:pk>/', ProveedorDetalle.as_view(), name='proveedor_detalle')
]