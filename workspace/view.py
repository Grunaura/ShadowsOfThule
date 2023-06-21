# view.py
import curses 

class GameView:
    def __init__(self, game, controller):
        self.game = game
        self.controller = controller

        # Initialize curses
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

    def cleanup(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def run(self):
        running = True
        while running:
            # Get the key pressed
            c = self.stdscr.getch()

            # Parse the key to a command
            command = self.controller.parse_input(c)
            if command is not None:
                self.stdscr.addstr(f"{command}\n")  # Display the command on the screen
                self.stdscr.refresh()

                # Run the command
                running = self.controller.run_command(command)

        self.cleanup()
