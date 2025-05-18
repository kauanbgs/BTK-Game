# File made by: Davi, Rafael

import time




inventoryItens = []
weaponsInventory = []

def inventory():
  from assets.things import clearScreen
  from assets.itens import Itens
  from menus.menu import menu
  from assets.things import updateStatus

  clearScreen()
  print("Seu inventário: ")
  print("[0] - Voltar")
  if not inventoryItens:
    clearScreen()
    print("Seu inventário está vazio.")
    time.sleep(2)
    menu()

  else:
    for i, item in enumerate(inventoryItens):
      utilizavel = False

      if item in Itens.base_itens and Itens.base_itens[item]["utilizavel"]:
        utilizavel = True
      elif item in Itens.materials and Itens.materials[item]["utilizavel"]:
        utilizavel = True
      elif item in Itens.Itens_personalizados and Itens.Itens_personalizados[item]["utilizavel"]:
        utilizavel = True

      if utilizavel:
        print(f"[{i + 1}] - {item} - UTILIZÁVEL")
      else:
        print(f"[{i + 1}] - {item}")
    option = input("Escolha uma opção: ")

    if not option.isdigit():
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      inventory()
    else:
      option = int(option)

    if option == 0:
      menu()
    elif option > len(inventoryItens) or option < 0:
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      inventory()
    else:
      item = inventoryItens[option - 1]

      if item in Itens.base_itens and Itens.base_itens[item]["utilizavel"]:
          print(f"Você usou: {item}")
          updateStatus(item)
          inventoryItens.remove(item)
          inventory()
      elif item in Itens.materials and Itens.materials[item]["utilizavel"]:
          print(f"Você usou: {item}")
          updateStatus(item)
          inventoryItens.remove(item)
          inventory()
      elif item in Itens.Itens_personalizados and Itens.Itens_personalizados[item]["utilizavel"]:
          print(f"Você usou: {item}")
          updateStatus(item)
          inventoryItens.remove(item)
          inventory()
      else:
          print(f"{item} não é utilizável.")
          time.sleep(1)
          inventory()
      
