import pygame
from InterfaceElement import InterfaceElement

class Console(InterfaceElement):

    def __init__(self, pos, size):
        self.pos = pos
        self.background_colour = (0, 0, 0)
        self.text_background_colour = (20, 20, 20)
        self.text_foreground_colour = (255, 255, 255)
        self.size = size
        self.font = pygame.font.SysFont('consolas', 16)

        self.text = ""

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.background_colour, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        text = self.font.render(self.text, self.text_background_colour, self.text_foreground_colour)
        text_rect = text.get_rect()
        text_rect.center = (self.pos[0] / 2 + self.size[0]/2, self.pos[1]/2 + self.size[1]/2)
        surface.blit(text, text_rect)

    def handle_event(self, event: pygame.event.Event):
        pass

    def update(self):
        pass

    def write(self, text: str):
        self.text += text