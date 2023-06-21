import os
import random
from map_generator import Map, generate_locations
from description_generator import DescriptionGenerator
from name_generator import NameGenerator
from map_generator import generate_maps
from location_classes import *

class World:
    def __init__(self, name="default", universe="one_alpha"):
        self.name = name
        self.universe = universe
        self.locations = []
        self.maps = []

    def generate(self):
        name_gen = NameGenerator()
        desc_gen = DescriptionGenerator()
        universe = Universe(name_gen.generate_universe_name(), desc_gen.generate_universe_description())
        self.locations.append(universe)

        planet_name = input("Enter the name of the planet: ")
        planet = Planet(planet_name, desc_gen.generate_planet_description())
        universe.add_location(planet)

        num_continents = random.randint(4, 7)  # Generate a random number of continents (4 to 7)
        for _ in range(num_continents):
            continent_name = name_gen.generate_continent_name()
            continent_desc = desc_gen.generate_continent_description()
            continent = Continent(continent_name, continent_desc)
            planet.add_location(continent)

            num_countries_per_continent = random.randint(3, 6)  # Generate a random number of countries per continent
            for _ in range(num_countries_per_continent):
                country_name = name_gen.generate_country_name()
                country_desc = desc_gen.generate_country_description()
                country = Country(country_name, country_desc)
                continent.add_location(country)

                num_states_per_country = random.randint(4, 8)  # Generate a random number of states per country
                for _ in range(num_states_per_country):
                    state_name = name_gen.generate_state_name()
                    state_desc = desc_gen.generate_state_description()
                    state = State(state_name, state_desc)
                    country.add_location(state)

                    num_cities_per_state = random.randint(3, 10)  # Generate a random number of cities per state
                    num_towns_per_state = random.randint(10, 30)  # Generate a random number of towns per state
                    num_villages_per_state = random.randint(20, 50)  # Generate a random number of villages per state

                    for _ in range(num_cities_per_state):
                        city_name = name_gen.generate_city_name()
                        city_desc = desc_gen.generate_city_description()
                        city = City(city_name, city_desc)
                        state.add_location(city)

                    for _ in range(num_towns_per_state):
                        town_name = name_gen.generate_town_name()
                        town_desc = desc_gen.generate_town_description()
                        town = Town(town_name, town_desc)
                        state.add_location(town)

                    for _ in range(num_villages_per_state):
                        village_name = name_gen.generate_village_name()
                        village_desc = desc_gen.generate_village_description()
                        village = Village(village_name, village_desc)
                        state.add_location(village)

        self.locations += generate_locations()
        map = Map()
        map.generate()
        self.maps.append(map)

    def save(self):
        os.makedirs(self.name.lower(), exist_ok=True)
        with open(os.path.join(self.name.lower(), 'location_definitions.py'), 'w') as f:
            f.write("from location_classes import Universe, Planet, Continent, Country, Region, State, Province, "
                    "City, Village, Town, Landmark\n\n")
            for location in self.locations:
                f.write(f"{location.name.lower().replace(' ', '_')} = {location.__class__.__name__}("
                        f'"{location.name}", "{location.description}")\n')
                if isinstance(location, Container):
                    for contained_location in location.locations:
                        f.write(f"{contained_location.name.lower().replace(' ', '_')} = "
                                f"{contained_location.__class__.__name__}("
                                f'"{contained_location.name}", "{contained_location.description}")\n')

def main():
    name = input("Enter the name of the world: ")
    universe_name = input("Enter the name of the universe (default: one_alpha): ")
    if not universe_name:
        universe_name = "one_alpha"
    world = World(name, universe_name)
    world.generate()
    world.save()

    generate_maps(world.name)

if __name__ == "__main__":
    main()
