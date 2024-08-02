#PROYECTO SATURNO

## Administrador de Negocios

Este es un proyecto de ejemplo desarrollado durante el curso de Python en Coder House. El proyecto está hecho con Django utilizando el patrón Models-Template-View (MTV) y consiste en un administrador de negocios que (por el momento) permite la gestión de Proveedores, Clientes y Productos.


## Descripción del Proyecto

El administrador de negocios permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) para tres entidades principales:
- **Proveedor**
- **Cliente**
- **Producto**

Cada una de estas entidades tiene sus propias vistas y formularios para gestionar la información de manera eficiente.


## Tecnologías Utilizadas

- **Lenguaje de programación**: Python
- **Framework**: Django
- **Base de datos**: SQLite (puede ser cambiada a otra base de datos según las necesidades)
- **Frontend**: HTML, CSS (Bootstrap)


## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/yaszcdp/Proyecto-Saturno.git
    cd Proyecto-Saturno
    code .
    ```

2. Aplicar las migraciones y ejecutar el servidor de desarrollo:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

3. Acceder a la aplicación en el navegador en `http://127.0.0.1:8000`.
   

## Uso

### Proveedores

- Crear nuevo proveedor: `/nuevo-proveedor`
- Listar proveedores: `/proveedores`
- Ver proveedor: `/ver-proveedor/<id>`
- Editar proveedor: `/editar-proveedores/<id>`
- Eliminar proveedor: `/eliminar-proveedor/<id>`

### Clientes

- Crear nuevo cliente: `/nuevo-cliente`
- Listar clientes: `/clientes`
- Ver cliente: `/ver-cliente/<id>`
- Editar cliente: `/editar-cliente/<id>`
- Eliminar cliente: `/eliminar-cliente/<id>`

### Productos

- Crear nuevo producto: `/nuevo-producto`
- Listar productos: `/productos`
- Ver producto: `/ver-producto/<id>`
- Editar producto: `/editar-producto/<id>`
- Eliminar producto: `/eliminar-producto/<id>`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cualquier cambio importante antes de realizarlo.

