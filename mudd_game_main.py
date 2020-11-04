#Stew Towle
#October 2020
# This is the main file to run a mudd style game

import MuddCharacter
import MuddRoom
import useful_function

print("Welcome to the Mudd")
print("In this world you type your commands and then press enter.")

def character_creation():
    """This function facilitates character creation"""
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
    return character

def start_prompt():
    player = character_creation()
    if useful_function.is_yes(input("Would you like to start the game, y/n?")):
        start_game(player, 0)
    else:
        response = input("would you like to start over? (y/n)")
        if useful_function.is_yes(response):
            start_prompt()
        else:
            print("Thanks for playing in the mudd, see ya swirly cone.")

def create_world(num_rooms):
    the_world = []
    for i in range(num_rooms):
        the_world.append(MuddRoom.MuddRoom(i, 0))
        the_world[i].randomize_room()
    return the_world

def run_input(doing, player, room):
    """takes an action, player and room and returns True if the game ends, otherwise returns False
    and alters the mutables it was passed (hopefully) to reflect the action
    """
    doing = str(doing).lower()
    if 'help' in doing:
        print("try typing look around, go to something, or exit followed by a direction with an exit")
    elif 'look around' in doing:
        print(room.look_around())
    elif 'exit' in doing:
        room.exit_attempt(doing)

def start_game(player_char, game_type):
    """This function puts a created character in the game world and begins the mudd"""
    print("You wake up in a room, facing north")
    game_over = False
    player_input = None
    world_map = create_world(8)
    if game_type == 1:
        current_room = world_map[0]
        while game_over == False:
            print("you see", current_room.get_description())
            player_input = input("what do you do: " + "\n")
            game_over = run_input(player_input, player_char, current_room)

start_prompt()