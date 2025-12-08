"""
Solución de Programación Orientada a Objetos (POO)
Programa para calcular el promedio semanal de temperaturas
"""

from abc import ABC, abstractmethod
from typing import List

class DatosClima(ABC):
    """
    Clase abstracta que define la interfaz para datos de clima.
    Demuestra el uso de herencia y polimorfismo.
    """
    
    @abstractmethod
    def obtener_temperatura(self) -> float:
        """Obtiene la temperatura del día."""
        pass
    
    @abstractmethod
    def calcular_promedio(self) -> float:
        """Calcula el promedio de temperaturas."""
        pass

class DiasClima(DatosClima):
    """
    Clase que representa un día del clima.
    Demuestra encapsulamiento con atributos privados.
    """
    
    def __init__(self, nombre_dia: str, temperatura: float = None):
        """
        Inicializa un día del clima.
        
        Args:
            nombre_dia (str): Nombre del día
            temperatura (float): Temperatura del día (opcional)
        """
        self.__nombre_dia = nombre_dia
        self.__temperatura = temperatura
    
    @property
    def nombre_dia(self) -> str:
        """Obtiene el nombre del día (propiedad de solo lectura)."""
        return self.__nombre_dia
    
    @property
    def temperatura(self) -> float:
        """Obtiene la temperatura del día."""
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor: float):
        """
        Establece la temperatura del día con validación.
        
        Args:
            valor (float): Temperatura a establecer
            
        Raises:
            ValueError: Si la temperatura no es un número válido
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("La temperatura debe ser un número.")
        self.__temperatura = valor
    
    def obtener_temperatura(self) -> float:
        """Retorna la temperatura del día."""
        return self.__temperatura
    
    def calcular_promedio(self) -> float:
        """Retorna la temperatura (promedio de un solo día)."""
        return self.__temperatura
    
    def __str__(self) -> str:
        """Representación en string del día."""
        return f"{self.__nombre_dia}: {self.__temperatura}°C"

class SemanaClima:
    """
    Clase que representa una semana de datos climáticos.
    Demuestra composición y gestión de colecciones.
    """
    
    def __init__(self):
        """Inicializa una semana vacía."""
        self.__dias = []
        self.__nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", 
                               "Viernes", "Sábado", "Domingo"]
    
    def agregar_dia(self, dia: DiasClima):
        """
        Agrega un día a la semana.
        
        Args:
            dia (DiasClima): Día a agregar
            
        Raises:
            ValueError: Si ya hay 7 días en la semana
        """
        if len(self.__dias) >= 7:
            raise ValueError("La semana ya tiene 7 días.")
        self.__dias.append(dia)
    
    def obtener_dias(self) -> List[DiasClima]:
        """Obtiene la lista de días de la semana."""
        return self.__dias.copy()
    
    def ingresar_temperaturas(self):
        """
        Solicita al usuario que ingrese las temperaturas de la semana.
        """
        print("=" * 50)
        print("INGRESO DE TEMPERATURAS SEMANALES")
        print("=" * 50)
        
        for nombre_dia in self.__nombres_dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura de {nombre_dia} (°C): "))
                    dia = DiasClima(nombre_dia, temp)
                    self.agregar_dia(dia)
                    break
                except ValueError as e:
                    print(f"Error: {e}")
    
    def calcular_promedio_semanal(self) -> float:
        """
        Calcula el promedio semanal de temperaturas.
        
        Returns:
            float: Promedio semanal
        """
        if len(self.__dias) == 0:
            return 0
        suma = sum(dia.temperatura for dia in self.__dias)
        return suma / len(self.__dias)
    
    def obtener_temperatura_maxima(self) -> float:
        """
        Obtiene la temperatura máxima de la semana.
        
        Returns:
            float: Temperatura máxima
        """
        if len(self.__dias) == 0:
            return 0
        return max(dia.temperatura for dia in self.__dias)
    
    def obtener_temperatura_minima(self) -> float:
        """
        Obtiene la temperatura mínima de la semana.
        
        Returns:
            float: Temperatura mínima
        """
        if len(self.__dias) == 0:
            return 0
        return min(dia.temperatura for dia in self.__dias)
    
    def obtener_rango_temperaturas(self) -> float:
        """
        Obtiene el rango de temperaturas (máxima - mínima).
        
        Returns:
            float: Rango de temperaturas
        """
        if len(self.__dias) == 0:
            return 0
        return self.obtener_temperatura_maxima() - self.obtener_temperatura_minima()
    
    def mostrar_resultados(self):
        """Muestra los resultados del análisis semanal."""
        print("\n" + "=" * 50)
        print("RESULTADOS DEL ANÁLISIS SEMANAL")
        print("=" * 50)
        
        print("\nTemperaturas diarias:")
        for dia in self.__dias:
            print(f"  {dia}")
        
        promedio = self.calcular_promedio_semanal()
        maxima = self.obtener_temperatura_maxima()
        minima = self.obtener_temperatura_minima()
        rango = self.obtener_rango_temperaturas()
        
        print(f"\nPromedio semanal: {promedio:.2f}°C")
        print(f"Temperatura máxima: {maxima}°C")
        print(f"Temperatura mínima: {minima}°C")
        print(f"Rango de temperaturas: {rango}°C")
        print("=" * 50)

def main():
    """Función principal que coordina el programa."""
    semana = SemanaClima()
    semana.ingresar_temperaturas()
    semana.mostrar_resultados()

if __name__ == "__main__":
    main()
