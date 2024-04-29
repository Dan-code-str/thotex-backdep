from django import forms
from .models import Persona, Empleado

class PersonaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

