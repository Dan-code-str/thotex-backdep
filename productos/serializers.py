from rest_framework import serializers
from .models import *
from django.http import JsonResponse
from rest_framework import status

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'