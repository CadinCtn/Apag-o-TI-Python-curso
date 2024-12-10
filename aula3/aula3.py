dados = {
  "nome": "Pedro",
  "ano_nascimento": 2002,
  "estado": "Paraná",
  "cidade": "Londrina",
  "estado_civil": "Solteiro(a)"
}
'''
print(dados)
print(dados["nome"])
print(dados["ano_nascimento"])
print(dados["estado"])
print(dados["cidade"])
print(dados["estado_civil"])
'''
#UPDATE
dados["ano_nascimento"] = 2000

#DELETE
del dados["cidade"]

user = {
  "nome": "Cristyan",
  "login": "cris",
  "senha": "12345",
}

player = {
    "nickname": "IndYni",
    "classe":{
      "principal": "Cavaleiro",
      "secundaria": "Necromante"
    } ,
    "armas": ["Alabarda", "Escudo", "Adaga"],
    "nivel": 12
  }


'''
print(user.keys(), player.keys()) #Mostra chaves
print(user.values(), player.values()) #Mostra valores
print(user.items(), player.items()) #Mostra valores e chaves
'''

nome = user.get("nome")
login = user.get("login")
senha = user.get("senha")

__login__ = str(input("Digite o login: "))
__password__ = str(input("Digite a senha: "))

__class__ = player.get("classe")
__main__ = __class__.get("principal")
__secondary__ = __class__.get("secundaria")

if __login__ == login and __password__ == senha:
    print("Seja bem vindo(a) ", player.get("nickname"))
    print( "você é um(a) ", __main__, __secondary__)
    print("Nível: ", player.get("nivel"))
    
    weapons = player.get("armas")
    item_0 = weapons[0]
    item_1 = weapons[1]
    item_2 = weapons[2]

    __inventory__ = [item_0, item_1, item_2]

    print(f"Inventario: {__inventory__[0]}")
    print(f"            {__inventory__[1]}")
    print(f"            {__inventory__[2]}")
    
else:
    print("Usuário ou senha inválidos")