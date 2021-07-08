from django.urls import path
from rest_proveedor.views import lista_proveedor

urlpatterns = [
    path('lista_proveedor', lista_proveedor, name="lista_proveedor"),
]