#File made by: Kauan

import time
from assets.things import clearScreen
from assets.things import typedPrint
from assets.config import Config


def menu():

  from areas.tavern import tavern

  while True:
    clearScreen()
    print("----------------Eldoria----------------")
    print("[1] - Inventário")
    print("[2] - Status")
    print("[3] - Taverna")
    print("[4] - Explorar") 
    print("[5] - Ferreiro")


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
      typedPrint("Entrando na taverna...", Config.speed)
      tavern()
    elif option == 4:
      clearScreen()
      typedPrint("Procurando áreas...", Config.speed)
      areas()
