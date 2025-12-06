class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def sonido(self):
        return "¡Miau!"

class Vaca(Animal):
    def sonido(self):
        return "¡Muuu!"

# Función que utiliza polimorfismo
def hacer_sonar(animal):
    return animal.sonido()

# Creación de objetos
perro = Perro()
gato = Gato()
vaca = Vaca()

# Uso del polimorfismo
print(hacer_sonar(perro))  # Salida: ¡Guau!
print(hacer_sonar(gato))   # Salida: ¡Miau!
print(hacer_sonar(vaca))   # Salida: ¡Muuu!