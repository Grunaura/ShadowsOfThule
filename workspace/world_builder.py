import os
import random
import json
from map_generator import Map, generate_locations
from description_generator import DescriptionGenerator
from name_generator import NameGenerator
from map_generator import generate_maps
from location_classes import *

def load_locations_from_json(json_file):
    with open(json_file, 'r') as f:
        locations = json.load(f)
    return locations

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

        planet_name = input("What is the name of the world: ")
        planet = Planet(planet_name, desc_gen.generate_planet_description())
        universe.add_location(planet)

        # Load the locations from the JSON file.
        json_file = os.path.join(planet_name.lower(), 'map_data.json')
        locations = load_locations_from_json(json_file)

        # Now, add these locations to the planet.
        for location in locations.values():
            planet.add_location(location)

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

                num_regions_per_continent = random.randint(2, 5)  # Generate a random number of regions per continent
                for _ in range(num_regions_per_continent):
                    region_name = name_gen.generate_region_name()
                    region_desc = desc_gen.generate_region_description()
                    region = Region(region_name, region_desc)
                    continent.add_location(region)

                    num_provinces_per_country = random.randint(1, 3)  # Generate a random number of provinces per country
                    for _ in range(num_provinces_per_country):
                        province_name = name_gen.generate_province_name()
                        province_desc = desc_gen.generate_province_description()
                        province = Province(province_name, province_desc)
                        country.add_location(province)

                        num_rivers_per_province = random.randint(1, 2)  # Generate a random number of rivers per province
                        for _ in range(num_rivers_per_province):
                            river_name = name_gen.generate_river_name()
                            river_desc = desc_gen.generate_river_description()
                            river = River(river_name, river_desc)
                            province.add_location(river)

                        num_cities_per_province = random.randint(1, 3)  # Generate a random number of cities per province
                        for _ in range(num_cities_per_province):
                            city_name = name_gen.generate_city_name()
                            city_desc = desc_gen.generate_city_description()
                            city = City(city_name, city_desc)
                            province.add_location(city)

                            num_buildings_per_city = random.randint(10, 20)  # Generate a random number of buildings per city
                            for _ in range(num_buildings_per_city):
                                building_name = name_gen.generate_building_name()
                                building_desc = desc_gen.generate_building_description()
                                building = Building(building_name, building_desc)
                                city.add_location(building)

                        num_villages_per_province = random.randint(3, 5)  # Generate a random number of villages per province
                        for _ in range(num_villages_per_province):
                            village_name = name_gen.generate_village_name()
                            village_desc = desc_gen.generate_village_description()
                            village = Village(village_name, village_desc)
                            province.add_location(village)

                            num_buildings_per_village = random.randint(5, 9)  # Generate a random number of buildings per village
                            for _ in range(num_buildings_per_village):
                                building_name = name_gen.generate_building_name()
                                building_desc = desc_gen.generate_building_description()
                                building = Building(building_name, building_desc)
                                village.add_location(building)

                        num_towns_per_province = random.randint(2, 4)  # Generate a random number of towns per province
                        for _ in range(num_towns_per_province):
                            town_name = name_gen.generate_town_name()
                            town_desc = desc_gen.generate_town_description()
                            town = Town(town_name, town_desc)
                            province.add_location(town)

                            num_buildings_per_town = random.randint(8, 14)  # Generate a random number of buildings per town
                            for _ in range(num_buildings_per_town):
                                building_name = name_gen.generate_building_name()
                                building_desc = desc_gen.generate_building_description()
                                building = Building(building_name, building_desc)
                                town.add_location(building)

                        num_forests_per_region = random.randint(1, 3)  # Generate a random number of forests per region
                        for _ in range(num_forests_per_region):
                            forest_name = name_gen.generate_forest_name()
                            forest_desc = desc_gen.generate_forest_description()
                            forest = Forest(forest_name, forest_desc)
                            region.add_location(forest)

                            num_landmarks_per_forest = random.randint(1, 3)  # Generate a random number of landmarks per forest
                            for _ in range(num_landmarks_per_forest):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                forest.add_location(landmark)

                                num_ruins_per_forest = random.randint(1, 3)  # Generate a random number of ruins per forest
                                for _ in range(num_ruins_per_forest):
                                    ruin_name = name_gen.generate_ruin_name()
                                    ruin_desc = desc_gen.generate_ruin_description()
                                    ruin = Ruin(ruin_name, ruin_desc)
                                    forest.add_location(ruin)

                        num_swamps_per_region = random.randint(1, 3)  # Generate a random number of swamps per region
                        for _ in range(num_swamps_per_region):
                            swamp_name = name_gen.generate_swamp_name()
                            swamp_desc = desc_gen.generate_swamp_description()
                            swamp = Swamp(swamp_name, swamp_desc)
                            region.add_location(swamp)

                            num_landmarks_per_swamp = random.randint(1, 3)  # Generate a random number of landmarks per swamp
                            for _ in range(num_landmarks_per_swamp):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                swamp.add_location(landmark)

                                num_ruins_per_swamp = random.randint(1, 3)  # Generate a random number of ruins per swamp
                                for _ in range(num_ruins_per_swamp):
                                    ruin_name = name_gen.generate_ruin_name()
                                    ruin_desc = desc_gen.generate_ruin_description()
                                    ruin = Ruin(ruin_name, ruin_desc)
                                    swamp.add_location(ruin)

                        num_fields_per_region = random.randint(1, 3)  # Generate a random number of fields per region
                        for _ in range(num_fields_per_region):
                            field_name = name_gen.generate_field_name()
                            field_desc = desc_gen.generate_field_description()
                            field = Field(field_name, field_desc)
                            region.add_location(field)

                            num_landmarks_per_field = random.randint(1, 3)  # Generate a random number of landmarks per field
                            for _ in range(num_landmarks_per_field):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                field.add_location(landmark)

                                num_ruins_per_field = random.randint(1, 3)  # Generate a random number of ruins per field
                                for _ in range(num_ruins_per_field):
                                    ruin_name = name_gen.generate_ruin_name()
                                    ruin_desc = desc_gen.generate_ruin_description()
                                    ruin = Ruin(ruin_name, ruin_desc)
                                    field.add_location(ruin)

                        num_deserts_per_region = random.randint(1, 3)  # Generate a random number of deserts per region
                        for _ in range(num_deserts_per_region):
                            desert_name = name_gen.generate_desert_name()
                            desert_desc = desc_gen.generate_desert_description()
                            desert = Desert(desert_name, desert_desc)
                            region.add_location(desert)

                            num_landmarks_per_desert = random.randint(1, 3)  # Generate a random number of landmarks per desert
                            for _ in range(num_landmarks_per_desert):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                desert.add_location(landmark)

                                num_ruins_per_desert = random.randint(1, 3)  # Generate a random number of ruins per desert
                                for _ in range(num_ruins_per_desert):
                                    ruin_name = name_gen.generate_ruin_name()
                                    ruin_desc = desc_gen.generate_ruin_description()
                                    ruin = Ruin(ruin_name, ruin_desc)
                                    desert.add_location(ruin)

                        num_lakes_per_region = random.randint(1, 3)  # Generate a random number of lakes per region
                        for _ in range(num_lakes_per_region):
                            lake_name = name_gen.generate_lake_name()
                            lake_desc = desc_gen.generate_lake_description()
                            lake = Lake(lake_name, lake_desc)
                            region.add_location(lake)

                            num_landmarks_per_lake = random.randint(1, 3)  # Generate a random number of landmarks per lake
                            for _ in range(num_landmarks_per_lake):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                lake.add_location(landmark)

                        num_mountains_per_continent = random.randint(1, 3)  # Generate a random number of mountains per continent
                        for _ in range(num_mountains_per_continent):
                            mountain_name = name_gen.generate_mountain_name()
                            mountain_desc = desc_gen.generate_mountain_description()
                            mountain = Mountain(mountain_name, mountain_desc)
                            continent.add_location(mountain)

                            num_landmarks_per_mountain = random.randint(1, 3)  # Generate a random number of landmarks per mountain
                            for _ in range(num_landmarks_per_mountain):
                                landmark_name = name_gen.generate_landmark_name()
                                landmark_desc = desc_gen.generate_landmark_description()
                                landmark = Landmark(landmark_name, landmark_desc)
                                mountain.add_location(landmark)

                                num_ruins_per_mountain = random.randint(1, 3)  # Generate a random number of ruins per mountain
                                for _ in range(num_ruins_per_mountain):
                                    ruin_name = name_gen.generate_ruin_name()
                                    ruin_desc = desc_gen.generate_ruin_description()
                                    ruin = Ruin(ruin_name, ruin_desc)
                                    mountain.add_location(ruin)

        num_oceans = random.randint(4, 7)  # Generate a random number of oceans (4 to 7)
        for _ in range(num_oceans):
            ocean_name = name_gen.generate_ocean_name()
            ocean_desc = desc_gen.generate_ocean_description()
            ocean = Ocean(ocean_name, ocean_desc)
            planet.add_location(ocean)

        num_islands = random.randint(2, 8)  # Generate a random number of islands (2 to 8)
        for _ in range(num_islands):
            island_name = name_gen.generate_island_name()
            island_desc = desc_gen.generate_island_description()
            island = Island(island_name, island_desc)
            planet.add_location(island)

        self.locations += generate_locations()
        map = Map()
        map.generate()
        self.maps.append(map)

    def save(self):
        os.makedirs(self.name.lower(), exist_ok=True)
        with open(os.path.join(self.name.lower(), 'location_definitions.py'), 'w') as f:
            f.write("from location_classes import Universe, Planet, Continent, Country, Region, Province, City, Village, Town, "
                    "Landmark, Forest, Field, Ruin, Mountain, Desert, Lake, River, Building, Castle, Dungeon, Room, Ocean, Island\n\n")
            for location in self.locations:
                f.write(f"{location.name.lower().replace(' ', '_')} = {location.__class__.__name__}("
                        f'"{location.name}", "{location.description}")\n')
                if isinstance(location, Container):
                    for contained_location in location.locations:
                        f.write(f"{contained_location.name.lower().replace(' ', '_')} = "
                                f"{contained_location.__class__.__name__}("
                                f'"{contained_location.name}", "{contained_location.description}")\n')

def main():
    world = World()
    world.generate()
    world.save()
    generate_maps(world.name)

if __name__ == "__main__":
    main()
