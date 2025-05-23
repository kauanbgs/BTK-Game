from assets.itens import Itens
from player.status import Char
from assets.config import Config
from player.inventory import inventory
from assets.things import clearScreen
import time
import random
from assets.things import typedPrint, DicesAnimation, d20, attackAnimation, magicAttackAnimation
from assets.itens import Spells

def duel(enemyName, enemyHealth, enemyAttack, enemyMana, enemySpells, boss):
    while Char.health > 0 and enemyHealth > 0:
        clearScreen()
        print(f"{enemyName} --- {enemyHealth}HP --- {enemyAttack}ATK --- {enemyMana}MP")
        print(f"{Char.Name} --- {Char.health}HP --- {Char.attack}ATK --- {Char.mana}MP")
        print("[1] - Atacar")
        print("[2] - Usar magia")

        option = input("Escolha uma opção: ")

        if not option.isdigit():
            clearScreen()
            print("Opção inválida!")
            time.sleep(1)
            continue
        option = int(option)

        if option == 1:
            result = d20()
            DicesAnimation()
            typedPrint(f"O dado rolou: {result}", Config.speed)
            time.sleep(1)
            clearScreen()
            dano = Char.attack * result
            enemyHealth -= dano
            attackAnimation()
            clearScreen()
            print(f"Você atacou {enemyName} e causou {dano} de dano!")
            time.sleep(2)

        elif option == 2:
            if Char.mana <= 0 or len(Char.spells) == 0:
                clearScreen()
                print("Você não tem mana ou não possui magias!")
                time.sleep(1)
                continue

            clearScreen()
            print("Escolha uma magia:")
            for i, spell_name in enumerate(Char.spells):
                spell_data = Spells.spells_database[spell_name]
                print(f"[{i}] - {spell_name} - {spell_data['custo']}MP - {spell_data.get('dano', spell_data.get('cura'))} {'DANO' if spell_data['tipo']=='dano' else 'CURA'}")

            spellOption = input("Escolha uma magia: ")

            if not spellOption.isdigit():
                clearScreen()
                print("Opção inválida!")
                time.sleep(1)
                continue

            spellOption = int(spellOption)

            if spellOption < 0 or spellOption >= len(Char.spells):
                clearScreen()
                print("Opção inválida!")
                time.sleep(1)
                continue

            spell_name = Char.spells[spellOption]
            spell_data = Spells.spells_database[spell_name]

            if Char.mana < spell_data['custo']:
                clearScreen()
                print("Mana insuficiente!")
                time.sleep(1)
                continue

            Char.mana -= spell_data['custo']

            if spell_data['tipo'] == "dano":
                dano = spell_data['dano']
                enemyHealth -= dano
                magicAttackAnimation(spell_data['ascii'])
                print(f"Você usou {spell_name} e causou {dano} de dano!")

            elif spell_data['tipo'] == "cura":
                cura = spell_data['cura']
                Char.health += cura
                magicAttackAnimation(spell_data['ascii'])
                print(f"Você usou {spell_name} e curou {cura} de vida!")

            time.sleep(2)

        # Verifica se o inimigo morreu
        if enemyHealth <= 0:
            clearScreen()
            print(f"{enemyName} foi derrotado!")
            break

        # --- Turno do Inimigo ---
        clearScreen()
        print(f"Turno de {enemyName}...")
        time.sleep(1)

        if enemyMana > 0 and len(enemySpells) > 0:
            enemyChoice = "magia" if boss else random.choice(["ataque", "magia"])
        else:
            enemyChoice = "ataque"

        if enemyChoice == "ataque":
            result = d20()
            DicesAnimation()
            dano_inimigo = enemyAttack * result
            Char.health -= dano_inimigo
            print(f"{enemyName} atacou e causou {dano_inimigo} de dano!")
            time.sleep(2)

        elif enemyChoice == "magia":
            spell_name = random.choice(enemySpells)
            spell_data = Spells.spells_database[spell_name]

            if enemyMana >= spell_data['custo']:
                enemyMana -= spell_data['custo']

                if spell_data['tipo'] == "dano":
                    dano = spell_data['dano']
                    Char.health -= dano
                    print(f"{enemyName} usou {spell_name} e causou {dano} de dano!")

                elif spell_data['tipo'] == "cura":
                    cura = spell_data['cura']
                    enemyHealth += cura
                    print(f"{enemyName} usou {spell_name} e se curou em {cura} de vida!")

                time.sleep(2)
            else:
                result = d20()
                DicesAnimation()
                dano_inimigo = enemyAttack * result
                Char.health -= dano_inimigo
                print(f"{enemyName} atacou e causou {dano_inimigo} de dano!")
                time.sleep(2)

        if Char.health <= 0:
            clearScreen()
            print("Você foi derrotado...")
            break
