import random
from monster import *

class Area:
    def __init__(self, name, monsters, spawn_rate):
        self.name = name
        self.monsters = monsters
        self.spawn_rate = spawn_rate

    def choose_random_monster(self):
        return random.choices(self.monsters, weights=self.spawn_rate)[0]
        
    def __str__(self):
        return self.name

citadel = Area("Citadel", [], [])
brook_forest = Area("Brook Forest", [weak_goblin, spear_goblin, bow_goblin], [0.6, 0.2, 0.2])
slime_mountain = Area("Slime Mountain", [slime, slimemorph], [0.8, 0.2])
fishman_beach = Area("Fishman Beach", [weak_fishman, spear_fishman, bow_fishman], [0.6, 0.2, 0.2])
graveyard = Area("Graveyard", [weak_skeleton, armored_skeleton], [0.9, 0.1])

boss_dimension = Area("Boss Dimension", [], [])
dark_mage_floor = Area("Dark Mage Floor", [dark_mage], [1])
dark_knight_floor = Area("Dark Knight Floor", [dark_knight], [1])