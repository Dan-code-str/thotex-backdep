from rest_framework import serializers
from .models import Cliente, Proveedor, SedeProveedor
from empleados.models import Persona
from empleados.Serializer import PersonaSerializer

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    # def create(self, validated_data):
    #     persona_data = validated_data.pop('Per_nombre')
    #     persona_instance = Persona.objects.create(**persona_data)
    #     cliente_instance = Cliente.objects.create(Per_nombre=persona_instance, **validated_data)
    #     return cliente_instance
    

    # def update(self, instance, validated_data):
    #     persona_data = validated_data.pop('Per_nombre')
    #     persona = instance.Per_nombre
    #     instance.Cl_codigo = validated_data.get('Cl_codigo', instance.Cl_codigo)
    #     instance.Cl_obligacion = validated_data.get('Cl_obligacion', instance.Cl_obligacion)
    #     persona.Per_codigo = persona_data.get('Per_codigo', persona.Per_codigo)
    #     persona.Per_tipoId = persona_data.get('Per_tipoId', persona.Per_tipoId)
    #     persona.Per_id = persona_data.get('Per_id', persona.Per_id)
    #     persona.Per_nombre = persona_data.get('Per_nombre', persona.Per_nombre)
    #     persona.Per_apellido = persona_data.get('Per_apellido', persona.Per_apellido)
    #     persona.Per_correo = persona_data.get('Per_correo', persona.Per_correo)
    #     persona.Per_telefono = persona_data.get('Per_telefono', persona.Per_telefono)
    #     persona.Mun_nombre = persona_data.get('Mun_nombre', persona.Mun_nombre)
    #     persona.save()
    #     instance.save()
    #     return instance
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['Per_nombre'] = PersonaSerializer(instance.Per_nombre).data
    #     return representation
    
    

class ProveedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proveedor
        fields = '__all__'

class SedeProveedorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = SedeProveedor
        fields = '__all__'