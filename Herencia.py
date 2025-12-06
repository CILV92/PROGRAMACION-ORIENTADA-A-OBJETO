class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} del año {self.año}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()} con {self.num_puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_manubrio):
        super().__init__(marca, modelo, año)
        self.tipo_manubrio = tipo_manubrio

    def descripcion(self):
        return f"{super().descripcion()} con manubrio {self.tipo_manubrio}"

# Uso
coche = Coche("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CBR", 2021, "deportivo")

print(coche.descripcion())  # Salida: Toyota Corolla del año 2020 con 4 puertas
print(moto.descripcion())   # Salida: Honda CBR del año 2021 con manubrio deportivo