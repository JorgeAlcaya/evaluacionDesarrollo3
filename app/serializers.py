from .models import Producto
from rest_framework import serializers

# esta clase nos permitira convertir el
# objeto en json y viceversa para la transmición de datos
# a traves de la API

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        