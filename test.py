import unittest
from random import randint
from pokemonlib.Core.Pokemon import Pokemon, Box, Team


class TestPokemon(unittest.TestCase):
    def test_pokemon_init(self):
        identifier = randint(1, 800)
        pokemon = Pokemon(identifier)
        self.assertEqual(pokemon._Pokemon__id, identifier)

    def test_pokemon_auto_naming(self):
        identifier = 25
        pokemon = Pokemon(identifier)
        self.assertEqual(pokemon.name, "pikachu")

    def test_pokemon_stats(self):
        identifier = 25
        pokemon = Pokemon(identifier)
        attacks = {1: ["Thunderbolt", 20, True], 2: ["Poop", 40, True], 3: ["Earthquake", 40, True],
                   4: ["Scratch", 40, True]}
        self.assertEqual(pokemon.get_stats(), {"speed": 90, "defsp": 50, "attksp": 50, "def": 40, "attk": 55,
                                               "hp": 35, "attacks": attacks})


class TestTeam(unittest.TestCase):
    def test_team_one_pokemon(self):
        identifier = randint(1, 800)
        pokemon = Pokemon(identifier)
        team = Team(pokemon)
        self.assertEqual(team._Team__pokemonlist[0]._Pokemon__id, identifier)

    def test_team_many_pokemon(self):
        identifier = randint(1, 800)
        pokemon = Pokemon(identifier)
        identifier2 = randint(1, 800)
        pokemon2 = Pokemon(identifier2)
        team = Team(pokemon, pokemon2)
        self.assertEqual(team._Team__pokemonlist[0]._Pokemon__id, identifier)
        self.assertEqual(team._Team__pokemonlist[1]._Pokemon__id, identifier2)


class TestBox(unittest.TestCase):
    def test_box_init_one_pokemon(self):
        identifier = randint(1, 800)
        pokemon = Pokemon(identifier)
        box = Box(pokemon)
        self.assertEqual(box._Box__pokemonlist[0]._Pokemon__id, identifier)

    def test_box_init_many_pokemon(self):
        identifier = randint(1, 800)
        pokemon = Pokemon(identifier)
        identifier2 = randint(1, 800)
        pokemon2 = Pokemon(identifier2)
        box = Box(pokemon, pokemon2)
        self.assertEqual(box._Box__pokemonlist[0]._Pokemon__id, identifier)
        self.assertEqual(box._Box__pokemonlist[1]._Pokemon__id, identifier2)

    def test_box_team_transfer(self):
        pokemon1 = Pokemon(randint(1, 800))
        pokemon2 = Pokemon(randint(1, 800))
        pokemon3 = Pokemon(randint(1, 800))
        team = Team(pokemon1)
        box1 = Box()
        box2 = Box(pokemon2)
        box2.transfer(team, 0)
        box1.add(pokemon3)
        team.transfer(box1, 1)
        team.transfer(box2, 0)
        self.assertEqual(box2._Box__pokemonlist[0], pokemon1)
        self.assertEqual(box1._Box__pokemonlist[0], pokemon3)
        self.assertEqual(box1._Box__pokemonlist[1], pokemon2)


if __name__ == '__main__':
    unittest.main()
