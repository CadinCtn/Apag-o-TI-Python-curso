class Conta:
    def __init__(self, numero, titular, saldo_inicial):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        if valor > self._saldo:
            return False
        self._saldo -= valor
        return True
    
    def depositar(self, valor):
        self._saldo += valor

    def get_numero(self):
        return self._numero
    
    def get_titular(self):
        return self._titular