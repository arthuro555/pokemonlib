import requests
import json
import os


def download_pokemon_data():
    print("Downloading pokemon data...")
    path = os.getcwd()
    pokemon_data_path = path + f"{os.path.sep}pokemonlib{os.path.sep}pokemon_data{os.path.sep}"
    pokemon_properties_path = f"{pokemon_data_path}pokemon_properties{os.path.sep}"
    print(pokemon_properties_path)

    if not os.path.exists(pokemon_data_path):
        os.mkdir(pokemon_data_path)
    if not os.path.exists(pokemon_properties_path):
        os.mkdir(pokemon_properties_path)

    all_pokemons = requests\
        .get("https://pokeapi.co/api/v2/pokemon/?limit=999999999")\
        .json()["results"]  # Get list of all pokemons

    for pokemon_endpoint in all_pokemons:
        pokemon_data = requests.get(pokemon_endpoint["url"]).json()

        types = []
        for x in pokemon_data["types"]:  # For each type the pokemon has
            types.append(str(x["type"]["name"]))  # transfer the values to another list

        stats = {}
        for x in pokemon_data["stats"]:  # for each stat of the pokemon
            stats[x["stat"]["name"]] = x["base_stat"]  # add the base stat in a dictionary with stat name as key

        simplified_pokemon_data = {"name": pokemon_data["name"], "types": types, "stats": stats}

        # Save it as json
        with open(pokemon_properties_path + "/pokemon_" + str(pokemon_data["id"]) + ".json", "w") as f:
            json.dump(simplified_pokemon_data, f)
            print(f"Saved {pokemon_data['name']}")
