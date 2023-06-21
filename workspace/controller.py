# controller.py

import curses

class Controller:
    def __init__(self, game):
        self.game = game
        self.actionable_commands = ["look", "use item", "move"]
        self.last_command = None

    def parse_input(self, c):
        # Map the key to an action
        if c == curses.KEY_UP:
            direction = "north"
            command = "move north"
        elif c == curses.KEY_DOWN:
            direction = "south"
            command = "move south"
        elif c == curses.KEY_LEFT:
            direction = "west"
            command = "move west"
        elif c == curses.KEY_RIGHT:
            direction = "east"
            command = "move east"
        elif c == ord('q'):
            command = "quit"
        else:
            return None  # Unhandled key press, return None

        # Save the last command
        self.last_command = command
        return command

    def run_command(self, command):
        if command == "quit":
            return False
        elif command in self.actionable_commands:
            # Call the corresponding function for this command
            getattr(self.game.player, command.replace(" ", "_"))()
        return True
