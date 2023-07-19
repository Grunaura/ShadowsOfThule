import sys
import pygame
from game_controller import GameController
from menu_controller import MenuController
from save_load import SaveLoad

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) # Set the width and height
        pygame.display.set_caption("Menu") # Set the window title
        self.BG = pygame.image.load("assets/images/background.jpg")
        self.game_controller = GameController(self.screen)
        self.menu_controller = MenuController(self.screen)
        self.save_load = SaveLoad()
        self.state = "MENU"
        
    def run_game_loop(self):
        while True:
            if self.state == "MENU":
                self.menu()
            elif self.state == "PLAY":
                self.play()
            elif self.state == "PAUSE":
                self.pause()
            elif self.state == "LOAD":
                self.load()
            elif self.state == "EXIT":
                self.exit()
            pygame.display.flip()

    def menu(self):
        self.state = self.menu_controller.show_menu()
    
    def play(self):
        try:
            self.state = self.game_controller.run_game_loop()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.state = "MENU"
    
    def pause(self):
        self.save_load.save_game(self.game_controller.player)
        self.state = "MENU"
    
    def load(self):
        loaded_player = self.save_load.load_game()
        if loaded_player:
            self.game_controller.player = loaded_player
            self.state = "PLAY"
        else:
            self.state = "MENU"
    
    def exit(self):
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run_game_loop()

if __name__ == "__main__":
    main()
