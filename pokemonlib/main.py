import logging
import configparser

from .pokemonDataDownload import GetPokeAPI as PkApi
from .GameClasses import PokemonClass as Pkmn
from .GameClasses import UIClass as UI


log = logging.getLogger("Main")
log.setLevel(logging.DEBUG)

# Read the config.ini file to decide if pokemons should be updated
config = configparser.ConfigParser()
config.read('config.ini')

if config.sections() == []:  # If config is Null Create it with default parameters

    config["Config Version"] = {  # Used to check if this config is compatible with the current software version.
        "version (DON'T MODIFY)": 1
    }
    config["Updater"] = {
        "auto-update pokemons": True,
        "auto-update attacks": False,
    }
    config["Modules To Start"] = {
        "UI": True,
        "Pokemon Class Test": True,
    }
    with open("config.ini", "w") as f:
        config.write(f)
    log.info("Created new config file")
    input("Press Enter when you finished editing your config file.")


try:

    if config["Updater"]["auto-update pokemons"] == True:
        PkApi.pokegetapi()

    if config["Updater"]["auto-update attacks"] == True:
        raise NotImplementedError("Attacks are not implemented for the moment")

    if config["Modules To Start"]["UI"] == True:
        log.debug("Starting graphic Test.")
        UI.graphictest()

    if config["Modules To Start"]["Pokemon Class Test"] == True:
        Pkmn.testPokemonClass(log)

except KeyError:  # If one of the keys aaren't found then Use default config
    # Log the error as "Warning" for the user to use a correct config
    log.error("Invalid config File. Using default configuration. To create a new config file, delete the old"+""
              " config.ini")
