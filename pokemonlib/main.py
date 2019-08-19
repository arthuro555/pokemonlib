from pokemonlib.pokemonDataDownload import GetPokeAPI as PkApi
from pokemonlib.GameClasses import PokemonClass as Pkmn
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
print(config["Updater"]["auto-update pokemons"])
if config["Updater"]["auto-update pokemons"] == True:
    PkApi.pokegetapi()
#UI.graphictest()
pikachu = Pkmn.Pokemon(25)
