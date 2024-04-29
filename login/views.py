# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .Serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime

User = get_user_model()

# class RegisterView(APIView):
    
#     def post(self, request):
                
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'mensaje': 'Registro fallido'})


class LoginView(APIView):
    
    def post(self, request):
        
        correo = request.data['correo']
        contrasena = request.data['contrasena']

        user = authenticate(username=correo, password=contrasena)
        if user is not None:
            login(request, user)
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token
            }
            
            return response
        else:
            return JsonResponse({'mensaje': 'Inicio de sesion fallido'})

class UserView(APIView):

    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            return JsonResponse({'mensaje': 'No hay token'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token expirado'})

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
        
class LogoutView(APIView):
    
        def post(self, request):
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'message': 'Sesion cerrada'
            }
            return response
                        
                        
        

