class Player:
    def __init__(self, username):
        self.username = username
        self.level = 1
        self.require_to_level_up = 100
        self.xp = 0
        self.max_hp = 100
        self.hp = 100
        self.strength = 100
        self.max_stamina = 100
        self.stamina = 100
        self.magic = 100
        self.max_mana = 100
        self.mana = 100
        self.agility = 100
        self.defense = 100
        self.luck = 100
        self.skills = ["Punch", "Stab", "Wish"]

    def display_stats(player):
        print("\nPlayer Stats:")
        print(f"Username: {player.username}")
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
        print(f"Skills: {', '.join(player.skills)}")
        print()

    def check_exp(player):
        if player.xp > player.require_to_level_up:
            player.level += 1
            player.xp = 0
            player.strength += 5
            player.max_hp += 5
            player.hp = player.max_hp
            player.max_stamina += 5
            player.stamina = player.max_stamina
            player.magic += 5
            player.max_mana += 5
            player.mana = player.max_mana
            player.agility += 5
            player.defense += 5
            player.luck += 5

            print("You have leveled up! Current level: " + str(player.level) + "\n")
            