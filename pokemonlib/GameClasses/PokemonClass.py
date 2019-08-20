import os  # for finding the relative path to pokemon_data
import json  # for parsing pokemon_data json files
import random  # for generating IV or other random values
import logging
from pokemonlib.misc import Exeptions  # for initialisation exceptions

logPokemon = logging.getLogger("Main.PokemonClass")


class Pokemon:
    def __init__(self, pokemon_id=1):
        """
        Pokemon is the base class of all pokemon objects. It stores the data and stats of the pokemons.
        It also generates the base stats of a pokemon basing on it's id.
        Usage: p = Pokemon(pokemon_id)
        Result: 'Pokemon detected as ´" + self.name + "´ has finished initializing.'
        """

        # Pokemon ID to recognize what pokemon it is even if self.name is changed (For Example Zoroarks
        # illusions or Dittos transformation)
        self.id = pokemon_id

        pokemon = []
        path = os.getcwd()  # Gets the relative path from main.py

        # Decides if using \ for windows or / for mac and linux in the path
        if os.name == "nt":
            path += "pokemonlib\\pokemon_data\\pokemon_properties\\"
        else:
            path += "pokemonlib/pokemon_data/pokemon_properties/"

        # Search in pokemon_data for the data of the pokemon depending on the ID
        for filename in os.listdir(path):
            if filename != "pokemon_" + str(self.id) + ".json":
                continue
            else:
                f = open(path + filename, "r")
                pokemon = json.load(f)
                f.close()
                break

        # When There are no properties in the list raise an error
        if pokemon == []:
            raise Exeptions.IdNotReferenced("The pokemon_data with id " + str(self.id) +
                                            " was not found in the directory ´" + path +
                                            "´. Make sure it is in a file named pokemon_(id of the pokemon_data).json")

        # Sets all the base pokemon data to object variables. If any needed information is missing
        # raise an error
        try:
            stats = pokemon["stats"]
            self.name = pokemon["name"]
            self.hp = stats["hp"]
            self.defph = stats["defense"]
            self.defsp = stats["special-defense"]
            self.attkph = stats["attack"]
            self.attksp = stats["special-defense"]
            self.lv = 1
            self.types = pokemon["types"]
            self.attacks = {1: ["Thunderbolt", 20, True], 2: ["Poop", 40, True], 3: ["Earthquake", 40, True],
                            4: ["Scratch", 40, True]}
            self.iv = random.randint(0, 31)
        except KeyError:
            raise Exeptions.InvalidPokemonData("Some needed data is missing in ´" + path + filename + "´. Please ensure"
                                               + " that the name, base stats, attacks and the type are included.")

        logPokemon.info("Pokemon detected as ´" + pokemon["name"] + "´ has finished initializing.")

    def getstats(self):
        """
        Gets all the stats of the pokemon and return them in form of a Dictionary.
        Usage: getstats()
        Returns: {'hp', 'def', 'defsp', 'attk', 'attksp', 'attacks'=[]}
        """
        return {"hp": self.hp, "def": self.defph, "defsp": self.defsp, "attk": self.attkph,
                "attksp": self.attksp, "attacks": self.attacks}


def testPokemonClass(loggerInstance=logPokemon):
    """
    A function that inits an object of the Pokemon Class to see if it works.
    :param loggerInstance:
    :return:
    """
    loggerInstance.info("Testing Pokemon Class:")
    num = int(input("Give the id of a Pokemon to pass to the pokemon class"))  # Get id to pass to the __init__
    # function from Pokemon Class

    if type(num) is int:
        num_poke = 0
        path = os.getcwd()  # Gets the relative path from main.py

        # Decides if using \ for windows or / for mac and linux in the path
        if os.name == "nt":
            path += "pokemonlib\\pokemon_data\\pokemon_properties\\"
        else:
            path += "pokemonlib/pokemon_data/pokemon_properties/"

        # Count the pokemon IDs
        for _ in os.listdir(path):
            num_poke += 1

        if num not in range(0, num_poke):
            raise Exeptions.IdNotReferenced("The id you entered is incorrect.")

    else:
        raise TypeError("Please enter an Integer.")

    pkmn = Pokemon(num)
    loggerInstance.info(pkmn.getstats())
    return True
