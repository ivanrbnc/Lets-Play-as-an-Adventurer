import random
from skill import *

class Monster:
    def __init__(self, name, hp, strength, stamina, magic, mana, agility, defense, xp_reward, skill_set):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.stamina = stamina
        self.magic = magic
        self.mana = mana
        self.agility = agility
        self.defense = defense
        self.xp_reward = xp_reward
        self.skill_set = skill_set
        self.initial_hp = hp
        self.initial_stamina = stamina
        self.initial_mana = mana

    def respawn(self):
        self.hp = self.initial_hp
        self.stamina = self.initial_stamina
        self.mana = self.initial_mana

    # For simplicity, every monster has the same skill set.
    def choose_random_skill(self):
        return random.choice(self.skill_set)

    def __str__(self):
        return self.name

weak_goblin = Monster("Weak Goblin", 100, 25, 55, 0, 0, 5, 15, 3, [bite, smash])
spear_goblin = Monster("Spear Goblin", 100, 35, 55, 0, 0, 8, 11, 5, [bite, smash])
bow_goblin = Monster("Bow Goblin", 100, 45, 35, 0, 0, 3, 7, 5, [bite, smash])
slime = Monster("Slime", 55, 5, 5, 0, 0, 5, 5, 3, [bite, smash])
slimemorph = Monster("Slimemorph", 75, 15, 15, 0, 0, 15, 15, 8, [bite, smash])
weak_fishman = Monster("Weak Fishman", 100, 25, 55, 0, 0, 5, 15, 3, [bite, smash])
spear_fishman = Monster("Spear Fishman", 100, 35, 55, 0, 0, 8, 11, 5, [bite, smash])
bow_fishman = Monster("Bow Fishman", 100, 45, 35, 0, 0, 3, 7, 5, [bite, smash])
weak_skeleton = Monster("Weak Skeleton", 25, 15, 15, 0, 0, 8, 3, 2, [bite, smash])
armored_skeleton = Monster("Armored Skeleton", 75, 35, 25, 0, 0, 8, 25, 15, [bite, smash])
dark_knight = Monster("Dark Knight", 500, 200, 100, 200, 100, 100, 100, 100, [heart_curse])
