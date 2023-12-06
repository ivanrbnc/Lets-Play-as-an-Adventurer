class Skill:
    def __init__(self, name, base_strength_percentage, stamina_cost, base_magic_percentage, mana_cost):
        self.name = name
        self.base_strength_percentage = base_strength_percentage
        self.stamina_cost = stamina_cost
        self.base_magic_percentage = base_magic_percentage
        self.mana_cost = mana_cost

    def __str__(self):
        return self.name

# Base Skill For All
punch = Skill("Punch", 0.5, 0, 0.0, 0)

# Player
stab = Skill("Stab", 0.35, 25, 0.0, 0)
wish = Skill("Wish", 0.0, 0, 0.35, 25)

# Monster
bite = Skill("Bite", 0.15, 15, 0.0, 0)
smash = Skill("Smash", 0.25, 25, 0.0, 0)

book_of_skill = {}

book_of_skill["Punch"] = punch
book_of_skill["Stab"] = stab
book_of_skill["Wish"] = wish
book_of_skill["Bite"] = bite
book_of_skill["Smash"] = smash