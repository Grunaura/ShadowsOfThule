# menu_controller.py

import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN

class Button:
    def __init__(self, text, x, y, width, height, color, highlight_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.highlight_color = highlight_color

    def draw(self, screen, mouse_pos):
        if self.is_over(mouse_pos):
            pygame.draw.rect(screen, self.highlight_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        font = pygame.font.SysFont(None, 50)
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


class MenuController:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.start_button = Button('Start Game', 300, 200, 200, 50, (0, 200, 0), (0, 255, 0))
        self.load_button = Button('Load Game', 300, 300, 200, 50, (0, 200, 0), (0, 255, 0))
        self.settings_button = Button('Settings', 300, 400, 200, 50, (0, 200, 0), (0, 255, 0))

    def show_menu(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.start_button.is_over(mouse_pos):
                        return 'PLAY'
                    elif self.load_button.is_over(mouse_pos):
                        return 'LOAD'
                    elif self.settings_button.is_over(mouse_pos):
                        print("Settings clicked")
                        # Implement your open settings functionality here

            self.screen.fill((0, 0, 0))
            self.start_button.draw(self.screen, mouse_pos)
            self.load_button.draw(self.screen, mouse_pos)
            self.settings_button.draw(self.screen, mouse_pos)

            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu_controller = MenuController(screen)
    menu_controller.show_menu()
