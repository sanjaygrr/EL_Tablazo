from django.urls import path
from .views import form_proveedores,pagina, contacto, quienesSomos, nuestrosproductos, form_mod_proveedor, form_del_proveedor, listado

urlpatterns = [
    path('', pagina, name="pagina"),
    path('contacto', contacto, name="contacto"),
    path('quienesSomos', quienesSomos, name="quienesSomos"),
    path('nuestrosproductos', nuestrosproductos, name="nuestrosproductos"),
    path('form-proveedor', form_proveedores, name="form_proveedor"),
    path('form-mod-proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form-del-proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
    path('listado', listado, name="listado"),

]