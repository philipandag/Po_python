import pygame
import sys
from Board import Board
from InterfaceElement import InterfaceElement
from Menu import Menu
from World import World
from OrganismChooser import OrganismChooser
from Console import Console
import pickle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PADDING = 25



class Game:
    HANDLED_EVENTS = [pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]
    MENU_HEIGHT = 50
    CHOOSER_HEIGHT = 100
    SAVE_FILE ="save_file.save"

    def __init__(self, size: (int, int)):
        self.screen = pygame.display.set_mode((size[0], size[1]))
        pygame.display.set_caption('Filip Gołaś 188776')
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.components = []
        self.board = None
        self.world = None

        self.menuPos = (0, 0)
        self.menuSize = (self.screen.get_width(), self.MENU_HEIGHT)

        self.organismChooserSize = (self.screen.get_width(), self.CHOOSER_HEIGHT)
        self.organismChooserPos = (0, self.screen.get_height() - self.CHOOSER_HEIGHT)

        self.boardPos = (PADDING, self.menuSize[1] + PADDING)
        board_smallest_dimension = min(self.screen.get_width() - PADDING,
                                       self.screen.get_height() - self.menuSize[1] - 2*PADDING -
                                       self.organismChooserSize[1])
        self.boardSize = (board_smallest_dimension, board_smallest_dimension)

        self.menu = Menu(self.menuPos, self.menuSize, self)
        self.components.append(self.menu)

        self.organismChooser = OrganismChooser(self.organismChooserPos,
                                               self.organismChooserSize)
        self.components.append(self.organismChooser)

        self.next_turn_key_pressed = False
        self.screen.fill(WHITE)

    def quit(self):
        pygame.quit()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.next_turn_key_pressed = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            self.next_turn_key_pressed = False

        for listener in self.components:
            listener.handle_event(event)

        for listener in self.world.organism_listeners:
            listener.handle_event(event)

    def update(self):
        if self.next_turn_key_pressed:
            self.world.next_turn()
        for comp in self.components:
            comp.update()

    def draw(self, surface: pygame.Surface):
        #surface.fill(WHITE)
        for comp in self.components:
            comp.draw(surface)

    def main_loop(self):
        if self.board is None:
            print("Board not initialised")
            self.quit()
            return

        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type in Game.HANDLED_EVENTS:
                    self.handle_event(event)

            self.update()
            #self.screen.fill(BLACK)
            self.draw(self.screen)
            pygame.display.update()
            self.clock.tick(25)

        self.quit()

    def create_world(self, dimensions: (int, int)):
        self.world = World(self)
        self.board = Board((PADDING, self.menu.size[1] + PADDING),
                           self.boardSize,
                           dimensions, self.world)
        self.components.append(self.board)
        self.world.set_board(self.board)
        self.organismChooser.setWorld(self.world)

    def get_world(self):
        return self.world

    def save_world(self):
        file = open(self.SAVE_FILE, "w")
        pickle.Pickler(file, self.world)

    def load_world(self):
        file = open(self.SAVE_FILE, "r")
        world = pickle.load(file)
