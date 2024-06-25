from django.db import models
from login.models import Municipio, Departamento, User
from django.core.validators import MaxValueValidator, MinValueValidator
# create your models here.

class Persona(models.Model):

    tipoId = [
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('PA', 'Pasaporte'),
    ]

    Per_codigo = models.AutoField(primary_key = True)
    Per_tipoId = models.CharField(max_length = 30, choices = tipoId, verbose_name='Tipo de identificacion')
    Per_id = models.CharField(max_length = 50, verbose_name='Identificacion')
    Per_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Per_apellido = models.CharField(max_length = 50, verbose_name='Apellido')
    Per_correo = models.EmailField(max_length = 50, verbose_name='Correo', unique=True)
    Per_telefono = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='Telefono')
    # Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)

    class Meta:
        db_table = "Persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self) -> str:
        return self.Per_nombre
    
class Empleado(models.Model):
    Emp_codigo = models.AutoField(primary_key=True)
    Emp_cargo = models.CharField(max_length = 60, verbose_name='cargo')
    Emp_salario = models.IntegerField(verbose_name="salario")
    Emp_fechaingreso = models.DateField(verbose_name="fecha de ingreso", auto_now_add=True)
    Persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class meta:
        db_table = "Empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self) -> str:
        return self.Persona.Per_nombre
