from rest_framework import serializers
from .models import *
from terceros.models import Cliente
from terceros.Serializer import ClienteSerializer
        
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['Cliente'] = ClienteSerializer(instance.Cliente).data
    #     return representation
        
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['Proveedor'] = ClienteSerializer(instance.Proveedor).data
    #     return representation
    
