import random
from monster import Monster

def display_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def player_attack(player, monster, skill):
    damage = calculate_damage(player, skill)
    monster.hp -= damage
    attack_log = f"{player.username} used {skill} and dealt {damage} damage to {monster.name}. {monster.name}'s HP: {monster.hp}"
    print(attack_log)
    return attack_log

def monster_attack(player, monster):
    # For simplicity, monster's attack is a basic one
    damage = calculate_damage(monster, "Basic Attack")
    player.hp -= damage
    monster_attack_log = f"{monster.name} used Basic Attack and dealt {damage} damage to {player.username}. {player.username}'s HP: {player.hp}"
    print(monster_attack_log)
    return monster_attack_log

def calculate_damage(character, skill):
    base_damage = character.strength * 0.15

    # Skill set for player
    if skill == "Stab":
        if character.stamina < 25:
            skill = "Punch"
        else:
            character.stamina -= 25
            if character.stamina < 0:
                character.stamina = 0
            base_damage = character.strength * 0.55

    elif skill == "Wish":
        if character.mana < 25:
            skill = "Punch"
        else:
            character.mana -= 25
            if character.mana < 0:
                character.mana = 0
            base_damage = character.magic * 0.55    

    total_damage = base_damage + random.randint(-5, 5)  # Add some randomness
    return int(max(0, total_damage))  # Ensure damage is non-negative

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

def choose_menu():
    menus = ["Citadel", "Brook Forest", "Slime Mountain", "Fishman Beach", "Graveyard", "Show Current Stats", "Save and Quit"]
    print("Choose an area:")
    display_menu(menus)
    return get_numeric_input("Enter the number of the area: ", 1, len(menus))

def battle(player, monster):
    print(f"\nBattle Start: {player.username} vs {monster.name}")
    combat_log = []

    while player.hp > 0 and monster.hp > 0:
        # Player's turn
        print("\nPlayer's Turn:")
        display_menu(player.skills)
        choice = get_numeric_input("Choose a skill: ", 1, len(player.skills))

        # Perform player's action
        if choice == 1:
            attack_log = player_attack(player, monster, "Punch")
        elif choice == 2:
            attack_log = player_attack(player, monster, "Stab")
        elif choice == 3:
            attack_log = player_attack(player, monster, "Wish")

        combat_log.append(attack_log)

        # Monster's turn
        print("\nMonster's Turn:")
        monster_attack_log = monster_attack(player, monster)
        combat_log.append(monster_attack_log)

    if player.hp <= 0:
        combat_log.append("You were defeated. Returning to Citadel.")
        return True, 1 # Return to Citadel

    elif monster.hp <= 0:
        combat_log.append(f"You defeated {monster.name}! Gained {monster.xp_reward} XP.")
        player.xp += monster.xp_reward
        player.check_exp()

    print("\nCombat Log:")
    for log_entry in combat_log:
        print(log_entry)

    area_choice = choose_menu()
    if area_choice == 1:  # Citadel
        return True, 1  # Player stays in the current area
    elif area_choice == 6:
        return False, 6 # Player stays in the current area
    elif area_choice == 7: # Saving game
        return None, 7
    else:
        return True, area_choice  # Player stays in the current area
    
def citadel_heal(player):
    player.hp = player.max_hp
    player.stamina = player.max_stamina
    player.mana = player.max_mana

def current_monster(monster_name):
    # Get the specific stats for the chosen monster
    if monster_name == "Weak Goblin":
        current_monster = Monster(monster_name, 100, 25, 55, 5, 15, 3)
    elif monster_name == "Spear Goblin":
        current_monster = Monster(monster_name, 100, 35, 55, 8, 11, 5)
    elif monster_name == "Bow Goblin":
        current_monster = Monster(monster_name, 100, 45, 35, 3, 7, 5)
    elif monster_name == "Slime":
        current_monster = Monster(monster_name, 55, 5, 5, 5, 5, 3)
    elif monster_name == "Slimemorph":
        current_monster = Monster(monster_name, 75, 15, 15, 15, 15, 8)
    elif monster_name == "Weak Fishman":
        current_monster = Monster(monster_name, 100, 25, 55, 5, 15, 3)
    elif monster_name == "Spear Fishman":
        current_monster = Monster(monster_name, 100, 35, 55, 8, 11, 5)
    elif monster_name == "Bow Fishman":
        current_monster = Monster(monster_name, 100, 45, 35, 3, 7, 5)
    elif monster_name == "Weak Skeleton":
        current_monster = Monster(monster_name, 25, 15, 15, 8, 3, 2)
    elif monster_name == "Armored Skeleton":
        current_monster = Monster(monster_name, 75, 35, 25, 8, 25, 15)
    else:
        print("Invalid monster choice.")
        return None
    return current_monster