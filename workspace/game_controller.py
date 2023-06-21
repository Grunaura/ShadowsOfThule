#game_controller.py

from combat_controller import CombatController
from game import Player, Location, Item, Quest

class GameController:
    def __init__(self):
        # Initialize game objects
        self.player = Player("Player", 100, [])
        self.location1 = Location("Start Village", "You are in a peaceful village.")
        self.location2 = Location("Dark Forest", "You have entered a gloomy forest.")
        self.location3 = Location("Mysterious Castle", "You are at the entrance of a grand castle.")
        # Connect locations
        self.location1.connect(self.location2, "north")
        self.location1.connect(self.location3, "east")
        self.location2.connect(self.location1, "south")
        self.location3.connect(self.location1, "west")
        self.player.current_location = self.location1
        self.show_actions = True  # Variable to track if actions should be displayed
        self.combat_controller = CombatController()

    def process_command(self, command):
        # Parse user input
        parts = command.split()
        action = parts[0]
        
        if action == "toggle actions":
            self.show_actions = not self.show_actions
        elif action == "move":            
            direction = parts[1]
            if self.player.move(direction):
                print("Moved to", self.player.current_location.name)
            else:
                print("Cannot move in that direction.")
        elif action == "use":
            item_name = " ".join(parts[1:])
            item = self.player.get_item(item_name)
            if item is not None:
                if self.player.use_item(item):
                    print("Used", item.name)
                else:
                    print("Cannot use that item.")
            else:
                print("Item not found.")
        elif action == "travel":
            destination = parts[1]
            method = " ".join(parts[2:])  # Assuming method can be more than one word
            self.player.travel(destination, method)
        elif action == "start":
            quest_name = " ".join(parts[1:])
            quest = self.player.get_quest(quest_name)
            if quest is not None:
                if self.player.start_quest(quest):
                    print("Started quest:", quest.name)
                else:
                    print("Cannot start that quest.")
            else:
                print("Quest not found.")
        elif action == "complete":
            quest_name = " ".join(parts[1:])
            quest = self.player.get_quest(quest_name)
            if quest is not None:
                if self.player.complete_quest(quest):
                    print("Completed quest:", quest.name)
                else:
                    print("Cannot complete that quest.")
            else:
                print("Quest not found.")
        elif action == "combat":
            enemy_name = " ".join(parts[1:])
            result = self.engage_combat(enemy_name)
            print(result)
        else:
            print("Invalid command.")

    def engage_combat(self, enemy_name):
        enemy = self.player.current_location.get_creature(enemy_name)
        if enemy:
            self.combat_controller.initiate_combat(self.player, enemy)
            return "You engage in combat!"
        else:
            return "There is no such creature here."

    def run_game_loop(self):
        # Start game loop
        while True:
            # Print current location description
            print(self.player.current_location.get_description())
            # Print available actions
            if self.show_actions:
                print("Available actions:")
                print("move <direction>")
                print("use <item>")
                print("start <quest>")
                print("complete <quest>")
                print("travel <destination> <method>")
                print("toggle actions")
                print("combat <enemy>")
            
            # Get user input
            command = input("Enter command: ")
            
            self.process_command(command)
