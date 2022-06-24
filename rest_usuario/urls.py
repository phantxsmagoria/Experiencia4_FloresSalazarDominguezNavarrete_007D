from django.urls import path
from rest_usuario.views import lista_usuarios,detalle_usuario

urlpatterns = [
    path('lista_usuarios',lista_usuarios,name="lista_usuarios"),
    path('detalle_usuario/<id>', detalle_usuario, name="detalle_usuario"),
]