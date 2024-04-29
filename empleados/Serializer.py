from rest_framework import serializers
from .models import Empleado, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    
    persona = PersonaSerializer(many=True)  # Include Persona data

    class Meta:
        model = Empleado
        exclude = ('Persona',)

    def create(self, validated_data):
        persona_data = validated_data.pop('persona')
        persona_instance = Persona.objects.create(**persona_data)
        empleado_instance = Empleado.objects.create(**validated_data, Persona=persona_instance)
        return empleado_instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['persona'] = PersonaSerializer(instance.Persona).data
        return representation