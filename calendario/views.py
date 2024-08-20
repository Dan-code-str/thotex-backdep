from django.shortcuts import render
from .models import Evento
from django.shortcuts import render
from rest_framework import generics
from .Serializer import EventoSerializer
from django.http import JsonResponse
from rest_framework import status
import jwt
from login.models import User
from rest_framework.response import Response

# Create your views here.

class EventoLista(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

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

        list = Evento.objects.all()

        json_type = EventoSerializer(list, many=True).data

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
        
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Usr_codigo=user)
            return JsonResponse({"mensaje": "Evento creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get(self, request, *args, **kwargs):
        register = EventoSerializer(self.get_object()).data
        
        context = {
            'data': register,
        }

        return Response(context, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.data)
        serializer = EventoSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        context = {
            'data': serializer.data,
        }

        return Response(context, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse({"mensaje":"Evento eliminado exitosamente"}, safe=False)

