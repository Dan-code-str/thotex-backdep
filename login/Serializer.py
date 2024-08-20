from rest_framework import serializers
from .models import User, Municipio, Departamento

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ['id', 'first_name', 'last_name', 'telefono', 'correo', 'contrasena']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }

        
    def create(self, validated_data):
        
        contrasena = validated_data.pop('contrasena', None)
        instance = self.Meta.model(**validated_data)
        if contrasena is not None:
            instance.set_password(contrasena)
        instance.save()
        
        return instance
    

# class MunicipioSerializer(serializers.ModelSerializer):
    
#     class Meta:     
#         model = Municipio
#         fields = '__all__'

# class DepartamentoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departamento
#         fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['Mun_id', 'Mun_nombre']

class DepartamentoSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True, source='municipio_set')

    class Meta:
        model = Departamento
        fields = ['Dep_id', 'Dep_nombre', 'municipios']
        