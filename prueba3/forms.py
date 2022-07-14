from django import forms 
from django.forms import ModelForm
from .models import Usuario, Contacto, Producto, Venta


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['pnombre','apellido','email','contraseña','rut','telefono','Direccion','region','comuna','suscripcion']

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = ['rut','pnombre','apellido','email','telefono','dudas']

class VentaForm(ModelForm):

    class Meta:
        model = Venta
        fields = ['id_venta','usuario','producto','cantidad']