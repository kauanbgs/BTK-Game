#File made by: Kauan

import random
import os
import time
from assets.config import Char
from assets.itens import Village
from assets.itens import Flashback
from player.inventory import inventory
from assets.itens import Itens

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
    if not Village.village_names:
        return "Você não pode mais visitar vilas."
    
    choice = random.choice(Village.village_names)
    Village.village_names.remove(choice)
    return choice

def flashback():
    if not Flashback.flashbacks:
        return "Não existem mais flashbacks."
    
    choice = random.choice(Flashback.flashbacks)
    Flashback.flashbacks.remove(choice)
    return choice

def revealChar(npc_name, initial_text, final_text, speed=0.045):
    clearScreen()
    print("???: ", end="")
    typedPrint(initial_text + "\n", speed)
    
    print("???: ", end="")
    typedPrint(f"Meu nome é {npc_name}", speed)
    
    time.sleep(1)
    clearScreen()
    
    print(f"{npc_name}: {initial_text}")
    print(f"{npc_name}: Meu nome é {npc_name}, ", end="")
    typedPrint(final_text + "\n", speed)
    time.sleep(2)

def updateStatus(item):
  from player.inventory import inventory, inventoryItens

  clearScreen()

  dados = {}
  if item in Itens.base_itens:
    dados = Itens.base_itens[item]
  elif item in Itens.Itens_personalizados:
    dados = Itens.Itens_personalizados[item]
  else:
    print("Item inválido para uso.")
    time.sleep(1)
    inventory()
    return

  inventoryItens.remove(item)

  efeito_aplicado = False

  if "cura" in dados:
    Char.health += dados["cura"]
    print(f"Você ganhou {dados['cura']} de vida! Sua vida atual é: {Char.health}")
    efeito_aplicado = True
  if "mana" in dados:
    Char.mana += dados["mana"]
    print(f"Você recuperou {dados['mana']} de mana! Sua mana atual é: {Char.mana}")
    efeito_aplicado = True
  if "forca" in dados:
    Char.attack += dados["forca"]
    print(f"Você ganhou {dados['forca']} de força! Sua força atual é: {Char.attack}")
    efeito_aplicado = True

  if not efeito_aplicado:
    print("Esse item não teve efeito.")

  time.sleep(2)
  inventory()
  
    
