from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from .models import Cliente, Producto, Pedido
from django.views import View
from django.shortcuts import get_object_or_404, render

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clientes = Cliente.objects.all()

        context['clientes'] = clientes

        return context


class RegistrarseView(TemplateView):
    template_name = 'registrarse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class verProducto(TemplateView):
    template_name = 'cargar_pedido.html'

    def get(self, *args, **kwargs):
        instance = get_object_or_404(Producto, pk=self.kwargs['pk'])

        context = {'producto': instance}

        return render(self.request, self.template_name, context)


class cargarPedido(TemplateView):
    template_name = 'producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        productos = Producto.objects.all()

        context['productos'] = productos

        return context
