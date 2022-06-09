from SquareBoard import SquareBoard
from Game import Game
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    game = Game((640, 640))
    game.create_world((5, 5), SquareBoard)
    game.main_loop()
