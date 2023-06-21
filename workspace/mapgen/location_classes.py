from ..game import Location

class Container(Location):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.locations = []

    def add_location(self, location):
        if self.validate_containment(location):
            self.locations.append(location)
        else:
            print(f"Error: Cannot place {type(location).__name__} within {type(self).__name__}.")

    def get_location(self, name):
        for location in self.locations:
            if location.name == name:
                return location
        return None

    def validate_containment(self, location):
        if hasattr(self, 'valid_locations'):
            return isinstance(location, self.valid_locations)
        else:
            return False

class Forest(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Field(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Ruins(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class City(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Village(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Town(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Landmark(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Universe(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class Planet(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class Continent(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class Country(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class Region(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class State(Container):

    def __init__(self, name, description):
        super().__init__(name, description)

class Province(Container):

    def __init__(self, name, description):
        super().__init__(name, description)
        
class Island(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
        
class Ocean(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Mountain(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
        
class Desert(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Lake(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class River(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Building(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Castle(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Dungeon(Container):
    
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Room(Container):
    valid_locations = tuple() # To be filled after all location classes are defined
    # This is a special case, as it is the only location that cannot contain other locations        
    def __init__(self, name, description):
        super().__init__(name, description)

# Defining valid locations after all classes are defined
Universe.valid_locations = (Planet,)
Planet.valid_locations = (Continent, Ocean)
Ocean.valid_locations = (Continent, Island)
Continent.valid_locations = (Country, Region)
Island.valid_locations = (Country, Region, Forest, Desert, Field, Ruins, Mountain, Castle, Dungeon)
Country.valid_locations = (Region, State, Province, Desert, Mountain, Lake, River)
Region.valid_locations = (Country, State, Province, Desert, Mountain, Village, Landmark, Forest, Field, Ruins)
Mountain.valid_locations = (Village, Landmark, Forest, Ruins)
Lake.valid_locations = (Landmark, Ruins)
River.valid_locations = (Landmark, Ruins)
Desert.valid_locations = (Landmark, Ruins)
State.valid_locations = (City, Village, Town, Landmark, Forest, Field, Desert, Ruins)
Province.valid_locations = (City, Village, Town, Landmark, Forest, Field, Ruins)
City.valid_locations = (Landmark, Ruins, Building, Castle, Dungeon)
Castle.valid_locations = (Landmark, Ruins, Building, Dungeon, Room)
Village.valid_locations = (Landmark, Forest, Field, Ruins, Building)
Town.valid_locations = (Landmark, Forest, Field, Ruins, Building)
Forest.valid_locations = (Landmark, Ruins, River, Lake)
Field.valid_locations = (Landmark, Ruins, River, Lake)
Ruins.valid_locations = (Landmark, River, Lake, Dungeon)
Landmark.valid_locations = (Building, Dungeon)
Building.valid_locations = (Dungeon, Room)
Dungeon.valid_locations = (Room,)
Room.valid_locations = tuple()