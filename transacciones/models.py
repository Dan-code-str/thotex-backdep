from django.db import models
from empleados.models import Persona
from terceros.models import Cliente, Proveedor, SedeProveedor
from login.models import User

# Create your models here.

class Venta(models.Model):

    Ven_codigo = models.AutoField(primary_key=True, verbose_name="Venta codigo")
    Ven_fechaGeneracion = models.DateField(verbose_name='Fecha generacion', auto_now_add=True)
    Ven_subtotal = models.DecimalField(verbose_name="Subtotal", decimal_places=2, max_digits=15)
    Ven_precioTotal = models.DecimalField(verbose_name="Precio total", decimal_places=2, max_digits=15)
    Ven_IVA = models.DecimalField(verbose_name="IVA", decimal_places=2, max_digits=3) #tipo de dato (IGUAL PRODUCTO)
    Cl_codigo = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", default=0)


    class Meta:
        db_table = "Venta"
        verbose_name =  "Venta"
        verbose_name_plural = "Ventas"
        
    def __str__(self) -> str:
        return str(self.Ven_codigo)
    

class Compra(models.Model):
    
    Com_codigo = models.AutoField(primary_key=True, verbose_name="Compra codigo")
    Com_fechaGeneracion = models.DateField(verbose_name='Fecha generacion', auto_now_add=True)
    Com_subtotal = models.DecimalField(verbose_name="Subtotal", decimal_places=2, max_digits=15)
    Com_precioTotal = models.DecimalField(verbose_name="Precio total", decimal_places=2, max_digits=15)
    Com_IVA = models.DecimalField(verbose_name="IVA", decimal_places=2, max_digits=3) #tipo de dato (IGUAL PRODUCTO)
    Cl_codigo = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", default=0)
    
    class Meta:
        db_table = "Compra"
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        
    def __str__(self) -> str:
        return self.Usr_codigo.first_name