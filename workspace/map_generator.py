# map_generator.py
import random
from world_builder import World
from map_generator import Map

class MapGenerator:
    def __init__(self):
        self.world = World()

    def generate_world_map(self):
        world_map = Map(self.world.width, self.world.height, self.world)

        for continent in self.world.continents:
            self.place_on_map(world_map, continent)

        return world_map

    def place_on_map(self, map, location):
        # Choose a random location on the map to place the location
        x = random.randint(0, map.width - 1)
        y = random.randint(0, map.height - 1)

        # Ensure the location fits within the map
        while not self.location_fits(map, location, x, y):
            x = random.randint(0, map.width - 1)
            y = random.randint(0, map.height - 1)

        # Place the location on the map
        for dx in range(location.width):
            for dy in range(location.height):
                map.contents[x + dx][y + dy] = location

    def location_fits(self, map, location, x, y):
        # Check if a location fits within the map at a given position
        if x + location.width > map.width or y + location.height > map.height:
            return False

        # Check if the location overlaps with any existing locations
        for dx in range(location.width):
            for dy in range(location.height):
                if map.contents[x + dx][y + dy] is not None:
                    return False

        return True
