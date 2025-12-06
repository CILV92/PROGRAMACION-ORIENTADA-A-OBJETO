class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular  # Atributo protegido
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return f"Se depositaron ${monto}. Saldo actual: ${self.__saldo}"
        return "Monto inválido."

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return f"Se retiraron ${monto}. Saldo actual: ${self.__saldo}"
        return "Fondos insuficientes o monto inválido."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"

# Uso
cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.depositar(500))  # Salida: Se depositaron $500. Saldo actual: $1500
print(cuenta.retirar(200))    # Salida: Se retiraron $200. Saldo actual: $1300
print(cuenta.consultar_saldo())  # Salida: Saldo actual: $1300