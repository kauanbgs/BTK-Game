#File made by: Kauan


from assets.itens import Itens
from player.status import Char

def joinItens(base, material):
  if base not in Itens.base_itens:
    print("Item base não encontrado.")
    return
  if material not in Itens.materials:
    print("Material não encontrado.")
    return
  
  if base == "Espada" and material == "Bola de slime":
    Char.weapon = "Espada Pegajosa"
  elif base == "Espada" and material == "Essencia de fogo":
    Char.weapon = "Espada Inflamável"
  if base == "Espada" and material == "Escama de dragao":
    Char.weapon = "Espada Resistente"
  elif base == "Espada" and material == "Garra de lobo":
    Char.weapon = "Espada Afiada"
  elif base == "Espada" and material == "Pluma de fenix":
    Char.weapon = "Espada Magica"

  elif base == "Pocao de cura" and material == "Bola de slime":
    Char.item = "Pocao Pegajosa de Cura"
  elif base == "Pocao de cura" and material == "Essencia de fogo":
    Char.item = "Pocao Ardente de Cura"
  elif base == "Pocao de cura" and material == "Escama de dragao":
    Char.item = "Pocao Resistente de Cura"
  elif base == "Pocao de cura" and material == "Garra de lobo":
    Char.item = "Pocao Cortante de Cura"
  elif base == "Pocao de cura" and material == "Pluma de fenix":
    Char.item = "Pocao Magica Regenerativa"

  elif base == "Pocao de mana" and material == "Bola de slime":
    Char.item = "Pocao Pegajosa de Mana"
  elif base == "Pocao de mana" and material == "Essencia de fogo":
    Char.item = "Pocao Energizante"
  elif base == "Pocao de mana" and material == "Escama de dragao":
    Char.item = "Pocao Encantada"
  elif base == "Pocao de mana" and material == "Garra de lobo":
    Char.item = "Pocao Aguçada de Mana"
  elif base == "Pocao de mana" and material == "Pluma de fenix":
    Char.item = "Pocao de Mana Mística"

  elif base == "Pocao de forca" and material == "Bola de slime":
    Char.item = "Pocao Flexível de Forca"
  elif base == "Pocao de forca" and material == "Essencia de fogo":
    Char.item = "Pocao de Forca Ardente"
  elif base == "Pocao de forca" and material == "Escama de dragao":
    Char.item = "Pocao de Forca Escamada"
  elif base == "Pocao de forca" and material == "Garra de lobo":
    Char.item = "Pocao de Forca Selvagem"
  elif base == "Pocao de forca" and material == "Pluma de fenix":
    Char.item = "Pocao de Forca Renascente"

  if base == "Espada":
    print(f"Você criou uma {Char.weapon} com {base} e {material}.")
  elif base == "Pocao de cura":
    print(f"Você criou uma {Char.item} com {base} e {material}.")
  elif base == "Pocao de mana":
    print(f"Você criou uma {Char.item} com {base} e {material}.")
  elif base == "Pocao de forca":
    print(f"Você criou uma {Char.item} com {base} e {material}.")
  else:
    print("Item não encontrado.")
    return
  
  
  
  