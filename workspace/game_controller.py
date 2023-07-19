#game_controller.py

import json
import pygame
from combat_controller import CombatController
from game import Player, Location, Item, Quest
from pygame.locals import *

class GameController:
    def __init__(self):
        # Initialize game objects
        self.player = Player("Player", 100, [])
        self.show_actions = True  # Variable to track if actions should be displayed
        self.combat_controller = CombatController()

        # Load locations from JSON
        self.locations = {}  # Store locations in a dictionary for easy access
        location_files = ["map_data.json"]
        for location_file in location_files:
            with open(location_file, 'r') as file:
                data = json.load(file)
                location = Location(data["name"], data["description"])
                self.locations[data["name"]] = location

        # Connect locations
        for location_file in location_files:
            with open(location_file, 'r') as file:
                data = json.load(file)
                for direction, location_name in data["connections"].items():
                    self.locations[data["name"]].connect(self.locations[location_name], direction)

        self.player.current_location = self.locations["Start Village"]
        self.running = True
        
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
        pygame.init()
        screen = pygame.display.set_mode((640, 480))

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                elif event.type == KEYDOWN:
                    if event.key == K_q:
                        self.running = False

                    elif event.key == K_a:
                        self.show_actions = not self.show_actions

            # Update game state here

            # Draw to the screen
            screen.fill((0, 0, 0))

            # More drawing code can go here...
            if self.show_text:
                text = self.font.render("Hello, World!", True, (255, 255, 255))
                screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))


            pygame.display.flip()

        pygame.quit()

    # Remaining methods ...

if __name__ == "__main__":
    controller = GameController()
    controller.run_game_loop()