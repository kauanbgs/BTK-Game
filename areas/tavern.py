#File made by: Kauan, Rafael

import time
from assets.config import Char
from assets.itens import Itens
from assets.things import clearScreen
from menus.menu import menu
from player.inventory import inventoryItens

def comprar_item(item):
    name = item["nome"]
    price = item["preco"]

    # Verifica se o jogador tem moedas suficientes
    if Char.coins >= price:
        inventoryItens.append(item)
        Char.coins -= price
        print(f"Você comprou {name} por {price} moedas!")
    else:
        print("Você não tem moedas suficientes!")

    time.sleep(2)

def tavern():
    Char.where = "Taverna"
    
    while True:
        clearScreen()
        mostrar_opcoes()
        option = input("Escolha uma opção: ")

        if not option.isdigit():
            clearScreen()
            print("Opção inválida!")
            time.sleep(1)
            continue

        option = int(option)

        if option == 0:
            clearScreen()
            print("Saindo da taverna...")
            time.sleep(1)
            menu()
            break

        elif 1 <= option <= len(Itens.tavern):
            clearScreen()
            choItem = Itens.tavern[option - 1]
            comprar_item(choItem)
        else:
            clearScreen()
            print("Opção inválida!")
            time.sleep(1)

def mostrar_opcoes():
    print(f"Você tem {Char.coins} moedas, e está na {Char.where}!")
    print("[0] - Voltar")
    for index, item in enumerate(Itens.tavern, start=1):
      print(f"[{index}] - {item['nome']} - {item['preco']} moedas")
