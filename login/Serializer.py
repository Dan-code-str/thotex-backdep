from rest_framework import serializers
from .models import User

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
        