from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.signals import post_save
from .Serializer import *
from rest_framework import generics
from .models import *
import jwt, datetime
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ClienteLista(generics.ListCreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(Usr_codigo=user)

    def perform_create(self, serializer):
        serializer.save(Usr_codigo=self.request.user)

    def post(self, request):
        per_correo = request.data.get('Per_nombre', {}).get('Per_correo')
        
        if per_correo and Persona.objects.filter(Per_correo=per_correo).exists():
            return JsonResponse({"errors": {"Per_correo": ["Este correo ya está en uso."]}}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return JsonResponse({"message": "Cliente creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClienteDetalle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(Usr_codigo=user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClienteSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        persona_instance = instance.Per_nombre

        self.perform_destroy(instance)
        self.perform_destroy(persona_instance)

        return JsonResponse({"message": "Cliente eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()



# class ClienteLista(generics.ListCreateAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

#     def post(self, request):
#         per_correo = request.data.get('Per_nombre', {}).get('Per_correo')
        
#         if per_correo and Persona.objects.filter(Per_correo=per_correo).exists():
#             return JsonResponse({"errors": {"Per_correo": ["This email is already in use."]}}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = ClienteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"message": "Cliente creado exitosamente"}, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ClienteDetalle(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = ClienteSerializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse(serializer.data)
    
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         persona_instance = instance.Per_nombre

#         self.perform_destroy(instance)
#         self.perform_destroy(persona_instance)

#         return JsonResponse({"message": "Cliente eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
    
#     def perform_destroy(self, instance):
#         instance.delete()
    

class ProveedorLista(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def post(self, request):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Proveedor creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProveedorDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProveedorSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
    
class SedeProveedorLista(generics.ListCreateAPIView):
    queryset = SedeProveedor.objects.all()
    serializer_class = SedeProveedorSerializer

    def post(self, request):
        serializer = SedeProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Sede creada exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SedeProveedorDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = SedeProveedor.objects.all()
    serializer_class = SedeProveedorSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SedeProveedorSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

