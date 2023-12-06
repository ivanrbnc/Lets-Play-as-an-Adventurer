import random
from skill import *

class Monster:
    def __init__(self, name, hp, strength, stamina, magic, mana, agility, defense, xp_reward):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.stamina = stamina
        self.magic = magic
        self.mana = mana
        self.agility = agility
        self.defense = defense
        self.xp_reward = xp_reward

    # For simplicity, every monster has the same skill set.
    def choose_random_skill(self):
        return random.choice([bite, smash])

    def __str__(self):
        return self.name

weak_goblin = Monster("Weak Goblin", 100, 25, 55, 0, 0, 5, 15, 3)
spear_goblin = Monster("Spear Goblin", 100, 35, 55, 0, 0, 8, 11, 5)
bow_goblin = Monster("Bow Goblin", 100, 45, 35, 0, 0, 3, 7, 5)
slime = Monster("Slime", 55, 5, 5, 0, 0, 5, 5, 3)
slimemorph = Monster("Slimemorph", 75, 15, 15, 0, 0, 15, 15, 8)
weak_fishman = Monster("Weak Fishman", 100, 25, 55, 0, 0, 5, 15, 3)
spear_fishman = Monster("Spear Fishman", 100, 35, 55, 0, 0, 8, 11, 5)
bow_fishman = Monster("Bow Fishman", 100, 45, 35, 0, 0, 3, 7, 5)
weak_skeleton = Monster("Weak Skeleton", 25, 15, 15, 0, 0, 8, 3, 2)
armored_skeleton = Monster("Armored Skeleton", 75, 35, 25, 0, 0, 8, 25, 15)