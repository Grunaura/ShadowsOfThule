import pygame, sys
from pygame.locals import *

pygame.init()

# Create the screen
SCREEN = pygame.display.set_mode((1270, 960))
pygame.display.set_caption("The Shadow of Thulea")

# Additional function to draw a black box (for covering previous box positions)
def draw_black_rect(surface, rect, corner_radius):
    pygame.draw.rect(surface, (0, 0, 0), rect)

def draw_rounded_rect(surface, rect, color, corner_radius):
    #Draw a rectangle with rounded corners on the specified surface
    if corner_radius < 0:
        raise ValueError(f"Corner radius {corner_radius} must be >= 0")
    elif corner_radius > min(rect.width, rect.height) / 2:
        raise ValueError(f"Corner radius {corner_radius} is too large for the rect")

    # Render the rectangle corners
    pygame.draw.circle(surface, color, (rect.topleft[0] + corner_radius, rect.topleft[1] + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.topright[0] - corner_radius, rect.topright[1] + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.bottomleft[0] + corner_radius, rect.bottomleft[1] - corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.bottomright[0] - corner_radius, rect.bottomright[1] - corner_radius), corner_radius)

    # Render the rectangle sides
    pygame.draw.rect(surface, color, rect.inflate(-2*corner_radius, 0))
    pygame.draw.rect(surface, color, rect.inflate(0, -2*corner_radius))

# Function to display the sprite animation
def sprite_animation():
    # Load the sprite sequence image
    sprite_sequence_image = pygame.image.load('assets\images\splash.png')

    # Define the number of slices and the duration of each slice
    num_slices = 40
    slice_duration = 0.1  # in seconds

    # Calculate the width of each slice
    slice_width = sprite_sequence_image.get_width() // num_slices

    # Create a black surface to hide the original image
    black_surface = pygame.Surface((slice_width, sprite_sequence_image.get_height()))
    black_surface.fill((0, 0, 0))

    # Function to display slices in a certain order
    def display_slices(slice_order):
        for slice_num in slice_order:
            # Display the original image
            SCREEN.blit(sprite_sequence_image, (0, 0))

            # Hide all slices after the current one
            for i in slice_order[slice_order.index(slice_num)+1:]:
                SCREEN.blit(black_surface, (i * slice_width, 0))

            pygame.display.update()

            # Wait for the duration of the slice
            pygame.time.wait(int(slice_duration * 1000))

    # Loop through each slice in the sequence from both ends towards the center
    left_to_right = list(range(num_slices // 2))
    right_to_left = list(range(num_slices - 1, num_slices // 2 - 1, -1))
    slice_order = [val for pair in zip(left_to_right, right_to_left) for val in pair]
    display_slices(slice_order)

class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        self.pos = pos
        self.text = font.render(text_input, True, pygame.Color(base_color))
        self.text_hovering = font.render(text_input, True, pygame.Color(hovering_color))
        self.width = self.text.get_width() + 20
        self.height = self.text.get_height() + 20
        self.rect = pygame.Rect(pos, (self.width, self.height))
        self.hovering = False
        self.base_color = base_color
        self.hovering_color = hovering_color

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovering = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovering:
                print(f"The '{self.text}' button has been pressed!")

    def draw(self, screen):
        if self.hovering:
            pygame.draw.rect(screen, pygame.Color(self.hovering_color), self.rect)
            screen.blit(self.text_hovering, (self.pos[0] + 10, self.pos[1] + 10))
        else:
            pygame.draw.rect(screen, pygame.Color(self.base_color), self.rect)
            screen.blit(self.text, (self.pos[0] + 10, self.pos[1] + 10))

# Main function
def main():
    global SCREEN  # Use the global SCREEN variable
    # Display the sprite animation
    sprite_animation()

    # Create a solid green box
    box_color = pygame.Color("#2b494c")  # RGB for green
    box_rect = pygame.Rect(100, 100, 500, 300)

    # Render the text "What be thy pleasure?" and blit it on the screen
    font_size = 36  # initial font size
    font = pygame.font.Font(None, font_size)
    text = font.render("What be thy pleasure?", True, (255, 255, 255))  # RGB for white
    text_rect = text.get_rect(center=box_rect.center)
    prev_box_rect = None  # Create a copy of the box rect to check for changes

    # Create buttons
    button1 = Button(pos=(box_rect.x + 50, box_rect.y + 50), text_input="Start", font=font, base_color="White", hovering_color="#2b494c")
    button2 = Button(pos=(box_rect.x + 50, box_rect.y + 100), text_input="Restore", font=font, base_color="White", hovering_color="#2b494c")
    button3 = Button(pos=(box_rect.x + 50, box_rect.y + 150), text_input="Introduction", font=font, base_color="White", hovering_color="#2b494c")
    button4 = Button(pos=(box_rect.x + 250, box_rect.y + 50), text_input="Options", font=font, base_color="White", hovering_color="#2b494c")
    button5 = Button(pos=(box_rect.x + 250, box_rect.y + 100), text_input="Make World", font=font, base_color="White", hovering_color="#2b494c")
    button6 = Button(pos=(box_rect.x + 250, box_rect.y + 150), text_input="Quit", font=font, base_color="White", hovering_color="#2b494c")

    drag = False
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if box_rect.collidepoint(event.pos):
                    drag = True
                    mouse_x, mouse_y = event.pos
                    offset_x = box_rect.x - mouse_x
                    offset_y = box_rect.y - mouse_y
                # Button event handling
                button1.handle_event(event)
                button2.handle_event(event)
                button3.handle_event(event)
                button4.handle_event(event)
                button5.handle_event(event)
                button6.handle_event(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    mouse_x, mouse_y = event.pos
                    box_rect.x = mouse_x + offset_x
                    box_rect.y = mouse_y + offset_y
                    text_rect.center = box_rect.center  # Update text position
                    # Update button positions
                    button1.pos = (box_rect.x + 50, box_rect.y + 50)
                    button2.pos = (box_rect.x + 50, box_rect.y + 100)
                    button3.pos = (box_rect.x + 50, box_rect.y + 150)
                    button4.pos = (box_rect.x + 250, box_rect.y + 50)
                    button5.pos = (box_rect.x + 250, box_rect.y + 100)
                    button6.pos = (box_rect.x + 250, box_rect.y + 150)
                    # Update button rects
                    button1.rect = pygame.Rect(button1.pos, (button1.width, button1.height))
                    button2.rect = pygame.Rect(button2.pos, (button2.width, button2.height))
                    button3.rect = pygame.Rect(button3.pos, (button3.width, button3.height))
                    button4.rect = pygame.Rect(button4.pos, (button4.width, button4.height))
                    button5.rect = pygame.Rect(button5.pos, (button5.width, button5.height))
                    button6.rect = pygame.Rect(button6.pos, (button6.width, button6.height))
            elif event.type == pygame.VIDEORESIZE:
                # Resize the window
                SCREEN = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
                pygame.display.flip()

        # Clear the screen
        # SCREEN.fill((0, 0, 0))

        # Draw the box
        draw_rounded_rect(SCREEN, box_rect, box_color, 10)

        # Draw the text
        SCREEN.blit(text, text_rect)

        # Draw the buttons
        button1.draw(SCREEN)
        button2.draw(SCREEN)
        button3.draw(SCREEN)
        button4.draw(SCREEN)
        button5.draw(SCREEN)
        button6.draw(SCREEN)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()