#File made by: Kauan

import os, time
from assets.config import Char
from assets.things import clearScreen

#Just print the status.
def status():
    clearScreen()
    print(f"Nome: {Char.charName}")
    print(f"Vida: {Char.health}")
    if Char.arma == "":
       print("Arma: Mãos")
    else:
      print(f"Arma: {Char.weapon}")
    print(f"Ataque: {Char.attack}")
    print(f"Defesa: {Char.defense}")
    print(f"Moedas: {Char.coins}")
    time.sleep(5)