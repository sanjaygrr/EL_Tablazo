from django.db import models

# Create your models here.
class Cliente(models.Model):
    identificacion = models.IntegerField(primary_key=True, verbose_name="Id de Usario")
    telefono = models.CharField ( max_length=10, verbose_name="telefono" ) 
    email =models.classEmailField(max_length=50, verbose_name=name="email")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    email = models.CharField(max_length=50, verbose_name="email")
    constraseña = models.CharField(max_length=50, verbose_name="Constraseña")
    pais = models.CharField(max_length=50, verbose_name="pais")

    def __str__(self):
        return self.telefono