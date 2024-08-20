from django.urls import path
from .views import *

urlpatterns = [
    path('eventos/', EventoLista.as_view(), name='eventos'),
    path('eventos/<int:pk>/', EventoDetalle.as_view(), name='evento'),
]