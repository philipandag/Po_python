import math

from Button import Button
import pygame

class HexButton(Button):
    SIDES = 6
    def __init__(self, size: (int, int), pos: (int, int), text: str = ""):
        self.needs_redraw = True
        self.size: (int, int) = size
        self.pos: (int, int) = pos
        self.color = (240, 240, 240, 255)
        self.side_length = self.size[0]//math.sqrt(3)
        self.shape = self.create_shape()
        self.fontColor = (0, 0, 0)
        self.hover_effect = (32, 32, 32, 0)
        self.text = text
        self.fontSize = 30
        self.font = pygame.font.SysFont(self.default_font, self.fontSize)
        if text != "":
            self.fontRender = self.renderText()
        else:
            self.fontRender = pygame.Surface((0, 0))
        self.image_normal, self.image_hover = self.create_images()
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=pos)
        self.hovered = False
        self.hover_effect_on = False
        self.onClickFunction = None

    def create_shape(self):
        from math import sin, cos, pi
        n, r = self.SIDES, self.side_length
        x, y = self.size[0] // 2, self.size[1] // 2
        return [
            (x + r * sin(2 * pi * i / n), y + r * cos(2 * pi * i / n))
            for i in range(n)]

    def create_images(self):

        image_normal = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        image_normal.convert_alpha()
        pygame.draw.polygon(image_normal, self.color, self.shape)
        pygame.draw.polygon(image_normal, (0, 0, 0), self.shape, 1)

        image_hover = image_normal.copy()
        image_hover.fill(self.hover_effect, special_flags=pygame.BLEND_RGBA_ADD)
        return image_normal, image_hover

    def draw(self, surface):
        if self.needs_redraw:
            surface.blit(self.image, (self.pos[0] + 1, self.pos[1] + 1, self.image.get_width() - 1, self.image.get_height() - 1))
            surface.blit(self.fontRender, (self.pos[0] + (self.size[0] - self.fontRender.get_size()[0]) // 2,
                                           self.pos[1]*1.01 + (self.size[1] - self.fontRender.get_size()[1]) // 2))
            self.needs_redraw = False

    def collides(self, pos):
        from math import pow
        return pow(self.pos[0] + self.size[0]//2 - pos[0], 2) + pow(self.pos[1] + self.size[1]//2 - pos[1], 2) <= pow(self.side_length*math.sqrt(3)/2, 2)