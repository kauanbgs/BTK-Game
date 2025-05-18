from assets.itens import Itens
from player.status import Char
from menus.menu import menu

import time
import os


def blacksmith():
  Char.foiFerreiro = True
  Char.where = "Ferreiro"
  

  print("Bem vindo ao ferreiro!")
  os.system('cls')
  print(f"Você tem {Char.coins} moedas!")
  print("[0] - Voltar")
  print(f"[1] - {Itens.blacksmith[0]["nome"]}  | {Itens.blacksmith[0]["preco"]} moedas  | +{Itens.blacksmith[0]["dano"]}ATK")
  print(f"[2] - {Itens.blacksmith[1]["nome"]}    | {Itens.blacksmith[1]["preco"]} moedas | +{Itens.blacksmith[1]["dano"]}ATK")
  print(f"[3] - {Itens.blacksmith[2]["nome"]}     | {Itens.blacksmith[2]["preco"]} moedas | +{Itens.blacksmith[2]["dano"]}ATK")
  print(f"[4] - {Itens.blacksmith[3]["nome"]}  | {Itens.blacksmith[3]["preco"]} moedas | +{Itens.blacksmith[3]["dano"]}ATK")
  print(f"[5] - {Itens.blacksmith[4]["nome"]} | {Itens.blacksmith[4]["preco"]} moedas | +{Itens.blacksmith[4]["dano"]}ATK")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    os.system('cls')
    print("Opção inválida!")
    time.sleep(1)
    os.system('cls')
    blacksmith()
  else:
    option = int(option)

  if option == 0:
    os.system('cls')
    print("Saindo do ferreiro...")
    time.sleep(1)
    menu()

  elif option == 1:
    if Char.weapon != "Espada gasta" or Char.weapon != "Cajado antigo":
      os.system('cls')
      print("Você já tem uma arma equipada!")
      ########



  else:
    os.system('cls')
    print("Opção inválida!")
    time.sleep(2)
    blacksmith()
