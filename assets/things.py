#File made by: Kauan

import random
import os
import time
from assets.config import Char
from assets.itens import Village

startTime = 0

#Starts an timer (it will be used on the saved games, at the game over and at the final page.)
def startTimer():
  global tempoComeco
  startTime = time.time()

#Just clear the screen, based on your OS.
def clearScreen():
  if os.name == 'nt':  # Windows
    os.system('cls')
  else:  # Linux ou macOS
    os.system('clear')

#Makes the print like an 'typing' print. You can change the speed by going on 'assets/config.py at the config class'
def typedPrint(text, speed):
  for i in text:
    print(i, end='', flush=True)
    time.sleep(speed)

def classUpdate():
  if Char.Name == "Aton":
    Char.classplayer = 1
    Char.health = 100
    Char.mana = 50
    Char.attack = 1.5
    Char.weapon = "Espada gasta"
  else:
    Char.classplayer = 2
    Char.health = 120
    Char.mana = 100
    Char.attack = 1.3
    Char.weapon = "Cajado antigo"


def randomVillage():
  choice = random.choice(Village.village_names)
  Village.village_names.remove(choice)
  if len(Village.village_names) == 0:
    return "Você não pode mais visitar vilas."
  return choice

