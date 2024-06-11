from django.db import models
from login.models import Municipio
from terceros.models import Proveedor

# Create your models here.
class Producto(models.Model):

    #iva = choices (exento, 0%, 5%, 19% - otros?)

    Prod_codigo = models.AutoField(primary_key=True, verbose_name="Codigo de producto")
    Prod_nombre = models.CharField(max_length = 60, verbose_name='Nombre producto')
    Prod_precio = models.DecimalField(verbose_name="Precio unitario", decimal_places=2, max_digits=15)
    Prod_cantidad = models.IntegerField(verbose_name="Cantidad")
    Prod_IVA = models.DecimalField(verbose_name="IVA", decimal_places=2, max_digits=3) #tipo de dato (Definir campo TIPO IVA - TOTAL IVA)
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Emp_codigo = models.ForeignKey(Proveedor, verbose_name="Empresa", on_delete=models.CASCADE)

    class Meta:
        db_table = "Producto"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return self.Prod_nombre