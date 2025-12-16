"""
Sistema de Reservas de Hotel
Ejemplo de Programación Orientada a Objetos (POO)

Este módulo demuestra los principios de POO mediante la creación de un sistema
de reservas para un hotel. Incluye clases para habitaciones, huéspedes y reservas.
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Habitacion:
    """
    Clase que representa una habitación en el hotel.
    
    Atributos:
        numero: Número único de la habitación
        tipo: Tipo de habitación (simple, doble, suite)
        precio_noche: Precio por noche en dólares
        disponible: Estado de disponibilidad de la habitación
    """
    
    def __init__(self, numero: int, tipo: str, precio_noche: float):
        """
        Inicializa una habitación con sus características.
        
        Args:
            numero: Número único de la habitación
            tipo: Tipo de habitación
            precio_noche: Precio por noche
        """
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.disponible = True
    
    def marcar_ocupada(self):
        """Marca la habitación como ocupada."""
        self.disponible = False
    
    def marcar_disponible(self):
        """Marca la habitación como disponible."""
        self.disponible = True
    
    def __str__(self) -> str:
        """Retorna una representación en string de la habitación."""
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio_noche}/noche - {estado}"


class Huesped:
    """
    Clase que representa un huésped del hotel.
    
    Atributos:
        nombre: Nombre completo del huésped
        email: Correo electrónico del huésped
        telefono: Número de teléfono del huésped
        documento: Número de documento de identidad
    """
    
    def __init__(self, nombre: str, email: str, telefono: str, documento: str):
        """
        Inicializa un huésped con sus datos personales.
        
        Args:
            nombre: Nombre del huésped
            email: Correo electrónico
            telefono: Número de teléfono
            documento: Número de documento
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento = documento
    
    def __str__(self) -> str:
        """Retorna una representación en string del huésped."""
        return f"{self.nombre} (Doc: {self.documento})"


class Reserva:
    """
    Clase que representa una reserva de habitación.
    
    Atributos:
        id_reserva: Identificador único de la reserva
        huesped: Objeto Huesped que realiza la reserva
        habitacion: Objeto Habitacion reservada
        fecha_entrada: Fecha de entrada (datetime)
        fecha_salida: Fecha de salida (datetime)
        estado: Estado de la reserva (confirmada, cancelada, completada)
    """
    
    contador_reservas = 1000  # Contador para generar IDs únicos
    
    def __init__(self, huesped: Huesped, habitacion: Habitacion, 
                 fecha_entrada: datetime, fecha_salida: datetime):
        """
        Inicializa una reserva.
        
        Args:
            huesped: Objeto Huesped
            habitacion: Objeto Habitacion
            fecha_entrada: Fecha de entrada
            fecha_salida: Fecha de salida
        """
        self.id_reserva = Reserva.contador_reservas
        Reserva.contador_reservas += 1
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = "confirmada"
        self.fecha_reserva = datetime.now()
    
    def calcular_noches(self) -> int:
        """Calcula el número de noches de la reserva."""
        return (self.fecha_salida - self.fecha_entrada).days
    
    def calcular_costo_total(self) -> float:
        """Calcula el costo total de la reserva."""
        noches = self.calcular_noches()
        return noches * self.habitacion.precio_noche
    
    def cancelar(self):
        """Cancela la reserva y libera la habitación."""
        self.estado = "cancelada"
        self.habitacion.marcar_disponible()
    
    def completar(self):
        """Marca la reserva como completada."""
        self.estado = "completada"
        self.habitacion.marcar_disponible()
    
    def __str__(self) -> str:
        """Retorna una representación en string de la reserva."""
        noches = self.calcular_noches()
        costo = self.calcular_costo_total()
        return (f"Reserva #{self.id_reserva} - {self.huesped.nombre} - "
                f"Habitación {self.habitacion.numero} - {noches} noches - "
                f"${costo:.2f} - Estado: {self.estado}")


class Hotel:
    """
    Clase que representa un hotel y gestiona sus operaciones.
    
    Atributos:
        nombre: Nombre del hotel
        habitaciones: Lista de objetos Habitacion
        reservas: Lista de objetos Reserva
    """
    
    def __init__(self, nombre: str):
        """
        Inicializa un hotel.
        
        Args:
            nombre: Nombre del hotel
        """
        self.nombre = nombre
        self.habitaciones: List[Habitacion] = []
        self.reservas: List[Reserva] = []
    
    def agregar_habitacion(self, habitacion: Habitacion):
        """Agrega una habitación al hotel."""
        self.habitaciones.append(habitacion)
    
    def obtener_habitaciones_disponibles(self, tipo: Optional[str] = None) -> List[Habitacion]:
        """
        Obtiene las habitaciones disponibles, opcionalmente filtradas por tipo.
        
        Args:
            tipo: Tipo de habitación (opcional)
        
        Returns:
            Lista de habitaciones disponibles
        """
        disponibles = [h for h in self.habitaciones if h.disponible]
        if tipo:
            disponibles = [h for h in disponibles if h.tipo == tipo]
        return disponibles
    
    def realizar_reserva(self, huesped: Huesped, habitacion: Habitacion,
                        fecha_entrada: datetime, fecha_salida: datetime) -> Optional[Reserva]:
        """
        Realiza una reserva si la habitación está disponible.
        
        Args:
            huesped: Objeto Huesped
            habitacion: Objeto Habitacion
            fecha_entrada: Fecha de entrada
            fecha_salida: Fecha de salida
        
        Returns:
            Objeto Reserva si es exitosa, None si falla
        """
        if not habitacion.disponible:
            print(f"Error: La habitación {habitacion.numero} no está disponible.")
            return None
        
        if fecha_salida <= fecha_entrada:
            print("Error: La fecha de salida debe ser posterior a la de entrada.")
            return None
        
        reserva = Reserva(huesped, habitacion, fecha_entrada, fecha_salida)
        habitacion.marcar_ocupada()
        self.reservas.append(reserva)
        return reserva
    
    def obtener_reservas_activas(self) -> List[Reserva]:
        """Obtiene todas las reservas activas (confirmadas)."""
        return [r for r in self.reservas if r.estado == "confirmada"]
    
    def mostrar_estado(self):
        """Muestra el estado actual del hotel."""
        print(f"\n{'='*60}")
        print(f"Hotel: {self.nombre}")
        print(f"{'='*60}")
        print(f"\nHabitaciones ({len(self.habitaciones)} total):")
        for habitacion in self.habitaciones:
            print(f"  {habitacion}")
        
        print(f"\nReservas Activas ({len(self.obtener_reservas_activas())} total):")
        for reserva in self.obtener_reservas_activas():
            print(f"  {reserva}")
        print(f"{'='*60}\n")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear hotel
    hotel = Hotel("Hotel Paradise")
    
    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "simple", 50.0))
    hotel.agregar_habitacion(Habitacion(102, "doble", 75.0))
    hotel.agregar_habitacion(Habitacion(103, "doble", 75.0))
    hotel.agregar_habitacion(Habitacion(201, "suite", 150.0))
    
    # Crear huéspedes
    huesped1 = Huesped("Juan García", "juan@email.com", "555-1234", "12345678")
    huesped2 = Huesped("María López", "maria@email.com", "555-5678", "87654321")
    huesped3 = Huesped("Carlos Rodríguez", "carlos@email.com", "555-9999", "11223344")
    
    # Realizar reservas
    fecha_entrada = datetime(2025, 12, 20)
    fecha_salida = datetime(2025, 12, 25)
    
    reserva1 = hotel.realizar_reserva(huesped1, hotel.habitaciones[0], fecha_entrada, fecha_salida)
    reserva2 = hotel.realizar_reserva(huesped2, hotel.habitaciones[1], fecha_entrada, fecha_salida)
    reserva3 = hotel.realizar_reserva(huesped3, hotel.habitaciones[3], fecha_entrada, fecha_salida)
    
    # Mostrar estado del hotel
    hotel.mostrar_estado()
    
    # Intentar reservar una habitación ocupada
    print("Intentando reservar habitación ocupada...")
    hotel.realizar_reserva(huesped1, hotel.habitaciones[0], fecha_entrada, fecha_salida)
    
    # Cancelar una reserva
    print("\nCancelando reserva #1001...")
    reserva2.cancelar()
    
    # Mostrar estado actualizado
    hotel.mostrar_estado()
