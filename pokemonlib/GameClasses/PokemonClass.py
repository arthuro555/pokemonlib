import os
import json
import random
from pokemonlib.misc import Exeptions


class Pokemon:
    def __init__(self, pokemon_id=1):
        self.id = pokemon_id
        pokemon = []
        localPath = os.getcwd().split("\\")
        print(localPath)
        path = ""
        for x in range(len(localPath)):
            path += str(localPath[x]) + "\\"
        path += "pokemonlib\\pokemon_data\\pokemon_properties\\"
        for filename in os.listdir(path + "\\"):
            if filename != "pokemon_" + str(self.id) + ".json":
                continue
            else:
                f = open(path+filename, "r")
                pokemon = json.load(f)
                print("Pokemon ´" + pokemon["name"] + "´ initializing.")
                f.close()
                break
        if pokemon == []:
            raise Exeptions.IdNotReferenced("The pokemon_data with id " + str(self.id) + " was not found in the directory ´"+path+"´. Make sure it is in a file named pokemon_(id of the pokemon_data).json")

        stats = pokemon["stats"]
        self.name = pokemon["name"]
        self.hp = stats["hp"]
        self.defph = stats["defense"]
        self.defsp = stats["special-defense"]
        self.attkph = stats["attack"]
        self.attksp = stats["special-defense"]
        self.lv = 1
        self.types = pokemon["types"]
        self.attacks = {1: ["Thunderbolt", 20, True], 2: ["Poop", 40, True], 3: ["Earthquake", 40, True], 4: ["Scratch", 40, True]}
        self.iv = random.randint(0, 31)

    def getstats(self):
        return {"hp": self.hp, "pp": self.pp, "def": self.defph, "defsp": self.defsp, "attk": self.attkph, "attksp": self.attksp, "attacks": self.attacks}

    def getstats(self):
        if self.id == 292:
            return {"pv": 1, }
        return()
