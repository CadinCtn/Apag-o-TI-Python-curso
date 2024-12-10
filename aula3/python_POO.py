class Usuario():
    def __init__(self, nome, ano_nascimento, cidade):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.cidade = cidade

    def saudacao(self):
        return f"Olá, me chamo {self.nome}, moro em {self.cidade} e nasci em {self.ano_nascimento}"
  


class Carro():
    def __init__(self, marca, modelo, ano, fipe):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.fipe = fipe

    def descricao(self):
        return f"{self.marca} {self.modelo} ano {self.ano} possui a fipe no valor de R${self.fipe}"


class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return f"*{self.nome}*: Au Au!"


class Gato(Animal):
    def som(self):
        return f"*{self.nome}*: Miau!"


class Conta():
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor    

    def sacar(self, valor):
        if valor > self.__saldo:
            return "Saldo insuficiente"
        else:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo


conta = Conta("Cristyan")
print(conta.get_saldo())
conta.depositar(100)
print(conta.get_saldo())
conta.sacar(1000)
print(conta.get_saldo())
conta.sacar(50)
print(conta.get_saldo())

'''
carro = Carro("Chevrolet", "Corvette Targa 6.0 V8", 2008, 380657)
print(carro.descricao())
'''

'''
pessoa = Usuario("Cristyan", 2005, "Cambé")
print(pessoa.saudacao())
'''


'''
__evee__ = Cachorro("Evve")
__dexter__ = Gato("Dexter")
print(__evee__.som())
print(__dexter__.som())
'''
