from rest_framework import generics
from .models import Empleado
from django.db.models.signals import post_save
from .Serializer import *

# Create your views here.
class EmpleadoLista(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
class EmpleadoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
# def create_persona(sender, instance, created, **kwargs):
#     if created:
#         empleado_persona = Empleado(Per_nombre = instance)
#         empleado_persona.save()
        
# post_save.connect(create_persona, sender = Empleado)
    
