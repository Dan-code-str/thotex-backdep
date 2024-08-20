from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt

class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expirado')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Token inválido')
        
        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        return (user, None)
