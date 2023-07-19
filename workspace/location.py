# location.py

class Location:
    def __init__(self, name, description, items=None, characters=None):
        self.name = name
        self.description = description
        self.exits = {}  # keys are directions, values are Locations
        self.items = items if items else []  # list of items present at the location
        self.characters = characters if characters else []  # list of characters present at the location

    def add_exit(self, direction, location):
        self.exits[direction] = location

    def get_exit(self, direction):
        return self.exits.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_description(self):
        description = self.description

        if self.items:
            description += "\nYou see here:"
            for item in self.items:
                description += f"\n- {item.name}"

        if self.characters:
            description += "\nYou see here:"
            for character in self.characters:
                description += f"\n- {character.name}"

        if self.exits:
            description += "\nExits are:"
            for direction in self.exits.keys():
                description += f"\n- {direction}"

        return description
