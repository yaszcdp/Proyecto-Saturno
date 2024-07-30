from django.urls import path
from appcuentas import views
from appcuentas.views import index

urlpatterns = [
    path('', index, name='index'),
    path('clientes', views.ClienteListView.as_view(), name='clientes'),
    path('cliente', views.ClienteDetailView.as_view(), name='cliente'),
    path('nuevo-cliente', views.ClienteCreateView.as_view(), name='nuevo-cliente'),
    path('editar-cliente', views.ClienteUpdateView.as_view(), name='editar-cliente'),

    path('proveedores', views.ProveedorListView.as_view(), name='proveedores'),
    path('proveedor', views.ProveedorDetailView.as_view(), name='proveedor'),
    path('nuevo-proveedor', views.ProveedorCreateView.as_view(), name='nuevo-proveedor'),
    path('editar-proveedor', views.ProveedorUpdateView.as_view(), name='editar-proveedor'),

    path('productos', views.ProductoListView.as_view(), name='productos'),
    path('producto', views.ProductoDetailView.as_view(), name='producto'),
    path('nuevo-producto', views.ProductoCreateView.as_view(), name='nuevo-producto'),
    path('editar-producto', views.ProductoUpdateView.as_view(), name='editar-producto'),

]
