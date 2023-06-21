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

                num_regions_per_country = random.randint(2, 5)  # Generate a random number of regions per country
                for _ in range(num_regions_per_country):
                    region_name = name_gen.generate_region_name()
                    region_desc = desc_gen.generate_region_description()
                    region = Region(region_name, region_desc)
                    country.add_location(region)

                    num_states_per_region = random.randint(4, 8)  # Generate a random number of states per region
                    for _ in range(num_states_per_region):
                        state_name = name_gen.generate_state_name()
                        state_desc = desc_gen.generate_state_description()
                        state = State(state_name, state_desc)
                        region.add_location(state)

                        num_rivers_per_state = random.randint(1, 2)  # Generate a random number of rivers per state
                        for _ in range(num_rivers_per_state):
                            river_name = name_gen.generate_river_name()
                            river_desc = desc_gen.generate_river_description()
                            river = River(river_name, river_desc)
                            state.add_location(river)

                        num_cities_per_state = random.randint(3, 10)  # Generate a random number of cities per state
                        num_towns_per_state = random.randint(3, 7)  # Generate a random number of towns per state
                        num_villages_per_state = random.randint(3, 7)  # Generate a random number of villages per state

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

                        num_forests_per_state = random.randint(1, 3)  # Generate a random number of forests per state
                        for _ in range(num_forests_per_state):
                            forest_name = name_gen.generate_forest_name()
                            forest_desc = desc_gen.generate_forest_description()
                            forest = Forest(forest_name, forest_desc)
                            state.add_location(forest)

                        num_fields_per_state = random.randint(1, 3)  # Generate a random number of fields per state
                        for _ in range(num_fields_per_state):
                            field_name = name_gen.generate_field_name()
                            field_desc = desc_gen.generate_field_description()
                            field = Field(field_name, field_desc)
                            state.add_location(field)

                        num_ruins_per_state = random.randint(1, 3)  # Generate a random number of ruins per state
                        for _ in range(num_ruins_per_state):
                            ruins_name = name_gen.generate_ruins_name()
                            ruins_desc = desc_gen.generate_ruins_description()
                            ruins = Ruins(ruins_name, ruins_desc)
                            state.add_location(ruins)

                        num_mountains_per_state = random.randint(1, 3)  # Generate a random number of mountains per state
                        for _ in range(num_mountains_per_state):
                            mountain_name = name_gen.generate_mountain_name()
                            mountain_desc = desc_gen.generate_mountain_description()
                            mountain = Mountain(mountain_name, mountain_desc)
                            state.add_location(mountain)

                        num_deserts_per_state = random.randint(1, 3)  # Generate a random number of deserts per state
                        for _ in range(num_deserts_per_state):
                            desert_name = name_gen.generate_desert_name()
                            desert_desc = desc_gen.generate_desert_description()
                            desert = Desert(desert_name, desert_desc)
                            state.add_location(desert)

                        num_lakes_per_state = random.randint(1, 3)  # Generate a random number of lakes per state
                        for _ in range(num_lakes_per_state):
                            lake_name = name_gen.generate_lake_name()
                            lake_desc = desc_gen.generate_lake_description()
                            lake = Lake(lake_name, lake_desc)
                            state.add_location(lake)

                        num_buildings_per_state = random.randint(1, 3)  # Generate a random number of buildings per state
                        for _ in range(num_buildings_per_state):
                            building_name = name_gen.generate_building_name()
                            building_desc = desc_gen.generate_building_description()
                            building = Building(building_name, building_desc)
                            state.add_location(building)

                            num_castles_per_building = random.randint(1, 2)  # Generate a random number of castles per building
                            for _ in range(num_castles_per_building):
                                castle_name = name_gen.generate_castle_name()
                                castle_desc = desc_gen.generate_castle_description()
                                castle = Castle(castle_name, castle_desc)
                                building.add_location(castle)

                            num_dungeons_per_building = random.randint(1, 2)  # Generate a random number of dungeons per building
                            for _ in range(num_dungeons_per_building):
                                dungeon_name = name_gen.generate_dungeon_name()
                                dungeon_desc = desc_gen.generate_dungeon_description()
                                dungeon = Dungeon(dungeon_name, dungeon_desc)
                                building.add_location(dungeon)

                    num_rooms_per_dungeon = random.randint(3, 6)  # Generate a random number of rooms per dungeon
                    for _ in range(num_rooms_per_dungeon):
                        room_name = name_gen.generate_room_name()
                        room_desc = desc_gen.generate_room_description()
                        room = Room(room_name, room_desc)
                        dungeon.add_location(room)

        self.locations += generate_locations()
        map = Map()
        map.generate()
        self.maps.append(map)

    def save(self):
        os.makedirs(self.name.lower(), exist_ok=True)
        with open(os.path.join(self.name.lower(), 'location_definitions.py'), 'w') as f:
            f.write("from location_classes import Universe, Planet, Continent, Country, Region, State, Province, "
                    "City, Village, Town, Landmark, Forest, Field, Ruins, Mountain, Desert, Lake, River, Building, "
                    "Castle, Dungeon, Room\n\n")
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
