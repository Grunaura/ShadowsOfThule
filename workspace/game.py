#game.py

from combat_controller import CombatController

class Player:
    def __init__(self, name, health, inventory):
        self._name = name
        self._health = health
        self._inventory = inventory
        self._current_location = None
        self._active_quests = []

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def inventory(self):
        return self._inventory

    @property
    def current_location(self):
        return self._current_location

    @current_location.setter
    def current_location(self, location):
        self._current_location = location

    @property
    def active_quests(self):
        return self._active_quests

    def get_item(self, name):
        """
        Get the item with the specified name from the player's inventory.
        Returns the item if found, None otherwise.
        """
        for item in self._inventory:
            if item.name.lower() == name.lower():
                return item
        return None

    def use_item(self, item):
        """
        Use the specified item.
        Returns True if the item was successfully used, False otherwise.
        """
        if item in self._inventory:
            self._inventory.remove(item)
            self._health += item.effect
            return True
        else:
            return False

    def get_quest(self, name):
        """
        Get the quest with the specified name from the player's active quests.
        Returns the quest if found, None otherwise.
        """
        for quest in self._active_quests:
            if quest.name.lower() == name.lower():
                return quest
        return None

    def start_quest(self, quest):
        """
        Start the specified quest.
        Returns True if the quest was successfully started, False otherwise.
        """
        if quest in self._active_quests:
            return False
        else:
            self._active_quests.append(quest)
            return True

    def complete_quest(self, quest):
        """
        Complete the specified quest.
        Returns True if the quest was successfully completed, False otherwise.
        """
        if quest in self._active_quests:
            self._active_quests.remove(quest)
            return True
        else:
            return False

    def add_item(self, item):
        """
        Add the specified item to the player's inventory.
        """
        self._inventory.append(item)

    def move(self, direction):
        """
        Move the player in the specified direction if possible.
        Returns True if the move was successful, False otherwise.
        """
        next_location = self.current_location.get_adjacent_Location(direction)
        if next_location is not None:
            self.current_location = next_location
            return True
        else:
            return False
        
class Location:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._adjacent_locations = {}

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def adjacent_locations(self):
        return self._adjacent_locations

    def connect_location(self, location, direction):
        """
        Connect this location to the specified location in the specified direction.
        """
        self._adjacent_locations[direction] = location
        location._adjacent_locations[self.get_opposite_direction(direction)] = self

    def get_adjacent_location(self, direction):
        """
        Get the adjacent location in the specified direction.
        Returns the location if found, None otherwise.
        """
        return self._adjacent_locations.get(direction)

    def get_opposite_direction(self, direction):
        """
        Get the opposite direction of the specified direction.
        """
        opposite_directions = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east"
        }
        return opposite_directions.get(direction)

    def move(self, direction):
        """
        Move the player in the specified direction if possible.
        Returns True if the move was successful, False otherwise.
        """
        next_location = self.current_location.get_adjacent_location(direction)
        if next_location is not None:
            self.current_location = next_location
            return True
        else:
            return False

    def get_item(self, name):
        """
        Get the item with the specified name from the player's inventory.
        Returns the item if found, None otherwise.
        """
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None

    def use_item(self, item):
        """
        Use the specified item.
        Returns True if the item was successfully used, False otherwise.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            self.health += item.effect
            return True
        else:
            return False

    def get_quest(self, name):
        """
        Get the quest with the specified name from the player's active quests.
        Returns the quest if found, None otherwise.
        """
        for quest in self.active_quests:
            if quest.name.lower() == name.lower():
                return quest
        return None

    def start_quest(self, quest):
        """
        Start the specified quest.
        Returns True if the quest was successfully started, False otherwise.
        """
        if quest in self.active_quests:
            return False
        else:
            self.active_quests.append(quest)
            return True

    def complete_quest(self, quest):
        """
        Complete the specified quest.
        Returns True if the quest was successfully completed, False otherwise.
        """
        if quest in self.active_quests:
            self.active_quests.remove(quest)
            return True
        else:
            return False

    def add_item(self, item):
        """
        Add the specified item to the player's inventory.
        """
        self.inventory.append(item)


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.adjacent_Locations = {}

    def connect(self, Location, direction):
        """
        Connect this Location to the specified Location in the specified direction.
        """
        self.adjacent_Locations[direction] = Location
        Location.adjacent_Locations[self.get_opposite_direction(direction)] = self

    def get_adjacent_Location(self, direction):
        """
        Get the adjacent Location in the specified direction.
        Returns the Location if found, None otherwise.
        """
        return self.adjacent_Locations.get(direction)

    def get_description(self):
        """
        Get the description of this Location.
        """
        return self.description

    def get_opposite_direction(self, direction):
        """
        Get the opposite direction of the specified direction.
        """
        if direction == "north":
            return "south"
        elif direction == "south":
            return "north"
        elif direction == "east":
            return "west"
        elif direction == "west":
            return "east"
        else:
            return None


class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def get_description(self):
        """
        Get the description of this item.
        """
        return self.description

class Quest:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives

    def get_description(self):
        """
        Get the description of this quest.
        """

        return self.description
    
class SideQuest(Quest):
    def __init__(self, name, description, objectives):
        super().__init__(name, description, objectives)
        self.side_quest_property = None  # Add additional properties specific to side quests

