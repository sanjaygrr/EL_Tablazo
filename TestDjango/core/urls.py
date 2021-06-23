from django.urls import path
from .views import home,sismos,informacion,productos,contacto

urlpatterns = [
 path('', home,name="Pagina"),
 path('/sismos', sismos,name="Sismos"),
 path('/informacion', informacion,name="Informacion"),
 path('/productos', productos,name="Productos"),
 path('/contacto', contacto,name="Contacto"),

]
