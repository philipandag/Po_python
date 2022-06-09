import pygame
from Button import Button
from GridContainer import GridContainer
from NextTurnButton import NextTurnButton
from WorldCreator import WorldCreator


class Menu(GridContainer):
    buttons_amount = 4
    def __init__(self, pos: (int, int), size: (int, int), window):
        super(Menu, self).__init__(pos, size, (self.buttons_amount, 1))
        self.window = window
        self.createButtons()

    def createButtons(self):
        self.grid = [[]]
        self.grid[0].append(Button(self.fieldSize, (self.fieldSize[0] * 0, 0), "Next turn").setOnClick(
            (lambda: self.window.get_world().next_turn())))
        self.grid[0].append(Button(self.fieldSize, (self.fieldSize[0] * 1, 0), "Save").setOnClick(
            (lambda: self.window.save_world())))
        self.grid[0].append(Button(self.fieldSize, (self.fieldSize[0] * 2, 0), "Load").setOnClick(
            (lambda: self.window.load_world())))
        self.grid[0].append(Button(self.fieldSize, (self.fieldSize[0] * 3, 0), "New Game").setOnClick(
            (lambda: WorldCreator(self.window))))

