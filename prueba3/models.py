from django.db import models

# Create your models here.

class Usuario(models.Model):
    pnombre =models.CharField(max_length=50, verbose_name='Primer Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.CharField(max_length=50,verbose_name='Email')
    contraseña = models.CharField(max_length=50,verbose_name='Contraseña')
    rut = models.CharField(primary_key=True, max_length=25,verbose_name='RUT')
    telefono = models.CharField(max_length=50,verbose_name='Teléfono')
    Direccion = models.CharField(max_length=50,verbose_name='Dirección')
    region = models.CharField(max_length=50,verbose_name='Región')
    comuna = models.CharField(max_length=50,verbose_name='Comuna')
    suscripcion = models.CharField(max_length=2,verbose_name="suscripcion")

    def __str__(self):
        return self.rut

class Contacto(models.Model):
    rut = models.CharField(primary_key=True, max_length=25,verbose_name='RUT')
    pnombre = models.CharField(max_length=50, verbose_name='Primer Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.CharField(max_length=50,verbose_name='Email')
    telefono = models.CharField(max_length=50,verbose_name='Teléfono')
    dudas = models.CharField(max_length=500,verbose_name='Dudas y Consultas')
    
    def __str__(self):
        return self.rut

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=25,verbose_name='ID_PRODUCTO')
    nom_producto = models.CharField(max_length=50, verbose_name='Nombre Producto')
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    
    def __str__(self):
        return self.nom_producto

class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=25,verbose_name='ID_VENTA')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True,verbose_name='Cantidad de producto')
    total_venta = models.IntegerField(null=True,verbose_name='Monto total de venta')
    descuento = models.CharField(max_length=25, verbose_name='Porcentaje de descuento')

    def __str__(self):
        return self.id_venta

