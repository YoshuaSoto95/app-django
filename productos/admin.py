from django.contrib import admin
from .models import Categoria, Producto

# personalizar el administrador
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    # Oculta el campo creado_en
    exclude = ('creado_en',)
    # Despliga los campos en la lista de productos
    list_display = ('id', 'nombre', 'stock', 'puntaje', 'creado_en')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
