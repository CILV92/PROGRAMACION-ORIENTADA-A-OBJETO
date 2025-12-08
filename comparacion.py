"""
Programa de Comparación entre Programación Tradicional y POO
Demuestra las diferencias y ventajas de ambos enfoques
"""

import programaciontradicional as tradicional 
import poo as poo 


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "=" * 60)
    print("COMPARACIÓN: PROGRAMACIÓN TRADICIONAL vs POO")
    print("=" * 60)
    print("\n1. Ejecutar solución con Programación Tradicional")
    print("2. Ejecutar solución con Programación Orientada a Objetos (POO)")
    print("3. Ver comparación de características")
    print("4. Salir")
    print("\n" + "=" * 60)


def mostrar_comparacion():
    """Muestra una comparación detallada entre ambos enfoques."""
    comparacion = """

           COMPARACIÓN: PROGRAMACIÓN TRADICIONAL vs POO                    


 PROGRAMACIÓN TRADICIONAL 
                                                                             
 Características:                                                            
  + Enfoque procedural basado en funciones                                   
  + Datos y funciones separadas                                             
  + Código lineal y secuencial                                              
  + Fácil de entender para problemas simples                                
                                                                             
 Ventajas:                                                                   
  + Simplicidad en programas pequeños                                       
  + Menor curva de aprendizaje                                              
  + Ejecución directa y predecible                                          
  + Menos overhead de memoria                                               
                                                                             
 Desventajas:                                                                
  + Difícil de mantener en proyectos grandes                                
  + Reutilización de código limitada                                        
  + Falta de encapsulamiento                                                
  + Propenso a errores en datos globales                                    
                                                                             


 PROGRAMACIÓN ORIENTADA A OBJETOS (POO) 
                                                                             
 Características:                                                            
  + Enfoque basado en clases y objetos                                      
  + Datos y métodos encapsulados                                            
  + Reutilización mediante herencia                                         
  + Polimorfismo y abstracción                                              
                                                                             
 Ventajas:                                                                   
  + Código modular y reutilizable                                           
  + Fácil mantenimiento y escalabilidad                                     
  + Encapsulamiento protege datos                                           
  + Herencia reduce duplicación de código                                   
  + Polimorfismo permite flexibilidad                                       
  + Mejor organización en proyectos grandes                                 
                                                                             
 Desventajas:                                                                
  + Mayor complejidad inicial                                               
  + Curva de aprendizaje más pronunciada                                    
  + Overhead de memoria por objetos                                         
  + Puede ser excesivo para problemas simples                               
                                                                             


 CONCEPTOS APLICADOS EN ESTE PROYECTO 
                                                                             
 Encapsulamiento:                                                            
  + Atributos privados (__temperatura, __nombre_dia)                        
  + Propiedades (property) para acceso controlado                           
  + Validación en setters                                                    
                                                                             
 Herencia:                                                                   
  + Clase abstracta DatosClima                                              
  + DiasClima hereda de DatosClima                                          
  + Implementación de métodos abstractos                                    
                                                                             
 Polimorfismo:                                                               
  + Métodos abstractos implementados en subclases                           
  + Comportamiento diferente según el tipo de objeto                        
                                                                             
 Composición:                                                                
  + SemanaClima contiene múltiples DiasClima                                
  + Relación "tiene-un" entre clases                                        
                                                                             


 RECOMENDACIONES DE USO 
                                                                             
 Usa Programación Tradicional cuando:                                       
  + Trabajas con scripts simples                                            
  + El proyecto es pequeño y de corta duración                              
  + Necesitas máximo rendimiento en operaciones simples                     
  + Estás aprendiendo los conceptos básicos                                 
                                                                             
 Usa POO cuando:                                                             
  + Trabajas en proyectos medianos o grandes                                
  + Necesitas reutilizar código                                             
  + Trabajas en equipo                                                       
  + Requieres mantenimiento a largo plazo                                   
  + Necesitas modelar entidades del mundo real                              
                                                                            

    """
    print(comparacion)


def main():
    """Función principal."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n" + "=" * 60)
            print("EJECUTANDO: PROGRAMACIÓN TRADICIONAL")
            print("=" * 60)
            tradicional.main()
        
        elif opcion == "2":
            print("\n" + "=" * 60)
            print("EJECUTANDO: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)")
            print("=" * 60)
            poo.main()
        
        elif opcion == "3":
            mostrar_comparacion()
        
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
