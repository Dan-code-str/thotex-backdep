from django.shortcuts import render
from rest_framework import generics
from .models import *
from .Serializer import *
from django.http import JsonResponse
from rest_framework import status
from django.http import HttpResponse
import jwt, datetime
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
import requests

class VentaLista(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def get(self, request):
        
        request = self.request
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()

        if user is None:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN)

        ventas = Venta.objects.filter(Usr_codigo=user)

        json_ventas = VentaSerializer(ventas, many=True).data

        context = {
            'data': json_ventas,
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request = self.request
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()

        if user is None:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN)

        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(Usr_codigo=user)
            return JsonResponse({"mensaje": "Venta creada exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VentaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def get(self, request, *args, **kwargs):
        register = VentaSerializer(self.get_object()).data
        
        context = {
            'data': register,
        }

        return Response(context, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = VentaSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        context = {
            'data': serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse({"mensaje": "Venta eliminada exitosamente"}, safe=False)
    
    
class CompraLista(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get(self, request):

        request = self.request
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()

        if user is None:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN)

        compras = Compra.objects.filter(Usr_codigo=user)

        json_type = CompraSerializer(compras, many=True).data

        context = {
            'data': json_type,
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):

        request = self.request
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()

        if user is None:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Usr_codigo=user)
            return JsonResponse({"mensaje": "Compra creada exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
class CompraDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get(self, request, *args, **kwargs):
        register =CompraSerializer(self.get_object()).data
        
        context = {
            'data': register,
        }

        return Response(context, status=status.HTTP_200_OK)
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompraSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        context = {
            'data': serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return JsonResponse({"mensaje": "Compra eliminada exitosamente"}, status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()
    
