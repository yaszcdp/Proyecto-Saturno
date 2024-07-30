from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'appcuentas/listar_clientes.html', {'clientes': clientes})