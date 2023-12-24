from skill import *
from item import *

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
        self.skills = [stab, spark, flee]
        self.backpack = {}
        self.weapon = None
        self.armor = None
        self.boots = None

    def add_item(self, item):
        # Check if an item with a similar name is already in the backpack
        similar_item = next((existing_item for existing_item in self.backpack if existing_item.name == item.name), None)

        if similar_item is not None:
            # If a similar item is found, increment its quantity
            self.backpack[similar_item] += 1
        else:
            # If no similar item is found, add the new item to the backpack
            self.backpack[item] = 1
    
    def display_storage(self):
        if not bool(self.backpack):
            print(f"{self.name}'s backpack is empty.")
        else:
            print(f"{self.name}'s Backpack")
            print("="*15)
            for item, quantity in self.backpack.items():
                print(f"{item.name}: {quantity}")
        
    def current_arsenal(self):
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"Boots: {self.boots}")

    def display_stats(self):
        print("\nself Stats:")
        print(f"Username: {self.name}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")
        print(f"HP: {self.hp}")

        print(f"Strength: {self.strength}", end='')
        if self.weapon is not None and isinstance(self.weapon, Physical_Weapon):
            print(f" [{self.weapon.strength}]")
        else:
            print("")

        print(f"Stamina: {self.stamina}")

        print(f"Magic: {self.magic}", end='')
        if self.weapon is not None and isinstance(self.weapon, Magical_Weapon):
            print(f" [{self.weapon.magic}]")
        else:
            print("")

        print(f"Mana: {self.mana}")

        print(f"Agility: {self.agility}", end='')
        if self.boots is not None:
            print(f" [{self.boots.agility}]")
        else:
            print("")

        print(f"Defense: {self.defense}", end='')
        if self.armor is not None:
            print(f" [{self.armor.defense}]")
        else:
            print("")

        print(f"Luck: {self.luck}")
        print(f"Skills: {[skill.name for skill in self.skills]}")
        print()

    def check_exp(self):
        if self.xp > self.require_to_level_up:
            self.level += 1
            self.xp = 0
            self.require_to_level_up *= 1.5
            self.strength += 10
            self.max_hp += 10
            self.hp = self.max_hp
            self.max_stamina += 10
            self.stamina = self.max_stamina
            self.magic += 10
            self.max_mana += 10
            self.mana = self.max_mana
            self.agility += 10
            self.defense += 10
            self.luck += 10

            print("You have leveled up! Current level: " + str(self.level) + "\n")