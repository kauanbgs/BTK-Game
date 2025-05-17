#File made by: Kauan


import os, time
from assets.config import Char
from assets.things import clearScreen
from assets.things import typedPrint
from assets.config import Config
from menus.menu import menu


def intro():
  clearScreen()
  typedPrint("E aqui começa sua história...\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Talvez você quisesse se tornar uma lenda, alguém cujo nome seria gravado em canções e sussurrado em tavernas por séculos.\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Ou talvez sua ambição fosse um pouco mais simples: juntar ouro suficiente para se tornar rico e viver uma vida de prostitutas e bebidas.\n", Config.speed)
  time.sleep(0.5)

  typedPrint(f"Seja qual for o caso, você é {Char.Name}, de Skalice:", Config.speed)
  if Char.classplayer == 1:
    typedPrint(" Um guerreiro, mestre da espada longa.\n", Config.speed)
  else:
    typedPrint(" Um mago, dominante do arcano.\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Seu caminho te trouxe até Eldoria, uma pequena vila, mas extremamente movimentada e cheia de aventuras.\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Todos os dias o sol se põe lentamente, e a lua brilha intensamente sobre as montanhas.\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Você caminha pelas ruas, observando o vilarejo ao seu redor. Nada fora do comum. Nada que indique que algo grande está prestes a acontecer.\n", Config.speed)
  time.sleep(0.5)

  typedPrint("Mas talvez, isso dependa de você.\n", Config.speed)
  time.sleep(0.5)
  menu()



  