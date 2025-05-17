#File made by: Kauan


import os, time
from assets.config import Char
from assets.things import clearScreen
from assets.things import typedPrint
from assets.things import classUpdate
from menus.menu import menu

def start():
  clearScreen()
  typedPrint("Você desperta, sentindo a areia fria sob seu corpo e o som das ondas quebrando na praia. \nAo abrir os olhos, percebe que está sozinho numa ilha deserta, cercado por uma densa floresta e um céu cinzento que promete tempestade.\n", 0.04)
  typedPrint("Enquanto tenta se levantar, algo chama sua atenção: duas armas repousam na areia, como se estivessem esperando por você.\n", 0.04)
  typedPrint("A primeira é uma \033[31mEspada gasta\033[0m pelo tempo, mas ainda forte — a arma dos Guerreiros.\n", 0.04)
  typedPrint("A segunda é um \033[31mCajado antigo\033[0m, adornado com símbolos arcanos que brilham fracamente — o instrumento dos Magos.\n", 0.04)
  typedPrint("\033[36mSua vida, Seu destino começam agora!\033[0m\n", 0.04)
  print("")
  time.sleep(3)

  while True:
    print("[1] - \033[33mEspada gasta\033[0m")
    print("[2] - \033[33mCajado antigo\033[0m")
    option = input("Digite sua escolha: ")

    if not option.isdigit():
      print("Opção inválida!")
      time.sleep(1)
      clearScreen()
      continue
    else:
      option = int(option)
    
    if option not in [1, 2]:
        print("Resposta inválida.")
        time.sleep(1)
        clearScreen()
        continue

    elif option == 1:
      Char.Name = "Aton"
      classUpdate()
      # history()]
      menu() # DELETE IT AFTER TESTING
    else:
      Char.Name = "Nextage"
      classUpdate()
      # history()
      menu() # DELETE IT AFTER TESTING

       