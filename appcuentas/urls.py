from django.urls import path
from appcuentas import views
from appcuentas.views import index

urlpatterns = [
    path('', index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('clientes', views.ClienteListView.as_view(), name='clientes'),
    path('ver-cliente/<int:pk>', views.ClienteDetailView.as_view(), name='ver-cliente'),
    path('nuevo-cliente', views.ClienteCreateView.as_view(), name='nuevo-cliente'),
    path('editar-cliente/<int:pk>', views.ClienteUpdateView.as_view(), name='editar-cliente'),
    path('eliminar-cliente/<int:pk>', views.ClienteDeleteView.as_view(), name='eliminar-cliente'),

    path('proveedores', views.ProveedorListView.as_view(), name='proveedores'),
    path('ver-proveedor/<int:pk>', views.ProveedorDetailView.as_view(), name='ver-proveedor'),
    path('nuevo-proveedor', views.ProveedorCreateView.as_view(), name='nuevo-proveedor'),
    path('editar-proveedor/<int:pk>', views.ProveedorUpdateView.as_view(), name='editar-proveedor'),
    path('eliminar-proveedor/<int:pk>', views.ProveedorDeleteView.as_view(), name='eliminar-proveedor'),

    path('productos', views.ProductoListView.as_view(), name='productos'),
    path('ver-producto/<int:pk>', views.ProductoDetailView.as_view(), name='ver-producto'),
    path('nuevo-producto', views.ProductoCreateView.as_view(), name='nuevo-producto'),
    path('editar-producto/<int:pk>', views.ProductoUpdateView.as_view(), name='editar-producto'),
    path('eliminar-producto/<int:pk>', views.ProductoDeleteView.as_view(), name='eliminar-producto'),

]
