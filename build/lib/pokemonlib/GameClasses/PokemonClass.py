import os  # for finding the relative path to pokemon_data
import json  # for parsing pokemon_data json files
import random  # for generating IV or other random values
import logging  # for printing data
from pokemonlib.misc import Exeptions  # for initialisation exceptions

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
logPokemon = logging.getLogger("Main.PokemonClass")
logPokemon.setLevel(logging.DEBUG)


class Pokemon(object):
    # noinspection PyTypeChecker
    def __init__(self, pokemon_id=1):
        """
        Pokemon is the base class of all pokemon objects. It stores the data and stats of the pokemons.
        It also generates the base stats of a pokemon basing on it's id.
        Usage: p = Pokemon(pokemon_id)
        Result: 'Pokemon detected as ´" + self.name + "´ has finished initializing.'
        """

        # Pokemon ID to recognize what pokemon it is even if self.name is changed (For Example Zoroarks
        # illusions or Dittos transformation)
        self.__id = pokemon_id

        pokemon = []
        path = os.getcwd()  # Gets the relative path from main.py

        # Decides if using \ for windows or / for mac and linux in the path
        if os.name == "nt":
            path += "\\pokemonlib\\pokemon_data\\pokemon_properties\\"
        else:
            path += "/pokemonlib/pokemon_data/pokemon_properties/"

        # Search in pokemon_data for the data of the pokemon depending on the ID
        for filename in os.listdir(path):
            if filename != "pokemon_" + str(self.__id) + ".json":
                continue
            else:
                f = open(path + filename, "r")
                pokemon = json.load(f)
                f.close()
                break

        # When There are no properties in the list raise an error
        if pokemon == []:
            raise Exeptions.IdNotReferenced("The pokemon_data with id " + str(self.__id) +
                                            " was not found in the directory ´" + path +
                                            "´. Make sure it is in a file named pokemon_(id of the pokemon_data).json")

        # Sets all the base pokemon data to object variables. If any needed information is missing
        # raise an error
        try:
            stats = pokemon["stats"]
            self.name = pokemon["name"]
            self._hp = stats["hp"]
            self._defph = stats["defense"]
            self._defsp = stats["special-defense"]
            self._attkph = stats["attack"]
            self._attksp = stats["special-defense"]
            self._speed = stats["speed"]
            self._lv = 1
            self._types = pokemon["types"]
            self._attacks = {1: ["Thunderbolt", 20, True], 2: ["Poop", 40, True], 3: ["Earthquake", 40, True],
                             4: ["Scratch", 40, True]}
            self._iv = random.randint(0, 31)

        except KeyError:
            raise Exeptions.InvalidPokemonData("Some needed data is missing in ´" + path + filename + "´. Please "
                                               + "ensure that the name, base stats, attacks and the type are included."
                                               + "")

        logPokemon.info("Pokemon detected as ´" + pokemon["name"] + "´ has finished initializing.")

    def getstats(self):
        """
        Gets all the stats of the pokemon and return them in form of a Dictionary.
        Usage: getstats()
        Returns: {'hp', 'def', 'defsp', 'attk', 'attksp', 'attacks'=[]}
        """
        return {"hp": self._hp, "def": self._defph, "defsp": self._defsp, "attk": self._attkph,
                "attksp": self._attksp, "speed": self._speed, "attacks": self._attacks}


class Team:
    def __init__(self, pokemon1, pokemon2=None, pokemon3=None, pokemon4=None, pokemon5=None, pokemon6=None):
        templist = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
        self.__pokemonlist = []
        for pokemon in templist:
            if pokemon is not None:  # Check if this argument was passed
                if isinstance(pokemon, Pokemon):  # Basic check
                    self.__pokemonlist.append(pokemon)
                else:
                    raise Exeptions.NotAPokemon("Argument was passed that wasn't an instance of pokemon class")
            else:
                self.__pokemonlist.append(None)

    def __str__(self):
        return_message = "The team contains "
        for pokemon in self.__pokemonlist:
            return_message += pokemon.name + " and "
        return return_message[:-5]

    @property
    def full(self):
        for pokemon in self.__pokemonlist:
            if pokemon is not None:
                continue
            return False
        return True

    def pop(self, pokemon_index):
        """
        Replaces a pokemon object with none and returns the Pokemon object.
        :param pokemon_index:
        :return:
        """
        return_value = self.__pokemonlist.pop(pokemon_index)
        if pokemon_index is 0:
            self.__pokemonlist.append(None)
        else:
            self.__pokemonlist.insert(pokemon_index, None)
        return return_value

    def insert(self, index, pokemon):
        """
        Add a pokemon to the team list. Returns True if setted successfully and False if something is already
        in the index passed.
        :param index:
        :param pokemon:
        :return:
        """
        if self.__pokemonlist[index] is not None:
            return False
        self.__pokemonlist[index] = pokemon
        return True

    def add(self, pokemon):
        """
        Adds a pokemon in the first Empty slot found. Returns False if None were found.
        :param pokemon:
        :return:
        """
        index = None
        try:
            index = self.__pokemonlist.index(None)
        except ValueError:
            return False
        self.__pokemonlist[index] = pokemon
        return True

    def transfer(self, BoxInstance, pokemon_index):
        """
        Transfers a pokemon object from this Team instance to a box instance.
        :param BoxInstance:
        :param pokemon_index:
        :return:
        """
        if not isinstance(BoxInstance, Box):
            raise Exeptions.InvalidInput("The argument passed to this method should be an instance of the Box Class")
        if BoxInstance.full is True:
            raise Exeptions.ListFull("Can't add any more items to the Box: It's full.")
        BoxInstance.add(self.__pokemonlist[pokemon_index])
        _ = self.pop(pokemon_index)
        return True

    def get_pokemon(self, index):
        """
        Get a pokemon of this instance using it's index
        :param index:
        :return:
        """
        return self.__pokemonlist[index]

    def get_all_pokemons(self):
        pokemon_list = []
        for pokemon in self.__pokemonlist:
            if pokemon is not None:
                pokemon_list.append(pokemon)


class Box(Team):
    def __init__(self, *args, **kwargs):
        templist = []
        self.__pokemonlist = []
        if "MaxPokemon" in kwargs:
            self.MaxPokemon = kwargs["MaxPokemon"]
        else:
            self.MaxPokemon = 50

        for _ in range(self.MaxPokemon):
            templist.append(None)

        for pkmn in args:
            length = 0
            for p in templist:
                if p is not None:
                    length += 1
            logPokemon.debug(str(length))
            logPokemon.debug(templist)
            logPokemon.debug(len(templist))
            templist[length] = pkmn

        for pos, pkmn in kwargs.items():
            if pos == "MaxPokemon":
                continue
            try:
                pos = [int(s) for s in pos.split() if s.isdigit()][0]
                templist[pos] = pkmn
            except IndexError:
                logPokemon.info("An Unvalid keyword arg was given. Handling it as a normal arg.")
                length = 0
                for p in templist:
                    if p is not None:
                        length += 1
                logPokemon.debug(str(length))
                logPokemon.debug(templist)
                logPokemon.debug(len(templist))
                templist[length] = pkmn

        if len(templist) - 1 > self.MaxPokemon:
            raise ValueError("You entered contradictory values: More pokemons than the max capacity of the box")

        for pokemon in templist:
            if pokemon is not None:  # Check if this argument was passed
                if isinstance(pokemon, Pokemon):  # Basic check
                    self.__pokemonlist.append(pokemon)
                else:
                    raise Exeptions.NotAPokemon("Argument was passed that wasn't an instance of pokemon class")
            else:
                self.__pokemonlist.append(pokemon)

    def __len__(self):
        length = 0
        for p in self.__pokemonlist:
            if p is not None:
                length += 1
        return length

    def transfer(self, TeamInstance, pokemon_index):
        """
        Transfers a pokemon object from this Box instance to a Team instance.
        :param TeamInstance:
        :param pokemon_index:
        :return:
        """
        if not isinstance(TeamInstance, Team):
            raise Exeptions.InvalidInput("The argument passed to this method should be an instance of the Team Class")
        if TeamInstance.full is True:
            raise Exeptions.ListFull("Can't add any more items to the Team: It's full.")
        TeamInstance.add(self.__pokemonlist[pokemon_index])
        _ = self.pop(pokemon_index)
        return True


def testPokemonClass(loggerInstance=logPokemon, pokemonId=None):
    """
    A function that inits an object of the Pokemon Class to see if it works.
    :param pokemonId:
    :param loggerInstance:
    :return:
    """
    loggerInstance.info("Testing Pokemon Class:")
    if pokemonId is None:
        num = int(input("Give the id of a Pokemon to pass to the pokemon class"))  # Get id to pass to the __init__
        # function from Pokemon Class
    else:
        num = pokemonId

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
