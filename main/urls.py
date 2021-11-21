from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='main_index'),
    path('registrarse', views.RegistrarseView.as_view(), name='main_registrarse'),
    path('producto/<int:pk>/', views.verProducto.as_view(), name='ver_producto'),
    path('cargar_pedido', views.cargarPedido.as_view(), name='cargar_pedido')
]
