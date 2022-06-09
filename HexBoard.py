import math

import pygame

from DirectionHex import DirectionHex
from DirectionSquare import DirectionSquare
from HexField import HexField
from GridContainer import GridContainer

from SquareBoard import SquareBoard


class HexBoard(SquareBoard):
    def __init__(self, pos: (int, int), size: (int, int), world):
        self.pos = pos
        self.fieldSize = size[0] // (world.dimensions[0] + world.dimensions[1] // 2)
        self.fieldSize = (self.fieldSize, self.fieldSize * 2/math.sqrt(3))
        self.dimensions = world.dimensions
        self.size = size
        self.grid = [[None for i in range(self.dimensions[1])] for j in range(self.dimensions[0])]
        self.world = world
        self.createGrid()
        self.direction_class = DirectionHex
        self.mouse_down_pos = None
        self.size = self.size[0], self.size[1] * (self.size[0] // (self.size[0] + (self.dimensions[1]//2)))

    def createGrid(self):
        for row in range(self.dimensions[1]):
            for column in range(self.dimensions[0]):
                field_pos = (self.pos[0] + self.fieldSize[0] * (column + row/2),
                             self.pos[1] + self.fieldSize[1]*3/4 * row)

                self.grid[column][row] = HexField(self.fieldSize, field_pos, (column, row), self.world)

    def handle_event(self, event):
        if event.type not in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            return
        f2 = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            for y in range(self.dimensions[1]):
                for x in range(self.dimensions[0]):
                    if self.at((x, y)).collides(event.pos):
                        self.mouse_down_pos = [x, y]

        elif event.type == pygame.MOUSEMOTION:

            if self.mouse_down_pos is not None:
                f1 = self.mouse_down_pos.copy()
                for y in range(self.dimensions[1]):
                    for x in range(self.dimensions[0]):
                        if self.at((x, y)).collides(event.pos):
                            f2 = [x, y]
                if f2 is None:
                    return

                self.drag_positions_fix(f1, f2)
                for y in range(self.dimensions[1]):
                    for x in range(self.dimensions[0]):
                        if y in range(f1[1], f2[1]+1) and x in range(f1[0], f2[0]+1):
                            self.at((x, y)).setHoverEffect(True)
                        else:
                            self.at((x, y)).setHoverEffect(False)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                for y in range(self.dimensions[1]):
                    for x in range(self.dimensions[0]):
                        if self.at((x, y)).collides(event.pos):
                            f2 = [x, y]
                if f2 is None:
                    return
                for y in range(self.dimensions[1]):
                    for x in range(self.dimensions[0]):
                        self.at((x, y)).setHoverEffect(False)
                if self.onBoard(f2):
                    self.at(f2).setHoverEffect(True)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_down_pos is not None:
                f1 = self.mouse_down_pos.copy()
                for y in range(self.dimensions[1]):
                    for x in range(self.dimensions[0]):
                        if self.at((x, y)).collides(event.pos):
                            f2 = [x, y]

                if f2 is None:
                    return
                self.drag_positions_fix(f1, f2)
                for y in range(f1[1], f2[1]+1):
                    for x in range(f1[0], f2[0]+1):
                        self.at((x, y)).onClick()
                self.mouse_down_pos = None

    # def handle_event(self, event):
    #     for row in self.grid:
    #         for field in row:
    #             field.handle_event(event)

    def drag_positions_fix(self, f1, f2):
        if f2[0] >= self.dimensions[0]:
            f2[0] = self.dimensions[0] - 1
        elif f2[0] < 0:
            f2[0] = 0
        if f2[1] >= self.dimensions[1]:
            f2[1] = self.dimensions[1] - 1
        elif f2[1] < 0:
            f2[1] = 0
        if f2[0] < f1[0]:
            f2[0], f1[0] = f1[0], f2[0]
        if f2[1] < f1[1]:
            f2[1], f1[1] = f1[1], f2[1]

    def grid_to_pos_px(self, grid_pos):
        pos_y = grid_pos[1] * self.fieldSize[1]
        pos_x = (grid_pos[0] + grid_pos[1] // 2) * self.fieldSize[0]

    def pos_to_grid_pos(self, pos):
        y = pos[1] // self.fieldSize[1]



