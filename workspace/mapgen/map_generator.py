class Map:
    def __init__(self, size=(100, 100)):
        self.size = size
        self.contents = []

    def generate(self):
        pass  # generate the contents here

class Location:
    def __init__(self, type):
        self.type = type
        self.contains = []

def generate_locations():
    return [Location('forest'), Location('desert')]  # as an example
