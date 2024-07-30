from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Cliente, Proveedor, Producto, Venta, Compra])
