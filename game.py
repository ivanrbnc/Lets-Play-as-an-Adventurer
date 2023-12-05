import random
from player import Player
from save_load import save_game, load_game
from utils import *

def main():
    # Try to load player data from the save file
    player = load_game()

    if player is not None:
        print(f"Welcome back, {player.username}!")
    else:
        # If the save file doesn't exist, create a new player
        username = input("Enter your adventurer's name: ")
        player = Player(username)
        save_game(player)    

    menus = {
        1: "Citadel",
        2: {"name": "Brook Forest", "monsters": ["Weak Goblin", "Spear Goblin", "Bow Goblin"]},
        3: {"name": "Slime Mountain", "monsters": ["Slime", "Slimemorph"]},
        4: {"name": "Fishman Beach", "monsters": ["Weak Fishman", "Spear Fishman", "Bow Fishman"]},
        5: {"name": "Graveyard", "monsters": ["Weak Skeleton", "Armored Skeleton"]},
        6: "Show Current Stats",
        7: "Save and Quit"
    }

    choice = choose_menu()

    while player.hp > 0:

        if choice == 1:  # Citadel
            citadel_heal(player)  # Player can choose to heal in the Citadel
            print("Healing in Citadel...\n")
            choice = choose_menu()
        elif choice == 6: # Current stats
            player.display_stats()
            choice = choose_menu()
        elif choice == 7:  # Save and Quit
            save_game(player)
            print("Game saved. Quitting.")
            should_quit = True  # Set a variable to indicate that the player wants to quit
            break
        elif choice in menus: # In one of the hunting grounds
            current_area = menus[choice]
            monster_name = random.choice(current_area["monsters"])

            current_monster = find_current_monster(monster_name)

            # Error in inputs
            if current_monster == None:
                continue

            moving, choice = battle(player, current_monster)

            if moving == True:
                pass
            elif moving == None:
                save_game(player)
                print("Game saved. Quitting.")
                should_quit = True  # Set a variable to indicate that the player wants to quit
                break
            elif moving == False:
                print("Staying in the current area.")
        else:
            print("Invalid area choice.")
            continue

    if should_quit:
        # Additional cleanup or farewell message can be added here
        pass

if __name__ == "__main__":
    main()