import pygame

from Button import Button
from DirectionSquare import DirectionSquare
from Field import Field
from GridContainer import GridContainer
from InterfaceElement import InterfaceElement
from Button import Button

class SquareBoard(GridContainer):

    def __init__(self, pos: (int, int), size: (int, int), world):
        m = min(size[0]//world.dimensions[0], size[1]//world.dimensions[1])
        size = (m*world.dimensions[0], m*world.dimensions[1])
        super(SquareBoard, self).__init__(pos, size, world.dimensions)
        self.world = world
        self.dimensions = world.dimensions
        self.createGrid()
        self.mouse_down_pos = None
        self.direction_class = DirectionSquare

    def createGrid(self):
        for row in range(self.dimensions[1]):
            for column in range(self.dimensions[0]):
                field_pos = (self.pos[0] + self.fieldSize[0] * column,
                             self.pos[1] + self.fieldSize[1] * row)

                self.grid[column][row] = Field(self.fieldSize, field_pos, (column, row), self.world)

    def setDimensions(self, dimensions):
        self.dimensions = dimensions

    def setGrid(self, grid):
        self.grid = grid

    def getGrid(self):
        return self.grid

    def onBoard(self, pos: (int, int)):
        return 0 <= pos[0] < self.dimensions[0] and 0 <= pos[1] < self.dimensions[1]

    def at(self, pos: (int, int)) -> 'Field':
        return self.grid[pos[0]][pos[1]]

    def handle_event(self, event):
        if event.type not in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            return
        event.pos = (event.pos[0] - self.pos[0], event.pos[1] - self.pos[1])
        field_pos = [event.pos[0] // self.fieldSize[0], event.pos[1] // self.fieldSize[1]]


        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.onBoard(field_pos):
                self.mouse_down_pos = field_pos

        elif event.type == pygame.MOUSEMOTION:
            if self.mouse_down_pos is not None:
                f1 = self.mouse_down_pos.copy()
                f2 = field_pos
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
                        self.at((x, y)).setHoverEffect(False)
                if self.onBoard(field_pos):
                    self.at(field_pos).setHoverEffect(True)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_down_pos is not None:
                f1 = self.mouse_down_pos.copy()
                f2 = field_pos
                self.drag_positions_fix(f1, f2)
                for y in range(f1[1], f2[1]+1):
                    for x in range(f1[0], f2[0]+1):
                        self.at((x, y)).onClick()
                self.mouse_down_pos = None

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

    def get_direction(self):
        return self.direction_class

    def redraw(self, surface):
        for row in self.grid:
            for field in row:
                field.toggle_needs_redraw()
                field.draw(surface)
