import logging  # Replacement for print() in cases it's not needed
import json  # Needed to Dump and Parse save files
import base64  # Additional layer of security for save files

from .PokemonClass import Pokemon  # Check if objects passed to player are Pokemon and not a chair or something

from pokemonlib.misc import Settings  # Import the project settings
from pokemonlib.misc import Security  # Encryption functions
from pokemonlib.misc import Exeptions  # Exceptions for when it goes wrong


playerlog = logging.getLogger("Main.PlayerClass")


class Player(object):
    def __init__(self, new=False, save=None, starter=None, password=None):
        if new:  # If there is no save to begin with
            self.__pokemon = []  # create a list of pokemons

            if starter is not None and isinstance(starter, Pokemon):  # If argument starter exists and is a Pokemon
                self.__pokemon.append(starter)  # Add it to the list

            self.__items = []  # Create the list of items

            save_data = {"pokemons": self.__pokemon, "items": self.__items}  # create a dictionary with all the data

            if Settings.POKEMON_LIKE_SAVES:  # If single save file
                with open("save.pksv", "w") as f:  # Save the data
                    if type(password) == str:  # If password valid
                        playerlog.info("Detected valid password input: Encryption enabled for this save file.")
                        save_data = base64.b85encode(Security.encrypt(json.dumps(save_data), password))
                    elif Settings.ENABLE_AUTO_ENCRYPTION_FOR_SAVE_FILES:  # If Automatic encryption Enabled
                        # encrypt the save_data before saving
                        save_data = base64.b85encode(Security.encrypt_default_password(json.dumps(save_data)))
                    else:
                        json.dump(save_data, f)
                    f.write(save_data)  # Write the data

            else:  # If multiple saves
                if type(save) == str:  # verify save file is a string
                    with open(save + ".pksv", "w") as f:
                        if type(password) == str:
                            playerlog.info("Detected valid password input: Encryption enabled for this save file.")
                            save_data = base64.b85encode(Security.encrypt(json.dumps(save_data), password))
                        elif Settings.ENABLE_AUTO_ENCRYPTION_FOR_SAVE_FILES:  # If Automatic encryption Enabled
                            # encrypt the save_data before saving
                            save_data = base64.b85encode(Security.encrypt_default_password(json.dumps(save_data)))
                        else:
                            save_data = json.dump(save_data, f)
                        f.write(save_data)

                    playerlog.info("New player created and saved")
                else:
                    playerlog.warning("New player instance created but not saved as no correct save filename was given")
                    playerlog.info("If you don't want to specify filename yourself, activate the Pokemon-like saves!")
        else:
            if Settings.POKEMON_LIKE_SAVES:  # If single save file
                with open("save.pksv", "r") as f:  # Save the data
                    if Settings.ENABLE_AUTO_ENCRYPTION_FOR_SAVE_FILES:  # If Automatic encryption Enabled
                        # Load and decrypt dictionnary
                        save_data = base64.b85decode(Security.decrypt_default_password(json.load(f)))
                    else:
                        save_data = json.load(f)

            else:  # If multiple saves
                if type(save) == str:  # verify save file is a string
                    with open(save + ".pksv", "r") as f:
                        save_data = json.load(f)
                    playerlog.info("New player created and saved")
                else:
                    playerlog.warning("New player instance created but not saved as no correct save filename was given")
                    playerlog.info("If you don't want to specify filename yourself, activate the Pokemon-like saves!")


class Trainer(Player):
    def __init__(self, pokemons):
        pass