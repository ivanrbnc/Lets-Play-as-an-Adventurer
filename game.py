from player import *
from save_load import save_game, load_game
from utils import *
from area import *
from skill import *

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

    choice = choose_menu(menus.values())

    while True:
        if choice == 1:  # Citadel
            citadel_heal(player)  # Player can choose to heal in the Citadel
            print("Healing in Citadel...\n")
            choice = choose_menu(menus.values())
        elif choice == 7: # Current stats
            player.display_stats()
            choice = choose_menu(menus.values())
        elif choice == 8:  # Save and Quit
            save_game(player)
            print("Game saved. Quitting.")
            break
        elif choice in menus: # In one of the hunting grounds
            current_area = menus[choice]

            current_monster = current_area.choose_random_monster()

            # Error in inputs
            if current_monster == None:
                continue

            moving, choice = battle(player, current_monster)

            if moving == True:
                pass
            elif moving == None:
                save_game(player)
                print("Game saved. Quitting.")
                break
            elif moving == False:
                print("Staying in the current area.")
        else:
            print("Invalid area choice.")
            continue

if __name__ == "__main__":
    main()