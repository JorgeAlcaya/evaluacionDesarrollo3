from django.contrib import admin
from .models import Cliente, Producto
# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
