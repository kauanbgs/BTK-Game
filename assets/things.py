#File made by: Kauan

import os
import time

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
