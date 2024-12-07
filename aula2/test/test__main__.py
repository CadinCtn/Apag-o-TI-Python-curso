import pytest
from pacote import service, usuario

def test_modulo_1():
  assert service.somar(1,2) == 3
  assert service.subtrair(9,2) == 7
  assert service.multiplicar(2,3) == 6
  assert service.dividir(5,2) == 2.5


def test_modulo_2():
  assert usuario.saudacao("Jonas") == f"Olá, seja bem vindo(a) Jonas"
