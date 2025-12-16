"""
Sistema de Gestión de Biblioteca
Ejemplo de Programación Orientada a Objetos (POO)

Este módulo demuestra los principios de POO mediante la creación de un sistema
de gestión de biblioteca. Incluye clases para libros, miembros, préstamos y multas.
"""

from datetime import datetime, timedelta
from typing import List, Optional
from enum import Enum


class EstadoLibro(Enum):
    """Enumeración para los estados posibles de un libro."""
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    MANTENIMIENTO = "mantenimiento"


class Genero(Enum):
    """Enumeración para los géneros literarios."""
    FICCION = "ficción"
    NO_FICCION = "no ficción"
    CIENCIA = "ciencia"
    HISTORIA = "historia"
    INFANTIL = "infantil"
    POESIA = "poesía"
    DRAMA = "drama"


class Libro:
    """
    Clase que representa un libro en la biblioteca.
    
    Atributos:
        isbn: Código ISBN único del libro
        titulo: Título del libro
        autor: Autor del libro
        genero: Género literario
        año_publicacion: Año de publicación
        estado: Estado actual del libro
        numero_copias: Número de copias disponibles
    """
    
    def __init__(self, isbn: str, titulo: str, autor: str, 
                 genero: Genero, año_publicacion: int, numero_copias: int = 1):
        """
        Inicializa un libro.
        
        Args:
            isbn: Código ISBN
            titulo: Título del libro
            autor: Autor del libro
            genero: Género del libro
            año_publicacion: Año de publicación
            numero_copias: Número de copias disponibles
        """
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_publicacion = año_publicacion
        self.numero_copias = numero_copias
        self.estado = EstadoLibro.DISPONIBLE
    
    def prestar_copia(self) -> bool:
        """
        Presta una copia del libro.
        
        Returns:
            True si se prestó exitosamente, False si no hay copias disponibles
        """
        if self.numero_copias > 0:
            self.numero_copias -= 1
            if self.numero_copias == 0:
                self.estado = EstadoLibro.PRESTADO
            return True
        return False
    
    def devolver_copia(self):
        """Devuelve una copia del libro."""
        self.numero_copias += 1
        if self.numero_copias > 0:
            self.estado = EstadoLibro.DISPONIBLE
    
    def esta_disponible(self) -> bool:
        """Verifica si el libro está disponible para préstamo."""
        return self.numero_copias > 0
    
    def __str__(self) -> str:
        """Retorna una representación en string del libro."""
        return (f'"{self.titulo}" por {self.autor} ({self.año_publicacion}) '
                f'- {self.genero.value} - Copias: {self.numero_copias}')


class Miembro:
    """
    Clase que representa un miembro de la biblioteca.
    
    Atributos:
        id_miembro: Identificador único del miembro
        nombre: Nombre del miembro
        email: Correo electrónico
        telefono: Número de teléfono
        fecha_registro: Fecha de registro
        activo: Estado de actividad del miembro
    """
    
    contador_miembros = 1
    
    def __init__(self, nombre: str, email: str, telefono: str):
        """
        Inicializa un miembro.
        
        Args:
            nombre: Nombre del miembro
            email: Correo electrónico
            telefono: Número de teléfono
        """
        self.id_miembro = Miembro.contador_miembros
        Miembro.contador_miembros += 1
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
        self.activo = True
    
    def __str__(self) -> str:
        """Retorna una representación en string del miembro."""
        estado = "Activo" if self.activo else "Inactivo"
        return f"Miembro #{self.id_miembro}: {self.nombre} ({self.email}) - {estado}"


class Prestamo:
    """
    Clase que representa un préstamo de libro.
    
    Atributos:
        id_prestamo: Identificador único del préstamo
        miembro: Objeto Miembro que realiza el préstamo
        libro: Objeto Libro prestado
        fecha_prestamo: Fecha del préstamo
        fecha_vencimiento: Fecha de vencimiento del préstamo
        fecha_devolucion: Fecha de devolución (None si aún está prestado)
        renovaciones: Número de renovaciones realizadas
    """
    
    contador_prestamos = 1
    DIAS_PRESTAMO = 14  # Duración estándar del préstamo
    MAX_RENOVACIONES = 2  # Máximo número de renovaciones
    
    def __init__(self, miembro: Miembro, libro: Libro):
        """
        Inicializa un préstamo.
        
        Args:
            miembro: Objeto Miembro
            libro: Objeto Libro
        """
        self.id_prestamo = Prestamo.contador_prestamos
        Prestamo.contador_prestamos += 1
        self.miembro = miembro
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        self.fecha_devolucion = None
        self.renovaciones = 0
    
    def renovar(self) -> bool:
        """
        Renueva el préstamo.
        
        Returns:
            True si se renovó exitosamente, False si se alcanzó el máximo de renovaciones
        """
        if self.renovaciones < self.MAX_RENOVACIONES:
            self.renovaciones += 1
            self.fecha_vencimiento = datetime.now() + timedelta(days=self.DIAS_PRESTAMO)
            return True
        return False
    
    def devolver(self):
        """Registra la devolución del libro."""
        self.fecha_devolucion = datetime.now()
    
    def esta_vencido(self) -> bool:
        """Verifica si el préstamo está vencido."""
        if self.fecha_devolucion:
            return False
        return datetime.now() > self.fecha_vencimiento
    
    def calcular_dias_restantes(self) -> int:
        """Calcula los días restantes para la devolución."""
        if self.fecha_devolucion:
            return 0
        dias = (self.fecha_vencimiento - datetime.now()).days
        return max(0, dias)
    
    def __str__(self) -> str:
        """Retorna una representación en string del préstamo."""
        estado = "Devuelto" if self.fecha_devolucion else "Activo"
        dias_restantes = self.calcular_dias_restantes()
        return (f"Préstamo #{self.id_prestamo} - {self.miembro.nombre} - "
                f'"{self.libro.titulo}" - {estado} - '
                f"Días restantes: {dias_restantes}")


class Multa:
    """
    Clase que representa una multa por retraso en la devolución.
    
    Atributos:
        id_multa: Identificador único de la multa
        prestamo: Objeto Prestamo asociado
        monto: Monto de la multa
        pagada: Estado de pago de la multa
        fecha_creacion: Fecha de creación de la multa
    """
    
    contador_multas = 1
    TARIFA_DIARIA = 1.50  # Tarifa por día de retraso
    
    def __init__(self, prestamo: Prestamo, dias_retraso: int):
        """
        Inicializa una multa.
        
        Args:
            prestamo: Objeto Prestamo
            dias_retraso: Número de días de retraso
        """
        self.id_multa = Multa.contador_multas
        Multa.contador_multas += 1
        self.prestamo = prestamo
        self.monto = dias_retraso * self.TARIFA_DIARIA
        self.pagada = False
        self.fecha_creacion = datetime.now()
    
    def pagar(self):
        """Registra el pago de la multa."""
        self.pagada = True
    
    def __str__(self) -> str:
        """Retorna una representación en string de la multa."""
        estado = "Pagada" if self.pagada else "Pendiente"
        return (f"Multa #{self.id_multa} - {self.prestamo.miembro.nombre} - "
                f"${self.monto:.2f} - {estado}")


class Biblioteca:
    """
    Clase que representa la biblioteca y gestiona sus operaciones.
    
    Atributos:
        nombre: Nombre de la biblioteca
        libros: Diccionario de libros (ISBN -> Libro)
        miembros: Lista de miembros
        prestamos: Lista de préstamos
        multas: Lista de multas
    """
    
    def __init__(self, nombre: str):
        """
        Inicializa una biblioteca.
        
        Args:
            nombre: Nombre de la biblioteca
        """
        self.nombre = nombre
        self.libros = {}  # ISBN -> Libro
        self.miembros: List[Miembro] = []
        self.prestamos: List[Prestamo] = []
        self.multas: List[Multa] = []
    
    def agregar_libro(self, libro: Libro):
        """Agrega un libro a la biblioteca."""
        if libro.isbn in self.libros:
            # Si el libro ya existe, aumentar el número de copias
            self.libros[libro.isbn].numero_copias += libro.numero_copias
        else:
            self.libros[libro.isbn] = libro
    
    def registrar_miembro(self, miembro: Miembro):
        """Registra un nuevo miembro."""
        self.miembros.append(miembro)
    
    def buscar_libro(self, titulo: str) -> Optional[Libro]:
        """Busca un libro por título."""
        for libro in self.libros.values():
            if titulo.lower() in libro.titulo.lower():
                return libro
        return None
    
    def realizar_prestamo(self, miembro: Miembro, libro: Libro) -> Optional[Prestamo]:
        """
        Realiza un préstamo de libro.
        
        Args:
            miembro: Objeto Miembro
            libro: Objeto Libro
        
        Returns:
            Objeto Prestamo si es exitoso, None si hay error
        """
        # Verificar si el miembro está activo
        if not miembro.activo:
            print(f"Error: El miembro {miembro.nombre} no está activo")
            return None
        
        # Verificar si hay copias disponibles
        if not libro.esta_disponible():
            print(f"Error: No hay copias disponibles de '{libro.titulo}'")
            return None
        
        # Verificar si el miembro tiene multas pendientes
        multas_pendientes = [m for m in self.multas 
                            if m.prestamo.miembro.id_miembro == miembro.id_miembro 
                            and not m.pagada]
        if multas_pendientes:
            print(f"Error: {miembro.nombre} tiene multas pendientes")
            return None
        
        # Crear préstamo
        prestamo = Prestamo(miembro, libro)
        libro.prestar_copia()
        self.prestamos.append(prestamo)
        
        return prestamo
    
    def devolver_libro(self, id_prestamo: int) -> bool:
        """
        Registra la devolución de un libro.
        
        Args:
            id_prestamo: ID del préstamo
        
        Returns:
            True si se devolvió exitosamente, False si no se encontró
        """
        for prestamo in self.prestamos:
            if prestamo.id_prestamo == id_prestamo:
                if prestamo.fecha_devolucion:
                    print("Error: Este préstamo ya fue devuelto")
                    return False
                
                prestamo.devolver()
                prestamo.libro.devolver_copia()
                
                # Crear multa si está vencido
                if prestamo.esta_vencido():
                    dias_retraso = (datetime.now() - prestamo.fecha_vencimiento).days
                    multa = Multa(prestamo, dias_retraso)
                    self.multas.append(multa)
                    print(f"Multa creada: {multa}")
                
                return True
        
        print(f"Error: Préstamo #{id_prestamo} no encontrado")
        return False
    
    def renovar_prestamo(self, id_prestamo: int) -> bool:
        """
        Renueva un préstamo.
        
        Args:
            id_prestamo: ID del préstamo
        
        Returns:
            True si se renovó exitosamente, False si no se puede renovar
        """
        for prestamo in self.prestamos:
            if prestamo.id_prestamo == id_prestamo:
                if prestamo.fecha_devolucion:
                    print("Error: No se puede renovar un préstamo devuelto")
                    return False
                
                if prestamo.renovar():
                    return True
                else:
                    print("Error: Se alcanzó el máximo de renovaciones")
                    return False
        
        print(f"Error: Préstamo #{id_prestamo} no encontrado")
        return False
    
    def obtener_prestamos_activos(self, miembro: Miembro) -> List[Prestamo]:
        """Obtiene los préstamos activos de un miembro."""
        return [p for p in self.prestamos 
                if p.miembro.id_miembro == miembro.id_miembro 
                and not p.fecha_devolucion]
    
    def obtener_prestamos_vencidos(self) -> List[Prestamo]:
        """Obtiene todos los préstamos vencidos."""
        return [p for p in self.prestamos 
                if not p.fecha_devolucion and p.esta_vencido()]
    
    def mostrar_catalogo(self):
        """Muestra el catálogo de libros."""
        print(f"\n{'='*70}")
        print(f"CATÁLOGO DE {self.nombre.upper()}")
        print(f"{'='*70}")
        
        if not self.libros:
            print("No hay libros en la biblioteca")
        else:
            # Agrupar por género
            generos = set(libro.genero for libro in self.libros.values())
            for genero in sorted(generos, key=lambda g: g.value):
                print(f"\n{genero.value.upper()}:")
                for libro in self.libros.values():
                    if libro.genero == genero:
                        disponibilidad = "✓ Disponible" if libro.esta_disponible() else "✗ No disponible"
                        print(f"  {libro} [{disponibilidad}]")
        
        print(f"{'='*70}\n")
    
    def mostrar_estado(self):
        """Muestra el estado general de la biblioteca."""
        print(f"\n{'='*70}")
        print(f"ESTADO DE {self.nombre.upper()}")
        print(f"{'='*70}")
        print(f"Total de libros: {len(self.libros)}")
        print(f"Total de miembros: {len(self.miembros)}")
        print(f"Préstamos activos: {len([p for p in self.prestamos if not p.fecha_devolucion])}")
        print(f"Préstamos vencidos: {len(self.obtener_prestamos_vencidos())}")
        print(f"Multas pendientes: {len([m for m in self.multas if not m.pagada])}")
        print(f"{'='*70}\n")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Municipal Central")
    
    # Agregar libros
    biblioteca.agregar_libro(Libro("978-0-06-112008-4", "El Quijote", "Miguel de Cervantes", 
                                   Genero.FICCION, 1605, 3))
    biblioteca.agregar_libro(Libro("978-0-14-028329-7", "1984", "George Orwell", 
                                   Genero.FICCION, 1949, 2))
    biblioteca.agregar_libro(Libro("978-0-06-093546-7", "Sapiens", "Yuval Noah Harari", 
                                   Genero.NO_FICCION, 2011, 2))
    biblioteca.agregar_libro(Libro("978-0-393-05081-8", "Una Breve Historia del Tiempo", 
                                   "Stephen Hawking", Genero.CIENCIA, 1988, 1))
    biblioteca.agregar_libro(Libro("978-0-7432-7356-5", "El Código Da Vinci", "Dan Brown", 
                                   Genero.FICCION, 2003, 4))
    
    # Mostrar catálogo
    biblioteca.mostrar_catalogo()
    
    # Registrar miembros
    miembro1 = Miembro("Laura García", "laura@email.com", "555-1111")
    miembro2 = Miembro("Carlos López", "carlos@email.com", "555-2222")
    miembro3 = Miembro("María Rodríguez", "maria@email.com", "555-3333")
    
    biblioteca.registrar_miembro(miembro1)
    biblioteca.registrar_miembro(miembro2)
    biblioteca.registrar_miembro(miembro3)
    
    # Realizar préstamos
    print("Realizando préstamos...\n")
    libro1 = biblioteca.buscar_libro("Quijote")
    libro2 = biblioteca.buscar_libro("1984")
    libro3 = biblioteca.buscar_libro("Sapiens")
    
    prestamo1 = biblioteca.realizar_prestamo(miembro1, libro1)
    prestamo2 = biblioteca.realizar_prestamo(miembro2, libro2)
    prestamo3 = biblioteca.realizar_prestamo(miembro3, libro3)
    
    if prestamo1:
        print(f"✓ {prestamo1}")
    if prestamo2:
        print(f"✓ {prestamo2}")
    if prestamo3:
        print(f"✓ {prestamo3}")
    
    # Mostrar estado
    biblioteca.mostrar_estado()
    
    # Renovar un préstamo
    print("Renovando préstamo #1...\n")
    biblioteca.renovar_prestamo(1)
    
    # Devolver un libro
    print("Devolviendo préstamo #2...\n")
    biblioteca.devolver_libro(2)
    
    # Mostrar préstamos activos de un miembro
    print(f"Préstamos activos de {miembro1.nombre}:")
    for prestamo in biblioteca.obtener_prestamos_activos(miembro1):
        print(f"  {prestamo}")
    
    # Mostrar estado final
    biblioteca.mostrar_estado()
