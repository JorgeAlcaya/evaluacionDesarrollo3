from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
# ---importamos nuestras estruras ---------------
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
#_________________ PARA USER ________________________________
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView
#_________________ PARA API ________________________________
from .serializers import ProductoSerializer
from rest_framework import generics

#_____________________________________________________________
class API_objects(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

# Create your views here.

#login


def registerView(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})


#login
def cliente_list(request):
    return render(request, 'app/cliente_list.html', {})

#logout
def logout(request):
    if request.method=='POST':
        form = LogoutView(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})



def index(request):
    return render(request, 'app/index.html', {})


def quienes(request):
    return render(request, 'app/quienes.html', {})


def nba(request):
    return render(request, 'app/nba.html', {})

def inicio(request):
    return render(request, 'registration/inicio.html', {})


def finalFantasy(request):
    return render(request, 'app/finalFantasy.html', {})


def blairWitch(request):
    return render(request, 'app/blairWitch.html', {})

#--------------ingresar producto
@login_required
def ingresarProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/ingresarProducto')
    else:
        form = ProductoForm()
        return render(request, 'app/ingresarProducto.html', {'form': form})


#--------------ingresar cliente
@login_required
def ingresarCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/ingresarCliente')
    else:
        form = ClienteForm()
        return render(request, 'app/ingresarCliente.html', {'formCliente': form})



#------------------editar productos
@login_required
def editarProducto(request, producto_id):
    # Recuperamos el objeto asociado al id
    instancia = Producto.objects.get(id=producto_id)
    # creamos un formulario que contenta los datos del registros recuperado
    form = ProductoForm(instance=instancia)

    #Comprobamos que sea enviado el formulario
    
    if request.method =="POST":
        form= ProductoForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editarProducto.html",{'form':form})
         
@login_required   
def borrarProducto(request, producto_id):
    instancia = Producto.objects.get(id=producto_id)
    instancia.delete()
    return redirect("/listarProductosFull")   #--> al raiz de las páginas


#------------------editar clientes
@login_required
def editarCliente(request, cliente_id):
    # Recuperamos el objeto asociado al id
    instancia = Cliente.objects.get(id=cliente_id)
    # creamos un formulario que contenta los datos del registros recuperado
    form = ClienteForm(instance=instancia)

    #Comprobamos que sea enviado el formulario
    
    if request.method =="POST":
        form= ClienteForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editarCliente.html",{'form':form})
         
@login_required   
def borrarCliente(request, cliente_id):
    instancia = Cliente.objects.get(id=cliente_id)
    instancia.delete()
    return redirect("/listarClientesFull")   #--> al raiz de las páginas


# ------------------listar Clientes
@login_required
def listarClientes(request):
    cliente = Cliente.objects.all()
    return render(request, "app/listarClientes.html", {'cliente': cliente})
@login_required
def listarClientesFull(request):
    cliente = Cliente.objects.all()
    return render(request, "app/listarClientesFull.html", {'cliente': cliente})
    
    
    
    
# ------------------filtros
@login_required
def listarProductos(request):
    producto = Producto.objects.all()
    precio = 0  # Filtro por defecto

    if request.POST.get('precio'):
        precio = int(request.POST.get('precio'))
        producto = producto.filter(precio__exact=precio)

    if request.POST.get('clasificacion'):
        clasificacion = request.POST.get('clasificacion')
        producto = producto.filter(clasificacion__exact=clasificacion)

    return render(request, "app/listarProductos.html", {'producto': producto})



@login_required
def listarProductosFull(request):
    producto = Producto.objects.all()
    precio = 0  # Filtro por defecto

    if request.POST.get('precio'):
        precio = int(request.POST.get('precio'))
        producto = producto.filter(precio__exact=precio)

    if request.POST.get('clasificacion'):
        clasificacion = request.POST.get('clasificacion')
        producto = producto.filter(clasificacion__exact=clasificacion)

    return render(request, "app/listarProductosFull.html", {'producto': producto})



# @login_required
# def listarProductos(request):
#     # creamos una variable que será colección y carga TODOS los registros
#     producto = Producto.objects.all()
#     # renderizamos la colección en el template: listar_carreras.html
#     return render(request, "app/listarProductos.html",
#                   {'producto': producto})