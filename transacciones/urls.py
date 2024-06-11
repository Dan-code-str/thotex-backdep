from django.urls import path
from .views import *


urlpatterns = [
    path('ventas/', VentaLista.as_view(), name='ventas'),
    path('ventas/<int:pk>/', VentaDetalle.as_view(), name='venta_detalle'),
    path('compras/', CompraLista.as_view(), name='compras'),
    path('compras/<int:pk>/', CompraDetalle.as_view(), name='compra_detalle')
]
