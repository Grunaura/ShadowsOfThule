#button.py

class Button():
    def __init__(self, image=None, rect=None, pos=None, text_input=None, font=None, base_color=None, hovering_color=None):
        self.x_pos = pos[0] if pos else None
        self.y_pos = pos[1] if pos else None
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input  
        
        if self.text_input is not None and self.font is not None:
            self.text_surf = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text_surf.get_rect(center=pos)  

        self.image = image
        if self.image is not None:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif rect is not None:
            self.rect = rect
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        else:
            self.rect = self.text_rect

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        if self.text_input is not None and self.font is not None:
            screen.blit(self.text_surf, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text_surf = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text_surf = self.font.render(self.text_input, True, self.base_color)
