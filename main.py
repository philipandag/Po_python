from Game import Game
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    game = Game((640, 640))
    game.create_world((20, 20))
    game.main_loop()
