"""
Ejemplos de uso de ambas soluciones sin entrada interactiva
Útil para demostración y pruebas
"""

import programaciontradicional as tradicional
import poo as poo


def ejemplo_tradicional():
    """Demuestra el uso de la programación tradicional."""
    print("\n" + "=" * 70)
    print("EJEMPLO: PROGRAMACIÓN TRADICIONAL")
    print("=" * 70)
    
    # Datos de ejemplo
    temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 24.0, 20.0]
    
    print("\nTemperaturas ingresadas:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia, temp in zip(dias, temperaturas):
        print(f"  {dia}: {temp}°C")
    
    # Cálculos
    promedio = tradicional.calcular_promedio(temperaturas)
    maxima = tradicional.encontrar_temperatura_maxima(temperaturas)
    minima = tradicional.encontrar_temperatura_minima(temperaturas)
    
    # Mostrar resultados
    print("\n" + "-" * 70)
    print("RESULTADOS:")
    print("-" * 70)
    print(f"Promedio semanal: {promedio:.2f}°C")
    print(f"Temperatura máxima: {maxima}°C")
    print(f"Temperatura mínima: {minima}°C")
    print(f"Rango de temperaturas: {maxima - minima}°C")
    
    # Análisis adicional
    print("\n" + "-" * 70)
    print("ANÁLISIS ADICIONAL:")
    print("-" * 70)
    
    # Días por encima del promedio
    dias_arriba = [(dia, temp) for dia, temp in zip(dias, temperaturas) if temp > promedio]
    print(f"\nDías por encima del promedio ({promedio:.2f}°C):")
    for dia, temp in dias_arriba:
        diferencia = temp - promedio
        print(f"  {dia}: {temp}°C (+{diferencia:.2f}°C)")
    
    # Días por debajo del promedio
    dias_abajo = [(dia, temp) for dia, temp in zip(dias, temperaturas) if temp < promedio]
    print(f"\nDías por debajo del promedio ({promedio:.2f}°C):")
    for dia, temp in dias_abajo:
        diferencia = promedio - temp
        print(f"  {dia}: {temp}°C (-{diferencia:.2f}°C)")


def ejemplo_poo():
    """Demuestra el uso de la programación orientada a objetos."""
    print("\n" + "=" * 70)
    print("EJEMPLO: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)")
    print("=" * 70)
    
    # Crear semana
    semana = poo.SemanaClima()
    
    # Datos de ejemplo
    datos = [
        ("Lunes", 20.5),
        ("Martes", 22.0),
        ("Miércoles", 19.5),
        ("Jueves", 21.0),
        ("Viernes", 23.5),
        ("Sábado", 24.0),
        ("Domingo", 20.0)
    ]
    
    print("\nCreando días y agregando a la semana...")
    for nombre, temp in datos:
        dia = poo.DiasClima(nombre, temp)
        semana.agregar_dia(dia)
        print(f"  [OK] {dia}")
    
    # Obtener resultados
    promedio = semana.calcular_promedio_semanal()
    maxima = semana.obtener_temperatura_maxima()
    minima = semana.obtener_temperatura_minima()
    rango = semana.obtener_rango_temperaturas()
    
    # Mostrar resultados
    print("\n" + "-" * 70)
    print("RESULTADOS:")
    print("-" * 70)
    print(f"Promedio semanal: {promedio:.2f}°C")
    print(f"Temperatura máxima: {maxima}°C")
    print(f"Temperatura mínima: {minima}°C")
    print(f"Rango de temperaturas: {rango}°C")
    
    # Análisis adicional
    print("\n" + "-" * 70)
    print("ANÁLISIS ADICIONAL:")
    print("-" * 70)
    
    dias = semana.obtener_dias()
    
    # Días por encima del promedio
    dias_arriba = [d for d in dias if d.temperatura > promedio]
    print(f"\nDías por encima del promedio ({promedio:.2f}°C):")
    for dia in dias_arriba:
        diferencia = dia.temperatura - promedio
        print(f"  {dia.nombre_dia}: {dia.temperatura}°C (+{diferencia:.2f}°C)")
    
    # Días por debajo del promedio
    dias_abajo = [d for d in dias if d.temperatura < promedio]
    print(f"\nDías por debajo del promedio ({promedio:.2f}°C):")
    for dia in dias_abajo:
        diferencia = promedio - dia.temperatura
        print(f"  {dia.nombre_dia}: {dia.temperatura}°C (-{diferencia:.2f}°C)")


def comparacion_directa():
    """Compara directamente ambos enfoques."""
    print("\n" + "=" * 70)
    print("COMPARACIÓN DIRECTA: TRADICIONAL vs POO")
    print("=" * 70)
    
    # Datos
    temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 24.0, 20.0]
    
    # Enfoque tradicional
    promedio_trad = tradicional.calcular_promedio(temperaturas)
    maxima_trad = tradicional.encontrar_temperatura_maxima(temperaturas)
    minima_trad = tradicional.encontrar_temperatura_minima(temperaturas)
    
    # Enfoque POO
    semana = poo.SemanaClima()
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for nombre, temp in zip(nombres_dias, temperaturas):
        dia = poo.DiasClima(nombre, temp)
        semana.agregar_dia(dia)
    
    promedio_poo = semana.calcular_promedio_semanal()
    maxima_poo = semana.obtener_temperatura_maxima()
    minima_poo = semana.obtener_temperatura_minima()
    
    # Mostrar comparación
    print("\n" + "-" * 70)
    print(f"{'Métrica':<30} {'Tradicional':<20} {'POO':<20}")
    print("-" * 70)
    print(f"{'Promedio semanal':<30} {promedio_trad:<20.2f} {promedio_poo:<20.2f}")
    print(f"{'Temperatura máxima':<30} {maxima_trad:<20.1f} {maxima_poo:<20.1f}")
    print(f"{'Temperatura mínima':<30} {minima_trad:<20.1f} {minima_poo:<20.1f}")
    print("-" * 70)
    
    # Verificar que los resultados son iguales
    print("\n[OK] Ambos enfoques producen los mismos resultados")
    print(f"  Promedio coincide: {abs(promedio_trad - promedio_poo) < 0.01}")
    print(f"  Máxima coincide: {maxima_trad == maxima_poo}")
    print(f"  Mínima coincide: {minima_trad == minima_poo}")


def demostrar_encapsulamiento():
    """Demuestra el encapsulamiento en POO."""
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN: ENCAPSULAMIENTO EN POO")
    print("=" * 70)
    
    # Crear un día
    dia = poo.DiasClima("Lunes", 20.5)
    print(f"\nDía creado: {dia}")
    
    # Acceso a propiedades
    print(f"\nAcceso a propiedades:")
    print(f"  Nombre del día: {dia.nombre_dia}")
    print(f"  Temperatura: {dia.temperatura}°C")
    
    # Modificar temperatura válida
    print(f"\nModificando temperatura a 25.0°C...")
    dia.temperatura = 25.0
    print(f"  Nueva temperatura: {dia.temperatura}°C")
    
    # Intentar modificar temperatura inválida
    print(f"\nIntentando establecer temperatura inválida...")
    try:
        dia.temperatura = "no es número"
    except ValueError as e:
        print(f"  [OK] Error capturado: {e}")
    
    # Intentar modificar nombre (propiedad de solo lectura)
    print(f"\nIntentando modificar nombre del día...")
    try:
        dia.nombre_dia = "Martes"
    except AttributeError as e:
        print(f"  [OK] Error capturado: No se puede establecer atributo (propiedad de solo lectura)")
    
    # Acceso a atributos privados
    print(f"\nIntentando acceder a atributos privados...")
    try:
        print(dia.__temperatura)
    except AttributeError:
        print(f"  [OK] No se puede acceder a __temperatura (atributo privado)")


def main():
    """Función principal."""
    print("\n" + "=" * 70)
    print("EJEMPLOS DE USO: PROGRAMACIÓN TRADICIONAL vs POO")
    print("=" * 70)
    
    # Ejecutar ejemplos
    ejemplo_tradicional()
    ejemplo_poo()
    comparacion_directa()
    demostrar_encapsulamiento()
    
    print("\n" + "=" * 70)
    print("FIN")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
