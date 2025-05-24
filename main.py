#Run this to play the game!

from menus.menu import menu
from areas.tavern import tavernIntro
from menus.classSelection import start
from history.villages.villageVentogard import ventogardIntro
from areas.fundition import joinItens
from player.inventory import inventory
from areas.fundition import showItens
from areas.blacksmith import blacksmithIntro
from resources.duel import duel
from assets.things import DicesAnimation

# joinItens("pocao de cura", "pluma de fenix")
duel("Slime")
