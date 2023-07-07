import pygame
import sys
import random
import noise
import numpy as np

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAP_HEIGHT = SCREEN_HEIGHT * 2 // 3
CONSOLE_HEIGHT = SCREEN_HEIGHT - MAP_HEIGHT
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CONTINENT_COLOR = (139, 69, 19)  # Brown color for continents
DESERT_COLOR = (255, 255, 0)  # Beige color for desert
FOREST_COLOR = (0, 100, 0)  # Dark green color for forest
MOUNTAIN_COLOR = (128, 128, 128)  # Gray color for mountains
SWAMP_COLOR = (0, 255,255)  # Grey Green color for swamp
PLAINS_COLOR = (255, 255, 255)  # Light Grey Green color for plains

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("World Builder")

# Clear the screen
screen.fill(BLUE)

def generate_waves_shape():
    shape = []
    num_points = random.randint(50, 130)  # Number of points for the vector line
    start_x = random.randint(0, SCREEN_WIDTH)
    start_y = random.randint(SCREEN_HEIGHT // 3, int(SCREEN_HEIGHT * 3 / 5))

    scale = 0.1  # The smaller the scale the smoother the noise
    octaves = 6  # Number of levels of detail
    persistence = 0.5  # Amplitude of each successive octave
    lacunarity = 2.0  # Frequency of each successive octave

    for i in range(num_points):
        x = start_x + i
        y = start_y + noise.pnoise2(x * scale, 
                                     start_y * scale, 
                                     octaves=octaves, 
                                     persistence=persistence, 
                                     lacunarity=lacunarity, 
                                     repeatx=SCREEN_WIDTH, 
                                     repeaty=SCREEN_HEIGHT, 
                                     base=0)
        shape.append((x, int(y)))

    return shape

def generate_continent_shape():
    shape = []
    num_points = random.randint(160000, 288000)  # Number of points for the vector line
    start_x = random.randint(0, SCREEN_WIDTH)
    start_y = random.randint(SCREEN_HEIGHT // 3, int(SCREEN_HEIGHT * 3 / 5))

    for _ in range(num_points):
        shape.append((start_x, start_y))
        direction = random.randint(0, 3)  # Random direction (0 = up, 1 = down, 2 = left, 3 = right)
        if direction == 0:
            start_y -= 1
        elif direction == 1:
            start_y += 1
        elif direction == 2:
            start_x -= 1
        else:
            start_x += 1

    return shape

# Draw the map area
map_area = pygame.Rect(0, 0, SCREEN_WIDTH, MAP_HEIGHT)
pygame.draw.rect(screen, BLUE, map_area)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Generate and draw the continent shape
    continent_shape = generate_continent_shape()
    pygame.draw.lines(screen, CONTINENT_COLOR, False, continent_shape, 2)

    # Display the continent shape on the map
    for i in range(len(continent_shape) - 1):
        pygame.draw.line(screen, CONTINENT_COLOR, continent_shape[i], continent_shape[i + 1], 1)

# Draw the console area
console_area = pygame.Rect(0, MAP_HEIGHT, SCREEN_WIDTH, CONSOLE_HEIGHT)
pygame.draw.rect(screen, WHITE, console_area)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate and draw the waves shape
    waves_shape = generate_waves_shape()
    pygame.draw.lines(screen, WHITE, False, waves_shape, 2)
    
    # Update the display
    pygame.display.flip()
    clock.tick(2)
    
# Quit the game
pygame.quit()
sys.exit()