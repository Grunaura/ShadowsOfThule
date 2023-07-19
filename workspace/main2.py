#main2.py

import pygame, pygame_gui, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Shadow of Thulea")

GB = pygame.image.load("assets/images/background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/GuyfordBlackletter.ttf", size)

def play(): # Play Screen
    pygame.display.set_caption("Play")
    
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("black")
        PLAY_TEXT = get_font(45).render("This is the play screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        PLAY_BACK = Button(image=None, pos=(640, 460), text_input="Go Back", font=get_font(50), base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()
        
def options(): # Options Screen
    pygame.display.set_caption("Options")
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("This is the options screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu(): # Main Menu Screen
    pygame.display.set_caption("Menu")

    QUIT_BUTTON = Button(pos=(540, 550), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    PLAY_BUTTON = Button(pos=(540, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(pos=(540, 400), text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    
    while True:
        SCREEN.blit(GB, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
       
        #MENU_TEXT = get_font(100).render("The Shadow of Thulea", True, ("#9a574f"))
        # Render the shadow
        SHADOW_COLOR = (0, 0, 0)  # Shadow color set to black
        SHADOW_OFFSET = (5, 5)  # Shadow offset
        SHADOW_TEXT = get_font(100).render("The Shadow of Thulea", True, SHADOW_COLOR)
        SHADOW_RECT = SHADOW_TEXT.get_rect(center=(640 + SHADOW_OFFSET[0], 100 + SHADOW_OFFSET[1]))
        SCREEN.blit(SHADOW_TEXT, SHADOW_RECT)
         
        # Render the title
        TITLE_TEXT = get_font(100).render("The Shadow of Thulea", True, ("#9a574f"))
        MENU_RECT = TITLE_TEXT.get_rect(center=(640, 100))

        SCREEN.blit(TITLE_TEXT, MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

            padding_percent = 0.05  # 5% padding
            # Draw the invisible rectangles
            if button.checkForInput(MENU_MOUSE_POS):
                pygame.draw.rect(SCREEN, button.base_color, (button.rect[0] - button.rect[2]*padding_percent, button.rect[1], button.rect[2]*(1+2*padding_percent), button.rect[3]), 2)
            else:
                pygame.draw.rect(SCREEN, button.base_color, (button.rect[0] - button.rect[2]*padding_percent, button.rect[1], button.rect[2]*(1+2*padding_percent), button.rect[3]), 2)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()                                                                                                                                          

main_menu()
