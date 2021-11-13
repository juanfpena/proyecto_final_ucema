from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from .models import Cliente, Producto, Pedido
from django.views import View

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clientes = Cliente.objects.all()

        context['clientes'] = clientes

        return context


class RegistrarseView(TemplateView):
    template_name = 'main/registrarse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
