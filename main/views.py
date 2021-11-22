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
    template_name = 'main/registro/registrarse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, *args, **kwargs):

        nuevo_cliente = Cliente()

        nuevo_cliente.nombre = self.request.POST.get('inputNombre', None)
        nuevo_cliente.apellido = self.request.POST.get('inputApellido', None)
        nuevo_cliente.email = self.request.POST.get('inputEmail', None)
        nuevo_cliente.direccion = self.request.POST.get('inputDireccion', None)
        nuevo_cliente.telefono = self.request.POST.get('inputTelefono', None)

        context = {
            'resultado': True
        }

        nuevo_cliente.save()

        return render(self.request, self.template_name, context)


class cargarPedido(TemplateView):
    template_name = 'main/pedidos/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        productos = Producto.objects.all()

        context['productos'] = productos

        return context
