"""
Pruebas unitarias para ambas soluciones
Demuestra cómo probar código tradicional y orientado a objetos
"""

import unittest
import programaciontradicional as tradicional
import poo as poo

class TestProgramacionTradicional(unittest.TestCase):
    """Pruebas para la solución tradicional."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 24.0, 20.0]
    
    def test_calcular_promedio(self):
        """Prueba el cálculo del promedio."""
        promedio = tradicional.calcular_promedio(self.temperaturas)
        promedio_esperado = sum(self.temperaturas) / len(self.temperaturas)
        self.assertAlmostEqual(promedio, promedio_esperado, places=2)
    
    def test_calcular_promedio_vacio(self):
        """Prueba el cálculo con lista vacía."""
        promedio = tradicional.calcular_promedio([])
        self.assertEqual(promedio, 0)
    
    def test_temperatura_maxima(self):
        """Prueba la búsqueda de temperatura máxima."""
        maxima = tradicional.encontrar_temperatura_maxima(self.temperaturas)
        self.assertEqual(maxima, 24.0)
    
    def test_temperatura_minima(self):
        """Prueba la búsqueda de temperatura mínima."""
        minima = tradicional.encontrar_temperatura_minima(self.temperaturas)
        self.assertEqual(minima, 19.5)
    
    def test_temperatura_maxima_vacio(self):
        """Prueba con lista vacía."""
        maxima = tradicional.encontrar_temperatura_maxima([])
        self.assertEqual(maxima, 0)
    
    def test_temperatura_minima_vacio(self):
        """Prueba con lista vacía."""
        minima = tradicional.encontrar_temperatura_minima([])
        self.assertEqual(minima, 0)


class TestDiasClima(unittest.TestCase):
    """Pruebas para la clase DiasClima."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.dia = poo.DiasClima("Lunes", 20.5)
    
    def test_crear_dia(self):
        """Prueba la creación de un día."""
        self.assertEqual(self.dia.nombre_dia, "Lunes")
        self.assertEqual(self.dia.temperatura, 20.5)
    
    def test_obtener_temperatura(self):
        """Prueba el método obtener_temperatura."""
        temp = self.dia.obtener_temperatura()
        self.assertEqual(temp, 20.5)
    
    def test_establecer_temperatura_valida(self):
        """Prueba establecer una temperatura válida."""
        self.dia.temperatura = 25.0
        self.assertEqual(self.dia.temperatura, 25.0)
    
    def test_establecer_temperatura_invalida(self):
        """Prueba que se rechace una temperatura inválida."""
        with self.assertRaises(ValueError):
            self.dia.temperatura = "no es número"
    
    def test_nombre_dia_solo_lectura(self):
        """Prueba que el nombre del día es de solo lectura."""
        with self.assertRaises(AttributeError):
            self.dia.nombre_dia = "Martes"
    
    def test_str_representation(self):
        """Prueba la representación en string."""
        expected = "Lunes: 20.5°C"
        self.assertEqual(str(self.dia), expected)


class TestSemanaClima(unittest.TestCase):
    """Pruebas para la clase SemanaClima."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.semana = poo.SemanaClima()
        self.temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 24.0, 20.0]
        self.nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", 
                            "Viernes", "Sábado", "Domingo"]
        
        # Agregar días a la semana
        for nombre, temp in zip(self.nombres_dias, self.temperaturas):
            dia = poo.DiasClima(nombre, temp)
            self.semana.agregar_dia(dia)
    
    def test_agregar_dia(self):
        """Prueba agregar un día a la semana."""
        dias = self.semana.obtener_dias()
        self.assertEqual(len(dias), 7)
    
    def test_agregar_dia_exceso(self):
        """Prueba que no se pueden agregar más de 7 días."""
        with self.assertRaises(ValueError):
            dia_extra = poo.DiasClima("Extra", 20.0)
            self.semana.agregar_dia(dia_extra)
    
    def test_calcular_promedio_semanal(self):
        """Prueba el cálculo del promedio semanal."""
        promedio = self.semana.calcular_promedio_semanal()
        promedio_esperado = sum(self.temperaturas) / len(self.temperaturas)
        self.assertAlmostEqual(promedio, promedio_esperado, places=2)
    
    def test_temperatura_maxima(self):
        """Prueba la búsqueda de temperatura máxima."""
        maxima = self.semana.obtener_temperatura_maxima()
        self.assertEqual(maxima, 24.0)
    
    def test_temperatura_minima(self):
        """Prueba la búsqueda de temperatura mínima."""
        minima = self.semana.obtener_temperatura_minima()
        self.assertEqual(minima, 19.5)
    
    def test_rango_temperaturas(self):
        """Prueba el cálculo del rango de temperaturas."""
        rango = self.semana.obtener_rango_temperaturas()
        rango_esperado = 24.0 - 19.5
        self.assertAlmostEqual(rango, rango_esperado, places=1)
    
    def test_semana_vacia(self):
        """Prueba operaciones en una semana vacía."""
        semana_vacia = poo.SemanaClima()
        self.assertEqual(semana_vacia.calcular_promedio_semanal(), 0)
        self.assertEqual(semana_vacia.obtener_temperatura_maxima(), 0)
        self.assertEqual(semana_vacia.obtener_temperatura_minima(), 0)
        self.assertEqual(semana_vacia.obtener_rango_temperaturas(), 0)


class TestComparacionResultados(unittest.TestCase):
    """Pruebas que comparan resultados entre ambos enfoques."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 24.0, 20.0]
        
        # Crear semana con POO
        self.semana = poo.SemanaClima()
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", 
                       "Viernes", "Sábado", "Domingo"]
        for nombre, temp in zip(nombres_dias, self.temperaturas):
            dia = poo.DiasClima(nombre, temp)
            self.semana.agregar_dia(dia)
    
    def test_promedio_igual(self):
        """Prueba que ambos enfoques dan el mismo promedio."""
        promedio_tradicional = tradicional.calcular_promedio(self.temperaturas)
        promedio_poo = self.semana.calcular_promedio_semanal()
        self.assertAlmostEqual(promedio_tradicional, promedio_poo, places=2)
    
    def test_maxima_igual(self):
        """Prueba que ambos enfoques encuentran la misma máxima."""
        maxima_tradicional = tradicional.encontrar_temperatura_maxima(self.temperaturas)
        maxima_poo = self.semana.obtener_temperatura_maxima()
        self.assertEqual(maxima_tradicional, maxima_poo)
    
    def test_minima_igual(self):
        """Prueba que ambos enfoques encuentran la misma mínima."""
        minima_tradicional = tradicional.encontrar_temperatura_minima(self.temperaturas)
        minima_poo = self.semana.obtener_temperatura_minima()
        self.assertEqual(minima_tradicional, minima_poo)


def run_tests():
    """Ejecuta todas las pruebas."""
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar todas las pruebas
    suite.addTests(loader.loadTestsFromTestCase(TestProgramacionTradicional))
    suite.addTests(loader.loadTestsFromTestCase(TestDiasClima))
    suite.addTests(loader.loadTestsFromTestCase(TestSemanaClima))
    suite.addTests(loader.loadTestsFromTestCase(TestComparacionResultados))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"Pruebas ejecutadas: {resultado.testsRun}")
    print(f"Exitosas: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Fallos: {len(resultado.failures)}")
    print(f"Errores: {len(resultado.errors)}")
    print("=" * 70)
    
    return resultado.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
