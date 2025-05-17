#File made by: Kauan


from player.status import Char
import os
import time
from assets.things import clearScreen
from assets.config import Config
from assets.config import Char
from menus.menu import menu
from assets.things import randomVillage
from history.villages.villageEldoria import eldoriaIntro


def areas():

  from assets.things import typedPrint

  clearScreen()
  Char.where = "Praia"
  print(f"Você está atualmente em: {Char.where}\n")
  print("Você pode ir para: ")
  print("[1] - Procurar vila")
    
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen()
    print("Opção inválida!")
    time.sleep(1)
    areas()
  else:
    option = int(option)
  
  if option == 1:
    clearScreen()
    if randomVillage() == "Eldoria":
      typedPrint("Você encontrou Eldoria!\n", Config.speed)
      time.sleep(0.5)
      eldoriaIntro()
    # elif randomVillage() == "Skalice":
    #   typedPrint("Você encontrou Skalice!\n", Config.speed)
    #   time.sleep(0.5)
    #   skaliceIntro()

  
  else:
    clearScreen()
    print("Opção não existente.")
    time.sleep(1)
    areas()