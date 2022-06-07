import random
import enum

import pygame

from Direction import Direction


class DirectionHex(Direction):
    NE = 1
    E = 2
    SE = 3
    SW = 4
    W = 5
    NW = 6
    DIRECTIONS = 6
    directions_list = [NE, E, SE, SW, W, NW]

    def __init__(self):
        self.value = DirectionHex.NE

    def randomise(self):
        self.value = random.choice(self.directions_list)

    def next(self):
        if self.value == DirectionHex.NW:
            self.value = DirectionHex.NE
        else:
            self.value = self.value + 1

    def delta(self) -> (int, int):
        dx, dy = 0, 0
        if self.value in (DirectionHex.NE, DirectionHex.E):
            dx = 1
        elif self.value in (DirectionHex.W, DirectionHex.SW):
            dx = -1
        if self.value in (DirectionHex.SW, DirectionHex.SE):
            dy = 1
        elif self.value in (DirectionHex.NW, DirectionHex.NE):
            dy = -1
        return dx, dy

    def directions(self) -> int:
        return self.DIRECTIONS

    def key_to_dir(self, key):
        if key == pygame.K_DOWN:
            self.value = self.SE
        elif key == pygame.K_RIGHT:
            self.value = self.E
        elif key == pygame.K_UP:
            self.value = self.NW
        elif key == pygame.K_LEFT:
            self.value = self.W
