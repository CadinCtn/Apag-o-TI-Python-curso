import pacote.service as ss
import pacote.usuario as u

nome = input("Digite seu nome: ")

opcao = 1

while opcao != 0:

  print("\n======================")
  print("  Calculadora Python")
  print("======================")
  print("1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("0 - Sair")

  u.saudacao(nome)

  try:
    
    opcao = int(input("Escolha uma operação para realizar: "))

    print("====================")


    match(opcao):
      case 1:
        print("Adição: ")
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        print("Resultado: ", ss.somar(num1, num2))
      
      case 2:
        print("Subtração: ")
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        print("Resultado: ", ss.subtrair(num1, num2))
        
      case 3:
        print("Multplicação: ")
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        print("Resultado: ", ss.multiplicar(num1, num2))
        
      case 4:
        print("Divisão: ")
        num1 = float(input("Numero 1: "))
        num2 = float(input("Numero 2: "))
        print("Resultado: ", ss.dividir(num1, num2))
      
      case 0:
        print("Encerrando...")
        break

      case _:
        print("VALOR INSERIDO INVÁLIDO!!!")

  except:
    print("VALOR INSERIDO INVÁLIDO!!!")