#Stew Towle
#October 2020
# This is the main file to run a mudd style game

import MuddCharacter
import useful_function

print("Welcome to the Town of Amaree")
print("In this world you type your commands and then press enter.")
print("For basic character creation press 1, for advanced press 2, for custom press 3")
creation_type = int(input("What style of character creation will you use? "))
if creation_type == 1:
    character = MuddCharacter.create_character(0)
elif creation_type == 2:
    character = MuddCharacter.create_character(1)
elif creation_type == 3:
    character = MuddCharacter.create_character(2)
else:
    character = MuddCharacter.create_character(0)
print("Your character", character.name, "is a", character.sort, character.get_job())
print("Your stats are: Vitality:", character.vit, "Strength:", character.str, 'Dexterity:', character.dex, 'Wisdom:', character.wis, 'Charisma:', character.cha)
print("You have a maximum hp (and current hp) of " + str(character.hp))