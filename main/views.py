from typing import Any, ContextManager
from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Cliente, Producto, Pedido
from django.views import View
from django.shortcuts import render, get_list_or_404
import datetime as dt

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        clientes = Cliente.objects.all()

        context['clientes'] = clientes

        return context


class RegistrarseView(View):
    template_name = 'main/registro/registrarse.html'

    def get(self, *args, **kwargs):

        context = {

        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        """
        Permite al usuario crear un registro de cliente.
        """

        nuevo_cliente = Cliente()

        nuevo_cliente.nombre = self.request.POST.get('inputNombre', None)
        nuevo_cliente.apellido = self.request.POST.get('inputApellido', None)
        nuevo_cliente.email = self.request.POST.get('inputEmail', None)
        nuevo_cliente.direccion = self.request.POST.get('inputDireccion', None)
        nuevo_cliente.telefono = self.request.POST.get('inputTelefono', None)

        nuevo_cliente.save()

        context = {
            'resultado': True
        }

        return render(self.request, self.template_name, context)


class registroCompletado(TemplateView):
    template_name = 'main/registro/registracion_concretada.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class verProductos(View):
    template_name = 'main/pedidos/producto.html'

    def get(self, *args, **kwargs):
        """
        Obtiene los objetos "Producto" con el fin de ser representados en la plantilla.
        """

        instance = get_list_or_404(Producto)

        context = {
            'productos': instance
        }

        return render(self.request, self.template_name, context)


class realizarPedido(View):
    template_name = 'main/pedidos/realizar_pedido.html'

    def get(self, *args, **kwargs: Any):
        """
        Obtiene los modelos de clientes y productos.
        """

        clientes = get_list_or_404(Cliente)
        productos = get_list_or_404(Producto)

        context = {
            'clientes': clientes,
            'productos': productos
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs: Any):
        """
        Genera un nuevo listado de productos para un cliente particular.
        """

        nuevo_pedido = Pedido()

        client_id = self.request.POST.get('seleccionCliente', None)
        cliente_instance = Cliente.objects.get(id=client_id)
        nuevo_pedido.cliente.add(cliente_instance)

        nuevo_pedido.fecha_y_hora = dt.datetime.now()

        productos = get_list_or_404(Producto)

        for producto in productos:
            quantity = max(self.request.POST.get('Q_' + str(producto.id)), 0)
            producto_instance = Producto.objects.get(id=producto.id)

            if quantity > 0:

                for i in range(quantity):
                    nuevo_pedido.lista_productos.add(producto_instance)

            continue

        nuevo_pedido.save()

        context = {
            "grabacion": True
        }

        return render(self.request, self.template_name, context)
