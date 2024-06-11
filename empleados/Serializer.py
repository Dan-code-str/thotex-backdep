from rest_framework import serializers
from .models import Empleado, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        extra_kwargs = {
            'Per_correo': {'validators': []},
        }

class EmpleadoSerializer(serializers.ModelSerializer):
    
    Persona = PersonaSerializer()  # Include Persona data

    class Meta:
        model = Empleado
        fields = '__all__'

    def create(self, validated_data):
        persona_data = validated_data.pop('Persona')
        persona_instance = Persona.objects.create(**persona_data)
        empleado_instance = Empleado.objects.create(**validated_data, Persona=persona_instance)
        return empleado_instance

    def update(self, instance, validated_data):
        persona_data = validated_data.pop('Persona')
        persona = instance.Persona
        instance.Emp_codigo = validated_data.get('Emp_codigo', instance.Emp_codigo)
        instance.Emp_cargo = validated_data.get('Emp_cargo', instance.Emp_cargo)
        instance.Emp_salario = validated_data.get('Emp_salario', instance.Emp_salario)
        instance.Emp_fechaingreso = validated_data.get('Emp_fechaingreso', instance.Emp_fechaingreso)
        persona.Per_codigo = persona_data.get('Per_codigo', persona.Per_codigo)
        persona.Per_tipoId = persona_data.get('Per_tipoId', persona.Per_tipoId)
        persona.Per_id = persona_data.get('Per_id', persona.Per_id)
        persona.Per_nombre = persona_data.get('Per_nombre', persona.Per_nombre)
        persona.Per_apellido = persona_data.get('Per_apellido', persona.Per_apellido)
        persona.Per_correo = persona_data.get('Per_correo', persona.Per_correo)
        persona.Per_telefono = persona_data.get('Per_telefono', persona.Per_telefono)
        persona.Mun_nombre = persona_data.get('Mun_nombre', persona.Mun_nombre)
        persona.save()
        instance.save()
        return instance