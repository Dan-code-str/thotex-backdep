# utils/jwt_utils.py
import jwt
from django.http import JsonResponse
from django.conf import settings
from rest_framework import status
from login.models import User

def decode_jwt(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN), None

    token = auth_header.split(' ')[1]

    if not token or token == 'null':
        return JsonResponse({'mensaje': 'No hay token'}, status=status.HTTP_403_FORBIDDEN), None

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse({'mensaje': 'Token expirado'}, status=status.HTTP_403_FORBIDDEN), None
    except jwt.InvalidTokenError:
        return JsonResponse({'mensaje': 'Token inválido'}, status=status.HTTP_403_FORBIDDEN), None

    user = User.objects.filter(id=payload['id']).first()
    if user is None:
        return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_403_FORBIDDEN), None

    return None, user
