from django import forms
from .models import Producto, Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'clasificacion', 'precio', ]
        labels = {'nombre': 'Nombre', 'descripcion': 'Descripcion Producto',
                  'precio': 'Precio Producto', 'clasificacion': 'Clasificación'}
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                   'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
                   'precio': forms.TextInput(attrs={'class': 'form-control'}), }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['producto', 'rut', 'nombre', 'apellido_paterno', 'apellido_materno',
                  'telefono', 'domicilio', 'region', 'comuna', 'fecha_nacimiento', ]
        labels = {'producto': 'Producto', 'rut': 'Rut', 'nombre': 'Nombre', 'apellido_paterno': 'Apellido Paterno', 'apellido_materno': 'Apellido materno', 'telefono': 'Teléfono',
                  'domicilio': 'Domicilio', 'region': 'Región', 'comuna': 'Comuna', 'fecha_nacimiento': 'Fecha de Nacimiento'}
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'class': 'datepicker'}), }