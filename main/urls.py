from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='main_index'),
    path('registrarse', views.RegistrarseView.as_view(), name='main_registrarse'),
    path('listado_productos', views.verProductos.as_view(),
         name='listado_productos'),
    path('registracion_completada', views.registroCompletado.as_view(),
         name='registracion_completada'),
    path('realizar_pedido', views.realizarPedido.as_view(), name='realizar_pedido')
]
