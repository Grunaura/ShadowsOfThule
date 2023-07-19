import pygame
import random
import pygame.freetype

# Set constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up fonts
font = pygame.freetype.SysFont(None, 24)

# Function to draw a star
def draw_star(surface, x, y):
    pygame.draw.circle(surface, (255, 255, 255), (x, y), 2)

# Function to create the scene
def create_scene(surface, input_box):
    surface.fill((0, 0, 0))  # Fill the screen with black to represent space
    # Add 100 stars at random positions
    for _ in range(100):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        draw_star(surface, x, y)
    # Draw the input box
    pygame.draw.rect(surface, (255, 255, 255), input_box, 2)
    # Render the current text inside the input_box
    font.render_to(surface, (input_box.x+5, input_box.y+5), current_text, (255, 255, 255))

# Text input box
input_box = pygame.Rect(20, SCREEN_HEIGHT - 40, 140, 32)
current_text = ''

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(current_text)
                current_text = ''
            elif event.key == pygame.K_BACKSPACE:
                current_text = current_text[:-1]
            else:
                current_text += event.unicode
    # Draw the scene
    create_scene(screen, input_box)
    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
