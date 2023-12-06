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

weak_goblin = Monster("Weak Goblin", 55, 15, 35, 0, 0, 5, 15, 15, [bite, smash, bite])
spear_goblin = Monster("Spear Goblin", 65, 21, 45, 0, 0, 8, 11, 21, [spear_throwing, bite])
bow_goblin = Monster("Bow Goblin", 75, 23, 55, 0, 0, 3, 7, 25, [shoot, bite])
slime = Monster("Slime", 25, 5, 15, 0, 0, 5, 5, 12, [gulping, bite])
slimemorph = Monster("Slimemorph", 100, 12, 55, 15, 55, 15, 15, 25, [delusion, gulping, bite])
weak_fishman = Monster("Weak Fishman", 55, 15, 35, 0, 0, 5, 15, 15, [bite, smash, bite])
spear_fishman = Monster("Spear Fishman", 65, 21, 45, 0, 0, 8, 11, 21, [spear_throwing, bite])
bow_fishman = Monster("Bow Fishman", 75, 23, 55, 0, 0, 3, 7, 25, [shoot, bite])
weak_skeleton = Monster("Weak Skeleton", 25, 6, 15, 0, 0, 8, 3, 12, [bone_torner, smash])
armored_skeleton = Monster("Armored Skeleton", 115, 25, 20, 0, 0, 8, 25, 28, [bone_spike, bone_torner, smash])

dark_mage = Monster("Dark Mage", 150, 25, 75, 100, 250, 50, 35, 100, [lesser_dark_hit, lesser_curse])
dark_knight = Monster("Dark Knight", 500, 180, 100, 180, 100, 100, 100, 250, [dark_dimension, heart_curse, smash])