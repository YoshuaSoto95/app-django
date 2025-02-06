from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # Cascade: elimina el producto si se elimina la categoria
    # Protect: lanza un error si se intenta eliminar la categoria
    # Restric: solo elimina si no existe productos relacionados
    # SetNull: pone en null la categoria si se elimina
    # setDefault: pone un valor por defecto si se elimina
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # auto_now_add: se crea la fecha al crear el registro
    creado_en = models.DateTimeField(default=timezone.now)

    # Oculta el campo creado_en
    def __str__(self):
        return self.nombre