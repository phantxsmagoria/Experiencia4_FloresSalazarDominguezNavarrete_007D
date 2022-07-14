from rest_framework import serializers
from prueba3.models import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['pnombre','apellido','email','contraseña','rut','telefono','Direccion','region','comuna','suscripcion']