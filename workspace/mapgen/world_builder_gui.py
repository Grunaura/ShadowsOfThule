import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("World Builder GUI")

# Set up colors
background_color = (255, 255, 255)
text_color = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(background_color)

    # Draw GUI elements
    text_surface = font.render("World Builder", True, text_color)
    text_surface = font.render("Let there be light.", True, text_color)
    text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(text_surface, text_rect)

    generate_button = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(window, (100, 100, 100), generate_button)
    generate_text = font.render("Generate World", True, (255, 255, 255))
    generate_text_rect = generate_text.get_rect(center=generate_button.center)
    window.blit(generate_text, generate_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
