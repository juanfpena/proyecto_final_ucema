from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Cliente, Producto, Pedido
from django.views import View
from django.shortcuts import render

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
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
        return super().get_context_data(**kwargs)


class cargarPedido(View):
    template_name = 'main/pedidos/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        productos = Producto.objects.all()
        clientes = Cliente.objects.all()

        context['productos'] = productos
        context['clientes'] = clientes

        return context

    def get(self, *args, **kwargs):

        instance = ''

        context = {

        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        """
        Permite al usuario crear un registro de cliente.
        """

        nuevo_pedido = Pedido()

        context = {

        }

        return render(self.request, self.template_name, context)
