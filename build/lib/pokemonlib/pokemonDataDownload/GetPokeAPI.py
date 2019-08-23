import requests
import json
import os


def pokegetapi():

    for idn in range(0, 807):
        ff = False
        types = []
        type = " "
        stats = {}
        idn += 1

        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(idn)+"/")

        for x in response.json()["types"]:
            if ff:
                type += " and "
            ff = True
            type += str(x["type"]["name"])
            types.append(str(x["type"]["name"]))
        name = response.json()["name"]

        print("Pokemon with id " + str(idn) + " is named " + name + ", and is a" + type + " type pokemon_data.")

        for x in response.json()["stats"]:
            stats[x["stat"]["name"]] = x["base_stat"]

        pokedata = {"name": name, "types": types, "stats": stats}

        path = os.getcwd()  # Gets the relative path from main.py

        # Decides if using \ for windows or / for mac and linux in the path
        if os.name == "nt":
            otherpath = path + "pokemonlib\\pokemon_data\\"
            path += "pokemonlib\\pokemon_data\\pokemon_properties\\"
        else:
            otherpath = path + "pokemonlib/pokemon_data/"
            path += "pokemonlib/pokemon_data/pokemon_properties/"

        try:

            with open(path + "/pokemon_" + str(idn) + ".json", "w+") as f:
                json.dump(pokedata, f)

            print("Saved " + str(idn))

        except FileNotFoundError:
            os.mkdir(otherpath)
            os.mkdir(path)

            with open(path + "/pokemon_" + str(idn) + ".json", "w+") as f:
                json.dump(pokedata, f)

            print("Saved " + str(idn))

