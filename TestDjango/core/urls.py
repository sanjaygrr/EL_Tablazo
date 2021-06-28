from django.urls import path
from .views import pagina,sismos,informacion,productos,contacto,cliente,form_cliente

urlpatterns = [
 path('', pagina,name="pagina"),
 path('sismos', sismos,name="sismos"),
 path('informacion', informacion,name="informacion"),
 path('productos', productos,name="productos"),
 path('contacto', contacto,name="contacto"),
 path('cliente_formulario', form_cliente,name="cliente_formulario"),
 path('cliente', cliente,name="cliente"),
]
