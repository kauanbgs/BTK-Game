from assets.itens import Itens
from player.status import Char
from assets.config import Config
from player.inventory import inventory, inventoryItens
from assets.things import clearScreen
import time
from menus.menu import menu
from assets.things import updateStatus
from assets.things import typedPrint
import random
from assets.things import DicesAnimation



def duel(enemyName, enemyHealth, enemyAttack, enemySpells, boss):
  while Char.health > 0 and enemyHealth > 0:
    clearScreen()
    print(f"Você está lutando contra {enemyName}!")
    print(f"Vida do inimigo: {enemyHealth}")
    print(f"Sua vida: {Char.health}")
    print(f"Sua mana: {Char.mana}")
    print("[1] - Atacar")
    print("[2] - Usar magia")
    option = input("Escolha uma opção: ")

    if not option.isdigit():
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      continue
    else:
      option = int(option)
    
    if option == 1:
      typedPrint("Rolando o dado...", Config.speed)
      dicesAnimation()
    