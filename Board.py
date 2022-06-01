import pygame

from Button import Button
from Field import Field
from GridContainer import GridContainer
from InterfaceElement import InterfaceElement
from Button import Button

class Board(GridContainer):

    def __init__(self, pos: (int, int), size: (int, int), dimensions: (int, int), world):
        super(Board, self).__init__(pos, size, dimensions)
        self.world = world
        self.createGrid()
        self.mouse_down_pos = None

    def createGrid(self):
        for row in range(self.dimensions[0]):
            for column in range(self.dimensions[1]):
                field_pos = (self.pos[0] + self.fieldSize[0] * row,
                             self.pos[1] + self.fieldSize[1] * column)

                self.grid[row][column] = Field(self.fieldSize, field_pos, (row, column), self.world)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down_pos = event.pos
        elif event.type == pygame.MOUSEMOTION:
            for x =
