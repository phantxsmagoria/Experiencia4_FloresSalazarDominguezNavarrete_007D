from django.contrib import admin
from .models import Usuario, Contacto, Producto, Venta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Venta)
