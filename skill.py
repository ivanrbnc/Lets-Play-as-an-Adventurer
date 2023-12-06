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
punch = Skill("Punch", 0.1, 0, 0.0, 0)

# Player
stab = Skill("Stab", 0.35, 5, 0.0, 0)
wish = Skill("Wish", 0.0, 0, 0.35, 5)
flee = Skill("Flee", 0.0, 0, 0.0, 0)

# Monster
bite = Skill("Bite", 0.15, 2, 0.0, 0)
smash = Skill("Smash", 0.25, 3, 0.0, 0)
shoot = Skill("Shoot", 0.35, 5, 0.0, 0)
spear_throwing = Skill("Spear Throwing", 0.4, 6, 0.0, 0)
gulping = Skill("Gulping", 0.2, 3, 0.0, 0)
delusion = Skill("Delusion", 0.0, 0, 0.4, 6)
bone_torner = Skill("Bone Torner", 0.2, 3, 0.0, 0)
bone_spike = Skill("Bone Spike", 0.45, 6, 0.0, 0)

# Boss Level
lesser_dark_hit = Skill("Lesser Dark Hit", 0.3, 5, 0.0, 0)
lesser_curse = Skill("Lesser Curse", 0.55, 21, 0.3, 25)
dark_dimension = Skill("Dark Dimension", 1.0, 25, 0.0, 0)
heart_curse = Skill("Heart Curse", 0.75, 21, 0.5, 25)