"""
Sistema de Tienda Online
Ejemplo de Programación Orientada a Objetos (POO)

Este módulo demuestra los principios de POO mediante la creación de un sistema
de tienda online. Incluye clases para productos, clientes, carrito de compras y pedidos.
"""

from datetime import datetime
from typing import List, Optional
from enum import Enum


class EstadoPedido(Enum):
    """Enumeración para los estados posibles de un pedido."""
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class Producto:
    """
    Clase que representa un producto en la tienda.
    
    Atributos:
        id_producto: Identificador único del producto
        nombre: Nombre del producto
        descripcion: Descripción del producto
        precio: Precio del producto
        stock: Cantidad disponible en inventario
        categoria: Categoría del producto
    """
    
    contador_productos = 1
    
    def __init__(self, nombre: str, descripcion: str, precio: float, 
                 stock: int, categoria: str):
        """
        Inicializa un producto.
        
        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio unitario
            stock: Cantidad en inventario
            categoria: Categoría del producto
        """
        self.id_producto = Producto.contador_productos
        Producto.contador_productos += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    
    def reducir_stock(self, cantidad: int) -> bool:
        """
        Reduce el stock del producto.
        
        Args:
            cantidad: Cantidad a reducir
        
        Returns:
            True si se redujo exitosamente, False si no hay suficiente stock
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False
    
    def aumentar_stock(self, cantidad: int):
        """Aumenta el stock del producto."""
        self.stock += cantidad
    
    def esta_disponible(self, cantidad: int = 1) -> bool:
        """Verifica si hay suficiente stock disponible."""
        return self.stock >= cantidad
    
    def __str__(self) -> str:
        """Retorna una representación en string del producto."""
        return (f"[{self.id_producto}] {self.nombre} - ${self.precio:.2f} "
                f"(Stock: {self.stock})")


class Cliente:
    """
    Clase que representa un cliente de la tienda.
    
    Atributos:
        id_cliente: Identificador único del cliente
        nombre: Nombre del cliente
        email: Correo electrónico
        telefono: Número de teléfono
        direccion: Dirección de envío
        fecha_registro: Fecha de registro en la tienda
    """
    
    contador_clientes = 1000
    
    def __init__(self, nombre: str, email: str, telefono: str, direccion: str):
        """
        Inicializa un cliente.
        
        Args:
            nombre: Nombre del cliente
            email: Correo electrónico
            telefono: Número de teléfono
            direccion: Dirección de envío
        """
        self.id_cliente = Cliente.contador_clientes
        Cliente.contador_clientes += 1
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = datetime.now()
    
    def __str__(self) -> str:
        """Retorna una representación en string del cliente."""
        return f"Cliente #{self.id_cliente}: {self.nombre} ({self.email})"


class ItemCarrito:
    """
    Clase que representa un artículo en el carrito de compras.
    
    Atributos:
        producto: Objeto Producto
        cantidad: Cantidad de unidades
    """
    
    def __init__(self, producto: Producto, cantidad: int):
        """
        Inicializa un artículo del carrito.
        
        Args:
            producto: Objeto Producto
            cantidad: Cantidad de unidades
        """
        self.producto = producto
        self.cantidad = cantidad
    
    def calcular_subtotal(self) -> float:
        """Calcula el subtotal del artículo."""
        return self.producto.precio * self.cantidad
    
    def __str__(self) -> str:
        """Retorna una representación en string del artículo."""
        subtotal = self.calcular_subtotal()
        return (f"{self.producto.nombre} x{self.cantidad} - "
                f"${self.producto.precio:.2f} c/u = ${subtotal:.2f}")


class CarritoCompras:
    """
    Clase que representa el carrito de compras de un cliente.
    
    Atributos:
        cliente: Objeto Cliente propietario del carrito
        items: Lista de objetos ItemCarrito
    """
    
    def __init__(self, cliente: Cliente):
        """
        Inicializa un carrito de compras.
        
        Args:
            cliente: Objeto Cliente
        """
        self.cliente = cliente
        self.items: List[ItemCarrito] = []
    
    def agregar_producto(self, producto: Producto, cantidad: int) -> bool:
        """
        Agrega un producto al carrito.
        
        Args:
            producto: Objeto Producto
            cantidad: Cantidad a agregar
        
        Returns:
            True si se agregó exitosamente, False si no hay stock
        """
        if not producto.esta_disponible(cantidad):
            print(f"Error: No hay suficiente stock de {producto.nombre}")
            return False
        
        # Verificar si el producto ya está en el carrito
        for item in self.items:
            if item.producto.id_producto == producto.id_producto:
                item.cantidad += cantidad
                return True
        
        # Agregar nuevo item
        self.items.append(ItemCarrito(producto, cantidad))
        return True
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del carrito.
        
        Args:
            id_producto: ID del producto a eliminar
        
        Returns:
            True si se eliminó, False si no se encontró
        """
        for i, item in enumerate(self.items):
            if item.producto.id_producto == id_producto:
                self.items.pop(i)
                return True
        return False
    
    def calcular_total(self) -> float:
        """Calcula el total del carrito."""
        return sum(item.calcular_subtotal() for item in self.items)
    
    def vaciar_carrito(self):
        """Vacía el carrito de compras."""
        self.items.clear()
    
    def __str__(self) -> str:
        """Retorna una representación en string del carrito."""
        if not self.items:
            return "Carrito vacío"
        
        contenido = "\n".join(f"  {item}" for item in self.items)
        total = self.calcular_total()
        return f"Carrito de {self.cliente.nombre}:\n{contenido}\nTotal: ${total:.2f}"


class Pedido:
    """
    Clase que representa un pedido realizado.
    
    Atributos:
        id_pedido: Identificador único del pedido
        cliente: Objeto Cliente que realizó el pedido
        items: Lista de objetos ItemCarrito
        estado: Estado actual del pedido
        fecha_pedido: Fecha de creación del pedido
        total: Monto total del pedido
    """
    
    contador_pedidos = 5000
    
    def __init__(self, cliente: Cliente, items: List[ItemCarrito]):
        """
        Inicializa un pedido.
        
        Args:
            cliente: Objeto Cliente
            items: Lista de objetos ItemCarrito
        """
        self.id_pedido = Pedido.contador_pedidos
        Pedido.contador_pedidos += 1
        self.cliente = cliente
        self.items = items.copy()
        self.estado = EstadoPedido.PENDIENTE
        self.fecha_pedido = datetime.now()
        self.total = sum(item.calcular_subtotal() for item in self.items)
    
    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        """Cambia el estado del pedido."""
        self.estado = nuevo_estado
    
    def obtener_detalles(self) -> str:
        """Retorna los detalles completos del pedido."""
        detalles = f"\n{'='*60}\n"
        detalles += f"PEDIDO #{self.id_pedido}\n"
        detalles += f"Cliente: {self.cliente.nombre}\n"
        detalles += f"Email: {self.cliente.email}\n"
        detalles += f"Dirección: {self.cliente.direccion}\n"
        detalles += f"Fecha: {self.fecha_pedido.strftime('%d/%m/%Y %H:%M')}\n"
        detalles += f"Estado: {self.estado.value.upper()}\n"
        detalles += f"{'-'*60}\n"
        detalles += "PRODUCTOS:\n"
        
        for item in self.items:
            detalles += f"  {item}\n"
        
        detalles += f"{'-'*60}\n"
        detalles += f"TOTAL: ${self.total:.2f}\n"
        detalles += f"{'='*60}\n"
        
        return detalles
    
    def __str__(self) -> str:
        """Retorna una representación en string del pedido."""
        return (f"Pedido #{self.id_pedido} - {self.cliente.nombre} - "
                f"${self.total:.2f} - {self.estado.value}")


class Tienda:
    """
    Clase que representa la tienda online y gestiona sus operaciones.
    
    Atributos:
        nombre: Nombre de la tienda
        productos: Lista de objetos Producto
        clientes: Lista de objetos Cliente
        pedidos: Lista de objetos Pedido
    """
    
    def __init__(self, nombre: str):
        """
        Inicializa una tienda.
        
        Args:
            nombre: Nombre de la tienda
        """
        self.nombre = nombre
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []
        self.pedidos: List[Pedido] = []
    
    def agregar_producto(self, producto: Producto):
        """Agrega un producto al catálogo."""
        self.productos.append(producto)
    
    def registrar_cliente(self, cliente: Cliente):
        """Registra un nuevo cliente."""
        self.clientes.append(cliente)
    
    def buscar_producto_por_nombre(self, nombre: str) -> Optional[Producto]:
        """Busca un producto por nombre."""
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                return producto
        return None
    
    def crear_pedido(self, cliente: Cliente, carrito: CarritoCompras) -> Optional[Pedido]:
        """
        Crea un pedido a partir del carrito de compras.
        
        Args:
            cliente: Objeto Cliente
            carrito: Objeto CarritoCompras
        
        Returns:
            Objeto Pedido si es exitoso, None si hay error
        """
        if not carrito.items:
            print("Error: El carrito está vacío")
            return None
        
        # Verificar stock y reducir inventario
        for item in carrito.items:
            if not item.producto.reducir_stock(item.cantidad):
                print(f"Error: No hay suficiente stock de {item.producto.nombre}")
                return None
        
        # Crear pedido
        pedido = Pedido(cliente, carrito.items)
        self.pedidos.append(pedido)
        carrito.vaciar_carrito()
        
        return pedido
    
    def obtener_pedidos_por_cliente(self, cliente: Cliente) -> List[Pedido]:
        """Obtiene todos los pedidos de un cliente."""
        return [p for p in self.pedidos if p.cliente.id_cliente == cliente.id_cliente]
    
    def mostrar_catalogo(self):
        """Muestra el catálogo de productos."""
        print(f"\n{'='*60}")
        print(f"CATÁLOGO DE {self.nombre.upper()}")
        print(f"{'='*60}")
        
        categorias = set(p.categoria for p in self.productos)
        for categoria in sorted(categorias):
            print(f"\n{categoria.upper()}:")
            for producto in self.productos:
                if producto.categoria == categoria:
                    print(f"  {producto}")
        
        print(f"{'='*60}\n")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear tienda
    tienda = Tienda("TechStore Online")
    
    # Agregar productos
    tienda.agregar_producto(Producto("Laptop Dell", "Laptop 15 pulgadas", 899.99, 10, "Electrónica"))
    tienda.agregar_producto(Producto("Mouse Logitech", "Mouse inalámbrico", 29.99, 50, "Accesorios"))
    tienda.agregar_producto(Producto("Teclado Mecánico", "Teclado RGB", 79.99, 25, "Accesorios"))
    tienda.agregar_producto(Producto("Monitor LG", "Monitor 27 pulgadas 4K", 349.99, 8, "Electrónica"))
    tienda.agregar_producto(Producto("Cable HDMI", "Cable HDMI 2.1", 15.99, 100, "Cables"))
    
    # Mostrar catálogo
    tienda.mostrar_catalogo()
    
    # Registrar clientes
    cliente1 = Cliente("Ana Martínez", "ana@email.com", "555-1111", "Calle Principal 123")
    cliente2 = Cliente("Pedro Sánchez", "pedro@email.com", "555-2222", "Avenida Central 456")
    
    tienda.registrar_cliente(cliente1)
    tienda.registrar_cliente(cliente2)
    
    # Cliente 1 realiza compras
    print(f"\n{cliente1.nombre} está comprando...\n")
    carrito1 = CarritoCompras(cliente1)
    carrito1.agregar_producto(tienda.productos[0], 1)  # Laptop
    carrito1.agregar_producto(tienda.productos[1], 2)  # Mouse
    carrito1.agregar_producto(tienda.productos[4], 3)  # Cable HDMI
    
    print(carrito1)
    
    # Crear pedido
    pedido1 = tienda.crear_pedido(cliente1, carrito1)
    if pedido1:
        print(pedido1.obtener_detalles())
    
    # Cliente 2 realiza compras
    print(f"\n{cliente2.nombre} está comprando...\n")
    carrito2 = CarritoCompras(cliente2)
    carrito2.agregar_producto(tienda.productos[2], 1)  # Teclado
    carrito2.agregar_producto(tienda.productos[3], 1)  # Monitor
    
    print(carrito2)
    
    # Crear pedido
    pedido2 = tienda.crear_pedido(cliente2, carrito2)
    if pedido2:
        print(pedido2.obtener_detalles())
    
    # Cambiar estado de pedidos
    print("Procesando pedidos...")
    pedido1.cambiar_estado(EstadoPedido.PROCESANDO)
    pedido2.cambiar_estado(EstadoPedido.ENVIADO)
    
    # Mostrar pedidos de un cliente
    print(f"\nPedidos de {cliente1.nombre}:")
    for pedido in tienda.obtener_pedidos_por_cliente(cliente1):
        print(f"  {pedido}")
