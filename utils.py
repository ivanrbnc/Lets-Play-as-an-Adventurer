import random
from skill import *
from area import *

menus = {
        1: citadel,
        2: brook_forest,
        3: slime_mountain,
        4: fishman_beach,
        5: graveyard,
        6: boss_dimension, 
        7: "Show Current Stats",
        8: "Save and Quit"
    }

boss_menus = {
        1: dark_mage_floor,
        2: dark_knight_floor,
    }

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

    base_damage = character.strength * skill.base_strength_percentage + character.magic * skill.base_magic_percentage

    # Calculate dodge chance based on agility
    dodge_chance = min(0.5, character.agility / 100)  # Maximum dodge chance is 50%

    if random.random() < dodge_chance:
        print(f"{target.name} dodged the attack!")
        return 0  # No damage is dealt due to successful dodge

    total_damage = base_damage - target.defense * 0.25
    return max(5, total_damage)

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
    elif area_choice == 7:
        return False, 7 # Player stays in the current area
    elif area_choice == 8: # Saving game
        return None, 8
    else:
        return True, area_choice
    
def citadel_heal(player):
    player.hp = player.max_hp
    player.stamina = player.max_stamina
    player.mana = player.max_mana

def choose_boss_tier(boss_menus):
    display_menu(boss_menus.values())
    chosen_area = get_numeric_input("Enter the number of boss tier: ", 1, len(boss_menus))
    return boss_menus.get(chosen_area)