from pokemonlib.pokemonDataDownload import GetPokeAPI as PkApi
from pokemonlib.GameClasses import PokemonClass as Pkmn
from pokemonlib.GameClasses import UIClass as UI

import configparser


config = configparser.ConfigParser()
config.read('config.ini')
if config.sections() == []:
    config["Updater"] = {
        "auto-update pokemons": True,
        "auto-update attacks": True
    }
    with open("config.ini", "w") as f:
        config.write(f)
if config["Updater"]["auto-update pokemons"] == True:
    PkApi.pokegetapi()

UI.graphictest()
pikachu = Pkmn.Pokemon(25)
