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
        return isinstance(location, (Region, State, Province, City, Village, Town, Landmark))

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
        
class Forrest(Location):
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
