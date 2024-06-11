from rest_framework import generics
from .models import Empleado
from django.db.models.signals import post_save
from .Serializer import *
from rest_framework import status
from django.http import JsonResponse


# Create your views here.
class EmpleadoLista(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def post(self, request):
        per_correo = request.data.get('Persona', {}).get('Per_correo')
        
        if per_correo and Persona.objects.filter(Per_correo=per_correo).exists():
            return JsonResponse({"errors": {"Per_correo": ["This email is already in use."]}}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Empleado creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmpleadoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EmpleadoSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        persona_instance = instance.Persona

        self.perform_destroy(instance)
        self.perform_destroy(persona_instance)

        return JsonResponse({"message": "Empleado eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    
# def create_persona(sender, instance, created, **kwargs):
#     if created:
#         empleado_persona = Empleado(Per_nombre = instance)
#         empleado_persona.save()
        
# post_save.connect(create_persona, sender = Empleado)
    
