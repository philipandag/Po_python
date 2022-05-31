import random
from Button import Button
import pygame


class Field(Button):

    hover_effect = (32, 32, 32)
    empty_color = (220, 220, 220)

    def __init__(self, size: (int, int), pos: (int, int), gridPos, world):
        super(Field, self).__init__(size, pos)
        self.color = (random.random() * 250, random.random() * 250, random.random() * 250)
        self.organism = None
        self.world = world
        self.gridPos = gridPos
        self.clicked = False

    def get_organism(self):
        return self.organism

    def set_organism(self, organism):
        self.organism = organism
        if organism is not None:
            organism.set_world(self.world)
            organism.set_field(self)

    def update(self):
        if self.organism is None:
            self.color = Field.empty_color
            self.text = ""
        else:
            self.color = self.organism.get_colour()
            self.text = self.organism.symbol

        if self.clicked:
            self.image.fill(self.color)
            self.clicked = False

        if self.hovered and not self.hover_effect_on:
            self.image.fill(Field.hover_effect, special_flags=pygame.BLEND_RGB_ADD)
            self.hover_effect_on = True
        elif not self.hovered:
            self.image.fill(self.color)
            if self.hover_effect_on:
                self.hover_effect_on = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def is_empty(self):
        return self.organism is None

    def onClick(self):
        if self.is_empty():
            organism = self.world.get_choosen_organism()
            self.world.set_organism(organism(), self.gridPos)
        else:
            self.world.set_organism(None, self.gridPos)
        self.clicked = True