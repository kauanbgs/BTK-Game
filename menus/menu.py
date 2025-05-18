#File made by: Kauan

import time
from assets.things import clearScreen
from assets.things import typedPrint
from assets.config import Config




def menu():
  from player.inventory import inventory
  from menus.areas import areas
  from areas.tavern import tavern
  from player.status import status

  while True:
    clearScreen()
    print("----------------Praia----------------")
    print("[1] - Inventário")
    print("[2] - Status")
    print("[3] - Explorar") 
    print("[4] - Equipamentos")


    option = input("Escolha uma opção: ")

    if not option.isdigit():
        typedPrint("Opção inválida!", Config.speed)
        time.sleep(1)
        continue
    else:
      option = int(option)


    if option not in [1, 2, 3, 4, 5]:
      typedPrint("Opção inválida!", Config.speed)
      time.sleep(1)
      continue


    elif option == 1:
      clearScreen()
      typedPrint("Abrindo a mochila...", Config.speed)
      time.sleep(.3)
      inventory()
    elif option == 2:
      clearScreen()
      typedPrint("Procurando informações...", Config.speed)
      status()
    elif option == 3:
      clearScreen()
      typedPrint("Procurando areas...", Config.speed)
      areas()
    elif option == 4:
      clearScreen(
      typedPrint("Procurando equipamentos...", Config.speed)
      
      )
