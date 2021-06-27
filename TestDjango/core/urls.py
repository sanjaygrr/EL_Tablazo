from django.urls import path
from .views import home,sismos,informacion,productos,contacto

urlpatterns = [
 path('', home,name="pagina"),
 path('sismos', sismos,name="sismos"),
 path('informacion', informacion,name="informacion"),
 path('productos', productos,name="productos"),
 path('contacto', contacto,name="contacto"),
 path('cliente_formulario', cliente_formulario,name="cliente_formulario"),
 path('clientes', clientes,name="clientes"),
 path('CLiente', Cliente,name="Cliente"),
]
