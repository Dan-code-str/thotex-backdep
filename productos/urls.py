from django.urls import path
from .views import *


urlpatterns = [
    path('productos/', ProductoLista.as_view(), name='productos_lista'),
    path('productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle')
]