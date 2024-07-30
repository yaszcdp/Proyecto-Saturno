from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "appcuentas/index.html")


#-------[ VISTAS CLIENTES ]-------
class ClienteListView(ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'appcuentas/listar-clientes.html'

class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'appcuentas/ver-cliente.html'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'appcuentas/nuevo-cliente.html'
    fields = ['nombre', 'direccion', 'cuit', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'appcuentas/editar-cliente.html'
    fields = ['nombre', 'direccion', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')



#-------[ VISTAS PROVEEDORES ]-------
class ProveedorListView(ListView):
    model = Proveedor
    context_object_name = 'proveedores'
    template_name = 'appcuentas/listar-proveedores.html'

class ProveedorDetailView(DetailView):
    model = Proveedor
    context_object_name = 'proveedor'
    template_name = 'appcuentas/ver-proveedor.html'

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'appcuentas/nuevo-proveedor.html'
    fields = ['empresa', 'telefono']
    success_url = reverse_lazy('proveedores')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'appcuentas/editar-proveedor.html'
    fields = ['empresa', 'telefono']
    success_url = reverse_lazy('proveedores')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')



#-------[ VISTAS PRODUCTOS ]-------
class ProductoListView(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'appcuentas/listar-productos.html'

class ProductoDetailView(DetailView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'appcuentas/ver-producto.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'appcuentas/nuevo-producto.html'
    fields = ['nombre', 'precio', 'stock']
    success_url = reverse_lazy('productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'appcuentas/editar-producto.html'
    fields = ['nombre', 'precio', 'stock']
    success_url = reverse_lazy('productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

