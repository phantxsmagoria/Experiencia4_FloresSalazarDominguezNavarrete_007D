from django.urls import path
from .views import index, vision,seguimiento, compras2, mision, quienessomos, formulario, adoptados, galeria, registrousuario, compras, mod_registrousuario, mostrardatos, del_registrousuario

urlpatterns = [
    path('',index,name="index"),
    path('index.html',index,name="index"),
    path('vision.html',vision,name="vision"),
    path('mision.html',mision,name="mision"),
    path('quienessomos.html',quienessomos,name="quienessomos"),
    path('formulario.html',formulario,name="formulario"),
    path('adoptados.html',adoptados,name="adoptados"),
    path('galeria.html',galeria,name="galeria"),
    path('compras.html',compras,name="compras"),
    path('compras2.html',compras2,name="compras2"),
    path('registrousuario.html',registrousuario,name="registrousuario"),
    path('mod_registrousuario.html/compras.html',compras,name="compras"),
    path('mod_registrousuario.html/compras2.html',compras2,name="compras2"),
    path('mod_registrousuario.html/index.html',index,name="index"),
    path('mod_registrousuario.html/vision.html',vision,name="vision"),
    path('mod_registrousuario.html/mision.html',mision,name="mision"),
    path('mod_registrousuario.html/quienessomos.html',quienessomos,name="quienessomos"),
    path('mod_registrousuario.html/formulario.html',formulario,name="formulario"),
    path('mod_registrousuario.html/adoptados.html',adoptados,name="adoptados"),
    path('mod_registrousuario.html/galeria.html',galeria,name="galeria"),
    path('mod_registrousuario.html/registrousuario.html',registrousuario,name="registrousuario"),
    path('mod_registrousuario.html/mostrardatos.html',mostrardatos,name="mostardatos"),
    path('mod_registrousuario.html/seguimiento.html',seguimiento,name="seguimiento"),
    path('mod_registrousuario.html/<id>',mod_registrousuario,name="mod_registrousuario"),
    path('del_registrousuario.html/<id>',del_registrousuario,name="del_registrousuario"),
    path('mostrardatos.html',mostrardatos,name="mostardatos"),
    path('seguimiento.html',seguimiento,name="seguimiento"),
]



