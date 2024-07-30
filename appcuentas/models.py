from django.db import models

# Create your models here.

#-----------------[ MODELOS PERSONA ]-----------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cuit = models.CharField(max_length=13)
    telefono = models.CharField(max_length=20)
    #cta_cte = models.ManyToManyField('Venta')
    deuda = models.FloatField(default=0.0, decimal_places=2)

    def __str__(self):
        return f"Nombre: {self.nombre} — Apellido: {self.apellido} — Cuit: {self.cuit} — Teléfono: {self.telefono} — Total Deuda: ${self.deuda}"
    
    def calcular_deuda(self):
        self.deuda = sum(venta.monto for venta in self.ventas.all())
        self.save()
    

class Proveedor(models.Model):
    empresa = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    #cta_cte = models.ManyToManyField('Compra')
    deuda = models.FloatField(default=0.0, decimal_places=2)

    def __str__(self):
        return f"Empresa: {self.empresa} — Teléfono: {self.telefono} — Total Adeudado: ${self.deuda}"
    
    def calcular_deuda(self):
        self.deuda = sum(compra.monto for compra in self.compras.all())
        self.save()

#-----------------[ MODELO PRODUCTO ]-----------------
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()

    def __str__(self):
        return f"Nombre: {self.nombre} — Precio: ${self.precio}"


#-----------------[ MODELOS REMITO (COMPRA Y VENTA) ]-----------------
class Remito(models.Model):
    fecha = models.DateField()
    monto = models.FloatField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField('Producto', through='ProductoRemito')

    def agregar_producto(self, producto, cantidad):
        producto_remito, created = ProductoRemito.objects.get_or_create(remito=self, producto=producto)
        if not created:
            producto_remito.cantidad += cantidad
        else:
            producto_remito.cantidad = cantidad
        producto_remito.save()
        self.monto = self.calcular_total()
        self.save()

    def calcular_total(self):
        return sum(producto_remito.cantidad * producto_remito.producto.precio for producto_remito in self.productoremito_set.all())

    def __str__(self):
        return f"Remito: {self.id} — Monto: {self.monto}"
    

class ProductoRemito(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    remito = models.ForeignKey(Remito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} = {self.cantidad * self.producto.precio}"

class Venta(Remito):
    estado = models.CharField(max_length=20, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=20, blank=True, null=True)
    apellido_cliente = models.CharField(max_length=20, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')

    def cargar_venta(self):
        if self.estado == 'Pendiente de pago':
            cliente = Cliente.objects.filter(nombre=self.nombre_cliente, apellido=self.apellido_cliente).first()
            if cliente:
                self.cliente = cliente
                self.save()
                cliente.calcular_deuda()
            else:
                print("Cliente no encontrado.")
        elif self.estado == 'Pagado':
            print("Venta pagada.")

    def __str__(self):
        return f"Venta: {self.id} — Monto: {self.monto}"

class Compra(Remito):
    proveedor = models.CharField(max_length=20, blank=True, null=True)

    def cargar_compra(self):
        proveedor = Proveedor.objects.filter(empresa=self.proveedor).first()
        if proveedor:
            self.save()
            proveedor.calcular_deuda()
        else:
            raise ValueError ("Proveedor no encontrado.")