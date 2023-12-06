import random
from monster import *

class Area:
    def __init__(self, name, monsters):
        self.name = name
        self.monsters = monsters

    def choose_random_monster(self):
        return random.choice(self.monsters)
    
    def __str__(self):
        return self.name

citadel = Area("Citadel", [])
brook_forest = Area("Brook Forest", [weak_goblin, spear_goblin, bow_goblin])
slime_mountain = Area("Slime Mountain", [slime, slimemorph])
fishman_beach = Area("Fishman Beach", [weak_fishman, spear_fishman, bow_fishman])
graveyard = Area("Graveyard", [weak_skeleton, armored_skeleton])
