from django.urls import path
from .views import pagina,sismos,informacion,productos,contacto,cliente,form_cliente,form_cliente_mod,form_cliente_del

urlpatterns = [
 path('', pagina,name="pagina"),
 path('sismos', sismos,name="sismos"),
 path('informacion', informacion,name="informacion"),
 path('productos', productos,name="productos"),
 path('contacto', contacto,name="contacto"),
 path('cliente_formulario', form_cliente,name="cliente_formulario"),
 path('cliente_formulario_mod/<id>', form_cliente_mod,name="cliente_formulario_mod"),
 path('cliente_formulario_del/<id>', form_cliente_del,name="cliente_formulario_del"),
 path('cliente', cliente,name="cliente"),
]
