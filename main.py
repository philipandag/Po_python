from SquareBoard import SquareBoard
from HexBoard import HexBoard
from Game import Game
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    game = Game((640, 640))
    game.create_world((10, 10), HexBoard)
    game.main_loop()
