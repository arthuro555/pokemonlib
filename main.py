import logging
from pokemonlib.pokemonDataDownload import GetPokeAPI as PkApi


log = logging.getLogger("Main")
log.setLevel(logging.INFO)

PkApi.download_pokemon_data()
