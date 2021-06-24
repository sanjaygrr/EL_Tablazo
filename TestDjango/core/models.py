from django.db import models

# Create your models here.
class Cliente(models.Model):
    identificacion = models.IntegerField(primary_key=True, verbose_name="Id de Usario")
    telefono = models.classEmailField ( max_length=50, verbose_name="Nombre de la categoria" ) 
    direccion =models.CharField(max_length=50, verbose_name=name="direccion")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categoria")


    def __str__(self):
        return self.nombreCategoria

        Número de identificación
Dirección.
Email
Contraseña
País.
