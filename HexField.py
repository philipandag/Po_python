import math
import random
from Button import Button
import pygame
from HexButton import HexButton

class HexField(HexButton):

    def __init__(self, size: (int, int), pos: (int, int), gridPos, world):
        super(HexField, self).__init__(size, pos, "")
        self.empty_color = self.color
        self.organism = None
        self.world = world
        self.gridPos = gridPos
        self.clicked = False

    def get_organism(self):
        return self.organism

    def set_organism(self, organism):
        self.organism = organism
        if organism is not None:
            organism.set_field(self)
            self.text = organism.get_symbol()
            self.color = organism.get_colour()
        else:
            self.color = self.empty_color
            self.text = ""

        self.needs_redraw = True
        self.fontRender = self.renderText()
        self.image_normal, self.image_hover = self.create_images()


    def is_empty(self):
        return self.organism is None

    def onClick(self):
        if self.is_empty():
            organism = self.world.get_chosen_organism()()
            self.world.set_organism(organism, self.gridPos)
            organism.set_world(self.world)
        else:
            self.world.set_organism(None, self.gridPos)
        self.needs_redraw = True
        self.clicked = True

    def renderText(self):
        max_size = 20
        lower, upper = 0, int(self.size[1]*math.sqrt(3)/2)
        while True:
            font = pygame.font.SysFont(self.default_font, int(max_size))
            size = font.size(self.text)

            if upper - lower <= 1:
                return font.render(self.text, False, self.fontColor)
            if size[0] <= self.size[0] and size[1] <= self.size[1]:
                lower = max_size
                max_size = (lower + upper) // 2
            else:
                upper = max_size
                max_size = (lower + upper) // 2

