import pygame
from Button import Button
from GridContainer import GridContainer
from NextTurnButton import NextTurnButton

class Menu(GridContainer):
    buttons_amount = 3
    def __init__(self, pos: (int, int), size: (int, int), window):
        super(Menu, self).__init__(pos, size, (self.buttons_amount, 1))
        self.window = window
        self.createButtons()

    def createButtons(self):
        self.grid = [[]]
        self.grid[0].append(NextTurnButton(self.fieldSize, (self.fieldSize[0] * 0, 0), self.window))
        self.grid[0].append(SaveButton(self.fieldSize, (self.fieldSize[0] * 1, 0), "Save"))
        self.grid[0].append(LoadButton(self.fieldSize, (self.fieldSize[0] * 2, 0), "Load"))
