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
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
import requests

# Create your views here.

class VentaLista(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def get_queryset(self):

        request = self.request
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token expirado'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN)
        
        ventas = Venta.objects.filter(Usr_codigo=user)
        lista_ventas = list(ventas.values())

        return JsonResponse({'data: ': lista_ventas}, safe=False)


    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token expirado'}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(id=payload['id']).first()

        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            # Asignar el usuario autenticado
            serializer.save(Usr_codigo=user)
            return JsonResponse({"message": "Venta creada exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     user = self.request.user.id

    #     serializer = VentaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # Asignar el usuario autenticado
    #         serializer.save(Usr_codigo=user)
    #         return JsonResponse({"message": "Venta creada exitosamente"}, status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     token = request.COOKIES.get('jwt')

    #     if not token:
    #         return JsonResponse({'mensaje': 'No hay token'})

    #     try:
    #         payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    #     except jwt.ExpiredSignatureError:
    #         return JsonResponse({'mensaje': 'Token expirado'})

    #     # Retrieve the current user based on the decoded payload
    #     user = get_user_model().objects.get(pk=payload['id'])

    #     # Access or create the serializer, ensuring 'Usr_codigo' is set
    #     data = request.data.copy()  # Avoid modifying original request data
    #     data['Usr_codigo'] = user.codigo  # Assuming 'codigo' holds the user's ID
    #     serializer = VentaSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({"message": "Venta creada exitosamente"}, status=status.HTTP_201_CREATED)
        
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer = VentaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({"message": "Venta creada exitosamente"}, status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VentaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = VentaSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
    
    
class CompraLista(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

#     # def post(self, request):
#     #     token = request.COOKIES.get('jwt')

#     #     if not token:
#     #         return JsonResponse({'mensaje': 'No hay token'})

#     #     try:
#     #         payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#     #     except jwt.ExpiredSignatureError:
#     #         return JsonResponse({'mensaje': 'Token expirado'})

#     #     # Retrieve the current user based on the decoded payload
#     #     user = get_user_model().objects.get(pk=payload['id'])

#     #     # Access or create the serializer, ensuring 'Usr_codigo' is set
#     #     data = request.data.copy()  # Avoid modifying original request data)
#     #     data['Usr_codigo'] = user.codigo  # Assuming 'codigo' holds the user's ID
#     #     serializer = CompraSerializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse({"message": "Compra creada exitosamente"}, status=status.HTTP_201_CREATED)
#     #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            usr_id = self.context['request'].user
            serializer.save()
            return JsonResponse({"message": "Compra creada exitosamente", "id": usr_id}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CompraLista(generics.ListCreateAPIView):
#     queryset = Compra.objects.all()
#     serializer_class = CompraSerializer

#     def post(self, request, *args, **kwargs):
#         try:
#             # Obtain JWT token from cookies
#             token = request.COOKIES.get('jwt')
            
#             if not token:
#                 return JsonResponse({"error": "JWT token not found"}, status=status.HTTP_401_UNAUTHORIZED)

#             # Make a GET request to the user endpoint with JWT token in headers
#             headers = {'Authorization': f'Bearer {token}'}
#             response = requests.get('http://localhost:8000/api/v1.0/user', headers=headers)
#             response.raise_for_status()  # Raise exception for 4xx/5xx status codes
            
#             # Parse JSON response
#             user_data = response.json()
#             user_id = user_data.get('id')

#             # Check if user ID is extracted correctly
#             if user_id is None:
#                 return JsonResponse({"error": "User ID not found in response"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#             # Proceed with Compra creation using request data
#             serializer = CompraSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({"message": "Compra creada exitosamente", "user_id": user_id}, status=status.HTTP_201_CREATED)
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         except requests.exceptions.RequestException as e:
#             # Handle GET request errors
#             return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except ValueError:
#             # Handle JSON decoding errors
#             return JsonResponse({"error": "Error decoding JSON response"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
class CompraDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompraSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
    
