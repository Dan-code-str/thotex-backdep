from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Empleado, Persona
from django.db.models.signals import post_save
from .Serializer import *
from rest_framework import status
from django.http import JsonResponse
import jwt
from login.models import User
from rest_framework.response import Response

class EmpleadoLista(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

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

        list = Empleado.objects.filter(Usr_codigo=user)

        json_type = EmpleadoSerializer(list, many=True).data

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

        per_correo = request.data.get('Persona', {}).get('Per_correo')
        
        if per_correo and Persona.objects.filter(Per_correo=per_correo).exists():
            return JsonResponse({"errors": {"Per_correo": ["Este correo ya está en uso"]}}, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Usr_codigo=user)
            return JsonResponse({"mensaje": "Empleado creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmpleadoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get(self, request, *args, **kwargs):
        register = EmpleadoSerializer(self.get_object()).data
        
        context = {
            'data': register,
        }

        return Response(context, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.data)
        serializer = EmpleadoSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        context = {
            'data': serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse({"mensaje":"Empleado eliminado exitosamente"}, safe=False)
    
