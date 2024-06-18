from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.http import JsonResponse
from rest_framework import status
from login.models import User
import jwt
from rest_framework.response import Response

# Create your views here.

class ProductoLista(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

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

        list = Producto.objects.filter(Usr_codigo=user)

        json_type = ProductoSerializer(list, many=True).data

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

        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Usr_codigo=user)
            return JsonResponse({"message": "Producto creado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductoSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)