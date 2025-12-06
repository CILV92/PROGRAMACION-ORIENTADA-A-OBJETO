from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau, miau!"

# Uso
perro = Perro()
gato = Gato()

print(perro.hacer_sonido())  # Salida: ¡Guau, guau!
print(gato.hacer_sonido())   # Salida: ¡Miau, miau!