import requests
import json
import os


def pokedatagetfromapi():

    for idn in range(0, 807):  # For all existing pokemon
        ff = False  # Reset this variable used to verify if first iteration of next for loop
        types = []  # Reset type list
        p_type = " "  # Reset the string that will be printed
        stats = {}  # Reset dictionary responsible for pokemon statistics
        # idn += 1   idk anymore why I added that

        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(idn)+"/")  # Get data in json from the api

        for x in response.json()["types"]:  # For each type the pokemon has
            if ff:  # if not first iteration
                p_type += " and "  # add an "and" in the string that will be printed
            ff = True  # Variable changed: Not first iteration
            p_type += str(x["type"]["name"])  # add the type of th pokemon to what will be printed
            types.append(str(x["type"]["name"]))  # transfer the values to another list
        name = response.json()["name"]  # Get the pokemon's name

        # print out the data collected
        print("Pokemon with id " + str(idn) + " is named " + name + ", and is a" + p_type + " type pokemon_data.")

        for x in response.json()["stats"]:  # for each stat of the pokemon
            stats[x["stat"]["name"]] = x["base_stat"]  # add the base stat in a dictionary with stat name as key

        # make a final dictionary containing all the needed data
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
            # Save the pokedata variable as json
            with open(path + "/pokemon_" + str(idn) + ".json", "w+") as f:
                json.dump(pokedata, f)

            print("Saved " + str(idn))

        except FileNotFoundError:  # If directory doesn't exist
            os.mkdir(otherpath)  # create the pokemon_data directory
            os.mkdir(path)  # create the pokemon_properties sub-directory

            with open(path + "/pokemon_" + str(idn) + ".json", "w+") as f:  # Now try again to save
                json.dump(pokedata, f)

            print("Saved " + str(idn))
