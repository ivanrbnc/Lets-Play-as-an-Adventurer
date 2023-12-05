import pickle

def save_game(player):
    with open("savefile.txt", "wb") as file:
        pickle.dump(player, file)

def load_game():
    try:
        with open("savefile.txt", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None