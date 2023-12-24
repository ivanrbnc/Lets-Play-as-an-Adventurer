import random
from player import *
from skill import *
from area import *
from monster import *

menus = {
        1: citadel,
        2: brook_forest,
        3: slime_mountain,
        4: fishman_beach,
        5: graveyard,
        6: boss_dimension, 
        7: "Show Current Stats",
        8: "Show Backpack",
        9: "Save and Quit"
    }

boss_menus = {
        1: dark_mage_floor,
        2: dark_knight_floor,
        3: "Back",
    }

storage_menus = {
        1: "Backpack",
        2: "Arsenal",
        3: "Back",
    }

def get_numeric_input(prompt, min_value, max_value):
    while True:
        try:
            choice = int(input(prompt))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu(options):
    print()
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def choose_menu(menus):
    display_menu(menus)
    return get_numeric_input("Enter the number of the area: ", 1, len(menus))

def choose_skill(player):
    display_menu(player.skills)
    skill_index = get_numeric_input("Enter the number of the skill: ", 1, len(player.skills))
    chosen_skill = player.skills[skill_index - 1]
    return chosen_skill

def player_attack(player, monster, skill):
    damage = calculate_damage(player, skill, monster)
    monster.hp -= damage

    if (monster.hp < 0):
        monster.hp = 0

    attack_log = f"{player.name} used {skill} and dealt {damage} damage to {monster.name}. {monster.name}'s HP: {monster.hp}"
    print(attack_log)
    return attack_log

def monster_attack(player, monster):
    chosen_skill = monster.choose_random_skill()
    damage = calculate_damage(monster, chosen_skill, player)
    player.hp -= damage

    if (player.hp < 0):
        player.hp = 0

    monster_attack_log = f"{monster.name} used {chosen_skill} and dealt {damage} damage to {player.name}. {player.name}'s HP: {player.hp}"
    print(monster_attack_log)
    return monster_attack_log

def calculate_damage(character, skill, target):
    if character.stamina < skill.stamina_cost or character.mana < skill.mana_cost:
        print(f"Not enough stamina or mana to use {skill.name}. Using Punch instead.")
        skill = punch
    else:
        character.stamina -= skill.stamina_cost
        character.mana -= skill.mana_cost

    if isinstance(character, Player) and character.weapon is not None: # For Player that wear weapon
        if isinstance(character.weapon, Physical_Weapon): # Physical
            base_damage = (character.strength + character.weapon.strength) * skill.base_strength_percentage + character.magic * skill.base_magic_percentage
        else: # Magic
            base_damage = character.strength * skill.base_strength_percentage + (character.magic + character.weapon.magic) * skill.base_magic_percentage
    else: # For Monster
        base_damage = character.strength * skill.base_strength_percentage + character.magic * skill.base_magic_percentage

    # Calculate dodge chance based on agility
    if isinstance(character, Player) and character.boots is not None: # For Player that wear boots
        dodge_chance = min(0.5, (character.agility + character.boots.agility) / 100)  # Maximum dodge chance is 50%
    else: # For Monster 
        dodge_chance = min(0.5, character.agility / 100)  # Maximum dodge chance is 50%

    if random.random() < dodge_chance:
        print(f"{target.name} dodged the attack!")
        return 0  # No damage is dealt due to successful dodge

    if isinstance(target, Player) and target.armor is not None: # For Attacking a Player that wear armor
        total_damage = base_damage - (target.defense + target.armor.defense) * 0.25
    else: # For Attacking a Monster
        total_damage = base_damage - target.defense * 0.25
        
    return round(max(random.randint(1, 5), total_damage), 2)

def battle(player, monster):
    print(f"\nBattle Start: {player.name} vs {monster.name}")
    combat_log = []

    while player.hp > 0 and monster.hp > 0:
        # Player's turn
        print("Player's Turn:")
        chosen_skill = choose_skill(player)

        if (chosen_skill == flee):
            print("You flee.")
            return True, 1

        attack_log = player_attack(player, monster, chosen_skill)
        combat_log.append(attack_log)

        if (monster.hp <= 0):
            dropped_items = get_dropped_items(monster.drop_item, monster.drop_chance)
            if dropped_items: # If there is at least one item dropped..
                for item in dropped_items:
                    player.add_item(item)

                item_log = f"Item Dropped: {', '.join(item.name for item in dropped_items)}"

                combat_log.append(item_log)
            break

        # Monster's turn
        print("Monster's Turn:")
        monster_attack_log = monster_attack(player, monster)
        combat_log.append(monster_attack_log)

    print("\nCombat Log:")
    for log_entry in combat_log:
        print(log_entry)

    if player.hp <= 0:
        print("You were defeated. Returning to Citadel.")
        return True, 1 # Return to Citadel
    elif monster.hp <= 0:
        print(f"You defeated {monster.name}! Gained {monster.xp_reward} XP.")
        player.xp += monster.xp_reward
        player.check_exp() # Checking if the player leveled up
        monster.respawn() # Respawn..

    area_choice = choose_menu(menus.values())
    if area_choice == 1:  # Citadel
        return True, 1
    elif area_choice == list(menus.keys())[-3]: # Current Stats
        return False, list(menus.keys())[-1] # Player stays in the current area
    elif area_choice == list(menus.keys())[-2]: # Backpack
        return False, list(menus.keys())[-2] # Player stays in the current area
    elif area_choice == list(menus.keys())[-1]: # Saving game
        return None, list(menus.keys())[-1]
    else:
        return True, area_choice
    
def citadel_heal(player):
    player.hp = player.max_hp
    player.stamina = player.max_stamina
    player.mana = player.max_mana

def choose_boss_tier(boss_menus):
    display_menu(boss_menus.values())
    chosen_area = get_numeric_input("Enter the number of boss tier: ", 1, len(boss_menus))
    if (chosen_area == 3):
        print("You scared.")
        return None
    return boss_menus.get(chosen_area)

def storage_menu(player):
    while True:
        display_menu(storage_menus.values())
        choice = get_numeric_input("Enter the number of activity you want to do: ", 1, len(boss_menus))
        if (choice == 1): # Backpack
            player.display_storage()
        elif (choice == 2): # Arsenal
            player.current_arsenal()
            arsenal_change = input("\nDo you want to change your arsenal setup? (Y/N)\n")

            if arsenal_change == "N":
                continue
            elif arsenal_change != "Y":
                print("Invalid Input.")

            while True:
                player.current_arsenal()
                arsenal_to_change = get_numeric_input("\nEnter the number of arsenal you want to change: ", 1, 3)
                
                if (arsenal_to_change == 1): # Weapon
                    # Filter items that are instances of Weapon from the dictionary
                    weapon_items_list = [key for key, value in player.backpack.items() if isinstance(key, Physical_Weapon) or isinstance(key, Magical_Weapon)]
                    if (weapon_items_list == []):
                        print("You got no weapon available!")
                    else:
                        display_menu(weapon_items_list)
                        weapon_input = get_numeric_input("Enter the number of weapon you want to wear: ", 1, len(weapon_items_list))  
                        weapon_to_wear = weapon_items_list[weapon_input - 1]
                        player.weapon = weapon_to_wear
                        print(f"You are currently wearing {weapon_to_wear.name}")

                elif (arsenal_to_change == 2): # Armor 
                    # Filter items that are instances of Armor from the dictionary
                    armor_items_list = [key for key, value in player.backpack.items() if isinstance(key, Armor)]
                    if (armor_items_list == []):
                        print("You got no armor available!")
                    else:
                        display_menu(armor_items_list)
                        armor_input = get_numeric_input("Enter the number of armor you want to wear: ", 1, len(armor_items_list))  
                        armor_to_wear = armor_items_list[armor_input - 1]
                        player.armor = armor_to_wear
                        print(f"You are currently wearing {armor_to_wear.name}")  
                
                elif (arsenal_to_change == 3): # Boots
                    # Filter items that are instances of Boots from the dictionary
                    boots_items_list = [key for key, value in player.backpack.items() if isinstance(key, Boots)]
                    if (boots_items_list == []):
                        print("You got no boots available!")
                    else:
                        display_menu(boots_items_list)
                        boots_input = get_numeric_input("Enter the number of boots you want to wear: ", 1, len(boots_items_list))  
                        boots_to_wear = boots_items_list[boots_input - 1]
                        player.boots = boots_to_wear
                        print(f"You are currently wearing {boots_to_wear.name}")

                arsenal_done = input("\nFinish setting up? (Y/N)\n")

                if arsenal_done == "Y":
                    break
                elif arsenal_done != "N":
                    print("Invalid Input.")

        elif (choice == 3): # Back
            break