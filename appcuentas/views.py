from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "appcuentas/index.html")


def buscar(request):
    query = request.GET.get('query', '')
    page = request.GET.get('page', '')

    if page == 'productos':
        productos = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'appcuentas/listar-productos.html', {'productos': productos})
    elif page == 'clientes':
        clientes = Cliente.objects.filter(nombre__icontains=query) | Cliente.objects.filter(apellido__icontains=query)
        return render(request, 'appcuentas/listar-clientes.html', {'clientes': clientes})
    elif page == 'proveedores':
        proveedores = Proveedor.objects.filter(empresa__icontains=query)
        return render(request, 'appcuentas/listar-proveedores.html', {'proveedores': proveedores})
    else:
        response = "No hay resultados"
        return HttpResponse(response)

#-------[ VISTAS CLIENTES ]-------
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'appcuentas/listar-clientes.html'

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    #context_object_name = 'cliente'
    template_name = 'appcuentas/ver-cliente.html'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'appcuentas/nuevo-cliente.html'
    fields = ['nombre', 'apellido', 'cuit', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'appcuentas/editar-cliente.html'
    fields = ['nombre', 'apellido', 'cuit', 'telefono']
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'appcuentas/eliminar-cliente.html'
    success_url = reverse_lazy('clientes')



#-------[ VISTAS PROVEEDORES ]-------
class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    context_object_name = 'proveedores'
    template_name = 'appcuentas/listar-proveedores.html'

class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    #context_object_name = 'proveedor'
    template_name = 'appcuentas/ver-proveedor.html'

class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'appcuentas/nuevo-proveedor.html'
    fields = ['empresa', 'telefono']
    success_url = reverse_lazy('proveedores')

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'appcuentas/editar-proveedor.html'
    fields = ['empresa', 'telefono']
    success_url = reverse_lazy('proveedores')

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'appcuentas/eliminar-proveedor.html'
    success_url = reverse_lazy('proveedores')



#-------[ VISTAS PRODUCTOS ]-------
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'appcuentas/listar-productos.html'

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    #context_object_name = 'producto'
    template_name = 'appcuentas/ver-producto.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'appcuentas/nuevo-producto.html'
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('productos')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'appcuentas/editar-producto.html'
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('productos')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'appcuentas/eliminar-producto.html'
    success_url = reverse_lazy('productos')

