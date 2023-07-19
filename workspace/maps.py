# maps.py

import random
import os.path
import json
from location_definitions import *
from world_builder import World



class Map:
    def __init__(self, width, height, world):
        self.width = width
        self.height = height
        self.world = world
        self.contents = [[None for _ in range(height)] for _ in range(width)]

    def generate(self):
        if os.path.exists('location_definition.py'):
            self.generate_maps_from_definition()
        else:
            self.generate_maps_organically()

    def generate_maps_from_definition(self):
        # Read location_definition.py and generate maps based on the data
        # ...

        def generate_maps_organically(self):
            # Generate maps organically from the bottom up
            maps = [self.generate_continent_map(continent) for continent in self.world.continents]
            return maps
        
    def generate(self):
        if os.path.exists('location_definition.py'):
            self.generate_maps_from_definition()
        else:
            maps = self.generate_maps_organically()  # Store the returned list here

        with open('maps.json', 'w') as f:
            json.dump([map.__dict__ for map in maps], f)

    def generate_continent_map(self, continent):
        # Generate the map for a continent
        continent_map = Map(continent.width, continent.height)

        # Create nested map structure
        continent_map.contents = [self.generate_country_map(country) for country in continent.countries]
        return continent_map

    def generate_country_map(self, country):
        # Generate the map for a country
        country_map = Map(country.width, country.height)

        # Create nested map structure
        country_map.contents = [self.generate_city_map(city) for city in country.cities]
        return country_map

    def generate_city_map(self, city):
        # Generate the map for a city
        city_map = Map(city.width, city.height)

        # Create nested map structure
        city_map.contents = [self.generate_building_map(building) for building in city.buildings]
        return city_map

    def generate_building_map(self, building):
        # Generate the map for a building
        building_map = Map(building.width, building.height)

        # No further contents as we're at the building level
        return building_map

    def generate_castle_map(self, castle):
        # Generate the map for a castle
        castle_map = Map(castle.width, castle.height)

        # No further contents as we're at the building level
        return castle_map

    def generate_dungeon_map(self, dungeon):
        # Generate the map for a dungeon
        dungeon_map = Map(dungeon.width, dungeon.height)

        # No further contents as we're at the building level
        return dungeon_map


def generate_maps():
    world = World()
    map = Map(100, 100, world)
    map.generate()
    return map


if __name__ == "__main__":
    generated_map = generate_maps()
    # Use the generated_map for the game
