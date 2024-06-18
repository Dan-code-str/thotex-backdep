from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework import status
from utils.jwt_utils import decode_jwt
import logging

logger = logging.getLogger(__name__)

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        error_response, user = decode_jwt(request)
        if error_response:
            request.jwt_auth_error = error_response
        else:
            request.user = user
            logger.info(f"Authenticated user: {user}")

