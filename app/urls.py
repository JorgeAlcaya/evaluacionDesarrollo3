from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Producto, Cliente
from django.contrib.auth.views import LoginView,LogoutView

#---------- rutas de la API ----------------------------
urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#---------- rutas de la app ----------------------------
urlpatterns += [   
    path('', views.index),
    path('quienes', views.quienes),
    path('nba', views.nba),
    path('finalFantasy', views.finalFantasy),
    path('blairWitch', views.blairWitch),
    path('ingresarProducto', views.ingresarProducto),
    path('ingresarCliente', views.ingresarCliente),
    path('listarProductosFull', views.listarProductosFull),
    path('listarClientesFull', views.listarClientesFull),
    path('editarProducto/<int:producto_id>', views.editarProducto),
    path('editarCliente/<int:cliente_id>', views.editarCliente),
    path('borrarProducto/<int:producto_id>', views.borrarProducto),
    path('borrarCliente/<int:cliente_id>', views.borrarCliente),
    path('listarProductos', views.listarProductos),
     path('listarClientes', views.listarClientes),
    path('inicio', views.inicio),
    
]

#---------- login ----------------------------
urlpatterns+= [
     
    #path('',views.indexView,name='home'),
    #path('dashboard/',views.dashboardView,name='dashboard'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('register/',views.registerView,name='register_url'),
    path('logout/',LogoutView.as_view(),name='logout_url'),
]