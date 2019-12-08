import pygame
from settings import *
class Button:
    def __init__(self, text, position, type, size=NORMAL, color=BUTTON_TEXT_COLOR, background=BUTTON_BACKGROUND):
        self.text = text
        f1 = pygame.font.Font(None, size)
        self.text1 = f1.render(text, 1, color)
        coor = self.text1.get_size()
        self.size = size - 10
        self.position = (position[0], position[1], position[0]+coor[0]+self.size, position[1] + coor[1]+self.size)
        self.type = type
        self.background = background 
        self.active = False
    
    def on_focus(self, point):
        return self.active and (self.position[0] <= point[0] <= self.position[2] + self.size and self.position[1] <= point[1] <= self.position[3]+self.size)  
    
    def draw_rect(self, window, color=BUTTON_BACKGROUND):
        pygame.draw.line(window, color, [self.position[0], self.position[1]], [self.position[2] + self.size, self.position[1]], 3)
        pygame.draw.line(window, color, [self.position[0], self.position[1]], [self.position[0], self.position[3] + self.size], 3)
        pygame.draw.line(window, color, [self.position[2] + self.size, self.position[3] + self.size], [self.position[2] + self.size, self.position[1]], 3)
        pygame.draw.line(window, color, [self.position[2] + self.size, self.position[3] + self.size], [self.position[0], self.position[3] + self.size], 3)
        surf1 = pygame.Surface((self.position[2] - self.position[0] + self.size, self.position[3] - self.position[1] + self.size))
        surf1.fill(self.background)
        window.blit(surf1, (self.position[0], self.position[1]))

    def selected(self, window, color=BUTTON_OUTLINE):
        if self.active == True:
            pygame.draw.line(window, color, [self.position[0]-5, self.position[1]-5], [self.position[2] + self.size+5, self.position[1]-5], 3)
            pygame.draw.line(window, color, [self.position[0]-5, self.position[1]-5], [self.position[0]-5, self.position[3] + self.size+5], 3)
            pygame.draw.line(window, color, [self.position[2] + self.size+5, self.position[3] + self.size+5], [self.position[2] + self.size+5, self.position[1]-5], 3)
            pygame.draw.line(window, color, [self.position[2] + self.size+5, self.position[3] + self.size+5], [self.position[0]-5, self.position[3] + self.size+5], 3)
        
    def block(self, window, color=TEXT_COLOR):
        if self.active:
            self.draw_rect(window)
            window.blit(self.text1, (self.position[0] + self.size, self.position[1] + self.size))
            