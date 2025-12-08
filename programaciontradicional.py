"""
Solución de Programación Tradicional
Programa para calcular el promedio semanal de temperaturas
"""

def obtener_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana.
    
    Returns:
        list: Lista con las 7 temperaturas ingresadas
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("=" * 50)
    print("INGRESO DE TEMPERATURAS SEMANALES")
    print("=" * 50)
    
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura de {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas.
    
    Args:
        temperaturas (list): Lista de temperaturas
        
    Returns:
        float: Promedio de las temperaturas
    """
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


def encontrar_temperatura_maxima(temperaturas):
    """
    Encuentra la temperatura máxima de la semana.
    
    Args:
        temperaturas (list): Lista de temperaturas
        
    Returns:
        float: Temperatura máxima
    """
    return max(temperaturas) if temperaturas else 0


def encontrar_temperatura_minima(temperaturas):
    """
    Encuentra la temperatura mínima de la semana.
    
    Args:
        temperaturas (list): Lista de temperaturas
        
    Returns:
        float: Temperatura mínima
    """
    return min(temperaturas) if temperaturas else 0


def mostrar_resultados(temperaturas):
    """
    Muestra los resultados del análisis de temperaturas.
    
    Args:
        temperaturas (list): Lista de temperaturas
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("\n" + "=" * 50)
    print("RESULTADOS DEL ANÁLISIS SEMANAL")
    print("=" * 50)
    
    print("\nTemperaturas diarias:")
    for dia, temp in zip(dias, temperaturas):
        print(f"  {dia}: {temp}°C")
    
    promedio = calcular_promedio(temperaturas)
    maxima = encontrar_temperatura_maxima(temperaturas)
    minima = encontrar_temperatura_minima(temperaturas)
    
    print(f"\nPromedio semanal: {promedio:.2f}°C")
    print(f"Temperatura máxima: {maxima}°C")
    print(f"Temperatura mínima: {minima}°C")
    print(f"Rango de temperaturas: {maxima - minima}°C")
    print("=" * 50)


def main():
    """Función principal que coordina el programa."""
    temperaturas = obtener_temperaturas()
    mostrar_resultados(temperaturas)


if __name__ == "__main__":
    main()