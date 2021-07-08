from django.db import models

# Create your models here.
class Pais(models.Model):
    pais = models.IntegerField(primary_key=True, verbose_name="Id de Pais")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre del Pais")

    def __str__(self):
        return self.nombrePais
class Cliente(models.Model):
    identificacion = models.AutoField(primary_key=True, verbose_name="Id de Usario")
    telefono = models.CharField ( max_length=12, verbose_name="telefono" ) 
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    email = models.EmailField(max_length=50, verbose_name="email")
    constraseña = models.CharField(max_length=50, verbose_name="Constraseña")
    pais =  models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre