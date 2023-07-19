#player.py
# player.py
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def look(self):
        print(f"You are at {self.location.name}. You see {self.location.description}.")

    def use_item(self):
        item = input("Which item do you want to use? ")
        # Assuming the player has a dictionary of items
        if item in self.items:
            self.items[item].use()

    def move_north(self):
        if "north" in self.location.exits:
            self.location = self.location.exits["north"]
        else:
            print("You can't go north.")

    def move_south(self):
        if "south" in self.location.exits:
            self.location = self.location.exits["south"]
        else:
            print("You can't go south.")

    def move_east(self):
        if "east" in self.location.exits:
            self.location = self.location.exits["east"]
        else:
            print("You can't go east.")

    def move_west(self):
        if "west" in self.location.exits:
            self.location = self.location.exits["west"]
        else:
            print("You can't go west.")
