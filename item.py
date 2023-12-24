class Item:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        pass    

    def __str__(self):
        return self.name

class Physical_Weapon(Item):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength

    def display_info(self):
        print(f"Weapon: {self.name}, Strength: {self.strength}")

class Magical_Weapon(Item):
    def __init__(self, name, magic):
        super().__init__(name)
        self.magic = magic

    def display_info(self):
        print(f"Weapon: {self.name}, Magic: {self.magic}")

class Armor(Item):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense

    def display_info(self):
        print(f"Armor: {self.name}, Defense: {self.defense}")

class Boots(Item):
    def __init__(self, name, agility):
        super().__init__(name)
        self.agility = agility

    def display_info(self):
        print(f"Boots: {self.name}, Agility: {self.agility}")

wooden_stick = Physical_Weapon("Wooden Stick", 10)
sharp_bone = Physical_Weapon("Sharp Bone", 11)
blob = Magical_Weapon("Blob", 9)

leather_clothes = Armor("Leather Clothes", 10)
leather_boots = Boots("Leather Boots", 10)

grimoire = Magical_Weapon("Grimoire", 275)
excalibur = Physical_Weapon("Excalibur", 275)