from skill import *
from utils import *

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.require_to_level_up = 100
        self.xp = 0
        self.max_hp = 95
        self.hp = 95
        self.strength = 35
        self.max_stamina = 75
        self.stamina = 75
        self.magic = 35
        self.max_mana = 75
        self.mana = 75
        self.agility = 30
        self.defense = 25
        self.luck = 100
        self.skills = [stab, wish, flee]
        
    def display_stats(player):
        print("\nPlayer Stats:")
        print(f"Username: {player.name}")
        print(f"Level: {player.level}")
        print(f"XP: {player.xp}")
        print(f"HP: {player.hp}")
        print(f"Strength: {player.strength}")
        print(f"Stamina: {player.stamina}")
        print(f"Magic: {player.magic}")
        print(f"Mana: {player.mana}")
        print(f"Agility: {player.agility}")
        print(f"Defense: {player.defense}")
        print(f"Luck: {player.luck}")
        print(f"Skills: {[skill.name for skill in player.skills]}")
        print()

    def check_exp(player):
        if player.xp > player.require_to_level_up:
            player.level += 1
            player.xp = 0
            player.require_to_level_up *= 1.5
            player.strength += 10
            player.max_hp += 10
            player.hp = player.max_hp
            player.max_stamina += 10
            player.stamina = player.max_stamina
            player.magic += 10
            player.max_mana += 10
            player.mana = player.max_mana
            player.agility += 10
            player.defense += 10
            player.luck += 10

            print("You have leveled up! Current level: " + str(player.level) + "\n")