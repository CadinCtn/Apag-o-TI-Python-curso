class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False